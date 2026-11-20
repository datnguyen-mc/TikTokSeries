#!/usr/bin/env python3
"""Dựng 10 Shorts dọc 9:16 (1080x1920) từ các đoạn đã chuẩn hoá trong ~/b3 (make_full3.py seg).
Dùng: python3 build_shorts.py [id ...]   (không truyền id = dựng tất cả). Đọc spec.json cùng thư mục."""
import json, os, subprocess, sys, unicodedata
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
B3 = os.path.join(os.path.expanduser("~"), "b3"); TMP = "/tmp/shorts_tmp"; os.makedirs(TMP, exist_ok=True)
FD = os.path.join(ROOT, "trailer", "_fonts"); SEMI = os.path.join(FD, "BeVietnamPro-SemiBold.ttf"); MED = os.path.join(FD, "BeVietnamPro-Medium.ttf")
LORA = "/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf"
W, H, FPS = 1080, 1920, 24
VY = 600; VH = 608                       # khung phim 16:9 ở giữa
GOLD = (242, 193, 78); CREAM = (245, 236, 214)
N = lambda s: unicodedata.normalize("NFC", s)
def run(c):
    r = subprocess.run(c, capture_output=True, text=True)
    if r.returncode: sys.exit("ffmpeg lỗi:\n" + r.stderr[-2500:])
def font(path, size, var=None):
    f = ImageFont.truetype(path, size)
    if var:
        try: f.set_variation_by_name(var)
        except Exception: pass
    return f
def fit(dr, txt, path, size, maxw, var=None):
    while size > 30:
        f = font(path, size, var)
        if dr.textlength(txt, font=f) <= maxw: return f
        size -= 2
    return font(path, size, var)
def overlay_png(s, path):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); dr = ImageDraw.Draw(im)
    # dải tối phía trên & dưới để chữ nổi trên nền mờ
    for y in range(0, VY):
        a = int(150 * (1 - y / VY) ** 0.6); dr.line([(0, y), (W, y)], fill=(0, 0, 0, a))
    for y in range(VY + VH, H):
        a = int(170 * ((y - VY - VH) / (H - VY - VH)) ** 0.8); dr.line([(0, y), (W, y)], fill=(0, 0, 0, a))
    # tên phim
    t = N("VỢ TÔI MẤT TRÍ NHỚ CÓ CHỌN LỌC"); f = font(LORA, 40, "SemiBold")
    tw = dr.textlength(t, font=f); dr.text(((W - tw) / 2, 190), t, font=f, fill=CREAM + (235,))
    dr.line([(W / 2 - 60, 250), (W / 2 + 60, 250)], fill=GOLD + (220,), width=3)
    # câu móc
    l1, l2 = (N(x) for x in s["hook"])
    f1 = fit(dr, l1, SEMI, 66, W - 110); f2 = fit(dr, l2, SEMI, 76, W - 90)
    for txt, f, y, col in ((l1, f1, 320, (255, 255, 255)), (l2, f2, 418, GOLD)):
        w = dr.textlength(txt, font=f)
        dr.text(((W - w) / 2, y), txt, font=f, fill=col + (255,), stroke_width=5, stroke_fill=(0, 0, 0, 230))
    # nhãn phần
    tag = N(s["part"].upper()); f = font(MED, 34); w = dr.textlength(tag, font=f) + 44
    x0 = (W - w) / 2; dr.rounded_rectangle([x0, 528, x0 + w, 578], radius=25, fill=(0, 0, 0, 150), outline=GOLD + (230,), width=2)
    dr.text((x0 + 22, 534), tag, font=f, fill=GOLD + (255,))
    # chân trang
    ft = N("Xem trọn bộ 25 phần · Hidden Cinema"); f = font(MED, 32)
    w = dr.textlength(ft, font=f); dr.text(((W - w) / 2, 1500), ft, font=f, fill=(225, 220, 210, 210))
    im.save(path)
def ass(cues, path):
    head = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Sub,Be Vietnam Pro SemiBold,62,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,0,0,0,0,100,100,0,0,1,4.5,1.5,8,60,60,1248,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    def ts(t):
        cs = int(round(t * 100)); return f"{cs//360000}:{cs//6000%60:02d}:{cs//100%60:02d}.{cs%100:02d}"
    BR = "\\N"; FAD = "{\\fad(60,60)}"
    lines = ["Dialogue: 0,%s,%s,Sub,,0,0,0,,%s%s" % (ts(a), ts(b), FAD, N(t).replace(chr(10), BR)) for a, b, t in cues]
    open(path, "w", encoding="utf-8").write(head + "\n".join(lines) + "\n")
def build(s):
    segs = s["segs"]; offs = []; o = 0.0
    for name, a, b in segs: offs.append(o); o += b - a
    D = o
    cues = []
    for i, a, b, t in s["cues"]:
        name, sa, sb = segs[i]; a, b = max(a, sa), min(b, sb)
        cues.append((offs[i] + a - sa, offs[i] + b - sa, t))
    png = os.path.join(TMP, f"S{s['id']}.png"); overlay_png(s, png)
    sub = os.path.join(TMP, f"S{s['id']}.ass"); ass(cues, sub)
    ins = []; g = []
    for k, (name, a, b) in enumerate(segs):
        ins += ["-i", os.path.join(B3, name + ".mov")]
        d = b - a
        g.append(f"[{k}:v]trim=start={a:.4f}:end={b:.4f},setpts=PTS-STARTPTS,fps={FPS},scale=1280:720,setsar=1[v{k}]")
        g.append(f"[{k}:a]atrim=start={a:.4f}:end={b:.4f},asetpts=PTS-STARTPTS,aformat=sample_rates=48000:channel_layouts=stereo,afade=t=in:st=0:d=0.03,afade=t=out:st={max(0,d-0.04):.3f}:d=0.04[a{k}]")
    n = len(segs); P = n
    g.append("".join(f"[v{k}][a{k}]" for k in range(n)) + f"concat=n={n}:v=1:a=1[vc][ac]")
    g.append("[vc]split[b0][f0]")
    g.append("[b0]scale=-2:480,crop=270:480,boxblur=8:2,scale=1080:1920,eq=brightness=-0.10:saturation=0.85[bg]")
    g.append(f"[f0]scale=1080:{VH}:flags=lanczos[fg]")
    g.append(f"[bg][fg]overlay=0:{VY}[m1]")
    g.append(f"[m1][{P}:v]overlay=0:0[m2]")
    subp = sub.replace(":", "\\:").replace(",", "\\,")
    g.append(f"[m2]subtitles=filename={subp}:fontsdir={FD}[m3]")
    g.append(f"color=c=0xF2C14E:s=1080x8:r={FPS}[bar]")
    g.append(f"[m3][bar]overlay=x='-W+W*t/{D:.3f}':y=1912:shortest=1,format=yuv420p[vout]")
    g.append("[ac]loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[aout]")
    out = os.path.join(ROOT, "phim", "shorts", f"Short_{s['id']}_{s['slug']}.mp4")
    run(["ffmpeg", "-y"] + ins + ["-loop", "1", "-i", png, "-filter_complex", ";".join(g), "-map", "[vout]", "-map", "[aout]",
         "-t", f"{D:.3f}", "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-profile:v", "high", "-r", str(FPS),
         "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out + ".part.mp4"])
    os.replace(out + ".part.mp4", out); print("xong", os.path.basename(out), f"{D:.1f}s", flush=True)
if __name__ == "__main__":
    S = json.load(open(os.path.join(HERE, "shorts_spec.json"), encoding="utf-8"))
    want = set(sys.argv[1:])
    for s in S:
        if not want or s["id"] in want: build(s)
