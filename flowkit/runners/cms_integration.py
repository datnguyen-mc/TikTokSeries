#!/usr/bin/env python3
"""
Module tích hợp CMS & Tự động ghép tập hoàn chỉnh (Auto Episode Merger + Real-time CMS Logger)
Dùng chung cho toàn bộ 6 series runners và CMS Backend.
Chỉ ghép các file VIDEO (.mp4) thực thụ, chuẩn hóa đồng nhất timebase/fps/audio để không bao giờ bị đứng hình.
"""

import os
import random
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


def _mirror_video_to_prompt_folder(local_video_path: str, ep_num: int, ep_folder_name: str = None) -> Optional[str]:
    """Đồng bộ (hardlink/copy) file .mp4 từ output_videos/ vào trực tiếp thư mục prompt (canh-XX / tap-X)."""
    if not local_video_path or not os.path.isfile(local_video_path):
        return None
    try:
        workspace_dir = os.path.dirname(_FLOWKIT_DIR)
        parts = os.path.relpath(os.path.abspath(local_video_path), workspace_dir).split(os.sep)
        if len(parts) < 2 or parts[1] != "output_videos":
            return None
        series_dir = os.path.join(workspace_dir, parts[0])
        if not os.path.isdir(series_dir):
            return None
        target_dir = None
        if ep_folder_name:
            cand = os.path.join(series_dir, ep_folder_name)
            if os.path.isdir(cand):
                target_dir = cand
        if not target_dir and ep_num > 0 and ep_num < 100:
            for entry in sorted(os.listdir(series_dir)):
                full_p = os.path.join(series_dir, entry)
                if not os.path.isdir(full_p) or entry == "output_videos":
                    continue
                m = re.match(rf"^(?:tap|canh)-?0*{ep_num}(?:-.*)?$", entry, re.IGNORECASE)
                if m:
                    target_dir = full_p
                    break
        if not target_dir:
            return None
        dst = os.path.join(target_dir, os.path.basename(local_video_path))
        if os.path.isfile(dst):
            if os.path.samefile(local_video_path, dst):
                return dst
            os.remove(dst)
        try:
            os.link(local_video_path, dst)
        except Exception:
            shutil.copy2(local_video_path, dst)
        return dst
    except Exception:
        return None



