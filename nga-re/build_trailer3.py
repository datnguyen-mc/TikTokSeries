import os,subprocess,fixes
F="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"; FS="/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
V=["-c:v","libx264","-preset","veryfast","-crf","18","-pix_fmt","yuv420p","-r","24","-video_track_timescale","12288"]
A=["-c:a","aac","-b:a","192k","-ar","48000","-ac","2"]
GOLD="0xE9C46A"
LOOK="eq=contrast=1.10:saturation=0.84:gamma=0.94,colorbalance=rs=-0.05:bs=0.06:rh=0.05:bh=-0.06,vignette=PI/5,drawbox=x=0:y=0:w=iw:h=92:color=black:t=fill,drawbox=x=0:y=ih-92:w=iw:h=92:color=black:t=fill"
def run(c): subprocess.run(["ffmpeg","-v","error","-y"]+c,check=True)
n=[0]
def tf(s):
    n[0]+=1; p=f"build/tr3/t{n[0]}.txt"; open(p,"w").write(s); return p
def text(lines,dur):
    # lines: (text,size,color,font,yoff)
    out=[]
    for (s,sz,col,font,yo) in lines:
        out.append(f"drawtext=fontfile={font}:textfile={tf(s)}:fontsize={sz}:fontcolor={col}:x=(w-text_w)/2:y=(h-text_h)/2+{yo}:alpha='min(1,min(t/0.7,({dur}-t)/0.7))'")
    return out
def card(out,lines,dur,ember=False):
    if ember:
        src=["-f","lavfi","-i",f"life=s=256x144:r=24:ratio=0.014:mold=24:life_color=#ff9d2e:death_color=#401500:mold_color=#000000"]
        vf=["scale=1280:720:flags=bicubic","gblur=sigma=2.4","eq=brightness=-0.06:contrast=1.2","vignette=PI/3.5"]
    else:
        src=["-f","lavfi","-i",f"color=c=black:s=1280x720:r=24"]; vf=[]
    vf+=text(lines,dur)+["drawbox=x=0:y=0:w=iw:h=92:color=black:t=fill","drawbox=x=0:y=ih-92:w=iw:h=92:color=black:t=fill",f"fade=in:st=0:d=0.5,fade=out:st={dur-0.5}:d=0.5"] if lines else vf+["null"]
    run(src+["-f","lavfi","-i","anullsrc=r=48000:cl=stereo","-t",str(dur),"-vf",",".join(vf)]+V+A+[out])
def seg(out,clip,ss,dur,gain=1.0,subs=(),vfi=0,vfo=0):
    vf=(fixes.pre(clip)+"," if fixes.pre(clip) else "")+LOOK
    for (s,a,b) in subs:
        vf+=f",drawtext=fontfile={F}:textfile={tf(s)}:fontsize=25:fontcolor=white:shadowcolor=black@0.8:shadowx=1:shadowy=1:x=(w-text_w)/2:y=h-64:enable='between(t,{a},{b})'"
    if vfi: vf+=f",fade=in:st=0:d={vfi}"
    if vfo: vf+=f",fade=out:st={dur-vfo}:d={vfo}"
    af=f"volume={gain},afade=in:st=0:d=0.08,afade=out:st={dur-0.12}:d=0.12"
    run(["-ss",str(ss),"-i",f"clips/{clip}.mp4","-t",str(dur),"-vf",vf,"-af",af]+V+A+[out])
