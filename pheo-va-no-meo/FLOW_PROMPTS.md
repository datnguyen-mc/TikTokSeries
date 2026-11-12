# 365 Ngày Phèo Làm Nội Trợ — Prompt Google Flow (Gemini Omni)

> **🗣️ QUY TẮC GIỌNG (từ 07/11/2026 — ưu tiên cao nhất, thay mọi chỗ ghi "giọng miền Nam" bên dưới):** toàn bộ thoại dùng **giọng Bắc thanh thoát** — giọng Hà Nội chuẩn, nhẹ, rõ, tinh tế. Trong prompt: câu FORMAT ghi "a soft, clear, elegant standard Northern Vietnamese (Hà Nội) accent"; mỗi `Voice:` kết thúc bằng "elegant standard Hà Nội Northern Vietnamese accent"; AVOID có "Southern or Central Vietnamese accents". Từ ngữ cũng theo miền Bắc: này/đây, nhé, không, vào, thật, quá/thế, thìa, bát, cốc, lợn, đắt, quả, hoa, nhặt, rơi, xem, gọi (không dùng nè, nghen, hông, vô, thiệt, ghê, muỗng, chén, ly, heo, mắc, trái, lượm, rớt, coi, kêu). Chuẩn viết clip: `flowkit/docs/TIKTOK_PROMPT_SPEC.md`, kiểm tra bằng `python3 flowkit/scripts/check_tiktok_episode.py <thư mục tập>`.


> Quy trình, thiết lập, lỗi thường gặp: xem [../FLOW_GUIDE.md](../FLOW_GUIDE.md)

**Định dạng chuẩn bắt buộc (từ 11/11/2026, Tập 24 trở đi):** mỗi tập là **"CÓ BIẾN!" — PHÈO & BÀ CHỦ HƯỜNG BÀN DRAMA CỦA NGÀY THEO CÁCH HÀI HƯỚC, MỖI CLIP MỘT TIN MỚI Ở MỘT LĨNH VỰC KHÁC NHAU (`60 giây = 6 clip × 10s`)** · tạo bằng **Gemini Omni** trong Google Flow · 9:16 · thoại tiếng Việt giọng Bắc thanh thoát (Hà Nội chuẩn) · không chữ trên video. Mẫu: [tap-24/](tap-24/README.md). Các tập 1–23 giữ nguyên file cũ (tập 17–23 theo định dạng dạy nấu ăn bên dưới).

> **Cấu trúc bắt buộc "Có biến!" (60 giây = 6 clip × 10s):**
> - **Lấy tin:** quét tin của 24 giờ gần nhất, tối đa 48 giờ trước giờ đăng (RSS Google Trends VN, VnExpress, Dân trí, Tuổi Trẻ, Thanh Niên), mở bài gốc kiểm chứng rồi ghi log vào `TRENDS.md`. Mỗi clip một tin thuộc **một lĩnh vực khác nhau**: mua sắm, tài chính – giá cả, công nghệ – mạng xã hội, thể thao, giáo dục – việc làm, đời sống – thời tiết, cảnh giác lừa đảo, giải trí… Không hai clip cùng lĩnh vực.
>   1. **Clip 1 — Hook + tin nóng nhất:** giây 0–2 Hường mở bằng câu cửa miệng **"Em ơi, có biến!"** (đúng một lần mỗi tập), rồi nói tin; Phèo bình một câu chốt.
>   2. **Clip 2–5 — Mỗi clip một tin:** người đưa tin nói một câu đời thường (không đọc tiêu đề báo), người kia chốt một câu hài. Sợi chỉ xuyên tập: **Phèo lái tin nào cũng về chuyện lương thưởng của mình, Hường né bằng một câu keo kiệt hoặc giả điếc.** Mỗi tin có **một đạo cụ hoặc cử chỉ** để người xem hiểu bằng hình (vòng vàng, cờ cổ vũ, điện thoại selfie…).
>   3. **Clip 6 — Lật kèo:** tin cuối gắn với chính ngày hôm đó (ngày lễ, sự kiện); Hường tặng Phèo một món quà hiểu theo nghĩa đen (Tập 24: Lễ độc thân → một chiếc đũa lẻ) → `SIGNATURE FREEZE` ở 1,5–2 giây cuối.
> - **Bối cảnh cố định:** góc bàn ăn cạnh bếp, buổi sáng muộn, ánh nắng qua rèm trắng bên trái; bàn tròn gỗ tối khăn ren trắng, ấm trà sứ trắng, hai chén trà, đĩa hạt hướng dương. **Hường ngồi ghế bành chạm gỗ đệm hồng bên trái, Phèo ngồi ghế nhựa đỏ thấp bên phải** (miếng hài hình ảnh cố định); không ai đứng dậy, không nấu nướng. Khối `[FORMAT]`, `[CHARACTERS …]`, `[CHARACTER STATE …]` và `[SET LOCK …]` chép nguyên văn từ `tap-24/clip-1.md` (chỉ đổi số tập).
> - **Điện thoại** của Hường luôn quay màn hình về phía Hường hoặc úp xuống bàn; không TV, không báo giấy, không màn hình có chữ.
> - **Lọc tin:** không thiên tai, tai nạn, án hình sự, điều tra, chính trị, chiến tranh, tôn giáo, bệnh tật của người thật, trẻ em thật, xổ số – cờ bạc; **không nêu tên người thật, tên sàn, tên hãng, thương hiệu** (nói "mạng xã hội", "sàn nào cũng sale"). Tin lừa đảo chỉ dùng khi câu chốt là lời nhắc cảnh giác. Số liệu đúng bài báo, đọc tròn bằng chữ.
> - **Thoại:** tối đa 2 lượt mỗi clip, 18–34 âm tiết, ≤ 4,2 âm tiết/giây; phản ứng trước rồi mới nói; không tự gọi tên mình; không lặp một cụm nội dung quá hai lần trong tập; nhịp cảm xúc của cùng một nhân vật không trùng ở hai clip liền nhau. Tin bám giờ (ví dụ "tối nay tuyển đá") chỉ dùng khi chắc chắn đăng kịp, nếu không thì viết cho không lệ thuộc giờ.
> - **README tập:** bảng sáu tin (lĩnh vực, tin, nguồn có link và giờ đăng, miếng hài), danh sách tin đã quét nhưng không dùng kèm lý do, hạn đăng (48 giờ tính từ tin cũ nhất), bảng lời thoại, ghi chú đạo cụ. `caption.md`: câu hỏi kéo bình luận, đúng 5 hashtag, không gắn giỏ hàng.

> **Định dạng cũ — Tập 17–23, không dùng cho tập mới:**
>
> **Cấu trúc chuẩn bắt buộc cho Series Phèo (Clip Dài 60s = 6 Clip × 10s — Hướng Dẫn Chi Tiết Từng Phần Cách Nấu Ngon, Gia Vị & Mẹo):**
> - **Mỗi tập chuẩn 60 giây (`6 clip × 10s`)** chia thành **6 phần hướng dẫn nấu ăn chuyên sâu, rõ ràng từng bước** để người xem nhìn và nghe là nấu theo thành công ngay:
>   1. **Clip 1 (00:00–00:10) — Phần 1: Cách chọn nguyên liệu tươi ngon & Giao kèo vào bếp:** Mở màn bằng nguyên liệu chính trên đảo bếp; `@Pheo` chỉ rõ **mẹo chọn nguyên liệu tươi ngon ngoài chợ** (cách nhìn màu thịt/cá, độ đàn hồi, lớp mỡ/da) kèm định lượng chuẩn xác; Bà chủ Hường (`@No`) bước vào giao đề bài / thử thách nấu ăn.
>   2. **Clip 2 (00:10–00:20) — Phần 2: Mẹo sơ chế & Bí quyết khử mùi tanh/nhớt/hôi:** `@Pheo` thực hiện và giải thích chi tiết **mẹo sơ chế nhà nghề** (chà muối hạt + chanh tươi, bóp gừng đập dập + rượu trắng, luộc sơ khử chua, thấm khô mặt bì...) giúp nguyên liệu sạch mùi, giòn ngọt và không bị bắn dầu khi chế biến.
>   3. **Clip 3 (00:20–00:30) — Phần 3: Công thức ướp & Pha sốt "Tỷ lệ vàng" (`Gia vị chuẩn`):** `@Pheo` đong rõ từng muỗng gia vị (muỗng canh nước mắm, muỗng đường, tiêu xay, hành tỏi băm, dầu hào...) và chỉ **mẹo thứ tự ướp gia vị** (ví dụ: ướp đường trước 15 phút để mỡ trong giòn, hoặc pha sốt tỷ lệ vàng trước khi rim để gia vị thấm đều không cháy).
>   4. **Clip 4 (00:30–00:40) — Phần 4: Kỹ thuật thắng màu / Phi thơm & Vào lửa đầu:** `@Pheo` hướng dẫn chi tiết nhiệt độ nồi/chảo, mẹo thắng nước màu cánh gián chuẩn không bị đắng, phi thơm hành tỏi gừng sả và áp chảo/xào săn nguyên liệu để khóa trọn nước ngọt tự nhiên bên trong.
>   5. **Clip 5 (00:40–00:50) — Phần 5: Bí quyết canh lửa, Châm nước & Thời gian nấu chuẩn xác:** `@Pheo` chỉ rõ mức lửa (lửa lớn hớt bọt hay lửa riu riu kho tộ), loại nước châm thêm (nước dừa tươi hay nước sôi), thời gian nấu chính xác từng phút và mẹo giữ cho nước sốt sánh kẹo bóng mượt hoặc nước canh trong vắt.
>   6. **Clip 6 (00:50–01:00) — Phần 6: Mẹo dậy hương cuối món, Bày ra đĩa & Cú lật kèo hài hước:** `@Pheo` chỉ mẹo rắc tiêu sọ đập dập / hành lá / ngò gai / ớt hiểm ngay lúc vừa tắt bếp để giữ trọn tinh dầu thơm; Bà chủ Hường thưởng thức mê mẩn khen nức nở rồi tung cú lật kèo "thưởng bá đạo" khiến `@Pheo` đứng hình (`SIGNATURE FREEZE`).
> - **Ngân sách thoại:** mỗi clip tối đa khoảng 31 âm tiết (`@Pheo` khoảng 20–24 âm tiết hướng dẫn rõ định lượng gia vị + mẹo nấu ngon, `@No` tối đa 7–10 âm tiết tung hứng hài hước). Số trong thoại viết bằng chữ tiếng Việt (năm trăm gam, ba muỗng canh, mười lăm phút).
> - **Định lượng thể hiện trực quan bằng hình:** gia vị chia sẵn trong chén sứ trắng nhỏ, đong bằng muỗng canh và muỗng cà phê trơn; không dùng cân điện tử, ly đong có vạch số hay chai lọ in chữ.
> - **An toàn thực phẩm (bắt buộc mọi tập):** README ghi rõ thời gian và dấu hiệu chín, dùng thớt/dao riêng cho đồ sống, mở nắp nồi nghiêng xa mặt, và nhắc chó mèo thật không ăn được hành, tỏi, tiêu, ớt, đồ mặn.
> - **Bối cảnh liền mạch:** cả 6 clip nối frame cuối mượt mà (`Seamless Frame Chaining`) ngay trong gian bếp (`KITCHEN`) hoặc di chuyển liền mạch sang góc bàn ăn (`DINING CORNER`).

