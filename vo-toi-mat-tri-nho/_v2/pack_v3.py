#!/usr/bin/env python3
"""Nén prompt flow_v3 để dán qua trình duyệt. python3 _v2/pack_v3.py dict | python3 _v2/pack_v3.py 01-01 01-02 ..."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); SDIR = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import build_v3 as B
from looks import LOOKS, PLACE, FACE, NAME, ROLE, VOICE
D = {"L": B.LOOK, "A": B.AVOID,
     "C": "[CHARACTERS] Use the attached character image for each person: same face, same hair, same outfit, exactly; only face and clothes come from it, never its background.",
     "N": "[CHARACTERS] No named characters; any people in frame are distant, blurred and unidentifiable.",
     "X": "Voice: standard Hà Nội Northern Vietnamese with natural Northern tones (never Southern or Central accents); a real actor recorded close on set with a little room tone, real breaths and tiny natural hesitations — never a voice-over or text-to-speech. Speak only the Vietnamese words inside the double quotes, once; never read these directions, names or tags aloud.",
     "Z": "[DIALOGUE] None. Every mouth stays closed; no voices at all.",
     "I": "In Vietnamese with exact lip-sync, spoken on camera by "}
for loc in B.SET_NAME:
    p = PLACE[loc][1]
    D["p" + loc] = f"[PLACE] {p[0].upper() + p[1:]}. The attached image \"{B.SET_NAME[loc]}\" shows this exact set: match its architecture, furniture, colours and light, seen from this shot's camera angle; never show the reference image itself."
    D["s" + loc] = f"[SOUND] {B.SFX[loc]}. No music."
for code, (w, flow, outfit) in LOOKS.items():
    D["c" + code] = f"- @{w} = {NAME[w]}, {ROLE[w]}: {FACE[w]}; wears {outfit}. Attached image: \"{flow}{B.SUFFIX}\"."
for w, v in VOICE.items():
    D["v" + w] = v
order = sorted(D, key=lambda k: -len(D[k]))
def h(s):
    x = 0
    for ch in s: x = (x * 31 + ord(ch)) & 0xFFFFFFFF
    return x
if sys.argv[1] == "dict":
    used = set()
    for f in sorted(os.listdir(os.path.join(SDIR, "flow_v3"))):
        pass
    print(json.dumps(D, ensure_ascii=False))
else:
    man = {m["id"]: m for m in json.load(open(os.path.join(SDIR, "flow_v3", "manifest.json"), encoding="utf-8"))}
    for sid in sys.argv[1:]:
        t = open(os.path.join(SDIR, "flow_v3", "p" + sid[:2], sid + ".txt"), encoding="utf-8").read()
        p = t
        for k in order: p = p.replace(D[k], "⟦" + k + "⟧")
        print(json.dumps([sid, man[sid]["dur"], man[sid]["ingredients"], len(t), h(t), p], ensure_ascii=False))
