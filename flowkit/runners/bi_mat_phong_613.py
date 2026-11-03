#!/usr/bin/env python3
"""
HỆ THỐNG TỰ ĐỘNG HÓA FLOWKIT NÂNG CAO CHO "BÍ MẬT PHÒNG 613: LỜI CẢNH BÁO ĐÊM RẰM":
1. KHÓA NHÂN VẬT CỐ ĐỊNH (CHARACTER LOCK): Tự động lấy & khóa chính xác media_id của @Phuong, @Trinh, @BacBaoVe, @BongAoTrang từ Google Flow Project.
2. MỖI CLIP 8 GIÂY (8.0s) VỚI MODEL VEO-LITE (veo_3_1_i2v_lite, model_family="veo"):
   - Clip 1 (Mở cảnh): Tạo Start Frame 16:9 khóa nhân vật (@Phuong, @Trinh, @BacBaoVe, @BongAoTrang) rồi render 8s bằng model veo_3_1_i2v_lite.
   - Clip 2..6 (EXTEND VIDEO 8s): Tự động trích xuất khung hình cuối (last frame 8.0s) của clip trước, upload làm Start Frame và render nối tiếp 8s bằng model veo_3_1_i2v_lite (Seamless Video Extend).
3. Tự động đặt tên clip trên Google Flow theo cảnh ([CẢNH XX - CLIP YY]) và tải ngay về máy + đồng bộ Cloudflare R2 & D1 khi hoàn thành.
4. Tự động đồng bộ thời gian thực với Console Dashboard UI.
"""

import os
import re
import sys
import time
import json
import base64
import subprocess
import requests
from datetime import datetime

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
    is_clip_completed_in_db,
    mark_clip_failed_in_db,
    trim_studio_reference_frames,
    probe_clip_streams,
)

FLOWKIT_API = "http://127.0.0.1:8200"
CHANNEL_SLUG = "bi-mat-phong-613"
ONLY_CLIP = int(os.environ.get("FLOWKIT_ONLY_CLIP", "0") or "0")

# 👉 PROJECT_ID GOOGLE FLOW CỦA SERIES "BÍ MẬT PHÒNG 613"
PROJECT_ID = "daf9939b-35f2-4d6c-a299-8efcabc3fc9a"
DEFAULT_PROJECT_ID = "daf9939b-35f2-4d6c-a299-8efcabc3fc9a"
ASPECT_RATIO = "VIDEO_ASPECT_RATIO_LANDSCAPE"
IMAGE_ASPECT_RATIO = "IMAGE_ASPECT_RATIO_LANDSCAPE"

# 👉 CẤU HÌNH MODEL VEO-LITE 8 GIÂY + EXTEND VIDEO
VIDEO_MODEL_FAMILY = "veo"
VIDEO_MODEL_NAME = "veo_3_1_i2v_lite"
CLIP_DURATION_S = 8

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SERIES_DIR = os.path.join(WORKSPACE_DIR, "bi-mat-phong-613")
FRAMES_DIR = os.path.join(SERIES_DIR, "exported_frames")
OUTPUT_VIDEOS_DIR = os.path.join(SERIES_DIR, "output_videos")
CHAR_REFS_DIR = os.path.join(SERIES_DIR, "character_refs")
CHAR_CACHE_FILE = os.path.join(CHAR_REFS_DIR, "character_media_ids.json")

os.makedirs(FRAMES_DIR, exist_ok=True)
os.makedirs(OUTPUT_VIDEOS_DIR, exist_ok=True)
os.makedirs(CHAR_REFS_DIR, exist_ok=True)

