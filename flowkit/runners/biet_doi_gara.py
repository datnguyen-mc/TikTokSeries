#!/usr/bin/env python3
"""
HỆ THỐNG TỰ ĐỘNG HÓA FLOWKIT NÂNG CAO CHO "BIỆT ĐỘI GARA":
1. Tự động chạy liên tiếp từ Cảnh 03 đến Cảnh 05 (18 clips).
2. Tải ngay lập tức video về máy tính khi hoàn thành và đổi tên chuẩn theo cảnh.
3. Chi tiết hóa toàn bộ API Request Logs (endpoint, mode, params khung hình Bắt đầu / Kết thúc).
4. Tự động đồng bộ thời gian thực với Console Dashboard UI.
5. Tự động trích xuất khung hình cuối (last frame) làm khung hình đầu (start frame) của clip sau (Seamless Chaining).
6. Tự động làm sạch prompt khi gặp lỗi chính sách / bản quyền và Auto-Retry.
"""

import os
import sys
import time
import json
import base64
import subprocess
import requests
from datetime import datetime

FLOWKIT_API = "http://127.0.0.1:8200"
PROJECT_ID = "30714c49-2878-439b-a46f-c52be6eee2fc"
WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SERIES_DIR = os.path.join(WORKSPACE_DIR, "biet-doi-gara")
FRAMES_DIR = os.path.join(SERIES_DIR, "exported_frames")
OUTPUT_VIDEOS_DIR = os.path.join(SERIES_DIR, "output_videos")

os.makedirs(FRAMES_DIR, exist_ok=True)
os.makedirs(OUTPUT_VIDEOS_DIR, exist_ok=True)

# Bản đồ lưu scene_id trong database để đồng bộ với Dashboard UI
SCENE_DB_MAP = {}
CURRENT_VIDEO_ID = None

def log(msg):
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] {msg}", flush=True)

def print_box(title, items, border_char="─"):
    width = 72
    print(f"\n┌─ {title} " + border_char * (width - len(title) - 5) + "┐")
    for k, v in items:
        prefix = f"│ • {k}: "
        val_str = str(v)
        # Handle wrap if too long
        if len(prefix) + len(val_str) > width - 2:
            val_display = val_str[:width - len(prefix) - 5] + "..."
        else:
            val_display = val_str
        spacing = " " * (width - len(prefix) - len(val_display) - 1)
        print(f"{prefix}{val_display}{spacing}│")
    print("└" + border_char * (width - 2) + "┘")

def check_connection():
    try:
        r = requests.get(f"{FLOWKIT_API}/health", timeout=5)
        data = r.json()
        if not data.get("extension_connected"):
            log("⚠️ FlowKit server đang chạy nhưng Chrome Extension chưa kết nối!")
            log(f"👉 Mở Chrome có cài Extension và giữ mở tab https://flow.google.com/project/{PROJECT_ID}")
            return False
        log("✅ FlowKit & Chrome Extension đang kết nối tốt!")
        return True
    except Exception as e:
        log(f"❌ Không kết nối được tới FlowKit API ({FLOWKIT_API}): {e}")
        return False

