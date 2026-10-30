# Kẻ Sống Sót: Bóng Ma — bản 3

Đã biên tập lại 60 cảnh / 360 prompt cho một phim liền mạch. Giữ chín danh tính hiện có trên Flow, thoại tiếng Việt miền Nam, hình người thật neo-noir, master 16:9 đầy khung.

- [Kịch bản hiện hành](KICH_BAN_60_PHUT.md): mỗi cảnh có mục đích, mỗi clip có đầu / hành động mới / cuối.
- [Bảng nối 359 điểm ghép](BANG_NOI_CLIP.md): gồm cả 59 ranh giới giữa các cảnh, ghi cách cắt và nối âm.
- [Khóa nhân vật, trang phục và đạo cụ](FLOW_PROMPTS.md).
- [Hồ sơ chín nhân vật](NHAN_VAT.md).
- [Các thay đổi bản 3](CAP_NHAT_V3.md).
- [Nguồn phân cảnh có cấu trúc](PHAN_CANH_V3.json): chỉnh nội dung tại đây để tái sinh không mất công biên tập.

## Điều gì thay đổi trong câu chuyện

Sơn có bảy ngày trước khi Hạ bị chuyển đi bằng tàu. Kiên muốn bịt lời người biết quá nhiều, Bà Hai muốn lấy lại quyền kiểm soát. Cuộc trao đổi ở cảng bị phản bội; thuốc Tê hư cấu do Dũng sử dụng gây bất động và được cả hai phe nhận ra. Hạ để lại dấu qua khăn, video và cửa kỹ thuật. Mây dẫn lực lượng cứu người. Sơn cứu cả Kiên rồi tự nhận còng.

Đồng hồ duy nhất chỉ mở lần đầu ở 52.2. Hai mảnh khăn cùng một nguồn và có đường giao nhận. Hạ giữ váy xám qua hết hải đăng, thay đồ tại đồn. Sổ gốc và bản sao phân biệt rõ. Hạn ngày bảy và các vị trí hỗ trợ có nguyên nhân nhìn thấy được.

## Cách tạo và dựng

360 clip vẫn là các đơn vị sản xuất mười giây. Trong đó có 38 lần nối chính xác frame trong cùng cú máy; 321 mối ghép còn lại là cú cắt biên tập có chủ đích. Một clip một camera setup, không tự chia ba góc và không giữ đứng hình nửa giây ở đuôi.

- **CONTINUE:** dùng frame cuối clip trước làm start frame, tiếp hành động ngay, không phát lại đoạn kết hoặc lời vừa nói.
- **CUT / OPEN / MATCH / J / L:** dùng Ingredients và reference của shot mới. Đừng ép start frame cũ sang nơi hoặc thời gian mới. Match cut là cắt hình, không biến hình.
- **Shot chỉ có người nền:** không đính mặc định bốn nhân vật chính; runner dùng text-to-video khi không chỉ định reference.
- **J/L-cut:** mix khoảng 0,25 giây âm địa điểm trước/sau trên timeline; model chỉ tạo một shot mới. Dùng ambience xuyên cảnh và một phần nhạc chung ở hậu kỳ.
- **Khung hình sạch:** mọi prompt cấm logo đài truyền hình hoặc kênh ở góc hình, watermark, chữ chạy tin tức, lower-third, biểu tượng LIVE/REC và timestamp. Validator chặn chữ TV/tin tức/truyền hình trong dữ liệu cảnh. Khi duyệt render, soi bốn góc khung; thấy logo hoặc chữ thì tạo lại clip.
- Mỗi prompt đã ghi đầu và cuối cụ thể, vị trí/trang phục/đạo cụ. Kiểm tra ghép đôi sau render, nhất là 40–43 và 50–53. Bản dọc cần reframe riêng cho cảnh nhiều người hai phía.

```bash
python3 build_full_60_scenes.py
python3 build_full_60_scenes.py --check
python3 -m unittest discover -s . -p 'test_prompts_v3.py'
```

`build_full_60_scenes.py` là lệnh tương thích gọi bộ biên dịch mới `build_prompts_v3.py`. Nguồn duy nhất là JSON; README cảnh, caption, kịch bản, bảng nối và các khóa được sinh đồng bộ. Không sửa riêng một prompt rồi tái sinh mà bỏ quên cập nhật nguồn.

## Trạng thái render

Đợt này chỉnh kịch bản/prompt, chưa chạy tạo video. Các video trong `output_videos/` giữ nguyên và không được xem là video bản 3 đã kiểm duyệt. Dùng `RENDER_MANIFEST_V3.json` để đối chiếu hash prompt khi tạo lại, tránh trộn hình cũ với kịch bản mới.

Các UUID danh tính đã có được giữ nguyên. Trước khi render, kiểm tra reference đúng biến thể tuổi/đồ cho hồi tưởng 25 năm trước và cảnh nhiều năm sau; danh sách và prompt ảnh nằm trong NHAN_VAT.md. Không có UUID biến thể mới được giả định đã tạo.

Bản trước khi chỉnh được lưu đầy đủ trong [bản sao trước v3](revisions/before_v3_20261030_143044.zip). [Báo cáo đánh giá cũ](DANH_GIA_TOI_UU.md) giữ làm lịch sử, không phải mô tả lỗi đang tồn tại của bản 3.
