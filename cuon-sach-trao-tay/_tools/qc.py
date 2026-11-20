#!/usr/bin/env python3
"""QC: contact sheet for clips matching prefixes + detect a corner TV logo (saturated R/G/B blobs top-right)."""
import sys,subprocess,os,glob
import numpy as np
P=os.path.expanduser('~/mnt/TikTokSeries/cuon-sach-trao-tay/film')
os.chdir(P)
prefixes=sys.argv[1].split(',')
name=sys.argv[2]
files=sorted(f for f in glob.glob('clips/*.mp4') if os.path.basename(f)[:2] in prefixes)
def frame(f,t,crop=None,w=None):
    vf=[]
    if crop: vf.append('crop='+crop)
    if w: vf.append(f'scale={w}:-2')
    cmd=['ffmpeg','-v','error','-ss',str(t),'-i',f,'-frames:v','1']+(['-vf',','.join(vf)] if vf else [])+['-f','rawvideo','-pix_fmt','rgb24','-']
    return subprocess.run(cmd,capture_output=True).stdout
flag=[]
for f in files:
    raw=frame(f,1.5,'200:110:1060:10')
    if len(raw)!=200*110*3: continue
    a=np.frombuffer(raw,np.uint8).reshape(110,200,3).astype(int)
    r,g,b=a[...,0],a[...,1],a[...,2]
    red=((r>g+80)&(r>b+80)).sum(); grn=((g>r+60)&(g>b+40)).sum(); blu=((b>r+60)&(b>g+40)).sum()
    if red>200 and grn>200 and blu>200: flag.append(os.path.basename(f)[:-4])
# contact sheet
os.makedirs('_qc',exist_ok=True)
tmp='/tmp/qcs'; os.makedirs(tmp,exist_ok=True)
for x in glob.glob(tmp+'/*'): os.remove(x)
for k,f in enumerate(files):
    i=os.path.basename(f)[:-4]
    subprocess.run(['ffmpeg','-v','error','-y','-ss','2','-i',f,'-frames:v','1','-vf',f"scale=320:-2,drawtext=text='{i}':x=6:y=6:fontsize=20:fontcolor=yellow:box=1:boxcolor=black@0.6",f'{tmp}/{k:03d}.jpg'])
cols=6; rows=(len(files)+cols-1)//cols
subprocess.run(['ffmpeg','-v','error','-y','-framerate','1','-i',f'{tmp}/%03d.jpg','-vf',f'tile={cols}x{rows}','-frames:v','1',f'_qc/{name}.jpg'])
print('clips',len(files),'logo_flag',flag,'sheet',f'_qc/{name}.jpg')
