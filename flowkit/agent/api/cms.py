"""CMS API — Authentication, Multi-Channel Studio, Video Generation Runner, Auto Episode Merger & Persistent Logs."""
import asyncio
import hashlib
import json
import logging
import os
import re
import secrets
import sys
from datetime import datetime, timezone
from typing import Optional

from fastapi import APIRouter, Header, HTTPException, Query
from fastapi.responses import FileResponse
from pydantic import BaseModel

from agent.db.schema import get_db
from agent.services.event_bus import event_bus
from agent.services.r2_storage import detect_media_info, normalize_r2_media_url

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/cms", tags=["cms"])

FLOWKIT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WORKSPACE_DIR = os.path.dirname(FLOWKIT_DIR)
RUNNERS_DIR = os.path.join(FLOWKIT_DIR, "runners")
if RUNNERS_DIR not in sys.path:
    sys.path.insert(0, RUNNERS_DIR)

try:
    from runners.cms_integration import merge_episode_clips, probe_video_duration
except ImportError:
    from cms_integration import merge_episode_clips, probe_video_duration  # type: ignore[no-redef]

# In-memory registry of active runner subprocesses per channel_slug
ACTIVE_JOBS: dict[str, dict] = {}

DEFAULT_CHANNELS = [
    {
        "slug": "mit-va-du-1970",
        "name": "Mít Và Đú 1970",
        "project_id": "234b0e61-f736-4e77-a1d9-527b2fadc582",
        "aspect_ratio": "VIDEO_ASPECT_RATIO_PORTRAIT",
        "runner_script": "runners/mit_va_du.py",
        "series_dir": "mit-va-du-1970",
        "ep_prefix": "tap",
        "description": "Gia đình chó nhân hóa Mít, Đú và bé Nở tại miền Tây Việt Nam năm 1970 (3D Pixar 9:16).",
        "characters": [
            {
                "tag": "@Mit",
                "name": "Mít (Chồng ~35 tuổi)",
                "default_media_id": "50cf224b-1304-4320-8896-4b4d599d2056",
                "description": "Chó đực lông vàng nâu nhân hóa đi hai chân, mõm và ngực trắng kem, mặc áo ba lỗ xám bạc màu và quần đùi tối màu.",
            },
            {
                "tag": "@Đú",
                "name": "Đú (Vợ ~30 tuổi)",
                "default_media_id": "44114803-92e4-48fb-ac9b-377a6c7c1cd2",
                "description": "Chó cái lông vàng kem nhân hóa đi hai chân, mõm trắng có vệt lông trắng dọc sống mũi, mặc áo bà ba hồng nhạt in hoa nhỏ.",
            },
            {
                "tag": "@Nở",
                "name": "Nở (Chó con 6 tuổi)",
                "default_media_id": "43579677-48b3-4d74-88e9-61b88aa07dd3",
                "description": "Chó con dễ thương nhân hóa đi hai chân, cao ngang bụng Mít, lông kem mềm có mảng nâu nhạt trên tai cụp, mặc áo vàng nhạt in hoa nhỏ và chân váy nâu.",
            },
        ],
    },
    {
        "slug": "365ngayvietnam",
        "name": "365 Ngày Việt Nam",
        "project_id": "bda4ab8d-725c-4e3c-aa82-ac806c877623",
        "aspect_ratio": "VIDEO_ASPECT_RATIO_PORTRAIT",
        "runner_script": "runners/365ngayvietnam.py",
        "series_dir": "365ngayvietnam",
        "ep_prefix": "tap",
        "description": "Hành trình du lịch trải nghiệm xuyên Việt 365 ngày từ Cực Bắc đến Cực Nam của cặp đôi Vy và Joi (9:16).",
        "characters": [
            {
                "tag": "@Vy",
                "name": "Vy (24 tuổi)",
                "default_media_id": "a83313e8-8d7b-4f5e-922f-a4cf4af625f1",
                "description": "Cô gái Việt Nam nhỏ nhắn 1m60, mặt trái xoan, má lúm đồng tiền bên phải, tóc đen dài buộc đuôi ngựa thấp.",
            },
            {
                "tag": "@Joi",
                "name": "Joi (28 tuổi)",
                "default_media_id": "9fc5f6b0-8d74-4a8f-9193-5f81ef6a28fa",
                "description": "Chàng trai Châu Âu cao 1m83, tóc nâu hạt dẻ gợn sóng, mắt xanh xám ấm áp, râu quai nón gọn gàng.",
            },
        ],
    },
    {
        "slug": "me-va-be",
        "name": "Mẹ Và Bé — Ngọc & Gạo, Bông",
        "project_id": "8df089b2-ac8f-4d21-9063-97d565697d04",
        "aspect_ratio": "VIDEO_ASPECT_RATIO_PORTRAIT",
        "runner_script": "runners/me_va_be.py",
        "series_dir": "me-va-be",
        "ep_prefix": "tap",
        "description": "Mẹ trẻ Ngọc 27 tuổi chăm sóc cặp song sinh Gạo và Bông trong căn phòng trọ ấm áp ở Sài Gòn (9:16).",
        "characters": [
            {
                "tag": "@Ngọc",
                "name": "Mẹ Ngọc (27 tuổi)",
                "default_media_id": "1ec03c5b-36c4-4dab-8513-3cb0c578c045",
                "description": "Người mẹ trẻ Việt Nam dịu dàng, nốt ruồi nhỏ dưới đuôi mắt trái, mặc pijama cotton màu be kem.",
            },
            {
                "tag": "@Gạo",
                "name": "Bé Gạo (Song sinh trai)",
                "default_media_id": "f0382828-7753-4268-813a-465bb65b883d",
                "description": "Bé trai bụ bẫm má phính, chỏm tóc đen dựng đứng như mầm cây, mặc bodysuit xanh bạc hà thêu gấu nhỏ.",
            },
            {
                "tag": "@Bông",
                "name": "Bé Bông (Song sinh gái)",
                "default_media_id": "63cb2de9-78cf-4f55-ab4a-d7d2e1b3f1cd",
                "description": "Bé gái má bầu bĩnh trắng hồng, mi dài cong, mặc bodysuit hồng phấn thêu dâu nhỏ và đội mũ tai thỏ.",
            },
        ],
    },
    {
        "slug": "pheo-va-no-meo",
        "name": "365 Ngày Phèo Làm Nội Trợ",
        "project_id": "d98ffa3b-7797-47c5-87be-55bb0e2a73f8",
        "aspect_ratio": "VIDEO_ASPECT_RATIO_PORTRAIT",
        "runner_script": "runners/pheo_va_no_meo.py",
        "series_dir": "pheo-va-no-meo",
        "ep_prefix": "tap",
        "description": "Chú mèo đen mập Phèo trổ tài nấu ăn mỗi ngày cho bà chủ Hường đanh đá (3D Pixar 9:16).",
        "characters": [
            {
                "tag": "@Pheo",
                "name": "Mèo Phèo (Đầu bếp)",
                "default_media_id": "af7d8804-5203-4364-b47e-cd30f20bf0fe",
                "description": "Mèo đen mập tròn nhân hóa đi hai chân, ngực có mảng lông trắng nhỏ, tai trái khuyết chữ V, đội mũ đầu bếp và tạp dề xanh navy.",
            },
            {
                "tag": "@No",
                "name": "Bà Chủ Hường / Nở",
                "default_media_id": "b25ca9d3-5643-4eac-badc-7fef900ca3c6",
                "description": "Cô chó Pomeranian lông xù màu kem cam nhân hóa, mặc đồ bộ lụa hồng cánh sen, đeo vòng ngọc trai.",
            },
            {
                "tag": "@My",
                "name": "Mèo Mỹ",
                "default_media_id": "cd039e3c-4d00-44ba-8a2f-c8240ff45f52",
                "description": "Cô mèo trắng sang chảnh nhân hóa đi hai chân, mắt xanh ngọc.",
            },
            {
                "tag": "@MèoTrẻ",
                "name": "Mèo Trẻ",
                "default_media_id": "9bd95545-60c2-4920-b327-55b36338014b",
                "description": "Chú mèo con năng động nhân hóa đi hai chân.",
            },
        ],
    },
    {
        "slug": "tay-du-ky-2026",
        "name": "Tây Du Ký 2026",
        "project_id": "5a1c26fe-7edc-42e3-b927-09e16e8f481d",
        "aspect_ratio": "VIDEO_ASPECT_RATIO_PORTRAIT",
        "runner_script": "runners/tay_du_ky.py",
        "series_dir": "tay-du-ky-2026",
        "ep_prefix": "tap",
        "description": "Drama đời thường hài hước của 4 thầy trò Đường Tăng thuê nhà trọ hẻm Sài Gòn 2026 (9:16).",
        "characters": [
            {
                "tag": "@Thay",
                "name": "Thầy (Đường Tăng)",
                "default_media_id": "ad0c12d2-83a3-46df-a61c-c97f150c1fd1",
                "description": "Nhà sư trẻ tuấn tú hiền lành, mặc áo cà sa cam nghệ và đeo chuỗi hạt gỗ.",
            },
            {
                "tag": "@DaiCa",
                "name": "Đại Ca (Ngộ Không)",
                "default_media_id": "34619eb9-7c90-4337-87c0-8375e53f4e3d",
                "description": "Chàng khỉ nhân hóa lanh lẹ, đeo vòng kim cô vàng, mặc áo bomber đỏ và quần jogger đen.",
            },
            {
                "tag": "@HeoLuoi",
                "name": "Heo Lười (Bát Giới)",
                "default_media_id": "e556190e-4c69-464c-b081-cd1b87a39135",
                "description": "Chàng heo nhân hóa mập tròn vui tính, mặc áo sơ mi khoác ngoài xanh navy.",
            },
            {
                "tag": "@UtKho",
                "name": "Út Khờ (Sa Tăng)",
                "default_media_id": "34b98c88-ca70-463a-bd23-128c4d405b38",
                "description": "Chàng trai to lớn thật thà, râu quai nón dày, đeo chuỗi hạt to và mặc tạp dề xanh rêu.",
            },
        ],
    },
    {
        "slug": "biet-doi-gara",
        "name": "Biệt Đội Gara",
        "project_id": "30714c49-2878-439b-a46f-c52be6eee2fc",
        "aspect_ratio": "VIDEO_ASPECT_RATIO_LANDSCAPE",
        "runner_script": "runners/biet_doi_gara.py",
        "series_dir": "biet-doi-gara",
        "ep_prefix": "canh",
        "description": "Biệt đội thợ máy Sài Gòn khám phá thiết bị công nghệ và bảo vệ bức thư quan trọng (16:9).",
        "characters": [
            {
                "tag": "@Thang",
                "name": "Thắng (Đội trưởng)",
                "default_media_id": "34755276-5033-4491-9dd8-cafc9539ee33",
                "description": "Đội trưởng thợ máy 36 tuổi điềm đạm, sẹo mảnh đuôi mày phải, đồng phục thợ máy xanh navy.",
            },
            {
                "tag": "@Lan",
                "name": "Lan (Nữ tay đua)",
                "default_media_id": "02ab9cff-aa83-4f36-af5e-7e2e19f1a7c4",
                "description": "Nữ thợ độ xe 29 tuổi cá tính, tóc đuôi ngựa cao, áo khoác biker da đen.",
            },
            {
                "tag": "@Hai",
                "name": "Hải (Thợ gầm bệ)",
                "default_media_id": "fa9044dc-ee57-4999-bcf5-57280a966964",
                "description": "Thợ máy 32 tuổi to khỏe vui tính, mặc áo ba lỗ xám và quần yếm bảo hộ.",
            },
            {
                "tag": "@Khoi",
                "name": "Khôi (IT Gara)",
                "default_media_id": "9221b0ff-b52e-4dbe-a31e-8dbec19fe492",
                "description": "Chuyên gia điện tử 24 tuổi đeo kính gọng mảnh, mặc hoodie xám phối khoác xanh rêu.",
            },
            {
                "tag": "@Minh",
                "name": "Minh (Đặc vụ)",
                "default_media_id": "72e13276-31ce-434b-bc19-25db0ff754be",
                "description": "Nhân vật phản diện lịch lãm mặc vest đen.",
            },
        ],
    },
    {
        "slug": "ke-song-sot",
        "name": "Kẻ Sống Sót: Bóng Ma",
        "project_id": "0aac1598-f1d9-4de2-84e8-9a5c0edb1df8",
        "aspect_ratio": "VIDEO_ASPECT_RATIO_LANDSCAPE",
        "runner_script": "runners/ke_song_sot.py",
        "series_dir": "ke-song-sot",
        "ep_prefix": "canh",
        "description": "Phim hành động tâm lý neo-noir 60 phút: sát thủ bị đường dây phản bội trốn về thị trấn biển, bảy ngày để phơi bày sổ đen; nữ trưởng công an thị trấn và lọ thuốc gây liệt (16:9, 60 cảnh × 6 clip).",
        "characters": [
            {
                "tag": "@Son",
                "name": "Sơn (Bóng Ma)",
                "default_media_id": "28356180-dea1-4c6c-bd80-8c3a41106957",
                "locked_media_id": "28356180-dea1-4c6c-bd80-8c3a41106957",
                "description": "Sát thủ 45 tuổi, tóc bạc hai bên, sẹo ngang sống mũi, dây đồng hồ quả quýt, áo khoác dã chiến ô liu (hiện tại) / vest đen găng da (quá khứ). Nghe hết, nói ít, giọng nam miền Nam trầm khô.",
                "ref_prompt": "Full-body photorealistic character reference of @Son, a 45-year-old Vietnamese man, 176 cm, lean and quiet, cropped black hair greying at the temples, weathered calm face, a thin old white scar across the bridge of his nose, a silver pocket-watch chain on his belt, faded olive field jacket over a grey shirt, dark trousers, worn brown boots; plain grey studio background, hard side light, 8K. Not resembling any real actor.",
            },
            {
                "tag": "@May",
                "name": "Đại úy Mây",
                "default_media_id": "b210621a-c403-42cb-94d5-8c0024496843",
                "locked_media_id": "b210621a-c403-42cb-94d5-8c0024496843",
                "description": "Trưởng công an thị trấn 38 tuổi, tóc ngắn lọn bạc phía trước, sơ mi kaki, còng ở thắt lưng. Thẳng thắn, sắc sảo, giữ luật bằng hai cái còng.",
                "ref_prompt": "Full-body photorealistic character reference of @May, a 38-year-old Vietnamese woman, 166 cm, athletic, sun-lined face, sharp warm eyes, short black hair with a single white streak at the front, plain khaki shirt with sleeves rolled, dark trousers, canvas shoes, a notebook in her chest pocket, handcuffs on her belt, no insignia; plain grey studio background, 8K.",
            },
            {
                "tag": "@Ha",
                "name": "Hạ (Tiệm hoa)",
                "default_media_id": "61e353d9-8e8a-48b1-934e-2f466ab87d09",
                "locked_media_id": "61e353d9-8e8a-48b1-934e-2f466ab87d09",
                "description": "Cô chủ tiệm hoa 32 tuổi, tóc dài, khăn lụa xanh nhạt, đầm lanh kem, tạp dề xanh. Dịu dàng nhưng kiên cường, khắc vạch đếm ngày chờ Sơn.",
                "ref_prompt": "Full-body photorealistic character reference of @Ha, a 32-year-old Vietnamese woman, 162 cm, slim, gentle bright face, long black hair tied loosely, a pale-blue silk scarf in her hair, cream linen dress, green canvas florist apron, flat sandals, holding white lily stems; plain grey studio background, soft warm light, 8K.",
            },
            {
                "tag": "@HaiNgoc",
                "name": "Bà Hai Ngọc (Rắn Đen)",
                "default_media_id": "ff423460-c3ce-4d3f-8c4b-f74d2a657a2f",
                "locked_media_id": "ff423460-c3ce-4d3f-8c4b-f74d2a657a2f",
                "description": "Trùm đường dây 60 tuổi, búi tóc bạc, vòng ngọc tay trái, tẩu đen, áo bà ba lụa tím. Ngọt ngào, chậm rãi, thực dụng tuyệt đối.",
                "ref_prompt": "Full-body photorealistic character reference of @HaiNgoc, a small upright 60-year-old Vietnamese woman, 158 cm, silver hair in a tight bun, powdered calm face, a thick jade bracelet on her left wrist, a long black cigarette holder, violet silk áo bà ba with a high collar, black silk trousers, embroidered slippers; plain grey studio background, 8K.",
            },
            {
                "tag": "@Dũng",
                "name": "Dũng 'Đinh' (Rắn Đen)",
                "default_media_id": "29967c42-6378-4e6e-a656-101fbda18b0b",
                "locked_media_id": "29967c42-6378-4e6e-a656-101fbda18b0b",
                "description": "Tay sai số một của Rắn Đen (35 tuổi), cao 180 cm, đầu đinh, khuyên tai bạc hình đinh ở tai trái, áo ba lỗ đen, bao súng luôn đóng. Ồn ào, nóng nảy.",
                "ref_prompt": "Full-body photorealistic reference of a heavy-shouldered 35-year-old Vietnamese man, 180 cm, buzz cut, a small nail-shaped silver earring in his left ear, black sleeveless shirt, black jeans, boots, a closed leather holster, arms crossed, loud confident face; plain grey background, 8K, not resembling any real actor.",
            },
            {
                "tag": "@Vũ Kiên",
                "name": "Vũ Kiên (Người Môi Giới)",
                "default_media_id": "cb559421-6180-43b2-bf78-ecc674c3b698",
                "locked_media_id": "cb559421-6180-43b2-bf78-ecc674c3b698",
                "description": "Doanh nhân 50 tuổi, tóc đen vuốt, vest trắng, đồng hồ vàng, nụ cười chính khách không bao giờ tắt, quen giết người bằng tay kẻ khác.",
                "ref_prompt": "Full-body photorealistic reference of a tall 50-year-old Vietnamese man with slicked black hair, a white tailored suit, white shirt, gold wristwatch, polished shoes, a wide politician's smile, one hand raised in greeting; plain grey background, 8K, not resembling any real actor.",
            },
            {
                "tag": "@Phó Thành",
                "name": "Phó Thành (Phó công an)",
                "default_media_id": "80289d04-f26d-4ac0-892b-5515509ea1fb",
                "locked_media_id": "80289d04-f26d-4ac0-892b-5515509ea1fb",
                "description": "Phó công an 26 tuổi của Mây, gầy, kính tròn, sơ mi xanh nhạt, không phù hiệu. Nhiệt tình, lễ phép, giỏi máy tính.",
                "ref_prompt": "Full-body photorealistic reference of a skinny 26-year-old Vietnamese man with round glasses, neat side-parted hair, plain light-blue shirt, dark trousers, sneakers, holding a phone and a notebook, eager nervous face; plain grey background, 8K.",
            },
            {
                "tag": "@Bác sĩ Linh",
                "name": "Bác sĩ Linh",
                "default_media_id": "d51873af-f5d5-48cd-844e-7d6fc9bf99a7",
                "locked_media_id": "d51873af-f5d5-48cd-844e-7d6fc9bf99a7",
                "description": "Bác sĩ thị trấn 55 tuổi, gầy, tóc bạc, kính gọng thép, áo blouse trắng sờn, ống nghe, cầm đồng hồ bấm giờ. Trầm, chính xác.",
                "ref_prompt": "Full-body photorealistic reference of a thin 55-year-old Vietnamese man, grey hair, wire glasses, worn white coat over a checked shirt, stethoscope, holding a small stopwatch, tired precise face; plain grey background, 8K.",
            },
            {
                "tag": "@Ông Bảy",
                "name": "Ông Bảy (Quán bờ kè)",
                "default_media_id": "eefba81d-07c5-42a5-bfe3-11bc176c6d4c",
                "locked_media_id": "eefba81d-07c5-42a5-bfe3-11bc176c6d4c",
                "description": "Chủ quán cà phê bờ kè 70 tuổi, mập, ria bạc, áo ba lỗ trắng, quần đùi, nón lá, luôn cầm khăn lau ly. Hào sảng, bảo vệ người lạ.",
                "ref_prompt": "Full-body photorealistic reference of a stout 70-year-old Vietnamese man with a white moustache, white singlet, shorts, rubber sandals, conical hat pushed back, wiping a glass with a rag, cheerful face; plain grey background, 8K.",
            },
        ],
    },
]


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")


