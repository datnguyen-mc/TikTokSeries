# Nhà Tèo & Sún — Tập 3: Tèo giặt đồ lần đầu

**Ngày 3** · Tập 30s = 3 clip × 10s (bỏ clip 3 → 20s) · 9:16 · thoại tiếng Việt · không chữ trên video

> **Cách dựng:** Clip 1: **Video → Gemini Omni → Ingredients**, độ dài 10s, đính ảnh tham chiếu, dán prompt → Clip 2 và 3: **Save frame** khung cuối clip trước → **Frames**, đặt ảnh đó làm **Start frame**, độ dài 10s, dán prompt → ghép 3 clip trong Scenebuilder. Nếu Flow đã có **Extend** cho Omni: bấm Extend trên clip trước rồi dán prompt clip sau, khỏi ghép. Chi tiết: FLOW_GUIDE mục 1.
> **Copy prompt:** mỗi file `clip-{số}.md` chỉ chứa đúng prompt: mở file, bấm Cmd+A rồi Cmd+C, dán thẳng vào ô prompt của Flow, không sửa gì.
> **Khóa nhân vật, bối cảnh, ảnh tham chiếu:** [FLOW_PROMPTS.md](../FLOW_PROMPTS.md) · **Quy trình, xử lý lỗi:** [FLOW_GUIDE.md](../../FLOW_GUIDE.md)

← Hôm trước: [Tập 2 — Quà 20/10 bất ngờ](../tap-2/README.md) · Hôm sau: [Tập 4 — Tèo rửa chén](../tap-4/README.md) →

---

**Tóm tắt:** Giữ lời hứa ở Tập 2, Tèo hùng hồn ra ban công giặt đồ và đổ gần hết chai nước giặt "cho sạch". Bọt trào thành sóng phủ kín ban công. Sún chạy ra, chỉ Tèo dùng đúng một nắp. Ít lâu sau quần áo thơm phức, Sún khen "Ông xã giỏi ghê!".
**Nhân vật & ảnh cần đính kèm:** Clip 1: `TEO_A.png` · `SUN.png` · `SP_NUOCGIAT.png`. Clip 2–3 (Frames): start frame là khung cuối của clip trước; nếu Flow cho đính thêm ảnh thì đính lại đủ 3 ảnh.
**Trang phục:** Tèo biến thể A · Sún đồ bộ xanh bạc hà.
**Sản phẩm lồng ghép:** Nước giặt. Tèo giơ chai như cúp ở 00:00–00:02.5, Sún hướng dẫn dùng một nắp ở 00:20–00:25, chai đứng trên máy giặt ở khung cuối.

**Kịch bản nhanh:**

| Thời gian | Hình ảnh | Thoại |
| --- | --- | --- |
| 00:00–00:02.5 | Góc thấp, Tèo đứng trên ghế nhựa, giơ chai nước giặt như cúp vô địch | Tèo: "Giặt đồ hả? Chuyện nhỏ!" |
| 00:02.5–00:05 | Trút nguyên rổ đồ (có đồ sơ sinh màu vàng) vào lồng giặt; Sún nhìn qua cửa kính, lắc đầu bỏ đi | — |
| 00:05–00:08 | Nhắm mắt đổ nước giặt ồ ạt, đổ mãi không dừng | Tèo: "Bỏ nhiều cho sạch nè!" |
| 00:08–00:10 | Đóng nắp, bấm nút, chống nạnh tự hào | — |
| 00:10–00:12 | Máy rung, bọt rỉ ra; Tèo không hay biết, giơ ngón cái | — |
| 00:12–00:15 | Bọt trào thành sóng phủ kín ban công, Tèo té ngồi | Tèo: "Ủa ủa! Bọt đâu ra vậy?!" |
| 00:15–00:17.5 | Sún chạy ra cửa kính, sững người | Sún: "Trời ơi, anh Tèo!" |
| 00:17.5–00:20 | Tèo ngập bọt tới ngực, bong bóng trên mũi, vớ em bé dính trên tai | Tèo: "Anh… bỏ hơi nhiều." |
| 00:20–00:23 | Sún bấm dừng máy, giơ nắp đong trước mặt Tèo | Sún: "Một nắp thôi, anh ơi!" |
| 00:23–00:25 | Sún đổ đúng một nắp; Tèo gật gù như học trò | Tèo: "Dạ, một nắp thôi!" |
| 00:25–00:28 | Ít lâu sau: ban công sạch, Tèo hít bộ đồ sơ sinh thơm, Sún ngửi theo | Sún: "Thơm ghê! Ông xã giỏi ghê!" |
| 00:28–00:30 | Phơi đồ, Sún tựa vai Tèo, đồ bay trong nắng → khung cuối | — |

## Các clip — mỗi file là nguyên một prompt, copy cả file dán vào Flow

| Clip | Thời gian | Cách tạo | File prompt |
| --- | --- | --- | --- |
| 1 | 00:00–00:10 | Ingredients: đính ảnh tham chiếu | [clip-1.md](clip-1.md) |
| 2 | 00:10–00:20 | Frames: start frame = khung cuối clip 1 | [clip-2.md](clip-2.md) |
| 3 | 00:20–00:30 | Frames: start frame = khung cuối clip 2 | [clip-3.md](clip-3.md) |

**Ghi chú Tập 3:**
- Sún chỉ thoáng hiện sau cửa kính ở Clip 1 để model "nhớ" mặt cô cho Clip 2–3. Đừng xóa chi tiết này.
- Cú cắt ở 00:25 là cố ý (tua nhanh tới lúc đồ giặt xong).
- Muốn nhắc thương hiệu: thay câu ở 00:25–00:28 thành "Nước giặt [tên] thơm ghê!"