---

## 1. Khóa nhân vật (Character Bible)

**Tên nhân vật trên Flow:** `@Pheo` · `@No`. Mỗi dòng khóa của nhân vật chính bắt đầu bằng `@Tên = …`, để Flow gọi đúng nhân vật đã lưu và model hiểu tên đó là nhân vật nào trong prompt.

**Quy tắc dùng khóa:**
- **FULL LOCK**: dán vào mọi Clip 1, và vào bất kỳ clip nào từ Clip 2 trở đi khi nhân vật **mới bước vào** (không có mặt ở clip ngay trước; thường là Hường ló vào bếp hoặc ở clip dọn ra ăn). Trong prompt, khối này nằm dưới nhãn `[CHARACTER ENTERING THIS SEGMENT]`.
- **SHORT LOCK**: dán vào mọi clip từ Clip 2 trở đi cho nhân vật **đã có mặt ở khung cuối clip trước**.
- Dán nguyên văn, không sửa chữ nào. Series này **không đổi trang phục** ở bất kỳ tập nào.
- Clip 2 trở đi làm bằng Save frame → Frames (hoặc Extend, xem FLOW_GUIDE mục 1): nếu Flow cho đính thêm ảnh ở chế độ này, đính ảnh tham chiếu ở mọi clip. Gemini Omni nhận nhiều ảnh tham chiếu hơn giới hạn 3 ảnh của Veo; nếu Flow vẫn giới hạn, ưu tiên nhân vật rồi tới sản phẩm.

### Phèo

Mèo đen mập ú đi hai chân, lông đen bóng, bụng tròn, mắt to màu hổ phách, ria trắng dài. **Dấu nhận diện: tai TRÁI có vết khuyết hình chữ V.** Mũ đầu bếp trắng cao đội lệch phải, áo thun trắng, tạp dề xanh navy có túi trước, khăn quàng cổ đỏ nhỏ.
Giọng đầu bếp Hà Nội trầm ấm, thanh thoát, dí dỏm. Tự tin, hài hước, tự hào tay nghề, nhưng tập nào cũng bị bà chủ làm cho đứng hình.

**FULL LOCK**

```text
@Pheo = PHÈO: an anthropomorphic chubby male black cat, adult, who stands and walks upright on two legs; the kitchen countertop reaches his waist. Glossy jet-black short fur, big round belly, round cheeks, big round amber-yellow eyes, small pink nose, long white whiskers, a tiny V-shaped notch on the tip of his LEFT ear (signature mark), thick black tail. Four-fingered black furry paw-hands with dark grey paw pads, barefoot. Outfit: tall white chef's toque tilted slightly to the right, white short-sleeve crew-neck t-shirt, navy-blue knee-length apron with one front pocket, small red neckerchief tied at the throat. Personality: confident, funny, proud of his cooking, easily stunned by his boss. Voice: deep, warm, strong and witty elegant Hà Nội Northern Vietnamese male chef voice, mid-30s.
```

**SHORT LOCK**

```text
@Pheo = PHÈO: chubby upright black cat, glossy jet-black fur, big amber-yellow eyes, notch on LEFT ear, long white whiskers, white chef's toque tilted right, white t-shirt, navy-blue apron, red neckerchief; deep, warm, witty elegant Hà Nội Northern Vietnamese male chef voice.
```

### Bà chủ Hường

Cô chó Pomeranian mập, lông xù màu kem cam, mặt tròn, mi cong dài, son hồng; thấp hơn Phèo một chút nhưng tròn hơn. Mặc đồ bộ lụa hồng in hoa nhỏ, đeo chuỗi ngọc trai, vòng vàng to ở hai tay, kính râm gọng đồi mồi gác trên đầu, mang dép lê hồng.
Giọng "bà chủ Hà Nội" ngọt ngào, đanh đá, thanh thoát. Giàu, dễ thương, mê ăn; ngọt ngào trong lời nói nhưng keo kiệt khoản tiền.

**FULL LOCK**

```text
@No = BÀ CHỦ HƯỜNG: an anthropomorphic chubby female Pomeranian dog, adult, who stands and walks upright on two legs; slightly shorter than Phèo but rounder. Very fluffy cream-orange fur with a lighter cream chest ruff, round face, small black button nose, big glossy dark-brown eyes with long curled eyelashes, pink lipstick, small upright fluffy ears, curled fluffy tail. Four-fingered fluffy paw-hands with soft pink paw pads. Outfit: pink silk Vietnamese pajama set (đồ bộ) with a small white-and-red flower print, short-sleeve button-up top and loose long trousers; a single-strand pearl necklace, chunky gold bracelets on both wrists, oversized tortoiseshell sunglasses pushed up on top of her head, pink house slippers. Personality: rich, cute, sassy, adores food, sweet with words but stingy with money. Voice: sweet, sassy elegant Hà Nội Northern Vietnamese rich-auntie female voice, around 40.
```

**SHORT LOCK**

```text
@No = BÀ CHỦ HƯỜNG: chubby upright cream-orange Pomeranian, very fluffy, long eyelashes, pink lipstick, pink floral silk pajama set, pearl necklace, gold bracelets, tortoiseshell sunglasses on her head; sweet, sassy elegant Hà Nội Northern Vietnamese rich-auntie voice.
```

---

## 2. Bối cảnh cố định

Cùng quy tắc với nhân vật: bối cảnh **có mặt ở clip trước** thì dùng SHORT; **vào khu vực mới trong clip** thì dùng FULL.

### Bếp (KITCHEN)

Bếp dựng như "phim trường nấu ăn": đảo bếp đá xám ở tiền cảnh, Phèo đứng sau đảo, mặt hướng vào máy. Bếp ga ở bên phải khung hình, cửa sổ có chậu rau thơm ở bên trái, cửa thông sang góc bàn ăn ở bên phải. Nắng vàng cuối buổi sáng chiếu từ bên trái.

**FULL**

```text
KITCHEN: a bright, modern Vietnamese home kitchen in a Saigon townhouse, laid out like a cozy cooking-show set. In the foreground a wide kitchen island with a light grey stone top, where Phèo works facing the camera: a thick round wooden cutting board in the middle and a two-burner gas stove built into the island on the right side of frame. Behind him: warm honey-colored wooden cabinets, a white-and-teal patterned cement-tile backsplash, a wide window on the left of frame with small terracotta pots of basil, mint and green onion on the sill, and an open doorway on the right of frame leading to the dining corner. Soft golden late-morning sunlight from the left window, warm cozy atmosphere, light steam haze in the air.
```

**SHORT**

```text
KITCHEN: same bright Saigon home kitchen, grey stone island with round wooden cutting board and gas stove on the right of frame, honey-wood cabinets, white-and-teal cement-tile backsplash, herb-pot window on the left, doorway to the dining corner on the right, golden late-morning light.
```

### Góc bàn ăn (DINING CORNER)

Ngay sau cửa bếp: bàn tròn gỗ tối, khăn ren trắng, nồi cơm điện. Ghế bành gỗ chạm đệm hồng của Hường (bên trái) đặt cạnh chiếc ghế nhựa đỏ thấp lè tè của Phèo (bên phải). Sự chênh lệch hai chiếc ghế là miếng hài hình ảnh cố định của series.

**FULL**

```text
DINING CORNER: the dining corner just through the doorway of the same kitchen, beside a tall window with sheer white curtains. A round dark-wood table with a white lace runner, a white electric rice cooker, blue-and-white ceramic rice bowls, wooden chopsticks and a glass pitcher of iced tea. Hường's big carved wooden armchair with a pink cushion on the left side of the table; Phèo's small red plastic stool on the right side. The same warm golden late-morning sunlight, softly filtered through the curtains.
```

**SHORT** (cho clip bàn ăn thứ hai, ví dụ Clip 10 khi Clip 9 đã ở bàn ăn)

```text
DINING CORNER: same round dark-wood table with white lace runner by the curtained window, rice cooker, blue-and-white bowls, Hường's carved armchair with pink cushion on the left, Phèo's small red plastic stool on the right, warm golden light.
```

---

## 3. Khóa phong cách

**[FORMAT]**: dán ở đầu mọi Clip 1.

```text
[FORMAT]
Vertical 9:16, 10-second clip, high-end 3D animated film, Pixar/Disney-quality stylized CGI, soft global illumination, shallow depth of field, 24fps, cinematic color grade. Bright, warm, appetizing food-film look: macro food close-ups, rising steam, sizzling oil, glossy sauces, crisp golden textures. Spoken dialogue in Vietnamese with a soft, clear, elegant standard Northern Vietnamese (Hà Nội) accent and accurate lip-sync; non-speaking characters keep their mouths closed. Spoken lines are written after a colon following the speaker; they are only spoken aloud, never shown as text. Cut only where the shot list says, and never flash or cut to an attached character reference turnaround sheet or plain grey studio backdrop at the start or end of the clip. No subtitles, no captions, no on-screen text, no logos, no watermark.
```

