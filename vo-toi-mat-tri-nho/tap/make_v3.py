#!/usr/bin/env python3
"""Ghép 3 phút bản 3 (P1–P3, shot 3–5s) thành một video 16:9, không phụ đề.
Dùng: python3 tap/make_2phut.py [buoc]   buoc = seg (chuẩn hoá từng shot) | join (ghép + chuẩn âm lượng)
Đọc clips/p01/P01-*.mp4 và clips/p02/P02-*.mp4 theo thứ tự tên."""
import glob, os, subprocess, sys, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TMP = os.path.join(os.path.expanduser("~"), "tapv3_tmp")
OUT = os.path.join(HERE, "Vo_toi_mat_tri_nho_V3_3phut.mp4")
W, H, FPS, SR = 1280, 720, 24, 48000
GRADE = "eq=contrast=1.03:saturation=0.97"

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        sys.exit("ffmpeg lỗi:\n" + r.stderr[-1500:])

def clips():
    nf = lambda s: unicodedata.normalize("NFC", os.path.basename(s))
    out = []
    for part in ("v3",):
        out += sorted(glob.glob(os.path.join(ROOT, "clips", part, "*.mp4")), key=nf)
    return out

def dur(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p], capture_output=True, text=True)
    return float(r.stdout.strip())

def seg():
    os.makedirs(TMP, exist_ok=True)
    for i, src in enumerate(clips()):
        dst = os.path.join(TMP, f"{i:02d}.mov")
        if os.path.exists(dst):
            continue
        d = dur(src)
        vf = f"scale={W}:{H},fps={FPS},{GRADE},format=yuv420p"
        af = f"aresample={SR},afade=t=in:st=0:d=0.03,afade=t=out:st={d-0.05:.3f}:d=0.05"
        run(["ffmpeg", "-y", "-i", src, "-vf", vf, "-af", af, "-c:v", "libx264", "-preset", "medium", "-crf", "16",
             "-c:a", "pcm_s16le", "-ar", str(SR), "-ac", "2", dst])
        print("seg", i, os.path.basename(src), f"{d:.2f}s", flush=True)

def join():
    segs = sorted(glob.glob(os.path.join(TMP, "[0-9][0-9].mov")))
    if len(segs) != len(clips()):
        sys.exit(f"Thiếu đoạn: {len(segs)}/{len(clips())} — chạy bước seg trước")
    lst = os.path.join(TMP, "list.txt")
    open(lst, "w").writelines(f"file '{s}'\n" for s in segs)
    base = os.path.join(TMP, "base.mov")
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", base])
    run(["ffmpeg", "-y", "-i", base, "-af", "loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000,aformat=channel_layouts=stereo",
         "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", OUT])
    print("Xong:", OUT, f"{dur(OUT):.1f}s")

if __name__ == "__main__":
    step = sys.argv[1] if len(sys.argv) > 1 else "seg"
    {"seg": seg, "join": join}[step]()
