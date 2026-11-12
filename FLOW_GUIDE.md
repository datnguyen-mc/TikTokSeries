# Hướng dẫn chung — Prompt Google Flow cho các series TikTok

**Áp dụng cho:** Mit & Đú 1970 · 365 Ngày Phèo Làm Nội Trợ · Nhà Tèo & Sún · Tây Du Ký 2026 · Mẹ và Bé · Biệt Đội Gara · Kẻ Sống Sót. Series 365 Ngày Việt Nam theo template riêng trong [MASTER_CONTEXT.md](365ngayvietnam/MASTER_CONTEXT.md); với series đó chỉ bảng **Độ dài tập** và mục **Kịch bản như người thật chia sẻ** dưới đây áp dụng chung.
> **⏱️ Từ 12/11/2026 (ưu tiên cao nhất):** các series TikTok (Mít & Đú, Phèo, Tây Du Ký, Mẹ và Bé, 365 Ngày Việt Nam) làm **mỗi tập 60 giây = 4 clip × 15 giây** trên **Gemini Omni 1.2 Flash**; `[FORMAT]` ghi `15-second clip`, thoại 38–54 âm tiết mỗi clip. Chuẩn chi tiết: `flowkit/docs/TIKTOK_PROMPT_SPEC.md`. Mọi chỗ ghi 10 giây / 3–6 clip bên dưới chỉ còn đúng cho các tập cũ đã render.
**Model:** Gemini Omni trong Google Flow, **10 giây mỗi clip** (cập nhật 24/10/2026; trước đó dùng Veo 3.1, 8 giây mỗi clip)
**Cấu trúc mỗi thư mục series — mỗi ngày đăng 1 tập, ghép từ các clip 10 giây; độ dài tập theo từng series (bảng "Độ dài tập" bên dưới):**
- `tap-{số}/`: thư mục của một tập (một ngày đăng). `README.md` là tổng quan: tóm tắt, ảnh cần đính kèm, kịch bản nhanh, ghi chú. `clip-1.md`, `clip-2.md`, … `clip-N.md`: **mỗi clip 10 giây là một file chỉ chứa đúng prompt** (copy cả file dán vào Flow), tương ứng một lần tạo trên Flow. `caption.md`: caption TikTok dán sẵn (tối đa 5 hashtag, vì từ giữa năm 2025 TikTok báo lỗi khi thêm hashtag thứ sáu), bình luận ghim tối đa 150 ký tự và các lưu ý trước khi đăng; README chỉ để link tới file này. Tập mới đánh số tiếp.
- `FLOW_PROMPTS.md`: khóa nhân vật, bối cảnh, phong cách và prompt tạo ảnh tham chiếu, dùng chung cho mọi tập.

| Series | Khóa nhân vật & ảnh tham chiếu | Các tập (1 tập/ngày) |
| ------ | ------------------------------ | --------------------- |
| Mit & Đú 1970 | [FLOW_PROMPTS.md](mit-va-du-1970/FLOW_PROMPTS.md) | [tap-1](mit-va-du-1970/tap-1/README.md) → [tap-31](mit-va-du-1970/tap-31/README.md) (từ 07/11/2026: mỗi tập một chuyện thôn quê 1970, 60 giây, không gượng ép tin 2026) |
| 365 Ngày Phèo Làm Nội Trợ | [FLOW_PROMPTS.md](pheo-va-no-meo/FLOW_PROMPTS.md) | [tap-1](pheo-va-no-meo/tap-1/README.md) → [tap-25](pheo-va-no-meo/tap-25/README.md) (tập 17–23: 60 giây dạy nấu; từ tập 24, 11/11/2026: "Có biến!", Phèo & Hường bàn drama của ngày, mỗi clip một tin ở một lĩnh vực; giọng Bắc từ 07/11) |
| Nhà Tèo & Sún | [FLOW_PROMPTS.md](teo-va-sun-cho/FLOW_PROMPTS.md) | [tap-1](teo-va-sun-cho/tap-1/README.md) → [tap-6](teo-va-sun-cho/tap-6/README.md) |
| Tây Du Ký 2026 | [FLOW_PROMPTS.md](tay-du-ky-2026/FLOW_PROMPTS.md) | [tap-8](tay-du-ky-2026/tap-8/README.md) → [tap-25](tay-du-ky-2026/tap-25/README.md) (tập 1–7 đã gỡ khỏi repo; từ 07/11/2026: 60 giây tổng kết hot & drama trong ngày, giọng Bắc) |
| 365 Ngày Việt Nam | [FLOW_PROMPTS.md](365ngayvietnam/FLOW_PROMPTS.md) | [tap1-ha-giang](365ngayvietnam/tap1-ha-giang/README.md) → [tap11-moc-chau](365ngayvietnam/tap11-moc-chau/README.md) |
| Mẹ và Bé | [FLOW_PROMPTS.md](me-va-be/FLOW_PROMPTS.md) | [tap-1](me-va-be/tap-1/README.md) → [tap-9](me-va-be/tap-9/README.md) |
| Biệt Đội Gara | [FLOW_PROMPTS.md](biet-doi-gara/FLOW_PROMPTS.md) | Phim 15 phút: [canh-01](biet-doi-gara/canh-01/README.md) → [canh-15](biet-doi-gara/canh-15/README.md), kịch bản tổng [KICH_BAN_PHIM.md](biet-doi-gara/KICH_BAN_PHIM.md) |
| Kẻ Sống Sót: Bóng Ma | [FLOW_PROMPTS.md](ke-song-sot/FLOW_PROMPTS.md) | Phim 60 phút: [canh-01](ke-song-sot/canh-01/README.md) → [canh-60](ke-song-sot/canh-60/README.md), kịch bản tổng [KICH_BAN_60_PHUT.md](ke-song-sot/KICH_BAN_60_PHUT.md), phân tích phim gốc trong [README.md](ke-song-sot/README.md), hồ sơ nhân vật [NHAN_VAT.md](ke-song-sot/NHAN_VAT.md) |
| Đường Đua Sinh Tử: 10 Giây Tự Do | [FLOW_PROMPTS.md](duong-dua-sinh-tu/FLOW_PROMPTS.md) | Phim 40 phút (4 Tập × 10 phút): [canh-01](duong-dua-sinh-tu/canh-01/README.md) → [canh-40](duong-dua-sinh-tu/canh-40/README.md), kịch bản tổng [KICH_BAN_40_PHUT.md](duong-dua-sinh-tu/KICH_BAN_40_PHUT.md), tổng quan [README.md](duong-dua-sinh-tu/README.md), hồ sơ nhân vật [NHAN_VAT.md](duong-dua-sinh-tu/NHAN_VAT.md) |

