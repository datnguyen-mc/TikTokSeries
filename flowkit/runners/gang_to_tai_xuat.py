#!/usr/bin/env python3
"""
HỆ THỐNG TỰ ĐỘNG HÓA FLOWKIT CHO PHIM "GĂNG TƠ TÁI XUẤT" — BẢN 2 (hành động hài phố cổ Hà Nội, 27 CẢNH × 4 CLIPS × 15S = 27 PHÚT):
1. KHÓA NHÂN VẬT CỐ ĐỊNH: tự tạo/lấy & khóa media_id của @Lam, @Mai, @BaHoa, @Khoa, @Hung, @Beo trên Google Flow Project.
2. MỖI CLIP 15 GIÂY VỚI GOOGLE FLOW OMNI 1.2 FLASH (omni_flash, model_version 1.2): 100% clip thoại Lip-Sync do nhân vật nói trên hình (bỏ người dẫn chuyện — yêu cầu 10/11/2026), nhịp giọng nhanh/vừa/chậm theo cảnh;
   prompt sinh từ gang-to-tai-xuat/PHAN_CANH_OMNI.json bằng flowkit/scripts/build_omni_horror_prompts.py.
3. Nối khung cuối clip trước chỉ khi cùng bối cảnh và không có nhân vật mới (FLOWKIT_CHAIN_LAST_FRAME=0 để tắt).
4. Tải video về máy, đồng bộ Cloudflare R2 & D1 và Console Dashboard UI (SQLite flow_agent.db).
Bản 1 (cảng Vạn Hải, Phong Sói) đã lưu ở gang-to-tai-xuat/revisions/ — bị thay vì quá giống ke-song-sot.
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
CHANNEL_SLUG = "gang-to-tai-xuat"
ONLY_CLIP = int(os.environ.get("FLOWKIT_ONLY_CLIP", "0") or "0")

# 👉 PROJECT_ID GOOGLE FLOW CỦA PHIM "GĂNG TƠ TÁI XUẤT"
# Flow Kit không tự tạo project được nữa: tạo 1 project mới trên https://flow.google.com rồi điền UUID vào đây
# (hoặc chạy với biến môi trường GANG_FLOW_PROJECT_ID=<uuid>).
PROJECT_ID = "684cb92f-8e9b-41cc-b5b7-9eefa19ce36f"
DEFAULT_PROJECT_ID = PROJECT_ID
ASPECT_RATIO = "VIDEO_ASPECT_RATIO_LANDSCAPE"

# Nối khung cuối clip trước vào slot [Bắt đầu] (yêu cầu 08/11/2026): chỉ khi clip cùng bối cảnh và không có
# nhân vật mới; clip đổi bối cảnh / có nhân vật mới dùng ảnh nhân vật (Ingredients) để giữ đúng mặt.
# Tắt hẳn nối khung: FLOWKIT_CHAIN_LAST_FRAME=0
CHAIN_LAST_FRAME = os.environ.get("FLOWKIT_CHAIN_LAST_FRAME", "1") == "1"
IMAGE_ASPECT_RATIO = "IMAGE_ASPECT_RATIO_LANDSCAPE"

# 👉 CẤU HÌNH MODEL GOOGLE FLOW OMNI 1.2 FLASH 15 GIÂY
# 09/11/2026: Omni 1.2 Flash ra mắt (clip 3–15s) → mỗi cảnh 4 clip × 15s = 60s, phim giữ nguyên thời lượng.
# Omni 1.1 (abra_*) chỉ có 4/6/8/10s nên runner này luôn gửi model_version "1.2".
VIDEO_MODEL_FAMILY = "omni_flash"
VIDEO_MODEL_NAME = "omni_flash_1.2"
OMNI_MODEL_VERSION = "1.2"
CLIP_DURATION_S = 15
CLIPS_PER_SCENE = 4
TOTAL_SCENES = 27

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SERIES_DIR = os.path.join(WORKSPACE_DIR, "gang-to-tai-xuat")
FRAMES_DIR = os.path.join(SERIES_DIR, "exported_frames")
OUTPUT_VIDEOS_DIR = os.path.join(SERIES_DIR, "output_videos")
CHAR_REFS_DIR = os.path.join(SERIES_DIR, "character_refs")
CHAR_CACHE_FILE = os.path.join(CHAR_REFS_DIR, "character_media_ids.json")

os.makedirs(FRAMES_DIR, exist_ok=True)
os.makedirs(OUTPUT_VIDEOS_DIR, exist_ok=True)
os.makedirs(CHAR_REFS_DIR, exist_ok=True)

# -------------------------------------------------------------
# 🎙️ PHIM 100% THOẠI NHÂN VẬT — KHÔNG CÓ NGƯỜI DẪN CHUYỆN (yêu cầu 10/11/2026)
# Nhịp giọng nhanh / vừa / chậm theo từng lượt thoại nằm sẵn trong prompt ("pace" trong PHAN_CANH_OMNI.json).
# -------------------------------------------------------------
DIALOGUE_VOICE_SPEC = {
    "voice_lock_id": "VOICE_LOCK_DIALOGUE_ONLY_GANG",
    "style_reference": "Không người dẫn chuyện: cả 108 clip chỉ có giọng nhân vật trên hình, giọng Hà Nội; nhịp nhanh / vừa / chậm theo cảnh",
    "prompt_directive": (
        "No narrator and no voice-over: every spoken line comes from the on-screen character with exact lip-sync, "
        "in a standard Hà Nội Northern Vietnamese accent; each character keeps one consistent voice, and the speaking speed "
        "follows the scene: fast in arguments, panic and chases, slow and soft in emotional moments."
    ),
}

# -------------------------------------------------------------
# 🔒 BẢNG ĐỊNH NGHĨA & KHÓA 6 NHÂN VẬT CỐ ĐỊNH CỦA PHIM (GĂNG TƠ TÁI XUẤT — BẢN 2)
# -------------------------------------------------------------
CHARACTER_SPECS = [
    {
        "key": "Lam",
        "tag": "@Lam",
        "aliases": ["@Lam", "Lâm", "Ông Lâm", "Lâm Rồng"],
        "default_media_id": "07af69cb-9869-4965-b6cf-c8c9c975f7aa",
        "voice_lock": "VOICE_LOCK_LAM_GANG",
        "voice_profile": "Fixed 63-year-old native Standard Northern Vietnamese male voice (~105 Hz calm husky low voice), dry humor (giọng ông 63 tuổi chuẩn Hà Nội, trầm khàn, điềm tĩnh, hóm).",
        "description": "Ông Lâm 'Lâm Rồng', 63 tuổi, ông xe ôm hiền lành ở cổng Ô Quan Chưởng, ba mươi năm trước là huyền thoại giang hồ phố cổ; nhỏ người, rắn rỏi, tóc bạc cắt cua, lông mày rậm bạc, mắt trái hơi mờ đục; áo gió kéo khóa xám bạc màu ngoài áo ba lỗ trắng, quần kaki rộng, dép nhựa, mũ cối xanh cũ, hình xăm rồng xanh sẫm trên cẳng tay phải.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @Lam, a 63-year-old Vietnamese man, humble motorbike-taxi driver, 163 cm, wiry and small, short grey crew cut, thick grey eyebrows, calm narrow eyes with a slightly cloudy left eye, deep sun wrinkles, wearing a faded grey zip-up windbreaker with the right sleeve pushed up to show a dark-green dragon tattoo on his forearm, a white tank top underneath, loose khaki trousers, plastic sandals, holding a battered green pith helmet; plain grey studio background, warm soft side light, 8K. Not resembling any real actor."
        ),
    },
    {
        "key": "Mai",
        "tag": "@Mai",
        "aliases": ["@Mai", "Mai", "Bé Mai"],
        "default_media_id": "77d55a1f-b8ee-4e66-b606-bcb19f22f542",
        "voice_lock": "VOICE_LOCK_MAI_GANG",
        "voice_profile": "Fixed 20-year-old native Standard Northern Vietnamese young female voice (~240 Hz clear lively soprano), quick and earnest (giọng nữ 20 tuổi chuẩn Hà Nội, trong, nhanh nhảu).",
        "description": "Mai, 20 tuổi, cháu gái ông Lâm, sinh viên công nghệ thông tin, mắc nợ app vay tiền vì muốn lo tiền mổ mắt cho ông; nhỏ nhắn, tóc bob đen mái thẳng, kính gọng đen tròn; hoodie tím lavender rộng, quần jean đen, giày thể thao trắng đế dày, ba lô đen nhỏ.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @Mai, a 20-year-old Vietnamese female IT student, 155 cm, petite, short black bob with straight bangs, round black-framed glasses, quick bright eyes, wearing an oversized lavender hoodie, black jeans, chunky white sneakers and a small black backpack; plain grey studio background, soft cinematic side light, 8K. Not resembling any real actor."
        ),
    },
    {
        "key": "BaHoa",
        "tag": "@BaHoa",
        "aliases": ["@BaHoa", "Bà Hoa", "Hoa Hổ", "BaHoa"],
        "default_media_id": "a310c641-d8a8-4d31-bccf-21c381b504f8",
        "voice_lock": "VOICE_LOCK_BAHOA_GANG",
        "voice_profile": "Fixed 61-year-old native Northern Vietnamese female voice (~200 Hz bold brassy alto), quick-witted and teasing (giọng bà 61 tuổi chuẩn Hà Nội, sang sảng, đanh đá, hài hước).",
        "description": "Bà Hoa 'Hoa Hổ', 61 tuổi, bộ não của băng ba mươi năm trước, nay là chủ quán bún chả đông nhất phố; đẫy đà, tóc xoăn ngắn nhuộm đỏ mận, mắt sắc, son đỏ, khuyên tai vàng tròn; áo lụa hoa tím, quần ống rộng đen, vòng vàng bản to, dép quai hậu thấp.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @BaHoa, a 61-year-old Vietnamese woman, bún chả shop owner, 155 cm, plump, short curly permed hair dyed burgundy, sharp bright eyes, red lipstick, gold hoop earrings, wearing a purple floral silk blouse, black wide trousers, a chunky gold bangle and low heeled sandals; plain grey studio background, warm soft side light, 8K. Not resembling any real actor."
        ),
    },
    {
        "key": "Khoa",
        "tag": "@Khoa",
        "aliases": ["@Khoa", "Ông Khoa", "Khoa Báo", "Khoa"],
        "default_media_id": "5d8b0ff3-1866-468c-a45f-98fba4674168",
        "voice_lock": "VOICE_LOCK_KHOA_GANG",
        "voice_profile": "Fixed 60-year-old native Standard Northern Vietnamese male voice (~130 Hz nasal wry tenor), deadpan and fussy (giọng ông 60 tuổi chuẩn Hà Nội, giọng mũi, tỉnh bơ).",
        "description": "Ông Khoa 'Khoa Báo', 60 tuổi, phù thủy mở khóa của băng năm xưa, nay sửa đài và điện thoại dưới gầm cầu thang; gầy cao lêu nghêu, hói đỉnh, tóc bạc phía sau buộc túm nhỏ, kính lúp dày đẩy lên trán; gile nâu nhiều túi ngoài sơ mi kẻ ô xanh, quần xám, giày vải.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @Khoa, a 60-year-old Vietnamese man, radio and phone repairman, 172 cm, thin and lanky, bald crown with long grey hair at the back tied in a small ponytail, thick magnifier glasses pushed up on his forehead, wearing a brown multi-pocket vest over a blue checkered shirt, grey trousers and canvas shoes; plain grey studio background, soft cinematic side light, 8K. Not resembling any real actor."
        ),
    },
    {
        "key": "Hung",
        "tag": "@Hung",
        "aliases": ["@Hung", "Hưng", "Hưng Phú Quý"],
        "default_media_id": "36377daf-7efc-4c8a-bfda-7a5e1f8f2d57",
        "voice_lock": "VOICE_LOCK_HUNG_GANG",
        "voice_profile": "Fixed 31-year-old native Standard Northern Vietnamese male voice (~125 Hz loud slick tenor), smug livestream salesman (giọng nam 31 tuổi chuẩn Hà Nội, to, trơn tru, kiêu ngạo).",
        "description": "Hưng 'Phú Quý', 31 tuổi, ông chủ ứng dụng vay tiền và mê livestream khoe khoang; cao gầy, tóc undercut nhuộm vàng tro, kính gọng vàng tròn, nụ cười vênh váo; áo bomber satin đen rộng ngoài áo phông trắng, quần jean đen rách, giày cổ cao trắng, nhiều nhẫn bạc, điện thoại gắn gimbal.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @Hung, a 31-year-old Vietnamese man, flashy loan app boss and livestreamer, 178 cm, tall and slim, dyed ash-blond undercut, round gold-rimmed glasses, cocky grin, wearing an oversized black satin bomber jacket over a plain white T-shirt, ripped black jeans, white high-top sneakers and several silver rings, holding a phone on a small selfie gimbal; plain grey studio background, soft cinematic side light, 8K. Not resembling any real actor."
        ),
    },
    {
        "key": "Beo",
        "tag": "@Beo",
        "aliases": ["@Beo", "Béo", "Béo Đầu Sấm"],
        "default_media_id": "957f67e8-6414-4457-bb0d-f3a266eeb772",
        "voice_lock": "VOICE_LOCK_BEO_GANG",
        "voice_profile": "Fixed 28-year-old native Standard Northern Vietnamese male voice (~95 Hz rough loud bass), blustering (giọng nam 28 tuổi chuẩn Hà Nội, ồm, to, hống hách).",
        "description": "Béo 'Đầu Sấm', 28 tuổi, đầu sỏ đòi nợ thuê của Phú Quý; to béo, đầu cạo trọc có hình tia sét cạo một bên, mắt híp, răng cửa bọc vàng; áo ba lỗ đen, quần soóc rằn ri, dép tông, dây chuyền vàng giả.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @Beo, a 28-year-old Vietnamese man, heavyset debt collector, 175 cm, big round build, shaved head with a lightning-bolt pattern shaved on one side, small eyes, a gold front tooth, wearing a black tank top, camouflage shorts, flip-flops and a cheap fake-gold chain; plain grey studio background, soft cinematic side light, 8K. Not resembling any real actor."
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
    """Đảm bảo 100% sử dụng đúng 6 nhân vật Găng Tơ Tái Xuất (@Lam, @Mai, @BaHoa, @Khoa, @Hung, @Beo) với media_id thực trên Google Flow."""
    global LOCKED_CHARACTER_MEDIA_IDS
    log("🔒 Đang đồng bộ danh sách 6 Nhân vật cố định (@Lam, @Mai, @BaHoa, @Khoa, @Hung, @Beo) trên Google Flow Project...")

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
                    headers={"x-flowkit-caller": f"{CHANNEL_SLUG}:create-char:{tag}"},
                    timeout=90,
                )
                if gen_res.status_code != 200 and wait_if_cooldown_error(gen_res.text, FLOWKIT_API, log):
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
                        headers={"x-flowkit-caller": f"{CHANNEL_SLUG}:create-char:{tag}"},
                        timeout=90,
                    )
                if gen_res.status_code == 200:
                    gdata = gen_res.json()
                    matched_mid = gdata.get("_mediaId") or gdata.get("media_id")
                    if not matched_mid:
                        medias = gdata.get("media") or (gdata.get("data") or {}).get("media") or []
                        if medias and isinstance(medias[0], dict):
                            matched_mid = medias[0].get("name") or medias[0].get("media_id")
                    time.sleep(9)
                else:
                    log(f"⚠️ Tạo ảnh mẫu cho {tag} trả về HTTP {gen_res.status_code}: {gen_res.text[:200]}")
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
    box_items.append(("🎙️ Lời Thoại", f"{DIALOGUE_VOICE_SPEC['voice_lock_id']} — {DIALOGUE_VOICE_SPEC['style_reference']}"))
    for spec in CHARACTER_SPECS:
        tag = spec["tag"]
        mid = LOCKED_CHARACTER_MEDIA_IDS.get(tag, "Chưa có (sẽ tự tạo khi chạy)")
        vlock = spec.get("voice_lock", "")
        box_items.append((f"Nhân Vật {tag}", f"media_id = {mid} | {vlock}"))
    box_items.append(("Model Video", f"{VIDEO_MODEL_NAME} (Google Flow Omni — {CLIP_DURATION_S}s/clip)"))
    box_items.append(("Chế Độ Khóa", f"Ingredients R2V (/api/flow/generate-video-omni {CLIP_DURATION_S}s, Omni {OMNI_MODEL_VERSION})"))
    print_box("🔒 ĐÃ KHÓA 6 NHÂN VẬT, GIỌNG THOẠI & CẤU HÌNH GOOGLE FLOW OMNI 1.2 15S", box_items)


def get_clip_reference_media_ids(prompt: str) -> list:
    """Chỉ lấy đúng media_id của các nhân vật được khai báo đầu dòng trong khối [2. CHARACTER & VOICE LOCK] hoặc [CHARACTERS] của shot hiện tại."""
    if "No named characters and no other people appear in this shot" in (prompt or ""):
        return []
    if "[2. CHARACTER & VOICE LOCK]" in prompt or "[CHARACTERS" in prompt:
        if "[2. CHARACTER & VOICE LOCK]" in prompt:
            char_block = prompt.split("[2. CHARACTER & VOICE LOCK]", 1)[1].split("[3. SCENE & SPATIAL LOCK]", 1)[0]
        else:
            char_block = re.split(r"\n\[[A-Z]", prompt.split("[CHARACTERS", 1)[1], maxsplit=1)[0]
        if "No named characters" in char_block:
            return []
        defined_tags = re.findall(r"^(?:-\s*)?(@[A-Za-z0-9_]+)\s*=", char_block, flags=re.MULTILINE)
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
    """Đồng bộ tức thì cms_channel, cms_episode (27 cảnh), cms_clip (108 clips), project, character, video, scene vào SQLite (flow_agent.db)."""
    global CURRENT_VIDEO_ID, SCENE_DB_MAP
    log("🔄 Đang đồng bộ cơ sở dữ liệu 'Găng Tơ Tái Xuất' với Console Dashboard UI (Google Flow Omni 1.2 15s)...")

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
                "Găng Tơ Tái Xuất (Phim Hành Động Hài 27 Phút)",
                "Phim hành động hài Việt Nam 27 phút, kịch bản gốc bản 2 (16:9, 27 cảnh × 4 clips × 15s = 108 clips — Google Flow Omni 1.2, 100% thoại nhân vật Lip-Sync, nhịp giọng theo cảnh).",
                "Ông Lâm — ông xe ôm hiền lành ở cổng Ô Quan Chưởng — thật ra là Lâm Rồng, huyền thoại phố cổ Hà Nội ba mươi năm trước. Khi cháu gái Mai bị app vay tiền Phú Quý của Hưng siết nợ vì lo tiền mổ mắt cho ông, Lâm Rồng tái xuất cùng Hoa Hổ (bà chủ quán bún chả) và Khoa Báo (thợ sửa đài): một phi vụ lừa ngược kẻ lừa đảo, rượt đuổi qua phố đường tàu, và buổi livestream khiến Hưng tự khai trước năm triệu người xem.",
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
            cid = f"char-gang-{idx:02d}"
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

        # Upsert cms_channel for gang-to-tai-xuat
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
                "Găng Tơ Tái Xuất (Phim Hành Động Hài 27 Phút — 27 Cảnh × 4 Clips × 15s)",
                PROJECT_ID,
                ASPECT_RATIO,
                "runners/gang_to_tai_xuat.py",
                "gang-to-tai-xuat",
                "canh",
                "Phim hành động hài Việt Nam 27 phút, kịch bản gốc bản 2 (16:9, 27 cảnh × 4 clips × 15s = 108 clips — Google Flow Omni 1.2, 100% thoại nhân vật Lip-Sync, nhịp giọng theo cảnh).",
                json.dumps(chars_json, ensure_ascii=False),
                now_iso,
            ),
        )

        CURRENT_VIDEO_ID = "video-gang-01"
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
                "Găng Tơ Tái Xuất (27 Phút — Cảnh 01 - 27)",
                "Phim hành động 27 Cảnh × 4 Clips × 15s = 108 Clips (100% thoại nhân vật Lip-Sync, nhịp giọng theo cảnh)",
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
                   VALUES (?, ?, ?, ?, ?, ?, ?, 0, 0, ?)
                   ON CONFLICT(id) DO UPDATE SET
                     project_id=excluded.project_id,
                     folder_name=excluded.folder_name,
                     label=excluded.label,
                     total_clips=excluded.total_clips,
                     updated_at=excluded.updated_at""",
                (ep_id, CHANNEL_SLUG, PROJECT_ID, s, folder_name, f"Cảnh {s:02d}", CLIPS_PER_SCENE, now_iso),
            )
            for c in range(1, CLIPS_PER_SCENE + 1):
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

                sid = existing.get(order) or f"sc-gang-{s:02d}-{c:02d}"
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
                        json.dumps(["Lam", "Mai", "BaHoa", "Khoa", "Hung", "Beo"]),
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
    # Prompt sinh từ PHAN_CANH_OMNI.json (có [AUDIO], [AVOID] nằm cuối):
    # - Cấp 1 (attempt=1): Làm mềm mô tả hình ảnh tiếng Anh ([TIMELINE], [SETTING], [CHARACTERS]), giữ nguyên câu thoại/lời dẫn tiếng Việt.
    # - Cấp 2 (attempt=2): Làm mềm thêm các từ nhạy cảm trong câu thoại/lời dẫn tiếng Việt nhưng vẫn giữ nguyên cấu trúc [AUDIO] và giọng đọc.
    # - Cấp 3+ (attempt>=3): Làm mềm toàn diện cả [TIMELINE] sang chuyển động điện ảnh an toàn 100% để vượt bộ lọc Google Flow.
    p = prompt or ""
    if "[AUDIO]" in p and "[AVOID]" in p:
        kept = []

        def _hold(m):
            line = m.group(0)
            if attempt >= 2:
                extra_vi = [
                    ("hắt cả xô sơn đỏ", "đổ cả xô sơn đỏ"),
                    ("bắt cả lũ về tội lừa đảo", "mời cả lũ về đồn làm việc"),
                    ("đơn tố cáo lừa đảo", "giấy mời làm việc"),
                    ("hai kẻ lừa đảo", "hai kẻ gian dối"),
                    ("mặt cắt không còn giọt máu", "mặt tái mét"),
                    ("cái thá gì", "là ai"),
                ]
                for k, v in extra_vi:
                    line = line.replace(k, v).replace(k.capitalize(), v.capitalize())
            kept.append(line)
            return f"⟦KEEP{len(kept) - 1}⟧"

        held = re.sub(r"^- (?:Narration|Dialogue|Turn \d+,) .*$", _hold, p, flags=re.MULTILINE)
        held = re.sub(r"burying his face in his (?:shaking|subtle) hands", "resting his forehead thoughtfully on his hand", held, flags=re.IGNORECASE)
        held = re.sub(r"buries his forehead in both (?:shaking|subtle) hands", "rests his forehead in his hands", held, flags=re.IGNORECASE)
        out = rewrite_prompt_on_failure(held, 1, CHARACTER_SPECS, ASPECT_RATIO)
        if attempt >= 3 and "[TIMELINE]" in out and "[AUDIO]" in out:
            tags = re.findall(r"^(?:-\s*)?(@[A-Za-z0-9_]+)\s*=", out, flags=re.MULTILINE)
            lead = tags[0] if tags else "the character"
            safe_timeline = (
                "[TIMELINE]\n"
                "0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.\n"
                "- 0.0–3.0s: Wide atmospheric camera movement establishing the Hà Nội old-quarter setting and lighting with no person in the opening frames.\n"
                f"- 3.0–7.0s: Smooth camera push-in revealing {lead} in the scene with subtle natural movement and an earnest expression.\n"
                + (f"- 7.0–11.0s: {lead} breathes steadily and turns slightly toward the soft light, hands relaxed.\n"
                   f"- 11.0–15.0s: {lead} holds a calm, composed gaze as the camera settles cleanly on the final frame.\n\n"
                   if CLIP_DURATION_S == 15 else
                   f"- 7.0–10.0s: {lead} holds a calm, composed gaze as the camera settles cleanly on the final frame.\n\n")
            )
            out = re.sub(r"\[TIMELINE\][\s\S]*?(?=\[AUDIO\])", safe_timeline, out)
        for i, line in enumerate(kept):
            out = out.replace(f"⟦KEEP{i}⟧", line)
        return out
    return rewrite_prompt_on_failure(prompt, attempt, CHARACTER_SPECS, ASPECT_RATIO)