# -------------------------------------------------------------
# 1. ĐỒNG BỘ DỰ ÁN VỚI DASHBOARD UI (DATABASE SYNC)
# -------------------------------------------------------------
def sync_dashboard_database():
    """Tự động tạo hoặc kiểm tra Project, Video, Scenes trong FlowKit DB để Dashboard luôn có data."""
    global CURRENT_VIDEO_ID, SCENE_DB_MAP
    log("🔄 Đang đồng bộ cơ sở dữ liệu với Dashboard UI...")
    
    # 1. Đảm bảo Project tồn tại
    try:
        r = requests.get(f"{FLOWKIT_API}/api/projects", timeout=5)
        projects = r.json() if r.status_code == 200 else []
        proj_exists = any(p.get("id") == PROJECT_ID for p in projects)
        if not proj_exists:
            log("   ...Đang đăng ký dự án 'Biệt Đội Gara' vào hệ thống...")
            p_payload = {
                "name": "Biệt Đội Gara",
                "flow_project_id": PROJECT_ID,
                "material": "realistic",
                "story": "Biệt đội thợ máy Sài Gòn khám phá thiết bị công nghệ và bảo vệ bức thư quan trọng.",
                "characters": [
                    {"name": "Thắng", "description": "Thắng, 36 tuổi, thợ máy điềm đạm dũng cảm"},
                    {"name": "Lan", "description": "Lan, 29 tuổi, nữ quái xế nhanh nhẹn, cá tính"},
                    {"name": "Hải", "description": "Hải, 32 tuổi, thợ máy to lớn, vui tính"},
                    {"name": "Khôi", "description": "Khôi, 24 tuổi, thiên tài công nghệ IT"}
                ]
            }
            requests.post(f"{FLOWKIT_API}/api/projects", json=p_payload, timeout=10)

        # 2. Đảm bảo Video (Tập phim) tồn tại
        r_v = requests.get(f"{FLOWKIT_API}/api/videos?project_id={PROJECT_ID}", timeout=5)
        videos = r_v.json() if r_v.status_code == 200 else []
        if videos:
            CURRENT_VIDEO_ID = videos[0]["id"]
        else:
            v_payload = {
                "project_id": PROJECT_ID,
                "title": "Biệt Đội Gara - Phần 1 (Cảnh 03 - 05)",
                "description": "Truy tìm bức thư quan trọng và kích hoạt vòng tay công nghệ",
                "orientation": "HORIZONTAL"
            }
            res_v = requests.post(f"{FLOWKIT_API}/api/videos", json=v_payload, timeout=10)
            if res_v.status_code == 200:
                CURRENT_VIDEO_ID = res_v.json().get("id")

        # 3. Đảm bảo 18 Scenes tồn tại
        if CURRENT_VIDEO_ID:
            r_s = requests.get(f"{FLOWKIT_API}/api/scenes?video_id={CURRENT_VIDEO_ID}", timeout=5)
            existing_scenes = r_s.json() if r_s.status_code == 200 else []
            
            order = 0
            for s in [3, 4, 5]:
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
                            "prompt": f"Cảnh {s:02d} - Clip {c}",
                            "video_prompt": prompt_preview,
                            "character_names": ["Thắng", "Lan", "Hải", "Khôi"]
                        }
                        r_new = requests.post(f"{FLOWKIT_API}/api/scenes", json=sc_payload, timeout=5)
                        if r_new.status_code == 200:
                            SCENE_DB_MAP[key] = r_new.json().get("id")
                    order += 1
                    
        log(f"✅ Đã đồng bộ Dashboard DB thành công! ({len(SCENE_DB_MAP)} scenes sẵn sàng)")
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
            "horizontal_video_status": "COMPLETED"
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
    p = prompt
    ip_replacements = {
        "superhero blockbuster": "photorealistic Vietnamese cinematic action film",
        "superhero": "high-tech specialist",
        "hollywood cinematography": "high-end cinema 24fps",
        "Hollywood": "cinematic",
        "marvel": "mechanic",
        "power ranger": "elite team",
        "alien technology": "advanced automotive engineering prototype",
        "alien": "experimental",
    }
    for k, v in ip_replacements.items():
        p = p.replace(k, v)
        p = p.replace(k.title(), v.title())

    violence_replacements = {
        "ghim vào cổ tay": "nhẹ nhàng khóa quanh cổ tay thành vòng tay",
        "ghim": "khóa nhẹ",
        "đâm": "lướt tới",
        "chém": "gạt đòn",
        "tước vũ khí": "thu hồi thiết bị",
        "tước": "thu hồi",
        "đánh nhau dằn co": "dồn dập tranh chấp công nghệ",
        "đánh nhau": "tranh chấp kỹ thuật",
        "bắn": "phát xung sáng",
        "vũ khí": "công cụ kỹ thuật",
        "hạ gục": "hóa giải",
        "chết": "bất ngờ",
        "máu": "vệt dầu máy",
    }
    for k, v in violence_replacements.items():
        p = p.replace(k, v)

    if attempt >= 2:
        p = p.replace("tranh chấp", "tương tác kỹ thuật")
        p = p.replace("áp sát dồn dập", "chuyển động nhịp nhàng")
        p = p.replace("gắt gao", "tập trung cao độ")
        
    return p

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
    """Tải ngay lập tức video về máy và đổi tên chuẩn theo cảnh."""
    scene_folder = os.path.join(OUTPUT_VIDEOS_DIR, f"canh-{scene_num:02d}")
    os.makedirs(scene_folder, exist_ok=True)
    
    filename = f"canh-{scene_num:02d}_clip-{clip_num:02d}.mp4"
    target_path = os.path.join(scene_folder, filename)
    
    log(f"📥 Đang tải video từ Google Flow về máy...")
    try:
        r = requests.get(video_url, stream=True, timeout=120)
        if r.status_code == 200:
            with open(target_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=1024*1024):
                    if chunk:
                        f.write(chunk)
            size_mb = os.path.getsize(target_path) / (1024 * 1024)
            print_box(
                "💾 CLIP HOÀN THÀNH & ĐÃ TẢI VỀ MÁY",
                [
                    ("Tên File Mới", filename),
                    ("Đường Dẫn Lưu", target_path),
                    ("Dung Lượng", f"{size_mb:.2f} MB"),
                    ("Thời Gian Hoàn Tất", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                ]
            )
            return target_path
        else:
            log(f"⚠️ Lỗi khi tải video (HTTP {r.status_code})")
    except Exception as e:
        log(f"⚠️ Ngoại lệ khi tải video: {e}")
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
    except Exception as e:
        pass
    return None

def extract_last_frame(video_source: str, scene_num: int, clip_num: int) -> str:
    """Trích xuất khung hình cuối cùng của clip bằng ffmpeg làm start frame cho clip sau."""
    out_frame = os.path.join(FRAMES_DIR, f"scene_{scene_num:02d}_clip_{clip_num:02d}_last.jpg")
    log(f"🎬 Dùng ffmpeg cắt khung hình cuối (Last Frame) của Cảnh {scene_num:02d} - Clip {clip_num:02d}...")
    try:
        # Cách 1: dùng -sseof -0.2 lấy frame sát cuối video
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
            # Cách 2: fallback seek trực tiếp giây thứ 9.5
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
# 4. GỬI API REQUEST & LOG CHI TIẾT PARAMS
# -------------------------------------------------------------
def submit_clip_with_detailed_log(prompt: str, scene_num: int, clip_num: int, start_image_media_id: str = None):
    """Gửi yêu cầu tạo video và in đầy đủ thông tin params request ra CLI."""
    key = f"canh_{scene_num:02d}_clip_{clip_num:02d}"
    sid = SCENE_DB_MAP.get(key) or f"scene_{scene_num:02d}_clip_{clip_num:02d}"

    if start_image_media_id:
        endpoint = "/api/flow/generate-video"
        mode = "🔗 Image-to-Video (Seamless Start Frame Chaining)"
        payload = {
            "start_image_media_id": start_image_media_id,
            "prompt": prompt,
            "project_id": PROJECT_ID,
            "scene_id": sid,
            "duration_s": 10,
            "model_family": "omni_flash",
            "resolution": "720p",
            "aspect_ratio": "VIDEO_ASPECT_RATIO_LANDSCAPE"
        }
    else:
        endpoint = "/api/flow/generate-video-omni-text"
        mode = "🎬 Text-to-Video (Khung hình gốc mở đầu cảnh)"
        payload = {
            "prompt": prompt,
            "project_id": PROJECT_ID,
            "scene_id": sid,
            "duration_s": 10,
            "resolution": "720p",
            "aspect_ratio": "VIDEO_ASPECT_RATIO_LANDSCAPE"
        }

    # IN LOG CHI TIẾT API REQUEST RA CLI
    print_box(
        "📡 FLOWKIT API REQUEST CALL",
        [
            ("Endpoint API", f"POST {endpoint}"),
            ("Phân Cảnh", f"Cảnh {scene_num:02d} - Clip {clip_num:02d}"),
            ("Chế Độ Tạo", mode),
            ("Slot [Bắt Đầu]", start_image_media_id if start_image_media_id else "[Trống - Khởi tạo từ Text]"),
            ("Slot [Kết Thúc]", "[Trống - Chuyển động tự do]"),
            ("Thời Lượng", "10 giây (Omni Flash abra_10s)"),
            ("Độ Phân Giải", "720p HD"),
            ("Tỉ Lệ Khung Hình", "LANDSCAPE (16:9 Widescreen)"),
            ("Model Family", "omni_flash"),
            ("Độ Dài Prompt", f"{len(prompt)} ký tự"),
            ("Prompt Preview", prompt[:120].replace("\n", " ") + "..."),
        ]
    )

    url = f"{FLOWKIT_API}{endpoint}"
    res = requests.post(url, json=payload, timeout=60)
    return res

def poll_generation(submit_res_data: dict, scene_num: int, clip_num: int, timeout_s=360):
    """
    Theo dõi tiến trình sinh video cho đến khi hoàn thành.
    Tự động xử lý cả hai cơ chế của Google Flow:
    1. workflows (Text-to-Video)
    2. operations (Image-to-Video có khung hình đầu)
    """
    url = f"{FLOWKIT_API}/api/flow/check-status"
    start_time = time.time()
    
    # Trích xuất thông tin polling
    flow_poll = submit_res_data.get("flowkitPolling") or {}
    workflows = submit_res_data.get("workflows") or flow_poll.get("workflows") or []
    operations = submit_res_data.get("operations") or flow_poll.get("operations") or []
    media_list = submit_res_data.get("media") or []
    primary_media_id = None
    if media_list and isinstance(media_list, list) and len(media_list) > 0:
        primary_media_id = media_list[0].get("name")
    if not primary_media_id and workflows:
        primary_media_id = workflows[0].get("primary_media_id")

    poll_mode_desc = "workflows (Text-to-Video)" if workflows else ("operations (Image-to-Video)" if operations else "direct media")
    log(f"⏳ Đang theo dõi tiến trình tạo video [Cảnh {scene_num:02d} - Clip {clip_num:02d}] (Chế độ: {poll_mode_desc})...")

    last_logged_time = 0
    while time.time() - start_time < timeout_s:
        elapsed = int(time.time() - start_time)
        try:
            # 1. Nếu có workflows (Text-to-Video Omni)
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
                        # Nếu trong wf chưa có url, gọi trực tiếp endpoint media
                        if not video_url and primary_media_id:
                            video_url = fetch_media_video_url(primary_media_id)
                        if video_url:
                            return {"success": True, "video_url": video_url}
                    elif st in ["FAILED", "ERROR"]:
                        log(f"❌ Google Flow báo lỗi: {res_data}")
                        return {"success": False, "error": "FLOW_FAILED"}
            
            # 2. Nếu có operations (Image-to-Video Omni)
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
                        log(f"🎉 Google Flow Image-to-Video hoàn tất sau {elapsed}s!")
                        target_mid = op_media_id or primary_media_id
                        if not video_url and target_mid:
                            video_url = fetch_media_video_url(target_mid)
                        if video_url:
                            return {"success": True, "video_url": video_url}

            # 3. Fallback: Nếu có primary_media_id, kiểm tra trực tiếp qua Media API
            if primary_media_id and elapsed >= 30:
                direct_url = fetch_media_video_url(primary_media_id)
                if direct_url:
                    log(f"🎉 Phát hiện video sẵn sàng qua Media API sau {elapsed}s!")
                    return {"success": True, "video_url": direct_url}

            # Log tiến trình định kỳ mỗi 12 giây
            if elapsed - last_logged_time >= 12:
                last_logged_time = elapsed
                log(f"   ...Google Flow đang vẽ video ({elapsed}s trôi qua)...")

        except Exception as e:
            log(f"   ...lỗi tạm thời khi poll ({e}), tiếp tục chờ...")

        time.sleep(6)

    log(f"⚠️ Hết thời gian chờ {timeout_s}s (Timeout) khi render Cảnh {scene_num:02d} - Clip {clip_num:02d}.")
    return {"success": False, "error": "TIMEOUT"}

# -------------------------------------------------------------
# 5. CHU TRÌNH ĐIỀU PHỐI TỔNG THỂ
# -------------------------------------------------------------
def run_clip_with_auto_retry(scene_num: int, clip_num: int, initial_prompt: str, start_image_media_id: str = None, max_retries: int = 3):
    current_prompt = initial_prompt
    
    for attempt in range(1, max_retries + 1):
        if attempt > 1:
            log(f"🔄 Đang thử lại lần {attempt}/{max_retries} sau khi làm sạch prompt...")
        
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
                log(f"❌ Google Flow phản hồi lỗi (HTTP {res.status_code}): {res.text}")
        except Exception as e:
            log(f"❌ Lỗi ngoại lệ khi gửi job: {e}")

        # TỰ ĐỘNG LÀM SẠCH PROMPT & THỬ LẠI
        if attempt < max_retries:
            log(f"🔧 [Tự động sửa] Đang khử từ khóa nhạy cảm / bạo lực lần {attempt}...")
            current_prompt = sanitize_prompt(current_prompt, attempt)
            update_clip_file(scene_num, clip_num, current_prompt)
            if attempt == 2 and start_image_media_id:
                log("🔄 Thử chuyển sang chế độ độc lập nếu khung hình đầu gặp giới hạn...")
                start_image_media_id = None
            log("⏳ Nghỉ 8 giây trước khi thử lại...")
            time.sleep(8)
            
    return {"success": False, "video_url": None}

def run_pipeline(start_scene=3, end_scene=5):
    print("\n" + "="*72)
    print("🎬 KHỞI ĐỘNG HỆ THỐNG FLOWKIT TỰ ĐỘNG THÔNG MINH — BIỆT ĐỘI GARA")
    print(f"📁 Phạm vi: Cảnh {start_scene:02d} đến Cảnh {end_scene:02d} (6 clips/cảnh)")
    print(f"🔗 Google Flow Project: {PROJECT_ID}")
    print(f"💾 Tải video tự động về: {OUTPUT_VIDEOS_DIR}")
    print(f"🖼️ Lưu khung hình nối cảnh tại: {FRAMES_DIR}")
    print("="*72 + "\n")

    if not check_connection():
        sys.exit(1)

    # Đồng bộ với Dashboard UI
    sync_dashboard_database()

    total_clips = (end_scene - start_scene + 1) * 6
    completed_clips = 0

    for s in range(start_scene, end_scene + 1):
        print("\n" + "#"*72)
        print(f"👉 BẮT ĐẦU CẢNH {s:02d}")
        print("#"*72)
        
        # Clip 1 của mỗi cảnh mới bắt đầu bối cảnh mới (khởi tạo từ Text hoặc Reference)
        previous_clip_last_frame_media_id = None
        
        scene_dir = os.path.join(SERIES_DIR, f"canh-{s:02d}")
        for c_idx in range(1, 7):
            fpath = os.path.join(scene_dir, f"clip-{c_idx}.md")
            if not os.path.exists(fpath):
                continue
                
            with open(fpath, "r", encoding="utf-8") as f:
                prompt_content = f.read().strip()
                
            completed_clips += 1
            progress_pct = (completed_clips / total_clips) * 100
            print(f"\n▶️ TIẾN ĐỘ TỔNG: [{completed_clips}/{total_clips}] ({progress_pct:.1f}%) — CẢNH {s:02d} - CLIP {c_idx:02d}")
            
            res = run_clip_with_auto_retry(
                scene_num=s,
                clip_num=c_idx,
                initial_prompt=prompt_content,
                start_image_media_id=previous_clip_last_frame_media_id
            )
            
            if res["success"] and res.get("video_url"):
                video_url = res["video_url"]
                
                # 1. TẢI NGAY LẬP TỨC VỀ MÁY VÀ ĐỔI TÊN CHUẨN
                local_video = download_and_rename_video(video_url, s, c_idx)
                
                # 2. CẬP NHẬT TRẠNG THÁI VÀ LINK VIDEO LÊN DASHBOARD UI
                update_dashboard_scene_status(s, c_idx, local_video if local_video else video_url)
                
                # 3. TRÍCH XUẤT LAST FRAME LÀM START FRAME CHO CLIP TIẾP THEO
                source_for_frame = local_video if local_video else video_url
                last_frame_path = extract_last_frame(source_for_frame, s, c_idx)
                if last_frame_path:
                    previous_clip_last_frame_media_id = upload_start_frame(last_frame_path)
                else:
                    previous_clip_last_frame_media_id = None
            else:
                log(f"⚠️ [Cảnh {s:02d} - Clip {c_idx:02d}] Bị bỏ qua do không hoàn tất render.")
                previous_clip_last_frame_media_id = None

            log("⏳ Nghỉ 5 giây trước khi tiếp tục clip kế tiếp...")
            time.sleep(5)

    print("\n" + "="*72)
    print(f"🎉 HOÀN THÀNH TOÀN BỘ CHU TRÌNH TỪ CẢNH {start_scene:02d} ĐẾN CẢNH {end_scene:02d}!")
    print(f"📁 Video hoàn chỉnh đã được lưu tại: {OUTPUT_VIDEOS_DIR}")
    print("="*72 + "\n")

if __name__ == "__main__":
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    run_pipeline(start, end)
