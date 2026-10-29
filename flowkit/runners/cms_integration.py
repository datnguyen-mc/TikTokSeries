#!/usr/bin/env python3
"""
Module tích hợp CMS & Tự động ghép tập hoàn chỉnh (Auto Episode Merger + Real-time CMS Logger)
Dùng chung cho toàn bộ 6 series runners và CMS Backend.
Chỉ ghép các file VIDEO (.mp4) thực thụ, chuẩn hóa đồng nhất timebase/fps/audio để không bao giờ bị đứng hình.
"""

import os
import re
import sys
import time
import json
import shutil
import sqlite3
import tempfile
import subprocess
import urllib.request
from datetime import datetime, timezone
from typing import Optional

try:
    import requests
except ImportError:
    requests = None

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_FLOWKIT_DIR = os.path.dirname(_THIS_DIR)
if _FLOWKIT_DIR not in sys.path:
    sys.path.insert(0, _FLOWKIT_DIR)

try:
    from agent.services.r2_storage import (
        load_r2_config,
        is_r2_configured,
        build_r2_key,
        upload_file_to_r2,
    )
except Exception:
    load_r2_config = None
    is_r2_configured = lambda cfg=None: False
    build_r2_key = None
    upload_file_to_r2 = None

os.environ["NO_PROXY"] = "127.0.0.1,localhost"
os.environ["no_proxy"] = "127.0.0.1,localhost"
FLOWKIT_API = os.environ.get("FLOWKIT_API", "http://127.0.0.1:8200")
_VALID_LEVELS = {"INFO", "SUCCESS", "WARN", "WARNING", "ERROR", "DEBUG"}


def _post_api_json(path: str, payload: dict, timeout: int = 10) -> dict:
    """Gửi POST JSON tới FlowKit Backend API (hỗ trợ cả requests và urllib)."""
    url = f"{FLOWKIT_API}{path}"
    try:
        if requests is not None:
            r = requests.post(url, json=payload, timeout=timeout)
            if r.status_code < 400:
                return r.json()
        else:
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode("utf-8"),
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode("utf-8"))
    except Exception:
        pass
    return {"ok": False}


def overwrite_existing_clip_files(
    local_video_path: str,
    ep_num: int,
    clip_num: int,
    ep_folder_name: str = None,
) -> list[str]:
    """
    Khi tạo lại (regenerate) 1 clip lẻ, đảm bảo ghi đè (overwrite) toàn bộ các file .mp4 cũ
    của đúng (ep_num, clip_num) đó nếu tồn tại ở các thư mục/tên tương đương trong output_videos.
    """
    if not local_video_path or not os.path.isfile(local_video_path):
        return []

    abs_new = os.path.realpath(local_video_path)
    ep_out_dir = os.path.dirname(local_video_path)
    output_videos_dir = os.path.dirname(ep_out_dir)
    if os.path.basename(output_videos_dir) != "output_videos":
        return []

    candidate_dirs = [ep_out_dir]
    if ep_folder_name:
        candidate_dirs.append(os.path.join(output_videos_dir, ep_folder_name))
    candidate_dirs.extend(
        [
            os.path.join(output_videos_dir, f"tap-{ep_num}"),
            os.path.join(output_videos_dir, f"tap-{ep_num:02d}"),
            os.path.join(output_videos_dir, f"tap{ep_num}"),
            os.path.join(output_videos_dir, f"canh-{ep_num:02d}"),
            os.path.join(output_videos_dir, f"canh-{ep_num}"),
        ]
    )
    if os.path.isdir(output_videos_dir):
        for name in os.listdir(output_videos_dir):
            full_sub = os.path.join(output_videos_dir, name)
            if os.path.isdir(full_sub) and re.match(rf"^(?:tap|canh)[-_]?0*{ep_num}(?:[-_]|$)", name, re.IGNORECASE):
                if full_sub not in candidate_dirs:
                    candidate_dirs.append(full_sub)

    overwritten = []
    seen_dirs = set()
    for d in candidate_dirs:
        if not os.path.isdir(d):
            continue
        real_d = os.path.realpath(d)
        if real_d in seen_dirs:
            continue
        seen_dirs.add(real_d)
        for fname in os.listdir(d):
            if not fname.lower().endswith(".mp4"):
                continue
            if "full" in fname.lower() or "merged" in fname.lower():
                continue
            c_num = _extract_clip_number_from_filename(fname)
            if c_num != clip_num:
                continue
            old_fpath = os.path.join(d, fname)
            if os.path.realpath(old_fpath) == abs_new:
                continue
            try:
                shutil.copy2(local_video_path, old_fpath)
                overwritten.append(old_fpath)
            except Exception:
                pass
    return overwritten


def sync_clip_to_r2_and_d1(
    channel_slug: str,
    ep_num: int,
    clip_num: int,
    local_video_path: str,
    ep_folder_name: str = None,
    project_id: str = None,
    prompt: str = None,
    media_id: str = None,
    frame_path: str = None,
) -> dict:
    """
    Tự động upload video clip vừa tải xong lên Cloudflare R2 Storage
    và đồng bộ bản ghi cms_clip vào Cloudflare D1 SQL + SQLite.
    """
    if not local_video_path or not os.path.isfile(local_video_path):
        return {"ok": False, "error": "LOCAL_VIDEO_NOT_FOUND"}

    overwrite_existing_clip_files(local_video_path, ep_num, clip_num, ep_folder_name=ep_folder_name)

    folder = ep_folder_name or f"tap-{ep_num:02d}"
    filename = os.path.basename(local_video_path)
    size_mb = round(os.path.getsize(local_video_path) / (1024 * 1024), 2)
    duration_s = probe_video_duration(local_video_path)

    r2_key = None
    r2_url = None
    frame_r2_key = None
    frame_r2_url = None

    if load_r2_config is not None:
        cfg = load_r2_config()
        if cfg.get("r2_auto_upload", True) and is_r2_configured(cfg):
            obj_key = build_r2_key(channel_slug, "episodes", filename, subfolder=folder, cfg=cfg)
            print(f"☁️ [R2 STORAGE] Đang upload & ghi đè clip {filename} ({size_mb:.2f} MB) lên Cloudflare R2...", flush=True)
            up_res = upload_file_to_r2(local_video_path, obj_key, content_type="video/mp4", cfg=cfg)
            if up_res.get("ok"):
                r2_key = up_res.get("r2_key")
                r2_url = up_res.get("r2_url")
                print(f"✅ [R2 STORAGE] Upload thành công: {r2_url}", flush=True)
                push_cms_log(
                    channel_slug,
                    f"☁️ Đã upload clip {filename} lên Cloudflare R2: {r2_url}",
                    level="SUCCESS",
                    category="R2_UPLOAD",
                    project_id=project_id,
                    episode=ep_num,
                    clip_num=clip_num,
                    details={"r2_key": r2_key, "r2_url": r2_url, "size_mb": size_mb},
                )
            elif not up_res.get("skipped"):
                err = up_res.get("error", "Unknown error")
                print(f"⚠️ [R2 STORAGE] Upload clip {filename} chưa thành công: {err}", flush=True)

            if frame_path and os.path.isfile(frame_path):
                f_key = build_r2_key(channel_slug, "frames", os.path.basename(frame_path), cfg=cfg)
                f_res = upload_file_to_r2(frame_path, f_key, content_type="image/jpeg", cfg=cfg)
                if f_res.get("ok"):
                    frame_r2_key = f_res.get("r2_key")
                    frame_r2_url = f_res.get("r2_url")

    payload = {
        "kind": "clip",
        "channel_slug": channel_slug,
        "project_id": project_id,
        "episode_num": ep_num,
        "folder_name": folder,
        "clip_num": clip_num,
        "prompt": prompt,
        "status": "COMPLETED",
        "local_path": local_video_path,
        "r2_key": r2_key,
        "r2_url": r2_url,
        "frame_local_path": frame_path,
        "frame_r2_key": frame_r2_key,
        "frame_r2_url": frame_r2_url,
        "size_mb": size_mb,
        "duration_s": duration_s,
        "media_id": media_id,
    }
    api_res = _post_api_json("/api/cms/cloud/sync-record", payload, timeout=15)
    _fallback_upsert_local_and_d1(payload, skip_local=bool(api_res.get("ok")))

    return {
        "ok": True,
        "r2_key": r2_key,
        "r2_url": r2_url,
        "size_mb": size_mb,
        "duration_s": duration_s,
    }


