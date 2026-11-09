> Ghi chú 09/11/2026: phim đổi tên thành "Cái Kết Cho Tiểu Tam" và chuyển sang 4 clip × 15s mỗi cảnh (Omni 1.2); dàn ý dưới đây là bản 6 × 10s cũ.
> Ghi chú 08/11/2026: nguồn chính thức là `../PHAN_CANH_OMNI.json` (đã thêm `speech_start` cho clip thoại nối liền; phim đã chuyển 100% sang thoại nhân vật nên lời ở đây là bản nháp cũ).

# Cái Kết Cho Tiểu Tam (tên cũ: Vợ Tào Khang) — dàn ý clip (nguồn cho người viết JSON)

25 cảnh × 6 clip × 10s = 25 phút. Hà Nội hôm nay. Mỗi clip: `[chars] | speaker | lời nháp | hình ảnh`.
`cont` = nối tiếp liền mạch (chỉ hợp lệ khi chars ⊆ chars clip trước, không rỗng, cùng setting). Còn lại là `cut`.
Người dẫn chuyện là NỮ (~50 tuổi, giọng Hà Nội) — compiler tự ghi giọng, chỉ cần speaker = "NARRATOR".

## Quy tắc riêng của phim này
- Ngoại tình thể hiện kín đáo: tựa đầu vào vai, nắm tay, cụng ly, ánh mắt. KHÔNG hôn, không giường, không cởi đồ, không gợi dục.
- "Đánh ghen" chỉ bằng lời và ánh mắt: không tát, không giật tóc, không hất nước, không xô đẩy, không ai chạm vào ai khi cãi nhau.
- Màn "cú ngã" (C13): Vy TỰ ngồi thụp xuống bậc cầu thang dưới cùng, ôm bụng — không ai đứng gần cô.
- Bắt giữ (C21): công an đi tới bình thản, Khải tự chìa cổ tay. Không còng giằng co.
- Giấy tờ, màn hình điện thoại, que thử thai, giấy niêm phong: không chữ đọc được (màn hình chỉ phát sáng, giấy chỉ có dòng mực mờ; que thử thai chỉ có hai vạch hồng).

## Bối cảnh khoá — dùng NGUYÊN VĂN khi cảnh ghi tên bối cảnh
- HOME = "Inside a narrow three-storey tube house in a Hà Nội old alley: a ground-floor kitchen with a gas stove and a big aluminum sticky-rice steamer, a wooden dining table with low stools, a steep tiled staircase, a small family altar shelf, a small white home camera on a high kitchen shelf."
- HOME_NIGHT = "Night inside a narrow three-storey tube house in a Hà Nội old alley: a dim ground-floor kitchen lit by one warm bulb and a charcoal stove, a wooden dining table, a steep tiled staircase, a small white home camera with a tiny green light on a high kitchen shelf."
- STALL = "Dawn on a Hà Nội old-quarter pavement corner: a small sticky-rice stall with a bamboo basket, a steaming pot and banana leaves under a big faded umbrella, low plastic stools, mopeds passing, blue-grey dawn light and yellow streetlamps."
- OFFICE = "A modern glass-walled director's office high in a Hà Nội tower: a large white desk with a family photo frame, a black leather chair, an architectural model of a residential tower, the city skyline beyond the windows."
- CAFE = "An upscale café at night: velvet armchairs, brass lamps, marble tables, rain-streaked floor-to-ceiling windows facing the street."
- APARTMENT = "A luxury high-rise apartment in the morning: a white marble kitchen island, a pale sofa, floor-to-ceiling windows over the city, glossy cold light."
- ROOM = "A tiny rented room in a crowded Hà Nội boarding alley at night: a single wooden bed, a folding table, a small barred window, a hot plate, an aluminum basin catching drips from the leaking ceiling, a bare yellow bulb."
- SHOP = "Before dawn at Thu's small sticky-rice shop on a Hà Nội old-quarter street: a worn wooden counter, rows of banana-leaf parcels, big steaming pots, warm yellow light spilling onto the pavement."

## Đạo cụ khoá (nguyên văn)
- EARRING_BOX = "a small empty red velvet earring box"
- PHOTO = "a framed family photo of Thu, Tùng and Na"
- LUNCHBOX = "a glossy black lacquered lunch box"
- TEST = "a plastic pregnancy test stick showing two faint pink lines"
- CAMERA = "the small white home camera on the high kitchen shelf"
- CAR = "a black luxury sedan with no badge"

## HỒI 1 — CƠM NHÀ (Cảnh 01–08)

