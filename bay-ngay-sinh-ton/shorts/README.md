# Bảy Ngày Sinh Tồn — Shorts cho TikTok, YouTube Shorts, Facebook Reels

Đây là bản cắt **các cảnh hay nhất** của phim 24 phút, gồm **11 phần dọc 9:16**, không phải cả phim. Mỗi phần là một khoảnh khắc trọn vẹn dài 30–60 giây (mở bằng câu thoại hoặc hành động gây tò mò, kết bằng câu chốt hoặc cliffhanger), xếp theo thứ tự truyện và đăng nối tiếp như một series.

- **Khung hình:** 1080×1920, 24 fps. Cảnh phim 16:9 để nguyên khung ở giữa, nền là chính cảnh đó làm mờ; không cắt mất nhân vật ở hai mép.
- **Chữ trên video:** nhãn xanh rừng “BẢY NGÀY SINH TỒN • PHẦN N” và câu hook ở trên khung phim (cụm nhấn màu cam lửa); phụ đề khớp tiếng ở dưới khung phim (chữ trắng); 2,5 giây cuối, hook đổi thành “CÒN TIẾP » PHẦN N+1” kèm hook của phần sau, phần cuối đổi thành “XEM FULL PHIM”. Mọi chữ nằm ngoài vùng nút bấm và caption của TikTok/Reels.
- **Phụ đề:** lấy từ tiếng thật trong clip (Whisper), chính tả và tên nhân vật sửa theo kịch bản `PHAN_CANH_OMNI.json`. Câu Omni nói khác kịch bản thì phụ đề theo tiếng thật.
- **Âm thanh:** chuẩn hoá −14 LUFS (mức TikTok/YouTube/Facebook dùng).
- **Nhịp:** khoảng lặng cuối mỗi clip được cắt còn 1 giây (clip cuối của phần giữ 1,8 giây cho câu chốt ngấm); clip nào Omni nói lặp lại mấy chữ cuối thì cắt trước đoạn lặp.
- **File:** video nằm phẳng trong `shorts/` dạng `NN-<slug>.mp4`; caption TikTok, tiêu đề + mô tả YouTube và caption Facebook của mọi phần nằm ở cuối `README.md` này.

Dựng lại (sau khi sửa plan hoặc render lại clip):

```bash
WHISPER_PYTHON=~/.venvs/whisper/bin/python ./flowkit/venv/bin/python flowkit/scripts/make_shorts.py bay-ngay-sinh-ton              # tất cả
WHISPER_PYTHON=~/.venvs/whisper/bin/python ./flowkit/venv/bin/python flowkit/scripts/make_shorts.py bay-ngay-sinh-ton --only 4     # một phần
./flowkit/venv/bin/python flowkit/scripts/make_shorts.py bay-ngay-sinh-ton --captions   # chỉ ghi lại README (lịch + caption)
```

Nội dung từng phần (clip, hook, caption, lịch) nằm trong `SHORTS_PLAN.json`.

## Lịch đăng & danh sách phần

| Phần | Video | Nội dung | Cảnh | Thời lượng | Đăng lúc | Ưu tiên |
|---|---|---|---|---|---|---|
| 1 | [`01-vlogger-sinh-ton-an-sau.mp4`](01-vlogger-sinh-ton-an-sau.mp4) | Vlogger sinh tồn diễn ăn sâu, ai ngờ là sâu thật | 01.1, 01.2, 01.3 | 43s | Thứ Bảy 14/11 – 11:00 | ⭐ |
| 2 | [`02-dau-tay-than-lua.mp4`](02-dau-tay-than-lua.mp4) | Ướm tay vào dấu tay thần lửa, sét đánh xuống hang | 03.2, 03.3, 03.4 | 43s | Thứ Bảy 14/11 – 19:00 |  |
| 3 | [`03-te-giac-tuyet-chung.mp4`](03-te-giac-tuyet-chung.mp4) | Tỉnh dậy giữa rừng, gặp tê giác đã tuyệt chủng | 04.2, 04.3, 04.4 | 43s | Chủ Nhật 15/11 – 11:00 |  |
| 4 | [`04-duoi-ho-bang-chan-bac.mp4`](04-duoi-ho-bang-chan-bac.mp4) | Đuổi hổ cứu cậu bé tiền sử bằng tấm chăn 300 nghìn | 06.1, 06.2, 06.3, 06.4 | 56s | Chủ Nhật 15/11 – 19:00 | ⭐ |
| 5 | [`05-mi-tom-sau-kho.mp4`](05-mi-tom-sau-kho.mp4) | Người tiền sử lần đầu ăn mì tôm | 08.2, 08.3, 08.4 | 45s | Thứ Hai 16/11 – 11:00 |  |
| 6 | [`06-cua-tre-ra-lua.mp4`](06-cua-tre-ra-lua.mp4) | Lửa của cả hang tắt, anh cưa tre ra lửa | 09.2, 09.3, 09.4 | 42s | Thứ Hai 16/11 – 19:00 |  |
| 7 | [`07-cuu-nguoi-duoi-ho-sut.mp4`](07-cuu-nguoi-duoi-ho-sut.mp4) | Cứu kẻ muốn đuổi mình khỏi hố sụt | 14.2, 14.3, 14.4 | 44s | Thứ Ba 17/11 – 11:00 |  |
| 8 | [`08-lu-dem-cuu-ong-lua.mp4`](08-lu-dem-cuu-ong-lua.mp4) | Lũ đêm ập về, cậu bé quay lại cứu ngọn lửa | 17.1, 17.2, 17.3, 17.4 | 55s | Thứ Ba 17/11 – 19:00 |  |
| 9 | [`09-ba-trieu-nguoi-xem.mp4`](09-ba-trieu-nguoi-xem.mp4) | Bỏ máy quay giữa lũ để giữ dây cứu cậu bé | 18.2, 18.3, 18.4 | 41s | Thứ Tư 18/11 – 11:00 | ⭐ |
| 10 | [`10-ban-tay-tren-vach.mp4`](10-ban-tay-tren-vach.mp4) | Dấu tay thần lửa trên vách hang hoá ra là của anh | 19.2, 19.3, 19.4 | 44s | Thứ Tư 18/11 – 19:00 |  |
| 11 | [`11-co-gai-ten-suoi.mp4`](11-co-gai-ten-suoi.mp4) | Bàn tay nhỏ bên cạnh là của cô gái tên Suối | 24.2, 24.3, 24.4 | 44s | Thứ Năm 19/11 – 11:00 |  |

