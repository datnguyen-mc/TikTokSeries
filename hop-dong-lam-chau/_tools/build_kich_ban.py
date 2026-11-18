#!/usr/bin/env python3
"""Tách kịch bản "Hợp Đồng Làm Cháu" (bản 2) thành từng cảnh: kich-ban/canh-XX.md + kich-ban/README.md.
Cảnh 00–06 lấy bảng shot từ build_shots.py (bản V3 đã render); cảnh 07–20 là bảng shot đề xuất trong file này.
Chạy từ thư mục gốc repo: python3 hop-dong-lam-chau/_tools/build_kich_ban.py"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import build_flow_files as B
import build_shots as S

LOOK = B.LOOK
FLOW = {c: LOOK[c]["flow"] for c in LOOK}
VN = {"BM1": "Bà Mận", "BM2": "Bà Mận", "BM3": "Bà Mận", "DA1": "Đạt", "DA2": "Đạt", "DA3": "Đạt", "DA4": "Đạt",
      "OT1": "Ông Thịnh", "OT2": "Ông Thịnh", "OT3": "Ông Thịnh", "OT4": "Ông Thịnh", "OT5": "Ông Thịnh (56 tuổi)",
      "MI0": "Minh (8 tuổi)", "MI1": "Minh", "MI2": "Minh", "MI3": "Minh", "BT1": "Bà Thoa", "BT2": "Bà Thoa", "BOM": "Bố Minh"}

# ------------------------------------------------------------------ dàn ý từng cảnh (bản 2, đã sửa mốc giờ)
# số: (tên, hồi, thời điểm, bối cảnh, [bộ đồ], mở, [diễn biến], câu treo)
SC = {
"00": ("Mở đầu", "Mở đầu", "sáng 29 Tết (chớp tới)", "B5 cổng nhà",
       ["MI2", "DA3", "BT1", "OT2"],
       "Cổng treo đèn lồng, hai thanh niên đứng đối diện nhau.",
       ["Bà Thoa giơ điện thoại qua rào: \"Thế đứa nào là cháu thật?\"",
        "Ông chống gậy ra hiên, nhìn cả hai, rồi nói với Đạt: \"Minh, vào ăn sáng con.\"",
        "Cận mặt Minh chết lặng. Cắt đen."],
       "Tiếng xe khách phanh thay cho chữ \"Ba ngày trước\"."),
"01": ("Đơn hàng cháu đích tôn", "Hồi 1 · Cháu thuê", "sáng 26 Tết", "B8 bến xe huyện",
       ["BM1", "DA1"],
       "Đạt xuống xe khách, lẩm nhẩm tập câu \"Ông ơi, cháu về rồi\".",
       ["Bà Mận túm tay áo Đạt kéo ra góc bến, dúi phong bì: \"Năm ngày thôi. Cháu làm cháu nội tôi, đừng để ông biết.\"",
        "Bà đọc hợp đồng như đọc văn khấn: không để ông biết; không lên gác mở tủ gỗ; phải đi trước giao thừa. Điều năm của công ty: lộ thì đền gấp đôi. Đạt khựng một nhịp rồi vẫn gật.",
        "Bà dặn: \"Từ hôm tai biến ông hay lẫn. Hôm trước còn gọi tôi bằng tên thằng con. Nhưng chuyện thằng Minh thì ông nhớ từng tí.\"",
        "Đạt hỏi về \"cháu\". Bà: \"Nó hiền, ít nói.\" Đạt: \"Ít nói thì cháu diễn được.\"",
        "Bà vừa quay đi, Đạt gọi về mái ấm: \"Cô ơi, cháu chuyển tiền rồi. Cô mua bánh chưng cho các em nhé. Năm nay các em có Tết rồi.\""],
       "Bà quay lại nắm chặt tay Đạt: \"Lộ ra là ông đuổi cả hai bà cháu ra đường đấy.\" Tiền đã gửi, không còn đường lùi."),
"02": ("Mười năm mà mày lùn đi à?", "Hồi 1 · Cháu thuê", "chiều 26 Tết", "B5 ngõ làng, B1 sân nhà",
       ["OT1", "DA1", "BM1"],
       "Ông Thịnh ngồi giữa sân, sơn lại một chiếc ghế gỗ trẻ con bé xíu.",
       ["Đạt ào vào ôm chầm: \"Ông ơi! Cháu về rồi!\" Cái ôm cứng đơ.",
        "Ông nhìn rất lâu: \"Mày là…\" Bà Mận nín thở. \"…thằng Minh. Mười năm mà mày lùn đi à?\"",
        "Bà cười gượng: \"Thành phố người ta ăn uống kham khổ.\" Đạt: \"Dạ… kham khổ lắm ông ạ.\"",
        "Đạt hỏi: \"Ghế của ai mà bé thế hả ông?\" Ông: \"Của một thằng không ngồi nữa.\""],
       "Ông quay vào nhà. Cận mắt ông thoáng liếc xuống cằm nhẵn của Đạt, chưa đến một giây."),
"03": ("Thi kiến thức cháu đích tôn", "Hồi 1 · Cháu thuê", "chiều 26 Tết, tiếp liền cảnh 02", "B1 sân, rào nhà bà Thoa",
       ["BT1", "DA1", "BM2", "OT1"],
       "Bà Thoa ló điện thoại qua rào: \"Các cháu ơi, xem live với bà nhé! Cháu đích tôn nhà ông Thịnh mười năm mới về này!\"",
       ["Bà Thoa sang hỏi dồn như gameshow: \"Mẹ mày tên gì?\" Đạt: \"Dạ… mẹ cháu tên là… Mẹ ạ!\"",
        "\"Năm lớp mấy mày đái dầm ở nhà bà?\" Bà Mận ho sặc.",
        "\"Thế hồi bé mày ngã cây gì?\" Đạt cứng họng. Ông đang bào gỗ, không ngẩng lên: \"Cây bưởi. Nó ngã cây bưởi.\"",
        "Bà Mận thì thầm: \"Ông vẫn nhớ cái đấy cơ à…\""],
       "Bà Thoa nheo mắt nhìn Đạt đang nhai kẹo lạc: \"Lạ nhỉ. Thằng Minh hồi bé dị ứng lạc cơ mà?\""),
"04": ("Dị ứng theo yêu cầu", "Hồi 1 · Cháu thuê", "chiều tối 26 Tết, đến đêm", "B1 sân, B4 bếp, B3 gác xép",
       ["DA1", "DA2", "BT1", "OT1", "OT3", "BM2"],
       "Đạt phun kẹo lạc: \"Ối! Ngứa! Ngứa quá!\", lăn ra phản. Diễn quá đà đến mức bà Thoa phải lùi lại rồi về.",
       ["Ông đẩy đĩa kẹo lạc sang: \"Ăn đi. Khỏi rồi.\"",
        "Ngoài bếp, bà Mận chấm nước mắt: \"Ông lẫn thật rồi. Đến cả chuyện thằng cháu dị ứng cũng quên.\" (đánh lạc hướng)",
        "Đêm trên gác xép, Đạt thấy cái tủ gỗ khóa móc. Đạt gọi cho \"sếp\": \"Ba mươi triệu… em biết rồi anh. Tiền cọc em gửi về mái ấm rồi. Em nhận vụ này vì tiền. Với lại… em muốn biết Tết có ông bà nó thế nào.\""],
       "Dưới sân vọng lên tiếng bào gỗ giữa đêm, rồi tắt. Tiếng ho khẽ ở chân cầu thang: ông đã đứng đó bao lâu?"),
"05": ("Cành đào xấu nhất chợ", "Hồi 1 · Cháu thuê", "sáng 27 Tết", "B6 chợ hoa huyện",
       ["OT2", "DA2"],
       "Ông chống gậy giữa chợ hoa: \"Mày chọn đi. Như mọi năm.\"",
       ["Đạt không biết \"mọi năm\" là thế nào, chọn đại một cành khẳng khiu, cong queo: \"Cành này không ai mua thì nó buồn.\"",
        "Ông khựng lại: thằng Minh hồi bé cũng nói đúng câu ấy. Ông trả tiền, không mặc cả, mắt đỏ hoe."],
       "Lần đầu ông gọi: \"Về thôi, cháu.\" (gọi \"cháu\", không gọi \"Minh\")."),
"06": ("Gói bánh chưng", "Hồi 2 · Cháu giả, Tết thật", "chiều 27 Tết", "B1 sân, lá dong, khuôn gỗ",
       ["OT1", "DA2", "BM2"],
       "Cận tay ông gói bánh vuông vức. Bánh của Đạt méo như cái gối.",
       ["Ông: \"Bánh này mà đặt lên bàn thờ, các cụ tưởng nhà mình nghèo.\" Bà cười. Đạt: \"Méo nhưng mà chắc ạ!\"",
        "Ông: \"Ngày xưa bố thằng Minh gói vuông nhất làng.\"",
        "Đạt buột miệng: \"Bố cháu… mất thế nào hả ông?\" Bà đánh rơi lạt."],
       "Ông buộc lạt, không ngẩng lên: \"Mày hỏi như người ngoài ấy.\""),
"07": ("Đêm canh nồi bánh", "Hồi 2 · Cháu giả, Tết thật", "đêm 27 Tết", "B1 bếp lửa ngoài sân",
       ["OT3", "DA2", "BT1"],
       "Lửa củi, nồi bánh sôi, hai ông cháu ngồi trên hai cái đòn kê thấp.",
       ["Ông kể chuyện mười năm trước: đám tang con trai, cãi nhau với con dâu, rồi câu nói với thằng cháu 18 tuổi: \"Đi rồi thì đừng về.\" \"Ông nói câu đấy. Nó nghe thật.\"",
        "Đạt nhập vai rồi lạc vai: \"Ông có giận cháu không?\" Ông: \"Ông không giận cháu. Ông giận ông.\"",
        "Đạt khóc, lần này không diễn."],
       "Bên kia rào, màn hình điện thoại bà Thoa sáng lên trong bóng tối. Bà đã quay hết."),
"08": ("Hai triệu người xem", "Hồi 2 · Cháu giả, Tết thật", "rạng sáng 28 Tết, ca đêm", "B9 bếp nhà hàng thành phố",
       ["MI1"],
       "Chảo lửa bùng, Minh đảo chảo, mặt lạnh tanh.",
       ["Đồng nghiệp (quần chúng): \"Mùng hai bay rồi mà vẫn đứng bếp à? Tết này không về quê chào ai à?\" Minh: \"Không có ai để chào.\"",
        "Giờ nghỉ, đồng nghiệp chìa điện thoại: \"Ông cụ khóc bên nồi bánh chưng với cháu đích tôn, hai triệu view rồi. Ê, sao giống ông mày kể thế?\"",
        "Minh xem: ông ngồi cạnh một thằng lạ, gọi nó là \"cháu\"."],
       "Minh cởi tạp dề: \"Thằng đấy là ai?\""),
"09": ("Tảo mộ", "Hồi 2 · Cháu giả, Tết thật", "chiều 28 Tết", "B7 nghĩa trang giữa đồng",
       ["DA2", "OT2", "BOM"],
       "Khói hương bay ngang ruộng.",
       ["Đạt đứng trước mộ bố Minh, thì thầm thật lòng: \"Cháu xin lỗi chú. Cháu mượn tên con chú mấy hôm. Cháu sẽ trả.\"",
        "Ông đứng sau lưng, nghe hết."],
       "Ông không nói gì, chỉ đặt tay lên vai Đạt. Đạt quay lại, không biết ông đã nghe được bao nhiêu."),
"10": ("Lý do thật của bà", "Hồi 2 · Cháu giả, Tết thật", "tối 28 Tết", "B4 bếp; B8 đầu làng",
       ["DA3", "BM2", "MI2"],
       "Đạt xách ba lô: \"Bà ơi, cháu không diễn được nữa. Tiền cọc cháu tiêu rồi, cháu xin làm thuê trả dần.\"",
       ["Bà giữ tay Đạt, khóc: năm ngoái ông bị tai biến, bác sĩ dặn đừng để ông buồn, mà đêm nào ông cũng ra cổng ngồi đến khuya.",
        "\"Bà nhắn tin cho thằng Minh mười năm, không một lần có hồi âm. Bà sợ Tết này là Tết cuối của ông.\"",
        "Đạt lặng lẽ đặt ba lô xuống."],
       "Xe khách dừng ở đầu làng trong đêm. Một đôi giày bước xuống. Minh."),
"11": ("Hai thằng Minh", "Hồi 2 · Cháu giả, Tết thật", "sáng 29 Tết", "B5 cổng nhà",
       ["DA3", "MI2", "BT1", "BM2", "OT2"],
       "Đạt kiễng chân treo đèn lồng. Cổng mở.",
       ["Hai người nhìn nhau. Bà Thoa giơ điện thoại: \"Thế đứa nào là cháu thật?\"",
        "Đạt nhanh trí: \"Anh… anh là shipper giao đào phải không ạ?\" Minh: \"Tôi là cháu nhà này.\"",
        "Bà Mận đánh rơi rổ bánh. Cận rất nhanh vết sẹo trên cằm Minh."],
       "Ông bước ra hiên, nhìn Minh, nhìn Đạt, rồi nói với Đạt: \"Minh, vào ăn sáng con.\" Minh chết lặng."),
"12": ("Bữa sáng của anh shipper", "Hồi 2 · Cháu giả, Tết thật", "sáng 29 Tết", "B2 mâm cơm gian giữa, B4 bếp",
       ["OT2", "BM2", "DA3", "MI2"],
       "Ba người ngồi mâm, \"anh shipper\" ngồi thêm một bên. Chiếc ghế gỗ bé xíu để trống cạnh mâm.",
       ["Minh thử ông: \"Cháu nghe nói cháu nội ông dị ứng lạc?\" Ông: \"Ừ. Khỏi rồi.\"",
        "Minh ăn lạc để chứng minh, cổ tay nổi mẩn đỏ. Ông thấy, rồi quay đi.",
        "Bà kéo Minh ra bếp, ôm cháu khóc không thành tiếng. Minh: \"Con đổi số từ năm thứ hai, bà ạ.\" Bà giơ điện thoại: mười năm tin nhắn gửi vào một số không còn ai dùng."],
       "Minh: \"Ông không nhận ra con, hay ông không muốn nhận?\" Bà: \"Ông lẫn rồi con ạ.\""),
"13": ("Ba mươi triệu", "Hồi 3 · Hai đứa cháu", "trưa 29 Tết", "B4 sau nhà, bờ ao",
       ["MI2", "DA3", "BT1"],
       "Minh túm cổ áo Đạt rồi buông ngay: \"Bao nhiêu tiền?\" \"Mười lăm triệu. Lộ thì đền ba mươi.\"",
       ["Minh rút điện thoại: \"Tôi trả ba mươi. Đủ đền. Đi đi.\"",
        "Đạt nhìn màn hình rất lâu, rồi cất tay vào túi: \"Anh vắng mười năm, giờ trả tiền để ông có cháu à? Thế anh khác gì em?\"",
        "Không ai đánh ai, chỉ có hai người đứng thở."],
       "Bên kia rào, bà Thoa áp điện thoại vào ngực, mắt sáng rực: \"Cháu thuê!\""),
"14": ("Livestream bóc phốt", "Hồi 3 · Hai đứa cháu", "chiều 29 Tết", "B1 sân nhà, cả xóm",
       ["BT1", "DA3", "MI2", "OT2", "BM2"],
       "Bà Thoa đứng giữa sân nói vào điện thoại: \"Các cháu ơi, cháu đích tôn nhà ông Thịnh là cháu thuê!\"",
       ["Hàng xóm kéo đến chật cổng. Có người nói: \"Tội ông, lẫn rồi nên bị lừa.\"",
        "Đạt bước ra nhận hết: \"Cháu lừa ông bà. Ông bà không biết gì.\" Minh im lặng."],
       "Cú lật. Ông chống gậy ra giữa sân: \"Tôi quên tắt bếp. Tôi quên cả tên bà nhà tôi. Nhưng thằng cháu tôi có cái sẹo ở cằm, ngã cây bưởi năm tám tuổi, chính tôi cõng nó đi khâu. Thằng này cằm nhẵn thín. Tôi biết từ lúc nó bước qua cổng.\""),
"15": ("Bà khoe cháu đi Nhật", "Hồi 3 · Hai đứa cháu", "chiều 29 Tết, tiếp liền", "B1 sân nhà",
       ["BM2", "OT2", "BT1", "MI2"],
       "Cả xóm im phăng phắc. Bà Mận ngồi phịch xuống bậc thềm: \"Thế… ông biết mà ông vẫn…\"",
       ["Ông quay sang bà Thoa: \"Bà khoe cháu đi Nhật năm năm nay, nó gọi về được mấy lần?\"",
        "Tay bà Thoa run. Bà tắt live, nói nhỏ: \"Nó đổi số rồi. Tôi live… là để có người nghe tôi nói.\"",
        "Ông: \"Tôi biết nó giả. Nhưng nó ngồi canh nồi bánh với tôi. Còn thằng thật thì mười năm…\" Lần đầu ông nhìn thẳng vào Minh."],
       "Minh bùng nổ: \"Ông bảo con đừng về cơ mà!\""),
"16": ("Đêm hai mươi chín năm ấy", "Hồi 3 · Hai đứa cháu", "chiều 29 Tết", "B2 gian thờ; B5 cổng",
       ["MI2", "OT2", "BOM", "DA3"],
       "Di ảnh bố Minh trên bàn thờ, khói hương thẳng đứng. Chỉ có hai ông cháu.",
       ["Minh trút hết: 18 tuổi, đứng ở đám tang bố, nghe ông nói câu ấy.",
        "\"Con về một lần rồi. Năm năm trước, đêm hai mươi chín. Con đứng ở cổng, thấy ông ngồi đấy. Ông nhìn con… rồi ông đứng dậy đi vào.\" Ông sững người.",
        "Minh: \"Mùng hai con bay. Con về để chào ông.\" Ông quay lưng: \"Thế thì chào đi.\" Minh xách ba lô ra cổng."],
       "Đạt đứng chặn ở cổng: \"Anh có biết đêm nào ông cũng ngồi ở cái cổng này không?\""),
"17": ("Cái tủ gỗ", "Hồi 3 · Hai đứa cháu", "chiều 30 Tết", "B3 gác xép; B5 cổng",
       ["BM2", "DA3", "MI2"],
       "Bà Mận đưa chìa khóa cho Đạt: \"Cháu mở đi. Điều thứ ba bà bỏ.\"",
       ["Trong tủ: mười phong bao lì xì đỏ, mỗi năm một cái; mười tấm vé xe khách lên thành phố, chín tấm còn nguyên, một tấm đã bấm lỗ.",
        "Bà kể: năm nào ông cũng mua vé, ra đến bến lại quay về. \"Chỉ có một năm ông lên đến tận nơi. Đứng ngoài cửa kính nhìn con nấu bếp. Về bảo tôi: nó mặc áo trắng, đẹp như bố nó. Rồi ông không lên nữa.\"",
        "Minh lật tấm vé: \"Năm năm trước… Cùng năm ấy con cũng về.\" Minh ôm xấp vé, vỡ òa."],
       "Bà chạy xuống sân: \"Ông đâu?\" Chiếc ghế ở cổng trống không, chiếc gậy dựng bên cạnh."),
"18": ("Ông nói với con trai", "Hồi 3 · Hai đứa cháu", "hoàng hôn tất niên (chiều 30)", "B7 nghĩa trang, bờ ruộng",
       ["MI2", "OT3", "BOM", "OT5", "MI0", "DA3", "MI3", "BM2"],
       "Minh chạy dọc bờ ruộng. Từ xa thấy ông ngồi một mình trước mộ con trai, không có gậy.",
       ["Ông nói với tấm bia: \"Thằng Minh về rồi. Tao không biết nói với nó thế nào. Mười năm tao tập mỗi một câu mà đến lúc gặp thì không nói được.\" Minh đứng sau lưng, nghe hết.",
        "Minh ngồi xuống cạnh ông. Ông không quay sang: \"Sẹo còn không?\" Minh nghiêng cằm, ông đưa tay chạm vào.",
        "Chớp lui: ông ngày trước cõng thằng bé 8 tuổi băng gạc ở cằm chạy qua chính bờ ruộng này.",
        "Ông: \"Ông xin lỗi.\" Minh: \"Con về rồi mà ông.\" Minh cõng ông về qua bờ ruộng.",
        "Về nhà, bà đưa Minh chiếc áo len cũ của bố. Minh vào bếp nấu mâm tất niên."],
       "Đạt xếp ba lô. Sắp giao thừa, hợp đồng hết hạn. Đạt khẽ khép cổng, không chào ai."),
"19": ("Phong bao thứ mười một", "Hồi 3 · Hai đứa cháu", "tối 30 Tết, sát giao thừa", "B8 bến xe huyện",
       ["DA3", "MI3", "BT2"],
       "Đạt ngồi một mình ở bến xe vắng, gọi về mái ấm: \"Các em ăn Tết vui không cô?\"",
       ["Minh phóng xe máy đến, đội mũ bảo hiểm. Bà Thoa đi xe ôm theo sau, ôm khư khư một cái hộp.",
        "Minh đưa Đạt phong bao thứ mười một, mới tinh: \"Ông bảo hợp đồng hết hạn rồi. Nhưng ông chưa ký hợp đồng nào cả. Ông chỉ có cháu.\"",
        "Bà Thoa mở hộp: chiếc ghế gỗ thứ hai, mùn cưa còn bám. \"Ông đóng bốn đêm. Ông bảo đóng cho thằng cháu chưa từng có ghế.\""],
       "Đạt nhìn đồng hồ: còn mười phút nữa là giao thừa. \"Không kịp đâu.\" Minh nổ máy, ném cho Đạt chiếc mũ bảo hiểm."),
"20": ("Xông đất", "Hồi 3 · Hai đứa cháu", "giao thừa → sáng mùng 1", "B5 cổng, B2 mâm cơm",
       ["OT4", "BM3", "MI3", "DA3", "DA4", "BT2", "BOM"],
       "Ông bà đứng trên hiên, pháo hoa nổ xa xa. Xe máy dừng ở đầu ngõ đúng lúc giao thừa.",
       ["Ông: \"Năm nay nhà này hai đứa xông đất.\" Minh và Đạt cùng bước qua cổng.",
        "Mâm cơm giao thừa Minh nấu, bánh chưng vuông y như bố Minh ngày xưa gói, cành đào cong queo cạnh mâm, hai chiếc ghế gỗ. Minh to xác ngồi lọt thỏm trên ghế bé, cả nhà cười.",
        "Ông chỉ chiếc ghế mới, lần đầu gọi tên thật: \"Đạt. Ngồi đây con.\" Bà Thoa được mời sang, ngồi cuối mâm, không cầm điện thoại.",
        "Ông đặt mười phong bao vào tay Minh: \"Mười cái Tết. Cầm lấy. Đi đâu thì đi. Nhớ đường về.\""],
       "Sáng mùng 1, chụp ảnh gia đình ở cổng. Bà Thoa giơ máy: \"Thế đứa nào là cháu thật?\" Ông: \"Cả hai.\" Đóng băng khung hình."),
}

# ------------------------------------------------------------------ bảng shot đề xuất cho cảnh 07–20
# (tên shot, giây, [bộ đồ], [(bộ đồ người nói, câu)])
P = {
"07": [("Lửa củi, nồi bánh sôi", 4, [], []),
       ("Hai ông cháu bên lửa", 5, ["OT3", "DA2"], []),
       ("Mười năm trước", 6, ["OT3"], [("OT3", "Mười năm trước, đám ma bố nó. Ông cãi nhau với mẹ nó.")]),
       ("Đi rồi thì đừng về", 5, ["OT3"], [("OT3", "Ông bảo nó: đi rồi thì đừng về.")]),
       ("Nó nghe thật", 5, ["OT3"], [("OT3", "Ông nói câu đấy. Nó nghe thật.")]),
       ("Đạt nhìn ông", 3, ["DA2"], []),
       ("Ông có giận cháu không", 4, ["DA2"], [("DA2", "Ông… ông có giận cháu không?")]),
       ("Ông giận ông", 5, ["OT3", "DA2"], [("OT3", "Ông không giận cháu. Ông giận ông.")]),
       ("Đạt khóc thật", 4, ["DA2"], []),
       ("Màn hình sáng sau rào", 3, ["BT1"], [])],
"08": [("Chảo lửa bùng", 4, ["MI1"], []),
       ("Mùng hai bay rồi", 5, ["MI1"], [("", "Đồng nghiệp (ngoài hình): Mùng hai bay rồi mà vẫn đứng bếp à?"), ("MI1", "Không có ai để chào.")]),
       ("Giờ nghỉ cửa sau", 4, ["MI1"], []),
       ("Hai triệu view", 6, ["MI1"], [("", "Đồng nghiệp (ngoài hình): Ông cụ khóc bên nồi bánh chưng với cháu đích tôn, hai triệu view rồi. Sao giống ông mày kể thế?")]),
       ("Ánh màn hình trên mặt", 4, ["MI1"], []),
       ("Thằng đấy là ai", 4, ["MI1"], [("MI1", "Thằng đấy… là ai?")]),
       ("Cởi tạp dề", 3, ["MI1"], [])],
"09": [("Khói hương ngang ruộng", 4, [], []),
       ("Đạt trước mộ", 4, ["DA2", "BOM"], []),
       ("Cháu mượn tên", 7, ["DA2"], [("DA2", "Cháu xin lỗi chú. Cháu mượn tên con chú mấy hôm. Cháu sẽ trả.")]),
       ("Ông đứng sau lưng", 4, ["OT2"], []),
       ("Bàn tay trên vai", 4, ["OT2", "DA2"], []),
       ("Đạt quay lại", 3, ["DA2"], [])],
"10": [("Đạt xách ba lô", 6, ["DA3"], [("DA3", "Bà ơi, cháu không diễn được nữa. Tiền cọc cháu tiêu rồi, cháu xin làm thuê trả dần.")]),
       ("Bà giữ tay", 4, ["BM2", "DA3"], []),
       ("Đêm nào ông cũng ra cổng", 7, ["BM2"], [("BM2", "Năm ngoái ông tai biến. Bác sĩ dặn đừng để ông buồn. Mà đêm nào ông cũng ra cổng ngồi.")]),
       ("Mười năm không hồi âm", 6, ["BM2"], [("BM2", "Bà nhắn cho thằng Minh mười năm, không một lần nó trả lời.")]),
       ("Tết cuối", 4, ["BM2"], [("BM2", "Bà sợ Tết này là Tết cuối của ông.")]),
       ("Đặt ba lô xuống", 3, ["DA3"], []),
       ("Xe khách đầu làng", 4, [], []),
       ("Đôi giày bước xuống", 3, ["MI2"], [])],
"11": [("Treo đèn lồng", 4, ["DA3"], []),
       ("Cổng mở", 4, ["MI2", "DA3"], []),
       ("Đứa nào cháu thật", 3, ["BT1"], [("BT1", "Thế đứa nào là cháu thật?")]),
       ("Anh shipper", 4, ["DA3"], [("DA3", "Anh… anh là shipper giao đào phải không ạ?")]),
       ("Tôi là cháu nhà này", 3, ["MI2"], [("MI2", "Tôi là cháu nhà này.")]),
       ("Rơi rổ bánh", 3, ["BM2"], []),
       ("Vết sẹo", 2, ["MI2"], []),
       ("Minh vào ăn sáng", 4, ["OT2"], [("OT2", "Minh, vào ăn sáng con.")]),
       ("Minh chết lặng", 3, ["MI2"], [])],
"12": [("Mâm cơm bốn người", 5, ["OT2", "DA3"], []),
       ("Ghế bé để trống", 3, [], []),
       ("Cháu nội dị ứng lạc", 4, ["MI2"], [("MI2", "Cháu nghe nói cháu nội ông dị ứng lạc?")]),
       ("Khỏi rồi", 3, ["OT2"], [("OT2", "Ừ. Khỏi rồi.")]),
       ("Minh ăn lạc", 4, ["MI2"], []),
       ("Cổ tay nổi mẩn", 3, ["MI2"], []),
       ("Ông quay đi", 3, ["OT2"], []),
       ("Bà ôm cháu trong bếp", 5, ["BM2", "MI2"], []),
       ("Đổi số năm thứ hai", 4, ["MI2"], [("MI2", "Con đổi số từ năm thứ hai, bà ạ.")]),
       ("Mười năm tin nhắn", 4, ["BM2"], []),
       ("Không muốn nhận", 5, ["MI2"], [("MI2", "Ông không nhận ra con, hay ông không muốn nhận?")]),
       ("Ông lẫn rồi", 3, ["BM2"], [("BM2", "Ông lẫn rồi con ạ.")])],
"13": [("Túm cổ áo", 4, ["MI2", "DA3"], [("MI2", "Bao nhiêu tiền?")]),
       ("Đền ba mươi", 4, ["DA3"], [("DA3", "Mười lăm triệu. Lộ thì đền ba mươi.")]),
       ("Tôi trả ba mươi", 5, ["MI2"], [("MI2", "Tôi trả ba mươi. Đủ đền. Đi đi.")]),
       ("Đạt nhìn màn hình", 4, ["DA3"], []),
       ("Thế anh khác gì em", 7, ["DA3"], [("DA3", "Anh vắng mười năm, giờ trả tiền để ông có cháu à? Thế anh khác gì em?")]),
       ("Hai người đứng thở", 4, ["MI2", "DA3"], []),
       ("Cháu thuê", 3, ["BT1"], [("BT1", "Cháu thuê!")])],
"14": [("Bóc phốt giữa sân", 6, ["BT1"], [("BT1", "Các cháu ơi, cháu đích tôn nhà ông Thịnh là cháu thuê!")]),
       ("Xóm kéo đến", 4, [], [("", "Quần chúng: Tội ông, lẫn rồi nên bị lừa.")]),
       ("Cháu lừa ông bà", 5, ["DA3"], [("DA3", "Cháu lừa ông bà. Ông bà không biết gì.")]),
       ("Minh im lặng", 3, ["MI2"], []),
       ("Ông chống gậy ra sân", 4, ["OT2"], []),
       ("Tôi quên tắt bếp", 6, ["OT2"], [("OT2", "Tôi quên tắt bếp. Tôi quên cả tên bà nhà tôi.")]),
       ("Cái sẹo cây bưởi", 7, ["OT2"], [("OT2", "Nhưng thằng cháu tôi có cái sẹo ở cằm, ngã cây bưởi năm tám tuổi, chính tôi cõng nó đi khâu.")]),
       ("Cằm nhẵn thín", 3, ["DA3"], [("OT2", "Thằng này cằm nhẵn thín.")]),
       ("Biết từ lúc qua cổng", 5, ["OT2"], [("OT2", "Tôi biết từ lúc nó bước qua cổng.")])],
"15": [("Cả xóm im lặng", 3, [], []),
       ("Ông biết mà ông vẫn", 5, ["BM2"], [("BM2", "Thế… ông biết mà ông vẫn…")]),
       ("Cháu đi Nhật", 6, ["OT2"], [("OT2", "Bà khoe cháu đi Nhật năm năm nay, nó gọi về được mấy lần?")]),
       ("Tay bà Thoa run", 3, ["BT1"], []),
       ("Có người nghe tôi nói", 6, ["BT1"], [("BT1", "Nó đổi số rồi. Tôi live… là để có người nghe tôi nói.")]),
       ("Nó ngồi canh nồi bánh", 7, ["OT2"], [("OT2", "Tôi biết nó giả. Nhưng nó ngồi canh nồi bánh với tôi. Còn thằng thật thì mười năm…")]),
       ("Ông nhìn Minh", 3, ["OT2", "MI2"], []),
       ("Ông bảo con đừng về", 4, ["MI2"], [("MI2", "Ông bảo con đừng về cơ mà!")])],
"16": [("Di ảnh, khói hương", 4, ["BOM"], []),
       ("Đám tang năm ấy", 6, ["MI2"], [("MI2", "Con mười tám tuổi, đứng ở đám tang bố, nghe ông nói câu ấy.")]),
       ("Con về một lần rồi", 7, ["MI2"], [("MI2", "Con về một lần rồi. Năm năm trước, đêm hai mươi chín. Con đứng ở cổng, thấy ông ngồi đấy.")]),
       ("Ông đứng dậy đi vào", 5, ["MI2"], [("MI2", "Ông nhìn con… rồi ông đứng dậy đi vào.")]),
       ("Ông sững người", 4, ["OT2"], []),
       ("Mùng hai con bay", 5, ["MI2"], [("MI2", "Mùng hai con bay. Con về để chào ông.")]),
       ("Thế thì chào đi", 4, ["OT2"], [("OT2", "Thế thì chào đi.")]),
       ("Xách ba lô ra cổng", 4, ["MI2"], []),
       ("Đạt chặn cổng", 6, ["DA3", "MI2"], [("DA3", "Anh có biết đêm nào ông cũng ngồi ở cái cổng này không?")])],
"17": [("Chìa khóa", 5, ["BM2", "DA3"], [("BM2", "Cháu mở đi. Điều thứ ba bà bỏ.")]),
       ("Ổ khóa bật", 3, ["DA3"], []),
       ("Mười phong bao", 4, [], []),
       ("Mười tấm vé xe", 4, [], []),
       ("Năm nào cũng mua vé", 6, ["BM2"], [("BM2", "Năm nào ông cũng mua vé. Ra đến bến lại quay về.")]),
       ("Đứng ngoài cửa kính", 8, ["BM2"], [("BM2", "Chỉ có một năm ông lên đến tận nơi. Đứng ngoài cửa kính nhìn con nấu bếp. Về bảo tôi: nó mặc áo trắng, đẹp như bố nó.")]),
       ("Tấm vé bấm lỗ", 4, ["MI2"], []),
       ("Cùng năm ấy", 5, ["MI2"], [("MI2", "Năm năm trước… Cùng năm ấy con cũng về.")]),
       ("Minh vỡ òa", 4, ["MI2"], []),
       ("Ông đâu", 3, ["BM2"], [("BM2", "Ông đâu?")]),
       ("Ghế ở cổng trống", 4, [], [])],
"18": [("Chạy dọc bờ ruộng", 5, ["MI2"], []),
       ("Ông ngồi trước mộ", 5, ["OT3", "BOM"], []),
       ("Tao không biết nói", 8, ["OT3"], [("OT3", "Thằng Minh về rồi. Tao không biết nói với nó thế nào.")]),
       ("Mười năm tập một câu", 7, ["OT3"], [("OT3", "Mười năm tao tập mỗi một câu mà đến lúc gặp thì không nói được.")]),
       ("Minh đứng sau lưng", 3, ["MI2"], []),
       ("Ngồi xuống cạnh ông", 4, ["MI2", "OT3"], []),
       ("Sẹo còn không", 4, ["OT3"], [("OT3", "Sẹo còn không?")]),
       ("Ông chạm vào sẹo", 4, ["OT3", "MI2"], []),
       ("Chớp lui: cõng cháu", 5, ["OT5", "MI0"], []),
       ("Ông xin lỗi", 5, ["OT3", "MI2"], [("OT3", "Ông xin lỗi."), ("MI2", "Con về rồi mà ông.")]),
       ("Cõng ông qua bờ ruộng", 6, ["MI2", "OT3"], []),
       ("Áo len của bố", 4, ["BM2", "MI3"], []),
       ("Đạt khép cổng", 4, ["DA3"], [])],
"19": [("Bến xe vắng", 4, ["DA3"], []),
       ("Gọi về mái ấm", 5, ["DA3"], [("DA3", "Các em ăn Tết vui không cô?")]),
       ("Xe máy phóng đến", 4, ["MI3"], []),
       ("Phong bao thứ mười một", 5, ["MI3", "DA3"], []),
       ("Ông chỉ có cháu", 8, ["MI3"], [("MI3", "Ông bảo hợp đồng hết hạn rồi. Nhưng ông chưa ký hợp đồng nào cả. Ông chỉ có cháu.")]),
       ("Bà Thoa mở hộp", 4, ["BT2"], []),
       ("Chiếc ghế thứ hai", 6, ["BT2"], [("BT2", "Ông đóng bốn đêm. Ông bảo đóng cho thằng cháu chưa từng có ghế.")]),
       ("Còn mười phút", 4, ["DA3"], [("DA3", "Không kịp đâu.")]),
       ("Minh nổ máy", 3, ["MI3", "DA3"], [])],
"20": [("Pháo hoa xa", 4, ["OT4", "BM3"], []),
       ("Xe dừng đầu ngõ", 3, ["MI3", "DA3"], []),
       ("Hai đứa xông đất", 5, ["OT4"], [("OT4", "Năm nay nhà này hai đứa xông đất.")]),
       ("Bước qua cổng", 4, ["MI3", "DA3"], []),
       ("Mâm cơm giao thừa", 5, ["OT4", "BM3"], []),
       ("Minh ngồi ghế bé", 4, ["MI3"], []),
       ("Đạt, ngồi đây con", 5, ["OT4", "DA3"], [("OT4", "Đạt. Ngồi đây con.")]),
       ("Bà Thoa cuối mâm", 3, ["BT2"], []),
       ("Mười cái Tết", 6, ["OT4", "MI3"], [("OT4", "Mười cái Tết. Cầm lấy.")]),
       ("Nhớ đường về", 5, ["OT4"], [("OT4", "Đi đâu thì đi. Nhớ đường về.")]),
       ("Ảnh mùng 1", 4, ["BT2"], [("BT2", "Thế đứa nào là cháu thật?")]),
       ("Cả hai", 4, ["OT4", "DA4"], [("OT4", "Cả hai.")])],
}

# trạng thái sản xuất
DONE = {"00", "01", "02", "03", "04", "05", "06"}

CHECK = [
    ("Trục thời gian cảnh 03–08 bị ngược", "Nhãn V3: cảnh 03, 04, 05 đều \"27 Tết\" nhưng cảnh 04 kết ở đêm (gác xép) rồi cảnh 05 lại là sáng chợ hoa; cảnh 06 \"sáng 28\", cảnh 07 đêm canh bánh lại đứng trước cảnh 09 \"chiều 28\"; video phải lan ra (08) trước khi Minh về (cuối 10, đêm 28).",
     "Trục mới: **26** = 01 sáng, 02 chiều, 03 chiều (bà Thoa sang ngay khi thấy cháu về), 04 chiều tối → đêm. **27** = 05 chợ hoa sáng, 06 gói bánh chiều, 07 đêm canh bánh. **28** = 08 rạng sáng, 09 chiều, 10 tối, Minh về đêm 28. **29** = 11–16. **30** = 17–20. Shot V3 không phải quay lại, chỉ sửa nhãn; Đạt mặc bomber suốt ngày 26 nên càng liền mạch."),
    ("Cảnh 19: ba người và một cái hộp trên một xe máy", "Minh chở bà Thoa ôm hộp ghế đến bến, rồi lại chở Đạt về: xe máy không chở nổi ba người cộng cái ghế.",
     "Bà Thoa **đi xe ôm theo sau**, giao hộp xong ở lại; Minh chở Đạt về, ném cho Đạt mũ bảo hiểm (đã ghi vào cảnh 19)."),
    ("Cảnh 20: Minh nấu mâm giao thừa nhưng ngay trước đó còn ở bến xe", "Cảnh 19 kết khi còn 10 phút là giao thừa, Minh không thể vừa nấu vừa đi đón Đạt.",
     "Cho Minh **nấu mâm tất niên ở cuối cảnh 18** (sau khi cõng ông về), rồi mới phát hiện Đạt đi (đã ghi vào cảnh 18)."),
    ("Lúc nào Minh mặc áo len của bố (MI3)", "Bản 2 để MI3 từ cảnh 18 nhưng không có lúc nào Minh thay đồ; cảnh 18 Minh chạy ra mộ ngay sau cảnh 17.",
     "Cảnh 18 Minh vẫn mặc **áo dạ đen (MI2)**; về nhà bà đưa áo len của bố, từ cảnh 19 mặc **MI3**. Thêm shot \"Áo len của bố\" ở cuối cảnh 18."),
    ("\"Ông đóng bốn đêm\" (cảnh 19)", "Với trục cũ, tiếng bào gỗ đêm đầu tiên là đêm 27, đến đêm 29 chỉ có ba đêm.",
     "Với trục mới (cảnh 04 là đêm 26), các đêm 26, 27, 28, 29 đúng **bốn đêm**: giữ nguyên câu của bản 2."),
    ("Trang phục bà Mận cảnh 02", "`NHAN_VAT_FLOW.md` ghi BM2 (áo cánh ở nhà) cho cảnh 02, nhưng shot V3 dùng BM1 (áo bông đi đường) vì bà vừa từ bến xe về cùng Đạt.",
     "Giữ **BM1** cho cảnh 02 như shot đã render; BM2 từ cảnh 03."),
    ("Trang phục Đạt cảnh 03–04", "Shot V3 03 và 04-01→04-07 mặc bomber (DA1), từ 04-09 (đêm) mới đổi áo len mượn (DA2).",
     "Khớp với trục mới: cả 02–04 là ngày 26, Đạt chưa thay đồ; tối 26 bà đưa áo len cũ (DA2)."),
    ("`NHAN_VAT_FLOW.md` còn theo bản 1", "OT3 (áo len đêm) còn ghi \"cảnh 18 nằm giường\"; chưa có prop chiếc ghế thứ hai, tấm vé bấm lỗ.",
     "Bảng bộ đồ theo cảnh ở mục dưới đã cập nhật theo bản 2. Cần sửa `_tools/build_flow_files.py` nếu muốn sinh lại file."),
    ("Câu mở đầu xuất hiện hai lần", "Cảnh 00 (mở đầu) và cảnh 11 dùng cùng sự kiện.",
     "Đúng ý đồ (chớp tới rồi quay lại). Cảnh 11 nên quay **góc khác** (từ trong sân nhìn ra, có thêm bà Mận đánh rơi rổ và câu \"anh shipper\") để khán giả không thấy lặp."),
]


def shots_v3(n):
    rows = []
    for sh in S.SCENES[n][1]:
        code, name, dur, place, looks, cam, action, lines, extra = sh
        thoai = " / ".join(f"{VN[c]}: {t}" for c, t, *_ in lines)
        rows.append((code, name, dur, looks, thoai))
    return rows


def shots_new(n):
    rows = []
    for i, (name, dur, looks, lines) in enumerate(P[n], 1):
        thoai = " / ".join((f"{VN[c]}: {t}" if c else t) for c, t in lines)
        rows.append((f"{n}-{i:02d}", name, dur, looks, thoai))
    return rows


def main():
    out = os.path.join(ROOT, "kich-ban")
    os.makedirs(out, exist_ok=True)
    idx = []
    total = 0
    for n, (ten, hoi, gio, canh, looks, mo, dien, treo) in SC.items():
        rows = shots_v3(n) if n in DONE else shots_new(n)
        sec = sum(r[2] for r in rows)
        total += sec
        st = "Đã render (V3)" if n in DONE else "Chưa quay — bảng shot đề xuất"
        L = [f"# Cảnh {n} · {ten}", "",
             f"**{hoi}** · {gio} · {canh} · ~{sec} giây · {len(rows)} shot · *{st}*", "",
             "## Nhân vật & bộ đồ (tên trên Flow)", ""]
        L += [f"- {FLOW[c]}" for c in looks] + ["", "## Kịch bản", "", f"**Mở:** {mo}", ""]
        L += [f"- {d}" for d in dien]
        L += ["", f"**Câu treo:** {treo}", "", "## Bảng shot", "",
              "| Shot | Tên | Giây | Đính trên Flow | Thoại |", "|---|---|---|---|---|"]
        for code, name, dur, lk, thoai in rows:
            L.append(f"| {code} | {name} | {dur} | {', '.join(FLOW[c] for c in lk) or '— (Text-to-Video)'} | {thoai or '—'} |")
        if n in DONE:
            L += ["", f"Prompt Flow từng shot: `film/v3/c{n}/`. Clip đã tải: `film/v3/clips/{n}-*.mp4`."]
        else:
            L += ["", "Thoại ghi \"(ngoài hình)\" là người không gắn nhân vật; khi viết prompt cho Omni nên để họ ở rìa khung, mờ, hoặc thu tiếng sau."]
        with open(os.path.join(out, f"canh-{n}.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(L) + "\n")
        idx.append((n, ten, hoi, gio, len(rows), sec, st))

    R = ["# Hợp Đồng Làm Cháu — Kịch bản từng cảnh", "",
         "*Sinh bởi `_tools/build_kich_ban.py` từ `CAU_CHUYEN_v2.md` (bản 2) và `film/v3/SHOTS.md`. Sửa trong script rồi chạy lại.*", "",
         f"**21 đoạn (cảnh 00 mở đầu + 20 cảnh) · {sum(i[4] for i in idx)} shot · ~{total // 60} phút {total % 60} giây.**", "",
         "| Cảnh | Tên | Hồi | Thời điểm | Shot | Giây | Trạng thái |", "|---|---|---|---|---|---|---|"]
    for n, ten, hoi, gio, k, sec, st in idx:
        R.append(f"| [{n}](canh-{n}.md) | {ten} | {hoi} | {gio} | {k} | {sec} | {st} |")
    R += ["", "## Kết quả rà kịch bản (18/11/2026)", "",
          "| # | Vấn đề | Chi tiết | Cách sửa |", "|---|---|---|---|"]
    for i, (a, b, c) in enumerate(CHECK, 1):
        R.append(f"| {i} | **{a}** | {b} | {c} |")
    R += ["", "Những điểm đã sửa trực tiếp trong các file cảnh: trục thời gian 03–08, cảnh 18 (Minh nấu mâm, thay áo len của bố), cảnh 19 (bà Thoa đi xe ôm, mũ bảo hiểm). `CAU_CHUYEN_v2.md` giữ nguyên.",
          "", "## Gài – trả: kiểm tra đã khớp", "",
          "Tất cả 16 cặp gài – trả trong bản 2 đều có cảnh trả tương ứng trong bảng shot (ghế gỗ 02→12→19→20; sẹo cằm 02→11→14→18; cây bưởi 03→14→18; dị ứng lạc 03→04→12; cành đào 05→20; bánh vuông 06→20; \"đi rồi thì đừng về\" 07→15→18→20; \"mùng hai bay\" 08→16→20; đứng sau lưng ở mộ 09↔18; \"cháu sẽ trả\" 09→20; ghế ở cổng 10→16→17; tin nhắn 10→12; \"các cháu\" của bà Thoa 03→14→15→20; đền 30 triệu 01→04→10→13; \"ông lẫn\" 01→04→12→14; tiếng bào gỗ 03→04→19)."]
    with open(os.path.join(out, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(R) + "\n")
    print(f"Xong: {len(idx)} cảnh, {sum(i[4] for i in idx)} shot, {total}s → kich-ban/")


if __name__ == "__main__":
    main()
