# Hướng dẫn chung — Prompt Google Flow cho 4 series TikTok

**Áp dụng cho:** Mit & Đú 1970 · 365 Ngày Phèo Làm Nội Trợ · Nhà Tèo & Sún · Tây Du Ký 2026
**Model:** Veo 3.1 trong Google Flow, **8 giây mỗi clip** (cập nhật 20/10/2026)
**Cấu trúc mỗi thư mục series — mỗi ngày đăng 1 tập (24s = 3 clip × 8s):**
- `tap-{số}/`: thư mục của một tập (một ngày đăng). `README.md` là tổng quan: tóm tắt, ảnh cần đính kèm, kịch bản nhanh, ghi chú. `clip-1.md`, `clip-2.md`, `clip-3.md`: **mỗi clip 8 giây là một file chỉ chứa đúng prompt** (copy cả file dán vào Flow), tương ứng một lần tạo trên Flow. Tập mới đánh số tiếp.
- `FLOW_PROMPTS.md`: khóa nhân vật, bối cảnh, phong cách và prompt tạo ảnh tham chiếu, dùng chung cho mọi tập.

| Series | Khóa nhân vật & ảnh tham chiếu | Các tập (1 tập/ngày) |
| ------ | ------------------------------ | --------------------- |
| Mit & Đú 1970 | [FLOW_PROMPTS.md](mit-va-du-1970/FLOW_PROMPTS.md) | [tap-1](mit-va-du-1970/tap-1/README.md) → [tap-11](mit-va-du-1970/tap-11/README.md) |
| 365 Ngày Phèo Làm Nội Trợ | [FLOW_PROMPTS.md](pheo-va-no-meo/FLOW_PROMPTS.md) | [tap-1](pheo-va-no-meo/tap-1/README.md) → [tap-7](pheo-va-no-meo/tap-7/README.md) |
| Nhà Tèo & Sún | [FLOW_PROMPTS.md](teo-va-sun-cho/FLOW_PROMPTS.md) | [tap-1](teo-va-sun-cho/tap-1/README.md) → [tap-6](teo-va-sun-cho/tap-6/README.md) |
| Tây Du Ký 2026 | [FLOW_PROMPTS.md](tay-du-ky-2026/FLOW_PROMPTS.md) | [tap-1](tay-du-ky-2026/tap-1/README.md) → [tap-7](tay-du-ky-2026/tap-7/README.md) |
| 365 Ngày Việt Nam | [FLOW_PROMPTS.md](365ngayvietnam/FLOW_PROMPTS.md) | [tap-1](365ngayvietnam/tap-1/README.md) → [tap-365] |

**Tập chủ đề 20/10:** Mit & Đú tap-8 · Phèo tap-3 · Tèo & Sún tap-2 · Tây Du Ký tap-4

**Tập xu hướng:** chủ đề lấy từ từ khóa Google Trends và TikTok, ghi lại trong [TRENDS.md](TRENDS.md). Tập xu hướng nên đăng ngay, không cần chờ đúng thứ tự.

---

## 1. Dán prompt vào Flow từng bước

Veo 3.1 tạo **tối đa 8 giây mỗi lần**, nên mỗi tập gồm 3 clip 8 giây (tổng 24 giây). **Mỗi file `clip-{số}.md` chỉ chứa đúng prompt:** mở file, bấm Cmd+A rồi Cmd+C, dán vào ô prompt của Flow, không sửa gì.

| Clip | Thời gian | Chế độ trong Flow | Đính kèm |
| ---- | --------- | ----------------- | -------- |
| **Clip 1** | 00:00–00:08 | **Video → Veo 3.1 → Ingredients** | Tối đa 3 ảnh: nhân vật và sản phẩm ghi trong README của tập |
| **Clip 2** | 00:08–00:16 | **Video → Veo 3.1 → Frames** | Start frame = khung cuối Clip 1 (Save frame) |
| **Clip 3** | 00:16–00:24 | **Video → Veo 3.1 → Frames** | Start frame = khung cuối Clip 2 *(bỏ clip này nếu chỉ cần tập 16s)* |

**Chuẩn bị một lần cho mỗi series:**
- Tạo nhân vật trên Flow từ ảnh tham chiếu và đặt **đúng tên** như bảng dưới. Dòng khai báo nhân vật trong prompt đã ghi sẵn dạng `@Pheo = PHÈO: …`: Flow gọi đúng nhân vật đã lưu, còn model hiểu PHÈO trong cả prompt chính là `@Pheo`.
- Tải ảnh sản phẩm (`SP_…`) và ảnh nhân vật phụ (`REF_…`) vào project, **giữ đúng tên file** để gọi được bằng `@`.

