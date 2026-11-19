#!/usr/bin/env python3
"""Trailer điện ảnh "Vợ tôi mất trí nhớ có chọn lọc" (bản 19/11, ~2 phút).
Nguồn: các đoạn phim đã sửa của bản dựng FULL_v3 (~/b3/*.mov, sinh bởi tap/make_full3.py seg).
Dùng: python3 trailer/v3/make_trailer3.py seg | flow | mix | all   (music = nhạc tự tổng hợp dự phòng)
Nhạc nền: tạo trên Flow Music (flowmusic.app, Lyria 3.5) — trailer/v3/nhac/take2.wav, ghép theo nhịp dựng (music_flow).
Hàm music() cũ (nhạc tự tổng hợp bằng numpy) vẫn giữ làm dự phòng."""
import os, sys, json, math, subprocess, wave
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); B3 = os.path.expanduser("~/b3"); TMP = os.path.expanduser("~/trw/seg")
OUT = os.path.join(HERE, "Trailer_Vo_toi_mat_tri_nho.mp4")
FONT = "/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf"
W, H, FPS, SR = 1280, 720, 24, 48000
GRADE = "eq=contrast=1.05:saturation=0.94:gamma=0.98,vignette=angle=0.32"
# (loại, ...) — shot: (nguồn, vào, ra, nhãn đoạn nhạc)
EDL = [
 ("black", 1.4, "cold"),
 ("shot", "V3", 0.0, 2.8, "cold"),                       # giày đỏ trên hành lang kính
 ("card", ["MƯỜI NĂM NGÀY CƯỚI"], 2.3, "cold"),
 ("shot", "V3", 9.5, 15.6, "setup"),                     # Tuấn: anh Quân họp gấp với đối tác Nhật… / Linh: Thế cơ à?
 ("shot", "V3", 41.3, 48.4, "setup"),                    # dưới cổng khách sạn / Đối tác Nhật gì mà mặc váy trắng…
 ("shot", "V3", 58.1, 61.0, "setup"),                    # Thế thì chị xuống chào đối tác Nhật một câu.
 ("shot", "V3", 97.3, 100.8, "setup"),                   # Quân: Cột nào? Khách sạn này toàn cột thôi em ạ!
 ("shot", "V3", 116.9, 118.9, "setup"),                  # Anh… là ai nhỉ?
 ("shot", "V3", 129.15, 132.4, "setup"),                 # Bỏ tay ra! Tôi còn chưa có người yêu
 ("shot", "V3", 149.3, 156.3, "setup"),                  # mất trí nhớ ngược dòng… mười năm lấy tôi?
 ("card", ["CÔ ẤY QUÊN", "ĐÚNG MỘT NGƯỜI"], 2.4, "hit"),
 ("shot", "P05-C2", 3.0, 6.3, "twist"),                  # Anh tài xế để va li ở đấy được rồi
 ("shot", "P11-C3", 7.1, 11.1, "twist"),                 # Chị nhớ hết. … Kể cả cái cột ở sảnh.
 ("shot", "P13-C2", 2.5, 5.95, "twist"),                 # Chị muốn biết anh ấy chọn gì khi tưởng không ai thấy.
 ("card", ["NHƯNG CÓ KẺ MUỐN", "CÔ KHÔNG BAO GIỜ NHỚ LẠI"], 2.6, "braam"),
 ("shot", "P05-C4", 2.0, 5.0, "threat"),                 # Vợ chú mất trí nhớ? Tiếc thật.
 ("shot", "P12-C4", 0.3, 3.9, "threat"),                 # Anh ta cần ảnh em với anh Quân trong nhà chị.
 ("shot", "P18-C2", 10.5, 13.8, "threat"),               # Ảnh không cần đúng. Chỉ cần đủ.
 ("shot", "P20-C1", 3.6, 8.4, "threat"),                 # Vợ mất trí. → ảnh trên màn chiếu
 ("shot", "P19-C1", 9.0, 13.4, "threat"),                # Bố mất nhiều thứ lắm con ạ. Cả mẹ nữa.
 ("shot", "P20-C2", 9.2, 15.0, "threat"),                # Nhưng tôi từ chối luôn tiền của quỹ. Tôi không đem vợ ra đổi tiền.
 ("shot", "P20-C3", 4.0, 6.0, "climax"),                 # giày đỏ bước vào phòng họp
 ("shot", "P20-C4", 0.6, 2.6, "climax"),                 # Quân sững người (cắt bỏ dải chữ máy quay ở mép trên)
 ("shot", "P21-C1", 4.125, 6.125, "climax"),             # Cái gì cần nhớ, tôi nhớ rất kỹ.
 ("shot", "P21-C5", 5.5, 7.5, "climax"),                 # Hưng chết lặng
 ("black", 0.8, "silence"),
 ("shot", "P22-C1", 2.0, 5.3, "heart"),                  # Cô gái hai mươi hai tuổi ơi, em có đồng ý lấy anh không?
 ("shot", "P22-C3", 4.9, 8.2, "heart"),                  # Em không quên được đâu. Nhưng em có thể chọn lọc.
 ("shot", "P25-C6", 9.5, 15.0, "heart"),                 # pháo hoa
 ("card", ["VỢ TÔI MẤT TRÍ NHỚ", "CÓ CHỌN LỌC"], 4.2, "title"),
 ("shot", "P23-C2", 7.7, 11.6, "stinger"),               # Vi phạm thì anh mất trí nhớ lần này là thật.
 ("card", ["SẮP RA MẮT"], 2.6, "end"),
 ("black", 0.6, "end"),
]
# Bỏ khỏi trailer 19/11 (chiều) vì không nhất quán ngoại hình: Linh ở sảnh khách sạn (V3 101–104s), Linh & Khang ở P04-C1/C2,
# Khang P10-C4, Quân P17-C3 (tóc, mặt khác hẳn các cảnh còn lại).
CROP = {"P20-C2": "crop=880:495:400:110,scale=1280:720:flags=lanczos",   # đẩy vật mờ hình chữ ∩ ra ngoài khung
        "P20-C4": "crop=1232:693:24:26,scale=1280:720:flags=lanczos"}    # cắt dải chữ "24 fps ALEXA 35…" ở mép trên
