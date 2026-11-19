import os,subprocess,sys,fixes
F="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"; FB="/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
V=["-c:v","libx264","-preset","veryfast","-crf","20","-pix_fmt","yuv420p","-r","24","-video_track_timescale","12288"]
A=["-c:a","aac","-b:a","160k","-ar","48000","-ac","2"]
def run(c): subprocess.run(["ffmpeg","-v","error","-y"]+c,check=True)
def txt(name,s):
    p=f"build/txt/{name}.txt"; open(p,"w").write(s); return p
def card(out,lines,dur,sizes):
    vf=[]
    n=len(lines)
    for i,(l,sz) in enumerate(zip(lines,sizes)):
        p=txt(os.path.basename(out)+str(i),l)
        y=f"(h-text_h)/2+{(i-(n-1)/2)*sz*1.7:.0f}"
        vf.append(f"drawtext=fontfile={FB if i==0 else F}:textfile={p}:fontsize={sz}:fontcolor=white:x=(w-text_w)/2:y={y}")
    vf.append(f"fade=in:st=0:d=0.8,fade=out:st={dur-0.8}:d=0.8")
    run(["-f","lavfi","-i",f"color=c=black:s=1280x720:r=24:d={dur}","-f","lavfi","-i",f"anullsrc=r=48000:cl=stereo","-t",str(dur),"-vf",",".join(vf)]+V+A+[out])
# captions: clip -> (text, start, end)
CAP={"S04_C11":("Mẩu giấy: “Cố lên sếp.”",3.5,6.8),"S05_C05":("Tin nhắn chưa gửi: “Anh về chưa”",1.5,6.5),"S05_C12":("Chữ trên bánh: “10 năm”",4.5,8.5),
"S06_C04":("Diệp: “Về đón con, em họp muộn.”",1.5,6.5),"S06_C06":("Khang: “Anh cũng họp. Nhờ bà ngoại đón nhé.”",3.0,7.5),
"S07_C01":("Ba tháng sau",0.8,4.5),"S08_C02":("Khang: “Anh không qua được. Sinh nhật Sóc. Anh xin lỗi.”",1.0,5.5),
"S08_C03":("Trâm: “Không sao ạ.”",3.5,5.8),"S08_C07":("“Con gái tròn 9 tuổi. Cảm ơn bố đã về sớm.”",2.0,9.0),"S08_C08":("Cuộc gọi đến: Mẹ",1.0,6.0),
"S08_C09":("Trâm: “Anh vui nhé.”",4.5,8.0),"S09_C04":("Trâm: “Em nhớ anh. Mai gặp chỗ cũ nhé.”",1.5,5.5),
"S13_C07":("Sóc: “Mẹ ơi mẹ đừng khóc nữa. Con xin lỗi vì con xem điện thoại của bố.”",1.5,8.5)}
CUT={"S12_C05":(7.35,8.62)}
SCENE_START={"S01_C01","S02_C01","S03_C01","S04_C01","S05_C01","S06_C01","S07_C01","S08_C01","S09_C01","S10_C01","S11_C01","S12_C01","S13_C01","S14_C01","S15_C01","S16_C01","S17_C01","S18_C01"}
clips=sorted(f[:-4] for f in os.listdir("clips"))
last={}
for c in clips: last[c[:3]]=c
parts=[]
card("build/full/000_title.mp4",["NGÃ RẼ","phim ngắn"],5,[96,30]); parts.append("build/full/000_title.mp4")
for c in clips:
    out=f"build/full/{c}.mp4"; parts.append(out)
    if os.path.exists(out) and os.path.getsize(out)>10000: continue
    d=float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f"clips/{c}.mp4"],capture_output=True,text=True).stdout)
    vf=[];af=[]
    if c in CUT:
        a,b=CUT[c]; vf.append(f"select='not(between(t,{a},{b}))',setpts=N/FRAME_RATE/TB"); af.append(f"aselect='not(between(t,{a},{b}))',asetpts=N/SR/TB"); d-=(b-a)
    if fixes.pre(c): vf.append(fixes.pre(c))
    if c in SCENE_START: vf.append("fade=in:st=0:d=0.5"); af.append("afade=in:st=0:d=0.3")
    if last[c[:3]]==c:
        fd=2.0 if c=="S18_C13" else 0.5
        vf.append(f"fade=out:st={d-fd-0.05:.2f}:d={fd}"); af.append(f"afade=out:st={d-fd-0.05:.2f}:d={fd}")
    if c in CAP:
        t,s,e=CAP[c]; p=txt(c,t)
        vf.append(f"drawtext=fontfile={F}:textfile={p}:fontsize={40 if c=='S07_C01' else 30}:fontcolor=white:box=1:boxcolor=black@0.55:boxborderw=14:x=(w-text_w)/2:y=h-110:enable='between(t,{s},{e})'")
    cmd=["-i",f"clips/{c}.mp4"]
    if vf: cmd+=["-vf",",".join(vf)]
    if af: cmd+=["-af",",".join(af)]
    run(cmd+V+A+[out+".tmp.mp4"]); os.replace(out+".tmp.mp4",out); print(c,flush=True)
card("build/full/zz1_quote.mp4",["Một lời nói thật khó nói hôm nay","đỡ đau hơn mười lời nói dối dễ nói."],7,[40,40]); parts.append("build/full/zz1_quote.mp4")
card("build/full/zz2_end.mp4",["NGÃ RẼ","Hình ảnh và giọng nói tạo bằng AI · 2026"],5,[80,26]); parts.append("build/full/zz2_end.mp4")
open("build/full.txt","w").write("".join(f"file '{os.path.abspath(p)}'\n" for p in parts))
run(["-f","concat","-safe","0","-i","build/full.txt","-c:v","copy","-af","loudnorm=I=-16:TP=-1.5:LRA=11","-c:a","aac","-b:a","192k","-ar","48000","-movflags","+faststart","nga-re_phim_v6.mp4"])
print("DONE",flush=True)
