import os,subprocess,fixes
F="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"; FS="/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
V=["-c:v","libx264","-preset","veryfast","-crf","18","-pix_fmt","yuv420p","-r","24","-video_track_timescale","12288"]
A=["-c:a","aac","-b:a","192k","-ar","48000","-ac","2"]
GOLD="0xE9C46A"
GRADE="curves=r='0/0 0.5/0.515 1/1':g='0/0.008 0.5/0.5 1/0.985':b='0/0.03 0.5/0.47 1/0.9',eq=contrast=1.12:saturation=0.82:gamma=0.95,split[ga][gb];[gb]gblur=sigma=14[gg];[ga][gg]blend=all_mode=screen:all_opacity=0.07,eq=brightness=-0.02,vignette=PI/4.8,noise=alls=6:allf=t+u"
def run(c): subprocess.run(["ffmpeg","-v","error","-y"]+c,check=True)
n=[0]
def tf(s):
    n[0]+=1; p=f"build/tr4/t{n[0]}.txt"; open(p,"w").write(s); return p
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
    vf+=text(lines,dur)+["noise=alls=6:allf=t+u","drawbox=x=0:y=0:w=iw:h=92:color=black:t=fill","drawbox=x=0:y=ih-92:w=iw:h=92:color=black:t=fill",f"fade=in:st=0:d=0.5,fade=out:st={dur-0.5}:d=0.5"] if lines else vf+["null"]
    run(src+["-f","lavfi","-i","anullsrc=r=48000:cl=stereo","-t",str(dur),"-vf",",".join(vf)]+V+A+[out])
def seg(out,clip,ss,dur,gain=1.0,subs=(),vfi=0,vfo=0):
    z=0.04 if dur>=2.2 else 0.02
    vf=(fixes.pre(clip)+"," if fixes.pre(clip) else "")+"crop=1280:536:0:92,"
    vf+=f"scale=w='trunc(1280*(1+{z}*t/{dur})/2)*2':h='trunc(536*(1+{z}*t/{dur})/2)*2':eval=frame,crop=1280:536,"+GRADE+",pad=1280:720:0:92:black"
    for (s_,a,b) in subs:
        vf+=f",drawtext=fontfile={F}:textfile={tf(s_)}:fontsize=24:fontcolor=white@0.95:shadowcolor=black@0.8:shadowx=1:shadowy=1:x=(w-text_w)/2:y=h-62:enable='between(t,{a},{b})'"
    if vfi: vf+=f",fade=in:st=0:d={vfi}"
    if vfo: vf+=f",fade=out:st={dur-vfo}:d={vfo}"
    af=f"volume={gain},afade=in:st=0:d=0.08,afade=out:st={dur-0.12}:d=0.12"
    run(["-ss",str(ss),"-i",f"clips/{clip}.mp4","-t",str(dur),"-vf",vf,"-af",af]+V+A+[out])