def clip_uses_start_frame(prompt: str) -> bool:
    """Prompt sinh từ PHAN_CANH_OMNI.json ghi rõ clip nào nối tiếp khung cuối clip trước (Frames)
    và clip nào là cảnh mới / có nhân vật mới (Ingredients — cần ảnh tham chiếu để giữ đúng mặt)."""
    if not CHAIN_LAST_FRAME:
        return False
    p = prompt or ""
    if "[SHOT]" in p:
        return "Continuity: continues the same moment" in p
    return True  # prompt định dạng cũ: giữ hành vi nối khung cũ


def clip_file_uses_start_frame(scene_num: int, clip_num: int) -> bool:
    """Đọc file prompt của một clip và cho biết clip đó có nối khung cuối clip trước không (để chỉ upload khi cần)."""
    p = os.path.join(SERIES_DIR, f"canh-{scene_num:02d}", f"clip-{clip_num}.md")
    try:
        with open(p, "r", encoding="utf-8") as fh:
            return clip_num > 1 and clip_uses_start_frame(fh.read())
    except OSError:
        return False


def clip_is_lipsync(prompt: str) -> bool:
    p = prompt or ""
    return "spoken on camera by" in p or "On-Screen Lip-Sync" in p


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
    if not CHAIN_LAST_FRAME:
        return None
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
                    ("Trạng Thái", f"Sẵn sàng Image-to-Video Omni {OMNI_MODEL_VERSION} Flash {CLIP_DURATION_S}s (16:9) ✅"),
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
    if not CHAIN_LAST_FRAME:
        return None
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


