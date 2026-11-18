"""Nén prompt flow_15s (P4–P25) thành từ điển macro + phần riêng, để dán vào trình duyệt ít ký tự hơn."""
import json, os, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
m = json.load(open(os.path.join(ROOT, "flow_15s", "manifest.json"), encoding="utf-8"))
todo = [c for c in m if c["part"] >= int(sys.argv[1] if len(sys.argv) > 1 else 4)]
texts = {c["id"]: open(os.path.join(ROOT, "flow_15s", f"p{c['part']:02d}", f"{c['id']}.txt"), encoding="utf-8").read().strip() for c in todo}
# macro = mọi dòng (hoặc đoạn trong ngoặc) lặp lại >= 2 lần
cnt = collections.Counter()
for t in texts.values():
    for ln in t.split("\n"):
        if len(ln) > 40: cnt[ln] += 1
    # mô tả giọng trong ngoặc
    import re
    for g in re.findall(r"\((?:wo)?man of \d+[^)]*?diction|\((?:wo)?man of \d+, [^,]+, [^,]+(?:, [^,]+)?", t):
        pass
lines = [ln for ln, k in cnt.items() if k >= 2]
macro = {ln: f"§{i}§" for i, ln in enumerate(sorted(lines, key=len, reverse=True))}
# thêm macro cho mô tả giọng
sys.path.insert(0, HERE)
from looks import VOICE
k = len(macro)
vmac = {}
for name, v in VOICE.items():
    vmac[v] = f"¤{name}¤"
out = {}
for cid, t in texts.items():
    L = []
    for ln in t.split("\n"):
        if ln in macro: L.append(macro[ln])
        else:
            for v, tok in vmac.items(): ln = ln.replace(v, tok)
            L.append(ln)
    out[cid] = "\n".join(L)
dic = {v: k for k, v in macro.items()}
dic.update({tok: v for v, tok in vmac.items()})
json.dump({"dic": dic, "clips": out}, open("/tmp/compact.json", "w"), ensure_ascii=False)
print("orig", sum(len(t) for t in texts.values()), "dict", sum(len(v) for v in dic.values()), "clips", sum(len(v) for v in out.values()), "n", len(out))
# kiểm tra giải nén
import re
def expand(s):
    return re.sub(r"§\d+§|¤\w+¤", lambda mm: dic[mm.group(0)], s)
assert all(expand(out[c]) == texts[c] for c in texts)
print("roundtrip ok")
