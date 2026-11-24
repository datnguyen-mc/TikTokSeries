# Bức Tường Mỏng — Shorts cho TikTok, YouTube Shorts, Facebook Reels

Bản cắt **12 khoảnh khắc cuốn nhất** của phim 23 phút thành **12 phần dọc 9:16**, dài 37–60 giây, đăng nối tiếp theo thứ tự truyện. Mỗi phần mở bằng một câu hoặc một tình huống gây tò mò và kết bằng câu chốt hoặc cliffhanger. Cái kết (cuộc họp cư dân, chiếc nhẫn, ba tiếng gõ cuối cùng) để dành cho phim full.

- **Nguồn:** cắt thẳng từ bản dựng cuối `film/BUC-TUONG-MONG_ban-dung-v5_1080p.mp4`, nên đã có đủ màu, phần làm mờ chữ/logo, tiếng gõ đã sửa và nhạc phim.
- **Khung hình:** 1080×1920, 24 fps. Cảnh phim 16:9 để nguyên khung ở giữa, nền là chính cảnh đó làm mờ; không cắt mất nhân vật ở hai mép.
- **Chữ trên video:** nhãn đỏ rượu “BỨC TƯỜNG MỎNG • PHẦN N” và câu hook ở trên khung phim; phụ đề ở dưới khung phim (lời Ngân màu vàng, người khác màu trắng, tiếng vọng qua tường màu xanh nhạt). 2,5 giây cuối, hook đổi thành “CÒN TIẾP » PHẦN N+1” kèm hook của phần sau. Mọi chữ nằm ngoài vùng nút bấm và caption của TikTok/Reels.
- **Phụ đề:** lấy từ phụ đề `.srt` của bản v5 (đúng chữ kịch bản), câu dài tách đôi.
- **Âm thanh:** chuẩn hoá −14 LUFS (mức TikTok/YouTube/Facebook dùng).
- **Kết quả:** video nằm phẳng trong `shorts/` dạng `NN-<slug>.mp4`; lịch đăng và caption 3 nền tảng của mọi phần nằm trong `README.md` này.

Dựng lại (sau khi sửa plan):

```bash
python3 buc-tuong-mong/_tools/make_shorts_btm.py            # tất cả
python3 buc-tuong-mong/_tools/make_shorts_btm.py --only 3   # một phần
python3 buc-tuong-mong/_tools/make_shorts_btm.py --captions # chỉ ghi lại README
```

## Lịch đăng & danh sách phần

| Phần | Video | Nội dung | Cảnh | Thời lượng | Đăng lúc | Ưu tiên |
|---|---|---|---|---|---|---|
| 1 | [`01-dang-tiep-khach.mp4`](01-dang-tiep-khach.mp4) | Chồng gọi về bảo đang tiếp khách, tiếng cười lại ở ngay bên kia tường | 01-02–01-11 | 50s | Thứ Năm 26/11 – 11:00 | ⭐ |
| 2 | [`02-ba-tieng-go.mp4`](02-ba-tieng-go.mp4) | Con gõ tường 3 tiếng, chồng ở nhà bên giật bắn mình | 01-12–02-04 | 38s | Thứ Năm 26/11 – 19:00 |  |
| 3 | [`03-dep-cua-bo.mp4`](03-dep-cua-bo.mp4) | Con trai thấy dép của bố trước cửa nhà hàng xóm mới | 02-06–02-13 | 44s | Thứ Sáu 27/11 – 11:00 |  |
| 4 | [`04-chi-gai-no.mp4`](04-chi-gai-no.mp4) | Bồ của chồng sang chào, tưởng vợ là chị gái người yêu | 03-02–03-09 | 39s | Thứ Sáu 27/11 – 19:00 | ⭐ |
| 5 | [`05-vo-no-mat-nam-nao.mp4`](05-vo-no-mat-nam-nao.mp4) | Bồ kể “vợ anh ấy mất rồi” cho chính người vợ nghe | 04-01, 04-03–04-13 | 58s | Thứ Bảy 28/11 – 11:00 |  |
| 6 | [`06-mon-muop-dang.mp4`](06-mon-muop-dang.mp4) | Chồng về thấy vợ và bồ ngồi chung mâm, bị ép ăn hết bát mướp đắng | 05-02–05-13 | 57s | Thứ Bảy 28/11 – 19:00 | ⭐ |
| 7 | [`07-anh-khai-tu-em.mp4`](07-anh-khai-tu-em.mp4) | “Anh khai tử em từ năm nào?” | 06-02–06-13 | 52s | Chủ Nhật 29/11 – 11:00 |  |
| 8 | [`08-livestream-nghe-tieng-ma.mp4`](08-livestream-nghe-tieng-ma.mp4) | Bồ livestream khoe nhà, vợ bật loa truyện ma áp vào tường | 09-01–09-12 | 58s | Chủ Nhật 29/11 – 19:00 | ⭐ |
| 9 | [`09-doc-to-len.mp4`](09-doc-to-len.mp4) | Chồng lừa vợ ký “giấy vay vốn”, đọc to lên mới biết là giấy bán nhà | 11-01–11-11 | 46s | Thứ Hai 30/11 – 11:00 |  |
| 10 | [`10-me-chau-o-ben-kia-tuong.mp4`](10-me-chau-o-ben-kia-tuong.mp4) | “Cháu có mẹ. Mẹ cháu ở bên kia tường.” | 12-04–12-13 | 39s | Thứ Hai 30/11 – 19:00 | ⭐ |
| 11 | [`11-vo-va-bo-doi-mat.mp4`](11-vo-va-bo-doi-mat.mp4) | Vợ và bồ đối mặt: “Em có chắc mai kia anh ấy không khai tử em?” | 15-01–15-11 | 53s | Thứ Ba 01/12 – 11:00 |  |
| 12 | [`12-phong-cong-chung.mp4`](12-phong-cong-chung.mp4) | Chồng dẫn bồ đóng giả vợ ra công chứng bán nhà, vợ thật bước vào | 18-01–18-03, 18-05–18-14 | 60s | Thứ Ba 01/12 – 19:00 | ⭐ |

