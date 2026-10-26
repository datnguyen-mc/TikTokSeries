# 365 Ngày Phèo Làm Nội Trợ — Prompt Google Flow (Gemini Omni)

> Quy trình, thiết lập, lỗi thường gặp: xem [../FLOW_GUIDE.md](../FLOW_GUIDE.md)

**Định dạng:** từ Tập 9 mỗi tập **từ 90s trở lên = 9 clip × 10s trở lên**, chia sẻ đủ công thức (Tập 1–7: 30s; Tập 8: 40s) · tạo bằng **Gemini Omni** trong Google Flow · 9:16 · thoại tiếng Việt · không chữ trên video

> **Lưu ý riêng cho series Phèo**
> - **Từ Tập 9: mỗi tập từ 90 giây trở lên, chuẩn 100 giây = 10 clip × 10s**, đi đủ hành trình của món ăn và **chia sẻ đủ công thức** như một người nấu thật:
>   1. **Clip 1 — Đi chợ về và kèo của tập:** 2 giây đầu là cú mồi (giỏ đồ đặt bịch lên đảo bếp, nguyên liệu lăn ra); "Ngày [số], Phèo vô bếp!"; Hường ló ở cửa bên phải ra một **kèo, điều kiện hoặc yêu cầu** (ăn kiêng, có khách, cá cược…) mà clip cuối sẽ trả lời. Phèo vào bếp qua cửa bên phải khung hình (cửa thông góc bàn ăn).
>   2. **Clip 2 — Nguyên liệu chính:** nói 4–5 nguyên liệu chính kèm định lượng và số người ăn (ví dụ: Nửa ký cá kèo, cho ba bốn người!), một mẹo chọn ngoài chợ.
>   3. **Clip 3–4 — Sơ chế:** rửa, khử mùi, cắt thái, ướp; mỗi clip một lý do và thời gian ướp.
>   4. **Clip 5–7 — Nấu:** từng bước với lửa to hay nhỏ, thời gian, dấu hiệu chín; gia vị nói định lượng **đúng lúc cho vào** (Hai muỗng nước mắm, một muỗng đường!); mỗi clip một mẹo.
>   5. **Clip 8 — Nêm nếm, hoàn thiện, trình bày:** tỉ lệ nêm, cách bày đĩa.
>   6. **Clip 9 — Dọn ra bàn ăn:** bưng món ra, bày, Hường nếm và phản ứng.
>   7. **Clip 10 — Twist:** trả lời kèo ở Clip 1, cú đứng hình ở 2 giây cuối, khung thumbnail.
> - **Hường ở giữa tập:** ít nhất 2 lần ló vào bếp ở Clip 3–8 (hít mùi, ăn vụng, hỏi xéo, ra thêm luật), mỗi lần 2–3 giây và tối đa 7 âm tiết. Lần đầu Hường vào trong một chuỗi Frames thì dán FULL LOCK dưới nhãn [CHARACTER ENTERING THIS SEGMENT].
> - **Ngân sách thoại:** mỗi clip tối đa khoảng 31 âm tiết (Phèo khoảng 24, Hường tối đa 7). Mỗi clip nói đúng **một con số quan trọng** (định lượng, thời gian hoặc mức lửa) và **một lý do**; phần còn lại nằm trong Công thức đầy đủ. Món ít bước thì 9 clip (90 giây, gộp Clip 9 và 10); món nhiều công đoạn thì 11–12 clip.
> - **Số trong thoại viết bằng chữ** (năm trăm gam, ba mươi phút), không viết chữ số hay đơn vị tắt trong prompt. **Định lượng thể hiện bằng hình:** nguyên liệu chia sẵn trong chén sứ trắng nhỏ, muỗng canh và muỗng cà phê trơn; không dùng cân điện tử, ly đong có vạch số hay đồng hồ có số.
> - **Đồ đi chợ về:** giỏ cói, túi nilon hồng hoặc trắng trơn, thịt cá gói lá chuối, trứng trong rổ tre, rau buộc lạt. Không dùng giấy báo, túi in chữ, khay xốp có tem, tem giá, hóa đơn hay cân có số. Thêm vào [AVOID] mọi clip: newspaper wrapping, printed bags, price tags, receipts, scale displays, measuring marks, labeled jars or bottles.
> - **Nhảy thời gian khi ướp, kho:** dùng tiếng hẹn giờ trong cùng clip, hoặc tô ướp sẵn lấy từ tủ lạnh (Tô này Phèo ướp từ sáng!), hoặc cắt cảnh bằng Ingredients (FLOW_GUIDE mục 1).
> - **An toàn thực phẩm (bắt buộc mọi tập):** README ghi thời gian và dấu hiệu chín (thịt heo, gà không còn hồng, nước thịt trong); ướp quá 30 phút thì để ngăn mát; thớt, dao riêng cho đồ sống và rau ăn sống; rửa tay sau khi chạm đồ sống; thức ăn thừa cất tủ lạnh trong vòng 2 giờ; một dòng nhắc chó mèo thật không ăn được hành, tỏi, ớt, đồ mặn. Thêm vào [AVOID]: washing raw chicken under running water, tasting from the stirring spoon then stirring again, raw meat touching herbs or cooked food, anyone leaning over an open flame, hot oil splashing, undercooked pink meat served.
> - **Công thức ở README:** mục **Công thức đầy đủ** (nguyên liệu, định lượng, từng bước, thời gian, mẹo, an toàn thực phẩm) kèm bảng **Clip ↔ bước công thức** để thoại và công thức khớp nhau, và mục **Công thức caption** tối đa khoảng 2.500 ký tự để dán vào caption TikTok (caption tối đa khoảng 4.000 ký tự gồm cả hashtag). Bình luận ghim chỉ khoảng 150 ký tự: dùng để nhắc công thức đầy đủ ở caption hoặc một mẹo chính.
> - **Bối cảnh:** các clip trước clip dọn ra ăn ở KITCHEN; clip dọn ra ăn ở DINING CORNER, mở bằng Ingredients lần nữa hoặc cắt theo hành động như Tập 8 (bưng nồi ra cửa → nồi vừa đặt xuống bàn).
> - Tập 1–7 (30s = 3 clip) và Tập 8 (40s = 4 clip) giữ nguyên độ dài cũ.
> - Twist và cú "đứng hình" luôn nằm ở clip cuối cùng.

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
Giọng đầu bếp miền Nam trầm ấm, mạnh mẽ, dí dỏm. Tự tin, hài hước, tự hào tay nghề, nhưng tập nào cũng bị bà chủ làm cho đứng hình.