⭐ = phần có hook mạnh nhất, nên dồn tương tác hoặc chạy quảng cáo trước.

## Cách đăng

- **TikTok:** đăng theo thứ tự, gom vào Playlist “Bảy Ngày Sinh Tồn”. Chọn ảnh bìa bằng khung hình có hook (giây đầu). Ghim 3 phần ⭐ lên trang cá nhân.
- **YouTube Shorts:** dán tiêu đề + mô tả ở phần caption bên dưới; khi phim full đã lên kênh, điền link vào `full_movie_url` trong plan rồi chạy `--captions` để mọi mô tả có link. Dùng “Related video” của Shorts trỏ về phim full.
- **Facebook Reels:** dán caption; tắt “Tạo phụ đề tự động” vì phụ đề đã in sẵn trên video.
- Mỗi ngày 2 phần (11:00 và 19:00), 3 nền tảng cùng giờ, bắt đầu 14/11/2026. Đổi ngày bắt đầu ở `schedule.start` rồi chạy `--captions`.

## Kiểm tra trước khi đăng

- `subtitle_replace` đang để trống: xem phụ đề Whisper rồi thêm cặp sửa chữ khi cần (tên Suối, Gầm, Ốc, Bin hay bị nghe sai), dựng lại phần đó bằng `--only`.
- `output_videos/` còn vài file phẳng kiểu `canh-01_clip-1.mp4` và một bản tiếng Anh `canh-01_clip-1_EN.mp4`; script luôn lấy bản trong `output_videos/canh-XX/`, nên các file phẳng không lọt vào short.

## Lỗi hình thấy trong clip đã chọn (chưa xử lý)

Plan chưa có `from`/`to` hay `fixes`; xem lại rồi render lại clip, hoặc cắt bằng `from` / `fixes` trước khi đăng.

- **03.2, 03.3** (phần 2): Omni vẽ khung máy quay giả (“24 fps”, “REC”, pin, “08.18m”, “35mm”) suốt cả clip.
- **06.1** (phần 4): viền khung phim đen bo góc khoảng 0–4 s, đúng giây mở đầu của phần.
- **17.2** (phần 8): viền khung phim kèm chữ “Snail @Snail” in trên hình khoảng 0–5 s.
- **24.4** (phần 11): giao diện quay điện thoại có chữ “Khang, 29” và đồng hồ đếm giờ khoảng 0–4 s.
- **Viền đen một lúc:** 04.3 (0–1,8 s), 08.4 (0–4 s), 09.3 (0–6 s), 17.3 (0–5 s và 9–13 s), 17.4 (0–2,8 s). Script chỉ tự cắt viền đen có suốt cả clip, nên các đoạn này vẫn hiện viền.

## Caption từng phần (copy dán)

### Phần 1/11 — Vlogger sinh tồn diễn ăn sâu, ai ngờ là sâu thật

`01-vlogger-sinh-ton-an-sau.mp4` · 43s · cảnh 01.1, 01.2, 01.3 · đăng Thứ Bảy 14/11 – 11:00

**TikTok**

```text
Vlogger sinh tồn Khang diễn cảnh đói lả giữa rừng: “Không còn cách nào khác, tôi phải ăn con sâu này để sống sót!” Tiếc là kẹo dẻo hình sâu đã hết, con trên tay là sâu thật. Lửa trong video là Bin châm hộ bằng bật lửa suốt ba năm, còn sau lưng “rừng sâu” là xe điện chở khách đang vẫy tay.
Bạn từng xem vlog sinh tồn nào “diễn” lộ liễu thế này chưa?

👉 Phần 2 ở trang cá nhân, Follow để xem tiếp!
#bayngaysinhton #sinhton #phimngan #haihuoc #vlogger
```

