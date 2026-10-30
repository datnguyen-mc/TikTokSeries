> Báo cáo này là đánh giá bản 2 trước khi biên tập. Bản 3 đã xử lý lại nội dung theo CAP_NHAT_V3.md; xem BANG_NOI_CLIP.md cho điểm nối hiện hành.

**KẺ SỐNG SÓT: BÓNG MA — ĐÁNH GIÁ TOÀN BỘ PROMPT**

Ngày rà soát: 30/10/2026. Phạm vi: bản hiện tại của 60 cảnh, 360 file `clip-*.md`, 60 README phân cảnh, kịch bản tổng, hồ sơ nhân vật, khóa Flow và mã sinh prompt. Đây là đánh giá kịch bản và chỉ dẫn dựng; chưa phải đánh giá diễn xuất, khẩu hình hay chất lượng hình ảnh của toàn bộ video đã render. Các đề xuất dưới đây chưa được áp dụng vào prompt gốc.

Trong quá trình rà soát, workspace có một đợt cập nhật nguồn khác. Báo cáo đã đối chiếu lại toàn bộ 360 prompt sau cập nhật: các lỗi thay từ như `[project LIST]` và các lần cắt đen theo chu kỳ đã hết; không còn được xem là lỗi đang tồn tại. Cảnh 38 hiện tên là “Đôi Găng Đầu Tiên”. Các số liệu dưới đây dùng bản đã đối chiếu lại.

**Nhận định chính**

Bộ phim có nền tốt: thị trấn biển có bản sắc, quan hệ Sơn–Bà Hai có sức nặng, và chuỗi biểu tượng găng tay–đồng hồ–khăn xanh–vạch đếm có thể tạo cảm xúc. Điểm kết Sơn tự đưa tay vào còng đáng giữ vì hoàn tất lựa chọn của nhân vật.

Tuy nhiên, bản hiện tại chưa đủ chặt để sản xuất tiếp toàn bộ như một phim liền. Ba việc cần làm trước là sửa nguyên nhân–kết quả của cao trào, thống nhất trạng thái nhân vật/đạo cụ, và bỏ cách phân cảnh tự động bằng từ khóa. Thêm nhiều tính từ điện ảnh vào prompt sẽ không giải quyết được ba vấn đề này.

Quy ước ưu tiên: **P0** = lỗi làm hỏng logic hoặc liên tục, cần sửa trước khi render phần liên quan; **P1** = ảnh hưởng lớn tới cảm xúc, nhịp và độ thuyết phục; **P2** = tinh chỉnh diễn xuất, hình ảnh, âm thanh.

**1. Những vấn đề cần sửa trước**

| Ưu tiên | Vị trí | Vấn đề có trong bản hiện tại | Hướng sửa |
|---|---|---|---|
| P0 | 05, 12–13, 32, 42–43, 49 | Khán giả được dạy Tê làm liệt, trông như chết. Sơn lại công khai giơ Tê, nói Hạ chờ 40 phút; Dũng và chính bà chủ xưởng vẫn tin anh chết. | Bỏ lời báo kế hoạch trước phản diện. Cho một phản diện nhận ra mánh và phá kế hoạch, hoặc viết lại mục đích dùng Tê. Cái chết giả không thể thành công chỉ vì những người biết thuốc bỗng quên quy luật. |
| P0 | 01.5, 11.5, 14.5–6, 33.6, 34.4, 52.1–3 | Đồng hồ đã mở ở cảnh 11 và 14, nhưng cảnh 33–34 nói chưa mở, cảnh 52 lại được dựng như lần đầu. Nó từng tích tắc ở cảnh 33 nhưng cảnh 52 nói dừng từ lúc lên dây đêm đó. | Chọn một lịch sử duy nhất. Khuyến nghị: ảnh Hạ ở mặt ngoài/nắp lưng, Sơn chỉ mở buồng mặt số ở cảnh 52; sửa toàn bộ cảnh trước để không mở nắp đó. Hoặc bỏ ý nghĩa “lần đầu” và viết cảnh 52 thành lần đầu anh thực sự xem giờ cùng Hạ. |
| P0 | 35–53 | 68 prompt có khóa Sơn mặc áo ô liu trong chuỗi mà kịch bản yêu cầu vest đen. | Tạo trạng thái riêng cho Sơn hiện tại mặc vest, tay trần; quy định hoa, dây đồng hồ, băng cổ tay theo từng đoạn. Đừng dùng khóa hiện tại ô liu hoặc khóa quá khứ có găng cho trạng thái này. |
| P0 | 51.5–53 | Khóa `HA_N` đổi Hạ sang áo trắng, jean ngay trên hải đăng; câu chuyện vẫn diễn ra liền sau lúc cô mặc váy xám bị giữ. | Giữ váy xám qua hết giải cứu và bắt giữ. Chỉ đổi đồ sau một chuyển cảnh ở đồn. “Được tự do” và “đã thay đồ” phải là hai trạng thái khác nhau. |
| P0 | 10.2, 18.5, 19.1, 51.5 | Sơn đã nhặt khăn rách ở tiệm hoa; Dũng lại có đúng khăn đó ở cảnh 18. Sau đó khăn xuất hiện trong tay Hạ do Mây đưa “ở cảng”, nhưng chưa có hành động trao; Hạ bị Kiên giữ suốt đoạn đó. | Chốt một chiếc khăn và đường đi từng lần đổi chủ. Có thể để Sơn nhặt một mảnh, Dũng giữ phần còn lại; đến cao trào chọn nơi trao khả thi. Không giải thích bằng một sự kiện chưa từng được dựng. |
| P0 | 17, 22, 25, 31, 34 | Khóa giải mã được giới thiệu rồi chưa có cảnh thực sự dùng. `LEDGER` mô tả sổ đen nhưng được gắn vào sổ đỏ. Cảnh 31 Sơn đặt sổ xuống mà chưa rõ lấy lại bằng cách nào. | Tách sổ đen/sổ đỏ/USB/khóa, quy định người giữ từng món; cho thấy thao tác mở phần dữ liệu khóa và thông tin mới thu được. |
| P0 | 43–48 | Tỉnh báo 5 phút nữa tới; cảnh 45 nói đã vào cảng; cảnh 48 lại mới tràn vào. Kiên giữ Hạ trên hải đăng hàng chục phút, trong khi Sơn được chờ tỉnh lại rồi đi cứu. | Viết một trục thời gian và dựng song song. Chốt lúc lực lượng đến, nhiệm vụ mỗi tổ, lý do chưa tiếp cận được con tin, và việc Kiên làm trong khoảng chờ. |
| P1 | 08.2, 31.6, 47.2 và các clip có gọi tên trong thoại | Cơ chế gắn tag chèn cả tên đầy đủ và `@Tag` vào trong câu phải được đọc, ví dụ “Thuốc giải nóng như trà Bà Hai Ngọc (@HaiNgoc).” | Gắn tag ở trường người nói và chỉ dẫn hình; giữ nguyên văn lời thoại bên trong câu. Không để thao tác khóa nhân vật tự viết lại giọng nói của nhân vật. |
| P1 | 05, 11, 25, 32, 34 | Hạn 7 ngày chủ yếu là quyết định cá nhân. Cảnh 25 nói Hạ sống thì không cần ngày 7, nhưng phim tiếp tục đếm như hạn bắt buộc. | Gắn ngày 7 với một sự kiện bên ngoài: Hạ bị chuyển đi, hồ sơ bị hủy, hoặc giao dịch cuối. Sau video Hạ, hạn phải khẩn cấp hơn thay vì mất ý nghĩa. |
| P1 | 08, 17, 23, 36 | Kiên mua hợp đồng để Sơn vào tù, rồi đổi ý muốn anh tự do; lý do đổi ý đang được kể để nối các cú lật. Bà Hai vừa muốn diệt Kiên vừa để Kiên mua chính sát thủ của mình. | Lập rõ mục tiêu, thông tin và lợi ích của từng phe ở từng thời điểm. Giữ một động cơ xuyên suốt của Kiên, chẳng hạn dùng hồ sơ và Hạ để ép Sơn làm việc. |
| P1 | 06, 15, 27, 36–54 | Hạ có nhiều ý nghĩa với Sơn nhưng ít hành động làm thay đổi tình thế. Cô chủ yếu là người xin, người bị giữ, người chờ. | Cho Hạ một lựa chọn có hậu quả: giấu manh mối trong video, nhận biết lối kỹ thuật hải đăng do từng sống ở đó, hoặc tạo khoảng trống để thoát tay Kiên. Phải gieo kỹ năng trước khi dùng. |
| P1 | 07, 11, 17–19, 29, 35, 43 | Mây nhìn thấy giấy tờ giả, súng và thuốc nhưng chờ khá lâu; sau đó rời thị trấn khi Dũng ở lại, rồi huy động dân vào khu vực có súng. | Cho Mây một kế hoạch điều tra và bảo vệ dân rõ. Quyết định đi tìm Hạ phải có đánh đổi được nhận biết. Để dân hỗ trợ quan sát, sơ tán, chặn lối; lực lượng có nhiệm vụ bắt giữ trực tiếp. |