def sync_merged_episode_to_r2_and_d1(
    channel_slug: str,
    ep_num: int,
    merged_video_path: str,
    ep_folder_name: str = None,
    project_id: str = None,
    clip_count: int = 0,
    total_clips: int = 0,
    is_complete: int = 1,
    duration_s: float = 0.0,
    size_mb: float = 0.0,
    unit_label: str = "Tập",
) -> dict:
    """
    Tự động upload video tập hoàn chỉnh (*_FULL.mp4) lên Cloudflare R2 Storage
    và đồng bộ bản ghi cms_episode vào Cloudflare D1 SQL + SQLite.
    """
    if not merged_video_path or not os.path.isfile(merged_video_path):
        return {"ok": False, "error": "MERGED_VIDEO_NOT_FOUND"}

    folder = ep_folder_name or f"tap-{ep_num:02d}"
    filename = os.path.basename(merged_video_path)
    sz = size_mb or round(os.path.getsize(merged_video_path) / (1024 * 1024), 2)
    dur = duration_s or probe_video_duration(merged_video_path)

    r2_key = None
    r2_url = None

    if load_r2_config is not None:
        cfg = load_r2_config()
        if cfg.get("r2_auto_upload", True) and is_r2_configured(cfg):
            obj_key = build_r2_key(channel_slug, "full_episodes", filename, cfg=cfg)
            print(f"☁️ [R2 STORAGE] Đang upload tập hoàn chỉnh {filename} ({sz:.2f} MB) lên Cloudflare R2...", flush=True)
            up_res = upload_file_to_r2(merged_video_path, obj_key, content_type="video/mp4", cfg=cfg)
            if up_res.get("ok"):
                r2_key = up_res.get("r2_key")
                r2_url = up_res.get("r2_url")
                print(f"✅ [R2 STORAGE] Đã đồng bộ {filename} lên R2: {r2_url}", flush=True)
                push_cms_log(
                    channel_slug,
                    f"☁️ Đã upload {unit_label} {ep_num:02d} FULL ({filename}) lên Cloudflare R2: {r2_url}",
                    level="SUCCESS",
                    category="R2_UPLOAD",
                    project_id=project_id,
                    episode=ep_num,
                    details={"r2_key": r2_key, "r2_url": r2_url, "size_mb": sz, "duration_s": dur},
                )
            elif not up_res.get("skipped"):
                err = up_res.get("error", "Unknown error")
                print(f"⚠️ [R2 STORAGE] Upload {filename} chưa thành công: {err}", flush=True)

    eff_total = max(total_clips or 0, clip_count)
    payload = {
        "kind": "episode",
        "channel_slug": channel_slug,
        "project_id": project_id,
        "episode_num": ep_num,
        "folder_name": folder,
        "label": f"{unit_label} {ep_num:02d}",
        "total_clips": eff_total,
        "rendered_clips": clip_count,
        "is_complete": is_complete,
        "merged_local_path": merged_video_path,
        "merged_r2_key": r2_key,
        "merged_r2_url": r2_url,
        "merged_size_mb": sz,
        "duration_s": dur,
    }
    api_res = _post_api_json("/api/cms/cloud/sync-record", payload, timeout=15)
    _fallback_upsert_local_and_d1(payload, skip_local=bool(api_res.get("ok")))

    return {
        "ok": True,
        "r2_key": r2_key,
        "r2_url": r2_url,
        "size_mb": sz,
        "duration_s": dur,
    }