**YouTube Shorts — tiêu đề** (71/100 ký tự)

```text
Vlogger sinh tồn diễn ăn sâu, ai ngờ là sâu thật | Bảy Ngày Sinh Tồn P1
```

**YouTube Shorts — mô tả**

```text
Vlogger sinh tồn Khang diễn cảnh đói lả giữa rừng: “Không còn cách nào khác, tôi phải ăn con sâu này để sống sót!” Tiếc là kẹo dẻo hình sâu đã hết, con trên tay là sâu thật. Lửa trong video là Bin châm hộ bằng bật lửa suốt ba năm, còn sau lưng “rừng sâu” là xe điện chở khách đang vẫy tay.

🎬 Full phim 24 phút có trên kênh YouTube, tìm “Bảy Ngày Sinh Tồn”
👉 Xem tiếp Phần 2: Ướm tay vào dấu tay thần lửa, sét đánh xuống hang

#Shorts #bayngaysinhton #sinhton #phimngan
```

**Facebook Reels**

```text
Vlogger sinh tồn Khang diễn cảnh đói lả giữa rừng: “Không còn cách nào khác, tôi phải ăn con sâu này để sống sót!” Tiếc là kẹo dẻo hình sâu đã hết, con trên tay là sâu thật. Lửa trong video là Bin châm hộ bằng bật lửa suốt ba năm, còn sau lưng “rừng sâu” là xe điện chở khách đang vẫy tay.

Bạn từng xem vlog sinh tồn nào “diễn” lộ liễu thế này chưa? 👇
👉 Xem tiếp Phần 2: Ướm tay vào dấu tay thần lửa, sét đánh xuống hang
🎬 Full phim 24 phút có trên kênh YouTube, tìm “Bảy Ngày Sinh Tồn”

#BayNgaySinhTon #SinhTon #PhimNgan #ThoiDoDa #haihuoc #vlogger
```

### Phần 2/11 — Ướm tay vào dấu tay thần lửa, sét đánh xuống hang

`02-dau-tay-than-lua.mp4` · 43s · cảnh 03.2, 03.3, 03.4 · đăng Thứ Bảy 14/11 – 19:00

**TikTok**

```text
Một mình trong hang Bàn Tay giữa đêm giông, Khang ướm tay vào dấu tay đỏ to nhất trên vách, thứ dân quanh đó bảo là tay thần lửa: “Ơ... vừa khít. Tay thần bằng tay tôi à?” Sét đánh ngay trên đầu, bàn tay dính chặt vào đá nóng dần như than. Anh tỉnh dậy bên bờ suối, gọi mãi mà Bin không thấy đâu.
Bạn có dám đặt tay vào vách đá đó không?

👉 Phần 3 ở trang cá nhân, Follow để xem tiếp!
#bayngaysinhton #sinhton #phimngan #bian #xuyenkhong
```

**YouTube Shorts — tiêu đề** (76/100 ký tự)

```text
Ướm tay vào dấu tay thần lửa, sét đánh ngay giữa hang | Bảy Ngày Sinh Tồn P2
```

**YouTube Shorts — mô tả**

```text
Một mình trong hang Bàn Tay giữa đêm giông, Khang ướm tay vào dấu tay đỏ to nhất trên vách, thứ dân quanh đó bảo là tay thần lửa: “Ơ... vừa khít. Tay thần bằng tay tôi à?” Sét đánh ngay trên đầu, bàn tay dính chặt vào đá nóng dần như than. Anh tỉnh dậy bên bờ suối, gọi mãi mà Bin không thấy đâu.

🎬 Full phim 24 phút có trên kênh YouTube, tìm “Bảy Ngày Sinh Tồn”
👉 Xem tiếp Phần 3: Tỉnh dậy giữa rừng, gặp tê giác đã tuyệt chủng

#Shorts #bayngaysinhton #sinhton #phimngan
```

**Facebook Reels**

```text
Một mình trong hang Bàn Tay giữa đêm giông, Khang ướm tay vào dấu tay đỏ to nhất trên vách, thứ dân quanh đó bảo là tay thần lửa: “Ơ... vừa khít. Tay thần bằng tay tôi à?” Sét đánh ngay trên đầu, bàn tay dính chặt vào đá nóng dần như than. Anh tỉnh dậy bên bờ suối, gọi mãi mà Bin không thấy đâu.

Bạn có dám đặt tay vào vách đá đó không? 👇
👉 Xem tiếp Phần 3: Tỉnh dậy giữa rừng, gặp tê giác đã tuyệt chủng
🎬 Full phim 24 phút có trên kênh YouTube, tìm “Bảy Ngày Sinh Tồn”

#BayNgaySinhTon #SinhTon #PhimNgan #ThoiDoDa #bian #xuyenkhong
```

### Phần 3/11 — Tỉnh dậy giữa rừng, gặp tê giác đã tuyệt chủng

