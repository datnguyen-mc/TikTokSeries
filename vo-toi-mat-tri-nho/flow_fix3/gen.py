#!/usr/bin/env python3
"""Sửa 3 (19/11): bó 99 hồng đỏ Linh đặt lên bàn ở 01-10 phải còn trên bàn ở 01-11, 01-14, 01-16, 01-17."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROPS = ("[PROPS] Continuity: the candlelit table now holds one big bouquet of ninety-nine deep-red roses wrapped in cream paper with a red satin ribbon, "
         "lying on its side across one end of the white tablecloth with a few loose red petals — exactly as Linh just laid it down. "
         "The bouquet stays on the table, clearly visible whenever the table is in frame, for the whole shot. Also on the table: glass candle holders, white plates, wine glasses.")
EXTRA = (" Also avoid: an empty table without the rose bouquet; the bouquet disappearing, moving, shrinking or changing colour; pink flowers or a small bouquet; "
         "anyone holding flowers or wrapping paper; camera brand logos or recording overlays; black bars or rounded frame borders.")
ACT = {
 "01-11": ("[ACTION] Linh rises and walks to the glass balustrade, the emerald gown catching the candlelight; Tuan trails behind, hugging the empty wrapper.",
           "[ACTION] Linh steps away from the candlelit table — the red rose bouquet stays lying on it — and walks toward the glass balustrade, the emerald gown catching the candlelight; Tuan follows her, his tablet tucked under one arm, both hands empty of flowers. The table with the bouquet stays in the frame."),
 "01-14": ("[ACTION] Tuan leans over the rail, then spins to block her view, waving his hands.",
           "[ACTION] Tuan leans over the rail, then spins to block her view, waving his hands. Behind them, softly out of focus, the candlelit table with the red rose bouquet lying on it."),
 "01-16": ("[ACTION] Linh picks up her gold clutch and walks toward the brass elevator, never hurrying.",
           "[ACTION] Linh, seated at the candlelit table right beside the red rose bouquet lying on it, picks up her gold clutch, rises and walks toward the brass elevator, never hurrying; the bouquet stays on the table."),
 "01-17": ("[ACTION] Macro: as the clutch brushes past, Linh's untouched glass of red wine tips over; a dark red stain blooms across the white tablecloth and fills the frame.",
           "[ACTION] Macro: as the gold clutch brushes past, Linh's untouched glass of red wine, standing right beside the red rose bouquet, tips over; a dark red stain blooms across the white tablecloth among loose red petals, the roses and cream paper visible at the edge of the frame."),
}
ING = {"01-11": ["Bối cảnh · Sân thượng", "Linh · Dạ hội xanh", "Tuấn · Vest be"],
       "01-14": ["Bối cảnh · Sân thượng", "Tuấn · Vest be", "Linh · Dạ hội xanh"],
       "01-16": ["Bối cảnh · Sân thượng", "Linh · Dạ hội xanh"],
       "01-17": ["Bối cảnh · Sân thượng"]}
out = {}
for sid, (old, new) in ACT.items():
    t = open(os.path.join(ROOT, "flow_v3", "p01", sid + ".txt"), encoding="utf-8").read()
    assert old in t, sid
    t = t.replace(old, new)
    i = t.index("[CHARACTERS]"); t = t[:i] + PROPS + "\n\n" + t[i:]
    t = t.rstrip() + EXTRA + "\n"
    open(os.path.join(ROOT, "flow_fix3", sid + ".txt"), "w", encoding="utf-8").write(t)
    out[sid] = [ING[sid], t]
json.dump(out, open(os.path.join(ROOT, "flow_fix3", "fix3.json"), "w", encoding="utf-8"), ensure_ascii=False)
print({k: len(v[1]) for k, v in out.items()})
