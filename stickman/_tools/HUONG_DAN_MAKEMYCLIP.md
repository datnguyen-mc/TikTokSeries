# MakeMyClip Editor + MCP: dựng phim chuyên nghiệp

MakeMyClip Editor (github.com/MakeMyClip/editor, MIT) là trình dựng phim chạy bằng FFmpeg mà Claude điều khiển qua MCP. Nó cắt, ghép, chuyển cảnh, thêm chữ và phụ đề, và xuất dự án cho **DaVinci Resolve / Final Cut Pro (FCPXML)** và **Premiere Pro (XML + SRT)**. Mọi thứ chạy trên máy bạn, không cần tài khoản hay API key.

## 1. Cài vào Claude Desktop (một lần, khoảng 3 phút)

1. Cài FFmpeg trên Mac. Mở Terminal và gõ:
   ```bash
   brew install ffmpeg
   ```
   Nếu chưa có Homebrew, cài theo hướng dẫn tại https://brew.sh trước.
2. Bấm đúp vào file **`makemyclip-editor.mcpb`** trong thư mục này (bản 0.4.2), hoặc kéo nó vào cửa sổ Claude Desktop, rồi bấm **Install**.
3. Trong phần cài đặt của extension, chỉnh **Media folder** thành:
   ```
   /Users/iseul-a/Documents/TikTokSeries/stickman
   ```
   Editor chỉ đọc và ghi trong thư mục này, nên các clip 01–06 đều dùng được ngay.
4. Bước này không bắt buộc, chỉ cần khi muốn Claude tự nghe và tạo phụ đề từ giọng nói:
   ```bash
   brew install whisper-cpp
   ```
   Tải model đa ngôn ngữ (có tiếng Việt) **ggml-small.bin** từ https://huggingface.co/ggerganov/whisper.cpp, rồi chọn file đó ở mục **Whisper model**. Lưu ý: model `.en` chỉ nghe được tiếng Anh.
5. Hỏi Claude: **"is my setup OK?"**. Claude sẽ chạy lệnh `doctor` và báo cần sửa gì.

## 2. Gói dựng chuyên nghiệp của mỗi clip (thư mục `pro/`)

| File | Dùng để |
|---|---|
| `video_clean.mp4` | Hình **không có phụ đề** và tiếng đã mix. Mỗi cảnh là một đoạn riêng trên timeline. |
| `voice.wav` · `music.wav` · `sfx.wav` | Ba track âm thanh riêng (24-bit, 48 kHz), đã duck sẵn. Cộng lại bằng `mix.wav`, ở −14 LUFS. |
| `*.fcpxml` | Mở trong **DaVinci Resolve** (File → Import → Timeline) hoặc **Final Cut Pro**. Đã cắt sẵn theo từng cảnh. Phụ đề là **title sửa được**: đổi chữ, font hay màu tuỳ ý. |
| `*.xml` + `*.srt` | Mở trong **Premiere Pro** (File → Import). Kéo file `.srt` vào track Captions. |
| `composition.json` | Timeline gốc của MakeMyClip, dùng để xem lại các bước dựng. |

**Khi chỉnh âm thanh trong DaVinci:** tắt tiếng track gốc của `video_clean.mp4`, rồi kéo `voice.wav`, `music.wav` và `sfx.wav` vào 3 track audio, đặt cùng bắt đầu ở 00:00. Sau đó có thể chỉnh riêng nhạc, hiệu ứng và giọng đọc.

## 3. Câu lệnh mẫu trong Claude Desktop (khi MCP đã bật)

- "Mở `06-ha-noi-san-chuot-1902/pro/video_clean.mp4`, thêm chuyển cảnh fade 0.3 giây giữa các cảnh, rồi xuất mp4 và file DaVinci."
- "Ghép clip 04, 05 và 06 thành một video tổng hợp, chèn title card đen 'Phần 1', 'Phần 2', 'Phần 3' giữa các clip, rồi xuất 1080p."
- "Làm bản 30 giây của clip 06: giữ cảnh 1, 5, 6, 7 và 10."
- "Kiểm tra các vết cắt xem có cắt ngang chữ không, và cho mình xem contact sheet."

Mỗi bước đều hoàn tác được (undo). Gõ `clip ui` trong Terminal (cần Node 24) để mở timeline trên trình duyệt và tự chỉnh tay.
