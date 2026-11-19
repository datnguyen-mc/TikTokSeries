import subprocess,numpy as np,sys,json
L=open('_check4/list.txt').read().split()
W,H=320,180
res={}
for c in L:
    raw=subprocess.run(['ffmpeg','-v','error','-i',f'_norm2/{c}.mp4','-vf',f'fps=6,scale={W}:{H},format=gray','-f','rawvideo','-'],capture_output=True).stdout
    F=np.frombuffer(raw,np.uint8).reshape(-1,H,W).astype(np.float32)
    if len(F)<6: continue
    sd=F.std(0); mean=F.mean(0)
    gx=np.abs(np.diff(mean,axis=1,prepend=0)); gy=np.abs(np.diff(mean,axis=0,prepend=0)); g=gx+gy
    logo=(sd<3)&(g>25)
    motion=np.median(sd)
    best=(0,None)
    # sliding 48x28 windows
    for y in range(0,H-28,7):
        for x in range(0,W-48,8):
            n=logo[y:y+28,x:x+48].sum()
            if n>best[0]: best=(int(n),(x,y))
    res[c]=(best[0],best[1],round(float(motion),1))
r=sorted(res.items(),key=lambda kv:-(kv[1][0]*(kv[1][2]>2)))
json.dump(res,open('_check4/static.json','w'))
for k,v in r[:40]: print(k,v)