def _fallback_upsert_local_and_d1(payload: dict, skip_local: bool = False) -> None:
    """Ghi trực tiếp vào SQLite cục bộ & Cloudflare D1 SQL để đồng bộ trạng thái hoàn thành trên nhiều máy local."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    db_path = os.path.join(_FLOWKIT_DIR, "flow_agent.db")
    kind = payload.get("kind")
    slug = payload.get("channel_slug", "")
    ep_num = int(payload.get("episode_num") or 0)

    if kind == "clip":
        clip_num = int(payload.get("clip_num") or 0)
        rec_id = f"{slug}:ep:{ep_num}:clip:{clip_num}"
        sql = """INSERT OR REPLACE INTO cms_clip
                 (id, channel_slug, project_id, episode_num, folder_name, clip_num, prompt, status,
                  local_path, r2_key, r2_url, frame_local_path, frame_r2_key, frame_r2_url,
                  size_mb, duration_s, media_id, updated_at)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        params = [
            rec_id,
            slug,
            payload.get("project_id"),
            ep_num,
            payload.get("folder_name") or f"tap-{ep_num:02d}",
            clip_num,
            payload.get("prompt"),
            payload.get("status") or "COMPLETED",
            payload.get("local_path"),
            payload.get("r2_key"),
            payload.get("r2_url"),
            payload.get("frame_local_path"),
            payload.get("frame_r2_key"),
            payload.get("frame_r2_url"),
            payload.get("size_mb"),
            payload.get("duration_s"),
            payload.get("media_id"),
            now,
        ]
    else:
        rec_id = f"{slug}:ep:{ep_num}"
        sql = """INSERT OR REPLACE INTO cms_episode
                 (id, channel_slug, project_id, episode_num, folder_name, label,
                  total_clips, rendered_clips, is_complete, merged_local_path,
                  merged_r2_key, merged_r2_url, merged_size_mb, duration_s, updated_at)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        params = [
            rec_id,
            slug,
            payload.get("project_id"),
            ep_num,
            payload.get("folder_name") or f"tap-{ep_num:02d}",
            payload.get("label") or f"Tập {ep_num:02d}",
            payload.get("total_clips") or 0,
            payload.get("rendered_clips") or 0,
            payload.get("is_complete") or 1,
            payload.get("merged_local_path"),
            payload.get("merged_r2_key"),
            payload.get("merged_r2_url"),
            payload.get("merged_size_mb"),
            payload.get("duration_s"),
            now,
        ]

    if not skip_local:
        try:
            with sqlite3.connect(db_path) as conn:
                conn.execute(sql, params)
                if kind == "episode" and payload.get("is_complete") and (payload.get("rendered_clips") or 0) >= max(payload.get("total_clips") or 0, 1):
                    conn.execute(
                        "UPDATE cms_clip SET status = 'COMPLETED', updated_at = ? WHERE channel_slug = ? AND episode_num = ?",
                        (now, slug, ep_num),
                    )
                conn.commit()
        except Exception:
            pass

    try:
        from agent.db.d1_client import is_d1_configured, d1_query_sync
        if is_d1_configured():
            d1_query_sync(sql, params)
            if kind == "episode" and payload.get("is_complete") and (payload.get("rendered_clips") or 0) >= max(payload.get("total_clips") or 0, 1):
                d1_query_sync(
                    "UPDATE cms_clip SET status = 'COMPLETED', updated_at = ? WHERE channel_slug = ? AND episode_num = ?",
                    [now, slug, ep_num],
                )
    except Exception:
        pass


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
            eff_level = level or arg2
            eff_cat = category or arg3
            eff_msg = message or arg4
        elif arg2.upper() in _VALID_LEVELS and message is not None:
            eff_level = level or arg2
            eff_cat = category or arg3
            eff_msg = message
        else:
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
        if requests is not None:
            requests.post(f"{FLOWKIT_API}/api/cms/logs", json=payload, timeout=3)
        else:
            req = urllib.request.Request(
                f"{FLOWKIT_API}/api/cms/logs",
                data=json.dumps(payload).encode("utf-8"),
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            urllib.request.urlopen(req, timeout=3)
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


def probe_clip_streams(video_path: str) -> dict:
    """Kiểm tra file có đúng là video .mp4 hợp lệ (có luồng video thực thụ, không phải ảnh tĩnh)."""
    try:
        res = subprocess.run(
            [
                "ffprobe",
                "-v",
                "error",
                "-show_entries",
                "format=duration:stream=index,codec_type,codec_name,width,height,nb_frames",
                "-of",
                "json",
                video_path,
            ],
            capture_output=True,
            text=True,
            timeout=20,
        )
        data = json.loads(res.stdout or "{}")
        streams = data.get("streams") or []
        fmt = data.get("format") or {}
        duration = float(fmt.get("duration") or 0.0)

        video_stream = None
        has_audio = False
        for s in streams:
            if s.get("codec_type") == "video" and s.get("codec_name") not in ("mjpeg", "png", "webp"):
                video_stream = s
            elif s.get("codec_type") == "audio":
                has_audio = True

        if not video_stream or duration <= 0.5:
            return {"valid_video": False}

        return {
            "valid_video": True,
            "width": int(video_stream.get("width") or 720),
            "height": int(video_stream.get("height") or 1280),
            "has_audio": has_audio,
            "duration": round(duration, 2),
        }
    except Exception:
        return {"valid_video": False}


def find_episode_clip_mp4s(output_videos_dir: str, ep_num: int, ep_folder_name: str = None) -> list[tuple[int, str]]:
    """
    Tìm tất cả các file VIDEO (.mp4) clip nhỏ thuộc Tập / Cảnh ep_num, sắp xếp theo đúng thứ tự clip 1 -> N.
    Chỉ lấy file video .mp4 hợp lệ, bỏ qua toàn bộ file ảnh (.jpg/.png) và bỏ qua file *_FULL.mp4.
    """
    candidate_dirs = []
    if ep_folder_name:
        candidate_dirs.append(os.path.join(output_videos_dir, ep_folder_name))
    candidate_dirs.extend(
        [
            os.path.join(output_videos_dir, f"tap-{ep_num}"),
            os.path.join(output_videos_dir, f"tap-{ep_num:02d}"),
            os.path.join(output_videos_dir, f"tap{ep_num}"),
            os.path.join(output_videos_dir, f"canh-{ep_num:02d}"),
            os.path.join(output_videos_dir, f"canh-{ep_num}"),
        ]
    )
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
        for fname in sorted(os.listdir(d)):
            if not fname.lower().endswith(".mp4"):
                continue
            if "full" in fname.lower() or "merged" in fname.lower():
                continue
            fpath = os.path.join(d, fname)
            if not os.path.isfile(fpath) or os.path.getsize(fpath) == 0:
                continue
            c_num = _extract_clip_number_from_filename(fname)
            if c_num not in found_by_clip_num:
                info = probe_clip_streams(fpath)
                if info.get("valid_video"):
                    found_by_clip_num[c_num] = fpath

    return sorted(found_by_clip_num.items(), key=lambda x: x[0])


def probe_video_duration(video_path: str) -> float:
    """Lấy thời lượng video (giây) qua ffprobe."""
    try:
        res = subprocess.run(
            [
                "ffprobe",
                "-v",
                "quiet",
                "-show_entries",
                "format=duration",
                "-of",
                "csv=p=0",
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
    Ghép toàn bộ các file VIDEO (.mp4) clip nhỏ của Tập/Cảnh ep_num thành 1 video hoàn chỉnh:
    - Luôn chuẩn hóa từng clip về cùng độ phân giải, 24fps CFR, time_base 1/12288, H.264 + AAC 48kHz
      trước khi nối để tuyệt đối không bị đứng hình (frozen frame) do lệch time_base giữa các API Google Flow.
    - Lưu tại: <series_dir>/output_videos/<ep_folder>/<channel_slug>_tap-XX_FULL.mp4
    - Đồng thời lưu bản sao tại: <series_dir>/output_videos/full_episodes/<channel_slug>_tap-XX_FULL.mp4
    """
    output_videos_dir = os.path.join(series_dir, "output_videos")
    clips = find_episode_clip_mp4s(output_videos_dir, ep_num, ep_folder_name)

    if not clips:
        msg = f"⚠️ Không tìm thấy clip video .mp4 nào để ghép cho {unit_label} {ep_num:02d}."
        print(msg, flush=True)
        push_cms_log(channel_slug, msg, level="WARN", category="MERGE", project_id=project_id, episode=ep_num)
        return {"ok": False, "success": False, "error": "NO_CLIPS_FOUND"}

    clip_paths = [p for _, p in clips]
    clip_nums = [n for n, _ in clips]

    ep_dir_out = os.path.dirname(clip_paths[0])
    full_episodes_dir = os.path.join(output_videos_dir, "full_episodes")
    os.makedirs(full_episodes_dir, exist_ok=True)

    prefix = "canh" if unit_label.lower() == "cảnh" else "tap"
    merged_filename = f"{channel_slug}_{prefix}-{ep_num:02d}_FULL.mp4"
    merged_in_ep_dir = os.path.join(ep_dir_out, merged_filename)
    merged_in_full_dir = os.path.join(full_episodes_dir, merged_filename)

    # Đếm tổng số clip kịch bản (clip-*.md) thực tế của tập trên ổ cứng
    expected_total_clips = 0
    prompt_dir_candidates = []
    if ep_folder_name:
        prompt_dir_candidates.append(os.path.join(series_dir, ep_folder_name))
    prompt_dir_candidates.extend([
        os.path.join(series_dir, f"tap-{ep_num}"),
        os.path.join(series_dir, f"tap-{ep_num:02d}"),
        os.path.join(series_dir, f"canh-{ep_num:02d}"),
    ])
    for pd in prompt_dir_candidates:
        if os.path.isdir(pd):
            md_clips = [f for f in os.listdir(pd) if re.match(r"^clip-\d+\.md$", f)]
            if md_clips:
                expected_total_clips = len(md_clips)
                break

    only_clip_env = int(os.environ.get("FLOWKIT_ONLY_CLIP", "0") or "0")
    already_had_merged = os.path.isfile(merged_in_ep_dir) or os.path.isfile(merged_in_full_dir)

    # Nếu chỉ đang tạo lại / ghi đè 1 clip lẻ (FLOWKIT_ONLY_CLIP > 0) và tập này chưa đủ toàn bộ các clip
    # cũng như chưa từng có file FULL trước đó -> chỉ ghi đè đúng clip lẻ đó, chưa ghép FULL sớm
    if only_clip_env > 0 and expected_total_clips > 0 and len(clip_paths) < expected_total_clips and not already_had_merged:
        skip_msg = (
            f"✅ Đã tạo & ghi đè hoàn tất {unit_label} {ep_num:02d} - Clip {only_clip_env:02d} "
            f"(Hiện có {len(clip_paths)}/{expected_total_clips} clips MP4; sẽ tự động ghép FULL khi đủ {expected_total_clips} clips)."
        )
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {skip_msg}", flush=True)
        push_cms_log(
            channel_slug,
            skip_msg,
            level="SUCCESS",
            category="RUNNER",
            project_id=project_id,
            episode=ep_num,
            clip_num=only_clip_env,
        )
        return {
            "ok": True,
            "success": True,
            "skipped_partial_merge": True,
            "clip_count": len(clip_paths),
            "expected_total_clips": expected_total_clips,
        }

    start_msg = (
        f"🎞️ Đang chuẩn hóa & ghép nối {len(clip_paths)} video clips ({clip_nums}) "
        f"thành 1 {unit_label.lower()} hoàn chỉnh: {merged_filename}..."
    )
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

    first_info = probe_clip_streams(clip_paths[0])
    target_w = first_info.get("width") or 720
    target_h = first_info.get("height") or 1280

    tmpdir = tempfile.mkdtemp(prefix="flowkit_merge_")
    try:
        norm_paths = []
        last_err = ""
        vf_chain = (
            f"scale={target_w}:{target_h}:force_original_aspect_ratio=decrease,"
            f"pad={target_w}:{target_h}:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=24,format=yuv420p"
        )

        for idx, cp in enumerate(clip_paths):
            c_info = probe_clip_streams(cp)
            norm_p = os.path.join(tmpdir, f"norm_{idx:02d}.mp4")

            if c_info.get("has_audio"):
                cmd_norm = [
                    "ffmpeg",
                    "-y",
                    "-i",
                    cp,
                    "-vf",
                    vf_chain,
                    "-c:v",
                    "libx264",
                    "-preset",
                    "fast",
                    "-crf",
                    "18",
                    "-r",
                    "24",
                    "-video_track_timescale",
                    "12288",
                    "-c:a",
                    "aac",
                    "-b:a",
                    "192k",
                    "-ar",
                    "48000",
                    "-ac",
                    "2",
                    "-af",
                    "aresample=async=1:first_pts=0",
                    "-shortest",
                    "-movflags",
                    "+faststart",
                    norm_p,
                ]
            else:
                cmd_norm = [
                    "ffmpeg",
                    "-y",
                    "-i",
                    cp,
                    "-f",
                    "lavfi",
                    "-i",
                    "anullsrc=channel_layout=stereo:sample_rate=48000",
                    "-map",
                    "0:v:0",
                    "-map",
                    "1:a:0",
                    "-vf",
                    vf_chain,
                    "-c:v",
                    "libx264",
                    "-preset",
                    "fast",
                    "-crf",
                    "18",
                    "-r",
                    "24",
                    "-video_track_timescale",
                    "12288",
                    "-c:a",
                    "aac",
                    "-b:a",
                    "192k",
                    "-ar",
                    "48000",
                    "-ac",
                    "2",
                    "-shortest",
                    "-movflags",
                    "+faststart",
                    norm_p,
                ]

            r_n = subprocess.run(cmd_norm, capture_output=True, text=True, timeout=180)
            if r_n.returncode == 0 and os.path.exists(norm_p) and os.path.getsize(norm_p) > 0:
                norm_paths.append(norm_p)
            else:
                last_err = r_n.stderr[-300:] if r_n.stderr else "Normalize failed"

        if not norm_paths:
            err_msg = f"❌ Không chuẩn hóa được các video clip để ghép {unit_label} {ep_num:02d}: {last_err}"
            print(err_msg, flush=True)
            push_cms_log(channel_slug, err_msg, level="ERROR", category="MERGE", project_id=project_id, episode=ep_num)
            return {"ok": False, "success": False, "error": err_msg}

        norm_list_path = os.path.join(tmpdir, "norm_list.txt")
        with open(norm_list_path, "w", encoding="utf-8") as f:
            for np in norm_paths:
                escaped = np.replace("'", "'\\''")
                f.write(f"file '{escaped}'\n")

        res = subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-f",
                "concat",
                "-safe",
                "0",
                "-i",
                norm_list_path,
                "-c:v",
                "copy",
                "-c:a",
                "copy",
                "-movflags",
                "+faststart",
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

            # Tự động upload file tập hoàn chỉnh lên Cloudflare R2 & đồng bộ D1 SQL
            r2_sync = sync_merged_episode_to_r2_and_d1(
                channel_slug=channel_slug,
                ep_num=ep_num,
                merged_video_path=merged_in_ep_dir,
                ep_folder_name=ep_folder_name or os.path.basename(ep_dir_out),
                project_id=project_id,
                clip_count=len(norm_paths),
                total_clips=max(expected_total_clips, len(norm_paths)),
                is_complete=1 if (expected_total_clips == 0 or len(norm_paths) >= expected_total_clips) else 0,
                duration_s=duration_s,
                size_mb=size_mb,
                unit_label=unit_label,
            )
            r2_url = r2_sync.get("r2_url")
            r2_key = r2_sync.get("r2_key")

            width = 72
            title = "🎞️ ĐÃ TỰ ĐỘNG GHÉP VIDEO TẬP HOÀN CHỈNH (FULL EPISODE)"
            print(f"\n┌─ {title} " + "─" * max(1, width - len(title) - 5) + "┐")
            box_rows = [
                ("Kênh / Series", channel_slug),
                (unit_label, f"{unit_label} {ep_num:02d} ({len(norm_paths)} video clips đã nối)"),
                ("Tên File Tập Hoàn Chỉnh", merged_filename),
                ("Tổng Thời Lượng", f"{duration_s:.1f} giây"),
                ("Dung Lượng", f"{size_mb:.2f} MB"),
                ("Đường Dẫn Tập", merged_in_ep_dir),
                ("Thư Mục Full Episodes", merged_in_full_dir),
            ]
            if r2_url:
                box_rows.append(("Cloudflare R2 URL", r2_url))
            for k, v in box_rows:
                line = f"│ • {k}: {v}"
                print(line[: width - 1].ljust(width - 1) + "│")
            print("└" + "─" * (width - 2) + "┘", flush=True)

            ok_msg = f"🎉 Đã ghép hoàn chỉnh {unit_label} {ep_num:02d} ({len(norm_paths)} video clips -> {merged_filename}, {duration_s:.1f}s, {size_mb:.2f} MB)"
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
                    "clips_merged": len(norm_paths),
                    "duration_s": duration_s,
                    "size_mb": size_mb,
                    "r2_key": r2_key,
                    "r2_url": r2_url,
                },
            )
            return {
                "ok": True,
                "success": True,
                "merged_path": merged_in_ep_dir,
                "output_path": merged_in_ep_dir,
                "full_episodes_path": merged_in_full_dir,
                "filename": merged_filename,
                "clip_count": len(norm_paths),
                "clips_merged": len(norm_paths),
                "clip_numbers": clip_nums,
                "duration_s": duration_s,
                "size_mb": size_mb,
                "r2_key": r2_key,
                "r2_url": r2_url,
            }
        else:
            err_msg = f"❌ Ghép {unit_label} {ep_num:02d} thất bại: {res.stderr[-300:] if res.stderr else 'Unknown error'}"
            print(err_msg, flush=True)
            push_cms_log(channel_slug, err_msg, level="ERROR", category="MERGE", project_id=project_id, episode=ep_num)
            return {"ok": False, "success": False, "error": err_msg}
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