**Nhạc nền**: câu mở đầu mục `[SOUND]` của mọi clip.

```text
Background music: upbeat, playful acoustic guitar and light marimba kitchen tune, low volume under the dialogue.
```

**Câu mở đầu clip 2 trở đi** (làm bằng Frames với start frame = khung cuối clip trước, hoặc bằng Extend): hai dòng đầu tiên của mọi clip từ Clip 2 đến clip cuối, trừ clip mở bằng Ingredients.

```text
[FORMAT]
Continue the scene seamlessly from the final frame of the previous clip, which is the first frame of this clip. Same characters, same outfits, same location, same lighting and color grade. Flawless continuity, no time skip, no jump cut at the start.
Vertical 9:16, 10-second clip, same animation style. Spoken lines are written after a colon following the speaker; they are only spoken aloud in Vietnamese with a soft, clear, elegant Northern (Hà Nội) accent and accurate lip-sync, never shown as text. Cut only where the shot list says, and never flash or cut to a standalone character reference sheet at the start or end of the clip. No subtitles, no captions, no on-screen text.
```

**Câu cửa miệng**: từ Tập 24 mọi tập mở bằng Hường nói *"Em ơi, có biến!"* trong 2 giây đầu. Các tập cũ mở bằng *"Ngày [số tập], Phèo vô bếp!"*.

**Cú "đứng hình" (chữ ký của series)**: 2 giây cuối của mọi tập.

`SIGNATURE FREEZE` dùng cho tập hài:

```text
Phèo freezes completely mid-motion: eyes wide open as saucers with tiny pupils, whiskers stiff and straight, mouth slightly open, body perfectly still like a paused frame; only the tip of his notched LEFT ear twitches once. The camera performs a smooth, controlled slow push-in with natural easing into a medium close-up of his stunned face while subtle natural secondary motion continues in his breathing, quivering white whiskers, and twitching notched left ear (never a snap-zoom or lifeless statue freeze). The upbeat music pauses softly with a gentle comedic plucked bass note.
```

`TOUCHING FREEZE` dùng cho tập cảm động:

```text
Phèo freezes completely mid-motion: eyes wide open, whiskers stiff and straight, mouth slightly open, body perfectly still like a paused frame; only the tip of his notched LEFT ear twitches once. The camera slowly pushes into a medium close-up of his face and holds. His amber eyes well up with shining tears and a single tear rolls down his black cheek. The music softens into one gentle, warm piano chord.
```

**Bố cục cố định**: bếp ga luôn ở bên phải khung hình; ở bàn ăn, Hường ngồi bên trái, Phèo ngồi bên phải. Khung cuối của clip cuối luôn đứng yên 1 giây để làm thumbnail.

---

## 4. Ảnh tham chiếu nhân vật

Tạo bằng Nano Banana / Imagen trong Flow, chọn ảnh đẹp nhất rồi **dùng lại cho mọi tập**. Mỗi nhân vật cần 1 ảnh xoay 4 góc và 1 ảnh chân dung.

### Phèo · ảnh xoay 4 góc (`PHEO_ref_turnaround`)

```text
Character turnaround sheet for a 3D animated series. PHÈO: an anthropomorphic chubby male black cat, adult, standing upright on two legs. Glossy jet-black short fur, big round belly, round cheeks, big round amber-yellow eyes, small pink nose, long white whiskers, a tiny V-shaped notch on the tip of his LEFT ear, thick black tail. Four-fingered black furry paw-hands with dark grey paw pads, barefoot. Outfit: tall white chef's toque tilted slightly to the right, white short-sleeve crew-neck t-shirt, navy-blue knee-length apron with one front pocket, small red neckerchief tied at the throat. Four full-body views side by side at the same scale: front, three-quarter, side profile, back. Relaxed neutral standing pose, arms at his sides, friendly closed-mouth smile. Pixar/Disney-quality stylized 3D render, soft even studio lighting, plain light-grey seamless background. No text, no labels, no numbers, no watermark.
```

### Phèo · ảnh chân dung (`PHEO_ref_portrait`)

```text
Close-up portrait for a 3D animated series. PHÈO: an anthropomorphic chubby male black cat with glossy jet-black short fur, round cheeks, big round amber-yellow eyes, small pink nose, long white whiskers and a tiny V-shaped notch on the tip of his LEFT ear (clearly visible), wearing a tall white chef's toque tilted slightly to the right, a white short-sleeve t-shirt, a navy-blue apron and a small red neckerchief. Three-quarter view, chest up, warm confident smile. Pixar/Disney-quality stylized 3D render, soft studio lighting, plain light-grey background. No text, no labels, no watermark.
```

### Bà chủ Hường · ảnh xoay 4 góc (`HUONG_ref_turnaround`)

```text
Character turnaround sheet for a 3D animated series. BÀ CHỦ HƯỜNG: an anthropomorphic chubby female Pomeranian dog, adult, standing upright on two legs, round and plump. Very fluffy cream-orange fur with a lighter cream chest ruff, round face, small black button nose, big glossy dark-brown eyes with long curled eyelashes, pink lipstick, small upright fluffy ears, curled fluffy tail. Four-fingered fluffy paw-hands with soft pink paw pads. Outfit: pink silk Vietnamese pajama set with a small white-and-red flower print, short-sleeve button-up top and loose long trousers; a single-strand pearl necklace, chunky gold bracelets on both wrists, oversized tortoiseshell sunglasses pushed up on top of her head, pink house slippers. Four full-body views side by side at the same scale: front, three-quarter, side profile, back. Relaxed neutral standing pose, paws clasped in front, sweet closed-mouth smile. Pixar/Disney-quality stylized 3D render, soft even studio lighting, plain light-grey seamless background. No text, no labels, no numbers, no watermark.
```

### Bà chủ Hường · ảnh chân dung (`HUONG_ref_portrait`)

```text
Close-up portrait for a 3D animated series. BÀ CHỦ HƯỜNG: an anthropomorphic chubby female Pomeranian dog with very fluffy cream-orange fur, a round face, big glossy dark-brown eyes with long curled eyelashes, pink lipstick, a small black button nose and small upright fluffy ears, wearing a pink silk floral pajama top, a single-strand pearl necklace, chunky gold bracelets and oversized tortoiseshell sunglasses pushed up on top of her head. Three-quarter view, chest up, sweet sassy smile, one paw touching her cheek. Pixar/Disney-quality stylized 3D render, soft studio lighting, plain light-grey background. No text, no labels, no watermark.
```

**Kiểm tra trước khi chốt ảnh:**
- Phèo: tai **TRÁI** có vết khuyết, mũ lệch **phải**, khăn cổ đỏ, tay 4 ngón.
- Hường: kính râm **gác trên đầu** (không đeo trên mắt), chuỗi ngọc trai, vòng vàng ở cả hai tay, đồ bộ hồng in hoa.
- Không có chữ, nhãn hay số trên ảnh.

### Ảnh sản phẩm

- Chụp ảnh thật từng sản phẩm trên nền trắng hoặc xám trơn, ánh sáng đều, mặt trước hướng vào máy, **mỗi ảnh 1 sản phẩm**.
- Đặt tên: `SP_chao-chong-dinh`, `SP_noi-inox`, `SP_nuoc-mam`, `SP_dau-an`, `SP_hat-nem`.
- Model không viết đúng chữ trên nhãn, nên prompt để nhãn trống; tên sản phẩm thêm bằng giỏ hàng TikTok hoặc lồng tiếng.
- **Mỗi tập một sản phẩm chính** có ảnh tham chiếu, lên hình tối đa khoảng 9 giây, đính ảnh ở clip sản phẩm lên hình lần đầu; các chai lọ khác để nhãn trống, không đính ảnh, không gọi tên thương hiệu.

---

## 5. Danh sách tập