def run(c):
    r = subprocess.run(c, capture_output=True, text=True)
    if r.returncode: sys.exit("ffmpeg lỗi:\n" + " ".join(c)[-600:] + "\n" + r.stderr[-1200:])
def timeline():
    t = 0.0; out = []
    for i, e in enumerate(EDL):
        d = round((e[3] - e[2]) * FPS) / FPS if e[0] == "shot" else e[1] if e[0] == "black" else e[2]
        out.append(dict(i=i, kind=e[0], start=t, dur=d, sec=e[-1], e=e)); t += d
    return out, t
def card_png(lines, path, title=False):
    from PIL import Image, ImageDraw, ImageFont
    im = Image.new("RGB", (W, H), (0, 0, 0)); dr = ImageDraw.Draw(im)
    size = 76 if title else 48; sp = 0.14 if title else 0.2
    f = ImageFont.truetype(FONT, size)
    try: f.set_variation_by_name("SemiBold" if title else "Medium")
    except Exception: pass
    lh = size * (1.45 if title else 1.6); y = H / 2 - lh * len(lines) / 2 + (size * 0.1)
    for ln in lines:
        ws = [dr.textlength(ch, font=f) for ch in ln]; tw = sum(ws) + size * sp * (len(ln) - 1); x = (W - tw) / 2
        for ch, w in zip(ln, ws):
            dr.text((x, y), ch, font=f, fill=(232, 220, 196) if title else (214, 206, 190)); x += w + size * sp
        y += lh
    if title:
        dr.line([(W/2 - 150, y + 6), (W/2 + 150, y + 6)], fill=(150, 120, 80), width=1)
    im.save(path)
