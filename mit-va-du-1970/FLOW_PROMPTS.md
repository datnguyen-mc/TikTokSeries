# Mit & Đú 1970 — Prompt Google Flow (Gemini Omni)

> Quy trình, thiết lập, lỗi thường gặp: xem [../FLOW_GUIDE.md](../FLOW_GUIDE.md)

**Định dạng:** từ Tập 13 mỗi tập **40–60s = 4–6 clip × 10s** tùy câu chuyện (Tập 1–12: 30s = 3 clip) · tạo bằng **Gemini Omni** trong Google Flow · 9:16 · thoại tiếng Việt · không chữ trên video

**Thế giới:** Miền Tây (Bến Tre – Cái Mơn) năm 1970. Cả nhà Mit là **chó nhân hóa 3D**, đi hai chân, bàn tay 4 ngón, không có con người. Tông màu hoài cổ (vàng mật ong, xanh lúa, nâu đất), hạt film nhẹ, giọng miền Tây.

**Độ dài và cấu trúc (từ Tập 13):** 40–60 giây = 4–6 clip × 10s tùy câu chuyện; tông vui vẻ, tình yêu, gia đình.

| Số clip | Khi nào | Bố cục |
| --- | --- | --- |
| 4 (40s, vừa một chuỗi Extend) | Một bối cảnh, một chuyện | 1 Mở · 2 Chuyện nhỏ · 3 Thương nhau · 4 Kết vui |
| 5 (50s) | Hai bối cảnh hoặc có một bất ngờ | 1 Mở · 2–3 Chuyện nhỏ · 4 Thương nhau · 5 Kết vui |
| 6 (60s) | Hai bước bất ngờ, hoặc nhắc lại tập cũ | 1 Mở · 2–4 Chuyện nhỏ · 5 Thương nhau · 6 Kết vui |

- **Mở:** lát cắt đời thường miền Tây 1970 có chi tiết thật (việc đồng áng, bữa cơm quê, chợ ghe, trường làng) và một câu thoại gây tò mò.
- **Chuyện nhỏ:** hiểu lầm, bất ngờ, một việc cả nhà cùng làm; mỗi clip đi thêm một bước, có cử chỉ và đồ vật đời thật.
- **Thương nhau:** lời nói giản dị, cái nắm tay, món quà nhỏ. **Kết vui:** tiếng cười hoặc cái ôm; khung thumbnail đứng yên 1 giây.
- **Từ Tập 13 (mùa vui):** gia đình đã ổn sau chặng sửa đổi; mỗi tập là một niềm vui đời thường miền Tây 1970: tát mương bắt cá, đi chợ nổi, đổ bánh xèo, thả diều, đờn ca tài tử, giỗ ông bà, Tết. Không kết bằng nước mắt hai tập liền. Trang phục mặc định: Trang phục A của cả nhà, trừ khi kịch bản ghi khác.

- **Như người thật kể chuyện nhà mình:** chi tiết đúng thời 1970 (đồ vật, món ăn, cách nói miền Tây), không dùng đồ hiện đại; mỗi clip 2–3 câu thoại, tối đa khoảng 31 âm tiết.
- **Sản phẩm** (đồ trẻ em: cặp, sách vở, bút…) xuất hiện tự nhiên trong chuyện, tối đa khoảng 10% thời lượng, lên hình chủ yếu trong một clip.

**Cách dán prompt:**
- Mỗi khối `text` bên dưới là **một lần dán** vào Flow. Dán nguyên khối, không sửa chữ.
- **FULL LOCK** dùng ở Clip 1, và cho nhân vật **xuất hiện lần đầu** ở bất kỳ clip nào từ Clip 2 trở đi (dòng `Entering in this segment:`).
- **SHORT LOCK** dùng từ Clip 2 đến clip cuối cho nhân vật đã có mặt ở clip ngay trước.
- Các khóa đã được chèn sẵn vào từng prompt, giống nhau từng chữ. Muốn đổi thiết kế nhân vật thì sửa ở mục 1, rồi dùng Find & Replace để sửa đồng loạt mọi chỗ.
- Clip 2 trở đi làm bằng **Save frame → Frames** (start frame = khung cuối clip trước), hoặc bằng **Extend** nếu Flow đã có Extend cho Gemini Omni (xem FLOW_GUIDE mục 1). Nếu Flow cho đính thêm ảnh ở chế độ Frames, đính lại ảnh tham chiếu, kể cả ảnh của nhân vật mới vào ở clip đó.

---

## 1. Khóa nhân vật (Character Bible)

**Tên nhân vật trên Flow:** `@Mit` · `@Đú` · `@Nở`. Mỗi dòng khóa của nhân vật chính bắt đầu bằng `@Tên = …`, để Flow gọi đúng nhân vật đã lưu và model hiểu tên đó là nhân vật nào trong prompt.

### Mit — người chồng

Chó cỏ Việt Nam lông vàng rơm, mõm và ngực màu kem, dáng gầy rắn rỏi, cao nhất nhà. **Dấu hiệu nhận dạng:** chóp **tai TRÁI gập xuống**.
Giọng miền Tây ấm, hơi khàn, lém lỉnh. Từng ham vui, sau biết sửa đổi.

**Trang phục A — nghèo / làm thuê** (Tập 1, 2, 5, 6, 7, 8, 9, 10, 11, 12): áo bà ba nâu đất bạc màu, quần đen xắn gối, khăn rằn quấn cổ, chân đất, ra ngoài thì đội nón lá.

