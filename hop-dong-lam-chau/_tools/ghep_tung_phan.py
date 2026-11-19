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
    dur = getattr(D, "DUR", {})
    return {sc: [(c, dur.get(c, d)) for c, d in shots if c not in D.CUT_SHOTS] for sc, shots in P.items() if sc not in D.CUT_SCENES}

def bars(c):
    """Đo viền đen (đen tuyền, cố định qua 6 khung) ở 4 cạnh, theo pixel trên khung 320x180."""
    src = os.path.join(G.CLIPS, f"{c}.mp4")
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", src, "-vf", "fps=1.5,scale=320:180,format=gray", "-frames:v", "6",
                        "-f", "rawvideo", "-"], capture_output=True)
    b = r.stdout; n = len(b) // (320 * 180)
    if not n: return 0, 0, 0, 0
    fr = [b[i * 57600:(i + 1) * 57600] for i in range(n)]
    def row_dark(y): return all(max(f[y * 320:(y + 1) * 320]) < 22 for f in fr)
    def col_dark(x): return all(max(f[x::320]) < 22 for f in fr)
    t = 0
    while t < 60 and row_dark(t): t += 1
    bo = 0
    while bo < 60 and row_dark(179 - bo): bo += 1
    l = 0
    while l < 100 and col_dark(l): l += 1
    rr = 0
    while rr < 100 and col_dark(319 - rr): rr += 1
    return t, bo, l, rr

def vf_for(c):
    f = []
    if c in getattr(D, "MANUAL_CROP", {}):
        k = D.MANUAL_CROP[c]; t = b = l = r = 0
        f.append(f"crop=iw*{k}:ih*{k}")
    else:
        t, b, l, r = bars(c)
    if not (t and b): t = b = 0          # viền chỉ một phía: coi là cảnh tối, không cắt
    if not (l and r): l = r = 0
    if t + b + l + r > 1 and t < 60 and b < 60:
        # cắt bỏ viền rồi lấy khung 16:9 ở giữa phần còn lại (thêm 1,5% cho sạch mép); tối đa phóng 22%
        ih_keep = (180 - t - b) / 180 - 0.015; iw_keep = (320 - l - r) / 320 - 0.015
        k = min(ih_keep, iw_keep) - (0.06 if (t and b and l and r) else 0)   # khung bo góc: cắt sâu thêm
        k = max(k, 0.78)
        cx = (l + (320 - r)) / 2 / 320; cy = (t + (180 - b)) / 2 / 180
        cx = min(max(cx, k / 2), 1 - k / 2); cy = min(max(cy, k / 2), 1 - k / 2)
        f.append(f"crop=iw*{k:.4f}:ih*{k:.4f}:iw*{cx - k / 2:.4f}:ih*{cy - k / 2:.4f}")
    f.append(f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,fps={FPS}")
    if c in D.NAMES:
        f.append(f"drawtext=fontfile={FONT}:text='{esc(D.NAMES[c])}':fontsize=30:fontcolor=white:x=60:y=h-110:"
                 f"box=1:boxcolor=black@0.45:boxborderw=14:enable='between(t,0.4,3.4)'")
    f.append("format=yuv420p")
    return ",".join(f)

def one(job):
    c, d = job; dst = os.path.join(NORM, f"{c}.mp4"); tmp = dst + ".part.mp4"
    vd = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "format=duration", "-of", "csv=p=0",
                         os.path.join(G.CLIPS, f"{c}.mp4")], capture_output=True, text=True).stdout.strip()
    try: d = min(float(d), float(vd) - 0.04)   # clip ngắn hơn kế hoạch: cắt theo clip, tránh hình đứng / lệch tiếng
    except ValueError: pass
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
    # Hình: nối copy. Tiếng: dựng lại chính xác từng mẫu theo số khung hình của từng đoạn
    # (concat copy tiếng AAC làm dư ~1 gói/đoạn -> tiếng lệch dần, có máy phát bị mất tiếng)
    vtmp = out + ".v.mp4"; araw = out + ".a.raw"
    G.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst, "-an", "-c", "copy", vtmp])
    with open(araw, "wb") as fa:
        for sg in segs:
            nf = int(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v", "-count_packets", "-show_entries",
                 "stream=nb_read_packets", "-of", "csv=p=0", sg], capture_output=True, text=True).stdout.strip())
            fa.write(subprocess.run(["ffmpeg", "-v", "error", "-i", sg, "-vn", "-ac", "2", "-ar", "48000", "-af",
                 f"apad,atrim=end_sample={nf * 48000 // FPS}", "-f", "s16le", "-"], capture_output=True).stdout)
    G.run(["ffmpeg", "-y", "-v", "error", "-i", vtmp, "-f", "s16le", "-ar", "48000", "-ac", "2", "-i", araw, "-map", "0:v", "-map", "1:a",
           "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-movflags", "+faststart", out])
    os.replace(vtmp, os.path.join(NORM, "_last_video_only.mp4")); os.replace(araw, os.path.join(NORM, "_last_audio.raw"))
    print("Xong:", out, len(segs), "đoạn")

if __name__ == "__main__":
    norm() if sys.argv[1:] == ["norm"] else concat()
