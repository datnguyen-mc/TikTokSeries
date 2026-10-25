# Nhà Tèo & Sún — Prompt Google Flow (Gemini Omni)

> Quy trình, thiết lập, lỗi thường gặp: xem [../FLOW_GUIDE.md](../FLOW_GUIDE.md)

**Định dạng:** từ Tập 7 mỗi tập **40–60s = 4–6 clip × 10s** tùy câu chuyện (Tập 1–6: 30s = 3 clip) · tạo bằng **Gemini Omni** trong Google Flow · 9:16 · thoại tiếng Việt · không chữ trên video

**Khán giả:** phụ nữ 18–50 · **Tỉ lệ nội dung:** 70% chuyện gia đình · 20% hài hước & cảm xúc · 10% sản phẩm

**Độ dài và cấu trúc (từ Tập 7):** 40–60 giây = 4–6 clip × 10s tùy câu chuyện.

| Số clip | Bố cục |
| --- | --- |
| 4 (40s) | 1 Mở · 2 Trục trặc · 3 Mẹo của Sún · 4 Thương nhau và kết vui |
| 5 (50s) | 1 Mở · 2–3 Trục trặc · 4 Mẹo của Sún · 5 Thương nhau và kết vui |
| 6 (60s) | 1 Mở · 2–3 Trục trặc · 4 Mẹo của Sún · 5 Thương nhau · 6 Kết vui |

- **Mở:** một tình huống trong nhà có thật (chăm con, việc nhà, quà cáp, tiền chợ) và câu thoại gây tò mò. **Trục trặc:** Tèo vụng về hoặc làm quá tay. **Mẹo của Sún:** một mẹo đời sống có thật; sản phẩm lên hình trong **một clip duy nhất**, khoảng 4–6 giây, tên thương hiệu nói một lần. **Kết:** yêu thương kèm chút hài, em bé thường là điểm chốt; khung thumbnail đứng yên 1 giây.
- **Như người thật chia sẻ:** mẹo chăm con, việc nhà phải đúng và an toàn (đặc biệt với em bé) và có nguồn trong README, ở mục **Mẹo trong tập** (mẹo nói gì, vì sao đúng, nguồn); mỗi clip 2–3 câu thoại, tối đa khoảng 31 âm tiết. Sản phẩm tối đa khoảng 10% thời lượng, tên thương hiệu chỉ nói bằng thoại.
**Slogan:** ❤️ "Nhà Tèo & Sún – Chuyện nhỏ mỗi ngày, yêu thương đong đầy!" (chỉ nói bằng thoại, không hiện chữ)

---

## 1. Khóa nhân vật (Character Bible)

**Tên nhân vật trên Flow:** `@TeoTeo` (chó đực) · `@SunSun` (chó cái). Trong prompt hai nhân vật cũng được gọi là TeoTeo và SunSun. Mỗi dòng khóa của nhân vật chính bắt đầu bằng `@Tên = …`, để Flow gọi đúng nhân vật đã lưu và model hiểu tên đó là nhân vật nào trong prompt.

Dán **nguyên văn** các khối bên dưới: **FULL LOCK** cho Clip 1 và cho clip mà nhân vật xuất hiện lần đầu; **SHORT LOCK** từ Clip 2 đến clip cuối cho nhân vật đã có mặt ở clip ngay trước. Các prompt trong từng file `tap-{số}/clip-{số}.md` đã chèn sẵn, chỉ cần copy.

### Tèo (TeoTeo) — ông chồng

Chihuahua đực lông ngắn màu vàng bò, mặt nạ nâu đậm quanh mắt, tai dơi rất to (**tai phải có vết khuyết nhỏ hình chữ V**, dấu nhận diện bắt buộc), mắt tròn đen láy, bụng hơi tròn, cao hơn Sún một cái đầu. Vụng về, hài hước nhưng rất thương vợ con.
**Giọng:** nam miền Nam, hơi khàn, ấm, hài hước. **Biểu cảm đặc trưng:** giật mình thì hai tai dựng đứng như ăng-ten, hối lỗi thì tai cụp sang hai bên. **Câu cửa miệng:** "Để anh lo!"

**Biến thể A — đồ ở nhà** (Tập 1, 3, 4): áo ba lỗ trắng gân, quần đùi caro đỏ–xanh navy, dép tông xanh dương.

