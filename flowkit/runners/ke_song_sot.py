#!/usr/bin/env python3
"""
HỆ THỐNG TỰ ĐỘNG HÓA FLOWKIT NÂNG CAO CHO "KẺ SỐNG SÓT: BÓNG MA":
1. KHÓA NHÂN VẬT CỐ ĐỊNH (CHARACTER LOCK): Tự động lấy & khóa chính xác media_id của @Son, @May, @Ha, @HaiNgoc từ Google Flow Project.
2. Luôn truyền reference_media_ids (@Son, @May, @Ha, @HaiNgoc) qua endpoint /api/flow/generate-video-omni (MZZa6b Ingredients R2V) cho Clip 1 và mọi clip mở cảnh mới ([FORMAT]).
3. Tự động trích xuất khung hình cuối (last frame) làm khung hình đầu (start frame) của clip nối tiếp (Seamless Chaining).
4. Tự động đặt tên clip trên Google Flow theo cảnh ([CẢNH XX - CLIP YY]) và tải ngay về máy khi hoàn thành.
5. Tự động đồng bộ thời gian thực với Console Dashboard UI.
"""

import os
import sys
import time
import json
import base64
import subprocess
import requests
from datetime import datetime

os.environ["NO_PROXY"] = "127.0.0.1,localhost"
os.environ["no_proxy"] = "127.0.0.1,localhost"

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cms_integration import (
    push_cms_log,
    merge_episode_clips,
    merge_multi_scenes_to_episode,
    wait_if_cooldown_error,
    sync_clip_to_r2_and_d1,
    rewrite_prompt_on_failure,
    find_episode_clip_mp4s,
    force_rename_clip_on_flow,
)

FLOWKIT_API = "http://127.0.0.1:8200"
CHANNEL_SLUG = "ke-song-sot"
ONLY_CLIP = int(os.environ.get("FLOWKIT_ONLY_CLIP", "0") or "0")

# 👉 PROJECT_ID GOOGLE FLOW CỦA SERIES "KẺ SỐNG SÓT: BÓNG MA" — tạo project mới trên Flow rồi điền trên CMS (http://localhost:8200/)
PROJECT_ID = "0aac1598-f1d9-4de2-84e8-9a5c0edb1df8"
DEFAULT_PROJECT_ID = "0aac1598-f1d9-4de2-84e8-9a5c0edb1df8"
ASPECT_RATIO = "VIDEO_ASPECT_RATIO_LANDSCAPE"
IMAGE_ASPECT_RATIO = "IMAGE_ASPECT_RATIO_LANDSCAPE"

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SERIES_DIR = os.path.join(WORKSPACE_DIR, "ke-song-sot")
FRAMES_DIR = os.path.join(SERIES_DIR, "exported_frames")
OUTPUT_VIDEOS_DIR = os.path.join(SERIES_DIR, "output_videos")
CHAR_REFS_DIR = os.path.join(SERIES_DIR, "character_refs")
CHAR_CACHE_FILE = os.path.join(CHAR_REFS_DIR, "character_media_ids.json")

os.makedirs(FRAMES_DIR, exist_ok=True)
os.makedirs(OUTPUT_VIDEOS_DIR, exist_ok=True)
os.makedirs(CHAR_REFS_DIR, exist_ok=True)

