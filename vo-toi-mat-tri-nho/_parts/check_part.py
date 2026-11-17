#!/usr/bin/env python3
"""Validate one fragment of Cái Kết Cho Tiểu Tam scenes before merging.

    python3 cai-ket-cho-tieu-tam/_parts/check_part.py cai-ket-cho-tieu-tam/_parts/part1.json
    python3 cai-ket-cho-tieu-tam/_parts/check_part.py cai-ket-cho-tieu-tam/_parts/part1.json --plan   # + speech windows

A fragment is a JSON list of scene objects. It is checked together with
_parts/header.json using the compiler's own validator, plus action-film rules.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "flowkit", "scripts"))
import build_omni_horror_prompts as B  # noqa: E402

EXTRA_RISKY = [
    r"\bcrash", r"\bsmash", r"\bhit(s|ting)?\b", r"\brams?\b", r"\bramm", r"\bshoot", r"\bshot at (him|her|them)\b", r"\bexplo",
    r"\bfist", r"\bbrawl", r"\bwrestl", r"\bshov", r"\bpush(es|ed|ing)?\b(?!-in)", r"\btackl", r"\bhostage", r"\btied\b",
    r"\brope around", r"\bgag", r"\bbound\b", r"\bdrag(?!on)", r"\bthreaten", r"\bpolice tape",
    # romance drama: keep intimacy tasteful, keep confrontations contact-free
    r"\bkiss", r"\bin bed\b", r"\bundress", r"\bnaked", r"\bnude\b", r"\blingerie", r"\bseduct", r"\bcleavage",
    r"\bshirtless", r"\bbikini", r"\bsensual", r"\bhair-pull", r"\bpulls? (her|his) hair", r"\bsplash(es|ed)? (water|coffee|a drink) (at|on|in)",
    r"\btrips? her\b", r"\bfalls? down the stairs", r"\btumbl",
]

# Giọng Bắc thanh thoát (07/11/2026): từ miền Nam không lẫn được với từ Bắc.
SOUTHERN_WORDS = re.compile(r"(?<!\w)(nè|nghen|hông|hổng|thiệt|tui|tụi|muỗng|heo|lượm|rớt|ổng|vầy|dzậy)(?!\w)", re.I)

# Tự nhiên (10/11/2026): lời lặp giữa hai clip liền nhau, cụm từ lặp trong phần, nhân vật tự gọi tên mình.
STOPWORDS = set("anh em chị mẹ con bố ba má ông bà cô cậu cháu tôi mình nó thì là mà có không đã đi cho của với này đấy ạ à ơi rồi cũng lại được những một hai các thế nào gì vào ra lên xuống đây kia ấy ai sao vẫn còn phải người nhà nhé chứ đâu biết làm".split())


def content_ngrams(text: str, n: int) -> set[str]:
    w = re.findall(r"[\wÀ-ỹ]+", text.lower())
    return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1) if not all(x in STOPWORDS for x in w[i:i + n])}


def own_names(name: str) -> set[str]:
    return {w for w in re.findall(r"[A-ZÀ-ỸĐ][\wÀ-ỹ]*", name) if w not in ("Ông", "Bà", "Bé", "Cô", "Anh", "Chị")}


def main() -> int:
    path = sys.argv[1]
    header = json.load(open(os.path.join(HERE, "header.json"), encoding="utf-8"))
    scenes = json.load(open(path, encoding="utf-8"))
    header["scenes"] = scenes
    errors, warns = B.validate(header)
    chars = header["characters"]
    D = B.clip_seconds(header)
    want = {10: 6, 15: 4}[D]  # 60s per scene: 6 × 10s (Omni 1.1) or 4 × 15s (Omni 1.2, 09/11/2026)
    for sc in scenes:
        if len(sc["clips"]) != want:
            errors.append(f"scene {sc['num']}: needs {want} clips")
        for k in ("num", "title", "time_label", "location", "axis", "props", "setting", "clips"):
            if k not in sc:
                errors.append(f"scene {sc.get('num')}: missing {k}")
        for i, c in enumerate(sc["clips"]):
            cid = c["id"]
            if cid != f"{sc['num']:02d}.{i + 1}":
                errors.append(f"{cid}: id should be {sc['num']:02d}.{i + 1}")
            if not c.get("steps"):  # user 10/11/2026: clip 15 s = nhiều cảnh quay, mỗi giây một bước
                errors.append(f"{cid}: needs \"shots\" (3–5) and \"steps\" (one per second)")
            visual = " ".join(B.visual_lines(c) + B.cameras(c) + [c.get("setting", sc["setting"]), c.get("extras", "")])
            for pat in EXTRA_RISKY:
                m = re.search(pat, visual, re.I)
                if m:
                    warns.append(f"{cid}: risky action word '{m.group(0)}'")
            cont = B.effective_continuity(sc["clips"], i, sc["setting"])
            if B.is_vo(c):  # NO_NARRATOR: user 08/11 (cai-ket), 10/11 (gang) — 100% lời thoại do nhân vật nói trên hình
                errors.append(f"{cid}: narrator clip — every line must be spoken on camera by a character")
                continue
            for t in B.turns(c):  # nhịp giọng theo cảnh (10/11/2026): lượt nào cũng có pace
                if t.get("pace") not in B.PACES:
                    errors.append(f"{cid}: turn by {t['speaker']} needs \"pace\": fast / normal / slow")
                m = SOUTHERN_WORDS.search(t["line"])
                if m:
                    warns.append(f"{cid}: Southern word '{m.group(0)}' in a Hà Nội line")
            if not all(t["speaker"] in chars for t in B.turns(c)):
                continue
            if c.get("continuity") == "continuous" and cont != "continuous":
                warns.append(f"{cid}: marked continuous but compiles as cut (newcomer / setting change)")
            if not B.is_vo(c) and cont == "cut":
                b = B.speech_plan(header, c, cont, D, clamp=False)[-1][3]
                if b > D - 0.8:
                    errors.append(f"{cid}: lip-sync on a cut clip ends at {b:.1f}s (>{D - 0.8:.1f}s) — shorten the line(s)")
    if "--plan" in sys.argv:  # khung thoại từng lượt để căn độ dài câu theo nhịp
        for sc in scenes:
            for i, c in enumerate(sc["clips"]):
                if B.is_vo(c) or not all(t["speaker"] in chars and t.get("pace") in B.PACES for t in B.turns(c)):
                    continue
                cont = B.effective_continuity(sc["clips"], i, sc["setting"])
                plan = B.speech_plan(header, c, cont, D, clamp=False)
                print(f"PLAN  {c['id']} {cont:10s} " + " | ".join(
                    f"{sp} {t['pace']} {B.syllables(ln)} syl {a:.1f}-{b:.1f}s" for (sp, ln, a, b), t in zip(plan, B.turns(c))))
    for w in list(warns):  # clip thiếu lời → Omni nói lại câu cho kín clip (bản render 10/11/2026)
        if "repeats lines" in w:
            warns.remove(w)
            errors.append(w)
    all_clips = [c for sc in scenes for c in sc["clips"]]
    said = lambda c: " ".join(t["line"] for t in B.turns(c))
    for a, b in zip(all_clips, all_clips[1:]):
        common = content_ngrams(said(a), 2) & content_ngrams(said(b), 2)
        if common:
            warns.append(f"{b['id']}: repeats words of {a['id']} {sorted(common)} — each clip should move the story on")
    counts: dict[str, list[str]] = {}
    for c in all_clips:
        for g in content_ngrams(said(c), 3):
            counts.setdefault(g, []).append(c["id"])
    for g, ids in sorted(counts.items()):
        if len(ids) >= 3:
            warns.append(f"phrase '{g}' used {len(ids)} times ({' '.join(ids)}) — vary it")
    for c in all_clips:
        for t in B.turns(c):
            if t["speaker"] in chars:
                hit = {n for n in own_names(chars[t["speaker"]].get("name", "")) if re.search(rf"(?<![\wÀ-ỹ]){n}(?![\wÀ-ỹ])", t["line"])}
                if hit:
                    warns.append(f"{c['id']}: {t['speaker']} says own name {sorted(hit)} — people say tôi/em/anh/ông, not their own name")
    for w in warns:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    n = sum(len(s["clips"]) for s in scenes)
    print(f"{len(scenes)} scenes, {n} clips, {len(errors)} errors, {len(warns)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
