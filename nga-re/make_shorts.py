#!/usr/bin/env python3
# Ngã Rẽ -> shorts 9:16 (1080x1920). Chạy: python3 make_shorts.py [so_phan ...]
import json,os,subprocess,sys,textwrap
from PIL import Image,ImageDraw,ImageFont
P=json.load(open("shorts/SHORTS_PLAN.json")); parts=P["parts"]; N=len(parts)
FB="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
if not os.path.exists(FB): FB="/System/Library/Fonts/Supplemental/Arial Bold.ttf"
def font(s): return ImageFont.truetype(FB,s)
def overlay(path,label,text,color=(255,255,255)):
    im=Image.new("RGBA",(1080,1920),(0,0,0,0)); d=ImageDraw.Draw(im)
    f1=font(38); w=d.textlength(label,font=f1); x=(1080-w)/2
    d.rounded_rectangle([x-26,300,x+w+26,362],radius=31,fill=(196,150,60,255)); d.text((x,309),label,font=f1,fill=(20,16,10,255))
    f2=font(60); lines=textwrap.wrap(text,width=24)[:4]; y=640-len(lines)*76-28
    for l in lines:
        w=d.textlength(l,font=f2); d.text(((1080-w)/2,y),l,font=f2,fill=color+(255,),stroke_width=5,stroke_fill=(0,0,0,255)); y+=76
    im.save(path)
def dur(p): return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p],capture_output=True,text=True).stdout)
only=[int(a) for a in sys.argv[1:]]
for x in parts:
    n=x["n"]
    if only and n not in only: continue
    d=f"shorts/phan-{n:02d}-{x['slug']}"; os.makedirs(d,exist_ok=True); out=f"{d}/nga-re-phan-{n:02d}.mp4"
    if os.path.exists(out) and os.path.getsize(out)>100000 and not only: continue
    src=[f"build/full/{c}.mp4" for c in x["clips"]]; T=sum(dur(s) for s in src)
    label=f"NGÃ RẼ • PHẦN {n}/{N}"
    overlay(f"{d}/_a.png",label,x["hook"]); overlay(f"{d}/_b.png",label,(f"CÒN TIẾP » PHẦN {n+1}" if n<N else "XEM PHIM ĐẦY ĐỦ TRÊN KÊNH"),(255,214,120))
    ins=[]; 
    for s in src: ins+=["-i",s]
    k=len(src); ins+=["-loop","1","-i",f"{d}/_a.png","-loop","1","-i",f"{d}/_b.png"]
    fc="".join(f"[{i}:v]fps=24,format=yuv420p,setsar=1[v{i}];[{i}:a]aresample=48000[a{i}];" for i in range(k))
    fc+="".join(f"[v{i}][a{i}]" for i in range(k))+f"concat=n={k}:v=1:a=1[v][a];"
    fc+="[v]split[m][b];[b]scale=270:480:force_original_aspect_ratio=increase,crop=270:480,gblur=sigma=12,scale=1080:1920,eq=brightness=-0.22:saturation=0.8[bg];"
    fc+="[m]scale=1080:608[fg];[bg][fg]overlay=0:656[c];"
    fc+=f"[c][{k}:v]overlay=0:0:enable='lt(t,{T-2.5:.2f})'[c2];[c2][{k+1}:v]overlay=0:0:enable='gte(t,{T-2.5:.2f})',fade=t=in:st=0:d=0.3,fade=t=out:st={T-0.4:.2f}:d=0.4[vo];"
    fc+=f"[a]loudnorm=I=-14:TP=-1.5:LRA=11,afade=t=out:st={T-0.4:.2f}:d=0.4[ao]"
    r=subprocess.run(["ffmpeg","-v","error","-y"]+ins+["-filter_complex",fc,"-map","[vo]","-map","[ao]","-t",f"{T:.2f}","-c:v","libx264","-preset","veryfast","-crf","20","-pix_fmt","yuv420p","-c:a","aac","-b:a","160k","-ar","48000","-movflags","+faststart",out+".tmp.mp4"],capture_output=True,text=True)
    if r.returncode: print(n,"ERR",r.stderr[-400:]); continue
    os.replace(out+".tmp.mp4",out)
    subprocess.run(["ffmpeg","-v","error","-y","-ss",f"{min(3,T/2):.1f}","-i",out,"-frames:v","1","-q:v","3",f"{d}/cover.jpg"])
    for t in ("_a.png","_b.png"): os.replace(f"{d}/{t}",f"build/sh/{n:02d}{t}")
    print(n,round(T,1),"ok",flush=True)