**FULL LOCK**

```text
@Pheo = PHÈO: an anthropomorphic chubby male black cat, adult, who stands and walks upright on two legs; the kitchen countertop reaches his waist. Glossy jet-black short fur, big round belly, round cheeks, big round amber-yellow eyes, small pink nose, long white whiskers, a tiny V-shaped notch on the tip of his LEFT ear (signature mark), thick black tail. Four-fingered black furry paw-hands with dark grey paw pads, barefoot. Outfit: tall white chef's toque tilted slightly to the right, white short-sleeve crew-neck t-shirt, navy-blue knee-length apron with one front pocket, small red neckerchief tied at the throat. Personality: confident, funny, proud of his cooking, easily stunned by his boss. Voice: deep, warm, strong and witty Southern Vietnamese male chef voice, mid-30s.
```

**SHORT LOCK**

```text
@Pheo = PHÈO: chubby upright black cat, glossy jet-black fur, big amber-yellow eyes, notch on LEFT ear, long white whiskers, white chef's toque tilted right, white t-shirt, navy-blue apron, red neckerchief; deep, warm, witty Southern Vietnamese male chef voice.
```

### Bà chủ Hường

Cô chó Pomeranian mập, lông xù màu kem cam, mặt tròn, mi cong dài, son hồng; thấp hơn Phèo một chút nhưng tròn hơn. Mặc đồ bộ lụa hồng in hoa nhỏ, đeo chuỗi ngọc trai, vòng vàng to ở hai tay, kính râm gọng đồi mồi gác trên đầu, mang dép lê hồng.
Giọng "bà chủ miền Nam" ngọt ngào, đanh đá. Giàu, dễ thương, mê ăn; ngọt ngào trong lời nói nhưng keo kiệt khoản tiền.

