#!/usr/bin/env python3
"""
FlowKit — Film → Shorts (TikTok / YouTube Shorts / Facebook Reels)

Cắt các đoạn nổi bật của một phim 16:9 (canh-XX/clip-YY) thành video dọc 1080×1920:
nền mờ từ chính cảnh phim, khung phim 16:9 ở giữa, câu hook ở trên, phụ đề tiếng Việt
khớp tiếng nói (Whisper) bên dưới khung phim, chừa vùng giao diện của TikTok/Reels.

Nguồn: <series>/shorts/SHORTS_PLAN.json (danh sách short, clip, hook, caption 3 nền tảng).
Kết quả: <series>/shorts/phan-XX-<slug>/ gồm <slug>.mp4, cover.jpg, phu-de.srt, caption.md
và <series>/shorts/README.md (bảng kế hoạch + lịch đăng).

Usage:
    python flowkit/scripts/make_shorts.py cai-ket-cho-tieu-tam                # transcribe + render tất cả
    python flowkit/scripts/make_shorts.py cai-ket-cho-tieu-tam --only 1 5 17  # chỉ vài phần
    python flowkit/scripts/make_shorts.py cai-ket-cho-tieu-tam --transcribe   # chỉ chạy Whisper (cache)
    python flowkit/scripts/make_shorts.py cai-ket-cho-tieu-tam --check        # báo clip nói lặp / thiếu file
    python flowkit/scripts/make_shorts.py cai-ket-cho-tieu-tam --captions     # chỉ ghi caption.md + README

Cần: ffmpeg, Pillow, và một Python có mlx_whisper (WHISPER_PYTHON; mặc định venv của VoiceStudio).
"""

import argparse
import difflib
import json
import os
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WHISPER_MODEL = os.environ.get("WHISPER_MODEL", "mlx-community/whisper-large-v3-turbo")
WHISPER_PYTHON = os.environ.get(
    "WHISPER_PYTHON",
    str(Path.home() / "Library/Application Support/VoiceStudio/runtime/project/.venv/bin/python3"),
)


# ---------------------------------------------------------------- Whisper

# Lines Whisper invents over music or effects (YouTube outros from its training data).
HALLUCINATIONS = ("subscribe", "ghiền mì gõ", "đăng ký kênh", "cảm ơn các bạn đã theo dõi",
                  "hẹn gặp lại các bạn", "không bỏ lỡ những video")


def hallucinated(text):
    return any(h in text.lower() for h in HALLUCINATIONS)


def whisper_worker(paths_file):
    """Runs under WHISPER_PYTHON: transcribe each (video, out_json) pair with word timestamps.

    mlx large-v3-turbo first (fast); a clip where it invents an outro line is redone with
    faster-whisper large-v3 + VAD, which skips the music/effects that triggered it.
    """
    import mlx_whisper
    vad_model = None

    for video, out_json in json.load(open(paths_file)):
        r = mlx_whisper.transcribe(
            video, path_or_hf_repo=WHISPER_MODEL, language="vi",
            word_timestamps=True, condition_on_previous_text=False,
        )
        segs = [(s["text"], s.get("no_speech_prob", 0),
                 [(w["word"], w["start"], w["end"]) for w in s.get("words", [])]) for s in r["segments"]]
        engine = "mlx-large-v3-turbo"
        if any(hallucinated(t) for t, _, _ in segs):
            if vad_model is None:
                from faster_whisper import WhisperModel
                vad_model = WhisperModel("large-v3", device="cpu", compute_type="int8")
            found, _ = vad_model.transcribe(video, language="vi", vad_filter=True,
                                            word_timestamps=True, condition_on_previous_text=False)
            segs = [(s.text, s.no_speech_prob, [(w.word, w.start, w.end) for w in s.words or []])
                    for s in found]
            engine = "faster-whisper-large-v3-vad"
        segs = [s for s in segs if s[1] <= 0.8 and not hallucinated(s[0])]
        words = [{"w": w.strip(), "s": round(float(st), 3), "e": round(float(en), 3)}
                 for _, _, ws in segs for w, st, en in ws]
        text = " ".join(t.strip() for t, _, _ in segs)
        Path(out_json).write_text(json.dumps({"text": text, "engine": engine, "words": words},
                                             ensure_ascii=False, indent=1))
        print(f"  [WHISPER] {Path(video).name} ({engine}): {text[:70]}", flush=True)