def _hash_password(password: str, salt: str = "flowkit_cms_2026") -> str:
    return hashlib.sha256(f"{salt}:{password}".encode("utf-8")).hexdigest()


_CMS_SEEDED = False


async def ensure_cms_seeded():
    """Ensure default admin user and series channels exist in SQLite (runs once per process)."""
    global _CMS_SEEDED
    if _CMS_SEEDED:
        return
    db = await get_db()
    now = _now_iso()

    col_cur = await db.execute("PRAGMA table_info(cms_channel)")
    cols = {r[1] for r in await col_cur.fetchall()}
    if "ep_prefix" not in cols:
        await db.execute("ALTER TABLE cms_channel ADD COLUMN ep_prefix TEXT NOT NULL DEFAULT 'tap'")
        await db.commit()

    await db.executescript(
        """
        CREATE TABLE IF NOT EXISTS cms_episode (
            id                TEXT PRIMARY KEY,
            channel_slug      TEXT NOT NULL,
            project_id        TEXT,
            episode_num       INTEGER NOT NULL,
            folder_name       TEXT NOT NULL,
            label             TEXT,
            total_clips       INTEGER NOT NULL DEFAULT 0,
            rendered_clips    INTEGER NOT NULL DEFAULT 0,
            is_complete       INTEGER NOT NULL DEFAULT 0,
            merged_local_path TEXT,
            merged_r2_key     TEXT,
            merged_r2_url     TEXT,
            merged_size_mb    REAL,
            duration_s        REAL,
            updated_at        TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now'))
        );
        CREATE INDEX IF NOT EXISTS idx_cms_episode_channel ON cms_episode(channel_slug, episode_num);

        CREATE TABLE IF NOT EXISTS cms_clip (
            id                TEXT PRIMARY KEY,
            channel_slug      TEXT NOT NULL,
            project_id        TEXT,
            episode_num       INTEGER NOT NULL,
            folder_name       TEXT NOT NULL,
            clip_num          INTEGER NOT NULL,
            prompt            TEXT,
            status            TEXT NOT NULL DEFAULT 'PENDING',
            local_path        TEXT,
            r2_key            TEXT,
            r2_url            TEXT,
            frame_local_path  TEXT,
            frame_r2_key      TEXT,
            frame_r2_url      TEXT,
            size_mb           REAL,
            duration_s        REAL,
            media_id          TEXT,
            updated_at        TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now'))
        );
        CREATE INDEX IF NOT EXISTS idx_cms_clip_channel_ep ON cms_clip(channel_slug, episode_num, clip_num);
        """
    )

    # 1. Seed default admin user (admin / admin123)
    cur = await db.execute("SELECT id FROM cms_user WHERE username = ?", ("admin",))
    if not await cur.fetchone():
        await db.execute(
            "INSERT INTO cms_user (id, username, password_hash, display_name, role, created_at) VALUES (?, ?, ?, ?, ?, ?)",
            ("admin-1", "admin", _hash_password("admin123"), "Quản Trị Viên FlowKit", "admin", now),
        )

    # 2. Seed channels & remove deprecated channels
    await db.execute("DELETE FROM cms_channel WHERE slug = ?", ("mai-hoa-thung",))
    await db.execute("DELETE FROM cms_episode WHERE channel_slug = ?", ("mai-hoa-thung",))
    await db.execute("DELETE FROM cms_clip WHERE channel_slug = ?", ("mai-hoa-thung",))

    for ch in DEFAULT_CHANNELS:
        cur = await db.execute("SELECT slug, project_id, characters_json FROM cms_channel WHERE slug = ?", (ch["slug"],))
        existing_row = await cur.fetchone()
        if not existing_row:
            await db.execute(
                """INSERT INTO cms_channel
                   (slug, name, project_id, aspect_ratio, runner_script, series_dir, ep_prefix, description, characters_json, updated_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    ch["slug"],
                    ch["name"],
                    ch["project_id"],
                    ch["aspect_ratio"],
                    ch["runner_script"],
                    ch["series_dir"],
                    ch["ep_prefix"],
                    ch["description"],
                    json.dumps(ch["characters"], ensure_ascii=False),
                    now,
                ),
            )
        else:
            ex = dict(existing_row)
            # Auto-sync project_id from runner script or DEFAULT_CHANNELS if empty in DB
            runner_pid = ch["project_id"]
            runner_abs = os.path.join(FLOWKIT_DIR, ch["runner_script"])
            if os.path.isfile(runner_abs):
                try:
                    with open(runner_abs, "r", encoding="utf-8") as rf:
                        m_pid = re.search(r'^PROJECT_ID\s*=\s*"([^"]+)"', rf.read(), flags=re.MULTILINE)
                        if m_pid and m_pid.group(1).strip():
                            runner_pid = m_pid.group(1).strip()
                except Exception:
                    pass
            if runner_pid and not (ex.get("project_id") or "").strip():
                await db.execute(
                    "UPDATE cms_channel SET project_id = ?, characters_json = ?, updated_at = ? WHERE slug = ?",
                    (runner_pid, json.dumps(ch["characters"], ensure_ascii=False), now, ch["slug"]),
                )
    await db.commit()
    _CMS_SEEDED = True


async def record_cms_log(
    channel_slug: str = "system",
    level: str = "INFO",
    category: str = "CMS",
    message: str = "",
    project_id: Optional[str] = None,
    episode: Optional[int] = None,
    clip_num: Optional[int] = None,
    details: Optional[dict] = None,
) -> dict:
    """Insert a log entry into cms_log and broadcast via WebSocket event_bus."""
    db = await get_db()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    details_str = json.dumps(details, ensure_ascii=False) if details else None
    cur = await db.execute(
        """INSERT INTO cms_log
           (channel_slug, project_id, episode, clip_num, level, category, message, details_json, created_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (channel_slug, project_id, episode, clip_num, level.upper(), category, message, details_str, now),
    )
    await db.commit()
    log_item = {
        "id": cur.lastrowid,
        "channel_slug": channel_slug,
        "project_id": project_id,
        "episode": episode,
        "clip_num": clip_num,
        "level": level.upper(),
        "category": category,
        "message": message,
        "details": details,
        "created_at": now,
    }
    await event_bus.emit("cms_log", log_item)
    return log_item


async def get_current_user(
    authorization: Optional[str] = Header(default=None),
    x_cms_token: Optional[str] = Header(default=None),
) -> Optional[dict]:
    token = None
    if authorization and authorization.lower().startswith("bearer "):
        token = authorization[7:].strip()
    elif x_cms_token:
        token = x_cms_token.strip()
    if not token:
        return None
    db = await get_db()
    cur = await db.execute(
        """SELECT u.id, u.username, u.display_name, u.role, s.token
           FROM cms_session s
           JOIN cms_user u ON u.id = s.user_id
           WHERE s.token = ?""",
        (token,),
    )
    row = await cur.fetchone()
    if not row:
        return None
    return dict(row)


# ─── Auth Models & Endpoints ─────────────────────────────────


class LoginRequest(BaseModel):
    username: str
    password: str


class ChangePasswordRequest(BaseModel):
    current_password: str
    new_password: str
    display_name: Optional[str] = None


@router.post("/auth/login")
async def cms_login(body: LoginRequest):
    await ensure_cms_seeded()
    db = await get_db()
    cur = await db.execute(
        "SELECT id, username, password_hash, display_name, role FROM cms_user WHERE username = ?",
        (body.username.strip(),),
    )
    user = await cur.fetchone()
    if not user or user["password_hash"] != _hash_password(body.password):
        await record_cms_log("system", "WARN", "AUTH", f"Đăng nhập thất bại cho tài khoản '{body.username}'")
        raise HTTPException(status_code=401, detail="Tên đăng nhập hoặc mật khẩu không đúng!")

    token = secrets.token_urlsafe(32)
    now = _now_iso()
    await db.execute(
        "INSERT INTO cms_session (token, user_id, created_at, expires_at) VALUES (?, ?, ?, ?)",
        (token, user["id"], now, "2099-12-31 23:59:59"),
    )
    await db.commit()
    await record_cms_log("system", "SUCCESS", "AUTH", f"Người dùng '{user['username']}' đã đăng nhập vào CMS.")
    return {
        "ok": True,
        "token": token,
        "user": {
            "id": user["id"],
            "username": user["username"],
            "display_name": user["display_name"],
            "role": user["role"],
        },
    }


@router.post("/auth/logout")
async def cms_logout(
    authorization: Optional[str] = Header(default=None),
    x_cms_token: Optional[str] = Header(default=None),
):
    user = await get_current_user(authorization, x_cms_token)
    if user:
        db = await get_db()
        await db.execute("DELETE FROM cms_session WHERE token = ?", (user["token"],))
        await db.commit()
        await record_cms_log("system", "INFO", "AUTH", f"Người dùng '{user['username']}' đã đăng xuất.")
    return {"ok": True}


@router.get("/auth/me")
async def cms_me(
    authorization: Optional[str] = Header(default=None),
    x_cms_token: Optional[str] = Header(default=None),
):
    await ensure_cms_seeded()
    user = await get_current_user(authorization, x_cms_token)
    if not user:
        raise HTTPException(status_code=401, detail="Chưa đăng nhập hoặc phiên đã hết hạn.")
    return {"ok": True, "user": user}


@router.post("/auth/change-password")
async def cms_change_password(
    body: ChangePasswordRequest,
    authorization: Optional[str] = Header(default=None),
    x_cms_token: Optional[str] = Header(default=None),
):
    user = await get_current_user(authorization, x_cms_token)
    if not user:
        raise HTTPException(status_code=401, detail="Chưa đăng nhập.")
    db = await get_db()
    cur = await db.execute("SELECT password_hash FROM cms_user WHERE id = ?", (user["id"],))
    row = await cur.fetchone()
    if not row or row["password_hash"] != _hash_password(body.current_password):
        raise HTTPException(status_code=400, detail="Mật khẩu hiện tại không chính xác.")
    new_hash = _hash_password(body.new_password)
    new_name = (body.display_name or user["display_name"]).strip()
    await db.execute(
        "UPDATE cms_user SET password_hash = ?, display_name = ? WHERE id = ?",
        (new_hash, new_name, user["id"]),
    )
    await db.commit()
    await record_cms_log("system", "SUCCESS", "AUTH", f"Tài khoản '{user['username']}' đã cập nhật mật khẩu.")
    return {"ok": True, "display_name": new_name}


# ─── Filesystem Scanning Helpers for Channels & Episodes ─────


def _extract_ep_number(folder_name: str, prefix: str) -> Optional[int]:
    """Parse episode number from folder names like tap-1, tap-16, tap1-ha-giang, canh-03."""
    m = re.match(rf"^{prefix}-?(\d+)(?:-.*)?$", folder_name, re.IGNORECASE)
    if m:
        return int(m.group(1))
    return None


def _media_url_for_path(abs_path: str) -> Optional[str]:
    if not abs_path or not os.path.isfile(abs_path):
        return None
    rel = os.path.relpath(abs_path, WORKSPACE_DIR)
    if rel.startswith(".."):
        return None
    try:
        mtime = int(os.path.getmtime(abs_path))
    except OSError:
        mtime = 0
    return f"/api/cms/media?path={rel}&v={mtime}"


def _find_clip_video_file(series_abs_dir: str, ep_num: int, ep_folder_name: str, clip_num: int) -> Optional[str]:
    ep_out_dir = os.path.join(series_abs_dir, "output_videos", ep_folder_name)
    alt_dirs = [
        ep_out_dir,
        os.path.join(series_abs_dir, "output_videos", f"tap-{ep_num:02d}"),
        os.path.join(series_abs_dir, "output_videos", f"tap-{ep_num}"),
        os.path.join(series_abs_dir, "output_videos", f"canh-{ep_num:02d}"),
    ]
    patterns = [
        f"tap-{ep_num:02d}_clip-{clip_num:02d}.mp4",
        f"tap-{ep_num}_clip-{clip_num}.mp4",
        f"canh-{ep_num:02d}_clip-{clip_num:02d}.mp4",
        f"TDK_T{ep_num:02d}_C{clip_num:02d}.mp4",
    ]
    for d in alt_dirs:
        if not os.path.isdir(d):
            continue
        for pat in patterns:
            cand = os.path.join(d, pat)
            if os.path.isfile(cand) and os.path.getsize(cand) > 0:
                return cand
        for fname in os.listdir(d):
            if not fname.endswith(".mp4") or "FULL" in fname:
                continue
            m = re.search(r"(?:clip-|_C)(\d+)\.mp4$", fname, re.IGNORECASE)
            if m and int(m.group(1)) == clip_num:
                cand = os.path.join(d, fname)
                if os.path.getsize(cand) > 0:
                    return cand
    return None


def _find_clip_frame_file(series_abs_dir: str, ep_num: int, clip_num: int) -> Optional[str]:
    frames_dir = os.path.join(series_abs_dir, "exported_frames")
    for fname in (
        f"tap_{ep_num:02d}_clip_{clip_num:02d}_last.jpg",
        f"scene_{ep_num:02d}_clip_{clip_num:02d}_last.jpg",
    ):
        cand = os.path.join(frames_dir, fname)
        if os.path.isfile(cand) and os.path.getsize(cand) > 0:
            return cand
    return None


def _find_merged_episode_file(series_abs_dir: str, channel_slug: str, ep_num: int, ep_folder_name: str) -> Optional[str]:
    full_names = [
        f"{channel_slug}_tap-{ep_num:02d}_FULL.mp4",
        f"{channel_slug}_canh-{ep_num:02d}_FULL.mp4",
        f"{channel_slug}_tap-{ep_num}_FULL.mp4",
    ]
    for full_name in full_names:
        candidates = [
            os.path.join(series_abs_dir, "output_videos", ep_folder_name, full_name),
            os.path.join(series_abs_dir, "output_videos", "full_episodes", full_name),
            os.path.join(series_abs_dir, "output_videos", f"tap-{ep_num:02d}", full_name),
            os.path.join(series_abs_dir, "output_videos", f"canh-{ep_num:02d}", full_name),
            os.path.join(series_abs_dir, "output_videos", full_name),
        ]
        for c in candidates:
            if os.path.isfile(c) and os.path.getsize(c) > 0:
                return c
    return None


def _scan_channel_episodes(
    channel_row: dict,
    include_prompts: bool = False,
    db_episodes_map: Optional[dict[int, dict]] = None,
    db_clips_map: Optional[dict[tuple[int, int], dict]] = None,
) -> list[dict]:
    series_abs_dir = os.path.join(WORKSPACE_DIR, channel_row["series_dir"])
    ep_prefix = channel_row.get("ep_prefix") or "tap"
    slug = channel_row["slug"]
    ep_map = db_episodes_map or {}
    clip_map = db_clips_map or {}

    ep_dirs: dict[int, str] = {}
    if os.path.isdir(series_abs_dir):
        for entry in sorted(os.listdir(series_abs_dir)):
            full_p = os.path.join(series_abs_dir, entry)
            if not os.path.isdir(full_p):
                continue
            ep_num = _extract_ep_number(entry, ep_prefix)
            if ep_num is not None:
                if ep_num not in ep_dirs or len(entry) > len(os.path.basename(ep_dirs[ep_num])):
                    ep_dirs[ep_num] = full_p

    # Tổng số tập dựa trên cả folder thực tế trên ổ cứng và các tập đã đồng bộ R2 / SQLite
    all_ep_nums = sorted(set(ep_dirs.keys()) | set(ep_map.keys()))
    episodes = []
    for ep_num in all_ep_nums:
        db_ep = ep_map.get(ep_num) or {}
        ep_dir = ep_dirs.get(ep_num)
        ep_folder_name = os.path.basename(ep_dir) if ep_dir else (db_ep.get("folder_name") or f"{ep_prefix}-{ep_num:02d}")
        clip_files: dict[int, str] = {}
        if ep_dir and os.path.isdir(ep_dir):
            for fname in os.listdir(ep_dir):
                m = re.match(r"^clip-(\d+)\.md$", fname)
                if m:
                    clip_files[int(m.group(1))] = os.path.join(ep_dir, fname)

        db_clip_nums = {c_num for (e_n, c_num) in clip_map.keys() if e_n == ep_num}
        all_clip_nums = sorted(set(clip_files.keys()) | db_clip_nums)

        clips_data = []
        rendered_count = 0
        r2_synced_clips = 0
        for c_num in all_clip_nums:
            c_path = clip_files.get(c_num)
            db_clip = clip_map.get((ep_num, c_num)) or {}
            v_file = _find_clip_video_file(series_abs_dir, ep_num, ep_folder_name, c_num) if os.path.isdir(series_abs_dir) else None
            f_file = _find_clip_frame_file(series_abs_dir, ep_num, c_num) if os.path.isdir(series_abs_dir) else None
            r2_key = db_clip.get("r2_key")
            raw_r2_url = db_clip.get("r2_url")
            r2_url = normalize_r2_media_url(raw_r2_url, r2_key, default_category="episodes") if (raw_r2_url or r2_key) else None
            raw_frame_r2_url = db_clip.get("frame_r2_url")
            frame_r2_key = db_clip.get("frame_r2_key")
            frame_r2_url = normalize_r2_media_url(raw_frame_r2_url, frame_r2_key, default_category="frames") if (raw_frame_r2_url or frame_r2_key) else None
            if r2_url:
                r2_synced_clips += 1

            is_done = bool(v_file or r2_url or db_clip.get("status") == "COMPLETED" or db_ep.get("is_complete"))
            if is_done:
                rendered_count += 1

            prompt_text = ""
            if include_prompts and c_path and os.path.isfile(c_path):
                try:
                    with open(c_path, "r", encoding="utf-8") as f:
                        prompt_text = f.read()
                except Exception:
                    prompt_text = ""
            if not prompt_text and db_clip.get("prompt"):
                prompt_text = db_clip["prompt"] if include_prompts else db_clip["prompt"][:240]

            local_media_url = _media_url_for_path(v_file)
            local_frame_url = _media_url_for_path(f_file)
            size_mb = round(os.path.getsize(v_file) / (1024 * 1024), 2) if v_file else db_clip.get("size_mb")
            eff_video_url = local_media_url or r2_url
            v_media_info = detect_media_info(v_file or r2_url or r2_key or "clip.mp4", default_category="episodes")
            f_media_info = detect_media_info(f_file or frame_r2_url or frame_r2_key or "frame.jpg", default_category="frames")

            clips_data.append(
                {
                    "clip_num": c_num,
                    "file_name": os.path.basename(c_path) if c_path else f"clip-{c_num}.md",
                    "file_path": c_path or "",
                    "prompt": prompt_text,
                    "status": "COMPLETED" if is_done else "PENDING",
                    "video_url": eff_video_url,
                    "r2_url": r2_url,
                    "r2_key": r2_key,
                    "media_kind": v_media_info["media_kind"],
                    "media_type": v_media_info["mime_type"],
                    "video_size_mb": size_mb,
                    "frame_url": local_frame_url or frame_r2_url,
                    "frame_r2_url": frame_r2_url,
                    "frame_media_type": f_media_info["mime_type"],
                }
            )

        merged_file = _find_merged_episode_file(series_abs_dir, slug, ep_num, ep_folder_name) if os.path.isdir(series_abs_dir) else None
        merged_local_url = _media_url_for_path(merged_file)
        merged_r2_key = db_ep.get("merged_r2_key")
        raw_merged_r2_url = db_ep.get("merged_r2_url")
        merged_r2_url = (
            normalize_r2_media_url(raw_merged_r2_url, merged_r2_key, default_category="full_episodes")
            if (raw_merged_r2_url or merged_r2_key)
            else None
        )
        merged_size = round(os.path.getsize(merged_file) / (1024 * 1024), 2) if merged_file else db_ep.get("merged_size_mb")
        m_media_info = detect_media_info(merged_file or merged_r2_url or merged_r2_key or "full.mp4", default_category="full_episodes")

        episodes.append(
            {
                "episode_num": ep_num,
                "folder_name": ep_folder_name,
                "label": db_ep.get("label") or f"{'Cảnh' if ep_prefix == 'canh' else 'Tập'} {ep_num:02d}",
                "total_clips": len(clips_data) if len(clips_data) > 0 else int(db_ep.get("total_clips") or 0),
                "rendered_clips": rendered_count if len(clips_data) > 0 else int(db_ep.get("rendered_clips") or 0),
                "r2_synced_clips": r2_synced_clips,
                "is_complete": bool(db_ep.get("is_complete")) or (len(clips_data) > 0 and rendered_count == len(clips_data)),
                "merged_video_url": merged_local_url or merged_r2_url,
                "merged_r2_url": merged_r2_url,
                "merged_r2_key": merged_r2_key,
                "merged_media_kind": m_media_info["media_kind"],
                "merged_media_type": m_media_info["mime_type"],
                "merged_video_path": merged_file or db_ep.get("merged_local_path"),
                "merged_size_mb": merged_size,
                "clips": clips_data,
            }
        )

    return episodes


async def _load_channel_db_maps(db, slug: str) -> tuple[dict[int, dict], dict[tuple[int, int], dict]]:
    ep_map: dict[int, dict] = {}
    clip_map: dict[tuple[int, int], dict] = {}
    try:
        ep_cur = await db.execute("SELECT * FROM cms_episode WHERE channel_slug = ?", (slug,))
        for r in await ep_cur.fetchall():
            d = dict(r)
            ep_n = int(d["episode_num"])
            if ep_n not in ep_map:
                ep_map[ep_n] = d
            else:
                prev = ep_map[ep_n]
                for k, v in d.items():
                    if v is not None and v != "" and (prev.get(k) is None or prev.get(k) == ""):
                        prev[k] = v
                if d.get("is_complete"):
                    prev["is_complete"] = 1
                prev["rendered_clips"] = max(int(prev.get("rendered_clips") or 0), int(d.get("rendered_clips") or 0))
    except Exception:
        pass
    try:
        cl_cur = await db.execute("SELECT * FROM cms_clip WHERE channel_slug = ?", (slug,))
        for r in await cl_cur.fetchall():
            d = dict(r)
            key = (int(d["episode_num"]), int(d["clip_num"]))
            if key not in clip_map:
                clip_map[key] = d
            else:
                prev = clip_map[key]
                for k, v in d.items():
                    if v is not None and v != "" and (prev.get(k) is None or prev.get(k) == ""):
                        prev[k] = v
                if d.get("status") == "COMPLETED":
                    prev["status"] = "COMPLETED"
    except Exception:
        pass
    # Backfill from cms_log (category = 'R2_UPLOAD') in case any R2 link was logged before DB sync
    try:
        lg_cur = await db.execute(
            "SELECT episode, clip_num, details_json FROM cms_log WHERE channel_slug = ? AND category = 'R2_UPLOAD' ORDER BY id ASC",
            (slug,),
        )
        for lr in await lg_cur.fetchall():
            ld = dict(lr)
            ep_n = ld.get("episode")
            cl_n = ld.get("clip_num")
            if ep_n is None:
                continue
            try:
                det = json.loads(ld.get("details_json") or "{}")
            except Exception:
                det = {}
            r2_u = det.get("r2_url")
            r2_k = det.get("r2_key")
            if not r2_u:
                continue
            if cl_n is not None:
                key = (int(ep_n), int(cl_n))
                entry = clip_map.setdefault(key, {"episode_num": int(ep_n), "clip_num": int(cl_n), "status": "COMPLETED"})
                entry["r2_url"] = r2_u
                entry["r2_key"] = r2_k or entry.get("r2_key")
                entry["size_mb"] = det.get("size_mb") or entry.get("size_mb")
                entry["status"] = "COMPLETED"
            else:
                entry = ep_map.setdefault(int(ep_n), {"episode_num": int(ep_n), "is_complete": 1})
                entry["merged_r2_url"] = r2_u
                entry["merged_r2_key"] = r2_k or entry.get("merged_r2_key")
                entry["merged_size_mb"] = det.get("size_mb") or entry.get("merged_size_mb")
    except Exception:
        pass
    return ep_map, clip_map


def _load_locked_character_ids(channel_row: dict) -> list[dict]:
    chars = []
    try:
        chars = json.loads(channel_row.get("characters_json") or "[]")
    except Exception:
        chars = []
    series_abs_dir = os.path.join(WORKSPACE_DIR, channel_row["series_dir"])
    cache_path = os.path.join(series_abs_dir, "character_refs", "character_media_ids.json")
    project_cache = {}
    if os.path.isfile(cache_path):
        try:
            with open(cache_path, "r", encoding="utf-8") as f:
                raw = json.load(f)
                if isinstance(raw, dict):
                    project_cache = raw.get(channel_row["project_id"]) or {}
        except Exception:
            project_cache = {}

    enriched = []
    for c in chars:
        tag = c.get("tag", "")
        mid = project_cache.get(tag) or c.get("default_media_id")
        enriched.append({**c, "locked_media_id": mid})
    return enriched


# ─── Channels & Episodes Endpoints ───────────────────────────


@router.get("/channels")
async def list_cms_channels():
    await ensure_cms_seeded()
    db = await get_db()
    cur = await db.execute("SELECT * FROM cms_channel ORDER BY rowid ASC")
    rows = [dict(r) for r in await cur.fetchall()]

    result = []
    for row in rows:
        slug = row["slug"]
        ep_map, clip_map = await _load_channel_db_maps(db, slug)
        episodes = _scan_channel_episodes(row, include_prompts=False, db_episodes_map=ep_map, db_clips_map=clip_map)
        total_eps = len(episodes)
        total_clips = sum(ep["total_clips"] for ep in episodes)
        rendered_clips = sum(ep["rendered_clips"] for ep in episodes)
        r2_clips = sum(ep.get("r2_synced_clips", 0) for ep in episodes)
        merged_eps = sum(1 for ep in episodes if ep.get("merged_video_url") or ep.get("is_complete"))
        r2_merged_eps = sum(1 for ep in episodes if ep.get("merged_r2_url"))
        job = ACTIVE_JOBS.get(slug)

        log_cur = await db.execute(
            "SELECT level, category, message, created_at FROM cms_log WHERE channel_slug = ? ORDER BY id DESC LIMIT 1",
            (slug,),
        )
        latest_log = await log_cur.fetchone()

        result.append(
            {
                "slug": slug,
                "name": row["name"],
                "project_id": row["project_id"],
                "aspect_ratio": row["aspect_ratio"],
                "runner_script": row["runner_script"],
                "series_dir": row["series_dir"],
                "ep_prefix": row["ep_prefix"],
                "description": row["description"],
                "characters": _load_locked_character_ids(row),
                "stats": {
                    "total_episodes": total_eps,
                    "completed_episodes": merged_eps,
                    "total_clips": total_clips,
                    "rendered_clips": rendered_clips,
                    "r2_synced_clips": r2_clips,
                    "merged_episodes": merged_eps,
                    "r2_merged_episodes": r2_merged_eps,
                },
                "active_job": (
                    {
                        "running": job["running"],
                        "pid": job.get("pid"),
                        "start_ep": job.get("start_ep"),
                        "end_ep": job.get("end_ep"),
                        "only_clip": job.get("only_clip"),
                        "started_at": job.get("started_at"),
                    }
                    if job and job.get("running")
                    else None
                ),
                "latest_log": dict(latest_log) if latest_log else None,
            }
        )
    return {"channels": result}


@router.get("/channels/{slug}")
async def get_cms_channel_detail(slug: str):
    await ensure_cms_seeded()
    db = await get_db()
    cur = await db.execute("SELECT * FROM cms_channel WHERE slug = ?", (slug,))
    row = await cur.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Không tìm thấy kênh '{slug}'")
    row_dict = dict(row)
    ep_map, clip_map = await _load_channel_db_maps(db, slug)
    episodes = _scan_channel_episodes(row_dict, include_prompts=True, db_episodes_map=ep_map, db_clips_map=clip_map)
    job = ACTIVE_JOBS.get(slug)
    return {
        "channel": {
            "slug": row_dict["slug"],
            "name": row_dict["name"],
            "project_id": row_dict["project_id"],
            "aspect_ratio": row_dict["aspect_ratio"],
            "runner_script": row_dict["runner_script"],
            "series_dir": row_dict["series_dir"],
            "ep_prefix": row_dict["ep_prefix"],
            "description": row_dict["description"],
            "characters": _load_locked_character_ids(row_dict),
            "active_job": (
                {
                    "running": job["running"],
                    "pid": job.get("pid"),
                    "start_ep": job.get("start_ep"),
                    "end_ep": job.get("end_ep"),
                    "only_clip": job.get("only_clip"),
                    "started_at": job.get("started_at"),
                }
                if job and job.get("running")
                else None
            ),
        },
        "episodes": episodes,
    }


@router.get("/gallery")
async def get_cms_gallery(channel_slug: Optional[str] = None):
    """Return all rendered media files (Full Episodes, Scene Clips, Frames/Images, Audio) across CMS channels with exact format & MIME metadata."""
    await ensure_cms_seeded()
    filter_slug = channel_slug.strip() if isinstance(channel_slug, str) and channel_slug.strip() else None
    db = await get_db()
    cur = await db.execute("SELECT * FROM cms_channel ORDER BY rowid ASC")
    rows = [dict(r) for r in await cur.fetchall()]

    channels_out = []
    items_out = []

    for row in rows:
        slug = row["slug"]
        ch_name = row["name"]
        aspect_ratio = row["aspect_ratio"]
        ep_prefix = row.get("ep_prefix") or "tap"
        ep_map, clip_map = await _load_channel_db_maps(db, slug)
        episodes = _scan_channel_episodes(row, include_prompts=False, db_episodes_map=ep_map, db_clips_map=clip_map)

        ch_full_count = 0
        ch_clip_count = 0
        ch_image_count = 0
        seen_urls: set[str] = set()

        for ep in episodes:
            ep_num = ep["episode_num"]
            ep_label = ep["label"]
            folder_name = ep["folder_name"]

            # 1. Full Episode video (.mp4)
            merged_url = ep.get("merged_r2_url") or ep.get("merged_video_url")
            if merged_url:
                ch_full_count += 1
                seen_urls.add(merged_url)
                if not filter_slug or filter_slug in ("ALL", slug):
                    m_info = detect_media_info(merged_url, default_category="full_episodes")
                    fname = (
                        os.path.basename(ep.get("merged_r2_key") or ep.get("merged_video_path") or "")
                        or f"{slug}_{ep_prefix}-{ep_num:02d}_FULL{m_info['ext']}"
                    )
                    items_out.append(
                        {
                            "id": f"{slug}:full:{ep_num}",
                            "channel_slug": slug,
                            "channel_name": ch_name,
                            "aspect_ratio": aspect_ratio,
                            "episode_num": ep_num,
                            "episode_label": ep_label,
                            "folder_name": folder_name,
                            "clip_num": None,
                            "category": "full_episode",
                            "title": f"{ep_label} — Tập Hoàn Chỉnh (FULL)",
                            "file_name": fname,
                            "url": merged_url,
                            "r2_url": ep.get("merged_r2_url"),
                            "r2_key": ep.get("merged_r2_key"),
                            "media_kind": m_info["media_kind"],
                            "media_type": m_info["mime_type"],
                            "ext": m_info["ext"].lstrip(".").upper(),
                            "size_mb": ep.get("merged_size_mb"),
                            "prompt_preview": f"Bản ghép hoàn chỉnh {ep_label} ({ep.get('total_clips', 0)} clips)",
                        }
                    )

            # 2. Individual Clips (.mp4) & Frames (.jpg/.png)
            for cl in ep.get("clips", []):
                c_num = cl["clip_num"]
                c_url = cl.get("r2_url") or cl.get("video_url")
                if c_url:
                    ch_clip_count += 1
                    seen_urls.add(c_url)
                    if not filter_slug or filter_slug in ("ALL", slug):
                        c_info = detect_media_info(c_url, default_category="episodes")
                        c_fname = (
                            os.path.basename(cl.get("r2_key") or "")
                            or f"{ep_prefix}-{ep_num:02d}_clip-{c_num:02d}{c_info['ext']}"
                        )
                        items_out.append(
                            {
                                "id": f"{slug}:clip:{ep_num}:{c_num}",
                                "channel_slug": slug,
                                "channel_name": ch_name,
                                "aspect_ratio": aspect_ratio,
                                "episode_num": ep_num,
                                "episode_label": ep_label,
                                "folder_name": folder_name,
                                "clip_num": c_num,
                                "category": "clip",
                                "title": f"{ep_label} • Clip {c_num:02d}",
                                "file_name": c_fname,
                                "url": c_url,
                                "r2_url": cl.get("r2_url"),
                                "r2_key": cl.get("r2_key"),
                                "thumbnail_url": cl.get("frame_r2_url") or cl.get("frame_url"),
                                "media_kind": c_info["media_kind"],
                                "media_type": c_info["mime_type"],
                                "ext": c_info["ext"].lstrip(".").upper(),
                                "size_mb": cl.get("video_size_mb"),
                                "prompt_preview": (cl.get("prompt") or "")[:180],
                            }
                        )

                f_url = cl.get("frame_r2_url") or cl.get("frame_url")
                if f_url:
                    ch_image_count += 1
                    seen_urls.add(f_url)
                    if not filter_slug or filter_slug in ("ALL", slug):
                        f_info = detect_media_info(f_url, default_category="frames")
                        f_fname = f"{ep_prefix}_{ep_num:02d}_clip_{c_num:02d}_last{f_info['ext']}"
                        items_out.append(
                            {
                                "id": f"{slug}:frame:{ep_num}:{c_num}",
                                "channel_slug": slug,
                                "channel_name": ch_name,
                                "aspect_ratio": aspect_ratio,
                                "episode_num": ep_num,
                                "episode_label": ep_label,
                                "folder_name": folder_name,
                                "clip_num": c_num,
                                "category": "frame",
                                "title": f"{ep_label} • Frame Cuối Clip {c_num:02d}",
                                "file_name": f_fname,
                                "url": f_url,
                                "r2_url": cl.get("frame_r2_url"),
                                "r2_key": None,
                                "media_kind": f_info["media_kind"],
                                "media_type": f_info["mime_type"],
                                "ext": f_info["ext"].lstrip(".").upper(),
                                "size_mb": None,
                                "prompt_preview": f"Khung hình nối cảnh cuối cùng của {ep_label} - Clip {c_num:02d}",
                            }
                        )

        # 3. Also scan exported_frames / character_refs on disk for any standalone images
        series_abs_dir = os.path.join(WORKSPACE_DIR, row["series_dir"])
        for sub_dir, sub_cat in (("exported_frames", "frame"), ("character_refs", "frame")):
            abs_sub = os.path.join(series_abs_dir, sub_dir)
            if not os.path.isdir(abs_sub):
                continue
            for fn in sorted(os.listdir(abs_sub)):
                if not fn.lower().endswith((".jpg", ".jpeg", ".png", ".webp", ".gif", ".mp4", ".webm", ".mp3", ".wav")):
                    continue
                abs_f = os.path.join(abs_sub, fn)
                if not os.path.isfile(abs_f):
                    continue
                m_url = _media_url_for_path(abs_f)
                if not m_url or m_url in seen_urls:
                    continue
                seen_urls.add(m_url)
                f_info = detect_media_info(abs_f, default_category="frames")
                if f_info["media_kind"] == "image":
                    ch_image_count += 1
                else:
                    ch_clip_count += 1
                if not filter_slug or filter_slug in ("ALL", slug):
                    sz = round(os.path.getsize(abs_f) / (1024 * 1024), 2)
                    items_out.append(
                        {
                            "id": f"{slug}:{sub_dir}:{fn}",
                            "channel_slug": slug,
                            "channel_name": ch_name,
                            "aspect_ratio": aspect_ratio,
                            "episode_num": 0,
                            "episode_label": "Tài Nguyên",
                            "folder_name": sub_dir,
                            "clip_num": None,
                            "category": sub_cat,
                            "title": fn,
                            "file_name": fn,
                            "url": m_url,
                            "r2_url": None,
                            "r2_key": None,
                            "media_kind": f_info["media_kind"],
                            "media_type": f_info["mime_type"],
                            "ext": f_info["ext"].lstrip(".").upper(),
                            "size_mb": sz,
                            "prompt_preview": f"Tệp media lưu tại {sub_dir}/{fn}",
                        }
                    )

        channels_out.append(
            {
                "slug": slug,
                "name": ch_name,
                "aspect_ratio": aspect_ratio,
                "ep_prefix": ep_prefix,
                "description": row["description"],
                "full_episodes_count": ch_full_count,
                "clips_count": ch_clip_count,
                "images_count": ch_image_count,
                "total_media_count": ch_full_count + ch_clip_count + ch_image_count,
            }
        )

    return {
        "channels": channels_out,
        "items": items_out,
        "total_items": len(items_out),
    }


class UpdateChannelRequest(BaseModel):
    name: Optional[str] = None
    project_id: Optional[str] = None
    aspect_ratio: Optional[str] = None
    description: Optional[str] = None


@router.patch("/channels/{slug}")
async def update_cms_channel(slug: str, body: UpdateChannelRequest):
    await ensure_cms_seeded()
    db = await get_db()
    cur = await db.execute("SELECT * FROM cms_channel WHERE slug = ?", (slug,))
    row = await cur.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Không tìm thấy kênh '{slug}'")
    row_dict = dict(row)

    new_name = body.name.strip() if body.name else row_dict["name"]
    new_pid = body.project_id.strip() if body.project_id else row_dict["project_id"]
    new_ar = body.aspect_ratio.strip() if body.aspect_ratio else row_dict["aspect_ratio"]
    new_desc = body.description.strip() if body.description is not None else row_dict["description"]

    await db.execute(
        """UPDATE cms_channel
           SET name = ?, project_id = ?, aspect_ratio = ?, description = ?, updated_at = ?
           WHERE slug = ?""",
        (new_name, new_pid, new_ar, new_desc, _now_iso(), slug),
    )
    await db.commit()

    # Sync PROJECT_ID and ASPECT_RATIO directly into runner script file
    runner_abs = os.path.join(FLOWKIT_DIR, row_dict["runner_script"])
    if os.path.isfile(runner_abs):
        try:
            with open(runner_abs, "r", encoding="utf-8") as f:
                code = f.read()
            code = re.sub(r'^PROJECT_ID\s*=\s*"[^"]*"', f'PROJECT_ID = "{new_pid}"', code, count=1, flags=re.MULTILINE)
            code = re.sub(r'^ASPECT_RATIO\s*=\s*"[^"]*"', f'ASPECT_RATIO = "{new_ar}"', code, count=1, flags=re.MULTILINE)
            with open(runner_abs, "w", encoding="utf-8") as f:
                f.write(code)
        except Exception as e:
            logger.warning("Failed to update runner script %s: %s", runner_abs, e)

    await record_cms_log(
        slug,
        "SUCCESS",
        "CONFIG",
        f"Đã cập nhật cấu hình kênh '{new_name}' (PROJECT_ID={new_pid}, ASPECT_RATIO={new_ar})",
        project_id=new_pid,
    )
    return {"ok": True, "slug": slug, "project_id": new_pid, "aspect_ratio": new_ar}


@router.post("/channels/{slug}/auto-lock-characters")
async def auto_lock_cms_channel_characters(slug: str, force_regenerate: bool = False):
    """Tự động kết nối Google Flow Project của kênh, kiểm tra hoặc tạo mới ảnh tham chiếu cho toàn bộ nhân vật (@Tag) và khóa cố định media_id."""
    import agent.services.flow_batch as fb
    from agent.services.flow_client import get_flow_client

    await ensure_cms_seeded()
    db = await get_db()
    cur = await db.execute("SELECT * FROM cms_channel WHERE slug = ?", (slug,))
    row = await cur.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Không tìm thấy kênh '{slug}'")
    row_dict = dict(row)

    project_id = (row_dict.get("project_id") or "").strip()
    runner_abs = os.path.join(FLOWKIT_DIR, row_dict["runner_script"])
    if not project_id and os.path.isfile(runner_abs):
        try:
            with open(runner_abs, "r", encoding="utf-8") as rf:
                m_pid = re.search(r'^PROJECT_ID\s*=\s*"([^"]+)"', rf.read(), flags=re.MULTILINE)
                if m_pid and m_pid.group(1).strip():
                    project_id = m_pid.group(1).strip()
        except Exception:
            pass

    if not project_id:
        raise HTTPException(status_code=400, detail=f"Kênh '{slug}' chưa có PROJECT_ID Google Flow.")

    chars = []
    try:
        chars = json.loads(row_dict.get("characters_json") or "[]")
    except Exception:
        chars = []

    default_ch = next((c for c in DEFAULT_CHANNELS if c["slug"] == slug), None)
    default_prompts = {
        c["tag"]: c.get("ref_prompt", "")
        for c in (default_ch.get("characters", []) if default_ch else [])
    }

    series_abs_dir = os.path.join(WORKSPACE_DIR, row_dict["series_dir"])
    char_refs_dir = os.path.join(series_abs_dir, "character_refs")
    os.makedirs(char_refs_dir, exist_ok=True)
    cache_path = os.path.join(char_refs_dir, "character_media_ids.json")

    cached_by_project = {}
    if os.path.isfile(cache_path):
        try:
            with open(cache_path, "r", encoding="utf-8") as f:
                cached_by_project = json.load(f)
        except Exception:
            cached_by_project = {}
    project_cache = cached_by_project.get(project_id, {}) if isinstance(cached_by_project, dict) else {}

    client = get_flow_client()
    remote_chars = []
    remote_images = []
    if client.connected:
        try:
            res = await client.batch_rpc(
                fb.RPC_PROJECT_MEDIA, fb.project_media_request(project_id), match=None, timeout=45
            )
            raw = res.get("data") or ""
            if raw:
                payload = fb.first_payload(raw, fb.RPC_PROJECT_MEDIA)
                if isinstance(payload, list):
                    raw_chars = payload[5] if len(payload) > 5 and isinstance(payload[5], list) else []
                    for ch in raw_chars:
                        if isinstance(ch, list) and len(ch) >= 5:
                            meta = ch[3] if isinstance(ch[3], list) else []
                            cname = meta[1] if len(meta) > 1 and isinstance(meta[1], str) else ""
                            cmid = ch[4] if isinstance(ch[4], str) else None
                            if cname and cmid:
                                remote_chars.append({"name": cname, "media_id": cmid})
                    items = payload[1] if len(payload) > 1 and isinstance(payload[1], list) else []
                    for it in items:
                        if isinstance(it, list) and len(it) >= 4 and isinstance(it[3], list):
                            det = it[3]
                            title = det[0] if len(det) > 0 and isinstance(det[0], str) else ""
                            is_vid = bool(det[2]) if len(det) > 2 else False
                            imid = det[4] if len(det) > 4 and isinstance(det[4], str) else None
                            if not is_vid and imid:
                                remote_images.append({"title": title, "media_id": imid})
        except Exception as e:
            logger.warning("Failed to query remote Flow project media for %s: %s", project_id, e)

    locked_map: dict[str, str] = {}
    created_now: list[str] = []
    updated_chars = []

    for c in chars:
        tag = c.get("tag", "")
        name = c.get("name", tag)
        tag_clean = tag.lower().lstrip("@")
        name_clean = name.lower().split("(")[0].strip()
        matched_mid = None

        for rc in remote_chars:
            rc_clean = rc["name"].strip().lower().lstrip("@")
            if rc_clean == tag_clean or rc_clean == name_clean:
                matched_mid = rc["media_id"]
                break

        if not matched_mid and not force_regenerate:
            matched_mid = project_cache.get(tag) or c.get("default_media_id") or None

        ref_prompt = (
            c.get("ref_prompt")
            or default_prompts.get(tag)
            or f"Full-body character reference of {tag} ({name}): {c.get('description', '')}. Plain studio background, 8K."
        )

        if matched_mid:
            locked_map[tag] = matched_mid
            c["default_media_id"] = matched_mid
            c["locked_media_id"] = matched_mid
        else:
            c["default_media_id"] = ""
            c["locked_media_id"] = ""
        if ref_prompt:
            c["ref_prompt"] = ref_prompt
        updated_chars.append(c)

    # Save to character_media_ids.json
    if not isinstance(cached_by_project, dict):
        cached_by_project = {}
    cached_by_project[project_id] = {**project_cache, **locked_map}
    try:
        with open(cache_path, "w", encoding="utf-8") as f:
            json.dump(cached_by_project, f, ensure_ascii=False, indent=2)
    except Exception as e:
        logger.warning("Failed to write %s: %s", cache_path, e)

    # Update cms_channel in SQLite
    await db.execute(
        "UPDATE cms_channel SET project_id = ?, characters_json = ?, updated_at = ? WHERE slug = ?",
        (project_id, json.dumps(updated_chars, ensure_ascii=False), _now_iso(), slug),
    )
    await db.commit()

    # Sync locked default_media_id into runner script (e.g., runners/ke_song_sot.py)
    if os.path.isfile(runner_abs) and locked_map:
        try:
            with open(runner_abs, "r", encoding="utf-8") as rf:
                rcode = rf.read()
            for tag, mid in locked_map.items():
                pattern = rf'("tag":\s*"{re.escape(tag)}"[\s\S]*?"default_media_id":\s*)"[^"]*"'
                rcode = re.sub(pattern, rf'\1"{mid}"', rcode, count=1)
            with open(runner_abs, "w", encoding="utf-8") as rf:
                rf.write(rcode)
        except Exception as e:
            logger.warning("Failed to update default_media_id in %s: %s", runner_abs, e)

    await record_cms_log(
        slug,
        "SUCCESS" if len(locked_map) == len(chars) else "WARN",
        "CHAR_LOCK",
        f"🔒 Đã đồng bộ & khóa {len(locked_map)}/{len(chars)} nhân vật trên Project {project_id} (Tạo mới: {', '.join(created_now) if created_now else '0'}).",
        project_id=project_id,
        details={"locked": locked_map, "created": created_now, "extension_connected": client.connected},
    )

    return {
        "ok": True,
        "slug": slug,
        "project_id": project_id,
        "extension_connected": client.connected,
        "locked_count": len(locked_map),
        "total_characters": len(chars),
        "created_now": created_now,
        "locked_media_ids": locked_map,
        "characters": updated_chars,
    }


class GeneratePromptsRequest(BaseModel):
    episode_num: int
    clip_count: int = 5
    story_idea: Optional[str] = None
    setting: Optional[str] = None
    scene_beats: Optional[list[str]] = None


class CreateEpisodeRequest(BaseModel):
    episode_num: int
    clip_count: int = 5
    folder_suffix: Optional[str] = None
    story_idea: Optional[str] = None
    setting: Optional[str] = None
    scene_beats: Optional[list[str]] = None
    clip_prompts: Optional[list[str]] = None
    overwrite: bool = True


def _build_structured_episode_prompts(
    row_dict: dict,
    chars: list[dict],
    episode_num: int,
    clip_count: int,
    story_idea: str = "",
    setting: str = "",
    scene_beats: Optional[list[str]] = None,
) -> list[str]:
    """Generate structured cinema-grade prompts for Clip 1..N with locked character anchors."""
    slug = row_dict["slug"]
    is_portrait = "PORTRAIT" in row_dict["aspect_ratio"]
    ar_text = "Vertical 9:16" if is_portrait else "Widescreen 16:9"
    char_tags = " ".join(c["tag"] for c in chars)

    if slug == "mit-va-du-1970":
        world_format = (
            f"{ar_text}, 10-second clip, high-end 3D animated film, Pixar/Disney-quality stylized CGI, "
            "soft global illumination, shallow depth of field, 24fps, cinematic color grade. "
            "Era and place: rural Mekong Delta / Vietnamese countryside, 1970. Warm nostalgic palette of honey gold, "
            "rice-paddy green and earth brown, subtle 35mm film grain. Every character in this world is a cute "
            "anthropomorphic 3D dog who stands and walks upright on two legs and has furry paw-hands with four fingers; "
            "no humans exist. Spoken dialogue in Vietnamese with a natural Southern Vietnamese accent and accurate lip-sync. "
            "Cut only where the shot list says. No subtitles, no captions, no on-screen text, no logos, no watermark."
        )
        default_setting = (
            "FRONT YARD OF THE BAMBOO HUT: a swept dirt yard in front of the small bamboo hut with its nipa-palm thatch roof "
            "and bamboo door, a large brown clay water jar beside the door, a narrow canal along the yard with a small wooden "
            "xuồng ba lá boat tied to a post, tall coconut palms leaning over the water in warm golden sunlight."
        )
        avoid_line = (
            "humans, human faces, human child, human hands, quadrupedal non-anthropomorphic dogs, pointed upright ears, "
            "scary teeth, modern plastic objects, readable letters or numbers anywhere, subtitles, captions, watermark, "
            "extra characters, outfit changes, distorted paws or extra fingers."
        )
    elif slug == "ke-song-sot":
        world_format = (
            "Widescreen 16:9 (2.39:1 anamorphic ratio), 10-second clip, photorealistic live-action neo-noir crime thriller "
            "film style set in a small Vietnamese seaside town (Hòn Sóng) and a big city at night. 24fps high-budget cinematography, "
            "crisp 90-degree shutter angle, razor-sharp motion. Bleached white-sun colour grade with cool shadows for the present day. "
            "No blood, no on-screen shooting. Dialogue in Vietnamese with natural Southern accent and lip-sync; first-person narration "
            "allowed as voice-over. No subtitles or on-screen text."
        )
        default_setting = (
            "HÒN SÓNG SEASIDE TOWN: weathered coastal streets, seafront coffee stall, florist shop, and wooden house on the casuarina hill "
            "under bleached coastal daylight and tense neo-noir atmosphere."
        )
        avoid_line = (
            "blood, gore, visible wounds, on-screen shooting, muzzle flashes, bullet hits on people, deaths on camera, torture, "
            "real brand logos, readable signs or documents, real police insignia, watermarks, text overlays, extra fingers, "
            "cartoon or anime look, likeness of any real actor."
        )
    else:
        world_format = (
            f"{ar_text}, 10-second clip, high-end 3D animated film, Pixar/DreamWorks-quality stylized CGI, "
            "soft global illumination, shallow depth of field, 24fps, cinematic color grade. "
            "Spoken dialogue in Vietnamese with natural expressive voice acting and accurate lip-sync. "
            "No subtitles, no captions, no on-screen text, no logos, no watermark."
        )
        default_setting = f"Bối cảnh đặc trưng của series {row_dict['name']}, ánh sáng điện ảnh ấm áp, chi tiết sống động."
        avoid_line = "subtitles, captions, watermark, readable text, extra limbs, outfit changes, sudden jump cuts."

    char_block_lines = []
    for c in chars:
        tag = c["tag"]
        name = c.get("name", tag)
        desc = c.get("description") or f"Nhân vật cố định {name}, khớp chính xác ảnh tham chiếu {tag}"
        char_block_lines.append(f"{tag} = {name} (exact match to {tag} reference image): {desc}")
    char_block = "\n".join(char_block_lines)

    final_setting = (setting or "").strip() or default_setting
    idea_text = (story_idea or "").strip() or f"Tình huống đời thường hài hước, đáng yêu của {char_tags} trong Tập {episode_num:02d}."

    default_beats = [
        f"Mở đầu tình huống: {char_tags} bắt đầu câu chuyện ({idea_text}) với biểu cảm hào hứng.",
        f"Phát triển tình huống: {char_tags} phối hợp hành động nhưng gặp một sự cố bất ngờ hài hước.",
        f"Cao trào vui nhộn: Cả nhóm {char_tags} xoay xở xử lý tình huống với biểu cảm sinh động.",
        f"Bước ngoặt đáng yêu: Một chi tiết bất ngờ khiến {char_tags} bật cười thích thú.",
        f"Kết thúc ấm áp: {char_tags} cùng nhau nhìn lại thành quả và cười rạng rỡ trong nắng ấm.",
    ]

    prompts: list[str] = []
    total = max(1, min(clip_count, 20))
    for idx in range(1, total + 1):
        beat = ""
        if scene_beats and idx - 1 < len(scene_beats) and scene_beats[idx - 1].strip():
            beat = scene_beats[idx - 1].strip()
        else:
            beat = default_beats[(idx - 1) % len(default_beats)]

        if idx == 1:
            p = (
                f"[FORMAT]\n{world_format}\n\n"
                f"[CHARACTERS — match the attached reference images {char_tags} exactly]\n"
                f"{char_block}\n\n"
                f"[SETTING]\n{final_setting}\n"
                f"Story context (Tập {episode_num:02d}): {idea_text}\n\n"
                f"[SHOT LIST]\n"
                f"00:00–00:03.5 | Medium wide establishing shot — {beat}\n"
                f"00:03.5–00:07 | Medium shot, dynamic camera — Các nhân vật {char_tags} tương tác trực tiếp với đạo cụ trong cảnh, cử chỉ tự nhiên và biểu cảm rõ nét.\n"
                f"00:07–00:10 | Medium close-up — Khoảnh khắc nhấn điểm hài hước/đáng yêu cuối cảnh 1 để chuẩn bị nối sang cảnh 2.\n\n"
                f"[SOUND]\n"
                f"Natural ambient background sounds, expressive foley matching movements, cheerful acoustic folk melody.\n\n"
                f"[END FRAME]\n"
                f"Medium shot in warm sunlight: {char_tags} in clear positions with expressive faces at the end of Clip 1. Hold still for the final 0.5 seconds.\n\n"
                f"[AVOID]\n{avoid_line}\n"
            )
        else:
            p = (
                f"Continue the scene seamlessly from the final frame of the previous clip, which is the first frame of this clip. "
                f"Same characters, same outfits, same location, same lighting and color grade. Flawless continuity, no time skip, no jump cut at the start.\n"
                f"{world_format}\n\n"
                f"[CHARACTERS — unchanged, match {char_tags} reference images]\n"
                f"{char_block}\n\n"
                f"[SHOT LIST — TẬP {episode_num:02d} CLIP {idx:02d}]\n"
                f"00:00–00:03.5 | Same medium shot, continuing seamlessly from the last frame of Clip {idx - 1} — {beat}\n"
                f"00:03.5–00:07 | Medium shot — Diễn biến tiếp nối mượt mà của {char_tags} trong bối cảnh ({final_setting}).\n"
                f"00:07–00:10 | Medium close-up — Biểu cảm đáng yêu của {char_tags} khép lại Clip {idx}.\n\n"
                f"[SOUND]\n"
                f"Seamless ambient audio continuation, lively foley effects, warm Vietnamese voice acting.\n\n"
                f"[END FRAME]\n"
                f"Medium shot: {char_tags} in a clear, balanced composition ready for seamless transition. Hold still for the final 0.5 seconds.\n\n"
                f"[AVOID]\n{avoid_line}\n"
            )
        prompts.append(p)
    return prompts


@router.post("/channels/{slug}/generate-prompts")
async def generate_cms_episode_prompts(slug: str, body: GeneratePromptsRequest):
    """Sinh tự động bộ kịch bản prompt chuẩn cho Tập mới (Clip 1..N) dựa trên cốt truyện & nhân vật khóa."""
    await ensure_cms_seeded()
    db = await get_db()
    cur = await db.execute("SELECT * FROM cms_channel WHERE slug = ?", (slug,))
    row = await cur.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Không tìm thấy kênh '{slug}'")
    row_dict = dict(row)
    chars = _load_locked_character_ids(row_dict)
    prompts = _build_structured_episode_prompts(
        row_dict=row_dict,
        chars=chars,
        episode_num=body.episode_num,
        clip_count=body.clip_count,
        story_idea=body.story_idea or "",
        setting=body.setting or "",
        scene_beats=body.scene_beats,
    )
    return {"ok": True, "episode_num": body.episode_num, "clip_count": len(prompts), "prompts": prompts}


@router.post("/channels/{slug}/episodes")
async def create_cms_episode(slug: str, body: CreateEpisodeRequest):
    await ensure_cms_seeded()
    db = await get_db()
    cur = await db.execute("SELECT * FROM cms_channel WHERE slug = ?", (slug,))
    row = await cur.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Không tìm thấy kênh '{slug}'")
    row_dict = dict(row)

    series_abs_dir = os.path.join(WORKSPACE_DIR, row_dict["series_dir"])
    ep_prefix = row_dict.get("ep_prefix") or "tap"
    folder_name = f"{ep_prefix}-{body.episode_num:02d}" if ep_prefix == "canh" else f"{ep_prefix}-{body.episode_num}"
    if body.folder_suffix:
        clean_suffix = re.sub(r"[^a-zA-Z0-9_-]", "-", body.folder_suffix.strip()).strip("-")
        if clean_suffix:
            folder_name = f"{folder_name}-{clean_suffix}"

    ep_dir = os.path.join(series_abs_dir, folder_name)
    os.makedirs(ep_dir, exist_ok=True)

    chars = _load_locked_character_ids(row_dict)
    total_clips = max(1, min(body.clip_count, 20))
    if body.clip_prompts and len(body.clip_prompts) > 0:
        prompts_to_write = body.clip_prompts
        total_clips = len(prompts_to_write)
    else:
        prompts_to_write = _build_structured_episode_prompts(
            row_dict=row_dict,
            chars=chars,
            episode_num=body.episode_num,
            clip_count=total_clips,
            story_idea=body.story_idea or "",
            setting=body.setting or "",
            scene_beats=body.scene_beats,
        )

    created_clips = []
    now = _now_iso()
    ep_id = f"{slug}:ep:{body.episode_num}"
    await db.execute(
        """INSERT OR REPLACE INTO cms_episode
           (id, channel_slug, project_id, episode_num, folder_name, label, total_clips, rendered_clips, is_complete, updated_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, 0, 0, ?)""",
        (
            ep_id,
            slug,
            row_dict["project_id"],
            body.episode_num,
            folder_name,
            f"{'Cảnh' if ep_prefix == 'canh' else 'Tập'} {body.episode_num:02d}",
            total_clips,
            now,
        ),
    )

    for c_idx in range(1, total_clips + 1):
        c_path = os.path.join(ep_dir, f"clip-{c_idx}.md")
        content = prompts_to_write[c_idx - 1]
        if body.overwrite or not os.path.exists(c_path):
            with open(c_path, "w", encoding="utf-8") as f:
                f.write(content)
        clip_id = f"{slug}:ep:{body.episode_num}:clip:{c_idx}"
        await db.execute(
            """INSERT OR REPLACE INTO cms_clip
               (id, channel_slug, project_id, episode_num, folder_name, clip_num, prompt, status, updated_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, 'PENDING', ?)""",
            (clip_id, slug, row_dict["project_id"], body.episode_num, folder_name, c_idx, content, now),
        )
        created_clips.append(c_idx)
    await db.commit()

    await record_cms_log(
        slug,
        "SUCCESS",
        "EPISODE",
        f"Đã khởi tạo & lưu kịch bản Tập {body.episode_num:02d} ({folder_name}) với {len(created_clips)} clips.",
        project_id=row_dict["project_id"],
        episode=body.episode_num,
    )
    return {"ok": True, "episode_num": body.episode_num, "folder_name": folder_name, "clips": created_clips}


class SaveClipPromptRequest(BaseModel):
    prompt: str


@router.put("/channels/{slug}/episodes/{ep_num}/clips/{clip_num}")
async def save_cms_clip_prompt(slug: str, ep_num: int, clip_num: int, body: SaveClipPromptRequest):
    await ensure_cms_seeded()
    db = await get_db()
    cur = await db.execute("SELECT * FROM cms_channel WHERE slug = ?", (slug,))
    row = await cur.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Không tìm thấy kênh '{slug}'")
    row_dict = dict(row)

    series_abs_dir = os.path.join(WORKSPACE_DIR, row_dict["series_dir"])
    ep_prefix = row_dict.get("ep_prefix") or "tap"

    # Find existing episode dir or create default
    target_ep_dir = None
    if os.path.isdir(series_abs_dir):
        for entry in sorted(os.listdir(series_abs_dir)):
            full_p = os.path.join(series_abs_dir, entry)
            if os.path.isdir(full_p) and _extract_ep_number(entry, ep_prefix) == ep_num:
                target_ep_dir = full_p
                break
    if not target_ep_dir:
        folder_name = f"{ep_prefix}-{ep_num:02d}" if ep_prefix == "canh" else f"{ep_prefix}-{ep_num}"
        target_ep_dir = os.path.join(series_abs_dir, folder_name)
        os.makedirs(target_ep_dir, exist_ok=True)

    clip_path = os.path.join(target_ep_dir, f"clip-{clip_num}.md")
    with open(clip_path, "w", encoding="utf-8") as f:
        f.write(body.prompt)

    ep_folder_name = os.path.basename(target_ep_dir)
    clip_id = f"{slug}:ep:{ep_num}:clip:{clip_num}"
    existing_cur = await db.execute("SELECT * FROM cms_clip WHERE id = ?", (clip_id,))
    existing_clip = await existing_cur.fetchone()
    if existing_clip:
        await db.execute(
            "UPDATE cms_clip SET prompt = ?, updated_at = ? WHERE id = ?",
            (body.prompt, _now_iso(), clip_id),
        )
    else:
        await db.execute(
            """INSERT INTO cms_clip
               (id, channel_slug, project_id, episode_num, folder_name, clip_num, prompt, status, updated_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, 'PENDING', ?)""",
            (clip_id, slug, row_dict["project_id"], ep_num, ep_folder_name, clip_num, body.prompt, _now_iso()),
        )
    await db.commit()

    await record_cms_log(
        slug,
        "INFO",
        "PROMPT",
        f"Đã lưu nội dung kịch bản Tập {ep_num:02d} - Clip {clip_num:02d} ({len(body.prompt)} ký tự).",
        project_id=row_dict["project_id"],
        episode=ep_num,
        clip_num=clip_num,
    )
    return {"ok": True, "clip_path": clip_path, "length": len(body.prompt)}


# ─── Episode Auto-Merger Endpoint ────────────────────────────


@router.post("/channels/{slug}/episodes/{ep_num}/merge")
async def merge_cms_episode(slug: str, ep_num: int):
    """Ghép toàn bộ các clip nhỏ của Tập `ep_num` thành 1 tập video hoàn chỉnh (.mp4)."""
    await ensure_cms_seeded()
    db = await get_db()
    cur = await db.execute("SELECT * FROM cms_channel WHERE slug = ?", (slug,))
    row = await cur.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Không tìm thấy kênh '{slug}'")
    row_dict = dict(row)

    series_abs_dir = os.path.join(WORKSPACE_DIR, row_dict["series_dir"])
    ep_prefix = row_dict.get("ep_prefix") or "tap"
    ep_folder_name = f"{ep_prefix}-{ep_num:02d}" if ep_prefix == "canh" else f"{ep_prefix}-{ep_num}"

    # Check if there is an existing episode folder in output_videos
    out_videos_dir = os.path.join(series_abs_dir, "output_videos")
    if os.path.isdir(out_videos_dir):
        for entry in sorted(os.listdir(out_videos_dir)):
            full_p = os.path.join(out_videos_dir, entry)
            if os.path.isdir(full_p) and _extract_ep_number(entry, ep_prefix) == ep_num:
                ep_folder_name = entry
                break

    loop = asyncio.get_running_loop()
    merge_res = await loop.run_in_executor(
        None,
        lambda: merge_episode_clips(
            series_dir=series_abs_dir,
            channel_slug=slug,
            ep_num=ep_num,
            ep_folder_name=ep_folder_name,
            project_id=row_dict["project_id"],
        ),
    )

    if not merge_res.get("ok"):
        raise HTTPException(
            status_code=400,
            detail=f"Chưa thể ghép Tập {ep_num:02d}: Không tìm thấy file clip .mp4 nào trong output_videos/{ep_folder_name}!",
        )

    merged_url = _media_url_for_path(merge_res["merged_path"])
    await event_bus.emit(
        "cms_episode_merged",
        {
            "channel_slug": slug,
            "episode_num": ep_num,
            "merged_video_url": merged_url,
            "clip_count": merge_res.get("clip_count"),
            "size_mb": merge_res.get("size_mb"),
            "duration_s": merge_res.get("duration_s"),
        },
    )
    return {
        "ok": True,
        "episode_num": ep_num,
        "merged_video_url": merged_url,
        **merge_res,
    }


# ─── Video Generation Runner Subprocess Manager ──────────────


class RunChannelJobRequest(BaseModel):
    start_ep: int
    end_ep: Optional[int] = None
    only_clip: Optional[int] = None


async def _stream_runner_process(
    slug: str,
    project_id: str,
    proc: asyncio.subprocess.Process,
    start_ep: int,
    end_ep: int,
    only_clip: Optional[int],
):
    try:
        assert proc.stdout is not None
        while True:
            line_bytes = await proc.stdout.readline()
            if not line_bytes:
                break
            line = line_bytes.decode("utf-8", errors="replace").rstrip()
            if not line:
                continue
            # Broadcast raw terminal line for live console view
            await event_bus.emit(
                "cms_terminal",
                {
                    "channel_slug": slug,
                    "line": line,
                    "timestamp": datetime.now().strftime("%H:%M:%S"),
                },
            )
        rc = await proc.wait()
        if rc == 0:
            await record_cms_log(
                slug,
                "SUCCESS",
                "JOB",
                f"🎉 Đã hoàn thành tiến trình tạo video & tự động ghép tập (Tập {start_ep:02d} -> {end_ep:02d})!",
                project_id=project_id,
                episode=start_ep,
                clip_num=only_clip,
            )
        else:
            await record_cms_log(
                slug,
                "WARN",
                "JOB",
                f"⚠️ Tiến trình runner kết thúc với mã thoát {rc} (Tập {start_ep:02d} -> {end_ep:02d}).",
                project_id=project_id,
                episode=start_ep,
                clip_num=only_clip,
            )
    except Exception as e:
        logger.exception("Error in runner stream for %s: %s", slug, e)
    finally:
        if slug in ACTIVE_JOBS:
            ACTIVE_JOBS[slug]["running"] = False
            ACTIVE_JOBS[slug]["finished_at"] = _now_iso()
        await event_bus.emit("cms_job_status", {"channel_slug": slug, "running": False})


@router.post("/channels/{slug}/run")
async def run_cms_channel_job(slug: str, body: RunChannelJobRequest):
    await ensure_cms_seeded()
    db = await get_db()
    cur = await db.execute("SELECT * FROM cms_channel WHERE slug = ?", (slug,))
    row = await cur.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail=f"Không tìm thấy kênh '{slug}'")
    row_dict = dict(row)

    existing = ACTIVE_JOBS.get(slug)
    if existing and existing.get("running"):
        raise HTTPException(status_code=409, detail=f"Kênh '{row_dict['name']}' đang chạy một tiến trình tạo video khác!")

    start_ep = body.start_ep
    end_ep = body.end_ep if body.end_ep is not None else start_ep
    only_clip = body.only_clip if body.only_clip and body.only_clip > 0 else None

    python_bin = os.path.join(FLOWKIT_DIR, "venv", "bin", "python")
    if not os.path.isfile(python_bin):
        python_bin = sys.executable

    script_abs = os.path.join(FLOWKIT_DIR, row_dict["runner_script"])
    if not os.path.isfile(script_abs):
        raise HTTPException(status_code=404, detail=f"Không tìm thấy runner script: {script_abs}")

    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"
    env["NO_PROXY"] = "127.0.0.1,localhost"
    env["no_proxy"] = "127.0.0.1,localhost"
    if only_clip:
        env["FLOWKIT_ONLY_CLIP"] = str(only_clip)
    else:
        env.pop("FLOWKIT_ONLY_CLIP", None)

    proc = await asyncio.create_subprocess_exec(
        python_bin,
        script_abs,
        str(start_ep),
        str(end_ep),
        cwd=FLOWKIT_DIR,
        env=env,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.STDOUT,
    )

    ACTIVE_JOBS[slug] = {
        "running": True,
        "pid": proc.pid,
        "process": proc,
        "start_ep": start_ep,
        "end_ep": end_ep,
        "only_clip": only_clip,
        "started_at": _now_iso(),
    }

    target_desc = (
        f"Tập {start_ep:02d} - Clip {only_clip:02d} (Tạo & ghi đè riêng đúng Clip {only_clip:02d})"
        if only_clip
        else (f"Tập {start_ep:02d}" if start_ep == end_ep else f"Tập {start_ep:02d} đến Tập {end_ep:02d}")
    )
    await record_cms_log(
        slug,
        "INFO",
        "JOB",
        f"🚀 Bắt đầu tạo video từ CMS cho kênh '{row_dict['name']}' — {target_desc} (PID {proc.pid})",
        project_id=row_dict["project_id"],
        episode=start_ep,
        clip_num=only_clip,
    )
    await event_bus.emit(
        "cms_job_status",
        {
            "channel_slug": slug,
            "running": True,
            "pid": proc.pid,
            "start_ep": start_ep,
            "end_ep": end_ep,
            "only_clip": only_clip,
        },
    )

    asyncio.create_task(_stream_runner_process(slug, row_dict["project_id"], proc, start_ep, end_ep, only_clip))
    return {
        "ok": True,
        "channel_slug": slug,
        "pid": proc.pid,
        "start_ep": start_ep,
        "end_ep": end_ep,
        "only_clip": only_clip,
    }


