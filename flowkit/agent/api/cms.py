"""CMS API — Authentication, Multi-Channel Studio, Video Generation Runner, Auto Episode Merger & Persistent Logs."""
import asyncio
import glob
import hashlib
import json
import logging
import os
import re
import secrets
import sys
from datetime import datetime, timezone
from typing import Optional

from fastapi import APIRouter, Header, HTTPException, Query, Request
from fastapi.responses import FileResponse
from pydantic import BaseModel

from agent.db.schema import get_db
from agent.services.event_bus import event_bus

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/cms", tags=["cms"])

FLOWKIT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WORKSPACE_DIR = os.path.dirname(FLOWKIT_DIR)
RUNNERS_DIR = os.path.join(FLOWKIT_DIR, "runners")
if RUNNERS_DIR not in sys.path:
    sys.path.insert(0, RUNNERS_DIR)

from cms_integration import find_episode_clip_mp4s, merge_episode_clips  # noqa: E402

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
]


def _now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")


def _hash_password(password: str, salt: str = "flowkit_cms_2026") -> str:
    return hashlib.sha256(f"{salt}:{password}".encode("utf-8")).hexdigest()


async def ensure_cms_seeded():
    """Ensure default admin user and 6 series channels exist in SQLite."""
    db = await get_db()
    now = _now_iso()

    col_cur = await db.execute("PRAGMA table_info(cms_channel)")
    cols = {r[1] for r in await col_cur.fetchall()}
    if "ep_prefix" not in cols:
        await db.execute("ALTER TABLE cms_channel ADD COLUMN ep_prefix TEXT NOT NULL DEFAULT 'tap'")
        await db.commit()

    # 1. Seed default admin user (admin / admin123)
    cur = await db.execute("SELECT id FROM cms_user WHERE username = ?", ("admin",))
    if not await cur.fetchone():
        await db.execute(
            "INSERT INTO cms_user (id, username, password_hash, display_name, role, created_at) VALUES (?, ?, ?, ?, ?, ?)",
            ("admin-1", "admin", _hash_password("admin123"), "Quản Trị Viên FlowKit", "admin", now),
        )

    # 2. Seed 6 channels
    for ch in DEFAULT_CHANNELS:
        cur = await db.execute("SELECT slug FROM cms_channel WHERE slug = ?", (ch["slug"],))
        if not await cur.fetchone():
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
    await db.commit()


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
    return f"/api/cms/media?path={rel}"


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
    full_name = f"{channel_slug}_tap-{ep_num:02d}_FULL.mp4"
    candidates = [
        os.path.join(series_abs_dir, "output_videos", ep_folder_name, full_name),
        os.path.join(series_abs_dir, "output_videos", "full_episodes", full_name),
        os.path.join(series_abs_dir, "output_videos", f"tap-{ep_num:02d}", full_name),
        os.path.join(series_abs_dir, "output_videos", f"canh-{ep_num:02d}", full_name),
    ]
    for c in candidates:
        if os.path.isfile(c) and os.path.getsize(c) > 0:
            return c
    return None


def _scan_channel_episodes(channel_row: dict, include_prompts: bool = False) -> list[dict]:
    series_abs_dir = os.path.join(WORKSPACE_DIR, channel_row["series_dir"])
    ep_prefix = channel_row.get("ep_prefix") or "tap"
    slug = channel_row["slug"]
    if not os.path.isdir(series_abs_dir):
        return []

    ep_dirs: dict[int, str] = {}
    for entry in sorted(os.listdir(series_abs_dir)):
        full_p = os.path.join(series_abs_dir, entry)
        if not os.path.isdir(full_p):
            continue
        ep_num = _extract_ep_number(entry, ep_prefix)
        if ep_num is not None:
            # Prefer more descriptive folder name if duplicate number exists
            if ep_num not in ep_dirs or len(entry) > len(os.path.basename(ep_dirs[ep_num])):
                ep_dirs[ep_num] = full_p

    episodes = []
    for ep_num in sorted(ep_dirs.keys()):
        ep_dir = ep_dirs[ep_num]
        ep_folder_name = os.path.basename(ep_dir)
        clip_files = []
        for fname in os.listdir(ep_dir):
            m = re.match(r"^clip-(\d+)\.md$", fname)
            if m:
                clip_files.append((int(m.group(1)), os.path.join(ep_dir, fname)))
        clip_files.sort(key=lambda x: x[0])

        clips_data = []
        rendered_count = 0
        for c_num, c_path in clip_files:
            v_file = _find_clip_video_file(series_abs_dir, ep_num, ep_folder_name, c_num)
            f_file = _find_clip_frame_file(series_abs_dir, ep_num, c_num)
            if v_file:
                rendered_count += 1
            prompt_text = ""
            if include_prompts and os.path.isfile(c_path):
                try:
                    with open(c_path, "r", encoding="utf-8") as f:
                        prompt_text = f.read()
                except Exception:
                    prompt_text = ""
            elif os.path.isfile(c_path):
                try:
                    with open(c_path, "r", encoding="utf-8") as f:
                        prompt_text = f.read(240)
                except Exception:
                    prompt_text = ""

            clips_data.append(
                {
                    "clip_num": c_num,
                    "file_name": os.path.basename(c_path),
                    "file_path": c_path,
                    "prompt": prompt_text,
                    "status": "COMPLETED" if v_file else "PENDING",
                    "video_url": _media_url_for_path(v_file),
                    "video_size_mb": round(os.path.getsize(v_file) / (1024 * 1024), 2) if v_file else None,
                    "frame_url": _media_url_for_path(f_file),
                }
            )

        merged_file = _find_merged_episode_file(series_abs_dir, slug, ep_num, ep_folder_name)
        episodes.append(
            {
                "episode_num": ep_num,
                "folder_name": ep_folder_name,
                "label": f"{'Cảnh' if ep_prefix == 'canh' else 'Tập'} {ep_num:02d}",
                "total_clips": len(clips_data),
                "rendered_clips": rendered_count,
                "is_complete": len(clips_data) > 0 and rendered_count == len(clips_data),
                "merged_video_url": _media_url_for_path(merged_file),
                "merged_video_path": merged_file,
                "merged_size_mb": round(os.path.getsize(merged_file) / (1024 * 1024), 2) if merged_file else None,
                "clips": clips_data,
            }
        )

    return episodes


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
        episodes = _scan_channel_episodes(row, include_prompts=False)
        total_eps = len(episodes)
        total_clips = sum(ep["total_clips"] for ep in episodes)
        rendered_clips = sum(ep["rendered_clips"] for ep in episodes)
        merged_eps = sum(1 for ep in episodes if ep.get("merged_video_url"))
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
                    "total_clips": total_clips,
                    "rendered_clips": rendered_clips,
                    "merged_episodes": merged_eps,
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
    episodes = _scan_channel_episodes(row_dict, include_prompts=True)
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
    for c_idx in range(1, total_clips + 1):
        c_path = os.path.join(ep_dir, f"clip-{c_idx}.md")
        if body.overwrite or not os.path.exists(c_path):
            content = prompts_to_write[c_idx - 1]
            with open(c_path, "w", encoding="utf-8") as f:
                f.write(content)
        created_clips.append(c_idx)

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
        f"Tập {start_ep:02d} - Clip {only_clip:02d}"
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
    ext = os.path.splitext(abs_target)[1].lower()
    media_type = "video/mp4" if ext == ".mp4" else ("image/jpeg" if ext in (".jpg", ".jpeg") else "application/octet-stream")
    return FileResponse(abs_target, media_type=media_type, filename=os.path.basename(abs_target))


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