# -------------------------------------------------------------
# 🔒 BẢNG ĐỊNH NGHĨA & KHÓA NHÂN VẬT CỐ ĐỊNH CỦA SERIES (BÍ MẬT PHÒNG 613)
# -------------------------------------------------------------
CHARACTER_SPECS = [
    {
        "key": "Phuong",
        "tag": "@Phuong",
        "aliases": ["@Phuong", "@Phương", "Phương", "Phuong"],
        "default_media_id": "613a0001-f101-4613-a613-000000000001",
        "description": "Nữ sinh viên 22 tuổi dịu dàng, nhạy cảm tâm linh; cao 160 cm, gương mặt trái xoan thanh tú, đôi mắt to biểu cảm, cài băng đô vải màu kem trên mái tóc đen dài xõa tự nhiên, mặc áo cardigan len mỏng màu kem khoác ngoài áo thun trắng và quần jean ống rộng xanh nhạt.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @Phuong, a 22-year-old Vietnamese female university student, 160 cm, "
            "slender petite build, gentle oval face, large expressive dark eyes, long straight black hair worn down with a neat cream "
            "fabric headband, wearing a soft cream knit cardigan over a plain white cotton T-shirt, light-blue wide-leg jeans, and white "
            "canvas sneakers; plain grey studio background, soft cinematic side light, 8K. Not resembling any real actor."
        ),
    },
    {
        "key": "Trinh",
        "tag": "@Trinh",
        "aliases": ["@Trinh", "Trinh"],
        "default_media_id": "613a0002-f102-4613-a613-000000000002",
        "description": "Bạn thân cùng phòng của Phương, 22 tuổi, sinh viên Báo chí cá tính, thực tế; cao 165 cm, dáng thon khỏe, gương mặt sắc sảo, tóc đen dài thẳng rẽ ngôi giữa, mặc áo thun form rộng màu cam đất (burnt orange) và quần jogger xám đậm.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @Trinh, a 22-year-old Vietnamese female student, 165 cm, lean athletic build, "
            "sharp confident facial features, attentive dark eyes, long straight black hair parted in the middle, wearing an oversized "
            "burnt-orange cotton T-shirt, dark charcoal-grey jogger trousers, and dark slides; plain grey studio background, soft cinematic "
            "side light, 8K. Not resembling any real actor."
        ),
    },
    {
        "key": "BacBaoVe",
        "tag": "@BacBaoVe",
        "aliases": ["@BacBaoVe", "Ông Bảy Bảo Vệ", "Ông Bảy", "BacBaoVe"],
        "default_media_id": "613a0003-f103-4613-a613-000000000003",
        "description": "Bảo vệ trực đêm chung cư cũ Lô C, 58 tuổi; cao 168 cm, dáng hơi gù, tóc cắt ngắn điểm bạc, gương mặt gầy góc cạnh lạnh lùng, vết sẹo bỏng mờ bên cổ trái, mặc đồng phục bảo vệ xanh đen sẫm, cầm chùm chìa khóa đồng cũ và đèn pin vỏ sắt.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @BacBaoVe, a 58-year-old Vietnamese night-shift security guard, 168 cm, "
            "thin slightly stooped build, short grey-streaked black hair, gaunt angular weathered face, cold watchful eyes, a faint old burn "
            "scar on the left side of his neck, wearing a dark navy-black short-sleeve security guard uniform shirt with shoulder epaulettes, "
            "dark trousers, worn black shoes, holding an old brass key ring in one hand and a heavy metal flashlight in the other; plain grey "
            "studio background, hard side light, 8K. Not resembling any real actor."
        ),
    },
    {
        "key": "BongAoTrang",
        "tag": "@BongAoTrang",
        "aliases": ["@BongAoTrang", "Linh", "Cô Gái Áo Trắng", "BongAoTrang"],
        "default_media_id": "613a0004-f104-4613-a613-000000000004",
        "description": "Nữ sinh viên nhạc viện từng thuê phòng 613 năm 2016; cao 162 cm, dáng mảnh mai, làn da trắng xanh tĩnh lặng, tóc đen dài xõa ngang lưng, mặc đầm vải voan trắng dài tay cổ vuông cổ điển, cổ tay phải đeo vòng chỉ đỏ gắn chuông bạc nhỏ, ánh mắt u buồn khẩn thiết.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @BongAoTrang, a 21-year-old Vietnamese woman, 162 cm, slender delicate build, "
            "pale porcelain skin with natural realistic texture, sorrowful expressive dark eyes, long straight black hair resting over her "
            "shoulders, wearing a clean vintage ankle-length off-white long-sleeve square-neck cotton dress, barefoot, with a thin red thread "
            "bracelet and tiny silver bell on her right wrist; plain grey studio background, cool moonlight side light, 8K. Clean cinematic "
            "appearance, no gore, no blood. Not resembling any real actor."
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
def load_and_lock_project_characters():
    """Đảm bảo 100% sử dụng đúng nhân vật Bí Mật Phòng 613 (@Phuong, @Trinh, @BacBaoVe, @BongAoTrang)."""
    global LOCKED_CHARACTER_MEDIA_IDS
    log("🔒 Đang kiểm tra và khóa bộ nhân vật cố định (@Phuong, @Trinh, @BacBaoVe, @BongAoTrang) trên Google Flow...")

    cached_by_project = {}
    if os.path.exists(CHAR_CACHE_FILE):
        try:
            with open(CHAR_CACHE_FILE, "r", encoding="utf-8") as f:
                cached_by_project = json.load(f)
        except Exception:
            cached_by_project = {}

    project_cache = cached_by_project.get(PROJECT_ID, {}) if isinstance(cached_by_project, dict) else {}

    remote_chars = []
    try:
        r = requests.get(f"{FLOWKIT_API}/api/flow/project-characters", params={"project_id": PROJECT_ID}, timeout=30)
        if r.status_code == 200:
            remote_chars = r.json().get("characters") or []
    except Exception as e:
        log(f"⚠️ Không truy vấn được danh sách nhân vật từ Google Flow (sẽ dùng ID khóa sẵn): {e}")

    locked = {}
    for spec in CHARACTER_SPECS:
        tag = spec["tag"]
        aliases_lower = {a.lower().lstrip("@") for a in spec["aliases"]}
        matched_mid = None

        for rc in remote_chars:
            rc_name = (rc.get("name") or "").strip().lower().lstrip("@")
            if rc_name in aliases_lower and rc.get("media_id"):
                matched_mid = rc["media_id"]
                break

        if not matched_mid and project_cache.get(tag):
            matched_mid = project_cache[tag]

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

        if not matched_mid and spec.get("default_media_id"):
            matched_mid = spec["default_media_id"]

        if matched_mid:
            locked[tag] = matched_mid

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
    for spec in CHARACTER_SPECS:
        tag = spec["tag"]
        mid = LOCKED_CHARACTER_MEDIA_IDS.get(tag, "Chưa có")
        box_items.append((f"Nhân Vật {tag}", f"media_id = {mid}"))
    box_items.append(("Model Video", f"{VIDEO_MODEL_NAME} (Veo 3.1 Lite — {CLIP_DURATION_S}s/clip)"))
    box_items.append(("Chế Độ Nối Cảnh", "Clip 1 Start-Frame Lock + Clip 2..6 Video Extend 8s"))
    print_box("🔒 ĐÃ KHÓA NHÂN VẬT & CẤU HÌNH VEO-LITE 8S + EXTEND VIDEO", box_items)


def is_new_scene_clip(prompt: str, clip_num: int, start_image_media_id: str = None) -> bool:
    """Clip 1 mở cảnh mới; từ Clip 2 đến Clip 6 luôn Extend Video (nối tiếp từ frame cuối của clip trước)."""
    return clip_num == 1 or not start_image_media_id


def get_clip_reference_media_ids(prompt: str) -> list:
    selected = []
    prompt_lower = prompt.lower()
    for spec in CHARACTER_SPECS:
        tag = spec["tag"]
        mid = LOCKED_CHARACTER_MEDIA_IDS.get(tag)
        if not mid:
            continue
        for alias in spec["aliases"]:
            if alias.lower() in prompt_lower:
                if mid not in selected:
                    selected.append(mid)
                break
    if not selected:
        for spec in CHARACTER_SPECS[:4]:
            mid = LOCKED_CHARACTER_MEDIA_IDS.get(spec["tag"])
            if mid and mid not in selected:
                selected.append(mid)
    return selected[:7]


def extract_start_frame_image_prompt(video_prompt: str, scene_num: int, clip_num: int) -> str:
    """Trích xuất mô tả [START FRAME] và [TIMELINE AND LOCATION] để tạo ảnh Start Frame 16:9 cho Clip 1 bằng nano_banana_pro."""
    start_desc = ""
    loc_desc = ""
    m_start = re.search(r"\[START FRAME[^\]]*\]\s*\n(.+?)(?:\n\n|\n\[|$)", video_prompt, flags=re.S)
    if m_start:
        start_desc = m_start.group(1).strip()
    m_loc = re.search(r"\[TIMELINE AND LOCATION\]\s*\n([^\[]+)", video_prompt, flags=re.S)
    if m_loc:
        loc_lines = [ln.strip() for ln in m_loc.group(1).strip().splitlines() if ln.strip()]
        loc_desc = " ".join(loc_lines[:2])
    base = (
        f"Photorealistic 16:9 widescreen 35mm cinema still frame for Scene {scene_num:02d} Clip {clip_num:02d} of "
        f"'Bí Mật Phòng 613'. {start_desc} Environment: {loc_desc} "
        "Atmospheric old-Saigon apartment jade-green walls, cyan-teal shadows, warm amber incense/altar highlights, "
        "natural Vietnamese skin tones, 8K, no text, no subtitles, no split screen."
    )
    return base[:1500]


def generate_scene_start_frame_for_veo(video_prompt: str, scene_num: int, clip_num: int, ref_media_ids: list) -> str:
    """Tạo ảnh Start Frame 16:9 khóa nhân vật (@Phuong, @Trinh, @BacBaoVe, @BongAoTrang) cho Clip mở đầu để nạp vào veo_3_1_i2v_lite (8s)."""
    cached_start = os.path.join(FRAMES_DIR, f"scene_{scene_num:02d}_clip_{clip_num:02d}_start_mid.txt")
    if os.path.exists(cached_start) and os.environ.get("FLOWKIT_FORCE_RERENDER") != "1":
        try:
            with open(cached_start, "r", encoding="utf-8") as f:
                mid = f.read().strip()
            if mid and len(mid) >= 20:
                return mid
        except Exception:
            pass

    img_prompt = extract_start_frame_image_prompt(video_prompt, scene_num, clip_num)
    log(f"🖼️ [VEO-LITE START FRAME] Đang tạo khung hình gốc 16:9 khóa nhân vật cho Cảnh {scene_num:02d} - Clip {clip_num:02d}...")
    try:
        res = requests.post(
            f"{FLOWKIT_API}/api/flow/generate-image",
            json={
                "prompt": img_prompt,
                "project_id": PROJECT_ID,
                "aspect_ratio": IMAGE_ASPECT_RATIO,
                "image_model": "nano_banana_pro",
                "character_media_ids": ref_media_ids or None,
                "count": 1,
            },
            timeout=90,
        )
        if res.status_code == 200:
            data = res.json()
            inner = data.get("data") if isinstance(data.get("data"), dict) else data
            mid = inner.get("media_id") or inner.get("_mediaId")
            if not mid:
                medias = inner.get("media") or []
                if medias and isinstance(medias[0], dict):
                    mid = medias[0].get("name") or medias[0].get("media_id")
            if mid:
                try:
                    with open(cached_start, "w", encoding="utf-8") as f:
                        f.write(mid)
                except Exception:
                    pass
                print_box(
                    "🖼️ ĐÃ TẠO KHUNG HÌNH BẮT ĐẦU (START FRAME) CHO VEO-LITE 8S",
                    [
                        ("Phân Cảnh", f"Cảnh {scene_num:02d} - Clip {clip_num:02d}"),
                        ("Start Frame Media ID", mid),
                        ("Khóa Nhân Vật", ", ".join(ref_media_ids) if ref_media_ids else "Bối cảnh gốc"),
                        ("Model Kế Tiếp", f"{VIDEO_MODEL_NAME} ({CLIP_DURATION_S}s I2V)"),
                    ],
                )
                return mid
        else:
            log(f"⚠️ Không tạo được ảnh Start Frame mới (HTTP {res.status_code}), dùng trực tiếp ảnh Reference nhân vật làm Start Frame cho Veo-Lite.")
    except Exception as e:
        log(f"⚠️ Ngoại lệ khi tạo ảnh Start Frame cho Veo-Lite: {e}")

    return ref_media_ids[0] if ref_media_ids else None


# -------------------------------------------------------------
# 1. ĐỒNG BỘ DỰ ÁN VỚI DASHBOARD UI (DATABASE SYNC)
# -------------------------------------------------------------
def sync_dashboard_database(start_scene: int = 1, end_scene: int = 15):
    """Tự động tạo hoặc kiểm tra Project, Characters, Video, Scenes (8s, veo) trong FlowKit DB."""
    global CURRENT_VIDEO_ID, SCENE_DB_MAP
    log("🔄 Đang đồng bộ cơ sở dữ liệu với Dashboard UI (Veo-Lite 8s + Video Extend)...")

    try:
        r = requests.get(f"{FLOWKIT_API}/api/projects", timeout=5)
        projects = r.json() if r.status_code == 200 else []
        proj_exists = any(p.get("id") == PROJECT_ID for p in projects)
        if not proj_exists:
            log("   ...Đang đăng ký dự án 'Bí Mật Phòng 613: Lời Cảnh Báo Đêm Rằm' vào hệ thống...")
            p_payload = {
                "name": "Bí Mật Phòng 613: Lời Cảnh Báo Đêm Rằm",
                "flow_project_id": PROJECT_ID,
                "material": "realistic",
                "video_model_family": VIDEO_MODEL_FAMILY,
                "story": "Phương và Trinh thuê căn phòng 613 giá rẻ tại chung cư cũ Sài Gòn và khám phá bí mật vụ hỏa hoạn đêm rằm năm 2016.",
                "characters": [
                    {"name": spec["tag"].lstrip("@"), "description": spec["description"]}
                    for spec in CHARACTER_SPECS
                ],
            }
            requests.post(f"{FLOWKIT_API}/api/projects", json=p_payload, timeout=10)

        r_chars = requests.get(f"{FLOWKIT_API}/api/characters", params={"project_id": PROJECT_ID}, timeout=5)
        if r_chars.status_code == 200:
            db_chars = r_chars.json() or []
            for spec in CHARACTER_SPECS:
                mid = LOCKED_CHARACTER_MEDIA_IDS.get(spec["tag"])
                if not mid:
                    continue
                aliases_lower = {a.lower().lstrip("@") for a in spec["aliases"]}
                for dbc in db_chars:
                    if (dbc.get("name") or "").strip().lower().lstrip("@") in aliases_lower:
                        requests.put(
                            f"{FLOWKIT_API}/api/characters/{dbc['id']}",
                            json={
                                "description": spec["description"],
                                "media_id": mid,
                                "status": "COMPLETED",
                            },
                            timeout=5,
                        )

        r_v = requests.get(f"{FLOWKIT_API}/api/videos?project_id={PROJECT_ID}", timeout=5)
        videos = r_v.json() if r_v.status_code == 200 else []
        if videos:
            CURRENT_VIDEO_ID = videos[0]["id"]
        else:
            v_payload = {
                "project_id": PROJECT_ID,
                "title": "Bí Mật Phòng 613: Lời Cảnh Báo Đêm Rằm (15 Cảnh × 6 Clips × 8s — Veo Lite)",
                "description": "Phim ngắn tâm lý bí ẩn kịch tính 15 Cảnh × 6 Clips × 8s (Model veo_3_1_i2v_lite + Video Extend)",
                "orientation": "HORIZONTAL",
            }
            res_v = requests.post(f"{FLOWKIT_API}/api/videos", json=v_payload, timeout=10)
            if res_v.status_code == 200:
                CURRENT_VIDEO_ID = res_v.json().get("id")

        if CURRENT_VIDEO_ID:
            r_s = requests.get(f"{FLOWKIT_API}/api/scenes?video_id={CURRENT_VIDEO_ID}", timeout=5)
            existing_scenes = r_s.json() if r_s.status_code == 200 else []

            order = 0
            for s in range(start_scene, end_scene + 1):
                for c in range(1, 7):
                    key = f"canh_{s:02d}_clip_{c:02d}"
                    match = next((sc for sc in existing_scenes if sc.get("display_order") == order), None)
                    if match:
                        SCENE_DB_MAP[key] = match["id"]
                    else:
                        fpath = os.path.join(SERIES_DIR, f"canh-{s:02d}", f"clip-{c}.md")
                        prompt_preview = f"Cảnh {s:02d} - Clip {c}"
                        if os.path.exists(fpath):
                            with open(fpath, "r", encoding="utf-8") as f:
                                prompt_preview = f.read().strip()[:200]
                        sc_payload = {
                            "video_id": CURRENT_VIDEO_ID,
                            "display_order": order,
                            "chain_type": "ROOT" if c == 1 else "CONTINUATION",
                            "duration": float(CLIP_DURATION_S),
                            "prompt": f"Cảnh {s:02d} - Clip {c}",
                            "video_prompt": prompt_preview,
                            "character_names": ["Phuong", "Trinh", "BacBaoVe", "BongAoTrang"],
                        }
                        r_new = requests.post(f"{FLOWKIT_API}/api/scenes", json=sc_payload, timeout=5)
                        if r_new.status_code == 200:
                            SCENE_DB_MAP[key] = r_new.json().get("id")
                    order += 1

        log(f"✅ Đã đồng bộ Dashboard DB thành công! ({len(SCENE_DB_MAP)} scenes × {CLIP_DURATION_S}s sẵn sàng)")
    except Exception as e:
        log(f"⚠️ Lỗi khi đồng bộ DB Dashboard: {e}")


def update_dashboard_scene_status(scene_num: int, clip_num: int, video_url: str):
    """Cập nhật trạng thái COMPLETED và link video lên Dashboard UI ngay lập tức."""
    key = f"canh_{scene_num:02d}_clip_{clip_num:02d}"
    sid = SCENE_DB_MAP.get(key)
    if not sid:
        return
    try:
        patch_payload = {
            "horizontal_video_url": video_url,
            "horizontal_video_status": "COMPLETED",
        }
        r = requests.patch(f"{FLOWKIT_API}/api/scenes/{sid}", json=patch_payload, timeout=5)
        if r.status_code == 200:
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
    """Tải ngay lập tức video 8s về máy và ghi đè (overwrite) đúng file clip chuẩn theo cảnh."""
    scene_folder = os.path.join(OUTPUT_VIDEOS_DIR, f"canh-{scene_num:02d}")
    os.makedirs(scene_folder, exist_ok=True)

    filename = f"canh-{scene_num:02d}_clip-{clip_num:02d}.mp4"
    target_path = os.path.join(scene_folder, filename)
    is_overwrite = os.path.exists(target_path)
    tmp_path = f"{target_path}.tmp"

    log("📥 Đang tải video 8s (Veo-Lite) từ Google Flow về máy...")
    try:
        r = requests.get(video_url, stream=True, timeout=120)
        if r.status_code == 200:
            with open(tmp_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        f.write(chunk)
            os.replace(tmp_path, target_path)
            trim_studio_reference_frames(target_path, log_fn=log)
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
                ("Model & Thời Lượng", f"{VIDEO_MODEL_NAME} ({CLIP_DURATION_S}s)"),
                ("Chế Độ Lưu", "Ghi đè (Overwritten)" if is_overwrite else "Tạo mới"),
                ("Đường Dẫn Lưu", target_path),
                ("Dung Lượng", f"{size_mb:.2f} MB"),
                ("Thời Gian Hoàn Tất", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            ]
            if r2_sync.get("r2_url"):
                box_rows.append(("Cloudflare R2 URL", r2_sync["r2_url"]))
            print_box(
                "💾 CLIP 8S HOÀN THÀNH & ĐÃ GHI ĐÈ VỀ MÁY" if is_overwrite else "💾 CLIP 8S HOÀN THÀNH & ĐÃ TẢI VỀ MÁY",
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
    """Trích xuất khung hình cuối cùng của clip 8s bằng ffmpeg làm Start Frame để Extend Video cho clip tiếp theo."""
    out_frame = os.path.join(FRAMES_DIR, f"scene_{scene_num:02d}_clip_{clip_num:02d}_last.jpg")
    log(f"🎬 [EXTEND VIDEO] Dùng ffmpeg cắt khung hình cuối (Last Frame 8.0s) của Cảnh {scene_num:02d} - Clip {clip_num:02d}...")
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
                "🖼️ ĐÃ TRÍCH XUẤT KHUNG HÌNH CUỐI (EXTEND VIDEO 8S)",
                [
                    ("Clip Nguồn (8s)", f"Cảnh {scene_num:02d} - Clip {clip_num:02d}"),
                    ("File Ảnh Nối Cảnh", os.path.basename(out_frame)),
                    ("Đường Dẫn Lưu", out_frame),
                    ("Dung Lượng Ảnh", f"{size_kb:.1f} KB"),
                    ("Mục Đích Sử Dụng", f"Extend Video sang Clip {clip_num + 1:02d} bằng {VIDEO_MODEL_NAME} (8s)"),
                ],
            )
            return out_frame
        else:
            cmd_fallback = [
                "ffmpeg", "-y",
                "-ss", "00:00:07.5",
                "-i", video_source,
                "-frames:v", "1",
                "-q:v", "2",
                out_frame,
            ]
            res_fb = subprocess.run(cmd_fallback, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=45)
            if res_fb.returncode == 0 and os.path.exists(out_frame) and os.path.getsize(out_frame) > 0:
                log(f"✨ Trích xuất khung hình cuối thành công (fallback ss 7.5s): {os.path.basename(out_frame)}")
                return out_frame
            else:
                log(f"⚠️ ffmpeg không trích xuất được frame: {result.stderr.decode('utf-8', errors='ignore')[:200]}")
                return None
    except Exception as e:
        log(f"⚠️ Lỗi khi trích xuất frame: {e}")
        return None


def upload_start_frame(image_path: str) -> str:
    """Nạp khung hình cuối vừa cắt vào slot [Bắt đầu] trên Google Flow để Extend Video bằng veo_3_1_i2v_lite."""
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
                "📤 ĐÃ TẢI ẢNH LÊN GOOGLE FLOW [EXTEND VIDEO START FRAME]",
                [
                    ("Media ID", media_id),
                    ("File Ảnh Nối", os.path.basename(image_path)),
                    ("Slot Kích Hoạt", "Khung hình [Bắt đầu] (Start Frame) để Extend Video"),
                    ("Trạng Thái", f"Sẵn sàng Extend Video 8s với {VIDEO_MODEL_NAME} ✅"),
                ],
            )
            return media_id
        else:
            log(f"⚠️ Không upload được frame: {res.text}")
            return None
    except Exception as e:
        log(f"⚠️ Lỗi upload frame: {e}")
        return None


def load_previous_last_frame(scene_num: int, prev_clip_num: int) -> str:
    """Lấy frame cuối của clip trước đã có trên đĩa (khi chạy lẻ 1 clip hoặc resume) rồi upload làm Start Frame để Extend Video."""
    frame_path = None
    mp4_candidate = os.path.join(
        OUTPUT_VIDEOS_DIR,
        f"canh-{scene_num:02d}",
        f"canh-{scene_num:02d}_clip-{prev_clip_num:02d}.mp4",
    )
    if os.path.exists(mp4_candidate) and os.path.getsize(mp4_candidate) > 50_000:
        frame_path = extract_last_frame(mp4_candidate, scene_num, prev_clip_num)
    if not frame_path:
        for cn, mp4_path in find_episode_clip_mp4s(OUTPUT_VIDEOS_DIR, scene_num, f"canh-{scene_num:02d}"):
            if cn == prev_clip_num:
                frame_path = extract_last_frame(mp4_path, scene_num, prev_clip_num)
                break
    if not frame_path:
        cached = os.path.join(FRAMES_DIR, f"scene_{scene_num:02d}_clip_{prev_clip_num:02d}_last.jpg")
        if os.path.exists(cached):
            frame_path = cached
    if not frame_path:
        log(
            f"⚠️ Chưa có video/frame cuối của Cảnh {scene_num:02d} - Clip {prev_clip_num:02d} — "
            f"Clip {prev_clip_num + 1:02d} sẽ tạo Start Frame khóa nhân vật mới cho {VIDEO_MODEL_NAME}."
        )
        return None
    return upload_start_frame(frame_path)


# -------------------------------------------------------------
# 4. GỬI API REQUEST VEO-LITE 8S + EXTEND VIDEO
# -------------------------------------------------------------
def submit_clip_with_detailed_log(prompt: str, scene_num: int, clip_num: int, start_image_media_id: str = None):
    """Gửi yêu cầu tạo video 8s bằng model veo-lite (veo_3_1_i2v_lite) kèm Extend Video cho Clip 2..6."""
    key = f"canh_{scene_num:02d}_clip_{clip_num:02d}"
    sid = SCENE_DB_MAP.get(key) or f"scene_{scene_num:02d}_clip_{clip_num:02d}"
    clip_tag = f"[CẢNH {scene_num:02d} - CLIP {clip_num:02d}]"
    flow_prompt = prompt if prompt.startswith(clip_tag) else f"{clip_tag}\n{prompt}"

    ref_media_ids = get_clip_reference_media_ids(prompt)
    is_extend = (clip_num > 1) and bool(start_image_media_id)

    # Nếu là Clip 1 (hoặc chưa có start_image_media_id từ clip trước), tạo Start Frame 16:9 khóa nhân vật cho Veo-Lite
    effective_start_mid = start_image_media_id
    if not effective_start_mid:
        effective_start_mid = generate_scene_start_frame_for_veo(prompt, scene_num, clip_num, ref_media_ids)

    if effective_start_mid:
        endpoint = "/api/flow/generate-video"
        if is_extend:
            mode = f"🔗 EXTEND VIDEO 8s ({VIDEO_MODEL_NAME} nối tiếp từ Frame cuối Clip {clip_num - 1:02d})"
            slot_desc = f"Extend Start Frame = {effective_start_mid}"
        else:
            mode = f"🎬 INITIAL VEO-LITE 8s ({VIDEO_MODEL_NAME} từ Start Frame khóa nhân vật)"
            slot_desc = f"Scene Start Frame = {effective_start_mid} (Refs: {', '.join(ref_media_ids)})"
        payload = {
            "start_image_media_id": effective_start_mid,
            "prompt": flow_prompt,
            "project_id": PROJECT_ID,
            "scene_id": sid,
            "duration_s": CLIP_DURATION_S,
            "model_family": VIDEO_MODEL_FAMILY,
            "resolution": "720p",
            "aspect_ratio": ASPECT_RATIO,
            "user_paygate_tier": "PAYGATE_TIER_TWO",
        }
    elif ref_media_ids:
        endpoint = "/api/flow/generate-video-refs"
        mode = f"🔒 Reference-to-Video 8s ({VIDEO_MODEL_NAME} fallback với {len(ref_media_ids)} nhân vật)"
        slot_desc = f"Refs = {', '.join(ref_media_ids)}"
        payload = {
            "reference_media_ids": ref_media_ids,
            "prompt": flow_prompt,
            "project_id": PROJECT_ID,
            "scene_id": sid,
            "duration_s": CLIP_DURATION_S,
            "model_family": VIDEO_MODEL_FAMILY,
            "resolution": "720p",
            "aspect_ratio": ASPECT_RATIO,
            "user_paygate_tier": "PAYGATE_TIER_TWO",
        }
    else:
        endpoint = "/api/flow/generate-video-omni-text"
        mode = "🎬 Text-to-Video 8s (Fallback)"
        slot_desc = "[Trống - Khởi tạo từ Text]"
        payload = {
            "prompt": flow_prompt,
            "project_id": PROJECT_ID,
            "scene_id": sid,
            "duration_s": CLIP_DURATION_S,
            "resolution": "720p",
            "aspect_ratio": ASPECT_RATIO,
        }

    print_box(
        "📡 FLOWKIT API REQUEST CALL (VEO-LITE 8S + EXTEND VIDEO)",
        [
            ("Endpoint API", f"POST {endpoint}"),
            ("Tên Trên Google Flow", clip_tag),
            ("Phân Cảnh", f"Cảnh {scene_num:02d} - Clip {clip_num:02d}"),
            ("Chế Độ Tạo", mode),
            ("Khóa Hình Ảnh / Nhân Vật", slot_desc),
            ("Thời Lượng", f"{CLIP_DURATION_S} giây (Veo 3.1 Lite 8s)"),
            ("Độ Phân Giải", "720p HD"),
            ("Tỉ Lệ Khung Hình", ASPECT_RATIO),
            ("Model Family / Wire ID", f"{VIDEO_MODEL_FAMILY} ({VIDEO_MODEL_NAME})"),
            ("Độ Dài Prompt", f"{len(flow_prompt)} ký tự"),
            ("Prompt Preview", flow_prompt[:120].replace("\n", " ") + "..."),
        ],
    )

    url = f"{FLOWKIT_API}{endpoint}"
    res = requests.post(url, json=payload, timeout=60)
    return res


def poll_generation(submit_res_data: dict, scene_num: int, clip_num: int, timeout_s=360):
    """Theo dõi tiến trình sinh video 8s (Veo-Lite) cho đến khi hoàn thành."""
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
        else ("operations (Veo 3.1 Lite 8s I2V / Video Extend)" if operations else "direct media")
    )
    log(f"⏳ Đang theo dõi tiến trình tạo video 8s [Cảnh {scene_num:02d} - Clip {clip_num:02d}] (Chế độ: {poll_mode_desc})...")

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
                        log(f"🎉 Google Flow (Veo-Lite 8s) render hoàn tất sau {elapsed}s!")
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
                log(f"   ...Google Flow ({VIDEO_MODEL_NAME} 8s) đang vẽ video ({elapsed}s trôi qua)...")

        except Exception as e:
            log(f"   ...lỗi tạm thời khi poll ({e}), tiếp tục chờ...")

        time.sleep(6)

    log(f"⚠️ Hết thời gian chờ {timeout_s}s (Timeout) khi render Cảnh {scene_num:02d} - Clip {clip_num:02d}.")
    return {"success": False, "error": "TIMEOUT"}


