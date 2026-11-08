# Ma Da Đầm Sen: Lời Nguyền Tháng Bảy (15 Cảnh × 6 Clips × 10s = 15 Phút)

- **Giọng Người Dẫn Chuyện (cố định cả 90 clip):** Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, sharp resonant mid-baritone with crisp consonants, fluent late-night ghost-story delivery in one continuous breath, every word spoken once and clearly, no stutter, no repeated words. Mỗi clip VO dùng **nguyên văn cùng một câu mô tả giọng** để Omni giữ một giọng duy nhất; đọc nhanh liên thanh như oan-thai-doi-me, ~4.0 âm tiết/giây, liền một hơi, không ngắt giữa câu.
- **Thoại nhân vật (Lip-Sync):** clip thoại chỉ mô tả giọng của người nói, không có người dẫn chuyện; mặt và môi người nói luôn thấy rõ.
- **Mật độ:** 90 clips × 10s — 69 clip VO + 21 clip thoại; lời nói nằm trong khung riêng bắt đầu từ 0.4s (xem cột *Khung thoại*).
- **Cách tạo trên Flow (runner tự chọn):** 20 clip nối khung cuối (Frames — cùng bối cảnh, không có nhân vật mới), 58 clip ảnh nhân vật (Ingredients), 12 clip chỉ text. Tắt nối khung: `FLOWKIT_CHAIN_LAST_FRAME=0`.
- **Hậu kỳ runner:** clip VO được tăng tốc giọng thêm 1.18x khi tải về (`FLOWKIT_VOICE_TEMPO` mặc định 1.18, đặt 1.0 để tắt), giữ nguyên khung hình 10s; clip lip-sync không bao giờ bị tăng tốc để khớp khẩu hình.
- **Màu phim & ánh sáng:** Low-key cinematic mystery lighting: flickering amber oil-lamp, candle and incense light against cold cyan-green moonlight on black water and midnight-blue shade; daylight stays muted, hazy and desaturated.
- **Nguồn dữ liệu:** `PHAN_CANH_OMNI.json` → `python3 flowkit/scripts/build_omni_horror_prompts.py ma-da-dam-sen` sinh lại toàn bộ clip, README, kịch bản.

## Danh Sách 15 Cảnh (90 Clips × 10s)

| Cảnh | Tiêu Đề | Thời Gian | Đường Dẫn |
|---|---|---|---|
| **Cảnh 01** | Đầm Sen Đầu Làng & Bóng Áo Trắng Lúc Chạng Vạng | 18:00 Chạng vạng đầu tháng bảy âm lịch (00:00–01:00) | [`canh-01/`](canh-01/README.md) |
| **Cảnh 02** | Bữa Cơm Tối & Lời Dặn Của Bà Hạnh | 19:30 Tối tại nhà bà Hạnh (01:00–02:00) | [`canh-02/`](canh-02/README.md) |
| **Cảnh 03** | Tiếng Gọi Tên Lúc Nửa Đêm | 00:30 Nửa đêm đầu tiên (02:00–03:00) | [`canh-03/`](canh-03/README.md) |
| **Cảnh 04** | Dấu Chân Ướt & Lá Sen Trên Gối | 06:00 Sáng sớm hôm sau (03:00–04:00) | [`canh-04/`](canh-04/README.md) |
| **Cảnh 05** | Ông Lý & Chuyện Ma Da Bắt Thế Mạng | 09:00 Sáng tại nhà ông Lý và đình làng (04:00–05:00) | [`canh-05/`](canh-05/README.md) |
| **Cảnh 06** | Mâm Cúng Bên Bờ Đầm & Những Ngọn Nến Tắt | 21:00 Tối (05:00–06:00) | [`canh-06/`](canh-06/README.md) |
| **Cảnh 07** | Khôi Mất Tích Giữa Trưa | 12:00 Trưa hôm sau (06:00–07:00) | [`canh-07/`](canh-07/README.md) |
| **Cảnh 08** | Chuyện Năm Xưa Bà Hạnh Giấu Kín | 20:00 Đêm mưa (07:00–08:00) | [`canh-08/`](canh-08/README.md) |
| **Cảnh 09** | Đêm Mưa Ba Mươi Năm Trước | Hồi tưởng — đêm mưa tháng bảy ba mươi năm trước (08:00–09:00) | [`canh-09/`](canh-09/README.md) |
| **Cảnh 10** | Đêm Rằm Tháng Bảy — Đầm Sen Gọi Khôi | 23:30 Đêm rằm tháng bảy (09:00–10:00) | [`canh-10/`](canh-10/README.md) |
| **Cảnh 11** | Chiếc Hộp Trầu Đồng Khắc Hình Hạc | 00:30 Đêm rằm đến rạng sáng (10:00–11:00) | [`canh-11/`](canh-11/README.md) |
| **Cảnh 12** | Đêm Ông Lý Bị Gọi Tên | 01:00 Đêm hôm sau (11:00–12:00) | [`canh-12/`](canh-12/README.md) |
| **Cảnh 13** | Lời Thú Tội Trước Sân Đình | 08:00 Sáng hôm sau tại đình làng (12:00–13:00) | [`canh-13/`](canh-13/README.md) |
| **Cảnh 14** | Lễ Cầu Siêu & Đèn Hoa Đăng Trên Mặt Đầm | 20:00 Tối cầu siêu (13:00–14:00) | [`canh-14/`](canh-14/README.md) |
| **Cảnh 15** | Mùa Sen Năm Sau & Bóng Người Thứ Hai | Một năm sau — sáng đến đêm (14:00–15:00) | [`canh-15/`](canh-15/README.md) |