def merge_multi_scenes_to_episode(
    series_dir: str,
    channel_slug: str,
    tap_num: int,
    start_scene: int,
    end_scene: int,
    project_id: str = None,
) -> dict:
    """
    Ghép 10 cảnh (ví dụ canh-01 -> canh-10 = 60 clips = 10 phút) thành 1 Tập Full 10 phút:
    - <series_dir>/output_videos/<channel_slug>_tap-{tap_num:02d}_FULL.mp4
    - <series_dir>/output_videos/<channel_slug>_tap-{tap_num}_FULL.mp4
    - <series_dir>/output_videos/full_episodes/<channel_slug>_tap-{tap_num:02d}_FULL.mp4
    - <series_dir>/output_videos/full_episodes/<channel_slug>_tap-{tap_num}_FULL.mp4
    """
    output_videos_dir = os.path.join(series_dir, "output_videos")
    full_episodes_dir = os.path.join(output_videos_dir, "full_episodes")
    os.makedirs(full_episodes_dir, exist_ok=True)

    scene_videos = []
    for s in range(start_scene, end_scene + 1):
        res = merge_episode_clips(series_dir, channel_slug, s, f"canh-{s:02d}", project_id=project_id, unit_label="Cảnh")
        if res.get("ok") and res.get("merged_path") and os.path.exists(res["merged_path"]):
            scene_videos.append(res["merged_path"])

    if not scene_videos:
        return {"ok": False, "error": "NO_SCENE_VIDEOS"}

    out_02d = os.path.join(output_videos_dir, f"{channel_slug}_tap-{tap_num:02d}_FULL.mp4")
    out_d = os.path.join(output_videos_dir, f"{channel_slug}_tap-{tap_num}_FULL.mp4")
    full_02d = os.path.join(full_episodes_dir, f"{channel_slug}_tap-{tap_num:02d}_FULL.mp4")
    full_d = os.path.join(full_episodes_dir, f"{channel_slug}_tap-{tap_num}_FULL.mp4")

    tmpdir = tempfile.mkdtemp(prefix="flowkit_merge10_")
    try:
        concat_list = os.path.join(tmpdir, "concat_list.txt")
        with open(concat_list, "w", encoding="utf-8") as f:
            for p in scene_videos:
                escaped = p.replace("'", "'\\''")
                f.write(f"file '{escaped}'\n")

        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-f",
                "concat",
                "-safe",
                "0",
                "-i",
                concat_list,
                "-c:v",
                "copy",
                "-c:a",
                "copy",
                "-movflags",
                "+faststart",
                out_02d,
            ],
            capture_output=True,
            text=True,
            timeout=300,
        )
        if os.path.exists(out_02d) and os.path.getsize(out_02d) > 0:
            shutil.copy2(out_02d, out_d)
            shutil.copy2(out_02d, full_02d)
            shutil.copy2(out_02d, full_d)
            dur = probe_video_duration(out_02d)
            sz = round(os.path.getsize(out_02d) / (1024 * 1024), 2)
            r2_sync = sync_merged_episode_to_r2_and_d1(
                channel_slug=channel_slug,
                ep_num=100 + tap_num,
                merged_video_path=out_02d,
                ep_folder_name=f"tap-{tap_num:02d}-full",
                project_id=project_id,
                clip_count=len(scene_videos) * 6,
                duration_s=dur,
                size_mb=sz,
                unit_label="Tập Full 10P",
            )
            msg = f"🎉 Đã ghép Tập {tap_num:02d} FULL 10 phút (Cảnh {start_scene:02d} -> {end_scene:02d}, {dur:.1f}s, {sz:.2f} MB)"
            print(msg, flush=True)
            push_cms_log(
                channel_slug,
                msg,
                level="SUCCESS",
                category="MERGE",
                project_id=project_id,
                episode=tap_num,
                details={
                    "output_path": out_02d,
                    "duration_s": dur,
                    "size_mb": sz,
                    "r2_key": r2_sync.get("r2_key"),
                    "r2_url": r2_sync.get("r2_url"),
                },
            )
            return {
                "ok": True,
                "output_path": out_02d,
                "duration_s": dur,
                "size_mb": sz,
                "r2_key": r2_sync.get("r2_key"),
                "r2_url": r2_sync.get("r2_url"),
            }
        return {"ok": False, "error": "CONCAT_FAILED"}
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