FULL LOCK
```text
@Mit = Mit (husband, about 35): anthropomorphic Vietnamese native dog (chó cỏ) standing upright on two legs, lean wiry build, short golden-tan fur, cream muzzle and cream chest, upright pointed ears with the LEFT ear tip folded down (signature detail), expressive dark-brown eyes, black nose, paw-hands with four fingers. He is the tallest of the family. Outfit A: faded earth-brown áo bà ba shirt, black trousers rolled up to the knees, black-and-white checkered khăn rằn scarf knotted around the neck, barefoot, a conical nón lá hat when outdoors. Voice: warm, slightly raspy Southern Vietnamese male voice, mid-30s, playful.
```
SHORT LOCK
```text
@Mit = Mit: golden-tan native dog, cream muzzle, LEFT ear tip folded; faded earth-brown áo bà ba, black trousers rolled to the knees, checkered khăn rằn at the neck, barefoot, nón lá when outdoors; warm, slightly raspy Southern male voice.
```

**Trang phục B — phú hộ** (Tập 3, 4): sơ mi lụa trắng xắn tay, quần tây màu be, dép da, đồng hồ vàng, dây chuyền vàng to bản, tóc vuốt bóng, kính râm tròn gọng vàng.

FULL LOCK
```text
@Mit = Mit (husband, about 35): anthropomorphic Vietnamese native dog (chó cỏ) standing upright on two legs, lean wiry build, short golden-tan fur, cream muzzle and cream chest, upright pointed ears with the LEFT ear tip folded down (signature detail), expressive dark-brown eyes, black nose, paw-hands with four fingers. He is the tallest of the family. Outfit B (rich period): white silk button-up shirt with sleeves rolled to the elbows, beige pleated trousers, brown leather sandals, gold wristwatch, thick gold chain necklace, head fur slicked back and glossy, round gold-rimmed sunglasses. Voice: warm, slightly raspy Southern Vietnamese male voice, mid-30s, playful.
```
SHORT LOCK
```text
@Mit = Mit: golden-tan native dog, cream muzzle, LEFT ear tip folded, slicked glossy head fur; white silk shirt, beige trousers, gold watch, thick gold chain, round gold-rimmed sunglasses; warm, slightly raspy Southern male voice.
```

### Đú — người vợ

Chó cỏ lông trắng kem, tai màu vàng nhạt cụp nhẹ về phía trước, mặt tròn hiền, mắt nâu hình hạnh nhân, tóc búi thấp cài **trâm gỗ**. Khi giàu cô vẫn giữ cây trâm gỗ, chi tiết cho thấy cô giản dị.
Thấp hơn Mit một cái đầu. Giọng miền Tây nhỏ nhẹ, ấm áp.

**Trang phục A** (Tập 1, 2, 5, 6, 7, 8, 9, 10, 11, 12): áo bà ba tím hoa cà bạc màu, quần lãnh đen, khăn rằn vắt vai, chân đất.

FULL LOCK
```text
@Đú = Đú (wife, early 30s): anthropomorphic Vietnamese native dog standing upright on two legs, slim gentle build, creamy-white fur, soft light-tan ears that fold forward, soft round face, gentle almond-shaped brown eyes, pink-brown nose, head fur gathered in a low bun held by a plain wooden hairpin, paw-hands with four fingers. She is about a head shorter than Mit. Outfit A: faded lavender áo bà ba shirt, black satin trousers, black-and-white checkered khăn rằn draped over one shoulder, barefoot. Voice: soft, warm Southern Vietnamese female voice, early 30s, gentle.
```
SHORT LOCK
```text
@Đú = Đú: creamy-white native dog, light-tan forward-folding ears, low bun with a wooden hairpin; faded lavender áo bà ba, black satin trousers, checkered khăn rằn over one shoulder, barefoot; soft, warm Southern female voice.
```

**Trang phục B — phú hộ** (Tập 3, 4): áo dài lụa màu ngà thêu sen hồng, quần lụa trắng, bông tai ngọc trai, vẫn cài trâm gỗ.

FULL LOCK
```text
@Đú = Đú (wife, early 30s): anthropomorphic Vietnamese native dog standing upright on two legs, slim gentle build, creamy-white fur, soft light-tan ears that fold forward, soft round face, gentle almond-shaped brown eyes, pink-brown nose, head fur gathered in a low bun held by a plain wooden hairpin, paw-hands with four fingers. She is about a head shorter than Mit. Outfit B (rich period): ivory silk áo dài embroidered with pink lotus flowers, white silk trousers, small pearl earrings, the same plain wooden hairpin in her bun. Voice: soft, warm Southern Vietnamese female voice, early 30s, gentle.
```
SHORT LOCK
```text
@Đú = Đú: creamy-white native dog, light-tan forward-folding ears, low bun with a wooden hairpin, pearl earrings; ivory silk áo dài with pink lotus embroidery, white silk trousers; soft, warm Southern female voice.
```

### Nở — con gái 6 tuổi

Cún con lông kem có mảng vàng rơm, **mảng vàng quanh mắt phải**, má phúng phính, mắt nâu tròn to, hai bím tóc ngắn buộc len đỏ. Cao ngang thắt lưng Mit.
Giọng bé gái trong trẻo, lanh lảnh.