@router.post("/channels/{slug}/stop")
async def stop_cms_channel_job(slug: str):
    job = ACTIVE_JOBS.get(slug)
    if not job or not job.get("running"):
        return {"ok": True, "stopped": False, "message": "Không có tiến trình nào đang chạy."}
    proc = job.get("process")
    if proc:
        try:
            proc.terminate()
        except Exception:
            pass
    job["running"] = False
    await record_cms_log(slug, "WARN", "JOB", f"🛑 Đã dừng tiến trình tạo video của kênh '{slug}' theo yêu cầu từ CMS.")
    await event_bus.emit("cms_job_status", {"channel_slug": slug, "running": False})
    return {"ok": True, "stopped": True}


# ─── Media Streaming Endpoint ────────────────────────────────


@router.get("/media")
async def serve_cms_media(path: str = Query(..., description="Relative path inside workspace")):
    clean_rel = os.path.normpath(path).lstrip(os.sep)
    abs_target = os.path.realpath(os.path.join(WORKSPACE_DIR, clean_rel))
    abs_workspace = os.path.realpath(WORKSPACE_DIR)
    if not abs_target.startswith(abs_workspace + os.sep):
        raise HTTPException(status_code=403, detail="Truy cập đường dẫn không hợp lệ.")
    if not os.path.isfile(abs_target):
        raise HTTPException(status_code=404, detail="File media không tồn tại.")
    minfo = detect_media_info(abs_target)
    return FileResponse(
        abs_target,
        media_type=minfo["mime_type"],
        filename=os.path.basename(abs_target),
        content_disposition_type="inline",
        headers={
            "Cache-Control": "no-cache, must-revalidate",
            "Accept-Ranges": "bytes",
        },
    )