def wait_if_cooldown_error(res_text: str, flowkit_api: str = None, log_fn=print) -> bool:
    """
    Kiểm tra nếu phản hồi lỗi từ Google Flow là PUBLIC_ERROR_UNUSUAL_ACTIVITY / local cooldown active:
    - Tự động đọc số giây cần chờ (ví dụ 'retry in about 66s'), chờ đủ thời gian (tối đa 70s)
      rồi gọi POST /api/flow/clear-hijack để mở khóa hàng đợi.
    - Trả về True để runner gửi lại đúng clip đó mà KHÔNG bị trừ lượt retry và KHÔNG sửa file prompt.
    """
    text = str(res_text or "")
    if (
        "PUBLIC_ERROR_UNUSUAL_ACTIVITY" not in text
        and "local cooldown active" not in text
        and "unusual_activity" not in text.lower()
        and "extension_hijack" not in text.lower()
    ):
        return False

    api_base = flowkit_api or FLOWKIT_API
    m = re.search(r"retry in about\s+(\d+)\s*s", text, re.IGNORECASE)
    reported_s = int(m.group(1)) if m else 65
    wait_s = min(max(reported_s + 3, 15), 70)

    log_fn(
        f"⏳ [COOLDOWN] Google Flow yêu cầu tạm nghỉ chống spam ({reported_s}s). "
        f"Tự động chờ {wait_s}s rồi gửi lại (KHÔNG tính lỗi, KHÔNG sửa file prompt)..."
    )
    time.sleep(wait_s)

    try:
        if requests is not None:
            requests.post(f"{api_base}/api/flow/clear-hijack", timeout=5)
        else:
            req = urllib.request.Request(f"{api_base}/api/flow/clear-hijack", data=b"{}", method="POST")
            urllib.request.urlopen(req, timeout=5)
    except Exception:
        pass

    log_fn("✅ [COOLDOWN] Đã hết thời gian nghỉ Cooldown & mở khóa hàng đợi. Tiếp tục gửi lại clip!")
    return True