**Trang phục A** (Tập 1, 2, 5, 6, 8, 9, 10, 11, 12): áo bà ba hồng phấn, quần đùi đen, chân đất.

FULL LOCK
```text
@Nở = Nở (their daughter, 6 years old): small anthropomorphic native-dog puppy standing upright on two legs, chubby round cheeks, cream fur with golden-tan patches including a tan patch around her right eye, big round shiny brown eyes, tiny black nose, two short head-fur pigtails tied with red yarn, paw-hands with four fingers. She is only waist-high to Mit. Outfit A: pale-pink áo bà ba shirt, black shorts, barefoot. Voice: high, bright, cheerful Southern Vietnamese little-girl voice, 6 years old.
```
SHORT LOCK
```text
@Nở = Nở: small cream puppy with golden-tan patches, tan patch around her right eye, two short pigtails tied with red yarn; pale-pink áo bà ba, black shorts, barefoot; high, bright little-girl voice.
```

**Trang phục B — phú hộ** (Tập 3, 4): đầm vàng xếp bèo tay phồng, vớ trắng, giày đỏ.

FULL LOCK
```text
@Nở = Nở (their daughter, 6 years old): small anthropomorphic native-dog puppy standing upright on two legs, chubby round cheeks, cream fur with golden-tan patches including a tan patch around her right eye, big round shiny brown eyes, tiny black nose, two short head-fur pigtails tied with red yarn, paw-hands with four fingers. She is only waist-high to Mit. Outfit B (rich period): yellow frilly dress with puffed sleeves, white socks, small red shoes. Voice: high, bright, cheerful Southern Vietnamese little-girl voice, 6 years old.
```
SHORT LOCK
```text
@Nở = Nở: small cream puppy with golden-tan patches, tan patch around her right eye, two short pigtails tied with red yarn; yellow frilly dress, white socks, small red shoes; high, bright little-girl voice.
```

**Trang phục C — đồng phục đi học** (Tập 7): áo sơ mi trắng tay ngắn, quần đùi xanh đen, chân đất.

FULL LOCK
```text
@Nở = Nở (their daughter, 6 years old): small anthropomorphic native-dog puppy standing upright on two legs, chubby round cheeks, cream fur with golden-tan patches including a tan patch around her right eye, big round shiny brown eyes, tiny black nose, two short head-fur pigtails tied with red yarn, paw-hands with four fingers. She is only waist-high to Mit. School outfit: white short-sleeve button-up school shirt, navy-blue shorts, barefoot. Voice: high, bright, cheerful Southern Vietnamese little-girl voice, 6 years old.
```
SHORT LOCK
```text
@Nở = Nở: small cream puppy with golden-tan patches, tan patch around her right eye, two short pigtails tied with red yarn; white short-sleeve school shirt, navy-blue shorts, barefoot; high, bright little-girl voice.
```

### Nhân vật phụ

Mỗi nhân vật phụ chỉ có **một khóa**, dùng nguyên văn ở mọi clip.

**Con trâu** (Tập 2): trâu thật, không nhân hóa, không đứng hai chân, không nói.
```text
THE WATER BUFFALO: a real, non-anthropomorphic dark-grey water buffalo on four legs, long backward-curving horns, mud-caked legs, calm sleepy eyes; it never stands upright and never talks.
```

**Tư Mập** (Tập 4, 5): bạn nhậu thấp, bụng phệ, lông trắng đốm đen, áo đỏ in hoa vàng. Giọng ồm, hay nịnh.
```text
TƯ MẬP (Mit's drinking buddy): anthropomorphic dog standing upright on two legs, short and very fat with a round belly, white fur with large black spots, droopy jowls, flashy red shirt with a big yellow flower print unbuttoned at the top, black trousers, a cheap gold ring, paw-hands with four fingers. Voice: loud, booming, flattering male voice.
```

**Sáu Ốm** (Tập 4, 5): bạn nhậu cao gầy, lông xám, mắt lim dim gian xảo, áo xanh cổ nhọn, quần ống loe. Giọng mũi, ngọt xớt.
```text
SÁU ỐM (Mit's drinking buddy): anthropomorphic dog standing upright on two legs, very tall and skinny, grey fur, long narrow face, sly half-closed eyes, shiny green shirt with a wide pointed collar, brown flared trousers, paw-hands with four fingers. Voice: nasal, sly, sweet-talking male voice.
```

**Chủ nợ** (Tập 5): dáng bulldog, lông vằn nâu sẫm, vest xám chật, mũ phớt đen, kẹp sổ nợ, ngậm tăm. Giọng trầm, cộc lốc.
```text
CHỦ NỢ (the debt collector): anthropomorphic dog standing upright on two legs, stocky bulldog build, dark-brindle fur, heavy jowls, permanent frown, too-tight dark-grey Western suit, black fedora hat, a thick ledger book with a blank cover under one arm, a toothpick in his mouth, paw-hands with four fingers. Voice: deep, gruff male voice.
```

**Chú Năm — chủ vựa sầu riêng** (Tập 6): to con, lông nâu sô-cô-la, mõm điểm bạc, nón rơm rách vành, áo ba lỗ, quần kaki. Giọng to nhưng hiền.
```text
CHÚ NĂM (the durian wharf boss): anthropomorphic dog standing upright on two legs, big and burly, chocolate-brown fur, grey-tipped muzzle, kind wrinkled eyes, wide frayed straw hat, sleeveless white undershirt, khaki shorts, a small cloth money pouch on his belt, paw-hands with four fingers. Voice: booming but kind Southern Vietnamese male voice.
```