# ─── Persistent Real-Time Logs Endpoints ─────────────────────


class CreateLogRequest(BaseModel):
    channel_slug: str = "system"
    project_id: Optional[str] = None
    episode: Optional[int] = None
    clip_num: Optional[int] = None
    level: str = "INFO"
    category: str = "RUNNER"
    message: str
    details: Optional[dict] = None


@router.post("/logs")
async def create_cms_log_entry(body: CreateLogRequest):
    item = await record_cms_log(
        channel_slug=body.channel_slug,
        level=body.level,
        category=body.category,
        message=body.message,
        project_id=body.project_id,
        episode=body.episode,
        clip_num=body.clip_num,
        details=body.details,
    )
    return {"ok": True, "log": item}


@router.get("/logs")
async def list_cms_logs(
    channel_slug: Optional[str] = None,
    level: Optional[str] = None,
    category: Optional[str] = None,
    episode: Optional[int] = None,
    search: Optional[str] = None,
    limit: int = 250,
):
    await ensure_cms_seeded()
    db = await get_db()
    clauses = []
    params: list = []

    if channel_slug and channel_slug != "ALL":
        clauses.append("channel_slug = ?")
        params.append(channel_slug)
    if level and level != "ALL":
        clauses.append("level = ?")
        params.append(level.upper())
    if category and category != "ALL":
        clauses.append("category = ?")
        params.append(category)
    if episode is not None:
        clauses.append("episode = ?")
        params.append(episode)
    if search and search.strip():
        clauses.append("(message LIKE ? OR details_json LIKE ?)")
        q = f"%{search.strip()}%"
        params.extend([q, q])

    where_sql = f"WHERE {' AND '.join(clauses)}" if clauses else ""
    safe_limit = max(1, min(limit, 1000))
    sql = f"SELECT * FROM cms_log {where_sql} ORDER BY id DESC LIMIT ?"
    params.append(safe_limit)

    cur = await db.execute(sql, tuple(params))
    rows = await cur.fetchall()
    logs = []
    for r in rows:
        d = dict(r)
        details_obj = None
        if d.get("details_json"):
            try:
                details_obj = json.loads(d["details_json"])
            except Exception:
                details_obj = None
        logs.append(
            {
                "id": d["id"],
                "channel_slug": d["channel_slug"],
                "project_id": d["project_id"],
                "episode": d["episode"],
                "clip_num": d["clip_num"],
                "level": d["level"],
                "category": d["category"],
                "message": d["message"],
                "details": details_obj,
                "created_at": d["created_at"],
            }
        )
    return {"logs": logs}


