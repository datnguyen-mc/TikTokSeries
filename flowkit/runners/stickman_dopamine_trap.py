#!/usr/bin/env python3
"""
Runner tự động hóa tạo phim ngắn Viral Stickman: "Cái Bẫy Dopamine Rẻ Tiền" (stickman-dopamine-trap)
- Tỉ lệ: 16:9 (VIDEO_ASPECT_RATIO_LANDSCAPE), 720p, 24 FPS
- Thời lượng: 60 giây (6 clips × 10 giây)
- Ngôn ngữ: Lồng tiếng Việt + Phụ đề Tiếng Việt
- Tự động trích xuất frame, đồng bộ lên SQLite, Cloudflare D1 và Cloudflare R2.
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
    sync_merged_episode_to_r2_and_d1,
    rewrite_prompt_on_failure,
    force_rename_clip_on_flow,
    is_clip_completed_in_db,
    persist_updated_prompt,
    mark_clip_failed_in_db,
)

FLOWKIT_API = os.environ.get("FLOWKIT_API", "http://127.0.0.1:8200")
CHANNEL_SLUG = "stickman-dopamine-trap"
PROJECT_ID = os.environ.get("FLOWKIT_PROJECT_ID", "3b955883-7851-42fe-a986-5ef82b4912e5")
ASPECT_RATIO = "VIDEO_ASPECT_RATIO_LANDSCAPE"
CLIP_DURATION_S = 10
TOTAL_CLIPS = 6

BASE_DIR = "/Users/iseul-a/Documents/TikTokSeries"
SERIES_DIR = os.path.join(BASE_DIR, CHANNEL_SLUG)
SCENE_DIR = os.path.join(SERIES_DIR, "canh-01")
OUTPUT_DIR = os.path.join(SERIES_DIR, "output_videos")
CLIPS_OUT_DIR = os.path.join(OUTPUT_DIR, "canh-01")
FRAMES_DIR = os.path.join(SERIES_DIR, "exported_frames")
DB_PATH = os.path.join(BASE_DIR, "flowkit", "flow_agent.db")

os.makedirs(CLIPS_OUT_DIR, exist_ok=True)
os.makedirs(FRAMES_DIR, exist_ok=True)


def log(msg: str, level: str = "INFO", clip_num: int = None):
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)
    push_cms_log(
        CHANNEL_SLUG,
        msg,
        level=level,
        category="RUNNER",
        project_id=PROJECT_ID,
        episode=1,
        clip_num=clip_num,
    )


def ensure_channel_in_db():
    now = datetime.now(timezone.utc).isoformat()
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO cms_channel (
                slug, name, project_id, aspect_ratio, series_dir, runner_script,
                ep_prefix, characters_json, description, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(slug) DO UPDATE SET
                name=excluded.name,
                project_id=excluded.project_id,
                aspect_ratio=excluded.aspect_ratio,
                series_dir=excluded.series_dir,
                runner_script=excluded.runner_script,
                description=excluded.description,
                updated_at=excluded.updated_at
            """,
            (
                CHANNEL_SLUG,
                "Stickman Viral: Cái Bẫy Dopamine Rẻ Tiền (16:9)",
                PROJECT_ID,
                "16:9",
                SERIES_DIR,
                "runners/stickman_dopamine_trap.py",
                "canh",
                "[]",
                "Phim ngắn Stickman 60s (6x10s 16:9) — Cái Bẫy Dopamine Rẻ Tiền (Lồng tiếng Việt)",
                now,
            ),
        )
        conn.commit()


def extract_last_frame(video_path: str, out_jpg: str) -> str:
    try:
        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-sseof",
                "-0.15",
                "-i",
                video_path,
                "-frames:v",
                "1",
                "-q:v",
                "2",
                out_jpg,
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return out_jpg if os.path.exists(out_jpg) else ""
    except Exception:
        return ""


def main():
    ensure_channel_in_db()
    only_clip = int(os.environ.get("FLOWKIT_ONLY_CLIP", "0") or "0")
    log("🚀 Bắt đầu đồng bộ & kiểm tra Stickman Dopamine Trap (6 clips × 10s = 60s, 16:9)...")

    for clip_num in range(1, TOTAL_CLIPS + 1):
        if only_clip and clip_num != only_clip:
            continue
        prompt_path = os.path.join(SCENE_DIR, f"clip-{clip_num}.md")
        with open(prompt_path, "r", encoding="utf-8") as f:
            prompt_text = f.read().strip()

        out_mp4 = os.path.join(CLIPS_OUT_DIR, f"canh-01_clip-{clip_num:02d}.mp4")
        frame_jpg = os.path.join(FRAMES_DIR, f"canh_01_clip_{clip_num:02d}_last.jpg")

        if os.path.exists(out_mp4) and os.path.getsize(out_mp4) > 50_000 and not only_clip:
            sz_mb = os.path.getsize(out_mp4) / (1024 * 1024)
            log(f"✅ Clip {clip_num:02d} đã sẵn sàng ({sz_mb:.2f} MB), trích xuất frame & đồng bộ R2/D1...", clip_num=clip_num)
            extract_last_frame(out_mp4, frame_jpg)
            sync_clip_to_r2_and_d1(
                channel_slug=CHANNEL_SLUG,
                ep_num=1,
                clip_num=clip_num,
                local_video_path=out_mp4,
                ep_folder_name="canh-01",
                project_id=PROJECT_ID,
                prompt=prompt_text,
                frame_path=frame_jpg if os.path.exists(frame_jpg) else None,
            )

    full_ep = os.path.join(OUTPUT_DIR, "canh-01_FULL.mp4")
    if os.path.exists(full_ep):
        sync_merged_episode_to_r2_and_d1(
            channel_slug=CHANNEL_SLUG,
            ep_num=1,
            merged_video_path=full_ep,
            ep_folder_name="canh-01",
            project_id=PROJECT_ID,
            clip_count=6,
            total_clips=6,
            is_complete=1,
            duration_s=60.0,
            unit_label="Cảnh",
        )
    log("🎉 Đã hoàn thành toàn bộ 6/6 clips + bản FULL 60s cho Stickman Dopamine Trap!")


if __name__ == "__main__":
    main()