### C01 — Người Đàn Bà Thức Dậy Trước Mặt Trời | "04:00 Rạng sáng, phố cổ Hà Nội (00:00–01:00)" | setting HOME
1. [] setting riêng "Pre-dawn aerial over the tiled roofs of Hà Nội's old quarter: mist, yellow streetlamps, a few lit kitchen windows." | NAR | Hà Nội lúc bốn giờ sáng, khi cả thành phố còn ngủ say, có những người đàn bà đã phải thức dậy rồi. | aerial mở đầu hoành tráng, máy bay hạ dần về một ô cửa bếp sáng đèn.
2. [@Thu] | NAR | Thu, ba mươi tư tuổi, mười hai năm làm dâu, sáng nào cũng đồ xôi từ lúc trời còn tối đen như mực. | nồi xôi bốc khói; Thu mở vung, hơi nước trùm mặt.
3. [@Thu] cont | NAR | Đôi bàn tay chai sạn ấy đã nuôi cả nhà qua những năm tháng chồng cô còn trắng tay. | cận tay Thu nắm xôi gói lá chuối.
4. [@BaNhan] cut | NAR | Bà Nhàn, mẹ chồng cô, bảy mươi tuổi, đau lưng không ngủ được, vẫn chống gậy lần xuống bếp phụ con dâu. | bà xuống từng bậc cầu thang.
5. [@BaNhan,@Thu] cut | @BaNhan | Thu ơi, con nghỉ tay ăn miếng xôi đi đã, tối qua thằng Tùng lại về muộn hả con? |
6. [@Thu,@BaNhan] cont | @Thu | Anh ấy dạo này nhiều việc lắm mẹ ạ, mẹ cứ lên ngủ thêm đi, con lo được hết. | Thu cười gượng, đỡ bát xôi cho mẹ.

### C02 — Đôi Bông Tai Đã Bán | "05:30 Sáng, gánh xôi góc phố (01:00–02:00)" | setting STALL
1. [] | NAR | Trời vừa hửng, gánh xôi của Thu đã bày ra góc phố quen, khói bốc nghi ngút trong làn sương lạnh. |
2. [@Thu] cut | NAR | Mười hai năm trước, cô bán đôi bông tai cưới, món hồi môn duy nhất, để chồng có vốn làm ăn. | Thu lấy EARRING_BOX từ túi tạp dề, mở ra, bên trong trống.
3. [@Thu] cont | NAR | Giờ chồng cô đã là giám đốc, nhưng cô vẫn giữ gánh xôi, vì sợ một ngày nào đó cả nhà lại trắng tay. |
4. [@Thu] cut + extras "a woman customer in a pink raincoat" | @Thu | Xôi xéo hành phi nóng đây, chị ăn thử đi, em gói thêm cho chị ít ruốc nhé! |
5. [@Thu] cut | NAR | Cô lắp chiếc camera nhỏ trong bếp để vừa bán hàng vừa trông mẹ chồng, đâu ngờ sau này nó cứu cả đời cô. | Thu liếc màn hình điện thoại cũ phát sáng (không chữ), mỉm cười.
6. [@Thu] cont | NAR | Cô đâu biết rằng cùng lúc ấy, ở một tòa nhà kính giữa thành phố, chồng cô đang mỉm cười với người khác. |

### C03 — Ông Giám Đốc Mới Phất | "07:30 Sáng, nhà Thu (02:00–03:00)" | setting HOME
1. [@Tung] | NAR | Tùng, chồng cô, ba mươi bảy tuổi, giám đốc công ty xây dựng mới phất, giờ chỉ quen vest đắt tiền và xe sang. | Tùng thắt lại cổ tay áo, soi gương cạnh cầu thang.
2. [@Na] cut | NAR | Bé Na, con gái họ, chín tuổi, ôm chiếc trống con đứng chờ bố từ sáng, chiều nay con có buổi diễn ở trường. |
3. [@Na,@Tung] cut | @Na | Bố ơi, chiều nay bố đến xem con đánh trống nhé, cô giáo bảo ai cũng có bố mẹ đến. |
4. [@Tung,@Na] cont | @Tung | Bố bận họp cả ngày, con bảo mẹ đi xem cho, bố còn phải kiếm tiền nuôi cả nhà. | Tùng xoa đầu qua loa, nhìn đồng hồ.
5. [@Thu,@Tung] cut | @Thu | Anh ăn bát xôi rồi hẵng đi, em đồ từ sáng sớm, vẫn còn nóng nguyên đây này. | Thu chìa bát xôi.
6. [@Tung,@Thu] cont | @Tung | Thôi, xôi với chả xôi, ngày nào cũng xôi, anh ra ngoài ăn cho sạch sẽ. | Tùng đi thẳng ra cửa, Thu đứng ôm bát.