⭐ = phần có hook mạnh nhất, nên dồn tương tác hoặc chạy quảng cáo trước.

## Cách đăng

- **Thứ tự:** đăng phim full lên YouTube trước (đề xuất Thứ Tư 25/11, 19:00), rồi mới đăng shorts từ Thứ Năm 26/11. Có link phim full thì điền vào `full_movie_url` trong plan và chạy `--captions` để mọi mô tả có link.
- **Nhãn nội dung AI (bắt buộc):** nhân vật trong phim do AI tạo, trông như người thật. TikTok: bật “Nội dung do AI tạo” trong mục Cài đặt khác khi đăng. YouTube: mục “Nội dung đã qua chỉnh sửa / dùng AI” chọn **Có**. Facebook: bật nhãn “Thông tin về AI” khi đăng thước phim.
- **TikTok:** đăng theo thứ tự, gom vào Playlist “Bức Tường Mỏng”. Ghim 3 phần ⭐ lên đầu trang cá nhân (đề xuất Phần 1, 8, 10). Chọn ảnh bìa ở giây đầu (có hook).
- **YouTube Shorts:** dán tiêu đề + mô tả bên dưới; ở mục “Video liên quan” (Related video) chọn phim full để Shorts dẫn người xem về phim dài.
- **Facebook Reels:** dán caption; tắt phụ đề tự động vì phụ đề đã in sẵn trên video.
- **Giờ đăng:** mỗi ngày 2 phần (11:00 và 19:00), 3 nền tảng cùng giờ, từ Thứ Năm 26/11 đến Thứ Ba 01/12. Đổi ngày bắt đầu ở `schedule.start` rồi chạy `--captions`.

## Ghi chú bản short

- **Chọn cảnh:** 12 khoảnh khắc, khoảng 10 phút trên 23 phút phim. Phần 5 bỏ câu “Chị thương em trai thật đấy” (04-02); phần 12 bỏ cận cảnh người đeo khẩu trang im lặng (18-04) cho nhịp nhanh.
- **Nhân vật:** Ngân (vợ, kỹ thuật viên thu âm), Hưng (chồng), Diễm (cô hàng xóm mới, bồ của Hưng), Bin (con trai 8 tuổi), bà Lụa (trưởng ban quản lý tòa nhà).

## Caption từng phần (copy dán)

### Phần 1/12 — Chồng gọi về bảo đang tiếp khách, tiếng cười lại ở ngay bên kia tường

`01-dang-tiep-khach.mp4` · 50s · cảnh 01-02–01-11 · đăng Thứ Năm 26/11 – 11:00

**TikTok**

```text
Ngân thu âm sách nói cả ngày trong phòng thu tại nhà, chồng tin chị đeo tai nghe thì chẳng nghe thấy gì. Tối nay anh gọi về: “Em ngủ trước đi. Anh đang tiếp khách, khuya mới về.” Chị áp tai vào bức tường chung với căn hộ bên cạnh… và nghe thấy tiếng anh cười.
Là bạn, bạn có gọi điện vạch mặt ngay không?

👉 Phần 2 ở trang cá nhân, Follow để xem tiếp!
#buctuongmong #phimngan #ngoaitinh #tieutam #chinhthat
```

**YouTube Shorts — tiêu đề** (98/100 ký tự)

```text
Chồng gọi về bảo đang tiếp khách, vợ áp tai vào tường nghe thấy tiếng anh cười | Bức Tường Mỏng P1
```

**YouTube Shorts — mô tả**

```text
Ngân thu âm sách nói cả ngày trong phòng thu tại nhà, chồng tin chị đeo tai nghe thì chẳng nghe thấy gì. Tối nay anh gọi về: “Em ngủ trước đi. Anh đang tiếp khách, khuya mới về.” Chị áp tai vào bức tường chung với căn hộ bên cạnh… và nghe thấy tiếng anh cười.

🎬 Full phim 23 phút có trên kênh YouTube, tìm “Bức Tường Mỏng”
👉 Xem tiếp Phần 2: Con gõ tường 3 tiếng, chồng ở nhà bên giật bắn mình

#Shorts #buctuongmong #phimngan #phimgiadinh
```

