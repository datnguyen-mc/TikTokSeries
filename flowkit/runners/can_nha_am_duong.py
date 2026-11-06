#!/usr/bin/env python3
"""
HỆ THỐNG TỰ ĐỘNG HÓA FLOWKIT NÂNG CAO CHO "CĂN NHÀ ÂM DƯƠNG":
1. KHÓA NHÂN VẬT CỐ ĐỊNH (CHARACTER LOCK): Tự động tạo/lấy & khóa chính xác media_id của @Binh, @BaPhuong, @OngQuan, @OngBay, @VongCuXa từ Google Flow Project.
2. MỖI CLIP 10 GIÂY (10.0s) VỚI MODEL GOOGLE FLOW OMNI (omni_flash, 10s Ingredients Reference-to-Video):
   - Chuẩn 80% Người dẫn chuyện VO (VOICE_LOCK_NARRATOR_CNHADG, nhân vật trên hình khép miệng) + 20% Thoại nhân vật bất ngờ (Lip-Sync).
   - Khóa chặt danh tính nhân vật trực tiếp qua Ingredients R2V (/api/flow/generate-video-omni) với đúng các nhân vật xuất hiện trong khung hình ([CHARACTERS]).
3. Tự động đặt tên clip trên Google Flow theo cảnh ([CẢNH XX - CLIP YY]) và tải ngay về máy + đồng bộ Cloudflare R2 & D1 khi hoàn thành.
4. Tự động đồng bộ thời gian thực với Console Dashboard UI (SQLite flow_agent.db).
"""

import os
import re
import sys
import time
import json
import base64
import sqlite3
import subprocess
import requests
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cms_integration import (
    push_cms_log,
    wait_if_cooldown_error,
    sync_clip_to_r2_and_d1,
    rewrite_prompt_on_failure,
    find_episode_clip_mp4s,
    force_rename_clip_on_flow,
    is_clip_completed_in_db,
    is_clip_failed_in_db,
    persist_updated_prompt,
    mark_clip_failed_in_db,
    trim_studio_reference_frames,
)

FLOWKIT_API = "http://127.0.0.1:8200"
CHANNEL_SLUG = "can-nha-am-duong"
ONLY_CLIP = int(os.environ.get("FLOWKIT_ONLY_CLIP", "0") or "0")

# 👉 PROJECT_ID GOOGLE FLOW CỦA SERIES "CĂN NHÀ ÂM DƯƠNG"
PROJECT_ID = "3b955883-7851-42fe-a986-5ef82b4912e5"
DEFAULT_PROJECT_ID = PROJECT_ID
ASPECT_RATIO = "VIDEO_ASPECT_RATIO_LANDSCAPE"
IMAGE_ASPECT_RATIO = "IMAGE_ASPECT_RATIO_LANDSCAPE"

# 👉 CẤU HÌNH MODEL GOOGLE FLOW OMNI 10 GIÂY (OMNI_FLASH 10S)
VIDEO_MODEL_FAMILY = "omni_flash"
VIDEO_MODEL_NAME = "omni_flash"
CLIP_DURATION_S = 10
TOTAL_SCENES = 15

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SERIES_DIR = os.path.join(WORKSPACE_DIR, "can-nha-am-duong")
FRAMES_DIR = os.path.join(SERIES_DIR, "exported_frames")
OUTPUT_VIDEOS_DIR = os.path.join(SERIES_DIR, "output_videos")
CHAR_REFS_DIR = os.path.join(SERIES_DIR, "character_refs")
CHAR_CACHE_FILE = os.path.join(CHAR_REFS_DIR, "character_media_ids.json")

os.makedirs(FRAMES_DIR, exist_ok=True)
os.makedirs(OUTPUT_VIDEOS_DIR, exist_ok=True)
os.makedirs(CHAR_REFS_DIR, exist_ok=True)

# -------------------------------------------------------------
# 🎙️ QUY ĐỊNH & KHÓA CỐ ĐỊNH GIỌNG ĐỌC NGƯỜI DẪN CHUYỆN (NARRATOR VOICE LOCK — CHUẨN MIỀN BẮC)
# -------------------------------------------------------------
NARRATOR_VOICE_SPEC = {
    "voice_lock_id": "VOICE_LOCK_NARRATOR_CNHADG",
    "role": "Người Dẫn Chuyện (Off-Screen Male Horror Narrator — 80% thời lượng / 72 Clips)",
    "style_reference": "MC Đình Soạn — HẺM Truyện Ma (Giọng nam chuẩn miền Bắc thanh thoát, trầm ấm, nhấn nhá rùng rợn lúc đêm khuya)",
    "gender_age": "42-year-old native Hanoi Standard Northern Vietnamese male storyteller (Nam trung niên 42 tuổi chuẩn giọng Hà Nội - miền Bắc)",
    "acoustic_profile": (
        "Deep, warm yet bone-chilling mid-baritone (~110 Hz fundamental pitch), open chest resonance, "
        "clear and unhurried storytelling articulation (thanh thoát, trầm ấm, nhấn nhá rùng rợn lúc đêm khuya), "
        "measured 0.95x speaking rate (135 words/min) with haunting 0.4s pauses at ellipses (…), "
        "crisp Northern Vietnamese consonant distinction (s/x, tr/ch, r/d/gi) and authentic 6-tone Hanoi cadence."
    ),
    "strict_rules": (
        "1. Cố định 100% một giọng Nam Người Dẫn Chuyện chuẩn miền Bắc (VOICE_LOCK_NARRATOR_CNHADG) xuyên suốt toàn bộ 90 clips (Cảnh 01 -> Cảnh 15). "
        "2. TUYỆT ĐỐI KHÔNG đổi sang giọng miền Nam (Sài Gòn/Miền Tây), giọng miền Trung, giọng nữ, giọng nam trẻ cao vút hoặc giọng đọc máy công nghiệp. "
        "3. Trong tất cả các clip VO (Người dẫn chuyện đọc ngoài khung hình), toàn bộ nhân vật xuất hiện trên màn hình PHẢI KHÉP MIỆNG TỰ NHIÊN (mouths remain naturally closed 0.0–10.0s), chỉ diễn xuất bằng ánh mắt, hơi thở và hành động."
    ),
    "prompt_directive": (
        "Narrator (Người Dẫn Chuyện) = Off-screen 42-year-old native Standard Northern Vietnamese male horror storyteller "
        "(MC Đình Soạn — HẺM Truyện Ma style). Voice profile: [VOICE_LOCK_NARRATOR_CNHADG — Cố định giọng Nam Người Dẫn Chuyện "
        "chuẩn miền Bắc xuyên suốt 90 clips]: Deep, resonant mid-baritone (~110 Hz), expressive, clear yet bone-chilling "
        "42-year-old native Hanoi Standard Northern Vietnamese male storyteller voice (giọng nam chuẩn miền Bắc thanh thoát, trầm ấm, "
        "nhấn nhá rùng rợn lúc đêm khuya chuẩn phong cách MC Đình Soạn HẺM Truyện Ma, tốc độ 0.95x). Strictly lock this exact "
        "vocal timbre, pitch, and pacing across all 90 clips; NEVER use a Southern or Central accent, never switch to a female or "
        "high-pitched voice, and never sound like a robotic TTS engine."
    ),
}

