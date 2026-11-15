# Báo cáo dựng phim — Hollywood Cold Open

**Phim:** Hổ Phách – Ngược Dòng Tiền Sử
**File:** `hollywood_cold_open.mp4`: 1920×1080, 24fps, H.264 + AAC 320k, dài 73,98 giây, letterbox 2.39:1
**Ngày dựng:** 14/11/2026

---

## 1. Phân tích footage (Phase 1)

| Hạng mục | Kết quả |
|---|---|
| Thư mục quét | `clips/` (thư mục `clips_regen` không tồn tại trong ho-phach-nguoc-dong-tien-su và cả TikTokSeries) |
| Số clip | 88 (Cảnh 01–22 × 4 clip). Đã phân tích đủ 88 clip, không bỏ sót clip nào |
| Thông số chung | 1280×720, 24fps, H.264 + AAC, mỗi clip 15,04 giây, tổng khoảng 22 phút |
| Clip regen | 7 clip có giờ sửa muộn hơn (11:58), trùng với ảnh `new_…` trong `_review`: Canh03_Clip3, Canh09_Clip4, Canh13_Clip4, Canh15_Clip2, Canh15_Clip3, Canh22_Clip1, Canh22_Clip4. Đây là các bản đã thay thế |
| Cách phân tích | Trích 6 khung hình mỗi clip (cả 88 clip). Với 24 clip ứng viên, trích thêm khung hình mỗi giây có timecode. Dò điểm cắt nội bộ (scene detection) và năng lượng dải giọng nói theo từng 0,25 giây |

**Giới hạn cần nói rõ:** không tạo được transcript lời thoại. Mô hình nhận dạng giọng nói (Whisper) phải tải từ Hugging Face, mà máy chủ này bị proxy chặn ở cả máy bạn lẫn môi trường dựng. Vì vậy lời thoại được đánh giá qua khẩu hình, biểu cảm và năng lượng âm thanh, chứ không theo nội dung câu nói. Điểm "âm thanh/thoại" trong bảng chấm là ước lượng.

### Mạch truyện (dựng lại từ hình ảnh)
1. **Cảnh 01–03:** Nhà khảo cổ trẻ (đeo kính), cô giáo lớn tuổi và anh quay phim (mũ đỏ) đào được một vật hình đĩa cùng khối hổ phách có côn trùng bên trong, rồi đem về phòng lab soi chụp.
2. **Cảnh 04:** Trong phòng lab, hổ phách bừng sáng, vòng tròn vàng mở cổng thời gian.
3. **Cảnh 05–07:** Kỷ băng hà. Đàn voi ma mút, bão tuyết, hai người trú sau tảng đá. Hổ phách cùng một hóa thạch kích hoạt cổng.
4. **Cảnh 08–10:** Biển cổ đại với bọ ba thùy và bọ cạp biển, sóng dữ, nhảy cổng.
5. **Cảnh 11–14:** Rừng kỷ Than Đá có chuồn chuồn và cuốn chiếu khổng lồ, đêm trong rừng, cháy rừng, nhảy cổng.
6. **Cảnh 15–19:** Kỷ khủng long. Khủng long cổ dài, thằn lằn bay, **hổ phách vỡ đôi**, núi lửa, T-rex rình rập, dùng drone đánh lạc hướng.
7. **Cảnh 20–22:** (phần kết, không đưa vào cold open)

## 2. Cấu trúc cold open (Phase 3)

