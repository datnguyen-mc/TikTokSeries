#!/usr/bin/env python3
"""
Bức Tường Mỏng — Shorts dọc 1080×1920 cho TikTok / YouTube Shorts / Facebook Reels.

Khác flowkit/scripts/make_shorts.py ở nguồn: cắt thẳng từ bản dựng cuối (film/…_v5_1080p.mp4)
nên giữ nguyên màu, phần làm mờ chữ/logo, tiếng gõ đã sửa và nhạc phim; phụ đề lấy từ .srt
của bản dựng (đúng chữ kịch bản). Bố cục, chữ, nhãn “CÒN TIẾP”, README caption dùng chung
hàm với make_shorts.py để giống hệt các phim trước.

Nguồn: buc-tuong-mong/shorts/SHORTS_PLAN.json — mỗi đoạn ghi shot đầu/cuối (from_shot, to_shot),
mốc thời gian lấy từ shorts/_timeline_v5.json.

    python3 buc-tuong-mong/_tools/make_shorts_btm.py             # dựng tất cả + README
    python3 buc-tuong-mong/_tools/make_shorts_btm.py --only 3 5  # vài phần
    python3 buc-tuong-mong/_tools/make_shorts_btm.py --captions  # chỉ ghi README
"""
import argparse
import importlib.util
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve()
PROJ, ROOT = HERE.parents[1], HERE.parents[2]
_spec = importlib.util.spec_from_file_location("make_shorts", ROOT / "flowkit/scripts/make_shorts.py")
ms = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ms)
for _d in (Path.home() / "codr/fonts", PROJ / "_tools/fonts"):
    if _d.exists():
        ms.FONT_DIRS.insert(0, _d)

W, H, VW, VH, VIDEO_Y, SUB_Y = ms.W, ms.H, ms.VW, ms.VH, ms.VIDEO_Y, ms.SUB_Y
MAX_CHARS = 58


class Film:
    def __init__(self):
        self.dir = PROJ
        self.shorts_dir = PROJ / "shorts"
        self.plan_path = self.shorts_dir / "SHORTS_PLAN.json"

    def plan(self):
        return json.loads(self.plan_path.read_text(encoding="utf-8"))


def srt_time(x):
    h, m, s = x.strip().split(":")
    s, ms_ = s.split(",")
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms_) / 1000


def srt_entries(path):
    out = []
    for block in path.read_text(encoding="utf-8").strip().split("\n\n"):
        lines = block.strip().split("\n")
        if len(lines) >= 3 and "-->" in lines[1]:
            a, b = lines[1].split("-->")
            out.append((srt_time(a), srt_time(b), " ".join(lines[2:])))
    return out


def script_lines():
    """{shot id: [(speaker, line)]} from the prompts the clips were rendered with."""
    pat = re.compile(r"^- (\d+\.\d)s–(\d+\.\d)s, @(\w+) \([^)]*\): (.+)$", re.M)
    out = {}
    for s in json.loads((PROJ / "film/shots.json").read_text(encoding="utf-8")):
        p = PROJ / s["prompt"]
        if p.exists():
            out[s["id"]] = [("@" + m.group(3), m.group(4).strip()) for m in pat.finditer(p.read_text(encoding="utf-8"))]
    return out


def split_text(text, maxc=MAX_CHARS):
    """Sentence pieces, long ones split at commas then near the middle; short neighbours merged."""
    pieces = [p.strip() for p in re.findall(r"[^.?!…]+(?:[.?!…]+[”\"]?|$)", text) if p.strip()]
    out = []
    for p in pieces:
        if len(p) <= maxc:
            out.append(p)
            continue
        cur = ""
        for x in [x for x in re.split(r"(?<=,)\s+", p) if x]:
            if cur and len(cur) + 1 + len(x) > maxc:
                out.append(cur)
                cur = x
            else:
                cur = f"{cur} {x}".strip()
        if cur:
            out.append(cur)
    final = []
    for p in out:
        while len(p) > maxc:
            words = p.split()
            i = min(range(1, len(words)), key=lambda k: abs(len(" ".join(words[:k])) - len(" ".join(words[k:]))))
            final.append(" ".join(words[:i]))
            p = " ".join(words[i:])
        final.append(p)
    merged = []
    for p in final:
        if merged and len(merged[-1]) + 1 + len(p) <= maxc:
            merged[-1] = f"{merged[-1]} {p}"
        else:
            merged.append(p)
    return merged


