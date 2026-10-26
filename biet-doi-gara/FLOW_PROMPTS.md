# Biệt Đội Gara — Prompt Google Flow (Gemini Omni)

> Quy trình, thiết lập, lỗi thường gặp: xem [../FLOW_GUIDE.md](../FLOW_GUIDE.md) · Kế hoạch series: [README.md](README.md)

**Định dạng:** tập nhiều đánh nhau **40s = 4 clip**, tập kể chuyện **60s = 6 clip** (10s mỗi clip) · tạo bằng **Gemini Omni** trong Google Flow · 9:16 · thoại tiếng Việt giọng miền Nam · không chữ trên video · **hình người thật kiểu phim siêu anh hùng**: người thật, giáp như đồ hóa trang thật cỡ phim lớn, hiệu ứng năng lượng bằng ánh sáng.

**Thế giới:** Sài Gòn hôm nay. **Gara Bảy** là tiệm độ xe hai tầng ven một con kênh, do **Bác Bảy** (người thầy của Thắng, đã mất) mở. Bốn người sống quanh gara như một gia đình: Thắng, Lan, Hải, Khôi. Đường dây **Găng Xám** của **Sói Xám** dùng găng năng lượng để trộm xe và buôn lậu qua cảng. Bác Bảy để lại năm **Lõi Giáp** giấu trong thùng đồ nghề cũ; mỗi lõi chọn một người và biến người đó thành chiến binh mặc giáp. Lõi thứ năm chọn **Đại úy Minh** (Tập 3). Luật của nhà: **muốn đua thì lên đường đua, ra đường là chở người mình thương.**

**Xương sống mỗi tập:**

| Loại tập | Số clip | Bố cục |
| --- | --- | --- |
| Đánh nhau (40s, vừa một chuỗi Extend) | 4 | 1 Hook hành động và biến hình · 2 Đánh, phần 1 · 3 Đánh, phần 2 và cú lật · 4 Phản diện lộ mặt hoặc móc câu |
| Kể chuyện (60s) | 6 | 1 Hook · 2 Đặt vấn đề · 3–4 Hành động · 5 Cú lật · 6 Gia đình và móc câu |

- **Gia đình là trái tim:** tập nào cũng có một khoảnh khắc thương nhau (bữa cơm, cái vỗ vai, câu nói về Bác Bảy). Hải nấu cơm cho cả nhà.
- **Thoại ngắn:** mỗi câu tối đa khoảng 10 âm tiết, không quá 4,5 âm tiết mỗi giây, mỗi clip tối đa khoảng 31 âm tiết. Ai nói thì máy thấy rõ mặt người đó (giáp có kính trong suốt nên vẫn thấy môi).
- **Quay như phim:** mỗi prompt có khối `[CAMERA & LIGHT]` và `[SHOT LIST]` chia nhịp 1–2,5 giây, mỗi nhịp một động tác (một cú đá, một cú né, một lần biến hình). Mỗi pha có một nhịp quay chậm làm điểm nhấn.
- **Cảnh nối nhau hợp lý:** mỗi clip bắt đầu đúng chỗ clip trước dừng; cắt cảnh chỉ khi đổi địa điểm hoặc nhảy thời gian, dòng đầu `[SHOT LIST]` ghi rõ thời gian đã trôi.

**Luật, an toàn, chính sách (bắt buộc, đã chặn trong [AVOID]):**
- **Không súng, không dao, không máu**, không vết thương ghê rợn, không ai chết. Kẻ xấu bị đánh ngã, bị khóa găng, rồi bị cảnh sát bắt.
- **Không cổ vũ đua xe trái phép** (tội hình sự theo Bộ luật Hình sự 2015, Điều 265–266): nhân vật chính chỉ đua trên đường đua kín; rượt đuổi bằng xe chỉ ở cảng, xưởng bỏ hoang hoặc đường đã được cảnh sát phong tỏa trong truyện; đi xe máy luôn đội mũ bảo hiểm, đi xe hơi luôn thắt dây an toàn.
- **Không giống thương hiệu hay phim có sẵn:** giáp, tên, câu biến hình là sáng tác mới, không giống bất kỳ loạt siêu nhân, siêu anh hùng nào; xe, container, biển hiệu không logo, không chữ, không biển số đọc được.
- **Nhãn AI:** mỗi tập bật nhãn **Nội dung do AI tạo**; caption ghi "Phim hư cấu do AI tạo".

