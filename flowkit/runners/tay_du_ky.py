#!/usr/bin/env python3
"""
HỆ THỐNG TỰ ĐỘNG HÓA FLOWKIT NÂNG CAO CHO "TÂY DU KÝ 2026" (KHUNG HÌNH DỌC 9:16):
1. KHÓA NHÂN VẬT CỐ ĐỊNH (CHARACTER LOCK): Tự động lấy & khóa chính xác media_id của @Thay (@DuongTang), @DaiCa (@NgoKhong), @HeoLuoi (@BatGioi), @UtKho (@SaTang) từ Google Flow Project.
2. Luôn truyền reference_media_ids qua endpoint /api/flow/generate-video-omni (MZZa6b Ingredients R2V) cho Clip 1 và mọi clip mở cảnh mới ([FORMAT]).
3. Tự động trích xuất khung hình cuối (last frame) làm khung hình đầu (start frame) của clip nối tiếp (Seamless Chaining).
4. Tự động đặt tên clip trên Google Flow theo cảnh ([TẬP XX - CLIP YY]) và tải ngay về máy khi hoàn thành.
5. Tự động đồng bộ thời gian thực với Console Dashboard UI (VERTICAL 9:16).
"""

import os
import re
import sys
import glob
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
    wait_if_cooldown_error,
    sync_clip_to_r2_and_d1,
    rewrite_prompt_on_failure,
    find_episode_clip_mp4s,
    force_rename_clip_on_flow,
)

FLOWKIT_API = "http://127.0.0.1:8200"
CHANNEL_SLUG = "tay-du-ky-2026"
ONLY_CLIP = int(os.environ.get("FLOWKIT_ONLY_CLIP", "0") or "0")

# 👉 PROJECT_ID GOOGLE FLOW CỦA SERIES "TÂY DU KÝ 2026" (Tỉ lệ: 9:16 PORTRAIT)
PROJECT_ID = "5a1c26fe-7edc-42e3-b927-09e16e8f481d"
DEFAULT_PROJECT_ID = "5a1c26fe-7edc-42e3-b927-09e16e8f481d"
ASPECT_RATIO = "VIDEO_ASPECT_RATIO_PORTRAIT"  # 9:16 Khung hình dọc TikTok
IMAGE_ASPECT_RATIO = "IMAGE_ASPECT_RATIO_PORTRAIT"

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SERIES_DIR = os.path.join(WORKSPACE_DIR, "tay-du-ky-2026")
FRAMES_DIR = os.path.join(SERIES_DIR, "exported_frames")
OUTPUT_VIDEOS_DIR = os.path.join(SERIES_DIR, "output_videos")
CHAR_REFS_DIR = os.path.join(SERIES_DIR, "character_refs")
CHAR_CACHE_FILE = os.path.join(CHAR_REFS_DIR, "character_media_ids.json")

os.makedirs(FRAMES_DIR, exist_ok=True)
os.makedirs(OUTPUT_VIDEOS_DIR, exist_ok=True)
os.makedirs(CHAR_REFS_DIR, exist_ok=True)