**Tập chủ đề 20/10:** Mit & Đú tap-8 · Phèo tap-3 · Tèo & Sún tap-2 · Tây Du Ký tap-4

**Tập xu hướng:** chủ đề lấy từ từ khóa Google Trends và TikTok, ghi lại trong [TRENDS.md](TRENDS.md). Tập xu hướng nên đăng ngay, không cần chờ đúng thứ tự.

**Độ dài tập TikTok (9:16) & Quy tắc Search Google bắt buộc** (áp dụng thống nhất cho tất cả kênh TikTok; các tập đã viết giữ nguyên file cũ):
- **Thời lượng mỗi tập TikTok (9:16): dao động từ 30 đến 60 giây (tối đa 60 giây = 3 đến 6 clip × 10s).** Tuyệt đối không làm vượt quá 60 giây (6 clip) cho một tập TikTok.
- **Bắt buộc Search Google khi cần thiết:** Trước khi viết kịch bản tập mới (công thức nấu ăn, định lượng gia vị, mẹo chăm bé, thông tin địa danh/giá vé/giờ vàng du lịch, mẹo đời sống, hoặc trend đang hot), bắt buộc phải tra cứu Google Search để lấy thông tin thật, chính xác 100% và ghi nguồn kiểm chứng vào `README.md` của tập.

| Series | Độ dài chuẩn | Số clip | Xương sống mỗi tập (30–60s) | Tra cứu Google bắt buộc khi viết |
| ------ | ------ | ----------- | ------------------ | ---------- |
| Tây Du Ký 2026 | **60s** từ 07/11/2026 (Tập 8–15: 30–60s) | **4 clip × 15s** từ Tập 24 (tập cũ 6 × 10s) | Bản tin hài tổng kết hot & drama trong ngày: hook 2 giây + tin #1 → tin #2 & bày mưu → phép lỗi nửa mùa → La Sát vào → đổ thừa & phát hiện → quạt Ba Tiêu hoặc câu hiền của Thầy, khung thumbnail đủ 5 nhân vật. Thoại ngắn tự nhiên giọng Bắc, không đọc bản tin | 2–4 tin hot trong 24–48 giờ (Google Trends VN, VnExpress, Dân trí, Tuổi Trẻ), ưu tiên tin hợp Tây Du Ký; ghi vào TRENDS.md |
| Mit & Đú 1970 | **60s** từ 07/11/2026 | **4 clip × 15s** từ Tập 30 (tập cũ 6 × 10s) | Một chuyện thôn quê Cái Mơn 1970 mỗi tập: hài mở màn → gag hình thể + Nở trêu → nốt trầm thiếu thốn → hy sinh thầm lặng → cao trào cảm động → kết ấm áp, câu chốt của Nở. Món ăn chỉ là chi tiết phụ; giữ giọng miền Tây | Phong tục, vật dụng, nghề, thời tiết, phương ngữ miền Tây xưa (1970); không gượng ép tin 2026 |
| 365 Ngày Phèo Làm Nội Trợ | **60s** từ 06/11/2026 | **4 clip × 15s** từ Tập 24 (tập cũ 6 × 10s) | Từ Tập 24 (11/11/2026) "Có biến!": Hường mở "Em ơi, có biến!" → mỗi clip một tin của ngày ở một lĩnh vực khác nhau, một câu tin + một câu đùa, Phèo xin tăng lương còn Hường lảng → clip 6 tin gắn với ngày đăng + quà chơi chữ theo nghĩa đen, đứng hình. Góc bàn ăn, không nấu. Giọng Bắc thanh thoát (Tập 17–23: dạy nấu 6 phần) | Tin 24–48 giờ (Google Trends VN, VnExpress, Dân trí, Tuổi Trẻ, Thanh Niên), mở bài gốc kiểm chứng; không người thật, thương hiệu, tội phạm, thiên tai, chính trị, trẻ em, cờ bạc; không trùng tin Tây Du Ký cùng ngày; ghi vào TRENDS.md |
| Nhà Tèo & Sún | **30–60s** (tối đa 60s) | **3–6 clip** | Chuyện trong nhà → Tèo vụng về hoặc trục trặc → mẹo đời sống (sản phẩm xuất hiện tự nhiên) → kết yêu thương | Mẹo vặt gia đình, cách dùng sản phẩm an toàn trên nhãn |
| 365 Ngày Việt Nam | **60s = 4 clip × 15s** cho tập mới từ 12/11/2026 (Tập 10–12: 30s; Tập 1–9: 60–90s) | **4 clip × 15s** (tập cũ 3 × 10s) | Hook flycam vào điểm hot → trải nghiệm / đặc sản → chốt tình cảm & nhử chặng sau. Vy và Joi nói chuyện với nhau như người thật, số liệu để ở caption | ⚡ Check hot (Google Trends VN, báo 2–4 tuần gần nhất, mùa hoa/mây/lễ hội) + địa danh, cung đường, giờ vàng, đặc sản & văn hóa địa phương; ghi vào TRENDS.md |
| Mẹ và Bé | **60s = 4 clip × 15s** cho tập mới từ 12/11/2026 (Tập 8–11: 30s; Tập 1–7: 40–60s) | **4 clip × 15s** (tập cũ 3 × 10s) | Hook 2 giây bằng khoảnh khắc của bé → đồ cho bé dùng thật, mẹo đi bằng hình → cao trào cảm xúc, khung cuối lặp khung đầu. Thoại tự nhiên như mẹ nói với con, không đọc mẹo | Cột mốc phát triển & an toàn trẻ nhỏ theo tuần tuổi (WHO, CDC, AAP, Bộ Y tế); **từ Tập 8** check đồ và nội dung hot (bảng TikTok Shop Mẹ & Bé, Google Trends VN), ghi vào TRENDS.md |
| Biệt Đội Gara | Phim 16:9 YouTube, cắt cảnh 60s cho TikTok | 6 clip / cảnh (60s) | Mỗi cảnh: hook 2 giây → hành động hoặc cảm xúc chính → cú lật hoặc câu móc | Cơ khí ô tô, kỹ thuật độ xe & cứu hộ thực tế |
| Kẻ Sống Sót: Bóng Ma | Phim 60:00 đăng YouTube (16:9), chia 60 cảnh × 60s | 360 (6 clip / cảnh) | Mỗi cảnh: hook 2 giây → một mối đe dọa, manh mối hoặc mảnh quá khứ → cú lật hoặc câu móc | Nghiệp vụ điều tra, pháp y, bối cảnh thị trấn biển |
| Đường Đua Sinh Tử: 10 Giây Tự Do | Phim 40:00 đăng YouTube (16:9), chia 40 cảnh × 60s | 240 (6 clip / cảnh) | Mỗi cảnh: hook 2 giây → đua xe, điều tra hoặc xung đột huynh đệ → cú lật hoặc câu móc | Thông số kỹ thuật xe đua (Supra, Charger, Eclipse, RX-7), thuật ngữ cơ khí |