def transcribe(film, clip_ids, force=False):
    todo = []
    for cid in clip_ids:
        src = film.clip_path(cid)
        out = film.whisper_path(cid)
        stale = (not out.exists() or out.stat().st_mtime < src.stat().st_mtime
                 or hallucinated(json.loads(out.read_text())["text"])) if src.exists() else False
        if src.exists() and (force or stale):
            todo.append([str(src), str(out)])
    if not todo:
        return
    film.whisper_dir.mkdir(parents=True, exist_ok=True)
    job = film.whisper_dir / "_todo.json"
    job.write_text(json.dumps(todo))
    print(f"  [WHISPER] {len(todo)} clip với {WHISPER_PYTHON}")
    subprocess.run([WHISPER_PYTHON, __file__, "--_whisper-worker", str(job)], check=True)
    job.unlink()


# ---------------------------------------------------------------- Film data

def norm(token):
    """Lowercase, keep Vietnamese diacritics, drop punctuation."""
    t = unicodedata.normalize("NFC", token.lower())
    return re.sub(r"[^\w]", "", t)


def bare(token):
    """norm() without diacritics — 'Tùng,' and 'tung' compare equal."""
    t = unicodedata.normalize("NFD", norm(token).replace("đ", "d"))
    return "".join(c for c in t if not unicodedata.combining(c))


class Film:
    def __init__(self, series):
        self.series = series
        self.dir = ROOT / series
        self.shorts_dir = self.dir / "shorts"
        self.whisper_dir = self.shorts_dir / "_whisper"
        self.plan_path = self.shorts_dir / "SHORTS_PLAN.json"
        self.turns = self._load_script()

    @staticmethod
    def split_id(cid):
        scene, clip = cid.split(".")
        return int(scene), int(clip)

    def clip_name(self, cid):
        s, c = self.split_id(cid)
        return f"canh-{s:02d}_clip-{c:02d}"

    def clip_path(self, cid):
        s, _ = self.split_id(cid)
        return self.dir / "output_videos" / f"canh-{s:02d}" / f"{self.clip_name(cid)}.mp4"

    def whisper_path(self, cid):
        return self.whisper_dir / f"{self.clip_name(cid)}.json"

    def words(self, cid):
        return json.loads(self.whisper_path(cid).read_text())["words"]

    def _load_script(self):
        """{clip id: [(speaker, line)]} from PHAN_CANH_OMNI.json or PHAN_CANH_V3.json."""
        turns = {}
        omni, v3 = self.dir / "PHAN_CANH_OMNI.json", self.dir / "PHAN_CANH_V3.json"
        if omni.exists():
            for scene in json.loads(omni.read_text())["scenes"]:
                for clip in scene["clips"]:
                    t = clip.get("turns") or ([{"speaker": clip["speaker"], "line": clip["line"]}]
                                              if clip.get("line") else [])
                    turns[clip["id"]] = [(x["speaker"], x["line"]) for x in t]
        elif v3.exists():
            for scene in json.loads(v3.read_text())["scenes"]:
                for clip in scene["clips"]:
                    cid = f"{scene['number']:02d}.{clip['number']}"
                    turns[cid] = [(x["speaker"], x["text"]) for x in clip.get("dialogue", [])]
        return turns

    def rendered_ids(self):
        ids = []
        for p in sorted((self.dir / "output_videos").glob("canh-*/canh-*_clip-*.mp4")):
            m = re.match(r"canh-(\d+)_clip-(\d+)$", p.stem)
            if m:
                ids.append(f"{int(m[1]):02d}.{int(m[2])}")
        return ids

    def plan(self):
        return json.loads(self.plan_path.read_text())

    def duration(self, cid):
        return probe_duration(self.clip_path(cid))


def probe_duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", str(path)], capture_output=True, text=True).stdout
    return float(out)


