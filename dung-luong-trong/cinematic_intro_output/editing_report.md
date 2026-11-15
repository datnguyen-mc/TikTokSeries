# Báo cáo dựng phim — "Dung Lượng Trống"

## 1. Footage đã phân tích
- **72/80 clip** trong `output_videos/` (đều 1280×720, 24 fps, H.264/AAC, 15,04 s; 9 clip bổ sung ở lượt tạo lại) — xem `probe.tsv`.
- Mỗi clip: trích 3 keyframe (2 s, 7 s, 12 s → `keyframes/`, 177 ảnh) và đã xem trực tiếp toàn bộ qua contact sheet; phân tích âm lượng + khoảng lặng (`audio.tsv`): clip nào cũng có tiếng, mean −29…−19 dB.
- Đã đối chiếu hình ảnh với kịch bản từng cảnh → xác nhận tên clip khớp nội dung (lượt tải đầu tiên có gán nhầm tên, đã sửa và loại 1 file chưa xác minh vào `output_videos/_unverified/`).
- **Giới hạn:** không chạy được nhận dạng giọng nói (model Whisper không tải được vì mạng chặn Hugging Face). `transcripts.json` lấy từ kịch bản lời thoại kèm mốc thời gian thiết kế, điểm cắt được kiểm tra lại bằng silencedetect trên audio thật.
- **21 clip không có** (Flow từ chối vì chính sách nội dung, xem `selected_scenes.md`). Đáng kể nhất: toàn bộ cảnh 02 (đòi nợ) và cảnh 14 (Nova báo thu hồi) → phim chính có các bước nhảy cốt truyện ở đó.

## 2. Mạch truyện (rút từ footage)
Hà Nội 2041. Khải — shipper nghèo nợ nần — cho NeuroRent "thuê não" khi ngủ. Anh bắt đầu biết những thứ chưa từng học (bài hát ru tiếng Nhật, mã cửa, khuôn mặt CEO Trịnh Huy) và thấy ký ức cyan về một vụ đẩy ngã. Lần theo dòng chữ "Đừng ngủ" trên tường, anh gặp Vy — cựu kỹ sư NeuroRent: ký ức của người giàu bị chuyển vào đầu người nghèo. Khải phát trực tiếp sự thật trước khi bị "thu hồi".

## 3. Thiết kế Cold Open (73,1 s)
| Phần | Thời gian | Kỹ thuật |
|---|---|---|
| HOOK | 0–4,1 s | Mở thẳng bằng ký ức cyan: Huy gào vào ống kính. Không logo/không lời chào. |
| MYSTERY | 4,1–23,8 s | Smash cut tiếng hét → đêm tĩnh; bút dạ, chữ trên tường "Đừng ngủ"; Nova ngọt ngào báo "phiên thuê não hoàn tất" (tương phản êm dịu/hỗn loạn). |
| ESCALATION | 23,8–51,8 s | Ngón tay tự bấm mã cửa; callback về tiếng hét ("Hắn đang hét vào mặt ai?"); Vy cầm ống sắt; câu chủ đề "Vào đầu những người nghèo…"; Huy chặn cửa; chiếc kính trượt trên sàn trong khoảng lặng. Drone trầm tự tổng hợp bắt đầu làm sound bridge. |
| CLIMAX | 51,8–64,0 s | Chip nháy đỏ, Nova chuyển đỏ "cảnh báo cuối cùng", Khải gồng mình "Tôi vẫn còn nhớ…". Drone tăng dần. |
| CLIFFHANGER | 64,0–69,5 s | Nova: "Phiên thu hồi bắt đầu sớm hơn. Anh sẽ không cảm thấy đau đâu." → cắt phụt sang đen 1,2 s, im lặng tuyệt đối. |
| TITLE | 69,5–73,1 s | "DUNG LƯỢNG TRỐNG / HÀ NỘI · 2041" fade trên nền đen + tiếng trầm 42 Hz; nối thẳng vào cảnh 1 trong bản final. |

Chi tiết từng đoạn: `editing_timeline.json`, lý do chọn + chấm điểm: `selected_scenes.md`.

