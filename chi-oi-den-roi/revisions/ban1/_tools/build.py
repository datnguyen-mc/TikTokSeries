# -*- coding: utf-8 -*-
"""Sinh NHAN_VAT_FLOW.md, SHOTS.md, kich-ban/canh-XX.md, film/cXX/XX-YY.txt và film/shots.json từ data.py.
Chạy: python3 _tools/build.py  (đứng ở đâu cũng được).
Khuôn lấy từ cuon-sach-trao-tay/_tools/build.py, viết lại cho chung: bộ gốc/bộ sửa, hồi tưởng và tiếng theo bối cảnh."""
import json, math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import TITLE, PEOPLE, OUTFITS, PLACES, PLACE_FLASH, PLACE_SOUND, LOOK, AVOID, AGE_EDIT, S

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYL_PER_S = 4.2          # tiếng Việt: ~4,2 âm tiết/giây khi nói chậm rõ
MAX_SECS = 15            # Omni tạo tối đa 15 giây một lần


def tag(p):
    return "@" + p


def full_prompt(code):
    person, flow, outfit, *_ = OUTFITS[code]
    P = PEOPLE[person]
    return (f"Full-body photorealistic character reference of {P['face']}, wearing {outfit}; standing relaxed, face clearly visible; "
            "plain light-grey studio background, soft even daylight, natural skin texture with pores and fine wrinkles, realistic proportions, 8K. "
            "Fictional adult, not resembling any real person. No text, no logo.")


def base_of(code):
    b = OUTFITS[code][5]
    return None if b is True else b


def edit_prompt(code):
    person, flow, outfit, *_ = OUTFITS[code]
    if code in AGE_EDIT:
        return AGE_EDIT[code].format(face=PEOPLE[person]["face"], outfit=outfit)
    return f"Same person, same face and hair, exactly. Now wearing {outfit}. Full body, plain light-grey studio background."


def timeline(lines):
    t = 0.3
    out = []
    for who, text, tone in lines:
        n = len(text.replace("…", " ").split())
        d = max(0.8, n / SYL_PER_S)
        out.append((round(t, 1), round(t + d, 1), who, text, tone))
        t += d + 0.45
    return out


def shot_secs(minimum, tl):
    if not tl:
        return max(4, minimum)
    return min(MAX_SECS, max(minimum, 4, math.ceil(tl[-1][1] + 2.2)))


def char_line(code):
    if code in OUTFITS:
        person, flow, outfit, *_ = OUTFITS[code]
        P = PEOPLE[person]
        return f"- {tag(person)} = {P['name']}, {P['role']} ({P['face']}); wears {outfit}. Attached image: \"{flow}\"."
    P = PEOPLE[code]
    return f"- {tag(code)} = {P['name']}, {P['role']} ({P['face']}); wears {P['outfit_text']}. No attached image."


def place_of(sc, sh):
    extra = sh[6]
    return extra if extra in PLACES else sc["place"]


def prompt_for(sc, sh, secs, tl):
    name, _, codes, cam, action, lines, extra = sh
    place = place_of(sc, sh)
    flash = PLACE_FLASH.get(place, "")
    look = LOOK + (" " + flash if flash else "")
    sound = PLACE_SOUND[place] if (place != sc["place"] and place in PLACE_SOUND) else sc["sound"]
    parts = [f"A single continuous {secs}-second shot, 16:9, one camera angle, no cuts.", "",
             f"[LOOK] {look}", "", f"[PLACE] {PLACES[place]}", ""]
    if codes:
        parts.append("[CHARACTERS] Use the attached character image for each person: same face, same hair, same outfit, exactly.")
        parts += [char_line(c) for c in codes]
        parts.append("Each named person appears exactly once. Background people stay distant, blurred and clearly different from them.")
    else:
        parts.append("[CHARACTERS] No named characters in this shot. Any people stay distant, blurred and anonymous.")
    parts += ["", f"[CAMERA] {cam}.", "", f"[ACTION] {action}", ""]
    if tl:
        parts.append("[DIALOGUE] In Vietnamese with exact lip-sync, standard Northern Vietnamese accent; each line spoken exactly once, on camera; only the speaker moves the lips:")
        for a, b, who, text, tone in tl:
            P = PEOPLE[who]
            parts.append(f"- {a}s–{b}s, {tag(who)} ({P['voice']}, {tone}): {text}")
        parts.append(f"After the last word nobody speaks until {secs}.0s. Never read these directions aloud.")
    else:
        parts.append("[DIALOGUE] None. Nobody speaks in this shot.")
    parts += ["", f"[SOUND] {sound}", "", f"[AVOID] {AVOID}"]
    return "\n".join(parts) + "\n"