| Tập | Tên | Nội dung | Sản phẩm |
| --- | --- | --- | --- |
| 1 | Cá diêu hồng chiên giòn | Hường hứa tăng lương, cuối cùng chỉ thưởng thêm một chén cơm | Chảo chống dính |
| 2 | Thịt kho trứng nước dừa | Phèo tính chia đôi 6 quả trứng, Hường gắp sạch cả 6, để lại cho Phèo thịt với nước kho | Nước mắm |
| 3 | Gà chiên nước mắm · Quà 20/10 | Phèo tặng hoa và quà mong được thưởng tiền, nhận về một nụ hôn và thêm ca nấu tối | Dầu ăn |
| 4 | Canh chua cá lóc | Hường tuyên bố ăn kiêng, ngửi mùi canh xong thì "ăn kiêng từ mai" và đổi luôn tô cá của Phèo | Nồi inox, hạt nêm |
| 5 | Trứng chiên thịt bằm · Sinh nhật Phèo | Hường gọi món ruột của Phèo; hóa ra hôm nay là sinh nhật Phèo (tập cảm động) | Chảo chống dính |
| 6 | Sườn ram mặn ngọt · Hường livestream | Hường dặn nấu đẹp vì trưa lên live; Phèo tưởng sắp nổi tiếng, nhưng Hường khoe "chị nấu đó" rồi chốt đơn luôn cái chảo | Chảo chống dính |
| 7 | Chân gà sả tắc · Tai kích hoạt | ⚡ Trend "tai kích hoạt": Hường mải lướt điện thoại; Phèo nói "giòn sần sật" là tai bà chủ dựng đứng, nhắc "tăng lương" thì tai cụp, "chị nghe hông rõ", nhắc "chân gà còn nữa" thì tai bật dựng lại | Nước mắm |
| 8 | Cá kèo kho rau răm · Cá kèo hông? | Phèo ra kèo "ai khen ngon trước thì bao trà sữa"; Hường né chữ "ngon" ba lần (ngộ ghê, ngất ngây con gà tây, hết sẩy), Phèo tự hô "NGON!" rồi bị chốt "Mèo khen mèo dài đuôi! Bao trà sữa!" (tập 40s = 4 clip × 10s) | Nước mắm |
| 9 | Gà kho gừng · Thưởng nóng | Hường cảm lạnh, quấn mền ra kèo "Ăn hết lạnh, chị thưởng nóng!"; Phèo chọn gừng già, chần gà với gừng đập dập, ướp, thắng nước màu, kho lửa nhỏ hai lăm phút; Hường ló vô bếp ba lần (mũi nghẹt mà khen thơm, cầm sẵn chén đũa, "hết nghẹt mũi luôn"); ăn tới toát mồ hôi, hết lạnh, Hường "thưởng nóng" cho Phèo đúng nghĩa đen: trùm cái mền ấm lên đầu Phèo (tập 100s = 10 clip × 10s) | Hạt nêm |
| 10 | Tôm rim ba chỉ · Thưởng một cây | Hường lắc vòng vàng ra kèo "Rim tôm bóng đẹp, chị thưởng một cây!", Phèo tưởng một cây vàng; Phèo chọn tôm vỏ bóng đầu dính chặt, rút chỉ lưng, ướp nửa muỗng đường cho giòn trong, áp chảo ba chỉ năm phút chắt bớt mỡ, xào tôm lửa lớn ba phút, rim hai muỗng nước mắm một muỗng đường rồi xóc nhẹ chảo không gãy đầu tôm; cuối tập Hường giữ lời trao cho Phèo nguyên… một cây kem xoài vàng ươm (tập 100s = 10 clip × 10s) | Nước mắm |
| 11 | Mực nhồi thịt sốt cà chua · Thưởng một tờ bự nhứt | Hường phe phẩy xấp tiền ra kèo "Nhồi mực tròn căng không bục, chị thưởng một tờ bự nhứt!", Phèo tưởng tờ 500k; Phèo chia sẻ trọn bộ công thức mực ống nhồi thịt bằm nấm mèo bún tàu, mẹo nhồi 8 phần ghim tăm tre hấp sơ 7 phút trước khi sốt cà chua với hai muỗng nước mắm một muỗng đường; cuối tập Hường giữ lời trao tận tay Phèo… nguyên một tờ giấy nến nướng bánh khổ bự (tập 100s = 10 clip × 10s) | Nước mắm |
| 12 | Cánh gà chiên nước mắm · Thưởng một chiếc nhẫn | Hường khoe bàn tay đeo nhẫn lấp lánh ra kèo "Cánh gà giòn rụm thấm mắm, chị thưởng một chiếc nhẫn đeo liền!", Phèo tưởng nhẫn vàng; Phèo chia sẻ trọn bộ công thức sáu trăm gam cánh gà giữa thấm khô khía hai đường mặt dưới, ướp một muỗng nước mắm mười lăm phút, áo mỏng bột bắp chiên lửa vừa mười hai phút rồi đảo nhanh trên lửa lớn ba mươi giây với sốt hai muỗng nước mắm một muỗng rưỡi đường và tỏi phi giòn; cuối tập Hường mở hộp nhung đỏ đeo thẳng vào ngón tay Phèo… một vòng hành tây chiên giòn vàng ươm tròn xoe (tập 100s = 10 clip × 10s) | Nước mắm |
| 13 | Thịt ba chỉ quay giòn bì bằng chảo · Thưởng một chiếc xe | Hường đứng tựa khung cửa lắc chìa khóa ra kèo "Quay ba chỉ nổ bì bằng chảo, chị thưởng liền một chiếc xe!", Phèo tưởng xe máy/xe hơi mới; Phèo chia sẻ trọn bộ công thức sáu trăm gam thịt ba chỉ tươi vuông vắn luộc sơ mặt bì mười phút với gừng đập dập rồi thấm khô, xăm nĩa đều tay khắp mặt bì, ướp ngũ vị hương vào phần thịt nạc, quét hai muỗng giấm trắng phủ một muỗng muối hạt làm khô da rồi gạt bớt muối thừa, úp mặt bì vào chảo chống dính lửa vừa mười lăm phút cho nổ cốm vàng ruộm và lật chiên vàng các mặt thịt; cuối tập Hường giữ lời đặt lên bàn trao thưởng cho Phèo… một chiếc xe đồ chơi dây cót mini bằng nhựa màu đỏ chạy vòng vòng quanh đĩa thịt (tập 60s = 6 clip × 10s) | Chảo chống dính |
| 14 | Cá lăng nấu măng chua · Thưởng Tết sớm dày cộp | ⚡ Trend săn cá lăng gần 20kg hồ Trị An & công bố thưởng Tết sớm (03/11): Hường cầm bao lì xì đỏ dày cộp hứa trao "thưởng Tết sớm dày cộp" nếu Phèo nấu cá lăng măng chua không tanh; Phèo chà cá lăng bằng muối hạt và chanh, luộc sơ măng chua 3 phút khử chua gắt, áp sơ cá với dầu điều nước mắm rồi nấu lửa vừa 12 phút; cuối tập Hường rút từ bao đỏ ra tặng Phèo nguyên… lốc lịch giấy dày cộp để bóc đếm ngày tới Tết (tập 50s = 5 clip × 10s) | Hạt nêm |
| 15 | Vịt cỏ om sấu nước dừa · Chốt lịch nghỉ lễ 24/11 hưởng nguyên lương | ⚡ Trend lịch nghỉ lễ Ngày Văn hóa Việt Nam 24/11 hưởng nguyên lương (03/11): Hường khoe lịch nghỉ lễ cuối cùng trong năm 24/11, Phèo hỏi xoáy "nghỉ gộp 4 ngày hay mở bếp trả 300% lương theo luật lao động?"; Phèo áp chảo vịt cỏ ướp sả gừng trong nồi gang cho săn da vàng óng rồi om với nước dừa tươi, sấu xanh và khoai sọ 15 phút; mùi vịt om sấu thơm nức mũi làm Hường chốt cho Phèo nghỉ lễ hưởng nguyên lương (tập 50s = 5 clip × 10s) | Nồi gang / bếp |
| 16 | Cơm gà nồi cơm điện · Gas tăng, điện giảm, thưởng hai phần trăm | ⚡ Tập hài thời sự đầu tiên (04/11): xăng giảm, điện giảm 2% từ 1/11, gas tháng 11 tăng, lương tối thiểu vùng 2027 tăng. Hường hí hửng "cái gì cũng giảm", Phèo sợ bị giảm lương; Hường dang tay chắn bếp vì gas tăng, Phèo nấu nguyên bữa bằng nồi cơm điện (phi tỏi gừng trong lòng nồi, xào hai chén gạo, bớt nước, ủ thêm mười phút); Hường ngủ gục chờ nồi nhảy nút; ăn xong Phèo xin tăng lương theo lương tối thiểu, Hường "thưởng hai phần trăm nồi cơm" đúng một muỗng rồi ôm nguyên nồi đi mất (tập 60s = 6 clip, trọn trong bếp) | Không |
| 17 | Thịt ba rọi kho tiêu xanh nước mắm kẹo | Hường hứa thưởng máy massage đấm lưng, cuối tập thưởng cây đập lưng bằng tre | Nước mắm |
| 18 | Cá lóc đồng kho tộ miền Tây | Hường hứa thưởng chuyến du lịch miền Tây sông nước, cuối tập thưởng bức tranh lịch miền Tây | Nước mắm |
| 19 | Sườn non rim mặn ngọt mềm rục tróc xương | Hường hứa thưởng chuyến nghỉ dưỡng nghe sóng biển rì rào, cuối tập cho ngâm chân nước muối áp vỏ ốc vô tai | Dầu hào |
| 20 | Gà ta kho gừng sả ớt thấm đẫm mặn ngọt | Hường hứa thưởng chuyến du lịch suối nước nóng tắm khoáng thư giãn; Phèo chọn 800g gà ta da vàng săn chắc, chà muối hạt + gừng đập dập 2 phút rửa trong thau khử mùi lông, ướp tỷ lệ vàng 3-2-1 trong 20 phút, xào săn lửa đầu với gừng sả rồi châm 150ml nước dừa tươi rim lửa nhỏ 15 phút sánh kẹo và dậy hương gừng tươi 30 giây cuối; cuối tập Hường bê ra thau nhựa nước gừng muối ấm cho Phèo ngâm chân "suối nước nóng khoáng gừng tại bếp" (tập 60s = 6 clip × 10s) | Nước mắm |
| 21 | Thịt nạc rim nước dừa ngon như xá xíu | Hường hứa thưởng "một tháng lương" nếu thịt nạc rim không khô; Phèo chọn 750g nạc vai thái miếng dày rửa trong chậu để ráo, băm tỏi + hành khô, ướp 2 thìa nước mắm, 1 thìa xì dầu, 1 thìa tương ớt, 1 thìa đường, ½ thìa hạt nêm, ½ thìa tiêu, 2 thìa dầu ít nhất 30 phút, áp chảo mỗi mặt 1 phút, rim 330ml nước dừa lửa liu riu 45 phút (10 phút lật một lần) rồi rim lửa to đến khi sốt sánh bóng tách dầu; cuối tập Hường bưng ra năm thanh "lương khô" buộc nơ — "một tháng lương… khô" (tập 60s = 6 clip × 10s, giọng Bắc thanh thoát) | Nước mắm |
| 22 | Đậu phụ nhồi thịt sốt cà chua · Thưởng "đi quẩy" | Hường hứa "không vỡ miếng nào thì tối nay chị cho em đi quẩy"; Phèo trộn 150 g thịt vai xay với mộc nhĩ, nấm hương, hành khô, hành lá, nêm 1 thìa cà phê nước mắm, ½ muối, ½ hạt nêm, ½ tiêu; chọn đậu trắng ngà, 5 bìa cắt đôi, khoét giữa chừa đáy 1 cm, nhồi vừa đầy miết nhẹ; dầu nóng lửa vừa, úp mặt thịt xuống trước, vàng chắc mới lật; phi hành khô, 4 quả cà chua bóc vỏ băm nhỏ, 2 thìa cà phê nước mắm, ½ muối, thả đậu vào sốt, om nhỏ lửa 10 phút, rắc hành; giữa tập Hường nhắc "vỡ một miếng là mất quẩy"; cuối tập Hường giữ lời giơ bó năm chiếc quẩy rán buộc nơ đỏ: "em tha hồ quẩy", Phèo đứng hình "đi quẩy thành ăn quẩy" (tập 60s = 6 clip × 10s, giọng Bắc thanh thoát; công thức theo VnExpress) | Nước mắm |
| 23 | Bò xào súp lơ xanh · Thưởng "áo phao" | Hường xoa tay than rét, hứa "bò mà mềm thì chị sắm cho em cái áo phao"; Phèo chọn 400 g thăn bò đỏ tươi, thái mỏng ngang thớ, ướp 1 thìa canh dầu hào, 1 thìa cà phê đường, 1 hạt nêm, ½ tiêu, nửa phần tỏi băm 15 phút; súp lơ bông xanh đậm nụ khít ngâm nước muối loãng 10 phút, chần 30 giây, thả nước đá; chảo thật nóng lửa to 1 thìa canh dầu, đảo bò 1 phút vừa săn thì tắt bếp trút ra; thêm 1 thìa canh dầu phi tỏi còn lại, xào súp lơ với 1 thìa cà phê đường, 1 hạt nêm, chút nước, lửa to 2 phút; trút bò đảo nhanh, tắt bếp, rắc tiêu; giữa tập Hường nhắc "bò mà dai là mất áo phao"; cuối tập Hường giữ lời giơ chiếc áo phao cứu sinh màu cam: "Áo phao đây, em mặc cho ấm nhé!", Phèo đứng hình "áo phao đi bơi à?!" (tập 60s = 6 clip × 10s, giọng Bắc thanh thoát; công thức theo Điện máy Xanh, mẹo chần và xào theo VnExpress) | Dầu hào |
| 24 | Có biến ngày 11/11 · Quà Lễ độc thân "một chiếc đũa" | ⚡ Tập đầu của format "Có biến!" (bàn drama của ngày, 11/11/2026): Hường hớn hở sale ngày đôi, Phèo "Lễ độc thân mà chị sắm như sắm đồ cưới"; vàng thế giới tụt mạnh, Hường ôm vòng vàng, Phèo "lương em đứng im cả năm"; mạng xã hội dùng AI đoán tuổi, Hường khai mười tám, Phèo dọa bị giới hạn giờ lướt; U23 Việt Nam thắng U23 Thái Lan ba không, Hường "nấu xong sớm thì cho xem ké"; vụ "mua hàng không đồng" rồi "luật sư mạng", Hường lén giấu điện thoại; cuối tập Hường tặng quà Lễ độc thân: một chiếc đũa lẻ, Phèo đứng hình "Đũa cũng độc thân à?!" (tập 60s = 6 clip × 10s, giọng Bắc thanh thoát, góc bàn ăn) | Không |
| 25 | Có biến ngày 13/11 · Quà Ngày Thế giới Tử tế "cả tấm lòng" | ⚡ Tập "Có biến!" thứ hai (tin quét chiều 12/11/2026, đăng 13/11, không dùng chung tin với Tây Du Ký tập 25): Hường mở màn "có biến" chuyện bên Trung Quốc có người đấu giá được căn hộ giá bằng bát phở, Phèo xin thưởng một bát phở để mua nhà, Hường lặng lẽ đẩy đĩa hạt hướng dương sang; hiệu trưởng, hiệu phó phải nói được tiếng Anh, Hường cầm chén trà kiểu sang "chị cũng học đây", Phèo dạy "raise my salary, please!", Hường nhún vai giả không hiểu; ngân hàng Anh, Mỹ chặn trợ lý AI tự vào tài khoản, Phèo xin làm trợ lý "chỉ lo đúng một việc: duyệt lương em", Hường ôm chặt điện thoại; bóng bàn nam Việt Nam vô địch Đông Nam Á, Hường che ấm trà "đập bóng vào là trừ lương"; giải nhạc Hàn sắp về Hà Nội, Phèo đòi tính tăng ca hai đêm trông nhà, Hường giả điếc; cuối tập Ngày Thế giới Tử tế, Hường tặng "cả tấm lòng": một bát lòng lợn luộc, Phèo đứng hình "Cả tấm lòng... là lòng lợn à?!" (tập 60s = 6 clip × 10s, giọng Bắc thanh thoát, góc bàn ăn) | Không |