**2. Lỗi hệ thống trong prompt và cách sinh**

Các con số dưới đây được kiểm tra trên 360 file hiện có, không suy ra từ vài cảnh mẫu:

- **360/360** prompt cùng ghi `16:9` và `2.39:1` mà không xác định rõ đâu là canvas, đâu là vùng hình. Chọn master 16:9 đầy khung hoặc 16:9 có vùng hình 2.39:1 và letterbox cụ thể. Bốn video FULL hiện có đều là 1280×720, 24 fps, khoảng 60,02 giây/cảnh; phép đo này chưa xác nhận bố cục bên trong hình.
- **360/360** prompt chia đúng ba mốc 0–3,5 / 3,5–7 / 7–10 giây. Nhịp chia đều đang phục vụ template hơn là diễn xuất. Một ánh nhìn có thể cần cả clip, còn một động tác khóa tay không cần ba góc máy khác nhau.
- **296** prompt bắt đầu bằng yêu cầu nối liền, không thấy cắt; bên dưới lại thường đổi tiêu cự, đổi góc hoặc đổi địa điểm. Tách “nối chuyển động” khỏi “cắt dựng có chủ đích”. Một clip mới không bắt buộc là một cú máy liên tục.
- **360/360** prompt yêu cầu giữ/đóng băng khung cuối 0,5 giây; **30** prompt nói đứng hình “kể cả gió”. Nếu làm đúng cả 360 lần thì có 180 giây hình bị giữ, dễ tạo nhịp khựng. Hãy kết bằng chuyển động nhỏ còn sống; lấy frame nối bằng công cụ, không bắt cả thế giới ngừng lại.
- Các lần cắt đen tự động theo chu kỳ đã được bỏ trong đợt cập nhật. Cần tiếp tục giữ nguyên tắc: cắt đen có lý do kể chuyện, không theo số thứ tự cảnh.
- **339** clip có khối chỉ dẫn thoại; **158** khối chứa nhiều lượt/câu đặt chung một mốc. Những clip như 09.6, 11.4, 13.4, 17.3, 19.5, 37.3, 50.3 cần nghe thử nhịp nói vì gom nhiều lời vào khoảng 3–3,5 giây. Đây không phải kết luận tất cả sẽ lỗi khẩu hình. Chia lượt thoại theo người nói và cho họ đủ thời gian phản ứng.
- Cách dùng ngoặc kép đang khác quy ước “không đặt thoại trong ngoặc kép” tại `FLOW_GUIDE.md:102,187–188`. Cần thống nhất quy cách nội bộ và thử một đoạn có thoại trước khi áp dụng hàng loạt; bản rà soát này không kiểm chứng tuyên bố kỹ thuật về model trong hướng dẫn đó.
- **33** clip trong cảnh 21–27 gọi Sơn là `in the past` dù đang diễn ra trong hành trình hiện tại. Mã trang phục và mã thời gian đang bị nhập làm một. Cần tách `timeline`, `costume`, `age`, `location`, `time_of_day`.
- Bộ phân loại dùng từ đơn nên hiểu sai “không chạy”, “kim không chạy”, “chạy rồi”. Cảnh **52.2** và **60.5** có thể bị gán máy quay rượt đuổi, whip pan và nhịp gõ nhanh vào cảnh đồng hồ/tái ngộ. Những cảnh cảm xúc quan trọng phải được chọn cách quay trực tiếp.
- Một setting đang áp cho cả sáu clip; nhiều chỗ nhân vật đi sang không gian mới nhưng prompt vẫn nối từ chỗ cũ. Ví dụ 01.2–4, 07.6, 09.6, 21.5, 26.5–6, 48.4–6, 58, 60. Không nên dò địa điểm từ chuỗi từ khóa khi có thể khai báo thẳng từng clip.
- Bảng màu “hiện tại nắng trắng / quá khứ đêm vàng” không đủ cho đêm hiện tại, bình minh, phòng trọ rạng sáng và hồi tưởng ban ngày. Giữ khác biệt sắc độ của hai tuyến thời gian nhưng vẫn khóa nguồn sáng thực tế của mỗi shot.
- Nhân vật được khóa trễ hơn lần đầu xuất hiện: **22.4** đã thấy Bà Hai nhưng tới 22.5 mới có khóa bà; **36.3** đã thấy Hạ nhưng không khai báo Hạ; **44.2** Dũng vác Sơn mà thiếu Sơn; **51.1** Hạ bò vào cửa nhưng thiếu Hạ. Tách người nhìn thấy trong hình và giọng ngoài hình, khai báo đúng từng nhóm.
- Hồ sơ và kịch bản chưa thống nhất lịch sử nhân vật. Kịch bản mới đã bỏ Sơn nhỏ và tuổi trẻ ở 28/38, nhưng `NHAN_VAT.md` vẫn kể Bà Hai nhặt Sơn năm 12 tuổi, đưa găng năm 20 và có ảnh Bà Hai trẻ. Chọn lịch sử nào thì cập nhật tất cả tài liệu theo lịch sử đó. Cảnh 60 “nhiều năm sau” vẫn dùng tuổi cũ; cần ảnh giai đoạn sau cho các gương mặt thấy rõ.

