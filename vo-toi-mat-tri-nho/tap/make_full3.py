#!/usr/bin/env python3
"""Dựng phim đầy đủ bản 3 (19/11): P1–P3 (bản V3) + P04–P25 (clips/full_p04_p25/Pxx-Cy.mp4).
Khác bản 2: cắt viền đen/khung bo góc theo từng shot, xoá dấu ✦ (delogo), cắt câu thoại lỗi theo KEEP.
Dùng:  python3 tap/make_full3.py plan | cards | seg [giây tối đa] | parts | full
Dữ liệu sửa hình: tap/fix_v3.json (shot, viền đen, hộp delogo cho từng clip — sinh từ bước QC).
Đoạn chuẩn hoá nằm ở ~/b3 (1280x720, 24fps, PCM 48k)."""
import glob, os, subprocess, sys, json, re, time
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
TMP = os.path.join(os.path.expanduser("~"), "b3"); CL = os.path.join(ROOT, "clips", "full_p04_p25")
V3SRC = os.path.join(HERE, "Vo_toi_mat_tri_nho_V3_3phut.mp4")   # bản V3 3 phút (dựng lại: make_v3.py seg + join)
OUT = os.path.join(ROOT, "phim", "full", "Vo_toi_mat_tri_nho_FULL.mp4"); PH = os.path.join(HERE, "phan_v3")
FONT = "/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf"
W, H, FPS, SR = 1280, 720, 24, 48000
GRADE = "eq=contrast=1.03:saturation=0.97"
LN = "loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000,aformat=channel_layouts=stereo"
FIX = json.load(open(os.path.join(HERE, "fix_v3.json")))
DROP = {"P06-C4"}                       # gộp vào 06-5
MOVE = {"P08-C5": (9, 0)}               # Quân tập cười → mở đầu Phần 9
# Đoạn giữ lại của clip nguồn (giây), theo thứ tự phát. Không khai báo = giữ cả clip.
KEEP = {
 "V3":     [(0, 2.833), (3.042, 17.167), (20.167, 40.333), (42.333, 64.54), (67.58, 999)],   # 20/11: 02-04 render lại (hết vấp), 01-01/03-03/03-05/03-08/03-09 render lại; bỏ shot 01-06 (Tuấn cầm nắm hồng nhỏ, lệch bó 99 bông)
             # bỏ khung đen; 01-12: bỏ 2s đầu (bàn trống, bản cũ trước khi có bó hoa);
             # 01-11/14/16/17 render lại 19/11 với bó hồng trên bàn (01-17 giữ cả shot);
             # bỏ shot 02-01 (váy trắng Mai Anh dính vết đỏ vô lý)
 "P05-C4": [(1.3, 9.6), (12.0, 999)],             # khung ngắm máy quay 0–1.3; lặp "rất coi trọng gia đình"
 "P07-C1": [(0, 8.1), (12.0, 999)],               # câu lặp méo tiếng 8.3–10.3
 "P08-C1": [(0, 3.5), (7.7, 999)],                 # bản R4 (19/11): Linh nói câu "ly hôn" hai lần — giữ lần nói trong cận Linh (19/11 tối: bỏ hẳn mẩu "…ly hôn" sót lại)
 "P08-C4": [(0, 12.1)],                            # 20/11: bỏ cú biến bàn làm việc thành mặt hồ
 "P09-C4": [(4.958, 999)],                         # bản R (19/11): bỏ shot đầu có khung ngắm + chữ "24 fps"
 "P10-C4": [(0, 13.2)],                           # bỏ cú lia về phòng trống
 "P14-C1": [(0, 8.05), (10.0, 999)],              # câu lạc "còn thư cho vợ"
 "P14-C3": [(0, 9.25), (10.8, 999)],              # 20/11: Linh đọc "Bé yêu của anh" hai lần
 "P17-C4": [(0, 11.0)],                           # đèn chiếu lọt khung
 "P18-C3": [(0, 13.45)],                          # bỏ cú lia sang rèm cửa
 "P19-C2": [(0, 10.3), (12.05, 999)],             # 20/11: Bống nói "Con hứa với mẹ rồi" hai lần
 "P19-C3": [(0, 11.96)],                           # 20/11: bỏ shot Linh mặc vest buổi sáng (ngược thời gian)
 "P20-C1": [(0, 5.9), (11.0, 13.6), (5.9, 8.2)],  # "Vợ mất trí." → ảnh trên màn chiếu → "Quỹ Hoa Anh Đào sẽ rút vốn."; bỏ câu lặp
 "P21-C4": [(0, 10.95)],                          # chân máy quay
 "P22-C1": [(3.0, 999)],                           # bản R3 (19/11): shot đầu có giao diện máy quay
 "P25-C5": [(0, 5.5)],                            # phần sau thay bằng 25-6
}
NOCROP = {"P20-C1"}
HFLIP = {"P09-C2", "P13-C3"}   # P13-C3 (20/11): trong xe hai người bị đổi chỗ so với 13-2;                      # bản R (19/11) quay ngược trục: lật ngang cho khớp 09-1/09-3                     # góc tối là nội dung cảnh (màn chiếu)
def run(c):
    r = subprocess.run(c, capture_output=True, text=True)
    if r.returncode: sys.exit("ffmpeg lỗi:\n" + " ".join(c)[-1800:] + "\n" + r.stderr[-1500:])