---

## 6. Các tập — mỗi ngày 1 tập

Mỗi tập mới **dao động từ 30–60s = 3–6 clip × 10s (tối đa 60 giây)** là một ngày đăng, nằm trong thư mục riêng `tap-{số}/` cùng thư mục này: `README.md` là tổng quan tập (kèm công thức đã tra cứu Google Search), `clip-1.md` … `clip-N.md` (3–6 file) là prompt của từng clip 10 giây. Các tập 1–12 đã viết trước đây giữ nguyên file cũ; tập mới đánh số tiếp và dùng nguyên các khóa ở mục 1–3.

| Ngày | File | Tên tập |
| --- | --- | --- |
| 1 | [tap-1/](tap-1/README.md) | Cá diêu hồng chiên giòn |
| 2 | [tap-2/](tap-2/README.md) | Thịt kho trứng nước dừa |
| 3 | [tap-3/](tap-3/README.md) | Gà chiên nước mắm · Quà 20/10 |
| 4 | [tap-4/](tap-4/README.md) | Canh chua cá lóc |
| 5 | [tap-5/](tap-5/README.md) | Trứng chiên thịt bằm · Sinh nhật Phèo |
| 6 | [tap-6/](tap-6/README.md) | Sườn ram mặn ngọt · Hường livestream |
| 7 | [tap-7/](tap-7/README.md) | Chân gà sả tắc · Tai kích hoạt |
| 8 | [tap-8/](tap-8/README.md) | Cá kèo kho rau răm · Cá kèo hông? |
| 9 | [tap-9/](tap-9/README.md) | Gà kho gừng · Thưởng nóng |
| 10 | [tap-10/](tap-10/README.md) | Tôm rim ba chỉ · Thưởng một cây |
| 11 | [tap-11/](tap-11/README.md) | Mực nhồi thịt sốt cà chua · Thưởng một tờ bự nhứt |
| 12 | [tap-12/](tap-12/README.md) | Cánh gà chiên nước mắm · Thưởng một chiếc nhẫn |
| 13 | [tap-13/](tap-13/README.md) | Thịt ba chỉ quay giòn bì bằng chảo · Thưởng một chiếc xe |
| 14 | [tap-14/](tap-14/README.md) | Cá lăng nấu măng chua · Thưởng Tết sớm dày cộp |
| 15 | [tap-15/](tap-15/README.md) | Vịt cỏ om sấu nước dừa · Chốt lịch nghỉ lễ 24/11 hưởng nguyên lương |
| 16 | [tap-16/](tap-16/README.md) | Cơm gà nồi cơm điện · Gas tăng, điện giảm, thưởng hai phần trăm |
| 17 | [tap-17/](tap-17/README.md) | Thịt ba rọi kho tiêu nước mắm kẹo · Bà chủ dọa dùng AI đi chợ hộ, Phèo đòi lãnh trợ cấp thất nghiệp |
| 18 | [tap-18/](tap-18/README.md) | Cá lóc đồng kho tộ miền Tây thịt săn chắc không tanh · Thưởng chuyến du lịch miền Tây trên lịch |
| 19 | [tap-19/](tap-19/README.md) | Sườn non rim mặn ngọt mềm rục tróc xương · Thưởng chuyến đi biển ngâm chân nước muối áp vỏ ốc |
| 20 | [tap-20/](tap-20/README.md) | Gà ta kho gừng sả ớt thấm đẫm mặn ngọt · Thưởng chuyến suối nước nóng khoáng gừng ngâm chân tại bếp |
| 21 | [tap-21/](tap-21/README.md) | Thịt nạc rim nước dừa ngon như xá xíu · Thưởng "một tháng lương… khô" |
| 22 | [tap-22/](tap-22/README.md) | Đậu phụ nhồi thịt sốt cà chua · Thưởng "đi quẩy"… một bó quẩy |
| 23 | [tap-23/](tap-23/README.md) | Bò xào súp lơ xanh · Thưởng "áo phao"… áo phao cứu sinh |
| 24 | [tap-24/](tap-24/README.md) | Có biến ngày 11/11 · Quà Lễ độc thân "một chiếc đũa" |
| 25 | [tap-25/](tap-25/README.md) | Có biến ngày 13/11 · Quà Ngày Thế giới Tử tế "cả tấm lòng" |

## Tập 14 (`tap-14`)

### Clip 1 (`tap-14/clip-1.md`)