**Cô giáo Hai** (Tập 7): chó lớn tuổi hiền hậu, lông trắng bạc, kính gọng tròn, áo dài trắng, cầm phấn. Giọng chậm, dịu dàng.
```text
CÔ GIÁO HAI (the village teacher): gentle older anthropomorphic dog standing upright on two legs, silver-white fur, soft drooping ears, round wire-rimmed glasses, white áo dài, black trousers, a stick of white chalk in one paw, paw-hands with four fingers. Voice: calm, kind Southern Vietnamese female voice.
```

**Bà bán vé số** (Tập 10): bà cụ nhỏ người, lưng hơi còng, lông xám bạc, mắt hiền nhiều nếp nhăn, nón lá cũ, áo bà ba nâu sẫm vá khuỷu tay, túi vải đeo vai, tay cầm xấp vé số in mờ không đọc được. Giọng khàn, hiền từ.
```text
BÀ BÁN VÉ SỐ (the elderly lottery-ticket seller): gentle elderly anthropomorphic dog standing upright on two legs, small and slightly stooped, soft grey-white fur, droopy ears, kind wrinkled eyes and a warm smile, a worn conical nón lá, a faded dark-brown áo bà ba with a patched elbow, black trousers, a cloth bag slung over one shoulder, a small fan of pastel lottery tickets with blank, unreadable print in one paw, paw-hands with four fingers. Voice: kind, raspy elderly Southern Vietnamese female voice.
```

---

## 2. Bối cảnh cố định

Dán nguyên văn vào mục `[SETTING]`. Dòng `Time: ...` (giờ, ánh sáng, đạo cụ riêng của cảnh) đã được viết sẵn ngay dưới trong từng prompt.

**Nhà tre — trong nhà** (Tập 1, 5, 7, 9, 10, 11)
```text
INSIDE THE BAMBOO HUT: a small one-room hut in the 1970 Mekong Delta with woven bamboo walls whose thin gaps let in stripes of light, a nipa-palm thatch roof on bamboo rafters, a packed dirt floor, a low bamboo bed with a woven straw mat, a small low wooden table beside the bed, a kerosene lamp with a glass chimney, a large brown clay water jar by the door, a wood-fire clay stove of three clay stones with a blackened pot in the corner; poor but neat and tidy.
```

**Nhà tre — sân trước** (Tập 2, 6, 12)
```text
FRONT YARD OF THE BAMBOO HUT: a swept dirt yard in front of the small bamboo hut with its nipa-palm thatch roof and bamboo door, a large brown clay water jar beside the door, a narrow brown canal along the yard with a small wooden xuồng ba lá boat tied to a post, tall coconut palms and nipa palms leaning over the water.
```

**Ruộng lúa** (Tập 2)
```text
THE RICE PADDY: a flooded rice paddy near the family's hut, shallow muddy water reflecting the sky, freshly plowed furrows, low earthen dikes, a distant line of coconut palms, thin mist over the water, a simple wooden plow with a curved handle hitched to the water buffalo.
```

**Biệt thự phú hộ** (Tập 3, 4, 5)
```text
THE RICH VILLA: a two-story pale-yellow French-colonial villa with a red clay-tile roof, green wooden shutters and an arched veranda hung with red paper lanterns; a swept front yard with potted bonsai along the steps and a gleaming red Honda 67 motorbike; inside, dark carved wooden furniture inlaid with mother-of-pearl, a polished patterned tile floor, tall shuttered windows and a wind-up gramophone with a brass horn on a carved side table.
```

**Bến ghe sầu riêng** (Tập 6)
```text
THE DURIAN WHARF: a riverside wharf on a wide brown river with a weathered wooden plank dock, long wooden cargo boats piled high with spiky green durians, bamboo baskets and wooden shoulder poles, pyramids of durians stacked on the dock, an open tin-roof shed for shade and a lush durian orchard on the bank behind.
```

**Trường làng** (Tập 7)
```text
THE VILLAGE SCHOOL: a small single-story schoolhouse with a red clay-tile roof, whitewashed walls and open wooden window shutters, a big shady tree in the dirt yard; inside, rows of simple wooden desks and benches, a blank black chalkboard with nothing written on it, sunlight slanting through the windows with floating dust motes.
```

**Bờ kênh hoa dại** (Tập 8, 10)
```text
THE WILDFLOWER CANAL BANK: a grassy canal bank near the family's bamboo hut, purple wild mua flowers (Melastoma) and small yellow wild daisies in tall grass, clusters of purple water hyacinth floating along the canal edge, coconut palms along the water, the small thatched bamboo hut visible farther down the bank.
```

---

## 3. Khóa phong cách

Khối `[FORMAT]`, đặt ở đầu mọi prompt Clip 1:
```text
[FORMAT]
Vertical 9:16, 10-second clip, high-end 3D animated film, Pixar/Disney-quality stylized CGI, soft global illumination, shallow depth of field, 24fps, cinematic color grade. Era and place: rural Mekong Delta, southern Vietnam, 1970. Warm nostalgic palette of honey gold, rice-paddy green and earth brown, subtle 35mm film grain. Every person in this world is an anthropomorphic dog who walks upright on two legs and has paw-hands with four fingers; no humans exist. Spoken dialogue in Vietnamese with a natural Southern Vietnamese (Mekong Delta) accent and accurate lip-sync. Spoken lines are written after a colon following the speaker; they are only spoken aloud, never shown as text. Cut only where the shot list says. No subtitles, no captions, no on-screen text, no logos, no watermark.
```

