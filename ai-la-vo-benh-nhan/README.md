# Ai Là Vợ Bệnh Nhân?

Phim ngắn gia đình – ngoại tình, hài chính kịch, một đêm ở bệnh viện. **23 cảnh · 304 shot · 24:47** (16:9, Omni 1.2 Flash 720p, khoảng 4461 tín dụng Flow).

- `CAU_CHUYEN.md` — cốt truyện, nhân vật, dàn ý 23 cảnh (mở · diễn biến · câu treo), gài – trả, câu thoại cắt short.
- `kich-ban/` — kịch bản từng cảnh (`canh-NN.md`) và bản chỉ có thoại (`KICH_BAN_THOAI.md`).
- `NHAN_VAT_FLOW.md` — nhân vật theo bộ đồ cần tạo trên Flow, kèm prompt ảnh mẫu và câu tả giọng.
- `film/SHOTS.md` — bảng shot: giây, nhân vật đính kèm, thoại. `film/cNN/NN-SS.txt` — prompt dán vào Flow cho từng shot. `film/shots.json` — cùng dữ liệu cho bước render.
- `film/clips/<shot>.mp4` — clip đã render. `FLOW_CLIPS.md` — nhật ký render (ID clip trên Flow).
- Nguồn: `_tools/phim.py` (nhân vật, bộ đồ, bối cảnh), `_tools/canh_a.py`, `canh_b.py`, `canh_c.py` (bảng shot). Sinh lại: `python3 ai-la-vo-benh-nhan/_tools/build.py`. Ghép phim: `python3 ai-la-vo-benh-nhan/_tools/ghep_phim.py [00 01 …]`.