| Series | Tên nhân vật trên Flow | Tên trong prompt |
| ------ | ---------------------- | ---------------- |
| Mit & Đú 1970 | `@Mit` · `@Đú` · `@Nở` | Mit · Đú · Nở |
| 365 Ngày Phèo Làm Nội Trợ | `@Pheo` · `@No` | PHÈO · BÀ CHỦ HƯỜNG |
| Nhà Tèo & Sún | `@TeoTeo` (chó đực) · `@SunSun` (chó cái) | TeoTeo · SunSun |
| Tây Du Ký 2026 | `@Thay` · `@DaiCa` · `@HeoLuoi` · `@UtKho` | THẦY · ĐẠI CA · HEO LƯỜI · ÚT KHỜ |

Mit & Đú và Tèo & Sún dùng luôn tên Flow trong cả prompt. Phèo và Tây Du Ký giữ tên gốc trong phần còn lại của prompt: "No" là từ tiếng Anh, viết "No walks in…" model dễ hiểu nhầm. Nếu nhân vật trên Flow được tạo từ ảnh bộ đồ thường ngày, ở các tập mặc đồ khác (Mit & Đú tập 3, 4 và cảnh mơ tập 10, Tèo & Sún tập 2, Tây Du Ký tập 3) thì đính thêm ảnh bộ đồ đó.

**Clip 1**
1. Bấm tên model ở ô prompt → **Video** → **Veo 3.1** → **Ingredients**. Mặc định Flow để model ảnh Nano Banana Pro: quên đổi sẽ ra ảnh, không ra video.
2. Thiết lập: dọc 9:16, độ dài 8s, số kết quả 2.
3. Đính ảnh: kéo thả vào ô prompt hoặc bấm **Add** bên dưới ô prompt. **Veo chỉ nhận tối đa 3 ảnh**: nếu README ghi nhiều hơn, ưu tiên nhân vật có mặt lâu nhất trong clip, rồi đến sản phẩm.
4. Dán prompt `clip-1.md`.
5. Kiểm tra dòng khai báo nhân vật: sau khi dán, `@Mit`, `@TeoTeo`… phải hiện thành thẻ nhân vật của Flow. Nếu vẫn là chữ thường, xóa `@Tên` rồi gõ lại `@` và chọn nhân vật trong danh sách. Nếu Veo không nhận thẻ nhân vật, đính ảnh `REF_…` như cũ. Với ảnh sản phẩm, gõ `@` chọn ảnh rồi ghi vai trò, ví dụ `@SP_TAP is the notebook.`
6. Bấm Generate, chọn bản đẹp nhất.

**Clip 2 và 3**
1. Mở clip vừa chọn, dừng ở khung cuối, bấm **Save frame**.
2. Bấm tên model → **Video** → **Veo 3.1** → **Frames**, kéo ảnh vừa lưu vào **+ Add start frame**.
3. Dán prompt `clip-2.md` (hoặc `clip-3.md`). Câu đầu prompt đã viết sẵn cho cách này: "Start exactly from the provided first frame…".
4. Bấm Generate. Clip 3 làm giống vậy, lấy khung cuối của Clip 2.

**Có thể dùng Extend không:** clip Veo 3.1 dài 8 giây có nút **Extend**, nhưng phần nối thêm chạy bằng **Veo 3.1 Lite** (bản nhẹ hơn) và tiếp nối từ giây cuối, nên chất lượng và độ dài có thể khác clip 1. Cách Save frame → Frames giữ đủ 8 giây và cùng model. Nếu vẫn muốn dùng Extend, thay câu đầu prompt clip 2, 3 bằng `Continue the scene seamlessly from the final frame of the previous clip.` Prompt nào cũng có mục **[END FRAME]** mô tả khung cuối, nên cách nào các clip cũng nối khớp.

**Ghép:** rê chuột lên clip → **More** → **Add to Scene** → trong Scenebuilder kéo các clip theo thứ tự → cắt bớt 0.2–0.5s ở chỗ nối nếu bị khựng → tải scene về.

**Flow đọc prompt thế nào:**
- Các nhãn `[FORMAT]`, `[CHARACTERS]`, `[SHOT LIST]`… chỉ là chữ thường để chia ý; model đọc như văn bản, không cần định dạng gì thêm. Giữ nguyên xuống dòng khi dán.
- Mốc giây `00:00–00:02 |` là nhịp hướng dẫn trong 8 giây. Model bám gần đúng chứ không chính xác từng khung hình.
- Prompt Clip 1 dài vài nghìn ký tự. Google chưa công bố giới hạn độ dài; nếu bản nháp bỏ sót chi tiết quan trọng, thay khối mô tả nhân vật đầy đủ bằng **SHORT LOCK** trong `FLOW_PROMPTS.md`, vì ảnh tham chiếu đã giữ ngoại hình.
- **Giọng:** gắn giọng cố định bằng `@Voice` chỉ có ở Gemini Omni, không có ở Veo. Giọng nhân vật dựa vào mô tả giọng trong khóa nhân vật; nếu giọng giữa các clip lệch nhau, lồng tiếng lại trong CapCut.