Nguồn gây phần lớn lỗi là `build_full_60_scenes.py`: `classify()` dò từ, `split_beats()` chia theo dấu câu, `shot_list()` chọn góc từ pool, và `get_setting_key()` dò setting. Một cụm như “không với hai phe” ở 42.3 bị đẩy thành hành động cuối clip; đó không phải thứ có thể quay. Mỗi shot phải mô tả điều khán giả nhìn/nghe được.

Đối chiếu lần cuối bằng cách chạy bản sao bộ sinh ở thư mục tạm cho thấy cả 360 prompt trùng bản sinh lại sau đợt cập nhật nguồn. `PRESERVED_SCENES` hiện rỗng; những chỉnh sửa riêng bổ sung sau này sẽ bị ghi đè nếu chỉ sửa clip rồi chạy lại bộ sinh. Nên sửa nguồn hoặc quản lý phần biên tập tay trước khi tái sinh. Đợt rà soát này chỉ tạo báo cáo, không ghi đè prompt trong workspace.

**3. Góp ý từng cảnh — Hồi 1**

| Cảnh | Ưu tiên | Cần tối ưu và cách xử lý |
|---|---|---|
| 01 — Ngày Thứ Nhất | P1 | Chuyến xe, quán, đường lên đồi và trong nhà bị ép thành một chuỗi nối liền. Dùng các cú cắt thiết lập địa lý. Giữ chi tiết Sơn chọn chỗ nhìn đường; gieo một dấu hiệu nguy hiểm cụ thể để mở phim có sức kéo hơn lời tự giới thiệu. |
| 02 — Hợp Đồng Cuối | P1 | Các từ hỏng ở clip 1/4 đã được sửa trong đợt cập nhật. Giữ cách Bà Hai đối xử như mẹ, nhưng giảm lời gắn nhãn “Bóng Ma”; cho một phản ứng nhỏ của Dũng thể hiện ghen với Sơn. Khóa vị trí ảnh Kiên và tay đẩy ảnh để nối được. |
| 03 — Khách Không Nhìn Biển | P1 | Giữ tư thế lưng quay biển vì đây là hành vi kể tính cách hiệu quả. Ba câu hỏi/đáp cần nhịp riêng. Cắt cảnh khi chuyển ra xe; lần đầu Mây nghi ngờ nên dựa vào một quan sát đủ đặc hiệu, không chỉ đôi giày. |
| 04 — Tiệm Hoa | P1 | “Ngày hôm sau” nhưng Hạ nói đã ba ngày: chốt số lần gặp. Dựng montage có cắt thay vì nối liền. Cho Hạ thấy Sơn làm một việc tử tế cụ thể để sự gần gũi có nền ngoài vẻ bí ẩn. |
| 05 — Sổ Đen | P0 | Sổ, USB, ba lọ Tê và súng đều xuất hiện như đã có sẵn, nhưng phim chưa cho thấy Sơn lấy chúng ở đâu. Gieo một đoạn lấy bằng chứng hoặc lời dẫn có hình tương ứng. Các lỗi thay từ và hai format tại clip 5 đã được sửa; vẫn cần kiểm tra lời giải thích Tê với cảnh 32. |
| 06 — Lời Xin Của Hạ | P1 | Hạ nhận ra anh mang súng mà gần như không có xung đột nội tâm. Thêm một nhịp cô ngừng gói hoa hoặc đặt điều kiện trước khi mời về biển. Chốt đồng hồ có ảnh gì từ lúc tặng và chiếc găng được tháo bên nào. |
| 07 — Mây Gõ Cửa | P1 | Căn cước nói 50, Sơn nói 45 có thể là hài khô nhưng cần rõ đây là giấy giả. Mây phát hiện giấy giả rồi chỉ theo dõi: thêm mục tiêu điều tra cụ thể. Clip 6 từ đồi xuống đồn phải là cắt cảnh. |
| 08 — Đêm Bị Gài | P1 | “Bắt tại trận” hiện thiếu một sự kiện phạm tội hay chứng cứ được gài tại hiện trường. Gieo thứ khiến Sơn thực sự bị quy kết. Theo dõi khẩu súng anh ném, vest anh cởi và găng đã mất để cảnh 10 không tự phục hồi quần áo. |
| 09 — Hai Người Lạ | P1 | Phản ứng bảo vệ người mới tới của ông Bảy cần một lý do nhỏ đã gieo từ trước. Chuyển quán → chợ → đồn bằng cắt có địa lý. Clip 6 có ba lượt thoại trong cùng một mốc, nên phân lại. |
| 10 — Tiệm Hoa Tan Hoang | P0 | Khăn được Sơn mang đi ở clip 6 nhưng sang cảnh 18 lại thuộc Dũng. Khóa đường đi khăn. Phân biệt điều Sơn tận mắt biết với điều anh suy đoán về Hạ; không khẳng định cô chết như sự thật khách quan. |
| 11 — Bảy Vạch | P0 | Mở đồng hồ ở clip 5 phá cảnh 52. Sau khi cắt sang đồi, clip 6 trở lại trong nhà cũng cần cắt; prompt clip 6 hiện vẫn giữ setting đồi dương. Rút bớt lời giải thích luật 7 ngày đã được nói trước. |
| 12 — Rừng Dương | P1 | Hai lần tiêm, hai lần ngã làm Tê thành lời giải quá tiện. Cho một đối thủ tạo khó khăn hoặc để một lần dùng thuốc không theo dự tính. Thể hiện rõ ai phát hiện hai người nằm và gọi Mây; tránh tiếng gọi không có nguồn. |
| 13 — Phòng Khám | P1 | Nhận diện ngay chất thuốc bằng một thao tác soi máu quá nhanh làm điều tra dễ dãi. Cho Linh nghi ngờ từ tiền sử một ca tương tự và xác nhận sau. Giới thiệu quy luật Tê như kiến thức về chất hư cấu, giữ nhất quán cho cao trào. |
| 14 — Hiên Nhà Gỗ | P0 | Giữ bố cục còng cạnh lọ vì nó tóm tắt lựa chọn của phim. Sửa cách Mây nhận ra Hạ mà không làm hỏng trạng thái đồng hồ. Sơn phải đưa một thông tin có thể kiểm chứng để Mây cân nhắc hợp tác, thay vì tin vì ảnh bạn. |
| 15 — Hạ Kể Về Biển | P1 | Đây là cảnh tốt để gieo Hạ biết cấu trúc hải đăng, phục vụ việc tự cứu ở cuối. Bớt những câu báo trước định mệnh quá rõ. Clip 6 về hiên nhà cần shot/khóa hiện tại riêng, không nhét một giây hiện tại vào khóa quá khứ. |
| 16 — Hải Đăng | P1 | “Xác đâu?” là cú hỏi đáng giữ, nhưng nó đã khiến khả năng Hạ sống khá rõ. Từ đây chuyển động lực sang tìm chứng cứ sống thay vì kéo dài bí ẩn cô chết hay chưa. Thiết lập đường lên, cửa phụ và ban công cho cao trào. |
| 17 — Mở USB | P0 | Chốt “khóa” là thiết bị chứa mã hay một món đồ dẫn tới mã; chìa khóa vật lý chưa tự giải thích được USB mã hóa. Cho Mây sao lưu bằng chứng và bố trí người giữ thị trấn. Giảm việc mọi manh mối đều được đọc thành lời. |
| 18 — Dũng Vào Thị Trấn | P0 | Sửa nguồn chiếc khăn. Gieo cách Dũng nhận lệnh hoặc đi về thành phố để lần xuất hiện cảnh 24 có nguyên nhân. Sự nhượng bộ trước Mây cần một lợi ích rõ của hắn, giúp phản diện vẫn nguy hiểm. |
| 19 — Khăn Lụa | P0 | Clip 2 vừa nói đã có bốn vạch vừa khắc thêm vạch thứ tư. Chỉ để ba vạch trước hành động hoặc bỏ lần khắc này. Mây cần nhận biết hậu quả của việc đi khi Dũng ở lại, thay vì để cảnh 29 giống một sơ suất bị quên. |
| 20 — Người Thứ Ba | P1 | Cho người gọi cung cấp một chi tiết chỉ người giữ Hạ mới biết, khiến Sơn có lý do nghe theo. Giọng Kiên phải đủ che danh tính nếu muốn giữ bí ẩn. Tránh kết bằng giải thích “có người thứ ba” khi hình và âm đã nói điều đó. |