# -------------------------------------------------------------
# 🔒 BẢNG ĐỊNH NGHĨA & KHÓA 6 NHÂN VẬT CỐ ĐỊNH CỦA SERIES (CĂN NHÀ ÂM DƯƠNG)
# -------------------------------------------------------------
CHARACTER_SPECS = [
    {
        "key": "Binh",
        "tag": "@Binh",
        "aliases": ["@Binh", "@Bình", "Bình", "Binh"],
        "default_media_id": "a1a78643-ce72-4217-86c7-b53b927e637a",
        "voice_lock": "VOICE_LOCK_BINH_CNHADG",
        "voice_profile": "Fixed 21-year-old native Standard Northern Vietnamese young male voice (~135 Hz tenor-baritone), trembling, anxious, guilt-ridden and breathless in horror moments (giọng nam trẻ 21 tuổi chuẩn miền Bắc, run rẩy, nghẹn ngào).",
        "description": "Nam sinh viên năm cuối 21 tuổi; 172 cm, dáng gầy nhợt nhạt, tóc đen ngắn rối, quầng mắt thâm, mặc áo hoodie xám bạc bên ngoài áo thun trắng nhàu, quần jean tối, đeo ba lô đen.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @Binh, a 21-year-old Vietnamese male university student, "
            "172 cm, thin pale build, messy short black hair, tired dark eyes with visible dark circles underneath, "
            "wearing a faded grey hoodie over a wrinkled white T-shirt, dark slim jeans, worn sneakers, carrying a "
            "black backpack; anxious guilty expression; plain grey studio background, soft cinematic side light, 8K. Not resembling any real actor."
        ),
    },
    {
        "key": "BaPhuong",
        "tag": "@BaPhuong",
        "aliases": ["@BaPhuong", "Bà Phượng", "BaPhuong", "Phượng"],
        "default_media_id": "a17f2e3b-8272-4cff-8de0-1c3ec43a11b1",
        "voice_lock": "VOICE_LOCK_PHUONG_CNHADG",
        "voice_profile": "Fixed 50-year-old native Standard Northern Vietnamese maternal female voice (~205 Hz warm mezzo), tearful, choked with heartache and maternal worry (giọng nữ trung niên 50 tuổi chuẩn miền Bắc, ấm áp, lo âu).",
        "description": "Nữ giáo viên về hưu 50 tuổi; 158 cm, tóc đen búi thấp lấm tấm bạc, gương mặt trái xoan nhân hậu nhưng phiền muộn, mặc áo sơ mi giản dị và quần tối.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @BaPhuong, a 50-year-old Vietnamese female retired school teacher, "
            "158 cm, neat black hair in a low bun with grey streaks, gentle worried oval face, "
            "wearing a simple pastel blouse and dark trousers, indoor slippers; plain grey studio background, soft side light, 8K. Not resembling any real actor."
        ),
    },
    {
        "key": "OngQuan",
        "tag": "@OngQuan",
        "aliases": ["@OngQuan", "Ông Quân", "OngQuan", "Quân"],
        "default_media_id": "e845a88f-7cd2-4b8f-9fa3-e75e7e337674",
        "voice_lock": "VOICE_LOCK_QUAN_CNHADG",
        "voice_profile": "Fixed 55-year-old native Standard Northern Vietnamese male baritone voice (~105 Hz stern baritone), gravelly, authoritative, hot-tempered at first then deeply remorseful (giọng nam trung niên 55 tuổi chuẩn miền Bắc, trầm đanh, uy nghiêm).",
        "description": "Nam nhân viên văn phòng 55 tuổi; 170 cm, dáng chắc, tóc húi cua bạc, gương mặt đanh nghiêm khắc, mùi thuốc lá, mặc áo sơ mi cổ cồn và quần tối.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @OngQuan, a 55-year-old Vietnamese male office worker, "
            "170 cm, stocky build, crew-cut greying hair, stern weathered face with deep frown lines, "
            "wearing a collared dress shirt with sleeves rolled and dark trousers, leather belt; "
            "plain grey studio background, hard side light, 8K. Not resembling any real actor."
        ),
    },
    {
        "key": "OngBay",
        "tag": "@OngBay",
        "aliases": ["@OngBay", "Ông Bảy", "OngBay", "Bảy"],
        "default_media_id": "10e5cdcf-3dd1-4b41-b999-21922b65de89",
        "voice_lock": "VOICE_LOCK_BAY_CNHADG",
        "voice_profile": "Fixed 60-year-old native Standard Northern Vietnamese rural elderly male voice (~115 Hz rustic baritone), warm, candid, grounded and hushed when warning of ghosts (giọng bác nông dân 60 tuổi chuẩn miền Bắc, mộc mạc, ấm áp).",
        "description": "Nam nông dân 60 tuổi; 168 cm, da ngăm đen, tóc bạc lấm tấm, gương mặt hiền hậu nhiều nếp nhăn, mặc áo sơ mi kẻ cũ và quần nâu, đi dép cao su.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @OngBay, a 60-year-old Vietnamese male rice farmer, "
            "168 cm, lean tanned dark-skinned build, silver-streaked hair, kind wrinkled face with warm eyes, "
            "wearing a faded plaid button-up shirt and brown work trousers, rubber sandals; "
            "plain grey studio background, warm side light, 8K. Not resembling any real actor."
        ),
    },
    {
        "key": "VongCuXa",
        "tag": "@VongCuXa",
        "aliases": ["@VongCuXa", "Cụ Xá", "Ông nội", "VongCuXa"],
        "default_media_id": "f8d1ff26-6134-4fa4-8c0f-13e8405e5f64",
        "voice_lock": "VOICE_LOCK_CUXA_CNHADG",
        "voice_profile": "Fixed 80-year-old native Standard Northern Vietnamese spectral elderly male voice (~98 Hz aged resonant bass-baritone), hoarse, slow, echoing with ancestral sorrow (giọng cụ già 80 tuổi chuẩn miền Bắc, khàn đục, vọng âm).",
        "description": "Vong hồn ông nội; gầy gò mờ ảo bán trong suốt, tóc trắng thưa, mắt tối buồn sâu hoắm, mặc áo bà ba nâu sồng truyền thống đã bạc, chân trần.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @VongCuXa, a ghostly translucent elderly Vietnamese male apparition, "
            "gaunt frail frame, wispy white hair, sad hollow dark eyes, wearing a faded traditional brown cotton tunic "
            "(áo bà ba nâu sồng), barefoot; semi-transparent ethereal ghost appearance with faint moonlight glow; "
            "plain dark studio background, cold blue-white rim light, 8K. Not resembling any real actor."
        ),
    },
    {
        "key": "VongLa",
        "tag": "@VongLa",
        "aliases": ["@VongLa", "Vong lạ", "VongLa", "Vong gốc mít"],
        "default_media_id": "0c2ade1f-c1cd-4c93-98e2-697231a54887",
        "voice_lock": "VOICE_LOCK_VONGLA_CNHADG",
        "voice_profile": "Chilling echoing Standard Northern Vietnamese spectral whisper reverberating from all directions in the dark (giọng ma vọng lạnh lẽo chuẩn miền Bắc từ bốn phía).",
        "description": "Vong hồn vất vưởng dưới gốc mít cổ thụ đầu cổng; bóng người cao gầy như que củi, da xám ngoét ướt đẫm sương đêm, tóc rối bết che nửa mặt, bàn tay xương xẩu có những ngón tay dài ngoằng lạnh buốt.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @VongLa, a terrifying wandering Vietnamese spirit entity, "
            "tall skeletal emaciated silhouette, ash-grey damp skin, tangled wet black hair covering half the face, "
            "glowing pale eyes in shadow, tattered dark wet clothes, long bony fingers; "
            "plain dark studio background, eerie cyan-green rim light, 8K. Not resembling any real actor."
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
    print(f"\n┌─ {title} " + border_char * max(1, width - len(title) - 5) + "┐")
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


def _is_valid_media_id(mid: str) -> bool:
    if not mid or not isinstance(mid, str) or len(mid) < 20:
        return False
    return True


# -------------------------------------------------------------
# 0. KHÓA NHÂN VẬT CỐ ĐỊNH (CHARACTER LOCK TỪ GOOGLE FLOW PROJECT)
# -------------------------------------------------------------
def load_and_lock_project_characters(force_remote: bool = False):
    """Đảm bảo 100% sử dụng đúng 5 nhân vật Căn Nhà Âm Dương (@Binh, @BaPhuong, @OngQuan, @OngBay, @VongCuXa) với media_id thực trên Google Flow."""
    global LOCKED_CHARACTER_MEDIA_IDS
    log("🔒 Đang đồng bộ danh sách 5 Nhân vật cố định (@Binh, @BaPhuong, @OngQuan, @OngBay, @VongCuXa) trên Google Flow Project...")

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
            if not (_is_valid_media_id(project_cache.get(tag)) or _is_valid_media_id(spec.get("default_media_id"))):
                need_remote = True
                break

    remote_chars = []
    if need_remote:
        try:
            r = requests.get(f"{FLOWKIT_API}/api/flow/project-characters", params={"project_id": PROJECT_ID}, timeout=30)
            if r.status_code == 200:
                remote_chars = r.json().get("characters") or []
        except Exception as e:
            log(f"⚠️ Không truy vấn được danh sách nhân vật từ Google Flow: {e}")

    locked = {}
    for spec in CHARACTER_SPECS:
        tag = spec["tag"]
        aliases_lower = {a.lower().lstrip("@") for a in spec["aliases"]}
        matched_mid = None

        for rc in remote_chars:
            rc_name = (rc.get("name") or "").strip().lower().lstrip("@")
            if rc_name in aliases_lower and _is_valid_media_id(rc.get("media_id")):
                matched_mid = rc["media_id"]
                break

        if not matched_mid and _is_valid_media_id(project_cache.get(tag)):
            matched_mid = project_cache[tag]

        if not matched_mid and _is_valid_media_id(spec.get("default_media_id")):
            matched_mid = spec["default_media_id"]

        if not matched_mid and spec.get("ref_prompt"):
            log(f"🎨 Đang tạo mới Nhân Vật & ảnh mẫu cố định cho {tag} trên Project {PROJECT_ID}...")
            try:
                gen_res = requests.post(
                    f"{FLOWKIT_API}/api/flow/create-character",
                    json={
                        "name": tag,
                        "prompt": spec["ref_prompt"],
                        "description": spec.get("description", ""),
                        "project_id": PROJECT_ID,
                        "aspect_ratio": IMAGE_ASPECT_RATIO,
                        "image_model": "nano_banana_pro",
                    },
                    timeout=90,
                )
                if gen_res.status_code == 200:
                    gdata = gen_res.json()
                    matched_mid = gdata.get("_mediaId") or gdata.get("media_id")
                    if not matched_mid:
                        medias = gdata.get("media") or (gdata.get("data") or {}).get("media") or []
                        if medias and isinstance(medias[0], dict):
                            matched_mid = medias[0].get("name") or medias[0].get("media_id")
            except Exception as e:
                log(f"⚠️ Không tự tạo được ảnh mẫu cho {tag}: {e}")

        if _is_valid_media_id(matched_mid):
            locked[tag] = matched_mid
            spec["default_media_id"] = matched_mid

    LOCKED_CHARACTER_MEDIA_IDS = locked

    try:
        if not isinstance(cached_by_project, dict):
            cached_by_project = {}
        cached_by_project[PROJECT_ID] = locked
        with open(CHAR_CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(cached_by_project, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

    box_items = [("Project ID", PROJECT_ID)]
    box_items.append((
        "🎙️ Giọng Dẫn Chuyện (VO 80%)",
        f"{NARRATOR_VOICE_SPEC['voice_lock_id']} — {NARRATOR_VOICE_SPEC['style_reference']}",
    ))
    for spec in CHARACTER_SPECS:
        tag = spec["tag"]
        mid = LOCKED_CHARACTER_MEDIA_IDS.get(tag, "Chưa có (sẽ tự tạo khi chạy)")
        vlock = spec.get("voice_lock", "")
        box_items.append((f"Nhân Vật {tag}", f"media_id = {mid} | {vlock}"))
    box_items.append(("Model Video", f"{VIDEO_MODEL_NAME} (Google Flow Omni — {CLIP_DURATION_S}s/clip)"))
    box_items.append(("Chế Độ Khóa", "Ingredients R2V (/api/flow/generate-video-omni 10s)"))
    print_box("🔒 ĐÃ KHÓA 6 NHÂN VẬT, GIỌNG NGƯỜI DẪN CHUYỆN & CẤU HÌNH GOOGLE FLOW OMNI 10S", box_items)


def get_clip_reference_media_ids(prompt: str) -> list:
    """Chỉ lấy đúng media_id của các nhân vật được khai báo đầu dòng trong khối [CHARACTERS] của shot hiện tại."""
    if "[CHARACTERS" in prompt:
        char_block = prompt.split("[CHARACTERS", 1)[1].split("[TIMELINE", 1)[0]
        defined_tags = re.findall(r"^(@[A-Za-z0-9_]+)\s*=", char_block, flags=re.MULTILINE)
        selected = []
        for tag in defined_tags:
            mid = LOCKED_CHARACTER_MEDIA_IDS.get(tag)
            if mid and mid not in selected:
                selected.append(mid)
        if selected:
            return selected[:7]

    selected = []
    for spec in CHARACTER_SPECS:
        tag = spec["tag"]
        mid = LOCKED_CHARACTER_MEDIA_IDS.get(tag)
        if not mid:
            continue
        tag_pat = rf"(?<![a-zA-Z0-9_À-ỹ]){re.escape(tag)}(?![a-zA-Z0-9_À-ỹ])"
        if re.search(tag_pat, prompt, flags=re.IGNORECASE):
            if mid not in selected:
                selected.append(mid)
    return selected[:7]


# -------------------------------------------------------------
# 1. ĐỒNG BỘ DỰ ÁN VỚI DASHBOARD UI & CMS TABLES (DATABASE SYNC)
# -------------------------------------------------------------
def sync_dashboard_database(start_scene: int = 1, end_scene: int = TOTAL_SCENES):
    """Đồng bộ tức thì cms_channel, cms_episode (15 cảnh), cms_clip (90 clips), project, character, video, scene vào SQLite (flow_agent.db)."""
    global CURRENT_VIDEO_ID, SCENE_DB_MAP
    log("🔄 Đang đồng bộ cơ sở dữ liệu 'Căn Nhà Âm Dương' với Console Dashboard UI (Google Flow Omni 10s)...")

    db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "flow_agent.db")
    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    try:
        conn = sqlite3.connect(db_path, timeout=30)
        conn.execute(
            """INSERT INTO project (id, name, description, story, material, status, user_paygate_tier, video_model_family)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)
               ON CONFLICT(id) DO UPDATE SET
                 name=excluded.name,
                 description=excluded.description,
                 story=excluded.story,
                 video_model_family=excluded.video_model_family""",
            (
                PROJECT_ID,
                "Căn Nhà Âm Dương (HẺM Truyện Ma — MC Đình Soạn)",
                "Phim ngắn kinh dị tâm linh dân gian Việt Nam 15 phút (16:9, 15 cảnh × 6 clips × 10s = 90 clips — Google Flow Omni, 80% VO MC Đình Soạn + 20% Lip-Sync).",
                "Bình — sinh viên năm cuối thua lỗ tiền ảo 70 triệu — cùng bố mẹ phải bán nhà phố về quê nội ở nhờ căn nhà ngói ba gian bỏ hoang 10 năm có cây mít cổ thụ đầu cổng. Những bàn tay lạnh buốt lúc nửa đêm dẫn đến bí mật phần mộ ông nội Cụ Xá bị bỏ quên suốt một thập kỷ.",
                "realistic",
                "ACTIVE",
                "PAYGATE_TIER_TWO",
                VIDEO_MODEL_FAMILY,
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
                    "voice_lock": spec.get("voice_lock", ""),
                    "voice_profile": spec.get("voice_profile", ""),
                    "description": f"{spec['description']} | Giọng ({spec.get('voice_lock', '')}): {spec.get('voice_profile', '')}",
                    "ref_prompt": spec["ref_prompt"],
                }
            )
            cid = f"char-cnhadg-{idx:02d}"
            conn.execute(
                """INSERT INTO character (id, name, description, image_prompt, entity_type, media_id)
                   VALUES (?, ?, ?, ?, ?, ?)
                   ON CONFLICT(id) DO UPDATE SET
                     name=excluded.name,
                     description=excluded.description,
                     image_prompt=excluded.image_prompt,
                     media_id=COALESCE(excluded.media_id, character.media_id)""",
                (cid, spec["tag"].lstrip("@"), spec["description"], spec["ref_prompt"], "character", mid or None),
            )
            conn.execute(
                "INSERT OR IGNORE INTO project_character (project_id, character_id) VALUES (?, ?)",
                (PROJECT_ID, cid),
            )

        # Upsert cms_channel for can-nha-am-duong
        conn.execute(
            """INSERT INTO cms_channel
               (slug, name, project_id, aspect_ratio, runner_script, series_dir, ep_prefix, description, characters_json, updated_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
               ON CONFLICT(slug) DO UPDATE SET
                 name=excluded.name,
                 project_id=excluded.project_id,
                 aspect_ratio=excluded.aspect_ratio,
                 runner_script=excluded.runner_script,
                 series_dir=excluded.series_dir,
                 ep_prefix=excluded.ep_prefix,
                 description=excluded.description,
                 characters_json=excluded.characters_json,
                 updated_at=excluded.updated_at""",
            (
                CHANNEL_SLUG,
                "Căn Nhà Âm Dương (15 Phút — 15 Cảnh × 6 Clips | HẺM Truyện Ma — MC Đình Soạn)",
                PROJECT_ID,
                ASPECT_RATIO,
                "runners/can_nha_am_duong.py",
                "can-nha-am-duong",
                "canh",
                "Phim ngắn kinh dị tâm linh dân gian Việt Nam 15 phút (Tác giả: Thu Thảo — Giọng kể chuẩn MC Đình Soạn HẺM Truyện Ma): Bình thua lỗ tiền ảo khiến bố mẹ bán nhà phố về quê nội ở nhờ căn nhà ngói ba gian bỏ hoang 10 năm dưới tán mít cổ thụ âm u (16:9, 15 cảnh × 6 clips × 10s = 90 clips — 80% VO + 20% Lip-Sync).",
                json.dumps(chars_json, ensure_ascii=False),
                now_iso,
            ),
        )

        CURRENT_VIDEO_ID = "video-cnhadg-01"
        conn.execute(
            """INSERT INTO video (id, project_id, title, description, orientation, status)
               VALUES (?, ?, ?, ?, ?, ?)
               ON CONFLICT(id) DO UPDATE SET
                 project_id=excluded.project_id,
                 title=excluded.title,
                 description=excluded.description""",
            (
                CURRENT_VIDEO_ID,
                PROJECT_ID,
                "Căn Nhà Âm Dương (15 Phút — Cảnh 01 - 15 | MC Đình Soạn HẺM Truyện Ma)",
                "Phim ngắn kinh dị tâm linh 15 Cảnh × 6 Clips × 10s = 90 Clips (80% VO MC Đình Soạn + 20% Lip-Sync)",
                "HORIZONTAL",
                "PROCESSING",
            ),
        )

        existing = {
            row[1]: row[0]
            for row in conn.execute("SELECT id, display_order FROM scene WHERE video_id = ?", (CURRENT_VIDEO_ID,)).fetchall()
        }
        order = 0
        for s in range(1, TOTAL_SCENES + 1):
            folder_name = f"canh-{s:02d}"
            ep_id = f"{CHANNEL_SLUG}:ep:{s}"
            conn.execute(
                """INSERT INTO cms_episode
                   (id, channel_slug, project_id, episode_num, folder_name, label, total_clips, rendered_clips, is_complete, updated_at)
                   VALUES (?, ?, ?, ?, ?, ?, 6, 0, 0, ?)
                   ON CONFLICT(id) DO UPDATE SET
                     project_id=excluded.project_id,
                     folder_name=excluded.folder_name,
                     label=excluded.label,
                     total_clips=6,
                     updated_at=excluded.updated_at""",
                (ep_id, CHANNEL_SLUG, PROJECT_ID, s, folder_name, f"Cảnh {s:02d}", now_iso),
            )
            for c in range(1, 7):
                key = f"canh_{s:02d}_clip_{c:02d}"
                fpath = os.path.join(SERIES_DIR, folder_name, f"clip-{c}.md")
                prompt_full = f"Cảnh {s:02d} - Clip {c}"
                if os.path.exists(fpath):
                    with open(fpath, "r", encoding="utf-8") as f:
                        prompt_full = f.read().strip()

                clip_id = f"{CHANNEL_SLUG}:ep:{s}:clip:{c}"
                conn.execute(
                    """INSERT INTO cms_clip
                       (id, channel_slug, project_id, episode_num, folder_name, clip_num, prompt, status, duration_s, updated_at)
                       VALUES (?, ?, ?, ?, ?, ?, ?, 'PENDING', ?, ?)
                       ON CONFLICT(id) DO UPDATE SET
                         project_id=excluded.project_id,
                         prompt=excluded.prompt,
                         duration_s=excluded.duration_s,
                         updated_at=excluded.updated_at""",
                    (clip_id, CHANNEL_SLUG, PROJECT_ID, s, folder_name, c, prompt_full, float(CLIP_DURATION_S), now_iso),
                )

                sid = existing.get(order) or f"sc-cnhadg-{s:02d}-{c:02d}"
                conn.execute(
                    """INSERT INTO scene (id, video_id, display_order, chain_type, duration, prompt, video_prompt, character_names, horizontal_video_status)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'PENDING')
                       ON CONFLICT(id) DO UPDATE SET
                         duration=excluded.duration,
                         prompt=excluded.prompt,
                         video_prompt=excluded.video_prompt""",
                    (
                        sid,
                        CURRENT_VIDEO_ID,
                        order,
                        "ROOT",
                        float(CLIP_DURATION_S),
                        f"Cảnh {s:02d} - Clip {c}",
                        prompt_full,
                        json.dumps(["Binh", "BaPhuong", "OngQuan", "OngBay", "VongCuXa", "VongLa"]),
                    ),
                )
                SCENE_DB_MAP[key] = sid
                order += 1

        conn.commit()
        conn.close()
        log(f"✅ Đã đồng bộ Console DB thành công! ({len(CHARACTER_SPECS)} nhân vật, {TOTAL_SCENES} cảnh & {len(SCENE_DB_MAP)} clips × {CLIP_DURATION_S}s Omni sẵn sàng)")
    except Exception as e:
        log(f"⚠️ Lỗi khi đồng bộ DB Dashboard: {e}")


def update_dashboard_scene_status(scene_num: int, clip_num: int, video_url: str):
    """Cập nhật trạng thái COMPLETED và link video lên Dashboard UI ngay lập tức."""
    key = f"canh_{scene_num:02d}_clip_{clip_num:02d}"
    sid = SCENE_DB_MAP.get(key)
    db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "flow_agent.db")
    try:
        conn = sqlite3.connect(db_path, timeout=30)
        if sid:
            conn.execute(
                "UPDATE scene SET horizontal_video_url = ?, horizontal_video_status = 'COMPLETED' WHERE id = ?",
                (video_url, sid),
            )
            conn.commit()
            log(f"🖥️ [DASHBOARD UI] Đã cập nhật Scene '{key}' thành trạng thái COMPLETED ✅")
        conn.close()
    except Exception as e:
        log(f"⚠️ Lỗi cập nhật Dashboard Scene: {e}")


def sanitize_prompt(prompt: str, attempt: int = 1) -> str:
    return rewrite_prompt_on_failure(prompt, attempt, CHARACTER_SPECS, ASPECT_RATIO)


def extract_last_frame(video_source: str, scene_num: int, clip_num: int) -> str:
    """Trích xuất khung hình cuối cùng của clip bằng ffmpeg làm start frame [Bắt đầu] cho clip kế tiếp."""
    if not video_source:
        return None
    out_frame = os.path.join(FRAMES_DIR, f"canh_{scene_num:02d}_clip_{clip_num:02d}_last.jpg")
    log(f"🎬 Dùng ffmpeg cắt khung hình cuối (Last Frame) của Cảnh {scene_num:02d} - Clip {clip_num:02d}...")
    try:
        cmd = [
            "ffmpeg", "-y",
            "-sseof", "-0.2",
            "-i", video_source,
            "-frames:v", "1",
            "-q:v", "2",
            out_frame,
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
                    ("Mục Đích Sử Dụng", f"Chèn vào slot [Bắt đầu] cho Clip {clip_num + 1:02d} (Seamless Match-On-Action)"),
                ],
            )
            return out_frame
        else:
            cmd_fallback = [
                "ffmpeg", "-y",
                "-ss", "00:00:09.5",
                "-i", video_source,
                "-frames:v", "1",
                "-q:v", "2",
                out_frame,
            ]
            res_fb = subprocess.run(cmd_fallback, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=45)
            if res_fb.returncode == 0 and os.path.exists(out_frame) and os.path.getsize(out_frame) > 0:
                log(f"✨ Trích xuất khung hình cuối thành công (fallback 9.5s): {os.path.basename(out_frame)}")
                return out_frame
            else:
                log(f"⚠️ ffmpeg không trích xuất được frame: {result.stderr.decode('utf-8', errors='ignore')[:200]}")
                return None
    except Exception as e:
        log(f"⚠️ Lỗi khi trích xuất frame cuối: {e}")
        return None


