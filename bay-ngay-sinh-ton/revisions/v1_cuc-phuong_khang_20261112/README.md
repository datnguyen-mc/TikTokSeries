# Bảy Ngày Sinh Tồn (Seven Days in the Stone Age) (24 Cảnh × 4 Clips × 15s = 24 Phút)

- **Không có người dẫn chuyện:** 100% lời thoại do nhân vật nói trên hình — cả 96 clip là thoại khớp khẩu hình. Giọng gốc của mỗi nhân vật (tuổi, chất giọng) giữ nguyên văn ở mọi clip để Omni không đổi người nói.
- **Nhịp giọng theo cảnh:** mỗi lượt thoại có nhịp riêng nối sau giọng gốc — **nhanh** (cãi vã, hoảng hốt, rượt đuổi, khoe khoang; tốc độ ×1.2), **vừa** (trò chuyện thường), **chậm** (xúc động, thú nhận, câu chốt lặng người; tốc độ ×0.9). Khung thoại tính theo nhịp nên câu chậm ít chữ hơn. Cả phim: 106 lượt nhanh, 108 lượt vừa, 65 lượt chậm.
- **Thoại nhân vật (Lip-Sync):** clip thoại chỉ mô tả giọng của người nói, không có người dẫn chuyện; mặt và môi người nói luôn thấy rõ.
- **Mật độ:** 96 clips × 15s, tất cả là clip thoại (9 clip có hai lượt thoại); lời nói nằm trong khung riêng bắt đầu từ 0.4s (xem cột *Khung thoại*).
- **Cách tạo trên Flow (runner tự chọn):** 18 clip nối khung cuối (Frames — cùng bối cảnh, không có nhân vật mới), 78 clip ảnh nhân vật (Ingredients), 0 clip chỉ text. Tắt nối khung: `FLOWKIT_CHAIN_LAST_FRAME=0`.
- **Hậu kỳ runner:** không có clip VO nên runner không tăng tốc giọng clip nào; tốc độ nói nằm trong prompt (nhịp từng lượt) để khớp khẩu hình.
- **Màu phim & ánh sáng:** Natural motivated light: clear green-gold afternoon sun through the jungle canopy and warm lamp light in the present day; misty dawn light, dappled midday sun, warm ember firelight inside the cave and cool blue storm light with white lightning flashes in the Stone Age; shadows stay soft, never murky.
- **Nguồn dữ liệu:** `PHAN_CANH_OMNI.json` → `python3 flowkit/scripts/build_omni_horror_prompts.py bay-ngay-sinh-ton` sinh lại toàn bộ clip, README, kịch bản.

## Danh Sách 24 Cảnh (96 Clips × 15s)

| Cảnh | Tiêu Đề | Thời Gian | Đường Dẫn |
|---|---|---|---|
| **Cảnh 01** | Five-Star Survival (Sinh tồn năm sao) | Chiều, rừng Cúc Phương ngày nay (00:00–01:00) | [`canh-01/`](canh-01/README.md) |
| **Cảnh 02** | Busted (Bị bóc phốt) | Tối, nhà nghỉ ven rừng (01:00–02:00) | [`canh-02/`](canh-02/README.md) |
| **Cảnh 03** | The Cave of Hands (Đêm giông trong hang Bàn Tay) | 23:00 (02:00–03:00) | [`canh-03/`](canh-03/README.md) |
| **Cảnh 04** | No Roads (Rừng không có đường) | Sáng ngày 1, hơn một vạn năm trước (03:00–04:00) | [`canh-04/`](canh-04/README.md) |
| **Cảnh 05** | Day One: Water and Fire (Ngày 1: Nước và lửa) | Trưa (04:00–05:00) | [`canh-05/`](canh-05/README.md) |
| **Cảnh 06** | The Boy on the Rock (Cậu bé trên tảng đá) | Chiều ngày 1 (05:00–06:00) | [`canh-06/`](canh-06/README.md) |
| **Cảnh 07** | The Cave With No Hands (Hang chưa có bàn tay) | Hoàng hôn ngày 1 (06:00–07:00) | [`canh-07/`](canh-07/README.md) |
| **Cảnh 08** | Day Two: Food That Doesn't Run (Ngày 2: Đồ ăn không biết chạy) | Sáng, khe suối đá (07:00–08:00) | [`canh-08/`](canh-08/README.md) |
| **Cảnh 09** | Day Three: The Fire Dies (Ngày 3: Lửa chết) | Đêm mưa đến rạng sáng (08:00–09:00) | [`canh-09/`](canh-09/README.md) |
| **Cảnh 10** | Day Four: Boiling Water in Bamboo (Ngày 4: Nước sôi trong ống tre) | Trưa đến đêm (09:00–10:00) | [`canh-10/`](canh-10/README.md) |
| **Cảnh 11** | Day Five: Spear vs. Fish Trap (Ngày 5: Cái giáo và cái lờ) | Sáng đến trưa, bãi suối (10:00–11:00) | [`canh-11/`](canh-11/README.md) |
| **Cảnh 12** | Night Five: The Seeing Stone (Đêm 5: Hòn đá có mắt) | Đêm, bên bếp lửa (11:00–12:00) | [`canh-12/`](canh-12/README.md) |
| **Cảnh 13** | Day Six: Roar Doesn't Return (Ngày 6: Roar không về) | Sáng sớm, cửa hang và rừng già (12:00–13:00) | [`canh-13/`](canh-13/README.md) |
| **Cảnh 14** | The Sinkhole (Hố sụt) | Trưa ngày 6 (13:00–14:00) | [`canh-14/`](canh-14/README.md) |
| **Cảnh 15** | Muddy Water (Nước đục) | Chiều ngày 6, bờ suối trên đường về (14:00–15:00) | [`canh-15/`](canh-15/README.md) |
| **Cảnh 16** | Nobody Believes (Không ai tin) | Chiều muộn ngày 6, hang dưới (15:00–16:00) | [`canh-16/`](canh-16/README.md) |
| **Cảnh 17** | Flood Night (Lũ đêm) | Đêm ngày 6 (16:00–17:00) | [`canh-17/`](canh-17/README.md) |
| **Cảnh 18** | Three Million and One Boy (Ba triệu người và một thằng nhóc) | Đêm lũ (17:00–18:00) | [`canh-18/`](canh-18/README.md) |
| **Cảnh 19** | Day Seven: The First Hand (Ngày 7: Bàn tay đầu tiên) | Bình minh (18:00–19:00) | [`canh-19/`](canh-19/README.md) |
| **Cảnh 20** | Snail's Seeing Stone (Hòn đá có mắt của Snail) | Trưa đến chiều ngày 7 (19:00–20:00) | [`canh-20/`](canh-20/README.md) |
| **Cảnh 21** | Storm on the Seventh Evening (Giông chiều thứ bảy) | Tối ngày 7 (20:00–21:00) | [`canh-21/`](canh-21/README.md) |
| **Cảnh 22** | Return (Trở về) | Sáng sớm, hang Bàn Tay ngày nay (21:00–22:00) | [`canh-22/`](canh-22/README.md) |
| **Cảnh 23** | The Video With No Acting (Video không diễn) | Một tuần sau, hiên nhà nghỉ (22:00–23:00) | [`canh-23/`](canh-23/README.md) |
| **Cảnh 24** | Fire-Maker (Người làm ra lửa) | Sáng, hang Bàn Tay ngày nay và hơn một vạn năm trước (23:00–24:00) | [`canh-24/`](canh-24/README.md) |
