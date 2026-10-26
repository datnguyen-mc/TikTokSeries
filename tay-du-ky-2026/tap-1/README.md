# Tây Du Ký 2026 — Tập 1: Ai ăn vụng hộp bánh?

**Ngày 1** · Tập 24s = 3 clip × 8s (bỏ clip 3 → 16s) · 9:16 · hoạt hình 2D · thoại tiếng Việt · không chữ trên video

> **Cách dựng:** Clip 1: **Video → Veo 3.1 → Ingredients**, đính ảnh tham chiếu (tối đa 3 ảnh), dán prompt → Clip 2 và 3: **Save frame** khung cuối clip trước → **Frames**, đặt ảnh đó làm **Start frame**, dán prompt → ghép 3 clip trong Scenebuilder. Chi tiết: FLOW_GUIDE mục 1.
> **Copy prompt:** mỗi file `clip-{số}.md` chỉ chứa đúng prompt: mở file, bấm Cmd+A rồi Cmd+C, dán thẳng vào ô prompt của Flow, không sửa gì.
> **Khóa nhân vật, bối cảnh, ảnh tham chiếu:** [FLOW_PROMPTS.md](../FLOW_PROMPTS.md) · **Quy trình, xử lý lỗi:** [FLOW_GUIDE.md](../../FLOW_GUIDE.md)

Hôm sau: [Tập 2 — Hóa đơn tiền điện](../tap-2/README.md) →

---

**Tóm tắt:** Út Khờ mở hộp bánh pía để dành thì chỉ còn vụn. Đại Ca lập tức "phá án", chĩa gậy vào Heo Lười đang dính vụn bánh đầy mõm. Heo Lười kêu oan: đó là vụn bánh phồng tôm! Bỗng một tiếng "rộp" vang lên từ góc thiền. Thầy từ từ xoay người lại, tay cầm miếng pía cuối cùng: "A Di Đà Phật... bánh chay mà. Ta tưởng đồ nhi cúng dường ta."

**Nhân vật & ảnh cần đính kèm:** `TDK_REF_UTKHO`, `TDK_REF_DAICA_A`, `TDK_REF_HEOLUOI`, `TDK_REF_THAY`. Nếu Flow giới hạn số ảnh thì đính một ảnh `TDK_REF_GROUP` thay cho cả bốn. Thầy ngồi quay lưng ở góc phòng ngay từ Clip 1, để model "nhớ" nhân vật cho cú twist ở Clip 3.

**Trang phục:** mặc định (Đại Ca biến thể A).

**Đạo cụ:** hộp bánh pía tròn bằng giấy màu kem (không in chữ), bánh pía vàng giòn, bịch bánh phồng tôm.

**Sản phẩm lồng ghép:** —

**Kịch bản nhanh:**

| Thời gian | Hình ảnh | Thoại |
| --- | --- | --- |
| 00:00–00:02 | Cận từ trên xuống: tay Út Khờ mở nắp hộp bánh pía, bên trong chỉ còn vụn và 4 tờ giấy lót trống | *(tiếng cồng)* |
| 00:02–00:04 | Cận mặt Út Khờ sững sờ, râu run run | Út Khờ: "Bánh pía của ta... đâu?" |
| 00:04–00:06 | Đại Ca lộn nhào từ nóc tủ lạnh xuống bàn trà, rút gậy Như Ý kéo dài ra | — |
| 00:06–00:08 | Đại Ca chĩa gậy vào Heo Lười đang nhai phồng má, mõm dính vụn; xa xa Thầy ngồi thiền quay lưng | Đại Ca: "Heo Lười! Khai mau!" |
| 00:08–00:11 | Đại Ca ghé sát mõm Heo Lười hít hít vụn bánh | Đại Ca: "Vụn bánh dính đầy mặt kìa!" |
| 00:11–00:13 | Út Khờ gật gù nghiêm trọng | Út Khờ: "Đại Ca nói phải." |
| 00:13–00:15 | Heo Lười giơ bịch phồng tôm, nhai rộp rộp để chứng minh | Heo Lười: "Oan! Vụn bánh phồng tôm mà!" |
| 00:15–00:16 | Một tiếng "rộp" vang lên từ góc thiền, cả ba đứng hình rồi từ từ quay đầu | — |
| 00:16–00:17 | Thầy từ từ xoay người trên bồ đoàn, tay cầm miếng pía cuối cùng | — |
| 00:17–00:22 | Thầy mở mắt, cười hiền, đặt tay lên ngực | Thầy: "A Di Đà Phật... bánh chay mà." · "Ta tưởng đồ nhi cúng dường ta." |
| 00:22–00:23 | Đại Ca ôm trán, Heo Lười há hốc làm rơi cả bánh phồng tôm, Út Khờ rưng rưng cúi đầu | Út Khờ: "Thầy... nói phải." |
| 00:23–00:24 | Thầy hiền từ chìa nửa miếng bánh cho Út Khờ (khung thumbnail) | — |

## Các clip — mỗi file là nguyên một prompt, copy cả file dán vào Flow

| Clip | Thời gian | Cách tạo | File prompt |
| --- | --- | --- | --- |
| 1 | 00:00–00:08 | Ingredients: đính ảnh tham chiếu | [clip-1.md](clip-1.md) |
| 2 | 00:08–00:16 | Frames: start frame = khung cuối clip 1 | [clip-2.md](clip-2.md) |
| 3 | 00:16–00:24 | Frames: start frame = khung cuối clip 2 | [clip-3.md](clip-3.md) |
