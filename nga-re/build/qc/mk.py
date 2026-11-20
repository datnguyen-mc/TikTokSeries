import os,subprocess,sys
cl=sorted(f[:-4] for f in os.listdir('build/full') if f.startswith('S') and f.endswith('.mp4'))
a,b=int(sys.argv[1]),int(sys.argv[2])
for k in range(a,b):
    grp=cl[k*8:(k+1)*8]
    if not grp: break
    rows=[]
    for c in grp:
        p=f'build/full/{c}.mp4'
        d=float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p],capture_output=True,text=True).stdout)
        o=f'build/qc/r_{c}.jpg'
        fps=5/(d-0.3)
        subprocess.run(["ffmpeg","-v","error","-y","-ss","0.15","-i",p,"-vf",f"fps={fps:.4f},scale=384:216,tile=5x1,drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='{c[1:]} {d:.0f}s':fontsize=16:fontcolor=yellow:box=1:boxcolor=black@0.65:x=3:y=3","-frames:v","1","-q:v","5",o])
        rows.append(o)
    ins=[]
    for r in rows: ins+=["-i",r]
    subprocess.run(["ffmpeg","-v","error","-y"]+ins+["-filter_complex",f"vstack=inputs={len(rows)}" if len(rows)>1 else "null","-q:v","5",f"build/qc/sheet_{k:02d}.jpg"])
    print(k,grp[0],grp[-1],flush=True)
