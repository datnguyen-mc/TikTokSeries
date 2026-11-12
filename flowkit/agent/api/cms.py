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

# TikTok series render 4 clips × 15s per episode (Omni 1.2) since 12/11/2026.
TIKTOK_15S_SLUGS = ("mit-va-du-1970", "pheo-va-no-meo", "me-va-be", "tay-du-ky-2026", "365ngayvietnam")

DEFAULT_CHANNELS = [
    {
        "slug": "mit-va-du-1970",
        "name": "Mít Và Đú 1970",
        "project_id": "234b0e61-f736-4e77-a1d9-527b2fadc582",
        "aspect_ratio": "VIDEO_ASPECT_RATIO_PORTRAIT",
        "runner_script": "runners/mit_va_du.py",
        "series_dir": "mit-va-du-1970",
        "ep_prefix": "tap",
        "description": "Phim tình cảm gia đình miền Tây những năm 1970 cảm động & hài hước dài 60s (4 clips × 15s) về gia đình chó nhân hóa Mít, Đú và bé Nở (3D Pixar 9:16).",
        "characters": [
            {
                "tag": "@Mit",
                "name": "Mít (Chồng ~35 tuổi)",
                "default_media_id": "27613158-7873-4f43-acc8-be0785085843",
                "locked_media_id": "27613158-7873-4f43-acc8-be0785085843",
                "description": "Chó đực lông vàng nâu nhân hóa đi hai chân, mõm và ngực trắng kem, mặc áo ba lỗ xám bạc màu và quần đùi tối màu.",
            },
            {
                "tag": "@Đú",
                "name": "Đú (Vợ ~30 tuổi)",
                "default_media_id": "0f6a1316-e7cf-4722-9930-3a58e3513445",
                "locked_media_id": "0f6a1316-e7cf-4722-9930-3a58e3513445",
                "description": "Chó cái lông vàng kem nhân hóa đi hai chân, mõm trắng có vệt lông trắng dọc sống mũi, mặc áo bà ba hồng nhạt in hoa nhỏ.",
            },
            {
                "tag": "@Nở",
                "name": "Nở (Chó con 6 tuổi)",
                "default_media_id": "d0535a47-2f3b-4173-8e35-8f7663673eaf",
                "locked_media_id": "d0535a47-2f3b-4173-8e35-8f7663673eaf",
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
        "description": "Clip dài 60s (4 clips × 15s) du lịch check-in danh thắng & thưởng thức món ăn đặc sản của Vy và Joi — mỗi cảnh xuất hiện ở một địa điểm/bàn ăn khác nhau, không lặp cảnh xe máy đội nón (9:16).",
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
        "description": "Clip dài 60s (4 clips × 15s) chia sẻ mẹo nuôi con khoa học, quay cận các hành động dễ thương của hai bé song sinh Gạo – Bông và giới thiệu đồ cho bé phù hợp từng giai đoạn tuổi (9:16).",
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
        "description": "Clip 60s (4 clips × 15s): mèo Phèo & bà chủ Hường bàn drama mỗi ngày theo cách hài hước, mỗi clip một tin mới ở một lĩnh vực khác nhau (3D Pixar 9:16).",
        "characters": [
            {
                "tag": "@Pheo",
                "name": "Mèo Phèo (Đầu bếp)",
                "default_media_id": "ed473cc1-f931-45ec-92a2-89119cb89076",
                "locked_media_id": "ed473cc1-f931-45ec-92a2-89119cb89076",
                "description": "Mèo đen mập tròn nhân hóa đi hai chân, ngực có mảng lông trắng nhỏ, tai trái khuyết chữ V, đội mũ đầu bếp và tạp dề xanh navy.",
            },
            {
                "tag": "@No",
                "name": "Bà Chủ Hường / Nở",
                "default_media_id": "8a1b632c-a961-4a87-b512-0724e965b5c3",
                "locked_media_id": "8a1b632c-a961-4a87-b512-0724e965b5c3",
                "description": "Cô chó Pomeranian lông xù màu kem cam nhân hóa, mặc đồ bộ lụa hồng cánh sen, đeo vòng ngọc trai.",
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
        "description": "Clip hài 60s (4 clips × 15s) tổng kết xu hướng hot và drama trong ngày của 4 thầy trò Đường Tăng tại nhà trọ Sài Gòn 2026 (2D 9:16).",
        "characters": [
            {
                "tag": "@Thay",
                "name": "Thầy (Đường Tăng)",
                "default_media_id": "6264f460-c89e-4c21-ad12-3c863a8217da",
                "locked_media_id": "6264f460-c89e-4c21-ad12-3c863a8217da",
                "description": "Nhà sư trẻ tuấn tú hiền lành, mặc áo cà sa cam nghệ và đeo chuỗi hạt gỗ.",
            },
            {
                "tag": "@DaiCa",
                "name": "Đại Ca (Ngộ Không)",
                "default_media_id": "513a5d32-d53b-4c0a-90da-ae4bffe948b8",
                "locked_media_id": "513a5d32-d53b-4c0a-90da-ae4bffe948b8",
                "description": "Chàng khỉ nhân hóa lanh lẹ, đeo vòng kim cô vàng, mặc áo bomber đỏ và quần jogger đen.",
            },
            {
                "tag": "@HeoLuoi",
                "name": "Heo Lười (Bát Giới)",
                "default_media_id": "c3701733-5f3a-4ca6-84dc-60ff28868ec1",
                "locked_media_id": "c3701733-5f3a-4ca6-84dc-60ff28868ec1",
                "description": "Chàng heo nhân hóa mập tròn vui tính, mặc áo sơ mi khoác ngoài xanh navy.",
            },
            {
                "tag": "@UtKho",
                "name": "Út Khờ (Sa Tăng)",
                "default_media_id": "3c49b152-f272-4718-9858-bb2dca2ce88a",
                "locked_media_id": "3c49b152-f272-4718-9858-bb2dca2ce88a",
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
    {
        "slug": "duong-dua-sinh-tu",
        "name": "Đường Đua Sinh Tử: 10 Giây Tự Do",
        "project_id": "f9738ca5-453b-4c72-98d3-630379a1fa2e",
        "aspect_ratio": "VIDEO_ASPECT_RATIO_LANDSCAPE",
        "runner_script": "runners/duong_dua_sinh_tu.py",
        "series_dir": "duong-dua-sinh-tu",
        "ep_prefix": "canh",
        "description": "Phim hành động tốc độ cao 40 phút: sĩ quan cảnh sát chìm Tom thâm nhập đội đua xe đường phố của Micdo để điều tra chuỗi vụ chặn xe tải trên xa lộ, đứng giữa huy hiệu cảnh sát và tình anh em trong 10 giây tự do (16:9, 4 Tập × 10 Cảnh = 40 cảnh × 6 clip = 240 clips).",
        "characters": [
            {
                "tag": "@Tom",
                "name": "Tom (Sĩ quan chìm LAPD)",
                "default_media_id": "d83378af-6eec-499e-a17c-2a12e5764219",
                "locked_media_id": "d83378af-6eec-499e-a17c-2a12e5764219",
                "description": "Tom (27 tuổi): sĩ quan cảnh sát chìm LAPD ẩn náu trong tiệm độ xe Ver's Geh; cao 183 cm, dáng thể thao săn chắc, tóc ngắn nâu sẫm cắt gọn, ánh mắt sắc bén, sẹo nhỏ mờ ở đuôi mày trái, mặc áo thun xám than bên trong sơ mi denim xanh đậm mở cúc, quần jean tối màu vương dầu máy.",
                "ref_prompt": "Full-body photorealistic character reference of @Tom, a 27-year-old Vietnamese-American man, 183 cm, athletic lean build, short textured dark-brown hair, sharp observant dark eyes, clean square jawline, a faint small scar at the outer left eyebrow, fitted charcoal T-shirt under an open dark-blue denim work shirt, oil-scuffed dark jeans, worn brown work boots, steel chronograph watch on left wrist; plain grey studio background, hard side light, 8K. Not resembling any real actor.",
            },
            {
                "tag": "@Micdo",
                "name": "Micdo (Thủ lĩnh)",
                "default_media_id": "317c339b-17ca-4564-934a-40987d1d50f0",
                "locked_media_id": "317c339b-17ca-4564-934a-40987d1d50f0",
                "description": "Micdo (32 tuổi): thủ lĩnh băng đua xe đường phố và đội xe đen; cao 185 cm, cơ bắp vạm vỡ, đầu cạo trọc, mặt vuông uy quyền, đeo dây chuyền bạc mặt chữ thập trên ngực, mặc áo ba lỗ trắng bên trong áo khoác da đen mở khóa.",
                "ref_prompt": "Full-body photorealistic character reference of @Micdo, a 32-year-old man, 185 cm, muscular heavy-shouldered build, clean-shaven bald head, commanding deep-set dark eyes, strong square jawline, a silver cross pendant on a heavy neck chain, fitted white sleeveless tank top under an open black leather jacket, dark jeans, heavy black boots; plain grey studio background, hard side light, 8K. Not resembling any real actor.",
            },
            {
                "tag": "@Ami",
                "name": "Ami (Quán Toto)",
                "default_media_id": "38ee1e43-a8ce-40ac-aff7-3f0383ccc3e4",
                "locked_media_id": "38ee1e43-a8ce-40ac-aff7-3f0383ccc3e4",
                "description": "Ami (24 tuổi): em gái út của Micdo, người trông coi quán ăn gia đình Toto; cao 168 cm, làn da ngăm ấm, tóc nâu đen dài buộc nửa đầu, đeo bông tai bạc nhỏ, mặc áo cổ tròn màu đỏ rượu vang kết hợp tạp dề vải canvas ngang eo và quần jean sáng màu.",
                "ref_prompt": "Full-body photorealistic character reference of @Ami, a 24-year-old woman, 168 cm, slim athletic build, warm olive skin, long dark-brown hair tied half-back, expressive dark eyes, silver stud earrings, fitted burgundy scoop-neck top, light-wash jeans, canvas shop apron tied at the waist, flat sneakers; plain grey studio background, soft warm light, 8K. Not resembling any real actor.",
            },
            {
                "tag": "@Cevin",
                "name": "Cevin (Cánh tay phải)",
                "default_media_id": "ccca3339-8c3a-4dd6-affc-e5b1459643b3",
                "locked_media_id": "ccca3339-8c3a-4dd6-affc-e5b1459643b3",
                "description": "Cevin (29 tuổi): cánh tay phải nóng nảy của Micdo; cao 179 cm, cơ bắp gân guốc, tóc ngắn dựng nhuộm sáng phần ngọn, râu dê gọn, sẹo nhỏ ở khớp ngón tay phải, đeo lắc bạc cổ tay phải, mặc áo sơ mi thợ máy ngắn tay màu đỏ sẫm.",
                "ref_prompt": "Full-body photorealistic character reference of @Cevin, a 29-year-old man, 179 cm, wiry muscular build, short spiky bleached-tip dark hair, intense brow, neat goatee, small chin scar, silver chain bracelet on right wrist, maroon short-sleeve mechanic shirt with rolled sleeves, dark cargo jeans, work boots; plain grey studio background, 8K. Not resembling any real actor.",
            },
            {
                "tag": "@Cina",
                "name": "Cina (Nữ quái tốc độ)",
                "default_media_id": "439d9f2b-627a-4565-96b8-9bbf40826086",
                "locked_media_id": "439d9f2b-627a-4565-96b8-9bbf40826086",
                "description": "Cina (28 tuổi): nữ quái tốc độ sát cánh cùng Micdo; cao 167 cm, dáng thon khỏe, tóc đen ngắn ngang cằm, ánh mắt sắc lạnh tự tin, khuyên tai vòng nhỏ bên tai trái, mặc áo ghi-lê da đen ngắn bên ngoài áo đỏ thẫm và quần da tối màu.",
                "ref_prompt": "Full-body photorealistic character reference of @Cina, a 28-year-old woman, 167 cm, lean athletic build, sharp jawline, short tousled chin-length black hair, fierce confident dark gaze, small hoop earring in left ear, cropped black leather vest over crimson top, low-rise dark leather trousers, heavy lace boots; plain grey studio background, 8K. Not resembling any real actor.",
            },
            {
                "tag": "@Seja",
                "name": "Seja (Kỹ thuật viên)",
                "default_media_id": "3bb3de48-4dd3-4a90-a3ea-60be3063a7b1",
                "locked_media_id": "3bb3de48-4dd3-4a90-a3ea-60be3063a7b1",
                "description": "Seja (22 tuổi): thiên tài toán học, máy tính và điện tử độ xe của nhóm; cao 175 cm, dáng gầy nhanh nhẹn, tóc đen xoăn rối, đeo kính gọng mảnh kỹ thuật, mặc áo sơ mi công nhân màu xanh ô liu khoác ngoài áo thun dài tay kẻ sọc, đeo dây túi laptop chéo ngực.",
                "ref_prompt": "Full-body photorealistic character reference of @Seja, a 22-year-old man, 175 cm, wiry lanky build, messy curly dark hair, quick restless eyes, thin-framed technical glasses, oversized olive graphic work shirt over striped long-sleeve tee, cargo trousers, sneakers, canvas laptop strap across chest; plain grey studio background, 8K. Not resembling any real actor.",
            },
            {
                "tag": "@Onle",
                "name": "Onle (Thợ máy gầm bệ)",
                "default_media_id": "5a83756f-9ebb-4e2d-8ed5-89c313dc6976",
                "locked_media_id": "5a83756f-9ebb-4e2d-8ed5-89c313dc6976",
                "description": "Onle (30 tuổi): thợ máy gầm bệ và tay lái bọc hậu điềm tĩnh của đội; cao 182 cm, vai rộng vạm vỡ, tóc đen cắt sát, râu dê gọn gàng, mặc bộ đồ liền thân thợ máy màu xanh rêu đậm buộc ngang hông bên ngoài áo thun đen.",
                "ref_prompt": "Full-body photorealistic character reference of @Onle, a 30-year-old man, 182 cm, broad-shouldered mechanic build, closely cropped dark hair, neat goatee, calm steady dark eyes, grease-weathered hands, grease-stained dark-green mechanic jumpsuit tied at the waist over a black T-shirt, heavy work boots; plain grey studio background, 8K. Not resembling any real actor.",
            },
            {
                "tag": "@NyTran",
                "name": "Ny Trần (Trùm Light Saigon)",
                "default_media_id": "bdd1b074-3809-46ac-963d-7ffc1d800d7c",
                "locked_media_id": "bdd1b074-3809-46ac-963d-7ffc1d800d7c",
                "description": "Ny Tran (30 tuổi): thủ lĩnh băng mô tô Light Saigon tại Little Saigon; cao 177 cm, gò má sắc, tóc đen undercut vuốt ngược bóng mượt, ánh mắt lạnh lùng, đeo dây chuyền vàng mảnh, mặc áo khoác da đen họa tiết da rắn bên ngoài sơ mi lụa đỏ sẫm mở cổ.",
                "ref_prompt": "Full-body photorealistic character reference of @NyTran, a 30-year-old Vietnamese man, 177 cm, lean sharp build, sharp cheekbones, sleek undercut slicked-back black hair, cold calculating dark eyes, thin gold neck chain, tailored black snake-pattern leather jacket over open-collar crimson silk shirt, black trousers, polished boots; plain grey studio background, 8K. Not resembling any real actor.",
            },
            {
                "tag": "@Cela",
                "name": "Cela (Anh họ Ny Trần)",
                "default_media_id": "d977c3f5-1225-4caa-8772-39b2588a71f3",
                "locked_media_id": "d977c3f5-1225-4caa-8772-39b2588a71f3",
                "description": "Cela (31 tuổi): anh họ và tay chân thân cận của Ny Tran; cao 174 cm, cơ bắp chắc nịch, tóc cạo hai bên buộc chỏm ngắn trên đỉnh, sẹo chéo bên má phải, hình xăm rồng kín cẳng tay phải, mặc áo ghi-lê da đen sát nách bên ngoài áo tối màu.",
                "ref_prompt": "Full-body photorealistic character reference of @Cela, a 31-year-old Vietnamese man, 174 cm, compact muscular build, shaved sides with a tied short topknot, narrow watchful eyes, diagonal scar across right cheek, dragon tattoo sleeve on right forearm, sleeveless black leather vest over dark shirt, black jeans, riding boots; plain grey studio background, 8K. Not resembling any real actor.",
            },
            {
                "tag": "@Nese",
                "name": "Trung sĩ Nese (LAPD)",
                "default_media_id": "823abd75-2434-4f07-8812-70ed808cb67b",
                "locked_media_id": "823abd75-2434-4f07-8812-70ed808cb67b",
                "description": "Trung sĩ Nese (46 tuổi): chỉ huy trực tiếp của Tom trong LAPD; cao 180 cm, dáng vẻ dày dạn sương gió, tóc cắt ngắn điểm bạc, ria mép tỉa gọn, mặc sơ mi trắng xắn tay nới lỏng cà vạt tối màu, đeo bao huy hiệu ở thắt lưng.",
                "ref_prompt": "Full-body photorealistic character reference of @Nese, a 46-year-old veteran police sergeant, 180 cm, solid build, greying crew-cut hair, weathered lined face, stern focused eyes, trimmed moustache, rolled-sleeve white dress shirt with loosened dark tie, badge holder at belt, charcoal trousers, leather shoes; plain grey studio background, 8K. Not resembling any real actor.",
            },
            {
                "tag": "@Kinan",
                "name": "Đặc vụ Kinan (FBI)",
                "default_media_id": "ea56efae-cf13-48ad-a069-dfa421e96a36",
                "locked_media_id": "ea56efae-cf13-48ad-a069-dfa421e96a36",
                "description": "Đặc vụ liên bang Kinan (44 tuổi): chỉ huy lực lượng đặc nhiệm FBI phối hợp điều tra; cao 178 cm, dáng thẳng nghiêm nghị, tóc nâu sẫm rẽ ngôi gọn, đeo kính gọng kim loại mảnh, mặc bộ vest xám than tối màu bên ngoài sơ mi xanh thép không thắt cà vạt.",
                "ref_prompt": "Full-body photorealistic character reference of @Kinan, a 44-year-old federal agent, 178 cm, trim upright build, neatly parted dark-brown hair, sharp angular features, piercing gaze, thin metal-frame glasses, tailored dark charcoal suit over steel-blue shirt without tie, federal credential folder at side; plain grey studio background, 8K. Not resembling any real actor.",
            },
            {
                "tag": "@Verni",
                "name": "Verni (Tài xế container)",
                "default_media_id": "79ff8afe-97f5-4165-a602-d42d1b1a8d70",
                "locked_media_id": "79ff8afe-97f5-4165-a602-d42d1b1a8d70",
                "description": "Verni (48 tuổi): tài xế xe container 18 bánh đường dài trên xa lộ Interstate 10; cao 173 cm, lồng ngực vạm vỡ, râu quai nón dày điểm bạc, gương mặt rám nắng phong sương, đội mũ lưỡi trai tài xế, mặc áo sơ mi kẻ caro bên trong áo ghi-lê bảo hộ màu nâu.",
                "ref_prompt": "Full-body photorealistic character reference of @Verni, a 48-year-old stocky long-haul truck driver, 173 cm, barrel-chested build, strong forearms, thick grey-streaked beard, sun-weathered face, defiant eyes, receding hair under a worn trucker cap, plaid flannel shirt under a padded brown work vest, dark jeans, heavy boots; plain grey studio background, 8K. Not resembling any real actor.",
            },
        ],
    },
    {
        "slug": "bi-mat-phong-613",
        "name": "Bí Mật Phòng 613: Lời Cảnh Báo Đêm Rằm",
        "project_id": "daf9939b-35f2-4d6c-a299-8efcabc3fc9a",
        "aspect_ratio": "VIDEO_ASPECT_RATIO_LANDSCAPE",
        "runner_script": "runners/bi_mat_phong_613.py",
        "series_dir": "bi-mat-phong-613",
        "ep_prefix": "canh",
        "description": "Phim ngắn tâm lý bí ẩn 15 phút lấy cảm hứng từ Phim ngắn 613: hai nữ sinh Phương và Trinh dọn vào phòng 613 chung cư cũ, đối mặt cô gái áo trắng Linh và vạch trần bí mật đêm cháy 03/11/2016 của Ông Bảy Bảo Vệ (16:9, 15 cảnh × 6 clips × 10s = 90 clips — Google Flow Omni v3.1, Giọng Chuẩn Bắc).",
        "characters": [
            {
                "tag": "@Phuong",
                "name": "Phương (Sinh viên Thiết kế, 22 tuổi)",
                "default_media_id": "41e63b7c-cd0b-47c9-94f2-c4fb84931f67",
                "locked_media_id": "41e63b7c-cd0b-47c9-94f2-c4fb84931f67",
                "description": "Nữ sinh viên 22 tuổi dịu dàng, nhạy cảm tâm linh; cao 160 cm, gương mặt trái xoan thanh tú, đôi mắt to biểu cảm, cài băng đô vải màu kem trên mái tóc đen dài xõa tự nhiên, mặc áo cardigan len mỏng màu kem khoác ngoài áo thun trắng và quần jean ống rộng xanh nhạt.",
                "ref_prompt": "Full-body photorealistic character reference of @Phuong, a 22-year-old Vietnamese female university student, 160 cm, slender petite build, gentle oval face, large expressive dark eyes, long straight black hair worn down with a neat cream fabric headband, wearing a soft cream knit cardigan over a plain white cotton T-shirt, light-blue wide-leg jeans, and white canvas sneakers; plain grey studio background, soft cinematic side light, 8K. Not resembling any real actor.",
            },
            {
                "tag": "@Trinh",
                "name": "Trinh (Bạn cùng phòng, 22 tuổi)",
                "default_media_id": "db08140d-6d7f-4e21-958c-253afd08f81d",
                "locked_media_id": "db08140d-6d7f-4e21-958c-253afd08f81d",
                "description": "Bạn thân cùng phòng của Phương, 22 tuổi, sinh viên Báo chí cá tính, thực tế; cao 165 cm, dáng thon khỏe, gương mặt sắc sảo, tóc đen dài thẳng rẽ ngôi giữa, mặc áo thun form rộng màu cam đất (burnt orange) và quần jogger xám đậm.",
                "ref_prompt": "Full-body photorealistic character reference of @Trinh, a 22-year-old Vietnamese female student, 165 cm, lean athletic build, sharp confident facial features, attentive dark eyes, long straight black hair parted in the middle, wearing an oversized burnt-orange cotton T-shirt, dark charcoal-grey jogger trousers, and dark slides; plain grey studio background, soft cinematic side light, 8K. Not resembling any real actor.",
            },
            {
                "tag": "@BacBaoVe",
                "name": "Ông Bảy Bảo Vệ (Bảo vệ trực đêm Lô C, 58 tuổi)",
                "default_media_id": "e31adf0c-91da-4077-b996-2089e52fcaf0",
                "locked_media_id": "e31adf0c-91da-4077-b996-2089e52fcaf0",
                "description": "Bảo vệ trực đêm chung cư cũ Lô C, 58 tuổi; cao 168 cm, dáng hơi gù, tóc cắt ngắn điểm bạc, gương mặt gầy góc cạnh lạnh lùng, vết sẹo bỏng mờ bên cổ trái, mặc đồng phục bảo vệ xanh đen sẫm, cầm chùm chìa khóa đồng cũ và đèn pin vỏ sắt.",
                "ref_prompt": "Full-body photorealistic character reference of @BacBaoVe, a 58-year-old Vietnamese night-shift security guard, 168 cm, thin slightly stooped build, short grey-streaked black hair, gaunt angular weathered face, cold watchful eyes, a faint old burn scar on the left side of his neck, wearing a dark navy-black short-sleeve security guard uniform shirt with shoulder epaulettes, dark trousers, worn black shoes, holding an old brass key ring in one hand and a heavy metal flashlight in the other; plain grey studio background, hard side light, 8K. Not resembling any real actor.",
            },
            {
                "tag": "@BongAoTrang",
                "name": "Linh — Cô Gái Áo Trắng Phòng 613 (21 tuổi)",
                "default_media_id": "435283fa-da21-430a-9649-0ecc8413c38b",
                "locked_media_id": "435283fa-da21-430a-9649-0ecc8413c38b",
                "description": "Nữ sinh viên nhạc viện từng thuê phòng 613 năm 2016; cao 162 cm, dáng mảnh mai, làn da trắng xanh tĩnh lặng, tóc đen dài xõa ngang lưng, mặc đầm vải voan trắng dài tay cổ vuông cổ điển, cổ tay phải đeo vòng chỉ đỏ gắn chuông bạc nhỏ, ánh mắt u buồn khẩn thiết.",
                "ref_prompt": "Full-body photorealistic character reference of @BongAoTrang, a 21-year-old Vietnamese woman, 162 cm, slender delicate build, pale porcelain skin with natural realistic texture, sorrowful expressive dark eyes, long straight black hair resting over her shoulders, wearing a clean vintage ankle-length off-white long-sleeve square-neck cotton dress, barefoot, with a thin red thread bracelet and tiny silver bell on her right wrist; plain grey studio background, cool moonlight side light, 8K. Clean cinematic appearance, no gore, no blood. Not resembling any real actor.",
            },
        ],
    },
    {
        "slug": "oan-thai-doi-me",
        "name": "Oán Thai Đòi Mẹ: Búp Bê Đất Nung",
        "project_id": "dedf1a01-6d2f-420c-bff0-f486b3ea12cc",
        "aspect_ratio": "VIDEO_ASPECT_RATIO_LANDSCAPE",
        "runner_script": "runners/oan_thai_doi_me.py",
        "series_dir": "oan-thai-doi-me",
        "ep_prefix": "canh",
        "description": "Phim ngắn kinh dị tâm linh cổ thuật 14 phút lấy cảm hứng từ Oán Thai Đòi Mẹ (Mudborn): Bách mang pho tượng đất nung không mắt từ lò bầu cổ bỏ hoang cuối bãi tha ma ven sông về nhà, người vợ mang thai Hà lỡ tay trám mất huyết ấn sau lưng tượng và điểm mắt lúc 2 giờ sáng (16:9, 14 cảnh × 6 clips × 10s = 84 clips — Google Flow Omni 10s, 80% Người dẫn chuyện VO + 20% Thoại nhân vật bất ngờ, Giọng Chuẩn Miền Bắc).",
        "characters": [
            {
                "tag": "@Bach",
                "name": "Bách (Kỹ sư quét 3D LiDAR, 30 tuổi)",
                "default_media_id": "",
                "locked_media_id": "",
                "description": "Nam kỹ sư quét 3D không gian 30 tuổi; cao 175 cm, dáng gầy săn chắc, gương mặt góc cạnh lo âu, đeo kính gọng kim loại mảnh, tóc đen ngắn rẽ ngôi tự nhiên, mặc áo khoác gió màu xám than bên ngoài áo thun đen, cầm máy quét 3D LiDAR cầm tay.",
                "ref_prompt": "Full-body photorealistic character reference of @Bach, a 30-year-old Vietnamese male 3D spatial scanning engineer, 175 cm, lean build, angular face with tired attentive dark eyes behind thin metal-frame glasses, short natural parted black hair, wearing a charcoal-grey windbreaker jacket over a plain black crew-neck T-shirt, dark cargo trousers, and dusty hiking boots, carrying a compact handheld 3D LiDAR scanner; plain grey studio background, soft cinematic side light, 8K. Not resembling any real actor.",
            },
            {
                "tag": "@Ha",
                "name": "Hà (Nghệ nhân phục chế gốm cổ, mang thai tháng thứ 7, 28 tuổi)",
                "default_media_id": "",
                "locked_media_id": "",
                "description": "Nữ nghệ nhân phục chế gốm cổ 28 tuổi đang mang thai tháng thứ 7; cao 162 cm, gương mặt trái xoan dịu dàng nhưng xanh xao, tóc đen dài búi thấp cài trâm gỗ, mặc váy bầu vải đũi màu kem nhạt khoác tạp dề vải bố nâu lấm đất sét khô.",
                "ref_prompt": "Full-body photorealistic character reference of @Ha, a 28-year-old pregnant Vietnamese female antique ceramic conservator (7 months pregnant), 162 cm, gentle oval face with pale complexion and expressive sorrowful dark eyes, long black hair pinned in a low bun with a wooden hairpin, wearing a loose cream-beige linen maternity dress with a brown canvas studio apron smudged with dried terracotta clay over her visible 7-month pregnant belly, flat indoor cloth slippers; plain grey studio background, soft side light, 8K. Not resembling any real actor.",
            },
            {
                "tag": "@ThayPhong",
                "name": "Thầy Phong (Nhà nghiên cứu cổ tự & Pháp sư trấn yểm, 36 tuổi)",
                "default_media_id": "",
                "locked_media_id": "",
                "description": "Nhà nghiên cứu cổ tự và pháp sư trấn yểm 36 tuổi; cao 174 cm, dáng điềm tĩnh sắc lạnh, tóc đen cắt gọn, mặc áo sơ mi cổ tàu màu chàm tối, cổ tay trái đeo chuỗi hạt gỗ mun 108 hạt, cầm la bàn đồng phong thủy cổ.",
                "ref_prompt": "Full-body photorealistic character reference of @ThayPhong, a 36-year-old Vietnamese folklore scholar and Taoist ritual master, 174 cm, composed athletic build, sharp cheekbones, calm piercing dark eyes, neat short black hair, wearing a dark indigo-black stand-collar linen shirt (áo sơ mi cổ tàu tối màu), dark trousers, a 108-bead black ebony prayer mala around his left wrist, holding an antique brass geomancy compass (la bàn đồng); plain grey studio background, soft side light, 8K. Not resembling any real actor.",
            },
            {
                "tag": "@BaLua",
                "name": "Bà Lụa (Oán Linh Người Thợ Gốm Năm 1996, 32 tuổi)",
                "default_media_id": "",
                "locked_media_id": "",
                "description": "Vong hồn người thợ gốm truyền thống năm 1996, 32 tuổi; cao 158 cm, gương mặt gầy u buồn phủ tro bếp xám trắng, tóc đen dài xõa che nửa má, mặc áo cánh nâu sồng truyền thống và quần đen lấm đất sét khô, hai bàn tay nứt nẻ.",
                "ref_prompt": "Full-body photorealistic character reference of @BaLua, a 32-year-old traditional Northern Vietnamese female potter from the 1990s, 158 cm, gaunt sorrowful face dusted with pale grey kiln ash, tearful dark eyes, long disheveled black hair partly covering one cheek, wearing a weathered dark-brown traditional Vietnamese cotton blouse (áo cánh nâu sồng) and black trousers stained with dried grey clay, calloused clay-crusted hands, barefoot; plain grey studio background, cool moonlit side light, 8K. Clean cinematic ghost appearance, no gore.",
            },
        ],
    },
    {
        "slug": "can-nha-am-duong",
        "name": "Căn Nhà Âm Dương (HẺM Truyện Ma — MC Đình Soạn)",
        "project_id": "3b955883-7851-42fe-a986-5ef82b4912e5",
        "aspect_ratio": "VIDEO_ASPECT_RATIO_LANDSCAPE",
        "runner_script": "runners/can_nha_am_duong.py",
        "series_dir": "can-nha-am-duong",
        "ep_prefix": "canh",
        "description": "Phim ngắn kinh dị tâm linh dân gian Việt Nam 15 phút (Tác giả: Thu Thảo — Giọng kể chuyện ma MC Đình Soạn HẺM Truyện Ma VOICE_LOCK_NARRATOR_CNHADG chuẩn miền Bắc): Bình thua lỗ tiền ảo hơn 400 triệu trốn về căn nhà ngói ba gian bỏ hoang gần 20 năm của ông nội dưới gốc mít cổ thụ âm u (16:9, 15 cảnh × 6 clips × 10s = 90 clips — Google Flow Omni 10s, 80% VO + 20% Lip-Sync).",
        "characters": [
            {
                "tag": "@Binh",
                "name": "Bình (Sinh viên 21 tuổi — VOICE_LOCK_BINH_CNHADG)",
                "default_media_id": "a1a78643-ce72-4217-86c7-b53b927e637a",
                "locked_media_id": "a1a78643-ce72-4217-86c7-b53b927e637a",
                "voice_lock": "VOICE_LOCK_BINH_CNHADG",
                "description": "Nam sinh viên năm cuối 21 tuổi; 172 cm, dáng gầy nhợt nhạt, tóc đen ngắn rối, quầng mắt thâm, mặc áo hoodie xám bạc bên ngoài áo thun trắng nhàu, quần jean tối, đeo ba lô đen. Giọng thoại: VOICE_LOCK_BINH_CNHADG (Nam trẻ 21t chuẩn miền Bắc ~135Hz, run rẩy, nghẹn ngào).",
                "ref_prompt": "Full-body photorealistic character reference of @Binh, a 21-year-old Vietnamese male university student, 172 cm, thin pale build, messy short black hair, tired dark eyes with visible dark circles underneath, wearing a faded grey hoodie over a wrinkled white T-shirt, dark slim jeans, worn sneakers, carrying a black backpack; anxious guilty expression; plain grey studio background, soft cinematic side light, 8K. Not resembling any real actor.",
            },
            {
                "tag": "@BaPhuong",
                "name": "Bà Phượng (Mẹ Bình, giáo viên về hưu, 50 tuổi — VOICE_LOCK_PHUONG_CNHADG)",
                "default_media_id": "a17f2e3b-8272-4cff-8de0-1c3ec43a11b1",
                "locked_media_id": "a17f2e3b-8272-4cff-8de0-1c3ec43a11b1",
                "voice_lock": "VOICE_LOCK_PHUONG_CNHADG",
                "description": "Nữ giáo viên về hưu 50 tuổi; 158 cm, tóc đen búi thấp lấm tấm bạc, gương mặt trái xoan nhân hậu nhưng phiền muộn, mặc áo sơ mi giản dị và quần tối. Giọng thoại: VOICE_LOCK_PHUONG_CNHADG (Nữ trung niên 50t chuẩn miền Bắc ~205Hz, ấm áp, nghẹn ngào).",
                "ref_prompt": "Full-body photorealistic character reference of @BaPhuong, a 50-year-old Vietnamese female retired school teacher, 158 cm, neat black hair in a low bun with grey streaks, gentle worried oval face, wearing a simple pastel blouse and dark trousers, indoor slippers; plain grey studio background, soft side light, 8K. Not resembling any real actor.",
            },
            {
                "tag": "@OngQuan",
                "name": "Ông Quân (Bố Bình, 55 tuổi — VOICE_LOCK_QUAN_CNHADG)",
                "default_media_id": "e845a88f-7cd2-4b8f-9fa3-e75e7e337674",
                "locked_media_id": "e845a88f-7cd2-4b8f-9fa3-e75e7e337674",
                "voice_lock": "VOICE_LOCK_QUAN_CNHADG",
                "description": "Nam nhân viên văn phòng 55 tuổi; 170 cm, dáng chắc, tóc húi cua bạc, gương mặt đanh nghiêm khắc, mặc áo sơ mi cổ cồn và quần tối. Giọng thoại: VOICE_LOCK_QUAN_CNHADG (Nam trung niên 55t chuẩn miền Bắc ~105Hz, trầm đanh, uy nghiêm).",
                "ref_prompt": "Full-body photorealistic character reference of @OngQuan, a 55-year-old Vietnamese male office worker, 170 cm, stocky build, crew-cut greying hair, stern weathered face with deep frown lines, wearing a collared dress shirt with sleeves rolled and dark trousers, leather belt; plain grey studio background, hard side light, 8K. Not resembling any real actor.",
            },
            {
                "tag": "@OngBay",
                "name": "Ông Bảy (Nông dân hàng xóm, 60 tuổi — VOICE_LOCK_BAY_CNHADG)",
                "default_media_id": "10e5cdcf-3dd1-4b41-b999-21922b65de89",
                "locked_media_id": "10e5cdcf-3dd1-4b41-b999-21922b65de89",
                "voice_lock": "VOICE_LOCK_BAY_CNHADG",
                "description": "Nam nông dân 60 tuổi; 168 cm, da ngăm đen, tóc bạc lấm tấm, gương mặt hiền hậu nhiều nếp nhăn, mặc áo sơ mi kẻ cũ và quần nâu, đi dép cao su. Giọng thoại: VOICE_LOCK_BAY_CNHADG (Bác nông dân 60t chuẩn miền Bắc ~115Hz, mộc mạc, ấm áp).",
                "ref_prompt": "Full-body photorealistic character reference of @OngBay, a 60-year-old Vietnamese male rice farmer, 168 cm, lean tanned dark-skinned build, silver-streaked hair, kind wrinkled face with warm eyes, wearing a faded plaid button-up shirt and brown work trousers, rubber sandals; plain grey studio background, warm side light, 8K. Not resembling any real actor.",
            },
            {
                "tag": "@VongCuXa",
                "name": "Vong Cụ Xá (Ông nội Bình, 80 tuổi — VOICE_LOCK_CUXA_CNHADG)",
                "default_media_id": "f8d1ff26-6134-4fa4-8c0f-13e8405e5f64",
                "locked_media_id": "f8d1ff26-6134-4fa4-8c0f-13e8405e5f64",
                "voice_lock": "VOICE_LOCK_CUXA_CNHADG",
                "description": "Vong hồn ông nội; gầy gò mờ ảo bán trong suốt, tóc trắng thưa, mắt tối buồn sâu hoắm, mặc áo bà ba nâu sồng truyền thống đã bạc, chân trần. Giọng thoại: VOICE_LOCK_CUXA_CNHADG (Cụ già 80t chuẩn miền Bắc ~98Hz, khàn đục, vọng âm).",
                "ref_prompt": "Full-body photorealistic character reference of @VongCuXa, a ghostly translucent elderly Vietnamese male apparition, gaunt frail frame, wispy white hair, sad hollow dark eyes, wearing a faded traditional brown cotton tunic (áo bà ba nâu sồng), barefoot; semi-transparent ethereal ghost appearance with faint moonlight glow; plain dark studio background, cold blue-white rim light, 8K. Not resembling any real actor.",
            },
            {
                "tag": "@VongLa",
                "name": "Vong Lạ Dưới Gốc Mít (Oán linh 28 tuổi — VOICE_LOCK_VONGLA_CNHADG)",
                "default_media_id": "0c2ade1f-c1cd-4c93-98e2-697231a54887",
                "locked_media_id": "0c2ade1f-c1cd-4c93-98e2-697231a54887",
                "voice_lock": "VOICE_LOCK_VONGLA_CNHADG",
                "description": "Vong hồn vất vưởng dưới gốc mít cổ thụ đầu cổng; bóng người cao gầy như que củi, da xám ngoét ướt đẫm sương đêm, tóc rối bết che nửa mặt, bàn tay xương xẩu có những ngón tay dài ngoằng lạnh buốt. Giọng thoại: VOICE_LOCK_VONGLA_CNHADG (Giọng ma vọng lạnh lẽo chuẩn miền Bắc).",
                "ref_prompt": "Full-body photorealistic character reference of @VongLa, a terrifying wandering Vietnamese spirit entity, tall skeletal emaciated silhouette, ash-grey damp skin, tangled wet black hair covering half the face, glowing pale eyes in shadow, tattered dark wet clothes, long bony fingers; plain dark studio background, eerie cyan-green rim light, 8K. Not resembling any real actor.",
            },
        ],
    },
    {
        "slug": "tieng-go-dem-ba-gio",
        "name": "Tiếng Gõ Đêm Ba Giờ: Lời Nguyền Giếng Đá Ong (HẺM Truyện Ma — MC Đình Soạn)",
        "project_id": "8a346c86-311f-47ae-8ccb-2d716a58c945",
        "aspect_ratio": "VIDEO_ASPECT_RATIO_LANDSCAPE",
        "runner_script": "runners/tieng_go_dem_ba_gio.py",
        "series_dir": "tieng-go-dem-ba-gio",
        "ep_prefix": "canh",
        "description": "Phim ngắn kinh dị tâm linh dân gian Bắc Bộ 15 phút (Giọng kể chuyện ma MC Đình Soạn HẺM Truyện Ma VOICE_LOCK_NARRATOR_TIENGGO chuẩn miền Bắc): Vũ Đình Lâm trông coi nhà cổ gỗ lim ba gian trong 3 đêm mưa ngâu tháng Bảy và đối mặt lời nguyền chiếc giếng đá ong lúc 3 giờ sáng (16:9, 15 cảnh × 6 clips × 10s = 90 clips — Google Flow Omni 10s, 80% VO + 20% Lip-Sync).",
        "characters": [
            {
                "tag": "@Lam",
                "name": "Vũ Đình Lâm (Nhiếp ảnh gia kiến trúc cổ, 27 tuổi — VOICE_LOCK_LAM_TIENGGO)",
                "default_media_id": "bf3d7dc9-c123-45eb-be8b-cd6196d35011",
                "locked_media_id": "bf3d7dc9-c123-45eb-be8b-cd6196d35011",
                "voice_lock": "VOICE_LOCK_LAM_TIENGGO",
                "description": "Nam nhiếp ảnh gia khảo sát kiến trúc cổ 27 tuổi; cao 174 cm, dáng gầy săn chắc, gương mặt góc cạnh tái nhợt đeo kính gọng mảnh, mặc áo khoác xanh rêu sẫm bên ngoài sơ mi xám, đeo túi da, cầm đèn pin đồng cổ. Giọng thoại: VOICE_LOCK_LAM_TIENGGO (Nam 27t chuẩn miền Bắc ~125Hz, trầm ấm, gấp gáp khi kinh hoàng).",
                "ref_prompt": "Full-body photorealistic character reference of @Lam, a 27-year-old Vietnamese male antique architecture conservator, 174 cm, lean build, pale angular face with attentive dark eyes behind thin metal-frame glasses, neat parted black hair, wearing a dark olive-green field jacket over a charcoal-grey collared shirt, dark trousers, leather satchel strap across his chest, holding a vintage brass flashlight emitting a warm amber beam; plain grey studio background, soft side light, 8K. Not resembling any real actor.",
            },
            {
                "tag": "@BaCam",
                "name": "Bà Cầm (Bà quản gia giữ nhà từ đường, 78 tuổi — VOICE_LOCK_BACAM_TIENGGO)",
                "default_media_id": "71231f5c-64e2-4c4c-945e-059ee37903f7",
                "locked_media_id": "71231f5c-64e2-4c4c-945e-059ee37903f7",
                "voice_lock": "VOICE_LOCK_BACAM_TIENGGO",
                "description": "Bà quản gia già 78 tuổi giữ nhà từ đường; dáng lưng còng, tóc bạc búi trâm gỗ mun, mắt trái kéo mây trắng đục (mù), mặc áo bà ba nâu đen, tay cầm đèn dầu đồng leo lét. Giọng thoại: VOICE_LOCK_BACAM_TIENGGO (Bà lão 78t chuẩn miền Bắc ~175Hz, khàn đặc, chậm rãi, lạnh gáy).",
                "ref_prompt": "Full-body photorealistic character reference of @BaCam, a 78-year-old Northern Vietnamese female caretaker of an ancestral temple, stooped posture, deeply wrinkled weathered face, silver hair pinned in a tight low bun with a black ebony hairpin, left eye cloudy milky-white blind and right eye sharp, wearing a dark earth-brown traditional Vietnamese tunic (áo bà ba nâu sẫm) and black silk trousers, holding a flickering antique brass oil lamp; plain grey studio background, soft side light, 8K. Not resembling any real actor.",
            },
            {
                "tag": "@CuTu",
                "name": "Cụ Từ Hạc (Cụ già giữ đền cổ, 85 tuổi — VOICE_LOCK_CUTU_TIENGGO)",
                "default_media_id": "17de0dcd-36c5-4c0c-8a9a-da1766a23268",
                "locked_media_id": "17de0dcd-36c5-4c0c-8a9a-da1766a23268",
                "voice_lock": "VOICE_LOCK_CUTU_TIENGGO",
                "description": "Cụ già giữ đền cổ 85 tuổi; râu bạc dài trước ngực, gương mặt nghiêm nghị sắc lạnh, mặc áo gấm đen truyền thống đội khăn xếp đen, cầm chuông đồng trấn hồn. Giọng thoại: VOICE_LOCK_CUTU_TIENGGO (Cụ già 85t chuẩn miền Bắc ~100Hz, trầm hùng, đanh thép, uy nghiêm).",
                "ref_prompt": "Full-body photorealistic character reference of @CuTu, an 85-year-old traditional Northern Vietnamese clan patriarch, gaunt stern face with high cheekbones, long silver beard reaching his chest, calm piercing dark eyes, wearing a traditional black silk brocade robe (áo gấm đen truyền thống) and black folded turban headdress (khăn xếp đen); plain grey studio background, soft side light, 8K.",
            },
            {
                "tag": "@CoUt",
                "name": "Oan Hồn Cô Út Nhài (Thiếu nữ dưới đáy giếng đá ong, 19 tuổi — VOICE_LOCK_COUT_TIENGGO)",
                "default_media_id": "9bdbd6ce-ef97-4c01-98e0-8b97370abd22",
                "locked_media_id": "9bdbd6ce-ef97-4c01-98e0-8b97370abd22",
                "voice_lock": "VOICE_LOCK_COUT_TIENGGO",
                "description": "Oán linh cô gái trẻ 19 tuổi bị trấn yểm dưới giếng đá ong 50 năm trước; da trắng bệch ướt sũng nước mưa, tóc đen dài che nửa mặt, mặc áo lụa trắng ngả màu bùn nước, cổ tay mang vòng xích sắt rỉ. Giọng thoại: VOICE_LOCK_COUT_TIENGGO (Thiếu nữ 19t chuẩn miền Bắc ~230Hz, trong trẻo pha tiếng vọng đáy giếng ai oán).",
                "ref_prompt": "Full-body photorealistic character reference of @CoUt, a 19-year-old tragic Northern Vietnamese maiden apparition, 160 cm, pale water-drenched porcelain skin, long wet black hair clinging to her cheeks, sorrowful dark eyes, wearing a water-soaked mud-stained off-white traditional Vietnamese silk dress, a rusted iron chain cuff with broken links on her wrist, barefoot; plain grey studio background, cool moonlit side light, 8K. Clean cinematic ghost appearance, no gore.",
            },
        ],
    },
    {
        "slug": "ma-da-dam-sen",
        "name": "Ma Da Đầm Sen: Lời Nguyền Tháng Bảy (HẺM Truyện Ma — MC Đình Soạn)",
        "project_id": "de6d15c5-b94e-4b5d-b854-649c6ba8d02d",
        "aspect_ratio": "VIDEO_ASPECT_RATIO_LANDSCAPE",
        "runner_script": "runners/ma_da_dam_sen.py",
        "series_dir": "ma-da-dam-sen",
        "ep_prefix": "canh",
        "description": "Phim ngắn kinh dị tâm linh dân gian Bắc Bộ 15 phút (kịch bản gốc; giọng kể chuẩn MC Đình Soạn HẺM Truyện Ma VOICE_LOCK_NARRATOR_MADA): ma da đầm sen đòi người thế mạng mỗi tháng bảy, và cái chết oan của cô gái mồ côi Thắm ba mươi năm trước (16:9, 15 cảnh × 6 clips × 10s = 90 clips — 77% VO + 23% Lip-Sync).",
        "characters": [
            {
                "tag": "@Ngan",
                "name": "Ngân (Cô giáo trẻ, 26 tuổi — VOICE_LOCK_NGAN_MADA)",
                "default_media_id": "25a39418-a4c6-4522-ab1a-14a441c02ec7",
                "locked_media_id": "25a39418-a4c6-4522-ab1a-14a441c02ec7",
                "voice_lock": "VOICE_LOCK_NGAN_MADA",
                "description": "Cô giáo tiểu học 26 tuổi từ thành phố về quê; dáng mảnh, tóc đen thẳng buộc thấp, ánh mắt điềm tĩnh cương quyết; áo blouse cộc tay màu kem, quần nâu sẫm, dép quai hậu, túi vải đeo vai. Giọng thoại: VOICE_LOCK_NGAN_MADA.",
                "ref_prompt": "Full-body photorealistic character reference of @Ngan, a 26-year-old Vietnamese female primary-school teacher, 160 cm, slim build, straight black hair tied low at the neck, calm determined dark eyes, natural oval face, wearing a cream short-sleeve blouse, dark-brown trousers, flat sandals and a small cloth shoulder bag; plain grey studio background, soft cinematic side light, 8K. Not resembling any real actor."
            },
            {
                "tag": "@Khoi",
                "name": "Khôi (Em trai Ngân, 19 tuổi — VOICE_LOCK_KHOI_MADA)",
                "default_media_id": "ebf480b6-29bd-45e5-a459-1c7658d56bb2",
                "locked_media_id": "ebf480b6-29bd-45e5-a459-1c7658d56bb2",
                "voice_lock": "VOICE_LOCK_KHOI_MADA",
                "description": "Em trai Ngân, sinh viên 19 tuổi về quê nghỉ hè; cao gầy, tóc đen ngắn rối, mặt xanh xao mệt mỏi; áo phông xanh than bạc màu, quần đùi xám, dép tổ ong trắng. Giọng thoại: VOICE_LOCK_KHOI_MADA.",
                "ref_prompt": "Full-body photorealistic character reference of @Khoi, a 19-year-old Vietnamese male university student, 174 cm, lanky build, short tousled black hair, pale tired face with dark circles, wearing a faded navy T-shirt, grey shorts and white plastic honeycomb sandals; plain grey studio background, soft cinematic side light, 8K. Not resembling any real actor."
            },
            {
                "tag": "@BaHanh",
                "name": "Bà Hạnh (Bà nội, 74 tuổi — VOICE_LOCK_HANH_MADA)",
                "default_media_id": "f096bc66-c159-4435-8a28-58a2f27663cc",
                "locked_media_id": "f096bc66-c159-4435-8a28-58a2f27663cc",
                "voice_lock": "VOICE_LOCK_HANH_MADA",
                "description": "Bà nội của Ngân và Khôi, 74 tuổi; nhỏ người, lưng còng, tóc bạc búi thấp dưới khăn nhung đen, gương mặt hiền nhiều nếp nhăn; áo cánh nâu, quần đen, tràng hạt gỗ ở cổ tay. Giọng thoại: VOICE_LOCK_HANH_MADA.",
                "ref_prompt": "Full-body photorealistic character reference of @BaHanh, a 74-year-old Vietnamese grandmother, 148 cm, small and slightly stooped, silver hair in a low bun under a black velvet headband, deep-lined gentle face, wearing a brown traditional áo cánh blouse and black trousers, wooden prayer beads on her wrist, barefoot in wooden clogs; plain grey studio background, warm soft side light, 8K. Not resembling any real actor."
            },
            {
                "tag": "@OngLy",
                "name": "Ông Lý (Cựu trưởng thôn, 72 tuổi — VOICE_LOCK_LY_MADA)",
                "default_media_id": "dde3cdc7-d3ad-4f81-b5de-30ec960275b0",
                "locked_media_id": "dde3cdc7-d3ad-4f81-b5de-30ec960275b0",
                "voice_lock": "VOICE_LOCK_LY_MADA",
                "description": "Cựu trưởng thôn 72 tuổi; cao gầy, tóc bạc chải ngược, mắt hẹp sắc lạnh; áo khoác cổ bẻ màu xanh rêu bạc màu ngoài áo may ô trắng, quần sẫm, chống gậy gỗ chạm. Giọng thoại: VOICE_LOCK_LY_MADA.",
                "ref_prompt": "Full-body photorealistic character reference of @OngLy, a 72-year-old Vietnamese former village chief, 176 cm, tall and gaunt, slicked-back grey hair, hard narrow eyes, deep frown lines, wearing a faded olive-green collared jacket over a white undershirt, dark trousers, holding a carved wooden walking cane; plain grey studio background, hard side light, 8K. Not resembling any real actor."
            },
            {
                "tag": "@CoTham",
                "name": "Vong Thắm (Cô gái chết đuối oan dưới đầm sen — VOICE_LOCK_THAM_MADA)",
                "default_media_id": "58f52ee3-e16b-4024-9740-c2173e4284f0",
                "locked_media_id": "58f52ee3-e16b-4024-9740-c2173e4284f0",
                "voice_lock": "VOICE_LOCK_THAM_MADA",
                "description": "Vong hồn Thắm, cô gái mồ côi chết đuối oan ở đầm sen ba mươi năm trước; da trắng bệch ướt sũng, tóc đen dài ướt quấn cuống sen, mắt buồn thăm thẳm; áo bà ba trắng ướt sũng, quần đen, chân trần. Giọng thoại: VOICE_LOCK_THAM_MADA.",
                "ref_prompt": "Full-body photorealistic character reference of @CoTham, the ghost of a young Vietnamese woman about 19 who drowned in a lotus pond long ago, 158 cm, slender, deathly pale wet skin, long soaked black hair tangled with thin lotus stems, dark sorrowful eyes, wearing a soaked white áo bà ba and black trousers, barefoot, water dripping; plain dark studio background, cold cyan-green rim light, 8K. Clean cinematic ghost appearance, no gore. Not resembling any real actor."
            },
            {
                "tag": "@ThamXua",
                "name": "Thắm thuở sinh thời (19 tuổi, hồi tưởng — VOICE_LOCK_THAMXUA_MADA)",
                "default_media_id": "c7a6d2c5-d9e3-45c0-96e6-9ba8783b3008",
                "locked_media_id": "c7a6d2c5-d9e3-45c0-96e6-9ba8783b3008",
                "voice_lock": "VOICE_LOCK_THAMXUA_MADA",
                "description": "Thắm lúc còn sống ba mươi năm trước: cô gái mồ côi 19 tuổi quét dọn đình làng; dáng mảnh, tóc đen dài tết một bím, mắt sợ hãi; áo bà ba trắng giản dị, quần đen, chân trần. Giọng thoại: VOICE_LOCK_THAMXUA_MADA.",
                "ref_prompt": "Full-body photorealistic character reference of @ThamXua, a slim 19-year-old Vietnamese orphan village girl from the 1990s, 158 cm, long black hair in a single braid, frightened dark eyes, natural healthy skin, wearing a plain white áo bà ba and black trousers, barefoot; plain grey studio background, soft warm side light, 8K. Not resembling any real actor."
            }
        ]
    },
    {
        "slug": "gang-to-tai-xuat",
        "name": "Găng Tơ Tái Xuất (Phim Hành Động Hài 27 Phút)",
        "project_id": "684cb92f-8e9b-41cc-b5b7-9eefa19ce36f",
        "aspect_ratio": "VIDEO_ASPECT_RATIO_LANDSCAPE",
        "runner_script": "runners/gang_to_tai_xuat.py",
        "series_dir": "gang-to-tai-xuat",
        "ep_prefix": "canh",
        "description": "Phim hành động hài Việt Nam 27 phút, kịch bản gốc bản 2, 100% thoại nhân vật (không người dẫn chuyện, nhịp giọng theo cảnh — 10/11/2026): ông xe ôm phố cổ hóa ra là Lâm Rồng, tái xuất cùng Hoa Hổ và Khoa Báo lừa ngược ông chủ app vay tiền Phú Quý đang siết nợ cháu gái (16:9, 27 cảnh × 4 clips × 15s = 108 clips — Google Flow Omni 1.2).",
        "characters": [
            {
                "tag": "@Lam",
                "name": "Ông Lâm (Lâm Rồng) — VOICE_LOCK_LAM_GANG",
                "default_media_id": "07af69cb-9869-4965-b6cf-c8c9c975f7aa",
                "locked_media_id": "07af69cb-9869-4965-b6cf-c8c9c975f7aa",
                "voice_lock": "VOICE_LOCK_LAM_GANG",
                "description": "Ông Lâm 'Lâm Rồng', 63 tuổi, ông xe ôm hiền lành ở cổng Ô Quan Chưởng, ba mươi năm trước là huyền thoại giang hồ phố cổ; nhỏ người, rắn rỏi, tóc bạc cắt cua, lông mày rậm bạc, mắt trái hơi mờ đục; áo gió kéo khóa xám bạc màu ngoài áo ba lỗ trắng, quần kaki rộng, dép nhựa, mũ cối xanh cũ, hình xăm rồng xanh sẫm trên cẳng tay phải. Giọng thoại: VOICE_LOCK_LAM_GANG.",
                "ref_prompt": "Full-body photorealistic character reference of @Lam, a 63-year-old Vietnamese man, humble motorbike-taxi driver, 163 cm, wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles, wearing a faded grey zip-up windbreaker with the right sleeve pushed up to show a dark-green dragon tattoo on his forearm, a white tank top underneath, loose khaki trousers, plastic sandals, holding a battered green pith helmet; plain grey studio background, warm soft side light, 8K. Not resembling any real actor."
            },
            {
                "tag": "@Mai",
                "name": "Mai — VOICE_LOCK_MAI_GANG",
                "default_media_id": "77d55a1f-b8ee-4e66-b606-bcb19f22f542",
                "locked_media_id": "77d55a1f-b8ee-4e66-b606-bcb19f22f542",
                "voice_lock": "VOICE_LOCK_MAI_GANG",
                "description": "Mai, 20 tuổi, cháu gái ông Lâm, sinh viên công nghệ thông tin, mắc nợ app vay tiền vì muốn lo tiền mổ mắt cho ông; nhỏ nhắn, tóc bob đen mái thẳng, kính gọng đen tròn; hoodie tím lavender rộng, quần jean đen, giày thể thao trắng đế dày, ba lô đen nhỏ. Giọng thoại: VOICE_LOCK_MAI_GANG.",
                "ref_prompt": "Full-body photorealistic character reference of @Mai, a 20-year-old Vietnamese female IT student, 155 cm, petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes, wearing an oversized lavender hoodie, black jeans, chunky white sneakers and a small black backpack; plain grey studio background, soft cinematic side light, 8K. Not resembling any real actor."
            },
            {
                "tag": "@BaHoa",
                "name": "Bà Hoa (Hoa Hổ) — VOICE_LOCK_BAHOA_GANG",
                "default_media_id": "a310c641-d8a8-4d31-bccf-21c381b504f8",
                "locked_media_id": "a310c641-d8a8-4d31-bccf-21c381b504f8",
                "voice_lock": "VOICE_LOCK_BAHOA_GANG",
                "description": "Bà Hoa 'Hoa Hổ', 61 tuổi, bộ não của băng ba mươi năm trước, nay là chủ quán bún chả đông nhất phố; đẫy đà, tóc xoăn ngắn nhuộm đỏ mận, mắt sắc, son đỏ, khuyên tai vàng tròn; áo lụa hoa tím, quần ống rộng đen, vòng vàng bản to, dép quai hậu thấp. Giọng thoại: VOICE_LOCK_BAHOA_GANG.",
                "ref_prompt": "Full-body photorealistic character reference of @BaHoa, a 61-year-old Vietnamese woman, bún chả shop owner, 155 cm, plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings, wearing a purple floral silk blouse, black wide trousers, a chunky gold bangle and low heeled sandals; plain grey studio background, warm soft side light, 8K. Not resembling any real actor."
            },
            {
                "tag": "@Khoa",
                "name": "Ông Khoa (Khoa Báo) — VOICE_LOCK_KHOA_GANG",
                "default_media_id": "5d8b0ff3-1866-468c-a45f-98fba4674168",
                "locked_media_id": "5d8b0ff3-1866-468c-a45f-98fba4674168",
                "voice_lock": "VOICE_LOCK_KHOA_GANG",
                "description": "Ông Khoa 'Khoa Báo', 60 tuổi, phù thủy mở khóa của băng năm xưa, nay sửa đài và điện thoại dưới gầm cầu thang; gầy cao lêu nghêu, hói đỉnh, tóc bạc phía sau buộc túm nhỏ, kính lúp dày đẩy lên trán; gile nâu nhiều túi ngoài sơ mi kẻ ô xanh, quần xám, giày vải. Giọng thoại: VOICE_LOCK_KHOA_GANG.",
                "ref_prompt": "Full-body photorealistic character reference of @Khoa, a 60-year-old Vietnamese man, radio and phone repairman, 172 cm, thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead, wearing a brown multi-pocket vest over a blue checkered shirt, grey trousers and canvas shoes; plain grey studio background, soft cinematic side light, 8K. Not resembling any real actor."
            },
            {
                "tag": "@Hung",
                "name": "Hưng Phú Quý — VOICE_LOCK_HUNG_GANG",
                "default_media_id": "36377daf-7efc-4c8a-bfda-7a5e1f8f2d57",
                "locked_media_id": "36377daf-7efc-4c8a-bfda-7a5e1f8f2d57",
                "voice_lock": "VOICE_LOCK_HUNG_GANG",
                "description": "Hưng 'Phú Quý', 31 tuổi, ông chủ ứng dụng vay tiền và mê livestream khoe khoang; cao gầy, tóc undercut nhuộm vàng tro, kính gọng vàng tròn, nụ cười vênh váo; áo bomber satin đen rộng ngoài áo phông trắng, quần jean đen rách, giày cổ cao trắng, nhiều nhẫn bạc, điện thoại gắn gimbal. Giọng thoại: VOICE_LOCK_HUNG_GANG.",
                "ref_prompt": "Full-body photorealistic character reference of @Hung, a 31-year-old Vietnamese man, flashy loan app boss and livestreamer, 178 cm, tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin, wearing an oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers and several silver rings, holding a phone on a small selfie gimbal; plain grey studio background, soft cinematic side light, 8K. Not resembling any real actor."
            },
            {
                "tag": "@Beo",
                "name": "Béo Đầu Sấm — VOICE_LOCK_BEO_GANG",
                "default_media_id": "957f67e8-6414-4457-bb0d-f3a266eeb772",
                "locked_media_id": "957f67e8-6414-4457-bb0d-f3a266eeb772",
                "voice_lock": "VOICE_LOCK_BEO_GANG",
                "description": "Béo 'Đầu Sấm', 28 tuổi, đầu sỏ đòi nợ thuê của Phú Quý; to béo, đầu cạo trọc có hình tia sét cạo một bên, mắt híp, răng cửa bọc vàng; áo ba lỗ đen, quần soóc rằn ri, dép tông, dây chuyền vàng giả. Giọng thoại: VOICE_LOCK_BEO_GANG.",
                "ref_prompt": "Full-body photorealistic character reference of @Beo, a 28-year-old Vietnamese man, heavyset debt collector, 175 cm, big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, a gold front tooth, wearing a black tank top, camouflage shorts, flip-flops and a cheap fake-gold chain; plain grey studio background, soft cinematic side light, 8K. Not resembling any real actor."
            }
        ]
    },
    {
        "slug": "cai-ket-cho-tieu-tam",
        "name": "Chính Thất Cao Tay, Tiểu Tam Trắng Tay (Phim Gia Đình 25 Phút)",
        "project_id": "e5783dc5-1a5e-4608-8fe9-e55f5f6de0bb",
        "aspect_ratio": "VIDEO_ASPECT_RATIO_LANDSCAPE",
        "runner_script": "runners/cai_ket_cho_tieu_tam.py",
        "series_dir": "cai-ket-cho-tieu-tam",
        "ep_prefix": "canh",
        "description": "Phim gia đình có miếng hài Việt Nam 25 phút, kịch bản gốc bản 3 (100% thoại nhân vật, không người dẫn chuyện, nhịp giọng theo cảnh): tiểu tam đến tận tiệm may áo dài của chính thất đặt may áo cưới; Thu bình thản nhận may, lật mặt cặp vợ chồng lừa đảo ngay tại đám hỏi và lật luôn sổ đỏ đứng tên mình (16:9, 25 cảnh × 4 clips × 15s = 100 clips — Google Flow Omni 1.2).",
        "characters": [
            {
                "tag": "@Thu",
                "name": "Thu — VOICE_LOCK_THU_VTK",
                "default_media_id": "5885e053-aa4f-47fe-87e9-4b8c8ff322e4",
                "locked_media_id": "5885e053-aa4f-47fe-87e9-4b8c8ff322e4",
                "voice_lock": "VOICE_LOCK_THU_VTK",
                "description": "Thu, 34 tuổi, chính thất điềm tĩnh và cao tay, chủ tiệm may áo dài nhỏ ở phố cổ, mười hai năm làm dâu; dáng mảnh, da hơi rám nắng, tóc đen dài búi thấp lỏng, ánh mắt hiền mà tinh, không trang điểm, bàn tay chai sạn; áo cotton xanh nhạt bạc màu xắn tay, quần nâu sẫm, tạp dề vải xanh rêu, thước dây vàng trên cổ, dép nhựa. Giọng thoại: VOICE_LOCK_THU_VTK.",
                "ref_prompt": "Full-body photorealistic character reference of @Thu, a 34-year-old Vietnamese woman who sells sticky rice at dawn, 158 cm, slim, lightly sun-tanned skin, long black hair in a low loose bun, gentle tired dark eyes, no makeup, work-roughened hands, wearing a faded light-blue cotton blouse with rolled sleeves, dark-brown trousers, a dark-green cloth apron and plastic sandals; plain grey studio background, soft warm side light, 8K. Not resembling any real actor."
            },
            {
                "tag": "@Tung",
                "name": "Tùng — VOICE_LOCK_TUNG_VTK",
                "default_media_id": "ffdaa99e-ad17-4113-bf9a-c82edee09ee2",
                "locked_media_id": "ffdaa99e-ad17-4113-bf9a-c82edee09ee2",
                "voice_lock": "VOICE_LOCK_TUNG_VTK",
                "description": "Tùng, 37 tuổi, chồng Thu, giám đốc công ty xây dựng mới phất; cao, hơi đẫy đà, tóc đen vuốt keo gọn, mặt nhẵn, mắt mí nặng tự tin; vest xám than may đo, sơ mi trắng hở cổ, đồng hồ vàng, giày da đen bóng. Giọng thoại: VOICE_LOCK_TUNG_VTK.",
                "ref_prompt": "Full-body photorealistic character reference of @Tung, a 37-year-old Vietnamese man, newly rich construction company director, 176 cm, tall and slightly heavy, neatly gelled black hair, clean-shaven, heavy-lidded confident eyes, wearing a tailored charcoal-grey suit, a white shirt open at the collar, a gold wristwatch and polished black shoes; plain grey studio background, soft cinematic side light, 8K. Not resembling any real actor."
            },
            {
                "tag": "@Vy",
                "name": "Vy (Bé Ba) — VOICE_LOCK_VY_VTK",
                "default_media_id": "640166a9-1269-41d5-b33e-baa5fd7d3eff",
                "locked_media_id": "640166a9-1269-41d5-b33e-baa5fd7d3eff",
                "voice_lock": "VOICE_LOCK_VY_VTK",
                "description": "Vy, 24 tuổi, cô thư ký xinh đẹp của Tùng — tiểu tam, thật ra là kẻ lừa đảo chuyên gài bẫy đại gia; mảnh mai nổi bật, tóc dài nâu sẫm uốn sóng bóng mượt, mắt sắc kẻ eyeliner, son đỏ; váy midi đỏ thẫm sát nách ôm dáng, dây chuyền vàng mảnh, giày cao gót màu be, túi xách trắng nhỏ không logo. Giọng thoại: VOICE_LOCK_VY_VTK.",
                "ref_prompt": "Full-body photorealistic character reference of @Vy, a 24-year-old Vietnamese woman, glamorous office secretary, 165 cm, slender and striking, long glossy wavy dark-brown hair, sharp feline eyes with winged eyeliner, red lipstick, wearing a fitted crimson sleeveless midi dress, a thin gold necklace, beige high heels and a small white handbag with no logo; plain grey studio background, soft cinematic side light, 8K. Not resembling any real actor."
            },
            {
                "tag": "@BaNhan",
                "name": "Bà Nhàn — VOICE_LOCK_BANHAN_VTK",
                "default_media_id": "be8ae10b-09a0-41f6-bff5-9cf021617e84",
                "locked_media_id": "be8ae10b-09a0-41f6-bff5-9cf021617e84",
                "voice_lock": "VOICE_LOCK_BANHAN_VTK",
                "description": "Bà Nhàn, 70 tuổi, mẹ Tùng, sống cùng con dâu Thu, khô và hóm, giả lẫn để đứng về phía con dâu; nhỏ gầy, tóc bạc búi thấp gọn, gương mặt hiền nhiều nếp nhăn; áo len cardigan nâu ngoài áo cánh xám, quần đen, dép vải, gậy tre chạm. Giọng thoại: VOICE_LOCK_BANHAN_VTK.",
                "ref_prompt": "Full-body photorealistic character reference of @BaNhan, a 70-year-old Vietnamese grandmother, 148 cm, small and thin, white hair in a neat low bun, kind deeply wrinkled face, wearing a brown knitted cardigan over a grey blouse, black trousers and cloth slippers, holding a carved bamboo walking stick; plain grey studio background, warm soft side light, 8K. Not resembling any real actor."
            },
            {
                "tag": "@Na",
                "name": "Bé Na — VOICE_LOCK_NA_VTK",
                "default_media_id": "ccc8c935-3187-4b7b-975a-9733195854cf",
                "locked_media_id": "ccc8c935-3187-4b7b-975a-9733195854cf",
                "voice_lock": "VOICE_LOCK_NA_VTK",
                "description": "Bé Na, 9 tuổi, con gái Thu và Tùng; nhỏ nhắn, mặt tròn, mắt sáng, tóc đen buộc hai bím ngắn dây chun đỏ; áo sơ mi trắng cộc tay đồng phục, váy xếp ly xanh than, khăn quàng đỏ, giày vải trắng. Giọng thoại: VOICE_LOCK_NA_VTK.",
                "ref_prompt": "Full-body photorealistic character reference of @Na, a 9-year-old Vietnamese schoolgirl, 130 cm, small with a round face and bright dark eyes, black hair in two short pigtails with red hair ties, wearing a white short-sleeve school shirt, a navy pleated skirt, a red scarf knotted at the neck and white canvas shoes; plain grey studio background, soft warm side light, 8K. Not resembling any real person."
            },
            {
                "tag": "@Khai",
                "name": "Khải — VOICE_LOCK_KHAI_VTK",
                "default_media_id": "68c8c0e0-1e95-46db-b6e6-8b6e94df5b99",
                "locked_media_id": "68c8c0e0-1e95-46db-b6e6-8b6e94df5b99",
                "voice_lock": "VOICE_LOCK_KHAI_VTK",
                "description": "Khải, 30 tuổi, chồng bí mật của Vy, đóng vai 'anh họ luật sư'; gầy, tóc undercut đen vuốt, ria mép mỏng, nụ cười nửa miệng ranh mãnh; sơ mi đen slim-fit xắn tay, quần kaki be, giày thể thao trắng, lắc tay bạc. Giọng thoại: VOICE_LOCK_KHAI_VTK.",
                "ref_prompt": "Full-body photorealistic character reference of @Khai, a 30-year-old Vietnamese man, smooth con artist, 172 cm, lean, styled black undercut hair, thin moustache, sly half-smile, wearing a black slim-fit shirt with rolled sleeves, beige chinos, white sneakers and a silver chain bracelet; plain grey studio background, soft cinematic side light, 8K. Not resembling any real actor."
            }
        ]
    },
    {
        "slug": "bay-ngay-sinh-ton",
        "name": "Bảy Ngày Sinh Tồn — Seven Days in the Stone Age (Phim Sinh Tồn 24 Phút)",
        "project_id": "",
        "aspect_ratio": "VIDEO_ASPECT_RATIO_LANDSCAPE",
        "runner_script": "runners/bay_ngay_sinh_ton.py",
        "series_dir": "bay-ngay-sinh-ton",
        "ep_prefix": "canh",
        "description": "Phim phiêu lưu sinh tồn có miếng hài, kịch bản gốc (100% thoại tiếng Anh do nhân vật nói trên hình, không người dẫn chuyện, nhịp giọng theo cảnh): YouTuber sinh tồn Khang bị bóc phốt diễn, ngủ một đêm giông trong hang Bàn Tay ở Cúc Phương và tỉnh dậy ở thời đồ đá; bảy lần mặt trời tự sống bằng hai bàn tay (16:9, 24 cảnh × 4 clips × 15s = 96 clips — Google Flow Omni 1.2).",
        "characters": [
            {
                "tag": "@Khang",
                "name": "Khang — VOICE_LOCK_KHANG_BNST",
                "default_media_id": "",
                "locked_media_id": "",
                "voice_lock": "VOICE_LOCK_KHANG_BNST",
                "description": "Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; olive-green tactical shirt with a plain patch without letters, khaki cargo trousers, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera, a bright orange backpack.",
                "ref_prompt": "Full-body photorealistic character reference of @Khang: Khang, 29, Vietnamese survival YouTuber; lean athletic build, tanned skin, short black undercut hair, light stubble, expressive dark eyes, a quick showman's grin; olive-green tactical shirt with a plain patch without letters, khaki cargo trousers, brown hiking boots, a red bandana tied on the left wrist, a black chest harness holding a small square chest camera, a bright orange backpack; plain grey studio background, soft cinematic side light, 8K. Not resembling any real actor.",
            },
            {
                "tag": "@Bin",
                "name": "Bin — VOICE_LOCK_BIN_BNST",
                "default_media_id": "",
                "locked_media_id": "",
                "voice_lock": "VOICE_LOCK_BIN_BNST",
                "description": "Bin, 24, Khang's cameraman and channel manager; slim, round face, round black-rimmed glasses, short messy black hair; cream bucket hat, thin yellow windbreaker over a black T-shirt, black jeans, white sneakers, a handheld camera gimbal.",
                "ref_prompt": "Full-body photorealistic character reference of @Bin: Bin, 24, Khang's cameraman and channel manager; slim, round face, round black-rimmed glasses, short messy black hair; cream bucket hat, thin yellow windbreaker over a black T-shirt, black jeans, white sneakers, a handheld camera gimbal; plain grey studio background, soft cinematic side light, 8K. Not resembling any real actor.",
            },
            {
                "tag": "@Stream",
                "name": "Stream — VOICE_LOCK_STREAM_BNST",
                "default_media_id": "",
                "locked_media_id": "",
                "voice_lock": "VOICE_LOCK_STREAM_BNST",
                "description": "Stream, 19, Stone Age forager girl of the cave clan; slim and agile, warm brown skin, long straight black hair tied back with a vine cord, bright alert dark eyes, two thin red-ochre stripes on each cheekbone; a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, a necklace of small stream-snail shells, a woven rattan basket on her back, barefoot.",
                "ref_prompt": "Full-body photorealistic character reference of @Stream: Stream, 19, Stone Age forager girl of the cave clan; slim and agile, warm brown skin, long straight black hair tied back with a vine cord, bright alert dark eyes, two thin red-ochre stripes on each cheekbone; a knee-length tunic of beaten tan bark cloth with a soft deer-hide wrap covering both shoulders, a necklace of small stream-snail shells, a woven rattan basket on her back, barefoot; plain grey studio background, soft cinematic side light, 8K. Not resembling any real actor.",
            },
            {
                "tag": "@Moon",
                "name": "Grandma Moon — VOICE_LOCK_MOON_BNST",
                "default_media_id": "",
                "locked_media_id": "",
                "voice_lock": "VOICE_LOCK_MOON_BNST",
                "description": "Grandma Moon, 65, Stone Age clan leader and keeper of the fire; small and straight-backed, deeply lined brown face, calm piercing eyes, white hair in a high knot held by a bone pin, a red-ochre dot on her forehead; a long dark hide cloak over a knee-length bark-cloth tunic, a thick green bamboo tube for carrying embers, barefoot.",
                "ref_prompt": "Full-body photorealistic character reference of @Moon: Grandma Moon, 65, Stone Age clan leader and keeper of the fire; small and straight-backed, deeply lined brown face, calm piercing eyes, white hair in a high knot held by a bone pin, a red-ochre dot on her forehead; a long dark hide cloak over a knee-length bark-cloth tunic, a thick green bamboo tube for carrying embers, barefoot; plain grey studio background, soft cinematic side light, 8K. Not resembling any real actor.",
            },
            {
                "tag": "@Roar",
                "name": "Roar — VOICE_LOCK_ROAR_BNST",
                "default_media_id": "",
                "locked_media_id": "",
                "voice_lock": "VOICE_LOCK_ROAR_BNST",
                "description": "Roar, 30, the clan's strongest Stone Age hunter; tall, broad-shouldered and muscular, weathered brown skin, thick black hair bound with a strip of bark, heavy brows, a fierce jaw; a sleeveless vest of dark boar hide that fully covers his chest, a knee-length bark-cloth kilt, a necklace of curved boar tusks, a long bamboo spear with a chipped stone tip, barefoot.",
                "ref_prompt": "Full-body photorealistic character reference of @Roar: Roar, 30, the clan's strongest Stone Age hunter; tall, broad-shouldered and muscular, weathered brown skin, thick black hair bound with a strip of bark, heavy brows, a fierce jaw; a sleeveless vest of dark boar hide that fully covers his chest, a knee-length bark-cloth kilt, a necklace of curved boar tusks, a long bamboo spear with a chipped stone tip, barefoot; plain grey studio background, soft cinematic side light, 8K. Not resembling any real actor.",
            },
            {
                "tag": "@Snail",
                "name": "Snail — VOICE_LOCK_SNAIL_BNST",
                "default_media_id": "",
                "locked_media_id": "",
                "voice_lock": "VOICE_LOCK_SNAIL_BNST",
                "description": "Snail, 8, Stream's little brother in the Stone Age clan; small and wiry, round cheeky face, big curious dark eyes, head shaved except a small tuft of hair on top; a small knee-length bark-cloth tunic covering both shoulders, a string of snail shells around one wrist, barefoot.",
                "ref_prompt": "Full-body photorealistic character reference of @Snail: Snail, 8, Stream's little brother in the Stone Age clan; small and wiry, round cheeky face, big curious dark eyes, head shaved except a small tuft of hair on top; a small knee-length bark-cloth tunic covering both shoulders, a string of snail shells around one wrist, barefoot; plain grey studio background, soft cinematic side light, 8K. Not resembling any real person.",
            }
        ]
    },
]

CHANNEL_MAX_EPISODES: dict[str, int] = {
    "duong-dua-sinh-tu": 40,
    "ke-song-sot": 60,
    "bi-mat-phong-613": 15,
    "oan-thai-doi-me": 14,
    "can-nha-am-duong": 15,
    "tieng-go-dem-ba-gio": 15,
    "ma-da-dam-sen": 15,
    "gang-to-tai-xuat": 27,
    "cai-ket-cho-tieu-tam": 25,
    "bay-ngay-sinh-ton": 24,
}


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

    # 2. Seed channels & remove deprecated channels / stale episode rows
    for dep_slug in ("mai-hoa-thung", "vo-tao-khang"):
        await db.execute("DELETE FROM cms_channel WHERE slug = ?", (dep_slug,))
        await db.execute("DELETE FROM cms_episode WHERE channel_slug = ?", (dep_slug,))
        await db.execute("DELETE FROM cms_clip WHERE channel_slug = ?", (dep_slug,))
    for ch_slug, max_ep in CHANNEL_MAX_EPISODES.items():
        await db.execute("DELETE FROM cms_episode WHERE channel_slug = ? AND episode_num > ?", (ch_slug, max_ep))
        await db.execute("DELETE FROM cms_clip WHERE channel_slug = ? AND episode_num > ?", (ch_slug, max_ep))
        await db.execute("DELETE FROM cms_log WHERE channel_slug = ? AND episode > ?", (ch_slug, max_ep))
    await db.execute("DELETE FROM scene WHERE id LIKE 'scene-ddst-%' AND display_order >= 240")

    for ch in DEFAULT_CHANNELS:
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
                    runner_pid,
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
            eff_pid = runner_pid or (ex.get("project_id") or "").strip()
            existing_chars_by_tag: dict[str, dict] = {}
            try:
                for ec in json.loads(ex.get("characters_json") or "[]"):
                    if isinstance(ec, dict) and ec.get("tag"):
                        existing_chars_by_tag[ec["tag"]] = ec
            except Exception:
                pass
            merged_chars = []
            for dc in ch["characters"]:
                mc = dict(dc)
                ec = existing_chars_by_tag.get(dc.get("tag", "")) or {}
                if not (mc.get("default_media_id") or "").strip() and (ec.get("default_media_id") or "").strip():
                    mc["default_media_id"] = ec["default_media_id"]
                if not (mc.get("locked_media_id") or "").strip() and (ec.get("locked_media_id") or "").strip():
                    mc["locked_media_id"] = ec["locked_media_id"]
                merged_chars.append(mc)
            await db.execute(
                """UPDATE cms_channel
                   SET name = ?, project_id = ?, aspect_ratio = ?, runner_script = ?,
                       series_dir = ?, ep_prefix = ?, description = ?, characters_json = ?, updated_at = ?
                   WHERE slug = ?""",
                (
                    ch["name"],
                    eff_pid,
                    ch["aspect_ratio"],
                    ch["runner_script"],
                    ch["series_dir"],
                    ch["ep_prefix"],
                    ch["description"],
                    json.dumps(merged_chars, ensure_ascii=False),
                    now,
                    ch["slug"],
                ),
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
        f"TGDBG_C{ep_num:02d}_CLIP{clip_num:02d}.mp4",
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
            m = re.search(r"(?:clip[-_]?|_C)(\d+)\.mp4$", fname, re.IGNORECASE)
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
    max_ep = CHANNEL_MAX_EPISODES.get(slug)
    all_ep_nums = sorted(
        ep_n
        for ep_n in (set(ep_dirs.keys()) | set(ep_map.keys()))
        if max_ep is None or (1 <= ep_n <= max_ep)
    )
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

            is_done = bool(v_file or r2_url)
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
                    "status": "COMPLETED" if is_done else (db_clip.get("status") if db_clip.get("status") == "FAILED" else "PENDING"),
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
        ep_total = len(clips_data) if len(clips_data) > 0 else int(db_ep.get("total_clips") or 0)
        ep_rendered = rendered_count if len(clips_data) > 0 else int(db_ep.get("rendered_clips") or 0)

        episodes.append(
            {
                "episode_num": ep_num,
                "folder_name": ep_folder_name,
                "label": db_ep.get("label") or f"{'Cảnh' if ep_prefix == 'canh' else 'Tập'} {ep_num:02d}",
                "total_clips": ep_total,
                "rendered_clips": ep_rendered,
                "failed_clips": max(0, ep_total - ep_rendered),
                "r2_synced_clips": r2_synced_clips,
                "is_complete": bool(ep_total > 0 and ep_rendered >= ep_total),
                "merged_video_url": merged_local_url or merged_r2_url,
                "merged_r2_url": merged_r2_url,
                "merged_r2_key": merged_r2_key,
                "merged_media_kind": m_media_info["media_kind"],
                "merged_media_type": m_media_info["mime_type"],
                "merged_video_path": merged_file
                or (
                    db_ep.get("merged_local_path")
                    if db_ep.get("merged_local_path") and os.path.isfile(db_ep["merged_local_path"])
                    else None
                ),
                "merged_size_mb": merged_size,
                "clips": clips_data,
            }
        )

    return episodes


async def _load_channel_db_maps(db, slug: str) -> tuple[dict[int, dict], dict[tuple[int, int], dict]]:
    ep_map: dict[int, dict] = {}
    clip_map: dict[tuple[int, int], dict] = {}
    max_ep = CHANNEL_MAX_EPISODES.get(slug)
    try:
        ep_cur = await db.execute("SELECT * FROM cms_episode WHERE channel_slug = ?", (slug,))
        for r in await ep_cur.fetchall():
            d = dict(r)
            ep_n = int(d["episode_num"])
            if max_ep is not None and ep_n > max_ep:
                continue
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
            ep_n = int(d["episode_num"])
            if max_ep is not None and ep_n > max_ep:
                continue
            key = (ep_n, int(d["clip_num"]))
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
            if max_ep is not None and int(ep_n) > max_ep:
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
                if key not in clip_map:
                    clip_map[key] = {
                        "episode_num": int(ep_n),
                        "clip_num": int(cl_n),
                        "status": "COMPLETED",
                        "r2_url": r2_u,
                        "r2_key": r2_k,
                        "size_mb": det.get("size_mb"),
                    }
            else:
                if int(ep_n) not in ep_map:
                    ep_map[int(ep_n)] = {
                        "episode_num": int(ep_n),
                        "is_complete": 1,
                        "merged_r2_url": r2_u,
                        "merged_r2_key": r2_k,
                        "merged_size_mb": det.get("size_mb"),
                    }
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
        completed_eps = sum(1 for ep in episodes if ep.get("is_complete"))
        merged_eps = sum(1 for ep in episodes if ep.get("merged_video_url"))
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
                    "completed_episodes": completed_eps,
                    "clips_per_episode": round(total_clips / total_eps) if total_eps > 0 else 0,
                    "total_clips": total_clips,
                    "rendered_clips": rendered_clips,
                    "failed_clips": max(0, total_clips - rendered_clips),
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
    remote_query_ok = False
    if client.connected:
        # Auto-create a fresh Google Flow project if still using placeholder UUID
        if project_id == "d8997010-1080-49f1-9220-10ec05919c8c":
            try:
                cp_res = await client.create_project(row_dict.get("name") or slug)
                new_pid = (cp_res.get("data") or {}).get("projectId")
                if new_pid:
                    project_id = new_pid
                    project_cache = cached_by_project.get(project_id, {}) if isinstance(cached_by_project, dict) else {}
            except Exception as e:
                logger.warning("Failed to auto-create Flow project for %s: %s", slug, e)
        try:
            res = await client.batch_rpc(
                fb.RPC_PROJECT_MEDIA, fb.project_media_request(project_id), match=None, timeout=45
            )
            raw = res.get("data") or ""
            if raw:
                payload = fb.first_payload(raw, fb.RPC_PROJECT_MEDIA)
                if isinstance(payload, list):
                    remote_query_ok = True
                    raw_chars = payload[5] if len(payload) > 5 and isinstance(payload[5], list) else []
                    for ch in raw_chars:
                        if isinstance(ch, list) and len(ch) >= 5:
                            cid = ch[0] if isinstance(ch[0], str) else None
                            meta = ch[3] if isinstance(ch[3], list) else []
                            cname = meta[1] if len(meta) > 1 and isinstance(meta[1], str) else ""
                            cmid = ch[4] if isinstance(ch[4], str) else None
                            if cname and cmid:
                                remote_chars.append({"name": cname, "media_id": cmid, "character_id": cid})
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
    img_aspect = (
        "IMAGE_ASPECT_RATIO_LANDSCAPE"
        if "LANDSCAPE" in (row_dict.get("aspect_ratio") or "")
        else "IMAGE_ASPECT_RATIO_PORTRAIT"
    )

    for c in chars:
        tag = c.get("tag", "")
        name = c.get("name", tag)
        tag_clean = tag.lower().lstrip("@")
        name_clean = name.lower().split("(")[0].strip()
        matched_mid = None
        matched_cid = None

        if not force_regenerate:
            for rc in remote_chars:
                rc_clean = rc["name"].strip().lower().lstrip("@")
                if rc_clean == tag_clean or rc_clean == name_clean:
                    matched_mid = rc["media_id"]
                    matched_cid = rc.get("character_id")
                    break

            if not matched_mid and not remote_query_ok:
                for ri in remote_images:
                    ri_clean = ri["title"].strip().lower().lstrip("@")
                    if ri_clean == tag_clean or ri_clean == name_clean:
                        matched_mid = ri["media_id"]
                        break

            if not matched_mid and not remote_query_ok:
                matched_mid = project_cache.get(tag) or c.get("default_media_id") or None

        ref_prompt = (
            c.get("ref_prompt")
            or default_prompts.get(tag)
            or f"Full-body character reference of {tag} ({name}): {c.get('description', '')}. Plain studio background, 8K."
        )

        if not matched_mid and client.connected and ref_prompt:
            try:
                gen_res = await client.create_character(
                    name=tag,
                    prompt=ref_prompt,
                    project_id=project_id,
                    description=c.get("description") or name,
                    aspect_ratio=img_aspect,
                    image_model="nano_banana_pro",
                )
                data_obj = gen_res.get("data") or {}
                medias = data_obj.get("media") or []
                if medias and isinstance(medias[0], dict):
                    matched_mid = medias[0].get("name") or medias[0].get("media_id")
                    matched_cid = data_obj.get("characterId") or medias[0].get("character_id")
                    if matched_mid:
                        created_now.append(tag)
                        try:
                            await client.rename_asset(
                                display_name=tag,
                                media_id=matched_mid,
                                project_id=project_id,
                            )
                        except Exception:
                            pass
            except Exception as e:
                logger.warning("Failed to auto-create character entity & image for %s: %s", tag, e)

        if matched_mid:
            locked_map[tag] = matched_mid
            c["default_media_id"] = matched_mid
            c["locked_media_id"] = matched_mid
            if matched_cid:
                c["character_id"] = matched_cid
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

    # Sync locked default_media_id and PROJECT_ID into runner script (e.g., runners/duong_dua_sinh_tu.py)
    if os.path.isfile(runner_abs):
        try:
            with open(runner_abs, "r", encoding="utf-8") as rf:
                rcode = rf.read()
            rcode = re.sub(r'^PROJECT_ID\s*=\s*"[^"]*"', f'PROJECT_ID = "{project_id}"', rcode, count=1, flags=re.MULTILINE)
            for tag, mid in locked_map.items():
                pattern = rf'("tag":\s*"{re.escape(tag)}"[\s\S]*?"default_media_id":\s*)"[^"]*"'
                rcode = re.sub(pattern, rf'\1"{mid}"', rcode, count=1)
            with open(runner_abs, "w", encoding="utf-8") as rf:
                rf.write(rcode)
        except Exception as e:
            logger.warning("Failed to update default_media_id in %s: %s", runner_abs, e)

    # Also update PHAN_CANH_V3.json if present in series directory
    phan_canh_path = os.path.join(series_abs_dir, "PHAN_CANH_V3.json")
    if os.path.isfile(phan_canh_path) and locked_map:
        try:
            with open(phan_canh_path, "r", encoding="utf-8") as pf:
                plan_data = json.load(pf)
            if isinstance(plan_data.get("identities"), dict):
                for _ik, iv in plan_data["identities"].items():
                    itag = iv.get("tag")
                    if itag and locked_map.get(itag):
                        iv["media_id"] = locked_map[itag]
                with open(phan_canh_path, "w", encoding="utf-8") as pf:
                    json.dump(plan_data, pf, ensure_ascii=False, indent=2)
        except Exception as e:
            logger.warning("Failed to update PHAN_CANH_V3.json for %s: %s", slug, e)

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
    clip_count: int = 4  # TikTok: 4 clips × 15s since 12/11/2026
    story_idea: Optional[str] = None
    setting: Optional[str] = None
    scene_beats: Optional[list[str]] = None


class CreateEpisodeRequest(BaseModel):
    episode_num: int
    clip_count: int = 4  # TikTok: 4 clips × 15s since 12/11/2026
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
    # TikTok series: 4 clips × 15s per episode on Omni 1.2 since 12/11/2026 (the runners read the length from
    # "N-second clip" in [FORMAT]); the landscape films keep their own 10s templates.
    clip_s = 15 if slug in TIKTOK_15S_SLUGS else 10
    t1, t2 = (5, 10) if clip_s == 15 else (3.5, 7)
    t1s, t2s = (f"{t1:04.1f}" if isinstance(t1, float) else f"{t1:02d}"), f"{t2:02d}"

    if slug == "mit-va-du-1970":
        world_format = (
            f"{ar_text}, {clip_s}-second clip, high-end 3D animated film, Pixar/Disney-quality stylized CGI, "
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
    elif slug == "duong-dua-sinh-tu":
        world_format = (
            "Full-frame 16:9 (1.78:1), no letterbox bars, 10-second clip, 24fps, photorealistic live-action high-octane street-racing "
            "crime thriller film style set in Los Angeles highways, tuner garages, and the Mojave Desert. 35mm anamorphic cinema lenses, "
            "sodium-vapour amber and neon cyan night grade, warm golden-hour desert sun. Dialogue in Vietnamese with natural Southern accent "
            "and accurate lip-sync. No subtitles or on-screen text."
        )
        default_setting = (
            "MICDO'S TUNER GARAGE & LOS ANGELES NIGHT STREETS: sodium-vapour amber streetlamps, custom tuned sports cars, "
            "hydraulic lifts, chrome tools, and rain-slick asphalt."
        )
        avoid_line = (
            "blood, gore, visible wounds, on-screen shooting, muzzle flashes, bullet hits on people, deaths on camera, torture, "
            "real brand logos, readable signs or documents, real police insignia, watermarks, text overlays, extra fingers, "
            "cartoon or anime look, likeness of any real actor."
        )
    else:
        world_format = (
            f"{ar_text}, {clip_s}-second clip, high-end 3D animated film, Pixar/DreamWorks-quality stylized CGI, "
            "soft global illumination, shallow depth of field, 24fps, cinematic color grade. "
            + (
                # TikTok series except Mít & Đú speak "giọng Bắc thanh thoát" (user rule, 07/11/2026)
                "Spoken dialogue in Vietnamese with a soft, clear, elegant standard Northern Vietnamese (Hà Nội) accent "
                "and accurate lip-sync. "
                if slug in ("pheo-va-no-meo", "me-va-be", "tay-du-ky-2026", "365ngayvietnam")
                else "Spoken dialogue in Vietnamese with natural expressive voice acting and accurate lip-sync. "
            )
            + "No subtitles, no captions, no on-screen text, no logos, no watermark."
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
                f"00:00–00:{t1s} | Medium wide establishing shot — {beat}\n"
                f"00:{t1s}–00:{t2s} | Medium shot, dynamic camera — Các nhân vật {char_tags} tương tác trực tiếp với đạo cụ trong cảnh, cử chỉ tự nhiên và biểu cảm rõ nét.\n"
                f"00:{t2s}–00:{clip_s:02d} | Medium close-up — Khoảnh khắc nhấn điểm hài hước/đáng yêu cuối cảnh 1 để chuẩn bị nối sang cảnh 2.\n\n"
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
                f"00:00–00:{t1s} | Same medium shot, continuing seamlessly from the last frame of Clip {idx - 1} — {beat}\n"
                f"00:{t1s}–00:{t2s} | Medium shot — Diễn biến tiếp nối mượt mà của {char_tags} trong bối cảnh ({final_setting}).\n"
                f"00:{t2s}–00:{clip_s:02d} | Medium close-up — Biểu cảm đáng yêu của {char_tags} khép lại Clip {idx}.\n\n"
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
                f"🎉 Đã hoàn thành tiến trình tạo video các clip (Tập {start_ep:02d} -> {end_ep:02d})! Bấm nút 'Ghép Clip Nhỏ Thành Tập FULL' trên UI khi cần ghép tập.",
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
    """Scan all series channels on disk and upsert episodes & clips (prompts + video paths) into cms_episode & cms_clip."""
    await ensure_cms_seeded()
    raw_db = getattr(db, "_sqlite", db)
    for ch_slug, max_ep in CHANNEL_MAX_EPISODES.items():
        await raw_db.execute("DELETE FROM cms_episode WHERE channel_slug = ? AND episode_num > ?", (ch_slug, max_ep))
        await raw_db.execute("DELETE FROM cms_clip WHERE channel_slug = ? AND episode_num > ?", (ch_slug, max_ep))
        await raw_db.execute("DELETE FROM cms_log WHERE channel_slug = ? AND episode > ?", (ch_slug, max_ep))
    await raw_db.execute("DELETE FROM scene WHERE id LIKE 'scene-ddst-%' AND display_order >= 240")
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
                    ep.get("merged_video_path"),
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
                        v_file,
                        cl.get("r2_key") or old_cl.get("r2_key"),
                        cl.get("r2_url") or old_cl.get("r2_url"),
                        f_file,
                        old_cl.get("frame_r2_key"),
                        cl.get("frame_r2_url") or old_cl.get("frame_r2_url"),
                        cl.get("video_size_mb") or old_cl.get("size_mb"),
                        old_cl.get("duration_s"),
                        old_cl.get("media_id"),
                        now,
                    ),
                )
                if slug == "duong-dua-sinh-tu" and cl.get("prompt"):
                    scene_id = f"scene-ddst-{ep_num:02d}-{c_num:02d}"
                    await raw_db.execute(
                        "UPDATE scene SET prompt = ?, video_prompt = ?, updated_at = ? WHERE id = ?",
                        (cl["prompt"], cl["prompt"], now, scene_id),
                    )
                clip_upserted += 1

    await raw_db.execute("DELETE FROM cms_episode WHERE id NOT LIKE '%:ep:%'")
    await raw_db.execute("DELETE FROM cms_clip WHERE id NOT LIKE '%:ep:%'")
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
    reconciled_clips_count = 0
    reconciled_episodes_count = 0
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
            max_ep = CHANNEL_MAX_EPISODES.get(ch_slug)
            cat = parts[2]
            fname = parts[-1]
            if cat == "episodes" and len(parts) >= 5:
                subf = parts[3]
                m_ep = re.search(r"(\d+)", subf) or re.search(r"(?:tap|canh|_T)[-_]?(\d+)", fname, re.IGNORECASE)
                m_cl = re.search(r"(?:clip[-_]|_C)(\d+)\.mp4$", fname, re.IGNORECASE)
                if m_ep and m_cl:
                    ep_n = int(m_ep.group(1))
                    cl_n = int(m_cl.group(1))
                    if max_ep is not None and ep_n > max_ep:
                        continue
                    if body.episode_num is not None and ep_n != body.episode_num:
                        continue
                    cid = f"{ch_slug}:ep:{ep_n}:clip:{cl_n}"
                    await db.execute(
                        """UPDATE cms_clip
                           SET r2_key = ?, r2_url = ?, size_mb = COALESCE(?, size_mb), status = 'COMPLETED', updated_at = ?
                           WHERE id = ?""",
                        (okey, ourl, osize, now, cid),
                    )
                    reconciled_clips_count += 1
            elif cat == "full_episodes":
                if ch_slug in ("duong-dua-sinh-tu", "tieng-go-dem-ba-gio", "can-nha-am-duong", "ma-da-dam-sen", "gang-to-tai-xuat", "cai-ket-cho-tieu-tam") and re.search(r"tap[-_]?\d+_FULL\.mp4$", fname, re.IGNORECASE):
                    continue
                m_ep = re.search(r"(?:tap|canh)[-_]?(\d+)_FULL\.mp4$", fname, re.IGNORECASE)
                if m_ep:
                    ep_n = int(m_ep.group(1))
                    if max_ep is not None and ep_n > max_ep:
                        continue
                    if body.episode_num is not None and ep_n != body.episode_num:
                        continue
                    eid = f"{ch_slug}:ep:{ep_n}"
                    await db.execute(
                        """UPDATE cms_episode
                           SET merged_r2_key = ?, merged_r2_url = ?, merged_size_mb = COALESCE(?, merged_size_mb), is_complete = 1, updated_at = ?
                           WHERE id = ?""",
                        (okey, ourl, osize, now, eid),
                    )
                    reconciled_episodes_count += 1

        await db.execute(
            """UPDATE cms_clip
               SET status = CASE
                   WHEN (r2_url IS NOT NULL AND r2_url != '') OR (local_path IS NOT NULL AND local_path != '') THEN 'COMPLETED'
                   ELSE CASE WHEN status = 'FAILED' THEN 'FAILED' ELSE 'PENDING' END
               END"""
        )

        await db.execute(
            """UPDATE cms_episode
               SET rendered_clips = (
                   SELECT COUNT(*) FROM cms_clip c
                   WHERE c.channel_slug = cms_episode.channel_slug
                     AND c.episode_num = cms_episode.episode_num
                     AND ((c.r2_url IS NOT NULL AND c.r2_url != '') OR (c.local_path IS NOT NULL AND c.local_path != ''))
               ),
               is_complete = CASE
                   WHEN total_clips > 0 AND (
                       SELECT COUNT(*) FROM cms_clip c
                       WHERE c.channel_slug = cms_episode.channel_slug
                         AND c.episode_num = cms_episode.episode_num
                         AND ((c.r2_url IS NOT NULL AND c.r2_url != '') OR (c.local_path IS NOT NULL AND c.local_path != ''))
                   ) >= total_clips THEN 1
                   ELSE 0
               END"""
        )
    except Exception as e:
        logger.warning("R2 reconciliation warning: %s", e)

    await db.commit()
    await record_cms_log(
        body.channel_slug or "system",
        "SUCCESS" if not errors else "WARN",
        "R2_SYNC",
        f"☁️ Đã đồng bộ Cloudflare R2: upload mới {len(uploaded_clips)} clips / {len(uploaded_episodes)} tập FULL; đối soát R2 {reconciled_clips_count} clips / {reconciled_episodes_count} tập FULL!",
        details={
            "uploaded_clips": len(uploaded_clips),
            "uploaded_episodes": len(uploaded_episodes),
            "reconciled_clips": reconciled_clips_count,
            "reconciled_episodes": reconciled_episodes_count,
            "errors": errors[:5],
        },
    )
    return {
        "ok": True,
        "uploaded_clips_count": len(uploaded_clips),
        "uploaded_episodes_count": len(uploaded_episodes),
        "reconciled_clips_count": reconciled_clips_count,
        "reconciled_episodes_count": reconciled_episodes_count,
        "uploaded_clips": uploaded_clips,
        "uploaded_episodes": uploaded_episodes,
        "errors": errors[:10],
    }

