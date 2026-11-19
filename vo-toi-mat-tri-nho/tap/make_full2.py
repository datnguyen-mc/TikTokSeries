#!/usr/bin/env python3
"""Bản dựng v2: thứ tự mới có 7 cảnh chèn, thẻ tên phần, cắt đuôi lặng, sửa bản V3 (P1–P3).
Dùng (mỗi bước chạy lại được, tự bỏ qua phần đã làm; chạy từng đợt ≤165s):
  python3 tap/make_full2.py plan    # in thứ tự dựng + clip thiếu
  python3 tap/make_full2.py seg     # chuẩn hoá clip mới/đã thay (dùng lại make_full.seg)
  python3 tap/make_full2.py cards   # tạo thẻ tên phần
  python3 tap/make_full2.py trim    # cắt đuôi lặng + sửa V3 → ~/tapfull_tmp/v2/*.mov
  python3 tap/make_full2.py parts   # tap/phan_v2/Pxx_<tên>.mp4
  python3 tap/make_full2.py full    # tap/Vo_toi_mat_tri_nho_FULL_v2.mp4
Khi thay clip trong clips/full_p04_p25: xoá ~/tapfull_tmp/<Pxx-Cy>.mov và ~/tapfull_tmp/v2/<Pxx-Cy>.mov rồi chạy lại seg→trim."""
import os, sys, json, re, subprocess, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_full as MF
TMP = MF.TMP; V2 = os.path.join(TMP, "v2"); HERE = MF.HERE; ROOT = MF.ROOT
OUT = os.path.join(HERE, "Vo_toi_mat_tri_nho_FULL_v2.mp4"); PH = os.path.join(HERE, "phan_v2")
FONT = "/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf"
DROP = {"P06-C4"}                       # gộp vào 06-5 (Hưng giao việc trong xe)
MOVE = {"P08-C5": (9, 0)}               # Quân tập cười → mở đầu Phần 9 (trước buổi hẹn)
AFTER = {}                              # 21-5 (Hưng sụp đổ) để cuối Phần 21: Hưng bị bảo vệ đưa ra ở 21-3
CUT_END = {"P21-C4": 10.95}             # bỏ cảnh toàn cuối có chân máy quay (bản render 18/11; nếu render lại 21-4 thì xoá dòng này)
TRIM_TAILS = False   # thử 18/11: cắt theo âm lượng làm mất nhịp hình (07-2, 08-4, 09-2, 20-4) → tắt
NOTRIM = {"P04-C4","P09-C4","P17-C4","P21-C5","P25-C1","P25-C5"}
V3_CUT = (2.833, 3.042)                 # khung đen
V3_DELOGO = "delogo=x=70:y=585:w=240:h=80:enable='between(t,159.15,160.45)'"  # chữ "Quan"
def titles(): return MF.titles()
def avail(): return {os.path.basename(c)[:-4] for c in MF.clips()}
def order():
    have = sorted(avail() - DROP); byp = {}
    for c in have:
        p = MOVE.get(c, (int(c[1:3]), None))[0]; byp.setdefault(p, []).append(c)
    for p, cs in byp.items():
        for c, (pp, pos) in MOVE.items():
            if pp == p and c in cs: cs.remove(c); cs.insert(pos, c)
        for c, a in AFTER.items():
            if c in cs and a in cs: cs.remove(c); cs.insert(cs.index(a) + 1, c)
    return dict(sorted(byp.items()))
def plan():
    t = titles(); o = order()
    print("P01–P03: bản V3 (bỏ khung đen 2.83–3.04s, xoá chữ 'Quan' 159.2–160.4s)")
    for p, cs in o.items(): print(f"Phần {p:2d} · {t.get(p,'')}: {' '.join(c[4:] for c in cs)}")
    print("Thiếu clip:", ", ".join(sorted({"P12-C2"} - avail())) or "không")
def run(c): MF.run(c)
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
def last_sound(src):
    """Thời điểm hết tiếng nói (năng lượng > đỉnh-18dB, cửa sổ 0.1s)."""
    import numpy as np
    raw = subprocess.run(["ffmpeg","-v","error","-i",src,"-ac","1","-ar","8000","-f","s16le","-"],capture_output=True).stdout
    a = np.frombuffer(raw, np.int16).astype(float) / 32768; w = 800
    db = 20 * np.log10(np.array([np.sqrt((a[i:i+w]**2).mean() + 1e-12) for i in range(0, len(a) - w, w)]))
    act = np.where(db > np.percentile(db, 95) - 18)[0]; d = MF.dur(src)
    return ((act[-1] + 1) * 0.1 if len(act) else d), d