# ---------------------------------------------------------------- Subtitles

def aligned_words(film, cid, use_script=True):
    """Whisper words (what was actually said) with the script's spelling and speaker where they match.

    use_script=False when the render came from another script version: matching against the wrong
    lines would paste in stray punctuation and speakers, so the words stay as Whisper heard them.
    """
    words = [dict(w) for w in film.words(cid)]
    if not use_script:
        return words
    script, starts = [], set()   # starts: script tokens that open a sentence (their capital says nothing)
    for spk, line in film.turns.get(cid, []):
        for k, tok in enumerate(line.split()):
            if k == 0 or re.search(r"[.?!…]$", script[-1][0]):
                starts.add(len(script))
            script.append((tok, spk))

    def spelled(j, heard):
        """Script token j, capitalised at a sentence start in the output, for a name, or where Whisper
        heard a new sentence (not right after a comma)."""
        tok = script[j][0]
        prev = out[-1]["w"] if out else ""
        cap = (not prev or re.search(r"[.?!…]$", prev) or (tok[:1].isupper() and j not in starts)
               or (heard[:1].isupper() and not prev.endswith(",")))
        return (tok[:1].upper() if cap else tok[:1].lower()) + tok[1:]

    sm = difflib.SequenceMatcher(None, [bare(w["w"]) for w in words],
                                 [bare(t) for t, _ in script], autojunk=False)
    out = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            for k in range(i2 - i1):
                w = words[i1 + k]
                out.append(dict(w, w=spelled(j1 + k, w["w"]), spk=script[j1 + k][1]))
        elif op == "replace" and _close(words[i1:i2], script[j1:j2]):
            # Misheard words ("thức dây", "L58"): show the script's words over the same time span.
            s, e = words[i1]["s"], words[i2 - 1]["e"]
            step = (e - s) / (j2 - j1)
            for k in range(j2 - j1):
                heard = words[i1]["w"] if k == 0 else ""
                out.append({"w": spelled(j1 + k, heard), "s": s + k * step, "e": s + (k + 1) * step,
                            "spk": script[j1 + k][1]})
        else:
            out.extend(words[i1:i2])   # said but not in the script (or dropped script words: skip)
    words = out
    # Unmatched words take the speaker of the nearest matched word before (else after) them.
    for seq in (words, list(reversed(words))):
        last = None
        for w in seq:
            if w.get("spk"):
                last = w["spk"]
            elif last:
                w["spk"] = last
    return words


def _close(heard, script):
    said = " ".join(bare(w["w"]) for w in heard)
    if re.search(r"\d", said):
        return True
    return difflib.SequenceMatcher(None, said, " ".join(bare(t) for t, _ in script)).ratio() >= 0.6


def _text(ws):
    return " ".join(w["w"] for w in ws)


def _split(ws, max_chars):
    """Split a too-long phrase where both halves are closest in length, preferring a break after
    punctuation or before a capital (a sentence Whisper heard without punctuation)."""
    if len(_text(ws)) <= max_chars or len(ws) < 2:
        return [ws]
    natural = [i for i in range(1, len(ws))
               if re.search(r"[.?!…,;:]$", ws[i - 1]["w"]) or ws[i]["w"][:1].isupper()]
    fits = [i for i in natural if max(len(_text(ws[:i])), len(_text(ws[i:]))) <= max_chars]
    candidates = fits or range(1, len(ws))
    i = min(candidates, key=lambda k: abs(len(_text(ws[:k])) - len(_text(ws[k:]))))
    return _split(ws[:i], max_chars) + _split(ws[i:], max_chars)


