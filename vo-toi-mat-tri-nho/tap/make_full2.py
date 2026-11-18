#!/usr/bin/env python3
"""Bản dựng v2: thứ tự mới có 7 cảnh chèn, thẻ tên phần, sửa bản V3 (P1–P3).
Dùng (mỗi bước chạy lại được, tự bỏ qua phần đã làm; chạy từng đợt ≤165s):
  python3 tap/make_full2.py plan    # in thứ tự dựng + clip thiếu
  python3 tap/make_full2.py seg     # chuẩn hoá clip (clip nào trong clips/full_p04_p25 mới hơn bản tạm thì làm lại)
  python3 tap/make_full2.py cards   # thẻ tên phim + tên từng phần
  python3 tap/make_full2.py trim    # áp cắt riêng (CUT_END) + sửa V3 → ~/tapfull_tmp/v2/*.mov
  python3 tap/make_full2.py parts   # tap/phan_v2/Pxx_<tên>.mp4
  python3 tap/make_full2.py full    # tap/Vo_toi_mat_tri_nho_FULL_v2.mp4"""
import os, sys, re, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_full as MF
TMP = MF.TMP; V2 = os.path.join(TMP, "v2"); HERE = MF.HERE; ROOT = MF.ROOT
OUT = os.path.join(HERE, "Vo_toi_mat_tri_nho_FULL_v2.mp4"); PH = os.path.join(HERE, "phan_v2")
FONT = "/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf"
DROP = {"P06-C4"}                       # gộp vào 06-5 (Hưng giao việc trong xe, có câu "Lần này, phải có ảnh")
MOVE = {"P08-C5": (9, 0)}               # Quân tập cười → mở đầu Phần 9 (trước buổi hẹn), không chen sau câu treo P08
AFTER = {}                              # 21-5 (Hưng sụp đổ) để cuối Phần 21 vì Hưng bị bảo vệ đưa ra ở 21-3
CUT_END = {"P21-C4": 10.95}             # bỏ cảnh toàn cuối có chân máy quay (bản cũ). Nếu render lại 21-4 thì xoá dòng này
CUT_START = {"P14-C2": 3.5}   # bỏ đoạn đầu có lớp chữ/khung máy quay (bản R/R2 ngày 18/11)
KEEP = {"P25-C5": [(0.0, 5.5), (9.5, 13.2)],    # bản cũ: bỏ đoạn có chân máy
        "P05-C4": [(1.3, 9.7), (12.0, 99)],     # bản R: bỏ khung máy quay 0–1.3s + câu "rất coi trọng gia đình" bị lặp
        "P07-C1": [(0.0, 8.4), (12.0, 99)],     # bản R: bỏ đoạn thoại lặp lộn xộn 8.4–12s
        "P22-C1": [(3.0, 11.85)]}               # bản R2: bỏ khung máy quay 0–3s + câu lặp cuối   # bản cũ: bỏ đoạn Tuấn cười có chân máy (5.5–9.5) và cuối có chân máy (13.2–15)
V3_CUT = (2.833, 3.042)                 # khung đen
V3_DELOGO = (159.15, 160.45, "delogo=x=70:y=585:w=240:h=80")   # chữ "Quan" lọt vào hình
def titles(): return MF.titles()
def avail(): return {os.path.basename(c)[:-4] for c in MF.clips()}
def order():
    byp = {}
    for c in sorted(avail() - DROP):
        byp.setdefault(MOVE.get(c, (int(c[1:3]), None))[0], []).append(c)
    for p, cs in byp.items():
        for c, (pp, pos) in MOVE.items():
            if pp == p and c in cs: cs.remove(c); cs.insert(pos, c)
        for c, a in AFTER.items():
            if c in cs and a in cs: cs.remove(c); cs.insert(cs.index(a) + 1, c)
    return dict(sorted(byp.items()))
def plan():
    t = titles()
    print("P01–P03: bản V3 (bỏ khung đen 2.83–3.04s, xoá chữ 'Quan' ~159.5s)")
    for p, cs in order().items(): print(f"Phần {p:2d} · {t.get(p,'')}: {' '.join(c[4:] if c[1:3]==f'{p:02d}' else c for c in cs)}")
    print("Thiếu:", ", ".join(sorted({"P12-C2","P06-C5","P08-C5","P10-C5","P15-C4","P19-C4","P21-C5","P23-C5"} - avail())) or "không")
def run(c): MF.run(c)
def stale(dst, src): return os.path.exists(dst) and os.path.exists(src) and os.path.getmtime(dst) < os.path.getmtime(src)
def seg2():
    for c in MF.clips():
        t = os.path.join(TMP, os.path.basename(c)[:-4] + ".mov")
        if stale(t, c): os.remove(t); print("clip mới:", os.path.basename(c), flush=True)
    MF.seg()