FULL LOCK — Biến thể A
```text
@TeoTeo = TeoTeo: adult male anthropomorphic smooth-coat Chihuahua, short sleek fawn-tan fur with a darker tan mask around the eyes, huge upright bat ears with a small V-shaped nick on the outer edge of his RIGHT ear, big glossy round dark-brown eyes, small black nose, slightly chubby round belly, about a head taller than SunSun. Wears a white ribbed tank top, red-and-navy plaid shorts and blue flip-flops. Voice: slightly husky, warm Southern Vietnamese male voice, early 30s, funny, a little clumsy, sweet.
```

SHORT LOCK — Biến thể A
```text
@TeoTeo = TeoTeo: fawn-tan smooth-coat Chihuahua, darker tan eye mask, huge bat ears with a nick on the RIGHT ear, chubby belly; white ribbed tank top, red-and-navy plaid shorts, blue flip-flops; slightly husky, warm Southern male voice.
```

**Biến thể B — diện đồ tặng quà** (Tập 2): áo sơ mi trắng tay ngắn, nơ đỏ nhỏ, lông đầu chải lệch bóng mượt, nhưng vẫn mặc quần đùi caro và mang dép tông (chi tiết gây cười).

FULL LOCK — Biến thể B
```text
@TeoTeo = TeoTeo: adult male anthropomorphic smooth-coat Chihuahua, short sleek fawn-tan fur with a darker tan mask around the eyes, huge upright bat ears with a small V-shaped nick on the outer edge of his RIGHT ear, big glossy round dark-brown eyes, small black nose, slightly chubby round belly, about a head taller than SunSun. Dressed up for a surprise: crisp white short-sleeve button-up shirt with a small red bow tie, the fur on top of his head neatly slicked to one side, but still in his red-and-navy plaid shorts and blue flip-flops. Voice: slightly husky, warm Southern Vietnamese male voice, early 30s, funny, a little clumsy, sweet.
```

SHORT LOCK — Biến thể B
```text
@TeoTeo = TeoTeo: fawn-tan smooth-coat Chihuahua, darker tan eye mask, huge bat ears with a nick on the RIGHT ear, chubby belly, head fur slicked to one side; crisp white short-sleeve shirt with small red bow tie, red-and-navy plaid shorts, blue flip-flops; slightly husky, warm Southern male voice.
```

### Sún (SunSun) — bà vợ

Chihuahua cái lông dài màu trắng kem bông mềm, tai có lông tua, nơ satin hồng trên đầu, lông mi dài cong, mắt nâu ấm, nhỏ nhắn, thấp hơn Tèo một cái đầu. Đảm đang, hay cằn nhằn nhưng luôn thương chồng con.
**Trang phục cố định:** đồ bộ xanh bạc hà in hoa nhí trắng, dép lê hồng. **Giọng:** nữ miền Nam, trong, nói nhanh, hơi cằn nhằn nhưng đầy yêu thương. **Câu cửa miệng:** "Ông xã giỏi ghê!"

FULL LOCK
```text
@SunSun = SunSun: adult female anthropomorphic long-coat Chihuahua, soft fluffy cream-white fur, long feathered ears, a pink satin bow on top of her head, long curled eyelashes, warm brown eyes, small dark nose, petite and slim, about a head shorter than TeoTeo. Wears a mint-green matching home set (short-sleeve top and long pants) printed with tiny white flowers, and pink house slippers. Voice: clear, quick Southern Vietnamese female voice, late 20s, a bit naggy but always loving.
```

SHORT LOCK
```text
@SunSun = SunSun: fluffy cream-white long-coat Chihuahua, feathered ears, pink satin bow on her head, long lashes, warm brown eyes; mint-green home set with tiny white flowers, pink house slippers; clear, quick, loving Southern female voice.
```

### Em bé — con của Tèo và Sún

Chihuahua sơ sinh, lông vàng bò xen mảng kem ở mặt và ngực, tai to còn cụp, mắt đen long lanh, luôn quấn khăn vàng pastel, có núm ti vàng (chỉ ngậm khi ngoan). **Không nói**, chỉ ê a, cười khanh khách, khóc nhỏ.

FULL LOCK
```text
BABY: newborn Chihuahua puppy, tiny enough to fit in one of TeoTeo's arms, soft fawn fur with cream patches on the face and chest, oversized floppy ears not yet upright, big shiny dark eyes, swaddled snugly in a soft pastel-yellow blanket, a small pastel-yellow pacifier only when calm. Makes only soft coos, giggles and small cries, never speaks words.
```

SHORT LOCK
```text
BABY: tiny newborn Chihuahua puppy, fawn fur with cream patches, floppy ears, swaddled in a pastel-yellow blanket; only coos, giggles and small cries.
```