**Cách dán prompt:** mỗi file `clip-{số}.md` là một lần dán. **FULL LOCK** dùng ở clip mở bằng Ingredients và cho nhân vật mới vào giữa chuỗi (dòng `[CHARACTER ENTERING THIS SEGMENT]`); **SHORT LOCK** dùng ở clip làm bằng Frames hoặc Extend. Khi nhân vật đang mặc giáp thì dùng khóa **GIÁP** của người đó.

---

## 1. Khóa nhân vật

**Tên nhân vật trên Flow:** `@Thang` · `@Lan` · `@Hai` · `@Khoi` · `@Minh`. Trong phần còn lại của prompt gọi là THẮNG · LAN · HẢI · KHÔI · MINH. Mỗi người có hai khóa: **thường phục** và **giáp**. Tạo nhân vật trên Flow từ ảnh thường phục; cảnh mặc giáp thì đính thêm ảnh giáp của người đó.

**Lõi Giáp:** năm lõi kim loại hình lục giác cỡ lòng bàn tay, mỗi lõi phát sáng một màu: đỏ (Thắng), trắng xanh băng (Lan), cam (Hải), vàng (Khôi), xanh thẫm (Minh). Khi được chọn, lõi gắn lên **cổ tay TRÁI** thành vòng tay phát sáng. **Câu biến hình:** "Lõi Bảy, khởi động!" Khi bấm lõi, các mảnh giáp sáng mở ra từ lõi, ôm lấy người từng mảnh trong khoảng hai giây, cuối cùng kính mũ trượt xuống; mặt vẫn thấy rõ qua kính trong suốt.

### Thắng "Gió" — anh cả, chủ Gara Bảy, cựu tay đua chuyên nghiệp

FULL LOCK — thường phục
```text
@Thang = THẮNG (36, the eldest, owner of Gara Bảy): a real Vietnamese man, about 178 cm tall, lean and strong, square jaw, calm dark eyes, light stubble, short black hair with a single silver streak at his LEFT temple (signature detail), a faded burn scar on his LEFT forearm. Civilian outfit: an olive-green mechanic's work jacket with the sleeves pushed up over a black T-shirt, dark work trousers, black boots, a red shop rag hanging from his back pocket. Voice: deep, calm, steady Southern Vietnamese male voice, mid-30s.
```
SHORT LOCK — thường phục
```text
@Thang = THẮNG: Vietnamese man, 36, silver streak at his LEFT temple, burn scar on his LEFT forearm, olive work jacket over a black T-shirt, red rag in his back pocket; deep, calm Southern male voice.
```
FULL LOCK — Giáp Gió
```text
@Thang = THẮNG in his armor GIÁP GIÓ: the same man inside a sleek red-and-black armored suit of matte composite plates with angular wind-vent fins on the shoulders and calves and glowing red light lines; an open-face armored helmet with a clear amber visor, so his whole face, the silver streak at his LEFT temple and his lips stay visible; a glowing red hexagonal core on his LEFT wrist. Power: short dashes of speed that leave red wind streaks. Voice: deep, calm, steady Southern Vietnamese male voice.
```
SHORT LOCK — Giáp Gió
```text
@Thang = THẮNG in GIÁP GIÓ: red-and-black armor with wind-vent fins, open-face helmet with a clear amber visor showing his face, red core on his LEFT wrist; deep, calm Southern male voice.
```

### Lan "Cáo" — tay lái giỏi nhất nhà

