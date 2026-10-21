#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tool Crawl Tin Tức Hot Bóng Đá Châu Âu & Tự Động Lập Kịch Bản Cho Tây Du Ký 2026
Hỗ trợ lấy tin từ VnExpress Thể Thao, 24h, BBC Sport... và tự sinh prompt Google Flow.

Cách dùng:
  python3 football_crawler.py --list                 # Quét và hiển thị tin nóng hôm nay
  python3 football_crawler.py --create-tap <số_tin>  # Chọn tin theo số thứ tự để tự sinh kịch bản và prompt tập mới
"""

import sys
import os
import re
import argparse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime

RSS_SOURCES = [
    {
        "name": "VnExpress Thể Thao",
        "url": "https://vnexpress.net/rss/the-thao.rss",
        "lang": "vi"
    },
    {
        "name": "BBC Sport Football",
        "url": "https://feeds.bbci.co.uk/sport/football/rss.xml",
        "lang": "en"
    }
]

FOOTBALL_KEYWORDS = [
    "ngoại hạng anh", "premier league", "champions league", "c1", "manchester", "man utd", "mu",
    "man city", "arsenal", "liverpool", "chelsea", "tottenham", "real madrid", "barcelona", "barca",
    "el clasico", "ronaldo", "messi", "haaland", "mbappe", "sa thải", "hlv", "var", "bóng vàng",
    "chuyển nhượng", "derby", "la liga", "bayern", "juventus"
]

def fetch_rss_news():
    articles = []
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}
    
    for src in RSS_SOURCES:
        try:
            req = urllib.request.Request(src["url"], headers=headers)
            with urllib.request.urlopen(req, timeout=6) as response:
                root = ET.fromstring(response.read())
                items = root.findall(".//item")
                for it in items:
                    title_elem = it.find("title")
                    desc_elem = it.find("description")
                    link_elem = it.find("link")
                    
                    title = title_elem.text.strip() if title_elem is not None and title_elem.text else ""
                    desc = desc_elem.text.strip() if desc_elem is not None and desc_elem.text else ""
                    link = link_elem.text.strip() if link_elem is not None and link_elem.text else ""
                    
                    clean_desc = re.sub(r'<[^>]+>', '', desc).strip()
                    text_to_check = (title + " " + clean_desc).lower()
                    relevance_score = sum(1 for kw in FOOTBALL_KEYWORDS if kw in text_to_check)
                    
                    if relevance_score > 0:
                        articles.append({
                            "source": src["name"],
                            "title": title,
                            "summary": clean_desc,
                            "link": link,
                            "score": relevance_score
                        })
        except Exception:
            continue
            
    articles.sort(key=lambda x: x["score"], reverse=True)
    return articles

def find_next_tap_number(base_dir):
    existing = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d)) and d.startswith("tap-")]
    nums = []
    for d in existing:
        try:
            nums.append(int(d.replace("tap-", "")))
        except ValueError:
            pass
    return max(nums) + 1 if nums else 1

def generate_football_episode(article, target_tap_num, base_dir):
    tap_dir = os.path.join(base_dir, f"tap-{target_tap_num}")
    os.makedirs(tap_dir, exist_ok=True)
    
    news_title = article["title"]
    news_source = article["source"]
    today_str = datetime.now().strftime("%d/%m/%Y")
    
    # 1. Generate README.md
    readme_content = f"""# Tây Du Ký 2026 — Tập {target_tap_num}: Đại chiến bóng đá đêm khuya

**Ngày {target_tap_num}** · Tập 24s = 3 clip × 8s (bỏ clip 3 → 16s) · 9:16 · thoại tiếng Việt · không chữ trên video

**⚡ Tập xu hướng bóng đá Châu Âu**
- **Sự kiện nóng:** "{news_title}" ({news_source} ngày {today_str})
- **Ý tưởng:** 4 thầy trò thức đêm xem bóng đá Châu Âu tại nhà trọ Sài Gòn. Ngộ Không fan cuồng cuồng nhiệt gáy sớm; Bát Giới ôm đĩa khô gà dự đoán HLV bay ghế; Sa Tăng làm trọng tài can ngăn; Sư phụ tưởng đâu niệm Phật hóa ra lén bật điện thoại giắt tay áo hóng VAR!