```text
[FORMAT]
Vertical 9:16, 10-second clip, high-end cinematic 3D food animation, Pixar/Disney-quality stylized CGI, 24fps, natural soft global illumination, physically accurate material shaders, shallow depth of field, controlled specular highlights, cinematic color grade. Characters have detailed soft fur and rich facial expressions, animated with natural anticipation, smooth easing, follow-through, believable weight transfer, and subtle secondary motion in ears, tail, whiskers, fur, clothing, and accessories—never robotic, jittery, foot-sliding, or deformed. Authentic Vietnamese culinary realism: realistic raw and cooked food textures (distinct skin, fat, and lean layers on meat; natural surface moisture on raw ingredients without plastic shine; physically accurate browning, shrinkage, sizzling, and rising steam only when heat is applied). Ultra-smooth camera work using slow dolly, gentle push-in, controlled pan, and smooth lateral tracking with natural acceleration and deceleration (no snap zooms, no whip pans, no camera teleports). Spoken dialogue in Vietnamese with a soft, clear, elegant standard Northern Vietnamese (Hà Nội) accent and accurate lip-sync when the speaker's face is clearly visible; non-speaking characters keep their mouths closed. Spoken lines are written after a colon following the speaker; they are only spoken aloud, never shown as text. Never flash or cut to an attached character reference sheet or studio backdrop. No subtitles, no captions, no on-screen text, no logos, no watermark.

[CHARACTERS — match the attached reference images @Pheo @No 100% exactly]
@Pheo = PHÈO (100% exact match to @Pheo reference image): an anthropomorphic chubby adult male black cat standing and walking upright on two legs; the kitchen countertop reaches his waist. Detailed velvety jet-black short fur with a small white chest locket patch, big round belly, round cheeks, big expressive amber-yellow eyes, small pink nose, long white whiskers, a distinct V-shaped notch on the tip of his LEFT ear (signature mark), thick black tail. Four-fingered black furry paw-hands with soft paw pads, barefoot. Outfit: tall white chef's toque tilted slightly to the right, crisp white short-sleeve crew-neck t-shirt, navy-blue knee-length kitchen apron with one front pocket, small red neckerchief tied neatly at the throat. Personality: confident, witty, proud of his culinary craft, easily left stunned by his boss's stingy twists. Voice: deep, warm, confident, humorous elegant Hà Nội Northern Vietnamese male chef voice, mid-30s.
@No = BÀ CHỦ HƯỜNG (100% exact match to @No reference image): an anthropomorphic chubby adult female Pomeranian dog standing and walking upright on two legs; slightly shorter than Phèo but rounder. Very fluffy cream-orange fur with a lighter cream chest ruff, round pampered face, small black button nose, big glossy dark-brown eyes with long curled eyelashes, pink lipstick, small upright fluffy Pomeranian ears, curled fluffy tail. Four-fingered fluffy cream-orange paw-hands with soft pink paw pads. Outfit: glossy lotus-pink silk Vietnamese pajama set (đồ bộ lụa hồng) with a delicate floral print, short-sleeve button-up top and loose long trousers; a single-strand white pearl necklace, chunky gold bracelets on both wrists, oversized tortoiseshell sunglasses pushed up on top of her head, pink indoor slippers. Personality: wealthy, cute, sassy, adores delicious food, sweet-talking yet stingy with money. Voice: sweet, sassy, rich-auntie elegant Hà Nội Northern Vietnamese female voice, around 40.

[SETTING]
KITCHEN: a bright, cozy Vietnamese home kitchen in a Saigon townhouse, laid out with strict spatial continuity like a culinary show set. In the foreground stands a wide kitchen island with a matte light-grey stone countertop where Phèo works facing the camera: a thick round wooden cutting board rests in the center, and a built-in two-burner gas stove sits on the right side of the island. Behind him: warm honey-colored wooden cabinets, a white-and-teal patterned cement-tile backsplash (gạch bông trắng xanh), a wide sunlit window on the left with small terracotta pots of Thai basil, mint, and green onions on the sill, and an open doorway on the right leading to the dining corner. Soft golden late-morning sunlight slants in from the left window.
Props on the grey stone island: in the center on a fresh green banana leaf beside the round wooden cutting board lie three thick, plump steaks of fresh river hemibagrus catfish (cá lăng tươi, 600g) with smooth silver-grey skin and firm pinkish-white flesh with natural moisture; to the left sit a white porcelain bowl of shredded pickled bamboo shoots (măng chua), red tomato wedges, a halved fresh green lime, coarse sea salt, and culantro/rice paddy herb (ngò gai, rau ngổ); on the unlit right gas stove sits a glossy terracotta clay pot (burner OFF, no smoke or steam).

[SHOT LIST]
00:00–00:03.5 | Medium shot at island level, smooth slow push-in with natural easing — @Pheo stands behind the grey stone island, sets down his woven rattan market basket and spreads open the green banana leaf to reveal the three thick, firm steaks of fresh river catfish (cá lăng) with natural surface moisture. @Pheo says (deep, warm elegant Hà Nội Northern Vietnamese chef voice, excited): Ngày mười bốn, Phèo vô bếp! Nay săn được cá lăng tươi rói nấu măng chua!
00:03.5–00:07 | Controlled pan right to a medium two-shot — @No (Bà Chủ Hường) leans through the open doorway on the right, holding up a thick, plump plain red lucky envelope (bao lì xì đỏ dày cộp, no text) in her right four-fingered fluffy paw, gold bracelets clinking as she winks slyly while @Pheo keeps his mouth closed. @No says (sweet, sassy elegant Hà Nội Northern Vietnamese auntie voice, tempting): Nấu cá lăng măng chua đỉnh, chị trao thưởng Tết sớm dày cộp luôn!
00:07–00:10 | Smooth pan back to a medium close-up on @Pheo — @No steps back out through the right doorway; @Pheo's amber-yellow eyes widen with joy, the V-shaped notch on his left ear twitches, and his right four-fingered black furry paw picks up the halved fresh lime and a pinch of coarse salt. @Pheo says (deep, warm elegant Hà Nội Northern Vietnamese chef voice, thrilled): Thưởng Tết sớm dày cộp hả? Sáu trăm gam cá lăng tới công chuyện liền!

[SOUND]
Background music: upbeat, playful acoustic guitar and light marimba kitchen tune, mixed gently under the dialogue.
Foley: crisp rustle of banana leaf, soft jingle of gold bracelets, paper rustle of the thick red envelope, cheerful kitchen chime.

[END FRAME]
Medium close-up of @Pheo behind the grey stone island in golden late-morning sunlight: holding half a fresh green lime in his right four-fingered black furry paw above the three fresh river catfish steaks on the banana leaf, his amber eyes gleaming and white whiskers twitching subtly while the unlit clay pot sits on the right stove.

[AVOID]
humans, human faces, human hands, extra fingers or fewer than four fingers per paw, robotic or jittery animation, foot sliding, body or muzzle deformation, non-speaking character moving mouth, smoke or boiling oil when stove burner is off, raw meat turning cooked instantly without heat, raw meat touching cooked food or fresh herbs, plastic or toy-like glossy food, utensils or ingredients appearing/disappearing or clipping through paws, reversed kitchen layout, snap zooms, whip pans, camera teleports, frozen statue end frames, newspaper wrapping, printed bags, price tags, receipts, scale displays, measuring marks, labeled jars or bottles, readable text, numbers, subtitles, logos, watermarks.
```

### Clip 2 (`tap-14/clip-2.md`)

```text
[FORMAT]
Continue the scene seamlessly from the final frame of the previous clip, which is the first frame of this clip. Same characters, exact same outfits and proportions, same kitchen/dining layout, same props and ingredient counts in their exact positions, same lighting and color grade. Flawless physical continuity, no time skip, no jump cut at the start.
Vertical 9:16, 10-second clip, high-end cinematic 3D food animation, 24fps, soft global illumination, macro food realism with controlled highlights and shallow depth of field. Smooth character animation with anticipation, natural easing, follow-through, weight transfer, and subtle secondary motion in ears, whiskers, tail, fur, and clothing. Ultra-smooth camera movement (slow dolly, gentle push-in, controlled pan; no snap zooms, no whip pans, no camera teleports). Spoken lines are written after a colon following the speaker; they are only spoken aloud in Vietnamese with a soft, clear, elegant Northern (Hà Nội) accent and accurate lip-sync, never shown as text; non-speaking characters keep their mouths closed. Never flash or cut to a standalone character reference sheet. No subtitles, no captions, no on-screen text.

[CHARACTERS — unchanged]
@Pheo = PHÈO (exact match to @Pheo reference): chubby upright bipedal black cat, velvety jet-black fur, amber-yellow eyes, V-shaped notch on LEFT ear, long white whiskers, four-fingered black furry paw-hands, white chef's toque tilted right, white t-shirt, navy-blue apron, red neckerchief; deep, warm, witty elegant Hà Nội Northern Vietnamese male chef voice.

[SETTING — unchanged]
KITCHEN: same bright Saigon home kitchen with strict spatial continuity—matte light-grey stone island in the foreground with the round wooden cutting board in the center and the two-burner gas stove on the right, honey-colored wood cabinets and white-and-teal cement-tile backsplash behind, herb-pot window on the left, open doorway to the dining corner on the right, warm golden late-morning sunlight from the left.
Props: three fresh river catfish steaks in a clean porcelain bowl, coarse salt, fresh lime, white paper towels, shredded pickled bamboo shoots in a colander, and a small pot of simmering water on the right stove.

[SHOT LIST]
00:00–00:05 | High-angle close-up on the grey stone island, gentle push-in — continuing seamlessly, @Pheo squeezes fresh lime juice and sprinkles coarse sea salt over the three river catfish steaks, rubbing the smooth silver-grey skin gently with his four-fingered black furry paws to remove natural slime, then rinses them in a bowl of clean water and pats every steak dry with a thick white paper towel. @Pheo says (deep, warm elegant Hà Nội Northern Vietnamese chef voice, sharing a culinary tip): Cá lăng chà muối với chanh rồi thấm khô, sạch nhớt mà thơm phức!
00:05–00:10 | Smooth lateral tracking shot rightward to the gas stove — on the lit right burner with a steady medium blue flame, @Pheo uses wooden chopsticks in his right four-fingered black furry paw to blanch the shredded yellow pickled bamboo shoots (măng chua) in boiling water for three minutes (indicated by a clean kitchen-timer chime, sound only), then lifts them out into a clean white bowl, steam rising naturally. @Pheo says (deep, warm elegant Hà Nội Northern Vietnamese chef voice, clear): Ba trăm gam măng chua luộc sơ ba phút cho hết vị chua gắt!

[SOUND]
Background music: upbeat, playful acoustic guitar and light marimba kitchen tune, mixed gently under the dialogue.
Foley: citrus squeeze, gentle rubbing on fish skin, patting of paper towel, gentle bubbling of boiling water, a single ding of a kitchen timer.

[END FRAME]
Medium close-up at the right stove: @Pheo holding wooden chopsticks in his right four-fingered black furry paw lifting steamed golden pickled bamboo shoots into a clean porcelain bowl, gentle steam rising and @Pheo's notched left ear and whiskers moving naturally.

[AVOID]
humans, human faces, human hands, extra fingers or fewer than four fingers per paw, robotic or jittery animation, foot sliding, body or muzzle deformation, non-speaking character moving mouth, smoke or boiling oil when stove burner is off, raw meat turning cooked instantly without heat, raw meat touching cooked food or fresh herbs, plastic or toy-like glossy food, utensils or ingredients appearing/disappearing or clipping through paws, reversed kitchen layout, snap zooms, whip pans, camera teleports, frozen statue end frames, newspaper wrapping, printed bags, price tags, receipts, scale displays, measuring marks, labeled jars or bottles, readable text, numbers, subtitles, logos, watermarks.
```

