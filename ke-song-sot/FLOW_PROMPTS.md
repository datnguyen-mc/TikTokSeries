# Khóa hình, đạo cụ và điểm nối — bản 3.1

Master 16:9 đầy khung, 24 fps. Một clip một camera setup; thoại tiếng Việt giọng miền Nam. Không đóng băng cuối clip, không tự tạo nhạc riêng từng đoạn. Nhạc và title làm trên timeline dựng.

**Cách tạo:** clip ghi CONTINUE mở bằng `Continue…`, dùng frame cuối clip trước; mọi cú cắt khác mở bằng `[FORMAT]`, đính lại các reference có mặt. Shot chỉ có người nền, không chỉ định reference, dùng text-to-video. Qua ranh giới cảnh luôn là cú cắt biên tập rõ, phù hợp runner hiện tại. Không kéo một start frame qua đổi địa điểm/tuổi/trang phục.

**Giọng ngoài hình:** chỉ khai báo giọng, không thêm người vào ảnh. Tag đứng ở trường người nói; không chèn tag hoặc thay tên bên trong câu được đọc.

**Khung hình sạch, không logo đài truyền hình:** mọi prompt cấm logo đài hoặc kênh ở góc hình, watermark, chữ chạy tin tức, lower-third (dải tên), biểu tượng LIVE/REC, đồng hồ thời gian và mọi đồ họa trên hình. Màn hình máy tính, điện thoại trong truyện không hiện kênh, bản tin hay thương hiệu đài; biểu tượng hãng tàu chỉ là hình đơn giản không đọc được. Dữ liệu cảnh không dùng chữ TV/tin tức/truyền hình để model không dựng thành bản tin, và validator chặn các chữ này. Khi duyệt render, soi bốn góc khung: thấy logo hoặc chữ thì tạo lại clip đó.

**Giọng người dẫn chuyện (khóa cố định):** Nữ khoảng năm mươi tuổi, giọng Nam Bộ (Sài Gòn); tông trầm ấm (alto), hơi khàn nhẹ; giọng kể điềm tĩnh, sâu lắng như người dẫn phim điện ảnh, không vui tươi, không kịch, không kiểu quảng cáo phim; nhịp chậm đều, khoảng ba rưỡi âm tiết mỗi giây, ngắt nhẹ ở mỗi dấu phẩy và dấu chấm; phát âm mềm và rõ; thu gần, khô, không vang phòng, không nhạc nền. Không phải nhân vật trong cảnh: mọi miệng trên hình khép, không ai nhép theo lời bà. Bộ biên dịch in nguyên văn bản tiếng Anh của khóa này vào cả bảy clip giới thiệu. Nếu Flow cho tạo `@Voice`, lưu một giọng tên NguoiKe theo đúng mô tả trên và gắn cho cả bảy clip.

**Người dẫn chuyện giới thiệu nhân vật:** khi một trong chín nhân vật chính lần đầu xuất hiện trên hình, người dẫn chuyện (giọng đã khóa ở trên, không phải nhân vật) giới thiệu ngắn tên và vai trò ở ngôi thứ ba, đúng nhịp nhân vật ra hình. Không giới thiệu lại khi đổi tuổi hoặc trang phục, không giới thiệu người không tên. Validator bắt buộc đủ chín lời giới thiệu và chặn người dẫn chuyện ở mọi clip khác. Nếu giọng dẫn lệch giữa các clip, lồng lại chín câu này bằng cùng một giọng khi dựng.

**Chuẩn cơ thể, khẩu hình, mắt mũi (in vào mọi prompt):** cúi nhặt đồ thì khuỵu gối và hông, tay được ghi nắm trọn rồi nhấc có sức nặng; đồ không tự bay, không tự trượt vào tay, không xuyên qua ngón; câu không ghi tay thì dùng tay đang rảnh, đồ đang cầm giữ nguyên tay; trao đồ thì thấy đủ hai bàn tay tới khi người nhận nắm chắc; chân không trượt, mỗi bàn tay đủ năm ngón. Bản đồ miệng sinh tự động từ mốc giây của thoại: chỉ người đang nói trong khung giây của mình mới nhép môi theo đúng từng âm tiết, ngoài các khung đó mọi miệng khép; lời dẫn và người dẫn chuyện thì không ai nhép. Mặt khớp ảnh tham chiếu suốt cảnh, không nháy ảnh thẻ nền xám ở đầu hoặc cuối clip.

**Thoại đi cùng chuyển động:** mỗi câu có khung giây riêng trùng nhịp hành động đang diễn ra, không chồng nhau, tối đa 4,5 âm tiết mỗi giây và 30 âm tiết mỗi clip. Đổi mốc nhịp trong ACTION thì sửa khung giây của câu tương ứng.

