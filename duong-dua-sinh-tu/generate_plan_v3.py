#!/usr/bin/env python3
"""Generate PHAN_CANH_V3.json for the 40-minute (40 scenes × 6 clips = 240 clips) action film
'Đường Đua Sinh Tử: 10 Giây Tự Do' using the Global Film Bible & Spatial/Entity State Pipeline.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from film_bible import (
    AUDIO_STYLE,
    CHARACTER_LOCK,
    ENVIRONMENT_LOCK,
    GLOBAL_FILM_BIBLE,
    OBJECT_LOCK,
    VEHICLE_LOCK,
    VEHICLE_SFX_LOCK,
    resolve_object_condition,
    resolve_vehicle_condition,
)
from scene_staging import get_scene_staging

BASE_DIR = Path(__file__).resolve().parent

# Single Source of Truth derived from GLOBAL_FILM_BIBLE (film_bible.py)
IDENTITIES = {
    base_key: {
        "tag": c["tag"],
        "name": c["name"],
        "media_id": c["media_id"],
        "identity": c["identity"],
        "voice": c["voice"],
    }
    for base_key, c in CHARACTER_LOCK.items()
}

LOOKS = {
    look_key: [base_key, c["age"], costume_desc]
    for base_key, c in CHARACTER_LOCK.items()
    for look_key, costume_desc in c["costumes"].items()
}

LOCATIONS = {
    loc_key: [env["description"], env["ambient_sound"]]
    for loc_key, env in ENVIRONMENT_LOCK.items()
}

PROPS = {
    **{veh_key: v["description"] for veh_key, v in VEHICLE_LOCK.items()},
    **{obj_key: o["description"] for obj_key, o in OBJECT_LOCK.items()},
}

NARRATOR = {
    "name_vi": AUDIO_STYLE["narrator"]["name_vi"],
    "voice": AUDIO_STYLE["narrator"]["voice"],
    "voice_vi": AUDIO_STYLE["narrator"]["voice_vi"],
}


# 40 Scene specifications (4 Tập × 10 Cảnh = 40 Cảnh, 240 Clips = 40 Phút)
SCENE_SPECS = [
    # ACT 1 (Scenes 01–07): PHÂN CẢNH 1 — VỤ CƯỚP TRÊN ĐƯỜNG CAO TỐC BAN ĐÊM (THE TRUCK HEIST)
    (1, "Đêm Đen Xa Lộ 10", "N1 night", "HIGHWAY_NIGHT", ["VERNI"], ["RIG_18", "CIVIC_TRIO"], 4,
     "Verni điều khiển xe container 18 bánh chở hàng điện tử giữa đêm thì ba chiếc Civic đen đèn gầm xanh lá áp sát.",
     "Ai đang điều khiển ba chiếc xe đen vây quanh đầu kéo trên xa lộ?",
     "Ba vệt đèn neon xanh lá xé màn đêm khóa chặt ba phía xe tải.",
     "Verni phát hiện đội hình vây ép qua gương chiếu hậu và tăng cảnh giác.",
     "Mở màn phi vụ cướp container tốc độ cao và giới thiệu tài xế Verni."),
    (2, "Mũi Cáp Thép 130 KM/H", "N1 night", "HIGHWAY_NIGHT", ["CEVIN_H", "VERNI"], ["CIVIC_TRIO", "RIG_18", "HARPOON_CABLE"], 5,
     "Chiếc Civic đầu ép tốc độ xe tải trong khi Cevin nhô lên cửa sổ trời bắn mũi cáp thép bám chặt khung kính cabin.",
     "Cevin có bắn trúng điểm neo vào cabin xe đầu kéo đang lao nhanh không?",
     "Cevin đứng hẳn qua cửa sổ trời giữa gió lốc 130 km/h nâng bộ phóng cáp.",
     "Mũi cáp thép găm chặt vào khung cabin, căng sợi dây cáp nối hai xe.",
     "Gieo kỹ năng liều mạng của Cevin và phương thức đánh cướp đặc trưng."),
    (3, "Đột Nhập Khoang Lái", "N1 night", "RIG_CABIN", ["CEVIN_H", "VERNI"], ["RIG_18", "HARPOON_CABLE"], 5,
     "Cevin đu dây cáp qua khoảng không lao vào khoang lái, khống chế Verni trước khi ông kịp phản kháng và đạp phanh.",
     "Verni có kịp chống trả trước khi Cevin chiếm được tay lái không?",
     "Cevin đu người qua khoảng không giữa hai xe và lao qua cửa phụ cabin.",
     "Cevin gạt tay Verni khỏi thiết bị tự vệ dưới ghế và chiếm quyền kiểm soát vô lăng.",
     "Tạo mối thù sâu sắc của Verni với băng cướp xe tải đêm."),
    (4, "Phá Chốt Thùng Container", "N1 night", "HIGHWAY_NIGHT", ["CINA_H", "CEVIN_H"], ["CIVIC_TRIO", "RIG_18", "BREACH_CHARGE"], 4,
     "Cina Tion điều khiển chiếc Civic thứ hai áp sát đuôi xe tải và kích hoạt thiết bị mở bung chốt cửa thùng hàng.",
     "Cina có mở được khóa thùng container khi xe đang lắc mạnh trên xa lộ không?",
     "Cina nhoài người từ cửa xe gắn thiết bị mở khóa từ tính vào chốt thùng.",
     "Cửa sau container bật mở toang, để lộ hàng trăm kiện điện tử đắt tiền.",
     "Giới thiệu Cina Tion và sự phối hợp ăn ý của đội xe đen."),
    (5, "Chuyển Hàng Trên Nắp Capô", "N1 night", "HIGHWAY_NIGHT", ["ONLE_H", "CINA_H", "CEVIN_H"], ["CIVIC_TRIO", "RIG_18"], 4,
     "Onle lái chiếc Civic thứ ba áp sát đuôi container để đồng đội chuyển các kiện hàng điện tử qua nắp capô mở sẵn.",
     "Đội xe có kịp bốc hết kiện hàng trước khi tới trạm kiểm soát xa lộ không?",
     "Onle giữ vững khoảng cách từng gang tấc phía sau đuôi thùng container đang mở.",
     "Các kiện hàng điện tử được chuyển gọn sang khoang xe thứ ba ở tốc độ cao.",
     "Giới thiệu Onle và hoàn tất khâu lấy hàng trên xa lộ."),
    (6, "Rút Lui Vào Bóng Đêm", "N1 night", "HIGHWAY_NIGHT", ["CEVIN_H", "CINA_H", "ONLE_H", "VERNI"], ["CIVIC_TRIO", "RIG_18"], 4,
     "Băng xe đen thu cáp, tắt đèn gầm xanh lá và rút lui sạch sẽ vào đường nhánh, bỏ lại chiếc container của Verni.",
     "Verni có kịp ghi lại dấu vết nào của ba chiếc xe độ trước khi chúng biến mất không?",
     "Cevin nhảy trở lại chiếc Civic dẫn đầu ngay trước khúc cua rẽ nhánh.",
     "Ba chiếc xe tắt toàn bộ đèn gầm neon, hòa vào màn đêm xa lộ.",
     "Khép lại vụ cướp mở màn và gieo manh mối đèn gầm xanh lá cho cuộc điều tra."),
    (7, "Sáng Sớm Ở Tiệm Ver's Geh", "D1 morning", "VERS_GARAGE", ["TOM"], ["ECLIPSE", "WRENCH_KIT", "F150_TRUCK"], 3,
     "Tại tiệm phụ tùng Ver's Geh của Ryh, Tom hoàn thiện chiếc Eclipse xanh neon và nghe tin giới tài xế xôn xao về vụ cướp đêm qua.",
     "Tom đang làm gì dưới vỏ bọc thợ máy tại tiệm phụ tùng của Ryh?",
     "Tom siết ốc cụm tăng áp cho chiếc Eclipse xanh neon dưới ánh nắng sớm.",
     "Ông chủ Ryh nhắc tới vụ cướp container đêm qua khiến Tom lập tức chú ý.",
     "Giới thiệu Tom và chuẩn bị cho chuyến ghé quán tạp hóa Toto mỗi trưa."),

    # ACT 2 (Scenes 08–14): PHÂN CẢNH 2 — CUỘC ĐỤNG ĐỘ TẠI QUÁN TẠP HÓA TOTO
    (8, "Bánh Mì Cá Ngừ Không Vỏ", "D1 midday", "TOTO_DINER", ["TOM", "AMI"], ["F150_TRUCK", "TUNA_SANDWICH"], 2,
     "Tom lái chiếc bán tải đỏ đến quán tạp hóa Toto, ngồi ở quầy bar gọi món bánh mì cá ngừ quen thuộc và trò chuyện với Ami.",
     "Vì sao ngày nào Tom cũng đến quán Toto gọi đúng một món bánh mì cá ngừ dở tệ?",
     "Tom đỗ chiếc bán tải đỏ ngoài hiên và ngồi vào chiếc ghế quen thuộc đối diện Ami.",
     "Ami vừa làm bánh vừa mỉm cười lắc đầu chê món cá ngừ của chính quán mình.",
     "Giới thiệu Ami Toto và sự gắn kết tự nhiên giữa cô với Tom."),
    (9, "Lời Thú Nhận Ở Quầy Bar", "D1 midday", "TOTO_DINER", ["TOM", "AMI"], ["TUNA_SANDWICH"], 2,
     "Ami đẩy đĩa bánh về phía Tom và hỏi thẳng lý do anh ghé quán; Tom nhìn sâu vào mắt cô thừa nhận anh đến vì cô.",
     "Ami sẽ phản ứng thế nào khi Tom thẳng thắn bày tỏ tình cảm ngay tại quầy?",
     "Ami đặt đĩa bánh mì cắt vỏ trước mặt Tom và chống tay nhìn anh dò hỏi.",
     "Tom nhìn thẳng vào mắt Ami nói anh đến đây mỗi ngày là vì cô.",
     "Bầu không khí lãng mạn vừa chớm nở thì tiếng pô xe của nhóm Cevin cắt ngang."),
    (10, "Bốn Chiếc Xe Độ Cập Bến", "D1 midday", "TOTO_PATIO", ["CEVIN", "CINA", "SEJA", "ONLE", "TOM"], ["F150_TRUCK"], 3,
     "Tiếng nẹt pô chói tai vang lên khi bốn chiếc xe độ của nhóm Micdo đỗ trước quán; Cevin hầm hầm nhìn chiếc bán tải của Tom.",
     "Nhóm của Cevin sẽ phản ứng ra sao khi thấy Tom vẫn tiếp tục xuất hiện ở quán Toto?",
     "Bốn chiếc xe độ hạ gầm phanh gấp ngay cạnh chiếc Ford F-150 của Tom.",
     "Cevin bước xuống đầu tiên với ánh mắt sát khí còn Seja và Onle đi theo sau.",
     "Giới thiệu Seja trong đội hình đời thường của băng đua xe."),
    (11, "Cơn Ghen Của Cevin", "D1 midday", "TOTO_DINER", ["CEVIN", "TOM", "CINA", "AMI"], ["TUNA_SANDWICH"], 4,
     "Cevin đập mạnh xuống bàn bar đuổi Tom cút khỏi quán; Cina Tion khuyên can nhưng Cevin gạt tay cô ra và thách thức Tom.",
     "Tom sẽ giữ vỏ bọc nhẫn nhịn hay đứng lên đáp trả sự khiêu khích của Cevin?",
     "Cevin đập tay xuống mặt quầy làm rung đĩa bánh mì của Tom.",
     "Cevin gạt tay Cina ra và chỉ thẳng vào mặt Tom thách thức, buộc Tom đứng dậy.",
     "Đẩy mâu thuẫn cá nhân giữa Tom và Cevin lên đỉnh điểm."),
    (12, "Cuộc Âu Đả Ngoài Hiên Quán", "D1 midday", "TOTO_PATIO", ["TOM", "CEVIN", "ONLE", "SEJA", "AMI"], ["F150_TRUCK"], 4,
     "Cevin tung cú đấm trước nhưng Tom né được và phản đòn; cả hai vật lộn làm gãy bàn gỗ ngoài hiên giữa tiếng la hét của Ami.",
     "Ai sẽ thắng trong màn ẩu đả tay đôi quyết liệt giữa Tom và Cevin?",
     "Cevin lao vào vung tay đấm thẳng nhưng Tom lách người phản đòn vào hông hắn.",
     "Hai người xô ngã chiếc bàn gỗ ngoài hiên trong khi Ami hét lớn yêu cầu dừng lại.",
     "Bộc lộ kỹ năng cận chiến bản năng của Tom trước khi Micdo xuất hiện."),
    (13, "Tiếng Gầm Động Cơ Quay RX-7", "D1 midday", "TOTO_PATIO", ["MICDO", "TOM_B", "CEVIN", "AMI"], ["RX7", "F150_TRUCK"], 5,
     "Chiếc Mazda RX-7 đỏ rực của Micdo Toto phanh cháy đường trước quán; Micdo bước ra quát lớn khiến cả đám lập tức im bặt.",
     "Thủ lĩnh Micdo Toto sẽ xử lý kẻ lạ mặt dám đánh nhau ngay tại quán gia đình mình thế nào?",
     "Tiếng động cơ quay Rotary gầm vang khi chiếc RX-7 đỏ phanh dừng trước hiên quán.",
     "Micdo tháo kính râm, quát một tiếng đầy uy quyền buộc Cevin phải lùi lại ngay.",
     "Giới thiệu Micdo Toto với thần thái thủ lĩnh tuyệt đối."),
    (14, "Tối Hậu Thư Của Micdo", "D1 midday", "TOTO_PATIO", ["MICDO", "TOM_B", "CEVIN", "AMI"], ["RX7", "F150_TRUCK"], 4,
     "Micdo hỏi lai lịch Tom ở tiệm Ryh rồi lạnh lùng đuổi Tom rời khỏi địa bàn gia đình Toto, cảnh báo không có khái niệm lần sau.",
     "Bị Micdo trục xuất khỏi quán Toto, Tom làm sao tiếp cận lại mục tiêu điều tra?",
     "Micdo bước sát đến trước mặt Tom, nhìn từ đầu đến chân đầy dò xét.",
     "Micdo ra tối hậu thư cấm Tom bén mảng tới quán, còn Tom lặng lẽ nhìn Ami rồi rời đi.",
     "Đóng cánh cửa tiếp cận qua quán ăn, buộc Tom phải tìm đường vào qua đường đua đêm."),

    # ACT 3 (Scenes 15–21): PHÂN CẢNH 3 — CUỘC HỌP BÍ MẬT CỦA LỰC LƯỢNG ĐẶC NHIỆM
    (15, "Biệt Thự Tác Chiến Chìm", "D1 afternoon", "TASKFORCE_HQ", ["NESE", "KINAN", "TOM_B"], ["CASE_FILES"], 3,
     "Tom mang vết bầm trên mặt trở về căn biệt thự chỉ huy bí mật của LAPD và FBI, nơi Trung sĩ Nese và Đặc vụ Kinan đang chờ.",
     "Thân phận thật sự của Tom và mục đích anh tiếp cận gia đình Toto là gì?",
     "Tom bước vào phòng tác chiến đầy bản đồ xa lộ với vết bầm trên gò má.",
     "Nese nhìn vết thương của Sĩ quan Tom và hỏi xoáy về cuộc đụng độ vừa xảy ra.",
     "Lật mở thân phận cảnh sát chìm LAPD của Tom và giới thiệu Nese cùng Kinan."),
    (16, "Báo Cáo Về Cánh Tay Phải Của Micdo", "D1 afternoon", "TASKFORCE_HQ", ["TOM_B", "NESE", "KINAN"], ["CASE_FILES"], 3,
     "Tom báo cáo về tính khí hung hãn của Cevin và việc anh đã bước đầu tạo được cầu nối với Ami tại quán Toto.",
     "Ban chỉ huy có chấp nhận cách tiếp cận chậm rãi qua gia đình Toto của Tom không?",
     "Tom chỉ vào ảnh chụp Cevin và quán Toto trên bảng hồ sơ điều tra.",
     "Kinan cắt ngang báo cáo của Tom vì cho rằng anh đang sa đà vào chuyện tình cảm.",
     "Làm rõ sự khác biệt quan điểm giữa Tom và đặc vụ liên bang Kinan."),
    (17, "Sức Ép Từ Giới Tài Xế Xe Tải", "D1 afternoon", "TASKFORCE_HQ", ["KINAN", "NESE", "TOM_B"], ["CASE_FILES"], 4,
     "Kinan đập hồ sơ vụ cướp của Verni xuống bàn, cảnh báo các tài xế container sắp tự trang bị vũ khí khiến xa lộ thành bãi chiến trường.",
     "Thời gian còn lại cho chiến dịch nằm vùng của Tom gấp rút đến mức nào?",
     "Kinan ném sấp ảnh hiện trường vụ cướp xe tải đêm qua lên bàn chiến thuật.",
     "Kinan cảnh báo Verni và hội tài xế đã dọa tự vũ trang nếu cảnh sát không bắt được thủ phạm.",
     "Đặt đồng hồ đếm ngược sinh tử lên nhiệm vụ của Tom."),
    (18, "Nghi Án Băng Light Saigon", "D1 afternoon", "TASKFORCE_HQ", ["NESE", "KINAN", "TOM_B"], ["CASE_FILES"], 3,
     "Nese chỉ vào hồ sơ băng đảng Light Saigon của Ny Tran, lưu ý FBI vẫn nghi ngờ nhóm này đứng sau đường dây tiêu thụ hàng lậu.",
     "Thủ phạm thực sự là đội đua của Micdo hay băng mô tô của Ny Tran?",
     "Nese lật hồ sơ giám sát khu Little Saigon và các kho hàng bến cảng của Ny Tran.",
     "Nese nhắc Tom phải giữ cái đầu lạnh và theo dõi cả hai đầu mối cùng lúc.",
     "Gieo nhánh điều tra dẫn tới vụ đột kích nhầm nhà Ny Tran ở hồi sau."),
    (19, "Kế Hoạch Đấu Xe Đêm Nay", "D1 afternoon", "TASKFORCE_HQ", ["TOM_B", "NESE", "KINAN"], ["CASE_FILES", "PINK_SLIP"], 4,
     "Tom đề xuất dùng chiếc Mitsubishi Eclipse xanh neon do đơn vị cấp để đấu trực tiếp với Micdo tại giải đua đêm nay do Tohe tổ chức.",
     "Làm thế nào Tom có thể buộc một tay đua kiêu ngạo như Micdo chấp nhận lời thách đấu?",
     "Tom đặt tờ giấy đăng ký chiếc Eclipse lên bản đồ khu công nghiệp Nam L.A.",
     "Tom khẳng định đường đua 1/4 dặm đêm nay là cánh cửa duy nhất để bước vào thế giới của Micdo.",
     "Chuyển hướng chiến thuật sang trận đua đêm mở màn."),
    (20, "Cược Chiếc Phao Cứu Sinh", "D1 late afternoon", "TASKFORCE_HQ", ["NESE", "TOM_B", "KINAN"], ["PINK_SLIP", "CASE_FILES"], 4,
     "Nese trao giấy tờ sở hữu chiếc Eclipse cho Tom nhưng cảnh báo nếu thua mất xe, anh sẽ mất luôn chiếc phao cứu sinh duy nhất.",
     "Tom sẽ đánh cược toàn bộ cơ hội nằm vùng của mình vào một cuộc đua 10 giây sao?",
     "Nese cầm tờ giấy tờ xe nhìn thẳng vào mắt Tom trước khi trao tận tay.",
     "Tom nhận lấy giấy tờ xe, cam kết sẽ giành được sự tôn trọng của Micdo ngay trong đêm nay.",
     "Khóa đạo cụ giấy tờ xe (Pink Slip) cho màn đặt cược ở Cảnh 24."),
    (21, "Cân Chỉnh Hai Bình NOS", "D1 dusk", "VERS_GARAGE", ["TOM_R"], ["ECLIPSE", "NOS_BOTTLES", "DIAG_LAPTOP"], 3,
     "Trước giờ xuất phát tại tiệm Ver's Geh, Tom kiểm tra hai bình khí NOS và bản đồ nhiên liệu trên laptop cho chiếc Eclipse xanh neon.",
     "Hệ thống động cơ chiếc Eclipse có chịu nổi áp lực nếu kích hoạt cả hai bình NOS không?",
     "Tom mở cốp sau kiểm tra van áp suất của hai bình khí Nitrous màu xanh.",
     "Ông chủ Ryh nhắc Tom trên màn hình laptop rằng bộ cổ góp sẽ quá tải nếu bấm NOS quá sớm.",
     "Gieo cảnh báo kỹ thuật dẫn tới sự cố bung sàn xe ở Cảnh 26."),

    # ACT 4 (Scenes 22–28): PHÂN CẢNH 4 — TRẬN ĐUA ĐÊM MỞ MÀN (THE FIRST RACE)
    (22, "Chảo Lửa Đua Đêm Nam L.A.", "N2 night", "RACE_MEET", ["TOM_R", "CINA"], ["ECLIPSE", "PINK_SLIP"], 4,
     "Hàng trăm xe độ tụ tập tại khu công nghiệp Nam L.A.; Tohe cầm loa hô luật cược 2.000 đô ăn tất trên đoạn đường 1/4 dặm.",
     "Ai sẽ dám bước vào vạch xuất phát đối đầu với những tay đua sừng sỏ nhất thành phố?",
     "Tohe đứng trên nắp capô giữa khói lốp và ánh đèn pha, hô vang luật chơi 2.000 đô.",
     "Inwe và Danny Yamato lần lượt đập sấp tiền mặt xuống nắp xe đăng ký tranh tài.",
     "Thiết lập quy mô và luật chơi khắc nghiệt của giải đua đường phố."),
    (23, "Vua Đường Phố Tiến Vào Vạch Đua", "N2 night", "RACE_MEET", ["MICDO", "TOM_R", "CEVIN", "CINA"], ["RX7", "ECLIPSE"], 4,
     "Chiếc Mazda RX-7 đỏ của Micdo tiến vào vạch xuất phát giữa tiếng reo hò; Tom lái chiếc Eclipse xanh neon tới xin tham gia.",
     "Micdo và Cevin sẽ phản ứng thế nào khi thấy gã khách quán bánh mì dám đem xe ra thách đua?",
     "Đám đông dạt ra hai bên khi chiếc RX-7 đỏ của Micdo lăn bánh vào làn đua chính.",
     "Tom cho chiếc Eclipse đỗ sát làn bên cạnh trong tiếng cười nhạo của Cevin.",
     "Đưa Tom và Micdo vào thế đối đầu trực diện trên vạch xuất phát."),
    (24, "Đặt Cược Giấy Tờ Xe 10.000 Đô", "N2 night", "RACE_MEET", ["TOM_R", "MICDO", "CINA", "CEVIN"], ["ECLIPSE", "RX7", "PINK_SLIP"], 5,
     "Không có 2.000 đô tiền mặt, Tom rút giấy tờ sở hữu chiếc Eclipse trị giá 10.000 đô ra cược; Micdo mỉm cười chấp nhận và Cina phất tay xuất phát.",
     "Micdo có chấp nhận lời thách cược bằng cả chiếc xe của một tay mơ không?",
     "Tom giơ tờ giấy tờ sở hữu hợp pháp của chiếc Eclipse ra trước mặt Tohe và Micdo.",
     "Micdo gật đầu nhận kèo, còn Cina bước ra giữa hai làn xe giơ cao hai tay hô chạy.",
     "Khởi động cuộc đua 1/4 dặm đầu tiên giữa Tom và Micdo."),
    (25, "Kích Hoạt Bình NOS Đầu Tiên", "N2 night", "RACE_COCKPIT", ["TOM_R", "MICDO"], ["ECLIPSE", "RX7", "NOS_BOTTLES", "DIAG_LAPTOP"], 5,
     "Bốn chiếc xe lao vút đi; bị chiếc RX-7 của Micdo bỏ lại nửa thân xe, Tom quyết định nhấn nút kích hoạt bình NOS đầu tiên.",
     "Cú bơm khí NOS có giúp Tom san bằng khoảng cách với chiếc RX-7 của Micdo không?",
     "Kim đồng hồ tua máy của Tom vọt lên vùng đỏ khi chiếc RX-7 dẫn đầu làn bên cạnh.",
     "Tom nhấn nút đỏ trên vô lăng, chiếc Eclipse lao vọt lên ngang hàng với Micdo.",
     "Đẩy tốc độ lên cực hạn và kích hoạt cảnh báo quá tải trên laptop."),
    (26, "Bung Sàn Phụ & Thua Một Thân Xe", "N2 night", "RACE_MEET", ["TOM_R", "MICDO", "CEVIN"], ["ECLIPSE", "RX7", "DIAG_LAPTOP"], 5,
     "Tom bấm tiếp bình NOS thứ hai khiến tấm sàn phụ bung ra tóe tia lửa; Micdo bình thản sang số vượt qua vạch đích trước Tom một thân xe và đòi chìa khóa.",
     "Chuyện gì xảy ra khi Tom cố ép động cơ vượt quá giới hạn để thắng Micdo?",
     "Màn hình laptop nhấp nháy báo động cơ quá tải nhưng Tom vẫn nhấn bình NOS thứ hai.",
     "Tấm sàn bên phụ bung chốt tóe tia lửa dưới gầm, chiếc RX-7 của Micdo cán đích trước và Micdo bước tới đòi xe.",
     "Bài học đầu tiên của Micdo dành cho Tom về bản lĩnh làm chủ con xe."),
    (27, "Còi Cảnh Sát Vây Ráp Bốn Phía", "N2 night", "RACE_ALLEY", ["MICDO", "TOM_R", "CEVIN"], ["ECLIPSE", "RX7"], 5,
     "Đèn xanh đỏ và còi cảnh sát LAPD ập tới từ bốn phía; đám đông tán loạn, Micdo bỏ chạy bộ vào hẻm tối và bị xe tuần tra chặn đầu khóa đuôi.",
     "Tom sẽ mặc kệ để cảnh sát bắt Micdo hay liều mình cứu mục tiêu điều tra?",
     "Ánh đèn tuần tra xanh đỏ quét rực khu phố khi Tohe hét lớn báo động có cảnh sát.",
     "Micdo chạy bộ vào con hẻm hẹp nhưng hai đầu hẻm đều xuất hiện đèn xe tuần tra khóa chặt.",
     "Đặt Micdo vào tình thế tuyệt vọng để tạo bước ngoặt cứu người của Tom."),
    (28, "Cú Drift 180 Độ Cứu Mạng", "N2 night", "RACE_ALLEY", ["TOM_R", "MICDO"], ["ECLIPSE"], 5,
     "Chiếc Eclipse bốc khói của Tom lao vào hẻm, drift xoay 180 độ mở toang cửa phụ đón Micdo lên xe rồi phóng vượt qua vòng vây cảnh sát.",
     "Tom và Micdo có thoát khỏi vòng vây xe tuần tra LAPD trên chiếc Eclipse đang bốc khói không?",
     "Chiếc Eclipse của Tom lao thẳng vào hẻm, kéo phanh tay xoay tròn 180 độ ngay cạnh Micdo.",
     "Micdo nhảy lên ghế phụ, Tom đạp lút ga vượt qua khe hẹp thoát khỏi đoàn xe tuần tra.",
     "Hành động cứu mạng giúp Tom xóa bỏ ranh giới người ngoài trong mắt Micdo."),

    # ACT 5 (Scenes 29–35): PHÂN CẢNH 5 — CUỘC CHẠM TRÁN TỬ THẦN VỚI BĂNG LIGHT SAIGON
    (29, "Mười Chiếc Mô Tô Đen Vây Kín", "N2 night", "SAIGON_LOT", ["TOM_R", "MICDO", "NYTRAN", "CELA"], ["ECLIPSE", "MOTO_PACK"], 4,
     "Vừa thoát cảnh sát, chiếc Eclipse của Tom và Micdo bất ngờ bị mười chiếc mô tô phân khối lớn của Ny Tran và Cela Nguyen ép vào bãi đất trống Little Saigon.",
     "Đội mô tô đen xuất hiện giữa đêm thuộc thế lực nào và muốn gì ở Micdo?",
     "Mười chiếc mô tô thể thao màu đen gầm rú vây quanh chiếc Eclipse từ mọi hướng.",
     "Ny Tran và Cela Nguyen dừng xe chặn đầu, buộc Tom phải tấp vào bãi đất trống.",
     "Giới thiệu hai phản diện chính Ny Tran và Cela Nguyen của băng Light Saigon."),
    (30, "Chạm Mặt Thủ Lĩnh Light Saigon", "N2 night", "SAIGON_LOT", ["NYTRAN", "MICDO", "TOM_R", "CELA"], ["ECLIPSE", "MOTO_PACK"], 4,
     "Ny Tran gõ mạnh vào kính xe buộc cả hai bước xuống; Micdo giơ hai tay bước ra nói chỉ đi ngang qua và nhận Tom là lính mới của mình.",
     "Micdo sẽ ứng phó thế nào khi rơi vào địa bàn của kẻ thù giữa lúc không có đồng đội?",
     "Ny Tran bước xuống mô tô, gõ mạnh vào kính cửa sổ bên lái của Tom.",
     "Micdo giơ hai tay bước ra che cho Tom, nói Tom chỉ là lính mới chưa biết luật.",
     "Khắc họa sự điềm tĩnh bảo vệ đàn em của Micdo trước mũi đe dọa."),
    (31, "Đường Dao Trên Nắp Capô", "N2 night", "SAIGON_LOT", ["CELA", "NYTRAN", "TOM_R", "MICDO"], ["ECLIPSE", "MOTO_PACK"], 4,
     "Cela Nguyen đi vòng quanh chiếc Eclipse xanh neon, dùng mũi dao cào một vệt dài trên lớp sơn xe và buông lời miệt thị Tom.",
     "Tom có kìm nén được cơn giận khi chiếc xe của mình bị Cela cố tình hủy hoại không?",
     "Cela Nguyen lượn quanh chiếc Eclipse, miết mũi dao tạo tiếng rít chói tai trên sơn xe.",
     "Cela cười khẩy chê Tom không biết xài đồ hiệu trong khi Tom siết chặt hai nắm tay.",
     "Khắc họa sự ngạo mạn tàn nhẫn của Cela Nguyen và băng Light Saigon."),
    (32, "Tranh Chấp Kho Hàng Bến Cảng", "N2 night", "SAIGON_LOT", ["NYTRAN", "MICDO", "TOM_R", "CELA"], ["ECLIPSE", "MOTO_PACK"], 5,
     "Ny Tran áp sát Tom và chất vấn Micdo chuyện người của Micdo lảng vảng quanh các kho hàng của hắn ở bến cảng, phá vỡ thỏa thuận giữa hai bên.",
     "Vì sao Ny Tran lại nghi ngờ nhóm của Micdo đang nhòm ngó kho hàng bến cảng của hắn?",
     "Ny Tran bước tới đối diện Tom và Micdo với ánh mắt sắc lạnh.",
     "Ny Tran nhắc lại ranh giới lãnh địa và buộc tội người của Micdo rình mò kho hàng cảng.",
     "Gieo mâu thuẫn lợi ích trực tiếp giữa băng Micdo và băng Light Saigon."),
    (33, "Bài Học Về Việc Chọn Phe", "N2 night", "SAIGON_LOT", ["NYTRAN", "MICDO", "TOM_R", "CELA"], ["ECLIPSE", "MOTO_PACK"], 5,
     "Micdo khẳng định không liên quan đến kho cảng, nhưng Ny Tran lùi lại chỉ vào chiếc Eclipse và tuyên bố dạy cho lính mới của Micdo một bài học.",
     "Ny Tran định làm gì để dằn mặt Micdo và gã lính mới ngay tại bãi đất trống?",
     "Micdo giữ giọng trầm tĩnh phủ nhận chuyện xâm phạm kho hàng của Ny Tran.",
     "Ny Tran lùi lại hai bước, ra hiệu cho đàn em nhắm thẳng vào chiếc Eclipse xanh neon.",
     "Đẩy căng thẳng lên đỉnh điểm trước khi chiếc xe bị phá hủy."),
    (34, "Chiếc Eclipse Chìm Trong Biển Lửa", "N2 night", "SAIGON_LOT", ["TOM_R", "MICDO", "NYTRAN", "CELA"], ["ECLIPSE", "MOTO_PACK"], 5,
     "Ny Tran và đàn em phá thủng bình nhiên liệu khiến chiếc Eclipse bốc cháy dữ dội giữa tiếng hét bất lực của Tom, rồi cả bọn phóng mô tô bỏ đi.",
     "Mất trắng chiếc xe đặc nhiệm trị giá hàng chục ngàn đô, Tom sẽ ăn nói sao với LAPD và Micdo?",
     "Đàn em của Ny Tran phá toạc phần đuôi xe nơi đặt hai bình khí NOS còn rò rỉ.",
     "Chiếc Eclipse bùng cháy dữ dội trong đêm khi Ny Tran cười lớn phóng mô tô rời đi.",
     "Chiếc Eclipse bị hủy hoàn toàn, tạo ra món nợ 'con xe 10 giây' giữa Tom và Micdo."),
    (35, "Cuốc Bộ Về Nhà Đầy Muội Than", "N2 night", "TOTO_BACKYARD", ["MICDO", "TOM_B"], ["RX7"], 3,
     "Từ bãi đất trống rực lửa, Micdo và Tom lặng lẽ đi bộ suốt quãng đường dài trở về khu nhà Toto với gương mặt và áo quần bám đầy muội than.",
     "Sau biến cố sinh tử vừa rồi, thái độ của Micdo đối với Tom đã thay đổi ra sao?",
     "Micdo và Tom bước đi song song dưới ánh đèn đường khuya với gương mặt lấm lem khói đen.",
     "Micdo vỗ nhẹ lên vai Tom trước khi mở cổng bước vào sân sau nhà mình.",
     "Chuyển nhịp từ hiểm nguy sang tình anh em gắn kết tại gia đình Toto."),

    # ACT 6 (Scenes 36–42): PHÂN CẢNH 6 — TIỆC BBQ VÀ SỰ THỪA NHẬN
    (36, "Bữa Tiệc BBQ Sân Sau", "N2 late night", "TOTO_BACKYARD", ["CEVIN", "AMI_N", "CINA", "MICDO", "TOM_B"], ["WRENCH_KIT"], 2,
     "Tại sân sau nhà Toto thơm mùi thịt nướng, cả nhóm sững sờ đứng bật dậy khi thấy Micdo và Tom đi bộ về trong bộ dạng ám đầy muội than.",
     "Cả nhóm sẽ phản ứng thế nào khi thấy thủ lĩnh của mình đi cùng gã khách hồi trưa?",
     "Cevin, Ami, Cina, Onle và Seja đang quây quần bên bếp nướng thì thấy cổng mở.",
     "Cevin đứng bật dậy hỏi dồn khi thấy áo quần Micdo và Tom bám đầy khói đen.",
     "Mở màn cảnh gia đình ấm áp đối lập với thế giới tội phạm bên ngoài."),
    (37, "Tuyên Bố Kết Nạp Của Micdo", "N2 late night", "TOTO_BACKYARD", ["MICDO", "TOM_B", "CEVIN", "CINA"], ["WRENCH_KIT"], 3,
     "Micdo nâng chai nước trước cả nhóm, tuyên bố Tom đã cứu anh khỏi nhà giam LAPD và từ đêm nay Tom chính thức là người của gia đình Toto.",
     "Các thành viên trong băng, đặc biệt là Cevin, có chấp nhận quyết định của Micdo không?",
     "Micdo cầm chai nước bước ra giữa sân, nhìn khắp lượt từng người anh em.",
     "Micdo tuyên bố ai đụng đến Tom là đụng đến mình, trong khi Cevin vẫn lườm Tom đầy cảnh giác.",
     "Tom chính thức thâm nhập vào lõi băng đảng của Micdo Toto."),
    (38, "Khăn Ẩm Của Ami", "N2 late night", "TOTO_BACKYARD", ["AMI_N", "TOM_B", "MICDO"], ["WRENCH_KIT"], 2,
     "Ami bước đến bên Tom, nhẹ nhàng dùng khăn ẩm lau vết muội than trên gò má anh và cảm ơn anh đã đưa anh trai cô trở về an toàn.",
     "Sự quan tâm chân thành của Ami tác động thế nào đến tâm lý cảnh sát chìm của Tom?",
     "Ami cầm chiếc khăn bông trắng bước lại gần Tom dưới ánh đèn dây vàng ấm.",
     "Ami chấm nhẹ vết khói trên má Tom, ánh mắt hai người chạm nhau đầy lưu luyến.",
     "Thắt chặt sợi dây tình cảm khiến Tom ngày càng khó xuống tay bắt giữ gia đình cô."),
    (39, "Bài Toán Xe 10 Giây Của Seja", "N2 late night", "TOTO_BACKYARD", ["SEJA", "TOM_B", "ONLE", "MICDO"], ["DIAG_LAPTOP"], 3,
     "Seja vừa nhai khoai tây chiên vừa tính toán: chiếc Eclipse đã nổ tung nghĩa là Tom nợ Micdo một 'con xe 10 giây', và hứa sẽ cùng Onle độ lại nếu Tom mang xác xe về.",
     "Làm thế nào Tom kiếm được một chiếc xe đủ sức chạy 1/4 dặm dưới 10 giây để trả nợ Micdo?",
     "Seja tiến lại gần Tom với ánh mắt lanh lợi, tay khua khoắng giải thích công thức tốc độ.",
     "Tom nhìn thẳng vào Micdo và hứa sẽ mang về cho cả đội một con xe 10 giây thực thụ.",
     "Đặt nền móng cho sự ra đời của chiếc Toyota Supra cam huyền thoại."),
    (40, "Xác Chiếc Toyota Supra Trên Xe Cứu Hộ", "D2 morning", "TOTO_GARAGE", ["TOM", "SEJA", "ONLE", "CEVIN"], ["SUPRA_SHELL", "WRENCH_KIT"], 3,
     "Sáng hôm sau, Tom chở một khung xe Toyota Supra rỉ sét về gara nhà Micdo; Cevin chê là đống sắt vụn nhưng Seja phát hiện khối động cơ 2JZ nguyên bản.",
     "Đống sắt vụn rỉ sét mà Tom mang về có thực sự trở thành một cỗ máy 10 giây được không?",
     "Chiếc xe cứu hộ hạ khung chiếc Supra cam bạc màu xuống trước cửa gara nhà Toto.",
     "Seja mở nắp capô và reo lên phấn khích khi thấy khối động cơ 2JZ-GTE bên trong.",
     "Khởi động quá trình lột xác của chiếc Toyota Supra cam."),
    (41, "Đêm Độ Xe & Tình Anh Em", "N3 night", "TOTO_GARAGE", ["TOM", "SEJA", "ONLE", "AMI_N"], ["SUPRA", "WRENCH_KIT", "DIAG_LAPTOP"], 2,
     "Suốt nhiều đêm liền, Tom cùng Seja và Onle đại tu động cơ và sơn lại lớp vỏ cam rực rỡ cho chiếc Supra, trong khi Ami luôn mang bữa khuya xuống tiếp sức.",
     "Quá trình cùng ăn cùng làm trong gara đã biến đổi nhận thức của Tom về nhóm Micdo ra sao?",
     "Tom, Seja và Onle phối hợp hạ khối động cơ tăng áp kép sáng bóng vào khoang máy chiếc Supra cam.",
     "Ami mang khay đồ ăn đêm vào gara, mỉm cười nhìn Tom lau mồ hôi bên thành xe mới sơn.",
     "Hoàn thiện chiếc Toyota Supra cam — phương tiện cứu mạng ở hồi cuối."),
    (42, "Quái Thú Dodge Charger 1970 Trong Gara", "N3 late night", "TOTO_GARAGE", ["MICDO", "TOM"], ["CHARGER", "WRENCH_KIT"], 3,
     "Sau khi mọi người về nghỉ, Micdo dẫn Tom vào góc sâu gara, kéo tấm bạt phủ chiếc Dodge Charger 1970 công suất 900 mã lực của cha mình và tâm sự về 10 giây tự do.",
     "Vì sao Micdo lại vừa tự hào vừa sợ hãi chưa từng dám lái chiếc Charger 900 mã lực của cha?",
     "Micdo kéo tấm bạt vải xám để lộ chiếc Dodge Charger 1970 đen bóng với bộ siêu nạp khổng lồ.",
     "Micdo kể về người cha quá cố và triết lý sống trọn vẹn trong 10 giây trên đường 1/4 dặm.",
     "Gieo chiếc Dodge Charger 1970 và câu thoại chủ đề cho màn đua cắt đầu tàu hỏa ở Cảnh 68–69."),

    # ACT 7 (Scenes 43–49): PHÂN CẢNH 7 — VỤ BẮT GIỮ SAI LẦM TẠI NHÀ NY TRAN
    (43, "Cuộc Gọi Thúc Ép Của Kinan", "D3 night", "TASKFORCE_HQ", ["TOM", "NESE", "KINAN"], ["CASE_FILES", "POLICE_RADIO"], 4,
     "Bị Kinan ép phải giao thủ phạm ngay lập tức để ngăn giới tài xế nổi loạn, Tom báo cáo mối nghi vấn về kho hàng điện tử của Ny Tran ở Little Saigon.",
     "Có phải Tom đang cố hướng mũi dùi điều tra sang Ny Tran để bảo vệ Micdo không?",
     "Kinan đập bàn yêu cầu lập tức mở chiến dịch đột kích ngay trong sáng mai.",
     "Tom cung cấp vị trí kho hàng của Ny Tran nơi anh từng bị vây ép đêm trước.",
     "Châm ngòi cho chiến dịch đột kích quy mô lớn vào dinh thự Ny Tran."),
    (44, "Bao Vây Dinh Thự Lúc Rạng Đông", "D4 dawn", "NYTRAN_MANSION", ["NESE_T", "KINAN_T", "TOM"], ["CASE_FILES", "POLICE_RADIO"], 4,
     "Rạng sáng, hàng chục xe đặc nhiệm của Nese và Kinan bao vây khu dinh thự của Ny Tran tại Little Saigon và phá cổng chính đột nhập.",
     "Cuộc đột kích bất ngờ lúc bình minh có tìm thấy tang vật các vụ cướp xe tải không?",
     "Đoàn xe đặc nhiệm phanh gấp trước cổng sắt dinh thự Ny Tran dưới ánh bình minh.",
     "Đội xung kích do Kinan và Nese dẫn đầu mở tung cổng chính tràn vào sân trong.",
     "Mở màn cao trào hành động của Phân cảnh 7."),
    (45, "Khống Chế Tại Phòng Khách", "D4 dawn", "NYTRAN_MANSION", ["KINAN_T", "NESE_T", "NYTRAN", "CELA"], ["CASE_FILES"], 4,
     "Gã bảo vệ vạm vỡ Gusa bị quật ngã xuống sàn; bố của Ny Tran mặc áo lụa bị giữ tại ghế sofa, gào lên phản đối việc khám xét không có căn cứ.",
     "Phản ứng quyết liệt của bố Ny Tran báo hiệu điều bất thường gì về số hàng trong kho?",
     "Đội đặc nhiệm khống chế Gusa và Cela ngay tại sảnh chính dinh thự.",
     "Bố của Ny Tran lớn tiếng khẳng định gia đình ông làm ăn hợp pháp và đóng thuế đầy đủ.",
     "Gieo sự sỉ nhục đối với gia đình Ny Tran — nguyên nhân trực tiếp dẫn tới cuộc báo thù sau đó."),
    (46, "Ánh Mắt Nhận Diện Qua Kính Xe", "D4 dawn", "NYTRAN_MANSION", ["NYTRAN", "TOM", "NESE_T", "CELA"], ["POLICE_RADIO"], 5,
     "Bị khóa tay dẫn ra sân, Ny Tran bất ngờ nhìn xuyên qua cửa kính xe chỉ huy thấy mặt Tom đang đứng phía sau và gào lên thề sẽ trả thù bằng máu.",
     "Chuyện gì sẽ xảy ra khi Ny Tran phát hiện gã lính mới của Micdo lại đi cùng đoàn cảnh sát?",
     "Ny Tran bị dẫn ngang qua chiếc xe chỉ huy có kính màu đang hé mở.",
     "Ny Tran bắt gặp ánh mắt của Tom, gằn giọng gào tên Tom và thề sẽ bắt cả băng phải trả giá.",
     "Lộ diện Tom trước mắt Ny Tran, khiến Ny Tran tin rằng Micdo đã cài cảnh sát hại mình."),
    (47, "Hóa Đơn Hải Quan Chính Ngạch", "D4 morning", "NYTRAN_WAREHOUSE", ["NESE_T", "KINAN_T", "TOM"], ["CUSTOMS_INVOICE", "CASE_FILES"], 4,
     "Trong kho hàng phía sau, Nese kiểm tra toàn bộ kiện hàng điện tử và sững sờ phát hiện mọi lô hàng đều có hóa đơn nhập khẩu hải quan hợp pháp.",
     "Những thùng hàng điện tử trong kho của Ny Tran có phải là tang vật vụ cướp xe tải không?",
     "Nese đối chiếu dãy mã số trên thùng hàng với tập chứng từ hải quan đóng dấu đỏ.",
     "Nese chạy ra thông báo cho Kinan và Tom rằng không có một món đồ nào trùng số seri bị cướp.",
     "Cú lật bất ngờ: băng Light Saigon không phải thủ phạm các vụ cướp container."),
    (48, "Cơn Thịnh Nộ Của Chỉ Huy", "D4 morning", "NYTRAN_MANSION", ["KINAN_T", "NESE_T", "TOM"], ["CASE_FILES", "CUSTOMS_INVOICE"], 4,
     "Kinan đập mạnh tay vào thành xe vì vồ hụt; Nese chỉ thẳng mặt Tom khiển trách anh đã bị Micdo làm mờ mắt và khẳng định thủ phạm chính là nhóm Toto.",
     "Sau sai lầm nghiêm trọng này, Tom còn đường nào để che chở cho Micdo nữa không?",
     "Kinan giận dữ đập tay lên nắp xe chỉ huy khi phải ra lệnh tháo còng trả tự do cho Ny Tran.",
     "Nese cảnh cáo Tom rằng thủ phạm thực sự chỉ có thể là Micdo Toto và buộc anh phải lấy bằng chứng.",
     "Đẩy Tom vào chân tường giữa kỷ luật ngành và tình cảm với gia đình Toto."),
    (49, "Tháo Còng & Lời Thề Báo Thù", "D4 morning", "NYTRAN_MANSION", ["NYTRAN", "CELA", "TOM", "NESE_T"], ["CUSTOMS_INVOICE"], 4,
     "Được tháo còng ngay trước hiên nhà, Ny Tran xoa cổ tay nhìn theo đoàn xe cảnh sát rút lui và ra lệnh cho Cela chuẩn bị thanh toán băng Micdo tại giải Race Wars.",
     "Ny Tran sẽ trả đũa nỗi nhục bị đột kích nhà như thế nào?",
     "Cán bộ hỗ trợ tháo khóa tay cho Ny Tran và Cela Nguyen giữa sân dinh thự.",
     "Ny Tran nhìn theo chiếc xe chở Tom khuất dần, ánh mắt ánh lên sát khí lạnh lẽo.",
     "Dẫn trực tiếp sang đại hội đua xe Race Wars tại sa mạc Mojave."),

    # ACT 8 (Scenes 50–56): PHÂN CẢNH 8 — BI KỊCH TẠI ĐẠI HỘI ĐUA XE RACE WARS
    (50, "Đại Hội Race Wars Sa Mạc Mojave", "D5 midday", "RACE_WARS", ["MICDO", "TOM", "SEJA_R", "AMI"], ["SUPRA", "JETTA"], 3,
     "Giữa cái nắng cháy da của sa mạc Mojave, hàng ngàn chiếc xe quy tụ tại Race Wars; Seja hào hứng chuẩn bị chiếc Volkswagen Jetta trắng bên lán trại của Micdo.",
     "Không khí náo nhiệt tại đại hội Race Wars ẩn chứa hiểm họa gì cho nhóm của Micdo?",
     "Đoàn xe của nhóm Micdo tiến vào đường băng sa mạc Mojave rực nắng.",
     "Seja lau bóng nắp capô chiếc Jetta trắng tâm huyết trong khi Tom và Ami đứng bên cạnh khích lệ.",
     "Thiết lập bối cảnh sa mạc Mojave và niềm tự hào của Seja với chiếc Jetta của cha."),
    (51, "Lời Khiêu Khích Của Ny Tran", "D5 midday", "RACE_WARS", ["NYTRAN_R", "SEJA_R", "CELA"], ["JETTA", "S2000"], 4,
     "Ny Tran lái chiếc Honda S2000 đen trờ tới vạch xuất phát cạnh Seja, dùng lời lẽ mưu mô khích thiên tài toán học cược giấy tờ chiếc Jetta.",
     "Seja có nhận ra cái bẫy mà Ny Tran đang giăng ra để chiếm chiếc xe kỷ vật không?",
     "Ny Tran đỗ chiếc S2000 đen bóng sát bên chiếc Jetta trắng của Seja.",
     "Ny Tran nhìn Seja bằng ánh mắt khiêu khích, thách cược giấy tờ chiếc Jetta đấu với danh dự của hắn.",
     "Ny Tran chọn điểm yếu tâm lý của Seja để mở màn cuộc trả thù."),
    (52, "Tỷ Lệ Thắng 64 Phần Trăm", "D5 midday", "RACE_WARS", ["SEJA_R", "NYTRAN_R", "TOM", "MICDO"], ["JETTA", "S2000", "PINK_SLIP", "DIAG_LAPTOP"], 4,
     "Mồ hôi vã ra như tắm vì áp lực, Seja nhìn màn hình máy tính tự tin tỷ lệ thắng là 64% rồi rút giấy tờ chiếc Jetta ra đặt cược trước khi Tom kịp ngăn.",
     "Con số 64% trên máy tính của Seja đã bỏ sót biến số chết người nào dưới nắp capô của Ny Tran?",
     "Tay Seja run nhẹ khi kiểm tra biểu đồ thông số trên chiếc laptop đặt ở ghế phụ.",
     "Seja nộp tờ giấy tờ sở hữu chiếc Jetta trắng cho trọng tài đúng lúc Tom và Micdo vừa chạy tới.",
     "Khoảnh khắc định mệnh dẫn tới bi kịch của Seja."),
    (53, "Cú Bấm NOS Ở Những Mét Cuối", "D5 midday", "RACE_WARS", ["SEJA_R", "NYTRAN_R"], ["JETTA", "S2000", "NOS_BOTTLES"], 5,
     "Còi xuất phát vang lên; chiếc Jetta của Seja dẫn trước nửa đường nhưng Ny Tran lạnh lùng bấm nút xả hệ thống NOS ẩn dưới ghế, vượt qua Seja ở những mét cuối cùng.",
     "Seja sẽ phản ứng thế nào khi thấy chiếc S2000 của Ny Tran bất ngờ xé gió vượt qua?",
     "Hai chiếc xe lao vút đi trên đường băng sa mạc, chiếc Jetta trắng vươn lên dẫn đầu.",
     "Ny Tran liếc nhìn sang rồi bật công tắc NOS đôi ẩn dưới ghế, đưa chiếc S2000 cán đích trước.",
     "Đánh sập niềm tin toán học của Seja chỉ trong vài giây cuối."),
    (54, "Hoảng Loạn Chạy Trốn Vào Sa Mạc", "D5 midday", "RACE_WARS", ["SEJA_R", "TOM", "MICDO"], ["JETTA"], 4,
     "Hoảng loạn ôm đầu trong xe vì mất chiếc Jetta kỷ vật, Seja không dừng lại ở vạch đích mà đạp ga phóng thẳng qua lối thoát chạy trốn vào sa mạc.",
     "Việc Seja hoảng sợ lái chiếc xe đã thua cược bỏ trốn sẽ gây ra hậu quả gì cho cả nhóm?",
     "Trong khoang lái, Seja ôm đầu tuyệt vọng không tin phép tính của mình có thể sai.",
     "Thay vì quay lại giao xe, Seja đạp lút ga phóng chiếc Jetta trắng thẳng ra đường sa mạc.",
     "Hành động bỏ trốn vì hoảng loạn của Seja trao cho Ny Tran cái cớ truy sát."),
    (55, "Đòi Nợ Tại Lán Trại Toto", "D5 afternoon", "RACE_WARS", ["NYTRAN_R", "MICDO", "CELA", "TOM"], ["S2000", "RX7"], 5,
     "Ny Tran dẫn Cela Nguyen và Gusa kéo tới lán trại của Micdo, đập mạnh lên nắp capô đòi giao ngay chiếc Jetta và thằng nhóc quỵt nợ Seja.",
     "Micdo sẽ bảo vệ người em lỡ dại của mình thế nào trước sự hung hãn của Ny Tran?",
     "Ny Tran bước xuống từ chiếc S2000, đập mạnh bàn tay lên nắp capô xe của Micdo.",
     "Micdo lập tức bước lên một bước, chắn trước toàn bộ các thành viên trong đội.",
     "Cuộc đối đầu trực diện giữa hai thủ lĩnh giữa cái nắng sa mạc."),
    (56, "Tuyên Chiến Giữa Sa Mạc", "D5 afternoon", "RACE_WARS", ["NYTRAN_R", "MICDO", "TOM", "CELA"], ["RX7", "S2000"], 5,
     "Micdo hứa sẽ tìm Seja mang xe trả sau, nhưng Ny Tran tiến sát mặt Micdo, buộc tội Micdo phái cảnh sát làm nhục cha hắn và tuyên bố giải quyết bằng vũ lực.",
     "Lời tuyên chiến của Ny Tran đẩy nhóm của Micdo vào bước đường cùng nào?",
     "Micdo giữ giọng bình tĩnh đề nghị sẽ tự đi tìm Seja và giao xe sau giải đấu.",
     "Ny Tran gằn giọng nhắc lại vụ đột kích sáng qua và tuyên bố mọi chuyện sẽ kết thúc bằng máu.",
     "Khép lại Phân cảnh 8 với hiểm họa sát sườn buộc Micdo phải làm vụ cướp cuối."),

    # ACT 9 (Scenes 57–63): PHÂN CẢNH 9 — VỤ CƯỚP CUỐI CÙNG VÀ BÍ MẬT ĐƯỢC BẬT MÍ (THE LAST HEIST)
    (57, "Đêm Chuẩn Bị Phi Vụ Cuối", "N5 night", "TOTO_GARAGE", ["MICDO_H", "CINA_H", "CEVIN_H", "ONLE_H"], ["CIVIC_TRIO", "HARPOON_CABLE"], 4,
     "Đêm muộn tại gara nhà Toto, Micdo, Cina, Cevin và Onle lặng lẽ chuẩn bị đồ nghề và ba chiếc Civic đen để thực hiện vụ cướp xe tải cuối cùng lấy tiền cứu Seja.",
     "Vì sao Micdo vẫn quyết định thực hiện vụ cướp xe tải dù biết rủi ro đang ở mức cao nhất?",
     "Bốn thành viên kiểm tra lại dây cáp thép và bộ đàm bên cạnh ba chiếc Civic đen trong gara.",
     "Micdo ra lệnh xuất phát nhanh trước khi Ami và Tom kịp phát hiện kế hoạch.",
     "Mở màn phi vụ cướp xe tải cuối cùng đầy định mệnh."),
    (58, "Lời Thú Nhận Với Ami", "N5 night", "TOTO_GARAGE", ["TOM_R", "AMI_N"], ["SUPRA", "POLICE_RADIO"], 5,
     "Tom lao tới chặn Ami lại khi cô định đi theo; bị Ami tra hỏi vì sao biết tài xế Verni đã vũ trang, Tom nghẹn ngào thú nhận mình là cảnh sát chìm LAPD rồi đưa cô lên chiếc Supra đuổi theo.",
     "Ami sẽ phản ứng ra sao khi biết người đàn ông cô yêu lại chính là cảnh sát chìm đang điều tra anh trai mình?",
     "Tom giữ chặt hai vai Ami ngay cửa gara, hét lớn rằng các tài xế xe tải đêm nay đã tự vũ trang.",
     "Trước ánh mắt bàng hoàng của Ami, Tom thú nhận thân phận LAPD rồi kéo cô lên chiếc Supra cam phóng đi.",
     "Bí mật lớn nhất của bộ phim được bật mí giữa tình thế ngàn cân treo sợi tóc."),
    (59, "Phản Đòn Trên Cao Tốc Sa Mạc", "D6 late afternoon", "DESERT_HIGHWAY", ["CEVIN_H", "VERNI", "MICDO_H"], ["CIVIC_TRIO", "RIG_18", "HARPOON_CABLE"], 5,
     "Trên xa lộ sa mạc, băng của Micdo áp sát chiếc container của Verni; khi Cevin đu cáp sang cabin, Verni bất ngờ hạ kính đánh trả quyết liệt khiến Cevin bị thương nặng và treo lơ lửng trên dây cáp.",
     "Chuyện gì xảy ra khi tài xế Verni đã chuẩn bị sẵn sàng để chống trả băng cướp?",
     "Cevin móc dây cáp phóng mình qua khoảng không hướng về phía cửa phụ cabin xe tải.",
     "Verni hạ kính chống trả dữ dội khiến Cevin trúng đòn nặng vào vùng bụng, mắc kẹt lơ lửng trên sợi cáp thép.",
     "Cái giá đắt của vụ cướp cuối: Cevin rơi vào cửa tử ngay giữa hai xe đang chạy tốc độ cao."),
    (60, "Xe Cina Gặp Nạn & Chiếc Supra Lao Tới", "D6 late afternoon", "DESERT_HIGHWAY", ["MICDO_H", "CINA_H", "TOM_R", "AMI_N"], ["CIVIC_TRIO", "RIG_18", "SUPRA"], 5,
     "Verni ép mạnh làm nổ lốp trước chiếc Civic của Cina khiến xe cô trượt văng khỏi làn đường; đúng lúc Micdo gào qua bộ đàm thì chiếc Toyota Supra cam của Tom và Ami xé gió lao tới.",
     "Ai có thể tiếp cận sợi cáp thép để cứu Cevin khi đội hình xe của Micdo đã vỡ vụn?",
     "Chiếc Civic của Cina bị nổ lốp trước, xoay vòng trượt dài ra lề cát sa mạc.",
     "Từ phía sau, chiếc Toyota Supra màu cam của Tom và Ami gầm rú vượt lên áp sát hông container.",
     "Chiếc xe 10 giây do Tom độ lại xuất hiện đúng khoảnh khắc sinh tử."),
    (61, "Cắt Cáp Cứu Người Ở Tốc Độ Cao", "D6 late afternoon", "DESERT_HIGHWAY", ["TOM_R", "AMI_N", "CEVIN_W"], ["SUPRA", "RIG_18", "HARPOON_CABLE"], 5,
     "Tom giao vô lăng chiếc Supra cho Ami giữ thẳng lái, còn mình nhoài nửa người ra ngoài cửa sổ cắt đứt sợi cáp thép và kéo Cevin vào ghế sau.",
     "Ami có giữ vững được tay lái ở tốc độ cao để Tom kéo Cevin thoát khỏi sợi cáp tử thần không?",
     "Tom đặt tay Ami lên vô lăng chiếc Supra cam rồi nhoài người ra ngoài cửa sổ xe.",
     "Tom dùng dao cắt đứt sợi cáp thép căng cứng, ôm trọn Cevin kéo vào khoang xe và đạp phanh tách khỏi đầu kéo.",
     "Màn giải cứu nghẹt thở gắn kết Tom, Ami và Cevin giữa lằn ranh sinh tử."),
    (62, "Cuộc Gọi Cứu Thương Mã LAPD 437", "D6 dusk", "DESERT_HIGHWAY", ["TOM_R", "MICDO_H", "CEVIN_W", "AMI_N"], ["SUPRA", "POLICE_RADIO"], 5,
     "Dừng xe bên lề sa mạc, thấy Cevin nguy kịch không thể chờ xe cấp cứu thường, Tom rút bộ đàm chuyên dụng đọc mã số 'Sĩ quan đặc nhiệm Tom, LAPD 437' gọi trực thăng y tế trước mặt Micdo.",
     "Để cứu mạng Cevin trong 5 phút cuối, Tom có dám tự phơi bày thân phận cảnh sát trước mặt Micdo không?",
     "Micdo giữ chặt vết thương cho Cevin đang thoi thóp bên lề đường cát sa mạc.",
     "Tom rút bộ đàm cảnh sát đọc vang mã hiệu LAPD 437 yêu cầu trực thăng y tế khẩn cấp tại xa lộ 86.",
     "Tom chọn cứu mạng người anh em của Micdo bằng cái giá là đánh mất hoàn toàn vỏ bọc."),
    (63, "Sự Thật Đổ Vỡ Dưới Cánh Trực Thăng", "D6 dusk", "DESERT_HIGHWAY", ["MICDO_H", "TOM_R", "CINA_H", "CEVIN_W"], ["SUPRA", "POLICE_RADIO"], 5,
     "Micdo bàng hoàng đứng dậy đối mặt Tom với ánh mắt vừa đau đớn vừa căm giận vì bị người anh em cùng bàn ăn lừa dối, rồi bế Cevin lên trực thăng cứu thương cắt đứt tình nghĩa.",
     "Micdo sẽ nói gì khi nhận ra người anh em mà mình bảo vệ lại chính là cảnh sát chìm?",
     "Micdo từ từ đứng dậy, nhìn chiếc bộ đàm trên tay Tom bằng ánh mắt sụp đổ hoàn toàn.",
     "Micdo gằn từng lời trách cứ sự phản bội của Tom rồi bế Cevin lên trực thăng y tế vừa đáp xuống.",
     "Mối quan hệ giữa Tom và Micdo tan vỡ hoàn toàn trước khi bước vào hồi kết."),

    # ACT 10 (Scenes 64–70): PHÂN CẢNH 10 — TRẬN CHIẾN CUỐI CÙNG VÀ CÁI KẾT (THE FINAL CHARGE)
    (64, "Bi Kịch Trước Hiên Nhà Toto", "D7 sunset", "TOTO_FRONT", ["SEJA_R", "MICDO", "AMI", "NYTRAN_R", "CELA"], ["JETTA", "MOTO_PACK"], 5,
     "Chiều tà trước nhà Toto, Seja mệt mỏi lái chiếc Jetta trắng trở về xin lỗi thì hai chiếc mô tô của Ny Tran và Cela Nguyen lao qua phục kích khiến Seja gục ngã trên bãi cỏ.",
     "Sự trở về muộn màng của Seja trước hiên nhà Toto gặp phải thảm kịch gì?",
     "Seja bước xuống từ chiếc Jetta trắng trước hiên nhà với gương mặt hối lỗi.",
     "Hai chiếc mô tô của Ny Tran và Cela lao vọt qua tấn công khiến Seja ngã gục trong vòng tay tuyệt vọng của Micdo.",
     "Cái chết của Seja đẩy cơn phẫn nộ của Micdo vượt qua mọi giới hạn."),
    (65, "Đánh Thức Quái Thú 900 Mã Lực", "D7 sunset", "TOTO_GARAGE", ["MICDO", "TOM_R", "AMI"], ["CHARGER", "SUPRA"], 5,
     "Đôi mắt hằn đỏ vì mất Seja, Micdo chạy vào gara giật tung tấm bạt phủ chiếc Dodge Charger 1970 công suất 900 mã lực của cha mình và phóng đi truy sát Ny Tran bất chấp tiếng gọi của Tom.",
     "Ai có thể cản được Micdo khi anh đã đánh thức con quái thú 900 mã lực của người cha quá cố?",
     "Micdo lao vào gara, giật phăng tấm bạt che chiếc Dodge Charger 1970 đen bóng.",
     "Bộ siêu nạp Supercharger gầm rú rung chuyển mặt đất khi Micdo phóng chiếc Charger ra đường còn Tom lái chiếc Supra đuổi theo.",
     "Chiếc Dodge Charger 1970 chính thức xuất trận cho cuộc rượt đuổi cuối cùng."),
    (66, "Đòn Trừng Phạt Trên Dốc Phố L.A.", "D7 sunset", "LA_HILLS_ROAD", ["MICDO", "TOM_R", "CELA", "NYTRAN_R"], ["CHARGER", "SUPRA", "MOTO_PACK"], 5,
     "Trên các con phố dốc Los Angeles, Micdo bẻ lái chiếc Charger khổng lồ húc văng đuôi xe của Cela Nguyen ở tốc độ 120 km/h khiến hắn ngã gục bên vách tường.",
     "Băng mô tô Light Saigon có chống đỡ nổi cơn thịnh nộ của chiếc Charger và chiếc Supra không?",
     "Chiếc Charger đen và chiếc Supra cam gầm rú bám sát hai chiếc mô tô trên đại lộ dốc đứng.",
     "Micdo đánh lái chiếc Charger chặn ép khiến mô tô của Cela văng vào vách tường bê tông bất tỉnh.",
     "Hạ gục Cela Nguyen, chỉ còn lại thủ lĩnh Ny Tran trên đường chạy trốn."),
    (67, "Ny Tran Đền Tội Dưới Kênh Thoát Nước", "D7 sunset", "LA_HILLS_ROAD", ["TOM_R", "NYTRAN_R", "MICDO"], ["SUPRA", "CHARGER", "MOTO_PACK"], 5,
     "Ny Tran quay đầu mô tô định tấn công Micdo nhưng Tom lao chiếc Supra lên song song khống chế chuẩn xác khiến mô tô của Ny Tran mất lái lao xuống kênh thoát nước nổ tung.",
     "Tom sẽ làm gì để bảo vệ Micdo trước đòn phản kích liều lĩnh của Ny Tran?",
     "Ny Tran ngoái lại trên yên mô tô định ra đòn về phía chiếc Charger của Micdo.",
     "Tom vọt chiếc Supra lên ngang hàng khống chế tay lái khiến chiếc mô tô của Ny Tran lao xuống kênh thoát nước bốc cháy.",
     "Kết thúc mối đe dọa từ băng Light Saigon, mở ra cuộc đối mặt cuối cùng giữa Tom và Micdo."),
    (68, "Một Phần Tư Dặm Trước Đường Ray", "D7 sunset", "RAIL_CROSSING", ["MICDO", "TOM_R"], ["CHARGER", "SUPRA"], 5,
     "Micdo không dừng lại mà lái chiếc Charger ra đường ngoại ô; hai chiếc xe dừng song song trước đường ray khi chuông tàu hỏa reo vang và Micdo rủ 'Sĩ quan Tom' đua trận cuối cùng.",
     "Khi mọi ân oán đã khép lại, Tom và Micdo sẽ giải quyết số phận của nhau bằng cách nào?",
     "Chiếc Charger đen và chiếc Supra cam dừng song song trước vạch chắn đường sắt đang nhấp nháy đèn đỏ.",
     "Micdo hạ kính nhắc lại triết lý sống vì 1/4 dặm tự do và rủ Tom đua trận cuối ngay khi đoàn tàu lao tới.",
     "Đỉnh cao cảm xúc của tình anh em và đam mê tốc độ."),
    (69, "Cắt Đầu Tàu Hỏa & Cú Lật Kinh Hoàng", "D7 sunset", "RAIL_CROSSING", ["MICDO", "TOM_R"], ["CHARGER", "SUPRA"], 5,
     "Hai chiếc xe gầm rú lao vút đi, chiếc Charger bốc đầu vượt qua đường ray chỉ một tích tắc trước mũi tàu hỏa nhưng ngay sau đó đâm sầm vào xe tải ngang đường, lộn nhào ba vòng.",
     "Ai sẽ về đích trong cuộc đua cắt đầu tàu hỏa và tai họa nào đang chờ ở bên kia đường ray?",
     "Mô-men xoắn cực đại nhấc bổng hai bánh trước chiếc Charger khi cả hai xe lao vút qua đường ray trước mũi tàu hỏa.",
     "Vừa qua khỏi đường ray, một chiếc xe tải từ hẻm lao ra khiến chiếc Charger va chạm mạnh, bay lộn nhào và lật ngửa bốc khói.",
     "Biến cố nghẹt thở ngay sau khoảnh khắc thăng hoa nhất của cuộc đua."),
    (70, "Chìa Khóa Con Xe 10 Giây", "D7 dusk", "CROSSING_BEYOND", ["TOM_R", "MICDO_W", "NESE_T"], ["SUPRA", "CHARGER", "SUPRA_KEY"], 5,
     "Tom kéo Micdo bị thương khỏi xác chiếc Charger ngay khi còi cảnh sát của Nese vang lên từ xa; Tom đặt chìa khóa chiếc Supra cam vào tay Micdo để trả nợ 'con xe 10 giây' rồi một mình đứng lại chịu trách nhiệm.",
     "Khi tiếng còi cảnh sát LAPD đã ở ngay đầu đường, Tom sẽ chọn chiếc huy hiệu hay chọn trả món nợ 10 giây cho người anh em?",
     "Tom phá cửa kéo Micdo thoát khỏi khoang lái chiếc Charger đang bốc khói giữa tiếng còi cảnh sát vọng lại.",
     "Tom đặt chìa khóa chiếc Supra cam vào tay Micdo, nhìn anh phóng vút về phía chân trời rồi giơ hai tay đứng đợi xe của Nese.",
     "Cái kết trọn vẹn và bi tráng: Tom giữ trọn lời hứa con xe 10 giây và danh dự của hai tay đua."),
]


FIRST_INTRO_CLIPS = {
    "01.1": ("VERNI", "Verni, tài xế xe đầu kéo đường dài trên xa lộ mười."),
    "02.1": ("CEVIN", "Cevin, cánh tay phải liều lĩnh trong đội xe của Micdo."),
    "04.1": ("CINA", "Cina, nữ quái tốc độ sát cánh cùng Micdo."),
    "05.1": ("ONLE", "Onle, tay lái bọc hậu và thợ máy của cả đội."),
    "07.1": ("TOM", "Tom, sĩ quan cảnh sát chìm ẩn náu trong tiệm độ xe."),
    "08.1": ("AMI", "Ami, cô gái út nhà Micdo, người giữ quán ăn gia đình."),
    "10.1": ("SEJA", "Seja, thiên tài toán học và điện tử độ xe của nhóm."),
    "13.1": ("MICDO", "Micdo, tay đua huyền thoại và thủ lĩnh cả đội."),
    "15.1": ("NESE_KINAN", "Trung sĩ Nese của LAPD và đặc vụ liên bang Kinan."),
    "29.1": ("NYTRAN_CELA", "Ny Tran, thủ lĩnh Light Saigon, cùng gã anh họ Cela."),
}

# Canonical scene-specific dialogue banks so every clip has unique, natural Southern Vietnamese dialogue
SCENE_DIALOGUES = {
    1: [
        "Cái quái gì phía sau vậy, lại là tụi xe đen nữa hả.",
        "Ba chiếc kèm sát ba bên luôn, tụi này tính ép đầu kéo rồi.",
        "Đèn gầm xanh lá kiểu này chỉ có băng đua đường đêm thôi.",
        "Đừng hòng ép xe tao vô lề, chuyến hàng này giao gấp lắm.",
        "Tụi nó khóa cứng làn trái với làn phải luôn rồi kìa.",
        "Phải giữ đều ga vượt qua đèo này trước khi tụi nó áp sát.",
    ],
    2: [
        "Giữ vững tốc độ một trăm ba, để tao lên nóc bắn cáp.",
        "Đầu xe nó lắc dữ lắm, canh ngay khung kính phụ mà bắn.",
        "Mũi cáp ăn chắc vô thành sắt rồi, khóa móc an toàn lại.",
        "Cẩn thận gió tạt ngang đó Cevin, dây cáp căng hết cỡ rồi.",
        "Nó định lắc đầu kéo hất tụi mình ra, giữ chặt tay lái đi.",
        "Tao chuẩn bị phóng qua cabin nó đây, giữ khoảng cách đều nghen.",
    ],
    3: [
        "Bám chắc dây cáp rồi, tao đáp qua cửa phụ đầu kéo ngay.",
        "Buông tay khỏi cái đồ dưới ghế ngay, ngồi yên cho tao.",
        "Thằng khốn liều mạng này, tụi mày cướp đường trắng trợn vậy sao.",
        "Ngồi im nếu không muốn văng khỏi cabin ở tốc độ này.",
        "Tao đạp phanh hạ tốc rồi, báo cho Cina tiến lên mở thùng.",
        "Đầu kéo đã nằm trong tay tao, đội sau vào lấy hàng lẹ đi.",
    ],
    4: [
        "Áp sát đuôi thùng xe đi, để chị gắn bộ mở chốt từ tính.",
        "Gió hút mạnh quá, giữ đầu xe cách cản sau nửa thước thôi.",
        "Chốt từ ăn đèn đỏ rồi, lùi nhẹ nửa thân xe chờ bung cửa.",
        "Hai cánh cửa thùng bật mở rồi kìa, hàng điện tử chất đầy trong đó.",
        "Gọi Onle đôn chiếc thứ ba lên nhận hàng ngay kẻo trễ giờ.",
        "Giữ nguyên làn giữa cho Onle áp nắp xe vô sát sàn thùng.",
    ],
    5: [
        "Đưa mũi xe sát vô gầm thùng, mở sẵn khóa nắp trước rồi.",
        "Chuyển từng kiện hàng lớn qua trước, tay chân lẹ làng lên anh em.",
        "Đầu đọc kỹ thuật số nguyên đai nguyên kiện, đúng lô hàng giá trị cao.",
        "Còn ba kiện cuối bên góc phải, kéo nốt qua khoang sau luôn.",
        "Đủ số lượng rồi đó, đóng nắp cốp lại chuẩn bị tách đội hình.",
        "Báo lên đầu kéo cho Cevin rút lui trước khi tới trạm tuần tra.",
    ],
    6: [
        "Thu dây cáp về, nhảy qua cửa sổ trời rút khỏi đầu kéo ngay.",
        "Tắt hết dàn đèn gầm xanh đi, chuẩn bị rẽ xuống nhánh đường phụ.",
        "Tụi nó rút sạch trong bóng tối rồi, đầu kéo mất đà chao đảo quá.",
        "Lũ cướp đường táo tợn thiệt, chuyến sau tao không để yên đâu.",
        "Chia ba ngả về điểm tập kết, đừng để xe nào bám đuôi theo.",
        "Đường cao tốc lại vắng tanh như chưa từng có chuyện gì xảy ra.",
    ],
    7: [
        "Cụm tăng áp chiếc xanh này chỉnh xong rồi, chiều nay chạy thử được.",
        "Đêm qua trên xa lộ mười lại có thêm một xe đầu kéo bị cướp.",
        "Cánh tài xế đường dài đang giận sôi máu vì mất trắng lô hàng lớn.",
        "Ông kiểm tra giùm bộ ống dẫn khí, tối nay cần xe chạy thật bốc.",
        "Nhớ siết kỹ cổ góp nghe chưa, giờ nghỉ trưa rồi qua quán Toto đi.",
        "Lấy chiếc bán tải đỏ chở thùng phụ tùng rồi ghé quán ăn trưa luôn.",
    ],
    8: [
        "Cho anh một phần bánh mì cá ngừ cắt vỏ như mọi hôm nghen.",
        "Ngày nào anh cũng tới gọi đúng món đó, bộ không thấy ngán hả.",
        "Nói thiệt món cá ngừ ở quán này dở tệ, chẳng ai thèm gọi đâu.",
        "Nhưng anh lại thích đúng cái vị do chính tay em làm mỗi trưa.",
        "Cắt xong phần vỏ bánh rồi đây, nước đá lạnh của anh luôn nè.",
        "Nhìn bộ đồ dính dầu máy là biết sáng giờ anh cắm đầu dưới gầm xe.",
    ],
    9: [
        "Thừa nhận đi, anh ghé quán mỗi trưa đâu phải vì dĩa bánh mì này.",
        "Đúng vậy, anh tới đây mỗi ngày chỉ để được nhìn thấy em thôi.",
        "Miệng lưỡi thợ máy ở tiệm ông Ryh ngày càng dẻo quá chừng rồi đó.",
        "Anh nói thiệt lòng mà, ngồi đây nhìn em dọn quán thấy bình yên lắm.",
        "Ăn lẹ đi kẻo bánh nguội, lát nữa nhóm anh trai em ghé qua đông lắm.",
        "Nghe tiếng pô xe ngoài đầu đường kìa, chắc tụi anh Cevin vừa tới.",
    ],
    10: [
        "Chiếc bán tải đỏ của thằng cha hôm qua lại đậu chình ình trước quán kìa.",
        "Tụi mình ghé uống nước thôi mà, làm gì mặt anh căng dữ vậy Cevin.",
        "Tao đã dặn nó đừng bén mảng tới gần Ami từ hôm qua rồi.",
        "Để tụi này coi thử thằng thợ máy mới của ông Ryh gan cỡ nào.",
        "Đừng làm ồn trước cửa quán nữa, khách khứa người ta nhìn kìa anh em.",
        "Bước vô trong coi nó còn dám ngồi liếc mắt nhìn Ami nữa không.",
    ],
    11: [
        "Thằng ranh này, tao đã bảo mày biến khỏi quán từ hôm qua rồi mà.",
        "Tôi chỉ là khách ghé ăn trưa đàng hoàng và trả tiền đủ thôi anh bạn.",
        "Nhìn cái mặt mày là biết tới rình mò quanh Ami chứ ăn uống gì.",
        "Thôi nào Cevin, để yên cho người ta ăn xong dĩa bánh đi mà.",
        "Tránh ra đi Cina, thằng lính mới này có cái mùi rất chướng mắt.",
        "Biến khỏi đây trước khi tao bẻ gãy răng mày, hay muốn thử ngay bây giờ.",
    ],
    12: [
        "Muốn động tay động chân thì bước ra hiên, đừng làm bể đồ trong quán.",
        "Mày dám né đòn của tao hả, hôm nay tao dạy cho mày biết điều.",
        "Hai người dừng tay lại ngay đi, đừng đánh nhau làm sập bàn của quán.",
        "Thằng thợ máy này ra đòn gọn gàng dữ, Cevin bị khóa tay luôn kìa.",
        "Cevin dừng lại ngay cho em, anh tính phá nát quán của gia đình hả.",
        "Tiếng động cơ quay ngoài đường lớn kìa, anh Micdo về tới nơi rồi đó.",
    ],
    13: [
        "Đủ rồi đó, Cevin lùi lại ngay lập tức cho tao.",
        "Thủ lĩnh coi kìa, thằng khốn này dám tới quán cưa cẩm Ami rồi làm loạn.",
        "Tao bảo lùi lại một bước, ở địa bàn này ai cho phép tụi mày tự tiện.",
        "Dọn mấy cái ghế gãy qua một bên, đừng để em gái tao phải dọn dẹp.",
        "Cậu đứng dậy phủi áo đi, nhìn thẳng vô mắt tao rồi trả lời.",
        "Làm việc ở tiệm phụ tùng của lão Ryh mà dám tới đây gây chuyện sao.",
    ],
    14: [
        "Lão Ryh là chỗ quen biết, tao nể lão ấy nhưng quán này là của nhà tao.",
        "Tôi không cố ý gây sự trước, chỉ tự vệ khi người của anh ra tay.",
        "Cậu đã làm đổ máu ở sân nhà tao thì không còn chuyện khách khứa gì nữa.",
        "Cầm lấy chìa khóa cái xe tải cũ kỹ của cậu rồi rời khỏi đây ngay.",
        "Đừng bao giờ để tao thấy mặt ở quán này nữa, tao không nói lần thứ hai.",
        "Được thôi, tôi đi ngay nhưng chuyện giữa chúng ta chưa dừng ở đây đâu.",
    ],
    15: [
        "Vết bầm trên mặt đẹp lắm, cậu vừa bị đám thợ máy đường phố dần cho hả.",
        "Đó là Cevin, cánh tay phải nóng nảy nhất trong đội xe của Micdo.",
        "Ít ra sau vụ va chạm đó cả đám người của Micdo đã nhớ mặt tôi.",
        "Nhớ mặt bằng cách bị đuổi thẳng cổ khỏi quán ăn của gia đình tụi nó sao.",
        "Nhưng em gái hắn là Ami đã bắt đầu tin tưởng và đứng về phía tôi.",
        "Vào bàn chiến thuật đi, đặc vụ Kinan có tin không mấy vui vẻ đâu.",
    ],
    16: [
        "Theo sát quán Toto mấy hôm nay thì Cevin chính là kẻ giữ đồ nghề trong nhóm.",
        "Chỉ dựa vào một trận đánh nhau ngoài hiên quán thì chưa xin được lệnh khám xét.",
        "Tôi cần thêm vài ngày để tách Ami và nắm lịch hoạt động ban đêm của họ.",
        "Chúng ta không có thời gian cho cậu đóng kịch gia đình ở đây đâu.",
        "Mỗi đêm trôi qua là thêm một chuyến xe điện tử trị giá hàng triệu đô biến mất.",
        "Nếu không bắt quả tang tại trận thì mọi suy đoán đều vô giá trị trước tòa.",
    ],
    17: [
        "Đọc biên bản của Verni đi, bốn vụ cướp đầu kéo chỉ trong vòng hai tuần.",
        "Giới tài xế đường dài đang phát điên và dọa sẽ tự trang bị vũ khí phòng thân.",
        "Nếu tụi cướp đụng độ tài xế có vũ trang thì xa lộ mười sẽ thành bãi chiến trường.",
        "Cấp trên ở cục liên bang đang đòi kết quả từng giờ một chứ không phải từng tuần.",
        "Vậy ông phải cho tôi phương tiện đủ mạnh để bước thẳng vào sào huyệt của chúng.",
        "Với đám quái xế này, lời nói không có trọng lượng bằng tốc độ trên đường nhựa.",
    ],
    18: [
        "Đừng quên bên điều tra liên bang vẫn đang đặt nghi vấn lên băng Light Saigon.",
        "Ny Tran và gã anh họ Cela vừa thuê thêm hai kho lớn gần cảng.",
        "Băng của Ny Tran rất tàn nhẫn nhưng cách chạy xe của chúng hoàn toàn khác.",
        "Ba chiếc xe đen hôm qua dùng lốp và bộ giảm xóc đặt riêng cho đường trường.",
        "Dù là Micdo hay Ny Tran thì cả hai phe đều sẽ lộ mặt ở giải đua đêm.",
        "Cậu định dùng cách gì để buộc Micdo cho cậu bước chân vào đội của hắn.",
    ],
    19: [
        "Đêm nay Tohe tổ chức giải đua một phần tư dặm lớn nhất khu Nam thành phố.",
        "Micdo chắc chắn sẽ mang chiếc xe đỏ của hắn ra giữ ngôi vương ở đó.",
        "Tôi sẽ lái chiếc xe xanh neon mà đơn vị vừa độ xong ra thách đấu hắn.",
        "Chiếc xe đó ngốn gần tám chục ngàn đô ngân sách kỹ thuật của đội đặc nhiệm.",
        "Muốn câu được con cá lớn nhất thì mồi câu cũng phải xứng tầm với nó.",
        "Chỉ cần chạy ngang ngửa với Micdo trên đường đua, hắn sẽ tự mở cửa đón tôi.",
    ],
    20: [
        "Giấy tờ đăng ký hợp pháp của chiếc xe xanh nằm trong phong bì này đây.",
        "Hãy nhớ kỹ, nếu cậu thua và mất xe thì mất luôn chiếc phao cứu sinh duy nhất.",
        "Đừng để cái tôi của một tay đua lấn át nhiệm vụ của một sĩ quan cảnh sát.",
        "Tôi hiểu rõ cái giá phải trả, đêm nay tôi sẽ không trở về tay trắng.",
        "Đội giám sát sẽ chỉ hỗ trợ vòng ngoài để tránh làm lộ vỏ bọc của cậu.",
        "Tôi đi chuẩn bị xe đây, hẹn gặp lại hai người sau khi có tin từ đường đua.",
    ],
    21: [
        "Hai bình khí tăng tốc đã nạp đầy áp suất, hệ thống phun nhiên liệu rất ổn định.",
        "Bản đồ động cơ trên máy tính cho thấy cổ góp sẽ chịu nhiệt cực lớn ở tua cao.",
        "Cậu nhớ đừng bấm bình thứ hai quá sớm kẻo áp lực làm bung cả sàn xe.",
        "Đối đầu với chiếc xe động cơ quay của Micdo thì không thể chạy giữ sức được.",
        "Ráng giữ nhịp sang số thật chuẩn, con xe này đủ sức chạm ngưỡng mười giây.",
        "Cảm ơn ông chủ, đêm nay tôi nhất định phải lấy được sự tôn trọng của hắn.",
    ],
    22: [
        "Đêm nay luật chơi vẫn như cũ, mỗi xe bước vào vạch góp hai ngàn đô tiền mặt.",
        "Ai cán đích trước ở đoạn đường một phần tư dặm này sẽ ôm trọn toàn bộ tiền cược.",
        "Ai không có đủ tiền mặt trong tay thì dạt qua hai bên lề cho rảnh đường.",
        "Tiền của tôi đủ cả xấp đây, con xe độ của tôi đêm nay chấp hết.",
        "Đếm cho kỹ đi, phần góp của tôi không thiếu một đồng lẻ nào đâu.",
        "Còn một làn trống cuối cùng, để coi đêm nay ai dám ra so kè với nhà vô địch.",
    ],
    23: [
        "Đám đông dạt hết ra kìa, chiếc xe đỏ của nhà vô địch đang tiến vào vạch.",
        "Khoan khóa sổ đã, giữ lại một làn trống cho xe của tôi tham gia cùng.",
        "Nhìn coi ai mò tới kìa, thằng nhóc ăn bánh mì cá ngừ hồi trưa chứ ai.",
        "Mày móc đâu ra hai ngàn đô tiền mặt mà đòi chen chân vô đường đua này.",
        "Cậu gan lắm mới dám vác mặt tới địa bàn đua đêm của tụi này một lần nữa.",
        "Tôi tới đây không phải để cãi nhau với đàn em của anh, tôi tới để đua.",
    ],
    24: [
        "Tôi không mang tiền mặt nhưng có giấy tờ sở hữu hợp pháp của chiếc xe này.",
        "Con xe này đáng giá hơn mười ngàn đô, tôi đặt cược bằng chính chiếc xe.",
        "Kèo thơm nhất đêm nay đây rồi, lấy giấy tờ xe đấu tiền mặt luôn.",
        "Cậu điên rồi nhóc, cậu định đem con xe đó ra đấu với xe của tao sao.",
        "Nếu anh thắng thì lấy xe, còn nếu tôi thắng tôi muốn có sự tôn trọng của anh.",
        "Được thôi, nổ máy nhập làn đi, để coi dưới nắp máy cậu có bản lĩnh gì.",
    ],
    25: [
        "Tất cả vào vạch sẵn sàng chưa, nhìn tay tôi phất xuống là đạp ga chạy.",
        "Hai chiếc bên hông tụt lại rồi, chỉ còn chiếc đỏ đang vọt lên dẫn đầu.",
        "Tua máy chạm vạch đỏ rồi nhưng vẫn kém mũi xe hắn nửa thân chiều dài.",
        "Chưa kết thúc đâu, tới lúc phải mở van bình khí tăng tốc đầu tiên rồi.",
        "Mũi xe vọt lên ngang cửa kính hắn rồi, giữ chặt vô lăng đừng để trượt bánh.",
        "Màn hình máy tính đang chớp đỏ báo quá tải cổ góp, áp suất tăng nhanh quá.",
    ],
    26: [
        "Cố thêm một nhịp cuối nữa thôi, mở tiếp bình khí tăng tốc thứ hai luôn.",
        "Tấm sàn thép bên ghế phụ bung chốt rồi, tia lửa đang quét rực dưới gầm xe.",
        "Chiếc xe đỏ sang số ngọt quá, hắn lướt qua vạch đích trước đúng một thân xe.",
        "Cậu chạy khá lắm nhóc, suýt chút nữa là làm nên chuyện lớn trước mặt tao rồi.",
        "Nhưng cậu bấm khí quá sớm làm hỏng cả cổ góp, giờ thì đưa chìa khóa xe đây.",
        "Chiếc xe này theo luật đã thuộc về anh, nhưng nghe tiếng còi hú đằng kia kìa.",
    ],
    27: [
        "Xe tuần tra cảnh sát ập tới từ bốn phía rồi, tất cả tản ra mau lên.",
        "Đám đông kẹt cứng lối ra chính, mạnh ai nấy phóng xe tháo chạy tứ tán.",
        "Tách khỏi chiếc xe đỏ đi, chạy bộ băng qua con hẻm kho hàng phía sau.",
        "Đầu hẻm bên kia cũng có hai xe tuần tra vừa bật đèn chớp chặn ngang rồi.",
        "Phía sau lưng thêm một xe cảnh sát nữa đang ép vô, hết đường thoát thân rồi.",
        "Quay đầu chiếc xe xanh lại ngay, không thể để hắn bị bắt ngay lúc này được.",
    ],
    28: [
        "Lên xe mau đi, nếu anh không muốn đêm nay phải vào trại giam ngồi bóc lịch.",
        "Con xe đang bốc khói gầm mà cậu còn dám quay đầu lao vô vòng vây sao.",
        "Bám chắc tay vịn ghế phụ đi, tôi sẽ lách qua khe thùng gỗ bên phải.",
        "Cú xoay đầu xe vừa khít gang tấc, xe tuần tra phía sau bị kẹt lại rồi.",
        "Đạp lút ga băng qua con dốc sắt này là cắt đuôi được đèn xe cảnh sát.",
        "Thoát khỏi vòng vây rồi, nhưng tiếng động cơ xe máy phía trước nghe lạ lắm.",
    ],
    29: [
        "Cả chục chiếc mô tô phân khối lớn màu đen đang khóa chặt đầu đường kìa.",
        "Đó là đám người của băng Light Saigon, tụi mình vô tình chạy lọt vô lãnh địa chúng.",
        "Tụi nó ép sát hai bên hông xe rồi, không còn khoảng trống để lùi lại đâu.",
        "Tấp xe vô bãi đất trống bên phải đi, đừng manh động kẻo tụi nó làm liều.",
        "Giữ cái đầu lạnh và để một mình tôi nói chuyện với tên cầm đầu ngoài đó.",
        "Hai gã chạy dẫn đầu vừa dừng xe chặn ngay trước mũi nắp capô của mình.",
    ],
    30: [
        "Tất cả tắt máy bước xuống xe ngay, giơ hai bàn tay lên cho tao thấy.",
        "Bình tĩnh đi Ny Tran, tụi tao chỉ lách cảnh sát đi ngang qua đây thôi.",
        "Đi ngang qua mà kéo cả khói xe mù mịt vô sát khu kho bãi của tao sao.",
        "Còn thằng ranh con mặc áo da này là ai, mặt mũi nhìn lạ hoắc vậy.",
        "Nó chỉ là lính mới vừa nhập hội đêm nay, chưa rành ranh giới khu này.",
        "Lính mới của tay đua lừng danh mà phải chạy một con xe bốc khói thảm hại vậy.",
    ],
    31: [
        "Nhìn kỹ con xe màu xanh này coi, toàn đồ độ đắt tiền gắn đầy khoang máy.",
        "Đồ nghề ngon lành cỡ này mà giao cho một thằng không biết cầm lái thì phí quá.",
        "Đường dao cào trên nắp sơn này là để đánh dấu chỗ tụi mày vừa bước chân vô.",
        "Kìm cái tay lại đi nhóc, một mình cậu không đấu lại cả chục người ở đây đâu.",
        "Sàn xe bên phụ còn rớt cả tấm chắn nhiệt ra ngoài, chạy kiểu gì tệ hại vậy.",
        "Để coi sau đêm nay thằng lính mới này còn giữ nổi chiếc xe mà chạy nữa không.",
    ],
    32: [
        "Nghe cho rõ đây, xưa nay mày đua đường của mày còn tao làm ăn đường của tao.",
        "Nhưng dạo gần đây người của mày cứ lảng vảng quanh khu kho hàng bến cảng của tao.",
        "Tao đã nói rồi, đội của tao không hề đụng chạm gì tới chuyện làm ăn của mày.",
        "Mày tưởng tao tin lời nói suông khi nửa đêm tụi mày mò tới sát ranh giới này sao.",
        "Nếu tụi mày đang tính kiếm chuyện hớt tay trên lô hàng của tao thì lầm to rồi.",
        "Chúng tôi chỉ tình cờ rẽ vào đây tránh xe tuần tra chứ không dòm ngó kho hàng nào.",
    ],
    33: [
        "Thằng lính mới chưa được hỏi tới mà đã dám mở miệng trả treo trước mặt tao hả.",
        "Chuyện này là giữa tao với mày, đừng lôi người mới vô làm lớn chuyện đêm nay.",
        "Muốn giữ hòa khí thì cũng phải có cái giá để nhớ cho kỹ luật lệ vùng này.",
        "Lùi hết ra sau ba bước, để tao dạy cho thằng lính mới bài học về chọn phe.",
        "Khoan đã Ny Tran, chiếc xe đó không liên quan gì tới hiềm khích của hai bên.",
        "Không liên quan thì đêm nay nó cũng phải nằm lại bãi đất này làm gương.",
    ],
    34: [
        "Dừng lại đi, trong cốp sau còn hai bình khí tăng tốc đang rò áp suất đó.",
        "Bình nhiên liệu phía sau bén lửa rồi, lùi xa khỏi thân xe ngay lập tức.",
        "Cả chiếc xe bùng cháy thành biển lửa rồi, không còn cứu vãn được gì nữa đâu.",
        "Coi như đống sắt cháy đen đó là học phí đầu đời cho tụi mày nhớ mặt tao.",
        "Biến khỏi khu đất này ngay trước khi tao đổi ý giữ cả hai đứa mày lại.",
        "Đi thôi nhóc, đứng nhìn đống tro tàn đó thêm nữa cũng không lấy lại được xe đâu.",
    ],
    35: [
        "Một đêm trắng tay thật sự, chiếc xe tâm huyết giờ chỉ còn là khung sắt cháy đen.",
        "Ít ra hai cái mạng của tụi mình vẫn còn nguyên vẹn để đi bộ về tới đây.",
        "Anh không trách chuyện tôi bấm khí quá sớm làm hỏng cuộc đua hồi nãy sao.",
        "Nếu cậu không quay đầu xe lao vô con hẻm đó thì giờ này tao đang ngồi trong khám.",
        "Mặt mũi hai anh em dính đầy muội than đen kịt, về tới sân chắc tụi nó hết hồn.",
        "Vào sân sau đi, giờ này cả đám vẫn còn đang nướng thịt chờ tin của tao đó.",
    ],
    36: [
        "Anh cả về rồi kìa, nhưng sao hai người lại đi bộ với mặt mũi đen thui vậy.",
        "Chuyện gì đã xảy ra với chiếc xe đỏ và con xe xanh của thằng nhóc này thế.",
        "Chiếc xe đỏ vẫn cất an toàn ở bãi phụ, còn xe của cậu ta thì tan xác rồi.",
        "Hai người có bị thương ở đâu không, ngồi xuống ghế uống ngụm nước trước đã.",
        "Sao thằng cha khách ăn bánh mì hồi trưa lại đi chung với anh về tận sân nhà.",
        "Tất cả gom lại quanh bàn nướng đi, tao có chuyện quan trọng cần tuyên bố đêm nay.",
    ],
    37: [
        "Đêm nay nếu không có cậu ta liều mạng quay xe lại thì tao đã nằm trong trại giam.",
        "Con xe xanh của cậu ta cũng vừa bị đám người của Ny Tran đốt cháy rụi ngoài bãi đất.",
        "Từ giờ phút này cậu ta là người của gia đình mình, ai đụng tới nó là đụng tới tao.",
        "Em vẫn chưa tin được hắn đâu anh cả, hắn xuất hiện đúng lúc tới mức đáng ngờ.",
        "Lời tao nói ra là quyết định cuối cùng, không ai được bàn ra tán vào chuyện này nữa.",
        "Cảm ơn anh đã tin tưởng, tôi sẽ không làm gia đình này phải thất vọng đâu.",
    ],
    38: [
        "Đưa mặt qua đây em lau bớt vết muội than trên gò má cho, khói bám dày quá.",
        "Cảm ơn em, vết xước hồi trưa cộng thêm khói lửa đêm nay nhìn chắc dữ tợn lắm.",
        "Anh không sao là tốt lắm rồi, lúc nghe tin cảnh sát vây đường đua em lo muốn chết.",
        "Anh đã hứa là sẽ không để chuyện gì xấu xảy ra với người nhà của em mà.",
        "Uống miếng nước mát rồi ăn chút thịt nướng đi, đêm nay anh vất vả quá nhiều rồi.",
        "Thấy hai người nói chuyện hợp ý vậy chắc từ mai quán hết ế món cá ngừ rồi.",
    ],
    39: [
        "Tôi đã tính toán kỹ rồi, con xe xanh của cậu cháy rụi nghĩa là kèo cược chưa thanh toán.",
        "Theo nguyên tắc đường đua thì cậu vẫn đang nợ anh cả một con xe chạy dưới mười giây.",
        "Đúng đó, muốn trả hết nợ cho thủ lĩnh thì phải dựng được một con xe mười giây thực thụ.",
        "Cậu chỉ cần kiếm được một cái xác xe có khung gầm tốt đem về xưởng sau nhà này.",
        "Tôi với Onle sẽ tháo máy độ lại từ đầu tới cuối cho cậu đủ sức đấu mọi đối thủ.",
        "Tôi hứa sẽ mang về cho các anh một con xe mười giây đúng nghĩa, cứ chờ xem.",
    ],
    40: [
        "Cậu hứa mang về xe mười giây mà lại kéo cái khung sắt rỉ sét này tới xưởng sao.",
        "Nhìn lớp vỏ móp méo này coi, đẩy bộ qua vạch đích còn chưa nổi huống chi là đua.",
        "Khoan chê đã anh em, dở cái nắp máy lên nhìn khối động cơ bên dưới trước đi.",
        "Trời đất ơi, nguyên khối động cơ tăng áp kép huyền thoại còn nguyên vẹn bên trong kìa.",
        "Chỉ cần đại tu lại dàn hơi và gắn bộ điều khiển mới là biến thành quái vật ngay.",
        "Xắn tay áo lên thôi anh em, đưa cái khung xe này lên cầu nâng bắt đầu làm liền.",
    ],
    41: [
        "Siết thêm nửa vòng ốc cổ xả nữa là áp suất buồng đốt đạt mức hoàn hảo luôn.",
        "Lớp sơn màu cam ánh kim mới phủ lên nhìn lột xác hoàn toàn so với lúc mới kéo về.",
        "Mấy anh em nghỉ tay ăn chút đồ nóng đi, làm suốt từ chiều tới khuya không biết mệt hả.",
        "Nhìn mọi người chung tay dựng lại con xe này, tôi mới hiểu thế nào là một gia đình.",
        "Ở đây tụi này không có nhiều tiền bạc nhưng đã coi nhau là anh em thì sống chết có nhau.",
        "Ngày mai đưa con xe màu cam này ra đường thử, đảm bảo cả thành phố phải ngước nhìn.",
    ],
    42: [
        "Đi theo tao vô góc trong cùng của xưởng, có thứ này tao muốn cho riêng cậu xem.",
        "Đây là chiếc xe cơ bắp đời một chín bảy mươi mà cha tao đã cùng tao dựng lên.",
        "Khối siêu nạp chín trăm mã lực này mạnh tới mức tới giờ tao vẫn chưa dám cầm lái.",
        "Vì sao một tay đua không biết sợ gì như anh lại ngại cầm lái con xe của cha mình.",
        "Bởi vì trong mười giây ngắn ngủi trên đường đua đó, tao mới thực sự cảm thấy mình tự do.",
        "Tôi hiểu cảm giác đó, có những giới hạn mà khi bước qua rồi sẽ không thể quay đầu lại.",
    ],
    43: [
        "Thời hạn điều tra đã cạn rồi, sáng mai đội đặc nhiệm bắt buộc phải ra quân bắt người.",
        "Nếu chưa có bằng chứng trực tiếp ở chỗ Micdo thì hãy kiểm tra kho hàng của Ny Tran trước.",
        "Đêm đua xe vừa rồi chính Ny Tran đã cảnh cáo về các kho hàng điện tử ở bến cảng.",
        "Cậu chắc chắn lũ người của Light Saigon đang cất giấu lô hàng cướp được ở đó chứ.",
        "Họ canh phòng khu bãi đất và kho sau nhà cực kỳ nghiêm ngặt bằng cả đội xe phân khối lớn.",
        "Được, rạng sáng mai toàn bộ lực lượng sẽ đột kích thẳng vào dinh thự của Ny Tran.",
    ],
    44: [
        "Tất cả các mũi tác chiến đã vào vị trí bao vây quanh khu dinh thự ngay lúc rạng đông.",
        "Cổng chính đã mở, đội xung kích tiến nhanh vào sân trong và khóa chặt lối thông ra kho sau.",
        "Đừng để bất kỳ ai bên trong kịp tẩu tán tài liệu hay chứng từ xuất nhập hàng hóa.",
        "Tôi sẽ ngồi lại trên xe chỉ huy để tránh làm lộ thân phận trước mặt đám đàn em ở đây.",
        "Kiểm soát toàn bộ khuôn viên, đưa những người có mặt trong nhà ra khu vực sân chính.",
        "Mũi thứ hai theo tôi tiến thẳng ra dãy nhà kho chứa hàng điện tử phía sau lưng.",
    ],
    45: [
        "Tất cả đứng yên tại chỗ, chúng tôi có lệnh kiểm tra toàn bộ khu vực kho bãi này.",
        "Các người làm cái quái gì vậy, gia đình tôi làm ăn lương thiện và đóng thuế đầy đủ.",
        "Đừng có lớn tiếng chống đối, giữ gã bảo vệ và đám người này ngồi yên tại phòng khách.",
        "Các người tự tiện xông vào nhà dân lúc sáng sớm mà không sợ pháp luật trừng phạt sao.",
        "Lục soát kỹ từng kiện hàng điện tử bên dưới xem có khớp với danh sách bị mất không.",
        "Dẫn Ny Tran và gã anh họ Cela ra ngoài sân trước để chờ đối chiếu biên bản kiểm kê.",
    ],
    46: [
        "Đưa hai tên cầm đầu này ra đứng cạnh xe chỉ huy, giữ chặt hai tay chúng lại.",
        "Kính cửa sau chiếc xe kia vừa hé xuống kìa, nhìn kỹ xem kẻ nào đang ngồi bên trong.",
        "Thì ra là mày hả Tom, chính mày đã dẫn đám cảnh sát tới úp sọt gia đình tao.",
        "Tao đã nhớ kỹ cái mặt mày rồi, cả mày lẫn băng của Micdo sẽ phải trả giá đắt.",
        "Đẩy hắn đi tiếp về phía trước, đừng để hắn đứng lại la hét trước cửa xe chỉ huy.",
        "Chết tiệt thật, ánh mắt của Ny Tran vừa rồi chứng tỏ hắn đã kết tội sang cả nhóm Toto.",
    ],
    47: [
        "Kiểm tra toàn bộ dãy mã số trên các thùng đầu đĩa và màn hình trong kho này ngay.",
        "Tập hóa đơn đóng dấu đỏ trên bàn kia là chứng từ nhập khẩu hải quan chính ngạch.",
        "Đối chiếu từng tờ một rồi, tất cả lô hàng ở đây đều có giấy tờ hợp pháp đầy đủ.",
        "Không có bất kỳ một món hàng nào trùng khớp với số seri của các vụ cướp trên xa lộ.",
        "Chúng ta vồ hụt hoàn toàn rồi, kho hàng của Ny Tran hoàn toàn sạch sẽ về mặt pháp lý.",
        "Ra sân báo ngay cho Kinan biết trước khi vụ bắt giữ này biến thành rắc rối pháp lý.",
    ],
    48: [
        "Toàn bộ hàng trong kho đều có hóa đơn hải quan hợp pháp, không có tang vật vụ cướp nào cả.",
        "Cái gì cơ, chúng ta huy động cả đội đặc nhiệm lúc rạng sáng chỉ để vồ vào chỗ trống sao.",
        "Cậu làm ăn kiểu gì vậy Tom, tin tình báo của cậu suýt làm hỏng uy tín của cả đơn vị.",
        "Cậu đã để tình cảm riêng tư làm mờ mắt và cố tình hướng mũi dùi sang chỗ khác đúng không.",
        "Thủ phạm thực sự của các vụ cướp xe tải chỉ có thể là Micdo Toto và đồng bọn của hắn.",
        "Đây là cơ hội cuối cùng, nếu cậu không mang về bằng chứng thật thì tôi sẽ tự tay bắt hết.",
    ],
    49: [
        "Tháo khóa tay cho Ny Tran và người của hắn ngay, thu quân rút khỏi dinh thự này.",
        "Nhìn bộ mặt bẽ bàng của mấy người kìa, nhớ kỹ ngày hôm nay các người đã làm nhục cha tôi.",
        "Món nợ làm nhục gia đình tao sáng nay chắc chắn tao sẽ đòi lại gấp mười lần.",
        "Chuẩn bị xe cộ và người ngợm đi Cela, tới đại hội đua xe ngoài sa mạc tìm tụi nó.",
        "Ny Tran đang đinh ninh chính Micdo đã gài bẫy báo cảnh sát tới phá nát nhà hắn.",
        "Phải赶 về báo ngay cho Micdo đề phòng trước khi Ny Tran nổ ra cuộc trả thù tại giải đua.",
    ],
    50: [
        "Nắng sa mạc Mojave nóng như đổ lửa mà hàng ngàn chiếc xe đã kéo về kín cả đường băng.",
        "Chiếc xe trắng này là kỷ vật cha để lại, hôm nay tôi đã chỉnh máy đạt phong độ cao nhất.",
        "Đừng có hồi hộp quá nha Seja, chạy đúng nhịp số như lúc tập ở xưởng là thắng chắc.",
        "Nước mát của mọi người đây, nhớ giữ sức vì chiều nay còn nhiều lượt chạy căng thẳng lắm.",
        "Tôi vẫn thấy bất an lắm, đám người của Ny Tran vừa kéo cả đoàn xe tiến vào cổng phụ kìa.",
        "Cứ giữ bình tĩnh ở khu lán trại, ở chốn đông người thế này hắn chưa dám làm càn đâu.",
    ],
    51: [
        "Chào thiên tài toán học của đội Toto, chiếc xe trắng nhìn cũng sạch sẽ bóng bẩy quá nhỉ.",
        "Tôi tới đây để thi đấu công bằng trên đường băng, không muốn kiếm chuyện cãi vã với anh.",
        "Thi đấu công bằng mà chỉ chạy lấy tiếng vỗ tay thôi thì nhạt nhẽo quá phải không nhóc.",
        "Mày có dám lấy giấy tờ sở hữu chiếc xe trắng đó ra đấu với chiếc xe đen của tao không.",
        "Đừng nghe lời khích tướng của hắn Seja, chiếc xe của hắn nhìn bên ngoài vậy chứ ẩn bài đó.",
        "Một thiên tài tính toán mọi thông số mà lại sợ không dám đặt cược vào con xe của mình sao.",
    ],
    52: [
        "Mồ hôi tay ra nhiều quá, nhưng biểu đồ máy tính báo tỷ lệ thắng của mình tới sáu mươi bốn phần trăm.",
        "Với trọng lượng nhẹ hơn và hộp số chỉnh ngắn, chiếc xe trắng sẽ vọt lên ngay từ khúc đầu.",
        "Tôi đồng ý nhận kèo cược này, giấy tờ hợp pháp của chiếc xe trắng tôi nộp cho trọng tài đây.",
        "Khoan đã Seja, sao cậu lại tự ý đem giấy tờ xe ra cược với Ny Tran mà không hỏi ý anh em.",
        "Em đã tính kỹ từng con số rồi, em muốn thắng chiếc xe của hắn để mang vinh quang về cho đội.",
        "Lỡ nộp giấy tờ vô tay trọng tài rồi, giờ chỉ còn cách tập trung hết sức mà đạp ga thôi.",
    ],
    53: [
        "Tiếng còi xuất phát vang lên rồi, chiếc xe trắng của Seja vọt lên dẫn trước nửa thân xe.",
        "Giai đoạn đầu hoàn toàn đúng như biểu đồ tính toán, giữ nguyên vòng tua sang số ba đi.",
        "Mày tưởng chỉ có mình mày biết tính toán thông số kỹ thuật trên đường đua thôi sao nhóc.",
        "Dưới gầm ghế chiếc xe đen của hắn giấu nguyên hệ thống bình khí tăng tốc kép cỡ lớn kìa.",
        "Chiếc xe đen lao vút lên như tên bắn ở năm chục mét cuối, vượt qua vạch đích mất rồi.",
        "Thua thật rồi, hắn giấu bài kỹ quá khiến toàn bộ phép tính của Seja đổ sông đổ bể hết.",
    ],
    54: [
        "Không thể nào như vậy được, công thức toán học mình đã kiểm tra kỹ làm sao sai được.",
        "Chiếc xe kỷ vật của cha giờ rơi vào tay Ny Tran thì mình biết ăn nói làm sao với anh cả.",
        "Sao chiếc xe trắng không giảm tốc ở cuối đường băng mà lại rồ ga phóng thẳng ra cổng sau vậy.",
        "Thằng bé hoảng loạn quá nên đạp ga chạy trốn thẳng vào đường sa mạc để giữ xe rồi.",
        "Hành động bỏ chạy kiểu đó chẳng khác nào châm lửa vào thùng thuốc súng của Ny Tran.",
        "Quay về lán trại tập hợp anh em ngay, Ny Tran chắc chắn đang kéo người qua đòi nợ đó.",
    ],
    55: [
        "Bước ra đây ngay Micdo, thằng nhóc người của mày vừa thua cược đã lái xe bỏ trốn rồi.",
        "Đưa ngay chiếc xe trắng hoặc giao cổ thằng nhóc quỵt nợ đó ra đây cho tao xử lý.",
        "Thằng bé chỉ nhất thời hoảng sợ thôi, tao sẽ tự đi tìm nó và mang xe tới giao cho mày sau.",
        "Đứng lùi hết ra sau lưng tao, không ai được phép manh động giữa bãi đua đông người này.",
        "Mày nghĩ chỉ một câu hẹn trả sau là xóa được cái thói quỵt nợ trước hàng ngàn con mắt sao.",
        "Giữ khoảng cách đi Cela, nếu tụi nó dám động thủ ở đây thì tôi sẽ can thiệp ngay lập tức.",
    ],
    56: [
        "Đêm nay ở giải đấu này tao không muốn có bất kỳ cuộc ẩu đả đổ máu nào xảy ra hết.",
        "Không có chuyện để sau này đâu, chính mày đã phái cảnh sát đột kích nhà tao sáng hôm qua.",
        "Mày làm nhục cha tao trước mặt bàn dân thiên hạ rồi giờ đàn em mày lại dám quỵt nợ tao.",
        "Tao đã nói chuyện cảnh sát khám nhà mày hoàn toàn không phải do người của tao báo tin.",
        "Đừng có chối quanh co nữa, món nợ danh dự này tao với mày sẽ giải quyết dứt điểm.",
        "Khi hắn đã nói tới mức đó thì chắc chắn hắn sẽ truy sát Seja và cả gia đình mình tới cùng.",
    ],
    57: [
        "Kiểm tra lại toàn bộ dây cáp và bộ đàm đi, đêm nay chúng ta phải làm nốt phi vụ cuối.",
        "Cần có một khoản tiền lớn ngay trong đêm nay để chuộc mạng cho Seja và đưa cả nhóm đi xa.",
        "Nhưng các tài xế xe đầu kéo trên tuyến đường sa mạc dạo này cảnh giác cao độ lắm anh cả.",
        "Không còn lựa chọn nào khác đâu, xong chuyến hàng cuối cùng này cả đội sẽ giải nghệ luôn.",
        "Khởi động ba chiếc xe đen thật êm, đừng để Ami trong nhà nghe thấy tiếng máy mà chạy ra.",
        "Xuất phát ra đường cao tốc tám mươi sáu ngay, canh đúng chuyến đầu kéo cuối ngày mà đánh.",
    ],
    58: [
        "Dừng lại đi Ami, em tuyệt đối không được lái xe đuổi theo anh trai em trong đêm nay.",
        "Tránh đường cho em đi, Seja đang gặp nạn còn anh trai em thì đang cần người hỗ trợ.",
        "Đêm nay các tài xế đầu kéo như Verni đều đã tự trang bị vũ khí để bắn trả tụi cướp rồi.",
        "Sao anh lại biết rõ tên tài xế xe tải và chuyện họ tự vũ trang, rốt cuộc anh là ai vậy.",
        "Anh là cảnh sát chìm thuộc LAPD, nhưng anh thề tình cảm anh dành cho em là hoàn toàn thật lòng.",
        "Giờ không phải lúc khóc đâu, lên chiếc xe cam đi với anh ngay nếu muốn cứu mạng anh trai em.",
    ],
    59: [
        "Chiếc đầu kéo của Verni đang chạy trước mặt kìa, giữ đều ga để Cevin chuẩn bị phóng cáp.",
        "Mũi cáp găm trúng khung cabin rồi, tao đu dây qua cửa phụ khống chế tay lái như mọi lần đây.",
        "Lũ cướp đường tụi mày lại dám mò tới nữa hả, lần này tao đã chuẩn bị sẵn đồ đón tụi mày rồi.",
        "Verni hạ kính chống trả quyết liệt quá, Cevin bị trúng đòn nặng ngay vùng bụng rồi kìa.",
        "Sợi cáp thép quấn chặt vô cổ tay Cevin làm nó bị treo lơ lửng bên hông đầu kéo mất rồi.",
        "Cina mau đưa xe áp sát vô giữa để cắt sợi cáp cứu Cevin trước khi nó bị kéo lê xuống đường.",
    ],
    60: [
        "Em đang ép xe vô sát đầu kéo đây nhưng lão tài xế cứ đánh lái lắc thùng xe dữ quá.",
        "Bánh trước bên trái xe của Cina bị ép nổ lốp rồi, chiếc xe đang trượt văng ra lề cát.",
        "Cina giữ chặt vô lăng đi, chiếc xe của cô ấy lật nhào qua dải cát ven đường mất rồi.",
        "Đội hình tan vỡ hết rồi, một mình xe tao phía trước không thể nào lùi lại cắt dây cáp kịp.",
        "Nhìn qua gương hậu kìa, chiếc xe màu cam của Tom đang xé gió lao vọt lên từ phía sau.",
        "Giữ vững tay lái nha Ami, anh sẽ đưa mũi xe áp sát ngay dưới chỗ Cevin đang bị treo.",
    ],
    61: [
        "Qua đây cầm chắc vô lăng giữ thẳng tay lái cho anh, tuyệt đối không được giảm tốc độ.",
        "Em sợ lắm Tom ơi, hai chiếc xe đang chạy sát rạt nhau ở tốc độ hơn một trăm cây số.",
        "Em làm được mà Ami, giữ thẳng mũi xe thêm năm giây nữa để anh nhoài người ra cắt cáp.",
        "Nắm được đai áo của Cevin rồi, lưỡi dao đã cắt đứt sợi dây cáp thép căng cứng kia rồi.",
        "Đỡ phụ anh kéo Cevin vô băng ghế sau đi, đạp phanh tách khỏi hông chiếc đầu kéo ngay.",
        "Tấp xe vô lề đường cát phía trước mau lên, vết thương ở bụng cậu ấy đang mất sức nhanh lắm.",
    ],
    62: [
        "Đặt Cevin nằm phẳng xuống đây, dùng khăn sạch ép thật chặt vào vết thương bên hông cậu ấy.",
        "Giữa đường cao tốc sa mạc thế này xe cấp cứu thông thường không thể nào tới kịp trong mười phút.",
        "Đây là Sĩ quan đặc nhiệm Tom mã số bốn ba bảy, yêu cầu trực thăng y tế khẩn cấp tại xa lộ tám mươi sáu.",
        "Có nạn nhân bị thương nặng vùng bụng đang nguy kịch, yêu cầu điều trực thăng tới tọa độ này ngay.",
        "Giọng nói và mã số cảnh sát đó là sao, mày vừa tự xưng là sĩ quan đặc nhiệm LAPD hả.",
        "Xin anh hãy bình tĩnh nghe tôi nói đã, lúc này tính mạng của Cevin là quan trọng hơn tất cả.",
    ],
    63: [
        "Sĩ quan cảnh sát Tom sao, vậy là suốt thời gian qua mày đã đóng kịch lừa dối cả gia đình tao.",
        "Mày ngồi ăn cơm ở sân nhà tao, mày nhìn vào mắt em gái tao trong khi mày là một tên cớm chìm.",
        "Tôi buộc phải gọi trực thăng bằng mã cảnh sát vì nếu chậm năm phút nữa Cevin sẽ không qua khỏi.",
        "Tiếng cánh quạt trực thăng y tế đã tới trên đầu rồi kìa, mau đưa Cevin lên khoang cấp cứu đi.",
        "Từ giây phút này giữa tao với mày không còn bất kỳ tình nghĩa anh em nào nữa hết, tránh xa em gái tao ra.",
        "Anh ấy bế Cevin lên trực thăng cùng Cina rồi, chúng ta cũng phải lập tức quay về nhà giữ an toàn cho Seja.",
    ],
    64: [
        "Chiếc xe trắng của Seja vừa chạy về đỗ trước hiên nhà kìa, thằng bé trông tiều tụy quá.",
        "Anh cả ơi cho em xin lỗi, em vì quá hoảng sợ nên đã làm liên lụy tới danh dự của cả nhóm.",
        "Cậu trở về bình an là tốt rồi, chuyện chiếc xe để anh cả tính, nhưng coi chừng hai chiếc mô tô đằng kia.",
        "Đám người của Ny Tran và Cela đang phóng mô tô lao thẳng tới hiên nhà với tốc độ điên cuồng.",
        "Nằm rạp hết xuống bãi cỏ đi, tụi nó vừa lướt qua tấn công thẳng vào chỗ Seja đang đứng.",
        "Không thể nào như vậy được, Seja ơi mở mắt ra nhìn anh đi, đừng bỏ tụi anh mà đi như vậy.",
    ],
    65: [
        "Thằng em hiền lành nhất trong nhà đã ngã xuống ngay trên thảm cỏ trước mắt chúng ta rồi.",
        "Anh cả đang chạy thẳng vô xưởng sau nhà với đôi mắt đỏ ngầu, anh ấy định làm chuyện điên rồ rồi.",
        "Tấm bạt phủ chiếc xe cơ bắp năm một chín bảy mươi của cha đã bị anh ấy giật tung ra rồi.",
        "Tiếng khối động cơ siêu nạp chín trăm mã lực đang gầm rú làm rung chuyển cả nền bê tông.",
        "Dừng lại đi Micdo, đừng để cơn giận làm mù quáng, hãy để cảnh sát giải quyết bọn Ny Tran.",
        "Anh ấy phóng chiếc xe đen lao vút ra đường rồi, tôi phải lái chiếc xe cam đuổi theo hỗ trợ ngay.",
    ],
    66: [
        "Hai chiếc mô tô của Ny Tran đang tháo chạy qua các con phố dốc đứng phía trên đồi.",
        "Chiếc xe cơ bắp của Micdo lao đi như một con thú dữ, khoảng cách đang thu hẹp từng mét một.",
        "Tụi nó đuổi sát tới sau lưng rồi kìa Ny Tran, tách ra hai làn đường dốc để cắt đuôi ngay.",
        "Micdo đánh lái ép thẳng mũi xe sắt khổng lồ vào đuôi chiếc mô tô của Cela ở tốc độ cao.",
        "Chiếc mô tô của Cela văng vào vách tường bê tông rồi, hắn bị gãy chân nằm rên rỉ bên lề đường.",
        "Giờ chỉ còn một mình Ny Tran phía trước, tôi phải vọt chiếc xe cam lên khóa góc tấn công của hắn.",
    ],
    67: [
        "Ny Tran đang ngoái lại định dùng vũ khí nhắm thẳng vào kính chắn gió chiếc xe của Micdo.",
        "Đạp lút ga đưa chiếc xe cam vọt lên song song bên phải để chắn tầm nhìn và ép tay lái hắn.",
        "Hết đường chạy trốn rồi Ny Tran, buông vũ khí xuống và tấp xe vào lề đường ngay lập tức.",
        "Cú va quệt làm tay lái chiếc mô tô của Ny Tran chao đảo mất kiểm soát trên con dốc đứng.",
        "Chiếc mô tô lao thẳng xuống lòng kênh thoát nước bê tông bên dưới và bốc cháy dữ dội rồi.",
        "Băng Light Saigon đã đền tội nhưng chiếc xe đen của Micdo vẫn tiếp tục phóng thẳng ra vùng ngoại ô.",
    ],
    68: [
        "Hai chiếc xe cùng dừng lại song song trước vạch chắn đường ray xe lửa ngoại ô vắng lặng.",
        "Mày biết không Tom, tao từng nói cả cuộc đời tao chỉ sống trọn vẹn vì một phần tư dặm này.",
        "Trong mười giây ngắn ngủi đó không có quá khứ, không có tương lai và không có bất kỳ luật lệ nào.",
        "Tôi biết điều đó Micdo, từ ngày bước chân vào xưởng xe của anh tôi đã hiểu rất rõ điều đó.",
        "Chuông báo hiệu đường sắt đang reo vang và đoàn tàu chở hàng khổng lồ đang lao tới rất gần rồi.",
        "Nhấn ga lên đi Sĩ quan, chúng ta cùng chạy một cuộc đua một phần tư dặm cuối cùng chứ.",
    ],
    69: [
        "Đèn đỏ đường ray chớp dồn dập rồi, gạt cần số và đạp lút bàn đạp ga ngay bây giờ.",
        "Sức mạnh chín trăm mã lực nhấc bổng hai bánh trước chiếc xe đen lên khỏi mặt đường nhựa.",
        "Hai chiếc xe lao vút đi song song như hai mũi tên hướng thẳng về phía đường ray trước mũi tàu.",
        "Chỉ trong một tích tắc nghẹt thở, đuôi hai chiếc xe vừa lướt qua thì đoàn tàu lao rầm qua phía sau.",
        "Coi chừng phía trước kìa Micdo, có một chiếc xe tải chở hàng vừa từ trong hẻm ngang lao ra chắn đường.",
        "Chiếc xe đen không kịp phanh đã đâm sầm vào đuôi xe tải, bay lộn nhào ba vòng rồi lật ngửa bốc khói.",
    ],
    70: [
        "Phanh gấp chiếc xe cam lại ngay, lao qua phá cửa cabin kéo anh ấy ra trước khi lửa bén vào.",
        "Bám vào vai tôi đi Micdo, ráng bước ra khỏi đống sắt vụn này trước khi bình xăng phát nổ.",
        "Tiếng còi hú của đoàn xe cảnh sát đang kéo tới đầu đường rồi, mày thắng rồi đó, còng tay tao đi.",
        "Tôi từng hứa sẽ mang về trả nợ cho anh một con xe mười giây, giờ chiếc xe cam này là của anh.",
        "Cầm lấy chìa khóa rồi leo lên chiếc xe cam phóng đi ngay đi, đừng ngoái đầu nhìn lại nữa.",
        "Chiếc xe cam đã khuất dần vào chân trời sa mạc, giờ chỉ còn một mình tôi đứng lại đối diện với Nese.",
    ],
}


# Remap and optimize the 70-scene master list into the tight 40-minute (40 scenes × 6 clips = 240 clips) edition
SELECTED_OLD_SCENES = [
    # Tập 1 (Cảnh 01–10): Vụ cướp xa lộ đêm, tiệm độ xe, quán Toto & Biệt thự tác chiến chìm
    1, 2, 4, 5, 7, 8, 10, 12, 13, 15,
    # Tập 2 (Cảnh 11–20): Cược giấy tờ xe, Đua đêm Nam L.A., Giải cứu Micdo, Băng Light Saigon đốt xe & Tiệc BBQ kết nạp
    20, 21, 24, 25, 26, 27, 28, 29, 34, 37,
    # Tập 3 (Cảnh 21–30): Tình cảm của Ami, Độ siêu xe Supra 10 giây, Quái thú Charger 1970, Đột kích nhà Ny Tran & Đại hội Race Wars
    38, 40, 41, 42, 44, 46, 47, 50, 53, 56,
    # Tập 4 (Cảnh 31–40): Thú nhận thân phận với Ami, Phi vụ cao tốc sa mạc, Cứu Cevin, Bi kịch Seja, Truy sát Ny Tran & 10 Giây Tự Do
    58, 59, 60, 61, 62, 64, 65, 67, 69, 70,
]

_SAFE_VI_DIALOGUE_FIXES = [
    ("bắn cáp", "phóng cáp"),
    ("bắn mũi cáp thép", "phóng mũi cáp thép"),
    ("bắn trúng điểm neo", "phóng trúng điểm neo"),
    ("mà bắn", "mà móc cáp"),
    ("như tên bắn", "nhanh như chớp"),
    ("trang bị vũ khí để bắn trả tụi cướp", "chuẩn bị sẵn sàng để chặn nhóm lấy hàng"),
    ("trang bị vũ khí để bắn trả", "chuẩn bị sẵn sàng để chống trả"),
    ("tự trang bị vũ khí", "tự chuẩn bị đồ phòng vệ"),
    ("tự vũ trang", "tự phòng vệ"),
    ("có vũ trang", "có chuẩn bị phòng vệ"),
    ("dùng vũ khí nhắm thẳng", "áp sát gây nguy hiểm"),
    ("buông vũ khí xuống", "dừng lại ngay"),
    ("thùng thuốc súng", "cơn giận dữ"),
    ("vụ cướp đêm qua", "phi vụ đêm qua"),
    ("vụ cướp container", "phi vụ lấy hàng container"),
    ("vụ cướp mở màn", "phi vụ mở màn"),
    ("xe đầu kéo bị cướp", "xe đầu kéo bị chặn lấy hàng"),
    ("vụ cướp trên xa lộ", "vụ mất hàng trên xa lộ"),
    ("các vụ cướp xe tải", "các vụ mất hàng xe tải"),
    ("vụ cướp xe tải", "phi vụ chặn xe tải"),
    ("bốn vụ cướp đầu kéo", "bốn vụ chặn xe đầu kéo"),
    ("tang vật vụ cướp", "tang vật vụ mất hàng"),
    ("số seri bị cướp", "số seri bị mất"),
    ("lô hàng cướp được", "lô hàng lấy được"),
    ("vụ cướp của Verni", "vụ mất hàng của Verni"),
    ("vụ cướp cuối", "phi vụ cuối"),
    ("băng cướp xe tải đêm", "nhóm chặn xe tải đêm"),
    ("băng cướp", "nhóm chặn xe"),
    ("phương thức đánh cướp", "phương thức lấy hàng"),
    ("chống trả tụi cướp", "chống trả nhóm chặn xe"),
    ("Nếu tụi cướp đụng độ", "Nếu nhóm chặn xe đụng độ"),
    ("Lũ cướp đường", "Đám người"),
    ("cướp đường trắng trợn", "chặn xe trắng trợn"),
    ("Cuộc Âu Đả Ngoài Hiên Quán", "Màn Đối Đầu Võ Thuật Ngoài Hiên Quán"),
    ("tung cú đấm trước nhưng Tom né được và phản đòn; cả hai vật lộn làm gãy bàn gỗ ngoài hiên giữa tiếng la hét của Ami", "lao vào so chiêu võ thuật nhưng Tom né đòn chuẩn nhịp và khóa thế; cả hai làm xê dịch bàn gỗ ngoài hiên khi Ami bước ra ngăn"),
    ("màn ẩu đả tay đôi quyết liệt", "màn đối đầu võ thuật tốc độ cao"),
    ("vung tay đấm thẳng nhưng Tom lách người phản đòn vào hông hắn", "ra chiêu áp sát nhưng Tom lách người khóa cổ tay chuẩn nhịp"),
    ("dám đánh nhau ngay tại quán", "dám đối đầu võ thuật ngay tại quán"),
    ("trận đánh nhau ngoài hiên quán", "màn đối đầu ngoài hiên quán"),
    ("đừng đánh nhau làm sập bàn", "đừng xô xát làm đổ bàn"),
    ("bẻ gãy răng mày", "dạy cho mày bài học"),
    ("làm đổ máu ở sân nhà tao", "gây náo loạn ở sân nhà tao"),
    ("Vết bầm trên mặt", "Vết bụi trên mặt"),
    ("vết bầm trên mặt", "vệt bụi trên mặt"),
    ("vết bầm trên gò má", "vệt bụi trên gò má"),
    ("nhìn vết thương của Sĩ quan Tom", "nhìn vệt bụi trên má Sĩ quan Tom"),
    ("Đường Dao Trên Nắp Capô", "Vệt Xước Trên Nắp Capô"),
    ("dùng mũi dao cào", "cào"),
    ("miết mũi dao", "cào"),
    ("Đường dao cào", "Vệt xước"),
    ("dùng dao cắt", "dùng kìm thép cắt"),
    ("lưỡi dao đã cắt", "kìm thép đã cắt"),
    ("Chiếc Eclipse Chìm Trong Biển Lửa", "Chiếc Eclipse Bốc Khói Mù Mịt"),
    ("phá thủng bình nhiên liệu khiến chiếc Eclipse bốc cháy dữ dội", "xả van áp suất khiến chiếc Eclipse bốc khói mù mịt"),
    ("bùng cháy dữ dội", "bốc khói mù mịt"),
    ("rực lửa", "đầy khói"),
    ("Bình nhiên liệu phía sau bén lửa rồi", "Hệ thống áp suất phía sau xả khói đặc rồi"),
    ("bùng cháy thành biển lửa rồi", "bốc khói mù mịt hỏng nặng rồi"),
    ("đống sắt cháy đen", "khung xe hư hỏng"),
    ("khung sắt cháy đen", "khung xe hư hỏng"),
    ("đốt cháy rụi", "làm hỏng nặng"),
    ("cháy rụi", "hỏng nặng"),
    ("nổ máy nhập làn", "khởi động máy nhập làn"),
    ("Xác Chiếc Toyota Supra", "Khung Chiếc Toyota Supra"),
    ("xác chiếc Charger", "khung chiếc Charger"),
    ("chuẩn xác", "chuẩn nhịp"),
    ("làm nổ lốp trước", "làm xẹp lốp trước"),
    ("bị nổ lốp trước", "bị xẹp lốp trước"),
    ("bị ép nổ lốp", "bị ép xẹp lốp"),
    ("lật nhào qua dải cát", "trượt dài qua dải cát"),
    ("nổ tung", "hư hỏng nặng"),
    ("đâm sầm vào xe tải", "va chạm vào xe tải"),
    ("giận sôi máu", "giận dữ lắm"),
    ("ẩu đả đổ máu", "xô xát căng thẳng"),
    ("bằng máu", "tới cùng"),
    ("lo muốn chết", "lo lắng vô cùng"),
    ("sống chết có nhau", "sướng khổ có nhau"),
    ("Chết tiệt thật", "Gay go thật"),
    ("lột xác hoàn toàn", "khác hẳn hoàn toàn"),
    ("khiến Cevin bị thương nặng và treo lơ lửng", "khiến Cevin mất thăng bằng và treo lơ lửng"),
    ("khiến Cevin trúng đòn nặng vào vùng bụng, mắc kẹt lơ lửng", "khiến Cevin mất đà trượt xuống bậc cửa, mắc kẹt lơ lửng"),
    ("Cevin bị trúng đòn nặng ngay vùng bụng rồi kìa", "Cevin bị mất thăng bằng trượt khỏi bậc cửa rồi kìa"),
    ("vết thương ở bụng cậu ấy đang mất sức nhanh lắm", "cậu ấy đang kiệt sức sau cú treo người trên cáp"),
    ("dùng khăn sạch ép thật chặt vào vết thương bên hông cậu ấy", "dùng khăn mát giữ ổn định phần dây đai bên hông cậu ấy"),
    ("Có nạn nhân bị thương nặng vùng bụng đang nguy kịch", "Có thành viên kiệt sức sau sự cố dây cáp tốc độ cao"),
    ("giữ chặt vết thương cho Cevin đang thoi thóp", "chăm sóc cho Cevin đang kiệt sức"),
    ("Hai người có bị thương ở đâu không", "Hai người có bị xây xát ở đâu không"),
    ("kéo Micdo bị thương khỏi", "đỡ Micdo bước ra khỏi"),
    ("truy sát", "truy đuổi"),
    ("lao qua phục kích khiến Seja gục ngã", "lao qua ép sát khiến Seja mất thăng bằng ngã xuống"),
    ("lao vọt qua tấn công khiến Seja ngã gục trong vòng tay tuyệt vọng của Micdo", "lao vọt qua ép sát khiến Seja mất đà ngã xuống bãi cỏ trước sự lo lắng của Micdo"),
    ("lướt qua tấn công thẳng vào chỗ Seja đang đứng", "lướt qua ép sát ngay chỗ Seja đang đứng"),
    ("Cái chết của Seja", "Sự cố của Seja"),
    ("vì mất Seja", "vì Seja gặp nạn"),
    ("húc văng đuôi xe của Cela Nguyen ở tốc độ 120 km/h khiến hắn ngã gục bên vách tường", "ép sát làn đường của Cela Nguyen ở tốc độ 120 km/h khiến hắn mất lái dừng bên vách tường"),
    ("văng vào vách tường bê tông bất tỉnh", "trượt vào lề đường dừng lại"),
    ("Hạ gục Cela Nguyen", "Vượt qua Cela Nguyen"),
    ("văng vào vách tường bê tông rồi, hắn bị gãy chân nằm rên rỉ bên lề đường", "trượt vào lề đường rồi, hắn đã mất đà dừng lại bên vách tường"),
    ("khóa góc tấn công", "khóa góc di chuyển"),
    ("Ny Tran Đền Tội Dưới Kênh Thoát Nước", "Ny Tran Mất Lái Dưới Kênh Thoát Nước"),
    ("định tấn công Micdo", "định ép xe Micdo"),
    ("bốc cháy dữ dội rồi", "trượt dài dừng lại rồi"),
    ("lao xuống kênh thoát nước bốc cháy", "trượt xuống kênh thoát nước dừng lại"),
    ("đã đền tội", "đã dừng bước"),
    ("Cắt Đầu Tàu Hỏa & Cú Lật Kinh Hoàng", "Cắt Đầu Tàu Hỏa & Cú Xoay Xe Nghẹt Thở"),
    ("lộn nhào ba vòng", "xoay vòng dừng lại bên lề"),
    ("bay lộn nhào và lật ngửa bốc khói", "xoay vòng và dừng lại bốc khói trắng"),
    ("đâm sầm vào đuôi xe tải, bay lộn nhào ba vòng rồi lật ngửa bốc khói", "va quệt vào đuôi xe tải, xoay vòng rồi dừng lại bên lề đường"),
    ("trước khi lửa bén vào", "trước khi khói tràn vào"),
    ("đống sắt vụn này trước khi bình xăng phát nổ", "chiếc xe này trước khi đội tuần tra kéo tới"),
    ("còng tay tao đi", "bắt giữ tao đi"),
]

_OLD_SPEC_MAP = {spec[0]: spec for spec in SCENE_SPECS}
_NEW_SCENE_SPECS = []
_NEW_SCENE_DIALOGUES = {}
_OLD_TO_NEW = {}

for _new_idx, _old_num in enumerate(SELECTED_OLD_SCENES, start=1):
    _OLD_TO_NEW[_old_num] = _new_idx
    _orig = list(_OLD_SPEC_MAP[_old_num])
    _orig[0] = _new_idx
    # Clean Vietnamese descriptions and titles in scene spec
    for _fi in (1, 7, 8, 9, 10, 11):
        _txt = _orig[_fi]
        for _k, _v in _SAFE_VI_DIALOGUE_FIXES:
            _txt = _txt.replace(_k, _v)
        _txt = _txt.replace("Cảnh 24", "Cảnh 13").replace("Cảnh 26", "Cảnh 15").replace("Cảnh 68–69", "Cảnh 39")
        _orig[_fi] = _txt
    _NEW_SCENE_SPECS.append(tuple(_orig))

    _d_lines = []
    for _line in SCENE_DIALOGUES[_old_num]:
        _cl = _line
        for _k, _v in _SAFE_VI_DIALOGUE_FIXES:
            _cl = _cl.replace(_k, _v)
        _d_lines.append(_cl)
    _NEW_SCENE_DIALOGUES[_new_idx] = _d_lines

SCENE_SPECS = _NEW_SCENE_SPECS

# Feature-film canonical dialogue bank for all 40 scenes (240 clips):
# Written with authentic Southern Vietnamese street-racing & undercover crime-drama subtext,
# distinct character voices, and zero play-by-play camera narration.
SCENE_DIALOGUES = {
    1: [
        "Giờ này mà ba chiếc xe đen tắt pha bám đuôi là có biến rồi.",
        "Kèm sát hai bên hông thế này là tính ép đầu kéo tao vô lề đây.",
        "Ánh đèn gầm xanh lá dưới mặt nhựa, đúng là tụi quái xế đường đêm rồi.",
        "Tránh xa mũi xe tao ra, mười tám bánh sắt này không đạp phanh nhường đường đâu!",
        "Khóa kín cả làn vượt lẫn làn trong, tụi nó tính vây sống chuyến hàng này.",
        "Đổ hết con đèo này là tới trạm tuần tra, đừng hòng buộc tao giảm ga!",
    ],
    2: [
        "Giữ cứng một trăm ba mươi cây số, để tao khóa mũi cáp vô cabin nó!",
        "Ngàm từ tính ăn chặt khung thép rồi, giữ đều chân ga cho tao căng cáp!",
        "Thằng liều mạng kia, buông cái khung cửa xe tao ra trước khi mất mạng!",
        "Ngồi yên trên ghế lái đi chú Verni, ở tốc độ này đừng có làm liều!",
        "Tụi mày cướp trắng chuyến hàng tâm huyết của tao, luật pháp không dung thứ đâu!",
        "Buồng lái đầu kéo êm xuôi rồi, Cina đưa xe hai áp sát đuôi thùng đi!",
    ],
    3: [
        "Ghìm mũi xe cách cản sau nửa thước, để chị khóa bộ kích từ vô chốt.",
        "Gió hút sau thùng gắt lắm, giữ vững tay lái chờ nhịp trả số của chị.",
        "Xung điện mở khóa ăn khớp rồi, nhả nhẹ chân ga cho cửa thùng bung ra.",
        "Cửa thùng mở toang rồi anh em, nguyên kiện hàng điện tử còn niêm phong kín.",
        "Onle đôn chiếc thứ ba vô khe giữa ngay, chị dạt làn mở đường cho.",
        "Tao ghìm cứng đầu kéo ở làn giữa rồi, áp sát vô lấy hàng lẹ đi!",
    ],
    4: [
        "Mũi xe khóa sát bệ thùng rồi, chốt nắp trước đã mở, chuyền hàng xuống đi!",
        "Ưu tiên mấy kiện hàng lớn trước, giữ nhịp đều tay kẻo lệch trọng tâm xe.",
        "Mẻ hàng đêm nay đáng giá từng đồng, đủ nuôi sống cả xưởng suốt mùa tới!",
        "Còn đúng một dặm nữa là tới trạm gác, thu cáp rút khỏi xa lộ ngay!",
        "Khoang sau khóa kín rồi, tắt sạch đèn gầm xanh lá, lặn vào bóng đêm thôi.",
        "Nhánh đường phụ phía sau sạch bóng đèn tuần tra, tản ra ba ngả về xưởng!",
    ],
    5: [
        "Cổ nạp chiếc xanh đã chỉnh chuẩn từng ly, chỉ chờ đêm xuống thử lửa.",
        "Thêm một chuyến hàng tiền triệu bốc hơi trên xa lộ mười mà không để lại dấu vết.",
        "Giới tài xế đường dài đã cạn kiên nhẫn, sóng gió ngoài xa lộ sắp nổi lên.",
        "Ông canh giùm tôi đường dẫn nhiên liệu, đêm nay con xe này gánh kèo lớn.",
        "Mấy thùng phụ tùng tôi chất lên xe rồi, tranh thủ ghé quán Toto ăn trưa chút.",
        "Muốn bước vào thế giới của Micdo thì phải bắt đầu từ nơi hắn trân trọng nhất.",
    ],
    6: [
        "Cho anh phần bánh mì cá ngừ cắt vỏ với ly đá lạnh như cũ nghen.",
        "Nói thiệt nghen, cá ngừ quán này dở ẹc mà trưa nào anh cũng ráng nuốt được.",
        "Bánh mì cắt vỏ của anh đây, ăn đi rồi khai thiệt coi tính mưu đồ gì.",
        "Thú thật đi, đâu có ai ghé quán mỗi trưa chỉ vì món bánh dở tệ này?",
        "Bánh mì dở thiệt, nhưng đó là cái cớ duy nhất để mỗi ngày anh được gặp em.",
        "Tiếng pô xe ngoài hiên là đội của Cevin đó, anh ngồi yên đừng chấp họ nghen.",
    ],
    7: [
        "Tao đã cảnh cáo rồi mà chiếc bán tải đỏ vẫn dám đậu trước quán hả?",
        "Mình ghé uống nước thôi mà anh Cevin, giữ hòa khí trước tiệm của Ami đi.",
        "Hạ cái đầu nóng xuống đi Cevin, chuyện làm ăn tối qua chưa đủ mệt sao anh em.",
        "Mày điếc hả thằng thợ máy, tao đã bảo đừng bao giờ bén mảng tới gần Ami nữa!",
        "Bữa trưa của tôi xong rồi, tôi trả tiền đàng hoàng rồi quay về xưởng làm việc đây.",
        "Đứng lại đó, bước chân vào địa bàn nhà Toto đâu phải muốn đi là đi dễ vậy!",
    ],
    8: [
        "Tôi không muốn gây chuyện trước tiệm của Ami, anh thu tay lại khi còn kịp đi.",
        "Bày đặt điềm tĩnh hả, để coi một thợ máy học đâu ra thế thủ nhà nghề!",
        "Tách ra ngay hai cái đầu nóng này, anh Micdo mà thấy cảnh này là không yên đâu!",
        "Dừng tay lại ngay cho em Cevin, anh lấy quyền gì mà đuổi khách trước quán của em!",
        "Tiếng pô động cơ quay ngoài đầu phố kìa, anh cả Micdo vừa trờ xe tới nơi rồi!",
        "Em lùi vô trong hiên đi Ami, để anh tự đứng ra nói chuyện với anh hai.",
    ],
    9: [
        "Dừng tay lại hết, Cevin lùi về sau lưng tao ngay lập tức!",
        "Chuyện hiểu lầm ngoài hiên chỉ là va chạm cá nhân, không liên quan tới quán của anh.",
        "Ở cái đất này, gia đình là giới hạn cuối cùng mà không kẻ nào được bước qua.",
        "Anh hai đừng đổ lỗi cho anh Tom, chính Cevin kiếm chuyện chặn đường ảnh trước cửa quán!",
        "Cậu làm cho lão Ryh thì về xưởng mà làm, cấm bén mảng tới quán này lần nữa.",
        "Quán ăn là của anh, nhưng đường đua một phần tư dặm đêm nay không của riêng ai.",
    ],
    10: [
        "Vệt bụi trên má coi bộ đắt giá đấy, cậu tính phá vỏ bọc nằm vùng sao?",
        "Bốn chuyến hàng công nghệ bốc hơi trong hai tuần, hội tài xế sắp tự phòng vệ hết rồi.",
        "Bị đuổi khỏi quán ăn nhưng tôi đã chạm đúng vào tự tôn của tay đua số một.",
        "Muốn bước vào thế giới của Micdo, chỉ có cách thách đấu hắn ngay trên vạch đua.",
        "Chiếc xe xanh này là con bài cuối của đơn vị, đừng biến nó thành sắt vụn.",
        "Nhớ kỹ cậu là cảnh sát chìm nha Tom, đừng để cô gái đó làm lạc hướng.",
    ],
    11: [
        "Giấy tờ sở hữu hợp pháp của chiếc xe xanh nằm gọn trong phong bì này cho cậu.",
        "Tám mươi ngàn đô ngân sách nằm dưới nắp máy đó, mất xe là cậu mất hết.",
        "Ngoài đường đua đêm chỉ có tốc độ và bản lĩnh, không có chỗ cho sự do dự.",
        "Tôi đánh cược cả sự nghiệp vào mười giây đêm nay, tôi sẽ không trở về tay trắng.",
        "Đội tác chiến sẽ khóa chặt vòng ngoài, vào trong chảo lửa đó chỉ có một mình cậu.",
        "Khi mặt trời lặn xuống, Micdo Toto sẽ phải tự tay mở cửa đón tôi vào đội.",
    ],
    12: [
        "Hai bình khí tăng tốc đã nạp kịch kim, áp suất đường ống sẵn sàng cho đêm nay.",
        "Biểu đồ nhiệt ở tua máy tám ngàn vòng đang chạm ngưỡng giới hạn của cổ góp.",
        "Bấm bình khí thứ hai quá sớm là áp lực xé toạc cả gầm xe ngay lập tức.",
        "Nhưng đối đầu với con quái vật động cơ quay của Micdo thì không có đường lùi.",
        "Mọi con ốc đã khóa chặt, đêm nay chiếc xe này phải phá vỡ bức tường mười giây.",
        "Cảm ơn ông đã giữ kín chuyện ở xưởng, tới giờ tôi ra đường đua đêm rồi.",
    ],
    13: [
        "Tôi không mang tiền mặt, nhưng tôi đặt lên bàn giấy tờ gốc của chiếc xe này.",
        "Mười ngàn đô tiền đồ độ dưới nắp máy, tôi cược trọn con xe cho một lượt chạy.",
        "Thằng khách hồi trưa dâng không chiếc xe độ kìa anh cả, nhận kèo cho nó sáng mắt!",
        "Đem cả con xe ra cược một phần tư dặm, cậu liều mạng hay chưa biết sợ đây?",
        "Anh thắng thì cầm chìa khóa lái xe về, còn tôi thắng thì tôi muốn sự tôn trọng.",
        "Mọi lời nói dừng ở vạch trắng này, gầm máy lên đi các tay đua của đêm nay!",
    ],
    14: [
        "Bám sát đuôi chiếc xe đỏ cho tao, đêm nay không có khái niệm về nhì đâu!",
        "Hai gã hai bên rớt lại sau lưng rồi, giờ chỉ còn tôi với anh thôi Micdo!",
        "Chạy khá lắm nhóc, nhưng muốn vượt qua mũi xe tao thì bấy nhiêu đó chưa đủ.",
        "Tới lúc mở van bình khí đầu tiên rồi, cho tôi thấy sức mạnh thật sự đi!",
        "San bằng khoảng cách rồi, giữ cứng tay lái ở làn trái, vạch đích ngay trước mặt kìa!",
        "Đèn báo quá tải cổ góp mặc kệ nó, đêm nay không thắng là mất hết tất cả!",
    ],
    15: [
        "Còn trăm thước cuối, xả nốt bình khí thứ hai, ép cạn giới hạn con máy này luôn!",
        "Áp suất dội ngược làm bung chốt sàn phụ rồi, ghìm chặt vô lăng kẻo văng đuôi xe!",
        "Sang số ở tám ngàn vòng ngọt lịm, không ai qua mặt nổi anh cả trên đường này!",
        "Cậu làm tao bất ngờ đấy nhóc, hiếm có ai ép xe tao phải gồng hết số cuối.",
        "Nhưng nóng vội bấm khí sớm đã giết chết cổ góp của cậu, đưa chìa khóa xe đây.",
        "Xe thuộc về anh theo đúng luật chơi, nhưng nghe tiếng còi hú khóa bốn ngả đường kìa!",
    ],
    16: [
        "Đoàn xe tuần tra khóa vòng vây rồi, tản ra mau, mở đường rút cho anh cả!",
        "Đại lộ chính kẹt cứng rồi, giấu chiếc xe đỏ vào kho rồi tách ra rút bộ!",
        "Băng qua dãy hẻm kho bãi phía sau này, đừng để ánh đèn pha của tụi nó bắt kịp.",
        "Hai xe tuần tra vừa khóa cứng đầu hẻm trước mặt, tụi nó tính trước đường rút rồi.",
        "Lối sau lưng cũng bị đèn chớp bịt kín, đêm nay tụi nó quyết dồn mình vào rọ.",
        "Nếu để Micdo sa lưới cảnh sát đêm nay thì toàn bộ chuyên án coi như chấm dứt!",
    ],
    17: [
        "Nhảy lên ghế phụ ngay đi Micdo, trừ khi anh muốn ngồi sau song sắt đêm nay!",
        "Khoang máy đang bốc khói mà cậu còn dám quay đầu lao thẳng vào vòng vây sao?",
        "Giữ chặt tay vịn đi, con xe này còn đủ sức đưa hai ta lách khỏi hẻm!",
        "Lách qua khe thùng gỗ vừa khít từng phân, tay lái của cậu không tầm thường đâu!",
        "Vọt qua con dốc sắt này là bỏ lại toàn bộ đèn chớp tuần tra sau lưng!",
        "Cắt đuôi cảnh sát rồi, nhưng tiếng pô xe máy phía trước không phải chuyện lành đâu.",
    ],
    18: [
        "Mười chiếc mô tô đen khóa ngã tư, mình lọt vô đất của Ny Tran rồi.",
        "Băng Light Saigon không bao giờ tha cho người lạ vượt ranh giới lúc nửa đêm.",
        "Họ khóa chặt cả đầu xe lẫn hai bên sườn, không còn khe nào để đánh lái.",
        "Trả số không rồi tắt máy đi nhóc, để một mình tao ra nói chuyện với hắn.",
        "Bước xuống bãi đá ngay Micdo, đưa hai bàn tay ra ánh đèn cho tao nhìn rõ!",
        "Nửa đêm kéo xe bốc khói chạy xuyên qua bãi kho tụi tao là coi thường ai hả?",
    ],
    19: [
        "Đừng đụng vào cốp sau chiếc xe đó, hai bình khí bên trong đang căng áp suất!",
        "Van áp suất xì khói đặc rồi, lùi ngay ra sau lưng tao đi Tom!",
        "Bao nhiêu tâm huyết dưới nắp máy... giờ chỉ còn lại khung xe ngập trong khói trắng.",
        "Coi như chiếc xe hỏng đó là học phí đầu đời cho lính mới của mày nhớ luật!",
        "Nhớ lấy bài học đêm nay, còn bén mảng qua bãi kho này là không yên đâu!",
        "Đi thôi nhóc, xe mất thì dựng lại sau, giữ được mạng về nhà mới là chính.",
    ],
    20: [
        "Đêm nay nếu cậu ta không quay xe lại hẻm, giờ này tao đã nằm trong trại giam.",
        "Để đưa tao thoát vây, cậu ta đã phải mất trắng chiếc xe trước mặt Ny Tran.",
        "Từ đêm nay Tom là người nhà Toto, bất kỳ ai đụng tới nó là đụng tới tao!",
        "Một thằng lạ mặt tự dưng liều mạng vì anh cả, em vẫn chưa thể tin hắn được.",
        "Ngồi xuống đi Cevin, cậu ấy đã mất trắng con xe để đưa anh Micdo về nhà đó.",
        "Cảm ơn anh đã coi tôi như anh em, tôi sẽ không làm mọi người thất vọng.",
    ],
    21: [
        "Ngồi yên em lau sạch lớp muội than trên má cho, đi đua xe mà lấm lem hết.",
        "Khói bụi ngoài bãi đất thôi mà, thấy em cười với anh thế này là hết mệt rồi.",
        "Nghe tin cảnh sát vây đường đua, tim em cứ thắt lại vì sợ hai người gặp chuyện.",
        "Anh đã hứa rồi mà, chừng nào anh còn ở đây thì người nhà em sẽ bình an.",
        "Uống ly nước mát rồi ăn chút thịt nướng cho ấm bụng đi, anh vất vả quá rồi.",
        "Là người một nhà rồi đó, nhưng cậu vẫn còn nợ tao một con xe mười giây nghen!",
    ],
    22: [
        "Cậu nợ anh cả xe mười giây mà lại kéo cái khung sắt rỉ sét này về xưởng hả?",
        "Bộ vỏ móp méo cỡ này thì đẩy bộ qua vạch đích còn khó huống chi là đem đua.",
        "Đừng nhìn lớp sơn rỉ bên ngoài, mở nắp máy lên coi trái tim của nó bên dưới kìa.",
        "Khoan đã anh em, dưới lớp bụi này là nguyên khối động cơ tăng áp kép huyền thoại kìa!",
        "Chỉ cần hạ dàn hơi mới và nạp lại điện tử là cỗ máy này bay dưới mười giây!",
        "Vậy thì xắn tay áo lên thôi anh em, biến cái khung sắt này thành quái vật đường phố!",
    ],
    23: [
        "Khóa chặt con ốc cổ xả cuối cùng rồi, áp suất buồng đốt đạt mức hoàn hảo luôn.",
        "Khoác lớp sơn màu cam ánh kim này lên, không ai nhận ra cái khung rỉ sét hôm nào!",
        "Mấy anh em nghỉ tay ăn chút đồ nóng đi, thức trắng mấy đêm liền không biết mệt hả?",
        "Cùng mọi người đổ mồ hôi bên chiếc xe này, tôi mới hiểu thế nào là một gia đình.",
        "Ở xưởng này không ai giàu tiền bạc, nhưng đã là anh em thì sướng khổ cùng chia.",
        "Khi chiếc xe cam này lăn bánh ra sa mạc Mojave, cả đại hội đua xe sẽ phải ngước nhìn!",
    ],
    24: [
        "Đi theo tao vào góc sâu của xưởng, có thứ này tao chỉ mở cho người trong nhà.",
        "Chiếc xe cơ bắp đời một chín bảy mươi này là kỷ vật cha tao cùng tao dựng nên.",
        "Chín trăm mã lực dưới khối siêu nạp này mạnh tới mức tao vẫn chưa dám cầm lái.",
        "Một tay đua làm chủ mọi cung đường như anh, sao lại e dè trước xe của cha mình?",
        "Bởi trong mười giây trên đường một phần tư dặm đó, con người ta mới thực sự tự do.",
        "Tôi hiểu điều đó, có những lằn ranh một khi đã bước qua thì không thể quay đầu lại.",
    ],
    25: [
        "Tất cả các mũi tác chiến đã khóa chặt vòng vây quanh dinh thự ngay lúc rạng đông.",
        "Cổng sắt mở toang rồi, đội xung kích tràn vào sân và khóa ngay lối thông ra kho!",
        "Khống chế toàn bộ sổ sách và kiện hàng, không để bất kỳ kẻ nào kịp tiêu hủy chứng từ!",
        "Tôi giữ liên lạc trên xe chỉ huy, lộ mặt lúc này là mất sạch đường về nhà Toto.",
        "Đọc lệnh khám xét liên bang và tách riêng từng người trong dinh thự ra giữa khoảng sân đá!",
        "Mũi kiểm tra số hai theo sát tôi, mở niêm phong dãy kho điện tử phía sau ngay lập tức!",
    ],
    26: [
        "Giữ hai tên cầm đầu đứng cạnh xe chỉ huy, chờ kết quả đối chiếu hàng từ kho sau!",
        "Nhìn qua khe kính chiếc xe chỉ huy kìa Ny Tran, coi kẻ nào đang ngồi trốn bên trong!",
        "Thì ra là lính mới của Micdo, chính tụi mày đã dẫn cảnh sát tới phá gia đình tao!",
        "Nhớ kỹ ánh mắt tao hôm nay đi Tom, món nợ này cả băng Toto phải trả gấp mười!",
        "Áp giải hai tên đó về phía hiên đá ngay, không để chúng tiếp cận gần cửa xe chỉ huy!",
        "Gay go rồi trung sĩ, Ny Tran vừa nhìn thấy tôi và đổ hết mối thù lên đầu Micdo.",
    ],
    27: [
        "Quét toàn bộ mã số trên các kiện hàng điện tử này, tìm cho ra tang vật bị mất!",
        "Khoan đã Kinan, toàn bộ sổ cái trên bàn đều đóng dấu thông quan chính ngạch cảng biển.",
        "Đã rà soát từng tờ chứng từ, mọi kiện hàng ở đây đều nhập khẩu hợp pháp đầy đủ.",
        "Không có dù chỉ một con ốc trùng khớp với danh sách hàng bị chặn trên xa lộ mười.",
        "Chúng ta đánh úp nhầm mục tiêu rồi, tin tình báo của cậu đẩy cả đội vào ngõ cụt!",
        "Tháo còng cho Ny Tran ngay, vậy là nhóm chặn xe tải chỉ có thể là đội Micdo!",
    ],
    28: [
        "Cái nắng sa mạc Mojave thiêu đốt mặt nhựa, vậy mà cả ngàn chiến mã đã hội tụ về đây.",
        "Chiếc xe trắng này là kỷ vật của cha em, hôm nay nó sẽ tỏa sáng trên đường băng.",
        "Hít sâu một hơi đi Seja, cứ sang số đúng nhịp máy như lúc anh em mình thử ở xưởng.",
        "Anh Tom nhìn ra vạch đua kìa, Ny Tran vừa đưa chiếc xe đen áp sát bên Seja rồi!",
        "Máy tính báo tỷ lệ thắng sáu mươi bốn phần trăm, em đặt cược giấy tờ xe luôn rồi!",
        "Đừng mắc bẫy của Ny Tran nha Seja, dưới gầm chiếc xe đen đó giấu đồ độ khủng lắm!",
    ],
    29: [
        "Đề-pa chuẩn từng phần trăm giây, mũi chiếc xe trắng của mình vươn lên chiếm lợi thế trước rồi!",
        "Mọi thông số đều khớp với biểu đồ, giữ vững vòng tua số ba là nắm chắc phần thắng!",
        "Mày tưởng vài công thức trên máy tính đủ để qua mặt tao trên đường băng này sao nhóc?",
        "Tạm biệt kỷ vật của cha mày đi nhóc, hai bình khí ngầm dưới ghế tao mở van rồi!",
        "Không thể nào thua ở mấy mét cuối như vậy được, mình làm mất xe của cha rồi!",
        "Không thể giao chiếc xe này cho Ny Tran được, phải đạp ga chạy khỏi đường băng này thôi!",
    ],
    30: [
        "Bước ra đây ngay Micdo, thằng đàn em của mày vừa thua kèo đã ôm xe bỏ trốn rồi!",
        "Thằng bé chỉ hoảng loạn nhất thời, tự tay tao sẽ tìm nó rồi mang xe trả cho mày.",
        "Hôm qua mày gài cảnh sát làm nhục cha tao, nay đàn em mày lại dám quỵt nợ tao!",
        "Nghe cho rõ đây Ny Tran, gia đình Toto chưa bao giờ dùng tay cảnh sát hại ai.",
        "Khỏi cần giải thích nhiều lời, món nợ danh dự này tao sẽ thu hồi cả vốn lẫn lãi!",
        "Ny Tran không dừng lại ở chiếc xe đâu Micdo, hắn sẽ lùng tìm Seja tới cùng đấy.",
    ],
    31: [
        "Dừng lại đi Ami, đêm nay em tuyệt đối không được một mình lái xe ra cao tốc!",
        "Buông tay em ra đi Tom, Seja đang gặp nguy còn anh Micdo đang lao vào chỗ hiểm!",
        "Chuyến đầu kéo đêm nay là cái bẫy, tài xế Verni đã chuẩn bị sẵn sàng chống trả rồi!",
        "Sao anh biết rõ tên tài xế và cầm bộ đàm kia... rốt cuộc anh là ai hả Tom?",
        "Anh là cảnh sát chìm LAPD, nhưng tình cảm anh dành cho em và nhà mình là thật.",
        "Hận anh sau cũng được, giờ lên chiếc xe cam với anh ngay để cứu mạng anh hai!",
    ],
    32: [
        "Xong chuyến hàng cuối này cả đội sẽ giải nghệ, giữ cứng chân ga cho Cevin phóng cáp!",
        "Ngàm cáp khóa cứng khung cửa rồi anh cả, em đu dây qua chiếm buồng lái ngay đây!",
        "Tao đã đợi tụi mày suốt cả tuần nay rồi, đừng hòng bước chân vào buồng lái tao!",
        "Gã tài xế đã phục sẵn trong cabin, Cevin bị trượt khỏi bậc cửa treo trên cáp rồi!",
        "Khóa cáp siết chặt cổ tay em rồi anh cả ơi, đầu kéo đang lắc ép em xuống đường!",
        "Cina đôn xe hai lên khe giữa ngay, cắt đứt sợi cáp trước khi Cevin kiệt sức!",
    ],
    33: [
        "Em đang ép mũi xe vô khe cáp đây, nhưng lão tài xế đánh võng thùng hàng gắt quá!",
        "Cản sắt đầu kéo ép xẹp lốp trước rồi, xe em đang trượt văng ra dải cát ven đường!",
        "Giữ chặt vô lăng đi Cina, ghìm thẳng bánh lái cho xe trượt dừng lại ngoài lề cát!",
        "Xe Cina văng khỏi đội hình rồi, một mình tao ở đầu cáp không sao lùi lại kịp!",
        "Tiếng pô tăng áp kép sau lưng... chiếc xe cam của Tom đang xé gió lao lên kìa!",
        "Giữ vững tinh thần nha Ami, anh sẽ đưa chiếc xe cam áp sát ngay dưới sợi cáp!",
    ],
    34: [
        "Sang đây nắm chặt vô lăng giữ cứng tốc độ cho anh, tuyệt đối không được nhả chân ga!",
        "Bánh xe đầu kéo sát ngay cửa kính rồi Tom ơi, em đang gồng hết sức giữ thẳng lái!",
        "Tin ở anh thêm năm giây nữa thôi Ami, giữ nguyên làn để anh bấm đứt sợi cáp!",
        "Sợi cáp đứt lìa rồi, bám chặt vào vai tôi đi Cevin, tôi kéo cậu vô xe ngay!",
        "Đỡ Cevin nằm xuống ghế sau đi Ami, anh đạp phanh tách khỏi hông chiếc đầu kéo đây!",
        "Cậu ấy va đập mạnh làm kiệt sức nhanh quá, phải tấp vô lề gọi cứu viện ngay!",
    ],
    35: [
        "Đặt Cevin nằm phẳng xuống đây, dùng khăn mát giữ ấm và nới lỏng đai ngực cho nó!",
        "Giữa sa mạc hoang vắng thế này, chờ xe cấp cứu đường bộ chạy tới làm sao kịp nữa!",
        "Tổng đài nghe rõ, đây là Sĩ quan đặc nhiệm Tom, mã hiệu bốn ba bảy thuộc LAPD!",
        "Có người nguy kịch trên xa lộ tám sáu, yêu cầu trực thăng y tế hạ cánh khẩn cấp!",
        "Sĩ quan bốn ba bảy sao... hóa ra người anh em ngồi chung bàn với tao là cớm chìm?",
        "Anh muốn xử tôi thế nào cũng được Micdo, nhưng hãy để trực thăng cứu sống Cevin đã!",
    ],
    36: [
        "Chiếc xe trắng của Seja vừa đỗ trước hiên kìa, cuối cùng thằng bé cũng về tới nhà.",
        "Anh cả ơi tha lỗi cho em, vì giữ xe của cha mà em làm liên lụy cả nhà...",
        "Về tới nhà là tốt rồi Seja, nhưng coi chừng hai chiếc mô tô đen ngoài đầu đường kìa!",
        "Ny Tran và Cela đang lao mô tô thẳng vào hiên nhà mình, cúi rạp người xuống mau!",
        "Tránh xa mép đường ngay Seja, hai chiếc mô tô của tụi nó đang ép sát vào chỗ em!",
        "Mở mắt nhìn anh đi Seja ơi, có anh hai với Ami đang giữ chặt tay em đây rồi!",
    ],
    37: [
        "Anh Tom ơi, thằng bé Seja hiền lành như vậy, sao bọn Ny Tran lại nhẫn tâm thế!",
        "Anh Micdo đi xuống xưởng với ánh mắt đáng sợ lắm, anh mau vô cản anh hai lại đi!",
        "Anh định đánh thức con xe chín trăm mã lực của cha anh giữa lúc đang phẫn nộ sao?",
        "Đụng tới em tao ngay trước hiên nhà này, hôm nay Ny Tran phải trả đủ từng phân một!",
        "Bình tĩnh lại đi Micdo, lái chiếc xe đó đi báo thù là anh tự đóng sập đường về!",
        "Không gì cản nổi cơn giận của Micdo nữa rồi, mình phải lấy chiếc xe cam bám theo ngay!",
    ],
    38: [
        "Chạy đằng trời cũng không thoát khỏi tay tao đâu Cela, tấp chiếc mô tô của mày vô lề!",
        "Ny Tran đang ép sát mạn xe anh kìa Micdo, để tôi đôn chiếc xe cam lên khóa góc!",
        "Trò săn đuổi của mày kết thúc tại đây rồi Ny Tran, hạ ga và dừng xe lại ngay!",
        "Tay lái của hắn quệt gương xe mình rồi trượt thẳng xuống lòng kênh bê tông bên dưới!",
        "Ny Tran đã nằm lại dưới lòng kênh chờ cảnh sát tới, dừng tay lại ở đây đi Micdo!",
        "Ân oán với băng Light Saigon đã khép lại, nhưng lòng của Micdo vẫn chưa thể dừng lại.",
    ],
    39: [
        "Một phần tư dặm cuối trước đường ray tàu hỏa... chạy với tao mười giây tự do đi Tom!",
        "Chín trăm mã lực nhấc bổng cả đầu xe lên, đúng là con quái vật của cha anh ấy!",
        "Tiếng còi tàu hỏa gầm sát bên sườn rồi, chỉ còn một tích tắc để hai xe vọt qua!",
        "Lướt qua mũi tàu hỏa trong một hơi thở, đây chính là mười giây tự do của đời tao!",
        "Đánh lái sang phải ngay Micdo, chiếc xe tải trong hẻm vừa lao ra chắn ngang đường kìa!",
        "Cú va quệt làm chiếc xe đen xoay vòng ra lề đất rồi, trụ vững trong đó nghe Micdo!",
    ],
    40: [
        "Khoang máy đang trào khói trắng, khoác tay lên vai tôi bước ra khỏi buồng lái ngay Micdo!",
        "Tựa hẳn vào vai tôi đi Micdo, còi xe của đội đặc nhiệm đã hú vang đầu đường rồi.",
        "Cuộc đua khép lại rồi Sĩ quan Tom, rút còng số tám ra hoàn thành nhiệm vụ của cậu đi.",
        "Đêm đầu tiên tôi nợ anh một con xe mười giây, chiếc xe cam này là của anh.",
        "Cầm lấy chìa khóa rồi nhấn ga đi về phía chân trời đi Micdo, đừng ngoái đầu lại!",
        "Món nợ mười giây đã trả trọn, giờ tôi đứng lại đây nhận mọi phán quyết, trung sĩ Nese.",
    ],
}

CHARACTER_ACTING_PERSONA = {
    "TOM": "composed undercover intensity, steady eye contact, grounded chest breathing, and natural hand follow-through while speaking",
    "MICDO": "gravelly authoritative stillness, deliberate weight shifts, unblinking eye contact, and deep resonant vocal projection",
    "AMI": "warm emotional candor, expressive dark eyes, natural head-and-shoulder nuance, and sincere vocal inflection",
    "CEVIN": "coiled street-fighter energy, sharp jaw tension, decisive hand gestures, and fiery vocal urgency",
    "CINA": "cool tactical composure, economical driver movements, focused gaze, and crisp vocal clarity",
    "SEJA": "earnest youthful intensity, quick expressive hand movements, attentive posture behind thin-framed glasses, and eager vocal cadence",
    "ONLE": "grounded veteran steadiness, calm broad-shouldered posture, measured gestures, and warm fraternal tone",
    "NYTRAN": "icy predatory calm, razor-sharp gaze, minimal controlled gestures, and smooth menacing vocal delivery",
    "CELA": "watchful enforcer tension, coiled shoulder posture, sharp chin movements, and clipped raspy projection",
    "NESE": "seasoned command gravitas, weathered observant eyes, grounded stance, and measured Southern Vietnamese diction",
    "KINAN": "crisp federal urgency, upright posture, decisive hand gestures, and commanding vocal pace",
    "VERNI": "hardened long-haul grit, braced forearm tension on the wheel, defiant eyes, and booming gravelly projection",
}

_NEW_FIRST_INTRO_CLIPS = {}
for _old_cid, _val in FIRST_INTRO_CLIPS.items():
    _old_s, _c_str = _old_cid.split(".")
    _new_s = _OLD_TO_NEW[int(_old_s)]
    _NEW_FIRST_INTRO_CLIPS[f"{_new_s:02d}.{_c_str}"] = _val
FIRST_INTRO_CLIPS = _NEW_FIRST_INTRO_CLIPS


for _char_key, _char_spec in CHARACTER_LOCK.items():
    if _char_key in IDENTITIES and _char_spec.get("media_id"):
        IDENTITIES[_char_key]["media_id"] = _char_spec["media_id"]


CAMERA_LENS_LABEL = {
    "E": "wide establishing 24mm",
    "W": "wide 35mm",
    "M": "medium two-shot 50mm",
    "I": "macro detail 85mm",
    "T": "low-angle tracking 35mm",
    "C": "tight close-up 85mm",
    "H": "kinetic handheld 35mm",
    "P": "dramatic push-in 50mm",
}

CAMERA_RHYTHM_MAP = {
    "E": "Continuous fluid tracking momentum from 0.0s, smooth spatial progression across 3.2–6.8s while dialogue plays in motion, and unbroken forward follow-through to 10.0s.",
    "W": "Immediate physical momentum at 0.0s, smooth weight and spatial progression through 3.2–6.8s while speaking in stride, and natural kinetic follow-through through 10.0s without freezing.",
    "M": "Unbroken two-shot physical flow from 0.0s, natural upper-body and hand follow-through across 3.2–6.8s synchronized with speech, and smooth settling momentum through 10.0s.",
    "I": "Immediate mechanical motion at 0.0s, progressive physical actuation through 3.2–6.8s under off-screen voice, and continuous dynamic follow-through to 10.0s.",
    "T": "High-velocity lateral tracking momentum from 0.0s, smooth steering and suspension articulation across 3.2–6.8s during the line, and sustained forward motion through 10.0s.",
    "C": "Fluid micro-expression and head-and-shoulder movement from 0.0s, organic lip-sync and hand gesture integration across 3.2–6.8s, and natural breathing follow-through to 10.0s.",
    "H": "Tightly choreographed kinetic momentum at 0.0s, seamless defensive footwork or steering follow-through across 3.2–6.8s during speech, and balanced physical recovery through 10.0s.",
    "P": "Steady purposeful push-in from 0.0s, continuous posture and gesture evolution through 3.2–6.8s as the line lands, and a living, breathing resolution through 10.0s.",
}


def _build_context_beats(
    s_num: int,
    c_num: int,
    cid: str,
    title: str,
    loc_key: str,
    story_time: str,
    cat: str,
    active_name: str,
    counterpart_name: str | None,
    veh_label: str,
    sec_veh_label: str,
    obj_label: str,
    staging: dict,
) -> tuple[str, str, str, str, str]:
    """Construct concrete, physically plausible (open_state, beat1, beat2, beat3, end_state) from scene_staging.py."""
    explicit_beats = staging.get("beats")
    if not explicit_beats or len(explicit_beats) < c_num or explicit_beats[c_num - 1] is None:
        raise ValueError(f"[{cid}] Missing explicit staging beats in scene_staging.py for Scene {s_num:02d} Clip {c_num}!")
    open_st, b1, b2, b3, end_st = explicit_beats[c_num - 1]
    open_full = f"In {loc_key} during {story_time} (shot {cid} opening): {open_st.strip()}."
    end_full = f"In {loc_key} at 10.0s of shot {cid}: {end_st.strip()}."
    return open_full, b1.strip(), b2.strip(), b3.strip(), end_full


def build_scene_clips(scene_spec: tuple) -> dict:
    (
        s_num,
        title,
        story_time,
        loc_key,
        chars,
        props,
        tension,
        purpose,
        q_vi,
        hook_vi,
        turn_vi,
        payoff_vi,
    ) = scene_spec

    loc_desc, loc_sound = LOCATIONS[loc_key]
    staging = get_scene_staging(
        s_num, title, story_time, loc_key, chars, props,
        IDENTITIES, LOOKS, VEHICLE_LOCK, OBJECT_LOCK, ENVIRONMENT_LOCK,
    )
    has_insert_clip3 = staging.get("insert_clip3") is not None
    cameras = ["E" if s_num == 1 else "W", "M", "I" if has_insert_clip3 else "T", "C", "H", "P"]
    # 16:9 YouTube film cuts continuously across camera angles — never use CONTINUE or inject previous last frame
    transitions = ["OPEN", "CUT", "CUT", "J", "CUT", "L"]

    # Determine lighting based on story_time
    if "night" in story_time:
        lighting = "Crisp nocturnal street lighting: sodium vapour and neon highlights cutting through deep asphalt shadows, natural skin tones, restrained contrast."
    elif "dawn" in story_time or "morning" in story_time:
        lighting = "Golden California morning light: low warm sun casting long directional shadows across asphalt and steel, cool ambient sky fill, natural skin tones."
    elif "sunset" in story_time or "dusk" in story_time:
        lighting = "Warm amber sunset glow: low horizon sun raking across vehicle bodywork and faces, long dramatic shadows, deep cobalt dusk sky."
    else:
        lighting = "Bright California daylight: clean directional sun with natural bounce off concrete and painted metal, realistic skin texture and clear shadow detail."

    prop_main = props[0] if props else "WRENCH_KIT"
    prop_main_readable = (
        VEHICLE_LOCK[prop_main]["name"] if prop_main in VEHICLE_LOCK
        else OBJECT_LOCK[prop_main]["name"] if prop_main in OBJECT_LOCK
        else f"the {prop_main.lower().replace('_', ' ')}"
    )

    clips = []

    for c_num in range(1, 7):
        cid = f"{s_num:02d}.{c_num}"
        cam = cameras[c_num - 1]
        trans = transitions[c_num - 1]
        lens_label = CAMERA_LENS_LABEL[cam]

        # Rank characters from scene cast by their appearance in the clip's Beat 2 (speaking beat), Beat 1, Open State, Beat 3
        raw_beat = (
            staging["beats"][c_num - 1]
            if staging.get("beats") and len(staging["beats"]) >= c_num
            else None
        )
        ranked_chars: list[str] = []
        if raw_beat is not None:
            r_open, r_b1, r_b2, r_b3, r_end = raw_beat
            for seg in (r_b2, r_b1, r_open, r_b3, r_end):
                matches = []
                for lk in chars:
                    nm = IDENTITIES[LOOKS[lk][0]]["name"]
                    m = re.search(rf"\b{re.escape(nm)}\b", seg)
                    if m:
                        matches.append((m.start(), lk))
                matches.sort()
                for _, lk in matches:
                    if lk not in ranked_chars:
                        ranked_chars.append(lk)
        if not ranked_chars:
            ranked_chars = list(chars)

        clip_chars = list(ranked_chars[:3])

        # Ensure narrator intro characters are present in that exact first-intro clip
        if cid in FIRST_INTRO_CLIPS:
            intro_key, _ = FIRST_INTRO_CLIPS[cid]
            if intro_key == "VERNI":
                clip_chars = ["VERNI"]
            elif intro_key == "CEVIN":
                clip_chars = ["CEVIN_H", "VERNI"]
            elif intro_key == "CINA":
                clip_chars = ["CINA_H", "CEVIN_H"]
            elif intro_key == "ONLE":
                clip_chars = ["ONLE_H", "CINA_H"]
            elif intro_key == "TOM":
                clip_chars = ["TOM"]
            elif intro_key == "AMI":
                clip_chars = ["TOM", "AMI"]
            elif intro_key == "SEJA":
                clip_chars = ["CEVIN", "SEJA", "ONLE"]
            elif intro_key == "MICDO":
                clip_chars = ["MICDO", "TOM_B", "CEVIN"]
            elif intro_key == "NESE_KINAN":
                clip_chars = ["NESE", "KINAN", "TOM_B"]
            elif intro_key == "NYTRAN_CELA":
                clip_chars = ["NYTRAN", "CELA", "TOM_R"]

        # Determine active speaker & distinct counterpart directly from ranked_chars
        active_speaker = ranked_chars[0] if ranked_chars else clip_chars[0]
        if active_speaker not in clip_chars and clip_chars:
            clip_chars = [active_speaker] + [k for k in clip_chars if k != active_speaker][:2]
        counterpart_look = next((k for k in clip_chars if k != active_speaker), None)

        active_base = LOOKS[active_speaker][0]
        active_name = IDENTITIES[active_base]["name"]
        counterpart_name = IDENTITIES[LOOKS[counterpart_look][0]]["name"] if counterpart_look else None
        if counterpart_name == active_name:
            counterpart_name = None

        # Dedicated Insert / B-Roll Shot handling for Clip 3 (`camera == "I"`)
        is_insert_shot = (c_num == 3 and cam == "I" and staging.get("insert_clip3") is not None and cid not in FIRST_INTRO_CLIPS)
        if is_insert_shot:
            clip_chars = []
            ins = staging["insert_clip3"]
            for lk in chars:
                nm = IDENTITIES[LOOKS[lk][0]]["name"]
                if f"While {nm}'s voice plays off screen" in ins["action"]:
                    active_speaker = lk
                    active_base = LOOKS[active_speaker][0]
                    active_name = nm
                    break
            start_frame = ins["start_frame"]
            action = ins["action"]
            end_frame = ins["end_frame"]
            shot_type = "INSERT_DETAIL"
            composition_str = ins["composition"]
            blocking_str = ins["blocking"]
            focus_str = ins["focus"]
            performance_str = f"Mechanical and physical detail moves with smooth, continuous follow-through from 0.0s to 10.0s while {active_name}'s voice plays cleanly off screen."
        else:
            shot_type = (
                "ESTABLISHING_WIDE" if cam in ("E", "W")
                else "VEHICLE_PURSUIT_TRACK" if cam == "T"
                else "REACTION_CLOSEUP" if cam == "C"
                else "KINETIC_HANDHELD" if cam == "H"
                else "DRAMATIC_PUSH_IN" if cam == "P"
                else "SCENE_MEDIUM"
            )
            open_st, b1, b2, b3, end_st = _build_context_beats(
                s_num, c_num, cid, title, loc_key, story_time,
                staging.get("category", "outdoor_urban"),
                active_name, counterpart_name,
                staging.get("veh_label", prop_main_readable),
                staging.get("sec_veh_label", "the road lane"),
                staging.get("obj_label", prop_main_readable),
                staging,
            )
            start_frame = open_st
            end_frame = end_st
            action = f"Beat 1 (0.0–3.2s): {b1}. Beat 2 (3.2–6.8s): {b2}. Beat 3 (6.8–10.0s): {b3}."

            combined_beats = f"{b1} {b2} {b3}"
            clip_prop = prop_main
            if "SUPRA_KEY" in props and ("SUPRA_KEY" in combined_beats or "ignition key" in combined_beats):
                clip_prop = "SUPRA_KEY"
            elif "CHARGER" in props and ("Charger" in combined_beats or "CHARGER" in combined_beats) and "Supra" not in combined_beats:
                clip_prop = "CHARGER"
            else:
                for pk in props:
                    if pk in combined_beats:
                        clip_prop = pk
                        break
            clip_prop_readable = (
                VEHICLE_LOCK[clip_prop]["name"] if clip_prop in VEHICLE_LOCK
                else OBJECT_LOCK[clip_prop]["name"] if clip_prop in OBJECT_LOCK
                else prop_main_readable
            )

            if counterpart_name:
                composition_str = f"Frame {active_name} and {counterpart_name} with {clip_prop_readable} anchored clearly in the {lens_label} lens geometry."
                blocking_str = f"Preserve left-to-right 180-degree spatial continuity inside {loc_key}; {active_name} moves smoothly on the near side while {counterpart_name} holds the counter-angle."
            else:
                composition_str = f"Frame {active_name} with {clip_prop_readable} and {staging['counterpart_placement']} anchored clearly in the {lens_label} lens geometry."
                blocking_str = f"Preserve left-to-right 180-degree spatial continuity inside {loc_key}; {active_name} holds the primary plane aligned with {staging['counterpart_placement']}."
            if cid == "40.6":
                focus_str = f"Keep tack-sharp focus on {active_name}'s eyes, natural breathing, and calm posture on the desert road as {counterpart_name or 'Sergeant Nese'} steps into the background depth plane."
            else:
                focus_str = f"Keep tack-sharp focus on {active_name}'s eyes and continuous hand-and-body follow-through with {clip_prop_readable}, maintaining readable background depth."
            persona = CHARACTER_ACTING_PERSONA.get(
                active_base,
                "restrained high-stakes intensity, continuous natural weight transfer, and fluid hand follow-through while speaking",
            )
            if counterpart_name:
                performance_str = (
                    f"{active_name} delivers the line with {persona}, while {counterpart_name} maintains active eyeline engagement, "
                    f"subtle listening posture, and natural closed-lip facial reaction."
                )
            else:
                performance_str = f"{active_name} delivers the line with {persona} and organic micro-expressions."

        moving_vehicle_scenes = {1, 2, 3, 4, 14, 15, 17, 29, 32, 33, 34, 38, 39}
        moving_vehicle_clips = {
            "05.6", "07.1", "08.5", "09.1", "09.6", "13.6", "16.1", "16.2", "16.6",
            "18.1", "18.2", "18.3", "19.5", "28.1", "28.4", "31.6", "36.1", "36.3",
            "36.4", "36.5", "37.4", "37.5", "37.6", "40.5", "40.6",
        }
        is_moving_vehicle_clip = (s_num in moving_vehicle_scenes) or (cid in moving_vehicle_clips)
        if is_moving_vehicle_clip:
            blocking_str = (
                f"{blocking_str} All moving vehicles travel in the exact same left-to-right forward direction along the road lane "
                f"with rapidly spinning wheels and matched forward velocity; never face head-on or reverse axis."
            )

        veh_sfx_list = [VEHICLE_SFX_LOCK[p] for p in props if p in VEHICLE_SFX_LOCK]
        primary_sfx = (
            "; ".join(veh_sfx_list[:2])
            if veh_sfx_list
            else "crisp tactical prop contact, footsteps, and authentic room acoustics"
        )
        if is_moving_vehicle_clip:
            sound_detail_str = (
                f"HIGH-PRIORITY AUTOMOTIVE SFX: {primary_sfx}, high-speed spinning tire-on-asphalt traction, "
                f"crisp gearshifts, and wind slipstream layered prominently with {active_name}'s Southern Vietnamese dialogue."
            )
        else:
            sound_detail_str = (
                f"PRIORITY DIEGETIC SFX: {primary_sfx}, clean mechanical contact, and natural breathing "
                f"layered clearly beneath {active_name}'s Southern Vietnamese dialogue."
            )

        line_text = SCENE_DIALOGUES[s_num][c_num - 1]
        line_syl = len(re.findall(r"[^\W\d_]+", line_text))
        dialogue = []
        spoken_mode = "off" if is_insert_shot else "on"
        if cid in FIRST_INTRO_CLIPS:
            _, intro_text = FIRST_INTRO_CLIPS[cid]
            intro_syl = len(re.findall(r"[^\W\d_]+", intro_text))
            intro_end = round(0.3 + max(3.0, intro_syl / 3.5), 1)
            line_start = round(intro_end + 0.3, 1)
            line_end = min(9.8, round(line_start + max(2.8, line_syl / 3.8), 1))
            dialogue.append({
                "speaker": "NARRATOR",
                "mode": "vo",
                "text": intro_text,
                "at": [0.3, intro_end],
            })
            dialogue.append({
                "speaker": active_speaker,
                "mode": spoken_mode,
                "text": line_text,
                "at": [line_start, line_end],
            })
        else:
            dur = max(3.2, min(6.6, round(line_syl / 3.7, 1)))
            dialogue.append({
                "speaker": active_speaker,
                "mode": spoken_mode,
                "text": line_text,
                "at": [2.8, round(2.8 + dur, 1)],
            })

        cinematic = {
            "intent": f"{purpose} (Shot {cid} — {shot_type} via {lens_label} lens).",
            "composition": composition_str,
            "blocking": blocking_str,
            "performance": performance_str,
            "focus": focus_str,
            "texture": "Weathered asphalt, brushed steel, painted bodywork, natural skin pores and subtle exhaust heat shimmer.",
            "sound_detail": sound_detail_str,
            "rhythm": CAMERA_RHYTHM_MAP[cam],
        }

        veh_states = {p: resolve_vehicle_condition(p, s_num, c_num) for p in props if p in VEHICLE_LOCK}
        obj_states = {p: resolve_object_condition(p, s_num, c_num) for p in props if p in OBJECT_LOCK}
        spatial_state = {
            "axis": staging["axis_rule"],
            "shot_type": shot_type,
            "subject_position": "mechanical/object detail insert" if is_insert_shot else staging["lead_placement"],
            "counterpart_position": staging["counterpart_placement"],
            "camera_code": cam,
            "screen_direction": (
                "co-directional left-to-right forward vehicle motion along established 180-degree axis with rapidly spinning wheels"
                if is_moving_vehicle_clip
                else "left-to-right along established 180-degree axis"
            ),
            "moving_vehicle_clip": is_moving_vehicle_clip,
        }
        entity_state = {
            "shot_type": shot_type,
            "vehicles": veh_states,
            "objects": obj_states,
            "visible_characters": list(clip_chars),
        }

        gear_names = ", ".join(IDENTITIES[LOOKS[k][0]]["name"] + f" ({k})" for k in clip_chars) or "Cận cảnh đạo cụ / phương tiện (không có nhân vật trong khung hình)"
        props_names = ", ".join(props)
        counter_vi = f" và {counterpart_name}" if counterpart_name else ""
        screenplay_vi = {
            "gear_vi": f"Nhân vật trong cảnh: {gear_names}. Đạo cụ & phương tiện khóa: {props_names}. Giữ nguyên trang phục và vị trí đạo cụ xuyên suốt cú máy {cid}.",
            "start_vi": f"Bối cảnh: {title} ({story_time}) · Góc máy {cam} ({shot_type}) · Mở hình tại 0.0s với {active_name}{counter_vi} trong không gian {loc_key}.",
            "beats_vi": (
                f"Nhịp 1 (0.0–3.2s): {active_name} {'bắt đầu thao tác với ' + prop_main + ' trong bối cảnh ' + title + ', giữ đúng vị trí không gian' if not is_insert_shot else 'thao tác kỹ thuật ngoài khung hình trong khi ống kính đặc tả chi tiết cơ khí'}. "
                f"Nhịp 2 (3.2–6.8s): {active_name} thực hiện chuyển động chính của phân cảnh {cid} đồng thời cất lời thoại ({line_text}). "
                f"Nhịp 3 (6.8–10.0s): Chuyển động lắng xuống tư thế kết của clip {cid}, giữ nhịp thở và âm thanh môi trường sống động tới 10.0s."
            ),
            "end_vi": f"Khóa tư thế của {active_name}{counter_vi} cùng đạo cụ ({props_names}) tại giây 10.0s, tuyệt đối không nháy ảnh thẻ tham chiếu.",
            "directing_vi": f"Góc máy {cam} ({shot_type}) · Chuyển cảnh {trans} · Đạo cụ khóa: {props_names}.",
        }

        wardrobe_targets = ", ".join(clip_chars) if clip_chars else "no visible cast (vehicle/object detail insert)"
        clips.append({
            "number": c_num,
            "location": loc_key,
            "characters": clip_chars,
            "props": list(props),
            "camera": cam,
            "shot_type": shot_type,
            "transition": trans,
            "start_frame": start_frame,
            "action": action,
            "end_frame": end_frame,
            "dialogue": dialogue,
            "lighting": lighting,
            "cinematic": cinematic,
            "spatial_state": spatial_state,
            "entity_state": entity_state,
            "wardrobe_note": f"Keep exact approved appearance for {wardrobe_targets} with props {', '.join(props)}; never show a studio reference backdrop.",
            "screenplay_vi": screenplay_vi,
            "avoid": (
                "changing vehicle color, wheel count or left-hand driver side, stationary or non-spinning wheels on moving vehicles, "
                "vehicles driving or facing in opposite directions during a race or pursuit, muted engine or tire sound effects, "
                "adding duplicate characters or broadcaster logos"
            ),
        })

    return {
        "number": s_num,
        "title": title,
        "story_time": story_time,
        "purpose": purpose,
        "dramaturgy": {
            "dramatic_question_vi": q_vi,
            "hook_vi": hook_vi,
            "turn_vi": turn_vi,
            "payoff_or_setup_vi": payoff_vi,
            "tension": tension,
        },
        "outgoing_audio": f"Carry the {loc_sound} across the cut into the next scene without quiet pause.",
        "clips": clips,
    }


def main():
    scenes = [build_scene_clips(spec) for spec in SCENE_SPECS]
    plan = {
        "schema_version": 3,
        "editorial_revision": "3.1",
        "title": "Đường Đua Sinh Tử: 10 Giây Tự Do",
        "frame_rate": 24,
        "aspect_ratio": "16:9",
        "clip_seconds": 10,
        "film_bible": {
            "vehicles": {k: v["description"] for k, v in VEHICLE_LOCK.items()},
            "objects": {k: v["description"] for k, v in OBJECT_LOCK.items()},
            "environments": {k: v["orientation_axis"] for k, v in ENVIRONMENT_LOCK.items()},
        },
        "narrator": NARRATOR,
        "identities": IDENTITIES,
        "looks": LOOKS,
        "locations": LOCATIONS,
        "props": PROPS,
        "scenes": scenes,
    }
    out_path = BASE_DIR / "PHAN_CANH_V3.json"
    out_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out_path} with {len(scenes)} scenes and {sum(len(s['clips']) for s in scenes)} clips.")


if __name__ == "__main__":
    main()
