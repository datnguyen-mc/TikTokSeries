import os,subprocess,io,json,warnings
warnings.simplefilter("ignore")
from PIL import Image,ImageChops
def frame(c,t):
    p=subprocess.run(["ffmpeg","-v","error","-ss",str(t),"-i",f"clips/{c}.mp4","-frames:v","1","-f","image2pipe","-vcodec","bmp","-"],capture_output=True).stdout
    return Image.open(io.BytesIO(p)).convert("RGB")
def cnt(mask): return mask.histogram()[255]
res=json.load(open("build/detect.json")) if os.path.exists("build/detect.json") else {}
for f in sorted(os.listdir("clips")):
    c=f[:-4]
    if c in res: continue
    d=float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f"clips/{f}"],capture_output=True,text=True).stdout)
    logo=[];bars=[]
    for t in (0.3,d/2,d-0.4):
        im=frame(c,t)
        R,G,B=im.crop((1080,20,1280,140)).split()
        red=ImageChops.multiply(ImageChops.multiply(R.point(lambda v:255*(v>170)),G.point(lambda v:255*(v<70))),B.point(lambda v:255*(v<70)))
        grn=ImageChops.multiply(ImageChops.multiply(G.point(lambda v:255*(v>120)),R.point(lambda v:255*(v<90))),B.point(lambda v:255*(v<110)))
        blu=ImageChops.multiply(ImageChops.multiply(B.point(lambda v:255*(v>130)),R.point(lambda v:255*(v<70))),G.point(lambda v:255*(v<110)))
        logo.append((cnt(red),cnt(grn),cnt(blu)))
        bb=im.convert("L").point(lambda v:255*(v>16)).getbbox()
        bars.append((bb[1],720-bb[3]) if bb else (0,0))
    res[c]={"logo":logo,"bars":bars}
    json.dump(res,open("build/detect.json","w"))
print(len(res))
print("LOGO",{c:v["logo"] for c,v in res.items() if any(r>60 and (g>40 or b>40) for r,g,b in v["logo"])})
print("BARS",{c:v["bars"] for c,v in res.items() if any(t>6 or b>6 for t,b in v["bars"])})