---

## 2. Bối cảnh cố định

Căn hộ hiện đại, ấm cúng của nhà Tèo & Sún. Trong prompt, khối bối cảnh được dán nguyên văn, bên dưới thêm 2 dòng riêng của từng tập: `Time & light:` (thời gian, ánh sáng) và `Props:` (đạo cụ).

**Phòng khách** (Tập 2): cửa ra hành lang bên trái, cửa sổ bên phải.
```text
LIVING ROOM: cozy modern Vietnamese apartment living room, light-oak floor with a round cream rug, soft beige fabric sofa with mustard and sage-green cushions, low wooden coffee table, framed family photos of the Chihuahua family on a cream wall, potted monstera and pothos plants, large window with sheer white curtains on the right, warm floor lamp, a wide doorway to the hallway on the left. Clean and lived-in, everything scaled for small dogs.
```

**Phòng ngủ** (Tập 1): từ trái sang phải là giường → nôi em bé → bàn nhỏ có đèn ngủ mặt trăng → ghế bập bênh.
```text
BEDROOM: cozy master bedroom in a modern Vietnamese apartment. From left to right: a double bed with white and pale-blue bedding, a white wooden baby crib with soft yellow bumpers right beside the bed, a small wooden side table with a moon-shaped nightlight, and a wooden rocking chair with a cream knitted throw over its back. A window with sheer curtains behind the rocking chair, a round wall clock with simple tick marks and no numbers.
```

**Nhà bếp** (Tập 4)
```text
KITCHEN: bright compact modern Vietnamese apartment kitchen, white cabinets with light-wood countertops, a stainless-steel sink under a window, a dish rack beside the sink, a gas stove, small pots of green herbs on the windowsill, a warm pendant lamp over a small round wooden dining table with four chairs, a baby bouncer seat with a pastel-yellow cushion beside the table, light-grey tiled floor.
```

**Ban công giặt đồ** (Tập 3): cửa kính vào nhà ở bên trái.
```text
LAUNDRY BALCONY: small apartment laundry balcony in Ho Chi Minh City, a white top-loading washing machine with a plain icon-only control panel, a small blue plastic step stool, a foldable stainless-steel drying rack, a woven laundry basket, little potted plants along the white railing, terracotta-tiled floor, a glass door back into the apartment on the left, view of mid-rise buildings and green treetops.
```

**Phòng tắm** (Tập 5): kệ bồn rửa ngang thắt lưng, chậu tắm em bé đặt chắc trên kệ; cửa ra hành lang bên trái, cửa sổ kính mờ bên phải.
```text
BATHROOM: bright, cozy modern Vietnamese apartment bathroom, white subway-tile walls with a mint-green accent stripe, light-grey anti-slip floor tiles, a wide white vanity counter at waist height with a small sink, a handheld shower head on a hose beside the sink, a small pastel-yellow baby bathtub with a soft inner bath support resting securely on the counter, a round wooden wall shelf with rolled white towels, a frosted-glass window on the right letting in soft daylight, a doorway to the hallway on the left. Clean and safe, everything scaled for small dogs.
```

---

## 3. Khóa phong cách

Khối `[FORMAT]`, đặt đầu mọi prompt **Clip 1**:
```text
[FORMAT]
Vertical 9:16, 10-second clip, high-end 3D animated film, Pixar/Disney-quality stylized CGI, cozy warm family-sitcom look, soft global illumination, shallow depth of field, 24fps, cinematic warm color grade, compositions framed for vertical video with the key action centered. All characters are anthropomorphic Chihuahuas who walk upright on two legs, with expressive faces and paw-hands with four fingers. Spoken dialogue in Vietnamese with a natural Southern Vietnamese accent and accurate lip-sync. Spoken lines are written after a colon following the speaker; they are only spoken aloud, never shown as text. Cut only where the shot list says. No subtitles, no captions, no on-screen text, no logos, no watermark.
```

Câu mở đầu, đặt đầu mọi prompt **từ Clip 2 đến clip cuối** (làm bằng Frames với start frame = khung cuối clip trước, hoặc bằng Extend; clip mở bằng Ingredients thì dùng [FORMAT]):
```text
Continue the scene seamlessly from the final frame of the previous clip, which is the first frame of this clip. Same characters, same outfits, same location, same lighting and color grade. Flawless continuity, no time skip, no jump cut at the start.
Vertical 9:16, 10-second clip, same animation style. Spoken lines are written after a colon following the speaker; they are only spoken aloud in Vietnamese with a natural Southern accent and accurate lip-sync, never shown as text. Cut only where the shot list says. No subtitles, no captions, no on-screen text.
```