@router.delete("/logs")
async def clear_cms_logs(channel_slug: Optional[str] = None):
    db = await get_db()
    if channel_slug and channel_slug != "ALL":
        await db.execute("DELETE FROM cms_log WHERE channel_slug = ?", (channel_slug,))
    else:
        await db.execute("DELETE FROM cms_log")
    await db.commit()
    return {"ok": True}


# ─── Cloudflare R2 Storage & D1 SQL Synchronization Endpoints ────────


class CloudConfigUpdateRequest(BaseModel):
    db_backend: Optional[str] = None
    cf_account_id: Optional[str] = None
    cf_api_token: Optional[str] = None
    cf_d1_database_id: Optional[str] = None
    r2_auto_upload: Optional[bool] = None
    r2_account_id: Optional[str] = None
    r2_access_key_id: Optional[str] = None
    r2_secret_access_key: Optional[str] = None
    r2_bucket_name: Optional[str] = None
    r2_public_url: Optional[str] = None
    r2_endpoint_url: Optional[str] = None
    r2_key_prefix: Optional[str] = None


class SyncRecordRequest(BaseModel):
    kind: str  # "clip" | "episode"
    channel_slug: str
    project_id: Optional[str] = None
    episode_num: int
    folder_name: Optional[str] = None
    clip_num: Optional[int] = None
    label: Optional[str] = None
    prompt: Optional[str] = None
    status: str = "COMPLETED"
    local_path: Optional[str] = None
    r2_key: Optional[str] = None
    r2_url: Optional[str] = None
    frame_local_path: Optional[str] = None
    frame_r2_key: Optional[str] = None
    frame_r2_url: Optional[str] = None
    total_clips: int = 0
    rendered_clips: int = 0
    is_complete: int = 1
    merged_local_path: Optional[str] = None
    merged_r2_key: Optional[str] = None
    merged_r2_url: Optional[str] = None
    merged_size_mb: Optional[float] = None
    size_mb: Optional[float] = None
    duration_s: Optional[float] = None
    media_id: Optional[str] = None


