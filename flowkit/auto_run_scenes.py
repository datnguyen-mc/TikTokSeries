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
WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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

def extract_last_frame(video_source: str, scene_num: int, clip_num: int) -> str:
    out_frame = os.path.join(FRAMES_DIR, f"scene_{scene_num:02d}_clip_{clip_num:02d}_last.jpg")
    log(f"🎬 Dùng ffmpeg cắt khung hình cuối (Last Frame) của Clip {clip_num}...")
    try:
        cmd = [
            "ffmpeg", "-y",
            "-sseof", "-0.1",
            "-i", video_source,
            "-vsync", "0",
            "-vframes", "1",
            "-q:v", "2",
            out_frame
        ]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=45)
        if result.returncode == 0 and os.path.exists(out_frame) and os.path.getsize(out_frame) > 0:
            log(f"✨ Cắt thành công khung hình nối cảnh: {os.path.basename(out_frame)}")
            return out_frame
        else:
            log(f"⚠️ ffmpeg không trích xuất được frame: {result.stderr.decode('utf-8', errors='ignore')[:200]}")
            return None
    except Exception as e:
        log(f"⚠️ Lỗi khi trích xuất frame: {e}")
        return None

def upload_start_frame(image_path: str) -> str:
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
            media_id = res.json().get("data", {}).get("media_id") or res.json().get("media_id")
            log(f"📤 Đã nạp ảnh vào slot [Bắt đầu] cho Clip tiếp theo (media_id: {media_id})")
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
    if start_image_media_id:
        endpoint = "/api/flow/generate-video"
        mode = "🔗 Image-to-Video (Seamless Start Frame Chaining)"
        payload = {
            "start_image_media_id": start_image_media_id,
            "prompt": prompt,
            "project_id": PROJECT_ID,
            "duration_s": 8,
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
            "duration_s": 8,
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
            ("Thời Lượng", "8 giây (Omni Flash / Veo)"),
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

def poll_workflow(workflows, scene_num: int, clip_num: int, timeout_s=240):
    url = f"{FLOWKIT_API}/api/flow/check-status"
    start_time = time.time()
    log(f"⏳ Đang theo dõi tiến trình tạo video [Cảnh {scene_num:02d} - Clip {clip_num:02d}]...")
    
    while time.time() - start_time < timeout_s:
        try:
            r = requests.post(url, json={"workflows": workflows, "project_id": PROJECT_ID}, timeout=30)
            if r.status_code == 200:
                res_data = r.json()
                st = res_data.get("status")
                elapsed = int(time.time() - start_time)
                if st == "COMPLETED":
                    log(f"🎉 Google Flow render hoàn tất sau {elapsed}s!")
                    video_url = None
                    wf_list = res_data.get("workflows") or []
                    for wf in wf_list:
                        m = wf.get("media") or {}
                        if m.get("url"):
                            video_url = m["url"]
                            break
                    return {"success": True, "video_url": video_url}
                elif st in ["FAILED", "ERROR"]:
                    log(f"❌ Google Flow báo lỗi: {res_data}")
                    return {"success": False, "error": "FLOW_FAILED"}
                else:
                    if elapsed % 12 == 0:
                        log(f"   ...Google Flow đang vẽ video ({elapsed}s, status: {st})...")
            else:
                log(f"   ...chờ phản hồi (HTTP {r.status_code})...")
        except Exception as e:
            log(f"   ...lỗi tạm thời khi poll: {e}")
            
        time.sleep(6)
        
    log("⚠️ Hết thời gian chờ (timeout).")
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
                inner = data.get("data", {})
                workflows = inner.get("workflows") or []
                media_id = inner.get("media", [{}])[0].get("name", "N/A")
                log(f"✅ Google Flow đã nhận job (Media ID: {media_id}).")
                
                if workflows:
                    poll_res = poll_workflow(workflows, scene_num, clip_num)
                    if poll_res["success"]:
                        return poll_res
                    else:
                        log(f"⚠️ Render thất bại ở lần thử {attempt}.")
                else:
                    time.sleep(70)
                    return {"success": True, "video_url": None}
            else:
                log(f"❌ Google Flow phản hồi lỗi (HTTP {res.status_code}): {res.text}")
        except Exception as e:
            log(f"❌ Lỗi ngoại lệ: {e}")

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
    print(f"📁 Phạm vi: Cảnh {start_scene:02d} đến Cảnh {end_scene:02d}")
    print(f"🔗 Google Flow Project: {PROJECT_ID}")
    print(f"💾 Tải video tự động về: {OUTPUT_VIDEOS_DIR}")
    print("="*72 + "\n")

    if not check_connection():
        sys.exit(1)

    # Đồng bộ với Dashboard UI
    sync_dashboard_database()

    total_clips = (end_scene - start_scene + 1) * 6
    completed_clips = 0
    previous_clip_last_frame_media_id = None

    for s in range(start_scene, end_scene + 1):
        print("\n" + "#"*72)
        print(f"👉 BẮT ĐẦU CẢNH {s:02d}")
        print("#"*72)
        
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
            
            if res["success"]:
                video_url = res.get("video_url")
                
                if video_url:
                    # 1. TẢI NGAY LẬP TỨC VỀ MÁY VÀ ĐỔI TÊN CHUẨN
                    local_video = download_and_rename_video(video_url, s, c_idx)
                    source_for_frame = local_video if local_video else video_url
                    
                    # 2. CẬP NHẬT TRẠNG THÁI VÀ LINK VIDEO LÊN DASHBOARD UI
                    update_dashboard_scene_status(s, c_idx, local_video if local_video else video_url)
                    
                    # 3. TRÍCH XUẤT LAST FRAME LÀM START FRAME CHO CLIP TIẾP THEO
                    last_frame_path = extract_last_frame(source_for_frame, s, c_idx)
                    if last_frame_path:
                        previous_clip_last_frame_media_id = upload_start_frame(last_frame_path)
                    else:
                        previous_clip_last_frame_media_id = None
                else:
                    previous_clip_last_frame_media_id = None
            else:
                log(f"⚠️ [Cảnh {s:02d} - Clip {c_idx}] Bị bỏ qua sau 3 lần thử.")
                previous_clip_last_frame_media_id = None

            log("⏳ Nghỉ 5 giây trước khi tiếp tục...")
            time.sleep(5)

    print("\n" + "="*72)
    print(f"🎉 HOÀN THÀNH TOÀN BỘ CHU TRÌNH TỪ CẢNH {start_scene:02d} ĐẾN CẢNH {end_scene:02d}!")
    print(f"📁 Video hoàn chỉnh đã được lưu tại: {OUTPUT_VIDEOS_DIR}")
    print("="*72 + "\n")

if __name__ == "__main__":
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    run_pipeline(start, end)