Câu mở đầu mọi prompt từ Clip 2 đến clip cuối (làm bằng Frames với start frame = khung cuối clip trước, hoặc bằng Extend; clip mở bằng Ingredients thì dùng [FORMAT]):
```text
Continue the scene seamlessly from the final frame of the previous clip, which is the first frame of this clip. Same characters, same outfits, same location, same lighting and color grade. Flawless continuity, no time skip, no jump cut at the start.
Vertical 9:16, 10-second clip, same animation style. Spoken lines are written after a colon following the speaker; they are only spoken aloud in Vietnamese with a natural Southern accent and accurate lip-sync, never shown as text. Cut only where the shot list says. No subtitles, no captions, no on-screen text.
```

> Câu mở đầu dùng được cho cả Save frame → Frames lẫn Extend: dán nguyên văn, không cần sửa (xem FLOW_GUIDE mục 1).

---

## 4. Ảnh tham chiếu nhân vật

Làm **một lần duy nhất trước khi dựng tập 1**, dùng cho cả series.

1. Tạo ảnh bằng công cụ tạo ảnh trong Flow (Nano Banana / Imagen), tỉ lệ **16:9** cho bảng 4 góc nhìn.
2. Mỗi prompt tạo vài ảnh, chọn ảnh đúng mô tả nhất. Soi kỹ **tai trái gập của Mit**, **mảng vàng quanh mắt phải của Nở** và **trâm gỗ của Đú**.
3. Lưu theo tên trong bảng dưới. Đính kèm ở Clip 1 của mỗi tập.
4. Nếu Flow đọc bảng 4 góc kém khi làm tham chiếu video, cắt riêng góc chính diện hoặc góc 3/4 để đính kèm.
5. Nếu Flow giới hạn số ảnh đính kèm, ưu tiên nhân vật có mặt lâu nhất trong clip.

| Tên ảnh | Nhân vật | Dùng ở tập |
| ------- | -------- | ---------- |
| `REF_MIT_A` | Mit — trang phục A | 1, 2, 5, 6, 7, 8, 9, 10, 11, 12 |
| `REF_MIT_B` | Mit — trang phục B | 3, 4, 10 (cảnh mơ, không bắt buộc) |
| `REF_DU_A` | Đú — trang phục A | 1, 2, 5, 6, 7, 8, 9, 10, 11, 12 |
| `REF_DU_B` | Đú — trang phục B | 3, 4 |
| `REF_NO_A` | Nở — trang phục A | 1, 2, 5, 6, 8, 9, 10, 11, 12 |
| `REF_NO_B` | Nở — trang phục B | 3, 4 |
| `REF_NO_C` | Nở — đồng phục | 7 |
| `REF_LINEUP` | Cả nhà, để so tỉ lệ chiều cao | Dùng để kiểm tra, không bắt buộc đính kèm |
| `REF_TU_MAP` | Tư Mập | 4, 5 |
| `REF_SAU_OM` | Sáu Ốm | 4, 5 |
| `REF_CHU_NO` | Chủ nợ | 5 |
| `REF_CHU_NAM` | Chú Năm | 6 |
| `REF_CO_GIAO` | Cô giáo Hai | 7 |
| `REF_BA_VE_SO` | Bà bán vé số | 10 |

**Ảnh sản phẩm** (Tập 7, 9, 10, 11, 12): chụp sản phẩm thật trên nền trơn, đủ sáng, mặt trước hướng vào máy, mỗi ảnh một sản phẩm. Lưu thành `SP_CAP` (cặp), `SP_TAP` (tập vở), `SP_BUT` (bút), `SP_BUTMAU` (hộp bút màu), `SP_CAP_SACH` (cặp mới ở Tập 11), `SP_SACHTRUYEN` (sách truyện tranh) và đính kèm ở clip sản phẩm lên hình lần đầu (thường là Clip 1). Nếu clip đó làm bằng Frames mà Flow không cho đính ảnh, cho sản phẩm có sẵn trong khung cuối của clip trước đã đính ảnh, hoặc mở clip đó bằng Ingredients. Nên chọn mẫu màu trơn, ít họa tiết để hợp bối cảnh 1970. Với sách truyện, che hoặc xóa tựa và mọi chữ trên bìa trước khi tải ảnh lên, để bìa chỉ còn tranh.

**REF_MIT_A**
```text
Character turnaround sheet for a 3D animated film, high-end Pixar/Disney-quality stylized CGI. The same single character shown four times side by side at the same scale: front view, three-quarter view, side profile and back view. Full body, neutral standing pose, arms relaxed at the sides, calm friendly expression. Character: anthropomorphic Vietnamese native dog (chó cỏ) standing upright on two legs, lean wiry build, short golden-tan fur, cream muzzle and cream chest, upright pointed ears with the LEFT ear tip folded down (signature detail), expressive dark-brown eyes, black nose, paw-hands with four fingers. Outfit A: faded earth-brown áo bà ba shirt, black trousers rolled up to the knees, black-and-white checkered khăn rằn scarf knotted around the neck, barefoot, a conical nón lá hat when outdoors. Shown without the hat so both ears, including the folded LEFT ear tip, are clearly visible. Plain light-grey seamless background, soft even studio lighting, no props, no text, no labels, no numbers, no watermark.
```