**4. Góp ý từng cảnh — Hồi 2**

| Cảnh | Ưu tiên | Cần tối ưu và cách xử lý |
|---|---|---|
| 21 — Xe Đò Đêm | P0 | Tách trạng thái Sơn hiện tại mặc vest khỏi quá khứ. Clip 5 vào nhà vệ sinh trạm nghỉ cần cắt và setting riêng. Việc Mây nói mang hai còng phải được theo dõi đến cảnh 26; tránh tiếp tục sinh thêm còng theo nhu cầu. |
| 22 — Tiệm Lụa | P0 | Chìa “giữ sáu năm” xung đột với “được cho năm 20 tuổi” khi Sơn 45. Sổ đỏ cần prop riêng. Bà Hai xuất hiện ở clip 4 phải được khai báo ngay. Gieo lý do bà để họ mở két trước khi bật đèn: bà muốn trao đổi hay cố ý thả mồi? |
| 23 — Trà Của Bà Hai | P1 | “Má không giết. Má bán.” là câu nên giữ. Cắt bớt phần kể lại kế hoạch Kiên sẽ tiếp tục kể ở cảnh 36. Cần rõ vì sao bà cho Sơn rời đi với sổ có thể hại mình, thay vì chỉ ngồi yên vì phong cách. |
| 24 — Bãi Xe Ngầm | P1 | Dũng đã ở biển nên cần dấu nối cho việc hắn quay về kịp. Dựng một toàn cảnh để hiểu lối chạy và lan can. Chọn một hoặc hai đòn rõ thay vì nhiều đòn/cửa xe/súng/gậy trong cùng 10 giây; khóa cách hắn thoát còng sau đó. |
| 25 — Phòng Trọ | P0 | Giữ nhịp nghỉ và đau sau truy đuổi. Sửa câu “Hạ sống thì không cần ngày thứ bảy” theo hạn bên ngoài đã chọn. Sổ đỏ phải mở được dữ liệu mới; xác định Sơn đang cởi vest, còn găng hay đã tháo để khóa hình không tự mặc lại. |
| 26 — Xưởng Tê | P0 | Mây mang hai còng, đã dùng ở 23 và 24, nhưng clip 4 lại có “cái còng cuối cùng”. Chuyển một lần khống chế sang dây hoặc cho thấy lấy lại còng. Việc họ cần bằng chứng xưởng phải có giá trị mới; chuyển mái → xưởng → ghe → sông bằng shot rõ. |
| 27 — Video Của Hạ | P1 | Cảnh 23 đã xác nhận Hạ sống, nên video phải làm được hơn việc xác nhận lại: cho thấy vị trí, thời hạn, hoặc một manh mối Hạ cố gửi. Tách hình trong điện thoại khỏi người thật trên ghe, tránh khóa Hạ như đang đứng cùng Sơn. |
| 28 — Cánh Cửa Đầu Tiên | P0 | Bản mới đã bỏ “trẻ hơn 10 tuổi”, nhưng hồ sơ vẫn kể một quá trình từ 12/20 tuổi tới sát thủ lâu năm. Chốt lần đầu làm việc ở tuổi nào, thời điểm được cho găng và lý do tiếp tục đeo. Giữ cú giao đạn cho Mây vì nó là hành động lựa chọn rõ. |
| 29 — Thị Trấn Bị Chiếm | P1 | Đây nên là hậu quả trực tiếp của một quyết định trước, nhất là Mây rời đi. Cho Thành một hành động chống cự/bảo vệ dân trước khi bị trói để không chỉ là con tin. Khóa việc Dũng thoát còng và ai còn đeo phần còng nào. |
| 30 — Chợ Cá | P1 | Cần một toàn cảnh lối vào/lối ra rồi mới cận đòn. Khóa số tay sai bị khống chế/còn chạy. Dũng đang biết Kiên giữ Hạ: xác định hắn trung thành với ai để lời đe dọa không chỉ tiện cho cảnh. Giảm dùng Tê như kết thúc mặc định. |
| 31 — Bà Hai Ở Hải Đăng | P0 | Sơn đặt sổ xuống rồi nói sẽ mang sổ chiều mai: cần thấy ai nhặt/giữ nó. Lời “rồi Bóng Ma chết” đang báo trước kế cho người biết Tê; sửa theo phương án cao trào. Bà Hai phải có lý do cụ thể chấp nhận cuộc gặp hai phe. |
| 32 — Bốn Mươi Phút | P0 | Quy luật “hết thuốc thì dậy” ở 13 và “quá 40 phút là thật” ở đây chưa có cầu nối. Thuốc giải xuất hiện đúng lúc giải bài toán. Gieo từ trước và đơn giản hóa quy luật hư cấu; bỏ độ chính xác phút/nhịp tim như thể không thể sai. Chốt mục tiêu tác chiến ngoài việc Sơn ngã xuống. |
| 33 — Đêm Cuối Với Hạ | P0 | Đây là lần nhắc lời hứa/đồng hồ thứ ba với thông tin gần nhau. Giữ một chi tiết mới có trả lời ở cảnh 52, cắt lời lặp cảnh 06. Sửa câu “chưa mở”; bỏ một giây hiện tại cuối clip nếu không tách được khóa và shot. |
| 34 — Vạch Thứ Bảy | P0 | Bằng chứng đã được giao hết cho Mây, nên phải rõ hai trùm tưởng còn thứ gì ở Sơn để tới cảng. Chốt bản thật/bản sao. Làm rõ quan hệ giữa hạn 7 ngày, giờ tỉnh tới và giờ chuyển Hạ; gieo đủ vạch của những ngày Sơn ở thành phố. |
| 35 — Thị Trấn Thức Dậy | P1 | Không nên giới thiệu cả mạng người dân vào trận bằng một bài nói. Dựng montage nhiệm vụ cụ thể: sơ tán, tín hiệu, xe cứu người. Bác sĩ chuẩn bị tại phòng khám, ông Bảy tại xe, Sơn ở phố: cần setting riêng. Khóa vest tay trần. |
| 36 — Người Môi Giới Lộ Mặt | P1 | Sơn đã đoán Kiên từ cảnh 23 nên đây là đối mặt, không còn cú lật danh tính mạnh. Có thể cho Kiên đưa điều kiện mới để tăng sức nặng. Thêm khóa Hạ ở clip 3. Mây đã biết kế ở cảnh 32 nên sự tái mặt cuối cảnh cần nguyên nhân mới. |
| 37 — Điều Kiện | P0 | Câu “hắn tin tôi làm vì tiền” xung đột với việc Kiên biết Sơn làm vì Hạ. Sửa luận lý thương lượng. Đừng để kế hoạch phụ thuộc vào giả định Kiên tự mang con tin ra chỗ nguy hiểm; cho Sơn đòi kiểm chứng trực tiếp như điều kiện rõ từ trước. |
| 38 — Đôi Găng Đầu Tiên | P1 | Bản mới đã thay đứa trẻ bằng Sơn trưởng thành, giúp đơn giản hóa hình nhưng làm lệch hồ sơ mẹ nuôi từ năm 12 tuổi. Chốt lại lịch sử quan hệ. Rút hồi tưởng còn 20–30 giây hoặc chuyển một phần về 21 để không ngắt áp lực trước cảng; dùng cắt thời gian thay cho cú lia tự biến đổi nhiều năm. |
| 39 — Hoàng Hôn Cảng Cá | P0 | Vẽ hình học cầu cảng: hai lối ô tô, chợ, xe van, lối lên hải đăng, vị trí người quan sát. Chốt giờ tới của tỉnh. Một nguồn sáng thấp không tự tạo hai bóng dài ngược hướng; nếu muốn hình đó phải gieo hai nguồn sáng. |
| 40 — Hai Chiếc Xe | P1 | Cảnh 39 đã có hai xe đến; cảnh 40 cần thêm một thay đổi thực sự thay vì diễn lại việc bước xuống. Chốt khoảng cách hai phe và vị trí Hạ trong một toàn cảnh. Giữ các phản ứng riêng, tránh gom bốn nhân vật nói/cử động trong một shot nhỏ. |

