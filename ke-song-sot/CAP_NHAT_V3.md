# Các thay đổi bản 3 — 30/10/2026

Đã viết lại toàn bộ 360 cú máy, sinh đồng bộ 60 README cảnh, 60 caption, kịch bản tổng, hồ sơ và khóa. Không tạo video hoặc thay file MP4 trong đợt này.

## Chuyển cảnh và chống lặp

- Mỗi clip có start frame, hành động mới và end frame cụ thể. 360 hành động khác nhau; không lặp nguyên câu thoại giữa các clip.
- Có bảng riêng cho đủ 359 mối ghép, gồm ranh giới 59 cảnh. 38 điểm dùng frame nối trong cùng cú máy; 321 điểm dùng cắt có ý đồ, đổi địa điểm/thời gian rõ.
- Bỏ giữ đứng hình 0,5 giây, chia ba góc theo template, slow motion ngẫu nhiên, nhạc riêng từng clip và việc lấy từ “chạy” để gán máy quay rượt đuổi.
- Một camera setup trong một clip. Với cú cắt cùng phòng, thay góc coverage rõ trong cùng nửa trục; với CONTINUE, giữ nguyên camera và tiếp hành động thay vì diễn lại.
- Đã rà riêng âm nối cuối từng cảnh sang cảnh sau, bỏ các âm/match hình dựa vào một sự kiện xảy ra từ vài clip trước.

## Kịch bản và liên tục

- Hạn bảy ngày gắn chuyến tàu chuyển Hạ; dữ liệu khóa thực sự được mở bằng token ở 25.2.
- Cao trào là trao đổi bị phản bội. Dũng dùng Tê giữ Sơn sống; phản diện nhận biết đúng chất của chúng. Không còn mẹo công khai báo 40 phút rồi đánh lừa chính người sản xuất thuốc.
- Mây xác minh trước khi hợp tác, xin hỗ trợ trước chuyến thành phố, giữ dân ngoài vùng nguy hiểm và dẫn tiếp cận hải đăng. Kiên hết đường xe nên dùng lối bộ kỹ thuật.
- Hạ chủ động để khăn, gửi dấu qua video, trì hoãn và giữ cửa cho lực lượng bằng kẹp tóc. Cô bắt đầu làm sạp hoa vì đời sống của mình.
- Một đồng hồ duy nhất: không mở trước 52.2, không có chiếc thứ hai ở kết. Ảnh để Mây nhận ra Hạ là ảnh rời.
- Khăn, sổ đen/đỏ, USB gốc/bản làm việc, token, còng và súng đều có đường đi rõ. Băng tay Sơn giữ bên trái. Hạ chỉ đổi đồ tại đồn; Sơn vest tay trần ở chuỗi cao trào.
- Thống nhất quá khứ xa cách 25 năm: Sơn 20, Bà Hai 35, giữ nguyên chín danh tính. Cảnh sau nhiều năm dùng đúng tuổi tăng thêm.
- Giảm lời dẫn và các lượt giải thích trùng; giữ giá phải trả qua lời khai và việc Sơn tự nhận còng. Không tạo thêm kết bằng một dãy vạch chờ mới.

## Nguồn và kiểm tra

`PHAN_CANH_V3.json` là nguồn duy nhất; `build_prompts_v3.py` biên dịch, lệnh cũ vẫn chạy được. `--check` kiểm tra cả dữ liệu và toàn bộ 485 file sinh ra khớp nguồn. Bộ 9 kiểm tra tự động bao gồm lỗi nối frame, đổi địa điểm trong CONTINUE, trang phục giải cứu, lần mở đồng hồ đầu, hành động lặp, tag lọt vào lời đọc chế độ tạo đúng kiểu cắt và reference chỉ cho người trong hình/ảnh được chỉ định.

`RENDER_MANIFEST_V3.json` ghi hash cho từng prompt. Trạng thái CMS/file MP4 cũ chưa được chuyển thành video bản 3. Sau khi tạo lại cần xem ghép đôi và kiểm tra toàn phim để xác nhận độ mượt hình/khẩu hình/âm thanh thực tế.

Đã chỉnh bộ chọn reference của runner để lời dẫn/đầu nối không kéo thêm nhân vật vào hình. Shot không có danh tính được chỉ định dùng text-to-video; hành vi chọn reference cũ vẫn giữ cho prompt đời trước.

Bản trước khi sửa: `revisions/before_v3_20261030_143044.zip`.

## Sửa lỗi ghép tự động và khóa quy tắc điện ảnh — 30/10/2026 (tối)