| Đoạn | Thời gian | Nội dung | Kỹ thuật |
|---|---|---|---|
| **HOOK** | 0,00 – 6,50 | T-rex trồi lên trên đầu hai người đang nấp (thấy được ngay giây thứ 0), rồi cận mặt nín thở | Mở bằng cold open, không logo. Smash cut sang đen 0,5 giây, nhạc cắt cụt |
| **MYSTERY** | 7,00 – 24,6 | Công trường yên bình, lộ ra vật hình đĩa, hổ phách ra ánh nắng, hổ phách bừng sáng, băng giá phủ cửa sổ, cổng mở ra thế giới tuyết | Tương phản bình yên và siêu nhiên. Tiếng tích tắc, riser dẫn vào cổng |
| **ESCALATION** | 24,6 – 47,8 | Bão tuyết với đàn ma mút, chạy trốn, nhảy cổng giữa sóng, chuồn chuồn khổng lồ, cuốn chiếu khổng lồ, cháy rừng, tiếng thét, lao vào cổng | Nhịp cắt nhanh dần (từ 2,8 giây xuống 1,6–2,3 giây mỗi cảnh). Cắt theo chuyển động, xen cảnh rộng và cận. Ostinato 120bpm |
| **CLIMAX** | 47,8 – 60,7 | Khoảnh khắc chậm: ngước nhìn khủng long cổ dài, rồi T-rex tiến sát, rồi T-rex bước ngay sau lưng | Ngắt nhịp để tạo tương phản (hợp xướng). Braam cùng trống dồn, riser |
| **CLIFFHANGER** | 60,7 – 68,6 | Hổ phách vỡ đôi, anh quay phim sững sờ, cô gái bật khóc | **Im lặng kịch tính** (cắt toàn bộ nhạc, chỉ còn tiếng gốc và một nốt piano trầm). Cắt đen đột ngột |
| Đen | 68,6 – 69,8 | Tiếng nổ trầm kéo dài | Cut to black 1,2 giây |
| Title | 69,8 – 74,0 | HỔ PHÁCH · NGƯỢC DÒNG TIỀN SỬ | Lấy từ intro title đã dựng trước |

**Không làm lộ kết phim:** cold open không có cảnh trở về hiện tại (cảnh 21), không có drone hóa thạch (cảnh 22), không có cảnh chôn hộp hay đổ thạch cao (cảnh 20). Chi tiết hổ phách vỡ chỉ đặt câu hỏi ("làm sao về được?") mà không trả lời.

## 3. Hình ảnh (Phase 4)
- Upscale từ 720p lên 1080p bằng lanczos.
- Grade nhẹ, đồng nhất cho mọi cảnh: tương phản +7%, giảm bão hòa 7%, vùng tối hơi xanh teal, vùng sáng hơi ấm, vignette, grain rất nhẹ. Giữ đúng tông của footage gốc.
- Letterbox 2.39:1. Đã kiểm tra từng cảnh, không cắt mất mặt nhân vật. Viền đen này cũng che được các vạch đen lỗi ở đầu một số clip gốc (01_1, 14_1, 21_1).
- Không dùng zoom, glitch hay flash nhân tạo. Các khoảnh khắc chuyển kỷ nguyên dùng ánh sáng cổng thời gian có sẵn trong footage.

## 4. Âm thanh
- **Tiếng gốc:** giữ trên toàn bộ phim, fade 15ms ở mỗi điểm cắt để không có tiếng "click". 8 cảnh được ưu tiên tiếng gốc (hơi thở T-rex, tiếng hét, hổ phách vỡ, tiếng khóc), nhạc tự giảm khoảng 7 dB dưới các cảnh này.
- **Nhạc:** do mình tự soạn và tổng hợp từ đầu (không dùng mẫu, không có bản quyền), cắt khớp từng đoạn hình như bảng ở mục 2.
- **Master:** compressor 2.5:1 rồi chuẩn hóa về **−13,5 LUFS** (mục tiêu −14), True Peak **−1,4 dBTP**, LRA 4,1 LU.

## 5. Kiểm tra chất lượng (QC)