**5. Góp ý từng cảnh — Hồi 3**

| Cảnh | Ưu tiên | Cần tối ưu và cách xử lý |
|---|---|---|
| 41 — Tam Giác | P1 | Sơn lần lượt chĩa súng vào hai bên dễ thành động tác trình diễn nếu không đổi thế trận. Chọn một lần nâng súng và một quyết định hạ súng có giá. Hạ cần phát tín hiệu/hành động đã gieo trước để tác động vào lựa chọn này. |
| 42 — Hợp Đồng Cuối Cùng | P0 | Sửa tận gốc việc giơ thuốc và báo 40 phút công khai. Clip 3 kết bằng “không với hai phe” là mệnh đề không thể quay. Giữ shot trên phản ứng của Hạ hoặc bàn tay Sơn; tách cử chỉ, phản ứng và ngã thành các nhịp có thời gian. |
| 43 — Bóng Ma Chết | P0 | Dũng biết thuốc mà vẫn kết luận chết là mắt xích yếu nhất. Kiên nói hợp đồng xong dù Bà Hai còn sống cũng không hợp điều kiện thuê. Viết cuộc tranh chấp từ mục tiêu cụ thể: ai giữ Sơn/bằng chứng/Hạ, ai vừa phản bội ai; cho kế Sơn gặp trở ngại thật. |
| 44 — Cảng Cá Nổ Tung | P0 | Súng đã được giơ lên nhưng hỗn chiến chuyển sang lưới/sào quá thuận lợi; cần bố trí khống chế có nguyên nhân nhìn thấy. Không quăng người bất động vào thúng như một đạo cụ hài. Giải thích lối xe Kiên thoát và chốt phút 15 bằng chuyển thời gian có chủ đích. |
| 45 — Phút Hai Mươi Lăm | P0 | Chờ từ phút 20 tới 25 mà Hạ chỉ được báo đang trên tháp khiến khẩn cấp bị đứng. Dựng song song với Hạ chủ động trì hoãn Kiên và lực lượng tìm đường tiếp cận. Bỏ con số mạch 3 nhịp/phút; chỉ cần thể hiện Linh chưa yên tâm và thời gian đang mất. |
| 46 — Dũng Đinh Vs Mây | P0 | Còng đã “gãy” nhưng đầu còn lại vẫn dùng được phải được định nghĩa: gãy phần nào, còn khóa nào. Cho thấy Dũng lần ra xe van bằng dấu vết, tránh tự tìm đúng chỗ. Giữ chi tiết Mây tận dụng còng của chính mình nhưng quay thành một chuỗi động tác đơn giản. |
| 47 — Tỉnh | P1 | Sơn tỉnh rồi lập tức lái xe và đánh tiếp làm cái giá dùng Tê nhẹ đi. Giữ yếu sức xuyên suốt và buộc anh dựa vào Mây/Hạ. Đặt tên cảnh rõ hơn như “Tỉnh Lại” để tránh nhầm tuyến công an tỉnh khi biên tập. |
| 48 — Đường Lên Hải Đăng | P0 | Khóa lại thời điểm tỉnh tới. Nón nên được đội trước khi xe chạy, tránh hai trạng thái trong một câu. Các shot ở cảng, đường, chân tháp, cầu thang và ban công cần cắt/setting riêng; clip 3 diễn ra dưới cảng nhưng bị bộ dò từ khóa gán setting hải đăng. |
| 49 — Bà Hai Bị Bắt | P1 | Chuyển cảnh này vào montage song song lúc Sơn lên tháp để không ngắt đối đầu. Câu “Má biết” phải khớp việc bà có bị lừa ở 43 hay không. Để bà tự tháo vòng là hành động kết thúc quyền lực; không cần nhiều câu giải thích thêm. |
| 50 — Hải Đăng: Kiên | P1 | “Ông chưa bắn ai” không đủ bảo đảm Sơn bước thẳng trước súng là lựa chọn khôn ngoan. Cho Hạ tạo khoảng hở cụ thể bằng kiến thức hải đăng hoặc một động tác đánh lạc hướng. Bông ly đã rơi ở 42.5 nên không thể còn nguyên trong túi để Hạ nhìn ở 50.4. |
| 51 — Tay Không | P0 | Không đổi Hạ sang đồ trắng giữa trận; sửa nguồn khăn xanh và khai báo Hạ ngay clip 1. Thay việc “váy trơn nên thoát” bằng động tác cô chủ động tạo ra. Làm rõ khi Sơn yếu thì Hạ giúp phần nào để chiến thắng thuộc về cả hai. |
| 52 — Mở Đồng Hồ | P0 | Chỉ có sức nặng sau khi sửa lịch sử đồng hồ. Gán cách quay trực tiếp, không dùng phân loại theo chữ “chạy”. Giữ thời gian im trước tiếng tích tắc. Chốt 31 vạch tương ứng mốc bị bắt nào; đừng thêm số chính xác khi lịch toàn phim chưa khóa. |
| 53 — Ngày Thứ Bảy Không Chạy | P1 | Giữ Sơn chủ động đưa tay. Hạ nên hiểu và chấp nhận lựa chọn, thay vì chỉ định cản rồi bị lắc đầu. Thành “bật nhầm” hải đăng dễ làm nhẹ kết cảm xúc; gieo việc sửa đèn từ trước hoặc cho Hạ/Mây bật có chủ đích. |
| 54 — Lời Của Hạ | P1 | Phần kể bị giữ chủ yếu xác nhận thông tin đã biết. Rút lời khai, giữ một chi tiết mới chứng minh Hạ tự bảo vệ mình hoặc giúp phá án. Thống nhất xưng hô “tao/mày” với Mây; giữ đồ thay sau một shot chuyển thời gian rõ. |
| 55 — Lời Khai | P1 | Đây là giá đạo đức của phim, cần giữ. Cho thấy Sơn chịu trách nhiệm với một nạn nhân/việc cụ thể bằng lời khai và phản ứng, thay vì mọi tội lỗi thành hình tượng “cánh cửa”. Tránh dùng câu đùa để hóa nhẹ hậu quả ngay sau lời nhận tội. |
| 56 — Sổ Đen Lên Báo | P1 | Thuốc giải không còn là tâm điểm nên bỏ lần nhắc 38 phút. “Không bấm dừng” nhưng đồng hồ vẫn dừng ở 38 là mâu thuẫn. Quyết định có chuyển POV sang Mây hay giữ Sơn là người dẫn; nếu đổi, thiết lập chủ đích thay vì xuất hiện đột ngột. |
| 57 — Hạ Và Mây | P1 | Giữ việc Hạ tự chọn ở lại và mở sạp hoa vì nó trả lại mục tiêu đời riêng. Bớt nhắc lại kẹp tóc/khắc vạch/đếm. Một quyết định thực tế của Hạ có thể thay cho thêm một câu khẩu hiệu về chờ đợi. |
| 58 — Xe Chở Phạm | P1 | Setting đang là quán bờ kè trong khi nhân vật ở trong xe: tạo nội thất xe riêng. Đường xe đi qua cầu cảng, quán, đồn và ngã ba phải khớp bản đồ. Giữ một hình tiễn biệt mạnh, giảm các lượt chào giống nhiều lần kết phim. |
| 59 — Bảy Vạch Trên Khung Cửa | P1 | Cảnh có hình đẹp nhưng đang thêm một kết sau lời khai, bản tin, chia tay và xe rời đi. Rút thành một đoạn ngắn. Cho vạch mới của Hạ mang nghĩa xây đời sống, không chỉ chuyển cô từ nhà giam sang chờ người khác. |
| 60 — Chuyến Xe Bình Minh | P0 | Chiếc đồng hồ thứ hai y hệt chưa được gieo, dễ làm khán giả nghĩ lỗi đạo cụ hơn là kết mở. Bỏ hoặc giới thiệu quan hệ hai chiếc từ trước. Khóa tuổi sau nhiều năm; bỏ camera rượt đuổi ở clip 5. Tựa phim cuối cần làm ở hậu kỳ vì prompt đồng thời cấm chữ trên hình. |

