#!/usr/bin/env python3
"""Sinh toàn bộ file sản xuất của phim "Ai Là Vợ Bệnh Nhân?" từ phim.py và canh_a/b/c.py.
Chạy từ gốc repo:  python3 ai-la-vo-benh-nhan/_tools/build.py
→ NHAN_VAT_FLOW.md · film/cNN/NN-SS.txt · film/SHOTS.md · film/shots.json · kich-ban/ · README.md"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import phim as P
import canh_a
import canh_b
import canh_c

SCENES = {}
for m in (canh_a, canh_b, canh_c):
    SCENES.update(m.SCENES)

CREDIT_PER_SEC = 3   # Omni 1.2 Flash, 720p, x1 (đo trên các phim trước)


def mmss(s):
    return f"{int(s) // 60}:{int(s) % 60:02d}"


def check(sc, s, errs):
    code, name, dur, place, looks, cam, action, lines, extra = s
    if not code.startswith(sc + "-"):
        errs.append(f"{code}: mã shot không thuộc cảnh {sc}")
    if place not in P.PLACES or place not in P.SOUND:
        errs.append(f"{code}: thiếu bối cảnh/âm thanh {place}")
    if not 2 <= dur <= 8:
        errs.append(f"{code}: thời lượng {dur}s ngoài khoảng 2–8s")
    if len(looks) > 2:
        errs.append(f"{code}: quá 2 nhân vật đính kèm")
    for c in looks:
        if c not in P.LOOK:
            errs.append(f"{code}: không có bộ đồ {c}")
    if len({P.LOOK[c]['person'] for c in looks if c in P.LOOK}) != len(looks):
        errs.append(f"{code}: một người xuất hiện hai lần")
    for ln in lines:
        if ln[0] not in (P.X, P.PH) and ln[0] not in looks:
            errs.append(f"{code}: người nói {ln[0]} không có trong khung")
    if '"' in action or '"' in cam:
        errs.append(f"{code}: có ngoặc kép trong prompt")


def main():
    errs, warns, js = [], [], []
    used = {c: [] for c in P.LOOK}
    shots_md = [f"# {P.TEN_PHIM} — Bảng shot", "",
                "*Sinh bởi `_tools/build.py`.* Flow: **Video → Thành phần**, Omni 1.2 Flash, 720p, 16:9, x1. "
                "Mỗi shot đính đúng các nhân vật ở cột *Đính* rồi dán nguyên `film/cNN/<shot>.txt`. "
                "Tên clip trên Flow: `VBN <shot> · <tên>`. Clip tải về đặt ở `film/clips/<shot>.mp4`.", ""]
    index = []
    thoai = [f"# {P.TEN_PHIM} — Kịch bản thoại", "",
             "*Sinh bởi `_tools/build.py`.* Bản đọc nhanh: chỉ có tên shot và lời thoại, theo đúng thứ tự dựng.", ""]
    total = 0
    for sc, S in SCENES.items():
        shots = S["shots"]
        secs = sum(s[2] for s in shots)
        looks_sc = []
        shots_md += [f"## Cảnh {sc} · {S['ten']} · {S['noi']} · {S['gio']}", "",
                     "| Shot | Giây | Đính | Thoại |", "|---|---|---|---|"]
        kb = [f"# Cảnh {sc} · {S['ten']}", "",
              f"*Sinh bởi `_tools/build.py`.* **{S['hoi']}** · {S['noi']} · {S['gio']} · {len(shots)} shot · {secs} giây "
              f"(bắt đầu ở phút {mmss(total)}).", "",
              "| Shot | Giây | Trong khung | Máy quay | Hành động | Thoại |", "|---|---|---|---|---|---|"]
        thoai += [f"## Cảnh {sc} · {S['ten']}", f"*{S['noi']} · {S['gio']} · phút {mmss(total)}*", ""]
        for s in shots:
            code, name, dur, place, looks, cam, action, lines, extra = s
            check(sc, s, errs)
            w = []
            p = P.prompt(s, w)
            warns += [f"{code}: {x}" for x in w]
            P.write(f"film/c{sc}/{code}.txt", p)
            for c in looks:
                if sc not in used[c]:
                    used[c].append(sc)
                if c not in looks_sc:
                    looks_sc.append(c)
            dinh = ", ".join(P.LOOK[c]["flow"] for c in looks) or "— (Text-to-Video)"
            loi = " / ".join(f"{P.speaker_vn(ln[0])}: {ln[1]}" for ln in lines)
            shots_md.append(f"| {code} · {name} | {dur} | {dinh} | {loi} |")
            kb.append(f"| {code} · {name} | {dur} | {dinh} | {cam} | {action} | {loi or '—'} |")
            if lines:
                for ln in lines:
                    thoai.append(f"- **{P.speaker_vn(ln[0])}:** {ln[1]}  ·  *{code}*")
            else:
                thoai.append(f"- *({name})*  ·  *{code}*")
            js.append(dict(code=code, name=name, dur=dur, scene=sc, refs=[P.LOOK[c]["flow"] for c in looks],
                           flow_name=f"VBN {code} · {name}", prompt=" ".join(p.split())))
        shots_md += ["", f"*{len(shots)} shot · {secs} giây*", ""]
        thoai.append("")
        kb += ["", "Bộ đồ dùng trong cảnh: " + ", ".join(f"{c} ({P.LOOK[c]['flow']})" for c in looks_sc) + "."]
        P.write(f"kich-ban/canh-{sc}.md", "\n".join(kb) + "\n")
        index.append((sc, S, len(shots), secs, total))
        total += secs

    n = len(js)
    gaps = 0.6 * (len(SCENES) - 1)
    shots_md.append(f"**Tổng {n} shot, {total} giây = {mmss(total)} (cộng {gaps:.0f} giây đen giữa các cảnh ≈ {mmss(total + gaps)}); "
                    f"khoảng {total * CREDIT_PER_SEC} tín dụng ở 720p.**")
    P.write("film/SHOTS.md", "\n".join(shots_md) + "\n")
    P.write("film/shots.json", json.dumps(js, ensure_ascii=False, indent=0))
    P.write("kich-ban/KICH_BAN_THOAI.md", "\n".join(thoai) + "\n")

    # kich-ban/README.md
    R = [f"# {P.TEN_PHIM} — Kịch bản từng cảnh", "",
         "*Sinh bởi `_tools/build.py` từ `_tools/canh_a.py`, `canh_b.py`, `canh_c.py`. Sửa trong script rồi chạy lại.*", "",
         f"**{len(SCENES)} cảnh · {n} shot · {mmss(total)}.** Bản đọc nhanh chỉ có thoại: [KICH_BAN_THOAI.md](KICH_BAN_THOAI.md).", "",
         "| Cảnh | Tên | Hồi | Giờ trong truyện | Bối cảnh | Shot | Giây | Bắt đầu |", "|---|---|---|---|---|---|---|---|"]
    for sc, S, k, secs, start in index:
        R.append(f"| [{sc}](canh-{sc}.md) | {S['ten']} | {S['hoi']} | {S['gio']} | {S['noi']} | {k} | {secs} | {mmss(start)} |")
    P.write("kich-ban/README.md", "\n".join(R) + "\n")

    # NHAN_VAT_FLOW.md
    L = [f"# {P.TEN_PHIM} — Nhân vật theo bộ đồ trên Flow", "",
         "*Sinh bởi `_tools/build.py`. Sửa trong `_tools/phim.py` rồi chạy lại, không sửa tay file này.*", "",
         "Mỗi bộ đồ là **một nhân vật riêng trên Flow**, đặt đúng tên ở cột *Tên trên Flow*. Thứ tự tạo: (1) tạo **bộ đồ gốc** "
         "của từng người bằng prompt đầy đủ (đánh dấu ★); (2) các bộ còn lại: đính ảnh bộ gốc làm tham chiếu và dùng *Prompt sửa* "
         "để giữ nguyên khuôn mặt. Giọng không gắn preset: câu tả giọng dưới đây được chép nguyên văn vào mọi prompt có thoại.", "",
         "## Khóa mặt và giọng", "", "| Tag | Nhân vật | Khuôn mặt | Giọng |", "|---|---|---|---|"]
    for k, p in P.PEOPLE.items():
        L.append(f"| `{k}` | {p['vn']} | {p['face']} | {p['voice']} |")
    L += ["", f"## {len(P.LOOKS)} nhân vật theo bộ đồ", "",
          "| Mã | Tên trên Flow | Cảnh dùng | Ghi chú | Prompt sửa (từ ảnh gốc) | Prompt đầy đủ |", "|---|---|---|---|---|---|"]
    for c, *_ in P.LOOKS:
        lk = P.LOOK[c]
        star = " ★" if P.BASE.get(lk["person"]) == c else ""
        L.append(f"| {c}{star} | {lk['flow']} | {', '.join(used[c]) or '—'} | {lk['note']} | "
                 f"{'— (tạo bằng prompt đầy đủ)' if star else P.edit_prompt(c)} | {P.ref_prompt(c)} |")
        if not used[c]:
            warns.append(f"bộ đồ {c} không dùng trong shot nào")
    L += ["", "## Cảnh nào dùng bộ nào", "", "| Cảnh | Bộ đồ |", "|---|---|"]
    for sc in SCENES:
        L.append(f"| {sc} | {', '.join(c for c in P.LOOK if sc in used[c])} |")
    P.write("NHAN_VAT_FLOW.md", "\n".join(L) + "\n")

    # README.md
    M = [f"# {P.TEN_PHIM}", "",
         f"Phim ngắn gia đình – ngoại tình, hài chính kịch, một đêm ở bệnh viện. **{len(SCENES)} cảnh · {n} shot · {mmss(total)}** "
         f"(16:9, Omni 1.2 Flash 720p, khoảng {total * CREDIT_PER_SEC} tín dụng Flow).", "",
         "- `CAU_CHUYEN.md` — cốt truyện, nhân vật, dàn ý 23 cảnh (mở · diễn biến · câu treo), gài – trả, câu thoại cắt short.",
         "- `kich-ban/` — kịch bản từng cảnh (`canh-NN.md`) và bản chỉ có thoại (`KICH_BAN_THOAI.md`).",
         "- `NHAN_VAT_FLOW.md` — nhân vật theo bộ đồ cần tạo trên Flow, kèm prompt ảnh mẫu và câu tả giọng.",
         "- `film/SHOTS.md` — bảng shot: giây, nhân vật đính kèm, thoại. `film/cNN/NN-SS.txt` — prompt dán vào Flow cho từng shot. "
         "`film/shots.json` — cùng dữ liệu cho bước render.",
         "- `film/clips/<shot>.mp4` — clip đã render. `FLOW_CLIPS.md` — nhật ký render (ID clip trên Flow).",
         "- Nguồn: `_tools/phim.py` (nhân vật, bộ đồ, bối cảnh), `_tools/canh_a.py`, `canh_b.py`, `canh_c.py` (bảng shot). "
         "Sinh lại: `python3 ai-la-vo-benh-nhan/_tools/build.py`. Ghép phim: `python3 ai-la-vo-benh-nhan/_tools/ghep_phim.py [00 01 …]`.", ""]
    P.write("README.md", "\n".join(M))

    for e in errs:
        print("LỖI  ", e)
    for w in warns:
        print("  !  ", w)
    print(f"{len(SCENES)} cảnh · {n} shot · {total} giây = {mmss(total)} · ~{total * CREDIT_PER_SEC} tín dụng")
    for sc, S, k, secs, start in index:
        print(f"  {sc} {mmss(start):>6}  {k:2d} shot {secs:3d}s  {S['ten']}")
    if errs:
        sys.exit(1)


if __name__ == "__main__":
    main()
