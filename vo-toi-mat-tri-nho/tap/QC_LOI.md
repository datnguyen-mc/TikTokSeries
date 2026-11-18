# Kiểm tra lỗi toàn phim — cập nhật 18/11/2026 (tối)

Đã soát: hình (283 shot + 1 khung/2 giây cho 35 clip giữ lại + 4 khung/giây cho bản V3), thoại (chuyển giọng thành chữ cả 80 clip + bản V3, so với kịch bản).

## A. Lỗi hình
| Clip | Lỗi | Cách sửa |
|---|---|---|
| 04-2 04-3 05-1 05-2 05-3 05-4 06-1 06-2 07-1 07-4 08-1 09-4 10-2 11-2 12-3 14-1 14-2 14-3 15-1 15-2 15-3 16-3 17-2 17-3 17-4 19-2 19-3 20-1 20-2 21-1 22-3 23-1 23-2 23-3 23-4 24-1 24-2 24-3 25-3 25-5 | Máy quay / chân máy lọt khung | Render lại bằng câu lệnh mới (`flow_15s_fix/`) |
| 06-4 | Chân máy cuối clip | **Bỏ**, gộp câu "Lần này, phải có ảnh" vào cảnh mới 06-5 |
| **21-4** (mới phát hiện) | Cảnh toàn cuối (11–15s) có máy quay trên chân máy giữa phòng họp | Cắt clip ở 10,95s khi dựng (thoại đã nói xong) — không tốn tín dụng |
| 22-3, 24-1 | Lớp giao diện ghi hình / camera điện thoại | Render lại |
| 13-1 | 4 người ở ghế sau thay vì 2 | Render lại, ghi rõ "đúng hai người" |
| 17-2, 17-3 | Đêm thứ bảy mưa mà ra ban ngày | Đổi bối cảnh: sảnh biệt thự đêm mưa bão |
| 19-3 | Không thấy tay cài áo vest trắng | Ghi rõ hành động cài cúc trong khung |
| Bản V3 (P1–3) | Khung đen 0,2s ở 2,83s; chữ "Quan" ở 159,2–160,4s | Đã xử lý khi dựng (cắt khung đen, xoá chữ) |

## B. Lỗi thoại (nghe máy)
| Clip | Lỗi | Xử lý |
|---|---|---|
| **10-1** | Câu chốt bị cắt: "Nhưng bác sĩ…" (mất "đẹp trai thế này thì em nhớ ngay!") | Thêm vào danh sách render lại, nói sớm hơn 1 giây |
| **12-1** | Mai Anh nói lặp "Chị định hắt nước vào mặt em à?" hai lần | Render lại |
| **22-1** | Linh nói "Tôi còn chưa biết gì về anh" hai lần | Render lại |
| 04-3 | Gần như không nghe ra câu "Bệnh án ghi: mất trí nhớ có chọn lọc" | Đã có trong danh sách render lại |
| 05-4 | Mất câu đầu "Nghe nói vợ chú mất trí nhớ", cuối clip nói lảm nhảm | Đã có trong danh sách render lại |
| 11-2 | Lặp câu "Ly thân mà tối nào cũng về ăn cơm" | Đã có trong danh sách |
| 19-2 | Lặp "Con hứa với mẹ rồi" | Đã có trong danh sách |
| 23-1 | Mất câu mở "Hợp đồng thử việc làm chồng. Sáu tháng." | Đã có trong danh sách |
| 15-2, 14-3, 24-2, 24-3, 20-1 | Thiếu/cụt nửa câu cuối hoặc thừa chữ | Đã có trong danh sách |
| V3 (~77s) | "Ly thân mà tối nay vẫn đặt bà… tối nay vẫn đặt bàn kỷ niệm" — vấp | Giữ (nghe như nói vấp tự nhiên) |
| Còn lại | Khớp kịch bản, 100% tiếng Việt | — |

## C. Thiếu cảnh
- **12-2** (lý do Mai Anh quay sang giúp Linh) bị Flow chặn 6 lần. Thử lần 7 với thoại trung tính: "Em nợ anh Hưng một khoản rất lớn." / "Anh ta bảo làm xong việc này thì xoá nợ cho em." (lỗi bị chặn được hoàn tín dụng).

## D. Việc còn lại
- Render 52 clip trong `flow_15s_fix/queue.json` (45 làm lại + 7 cảnh mới) ≈ 3.120 tín dụng.
- Soát từng clip mới (máy quay, nhân bản, ngày/đêm, thoại), đặt tên, tải ZIP dự án, thay vào `clips/full_p04_p25/`.
- Dựng: `python3 tap/make_full2.py seg → cards → trim → full` (thẻ tên phim + tên phần, thứ tự mới).
- Đã thử cắt "khoảng lặng cuối clip" tự động theo âm lượng → làm mất nhịp hình (07-2, 08-4 thuyền giấy, 09-2, 20-4) nên **tắt**, giữ nguyên clip.

## E. Kết quả render lại (18/11, máy Mac thứ hai)
- Đã render 52 clip trong `flow_15s_fix/queue.json` + 9 bản làm lại lần 2 (R2). Tên trên Flow: `Pxx-Cy R · …` (lần 1), `Pxx-Cy R2 · …` (lần 2), `X…` = bản loại.
- Soát hình 12 khung/clip cho toàn bộ bản mới: hết máy quay/chân máy. Lỗi mới gặp và cách xử lý:
  - Lớp giao diện máy quay / chữ "ARRI", "@Linh" trên hình (05-3, 15-2, 17-2, 22-1, 14-2, 05-4): bỏ chữ "ARRI Alexa 35" và "@tên" khỏi câu lệnh (bản R2) hoặc cắt bỏ vài giây đầu khi dựng (14-2: 3,5s; 05-4: 1,3s; 22-1: 3s).
  - Flow chặn 3 clip có bé Bống (16-3, 19-2, 25-5): 16-3 chuyển sang phòng chơi trên thảm, 19-2 dùng cảnh trung hai người → qua. 25-5 bị chặn 2 lần → dùng bản cũ, ghép 0–5,5s + 9,5–13,2s (bỏ đoạn có chân máy).
  - 12-2 (động cơ của Mai Anh) đã render được với thoại "Em nợ anh Hưng một khoản rất lớn…".
- Nghe lại thoại bản mới: đã sửa 10-1, 11-2, 12-1, 04-3, 05-4, 15-2, 23-2. Còn lặp nhẹ kiểu nói nhấn (14-1, 14-3, 19-2) — giữ. Câu lặp/lộn xộn ở 05-4, 07-1, 22-1 cắt bỏ khi dựng (KEEP trong `make_full2.py`). 23-1 bản mới vẫn thiếu câu "Hợp đồng thử việc làm chồng. Sáu tháng." (hình tờ giấy + 22-3 đã gợi đủ).
- Còn nhỏ, chưa sửa: 06-2 Hưng vẫn đứng trong phòng khi Tuấn nói; 20-2 có mảng sáng mờ ở tiền cảnh 9–15s; 17-4 cảnh cuối là đèn máy chiếu.
- Phim mới: `tap/Vo_toi_mat_tri_nho_FULL_v2.mp4` (25,5 phút, có thẻ tên phim + 22 thẻ tên phần).