B=0.3;Q=0.45
P=[("S09_C04",0.5,2.7,B,(),0.8,0),
("S09_C05",0.9,4.1,1,[("Em... nhớ... anh.",0.6,3.6)],0,0.4),
("card",[("HIDDEN CINEMA",30,"white",F,-22),("TRÂN TRỌNG GIỚI THIỆU",20,"white@0.85",F,22)],3.0,False),
("S01_C01",1.0,2.8,B,(),0.4,0),
("S01_C07",1.3,4.0,1,[("Hôm qua bố cũng bận.",0.2,1.5),("Hôm kia cũng bận.",2.7,3.9)]),
("S02_C10",2.0,2.5,B),("S04_C09",1.0,2.5,B),("S06_C10",2.0,2.5,Q,(),0,0.5),
("card",[],0.6,False),
("S07_C08",1.6,4.3,1,[("Anh với cô ấy hết tình cảm lâu rồi.",0.2,1.9),("Ở chung nhà mà như hai người thuê trọ.",2.3,4.2)],0.3,0),
("S07_C02",0.8,1.8,B),
("S10_C02",1.0,4.3,1,[("Bao lâu rồi?",0.3,1.4),("Ba tháng.",3.2,4.1)]),
("S10_C05",1.0,2.2,1,[("Tôi làm gì sai?",0.5,1.7)],0,0.3),
("card",[("MỘT LỜI NÓI DỐI",54,GOLD,FS,-34),("CÓ THỂ LÀM TỔN THƯƠNG BAO NHIÊU NGƯỜI?",26,GOLD,FS,34)],4.0,False),
("S12_C05",0.3,4.2,1,[("Hiền cái gì! Hiền mà đi cướp chồng người ta.",0.2,4.0)]),
("S06_C09",1.5,1.3,Q),("S09_C06",1.5,1.5,Q),("S09_C10",2.5,1.5,B),("S13_C02",1.0,1.4,Q),("S13_C05",3.2,1.8,0.6),
("S13_C06",1.5,4.5,1,[("Chị... chị Diệp.",0.3,1.7),("Cô biết tên tôi cơ à.",2.7,4.2)]),
("S14_C07",2.0,1.5,B),("S15_C05",3.0,1.4,B),("S10_C12",2.0,2.0,B),
("S11_C06",1.8,4.2,1,[("Khôi ơi. Bố mẹ cậu bỏ nhau,",0.2,2.5),("có phải tại cậu không?",2.7,4.0)],0,0.3),
("card",[("MỘT PHIM NGẮN CỦA",22,"white@0.9",F,-40),("HIDDEN CINEMA",58,GOLD,FS,14)],3.2,False),
("S15_C08",7.8,4.0,1,[("Ba người, không ai nói thật cả.",0.2,3.8)]),
("S17_C07",0.8,3.0,1,[("Thế sao bố mắng con?",1.0,2.5)]),
("S15_C11",4.5,2.0,B),("S10_C11",1.5,2.0,B),
("S14_C15",8.4,2.9,1,[("Cô còn trẻ. Đừng để ai biến cô thành bí mật của họ.",0.3,2.7)],0,0.5),
("card",[],0.7,False),
("S18_C12",0.8,5.0,1,[("Con chưa tô bố. Để xem đã.",0.4,2.4),("Ừ. Bố đợi.",3.0,4.5)],0.4,0.6),
"TITLE",
("card",[("NGÃ RẼ",128,GOLD,FS,-24),("PHIM NGẮN  ·  2026",26,"white@0.9",F,78)],6.0,False)]
parts=[];t=0;title=None
for i,p in enumerate(P):
    if p=="TITLE": title=t; continue
    out=f"build/tr3/{i:02d}.mp4"
    if p[0]=="card": card(out,p[1],p[2],p[3]); t+=p[2]
    else: seg(out,*p); t+=p[2]
    parts.append(out)
open("build/tr3.txt","w").write("".join(f"file '{os.path.abspath(x)}'\n" for x in parts))
run(["-f","concat","-safe","0","-i","build/tr3.txt","-c","copy","build/tr3_nomusic.mp4"])
print("total",t,"title",title)
M="music/Caught in the Middle.mp3"
run(["-i","build/tr3_nomusic.mp4","-i",M,"-ss","147","-i",M,"-filter_complex",
 f"[1:a]atrim=0:{title},afade=in:st=0:d=2,afade=out:st={title-1.5}:d=1.5,volume=1.0[ma];"
 f"[2:a]atrim=0:{t-title},afade=in:st=0:d=0.6,afade=out:st={t-title-2.5}:d=2.5,volume=1.6,adelay={int(title*1000)}|{int(title*1000)}[mb];"
 f"[ma][mb]amix=inputs=2:normalize=0[m];[0:a]asplit[d1][d2];[m][d1]sidechaincompress=threshold=0.03:ratio=5:attack=40:release=500[md];[d2][md]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]",
 "-map","0:v","-map","[a]","-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-movflags","+faststart","nga-re_trailer_v3.mp4"])
print("DONE")
