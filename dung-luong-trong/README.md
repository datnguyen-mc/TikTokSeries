# Dung Lượng Trống (Free Space) (20 Cảnh × 4 Clips × 15s = 20 Phút)

- **Không có người dẫn chuyện:** 100% lời thoại do nhân vật nói trên hình — cả 80 clip là thoại khớp khẩu hình. Giọng gốc của mỗi nhân vật (tuổi, chất giọng, giọng Hà Nội) giữ nguyên văn ở mọi clip để Omni không đổi người nói.
- **Nhịp giọng theo cảnh:** mỗi lượt thoại có nhịp riêng nối sau giọng gốc — **nhanh** (cãi vã, hoảng hốt, rượt đuổi, khoe khoang; tốc độ ×1.2), **vừa** (trò chuyện thường), **chậm** (xúc động, thú nhận, câu chốt lặng người; tốc độ ×0.9). Khung thoại tính theo nhịp nên câu chậm ít chữ hơn. Cả phim: 71 lượt nhanh, 89 lượt vừa, 80 lượt chậm.
- **Thoại nhân vật (Lip-Sync):** clip thoại chỉ mô tả giọng của người nói, không có người dẫn chuyện; mặt và môi người nói luôn thấy rõ.
- **Mật độ:** 80 clips × 15s, tất cả là clip thoại; lời nói nằm trong khung riêng bắt đầu từ 0.4s (xem cột *Khung thoại*).
- **Cách tạo trên Flow (runner tự chọn):** 41 clip nối khung cuối (Frames — cùng bối cảnh, không có nhân vật mới), 39 clip ảnh nhân vật (Ingredients), 0 clip chỉ text. Tắt nối khung: `FLOWKIT_CHAIN_LAST_FRAME=0`.
- **Hậu kỳ runner:** không có clip VO nên runner không tăng tốc giọng clip nào; tốc độ nói nằm trong prompt (nhịp từng lượt) để khớp khẩu hình.
- **Màu phim & ánh sáng:** Motivated, grounded light: warm sodium-orange street light and bare tungsten bulbs in the alleys and rooms, soft grey daylight through barred windows, a cool violet glow from NeuroRent devices and holograms; memory flashbacks are graded cold cyan-blue with flickering, slightly unstable light and a faint digital glitch; shadows stay soft, never murky.
- **Nguồn dữ liệu:** `PHAN_CANH_OMNI.json` → `python3 flowkit/scripts/build_omni_horror_prompts.py dung-luong-trong` sinh lại toàn bộ clip, README, kịch bản.

## Danh Sách 20 Cảnh (80 Clips × 15s)

| Cảnh | Tiêu Đề | Thời Gian | Đường Dẫn |
|---|---|---|---|
| **Cảnh 01** | 3:17 AM (Ba giờ mười bảy phút) | 3 giờ 17 phút sáng, phòng trọ khu tập thể Kim Liên (00:00–01:00) | [`canh-01/`](canh-01/README.md) |
| **Cảnh 02** | Seven Days Earlier (Bảy ngày trước) | Bảy ngày trước, trưa, cổng khu tập thể (01:00–02:00) | [`canh-02/`](canh-02/README.md) |
| **Cảnh 03** | Three Million Two (Ba triệu hai) | Chiều cùng ngày, phòng trọ (02:00–03:00) | [`canh-03/`](canh-03/README.md) |
| **Cảnh 04** | Grandma Tư (Bà Tư) | Chạng vạng, sân chung khu tập thể (03:00–04:00) | [`canh-04/`](canh-04/README.md) |
| **Cảnh 05** | I Agree (Đồng ý) | Đêm cùng ngày, phòng trọ (04:00–05:00) | [`canh-05/`](canh-05/README.md) |
| **Cảnh 06** | Money While You Sleep (Ngủ ra tiền) | Ngày 1 đến ngày 3 (05:00–06:00) | [`canh-06/`](canh-06/README.md) |
| **Cảnh 07** | The Strange Song (Bài hát lạ) | Sáng ngày 4, phòng trọ (06:00–07:00) | [`canh-07/`](canh-07/README.md) |
| **Cảnh 08** | The Door Code (Mã cửa) | Trưa ngày 5, cửa tòa văn phòng giữa phố (07:00–08:00) | [`canh-08/`](canh-08/README.md) |
| **Cảnh 09** | Don't Sleep (Không ngủ) | Đêm ngày 6, phòng trọ (08:00–09:00) | [`canh-09/`](canh-09/README.md) |
| **Cảnh 10** | The Memory (Ký ức) | Ký ức đêm 6 tháng 11, căn hộ bỏ hoang, xen với phòng trọ 3 giờ 17 sáng (09:00–10:00) | [`canh-10/`](canh-10/README.md) |
| **Cảnh 11** | The Abandoned Block (Khu tập thể bỏ hoang) | Sáng ngày 7, khu tập thể Kim Liên nhà C bỏ hoang (10:00–11:00) | [`canh-11/`](canh-11/README.md) |
| **Cảnh 12** | The Truth (Sự thật) | Sáng ngày 7, phòng 7.04 (11:00–12:00) | [`canh-12/`](canh-12/README.md) |
| **Cảnh 13** | The Safe (Két sắt) | Trưa ngày 7, phòng 7.04 (12:00–13:00) | [`canh-13/`](canh-13/README.md) |
| **Cảnh 14** | Reclaim at Midnight (Thu hồi lúc 0 giờ) | Chiều ngày 7, phòng 7.04 (13:00–14:00) | [`canh-14/`](canh-14/README.md) |
| **Cảnh 15** | Little Hạnh (Bé Hạnh) | Chạng vạng ngày 7, sân chung khu tập thể (14:00–15:00) | [`canh-15/`](canh-15/README.md) |
| **Cảnh 16** | The Choice (Lựa chọn) | 11 giờ 20 đêm ngày 7, phòng trọ (15:00–16:00) | [`canh-16/`](canh-16/README.md) |
| **Cảnh 17** | Live (Phát trực tiếp) | 11 giờ 47 đêm ngày 7, phòng trọ (16:00–17:00) | [`canh-17/`](canh-17/README.md) |
| **Cảnh 18** | Ten Seconds (Mười giây) | 11 giờ 56 đêm ngày 7, phòng trọ (17:00–18:00) | [`canh-18/`](canh-18/README.md) |
| **Cảnh 19** | The Morning After (Sáng hôm sau) | Sáng hôm sau, phòng trọ (18:00–19:00) | [`canh-19/`](canh-19/README.md) |
| **Cảnh 20** | The Lullaby (Bài hát ru) | Sáng hôm sau, sân chung và phòng trọ (19:00–20:00) | [`canh-20/`](canh-20/README.md) |
