#!/usr/bin/env python3
"""Bản clip 10 giây cho Flow web (Omni 1.2 Flash trên giao diện web tối đa 10s, 17/11/2026).

Mỗi clip 15s (3 lượt thoại) được tách thành 2 clip 10s:
  clip a = lượt 1 + lượt 2 (giữ nguyên văn),
  clip b = lượt 3 + một câu đáp mới (REPLY bên dưới) để clip không bị trống tiếng.
Mặc định sinh 30 clip đầu (cảnh 01.1 → 04.3) vào vo-toi-mat-tri-nho/flow_10s/.

    python3 vo-toi-mat-tri-nho/_parts/build_10s.py            # 30 clip đầu
    python3 vo-toi-mat-tri-nho/_parts/build_10s.py 01.1 08.4  # khoảng clip 15s khác
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SDIR = os.path.dirname(HERE)
REPO = os.path.dirname(SDIR)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(REPO, "flowkit", "scripts"))
import build_omni_horror_prompts as B  # noqa: E402
import header_data as H  # noqa: E402
import build_json as J  # noqa: E402
from scenes_act1 import SCENES as A1  # noqa: E402
from scenes_act2 import SCENES as A2  # noqa: E402
from scenes_act3 import SCENES as A3  # noqa: E402

D = 10
LIMIT = D - 0.6  # lời nói phải xong trước 9.4s

# Câu đáp mới cho clip b: (speaker, pace, tone, line, [hành động]) — speaker phải có trong clip.
REPLY = {
    "01.1": ("@Linh", "slow", "dry", "Ừ, chín mươi chín bông, đẹp thật. Chỉ thiếu đúng một người tặng thôi.", ["looking at the roses", "setting them aside"]),
    "01.2": ("@Tuan", "fast", "sheepish", "Dạ, em tập rồi chị ạ, mà gương nhà em nó cũng không tin!", ["scratching the back of his head", "grinning helplessly"]),
    "01.3": ("@Tuan", "fast", "sheepish", "Dạ, thật thà là điểm mạnh duy nhất của em đấy chị ạ!", ["scratching his head", "grinning weakly"]),
    "01.4": ("@Tuan", "slow", "deflated, to himself", "Mà thôi, em cũng phải lo lấy thân em trước đã.", ["lowering the phone", "staring at the closed elevator doors"]),
    "02.1": ("@Quan", "normal", "evasive", "Ừ, để anh xem lịch đã. Tối nay anh còn một cuộc họp nữa.", ["checking his silver watch", "glancing at the elevators"]),
    "02.2": ("@MaiAnh", "fast", "sulky", "Lai Hàn á? Anh nói dối kém thế! Thôi được, em đứng sau cột vậy.", ["rolling her eyes", "stomping off toward the pillar"]),
    "02.3": ("@Linh", "slow", "icy deadpan", "Ừ. Toàn cột. Mà cột nào cũng biết đi giày cao gót.", ["glancing down at a pair of white heels peeking out behind the pillar", "looking back at him"]),
    "02.4": ("@Quan", "fast", "frantic", "Em đừng đùa anh! Vợ ơi, mở mắt ra nhìn anh này, vợ ơi!", ["kneeling beside the sofa", "patting her hand"]),
    "03.1": ("@Linh", "fast", "indignant", "Chồng mười năm? Anh trông già thế này mà đòi làm chồng một cô gái hai mươi hai tuổi à?", ["looking him up and down", "pulling the blanket higher"]),
    "03.2": ("@Quan", "fast", "exasperated", "Chịu là thế nào? Mười năm cơm nước, ngày nào cũng gặp, em nhớ con mà quên bố nó à?", ["throwing up his hands", "pacing beside the bed"]),
    "03.3": ("@Quan", "slow", "stunned, quiet", "Tôi làm cô ấy đau đến thế sao?", ["staring at the closed door", "loosening his collar"]),
    "03.4": ("@Khang", "slow", "dry deadpan", "Tạm thời thì anh là người lạ. Một người lạ rất đáng ngờ.", ["closing the white folder", "giving a small shrug"]),
    "04.1": ("@Linh", "fast", "gleeful", "Bác sĩ thì càng tốt! Bệnh án do cậu ký, ai mà dám cãi!", ["clapping her hands softly", "beaming at him"]),
    "04.2": ("@Khang", "slow", "gentle", "Cậu vẫn còn thương anh ta nhiều lắm, đúng không?", ["leaning forward", "watching her eyes"]),
    "04.3": ("@Khang", "normal", "resigned, dry", "Được. Tớ giúp. Nhưng lỡ lộ ra thì tớ bảo là tớ không quen cậu.", ["putting his glasses back on", "holding up one finger"]),
}

# Rút ngắn lượt 1/2 khi clip a không vừa 10s: {clip: {chỉ số lượt: câu mới}}
SHORTEN = {
    "03.2": {0: "Chồng á? Anh đùa à? Tôi mới hai mươi hai tuổi, đang đi thi người mẫu cơ mà!"},
    "03.4": {0: "Bao giờ cô ấy nhớ lại? Tuần sau tôi cần cô ấy ký giấy.",
             1: "Chưa ký được đâu. Về pháp lý, chị ấy đang là cô gái hai mươi hai tuổi."},
}

DATA = {**J.header(), "clip_seconds": D}
J.D = D  # generator functions use J.D


ROLE = {"@Linh": "32, the elegant wife", "@Quan": "36, the handsome husband", "@MaiAnh": "25, the young yoga teacher",
        "@Khang": "34, the doctor with rimless glasses", "@Tuan": "35, the dimpled assistant", "@Bong": "7, the little girl"}


def lean(prompt: str, c: dict) -> str:
    """Bản gọn cho ô nhập Flow web: ảnh nhân vật đã giữ khuôn mặt nên chỉ ghi vai + trang phục, bỏ khối ánh sáng."""
    prompt = re.sub(r"\[LIGHTING\]\n[^\n]*\n\n", "", prompt)
    ward = c.get("wardrobe") or {}
    lines = ["[CHARACTERS]", "Use the attached character images for every face and hairstyle; keep them exactly consistent. "
             "The characters are already in place in the first frame; never show the reference portrait."]
    for t in c["chars"]:
        outfit = ward.get(t) or H.CHARACTERS[t]["anchor"].split("; ")[-1].rstrip(".")
        note = " (this outfit, not the one in the reference image)" if t in ward else ""
        lines.append(f"- {t} = {H.CHARACTERS[t]['name']}, {ROLE[t]}; wears {outfit}{note}.")
    lines.append("Nobody else appears in the shot.")
    return re.sub(r"\[CHARACTERS\]\n.*?Nobody else appears in the shot\.", "\n".join(lines), prompt, flags=re.S)


def plan_of(c):
    tmp = dict(c, _dialogue_only=True, steps=[""] * D)
    return B.speech_plan(DATA, tmp, "cut", D, clamp=False)


def make_clip(sc, cl, cid, turns, acts, tail, seed):
    setting = H.S[cl["set"]] if cl.get("set") else H.S[sc["setting"]]
    c = {"id": cid, "chars": cl["c"],
         "turns": [{"speaker": s, "line": ln, "pace": p, "tone": tone} for s, p, tone, ln in turns],
         "continuity": "cut", "sfx": cl.get("sfx", sc["sfx"]), "setting": setting}
    ward = dict(sc.get("wardrobe") or {})
    ward.update(cl.get("wardrobe") or {})
    ward = {t: H.W[w] for t, w in ward.items() if w and t in cl["c"]}
    if ward:
        c["wardrobe"] = ward
    plan = plan_of(c)
    own = J.owners(plan)
    fake = {"c": cl["c"], "t": turns, "a": acts, "tail": tail}
    c["shots"] = J.build_shots(fake, plan, own, sc["room"], seed)
    c["steps"] = J.build_steps(fake, plan, own)
    c["_dialogue_only"] = True
    return c, plan


def main() -> int:
    lo, hi = (sys.argv[1], sys.argv[2]) if len(sys.argv) > 2 else ("01.1", "04.3")
    out_dir = os.path.join(SDIR, "flow_10s")
    os.makedirs(out_dir, exist_ok=True)
    errors, rows, seed = [], [], 0
    for sc in A1 + A2 + A3:
        for i, cl in enumerate(sc["clips"]):
            cid = f"{sc['num']:02d}.{i + 1}"
            if not (lo <= cid <= hi):
                continue
            if cid not in REPLY:
                errors.append(f"{cid}: chưa có câu đáp REPLY cho clip b")
                continue
            t1, t2, t3 = cl["t"]
            fix = SHORTEN.get(cid, {})
            t1 = (*t1[:3], fix[0]) if 0 in fix else t1
            t2 = (*t2[:3], fix[1]) if 1 in fix else t2
            a = cl["a"]
            sp, p, tone, ln, ra = REPLY[cid]
            parts = [
                (f"{cid}a", [t1, t2], [a[0], a[1]], []),
                (f"{cid}b", [t3, (sp, p, tone, ln)], [a[2], ra], cl["tail"]),
            ]
            for pid, turns, acts, tail in parts:
                seed += 1
                c, plan = make_clip(sc, cl, pid, turns, acts, tail, seed)
                end = plan[-1][3]
                syl = sum(B.syllables(t[3]) for t in turns)
                if end > LIMIT:
                    errors.append(f"{pid}: lời nói hết lúc {end:.1f}s > {LIMIT}s — rút ngắn")
                if end < D - 3.0:
                    errors.append(f"{pid}: lời nói hết sớm ({end:.1f}s) — Omni dễ nói lặp, thêm chữ")
                vis = " ".join(c["steps"] + [s["camera"] for s in c["shots"]])
                for pat in B.BANNED_VISUAL:
                    if re.search(pat, vis, re.I):
                        errors.append(f"{pid}: từ rủi ro {pat}")
                prompt = B.render_prompt(DATA, sc, c, "cut")
                with open(os.path.join(out_dir, f"{pid}.md"), "w", encoding="utf-8") as f:
                    f.write(prompt)
                os.makedirs(os.path.join(out_dir, "web"), exist_ok=True)
                with open(os.path.join(out_dir, "web", f"{pid}.txt"), "w", encoding="utf-8") as f:
                    f.write(lean(prompt, c))
                who = " ".join(t[0] for t in turns)
                rows.append(f"| {pid} | {', '.join(cl['c'])} | {syl} | 0.4–{end:.1f}s | " + " / ".join(f"{t[0]}: {t[3]}" for t in turns) + " |")
    with open(os.path.join(out_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(f"# {H.TITLE} — clip 10 giây cho Flow web ({len(rows)} clip)\n\n"
                "Mỗi clip 15s được tách thành clip a (lượt 1+2) và clip b (lượt 3 + câu đáp mới). "
                "Tạo trên Flow: Video · Thành phần (gắn ảnh nhân vật) · 16:9 · Omni 1.2 Flash · 720p · 10 giây.\n\n"
                "| Clip | Nhân vật | Âm tiết | Khung thoại | Lời thoại |\n|---|---|---|---|---|\n" + "\n".join(rows) + "\n")
    for e in errors:
        print("ERROR", e)
    print(f"{len(rows)} clip 10s → {out_dir}, {len(errors)} lỗi")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