class SyncR2BatchRequest(BaseModel):
    channel_slug: Optional[str] = None
    episode_num: Optional[int] = None
    force: bool = False


async def _populate_all_channels_into_db(db) -> dict:
    """Scan all 6 series channels on disk and upsert episodes & clips (prompts + video paths) into cms_episode & cms_clip."""
    await ensure_cms_seeded()
    raw_db = getattr(db, "_sqlite", db)
    cur = await raw_db.execute("SELECT * FROM cms_channel ORDER BY rowid ASC")
    channels = [dict(r) for r in await cur.fetchall()]
    now = _now_iso()
    ep_upserted = 0
    clip_upserted = 0

    for ch in channels:
        slug = ch["slug"]
        pid = ch["project_id"]
        ep_map, clip_map = await _load_channel_db_maps(raw_db, slug)
        episodes = _scan_channel_episodes(ch, include_prompts=True, db_episodes_map=ep_map, db_clips_map=clip_map)
        for ep in episodes:
            ep_num = ep["episode_num"]
            ep_id = f"{slug}:ep:{ep_num}"
            old_ep = ep_map.get(ep_num) or {}
            await raw_db.execute(
                """INSERT OR REPLACE INTO cms_episode
                   (id, channel_slug, project_id, episode_num, folder_name, label,
                    total_clips, rendered_clips, is_complete, merged_local_path,
                    merged_r2_key, merged_r2_url, merged_size_mb, duration_s, updated_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    ep_id,
                    slug,
                    pid,
                    ep_num,
                    ep["folder_name"],
                    ep["label"],
                    ep["total_clips"],
                    ep["rendered_clips"],
                    1 if ep["is_complete"] else 0,
                    ep.get("merged_video_path") or old_ep.get("merged_local_path"),
                    ep.get("merged_r2_key") or old_ep.get("merged_r2_key"),
                    ep.get("merged_r2_url") or old_ep.get("merged_r2_url"),
                    ep.get("merged_size_mb") or old_ep.get("merged_size_mb"),
                    old_ep.get("duration_s"),
                    now,
                ),
            )
            ep_upserted += 1

            for cl in ep.get("clips", []):
                c_num = cl["clip_num"]
                clip_id = f"{slug}:ep:{ep_num}:clip:{c_num}"
                old_cl = clip_map.get((ep_num, c_num)) or {}
                series_abs_dir = os.path.join(WORKSPACE_DIR, ch["series_dir"])
                v_file = _find_clip_video_file(series_abs_dir, ep_num, ep["folder_name"], c_num)
                f_file = _find_clip_frame_file(series_abs_dir, ep_num, c_num)
                await raw_db.execute(
                    """INSERT OR REPLACE INTO cms_clip
                       (id, channel_slug, project_id, episode_num, folder_name, clip_num,
                        prompt, status, local_path, r2_key, r2_url,
                        frame_local_path, frame_r2_key, frame_r2_url,
                        size_mb, duration_s, media_id, updated_at)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (
                        clip_id,
                        slug,
                        pid,
                        ep_num,
                        ep["folder_name"],
                        c_num,
                        cl.get("prompt") or old_cl.get("prompt") or "",
                        cl.get("status") or "PENDING",
                        v_file or old_cl.get("local_path"),
                        cl.get("r2_key") or old_cl.get("r2_key"),
                        cl.get("r2_url") or old_cl.get("r2_url"),
                        f_file or old_cl.get("frame_local_path"),
                        old_cl.get("frame_r2_key"),
                        cl.get("frame_r2_url") or old_cl.get("frame_r2_url"),
                        cl.get("video_size_mb") or old_cl.get("size_mb"),
                        old_cl.get("duration_s"),
                        old_cl.get("media_id"),
                        now,
                    ),
                )
                clip_upserted += 1

    await raw_db.commit()
    return {"episodes_indexed": ep_upserted, "clips_indexed": clip_upserted}


