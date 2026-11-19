#!/usr/bin/env python3
"""Trích để soát: mỗi shot 8 khung (480x270, ghép 4x2) + âm thanh 16kHz mono; chạy theo lô có giới hạn thời gian."""
import json, os, subprocess, sys, time
V = os.path.expanduser('~/mnt/TikTokSeries/hop-dong-lam-chau/film/v3')
O = V + '/_check2'; os.makedirs(O, exist_ok=True)
budget = float(sys.argv[1]) if len(sys.argv) > 1 else 140
t0 = time.time(); done = 0; left = 0
for f in sorted(os.listdir(V + '/clips')):
    if not f.endswith('.mp4'): continue
    c = f[:-4]; src = f'{V}/clips/{f}'
    jp, wv = f'{O}/{c}.jpg', f'{O}/{c}.wav'
    cn = f'{O}/{c}_cn.jpg'
    if os.path.exists(cn) and os.path.getmtime(cn) > os.path.getmtime(src) and os.path.exists(wv): continue
    if time.time() - t0 > budget: left += 1; continue
    d = float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',src],capture_output=True,text=True).stdout or 4)
    fps = 8 / max(d, 0.5)
    subprocess.run(['ffmpeg','-y','-v','error','-i',src,'-vf',f'fps={fps:.4f},scale=480:270,tile=4x2','-frames:v','1','-q:v','4',jp])
    subprocess.run(['ffmpeg','-y','-v','error','-i',src,'-vn','-ac','1','-ar','16000',wv])
    fc = ("scale=1280:720,split=2[a][b];[a]crop=360:200:0:0[l];[b]crop=360:200:920:0[r];[l][r]hstack")
    subprocess.run(['ffmpeg','-y','-v','error','-ss',f'{d*0.3:.2f}','-i',src,'-ss','0','-frames:v','1','-filter_complex',fc,'-q:v','4',cn+'.a.jpg'])
    subprocess.run(['ffmpeg','-y','-v','error','-ss',f'{d*0.8:.2f}','-i',src,'-frames:v','1','-filter_complex',fc,'-q:v','4',cn+'.b.jpg'])
    subprocess.run(['ffmpeg','-y','-v','error','-i',cn+'.a.jpg','-i',cn+'.b.jpg','-filter_complex','hstack','-q:v','4',cn])
    for x in (cn+'.a.jpg',cn+'.b.jpg'):
        try: os.rename(x, O+'/_tmp_'+os.path.basename(x))
        except OSError: pass
    done += 1
print('xong', done, 'còn', left)