### Clip 3 (`tap-14/clip-3.md`)

```text
[FORMAT]
Vertical 9:16, 10-second clip, high-end cinematic 3D food animation, Pixar/Disney-quality stylized CGI, 24fps, natural soft global illumination, physically accurate material shaders, shallow depth of field, controlled specular highlights, cinematic color grade. Characters have detailed soft fur and rich facial expressions, animated with natural anticipation, smooth easing, follow-through, believable weight transfer, and subtle secondary motion in ears, tail, whiskers, fur, clothing, and accessories—never robotic, jittery, foot-sliding, or deformed. Authentic Vietnamese culinary realism: realistic raw and cooked food textures (distinct skin, fat, and lean layers on meat; natural surface moisture on raw ingredients without plastic shine; physically accurate browning, shrinkage, sizzling, and rising steam only when heat is applied). Ultra-smooth camera work using slow dolly, gentle push-in, controlled pan, and smooth lateral tracking with natural acceleration and deceleration (no snap zooms, no whip pans, no camera teleports). Spoken dialogue in Vietnamese with a soft, clear, elegant standard Northern Vietnamese (Hà Nội) accent and accurate lip-sync when the speaker's face is clearly visible; non-speaking characters keep their mouths closed. Spoken lines are written after a colon following the speaker; they are only spoken aloud, never shown as text. Never flash or cut to an attached character reference sheet or studio backdrop. No subtitles, no captions, no on-screen text, no logos, no watermark.

[CHARACTERS — match the attached reference images @Pheo @No 100% exactly]
@Pheo = PHÈO (100% exact match to @Pheo reference image): an anthropomorphic chubby adult male black cat standing and walking upright on two legs; the kitchen countertop reaches his waist. Detailed velvety jet-black short fur with a small white chest locket patch, big round belly, round cheeks, big expressive amber-yellow eyes, small pink nose, long white whiskers, a distinct V-shaped notch on the tip of his LEFT ear (signature mark), thick black tail. Four-fingered black furry paw-hands with soft paw pads, barefoot. Outfit: tall white chef's toque tilted slightly to the right, crisp white short-sleeve crew-neck t-shirt, navy-blue knee-length kitchen apron with one front pocket, small red neckerchief tied neatly at the throat. Personality: confident, witty, proud of his culinary craft, easily left stunned by his boss's stingy twists. Voice: deep, warm, confident, humorous elegant Hà Nội Northern Vietnamese male chef voice, mid-30s.
@No = BÀ CHỦ HƯỜNG (100% exact match to @No reference image): an anthropomorphic chubby adult female Pomeranian dog standing and walking upright on two legs; slightly shorter than Phèo but rounder. Very fluffy cream-orange fur with a lighter cream chest ruff, round pampered face, small black button nose, big glossy dark-brown eyes with long curled eyelashes, pink lipstick, small upright fluffy Pomeranian ears, curled fluffy tail. Four-fingered fluffy cream-orange paw-hands with soft pink paw pads. Outfit: glossy lotus-pink silk Vietnamese pajama set (đồ bộ lụa hồng) with a delicate floral print, short-sleeve button-up top and loose long trousers; a single-strand white pearl necklace, chunky gold bracelets on both wrists, oversized tortoiseshell sunglasses pushed up on top of her head, pink indoor slippers. Personality: wealthy, cute, sassy, adores delicious food, sweet-talking yet stingy with money. Voice: sweet, sassy, rich-auntie elegant Hà Nội Northern Vietnamese female voice, around 40.

[SETTING]
KITCHEN: a bright, cozy Vietnamese home kitchen in a Saigon townhouse, laid out with strict spatial continuity like a culinary show set. In the foreground stands a wide kitchen island with a matte light-grey stone countertop where Phèo works facing the camera: a thick round wooden cutting board rests in the center, and a built-in two-burner gas stove sits on the right side of the island. Behind him: warm honey-colored wooden cabinets, a white-and-teal patterned cement-tile backsplash (gạch bông trắng xanh), a wide sunlit window on the left with small terracotta pots of Thai basil, mint, and green onions on the sill, and an open doorway on the right leading to the dining corner. Soft golden late-morning sunlight slants in from the left window.
Props on the island and right stove: the terracotta clay pot sits on the lit right gas burner over a steady blue flame; beside the stove sit the plate of cleaned, patted-dry river catfish steaks, the bowl of blanched pickled bamboo shoots, tomato wedges, fish sauce, and a small blank-labeled jar of seasoning granules (`SP_hat-nem`, matching the attached product reference image).

[SHOT LIST]
00:00–00:04.5 | Close-up on the terracotta clay pot on the right gas stove, slow push-in — golden annatto oil shimmers over the lit burner as minced garlic and shallots sizzle fragrantly; @Pheo uses wooden chopsticks in his right four-fingered black furry paw to lay the three thick river catfish steaks gently into the pot, searing both sides lightly with a spoonful of amber fish sauce until the skin firms up and turns a delicate golden-ivory. @Pheo says (deep, warm elegant Hà Nội Northern Vietnamese chef voice, confident): Phi hành tỏi dầu điều, áp sơ cá lăng với nước mắm cho thịt săn chắc!
00:04.5–00:07.5 | Medium shot at the island, controlled pan — @Pheo pours boiling water from a kettle into the clay pot along with the blanched pickled bamboo shoots and red tomato wedges, bringing the broth to a gentle, clear golden-orange simmer with rising steam. @Pheo says (deep, warm elegant Hà Nội Northern Vietnamese chef voice, enthusiastic): Trút măng chua với nước sôi vô, nấu lửa vừa mười hai phút!
00:07.5–00:10 | Medium two-shot toward the right doorway, static — @No (Bà Chủ Hường) peeks in through the right doorway sniffing the fragrant steam and shaking the thick red lucky envelope playfully while @Pheo smiles with his mouth closed. @No says (sweet, sassy elegant Hà Nội Northern Vietnamese auntie voice, reminding): Canh mà tanh là bao thưởng Tết sớm bay mất tiêu nghen Phèo!

[SOUND]
Background music: upbeat, playful acoustic guitar and light marimba kitchen tune, mixed gently under the dialogue.
Foley: fragrant sizzle of garlic and shallots in oil, gentle pour of hot water, soft bubbling of soup in the clay pot, light rustle of the red envelope.

[END FRAME]
Medium shot at the right stove: @Pheo standing by the gently bubbling terracotta pot of golden-orange river catfish and bamboo shoot soup while @No smiles in the right doorway holding the thick red envelope; camera stabilizes smoothly with natural rising steam and subtle breathing motion.

[AVOID]
humans, human faces, human hands, extra fingers or fewer than four fingers per paw, robotic or jittery animation, foot sliding, body or muzzle deformation, non-speaking character moving mouth, smoke or boiling oil when stove burner is off, raw meat turning cooked instantly without heat, raw meat touching cooked food or fresh herbs, plastic or toy-like glossy food, utensils or ingredients appearing/disappearing or clipping through paws, reversed kitchen layout, snap zooms, whip pans, camera teleports, frozen statue end frames, newspaper wrapping, printed bags, price tags, receipts, scale displays, measuring marks, labeled jars or bottles, readable text, numbers, subtitles, logos, watermarks.
```

### Clip 4 (`tap-14/clip-4.md`)