**Kịch bản "như người thật chia sẻ" & Tra cứu Google thực tế** (mọi series TikTok 30–60s):
- **Thời lượng gọn 30–60 giây (3–6 clip × 10s):** Chọn đúng điểm đắt giá nhất của câu chuyện, món ăn hoặc điểm đến. Không kéo dài lê thê quá 60 giây.
- **Bắt buộc Search Google khi cần thiết:** Mọi tên món, định lượng, giờ giấc, nơi chốn, giá cả, giờ mở cửa, luật lệ, công thức nấu ăn, mẹo chăm trẻ, mẹo sức khỏe phải được tra cứu Google trước khi viết và ghi nguồn trong `README.md` (ưu tiên Bộ Y tế, WHO, CDC, hướng dẫn chính thức).
- **Mỗi clip có một điều mới** cho người xem: một chi tiết đời thật, một mẹo, một bước làm, một con số hoặc một nhịp cảm xúc. Không có clip chỉ để kéo dài.
- **Nói như người thật:** câu ngắn, giọng miền Nam tự nhiên, có cảm thán, có kể chuyện ngôi thứ nhất; không đọc như thuyết minh, không giảng đạo lý.
- **Giữ tốc độ thoại tự nhiên:** mỗi clip tối đa khoảng 30–31 âm tiết thoại (không quá 4,5 âm tiết/giây).
- **Giữ người xem:** khoảng 10–15 giây lại có một điểm mới (câu hỏi, bất ngờ, mẹo, tình huống); clip cuối luôn có điểm chốt và khung thumbnail.

---

## 1. Dán prompt vào Flow từng bước

Gemini Omni tạo **tối đa 10 giây mỗi lần** (Veo 3.1 chỉ được 8 giây), nên tập TikTok dài bao nhiêu thì ghép bấy nhiêu clip 10 giây: **dao động từ 30 đến 60 giây = 3 đến 6 clip × 10s (tối đa 60 giây)**. **Mỗi file `clip-{số}.md` chỉ chứa đúng prompt:** mở file, bấm Cmd+A rồi Cmd+C, dán vào ô prompt của Flow, không sửa gì.

| Clip | Thời gian | Chế độ trong Flow (9:16 TikTok) | Chế độ trong Flow (16:9 YouTube: Kẻ Sống Sót, Đường Đua Sinh Tử, Biệt Đội Gara) |
| ---- | --------- | ----------------- | ------------------------------------------------------------------------------- |
| **Clip 1** | 00:00–00:10 | **Video → Gemini Omni → Ingredients** (Đính ảnh nhân vật và sản phẩm) | **Video → Gemini Omni → Ingredients** (hoặc Text-to-Video nếu cảnh không có nhân vật chính) |
| **Clip 2 trở đi** | mỗi clip thêm 10 giây | **Video → Gemini Omni → Frames**, **luôn** lấy khung cuối clip trước làm start frame, kể cả clip mở bằng `[FORMAT]` hoặc cắt cảnh | **Video → Gemini Omni → Ingredients** (Luôn mở bằng `[FORMAT]`, đính kèm nhân vật có mặt, **tuyệt đối KHÔNG chèn frame cuối** của clip trước vì phim 16:9 YouTube chuyển góc máy liên tục) |

