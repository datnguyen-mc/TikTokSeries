#!/usr/bin/env python3
"""
HỆ THỐNG TỰ ĐỘNG HÓA FLOWKIT NÂNG CAO CHO "ĐƯỜNG ĐUA SINH TỬ: 10 GIÂY TỰ DO":
1. KHÓA NHÂN VẬT CỐ ĐỊNH (CHARACTER LOCK): Tự động lấy & khóa chính xác media_id của 12 nhân vật (@Tom, @Micdo, @Ami, @Cevin, @Cina, @Seja, @Onle, @NyTran, @Cela, @Nese, @Kinan, @Verni) từ Google Flow Project.
2. Luôn truyền reference_media_ids qua endpoint /api/flow/generate-video-omni (MZZa6b Ingredients R2V) cho Clip 1 và mọi clip mở cảnh mới ([FORMAT]).
3. Tự động trích xuất khung hình cuối (last frame) làm khung hình đầu (start frame) của clip nối tiếp (Seamless Chaining).
4. Tự động đặt tên clip trên Google Flow theo cảnh ([CẢNH XX - CLIP YY]) và tải ngay về máy khi hoàn thành.
5. Tự động đồng bộ thời gian thực với Console Dashboard UI.
"""

import os
import sys
import time
import json
import base64
import subprocess
import requests
from datetime import datetime

os.environ["NO_PROXY"] = "127.0.0.1,localhost"
os.environ["no_proxy"] = "127.0.0.1,localhost"

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cms_integration import (
    push_cms_log,
    merge_episode_clips,
    merge_multi_scenes_to_episode,
    wait_if_cooldown_error,
    sync_clip_to_r2_and_d1,
    rewrite_prompt_on_failure,
    find_episode_clip_mp4s,
    force_rename_clip_on_flow,
    trim_studio_reference_frames,
    probe_clip_streams,
)

FLOWKIT_API = "http://127.0.0.1:8200"
CHANNEL_SLUG = "duong-dua-sinh-tu"
ONLY_CLIP = int(os.environ.get("FLOWKIT_ONLY_CLIP", "0") or "0")

# 👉 PROJECT_ID GOOGLE FLOW CỦA SERIES "ĐƯỜNG ĐUA SINH TỬ: 10 GIÂY TỰ DO" — tạo project mới trên Flow rồi điền trên CMS (http://localhost:8200/)
PROJECT_ID = "f9738ca5-453b-4c72-98d3-630379a1fa2e"
DEFAULT_PROJECT_ID = "f9738ca5-453b-4c72-98d3-630379a1fa2e"
ASPECT_RATIO = "VIDEO_ASPECT_RATIO_LANDSCAPE"
IMAGE_ASPECT_RATIO = "IMAGE_ASPECT_RATIO_LANDSCAPE"

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SERIES_DIR = os.path.join(WORKSPACE_DIR, "duong-dua-sinh-tu")
FRAMES_DIR = os.path.join(SERIES_DIR, "exported_frames")
OUTPUT_VIDEOS_DIR = os.path.join(SERIES_DIR, "output_videos")
CHAR_REFS_DIR = os.path.join(SERIES_DIR, "character_refs")
CHAR_CACHE_FILE = os.path.join(CHAR_REFS_DIR, "character_media_ids.json")

os.makedirs(FRAMES_DIR, exist_ok=True)
os.makedirs(OUTPUT_VIDEOS_DIR, exist_ok=True)
os.makedirs(CHAR_REFS_DIR, exist_ok=True)