## 4. Kỹ thuật
- Chuẩn hoá: 1920×1080 (lanczos từ nguồn 720p — Flow chỉ xuất 720p gốc; bản 1080p "tăng độ phân giải" của Flow tốn thêm 5 credit/clip, chưa dùng), 24 fps, yuv420p, H.264 CRF 17–18, AAC 192k 48 kHz.
- Màu: chỉnh nhẹ đồng nhất `contrast 1.04, saturation 0.96`; không flash/zoom/glitch nhân tạo.
- Âm thanh: giữ tiếng gốc; fade 30/60 ms ở điểm cắt chống tiếng "click"; loudnorm EBU R128 −16 LUFS (đo được −16,6 LUFS, peak −1,5 dBFS); bed tension tự tổng hợp (không có nhạc bên thứ ba).
- **Đồng bộ:** phát hiện ghép concat AAC gây lệch tiếng tích luỹ (tới 1,1 s ở phim đầy đủ) → dựng lại: hình cắt theo số khung nguyên, tiếng ghép PCM đúng mẫu, mã hoá AAC một lần. Kết quả: cold open 73,125 s (lệch hình/tiếng 6 ms do làm tròn container), phim đầy đủ 1080,000/1080,000 s, bản final 1153,1 s.
- Sửa lỗi hình: xoá logo "VTV"/"VTVgo" do AI tự vẽ (canh-16_clip-4, canh-11_clip-4) bằng delogo; phóng 6% shot đầu canh-01_clip-2 để bỏ viền đen bo góc.
- Phim chính: cắt cứng giữa các clip trong cùng cảnh, fade-qua-đen 0,5 s giữa các cảnh.

## 5. Final QC
1. **3 giây đầu:** có — mặt giận dữ cận cảnh + glitch + lời đe doạ, không intro.
2. **Câu chuyện nhỏ:** có — bí ẩn (chữ trên tường) → hiện tượng (tay tự bấm) → giải thích một nửa (ký ức bị chuyển) → mối đe doạ (thu hồi) → cliffhanger.
3. **Nhịp:** đoạn đầu 4–6 s, cao trào 3–5 s, khoảng lặng có chủ đích (kính rơi, màn đen); mọi đoạn có câu thoại/hành động phục vụ mạch.
4. **Âm thanh:** dùng thoại gốc + drone tăng dần + im lặng tuyệt đối trước tiêu đề.
5. **Muốn xem tiếp:** kết bằng lời đe doạ "không cảm thấy đau" + cắt đen.
6. **Lộ tình tiết:** không dùng cảnh gọi tên hung thủ, twist ký ức của Vy, hay kết (mất trí nhớ/bắt Huy/bà Tư nhớ lại). Có lộ một cuộc xô xát trong ký ức, nhưng không rõ nạn nhân và hệ quả.
7. **Kỹ thuật:** blackdetect chỉ thấy đoạn đen chủ đích (68,3–73,1 s); decode điểm nối cold open → phim chính không lỗi; tiếng khớp hình.

**Hạn chế còn lại:** 21 clip thiếu khiến phim chính có các bước nhảy (đặc biệt cảnh 02, 14); nguồn 720p nâng lên 1080p; transcript là kịch bản chứ không phải ASR.

## 6. File đầu ra
- `hollywood_cold_open.mp4` — cold open 73 s
- `dung_luong_trong_full_movie.mp4` — phim chính 18:00 (72 clip)
- `dung_luong_trong_final_with_cold_open.mp4` — cold open + phim chính 19:13
- `editing_timeline.json`, `selected_scenes.md`, `editing_report.md`, `transcripts.json`, `probe.tsv`, `audio.tsv`, `keyframes/`

