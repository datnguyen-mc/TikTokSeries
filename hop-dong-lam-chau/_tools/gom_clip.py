#!/usr/bin/env python3
"""Chép clip tải từ Flow (~/Downloads/V3-<shot>_<id8>.mp4) vào film/v3/clips/<shot>.mp4.
  python3 gom_clip.py [thư_mục_downloads]   — bản mới nhất của mỗi shot thắng; ghi đè nếu khác id."""
import glob, os, re, shutil, sys, json
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
CLIPS = os.path.join(ROOT, "film", "v3", "clips"); os.makedirs(CLIPS, exist_ok=True)
D = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/Downloads")
IDS = os.path.join(CLIPS, "_ids.json"); ids = json.load(open(IDS)) if os.path.exists(IDS) else {}
n = 0
for f in sorted(glob.glob(os.path.join(D, "V3-*_*.mp4")), key=os.path.getmtime):
    m = re.match(r"V3-(\d\d[a-z]?-\d\d)_([0-9a-f]{8})\.mp4$", os.path.basename(f))
    if not m or os.path.getsize(f) < 100_000: continue
    c, h = m.groups()
    if ids.get(c) == h and os.path.exists(os.path.join(CLIPS, c + ".mp4")): continue
    shutil.copy2(f, os.path.join(CLIPS, c + ".mp4")); ids[c] = h; n += 1
json.dump(ids, open(IDS, "w"), indent=0, sort_keys=True)
print("chép", n, "· có", len([x for x in os.listdir(CLIPS) if x.endswith(".mp4")]), "clip")