| Kiểm tra | Kết quả |
|---|---|
| Khung hình lọt từ góc máy khác | **Lỗi ở bản 1, đã sửa.** Ba cảnh (S1, S18, S25) dính 1–5 khung hình của góc máy trước, do trong clip gốc có điểm cắt nội bộ. Mình dò điểm cắt nội bộ của cả 18 clip đã dùng, chỉnh lại in/out cho cách điểm cắt ít nhất 0,04 giây, rồi render lại. Bản cuối không còn điểm cắt nào nằm giữa cảnh |
| Khung đen ngoài ý muốn | Không có. Chỉ có đen ở 6,5–7,0s (smash cut), 68,6–69,8s (cut to black) và lúc fade cuối |
| Đồng bộ tiếng và hình | Tiếng gốc được cắt cùng in/out với hình, đặt khớp từng mẫu âm. Lệch tổng sau ghép dưới 1 khung hình (74,0s so với 73,98s) |
| Âm lượng | −13,5 LUFS / −1,4 dBTP, không bị clip |

### Tự đánh giá
1. **3 giây đầu có giữ người xem không?** Có. Đầu T-rex xuất hiện ngay giây đầu, hai người đang nấp ngay bên dưới.
2. **Có thành một câu chuyện nhỏ không?** Có. Đi từ nguy hiểm, quay về khởi đầu bình yên, qua hành trình qua các kỷ nguyên, tới khủng long, tới mất chìa khóa trở về.
3. **Nhịp có ra chất điện ảnh hay chỉ là montage ngẫu nhiên?** Đoạn nào cũng có mục đích: tương phản, leo thang, ngắt nhịp, im lặng.
4. **Âm thanh có tăng cảm xúc không?** Có hai khoảng lặng chủ đích (sau hook và lúc hổ phách vỡ). Nhạc đi lên theo từng đoạn.
5. **Đoạn kết có khiến người xem muốn xem tiếp?** Hổ phách vỡ, nhân vật khóc, cắt đen, rồi hiện tên phim.
6. **Có lộ tình tiết quan trọng không?** Không có cảnh nào từ cảnh 20–22.
7. **Lỗi kỹ thuật:** đã sửa toàn bộ lỗi phát hiện ở bản 1.

### Điểm còn hạn chế / gợi ý
- Không có transcript nên chưa chọn được câu thoại "đắt" theo nội dung. Nếu bạn gửi kịch bản hoặc lời thoại của các cảnh, mình có thể đặt một câu thoại bí ẩn làm sound bridge ở phần hook hoặc ngay trước khi cắt đen.
- Footage gốc là 720p nên bản 1080p là upscale. Độ nét tối đa vẫn bị giới hạn bởi nguồn.

---

## 6. Bản phim hoàn chỉnh — `HoPhach_NguocDongTienSu_FULL.mp4`

**Cấu trúc**
1. **Hollywood Cold Open** (0:00 – 1:14): toàn bộ `hollywood_cold_open.mp4`, khép lại bằng title card.
2. **Phim chính** (1:14 – khoảng 23:16): đủ 88 clip theo đúng thứ tự Cảnh 01 → 22, không cắt bớt. Mở vào bằng fade-in từ đen 0,8 giây. Clip cuối fade-out 1,5 giây.
3. **Phần kết** (16 giây): câu "MỖI HÓA THẠCH LÀ MỘT CÂU CHUYỆN CHƯA KỂ", tên phim, rồi "— HẾT —", đi cùng nhạc kết tự soạn (impact, piano, hợp xướng).

**Xử lý phim chính**
- Upscale từ 720p lên 1080p, cùng tông màu và letterbox 2.39:1 như cold open để cả phim đồng nhất. Grain nhẹ hơn để giữ dung lượng.
- Âm thanh: đo loudness từng clip rồi đưa về cùng mức −15 LUFS, nên thoại giữa các clip không lúc to lúc nhỏ. Có limiter chống vỡ tiếng và fade 12ms ở mỗi điểm nối để không có tiếng "click".
- Mã hóa H.265/HEVC (thẻ hvc1, phát trực tiếp trên macOS/iOS/QuickTime, đăng được TikTok và YouTube). Mục đích là giữ cả phim trong một file dưới 400MB mà vẫn ở 1080p.