Rà theo bản nhận xét cảnh 01.1. Lỗi gốc nằm ở lượt "nhịp nhanh" lúc 16:42. Lượt này ghép action của mọi clip theo khuôn Beat 1 = hành động gốc, Beat 2 = ghi chú blocking, Beat 3 = ghi chú diễn xuất. Vì ghi chú blocking tả lại đúng hành động gốc, cả 360 clip đều bảo model diễn động tác chính hai lần. End frame còn bị gắn thêm "Final physical lock", tức một hành động chứ không phải trạng thái.

- **Hành động:** viết lại 360 action thành ba nhịp có mốc giây riêng; mỗi sự kiện chỉ xảy ra một lần và nhịp cuối rơi đúng end frame. Start/end frame chỉ ghi trạng thái, đã bỏ "Framing:" và "Final physical lock". Khôi phục nghĩa các chỗ bị đổi "slowly → briskly" (41.5, 47.6, 48.3, 52.4, 55.6, 60.5).
- **Thoại:** tối đa 30 âm tiết mỗi clip theo quy tắc Omni trong FLOW_GUIDE. Trước đây 213 clip vượt mức, dài nhất 65 âm tiết; nay 256 clip nằm trong 15–30, còn lại ngắn hơn ở các nhịp lặng, dài nhất 29. Đã bỏ các câu kể trước thông tin chưa tới lượt.
- **01.1, cảnh mở đầu hoành tráng:** không còn Sơn độc thoại. Máy 24mm trượt thấp dọc lề đường theo xe khách liên tỉnh đang chạy lúc bình minh.
  - **Cấu tạo xe ghi rõ:** xe chạy bên phải đường, ghế tài xế bên trái cabin, cửa hành khách là cửa gấp ở hông phải ngay sau bánh trước và quay về máy quay; cửa tài xế phía xa luôn đóng.
  - **Diễn tiến:** tài xế phanh, bấm nút mở cửa và ngồi yên suốt cảnh. Một bà cụ đội nón lá và một thanh niên ôm thùng các-tông xuống trước bằng cửa hành khách, rồi Sơn xuống cuối, xuống hẳn trước 6.5s. Người dẫn chuyện chỉ đọc tên sau khi anh đã đứng trên mặt đường (6.7–9.6s).
  - **Danh sách cấm riêng của clip:** không ai dùng cửa tài xế, tài xế không rời ghế, Sơn không xuống trước và không mang túi thứ hai.
  - **Đối xứng với 60.4:** xe chạy từ trái sang phải khung; cảnh trở về 60.4 đổi cho xe rời khung về bên phải.
- **Người dẫn chuyện giới thiệu nhân vật:** chín nhân vật chính, mỗi người được giới thiệu một câu ngắn ở clip đầu tiên họ ra hình: Sơn 01.1, ông Bảy 01.2, Bà Hai và Dũng 02.1, Mây và Thành 03.2, Hạ 04.1, bác sĩ Linh 13.1, Kiên 36.1. Thoại trong các clip này được rút gọn để tổng vẫn ≤ 30 âm tiết. Validator bắt buộc đủ chín lời và chặn người dẫn chuyện ở các clip khác.
- **Thoại đi cùng chuyển động:** cả 488 câu có khung giây riêng, in ngay trước câu trong prompt (ví dụ 3.0–6.3s). Câu bắt đầu đúng nhịp hành động đang diễn ra, không chồng nhau, tối đa 4,5 âm tiết mỗi giây. 50.3, 50.6 và 53.1 được nới mốc nhịp cho hai lượt thoại chung một nhịp. Câu bộ đàm 56.1 bỏ dấu hai chấm, vì prompt chỉ đọc phần sau dấu hai chấm cuối.
- **Quy tắc chung trong mọi prompt:**
  - 24fps; shutter 180°, riêng 150° cho handheld hành động.
  - Màu: bóng lạnh, highlight ấm vừa phải, da tự nhiên.
  - Diễn xuất: micro-expression, thở nhẹ, mắt tự nhiên.
  - "In a single continuous shot" để chống Omni tự chia cảnh.
  - Hiệu ứng âm thanh phải có nguồn trong cảnh.
  - Giữ vị trí, ánh nhìn, tay cầm đạo cụ và hướng di chuyển qua cú cắt.
