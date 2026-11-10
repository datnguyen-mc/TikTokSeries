# Chính Thất Cao Tay, Tiểu Tam Trắng Tay (25 Cảnh × 4 Clips × 15s = 25 Phút)

- **Không có người dẫn chuyện:** 100% lời thoại do nhân vật nói trên hình — cả 100 clip là thoại khớp khẩu hình. Giọng gốc của mỗi nhân vật (tuổi, chất giọng, giọng Hà Nội) giữ nguyên văn ở mọi clip để Omni không đổi người nói.
- **Nhịp giọng theo cảnh:** mỗi lượt thoại có nhịp riêng nối sau giọng gốc — **nhanh** (cãi vã, hoảng hốt, rượt đuổi, khoe khoang; tốc độ ×1.2), **vừa** (trò chuyện thường), **chậm** (xúc động, thú nhận, câu chốt lặng người; tốc độ ×0.9). Khung thoại tính theo nhịp nên câu chậm ít chữ hơn. Cả phim: 95 lượt nhanh, 105 lượt vừa, 89 lượt chậm.
- **Thoại nhân vật (Lip-Sync):** clip thoại chỉ mô tả giọng của người nói, không có người dẫn chuyện; mặt và môi người nói luôn thấy rõ.
- **Mật độ:** 100 clips × 15s, tất cả là clip thoại (5 clip có hai lượt thoại); lời nói nằm trong khung riêng bắt đầu từ 0.4s (xem cột *Khung thoại*).
- **Cách tạo trên Flow (runner tự chọn):** 36 clip nối khung cuối (Frames — cùng bối cảnh, không có nhân vật mới), 64 clip ảnh nhân vật (Ingredients), 0 clip chỉ text. Tắt nối khung: `FLOWKIT_CHAIN_LAST_FRAME=0`.
- **Hậu kỳ runner:** không có clip VO nên runner không tăng tốc giọng clip nào; tốc độ nói nằm trong prompt (nhịp từng lượt) để khớp khẩu hình.
- **Màu phim & ánh sáng:** Naturalistic soft lighting: warm window light and a desk lamp over the sewing machine in the tailor shop, warm tungsten at home, cool blue-white glass light in the luxury apartment and the office, golden chandelier light at the banquet hall, soft green-gold daylight in the countryside.
- **Nguồn dữ liệu:** `PHAN_CANH_OMNI.json` → `python3 flowkit/scripts/build_omni_horror_prompts.py cai-ket-cho-tieu-tam` sinh lại toàn bộ clip, README, kịch bản.

## Danh Sách 25 Cảnh (100 Clips × 15s)

| Cảnh | Tiêu Đề | Thời Gian | Đường Dẫn |
|---|---|---|---|
| **Cảnh 01** | Khách Lạ Đặt Áo Cưới | Chiều, tiệm may áo dài phố Hàng Gai (00:00–01:00) | [`canh-01/`](canh-01/README.md) |
| **Cảnh 02** | Bữa Cơm Có Mùi Nước Hoa | Tối, nhà Thu (01:00–02:00) | [`canh-02/`](canh-02/README.md) |
| **Cảnh 03** | Chiếc Hộp Sơn Mài Của Mẹ Chồng | Đêm, phòng bà Nhàn (02:00–03:00) | [`canh-03/`](canh-03/README.md) |
| **Cảnh 04** | Vợ Chồng Nhà Lừa | Đêm, căn hộ cao cấp của Vy (03:00–04:00) | [`canh-04/`](canh-04/README.md) |
| **Cảnh 05** | Buổi Thử Áo Đầu Tiên | Vài ngày sau, tiệm may (04:00–05:00) | [`canh-05/`](canh-05/README.md) |
| **Cảnh 06** | Tờ Giấy Ký Không Đọc | Tối, nhà Thu (05:00–06:00) | [`canh-06/`](canh-06/README.md) |
| **Cảnh 07** | Anh Họ Luật Sư | Sáng hôm sau, nhà Thu (06:00–07:00) | [`canh-07/`](canh-07/README.md) |
| **Cảnh 08** | Cô Dâu Về Ra Mắt | Chiều chủ nhật, nhà Thu (07:00–08:00) | [`canh-08/`](canh-08/README.md) |
| **Cảnh 09** | Về Quê Cô Dâu | Chiều, một làng quê Nam Định (08:00–09:00) | [`canh-09/`](canh-09/README.md) |
| **Cảnh 10** | Bé Na Theo Bố | Cuối tuần, trước tiệm may rồi đêm trong tiệm (09:00–10:00) | [`canh-10/`](canh-10/README.md) |
| **Cảnh 11** | Bể Bơi Trên Tầng Thượng | Thứ bảy, căn hộ của Vy (10:00–11:00) | [`canh-11/`](canh-11/README.md) |
| **Cảnh 12** | Năm Tỷ Sính Lễ | Thứ hai, văn phòng giám đốc (11:00–12:00) | [`canh-12/`](canh-12/README.md) |
| **Cảnh 13** | Chính Thất Đồng Ý Ly Hôn | Chiều, quán cà phê nhìn ra hồ Gươm (12:00–13:00) | [`canh-13/`](canh-13/README.md) |
| **Cảnh 14** | Buổi Thử Áo Cuối Cùng | Ba ngày trước đám hỏi, tiệm may (13:00–14:00) | [`canh-14/`](canh-14/README.md) |
| **Cảnh 15** | Đêm Trước Đám Hỏi | Đêm trước đám hỏi (14:00–15:00) | [`canh-15/`](canh-15/README.md) |
| **Cảnh 16** | Đám Hỏi Bắt Đầu | Tối, sảnh tiệc khách sạn (15:00–16:00) | [`canh-16/`](canh-16/README.md) |
| **Cảnh 17** | Món Quà Cưới | Tối, sảnh tiệc khách sạn (16:00–17:00) | [`canh-17/`](canh-17/README.md) |
| **Cảnh 18** | Sổ Đỏ Đứng Tên Ai | Tối, sảnh tiệc khách sạn (17:00–18:00) | [`canh-18/`](canh-18/README.md) |
| **Cảnh 19** | Lối Thoát Hiểm | Tối, hành lang sau sảnh tiệc (18:00–19:00) | [`canh-19/`](canh-19/README.md) |
| **Cảnh 20** | Cây Tùng Đổ | Khuya, sảnh tiệc vắng (19:00–20:00) | [`canh-20/`](canh-20/README.md) |
| **Cảnh 21** | Ghế Chủ Tịch | Một tuần sau, phòng họp cổ đông (20:00–21:00) | [`canh-21/`](canh-21/README.md) |
| **Cảnh 22** | Phòng Thăm Gặp | Vài ngày sau, phòng thăm gặp (21:00–22:00) | [`canh-22/`](canh-22/README.md) |
| **Cảnh 23** | Viên Gạch Đầu Tiên | Một tháng sau, công trường lúc bình minh (22:00–23:00) | [`canh-23/`](canh-23/README.md) |
| **Cảnh 24** | Áo Dài Mừng Thọ | Mấy tháng sau, tối sinh nhật bà Nhàn (23:00–24:00) | [`canh-24/`](canh-24/README.md) |
| **Cảnh 25** | Đo Lòng Người | Một năm sau, tiệm may hai tầng lúc bình minh (24:00–25:00) | [`canh-25/`](canh-25/README.md) |