**Facebook Reels**

```text
Ngân thu âm sách nói cả ngày trong phòng thu tại nhà, chồng tin chị đeo tai nghe thì chẳng nghe thấy gì. Tối nay anh gọi về: “Em ngủ trước đi. Anh đang tiếp khách, khuya mới về.” Chị áp tai vào bức tường chung với căn hộ bên cạnh… và nghe thấy tiếng anh cười.

Là bạn, bạn có gọi điện vạch mặt ngay không? 👇
👉 Xem tiếp Phần 2: Con gõ tường 3 tiếng, chồng ở nhà bên giật bắn mình
🎬 Full phim 23 phút có trên kênh YouTube, tìm “Bức Tường Mỏng”

#BucTuongMong #PhimNgan #NgoaiTinh #PhimGiaDinh #tieutam #chinhthat
```

### Phần 2/12 — Con gõ tường 3 tiếng, chồng ở nhà bên giật bắn mình

`02-ba-tieng-go.mp4` · 38s · cảnh 01-12–02-04 · đăng Thứ Năm 26/11 – 19:00

**TikTok**

```text
Bé Bin không ngủ được, sang phòng mẹ và dạy mẹ ám hiệu: “Ba tiếng là con thương mẹ.” Hai mẹ con gõ lên bức tường chung. Bên kia, ông bố giật bắn người, nói dối bồ là “nhà bên đóng đinh”. Sáng hôm sau anh mới về, áo còn thơm mùi hoa ly.
Mùi nước hoa trên áo chồng, bạn có tin là “của khách” không?

👉 Phần 3 ở trang cá nhân, Follow để xem tiếp!
#buctuongmong #phimngan #ngoaitinh #tinhmecon #phimgiadinh
```

**YouTube Shorts — tiêu đề** (83/100 ký tự)

```text
Con gõ tường 3 tiếng, chồng đang ở nhà bồ bên kia giật bắn mình | Bức Tường Mỏng P2
```

**YouTube Shorts — mô tả**

```text
Bé Bin không ngủ được, sang phòng mẹ và dạy mẹ ám hiệu: “Ba tiếng là con thương mẹ.” Hai mẹ con gõ lên bức tường chung. Bên kia, ông bố giật bắn người, nói dối bồ là “nhà bên đóng đinh”. Sáng hôm sau anh mới về, áo còn thơm mùi hoa ly.

🎬 Full phim 23 phút có trên kênh YouTube, tìm “Bức Tường Mỏng”
👉 Xem tiếp Phần 3: Con trai thấy dép của bố trước cửa nhà hàng xóm mới

#Shorts #buctuongmong #phimngan #phimgiadinh
```

**Facebook Reels**

```text
Bé Bin không ngủ được, sang phòng mẹ và dạy mẹ ám hiệu: “Ba tiếng là con thương mẹ.” Hai mẹ con gõ lên bức tường chung. Bên kia, ông bố giật bắn người, nói dối bồ là “nhà bên đóng đinh”. Sáng hôm sau anh mới về, áo còn thơm mùi hoa ly.

Mùi nước hoa trên áo chồng, bạn có tin là “của khách” không? 👇
👉 Xem tiếp Phần 3: Con trai thấy dép của bố trước cửa nhà hàng xóm mới
🎬 Full phim 23 phút có trên kênh YouTube, tìm “Bức Tường Mỏng”

#BucTuongMong #PhimNgan #NgoaiTinh #PhimGiaDinh #tinhmecon #phimgiadinh
```

### Phần 3/12 — Con trai thấy dép của bố trước cửa nhà hàng xóm mới

`03-dep-cua-bo.mp4` · 44s · cảnh 02-06–02-13 · đăng Thứ Sáu 27/11 – 11:00

**TikTok**

```text
Sáng đi học, Bin khựng lại trước cửa căn hộ mới bên cạnh: trên giá giày có đôi dép xanh vẽ ngôi sao vàng, đôi dép chính tay cậu vẽ cho bố. “Mẹ ơi! Dép của bố ở nhà bên này!” Ông bố vội bịa chuyện sang sửa bóng đèn, còn bà trưởng ban quản lý thì đang đi tìm người vừa dọn vào căn 1206.
Bạn nghĩ người vợ đã biết chuyện chưa?

👉 Phần 4 ở trang cá nhân, Follow để xem tiếp!
#buctuongmong #phimngan #ngoaitinh #tieutam #phimgiadinh
```

**YouTube Shorts — tiêu đề** (90/100 ký tự)

```text
Con trai thấy dép của bố trước cửa nhà hàng xóm mới, bố vội bịa chuyện | Bức Tường Mỏng P3
```

**YouTube Shorts — mô tả**

