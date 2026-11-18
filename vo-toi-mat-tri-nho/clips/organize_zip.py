#!/usr/bin/env python3
"""Giải nén ZIP dự án Flow → clips/full_p04_p25/Pxx-Cy.mp4, ưu tiên bản R2 > R > bản gốc; bỏ tên bắt đầu bằng X (bản loại).
Dùng: python3 clips/organize_zip.py "<đường dẫn zip>" """
import sys, os, re, zipfile, shutil, unicodedata, json
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "full_p04_p25"); RAW = os.path.join(HERE, "zip_all")
z = zipfile.ZipFile(sys.argv[1]); best = {}
for n in z.namelist():
    b = unicodedata.normalize("NFC", os.path.basename(n))
    m = re.match(r"P(\d\d)-C(\d)(?:_(R2?))?_·", b)
    if not m or not b.endswith(".mp4"): continue
    cid = f"P{m.group(1)}-C{m.group(2)}"; rank = {"R2": 2, "R": 1}.get(m.group(3), 0)
    if cid not in best or rank > best[cid][0]: best[cid] = (rank, n)
os.makedirs(OUT, exist_ok=True); log = {}
for cid, (rank, n) in sorted(best.items()):
    dst = os.path.join(OUT, cid + ".mp4"); tag = ["gốc", "R", "R2"][rank]
    log[cid] = tag
    if os.path.exists(dst) and os.path.getsize(dst) == z.getinfo(n).file_size: continue   # không đổi → giữ nguyên (khỏi chuẩn hoá lại)
    with z.open(n) as s, open(dst + ".part", "wb") as d: shutil.copyfileobj(s, d)
    os.replace(dst + ".part", dst); log[cid] = tag
json.dump(log, open(os.path.join(HERE, "nguon_clip.json"), "w"), ensure_ascii=False, indent=1)
print(len(log), "clip;", sum(v != "gốc" for v in log.values()), "bản mới")
