#!/usr/bin/env python3
"""
Runner tự động hóa tạo phim ngắn Stickman (Mode A · Director Mode — Style 4: Cozy Storytelling)
Dựa trên bộ chuẩn của repository `kaomei/stickman-video-director`:
- Tỉ lệ: 16:9 (VIDEO_ASPECT_RATIO_LANDSCAPE), 720p, 24 FPS
- Thời lượng: 60 giây (6 clips × 10 giây) trên Google Flow Omni Flash
- Tự động tải video về máy, ghép thành bản FULL 60s và đồng bộ lên Cloudflare D1 & R2.
"""

import os
import sys
import time
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
    force_rename_clip_on_flow,
    is_clip_completed_in_db,
    persist_updated_prompt,
    mark_clip_failed_in_db,
)

FLOWKIT_API = os.environ.get("FLOWKIT_API", "http://127.0.0.1:8200")
CHANNEL_SLUG = "stickman-cozy-story"
PROJECT_ID = os.environ.get("FLOWKIT_PROJECT_ID", "3b955883-7851-42fe-a986-5ef82b4912e5")
ASPECT_RATIO = "VIDEO_ASPECT_RATIO_LANDSCAPE"
CLIP_DURATION_S = 10
TOTAL_CLIPS = 6
ONLY_CLIP = int(os.environ.get("FLOWKIT_ONLY_CLIP", "0") or "0")

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SERIES_DIR = os.path.join(WORKSPACE_DIR, CHANNEL_SLUG)
PROMPTS_DIR = os.path.join(SERIES_DIR, "canh-01")
OUTPUT_VIDEOS_DIR = os.path.join(SERIES_DIR, "output_videos")
FRAMES_DIR = os.path.join(SERIES_DIR, "exported_frames")
DB_PATH = os.path.join(WORKSPACE_DIR, "flowkit", "flow_agent.db")

os.makedirs(PROMPTS_DIR, exist_ok=True)
os.makedirs(os.path.join(OUTPUT_VIDEOS_DIR, "canh-01"), exist_ok=True)
os.makedirs(FRAMES_DIR, exist_ok=True)


def log(msg: str, level: str = "INFO", clip_num: int = None):
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)
    try:
        push_cms_log(
            channel_slug=CHANNEL_SLUG,
            level=level,
            stage="STICKMAN_DIRECTOR",
            message=msg,
            episode=1,
            clip=clip_num,
        )
    except Exception:
        pass