def stale(dst, src): return os.path.exists(dst) and os.path.exists(src) and os.path.getmtime(dst) < os.path.getmtime(src)
def seg2():
    for c in MF.clips():
        t = os.path.join(TMP, os.path.basename(c)[:-4] + ".mov")
        if stale(t, c): os.remove(t); print("clip mới:", os.path.basename(c), flush=True)
    MF.seg()
def trim():
    os.makedirs(V2, exist_ok=True); log = {}
    for p, cs in order().items():
        for i, c in enumerate(cs):
            src = os.path.join(TMP, c + ".mov"); dst = os.path.join(V2, c + ".mov")
            if stale(dst, src): os.remove(dst)
            if os.path.exists(dst) or not os.path.exists(src): continue
            s, d = last_sound(src); end = d
            if TRIM_TAILS and c not in NOTRIM:
                keep, cap = (2.0, 5.0) if i < len(cs) - 1 else (4.0, 4.0)   # clip cuối phần giữ nhịp treo lâu hơn
                if d - s > keep + 0.5: end = max(s + keep, d - cap)
            if c in CUT_END: end = min(end, CUT_END[c])
            log[c] = round(d - end, 2)
            if end >= d - 0.05: run(["cp", src, dst])
            else:
                run(["ffmpeg","-y","-i",src,"-t",f"{end:.3f}","-af",f"afade=t=out:st={end-0.25:.3f}:d=0.25","-c:v","libx264","-preset","medium","-crf","17","-c:a","pcm_s16le",dst[:-4]+".part.mov"])
                os.replace(dst[:-4]+".part.mov", dst)
            print("trim", c, f"-{d-end:.1f}s", flush=True)
    v = os.path.join(V2, "P00-V3.mov")
    if not os.path.exists(v):
        a, b = V3_CUT
        fc = (f"[0:v]trim=0:{a},setpts=PTS-STARTPTS[v1];[0:v]trim={b},setpts=PTS-STARTPTS[v2];[v1][v2]concat=n=2:v=1:a=0,{V3_DELOGO.replace('159.15',str(159.15-(b-a))).replace('160.45',str(160.45-(b-a)))}[v];"
              f"[0:a]atrim=0:{a},asetpts=PTS-STARTPTS[a1];[0:a]atrim={b},asetpts=PTS-STARTPTS[a2];[a1][a2]concat=n=2:v=0:a=1[a]")
        run(["ffmpeg","-y","-i",os.path.join(TMP,"P00-V3.mov"),"-filter_complex",fc,"-map","[v]","-map","[a]","-c:v","libx264","-preset","medium","-crf","17","-c:a","pcm_s16le",v[:-4]+".part.mov"])
        os.replace(v[:-4]+".part.mov", v); print("V3 fixed", flush=True)
def segs_of(p, cs): return [os.path.join(V2, f"T{p:02d}.mov")] + [os.path.join(V2, c + ".mov") for c in cs]
def parts():
    os.makedirs(PH, exist_ok=True); t = titles()
    for p, cs in order().items():
        out = os.path.join(PH, f"P{p:02d}_{MF.safe(t.get(p,''))}.mp4")
        if os.path.exists(out): continue
        tmp = os.path.join(V2, f"part{p:02d}.mp4"); print("part", p, f"{MF.concat(segs_of(p, cs), tmp):.1f}s", flush=True); run(["cp", tmp, out])
def full():
    segs = [os.path.join(V2, "T00.mov"), os.path.join(V2, "P00-V3.mov")]
    for p, cs in order().items(): segs += segs_of(p, cs)
    miss = [s for s in segs if not os.path.exists(s)]
    if miss: sys.exit("Thiếu: " + ", ".join(os.path.basename(m) for m in miss))
    d = MF.concat(segs, os.path.join(V2, "full.mp4")); run(["cp", os.path.join(V2, "full.mp4"), OUT]); print("Xong", OUT, f"{d/60:.1f} phút")
if __name__ == "__main__":
    {"plan": plan, "seg": seg2, "cards": cards, "trim": trim, "parts": parts, "full": full}[sys.argv[1]]()