```text
Sáng đi học, Bin khựng lại trước cửa căn hộ mới bên cạnh: trên giá giày có đôi dép xanh vẽ ngôi sao vàng, đôi dép chính tay cậu vẽ cho bố. “Mẹ ơi! Dép của bố ở nhà bên này!” Ông bố vội bịa chuyện sang sửa bóng đèn, còn bà trưởng ban quản lý thì đang đi tìm người vừa dọn vào căn 1206.

🎬 Full phim 23 phút có trên kênh YouTube, tìm “Bức Tường Mỏng”
👉 Xem tiếp Phần 4: Bồ của chồng sang chào, tưởng vợ là chị gái người yêu

#Shorts #buctuongmong #phimngan #phimgiadinh
```

**Facebook Reels**

```text
Sáng đi học, Bin khựng lại trước cửa căn hộ mới bên cạnh: trên giá giày có đôi dép xanh vẽ ngôi sao vàng, đôi dép chính tay cậu vẽ cho bố. “Mẹ ơi! Dép của bố ở nhà bên này!” Ông bố vội bịa chuyện sang sửa bóng đèn, còn bà trưởng ban quản lý thì đang đi tìm người vừa dọn vào căn 1206.

Bạn nghĩ người vợ đã biết chuyện chưa? 👇
👉 Xem tiếp Phần 4: Bồ của chồng sang chào, tưởng vợ là chị gái người yêu
🎬 Full phim 23 phút có trên kênh YouTube, tìm “Bức Tường Mỏng”

#BucTuongMong #PhimNgan #NgoaiTinh #PhimGiaDinh #tieutam #phimgiadinh
```

### Phần 4/12 — Bồ của chồng sang chào, tưởng vợ là chị gái người yêu

`04-chi-gai-no.mp4` · 39s · cảnh 03-02–03-09 · đăng Thứ Sáu 27/11 – 19:00

**TikTok**

```text
Cô hàng xóm mới xách giỏ hoa quả sang chào: “Em là người yêu anh Hưng, em trai chị ạ. Anh ấy ngại, nên em tự sang chào chị.” Hưng chính là chồng của Ngân. Chị không khóc, không làm ầm, chỉ mỉm cười: “Vào nhà đi em. Chị là chị gái nó.”
Là bạn, bạn có diễn tiếp vai “chị gái” như Ngân không?

👉 Phần 5 ở trang cá nhân, Follow để xem tiếp!
#buctuongmong #phimngan #ngoaitinh #tieutam #chinhthat
```

**YouTube Shorts — tiêu đề** (81/100 ký tự)

```text
Bồ của chồng sang tận nhà chào, tưởng vợ là chị gái người yêu | Bức Tường Mỏng P4
```

**YouTube Shorts — mô tả**

```text
Cô hàng xóm mới xách giỏ hoa quả sang chào: “Em là người yêu anh Hưng, em trai chị ạ. Anh ấy ngại, nên em tự sang chào chị.” Hưng chính là chồng của Ngân. Chị không khóc, không làm ầm, chỉ mỉm cười: “Vào nhà đi em. Chị là chị gái nó.”

🎬 Full phim 23 phút có trên kênh YouTube, tìm “Bức Tường Mỏng”
👉 Xem tiếp Phần 5: Bồ kể “vợ anh ấy mất rồi” cho chính người vợ nghe

#Shorts #buctuongmong #phimngan #phimgiadinh
```

**Facebook Reels**

```text
Cô hàng xóm mới xách giỏ hoa quả sang chào: “Em là người yêu anh Hưng, em trai chị ạ. Anh ấy ngại, nên em tự sang chào chị.” Hưng chính là chồng của Ngân. Chị không khóc, không làm ầm, chỉ mỉm cười: “Vào nhà đi em. Chị là chị gái nó.”

Là bạn, bạn có diễn tiếp vai “chị gái” như Ngân không? 👇
👉 Xem tiếp Phần 5: Bồ kể “vợ anh ấy mất rồi” cho chính người vợ nghe
🎬 Full phim 23 phút có trên kênh YouTube, tìm “Bức Tường Mỏng”

#BucTuongMong #PhimNgan #NgoaiTinh #PhimGiaDinh #tieutam #chinhthat
```

### Phần 5/12 — Bồ kể “vợ anh ấy mất rồi” cho chính người vợ nghe

`05-vo-no-mat-nam-nao.mp4` · 58s · cảnh 04-01, 04-03–04-13 · đăng Thứ Bảy 28/11 – 11:00

**TikTok**

```text
Diễm vô tư kể “anh Hưng” một mình nuôi con từ hồi vợ mất. Ngân rót trà, hỏi như không: “Vợ nó mất năm nào nhỉ?” “Năm cháu lên ba ạ.” “Ừ. Chết lâu rồi.” Đúng lúc ấy Bin đi học về: “Mẹ ơi, con về rồi!”
Câu “Vì tin người” của Ngân làm bạn nghĩ gì?

👉 Phần 6 ở trang cá nhân, Follow để xem tiếp!
#buctuongmong #phimngan #ngoaitinh #tieutam #chinhthat
```

**YouTube Shorts — tiêu đề** (75/100 ký tự)

```text
Bồ kể vợ anh ấy mất rồi, người vợ ngồi rót trà nghe hết | Bức Tường Mỏng P5
```

**YouTube Shorts — mô tả**