| Nhân vật | Handle | media_id đã có |
|---|---|---|
| Sơn | `@Son` | `28356180-dea1-4c6c-bd80-8c3a41106957` |
| Mây | `@May` | `b210621a-c403-42cb-94d5-8c0024496843` |
| Hạ | `@Ha` | `61e353d9-8e8a-48b1-934e-2f466ab87d09` |
| Bà Hai | `@HaiNgoc` | `ff423460-c3ce-4d3f-8c4b-f74d2a657a2f` |
| Dũng | `@Dũng` | `29967c42-6378-4e6e-a656-101fbda18b0b` |
| Kiên | `@Vũ Kiên` | `cb559421-6180-43b2-bf78-ecc674c3b698` |
| Thành | `@Phó Thành` | `80289d04-f26d-4ac0-892b-5515509ea1fb` |
| Bác sĩ Linh | `@Bác sĩ Linh` | `d51873af-f5d5-48cd-844e-7d6fc9bf99a7` |
| Ông Bảy | `@Ông Bảy` | `eefba81d-07c5-42a5-bfe3-11bc176c6d4c` |

## Biến thể dùng cùng danh tính

Các UUID trên là reference danh tính đã có, không phải xác nhận rằng mọi ảnh biến thể đã được tạo. Trước khi render, kiểm tra ảnh đúng tuổi/trang phục, đặc biệt Sơn 20 tuổi, Bà Hai 35 tuổi và các giai đoạn nhiều năm sau. Không tạo thêm nhân vật mới cho mỗi bộ đồ.

- **SON** → `@Son`, 45 tuổi: cropped hair greying at the temples, faded olive field jacket over grey henley shirt, dark cargo trousers, worn brown leather boots, bare hands, carrying his weathered dark-olive canvas backpack with thick shoulder straps when traveling.
- **SON_P** → `@Son`, 45 tuổi: recent past, cropped greying hair, tailored matte-black suit, open-collar white shirt, black leather gloves, polished black shoes, concealed underarm leather holster.
- **SON_S** → `@Son`, 45 tuổi: present timeline, matte-black suit, open-collar white shirt, BARE hands, no gloves, no flower in breast pocket.
- **SON_Y** → `@Son`, 20 tuổi: distant past age 20, black hair without grey, rain-damp plain dark shirt and worn dark trousers, BARE hands.
- **SON_Y_S** → `@Son`, 20 tuổi: distant past age 20, black hair without grey, plain black suit, bare hands before first doorway, new black leather gloves kept in pocket until the exit.
- **SON_O** → `@Son`, 65 tuổi: later years age 65, older weathered hands, faded olive field jacket, weathered dark-olive canvas backpack slung over left shoulder, bare hands, frame below shoulders only without a face reveal.
- **MAY** → `@May`, 38 tuổi: plain khaki shirt with rolled sleeves, dark trousers, no readable insignia, small black investigation notebook and pen, discreet dark-brown leather crossbody duty pouch, steel handcuffs at belt.
- **MAY_C** → `@May`, 38 tuổi: dark-blue denim jacket over charcoal T-shirt, dark jeans, sneakers, compact black tactical daypack/backpack over shoulders, no uniform shirt visible.
- **MAY_O** → `@May`, 58 tuổi: older face age 58, more silver in the same short haircut, plain khaki shirt, dark trousers, ordinary motorcycle helmet held at her side when specified.
- **HA** → `@Ha`, 32 tuổi: cream linen dress, forest-green florist apron with pocket shears, intact long pale-blue silk scarf at neck, silver hair clip pinned at back of hair, flat sandals.
- **HA_D** → `@Ha`, 32 tuổi: plain grey cotton dress, loose untidy hair with silver hair clip pinned at back until 45.4, thin sandals, scarf absent from neck, no visible injury.
- **HA_R** → `@Ha`, 32 tuổi: same grey cotton dress and thin sandals after rescue, recovered long torn pale-blue silk scarf draped warmly over shoulders, no white blouse or jeans yet.
- **HA_N** → `@Ha`, 32 tuổi: after a stated clothing change at the station, borrowed clean white blouse, blue jeans, flat sandals, long pale-blue silk scarf carried or worn.
- **HA_O** → `@Ha`, 52 tuổi: older face age 52, long hair with a little grey tied back, cream work blouse, forest-green florist apron, the same pale-blue silk scarf.
- **HAINGOC** → `@HaiNgoc`, 60 tuổi: silver hair in a tight bun, deep-violet silk áo bà ba, black silk trousers, embroidered slippers, jade bracelet on LEFT wrist until 49.3, unlit black holder in fingers.
- **HAINGOC_Y** → `@HaiNgoc`, 35 tuổi: distant past age 35, black hair in the same tight bun, simpler violet áo bà ba, black trousers, green jade bracelet on LEFT wrist.
- **DUNG** → `@Dũng`, 35 tuổi: black sleeveless shirt, black jeans, heavy boots, nail-shaped silver earring in LEFT ear, heavy black canvas shoulder bag for work gear.
- **KIEN** → `@Vũ Kiên`, 50 tuổi: tailored white suit, luxury gold wristwatch on left wrist, polished shoes, clothing becomes rumpled during flight to lighthouse.
- **THANH** → `@Phó Thành`, 26 tuổi: plain light-blue shirt, dark trousers, round glasses, no readable insignia, leather evidence folder and compact police radio.
- **LINH** → `@Bác sĩ Linh`, 55 tuổi: worn white doctor coat over checked shirt, stethoscope around neck, practical canvas medical response bag.
- **BAY** → `@Ông Bảy`, 70 tuổi: white cotton singlet, dark shorts, rubber sandals, conical hat outside, checkered cloth over shoulder for cleaning coffee glasses.
- **BAY_O** → `@Ông Bảy`, 90 tuổi: much older face and hands at age 90, same white moustache, white singlet, shorts, working steadily behind the coffee counter with a clean glass cloth.

