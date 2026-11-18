#!/usr/bin/env python3
"""Xuất kịch bản từng phần ra thư mục kich-ban/ và kiểm tra lỗi kịch bản.
    python3 _v2/export_kich_ban.py
P1–P3 lấy bản 3 (parts_v3.py, đã render); P4–P25 lấy bản 2 (parts1–3.py)."""
import json, os, re, sys, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import parts1, parts2, parts3, parts_v3  # noqa: E402
from build_v2 import CAM_VI, MOVE_VI, look_of, speech_secs  # noqa: E402
from looks import NAME, LOOKS  # noqa: E402
from vi_actions import VI  # noqa: E402

OUT = os.path.join(ROOT, "kich-ban")
V2 = {p["num"]: p for m in (parts1, parts2, parts3) for p in m.PARTS}
V3 = {p["num"]: p for p in parts_v3.PARTS}
PACE_VI = {"fast": "nói nhanh", "normal": "nói vừa", "slow": "nói chậm"}

# tên bối cảnh tiếng Việt lấy từ CAU_CHUYEN.md mục 5
PLACE_VI = {}
for ln in open(os.path.join(ROOT, "CAU_CHUYEN.md"), encoding="utf-8"):
    m = re.match(r"^\| (B\d+) \| ([^|]+) \| ([^|]+) \|", ln)
    if m and ("Sân thượng" in ln or m.group(1) not in PLACE_VI) and not m.group(2).startswith("Bống"):
        PLACE_VI[m.group(1)] = m.group(2).strip()

M15 = {}
try:
    for c in json.load(open(os.path.join(ROOT, "flow_15s", "manifest.json"), encoding="utf-8")):
        M15.setdefault(c["part"], []).append(c)
except FileNotFoundError:
    pass

VSYL = re.compile(r'^(ngh|ng|nh|ch|gh|gi|kh|ph|qu|th|tr|[bcdghklmnprstvx])?(oa|oe|uy|ua|uo|ia|[aeiouy])+(ch|ng|nh|[cmnptiyou])?$')
def foreign(line):
    t = unicodedata.normalize("NFD", line.lower()).replace("đ", "d")
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return [w for w in re.findall(r"[a-z]+", t) if not VSYL.match(w)]

def slug(s):
    s = unicodedata.normalize("NFD", s).replace("đ", "d").replace("Đ", "D")
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-")

def mmss(x):
    return f"{int(x)//60}:{int(x)%60:02d}"

issues = []
index = []
os.makedirs(OUT, exist_ok=True)
for n in range(1, 26):
    p = V3.get(n, V2[n]); ver = "Bản 3 (đã render)" if n in V3 else "Bản 2"
    total = sum(s["d"] for s in p["shots"])
    people = {}
    for s in p["shots"]:
        for w in s["who"]:
            people.setdefault(w, set()).add(look_of(p, s, w))
    locs = [p["loc"]] + sorted({s["loc"] for s in p["shots"] if s["loc"] and s["loc"] != p["loc"]}, key=lambda b: int(b[1:]))
    L = [f"# Phần {n:02d} · {p['title']}", "",
         f"- **Phiên bản:** {ver} · **Thời lượng:** ~{total} giây · **Số shot:** {len(p['shots'])}",
         "- **Bối cảnh:** " + "; ".join(f"{b} — {PLACE_VI.get(b, b)}" for b in locs),
         "- **Nhân vật & trang phục (tên trên Flow):** " + (", ".join(f"{NAME[w]}: " + " / ".join(f"{LOOKS[c][1]} ({c})" for c in sorted(cs)) for w, cs in people.items()) or "—"),
         f"- **Mở (3 giây đầu):** {p['hook']}",
         f"- **Câu treo cuối phần:** {p['cliff']}",
         f"- **Chuyển sang phần sau:** {p['tr']}", "",
         "## Kịch bản từng shot", "",
         "| Mốc | Shot | Dài | Máy quay | Trong khung | Hành động | Thoại |", "|---|---|---|---|---|---|---|"]
    t = 0.0
    lines_all = []
    for i, s in enumerate(p["shots"], 1):
        sid = f"{n:02d}-{i:02d}"
        size, move = s["cam"].split()
        cam = f"{CAM_VI[size]}, {MOVE_VI[move]}"
        if s["loc"] and s["loc"] != p["loc"]:
            cam += f" · {PLACE_VI.get(s['loc'], s['loc'])}"
        who = ", ".join(f"{NAME[w]} ({look_of(p, s, w)})" for w in s["who"]) or "—"
        act = VI.get(sid)
        if not act:
            issues.append(f"{sid}: thiếu diễn giải tiếng Việt cho hành động"); act = s["act"]
        say = "—"
        if s["say"]:
            sp, pace, tone, line = s["say"]
            say = f"**{NAME[sp]}** ({PACE_VI[pace]}): {line}"
            lines_all.append(line)
            if sp not in s["who"]:
                issues.append(f"{sid}: người nói {NAME[sp]} không có trong khung hình")
            need = 0.3 + speech_secs(sp, pace, line) + 0.3
            if need > s["d"] + 0.05:
                issues.append(f"{sid}: câu thoại cần ~{need:.1f}s nhưng shot chỉ {s['d']}s (khi render sẽ tự kéo dài)")
            bad = foreign(line)
            if bad:
                issues.append(f"{sid}: từ không phải tiếng Việt trong thoại: {', '.join(bad)}")
        for w in s["who"]:
            c = look_of(p, s, w)
            if c not in LOOKS or LOOKS[c][0] != w:
                issues.append(f"{sid}: mã trang phục {c} không khớp nhân vật {NAME[w]}")
        if len(s["who"]) > 2:
            issues.append(f"{sid}: {len(s['who'])} người trong khung (khuyến nghị tối đa 2)")
        L.append(f"| {mmss(t)} | `{sid}` | {s['d']}s | {cam} | {who} | {act} | {say} |")
        t += s["d"]
    # câu treo phải có trong thoại
    q = re.findall(r'"([^"]+)"', p["cliff"])
    norm = lambda x: re.sub(r"[^\w]", "", x.lower())
    for qq in q:
        if not any(norm(qq) in norm(l) or norm(l) in norm(qq) for l in lines_all):
            issues.append(f"P{n:02d}: câu treo \"{qq}\" không khớp câu thoại nào trong phần")
    if n in M15 and n not in V3:
        L += ["", "## Chia đoạn 15 giây để render (flow_15s)", "", "| Đoạn | Shot gộp | Nhân vật gắn | Thoại |", "|---|---|---|---|"]
        for c in M15[n]:
            L.append(f"| `{c['id']}` | {c['shots'][0]} → {c['shots'][-1]} | {', '.join(c['chars']) or '—'} | {' / '.join(c['lines']) or '—'} |")
    if n in V3:
        L += ["", "*Đã render ở 720p: clip từng shot trong `clips/v3/`, bản ghép 3 phút trong `tap/Vo_toi_mat_tri_nho_V3_3phut.mp4`.*"]
    fn = f"P{n:02d}_{slug(p['title'])}.md"
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write("\n".join(L) + "\n")
    index.append((n, p["title"], total, len(p["shots"]), ver, fn, sum(1 for s in p["shots"] if s["say"])))