**6. Điều chỉnh nhịp phim để thành một mạch hoàn chỉnh**

Không nên buộc mọi đơn vị kể chuyện dài đúng một phút. Có thể giữ 360 clip như đơn vị sản xuất, nhưng dựng cảnh dài/ngắn theo biến chuyển: cuộc đối đầu cần được ở lại đủ lâu, một manh mối chỉ cần một insert. Tránh để mỗi phút đều mở lại bằng thiết lập không gian rồi đóng bằng câu móc.

Một phương án phân bổ 60 phút để tham khảo:

| Phần | Thời lượng | Nhiệm vụ |
|---|---:|---|
| Đến Hòn Sóng, lời hứa với Hạ, bị truy tìm | 0–12 phút | Cho khán giả hiểu Sơn muốn gì, nguy hiểm gì đang tới và tại sao 7 ngày có nghĩa. |
| Mây hợp tác, về thành phố, lấy bằng chứng và tín hiệu Hạ | 12–28 phút | Mỗi cuộc điều tra tạo thông tin mới và một cái giá. |
| Hòn Sóng chịu hậu quả, thương lượng hai phe, chuẩn bị trao đổi | 28–39 phút | Đẩy nhân vật vào lựa chọn không thể tiếp tục làm sát thủ. |
| Cảng cá, kế hoạch gặp sự cố, cứu người, hải đăng | 39–53 phút | Tăng áp lực liên tục; dựng song song thay vì chờ hết cảnh mới quay lại tuyến kia. |
| Nhận trách nhiệm và hậu truyện | 53–60 phút | Chọn ít điểm kết, dành một khoảng lặng thật cho cái giá của Sơn và lựa chọn của Hạ. |

