# 🏚️ CĂN NHÀ ÂM DƯƠNG — Phim AI Kinh Dị Tâm Linh 15 Phút

> **Nguồn gốc:** Truyện ma "Căn Nhà Âm Dương" — Kênh HẸM Truyện Ma, tác giả Thu Thảo, MC Đình Soạn kể
> **Thể loại:** SUPERNATURAL_FOLK_HORROR | Kinh dị tâm linh làng quê Bắc Bộ
> **Thời lượng:** ~15 phút (15 cảnh × 6 clip × 10s = 90 clips)
> **Phong cách:** 80% Người dẫn chuyện VO (giọng Bắc trầm lạnh) + 20% Thoại nhân vật bất ngờ
> **Định dạng:** 16:9 Landscape | Google Flow Omni 10s (`omni_flash`)

## 📖 Tóm Tắt

Bình (21 tuổi, sinh viên) sa vào bẫy đầu tư tiền ảo, nợ hơn 400 triệu đồng. Trốn khỏi thành phố, cậu về căn nhà hoang của ông nội ở một ngôi làng vùng đồng bằng Bắc Bộ. Căn nhà bỏ hoang gần 20 năm — và sau vụ tai nạn thảm khốc cướp đi 6 mạng người ngay trước cổng, nó đã trở thành nơi trú ngụ của vong hồn. Đêm đêm, Bình gặp những chuyện kinh hoàng: bàn tay ma thò qua màn, vết bầm xuất hiện trên cổ tay rồi biến mất, bóng trắng lượn lờ. Cuối cùng, vong ông nội hiện ra tiết lộ sự thật — và Bình phải gọi bố về chuộc lỗi với người đã khuất.

## 👥 Nhân Vật

| Tag | Nhân vật | Mô tả |
|-----|----------|-------|
| `@Binh` | Bình | SV 21 tuổi, gầy nhợt, tóc rối, ba lô đen |
| `@BaPhuong` | Bà Phượng | Mẹ Bình, GV về hưu 50 tuổi, nhân hậu |
| `@OngQuan` | Ông Quân | Bố Bình, nhân viên VP 55 tuổi, cộc cằn |
| `@OngBay` | Ông Bảy | Nông dân hàng xóm 60 tuổi, hiền hậu |
| `@Cuong` | Cường | Con ông Bảy, thợ hàn 18 tuổi, vạm vỡ |
| `@VongCuXa` | Vong Cụ Xá | Ông nội Bình, vong linh bán trong suốt |
| `@VongLa` | Vong lạ | Vong tai nạn, mặt méo mó, mắt đen ngòm |

## 🎙️ Voice Lock

| ID | Mô tả |
|----|-------|
| `VOICE_LOCK_NARRATOR_CNHADG` | Giọng nam chuẩn miền Bắc 40 tuổi, trầm lạnh, kể chuyện ma đêm khuya |
| `VOICE_LOCK_BINH_CNHADG` | Giọng nam trẻ 21 tuổi, run rẩy lo lắng, chuẩn Bắc |
| `VOICE_LOCK_PHUONG_CNHADG` | Giọng nữ 50 tuổi, ấm áp nghẹn ngào, chuẩn Bắc |
| `VOICE_LOCK_QUAN_CNHADG` | Giọng nam 55 tuổi, khàn cộc cằn, chuẩn Bắc |
| `VOICE_LOCK_BAY_CNHADG` | Giọng nam 60 tuổi, hiền hòa nông dân, chuẩn Bắc |
| `VOICE_LOCK_CUXA_CNHADG` | Giọng nam già, khàn đục ma quái, chuẩn Bắc |

## 📁 Cấu Trúc

```
can-nha-am-duong/
├── README.md
├── canh-01/ ... canh-15/    (mỗi thư mục có clip-1.md ... clip-6.md)
├── character_refs/           (ảnh tham chiếu nhân vật)
├── exported_frames/          (khung hình cuối mỗi clip)
└── output_videos/            (video MP4 đầu ra)
```

## 🛠️ Chạy Pipeline

```bash
cd /Users/iseul-a/Documents/TikTokSeries
./flowkit/venv/bin/python flowkit/runners/can_nha_am_duong.py
```