- **Khung hình sạch:** cấm logo đài truyền hình hoặc kênh, watermark, chữ chạy tin tức, lower-third, LIVE/REC, timestamp. Validator chặn chữ TV/tin tức/truyền hình trong dữ liệu cảnh.
- **Ánh sáng và bối cảnh:** cả 69 thiết lập ánh sáng ghi rõ nguồn và hướng (key/fill). 09.6, 13.6, 02.6 và 19.6 có ánh sáng riêng đúng địa điểm và giờ. Bối cảnh Hòn Sóng thêm 3–4 dấu hiệu Việt Nam: đường nhựa nứt viền cát, nhà bê tông thấp bạc màu muối, mái tôn, phi lao, thuyền đánh cá.
- **Liên tục:**
  - Vạch đếm ngày ở 07.4 là 2, không còn mặc định 7.
  - Mây không đeo còng từ 24.6 tới 35.1.
  - Kính của Thành: cong nhưng chưa quấn băng ở cảnh 29, quấn băng từ 30, kính mới ở 56.5.
  - Đồng hồ được ghi vào đạo cụ ở 53.1–53.3; phong bì bản sao ghi vào đạo cụ từ 34.2 tới 43.1.
  - 25.1 dùng USB bản sao; 54.3 dùng điện thoại của Mây; balo không còn ghi chú sai thời điểm trước 35.4.
- **Kiểm tra:** validator mới chặn action thiếu ba nhịp hoặc lặp blocking, frame chứa hành động, thoại trên 30 âm tiết và chữ gợi bản tin. Bộ test tăng từ 12 lên 18.

Ghi chú mở: luật "mọi clip có thoại" vẫn giữ. 13 clip vốn được thiết kế lặng (ví dụ 04.4, 33.5, 53.4, 57.5) nay có một câu ngắn, và ghi chú âm thanh của chúng đã được sửa cho khớp. Hash prompt trong `RENDER_MANIFEST_V3.json` đã đổi, nên mọi clip đã render từ bản 16:42 cần tạo lại.

## Rà soát "prompt thông minh" toàn phim — 31/10/2026

**Lời giới thiệu do người khác đọc**
- Người dẫn chuyện là giọng nữ trưởng thành, đứng ngoài truyện. Prompt ghi rõ "giọng kể ngoài truyện, không phải nhân vật trong hình", và mọi miệng trên hình phải khép khi người dẫn chuyện nói.
- Lời giới thiệu ở ngôi thứ ba: "Sơn, bốn lăm tuổi. Giang hồ gọi là Bóng Ma.", "Người con gái ấy là Hạ, chủ tiệm hoa.", "Người giữ phòng khám Hòn Sóng, bác sĩ Linh."
- Bỏ các câu nhân vật tự xưng tên: Sơn ở 01.2, Mây ở 03.3 và 48.6. Validator chặn nhân vật tự giới thiệu và chặn người dẫn chuyện dùng ngôi thứ nhất.

**Rà 360 clip bằng 10 agent, mỗi phát hiện có 3 agent phản biện độc lập**
- Kết quả: 146 bản sửa được giữ. Bản sửa nào cũng đã chạy thử qua validator thật trước khi áp.
- Các nhóm lỗi đã sửa:
  - Thoại lệch nhịp với hành động: nói khi chưa ra hình, nói khi cửa xe chưa mở, hai câu chen nhau.
  - Ánh sáng sai địa điểm.
  - Đạo cụ thừa hoặc thiếu.
  - Tay hoặc vị trí bị nhảy qua cú cắt.
  - Đại từ mơ hồ khi có hai nhân vật nam.
  - Ghi chú âm thanh mâu thuẫn với thoại.
  - Một số lỗi truyện: "chủ nợ" thành "con nợ" ở 55.4; đèn dự phòng không phải đèn quay.

**Sửa ở cấp toàn phim (bộ biên dịch và thư viện)**
- Câu mở cảnh in đúng mốc giây của câu thoại đầu, không còn ghi cứng 0.2s.
- Mọi câu thoại kết thúc trước 9.8s để Omni không cắt đuôi câu.
- Không dùng chế độ "qua thiết bị" khi người nói đang có mặt trên hình.
- Băng cổ tay chỉ có ở mốc hiện tại, không có trong hồi tưởng.
- Còng của Mây đếm theo từng lần dùng trong chuyến thành phố và không có từ 24.6 đến 35.1.
- Túi của Dũng mất từ 46.6. Còng cũ của hắn vẫn ở cổ tay trong 46.4.
- Áo vest của Sơn cởi suốt cảnh 25. Sơn không mang balo khi bị áp giải.
- Đồng hồ đóng nắp đúng trong 52.6.
- Thêm đạo cụ KIEN_GUN (luôn ở tay trái, không bắn), HOUSE_KEY và MAY_FOLDER.
- Bổ sung người còn thiếu trong cảnh toàn 41.6, 42.4 và 42.6; bỏ Dũng khỏi cận cảnh tay ở 02.2.
- Ánh sáng tách theo địa điểm: 101 thiết lập.

