# Dựng lại bản 3 — 19/11/2026 (máy Mac mini)

**File:** `tap/Vo_toi_mat_tri_nho_FULL_v3.mp4` (25 phút 18 giây, 1280×720, 24 khung/giây) và 23 file từng phần trong `tap/phan_v3/`.
**Cách dựng:** `python3 tap/make_full3.py seg → full → full2` (`parts` cho file từng phần). Dữ liệu sửa hình theo từng shot: `tap/fix_v3.json`.

Lưu ý: toàn bộ file mp4 trên máy này đã bị xoá sau lần `git pull` lúc 01:11 (mp4 không nằm trong git). Đã tải lại toàn bộ clip từ Flow và tách vào `clips/full_p04_p25/` bằng `clips/organize_zip.py` (nay nhận cả tên R3, R4…).

## Bản sửa 19/11 (tối) — cảnh thoại giữ người đang nói trong khung
Render lại trên Flow 9 clip (540 tín dụng): 09-1…09-4 (cảnh hẹn bờ hồ: đồ trên bàn cố định, hội thoại quay hai người/cận đúng người nói), 14-2, 22-1, 23-1, 08-1 (2 lần — lần đầu Mai Anh nói câu của Linh).
Khi dựng: 09-2 lật ngang cho đúng trục với 09-1/09-3; 09-4 bỏ shot đầu (khung ngắm + chữ "24 fps"); 22-1 bỏ shot đầu (giao diện máy quay); 08-1 bỏ câu "ly hôn" bị nói lặp trong shot hai người.
Câu lệnh: flow_fix2/gen.py → fix2.json. Clip cũ lưu ở clips/full_p04_p25/_old_1911/.
Trailer bản 4 (kiểu trailer chiếu rạp, 2.39:1, thẻ chữ vàng nền tàn lửa, phụ đề tiếng Anh): trailer/v4/make_trailer4.py → Trailer_Vo_toi_mat_tri_nho_v4.mp4.

## Render lại hôm nay (5 clip × 60 tín dụng = 300 tín dụng)
| Clip | Lỗi cũ | Kết quả |
|---|---|---|
| 23-1 (R3) | Mất câu "Hợp đồng thử việc làm chồng. Sáu tháng." | Đạt — nghe rõ câu mở, điều một, "Đồng ý" |
| 20-1 (R2) | Mất "Giám đốc ngoại tình." | Vẫn mất câu này; khi dựng cắt câu lặp, đưa ảnh trên màn chiếu vào giữa: "Vợ mất trí." → ảnh → "Quỹ Hoa Anh Đào sẽ rút vốn." |
| 11-1 (R) | Câu chốt "…với đối tác Nhật" bị cụt | Đạt phần lớn: "…hay đi họp với đối tác của mình" (khác kịch bản 1 chữ, nghĩa giữ nguyên) |
| 10-4 (R) | Mất "không còn tỉnh táo" | Đạt câu chính; mất vế "Rồi gạt cô ấy ra" (vẫn hiểu). Có dấu ✦ + chữ "24 fps" góc phải → đã xoá khi dựng; bỏ 1,8s cuối (lia về phòng trống) |
| 25-6 (mới) | Kết phim không có trẻ em | Đạt: Tuấn cười một mình → kẹp tóc hoa anh đào trên bó hồng → hai vợ chồng ngắm pháo hoa |

## Sửa khi dựng (không tốn tín dụng)
| Loại | Clip | Xử lý |
|---|---|---|
| Viền đen trên/dưới, khung bo góc, viền hai bên | 04-1 04-2 04-3 05-1 05-4 06-1 07-1 07-2 07-3 07-4 08-2 08-4 09-2 09-3 09-4 10-5 12-1 13-2 13-3 15-3 16-1 16-2 17-4 18-1 18-3 21-4 21-5 22-1 24-1 24-2 25-1 và 20 shot trong bản V3 | Cắt vào khung hình sạch theo từng shot, giữ 16:9, phóng lại 1280×720 (máy dò tự động, đã soát lại 2 lần: không còn viền) |
| Dấu ✦ (Gemini) chép từ ảnh nhân vật | 04-3, 08-1, 10-1, 10-4, 11-2 | Xoá (delogo) đúng vị trí, đúng đoạn |
| Chữ "Quan" trên hình | Bản V3 159,2–160,4s | Phóng nhẹ shot đó để chữ ra ngoài khung (không còn vệt mờ) |
| Khung đen | Bản V3 2,83s | Cắt |
| Cảnh ví hất đổ ly rượu vô lý (bàn đã trống, ví "bay" vào khung) | Bản V3, phút 1:04–1:06 | Bỏ cú hất, giữ 1s vết rượu loang sau khi Linh rời bàn |
| Váy trắng Mai Anh dính vết đỏ (shot 02-01) | Bản V3, phút 1:06–1:09 | Bỏ shot, vào thẳng cận Mai Anh |
| Loé trắng cuối phần 9 | 09-4 13,5–15s | Cắt |
| Dải chữ máy quay "24 fps · ALEXA 35 · 00.45mm" ở mép trên | 20-4 (0–3,9s) | Phóng nhẹ shot để đẩy dải chữ ra ngoài khung |
| Thoại lặp / chữ đè / khung ngắm | 05-4, 07-1, 14-1, 14-2, 22-1 | Cắt đoạn lỗi (đã nghe lại sau khi cắt: câu liền mạch) |
| Máy quay / đèn chiếu / cảnh thừa | 17-4 (sau 11s), 18-3 (sau 13,45s), 21-4 (sau 10,95s) | Cắt |
| Kết phim | 25-5 (giữ 0–5,5s) + 25-6 | |

## Còn để nguyên (nhỏ, chấp nhận)
- 20-1: thiếu câu "Giám đốc ngoại tình" (ý vẫn rõ nhờ ảnh trên màn chiếu).
- 20-2: vật mờ tiền cảnh hình chữ ∩ trong 3 giây.
- 23-4: trứng ốp hoà vào lịch; 25-4: một cú hoà hình ngắn trong cảnh Tuấn và Bống.
- Lặp chữ nhẹ ở 08-5, 14-3, 19-2, 22-2.
- Âm lượng toàn phim −18 LUFS (đủ nghe; nếu đăng nền tảng yêu cầu −14 thì chuẩn lại).

---

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
