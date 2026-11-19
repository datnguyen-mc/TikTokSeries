import subprocess,numpy as np,json
L=open('_check4/list.txt').read().split()
W,H=320,180; out={}
reg={'TL':(0,0),'TR':(224,0),'BL':(0,135),'BR':(224,135)}
for c in L:
    raw=subprocess.run(['ffmpeg','-v','error','-i',f'_norm2/{c}.mp4','-vf',f'fps=6,scale={W}:{H},format=gray','-f','rawvideo','-'],capture_output=True).stdout
    F=np.frombuffer(raw,np.uint8).reshape(-1,H,W).astype(np.float32)
    best=(0,'',0)
    for s in range(0,max(1,len(F)-9),3):
        B=F[s:s+9]; sd=B.std(0); m=B.mean(0)
        g=np.abs(np.diff(m,axis=1,prepend=m[:,:1]))+np.abs(np.diff(m,axis=0,prepend=m[:1]))
        mov=np.median(sd)
        if mov<1.5: continue
        lg=(sd<1.2)&(g>30)
        for k,(x,y) in reg.items():
            n=int(lg[y:y+45,x:x+96].sum())
            if n>best[0]: best=(n,k,round(s/6,1))
    out[c]=best
json.dump(out,open('_check4/win.json','w'))
for k,v in sorted(out.items(),key=lambda kv:-kv[1][0])[:25]: print(k,v)