```text
[FORMAT]
Continue the scene seamlessly from the final frame of the previous clip, which is the first frame of this clip. Same characters, exact same outfits and proportions, same kitchen/dining layout, same props and ingredient counts in their exact positions, same lighting and color grade. Flawless physical continuity, no time skip, no jump cut at the start.
Vertical 9:16, 10-second clip, high-end cinematic 3D food animation, 24fps, soft global illumination, macro food realism with controlled highlights and shallow depth of field. Smooth character animation with anticipation, natural easing, follow-through, weight transfer, and subtle secondary motion in ears, whiskers, tail, fur, and clothing. Ultra-smooth camera movement (slow dolly, gentle push-in, controlled pan; no snap zooms, no whip pans, no camera teleports). Spoken lines are written after a colon following the speaker; they are only spoken aloud in Vietnamese with a soft, clear, elegant Northern (Hà Nội) accent and accurate lip-sync, never shown as text; non-speaking characters keep their mouths closed. Never flash or cut to a standalone character reference sheet. No subtitles, no captions, no on-screen text.

[CHARACTERS — unchanged]
@Pheo = PHÈO (exact match to @Pheo reference): chubby upright bipedal black cat, velvety jet-black fur, amber-yellow eyes, V-shaped notch on LEFT ear, long white whiskers, four-fingered black furry paw-hands, white chef's toque tilted right, white t-shirt, navy-blue apron, red neckerchief; deep, warm, witty elegant Hà Nội Northern Vietnamese male chef voice.

[SETTING — unchanged]
KITCHEN: same bright Saigon home kitchen with strict spatial continuity—matte light-grey stone island in the foreground with the round wooden cutting board in the center and the two-burner gas stove on the right, honey-colored wood cabinets and white-and-teal cement-tile backsplash behind, herb-pot window on the left, open doorway to the dining corner on the right, warm golden late-morning sunlight from the left.
Props: the bubbling terracotta clay pot of cá lăng măng chua on the right stove, the blank-labeled jar of seasoning granules (`SP_hat-nem`, matching the product reference), a small porcelain bowl of chopped culantro and rice paddy herb (ngò gai, rau ngổ) and sliced red chili, and a clean soup ladle.

[SHOT LIST]
00:00–00:04.5 | Macro close-up at the right stove, smooth push-in — after a brief kitchen-timer chime (sound only) marking twelve minutes of simmering, the river catfish steaks are fully cooked, flaky, and snow-white inside the clear, shimmering golden-orange bamboo shoot broth; @Pheo holds the blank-labeled jar of seasoning granules (`SP_hat-nem`) in his left four-fingered black furry paw and scoops one neat spoonful with his right paw into the simmering pot. @Pheo says (deep, warm elegant Hà Nội Northern Vietnamese chef voice, proud): Mười hai phút cá chín mềm ngọt, nêm một muỗng hạt nêm cho vị thanh đậm đà!
00:04.5–00:10 | Medium close-up at the stove, gentle pull-back — @Pheo turns the gas burner knob OFF (the blue flame extinguishes completely), sprinkles fresh green chopped culantro, rice paddy herb, and red chili slices over the steaming clay pot, then uses two thick cloth pot-holders with his four-fingered paws to lift the steaming terracotta pot toward the right doorway. @Pheo says (deep, warm elegant Hà Nội Northern Vietnamese chef voice, joyful): Tắt bếp rắc ngò gai thơm lừng, bưng ra nhận thưởng Tết sớm thôi!

[SOUND]
Background music: upbeat, playful acoustic guitar and light marimba kitchen tune, mixed gently under the dialogue.
Foley: single kitchen timer ding, soft sprinkle of seasoning granules, click of gas burner turning off, gentle clatter of clay pot lifted with cloth pot-holders.

[END FRAME]
Medium shot of @Pheo turning toward the right doorway holding the steaming terracotta clay pot of cá lăng nấu măng chua with two cloth pot-holders, fragrant steam rising and his notched left ear twitching with anticipation.

[AVOID]
humans, human faces, human hands, extra fingers or fewer than four fingers per paw, robotic or jittery animation, foot sliding, body or muzzle deformation, non-speaking character moving mouth, smoke or boiling oil when stove burner is off, raw meat turning cooked instantly without heat, raw meat touching cooked food or fresh herbs, plastic or toy-like glossy food, utensils or ingredients appearing/disappearing or clipping through paws, reversed kitchen layout, snap zooms, whip pans, camera teleports, frozen statue end frames, newspaper wrapping, printed bags, price tags, receipts, scale displays, measuring marks, labeled jars or bottles, readable text, numbers, subtitles, logos, watermarks.
```

### Clip 5 (`tap-14/clip-5.md`)

```text
[FORMAT]
Vertical 9:16, 10-second clip, high-end cinematic 3D food animation, Pixar/Disney-quality stylized CGI, 24fps, natural soft global illumination, physically accurate material shaders, shallow depth of field, controlled specular highlights, cinematic color grade. Characters have detailed soft fur and rich facial expressions, animated with natural anticipation, smooth easing, follow-through, believable weight transfer, and subtle secondary motion in ears, tail, whiskers, fur, clothing, and accessories—never robotic, jittery, foot-sliding, or deformed. Authentic Vietnamese culinary realism: realistic raw and cooked food textures (distinct skin, fat, and lean layers on meat; natural surface moisture on raw ingredients without plastic shine; physically accurate browning, shrinkage, sizzling, and rising steam only when heat is applied). Ultra-smooth camera work using slow dolly, gentle push-in, controlled pan, and smooth lateral tracking with natural acceleration and deceleration (no snap zooms, no whip pans, no camera teleports). Spoken dialogue in Vietnamese with a soft, clear, elegant standard Northern Vietnamese (Hà Nội) accent and accurate lip-sync when the speaker's face is clearly visible; non-speaking characters keep their mouths closed. Spoken lines are written after a colon following the speaker; they are only spoken aloud, never shown as text. Never flash or cut to an attached character reference sheet or studio backdrop. No subtitles, no captions, no on-screen text, no logos, no watermark.

[CHARACTERS — match the attached reference images @Pheo @No 100% exactly]
@Pheo = PHÈO (100% exact match to @Pheo reference image): an anthropomorphic chubby adult male black cat standing and walking upright on two legs; the kitchen countertop reaches his waist. Detailed velvety jet-black short fur with a small white chest locket patch, big round belly, round cheeks, big expressive amber-yellow eyes, small pink nose, long white whiskers, a distinct V-shaped notch on the tip of his LEFT ear (signature mark), thick black tail. Four-fingered black furry paw-hands with soft paw pads, barefoot. Outfit: tall white chef's toque tilted slightly to the right, crisp white short-sleeve crew-neck t-shirt, navy-blue knee-length kitchen apron with one front pocket, small red neckerchief tied neatly at the throat. Personality: confident, witty, proud of his culinary craft, easily left stunned by his boss's stingy twists. Voice: deep, warm, confident, humorous elegant Hà Nội Northern Vietnamese male chef voice, mid-30s.
@No = BÀ CHỦ HƯỜNG (100% exact match to @No reference image): an anthropomorphic chubby adult female Pomeranian dog standing and walking upright on two legs; slightly shorter than Phèo but rounder. Very fluffy cream-orange fur with a lighter cream chest ruff, round pampered face, small black button nose, big glossy dark-brown eyes with long curled eyelashes, pink lipstick, small upright fluffy Pomeranian ears, curled fluffy tail. Four-fingered fluffy cream-orange paw-hands with soft pink paw pads. Outfit: glossy lotus-pink silk Vietnamese pajama set (đồ bộ lụa hồng) with a delicate floral print, short-sleeve button-up top and loose long trousers; a single-strand white pearl necklace, chunky gold bracelets on both wrists, oversized tortoiseshell sunglasses pushed up on top of her head, pink indoor slippers. Personality: wealthy, cute, sassy, adores delicious food, sweet-talking yet stingy with money. Voice: sweet, sassy, rich-auntie elegant Hà Nội Northern Vietnamese female voice, around 40.

[SETTING]
DINING CORNER: the cozy dining corner just through the right doorway of the kitchen, beside a tall window with sheer white curtains. A round dark-wood dining table with a white lace runner, a white electric rice cooker, blue-and-white ceramic rice bowls, wooden chopsticks, and a glass pitcher of iced tea. Hường's large carved wooden armchair with a pink cushion stands on the left side of the table; Phèo's low red plastic stool stands on the right side of the table. Soft golden late-morning sunlight filters through the sheer curtains.
Props on the round dark-wood dining table: the steaming terracotta clay pot of river catfish and pickled bamboo shoot soup (cá lăng nấu măng chua) sits at the center on a woven trivet, with snow-white catfish steaks, golden bamboo shoots, red tomatoes, and green herbs visible; two blue-and-white ceramic bowls, wooden chopsticks, a small saucer of fish sauce with chili slices, and the thick red envelope beside @No.

[SHOT LIST]
00:00–00:03.5 | Medium two-shot at the dining table, gentle push-in — @No (Bà Chủ Hường) sits in her carved wooden armchair on the left, tastes a spoonful of the clear golden-orange soup and a flaky white piece of river catfish, her eyes sparkling with delight while @Pheo sits on his low red plastic stool on the right rubbing his four-fingered black furry paws eagerly. @No says (sweet, sassy elegant Hà Nội Northern Vietnamese auntie voice, delighted): Cá lăng béo ngọt, măng chua thanh mát đỉnh của chóp luôn!
00:03.5–00:07.5 | Close-up over the table, smooth controlled pan — @Pheo stretches out both paws eagerly and asks for his early Tet bonus; @No grins sweetly, opens the thick red envelope, and pulls out… a chunky miniature tear-off daily paper block calendar decorated only with a painted yellow apricot blossom (lốc lịch giấy dày cộp in hình bông mai vàng, completely blank of any text or numbers) and places it into @Pheo's paws. @No says (sweet, sassy elegant Hà Nội Northern Vietnamese auntie voice, cheeky): Thưởng Tết sớm nguyên lốc lịch dày cộp để em bóc đếm ngày tới Tết nè!
00:07.5–00:10 | Medium close-up on @Pheo with a smooth slow push-in and natural easing — @Pheo stares dumbfounded at the thick block calendar in his four-fingered black furry paws, his jaw dropping slightly while his long white whiskers quiver and his V-notched left ear twitches in comedic disbelief as @No happily ladles more soup into her bowl on the left. @Pheo says (deep, warm elegant Hà Nội Northern Vietnamese chef voice, stunned): Ủa… thưởng Tết sớm là tặng lốc lịch đếm ngày hả chị?!

[SOUND]
Background music: upbeat, playful acoustic guitar and light marimba kitchen tune, mixed gently under the dialogue.
Foley: slurp of hot soup, paper rustle as the thick block calendar is pulled from the red envelope, a playful comedic bass pluck and slide whistle as @Pheo reacts in disbelief.

[END FRAME]
Medium two-shot at the sunlit dining table: @Pheo on the right low red stool holding the thick yellow-blossom paper block calendar in his four-fingered black furry paws with wide stunned amber eyes, subtly quivering white whiskers, and twitching V-notched left ear; @No on the left armchair happily enjoying the steaming bowl of cá lăng nấu măng chua; camera stabilizes smoothly with natural secondary motion and rising steam (thumbnail).

[AVOID]
humans, human faces, human hands, extra fingers or fewer than four fingers per paw, robotic or jittery animation, foot sliding, body or muzzle deformation, non-speaking character moving mouth, smoke or boiling oil when stove burner is off, raw meat turning cooked instantly without heat, raw meat touching cooked food or fresh herbs, plastic or toy-like glossy food, utensils or ingredients appearing/disappearing or clipping through paws, reversed kitchen layout, snap zooms, whip pans, camera teleports, frozen statue end frames, newspaper wrapping, printed bags, price tags, receipts, scale displays, measuring marks, labeled jars or bottles, readable text, numbers, subtitles, logos, watermarks.
```
