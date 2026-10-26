# Hướng dẫn chung — Prompt Google Flow cho 4 series TikTok

**Áp dụng cho:** Mit & Đú 1970 · 365 Ngày Phèo Làm Nội Trợ · Nhà Tèo & Sún · Tây Du Ký 2026. Series 365 Ngày Việt Nam theo template riêng trong [MASTER_CONTEXT.md](365ngayvietnam/MASTER_CONTEXT.md); với series đó chỉ bảng **Độ dài tập** và mục **Kịch bản như người thật chia sẻ** dưới đây áp dụng chung.
**Model:** Gemini Omni trong Google Flow, **10 giây mỗi clip** (cập nhật 24/10/2026; trước đó dùng Veo 3.1, 8 giây mỗi clip)
**Cấu trúc mỗi thư mục series — mỗi ngày đăng 1 tập, ghép từ các clip 10 giây; độ dài tập theo từng series (bảng "Độ dài tập" bên dưới):**
- `tap-{số}/`: thư mục của một tập (một ngày đăng). `README.md` là tổng quan: tóm tắt, ảnh cần đính kèm, kịch bản nhanh, ghi chú. `clip-1.md`, `clip-2.md`, … `clip-N.md`: **mỗi clip 10 giây là một file chỉ chứa đúng prompt** (copy cả file dán vào Flow), tương ứng một lần tạo trên Flow. Tập mới đánh số tiếp.
- `FLOW_PROMPTS.md`: khóa nhân vật, bối cảnh, phong cách và prompt tạo ảnh tham chiếu, dùng chung cho mọi tập.

| Series | Khóa nhân vật & ảnh tham chiếu | Các tập (1 tập/ngày) |
| ------ | ------------------------------ | --------------------- |
| Mit & Đú 1970 | [FLOW_PROMPTS.md](mit-va-du-1970/FLOW_PROMPTS.md) | [tap-1](mit-va-du-1970/tap-1/README.md) → [tap-12](mit-va-du-1970/tap-12/README.md) |
| 365 Ngày Phèo Làm Nội Trợ | [FLOW_PROMPTS.md](pheo-va-no-meo/FLOW_PROMPTS.md) | [tap-1](pheo-va-no-meo/tap-1/README.md) → [tap-8](pheo-va-no-meo/tap-8/README.md) |
| Nhà Tèo & Sún | [FLOW_PROMPTS.md](teo-va-sun-cho/FLOW_PROMPTS.md) | [tap-1](teo-va-sun-cho/tap-1/README.md) → [tap-6](teo-va-sun-cho/tap-6/README.md) |
| Tây Du Ký 2026 | [FLOW_PROMPTS.md](tay-du-ky-2026/FLOW_PROMPTS.md) | [tap-1](tay-du-ky-2026/tap-1/README.md) → [tap-8](tay-du-ky-2026/tap-8/README.md) |
| 365 Ngày Việt Nam | [FLOW_PROMPTS.md](365ngayvietnam/FLOW_PROMPTS.md) | [tap-1](365ngayvietnam/tap-1/README.md) → [tap-365] |

**Tập chủ đề 20/10:** Mit & Đú tap-8 · Phèo tap-3 · Tèo & Sún tap-2 · Tây Du Ký tap-4

**Tập xu hướng:** chủ đề lấy từ từ khóa Google Trends và TikTok, ghi lại trong [TRENDS.md](TRENDS.md). Tập xu hướng nên đăng ngay, không cần chờ đúng thứ tự.

**Độ dài tập** (áp dụng cho tập mới từ 25/10/2026; các tập đã viết giữ nguyên độ dài cũ):

| Series | Độ dài | Số clip 10s | Xương sống mỗi tập | Áp dụng từ |
| ------ | ------ | ----------- | ------------------ | ---------- |
| Tây Du Ký 2026 | khoảng 60s | 6 | Hook và vấn đề → kế hoạch → phép thuật ra tay → leo thang → lật kèo → chốt cười, thumbnail | Tập 9 |
| Mit & Đú 1970 | 40–60s tùy câu chuyện | 4–6 | Lát cắt đời thường 1970 → chuyện nhỏ trong nhà → khoảnh khắc thương nhau → kết ấm áp, vui vẻ | Tập 13 |
| 365 Ngày Phèo Làm Nội Trợ | từ 90s trở lên | từ 9 | Đi chợ về → nguyên liệu, định lượng → sơ chế → nấu từng bước → nêm nếm, trình bày → dọn ra ăn cùng Hường → twist, đứng hình | Tập 9 |
| Nhà Tèo & Sún | 40–60s tùy câu chuyện | 4–6 | Chuyện trong nhà → Tèo vụng về hoặc trục trặc → mẹo đời sống (sản phẩm xuất hiện tự nhiên) → kết yêu thương | Tập 7 |
| 365 Ngày Việt Nam | khoảng 90s | 9 (8–10 tùy lộ trình) | Xem [MASTER_CONTEXT.md](365ngayvietnam/MASTER_CONTEXT.md) của series | Tập 5 |

