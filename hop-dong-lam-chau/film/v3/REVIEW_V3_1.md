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

## Đợt 5 (19/11, mac-mini): tải lại toàn bộ, soát lại, dựng lại
- Tải lại 229 clip từ Flow (bản mới nhất của từng shot; 59 shot cảnh 01–06 dùng bản gốc đã có trong Downloads, 01-11 và 03-13 dùng bản đã sửa logo). Bảng mã → video id: `clips/_ids.json`.
- Soát: 4 khung/shot cho cả 229 shot, góc trên trái/phải để bắt logo kênh truyền hình (không còn shot nào có logo), nghe thoại bằng máy so với kịch bản (khớp; các đoạn "lạ" ở shot không thoại là máy nghe nhầm tiếng nền).
- Bỏ khi dựng (`dung_phim.py` → `CUT_SHOTS`): 02-04 (ông sơn một cái ghế cỡ người lớn, lệch với ghế con ở 02-01/02-02), 12-02 (ghế "trẻ con" lại cỡ người lớn), 16-01 (di ảnh đen trắng, khác di ảnh màu ở các shot sau).
- Làm lại 20-06 trên Flow: Minh ngồi thụp xuống chiếc ghế con, đầu gối lên tới cằm, bật cười. Clip mới có khung viền kiểu cuộn phim → phóng tay 12% (`MANUAL_CROP`). Bản cũ để ở `clips/_cu/`.
- `ghep_tung_phan.py`: tự đo viền đen từng clip (chỉ cắt khi có viền cả hai phía, khung bo góc cắt sâu thêm), shot ngắn hơn kế hoạch thì cắt theo độ dài clip để không đứng hình/lệch tiếng.
- Kết quả: `Hop_Dong_Lam_Chau_FULL.mp4` 17:44 (1064 giây), 268 đoạn, hình và tiếng dài bằng nhau.
- Còn để ngỏ (lỗi nhỏ): 01b-07 người hỏi "Tập đóng phim à cháu?" là một ông khách thay vì bà cụ; di ảnh bố Minh ở cảnh 16 vẫn khác nhau đôi chút giữa các shot.

## Đợt 6 — Sửa lỗi mất tiếng (19/11)
- Nguyên nhân: nối concat `-c copy` làm dư ~1 gói AAC ở mỗi điểm nối (247 điểm) → track tiếng dài 1074,9 s so với hình 1066,1 s; tiếng lệch dần tới ~8 s cuối phim, có trình phát nuốt mất tiếng.
- Sửa: dựng lại tiếng chính xác từng mẫu theo số khung hình từng đoạn (_meta/timeline_exact.txt), mux lại với hình gốc. Kiểm tra khớp môi 5 điểm (01-04, 08-03, 13-05, 18-04, 20-09): lệch 0 ms.
- 21 thẻ tiêu đề/màn đen trước đây im lặng tuyệt đối → lót nhạc Flow Music (đoạn êm của track A), tràn mềm 1,4 s sang đầu cảnh. Không còn đoạn câm >0,4 s (ngưỡng −50 dB). Âm lượng −16,4 LUFS.
- _tools/ghep_tung_phan.py đã sửa phần concat để không tái phát (bản cũ: .bak). Lưu ý: lót nhạc dưới thẻ chưa nằm trong script — nếu dựng lại cần lót lại.
- Bản cũ: _cu/Hop_Dong_Lam_Chau_FULL_lech_tieng.mp4
- Trailer: thay chỗ ngắt nhạc cứng 0,6 s trước tiêu đề bằng đoạn nhạc tắt dần; lấp khoảng hở ở 112 s. Bản cuối: trailer/Hop_Dong_Lam_Chau_Trailer.mp4 (2:01, −14 LUFS).

## Đợt 7 — Soát logo & nhất quán (19/11)
- Soát 226 shot: soi phóng 4 góc + máy dò vùng đứng yên theo cửa sổ 1,5 s trên toàn thời lượng → không thấy logo kênh truyền hình (chỉ bắt được dòng tên nhân vật do mình chèn).
- Bà Thoa sai mặt/tóc: 03-02 (tóc bạc búi), 03-05 (người khác, tóc đen thẳng) → thay bằng bản gốc V3 trong Downloads (2108b2d7, 3e4c2652), thoại khớp. 19-06 (tóc bạc búi, không thoại) → bỏ (`CUT_SHOTS`). Bản cũ ở `clips/_cu/`.
- Dựng lại FULL (17:42, 267 đoạn, tiếng chuẩn từng mẫu + nhạc dưới thẻ, không đoạn câm). Trailer: thay 03-05 mới (0,6–2,45), bớt đầu 04-01 cho giữ nhịp nhạc.