def seg():
    os.makedirs(TMP, exist_ok=True); tl, T = timeline()
    for x in tl:
        e = x["e"]; dst = os.path.join(TMP, f"{x['i']:02d}.mov"); d = x["dur"]
        if os.path.exists(dst) and os.path.exists(dst + ".k") and open(dst + ".k").read() == json.dumps(e): continue
        if e[0] == "shot":
            src = os.path.join(B3, e[1] + ".mov"); fa = round(e[2] * FPS)
            vf = f"trim=start_frame={fa}:end_frame={fa + round(d * FPS)},setpts=PTS-STARTPTS," + (CROP[e[1]] + "," if e[1] in CROP else "") + f"{GRADE},format=yuv420p"
            af = f"atrim=start={fa / FPS:.4f}:duration={d:.4f},asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.04,afade=t=out:st={d - 0.06:.3f}:d=0.06"
            run(["ffmpeg","-y","-i",src,"-vf",vf,"-af",af,"-c:v","libx264","-preset","medium","-crf","16","-c:a","pcm_s16le","-ar",str(SR),"-ac","2",dst])
        else:
            png = dst[:-4] + ".png"
            if e[0] == "card": card_png(e[1], png, title=(e[-1] == "title"))
            else:
                from PIL import Image; Image.new("RGB", (W, H)).save(png)
            fi = 0.5 if e[-1] == "title" else 0.35
            vf = f"fps={FPS},format=yuv420p" + (f",fade=t=in:st=0:d={fi},fade=t=out:st={d - 0.4:.2f}:d=0.4" if e[0] == "card" else "")
            run(["ffmpeg","-y","-loop","1","-t",f"{d:.4f}","-i",png,"-f","lavfi","-t",f"{d:.4f}","-i",f"anullsrc=r={SR}:cl=stereo",
                 "-vf",vf,"-c:v","libx264","-preset","medium","-crf","16","-c:a","pcm_s16le","-shortest",dst])
        open(dst + ".k", "w").write(json.dumps(e)); print("seg", x["i"], e[0], f"{d:.2f}s", flush=True)
    print(f"tổng {T:.2f}s")
# ---------------- nhạc & hiệu ứng (numpy) ----------------
def env_ad(n, a, d):
    t = np.arange(n) / SR; return np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / d)
def lp(x, k):            # lọc thông thấp đơn giản: trung bình trượt k mẫu (lặp 2 lần)
    if k <= 1: return x
    c = np.ones(k) / k; return np.convolve(np.convolve(x, c, "same"), c, "same")
def sine(f, dur, ph=0):
    t = np.arange(int(dur * SR)) / SR; return np.sin(2 * np.pi * f * t + ph)
def boom(dur=3.0, f0=70, f1=32, amp=1.0):
    n = int(dur * SR); t = np.arange(n) / SR; f = f1 + (f0 - f1) * np.exp(-t * 4)
    ph = 2 * np.pi * np.cumsum(f) / SR; s = np.sin(ph) * np.exp(-t / 0.9)
    cl = lp(np.random.randn(n), 6) * np.exp(-t / 0.03) * 0.5
    return amp * (s + cl)
def braam(dur=3.2, root=55.0, amp=0.8):
    n = int(dur * SR); t = np.arange(n) / SR; s = np.zeros(n)
    for f, a in [(root, 1), (root * 2, .7), (root * 3, .45), (root * 1.5 * 2, .35), (root * 4.01, .25)]:
        for det in (-0.6, 0.6):
            ph = 2 * np.pi * (f + det) * t; s += a * (2 * ((ph / (2 * np.pi)) % 1) - 1) * 0.5   # răng cưa
    s = lp(s, 18); e = np.minimum(1, t / 0.08) * np.exp(-t / 1.4)
    return amp * s * e / 3
def riser(dur=4.0, amp=0.5):
    n = int(dur * SR); t = np.arange(n) / SR; x = t / dur
    nz = np.random.randn(n); bright = lp(nz, 40) * (1 - x) + lp(nz, 4) * x
    f = 180 * (2 ** (2.2 * x)); tone = np.sin(2 * np.pi * np.cumsum(f) / SR) * 0.4
    return amp * (bright * 0.7 + tone) * (x ** 2.2)
def heartbeat(amp=0.9):
    s = np.zeros(int(0.7 * SR))
    for off, a in [(0, 1), (0.22, .7)]:
        b = sine(48, 0.25) * env_ad(int(0.25 * SR), 0.005, 0.07) * a; i = int(off * SR); s[i:i + len(b)] += b
    return amp * s
def pluck(f, dur=1.2, amp=0.35, damp=0.996):
    n = int(dur * SR); p = max(2, int(SR / f)); buf = np.random.uniform(-1, 1, p); out = np.zeros(n)
    for i in range(n):
        out[i] = buf[i % p]; buf[i % p] = damp * 0.5 * (buf[i % p] + buf[(i + 1) % p])
    return amp * lp(out, 2)
def piano(f, dur=2.5, amp=0.3):
    n = int(dur * SR); t = np.arange(n) / SR; s = np.zeros(n)
    for k, a in [(1, 1), (2, .45), (3, .22), (4, .12), (5, .06)]:
        s += a * np.sin(2 * np.pi * f * k * t) * np.exp(-t * (0.9 + 0.7 * k))
    return amp * s * np.minimum(1, t / 0.004)
