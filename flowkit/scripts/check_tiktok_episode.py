#!/usr/bin/env python3
"""Check one TikTok episode folder against flowkit/docs/TIKTOK_PROMPT_SPEC.md.

Usage: python3 flowkit/scripts/check_tiktok_episode.py <episode dir>   (exit 0 = all clips OK)
"""
import glob, os, re, sys

VI = re.compile(r"[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ]", re.I)
SEG = re.compile(r"^\s*(\d{2}):(\d{2}(?:\.\d+)?)\s*[–-]\s*(\d{2}):(\d{2}(?:\.\d+)?)\s*\|(.*)$")
SAY = re.compile(r"(@?[\wÀ-ỹ][\wÀ-ỹ ]{0,30}?) says \((.*?)\):\s*(.+?)$")
CLOCK = re.compile(r"\b\d{1,2}[:h]\d{2}\s?(AM|PM|am|pm|sáng|chiều|tối)\b|\b\d{1,2}\s?(AM|PM)\b|Time:\s*\d|\b(?!9:16\b|16:9\b)\d{1,2}:\d{2}\b(?![–-]\d)")
SAY_HEAD = re.compile(r"(@?[\wÀ-ỹ][\wÀ-ỹ ]{0,30}?) says \((.*?)\):\s*")
TAG = re.compile(r"@[A-Za-zÀ-ỹĐđ][\wÀ-ỹĐđ]*")


def syl(t):
    return len([w for w in re.split(r"\s+", re.sub(r"[^\wÀ-ỹ\s]", " ", t)) if w])


EN_WORDS = {"the", "a", "an", "his", "her", "their", "and", "as", "while", "with", "to", "of", "on", "in", "into", "at",
            "he", "she", "they", "is", "are", "camera", "shot", "same", "continuous", "mouth", "stays", "closed", "then"}


def is_vi(sent):
    ws = [w for w in re.split(r"\s+", sent) if w and not w.startswith("@")]
    if not ws:
        return False
    en = sum(1 for w in ws if re.sub(r"[^a-z]", "", w.lower()) in EN_WORDS)
    if en >= 2 or (en >= 1 and len(ws) <= 3 and not VI.search(sent)):
        return False
    return True


def viet_only(x):
    keep = []
    for sent in re.split(r"(?<=[.!?…])\s+", x.strip()):
        if is_vi(sent):
            keep.append(sent)
        else:
            break
    return " ".join(keep)


def sections(t):
    return re.findall(r"^\[([A-Z][^\]]*)\]", t, re.M)


def main(d):
    files = sorted(glob.glob(os.path.join(d, "clip-*.md")), key=lambda f: int(re.search(r"clip-(\d+)", f).group(1)))
    if not files:
        print("ERROR no clip files"); return 1
    voices = {}
    bad = 0
    for f in files:
        t = open(f, encoding="utf-8").read()
        errs, warns = [], []
        if not t.lstrip().startswith("[FORMAT]"):
            errs.append("must start with [FORMAT]")
        secs = sections(t)
        if not secs or not secs[-1].startswith("AVOID"):
            errs.append(f"[AVOID] must be the last section (got {secs[-1:]})")
        if re.search(r"^#|\*\*|^\|.*\|\s*$", t, re.M):
            errs.append("markdown (#, **, table) in prompt")
        if re.search(r"#[0-9A-Fa-f]{6}\b", t):
            errs.append("hex colour code")
        body_wo_segments = "\n".join(l for l in t.splitlines() if not SEG.match(l))
        m = CLOCK.search(body_wo_segments)
        if m:
            errs.append(f"clock digits: {m.group(0)!r}")
        if "Clean frame" not in t:
            errs.append("clean-frame sentence missing")
        # characters block
        cm = re.search(r"^\[CHARACTERS[^\]]*\]\n(.*?)(?=^\[)", t, re.M | re.S)
        declared = set()
        if cm:
            for line in cm.group(1).splitlines():
                mm = re.match(r"^-?\s*(@[\wÀ-ỹĐđ]+)\s*=", line)
                if mm:
                    declared.add(mm.group(1))
                    v = re.search(r"Voice:\s*(.+)$", line)
                    if v:
                        voices.setdefault(mm.group(1), set()).add(v.group(1).strip())
        else:
            errs.append("no [CHARACTERS…] block")
        used = set(TAG.findall(t))
        stray = {u for u in used if u not in declared and not any(u.startswith(dc) for dc in declared)}
        if stray:
            errs.append(f"tags mentioned but not declared (runner would attach their refs): {sorted(stray)}")
        # dialogue
        turns, total = 0, 0
        lines_seen = []
        for line in t.splitlines():
            sm = SEG.match(line)
            if not sm:
                if SAY.search(line):
                    errs.append("dialogue outside a timed segment: " + line[:80])
                continue
            a = int(sm.group(1)) * 60 + float(sm.group(2))
            b = int(sm.group(3)) * 60 + float(sm.group(4))
            seg = sm.group(5)
            heads = list(SAY_HEAD.finditer(seg))
            says = [(h.group(1), h.group(2), seg[h.end():(heads[i + 1].start() if i + 1 < len(heads) else len(seg))]) for i, h in enumerate(heads)]
            if not says:
                continue
            speakers = {s[0].strip() for s in says}
            if len(speakers) > 1:
                errs.append(f"{len(speakers)} speakers in one segment {sm.group(1)}:{sm.group(2)}")
            n = 0
            for who, voice, txt in says:
                vi = viet_only(txt)
                lines_seen.append(vi)
                n += syl(vi)
                turns += 1
            total += n
            dur = b - a
            rate = n / dur if dur > 0 else 99
            if rate > 4.4:
                errs.append(f"segment {a:.1f}–{b:.1f}s: {n} syllables = {rate:.1f}/s (max 4.2, hard limit 4.4)")
            elif rate > 4.2:
                warns.append(f"segment {a:.1f}–{b:.1f}s: {rate:.1f} syllables/s (target ≤ 4.2)")
        if turns > 3 or (turns == 3 and total > 24):
            errs.append(f"{turns} speaking turns ({total} syllables)")
        if total > 36:
            errs.append(f"{total} spoken syllables in clip (max 36)")
        for ln in lines_seen:
            if ln and t.count(ln[:25]) > 1:
                errs.append("dialogue repeated elsewhere in prompt: " + ln[:40])
        if not 3000 <= len(t) <= 11000:
            warns.append(f"length {len(t)} chars")
        name = os.path.basename(f)
        if errs:
            bad += 1
            for e in errs:
                print(f"ERROR {name}: {e}")
        for w in warns:
            print(f"WARN  {name}: {w}")
        print(f"{'OK   ' if not errs else 'FAIL '} {name}: {turns} turns, {total} syllables, {len(t)} chars")
    for tag, vs in voices.items():
        if len(vs) > 1:
            bad += 1
            print(f"ERROR voice string for {tag} differs between clips: {len(vs)} variants")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