`03-te-giac-tuyet-chung.mp4` · 43s · cảnh 04.2, 04.3, 04.4 · đăng Chủ Nhật 15/11 – 11:00

**TikTok**

```text
Dấu chân to bằng cái mâm, ba ngón tròn, mà ở Cúc Phương giờ chẳng còn con gì to thế. Sau bụi lau là một con tê giác thật: “Tê giác tuyệt chủng ở Việt Nam từ năm hai nghìn không trăm mười một! Bin không thuê nổi con này!” Không đường, không rác, không một tiếng xe máy, Khang bắt đầu nghĩ tia sét đã đưa anh về thời chưa có con đường nào.
Gặp tê giác cách 30 mét, bạn chạy hay nằm im?

👉 Phần 4 ở trang cá nhân, Follow để xem tiếp!
#bayngaysinhton #sinhton #phimngan #tegiac #xuyenkhong
```

**YouTube Shorts — tiêu đề** (77/100 ký tự)

```text
Tỉnh dậy giữa rừng, gặp tê giác đã tuyệt chủng từ 2011 | Bảy Ngày Sinh Tồn P3
```

**YouTube Shorts — mô tả**

```text
Dấu chân to bằng cái mâm, ba ngón tròn, mà ở Cúc Phương giờ chẳng còn con gì to thế. Sau bụi lau là một con tê giác thật: “Tê giác tuyệt chủng ở Việt Nam từ năm hai nghìn không trăm mười một! Bin không thuê nổi con này!” Không đường, không rác, không một tiếng xe máy, Khang bắt đầu nghĩ tia sét đã đưa anh về thời chưa có con đường nào.

🎬 Full phim 24 phút có trên kênh YouTube, tìm “Bảy Ngày Sinh Tồn”
👉 Xem tiếp Phần 4: Đuổi hổ cứu cậu bé tiền sử bằng tấm chăn 300 nghìn

#Shorts #bayngaysinhton #sinhton #phimngan
```

**Facebook Reels**

```text
Dấu chân to bằng cái mâm, ba ngón tròn, mà ở Cúc Phương giờ chẳng còn con gì to thế. Sau bụi lau là một con tê giác thật: “Tê giác tuyệt chủng ở Việt Nam từ năm hai nghìn không trăm mười một! Bin không thuê nổi con này!” Không đường, không rác, không một tiếng xe máy, Khang bắt đầu nghĩ tia sét đã đưa anh về thời chưa có con đường nào.

Gặp tê giác cách 30 mét, bạn chạy hay nằm im? 👇
👉 Xem tiếp Phần 4: Đuổi hổ cứu cậu bé tiền sử bằng tấm chăn 300 nghìn
🎬 Full phim 24 phút có trên kênh YouTube, tìm “Bảy Ngày Sinh Tồn”

#BayNgaySinhTon #SinhTon #PhimNgan #ThoiDoDa #tegiac #xuyenkhong
```

### Phần 4/11 — Đuổi hổ cứu cậu bé tiền sử bằng tấm chăn 300 nghìn

`04-duoi-ho-bang-chan-bac.mp4` · 56s · cảnh 06.1, 06.2, 06.3, 06.4 · đăng Chủ Nhật 15/11 – 19:00

**TikTok**

```text
Cậu bé Ốc kẹt trên tảng đá giữa suối, con hổ rình từ trưa. Khang giương tấm chăn bạc cứu hộ, thổi còi, hét thật to: “Làm mình to ra, làm ồn, không bao giờ quay lưng bỏ chạy!” Hổ lùi thật, Ốc tưởng anh có da bạc, còn chị của Ốc thì chĩa giáo đá vào người lạ.
Gặp hổ ngoài đời, bạn có nhớ mẹo này không?

👉 Phần 5 ở trang cá nhân, Follow để xem tiếp!
#bayngaysinhton #sinhton #phimngan #meosinhton #thoidoda
```

**YouTube Shorts — tiêu đề** (77/100 ký tự)

```text
Đuổi hổ cứu cậu bé tiền sử bằng tấm chăn bạc 300 nghìn | Bảy Ngày Sinh Tồn P4
```

**YouTube Shorts — mô tả**

```text
Cậu bé Ốc kẹt trên tảng đá giữa suối, con hổ rình từ trưa. Khang giương tấm chăn bạc cứu hộ, thổi còi, hét thật to: “Làm mình to ra, làm ồn, không bao giờ quay lưng bỏ chạy!” Hổ lùi thật, Ốc tưởng anh có da bạc, còn chị của Ốc thì chĩa giáo đá vào người lạ.

🎬 Full phim 24 phút có trên kênh YouTube, tìm “Bảy Ngày Sinh Tồn”
👉 Xem tiếp Phần 5: Người tiền sử lần đầu ăn mì tôm

#Shorts #bayngaysinhton #sinhton #phimngan
```

**Facebook Reels**