> **Quy tắc bắt buộc cho phim ngắn 9:16 TikTok (`mit-va-du-1970`, `pheo-va-no-meo`, `me-va-be`, `tay-du-ky-2026`, `365ngayvietnam`):** từ Clip 2 trở đi, clip nào cũng mở từ khung cuối của clip trước (`start_image_media_id` / Frames). Runner tự cắt khung cuối bằng ffmpeg, nạp vào slot [Bắt đầu] của clip kế tiếp và giữ khung đó cả khi chạy lại; chạy lẻ một clip thì runner lấy khung cuối từ video clip trước đã có trên máy. Chỉ khi clip trước chưa có video nào, clip đó mới tạm dùng Ingredients.

> **Quy tắc bắt buộc cho Phim 16:9 YouTube (`ke-song-sot`, `duong-dua-sinh-tu`, `biet-doi-gara`):**
> - Phim điện ảnh 16:9 trên YouTube chuyển cảnh và đổi góc máy liên tục giữa các cú máy (Wide, Medium, Close-up, Tracking, Insert/B-Roll). Vì vậy **tuyệt đối KHÔNG trích xuất và nạp frame cuối (`start_image_media_id` / Frames) vào clip kế tiếp**.
> - Mọi clip từ Clip 1 đến Clip 6 đều mở đầu bằng `[FORMAT]` và gọi trực tiếp **Ingredients Reference-to-Video** (`/api/flow/generate-video-omni` với danh sách `reference_media_ids` của đúng các nhân vật có mặt trong khung hình) hoặc **Text-to-Video** (`/api/flow/generate-video-omni-text` cho cảnh cận đạo cụ/phương tiện/toàn cảnh không có nhân vật chính).
> - **Chống nháy ảnh thẻ nhân vật ở đầu/cuối clip (Studio Reference Card Guard):** Mọi prompt phải có chỉ dẫn rõ trong `[FORMAT]`, `[CHARACTERS]`, `[FINAL COMPOSITION AT 10.0s]` và `[AVOID]`: chỉ dùng ảnh tham chiếu để khóa khuôn mặt/trang phục bên trong bối cảnh sống của phim; tuyệt đối không hiển thị hoặc cắt sang ảnh thẻ nhân vật nền xám studio ở giây đầu hoặc giây cuối của clip (`never flash or cut to an attached character reference portrait or plain grey studio backdrop at the start or end of the clip`).
> - **Kiến trúc Global Film Bible thống nhất (`film_bible.py`):** Mọi phim dài đều quản lý tập trung `CHARACTER_LOCK`, `VEHICLE_LOCK`, `ENVIRONMENT_LOCK`, `OBJECT_LOCK`, `PHYSICS_RULES`, `CINEMATIC_STYLE`, `AUDIO_STYLE`, `START_STATE` / `END_STATE`, `Mouth map` (chỉ định chính xác ai mở miệng ở khung giây nào, người nghe khép miệng) và khối `[AVOID]` sạch (không chứa từ khóa nhạy cảm gây chặn chính sách).
> - **Quy tắc An toàn Cảnh Hành động & Võ thuật (Simulated Stunt Choreography Rule):** Mọi cảnh đối đầu tay đôi, võ thuật, va chạm hoặc rượt đuổi tốc độ cao phải được mô tả dưới góc độ **biên đạo cascadeur chuyên nghiệp** để không vi phạm chính sách nội dung của Google Flow:
>   `Cinematic Vietnamese martial arts action sequence, 10 seconds, photorealistic live-action, 16:9, 24fps. Two professional stunt performers execute a tightly choreographed martial arts confrontation. Fast defensive movements, precise dodges, controlled kicks, dramatic camera tracking, dynamic footwork and realistic physical reactions. One performer loses balance and falls safely onto padded flooring outside the camera's view. Intense action-film atmosphere, realistic lighting, handheld cinematography, fast-paced editing style, authentic Vietnamese action cinema. No blood, no graphic injuries, no gore. All movements are simulated stunt choreography.`

Nếu giao diện Flow đặt tên chế độ khác, chọn chế độ tạo video từ ảnh tham chiếu cho Clip 1 và chế độ khung đầu (first frame) cho Clip 2 trở đi.

**Nhảy thời gian trong tập** (ướp, kho, chiều hôm đó, sáng hôm sau), chọn một trong ba cách:
1. **Trong cùng clip:** tiếng hẹn giờ ting, mở nắp thấy món đã xong; dùng khi chỉ chờ tối đa khoảng 30 phút.
2. **Đồ làm sẵn:** nhân vật lấy tô đã ướp sẵn trong tủ lạnh và nói ra, ví dụ: Tô này Phèo ướp từ sáng!
3. **Cắt cảnh:** mở clip mới bằng [FORMAT] và FULL LOCK, không dùng câu Continue…, nhưng vẫn chạy **Frames** với khung cuối clip trước làm start frame; dòng đầu [SHOT LIST] ghi rõ, ví dụ `Hard cut: thirty minutes later, same kitchen, same outfits, same lighting.` README ghi rõ clip nào là cắt cảnh.

**Chuẩn bị một lần cho mỗi series:**
- Tạo nhân vật trên Flow từ ảnh tham chiếu và đặt **đúng tên** như bảng dưới. Dòng khai báo nhân vật trong prompt đã ghi sẵn dạng `@Pheo = PHÈO: …`: Flow gọi đúng nhân vật đã lưu, còn model hiểu PHÈO trong cả prompt chính là `@Pheo`.
- Tải ảnh sản phẩm (`SP_…`) và ảnh nhân vật phụ (`REF_…`) vào project, **giữ đúng tên file** để gọi được bằng `@`.
- **Giọng (`@Voice`):** Gemini Omni có `@Voice`. Nếu Flow cho gắn giọng vào nhân vật đã lưu, gắn cho mỗi nhân vật một giọng cố định ngay từ đầu và giữ nguyên ở mọi tập. Prompt vẫn giữ câu mô tả giọng trong khóa nhân vật.