### C04 — Cô Thư Ký Váy Đỏ | "08:30 Sáng, văn phòng giám đốc (03:00–04:00)" | setting OFFICE
1. [] | NAR | Ở tầng hai mươi của tòa nhà kính, căn phòng giám đốc lúc nào cũng thơm mùi nước hoa đắt tiền. |
2. [@Vy] cut | NAR | Vy, cô thư ký mới hai mươi bốn tuổi, xinh đẹp, ngọt ngào, và biết rất rõ mình muốn gì ở người đàn ông này. | Vy bước vào, gót giày gõ sàn, chỉnh tóc.
3. [@Vy,@Tung] cut | @Vy | Anh Tùng ơi, em tự tay nấu cơm trưa cho anh đấy, dạo này anh gầy đi nhiều quá. | đặt LUNCHBOX lên bàn.
4. [@Tung,@Vy] cont | @Tung | Lâu lắm rồi mới có người lo cho anh một bữa trưa tử tế thế này đấy em ạ. |
5. [@Vy] cut | NAR | Hộp cơm ấy mua ở nhà hàng dưới phố, nhưng Vy biết, đàn ông chỉ cần nghe hai chữ tự tay. |
6. [@Vy] cont | NAR | Cô nghiêng đầu cười, liếc qua tấm ảnh gia đình trên bàn, rồi lặng lẽ úp nó xuống mặt bàn. | Vy úp PHOTO xuống.

### C05 — Người Tình Bí Mật | "12:00 Trưa, quán cà phê kín đáo (04:00–05:00)" | setting CAFE (đổi "at night" thành ban trưa: "An upscale café at noon: velvet armchairs, brass lamps, marble tables, tall windows facing a leafy street.")
1. [] | NAR | Giờ nghỉ trưa, Vy không ăn cơm với giám đốc, cô lén đến một quán cà phê kín đáo cách đó ba con phố. |
2. [@Khai] cut | NAR | Ở góc khuất, Khải đang đợi, người tình thật sự của Vy, kẻ đứng sau mọi nước cờ của cô. |
3. [@Vy,@Khai] cut | @Khai | Thế nào em, lão giám đốc cắn câu chưa? Hợp đồng lớn sắp ký rồi đấy. |
4. [@Vy,@Khai] cont | @Vy | Nửa năm thôi anh, em sẽ khiến lão bỏ vợ, sang tên hết nhà cửa cho em. |
5. [@Khai,@Vy] cont | @Khai | Đừng để lão biết có anh, đàn ông ngu đến mấy cũng có lúc tỉnh ra đấy em. |
6. [@Vy] cut | NAR | Vy khuấy ly cà phê, mỉm cười, cô đã tính kỹ từng bước để bước chân vào căn nhà của người khác. |

### C06 — Sợi Tóc Trên Áo Chồng | "23:30 Đêm, nhà Thu (05:00–06:00)" | setting HOME_NIGHT
1. [] | NAR | Đêm ấy, Tùng lại về lúc gần nửa đêm, mùi rượu lẫn mùi nước hoa lạ phảng phất khắp căn nhà nhỏ. | áo sơ mi vắt trên ghế, cà vạt.
2. [@Thu] cut | NAR | Thu lặng lẽ nhặt chiếc áo sơ mi chồng vứt trên ghế, định mang đi giặt như mọi đêm. |
3. [@Thu] cont | NAR | Trên cổ áo trắng là một vệt son đỏ, và vắt ngang vai áo là một sợi tóc dài uốn xoăn màu nâu. | cận cổ áo.
4. [@Thu,@Tung] cut | @Thu | Anh Tùng, vệt son trên áo anh là của ai? Anh nói thật với em đi. |
5. [@Tung,@Thu] cont | @Tung | Tiếp khách thì dính son là chuyện thường, cô đừng nghĩ linh tinh rồi làm ầm lên. |
6. [@Thu] cut | NAR | Tùng quay lưng đi ngủ, còn Thu ngồi bên bậc cầu thang đến sáng, tay vẫn nắm chặt chiếc áo. |

### C07 — Chuyến Công Tác Đà Nẵng | "Chiều tà, khu nghỉ dưỡng biển (06:00–07:00)" | setting "Sunset at a luxury seaside resort: an infinity pool terrace with white loungers, palm trees, the sea glowing orange."
1. [] | NAR | Tùng bảo vợ phải đi công tác Đà Nẵng ba ngày, đúng vào dịp sinh nhật lần thứ ba mươi lăm của cô. | aerial resort.
2. [@Tung,@Vy] cut | NAR | Nhưng chuyến công tác ấy chỉ có hai người, bên bể bơi khu nghỉ dưỡng nhìn ra biển. | ngồi ghế dài, cụng ly nước cam (kín đáo).
3. [@Vy,@Tung] cont | @Vy | Anh ơi, ở bên anh em mới biết thế nào là được yêu, vợ anh có biết chiều anh thế này không? |
4. [@Tung,@Vy] cont | @Tung | Cô ấy chỉ biết xôi với chợ thôi em ạ, sống với cô ấy anh thấy mình già đi mười tuổi. |
5. [@Thu,@Na] cut setting HOME_NIGHT | NAR | Ở nhà, Thu và bé Na thắp nến trên chiếc bánh nhỏ, chiếc ghế của Tùng vẫn để trống suốt bữa. |
6. [@Na,@Thu] cont | @Na | Mẹ ơi, con ước bố về ăn cơm với mẹ con mình, như hồi nhà mình còn nghèo ấy. |