> **Cách dựng:** Clip 1: **Video → Veo 3.1 → Ingredients**, đính ảnh tham chiếu → Clip 2 và 3: **Save frame** khung cuối clip trước → **Frames**, đặt làm **Start frame** → ghép 3 clip trong Scenebuilder. Chi tiết: FLOW_GUIDE mục 1.

← Hôm trước: [Tập {target_tap_num - 1}](../tap-{target_tap_num - 1}/README.md)

---

**Tóm tắt:** 3 giờ sáng tại phòng khách nhà trọ Sài Gòn, màn hình TV phát trực tiếp đại chiến bóng đá rực lửa. Ngộ Không nhảy tưng tưng trên lưng ghế, vung gậy Như Ý hô hào cuồng nhiệt. Bát Giới nằm ườn dưới sàn gặm đồ ăn, buông câu cà khịa: "Đá vầy HLV chuẩn bị bay ghế là cái chắc!". Ngộ Không nổi đóa chỉ gậy dọa đánh, Sa Tăng vội chạy ra can. Bất thình lình, Sư phụ từ trong buồng bước ra nghiêm mặt: "Đêm hôm khuya khoắt ồn ào...". Nhưng mắt Sư phụ liếc vào màn hình TV, bấm điện thoại giắt trong tay áo: "A Di Đà Phật... quả đó bóng chạm tay rồi, VAR đâu?".

**Nhân vật:** `@DuongTang`, `@NgoKhong`, `@BatGioi`, `@SaTang`
**Bối cảnh:** Phòng khách nhà ống Sài Gòn về đêm (đèn mờ, ánh sáng xanh từ TV phát trực tiếp bóng đá, bàn inox, quạt máy).
**Trang phục:** Mặc định.

| Thời gian | Hình ảnh | Thoại |
| --- | --- | --- |
| 00:00–00:02 | Ngộ Không đứng trên ghế sofa, tay vung gậy Như Ý hô hào, TV phát bóng đá **(hook)** | Ngộ Không: "Vô! Ép sân dữ dội chưa!" |
| 00:02–00:05 | Bát Giới nằm ôm đĩa đồ ăn cười khẩy, lắc đầu chê bai | Bát Giới: "Đá vầy HLV bay ghế sớm!" |
| 00:05–00:08 | Ngộ Không phóng gậy chỉ thẳng mặt Bát Giới; Sa Tăng từ bếp chạy ra can | Ngộ Không: "Lão Trư, mi bớt trù ẻo coi!" |
| 00:08–00:11 | Sa Tăng kéo Bát Giới lùi lại, tay cầm dĩa dưa hấu giảng hòa | Sa Tăng: "Đại sư huynh bớt nóng, ăn miếng dưa..." |
| 00:11–00:13 | Bát Giới phẩy tay, chớp mắt thách thức cá cược chầu ăn sáng | Bát Giới: "Dám cá chầu hủ tiếu không?" |
| 00:13–00:16 | Tiếng ho khẽ từ cửa phòng ngủ; bóng Sư phụ bước ra, cả ba đứng hình | Sư phụ: "Nửa đêm... ai cho mấy đứa cá độ?" |
| 00:16–00:19 | Ba đệ tử cúi đầu chắp tay chịu tội, tưởng sắp bị mắng té tát | Ngộ Không: "Sư phụ... tụi con lỡ..." |
| 00:19–00:22 | Sư phụ thò tay vào ống tay áo rút smartphone, mắt nhìn chăm chú TV | Sư phụ: "Quả vừa rồi chạm tay rõ mồn một!" |
| 00:22–00:24 | Cả 4 thầy trò chụm đầu cùng dán mắt vào TV chờ tổ VAR **(thumbnail)** | Sư phụ: "A Di Đà Phật... VAR đâu rồi?" |

## Các clip