**REF_MIT_B**
```text
Character turnaround sheet for a 3D animated film, high-end Pixar/Disney-quality stylized CGI. The same single character shown four times side by side at the same scale: front view, three-quarter view, side profile and back view. Full body, neutral standing pose, arms relaxed at the sides, calm friendly expression. Character: anthropomorphic Vietnamese native dog (chó cỏ) standing upright on two legs, lean wiry build, short golden-tan fur, cream muzzle and cream chest, upright pointed ears with the LEFT ear tip folded down (signature detail), expressive dark-brown eyes, black nose, paw-hands with four fingers. Outfit B (rich period): white silk button-up shirt with sleeves rolled to the elbows, beige pleated trousers, brown leather sandals, gold wristwatch, thick gold chain necklace, head fur slicked back and glossy, round gold-rimmed sunglasses. Plain light-grey seamless background, soft even studio lighting, no props, no text, no labels, no numbers, no watermark.
```

**REF_DU_A**
```text
Character turnaround sheet for a 3D animated film, high-end Pixar/Disney-quality stylized CGI. The same single character shown four times side by side at the same scale: front view, three-quarter view, side profile and back view. Full body, neutral standing pose, arms relaxed at the sides, calm friendly expression. Character: anthropomorphic Vietnamese native dog standing upright on two legs, slim gentle build, creamy-white fur, soft light-tan ears that fold forward, soft round face, gentle almond-shaped brown eyes, pink-brown nose, head fur gathered in a low bun held by a plain wooden hairpin, paw-hands with four fingers. Outfit A: faded lavender áo bà ba shirt, black satin trousers, black-and-white checkered khăn rằn draped over one shoulder, barefoot. Plain light-grey seamless background, soft even studio lighting, no props, no text, no labels, no numbers, no watermark.
```

**REF_DU_B**
```text
Character turnaround sheet for a 3D animated film, high-end Pixar/Disney-quality stylized CGI. The same single character shown four times side by side at the same scale: front view, three-quarter view, side profile and back view. Full body, neutral standing pose, arms relaxed at the sides, calm friendly expression. Character: anthropomorphic Vietnamese native dog standing upright on two legs, slim gentle build, creamy-white fur, soft light-tan ears that fold forward, soft round face, gentle almond-shaped brown eyes, pink-brown nose, head fur gathered in a low bun held by a plain wooden hairpin, paw-hands with four fingers. Outfit B (rich period): ivory silk áo dài embroidered with pink lotus flowers, white silk trousers, small pearl earrings, the same plain wooden hairpin in her bun. Plain light-grey seamless background, soft even studio lighting, no props, no text, no labels, no numbers, no watermark.
```

**REF_NO_A**
```text
Character turnaround sheet for a 3D animated film, high-end Pixar/Disney-quality stylized CGI. The same single character shown four times side by side at the same scale: front view, three-quarter view, side profile and back view. Full body, neutral standing pose, arms relaxed at the sides, calm friendly expression. Character: small anthropomorphic native-dog puppy standing upright on two legs, chubby round cheeks, cream fur with golden-tan patches including a tan patch around her right eye, big round shiny brown eyes, tiny black nose, two short head-fur pigtails tied with red yarn, paw-hands with four fingers. Outfit A: pale-pink áo bà ba shirt, black shorts, barefoot. Plain light-grey seamless background, soft even studio lighting, no props, no text, no labels, no numbers, no watermark.
```

**REF_NO_B**
```text
Character turnaround sheet for a 3D animated film, high-end Pixar/Disney-quality stylized CGI. The same single character shown four times side by side at the same scale: front view, three-quarter view, side profile and back view. Full body, neutral standing pose, arms relaxed at the sides, calm friendly expression. Character: small anthropomorphic native-dog puppy standing upright on two legs, chubby round cheeks, cream fur with golden-tan patches including a tan patch around her right eye, big round shiny brown eyes, tiny black nose, two short head-fur pigtails tied with red yarn, paw-hands with four fingers. Outfit B (rich period): yellow frilly dress with puffed sleeves, white socks, small red shoes. Plain light-grey seamless background, soft even studio lighting, no props, no text, no labels, no numbers, no watermark.
```

**REF_NO_C**
```text
Character turnaround sheet for a 3D animated film, high-end Pixar/Disney-quality stylized CGI. The same single character shown four times side by side at the same scale: front view, three-quarter view, side profile and back view. Full body, neutral standing pose, arms relaxed at the sides, calm friendly expression. Character: small anthropomorphic native-dog puppy standing upright on two legs, chubby round cheeks, cream fur with golden-tan patches including a tan patch around her right eye, big round shiny brown eyes, tiny black nose, two short head-fur pigtails tied with red yarn, paw-hands with four fingers. School outfit: white short-sleeve button-up school shirt, navy-blue shorts, barefoot. Plain light-grey seamless background, soft even studio lighting, no props, no text, no labels, no numbers, no watermark.
```