# -------------------------------------------------------------
# 🔒 BẢNG ĐỊNH NGHĨA & KHÓA NHÂN VẬT CỐ ĐỊNH CỦA SERIES (ĐƯỜNG ĐUA SINH TỬ — 12 NHÂN VẬT CHÍNH & PHỤ)
# -------------------------------------------------------------
CHARACTER_SPECS = [
    {
        "key": "Tom",
        "tag": "@Tom",
        "aliases": ["@Tom", "TOM (27", "TOM in", "@Tom = Tom", "Tom"],
        "default_media_id": "53e825dd-52eb-41f9-bf6a-4fe562792c55",
        "description": "Tom (27 tuổi): sĩ quan cảnh sát chìm LAPD ẩn náu trong tiệm độ xe Ver's Geh; cao 183 cm, dáng thể thao săn chắc, tóc ngắn nâu sẫm cắt gọn, ánh mắt sắc bén, sẹo nhỏ mờ ở đuôi mày trái, mặc áo thun xám than bên trong sơ mi denim xanh đậm mở cúc, quần jean tối màu vương dầu máy.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @Tom, a 27-year-old Vietnamese-American man, 183 cm, athletic lean build, short textured "
            "dark-brown hair, sharp observant dark eyes, clean square jawline, a faint small scar at the outer left eyebrow, fitted charcoal T-shirt "
            "under an open dark-blue denim work shirt, oil-scuffed dark jeans, worn brown work boots, steel chronograph watch on left wrist; plain grey "
            "studio background, hard side light, 8K. Not resembling any real actor."
        ),
    },
    {
        "key": "Micdo",
        "tag": "@Micdo",
        "aliases": ["@Micdo", "MICDO (32", "MICDO in", "@Micdo = Micdo", "Micdo"],
        "default_media_id": "0044e498-ba46-4b33-b325-cb5a322cf73a",
        "description": "Micdo (32 tuổi): thủ lĩnh băng đua xe đường phố và đội xe đen; cao 185 cm, cơ bắp vạm vỡ, đầu cạo trọc, mặt vuông uy quyền, đeo dây chuyền bạc mặt chữ thập trên ngực, mặc áo ba lỗ trắng bên trong áo khoác da đen mở khóa.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @Micdo, a 32-year-old man, 185 cm, muscular heavy-shouldered build, clean-shaven bald head, "
            "commanding deep-set dark eyes, strong square jawline, a silver cross pendant on a heavy neck chain, fitted white sleeveless tank top under "
            "an open black leather jacket, dark jeans, heavy black boots; plain grey studio background, hard side light, 8K. Not resembling any real actor."
        ),
    },
    {
        "key": "Ami",
        "tag": "@Ami",
        "aliases": ["@Ami", "AMI (24", "AMI in", "@Ami = Ami", "Ami"],
        "default_media_id": "7226ddde-c39f-4278-a8ed-ab6187fb7509",
        "description": "Ami (24 tuổi): em gái út của Micdo, người trông coi quán ăn gia đình Toto; cao 168 cm, làn da ngăm ấm, tóc nâu đen dài buộc nửa đầu, đeo bông tai bạc nhỏ, mặc áo cổ tròn màu đỏ rượu vang kết hợp tạp dề vải canvas ngang eo và quần jean sáng màu.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @Ami, a 24-year-old woman, 168 cm, slim athletic build, warm olive skin, long dark-brown hair "
            "tied half-back, expressive dark eyes, silver stud earrings, fitted burgundy scoop-neck top, light-wash jeans, canvas shop apron tied at the "
            "waist, flat sneakers; plain grey studio background, soft warm light, 8K. Not resembling any real actor."
        ),
    },
    {
        "key": "Cevin",
        "tag": "@Cevin",
        "aliases": ["@Cevin", "CEVIN (29", "CEVIN in", "@Cevin = Cevin", "Cevin"],
        "default_media_id": "a0c490db-9269-4093-b7d6-54c7f854dca5",
        "description": "Cevin (29 tuổi): cánh tay phải nóng nảy của Micdo; cao 179 cm, cơ bắp gân guốc, tóc ngắn dựng nhuộm sáng phần ngọn, râu dê gọn, sẹo nhỏ ở khớp ngón tay phải, đeo lắc bạc cổ tay phải, mặc áo sơ mi thợ máy ngắn tay màu đỏ sẫm.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @Cevin, a 29-year-old man, 179 cm, wiry muscular build, short spiky bleached-tip dark hair, "
            "intense brow, neat goatee, small chin scar, silver chain bracelet on right wrist, maroon short-sleeve mechanic shirt with rolled sleeves, "
            "dark cargo jeans, work boots; plain grey studio background, 8K. Not resembling any real actor."
        ),
    },
    {
        "key": "Cina",
        "tag": "@Cina",
        "aliases": ["@Cina", "CINA (28", "CINA in", "@Cina = Cina", "Cina"],
        "default_media_id": "6ef4b4a9-e0a5-4b63-a245-a995f11bd7ea",
        "description": "Cina (28 tuổi): nữ quái tốc độ sát cánh cùng Micdo; cao 167 cm, dáng thon khỏe, tóc đen ngắn ngang cằm, ánh mắt sắc lạnh tự tin, khuyên tai vòng nhỏ bên tai trái, mặc áo ghi-lê da đen ngắn bên ngoài áo đỏ thẫm và quần da tối màu.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @Cina, a 28-year-old woman, 167 cm, lean athletic build, sharp jawline, short tousled "
            "chin-length black hair, fierce confident dark gaze, small hoop earring in left ear, cropped black leather vest over crimson top, low-rise "
            "dark leather trousers, heavy lace boots; plain grey studio background, 8K. Not resembling any real actor."
        ),
    },
    {
        "key": "Seja",
        "tag": "@Seja",
        "aliases": ["@Seja", "SEJA (22", "SEJA in", "@Seja = Seja", "Seja"],
        "default_media_id": "7dc7e4cc-d7ae-47e4-b3d3-cee720775859",
        "description": "Seja (22 tuổi): thiên tài toán học, máy tính và điện tử độ xe của nhóm; cao 175 cm, dáng gầy nhanh nhẹn, tóc đen xoăn rối, đeo kính gọng mảnh kỹ thuật, mặc áo sơ mi công nhân màu xanh ô liu khoác ngoài áo thun dài tay kẻ sọc, đeo dây túi laptop chéo ngực.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @Seja, a 22-year-old man, 175 cm, wiry lanky build, messy curly dark hair, quick restless "
            "eyes, thin-framed technical glasses, oversized olive graphic work shirt over striped long-sleeve tee, cargo trousers, sneakers, canvas "
            "laptop strap across chest; plain grey studio background, 8K. Not resembling any real actor."
        ),
    },
    {
        "key": "Onle",
        "tag": "@Onle",
        "aliases": ["@Onle", "ONLE (30", "ONLE in", "@Onle = Onle", "Onle"],
        "default_media_id": "58d0ebc5-cd00-4af2-9ea8-3b11f352556e",
        "description": "Onle (30 tuổi): thợ máy gầm bệ và tay lái bọc hậu điềm tĩnh của đội; cao 182 cm, vai rộng vạm vỡ, tóc đen cắt sát, râu dê gọn gàng, mặc bộ đồ liền thân thợ máy màu xanh rêu đậm buộc ngang hông bên ngoài áo thun đen.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @Onle, a 30-year-old man, 182 cm, broad-shouldered mechanic build, closely cropped dark hair, "
            "neat goatee, calm steady dark eyes, grease-weathered hands, grease-stained dark-green mechanic jumpsuit tied at the waist over a black "
            "T-shirt, heavy work boots; plain grey studio background, 8K. Not resembling any real actor."
        ),
    },
    {
        "key": "NyTran",
        "tag": "@NyTran",
        "aliases": ["@NyTran", "NY TRẦN", "NY TRAN", "@NyTran = Ny Tran", "Ny Trần", "Ny Tran", "NyTran"],
        "default_media_id": "3004cbee-ba9f-42d8-b11e-c55fec49e5ab",
        "description": "Ny Tran (30 tuổi): thủ lĩnh băng mô tô Light Saigon tại Little Saigon; cao 177 cm, gò má sắc, tóc đen undercut vuốt ngược bóng mượt, ánh mắt lạnh lùng, đeo dây chuyền vàng mảnh, mặc áo khoác da đen họa tiết da rắn bên ngoài sơ mi lụa đỏ sẫm mở cổ.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @NyTran, a 30-year-old Vietnamese man, 177 cm, lean sharp build, sharp cheekbones, sleek "
            "undercut slicked-back black hair, cold calculating dark eyes, thin gold neck chain, tailored black snake-pattern leather jacket over "
            "open-collar crimson silk shirt, black trousers, polished boots; plain grey studio background, 8K. Not resembling any real actor."
        ),
    },
    {
        "key": "Cela",
        "tag": "@Cela",
        "aliases": ["@Cela", "CELA (31", "@Cela = Cela", "Cela"],
        "default_media_id": "57d9ea23-b1c8-4f65-b65b-918d070bd76c",
        "description": "Cela (31 tuổi): anh họ và tay chân thân cận của Ny Tran; cao 174 cm, cơ bắp chắc nịch, tóc cạo hai bên buộc chỏm ngắn trên đỉnh, sẹo chéo bên má phải, hình xăm rồng kín cẳng tay phải, mặc áo ghi-lê da đen sát nách bên ngoài áo tối màu.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @Cela, a 31-year-old Vietnamese man, 174 cm, compact muscular build, shaved sides with a "
            "tied short topknot, narrow watchful eyes, diagonal scar across right cheek, dragon tattoo sleeve on right forearm, sleeveless black leather "
            "vest over dark shirt, black jeans, riding boots; plain grey studio background, 8K. Not resembling any real actor."
        ),
    },
    {
        "key": "Nese",
        "tag": "@Nese",
        "aliases": ["@Nese", "TRUNG SĨ NESE", "NESE (46", "@Nese = Nese", "Trung sĩ Nese", "Nese"],
        "default_media_id": "27ede5a3-d368-4b6e-a8e0-b8b4d8574f03",
        "description": "Trung sĩ Nese (46 tuổi): chỉ huy trực tiếp của Tom trong LAPD; cao 180 cm, dáng vẻ dày dạn sương gió, tóc cắt ngắn điểm bạc, ria mép tỉa gọn, mặc sơ mi trắng xắn tay nới lỏng cà vạt tối màu, đeo bao huy hiệu ở thắt lưng.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @Nese, a 46-year-old veteran police sergeant, 180 cm, solid build, greying crew-cut hair, "
            "weathered lined face, stern focused eyes, trimmed moustache, rolled-sleeve white dress shirt with loosened dark tie, badge holder at belt, "
            "charcoal trousers, leather shoes; plain grey studio background, 8K. Not resembling any real actor."
        ),
    },
    {
        "key": "Kinan",
        "tag": "@Kinan",
        "aliases": ["@Kinan", "ĐẶC VỤ KINAN", "KINAN (44", "@Kinan = Kinan", "Đặc vụ Kinan", "Kinan"],
        "default_media_id": "c5238e27-22b2-44e2-84b7-a0b6296d649d",
        "description": "Đặc vụ liên bang Kinan (44 tuổi): chỉ huy lực lượng đặc nhiệm FBI phối hợp điều tra; cao 178 cm, dáng thẳng nghiêm nghị, tóc nâu sẫm rẽ ngôi gọn, đeo kính gọng kim loại mảnh, mặc bộ vest xám than tối màu bên ngoài sơ mi xanh thép không thắt cà vạt.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @Kinan, a 44-year-old federal agent, 178 cm, trim upright build, neatly parted dark-brown "
            "hair, sharp angular features, piercing gaze, thin metal-frame glasses, tailored dark charcoal suit over steel-blue shirt without tie, "
            "federal credential folder at side; plain grey studio background, 8K. Not resembling any real actor."
        ),
    },
    {
        "key": "Verni",
        "tag": "@Verni",
        "aliases": ["@Verni", "VERNI (48", "@Verni = Verni", "Verni"],
        "default_media_id": "5e834823-4e0f-4c3c-a881-c645630a898a",
        "description": "Verni (48 tuổi): tài xế xe container 18 bánh đường dài trên xa lộ Interstate 10; cao 173 cm, lồng ngực vạm vỡ, râu quai nón dày điểm bạc, gương mặt rám nắng phong sương, đội mũ lưỡi trai tài xế, mặc áo sơ mi kẻ caro bên trong áo ghi-lê bảo hộ màu nâu.",
        "ref_prompt": (
            "Full-body photorealistic character reference of @Verni, a 48-year-old stocky long-haul truck driver, 173 cm, barrel-chested build, strong "
            "forearms, thick grey-streaked beard, sun-weathered face, defiant eyes, receding hair under a worn trucker cap, plaid flannel shirt under "
            "a padded brown work vest, dark jeans, heavy boots; plain grey studio background, 8K. Not resembling any real actor."
        ),
    },
]

LOCKED_CHARACTER_MEDIA_IDS = {}
SCENE_DB_MAP = {}
CURRENT_VIDEO_ID = None
CURRENT_EP_NUM = None
CURRENT_CLIP_NUM = None


def log(msg):
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] {msg}", flush=True)
    level = "INFO"
    if "❌" in msg:
        level = "ERROR"
    elif "⚠️" in msg:
        level = "WARN"
    elif any(icon in msg for icon in ("✅", "🎉", "💾", "🎞️", "🔒")):
        level = "SUCCESS"
    push_cms_log(
        CHANNEL_SLUG,
        level,
        "RUNNER",
        msg,
        project_id=PROJECT_ID,
        episode=CURRENT_EP_NUM,
        clip_num=CURRENT_CLIP_NUM,
    )


def print_box(title, items, border_char="─"):
    width = 72
    print(f"\n┌─ {title} " + border_char * (width - len(title) - 5) + "┐")
    for k, v in items:
        prefix = f"│ • {k}: "
        val_str = str(v)
        if len(prefix) + len(val_str) > width - 2:
            val_display = val_str[:width - len(prefix) - 5] + "..."
        else:
            val_display = val_str
        spacing = " " * max(0, width - len(prefix) - len(val_display) - 1)
        print(f"{prefix}{val_display}{spacing}│")
    print("└" + border_char * (width - 2) + "┘", flush=True)
    push_cms_log(
        CHANNEL_SLUG,
        "SUCCESS" if "HOÀN THÀNH" in title or "ĐÃ KHÓA" in title else "INFO",
        "API_BOX",
        title,
        project_id=PROJECT_ID,
        episode=CURRENT_EP_NUM,
        clip_num=CURRENT_CLIP_NUM,
        details={k: str(v) for k, v in items},
    )