---

## 2. Thiết lập trước mỗi lần tạo

- **Tỉ lệ:** 9:16 (dọc TikTok)
- **Thời lượng:** 8s
- **Model:** bấm tên model → **Video** → **Veo 3.1** (mặc định Flow để model ảnh Nano Banana Pro). Chạy thử bằng bản Fast cho rẻ, chốt bằng bản Quality nếu tài khoản có.
- **Chế độ:** Clip 1 dùng **Ingredients** (tối đa 3 ảnh), Clip 2–3 dùng **Frames**
- **Đặt tên theo mẫu:** `MIT_T01_C1_v1` (series_tập_clip_phiên bản)

---

## 3. Khóa nhân vật (quan trọng nhất)

1. **Tạo ảnh tham chiếu một lần duy nhất.** Mỗi file series có mục *"Ảnh tham chiếu nhân vật"* kèm prompt tạo ảnh. Chọn ảnh đẹp nhất cho mỗi nhân vật, lưu lại và **dùng cho mọi tập**.
2. **Đính kèm đúng nhân vật có mặt** trong clip đó, không đính thừa (đính thừa dễ làm xuất hiện nhân vật lạ). Veo nhận tối đa 3 ảnh mỗi lần tạo.
3. **Dán khối `[CHARACTERS]` nguyên văn, không sửa chữ nào.** Model nhận ra nhân vật nhờ chính câu chữ đó; đổi một từ cũng có thể làm đổi màu lông hoặc trang phục.
4. **Mô tả giọng y hệt nhau** ở mọi clip, mọi tập để giọng nhân vật giữ ổn định.
5. **Không đổi trang phục** giữa các clip, trừ khi kịch bản ghi rõ *"Trang phục: biến thể B"*.
6. **Sản phẩm bán hàng:** đính kèm ảnh chụp sản phẩm thật làm tham chiếu. Prompt đã viết sẵn câu *"matching the attached product reference image"*. Model không viết chữ trên nhãn chuẩn được, nên nhãn để trống hoặc mờ; tên sản phẩm được nhắc trong thoại.

---

## 4. Cấu trúc một prompt

Prompt viết **bằng tiếng Anh**, **thoại tiếng Việt** đặt trong ngoặc kép.

> **Riêng Tây Du Ký 2026 là hoạt hình 2D** (từ 26/10/2026): [FORMAT] và câu mở đầu Clip 2/3 lấy ở mục 3 của [FLOW_PROMPTS.md](tay-du-ky-2026/FLOW_PROMPTS.md), không dùng khối 3D mẫu dưới đây.

### Clip 1 — tạo mới (Ingredients)

```
[FORMAT]
Vertical 9:16, 8-second shot, high-end 3D animated film, Pixar/Disney-quality stylized CGI, soft global illumination, shallow depth of field, 24fps, cinematic color grade. Spoken dialogue in Vietnamese with a natural Southern Vietnamese accent and accurate lip-sync. No subtitles, no captions, no on-screen text, no logos, no watermark.

[CHARACTERS — match the attached reference images exactly]
@<Tên Flow> = <TÊN>: <khóa nhân vật nguyên văn: loài, màu lông, dáng, mắt, trang phục, phụ kiện, giọng>

[SETTING]
<địa điểm, thời gian trong ngày, ánh sáng, đạo cụ chính>

[SHOT LIST]
00:00–00:02 | <cỡ cảnh + chuyển động máy> — <hành động>
00:02–00:05 | <cỡ cảnh> — <TÊN> says (<giọng>, <cảm xúc>): "<thoại tiếng Việt>"
00:05–00:08 | <cỡ cảnh> — <hành động dẫn sang khung cuối>

[SOUND]
<âm thanh môi trường, tiếng động, nhạc nền>

[END FRAME]
<khung cuối: ai đứng đâu, nhìn về đâu, cầm gì, góc máy, ánh sáng>. Hold still for the final 0.5 seconds.

[AVOID]
Extra characters, outfit changes, text or letters anywhere, distorted paws or hands, ...
```

### Clip 2 và 3 — Frames (start frame = khung cuối clip trước)

```
Start exactly from the provided first frame (the final frame of the previous clip) and continue the scene seamlessly. Same characters, same outfits, same location, same lighting and color grade. Flawless continuity, no time skip, no jump cut at the start.

[CHARACTERS — unchanged]
@<Tên Flow> = <TÊN>: <khóa rút gọn 1 dòng: đặc điểm nhận dạng + trang phục + giọng>

[SHOT LIST] ... [SOUND] ... [END FRAME] ... [AVOID] ...
```

