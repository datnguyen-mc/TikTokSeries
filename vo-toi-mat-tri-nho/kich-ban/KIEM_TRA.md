# Kiểm tra kịch bản

1 điểm cần xem:

- 06-03: câu thoại cần ~3.1s nhưng shot chỉ 3s (khi render sẽ tự kéo dài)

## Rà soát nội dung (đọc lại toàn bộ 25 phần, 18/11/2026)

Đã kiểm tự động: người nói luôn có mặt trong khung, mã trang phục khớp đúng nhân vật, tối đa 2 người/khung, thoại 100% tiếng Việt, câu treo cuối mỗi phần có trong thoại, đủ thời gian nói.

**Đã sửa**
- **P25 (kết phim):** thoại "Chín mươi chín bông là cho em. Bông thứ một trăm là anh." (trả cho câu P01 "Thiếu đúng một bông là anh ấy") nhưng hình lại là bó **cúc trắng**. Đã đổi thành Quân **tự tay** ôm bó 99 bông hồng đỏ (đối xứng P01, lần này không nhờ Tuấn); kẹp tóc hoa anh đào cài lên bó hồng ở shot cuối. Đã cập nhật `_v2/parts3.py`, `CAU_CHUYEN.md`, prompt `flow_v2/` và `flow_15s/`.

**Để nguyên (có chủ ý)**
- **P03:** Linh "quên đúng mười năm" nhưng vẫn nhớ Bống (7 tuổi) — đây là chính cái "có chọn lọc", Quân và Khang thoại ngay về điều này.
- **P11:** Linh gọi Mai Anh là "chị" vì đang đóng vai cô gái 22 tuổi; tới câu chốt mới xưng lại "chị".
- **06-03:** câu của Quân dài hơn shot 0,1 giây — khi tạo prompt, shot tự kéo dài cho đủ.

**Lưu ý**
- **Trailer** dùng câu rút gọn khác bản phim một chút: T2 "Bỏ ra! Tôi còn chưa có người yêu!" (phim P03: "Bỏ tay ra! Tôi còn chưa có người yêu đâu đấy!"); T7 gộp thoại P20 và P21. Bình thường với trailer.
- **P01–P03** đã render theo bản 3; P04–P25 chưa render (prompt 15 giây trong `flow_15s/`).