| Series | Tên nhân vật trên Flow | Tên trong prompt |
| ------ | ---------------------- | ---------------- |
| Mit & Đú 1970 | `@Mit` · `@Đú` · `@Nở` | Mit · Đú · Nở |
| 365 Ngày Phèo Làm Nội Trợ | `@Pheo` · `@No` | PHÈO · BÀ CHỦ HƯỜNG |
| Nhà Tèo & Sún | `@TeoTeo` (chó đực) · `@SunSun` (chó cái) | TeoTeo · SunSun |
| Tây Du Ký 2026 | `@Thay` · `@DaiCa` · `@HeoLuoi` · `@UtKho` | THẦY · ĐẠI CA · HEO LƯỜI · ÚT KHỜ |
| Mẹ và Bé | `@Ngoc` · `@Gao` · `@Bong` | NGỌC · GẠO · BÔNG |
| Biệt Đội Gara | `@Thang` · `@Lan` · `@Hai` · `@Khoi` · `@Minh` | THẮNG · LAN · HẢI · KHÔI · MINH |
| Kẻ Sống Sót: Bóng Ma | `@Son` · `@May` · `@Ha` · `@HaiNgoc` · `@Dũng` · `@Vũ Kiên` · `@Phó Thành` · `@Bác sĩ Linh` · `@Ông Bảy`; người dẫn chuyện dùng `@Voice` tên NguoiKe nếu Flow cho tạo | Sơn · Mây · Hạ · Bà Hai · Dũng · Kiên · Thành · Bác sĩ Linh · Ông Bảy |
| Đường Đua Sinh Tử: 10 Giây Tự Do | `@Tom` · `@Micdo` · `@Ami` · `@Cevin` · `@Cina` · `@Seja` · `@Onle` · `@NyTran` · `@Cela` · `@Nese` · `@Kinan` · `@Verni` | Tom · Micdo · Ami · Cevin · Cina · Seja · Onle · Ny Trần · Cela · Trung sĩ Nese · Đặc vụ Kinan · Verni |

Mit & Đú và Tèo & Sún dùng luôn tên Flow trong cả prompt. Phèo, Tây Du Ký, Mẹ và Bé và Biệt Đội Gara giữ tên gốc trong phần còn lại của prompt: "No" là từ tiếng Anh, viết "No walks in…" model dễ hiểu nhầm. Nếu nhân vật trên Flow được tạo từ ảnh bộ đồ thường ngày, ở các tập mặc đồ khác (Mit & Đú tập 3, 4 và cảnh mơ tập 10, Tèo & Sún tập 2, Tây Du Ký tập 3) thì đính thêm ảnh bộ đồ đó.

**Clip 1**
1. Bấm tên model ở ô prompt → **Video** → **Gemini Omni** → **Ingredients**. Mặc định Flow để model ảnh Nano Banana Pro: quên đổi sẽ ra ảnh, không ra video.
2. Thiết lập: dọc 9:16, độ dài **10s**, số kết quả 2 (nếu có).
3. Đính ảnh: kéo thả vào ô prompt hoặc bấm **Add** bên dưới ô prompt. **Omni nhận nhiều ảnh tham chiếu hơn Veo** (Veo chỉ nhận 3), nên có thể đính đủ các nhân vật có mặt trong clip. Nếu Flow vẫn báo giới hạn, ưu tiên nhân vật có mặt lâu nhất trong clip, rồi đến sản phẩm.
4. Dán prompt `clip-1.md`.
5. Kiểm tra dòng khai báo nhân vật: sau khi dán, `@Mit`, `@TeoTeo`… phải hiện thành thẻ nhân vật của Flow. Nếu vẫn là chữ thường, xóa `@Tên` rồi gõ lại `@` và chọn nhân vật trong danh sách. Nếu Omni không nhận thẻ nhân vật, đính ảnh `REF_…` như cũ. Với ảnh sản phẩm, gõ `@` chọn ảnh rồi ghi vai trò, ví dụ `@SP_TAP is the notebook.`
6. Bấm Generate, chọn bản đẹp nhất.

**Clip 2 trở đi**
1. Mở clip vừa chọn, dừng ở khung cuối, bấm **Save frame**.
2. Bấm tên model → **Video** → **Gemini Omni** → **Frames**, kéo ảnh vừa lưu vào **+ Add start frame**, để độ dài 10s.
3. Dán prompt `clip-2.md`. Hai dòng đầu prompt đã viết sẵn: "Continue the scene seamlessly from the final frame of the previous clip…".
4. Bấm Generate. Các clip sau làm giống vậy, mỗi clip lấy khung cuối của clip ngay trước.

**Dùng Extend thay cho Frames:** Gemini Omni 1.1 cho nối dài video đã tạo, mỗi lần thêm tối đa 10 giây, tổng tối đa 40 giây, và đọc lại cả đoạn trước nên nhân vật và giọng giữ đều hơn. Nếu Flow của bạn đã có nút **Extend** cho Omni (một số tài khoản chưa có): tạo Clip 1, bấm **Extend**, dán nguyên prompt `clip-2.md`, rồi Extend tiếp với `clip-3.md`, `clip-4.md`. Một chuỗi Extend dài tối đa 40 giây (4 clip); tập dài hơn thì Save frame khung cuối của clip thứ 4, mở chuỗi mới bằng **Frames** với `clip-5.md`, rồi Extend tiếp. Ghép các chuỗi trong Scenebuilder. Câu mở đầu clip 2 trở đi dùng được cho cả hai cách. Mốc giây trong prompt mỗi clip luôn tính từ đầu clip đó: 00:00 của Clip N là giây 10 × (N − 1) của tập (Clip 2 là giây 10, Clip 5 là giây 40).

