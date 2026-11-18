#!/usr/bin/env python3
"""Nén prompt flow_15s thành dạng ngắn để dán qua trình duyệt: các khối lặp lại thay bằng mã ⟦k⟧, kèm checksum."""
import glob, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); SDIR = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import build_15s as B
from looks import LOOKS, PLACE

D = {"S": B.STYLE, "A": B.AVOID,
     "K": "Keep every face, hairstyle and outfit exactly consistent. Attached reference images show faces and clothes only — never copy their backgrounds, and never flash the studio reference portrait; the characters are already in place in the very first frame.",
     "W": "- Whoever is speaking has the face clearly on screen in that shot; the camera keeps one side of the line so eyelines match across the cuts.",
     "E": "Emotion shows through physical cues (breathing, eyes, jaw, hands, posture); one clear action per beat.",
     "T": "- Throughout, only the person whose turn it is moves the lips while anyone else listens with the mouth closed; real breaths and tiny natural hesitations, recorded close on set with a little room tone — it sounds like real actors talking, never like a voice-over or text-to-speech.",
     "V": "- Voices: every character speaks standard Hà Nội Northern Vietnamese (never Southern or Central accents), says each word once and clearly, and different characters sound clearly different in pitch, age and texture.",
     "Q": "- Speak only the Vietnamese words inside the double quotes, once, with natural Northern Vietnamese tones; never read these directions, names or tags aloud.",
     "H": "16:9 widescreen, 24 fps, with hard cuts only at "}
for code, (w, _, _) in LOOKS.items():
    D["c" + code] = B.char_line(w, code)
for l, (_, desc) in PLACE.items():
    D["p" + l] = desc
for w, v in B.VOICE.items():
    D["v" + w] = v
for k, (_, d) in B.PACE.items():
    D["s" + k] = d
order = sorted(D, key=lambda k: -len(D[k]))

def h(s):
    x = 0
    for ch in s:
        x = (x * 31 + ord(ch)) & 0xFFFFFFFF
    return x

def pack(txt):
    for k in order:
        txt = txt.replace(D[k], "⟦" + k + "⟧")
    return txt

if __name__ == "__main__":
    if sys.argv[1:2] == ["dict"]:
        print(json.dumps(D, ensure_ascii=False))
    else:
        for f in sys.argv[1:]:
            t = open(f, encoding="utf-8").read()
            print(json.dumps({"id": os.path.basename(f)[:-4], "n": len(t), "h": h(t), "p": pack(t)}, ensure_ascii=False))