def dur(p): return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p],capture_output=True,text=True).stdout)
def titles():
    m = json.load(open(os.path.join(ROOT, "flow_15s", "manifest.json"))); return {x["part"]: x["title"] for x in m}
def avail(): return {os.path.basename(c)[:-4] for c in glob.glob(os.path.join(CL, "P[0-9][0-9]-C[0-9].mp4"))}
def order():
    byp = {}
    for c in sorted(avail() - DROP): byp.setdefault(MOVE.get(c, (int(c[1:3]), None))[0], []).append(c)
    for p, cs in byp.items():
        for c, (pp, pos) in MOVE.items():
            if pp == p and c in cs: cs.remove(c); cs.insert(pos, c)
    return dict(sorted(byp.items()))
def plan():
    t = titles()
    print("P01–P03: bản V3"); [print(f"Phần {p:2d} · {t.get(p,'')}: {' '.join(c[4:] for c in cs)}") for p, cs in order().items()]
# ---------- sửa hình theo shot ----------
def keep_frames(name):
    fx = FIX[name]; n = fx["n"]; cuts = {a for a, b in fx["shots"]} | {n}; out = []
    for a, b in KEEP.get(name, [(0, 999)]):
        fa, fb = round(a * FPS), min(n, round(b * FPS))
        for c in cuts:                      # bám vào điểm cắt cảnh nếu lệch ≤ 3 khung
            if abs(fa - c) <= 3: fa = c
            if abs(fb - c) <= 3: fb = c
        out.append((fa, fb))
    return out
def crop_of(name, a, b):
    if name in NOCROP: return None
    for fa, fb, w, h, x, y in FIX[name].get("mcrop", []):     # cắt tay (vd. đẩy chữ "Quan" ra ngoài khung)
        if fa < b and fb > a: return (w, h, x, y)
    t = bo = l = r = k = 0
    for fa, fb, T, B, L, Rr, K in FIX[name]["bord"]:
        if fa < b and fb > a and min(fb, b) - max(fa, a) >= 2: t, bo, l, r, k = max(t, T), max(bo, B), max(l, L), max(r, Rr), max(k, K)
    if not (t or bo or l or r or k): return None
    if (l > 6 or r > 6) and k < 8: k = 8                     # khung bo góc: lấn thêm để hết góc đen
    m = 2; x0, y0, x1, y1 = l + k + m, t + k + m, W - r - k - m, H - bo - k - m; w, h = x1 - x0, y1 - y0
    if w * 9 > h * 16: w2 = h * 16 // 9; x0 += (w - w2) // 2; w = w2
    else: h2 = w * 9 // 16; y0 += (h - h2) // 2; h = h2
    w -= w % 2; h -= h % 2
    return None if W - w < 6 else (w, h, x0, y0)
def pieces(name):
    out = []
    for ka, kb in keep_frames(name):
        b = sorted({ka, kb} | {x for s in FIX[name]["shots"] for x in s if ka < x < kb})
        for a, e in zip(b, b[1:]):
            c = crop_of(name, a, e)
            if out and out[-1][1] == a and out[-1][2] == c: out[-1][1] = e
            else: out.append([a, e, c])
    return out