def upload_start_frame(image_path: str) -> str:
    """Tải khung hình cuối vừa cắt lên Google Flow để chèn vào slot [Bắt đầu] (Start Frame) của clip kế tiếp."""
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
            "mime_type": "image/jpeg",
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
                "📤 ĐÃ TẢI ẢNH CUỐI & CHÈN VÀO GOOGLE FLOW [BẮT ĐẦU]",
                [
                    ("Media ID", media_id),
                    ("File Ảnh Nối", os.path.basename(image_path)),
                    ("Slot Kích Hoạt", "Khung hình [Bắt đầu] (Start Frame) cho Clip tiếp theo"),
                    ("Trạng Thái", "Sẵn sàng Image-to-Video Omni Flash 10s (16:9) ✅"),
                ],
            )
            return media_id
        else:
            log(f"⚠️ Upload start frame thất bại (HTTP {res.status_code}): {res.text[:200]}")
            return None
    except Exception as e:
        log(f"⚠️ Ngoại lệ khi upload start frame: {e}")
        return None


def load_previous_last_frame(scene_num: int, prev_clip_num: int) -> str:
    """Lấy (hoặc trích xuất từ video đã có trên máy/R2) khung hình cuối của clip trước và upload lên Google Flow."""
    cached_frame = os.path.join(FRAMES_DIR, f"canh_{scene_num:02d}_clip_{prev_clip_num:02d}_last.jpg")
    if os.path.exists(cached_frame) and os.path.getsize(cached_frame) > 0:
        log(f"🔗 Dùng lại frame cuối đã cắt của Cảnh {scene_num:02d} - Clip {prev_clip_num:02d}: {os.path.basename(cached_frame)}")
        return upload_start_frame(cached_frame)

    for cn, mp4_path in find_episode_clip_mp4s(OUTPUT_VIDEOS_DIR, scene_num, f"canh-{scene_num:02d}"):
        if cn == prev_clip_num and os.path.exists(mp4_path):
            frame_path = extract_last_frame(mp4_path, scene_num, prev_clip_num)
            return upload_start_frame(frame_path) if frame_path else None

    r2_url = is_clip_completed_in_db(CHANNEL_SLUG, scene_num, prev_clip_num)
    if r2_url and str(r2_url).startswith("http"):
        frame_path = extract_last_frame(r2_url, scene_num, prev_clip_num)
        return upload_start_frame(frame_path) if frame_path else None

    return None