# -------------------------------------------------------------
# 🔒 BẢNG ĐỊNH NGHĨA & KHÓA NHÂN VẬT CỐ ĐỊNH CỦA SERIES (KẺ SỐNG SÓT — 9 NHÂN VẬT CHÍNH & PHỤ)
# -------------------------------------------------------------
CHARACTER_SPECS = [
    {
        "key": "Son",
        "tag": "@Son",
        "aliases": ["@Son", "@Sơn", "SƠN (45", "SƠN in the past", "@Son = SƠN", "Son"],
        "default_media_id": "28356180-dea1-4c6c-bd80-8c3a41106957",
        "description": "Sơn 'Bóng Ma' (45 tuổi): sát thủ hợp đồng, người kể chuyện; tóc bạc hai bên, sẹo trắng mảnh ngang sống mũi, dây đồng hồ quả quýt ở thắt lưng; hiện tại áo khoác dã chiến ô liu, quá khứ vest đen găng da.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @Son, a 45-year-old Vietnamese man, 176 cm, lean and quiet, cropped black hair "
            "greying at the temples, weathered calm face, a thin old white scar across the bridge of his nose, a silver pocket-watch chain on his belt, "
            "faded olive field jacket over a grey shirt, dark trousers, worn brown boots; plain grey studio background, hard side light, 8K. Not resembling any real actor."
        ),
    },
    {
        "key": "May",
        "tag": "@May",
        "aliases": ["@May", "@Mây", "MÂY (38", "MÂY in civilian", "@May = MÂY", "Đại úy Mây", "May"],
        "default_media_id": "b210621a-c403-42cb-94d5-8c0024496843",
        "description": "Đại úy Mây (38 tuổi): trưởng công an thị trấn Hòn Sóng; tóc ngắn có lọn bạc phía trước, mặt rám nắng, sơ mi kaki xắn tay, sổ tay túi ngực, còng ở thắt lưng, không phù hiệu.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @May, a 38-year-old Vietnamese woman, 166 cm, athletic, sun-lined face, sharp warm eyes, "
            "short black hair with a single white streak at the front, plain khaki shirt with sleeves rolled, dark trousers, canvas shoes, a notebook in her "
            "chest pocket, handcuffs on her belt, no insignia; plain grey studio background, 8K."
        ),
    },
    {
        "key": "Ha",
        "tag": "@Ha",
        "aliases": ["@Ha", "@Hạ", "HẠ (32", "HẠ held captive", "HẠ free", "@Ha = HẠ", "Ha"],
        "default_media_id": "61e353d9-8e8a-48b1-934e-2f466ab87d09",
        "description": "Hạ (32 tuổi): cô chủ tiệm hoa, người yêu của Sơn; tóc đen dài buộc lỏng, khăn lụa xanh nhạt, đầm lanh kem, tạp dề xanh (quá khứ); váy xám không khăn (bị giữ); blouse trắng, khăn xanh (tự do).",
        "ref_prompt": (
            "Full-body photorealistic character reference of @Ha, a 32-year-old Vietnamese woman, 162 cm, slim, gentle bright face, long black hair tied "
            "loosely, a pale-blue silk scarf in her hair, cream linen dress, green canvas florist apron, flat sandals, holding white lily stems; plain grey "
            "studio background, soft warm light, 8K."
        ),
    },
    {
        "key": "HaiNgoc",
        "tag": "@HaiNgoc",
        "aliases": ["@HaiNgoc", "@HaiNgọc", "BÀ HAI NGỌC", "Bà Hai Ngọc", "HaiNgoc"],
        "default_media_id": "ff423460-c3ce-4d3f-8c4b-f74d2a657a2f",
        "description": "Bà Hai Ngọc (60 tuổi): trùm Rắn Đen, chủ tiệm lụa; búi tóc bạc, mặt phấn bình thản, vòng ngọc dày tay trái, tẩu đen, áo bà ba lụa tím.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @HaiNgoc, a small upright 60-year-old Vietnamese woman, 158 cm, silver hair in a tight bun, "
            "powdered calm face, a thick jade bracelet on her left wrist, a long black cigarette holder, violet silk áo bà ba with a high collar, black silk "
            "trousers, embroidered slippers; plain grey studio background, 8K."
        ),
    },
    {
        "key": "Dung",
        "tag": "@Dũng",
        "aliases": ["@Dũng", "@Dung", "DŨNG \"ĐINH\"", "Dũng Đinh", "Dũng"],
        "default_media_id": "29967c42-6378-4e6e-a656-101fbda18b0b",
        "description": "Dũng 'Đinh' (35 tuổi): tay sai số một của Rắn Đen; cao 180 cm, vai nặng, đầu đinh, khuyên tai bạc hình đinh ở tai trái, áo ba lỗ đen, bao súng luôn đóng.",
        "ref_prompt": (
            "Full-body photorealistic reference of a heavy-shouldered 35-year-old Vietnamese man, 180 cm, buzz cut, a small nail-shaped silver earring "
            "in his left ear, black sleeveless shirt, black jeans, boots, a closed leather holster, arms crossed, loud confident face; plain grey background, 8K, not resembling any real actor."
        ),
    },
    {
        "key": "VuKien",
        "tag": "@Vũ Kiên",
        "aliases": ["@Vũ Kiên", "@VuKien", "VŨ KIÊN", "Vũ Kiên"],
        "default_media_id": "cb559421-6180-43b2-bf78-ecc674c3b698",
        "description": "Vũ Kiên (50 tuổi): doanh nhân vest trắng, mục tiêu hợp đồng và Người Môi Giới; cao, tóc đen vuốt, vest trắng, đồng hồ vàng, nụ cười chính khách không bao giờ tắt.",
        "ref_prompt": (
            "Full-body photorealistic reference of a tall 50-year-old Vietnamese man with slicked black hair, a white tailored suit, white shirt, "
            "gold wristwatch, polished shoes, a wide politician's smile, one hand raised in greeting; plain grey background, 8K, not resembling any real actor."
        ),
    },
    {
        "key": "PhoThanh",
        "tag": "@Phó Thành",
        "aliases": ["@Phó Thành", "@PhoThanh", "PHÓ THÀNH", "Phó Thành"],
        "default_media_id": "80289d04-f26d-4ac0-892b-5515509ea1fb",
        "description": "Phó Thành (26 tuổi): phó công an của Mây; gầy, kính tròn, tóc rẽ ngôi, sơ mi xanh nhạt, không phù hiệu, nhiệt tình, lễ phép.",
        "ref_prompt": (
            "Full-body photorealistic reference of a skinny 26-year-old Vietnamese man with round glasses, neat side-parted hair, plain light-blue shirt, "
            "dark trousers, sneakers, holding a phone and a notebook, eager nervous face; plain grey background, 8K."
        ),
    },
    {
        "key": "BacSiLinh",
        "tag": "@Bác sĩ Linh",
        "aliases": ["@Bác sĩ Linh", "@BacSiLinh", "BÁC SĨ LINH", "Bác sĩ Linh"],
        "default_media_id": "d51873af-f5d5-48cd-844e-7d6fc9bf99a7",
        "description": "Bác sĩ Linh (55 tuổi): bác sĩ thị trấn; gầy, tóc bạc, kính gọng thép, áo blouse trắng sờn ngoài sơ mi ca rô, ống nghe, cầm đồng hồ bấm giờ.",
        "ref_prompt": (
            "Full-body photorealistic reference of a thin 55-year-old Vietnamese man, grey hair, wire glasses, worn white coat over a checked shirt, "
            "stethoscope, holding a small stopwatch, tired precise face; plain grey background, 8K."
        ),
    },
    {
        "key": "OngBay",
        "tag": "@Ông Bảy",
        "aliases": ["@Ông Bảy", "@OngBay", "ÔNG BẢY", "Ông Bảy"],
        "default_media_id": "eefba81d-07c5-42a5-bfe3-11bc176c6d4c",
        "description": "Ông Bảy (70 tuổi): chủ quán cà phê bờ kè; mập, ria bạc, áo ba lỗ trắng, quần đùi, nón lá, dép lê, luôn cầm khăn lau ly.",
        "ref_prompt": (
            "Full-body photorealistic reference of a stout 70-year-old Vietnamese man with a white moustache, white singlet, shorts, rubber sandals, "
            "conical hat pushed back, wiping a glass with a rag, cheerful face; plain grey background, 8K."
        ),
    },
]

LOCKED_CHARACTER_MEDIA_IDS = {}
SCENE_DB_MAP = {}
CURRENT_VIDEO_ID = None
CURRENT_EP_NUM = None
CURRENT_CLIP_NUM = None


def log(msg):
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] {msg}", flush=True)
    level = "INFO"
    if "❌" in msg:
        level = "ERROR"
    elif "⚠️" in msg:
        level = "WARN"
    elif any(icon in msg for icon in ("✅", "🎉", "💾", "🎞️", "🔒")):
        level = "SUCCESS"
    push_cms_log(
        CHANNEL_SLUG,
        level,
        "RUNNER",
        msg,
        project_id=PROJECT_ID,
        episode=CURRENT_EP_NUM,
        clip_num=CURRENT_CLIP_NUM,
    )


def print_box(title, items, border_char="─"):
    width = 72
    print(f"\n┌─ {title} " + border_char * (width - len(title) - 5) + "┐")
    for k, v in items:
        prefix = f"│ • {k}: "
        val_str = str(v)
        if len(prefix) + len(val_str) > width - 2:
            val_display = val_str[:width - len(prefix) - 5] + "..."
        else:
            val_display = val_str
        spacing = " " * max(0, width - len(prefix) - len(val_display) - 1)
        print(f"{prefix}{val_display}{spacing}│")
    print("└" + border_char * (width - 2) + "┘", flush=True)
    push_cms_log(
        CHANNEL_SLUG,
        "SUCCESS" if "HOÀN THÀNH" in title or "ĐÃ KHÓA" in title else "INFO",
        "API_BOX",
        title,
        project_id=PROJECT_ID,
        episode=CURRENT_EP_NUM,
        clip_num=CURRENT_CLIP_NUM,
        details={k: str(v) for k, v in items},
    )


def check_connection():
    try:
        r = requests.get(f"{FLOWKIT_API}/health", timeout=5)
        data = r.json()
        if not data.get("extension_connected"):
            log("⚠️ FlowKit server đang chạy nhưng Chrome Extension chưa kết nối!")
            log(f"👉 Mở Chrome có cài Extension và giữ mở tab https://labs.google/fx/vi/tools/flow/project/{PROJECT_ID}")
            return False
        log("✅ FlowKit & Chrome Extension đang kết nối tốt!")
        return True
    except Exception as e:
        log(f"❌ Không kết nối được tới FlowKit API ({FLOWKIT_API}): {e}")
        return False


