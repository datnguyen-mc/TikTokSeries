#!/usr/bin/env python3
"""Gom clip Flow đã tải về (~/Downloads/VBN_<shot>_*.mp4) vào film/clips/<shot>.mp4.
Clip trên Flow được đặt tên "VBN <shot> · <tên>" trước khi tải, nên file tải về bắt đầu bằng VBN_<shot>_.
Chạy: python3 ai-la-vo-benh-nhan/_tools/gom_clip.py [thư mục Downloads]   (mặc định ~/mnt/Downloads rồi ~/Downloads)
File mới hơn sẽ ghi đè bản cũ trong film/clips (dùng khi quay lại một shot)."""
import glob, os, re, shutil, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLIPS = os.path.join(ROOT, "film", "clips")
cands = [sys.argv[1]] if len(sys.argv) > 1 else [os.path.expanduser("~/mnt/Downloads"), os.path.expanduser("~/Downloads")]
D = next((d for d in cands if os.path.isdir(d)), None)
if not D:
    sys.exit("Không thấy thư mục Downloads")
os.makedirs(CLIPS, exist_ok=True)
best = {}
for f in glob.glob(os.path.join(D, "VBN_*.mp4")):
    m = re.match(r"VBN_(\d\d-\d\d)_", os.path.basename(f))
    if m and (m.group(1) not in best or os.path.getmtime(f) > os.path.getmtime(best[m.group(1)])):
        best[m.group(1)] = f
new = 0
for code, f in sorted(best.items()):
    dst = os.path.join(CLIPS, code + ".mp4")
    if not os.path.exists(dst) or os.path.getmtime(f) > os.path.getmtime(dst) + 1:
        shutil.copy2(f, dst); new += 1
print(f"{len(best)} clip VBN trong {D}; chép mới {new}; film/clips có {len(glob.glob(os.path.join(CLIPS, '*.mp4')))} file")