def build_cues(words, max_chars=56):
    # Phrases end at a speaker change, a pause, or a full stop (unless the sentence is a 1–2 word reply).
    phrases, cur = [], []
    for w in words:
        if cur and (w.get("spk") != cur[-1].get("spk") or w["s"] - cur[-1]["e"] > 0.6
                    or (re.search(r"[.?!…]$", cur[-1]["w"]) and len(cur) >= 3)):
            phrases.append(cur)
            cur = []
        cur.append(w)
    if cur:
        phrases.append(cur)
    cues = [{"s": p[0]["s"], "e": p[-1]["e"], "spk": p[0].get("spk"), "text": _text(p)}
            for phrase in phrases for p in _split(phrase, max_chars)]
    for k, c in enumerate(cues):
        if k == 0 or not cues[k - 1]["text"].endswith(","):
            c["text"] = c["text"][:1].upper() + c["text"][1:]
    for a, b in zip(cues, cues[1:]):
        a["e"] = min(max(a["e"] + 0.3, a["s"] + 0.8), b["s"])
    if cues:
        cues[-1]["e"] += 0.3
    return cues


def find_repeats(film, cid, n=4):
    """Times where a 4-word phrase is said again in the clip although the script says it once."""
    words = film.words(cid)
    script = " ".join(bare(t) for _, line in film.turns.get(cid, []) for t in line.split())
    seen, hits = {}, []
    for i in range(len(words) - n + 1):
        gram = " ".join(bare(w["w"]) for w in words[i:i + n])
        if gram in seen and script.count(gram) < 2:
            hits.append((words[seen[gram]]["s"], words[i]["s"], gram))
        seen.setdefault(gram, i)
    return hits


def fmt_srt(t):
    ms = int(round(t * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


# ---------------------------------------------------------------- Graphics (Pillow)

W, H = 1080, 1920
VW, VH = 1080, 608            # film box, full width 16:9
VIDEO_Y = 650                 # film box top; centre ≈ screen centre
SUB_Y = VIDEO_Y + VH + 24     # subtitles under the film, above TikTok/Reels caption UI
SUB_H = 210
SUB_MAX_W = 880               # keep clear of the right-hand action icons
FONT_DIRS = [Path.home() / "Library/Fonts", Path("/Library/Fonts"),
             Path("/System/Library/Fonts/Supplemental"), Path("/usr/share/fonts/truetype/roboto")]


def font(name, size):
    from PIL import ImageFont
    for d in FONT_DIRS:
        for candidate in (name, "Arial Unicode.ttf"):
            if (d / candidate).exists():
                return ImageFont.truetype(str(d / candidate), size)
    raise SystemExit(f"Không tìm thấy font {name}")


def hex_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rich_runs(line, base, accent):
    """'đặt may [ÁO CƯỚI]' → [('đặt may ', base), ('ÁO CƯỚI', accent)]."""
    return [(part, accent if i % 2 else base)
            for i, part in enumerate(re.split(r"\[|\]", line)) if part]


def wrap(text, fnt, max_w):
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if cur and fnt.getlength(re.sub(r"[\[\]]", "", trial)) > max_w:
            lines.append(cur)
            cur = word
        else:
            cur = trial
    return lines + ([cur] if cur else [])


def draw_lines(img, lines, fnt, top, base, accent, stroke, line_h):
    """Centred multi-colour lines with a black stroke and a soft shadow."""
    from PIL import Image, ImageDraw, ImageFilter
    shadow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    sd, d = ImageDraw.Draw(shadow), ImageDraw.Draw(img)
    for row, line in enumerate(lines):
        runs = rich_runs(line, base, accent)
        width = sum(fnt.getlength(t) for t, _ in runs)
        x, y = (img.width - width) / 2, top + row * line_h
        for text, _ in runs:
            sd.text((x + 3, y + 5), text, font=fnt, fill=(0, 0, 0, 200), stroke_width=stroke + 2,
                    stroke_fill=(0, 0, 0, 200))
            x += fnt.getlength(text)
    img.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(6)))
    for row, line in enumerate(lines):
        runs = rich_runs(line, base, accent)
        width = sum(fnt.getlength(t) for t, _ in runs)
        x, y = (img.width - width) / 2, top + row * line_h
        for text, colour in runs:
            d.text((x, y), text, font=fnt, fill=colour, stroke_width=stroke, stroke_fill=(0, 0, 0))
            x += fnt.getlength(text)


