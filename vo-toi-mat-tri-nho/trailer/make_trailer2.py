#!/usr/bin/env python3
"""Trailer điện ảnh ~1 phút "VỢ TÔI MẤT TRÍ NHỚ CÓ CHỌN LỌC" (giọng A).
Dùng: python3 make_trailer2.py   (đọc clip trong ../clips/trailer và ../clips/p01)
Khung 2.39:1, thẻ chữ chèn trong khung, nhạc nền tổng hợp (drone + nhịp tim + boom) né thoại."""
import glob, os, subprocess, sys, tempfile, unicodedata, wave
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
CLIPS = [os.path.join(HERE, "..", "clips", "trailer"), os.path.join(HERE, "..", "clips", "p01")]
OUT = os.path.join(HERE, "Trailer_1phut_Vo_toi_mat_tri_nho.mp4")
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
W, H, FPS, SR = 1280, 720, 24, 48000
BAR = 92  # 720-2*92 = 536 -> 2.39:1
# (loại, nguồn/chữ, vào, ra)  — card: (chữ, thời lượng, kiểu)
EDL = [
    ("clip", "P01-01", 0.0, 2.4),
    ("card", "MƯỜI NĂM NGÀY CƯỚI", 1.6, "hit"),
    ("clip", "TRAILER-T1", 0.3, 7.1),
    ("clip", "TRAILER-T1", 10.1, 11.6),
    ("card", "CÔ ẤY TỈNH DẬY…|VÀ QUÊN ĐÚNG MỘT NGƯỜI", 1.9, "hit"),
    ("clip", "TRAILER-T2", 4.2, 10.0),
    ("clip", "TRAILER-T3", 3.3, 9.3),
    ("card", "NHƯNG AI MỚI LÀ NGƯỜI ĐANG DIỄN?", 1.6, "hit"),
    ("clip", "TRAILER-T4", 4.2, 8.7),
    ("clip", "TRAILER-T5", 3.2, 8.4),
    ("clip", "TRAILER-T6", 0.6, 3.4),
    ("clip", "TRAILER-T6", 7.0, 9.3),
    ("card", "BA MƯƠI NGÀY.|MỘT CHỦ TỊCH GIẤU MẶT.", 1.9, "hit"),
    ("clip", "TRAILER-T7", 0.2, 14.2),
    ("card", "VỢ TÔI MẤT TRÍ NHỚ|CÓ CHỌN LỌC", 3.4, "title"),
    ("clip", "TRAILER-T8", 0.3, 8.1),
    ("card", "SẮP RA MẮT", 1.8, "end"),
]

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        sys.exit("ffmpeg lỗi:\n" + " ".join(cmd[:6]) + "\n" + r.stderr[-1500:])

def find(code):
    nf = lambda s: unicodedata.normalize("NFC", s)
    for d in CLIPS:
        hits = sorted(p for p in glob.glob(os.path.join(d, "*.mp4")) if nf(os.path.basename(p)).startswith(code))
        if hits:
            return hits[0]
    sys.exit("Thiếu clip " + code)

def text_vf(text, kind, d):
    lines = text.split("|")
    size = {"title": 66, "end": 40, "hit": 44}[kind]
    gap = size * 1.4
    y0 = H / 2 - gap * (len(lines) - 1) / 2
    fi, fo = (0.5, 0.6) if kind == "title" else (0.25, 0.3)
    a = f"if(lt(t,{fi}),t/{fi},if(gt(t,{d}-{fo}),({d}-t)/{fo},1))"
    out = []
    for i, ln in enumerate(lines):
        ln = ln.replace(":", r"\:").replace("'", "’")
        out.append(f"drawtext=fontfile={FONT}:text='{ln}':fontsize={size}:fontcolor=0xF3E7CF:"
                   f"x=(w-text_w)/2:y={y0 + i*gap:.0f}-text_h/2:alpha='{a}'")
    return ",".join(out)

LETTERBOX = f"drawbox=x=0:y=0:w={W}:h={BAR}:color=black:t=fill,drawbox=x=0:y={H-BAR}:w={W}:h={BAR}:color=black:t=fill"
GRADE = "eq=contrast=1.04:saturation=0.96,vignette=PI/5"

