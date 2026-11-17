#!/usr/bin/env python3
"""Tạo runner flowkit/runners/vo_toi_mat_tri_nho.py (clone runner cai_ket_cho_tieu_tam.py, thay nhân vật/tên phim)
và đăng ký kênh "vo-toi-mat-tri-nho" trong flowkit/agent/api/cms.py. Chạy một lần:

    python3 vo-toi-mat-tri-nho/_parts/make_runner.py
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import header_data as H  # noqa: E402

SLUG = "vo-toi-mat-tri-nho"
TITLE = "Vợ Tôi Mất Trí Nhớ Có Chọn Lọc"
OLD_TITLE = "Chính Thất Cao Tay, Tiểu Tam Trắng Tay"
STORY = ("Đúng tối kỷ niệm mười năm ngày cưới, cựu hoa khôi Linh bắt gặp chồng là giám đốc Quân khoác tay cô giáo yoga Mai Anh ở sảnh khách sạn. "
         "Cô ngất rất đẹp rồi tỉnh dậy 'mất trí nhớ có chọn lọc': nhớ con, nhớ mật khẩu thẻ, chỉ quên mỗi chồng — muốn làm chồng thì phải tán lại từ đầu. "
         "Bác sĩ Khang thành đồng phạm, Mai Anh biết mình bị lừa và thành đồng minh của Linh, thư tình giao nhầm phong bì, bé Bống lỡ miệng. "
         "Quân biết vợ giả vờ và diễn theo đến màn cầu hôn lần hai; Linh đồng ý với điều kiện anh ký hợp đồng thử việc làm chồng sáu tháng. "
         "Một năm sau, đúng nhà hàng cũ, lần này anh đến trước.")
DESC = ("Phim hài – tình cảm gia đình Việt Nam 25 phút, kịch bản gốc (100% thoại nhân vật, không người dẫn chuyện, nhịp giọng theo cảnh): "
        "vợ giả mất trí nhớ để bắt người chồng ngoại tình tán lại mình từ đầu; tiểu tam thành đồng minh, kết có hậu bằng hợp đồng thử việc làm chồng "
        "(16:9, 25 cảnh × 4 clips × 15s = 100 clips — Google Flow Omni 1.2).")

EXTRA = {  # voice lock, giọng (VN/EN), mô tả tiếng Việt, chiều cao + vai cho ảnh mẫu
    "@Linh": ("VOICE_LOCK_LINH_VTMN", "Fixed 32-year-old native Standard Northern Vietnamese female voice (~220 Hz clear warm alto), elegant and playful (giọng nữ 32 tuổi chuẩn Hà Nội, trong ấm, sang, tinh nghịch).",
              "Linh, 32 tuổi, cựu người mẫu kiêm hoa khôi, vợ Quân, giả mất trí nhớ có chọn lọc; đẹp nổi bật kiểu nữ chính, cao, dáng người mẫu, da trắng sáng mịn, tóc đen dài suôn mượt, mắt hạnh nhân to sáng, gò má cao, nụ cười rạng rỡ; sơ mi lụa ngà, quần ống rộng cạp cao màu kem, khuyên tai ngọc trai, giày cao gót màu nude.",
              "a 32-year-old Vietnamese woman, former fashion model and beauty-pageant winner, 170 cm"),
    "@Quan": ("VOICE_LOCK_QUAN_VTMN", "Fixed 36-year-old native Standard Northern Vietnamese male voice (~115 Hz smooth resonant baritone), charming, cracking when flustered (giọng nam 36 tuổi chuẩn Hà Nội, trầm ấm, cuốn hút).",
              "Quân, 36 tuổi, chồng Linh, giám đốc công ty thiết kế nội thất cao cấp; nam chính điển trai, cao, dáng thể thao, quai hàm sắc, tóc ngắn rẽ ngôi gọn, râu lún phún, má lúm khi cười; vest xanh navy may đo, sơ mi trắng hở cổ, đồng hồ bạc, giày da nâu.",
              "a 36-year-old Vietnamese man, CEO of a luxury interior-design company, 180 cm"),
    "@MaiAnh": ("VOICE_LOCK_MAIANH_VTMN", "Fixed 25-year-old native Standard Northern Vietnamese young female voice (~260 Hz bright airy soprano), bubbly and quick (giọng nữ 25 tuổi chuẩn Hà Nội, trong, nhí nhảnh).",
                "Mai Anh, 25 tuổi, cô giáo yoga kiêm KOL, người yêu bí mật của Quân rồi thành đồng minh của Linh; xinh tươi rạng rỡ, dáng thon săn chắc, da nâu mật ong, tóc nâu hạt dẻ dài gợn sóng, mắt nai mi dài, mặt trái tim, môi hồng bóng; cardigan len hồng ngoài áo trắng ôm, quần jeans xanh nhạt, giày thể thao trắng, khuyên tròn vàng nhỏ.",
                "a 25-year-old Vietnamese woman, yoga instructor and lifestyle influencer, 163 cm"),
    "@Khang": ("VOICE_LOCK_KHANG_VTMN", "Fixed 34-year-old native Standard Northern Vietnamese male voice (~140 Hz calm gentle tenor), dry deadpan (giọng nam 34 tuổi chuẩn Hà Nội, điềm đạm, hài tỉnh bơ).",
               "Khang, 34 tuổi, bác sĩ phục hồi chức năng, bạn đại học của Linh; điển trai kiểu trí thức, cao gầy, da sáng, tóc đen rối nhẹ, kính không gọng, nụ cười nửa miệng; áo blouse trắng ngoài sơ mi xanh nhạt, quần xám, ống nghe trên cổ, giày thể thao trắng.",
               "a 34-year-old Vietnamese man, rehabilitation doctor, 178 cm"),
    "@Tuan": ("VOICE_LOCK_TUAN_VTMN", "Fixed 35-year-old native Standard Northern Vietnamese male voice (~150 Hz lively nasal comic tenor), gabbling when lying (giọng nam 35 tuổi chuẩn Hà Nội, nhanh nhảu, hài).",
              "Tuấn, 35 tuổi, trợ lý kiêm bạn thân của Quân, nói dối dở nhất Hà Nội; đẹp trai kiểu trẻ trung, mặt nhẵn, má lúm sâu, mắt sáng, tóc đen dày hơi xoăn, người đầm; vest màu be, sơ mi hồng nhạt không cà vạt, giày lười nâu, luôn kẹp máy tính bảng.",
              "a 35-year-old Vietnamese man, a CEO's personal assistant, 170 cm"),
    "@Bong": ("VOICE_LOCK_BONG_VTMN", "Fixed 7-year-old native Standard Northern Vietnamese girl voice (~320 Hz high clear child voice), earnest and bright (giọng bé gái 7 tuổi chuẩn Hà Nội, trong trẻo).",
              "Bống, 7 tuổi, con gái Linh và Quân; bé gái đáng yêu, mặt tròn hồng hào, mắt to long lanh, mái bằng, hai bím cao buộc nơ vàng, răng sún; váy cotton vàng cổ trắng, tất trắng, giày đỏ nhỏ.",
              "a 7-year-old Vietnamese girl, 120 cm"),
}
KEYS = {"@Linh": "Linh", "@Quan": "Quan", "@MaiAnh": "MaiAnh", "@Khang": "Khang", "@Tuan": "Tuan", "@Bong": "Bong"}
ALIASES = {"@Linh": ["@Linh", "Linh", "Chị Linh"], "@Quan": ["@Quan", "Quân", "Anh Quân", "Quan"],
           "@MaiAnh": ["@MaiAnh", "Mai Anh", "MaiAnh"], "@Khang": ["@Khang", "Khang", "Bác sĩ Khang"],
           "@Tuan": ["@Tuan", "Tuấn", "Tuan"], "@Bong": ["@Bong", "Bống", "Bé Bống", "Bong"]}


def look(tag: str) -> tuple[str, str]:
    """(ngoại hình, trang phục) tiếng Anh tách từ anchor."""
    parts = H.CHARACTERS[tag]["anchor"].split("; ")
    return parts[-2], parts[-1].rstrip(".")


def ref_prompt(tag: str) -> str:
    face, outfit = look(tag)
    who = EXTRA[tag][3]
    return (f"Full-body photorealistic character reference of {tag}, {who}, {face}, wearing {outfit}; "
            "plain light-grey studio background, soft flattering beauty light, sharp focus on a camera-ready face, natural skin texture, 8K. "
            "Not resembling any real actor or real person.")


def specs_py() -> str:
    out = ["CHARACTER_SPECS = ["]
    for tag in H.CHARACTERS:
        vl, vp, desc, _ = EXTRA[tag]
        out += ["    {",
                f"        \"key\": {json.dumps(KEYS[tag])},",
                f"        \"tag\": {json.dumps(tag)},",
                f"        \"aliases\": {json.dumps(ALIASES[tag], ensure_ascii=False)},",
                "        \"default_media_id\": \"\",  # tự tạo ảnh mẫu từ ref_prompt ở lần chạy đầu, rồi khoá vào character_refs/character_media_ids.json",
                f"        \"voice_lock\": {json.dumps(vl)},",
                f"        \"voice_profile\": {json.dumps(vp, ensure_ascii=False)},",
                f"        \"description\": {json.dumps(desc, ensure_ascii=False)},",
                f"        \"ref_prompt\": (\n            {json.dumps(ref_prompt(tag), ensure_ascii=False)}\n        ),",
                "    },"]
    out.append("]")
    return "\n".join(out)


def make_runner() -> None:
    src = open(os.path.join(REPO, "flowkit", "runners", "cai_ket_cho_tieu_tam.py"), encoding="utf-8").read()
    start = src.index("CHARACTER_SPECS = [")
    end = src.index("\n]\n", start) + 2
    src = src[:start] + specs_py() + src[end:]
    names = ", ".join(H.CHARACTERS)
    old_story = re.search(r'"(Cô thư ký Vy đến tận tiệm may[^"]*)"', src).group(1)
    reps = [
        ('PROJECT_ID = "e5783dc5-1a5e-4608-8fe9-e55f5f6de0bb"', 'PROJECT_ID = ""\nPROJECT_ID = os.environ.get("VTK_FLOW_PROJECT_ID", "").strip() or PROJECT_ID'),
        ('"Phim gia đình có miếng hài Việt Nam 25 phút, kịch bản gốc bản 3 (16:9, 25 cảnh × 4 clips × 15s = 100 clips — Google Flow Omni 1.2, 100% thoại nhân vật Lip-Sync, nhịp giọng theo cảnh)."',
         json.dumps(DESC, ensure_ascii=False)),
        (old_story, STORY.replace('"', "'")),
        ("cai-ket-cho-tieu-tam", SLUG), ("cai_ket_cho_tieu_tam", "vo_toi_mat_tri_nho"),
        (OLD_TITLE.upper(), TITLE.upper()), (OLD_TITLE, TITLE), (" (tên cũ: Cái Kết Cho Tiểu Tam)", ""),
        ("Phim Gia Đình 25 Phút", "Phim Hài Gia Đình 25 Phút"),
        ("PHIM GIA ĐÌNH", "PHIM HÀI GIA ĐÌNH"),
        ("@Thu, @Tung, @Vy, @BaNhan, @Na, @Khai", names),
        ('json.dumps(["Thu", "Tung", "Vy", "BaNhan", "Na", "Khai"])', f"json.dumps({json.dumps(list(KEYS.values()))})"),
    ]
    for a, b in reps:
        if a not in src:
            print(f"⚠️  không thấy: {a[:60]}")
        src = src.replace(a, b)
    left = [w for w in ("Tiểu Tam Trắng", "@Thu", "@Khai", "tiệm may") if w in src]
    if left:
        print("⚠️  còn sót:", left)
    dst = os.path.join(REPO, "flowkit", "runners", "vo_toi_mat_tri_nho.py")
    open(dst, "w", encoding="utf-8").write(src)
    os.chmod(dst, 0o755)
    print("wrote", dst)


def register_cms() -> None:
    p = os.path.join(REPO, "flowkit", "agent", "api", "cms.py")
    s = open(p, encoding="utf-8").read()
    if f'"slug": "{SLUG}"' in s:
        print("cms.py: kênh đã có, bỏ qua")
        return
    chars = []
    for tag in H.CHARACTERS:
        vl, _, desc, _ = EXTRA[tag]
        chars.append({"tag": tag, "name": f"{H.CHARACTERS[tag]['name']} — {vl}", "default_media_id": "", "locked_media_id": "",
                      "voice_lock": vl, "description": f"{desc} Giọng thoại: {vl}.", "ref_prompt": ref_prompt(tag)})
    entry = {"slug": SLUG, "name": f"{TITLE} (Phim Hài Gia Đình 25 Phút)", "project_id": "",
             "aspect_ratio": "VIDEO_ASPECT_RATIO_LANDSCAPE", "runner_script": "runners/vo_toi_mat_tri_nho.py",
             "series_dir": SLUG, "ep_prefix": "canh", "description": DESC, "characters": chars}
    block = json.dumps(entry, ensure_ascii=False, indent=4)
    block = "\n".join("    " + ln for ln in block.splitlines()) + ",\n"
    i = s.index("CHANNEL_MAX_EPISODES")
    j = s.rindex("\n]\n", 0, i) + 1  # end of DEFAULT_CHANNELS
    s = s[:j] + block + s[j:]
    s = s.replace('    "dung-luong-trong": 20,\n}', f'    "dung-luong-trong": 20,\n    "{SLUG}": 25,\n}}', 1)
    s = s.replace('"gang-to-tai-xuat", "cai-ket-cho-tieu-tam") and re.search', f'"gang-to-tai-xuat", "cai-ket-cho-tieu-tam", "{SLUG}") and re.search', 1)
    open(p, "w", encoding="utf-8").write(s)
    print("cms.py: đã đăng ký kênh", SLUG)


if __name__ == "__main__":
    make_runner()
    register_cms()