```text
Cậu bé Ốc kẹt trên tảng đá giữa suối, con hổ rình từ trưa. Khang giương tấm chăn bạc cứu hộ, thổi còi, hét thật to: “Làm mình to ra, làm ồn, không bao giờ quay lưng bỏ chạy!” Hổ lùi thật, Ốc tưởng anh có da bạc, còn chị của Ốc thì chĩa giáo đá vào người lạ.

Gặp hổ ngoài đời, bạn có nhớ mẹo này không? 👇
👉 Xem tiếp Phần 5: Người tiền sử lần đầu ăn mì tôm
🎬 Full phim 24 phút có trên kênh YouTube, tìm “Bảy Ngày Sinh Tồn”

#BayNgaySinhTon #SinhTon #PhimNgan #ThoiDoDa #meosinhton #thoidoda
```

### Phần 5/11 — Người tiền sử lần đầu ăn mì tôm

`05-mi-tom-sau-kho.mp4` · 45s · cảnh 08.2, 08.3, 08.4 · đăng Thứ Hai 16/11 – 11:00

**TikTok**

```text
Suối bảo Khang thôi đuổi cá, lật đá lên mà bắt ốc: “Ốc không biết chạy. Hợp với anh.” Anh xé gói mì tôm cuối cùng chia cho lũ trẻ, cậu bé Ốc nhai rộp rộp rồi chạy đi khoe cả hang: “Sâu khô ngon quá!” Bà trưởng hang chỉ nói một câu: “Người biết chia không phải ma.”
Nếu là người tiền sử, bạn sẽ gọi gói mì tôm là gì?

👉 Phần 6 ở trang cá nhân, Follow để xem tiếp!
#bayngaysinhton #sinhton #phimngan #haihuoc #mitom
```

**YouTube Shorts — tiêu đề** (75/100 ký tự)

```text
Người tiền sử lần đầu ăn mì tôm: “Sâu khô ngon quá!” | Bảy Ngày Sinh Tồn P5
```

**YouTube Shorts — mô tả**

```text
Suối bảo Khang thôi đuổi cá, lật đá lên mà bắt ốc: “Ốc không biết chạy. Hợp với anh.” Anh xé gói mì tôm cuối cùng chia cho lũ trẻ, cậu bé Ốc nhai rộp rộp rồi chạy đi khoe cả hang: “Sâu khô ngon quá!” Bà trưởng hang chỉ nói một câu: “Người biết chia không phải ma.”

🎬 Full phim 24 phút có trên kênh YouTube, tìm “Bảy Ngày Sinh Tồn”
👉 Xem tiếp Phần 6: Lửa của cả hang tắt, anh cưa tre ra lửa

#Shorts #bayngaysinhton #sinhton #phimngan
```

**Facebook Reels**

```text
Suối bảo Khang thôi đuổi cá, lật đá lên mà bắt ốc: “Ốc không biết chạy. Hợp với anh.” Anh xé gói mì tôm cuối cùng chia cho lũ trẻ, cậu bé Ốc nhai rộp rộp rồi chạy đi khoe cả hang: “Sâu khô ngon quá!” Bà trưởng hang chỉ nói một câu: “Người biết chia không phải ma.”

Nếu là người tiền sử, bạn sẽ gọi gói mì tôm là gì? 👇
👉 Xem tiếp Phần 6: Lửa của cả hang tắt, anh cưa tre ra lửa
🎬 Full phim 24 phút có trên kênh YouTube, tìm “Bảy Ngày Sinh Tồn”

#BayNgaySinhTon #SinhTon #PhimNgan #ThoiDoDa #haihuoc #mitom
```

### Phần 6/11 — Lửa của cả hang tắt, anh cưa tre ra lửa

`06-cua-tre-ra-lua.mp4` · 42s · cảnh 09.2, 09.3, 09.4 · đăng Thứ Hai 16/11 – 19:00

**TikTok**

```text
Đêm mưa, lửa của cả hang tắt ngấm, Gầm đổ tội cho người lạ mang xui tới. Khang nhớ lại cụ người Mường cưa tre ra lửa mà ngày trước anh tưởng là diễn, cùng Suối cưa đến khi mùn tre thành than rồi bùng cháy. Bà trưởng hang đặt tên anh là Người Làm Lửa, còn anh rưng rưng: “Hai mươi chín tuổi, đây là ngọn lửa đầu tiên của tôi.”
Bạn có biết cách cưa tre ra lửa không?

👉 Phần 7 ở trang cá nhân, Follow để xem tiếp!
#bayngaysinhton #sinhton #phimngan #meosinhton #lamlua
```

**YouTube Shorts — tiêu đề** (84/100 ký tự)

```text
Lửa của cả hang đã chết, vlogger cưa tre ra ngọn lửa đầu tiên | Bảy Ngày Sinh Tồn P6
```

**YouTube Shorts — mô tả**