def pad(freqs, dur, amp=0.12, att=1.5):
    n = int(dur * SR); t = np.arange(n) / SR; s = np.zeros(n)
    for f in freqs:
        for det in (-0.25, 0.25): s += np.sin(2 * np.pi * (f + det) * t + det)
    e = np.minimum(1, t / att) * np.minimum(1, (dur - t) / min(att, dur / 2))
    return amp * s * e / len(freqs)
N = lambda m: 440.0 * 2 ** ((m - 69) / 12)
def music():
    tl, T = timeline(); n = int((T + 4) * SR); L = np.zeros(n); R = np.zeros(n)
    def add(sig, at, pan=0.0, g=1.0):
        i = int(at * SR); j = min(n, i + len(sig)); s = sig[: j - i] * g
        L[i:j] += s * math.cos((pan + 1) * math.pi / 4) * 1.41; R[i:j] += s * math.sin((pan + 1) * math.pi / 4) * 1.41
    sec = {}
    for x in tl: sec.setdefault(x["sec"], [x["start"], x["start"] + x["dur"]]); sec[x["sec"]][1] = x["start"] + x["dur"]
    cards = [x for x in tl if x["kind"] == "card"]
    # 1) mở: drone + nhịp tim
    a, b = sec["cold"]; add(pad([N(33), N(40), N(45)], b - a + 1.0, 0.16, 1.2), a)
    t = 0.25
    while t < cards[0]["start"] - 0.3: add(heartbeat(0.8), t); t += 0.95
    add(boom(3.2, amp=0.9), cards[0]["start"]); add(riser(1.2, 0.25), cards[0]["start"] - 1.2)
    # 2) giới thiệu (hài nhẹ): pluck nhịp 104 bpm, cung La thứ ngũ cung
    a, b = sec["setup"]; beat = 60 / 104; motif = [57, 60, 64, 62, 60, 64, 67, 64, 57, 60, 62, 64, 62, 60, 59, 60]
    k = 0; t = a + 0.2
    while t < b - 0.3:
        m = motif[k % 16]; add(pluck(N(m), 0.9, 0.22), t, pan=(-0.3 if k % 2 else 0.3)); 
        if k % 4 == 0: add(pluck(N(m - 24), 1.4, 0.3, 0.998), t)
        t += beat / 2 if k % 8 in (2, 3, 6, 7) else beat; k += 1
    add(pad([N(45), N(52), N(57)], b - a, 0.07, 2.0), a)
    # 3) thẻ 2: cú đập
    c = cards[1]; add(riser(1.6, 0.35), c["start"] - 1.6); add(boom(3.0, amp=1.0), c["start"])
    # 4) lật mặt: pluck tinh nghịch + bass
    a, b = sec["twist"]; motif2 = [69, 67, 64, 67, 69, 72, 69, 67]; k = 0; t = a + 0.1
    while t < b - 0.2:
        add(pluck(N(motif2[k % 8]), 0.8, 0.2), t, pan=0.25 * ((-1) ** k))
        if k % 2 == 0: add(pluck(N(45 if k % 4 == 0 else 40), 1.0, 0.32, 0.997), t)
        t += beat / 2 * (2 if k % 4 == 3 else 1); k += 1
    # 5) thẻ 3: braam
    c = cards[2]; add(braam(3.6, 55.0, 0.9), c["start"]); add(boom(3.0, amp=0.8), c["start"])
    # 6) âm mưu: ostinato 120 bpm + tiếng tích tắc + drone dâng
    a, b = sec["threat"]; e8 = 0.25; t = a; k = 0
    while t < b:
        g = 0.55 + 0.45 * (t - a) / (b - a)
        add(sine(N(33 + (5 if (k // 16) % 2 else 0)), 0.2) * env_ad(int(0.2 * SR), 0.004, 0.08), t, g=0.55 * g)
        if k % 2 == 0: add(lp(np.random.randn(int(0.03 * SR)), 2) * env_ad(int(0.03 * SR), 0.001, 0.006), t, pan=0.5, g=0.12 * g)
        t += e8; k += 1
    add(pad([N(33), N(40), N(44)], b - a, 0.14, 2.5), a)
    add(riser(5.0, 0.55), b - 5.0)
    # 7) cao trào: cú đập mỗi nhát cắt
    for x in tl:
        if x["sec"] == "climax": add(boom(2.2, 90, 35, 0.95), x["start"]); add(braam(2.0, 55.0 * (1.0 if x["i"] % 2 else 1.189), 0.45), x["start"])
    # 8) lặng 0.8s rồi piano + pad cảm xúc (Am – F – C – G)
    a, b = sec["heart"]; prog = [(57, [57, 60, 64]), (53, [53, 57, 60]), (48, [55, 60, 64]), (55, [55, 59, 62])]
    span = (b - a) / 4
    for ci, (bass, ch) in enumerate(prog):
        t0 = a + ci * span; add(piano(N(bass - 12), 3.5, 0.32), t0)
        for j in range(6):
            add(piano(N(ch[j % 3] + (12 if j >= 3 else 0)), 2.2, 0.17), t0 + j * span / 6, pan=0.2 * ((-1) ** j))
        add(pad([N(m) for m in ch], span + 0.8, 0.08 + 0.05 * ci, 0.6), t0)
    add(riser(2.4, 0.3), b - 2.4)
    # 9) tựa phim: cú đập lớn + nốt ngân
    c = cards[3]; add(boom(4.0, 80, 30, 1.1), c["start"]); add(braam(4.0, 55.0, 0.6), c["start"])
    add(pad([N(57), N(64), N(69), N(76)], c["dur"] + 0.6, 0.12, 0.3), c["start"])
    # 10) câu chốt hài: hai nốt pluck
    a, b = sec["stinger"]; add(pluck(N(64), 0.9, 0.22), b - 0.9); add(pluck(N(57), 1.2, 0.26), b - 0.5)
    # 11) sắp ra mắt
    c = cards[4]; add(boom(3.0, amp=0.9), c["start"])
    pk = max(np.abs(L).max(), np.abs(R).max()); L /= pk; R /= pk
    st = (np.stack([L, R], 1) * 0.89 * 32767).astype(np.int16)
    with wave.open(os.path.join(TMP, "music.wav"), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(st.tobytes())
    print("nhạc", f"{T:.1f}s")
FLOWMUSIC = os.path.join(HERE, "nhac", "take2.wav")   # nhạc tạo trên Flow Music (Lyria 3.5), bản 2
def read_wav(p):
    r = subprocess.run(["ffmpeg","-v","error","-i",p,"-f","f32le","-ac","2","-ar",str(SR),"-"],capture_output=True)
    return np.frombuffer(r.stdout, dtype=np.float32).reshape(-1, 2).astype(np.float64)
def music_flow():
    """Ghép nhạc Flow Music vào nhịp dựng theo các mốc (giờ trailer T ↔ giờ nhạc M).
    Mốc nhạc bản 2: mở 1.0s · cú đập 40.0s · braam 56.0s · nhịp 120 bpm · cao trào lấy đoạn đập 73.5–81.5s · cảm xúc từ 88.0s.
    Giữa hai mốc, nếu độ dài lệch thì bỏ bớt hoặc lặp lại nhạc ở giữa đoạn, theo bội số 2s (1 ô nhịp) hoặc 0.5s (1 phách)."""
    tl, T = timeline(); Mw = read_wav(FLOWMUSIC); n = int((T + 1) * SR); out = np.zeros((n, 2))
    cards = [x for x in tl if x["kind"] == "card"]; cl = [x for x in tl if x["sec"] == "climax"]; ht = [x for x in tl if x["sec"] == "heart"]
    t_cl = cl[0]["start"]; t_sil = cl[-1]["start"] + cl[-1]["dur"]; t_ht = ht[0]["start"]
    anchors = [(0.0, 1.0), (cards[1]["start"], 40.0), (cards[2]["start"], 56.0), (t_cl, 73.5), (t_sil, 81.5)]
    plan = []
    for (ta, ma), (tb, mb) in zip(anchors, anchors[1:]):
        d = (mb - ma) - (tb - ta); k2 = round(d / 2) * 2
        j = k2 if abs(d - k2) <= 0.5 else round(d / 0.5) * 0.5
        r = d - j; ma2 = ma + r
        if abs(j) < 1e-6: plan.append((ta, tb, ma2)); continue
        mid = round(((ma2 + mb) / 2) / 2) * 2
        if j < 0: mid = max(mid, math.ceil((ma2 + abs(j) + 2) / 2) * 2)   # lặp: không phát lại cú đập ở mốc đầu
        tm = ta + (mid - ma2); plan += [(ta, tm, ma2), (tm, tb, mid + j)]
        print(f"  đoạn {ta:.2f}–{tb:.2f}: {'bỏ' if j > 0 else 'lặp'} {abs(j):.1f}s nhạc tại M{mid:.1f}, lệch {r:+.2f}s")
    plan.append((t_ht, T, 88.0))
    xf = int(0.08 * SR)
    for a, b, m0 in plan:
        i0 = int(a * SR); k0 = int(m0 * SR); L = min(int((b - a) * SR) + xf, len(Mw) - k0, n - i0)
        if L <= 0: continue
        seg = Mw[k0:k0 + L].copy(); r = np.ones(L); r[:xf] = np.linspace(0, 1, xf); r[-xf:] = np.linspace(1, 0, xf)
        if a == 0.0: r[:xf] = 1
        out[i0:i0 + L] += seg * r[:, None]
    out[int(t_sil * SR):int(t_ht * SR)] = 0
    def add(sig, at, g=1.0):
        i = int(at * SR); j = min(n, i + len(sig)); out[i:j] += (sig[:j - i] * g)[:, None]
    t = 0.25
    while t < cards[0]["start"] - 0.3: add(heartbeat(0.8), t, 0.35); t += 0.95
    add(boom(3.0, amp=0.9), cards[-1]["start"], 0.5)
    pk = np.abs(out).max(); out = out / pk * 0.89
    st = (out * 32767).astype(np.int16)
    with wave.open(os.path.join(TMP, "music.wav"), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(st.tobytes())
    print("nhạc Flow Music ghép xong", f"{T:.1f}s", "cao trào", f"{t_cl:.2f}", "lặng", f"{t_sil:.2f}", "cảm xúc", f"{t_ht:.2f}")
def mix():
    tl, T = timeline(); segs = [os.path.join(TMP, f"{x['i']:02d}.mov") for x in tl]
    lst = os.path.join(TMP, "list.txt"); open(lst, "w").writelines(f"file '{s}'\n" for s in segs)
    base = os.path.join(TMP, "base.mov"); run(["ffmpeg","-y","-f","concat","-safe","0","-i",lst,"-c","copy",base])
    fc = ("[0:a]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,asplit=2[dlg][key];"
          "[1:a]lowpass=f=12000,volume=0.6,aformat=sample_fmts=fltp:channel_layouts=stereo[mus];"
          "[mus][key]sidechaincompress=threshold=0.02:ratio=8:attack=15:release=400:makeup=1[duck];"
          "[dlg][duck]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-14:TP=-1.0:LRA=12,aformat=channel_layouts=stereo[a]")
    fc1 = fc.replace(",loudnorm=I=-14:TP=-1.0:LRA=12", "")
    pre = os.path.join(TMP, "premix.wav")
    run(["ffmpeg","-y","-i",base,"-i",os.path.join(TMP,"music.wav"),"-filter_complex",fc1,"-map","[a]","-c:a","pcm_s24le",pre])
    r = subprocess.run(["ffmpeg","-hide_banner","-i",pre,"-af","loudnorm=I=-14:TP=-1.0:LRA=16:print_format=json","-f","null","-"],capture_output=True,text=True).stderr
    m = json.loads(r[r.rindex("{"):r.rindex("}") + 1])
    ln = (f"loudnorm=I=-14:TP=-1.0:LRA=16:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}"
          f":measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true,aresample=48000,aformat=channel_layouts=stereo")
    run(["ffmpeg","-y","-i",base,"-i",pre,"-map","0:v","-map","1:a","-af",ln,
         "-c:v","libx264","-preset","slow","-crf","17","-pix_fmt","yuv420p","-c:a","aac","-b:a","256k","-movflags","+faststart",OUT])
    os.remove(pre)
    os.remove(base); print("Xong:", OUT)
if __name__ == "__main__":
    a = sys.argv[1] if len(sys.argv) > 1 else "all"
    if a == "plan":
        tl, T = timeline(); [print(f"{x['start']:6.2f} {x['dur']:5.2f} {x['sec']:8s} {x['e'][1] if x['kind']=='shot' else x['kind']}") for x in tl]; print(T)
    elif a == "all": seg(); music_flow(); mix()
    elif a == "flow": music_flow()
    else: {"seg": seg, "music": music, "mix": mix}[a]()
