# Tây Du Ký 2026 — Tập 1: Ai ăn vụng hộp bánh?

**Ngày 1** · Tập 30s = 3 clip × 10s (bỏ clip 3 → 20s) · 9:16 · thoại tiếng Việt · không chữ trên video

> **Cách dựng:** Clip 1: **Video → Gemini Omni → Ingredients**, độ dài 10s, đính ảnh tham chiếu, dán prompt → Clip 2 và 3: **Save frame** khung cuối clip trước → **Frames**, đặt ảnh đó làm **Start frame**, độ dài 10s, dán prompt → ghép 3 clip trong Scenebuilder. Nếu Flow đã có **Extend** cho Omni: bấm Extend trên clip trước rồi dán prompt clip sau, khỏi ghép. Chi tiết: FLOW_GUIDE mục 1.
> **Copy prompt:** mỗi file `clip-{số}.md` chỉ chứa đúng prompt: mở file, bấm Cmd+A rồi Cmd+C, dán thẳng vào ô prompt của Flow, không sửa gì.
> **Khóa nhân vật, bối cảnh, ảnh tham chiếu:** [FLOW_PROMPTS.md](../FLOW_PROMPTS.md) · **Quy trình, xử lý lỗi:** [FLOW_GUIDE.md](../../FLOW_GUIDE.md)

Hôm sau: [Tập 2 — Hóa đơn tiền điện](../tap-2/README.md) →

---

**Tóm tắt:** Sa Tăng mở hộp bánh pía để dành thì chỉ còn vụn. Ngộ Không lập tức "phá án", chĩa gậy vào Bát Giới đang dính vụn bánh đầy mõm. Bát Giới kêu oan: đó là vụn bánh phồng tôm! Bỗng một tiếng "rộp" vang lên từ góc thiền. Sư phụ từ từ xoay người lại, tay cầm miếng pía cuối cùng: "A Di Đà Phật... bánh chay mà. Ta tưởng đồ nhi cúng dường ta."

**Nhân vật & ảnh cần đính kèm:** `TDK_REF_SATANG`, `TDK_REF_NGOKHONG_A`, `TDK_REF_BATGIOI`, `TDK_REF_SUPHU`. Nếu Flow giới hạn số ảnh thì đính một ảnh `TDK_REF_GROUP` thay cho cả bốn. Sư phụ ngồi quay lưng ở góc phòng ngay từ Clip 1, để model "nhớ" nhân vật cho cú twist ở Clip 3.

**Trang phục:** mặc định (Ngộ Không biến thể A).

**Đạo cụ:** hộp bánh pía tròn bằng giấy màu kem (không in chữ), bánh pía vàng giòn, bịch bánh phồng tôm.

**Sản phẩm lồng ghép:** —

**Kịch bản nhanh:**

| Thời gian | Hình ảnh | Thoại |
| --- | --- | --- |
| 00:00–00:02 | Cận từ trên xuống: tay Sa Tăng mở nắp hộp bánh pía, bên trong chỉ còn vụn và 4 tờ giấy lót trống | *(tiếng cồng)* |
| 00:02–00:05 | Cận mặt Sa Tăng sững sờ, râu run run | Sa Tăng: "Bánh pía của ta... đâu?" |
| 00:05–00:07 | Ngộ Không lộn nhào từ nóc tủ lạnh xuống bàn trà, rút gậy Như Ý kéo dài ra | — |
| 00:07–00:09 | Ngộ Không chĩa gậy vào Bát Giới đang nhai phồng má, mõm dính vụn | Ngộ Không: "Bát Giới! Khai mau!" |
| 00:09–00:10 | Bát Giới đứng hình, má còn phồng; xa xa Sư phụ ngồi thiền quay lưng | — |
| 00:10–00:13 | Ngộ Không ghé sát mõm Bát Giới hít hít vụn bánh | Ngộ Không: "Vụn bánh dính đầy mặt kìa!" |
| 00:13–00:15.5 | Sa Tăng gật gù nghiêm trọng | Sa Tăng: "Đại sư huynh nói phải." |
| 00:15.5–00:18 | Bát Giới giơ bịch phồng tôm, nhai rộp rộp để chứng minh | Bát Giới: "Oan! Vụn bánh phồng tôm mà!" |
| 00:18–00:20 | Một tiếng "rộp" vang lên từ góc thiền, cả ba đứng hình rồi từ từ quay đầu | — |
| 00:20–00:22 | Sư phụ từ từ xoay người trên bồ đoàn, tay cầm miếng pía cuối cùng | — |
| 00:22–00:24.5 | Sư phụ mở mắt, cười hiền, đặt tay lên ngực | Sư phụ: "A Di Đà Phật... bánh chay mà." |
| 00:24.5–00:27 | Sư phụ vẫn đặt tay lên ngực, cười ngây thơ | Sư phụ: "Ta tưởng đồ nhi cúng dường ta." |
| 00:27–00:28.5 | Ngộ Không ôm trán, Bát Giới há hốc làm rơi cả bánh phồng tôm, Sa Tăng rưng rưng cúi đầu | Sa Tăng: "Sư phụ... nói phải." |
| 00:28.5–00:30 | Sư phụ hiền từ chìa nửa miếng bánh cho Sa Tăng (khung thumbnail) | — |

## Các clip — mỗi file là nguyên một prompt, copy cả file dán vào Flow

| Clip | Thời gian | Cách tạo | File prompt |
| --- | --- | --- | --- |
| 1 | 00:00–00:10 | Ingredients: đính ảnh tham chiếu | [clip-1.md](clip-1.md) |
| 2 | 00:10–00:20 | Frames: start frame = khung cuối clip 1 | [clip-2.md](clip-2.md) |
| 3 | 00:20–00:30 | Frames: start frame = khung cuối clip 2 | [clip-3.md](clip-3.md) |