def check_connection():
    try:
        r = requests.get(f"{FLOWKIT_API}/health", timeout=5)
        data = r.json()
        if not data.get("extension_connected"):
            log("⚠️ FlowKit server đang chạy nhưng Chrome Extension chưa kết nối!")
            log(f"👉 Mở Chrome có cài Extension và giữ mở tab https://labs.google/fx/vi/tools/flow/project/{PROJECT_ID}")
            return False
        log("✅ FlowKit & Chrome Extension đang kết nối tốt!")
        return True
    except Exception as e:
        log(f"❌ Không kết nối được tới FlowKit API ({FLOWKIT_API}): {e}")
        return False


# -------------------------------------------------------------
# 0. KHÓA NHÂN VẬT CỐ ĐỊNH (CHARACTER LOCK TỪ GOOGLE FLOW PROJECT)
# -------------------------------------------------------------
def load_and_lock_project_characters(force_remote: bool = False):
    """Đồng bộ hoặc tự động tạo mới & khóa đúng 12 nhân vật chính & phụ trên Google Flow Project."""
    global LOCKED_CHARACTER_MEDIA_IDS, PROJECT_ID
    log("🔒 Đang đồng bộ danh sách 12 Nhân vật (@Tom, @Micdo, @Ami, @Cevin, @Cina, @Seja, @Onle, @NyTran, @Cela, @Nese, @Kinan, @Verni) từ Google Flow Project...")

    # Tự động khởi tạo Project mới trên Google Flow nếu PROJECT_ID đang là ID mặc định chưa tạo
    if PROJECT_ID == "d8997010-1080-49f1-9220-10ec05919c8c":
        try:
            cp = requests.post(
                f"{FLOWKIT_API}/api/flow/create-project",
                json={"title": "Đường Đua Sinh Tử: 10 Giây Tự Do"},
                timeout=45,
            )
            if cp.status_code == 200:
                cp_data = cp.json()
                new_pid = cp_data.get("projectId") or (cp_data.get("data") or {}).get("projectId")
                if new_pid:
                    PROJECT_ID = new_pid
                    log(f"✨ Đã tự động tạo mới Project 'Đường Đua Sinh Tử: 10 Giây Tự Do' trên Google Flow: {PROJECT_ID}")
        except Exception as e:
            log(f"⚠️ Chưa tự tạo được Project mới trên Google Flow: {e}")

    cached_by_project = {}
    if os.path.exists(CHAR_CACHE_FILE):
        try:
            with open(CHAR_CACHE_FILE, "r", encoding="utf-8") as f:
                cached_by_project = json.load(f)
        except Exception:
            cached_by_project = {}

    project_cache = cached_by_project.get(PROJECT_ID, {}) if isinstance(cached_by_project, dict) else {}

    remote_chars = []
    remote_images = []
    remote_query_ok = False
    try:
        r = requests.get(f"{FLOWKIT_API}/api/flow/project-characters", params={"project_id": PROJECT_ID}, timeout=30)
        if r.status_code == 200:
            rdata = r.json()
            remote_chars = rdata.get("characters") or []
            remote_images = rdata.get("images") or []
            remote_query_ok = True
            log(f"✅ Project {PROJECT_ID} hiện có {len(remote_chars)} nhân vật & {len(remote_images)} ảnh mẫu trên Google Flow")
    except Exception as e:
        log(f"⚠️ Không truy vấn được danh sách nhân vật từ Google Flow (sẽ dùng ID khóa sẵn): {e}")

    remote_valid_ids = {
        rc.get("media_id") for rc in remote_chars if rc.get("media_id")
    } | {
        ri.get("media_id") for ri in remote_images if ri.get("media_id")
    }

    locked = {}
    created_any = False
    for spec in CHARACTER_SPECS:
        tag = spec["tag"]
        tag_clean = tag.lower().lstrip("@")
        aliases_lower = {a.lower().lstrip("@") for a in spec["aliases"]}
        matched_mid = None

        for rc in remote_chars:
            rc_name = (rc.get("name") or "").strip().lower().lstrip("@")
            if (rc_name == tag_clean or rc_name in aliases_lower) and rc.get("media_id"):
                matched_mid = rc["media_id"]
                break

        if not matched_mid and not remote_query_ok:
            for ri in remote_images:
                ri_title = (ri.get("title") or "").strip().lower().lstrip("@")
                if (ri_title == tag_clean or ri_title in aliases_lower) and ri.get("media_id"):
                    matched_mid = ri["media_id"]
                    break

        if not matched_mid and not remote_query_ok and project_cache.get(tag):
            cand = project_cache[tag]
            if not remote_query_ok or cand in remote_valid_ids:
                matched_mid = cand

        if not matched_mid and not remote_query_ok and spec.get("default_media_id"):
            cand = spec["default_media_id"]
            if not remote_query_ok or cand in remote_valid_ids:
                matched_mid = cand

        # Tự động tạo Nhân Vật (Character Entity + Ảnh mẫu Nano Banana Pro 16:9) nếu chưa có trong mục Characters trên Project
        if not matched_mid and spec.get("ref_prompt"):
            log(f"🎨 Đang tự động tạo Nhân Vật & ảnh mẫu cố định cho {tag} trên Google Flow Project {PROJECT_ID}...")
            try:
                gen_res = requests.post(
                    f"{FLOWKIT_API}/api/flow/create-character",
                    json={
                        "name": tag,
                        "prompt": spec["ref_prompt"],
                        "description": spec.get("description", ""),
                        "project_id": PROJECT_ID,
                        "aspect_ratio": IMAGE_ASPECT_RATIO,
                        "image_model": "nano_banana_pro",
                    },
                    timeout=120,
                )
                if gen_res.status_code == 200:
                    gdata = gen_res.json()
                    matched_mid = gdata.get("_mediaId") or gdata.get("media_id")
                    char_entity_id = gdata.get("characterId")
                    img_url = None
                    if not matched_mid:
                        medias = gdata.get("media") or (gdata.get("data") or {}).get("media") or []
                        if medias and isinstance(medias[0], dict):
                            matched_mid = medias[0].get("name") or medias[0].get("media_id")
                            if not char_entity_id:
                                char_entity_id = medias[0].get("character_id")
                            img_url = (medias[0].get("image") or {}).get("fifeUrl") or medias[0].get("url")
                    if matched_mid:
                        created_any = True
                        log(f"✅ Đã tạo xong Nhân Vật {tag} (characterId={char_entity_id}) -> media_id = {matched_mid}")
                        try:
                            requests.post(
                                f"{FLOWKIT_API}/api/flow/rename-asset",
                                json={"display_name": tag, "media_id": matched_mid, "project_id": PROJECT_ID},
                                timeout=20,
                            )
                        except Exception:
                            pass
                        if img_url:
                            try:
                                ir = requests.get(img_url, timeout=30)
                                if ir.status_code == 200:
                                    img_path = os.path.join(CHAR_REFS_DIR, f"{spec['key']}.jpg")
                                    with open(img_path, "wb") as imgf:
                                        imgf.write(ir.content)
                            except Exception:
                                pass
                    time.sleep(3)
                else:
                    log(f"⚠️ Không tự tạo được nhân vật cho {tag} (HTTP {gen_res.status_code}): {gen_res.text[:200]}")
            except Exception as e:
                log(f"⚠️ Ngoại lệ khi tự tạo nhân vật cho {tag}: {e}")

        # Fallback nếu API tạo mới tạm thời lỗi thì dùng lại ảnh có sẵn trong project
        if not matched_mid:
            for ri in remote_images:
                ri_title = (ri.get("title") or "").strip().lower().lstrip("@")
                if (ri_title == tag_clean or ri_title in aliases_lower) and ri.get("media_id"):
                    matched_mid = ri["media_id"]
                    break
        if not matched_mid and project_cache.get(tag):
            cand = project_cache[tag]
            if not remote_query_ok or cand in remote_valid_ids:
                matched_mid = cand
        if not matched_mid and spec.get("default_media_id"):
            cand = spec["default_media_id"]
            if not remote_query_ok or cand in remote_valid_ids:
                matched_mid = cand

        if matched_mid:
            locked[tag] = matched_mid
            spec["default_media_id"] = matched_mid
        else:
            log(f"ℹ️ Nhân vật {tag} chưa có media_id trên Google Flow Project {PROJECT_ID}.")

    LOCKED_CHARACTER_MEDIA_IDS = locked

    try:
        if not isinstance(cached_by_project, dict):
            cached_by_project = {}
        cached_by_project[PROJECT_ID] = locked
        with open(CHAR_CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(cached_by_project, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

    if locked and (remote_chars or created_any):
        try:
            import re as _re
            self_path = os.path.abspath(__file__)
            with open(self_path, "r", encoding="utf-8") as rf:
                self_code = rf.read()
            self_code = _re.sub(r'^PROJECT_ID\s*=\s*"[^"]*"', f'PROJECT_ID = "{PROJECT_ID}"', self_code, count=1, flags=_re.MULTILINE)
            for t_tag, t_mid in locked.items():
                pat = rf'("tag":\s*"{_re.escape(t_tag)}"[\s\S]*?"default_media_id":\s*)"[^"]*"'
                self_code = _re.sub(pat, rf'\1"{t_mid}"', self_code, count=1)
            with open(self_path, "w", encoding="utf-8") as rf:
                rf.write(self_code)
        except Exception:
            pass

        try:
            import re as _re
            bible_path = os.path.join(SERIES_DIR, "film_bible.py")
            if os.path.exists(bible_path):
                with open(bible_path, "r", encoding="utf-8") as bf:
                    bible_code = bf.read()
                for t_tag, t_mid in locked.items():
                    pat = rf'("tag":\s*"{_re.escape(t_tag)}"[\s\S]*?"media_id":\s*)"[^"]*"'
                    bible_code = _re.sub(pat, rf'\1"{t_mid}"', bible_code, count=1)
                with open(bible_path, "w", encoding="utf-8") as bf:
                    bf.write(bible_code)
        except Exception:
            pass

        try:
            plan_path = os.path.join(SERIES_DIR, "PHAN_CANH_V3.json")
            if os.path.exists(plan_path):
                with open(plan_path, "r", encoding="utf-8") as pf:
                    plan_data = json.load(pf)
                for _ik, iv in (plan_data.get("identities") or {}).items():
                    itag = iv.get("tag")
                    if itag and locked.get(itag):
                        iv["media_id"] = locked[itag]
                with open(plan_path, "w", encoding="utf-8") as pf:
                    json.dump(plan_data, pf, ensure_ascii=False, indent=2)
        except Exception:
            pass

    box_items = [("Project ID", PROJECT_ID)]
    for spec in CHARACTER_SPECS:
        tag = spec["tag"]
        mid = LOCKED_CHARACTER_MEDIA_IDS.get(tag, "Chưa tạo trên Flow")
        box_items.append((f"Nhân Vật {tag}", f"media_id = {mid}"))
    box_items.append(("Chế Độ Khóa", "Ingredients R2V (/api/flow/generate-video-omni) + Seamless I2V"))
    print_box("🔒 ĐỒNG BỘ 12 NHÂN VẬT TỪ GOOGLE FLOW (CHARACTER LOCK)", box_items)


def is_new_scene_clip(prompt: str, clip_num: int, start_image_media_id: str = None) -> bool:
    """16:9 YouTube films cut continuously between camera angles; every clip opens with [FORMAT] and uses Ingredients R2V / Text-to-Video without chaining the previous clip's last frame."""
    return True


def get_clip_reference_media_ids(prompt: str) -> list:
    import re as _re
    # V3 declares visible people and printed portraits separately from voice-only
    # speakers and the previous-shot handoff. Those names must not spawn bodies.
    if "[CHARACTERS" in prompt:
        reference_sections = _re.findall(
            r"^\[(?:CHARACTERS[^\]]*|PICTURE-ONLY REFERENCES)\]\s*\n(.*?)(?=^\[|\Z)",
            prompt,
            flags=_re.MULTILINE | _re.DOTALL,
        )
        reference_text = "\n".join(reference_sections)
        selected = []
        for spec in CHARACTER_SPECS:
            tag = spec["tag"]
            mid = LOCKED_CHARACTER_MEDIA_IDS.get(tag)
            tag_pat = rf"(?<![a-zA-Z0-9_À-ỹ]){_re.escape(tag)}(?![a-zA-Z0-9_À-ỹ])"
            if mid and _re.search(tag_pat, reference_text, flags=_re.IGNORECASE):
                if mid not in selected:
                    selected.append(mid)
        return selected[:7]
    selected = []
    for spec in CHARACTER_SPECS:
        tag = spec["tag"]
        mid = LOCKED_CHARACTER_MEDIA_IDS.get(tag)
        if not mid:
            continue
        tag_pat = rf"(?<![a-zA-Z0-9_À-ỹ]){_re.escape(tag)}(?![a-zA-Z0-9_À-ỹ])"
        if _re.search(tag_pat, prompt, flags=_re.IGNORECASE):
            if mid not in selected:
                selected.append(mid)
            continue
        for alias in spec["aliases"]:
            if len(alias) <= 3 and not alias.startswith("@"):
                continue
            alias_pat = rf"(?<![a-zA-Z0-9_À-ỹ]){_re.escape(alias)}(?![a-zA-Z0-9_À-ỹ])"
            if _re.search(alias_pat, prompt, flags=_re.IGNORECASE):
                if mid not in selected:
                    selected.append(mid)
                break
    return selected[:7]


# -------------------------------------------------------------
# 1. ĐỒNG BỘ DỰ ÁN VỚI DASHBOARD UI (DATABASE SYNC)
# -------------------------------------------------------------
def sync_dashboard_database(start_scene: int = 1, end_scene: int = 40):
    """Đồng bộ tức thì Project, 12 Characters, Video, 40 Cảnh (240 Scenes/Clips) trực tiếp vào SQLite (flow_agent.db)."""
    global CURRENT_VIDEO_ID, SCENE_DB_MAP
    log("🔄 Đang đồng bộ cơ sở dữ liệu với Dashboard UI (40 cảnh / 240 clips = 40 phút)...")

    db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "flow_agent.db")
    try:
        import sqlite3
        conn = sqlite3.connect(db_path, timeout=30)
        desc_40m = "Phim hành động tốc độ cao 40 phút (16:9, 4 Tập × 10 Cảnh = 40 cảnh × 6 clip = 240 clips)."
        conn.execute(
            """INSERT INTO project (id, name, description, story, material, status, user_paygate_tier)
               VALUES (?, ?, ?, ?, ?, ?, ?)
               ON CONFLICT(id) DO UPDATE SET
                 name=excluded.name,
                 description=excluded.description,
                 story=excluded.story""",
            (
                PROJECT_ID,
                "Đường Đua Sinh Tử: 10 Giây Tự Do",
                desc_40m,
                "Sĩ quan cảnh sát chìm Tom thâm nhập vào đội đua xe đường phố của Micdo để điều tra chuỗi vụ chặn xe tải trên xa lộ Los Angeles, nhưng ranh giới giữa huy hiệu cảnh sát và tình anh em bị đẩy tới giới hạn trong 10 giây quyết định.",
                "realistic",
                "ACTIVE",
                "PAYGATE_TIER_TWO",
            ),
        )
        chars_json = []
        for idx, spec in enumerate(CHARACTER_SPECS, start=1):
            mid = LOCKED_CHARACTER_MEDIA_IDS.get(spec["tag"]) or spec.get("default_media_id") or ""
            chars_json.append(
                {
                    "tag": spec["tag"],
                    "name": spec["tag"].lstrip("@"),
                    "default_media_id": mid,
                    "locked_media_id": mid,
                    "description": spec["description"],
                    "ref_prompt": spec["ref_prompt"],
                }
            )
            cid = f"char-ddst-{idx:02d}"
            conn.execute(
                """INSERT INTO character (id, name, description, image_prompt, entity_type, media_id)
                   VALUES (?, ?, ?, ?, ?, ?)
                   ON CONFLICT(id) DO UPDATE SET
                     name=excluded.name,
                     description=excluded.description,
                     image_prompt=excluded.image_prompt,
                     media_id=excluded.media_id""",
                (cid, spec["tag"].lstrip("@"), spec["description"], spec["ref_prompt"], "character", mid or None),
            )
            conn.execute(
                "INSERT OR IGNORE INTO project_character (project_id, character_id) VALUES (?, ?)",
                (PROJECT_ID, cid),
            )

        conn.execute(
            "UPDATE cms_channel SET project_id = ?, description = ?, characters_json = ? WHERE slug = ?",
            (PROJECT_ID, desc_40m, json.dumps(chars_json, ensure_ascii=False), CHANNEL_SLUG),
        )
        conn.execute("DELETE FROM cms_episode WHERE channel_slug = ? AND episode_num > 40", (CHANNEL_SLUG,))
        conn.execute("DELETE FROM cms_clip WHERE channel_slug = ? AND episode_num > 40", (CHANNEL_SLUG,))

        vrow = conn.execute("SELECT id FROM video WHERE project_id = ? LIMIT 1", (PROJECT_ID,)).fetchone()
        if vrow:
            CURRENT_VIDEO_ID = vrow[0]
            conn.execute(
                "UPDATE video SET title = ? WHERE id = ?",
                ("Đường Đua Sinh Tử: 10 Giây Tự Do (40 Phút — Cảnh 01 - 40)", CURRENT_VIDEO_ID),
            )
        else:
            CURRENT_VIDEO_ID = "video-ddst-01"
            conn.execute(
                """INSERT INTO video (id, project_id, title, description, orientation, status)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (
                    CURRENT_VIDEO_ID,
                    PROJECT_ID,
                    "Đường Đua Sinh Tử: 10 Giây Tự Do (40 Phút — Cảnh 01 - 40)",
                    desc_40m,
                    "HORIZONTAL",
                    "DRAFT",
                ),
            )

        conn.execute("DELETE FROM scene WHERE video_id = ? AND display_order >= 240", (CURRENT_VIDEO_ID,))

        for s_idx in range(1, 41):
            scene_dir = os.path.join(SERIES_DIR, f"canh-{s_idx:02d}")
            ep_id = f"{CHANNEL_SLUG}:ep:{s_idx}"
            rendered_in_ep = 0
            for c_idx in range(1, 7):
                ord_int = (s_idx - 1) * 6 + (c_idx - 1)
                sc_id = f"scene-ddst-{s_idx:02d}-{c_idx:02d}"
                fpath = os.path.join(scene_dir, f"clip-{c_idx}.md")
                prompt_txt = ""
                if os.path.exists(fpath):
                    try:
                        with open(fpath, "r", encoding="utf-8") as pf:
                            prompt_txt = pf.read().strip()
                    except Exception:
                        prompt_txt = ""
                chain_type = "ROOT" if is_new_scene_clip(prompt_txt, c_idx, "CHECK_CONTINUE") else "CONTINUATION"
                existing_mp4 = os.path.join(OUTPUT_VIDEOS_DIR, f"canh-{s_idx:02d}", f"canh-{s_idx:02d}_clip-{c_idx:02d}.mp4")
                has_mp4 = os.path.exists(existing_mp4) and os.path.getsize(existing_mp4) > 50_000
                if has_mp4:
                    rendered_in_ep += 1
                conn.execute(
                    """INSERT INTO scene (id, video_id, display_order, chain_type, prompt, video_prompt, horizontal_video_status, horizontal_video_url)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                       ON CONFLICT(id) DO UPDATE SET
                         video_id=excluded.video_id,
                         display_order=excluded.display_order,
                         chain_type=excluded.chain_type,
                         prompt=excluded.prompt,
                         video_prompt=excluded.video_prompt,
                         horizontal_video_status=CASE WHEN excluded.horizontal_video_status='COMPLETED' THEN 'COMPLETED' ELSE scene.horizontal_video_status END,
                         horizontal_video_url= COALESCE(excluded.horizontal_video_url, scene.horizontal_video_url)""",
                    (
                        sc_id,
                        CURRENT_VIDEO_ID,
                        ord_int,
                        chain_type,
                        f"[CẢNH {s_idx:02d} - CLIP {c_idx:02d}]",
                        prompt_txt,
                        "COMPLETED" if has_mp4 else "PENDING",
                        existing_mp4 if has_mp4 else None,
                    ),
                )
                clip_id = f"{CHANNEL_SLUG}:ep:{s_idx}:clip:{c_idx}"
                conn.execute(
                    """INSERT INTO cms_clip (id, channel_slug, project_id, episode_num, folder_name, clip_num, prompt, status, local_path)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                       ON CONFLICT(id) DO UPDATE SET
                         project_id=excluded.project_id,
                         folder_name=excluded.folder_name,
                         prompt=excluded.prompt,
                         status=CASE WHEN excluded.status='COMPLETED' THEN 'COMPLETED' ELSE cms_clip.status END,
                         local_path=COALESCE(excluded.local_path, cms_clip.local_path)""",
                    (
                        clip_id,
                        CHANNEL_SLUG,
                        PROJECT_ID,
                        s_idx,
                        f"canh-{s_idx:02d}",
                        c_idx,
                        prompt_txt,
                        "COMPLETED" if has_mp4 else "PENDING",
                        existing_mp4 if has_mp4 else None,
                    ),
                )
                SCENE_DB_MAP[f"canh_{s_idx:02d}_clip_{c_idx:02d}"] = sc_id
            conn.execute(
                """INSERT INTO cms_episode (id, channel_slug, project_id, episode_num, folder_name, label, total_clips, rendered_clips, is_complete)
                   VALUES (?, ?, ?, ?, ?, ?, 6, ?, ?)
                   ON CONFLICT(id) DO UPDATE SET
                     project_id=excluded.project_id,
                     folder_name=excluded.folder_name,
                     label=excluded.label,
                     total_clips=6,
                     rendered_clips=MAX(cms_episode.rendered_clips, excluded.rendered_clips),
                     is_complete=MAX(cms_episode.is_complete, excluded.is_complete)""",
                (
                    ep_id,
                    CHANNEL_SLUG,
                    PROJECT_ID,
                    s_idx,
                    f"canh-{s_idx:02d}",
                    f"Cảnh {s_idx:02d}",
                    rendered_in_ep,
                    1 if rendered_in_ep == 6 else 0,
                ),
            )

        conn.commit()
        conn.close()
        log(f"✅ Đã đồng bộ Dashboard DB thành công! ({len(CHARACTER_SPECS)} nhân vật & 240 clips / 40 phút sẵn sàng)")
    except Exception as e:
        log(f"⚠️ Lỗi khi đồng bộ DB Dashboard: {e}")


def update_dashboard_scene_status(scene_num: int, clip_num: int, video_url: str):
    """Cập nhật trạng thái COMPLETED và link video lên Dashboard UI ngay lập tức."""
    key = f"canh_{scene_num:02d}_clip_{clip_num:02d}"
    sid = SCENE_DB_MAP.get(key)
    db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "flow_agent.db")
    try:
        import sqlite3
        conn = sqlite3.connect(db_path, timeout=30)
        if sid:
            conn.execute(
                "UPDATE scene SET horizontal_video_url = ?, horizontal_video_status = 'COMPLETED' WHERE id = ?",
                (video_url, sid),
            )
        clip_id = f"{CHANNEL_SLUG}:ep:{scene_num}:clip:{clip_num}"
        conn.execute(
            "UPDATE cms_clip SET status = 'COMPLETED', local_path = COALESCE(local_path, ?) WHERE id = ?",
            (video_url, clip_id),
        )
        conn.commit()
        conn.close()
        log(f"🖥️ [DASHBOARD UI] Đã cập nhật Scene '{key}' thành trạng thái COMPLETED ✅")
    except Exception as e:
        log(f"⚠️ Lỗi cập nhật Dashboard Scene: {e}")


# -------------------------------------------------------------
# 2. BỘ TỰ ĐỘNG SỬA PROMPT KHI THẤT BẠI (PROMPT SANITIZER & RETRY)
# -------------------------------------------------------------
def sanitize_prompt(prompt: str, attempt: int = 1) -> str:
    return rewrite_prompt_on_failure(prompt, attempt, CHARACTER_SPECS, ASPECT_RATIO)


def update_clip_file(scene_num: int, clip_num: int, new_prompt: str):
    fpath = os.path.join(SERIES_DIR, f"canh-{scene_num:02d}", f"clip-{clip_num}.md")
    try:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_prompt)
        log(f"💾 Đã ghi đè prompt đã sửa an toàn vào: {fpath}")
    except Exception as e:
        log(f"⚠️ Lỗi khi ghi file {fpath}: {e}")


# -------------------------------------------------------------
# 3. TỰ ĐỘNG TẢI VIDEO VỀ MÁY VÀ ĐỔI TÊN THEO CẢNH
# -------------------------------------------------------------
def download_and_rename_video(video_url: str, scene_num: int, clip_num: int) -> str:
    """Tải ngay lập tức video về máy và ghi đè (overwrite) đúng file clip chuẩn theo cảnh."""
    scene_folder = os.path.join(OUTPUT_VIDEOS_DIR, f"canh-{scene_num:02d}")
    os.makedirs(scene_folder, exist_ok=True)

    filename = f"canh-{scene_num:02d}_clip-{clip_num:02d}.mp4"
    target_path = os.path.join(scene_folder, filename)
    is_overwrite = os.path.exists(target_path)
    tmp_path = f"{target_path}.tmp"

    log("📥 Đang tải video từ Google Flow về máy...")
    try:
        r = requests.get(video_url, stream=True, timeout=120)
        if r.status_code == 200:
            with open(tmp_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        f.write(chunk)
            os.replace(tmp_path, target_path)
            trim_studio_reference_frames(target_path, log_fn=log)
            size_mb = os.path.getsize(target_path) / (1024 * 1024)
            r2_sync = sync_clip_to_r2_and_d1(
                channel_slug=CHANNEL_SLUG,
                ep_num=scene_num,
                clip_num=clip_num,
                local_video_path=target_path,
                ep_folder_name=f"canh-{scene_num:02d}",
                project_id=PROJECT_ID,
            )
            box_rows = [
                ("Tên File Clip", filename),
                ("Chế Độ Lưu", "Ghi đè (Overwritten)" if is_overwrite else "Tạo mới"),
                ("Đường Dẫn Lưu", target_path),
                ("Dung Lượng", f"{size_mb:.2f} MB"),
                ("Thời Gian Hoàn Tất", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            ]
            if r2_sync.get("r2_url"):
                box_rows.append(("Cloudflare R2 URL", r2_sync["r2_url"]))
            print_box(
                "💾 CLIP HOÀN THÀNH & ĐÃ GHI ĐÈ VỀ MÁY" if is_overwrite else "💾 CLIP HOÀN THÀNH & ĐÃ TẢI VỀ MÁY",
                box_rows,
            )
            return target_path
        else:
            log(f"⚠️ Lỗi khi tải video (HTTP {r.status_code})")
    except Exception as e:
        log(f"⚠️ Ngoại lệ khi tải video: {e}")
    finally:
        if os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except Exception:
                pass
    return None


def fetch_media_video_url(media_id: str) -> str:
    """Truy vấn trực tiếp GET /api/flow/media/{media_id} để lấy signed fifeUrl."""
    if not media_id or media_id == "N/A":
        return None
    try:
        r = requests.get(f"{FLOWKIT_API}/api/flow/media/{media_id}", timeout=15)
        if r.status_code == 200:
            m_data = r.json()
            inner = m_data.get("data") if isinstance(m_data.get("data"), dict) else m_data
            video_info = inner.get("video") or {}
            fife_url = video_info.get("fifeUrl") or video_info.get("downloadUrl")
            if fife_url and fife_url.startswith("http"):
                return fife_url
    except Exception:
        pass
    return None


def extract_last_frame(video_source: str, scene_num: int, clip_num: int) -> str:
    """Trích xuất khung hình cuối cùng của clip bằng ffmpeg làm start frame cho clip sau."""
    trim_studio_reference_frames(video_source, log_fn=log)
    out_frame = os.path.join(FRAMES_DIR, f"scene_{scene_num:02d}_clip_{clip_num:02d}_last.jpg")
    log(f"🎬 Dùng ffmpeg cắt khung hình cuối (Last Frame) của Cảnh {scene_num:02d} - Clip {clip_num:02d}...")
    try:
        cmd = [
            "ffmpeg", "-y",
            "-sseof", "-0.2",
            "-i", video_source,
            "-frames:v", "1",
            "-q:v", "2",
            out_frame
        ]
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=45)
        if result.returncode == 0 and os.path.exists(out_frame) and os.path.getsize(out_frame) > 0:
            size_kb = os.path.getsize(out_frame) / 1024
            print_box(
                "🖼️ ĐÃ TRÍCH XUẤT KHUNG HÌNH CUỐI THÀNH CÔNG",
                [
                    ("Clip Nguồn", f"Cảnh {scene_num:02d} - Clip {clip_num:02d}"),
                    ("File Ảnh Nối Cảnh", os.path.basename(out_frame)),
                    ("Đường Dẫn Lưu", out_frame),
                    ("Dung Lượng Ảnh", f"{size_kb:.1f} KB"),
                    ("Mục Đích Sử Dụng", f"Nạp vào slot [Bắt đầu] cho Clip {clip_num + 1:02d} (Seamless Chaining)"),
                ]
            )
            return out_frame
        else:
            cmd_fallback = [
                "ffmpeg", "-y",
                "-ss", "00:00:09.5",
                "-i", video_source,
                "-frames:v", "1",
                "-q:v", "2",
                out_frame
            ]
            res_fb = subprocess.run(cmd_fallback, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=45)
            if res_fb.returncode == 0 and os.path.exists(out_frame) and os.path.getsize(out_frame) > 0:
                log(f"✨ Trích xuất khung hình cuối thành công (fallback ss 9.5s): {os.path.basename(out_frame)}")
                return out_frame
            else:
                log(f"⚠️ ffmpeg không trích xuất được frame: {result.stderr.decode('utf-8', errors='ignore')[:200]}")
                return None
    except Exception as e:
        log(f"⚠️ Lỗi khi trích xuất frame: {e}")
        return None


def upload_start_frame(image_path: str) -> str:
    """Nạp khung hình vừa cắt vào slot [Bắt đầu] trên Google Flow qua API."""
    if not image_path or not os.path.exists(image_path):
        return None
    url = f"{FLOWKIT_API}/api/flow/upload-image"
    try:
        with open(image_path, "rb") as f:
            b64_str = base64.b64encode(f.read()).decode("utf-8")

        payload = {
            "image_base64": b64_str,
            "project_id": PROJECT_ID,
            "file_name": os.path.basename(image_path),
            "mime_type": "image/jpeg"
        }
        res = requests.post(url, json=payload, timeout=45)
        if res.status_code == 200:
            res_json = res.json()
            media_id = (
                res_json.get("media_id")
                or res_json.get("_mediaId")
                or (res_json.get("data") or {}).get("media_id")
                or ((res_json.get("data") or {}).get("media") or {}).get("name")
            )
            print_box(
                "📤 ĐÃ TẢI ẢNH LÊN GOOGLE FLOW [BẮT ĐẦU]",
                [
                    ("Media ID", media_id),
                    ("File Ảnh Nối", os.path.basename(image_path)),
                    ("Slot Kích Hoạt", "Khung hình [Bắt đầu] (Start Frame) cho Clip tiếp theo"),
                    ("Trạng Thái", "Sẵn sàng Image-to-Video Omni Flash 10s ✅"),
                ]
            )
            return media_id
        else:
            log(f"⚠️ Không upload được frame: {res.text}")
            return None
    except Exception as e:
        log(f"⚠️ Lỗi upload frame: {e}")
        return None


# -------------------------------------------------------------
# 4. GỬI API REQUEST & LOG CHI TIẾT PARAMS (KHÓA NHÂN VẬT)
# -------------------------------------------------------------
def submit_clip_with_detailed_log(prompt: str, scene_num: int, clip_num: int, start_image_media_id: str = None):
    """Gửi yêu cầu tạo video và luôn khóa đúng nhân vật Đường Đua Sinh Tử."""
    if len(LOCKED_CHARACTER_MEDIA_IDS) < len(CHARACTER_SPECS):
        load_and_lock_project_characters()
    key = f"canh_{scene_num:02d}_clip_{clip_num:02d}"
    sid = SCENE_DB_MAP.get(key) or f"scene_{scene_num:02d}_clip_{clip_num:02d}"
    clip_tag = f"[CẢNH {scene_num:02d} - CLIP {clip_num:02d}]"
    flow_prompt = prompt if prompt.startswith(clip_tag) else f"{clip_tag}\n{prompt}"

    use_char_refs = is_new_scene_clip(prompt, clip_num, start_image_media_id)
    ref_media_ids = get_clip_reference_media_ids(prompt)

    if not use_char_refs and start_image_media_id:
        endpoint = "/api/flow/generate-video"
        mode = "🔗 Image-to-Video (Nối tiếp khung hình cuối Clip trước)"
        slot_desc = f"Start Frame = {start_image_media_id}"
        payload = {
            "start_image_media_id": start_image_media_id,
            "prompt": flow_prompt,
            "project_id": PROJECT_ID,
            "scene_id": sid,
            "duration_s": 10,
            "model_family": "omni_flash",
            "resolution": "720p",
            "aspect_ratio": ASPECT_RATIO
        }
    elif ref_media_ids:
        endpoint = "/api/flow/generate-video-omni"
        mode = f"🔒 Ingredients Reference-to-Video (Khóa {len(ref_media_ids)} nhân vật gốc Đường Đua Sinh Tử)"
        slot_desc = f"Ingredients Refs = {', '.join(ref_media_ids)}"
        payload = {
            "reference_media_ids": ref_media_ids,
            "prompt": flow_prompt,
            "project_id": PROJECT_ID,
            "scene_id": sid,
            "duration_s": 10,
            "resolution": "720p",
            "aspect_ratio": ASPECT_RATIO
        }
    else:
        endpoint = "/api/flow/generate-video-omni-text"
        mode = "🎬 Text-to-Video (Khung hình gốc mở đầu cảnh)"
        slot_desc = "[Trống - Khởi tạo từ Text]"
        payload = {
            "prompt": flow_prompt,
            "project_id": PROJECT_ID,
            "scene_id": sid,
            "duration_s": 10,
            "resolution": "720p",
            "aspect_ratio": ASPECT_RATIO
        }

    print_box(
        "📡 FLOWKIT API REQUEST CALL (CHARACTER LOCKED)",
        [
            ("Endpoint API", f"POST {endpoint}"),
            ("Tên Trên Google Flow", clip_tag),
            ("Phân Cảnh", f"Cảnh {scene_num:02d} - Clip {clip_num:02d}"),
            ("Chế Độ Tạo", mode),
            ("Khóa Hình Ảnh / Nhân Vật", slot_desc),
            ("Thời Lượng", "10 giây (Omni Flash 10s)"),
            ("Độ Phân Giải", "720p HD"),
            ("Tỉ Lệ Khung Hình", ASPECT_RATIO),
            ("Model Family", "omni_flash"),
            ("Độ Dài Prompt", f"{len(flow_prompt)} ký tự"),
            ("Prompt Preview", flow_prompt[:120].replace("\n", " ") + "..."),
        ]
    )

    url = f"{FLOWKIT_API}{endpoint}"
    res = requests.post(url, json=payload, timeout=60)
    return res


def lookup_operation_media_in_project(operation_id: str) -> str:
    """Tra cứu trực tiếp media_id của operation trong project listing trên Google Flow."""
    if not operation_id:
        return None
    try:
        r = requests.get(
            f"{FLOWKIT_API}/api/flow/debug-listing/{operation_id}",
            params={"project_id": PROJECT_ID},
            timeout=90,
        )
        if r.status_code == 200:
            return r.json().get("matched_media_id")
    except Exception:
        pass
    return None


def poll_generation(submit_res_data: dict, scene_num: int, clip_num: int, timeout_s=210):
    """Theo dõi tiến trình sinh video cho đến khi hoàn thành."""
    url = f"{FLOWKIT_API}/api/flow/check-status"
    start_time = time.time()

    flow_poll = submit_res_data.get("flowkitPolling") or {}
    workflows = submit_res_data.get("workflows") or flow_poll.get("workflows") or []
    operations = submit_res_data.get("operations") or flow_poll.get("operations") or []
    media_list = submit_res_data.get("media") or []
    primary_media_id = None
    if media_list and isinstance(media_list, list) and len(media_list) > 0:
        primary_media_id = media_list[0].get("name")
    if not primary_media_id and workflows:
        primary_media_id = workflows[0].get("primary_media_id")

    poll_mode_desc = "workflows (Text-to-Video)" if workflows else ("operations (Ingredients R2V / Image-to-Video)" if operations else "direct media")
    log(f"⏳ Đang theo dõi tiến trình tạo video [Cảnh {scene_num:02d} - Clip {clip_num:02d}] (Chế độ: {poll_mode_desc})...")

    last_logged_time = 0
    complaint_seen_count = 0
    while time.time() - start_time < timeout_s:
        elapsed = int(time.time() - start_time)
        try:
            if workflows:
                r = requests.post(url, json={"workflows": workflows, "project_id": PROJECT_ID}, timeout=120)
                if r.status_code == 200:
                    res_data = r.json()
                    st = res_data.get("status")
                    if st == "COMPLETED" or res_data.get("done") is True:
                        log(f"🎉 Google Flow render hoàn tất sau {elapsed}s!")
                        video_url = None
                        for wf in (res_data.get("workflows") or []):
                            m = wf.get("media") or {}
                            if m.get("url"):
                                video_url = m["url"]
                                break
                        if not video_url and primary_media_id:
                            video_url = fetch_media_video_url(primary_media_id)
                        if video_url:
                            force_rename_clip_on_flow(
                                FLOWKIT_API, PROJECT_ID, submit_res_data,
                                f"[CẢNH {scene_num:02d} - CLIP {clip_num:02d}]",
                                media_id=primary_media_id, log_fn=log,
                            )
                            return {"success": True, "video_url": video_url}
                    elif st in ["FAILED", "ERROR"]:
                        log(f"❌ Google Flow báo lỗi: {res_data}")
                        return {"success": False, "error": "FLOW_FAILED"}

            elif operations:
                r = requests.post(url, json={"operations": operations, "project_id": PROJECT_ID}, timeout=120)
                if r.status_code == 200:
                    res_data = r.json()
                    inner_ops = res_data.get("operations") or res_data.get("data", {}).get("operations") or []
                    all_done = True
                    has_failed = False
                    video_url = None
                    op_media_id = None
                    op_complaint = None
                    first_op_id = None

                    for op in inner_ops:
                        op_id_cand = (op.get("operation") or {}).get("name") or op.get("name")
                        if op_id_cand and not first_op_id:
                            first_op_id = op_id_cand
                        op_status = op.get("status", "")
                        if op.get("complaint"):
                            op_complaint = op.get("complaint")
                        op_meta = op.get("operation", {}).get("metadata", {}).get("video", {})
                        if not op_meta:
                            op_meta = op.get("metadata", {}).get("video", {})
                        if op_meta.get("mediaId"):
                            op_media_id = op_meta.get("mediaId")
                        if op_status == "MEDIA_GENERATION_STATUS_SUCCESSFUL":
                            v_url = op_meta.get("fifeUrl") or op_meta.get("downloadUrl")
                            if v_url:
                                video_url = v_url
                        elif op_status == "MEDIA_GENERATION_STATUS_FAILED":
                            has_failed = True
                            all_done = False
                        else:
                            all_done = False

                    if not first_op_id and operations:
                        op0 = operations[0] if isinstance(operations[0], dict) else {}
                        first_op_id = (op0.get("operation") or {}).get("name") or op0.get("name")

                    if has_failed:
                        log(f"❌ Operation thất bại: {res_data}")
                        return {"success": False, "error": "OPERATION_FAILED"}

                    # Nếu backend thiếu project_id trong cache, chủ động tra cứu trực tiếp qua debug-listing
                    if not op_media_id and first_op_id and elapsed >= 36:
                        if op_complaint == "no project id for the listing lookup" or elapsed % 18 < 6:
                            looked_up_mid = lookup_operation_media_in_project(first_op_id)
                            if looked_up_mid:
                                op_media_id = looked_up_mid
                                primary_media_id = looked_up_mid
                                direct_v_url = fetch_media_video_url(looked_up_mid)
                                if direct_v_url:
                                    log(f"🎉 Phát hiện video hoàn tất qua Project Listing sau {elapsed}s!")
                                    force_rename_clip_on_flow(
                                        FLOWKIT_API, PROJECT_ID, submit_res_data,
                                        f"[CẢNH {scene_num:02d} - CLIP {clip_num:02d}]",
                                        media_id=looked_up_mid, log_fn=log,
                                    )
                                    return {"success": True, "video_url": direct_v_url}

                    if (
                        op_complaint
                        and op_complaint != "no project id for the listing lookup"
                        and not op_media_id
                    ):
                        complaint_seen_count += 1
                        if elapsed >= 110 and complaint_seen_count >= 5:
                            looked_up_mid = lookup_operation_media_in_project(first_op_id) if first_op_id else None
                            if looked_up_mid:
                                op_media_id = looked_up_mid
                                primary_media_id = looked_up_mid
                                direct_v_url = fetch_media_video_url(looked_up_mid)
                                if direct_v_url:
                                    log(f"🎉 Phát hiện video hoàn tất qua Project Listing sau {elapsed}s!")
                                    force_rename_clip_on_flow(
                                        FLOWKIT_API, PROJECT_ID, submit_res_data,
                                        f"[CẢNH {scene_num:02d} - CLIP {clip_num:02d}]",
                                        media_id=looked_up_mid, log_fn=log,
                                    )
                                    return {"success": True, "video_url": direct_v_url}
                            else:
                                log(f"⚠️ Google Flow báo lỗi/từ chối operation ({op_complaint}) sau {elapsed}s và không sinh media — chuyển sang thử lại!")
                                return {"success": False, "error": f"FLOW_COMPLAINT: {op_complaint}"}

                    if all_done and inner_ops:
                        log(f"🎉 Google Flow render hoàn tất sau {elapsed}s!")
                        target_mid = op_media_id or primary_media_id
                        if not video_url and target_mid:
                            video_url = fetch_media_video_url(target_mid)
                        if video_url:
                            force_rename_clip_on_flow(
                                FLOWKIT_API, PROJECT_ID, submit_res_data,
                                f"[CẢNH {scene_num:02d} - CLIP {clip_num:02d}]",
                                media_id=target_mid, log_fn=log,
                            )
                            return {"success": True, "video_url": video_url}

            if primary_media_id and elapsed >= 30:
                direct_url = fetch_media_video_url(primary_media_id)
                if direct_url:
                    log(f"🎉 Phát hiện video sẵn sàng qua Media API sau {elapsed}s!")
                    force_rename_clip_on_flow(
                        FLOWKIT_API, PROJECT_ID, submit_res_data,
                        f"[CẢNH {scene_num:02d} - CLIP {clip_num:02d}]",
                        media_id=primary_media_id, log_fn=log,
                    )
                    return {"success": True, "video_url": direct_url}

            if elapsed - last_logged_time >= 12:
                last_logged_time = elapsed
                log(f"   ...Google Flow đang vẽ video đúng nhân vật ({elapsed}s trôi qua)...")

        except Exception as e:
            log(f"   ...lỗi tạm thời khi poll ({e}), tiếp tục chờ...")

        time.sleep(6)

    log(f"⚠️ Hết thời gian chờ {timeout_s}s (Timeout) khi render Cảnh {scene_num:02d} - Clip {clip_num:02d}.")
    return {"success": False, "error": "TIMEOUT"}


# -------------------------------------------------------------
# 5. CHU TRÌNH ĐIỀU PHỐI TỔNG THỂ
# -------------------------------------------------------------
def _is_transient_transport_error(err_text: str) -> bool:
    t = (err_text or "").lower()
    transient_markers = (
        "no_injection_result",
        "asynchronous response",
        "message channel closed",
        "extension not connected",
        "read timed out",
        "connection aborted",
        "connection reset",
        "bad gateway",
        "service unavailable",
        "gateway timeout",
    )
    return any(m in t for m in transient_markers)


def run_clip_with_auto_retry(scene_num: int, clip_num: int, initial_prompt: str, start_image_media_id: str = None, max_retries: int = 2):
    current_prompt = initial_prompt
    policy_attempt = 0

    for attempt in range(1, max_retries + 1):
        if attempt > 1:
            log(f"🔄 Đang chạy lại Cảnh {scene_num:02d} - Clip {clip_num:02d} (Lần {attempt}/{max_retries})...")

        transient_fail = False
        try:
            res = submit_clip_with_detailed_log(current_prompt, scene_num, clip_num, start_image_media_id)
            cooldown_loops = 0
            while res.status_code != 200 and cooldown_loops < 5:
                err_body = res.text or ""
                if wait_if_cooldown_error(err_body, FLOWKIT_API, log):
                    cooldown_loops += 1
                    res = submit_clip_with_detailed_log(current_prompt, scene_num, clip_num, start_image_media_id)
                else:
                    break

            if res.status_code == 200:
                data = res.json()
                inner = data.get("data") if isinstance(data.get("data"), dict) else data
                log("✅ Google Flow đã chấp nhận job tạo video.")

                poll_res = poll_generation(inner, scene_num, clip_num)
                if poll_res["success"] and poll_res.get("video_url"):
                    return poll_res
                else:
                    log(f"⚠️ Không nhận được video URL hoàn chỉnh ở lần thử {attempt}/{max_retries} ({poll_res.get('error')}).")
            else:
                err_body = res.text or ""
                log(f"❌ Google Flow phản hồi lỗi (HTTP {res.status_code}): {err_body}")
                if _is_transient_transport_error(err_body):
                    transient_fail = True
        except Exception as e:
            log(f"❌ Lỗi ngoại lệ khi gửi job: {e}")
            if _is_transient_transport_error(str(e)):
                transient_fail = True

        if attempt < max_retries:
            if transient_fail:
                log(f"⏳ Lỗi kết nối Extension tạm thời — giữ nguyên prompt gốc và thử lại lần {attempt + 1}/{max_retries} sau 6 giây...")
                time.sleep(6)
                continue
            policy_attempt += 1
            log(f"🔧 [LÀM MỀM PROMPT TỰ ĐỘNG - LẦN THỬ {attempt + 1}/{max_retries}] Đang làm mềm prompt trong bộ nhớ cho Cảnh {scene_num:02d} - Clip {clip_num:02d} (giữ nguyên file .md chuẩn)...")
            current_prompt = sanitize_prompt(initial_prompt, policy_attempt)
            start_image_media_id = None
            log("🔄 Khóa trực tiếp nhân vật gốc (Ingredients R2V) và chạy lại sau 5 giây...")
            time.sleep(5)

    log(f"⏭️ [BỎ QUA SAU {max_retries} LẦN LỖI] Cảnh {scene_num:02d} - Clip {clip_num:02d} đã fail {max_retries} lần — tạm bỏ qua để kiểm tra và tạo lại sau!")
    return {"success": False, "video_url": None}


def run_pipeline(start_scene=1, end_scene=40):
    global CURRENT_EP_NUM, CURRENT_CLIP_NUM
    print("\n" + "=" * 72)
    print("🎬 KHỞI ĐỘNG HỆ THỐNG FLOWKIT TỰ ĐỘNG THÔNG MINH — ĐƯỜNG ĐUA SINH TỬ (40 PHÚT)")
    print(f"📁 Phạm vi: Cảnh {start_scene:02d} đến Cảnh {end_scene:02d} (6 clips/cảnh)")
    print(f"🔗 Google Flow Project: {PROJECT_ID}")
    print(f"💾 Tải video tự động về: {OUTPUT_VIDEOS_DIR}")
    print(f"🖼️ Lưu khung hình nối cảnh tại: {FRAMES_DIR}")
    print("=" * 72 + "\n", flush=True)

    if not check_connection():
        sys.exit(1)

    load_and_lock_project_characters()
    sync_dashboard_database(start_scene, end_scene)

    clip_indices = [ONLY_CLIP] if ONLY_CLIP > 0 else list(range(1, 7))
    total_clips = (end_scene - start_scene + 1) * len(clip_indices)
    completed_clips = 0
    force_rerender = os.environ.get("FLOWKIT_FORCE_RERENDER") == "1"

    for s in range(start_scene, end_scene + 1):
        CURRENT_EP_NUM = s
        print("\n" + "#" * 72)
        print(f"👉 BẮT ĐẦU CẢNH {s:02d}")
        print("#" * 72, flush=True)

        previous_clip_last_frame_media_id = None
        rendered_in_this_run = set()

        scene_dir = os.path.join(SERIES_DIR, f"canh-{s:02d}")
        for c_idx in clip_indices:
            CURRENT_CLIP_NUM = c_idx
            fpath = os.path.join(scene_dir, f"clip-{c_idx}.md")
            if not os.path.exists(fpath):
                continue

            existing_mp4 = os.path.join(OUTPUT_VIDEOS_DIR, f"canh-{s:02d}", f"canh-{s:02d}_clip-{c_idx:02d}.mp4")
            if ONLY_CLIP == 0 and not force_rerender and os.path.exists(existing_mp4) and os.path.getsize(existing_mp4) > 50_000:
                stream_info = probe_clip_streams(existing_mp4)
                if stream_info.get("has_video"):
                    completed_clips += 1
                    progress_pct = (completed_clips / max(1, total_clips)) * 100
                    size_mb = os.path.getsize(existing_mp4) / (1024 * 1024)
                    log(f"✅ [{completed_clips}/{total_clips}] ({progress_pct:.1f}%) Cảnh {s:02d} - Clip {c_idx:02d} đã tồn tại ({size_mb:.2f} MB) — bỏ qua.")
                    previous_clip_last_frame_media_id = None
                    continue

            with open(fpath, "r", encoding="utf-8") as f:
                prompt_content = f.read().strip()

            # Phim 16:9 YouTube chuyển góc máy liên tục nên không chèn frame cuối của clip trước
            previous_clip_last_frame_media_id = None

            completed_clips += 1
            progress_pct = (completed_clips / max(1, total_clips)) * 100
            print(f"\n▶️ TIẾN ĐỘ TỔNG: [{completed_clips}/{total_clips}] ({progress_pct:.1f}%) — CẢNH {s:02d} - CLIP {c_idx:02d}", flush=True)

            res = run_clip_with_auto_retry(
                scene_num=s,
                clip_num=c_idx,
                initial_prompt=prompt_content,
                start_image_media_id=None
            )

            if res["success"] and res.get("video_url"):
                video_url = res["video_url"]
                local_video = download_and_rename_video(video_url, s, c_idx)
                if local_video:
                    rendered_in_this_run.add(c_idx)
                    extract_last_frame(local_video, s, c_idx)
                previous_clip_last_frame_media_id = None
                update_dashboard_scene_status(s, c_idx, local_video if local_video else video_url)
            else:
                log(f"⚠️ [Cảnh {s:02d} - Clip {c_idx:02d}] Bị bỏ qua do không hoàn tất render.")
                previous_clip_last_frame_media_id = None

            log("⏳ Nghỉ 5 giây trước khi tiếp tục clip kế tiếp...")
            time.sleep(5)

        existing_nums = rendered_in_this_run if ONLY_CLIP > 0 else {cn for cn, _ in find_episode_clip_mp4s(OUTPUT_VIDEOS_DIR, s, f"canh-{s:02d}")}
        missing_clips = [c_idx for c_idx in clip_indices if c_idx not in existing_nums and os.path.exists(os.path.join(scene_dir, f"clip-{c_idx}.md"))]
        if missing_clips:
            log(f"⏭️ [DANH SÁCH CLIP TẠM BỎ QUA] Cảnh {s:02d} còn {len(missing_clips)} clip chưa hoàn tất ({missing_clips}).")

        CURRENT_CLIP_NUM = None
        merged_scene_mp4 = os.path.join(OUTPUT_VIDEOS_DIR, f"canh-{s:02d}", f"{CHANNEL_SLUG}_canh-{s:02d}_FULL.mp4")
        if rendered_in_this_run or not os.path.exists(merged_scene_mp4):
            merge_episode_clips(SERIES_DIR, CHANNEL_SLUG, s, f"canh-{s:02d}", project_id=PROJECT_ID, unit_label="Cảnh")
        if s % 10 == 0:
            tap_num = s // 10
            ep_full_mp4 = os.path.join(OUTPUT_VIDEOS_DIR, "_FULL_EPISODES", f"{CHANNEL_SLUG}_tap-{tap_num:02d}_FULL.mp4")
            if rendered_in_this_run or not os.path.exists(ep_full_mp4):
                merge_multi_scenes_to_episode(SERIES_DIR, CHANNEL_SLUG, tap_num, s - 9, s, project_id=PROJECT_ID)

    print("\n" + "=" * 72)
    print(f"🎉 HOÀN THÀNH TOÀN BỘ CHU TRÌNH TỪ CẢNH {start_scene:02d} ĐẾN CẢNH {end_scene:02d}!")
    print(f"📁 Video hoàn chỉnh đã được lưu tại: {OUTPUT_VIDEOS_DIR}")
    print("=" * 72 + "\n", flush=True)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ("--init-chars", "init-chars", "0"):
        check_connection()
        load_and_lock_project_characters(force_remote=True)
        sync_dashboard_database(1, 40)
        sys.exit(0)
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 40
    run_pipeline(start, end)

