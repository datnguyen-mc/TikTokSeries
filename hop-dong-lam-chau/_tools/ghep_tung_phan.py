#!/usr/bin/env python3
"""Ghép phim V3.1 theo từng đợt (mỗi lần chạy tối đa ~150 giây, chạy lại để tiếp tục).
  python3 ghep_tung_phan.py norm    -> chuẩn hoá clip (cắt đúng giây, phóng bỏ viền, ghi tên nhân vật) vào film/v3/_norm2/
  python3 ghep_tung_phan.py concat  -> nối thành film/v3/Hop_Dong_Lam_Chau_FULL.mp4, kèm thẻ chữ thời gian/nơi chốn
Kế hoạch dựng (bỏ cảnh nào, thẻ chữ, tên nhân vật) nằm trong dung_phim.py."""
import os, sys, time, subprocess, glob
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import ghep_phim as G
import dung_phim as D
NORM = os.path.join(G.ROOT, "film", "v3", "_norm2"); os.makedirs(NORM, exist_ok=True)
def _font(names):
    for n in names:
        for d in ("/usr/share/fonts", "/System/Library/Fonts", "/Library/Fonts"):
            g = glob.glob(f"{d}/**/{n}", recursive=True)
            if g: return g[0]
    return None
FONT = _font(["DejaVuSerif.ttf", "Times New Roman.ttf", "Georgia.ttf"])
FONT_B = _font(["DejaVuSerif-Bold.ttf", "Times New Roman Bold.ttf", "Georgia Bold.ttf"]) or FONT
W, H, FPS = G.W, G.H, G.FPS

def esc(t):
    return t.replace("\\", "\\\\").replace(":", "\\:").replace("'", "’").replace(",", "\\,")

def plan():
    P = G.plan()
    return {sc: [(c, d) for c, d in shots if c not in D.CUT_SHOTS] for sc, shots in P.items() if sc not in D.CUT_SCENES}

def bars(c):
    """Đo viền đen (trên, dưới, trái, phải) theo tỉ lệ khung, lấy max của 3 khung hình."""
    import numpy as np
    raw = subprocess.run(["ffmpeg", "-v", "error", "-ss", "1", "-i", os.path.join(G.CLIPS, f"{c}.mp4"), "-frames:v", "3",
                          "-vf", "fps=1,scale=320:180,format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
    a = np.frombuffer(raw, np.uint8).reshape(-1, 180, 320).max(0)
    def run(rows):
        n = 0
        for r in rows:
            if r.max() >= 30: break
            n += 1
        return n
    return run(a), run(a[::-1]), run(a.T), run(a.T[::-1])

def vf_for(c):
    f = []
    t, b, l, r = bars(c)
    # chỉ coi là viền khi hai bên đối xứng (cảnh tối một phía không phải viền)
    tb = max(t, b) if abs(t - b) <= 3 and min(t, b) >= 2 else 0
    lr = max(l, r) if abs(l - r) <= 3 and min(l, r) >= 2 else 0
    z = min(max(2 * tb / 180, 2 * lr / 320), 0.22)
    if c in D.CROP or z > 0:
        z = max(z + 0.012, 0.074 if c in D.CROP else 0)
        f.append(f"crop=iw*{1 - z:.3f}:ih*{1 - z:.3f}")
    f.append(f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,fps={FPS}")
    if c in D.NAMES:
        f.append(f"drawtext=fontfile={FONT}:text='{esc(D.NAMES[c])}':fontsize=30:fontcolor=white:x=60:y=h-110:"
                 f"box=1:boxcolor=black@0.45:boxborderw=14:enable='between(t,0.4,3.4)'")
    f.append("format=yuv420p")
    return ",".join(f)

def one(job):
    c, d = job; dst = os.path.join(NORM, f"{c}.mp4"); tmp = dst + ".part.mp4"
    r = subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", os.path.join(G.CLIPS, f"{c}.mp4"), "-t", str(d), "-vf", vf_for(c),
        "-af", "aresample=48000,apad", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-threads", "2",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", "-t", str(d), tmp], capture_output=True, text=True)
    if r.returncode: return c + " LỖI " + r.stderr[-300:]
    os.replace(tmp, dst); return c

def card(name, text, d=2.4, size=46):
    dst = os.path.join(NORM, name)
    if os.path.exists(dst): return dst
    vf = (f"drawtext=fontfile={FONT_B if size > 50 else FONT}:text='{esc(text)}':fontsize={size}:fontcolor=white:"
          f"x=(w-text_w)/2:y=(h-text_h)/2,fade=t=in:st=0:d=0.4,fade=t=out:st={d-0.4}:d=0.4,format=yuv420p")
    G.run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", f"color=c=black:s={W}x{H}:r={FPS}:d={d}", "-f", "lavfi", "-i",
           "anullsrc=r=48000:cl=stereo", "-t", str(d), "-vf", vf, "-c:v", "libx264", "-c:a", "aac", "-ar", "48000", "-ac", "2", dst])
    return dst

def norm(budget=150):
    t0 = time.time(); P = plan()
    miss = [c for sc in P for c, _ in P[sc] if not os.path.exists(os.path.join(G.CLIPS, f"{c}.mp4"))]
    if miss: print("Thiếu clip:", " ".join(miss))
    jobs = [(c, d) for sc in P for c, d in P[sc] if c not in miss and not os.path.exists(os.path.join(NORM, f"{c}.mp4"))]
    blk = os.path.join(NORM, "_black.mp4")
    if not os.path.exists(blk): G.black(blk)
    card("_title.mp4", D.TITLE, d=3.5, size=64)
    for c, t in D.CARDS.items(): card(f"_card_{c}.mp4", t)
    done = 0
    with ThreadPoolExecutor(3) as ex:
        for r in ex.map(lambda j: one(j) if time.time() - t0 < budget else None, jobs):
            if r and "LỖI" in r: print(r)
            elif r: done += 1
    left = sum(1 for sc in P for c, _ in P[sc] if not os.path.exists(os.path.join(NORM, f"{c}.mp4")))
    print(f"xong {done} clip, còn {left}")

def concat():
    P = plan(); segs = [os.path.join(NORM, "_title.mp4")]
    for i, sc in enumerate(P):
        if i: segs.append(os.path.join(NORM, "_black.mp4"))
        for c, _ in P[sc]:
            if c in D.CARDS: segs.append(os.path.join(NORM, f"_card_{c}.mp4"))
            segs.append(os.path.join(NORM, f"{c}.mp4"))
    lst = os.path.join(NORM, "list.txt"); open(lst, "w").writelines(f"file '{s}'\n" for s in segs)
    out = os.path.join(G.ROOT, "film", "v3", "Hop_Dong_Lam_Chau_FULL.mp4")
    G.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", "-movflags", "+faststart", out])
    print("Xong:", out, len(segs), "đoạn")

if __name__ == "__main__":
    norm() if sys.argv[1:] == ["norm"] else concat()