**Kịch bản "như người thật chia sẻ"** (mọi series):
- **Mỗi clip có một điều mới** cho người xem: một chi tiết đời thật, một mẹo, một bước làm, một con số hoặc một nhịp cảm xúc. Không có clip chỉ để kéo dài.
- **Cụ thể như người đã làm thật:** tên món, định lượng, giờ giấc, nơi chốn, và vì sao làm như vậy. Giá cả, giờ mở cửa, luật lệ, công thức, mẹo chăm trẻ, mẹo sức khỏe và cách dùng hóa chất tẩy rửa phải kiểm chứng và ghi nguồn trong README (ưu tiên Bộ Y tế, WHO, hướng dẫn trên nhãn sản phẩm).
- **Nói như người thật:** câu ngắn, giọng miền Nam tự nhiên, có cảm thán, có kể chuyện ngôi thứ nhất; không đọc như thuyết minh, không giảng đạo lý.
- **Tập dài không nói nhanh hơn:** mỗi clip vẫn tối đa khoảng 31 âm tiết thoại; muốn chia sẻ nhiều hơn thì thêm clip.
- **Giữ người xem:** khoảng 10–15 giây lại có một điểm mới (câu hỏi, bất ngờ, mẹo, tình huống); clip cuối luôn có điểm chốt và khung thumbnail.

---

## 1. Dán prompt vào Flow từng bước

Gemini Omni tạo **tối đa 10 giây mỗi lần** (Veo 3.1 chỉ được 8 giây), nên tập dài bao nhiêu thì ghép bấy nhiêu clip 10 giây: 40–60 giây là 4–6 clip, 90 giây là 9 clip (bảng "Độ dài tập" ở trên). **Mỗi file `clip-{số}.md` chỉ chứa đúng prompt:** mở file, bấm Cmd+A rồi Cmd+C, dán vào ô prompt của Flow, không sửa gì.

| Clip | Thời gian | Chế độ trong Flow | Đính kèm |
| ---- | --------- | ----------------- | -------- |
| **Clip 1** | 00:00–00:10 | **Video → Gemini Omni → Ingredients** | Ảnh nhân vật và sản phẩm ghi trong README của tập |
| **Clip 2** | 00:10–00:20 | **Video → Gemini Omni → Frames** | Start frame = khung cuối Clip 1 (Save frame) |
| **Clip 3 trở đi** | mỗi clip thêm 10 giây | **Video → Gemini Omni → Frames** | Start frame = khung cuối clip ngay trước |
| **Clip đổi bối cảnh hoặc cắt cảnh** | — | **Video → Gemini Omni → Ingredients** | Khi README ghi clip đó mở cảnh mới hoặc nhảy thời gian: đính lại ảnh tham chiếu, dán [FORMAT] và FULL LOCK như Clip 1, không dán câu Continue the scene seamlessly… |

Nếu giao diện Flow đặt tên chế độ khác, chọn chế độ tạo video từ ảnh tham chiếu cho Clip 1 và chế độ khung đầu (first frame) cho Clip 2 trở đi.

**Nhảy thời gian trong tập** (ướp, kho, chiều hôm đó, sáng hôm sau), chọn một trong ba cách:
1. **Trong cùng clip:** tiếng hẹn giờ ting, mở nắp thấy món đã xong; dùng khi chỉ chờ tối đa khoảng 30 phút.
2. **Đồ làm sẵn:** nhân vật lấy tô đã ướp sẵn trong tủ lạnh và nói ra, ví dụ: Tô này Phèo ướp từ sáng!
3. **Cắt cảnh:** mở clip mới bằng **Ingredients** với [FORMAT] và FULL LOCK, không dùng câu Continue…; dòng đầu [SHOT LIST] ghi rõ, ví dụ `Hard cut: thirty minutes later, same kitchen, same outfits, same lighting.` README ghi rõ clip nào là cắt cảnh.

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

Mit & Đú và Tèo & Sún dùng luôn tên Flow trong cả prompt. Phèo và Tây Du Ký giữ tên gốc trong phần còn lại của prompt: "No" là từ tiếng Anh, viết "No walks in…" model dễ hiểu nhầm. Nếu nhân vật trên Flow được tạo từ ảnh bộ đồ thường ngày, ở các tập mặc đồ khác (Mit & Đú tập 3, 4 và cảnh mơ tập 10, Tèo & Sún tập 2, Tây Du Ký tập 3) thì đính thêm ảnh bộ đồ đó.

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

**Ghép:** rê chuột lên clip → **More** → **Add to Scene** → trong Scenebuilder kéo các clip theo thứ tự → cắt bớt 0.2–0.5s ở chỗ nối nếu bị khựng → tải scene về. Tập dài tối đa 40 giây (4 clip) làm bằng một chuỗi Extend thì không cần bước này; tập dài hơn (Tây Du Ký 60 giây, Phèo và 365 Ngày Việt Nam 90 giây, Mit và Tèo 5–6 clip) vẫn phải ghép các chuỗi Extend và các clip mở lại bằng Ingredients trong Scenebuilder.

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
- **Chế độ:** Clip 1 dùng **Ingredients**; Clip 2 trở đi dùng **Frames** (hoặc Extend); clip đổi bối cảnh hoặc cắt cảnh dùng lại **Ingredients**.
- **Neo lại nhân vật ở tập dài:** nếu Frames cho đính ảnh, đính lại ảnh tham chiếu ở mọi clip. Nếu không, cứ sau 3–4 clip mở một clip bằng **Ingredients** (cắt theo hành động, dán [FORMAT] và FULL LOCK) để nhân vật không lệch dần qua nhiều lần Save frame.
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

> **Riêng Tây Du Ký 2026 là hoạt hình 2D** (từ 26/10/2026): [FORMAT] và câu mở đầu Clip 2/3 lấy ở mục 3 của [FLOW_PROMPTS.md](tay-du-ky-2026/FLOW_PROMPTS.md), không dùng khối 3D mẫu dưới đây.

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
