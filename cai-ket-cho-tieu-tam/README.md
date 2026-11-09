# Cái Kết Cho Tiểu Tam (25 Cảnh × 4 Clips × 15s = 25 Phút)

- **Giọng Người Dẫn Chuyện (cố định cả 100 clip):** Vietnamese woman about 50, strictly standard Hà Nội Northern accent (giọng chuẩn Hà Nội Bắc Bộ, never Southern accent) with clear six tones, warm low alto with a slight husk, fast fluent heartfelt family-drama storytelling in one continuous breath, every word spoken once and clearly, no stutter, no repeated words. Mỗi clip VO dùng **nguyên văn cùng một câu mô tả giọng** để Omni giữ một giọng duy nhất; đọc nhanh liên thanh như oan-thai-doi-me, ~4.0 âm tiết/giây, liền một hơi, không ngắt giữa câu.
- **Thoại nhân vật (Lip-Sync):** clip thoại chỉ mô tả giọng của người nói, không có người dẫn chuyện; mặt và môi người nói luôn thấy rõ.
- **Mật độ:** 100 clips × 15s — 0 clip VO + 100 clip thoại (65 clip có hai lượt thoại); lời nói nằm trong khung riêng bắt đầu từ 0.4s (xem cột *Khung thoại*).
- **Cách tạo trên Flow (runner tự chọn):** 24 clip nối khung cuối (Frames — cùng bối cảnh, không có nhân vật mới), 76 clip ảnh nhân vật (Ingredients), 0 clip chỉ text. Tắt nối khung: `FLOWKIT_CHAIN_LAST_FRAME=0`.
- **Hậu kỳ runner:** clip VO được tăng tốc giọng thêm 1.18x khi tải về (`FLOWKIT_VOICE_TEMPO` mặc định 1.18, đặt 1.0 để tắt), giữ nguyên khung hình 15s; clip lip-sync không bao giờ bị tăng tốc để khớp khẩu hình.
- **Màu phim & ánh sáng:** Naturalistic soft lighting: warm tungsten and charcoal-stove glow at home, cool grey-blue dawn light with yellow streetlamps on the old-quarter pavement, crisp cold daylight in the glass office and luxury apartment, wet neon reflections on rainy nights.
- **Nguồn dữ liệu:** `PHAN_CANH_OMNI.json` → `python3 flowkit/scripts/build_omni_horror_prompts.py cai-ket-cho-tieu-tam` sinh lại toàn bộ clip, README, kịch bản.

## Danh Sách 25 Cảnh (100 Clips × 15s)

| Cảnh | Tiêu Đề | Thời Gian | Đường Dẫn |
|---|---|---|---|
| **Cảnh 01** | Người Đàn Bà Thức Dậy Trước Mặt Trời | 04:00 Rạng sáng, phố cổ Hà Nội (00:00–01:00) | [`canh-01/`](canh-01/README.md) |
| **Cảnh 02** | Đôi Bông Tai Đã Bán | 05:30 Sáng, gánh xôi góc phố (01:00–02:00) | [`canh-02/`](canh-02/README.md) |
| **Cảnh 03** | Ông Giám Đốc Mới Phất | 07:30 Sáng, nhà Thu (02:00–03:00) | [`canh-03/`](canh-03/README.md) |
| **Cảnh 04** | Cô Thư Ký Váy Đỏ | 08:30 Sáng, văn phòng giám đốc (03:00–04:00) | [`canh-04/`](canh-04/README.md) |
| **Cảnh 05** | Người Tình Bí Mật | 12:00 Trưa, quán cà phê kín đáo (04:00–05:00) | [`canh-05/`](canh-05/README.md) |
| **Cảnh 06** | Sợi Tóc Trên Áo Chồng | 23:30 Đêm, nhà Thu (05:00–06:00) | [`canh-06/`](canh-06/README.md) |
| **Cảnh 07** | Chuyến Công Tác Đà Nẵng | Chiều tà, khu nghỉ dưỡng biển (06:00–07:00) | [`canh-07/`](canh-07/README.md) |
| **Cảnh 08** | Bức Ảnh Lúc Nửa Đêm | Đêm, nhà Thu (07:00–08:00) | [`canh-08/`](canh-08/README.md) |
| **Cảnh 09** | Bé Ba Ghé Gánh Xôi | 06:00 Sáng, góc phố (08:00–09:00) | [`canh-09/`](canh-09/README.md) |
| **Cảnh 10** | Mâm Cơm Đòi Ly Hôn | 19:00 Tối, nhà Thu (09:00–10:00) | [`canh-10/`](canh-10/README.md) |
| **Cảnh 11** | Nước Mắt Bên Bếp Than | Nửa đêm, bếp nhà Thu (10:00–11:00) | [`canh-11/`](canh-11/README.md) |
| **Cảnh 12** | Hai Vạch Hồng | Sáng, căn hộ cao cấp (11:00–12:00) | [`canh-12/`](canh-12/README.md) |
| **Cảnh 13** | Cú Ngã Trên Cầu Thang | Chiều, nhà Thu (12:00–13:00) | [`canh-13/`](canh-13/README.md) |
| **Cảnh 14** | Mẹ Chồng Chọn Con Dâu | Sáng, nhà Thu (13:00–14:00) | [`canh-14/`](canh-14/README.md) |
| **Cảnh 15** | Căn Phòng Trọ Mười Mét Vuông | Tối, xóm trọ (14:00–15:00) | [`canh-15/`](canh-15/README.md) |
| **Cảnh 16** | Chữ Ký Định Mệnh | Sáng, nhà cũ & văn phòng (15:00–16:00) | [`canh-16/`](canh-16/README.md) |
| **Cảnh 17** | Quán Xôi Của Thu | 05:30 Sáng, sáu tháng sau (16:00–17:00) | [`canh-17/`](canh-17/README.md) |
| **Cảnh 18** | Công Ty Rỗng Ruột | Sáng, văn phòng giám đốc (17:00–18:00) | [`canh-18/`](canh-18/README.md) |
| **Cảnh 19** | Sau Lớp Kính Quán Cà Phê | Tối mưa, quán cà phê quen của Vy (18:00–19:00) | [`canh-19/`](canh-19/README.md) |
| **Cảnh 20** | Căn Nhà Bị Niêm Phong | Đêm mưa đến rạng sáng, trước cổng nhà cũ (19:00–20:00) | [`canh-20/`](canh-20/README.md) |
| **Cảnh 21** | Chuyến Bay Không Cất Cánh | Sáng, sảnh ga đi sân bay (20:00–21:00) | [`canh-21/`](canh-21/README.md) |
| **Cảnh 22** | Gói Xôi Lúc Bình Minh | 05:30 Sáng, quán xôi của Thu (21:00–22:00) | [`canh-22/`](canh-22/README.md) |
| **Cảnh 23** | Mẹ Vẫn Là Mẹ | Tối, gác nhỏ trên quán xôi (22:00–23:00) | [`canh-23/`](canh-23/README.md) |
| **Cảnh 24** | Buổi Diễn Văn Nghệ | Chiều, hội trường trường tiểu học (23:00–24:00) | [`canh-24/`](canh-24/README.md) |
| **Cảnh 25** | Vợ Tào Khang | 06:00 Sáng, một năm sau (24:00–25:00) | [`canh-25/`](canh-25/README.md) |