```text
Diễm vô tư kể “anh Hưng” một mình nuôi con từ hồi vợ mất. Ngân rót trà, hỏi như không: “Vợ nó mất năm nào nhỉ?” “Năm cháu lên ba ạ.” “Ừ. Chết lâu rồi.” Đúng lúc ấy Bin đi học về: “Mẹ ơi, con về rồi!”

🎬 Full phim 23 phút có trên kênh YouTube, tìm “Bức Tường Mỏng”
👉 Xem tiếp Phần 6: Chồng về thấy vợ và bồ ngồi chung mâm, bị ép ăn hết bát mướp đắng

#Shorts #buctuongmong #phimngan #phimgiadinh
```

**Facebook Reels**

```text
Diễm vô tư kể “anh Hưng” một mình nuôi con từ hồi vợ mất. Ngân rót trà, hỏi như không: “Vợ nó mất năm nào nhỉ?” “Năm cháu lên ba ạ.” “Ừ. Chết lâu rồi.” Đúng lúc ấy Bin đi học về: “Mẹ ơi, con về rồi!”

Câu “Vì tin người” của Ngân làm bạn nghĩ gì? 👇
👉 Xem tiếp Phần 6: Chồng về thấy vợ và bồ ngồi chung mâm, bị ép ăn hết bát mướp đắng
🎬 Full phim 23 phút có trên kênh YouTube, tìm “Bức Tường Mỏng”

#BucTuongMong #PhimNgan #NgoaiTinh #PhimGiaDinh #tieutam #chinhthat
```

### Phần 6/12 — Chồng về thấy vợ và bồ ngồi chung mâm, bị ép ăn hết bát mướp đắng

`06-mon-muop-dang.mp4` · 57s · cảnh 05-02–05-13 · đăng Thứ Bảy 28/11 – 19:00

**TikTok**

```text
Hưng vừa bước vào nhà đã khựng lại: bồ đang ngồi ăn cơm với vợ. Ngân bình thản: “Em trai về rồi đấy à. Rửa tay rồi ăn cơm.” Món canh hôm nay là mướp đắng, món anh ghét nhất. “Ở nhà chị, nó ăn hết.”
Bát canh mướp đắng này, bạn chấm Ngân mấy điểm?

👉 Phần 7 ở trang cá nhân, Follow để xem tiếp!
#buctuongmong #phimngan #ngoaitinh #tieutam #chinhthat
```

**YouTube Shorts — tiêu đề** (90/100 ký tự)

```text
Chồng về thấy vợ và bồ ngồi chung mâm, bị ép ăn hết bát canh mướp đắng | Bức Tường Mỏng P6
```

**YouTube Shorts — mô tả**

```text
Hưng vừa bước vào nhà đã khựng lại: bồ đang ngồi ăn cơm với vợ. Ngân bình thản: “Em trai về rồi đấy à. Rửa tay rồi ăn cơm.” Món canh hôm nay là mướp đắng, món anh ghét nhất. “Ở nhà chị, nó ăn hết.”

🎬 Full phim 23 phút có trên kênh YouTube, tìm “Bức Tường Mỏng”
👉 Xem tiếp Phần 7: “Anh khai tử em từ năm nào?”

#Shorts #buctuongmong #phimngan #phimgiadinh
```

**Facebook Reels**

```text
Hưng vừa bước vào nhà đã khựng lại: bồ đang ngồi ăn cơm với vợ. Ngân bình thản: “Em trai về rồi đấy à. Rửa tay rồi ăn cơm.” Món canh hôm nay là mướp đắng, món anh ghét nhất. “Ở nhà chị, nó ăn hết.”

Bát canh mướp đắng này, bạn chấm Ngân mấy điểm? 👇
👉 Xem tiếp Phần 7: “Anh khai tử em từ năm nào?”
🎬 Full phim 23 phút có trên kênh YouTube, tìm “Bức Tường Mỏng”

#BucTuongMong #PhimNgan #NgoaiTinh #PhimGiaDinh #tieutam #chinhthat
```

### Phần 7/12 — “Anh khai tử em từ năm nào?”

`07-anh-khai-tu-em.mp4` · 52s · cảnh 06-02–06-13 · đăng Chủ Nhật 29/11 – 11:00

**TikTok**

```text
Khách về, Hưng lắp bắp xin giải thích. Ngân vẫn rửa bát, không quay đầu: “Anh khai tử em từ năm nào?” Đêm ấy anh lại sang nhà bên, hứa với bồ: “Tuần sau. Đứng tên em. Rồi anh đón thằng Bin sang ở với mình.” Anh quên mất bức tường giữa hai nhà mỏng đến mức nào.
Nghe đến đây, nếu là Ngân bạn sẽ làm gì?

👉 Phần 8 ở trang cá nhân, Follow để xem tiếp!
#buctuongmong #phimngan #ngoaitinh #chinhthat #phimgiadinh
```

**YouTube Shorts — tiêu đề** (95/100 ký tự)

```text
Anh khai tử em từ năm nào? Chồng hứa sang tên nhà cho bồ, vợ nghe qua tường | Bức Tường Mỏng P7
```

**YouTube Shorts — mô tả**

