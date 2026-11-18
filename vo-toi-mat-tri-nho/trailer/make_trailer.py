#!/usr/bin/env python3
"""Ghép trailer "VỢ TÔI MẤT TRÍ NHỚ CÓ CHỌN LỌC" từ clip Flow phần 1.
Dùng: python3 make_trailer.py <thư_mục_clip> [file_ra.mp4]
Clip được nhận theo tiền tố tên file "P01-XX" (tên đặt trên Flow)."""
import glob, os, subprocess, sys, tempfile, unicodedata

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
W, H, FPS = 1280, 720, 24
# (loại, nội dung, thời lượng)
EDL = [
    ("clip", "P01-01", 3.0),
    ("card", "MƯỜI NĂM NGÀY CƯỚI", 2.0),
    ("clip", "P01-02", 3.0),
    ("clip", "P01-03", 4.0),
    ("clip", "P01-07", 5.0),
    ("card", "ANH GỬI HOA…|VÀ MỘT LỜI NÓI DỐI", 2.4),
    ("clip", "P01-04", 5.0),
    ("clip", "P01-11", 4.0),
    ("clip", "P01-12", 5.0),
    ("clip", "P01-13", 4.0),
    ("clip", "P01-14", 4.0),
    ("clip", "P01-15", 3.0),
    ("title", "VỢ TÔI MẤT TRÍ NHỚ|CÓ CHỌN LỌC", 3.8),
    ("card", "SẮP RA MẮT", 2.2),
]

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        sys.exit("ffmpeg lỗi:\n" + r.stderr[-1500:])

def find_clip(folder, code):
    nf = lambda s: unicodedata.normalize("NFC", s)
    hits = sorted(p for p in glob.glob(os.path.join(folder, "**", "*.mp4"), recursive=True)
                  if nf(os.path.basename(p)).startswith(code))
    return hits[0] if hits else None

def text_filter(text, big, d):
    lines = text.split("|")
    size = 64 if big else 44
    gap = size * 1.35
    y0 = H / 2 - gap * (len(lines) - 1) / 2
    alpha = f"if(lt(t,0.4),t/0.4,if(gt(t,{d}-0.4),({d}-t)/0.4,1))"
    parts = []
    for i, ln in enumerate(lines):
        ln = ln.replace(":", r"\:").replace("'", "’")
        parts.append(f"drawtext=fontfile={FONT}:text='{ln}':fontsize={size}:fontcolor=0xF2E6D0:"
                     f"x=(w-text_w)/2:y={y0 + i*gap:.0f}-text_h/2:alpha='{alpha}'")
    return ",".join(parts)

def main():
    src = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "Trailer_Vo_toi_mat_tri_nho.mp4")
    missing = [c for k, c, _ in EDL if k == "clip" and not find_clip(src, c)]
    if missing:
        sys.exit("Thiếu clip: " + ", ".join(missing))
    tmp = tempfile.mkdtemp()
    segs = []
    for n, (kind, val, d) in enumerate(EDL):
        seg = os.path.join(tmp, f"{n:02d}.mp4")
        if kind == "clip":
            vf = (f"scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,fps={FPS},"
                  f"fade=t=in:st=0:d=0.12,fade=t=out:st={d-0.15}:d=0.15,format=yuv420p")
            af = f"aresample=48000,afade=t=in:st=0:d=0.08,afade=t=out:st={d-0.2}:d=0.2"
            run(["ffmpeg", "-y", "-i", find_clip(src, val), "-t", str(d), "-vf", vf, "-af", af,
                 "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", seg])
        else:
            big = kind == "title"
            # tiếng trầm "boom" cho tựa phim, nền yên lặng cho thẻ chữ
            boom = (f"aevalsrc='0.6*sin(2*PI*(42-18*t)*t)*exp(-2.2*t)|0.6*sin(2*PI*(42-18*t)*t)*exp(-2.2*t)':s=48000:d={d}"
                    if big else f"anullsrc=r=48000:cl=stereo,atrim=0:{d}")
            run(["ffmpeg", "-y", "-f", "lavfi", "-i", f"color=c=black:s={W}x{H}:r={FPS}:d={d}",
                 "-f", "lavfi", "-i", boom, "-vf", text_filter(val, big, d) + ",format=yuv420p",
                 "-shortest", "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-c:a", "aac", "-b:a", "192k",
                 "-ar", "48000", "-ac", "2", seg])
        segs.append(seg)
    lst = os.path.join(tmp, "list.txt")
    with open(lst, "w") as f:
        f.writelines(f"file '{s}'\n" for s in segs)
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", "-movflags", "+faststart", out])
    print("Xong:", out)

if __name__ == "__main__":
    main()