Nên gộp/rút thông tin trùng giữa 06–15–33, 17–23–36, 32–37 và 54–57–59. Dùng thời gian lấy lại để tăng vai trò Hạ, làm rõ bằng chứng bị đánh cắp, và cho đối thủ một lần thực sự phá kế Sơn.

**Một hướng sửa cao trào giữ được phần lớn chất liệu hiện có:**

1. Ở 34–37, chốt giao dịch: Sơn đòi thấy Hạ trực tiếp; hai phe tới vì mỗi phe cần một thứ cụ thể. Phân biệt bằng chứng Mây đã giữ với thứ phản diện tin Sơn còn nắm.
2. Ở 42, bỏ việc giơ thuốc và báo 40 phút cho cả cảng. Nếu vẫn giữ cái chết giả, phải trình bày đó là một canh bạc có khả năng bị lộ, không phải mẹo chắc thắng.
3. Ở 43, Kiên hoặc Dũng nhận ra dấu hiệu Tê. Kế Sơn hỏng một phần; Bà Hai có lựa chọn thực sự giữa giữ “món hàng” và bảo vệ đứa con. Hai phe xung đột vì lợi ích và phản bội, không vì tự tuyên bố một hợp đồng chưa làm là hoàn tất.
4. Ở 44–47, Mây cứu được Sơn nhưng để mất tuyến Hạ. Dựng đồng thời bác sĩ, lực lượng khống chế cảng và Hạ trì hoãn Kiên. Mỗi tuyến thay đổi tình thế ở tuyến khác.
5. Ở 48–51, Sơn vẫn yếu. Hạ dùng điều đã gieo ở 15–16 để tạo khoảng trống; Sơn lựa chọn khống chế thay vì giết. Cứu người là kết quả của hợp tác, không phải một người vừa hồi phục đột nhiên giải quyết hết.
6. Ở 52–53, đồng hồ và chiếc còng trả lời lời hứa: anh đã hết nghề nhưng vẫn phải chịu trách nhiệm. Đây là đỉnh cảm xúc nên giữ đủ khoảng lặng.