```text
Khách về, Hưng lắp bắp xin giải thích. Ngân vẫn rửa bát, không quay đầu: “Anh khai tử em từ năm nào?” Đêm ấy anh lại sang nhà bên, hứa với bồ: “Tuần sau. Đứng tên em. Rồi anh đón thằng Bin sang ở với mình.” Anh quên mất bức tường giữa hai nhà mỏng đến mức nào.

🎬 Full phim 23 phút có trên kênh YouTube, tìm “Bức Tường Mỏng”
👉 Xem tiếp Phần 8: Bồ livestream khoe nhà, vợ bật loa truyện ma áp vào tường

#Shorts #buctuongmong #phimngan #phimgiadinh
```

**Facebook Reels**

```text
Khách về, Hưng lắp bắp xin giải thích. Ngân vẫn rửa bát, không quay đầu: “Anh khai tử em từ năm nào?” Đêm ấy anh lại sang nhà bên, hứa với bồ: “Tuần sau. Đứng tên em. Rồi anh đón thằng Bin sang ở với mình.” Anh quên mất bức tường giữa hai nhà mỏng đến mức nào.

Nghe đến đây, nếu là Ngân bạn sẽ làm gì? 👇
👉 Xem tiếp Phần 8: Bồ livestream khoe nhà, vợ bật loa truyện ma áp vào tường
🎬 Full phim 23 phút có trên kênh YouTube, tìm “Bức Tường Mỏng”

#BucTuongMong #PhimNgan #NgoaiTinh #PhimGiaDinh #chinhthat #phimgiadinh
```

### Phần 8/12 — Bồ livestream khoe nhà, vợ bật loa truyện ma áp vào tường

`08-livestream-nghe-tieng-ma.mp4` · 58s · cảnh 09-01–09-12 · đăng Chủ Nhật 29/11 – 19:00

**TikTok**

```text
“Cả nhà ơi! Hôm nay em live ở nhà mới nhé! Anh yêu mua cho em đấy!” Bên kia tường, Ngân xoay chiếc loa kiểm âm về phía bức tường chung và vặn to. Giữa buổi live, một giọng đàn bà thì thào vọng ra từ trong tường: “Tôi chết rồi… sao vẫn nghe thấy anh cười?”
Màn trả đũa này của Ngân, bạn thấy đã chưa?

👉 Phần 9 ở trang cá nhân, Follow để xem tiếp!
#buctuongmong #phimngan #ngoaitinh #tieutam #livestream
```

**YouTube Shorts — tiêu đề** (87/100 ký tự)

```text
Bồ livestream khoe nhà được tặng, vợ bật loa truyện ma áp vào tường | Bức Tường Mỏng P8
```

**YouTube Shorts — mô tả**

```text
“Cả nhà ơi! Hôm nay em live ở nhà mới nhé! Anh yêu mua cho em đấy!” Bên kia tường, Ngân xoay chiếc loa kiểm âm về phía bức tường chung và vặn to. Giữa buổi live, một giọng đàn bà thì thào vọng ra từ trong tường: “Tôi chết rồi… sao vẫn nghe thấy anh cười?”

🎬 Full phim 23 phút có trên kênh YouTube, tìm “Bức Tường Mỏng”
👉 Xem tiếp Phần 9: Chồng lừa vợ ký “giấy vay vốn”, đọc to lên mới biết là giấy bán nhà

#Shorts #buctuongmong #phimngan #phimgiadinh
```

**Facebook Reels**

```text
“Cả nhà ơi! Hôm nay em live ở nhà mới nhé! Anh yêu mua cho em đấy!” Bên kia tường, Ngân xoay chiếc loa kiểm âm về phía bức tường chung và vặn to. Giữa buổi live, một giọng đàn bà thì thào vọng ra từ trong tường: “Tôi chết rồi… sao vẫn nghe thấy anh cười?”

Màn trả đũa này của Ngân, bạn thấy đã chưa? 👇
👉 Xem tiếp Phần 9: Chồng lừa vợ ký “giấy vay vốn”, đọc to lên mới biết là giấy bán nhà
🎬 Full phim 23 phút có trên kênh YouTube, tìm “Bức Tường Mỏng”

#BucTuongMong #PhimNgan #NgoaiTinh #PhimGiaDinh #tieutam #livestream
```

### Phần 9/12 — Chồng lừa vợ ký “giấy vay vốn”, đọc to lên mới biết là giấy bán nhà

`09-doc-to-len.mp4` · 46s · cảnh 11-01–11-11 · đăng Thứ Hai 30/11 – 11:00

**TikTok**

```text
Hưng đặt xấp giấy trước mặt vợ: “Em ký giúp anh mấy chữ. Giấy vay vốn mua xe cho công ty.” Ngân không cầm bút: “Anh đọc to lên cho em nghe.” “Bên A đồng ý ủy quyền cho bên B… toàn quyền định đoạt căn hộ…” Không lừa được, anh trở mặt: “Em không ký thì ly hôn. Thằng Bin theo anh.”
“Anh cứ thử.” Bạn có tin Ngân giữ được con không?

👉 Phần 10 ở trang cá nhân, Follow để xem tiếp!
#buctuongmong #phimngan #ngoaitinh #lyhon #phimgiadinh
```