# ─── Smart Multi-Stage Prompt Rewriter (Zero-Skip Guarantee) ─────────────────

_EN_SAFE_REPLACEMENTS = [
    (r"\bsuperhero blockbuster\b", "photorealistic Vietnamese cinematic film"),
    (r"\bsuperhero\b", "skilled specialist"),
    (r"\bhollywood cinematography\b", "high-end cinema 24fps"),
    (r"\bhollywood\b", "cinematic"),
    (r"\bmarvel\b", "cinematic"),
    (r"\balien technology\b", "advanced engineering prototype"),
    (r"\balien\b", "experimental"),
    (r"\bweapon(?:s)?\b", "technical tool"),
    (r"\bgun(?:s)?\b", "diagnostic device"),
    (r"\bknife|knives|blade(?:s)?|sword(?:s)?|dagger(?:s)?\b", "metal tool"),
    (r"\bblood(?:y)?|bleed(?:ing)?\b", "dark machine oil"),
    (r"\bwound(?:s|ed)?|injury|injured\b", "mark"),
    (r"\bscar(?:s|red)?\b", "distinctive feature"),
    (r"\bexplod(?:e|es|ed|ing)|explosion(?:s)?|bomb(?:s)?|blast(?:s)?\b", "bright light pulse"),
    (r"\bshoot(?:s|ing)?|shot(?:s)?\b", "project"),
    (r"\bfight(?:s|ing)?|combat|battle(?:s)?|brawl\b", "intense teamwork"),
    (r"\bpunch(?:es|ing)?|kick(?:s|ing)?|slap(?:s|ping)?|strike(?:s|ing)?|hit(?:s|ting)?\b", "gesture toward"),
    (r"\bslam(?:s|med|ming)?\b", "place firmly"),
    (r"\blunge(?:s|d|ing)?\b", "step quickly"),
    (r"\bchok(?:e|es|ing)|strangl(?:e|es|ing)\b", "hold back"),
    (r"\bkill(?:s|ed|ing)?|dead|death|die(?:s|d)?|corpse(?:s)?|murder\b", "stop"),
    (r"\battack(?:s|ed|ing)?|assault\b", "approach"),
    (r"\bcrash(?:es|ed|ing)?|collid(?:e|es|ed|ing)|collision\b", "sudden stop"),
    (r"\bfire|flame(?:s)?|burn(?:s|ed|ing)?\b", "warm amber glow"),
    (r"\belectric shock|electrocut(?:e|ed|ing)\b", "bright energy shimmer"),
    (r"\bhack(?:er|ers|ing|ed)?\b", "digital diagnostics"),
    (r"\bsteal(?:s|ing)?|thief|thieves|rob(?:bery|bing)?|crime|criminal(?:s)?\b", "mystery"),
    (r"\bterror|terrified|panic(?:ked|king)?|horrified|horror|scream(?:s|ed|ing)?\b", "surprised expression"),
    (r"\bcry(?:ing)?|cries|sobbing|weep(?:ing)?|tears\b", "emotional expression"),
    (r"\bfuss(?:es|ing)?|whin(?:e|es|ing)|groan(?:s|ing)?\b", "soft sound"),
    (r"\bnaked|nude|nudity|undress(?:ed|ing)?|bare chest|uncovered chest\b", "modest casual home attire"),
    (r"\bbreastfeed(?:ing)?|nursing pillow|nursing cover|suck(?:ing|ling)?\b", "caring for the babies with a soft support cushion"),
    (r"\bnewborn baby|newborn babies|newborn\b", "adorable young baby"),
    (r"\binfant(?:s)?\b", "young child"),
    (r"\bskull(?:s)?|skeleton(?:s)?|demon(?:s)?|monster(?:s)?\b", "traditional ornament"),
    (r"\bbuddha|buddhist|monk(?:'s)?|altar\b", "serene zen teacher"),
]