FULL LOCK — thường phục
```text
@Lan = LAN (29, the best driver of the family): a real Vietnamese woman, about 162 cm tall, petite and athletic, sharp bright eyes, a confident half smile, a short black bob with one ice-blue streak on the RIGHT side (signature detail). Civilian outfit: a white leather moto jacket over a grey top, black jeans, white sneakers. Voice: quick, bright, confident Southern Vietnamese female voice, late 20s.
```
SHORT LOCK — thường phục
```text
@Lan = LAN: Vietnamese woman, 29, short black bob with an ice-blue streak on the RIGHT, white leather moto jacket, black jeans, white sneakers; quick, bright Southern female voice.
```
FULL LOCK — Giáp Cáo
```text
@Lan = LAN in her armor GIÁP CÁO: the same woman inside a slim white armored suit with ice-blue light lines and a small fox-ear crest on the helmet; an open-face armored helmet with a clear ice-blue visor, so her whole face and the ice-blue streak in her hair stay visible; a glowing white-blue hexagonal core on her LEFT wrist. Power: blinding speed and agility that leaves white-blue afterimages. Voice: quick, bright, confident Southern Vietnamese female voice.
```
SHORT LOCK — Giáp Cáo
```text
@Lan = LAN in GIÁP CÁO: slim white armor with ice-blue lines and a fox-ear crest, open-face helmet with a clear ice-blue visor showing her face, white-blue core on her LEFT wrist; quick, bright Southern female voice.
```

### Hải "Búa" — thợ máy, võ sĩ Vovinam, người nấu cơm cho cả nhà

FULL LOCK — thường phục
```text
@Hai = HẢI (32, the family's mechanic, cook and Vovinam fighter): a real Vietnamese man, about 188 cm tall, big and broad-shouldered, warm brown eyes, a short full black beard, hair shaved short on the sides with a short top (signature detail: the tallest and biggest of the family). Civilian outfit: a grey tank top under a brown leather work apron, dark cargo trousers, boots, a big steel wrench usually in his hand or apron. Voice: big, warm, booming Southern Vietnamese male voice, early 30s, gentle.
```
SHORT LOCK — thường phục
```text
@Hai = HẢI: very big Vietnamese man, 32, short full beard, shaved sides, grey tank top under a brown leather apron, steel wrench; big, warm, booming Southern male voice.
```
FULL LOCK — Giáp Búa
```text
@Hai = HẢI in his armor GIÁP BÚA: the same big man inside heavy orange-and-gunmetal armor with thick shoulder plates and a short buffalo-horn crest on the helmet; an open-face armored helmet with a clear orange visor, so his bearded face stays visible; a glowing orange hexagonal core on his LEFT wrist. His steel wrench turns into a glowing orange energy hammer that knocks enemies back with harmless shockwaves of light. Voice: big, warm, booming Southern Vietnamese male voice.
```
SHORT LOCK — Giáp Búa
```text
@Hai = HẢI in GIÁP BÚA: heavy orange-and-gunmetal armor with a buffalo-horn crest, open-face helmet with a clear orange visor showing his bearded face, orange core on his LEFT wrist, glowing orange energy hammer; big, warm, booming Southern male voice.
```

### Khôi "Bit" — dân công nghệ, vai gây cười

FULL LOCK — thường phục
```text
@Khoi = KHÔI (25, the family's tech genius and joker): a real Vietnamese young man, about 170 cm tall, slim, round tortoiseshell glasses (signature detail), messy black hair, an expressive nervous face. Civilian outfit: a mustard-yellow hoodie, black joggers, sneakers, headphones around his neck, a laptop in his hands or a small backpack. Voice: fast, nervous, funny Southern Vietnamese male voice, mid-20s.
```
SHORT LOCK — thường phục
```text
@Khoi = KHÔI: slim Vietnamese young man, 25, round tortoiseshell glasses, messy hair, mustard-yellow hoodie, headphones around his neck; fast, nervous, funny Southern male voice.
```
FULL LOCK — Giáp Bit
```text
@Khoi = KHÔI in his armor GIÁP BIT: the same young man inside a slim yellow-and-black armored suit with circuit-like light lines and two palm-sized drones docked on his shoulders; an open-face armored helmet with a clear yellow visor, so his face and his round glasses stay visible; a glowing yellow hexagonal core on his LEFT wrist. Power: his drones fire rings of yellow light that switch off enemy gauntlets. Voice: fast, nervous, funny Southern Vietnamese male voice.
```
SHORT LOCK — Giáp Bit
```text
@Khoi = KHÔI in GIÁP BIT: slim yellow-and-black armor with two shoulder drones, open-face helmet with a clear yellow visor showing his face and round glasses, yellow core on his LEFT wrist; fast, nervous, funny Southern male voice.
```