## Quy tắc liên tục đã chốt

- Đồng hồ duy nhất: Hạ tặng ở 06.5, hỏng do va đập ở 08.4; Sơn không mở trước 52.2. Ảnh Mây nhận ra ở 14 là ảnh rời. Mây giữ từ 34.4 tới 45.5, sau đó trả Sơn. Không có chiếc thứ hai ở cảnh cuối.
- Khăn duy nhất bị xé: mảnh ngắn Sơn nhặt ở 10, phần dài Dũng để lại ở 18. Cả hai về Mây ở 34.3; phần dài trả Hạ ở 52.5. Không dùng khăn bất ngờ để trói Kiên.
- Sổ đen/USB gốc giữ ở đồn sau 17.1; sổ đỏ/token theo chuyến thành phố. Bản gốc giao điều tra ở 34.5. Sơn chỉ mang phong bì bản sao tới cảng.
- Sơn áo ô liu ở hiện tại đầu phim, vest tay trần ở 21.5–27 và 35–55. Hồi tưởng vẫn đúng biến thể riêng. Băng cổ tay TRÁI từ 25.1; tay phải không bị thương. Không cài hoa trong cao trào hiện tại.
- Hạ váy xám đến hết 53, nhận lại khăn ở 52.5, thay đồ trắng/jean tại đồn trước 54.1. Trang phục sau cứu không tự đổi ngay khi thoát khỏi Kiên.
- Mây dùng đúng hai còng trong chuyến thành phố: 23.5 và 24.5. Còng Dũng bị cắt xích ở 24.6, không biến thành còng dùng lại được. Mây nhận hai còng mới ở 35.1; một giữ Dũng, một giữ Sơn. Tổ hỗ trợ giữ Kiên bằng còng của họ.
- Vũ khí của Sơn được giao toàn bộ cho Mây ở 28.4. Anh không mang súng ở cảng/hải đăng. Súng Kiên được thu làm vật chứng, không bị ném xuống biển.
- Tê là chất hư cấu, gây bất động còn thở, thời gian hồi phục không cố định. Không dùng làm giả chết, không có mốc 38/40 phút hoặc chỉ dẫn áp dụng thực tế. Phản diện biết đúng thuốc của chúng.
- Bảy vạch: 01→1; 07→2; 12→3; 19→4; 28.5 bù hai ngày đi thành phố→6; 34.1→7. Hạ không bắt đầu một dãy đếm tù mới ở kết phim.
- Hải đăng: cửa chính phía đông; cửa kỹ thuật bắc; lan can biển phía nam. Mây thử đèn ở 16.5, Hạ giữ cửa bằng kẹp ở 45.4, tổ hỗ trợ vào ở 48.5, bật đèn theo lệnh ở 51.1.

## Thư viện đạo cụ