@router.get("/cloud/status")
async def get_cms_cloud_status(live: bool = False):
    """Kiểm tra trạng thái kết nối Cloudflare D1 SQL và Cloudflare R2 Storage."""
    from agent.config import get_cloud_config
    from agent.db.d1_client import is_d1_configured, test_d1_connection
    from agent.services.r2_storage import is_r2_configured, test_r2_connection

    await ensure_cms_seeded()
    db = await get_db()
    cfg = get_cloud_config()

    ep_cur = await db.execute("SELECT COUNT(*) as total, SUM(CASE WHEN merged_r2_url IS NOT NULL AND merged_r2_url != '' THEN 1 ELSE 0 END) as r2_count FROM cms_episode")
    ep_row = dict(await ep_cur.fetchone() or {})
    cl_cur = await db.execute("SELECT COUNT(*) as total, SUM(CASE WHEN r2_url IS NOT NULL AND r2_url != '' THEN 1 ELSE 0 END) as r2_count FROM cms_clip")
    cl_row = dict(await cl_cur.fetchone() or {})

    d1_status = {"configured": is_d1_configured(cfg), "database_id": cfg.get("cf_d1_database_id"), "ok": is_d1_configured(cfg)}
    r2_status = {"configured": is_r2_configured(cfg), "bucket": cfg.get("r2_bucket_name"), "ok": is_r2_configured(cfg)}

    if live:
        if is_d1_configured(cfg):
            d1_status = await test_d1_connection(cfg)
        if is_r2_configured(cfg):
            r2_status = await asyncio.to_thread(test_r2_connection, cfg)

    masked_cfg = {
        "db_backend": cfg.get("db_backend", "d1"),
        "cf_account_id": cfg.get("cf_account_id", ""),
        "cf_api_token_set": bool(cfg.get("cf_api_token")),
        "cf_d1_database_id": cfg.get("cf_d1_database_id", ""),
        "r2_auto_upload": cfg.get("r2_auto_upload", True),
        "r2_account_id": cfg.get("r2_account_id", ""),
        "r2_access_key_id": cfg.get("r2_access_key_id", ""),
        "r2_secret_key_set": bool(cfg.get("r2_secret_access_key")),
        "r2_bucket_name": cfg.get("r2_bucket_name", "tiktok-series"),
        "r2_public_url": cfg.get("r2_public_url", ""),
        "r2_endpoint_url": cfg.get("r2_endpoint_url", ""),
        "r2_key_prefix": cfg.get("r2_key_prefix", "series"),
    }

    return {
        "ok": True,
        "config": masked_cfg,
        "d1": d1_status,
        "r2": r2_status,
        "stats": {
            "indexed_episodes": ep_row.get("total") or 0,
            "r2_merged_episodes": ep_row.get("r2_count") or 0,
            "indexed_clips": cl_row.get("total") or 0,
            "r2_clips": cl_row.get("r2_count") or 0,
        },
    }


@router.post("/cloud/config")
async def update_cms_cloud_config(body: CloudConfigUpdateRequest):
    """Lưu cấu hình Cloudflare D1 SQL & R2 Storage vào flowkit/.env và kích hoạt ngay."""
    from agent.config import update_env_file, get_cloud_config
    from agent.db.d1_client import is_d1_configured, test_d1_connection, init_d1_schema
    from agent.db.schema import SCHEMA
    from agent.services.r2_storage import is_r2_configured, test_r2_connection

    updates: dict[str, str] = {}
    if body.db_backend is not None:
        updates["DB_BACKEND"] = body.db_backend.strip().lower()
    if body.cf_account_id is not None:
        updates["CF_ACCOUNT_ID"] = body.cf_account_id.strip()
    if body.cf_api_token is not None and body.cf_api_token.strip():
        updates["CF_API_TOKEN"] = body.cf_api_token.strip()
    if body.cf_d1_database_id is not None:
        updates["CF_D1_DATABASE_ID"] = body.cf_d1_database_id.strip()
    if body.r2_auto_upload is not None:
        updates["R2_AUTO_UPLOAD"] = "1" if body.r2_auto_upload else "0"
    if body.r2_account_id is not None:
        updates["R2_ACCOUNT_ID"] = body.r2_account_id.strip()
    if body.r2_access_key_id is not None:
        updates["R2_ACCESS_KEY_ID"] = body.r2_access_key_id.strip()
    if body.r2_secret_access_key is not None and body.r2_secret_access_key.strip():
        updates["R2_SECRET_ACCESS_KEY"] = body.r2_secret_access_key.strip()
    if body.r2_bucket_name is not None:
        updates["R2_BUCKET_NAME"] = body.r2_bucket_name.strip() or "tiktok-series"
    if body.r2_public_url is not None:
        updates["R2_PUBLIC_URL"] = body.r2_public_url.strip().rstrip("/")
    if body.r2_endpoint_url is not None:
        updates["R2_ENDPOINT_URL"] = body.r2_endpoint_url.strip().rstrip("/")
    if body.r2_key_prefix is not None:
        updates["R2_KEY_PREFIX"] = body.r2_key_prefix.strip().strip("/")

    if updates:
        update_env_file(updates)

    cfg = get_cloud_config()
    d1_test = {"configured": False}
    r2_test = {"configured": False}

    if is_d1_configured(cfg):
        await init_d1_schema(SCHEMA)
        d1_test = await test_d1_connection(cfg)
    if is_r2_configured(cfg):
        r2_test = await asyncio.to_thread(test_r2_connection, cfg)

    await record_cms_log(
        "system",
        "SUCCESS",
        "CLOUD",
        f"Đã lưu cấu hình Cloudflare D1 SQL & R2 Storage (D1={'OK' if d1_test.get('ok') else 'Chờ cấu hình'}, R2={'OK' if r2_test.get('ok') else 'Chờ cấu hình'}).",
    )
    return {"ok": True, "d1": d1_test, "r2": r2_test}


class MarkEpisodeStatusRequest(BaseModel):
    status: str = "COMPLETED"  # "COMPLETED" or "PENDING"
    up_to: bool = False  # If True, apply to all episodes <= ep_num


@router.post("/channels/{slug}/episodes/{ep_num}/mark-status")
async def mark_cms_episode_status(slug: str, ep_num: int, body: MarkEpisodeStatusRequest):
    """Đánh dấu hoàn thành (COMPLETED) hoặc đặt lại (PENDING) cho 1 tập (hoặc từ tập 1 -> ep_num) và đồng bộ D1 SQL."""
    await ensure_cms_seeded()
    db = await get_db()
    now = _now_iso()
    target_status = "COMPLETED" if body.status.upper() == "COMPLETED" else "PENDING"
    is_done_int = 1 if target_status == "COMPLETED" else 0

    if body.up_to:
        await db.execute(
            """UPDATE cms_episode
               SET rendered_clips = CASE WHEN ? = 1 THEN total_clips ELSE 0 END,
                   is_complete = ?,
                   updated_at = ?
               WHERE channel_slug = ? AND episode_num <= ?""",
            (is_done_int, is_done_int, now, slug, ep_num),
        )
        await db.execute(
            """UPDATE cms_clip
               SET status = ?,
                   updated_at = ?
               WHERE channel_slug = ? AND episode_num <= ?""",
            (target_status, now, slug, ep_num),
        )
    else:
        await db.execute(
            """UPDATE cms_episode
               SET rendered_clips = CASE WHEN ? = 1 THEN total_clips ELSE 0 END,
                   is_complete = ?,
                   updated_at = ?
               WHERE channel_slug = ? AND episode_num = ?""",
            (is_done_int, is_done_int, now, slug, ep_num),
        )
        await db.execute(
            """UPDATE cms_clip
               SET status = ?,
                   updated_at = ?
               WHERE channel_slug = ? AND episode_num = ?""",
            (target_status, now, slug, ep_num),
        )

    await db.commit()
    msg = (
        f"✅ Đã đánh dấu HOÀN THÀNH từ Tập 01 → Tập {ep_num:02d} (đồng bộ D1 SQL đa máy)!"
        if (body.up_to and is_done_int)
        else f"✅ Đã đánh dấu HOÀN THÀNH Tập {ep_num:02d} (đồng bộ D1 SQL đa máy)!"
        if is_done_int
        else f"🔄 Đã đặt lại trạng thái CHỜ RENDER cho Tập {ep_num:02d}!"
    )
    await record_cms_log(slug, "SUCCESS" if is_done_int else "INFO", "STATUS_SYNC", msg, episode=ep_num)
    return {"ok": True, "channel_slug": slug, "episode_num": ep_num, "status": target_status, "up_to": body.up_to, "message": msg}