# -------------------------------------------------------------
# 5. CHU TRÌNH ĐIỀU PHỐI TỔNG THỂ (VEO-LITE 8S + EXTEND VIDEO)
# -------------------------------------------------------------
def run_clip_with_auto_retry(scene_num: int, clip_num: int, initial_prompt: str, start_image_media_id: str = None, max_retries: int = 2):
    current_prompt = initial_prompt

    for attempt in range(1, max_retries + 1):
        if attempt > 1:
            log(f"🔄 Đang chạy lại Cảnh {scene_num:02d} - Clip {clip_num:02d} (Lần {attempt}/{max_retries})...")

        try:
            res = submit_clip_with_detailed_log(current_prompt, scene_num, clip_num, start_image_media_id)
            cooldown_loops = 0
            while res.status_code != 200 and cooldown_loops < 5:
                if wait_if_cooldown_error(res.text, FLOWKIT_API, log):
                    cooldown_loops += 1
                    res = submit_clip_with_detailed_log(current_prompt, scene_num, clip_num, start_image_media_id)
                else:
                    break

            if res.status_code == 200:
                data = res.json()
                inner = data.get("data") if isinstance(data.get("data"), dict) else data
                log(f"✅ Google Flow đã chấp nhận job tạo video 8s ({VIDEO_MODEL_NAME}).")

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
            log(f"🔧 [ĐỔI PROMPT TỰ ĐỘNG - LẦN THỬ {attempt + 1}/{max_retries}] Đang làm mềm prompt trên bộ nhớ cho Cảnh {scene_num:02d} - Clip {clip_num:02d}...")
            current_prompt = sanitize_prompt(initial_prompt, attempt)
            if start_image_media_id:
                log(f"🔄 Giữ frame cuối của clip trước để Extend Video 8s ({VIDEO_MODEL_NAME}) và chạy lại sau 5 giây...")
            else:
                log(f"🔄 Khởi tạo lại Start Frame khóa nhân vật cho {VIDEO_MODEL_NAME} 8s và chạy lại sau 5 giây...")
            time.sleep(5)

    log(f"⏭️ [BỎ QUA SAU {max_retries} LẦN LỖI] Cảnh {scene_num:02d} - Clip {clip_num:02d} đã fail {max_retries} lần — tạm bỏ qua để kiểm tra và tạo lại sau!")
    return {"success": False, "video_url": None}