---

## 4. Ảnh tham chiếu nhân vật

Tạo bằng Nano Banana / Imagen trong Flow, tỉ lệ 16:9 (đủ chỗ cho 4 góc nhìn). Mỗi nhân vật chạy 3–4 lần, chọn ảnh đẹp nhất, lưu đúng tên file bên dưới và **dùng lại cho mọi tập**.

| File | Dùng cho |
| --- | --- |
| `TEO_A.png` | Tập 1, 3, 4, 5, 6 |
| `TEO_B.png` | Tập 2 |
| `SUN.png` | Tất cả các tập |
| `BABY.png` | Tập 1, 4, 5, 6 |

**TEO_A.png — Tèo, đồ ở nhà**
```text
Character turnaround sheet, high-end 3D animated film style, Pixar/Disney-quality stylized CGI. The same adult male anthropomorphic smooth-coat Chihuahua standing upright on two legs, shown four times side by side in one row: front view, three-quarter view, side view, back view. Short sleek fawn-tan fur with a darker tan mask around the eyes, huge upright bat ears with a small V-shaped nick on the outer edge of his RIGHT ear, big glossy round dark-brown eyes, small black nose, slightly chubby round belly, paw-hands with four fingers. Wears a white ribbed tank top, red-and-navy plaid shorts and blue flip-flops. Full body from head to toe, neutral relaxed standing pose, friendly slight smile, identical design and scale in every view, soft even studio lighting, plain light-grey seamless background. No text, no labels, no numbers, no watermark.
```

**TEO_B.png — Tèo, diện đồ tặng quà** (đính kèm `TEO_A.png` khi tạo để giữ nguyên khuôn mặt)
```text
Same character as the attached image, only the outfit changes. Character turnaround sheet, high-end 3D animated film style, Pixar/Disney-quality stylized CGI. The same adult male anthropomorphic smooth-coat Chihuahua standing upright on two legs, shown four times side by side in one row: front view, three-quarter view, side view, back view. Short sleek fawn-tan fur with a darker tan mask around the eyes, huge upright bat ears with a small V-shaped nick on the outer edge of his RIGHT ear, big glossy round dark-brown eyes, small black nose, slightly chubby round belly, paw-hands with four fingers. Dressed up: crisp white short-sleeve button-up shirt with a small red bow tie, the fur on top of his head neatly slicked to one side, red-and-navy plaid shorts and blue flip-flops. Full body from head to toe, neutral relaxed standing pose, proud slightly shy smile, identical design and scale in every view, soft even studio lighting, plain light-grey seamless background. No text, no labels, no numbers, no watermark.
```

**SUN.png — Sún**
```text
Character turnaround sheet, high-end 3D animated film style, Pixar/Disney-quality stylized CGI. The same adult female anthropomorphic long-coat Chihuahua standing upright on two legs, shown four times side by side in one row: front view, three-quarter view, side view, back view. Soft fluffy cream-white fur, long feathered ears, a pink satin bow on top of her head, long curled eyelashes, warm brown eyes, small dark nose, petite and slim, paw-hands with four fingers. Wears a mint-green matching home set (short-sleeve top and long pants) printed with tiny white flowers, and pink house slippers. Full body from head to toe, neutral relaxed standing pose, gentle warm smile, identical design and scale in every view, soft even studio lighting, plain light-grey seamless background. No text, no labels, no numbers, no watermark.
```

**BABY.png — Em bé**
```text
Character reference sheet, high-end 3D animated film style, Pixar/Disney-quality stylized CGI. The same newborn Chihuahua puppy shown four times side by side in one row: front view, three-quarter view, side view and top-down view, lying calmly on a soft plain light-grey surface. Soft fawn fur with cream patches on the face and chest, oversized floppy ears not yet upright, big shiny dark eyes, swaddled snugly in a soft pastel-yellow blanket with only the head and tiny front paws visible, a small pastel-yellow pacifier. Identical design and scale in every view, soft even studio lighting, plain light-grey seamless background. No text, no labels, no numbers, no watermark.
```

**Kiểm tra trước khi chốt ảnh:** tai phải của Tèo có vết khuyết · Sún có nơ hồng · lông Sún trắng kem (không ngả vàng) · bé quấn khăn vàng · trên ảnh không có chữ.