---

## 5. Thoại

- **Một clip 8 giây chứa tối đa khoảng 25 âm tiết thoại**, và mỗi mốc có thoại cần đủ thời gian nói: **không quá 4,5 âm tiết mỗi giây**. Toàn bộ prompt đã được canh theo nhịp này; thoại dài hơn sẽ bị nói vội hoặc bị cắt.
- Luôn ghi rõ **ai nói, giọng gì, cảm xúc gì**.
- Nếu model đọc tiếng Việt chưa chuẩn: vẫn giữ khẩu hình rồi **lồng tiếng lại** trong CapCut hoặc bằng công cụ giọng AI, dùng cùng một giọng cho mỗi nhân vật ở mọi tập.
- **Không có chữ trên video.** Nếu cần phụ đề thì thêm trong CapCut sau khi ghép.

---

## 6. Quy tắc TikTok

- **2 giây đầu phải có điểm thu hút:** một hành động bất ngờ, một câu thoại gây tò mò hoặc một cận cảnh mạnh. Các kịch bản đã đặt sẵn điểm này ở 00:00–00:02 của Clip 1.
- **Clip 3 kết bằng "điểm chốt":** cười, xúc động hoặc twist, kèm một khung cuối đứng yên đủ lâu để làm thumbnail.
- **Sản phẩm:** chỉ xuất hiện tự nhiên trong câu chuyện, tối đa khoảng 10% thời lượng.

---

## 7. Lỗi thường gặp và cách sửa

| Lỗi | Cách sửa |
| --- | -------- |
| Nhân vật đổi mặt/màu lông giữa các clip | Đính lại ảnh tham chiếu, thêm câu `Maintain the exact character designs from the reference images.` |
| Xuất hiện chữ, biển hiệu, logo | Thêm vào [AVOID]: `any readable text, signage, labels, logos` |
| Video tự hiện phụ đề theo lời thoại | Prompt đã có `No subtitles, no captions`; nếu vẫn hiện, tạo lại hoặc thêm `no burned-in captions` vào [AVOID] |
| Chỗ nối bị nhảy sáng hoặc nhảy màu | Thêm `same lighting direction and color grade as the previous segment` |
| Xuất hiện nhân vật lạ | Thêm `Only the listed characters appear in frame.` |
| Bàn tay/chân thú bị méo | Thêm `anatomically consistent paws with four fingers, clean hand poses` |
| Nói sai thoại hoặc nói quá nhanh | Rút ngắn thoại, mỗi câu ≤ 10 âm tiết, hoặc lồng tiếng lại |
| Hành động bị vội trong 8 giây | Bỏ bớt một hành động phụ ở mốc đó, giữ nguyên thoại và [END FRAME] |
| Máy quay chuyển động lung tung | Ghi rõ `static camera` hoặc `slow push-in only` cho từng mốc thời gian |
| Tây Du Ký ra hình 3D hoặc nửa 2D nửa 3D | Chỉ đính ảnh nhân vật bản 2D, không dùng lại ảnh 3D cũ, rồi tạo lại clip đó |

---

## Nguồn tham khảo

- [Veo 3.1 — Gemini API docs](https://ai.google.dev/gemini-api/docs/veo): video 8 giây, hỗ trợ 16:9 và 9:16, khung đầu/cuối; qua API mỗi lần Extend thêm 7 giây.
- [Veo 3.1 Ingredients to Video — Google Blog](https://blog.google/innovation-and-ai/technology/ai/veo-3-1-ingredients-to-video/): Ingredients có xuất dọc 9:16.
- [Bringing new Veo 3.1 updates into Flow — Google Blog](https://blog.google/innovation-and-ai/products/veo-updates-flow/): Extend trong Flow cho video dài từ một phút trở lên.
- [Google Veo 3.1: What's New — RunDiffusion](https://www.rundiffusion.com/google-new-veo-3-1-model): Ingredients nhận tối đa 3 ảnh tham chiếu.
- [Google Flow Video Length and How to Extend Clips — Toolfolio](https://toolfolio.com/articles/make-videos-longer-than-eight-seconds-in-veo): Veo 3.1 tạo 4/6/8 giây; chỉ clip 8 giây mới Extend được; phần Extend chạy bằng Veo 3.1 Lite.
- [Flow Help — tạo video trong Google Flow](https://support.google.com/flow/answer/16894016?hl=en): chế độ Frames và Ingredients, gọi ảnh và nhân vật bằng `@`, model mặc định là Nano Banana Pro.
- [Edit videos & build scenes in Google Flow — Google Labs Help](https://support.google.com/labs/answer/16935718?hl=en&co=GENIE.Platform%3DDesktop): Save frame, Add to Scene, Extend.