**FULL LOCK**

```text
@No = BÀ CHỦ HƯỜNG: an anthropomorphic chubby female Pomeranian dog, adult, who stands and walks upright on two legs; slightly shorter than Phèo but rounder. Very fluffy cream-orange fur with a lighter cream chest ruff, round face, small black button nose, big glossy dark-brown eyes with long curled eyelashes, pink lipstick, small upright fluffy ears, curled fluffy tail. Four-fingered fluffy paw-hands with soft pink paw pads. Outfit: pink silk Vietnamese pajama set (đồ bộ) with a small white-and-red flower print, short-sleeve button-up top and loose long trousers; a single-strand pearl necklace, chunky gold bracelets on both wrists, oversized tortoiseshell sunglasses pushed up on top of her head, pink house slippers. Personality: rich, cute, sassy, adores food, sweet with words but stingy with money. Voice: sweet, sassy Southern Vietnamese rich-auntie female voice, around 40.
```

**SHORT LOCK**

```text
@No = BÀ CHỦ HƯỜNG: chubby upright cream-orange Pomeranian, very fluffy, long eyelashes, pink lipstick, pink floral silk pajama set, pearl necklace, gold bracelets, tortoiseshell sunglasses on her head; sweet, sassy Southern Vietnamese rich-auntie voice.
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
Vertical 9:16, 10-second clip, high-end 3D animated film, Pixar/Disney-quality stylized CGI, soft global illumination, shallow depth of field, 24fps, cinematic color grade. Bright, warm, appetizing food-film look: macro food close-ups, rising steam, sizzling oil, glossy sauces, crisp golden textures. Spoken dialogue in Vietnamese with a natural Southern Vietnamese accent and accurate lip-sync. Spoken lines are written after a colon following the speaker; they are only spoken aloud, never shown as text. Cut only where the shot list says. No subtitles, no captions, no on-screen text, no logos, no watermark.
```

**Nhạc nền**: câu mở đầu mục `[SOUND]` của mọi clip.

```text
Background music: upbeat, playful acoustic guitar and light marimba kitchen tune, low volume under the dialogue.
```

**Câu mở đầu clip 2 trở đi** (làm bằng Frames với start frame = khung cuối clip trước, hoặc bằng Extend): hai dòng đầu tiên của mọi clip từ Clip 2 đến clip cuối, trừ clip mở bằng Ingredients.

```text
Continue the scene seamlessly from the final frame of the previous clip, which is the first frame of this clip. Same characters, same outfits, same location, same lighting and color grade. Flawless continuity, no time skip, no jump cut at the start.
Vertical 9:16, 10-second clip, same animation style. Spoken lines are written after a colon following the speaker; they are only spoken aloud in Vietnamese with a natural Southern accent and accurate lip-sync, never shown as text. Cut only where the shot list says. No subtitles, no captions, no on-screen text.
```

**Câu cửa miệng**: mọi tập mở bằng *"Ngày [số tập], Phèo vô bếp!"* (tập 6 là "Ngày sáu, Phèo vô bếp!", cứ thế đếm tới 365).

**Cú "đứng hình" (chữ ký của series)**: 2 giây cuối của mọi tập.

`SIGNATURE FREEZE` dùng cho tập hài:

```text
Phèo freezes completely mid-motion: eyes wide open as saucers with tiny pupils, whiskers stiff and straight, mouth slightly open, body perfectly still like a paused frame; only the tip of his notched LEFT ear twitches once. The camera snap-zooms into a medium close-up of his face and holds. The background music stops abruptly with a soft record-scratch, followed by silence and a single ticking clock.
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

---

## 6. Các tập — mỗi ngày 1 tập

Mỗi tập (từ Tập 9: từ 90s = 9 clip × 10s trở lên; Tập 1–7: 30s = 3 clip; Tập 8: 40s = 4 clip) là một ngày đăng, nằm trong thư mục riêng `tap-{số}/` cùng thư mục này: `README.md` là tổng quan tập, `clip-1.md` … `clip-N.md` (từ Tập 9 ít nhất 9 file) là prompt của từng clip 10 giây. Tập mới đánh số tiếp (`tap-9/`, …) và dùng nguyên các khóa ở mục 1–3.

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