@router.post("/cloud/sync-record")
async def sync_cms_cloud_record(body: SyncRecordRequest):
    """Lưu thông tin clip / tập hoàn chỉnh (cùng link R2) từ Runner vào D1 SQL + SQLite."""
    await ensure_cms_seeded()
    db = await get_db()
    now = _now_iso()
    slug = body.channel_slug
    ep_num = body.episode_num
    folder = body.folder_name or f"tap-{ep_num:02d}"

    if body.kind == "clip" and body.clip_num is not None:
        clip_id = f"{slug}:ep:{ep_num}:clip:{body.clip_num}"
        cur = await db.execute("SELECT * FROM cms_clip WHERE id = ?", (clip_id,))
        existing_row = await cur.fetchone()
        existing = dict(existing_row) if existing_row else {}
        prompt_val = body.prompt if body.prompt is not None else (existing.get("prompt") or "")
        r2_key_val = body.r2_key or existing.get("r2_key")
        r2_url_val = body.r2_url or existing.get("r2_url")
        frame_r2_key_val = body.frame_r2_key or existing.get("frame_r2_key")
        frame_r2_url_val = body.frame_r2_url or existing.get("frame_r2_url")
        size_val = body.size_mb if body.size_mb is not None else existing.get("size_mb")
        dur_val = body.duration_s if body.duration_s is not None else existing.get("duration_s")
        media_id_val = body.media_id or existing.get("media_id")

        await db.execute(
            """INSERT OR REPLACE INTO cms_clip
               (id, channel_slug, project_id, episode_num, folder_name, clip_num,
                prompt, status, local_path, r2_key, r2_url,
                frame_local_path, frame_r2_key, frame_r2_url,
                size_mb, duration_s, media_id, updated_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                clip_id,
                slug,
                body.project_id or existing.get("project_id"),
                ep_num,
                folder,
                body.clip_num,
                prompt_val,
                body.status or "COMPLETED",
                body.local_path or existing.get("local_path"),
                r2_key_val,
                r2_url_val,
                body.frame_local_path or existing.get("frame_local_path"),
                frame_r2_key_val,
                frame_r2_url_val,
                size_val,
                dur_val,
                media_id_val,
                now,
            ),
        )
        # Tự động tính lại số clip đã xong của tập để đánh dấu hoàn thành tập khi đủ clip
        cnt_cur = await db.execute(
            """SELECT COUNT(*) as total_c,
                      SUM(CASE WHEN status = 'COMPLETED' THEN 1 ELSE 0 END) as done_c
               FROM cms_clip
               WHERE channel_slug = ? AND episode_num = ?""",
            (slug, ep_num),
        )
        cnt_row = await cnt_cur.fetchone()
        if cnt_row:
            total_c = int(cnt_row["total_c"] or 0)
            done_c = int(cnt_row["done_c"] or 0)
            if total_c > 0:
                is_ep_done = 1 if done_c >= total_c else 0
                await db.execute(
                    """UPDATE cms_episode
                       SET rendered_clips = ?,
                           is_complete = CASE WHEN is_complete = 1 THEN 1 ELSE ? END,
                           updated_at = ?
                       WHERE channel_slug = ? AND episode_num = ?""",
                    (done_c, is_ep_done, now, slug, ep_num),
                )
        await db.commit()
        await event_bus.emit(
            "cms_clip_synced",
            {
                "channel_slug": slug,
                "episode_num": ep_num,
                "clip_num": body.clip_num,
                "r2_url": r2_url_val,
                "r2_key": r2_key_val,
                "size_mb": size_val,
            },
        )
        return {"ok": True, "id": clip_id, "r2_url": r2_url_val}

    ep_id = f"{slug}:ep:{ep_num}"
    cur_ep = await db.execute("SELECT * FROM cms_episode WHERE id = ?", (ep_id,))
    existing_ep_row = await cur_ep.fetchone()
    existing_ep = dict(existing_ep_row) if existing_ep_row else {}
    merged_r2_key_val = body.merged_r2_key or existing_ep.get("merged_r2_key")
    merged_r2_url_val = body.merged_r2_url or existing_ep.get("merged_r2_url")
    merged_size_val = body.merged_size_mb or body.size_mb or existing_ep.get("merged_size_mb")
    dur_ep_val = body.duration_s if body.duration_s is not None else existing_ep.get("duration_s")

    await db.execute(
        """INSERT OR REPLACE INTO cms_episode
           (id, channel_slug, project_id, episode_num, folder_name, label,
            total_clips, rendered_clips, is_complete, merged_local_path,
            merged_r2_key, merged_r2_url, merged_size_mb, duration_s, updated_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            ep_id,
            slug,
            body.project_id or existing_ep.get("project_id"),
            ep_num,
            folder,
            body.label or existing_ep.get("label") or f"Tập {ep_num:02d}",
            body.total_clips or existing_ep.get("total_clips") or 0,
            body.rendered_clips or existing_ep.get("rendered_clips") or 0,
            body.is_complete,
            body.merged_local_path or existing_ep.get("merged_local_path"),
            merged_r2_key_val,
            merged_r2_url_val,
            merged_size_val,
            dur_ep_val,
            now,
        ),
    )
    if body.is_complete and body.rendered_clips >= max(body.total_clips, 1):
        await db.execute(
            """UPDATE cms_clip
               SET status = 'COMPLETED',
                   updated_at = ?
               WHERE channel_slug = ? AND episode_num = ?""",
            (now, slug, ep_num),
        )
    await db.commit()
    await event_bus.emit(
        "cms_episode_synced",
        {
            "channel_slug": slug,
            "episode_num": ep_num,
            "merged_r2_url": body.merged_r2_url,
            "merged_r2_key": body.merged_r2_key,
            "size_mb": body.merged_size_mb or body.size_mb,
        },
    )
    return {"ok": True, "id": ep_id, "merged_r2_url": body.merged_r2_url}


@router.post("/cloud/sync-d1")
async def sync_all_cms_data_to_d1(direction: str = "push"):
    """
    Quét toàn bộ dữ liệu 6 kênh (prompts, episodes, clips, characters, projects, logs)
    và đồng bộ 100% lên Cloudflare D1 SQL (hoặc pull từ D1 về máy).
    """
    from agent.db.d1_client import is_d1_configured, sync_sqlite_to_d1, sync_d1_to_sqlite
    from agent.db.schema import SCHEMA

    await ensure_cms_seeded()
    db = await get_db()
    indexed = await _populate_all_channels_into_db(db)

    if not is_d1_configured():
        return {
            "ok": False,
            "indexed_locally": indexed,
            "error": "Đã lập chỉ mục toàn bộ dữ liệu cục bộ vào bảng cms_episode & cms_clip, nhưng bạn chưa điền CF_ACCOUNT_ID / CF_D1_DATABASE_ID / CF_API_TOKEN để đẩy lên Cloudflare D1 SQL.",
        }

    if direction == "pull":
        res = await sync_d1_to_sqlite(db, SCHEMA)
        await record_cms_log(
            "system",
            "SUCCESS" if res.get("ok") else "WARN",
            "D1_SYNC",
            f"Đã kéo {res.get('total_rows_pulled', 0)} bản ghi từ Cloudflare D1 SQL về máy.",
            details=res,
        )
        return {**res, "indexed_locally": indexed}

    res = await sync_sqlite_to_d1(db, SCHEMA)
    await record_cms_log(
        "system",
        "SUCCESS" if res.get("ok") else "WARN",
        "D1_SYNC",
        f"☁️ Đã đồng bộ {res.get('total_rows_synced', 0)} bản ghi từ tất cả các bảng lên Cloudflare D1 SQL!",
        details=res,
    )
    return {**res, "indexed_locally": indexed}


@router.post("/cloud/sync-r2")
async def sync_videos_to_r2(body: SyncR2BatchRequest):
    """
    Tự động quét các video clip & tập FULL (.mp4) đã hoàn thành trên máy và upload đồng loạt lên Cloudflare R2 Storage,
    sau đó cập nhật r2_url vào Cloudflare D1 SQL.
    """
    from agent.services.r2_storage import (
        load_r2_config,
        is_r2_configured,
        build_r2_key,
        upload_file_to_r2,
        list_r2_bucket_objects,
    )

    await ensure_cms_seeded()
    db = await get_db()
    await _populate_all_channels_into_db(db)

    r2_cfg = load_r2_config()
    if not is_r2_configured(r2_cfg):
        raise HTTPException(
            status_code=400,
            detail="Chưa cấu hình Cloudflare R2 Storage (vui lòng nhập R2_ACCESS_KEY_ID + R2_SECRET_ACCESS_KEY hoặc CF_API_TOKEN).",
        )

    where_ep = []
    params_ep: list = []
    if body.channel_slug and body.channel_slug != "ALL":
        where_ep.append("channel_slug = ?")
        params_ep.append(body.channel_slug)
    if body.episode_num is not None:
        where_ep.append("episode_num = ?")
        params_ep.append(body.episode_num)

    where_sql = f"WHERE {' AND '.join(where_ep)}" if where_ep else ""

    uploaded_clips = []
    uploaded_episodes = []
    errors = []
    now = _now_iso()

    # 1. Upload individual clips
    cl_cur = await db.execute(f"SELECT * FROM cms_clip {where_sql} ORDER BY channel_slug, episode_num, clip_num", tuple(params_ep))
    clips = [dict(r) for r in await cl_cur.fetchall()]
    for cl in clips:
        lpath = cl.get("local_path")
        if not lpath or not os.path.isfile(lpath):
            continue
        if cl.get("r2_url") and not body.force:
            continue

        fname = os.path.basename(lpath)
        obj_key = build_r2_key(cl["channel_slug"], "episodes", fname, subfolder=cl["folder_name"], cfg=r2_cfg)
        up_res = await asyncio.to_thread(upload_file_to_r2, lpath, obj_key, "video/mp4", r2_cfg)
        if up_res.get("ok"):
            dur = cl.get("duration_s") or await asyncio.to_thread(probe_video_duration, lpath)
            await db.execute(
                """UPDATE cms_clip
                   SET r2_key = ?, r2_url = ?, size_mb = ?, duration_s = ?, status = 'COMPLETED', updated_at = ?
                   WHERE id = ?""",
                (up_res["r2_key"], up_res["r2_url"], up_res["size_mb"], dur, now, cl["id"]),
            )
            uploaded_clips.append({"id": cl["id"], "r2_url": up_res["r2_url"], "size_mb": up_res["size_mb"]})
        else:
            errors.append(f"{fname}: {up_res.get('error')}")

    # 2. Upload merged full episodes
    ep_cur = await db.execute(f"SELECT * FROM cms_episode {where_sql} ORDER BY channel_slug, episode_num", tuple(params_ep))
    episodes = [dict(r) for r in await ep_cur.fetchall()]
    for ep in episodes:
        mpath = ep.get("merged_local_path")
        if not mpath or not os.path.isfile(mpath):
            continue
        if ep.get("merged_r2_url") and not body.force:
            continue

        fname = os.path.basename(mpath)
        obj_key = build_r2_key(ep["channel_slug"], "full_episodes", fname, cfg=r2_cfg)
        up_res = await asyncio.to_thread(upload_file_to_r2, mpath, obj_key, "video/mp4", r2_cfg)
        if up_res.get("ok"):
            dur = ep.get("duration_s") or await asyncio.to_thread(probe_video_duration, mpath)
            await db.execute(
                """UPDATE cms_episode
                   SET merged_r2_key = ?, merged_r2_url = ?, merged_size_mb = ?, duration_s = ?, updated_at = ?
                   WHERE id = ?""",
                (up_res["r2_key"], up_res["r2_url"], up_res["size_mb"], dur, now, ep["id"]),
            )
            uploaded_episodes.append({"id": ep["id"], "r2_url": up_res["r2_url"], "size_mb": up_res["size_mb"]})
        else:
            errors.append(f"{fname}: {up_res.get('error')}")

    # 3. Also check 10-minute full episodes in output_videos (e.g. biet-doi-gara_tap-01_FULL.mp4)
    if not body.channel_slug or body.channel_slug in ("ALL", "biet-doi-gara"):
        bdg_full = os.path.join(WORKSPACE_DIR, "biet-doi-gara", "output_videos", "biet-doi-gara_tap-01_FULL.mp4")
        if os.path.isfile(bdg_full):
            ep10_id = "biet-doi-gara:ep:101"
            cur10 = await db.execute("SELECT merged_r2_url FROM cms_episode WHERE id = ?", (ep10_id,))
            row10 = await cur10.fetchone()
            if body.force or not (row10 and row10["merged_r2_url"]):
                obj_key = build_r2_key("biet-doi-gara", "full_episodes", "biet-doi-gara_tap-01_FULL.mp4", cfg=r2_cfg)
                up_res = await asyncio.to_thread(upload_file_to_r2, bdg_full, obj_key, "video/mp4", r2_cfg)
                if up_res.get("ok"):
                    dur = await asyncio.to_thread(probe_video_duration, bdg_full)
                    await db.execute(
                        """INSERT OR REPLACE INTO cms_episode
                           (id, channel_slug, project_id, episode_num, folder_name, label,
                            total_clips, rendered_clips, is_complete, merged_local_path,
                            merged_r2_key, merged_r2_url, merged_size_mb, duration_s, updated_at)
                           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                        (
                            ep10_id,
                            "biet-doi-gara",
                            "30714c49-2878-439b-a46f-c52be6eee2fc",
                            101,
                            "tap-01-full-10p",
                            "Tập 01 FULL (10 Phút - Cảnh 01..10)",
                            60,
                            60,
                            1,
                            bdg_full,
                            up_res["r2_key"],
                            up_res["r2_url"],
                            up_res["size_mb"],
                            dur,
                            now,
                        ),
                    )
                    uploaded_episodes.append({"id": ep10_id, "r2_url": up_res["r2_url"], "size_mb": up_res["size_mb"]})

    # 4. Also reconcile any existing objects already in R2 bucket (e.g. when local .mp4 files were deleted)
    try:
        r2_objs = await asyncio.to_thread(list_r2_bucket_objects, r2_cfg.get("r2_key_prefix", "series"), r2_cfg)
        for obj in r2_objs:
            okey = obj["r2_key"]
            ourl = obj["r2_url"]
            osize = obj["size_mb"]
            parts = okey.split("/")
            # Expected: series/<slug>/<category>/...
            if len(parts) < 4:
                continue
            ch_slug = parts[1]
            if body.channel_slug and body.channel_slug != "ALL" and ch_slug != body.channel_slug:
                continue
            cat = parts[2]
            fname = parts[-1]
            if cat == "episodes" and len(parts) >= 5:
                subf = parts[3]
                m_ep = re.search(r"(\d+)", subf) or re.search(r"(?:tap|canh|_T)[-_]?(\d+)", fname, re.IGNORECASE)
                m_cl = re.search(r"(?:clip[-_]|_C)(\d+)\.mp4$", fname, re.IGNORECASE)
                if m_ep and m_cl:
                    ep_n = int(m_ep.group(1))
                    cl_n = int(m_cl.group(1))
                    if body.episode_num is not None and ep_n != body.episode_num:
                        continue
                    cid = f"{ch_slug}:ep:{ep_n}:clip:{cl_n}"
                    await db.execute(
                        """UPDATE cms_clip
                           SET r2_key = ?, r2_url = ?, size_mb = COALESCE(size_mb, ?), status = 'COMPLETED', updated_at = ?
                           WHERE id = ?""",
                        (okey, ourl, osize, now, cid),
                    )
            elif cat == "full_episodes":
                m_ep = re.search(r"(?:tap|canh)[-_]?(\d+)_FULL\.mp4$", fname, re.IGNORECASE)
                if m_ep:
                    ep_n = int(m_ep.group(1))
                    if body.episode_num is not None and ep_n != body.episode_num:
                        continue
                    eid = f"{ch_slug}:ep:{ep_n}"
                    await db.execute(
                        """UPDATE cms_episode
                           SET merged_r2_key = ?, merged_r2_url = ?, merged_size_mb = COALESCE(merged_size_mb, ?), is_complete = 1, updated_at = ?
                           WHERE id = ?""",
                        (okey, ourl, osize, now, eid),
                    )
    except Exception:
        pass

    await db.commit()
    await record_cms_log(
        body.channel_slug or "system",
        "SUCCESS" if not errors else "WARN",
        "R2_SYNC",
        f"☁️ Đã đồng bộ lên Cloudflare R2: {len(uploaded_clips)} video clips & {len(uploaded_episodes)} tập FULL!",
        details={"uploaded_clips": len(uploaded_clips), "uploaded_episodes": len(uploaded_episodes), "errors": errors[:5]},
    )
    return {
        "ok": True,
        "uploaded_clips_count": len(uploaded_clips),
        "uploaded_episodes_count": len(uploaded_episodes),
        "uploaded_clips": uploaded_clips,
        "uploaded_episodes": uploaded_episodes,
        "errors": errors[:10],
    }