- **WATCH:** ONE silver pocket watch, engraved flower on closed lid, same chain throughout. No second matching watch.
- **WATCH_OPEN:** The SAME watch OPEN for the first time at 52.2; cracked glass, small photo of Hạ inside lid, hands stopped until 52.3.
- **PHOTO:** Loose wallet photograph of Hạ, physically separate from the still-closed pocket watch.
- **KIEN_PHOTO:** Photograph of Kiên in white suit with a hand-drawn building sketch on its back; no legible words.
- **BLACK_BOOK:** Original BLACK leather ledger, receipt and original USB initially fixed inside back cover.
- **RED_BOOK:** Original RED cloth ledger, handwritten signature shapes, distinct from black leather ledger.
- **RED_COPY:** COPY of red-ledger pages: one loose copied page folded into Sơn's jacket at 31.4, then the copies kept in a plain envelope from 34.2. Originals are with the investigator after 34.5.
- **USB:** Original USB from black ledger, preserved in an evidence sleeve at the station after 17.1.
- **USB_COPY:** Separate working USB copy of the original, used with the borrowed laptop. Original stays in evidence.
- **TOKEN:** USB-shaped hardware security token from the safe; NOT the metal door key.
- **RECEIPT:** Dispatch receipt with seven dated boxes and a ship stamp, no readable generated text.
- **TIN:** Dented fitted tin containing three sealed fictional Tê vials, no opening or use instructions.
- **VIAL:** Fictional Tê device or sealed vial associated with the attackers. No real substance, dose or application technique.
- **VIAL_SAMPLE:** ONE unopened sample carton filmed on its original shelf, then sealed as evidence; no recipe or usable label.
- **SCARF:** One long pale-blue silk scarf, intact in the past before abduction.
- **SCARF_FRAGMENT:** Short torn end of Hạ scarf, recovered by Sơn at the latch, later sealed with Mây. Not a full scarf.
- **SCARF_REMAINDER:** Long remaining section of the SAME scarf, matching torn edge; given by Dũng to Mây, returned to Hạ at 52.5.
- **MARKS:** Exactly one tally per story day at cabin frame: 1 at scene 1, 2 at 7, 3 at 12, 4 at 19, 6 after 28.5, 7 after 34.1.
- **GUN_CASE:** Locked handgun case, no discharge. Sơn transfers complete case and key to Mây at 28.4 and remains unarmed thereafter.
- **GLOVES:** One pair of black gloves first gifted twenty-five years ago; present-day pair folded into the open backpack on the cabin cot at 35.4; the bag is zipped shut at 38.6.
- **HAIRCLIP:** Hạ silver hair clip, deliberately wedged into service-hatch latch at 45.4, recovered at 48.5 and logged at 54.5.
- **LILY:** One white lily from Hạ family-home vase, wrapped at 57.5 and held at the public walkway during departure.
- **BACKPACK:** Sơn's weathered dark-olive canvas backpack with thick shoulder straps and brass zipper (carries his ledger, sealed tin, locked case and spare clothes during travel; left on the cabin cot at 35.4/38.6 before the harbour exchange, and carried again on his return at 60.4).
- **DUTY_POUCH:** Mây's discreet dark-brown leather crossbody duty pouch, small black field notebook, pen and compact police radio.
- **DAYPACK:** Mây's compact black tactical daypack/backpack worn over her denim jacket during the city & river-factory mission (Scenes 19.5–27.6), holding evidence sleeves and borrowed tools.
- **CUFFS:** Standard steel police handcuffs carried by Mây (two pairs used in the city at 23.5 and 24.5; two fresh pairs issued by Thành at 35.1 and used at 46.4 and 53.3).
- **TOOL_BAG:** Dũng's heavy black canvas shoulder work bag strapped across his torso, used to carry field restraint gear and the Tê applicator.
- **MED_BAG:** Bác sĩ Linh's practical canvas emergency medical bag and stethoscope with airway/breathing-support kit (no miracle antidote syringe).
- **CLIPBOARD:** Phó Thành's dark leather evidence folder, witness statement pad, pen and police radio handset.
- **COFFEE_TRAY:** Ông Bảy's traditional Vietnamese iced-coffee glasses, metal phin filter, checkered wiping towel and plastic fish-market crate/tray.
- **KIEN_GUN:** Kiên's compact black handgun, always held low in his LEFT hand with the muzzle toward the floor while his right hand grips Hạ or the hatch; never fired, no muzzle flash; dropped at 51.3 and lifted by the grip into an evidence bag by Mây at 51.5, never thrown into the sea.
- **HOUSE_KEY:** Old brass key of Hạ's family house by the harbour, kept by Mây in her duty pouch until she lays it on the station table at 54.6; Hạ's own key afterwards.
- **MAY_FOLDER:** Mây's own thin grey card investigation folder, held by her alone; never confused with Thành's dark leather evidence folder.

## Âm thanh và bản dọc

Giữ cùng giọng cho mỗi danh tính. J/L-cut thực hiện trên timeline bằng các track ambience tách rời; không yêu cầu model tạo hai địa điểm trong một clip. Dùng một bộ ambience xuyên cảnh, không reset nhạc ở mỗi mười giây. Với 40–43, làm reframe dọc riêng vì crop giữa sẽ mất một phe và con tin.

Sau render, xem từng cặp clip và các ranh giới cảnh. Nếu có frame đệm lặp thì trim đúng phần đệm, không cắt mất động tác. Không kéo dài tĩnh để ép bản dựng thành đúng 60:00.