### C08 — Bức Ảnh Lúc Nửa Đêm | "Đêm, nhà Thu (07:00–08:00)" | setting HOME_NIGHT
1. [@Thu] | NAR | Đêm Tùng về, điện thoại anh rung trên bàn, màn hình sáng lên một cái tên được lưu là anh Tuấn kế toán. | màn hình phát sáng không chữ.
2. [@Thu] cont | NAR | Thu mở ra, và cả thế giới của cô sụp đổ, đó là ảnh một cô gái váy đỏ đang tựa vào vai chồng cô. | ánh màn hình hắt lên mặt, Thu che miệng.
3. [@Tung,@Thu] cut | @Tung | Cô lục điện thoại của tôi à? Cô còn biết tôn trọng chồng mình không hả? |
4. [@Thu,@Tung] cont | @Thu | Mười hai năm em bán cả bông tai cưới cho anh làm ăn, anh trả em thế này sao? |
5. [@Tung,@Thu] cont | @Tung | Chuyện cũ rồi, đừng lôi ra kể công mãi, tôi chán cái nhà này lắm rồi. |
6. [@BaNhan] cut setting riêng "Night on the dim tiled stair landing of the tube house, a faint light from the kitchen below." | NAR | Trên chiếu nghỉ cầu thang, bà Nhàn đứng lặng trong bóng tối, nghe hết từng lời đứa con trai mình nói. |

## HỒI 2 — BÉ BA (Cảnh 09–17)

### C09 — Bé Ba Ghé Gánh Xôi | "06:00 Sáng, góc phố (08:00–09:00)" | setting STALL
1. [@Vy] | NAR | Sáng hôm ấy, một chiếc xe sang dừng ngay trước gánh xôi, cô gái váy đỏ bước xuống, kính đen che nửa mặt. | CAR dừng; Vy bước xuống, đeo kính râm.
2. [@Thu] cut | NAR | Thu nhận ra ngay chiếc váy đỏ trong tấm ảnh đêm qua, đôi tay đang gói xôi của cô khựng lại. |
3. [@Vy,@Thu] cut | @Vy | Chị cho em một gói xôi xéo, nghe nói ngày xưa anh Tùng mê xôi của chị lắm. |
4. [@Thu,@Vy] cont | @Thu | Ngày xưa hay bây giờ, anh ấy vẫn là chồng tôi, cô muốn ăn xôi thì cứ ngồi xuống. |
5. [@Vy,@Thu] cont | @Vy | Chị giữ được bếp, nhưng giữ không nổi chồng đâu chị ạ, nhìn đôi tay chị kìa. | Vy tháo kính, liếc tay Thu.
6. [@Thu] cut | NAR | Vy đặt tờ tiền lên mẹt xôi rồi bỏ đi, còn Thu nhìn đôi bàn tay chai sạn của mình rất lâu. |

### C10 — Mâm Cơm Đòi Ly Hôn | "19:00 Tối, nhà Thu (09:00–10:00)" | setting HOME_NIGHT (đổi thành buổi tối có mâm cơm: giữ nguyên chuỗi HOME_NIGHT)
1. [] | NAR | Tối hôm đó, Thu nấu một mâm cơm đủ món Tùng thích, như cố níu chút hơi ấm cuối cùng của gia đình. | mâm cơm trên bàn gỗ.
2. [@Tung,@Thu] cut | @Tung | Mình ly hôn đi, tôi không chịu nổi cái mùi bếp núc với gánh xôi của cô nữa. |
3. [@Thu,@Tung] cont | @Thu | Anh nói lại xem, anh định bỏ mẹ con em vì một đứa con gái kém anh mười mấy tuổi à? |
4. [@BaNhan] cut | NAR | Bà Nhàn chống gậy đứng bật dậy, đôi tay già run lên, đôi đũa trên tay rơi xuống mâm cơm. |
5. [@BaNhan,@Tung] cut | @BaNhan | Tùng, mày quên ai bán bông tai cho mày làm ăn rồi à? Mày còn là người không? |
6. [@Tung,@BaNhan] cont | @Tung | Mẹ đừng bênh cô ấy nữa, con có quyền sống cho mình, con quyết rồi. |

### C11 — Nước Mắt Bên Bếp Than | "Nửa đêm, bếp nhà Thu (10:00–11:00)" | setting HOME_NIGHT
1. [@Thu] | NAR | Nửa đêm, Thu ngồi một mình bên bếp than, nồi xôi sáng mai vẫn phải đồ, nước mắt rơi cả vào chậu gạo. |
2. [@Thu] cont | NAR | Cô không dám khóc thành tiếng, sợ mẹ chồng thức giấc, sợ con gái nhìn thấy mẹ yếu đuối. |
3. [@Na,@Thu] cut | NAR | Bé Na lặng lẽ xuống bếp từ lúc nào, đôi tay nhỏ xíu vòng qua ôm lấy lưng mẹ. |
4. [@Na,@Thu] cont | @Na | Mẹ đừng khóc nữa, bố không cần mẹ thì con với bà cần mẹ, mẹ nhé. |
5. [@Thu,@Na] cont | @Thu | Ừ, mẹ không khóc nữa, mẹ còn có con, có bà, mẹ phải sống cho đàng hoàng. |
6. [] cut | NAR | Ngọn lửa bếp than bùng lên trong đêm, như lời hứa của một người đàn bà sẽ không bao giờ gục ngã. | cận than hồng bùng sáng.