**REF_LINEUP** (cả nhà đứng cạnh nhau)
```text
Height reference lineup for a 3D animated film, high-end Pixar/Disney-quality stylized CGI. A family of three anthropomorphic dogs standing side by side on the same ground line, full body, front view, relaxed friendly expressions. Left, the father: anthropomorphic Vietnamese native dog (chó cỏ) standing upright on two legs, lean wiry build, short golden-tan fur, cream muzzle and cream chest, upright pointed ears with the LEFT ear tip folded down (signature detail), expressive dark-brown eyes, black nose, paw-hands with four fingers. Outfit A: faded earth-brown áo bà ba shirt, black trousers rolled up to the knees, black-and-white checkered khăn rằn scarf knotted around the neck, barefoot, a conical nón lá hat when outdoors. No hat. Middle, the 6-year-old daughter, only waist-high to her father: small anthropomorphic native-dog puppy standing upright on two legs, chubby round cheeks, cream fur with golden-tan patches including a tan patch around her right eye, big round shiny brown eyes, tiny black nose, two short head-fur pigtails tied with red yarn, paw-hands with four fingers. Outfit A: pale-pink áo bà ba shirt, black shorts, barefoot. Right, the mother, about a head shorter than the father: anthropomorphic Vietnamese native dog standing upright on two legs, slim gentle build, creamy-white fur, soft light-tan ears that fold forward, soft round face, gentle almond-shaped brown eyes, pink-brown nose, head fur gathered in a low bun held by a plain wooden hairpin, paw-hands with four fingers. Outfit A: faded lavender áo bà ba shirt, black satin trousers, black-and-white checkered khăn rằn draped over one shoulder, barefoot. Plain light-grey seamless background, soft even studio lighting, no text, no labels, no height chart, no numbers, no watermark.
```

**REF_TU_MAP**
```text
Character turnaround sheet for a 3D animated film, high-end Pixar/Disney-quality stylized CGI. The same single character shown four times side by side at the same scale: front view, three-quarter view, side profile and back view. Full body, neutral standing pose, arms relaxed at the sides, calm friendly expression. Character: anthropomorphic dog standing upright on two legs, short and very fat with a round belly, white fur with large black spots, droopy jowls, flashy red shirt with a big yellow flower print unbuttoned at the top, black trousers, a cheap gold ring, paw-hands with four fingers. Plain light-grey seamless background, soft even studio lighting, no props, no text, no labels, no numbers, no watermark.
```

**REF_SAU_OM**
```text
Character turnaround sheet for a 3D animated film, high-end Pixar/Disney-quality stylized CGI. The same single character shown four times side by side at the same scale: front view, three-quarter view, side profile and back view. Full body, neutral standing pose, arms relaxed at the sides, calm friendly expression. Character: anthropomorphic dog standing upright on two legs, very tall and skinny, grey fur, long narrow face, sly half-closed eyes, shiny green shirt with a wide pointed collar, brown flared trousers, paw-hands with four fingers. Plain light-grey seamless background, soft even studio lighting, no props, no text, no labels, no numbers, no watermark.
```

**REF_CHU_NO**
```text
Character turnaround sheet for a 3D animated film, high-end Pixar/Disney-quality stylized CGI. The same single character shown four times side by side at the same scale: front view, three-quarter view, side profile and back view. Full body, neutral standing pose, arms relaxed at the sides, calm friendly expression. Character: anthropomorphic dog standing upright on two legs, stocky bulldog build, dark-brindle fur, heavy jowls, permanent frown, too-tight dark-grey Western suit, black fedora hat, a thick ledger book with a blank cover under one arm, a toothpick in his mouth, paw-hands with four fingers. Plain light-grey seamless background, soft even studio lighting, no props, no text, no labels, no numbers, no watermark.
```

**REF_CHU_NAM**
```text
Character turnaround sheet for a 3D animated film, high-end Pixar/Disney-quality stylized CGI. The same single character shown four times side by side at the same scale: front view, three-quarter view, side profile and back view. Full body, neutral standing pose, arms relaxed at the sides, calm friendly expression. Character: anthropomorphic dog standing upright on two legs, big and burly, chocolate-brown fur, grey-tipped muzzle, kind wrinkled eyes, wide frayed straw hat, sleeveless white undershirt, khaki shorts, a small cloth money pouch on his belt, paw-hands with four fingers. Plain light-grey seamless background, soft even studio lighting, no props, no text, no labels, no numbers, no watermark.
```

**REF_CO_GIAO**
```text
Character turnaround sheet for a 3D animated film, high-end Pixar/Disney-quality stylized CGI. The same single character shown four times side by side at the same scale: front view, three-quarter view, side profile and back view. Full body, neutral standing pose, arms relaxed at the sides, calm friendly expression. Character: gentle older anthropomorphic dog standing upright on two legs, silver-white fur, soft drooping ears, round wire-rimmed glasses, white áo dài, black trousers, a stick of white chalk in one paw, paw-hands with four fingers. Plain light-grey seamless background, soft even studio lighting, no props, no text, no labels, no numbers, no watermark.
```

**REF_BA_VE_SO**
```text
Character turnaround sheet for a 3D animated film, high-end Pixar/Disney-quality stylized CGI. The same single character shown four times side by side at the same scale: front view, three-quarter view, side profile and back view. Full body, neutral standing pose, arms relaxed at the sides, calm friendly expression. Character: gentle elderly anthropomorphic dog standing upright on two legs, small and slightly stooped, soft grey-white fur, droopy ears, kind wrinkled eyes and a warm smile, a worn conical nón lá, a faded dark-brown áo bà ba with a patched elbow, black trousers, a cloth bag slung over one shoulder, a small fan of pastel lottery tickets with blank, unreadable print in one paw, paw-hands with four fingers.. Plain light-grey seamless background, soft even studio lighting, no props, no text, no labels, no numbers, no watermark.
```