def synth(timeline, total):
    """Nhạc nền: drone trầm + nhịp tim + boom ở thẻ chữ; trả về mảng stereo float."""
    n = int(total * SR); t = np.arange(n) / SR
    out = np.zeros(n)
    title_t = next(s for s, k, d in timeline if k == "title")
    # drone dâng dần tới tựa phim, tắt hẳn ở đoạn hài cuối
    env = np.clip(t / title_t, 0, 1) ** 1.5 * (t < title_t)
    env = np.maximum(env * 0.85 + 0.15 * (t < title_t), 0)
    drone = (0.5 * np.sin(2*np.pi*55*t) + 0.3 * np.sin(2*np.pi*82.4*t + 0.5*np.sin(2*np.pi*0.2*t))
             + 0.18 * np.sin(2*np.pi*110*t) * (0.6 + 0.4*np.sin(2*np.pi*0.13*t)))
    out += 0.10 * env * drone
    def thump(at, amp, f0=58, f1=34, dec=7.0, dur=1.6):
        i0 = int(at * SR); m = min(int(dur * SR), n - i0)
        if m <= 0: return
        x = np.arange(m) / SR
        f = f1 + (f0 - f1) * np.exp(-x * 3)
        ph = 2*np.pi*np.cumsum(f) / SR
        out[i0:i0+m] += amp * np.sin(ph) * np.exp(-x * dec)
    # nhịp tim mở đầu và trước tựa phim
    for k in range(3):
        thump(0.15 + k * 0.8, 0.35, dec=14, dur=0.4); thump(0.40 + k * 0.8, 0.25, dec=16, dur=0.3)
    for s, k, d in timeline:
        if k == "hit": thump(s, 0.55)
        if k == "title": thump(s, 0.9, f0=62, f1=28, dec=2.2, dur=3.4)
        if k == "end": thump(s, 0.35, dec=5)
    # tiếng "whoosh" (nhiễu lọc dâng) 1.2 giây trước mỗi thẻ chữ
    rng = np.random.default_rng(7)
    for s, k, d in timeline:
        if k in ("hit", "title"):
            m = int(1.2 * SR); i1 = int(s * SR); i0 = max(0, i1 - m)
            noise = rng.standard_normal(i1 - i0)
            noise = np.convolve(noise, np.ones(24) / 24, mode="same")
            out[i0:i1] += 0.08 * noise * np.linspace(0, 1, i1 - i0) ** 2
    out = np.tanh(out * 1.2) * 0.8
    return np.stack([out, out], 1)

def main():
    tmp = tempfile.mkdtemp()
    segs, timeline, cur = [], [], 0.0
    for n, e in enumerate(EDL):
        seg = os.path.join(tmp, f"{n:02d}.mp4")
        if e[0] == "clip":
            _, code, a, b = e; d = b - a
            vf = f"scale={W}:{H},fps={FPS},{GRADE},{LETTERBOX},fade=t=in:st=0:d=0.06,fade=t=out:st={d-0.08:.3f}:d=0.08,format=yuv420p"
            af = f"aresample={SR},afade=t=in:st=0:d=0.05,afade=t=out:st={d-0.12:.3f}:d=0.12"
            run(["ffmpeg", "-y", "-ss", str(a), "-t", f"{d:.3f}", "-i", find(code), "-vf", vf, "-af", af,
                 "-c:v", "libx264", "-preset", "medium", "-crf", "17", "-c:a", "pcm_s16le", "-ar", str(SR), "-ac", "2", seg.replace(".mp4", ".mov")])
            timeline.append((cur, "clip", d))
        else:
            _, text, d, kind = e
            run(["ffmpeg", "-y", "-f", "lavfi", "-i", f"color=c=black:s={W}x{H}:r={FPS}:d={d}",
                 "-f", "lavfi", "-i", f"anullsrc=r={SR}:cl=stereo", "-t", str(d),
                 "-vf", text_vf(text, kind, d) + ",format=yuv420p", "-c:v", "libx264", "-preset", "medium", "-crf", "17",
                 "-c:a", "pcm_s16le", seg.replace(".mp4", ".mov")])
            timeline.append((cur, kind, d))
        segs.append(seg.replace(".mp4", ".mov")); cur += d
    lst = os.path.join(tmp, "list.txt")
    open(lst, "w").writelines(f"file '{s}'\n" for s in segs)
    base = os.path.join(tmp, "base.mov")
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", base])
    music = synth(timeline, cur)
    mw = os.path.join(tmp, "music.wav")
    with wave.open(mw, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((np.clip(music, -1, 1) * 32767).astype("<i2").tobytes())
    # thoại ưu tiên: nhạc tự hạ khi có tiếng nói
    fc = ("[0:a]aformat=sample_rates=48000:channel_layouts=stereo,asplit=2[dia][sc];"
          "[1:a]aformat=sample_rates=48000:channel_layouts=stereo[mus];"
          "[mus][sc]sidechaincompress=threshold=0.02:ratio=8:attack=20:release=400[duck];"
          "[dia][duck]amix=inputs=2:normalize=0,alimiter=limit=0.95,loudnorm=I=-16:TP=-1.5:LRA=11[a]")
    run(["ffmpeg", "-y", "-i", base, "-i", mw, "-filter_complex", fc, "-map", "0:v", "-map", "[a]",
         "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-movflags", "+faststart", OUT])
    print(f"Xong: {OUT}  ({cur:.1f}s)")
    for s, k, d in timeline:
        print(f"  {s:6.2f}s  {k:5s} {d:.2f}s")

if __name__ == "__main__":
    main()