def boost_clip_voice_speed(video_path: str, tempo: float = 1.18) -> bool:
    """Tăng tốc giọng đọc (giữ cao độ & độ dài hình). Bản cũ nối lại đuôi audio gốc nên mấy chữ cuối bị
    đọc lặp (08/11/2026); nay dùng cms_integration.boost_voice_tempo_safe: lấp phần cuối bằng tiếng nền."""
    from cms_integration import boost_voice_tempo_safe
    return boost_voice_tempo_safe(video_path, tempo=tempo, log_fn=log)


def download_and_rename_video(video_url: str, scene_num: int, clip_num: int, boost_voice: bool = True) -> str:
    """Tải ngay lập tức video 15s (Omni 1.2) về máy, tăng tốc nhịp đọc 1.18x, cắt ảnh cuối và đồng bộ lên Cloudflare R2 & D1."""
    scene_folder = os.path.join(OUTPUT_VIDEOS_DIR, f"canh-{scene_num:02d}")
    os.makedirs(scene_folder, exist_ok=True)

    filename = f"canh-{scene_num:02d}_clip-{clip_num:02d}.mp4"
    target_path = os.path.join(scene_folder, filename)
    is_overwrite = os.path.exists(target_path)
    tmp_path = f"{target_path}.tmp"

    log("📥 Đang tải video 15s (Google Flow Omni 1.2) từ Google Flow về máy...")
    try:
        r = requests.get(video_url, stream=True, timeout=120)
        if r.status_code == 200:
            with open(tmp_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        f.write(chunk)
            os.replace(tmp_path, target_path)
            trim_studio_reference_frames(target_path, log_fn=log)
            # Giọng dẫn nhanh như oan-thai-doi-me (yêu cầu 08/11/2026): mặc định tăng tốc 1.18x; đặt FLOWKIT_VOICE_TEMPO=1.0 để tắt.
            voice_tempo = float(os.environ.get("FLOWKIT_VOICE_TEMPO", "1.18") or "1.18")
            if boost_voice:
                boost_clip_voice_speed(target_path, tempo=voice_tempo)
            else:
                log("🗣️ Clip lip-sync: giữ nguyên tốc độ giọng để khớp khẩu hình (bỏ qua atempo).")
            frame_path = extract_last_frame(target_path, scene_num, clip_num)
            size_mb = os.path.getsize(target_path) / (1024 * 1024)
            r2_sync = sync_clip_to_r2_and_d1(
                channel_slug=CHANNEL_SLUG,
                ep_num=scene_num,
                clip_num=clip_num,
                local_video_path=target_path,
                frame_path=frame_path,
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
                "💾 CLIP 15S HOÀN THÀNH & ĐÃ GHI ĐÈ VỀ MÁY" if is_overwrite else "💾 CLIP 15S HOÀN THÀNH & ĐÃ TẢI VỀ MÁY",
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


def enforce_dialogue_voice_lock(prompt: str) -> str:
    """Prompt sinh từ PHAN_CANH_OMNI.json luôn có [AUDIO]; nếu bản làm mềm (retry) lỡ mất khối đó thì chỉ chèn lại
    luật thoại nhân vật — phim này không có người dẫn chuyện."""
    p = (prompt or "").strip()
    if "[AUDIO]" not in p and DIALOGUE_VOICE_SPEC["voice_lock_id"] not in p:
        p += f"\n\n[VOICE LOCK — DIALOGUE ONLY ({DIALOGUE_VOICE_SPEC['voice_lock_id']})]\n{DIALOGUE_VOICE_SPEC['prompt_directive']}\n"
    return p


def ensure_no_char_in_opening_beat(prompt: str) -> str:
    """
    Quy tắc bắt buộc (08/11/2026):
    Nếu clip KHÔNG có hình frame cuối từ clip trước (start_image_media_id is None, tức dùng Ingredients R2V hoặc Text-to-Video),
    tuyệt đối KHÔNG quy định @NhânVật ở Beat 1 (0.0–3.0s) để tránh Google Flow Omni dán ảnh thẻ studio của nhân vật vào đầu clip.
    Beat 1 (0.0–3.0s) chỉ mô tả bối cảnh/ánh sáng/chuyển động máy quay, và chuyển hành động nhân vật sang Beat 2 (3.0–7.0s).
    """
    p = prompt or ""
    m_b1 = re.search(r"^(- 0\.0[–-]3\.0s:\s*)(.+)$", p, flags=re.MULTILINE)
    m_b2 = re.search(r"^(- 3\.0[–-]7\.0s:\s*)(.+)$", p, flags=re.MULTILINE)
    if not m_b1 or not m_b2:
        return p
    b1_text = m_b1.group(2).strip()
    b2_text = m_b2.group(2).strip()
    if not re.search(r"@[A-Za-z0-9_]+", b1_text):
        return p
    loc_match = re.search(r"\[LOCATION\]\s*\n([^\n]+)", p)
    loc_desc = loc_match.group(1).strip().rstrip(".") if loc_match else "the sunny Hà Nội old-quarter setting"
    new_b1 = f"Atmospheric establishing view of {loc_desc}, camera moving smoothly through the environment and light with no person in the opening frames."
    combined_b2 = f"{b1_text.rstrip('.')} — then {b2_text[0].lower() + b2_text[1:] if len(b2_text) > 1 and not b2_text.startswith('@') else b2_text}"
    p = p[:m_b1.start()] + m_b1.group(1) + new_b1 + p[m_b1.end():]
    m_b2_new = re.search(r"^(- 3\.0[–-]7\.0s:\s*)(.+)$", p, flags=re.MULTILINE)
    if m_b2_new:
        p = p[:m_b2_new.start()] + m_b2_new.group(1) + combined_b2 + p[m_b2_new.end():]
    p = p.replace(
        "clothing stays fully worn from the first frame.",
        "0.0–3.0s shows the environment and props only with no character on screen, and characters enter from 3.0s onward with clothing fully worn.",
    )
    return p


def submit_clip_with_detailed_log(prompt: str, scene_num: int, clip_num: int, start_image_media_id: str = None):
    if not CHAIN_LAST_FRAME:
        start_image_media_id = None
    key = f"canh_{scene_num:02d}_clip_{clip_num:02d}"
    sid = SCENE_DB_MAP.get(key) or f"scene_{scene_num:02d}_clip_{clip_num:02d}"
    clip_tag = f"[CẢNH {scene_num:02d} - CLIP {clip_num:02d}]"
    enforced_prompt = enforce_dialogue_voice_lock(prompt)
    if not start_image_media_id:
        enforced_prompt = ensure_no_char_in_opening_beat(enforced_prompt)
    # Không chèn nhãn "[CẢNH xx - CLIP yy]" vào đầu prompt: chữ ở dòng đầu dễ bị Omni vẽ thành title card.
    # Tên clip trên Flow vẫn được đặt lại sau khi render xong bằng force_rename_clip_on_flow().
    flow_prompt = enforced_prompt

    ref_media_ids = get_clip_reference_media_ids(enforced_prompt)
    voice_mode_desc = "🗣️ Nhân Vật Thoại Trực Tiếp (Lip-Sync giọng Hà Nội, nhịp nhanh/vừa/chậm theo cảnh, không người dẫn chuyện)"

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
            "model_version": OMNI_MODEL_VERSION,
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
            "model_version": OMNI_MODEL_VERSION,
            "resolution": "720p",
            "aspect_ratio": ASPECT_RATIO,
        }
    else:
        endpoint = "/api/flow/generate-video-omni-text"
        mode = f"🎬 Scene Opening (Text-to-Video Omni {OMNI_MODEL_VERSION} {CLIP_DURATION_S}s)"
        slot_desc = "[Trống - Khởi tạo cảnh gốc]"
        payload = {
            "prompt": flow_prompt,
            "project_id": PROJECT_ID,
            "scene_id": sid,
            "duration_s": CLIP_DURATION_S,
            "model_version": OMNI_MODEL_VERSION,
            "resolution": "720p",
            "aspect_ratio": ASPECT_RATIO,
        }

    print_box(
        "📡 FLOWKIT API REQUEST CALL (GOOGLE FLOW OMNI 1.2 15S)",
        [
            ("Endpoint API", f"POST {endpoint}"),
            ("Tên Trên Google Flow", clip_tag),
            ("Phân Cảnh", f"Cảnh {scene_num:02d} - Clip {clip_num:02d}"),
            ("Chế Độ Tạo", mode),
            ("Khóa Hình Ảnh / Nhân Vật", slot_desc),
            ("Quy Định Giọng Đọc", voice_mode_desc),
            ("Thời Lượng", f"{CLIP_DURATION_S} giây (Omni {OMNI_MODEL_VERSION} Flash)"),
            ("Độ Phân Giải", "720p HD"),
            ("Tỉ Lệ Khung Hình", ASPECT_RATIO),
            ("Model Family", VIDEO_MODEL_FAMILY),
            ("Độ Dài Prompt", f"{len(flow_prompt)} ký tự"),
            ("Prompt Preview", flow_prompt[:120].replace("\n", " ") + "..."),
        ],
    )

    url = f"{FLOWKIT_API}{endpoint}"
    headers = {"x-flowkit-caller": f"{CHANNEL_SLUG}:canh-{scene_num:02d}_clip-{clip_num:02d}"}
    res = requests.post(url, json=payload, headers=headers, timeout=60)
    return res


def poll_generation(submit_res_data: dict, scene_num: int, clip_num: int, timeout_s=15 * CLIP_DURATION_S):
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
        else (f"operations (Omni {OMNI_MODEL_VERSION} {CLIP_DURATION_S}s R2V/I2V)" if operations else "direct media")
    )
    log(f"⏳ Đang theo dõi tiến trình tạo video {CLIP_DURATION_S}s [Cảnh {scene_num:02d} - Clip {clip_num:02d}] (Chế độ: {poll_mode_desc})...")

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
                        elif op_complaint and "media not found" not in op_complaint.lower() and elapsed >= 65 and not (op.get("operation", {}).get("metadata", {}).get("video", {}).get("mediaId")):
                            # "Media not found." is reported while a 15s Omni render is still running (and by finished jobs too,
                            # see flowkit/CLAUDE.md); aborting at 65s threw away clips that needed ~90s (10/11/2026).
                            log(f"⚠️ Google Flow từ chối/báo lỗi sau {elapsed}s ({op_complaint}) — kết thúc poll sớm để làm mềm prompt & chạy lại!")
                            has_failed = True
                            all_done = False
                        else:
                            all_done = False

                    if has_failed:
                        log(f"❌ Operation thất bại: {res_data}")
                        return {"success": False, "error": "OPERATION_FAILED"}

                    if all_done and inner_ops:
                        log(f"🎉 Google Flow (Omni {OMNI_MODEL_VERSION} {CLIP_DURATION_S}s) render hoàn tất sau {elapsed}s!")
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
                log(f"   ...Google Flow ({VIDEO_MODEL_NAME} {CLIP_DURATION_S}s) đang vẽ video ({elapsed}s trôi qua)...")

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
                log(f"✅ Google Flow đã chấp nhận job tạo video {CLIP_DURATION_S}s ({VIDEO_MODEL_NAME}).")

                poll_res = poll_generation(inner, scene_num, clip_num)
                if poll_res["success"] and poll_res.get("video_url"):
                    return poll_res
                else:
                    log(f"⚠️ Không nhận được video URL hoàn chỉnh ở lần thử {attempt}/{max_retries} ({poll_res.get('error')}).")
                    if poll_res.get("error") == "TIMEOUT" and attempt < max_retries:
                        # 10/11/2026: Flow nhận job rồi không tạo gì (giới hạn lượt theo giờ) — không phải lỗi nội dung,
                        # nên giữ nguyên prompt, chờ dần 3 → 15 phút rồi gửi lại thay vì làm mềm prompt và gửi dồn.
                        wait_s = min(900, 180 * attempt)
                        log(f"⏸️ Flow không trả video (có thể đang giới hạn lượt) — chờ {wait_s // 60} phút rồi gửi lại nguyên prompt.")
                        time.sleep(wait_s)
                        continue
            else:
                log(f"❌ Google Flow phản hồi lỗi (HTTP {res.status_code}): {res.text}")
                if "CAPTCHA_FAILED" in (res.text or ""):
                    log("🛑 [CAPTCHA_FAILED] Tab Google Flow trên trình duyệt cần được người dùng kiểm tra/tải lại (không sửa file prompt).")
                    return {"success": False, "video_url": None, "error": "CAPTCHA_FAILED"}
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
    print("🎬 KHỞI ĐỘNG HỆ THỐNG FLOWKIT — GĂNG TƠ TÁI XUẤT (OMNI 1.2 15S)")
    print(f"📁 Phạm vi: Cảnh {start_scene:02d} đến Cảnh {end_scene:02d} ({CLIPS_PER_SCENE} clips × {CLIP_DURATION_S}s = {CLIPS_PER_SCENE * CLIP_DURATION_S}s/cảnh)")
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

    clip_indices = [ONLY_CLIP] if ONLY_CLIP > 0 else list(range(1, CLIPS_PER_SCENE + 1))
    total_clips = (end_scene - start_scene + 1) * len(clip_indices)
    completed_clips = 0

    for s in range(start_scene, end_scene + 1):
        CURRENT_EP_NUM = s
        print("\n" + "#" * 72)
        print(f"👉 BẮT ĐẦU CẢNH {s:02d} ({CLIPS_PER_SCENE} Clips × {CLIP_DURATION_S}s — Google Flow Omni {OMNI_MODEL_VERSION})")
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
                f"CẢNH {s:02d} - CLIP {c_idx:02d} [OMNI {CLIP_DURATION_S}S | {VIDEO_MODEL_NAME}]",
                flush=True,
            )

            # Từ Clip 2 trở đi: tự động lấy/cắt khung hình cuối của Clip trước và chèn vào slot [Bắt đầu]
            use_start_frame = c_idx > 1 and clip_uses_start_frame(prompt_content)
            if use_start_frame and not previous_clip_last_frame_media_id:
                previous_clip_last_frame_media_id = load_previous_last_frame(s, c_idx - 1)
            if c_idx > 1 and not use_start_frame:
                log("🎬 Cảnh mới / nhân vật mới → dùng ảnh nhân vật (Ingredients), không nối khung cuối clip trước.")

            res = run_clip_with_auto_retry(
                scene_num=s,
                clip_num=c_idx,
                initial_prompt=prompt_content,
                start_image_media_id=previous_clip_last_frame_media_id if use_start_frame else None,
            )

            if res["success"] and res.get("video_url"):
                video_url = res["video_url"]
                local_video = download_and_rename_video(video_url, s, c_idx, boost_voice=not clip_is_lipsync(prompt_content))
                if local_video:
                    rendered_in_this_run.add(c_idx)
                update_dashboard_scene_status(s, c_idx, local_video if local_video else video_url)
                frame_path = os.path.join(FRAMES_DIR, f"canh_{s:02d}_clip_{c_idx:02d}_last.jpg")
                if not os.path.exists(frame_path) or os.path.getsize(frame_path) == 0:
                    frame_path = extract_last_frame(local_video if local_video else video_url, s, c_idx)
                has_next_clip = c_idx != clip_indices[-1]
                previous_clip_last_frame_media_id = (
                    upload_start_frame(frame_path)
                    if frame_path and has_next_clip and clip_file_uses_start_frame(s, c_idx + 1)
                    else None
                )
            elif res.get("error") == "CAPTCHA_FAILED":
                log("🛑 Tạm dừng pipeline do tab Google Flow báo lỗi CAPTCHA_FAILED. Sau khi tải lại tab Google Flow trên Chrome, hãy bấm Chạy tiếp!")
                return
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
                prev_start_id = (
                    load_previous_last_frame(s, m_idx - 1)
                    if (m_idx > 1 and clip_uses_start_frame(updated_m_prompt))
                    else None
                )
                m_res = run_clip_with_auto_retry(
                    scene_num=s,
                    clip_num=m_idx,
                    initial_prompt=updated_m_prompt,
                    start_image_media_id=prev_start_id,
                    max_retries=3,
                )
                if m_res["success"] and m_res.get("video_url"):
                    v_url = m_res["video_url"]
                    loc_vid = download_and_rename_video(v_url, s, m_idx, boost_voice=not clip_is_lipsync(updated_m_prompt))
                    if loc_vid:
                        rendered_in_this_run.add(m_idx)
                    update_dashboard_scene_status(s, m_idx, loc_vid if loc_vid else v_url)

        CURRENT_CLIP_NUM = None
        log(f"✅ Đã hoàn tất render các clip {CLIP_DURATION_S}s của Cảnh {s:02d} (Bỏ qua auto-merge; bấm nút ghép tập trên UI khi cần).")

    # 🔄 VÒNG QUÉT TỔNG KIỂM TRA & TỰ ĐỘNG CHẠY LẠI MỌI CLIP LỖI / THIẾU TRÊN TOÀN BỘ CÁC CẢNH (AUTO-HEAL SWEEP)
    for sweep_round in range(1, 3):
        all_failed_or_missing = []
        for s in range(start_scene, end_scene + 1):
            scene_dir = os.path.join(SERIES_DIR, f"canh-{s:02d}")
            done_mp4s = {cn for cn, _ in find_episode_clip_mp4s(OUTPUT_VIDEOS_DIR, s, f"canh-{s:02d}")}
            for c_idx in clip_indices:
                fpath = os.path.join(scene_dir, f"clip-{c_idx}.md")
                if not os.path.exists(fpath):
                    continue
                if c_idx not in done_mp4s and not is_clip_completed_in_db(CHANNEL_SLUG, s, c_idx):
                    all_failed_or_missing.append((s, c_idx, fpath))

        if not all_failed_or_missing:
            log(f"✅ [KIỂM TRA HOÀN TẤT - VÒNG {sweep_round}] Toàn bộ 100% các clip từ Cảnh {start_scene:02d} đến Cảnh {end_scene:02d} đều đã COMPLETED (0 clip lỗi)!")
            break

        log(
            f"🔄 [AUTO-HEAL SWEEP #{sweep_round}] Phát hiện {len(all_failed_or_missing)} clip bị lỗi/thiếu "
            f"({[(s, c) for s, c, _ in all_failed_or_missing]}) — tự động làm mềm prompt & chạy lại ngay!"
        )
        for s, c_idx, m_fpath in all_failed_or_missing:
            CURRENT_EP_NUM = s
            CURRENT_CLIP_NUM = c_idx
            with open(m_fpath, "r", encoding="utf-8") as mf:
                m_prompt = mf.read().strip()
            updated_m_prompt = sanitize_prompt(m_prompt, sweep_round + 1)
            persist_updated_prompt(
                series_dir=SERIES_DIR,
                channel_slug=CHANNEL_SLUG,
                ep_num=s,
                clip_num=c_idx,
                new_prompt=updated_m_prompt,
                ep_folder_name=f"canh-{s:02d}",
                project_id=PROJECT_ID,
                scene_db_id=SCENE_DB_MAP.get(f"canh_{s:02d}_clip_{c_idx:02d}"),
                attempt=sweep_round + 1,
                log_fn=log,
            )
            prev_start_id = (
                load_previous_last_frame(s, c_idx - 1)
                if (c_idx > 1 and clip_uses_start_frame(updated_m_prompt))
                else None
            )
            m_res = run_clip_with_auto_retry(
                scene_num=s,
                clip_num=c_idx,
                initial_prompt=updated_m_prompt,
                start_image_media_id=prev_start_id,
                max_retries=3,
            )
            if m_res["success"] and m_res.get("video_url"):
                v_url = m_res["video_url"]
                loc_vid = download_and_rename_video(v_url, s, c_idx, boost_voice=not clip_is_lipsync(updated_m_prompt))
                update_dashboard_scene_status(s, c_idx, loc_vid if loc_vid else v_url)
            time.sleep(5)

    print("\n" + "=" * 72)
    print(f"🎉 HOÀN THÀNH TOÀN BỘ CHU TRÌNH TỪ CẢNH {start_scene:02d} ĐẾN CẢNH {end_scene:02d} (GOOGLE FLOW OMNI 1.2 15S)!")
    print(f"📁 Video hoàn chỉnh đã được lưu tại: {OUTPUT_VIDEOS_DIR}")
    print("=" * 72 + "\n", flush=True)


if __name__ == "__main__":
    if not _is_valid_media_id(PROJECT_ID):
        print("❌ Chưa có PROJECT_ID cho Găng Tơ Tái Xuất. Tạo 1 project mới trên https://flow.google.com, rồi chạy:\n"
              "   GANG_FLOW_PROJECT_ID=<uuid-project> python flowkit/runners/gang_to_tai_xuat.py 1 27\n"
              "(hoặc điền UUID vào PROJECT_ID trong flowkit/runners/gang_to_tai_xuat.py)", flush=True)
        sys.exit(2)
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    end = int(sys.argv[2]) if len(sys.argv) > 2 else TOTAL_SCENES
    run_pipeline(start, end)