def pill(img, text, fnt, cy, bg, fg):
    from PIL import ImageDraw
    d = ImageDraw.Draw(img)
    tw = fnt.getlength(text)
    asc, desc = fnt.getmetrics()
    pad_x, pad_y = 28, 14
    box = ((img.width - tw) / 2 - pad_x, cy - (asc + desc) / 2 - pad_y,
           (img.width + tw) / 2 + pad_x, cy + (asc + desc) / 2 + pad_y)
    d.rounded_rectangle(box, radius=(box[3] - box[1]) / 2, fill=bg)
    d.text(((img.width - tw) / 2, cy - (asc + desc) / 2), text, font=fnt, fill=fg)


def render_top(path, tag, hook, style, badge=None):
    """Series tag pill + hook (2–3 lines) above the film box; with a badge ("CÒN TIẾP »…") above the hook."""
    from PIL import Image
    img = Image.new("RGBA", (W, VIDEO_Y), (0, 0, 0, 0))
    pill(img, tag, font("Roboto-Bold.ttf", 34), 232, hex_rgb(style["tag_bg"]), (255, 255, 255))
    region = 300
    size = 74
    if badge:
        pill(img, badge, font("Roboto-Black.ttf", 42), 340, hex_rgb(style["accent"]), (20, 20, 20))
        region, size = 395, 62
    while True:
        fnt = font("Roboto-Black.ttf", size)
        lines = [l for part in hook.split("\n") for l in wrap(part, fnt, 980)]
        if len(lines) <= 3 or size <= 56:
            break
        size -= 4
    # Keep a [highlight] that wrapped onto the next line highlighted there too.
    for i in range(len(lines) - 1):
        if lines[i].count("[") > lines[i].count("]"):
            lines[i] += "]"
            lines[i + 1] = "[" + lines[i + 1]
    line_h = int(size * 1.18)
    block = line_h * len(lines)
    top = region + (VIDEO_Y - 30 - region - block) / 2
    draw_lines(img, lines, fnt, top, (255, 255, 255), hex_rgb(style["accent"]), 6, line_h)
    img.save(path)


def wrap_balanced(text, fnt, max_w):
    """Two lines of similar width, preferring a break after punctuation."""
    words = text.split()
    if fnt.getlength(text) <= max_w or len(words) < 2:
        return [text]
    best = None
    for i in range(1, len(words)):
        a, b = " ".join(words[:i]), " ".join(words[i:])
        widest = max(fnt.getlength(a), fnt.getlength(b))
        if widest > max_w:
            continue
        score = widest - (150 if words[i - 1].endswith((",", ".", "?", "!", ";", ":", "…")) else 0)
        if best is None or score < best[0]:
            best = (score, [a, b])
    return best[1] if best else wrap(text, fnt, max_w)


def render_sub(path, text, colour):
    from PIL import Image
    img = Image.new("RGBA", (W, SUB_H), (0, 0, 0, 0))
    fnt = font("Roboto-Bold.ttf", 56)
    lines = wrap_balanced(text, fnt, SUB_MAX_W)[:3]
    line_h = 70
    draw_lines(img, lines, fnt, 10 + (2 - min(len(lines), 2)) * line_h / 2, colour, colour, 5, line_h)
    img.save(path)


# ---------------------------------------------------------------- Video (ffmpeg)

def detect_bars(film, cid, cache):
    """Letterbox bars present for the whole clip → crop box [w, h, x, y], else None."""
    key = film.clip_name(cid)
    src = film.clip_path(cid)
    if key in cache and cache[key]["mtime"] == src.stat().st_mtime:
        return cache[key]["crop"]
    err = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(src), "-vf",
                          "cropdetect=limit=0.09:round=2:reset=0", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    found = re.findall(r"crop=(\d+):(\d+):(\d+):(\d+)", err)
    crop = None
    if found:
        w, h, x, y = map(int, found[-1])
        # Moderate bars only: a tiny box usually means a dark scene, not letterboxing.
        if 560 <= h < 704 and w >= 1240:
            crop = [w, h, x, y]
    cache[key] = {"mtime": src.stat().st_mtime, "crop": crop}
    return crop


