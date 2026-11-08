#!/usr/bin/env python3
"""Validate one fragment of Găng Tơ Tái Xuất scenes before merging.

    python3 gang-to-tai-xuat/_parts/check_part.py gang-to-tai-xuat/_parts/part1.json

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
    r"\brope around", r"\bgag", r"\bbound\b", r"\bdrag(?!on)", r"\bthreaten", r"\bfire extinguisher at\b", r"\bpolice tape",
]


def main() -> int:
    path = sys.argv[1]
    header = json.load(open(os.path.join(HERE, "header.json"), encoding="utf-8"))
    scenes = json.load(open(path, encoding="utf-8"))
    header["scenes"] = scenes
    errors, warns = B.validate(header)
    chars = header["characters"]
    for sc in scenes:
        if len(sc["clips"]) != 6:
            errors.append(f"scene {sc['num']}: needs 6 clips")
        for k in ("num", "title", "time_label", "location", "axis", "props", "setting", "clips"):
            if k not in sc:
                errors.append(f"scene {sc.get('num')}: missing {k}")
        for i, c in enumerate(sc["clips"]):
            cid = c["id"]
            if cid != f"{sc['num']:02d}.{i + 1}":
                errors.append(f"{cid}: id should be {sc['num']:02d}.{i + 1}")
            visual = " ".join(c["beats"] + [c["camera"], c.get("setting", sc["setting"]), c.get("extras", "")])
            for pat in EXTRA_RISKY:
                m = re.search(pat, visual, re.I)
                if m:
                    warns.append(f"{cid}: risky action word '{m.group(0)}'")
            cont = B.effective_continuity(sc["clips"], i, sc["setting"])
            if c.get("continuity") == "continuous" and cont != "continuous":
                warns.append(f"{cid}: marked continuous but compiles as cut (newcomer / setting change)")
            if c["speaker"] != "NARRATOR" and cont == "cut":
                a, b = B.speech_window(c["line"], chars[c["speaker"]]["rate"], start=3.0, max_end=99)
                if b > 9.2:
                    errors.append(f"{cid}: lip-sync on a cut clip ends at {b:.1f}s (>9.2s) — shorten to ≤22 syllables")
    for w in warns:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    n = sum(len(s["clips"]) for s in scenes)
    print(f"{len(scenes)} scenes, {n} clips, {len(errors)} errors, {len(warns)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