| Clip | Thời gian | Cách tạo | File prompt |
| --- | --- | --- | --- |
| 1 | 00:00–00:08 | Ingredients | [clip-1.md](clip-1.md) |
| 2 | 00:08–00:16 | Frames (Start frame = cuối clip 1) | [clip-2.md](clip-2.md) |
| 3 | 00:16–00:24 | Frames (Start frame = cuối clip 2) | [clip-3.md](clip-3.md) |
"""
    with open(os.path.join(tap_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme_content)

    # 2. Generate clip-1.md
    clip1_content = """[FORMAT]
Vertical 9:16, 8-second shot, high-end 3D animated film, Pixar/Disney-quality stylized CGI, modern Saigon interior at late night, dim ambient room light illuminated by the flickering bright blue glow of a television broadcasting a football match, 24fps. Spoken dialogue in Vietnamese with Southern Vietnamese accents and accurate lip-sync. No subtitles, no captions, no on-screen text, no logos, no watermark.

[CHARACTERS — match the attached reference images exactly]
@NgoKhong = NGỘ KHÔNG: small agile anthropomorphic monkey, golden-brown fur, red heart-shaped face, bright amber eyes, thin golden circlet headband, red bomber jacket over plain yellow t-shirt, tiger-stripe cargo shorts, barefoot; holding his pen-sized staff extended into a short red-and-gold staff. Restless, fiery, passionate football fanatic. Voice: fast, sharp, quick-witted, excitable young male voice.
@BatGioi = BÁT GIỚI: chubby anthropomorphic pink pig, big floppy ears, round snout, oversized black t-shirt, navy robe, small nine-tooth rake strapped across his back, lying lazily on the tiled floor holding a snack bowl. Voice: lazy, smug, sarcastic nasal male voice.
@SaTang = SA TĂNG: tall muscular anthropomorphic demon, dark blue-grey skin, curly red beard, black eyebrows, wooden prayer bead necklace, wearing a dark-grey sleeveless top and green cleaning apron. Calm, practical mediator. Voice: deep, calm, gentle Southern male voice.

[SETTING — LIVING ROOM AT MIDNIGHT]
SAIGON TOWNHOUSE LIVING ROOM: late night at 3:00 AM, dim room lighting, glowing television screen on the right showing animated footballers on a green pitch, folding stainless-steel table, ceiling fan gently spinning, quiet alley outside visible through balcony window.

[SHOT LIST]
00:00–00:02 | Medium two-shot, quick push-in — Ngộ Không perches excitedly on the armrest of a wooden chair, waving his mini staff in the air, his eyes reflecting the flashing TV screen. NGỘ KHÔNG shouts (fast, fiery, cheering): "Vô! Ép sân dữ dội chưa!"
00:02–00:05 | Medium close-up on floor — Bát Giới lies comfortably on the tiled floor with a snack bowl, casually chewing and rolling his eyes smugly toward the TV. BÁT GIỚI says (lazy, smug, mocking tone): "Đá vầy HLV bay ghế sớm!"
00:05–00:08 | Medium two-shot — Ngộ Không snaps his head around in rage, leaping onto the stainless-steel table and pointing his staff right at Bát Giới's snout; Sa Tăng rushes in from the kitchen with a plate of sliced watermelon to intervene. NGỘ KHÔNG yells (sharp, angry): "Lão Trư, mi bớt trù ẻo coi!"

[SOUND]
Muffled stadium crowd roar from television, whoosh of staff extending, crunching snack sounds, energetic modern sitcom acoustic guitar beat.

[END FRAME]
Medium two-shot in dim room: Ngộ Không crouched atop the metal table pointing his red staff down at Bát Giới; Bát Giới on the floor shielding his face with his snack bowl; Sa Tăng stepping between them with a watermelon plate; flashing blue TV light on their faces. Hold completely still for the final 0.5 seconds.

[AVOID]
Subtitles, legible letters on TV screen, realistic violence, human bodies, outfit changes, distorted paws or extra fingers.
"""
    with open(os.path.join(tap_dir, "clip-1.md"), "w", encoding="utf-8") as f:
        f.write(clip1_content)

    # 3. Generate clip-2.md
    clip2_content = """Start exactly from the provided first frame (the final frame of the previous clip) and continue the scene seamlessly. Same characters, same outfits, same location, same lighting and color grade. Flawless continuity, no time skip, no jump cut at the start.