def video_filter(film, cid, fixes, bars_cache):
    fix = fixes.get(cid, {})
    parts = []
    if "delogo" in fix:
        x, y, w, h = fix["delogo"]
        parts.append(f"delogo=x={x}:y={y}:w={w}:h={h}")
    crop = fix.get("crop") or detect_bars(film, cid, bars_cache)
    if crop:
        parts.append("crop={}:{}:{}:{}".format(*crop))
    parts += [f"scale={VW}:{VH}:force_original_aspect_ratio=increase:flags=lanczos",
              f"crop={VW}:{VH}", "setsar=1", "fps=24", "format=yuv420p"]
    return ",".join(parts)


def plan_segments(film, short):
    """Resolve each segment's [from, to] window: trim dead air after the last word."""
    segs = []
    for i, seg in enumerate(short["segments"]):
        cid = seg["clip"]
        dur = film.duration(cid)
        words = [w for w in film.words(cid)
                 if w["s"] >= seg.get("from", 0) and w["e"] <= seg.get("to", dur) + 0.05]
        start = seg.get("from", 0.0)
        if "to" in seg:
            end = seg["to"]
        else:
            tail = 1.8 if i == len(short["segments"]) - 1 else 1.0
            end = min(dur, words[-1]["e"] + tail) if words else dur
        segs.append({"clip": cid, "from": start, "to": end})
    return segs


def render_short(film, plan, short, out_dir, bars_cache):
    style = plan["style"]
    n = short["n"]
    tmp = out_dir / "_tmp"
    tmp.mkdir(parents=True, exist_ok=True)
    segs = plan_segments(film, short)

    # Subtitles on the output timeline.
    cues, t0 = [], 0.0
    colours = {k: hex_rgb(v) for k, v in plan.get("speaker_colors", {}).items()}
    for seg in segs:
        words = [w for w in aligned_words(film, seg["clip"], plan.get("match_script", True))
                 if seg["from"] - 0.05 <= (w["s"] + w["e"]) / 2 <= seg["to"]]
        for c in build_cues(words):
            c["s"] = max(c["s"] - seg["from"], 0) + t0
            c["e"] = min(c["e"] - seg["from"], seg["to"] - seg["from"]) + t0
            cues.append(c)
        t0 += seg["to"] - seg["from"]
    total = t0

    tag = f"{plan['tag']}  •  PHẦN {n}"
    render_top(tmp / "top.png", tag, short["hook"], style)
    # Last 2.5 s: the hook gives way to a teaser of the next part.
    nxt = next((s for s in plan["shorts"] if s["n"] == n + 1), None)
    if nxt:
        render_top(tmp / "top_end.png", tag, nxt["hook"], style, badge=f"CÒN TIẾP » PHẦN {n + 1}")
    else:
        render_top(tmp / "top_end.png", tag, plan["final_end_text"], style, badge=plan["final_badge"])
    end_from = max(total - 2.5, 0)
    fix_words = plan.get("subtitle_replace", {})
    for k, c in enumerate(cues):
        for wrong, right in fix_words.items():
            c["text"] = re.sub(wrong, right, c["text"])   # keys are regex patterns
        render_sub(tmp / f"sub_{k:03d}.png", c["text"], colours.get(c["spk"], (255, 255, 255)))

    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y"]
    for seg in segs:
        cmd += ["-ss", f"{seg['from']:.3f}", "-t", f"{seg['to'] - seg['from']:.3f}",
                "-i", str(film.clip_path(seg["clip"]))]
    pngs = [tmp / "top.png", tmp / "top_end.png"] + [tmp / f"sub_{k:03d}.png" for k in range(len(cues))]
    for p in pngs:
        cmd += ["-i", str(p)]

    fc = []
    for i, seg in enumerate(segs):
        d = seg["to"] - seg["from"]
        fc.append(f"[{i}:v]{video_filter(film, seg['clip'], plan.get('fixes', {}), bars_cache)}[v{i}]")
        fc.append(f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo,"
                  f"afade=t=in:d=0.04,afade=t=out:st={max(d - 0.08, 0):.3f}:d=0.08[a{i}]")
    fc.append("".join(f"[v{i}][a{i}]" for i in range(len(segs))) + f"concat=n={len(segs)}:v=1:a=1[mv][ma]")
    fc.append("[mv]split[m1][m2]")
    fc.append(f"[m2]crop={VH * 9 // 16}:{VH},scale=270:480,gblur=sigma=9,scale={W}:{H},"
              f"eq=brightness=-0.13:saturation=1.1[bg]")
    fc.append(f"[bg][m1]overlay=0:{VIDEO_Y}[c0]")
    base = len(segs)
    fc.append(f"[c0][{base}:v]overlay=0:0:enable='lt(t,{end_from:.3f})'[t0]")
    fc.append(f"[t0][{base + 1}:v]overlay=0:0:enable='gte(t,{end_from:.3f})'[t1]")
    last = "t1"
    for k, c in enumerate(cues):
        fc.append(f"[{last}][{base + 2 + k}:v]overlay=0:{SUB_Y}:"
                  f"enable='between(t,{c['s']:.3f},{c['e']:.3f})'[s{k}]")
        last = f"s{k}"
    fc.append(f"[{last}]null[vout]")
    fc.append("[ma]loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[aout]")

    mp4 = out_dir / f"{out_dir.name}.mp4"
    cmd += ["-filter_complex", ";".join(fc), "-map", "[vout]", "-map", "[aout]",
            "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-profile:v", "high",
            "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(mp4)]
    subprocess.run(cmd, check=True)

    # Cover: one frame of the finished short (hook already on it).
    cover_t = short.get("cover_at", 1.0)
    subprocess.run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", f"{cover_t:.2f}",
                    "-i", str(mp4), "-frames:v", "1", "-q:v", "3", str(out_dir / "cover.jpg")], check=True)

    srt = "\n".join(f"{k + 1}\n{fmt_srt(c['s'])} --> {fmt_srt(c['e'])}\n{c['text']}\n"
                    for k, c in enumerate(cues))
    (out_dir / "phu-de.srt").write_text(srt)
    for p in tmp.iterdir():
        p.unlink()
    tmp.rmdir()
    return {"duration": round(total, 1), "segments": segs}