```text
Đêm mưa, lửa của cả hang tắt ngấm, Gầm đổ tội cho người lạ mang xui tới. Khang nhớ lại cụ người Mường cưa tre ra lửa mà ngày trước anh tưởng là diễn, cùng Suối cưa đến khi mùn tre thành than rồi bùng cháy. Bà trưởng hang đặt tên anh là Người Làm Lửa, còn anh rưng rưng: “Hai mươi chín tuổi, đây là ngọn lửa đầu tiên của tôi.”

🎬 Full phim 24 phút có trên kênh YouTube, tìm “Bảy Ngày Sinh Tồn”
👉 Xem tiếp Phần 7: Cứu kẻ muốn đuổi mình khỏi hố sụt

#Shorts #bayngaysinhton #sinhton #phimngan
```

**Facebook Reels**

```text
Đêm mưa, lửa của cả hang tắt ngấm, Gầm đổ tội cho người lạ mang xui tới. Khang nhớ lại cụ người Mường cưa tre ra lửa mà ngày trước anh tưởng là diễn, cùng Suối cưa đến khi mùn tre thành than rồi bùng cháy. Bà trưởng hang đặt tên anh là Người Làm Lửa, còn anh rưng rưng: “Hai mươi chín tuổi, đây là ngọn lửa đầu tiên của tôi.”

Bạn có biết cách cưa tre ra lửa không? 👇
👉 Xem tiếp Phần 7: Cứu kẻ muốn đuổi mình khỏi hố sụt
🎬 Full phim 24 phút có trên kênh YouTube, tìm “Bảy Ngày Sinh Tồn”

#BayNgaySinhTon #SinhTon #PhimNgan #ThoiDoDa #meosinhton #lamlua
```

### Phần 7/11 — Cứu kẻ muốn đuổi mình khỏi hố sụt

`07-cuu-nguoi-duoi-ho-sut.mp4` · 44s · cảnh 14.2, 14.3, 14.4 · đăng Thứ Ba 17/11 – 11:00

**TikTok**

```text
Gầm, thợ săn ghét người lạ nhất hang, trẹo chân dưới đáy hố sụt. Khang nẹp chân, buộc dây leo kéo anh lên dù Gầm hỏi thẳng: “Sao cứu tôi? Tôi muốn anh rời khỏi hang.” Lên tới bờ, Gầm chìa tay: “Từ hôm nay, anh là anh em của tôi.”
Bạn có cứu người từng muốn đuổi mình đi không?

👉 Phần 8 ở trang cá nhân, Follow để xem tiếp!
#bayngaysinhton #sinhton #phimngan #anhem #cuunguoi
```

**YouTube Shorts — tiêu đề** (83/100 ký tự)

```text
Cứu kẻ muốn đuổi mình khỏi hố sụt, nhận lại một người anh em | Bảy Ngày Sinh Tồn P7
```

**YouTube Shorts — mô tả**

```text
Gầm, thợ săn ghét người lạ nhất hang, trẹo chân dưới đáy hố sụt. Khang nẹp chân, buộc dây leo kéo anh lên dù Gầm hỏi thẳng: “Sao cứu tôi? Tôi muốn anh rời khỏi hang.” Lên tới bờ, Gầm chìa tay: “Từ hôm nay, anh là anh em của tôi.”

🎬 Full phim 24 phút có trên kênh YouTube, tìm “Bảy Ngày Sinh Tồn”
👉 Xem tiếp Phần 8: Lũ đêm ập về, cậu bé quay lại cứu ngọn lửa

#Shorts #bayngaysinhton #sinhton #phimngan
```

**Facebook Reels**

```text
Gầm, thợ săn ghét người lạ nhất hang, trẹo chân dưới đáy hố sụt. Khang nẹp chân, buộc dây leo kéo anh lên dù Gầm hỏi thẳng: “Sao cứu tôi? Tôi muốn anh rời khỏi hang.” Lên tới bờ, Gầm chìa tay: “Từ hôm nay, anh là anh em của tôi.”

Bạn có cứu người từng muốn đuổi mình đi không? 👇
👉 Xem tiếp Phần 8: Lũ đêm ập về, cậu bé quay lại cứu ngọn lửa
🎬 Full phim 24 phút có trên kênh YouTube, tìm “Bảy Ngày Sinh Tồn”

#BayNgaySinhTon #SinhTon #PhimNgan #ThoiDoDa #anhem #cuunguoi
```

### Phần 8/11 — Lũ đêm ập về, cậu bé quay lại cứu ngọn lửa

`08-lu-dem-cuu-ong-lua.mp4` · 55s · cảnh 17.1, 17.2, 17.3, 17.4 · đăng Thứ Ba 17/11 – 19:00

**TikTok**

```text
Cả hang lên vách núi tránh lũ thì thiếu một người: cậu bé Ốc đã quay xuống hang dưới tìm ống lửa. “Lửa nhỏ ơi, lần này tao không để mày chết đâu!” Gầm ngồi tựa đá giữ dây, Khang lội xuống dòng nước bùn, cõng Ốc lên vai chạy về phía tảng đá lớn.
Ốc dũng cảm hay liều mạng?

👉 Phần 9 ở trang cá nhân, Follow để xem tiếp!
#bayngaysinhton #sinhton #phimngan #luquet #cuunguoi
```

