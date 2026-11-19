import os,subprocess,fixes
F="/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"; FB="/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
V=["-c:v","libx264","-preset","veryfast","-crf","18","-pix_fmt","yuv420p","-r","24","-video_track_timescale","12288"]
A=["-c:a","aac","-b:a","192k","-ar","48000","-ac","2"]
LOOK="eq=contrast=1.06:saturation=0.9:brightness=-0.01,drawbox=x=0:y=0:w=iw:h=92:color=black:t=fill,drawbox=x=0:y=ih-92:w=iw:h=92:color=black:t=fill"
def run(c): subprocess.run(["ffmpeg","-v","error","-y"]+c,check=True)
def card(out,lines,dur,sizes,fi=0.5,fo=0.5):
    vf=[];n=len(lines)
    for i,(l,sz) in enumerate(zip(lines,sizes)):
        p=out+f".{i}.txt"; open(p,"w").write(l)
        y=f"(h-text_h)/2+{(i-(n-1)/2)*sz*1.8:.0f}"
        vf.append(f"drawtext=fontfile={FB if sz>60 else F}:textfile={p}:fontsize={sz}:fontcolor=white:x=(w-text_w)/2:y={y}")
    if not lines: vf.append("null")
    vf.append(f"fade=in:st=0:d={fi},fade=out:st={dur-fo}:d={fo}")
    run(["-f","lavfi","-i",f"color=c=black:s=1280x720:r=24:d={dur}","-f","lavfi","-i","anullsrc=r=48000:cl=stereo","-t",str(dur),"-vf",",".join(vf)]+V+A+[out])
def seg(out,clip,ss,dur,gain=1.0,vfi=0,vfo=0):
    vf=(fixes.pre(clip)+"," if fixes.pre(clip) else "")+LOOK
    if vfi: vf+=f",fade=in:st=0:d={vfi}"
    if vfo: vf+=f",fade=out:st={dur-vfo}:d={vfo}"
    af=f"volume={gain},afade=in:st=0:d=0.08,afade=out:st={dur-0.12}:d=0.12"
    run(["-ss",str(ss),"-i",f"clips/{clip}.mp4","-t",str(dur),"-vf",vf,"-af",af]+V+A+[out])
B=0.3
plan=[("card",[],1.0,[]),
("S09_C04",0.5,3.0,B,0.6,0),("S09_C05",0.9,4.1,1,0,0),("S09_C10",2.0,3.0,B,0,0),("S10_C02",1.0,4.3,1,0,0.3),
("card",["Một gia đình bình thường."],2.4,[40]),
("S01_C01",1.0,3.0,B,0.3,0),("S01_C07",1.3,4.0,1,0,0),("S02_C10",2.0,3.0,B,0,0),("S04_C09",1.0,2.8,B,0,0),("S06_C09",1.0,3.0,0.5,0,0),("S06_C10",2.0,3.0,0.5,0,0.3),
("card",["Một lời nói dối."],2.4,[40]),
("S07_C02",0.8,2.4,B,0.3,0),("S07_C08",1.6,4.3,1,0,0),("S10_C05",1.0,2.2,1,0,0),("S12_C05",0.3,4.2,1,0,0),("S13_C02",1.0,2.4,0.5,0,0),("S13_C05",3.0,3.0,0.6,0,0),("S13_C06",1.5,4.5,1,0,0.3),
("card",["Và một đứa trẻ đứng giữa."],2.6,[40]),
("S10_C12",2.0,3.0,B,0.3,0),("S11_C06",1.8,4.2,1,0,0),("S15_C08",7.8,4.0,1,0,0),("S17_C07",0.8,3.0,1,0,0),("S15_C11",4.0,3.5,B,0,0),("S10_C11",1.5,3.0,B,0,0.5),
"CLIMAX_END",
("S14_C15",8.4,2.9,1,0.3,0.4),
("card",[],0.8,[]),
("card",["NGÃ RẼ"],4.5,[110],0.8,0.8),
("S18_C12",0.8,5.0,1,0.4,0.6),
("card",["Một lời nói thật khó nói hôm nay","đỡ đau hơn mười lời nói dối dễ nói."],4.5,[36,36],0.6,1.0)]
parts=[];t=0;climax=None
for i,p in enumerate(plan):
    if p=="CLIMAX_END": climax=t; continue
    out=f"build/tr/{i:02d}.mp4"
    if p[0]=="card": card(out,p[1],p[2],p[3],*(p[4:] if len(p)>4 else ())); t+=p[2]
    else: seg(out,*p); t+=p[2]
    parts.append(out)
open("build/tr.txt","w").write("".join(f"file '{os.path.abspath(x)}'\n" for x in parts))
run(["-f","concat","-safe","0","-i","build/tr.txt","-c","copy","build/tr_nomusic.mp4"])
off=145.0-climax
print("total",t,"climax",climax,"music offset",off)
run(["-i","build/tr_nomusic.mp4","-ss",f"{off}","-i","music/Caught in the Middle.mp3","-filter_complex",
 f"[1:a]atrim=0:{t},afade=in:st=0:d=6,afade=out:st={t-3}:d=3,volume=0.9[m];[0:a]asplit[d1][d2];[m][d1]sidechaincompress=threshold=0.03:ratio=6:attack=40:release=500[md];[d2][md]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]",
 "-map","0:v","-map","[a]","-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-movflags","+faststart","nga-re_trailer_v2.mp4"])
print("DONE")