B=0.3;Q=0.45
P=[("S09_C04",0.5,2.7,B,(),0.8,0),
("S09_C05",0.9,4.1,1,[("Em... nhớ... anh.",0.6,3.6)],0,0.4),
("card",[("H I D D E N    C I N E M A",24,"white",F,-22),("T R Â N    T R Ọ N G    G I Ớ I    T H I Ệ U",15,"white@0.85",F,22)],3.0,False),
("S01_C01",1.0,2.8,B,(),0.4,0),
("S01_C07",1.3,4.0,1,[("Hôm qua bố cũng bận.",0.2,1.5),("Hôm kia cũng bận.",2.7,3.9)]),
("S02_C10",2.0,2.5,B),("S04_C09",1.0,2.5,B),("S06_C10",2.0,2.5,Q,(),0,0.5),
("card",[],0.6,False),
("S07_C08",1.6,4.3,1,[("Anh với cô ấy hết tình cảm lâu rồi.",0.2,1.9),("Ở chung nhà mà như hai người thuê trọ.",2.3,4.2)],0.3,0),
("S07_C01",2.0,1.8,B),
("S10_C02",1.0,4.3,1,[("Bao lâu rồi?",0.3,1.4),("Ba tháng.",3.2,4.1)]),
("S10_C05",1.0,2.2,1,[("Tôi làm gì sai?",0.5,1.7)],0,0.3),
("card",[("M Ộ T    L Ờ I    N Ó I    D Ố I",46,GOLD,FS,-34),("C Ó    T H Ể    L À M    T Ổ N    T H Ư Ơ N G    B A O    N H I Ê U    N G Ư Ờ I ?",19,GOLD,FS,34)],4.0,False),
("S12_C05",0.3,4.2,1,[("Hiền cái gì! Hiền mà đi cướp chồng người ta.",0.2,4.0)]),
("S06_C09",1.5,1.3,Q),("S09_C06",1.5,1.5,Q),("S09_C10",2.5,1.5,B),("S13_C02",1.0,1.4,Q),("S13_C05",3.2,1.8,0.6),
("S13_C06",1.5,4.5,1,[("Chị... chị Diệp.",0.3,1.7),("Cô biết tên tôi cơ à.",2.7,4.2)]),
("S14_C07",2.0,1.5,B),("S15_C05",3.0,1.4,B),("S10_C12",2.0,2.0,B),
("S11_C06",1.8,4.2,1,[("Khôi ơi. Bố mẹ cậu bỏ nhau,",0.2,2.5),("có phải tại cậu không?",2.7,4.0)],0,0.3),
("card",[("M Ộ T    P H I M    N G Ắ N    C Ủ A",16,"white@0.9",F,-40),("H I D D E N    C I N E M A",46,GOLD,FS,14)],3.2,False),
("S15_C08",7.8,4.0,1,[("Ba người, không ai nói thật cả.",0.2,3.8)]),
("S17_C07",0.8,3.0,1,[("Thế sao bố mắng con?",1.0,2.5)]),
("S15_C11",4.5,2.0,B),("S10_C11",1.5,2.0,B),
("S14_C15",8.4,2.9,1,[("Cô còn trẻ. Đừng để ai biến cô thành bí mật của họ.",0.3,2.7)],0,0.5),
("card",[],0.7,False),
("S18_C12",0.8,5.0,1,[("Con chưa tô bố. Để xem đã.",0.4,2.4),("Ừ. Bố đợi.",3.0,4.5)],0.4,0.6),
"TITLE",
("card",[("N G Ã    R Ẽ",104,GOLD,FS,-24),("P H I M    N G Ắ N    ·    2 0 2 6",18,"white@0.9",F,78)],6.0,False)]
parts=[];t=0;title=None;booms=[];blacks=[]
for i,p in enumerate(P):
    if p=="TITLE": title=t; continue
    out=f"build/tr4/{i:02d}.mp4"
    if p[0]=="card":
        (booms if p[1] else blacks).append(t)
        card(out,p[1],p[2],p[3]); t+=p[2]
    else: seg(out,*p); t+=p[2]
    parts.append(out)
open("build/tr4.txt","w").write("".join(f"file '{os.path.abspath(x)}'\n" for x in parts))
run(["-f","concat","-safe","0","-i","build/tr4.txt","-c","copy","build/tr4_nomusic.mp4"])
print("total",t,"title",title)
M="music/Caught in the Middle.mp3"
run(["-f","lavfi","-i","aevalsrc='0.95*sin(2*PI*(58-13*t)*t)*exp(-2.4*t)+0.25*sin(2*PI*(116-20*t)*t)*exp(-5*t)':d=2.4:s=48000","-ac","2","build/tr4/boom.wav"])
run(["-f","lavfi","-i","anoisesrc=d=3.2:c=pink:r=48000:a=0.5","-af","highpass=f=500,lowpass=f=7000,volume='pow(t/3.2,2.5)':eval=frame,afade=out:st=3.1:d=0.1","-ac","2","build/tr4/riser.wav"])
riser_at=max(0,blacks[-1]-3.2)
ins=["-i","build/tr4_nomusic.mp4","-i",M,"-ss","147","-i",M]
fc=(f"[1:a]atrim=0:{title},afade=in:st=0:d=2,afade=out:st={blacks[-1]-0.3}:d=0.3,volume=1.0[ma];"
    f"[2:a]atrim=0:{t-title},afade=in:st=0:d=0.6,afade=out:st={t-title-2.5}:d=2.5,volume=1.6,adelay={int(title*1000)}|{int(title*1000)}[mb];")
lab=["[ma]","[mb]"]
k=3
for bt in booms:
    ins+=["-i","build/tr4/boom.wav"]; fc+=f"[{k}:a]volume=0.9,adelay={int(bt*1000)}|{int(bt*1000)}[s{k}];"; lab.append(f"[s{k}]"); k+=1
ins+=["-i","build/tr4/riser.wav"]; fc+=f"[{k}:a]volume=0.5,adelay={int(riser_at*1000)}|{int(riser_at*1000)}[s{k}];"; lab.append(f"[s{k}]")
fc+="".join(lab)+f"amix=inputs={len(lab)}:normalize=0[m];[0:a]asplit[d1][d2];[m][d1]sidechaincompress=threshold=0.03:ratio=5:attack=40:release=500[md];[d2][md]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=13[a]"
run(ins+["-filter_complex",fc,"-map","0:v","-map","[a]","-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-movflags","+faststart","phim/trailer/nga-re_trailer_v6.mp4"])
print("booms",booms,"blacks",blacks,"DONE")