### C12 — Hai Vạch Hồng | "Sáng, căn hộ cao cấp (11:00–12:00)" | setting APARTMENT
1. [] | NAR | Căn hộ cao cấp Tùng thuê cho Vy nhìn ra cả thành phố, tiền thuê mỗi tháng bằng một năm Thu bán xôi. |
2. [@Vy] cut | NAR | Sáng ấy, Vy cầm que thử thai đã chuẩn bị sẵn, hai vạch hồng được cô mua lại từ một người quen. | Vy cầm TEST.
3. [@Vy,@Tung] cut | @Vy | Anh ơi, mình có con rồi, bác sĩ bảo nhiều khả năng là con trai đấy anh. | chìa TEST.
4. [@Tung,@Vy] cont | @Tung | Con trai thật à em? Anh sẽ lo cho mẹ con em đầy đủ, anh hứa với em. |
5. [@Vy,@Tung] cont | @Vy | Nhưng con em không thể là con ngoài giá thú, anh phải ly hôn ngay, sang tên căn nhà cho con. |
6. [@Vy] cut | NAR | Tùng gật đầu không chút do dự, còn Vy quay mặt đi, khóe môi cong lên một nụ cười lạnh. |

### C13 — Cú Ngã Trên Cầu Thang | "Chiều, nhà Thu (12:00–13:00)" | setting HOME
1. [@Vy] | NAR | Chiều hôm sau, Vy tự tìm đến nhà Thu, tay xách giỏ trái cây, nói là đến chào chị cả. |
2. [@Thu,@Vy] cut | @Vy | Em đến xem nhà một chút, sắp tới em với con trai anh Tùng sẽ về đây ở. |
3. [@Thu,@Vy] cont | @Thu | Đây là nhà của mẹ con tôi, mời cô về cho, tôi không muốn nói chuyện với cô. | Thu chỉ tay ra cửa, đứng cách xa Vy.
4. [@Vy] cut | NAR | Nghe tiếng xe Tùng đỗ ngoài ngõ, Vy bỗng ôm bụng, tự ngồi thụp xuống chân cầu thang, kêu lên thất thanh. | không ai ở gần cô.
5. [@Tung,@Thu] cut | @Tung | Cô làm cái gì cô ấy thế hả? Cô ấy đang mang thai con của tôi đấy! | Tùng chỉ tay vào Thu, quát.
6. [@Thu] cut | NAR | Thu đứng chết lặng, không ai tin cô, chỉ có chiếc camera nhỏ trên kệ bếp vẫn lặng lẽ nhấp nháy đèn xanh. | cận CAMERA đèn xanh.

### C14 — Mẹ Chồng Chọn Con Dâu | "Sáng, nhà Thu (13:00–14:00)" | setting HOME
1. [] | NAR | Một tuần sau, tờ đơn ly hôn nằm trên chiếc bàn ăn, nơi mười hai năm nay Thu dọn biết bao mâm cơm. | giấy tờ (không chữ đọc được), bút.
2. [@Thu] cut | NAR | Thu ký tên, không khóc, không van xin, cô chỉ xin được nuôi bé Na, ngoài ra không lấy gì cả. |
3. [@Tung,@Thu] cut | @Tung | Căn nhà này tôi xây, cô dọn đi trong tuần này, đừng để Vy phải nhìn thấy cô. |
4. [@BaNhan] cut | NAR | Bà Nhàn lặng lẽ xách chiếc làn mây cũ, khoác áo, đứng cạnh con dâu và cháu gái ở bậc cửa. |
5. [@BaNhan,@Tung] cut | @BaNhan | Mẹ đi theo con dâu, con trai tôi chết từ hôm nó bỏ vợ bỏ con rồi. |
6. [@Tung] cut | NAR | Tùng đứng giữa căn nhà rộng, lần đầu thấy nó trống trải đến thế, nhưng anh vẫn không nói một lời giữ lại. |

### C15 — Căn Phòng Trọ Mười Mét Vuông | "Tối, xóm trọ (14:00–15:00)" | setting ROOM
1. [] | NAR | Ba bà cháu dọn về căn phòng trọ mười mét vuông, mưa dột tong tỏng xuống chiếc chậu nhôm giữa nhà. |
2. [@Thu] cut | NAR | Thu lau nhà, kê giường, xếp nồi xôi vào góc, như thể chỉ là chuyển nhà chứ không phải mất cả một đời. |
3. [@BaNhan,@Thu] cut | @BaNhan | Con ạ, mẹ còn ít vàng dành dụm, con cầm lấy mà mở một quán xôi cho tử tế. | bà đưa gói khăn tay nhỏ.
4. [@Thu,@BaNhan] cont | @Thu | Mẹ giữ lấy mà dưỡng già, con còn đôi bàn tay, con sẽ làm lại từ đầu mẹ ạ. | Thu gập tay bà lại.
5. [@Na] cut | NAR | Bé Na ngồi học bài dưới bóng đèn vàng, cạnh đó là bức tranh con vẽ ba người phụ nữ nắm tay nhau. | tranh sáp màu, không chữ.
6. [@Thu] cut | NAR | Đêm ấy, lần đầu tiên sau nhiều năm, Thu ngủ một giấc thật sâu, không phải thức chờ ai về nữa. |