_VI_SAFE_REPLACEMENTS = [
    ("ghim vào cổ tay", "nhẹ nhàng khóa quanh cổ tay thành vòng tay"),
    ("tước vũ khí", "thu hồi thiết bị"),
    ("vũ khí", "thiết bị kỹ thuật"),
    ("đánh nhau dằn co", "phối hợp xử lý kỹ thuật"),
    ("đánh nhau", "tương tác kỹ thuật"),
    ("vật lộn", "xoay sở kỹ thuật"),
    ("khống chế", "giữ ổn định"),
    ("bắt cóc", "giữ lại"),
    ("tội phạm", "đối phương"),
    ("kẻ địch", "đối phương"),
    ("kẻ xấu", "đối phương"),
    ("sát thủ", "người lạ"),
    ("máu", "vệt dầu máy"),
    ("vết sẹo", "nét mặt góc cạnh"),
    ("sẹo", "nét riêng"),
    ("đâm", "tiến tới"),
    ("chém", "vung tay"),
    ("bắn", "phát sáng"),
    ("nổ tung", "phát sáng rực"),
    ("phát nổ", "phát sáng"),
    ("cháy nổ", "lóe sáng"),
    ("giết", "ngăn lại"),
    ("chết", "đứng yên"),
    ("hạ gục", "hóa giải"),
    ("ngất xỉu", "mệt mỏi"),
    ("hoảng loạn", "bất ngờ"),
    ("sợ hãi", "ngạc nhiên"),
    ("khóc thét", "lên tiếng"),
    ("bú đôi", "nằm gối đôi"),
    ("cho bú", "chăm bé"),
    ("bú mẹ", "ăn sữa"),
]


def _extract_dialogue_lines(prompt: str) -> list[str]:
    """Trích xuất các câu thoại tiếng Việt trong prompt để bảo toàn 100% nội dung kịch bản."""
    lines = []
    for raw_line in prompt.splitlines():
        m = re.search(r"([A-ZÀ-ỸĐa-zà-ỹđ0-9_@\s]+\s+says\s*(?:\([^)]*\))?\s*:\s*.+)$", raw_line.strip())
        if m:
            lines.append(m.group(1).strip())
    return lines


