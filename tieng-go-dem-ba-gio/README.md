# Tiếng Gõ Đêm Ba Giờ: Lời Nguyền Giếng Đá Ong (15 Cảnh × 6 Clips × 10s = 15 Phút)

- **Giọng Người Dẫn Chuyện (cố định cả 90 clip):** Vietnamese man about 45, standard Hà Nội accent with clear six tones, firm resonant baritone with a slight rasp, crisp consonants, tense late-night ghost-story delivery at a brisk, steady pace, only tiny breaths at commas, no dragged vowels. Mỗi clip VO dùng **nguyên văn cùng một câu mô tả giọng** để Omni giữ một giọng duy nhất; nhịp ~4 âm tiết/giây.
- **Thoại nhân vật (Lip-Sync):** clip thoại chỉ mô tả giọng của người nói, không có người dẫn chuyện; mặt và môi người nói luôn thấy rõ.
- **Mật độ:** 90 clips × 10s — 76 clip VO + 14 clip thoại; lời nói nằm trong khung riêng bắt đầu từ 0.4s (xem cột *Khung thoại*).
- **Cách tạo trên Flow (runner tự chọn):** 37 clip nối khung cuối (Frames), 52 clip ảnh nhân vật (Ingredients), 1 clip chỉ text.
- **Hậu kỳ runner:** `atempo` tăng tốc giọng chỉ áp dụng cho clip VO; clip lip-sync giữ nguyên tốc độ để khớp khẩu hình.
- **Nguồn dữ liệu:** `PHAN_CANH_OMNI.json` → `python3 flowkit/scripts/build_omni_horror_prompts.py tieng-go-dem-ba-gio` sinh lại toàn bộ clip, README, kịch bản.

## Danh Sách 15 Cảnh (90 Clips × 10s)

| Cảnh | Tiêu Đề | Thời Gian | Đường Dẫn |
|---|---|---|---|
| **Cảnh 01** | Cổng Nhà Cổ Trong Mưa Ngâu & Ba Lời Thề Bên Giếng Đá Ong | 18:30 Chập tối tháng Bảy âm lịch (00:00–01:00) | [`canh-01/`](canh-01/README.md) |
| **Cảnh 02** | Đêm Đầu Tiên — Đồng Hồ Dừng Lúc 2 Giờ 59 Phút & Tiếng Gõ Dưới Đáy Giếng | 02:59 Rạng sáng Đêm thứ nhất (01:00–02:00) | [`canh-02/`](canh-02/README.md) |
| **Cảnh 03** | Tấm Khăn Lụa Đen Rơi Xuống & Bóng Người Trong Gương Đồng | 03:05 Rạng sáng Đêm thứ nhất (02:00–03:00) | [`canh-03/`](canh-03/README.md) |
| **Cảnh 04** | Bóng Ma Tiến Gần Trong Từng Tấm Ảnh Chụp Đèn Flash | 03:20–04:30 Rạng sáng Đêm thứ nhất (03:00–04:00) | [`canh-04/`](canh-04/README.md) |
| **Cảnh 05** | Buổi Sáng Kỳ Lạ & Cánh Cổng Bị Khóa Trái Bằng Xích Đồng | 06:30 Sáng sớm & Chiều muộn Ngày thứ hai (04:00–05:00) | [`canh-05/`](canh-05/README.md) |
| **Cảnh 06** | Đêm Thứ Hai — Xuất Hiện Cánh Cửa Gỗ Thứ Tư Cuối Hành Lang | 01:30 Rạng sáng Đêm thứ hai (05:00–06:00) | [`canh-06/`](canh-06/README.md) |
| **Cảnh 07** | Căn Buồng Bị Niêm Phong 50 Năm & Đường Hầm Thông Xuống Đáy Giếng | 02:00 Rạng sáng Đêm thứ hai (06:00–07:00) | [`canh-07/`](canh-07/README.md) |
| **Cảnh 08** | Cụ Từ Tiết Lộ Thảm Án 50 Năm Trước & Sự Thật Về Bà Cầm | 02:30 Rạng sáng Đêm thứ hai (07:00–08:00) | [`canh-08/`](canh-08/README.md) |
| **Cảnh 09** | Tờ Hợp Đồng Hóa Vàng Mã & Khế Ước Bắt Người Thế Mạng | 02:45 Rạng sáng Đêm thứ hai (08:00–09:00) | [`canh-09/`](canh-09/README.md) |
| **Cảnh 10** | Ác Linh Bà Cầm Hiện Nguyên Hình Ngoài Hiên Nhà Cổ | 02:55 Rạng sáng Đêm thứ hai (09:00–10:00) | [`canh-10/`](canh-10/README.md) |
| **Cảnh 11** | Đêm Thứ Ba (02:45 Sáng) — Nước Giếng Đen Tràn Ngập & Bóng Ma Bước Ra Từ Gương | 02:45 Rạng sáng Đêm thứ ba (10:00–11:00) | [`canh-11/`](canh-11/README.md) |
| **Cảnh 12** | Cuộc Vây Hãm Của Ác Linh Bà Cầm Ngoài Sân Mưa Bão | 02:52 Rạng sáng Đêm thứ ba (11:00–12:00) | [`canh-12/`](canh-12/README.md) |
| **Cảnh 13** | Nhát Búa Lúc 2 Giờ 59 Phút — Đập Vỡ Bia Trấn Yểm Đáy Giếng | 02:59 Rạng sáng Đêm thứ ba (12:00–13:00) | [`canh-13/`](canh-13/README.md) |
| **Cảnh 14** | Giọt Nước Mắt Giải Oan & Lời Tạ Từ Bên Miệng Giếng | 03:05 Rạng sáng Đêm thứ ba sau cơn bão (13:00–14:00) | [`canh-14/`](canh-14/README.md) |
| **Cảnh 15** | Bình Minh Trên Nhà Cổ & Dấu Tay Hơi Nước Trên Gương Đồng | 06:30 Bình minh Ngày thứ tư (14:00–15:00) | [`canh-15/`](canh-15/README.md) |
