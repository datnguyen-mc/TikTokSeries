# Rà soát bản V3 → kế hoạch V3.1 (18/11)

## Đã rà
- 219 shot: thời lượng, cắt cảnh, âm lượng, viền đen (tự động); lời thoại (chuyển giọng nói thành chữ, so với kịch bản); hình (xem từng shot).

## Thay đổi cách dựng (theo góp ý: bỏ cảnh trùng, phim liền mạch, dẫn dắt người xem)
- **Bỏ cảnh 00** (mở đầu kể trước): trùng gần hết cảnh 11 (cổng nhà, Minh xuất hiện, bà Thoa ló qua tường, ông ra hiên). Phim nay chạy đúng thứ tự thời gian, bắt đầu từ bến xe 26 Tết.
- **Thẻ chữ thời gian/nơi chốn** trước các mốc (19 thẻ) và **tên nhân vật** ở lần xuất hiện đầu (Đạt, bà Mận, ông Thịnh, bà Thoa, Minh). Xem `_tools/dung_phim.py`.
- Mốc thời gian được sắp lại cho khớp: 26 bến xe → 26 chiều về nhà → 27 thi kiến thức/dị ứng/gác xép → 28 chợ hoa, gói bánh, canh nồi bánh → cùng đêm Minh thấy clip → 29 tảo mộ, tối bà kể, khuya Minh về → 30 sáng cổng nhà … tất niên → giao thừa → mùng 1.
- **Bà Thoa** đổi sang cầm điện thoại bằng tay (bỏ gậy selfie trông như máy quay). Tạo ảnh tham chiếu mới trên Flow: “Bà Thoa · Cầm điện thoại”.
- 29 shot có viền đen mỏng sẽ được phóng 8% khi ghép (danh sách CROP trong `dung_phim.py`).

## Shot làm lại trên Flow (40 shot)
| Lý do | Shot |
|---|---|
| Lộ máy quay trong khung | 03-03 |
| Bà Thoa gậy selfie → cầm tay | 03-01 03-02 03-04 03-05 03-06 03-08 03-10 03-15 04-03 04-04 07-10 11-03 13-07 14-01 15-04 15-05 |
| Viền đen dày / khung bo góc | 01-06 01-14 01-16 02-13 03-07 04-05 04-12 05-06 06-04 10-06 10-07 16-02 18-02 19-08 |
| Sai nội dung | 02-04 (vẽ giấy thay vì sơn ghế con) · 06-02 (bánh của Đạt phải méo) · 09-04 (Đạt mặc nhầm áo, trông như Minh) · 12-02, 20-06 (ghế không ra ghế trẻ con) · 12-06 (không thấy nổi mẩn ở cổ tay) · 20-12 (thừa một người áo dài) |
| Thoại lỗi | 01-08 (câu bị cụt → “Điều năm, hợp đồng ghi rõ: không được để lộ.”) · 05-03 (lặp “như mọi năm”) |

Mọi prompt làm lại đều thêm: khung 16:9 kín, không viền, không bo góc, không máy quay/chân máy/gậy selfie/micro trong hình.

## Ghép lại (khi đã tải clip mới về `clips/`)
```
python3 hop-dong-lam-chau/_tools/ghep_tung_phan.py norm    # chạy lặp tới khi "còn 0"
python3 hop-dong-lam-chau/_tools/ghep_tung_phan.py concat
```

---
## Đợt 2 (18/11 tối): rà 8 khung/shot cho 173 shot cũ + thêm cảnh
Kiểm tra tự động độ chuyển động từng khung (bắt nhảy hình): chỉ 02-12 có chuyển động mạnh ở giây 4,5 (ông đứng dậy), xem từng khung thì liền mạch, giữ.

| Shot | Lỗi thấy trong khung hình | Xử lý |
|---|---|---|
| 18-05 | Người ngồi tiền cảnh là một thanh niên tóc đen (trông như Minh thứ hai), không phải ông | Làm lại: ông đội mũ len ngồi tiền cảnh |
| 18-08, 18-10 | 18-06 Minh ngồi xuống cạnh ông, nhưng 18-08/18-10 cả hai lại đứng | Làm lại: cả hai ngồi bệt trước mộ |
| 20-02 | Đạt áo đỏ cầm lái, sau lưng thêm một người | Làm lại: Minh áo len kem lái, Đạt ngồi sau, đội mũ bảo hiểm |
| 10-01, 14-04 | Viền đen / khung bo góc | Thêm vào danh sách phóng 8% |
| 16-01…16-07 | Di ảnh bố Minh trên bàn thờ khác nhau giữa các shot | Ghi nhận, chưa sửa (lỗi nhỏ, khó thấy khi xem nhanh) |