**Khóa giọng người dẫn chuyện:** `PHAN_CANH_V3.json` có mục `narrator` riêng.
- **Mô tả giọng:** nữ khoảng 50 tuổi, giọng Sài Gòn, trầm ấm, hơi khàn nhẹ; kể điềm tĩnh như người dẫn phim điện ảnh; nhịp chậm khoảng 3,5 âm tiết/giây; thu khô, không vang, không nhạc nền.
- **Nơi xuất hiện:** bộ biên dịch in nguyên văn khóa giọng vào cả bảy clip giới thiệu. Bản tiếng Việt nằm trong FLOW_PROMPTS.md và NHAN_VAT.md.
- **Nhịp đọc:** câu nào của người dẫn chuyện vượt 3,8 âm tiết/giây thì validator báo lỗi. Bốn câu giới thiệu đã được rút gọn để đạt nhịp này (01.1, 01.2, 02.1, 03.2).

**Chuẩn hóa cơ thể, khẩu hình, mắt mũi (in vào mọi prompt, mục [BODY, MOUTH AND FACE STANDARD]):**
- **Nhặt, đặt, trao đồ:** cúi nhặt thì khuỵu gối và hông, tay được ghi nắm trọn rồi nhấc có sức nặng. Đồ không tự bay, không tự trượt vào tay, không xuyên qua ngón. Câu không ghi tay thì dùng tay đang rảnh; đồ đang cầm giữ nguyên tay. Trao đồ thì thấy đủ hai bàn tay. Chân không trượt, mỗi bàn tay đủ năm ngón. Clip 51.5 (Mây nhặt khẩu súng) được thêm động tác ngồi xuống.
- **Bản đồ miệng:** sinh tự động từ mốc giây của thoại. Mỗi khung giây ghi đúng một người được nhép môi, khớp từng âm tiết tiếng Việt; lời dẫn, người dẫn chuyện và giọng ngoài khung thì mọi miệng khép; ngoài các khung đó không ai nhép theo.
- **Mặt và mắt:** mặt khớp ảnh tham chiếu ở mọi khung (mắt, mí, sống mũi, đầu mũi, môi, cằm, tai), không biến dạng khi quay đầu, dấu nhận diện đúng chỗ. Chớp mắt tự nhiên, hai mắt cùng nhìn đúng hướng, không trợn, không lác, chỉ khóc khi kịch bản ghi.
- **AVOID:** thêm đồ vật trôi hoặc xuyên tay, ngón tay thừa hoặc dính, miệng cử động ngoài khung thoại, lệch khẩu hình, mặt biến dạng, mắt lệch.
- **Gọn prompt:** bỏ đoạn chép lại end frame của clip trước trong mục EDIT IN, vì trùng start frame và dễ khiến model vẽ lại cảnh cũ.

## Rà riêng cho Google Flow Omni — 31/10/2026

Đối chiếu với tài liệu Gemini Omni Flash và FLOW_GUIDE:

- **Đạt sẵn trên cả 360 prompt:**
  - Không có dấu ngoặc kép, nên không có chữ bị vẽ lên hình.
  - Mỗi clip tối đa 5 ảnh tham chiếu (runner cho tối đa 7).
  - Chuỗi Frames liên tiếp dài nhất 2 clip, dưới mức 3–4 clip cần neo lại nhân vật.
  - Thoại không quá 30 âm tiết mỗi clip và 4,5 âm tiết mỗi giây; mỗi khung giây một câu, câu thoại đứng sau dấu hai chấm ở cuối dòng.
  - Omni không công bố giới hạn độ dài prompt, nên prompt 8–12,6 KB không bị cắt.
- **Đã chỉnh trong bộ biên dịch:**
  - Omni không có ô negative prompt, nên mục AVOID đổi thành câu mệnh lệnh "Do not show or do…", và mục cấm riêng của clip cũng vậy.
  - FORMAT thêm "No scene cuts" cạnh "single continuous shot", và câu chuẩn: thoại tiếng Việt chỉ đọc thành tiếng, không hiện thành chữ.
  - Clip nối tiếp mở đầu theo đúng mẫu Frames của FLOW_GUIDE: khung cuối clip trước là khung đầu clip này, cùng nhân vật, trang phục, địa điểm, hướng sáng và màu; không nhảy thời gian.
  - Khối nhân vật thêm câu: giữ đúng thiết kế nhân vật đã duyệt, chỉ người được liệt kê và người không tên có ghi trong cảnh mới xuất hiện.
  - Nhãn thoại trong prompt chuyển sang tiếng Anh kèm giọng đã khóa của từng nhân vật (Omni hiểu tiếng Anh tốt nhất). Tài liệu cho người đọc vẫn giữ nhãn tiếng Việt.
  - Chữ viết tay, giấy in, chữ ký và màn hình trong truyện luôn mờ, không đọc được.
- **FLOW_GUIDE:** bảng tên nhân vật trên Flow ghi đủ chín thẻ, cộng `@Voice` NguoiKe cho người dẫn chuyện.