**Ghép:** rê chuột lên clip → **More** → **Add to Scene** → trong Scenebuilder kéo các clip theo thứ tự → cắt bớt 0.2–0.5s ở chỗ nối nếu bị khựng → tải scene về. Tập dài 30–40 giây (3–4 clip) làm bằng một chuỗi Extend thì không cần bước này; tập dài 50–60 giây (5–6 clip), hoặc tập có clip mở lại bằng Ingredients, vẫn phải ghép các chuỗi Extend và các clip đó trong Scenebuilder.

**Flow đọc prompt thế nào:**
- Các nhãn `[FORMAT]`, `[CHARACTERS]`, `[SHOT LIST]`… chỉ là chữ thường để chia ý; model đọc như văn bản, không cần định dạng gì thêm. Giữ nguyên xuống dòng khi dán.
- Mốc giây `00:00–00:02 |` là nhịp hướng dẫn trong 10 giây. Model bám gần đúng chứ không chính xác từng khung hình.
- **Thoại không đặt trong ngoặc kép.** Gemini Omni hiểu chữ trong ngoặc kép là chữ cần hiện lên hình, nên dễ ra phụ đề. Prompt ghi thoại sau dấu hai chấm, ví dụ `PHÈO says (deep, warm chef voice; proud): Ngày tám, Phèo vô bếp!`. Mỗi mốc giây có tối đa một câu thoại, và câu thoại luôn đứng cuối dòng để model biết chỗ dừng. Không dùng ngoặc kép ở bất kỳ đâu trong prompt, kể cả phần mô tả âm thanh.
- **Omni mặc định tự chia nhiều cảnh trong một clip.** Prompt đã có câu `Cut only where the shot list says.`; mỗi mốc giây trong `[SHOT LIST]` là một cảnh hoặc một chuyển động máy.
- Prompt Clip 1 dài vài nghìn ký tự. Google chưa công bố giới hạn độ dài; nếu bản nháp bỏ sót chi tiết quan trọng, thay khối mô tả nhân vật đầy đủ bằng **SHORT LOCK** trong `FLOW_PROMPTS.md`, vì ảnh tham chiếu đã giữ ngoại hình.
- Omni chạy tốt nhất với tiếng Anh; thoại tiếng Việt vẫn tạo được nhưng có lúc lệch. Cách xử lý ở mục 5.

---

## 2. Thiết lập trước mỗi lần tạo

- **Tỉ lệ:** 9:16 (dọc TikTok)
- **Thời lượng:** 10s
- **Model:** bấm tên model → **Video** → **Gemini Omni** (mặc định Flow để model ảnh Nano Banana Pro). Nếu tài khoản cho chọn độ phân giải, chạy thử ở mức thấp cho rẻ, chốt ở 720p trở lên.
- **Chế độ:** Clip 1 dùng **Ingredients**; Clip 2 trở đi luôn dùng **Frames** (hoặc Extend) với khung cuối clip trước, kể cả clip đổi bối cảnh hoặc cắt cảnh.
- **Neo lại nhân vật ở tập dài:** nếu Frames cho đính ảnh, đính lại ảnh tham chiếu ở mọi clip. Nếu không, giữ FULL LOCK trong khối [CHARACTERS] của prompt để nhân vật không lệch dần qua nhiều lần Save frame; không bỏ khung cuối để mở lại bằng Ingredients.
- **Đặt tên theo mẫu:** `MIT_T01_C1_v1` (series_tập_clip_phiên bản)

---

## 3. Khóa nhân vật (quan trọng nhất)

1. **Tạo ảnh tham chiếu một lần duy nhất.** Mỗi file series có mục *"Ảnh tham chiếu nhân vật"* kèm prompt tạo ảnh. Chọn ảnh đẹp nhất cho mỗi nhân vật, lưu lại và **dùng cho mọi tập**.
2. **Đính kèm đúng nhân vật có mặt** trong clip đó, không đính thừa (đính thừa dễ làm xuất hiện nhân vật lạ). Omni nhận nhiều ảnh hơn Veo, nhưng quy tắc này vẫn giữ.
3. **Dán khối `[CHARACTERS]` nguyên văn, không sửa chữ nào.** Model nhận ra nhân vật nhờ chính câu chữ đó; đổi một từ cũng có thể làm đổi màu lông hoặc trang phục.
4. **Mô tả giọng y hệt nhau** ở mọi clip, mọi tập để giọng nhân vật giữ ổn định. Nếu Flow cho gắn `@Voice`, gắn thêm giọng cố định cho từng nhân vật.
5. **Không đổi trang phục** giữa các clip, trừ khi kịch bản ghi rõ *"Trang phục: biến thể B"*.
6. **Sản phẩm bán hàng:** đính kèm ảnh chụp sản phẩm thật làm tham chiếu. Prompt đã viết sẵn câu *matching the attached product reference image*. Model không viết chữ trên nhãn chuẩn được, nên nhãn để trống hoặc mờ; tên sản phẩm được nhắc trong thoại.

---

## 4. Cấu trúc một prompt

Prompt viết **bằng tiếng Anh**. **Thoại tiếng Việt** ghi sau dấu hai chấm, **không đặt trong ngoặc kép**, mỗi mốc giây tối đa một câu và câu thoại đứng cuối dòng.