def card(name, lines, d=2.6):
    dst = os.path.join(V2, name + ".mov")
    if os.path.exists(dst): return dst
    from PIL import Image, ImageDraw, ImageFont
    im = Image.new("RGB", (1280, 720), (8, 8, 10)); dr = ImageDraw.Draw(im)
    y = 360 - sum(s for _, s in lines) * 0.75
    for txt, size in lines:
        f = ImageFont.truetype(FONT, size)
        try: f.set_variation_by_name("SemiBold" if size > 40 else "Regular")
        except Exception: pass
        w = dr.textlength(txt, font=f); dr.text(((1280 - w) / 2, y), txt, font=f, fill=(236, 226, 205) if size > 40 else (190, 182, 168))
        y += size * 1.5
    png = dst[:-4] + ".png"; im.save(png)
    run(["ffmpeg","-y","-loop","1","-t",str(d),"-i",png,"-f","lavfi","-t",str(d),"-i",f"anullsrc=r={MF.SR}:cl=stereo",
         "-vf",f"fps={MF.FPS},format=yuv420p,fade=t=in:st=0:d=0.5,fade=t=out:st={d-0.5}:d=0.5","-c:v","libx264","-preset","medium","-crf","17",
         "-c:a","pcm_s16le","-shortest",dst[:-4] + ".part.mov"])
    os.replace(dst[:-4] + ".part.mov", dst); return dst
def cards():
    os.makedirs(V2, exist_ok=True); t = titles()
    card("T00", [("VỢ TÔI MẤT TRÍ NHỚ", 64), ("CÓ CHỌN LỌC", 64), ("", 20)], 3.2)
    for p in order(): card(f"T{p:02d}", [(f"Phần {p}", 30), (t.get(p, ""), 54)]); print("card", p, flush=True)
def trim():
    os.makedirs(V2, exist_ok=True)
    for p, cs in order().items():
        for c in cs:
            src = os.path.join(TMP, c + ".mov"); dst = os.path.join(V2, c + ".mov")
            if stale(dst, src): os.remove(dst)
            if os.path.exists(dst) or not os.path.exists(src): continue
            if c in KEEP:
                segs = KEEP[c]; n = len(segs)
                fc = "".join(f"[0:v]trim={a}:{b},setpts=PTS-STARTPTS[v{i}];[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.05,afade=t=out:st={b-a-0.08:.2f}:d=0.08[a{i}];" for i,(a,b) in enumerate(segs))
                fc += "".join(f"[v{i}][a{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=1[v][a]"
                run(["ffmpeg","-y","-i",src,"-filter_complex",fc,"-map","[v]","-map","[a]","-c:v","libx264","-preset","medium","-crf","17","-c:a","pcm_s16le",dst[:-4]+".part.mov"])
                os.replace(dst[:-4]+".part.mov", dst); print("ghép đoạn", c, segs, flush=True)
            elif c in CUT_END or c in CUT_START:
                st = CUT_START.get(c, 0.0); end = CUT_END.get(c, MF.dur(src))
                run(["ffmpeg","-y","-ss",f"{st:.3f}","-i",src,"-t",f"{end-st:.3f}","-af",f"afade=t=in:st=0:d=0.15,afade=t=out:st={end-st-0.25:.3f}:d=0.25","-c:v","libx264","-preset","medium","-crf","17","-c:a","pcm_s16le",dst[:-4]+".part.mov"])
                os.replace(dst[:-4]+".part.mov", dst); print("cắt", c, f"{st}–{end:.2f}s", flush=True)
            else: run(["cp", src, dst])
    v = os.path.join(V2, "P00-V3.mov")
    if not os.path.exists(v):
        a, b = V3_CUT; s0, s1, flt = V3_DELOGO; sh = b - a
        fc = (f"[0:v]trim=0:{a},setpts=PTS-STARTPTS[v1];[0:v]trim={b},setpts=PTS-STARTPTS[v2];[v1][v2]concat=n=2:v=1:a=0,{flt}:enable='between(t,{s0-sh:.2f},{s1-sh:.2f})'[v];"
              f"[0:a]atrim=0:{a},asetpts=PTS-STARTPTS[a1];[0:a]atrim={b},asetpts=PTS-STARTPTS[a2];[a1][a2]concat=n=2:v=0:a=1[a]")
        run(["ffmpeg","-y","-i",os.path.join(TMP,"P00-V3.mov"),"-filter_complex",fc,"-map","[v]","-map","[a]","-c:v","libx264","-preset","medium","-crf","17","-c:a","pcm_s16le",v[:-4]+".part.mov"])
        os.replace(v[:-4]+".part.mov", v); print("V3 đã sửa", flush=True)
def segs_of(p, cs): return [os.path.join(V2, f"T{p:02d}.mov")] + [os.path.join(V2, c + ".mov") for c in cs]
def parts():
    os.makedirs(PH, exist_ok=True); t = titles()
    for p, cs in order().items():
        out = os.path.join(PH, f"P{p:02d}_{MF.safe(t.get(p,''))}.mp4")
        tmp = os.path.join(V2, f"part{p:02d}.mp4"); print("part", p, f"{MF.concat(segs_of(p, cs), tmp):.1f}s", flush=True); run(["cp", tmp, out])
def full():
    segs = [os.path.join(V2, "T00.mov"), os.path.join(V2, "P00-V3.mov")]
    for p, cs in order().items(): segs += segs_of(p, cs)
    miss = [s for s in segs if not os.path.exists(s)]
    if miss: sys.exit("Thiếu: " + ", ".join(os.path.basename(m) for m in miss))
    d = MF.concat(segs, os.path.join(V2, "full.mp4")); run(["cp", os.path.join(V2, "full.mp4"), OUT]); print("Xong", OUT, f"{d/60:.1f} phút")
if __name__ == "__main__":
    {"plan": plan, "seg": seg2, "cards": cards, "trim": trim, "parts": parts, "full": full}[sys.argv[1]]()