**YouTube Shorts — tiêu đề** (84/100 ký tự)

```text
Lũ đêm ập về, cậu bé tiền sử quay lại cứu ống lửa của cả hang | Bảy Ngày Sinh Tồn P8
```

**YouTube Shorts — mô tả**

```text
Cả hang lên vách núi tránh lũ thì thiếu một người: cậu bé Ốc đã quay xuống hang dưới tìm ống lửa. “Lửa nhỏ ơi, lần này tao không để mày chết đâu!” Gầm ngồi tựa đá giữ dây, Khang lội xuống dòng nước bùn, cõng Ốc lên vai chạy về phía tảng đá lớn.

🎬 Full phim 24 phút có trên kênh YouTube, tìm “Bảy Ngày Sinh Tồn”
👉 Xem tiếp Phần 9: Bỏ máy quay giữa lũ để giữ dây cứu cậu bé

#Shorts #bayngaysinhton #sinhton #phimngan
```

**Facebook Reels**

```text
Cả hang lên vách núi tránh lũ thì thiếu một người: cậu bé Ốc đã quay xuống hang dưới tìm ống lửa. “Lửa nhỏ ơi, lần này tao không để mày chết đâu!” Gầm ngồi tựa đá giữ dây, Khang lội xuống dòng nước bùn, cõng Ốc lên vai chạy về phía tảng đá lớn.

Ốc dũng cảm hay liều mạng? 👇
👉 Xem tiếp Phần 9: Bỏ máy quay giữa lũ để giữ dây cứu cậu bé
🎬 Full phim 24 phút có trên kênh YouTube, tìm “Bảy Ngày Sinh Tồn”

#BayNgaySinhTon #SinhTon #PhimNgan #ThoiDoDa #luquet #cuunguoi
```

### Phần 9/11 — Bỏ máy quay giữa lũ để giữ dây cứu cậu bé

`09-ba-trieu-nguoi-xem.mp4` · 41s · cảnh 18.2, 18.3, 18.4 · đăng Thứ Tư 18/11 – 11:00

**TikTok**

```text
Dây buộc đá được ném xuống, Khang buộc Ốc bằng nút ghế cho cả hang kéo lên. Đúng lúc ấy đai máy quay bung, bảy ngày hình ảnh duy nhất nằm trong tay anh, và anh buông nó xuống dòng lũ: “Ba triệu người xem không đáng bằng một đứa trẻ ôm ống lửa.” Bà trưởng hang nói: “Lửa còn, người còn.”
Là bạn, bạn có buông máy quay không?

👉 Phần 10 ở trang cá nhân, Follow để xem tiếp!
#bayngaysinhton #sinhton #phimngan #xucdong #luquet
```

**YouTube Shorts — tiêu đề** (64/100 ký tự)

```text
Bỏ máy quay giữa lũ để giữ dây cứu cậu bé | Bảy Ngày Sinh Tồn P9
```

**YouTube Shorts — mô tả**

```text
Dây buộc đá được ném xuống, Khang buộc Ốc bằng nút ghế cho cả hang kéo lên. Đúng lúc ấy đai máy quay bung, bảy ngày hình ảnh duy nhất nằm trong tay anh, và anh buông nó xuống dòng lũ: “Ba triệu người xem không đáng bằng một đứa trẻ ôm ống lửa.” Bà trưởng hang nói: “Lửa còn, người còn.”

🎬 Full phim 24 phút có trên kênh YouTube, tìm “Bảy Ngày Sinh Tồn”
👉 Xem tiếp Phần 10: Dấu tay thần lửa trên vách hang hoá ra là của anh

#Shorts #bayngaysinhton #sinhton #phimngan
```

**Facebook Reels**

```text
Dây buộc đá được ném xuống, Khang buộc Ốc bằng nút ghế cho cả hang kéo lên. Đúng lúc ấy đai máy quay bung, bảy ngày hình ảnh duy nhất nằm trong tay anh, và anh buông nó xuống dòng lũ: “Ba triệu người xem không đáng bằng một đứa trẻ ôm ống lửa.” Bà trưởng hang nói: “Lửa còn, người còn.”

Là bạn, bạn có buông máy quay không? 👇
👉 Xem tiếp Phần 10: Dấu tay thần lửa trên vách hang hoá ra là của anh
🎬 Full phim 24 phút có trên kênh YouTube, tìm “Bảy Ngày Sinh Tồn”

#BayNgaySinhTon #SinhTon #PhimNgan #ThoiDoDa #xucdong #luquet
```

### Phần 10/11 — Dấu tay thần lửa trên vách hang hoá ra là của anh

`10-ban-tay-tren-vach.mp4` · 44s · cảnh 19.2, 19.3, 19.4 · đăng Thứ Tư 18/11 – 19:00

**TikTok**