## 7. Cập nhật lượt tạo lại (tạo lại 21 clip thiếu)
- Thêm 9 clip: 02-1 (bản viết dịu), 05-4, 09-1, 09-2, 09-4, 10-1, 11-2, 14-3, 18-4. Đã kiểm keyframe, khớp kịch bản. Phóng 6% shot đầu 18-4 để bỏ viền đen.
- Đã tạo được trên Flow nhưng **chưa tải về được** (ứng dụng chặn tải xuống từ 05:27): canh-14_clip-4, canh-18_clip-3, canh-19_clip-1 (19-1 là bản dàn lại: Linh đứng ở cửa, không ôm).
- Bị từ chối nhiều lần: 02-3, 02-4, 03-1, 06-1, 14-1, 14-2, 17-2 (chính sách, kể cả bản viết dịu); 02-2, 06-3 ("không tạo được âm thanh" 3 lần).
- Đã tải và ghép thêm 14-4, 18-3, 19-1 (Flow có nhiều bản: chọn 18-3 bản 5a95f6ce vì bản kia đổi áo Linh giữa các shot; 19-1 bản bc15510b đúng kịch bản gốc, không viền). Phim chính: **71/80 clip, 17:45**.
- Còn thiếu 9 clip: 02-2, 02-3, 02-4, 03-1, 06-1, 06-3, 14-1, 14-2, 17-2.

## 8. Viết lại prompt (lượt 3)
- Đã viết lại và cập nhật vào `clip-N.md` + README cho 9 clip thiếu (bản gốc: `_prompt_backup_v1/`). Thành công: **17-2** (bỏ địa chỉ cụ thể và "danh sách tài khoản"). Phim chính: **72/80 clip, 18:00**.
- Vẫn bị Flow chặn sau 2 lượt gửi bản mới (tổng 3–5 lần/clip): 02-2, 02-3, 02-4, 03-1, 06-1, 06-3, 14-1, 14-2 — 7 lỗi chính sách, 06-3 lỗi âm thanh.

## 9. Review vòng 2 – sửa cảnh ngã/chặn người & lỗi logic (14/11/2026)
Đã review cả 72 clip (5 khung/clip, kèm khung dày cho các clip nghi vấn). Cảnh có ngã/chặn người duy nhất trong kịch bản là 10-3; các cảnh đối đầu khác (02-1, 11-3/11-4, 18-2) đều hợp lý.

| Clip | Lỗi | Xử lý |
|---|---|---|
| 10-3 | Cận cảnh Huy chặn cửa không cho thấy vị trí hai người. Cú đẩy không đọc được: Lâm đang đi giữa phòng rồi bỗng nằm cạnh bàn. Thoại "Buông tôi ra!" không khớp. | Viết lại prompt và render mới (8dd21818): two-shot Huy chắn cửa, đẩy ngực Lâm, Lâm loạng choạng lùi, vấp chân bàn, ngồi sụp xuống sàn, kính văng. Thoại 3 đổi thành "Anh điên rồi à!..." |
| 01-3 | Hai Nova cùng lúc: một trên gối và một bóng khổng lồ ở tiền cảnh. | Đổi góc máy Shot 1, chỉ cho phép một hologram; render mới (644f7342). Shot 1 bị letterbox, đã crop về 16:9. |
| 03-3 | Giao diện máy quay hiện trên hình ("Hanoi in 2041", "24 fps", "85mm"). | Render mới (6a5b7107), crop nhẹ viền bo góc ở Shot 1. |
| 03-4 | Dải phụ đề đen có chữ ở đáy hình, Shot 1. | Hai lần render lại đều bị Flow chặn vì chính sách, nên giữ take cũ và crop Shot 1 (0–5s) để bỏ dải chữ và letterbox. |
| 09-3 | Rèm gác xép hiện thành mảnh vải đen bay lơ lửng. | Tả rõ rèm hoa treo trên thanh; render mới (eec6ee7b). |

Bản cũ lưu ở `output_videos/_replaced_v1/`, prompt cũ ở `_prompt_backup_v2/`. AVOID của các clip trên được bổ sung: viewfinder/HUD, thông số ống kính, viền bo góc, dải phụ đề đen.
Cold open: cập nhật điểm cắt 10-3 theo take mới (5.00–9.50s chặn cửa; 13.05–14.95s chiếc kính). Tổng thời lượng giữ nguyên 73.125s.
Đã dựng lại: full movie 18:00 (1080.000s) và bản final kèm cold open 19:13 (1153.13s), H.264 1080p24 + AAC 48k.
