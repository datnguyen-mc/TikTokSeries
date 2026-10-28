#!/usr/bin/env python3
"""
Module tích hợp CMS & Tự động ghép tập hoàn chỉnh (Auto Episode Merger + Real-time CMS Logger)
Dùng chung cho toàn bộ 6 series runners và CMS Backend.
"""

import os
import re
import json
import shutil
import tempfile
import subprocess
import requests
from datetime import datetime

os.environ["NO_PROXY"] = "127.0.0.1,localhost"
os.environ["no_proxy"] = "127.0.0.1,localhost"
FLOWKIT_API = os.environ.get("FLOWKIT_API", "http://127.0.0.1:8200")
_VALID_LEVELS = {"INFO", "SUCCESS", "WARN", "WARNING", "ERROR", "DEBUG"}


def push_cms_log(
    channel_slug: str,
    arg2: str = "INFO",
    arg3: str = "RUNNER",
    arg4: str = None,
    project_id: str = None,
    episode: int = None,
    clip_num: int = None,
    details: dict = None,
    level: str = None,
    category: str = None,
    message: str = None,
):
    """Đẩy log thời gian thực về CMS Database & WebSocket (hỗ trợ cả 2 thứ tự tham số)."""
    try:
        if arg4 is not None:
            # Called as push_cms_log(channel_slug, level, category, message, ...)
            eff_level = level or arg2
            eff_cat = category or arg3
            eff_msg = message or arg4
        elif arg2.upper() in _VALID_LEVELS and message is not None:
            eff_level = level or arg2
            eff_cat = category or arg3
            eff_msg = message
        else:
            # Called as push_cms_log(channel_slug, message, level=..., category=...)
            eff_msg = message or arg2
            eff_level = level or (arg3 if arg3.upper() in _VALID_LEVELS else "INFO")
            eff_cat = category or ("RUNNER" if arg3.upper() in _VALID_LEVELS else arg3)

        payload = {
            "channel_slug": channel_slug,
            "project_id": project_id,
            "episode": episode,
            "clip_num": clip_num,
            "level": eff_level.upper(),
            "category": eff_cat,
            "message": eff_msg,
            "details": details,
        }
        requests.post(f"{FLOWKIT_API}/api/cms/logs", json=payload, timeout=3)
    except Exception:
        pass


def _extract_clip_number_from_filename(fname: str) -> int:
    """Trích xuất số thứ tự clip từ tên file mp4 (clip-01.mp4, _C01.mp4, clip_01.mp4...)."""
    m = re.search(r"(?:clip[-_]|_C)(\d+)\.mp4$", fname, re.IGNORECASE)
    if m:
        return int(m.group(1))
    m2 = re.search(r"(\d+)\.mp4$", fname)
    if m2:
        return int(m2.group(1))
    return 9999


def find_episode_clip_mp4s(output_videos_dir: str, ep_num: int, ep_folder_name: str = None) -> list[tuple[int, str]]:
    """
    Tìm tất cả các file mp4 clip nhỏ thuộc Tập / Cảnh ep_num, sắp xếp theo đúng thứ tự clip 1 -> N.
    Loại bỏ các file *_FULL.mp4 để không ghép trùng.
    """
    candidate_dirs = []
    if ep_folder_name:
        candidate_dirs.append(os.path.join(output_videos_dir, ep_folder_name))
    candidate_dirs.extend([
        os.path.join(output_videos_dir, f"tap-{ep_num}"),
        os.path.join(output_videos_dir, f"tap-{ep_num:02d}"),
        os.path.join(output_videos_dir, f"tap{ep_num}"),
        os.path.join(output_videos_dir, f"canh-{ep_num:02d}"),
        os.path.join(output_videos_dir, f"canh-{ep_num}"),
    ])
    if os.path.isdir(output_videos_dir):
        for name in os.listdir(output_videos_dir):
            full_sub = os.path.join(output_videos_dir, name)
            if os.path.isdir(full_sub) and re.match(rf"^(?:tap|canh)[-_]?0*{ep_num}(?:[-_]|$)", name, re.IGNORECASE):
                if full_sub not in candidate_dirs:
                    candidate_dirs.append(full_sub)

    found_by_clip_num: dict[int, str] = {}
    for d in candidate_dirs:
        if not os.path.isdir(d):
            continue
        for fname in os.listdir(d):
            if not fname.lower().endswith(".mp4"):
                continue
            if "full" in fname.lower() or "merged" in fname.lower():
                continue
            fpath = os.path.join(d, fname)
            if not os.path.isfile(fpath) or os.path.getsize(fpath) == 0:
                continue
            c_num = _extract_clip_number_from_filename(fname)
            if c_num not in found_by_clip_num:
                found_by_clip_num[c_num] = fpath

    return sorted(found_by_clip_num.items(), key=lambda x: x[0])


