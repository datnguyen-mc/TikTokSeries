# Tây Du Ký 2026 — Tập 16: Cấm bóp còi thì… hét

**Ngày 16** · **⚡ Tập xu hướng ngày 04/11/2026** · Tập 30s = 3 clip × 10s · 9:16 · hoạt hình 2D · thoại tiếng Việt · không chữ trên video

**⚡ Vì sao hot:** từ 01/11/2026 thành phố Thâm Quyến (Trung Quốc) cấm ô tô bấm còi 24/24 trên mọi tuyến đường, phạt 300 NDT (khoảng 1 triệu đồng), dùng thiết bị dò âm thanh định vị xe bấm còi trong bán kính 80 m. Tài xế hạ kính hét to để xin đường, có người phát loa phóng thanh nhỏ qua cửa sổ, có người mang còi cổ vũ thể thao. VnExpress viết: "Trên mạng xã hội, nhiều người ví đường phố Thâm Quyến lúc này giống Hoa Quả Sơn" ([VnExpress, 03/11/2026 15:42](https://vnexpress.net/tai-xe-het-lon-de-xin-duong-vi-lenh-cam-bop-coi-5140225.html); [VOV](https://vov.vn/the-gioi/tham-quyen-trung-quoc-cam-o-to-bam-coi-toan-thanh-pho-2424-gio-post1341876.vov)). Dân mạng tự đem Hoa Quả Sơn, quê của Ngộ Không, ra so sánh, nên đây là tin hợp nhất với Tây Du Ký trong ngày. Kiểm tra lúc 04/11/2026.

**Đã quét và không chọn (04/11):** RSS Google Trends VN (bầu cử giữa kỳ Mỹ, CKTG Liên Minh Huyền Thoại IG vs TES, nhà máy giày 1.600 công nhân giải thể, đường sắt cao tốc, Hoắc Kiến Hoa): chính trị, game, người thật, tin buồn. Collins chọn "mogging" làm từ của năm 2026 ([Tuổi Trẻ 04/11](https://tuoitre.vn/mogging-la-gi-ma-duoc-chon-lam-tu-cua-nam-100261103220821155.htm)): để dành, hợp cho một tập "Thầy đẹp trai nhất nhà". Xăng, điện, gas, lương tối thiểu: Phèo tập 16 đã dùng.

> **Tập 16 cũ** (Nhờ bấm giùm điện thoại, 5 clip, tin ngày 02/11) chưa render clip nào và tin đã quá khung 24–48 giờ, nên được thay bằng tập này. Bản cũ còn trong git, commit `b144d4b`.

> **Cách dựng:** Clip 1: **Video → Gemini Omni → Ingredients**, 10s, đính `TDK_REF_GROUP` (hoặc `TDK_REF_DAICA_A`, `TDK_REF_HEOLUOI`), `TDK_REF_BACHMA`, `TDK_REF_LASAT`, `TDK_REF_THAY`, dán prompt. Clip 2, Clip 3: **Save frame** khung cuối clip trước → **Frames**, đặt làm **Start frame**, 10s, dán prompt (runner tự nối khung cuối). Ghép 3 clip trong Scenebuilder. Chi tiết: FLOW_GUIDE mục 1.
> **Copy prompt:** mỗi file `clip-{số}.md` chỉ chứa đúng prompt: mở file, bấm Cmd+A rồi Cmd+C, dán thẳng vào ô prompt của Flow, không sửa gì.
> **Khóa nhân vật, bối cảnh, ảnh tham chiếu:** [FLOW_PROMPTS.md](../FLOW_PROMPTS.md) · **Quy trình, xử lý lỗi:** [FLOW_GUIDE.md](../../FLOW_GUIDE.md)

← Hôm trước: [Tập 15 — Chùa online gõ mõ công đức & Bẫy cúng dường dỏm](../tap-15/README.md)

---

**Tóm tắt:** 10 giờ rưỡi đêm, Heo Lười chạy xe về tới hẻm với bịch hủ tiếu thì Bạch Mã nằm ngủ chắn ngang cổng. Heo Lười định bóp còi, Đại Ca thò gậy gạt tay: mười giờ đêm rồi, cấm bóp còi. Heo Lười giơ điện thoại: bên Thâm Quyến cấm còi thì người ta hét. Heo Lười hét "Tránh đường!", ngựa vẫn ngáy. Đại Ca chê nhỏ, biến thành cái loa vàng mặt khỉ rú một tiếng, cả hẻm bật đèn, chó sủa, gà gáy. La Sát mở cửa: "Tưởng Hoa Quả Sơn hả?" Thầy bước ra, vuốt cổ Bạch Mã, ngựa đứng dậy nhường đường không một tiếng động. Heo Lười mừng quá chồm tới, cái bụng đè trúng nút còi. La Sát quạt một phát, Heo Lười xoay vòng vô nhà.

**Phép chính:** 72 phép biến hóa, Đại Ca hóa loa vàng mặt khỉ (lấy ý từ tin tài xế Thâm Quyến phát loa qua cửa sổ). **Kiểu lật kèo:** cả tập giành nhau xin đường bằng tiếng ồn, người nói nhỏ nhất lại mở được đường, và cái bụng của Heo Lười bóp còi thay chủ.

**Bài học nhỏ đời thật:** Luật Trật tự, an toàn giao thông đường bộ 2024 quy định không sử dụng còi từ 22 giờ hôm trước đến 05 giờ hôm sau trong khu đông dân cư, khu vực cơ sở khám bệnh, chữa bệnh, trừ xe ưu tiên ([LSVN, 13/01/2025](https://lsvn.vn/quy-dinh-ve-su-dung-den-tin-hieu-coi-khi-tham-gia-giao-thong-a151640.html), bài dẫn Điều 21; [Báo Quốc tế](https://baoquocte.vn/khi-lai-xe-trong-khu-do-thi-va-dong-dan-cu-tru-cac-khu-vuc-co-bien-cam-su-dung-coi-nguoi-lai-xe-duoc-su-dung-coi-nhu-the-nao-292587.html) dẫn Điều 24; chưa mở được văn bản gốc để chốt số điều, nên caption chỉ ghi tên luật). Mức phạt xe máy theo Nghị định 168/2024 chưa kiểm được, nên không nói trong thoại hay caption.

## Kịch bản nhanh (30 giây)

| Giây | Hình | Thoại |
| --- | --- | --- |
| 0–2 | **Hook:** cận ngón tay Heo Lười sắp bấm còi, đầu gậy vàng thò vô gạt ra | — |
| 2–5 | Hẻm đêm, Bạch Mã ngủ chắn cổng, Đại Ca treo ngược trên ban công | Đại Ca: "Mười giờ đêm rồi, cấm bóp còi nghen!" |
| 5–8 | Heo Lười giơ điện thoại | Heo Lười: "Bên Thâm Quyến cấm còi, người ta hét nè!" |
| 8–10 | Heo Lười hít một hơi, bụng phồng như trái banh | — |
| 10–11,5 | Hét, sóng âm hoạt hình chạy dọc hẻm | Heo Lười: "Tránh đường!" |
| 11,5–14 | Ngựa vẫn ngáy; Đại Ca biến thành loa vàng mặt khỉ | Đại Ca: "Hét nhỏ xíu, coi Đại Ca nè!" |
| 14–16 | Loa rú, cả hẻm bật đèn, chó sủa, gà gáy | — |
| 16–18,5 | La Sát đập cửa bước ra | La Sát: "Mấy đứa! Tưởng Hoa Quả Sơn hả?" |
| 18,5–20 | La Sát giơ quạt, Đại Ca và Heo Lười đứng hình | — |
| 20–22,5 | Thầy vuốt cổ Bạch Mã, ngựa lặng lẽ đứng dậy nhường đường | — |
| 22,5–25 | Thầy cười hiền | Thầy: "Nói nhỏ là có đường mà, đồ nhi." |
| 25–26,5 | Heo Lười chồm tới, bụng đè nút còi: BÍÍP | — |
| 26,5–28,5 | Quạt bung "phạch" | Heo Lười: "Oan! Cái bụng bấm mà!" |
| 28,5–30 | Gió vàng thổi Heo Lười cùng chiếc xe xoay vòng vô nhà; khung thumbnail | — |

Thoại cả tập: 7 câu, 46 âm tiết, câu dài nhất 9 âm tiết. Mở bằng ngón tay sắp bấm còi, kết bằng cái bụng bấm còi.

## Các clip — mỗi file là nguyên một prompt, copy cả file dán vào Flow

| Clip | Thời gian | Cách tạo | File prompt |
| --- | --- | --- | --- |
| 1 | 00:00–00:10 | Ingredients (22:30): đính `TDK_REF_GROUP`, `TDK_REF_BACHMA`, `TDK_REF_LASAT`, `TDK_REF_THAY` | [clip-1.md](clip-1.md) |
| 2 | 00:10–00:20 | Frames: start frame = khung cuối clip 1 (La Sát xuất hiện, khóa đầy đủ trong prompt) | [clip-2.md](clip-2.md) |
| 3 | 00:20–00:30 | Frames: start frame = khung cuối clip 2 (Thầy xuất hiện, khóa đầy đủ trong prompt) | [clip-3.md](clip-3.md) |

**Bối cảnh:** dùng HẺM TRƯỚC NHÀ (mục 2.2 của bible) nhưng đổi sang ban đêm 22:30: cửa sổ trên lầu tắt đèn lúc đầu, đèn dây và ánh trăng. Chiếc xe tay ga xanh nhạt của Heo Lười và bịch hủ tiếu là đạo cụ riêng của tập.

- **Caption:** [caption.md](caption.md)