> **Riêng Tây Du Ký 2026 là hoạt hình 2D** (từ 26/10/2026): [FORMAT], câu mở đầu clip 2 trở đi và câu chặn 3D cuối [AVOID] lấy ở mục 3 của [FLOW_PROMPTS.md](tay-du-ky-2026/FLOW_PROMPTS.md), không dùng khối 3D mẫu dưới đây.
>
> **Riêng Mẹ và Bé là hình người thật** (từ 26/10/2026): [FORMAT], câu mở đầu clip 2 trở đi và câu chặn cuối [AVOID] (chặn hình hoạt hình, em bé méo mặt, đồ trong nôi, bình bú) lấy ở mục 3 của [FLOW_PROMPTS.md](me-va-be/FLOW_PROMPTS.md). Video có người giống thật phải bật nhãn **Nội dung do AI tạo** khi đăng.
>
> **Riêng Biệt Đội Gara là người thật kèm chiến binh mặc giáp** (từ 26/10/2026): [FORMAT], câu mở đầu và câu chặn cuối [AVOID] (không súng, không máu, không đua ẩu ngoài đường thật, không giáp giống loạt phim có sẵn) lấy ở mục 4 của [FLOW_PROMPTS.md](biet-doi-gara/FLOW_PROMPTS.md). Mỗi nhân vật có khóa thường phục và khóa giáp; clip biến hình có thêm khối `[TRANSFORMATION IN THIS SEGMENT]`.

### Clip 1 — tạo mới (Ingredients)

```
[FORMAT]
Vertical 9:16, 10-second clip, high-end 3D animated film, Pixar/Disney-quality stylized CGI, soft global illumination, shallow depth of field, 24fps, cinematic color grade. Spoken dialogue in Vietnamese with a natural Southern Vietnamese accent and accurate lip-sync. Spoken lines are written after a colon following the speaker; they are only spoken aloud, never shown as text. Cut only where the shot list says. No subtitles, no captions, no on-screen text, no logos, no watermark.

[CHARACTERS — match the attached reference images exactly]
@<Tên Flow> = <TÊN>: <khóa nhân vật nguyên văn: loài, màu lông, dáng, mắt, trang phục, phụ kiện, giọng>

[SETTING]
<địa điểm, thời gian trong ngày, ánh sáng, đạo cụ chính>

[SHOT LIST]
00:00–00:02 | <cỡ cảnh + chuyển động máy> — <hành động>
00:02–00:05 | <cỡ cảnh> — <hành động>. <TÊN> says (<giọng>, <cảm xúc>): <thoại tiếng Việt>
00:05–00:08 | <cỡ cảnh> — <hành động>. <TÊN> says (<giọng>, <cảm xúc>): <thoại tiếng Việt>
00:08–00:10 | <cỡ cảnh> — <hành động dẫn sang khung cuối>

[SOUND]
<âm thanh môi trường, tiếng động, nhạc nền>

[END FRAME]
<khung cuối: ai đứng đâu, nhìn về đâu, cầm gì, góc máy, ánh sáng>. Hold still for the final 0.5 seconds.

[AVOID]
Extra characters, outfit changes, text or letters anywhere, subtitles, distorted paws or hands, ...
```

### Clip 2 trở đi — Frames (start frame = khung cuối clip trước) hoặc Extend

```
Continue the scene seamlessly from the final frame of the previous clip, which is the first frame of this clip. Same characters, same outfits, same location, same lighting and color grade. Flawless continuity, no time skip, no jump cut at the start.
Vertical 9:16, 10-second clip, same animation style. Spoken lines are written after a colon following the speaker; they are only spoken aloud in Vietnamese with a natural Southern accent and accurate lip-sync, never shown as text. Cut only where the shot list says. No subtitles, no captions, no on-screen text.

[CHARACTERS — unchanged]
@<Tên Flow> = <TÊN>: <khóa rút gọn 1 dòng: đặc điểm nhận dạng + trang phục + giọng>

[SHOT LIST] ... [SOUND] ... [END FRAME] ... [AVOID] ...
```

Khối `[FORMAT]` và hai dòng mở đầu clip 2 trở đi của từng series nằm ở mục 3 trong `FLOW_PROMPTS.md` của series đó.

---

## 5. Thoại

- **Một clip 10 giây chứa tối đa khoảng 31 âm tiết thoại**, và mỗi mốc có thoại cần đủ thời gian nói: **không quá 4,5 âm tiết mỗi giây**. Thoại dài hơn sẽ bị nói vội, hoặc bị Omni cắt bớt cho vừa clip. Tập dài hơn nghĩa là thêm clip, không phải nói nhanh hơn.
- **Không đặt thoại trong ngoặc kép** (Omni có thể in thành chữ trên hình). Mỗi mốc giây tối đa một câu thoại, đặt ở cuối dòng.
- Luôn ghi rõ **ai nói, giọng gì, cảm xúc gì**.
- Nếu model đọc tiếng Việt chưa chuẩn: vẫn giữ khẩu hình rồi **lồng tiếng lại** trong CapCut hoặc bằng công cụ giọng AI, dùng cùng một giọng cho mỗi nhân vật ở mọi tập.
- **Không có chữ trên video.** Nếu cần phụ đề thì thêm trong CapCut sau khi ghép.

---

## 6. Quy tắc TikTok

- **2 giây đầu phải có điểm thu hút:** một hành động bất ngờ, một câu thoại gây tò mò hoặc một cận cảnh mạnh. Các kịch bản đã đặt sẵn điểm này ở 00:00–00:02 của Clip 1.
- **Clip cuối kết bằng "điểm chốt":** cười, xúc động hoặc twist, kèm một khung cuối đứng yên đủ lâu để làm thumbnail.
- **Tập dài giữ nhịp:** khoảng 10–15 giây lại có một điểm mới; xem mục "Kịch bản như người thật chia sẻ" ở đầu file.
- **Sản phẩm:** chỉ xuất hiện tự nhiên trong câu chuyện, tối đa khoảng 10% thời lượng.

