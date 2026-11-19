#!/usr/bin/env python3
"""Trailer điện ảnh bản 4 (19/11) — theo tinh thần trailer phim Việt chiếu rạp:
khung 2.39:1, mở màn đen + âm thanh không khí, thẻ chữ vàng ánh kim trên nền tàn lửa, cắt nhanh dần về cao trào,
mỗi câu thoại giữ nguyên hình người đang nói, phụ đề tiếng Anh, nhạc Flow Music.
Dùng: python3 trailer/v4/make_trailer4.py seg | flow | mix | subs | all"""
import os, sys, json, math, subprocess, wave
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(os.path.dirname(HERE), "v3"))
import make_trailer3 as M3
from cards import render_card, BAR
B3 = os.path.expanduser("~/b3"); TMP = os.path.expanduser("~/trw/seg4")
OUT = os.path.join(HERE, "Trailer_Vo_toi_mat_tri_nho_v4.mp4")
W, H, FPS, SR = 1280, 720, 24, 48000
GRADE = "eq=contrast=1.06:saturation=0.9:gamma=0.97,colorbalance=rs=-0.02:bs=0.03:rh=0.03:bh=-0.02,vignette=angle=0.35"
CROP = {"P20-C2": "crop=880:495:400:110,scale=1280:720:flags=lanczos"}
YSHIFT = {}                                              # dịch khung 2.39 lên/xuống cho từng shot (px, âm = lên)
STUDIO = "HIDDEN CINEMA"
# (loại, ...) — shot: (nguồn, vào, ra, đoạn, phụ đề Anh)
EDL = [
 ("black", 1.6, "cold"),
 ("shot", "V3", 0.0, 2.8, "cold", ""),
 ("card", [(STUDIO, 40, 0.32, "SemiBold"), ("TRÂN TRỌNG GIỚI THIỆU", 26, 0.42, "Medium")], 2.8, "cold"),
 ("shot", "V3", 9.5, 15.6, "setup", "Ms. Linh! Mr. Quân had an urgent meeting with a Japanese partner. He sent these for you.|Oh, did he?"),
 ("shot", "V3", 41.3, 48.4, "setup", "Since when do Japanese partners wear white dresses and hang on my husband's arm?"),
 ("shot", "V3", 58.1, 61.0, "setup", "Then I'll go down and say hello to this Japanese partner."),
 ("shot", "V3", 97.65, 100.8, "setup", "Which pillar? This hotel is nothing but pillars, darling!"),
 ("shot", "V3", 116.9, 118.9, "setup", "Who... are you?"),
 ("shot", "V3", 129.15, 132.4, "setup", "Let go of me! I don't even have a boyfriend!"),
 ("shot", "V3", 149.3, 156.3, "setup", "Retrograde amnesia. She's forgotten exactly the last ten years.|Exactly the ten years she's been married to me?"),
 ("card", [("CÔ ẤY QUÊN", 48, 0.22, "SemiBold"), ("ĐÚNG MỘT NGƯỜI", 48, 0.22, "SemiBold")], 2.4, "hit"),
 ("shot", "P05-C2", 3.0, 6.3, "twist", "You can leave the suitcase there, driver. Thank you."),
 ("shot", "P11-C3", 7.1, 11.1, "twist", "I remember everything. Even the pillar in the lobby."),
 ("shot", "P13-C2", 2.5, 5.95, "twist", "I want to see what he chooses when he thinks no one is watching."),
 ("shot", "P09-C3", 6.6, 11.3, "twist", "Five points. Minus five for being ten years late."),
 ("card", [("NHƯNG CÓ KẺ MUỐN", 44, 0.22, "SemiBold"), ("CÔ KHÔNG BAO GIỜ NHỚ LẠI", 44, 0.22, "SemiBold")], 2.6, "braam"),
 ("shot", "P05-C4", 2.0, 5.0, "threat", "I hear your wife lost her memory. What a pity."),
 ("shot", "P12-C4", 0.3, 3.9, "threat", "He wants photos of me and Quân inside your house."),
 ("shot", "P18-C2", 10.5, 14.45, "threat", "A photo doesn't need to be true. Just convincing enough."),
 ("shot", "P20-C1", 3.6, 8.4, "threat", "A wife who's lost her mind."),
 ("shot", "P19-C1", 9.6, 13.4, "threat", "I've lost so much, sweetie. Even your mom."),
 ("shot", "P20-C2", 9.2, 15.0, "threat", "And I'm turning down the fund's money.|I won't trade my wife for money."),
 ("shot", "P20-C3", 4.0, 6.0, "climax", ""),
 ("shot", "P20-C4", 0.6, 2.6, "climax", ""),
 ("shot", "P21-C1", 4.125, 6.125, "climax", "Whatever needs remembering, I remember very well."),
 ("shot", "P21-C5", 5.5, 7.5, "climax", ""),
 ("black", 0.8, "silence"),
 ("shot", "P22-C1", 0.0, 4.3, "heart", "Twenty-two-year-old girl... will you marry me?"),
 ("shot", "P22-C3", 4.9, 8.2, "heart", "I can't forget. But I can be selective."),
 ("shot", "P25-C6", 9.5, 15.0, "heart", ""),
 ("card", [("VỢ TÔI MẤT TRÍ NHỚ", 80, 0.08, "Bold"), ("CÓ CHỌN LỌC", 50, 0.3, "SemiBold")], 4.4, "title"),
 ("shot", "P23-C2", 7.7, 11.6, "stinger", "Break the rules, and this time the memory loss will be real."),
 ("card", [("SẮP KHỞI CHIẾU", 40, 0.36, "SemiBold")], 2.8, "end"),
 ("black", 0.6, "end"),
]
def run(c):
    r = subprocess.run(c, capture_output=True, text=True)
    if r.returncode: sys.exit("ffmpeg lỗi:\n" + " ".join(c)[-500:] + "\n" + r.stderr[-1200:])