def download_and_rename_video(video_url: str, scene_num: int, clip_num: int) -> str:
    """Tải ngay lập tức video 10s (Omni) về máy, cắt ảnh cuối và đồng bộ lên Cloudflare R2 & D1."""
    scene_folder = os.path.join(OUTPUT_VIDEOS_DIR, f"canh-{scene_num:02d}")
    os.makedirs(scene_folder, exist_ok=True)

    filename = f"canh-{scene_num:02d}_clip-{clip_num:02d}.mp4"
    target_path = os.path.join(scene_folder, filename)
    is_overwrite = os.path.exists(target_path)
    tmp_path = f"{target_path}.tmp"

    log("📥 Đang tải video 10s (Google Flow Omni) từ Google Flow về máy...")
    try:
        r = requests.get(video_url, stream=True, timeout=120)
        if r.status_code == 200:
            with open(tmp_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        f.write(chunk)
            os.replace(tmp_path, target_path)
            trim_studio_reference_frames(target_path, log_fn=log)
            frame_path = extract_last_frame(target_path, scene_num, clip_num)
            size_mb = os.path.getsize(target_path) / (1024 * 1024)
            r2_sync = sync_clip_to_r2_and_d1(
                channel_slug=CHANNEL_SLUG,
                ep_num=scene_num,
                clip_num=clip_num,
                local_video_path=target_path,
                last_frame_path=frame_path,
                ep_folder_name=f"canh-{scene_num:02d}",
                project_id=PROJECT_ID,
            )
            box_rows = [
                ("Tên File Clip", filename),
                ("Model & Thời Lượng", f"{VIDEO_MODEL_NAME} ({CLIP_DURATION_S}s)"),
                ("Chế Độ Lưu", "Ghi đè (Overwritten)" if is_overwrite else "Tạo mới"),
                ("Đường Dẫn Lưu", target_path),
                ("Dung Lượng", f"{size_mb:.2f} MB"),
                ("Thời Gian Hoàn Tất", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            ]
            if r2_sync.get("r2_url"):
                box_rows.append(("Cloudflare R2 URL", r2_sync["r2_url"]))
            print_box(
                "💾 CLIP 10S HOÀN THÀNH & ĐÃ GHI ĐÈ VỀ MÁY" if is_overwrite else "💾 CLIP 10S HOÀN THÀNH & ĐÃ TẢI VỀ MÁY",
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


def enforce_narrator_and_voice_lock(prompt: str) -> str:
    """
    Đảm bảo 100% mọi prompt gửi lên Google Flow đều có quy định khóa chặt Giọng Người Dẫn Chuyện
    (VOICE_LOCK_NARRATOR_CNHADG — Nam 42 tuổi chuẩn miền Bắc, phong cách MC Đình Soạn HẺM Truyện Ma, tốc độ 0.95x)
    và giọng thoại nhân vật chuẩn miền Bắc, ngay cả khi prompt được làm mềm (retry).
    """
    p = (prompt or "").strip()
    if NARRATOR_VOICE_SPEC["voice_lock_id"] not in p:
        narrator_block = (
            "\n\n[MANDATORY NARRATOR & VOICE LOCK — STANDARD NORTHERN VIETNAMESE (GIỌNG CHUẨN MIỀN BẮC)]\n"
            f"{NARRATOR_VOICE_SPEC['prompt_directive']}\n"
            f"Strict Voice Rules: {NARRATOR_VOICE_SPEC['strict_rules']}\n"
        )
        p = p + narrator_block
    return p


def submit_clip_with_detailed_log(prompt: str, scene_num: int, clip_num: int, start_image_media_id: str = None):
    key = f"canh_{scene_num:02d}_clip_{clip_num:02d}"
    sid = SCENE_DB_MAP.get(key) or f"scene_{scene_num:02d}_clip_{clip_num:02d}"
    clip_tag = f"[CẢNH {scene_num:02d} - CLIP {clip_num:02d}]"
    enforced_prompt = enforce_narrator_and_voice_lock(prompt)
    flow_prompt = enforced_prompt if enforced_prompt.startswith(clip_tag) else f"{clip_tag}\n{enforced_prompt}"

    ref_media_ids = get_clip_reference_media_ids(enforced_prompt)
    is_vo_clip = "Off-Screen Male Narrator" in enforced_prompt or "VOICE_LOCK_NARRATOR_CNHADG | speaking off-screen" in enforced_prompt
    voice_mode_desc = (
        f"🎙️ VO Người Dẫn Chuyện ({NARRATOR_VOICE_SPEC['voice_lock_id']} — Nam 42t chuẩn Bắc MC Đình Soạn 0.95x, nhân vật khép miệng)"
        if is_vo_clip
        else "🗣️ Nhân Vật Thoại Trực Tiếp (Lip-Sync chuẩn miền Bắc, khớp khẩu hình)"
    )

    if start_image_media_id:
        endpoint = "/api/flow/generate-video"
        mode = "🔗 Image-to-Video (Nối tiếp khung hình cuối Clip trước vào slot [Bắt đầu])"
        slot_desc = f"Start Frame [Bắt đầu] = {start_image_media_id}"
        payload = {
            "start_image_media_id": start_image_media_id,
            "prompt": flow_prompt,
            "project_id": PROJECT_ID,
            "scene_id": sid,
            "duration_s": CLIP_DURATION_S,
            "model_family": VIDEO_MODEL_FAMILY,
            "resolution": "720p",
            "aspect_ratio": ASPECT_RATIO,
        }
    elif ref_media_ids:
        endpoint = "/api/flow/generate-video-omni"
        mode = f"🔒 Ingredients Reference-to-Video (Khóa {len(ref_media_ids)} nhân vật gốc trên Google Flow)"
        slot_desc = f"Ingredients Refs = {', '.join(ref_media_ids)}"
        payload = {
            "reference_media_ids": ref_media_ids,
            "prompt": flow_prompt,
            "project_id": PROJECT_ID,
            "scene_id": sid,
            "duration_s": CLIP_DURATION_S,
            "resolution": "720p",
            "aspect_ratio": ASPECT_RATIO,
        }
    else:
        endpoint = "/api/flow/generate-video-omni-text"
        mode = "🎬 Scene Opening (Text-to-Video Omni 10s)"
        slot_desc = "[Trống - Khởi tạo cảnh gốc]"
        payload = {
            "prompt": flow_prompt,
            "project_id": PROJECT_ID,
            "scene_id": sid,
            "duration_s": CLIP_DURATION_S,
            "resolution": "720p",
            "aspect_ratio": ASPECT_RATIO,
        }

    print_box(
        "📡 FLOWKIT API REQUEST CALL (GOOGLE FLOW OMNI 10S)",
        [
            ("Endpoint API", f"POST {endpoint}"),
            ("Tên Trên Google Flow", clip_tag),
            ("Phân Cảnh", f"Cảnh {scene_num:02d} - Clip {clip_num:02d}"),
            ("Chế Độ Tạo", mode),
            ("Khóa Hình Ảnh / Nhân Vật", slot_desc),
            ("Quy Định Giọng Đọc", voice_mode_desc),
            ("Thời Lượng", f"{CLIP_DURATION_S} giây (Omni Flash 10s)"),
            ("Độ Phân Giải", "720p HD"),
            ("Tỉ Lệ Khung Hình", ASPECT_RATIO),
            ("Model Family", VIDEO_MODEL_FAMILY),
            ("Độ Dài Prompt", f"{len(flow_prompt)} ký tự"),
            ("Prompt Preview", flow_prompt[:120].replace("\n", " ") + "..."),
        ],
    )

    url = f"{FLOWKIT_API}{endpoint}"
    res = requests.post(url, json=payload, timeout=60)
    return res


def poll_generation(submit_res_data: dict, scene_num: int, clip_num: int, timeout_s=360):
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

    poll_mode_desc = (
        "workflows (Text-to-Video)"
        if workflows
        else ("operations (Omni 10s R2V/I2V)" if operations else "direct media")
    )
    log(f"⏳ Đang theo dõi tiến trình tạo video 10s [Cảnh {scene_num:02d} - Clip {clip_num:02d}] (Chế độ: {poll_mode_desc})...")

    last_logged_time = 0
    while time.time() - start_time < timeout_s:
        elapsed = int(time.time() - start_time)
        try:
            if workflows:
                r = requests.post(url, json={"workflows": workflows, "project_id": PROJECT_ID}, timeout=120)
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
                r = requests.post(url, json={"operations": operations, "project_id": PROJECT_ID}, timeout=120)
                if r.status_code == 200:
                    res_data = r.json()
                    inner_ops = res_data.get("operations") or res_data.get("data", {}).get("operations") or []
                    all_done = True
                    has_failed = False
                    video_url = None
                    op_media_id = None

                    for op in inner_ops:
                        op_status = op.get("status", "")
                        op_complaint = op.get("complaint") or ""
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
                        elif elapsed >= 75 and "Media not found" in op_complaint:
                            log(f"⚠️ Sau {elapsed}s job vẫn báo '{op_complaint}' — chuyển sang làm mềm prompt ngay!")
                            has_failed = True
                            all_done = False
                        else:
                            all_done = False

                    if has_failed:
                        log(f"❌ Operation thất bại: {res_data}")
                        return {"success": False, "error": "OPERATION_FAILED"}

                    if all_done and inner_ops:
                        log(f"🎉 Google Flow (Omni 10s) render hoàn tất sau {elapsed}s!")
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
                log(f"   ...Google Flow ({VIDEO_MODEL_NAME} 10s) đang vẽ video ({elapsed}s trôi qua)...")

        except Exception as e:
            log(f"   ...lỗi tạm thời khi poll ({e}), tiếp tục chờ...")

        time.sleep(6)

    log(f"⚠️ Hết thời gian chờ {timeout_s}s (Timeout) khi render Cảnh {scene_num:02d} - Clip {clip_num:02d}.")
    return {"success": False, "error": "TIMEOUT"}


def run_clip_with_auto_retry(scene_num: int, clip_num: int, initial_prompt: str, start_image_media_id: str = None, max_retries: int = 4):
    current_prompt = initial_prompt
    key = f"canh_{scene_num:02d}_clip_{clip_num:02d}"
    sid = SCENE_DB_MAP.get(key)
    ep_folder = f"canh-{scene_num:02d}"

    # Nếu clip đã từng bị đánh dấu FAILED ở lần chạy trước, tự động làm mềm & cập nhật file prompt ngay từ đầu
    sanitize_level = 0
    if is_clip_failed_in_db(CHANNEL_SLUG, scene_num, clip_num):
        sanitize_level = 1
        log(f"🔧 [PHÁT HIỆN CLIP LỖI TRƯỚC ĐÓ] Tự động cập nhật & làm mềm prompt Cảnh {scene_num:02d} - Clip {clip_num:02d} trước khi chạy lại...")
        current_prompt = sanitize_prompt(initial_prompt, sanitize_level)
        persist_updated_prompt(
            series_dir=SERIES_DIR,
            channel_slug=CHANNEL_SLUG,
            ep_num=scene_num,
            clip_num=clip_num,
            new_prompt=current_prompt,
            ep_folder_name=ep_folder,
            project_id=PROJECT_ID,
            scene_db_id=sid,
            attempt=sanitize_level,
            log_fn=log,
        )

    for attempt in range(1, max_retries + 1):
        active_start_id = start_image_media_id if attempt <= 2 else None
        if attempt > 1:
            log(f"🔄 Đang chạy lại Cảnh {scene_num:02d} - Clip {clip_num:02d} với prompt đã cập nhật (Lần {attempt}/{max_retries})...")

        try:
            res = submit_clip_with_detailed_log(current_prompt, scene_num, clip_num, active_start_id)
            cooldown_loops = 0
            while res.status_code != 200 and cooldown_loops < 5:
                if wait_if_cooldown_error(res.text, FLOWKIT_API, log):
                    cooldown_loops += 1
                    res = submit_clip_with_detailed_log(current_prompt, scene_num, clip_num, active_start_id)
                else:
                    break

            if res.status_code == 200:
                data = res.json()
                inner = data.get("data") if isinstance(data.get("data"), dict) else data
                log(f"✅ Google Flow đã chấp nhận job tạo video 10s ({VIDEO_MODEL_NAME}).")

                poll_res = poll_generation(inner, scene_num, clip_num)
                if poll_res["success"] and poll_res.get("video_url"):
                    return poll_res
                else:
                    log(f"⚠️ Không nhận được video URL hoàn chỉnh ở lần thử {attempt}/{max_retries} ({poll_res.get('error')}).")
            else:
                log(f"❌ Google Flow phản hồi lỗi (HTTP {res.status_code}): {res.text}")
        except Exception as e:
            log(f"❌ Lỗi ngoại lệ khi gửi job: {e}")

        if attempt < max_retries:
            sanitize_level += 1
            log(
                f"🔧 [TỰ ĐỘNG CẬP NHẬT PROMPT & CHẠY LẠI - LẦN {attempt + 1}/{max_retries}] "
                f"Đang làm mềm cấp độ {sanitize_level} & lưu lại file canh-{scene_num:02d}/clip-{clip_num}.md..."
            )
            current_prompt = sanitize_prompt(initial_prompt, sanitize_level)
            persist_updated_prompt(
                series_dir=SERIES_DIR,
                channel_slug=CHANNEL_SLUG,
                ep_num=scene_num,
                clip_num=clip_num,
                new_prompt=current_prompt,
                ep_folder_name=ep_folder,
                project_id=PROJECT_ID,
                scene_db_id=sid,
                attempt=sanitize_level,
                log_fn=log,
            )
            time.sleep(5)

    log(f"⏭️ [BỎ QUA SAU {max_retries} LẦN THỬ] Cảnh {scene_num:02d} - Clip {clip_num:02d} đã thử {max_retries} cấp độ prompt — sẽ tự động chạy lại ở cuối cảnh!")
    return {"success": False, "video_url": None}


def run_pipeline(start_scene=1, end_scene=TOTAL_SCENES):
    global CURRENT_EP_NUM, CURRENT_CLIP_NUM
    print("\n" + "=" * 72)
    print("🎬 KHỞI ĐỘNG HỆ THỐNG FLOWKIT — CĂN NHÀ ÂM DƯƠNG (OMNI 10S)")
    print(f"📁 Phạm vi: Cảnh {start_scene:02d} đến Cảnh {end_scene:02d} (6 clips × {CLIP_DURATION_S}s = {6 * CLIP_DURATION_S}s/cảnh)")
    print(f"🤖 Model Video: {VIDEO_MODEL_NAME} (model_family={VIDEO_MODEL_FAMILY}, {CLIP_DURATION_S}s/clip Ingredients R2V)")
    print(f"🔗 Google Flow Project: {PROJECT_ID}")
    print(f"💾 Tải video tự động về: {OUTPUT_VIDEOS_DIR}")
    print("=" * 72 + "\n", flush=True)

    sync_dashboard_database(start_scene, end_scene)

    if os.environ.get("FLOWKIT_SYNC_DB_ONLY") == "1":
        log("✅ Đã hoàn tất chế độ FLOWKIT_SYNC_DB_ONLY=1.")
        return

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
        print(f"👉 BẮT ĐẦU CẢNH {s:02d} (6 Clips × {CLIP_DURATION_S}s — Google Flow Omni 10s)")
        print("#" * 72, flush=True)

        previous_clip_last_frame_media_id = None
        rendered_in_this_run = set()
        scene_dir = os.path.join(SERIES_DIR, f"canh-{s:02d}")

        for c_idx in clip_indices:
            CURRENT_CLIP_NUM = c_idx
            fpath = os.path.join(scene_dir, f"clip-{c_idx}.md")
            if not os.path.exists(fpath):
                continue

            if ONLY_CLIP == 0 and os.environ.get("FLOWKIT_FORCE_RERENDER") != "1":
                r2_done = is_clip_completed_in_db(CHANNEL_SLUG, s, c_idx)
                if r2_done:
                    completed_clips += 1
                    progress_pct = (completed_clips / max(1, total_clips)) * 100
                    log(
                        f"☁️ [{completed_clips}/{total_clips}] ({progress_pct:.1f}%) Cảnh {s:02d} - Clip {c_idx:02d} "
                        f"đã có video trên R2/D1 ({r2_done}) — bỏ qua!"
                    )
                    previous_clip_last_frame_media_id = None
                    continue

            with open(fpath, "r", encoding="utf-8") as f:
                prompt_content = f.read().strip()

            completed_clips += 1
            progress_pct = (completed_clips / max(1, total_clips)) * 100
            print(
                f"\n▶️ TIẾN ĐỘ TỔNG: [{completed_clips}/{total_clips}] ({progress_pct:.1f}%) — "
                f"CẢNH {s:02d} - CLIP {c_idx:02d} [OMNI 10S | {VIDEO_MODEL_NAME}]",
                flush=True,
            )

            # Từ Clip 2 trở đi: tự động lấy/cắt khung hình cuối của Clip trước và chèn vào slot [Bắt đầu]
            if c_idx > 1 and not previous_clip_last_frame_media_id:
                previous_clip_last_frame_media_id = load_previous_last_frame(s, c_idx - 1)

            res = run_clip_with_auto_retry(
                scene_num=s,
                clip_num=c_idx,
                initial_prompt=prompt_content,
                start_image_media_id=previous_clip_last_frame_media_id if c_idx > 1 else None,
            )

            if res["success"] and res.get("video_url"):
                video_url = res["video_url"]
                local_video = download_and_rename_video(video_url, s, c_idx)
                if local_video:
                    rendered_in_this_run.add(c_idx)
                update_dashboard_scene_status(s, c_idx, local_video if local_video else video_url)
                frame_path = os.path.join(FRAMES_DIR, f"canh_{s:02d}_clip_{c_idx:02d}_last.jpg")
                if not os.path.exists(frame_path) or os.path.getsize(frame_path) == 0:
                    frame_path = extract_last_frame(local_video if local_video else video_url, s, c_idx)
                has_next_clip = c_idx != clip_indices[-1]
                previous_clip_last_frame_media_id = (
                    upload_start_frame(frame_path) if frame_path and has_next_clip else None
                )
            else:
                mark_clip_failed_in_db(CHANNEL_SLUG, s, c_idx)
                log(f"⚠️ [Cảnh {s:02d} - Clip {c_idx:02d}] Đã đánh dấu FAILED để retry sau.")
                previous_clip_last_frame_media_id = None

            log("⏳ Nghỉ 5 giây trước khi tiếp tục clip kế tiếp...")
            time.sleep(5)

        existing_nums = (
            rendered_in_this_run
            if ONLY_CLIP > 0
            else (
                {cn for cn, _ in find_episode_clip_mp4s(OUTPUT_VIDEOS_DIR, s, f"canh-{s:02d}")}
                | {c_idx for c_idx in clip_indices if is_clip_completed_in_db(CHANNEL_SLUG, s, c_idx)}
            )
        )
        missing_clips = [
            c_idx
            for c_idx in clip_indices
            if c_idx not in existing_nums and os.path.exists(os.path.join(scene_dir, f"clip-{c_idx}.md"))
        ]
        if missing_clips:
            log(
                f"🔄 [AUTO-UPDATE & RE-RUN CLIP LỖI] Cảnh {s:02d} còn {len(missing_clips)} clip chưa hoàn tất ({missing_clips}) "
                "— tiến hành tự động cập nhật prompt & chạy lại ngay!"
            )
            for m_idx in missing_clips:
                CURRENT_CLIP_NUM = m_idx
                m_fpath = os.path.join(scene_dir, f"clip-{m_idx}.md")
                with open(m_fpath, "r", encoding="utf-8") as mf:
                    m_prompt = mf.read().strip()
                updated_m_prompt = sanitize_prompt(m_prompt, 2)
                persist_updated_prompt(
                    series_dir=SERIES_DIR,
                    channel_slug=CHANNEL_SLUG,
                    ep_num=s,
                    clip_num=m_idx,
                    new_prompt=updated_m_prompt,
                    ep_folder_name=f"canh-{s:02d}",
                    project_id=PROJECT_ID,
                    scene_db_id=SCENE_DB_MAP.get(f"canh_{s:02d}_clip_{m_idx:02d}"),
                    attempt=2,
                    log_fn=log,
                )
                prev_start_id = load_previous_last_frame(s, m_idx - 1) if m_idx > 1 else None
                m_res = run_clip_with_auto_retry(
                    scene_num=s,
                    clip_num=m_idx,
                    initial_prompt=updated_m_prompt,
                    start_image_media_id=prev_start_id,
                    max_retries=3,
                )
                if m_res["success"] and m_res.get("video_url"):
                    v_url = m_res["video_url"]
                    loc_vid = download_and_rename_video(v_url, s, m_idx)
                    if loc_vid:
                        rendered_in_this_run.add(m_idx)
                    update_dashboard_scene_status(s, m_idx, loc_vid if loc_vid else v_url)

        CURRENT_CLIP_NUM = None
        log(f"✅ Đã hoàn tất render các clip 10s của Cảnh {s:02d} (Bỏ qua auto-merge; bấm nút ghép tập trên UI khi cần).")

    print("\n" + "=" * 72)
    print(f"🎉 HOÀN THÀNH TOÀN BỘ CHU TRÌNH TỪ CẢNH {start_scene:02d} ĐẾN CẢNH {end_scene:02d} (GOOGLE FLOW OMNI 10S)!")
    print(f"📁 Video hoàn chỉnh đã được lưu tại: {OUTPUT_VIDEOS_DIR}")
    print("=" * 72 + "\n", flush=True)


if __name__ == "__main__":
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    end = int(sys.argv[2]) if len(sys.argv) > 2 else TOTAL_SCENES
    run_pipeline(start, end)

