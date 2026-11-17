# Vợ Tôi Mất Trí Nhớ Có Chọn Lọc (25 Cảnh × 4 Clips × 15s = 25 Phút)

- **Không có người dẫn chuyện:** 100% lời thoại do nhân vật nói trên hình — cả 100 clip là thoại khớp khẩu hình. Giọng gốc của mỗi nhân vật (tuổi, chất giọng, giọng Hà Nội) giữ nguyên văn ở mọi clip để Omni không đổi người nói.
- **Nhịp giọng theo cảnh:** mỗi lượt thoại có nhịp riêng nối sau giọng gốc — **nhanh** (cãi vã, hoảng hốt, rượt đuổi, khoe khoang; tốc độ ×1.2), **vừa** (trò chuyện thường), **chậm** (xúc động, thú nhận, câu chốt lặng người; tốc độ ×0.9). Khung thoại tính theo nhịp nên câu chậm ít chữ hơn. Cả phim: 113 lượt nhanh, 106 lượt vừa, 81 lượt chậm.
- **Thoại nhân vật (Lip-Sync):** clip thoại chỉ mô tả giọng của người nói, không có người dẫn chuyện; mặt và môi người nói luôn thấy rõ.
- **Mật độ:** 100 clips × 15s, tất cả là clip thoại; lời nói nằm trong khung riêng bắt đầu từ 0.4s (xem cột *Khung thoại*).
- **Cách tạo trên Flow (runner tự chọn):** 59 clip nối khung cuối (Frames — cùng bối cảnh, không có nhân vật mới), 41 clip ảnh nhân vật (Ingredients), 0 clip chỉ text. Tắt nối khung: `FLOWKIT_CHAIN_LAST_FRAME=0`.
- **Hậu kỳ runner:** không có clip VO nên runner không tăng tốc giọng clip nào; tốc độ nói nằm trong prompt (nhịp từng lượt) để khớp khẩu hình.
- **Màu phim & ánh sáng:** Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.
- **Nguồn dữ liệu:** `PHAN_CANH_OMNI.json` → `python3 flowkit/scripts/build_omni_horror_prompts.py vo-toi-mat-tri-nho` sinh lại toàn bộ clip, README, kịch bản.

## Danh Sách 25 Cảnh (100 Clips × 15s)

| Cảnh | Tiêu Đề | Thời Gian | Đường Dẫn |
|---|---|---|---|
| **Cảnh 01** | Kỷ Niệm Mười Năm Thiếu Một Người | Tối, nhà hàng sân thượng nhìn ra hồ (00:00–01:00) | [`canh-01/`](canh-01/README.md) |
| **Cảnh 02** | Đối Tác Nhật Lai Hàn | Cùng tối, sảnh khách sạn năm sao (01:00–02:00) | [`canh-02/`](canh-02/README.md) |
| **Cảnh 03** | Anh Là Ai? | Sáng hôm sau, phòng VIP bệnh viện (02:00–03:00) | [`canh-03/`](canh-03/README.md) |
| **Cảnh 04** | Bác Sĩ Đồng Phạm | Cùng ngày, phòng VIP bệnh viện (03:00–04:00) | [`canh-04/`](canh-04/README.md) |
| **Cảnh 05** | Về Nhà Với Người Lạ | Chiều tối, biệt thự ven hồ (04:00–05:00) | [`canh-05/`](canh-05/README.md) |
| **Cảnh 06** | Nội Quy Của Cô Gái Hai Mươi Hai | Sáng hôm sau, bếp biệt thự rồi văn phòng Quân (05:00–06:00) | [`canh-06/`](canh-06/README.md) |
| **Cảnh 07** | Tiểu Tam Sốt Ruột | Trưa, phòng tập yoga của Mai Anh (06:00–07:00) | [`canh-07/`](canh-07/README.md) |
| **Cảnh 08** | Tờ Đơn Thành Thuyền Giấy | Tối, phòng khách biệt thự (07:00–08:00) | [`canh-08/`](canh-08/README.md) |
| **Cảnh 09** | Buổi Hẹn Đầu Tiên, Lần Thứ Hai | Tối, quán bún chả ven hồ (08:00–09:00) | [`canh-09/`](canh-09/README.md) |
| **Cảnh 10** | Đối Thủ Áo Blouse Trắng | Chiều, phòng khách biệt thự (09:00–10:00) | [`canh-10/`](canh-10/README.md) |
| **Cảnh 11** | Lớp Yoga Của Tiểu Tam | Sáng, phòng tập yoga của Mai Anh (10:00–11:00) | [`canh-11/`](canh-11/README.md) |
| **Cảnh 12** | Hai Người Đàn Bà, Một Bàn Trà | Chiều, quán cà phê nhìn ra hồ (11:00–12:00) | [`canh-12/`](canh-12/README.md) |
| **Cảnh 13** | Đồng Minh Bất Đắc Dĩ | Cùng chiều, quán cà phê (12:00–13:00) | [`canh-13/`](canh-13/README.md) |
| **Cảnh 14** | Hai Người Yêu Đòi Quà Cùng Lúc | Sáng thứ hai, văn phòng của Quân (13:00–14:00) | [`canh-14/`](canh-14/README.md) |
| **Cảnh 15** | Nhầm Phong Bì | Tối, phòng khách biệt thự; rồi phòng tập yoga (14:00–15:00) | [`canh-15/`](canh-15/README.md) |
| **Cảnh 16** | Bống Biết Hết | Đêm, phòng ngủ của Bống (15:00–16:00) | [`canh-16/`](canh-16/README.md) |
| **Cảnh 17** | Bát Cháo Lúc Nửa Đêm | Nửa đêm mưa, bếp biệt thự (16:00–17:00) | [`canh-17/`](canh-17/README.md) |
| **Cảnh 18** | Lời Chia Tay Thật Lòng | Sáng hôm sau, phòng tập yoga (17:00–18:00) | [`canh-18/`](canh-18/README.md) |
| **Cảnh 19** | Bống Lỡ Miệng | Chiều thứ năm, phòng khách biệt thự (18:00–19:00) | [`canh-19/`](canh-19/README.md) |
| **Cảnh 20** | Đồng Phạm Gặp Đồng Phạm | Sáng thứ sáu, phòng khám của bác sĩ Khang (19:00–20:00) | [`canh-20/`](canh-20/README.md) |
| **Cảnh 21** | Sinh Nhật Hai Mươi Hai, Lần Thứ Hai | Tối thứ bảy, vườn biệt thự (20:00–21:00) | [`canh-21/`](canh-21/README.md) |
| **Cảnh 22** | Màn Cầu Hôn Lần Hai | Cùng tối, dưới cổng hoa hồng (21:00–22:00) | [`canh-22/`](canh-22/README.md) |
| **Cảnh 23** | Hợp Đồng Thử Việc | Cùng tối, bàn bánh sinh nhật (22:00–23:00) | [`canh-23/`](canh-23/README.md) |
| **Cảnh 24** | Sáu Tháng Sau | Sáu tháng sau, bếp biệt thự buổi sáng (23:00–24:00) | [`canh-24/`](canh-24/README.md) |
| **Cảnh 25** | Kỷ Niệm Mười Một Năm | Tối, nhà hàng sân thượng nhìn ra hồ (24:00–25:00) | [`canh-25/`](canh-25/README.md) |