### Đại úy Minh — nữ cảnh sát hình sự, lõi thứ năm (từ Tập 2)

FULL LOCK — thường phục
```text
@Minh = MINH (35, a police detective captain): a real Vietnamese woman, about 168 cm tall, athletic, sharp straight eyebrows, serious dark eyes, a thin pale scar on her chin (signature detail), black hair in a tight low bun. Civilian outfit: a black plain-clothes jacket over a white shirt, dark trousers, low black boots, no badges or readable text. Voice: firm, low, clear Southern Vietnamese female voice, mid-30s.
```
SHORT LOCK — thường phục
```text
@Minh = MINH: Vietnamese woman, 35, thin scar on her chin, tight low bun, black jacket over a white shirt; firm, low, clear Southern female voice.
```
FULL LOCK — Giáp Khiên
```text
@Minh = MINH in her armor GIÁP KHIÊN: the same woman inside navy-and-silver armor with clean straight lines and a round energy shield of navy light on her left forearm; an open-face armored helmet with a clear navy visor, so her face and the scar on her chin stay visible; a glowing navy hexagonal core on her LEFT wrist. Power: an energy shield and navy light cuffs that lock enemy gauntlets for arrest. Voice: firm, low, clear Southern Vietnamese female voice.
```
SHORT LOCK — Giáp Khiên
```text
@Minh = MINH in GIÁP KHIÊN: navy-and-silver armor with a round navy energy shield on her left forearm, open-face helmet with a clear navy visor showing her face and chin scar, navy core on her LEFT wrist; firm, low, clear Southern female voice.
```

### Nhân vật phụ (một khóa, dùng nguyên văn mọi clip)

**Bác Bảy** — người thầy đã mất, chỉ xuất hiện qua hình ảnh hologram.
```text
BÁC BẢY (the late founder of Gara Bảy, seen only as a hologram): a kind old Vietnamese mechanic in his late 60s with a white crew cut, deep smile lines and a faded blue work shirt, shown as a flickering soft-blue hologram projected from a small old device. Voice: warm, gravelly elderly Southern Vietnamese male voice.
```

**Sói Xám** — trùm đường dây.
```text
SÓI XÁM (the villain): a Vietnamese man of about 45 with salt-and-pepper hair slicked back and cold grey eyes, inside dark gunmetal armor with a wolf-head helmet whose two red eye slits glow; when he speaks, the wolf faceplate splits open so his face and lips are visible. He wears grey leather gloves over the armor. Voice: low, slow, quiet male voice.
```

**Găng Xám** — đàn em của Sói Xám, không nói, không lộ mặt.
```text
GĂNG XÁM HENCHMEN: men in identical grey padded tactical armor with plain grey full helmets that hide their faces, and glowing grey power gauntlets that give them inhuman strength; they never speak.
```

---

## 2. Xe

Dán vào `[SETTING]` hoặc `[CHARACTERS]` khi xe có mặt. Không logo, không huy hiệu hãng, không biển số đọc được.

```text
THẮNG'S CAR: a matte-black two-door sports coupe with thin red pinstripes and black custom wheels, no badges or logos, no readable license plate.
```
```text
LAN'S CAR: a restored white compact hatchback from the 1990s with two ice-blue racing stripes, her late father's car, no badges or logos, no readable license plate.
```
```text
LAN'S MOTORBIKE: a white sport motorbike with ice-blue accents, no badges or logos, no readable license plate; anyone riding it always wears a helmet.
```
```text
HẢI'S TRUCK: a dark-orange pickup truck with a tool rack in the bed, no badges or logos, no readable license plate.
```

