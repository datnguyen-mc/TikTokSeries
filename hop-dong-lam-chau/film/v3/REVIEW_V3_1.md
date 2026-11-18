# Rà soát bản V3 → kế hoạch V3.1 (18/11)

Đã rà: 219 shot (thời lượng, cắt cảnh, âm lượng, viền đen), lời thoại (máy nghe lại, so với kịch bản), hình (4 rồi 8 khung/shot).

## Thay đổi cách dựng
- **Bỏ cảnh 00** (mở đầu kể trước, trùng gần hết cảnh 11). Phim chạy đúng thứ tự thời gian, mở từ bến xe sáng 26 Tết.
- **Thẻ chữ thời gian/nơi chốn** (20 thẻ) và **tên nhân vật** ở lần xuất hiện đầu: `_tools/dung_phim.py`. Trục: 26 = 01–04 (+01b), 27 = 05–07, 28 = 08–10, 29 = 11–16, 30 = 17–20; 18b là hồi tưởng bốn đêm 26–29.
- **Bà Thoa** cầm điện thoại bằng tay (bỏ gậy selfie trông như máy quay). Ảnh nhân vật mới trên Flow: "Bà Thoa · Cầm điện thoại".
- 27 shot có viền đen mỏng được phóng 8% khi ghép (CROP trong `dung_phim.py`).

## Shot làm lại, đợt 1 (đã render 18/11 chiều)
| Lý do | Shot |
|---|---|
| Lộ máy quay trong khung | 03-03 |
| Bà Thoa gậy selfie → cầm tay | 03-01 03-02 03-04 03-05 03-06 03-08 03-10 03-15 04-03 04-04 07-10 11-03 13-07 14-01 15-04 15-05 |
| Viền đen dày / khung bo góc | 01-06 01-14 01-16 02-13 03-07 04-05 04-12 05-06 06-04 10-06 10-07 16-02 18-02 19-08 |
| Sai nội dung | 02-04 (vẽ giấy thay vì sơn ghế) · 06-02 (bánh của Đạt phải méo) · 09-04 (Đạt mặc nhầm áo) · 12-02, 20-06 (ghế không ra ghế trẻ con) · 12-06 (không thấy nổi mẩn) · 20-12 (thừa người) |
| Thoại | 05-03 (lặp "như mọi năm") |

## Shot làm lại, đợt 2 (`_tools/build_shots_3.py`, REDO)
| Shot | Lỗi | Xử lý |
|---|---|---|
| 18-05 | Người ngồi tiền cảnh là thanh niên giống Minh, không phải ông | Ông đội mũ len ngồi tiền cảnh |
| 18-08, 18-10 | 18-06 Minh ngồi xuống cạnh ông, 18-08/18-10 lại đứng | Cả hai ngồi bệt trước mộ |
| 20-02 | Đạt cầm lái, thêm người lạ | Minh áo len kem lái, Đạt ngồi sau |
| 01-08 | Bản đợt 1 đổi câu → 01-09 "Gấp… đôi ạ?" mất nghĩa; bản gốc bị cụt | Câu gốc "lộ thì đền gấp đôi", 5 giây |
| 13-01 | "Bao nhiêu tiền?" nói lí nhí | Làm lại |
| 17-01 | "Điều thứ ba bà bỏ" sai logic (đưa chìa khóa tủ = bỏ điều hai) | "Điều thứ hai bà bỏ." |
| 19-05 | Mất câu chốt "Ông chỉ có cháu." | Tách 3 câu có ngắt nghỉ |
| 20-10 | Lặp "nhớ đường về" | Làm lại |
| 10-01, 14-04 | Viền đen | Phóng 8% khi ghép |
| 16-01…16-07 | Di ảnh bố Minh khác nhau giữa các shot | Ghi nhận, chưa sửa |

Thoại 09-03, 10-01, 13-02, 14-08 đã đổi so với bản 2 vì Flow từ chối câu gốc. Logic đền tiền vẫn khớp: 01-08 → 04-11 → 13-03.

## Phân cảnh mới
- **01b · Học làm cháu trên xe buýt về làng** (9 shot, 43s): bà Mận kiểm tra bài, Đạt sờ cằm nhẵn "Nhưng cằm cháu làm gì có sẹo hả bà?", trả lời "Lạc ạ!", tập gọi "Ông ơi!" làm gà trong lồng kêu toáng, cả xe quay lại.
- **18b · Những đêm đóng ghế** (7 shot, 36s): ông bào gỗ trong đêm, ghi sổ "Thằng bé tên Đạt. Mồ côi. Ăn được lạc.", đắp chăn cho Đạt, bà hỏi "Ông đóng ghế cho ai thế?" ("Cho đứa nào cần ghế."), gửi hộp qua tường nhờ bà Thoa "Tối ba mươi, mang ra bến xe hộ tôi". Trả ở 19-07.

## Quy trình
1. Tải clip từ Flow về Downloads với tên `V3-<shot>_<id8>.mp4`, rồi `python3 _tools/gom_clip.py` (bản mới nhất mỗi shot thắng).
2. `python3 _tools/ghep_tung_phan.py norm` (lặp tới "còn 0") rồi `concat`.

## Đợt 4 (18/11 đêm, máy Mac mới): render, tải, soát, ghép
- Render 25 shot của `build_shots_3.py` + làm lại 3 shot sau khi soát: **18b-01** (dính logo kênh "VTV5" và viền đen), **10-07** (viền/khung lệch), **03-06** (hai lần mất câu chốt "Mẹ ạ!", lần ba đổi thành "Dạ, mẹ cháu tên là Mẹ ạ!" thì đủ câu).
- Tải đủ 229 clip từ Flow về `clips/` (`_tools/gom_tam.py` ghép file tải tạm của app với mã shot, kiểm tra thời lượng; `clips/_ids.json` ghi id Flow của từng shot). Clip cảnh 00–06 đối chiếu hình với bản cũ trên mac-mini: khớp.
- Soát 8 khung/shot + nghe lại thoại cho 50 clip mới: thoại đều khớp kịch bản.
- Ghép: tự đo viền đen từng clip rồi phóng vừa đủ để mất viền (chỉ khi viền đối xứng). Bản `Hop_Dong_Lam_Chau_FULL.mp4`: 17 phút 57 giây, 229 shot + tiêu đề + 20 thẻ chữ.
- Còn để ý, chưa sửa: 01b-07 người nói là đàn ông trung niên (kịch bản ghi bà cụ, vẫn hợp lý); 02-04 ghế ông sơn chưa nhỏ hẳn; di ảnh bố Minh cảnh 16 mỗi shot một kiểu.