Đây là phương án biên tập đề xuất; cần chọn dứt khoát trước khi viết lại prompt liên quan, vì thay cao trào sẽ tác động các cảnh gieo Tê và các lời thoại báo trước.

**7. Chuẩn prompt nên áp dụng sau khi chốt kịch bản**

Mỗi clip cần một nhiệm vụ rõ: nhân vật muốn làm gì, gặp trở ngại gì, kết thúc khác lúc bắt đầu ra sao. Với clip thuần cảm xúc, biến chuyển có thể chỉ là quyết định nhìn lại người kia; không cần thêm chạy, cầm đồ hoặc quay chậm để đủ hành động.

Khai báo tách biệt: thời gian truyện, giờ trong ngày, địa điểm, người trong hình, giọng ngoài hình, trang phục, đạo cụ đang giữ, trạng thái đầu và cuối. Camera phải phục vụ thông tin cảnh; không bốc góc từ một danh sách theo từ khóa.

Ví dụ thay cho cách quay hiện tại ở **60.5**, sau khi đã bỏ chiếc đồng hồ thứ hai và chọn đúng ảnh Hạ ở giai đoạn sau:

```text
[FORMAT]
10 seconds. 16:9 full-frame. Photorealistic live-action Vietnamese coastal drama.

[CONTINUITY]
Present timeline, years after the main story, dawn.
Use the approved older-Hạ reference and the costume established in clip 60.1.
Location: Hạ's flower stall at the fish-market entrance.
Cut from the previous clip to Hạ. The arriving man stays off screen.

[SHOT]
0–10s: One locked medium close-up, 50mm lens, camera inside the flower stall.
Hạ is arranging white lilies. The coach engine recedes outside.
She pauses with one stem in her hand and looks toward the doorway.
Let recognition develop gradually. Her hand relaxes; she sets the stem down.
End with her still looking toward the doorway, breathing naturally.

[LIGHT AND SOUND]
Soft dawn light from the doorway, cool sea fill, natural skin tones.
Coach engine fading into sea wind and footsteps approaching on sand.
No dialogue in this clip. No score until the final pause.

[EXCLUDE]
No text, subtitles or logos. No additional watch. No slow motion or freeze frame.
```

Đây là mẫu ý đồ quay, chưa phải prompt đã nạp vào pipeline. Lời “Hết việc chưa?” có thể giữ ở clip 60.6; tiếng bước chân và phản ứng Hạ đủ nối cảm xúc qua cú cắt.

Về âm thanh, cần một bản thiết kế xuyên phim: giọng Sơn cố định, âm biển của Hòn Sóng, tiếng tích tắc chỉ xuất hiện khi có ý nghĩa, và các đoạn J-cut/L-cut để thoại/tiếng nền đi qua mối cắt. Không để mỗi clip tự chọn một nhạc cụ, một bass hoặc một tiếng nền ngẫu nhiên. Những câu như “anh nhớ mùi xưởng” cần đổi thành biểu hiện thấy/nghe được hoặc một hồi tưởng có chủ đích.

**8. Thứ tự thực hiện đề xuất**

1. Chốt logic Tê, hợp đồng Kiên/Bà Hai, hạn 7 ngày và vai trò chủ động của Hạ.
2. Lập bảng liên tục cho 60 cảnh: ngày/giờ/tuổi/đồ/đồng hồ/khăn/sổ/USB/còng/súng/hoa/băng tay. Chốt một bản đồ Hòn Sóng.
3. Sửa kịch bản tổng cùng hồ sơ và khóa nhân vật. Rút các cảnh nhắc lại thông tin, chia nhịp theo ý đồ dựng.
4. Sửa bộ sinh hoặc chuyển các cảnh quan trọng sang shot viết tay có quản lý. Giữ nguyên các chỉnh sửa hiện có cho tới khi đã đối chiếu và thay thế có chủ đích.
5. Dựng thử ba đoạn để kiểm tra cách kể: 01–03 cho địa lý/nhân vật, 22–24 cho điều tra/hành động, 41–43 cho cao trào. Nghe thoại và xem điểm nối trong chuỗi, không chỉ xem từng clip riêng.
6. Sau khi ba đoạn hoạt động, mới render tiếp phần còn lại; dựng âm thanh và nhịp toàn phim trước khi cắt bản dọc. Các cảnh nhiều người ở hai phía như 40–43 nên có phương án reframe riêng cho 9:16, không mặc định crop giữa.

**Các nguồn nội bộ chính để đối chiếu**

- [Kịch bản 60 cảnh](/Users/iseul-a/Documents/METACREW/TikTokSeries/ke-song-sot/KICH_BAN_60_PHUT.md)
- [Khóa nhân vật và đạo cụ](/Users/iseul-a/Documents/METACREW/TikTokSeries/ke-song-sot/FLOW_PROMPTS.md)
- [Hồ sơ và biến thể nhân vật](/Users/iseul-a/Documents/METACREW/TikTokSeries/ke-song-sot/NHAN_VAT.md)
- [Bộ sinh prompt](/Users/iseul-a/Documents/METACREW/TikTokSeries/ke-song-sot/build_full_60_scenes.py)
- [Ví dụ khóa trang phục xung đột tại 42.3](/Users/iseul-a/Documents/METACREW/TikTokSeries/ke-song-sot/canh-42/clip-3.md)
- [Ví dụ đổi trạng thái Hạ tại 51.5](/Users/iseul-a/Documents/METACREW/TikTokSeries/ke-song-sot/canh-51/clip-5.md)
- [Ví dụ máy quay sai ý cảnh tại 60.5](/Users/iseul-a/Documents/METACREW/TikTokSeries/ke-song-sot/canh-60/clip-5.md)