# ---------------------------------------------------------------- Captions & plan README

WEEKDAYS = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"]


def part_dir(film, short):
    return film.shorts_dir / f"phan-{short['n']:02d}-{short['slug']}"


def slot(plan, n):
    from datetime import date, timedelta
    sch = plan["schedule"]
    day = date.fromisoformat(sch["start"]) + timedelta(days=(n - 1) // sch["per_day"])
    return f"{WEEKDAYS[day.weekday()]} {day:%d/%m} – {sch['times'][(n - 1) % sch['per_day']]}"


def caption_texts(plan, short):
    n, shorts = short["n"], plan["shorts"]
    nxt = next((s for s in shorts if s["n"] == n + 1), None)
    full = (f"🎬 Xem full phim: {plan['full_movie_url']}" if plan.get("full_movie_url")
            else plan["full_movie_line"])
    next_line = (f"👉 Xem tiếp Phần {n + 1}: {nxt['title']}" if nxt else plan["final_cta"])
    tags = {p: " ".join(plan["hashtags"][p] + (short.get("tags", []) if p != "youtube" else []))
            for p in ("tiktok", "youtube", "facebook")}
    tiktok_next = f"👉 Phần {n + 1} ở trang cá nhân, Follow để xem tiếp!" if nxt else plan["final_cta"]
    tiktok = f"{short['caption']}\n{short['question']}\n\n{tiktok_next}\n{tags['tiktok']}"
    youtube = f"{short['caption']}\n\n{full}\n{next_line}\n\n#Shorts {tags['youtube']}"
    facebook = f"{short['caption']}\n\n{short['question']} 👇\n{next_line}\n{full}\n\n{tags['facebook']}"
    return tiktok, youtube, facebook


def write_captions(film, plan, manifest):
    total = len(plan["shorts"])
    rows = []
    for short in plan["shorts"]:
        n = short["n"]
        info = manifest.get(str(n), {})
        dur = f"{info['duration']:.0f}s" if info else "chưa render"
        clips = ", ".join(dict.fromkeys(seg["clip"] for seg in short["segments"]))
        d = part_dir(film, short)
        d.mkdir(parents=True, exist_ok=True)
        tiktok, youtube, facebook = caption_texts(plan, short)
        (d / "caption.md").write_text(
            f"# Phần {n}/{total} — {short['title']}\n\n"
            f"- **Video:** `{d.name}.mp4` ({dur}) · bìa `cover.jpg` · phụ đề rời `phu-de.srt`\n"
            f"- **Cảnh trong phim:** {clips}\n"
            f"- **Lịch đăng:** {slot(plan, n)} (cả 3 nền tảng)\n\n"
            f"## TikTok\n\n```text\n{tiktok}\n```\n\n"
            f"## YouTube Shorts\n\n**Tiêu đề** ({len(short['yt_title'])}/100 ký tự):\n\n"
            f"```text\n{short['yt_title']}\n```\n\n**Mô tả:**\n\n```text\n{youtube}\n```\n\n"
            f"## Facebook Reels\n\n```text\n{facebook}\n```\n")
        star = "⭐" if short.get("top") else ""
        rows.append(f"| {n} | [{short['title']}]({d.name}/caption.md) | {clips} | {dur} | {slot(plan, n)} | {star} |")

    lines = lambda key: "\n".join(plan[key]) if isinstance(plan[key], list) else plan[key]
    readme = lines("readme_intro").rstrip() + "\n\n" + \
        "## Lịch đăng & danh sách phần\n\n" + \
        "| Phần | Nội dung (mở caption) | Cảnh | Thời lượng | Đăng lúc | Ưu tiên |\n" + \
        "|---|---|---|---|---|---|\n" + "\n".join(rows) + "\n\n" + lines("readme_notes").rstrip() + "\n"
    (film.shorts_dir / "README.md").write_text(readme)


def main():
    if len(sys.argv) == 3 and sys.argv[1] == "--_whisper-worker":
        return whisper_worker(sys.argv[2])
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("series")
    ap.add_argument("--only", nargs="*", type=int, help="chỉ render các phần này (số n trong plan)")
    ap.add_argument("--transcribe", action="store_true", help="chỉ chạy Whisper cho mọi clip đã render")
    ap.add_argument("--check", action="store_true", help="báo clip thiếu file / nói lặp câu")
    ap.add_argument("--captions", action="store_true", help="chỉ ghi caption.md + README, không render")
    ap.add_argument("--force-whisper", action="store_true")
    args = ap.parse_args()

    film = Film(args.series)
    if args.transcribe:
        return transcribe(film, film.rendered_ids(), force=args.force_whisper)
    if args.check:
        transcribe(film, film.rendered_ids())
        for cid in film.rendered_ids():
            for first, again, gram in find_repeats(film, cid):
                print(f"  [LẶP] {cid}: '{gram}' nói lúc {first:.1f}s rồi lặp lại lúc {again:.1f}s")
        return

    plan = film.plan()
    manifest_path = film.shorts_dir / "_render.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    if not args.captions:
        needed = sorted({seg["clip"] for s in plan["shorts"] for seg in s["segments"]
                         if not args.only or s["n"] in args.only})
        transcribe(film, [c for c in needed if film.clip_path(c).exists()], force=args.force_whisper)
        bars_path = film.whisper_dir / "_bars.json"
        bars = json.loads(bars_path.read_text()) if bars_path.exists() else {}
        for short in plan["shorts"]:
            if args.only and short["n"] not in args.only:
                continue
            missing = [seg["clip"] for seg in short["segments"] if not film.clip_path(seg["clip"]).exists()]
            if missing:
                print(f"  [BỎ QUA] Phần {short['n']}: chưa có clip {', '.join(missing)}")
                continue
            print(f"  [SHORT] Phần {short['n']}: {short['title']}")
            manifest[str(short["n"])] = render_short(film, plan, short, part_dir(film, short), bars)
            print(f"          → {manifest[str(short['n'])]['duration']}s")
            bars_path.write_text(json.dumps(bars, indent=1))
            manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=1))
    write_captions(film, plan, manifest)
    print(f"  [XONG] {film.shorts_dir / 'README.md'}")


if __name__ == "__main__":
    main()
