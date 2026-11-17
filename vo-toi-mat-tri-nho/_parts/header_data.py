"""Header của phim "Vợ Tôi Mất Trí Nhớ Có Chọn Lọc": nhân vật, bối cảnh khoá, trang phục, siêu dữ liệu 25 cảnh."""

SERIES = "vo-toi-mat-tri-nho"
TITLE = "Vợ Tôi Mất Trí Nhớ Có Chọn Lọc"

STYLE = ("Photorealistic live-action Vietnamese romantic family comedy-drama set in a modern Vietnamese city today among the stylish upper-middle class; "
         "glossy premium streaming-series look, flattering beauty lighting on every face, creamy luminous skin tones, warm golden highlights, "
         "rich teal-and-amber palette, elegant wardrobe, subtle 35mm film grain, shallow depth of field.")
LIGHTING = ("Flattering soft key light on every face: golden city-light bokeh and candlelight on the rooftop at night, warm crystal chandeliers in the hotel lobby, "
            "clean soft white daylight in the hospital and the yoga studio, bright airy sun in the villa by day, warm amber lamps in the villa at night, "
            "golden window light in the café, yellow bulb strings at the lakeside food stall, glowing fairy lights at the garden party.")
VOICE_COMMON = ("every character speaks standard Northern Vietnamese (never Southern or Central accents), says each word once and clearly, "
                "and sounds clearly different from the other speaker in pitch, age and texture.")

# anchor: phần cuối sau "; " là trang phục (build script thay phần này khi clip có "wardrobe").
CHARACTERS = {
    "@Linh": {
        "name": "Linh",
        "anchor": "Linh, 32, Quân's wife, a former fashion model and beauty-pageant winner who gave up the runway for her family and is now faking amnesia; "
                  "breathtakingly beautiful leading lady, tall and graceful with model proportions, flawless luminous fair skin, long silky straight black hair falling past her shoulders, "
                  "large bright almond-shaped dark eyes, high cheekbones, a radiant smile, soft natural makeup with rosy lips; "
                  "elegant ivory silk blouse, high-waisted cream wide-leg trousers, delicate pearl earrings, nude heels.",
        "voice": "woman of 32, clear warm alto with an elegant Northern lilt, playful and bright when acting young",
        "rate": 4.0,
    },
    "@Quan": {
        "name": "Quân",
        "anchor": "Quân, 36, Linh's husband, CEO of a luxury interior-design company; strikingly handsome leading man, tall and athletic, sharp jawline, "
                  "neatly styled short black hair with a side part, warm expressive dark eyes, light designer stubble, a charming dimpled smile; "
                  "tailored navy suit, crisp white shirt open at the collar with no tie, silver wristwatch, polished brown leather shoes.",
        "voice": "man of 36, smooth resonant baritone, confident and charming, cracking higher when flustered",
        "rate": 4.0,
    },
    "@MaiAnh": {
        "name": "Mai Anh",
        "anchor": "Mai Anh, 25, a yoga instructor and lifestyle influencer who is Quân's secret girlfriend; gorgeous and radiant, slim and toned, "
                  "glowing golden-tan skin, long glossy wavy chestnut-brown hair, big doe eyes with long lashes, a sweet heart-shaped face, glossy pink lips; "
                  "soft pink knit cardigan over a fitted white top, light-blue straight jeans, white sneakers, small gold hoop earrings.",
        "voice": "young woman of 25, bright airy soprano, bubbly and quick, turning small and soft when hurt",
        "rate": 4.0,
    },
    "@Khang": {
        "name": "Khang",
        "anchor": "Khang, 34, a rehabilitation doctor and Linh's old university friend; handsome in a gentle intellectual way, tall and lean, "
                  "fair clear skin, soft tousled black hair, kind calm eyes behind thin rimless glasses, a dry half-smile; "
                  "crisp white doctor's coat over a light-blue shirt and grey trousers, a stethoscope around the neck, white sneakers.",
        "voice": "man of 34, calm gentle tenor, dry deadpan humour, never in a hurry",
        "rate": 4.0,
    },
    "@Tuan": {
        "name": "Tuấn",
        "anchor": "Tuấn, 35, Quân's personal assistant and best friend, a hopeless liar; cheerful boyish good looks, fresh clean-shaven face with deep dimples, "
                  "bright lively eyes, thick slightly wavy black hair, a stocky friendly build; "
                  "light-beige suit, pale-pink shirt with no tie, brown loafers, a tablet always tucked under one arm.",
        "voice": "man of 35, lively nasal comic tenor, gabbling fast whenever he lies",
        "rate": 4.0,
    },
    "@Bong": {
        "name": "Bống",
        "anchor": "Bống, 7, Linh and Quân's daughter; adorable little girl with a round rosy face, huge sparkling dark eyes, straight black bangs and two high pigtails with yellow ribbons, a gap-toothed grin; "
                  "yellow cotton dress with a white Peter Pan collar, white socks, small red shoes.",
        "voice": "girl of 7, high clear child voice, very earnest and bright",
        "rate": 3.8,
    },
}