Style unchanged: high-end 3D animated film, vertical 9:16, Vietnamese dialogue with a natural Southern accent and accurate lip-sync, no subtitles or on-screen text.

[CHARACTERS — locked]
@NgoKhong = NGỘ KHÔNG: small golden-brown monkey, red heart-shaped face, amber eyes, thin golden circlet, red bomber jacket, tiger-stripe shorts, holding short staff; fiery and impatient.
@BatGioi = BÁT GIỚI: chubby pink pig, oversized black t-shirt, navy robe, lazy and cheeky.
@SaTang = SA TĂNG: blue-grey skin, red beard, wooden bead necklace, green apron; calm peacemaker.
Entering at 00:05:
@DuongTang = SƯ PHỤ: young human monk, shaved head, calm face, saffron-orange robe with deep-red kasaya sash, smartphone tucked into wide right sleeve; serene and dignified.

[SETTING — LOCKED LIVING ROOM AT MIDNIGHT]
SAIGON TOWNHOUSE LIVING ROOM: dim late-night room illuminated by flickering TV glow, stainless-steel table, small wooden Buddhist altar shelf high on the upper wall serene and untouched.

[SHOT LIST]
00:00–00:03 | Medium shot, continuing smoothly from Start Frame — Sa Tăng places the watermelon plate on the table, gently pushing Ngộ Không's staff down with two fingers. SA TĂNG says (deep, calm Southern voice; soothing): "Đại sư huynh bớt nóng, ăn miếng dưa..."
00:03–00:05 | Medium close-up — Bát Giới sits up, dusting crumbs off his belly, raising a chubby finger with an impish smirk. BÁT GIỚI says (cheeky, betting tone): "Dám cá chầu hủ tiếu không?"
00:05–00:08 | Medium wide shot — a soft cough echoes from the hallway; the wooden bedroom door creaks open and Sư phụ steps into the room, hands folded serenely, his shadow stretching across the floor; all three disciples freeze instantly like statues. SƯ PHỤ says (gentle, strict, slow): "Nửa đêm... ai cho mấy đứa cá độ?"

[SOUND]
Soft door creak, sudden comedic silence as the football crowd noise mutes slightly, tense clock tick, soft chime as Sư phụ enters.

[END FRAME]
Medium wide three-shot: Sư phụ standing in the center background in his saffron robe with arms folded inside wide sleeves, looking sternly forward; Ngộ Không frozen atop the table with his staff frozen mid-air; Bát Giới frozen on the floor with finger raised; blue TV light washing across them. Hold still for the final 0.5 seconds.

[AVOID]
Subtitles, touching the high altar shelf, changes to robe or clothing colors, morphing characters, harsh light.
"""
    with open(os.path.join(tap_dir, "clip-2.md"), "w", encoding="utf-8") as f:
        f.write(clip2_content)

    # 4. Generate clip-3.md
    clip3_content = """Start exactly from the provided first frame (the final frame of the previous clip) and continue the scene seamlessly. Same characters, same outfits, same location, same lighting and color grade. Flawless continuity, no time skip, no jump cut at the start.
Style unchanged: high-end 3D animated film, vertical 9:16, Vietnamese dialogue with a natural Southern accent and accurate lip-sync, no subtitles or on-screen text.

[CHARACTERS — locked]
@DuongTang = SƯ PHỤ: young shaved-head human monk, saffron-orange robe with red sash, wooden beads, modern smartphone in right sleeve; gentle, surprisingly invested in football.
@NgoKhong = NGỘ KHÔNG: small golden-brown monkey, red bomber jacket, tiger-stripe shorts; wide-eyed, guilty.
@BatGioi = BÁT GIỚI: chubby pink pig, black t-shirt, looking terrified.
@SaTang = SA TĂNG: blue-grey skin, red beard, green apron; respectful.

[SETTING — LOCKED LIVING ROOM AT MIDNIGHT]
SAIGON TOWNHOUSE LIVING ROOM: late-night television glow illuminating the four characters, stainless-steel table, quiet townhouse ambiance.