def seed_channel_in_db():
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        """INSERT OR REPLACE INTO cms_channel
           (slug, name, project_id, aspect_ratio, series_dir, runner_script, ep_prefix, characters_json, description, updated_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            CHANNEL_SLUG,
            "Stickman Cozy Story — The Fake Rest Trap",
            PROJECT_ID,
            ASPECT_RATIO,
            CHANNEL_SLUG,
            "runners/stickman_cozy_story.py",
            "canh",
            "[]",
            "Phim ngắn hoạt hình Stickman 60s (16:9) theo chuẩn kaomei/stickman-video-director Style 4",
            now,
        ),
    )
    cur.execute(
        """INSERT OR REPLACE INTO cms_episode
           (id, channel_slug, project_id, episode_num, folder_name, label,
            total_clips, rendered_clips, is_complete, updated_at)
           VALUES (?, ?, ?, ?, ?, ?, ?,
                   COALESCE((SELECT rendered_clips FROM cms_episode WHERE id = ?), 0),
                   COALESCE((SELECT is_complete FROM cms_episode WHERE id = ?), 0),
                   ?)""",
        (
            f"{CHANNEL_SLUG}:ep:1",
            CHANNEL_SLUG,
            PROJECT_ID,
            1,
            "canh-01",
            "Phim Ngắn 60s — Why Resting Still Leaves You Exhausted",
            TOTAL_CLIPS,
            f"{CHANNEL_SLUG}:ep:1",
            f"{CHANNEL_SLUG}:ep:1",
            now,
        ),
    )
    for c_num in range(1, TOTAL_CLIPS + 1):
        p_file = os.path.join(PROMPTS_DIR, f"clip-{c_num}.md")
        p_text = open(p_file, "r", encoding="utf-8").read().strip() if os.path.isfile(p_file) else ""
        cid = f"{CHANNEL_SLUG}:ep:1:clip:{c_num}"
        cur.execute(
            """INSERT OR IGNORE INTO cms_clip
               (id, channel_slug, project_id, episode_num, folder_name, clip_num, prompt, status, updated_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, 'PENDING', ?)""",
            (cid, CHANNEL_SLUG, PROJECT_ID, 1, "canh-01", c_num, p_text, now),
        )
        if p_text:
            cur.execute("UPDATE cms_clip SET prompt = ?, updated_at = ? WHERE id = ?", (p_text, now, cid))
    conn.commit()
    conn.close()


def extract_last_frame(video_path: str, clip_num: int) -> str | None:
    out_jpg = os.path.join(FRAMES_DIR, f"canh_01_clip_{clip_num:02d}_last.jpg")
    try:
        subprocess.run(
            ["ffmpeg", "-y", "-sseof", "-0.15", "-i", video_path, "-vframes", "1", "-q:v", "2", out_jpg],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30,
        )
        if os.path.isfile(out_jpg) and os.path.getsize(out_jpg) > 0:
            return out_jpg
    except Exception:
        pass
    return None


def fetch_media_video_url(media_id: str) -> str | None:
    if not media_id:
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


def generate_single_clip(clip_num: int) -> bool:
    prompt_file = os.path.join(PROMPTS_DIR, f"clip-{clip_num}.md")
    if not os.path.isfile(prompt_file):
        log(f"❌ Không tìm thấy file prompt: {prompt_file}", "ERROR", clip_num)
        return False

    target_mp4 = os.path.join(OUTPUT_VIDEOS_DIR, "canh-01", f"canh-01_clip-{clip_num:02d}.mp4")
    if os.path.isfile(target_mp4) and os.path.getsize(target_mp4) > 100_000 and not ONLY_CLIP:
        log(f"✅ Clip {clip_num:02d} đã tồn tại trên máy ({os.path.getsize(target_mp4)/1048576:.2f} MB), bỏ qua.", "INFO", clip_num)
        return True

    prompt_text = open(prompt_file, "r", encoding="utf-8").read().strip()

    for attempt in range(1, 5):
        log(f"🎬 Đang gửi yêu cầu tạo Stickman Clip {clip_num:02d}/06 (Lần thử {attempt}/4)...", "INFO", clip_num)
        payload = {
            "prompt": prompt_text,
            "project_id": PROJECT_ID,
            "scene_id": f"stickman_cozy_01_{clip_num:02d}",
            "duration_s": CLIP_DURATION_S,
            "model_family": "omni_flash",
            "resolution": "720p",
            "aspect_ratio": ASPECT_RATIO,
        }
        try:
            resp = requests.post(f"{FLOWKIT_API}/api/flow/generate-video-omni-text", json=payload, timeout=240)
            if resp.status_code == 200:
                data = resp.json()
                media_id = data.get("media_id")
                video_url = data.get("video_url") or fetch_media_video_url(media_id)
                if not video_url and media_id:
                    for _ in range(18):
                        time.sleep(5)
                        video_url = fetch_media_video_url(media_id)
                        if video_url:
                            break
                if video_url:
                    if media_id:
                        force_rename_clip_on_flow(media_id, f"[STICKMAN COZY - CLIP {clip_num:02d}]", PROJECT_ID)
                    tmp_path = f"{target_mp4}.tmp"
                    r_dl = requests.get(video_url, stream=True, timeout=120)
                    if r_dl.status_code == 200:
                        with open(tmp_path, "wb") as f_out:
                            for chunk in r_dl.iter_content(chunk_size=1024 * 512):
                                if chunk:
                                    f_out.write(chunk)
                        os.replace(tmp_path, target_mp4)
                        frame_path = extract_last_frame(target_mp4, clip_num)
                        sync_clip_to_r2_and_d1(
                            channel_slug=CHANNEL_SLUG,
                            ep_num=1,
                            clip_num=clip_num,
                            local_video_path=target_mp4,
                            frame_path=frame_path,
                            ep_folder_name="canh-01",
                            project_id=PROJECT_ID,
                        )
                        log(f"🎉 Hoàn thành Stickman Clip {clip_num:02d}/06 -> {target_mp4}", "SUCCESS", clip_num)
                        return True
            else:
                err_txt = resp.text[:300]
                log(f"⚠️ Lỗi HTTP {resp.status_code} khi tạo Clip {clip_num:02d}: {err_txt}", "WARN", clip_num)
                if resp.status_code == 503 and "Extension not connected" in err_txt:
                    log("⏳ Chrome Extension Google Flow chưa kết nối tới cổng 8200. Vui lòng mở tab Google Flow trên Chrome!", "WARN", clip_num)
                    return False
                if wait_if_cooldown_error(err_txt, log_fn=lambda m: log(m, "WARN", clip_num)):
                    continue
                new_p = rewrite_prompt_on_failure(prompt_text, attempt=attempt, aspect_ratio=ASPECT_RATIO)
                if new_p and new_p != prompt_text:
                    prompt_text = new_p
                    persist_updated_prompt(CHANNEL_SLUG, 1, clip_num, prompt_text, prompt_file=prompt_file)
        except Exception as e:
            log(f"⚠️ Ngoại lệ khi tạo Clip {clip_num:02d}: {e}", "WARN", clip_num)
        time.sleep(8)

    mark_clip_failed_in_db(CHANNEL_SLUG, 1, clip_num, "Failed after 4 attempts")
    return False


def main():
    seed_channel_in_db()
    log("🚀 Bắt đầu chạy Stickman Cozy Story (6 clips × 10s = 60s, 16:9)...")
    clips_to_run = [ONLY_CLIP] if ONLY_CLIP > 0 else list(range(1, TOTAL_CLIPS + 1))
    all_ok = True
    for c_num in clips_to_run:
        ok = generate_single_clip(c_num)
        if not ok:
            all_ok = False
        time.sleep(4)
    if all_ok:
        log("🎉 Đã hoàn thành toàn bộ 6/6 clips cho phim ngắn Stickman Cozy Story!", "SUCCESS")


if __name__ == "__main__":
    main()