---

## 7. Lỗi thường gặp và cách sửa

| Lỗi | Cách sửa |
| --- | -------- |
| Nhân vật đổi mặt/màu lông giữa các clip | Đính lại ảnh tham chiếu, thêm câu `Maintain the exact character designs from the reference images.` |
| Xuất hiện chữ, biển hiệu, logo | Thêm vào [AVOID]: `any readable text, signage, labels, logos` |
| Thoại hiện thành chữ hoặc phụ đề | Kiểm tra prompt không còn dấu ngoặc kép và thoại nằm sau dấu hai chấm ở cuối dòng; nếu vẫn hiện, tạo lại hoặc thêm `no burned-in captions` vào [AVOID] |
| Omni tự cắt sang góc máy khác | Giữ câu `Cut only where the shot list says.`; với cảnh cần liền một hơi, thêm `In a single continuous shot.` vào mốc giây đó |
| Chỗ nối bị nhảy sáng hoặc nhảy màu | Thêm `same lighting direction and color grade as the previous segment` |
| Xuất hiện nhân vật lạ | Thêm `Only the listed characters appear in frame.` |
| Bàn tay/chân thú bị méo | Thêm `anatomically consistent paws with four fingers, clean hand poses` |
| Nói sai thoại, nói quá nhanh hoặc bị cắt câu | Rút ngắn thoại, mỗi câu ≤ 10 âm tiết, hoặc lồng tiếng lại |
| Hành động bị vội trong 10 giây | Bỏ bớt một hành động phụ ở mốc đó, giữ nguyên thoại và [END FRAME] |
| Máy quay chuyển động lung tung | Ghi rõ `static camera` hoặc `slow push-in only` cho từng mốc thời gian |
| Em bé (Mẹ và Bé) méo mặt, thừa ngón, trông như búp bê hoặc lớn hơn trẻ sơ sinh | Đính lại `REF_GAO`, `REF_BONG`; bớt cử động tay của bé ở mốc đó; tránh cận bàn tay bé quá 2 giây; tạo lại clip |
| Tây Du Ký ra hình 3D hoặc nửa 2D nửa 3D | Chỉ đính ảnh nhân vật bản 2D, không dùng lại ảnh 3D cũ, rồi tạo lại clip đó |

---

## Nguồn tham khảo

- [Generate and edit videos with Gemini Omni Flash — Gemini API docs](https://ai.google.dev/gemini-api/docs/omni): clip 3–10 giây, hỗ trợ 9:16 và 16:9; nối dài thêm tối đa 10 giây mỗi lần, tổng tối đa 40 giây; chữ muốn hiện lên hình thì ghi trong ngoặc kép; chống cắt cảnh bằng "In a single continuous shot"; tiếng Anh hỗ trợ đầy đủ nhất.
- [Gemini Omni 1.1 Flash Review — PromptsLove](https://promptslove.com/blog/gemini-omni-1-1-flash-review/): Omni có trong Google Flow từ 27/08/2026; Flow dùng thẻ `@Tên` và `@Voice`; ghi thoại sau dấu hai chấm, không dùng ngoặc kép vì ngoặc kép làm chữ hiện thành phụ đề; Omni mặc định tự chia nhiều cảnh; thoại dài có thể bị cắt.
- [Google Flow feature matrix — google-flow-scripting-skill](https://github.com/agbelemi/google-flow-scripting-skill/blob/main/reference/FLOW-FEATURES.md): trong Flow, Omni tạo 4/6/8/10 giây ở chế độ khung đầu và ảnh tham chiếu; không áp giới hạn 3 ảnh của Veo cho Omni.
- [Gemini Omni can now extend videos to 40 seconds — Digital Trends](https://www.digitaltrends.com/cool-tech/gemini-omni-can-now-extend-videos-to-40-seconds-and-upscale-them-to-4k/): Omni 1.1 nối dài từng đoạn 10 giây tới 40 giây, có trong Flow cho gói AI Plus, Pro, Ultra (27/08/2026).
- [Google Flow Video Length and How to Extend Clips — Toolfolio](https://toolfolio.com/articles/make-videos-longer-than-eight-seconds-in-veo): Veo 3.1 tạo 4/6/8 giây, Gemini Omni Flash tới 10 giây; bản cập nhật 06/10/2026 ghi Extend cho Omni Flash trong Flow là "sắp có".
- [Flow Help — tạo video trong Google Flow](https://support.google.com/flow/answer/16894016?hl=en): chế độ Frames và Ingredients, gọi ảnh và nhân vật bằng `@`, model mặc định là Nano Banana Pro.
- [Edit videos & build scenes in Google Flow — Google Labs Help](https://support.google.com/labs/answer/16935718?hl=en&co=GENIE.Platform%3DDesktop): Save frame, Add to Scene, Extend.
- Chuẩn cũ (Veo 3.1, đến 23/10/2026): [Veo 3.1 — Gemini API docs](https://ai.google.dev/gemini-api/docs/veo) (video 8 giây, khung đầu/cuối) · [Veo 3.1 Ingredients to Video — Google Blog](https://blog.google/innovation-and-ai/technology/ai/veo-3-1-ingredients-to-video/) · [Google Veo 3.1: What's New — RunDiffusion](https://www.rundiffusion.com/google-new-veo-3-1-model) (Ingredients tối đa 3 ảnh).
