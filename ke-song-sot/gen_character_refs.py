#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tạo toàn bộ ảnh tham chiếu nhân vật của "Kẻ Sống Sót: Bóng Ma" bằng FlowKit (Nano Banana Pro) từ các prompt trong NHAN_VAT.md.

Cách dùng:
  python3 gen_character_refs.py --dry-run          # chỉ liệt kê prompt sẽ chạy
  python3 gen_character_refs.py                    # tạo tất cả
  python3 gen_character_refs.py --only KHAI NGAN   # chỉ một số nhân vật
  python3 gen_character_refs.py --project <FLOW_PROJECT_ID>

Điều kiện: FlowKit server chạy ở http://127.0.0.1:8200, Chrome Extension đã kết nối, có PROJECT_ID
(lấy từ tham số --project, biến môi trường FLOW_PROJECT_ID, hoặc PROJECT_ID trong flowkit/runners/ke_song_sot.py).
Kết quả: character_refs/<TÊN>.jpg và character_refs/character_media_ids.json (runner đọc được ngay).
"""
import argparse
import json
import os
import re
import sys
import time

import requests

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE = os.path.dirname(BASE_DIR)
FLOWKIT_API = os.environ.get("FLOWKIT_API", "http://127.0.0.1:8200")
BIBLE = os.path.join(BASE_DIR, "NHAN_VAT.md")
OUT_DIR = os.path.join(BASE_DIR, "character_refs")
RUNNER = os.path.join(WORKSPACE, "flowkit", "runners", "ke_song_sot.py")

HANDLE_BY_KEY = {"SON": "@Son", "MAY": "@May", "HA": "@Ha", "HAINGOC": "@HaiNgoc"}
LANDSCAPE_HINTS = ("portrait", "expressions", "lineup")


def load_prompts():
    text = open(BIBLE, encoding="utf-8").read()
    prompts = []
    for block in re.findall(r"```text\n(.*?)```", text, re.DOTALL):
        for line in block.strip().splitlines():
            m = re.match(r"([A-Z]+)_(\d\d)_([a-z_]+):\s*(.+)", line.strip())
            if m:
                key, idx, variant, prompt = m.groups()
                name = f"{key}_{idx}_{variant}"
                aspect = "IMAGE_ASPECT_RATIO_LANDSCAPE" if any(h in variant for h in LANDSCAPE_HINTS) else "IMAGE_ASPECT_RATIO_PORTRAIT"
                prompts.append({"name": name, "key": key, "idx": idx, "variant": variant, "prompt": prompt.strip(), "aspect": aspect})
    return prompts


def resolve_project_id(arg):
    if arg:
        return arg
    if os.environ.get("FLOW_PROJECT_ID"):
        return os.environ["FLOW_PROJECT_ID"]
    try:
        src = open(RUNNER, encoding="utf-8").read()
        m = re.search(r'^PROJECT_ID\s*=\s*"([^"]*)"', src, re.M)
        if m and m.group(1):
            return m.group(1)
    except OSError:
        pass
    return ""


def extract_media_id(data):
    if not isinstance(data, dict):
        return None
    for k in ("_mediaId", "media_id", "mediaId"):
        if data.get(k):
            return data[k]
    medias = data.get("media") or (data.get("data") or {}).get("media") or []
    if medias and isinstance(medias[0], dict):
        return medias[0].get("name") or medias[0].get("media_id") or medias[0].get("mediaId")
    return None


def media_url(media_id):
    for _ in range(20):
        try:
            r = requests.get(f"{FLOWKIT_API}/api/flow/media/{media_id}", timeout=15)
            if r.status_code == 200:
                d = r.json()
                inner = d.get("data") if isinstance(d.get("data"), dict) else d
                for section in ("image", "video", "media"):
                    info = inner.get(section) or {}
                    url = info.get("fifeUrl") or info.get("downloadUrl") or info.get("url")
                    if url and str(url).startswith("http"):
                        return url
                url = inner.get("fifeUrl") or inner.get("downloadUrl")
                if url and str(url).startswith("http"):
                    return url
        except requests.RequestException:
            pass
        time.sleep(3)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", default="")
    ap.add_argument("--only", nargs="*", default=None, help="SON MAY HA HAINGOC DUNG KIEN THANH LINH BAY SONBOY SONYOUNG GOONS")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    prompts = load_prompts()
    if args.only:
        wanted = {k.upper() for k in args.only}
        prompts = [p for p in prompts if p["key"] in wanted]
    print(f"Tìm thấy {len(prompts)} prompt ảnh trong NHAN_VAT.md")
    if args.dry_run:
        for p in prompts:
            print(f"  {p['name']:28s} {p['aspect'].split('_')[-1]:9s} {p['prompt'][:70]}…")
        return 0

    project_id = resolve_project_id(args.project)
    if not project_id:
        print("❌ Chưa có PROJECT_ID Google Flow cho kênh ke-song-sot. Tạo project trên Flow rồi điền trên CMS (http://localhost:8200/) hoặc chạy với --project <id>.")
        return 1
    try:
        h = requests.get(f"{FLOWKIT_API}/health", timeout=5).json()
    except requests.RequestException as e:
        print(f"❌ Không kết nối được FlowKit ({FLOWKIT_API}): {e}")
        return 1
    if not h.get("extension_connected"):
        print("❌ Chrome Extension chưa kết nối. Mở Chrome có FlowKit Extension và giữ một tab Flow project đang đăng nhập.")
        return 1

    os.makedirs(OUT_DIR, exist_ok=True)
    manifest_path = os.path.join(OUT_DIR, "character_refs.json")
    manifest = {}
    if os.path.exists(manifest_path):
        try:
            manifest = json.load(open(manifest_path, encoding="utf-8"))
        except Exception:
            manifest = {}

    for p in prompts:
        if manifest.get(p["name"], {}).get("media_id") and os.path.exists(os.path.join(OUT_DIR, p["name"] + ".jpg")):
            print(f"⏭️  {p['name']} đã có, bỏ qua.")
            continue
        print(f"🎨 {p['name']} …", flush=True)
        try:
            r = requests.post(
                f"{FLOWKIT_API}/api/flow/generate-image",
                json={"prompt": p["prompt"], "project_id": project_id, "aspect_ratio": p["aspect"], "image_model": "nano_banana_pro", "count": 1},
                timeout=180,
            )
        except requests.RequestException as e:
            print(f"   ⚠️ lỗi mạng: {e}")
            continue
        if r.status_code != 200:
            print(f"   ⚠️ HTTP {r.status_code}: {r.text[:200]}")
            continue
        mid = extract_media_id(r.json())
        if not mid:
            print(f"   ⚠️ không lấy được media_id: {str(r.json())[:200]}")
            continue
        url = media_url(mid)
        local = None
        if url:
            try:
                img = requests.get(url, timeout=60)
                if img.status_code == 200:
                    local = os.path.join(OUT_DIR, p["name"] + ".jpg")
                    open(local, "wb").write(img.content)
            except requests.RequestException:
                pass
        manifest[p["name"]] = {"media_id": mid, "file": os.path.basename(local) if local else None, "aspect": p["aspect"]}
        json.dump(manifest, open(manifest_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print(f"   ✅ media_id={mid}" + (f" → {os.path.basename(local)}" if local else " (chưa tải được file, thử lại sau)"))
        time.sleep(4)

    # Ghi cache để runner khóa nhân vật ngay: ảnh _01_ của 5 handle chính
    locked = {}
    for key, handle in HANDLE_BY_KEY.items():
        for name, info in manifest.items():
            if name.startswith(f"{key}_01_") and info.get("media_id"):
                locked[handle] = info["media_id"]
    cache_path = os.path.join(OUT_DIR, "character_media_ids.json")
    cache = {}
    if os.path.exists(cache_path):
        try:
            cache = json.load(open(cache_path, encoding="utf-8"))
        except Exception:
            cache = {}
    cache[project_id] = {**cache.get(project_id, {}), **locked}
    json.dump(cache, open(cache_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"\n🔒 Đã ghi {len(locked)} handle vào {cache_path}: {locked}")
    print(f"📁 Ảnh và manifest ở {OUT_DIR}. Tải thêm các ảnh REF_ (Lão Sáu, Hạnh, Bình…) vào project Flow và giữ đúng tên file.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