---

## 3. Bối cảnh cố định

**Gara Bảy — trong xưởng, ban đêm** (Tập 1)
```text
GARA BẢY AT NIGHT: a two-story car garage workshop beside a canal in Saigon: a big steel roll-up shutter facing the street, exposed brick walls stained with engine oil, one teal neon strip light and warm work lamps, walls of hanging tools, stacks of old tires, a hydraulic car lift, oil stains on the concrete floor; a steel mezzanine up a metal staircase with a long wooden dinner table and stools; an old dented metal toolbox on a high shelf; no signs, posters or readable text anywhere.
```

**Cảng container về đêm** (Tập 2, 3)
```text
THE CONTAINER PORT AT NIGHT: a container port on the Saigon river at night: long stacks of plain shipping containers in red, blue and green with no text or logos, tall gantry cranes with bright white floodlights, wet asphalt reflecting orange sodium light, puddles, a flatbed truck between the stacks, the dark river and a lit bridge in the distance; no signs or readable text.
```

**Sân thượng Gara Bảy** (Tập 3)
```text
THE ROOFTOP OF GARA BẢY: the flat rooftop of the garage at dusk with warm string lights, potted plants, a low folding table with a steaming hotpot, bowls and chopsticks, plastic stools, and a view over the canal to a big lit bridge across the river.
```

---

## 4. Khóa phong cách

Khối `[FORMAT]`, đặt ở đầu prompt Clip 1 và mọi clip mở lại bằng Ingredients:
```text
[FORMAT]
Vertical 9:16, 10-second clip, photorealistic live-action superhero action film look, as if shot on a 35mm cinema camera with subtle anamorphic lens flares: real people with natural skin texture; the armored suits look like real, high-end practical costumes of matte composite plates and metal with glowing colored light lines; energy powers are clean bright light, never fire damage or blood. Present-day Saigon, high-contrast teal-and-orange grade, neon and sodium light, wet reflections, 24fps. No guns or firearms anywhere. Spoken dialogue in Vietnamese with a natural Southern Vietnamese accent and accurate lip-sync; armored characters speak through clear visors so their lips are visible. Spoken lines are written after a colon following the speaker; they are only spoken aloud, never shown as text. Cut only where the shot list says. No subtitles, no captions, no on-screen text, no logos, no watermark.
```

Câu mở đầu mọi prompt làm bằng Frames hoặc Extend:
```text
Continue the scene seamlessly from the final frame of the previous clip, which is the first frame of this clip. Same characters, same outfits or armor, same location, same lighting and color grade. Flawless continuity, no time skip, no jump cut at the start.
Vertical 9:16, 10-second clip, same photorealistic live-action superhero film look. Spoken lines are written after a colon following the speaker; they are only spoken aloud in Vietnamese with a natural Southern accent and accurate lip-sync, never shown as text. Cut only where the shot list says. No subtitles, no captions, no on-screen text.
```

Câu chặn đặt **cuối mọi khối [AVOID]**:
```text
cartoon, anime or video-game look, plastic or toy-like armor, armor resembling any existing superhero or sentai franchise, guns, firearms, knives or any bladed weapon, blood, gore, broken bones, visible injuries, anyone killed, anyone thrown into real traffic, reckless driving among real traffic, riding a motorbike without a helmet, real car brand logos or badges, readable license plates, readable text, signs or logos, faces hidden while speaking, dialogue spoken by the wrong character, extra people in focus or speaking, distorted hands or extra fingers, subtitles.
```

---

## 5. Ảnh tham chiếu

Làm một lần trước khi dựng Tập 1, bằng công cụ tạo ảnh trong Flow (Nano Banana / Imagen), tỉ lệ **16:9** cho bảng 3 góc nhìn. Chọn ảnh giống người thật nhất; soi kỹ dấu hiệu nhận dạng (vệt tóc bạc bên trái của Thắng, lọn tóc xanh bên phải của Lan, bộ râu và vóc người của Hải, kính tròn của Khôi, sẹo cằm của Minh) và màu giáp. Tạo nhân vật trên Flow từ ảnh thường phục.