def timeline():
    t = 0.0; out = []
    for i, e in enumerate(EDL):
        d = round((e[3] - e[2]) * FPS) / FPS if e[0] == "shot" else e[1] if e[0] == "black" else e[2]
        sec = e[4] if e[0] == "shot" else e[-1]
        out.append(dict(i=i, kind=e[0], start=t, dur=d, sec=sec, e=e)); t += d
    return out, t
def seg():
    os.makedirs(TMP, exist_ok=True); tl, T = timeline()
    for x in tl:
        e = x["e"]; dst = os.path.join(TMP, f"{x['i']:02d}.mov"); d = x["dur"]; key = json.dumps(e, ensure_ascii=False) + GRADE + str(YSHIFT.get(e[1] if e[0] == "shot" else "", 0))
        if os.path.exists(dst) and os.path.exists(dst + ".k") and open(dst + ".k").read() == key: continue
        if e[0] == "shot":
            src = os.path.join(B3, e[1] + ".mov"); fa = round(e[2] * FPS); ys = YSHIFT.get(e[1], 0)
            box = f"drawbox=x=0:y=0:w={W}:h={BAR}:color=black:t=fill,drawbox=x=0:y={H-BAR}:w={W}:h={BAR}:color=black:t=fill"
            shift = f"crop={W}:{H}:0:{max(0,ys)},pad={W}:{H}:0:{max(0,-ys)}," if ys else ""
            vf = f"trim=start_frame={fa}:end_frame={fa + round(d * FPS)},setpts=PTS-STARTPTS," + (CROP[e[1]] + "," if e[1] in CROP else "") + shift + f"{GRADE},{box},format=yuv420p"
            af = f"atrim=start={fa / FPS:.4f}:duration={d:.4f},asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.04,afade=t=out:st={d - 0.06:.3f}:d=0.06"
            run(["ffmpeg","-y","-i",src,"-vf",vf,"-af",af,"-c:v","libx264","-preset","medium","-crf","16","-c:a","pcm_s16le","-ar",str(SR),"-ac","2",dst])
        elif e[0] == "card":
            render_card(e[1], d, dst, title=(e[-1] == "title"), seed=x["i"] + 3)
        else:
            run(["ffmpeg","-y","-f","lavfi","-t",f"{d:.4f}","-i",f"color=c=black:s={W}x{H}:r={FPS}","-f","lavfi","-t",f"{d:.4f}","-i",f"anullsrc=r={SR}:cl=stereo",
                 "-c:v","libx264","-preset","medium","-crf","16","-pix_fmt","yuv420p","-c:a","pcm_s16le","-shortest",dst])
        open(dst + ".k", "w").write(key); print("seg", x["i"], e[0], f"{d:.2f}s", flush=True)
    print(f"tổng {T:.2f}s")
