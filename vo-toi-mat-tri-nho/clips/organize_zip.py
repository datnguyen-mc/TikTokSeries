#!/usr/bin/env python3
"""Giải nén ZIP dự án Flow → clips/full_p04_p25/Pxx-Cy.mp4 (ưu tiên bản R2 > R > gốc; tên bắt đầu bằng X = bản loại, bỏ qua)
và clips/v3/V3_pp-ss.mp4 (bản 'b' thay bản thường cho 01-12, 02-16).
Dùng: python3 clips/organize_zip.py "<đường dẫn zip>" """
import sys, os, re, zipfile, shutil, unicodedata, json
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "full_p04_p25"); V3 = os.path.join(HERE, "v3")
z = zipfile.ZipFile(sys.argv[1]); best = {}; v3 = {}
for n in z.namelist():
    b = unicodedata.normalize("NFC", os.path.basename(n))
    if not b.endswith(".mp4"): continue
    m = re.match(r"P(\d\d)-C(\d)(?:_(R\d?))?_·", b)
    if m:
        cid = f"P{m.group(1)}-C{m.group(2)}"; rank = 0 if not m.group(3) else int(m.group(3)[1:] or 1)
        if cid not in best or rank > best[cid][0]: best[cid] = (rank, n)
    m = re.match(r"V3_(\d\d-\d\d)(b?)_", b)
    if m:
        k = m.group(1); r = 1 if m.group(2) else 0
        if k not in v3 or r > v3[k][0]: v3[k] = (r, n)
def put(n, dst):
    if os.path.exists(dst) and os.path.getsize(dst) == z.getinfo(n).file_size: return
    with z.open(n) as s, open(dst + ".part", "wb") as d: shutil.copyfileobj(s, d)
    os.replace(dst + ".part", dst)
os.makedirs(OUT, exist_ok=True); os.makedirs(V3, exist_ok=True); log = {}
for cid, (rank, n) in sorted(best.items()):
    put(n, os.path.join(OUT, cid + ".mp4")); log[cid] = ["gốc", "R", "R2"][rank]
for k, (r, n) in sorted(v3.items()): put(n, os.path.join(V3, f"V3_{k}.mp4"))
json.dump(log, open(os.path.join(HERE, "nguon_clip.json"), "w"), ensure_ascii=False, indent=1)
print(len(log), "clip;", sum(v != "gốc" for v in log.values()), "bản mới;", len(v3), "shot V3")