---

## 5. Danh sách tập

| Tập | Tên | Nội dung | Sản phẩm |
| --- | --- | -------- | -------- |
| 1 | Nhà tre nghèo | Nồi cơm toàn khoai lang; Nở tập viết bằng que trên nền đất vì không có tập; Mit hứa sẽ làm giàu | Gợi nhu cầu: Nở chưa có tập vở |
| 2 | Kho báu dưới ruộng | Lưỡi cày vướng hũ sành đầy vàng; Mit chạy về khoe; Đú làm rơi rổ rau | — |
| 3 | Phú hộ | Honda 67, biệt thự, máy hát; Đú dặn "giàu rồi nhớ giữ"; Mit cười lớn, tung tiền | — |
| 4 | Ham vui phung phí | Tiệc với Tư Mập, Sáu Ốm; mua "gà vàng phong thủy"; Nở ôm gối chờ ba; Đú khóc bên cửa sổ | — |
| 5 | Trắng tay | Chủ nợ khiêng đồ; bạn nhậu làm ngơ; dầm mưa về nhà tre; "Còn nhau là còn tất cả" | — |
| 6 | Khuân sầu riêng | Mit làm thuê ở bến ghe, bị gai chích; nhận tiền công đầu tiên; mua bánh bò cho Nở | — |
| 7 | Ngày đầu đi học | Đú ủi áo bằng bàn ủi than; Mit tặng cặp, tập, bút mới; Nở viết chữ đầu tiên | **Cặp, tập vở, bút** |
| 8 | Bó hoa dại 20/10 | Mit và Nở hái hoa dại tặng Đú; Đú bật khóc hạnh phúc; cả nhà dưới hoàng hôn | — |
| 9 | Nở dạy ba học chữ | Nở làm cô giáo nhỏ dạy ba cầm bút; chữ ba "như gà bới"; chữ đầu tiên Mit viết là tên Đú; Đú rưng rưng "Chữ đẹp nhất đời em đó" | **Tập vở, bút** |
| 10 | Vé số độc đắc | ⚡ Trend jackpot: đi làm về, Mit bị rao "trúng độc đắc giàu to", mơ lại thành phú hộ rồi tỉnh: "Giàu nhờ hên xui… mất một lần rồi"; mua hộp bút màu cho Nở; bà cụ: "Thương con vậy là trúng độc đắc rồi!"; Mit: "Độc đắc của ba là đây nè" | **Hộp bút màu** |
| 11 | Chiếc cặp mới của Nở | Sáng sớm Nở gói tập và hộp bút màu vào tấm khăn vải cũ; Mit tặng chiếc cặp mới; cả nhà nắm tay dắt Nở tới trường dọc bờ kênh: "Chữ của con là tương lai của cả nhà mình." | **Cặp sách** |
| 12 | Chuyện cổ tích của ba | 🌕 Đêm rằm tháng Chín: Nở ôm gối chờ ba kể chuyện như ở Tập 4; Mit đánh vần cuốn sách cô Hai thưởng chậm rì, rồi kể "chuyện anh khờ cày trúng hũ vàng" (chính đời mình); Nở: "Anh khờ đó… giống ba ghê!"; Mit: "Ờ… mà ảnh còn vợ, còn con"; Nở thiếp đi: "Vậy là còn tất cả…" | **Sách truyện tranh** |

> 💡 Tập 8 đứng độc lập được. Có thể dựng trước để đăng đúng dịp 20/10.

---

## 6. Các tập — mỗi ngày 1 tập

Mỗi tập (từ Tập 13: 40–60s = 4–6 clip × 10s; Tập 1–12: 30s = 3 clip) là một ngày đăng, nằm trong thư mục riêng `tap-{số}/` cùng thư mục này: `README.md` là tổng quan tập, `clip-1.md` … `clip-N.md` (4–6 file; Tập 1–12: `clip-1.md` … `clip-3.md`) là prompt của từng clip 10 giây. Tập mới đánh số tiếp (`tap-13/`, …) và dùng nguyên các khóa ở mục 1–3.

| Ngày | File | Tên tập |
| --- | --- | --- |
| 1 | [tap-1/](tap-1/README.md) | Nhà tre nghèo |
| 2 | [tap-2/](tap-2/README.md) | Kho báu dưới ruộng |
| 3 | [tap-3/](tap-3/README.md) | Phú hộ |
| 4 | [tap-4/](tap-4/README.md) | Ham vui phung phí |
| 5 | [tap-5/](tap-5/README.md) | Trắng tay |
| 6 | [tap-6/](tap-6/README.md) | Khuân sầu riêng |
| 7 | [tap-7/](tap-7/README.md) | Ngày đầu đi học của Nở |
| 8 | [tap-8/](tap-8/README.md) | Bó hoa dại 20/10 |
| 9 | [tap-9/](tap-9/README.md) | Nở dạy ba học chữ |
| 10 | [tap-10/](tap-10/README.md) | Vé số độc đắc |
| 11 | [tap-11/](tap-11/README.md) | Chiếc cặp mới của Nở |
| 12 | [tap-12/](tap-12/README.md) | Chuyện cổ tích của ba |