# -------------------------------------------------------------
# 0. KHÓA NHÂN VẬT CỐ ĐỊNH (CHARACTER LOCK TỪ GOOGLE FLOW PROJECT)
# -------------------------------------------------------------
def load_and_lock_project_characters(force_remote: bool = False):
    """Đồng bộ và khóa đúng 9 nhân vật chính & phụ do người dùng tự tạo trong mục Characters trên Google Flow Project."""
    global LOCKED_CHARACTER_MEDIA_IDS
    log("🔒 Đang đồng bộ danh sách 9 Nhân vật chính & phụ (@Son, @May, @Ha, @HaiNgoc, @Dũng, @Vũ Kiên, @Phó Thành, @Bác sĩ Linh, @Ông Bảy) từ Google Flow Project...")

    cached_by_project = {}
    if os.path.exists(CHAR_CACHE_FILE):
        try:
            with open(CHAR_CACHE_FILE, "r", encoding="utf-8") as f:
                cached_by_project = json.load(f)
        except Exception:
            cached_by_project = {}

    project_cache = cached_by_project.get(PROJECT_ID, {}) if isinstance(cached_by_project, dict) else {}

    need_remote = force_remote or os.environ.get("FLOWKIT_REFRESH_CHARS") == "1"
    if not need_remote:
        for spec in CHARACTER_SPECS:
            tag = spec["tag"]
            if not (project_cache.get(tag) or spec.get("default_media_id")):
                need_remote = True
                break

    remote_chars = []
    if need_remote:
        try:
            r = requests.get(f"{FLOWKIT_API}/api/flow/project-characters", params={"project_id": PROJECT_ID}, timeout=30)
            if r.status_code == 200:
                remote_chars = r.json().get("characters") or []
                if remote_chars:
                    log(f"✅ Tìm thấy {len(remote_chars)} nhân vật đã tạo trong mục Characters của Project {PROJECT_ID}")
        except Exception as e:
            log(f"⚠️ Không truy vấn được danh sách nhân vật từ Google Flow (sẽ dùng ID khóa sẵn): {e}")

    locked = {}
    for spec in CHARACTER_SPECS:
        tag = spec["tag"]
        tag_clean = tag.lower().lstrip("@")
        aliases_lower = {a.lower().lstrip("@") for a in spec["aliases"]}
        matched_mid = None

        # 1. Ưu tiên khớp chính xác tên nhân vật trong mục Characters (payload[5]) trên Google Flow
        for rc in remote_chars:
            rc_name = (rc.get("name") or "").strip().lower().lstrip("@")
            if (rc_name == tag_clean or rc_name in aliases_lower) and rc.get("media_id"):
                matched_mid = rc["media_id"]
                break

        # 2. Fallback qua cache hoặc default_media_id đã đồng bộ
        if not matched_mid and project_cache.get(tag):
            matched_mid = project_cache[tag]

        if not matched_mid and spec.get("default_media_id"):
            matched_mid = spec["default_media_id"]

        if matched_mid:
            locked[tag] = matched_mid
            spec["default_media_id"] = matched_mid
        else:
            log(f"ℹ️ Nhân vật {tag} chưa được tạo trong mục Characters trên Google Flow Project {PROJECT_ID}.")

    LOCKED_CHARACTER_MEDIA_IDS = locked

    try:
        if not isinstance(cached_by_project, dict):
            cached_by_project = {}
        cached_by_project[PROJECT_ID] = locked
        with open(CHAR_CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(cached_by_project, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

    # Tự động ghi nhận default_media_id đã đồng bộ vào file runner nếu lấy từ remote
    if locked and remote_chars:
        try:
            import re as _re
            self_path = os.path.abspath(__file__)
            with open(self_path, "r", encoding="utf-8") as rf:
                self_code = rf.read()
            for t_tag, t_mid in locked.items():
                pat = rf'("tag":\s*"{_re.escape(t_tag)}"[\s\S]*?"default_media_id":\s*)"[^"]*"'
                self_code = _re.sub(pat, rf'\1"{t_mid}"', self_code, count=1)
            with open(self_path, "w", encoding="utf-8") as rf:
                rf.write(self_code)
        except Exception:
            pass

    box_items = [("Project ID", PROJECT_ID)]
    for spec in CHARACTER_SPECS:
        tag = spec["tag"]
        mid = LOCKED_CHARACTER_MEDIA_IDS.get(tag, "Chưa tạo trên Flow")
        box_items.append((f"Nhân Vật {tag}", f"media_id = {mid}"))
    box_items.append(("Chế Độ Khóa", "Ingredients R2V (/api/flow/generate-video-omni) + Seamless I2V"))
    print_box("🔒 ĐỒNG BỘ 9 NHÂN VẬT TỪ GOOGLE FLOW (CHARACTER LOCK)", box_items)


def is_new_scene_clip(prompt: str, clip_num: int, start_image_media_id: str = None) -> bool:
    if clip_num == 1 or not start_image_media_id:
        return True
    stripped = prompt.lstrip()
    if stripped.startswith(("Continue the scene seamlessly", "Continue the scene from")):
        return False
    if stripped.startswith("[FORMAT]") or stripped.startswith("[ĐỊNH DẠNG]"):
        return True
    return False


def get_clip_reference_media_ids(prompt: str) -> list:
    import re as _re
    # V3 declares visible people and printed portraits separately from voice-only
    # speakers and the previous-shot handoff. Those names must not spawn bodies.
    if "[CHARACTERS — approved identities and current appearances]" in prompt:
        reference_sections = _re.findall(
            r"^\[(?:CHARACTERS — approved identities and current appearances|PICTURE-ONLY REFERENCES)\]\s*\n(.*?)(?=^\[|\Z)",
            prompt,
            flags=_re.MULTILINE | _re.DOTALL,
        )
        reference_text = "\n".join(reference_sections)
        selected = []
        for spec in CHARACTER_SPECS:
            tag = spec["tag"]
            mid = LOCKED_CHARACTER_MEDIA_IDS.get(tag)
            tag_pat = rf"(?<![a-zA-Z0-9_À-ỹ]){_re.escape(tag)}(?![a-zA-Z0-9_À-ỹ])"
            if mid and _re.search(tag_pat, reference_text, flags=_re.IGNORECASE):
                if mid not in selected:
                    selected.append(mid)
        # An intentionally empty cast is a text-only shot, not four default faces.
        return selected[:7]
    selected = []
    for spec in CHARACTER_SPECS:
        tag = spec["tag"]
        mid = LOCKED_CHARACTER_MEDIA_IDS.get(tag)
        if not mid:
            continue
        # 1. Khớp chính xác @Tag có ranh giới từ (để @Ha không khớp nhầm vào @HaiNgoc)
        tag_pat = rf"(?<![a-zA-Z0-9_À-ỹ]){_re.escape(tag)}(?![a-zA-Z0-9_À-ỹ])"
        if _re.search(tag_pat, prompt, flags=_re.IGNORECASE):
            if mid not in selected:
                selected.append(mid)
            continue
        # 2. Khớp các định danh rõ ràng trong khối nhân vật / lời thoại
        for alias in spec["aliases"]:
            if len(alias) <= 3 and not alias.startswith("@"):
                continue
            alias_pat = rf"(?<![a-zA-Z0-9_À-ỹ]){_re.escape(alias)}(?![a-zA-Z0-9_À-ỹ])"
            if _re.search(alias_pat, prompt, flags=_re.IGNORECASE):
                if mid not in selected:
                    selected.append(mid)
                break
    if not selected:
        for spec in CHARACTER_SPECS[:4]:
            mid = LOCKED_CHARACTER_MEDIA_IDS.get(spec["tag"])
            if mid and mid not in selected:
                selected.append(mid)
    return selected[:7]


# -------------------------------------------------------------
# 1. ĐỒNG BỘ DỰ ÁN VỚI DASHBOARD UI (DATABASE SYNC)
# -------------------------------------------------------------
def sync_dashboard_database(start_scene: int = 1, end_scene: int = 60):
    """Đồng bộ tức thì Project, 9 Characters, Video, Scenes trực tiếp vào SQLite (flow_agent.db) mà không lo nghẽn HTTP timeout."""
    global CURRENT_VIDEO_ID, SCENE_DB_MAP
    log("🔄 Đang đồng bộ cơ sở dữ liệu với Dashboard UI...")

    db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "flow_agent.db")
    try:
        import sqlite3
        conn = sqlite3.connect(db_path, timeout=30)
        conn.execute(
            """INSERT INTO project (id, name, description, story, material, status, user_paygate_tier)
               VALUES (?, ?, ?, ?, ?, ?, ?)
               ON CONFLICT(id) DO UPDATE SET
                 name=excluded.name,
                 description=excluded.description,
                 story=excluded.story""",
            (
                PROJECT_ID,
                "Kẻ Sống Sót: Bóng Ma",
                "Phim hành động tâm lý neo-noir 60 phút (16:9, 60 cảnh × 6 clip).",
                "Sát thủ bị đường dây phản bội trốn về thị trấn biển, tự cho mình bảy ngày để phơi bày sổ tiền của chúng; nữ trưởng công an thị trấn và lọ thuốc gây liệt quyết định số phận anh.",
                "realistic",
                "ACTIVE",
                "PAYGATE_TIER_TWO",
            ),
        )
        chars_json = []
        for idx, spec in enumerate(CHARACTER_SPECS, start=1):
            mid = LOCKED_CHARACTER_MEDIA_IDS.get(spec["tag"]) or spec.get("default_media_id") or ""
            chars_json.append(
                {
                    "tag": spec["tag"],
                    "name": spec["tag"].lstrip("@"),
                    "default_media_id": mid,
                    "locked_media_id": mid,
                    "description": spec["description"],
                    "ref_prompt": spec["ref_prompt"],
                }
            )
            cid = f"char-kss-{idx:02d}"
            conn.execute(
                """INSERT INTO character (id, name, description, image_prompt, entity_type, media_id)
                   VALUES (?, ?, ?, ?, ?, ?)
                   ON CONFLICT(id) DO UPDATE SET
                     name=excluded.name,
                     description=excluded.description,
                     image_prompt=excluded.image_prompt,
                     media_id=excluded.media_id""",
                (cid, spec["tag"].lstrip("@"), spec["description"], spec["ref_prompt"], "character", mid or None),
            )
            conn.execute(
                "INSERT OR IGNORE INTO project_character (project_id, character_id) VALUES (?, ?)",
                (PROJECT_ID, cid),
            )

        conn.execute(
            "UPDATE cms_channel SET project_id = ?, characters_json = ? WHERE slug = ?",
            (PROJECT_ID, json.dumps(chars_json, ensure_ascii=False), CHANNEL_SLUG),
        )

        vrow = conn.execute("SELECT id FROM video WHERE project_id = ? LIMIT 1", (PROJECT_ID,)).fetchone()
        if vrow:
            CURRENT_VIDEO_ID = vrow[0]
            for sc_id, ord_val in conn.execute(
                "SELECT id, display_order FROM scene WHERE video_id = ?", (CURRENT_VIDEO_ID,)
            ).fetchall():
                ord_int = int(ord_val or 0)
                s_idx = (ord_int // 6) + 1
                c_idx = (ord_int % 6) + 1
                SCENE_DB_MAP[f"canh_{s_idx:02d}_clip_{c_idx:02d}"] = sc_id
        conn.commit()
        conn.close()
        log(f"✅ Đã đồng bộ Dashboard DB thành công! ({len(CHARACTER_SPECS)} nhân vật & 360 clips sẵn sàng)")
    except Exception as e:
        log(f"⚠️ Lỗi khi đồng bộ DB Dashboard: {e}")


def update_dashboard_scene_status(scene_num: int, clip_num: int, video_url: str):
    """Cập nhật trạng thái COMPLETED và link video lên Dashboard UI ngay lập tức."""
    key = f"canh_{scene_num:02d}_clip_{clip_num:02d}"
    sid = SCENE_DB_MAP.get(key)
    db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "flow_agent.db")
    try:
        import sqlite3
        conn = sqlite3.connect(db_path, timeout=30)
        if sid:
            conn.execute(
                "UPDATE scene SET horizontal_video_url = ?, horizontal_video_status = 'COMPLETED' WHERE id = ?",
                (video_url, sid),
            )
        clip_id = f"{CHANNEL_SLUG}:ep{scene_num:03d}:clip{clip_num:02d}"
        conn.execute(
            "UPDATE cms_clip SET status = 'COMPLETED', local_path = COALESCE(local_path, ?) WHERE id = ?",
            (video_url, clip_id),
        )
        conn.commit()
        conn.close()
        log(f"🖥️ [DASHBOARD UI] Đã cập nhật Scene '{key}' thành trạng thái COMPLETED ✅")
    except Exception as e:
        log(f"⚠️ Lỗi cập nhật Dashboard Scene: {e}")


# -------------------------------------------------------------
# 2. BỘ TỰ ĐỘNG SỬA PROMPT KHI THẤT BẠI (PROMPT SANITIZER & RETRY)
# -------------------------------------------------------------
def sanitize_prompt(prompt: str, attempt: int = 1) -> str:
    return rewrite_prompt_on_failure(prompt, attempt, CHARACTER_SPECS, ASPECT_RATIO)


def update_clip_file(scene_num: int, clip_num: int, new_prompt: str):
    fpath = os.path.join(SERIES_DIR, f"canh-{scene_num:02d}", f"clip-{clip_num}.md")
    try:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_prompt)
        log(f"💾 Đã ghi đè prompt đã sửa an toàn vào: {fpath}")
    except Exception as e:
        log(f"⚠️ Lỗi khi ghi file {fpath}: {e}")


