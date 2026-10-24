# Nhà Tèo & Sún — Tập 1: Lần đầu làm cha

**Ngày 1** · Tập 30s = 3 clip × 10s (bỏ clip 3 → 20s) · 9:16 · thoại tiếng Việt · không chữ trên video

> **Cách dựng:** Clip 1: **Video → Gemini Omni → Ingredients**, độ dài 10s, đính ảnh tham chiếu, dán prompt → Clip 2 và 3: **Save frame** khung cuối clip trước → **Frames**, đặt ảnh đó làm **Start frame**, độ dài 10s, dán prompt → ghép 3 clip trong Scenebuilder. Nếu Flow đã có **Extend** cho Omni: bấm Extend trên clip trước rồi dán prompt clip sau, khỏi ghép. Chi tiết: FLOW_GUIDE mục 1.
> **Copy prompt:** mỗi file `clip-{số}.md` chỉ chứa đúng prompt: mở file, bấm Cmd+A rồi Cmd+C, dán thẳng vào ô prompt của Flow, không sửa gì.
> **Khóa nhân vật, bối cảnh, ảnh tham chiếu:** [FLOW_PROMPTS.md](../FLOW_PROMPTS.md) · **Quy trình, xử lý lỗi:** [FLOW_GUIDE.md](../../FLOW_GUIDE.md)

Hôm sau: [Tập 2 — Quà 20/10 bất ngờ](../tap-2/README.md) →

---

**Tóm tắt:** Nửa đêm bé khóc, Tèo giành phần dỗ con để Sún ngủ tiếp. Lúc vỗ ợ hơi, bé ọc sữa lên vai ba; Tèo rút giấy Top Gia mềm mịn lau miệng cho con. Sáng ra, Sún thấy chồng ngủ gục trên ghế bập bênh, tay vẫn ôm chặt con; cô đắp chăn, hôn trán chồng, và Tèo nói mớ "Để anh lo…".
**Nhân vật & ảnh cần đính kèm:** Clip 1: `TEO_A.png` · `SUN.png` · `BABY.png` · `SP_TOPGIA.png`. Clip 2–3 (Frames): start frame là khung cuối của clip trước; nếu Flow cho đính thêm ảnh thì đính lại đủ 4 ảnh.
**Trang phục:** Tèo biến thể A · Sún đồ bộ xanh bạc hà · bé quấn khăn vàng.
**Sản phẩm lồng ghép:** Giấy ăn Top Gia, gói giấy mềm trên bàn nhỏ cạnh ghế bập bênh. Tèo rút giấy và nói tên sản phẩm ở 00:15–00:17; gói giấy còn hiện mờ ở khung cuối.

**Kịch bản nhanh:**

| Thời gian | Hình ảnh | Thoại |
| --- | --- | --- |
| 00:00–00:02 | Đêm, cận mặt Tèo đang ngủ; bé khóc, hai tai Tèo bật dựng như ăng-ten | — |
| 00:02–00:04 | Sún lơ mơ ngồi dậy | Sún: "Anh dỗ được không đó?" |
| 00:04–00:06 | Tèo nhẹ ấn vai vợ nằm xuống, kéo chăn | Tèo: "Em ngủ đi, để anh lo." |
| 00:06–00:08 | Sún ngủ tiếp; Tèo nhón chân tới nôi, dép kêu chút chít, nhăn mặt | — |
| 00:08–00:10 | Tèo bế bé đang khóc lên khỏi nôi | Tèo: "Ba đây, ba đây con." |
| 00:10–00:13.5 | Ngồi ghế bập bênh, đặt bé lên vai, vỗ lưng | Tèo: "Ợ một cái nè con." |
| 00:13.5–00:15 | Bé ọc chút sữa lên vai áo, Tèo đứng hình, tai cụp | — |
| 00:15–00:17 | Rút tờ giấy Top Gia mềm mịn từ gói trên bàn nhỏ | Tèo: "Có giấy Top Gia mềm mịn đây." |
| 00:17–00:20 | Nhẹ nhàng lau miệng cho bé; bé nín, nhìn ba | Tèo: "Êm ru, không rát da con." |
| 00:20–00:22.5 | Ánh sáng chuyển từ đêm sang sáng; Tèo ngủ gục, vẫn ôm chặt con | — |
| 00:22.5–00:24.5 | Sún thức dậy, nhìn sang, mỉm cười xúc động | — |
| 00:24.5–00:27 | Sún đắp chăn len cho hai cha con | Sún: "Ông xã nhà mình giỏi ghê." |
| 00:27–00:28.5 | Sún hôn trán Tèo; Tèo cười trong mơ | Tèo (nói mớ): "Để anh lo…" |
| 00:28.5–00:30 | Sún nén cười, tựa má lên vai chồng → khung cuối | — |

## Các clip — mỗi file là nguyên một prompt, copy cả file dán vào Flow

| Clip | Thời gian | Cách tạo | File prompt |
| --- | --- | --- | --- |
| 1 | 00:00–00:10 | Ingredients: đính ảnh tham chiếu | [clip-1.md](clip-1.md) |
| 2 | 00:10–00:20 | Frames: start frame = khung cuối clip 1 | [clip-2.md](clip-2.md) |
| 3 | 00:20–00:30 | Frames: start frame = khung cuối clip 2 | [clip-3.md](clip-3.md) |

**Ghi chú Tập 1:**
- Nếu model đọc "Top Gia" chưa chuẩn, lồng tiếng lại riêng câu ở 00:15–00:17.
- Clip 3 chuyển ánh sáng đêm → sáng ngay trong cùng một khung hình. Nếu model tự cắt cảnh đột ngột, tạo lại clip đó; khung cuối vẫn dùng được.