def check():
    """Bắt lỗi dữ liệu trước khi sinh file."""
    errs = []
    for sc in S:
        for i, sh in enumerate(sc["shots"], 1):
            sid = f"{sc['num']}-{i:02d}"
            if len(sh) != 7:
                errs.append(f"{sid}: shot phải có 7 phần tử"); continue
            name, mins, codes, cam, action, lines, extra = sh
            for c in codes:
                if c not in OUTFITS and not (c in PEOPLE and PEOPLE[c].get("text_only")):
                    errs.append(f"{sid}: mã '{c}' không có trong OUTFITS")
            if len([c for c in codes if c in OUTFITS]) > 2:
                errs.append(f"{sid}: quá 2 nhân vật gắn ảnh")
            if extra and extra not in PLACES and not extra.startswith("EXIST:"):
                errs.append(f"{sid}: bối cảnh '{extra}' không có")
            in_frame = {OUTFITS[c][0] if c in OUTFITS else c for c in codes}
            for who, text, tone in lines:
                if who not in PEOPLE:
                    errs.append(f"{sid}: người nói '{who}' không có")
                elif who not in in_frame:
                    errs.append(f"{sid}: {who} nói nhưng không có trong khung")
            tl = timeline(lines)
            if tl and tl[-1][1] + 1.0 > MAX_SECS:
                errs.append(f"{sid}: thoại quá dài cho {MAX_SECS}s")
    if errs:
        print("\n".join(errs)); sys.exit(1)