def music_flow():
    """Nhạc Flow Music bản 2 khớp mốc: thẻ 'cô ấy quên' ↔ cú đập 40s, thẻ 'nhưng có kẻ' ↔ braam 56s, cao trào ↔ 73.5–81.5s, cảm xúc từ 88s."""
    tl, T = timeline(); Mw = M3.read_wav(M3.FLOWMUSIC); n = int((T + 1) * SR); out = np.zeros((n, 2))
    cards = [x for x in tl if x["kind"] == "card"]; by = {x["sec"]: x for x in cards}
    cl = [x for x in tl if x["sec"] == "climax"]; ht = [x for x in tl if x["sec"] == "heart"]
    t_cl = cl[0]["start"]; t_sil = cl[-1]["start"] + cl[-1]["dur"]; t_ht = ht[0]["start"]
    anchors = [(0.0, 1.0), (by["hit"]["start"], 40.0), (by["braam"]["start"], 56.0), (t_cl, 73.5), (t_sil, 81.5)]
    plan = []
    for (ta, ma), (tb, mb) in zip(anchors, anchors[1:]):
        d = (mb - ma) - (tb - ta); j = round(d / 2) * 2; r = d - j      # nhảy theo ô nhịp 2s; phần lẻ r dồn vào điểm nối
        if ta == 0.0: plan.append((0.0, tb, ma + d)); continue           # đoạn đầu: chỉ cần khớp mốc cuối
        if abs(d) < 0.05: plan.append((ta, tb, ma)); continue
        mid = round(((ma + mb) / 2) / 2) * 2
        if j < 0: mid = max(mid, math.ceil((ma + abs(j) + 2) / 2) * 2)
        tm = ta + (mid - ma); plan += [(ta, tm, ma), (tm, tb, mid + j + r)]
        print(f"  đoạn {ta:.2f}–{tb:.2f}: {'bỏ' if j > 0 else 'lặp'} {abs(j):.1f}s nhạc tại M{mid:.1f}, lệch {r:+.2f}s")
    plan.append((t_ht, T, 88.0))
    xf = int(0.08 * SR)
    for a, b, m0 in plan:
        i0 = int(a * SR); k0 = int(m0 * SR); L = min(int((b - a) * SR) + xf, len(Mw) - k0, n - i0)
        if L <= 0: continue
        seg = Mw[k0:k0 + L].copy(); rr = np.ones(L); rr[:xf] = np.linspace(0, 1, xf); rr[-xf:] = np.linspace(1, 0, xf)
        if a == 0.0: rr[:xf] = 1
        out[i0:i0 + L] += seg * rr[:, None]
    out[int(t_sil * SR):int(t_ht * SR)] = 0
    out[:int(1.6 * SR)] *= np.linspace(0, 1, int(1.6 * SR))[:, None] ** 2          # mở: nhạc dâng chậm từ màn đen
    def add(sig, at, g=1.0):
        i = int(at * SR); j = min(n, i + len(sig)); out[i:j] += (sig[:j - i] * g)[:, None]
    # không khí mở màn: gió đêm + tiếng tim
    rng = np.random.default_rng(3); wind = M3.lp(rng.standard_normal(int(4.4 * SR)), 60) * 0.5
    wind *= np.minimum(1, np.arange(len(wind)) / SR / 1.0) * np.minimum(1, (len(wind) / SR - np.arange(len(wind)) / SR) / 1.2)
    add(wind, 0.0, 0.6)
    t = 0.3
    while t < by["cold"]["start"] - 0.3: add(M3.heartbeat(0.8), t, 0.4); t += 0.95
    add(M3.boom(3.0, amp=0.9), by["cold"]["start"], 0.45)
    add(M3.boom(3.0, amp=0.9), by["end"]["start"], 0.5)
    pk = np.abs(out).max(); out = out / pk * 0.89
    st = (out * 32767).astype(np.int16)
    with wave.open(os.path.join(TMP, "music.wav"), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(st.tobytes())
    print("nhạc ghép xong", f"{T:.1f}s")
def mix(subs=None):
    tl, T = timeline(); segs = [os.path.join(TMP, f"{x['i']:02d}.mov") for x in tl]
    lst = os.path.join(TMP, "list.txt"); open(lst, "w").writelines(f"file '{s}'\n" for s in segs)
    base = os.path.join(TMP, "base.mov"); run(["ffmpeg","-y","-f","concat","-safe","0","-i",lst,"-c","copy",base])
    fc = ("[0:a]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,asplit=2[dlg][key];"
          "[1:a]lowpass=f=12000,volume=0.6,aformat=sample_fmts=fltp:channel_layouts=stereo[mus];"
          "[mus][key]sidechaincompress=threshold=0.02:ratio=8:attack=15:release=400:makeup=1[duck];"
          "[dlg][duck]amix=inputs=2:normalize=0:duration=first,aformat=channel_layouts=stereo[a]")
    pre = os.path.join(TMP, "premix.wav")
    run(["ffmpeg","-y","-i",base,"-i",os.path.join(TMP,"music.wav"),"-filter_complex",fc,"-map","[a]","-c:a","pcm_s24le",pre])
    r = subprocess.run(["ffmpeg","-hide_banner","-i",pre,"-af","loudnorm=I=-14:TP=-1.0:LRA=16:print_format=json","-f","null","-"],capture_output=True,text=True).stderr
    m = json.loads(r[r.rindex("{"):r.rindex("}") + 1])
    ln = (f"loudnorm=I=-14:TP=-1.0:LRA=16:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}"
          f":measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true,aresample=48000,aformat=channel_layouts=stereo")
    vf = ["-vf", f"subtitles={subs}"] if subs and os.path.exists(subs) else []
    run(["ffmpeg","-y","-i",base,"-i",pre,"-map","0:v","-map","1:a"] + vf + ["-af",ln,
         "-c:v","libx264","-preset","slow","-crf","17","-pix_fmt","yuv420p","-c:a","aac","-b:a","256k","-movflags","+faststart",OUT])
    os.remove(pre); os.remove(base); print("Xong:", OUT, f"{T:.1f}s")
def ass(cues, path):
    """cues: [(start, end, text)] → file .ass (chữ trắng nhỏ, mép dưới khung hình 2.39)."""
    def ts(t): h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60; return f"{h}:{m:02d}:{s:05.2f}"
    head = ("[Script Info]\nScriptType: v4.00+\nPlayResX: 1280\nPlayResY: 720\n\n[V4+ Styles]\n"
            "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\n"
            f"Style: Sub,Lato,27,&H00F0F0F0,&H00F0F0F0,&H00000000,&H64000000,0,0,0,0,100,100,0.3,0,1,1.2,0.6,2,80,80,{BAR + 22},1\n\n"
            "[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n")
    open(path, "w").write(head + "".join(f"Dialogue: 0,{ts(a)},{ts(b)},Sub,,0,0,0,,{t}\n" for a, b, t in cues))
if __name__ == "__main__":
    a = sys.argv[1] if len(sys.argv) > 1 else "plan"
    if a == "plan":
        tl, T = timeline(); [print(f"{x['i']:2d} {x['start']:6.2f} {x['dur']:5.2f} {x['sec']:8s} {x['e'][1] if x['kind']=='shot' else x['kind']}") for x in tl]; print(T)
    elif a == "seg": seg()
    elif a == "flow": music_flow()
    elif a == "mix": mix(sys.argv[2] if len(sys.argv) > 2 else None)