| Tên ảnh | Nội dung | Dùng ở |
| --- | --- | --- |
| `REF_THANG`, `REF_LAN`, `REF_HAI`, `REF_KHOI`, `REF_MINH` | Thường phục | Mọi tập |
| `REF_THANG_GIAP`, `REF_LAN_GIAP`, `REF_HAI_GIAP`, `REF_KHOI_GIAP`, `REF_MINH_GIAP` | Giáp | Cảnh mặc giáp (Tập 2, 3) |
| `REF_SOI_XAM`, `REF_GANG_XAM` | Phản diện, đàn em | Tập 1–3 |
| `REF_BAC_BAY` | Hologram Bác Bảy | Tập 1 |
| `REF_LOI_GIAP` | Năm lõi giáp trong hộp mút | Tập 1 |
| `REF_XE_LAN` | Xe của Lan | Tập 1, 2 |

**Năm prompt tạo năm nhân vật** (thường phục, tỉ lệ 16:9, mỗi prompt tạo 2–4 ảnh rồi chọn ảnh đẹp nhất; dùng ảnh này để tạo nhân vật trên Flow):

**REF_THANG**
```text
Character reference sheet for a photorealistic live-action action film. The same single man shown three times side by side at the same scale: front view, three-quarter view and side profile. Full body, neutral standing pose, arms relaxed, calm confident expression. A real Vietnamese man, 36 years old, about 178 cm tall, lean and strong, square jaw, calm dark eyes, light stubble, short black hair with a single silver streak at his LEFT temple, a faded burn scar on his LEFT forearm. He wears an olive-green mechanic's work jacket with the sleeves pushed up over a black T-shirt, dark work trousers, black boots, and a red shop rag hanging from his back pocket. An original face that does not resemble any real actor or celebrity. Photorealistic, natural skin texture, real fabric and leather materials, plain light-grey seamless studio background, soft even studio lighting, no text, no labels, no logos, no watermark.
```

**REF_LAN**
```text
Character reference sheet for a photorealistic live-action action film. The same single woman shown three times side by side at the same scale: front view, three-quarter view and side profile. Full body, neutral standing pose, arms relaxed, confident half smile. A real Vietnamese woman, 29 years old, about 162 cm tall, petite and athletic, sharp bright eyes, a short black bob haircut with one ice-blue streak on the RIGHT side. She wears a white leather moto jacket over a grey top, black jeans and white sneakers. An original face that does not resemble any real actor or celebrity. Photorealistic, natural skin texture, real fabric and leather materials, plain light-grey seamless studio background, soft even studio lighting, no text, no labels, no logos, no watermark.
```

**REF_HAI**
```text
Character reference sheet for a photorealistic live-action action film. The same single man shown three times side by side at the same scale: front view, three-quarter view and side profile. Full body, neutral standing pose, arms relaxed, warm friendly expression. A real Vietnamese man, 32 years old, about 188 cm tall, big and broad-shouldered, warm brown eyes, a short full black beard, hair shaved short on the sides with a short top. He wears a grey tank top under a brown leather work apron, dark cargo trousers and boots, and holds a big steel wrench in his right hand. An original face that does not resemble any real actor or celebrity. Photorealistic, natural skin texture, real fabric and leather materials, plain light-grey seamless studio background, soft even studio lighting, no text, no labels, no logos, no watermark.
```

**REF_KHOI**
```text
Character reference sheet for a photorealistic live-action action film. The same single young man shown three times side by side at the same scale: front view, three-quarter view and side profile. Full body, neutral standing pose, arms relaxed, nervous friendly grin. A real Vietnamese young man, 25 years old, about 170 cm tall, slim, round tortoiseshell glasses, messy black hair, an expressive face. He wears a mustard-yellow hoodie, black joggers, sneakers and headphones around his neck, and holds a closed laptop under one arm. An original face that does not resemble any real actor or celebrity. Photorealistic, natural skin texture, real fabric and leather materials, plain light-grey seamless studio background, soft even studio lighting, no text, no labels, no logos, no watermark.
```

