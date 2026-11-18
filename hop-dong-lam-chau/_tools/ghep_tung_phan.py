#!/usr/bin/env python3
"""Ghép phim theo từng đợt (mỗi lần chạy tối đa ~150 giây, chạy lại để tiếp tục).
  python3 ghep_tung_phan.py norm    -> chuẩn hoá clip còn thiếu vào film/v3/_norm/
  python3 ghep_tung_phan.py concat  -> nối thành film/v3/Hop_Dong_Lam_Chau_FULL.mp4"""
import os, sys, time, subprocess
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import ghep_phim as G
NORM = os.path.join(G.ROOT, "film", "v3", "_norm"); os.makedirs(NORM, exist_ok=True)
VF = f"scale={G.W}:{G.H}:force_original_aspect_ratio=decrease,pad={G.W}:{G.H}:(ow-iw)/2:(oh-ih)/2,fps={G.FPS},format=yuv420p"
def one(job):
    c, d = job; dst = os.path.join(NORM, f"{c}.mp4"); tmp = dst + ".part.mp4"
    r = subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", os.path.join(G.CLIPS, f"{c}.mp4"), "-t", str(d), "-vf", VF,
        "-af", "aresample=48000,apad", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-threads", "2",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", tmp], capture_output=True, text=True)
    if r.returncode: return c + " LỖI " + r.stderr[-300:]
    os.replace(tmp, dst); return c
def norm(budget=150):
    t0 = time.time(); P = G.plan()
    jobs = [(c, d) for sc in P for c, d in P[sc] if not os.path.exists(os.path.join(NORM, f"{c}.mp4"))]
    blk = os.path.join(NORM, "_black.mp4")
    if not os.path.exists(blk): G.black(blk)
    done = 0
    with ThreadPoolExecutor(3) as ex:
        futs = []
        for j in jobs:
            futs.append(ex.submit(lambda j=j: one(j) if time.time() - t0 < budget else None))
        for f in futs:
            r = f.result()
            if r and "LỖI" in r: print(r)
            elif r: done += 1
    left = sum(1 for sc in P for c, _ in P[sc] if not os.path.exists(os.path.join(NORM, f"{c}.mp4")))
    print(f"xong {done} clip, còn {left}")
def concat():
    P = G.plan(); segs = []
    for i, sc in enumerate(P):
        if i: segs.append(os.path.join(NORM, "_black.mp4"))
        segs += [os.path.join(NORM, f"{c}.mp4") for c, _ in P[sc]]
    lst = os.path.join(NORM, "list.txt"); open(lst, "w").writelines(f"file '{s}'\n" for s in segs)
    out = os.path.join(G.ROOT, "film", "v3", "Hop_Dong_Lam_Chau_FULL.mp4")
    G.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", "-movflags", "+faststart", out])
    print("Xong:", out, len(segs), "đoạn")
if __name__ == "__main__":
    norm() if sys.argv[1:] == ["norm"] else concat()