def build(name, src, dst, grade):
    fx = FIX[name]; pcs = pieces(name); kf = keep_frames(name)
    pre = [f"fps={FPS}", f"scale={W}:{H}"] + (["hflip"] if name in HFLIP else [])
    for fa, fb, x, y, w, h in fx["delogo"]:
        x, y = max(1, x), max(1, y); w, h = min(w, W - 1 - x), min(h, H - 1 - y)
        pre.append(f"delogo=x={x}:y={y}:w={w}:h={h}:enable='between(n,{fa},{fb-1})'")
    g = [f"[0:v]{','.join(pre)},split={len(pcs)}" + "".join(f"[s{i}]" for i in range(len(pcs)))]
    for i, (a, e, c) in enumerate(pcs):
        f = f"[s{i}]trim=start_frame={a}:end_frame={e},setpts=PTS-STARTPTS"
        if c: f += f",crop={c[0]}:{c[1]}:{c[2]}:{c[3]},scale={W}:{H}:flags=lanczos"
        g.append(f + f",setsar=1[p{i}]")
    g.append("".join(f"[p{i}]" for i in range(len(pcs))) + f"concat=n={len(pcs)}:v=1:a=0," + (GRADE + "," if grade else "") + "format=yuv420p[v]")
    g.append(f"[0:a]aresample={SR},asplit={len(kf)}" + "".join(f"[t{i}]" for i in range(len(kf))))
    for i, (a, e) in enumerate(kf):
        d = (e - a) / FPS
        g.append(f"[t{i}]atrim=start={a/FPS:.4f}:end={e/FPS:.4f},asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.03,afade=t=out:st={d-0.05:.3f}:d=0.05[u{i}]")
    g.append("".join(f"[u{i}]" for i in range(len(kf))) + f"concat=n={len(kf)}:v=0:a=1[a]")
    part = dst[:-4] + ".part.mov"
    run(["ffmpeg","-y","-i",src,"-filter_complex",";".join(g),"-map","[v]","-map","[a]","-c:v","libx264","-preset","medium","-crf","16",
         "-c:a","pcm_s16le","-ar",str(SR),"-ac","2","-shortest",part])
    os.replace(part, dst)
def sig(name): return json.dumps([pieces(name), FIX[name]["delogo"], name in HFLIP])
def seg(limit=150):
    os.makedirs(TMP, exist_ok=True); t0 = time.time(); todo = 0
    jobs = [("V3", V3SRC, False)] + [(c, os.path.join(CL, c + ".mp4"), True) for cs in order().values() for c in cs]
    for name, src, grade in jobs:
        if not os.path.exists(src): print("THIẾU nguồn", src); todo += 1; continue
        dst = os.path.join(TMP, name + ".mov"); sg = dst + ".sig"
        if os.path.exists(dst) and os.path.getmtime(dst) > os.path.getmtime(src) and os.path.exists(sg) and open(sg).read() == sig(name): continue
        if time.time() - t0 > limit: todo += 1; continue
        build(name, src, dst, grade); open(sg, "w").write(sig(name)); print("seg", name, f"{dur(dst):.2f}s", len(pieces(name)), "đoạn", flush=True)
    print("CÒN", todo, "clip" if todo else "— xong seg", flush=True)
def card(name, lines, d=2.6):
    dst = os.path.join(TMP, name + ".mov")
    if os.path.exists(dst): return dst
    from PIL import Image, ImageDraw, ImageFont
    im = Image.new("RGB", (W, H), (8, 8, 10)); dr = ImageDraw.Draw(im); y = 360 - sum(s for _, s in lines) * 0.75
    for txt, size in lines:
        f = ImageFont.truetype(FONT, size)
        try: f.set_variation_by_name("SemiBold" if size > 40 else "Regular")
        except Exception: pass
        w = dr.textlength(txt, font=f); dr.text(((W - w) / 2, y), txt, font=f, fill=(236, 226, 205) if size > 40 else (190, 182, 168)); y += size * 1.5
    png = dst[:-4] + ".png"; im.save(png)
    run(["ffmpeg","-y","-loop","1","-t",str(d),"-i",png,"-f","lavfi","-t",str(d),"-i",f"anullsrc=r={SR}:cl=stereo",
         "-vf",f"fps={FPS},format=yuv420p,fade=t=in:st=0:d=0.5,fade=t=out:st={d-0.5}:d=0.5","-c:v","libx264","-preset","medium","-crf","17","-c:a","pcm_s16le","-shortest",dst[:-4] + ".part.mov"])
    os.replace(dst[:-4] + ".part.mov", dst); return dst
def cards():
    os.makedirs(TMP, exist_ok=True); t = titles()
    card("T00", [("VỢ TÔI MẤT TRÍ NHỚ", 64), ("CÓ CHỌN LỌC", 64), ("", 20)], 3.2)
    for p in order(): card(f"T{p:02d}", [(f"Phần {p}", 30), (t.get(p, ""), 54)])
    card("T99", [("HẾT", 64), ("", 20), ("Vợ Tôi Mất Trí Nhớ Có Chọn Lọc · Hidden Cinema", 28)], 4.0)
    print("xong thẻ tên", flush=True)
