#!/usr/bin/env python3
"""Merge header.json + part_p1..4.json into ../PHAN_CANH_OMNI.json.

The skeleton (rebuilt from DAN_Y.md by make_skeleton.py) is authoritative for dialogue, chars,
settings, wardrobe and intercut; the parts contribute tones, sfx, shots, steps, extras, axis, props.
When DAN_Y merged two turns of one speaker, their tones are joined. Underscore keys are dropped.
The synced parts are written back so check_part.py keeps passing.

    python3 bay-ngay-sinh-ton/_parts/make_skeleton.py
    python3 bay-ngay-sinh-ton/_parts/merge.py
    python3 flowkit/scripts/build_omni_horror_prompts.py bay-ngay-sinh-ton
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SYNC_KEYS = ("chars", "setting", "wardrobe", "intercut")


def clean(obj):
    if isinstance(obj, dict):
        return {k: clean(v) for k, v in obj.items() if not k.startswith("_")}
    if isinstance(obj, list):
        return [clean(v) for v in obj]
    return obj


def sync_turns(cid: str, sk_turns: list[dict], part_turns: list[dict]) -> list[dict]:
    """Skeleton turns with tones taken from the part; part turns are grouped onto merged skeleton turns."""
    if len(sk_turns) == len(part_turns):  # same shape: lines may have been edited in DAN_Y, tones stay
        return [{**{k: v for k, v in st.items() if not k.startswith("_")}, "tone": pt.get("tone", "")}
                for st, pt in zip(sk_turns, part_turns)]
    out, i = [], 0
    for st in sk_turns:
        group, text = [], ""
        while i < len(part_turns) and part_turns[i]["speaker"] == st["speaker"] and len(text) < len(st["line"]):
            group.append(part_turns[i])
            text = (text + " " + part_turns[i]["line"]).strip()
            i += 1
        if text != st["line"]:
            raise SystemExit(f"{cid}: part turns do not add up to skeleton line: {st['line']!r}")
        tones = list(dict.fromkeys(t["tone"] for t in group if t.get("tone")))
        out.append({**{k: v for k, v in st.items() if not k.startswith("_")}, "tone": ", then ".join(tones)})
    return out


def main():
    data = json.load(open(HERE / "header.json", encoding="utf-8"))
    for k in range(1, 5):
        skel = {sc["num"]: sc for sc in json.load(open(HERE / f"skeleton_p{k}.json", encoding="utf-8"))}
        part = json.load(open(HERE / f"part_p{k}.json", encoding="utf-8"))
        for sc in part:
            ssc = skel[sc["num"]]
            sc["setting"] = ssc["setting"]
            sk_clips = {c["id"]: c for c in ssc["clips"]}
            for c in sc["clips"]:
                sk = sk_clips[c["id"]]
                c["turns"] = sync_turns(c["id"], sk["turns"], c["turns"])
                for key in SYNC_KEYS:
                    if key in sk:
                        c[key] = sk[key]
                    else:
                        c.pop(key, None)
        with open(HERE / f"part_p{k}.json", "w", encoding="utf-8") as f:
            json.dump(part, f, ensure_ascii=False, indent=1)
        data["scenes"] += clean(part)
    nums = [sc["num"] for sc in data["scenes"]]
    assert nums == list(range(1, 25)), nums
    with open(HERE.parent / "PHAN_CANH_OMNI.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"PHAN_CANH_OMNI.json: {len(data['scenes'])} scenes, {sum(len(s['clips']) for s in data['scenes'])} clips")


if __name__ == "__main__":
    main()