### C16 — Chữ Ký Định Mệnh | "Sáng, nhà cũ & văn phòng (15:00–16:00)" | setting OFFICE
1. [@Vy] setting HOME | NAR | Thu vừa dọn đi, Vy đã dọn vào, dỡ bỏ gian bếp đồ xôi của Thu, thay bằng quầy rượu và rèm nhung đỏ. |
2. [@Vy,@Tung] cut | @Vy | Anh ký vào đây cho em, giấy ủy quyền thôi mà, để em lo hết giấy tờ cho con. |
3. [@Tung,@Vy] cont | @Tung | Em lo thì anh yên tâm, anh ký luôn, mấy cái giấy tờ này anh chả buồn đọc. |
4. [@Vy] cut | NAR | Chỉ một chữ ký, Tùng đã trao cho Vy quyền định đoạt cả công ty lẫn căn nhà anh vừa đuổi vợ ra khỏi. |
5. [@Khai] cut setting riêng "Inside a black luxury sedan with no badge parked in a dim underground car park, the elevator doors glowing in the distance." | NAR | Dưới hầm xe, Khải ngồi chờ trong chiếc xe đen, ngón tay gõ nhịp lên vô lăng, mắt dán vào cửa thang máy. |
6. [@Vy,@Khai] cut (cùng setting xe) | @Khai | Xong rồi chứ em? Ba tháng nữa mình rút hết tiền, bay ra nước ngoài sống như vua. |

### C17 — Quán Xôi Của Thu | "05:30 Sáng, sáu tháng sau (16:00–17:00)" | setting SHOP
1. [] | NAR | Sáu tháng sau, ở một góc phố cổ, quán xôi nhỏ của Thu đã mở cửa từ khi trời còn tối. |
2. [@Thu] cut | NAR | Không cửa hàng sang, không biển hiệu đẹp, chỉ có nồi xôi dẻo thơm và nụ cười hiền như ngày nào. |
3. [] + extras "a long queue of office workers and students waiting under the streetlamps" | NAR | Người ta xếp hàng dài từ đầu phố, có người đi xe cả tiếng đồng hồ chỉ để mua một gói xôi. |
4. [@BaNhan,@Na] cut | NAR | Bà Nhàn ngồi gói lá chuối, bé Na buộc lạt, ba bà cháu cười nói rộn ràng như chưa từng mất gì. |
5. [@Thu] cut + extras "a few customers holding banana-leaf parcels" | @Thu | Xôi hôm nay hết sớm rồi, mai cả nhà quay lại, em để phần trước cho nhé! |
6. [@Thu] cont | NAR | Người đàn bà từng bị chê tay chân thô ráp, giờ chính đôi bàn tay ấy đang nuôi sống cả gia đình. |

## HỒI 3 — QUẢ BÁO (Cảnh 18–25)

### C18 — Công Ty Rỗng Ruột | "Sáng, văn phòng giám đốc (17:00–18:00)" | setting OFFICE
1. [] | NAR | Cùng lúc ấy, công ty của Tùng bắt đầu lung lay, những hợp đồng lớn lần lượt bị hủy không rõ lý do. |
2. [@Tung] cut + extras "a middle-aged accountant in a grey cardigan holding a folder" | NAR | Kế toán trưởng run run đặt tập hồ sơ lên bàn, tài khoản công ty chỉ còn vài trăm nghìn đồng. |
3. [@Tung] cont (cùng extras) | @Tung | Tiền đâu hết rồi? Ai rút hết tiền của công ty tôi? Gọi Vy lên đây ngay! |
4. [@Tung] cut | NAR | Mọi lệnh chuyển tiền đều có chữ ký ủy quyền, chữ ký của chính người đàn bà anh tin nhất. | giấy tờ chỉ là dòng mực mờ.
5. [@Tung] cont | NAR | Anh gọi cho Vy, mười cuộc, hai mươi cuộc, đầu dây bên kia chỉ còn tiếng thuê bao lạnh lùng. |
6. [@Tung] cut setting riêng "Dusk on a busy Hà Nội street, rush-hour mopeds, neon shop lights flickering on." | NAR | Tùng đi ra phố như người mất hồn, chiếc vest đắt tiền nhàu nhĩ, cà vạt lệch sang một bên. |