# -------------------------------------------------------------
# 🔒 BẢNG ĐỊNH NGHĨA & KHÓA NHÂN VẬT CỐ ĐỊNH CỦA SERIES (TÂY DU KÝ 2026)
# -------------------------------------------------------------
CHARACTER_SPECS = [
    {
        "key": "Thay",
        "tag": "@Thay",
        "aliases": ["@Thay", "@DuongTang", "DuongTang", "Đường Tăng", "Thầy"],
        "default_media_id": "ad0c12d2-83a3-46df-a61c-c97f150c1fd1",
        "description": "Thầy / Đường Tăng: nhà sư trẻ tuấn tú hiền lành, đầu cạo trọc, mặc áo cà sa cam nghệ và áo lót trắng ngà, đeo chuỗi hạt gỗ 108 hạt.",
        "ref_prompt": (
            "Full-body 3D stylized character reference sheet of @Thay (DuongTang), a handsome gentle young monk in his late 20s, "
            "clean-shaven head, serene warm eyes, wearing a saffron-orange monk robe draped over a cream inner shirt and wooden prayer beads. "
            "High-end stylized 3D CGI animation, vertical 9:16."
        ),
    },
    {
        "key": "DaiCa",
        "tag": "@DaiCa",
        "aliases": ["@DaiCa", "@NgoKhong", "NgoKhong", "Ngộ Không", "Đại Ca"],
        "default_media_id": "34619eb9-7c90-4337-87c0-8375e53f4e3d",
        "description": "Đại Ca / Ngộ Không: chàng khỉ nhân hóa lanh lẹ, lông vàng nâu, đeo vòng kim cô vàng trên trán, mặc áo khoác bomber đỏ, quần jogger đen.",
        "ref_prompt": (
            "Full-body 3D stylized character reference sheet of @DaiCa (NgoKhong), an agile anthropomorphic golden-furred monkey king "
            "standing upright on two legs, wearing a golden headband circlet (vòng kim cô), a modern red streetwear bomber jacket over a yellow tee, "
            "and black cargo joggers. High-end stylized 3D CGI animation, vertical 9:16."
        ),
    },
    {
        "key": "HeoLuoi",
        "tag": "@HeoLuoi",
        "aliases": ["@HeoLuoi", "@BatGioi", "BatGioi", "Bát Giới", "Heo Lười"],
        "default_media_id": "e556190e-4c69-464c-b081-cd1b87a39135",
        "description": "Heo Lười / Bát Giới: chàng heo nhân hóa mập tròn vui tính, mũi heo hồng, tai to, mặc áo thun đen hở bụng tròn và áo sơ mi khoác ngoài xanh navy.",
        "ref_prompt": (
            "Full-body 3D stylized character reference sheet of @HeoLuoi (BatGioi), a chubby cheerful anthropomorphic pig standing upright, "
            "pink pig snout and big floppy ears, round belly, wearing an open navy-blue Hawaiian shirt over a black t-shirt and shorts. "
            "High-end stylized 3D CGI animation, vertical 9:16."
        ),
    },
    {
        "key": "UtKho",
        "tag": "@UtKho",
        "aliases": ["@UtKho", "@SaTang", "SaTang", "Sa Tăng", "Út Khờ"],
        "default_media_id": "34b98c88-ca70-463a-bd23-128c4d405b38",
        "description": "Út Khờ / Sa Tăng: chàng trai to lớn thật thà, râu quai nón dày, đeo chuỗi hạt to quanh cổ, mặc tạp dề xanh rêu.",
        "ref_prompt": (
            "Full-body 3D stylized character reference sheet of @UtKho (SaTang), a tall muscular honest-looking man with a thick beard "
            "and topknot hair, wearing large wooden beads around his neck and an olive-green apron over work clothes. "
            "High-end stylized 3D CGI animation, vertical 9:16."
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


def resolve_episode_dir(ep_num: int) -> str:
    """Tìm thư mục tập phim (tap-8, tap-08...)."""
    candidates = [
        os.path.join(SERIES_DIR, f"tap-{ep_num}"),
        os.path.join(SERIES_DIR, f"tap-{ep_num:02d}"),
        os.path.join(SERIES_DIR, f"tap{ep_num}"),
    ]
    for c in candidates:
        if os.path.isdir(c):
            return c
    matches = sorted(glob.glob(os.path.join(SERIES_DIR, f"tap*{ep_num}*")))
    for m in matches:
        if os.path.isdir(m):
            return m
    return os.path.join(SERIES_DIR, f"tap-{ep_num}")


def get_episode_clips(ep_dir: str) -> list:
    """Lấy danh sách (clip_num, clip_path) đã sắp xếp theo thứ tự."""
    if not os.path.isdir(ep_dir):
        return []
    clips = []
    for fname in os.listdir(ep_dir):
        m = re.match(r"^clip-(\d+)\.md$", fname)
        if m:
            clips.append((int(m.group(1)), os.path.join(ep_dir, fname)))
    clips.sort(key=lambda x: x[0])
    return clips


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
    """Đảm bảo 100% sử dụng đúng 4 thầy trò đã quy định trong Google Flow Project."""
    global LOCKED_CHARACTER_MEDIA_IDS
    log("🔒 Đang kiểm tra và khóa bộ nhân vật cố định (4 Thầy Trò Tây Du Ký 2026) trên Google Flow...")

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

        if not matched_mid and PROJECT_ID == DEFAULT_PROJECT_ID and spec.get("default_media_id"):
            matched_mid = spec["default_media_id"]

        if not matched_mid and project_cache.get(tag):
            matched_mid = project_cache[tag]

        if not matched_mid and spec.get("ref_prompt"):
            log(f"🎨 Đang tạo mới ảnh mẫu cố định cho nhân vật {tag} trên Project {PROJECT_ID}...")
            try:
                gen_res = requests.post(
                    f"{FLOWKIT_API}/api/flow/generate-image",
                    json={
                        "prompt": spec["ref_prompt"],
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
    box_items.append(("Chế Độ Khóa", "Ingredients R2V (/api/flow/generate-video-omni) + Seamless I2V"))
    print_box("🔒 ĐÃ KHÓA NHÂN VẬT CỐ ĐỊNH (CHARACTER LOCK)", box_items)


def is_new_scene_clip(prompt: str, clip_num: int, start_image_media_id: str = None) -> bool:
    if clip_num == 1 or not start_image_media_id:
        return True
    stripped = prompt.lstrip()
    if stripped.startswith("Continue the scene seamlessly"):
        return False
    if stripped.startswith("[FORMAT]") or stripped.startswith("[ĐỊNH DẠNG]"):
        return True
    return False


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
        for spec in CHARACTER_SPECS:
            mid = LOCKED_CHARACTER_MEDIA_IDS.get(spec["tag"])
            if mid and mid not in selected:
                selected.append(mid)
    return selected[:7]


# -------------------------------------------------------------
# 1. ĐỒNG BỘ DỰ ÁN VỚI DASHBOARD UI (DATABASE SYNC - 9:16)
# -------------------------------------------------------------
def sync_dashboard_database(start_ep: int, end_ep: int):
    """Tự động tạo hoặc kiểm tra Project, Characters, Video, Scenes trong FlowKit DB."""
    global CURRENT_VIDEO_ID, SCENE_DB_MAP
    log("🔄 Đang đồng bộ cơ sở dữ liệu với Dashboard UI (9:16 VERTICAL)...")

    try:
        r = requests.get(f"{FLOWKIT_API}/api/projects", timeout=5)
        projects = r.json() if r.status_code == 200 else []
        proj_exists = any(p.get("id") == PROJECT_ID for p in projects)
        if not proj_exists:
            log("   ...Đang đăng ký dự án 'Tây Du Ký 2026' vào hệ thống...")
            p_payload = {
                "name": "Tây Du Ký 2026",
                "flow_project_id": PROJECT_ID,
                "material": "anime",
                "story": "Bốn thầy trò Thầy, Đại Ca, Heo Lười, Út Khờ thuê nhà trọ ở hẻm Sài Gòn năm 2026.",
                "characters": [
                    {"name": spec["tag"].lstrip("@"), "description": spec["description"]}
                    for spec in CHARACTER_SPECS
                ]
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
                "title": f"Tây Du Ký 2026 (Tập {start_ep:02d} - {end_ep:02d})",
                "description": "Drama đời thường hài hước của 4 thầy trò ở hẻm Sài Gòn 2026 (Khung hình dọc 9:16)",
                "orientation": "VERTICAL"
            }
            res_v = requests.post(f"{FLOWKIT_API}/api/videos", json=v_payload, timeout=10)
            if res_v.status_code == 200:
                CURRENT_VIDEO_ID = res_v.json().get("id")

        if CURRENT_VIDEO_ID:
            r_s = requests.get(f"{FLOWKIT_API}/api/scenes?video_id={CURRENT_VIDEO_ID}", timeout=5)
            existing_scenes = r_s.json() if r_s.status_code == 200 else []

            order = 0
            for ep in range(start_ep, end_ep + 1):
                ep_dir = resolve_episode_dir(ep)
                clips = get_episode_clips(ep_dir)
                for c_num, fpath in clips:
                    key = f"tap_{ep:02d}_clip_{c_num:02d}"
                    match = next((sc for sc in existing_scenes if sc.get("display_order") == order), None)
                    if match:
                        SCENE_DB_MAP[key] = match["id"]
                    else:
                        prompt_preview = f"Tập {ep:02d} - Clip {c_num}"
                        if os.path.exists(fpath):
                            with open(fpath, "r", encoding="utf-8") as f:
                                prompt_preview = f.read().strip()[:200]
                        sc_payload = {
                            "video_id": CURRENT_VIDEO_ID,
                            "display_order": order,
                            "chain_type": "ROOT" if c_num == 1 else "CONTINUATION",
                            "prompt": f"Tập {ep:02d} - Clip {c_num}",
                            "video_prompt": prompt_preview,
                            "character_names": ["Thay", "DaiCa", "HeoLuoi", "UtKho"]
                        }
                        r_new = requests.post(f"{FLOWKIT_API}/api/scenes", json=sc_payload, timeout=5)
                        if r_new.status_code == 200:
                            SCENE_DB_MAP[key] = r_new.json().get("id")
                    order += 1

        log(f"✅ Đã đồng bộ Dashboard DB thành công! ({len(SCENE_DB_MAP)} scenes sẵn sàng)")
    except Exception as e:
        log(f"⚠️ Lỗi khi đồng bộ DB Dashboard: {e}")


def update_dashboard_scene_status(ep_num: int, clip_num: int, video_url: str):
    """Cập nhật trạng thái COMPLETED và link video 9:16 lên Dashboard UI ngay lập tức."""
    key = f"tap_{ep_num:02d}_clip_{clip_num:02d}"
    sid = SCENE_DB_MAP.get(key)
    if not sid:
        return
    try:
        patch_payload = {
            "vertical_video_url": video_url,
            "vertical_video_status": "COMPLETED"
        }
        r = requests.patch(f"{FLOWKIT_API}/api/scenes/{sid}", json=patch_payload, timeout=5)
        if r.status_code == 200:
            log(f"🖥️ [DASHBOARD UI] Đã cập nhật Scene '{key}' (9:16) thành trạng thái COMPLETED ✅")
    except Exception as e:
        log(f"⚠️ Lỗi cập nhật Dashboard Scene: {e}")


# -------------------------------------------------------------
# 2. BỘ TỰ ĐỘNG SỬA PROMPT KHI THẤT BẠI (PROMPT SANITIZER & RETRY)
# -------------------------------------------------------------
def sanitize_prompt(prompt: str, attempt: int = 1) -> str:
    return rewrite_prompt_on_failure(prompt, attempt, CHARACTER_SPECS, ASPECT_RATIO)


def update_clip_file(fpath: str, new_prompt: str):
    try:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_prompt)
        log(f"💾 Đã ghi đè prompt đã sửa an toàn vào: {fpath}")
    except Exception as e:
        log(f"⚠️ Lỗi khi ghi file {fpath}: {e}")


# -------------------------------------------------------------
# 3. TỰ ĐỘNG TẢI VIDEO VỀ MÁY VÀ ĐỔI TÊN THEO TẬP
# -------------------------------------------------------------
def download_and_rename_video(video_url: str, ep_num: int, clip_num: int, ep_folder_name: str) -> str:
    """Tải ngay lập tức video về máy và ghi đè (overwrite) đúng file clip chuẩn theo tập."""
    ep_folder = os.path.join(OUTPUT_VIDEOS_DIR, ep_folder_name)
    os.makedirs(ep_folder, exist_ok=True)

    filename = f"TDK_T{ep_num:02d}_C{clip_num:02d}.mp4"
    target_path = os.path.join(ep_folder, filename)
    is_overwrite = os.path.exists(target_path)
    tmp_path = f"{target_path}.tmp"

    log("📥 Đang tải video 9:16 từ Google Flow về máy...")
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
                ep_num=ep_num,
                clip_num=clip_num,
                local_video_path=target_path,
                ep_folder_name=ep_folder_name,
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
                "💾 CLIP HOÀN THÀNH & ĐÃ GHI ĐÈ VỀ MÁY (9:16)" if is_overwrite else "💾 CLIP HOÀN THÀNH & ĐÃ TẢI VỀ MÁY (9:16)",
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


def extract_last_frame(video_source: str, ep_num: int, clip_num: int) -> str:
    """Trích xuất khung hình cuối cùng của clip bằng ffmpeg làm start frame cho clip sau."""
    out_frame = os.path.join(FRAMES_DIR, f"tap_{ep_num:02d}_clip_{clip_num:02d}_last.jpg")
    log(f"🎬 Dùng ffmpeg cắt khung hình cuối (Last Frame) của Tập {ep_num:02d} - Clip {clip_num:02d}...")
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
                    ("Clip Nguồn", f"Tập {ep_num:02d} - Clip {clip_num:02d}"),
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
                    ("Trạng Thái", "Sẵn sàng Image-to-Video Omni Flash 10s (9:16) ✅"),
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
# 4. GỬI API REQUEST & LOG CHI TIẾT PARAMS (9:16 PORTRAIT + KHÓA NHÂN VẬT)
# -------------------------------------------------------------
def submit_clip_with_detailed_log(prompt: str, ep_num: int, clip_num: int, start_image_media_id: str = None):
    """Gửi yêu cầu tạo video 9:16 và luôn khóa đúng nhân vật 4 thầy trò."""
    key = f"tap_{ep_num:02d}_clip_{clip_num:02d}"
    sid = SCENE_DB_MAP.get(key) or f"tap_{ep_num:02d}_clip_{clip_num:02d}"
    clip_tag = f"[TẬP {ep_num:02d} - CLIP {clip_num:02d}]"
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
        mode = f"🔒 Ingredients Reference-to-Video (Khóa {len(ref_media_ids)} nhân vật gốc Tây Du Ký)"
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
        mode = "🎬 Text-to-Video (Khung hình gốc mở đầu tập)"
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
        "📡 FLOWKIT API REQUEST CALL (9:16 PORTRAIT — CHARACTER LOCKED)",
        [
            ("Endpoint API", f"POST {endpoint}"),
            ("Tên Trên Google Flow", clip_tag),
            ("Phân Cảnh", f"Tập {ep_num:02d} - Clip {clip_num:02d}"),
            ("Chế Độ Tạo", mode),
            ("Khóa Hình Ảnh / Nhân Vật", slot_desc),
            ("Thời Lượng", "10 giây (Omni Flash 10s)"),
            ("Độ Phân Giải", "720p HD"),
            ("Tỉ Lệ Khung Hình", "PORTRAIT (9:16 Vertical TikTok)"),
            ("Model Family", "omni_flash"),
            ("Độ Dài Prompt", f"{len(flow_prompt)} ký tự"),
            ("Prompt Preview", flow_prompt[:120].replace("\n", " ") + "..."),
        ]
    )

    url = f"{FLOWKIT_API}{endpoint}"
    res = requests.post(url, json=payload, timeout=60)
    return res


def poll_generation(submit_res_data: dict, ep_num: int, clip_num: int, timeout_s=360):
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
    log(f"⏳ Đang theo dõi tiến trình tạo video [Tập {ep_num:02d} - Clip {clip_num:02d}] (Chế độ: {poll_mode_desc})...")

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
                                f"[TẬP {ep_num:02d} - CLIP {clip_num:02d}]",
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
                                f"[TẬP {ep_num:02d} - CLIP {clip_num:02d}]",
                                media_id=target_mid, log_fn=log,
                            )
                            return {"success": True, "video_url": video_url}

            if primary_media_id and elapsed >= 30:
                direct_url = fetch_media_video_url(primary_media_id)
                if direct_url:
                    log(f"🎉 Phát hiện video sẵn sàng qua Media API sau {elapsed}s!")
                    force_rename_clip_on_flow(
                        FLOWKIT_API, PROJECT_ID, submit_res_data,
                        f"[TẬP {ep_num:02d} - CLIP {clip_num:02d}]",
                        media_id=primary_media_id, log_fn=log,
                    )
                    return {"success": True, "video_url": direct_url}

            if elapsed - last_logged_time >= 12:
                last_logged_time = elapsed
                log(f"   ...Google Flow đang vẽ video 9:16 đúng nhân vật ({elapsed}s trôi qua)...")

        except Exception as e:
            log(f"   ...lỗi tạm thời khi poll ({e}), tiếp tục chờ...")

        time.sleep(6)

    log(f"⚠️ Hết thời gian chờ {timeout_s}s (Timeout) khi render Tập {ep_num:02d} - Clip {clip_num:02d}.")
    return {"success": False, "error": "TIMEOUT"}


# -------------------------------------------------------------
# 5. CHU TRÌNH ĐIỀU PHỐI TỔNG THỂ
# -------------------------------------------------------------
def run_clip_with_auto_retry(ep_num: int, clip_num: int, fpath: str, initial_prompt: str, start_image_media_id: str = None, max_retries: int = 6):
    current_prompt = initial_prompt

    for attempt in range(1, max_retries + 1):
        if attempt > 1:
            log(f"🔄 [KHÔNG BỎ SÓT CLIP] Đang chạy lại Tập {ep_num:02d} - Clip {clip_num:02d} (Lần {attempt}/{max_retries}) với prompt đã viết lại...")

        try:
            res = submit_clip_with_detailed_log(current_prompt, ep_num, clip_num, start_image_media_id)
            if res.status_code == 200:
                data = res.json()
                inner = data.get("data") if isinstance(data.get("data"), dict) else data
                log("✅ Google Flow đã chấp nhận job tạo video 9:16.")

                poll_res = poll_generation(inner, ep_num, clip_num)
                if poll_res["success"] and poll_res.get("video_url"):
                    return poll_res
                else:
                    log(f"⚠️ Không nhận được video URL hoàn chỉnh ở lần thử {attempt} ({poll_res.get('error')}). Đổi prompt ngay lập tức!")
            else:
                log(f"❌ Google Flow phản hồi lỗi (HTTP {res.status_code}): {res.text}")
                if wait_if_cooldown_error(res.text, FLOWKIT_API, log):
                    res_after = submit_clip_with_detailed_log(current_prompt, ep_num, clip_num, start_image_media_id)
                    if res_after.status_code == 200:
                        data = res_after.json()
                        inner = data.get("data") if isinstance(data.get("data"), dict) else data
                        log("✅ Google Flow đã chấp nhận job tạo video sau khi chờ Cooldown.")
                        poll_res = poll_generation(inner, ep_num, clip_num)
                        if poll_res["success"] and poll_res.get("video_url"):
                            return poll_res
        except Exception as e:
            log(f"❌ Lỗi ngoại lệ khi gửi job: {e}")

        if attempt < max_retries:
            log(f"🔧 [ĐỔI PROMPT TỰ ĐỘNG - CẤP ĐỘ {attempt}] Đang viết lại prompt an toàn cho Tập {ep_num:02d} - Clip {clip_num:02d}...")
            current_prompt = sanitize_prompt(current_prompt, attempt)
            update_clip_file(fpath, current_prompt)
            start_image_media_id = None
            log("🔄 Khóa trực tiếp nhân vật gốc (Ingredients R2V) và chạy lại sau 5 giây...")
            time.sleep(5)

    return {"success": False, "video_url": None}


def run_pipeline(start_ep=12, end_ep=12):
    global CURRENT_EP_NUM, CURRENT_CLIP_NUM
    print("\n" + "=" * 72)
    print("🎬 KHỞI ĐỘNG HỆ THỐNG FLOWKIT TỰ ĐỘNG — TÂY DU KÝ 2026 (9:16)")
    print(f"📁 Phạm vi: Tập {start_ep:02d} đến Tập {end_ep:02d}")
    print(f"📐 Tỉ lệ khung hình: 9:16 PORTRAIT (Vertical TikTok)")
    print(f"🔗 Google Flow Project: {PROJECT_ID}")
    print(f"💾 Tải video tự động về: {OUTPUT_VIDEOS_DIR}")
    print(f"🖼️ Lưu khung hình nối cảnh tại: {FRAMES_DIR}")
    print("=" * 72 + "\n", flush=True)

    if not check_connection():
        sys.exit(1)

    load_and_lock_project_characters()
    sync_dashboard_database(start_ep, end_ep)

    episode_plan = []
    total_clips = 0
    for ep in range(start_ep, end_ep + 1):
        ep_dir = resolve_episode_dir(ep)
        clips = get_episode_clips(ep_dir)
        if ONLY_CLIP > 0:
            clips = [(c, p) for c, p in clips if c == ONLY_CLIP]
        if clips:
            episode_plan.append((ep, ep_dir, clips))
            total_clips += len(clips)

    if total_clips == 0:
        log(f"⚠️ Không tìm thấy file clip-*.md nào trong phạm vi Tập {start_ep} - {end_ep}!")
        return

    completed_clips = 0

    for ep, ep_dir, clips in episode_plan:
        CURRENT_EP_NUM = ep
        ep_folder_name = os.path.basename(ep_dir)
        print("\n" + "#" * 72)
        print(f"👉 BẮT ĐẦU TẬP {ep:02d} ({ep_folder_name}) — {len(clips)} CLIPS")
        print("#" * 72, flush=True)

        previous_clip_last_frame_media_id = None
        rendered_in_this_run = set()

        for c_idx, fpath in clips:
            CURRENT_CLIP_NUM = c_idx
            with open(fpath, "r", encoding="utf-8") as f:
                prompt_content = f.read().strip()

            completed_clips += 1
            progress_pct = (completed_clips / total_clips) * 100
            print(f"\n▶️ TIẾN ĐỘ TỔNG: [{completed_clips}/{total_clips}] ({progress_pct:.1f}%) — TẬP {ep:02d} - CLIP {c_idx:02d}", flush=True)

            res = run_clip_with_auto_retry(
                ep_num=ep,
                clip_num=c_idx,
                fpath=fpath,
                initial_prompt=prompt_content,
                start_image_media_id=None
            )

            if res["success"] and res.get("video_url"):
                video_url = res["video_url"]
                local_video = download_and_rename_video(video_url, ep, c_idx, ep_folder_name)
                if local_video:
                    rendered_in_this_run.add(c_idx)
                update_dashboard_scene_status(ep, c_idx, local_video if local_video else video_url)
            else:
                log(f"⚠️ [Tập {ep:02d} - Clip {c_idx:02d}] Bị bỏ qua do không hoàn tất render.")
                previous_clip_last_frame_media_id = None

            log("⏳ Nghỉ 5 giây trước khi tiếp tục clip kế tiếp...")
            time.sleep(5)

        # 🛡️ VÒNG LẶP VÉT CẠN: Đảm bảo 100% không bỏ sót bất kỳ clip nào của Tập trước khi ghép FULL
        existing_nums = rendered_in_this_run if ONLY_CLIP > 0 else {cn for cn, _ in find_episode_clip_mp4s(OUTPUT_VIDEOS_DIR, ep, ep_folder_name)}
        missing_clips = [(c_idx, fpath) for c_idx, fpath in clips if c_idx not in existing_nums]
        if missing_clips:
            log(f"🛡️ [CAM KẾT KHÔNG BỎ SÓT] Phát hiện Tập {ep:02d} còn thiếu {len(missing_clips)} clip. Đang đổi sang Ultra-Safe Prompt & render bù ngay!")
            for mc, fpath_m in missing_clips:
                CURRENT_CLIP_NUM = mc
                with open(fpath_m, "r", encoding="utf-8") as f:
                    raw_p = f.read().strip()
                ultra_safe_p = sanitize_prompt(raw_p, attempt=3)
                update_clip_file(fpath_m, ultra_safe_p)
                rec_res = run_clip_with_auto_retry(ep_num=ep, clip_num=mc, fpath=fpath_m, initial_prompt=ultra_safe_p, start_image_media_id=None, max_retries=4)
                if rec_res["success"] and rec_res.get("video_url"):
                    local_v = download_and_rename_video(rec_res["video_url"], ep, mc, ep_folder_name)
                    update_dashboard_scene_status(ep, mc, local_v if local_v else rec_res["video_url"])

        CURRENT_CLIP_NUM = None
        merge_episode_clips(SERIES_DIR, CHANNEL_SLUG, ep, ep_folder_name, project_id=PROJECT_ID)

    print("\n" + "=" * 72)
    print(f"🎉 HOÀN THÀNH TOÀN BỘ CHU TRÌNH TỪ TẬP {start_ep:02d} ĐẾN TẬP {end_ep:02d}!")
    print(f"📁 Video hoàn chỉnh (9:16) đã được lưu tại: {OUTPUT_VIDEOS_DIR}")
    print("=" * 72 + "\n", flush=True)


if __name__ == "__main__":
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    run_pipeline(start, end)
