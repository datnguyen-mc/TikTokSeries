# Găng Tơ Tái Xuất (27 Cảnh × 6 Clips × 10s = 27 Phút)

- **Giọng Người Dẫn Chuyện (cố định cả 162 clip):** Vietnamese man about 45, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm punchy baritone with a playful knowing edge, fast witty caper-film storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words. Mỗi clip VO dùng **nguyên văn cùng một câu mô tả giọng** để Omni giữ một giọng duy nhất; đọc nhanh liên thanh như oan-thai-doi-me, ~4.0 âm tiết/giây, liền một hơi, không ngắt giữa câu.
- **Thoại nhân vật (Lip-Sync):** clip thoại chỉ mô tả giọng của người nói, không có người dẫn chuyện; mặt và môi người nói luôn thấy rõ.
- **Mật độ:** 162 clips × 10s — 102 clip VO + 60 clip thoại; lời nói nằm trong khung riêng bắt đầu từ 0.4s (xem cột *Khung thoại*).
- **Cách tạo trên Flow (runner tự chọn):** 45 clip nối khung cuối (Frames — cùng bối cảnh, không có nhân vật mới), 96 clip ảnh nhân vật (Ingredients), 21 clip chỉ text. Tắt nối khung: `FLOWKIT_CHAIN_LAST_FRAME=0`.
- **Hậu kỳ runner:** clip VO được tăng tốc giọng thêm 1.18x khi tải về (`FLOWKIT_VOICE_TEMPO` mặc định 1.18, đặt 1.0 để tắt), giữ nguyên khung hình 10s; clip lip-sync không bao giờ bị tăng tốc để khớp khẩu hình.
- **Màu phim & ánh sáng:** Bright natural lighting: warm golden morning and sunset light over the old quarter, crisp midday daylight, colorful neon signs without readable letters and warm shop lamps at night; shadows stay soft, never gloomy.
- **Nguồn dữ liệu:** `PHAN_CANH_OMNI.json` → `python3 flowkit/scripts/build_omni_horror_prompts.py gang-to-tai-xuat` sinh lại toàn bộ clip, README, kịch bản.

## Danh Sách 27 Cảnh (162 Clips × 10s)

| Cảnh | Tiêu Đề | Thời Gian | Đường Dẫn |
|---|---|---|---|
| **Cảnh 01** | Ông Xe Ôm Cổng Ô | 06:00 Bình minh, phố cổ (00:00–01:00) | [`canh-01/`](canh-01/README.md) |
| **Cảnh 02** | Cháu Gái Và Cái App Vay Tiền | 22:00 Đêm, nhà ông Lâm (01:00–02:00) | [`canh-02/`](canh-02/README.md) |
| **Cảnh 03** | Sơn Đỏ Trên Cửa Cuốn | 23:00 Đêm hôm sau (02:00–03:00) | [`canh-03/`](canh-03/README.md) |
| **Cảnh 04** | Bí Mật Của Mai | Nửa đêm (03:00–04:00) | [`canh-04/`](canh-04/README.md) |
| **Cảnh 05** | Đế Chế Phú Quý | 10:00 Sáng (04:00–05:00) | [`canh-05/`](canh-05/README.md) |
| **Cảnh 06** | Chiếc Hộp Sắt Dưới Gầm Giường | 23:00 Đêm (05:00–06:00) | [`canh-06/`](canh-06/README.md) |
| **Cảnh 07** | Hoa Hổ Bún Chả | 11:00 Trưa (06:00–07:00) | [`canh-07/`](canh-07/README.md) |
| **Cảnh 08** | Khoa Báo Sửa Đài | 14:00 Chiều (07:00–08:00) | [`canh-08/`](canh-08/README.md) |
| **Cảnh 09** | Kế Hoạch Rồng Về Phố | 21:00 Tối (08:00–09:00) | [`canh-09/`](canh-09/README.md) |
| **Cảnh 10** | Bà Trùm Kim Cương | 09:30 Sáng (09:00–10:00) | [`canh-10/`](canh-10/README.md) |
| **Cảnh 11** | Hưng Cắn Câu | 10:00 Sáng (10:00–11:00) | [`canh-11/`](canh-11/README.md) |
| **Cảnh 12** | Khoa Báo Vào Phòng Máy | 10:20 Sáng (11:00–12:00) | [`canh-12/`](canh-12/README.md) |
| **Cảnh 13** | Cú Lật Mặt | 10:40 Sáng (12:00–13:00) | [`canh-13/`](canh-13/README.md) |
| **Cảnh 14** | Rượt Đuổi Giữa Phố | 11:00 Trưa (13:00–14:00) | [`canh-14/`](canh-14/README.md) |
| **Cảnh 15** | Chuyến Tàu Cắt Ngang | 11:05 Trưa (14:00–15:00) | [`canh-15/`](canh-15/README.md) |
| **Cảnh 16** | Hổ Bị Mời Về Đồn | 14:00 Chiều (15:00–16:00) | [`canh-16/`](canh-16/README.md) |
| **Cảnh 17** | Đêm Trên Sân Thượng | 22:00 Đêm (16:00–17:00) | [`canh-17/`](canh-17/README.md) |
| **Cảnh 18** | Ổ Cứng Cải Lương | 09:00 Sáng (17:00–18:00) | [`canh-18/`](canh-18/README.md) |
| **Cảnh 19** | Ông Già Xe Ôm Đến Trả Nợ | 20:00 Tối (18:00–19:00) | [`canh-19/`](canh-19/README.md) |
| **Cảnh 20** | Buổi Livestream Định Mệnh | 20:10 Tối (19:00–20:00) | [`canh-20/`](canh-20/README.md) |
| **Cảnh 21** | Đế Chế Sụp Đổ | 20:20 Tối (20:00–21:00) | [`canh-21/`](canh-21/README.md) |
| **Cảnh 22** | Phố Cổ Đứng Dậy | 20:30 Tối (21:00–22:00) | [`canh-22/`](canh-22/README.md) |
| **Cảnh 23** | Siêu Xe Kẹt Giờ Tan Tầm | 20:45 Tối (22:00–23:00) | [`canh-23/`](canh-23/README.md) |
| **Cảnh 24** | Trên Cây Cầu Sắt | 21:00 Đêm (23:00–24:00) | [`canh-24/`](canh-24/README.md) |
| **Cảnh 25** | Kẻ Đòi Nợ Bị Đòi Nợ | 21:10 Đêm & sáng hôm sau (24:00–25:00) | [`canh-25/`](canh-25/README.md) |
| **Cảnh 26** | Đôi Mắt Sáng Lại | Một tuần sau (25:00–26:00) | [`canh-26/`](canh-26/README.md) |
| **Cảnh 27** | Găng Tơ Tái Xuất | 07:00 Sáng (26:00–27:00) | [`canh-27/`](canh-27/README.md) |
