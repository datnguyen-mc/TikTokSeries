# Kiểm tra lỗi bản FULL (18/11/2026) — soát từng shot (283 shot, 2 khung/shot, xem tap/_qc/shots_*.jpg)

## Lỗi phát hiện
- **Máy quay / chân máy lọt vào khung hình** (nguyên nhân: câu lệnh có "locked off on a tripod", "recorded close on set", "spoken on camera"):
  04-2, 04-3, 05-1, 05-2, 05-3, 05-4, 06-1, 06-2, 07-1, 07-4, 08-1, 09-4, 10-2, 11-2, 12-3, 14-1, 14-2, 14-3,
  15-1, 15-2, 15-3, 16-3, 17-2, 17-3, 17-4, 19-2, 19-3, 20-1, 20-2, 21-1, 22-3, 23-1, 23-2, 23-3, 23-4,
  24-1, 24-2, 24-3, 25-3, 25-5
- **Giao diện máy quay / điện thoại đè lên hình:** 22-3 (thanh HUD ghi hình), 24-1 (giao diện camera điện thoại)
- **Nhân vật bị nhân đôi trong cùng khung:** 13-1 (4 người ở ghế sau thay vì 2)
- **Sai ngày/đêm:** 17-2, 17-3 (cảnh đêm thứ bảy mưa nhưng ra ban ngày)
- **Thiếu hành động:** 19-3 shot 4 (không thấy tay cài áo vest trắng)
- **12-2** bị Flow chặn 6 lần → thiếu.

## Cách sửa (đang làm)
- Đổi câu lệnh: "a completely static frame", "close, natural dialogue sound", "spoken in frame"; AVOID thêm
  máy quay, chân máy, đèn, micro, đoàn phim, lớp phủ máy quay/điện thoại, nhân vật xuất hiện hai lần.
- 17-2, 17-3: đổi bối cảnh sang sảnh biệt thự ban đêm, mưa.
- Render lại 41 clip trên (≈ 2.460 tín dụng), soát lại từng shot, rồi ghép lại có thẻ tên phần để người xem theo dõi.