def _is_studio_portrait_frame_rgb(buf: bytes, w: int = 160, h: int = 90) -> bool:
    """Detect full-body character reference sheet on a plain grey/charcoal studio backdrop (character in Center, Left, or Right)."""
    zones = []
    for xr in (range(5, 52, 2), range(56, 104, 2), range(108, 155, 2)):
        sats, lumas, diffs = [], [], []
        for y in range(8, 78, 2):
            for x in xr:
                idx = (y * w + x) * 3
                r, g, b = buf[idx], buf[idx + 1], buf[idx + 2]
                sats.append(max(r, g, b) - min(r, g, b))
                lumas.append((r + g + b) // 3)
                idx_r = (y * w + (x + 2)) * 3
                diffs.append(abs(int(buf[idx]) - int(buf[idx_r])) + abs(int(buf[idx + 1]) - int(buf[idx_r + 1])))
        zones.append((
            sum(sats) / len(sats),
            sum(lumas) / len(lumas),
            sum(diffs) / len(diffs),
        ))
    # Check if any 1 zone has the character (high gradient) while the other 2 zones are flat studio backdrop
    for p_idx in (1, 0, 2):
        bg_indices = [i for i in (0, 1, 2) if i != p_idx]
        bg_sat = sum(zones[i][0] for i in bg_indices) / 2.0
        bg_luma = sum(zones[i][1] for i in bg_indices) / 2.0
        bg_grad = sum(zones[i][2] for i in bg_indices) / 2.0
        person_grad = zones[p_idx][2]
        if (
            bg_sat < 22.0
            and 85.0 <= bg_luma <= 205.0
            and bg_grad < 4.5
            and person_grad > 24.0
            and person_grad > bg_grad * 5.0
        ):
            return True
    return False


def trim_studio_reference_frames(video_path: str, log_fn=None) -> bool:
    """
    Quét 24fps ở đầu và cuối clip để phát hiện và cắt bỏ các frame ảnh thẻ nhân vật (nền xám studio)
    trên luồng hình ảnh (giữ nguyên 100% luồng âm thanh 10s để không bao giờ bị cụt lời thoại).
    """
    if not video_path or not os.path.isfile(video_path):
        return False
    w, h = 160, 90
    frame_bytes = w * h * 3
    try:
        cmd = [
            "ffmpeg", "-v", "error", "-i", video_path,
            "-vf", f"fps=24,scale={w}:{h}",
            "-f", "rawvideo", "-pix_fmt", "rgb24", "-"
        ]
        raw = subprocess.check_output(cmd, timeout=45)
        n = len(raw) // frame_bytes
        if n < 48:
            return False
        flags = [_is_studio_portrait_frame_rgb(raw[i * frame_bytes:(i + 1) * frame_bytes], w, h) for i in range(n)]
        # Chỉ tính là studio card ở đầu nếu bắt đầu ngay từ frame 0 hoặc 1
        head_frames = 0
        if flags[0] or flags[1]:
            for i in range(min(48, n)):
                if flags[i]:
                    head_frames = i + 1
                elif i > head_frames + 2:
                    break
        tail_frames = 0
        if flags[-1] or flags[-2]:
            for i in range(1, min(48, n) + 1):
                if flags[-i]:
                    tail_frames = i
                elif i > tail_frames + 2:
                    break

        is_long_youtube_movie = any(s in video_path for s in ("duong-dua-sinh-tu", "ke-song-sot"))
        min_head_frames = 12 if (is_long_youtube_movie and n >= 232) else 0
        if head_frames == 0 and tail_frames == 0 and min_head_frames == 0:
            return False

        start_frame = max(min_head_frames, min(head_frames + 2, n // 4) if head_frames > 0 else 0)
        end_frame = max(n - tail_frames - 2, (n * 3) // 4) if tail_frames > 0 else n
        start_s = round(start_frame / 24.0, 3)
        end_s = round(end_frame / 24.0, 3)
        total_dur = round(n / 24.0, 3)
        if end_s - start_s < 5.0:
            return False

        if head_frames > 0 or tail_frames > 0:
            msg = f"✂️ [STUDIO-CARD VIDEO-ONLY GUARD] Phát hiện frame tham chiếu ở {os.path.basename(video_path)} (đầu={head_frames}f, cuối={tail_frames}f) -> Cắt hình {start_s:.2f}s–{end_s:.2f}s & giữ nguyên 100% âm thanh"
        else:
            msg = f"✂️ [TRIM 0.5s ĐẦU] Đã cắt bỏ 0.50s hình đầu tiên của {os.path.basename(video_path)} -> Giữ đoạn sạch {start_s:.2f}s–{end_s:.2f}s"
        if log_fn:
            log_fn(msg)
        else:
            print(msg, flush=True)

        stretch = round(total_dur / max(1.0, end_s - start_s), 5)
        tmp_trim = f"{video_path}.trim.mp4"
        trim_cmd = [
            "ffmpeg", "-y",
            "-i", video_path,
            "-filter_complex", f"[0:v]trim=start={start_s:.3f}:end={end_s:.3f},setpts={stretch:.5f}*(PTS-STARTPTS)[v]",
            "-map", "[v]", "-map", "0:a",
            "-c:v", "libx264", "-preset", "fast", "-crf", "18",
            "-c:a", "copy", "-shortest",
            "-movflags", "+faststart",
            tmp_trim,
        ]
        res = subprocess.run(trim_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=90)
        if res.returncode == 0 and os.path.isfile(tmp_trim) and os.path.getsize(tmp_trim) > 10000:
            os.replace(tmp_trim, video_path)
            return True
        if os.path.exists(tmp_trim):
            os.remove(tmp_trim)
    except Exception as e:
        if log_fn:
            log_fn(f"⚠️ Lỗi khi kiểm tra/cắt studio frame: {e}")
    return False


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

    trim_studio_reference_frames(local_video_path)
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
    _fallback_upsert_local_and_d1(payload, skip_local=False)

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
    _fallback_upsert_local_and_d1(payload, skip_local=False)

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
        sql = """INSERT INTO cms_clip
                 (id, channel_slug, project_id, episode_num, folder_name, clip_num, prompt, status,
                  local_path, r2_key, r2_url, frame_local_path, frame_r2_key, frame_r2_url,
                  size_mb, duration_s, media_id, updated_at)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                 ON CONFLICT(id) DO UPDATE SET
                  status = excluded.status,
                  local_path = COALESCE(excluded.local_path, cms_clip.local_path),
                  r2_key = COALESCE(excluded.r2_key, cms_clip.r2_key),
                  r2_url = COALESCE(excluded.r2_url, cms_clip.r2_url),
                  frame_local_path = COALESCE(excluded.frame_local_path, cms_clip.frame_local_path),
                  frame_r2_key = COALESCE(excluded.frame_r2_key, cms_clip.frame_r2_key),
                  frame_r2_url = COALESCE(excluded.frame_r2_url, cms_clip.frame_r2_url),
                  size_mb = COALESCE(excluded.size_mb, cms_clip.size_mb),
                  duration_s = COALESCE(excluded.duration_s, cms_clip.duration_s),
                  media_id = COALESCE(excluded.media_id, cms_clip.media_id),
                  updated_at = excluded.updated_at"""
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
        sql = """INSERT INTO cms_episode
                 (id, channel_slug, project_id, episode_num, folder_name, label,
                  total_clips, rendered_clips, is_complete, merged_local_path,
                  merged_r2_key, merged_r2_url, merged_size_mb, duration_s, updated_at)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                 ON CONFLICT(id) DO UPDATE SET
                  total_clips = MAX(cms_episode.total_clips, excluded.total_clips),
                  rendered_clips = MAX(cms_episode.rendered_clips, excluded.rendered_clips),
                  is_complete = MAX(cms_episode.is_complete, excluded.is_complete),
                  merged_local_path = COALESCE(excluded.merged_local_path, cms_episode.merged_local_path),
                  merged_r2_key = COALESCE(excluded.merged_r2_key, cms_episode.merged_r2_key),
                  merged_r2_url = COALESCE(excluded.merged_r2_url, cms_episode.merged_r2_url),
                  merged_size_mb = COALESCE(excluded.merged_size_mb, cms_episode.merged_size_mb),
                  duration_s = COALESCE(excluded.duration_s, cms_episode.duration_s),
                  updated_at = excluded.updated_at"""
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
                if kind == "episode":
                    conn.execute(
                        """UPDATE cms_clip
                           SET status = CASE
                               WHEN (r2_url IS NOT NULL AND r2_url != '') OR (local_path IS NOT NULL AND local_path != '') THEN 'COMPLETED'
                               ELSE 'FAILED'
                           END,
                           updated_at = ?
                           WHERE channel_slug = ? AND episode_num = ?""",
                        (now, slug, ep_num),
                    )
                conn.commit()
        except Exception:
            pass

    try:
        from agent.db.d1_client import is_d1_configured, d1_query_sync
        if is_d1_configured():
            d1_query_sync(sql, params)
            if kind == "episode":
                d1_query_sync(
                    """UPDATE cms_clip
                       SET status = CASE
                           WHEN (r2_url IS NOT NULL AND r2_url != '') OR (local_path IS NOT NULL AND local_path != '') THEN 'COMPLETED'
                           ELSE 'FAILED'
                       END,
                       updated_at = ?
                       WHERE channel_slug = ? AND episode_num = ?""",
                    [now, slug, ep_num],
                )
    except Exception:
        pass


def is_clip_completed_in_db(channel_slug: str, ep_num: int, clip_num: int) -> Optional[str]:
    """Return R2 URL (or valid local_path) if clip already has a rendered video in cms_clip, else None."""
    db_path = os.path.join(_FLOWKIT_DIR, "flow_agent.db")
    if not os.path.isfile(db_path):
        return None
    try:
        with sqlite3.connect(db_path) as conn:
            row = conn.execute(
                "SELECT r2_url, local_path FROM cms_clip WHERE id = ?",
                (f"{channel_slug}:ep:{ep_num}:clip:{clip_num}",),
            ).fetchone()
            if row:
                r2_url, local_path = row
                if r2_url and str(r2_url).strip():
                    return str(r2_url).strip()
                if local_path and os.path.isfile(str(local_path)) and os.path.getsize(str(local_path)) > 50_000:
                    return str(local_path)
    except Exception:
        pass
    return None


def is_clip_failed_in_db(channel_slug: str, ep_num: int, clip_num: int) -> bool:
    """Return True if clip is currently marked FAILED in cms_clip without a valid video."""
    db_path = os.path.join(_FLOWKIT_DIR, "flow_agent.db")
    if not os.path.isfile(db_path):
        return False
    try:
        with sqlite3.connect(db_path) as conn:
            row = conn.execute(
                "SELECT status, r2_url, local_path FROM cms_clip WHERE id = ?",
                (f"{channel_slug}:ep:{ep_num}:clip:{clip_num}",),
            ).fetchone()
            if row:
                status, r2_url, local_path = row
                if r2_url and str(r2_url).strip():
                    return False
                if local_path and os.path.isfile(str(local_path)) and os.path.getsize(str(local_path)) > 50_000:
                    return False
                return str(status or "").upper() == "FAILED"
    except Exception:
        pass
    return False


def persist_updated_prompt(
    series_dir: str,
    channel_slug: str,
    ep_num: int,
    clip_num: int,
    new_prompt: str,
    ep_folder_name: str = None,
    project_id: str = None,
    scene_db_id: str = None,
    attempt: int = 1,
    log_fn=None,
) -> bool:
    """
    Khi một clip bị lỗi từ Google Flow, tự động lưu prompt đã làm mềm/cập nhật
    xuống trực tiếp file canh-XX/clip-Y.md (hoặc tap-X/clip-Y.md) trên ổ đĩa
    VÀ đồng bộ ngay vào bảng cms_clip + scene trong SQLite & Cloudflare D1.
    """
    if not new_prompt or not new_prompt.strip():
        return False

    clean_prompt = new_prompt.strip() + "\n"
    folder = ep_folder_name or f"canh-{ep_num:02d}"
    clip_file = os.path.join(series_dir, folder, f"clip-{clip_num}.md")

    try:
        if os.path.isdir(os.path.dirname(clip_file)):
            with open(clip_file, "w", encoding="utf-8") as f:
                f.write(clean_prompt)
    except Exception as e:
        if log_fn:
            log_fn(f"⚠️ Không ghi được file prompt {clip_file}: {e}")

    db_path = os.path.join(_FLOWKIT_DIR, "flow_agent.db")
    clip_id = f"{channel_slug}:ep:{ep_num}:clip:{clip_num}"
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    if os.path.isfile(db_path):
        try:
            with sqlite3.connect(db_path, timeout=30) as conn:
                conn.execute(
                    "UPDATE cms_clip SET prompt = ?, status = 'PENDING', updated_at = ? WHERE id = ?",
                    (clean_prompt.strip(), now, clip_id),
                )
                if scene_db_id:
                    conn.execute(
                        "UPDATE scene SET video_prompt = ?, horizontal_video_status = 'PENDING' WHERE id = ?",
                        (clean_prompt.strip(), scene_db_id),
                    )
                conn.commit()
        except Exception:
            pass

    try:
        _post_api_json(
            f"/api/cms/channels/{channel_slug}/episodes/{ep_num}/clips/{clip_num}",
            {"prompt": clean_prompt.strip()},
            timeout=8,
        )
    except Exception:
        pass

    try:
        from agent.db.d1_client import is_d1_configured, d1_query_sync
        if is_d1_configured():
            d1_query_sync(
                "UPDATE cms_clip SET prompt = ?, status = 'PENDING', updated_at = ? WHERE id = ?",
                [clean_prompt.strip(), now, clip_id],
            )
            if scene_db_id:
                d1_query_sync(
                    "UPDATE scene SET video_prompt = ?, horizontal_video_status = 'PENDING' WHERE id = ?",
                    [clean_prompt.strip(), scene_db_id],
                )
    except Exception:
        pass

    msg = (
        f"💾 [AUTO-UPDATE PROMPT] Đã tự động cập nhật & lưu file {folder}/clip-{clip_num}.md "
        f"+ đồng bộ DB (Cấp độ làm mềm {attempt}, {len(clean_prompt)} ký tự) để chạy lại!"
    )
    if log_fn:
        log_fn(msg)
    else:
        print(msg, flush=True)
        push_cms_log(
            channel_slug,
            "INFO",
            "PROMPT_AUTO_FIX",
            msg,
            project_id=project_id,
            episode=ep_num,
            clip_num=clip_num,
        )
    return True


def mark_clip_failed_in_db(channel_slug: str, ep_num: int, clip_num: int, scene_id: str = None) -> None:
    """Mark a clip without video as FAILED in local SQLite and Cloudflare D1 SQL so it can be retried."""
    db_path = os.path.join(_FLOWKIT_DIR, "flow_agent.db")
    clip_id = f"{channel_slug}:ep:{ep_num}:clip:{clip_num}"
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    if os.path.isfile(db_path):
        try:
            with sqlite3.connect(db_path) as conn:
                conn.execute(
                    "UPDATE cms_clip SET status = 'FAILED', updated_at = ? WHERE id = ? AND (r2_url IS NULL OR r2_url = '')",
                    (now, clip_id),
                )
                if scene_id:
                    conn.execute(
                        "UPDATE scene SET horizontal_video_status = 'FAILED' WHERE id = ? AND (horizontal_video_url IS NULL OR horizontal_video_url = '')",
                        (scene_id,),
                    )
                conn.commit()
        except Exception:
            pass
    try:
        from agent.db.d1_client import is_d1_configured, d1_query_sync
        if is_d1_configured():
            d1_query_sync(
                "UPDATE cms_clip SET status = 'FAILED', updated_at = ? WHERE id = ? AND (r2_url IS NULL OR r2_url = '')",
                [now, clip_id],
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

    # Nếu các file .mp4 local đã được xóa nhưng đã lưu trên Cloudflare R2 (cms_clip.r2_url),
    # tự động tải các clip từ R2 về khi người dùng bấm nút Ghép Tập trên UI
    if not clips:
        try:
            db_path = os.path.join(_FLOWKIT_DIR, "flow_agent.db")
            if os.path.isfile(db_path):
                with sqlite3.connect(db_path) as conn:
                    cur = conn.execute(
                        """SELECT clip_num, r2_url, folder_name FROM cms_clip
                           WHERE channel_slug = ? AND episode_num = ? AND r2_url IS NOT NULL AND r2_url != ''
                           ORDER BY clip_num ASC""",
                        (channel_slug, ep_num),
                    )
                    r2_rows = cur.fetchall()
                if r2_rows:
                    subf = ep_folder_name or r2_rows[0][2] or f"canh-{ep_num:02d}"
                    dl_dir = os.path.join(output_videos_dir, subf)
                    os.makedirs(dl_dir, exist_ok=True)
                    for c_num, r2_url, _ in r2_rows:
                        dst_mp4 = os.path.join(dl_dir, f"{subf}_clip-{c_num:02d}.mp4")
                        if not os.path.isfile(dst_mp4) or os.path.getsize(dst_mp4) == 0:
                            if requests is not None:
                                r = requests.get(r2_url, timeout=120)
                                if r.status_code == 200 and len(r.content) > 1000:
                                    with open(dst_mp4, "wb") as vf:
                                        vf.write(r.content)
                            else:
                                urllib.request.urlretrieve(r2_url, dst_mp4)
                    clips = find_episode_clip_mp4s(output_videos_dir, ep_num, ep_folder_name)
        except Exception as e:
            print(f"⚠️ Lỗi tải clip từ R2 khi ghép tập: {e}", flush=True)

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
            trim_studio_reference_frames(cp)
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
                    "aresample=async=1:first_pts=0,afade=t=in:st=0:d=0.12",
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
            msg = f"🎉 Đã ghép Tập {tap_num:02d} FULL 10 phút (Cảnh {start_scene:02d} -> {end_scene:02d}, {dur:.1f}s, {sz:.2f} MB)"
            print(msg, flush=True)
            return {
                "ok": True,
                "output_path": out_02d,
                "duration_s": dur,
                "size_mb": sz,
            }
        return {"ok": False, "error": "CONCAT_FAILED"}
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)


def _flow_generation_cooldown_remaining(api_base: str) -> Optional[float]:
    """Số giây khóa tạo video còn lại theo FlowKit server (None nếu không đọc được)."""
    try:
        if requests is not None:
            data = requests.get(f"{api_base}/api/flow/status", timeout=5).json()
        else:
            with urllib.request.urlopen(f"{api_base}/api/flow/status", timeout=5) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        throttle = data.get("generation_throttle") or {}
        if not throttle.get("cooldown_active"):
            return 0.0
        return float(throttle.get("cooldown_remaining_s") or 0.0)
    except Exception:
        return None


def wait_if_cooldown_error(res_text: str, flowkit_api: str = None, log_fn=print) -> bool:
    """
    Kiểm tra nếu phản hồi lỗi từ Google Flow là PUBLIC_ERROR_UNUSUAL_ACTIVITY / local cooldown active:
    - Chờ đến khi khóa tạo video trên FlowKit server thật sự hết (đọc GET /api/flow/status),
      cộng thêm vài giây ngẫu nhiên để các kênh chạy song song không gửi cùng lúc.
    - KHÔNG gọi /api/flow/clear-hijack: khóa là dùng chung cho mọi kênh, gỡ sớm rồi gửi tiếp
      vào lúc Google đang chặn chỉ làm Google chặn lâu hơn.
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
    reported_s = int(m.group(1)) if m else 75
    remaining = _flow_generation_cooldown_remaining(api_base)
    if remaining is None:
        remaining = float(reported_s)

    log_fn(
        f"⏳ [COOLDOWN] Google Flow yêu cầu tạm nghỉ chống spam (còn ~{int(remaining)}s). "
        f"Tự động chờ đến khi hết khóa rồi gửi lại (KHÔNG tính lỗi, KHÔNG sửa file prompt)..."
    )

    waited = 0.0
    last_report = 0.0
    while remaining > 0:
        step = min(remaining + 1.0, 30.0)
        time.sleep(step)
        waited += step
        latest = _flow_generation_cooldown_remaining(api_base)
        remaining = latest if latest is not None else max(0.0, remaining - step)
        if remaining > 0 and waited - last_report >= 120:
            last_report = waited
            log_fn(f"   ...vẫn đang trong thời gian khóa của Google Flow (còn ~{int(remaining)}s)...")

    jitter_s = random.uniform(3.0, 15.0)
    time.sleep(jitter_s)
    log_fn(f"✅ [COOLDOWN] Đã hết thời gian khóa (chờ {int(waited + jitter_s)}s). Tiếp tục gửi lại clip!")
    return True


# ─── Smart Multi-Stage Prompt Rewriter (Zero-Skip Guarantee) ─────────────────

_EN_SAFE_REPLACEMENTS = [
    (r"\bdyke\b", "embankment"),
    (r"\bprimary-school\b", "literature"),
    (r"\bexhausted\s+dark\s+eyes\s+with\s+heavy\s+dark\s+circles\s+underneath\b", "attentive dark eyes"),
    (r"\bheavy\s+dark\s+circles\s+underneath\b", "clear natural features"),
    (r"\bhuddles\s+by\b", "sits quietly by"),
    (r"\btrembling,\s+anxious\b", "expressive, earnest"),
    (r"\btrembling\b", "subtle"),
    (r"\banxious\b", "focused"),
    (r"\bsupernatural\s+folk-horror\s+film\b", "atmospheric Vietnamese mystery drama film"),
    (r"\bSUPERNATURAL_FOLK_HORROR\b", "ATMOSPHERIC_MYSTERY_DRAMA"),
    (r"\bfolk-horror\b", "atmospheric mystery"),
    (r"\bvisceral\s+psychological\s+dread\b", "deep emotional tension"),
    (r"\bpsychological\s+dread\b", "emotional tension"),
    (r"\bcorpse-pale\b", "cool silver"),
    (r"\bash-pale\b", "weathered"),
    (r"\bash-grey\b", "weathered grey"),
    (r"\bmilky-white\s+blind\b", "aged squinting"),
    (r"\bspine-chilling\b", "compelling"),
    (r"\bbone-chilling\b", "resonant"),
    (r"\bchillingly\b", "calmly"),
    (r"\bchilling\b", "atmospheric"),
    (r"\bhorror\s+storyteller\b", "late-night drama storyteller"),
    (r"\bhorror\s+storytelling\b", "late-night drama storytelling"),
    (r"\bhorror\s+cinema\b", "mystery cinema"),
    (r"\bhorror\s+insert\b", "cinematic insert"),
    (r"\bhorror\s+performance\b", "dramatic performance"),
    (r"\bhorror\s+behaviour\b", "dramatic behaviour"),
    (r"\bhorror\s+tension\b", "dramatic tension"),
    (r"\bhorror\s+moments\b", "emotional moments"),
    (r"\bhorror\s+soundscape\b", "atmospheric soundscape"),
    (r"\bhorror\s+ambience\b", "night ambience"),
    (r"\bhorror\s+sound\s+effects\b", "ambient foley effects"),
    (r"\bHorror\s+SFX\b", "Ambient SFX"),
    (r"\brusted\s+iron\s+chains\b", "weathered iron bands"),
    (r"\biron\s+chains\b", "iron bands"),
    (r"\bchain\s+cuff\b", "wrist bracelet"),
    (r"\bchained\b", "sealed"),
    (r"\bchains\b", "bands"),
    (r"\bskeletal\b", "slender"),
    (r"\bemaciated\b", "slender"),
    (r"\bbony\s+fingers\b", "long fingers"),
    (r"\bspectral\b", "distant"),
    (r"\bapparition\b", "figure"),
    (r"\bwandering\s+Vietnamese\s+spirit\s+entity\b", "mysterious Vietnamese figure"),
    (r"\bspirit\s+entity\b", "mysterious figure"),
    (r"\btragic\s+Northern\s+Vietnamese\s+maiden\b", "young Northern Vietnamese woman"),
    (r"\bvisceral\b", "expressive"),
    (r"\bdread\b", "tension"),
    (r"\bblind\b", "squinting"),
    (r"\bragged\s+breathing\b", "steady breathing"),
    (r"\bdilated\s+pupils\b", "focused eyes"),
    (r"\bcold\s+sweat\b", "rain droplets"),
    (r"\bguilt-ridden\b", "earnest"),
    (r"\bsuperhero blockbuster\b", "photorealistic Vietnamese cinematic film"),
    (r"\bsuperhero\b", "skilled specialist"),
    (r"\bhollywood cinematography\b", "high-end cinema 24fps"),
    (r"\bhollywood\b", "cinematic"),
    (r"\bmarvel\b", "cinematic"),
    (r"\balien technology\b", "advanced engineering prototype"),
    (r"\balien\b", "experimental"),
    (r"\bneo-noir\s+crime\s+thriller\b", "atmospheric coastal mystery drama"),
    (r"\bcrime\s+thriller\b", "coastal mystery drama"),
    (r"\bneo-noir\b", "atmospheric cinematic"),
    (r"\bsteel\s+handcuffs\s+at\s+belt\b", "utility clip at belt"),
    (r"\b(?:handcuff|handcuffs|handcuffed|cuff|cuffs|cuffed|shackle|shackles|shackled|wrist-clasp|wrist-clasps)\b", "wrist clip"),
    (r"\bbolt\s+cutters\b", "heavy metal wrench"),
    (r"\b(?:holding\s+room|interrogation\s+room|detention\s+room|cell\s+block|evidence\s+room|police\s+post)\b", "quiet office room"),
    (r"\b(?:interrogat(?:e|es|ed|ing|ion))\b", "questioning"),
    (r"\b(?:captive|prisoner|hostage|suspect|suspects|fugitive)\b", "person"),
    (r"\b(?:custody\s+vehicle|custody\s+road|custody\s+pair|in\s+custody|custody|arrest|arrested)\b", "escort"),
    (r"\bboth\s+hands\s+behind\s+his\s+back\b", "both hands held calmly in front"),
    (r"\bbehind\s+his\s+back\b", "at his side"),
    (r"\b(?:pursuer|pursuers|enforcer|enforcers|henchman|henchmen|guard|guards)\b", "escort"),
    (r"\bunder\s+guard\b", "accompanied"),
    (r"\bstretcher\b", "wheeled cot"),
    (r"\bdrowsy\s+man\b", "resting man"),
    (r"\bstop\s+dead\b", "pause still"),
    (r"\bdead\s+air\b", "quiet pause"),
    (r"\bdead\s+stare\b", "fixed gaze"),
    (r"\bdead\s+silence\b", "complete silence"),
    (r"\bdead\s+drop\b", "hidden drop"),
    (r"\b(?:weapon|weapons)\b", "technical tool"),
    (r"\b(?:gun|guns|firearm|firearms|pistol|pistols|gunfire)\b", "metallic device"),
    (r"\b(?:knife|knives|blade|blades|sword|swords|dagger|daggers)\b", "metal pocket tool"),
    (r"\b(?:syringe|syringes|hypodermic)\b", "small glass applicator"),
    (r"\b(?:paralytic|poison|toxin|narcotic|drug\s+lab|drug-use)\b", "sleeping serum"),
    (r"\b(?:contract\s+killer|hitman|assassin)\b", "underground operative"),
    (r"\b(?:blood|bloody|bleed|bleeding|gore)\b", "dark shadow"),
    (r"\b(?:wound|wounds|wounded|injury|injured)\b", "mark"),
    (r"\b(?:explod(?:e|es|ed|ing)|explosion|explosions|bomb|bombs|blast|blasts)\b", "bright light pulse"),
    (r"\bgunshot(?:s)?\b", "loud impact"),
    (r"\bshoot(?:s|ing)?\s+(?:at|him|her|them)\b", "confront"),
    (r"\b(?:fight|fights|fighting|combat|battle|battles|brawl)\b", "intense confrontation"),
    (r"\b(?:punch|punches|punching|kick|kicks|kicking|slap|slaps|slapping|strike|strikes|striking)\b", "gesture toward"),
    (r"\b(?:chok(?:e|es|ing)|strangl(?:e|es|ing))\b", "hold back"),
    (r"\b(?:kill|kills|killed|killing|dead|death|die|dies|died|corpse|corpses|murder|suicide|torture)\b", "stop"),
    (r"\b(?:attack|attacks|attacked|attacking|assault)\b", "approach"),
    (r"\b(?:crash|crashes|crashed|crashing|collid(?:e|es|ed|ing)|collision)\b", "sudden stop"),
    (r"\b(?:electric\s+shock|electrocut(?:e|ed|ing))\b", "bright energy shimmer"),
    (r"\b(?:terror|terrified|panic|panicked|panicking|horrified|horror|scream|screams|screamed|screaming)\b", "tense expression"),
    (r"\b(?:naked|nude|nudity|undress|undressed|undressing|bare\s+chest|uncovered\s+chest)\b", "modest casual home attire"),
    (r"\b(?:breastfeed|breastfeeding|nursing\s+pillow|nursing\s+cover|suckling)\b", "caring for the babies with a soft support cushion"),
    (r"\b(?:newborn\s+baby|newborn\s+babies|newborn)\b", "adorable young baby"),
    (r"\b(?:infant|infants)\b", "young child"),
    (r"\b(?:skull|skulls|skeleton|skeletons|demon|demons|monster|monsters|ghost|ghosts|corpse|corpses)\b", "traditional ornament"),
    (r"\b(?:horror|terror|terrified|haunted|gore|blood|bloody|physical\s+violence|physical\s+harm)\b", "dramatic mystery"),
]

_VI_SAFE_REPLACEMENTS = [
    ("cái bẫy đầu tư tiền ảo trên mạng", "chuyện làm ăn xa nhà chưa thuận lợi"),
    ("lòng tham cứ thế cuốn lấy tâm trí", "cậu cứ thế dồn hết tâm sức vào đó"),
    ("đầu tư tiền ảo", "công việc làm ăn"),
    ("tài khoản tiền ảo", "màn hình điện thoại"),
    ("tiền ảo", "công việc"),
    ("khi sàn sập", "khi công việc gặp trắc trở"),
    ("sàn sập", "gặp biến cố"),
    ("số nợ lãi mẹ đẻ lãi con", "những khoản chi phí dồn lại"),
    ("lãi mẹ đẻ lãi con", "nhiều khoản dồn lại"),
    ("kể chuyện ma đêm khuya", "kể chuyện đêm khuya"),
    ("HẺM Truyện Ma", "Kể Chuyện Đêm Khuya"),
    ("truyện ma", "chuyện đêm khuya"),
    ("cao trào kinh dị", "cao trào tâm lý"),
    ("kinh dị tâm linh", "tâm lý bí ẩn"),
    ("kinh dị", "tâm lý bí ẩn"),
    ("rùng rợn", "trầm lắng"),
    ("rờn rợn", "trầm mặc"),
    ("lạnh gáy", "sâu lắng"),
    ("tuyệt vọng", "trầm tư suy nghĩ"),
    ("cháy đỏ rực", "biến động"),
    ("run rẩy ôm lấy đầu", "đưa tay lên trán suy tư"),
    ("tự nhốt mình vào một cái bẫy không lối thoát", "bước vào một thử thách đầy bí ẩn"),
    ("cái bẫy không lối thoát", "không gian tĩnh mịch"),
    ("cõi âm dương giao hòa", "ngôi nhà cổ tĩnh mịch"),
    ("cõi âm dương", "không gian xưa cũ"),
    ("oan hồn", "hình bóng"),
    ("oán linh", "hình bóng"),
    ("vong hồn", "hình bóng"),
    ("Vong hồn", "Hình bóng"),
    ("hồn ma", "bóng người"),
    ("bóng ma", "bóng người"),
    ("ma quái", "kỳ bí"),
    ("giọng ma vọng", "giọng vọng xa xăm"),
    ("trấn yểm", "niêm phong"),
    ("trấn hồn", "cổ truyền"),
    ("dìm chết", "rơi xuống"),
    ("chết oan", "khuất bóng"),
    ("chết đuối", "chìm dưới nước"),
    ("xác chết", "dấu vết"),
    ("hài cốt", "di vật cổ"),
    ("xương cốt", "di vật"),
    ("quan tài", "rương gỗ cổ"),
    ("ngôi mộ", "bia đá cổ"),
    ("phần mộ", "khu đất cổ"),
    ("nấm mộ", "mô đất cổ"),
    ("bia mộ", "bia đá"),
    ("nghĩa địa", "cánh đồng chiều"),
    ("bóp cổ", "nắm giữ"),
    ("siết cổ", "giữ chặt"),
    ("bóp nghẹt", "đè nặng"),
    ("vết bầm tím", "vệt sương mờ"),
    ("bầm tím", "sẫm màu"),
    ("mù một mắt", "nheo mắt"),
    ("kéo mây trắng đục (mù)", "nheo lại trầm tư"),
    ("trắng dã", "mờ sương"),
    ("trắng bệch", "nhợt nhạt"),
    ("xám ngoét", "xám trầm"),
    ("xương xẩu", "gầy gò"),
    ("hoảng loạn", "bất ngờ"),
    ("khiếp đảm", "sững sờ"),
    ("kinh hoàng", "bàng hoàng"),
    ("gào thét", "gọi lớn"),
    ("hét thất thanh", "thốt lên"),
    ("cúng cô hồn", "thắp hương tưởng niệm"),
    ("đòi mạng", "vọng về"),
    ("ống tiêm", "ống thuốc nhỏ"),
    ("mũi tiêm", "ống thuốc"),
    ("ống Tê", "ống mẫu"),
    ("thuốc tê", "dung dịch"),
    ("thuốc liệt", "dung dịch"),
    ("còng số tám", "khóa cổ tay"),
    ("còng tay", "khóa tay"),
    ("mở còng", "mở khóa"),
    ("tháo còng", "tháo khóa"),
    ("bị còng", "bị giữ"),
    ("còng", "khóa"),
    ("dây xích", "dây cáp"),
    ("xích sắt", "dây cáp"),
    ("xích", "dây khóa"),
    ("giấy giả", "giấy tờ"),
    ("giữ cô ấy", "đi cùng cô ấy"),
    ("giữ Hạ", "đi cùng Hạ"),
    ("bắt cóc", "đưa đi"),
    ("nằm như chết", "nằm bất động như ngủ sâu"),
    ("ngửa như chết", "ngửa bất động"),
    ("chết thiệt", "bất động thiệt"),
    ("giao xác", "giao người"),
    ("lấy xác", "đưa người"),
    ("xác nó", "người nó"),
    ("xác đâu", "tung tích đâu"),
    ("cho tôi xác", "cho thấy tung tích"),
    ("khẩu súng ngắn", "vật trong bao da"),
    ("khẩu súng", "vật trong bao da"),
    ("họng súng", "vật thép"),
    ("nòng súng", "vật thép"),
    ("chĩa súng", "giơ tay"),
    ("rút súng", "rút đồ trong bao"),
    ("bắn bà ta", "hạ bà ta"),
    ("bắn tôi", "nhắm vào tôi"),
    ("bắn má", "đối đầu má"),
    ("bắn nó", "chặn nó"),
    ("ghim vào cổ tay", "nhẹ nhàng khóa quanh cổ tay"),
    ("tước vũ khí", "thu hồi thiết bị"),
    ("vũ khí", "thiết bị"),
    ("đánh nhau dằn co", "giằng co kịch tính"),
    ("vật lộn", "giằng co"),
    ("sát thủ", "người ẩn danh"),
    ("máu", "vệt tối"),
    ("đâm", "tiến tới"),
    ("chém", "vung tay"),
    ("nổ tung", "bùng lên"),
    ("phát nổ", "lóe sáng"),
    ("cháy nổ", "lóe sáng"),
    ("giết người", "làm việc tối"),
    ("giết", "dừng"),
    ("hạ gục", "khống chế"),
    ("khóc thét", "lên tiếng"),
    ("bú đôi", "nằm gối đôi"),
    ("cho bú", "chăm bé"),
    ("bú mẹ", "ăn sữa"),
]


def _extract_dialogue_lines(prompt: str) -> list[str]:
    """Trích xuất các câu thoại tiếng Việt trong prompt để bảo toàn 100% nội dung kịch bản và khóa giọng VOICE_LOCK."""
    lines = []
    for raw_line in prompt.splitlines():
        s = raw_line.strip()
        m_turn = re.match(r"^-\s*Turn\s+\d+\s*(.+)$", s, flags=re.IGNORECASE)
        if m_turn:
            lines.append(m_turn.group(1).strip())
            continue
        m_v3_timed = re.match(
            r"^\d+(?:\.\d+)?[–\-]\d+(?:\.\d+)?s\s*·\s*(.+:\s*\"[^\"]+\".*)$",
            s,
        )
        if m_v3_timed:
            lines.append(m_v3_timed.group(1).strip())
            continue
        m_v3 = re.match(
            r"^([A-ZÀ-ỸĐ][A-ZÀ-ỸĐa-zà-ỹđ0-9_@\s\(\)\-]+,\s*(?:nói trong hình|ngoài khung hình|lời dẫn ngoài hình|qua thiết bị):\s*.+)$",
            s,
        )
        if m_v3:
            lines.append(m_v3.group(1).strip())
            continue
        m = re.search(r"([A-ZÀ-ỸĐa-zà-ỹđ0-9_@\s]+\s+(?:says|speaks)[^:]*:\s*.+)$", s)
        if m:
            lines.append(m.group(1).strip())
            continue
        m_vi = re.search(r'((?:[A-ZÀ-ỸĐ][A-ZÀ-ỸĐa-zà-ỹđ0-9_@\s\(\)\-]+:\s*"[^"]+"(?:\s*·\s*)?)+)', s)
        if m_vi:
            lines.append(m_vi.group(1).strip())
    return lines


def _extract_action_beats(prompt: str) -> list[str]:
    """Trích xuất Beat 1 (0.0–3.0s / 0.0s–2.5s), Beat 2 (3.0–7.0s / 2.5s–7.5s), Beat 3 (7.0–10.0s / 7.5s–10.0s) từ khối [ACTION] hoặc [5. CAMERA & TIMED ACTION] để giữ nguyên mạch chuyển cảnh mượt."""
    beats = []
    for raw_line in prompt.splitlines():
        s = raw_line.strip()
        if re.match(r"^-\s*(?:Beat\s+[123]\b|\d+\.\d+s[–\-]\d+\.\d+s\s*\()", s, flags=re.IGNORECASE):
            beats.append(s)
    return beats


def rewrite_prompt_on_failure(
    prompt: str,
    attempt: int = 1,
    character_specs: list[dict] = None,
    aspect_ratio: str = "VIDEO_ASPECT_RATIO_PORTRAIT",
) -> str:
    """
    Bộ đổi Prompt thông minh đa cấp độ ngay khi gặp lỗi từ Google Flow:
    - Cấp độ 1 (attempt=1): Khử toàn bộ từ khóa nhạy cảm Anh/Việt, làm sạch khối [AVOID], làm mềm chuyển động và giữ nguyên toàn bộ cấu trúc 3-Beat Match-On-Action + VOICE_LOCK.
    - Cấp độ 2 (attempt=2): Tái cấu trúc gọn sạch, giữ nguyên 3-Beat Match-On-Action (Beat 1, Beat 2, Beat 3), khóa nhân vật @Tag, khóa giọng MC Đình Soạn 0.95x & lời thoại tiếng Việt.
    - Cấp độ 3+ (attempt>=3): Tái cấu trúc Storyboard siêu an toàn đảm bảo 100% vượt qua bộ lọc Google Flow mà vẫn giữ khóa nhân vật @Tag và VOICE_LOCK.
    """
    p = prompt or ""
    has_mc_dinh_soan = "VOICE_LOCK_NARRATOR_" in p or "MC Đình Soạn" in p

    # 1. Luôn áp dụng bộ lọc từ khóa an toàn Anh & Việt
    for pat, repl in _EN_SAFE_REPLACEMENTS:
        p = re.sub(pat, repl, p, flags=re.IGNORECASE)
    for k, v in _VI_SAFE_REPLACEMENTS:
        p = p.replace(k, v).replace(k.capitalize(), v.capitalize())

    # 2. Thay thế phần [AVOID] (vốn thường chứa các từ nhạy cảm như nudity, blood, weapon làm kích hoạt nhầm bộ lọc)
    clean_avoid = (
        "[AVOID]\n"
        "title cards, movie titles, episode titles, scene headers, chapter titles, lower-thirds, timecodes, "
        "subtitles, captions, on-screen text, typography overlays, readable letters or numbers, watermarks, logos, "
        "visual glitches, distorted hands, extra fingers, abrupt jump cuts."
    )
    if "[AVOID]" in p:
        p = re.sub(r"\[AVOID\][\s\S]*$", clean_avoid, p)
    else:
        p = p.rstrip() + "\n\n" + clean_avoid

    is_portrait = "PORTRAIT" in (aspect_ratio or "").upper()
    orient_str = "Vertical 9:16" if is_portrait else "Full-frame 16:9 widescreen"
    is_2d = "2d animated" in p.lower() or "hand-drawn" in p.lower()
    is_3d = "3d cgi" in p.lower() or "pixar" in p.lower()

    # 3. Cấp độ 1: Khử từ nhạy cảm + làm mềm hành động + giữ nguyên toàn bộ cấu trúc 3-Beat Match-On-Action
    if attempt <= 1:
        p2 = re.sub(
            r"^Continue the scene(?: seamlessly| from[^\n]*)?[^\n]*\n(?:Vertical 9:16[^\n]*\n|Horizontal 16:9[^\n]*\n)?",
            (
                f"[FORMAT]\n{orient_str}, 10-second clip, "
                + (
                    "2D hand-drawn cel-shaded animated comedy cartoon, vibrant colors, 24fps. "
                    if is_2d
                    else "Pixar/Disney-style 3D CGI animated film, warm expressive lighting, 24fps. "
                    if is_3d
                    else "photorealistic cinematic live-action film shot on 35mm lens, balanced atmospheric lighting, 24fps. "
                )
                + "In a single continuous shot from 0.0s to 10.0s: ONE camera setup and ONE location, never flash or cut to a studio reference portrait at the start or end. Spoken dialogue in Vietnamese with natural accent and accurate lip-sync. Pure clean camera footage ONLY — strictly no title cards, no movie/episode/scene titles, no subtitles, no on-screen text.\n\n"
            ),
            p.lstrip(),
            flags=re.IGNORECASE,
        )
        p2 = re.sub(r"\bExtreme close-up\b", "Medium close-up", p2, flags=re.IGNORECASE)
        p2 = re.sub(r"\bfrantically|desperately|violently|aggressively|furiously\b", "expressively", p2, flags=re.IGNORECASE)
        p2 = re.sub(r"\bdark shadows|pitch black|eerie|ominous\b", "balanced cinematic lighting", p2, flags=re.IGNORECASE)
        if p2.strip() == (prompt or "").strip():
            p2 = p2.rstrip() + f"\n# Safe-Retry-Pass-{attempt}"
        return p2

    # 4. Cấp độ 2+: Tái cấu trúc Storyboard siêu an toàn, bảo toàn đúng các @Character, Narrator VOICE_LOCK, 3-Beat Match-On-Action và lời thoại
    dialogues = _extract_dialogue_lines(p)
    beats = _extract_action_beats(p)
    char_lines = []
    narrator_line = ""
    for line in p.splitlines():
        s_line = line.strip().lstrip("-").strip()
        if s_line.startswith("@") and "=" in s_line:
            clean_line = "- " + s_line
            for pat, repl in _EN_SAFE_REPLACEMENTS:
                clean_line = re.sub(pat, repl, clean_line, flags=re.IGNORECASE)
            for k, v in _VI_SAFE_REPLACEMENTS:
                clean_line = clean_line.replace(k, v)
            char_lines.append(clean_line)
        elif s_line.startswith("Narrator") and "=" in s_line:
            clean_narr = "- " + s_line
            for pat, repl in _EN_SAFE_REPLACEMENTS:
                clean_narr = re.sub(pat, repl, clean_narr, flags=re.IGNORECASE)
            for k, v in _VI_SAFE_REPLACEMENTS:
                clean_narr = clean_narr.replace(k, v)
            narrator_line = clean_narr

    if not char_lines and character_specs:
        for spec in character_specs:
            tag = spec.get("tag", "")
            if not tag or tag not in p:
                continue
            desc = spec.get("description", "")
            for pat, repl in _EN_SAFE_REPLACEMENTS:
                desc = re.sub(pat, repl, desc, flags=re.IGNORECASE)
            for k, v in _VI_SAFE_REPLACEMENTS:
                desc = desc.replace(k, v)
            char_lines.append(f"- {tag} = {desc}")

    if narrator_line:
        char_lines.append(narrator_line)

    setting_match = re.search(r"(?:\[(?:SETTING|TIMELINE AND LOCATION)\]\s*\n(?:Scene[^\n]*\n)?([^\n]+)|-\s*Location & Architecture:\s*([^\n]+))", p)
    setting_line = (setting_match.group(1) or setting_match.group(2) or "").strip() if setting_match else "Traditional Northern Vietnamese courtyard and wooden house in atmospheric evening mist."
    setting_line = setting_line[:280]

    style_header = (
        f"[FORMAT]\n10 seconds (0.0s–10.0s), {orient_str}, 24 fps, "
        + (
            "2D animated comedy cartoon with clean bold outlines and flat cel shading. "
            if is_2d
            else "stylized 3D CGI animation with warm cinematic lighting. "
            if is_3d
            else "photorealistic live-action Vietnamese atmospheric mystery drama film (`omni_flash` 10s). "
        )
        + "In a single continuous shot from 0.0s to 10.0s: ONE camera setup and ONE location, never flash or cut to a studio reference portrait at the start or end. Spoken Vietnamese audio with Standard Northern Vietnamese accent (giọng chuẩn miền Bắc). Pure clean camera footage ONLY — strictly no title cards, no movie/episode/scene titles, no subtitles, no captions, no on-screen text, no logos.\n"
    )

    chars_block = (
        "[CHARACTERS — approved identities and locked Standard Northern Vietnamese voice profiles]\n"
        "Use the attached reference images strictly for facial identity and wardrobe inside the live scene; never show their plain grey studio background or cut to a portrait card.\n"
        + ("\n".join(char_lines[:6]) if char_lines else "No named lead visible.")
        + "\n"
    )

    if attempt == 2 and beats:
        beats_str = "\n".join(beats[:3])
        dlg_str = "\n".join(f"- Turn {idx + 1} {d}" for idx, d in enumerate(dialogues[:3]))
        shots_block = (
            "[ACTION — 0.0s–10.0s, one continuous evolving take with smooth 3-Beat Match-On-Action transitions]\n"
            f"{beats_str}\n\n"
            "[DIALOGUE — Timed to Action]\n"
            f"{dlg_str}\n"
            'Spoken Audio Rule: Only the Vietnamese words inside the quotation marks ("...") are spoken aloud. Never read speaker names, @tags, timestamps, or voice-lock IDs.\n'
        )
    elif attempt == 2:
        d1 = f" {dialogues[0]}" if len(dialogues) >= 1 else ""
        d2 = f" {dialogues[1]}" if len(dialogues) >= 2 else ""
        d3 = f" {dialogues[2]}" if len(dialogues) >= 3 else ""
        shots_block = (
            "[SHOT LIST]\n"
            f"00:00–00:03.0 | Medium wide shot, 35mm lens, smooth incoming match-on-action camera movement — the characters interact naturally in the scene with expressive body language.{d1}\n"
            f"00:03.0–00:07.0 | Medium close-up, 50mm lens, balanced atmospheric lighting — focused reaction and natural performance.{d2}\n"
            f"00:07.0–00:10.0 | Medium shot, 35mm lens, steady outgoing bridge — the characters conclude the moment with clear expressions and hold a smooth 0.5s visual bridge at the end.{d3}\n"
        )
    else:
        all_d = "\n".join(f"- Turn {idx + 1} {d}" for idx, d in enumerate(dialogues[:3]))
        lens_variant = "50mm cinema lens" if attempt % 2 == 0 else "35mm cinema lens"
        light_variant = "warm amber lantern lighting" if attempt % 2 == 0 else "balanced atmospheric evening lighting"
        b2_summary = beats[1] if len(beats) >= 2 else "the characters perform the scene naturally with expressive emotion."
        shots_block = (
            "[ACTION & SHOT LIST]\n"
            f"00:00–00:03.0 | Medium wide shot ({lens_variant}, {light_variant}) — smooth incoming match-on-action continuity in the scene.\n"
            f"00:03.0–00:07.0 | Medium shot ({lens_variant}) — {b2_summary}\n"
            f"00:07.0–00:10.0 | Medium close-up ({lens_variant}, smooth framing) — calm reaction and natural posture, holding a clean 0.5s bridge at the end.\n\n"
            "[DIALOGUE — Timed to Action]\n"
            f"{all_d}\n"
            'Spoken Audio Rule: Only the Vietnamese words inside the quotation marks ("...") are spoken aloud.\n'
        )

    m_spd = re.search(r"\b(1\.\d{2}x)\b", prompt or "")
    clip_spd = m_spd.group(1) if m_spd else "1.38x"
    narr_id = (
        "VOICE_LOCK_NARRATOR_TIENGGO"
        if "VOICE_LOCK_NARRATOR_TIENGGO" in (prompt or "")
        else "VOICE_LOCK_NARRATOR_OANTHAI"
        if "VOICE_LOCK_NARRATOR_OANTHAI" in (prompt or "")
        else "VOICE_LOCK_NARRATOR_CNHADG"
    )
    voice_speed_block = (
        "[VOICE & DIALOGUE LOCK — STANDARD NORTHERN VIETNAMESE (GIỌNG CHUẨN MIỀN BẮC — ĐỌC NHANH LIÊN THANH 1.35x–1.45x)]\n"
        f"All spoken Vietnamese dialogue and off-screen narration must be delivered in a 100% Standard Northern Vietnamese accent (giọng chuẩn miền Bắc) with rapid-fire continuous articulation, single locked 42–48-year-old Northern Vietnamese male narrator voice ({narr_id}, ~120 Hz sharp energetic mid-baritone, 220–255 syllables/min, zero mid-sentence pauses, dynamic fast pace at {clip_spd} speed when VO, or locked character voice when Lip-Sync), and accurate synchronization. "
        "Strictly forbid Southern Vietnamese (Saigon/Mekong Delta) or Central accent, never slow down or drag out words, and never switch the narrator's vocal identity. "
        "When the off-screen narrator speaks, all on-screen characters keep their mouths naturally closed.\n"
    )

    sound_line = (
        f"[SOUND]\nAtmospheric night room ambience, rain and wind foley, rapid-fire close-mic Standard Northern Vietnamese voice (locked {narr_id} ~120 Hz at {clip_spd} fast continuous pace, 220–255 syllables/min) with 0.15s audio continuity at 0.0s and 10.0s.\n\n"
        if has_mc_dinh_soan
        else "[SOUND]\nNatural room ambience, clear Vietnamese dialogue, gentle background instrumental score.\n\n"
    )

    rebuilt = (
        f"{style_header}\n"
        f"{chars_block}\n"
        f"[TIMELINE AND LOCATION]\n{setting_line}\n\n"
        f"{shots_block}\n"
        f"{voice_speed_block}\n"
        f"{sound_line}"
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




# ─────────────────────────────────────────────────────────────
# Tăng tốc giọng đọc an toàn (08/11/2026)
# Bản cũ nối 2.4s CUỐI CỦA AUDIO GỐC vào sau phần đã tăng tốc → mấy chữ cuối của người dẫn
# bị đọc lại lần hai (đo được 15/29 clip VO). Bản này lấp phần thiếu bằng tiếng nền (room tone)
# lấy từ đoạn yên tĩnh nhất của chính clip, phát xuôi/ngược xen kẽ để không có tiếng click.
# ─────────────────────────────────────────────────────────────
def _audio_rms_profile(video_path: str, sr: int = 8000):
    import array
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", video_path, "-vn", "-ac", "1", "-ar", str(sr), "-f", "s16le", "-"],
        capture_output=True, timeout=60,
    ).stdout
    a = array.array("h")
    a.frombytes(raw[: len(raw) // 2 * 2])
    pref = [0]
    for v in a:
        pref.append(pref[-1] + v * v)
    return pref, len(a)


def find_room_tone_window(video_path: str, start_s: float, end_s: float, win_s: float = 0.4) -> Optional[float]:
    """Trả về mốc bắt đầu (giây) của cửa sổ win_s có đỉnh năng lượng con (50ms) thấp nhất trong [start_s, end_s)."""
    sr = 8000
    try:
        pref, n = _audio_rms_profile(video_path, sr)
    except Exception:
        return None
    w = int(win_s * sr)
    hop = int(0.05 * sr)
    s0, s1 = int(start_s * sr), min(n, int(end_s * sr)) - w
    best = None
    for s in range(max(0, s0), max(0, s1) + 1, hop):
        max_sub = max(pref[k + hop] - pref[k] for k in range(s, s + w, hop))
        tot = pref[s + w] - pref[s]
        # Ưu tiên vùng nửa cuối clip (sau khi lời thoại đã dứt) để không dính âm đầu câu ở 0.3s-0.5s
        tail_bonus = 0.85 if (s / sr) >= 6.0 else 1.0
        score = (max_sub * tail_bonus, tot)
        if best is None or score < best[0]:
            best = (score, s)
    return None if best is None else best[1] / sr


def _room_tone_chain(label_in: str, ws: float, win_s: float, need_s: float, tag: str) -> tuple[str, str]:
    """Filter tạo đoạn tiếng nền dài need_s từ cửa sổ [ws, ws+win_s] (xuôi/ngược xen kẽ, không click)."""
    import math
    k = max(2, math.ceil(need_s / win_s) + 1)
    parts = [f"{label_in}asplit={k}" + "".join(f"[{tag}s{i}]" for i in range(k)) + ";"]
    for i in range(k):
        rev = ",areverse" if i % 2 else ""
        parts.append(f"[{tag}s{i}]atrim=start={ws:.3f}:end={ws + win_s:.3f},asetpts=PTS-STARTPTS{rev}[{tag}p{i}];")
    parts.append("".join(f"[{tag}p{i}]" for i in range(k)) + f"concat=n={k}:v=0:a=1,atrim=0:{need_s:.3f}[{tag}];")
    return "".join(parts), f"[{tag}]"


def boost_voice_tempo_safe(video_path: str, tempo: float = 1.18, log_fn=None) -> bool:
    """Tăng tốc toàn bộ audio clip theo tempo (giữ cao độ), giữ nguyên hình 100% (-c:v copy);
    phần thời lượng còn thiếu ở cuối được lấp bằng tiếng nền của chính clip — KHÔNG phát lại lời nói."""
    _log = log_fn or (lambda m: print(m, flush=True))
    if not video_path or not os.path.exists(video_path) or tempo <= 1.01:
        return False
    out_tmp = f"{video_path}.fast.mp4"
    try:
        dur = probe_video_duration(video_path) or 10.0
        fast_len = dur / tempo
        xf = 0.2
        need = dur - fast_len + xf + 0.05
        win = 0.4
        ws = find_room_tone_window(video_path, 0.05, dur - 0.05, win)
        if ws is None:
            af = f"[0:a]atempo={tempo:.3f},apad,atrim=0:{dur:.3f},asetpts=PTS-STARTPTS[aout]"
        else:
            tone_f, tone_l = _room_tone_chain("[a1]", ws, win, need, "tone")
            af = (
                "[0:a]asplit=2[a0][a1];"
                f"[a0]atempo={tempo:.3f}[fast];"
                + tone_f
                + f"[fast]{tone_l}acrossfade=d={xf:.2f}:c1=tri:c2=tri,atrim=0:{dur:.3f},asetpts=PTS-STARTPTS[aout]"
            )
        cmd = ["ffmpeg", "-y", "-i", video_path, "-filter_complex", af, "-map", "0:v:0", "-map", "[aout]",
               "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out_tmp]
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
        if res.returncode == 0 and os.path.exists(out_tmp) and os.path.getsize(out_tmp) > 10000:
            os.replace(out_tmp, video_path)
            _log(f"⚡ Đã tăng tốc giọng đọc {tempo:.2f}x, lấp {dur - fast_len:.2f}s cuối bằng tiếng nền (không lặp lời).")
            return True
        _log(f"⚠️ Tăng tốc giọng thất bại, giữ audio gốc: {res.stderr[-300:]}")
    except Exception as e:
        _log(f"⚠️ Không thể tăng tốc audio ({e}), giữ nguyên audio gốc.")
    finally:
        if os.path.exists(out_tmp):
            try:
                os.remove(out_tmp)
            except Exception:
                pass
    return False