def probe_video_duration(video_path: str) -> float:
    """Lấy thời lượng video (giây) qua ffprobe."""
    try:
        res = subprocess.run(
            [
                "ffprobe", "-v", "quiet",
                "-show_entries", "format=duration",
                "-of", "csv=p=0",
                video_path,
            ],
            capture_output=True,
            text=True,
            timeout=20,
        )
        return round(float(res.stdout.strip()), 2)
    except Exception:
        return 0.0


def merge_episode_clips(
    series_dir: str,
    channel_slug: str,
    ep_num: int,
    ep_folder_name: str = None,
    project_id: str = None,
    unit_label: str = "Tập",
) -> dict:
    """
    Tự động ghép toàn bộ các clip nhỏ của Tập/Cảnh ep_num thành 1 video hoàn chỉnh:
    - Lưu tại: <series_dir>/output_videos/<ep_folder>/<channel_slug>_tap-XX_FULL.mp4
    - Đồng thời lưu bản sao tại: <series_dir>/output_videos/full_episodes/<channel_slug>_tap-XX_FULL.mp4
    """
    output_videos_dir = os.path.join(series_dir, "output_videos")
    clips = find_episode_clip_mp4s(output_videos_dir, ep_num, ep_folder_name)

    if not clips:
        msg = f"⚠️ Không tìm thấy clip .mp4 nào để ghép cho {unit_label} {ep_num:02d}."
        print(msg, flush=True)
        push_cms_log(channel_slug, msg, level="WARN", category="MERGE", project_id=project_id, episode=ep_num)
        return {"success": False, "error": "NO_CLIPS_FOUND"}

    clip_paths = [p for _, p in clips]
    clip_nums = [n for n, _ in clips]

    ep_dir_out = os.path.dirname(clip_paths[0])
    full_episodes_dir = os.path.join(output_videos_dir, "full_episodes")
    os.makedirs(full_episodes_dir, exist_ok=True)

    prefix = "canh" if unit_label.lower() == "cảnh" else "tap"
    merged_filename = f"{channel_slug}_{prefix}-{ep_num:02d}_FULL.mp4"
    merged_in_ep_dir = os.path.join(ep_dir_out, merged_filename)
    merged_in_full_dir = os.path.join(full_episodes_dir, merged_filename)

    start_msg = f"🎞️ Đang tự động ghép {len(clip_paths)} clips ({clip_nums}) thành 1 {unit_label.lower()} hoàn chỉnh: {merged_filename}..."
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {start_msg}", flush=True)
    push_cms_log(
        channel_slug,
        start_msg,
        level="INFO",
        category="MERGE",
        project_id=project_id,
        episode=ep_num,
        details={"clips_count": len(clip_paths), "clips": [os.path.basename(p) for p in clip_paths]},
    )

    tmpdir = tempfile.mkdtemp(prefix="flowkit_merge_")
    try:
        concat_list_path = os.path.join(tmpdir, "concat_list.txt")
        with open(concat_list_path, "w", encoding="utf-8") as f:
            for cp in clip_paths:
                escaped = cp.replace("'", "'\\''")
                f.write(f"file '{escaped}'\n")

        # Cách 1: Ghép trực tiếp tốc độ cao (-c copy) giữ nguyên chất lượng gốc
        cmd_copy = [
            "ffmpeg", "-y",
            "-f", "concat", "-safe", "0",
            "-i", concat_list_path,
            "-c:v", "copy", "-c:a", "copy",
            "-movflags", "+faststart",
            merged_in_ep_dir,
        ]
        res = subprocess.run(cmd_copy, capture_output=True, text=True, timeout=180)

        # Cách 2: Nếu khác thông số codec/timebase, tự động chuẩn hóa h264/aac rồi ghép
        if res.returncode != 0 or not os.path.exists(merged_in_ep_dir) or os.path.getsize(merged_in_ep_dir) == 0:
            norm_paths = []
            for idx, cp in enumerate(clip_paths):
                norm_p = os.path.join(tmpdir, f"norm_{idx:02d}.mp4")
                cmd_norm = [
                    "ffmpeg", "-y", "-i", cp,
                    "-c:v", "libx264", "-preset", "fast", "-crf", "18",
                    "-pix_fmt", "yuv420p", "-r", "24",
                    "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
                    "-movflags", "+faststart",
                    norm_p,
                ]
                r_n = subprocess.run(cmd_norm, capture_output=True, text=True, timeout=180)
                if r_n.returncode == 0 and os.path.exists(norm_p):
                    norm_paths.append(norm_p)
            if norm_paths:
                norm_list_path = os.path.join(tmpdir, "norm_list.txt")
                with open(norm_list_path, "w", encoding="utf-8") as f:
                    for np in norm_paths:
                        escaped = np.replace("'", "'\\''")
                        f.write(f"file '{escaped}'\n")
                subprocess.run(
                    [
                        "ffmpeg", "-y",
                        "-f", "concat", "-safe", "0",
                        "-i", norm_list_path,
                        "-c", "copy",
                        "-movflags", "+faststart",
                        merged_in_ep_dir,
                    ],
                    capture_output=True,
                    text=True,
                    timeout=180,
                )

        if os.path.exists(merged_in_ep_dir) and os.path.getsize(merged_in_ep_dir) > 0:
            shutil.copy2(merged_in_ep_dir, merged_in_full_dir)
            size_mb = round(os.path.getsize(merged_in_ep_dir) / (1024 * 1024), 2)
            duration_s = probe_video_duration(merged_in_ep_dir)

            width = 72
            title = "🎞️ ĐÃ TỰ ĐỘNG GHÉP TẬP HOÀN CHỈNH (FULL EPISODE)"
            print(f"\n┌─ {title} " + "─" * max(1, width - len(title) - 5) + "┐")
            for k, v in [
                ("Kênh / Series", channel_slug),
                (unit_label, f"{unit_label} {ep_num:02d} ({len(clip_paths)} clips đã ghép)"),
                ("Tên File Tập Hoàn Chỉnh", merged_filename),
                ("Tổng Thời Lượng", f"{duration_s:.1f} giây"),
                ("Dung Lượng", f"{size_mb:.2f} MB"),
                ("Đường Dẫn Tập", merged_in_ep_dir),
                ("Thư Mục Full Episodes", merged_in_full_dir),
            ]:
                line = f"│ • {k}: {v}"
                print(line[: width - 1].ljust(width - 1) + "│")
            print("└" + "─" * (width - 2) + "┘", flush=True)

            ok_msg = f"🎉 Đã ghép hoàn chỉnh {unit_label} {ep_num:02d} ({len(clip_paths)} clips -> {merged_filename}, {duration_s:.1f}s, {size_mb:.2f} MB)"
            push_cms_log(
                channel_slug,
                ok_msg,
                level="SUCCESS",
                category="MERGE",
                project_id=project_id,
                episode=ep_num,
                details={
                    "output_path": merged_in_ep_dir,
                    "full_episodes_path": merged_in_full_dir,
                    "filename": merged_filename,
                    "clips_merged": len(clip_paths),
                    "duration_s": duration_s,
                    "size_mb": size_mb,
                },
            )
            return {
                "ok": True,
                "success": True,
                "merged_path": merged_in_ep_dir,
                "output_path": merged_in_ep_dir,
                "full_episodes_path": merged_in_full_dir,
                "filename": merged_filename,
                "clip_count": len(clip_paths),
                "clips_merged": len(clip_paths),
                "clip_numbers": clip_nums,
                "duration_s": duration_s,
                "size_mb": size_mb,
            }
        else:
            err_msg = f"❌ Ghép {unit_label} {ep_num:02d} thất bại: {res.stderr[-300:] if res.stderr else 'Unknown error'}"
            print(err_msg, flush=True)
            push_cms_log(channel_slug, err_msg, level="ERROR", category="MERGE", project_id=project_id, episode=ep_num)
            return {"ok": False, "success": False, "error": err_msg}
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)