# trailer
try:
    sys.path.insert(0, os.path.join(ROOT, "trailer"))
    from build_trailer_prompts import CLIPS as TCL  # noqa: E402
    T = ["# Trailer 1 phút (giọng A)", "", "File: `trailer/Trailer_1phut_Vo_toi_mat_tri_nho.mp4` (71 giây, khung 2.39:1). Dựng bằng `trailer/make_trailer2.py`.", "",
         "| Clip | Tên | Dài | Bối cảnh | Nhân vật | Thoại |", "|---|---|---|---|---|---|"]
    for c in TCL:
        turns = " / ".join(f"**{NAME[w]}:** {line}" for w, a, b, how, line in c["turns"]) or "—"
        T.append(f"| {c['id']} | {c['title']} | {c['dur']}s | {PLACE_VI.get(c['loc'], c['loc'])} | {', '.join(LOOKS[x][1] for x in c['looks'])} | {turns} |")
    T += ["", "**Thứ tự dựng:** giày cao gót đỏ (P01) → thẻ *MƯỜI NĂM NGÀY CƯỚI* → T1 → thẻ *CÔ ẤY TỈNH DẬY… VÀ QUÊN ĐÚNG MỘT NGƯỜI* → T2 → T3 → thẻ *NHƯNG AI MỚI LÀ NGƯỜI ĐANG DIỄN?* → T4 → T5 → T6 → thẻ *BA MƯƠI NGÀY. MỘT CHỦ TỊCH GIẤU MẶT.* → T7 → tựa phim → T8 → *SẮP RA MẮT*."]
    open(os.path.join(OUT, "TRAILER.md"), "w", encoding="utf-8").write("\n".join(T) + "\n")
except Exception as e:  # noqa: BLE001
    issues.append(f"Trailer: không đọc được ({e})")

tot = sum(x[2] for x in index)
I = ["# Kịch bản từng phần — VỢ TÔI MẤT TRÍ NHỚ CÓ CHỌN LỌC", "",
     f"25 phần · {sum(x[3] for x in index)} shot · ~{tot//60} phút {tot%60} giây · giọng A (giọng diễn viên thật, câu tả giọng cố định cho từng nhân vật).",
     "Cốt truyện, gài – trả: `../CAU_CHUYEN.md`. Mã trang phục: `../NHAN_VAT_FLOW.md`. Kết quả kiểm tra: `KIEM_TRA.md`.", "",
     "| Phần | Tên | Dài | Shot | Câu thoại | Phiên bản | File |", "|---|---|---|---|---|---|---|"]
for n, title, d, k, ver, fn, nl in index:
    I.append(f"| {n:02d} | {title} | {d}s | {k} | {nl} | {ver} | [{fn}]({fn}) |")
I += ["", "Trailer: [TRAILER.md](TRAILER.md)"]
open(os.path.join(OUT, "00_MUC_LUC.md"), "w", encoding="utf-8").write("\n".join(I) + "\n")
K = ["# Kiểm tra kịch bản", "", f"{len(issues)} điểm cần xem:" if issues else "Không phát hiện lỗi.", ""] + [f"- {x}" for x in issues]
open(os.path.join(OUT, "KIEM_TRA.md"), "w", encoding="utf-8").write("\n".join(K) + "\n")
print(f"{len(index)} phần, {tot}s; {len(issues)} điểm cần xem")
for x in issues: print(" -", x)