**REF_MINH**
```text
Character reference sheet for a photorealistic live-action action film. The same single woman shown three times side by side at the same scale: front view, three-quarter view and side profile. Full body, neutral standing pose, arms relaxed, serious, alert expression. A real Vietnamese woman, 35 years old, about 168 cm tall, athletic, sharp straight eyebrows, serious dark eyes, a thin pale scar on her chin, black hair pulled into a tight low bun. She wears a black plain-clothes jacket over a white shirt, dark trousers and low black boots, with no badge, insignia or readable text. An original face that does not resemble any real actor or celebrity. Photorealistic, natural skin texture, real fabric and leather materials, plain light-grey seamless studio background, soft even studio lighting, no text, no labels, no logos, no watermark.
```

**Năm prompt ảnh mặc giáp** (đính kèm ảnh thường phục của chính người đó khi tạo, để giữ đúng gương mặt):

**REF_THANG_GIAP**
```text
Character reference sheet for a photorealistic live-action superhero film. The same single man as in the attached reference photo, with exactly the same face, shown three times side by side at the same scale: front view, three-quarter view and side profile. Full body, neutral standing pose, arms relaxed, calm confident expression. He wears his armor GIÁP GIÓ: a sleek red-and-black armored suit with angular wind-vent fins on the shoulders and calves and glowing red light lines, an open-face armored helmet with a clear amber visor so his whole face and the silver streak at his LEFT temple stay visible, and a glowing red hexagonal core on his LEFT wrist. The armor looks like a real, high-end practical film costume of matte composite plates and brushed metal with glowing light lines, an original design that does not resemble any existing superhero or sentai franchise. Photorealistic, natural skin texture, plain light-grey seamless studio background, soft even studio lighting, no weapons, no text, no labels, no logos, no watermark.
```

**REF_LAN_GIAP**
```text
Character reference sheet for a photorealistic live-action superhero film. The same single woman as in the attached reference photo, with exactly the same face, shown three times side by side at the same scale: front view, three-quarter view and side profile. Full body, neutral standing pose, arms relaxed, confident half smile. She wears her armor GIÁP CÁO: a slim white armored suit with ice-blue light lines and a small fox-ear crest on the helmet, an open-face armored helmet with a clear ice-blue visor so her whole face and the ice-blue streak in her hair stay visible, and a glowing white-blue hexagonal core on her LEFT wrist. The armor looks like a real, high-end practical film costume of matte composite plates and brushed metal with glowing light lines, an original design that does not resemble any existing superhero or sentai franchise. Photorealistic, natural skin texture, plain light-grey seamless studio background, soft even studio lighting, no weapons, no text, no labels, no logos, no watermark.
```

**REF_HAI_GIAP**
```text
Character reference sheet for a photorealistic live-action superhero film. The same single man as in the attached reference photo, with exactly the same face, shown three times side by side at the same scale: front view, three-quarter view and side profile. Full body, neutral standing pose, arms relaxed, warm friendly expression. He wears his armor GIÁP BÚA: heavy orange-and-gunmetal armor with thick shoulder plates and a short buffalo-horn crest on the helmet, an open-face armored helmet with a clear orange visor so his bearded face stays visible, a glowing orange hexagonal core on his LEFT wrist, and a big glowing orange energy hammer of light held in his right hand. The armor looks like a real, high-end practical film costume of matte composite plates and brushed metal with glowing light lines, an original design that does not resemble any existing superhero or sentai franchise. Photorealistic, natural skin texture, plain light-grey seamless studio background, soft even studio lighting, no weapons, no text, no labels, no logos, no watermark.
```

