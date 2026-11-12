#!/usr/bin/env python3
"""Validate one filled part (_parts/part_pK.json) with the real builder rules.

    python3 bay-ngay-sinh-ton/_parts/check_part.py 1        # checks part_p1.json against skeleton_p1.json

Errors block the build; warnings should be fixed unless there is a reason (e.g. extras in a crowd scene).
Extra checks: turns, chars, setting and wardrobe must stay exactly as in the skeleton; every turn has an
English tone; every clip has sfx.
"""
import copy
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
spec = importlib.util.spec_from_file_location("builder", REPO / "flowkit/scripts/build_omni_horror_prompts.py")
B = importlib.util.module_from_spec(spec)
spec.loader.exec_module(B)


def main():
    k = sys.argv[1]
    header = json.load(open(HERE / "header.json", encoding="utf-8"))
    skel = json.load(open(HERE / f"skeleton_p{k}.json", encoding="utf-8"))
    part = json.load(open(HERE / f"part_p{k}.json", encoding="utf-8"))
    errors, warns = [], []

    sk_clips = {c["id"]: (sc, c) for sc in skel for c in sc["clips"]}
    seen = set()
    for sc in part:
        for c in sc["clips"]:
            cid = c["id"]
            seen.add(cid)
            if cid not in sk_clips:
                errors.append(f"{cid}: not in skeleton")
                continue
            ssc, sk = sk_clips[cid]
            for key in ("setting", "wardrobe"):
                if c.get(key) != sk.get(key):
                    errors.append(f"{cid}: {key} differs from the skeleton (keep it verbatim)")
            if sc.get("setting") != ssc.get("setting"):
                errors.append(f"scene {sc['num']}: scene setting differs from the skeleton")
            if c.get("chars") != sk["chars"]:
                errors.append(f"{cid}: chars {c.get('chars')} != skeleton {sk['chars']}")
            got = [(t["speaker"], t["line"], t["pace"]) for t in c.get("turns", [])]
            want = [(t["speaker"], t["line"], t["pace"]) for t in sk["turns"]]
            if got != want:
                errors.append(f"{cid}: turns (speaker/line/pace) changed — copy them verbatim from the skeleton")
            for t in c.get("turns", []):
                tone = t.get("tone", "")
                if not tone or not tone.isascii():
                    errors.append(f"{cid}: turn by {t['speaker']} needs a short English tone")
            if not c.get("sfx"):
                errors.append(f"{cid}: missing sfx")
            for key in ("steps", "shots", "continuity"):
                if key not in c:
                    errors.append(f"{cid}: missing {key}")
    missing = set(sk_clips) - seen
    if missing:
        errors.append(f"missing clips: {sorted(missing)}")

    data = copy.deepcopy(header)
    data["scenes"] = copy.deepcopy(part)
    if not errors:
        e, w = B.validate(data)
        # Monologue clips (03.x–05.x, 06.2, 07.4, 23.2) still have one speaker's turns in a row;
        # they are merged into one turn at the final merge, so this error is deferred here.
        deferred = [x for x in e if "two turns in a row by the same speaker" in x]
        for x in deferred:
            print("NOTE ", x, "(deferred: merged at final merge)")
        errors += [x for x in e if x not in deferred]
        warns += w
        if not e:
            for sc in data["scenes"]:
                for i, c in enumerate(sc["clips"]):
                    B.render_prompt(data, sc, c, B.effective_continuity(sc["clips"], i, sc["setting"]))
    for w in warns:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"part {k}: {len(seen)} clips, {len(errors)} errors, {len(warns)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