### C19 — Sau Lớp Kính Quán Cà Phê | "Tối mưa (18:00–19:00)" | setting "Rainy night on the pavement outside an upscale café, warm light glowing through tall rain-streaked windows."
1. [] | NAR | Tối hôm ấy, đi ngang quán cà phê quen của Vy, Tùng khựng lại trước lớp kính sáng đèn. |
2. [@Vy,@Khai] cut setting CAFE | NAR | Bên trong, Vy đang tựa đầu vào vai một gã đàn ông khác, hai người cụng ly, cười rất tươi. |
3. [@Tung] cut | NAR | Tùng đứng chết trân dưới mưa, nhìn bàn tay gã kia vuốt lên chiếc bụng phẳng lì của Vy. | Tùng nhìn qua kính.
4. [@Tung,@Vy] cut setting CAFE | @Tung | Vy, gã này là ai? Còn đứa con của anh, em giải thích cho anh nghe đi! |
5. [@Vy,@Tung] cont | @Vy | Con nào hả anh? Que thử thai em mua mười nghìn ngoài hiệu thuốc đấy, anh ngây thơ thật. |
6. [@Vy,@Tung] cont | @Vy | Anh tưởng em yêu cái bụng phệ của anh à? Em yêu tiền của anh thôi, giờ tiền hết rồi. | Vy đứng dậy, khoác túi, bỏ đi.

### C20 — Căn Nhà Bị Niêm Phong | "Đêm mưa, trước cổng nhà cũ (19:00–20:00)" | setting "Rainy night in a narrow Hà Nội alley outside a closed steel gate of a tube house, a paper seal stuck across the gate, a single streetlamp."
1. [] | NAR | Đêm đó Tùng về đến nhà, cánh cổng đã dán giấy niêm phong, căn nhà bị Vy đem thế chấp ngân hàng từ lâu. | giấy niêm phong không chữ đọc được.
2. [@Tung] cut | NAR | Anh ngồi sụp xuống bậc cửa dưới mưa, chiếc vest ướt sũng, điện thoại không còn ai để gọi. |
3. [@Tung] cont | NAR | Anh mở ứng dụng camera bếp mà Thu cài cho anh từ ngày xưa, những đoạn ghi hình cũ vẫn còn lưu lại. |
4. [@Tung] cut | NAR | Đoạn video buổi chiều hôm ấy hiện ra, Vy tự ngồi xuống cầu thang, tự ôm bụng, tự kêu la. | cận mặt Tùng, ánh màn hình hắt lên (không thấy màn hình).
5. [@Tung] cont | NAR | Thu chưa từng chạm vào cô ta, vậy mà anh đã quát vào mặt người vợ mười hai năm, chẳng một lời xin lỗi. |
6. [@Tung] cut | NAR | Rạng sáng, Tùng lau nước mắt, đứng dậy đi thẳng đến đồn công an, việc tử tế đầu tiên anh làm sau một năm trời. |

### C21 — Chuyến Bay Không Cất Cánh | "Sáng, sảnh sân bay (20:00–21:00)" | setting "A bright modern airport departure hall: polished stone floor, check-in counters, tall glass walls, travelers with suitcases in the distance."
1. [] | NAR | Sáng hôm sau ở sân bay, Vy và Khải kéo vali, chuẩn bị bay ra nước ngoài với toàn bộ số tiền chiếm đoạt. |
2. [@Vy,@Khai] cut | NAR | Hai kẻ lừa đảo nắm tay nhau thật chặt, đeo kính đen, ung dung đi về phía quầy làm thủ tục. |
3. [@Khai,@Vy] cont | @Khai | Qua được cửa này là mình giàu cả đời em ạ, lão Tùng giờ chắc đang ngồi khóc ở đâu đó. |
4. [@Vy] cut + extras "two police officers in dark-green uniforms walking calmly toward her" | NAR | Nhưng trước quầy làm thủ tục, hai cán bộ công an đã đứng chờ sẵn, trên tay là lệnh bắt khẩn cấp. |
5. [@Vy] cont (cùng extras) | @Vy | Các anh nhầm người rồi, tôi là vợ giám đốc, các anh có biết tôi là ai không? | Vy lùi một bước, tay siết quai túi.
6. [@Khai] cut + extras "a police officer standing calmly beside him" | NAR | Khải buông vali, tự chìa hai cổ tay ra, tấm vé máy bay hạng thương gia rơi xuống sàn đá lạnh. |

### C22 — Gói Xôi Lúc Bình Minh | "05:30 Sáng, quán xôi (21:00–22:00)" | setting SHOP
1. [] | NAR | Một tuần sau, trời còn chưa sáng, có một người đàn ông gầy rộc đứng lặng rất lâu ở cuối hàng mua xôi. |
2. [@Thu,@Tung] cut | NAR | Thu ngẩng lên nhận ra Tùng, chiếc sơ mi nhàu cũ, đôi mắt trũng sâu của một người đã mất tất cả. |
3. [@Tung,@Thu] cont | @Tung | Thu ơi, anh sai rồi, anh mù quáng, em cho anh về với mẹ con em được không? |
4. [@Thu,@Tung] cont | @Thu | Gói xôi này em mời anh, còn cơm nhà, chính anh đã tự tay bỏ đi rồi. | Thu đặt gói xôi lá chuối vào tay anh.
5. [@Tung] cut | NAR | Tùng quỳ xuống bên vỉa hè, hai tay ôm gói xôi nóng, nước mắt rơi lã chã trên lớp lá chuối. |
6. [@Thu] cut | NAR | Thu quay vào bếp không ngoái lại, không phải vì hết thương, mà vì cô đã học được cách thương chính mình. |