**REF_KHOI_GIAP**
```text
Character reference sheet for a photorealistic live-action superhero film. The same single young man as in the attached reference photo, with exactly the same face, shown three times side by side at the same scale: front view, three-quarter view and side profile. Full body, neutral standing pose, arms relaxed, nervous friendly grin. He wears his armor GIÁP BIT: a slim yellow-and-black armored suit with circuit-like light lines and two palm-sized drones docked on his shoulders, an open-face armored helmet with a clear yellow visor so his face and round glasses stay visible, and a glowing yellow hexagonal core on his LEFT wrist. The armor looks like a real, high-end practical film costume of matte composite plates and brushed metal with glowing light lines, an original design that does not resemble any existing superhero or sentai franchise. Photorealistic, natural skin texture, plain light-grey seamless studio background, soft even studio lighting, no weapons, no text, no labels, no logos, no watermark.
```

**REF_MINH_GIAP**
```text
Character reference sheet for a photorealistic live-action superhero film. The same single woman as in the attached reference photo, with exactly the same face, shown three times side by side at the same scale: front view, three-quarter view and side profile. Full body, neutral standing pose, arms relaxed, serious, alert expression. She wears her armor GIÁP KHIÊN: navy-and-silver armor with clean straight lines and a round energy shield of navy light on her left forearm, an open-face armored helmet with a clear navy visor so her face and the scar on her chin stay visible, and a glowing navy hexagonal core on her LEFT wrist. The armor looks like a real, high-end practical film costume of matte composite plates and brushed metal with glowing light lines, an original design that does not resemble any existing superhero or sentai franchise. Photorealistic, natural skin texture, plain light-grey seamless studio background, soft even studio lighting, no weapons, no text, no labels, no logos, no watermark.
```

**REF_LOI_GIAP**
```text
Photorealistic product-style photo for a live-action superhero film: an old dented metal toolbox lid open, revealing a fitted grey foam case holding five palm-sized hexagonal metal cores side by side, each glowing softly in its own color: red, white-blue, orange, yellow and navy; brushed-metal edges, fine engraved circuit lines, warm workshop light. No text, no logos, no watermark.
```

---

## 6. Danh sách tập

| Tập | Tên | Độ dài | Nội dung |
| --- | --- | :---: | --- |
| 1 | Năm chiếc lõi | 60s | Đang ăn cơm tấm thì Găng Xám xé cửa cuốn, nhấc bổng xe của Lan bằng một tay; Hải đá như đá cột điện; xe bị cướp. Thùng đồ nghề của Bác Bảy rơi bể, lộ năm lõi giáp và hologram của Bác: "Tụi con là gia đình, giữ nhau mà sống." Bốn lõi chọn bốn người; Thắng bấm lõi: "Lõi Bảy, khởi động!" |
| 2 | Lần đầu mặc giáp | 40s | Một giờ sau ở cảng: bốn chiến binh lần đầu ra trận, búa năng lượng, bóng cáo, gió đỏ, drone khóa găng; Lan lấy lại xe; Sói Xám lộ mặt trên cẩu trục; còi cảnh sát, cả nhà không chạy mà đứng chờ; Đại úy Minh bước ra trong ánh đèn |
| 3 | Chiếc lõi thứ năm | 60s | Minh chất vấn "Ai cho mấy người tự xử?"; Găng Xám đợt hai phục kích; lõi xanh thẫm trong ba lô Khôi bay ra chọn Minh; Giáp Khiên chặn đòn, khóa găng, bắt người; tối đó cả nhà mời Minh ăn lẩu trên sân thượng |
| 4–12 | Theo mạch mùa 1 trong [README.md](README.md) | 40–60s | Viết tiếp khi duyệt xong Tập 1–3 |

---

## 7. Các tập — mỗi ngày 1 tập

| Ngày | File | Tên tập |
| --- | --- | --- |
| 1 | [tap-1/](tap-1/README.md) | Năm chiếc lõi |
| 2 | [tap-2/](tap-2/README.md) | Lần đầu mặc giáp |
| 3 | [tap-3/](tap-3/README.md) | Chiếc lõi thứ năm |
