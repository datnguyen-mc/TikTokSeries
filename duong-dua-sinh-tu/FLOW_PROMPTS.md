# Khóa hình, đạo cụ và điểm nối — bản 3.1

Master 16:9 đầy khung, 24 fps. Một clip một camera setup; thoại tiếng Việt giọng miền Nam. Không đóng băng cuối clip, không tự tạo nhạc riêng từng đoạn. Nhạc và title làm trên timeline dựng.

**Cách tạo:** clip ghi CONTINUE mở bằng `Continue…`, dùng frame cuối clip trước; mọi cú cắt khác mở bằng `[FORMAT]`, đính lại các reference có mặt. Shot chỉ có người nền, không chỉ định reference, dùng text-to-video. Qua ranh giới cảnh luôn là cú cắt biên tập rõ, phù hợp runner hiện tại. Không kéo một start frame qua đổi địa điểm/tuổi/trang phục.

**Khung hình sạch, không logo đài truyền hình, không nháy ảnh thẻ nhân vật:** mọi prompt cấm logo đài hoặc kênh ở góc hình, watermark, chữ chạy tin tức, lower-third, biểu tượng LIVE/REC, đồng hồ thời gian và tuyệt đối cấm chèn/nháy ảnh thẻ tham chiếu nhân vật nền xám ở đầu hoặc cuối clip.

**Giọng người dẫn chuyện (khóa cố định):** Nữ khoảng năm mươi tuổi, giọng Nam Bộ (Sài Gòn); tông trầm ấm (alto), hơi khàn nhẹ; giọng kể điềm tĩnh, sâu lắng như người dẫn phim điện ảnh, nhịp chậm đều, khoảng ba rưỡi âm tiết mỗi giây. Không phải nhân vật trong cảnh: mọi miệng trên hình khép, không ai nhép theo lời bà.

| Nhân vật | Handle | media_id đã có |
|---|---|---|
| Tom | `@Tom` | `d83378af-6eec-499e-a17c-2a12e5764219` |
| Micdo | `@Micdo` | `317c339b-17ca-4564-934a-40987d1d50f0` |
| Ami | `@Ami` | `38ee1e43-a8ce-40ac-aff7-3f0383ccc3e4` |
| Cevin | `@Cevin` | `ccca3339-8c3a-4dd6-affc-e5b1459643b3` |
| Cina | `@Cina` | `439d9f2b-627a-4565-96b8-9bbf40826086` |
| Seja | `@Seja` | `3bb3de48-4dd3-4a90-a3ea-60be3063a7b1` |
| Onle | `@Onle` | `5a83756f-9ebb-4e2d-8ed5-89c313dc6976` |
| Ny Tran | `@NyTran` | `bdd1b074-3809-46ac-963d-7ffc1d800d7c` |
| Cela | `@Cela` | `d977c3f5-1225-4caa-8772-39b2588a71f3` |
| Nese | `@Nese` | `823abd75-2434-4f07-8812-70ed808cb67b` |
| Kinan | `@Kinan` | `ea56efae-cf13-48ad-a069-dfa421e96a36` |
| Verni | `@Verni` | `79ff8afe-97f5-4165-a602-d42d1b1a8d70` |

## Biến thể dùng cùng danh tính