# Bối cảnh khoá (dán nguyên văn vào "setting").
S = {
    "ROOF": "A luxurious rooftop restaurant terrace at night high above a wide city lake, privately booked and empty of other guests: one candlelit table with white linen and red roses, "
            "a glass balustrade, the city's golden lights and the dark lake below, potted olive trees, warm string lights overhead, a private brass elevator at the end of the terrace.",
    "LOBBY": "The grand lobby of a five-star hotel at night, quiet and empty: polished cream marble floor, a sweeping crystal chandelier, tall marble pillars, "
             "velvet emerald sofas, a bank of brass elevator doors, huge white orchid arrangements.",
    "HOSP": "A bright private VIP hospital room by day: a white adjustable hospital bed with crisp sheets, a bedside monitor showing only soft wave lines, a vase of white lilies, "
            "a large window with sheer curtains over the city, a pale-wood visitor chair.",
    "CORR": "The quiet hospital corridor outside the VIP room by day: pale walls, a long window with soft daylight, a wooden bench, a potted fern, a closed pale-wood door.",
    "CLINIC": "A calm doctor's consultation office in the private hospital by day: a white desk with a reading lamp, a model of a human brain, a softly glowing lightbox on the wall, "
              "a window with soft daylight, two chairs facing the desk.",
    "LIV_EVE": "The open living room of a modern lakeside villa in the evening: double-height glass walls onto a garden, a long cream sofa, a walnut coffee table, "
               "a large abstract painting, warm amber floor lamps, a floating staircase with glass rails.",
    "LIV_DAY": "The open living room of a modern lakeside villa by day: double-height glass walls onto a sunny garden, a long cream sofa, a walnut coffee table, "
               "a large abstract painting, a floating staircase with glass rails, bright soft daylight.",
    "KIT_DAY": "The bright modern kitchen of the villa in the morning: a white marble island with tall stools, matte sage-green cabinets, copper pendant lamps, "
               "a bowl of lemons, a large window onto the sunny garden.",
    "KIT_NIGHT": "The modern kitchen of the villa late at night: a white marble island with tall stools, matte sage-green cabinets, only the warm copper pendant lamps lit, "
                 "a small pot of rice porridge steaming on the stove, rain streaming down the dark garden window.",
    "YOGA": "Mai Anh's airy yoga studio on a high floor by day: pale oak floor, rolled lilac yoga mats, tall mirrors along one wall, hanging green plants, "
            "floor-to-ceiling windows with soft white daylight over the city.",
    "YOGA_EVE": "Mai Anh's airy yoga studio on a high floor in the evening: pale oak floor, rolled lilac yoga mats, tall mirrors along one wall, hanging green plants, "
                "warm low lamps, floor-to-ceiling windows onto the city lights.",
    "CAFE": "A chic quiet café overlooking a green city lake in the afternoon: a marble round table with two cups of tea, rattan chairs, big windows onto the green lake, "
            "a glass pastry display, warm golden daylight.",
    "STREET": "A cosy lakeside street-food corner at night: low plastic stools and a small steel table with bowls of bún chả, a charcoal grill with rising smoke, "
              "strings of yellow bulbs, reflections dancing on the dark water.",
    "OFFICE": "Quân's glass-walled CEO office high above the city by day: a long walnut desk, a white leather sofa, shelves of interior-design fabric and wood samples, "
              "a panoramic city view, two envelopes on the desk, one blue and one pink.",
    "BROOM": "Bống's pastel bedroom in the villa at night: a small white bed with star-patterned sheets, a soft moon-shaped night lamp, plush toys on a shelf, "
             "a reading nook by the window.",
    "GARDEN": "The villa garden at night dressed for a birthday party: strings of warm fairy lights over the lawn, a white rose arch, a small round table with a cream birthday cake and candles, "
              "lanterns along a stone path, a still pool reflecting the lights.",
}

# Trang phục thay theo cảnh (chỉ phần trang phục, không đổi mặt/tóc).
W = {
    "L_GOWN": "floor-length emerald-green satin evening gown with thin straps, diamond drop earrings, a slim gold clutch",
    "L_HOSP": "pale-blue cotton hospital gown under a soft white knit cardigan",
    "L_YOUNG": "oversized pastel-yellow hoodie, short pleated white tennis skirt over light leggings, chunky white sneakers, a pink scrunchie on the wrist",
    "L_DATE": "pastel-pink cropped cardigan over a white cotton sundress, white sneakers, a small pearl hair clip",
    "L_YOGA": "sage-green long-sleeve fitted yoga top and matching full-length yoga trousers, bare feet",
    "L_PJ": "soft lavender silk pajama set with long sleeves and long trousers",
    "L_PARTY": "flowing white chiffon midi dress with fluttering sleeves, a thin gold belt, white strappy heels",
    "L_BOSS": "sharp white tailored blazer over a black silk top, slim black trousers, gold earrings, black heels",
    "L_RED": "floor-length deep-red silk evening gown with long sleeves, ruby drop earrings",
    "Q_HOME": "rumpled grey T-shirt and navy pajama trousers, barefoot",
    "Q_DATE": "white polo shirt, beige chinos, white leather sneakers",
    "Q_PARTY": "cream linen suit over a white shirt, no tie, brown loafers",
    "Q_APRON": "grey T-shirt, dark jeans and a frilly pink kitchen apron, house slippers",
    "Q_TUX": "classic black tuxedo with a black bow tie, white shirt",
    "M_LOBBY": "chic short white bouclé jacket dress, a pearl hair clip, white heels",
    "M_YOGA": "lilac long-sleeve fitted yoga top and matching full-length yoga trousers, bare feet",
    "M_PARTY": "elegant lavender satin midi dress with cap sleeves, small pearl earrings, silver heels",
    "K_PARTY": "light-grey casual blazer over a white T-shirt, dark trousers, white sneakers",
    "B_PJ": "pink star-print long pajamas",
}

NOUN = {"@Linh": "the elegant wife", "@Quan": "the husband", "@MaiAnh": "the young yoga teacher",
        "@Khang": "the doctor", "@Tuan": "the assistant", "@Bong": "the little girl"}
