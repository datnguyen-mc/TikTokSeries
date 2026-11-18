#!/usr/bin/env python3
"""Gom file tải tạm của trình duyệt trong app Claude (~/Downloads/.Q6L2SF6YDW.com.anthropic.claudefordesktop.*)
theo đúng thứ tự tải, đặt tên V3-<shot>_<id8>.mp4 rồi chép vào film/v3/clips/<shot>.mp4.
  python3 gom_tam.py <từ_giờ_UTC 'YYYY-mm-dd HH:MM:SS'> '<shot id8> <shot id8> ...'   (thứ tự tải)"""
import glob, os, sys, json, subprocess, shutil, datetime
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
CLIPS = os.path.join(ROOT, "film", "v3", "clips"); os.makedirs(CLIPS, exist_ok=True)
D = os.path.join(os.path.dirname(os.path.dirname(ROOT)), "Downloads") if False else os.path.expanduser("~/mnt/Downloads")
since = datetime.datetime.strptime(sys.argv[1], "%Y-%m-%d %H:%M:%S").replace(tzinfo=datetime.timezone.utc).timestamp()
log = [x.split() for x in sys.argv[2].split(",") if x.strip()]
tmp = sorted([f for f in glob.glob(os.path.join(D, ".Q6L2SF6YDW.com.anthropic.claudefordesktop.*")) if os.path.getmtime(f) >= since], key=os.path.getmtime)
import ghep_phim as G, build_shots_3 as S3
dur = {c: d for v in G.plan().values() for c, d in v}
dur.update({s[0]: s[2] for s in S3.REDO})
IDS = os.path.join(CLIPS, "_ids.json"); ids = json.load(open(IDS)) if os.path.exists(IDS) else {}
print(len(tmp), "file tạm,", len(log), "lượt tải")
def dlen(f):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f], capture_output=True, text=True).stdout or 0)
# Ghép file ↔ lượt tải theo thứ tự, dùng thời lượng để phát hiện lượt tải bị mất (bỏ qua lượt đó).
k = 0; lost = []; amb = []
for f in tmp:
    d = dlen(f)
    if d < 0.5:
        print("bỏ qua file hỏng/đang tải", os.path.basename(f)); continue
    j0 = k
    if os.environ.get("ORDER") != "1":
        while k < len(log) and abs(d - dur.get(log[k][0], d)) >= 0.2:
            k += 1
    elif k < len(log) and abs(d - dur.get(log[k][0], d)) >= 0.2:
        print("  (lệch thời lượng so với kế hoạch)", end=" ")
    if k >= len(log):
        print("không khớp được file", os.path.basename(f), f"{d:.2f}s — dừng"); break
    lost += [log[x][0] for x in range(j0, k)]
    if k > j0 and any(abs(dur.get(log[x][0], 0) - d) < 0.2 for x in range(j0, k)): amb.append(log[k][0])
    c, h = log[k]; k += 1
    dst = os.path.join(D, f"V3-{c}_{h}.mp4"); os.replace(f, dst)
    shutil.copy2(dst, os.path.join(CLIPS, c + ".mp4")); ids[c] = h
    print(c, h, f"{d:.2f}s")
print("MẤT:", " ".join(lost) or "—", "| CẦN SOÁT (có thể lệch):", " ".join(amb) or "—", "| chưa có file:", " ".join(x[0] for x in log[k:]) or "—")
json.dump(ids, open(IDS, "w"), indent=0, sort_keys=True)
print("clips:", len([x for x in os.listdir(CLIPS) if x.endswith(".mp4")]))