- **TOM** → `@Tom`, 27 tuổi: fitted charcoal T-shirt under an open dark-blue denim work shirt, oil-scuffed dark jeans, worn brown work boots, steel chronograph watch on left wrist.
- **TOM_R** → `@Tom`, 27 tuổi: matte-black leather bomber jacket over a grey crew-neck T-shirt, dark jeans, black driving sneakers, steel chronograph watch on left wrist.
- **TOM_B** → `@Tom`, 27 tuổi: open dark-blue work shirt over charcoal T-shirt, subtle cheekbone bruise and soot smudge on jaw, dark jeans, worn work boots.
- **MICDO** → `@Micdo`, 32 tuổi: fitted white sleeveless tank top under an open black leather jacket, silver cross pendant on chain, dark jeans, heavy black boots.
- **MICDO_H** → `@Micdo`, 32 tuổi: black tactical driving windbreaker zipped over dark shirt, black leather driving gloves, dark cargo trousers, heavy boots.
- **MICDO_W** → `@Micdo`, 32 tuổi: scuffed black leather jacket over white tank top, minor forehead scrape from the rollover, bare hands, dark jeans, heavy boots.
- **AMI** → `@Ami`, 24 tuổi: fitted burgundy scoop-neck top, light-wash jeans, canvas shop apron tied at the waist, flat sneakers, silver stud earrings.
- **AMI_N** → `@Ami`, 24 tuổi: cropped tan suede jacket over burgundy top, dark jeans, sneakers, hair loose over shoulders.
- **CEVIN** → `@Cevin`, 29 tuổi: maroon short-sleeve mechanic shirt with rolled sleeves, silver chain bracelet on right wrist, dark cargo jeans, work boots.
- **CEVIN_H** → `@Cevin`, 29 tuổi: black hooded tactical vest over dark long-sleeve shirt, fingerless driving gloves, safety harness clip at waist, dark cargo pants.
- **CEVIN_W** → `@Cevin`, 29 tuổi: torn black tactical vest with a clean field compress held against his bruised side, sweat-streaked face, fingerless gloves.
- **CINA** → `@Cina`, 28 tuổi: cropped black leather vest over crimson top, low-rise dark leather trousers, heavy lace boots.
- **CINA_H** → `@Cina`, 28 tuổi: fitted black zip driving jacket, fingerless leather driving gloves, dark tactical pants, compact radio earpiece.
- **SEJA** → `@Seja`, 22 tuổi: oversized olive graphic work shirt over striped long-sleeve tee, cargo trousers, sneakers, canvas laptop strap across chest.
- **SEJA_R** → `@Seja`, 22 tuổi: white-and-blue racing windbreaker over dark tee, cargo trousers, driving shoes, thin-framed glasses.
- **ONLE** → `@Onle`, 30 tuổi: grease-stained dark-green mechanic jumpsuit tied at the waist over a black T-shirt, heavy work boots.
- **ONLE_H** → `@Onle`, 30 tuổi: dark matte bomber jacket, black cap pulled low, dark jeans, leather driving gloves.
- **NYTRAN** → `@NyTran`, 30 tuổi: tailored black snake-pattern leather jacket over open-collar crimson silk shirt, gold chain, black trousers, polished boots.
- **NYTRAN_R** → `@NyTran`, 30 tuổi: armored black motorcycle leather jacket over crimson shirt, black riding gloves, dark trousers, riding boots.
- **CELA** → `@Cela`, 31 tuổi: sleeveless black leather vest over dark shirt, dragon tattoo sleeve on right forearm, black jeans, riding boots.
- **NESE** → `@Nese`, 46 tuổi: rolled-sleeve white dress shirt with loosened dark tie, badge holder at belt, charcoal trousers, leather shoes.
- **NESE_T** → `@Nese`, 46 tuổi: dark navy police windbreaker over dress shirt, tactical vest, radio handset clipped at shoulder.
- **KINAN** → `@Kinan`, 44 tuổi: tailored dark charcoal suit over steel-blue shirt without tie, federal credential folder at side.
- **KINAN_T** → `@Kinan`, 44 tuổi: dark field windbreaker over steel-blue shirt, tactical vest, ear-tube radio.
- **VERNI** → `@Verni`, 48 tuổi: plaid flannel shirt under a padded brown work vest, trucker cap, dark jeans, heavy boots.

## Thư viện đạo cụ & Phương tiện

- **RIG_18:** Massive 18-wheel charcoal highway semi-truck and sealed silver cargo trailer hauling high-value electronics crates.
- **CIVIC_TRIO:** Three matte-black lowered sport coupes with glowing green LED underglow, sunroof hatch and reinforced front hood latches.
- **ECLIPSE:** Neon-green tuned sport coupe with carbon hood, silver sport graphics, dual NOS bottles in the rear mount and telemetry laptop on the dash.
- **RX7:** Deep-red rotary sport coupe with sleek aerodynamic body, silver twin-spoke rims and cockpit boost gauges.
- **CHARGER:** Classic 1970 matte-black muscle car with a towering chrome supercharger blower rising through the hood.
- **SUPRA_SHELL:** Rusted, dented orange sport coupe rolling shell on a flatbed tow truck before rebuild, carrying an intact twin-turbo engine block under the hood.
- **SUPRA:** Rebuilt 10-second bright metallic-orange twin-turbo sport coupe with removable targa roof and high rear wing.
- **JETTA:** Prized alpine-white tuned sport sedan with white alloy rims and custom dashboard telemetry display.
- **S2000:** Jet-black open-top roadster with concealed dual Nitrous Oxide system under the driver seat.
- **MOTO_PACK:** Matte-black high-displacement street sport motorcycles with carbon-textured fairings.
- **F150_TRUCK:** Bright-red shop pickup truck carrying wooden auto-parts crates in the rear bed.
- **HARPOON_CABLE:** Heavy-duty pneumatic steel-cable grapnel launcher and high-tensile safety tether line linking the coupe and truck cabin.
- **BREACH_CHARGE:** Compact magnetic remote latch-release module attached to the rear container door lock.
- **TUNA_SANDWICH:** White ceramic plate holding a crustless tuna sandwich and a tall glass of iced water on the Toto counter.
- **PINK_SLIP:** Official vehicle title registration certificate folded inside a clear protective sleeve.
- **NOS_BOTTLES:** Twin blue high-pressure Nitrous Oxide cylinders mounted behind the cockpit with a red steering-wheel trigger button.
- **DIAG_LAPTOP:** Ruggedized silver tuning laptop displaying engine manifold pressure curves and overload warnings without readable text.
- **CASE_FILES:** Thick manila highway-heist investigation folders, satellite route maps and customs manifests without readable text.
- **WRENCH_KIT:** Heavy chrome torque wrench, socket tray and engine hoist chains inside the garage.
- **POLICE_RADIO:** Tom's concealed LAPD encrypted tactical radio handset used for emergency medevac coordination.
- **SUPRA_KEY:** Single metal ignition key to the orange 10-second sport coupe on a steel ring.
- **CUSTOMS_INVOICE:** Stamped customs clearance ledger and legal import manifests inside Ny Tran's bonded warehouse.