def concat(segs, out, norm=True):
    miss = [s for s in segs if not os.path.exists(s)]
    if miss: sys.exit("Thiếu đoạn: " + ", ".join(os.path.basename(m) for m in miss))
    lst = out + ".txt"; open(lst, "w").writelines(f"file '{s}'\n" for s in segs); base = out + ".base.mov"
    run(["ffmpeg","-y","-f","concat","-safe","0","-i",lst,"-c","copy",base])
    run(["ffmpeg","-y","-i",base,"-af",LN,"-c:v","copy","-c:a","aac","-b:a","192k","-movflags","+faststart",out]); os.remove(base); return dur(out)
def safe(s): return re.sub(r"[^\w\-]+", "_", s, flags=re.U).strip("_")
def parts(limit=150):
    os.makedirs(PH, exist_ok=True); t = titles(); t0 = time.time()
    jobs = [(0, "P01-03_Mo_dau", [os.path.join(TMP, "T00.mov"), os.path.join(TMP, "V3.mov")])]
    jobs += [(p, f"P{p:02d}_{safe(t.get(p,''))}", [os.path.join(TMP, f"T{p:02d}.mov")] + [os.path.join(TMP, c + ".mov") for c in cs]) for p, cs in order().items()]
    for p, nm, segs in jobs:
        out = os.path.join(PH, nm + ".mp4")
        if os.path.exists(out) and all(os.path.getmtime(out) > os.path.getmtime(s) for s in segs): continue
        if time.time() - t0 > limit: print("CÒN phần", p, flush=True); continue
        tmp = os.path.join(TMP, f"part{p:02d}.mp4"); d = concat(segs, tmp); run(["cp", tmp, out]); os.remove(tmp); print("part", p, f"{d:.1f}s", flush=True)
def full_list():
    segs = [os.path.join(TMP, "T00.mov"), os.path.join(TMP, "V3.mov")]
    for p, cs in order().items(): segs += [os.path.join(TMP, f"T{p:02d}.mov")] + [os.path.join(TMP, c + ".mov") for c in cs]
    return segs + [os.path.join(TMP, "T99.mov")]
def full():
    """2 bước để mỗi lần chạy < 3 phút: full (ghép copy) → full2 (chuẩn âm lượng + AAC)."""
    segs = full_list(); miss = [s for s in segs if not os.path.exists(s)]
    if miss: sys.exit("Thiếu đoạn: " + ", ".join(os.path.basename(m) for m in miss))
    lst = os.path.join(TMP, "full.txt"); open(lst, "w").writelines(f"file '{s}'\n" for s in segs)
    run(["ffmpeg","-y","-f","concat","-safe","0","-i",lst,"-c","copy",os.path.join(TMP, "full.base.mov")]); print("base", f"{dur(os.path.join(TMP,'full.base.mov'))/60:.2f} phút", flush=True)
# 20/11: âm lượng bản full chuẩn YouTube — nén nhẹ dải động rồi loudnorm 2 lượt (đo → áp tuyến tính) về −14 LUFS.
PRE = "acompressor=threshold=-30dB:ratio=3:attack=10:release=250:makeup=4,alimiter=limit=0.32:level=false"
LNT = "I=-14:TP=-2:LRA=16"
def full2m():
    r = subprocess.run(["ffmpeg","-hide_banner","-nostats","-i",os.path.join(TMP, "full.base.mov"),"-vn","-af",f"{PRE},loudnorm={LNT}:print_format=json","-f","null","-"],capture_output=True,text=True)
    js = r.stderr[r.stderr.rindex("{"):r.stderr.rindex("}")+1]; open(os.path.join(TMP, "full.loud.json"),"w").write(js); print("đo:", js.replace("\n"," "), flush=True)
def full2():
    tmp = os.path.join(TMP, "full.mp4"); m = json.load(open(os.path.join(TMP, "full.loud.json")))
    af = (f"{PRE},loudnorm={LNT}:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}"
          f":measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true,aresample=48000,aformat=channel_layouts=stereo")
    run(["ffmpeg","-y","-i",os.path.join(TMP, "full.base.mov"),"-af",af,"-c:v","copy","-c:a","aac","-b:a","192k","-movflags","+faststart",tmp])
    os.makedirs(os.path.dirname(OUT), exist_ok=True); run(["cp", tmp, OUT]); print("Xong:", OUT, f"{dur(OUT)/60:.2f} phút", flush=True)
if __name__ == "__main__":
    a = sys.argv[1] if len(sys.argv) > 1 else "plan"
    if a in ("seg", "parts") and len(sys.argv) > 2: {"seg": seg, "parts": parts}[a](float(sys.argv[2]))
    else: {"plan": plan, "seg": seg, "cards": cards, "parts": parts, "full": full, "full2m": full2m, "full2": full2}[a]()