**YouTube Shorts — tiêu đề** (85/100 ký tự)

```text
Chồng lừa vợ ký giấy vay vốn, đọc to lên mới biết là giấy bán nhà | Bức Tường Mỏng P9
```

**YouTube Shorts — mô tả**

```text
Hưng đặt xấp giấy trước mặt vợ: “Em ký giúp anh mấy chữ. Giấy vay vốn mua xe cho công ty.” Ngân không cầm bút: “Anh đọc to lên cho em nghe.” “Bên A đồng ý ủy quyền cho bên B… toàn quyền định đoạt căn hộ…” Không lừa được, anh trở mặt: “Em không ký thì ly hôn. Thằng Bin theo anh.”

🎬 Full phim 23 phút có trên kênh YouTube, tìm “Bức Tường Mỏng”
👉 Xem tiếp Phần 10: “Cháu có mẹ. Mẹ cháu ở bên kia tường.”

#Shorts #buctuongmong #phimngan #phimgiadinh
```

**Facebook Reels**

```text
Hưng đặt xấp giấy trước mặt vợ: “Em ký giúp anh mấy chữ. Giấy vay vốn mua xe cho công ty.” Ngân không cầm bút: “Anh đọc to lên cho em nghe.” “Bên A đồng ý ủy quyền cho bên B… toàn quyền định đoạt căn hộ…” Không lừa được, anh trở mặt: “Em không ký thì ly hôn. Thằng Bin theo anh.”

“Anh cứ thử.” Bạn có tin Ngân giữ được con không? 👇
👉 Xem tiếp Phần 10: “Cháu có mẹ. Mẹ cháu ở bên kia tường.”
🎬 Full phim 23 phút có trên kênh YouTube, tìm “Bức Tường Mỏng”

#BucTuongMong #PhimNgan #NgoaiTinh #PhimGiaDinh #lyhon #phimgiadinh
```

### Phần 10/12 — “Cháu có mẹ. Mẹ cháu ở bên kia tường.”

`10-me-chau-o-ben-kia-tuong.mp4` · 39s · cảnh 12-04–12-13 · đăng Thứ Hai 30/11 – 19:00

**TikTok**

```text
Bố đưa Bin sang chơi với “cô Diễm”. Bố vừa ra ban công nghe điện thoại, Bin lỡ tay làm đổ nước cam lên chiếc sofa trắng. Gương mặt ngọt ngào biến mất: “Đúng là không có mẹ dạy!” Bin ngồi thẳng lưng: “Cháu có mẹ. Mẹ cháu ở bên kia tường.” Rồi cậu bé gõ lên tường ba tiếng…
Ba tiếng gõ trả lời từ bên kia tường, bạn có rưng rưng không?

👉 Phần 11 ở trang cá nhân, Follow để xem tiếp!
#buctuongmong #phimngan #ngoaitinh #tinhmecon #tieutam
```

**YouTube Shorts — tiêu đề** (87/100 ký tự)

```text
Bị bồ của bố mắng không có mẹ dạy, bé trai gõ tường 3 tiếng gọi mẹ | Bức Tường Mỏng P10
```

**YouTube Shorts — mô tả**

```text
Bố đưa Bin sang chơi với “cô Diễm”. Bố vừa ra ban công nghe điện thoại, Bin lỡ tay làm đổ nước cam lên chiếc sofa trắng. Gương mặt ngọt ngào biến mất: “Đúng là không có mẹ dạy!” Bin ngồi thẳng lưng: “Cháu có mẹ. Mẹ cháu ở bên kia tường.” Rồi cậu bé gõ lên tường ba tiếng…

🎬 Full phim 23 phút có trên kênh YouTube, tìm “Bức Tường Mỏng”
👉 Xem tiếp Phần 11: Vợ và bồ đối mặt: “Em có chắc mai kia anh ấy không khai tử em?”

#Shorts #buctuongmong #phimngan #phimgiadinh
```

**Facebook Reels**

```text
Bố đưa Bin sang chơi với “cô Diễm”. Bố vừa ra ban công nghe điện thoại, Bin lỡ tay làm đổ nước cam lên chiếc sofa trắng. Gương mặt ngọt ngào biến mất: “Đúng là không có mẹ dạy!” Bin ngồi thẳng lưng: “Cháu có mẹ. Mẹ cháu ở bên kia tường.” Rồi cậu bé gõ lên tường ba tiếng…

Ba tiếng gõ trả lời từ bên kia tường, bạn có rưng rưng không? 👇
👉 Xem tiếp Phần 11: Vợ và bồ đối mặt: “Em có chắc mai kia anh ấy không khai tử em?”
🎬 Full phim 23 phút có trên kênh YouTube, tìm “Bức Tường Mỏng”

#BucTuongMong #PhimNgan #NgoaiTinh #PhimGiaDinh #tinhmecon #tieutam
```

### Phần 11/12 — Vợ và bồ đối mặt: “Em có chắc mai kia anh ấy không khai tử em?”