def cues_for(segs, entries, timeline, lines, colours):
    def shot_at(t):
        for sid, a, b in timeline:
            if a - 0.05 <= t < b:
                return sid
        return None

    cues, t0 = [], 0.0
    for a, b in segs:
        for s, e, raw in entries:
            if e <= a + 0.05 or s >= b - 0.05:
                continue
            wall = "<i>" in raw
            text = re.sub(r"</?i>", "", raw).strip()
            spk = "wall" if wall else next((k for k, l in lines.get(shot_at(s + 0.1), []) if l == text), None)
            colour = colours.get(spk, (255, 255, 255))
            parts = split_text(text)
            total = sum(len(p) for p in parts)
            cum = 0
            for p in parts:
                ps = s + (e - s) * cum / total
                cum += len(p)
                pe = s + (e - s) * cum / total
                cs, ce = max(ps, a), min(pe, b)
                if ce - cs < 0.25:
                    continue
                cues.append({"s": cs - a + t0, "e": ce - a + t0, "text": p, "colour": colour})
        t0 += b - a
    return cues, t0


def render(film, plan, short):
    n = short["n"]
    timeline = json.loads((PROJ / plan["timeline"]).read_text())
    T = {sid: (a, b) for sid, a, b in timeline}
    segs = []
    for seg in short["segments"]:
        a = T[seg["from_shot"]][0] + seg.get("trim_start", 0.0)
        b = T[seg["to_shot"]][1] - seg.get("trim_end", 0.0)
        segs.append((round(a, 3), round(b, 3)))
    colours = {k: ms.hex_rgb(v) for k, v in plan.get("speaker_colors", {}).items()}
    cues, total = cues_for(segs, srt_entries(PROJ / plan["film_srt"]), timeline, script_lines(), colours)

    tmp = Path(tempfile.mkdtemp(prefix=f"btm_short_{n:02d}_"))   # ngoài thư mục dự án
    style = plan["style"]
    tag = f"{plan['tag']}  •  PHẦN {n}"
    ms.render_top(tmp / "top.png", tag, short["hook"], style)
    nxt = next((s for s in plan["shorts"] if s["n"] == n + 1), None)
    if nxt:
        ms.render_top(tmp / "top_end.png", tag, nxt["hook"], style, badge=f"CÒN TIẾP » PHẦN {n + 1}")
    else:
        ms.render_top(tmp / "top_end.png", tag, plan["final_end_text"], style, badge=plan["final_badge"])
    end_from = max(total - 2.5, 0)
    for k, c in enumerate(cues):
        ms.render_sub(tmp / f"sub_{k:03d}.png", c["text"], c["colour"])

    src = str(PROJ / plan["film_file"])
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y"]
    for a, b in segs:
        cmd += ["-ss", f"{a:.3f}", "-t", f"{b - a:.3f}", "-i", src]
    pngs = [tmp / "top.png", tmp / "top_end.png"] + [tmp / f"sub_{k:03d}.png" for k in range(len(cues))]
    for p in pngs:
        cmd += ["-i", str(p)]
    fc = []
    for i, (a, b) in enumerate(segs):
        d = b - a
        fo = 0.4 if i == len(segs) - 1 else 0.06
        fc.append(f"[{i}:v]scale={VW}:{VH}:force_original_aspect_ratio=increase:flags=lanczos,"
                  f"crop={VW}:{VH},setsar=1,fps=24,format=yuv420p[v{i}]")
        fc.append(f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=0.04,"
                  f"afade=t=out:st={max(d - fo, 0):.3f}:d={fo}[a{i}]")
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
        fc.append(f"[{last}][{base + 2 + k}:v]overlay=0:{SUB_Y}:enable='between(t,{c['s']:.3f},{c['e']:.3f})'[s{k}]")
        last = f"s{k}"
    fc.append(f"[{last}]null[vout]")
    fc.append("[ma]loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[aout]")
    out = ms.video_path(film, short)
    cmd += ["-filter_complex", ";".join(fc), "-map", "[vout]", "-map", "[aout]",
            "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-profile:v", "high",
            "-pix_fmt", "yuv420p", "-r", "24", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(out)]
    subprocess.run(cmd, check=True)
    shutil.rmtree(tmp, ignore_errors=True)
    return {"duration": round(total, 1),
            "segments": [{"clip": s["clip"], "from": a, "to": b} for s, (a, b) in zip(short["segments"], segs)],
            "cues": len(cues)}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", nargs="*", type=int)
    ap.add_argument("--captions", action="store_true")
    args = ap.parse_args()
    film = Film()
    plan = film.plan()
    manifest_path = film.shorts_dir / "_render.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    if not args.captions:
        for short in plan["shorts"]:
            if args.only and short["n"] not in args.only:
                continue
            print(f"  [SHORT] Phần {short['n']}: {short['title']}", flush=True)
            manifest[str(short["n"])] = render(film, plan, short)
            print(f"          → {manifest[str(short['n'])]['duration']}s", flush=True)
            manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=1))
    ms.write_captions(film, plan, manifest)
    print(f"  [XONG] {film.shorts_dir / 'README.md'}")


if __name__ == "__main__":
    main()
