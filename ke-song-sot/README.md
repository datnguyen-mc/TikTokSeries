# Kẻ Sống Sót — Bóng Ma 🌊🕯️

> **Trạng thái:** kịch bản 60 phút bản 2 (bám theo phim gốc), chưa dựng. Bản 1 (cựu đặc nhiệm, đảo tù) lưu ở [_v1_cuu-dac-vu/](_v1_cuu-dac-vu/).
> - **Kịch bản tổng 60 cảnh:** [KICH_BAN_60_PHUT.md](KICH_BAN_60_PHUT.md) · Prompt từng clip: `canh-01/` … `canh-60/` (sinh bằng [build_full_60_scenes.py](build_full_60_scenes.py)).
> - **Khóa nhân vật & prompt Flow:** [FLOW_PROMPTS.md](FLOW_PROMPTS.md) · **Hồ sơ tính cách & prompt ảnh:** [NHAN_VAT.md](NHAN_VAT.md) (tạo ảnh bằng [gen_character_refs.py](gen_character_refs.py)) · Đăng YouTube: [youtube.md](youtube.md).

---

## 0. Phim mẫu: "Kẻ Sinh Tồn Tội Lỗi" thật ra là phim gì

**Nguồn:** [youtube.com/watch?v=vrzn1w0tuk4](https://www.youtube.com/watch?v=vrzn1w0tuk4), kênh MIM2Movies, 84 phút 22 giây, 1,07 triệu lượt xem. Không có video nào tên "Tử Tù Tội Lỗi"; cách gọi đó trỏ về video này (thumbnail nhà tù trên đảo).

**Xác định phim gốc:** cùng kênh đăng **đúng file 5062 giây này** một lần nữa dưới tên *TỬ ĐỊA TỬ VONG* với cast thật **David S. Hogan, D'Angelo Midili, Angela DiMarco** và tóm tắt "sát thủ hợp đồng trả thù băng đảng sau khi người tình bị hại, bị truy đuổi, một cảnh sát trưởng thị trấn nhỏ phải giải câu đố". Ba diễn viên đó đóng chung đúng một phim: ***Narco Hitman*** (tên khác *Paralytic*, Hàn Quốc phát hành là *Still Alive*), phim độc lập Mỹ 2016 của Joey Johnson, thể loại mystery thriller, ~84 phút. Khung hình thật trong video là một người đàn ông lớn tuổi ria bạc trong nhà gỗ, không phải ngôi sao hành động. Vậy **logline "cựu đặc vụ bị bỏ rơi ở vùng chiến sự" và thumbnail đảo tù là bịa để câu view**; cốt truyện thật như sau.

**Cốt truyện thật của *Narco Hitman*** (ghép từ IMDb, Letterboxd, Amazon):
1. Carson "The Ghost" là sát thủ hợp đồng nổi tiếng. Băng ma túy Chutro thuê anh hạ một thị trưởng ở California.
2. Trong lúc chuẩn bị, anh gặp Clarissa; cô xin anh bỏ nghề đi cùng cô. Anh từ chối.
3. Vụ việc đổ bể, băng đảng trở mặt; anh biết tin Clarissa bị tra tấn và giết.
4. Anh trốn về một căn nhà gỗ hẻo lánh gần thị trấn nhỏ, tự cho mình **một tuần** để phơi bày sổ tiền của băng đảng; không xong thì anh sẽ kết liễu đời mình.
5. **Nữ cảnh sát trưởng** thị trấn thấy người lạ, điều tra và bị kéo vào; anh dùng cô và **thuốc gây liệt** do chính băng đảng sản xuất để thoát án tử của băng đảng (tên *Paralytic* và *Still Alive* từ đây).
6. Một **tổ chức bí ẩn, nguy hiểm hơn** kéo anh trở lại nghề giết thuê.
7. Kể bằng **lời dẫn ngôi thứ nhất**, hiện tại và quá khứ đan xen, nhiều cú lật, kết mở "để khán giả viết chương tiếp".

**Cái gì ăn khách, cái gì không:** người xem khen "cú lật thông minh", "đe dọa tàn bạo đáng sợ", "kết có hậu"; chê "nửa phim là người ta nói chuyện điện thoại", "nhân vật chính kể nhiều hơn làm", diễn xuất yếu. Kịch bản của mình giữ bộ xương (sát thủ, phản bội, người yêu chết, thị trấn nhỏ, nữ công an, thuốc liệt, hạn bảy ngày, tổ chức giấu mặt, kết mở) và sửa đúng chỗ bị chê: **mỗi cảnh một hành động**, lời dẫn tối đa hai câu, điện thoại chỉ ở ba cảnh.

**Những gì tôi đổi cho khác phim gốc:** bối cảnh Việt (thị trấn biển Hòn Sóng, thành phố đêm, tiệm hoa, tiệm lụa); mục tiêu là doanh nhân thay vì thị trưởng; trùm đường dây là một **người đàn bà** bán lụa; thuốc liệt dùng để **làm giả cái chết của chính sát thủ** chứ không chỉ để thoát; "tổ chức bí ẩn" cuối cùng là **chính mục tiêu bị thuê giết**; ngày thứ bảy anh "không chạy nữa" thay vì tự kết liễu.

---

## 1. Ý tưởng một câu

**Sơn "Bóng Ma"**, sát thủ hợp đồng của đường dây **Rắn Đen**, từ chối lời xin bỏ nghề của **Hạ**, cô chủ tiệm hoa anh yêu; hợp đồng cuối đổ bể, Rắn Đen phản bội và Hạ bị giết. Anh trốn về thị trấn biển **Hòn Sóng**, tự cho mình **bảy ngày** để phơi bày sổ tiền của Rắn Đen, trong khi **Đại úy Mây**, trưởng công an thị trấn, bắt đầu hỏi người lạ trong căn nhà gỗ ven rừng dương là ai. **"Bóng ma không chết. Bóng ma chỉ hết việc."**

## 2. Lấy gì, không lấy gì

**Lấy bộ xương** của *Narco Hitman* như mục 0. **Không lấy** tên nhân vật, thoại, tên băng đảng, thành phố, gương mặt diễn viên; không đóng gói lại phim người khác. Chất Việt: thị trấn biển bạc nắng, quán cà phê bờ kè, chợ cá, rừng dương, tiệm lụa, nhang, nước mắm.

## 3. Định dạng (đã chốt)

| Mục | Chốt |
|---|---|
| Tên | **Kẻ Sống Sót: Bóng Ma** (thư mục `ke-song-sot/`, slug `ke-song-sot`) |
| Phong cách | Người thật, neo-noir; hiện tại nắng trắng lạnh, quá khứ đêm ám vàng; lời dẫn ngôi thứ nhất |
| Độ dài | **60:00** = 60 cảnh × 6 clip × 10 giây = 360 clip |
| Nhân vật chính | **4 handle:** `@Son`, `@May`, `@Ha`, `@HaiNgoc`; Dũng "Đinh", Vũ Kiên, Phó Thành, Bác sĩ Linh, Ông Bảy mô tả bằng chữ |
| Vũ khí | Súng trong bao hoặc giơ lên, không bắn vào người; thuốc Tê (liệt, không chết); khóa tay, còng |
| Khung hình | 16:9 YouTube; crop 9:16 TikTok |

## 4. Thế giới (hư cấu)

- **Hòn Sóng:** thị trấn biển một con đường, cảng cá, quán cà phê bờ kè của Ông Bảy, chợ, cầu bê tông, hải đăng cũ trên vách.
- **Căn nhà gỗ** trong rừng dương trên đồi cát: giường xếp, bàn, radio, bảy vạch khắc trên khung cửa.
- **Thành phố đêm (quá khứ):** tòa kính, bãi xe ngầm, mái nhà, tiệm hoa dưới chân tòa nhà của Vũ Kiên.
- **Tiệm lụa** của Bà Hai Ngọc: bình phong cho Rắn Đen; **xưởng Tê** trong nhà máy nước mắm bỏ hoang ven sông.

## 5. Nhân vật

| Nhân vật | Vai | Nhận diện |
|---|---|---|
| **Sơn "Bóng Ma"** (`@Son`) | Sát thủ hợp đồng, người kể chuyện | 45 tuổi, tóc bạc hai bên, **sẹo trắng mảnh ngang sống mũi**, **dây đồng hồ quả quýt** ở thắt lưng; hiện tại áo khoác dã chiến ô liu; quá khứ vest đen không cà vạt, găng da |
| **Đại úy Mây** (`@May`) | Trưởng công an thị trấn | 38 tuổi, tóc ngắn có **lọn bạc phía trước**, áo kaki xắn tay, sổ tay túi ngực |
| **Hạ** (`@Ha`) | Cô chủ tiệm hoa, chỉ trong quá khứ | 32 tuổi, **khăn lụa xanh nhạt**, đầm lanh kem, tạp dề xanh |
| **Bà Hai Ngọc** (`@HaiNgoc`) | Trùm Rắn Đen, chủ tiệm lụa | 60 tuổi, búi tóc bạc, **vòng ngọc tay trái**, tẩu đen, áo bà ba lụa tím |
| **Dũng "Đinh"** | Tay sai số một | 35 tuổi, đầu đinh, **khuyên tai hình đinh**, áo ba lỗ đen |
| **Vũ Kiên** | Mục tiêu của hợp đồng, Người Môi Giới | 50 tuổi, vest trắng, cười rộng |
| **Phó Thành** | Phó của Mây | 26 tuổi, kính tròn, nhiệt tình |
| **Bác sĩ Linh** | Bác sĩ thị trấn | 55 tuổi, gầy, áo blouse sờn |
| **Ông Bảy** | Chủ quán cà phê bờ kè | 70 tuổi, ria bạc, nón lá |

## 6. Danh sách 60 cảnh

Xem mục lục trong [KICH_BAN_60_PHUT.md](KICH_BAN_60_PHUT.md). Ba hồi: **Hồi 1 (1–20) Bảy ngày**, **Hồi 2 (21–40) Thuốc Tê**, **Hồi 3 (41–60) Người Môi Giới**.

## 7. Làm phim noir với AI (Gemini Omni 10 giây)

- Hai bảng màu phải tách bạch: hiện tại trắng bạc, quá khứ ám vàng; clip "Quá khứ:" luôn mở bằng Ingredients với khóa đồ quá khứ.
- Lời dẫn đặt ở nhịp 1 hoặc 3, không trùng với thoại có khẩu hình.
- Mỗi cảnh ít nhất một hành động vật lý (đi, lục, khóa tay, chạy, châm thuốc, khắc vạch), tránh hai người ngồi nói chuyện quá 2 clip.
- Thuốc Tê mô tả bằng hình: lọ trong, ống tiêm, người ngã mềm rồi mắt vẫn mở.

## 8. Luật, an toàn và chính sách

- Không máu, không ai chết trên hình, không tra tấn trên hình, không tự sát, không bắn vào người, không dùng thuốc để phê. Cái chết trong quá khứ hiện qua ảnh, lời dẫn, vỏ đạn, băng niêm phong.
- Công an là phe tốt, không cơ quan có thật, không phù hiệu đọc được. Không tên hay gương mặt diễn viên thật.
- Nhãn AI trên TikTok và YouTube; caption ghi "phim hư cấu do AI tạo, không bắt chước".

## 9. Việc tiếp theo

1. Tạo project Flow, điền PROJECT_ID cho kênh `ke-song-sot` trên CMS; mở Chrome Extension.
2. `python3 gen_character_refs.py` để tạo ảnh 4 nhân vật chính và các REF phụ theo [NHAN_VAT.md](NHAN_VAT.md).
3. Dựng thử Cảnh 1 (hiện tại) và Cảnh 3 (quá khứ) để chốt hai bảng màu, rồi dựng 60 cảnh bằng runner `flowkit/runners/ke_song_sot.py`.