# -------------------------------------------------------------
# 3. TỰ ĐỘNG TẢI VIDEO VỀ MÁY VÀ ĐỔI TÊN THEO CẢNH
# -------------------------------------------------------------
def download_and_rename_video(video_url: str, scene_num: int, clip_num: int) -> str:
    """Tải ngay lập tức video về máy và ghi đè (overwrite) đúng file clip chuẩn theo cảnh."""
    scene_folder = os.path.join(OUTPUT_VIDEOS_DIR, f"canh-{scene_num:02d}")
    os.makedirs(scene_folder, exist_ok=True)

    filename = f"canh-{scene_num:02d}_clip-{clip_num:02d}.mp4"
    target_path = os.path.join(scene_folder, filename)
    is_overwrite = os.path.exists(target_path)
    tmp_path = f"{target_path}.tmp"

    log("📥 Đang tải video từ Google Flow về máy...")
    try:
        r = requests.get(video_url, stream=True, timeout=120)
        if r.status_code == 200:
            with open(tmp_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        f.write(chunk)
            os.replace(tmp_path, target_path)
            size_mb = os.path.getsize(target_path) / (1024 * 1024)
            r2_sync = sync_clip_to_r2_and_d1(
                channel_slug=CHANNEL_SLUG,
                ep_num=scene_num,
                clip_num=clip_num,
                local_video_path=target_path,
                ep_folder_name=f"canh-{scene_num:02d}",
                project_id=PROJECT_ID,
            )
            box_rows = [
                ("Tên File Clip", filename),
                ("Chế Độ Lưu", "Ghi đè (Overwritten)" if is_overwrite else "Tạo mới"),
                ("Đường Dẫn Lưu", target_path),
                ("Dung Lượng", f"{size_mb:.2f} MB"),
                ("Thời Gian Hoàn Tất", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            ]
            if r2_sync.get("r2_url"):
                box_rows.append(("Cloudflare R2 URL", r2_sync["r2_url"]))
            print_box(
                "💾 CLIP HOÀN THÀNH & ĐÃ GHI ĐÈ VỀ MÁY" if is_overwrite else "💾 CLIP HOÀN THÀNH & ĐÃ TẢI VỀ MÁY",
                box_rows,
            )
            return target_path
        else:
            log(f"⚠️ Lỗi khi tải video (HTTP {r.status_code})")
    except Exception as e:
        log(f"⚠️ Ngoại lệ khi tải video: {e}")
    finally:
        if os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except Exception:
                pass
    return None


def fetch_media_video_url(media_id: str) -> str:
    """Truy vấn trực tiếp GET /api/flow/media/{media_id} để lấy signed fifeUrl."""
    if not media_id or media_id == "N/A":
        return None
    try:
        r = requests.get(f"{FLOWKIT_API}/api/flow/media/{media_id}", timeout=15)
        if r.status_code == 200:
            m_data = r.json()
            inner = m_data.get("data") if isinstance(m_data.get("data"), dict) else m_data
            video_info = inner.get("video") or {}
            fife_url = video_info.get("fifeUrl") or video_info.get("downloadUrl")
            if fife_url and fife_url.startswith("http"):
                return fife_url
    except Exception:
        pass
    return None


def extract_last_frame(video_source: str, scene_num: int, clip_num: int) -> str:
    """Trích xuất khung hình cuối cùng của clip bằng ffmpeg làm start frame cho clip sau."""
    out_frame = os.path.join(FRAMES_DIR, f"scene_{scene_num:02d}_clip_{clip_num:02d}_last.jpg")
    log(f"🎬 Dùng ffmpeg cắt khung hình cuối (Last Frame) của Cảnh {scene_num:02d} - Clip {clip_num:02d}...")
    try:
        cmd = [
            "ffmpeg", "-y",
            "-sseof", "-0.2",
            "-i", video_source,
            "-frames:v", "1",
            "-q:v", "2",
            out_frame
        ]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=45)
        if result.returncode == 0 and os.path.exists(out_frame) and os.path.getsize(out_frame) > 0:
            size_kb = os.path.getsize(out_frame) / 1024
            print_box(
                "🖼️ ĐÃ TRÍCH XUẤT KHUNG HÌNH CUỐI THÀNH CÔNG",
                [
                    ("Clip Nguồn", f"Cảnh {scene_num:02d} - Clip {clip_num:02d}"),
                    ("File Ảnh Nối Cảnh", os.path.basename(out_frame)),
                    ("Đường Dẫn Lưu", out_frame),
                    ("Dung Lượng Ảnh", f"{size_kb:.1f} KB"),
                    ("Mục Đích Sử Dụng", f"Nạp vào slot [Bắt đầu] cho Clip {clip_num + 1:02d} (Seamless Chaining)"),
                ]
            )
            return out_frame
        else:
            cmd_fallback = [
                "ffmpeg", "-y",
                "-ss", "00:00:09.5",
                "-i", video_source,
                "-frames:v", "1",
                "-q:v", "2",
                out_frame
            ]
            res_fb = subprocess.run(cmd_fallback, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=45)
            if res_fb.returncode == 0 and os.path.exists(out_frame) and os.path.getsize(out_frame) > 0:
                log(f"✨ Trích xuất khung hình cuối thành công (fallback ss 9.5s): {os.path.basename(out_frame)}")
                return out_frame
            else:
                log(f"⚠️ ffmpeg không trích xuất được frame: {result.stderr.decode('utf-8', errors='ignore')[:200]}")
                return None
    except Exception as e:
        log(f"⚠️ Lỗi khi trích xuất frame: {e}")
        return None


def upload_start_frame(image_path: str) -> str:
    """Nạp khung hình vừa cắt vào slot [Bắt đầu] trên Google Flow qua API."""
    if not image_path or not os.path.exists(image_path):
        return None
    url = f"{FLOWKIT_API}/api/flow/upload-image"
    try:
        with open(image_path, "rb") as f:
            b64_str = base64.b64encode(f.read()).decode("utf-8")

        payload = {
            "image_base64": b64_str,
            "project_id": PROJECT_ID,
            "file_name": os.path.basename(image_path),
            "mime_type": "image/jpeg"
        }
        res = requests.post(url, json=payload, timeout=45)
        if res.status_code == 200:
            res_json = res.json()
            media_id = (
                res_json.get("media_id")
                or res_json.get("_mediaId")
                or (res_json.get("data") or {}).get("media_id")
                or ((res_json.get("data") or {}).get("media") or {}).get("name")
            )
            print_box(
                "📤 ĐÃ TẢI ẢNH LÊN GOOGLE FLOW [BẮT ĐẦU]",
                [
                    ("Media ID", media_id),
                    ("File Ảnh Nối", os.path.basename(image_path)),
                    ("Slot Kích Hoạt", "Khung hình [Bắt đầu] (Start Frame) cho Clip tiếp theo"),
                    ("Trạng Thái", "Sẵn sàng Image-to-Video Omni Flash 10s ✅"),
                ]
            )
            return media_id
        else:
            log(f"⚠️ Không upload được frame: {res.text}")
            return None
    except Exception as e:
        log(f"⚠️ Lỗi upload frame: {e}")
        return None


# -------------------------------------------------------------
# 4. GỬI API REQUEST & LOG CHI TIẾT PARAMS (KHÓA NHÂN VẬT)
# -------------------------------------------------------------
def submit_clip_with_detailed_log(prompt: str, scene_num: int, clip_num: int, start_image_media_id: str = None):
    """Gửi yêu cầu tạo video và luôn khóa đúng nhân vật Kẻ Sống Sót."""
    if len(LOCKED_CHARACTER_MEDIA_IDS) < len(CHARACTER_SPECS):
        load_and_lock_project_characters()
    key = f"canh_{scene_num:02d}_clip_{clip_num:02d}"
    sid = SCENE_DB_MAP.get(key) or f"scene_{scene_num:02d}_clip_{clip_num:02d}"
    clip_tag = f"[CẢNH {scene_num:02d} - CLIP {clip_num:02d}]"
    flow_prompt = prompt if prompt.startswith(clip_tag) else f"{clip_tag}\n{prompt}"

    use_char_refs = is_new_scene_clip(prompt, clip_num, start_image_media_id)
    ref_media_ids = get_clip_reference_media_ids(prompt)

    if not use_char_refs and start_image_media_id:
        endpoint = "/api/flow/generate-video"
        mode = "🔗 Image-to-Video (Nối tiếp khung hình cuối Clip trước)"
        slot_desc = f"Start Frame = {start_image_media_id}"
        payload = {
            "start_image_media_id": start_image_media_id,
            "prompt": flow_prompt,
            "project_id": PROJECT_ID,
            "scene_id": sid,
            "duration_s": 10,
            "model_family": "omni_flash",
            "resolution": "720p",
            "aspect_ratio": ASPECT_RATIO
        }
    elif ref_media_ids:
        endpoint = "/api/flow/generate-video-omni"
        mode = f"🔒 Ingredients Reference-to-Video (Khóa {len(ref_media_ids)} nhân vật gốc Kẻ Sống Sót)"
        slot_desc = f"Ingredients Refs = {', '.join(ref_media_ids)}"
        payload = {
            "reference_media_ids": ref_media_ids,
            "prompt": flow_prompt,
            "project_id": PROJECT_ID,
            "scene_id": sid,
            "duration_s": 10,
            "resolution": "720p",
            "aspect_ratio": ASPECT_RATIO
        }
    else:
        endpoint = "/api/flow/generate-video-omni-text"
        mode = "🎬 Text-to-Video (Khung hình gốc mở đầu cảnh)"
        slot_desc = "[Trống - Khởi tạo từ Text]"
        payload = {
            "prompt": flow_prompt,
            "project_id": PROJECT_ID,
            "scene_id": sid,
            "duration_s": 10,
            "resolution": "720p",
            "aspect_ratio": ASPECT_RATIO
        }

    print_box(
        "📡 FLOWKIT API REQUEST CALL (CHARACTER LOCKED)",
        [
            ("Endpoint API", f"POST {endpoint}"),
            ("Tên Trên Google Flow", clip_tag),
            ("Phân Cảnh", f"Cảnh {scene_num:02d} - Clip {clip_num:02d}"),
            ("Chế Độ Tạo", mode),
            ("Khóa Hình Ảnh / Nhân Vật", slot_desc),
            ("Thời Lượng", "10 giây (Omni Flash 10s)"),
            ("Độ Phân Giải", "720p HD"),
            ("Tỉ Lệ Khung Hình", ASPECT_RATIO),
            ("Model Family", "omni_flash"),
            ("Độ Dài Prompt", f"{len(flow_prompt)} ký tự"),
            ("Prompt Preview", flow_prompt[:120].replace("\n", " ") + "..."),
        ]
    )

    url = f"{FLOWKIT_API}{endpoint}"
    res = requests.post(url, json=payload, timeout=60)
    return res


def poll_generation(submit_res_data: dict, scene_num: int, clip_num: int, timeout_s=360):
    """Theo dõi tiến trình sinh video cho đến khi hoàn thành."""
    url = f"{FLOWKIT_API}/api/flow/check-status"
    start_time = time.time()

    flow_poll = submit_res_data.get("flowkitPolling") or {}
    workflows = submit_res_data.get("workflows") or flow_poll.get("workflows") or []
    operations = submit_res_data.get("operations") or flow_poll.get("operations") or []
    media_list = submit_res_data.get("media") or []
    primary_media_id = None
    if media_list and isinstance(media_list, list) and len(media_list) > 0:
        primary_media_id = media_list[0].get("name")
    if not primary_media_id and workflows:
        primary_media_id = workflows[0].get("primary_media_id")

    poll_mode_desc = "workflows (Text-to-Video)" if workflows else ("operations (Ingredients R2V / Image-to-Video)" if operations else "direct media")
    log(f"⏳ Đang theo dõi tiến trình tạo video [Cảnh {scene_num:02d} - Clip {clip_num:02d}] (Chế độ: {poll_mode_desc})...")

    last_logged_time = 0
    while time.time() - start_time < timeout_s:
        elapsed = int(time.time() - start_time)
        try:
            if workflows:
                r = requests.post(url, json={"workflows": workflows, "project_id": PROJECT_ID}, timeout=30)
                if r.status_code == 200:
                    res_data = r.json()
                    st = res_data.get("status")
                    if st == "COMPLETED" or res_data.get("done") is True:
                        log(f"🎉 Google Flow render hoàn tất sau {elapsed}s!")
                        video_url = None
                        for wf in (res_data.get("workflows") or []):
                            m = wf.get("media") or {}
                            if m.get("url"):
                                video_url = m["url"]
                                break
                        if not video_url and primary_media_id:
                            video_url = fetch_media_video_url(primary_media_id)
                        if video_url:
                            force_rename_clip_on_flow(
                                FLOWKIT_API, PROJECT_ID, submit_res_data,
                                f"[CẢNH {scene_num:02d} - CLIP {clip_num:02d}]",
                                media_id=primary_media_id, log_fn=log,
                            )
                            return {"success": True, "video_url": video_url}
                    elif st in ["FAILED", "ERROR"]:
                        log(f"❌ Google Flow báo lỗi: {res_data}")
                        return {"success": False, "error": "FLOW_FAILED"}

            elif operations:
                r = requests.post(url, json={"operations": operations, "project_id": PROJECT_ID}, timeout=30)
                if r.status_code == 200:
                    res_data = r.json()
                    inner_ops = res_data.get("operations") or res_data.get("data", {}).get("operations") or []
                    all_done = True
                    has_failed = False
                    video_url = None
                    op_media_id = None

                    for op in inner_ops:
                        op_status = op.get("status", "")
                        if op_status == "MEDIA_GENERATION_STATUS_SUCCESSFUL":
                            op_meta = op.get("operation", {}).get("metadata", {}).get("video", {})
                            if not op_meta:
                                op_meta = op.get("metadata", {}).get("video", {})
                            v_url = op_meta.get("fifeUrl") or op_meta.get("downloadUrl")
                            if v_url:
                                video_url = v_url
                            op_media_id = op_meta.get("mediaId")
                        elif op_status == "MEDIA_GENERATION_STATUS_FAILED":
                            has_failed = True
                            all_done = False
                        else:
                            all_done = False

                    if has_failed:
                        log(f"❌ Operation thất bại: {res_data}")
                        return {"success": False, "error": "OPERATION_FAILED"}

                    if all_done and inner_ops:
                        log(f"🎉 Google Flow render hoàn tất sau {elapsed}s!")
                        target_mid = op_media_id or primary_media_id
                        if not video_url and target_mid:
                            video_url = fetch_media_video_url(target_mid)
                        if video_url:
                            force_rename_clip_on_flow(
                                FLOWKIT_API, PROJECT_ID, submit_res_data,
                                f"[CẢNH {scene_num:02d} - CLIP {clip_num:02d}]",
                                media_id=target_mid, log_fn=log,
                            )
                            return {"success": True, "video_url": video_url}

            if primary_media_id and elapsed >= 30:
                direct_url = fetch_media_video_url(primary_media_id)
                if direct_url:
                    log(f"🎉 Phát hiện video sẵn sàng qua Media API sau {elapsed}s!")
                    force_rename_clip_on_flow(
                        FLOWKIT_API, PROJECT_ID, submit_res_data,
                        f"[CẢNH {scene_num:02d} - CLIP {clip_num:02d}]",
                        media_id=primary_media_id, log_fn=log,
                    )
                    return {"success": True, "video_url": direct_url}

            if elapsed - last_logged_time >= 12:
                last_logged_time = elapsed
                log(f"   ...Google Flow đang vẽ video đúng nhân vật ({elapsed}s trôi qua)...")

        except Exception as e:
            log(f"   ...lỗi tạm thời khi poll ({e}), tiếp tục chờ...")

        time.sleep(6)

    log(f"⚠️ Hết thời gian chờ {timeout_s}s (Timeout) khi render Cảnh {scene_num:02d} - Clip {clip_num:02d}.")
    return {"success": False, "error": "TIMEOUT"}


# -------------------------------------------------------------
# 5. CHU TRÌNH ĐIỀU PHỐI TỔNG THỂ
# -------------------------------------------------------------
def _is_transient_transport_error(err_text: str) -> bool:
    t = (err_text or "").lower()
    transient_markers = (
        "no_injection_result",
        "asynchronous response",
        "message channel closed",
        "extension not connected",
        "read timed out",
        "connection aborted",
        "connection reset",
        "bad gateway",
        "service unavailable",
        "gateway timeout",
    )
    return any(m in t for m in transient_markers)


def run_clip_with_auto_retry(scene_num: int, clip_num: int, initial_prompt: str, start_image_media_id: str = None, max_retries: int = 6):
    current_prompt = initial_prompt
    policy_attempt = 0

    for attempt in range(1, max_retries + 1):
        if attempt > 1:
            log(f"🔄 [KHÔNG BỎ SÓT CLIP] Đang chạy lại Cảnh {scene_num:02d} - Clip {clip_num:02d} (Lần {attempt}/{max_retries})...")

        transient_fail = False
        try:
            res = submit_clip_with_detailed_log(current_prompt, scene_num, clip_num, start_image_media_id)
            if res.status_code == 200:
                data = res.json()
                inner = data.get("data") if isinstance(data.get("data"), dict) else data
                log("✅ Google Flow đã chấp nhận job tạo video.")

                poll_res = poll_generation(inner, scene_num, clip_num)
                if poll_res["success"] and poll_res.get("video_url"):
                    return poll_res
                else:
                    log(f"⚠️ Không nhận được video URL hoàn chỉnh ở lần thử {attempt} ({poll_res.get('error')}).")
            else:
                err_body = res.text or ""
                log(f"❌ Google Flow phản hồi lỗi (HTTP {res.status_code}): {err_body}")
                if wait_if_cooldown_error(err_body, FLOWKIT_API, log):
                    res_after = submit_clip_with_detailed_log(current_prompt, scene_num, clip_num, start_image_media_id)
                    if res_after.status_code == 200:
                        data = res_after.json()
                        inner = data.get("data") if isinstance(data.get("data"), dict) else data
                        log("✅ Google Flow đã chấp nhận job tạo video sau khi chờ Cooldown.")
                        poll_res = poll_generation(inner, scene_num, clip_num)
                        if poll_res["success"] and poll_res.get("video_url"):
                            return poll_res
                elif _is_transient_transport_error(err_body):
                    transient_fail = True
        except Exception as e:
            log(f"❌ Lỗi ngoại lệ khi gửi job: {e}")
            if _is_transient_transport_error(str(e)):
                transient_fail = True

        if attempt < max_retries:
            if transient_fail:
                log(f"⏳ Lỗi kết nối Extension tạm thời — giữ nguyên prompt gốc và thử lại sau 6 giây...")
                time.sleep(6)
                continue
            policy_attempt += 1
            log(f"🔧 [ĐỔI PROMPT TỰ ĐỘNG - CẤP ĐỘ {policy_attempt}] Đang làm mềm prompt trên bộ nhớ cho Cảnh {scene_num:02d} - Clip {clip_num:02d}...")
            current_prompt = sanitize_prompt(initial_prompt, policy_attempt)
            start_image_media_id = None
            log("🔄 Khóa trực tiếp nhân vật gốc (Ingredients R2V) và chạy lại sau 5 giây...")
            time.sleep(5)

    return {"success": False, "video_url": None}


def run_pipeline(start_scene=1, end_scene=60):
    global CURRENT_EP_NUM, CURRENT_CLIP_NUM
    print("\n" + "=" * 72)
    print("🎬 KHỞI ĐỘNG HỆ THỐNG FLOWKIT TỰ ĐỘNG THÔNG MINH — KẺ SỐNG SÓT")
    print(f"📁 Phạm vi: Cảnh {start_scene:02d} đến Cảnh {end_scene:02d} (6 clips/cảnh)")
    print(f"🔗 Google Flow Project: {PROJECT_ID}")
    print(f"💾 Tải video tự động về: {OUTPUT_VIDEOS_DIR}")
    print(f"🖼️ Lưu khung hình nối cảnh tại: {FRAMES_DIR}")
    print("=" * 72 + "\n", flush=True)

    if not check_connection():
        sys.exit(1)

    load_and_lock_project_characters()
    sync_dashboard_database(start_scene, end_scene)

    clip_indices = [ONLY_CLIP] if ONLY_CLIP > 0 else list(range(1, 7))
    total_clips = (end_scene - start_scene + 1) * len(clip_indices)
    completed_clips = 0

    for s in range(start_scene, end_scene + 1):
        CURRENT_EP_NUM = s
        print("\n" + "#" * 72)
        print(f"👉 BẮT ĐẦU CẢNH {s:02d}")
        print("#" * 72, flush=True)

        previous_clip_last_frame_media_id = None
        rendered_in_this_run = set()

        scene_dir = os.path.join(SERIES_DIR, f"canh-{s:02d}")
        for c_idx in clip_indices:
            CURRENT_CLIP_NUM = c_idx
            fpath = os.path.join(scene_dir, f"clip-{c_idx}.md")
            if not os.path.exists(fpath):
                continue

            with open(fpath, "r", encoding="utf-8") as f:
                prompt_content = f.read().strip()

            # Nếu clip hiện tại là CONTINUE (nối tiếp frame cuối của clip trước) nhưng chưa có media_id
            # (ví dụ chạy lẻ 1 clip trên UI), tự động lấy frame cuối của clip trước từ ổ cứng và upload!
            if (
                c_idx > 1
                and not previous_clip_last_frame_media_id
                and not is_new_scene_clip(prompt_content, c_idx, "CHECK_CONTINUE")
            ):
                prev_frame_path = os.path.join(FRAMES_DIR, f"scene_{s:02d}_clip_{c_idx - 1:02d}_last.jpg")
                if not os.path.exists(prev_frame_path):
                    prev_video_path = os.path.join(OUTPUT_VIDEOS_DIR, f"canh-{s:02d}", f"canh-{s:02d}_clip-{c_idx - 1:02d}.mp4")
                    if os.path.exists(prev_video_path):
                        prev_frame_path = extract_last_frame(prev_video_path, s, c_idx - 1)
                if prev_frame_path and os.path.exists(prev_frame_path):
                    previous_clip_last_frame_media_id = upload_start_frame(prev_frame_path)

            completed_clips += 1
            progress_pct = (completed_clips / max(1, total_clips)) * 100
            print(f"\n▶️ TIẾN ĐỘ TỔNG: [{completed_clips}/{total_clips}] ({progress_pct:.1f}%) — CẢNH {s:02d} - CLIP {c_idx:02d}", flush=True)

            res = run_clip_with_auto_retry(
                scene_num=s,
                clip_num=c_idx,
                initial_prompt=prompt_content,
                start_image_media_id=previous_clip_last_frame_media_id
            )

            if res["success"] and res.get("video_url"):
                video_url = res["video_url"]
                local_video = download_and_rename_video(video_url, s, c_idx)
                if local_video:
                    rendered_in_this_run.add(c_idx)
                    frame_path = extract_last_frame(local_video, s, c_idx)
                    next_fpath = os.path.join(scene_dir, f"clip-{c_idx + 1}.md")
                    if c_idx < 6 and frame_path and os.path.exists(next_fpath):
                        with open(next_fpath, "r", encoding="utf-8") as nf:
                            next_prompt = nf.read().strip()
                        if not is_new_scene_clip(next_prompt, c_idx + 1, "CHECK_CONTINUE"):
                            previous_clip_last_frame_media_id = upload_start_frame(frame_path)
                        else:
                            previous_clip_last_frame_media_id = None
                    else:
                        previous_clip_last_frame_media_id = None
                else:
                    previous_clip_last_frame_media_id = None
                update_dashboard_scene_status(s, c_idx, local_video if local_video else video_url)
            else:
                log(f"⚠️ [Cảnh {s:02d} - Clip {c_idx:02d}] Bị bỏ qua do không hoàn tất render.")
                previous_clip_last_frame_media_id = None

            log("⏳ Nghỉ 5 giây trước khi tiếp tục clip kế tiếp...")
            time.sleep(5)

        # 🛡️ VÒNG LẶP VÉT CẠN: Đảm bảo 100% không bỏ sót bất kỳ clip nào của Cảnh trước khi ghép FULL
        existing_nums = rendered_in_this_run if ONLY_CLIP > 0 else {cn for cn, _ in find_episode_clip_mp4s(OUTPUT_VIDEOS_DIR, s, f"canh-{s:02d}")}
        missing_clips = [c_idx for c_idx in clip_indices if c_idx not in existing_nums and os.path.exists(os.path.join(scene_dir, f"clip-{c_idx}.md"))]
        if missing_clips:
            log(f"🛡️ [CAM KẾT KHÔNG BỎ SÓT] Phát hiện Cảnh {s:02d} còn thiếu {len(missing_clips)} clip ({missing_clips}). Đang đổi sang Ultra-Safe Prompt & render bù ngay!")
            for mc in missing_clips:
                CURRENT_CLIP_NUM = mc
                fpath_m = os.path.join(scene_dir, f"clip-{mc}.md")
                with open(fpath_m, "r", encoding="utf-8") as f:
                    raw_p = f.read().strip()
                ultra_safe_p = sanitize_prompt(raw_p, attempt=3)
                update_clip_file(s, mc, ultra_safe_p)
                rec_res = run_clip_with_auto_retry(scene_num=s, clip_num=mc, initial_prompt=ultra_safe_p, start_image_media_id=None, max_retries=4)
                if rec_res["success"] and rec_res.get("video_url"):
                    local_v = download_and_rename_video(rec_res["video_url"], s, mc)
                    update_dashboard_scene_status(s, mc, local_v if local_v else rec_res["video_url"])

        CURRENT_CLIP_NUM = None
        merge_episode_clips(SERIES_DIR, CHANNEL_SLUG, s, f"canh-{s:02d}", project_id=PROJECT_ID, unit_label="Cảnh")
        if s % 10 == 0:
            tap_num = s // 10
            merge_multi_scenes_to_episode(SERIES_DIR, CHANNEL_SLUG, tap_num, s - 9, s, project_id=PROJECT_ID)

    print("\n" + "=" * 72)
    print(f"🎉 HOÀN THÀNH TOÀN BỘ CHU TRÌNH TỪ CẢNH {start_scene:02d} ĐẾN CẢNH {end_scene:02d}!")
    print(f"📁 Video hoàn chỉnh đã được lưu tại: {OUTPUT_VIDEOS_DIR}")
    print("=" * 72 + "\n", flush=True)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ("--init-chars", "init-chars", "0"):
        check_connection()
        load_and_lock_project_characters(force_remote=True)
        sync_dashboard_database(1, 60)
        sys.exit(0)
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 60
    run_pipeline(start, end)
