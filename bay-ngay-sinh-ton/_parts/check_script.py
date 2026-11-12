#!/usr/bin/env python3
"""Check the hand-written outline _parts/DAN_Y.md (English dialogue, 15 s Omni clips).

- words per clip: target 32-37 (provisional, re-measure with Whisper after test renders)
- speakers in LIPSYNC:... match the turn lines, at most 3 turns
- pace is nhanh / vừa / chậm
- nobody says their own name
- estimated speech end (0.4 s start, 0.3 s between turns) stays under 14.4 s

Usage: python3 bay-ngay-sinh-ton/_parts/check_script.py [--fix]
--fix rewrites the `NN từ` field of each clip header with the counted value.
"""
import re
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "DAN_Y.md"
WORDS_MIN, WORDS_MAX = 32, 37
# words per second by pace: a guess for Omni English (~2.8 w/s). Omni mostly ignores pace labels
# (Whisper, 10/11), so the spread is kept narrow; re-measure after the first renders.
WPS = {"nhanh": 3.2, "vừa": 2.8, "chậm": 2.4}
SPEECH_START, TURN_GAP, SPEECH_END_MAX = 0.4, 0.3, 14.4
NAMES = {"Khang": "Khang", "Bin": "Bin", "Stream": "Stream", "Moon": "Moon", "Roar": "Roar", "Snail": "Snail"}

CLIP_RE = re.compile(r"^- \*\*Clip (\d\d\.\d)\*\* · `LIPSYNC:([^`]+)` · `(\S+) từ`")
TURN_RE = re.compile(r"^  - \*\*@(\w+)\*\* \(([^,)]+)[^)]*\): (.+)$")


def count_words(text):
    n = 0
    for tok in re.split(r"[\s\-–—]+", text):
        tok = tok.strip(".,!?;:…'\"()")
        if not tok:
            continue
        if re.fullmatch(r"(?:[a-z]\.){2,}", tok + "." if not tok.endswith(".") else tok):
            n += tok.count(".") or 2  # p.m. -> "pee em"
        else:
            n += 1
    return n


def main():
    fix = "--fix" in sys.argv
    lines = SCRIPT.read_text(encoding="utf-8").splitlines()
    clips = []
    for i, line in enumerate(lines):
        m = CLIP_RE.match(line)
        if m:
            clips.append({"id": m.group(1), "line": i, "speakers": m.group(2).split("+"), "turns": []})
            continue
        t = TURN_RE.match(line)
        if t and clips:
            clips[-1]["turns"].append((t.group(1), t.group(2).strip(), t.group(3)))

    errors = warnings = 0
    total_words = 0
    for c in clips:
        cid, turns = c["id"], c["turns"]
        words = sum(count_words(text) for _, _, text in turns)
        total_words += words
        problems = []
        if [s.lstrip("@") for s in c["speakers"]] != [s for s, _, _ in turns]:
            problems.append(("ERROR", f"LIPSYNC {'+'.join(c['speakers'])} != turns {[s for s, _, _ in turns]}"))
        for (a, pa, _), (b, pb, _) in zip(turns, turns[1:]):
            if a == b and pa == pb:
                problems.append(("ERROR", f"@{a} has two turns in a row at the same pace — merge them"))
        if len(turns) > 3:
            problems.append(("ERROR", f"{len(turns)} turns (max 3)"))
        if not WORDS_MIN <= words <= WORDS_MAX:
            problems.append(("ERROR", f"{words} words (target {WORDS_MIN}-{WORDS_MAX})"))
        end = SPEECH_START
        for k, (spk, pace, text) in enumerate(turns):
            if pace not in WPS:
                problems.append(("ERROR", f"turn {k + 1}: pace '{pace}'"))
                continue
            end += count_words(text) / WPS[pace] + (TURN_GAP if k else 0)
            name = NAMES.get(spk)
            if name and re.search(rf"\b{name}\b", text):
                problems.append(("ERROR", f"turn {k + 1}: @{spk} says own name"))
        if end > SPEECH_END_MAX:
            problems.append(("WARN", f"estimated speech ends at {end:.1f}s"))
        for level, msg in problems:
            print(f"{level} {cid}: {msg}")
            if level == "ERROR":
                errors += 1
            else:
                warnings += 1
        if fix:
            lines[c["line"]] = re.sub(r"`\S+ từ`", f"`{words} từ`", lines[c["line"]])

    paces = [p for c in clips for _, p, _ in c["turns"]]
    print(f"{len(clips)} clips, {total_words} words, "
          f"pace nhanh {paces.count('nhanh')} / vừa {paces.count('vừa')} / chậm {paces.count('chậm')}, "
          f"{errors} errors, {warnings} warnings")
    if fix:
        SCRIPT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