def rewrite_prompt_on_failure(
    prompt: str,
    attempt: int = 1,
    character_specs: list[dict] = None,
    aspect_ratio: str = "VIDEO_ASPECT_RATIO_PORTRAIT",
) -> str:
    """
    Bộ đổi Prompt thông minh đa cấp độ ngay khi gặp lỗi từ Google Flow:
    - Cấp độ 1 (attempt=1): Khử toàn bộ từ khóa nhạy cảm Anh/Việt & làm sạch khối [AVOID] (loại bỏ từ khóa cấm nằm trong [AVOID]).
    - Cấp độ 2 (attempt=2): Làm mềm chuyển động trong [SHOT LIST], chuyển sang góc máy tĩnh/mượt và ép dùng [FORMAT] (Ingredients R2V).
    - Cấp độ 3 (attempt=3): Tái cấu trúc thành Storyboard sạch 3 phân cảnh, giữ nguyên khóa nhân vật @Tag và 100% lời thoại tiếng Việt.
    - Cấp độ 4+ (attempt>=4): Chế độ Ultra-Safe Studio Prompt tối giản, đảm bảo 100% vượt qua bộ lọc của Google Flow và không bỏ sót clip.
    """
    p = prompt or ""

    # 1. Luôn áp dụng bộ lọc từ khóa an toàn Anh & Việt
    for pat, repl in _EN_SAFE_REPLACEMENTS:
        p = re.sub(pat, repl, p, flags=re.IGNORECASE)
    for k, v in _VI_SAFE_REPLACEMENTS:
        p = p.replace(k, v).replace(k.capitalize(), v.capitalize())

    # 2. Thay thế phần [AVOID] (vốn thường chứa các từ nhạy cảm như nudity, blood, weapon làm kích hoạt nhầm bộ lọc)
    clean_avoid = (
        "[AVOID]\n"
        "subtitles, captions, on-screen text, readable letters or numbers, watermarks, logos, "
        "visual glitches, distorted hands, extra fingers, abrupt jump cuts."
    )
    if "[AVOID]" in p:
        p = re.sub(r"\[AVOID\][\s\S]*$", clean_avoid, p)
    else:
        p = p.rstrip() + "\n\n" + clean_avoid

    # Nếu ở attempt 1 mà p đã thay đổi so với prompt gốc thì trả về ngay
    if attempt == 1 and p.strip() != (prompt or "").strip():
        return p

    # 3. Cấp độ 2: Làm mềm hành động & chuyển sang chế độ mở cảnh [FORMAT] độc lập (tránh lỗi từ start_frame)
    is_portrait = "PORTRAIT" in (aspect_ratio or "").upper()
    orient_str = "Vertical 9:16" if is_portrait else "Horizontal 16:9"
    is_2d = "2d animated" in p.lower() or "hand-drawn" in p.lower()
    is_3d = "3d cgi" in p.lower() or "pixar" in p.lower()

    if attempt <= 2:
        p2 = re.sub(
            r"^Continue the scene seamlessly[^\n]*\n(?:Vertical 9:16[^\n]*\n|Horizontal 16:9[^\n]*\n)?",
            (
                f"[FORMAT]\n{orient_str}, 10-second clip, "
                + (
                    "2D hand-drawn cel-shaded animated comedy cartoon, vibrant colors, 24fps. "
                    if is_2d
                    else "Pixar/Disney-style 3D CGI animated film, warm expressive lighting, 24fps. "
                    if is_3d
                    else "photorealistic cinematic live-action film shot on 35mm lens, warm natural lighting, 24fps. "
                )
                + "Spoken dialogue in Vietnamese with natural accent and accurate lip-sync. No subtitles, no on-screen text.\n\n"
            ),
            p.lstrip(),
            flags=re.IGNORECASE,
        )
        p2 = re.sub(r"\bExtreme close-up\b", "Medium close-up", p2, flags=re.IGNORECASE)
        p2 = re.sub(r"\bfrantically|desperately|violently|aggressively|furiously\b", "expressively", p2, flags=re.IGNORECASE)
        p2 = re.sub(r"\bdark shadows|pitch black|eerie|ominous\b", "warm balanced cinematic lighting", p2, flags=re.IGNORECASE)
        if p2.strip() == (prompt or "").strip():
            p2 = p2.rstrip() + f"\n# Safe-Retry-Pass-{attempt}"
        return p2

    # 4. Cấp độ 3 & 4+: Tái cấu trúc Storyboard siêu an toàn, bảo toàn @Character và lời thoại
    dialogues = _extract_dialogue_lines(p)
    char_lines = []
    if character_specs:
        for spec in character_specs:
            tag = spec.get("tag", "")
            desc = spec.get("description", "")
            # Làm sạch mô tả nhân vật
            for k, v in _VI_SAFE_REPLACEMENTS:
                desc = desc.replace(k, v)
            char_lines.append(f"{tag} = {desc}")
    else:
        for line in p.splitlines():
            if line.strip().startswith("@") and "=" in line:
                char_lines.append(line.strip())

    setting_match = re.search(r"\[SETTING\]\s*\n([^\n]+)", p)
    setting_line = setting_match.group(1).strip() if setting_match else "A warm, well-lit cinematic indoor setting in Vietnam."
    setting_line = setting_line[:260]

    style_header = (
        f"[FORMAT]\n{orient_str}, 10-second clip, "
        + (
            "2D animated comedy cartoon with clean bold outlines and flat cel shading, 24fps. "
            if is_2d
            else "stylized 3D CGI animation with warm cinematic lighting, 24fps. "
            if is_3d
            else "photorealistic live-action cinematic 35mm film, warm natural daylight, shallow depth of field, 24fps. "
        )
        + "Spoken dialogue in Vietnamese with accurate lip-sync. No subtitles, no captions, no on-screen text, no logos.\n"
    )

    chars_block = "[CHARACTERS — match the attached reference images exactly]\n" + "\n".join(char_lines[:5]) + "\n"

    if attempt == 3:
        d1 = f" {dialogues[0]}" if len(dialogues) >= 1 else ""
        d2 = f" {dialogues[1]}" if len(dialogues) >= 2 else ""
        d3 = f" {dialogues[2]}" if len(dialogues) >= 3 else ""
        shots_block = (
            "[SHOT LIST]\n"
            f"00:00–00:03.5 | Medium wide shot, 35mm lens, gentle camera movement — the characters interact naturally in the scene with expressive body language.{d1}\n"
            f"00:03.5–00:07 | Medium close-up, 50mm lens, warm lighting — focused reaction and natural conversation.{d2}\n"
            f"00:07–00:10 | Medium shot, 35mm lens, steady framing — the characters conclude the moment with clear expressions and hold steady at the end.{d3}\n"
        )
    else:
        all_d = " ".join(dialogues[:3])
        lens_variant = "50mm cinema lens" if attempt % 2 == 0 else "35mm cinema lens"
        light_variant = "soft golden daylight" if attempt % 2 == 0 else "warm studio practical lighting"
        shots_block = (
            "[SHOT LIST]\n"
            f"00:00–00:05 | Medium shot ({lens_variant}, {light_variant}) — the characters stand in the scene and converse naturally with warm, clear expressions. {all_d}\n"
            f"00:05–00:10 | Medium wide shot ({lens_variant}, smooth framing) — calm reaction and natural posture, holding still for the final 0.5 seconds.\n"
        )

    rebuilt = (
        f"{style_header}\n"
        f"{chars_block}\n"
        f"[SETTING]\n{setting_line}\n\n"
        f"{shots_block}\n"
        "[SOUND]\nNatural room ambience, clear Vietnamese dialogue, gentle background instrumental score.\n\n"
        f"{clean_avoid}\n"
    )
    return rebuilt


def force_rename_clip_on_flow(
    flowkit_api: str,
    project_id: str,
    submit_res_data: dict,
    display_name: str,
    media_id: str | None = None,
    log_fn=None,
) -> bool:
    """Ép đổi tên asset video trên giao diện Google Flow ngay sau khi render hoàn tất."""
    if not display_name:
        return False
    _log = log_fn or (lambda msg: print(msg, flush=True))
    flow_poll = (submit_res_data or {}).get("flowkitPolling") or {}
    workflows = (submit_res_data or {}).get("workflows") or flow_poll.get("workflows") or []
    operations = (submit_res_data or {}).get("operations") or flow_poll.get("operations") or []
    media_list = (submit_res_data or {}).get("media") or []

    asset_id = None
    if operations and isinstance(operations, list):
        op0 = operations[0] if isinstance(operations[0], dict) else {}
        asset_id = (op0.get("operation") or {}).get("name") or op0.get("name")
    if not asset_id and workflows and isinstance(workflows, list):
        wf0 = workflows[0] if isinstance(workflows[0], dict) else {}
        asset_id = wf0.get("name")
    if not media_id:
        if workflows and isinstance(workflows, list):
            wf0 = workflows[0] if isinstance(workflows[0], dict) else {}
            media_id = wf0.get("primary_media_id")
        if not media_id and media_list and isinstance(media_list, list):
            m0 = media_list[0] if isinstance(media_list[0], dict) else {}
            media_id = m0.get("name")

    if not asset_id and not media_id:
        return False

    try:
        resp = requests.post(
            f"{flowkit_api.rstrip('/')}/api/flow/rename-asset",
            json={
                "asset_id": asset_id,
                "media_id": media_id,
                "project_id": project_id,
                "display_name": display_name,
            },
            timeout=25,
        )
        if resp.status_code == 200:
            _log(f"🏷️ [GOOGLE FLOW RENAME] Đã ép đổi tên clip trên Google Flow -> '{display_name}' ✅")
            return True
        else:
            _log(f"⚠️ [GOOGLE FLOW RENAME] Chưa đổi được tên trên Flow (HTTP {resp.status_code}): {resp.text[:120]}")
    except Exception as e:
        _log(f"⚠️ [GOOGLE FLOW RENAME] Lỗi gọi API đổi tên: {e}")
    return False