## Đợt 8 — Làm lại 15-07 (19/11)
- 15-07 "Ông nhìn Minh": bản cũ quay qua vai, ông quay mặt nhìn ra ngoài chứ không nhìn Minh. Tạo lại trên Flow (hai nhân vật tham chiếu, khung ngang hai người đối diện, ông ngẩng lên nhìn thẳng Minh), chọn bản 209437f7, kéo dài 4 s (`DUR`). Bản cũ ở `clips/_cu/`.
- Dựng lại FULL (tiếng chuẩn từng mẫu + nhạc dưới thẻ, không đoạn câm).

## Đợt 9 — Sửa lệch hình/thoại (19/11)
- Nguyên nhân: 5 shot (04-02, 04-06, 04-08, 05-01, 05-02) clip gốc 4 s nhưng kế hoạch 5–8 s → hình dừng ở 4 s còn tiếng được đệm dài; khi nối, hình bị chừa trống 1–4 s mỗi chỗ → từ ~phút 4 hình chậm hơn tiếng tới ~9 s, thoại lệch miệng.
- Thêm: 01-08 và 14-07 trong _norm2 là bản cũ ngắn 1 s (mất đuôi "gấp đôi", "đi khâu") → dựng lại đủ 5 s / 8 s.
- Sửa: cắt tiếng 5 shot trên bằng đúng hình; `one()` đo độ dài theo luồng hình; dựng hình bằng cách giải mã từng đoạn ra khung rồi mã hoá liền mạch (`_meta/pipe_enc.sh`), tiếng cắt theo đúng số khung từng đoạn.
- Kết quả: FULL 17:36 (25.344 khung), hình = tiếng, mốc thời gian đều; so 12 điểm rải khắp phim: hình đúng khung, tiếng lệch 0 ms. Bản lỗi cũ: `_cu/FULL_lech_hinh_9s.mp4`.

## Đợt 10 — Làm lại 3 cảnh mở đầu (19/11)
- 01-01 (Đạt xuống xe) tự nhảy góc máy giữa clip ở giây 2,3; 01-02 mặt Đạt khác 01-01; 01-03 người qua đường che Bà Mận và Đạt.
- Tạo lại trên Flow bằng Omni 1.1 Flash (theo yêu cầu), mỗi cảnh 2 bản, máy liền một góc (01-01 dolly tiến chậm; 01-02, 01-03 chân máy cố định, không ai che). Chọn: 01-01 bản B, 01-02 bản B (bản A lặp câu 3 lần), 01-03 bản B. 01-02 kéo 4 s (`DUR`), 01-01 phóng 8% bỏ viền bo góc (`MANUAL_CROP`).
- Dựng lại FULL (17:37, 25.365 khung, hình = tiếng, mốc thời gian đều); trailer v2 thay cảnh 01-01 mới.

## Đợt 11 — Làm lại 18-11 (19/11)
- 18-11 "Cõng ông qua bờ ruộng" (~15:04): tư thế cõng sai (máy sau lưng Minh mà mặt ông quay về máy, ba lô kẹp giữa hai người, chân ông chạm đất).
- Tạo lại bằng Omni 1.1 (6 s, 2 bản): khung ngang, ông áp lưng Minh ôm qua vai, chân lơ lửng, ba lô đeo trước ngực. Chọn bản ad448fb2 (cận hơn, thấy mặt ông). Bản cũ ở `clips/_cu/`.
- Dựng lại FULL. Tín dụng Flow đã hết sau lượt này.

## Đợt 12 — Shorts + sửa 17-06 (19/11)
- 17-06: clip Flow bị cụt giữa chữ "bố" ("đẹp như b…") → kết cảnh ở 7,32 s sau "nó mặc áo trắng" (`DUR`). Đã dựng lại FULL.
- 4 shorts dọc 9:16 trong `shorts/` (mô tả đăng bài: `shorts/MO_TA_SHORTS.md`).