```text
Sáng ngày thứ bảy, bà trưởng hang mở tục mới: ai cứu được hang thì để bàn tay lên vách, tay Khang đặt chính giữa. Anh lặng người: “Bàn tay to ở giữa... là tay tôi. Từ đầu đã vậy.” Suối đặt tay mình ngay cạnh: “Anh có đi, bàn tay anh vẫn ở lại.”
Bạn đoán ra bí mật bàn tay từ phần nào?

👉 Phần 11 ở trang cá nhân, Follow để xem tiếp!
#bayngaysinhton #sinhton #phimngan #plottwist #xuyenkhong
```

**YouTube Shorts — tiêu đề** (77/100 ký tự)

```text
Dấu tay thần lửa trên vách hang hoá ra là tay của anh | Bảy Ngày Sinh Tồn P10
```

**YouTube Shorts — mô tả**

```text
Sáng ngày thứ bảy, bà trưởng hang mở tục mới: ai cứu được hang thì để bàn tay lên vách, tay Khang đặt chính giữa. Anh lặng người: “Bàn tay to ở giữa... là tay tôi. Từ đầu đã vậy.” Suối đặt tay mình ngay cạnh: “Anh có đi, bàn tay anh vẫn ở lại.”

🎬 Full phim 24 phút có trên kênh YouTube, tìm “Bảy Ngày Sinh Tồn”
👉 Xem tiếp Phần 11: Bàn tay nhỏ bên cạnh là của cô gái tên Suối

#Shorts #bayngaysinhton #sinhton #phimngan
```

**Facebook Reels**

```text
Sáng ngày thứ bảy, bà trưởng hang mở tục mới: ai cứu được hang thì để bàn tay lên vách, tay Khang đặt chính giữa. Anh lặng người: “Bàn tay to ở giữa... là tay tôi. Từ đầu đã vậy.” Suối đặt tay mình ngay cạnh: “Anh có đi, bàn tay anh vẫn ở lại.”

Bạn đoán ra bí mật bàn tay từ phần nào? 👇
👉 Xem tiếp Phần 11: Bàn tay nhỏ bên cạnh là của cô gái tên Suối
🎬 Full phim 24 phút có trên kênh YouTube, tìm “Bảy Ngày Sinh Tồn”

#BayNgaySinhTon #SinhTon #PhimNgan #ThoiDoDa #plottwist #xuyenkhong
```

### Phần 11/11 — Bàn tay nhỏ bên cạnh là của cô gái tên Suối

`11-co-gai-ten-suoi.mp4` · 44s · cảnh 24.2, 24.3, 24.4 · đăng Thứ Năm 19/11 – 11:00

**TikTok**

```text
Trở lại hang Bàn Tay ngày nay, Khang chạm vào dấu tay nhỏ bên cạnh tay mình: “Còn bàn tay nhỏ hơn, ngay bên cạnh. Là của cô gái tên Suối.” Bin không tin, sấm lại rền, Khang chỉ cười: bên đó giờ họ có lửa rồi. Hơn một vạn năm trước, cậu bé Ốc đang dạy cả hang cưa tre ra lửa, bằng đúng câu cửa miệng của chú Lửa.
Cái kết này bạn chấm mấy điểm?

🎬 Xem trọn bộ 24 phút trên kênh YouTube.
#bayngaysinhton #sinhton #phimngan #ketphim #tinhyeu
```

**YouTube Shorts — tiêu đề** (67/100 ký tự)

```text
Bàn tay nhỏ bên cạnh là của cô gái tên Suối | Bảy Ngày Sinh Tồn P11
```

**YouTube Shorts — mô tả**

```text
Trở lại hang Bàn Tay ngày nay, Khang chạm vào dấu tay nhỏ bên cạnh tay mình: “Còn bàn tay nhỏ hơn, ngay bên cạnh. Là của cô gái tên Suối.” Bin không tin, sấm lại rền, Khang chỉ cười: bên đó giờ họ có lửa rồi. Hơn một vạn năm trước, cậu bé Ốc đang dạy cả hang cưa tre ra lửa, bằng đúng câu cửa miệng của chú Lửa.

🎬 Full phim 24 phút có trên kênh YouTube, tìm “Bảy Ngày Sinh Tồn”
🎬 Xem trọn bộ 24 phút trên kênh YouTube.

#Shorts #bayngaysinhton #sinhton #phimngan
```

**Facebook Reels**

```text
Trở lại hang Bàn Tay ngày nay, Khang chạm vào dấu tay nhỏ bên cạnh tay mình: “Còn bàn tay nhỏ hơn, ngay bên cạnh. Là của cô gái tên Suối.” Bin không tin, sấm lại rền, Khang chỉ cười: bên đó giờ họ có lửa rồi. Hơn một vạn năm trước, cậu bé Ốc đang dạy cả hang cưa tre ra lửa, bằng đúng câu cửa miệng của chú Lửa.

Cái kết này bạn chấm mấy điểm? 👇
🎬 Xem trọn bộ 24 phút trên kênh YouTube.
🎬 Full phim 24 phút có trên kênh YouTube, tìm “Bảy Ngày Sinh Tồn”

#BayNgaySinhTon #SinhTon #PhimNgan #ThoiDoDa #ketphim #tinhyeu
```