**Ảnh sản phẩm:** chụp sản phẩm thật trên nền trơn, đủ sáng, thẳng mặt trước, lưu thành `SP_TOPGIA.png` (giấy ăn), `SP_SUATAM.png`, `SP_NUOCGIAT.png`, `SP_NUOCRUACHEN.png`, `SP_SUATAMBE.png` (sữa tắm gội cho bé). Đính kèm ở clip sản phẩm lên hình lần đầu (cùng ảnh nhân vật nếu đó là Clip 1). Nếu clip đó làm bằng Frames mà Flow không cho đính ảnh, cho sản phẩm có sẵn trong khung cuối của clip trước đã đính ảnh, hoặc mở clip đó bằng Ingredients.

---

## 5. Danh sách tập

| Tập | Tên | Nội dung | Sản phẩm |
| --- | --- | --- | --- |
| 1 | Lần đầu làm cha | Nửa đêm Tèo giành dỗ con cho Sún ngủ; bé ọc sữa, Tèo lau bằng giấy mềm; sáng ra Sún đắp chăn cho hai cha con | Giấy ăn Top Gia |
| 2 | Quà 20/10 bất ngờ | Tèo diện nơ đỏ giấu quà, trượt chân lộ bí mật, quỳ tặng hoa và sữa tắm, hứa chia đôi việc nhà | Sữa tắm |
| 3 | Tèo giặt đồ lần đầu | Giữ lời hứa, Tèo đổ quá tay nước giặt, bọt tràn ban công; Sún chỉ dùng một nắp; đồ thơm, Sún khen | Nước giặt |
| 4 | Tèo rửa chén | Tèo giành rửa chén, một giọt nước rửa chén sạch dầu mỡ; khoe tài làm văng chén nhựa, bé cười, cả nhà ôm nhau | Nước rửa chén |
| 5 | Tèo tắm cho con lần đầu | Tiếp tục giữ lời hứa, Tèo chuẩn bị quá đà như sắp mổ; Sún dạy thử nước bằng khuỷu tay; Tèo đỡ đầu cổ con chuẩn từng chút thì bị bé đạp nước tạt ướt mặt; quấn khăn, cả nhà ôm nhau | Sữa tắm gội cho bé |
| 6 | Halloween đầu tiên của bé | ⚡ Trend Halloween: Sún khoe bé trong bộ đồ bí ngô; Tèo bước ra trong bộ "xác ướp" quấn giấy Top Gia, nhảy mà giấy không rách; bé nắm đầu giấy làm Tèo xoay tròn bung hết; cả nhà bên đèn bí ngô | Giấy ăn Top Gia |

**Mạch nối các tập:** Tập 2 Tèo hứa "Mai anh giặt đồ luôn!" → Tập 3 Tèo giặt đồ, học bài "một nắp thôi" → Tập 4 Tèo rửa chén, nhớ bài "một giọt thôi". Nên đăng theo đúng thứ tự.

**Bản 20 giây (Tập 1–6):** dừng sau Clip 2. Khung cuối Clip 2 của các tập này đều được thiết kế để kết được.

**Sản phẩm chưa có thương hiệu (Tập 2–4):** thoại đang để chung chung (ví dụ "chai sữa tắm này"). Muốn nhắc tên thương hiệu thì thay thẳng vào câu thoại, giữ mỗi câu tối đa 12 âm tiết.

---

## 6. Các tập — mỗi ngày 1 tập

Mỗi tập (từ Tập 7: 40–60s = 4–6 clip × 10s; Tập 1–6: 30s = 3 clip) là một ngày đăng, nằm trong thư mục riêng `tap-{số}/` cùng thư mục này: `README.md` là tổng quan tập, `clip-1.md` … `clip-N.md` (4–6 file; Tập 1–6: `clip-1.md` … `clip-3.md`) là prompt của từng clip 10 giây. Tập mới đánh số tiếp (`tap-7/`, …) và dùng nguyên các khóa ở mục 1–3.

| Ngày | File | Tên tập |
| --- | --- | --- |
| 1 | [tap-1/](tap-1/README.md) | Lần đầu làm cha |
| 2 | [tap-2/](tap-2/README.md) | Quà 20/10 bất ngờ |
| 3 | [tap-3/](tap-3/README.md) | Tèo giặt đồ lần đầu |
| 4 | [tap-4/](tap-4/README.md) | Tèo rửa chén |
| 5 | [tap-5/](tap-5/README.md) | Tèo tắm cho con lần đầu |
| 6 | [tap-6/](tap-6/README.md) | Halloween đầu tiên của bé |