`11-vo-va-bo-doi-mat.mp4` · 53s · cảnh 15-01–15-11 · đăng Thứ Ba 01/12 – 11:00

**TikTok**

```text
Diễm đã biết sự thật, sang tận nhà đối chất: “Chị là vợ anh ấy.” “Ừ.” “Sổ hồng căn bên kia đứng tên em rồi.” Ngân không giận, chỉ nói một câu: “Anh ấy khai tử chị để có em. Em có chắc, mai kia anh ấy không khai tử em?”
Nếu là Diễm, bạn sẽ ở lại hay rời đi?

👉 Phần 12 ở trang cá nhân, Follow để xem tiếp!
#buctuongmong #phimngan #ngoaitinh #chinhthat #tieutam
```

**YouTube Shorts — tiêu đề** (96/100 ký tự)

```text
Vợ và bồ đối mặt: anh ấy khai tử chị để có em, mai kia có khai tử em không? | Bức Tường Mỏng P11
```

**YouTube Shorts — mô tả**

```text
Diễm đã biết sự thật, sang tận nhà đối chất: “Chị là vợ anh ấy.” “Ừ.” “Sổ hồng căn bên kia đứng tên em rồi.” Ngân không giận, chỉ nói một câu: “Anh ấy khai tử chị để có em. Em có chắc, mai kia anh ấy không khai tử em?”

🎬 Full phim 23 phút có trên kênh YouTube, tìm “Bức Tường Mỏng”
👉 Xem tiếp Phần 12: Chồng dẫn bồ đóng giả vợ ra công chứng bán nhà, vợ thật bước vào

#Shorts #buctuongmong #phimngan #phimgiadinh
```

**Facebook Reels**

```text
Diễm đã biết sự thật, sang tận nhà đối chất: “Chị là vợ anh ấy.” “Ừ.” “Sổ hồng căn bên kia đứng tên em rồi.” Ngân không giận, chỉ nói một câu: “Anh ấy khai tử chị để có em. Em có chắc, mai kia anh ấy không khai tử em?”

Nếu là Diễm, bạn sẽ ở lại hay rời đi? 👇
👉 Xem tiếp Phần 12: Chồng dẫn bồ đóng giả vợ ra công chứng bán nhà, vợ thật bước vào
🎬 Full phim 23 phút có trên kênh YouTube, tìm “Bức Tường Mỏng”

#BucTuongMong #PhimNgan #NgoaiTinh #PhimGiaDinh #chinhthat #tieutam
```

### Phần 12/12 — Chồng dẫn bồ đóng giả vợ ra công chứng bán nhà, vợ thật bước vào

`12-phong-cong-chung.mp4` · 60s · cảnh 18-01–18-03, 18-05–18-14 · đăng Thứ Ba 01/12 – 19:00

**TikTok**

```text
9 giờ sáng thứ Sáu, phòng công chứng. Hưng đẩy tập hồ sơ qua bàn: “Vợ tôi ký là xong.” Người phụ nữ đeo khẩu trang, đội mũ sụp ngồi im không nói. Cửa kính bật mở: “Chào em trai. Chị gái anh đến rồi đây.”
Cái kết cho người chồng này, bạn muốn là gì?

🎬 Cái kết ở phim full 23 phút trên kênh YouTube, tìm “Bức Tường Mỏng”.
#buctuongmong #phimngan #ngoaitinh #chinhthat #tieutam
```

**YouTube Shorts — tiêu đề** (85/100 ký tự)

```text
Chồng dẫn bồ đóng giả vợ ra công chứng bán nhà, vợ thật bước vào | Bức Tường Mỏng P12
```

**YouTube Shorts — mô tả**

```text
9 giờ sáng thứ Sáu, phòng công chứng. Hưng đẩy tập hồ sơ qua bàn: “Vợ tôi ký là xong.” Người phụ nữ đeo khẩu trang, đội mũ sụp ngồi im không nói. Cửa kính bật mở: “Chào em trai. Chị gái anh đến rồi đây.”

🎬 Full phim 23 phút có trên kênh YouTube, tìm “Bức Tường Mỏng”
🎬 Cái kết ở phim full 23 phút trên kênh YouTube, tìm “Bức Tường Mỏng”.

#Shorts #buctuongmong #phimngan #phimgiadinh
```

**Facebook Reels**

```text
9 giờ sáng thứ Sáu, phòng công chứng. Hưng đẩy tập hồ sơ qua bàn: “Vợ tôi ký là xong.” Người phụ nữ đeo khẩu trang, đội mũ sụp ngồi im không nói. Cửa kính bật mở: “Chào em trai. Chị gái anh đến rồi đây.”

Cái kết cho người chồng này, bạn muốn là gì? 👇
🎬 Cái kết ở phim full 23 phút trên kênh YouTube, tìm “Bức Tường Mỏng”.
🎬 Full phim 23 phút có trên kênh YouTube, tìm “Bức Tường Mỏng”

#BucTuongMong #PhimNgan #NgoaiTinh #PhimGiaDinh #chinhthat #tieutam
```