### C23 — Mẹ Vẫn Là Mẹ | "Tối, gác nhỏ trên quán xôi (22:00–23:00)" | setting "Evening in a small cozy room above the sticky-rice shop: a low wooden bed, a family altar with incense, a window over the old-quarter street, a warm lamp."
1. [@Tung] cut setting riêng "Evening on a narrow wooden staircase leading up to a closed door above the sticky-rice shop, warm light under the door." | NAR | Tối ấy, Tùng tìm đến chỗ ở mới của mẹ, đứng ngoài cửa rất lâu mà không dám gõ. |
2. [@BaNhan,@Tung] cut | @BaNhan | Mày đến đây làm gì? Mẹ già rồi, không còn gì cho mày lấy nữa đâu con. |
3. [@Tung,@BaNhan] cont | @Tung | Mẹ ơi, con không lấy gì nữa, con chỉ xin mẹ cho con được làm người tử tế lại. |
4. [@BaNhan,@Tung] cont | @BaNhan | Tử tế thì phải làm cả đời, mai con ra quán rửa bát, làm thuê cho con Thu đi. |
5. [@Tung] cut | NAR | Tùng cúi đầu thật thấp, lần đầu tiên sau nhiều năm, anh nghe lời mẹ mà không cãi một câu. |
6. [@BaNhan] cut | NAR | Bà Nhàn khép cửa, lén lau giọt nước mắt, dù sao nó vẫn là đứa con bà mang nặng đẻ đau. |

### C24 — Buổi Diễn Văn Nghệ | "Chiều, hội trường trường tiểu học (23:00–24:00)" | setting "Afternoon in a primary school hall: a small stage with paper flower decorations and colorful bunting, rows of plastic chairs filled with parents."
1. [] | NAR | Cuối năm học, hội trường trường tiểu học chật kín phụ huynh, cờ hoa rực rỡ khắp sân khấu nhỏ. |
2. [@Na] cut | NAR | Bé Na đánh trống đi đầu đội văn nghệ, mắt không ngừng nhìn xuống hàng ghế phụ huynh tìm kiếm. |
3. [@Thu,@Tung] cut | NAR | Ở hàng ghế cuối, Tùng ngồi cạnh Thu, lần đầu tiên sau chín năm anh đến xem con biểu diễn. |
4. [@Na,@Tung] cut setting riêng "Backstage corner of the school hall after the show, paper decorations, soft afternoon light." | @Na | Bố đến thật rồi! Bố ơi, lần sau bố đến sớm hơn để ngồi hàng đầu nhé. |
5. [@Tung,@Na] cont | @Tung | Bố hứa, từ nay buổi diễn nào của con, bố cũng đến sớm nhất, ngồi hàng đầu tiên. | Tùng quỳ xuống ngang tầm con.
6. [@Thu] cut (setting backstage) | NAR | Thu đứng nhìn hai bố con, cô không tha thứ để quay lại, nhưng cô tha thứ để con mình có bố. |

### C25 — Vợ Tào Khang | "06:00 Sáng, một năm sau (24:00–25:00)" | setting SHOP (sáng sớm, nắng vàng đầu tiên)
1. [] | NAR | Một năm sau, quán xôi nhỏ đã thành ba cửa hàng, nhưng sáng nào bà chủ vẫn tự tay đồ mẻ xôi đầu tiên. |
2. [@Thu] cut | NAR | Thu đứng bên nồi xôi nghi ngút khói, đôi bàn tay vẫn chai sạn, nhưng ánh mắt đã sáng như năm mười tám tuổi. |
3. [@Tung] cut | NAR | Ở góc quán, Tùng lặng lẽ rửa bát, làm thuê cho chính người vợ cũ, mỗi ngày trả một chút nợ ân tình. |
4. [@Thu,@Na] cut | @Na | Mẹ ơi, sau này lớn lên con muốn giỏi giang như mẹ, không cần dựa vào ai cả. |
5. [@Thu,@Na] cont | @Thu | Con cứ sống tử tế, chăm chỉ, ai bỏ con mà đi thì người thiệt là họ, không phải con. |
6. [] cut setting riêng "Sunrise aerial over the tiled roofs of Hà Nội's old quarter, golden light, steam rising from a small shop on a corner street." | NAR | Đàn ông có thể đi tìm hương lạ, nhưng người vợ tào khang, cả đời chỉ có một mà thôi. | shot cuối hoành tráng.