def main():
    check()
    manifest = []; total = 0; gen_total = 0
    os.makedirs(os.path.join(ROOT, "kich-ban"), exist_ok=True)
    shots_md = [f"# {TITLE} — bảng shot", "",
                "*Sinh bởi `_tools/build.py` từ `_tools/data.py`. Sửa dữ liệu rồi chạy lại.* Flow: Omni 1.2 Flash, 16:9, 720p, x1. Tên video trên Flow: `<shot> · <tên>`.", ""]
    index = ["| Cảnh | Tên | Hồi | Thời điểm | Shot | Giây |", "|---|---|---|---|---|---|"]
    for sc in S:
        d = os.path.join(ROOT, "film", "c" + sc["num"]); os.makedirs(d, exist_ok=True)
        rows = []; sc_secs = 0
        for i, sh in enumerate(sc["shots"], 1):
            sid = f"{sc['num']}-{i:02d}"
            name, mins, codes, cam, action, lines, extra = sh
            tl = timeline(lines); secs = shot_secs(mins, tl)
            fpath = os.path.join(d, f"{sid}.txt")
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(prompt_for(sc, sh, secs, tl))
            attach = ", ".join(OUTFITS[c][1] for c in codes if c in OUTFITS) or "Text-to-Video"
            gen_total += secs; sc_secs += secs
            dia = " / ".join(f"{PEOPLE[w]['name']}: {t}" for w, t, _ in lines)
            rows.append(f"| {sid} | {name} | {secs} | {attach} | {dia} |")
            manifest.append(dict(id=sid, scene=sc["num"], name=name, secs=secs, place=place_of(sc, sh),
                                 attach=[OUTFITS[c][1] for c in codes if c in OUTFITS],
                                 prompt=os.path.relpath(fpath, ROOT), output=f"film/clips/{sid}.mp4"))
        total += sc_secs
        hdr = f"## Cảnh {sc['num']} · {sc['title']} · {sc['when']}"
        tbl = ["| Shot | Tên | Giây | Đính trên Flow | Thoại |", "|---|---|---|---|---|"] + rows
        shots_md += [hdr, ""] + tbl + [""]
        index.append(f"| [{sc['num']}](canh-{sc['num']}.md) | {sc['title']} | {sc['act']} | {sc['when']} | {len(sc['shots'])} | {sc_secs} |")
        outfits = sorted({c for sh in sc["shots"] for c in sh[2] if c in OUTFITS})
        with open(os.path.join(ROOT, "kich-ban", f"canh-{sc['num']}.md"), "w", encoding="utf-8") as f:
            f.write("\n".join([f"# Cảnh {sc['num']} · {sc['title']}", "",
                               f"**{sc['act']}** · {sc['when']} · ~{sc_secs} giây · {len(sc['shots'])} shot", "",
                               "## Nhân vật & bộ đồ (tên trên Flow)", ""] + [f"- {OUTFITS[c][1]}" for c in outfits] +
                              ["", "## Bảng shot", ""] + tbl +
                              ["", f"Prompt Flow từng shot: `film/c{sc['num']}/`. Clip đã tải: `film/clips/{sc['num']}-*.mp4`.", ""]))
    shots_md.insert(4, f"**{len(manifest)} shot · {total // 60} phút {total % 60} giây chưa tính thẻ chữ · {gen_total} giây cần tạo trên Flow.**\n")
    with open(os.path.join(ROOT, "SHOTS.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(shots_md))
    with open(os.path.join(ROOT, "film", "shots.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)
    with open(os.path.join(ROOT, "kich-ban", "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join([f"# {TITLE} — Kịch bản từng cảnh", "",
                           f"*Sinh bởi `_tools/build.py`.* **{len(S)} cảnh · {len(manifest)} shot · ~{total // 60} phút {total % 60} giây, chưa tính thẻ chữ.**", ""] + index) + "\n")
    # NHAN_VAT_FLOW.md
    nv = [f"# {TITLE} — Nhân vật theo bộ đồ trên Flow", "",
          "*Sinh bởi `_tools/build.py`.* Mỗi bộ đồ là **một nhân vật riêng trên Flow**, đặt đúng tên ở cột *Tên trên Flow*. "
          "Tạo bộ gốc (★) bằng prompt đầy đủ; các bộ còn lại đính ảnh bộ ở cột *Gốc từ* rồi dùng *Prompt sửa* "
          "(nếu sửa ra lệch mặt thì dùng *Prompt đầy đủ*).", "",
          "## Khóa mặt và giọng", "", "| Tag | Nhân vật | Khuôn mặt | Giọng |", "|---|---|---|---|"]
    for k, P in PEOPLE.items():
        nv.append(f"| `@{k}` | {P['name']}{' *(không gắn ảnh)*' if P.get('text_only') else ''} | {P['face']} | {P['voice']} |")
    nv += ["", f"## {len(OUTFITS)} nhân vật theo bộ đồ", "",
           "| Mã | Tên trên Flow | Cảnh dùng | Ghi chú | Gốc từ | Prompt sửa | Prompt đầy đủ |", "|---|---|---|---|---|---|---|"]
    for c, (person, flow, outfit, scenes, note, base) in OUTFITS.items():
        b = base_of(c)
        nv.append(f"| {c}{' ★' if b is None else ''} | {flow} | {scenes} | {note} | {OUTFITS[b][1] if b else '—'} | "
                  f"{edit_prompt(c) if b else '—'} | {full_prompt(c)} |")
    with open(os.path.join(ROOT, "NHAN_VAT_FLOW.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(nv) + "\n")
    print(f"{len(S)} cảnh, {len(manifest)} shot, {total // 60}:{total % 60:02d} phim, {gen_total}s cần tạo (~{gen_total * 4} credit)")


if __name__ == "__main__":
    main()
