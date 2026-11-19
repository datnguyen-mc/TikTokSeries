#!/usr/bin/env python3
"""Gom clip đã tải về ~/Downloads vào film/v3/clips/<mã>.mp4.
- Cảnh 01–06 bản gốc: file V3-<mã>[r]_·_..._<id>.mp4 (bản 'r' = bản sửa logo, ưu tiên).
- Clip tải mới: truyền JSON {mã: id8 video} qua đối số 1 (file _meta/got.json)."""
import glob, json, os, re, shutil, sys
V = os.path.expanduser('~/mnt/TikTokSeries/hop-dong-lam-chau/film/v3')
D = os.path.expanduser('~/mnt/Downloads')
LOCAL = sys.argv[2].split(',') if len(sys.argv) > 2 else []
os.makedirs(V + '/clips', exist_ok=True)
ids = {}
if os.path.exists(V + '/clips/_ids.json'): ids = json.load(open(V + '/clips/_ids.json'))
got = json.load(open(sys.argv[1])) if len(sys.argv) > 1 and os.path.exists(sys.argv[1]) else {}
n = 0
for code in LOCAL:
    fs = sorted(glob.glob(f'{D}/V3-{code}r_*.mp4')) or sorted(glob.glob(f'{D}/V3-{code}_*.mp4'))
    if not fs: print('thiếu bản gốc', code); continue
    shutil.copy2(fs[-1], f'{V}/clips/{code}.mp4'); ids[code] = os.path.basename(fs[-1]); n += 1
for code, vid in got.items():
    fs = [f for f in glob.glob(f'{D}/*_{vid}.mp4')]
    if not fs: print('chưa thấy', code, vid); continue
    if ids.get(code) == vid and os.path.exists(f'{V}/clips/{code}.mp4'): continue
    shutil.copy2(fs[0], f'{V}/clips/{code}.mp4'); ids[code] = vid; n += 1
json.dump(ids, open(V + '/clips/_ids.json', 'w'), indent=0)
print('đã gom', n, '· tổng', len([f for f in os.listdir(V + '/clips') if f.endswith('.mp4')]))