def run_pipeline(start_scene=1, end_scene=15):
    global CURRENT_EP_NUM, CURRENT_CLIP_NUM
    print("\n" + "=" * 72)
    print("🎬 KHỞI ĐỘNG HỆ THỐNG FLOWKIT — BÍ MẬT PHÒNG 613 (VEO-LITE 8S + EXTEND VIDEO)")
    print(f"📁 Phạm vi: Cảnh {start_scene:02d} đến Cảnh {end_scene:02d} (6 clips × {CLIP_DURATION_S}s = {6 * CLIP_DURATION_S}s/cảnh)")
    print(f"🤖 Model Video: {VIDEO_MODEL_NAME} (model_family={VIDEO_MODEL_FAMILY}, {CLIP_DURATION_S}s/clip + Video Extend)")
    print(f"🔗 Google Flow Project: {PROJECT_ID}")
    print(f"💾 Tải video tự động về: {OUTPUT_VIDEOS_DIR}")
    print(f"🖼️ Lưu khung hình Extend Video tại: {FRAMES_DIR}")
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
        print(f"👉 BẮT ĐẦU CẢNH {s:02d} (6 Clips × {CLIP_DURATION_S}s — Veo-Lite + Video Extend)")
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
                        f"đã có video ({r2_done}) — nạp frame cuối làm mốc Extend Video cho clip kế tiếp."
                    )
                    previous_clip_last_frame_media_id = None
                    continue

            with open(fpath, "r", encoding="utf-8") as f:
                prompt_content = f.read().strip()

            # 🔗 EXTEND VIDEO: Từ Clip 2 trở đi luôn lấy frame cuối của Clip (c_idx - 1) làm Start Frame cho Veo-Lite 8s
            if c_idx > 1 and not previous_clip_last_frame_media_id:
                previous_clip_last_frame_media_id = load_previous_last_frame(s, c_idx - 1)

            completed_clips += 1
            progress_pct = (completed_clips / max(1, total_clips)) * 100
            mode_tag = "ROOT 8s" if c_idx == 1 else f"EXTEND 8s từ Clip {c_idx - 1:02d}"
            print(
                f"\n▶️ TIẾN ĐỘ TỔNG: [{completed_clips}/{total_clips}] ({progress_pct:.1f}%) — "
                f"CẢNH {s:02d} - CLIP {c_idx:02d} [{mode_tag} | {VIDEO_MODEL_NAME}]",
                flush=True,
            )

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

                # Trích xuất frame cuối của clip 8s vừa xong để Extend Video sang clip tiếp theo (c_idx + 1)
                frame_path = extract_last_frame(local_video if local_video else video_url, s, c_idx)
                has_next_clip = c_idx < 6
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
            else {cn for cn, _ in find_episode_clip_mp4s(OUTPUT_VIDEOS_DIR, s, f"canh-{s:02d}")}
        )
        missing_clips = [
            c_idx
            for c_idx in clip_indices
            if c_idx not in existing_nums and os.path.exists(os.path.join(scene_dir, f"clip-{c_idx}.md"))
        ]
        if missing_clips:
            log(
                f"⏭️ [DANH SÁCH CLIP TẠM BỎ QUA] Cảnh {s:02d} có {len(missing_clips)} clip chưa hoàn tất ({missing_clips}) "
                "sau 2 lần thử — giữ nguyên kịch bản gốc để kiểm tra và tạo lại sau."
            )

        CURRENT_CLIP_NUM = None
        log(f"✅ Đã hoàn tất render các clip 8s của Cảnh {s:02d} (Bỏ qua auto-merge; bấm nút ghép tập trên UI khi cần).")

    print("\n" + "=" * 72)
    print(f"🎉 HOÀN THÀNH TOÀN BỘ CHU TRÌNH TỪ CẢNH {start_scene:02d} ĐẾN CẢNH {end_scene:02d} (VEO-LITE 8S + EXTEND VIDEO)!")
    print(f"📁 Video hoàn chỉnh đã được lưu tại: {OUTPUT_VIDEOS_DIR}")
    print("=" * 72 + "\n", flush=True)


if __name__ == "__main__":
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 15
    run_pipeline(start, end)