[SHOT LIST]
00:00–00:02 | Medium shot, continuing from Start Frame — Ngộ Không quickly hides his staff behind his back, jumping down from the table and bowing his head guiltily beside Bát Giới and Sa Tăng. NGỘ KHÔNG stammers (sheepish, humble): "Sư phụ... tụi con lỡ..."
00:02–00:05 | Medium close-up on Sư phụ, slow push-in — Sư phụ keeps his serene expression, but his right hand slides smoothly into his sleeve and pulls out his smartphone, his eyes locking onto the glowing TV screen with sudden intense focus. SƯ PHỤ says (gentle tone, but sharp football observation): "Quả vừa rồi chạm tay rõ mồn một!"
00:05–00:08 | Medium group four-shot — the three disciples' jaws drop in disbelief, then they all eagerly lean in around Sư phụ, four pairs of eyes glued to the TV screen in total suspense. SƯ PHỤ presses his palms together with a tiny smirk. SƯ PHỤ says (serene whisper): "A Di Đà Phật... VAR đâu rồi?"

[SOUND]
Sudden whistle blow from television, energetic comedy marimba resolving into a lively modern Vietnamese hip-hop beat, subtle smartphone screen tap, cheerful audience laughter sting.

[END FRAME]
Medium four-shot centered in front of the television: Sư phụ in center holding his smartphone up beside his chest, watching the screen intently with a faint knowing smile; Ngộ Không perched on his left peering forward; Bát Giới on the right with mouth open; Sa Tăng looking over Sư phụ's shoulder; colorful flickering TV light illuminating their faces. Hold completely still for the final 1.0 second as an irresistible thumbnail frame.

[AVOID]
Subtitles, disrespect to monk figure, brand logos on smartphone, distorted hands or paws, flickering camera cuts.
"""
    with open(os.path.join(tap_dir, "clip-3.md"), "w", encoding="utf-8") as f:
        f.write(clip3_content)

    print(f"-> Đã tạo thành công Tập {target_tap_num} tại: {tap_dir}")
    print(f"   + {os.path.join(tap_dir, 'README.md')}")
    print(f"   + {os.path.join(tap_dir, 'clip-1.md')}")
    print(f"   + {os.path.join(tap_dir, 'clip-2.md')}")
    print(f"   + {os.path.join(tap_dir, 'clip-3.md')}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tool crawl tin bóng đá Châu Âu cho Tây Du Ký 2026")
    parser.add_argument("--list", action="store_true", help="Hiển thị danh sách tin tức bóng đá hot nhất hôm nay")
    parser.add_argument("--create-tap", type=int, default=None, help="Chọn số thứ tự tin tức để tự động tạo tập mới (1..N)")
    args = parser.parse_args()

    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    
    print(f"=== ĐANG QUÉT TIN TỨC BÓNG ĐÁ CHÂU ÂU HOT ({datetime.now().strftime('%d/%m/%Y %H:%M')}) ===")
    news = fetch_rss_news()
    
    if not news:
        print("Không tìm thấy tin phù hợp.")
        sys.exit(0)
        
    top_news = news[:10]
    
    if args.list or args.create_tap is None:
        print(f"Tìm thấy {len(news)} tin bóng đá nóng hôm nay (hiển thị Top 10):\n")
        for i, item in enumerate(top_news, 1):
            print(f"[{i}] [{item['source']}] {item['title']} (Điểm hot: {item['score']})")
            if item['summary']:
                print(f"    -> Tóm tắt: {item['summary'][:130]}...\n")
        print("💡 Gợi ý lệnh tạo tập mới tự động: python3 football_crawler.py --create-tap 1")

    if args.create_tap is not None:
        idx = args.create_tap - 1
        if 0 <= idx < len(top_news):
            chosen = top_news[idx]
            next_tap = find_next_tap_number(base_dir)
            print(f"\n🚀 Đang tạo Tập {next_tap} dựa trên tin: '{chosen['title']}'...")
            generate_football_episode(chosen, next_tap, base_dir)
        else:
            print(f"Lỗi: Số thứ tự phải nằm trong khoảng 1 đến {len(top_news)}")
