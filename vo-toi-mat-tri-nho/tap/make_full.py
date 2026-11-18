#!/usr/bin/env python3
"""Ghép phim đầy đủ: P1–P3 (bản V3 3 phút) + P04–P25 (clip 15s từ Flow, clips/full_p04_p25/Pxx-Cy.mp4).
Dùng: python3 tap/make_full.py seg | parts | full
  seg   : chuẩn hoá từng clip (1280x720, 24fps, PCM 48k, fade âm 30/50ms) vào ~/tapfull_tmp
  parts : ghép từng phần → tap/phan/Pxx_<tên>.mp4 (chuẩn âm lượng -16 LUFS)
  full  : ghép toàn phim → tap/Vo_toi_mat_tri_nho_FULL.mp4"""
import glob, os, subprocess, sys, json, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
TMP = os.path.join(os.path.expanduser("~"), "tapfull_tmp")
CL = os.path.join(ROOT, "clips", "full_p04_p25")
V3 = os.path.join(HERE, "Vo_toi_mat_tri_nho_V3_3phut.mp4")
OUT = os.path.join(HERE, "Vo_toi_mat_tri_nho_FULL.mp4")
PH = os.path.join(HERE, "phan")
W, H, FPS, SR = 1280, 720, 24, 48000
GRADE = "eq=contrast=1.03:saturation=0.97"
LN = "loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000,aformat=channel_layouts=stereo"
def run(c):
    r = subprocess.run(c, capture_output=True, text=True)
    if r.returncode: sys.exit("ffmpeg lỗi:\n" + r.stderr[-1500:])
def dur(p):
    return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p],capture_output=True,text=True).stdout)
def clips():
    return sorted(glob.glob(os.path.join(CL, "P[0-9][0-9]-C[0-9].mp4")))
def titles():
    m = json.load(open(os.path.join(ROOT, "flow_15s", "manifest.json")))
    return {x["part"]: x["title"] for x in m}
def seg():
    os.makedirs(TMP, exist_ok=True)
    jobs = [("P00-V3", V3, False)] + [(os.path.basename(c)[:-4], c, True) for c in clips()]
    for name, src, grade in jobs:
        dst = os.path.join(TMP, name + ".mov")
        if os.path.exists(dst): continue
        d = dur(src)
        vf = f"scale={W}:{H},fps={FPS}," + (GRADE + "," if grade else "") + "format=yuv420p"
        af = f"aresample={SR},afade=t=in:st=0:d=0.03,afade=t=out:st={d-0.05:.3f}:d=0.05"
        part = dst[:-4] + ".part.mov"
        run(["ffmpeg","-y","-i",src,"-vf",vf,"-af",af,"-c:v","libx264","-preset","medium","-crf","17",
             "-c:a","pcm_s16le","-ar",str(SR),"-ac","2",part])
        os.replace(part, dst)
        print("seg", name, f"{d:.2f}s", flush=True)
def concat(segs, out):
    lst = out + ".txt"; open(lst,"w").writelines(f"file '{s}'\n" for s in segs)
    base = out + ".base.mov"
    run(["ffmpeg","-y","-f","concat","-safe","0","-i",lst,"-c","copy",base])
    run(["ffmpeg","-y","-i",base,"-af",LN,"-c:v","copy","-c:a","aac","-b:a","192k","-movflags","+faststart",out])
    os.remove(base)
    return dur(out)
def safe(s):
    return re.sub(r"[^\w\-]+", "_", s, flags=re.U).strip("_")
def parts():
    os.makedirs(PH, exist_ok=True); t = titles()
    by = {}
    for s in sorted(glob.glob(os.path.join(TMP, "P[0-9][0-9]-C[0-9].mov"))):
        by.setdefault(int(os.path.basename(s)[1:3]), []).append(s)
    for p, segs in sorted(by.items()):
        out = os.path.join(PH, f"P{p:02d}_{safe(t.get(p,''))}.mp4")
        print("part", p, len(segs), f"{concat(segs, os.path.join(TMP, f'part{p:02d}.mp4')):.1f}s", flush=True)
        run(["cp", os.path.join(TMP, f"part{p:02d}.mp4"), out])
def full():
    segs = [os.path.join(TMP, "P00-V3.mov")] + sorted(glob.glob(os.path.join(TMP, "P[0-9][0-9]-C[0-9].mov")))
    d = concat(segs, os.path.join(TMP, "full.mp4"))
    run(["cp", os.path.join(TMP, "full.mp4"), OUT]); print("Xong:", OUT, f"{d/60:.1f} phút", flush=True)
if __name__ == "__main__":
    {"seg": seg, "parts": parts, "full": full}[sys.argv[1] if len(sys.argv) > 1 else "seg"]()
