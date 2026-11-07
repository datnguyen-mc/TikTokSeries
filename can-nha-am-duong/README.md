# Căn Nhà Âm Dương: Oan Hồn Dưới Gốc Mít (15 Cảnh × 6 Clips × 10s = 15 Phút)

- **Giọng Người Dẫn Chuyện (cố định cả 90 clip):** Vietnamese man about 45, standard Hà Nội accent with clear six tones, firm resonant baritone with a slight rasp, crisp consonants, tense late-night ghost-story delivery at a brisk, steady pace, only tiny breaths at commas, no dragged vowels. Mỗi clip VO dùng **nguyên văn cùng một câu mô tả giọng** để Omni giữ một giọng duy nhất; nhịp ~4 âm tiết/giây.
- **Thoại nhân vật (Lip-Sync):** clip thoại chỉ mô tả giọng của người nói, không có người dẫn chuyện; mặt và môi người nói luôn thấy rõ.
- **Mật độ:** 90 clips × 10s — 67 clip VO + 23 clip thoại; lời nói nằm trong khung riêng bắt đầu từ 0.4s (xem cột *Khung thoại*).
- **Cách tạo trên Flow (runner tự chọn):** 33 clip nối khung cuối (Frames), 56 clip ảnh nhân vật (Ingredients), 1 clip chỉ text.
- **Hậu kỳ runner:** `atempo` tăng tốc giọng chỉ áp dụng cho clip VO; clip lip-sync giữ nguyên tốc độ để khớp khẩu hình.
- **Nguồn dữ liệu:** `PHAN_CANH_OMNI.json` → `python3 flowkit/scripts/build_omni_horror_prompts.py can-nha-am-duong` sinh lại toàn bộ clip, README, kịch bản.

## Danh Sách 15 Cảnh (90 Clips × 10s)

| Cảnh | Tiêu Đề | Thời Gian | Đường Dẫn |
|---|---|---|---|
| **Cảnh 01** | Chuyến Xe Khách Đêm Khuya & Món Nợ Bốn Trăm Triệu | 23:30 Đêm khuya trên quốc lộ về quê nội (00:00–01:00) | [`canh-01/`](canh-01/README.md) |
| **Cảnh 02** | Bến Xe Thị Xã, Quán Cơm Bụi & Cánh Cổng Sắt Dưới Gốc Mít Cổ Thụ | 14:30–17:45 Chiều tà nơi thị xã và đường về xóm nhỏ (01:00–02:00) | [`canh-02/`](canh-02/README.md) |
| **Cảnh 03** | Ông Bảy Hàng Xóm & Lời Kể Rợn Tóc Gáy Về Vụ Lật Xe Lúc Ba Giờ Sáng | 18:00–21:00 Chập tối tại cổng nhà hoang và hiên nhà Ông Bảy (02:00–03:00) | [`canh-03/`](canh-03/README.md) |
| **Cảnh 04** | Phá Khóa Dọn Nhà Hoang & Cuộc Gọi Tuyệt Vọng Từ Mẹ | 07:00–11:30 Sáng hôm sau tại căn nhà hoang của Cụ Xá (03:00–04:00) | [`canh-04/`](canh-04/README.md) |
| **Cảnh 05** | Đêm Đầu Tiên Một Mình & Vết Bầm Năm Ngón Tay Lúc Rạng Sáng | 23:45 Đêm đầu tiên đến 06:00 Sáng hôm sau (04:00–05:00) | [`canh-05/`](canh-05/README.md) |
| **Cảnh 06** | Chuyện Rượu Đêm Của Ông Tư — Bóng Ma Xin Thuốc Lá Dưới Gốc Mít | 16:30 Chiều đến 22:30 Đêm khuya Ngày thứ hai (05:00–06:00) | [`canh-06/`](canh-06/README.md) |
| **Cảnh 07** | Đêm Thứ Ba — Chiếc Xoong Nhôm Rơi Chói Tai & Bóng Trắng Ngoài Cửa Sổ | 01:30 Rạng sáng Đêm thứ ba (06:00–07:00) | [`canh-07/`](canh-07/README.md) |
| **Cảnh 08** | Đêm Thứ Tư Kinh Hoàng — Bàn Tay Xám Ngoét Thò Qua Lớp Màn | 02:45 Rạng sáng Đêm thứ tư (07:00–08:00) | [`canh-08/`](canh-08/README.md) |
| **Cảnh 09** | Vết Bầm Không Tan & Nỗi Tuyệt Vọng Không Chốn Dung Thân | 06:30 Sáng hôm sau tại sân gạch nhà hoang (08:00–09:00) | [`canh-09/`](canh-09/README.md) |
| **Cảnh 10** | Đêm Thứ Năm — Vong Hồn Ông Nội Hiện Hình Trong Góc Phòng | 01:00 Rạng sáng Đêm thứ năm (09:00–10:00) | [`canh-10/`](canh-10/README.md) |
| **Cảnh 11** | Cuộc Gọi Cho Bố & Bàn Tay Giận Dữ Khựng Lại Giữa Sân Quê | 06:00 Rạng sáng đến 16:30 Chiều Ngày thứ sáu (10:00–11:00) | [`canh-11/`](canh-11/README.md) |
| **Cảnh 12** | Giấc Mơ Đẫm Nước Mắt Của Ông Quân & Nén Hương Tạ Tội Trước Mộ Cha | 23:00 Đêm thứ sáu đến Sáng hôm sau (11:00–12:00) | [`canh-12/`](canh-12/README.md) |
| **Cảnh 13** | Bốn Mươi Chín Ngày Ăn Chay Cầu Siêu & Ngôi Miếu Nhỏ Dưới Gốc Mít | Suốt 49 ngày hương khói tại quê nội (12:00–13:00) | [`canh-13/`](canh-13/README.md) |
| **Cảnh 14** | Món Nợ Được Hoàn Trả & Mâm Cơm Đoàn Tụ Nơi Quê Nội | Những ngày cuối năm ấm áp tại quê nội (13:00–14:00) | [`canh-14/`](canh-14/README.md) |
| **Cảnh 15** | Đêm Trăng Thanh Tịnh — Dương Thịnh Âm An & Lời Nhắn Cõi Âm | 22:00 Đêm trăng rằm thanh tịnh nơi quê nội (14:00–15:00) | [`canh-15/`](canh-15/README.md) |