## Phân cảnh mới (`_tools/build_shots_3.py`)
- **01b · Học làm cháu trên xe buýt về làng** (9 shot, ~43s), sau cảnh bến xe: bà Mận kiểm tra bài, Đạt sờ cằm nhẵn ("Nhưng cằm cháu làm gì có sẹo hả bà?"), trả lời "Lạc ạ!", tập gọi "Ông ơi!" to đến mức gà trong lồng kêu và cả xe quay lại. Cài sẵn chuyện sẹo và dị ứng lạc cho các cảnh sau.
- **18b · Những đêm đóng ghế** (7 shot, ~36s), sau khi Đạt lặng lẽ đi, trước bến xe: ông bào gỗ trong đêm, ghi sổ "Thằng bé tên Đạt. Mồ côi. Ăn được lạc.", đắp chăn cho Đạt ngủ, đóng xong chiếc ghế mới, bà hỏi "Ông đóng ghế cho ai thế?" ("Cho đứa nào cần ghế."), rồi gửi hộp qua tường nhờ bà Thoa "Tối ba mươi, mang ra bến xe hộ tôi". Nối thẳng vào 19-06/19-07, lúc bà Thoa mở hộp ra ghế.

## Đợt 3 (18/11 khuya): nghe lại thoại + soát logic kịch bản
| Shot | Lỗi | Xử lý |
|---|---|---|
| 01-08 | Bản làm lại hôm nay đổi câu thành "hợp đồng ghi rõ: không được để lộ" → shot sau (01-09 "Gấp… đôi ạ?") mất nghĩa | Làm lại với câu gốc "lộ thì đền gấp đôi", tăng lên 5 giây cho khỏi cụt |
| 13-01 | "Bao nhiêu tiền?" nói lí nhí, gần như không nghe rõ | Làm lại |
| 17-01 | "Điều thứ ba bà bỏ" sai logic (đưa chìa khóa tủ = bỏ điều hai) | Làm lại: "Điều thứ hai bà bỏ." |
| 19-05 | Mất câu cuối "Ông chỉ có cháu." (câu chốt của phim) | Làm lại, tách 3 câu có ngắt nghỉ |
| 20-10 | Ông lặp "nhớ đường về" hai lần | Làm lại |

Thẻ chữ thời gian sửa theo trục của kịch bản (Đạt mặc bomber suốt ngày 26 nên cảnh 02–04 cùng ngày 26; bốn đêm đóng ghế 26–29).
Kịch bản `kich-ban/` đã cập nhật: thoại khớp 100% với prompt phim (máy so từng shot), thêm `canh-01b.md`, `canh-18b.md`, đánh dấu bỏ cảnh 00.

## Việc trên Flow khi đăng nhập lại
1. Render 25 shot của `_tools/build_shots_3.py`: 16 shot cảnh mới (01b, 18b) + 9 shot làm lại (01-08, 13-01, 17-01, 18-05, 18-08, 18-10, 19-05, 20-02, 20-10). Cần ảnh nhân vật "Bà Thoa · Cầm điện thoại" (đã tạo).
2. Tải 39 clip làm lại hôm nay (bỏ 01-08 bản đổi câu) + 25 clip trên.
3. Soát 8 khung/shot + nghe lại thoại cho 64 clip mới.
4. `python3 _tools/ghep_tung_phan.py norm` (lặp tới "còn 0") rồi `concat`.

## Đợt 5 (19/11, mac-mini): tải lại toàn bộ, soát lại, dựng lại
- Tải lại 229 clip từ Flow (bản mới nhất của từng shot; 59 shot cảnh 01–06 dùng bản gốc đã có trong Downloads, 01-11 và 03-13 dùng bản đã sửa logo). Bảng mã → video id: `clips/_ids.json`.
- Soát: 4 khung/shot cho cả 229 shot, góc trên trái/phải để bắt logo kênh truyền hình (không còn shot nào có logo), nghe thoại bằng máy so với kịch bản (khớp; các đoạn "lạ" ở shot không thoại là máy nghe nhầm tiếng nền).
- Bỏ khi dựng (`dung_phim.py` → `CUT_SHOTS`): 02-04 (ông sơn một cái ghế cỡ người lớn, lệch với ghế con ở 02-01/02-02), 12-02 (ghế "trẻ con" lại cỡ người lớn), 16-01 (di ảnh đen trắng, khác di ảnh màu ở các shot sau).
- Làm lại 20-06 trên Flow: Minh ngồi thụp xuống chiếc ghế con, đầu gối lên tới cằm, bật cười. Clip mới có khung viền kiểu cuộn phim → phóng tay 12% (`MANUAL_CROP`). Bản cũ để ở `clips/_cu/`.
- `ghep_tung_phan.py`: tự đo viền đen từng clip (chỉ cắt khi có viền cả hai phía, khung bo góc cắt sâu thêm), shot ngắn hơn kế hoạch thì cắt theo độ dài clip để không đứng hình/lệch tiếng.
- Kết quả: `Hop_Dong_Lam_Chau_FULL.mp4` 17:44 (1064 giây), 268 đoạn, hình và tiếng dài bằng nhau.
- Còn để ngỏ (lỗi nhỏ): 01b-07 người hỏi "Tập đóng phim à cháu?" là một ông khách thay vì bà cụ; di ảnh bố Minh ở cảnh 16 vẫn khác nhau đôi chút giữa các shot.
