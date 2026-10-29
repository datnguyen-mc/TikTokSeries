"""Configuration constants."""
import json
import os
from pathlib import Path

# ─── Paths ───────────────────────────────────────────────────
BASE_DIR = Path(os.environ.get("FLOW_AGENT_DIR", Path(__file__).parent.parent))
DB_PATH = BASE_DIR / "flow_agent.db"

# Load .env file if present in flowkit/
_ENV_FILE = BASE_DIR / ".env"
if _ENV_FILE.is_file():
    for _line in _ENV_FILE.read_text(encoding="utf-8").splitlines():
        _line = _line.strip()
        if _line and not _line.startswith("#") and "=" in _line:
            _k, _v = _line.split("=", 1)
            os.environ.setdefault(_k.strip(), _v.strip().strip('"').strip("'"))

# ─── API Server ──────────────────────────────────────────────
API_HOST = os.environ.get("API_HOST", "127.0.0.1")
API_PORT = int(os.environ.get("API_PORT", "8200"))

# ─── WebSocket Server (extension connects here) ─────────────
WS_HOST = os.environ.get("WS_HOST", "127.0.0.1")
WS_PORT = int(os.environ.get("WS_PORT", "9222"))


# ─── Flow batchexecute ──────────────────────────────────────
# Every call is signed in the page with the session cookie plus a per-page `at`
# token, so the extension runs it inside a signed-in flow.google.com tab. This
# is the only transport; the REST path it replaced was removed once Flow stopped
# minting the bearer it needed.

# The Flow project every RPC is scoped to. Project creation went with the old
# labs.google tRPC endpoint, so a project is made once in the Flow UI and its
# uuid pinned here; POST /api/projects falls back to it when no id is given.
FLOW_PROJECT_ID = os.environ.get("FLOW_PROJECT_ID", "")

# Capabilities whose payloads were never captured off the new UI (4K upscale,
# reference-to-video, start+end-frame chaining) fail loudly by default. With
# this on, the two that have a sane fallback degrade instead: chaining and r2v
# both drop to plain i2v off the start frame. Upscale has no fallback.
FLOW_ALLOW_DEGRADED = os.environ.get("FLOW_ALLOW_DEGRADED", "0") == "1"

# Process-wide guard for every CAPTCHA-bearing generation submit, including
# direct API calls that bypass the background worker's limiter.
FLOW_GENERATION_MIN_INTERVAL_S = max(
    0.0, float(os.environ.get("FLOW_GENERATION_MIN_INTERVAL_S", "3"))
)
FLOW_GENERATION_MAX_CONCURRENT = max(
    1, int(os.environ.get("FLOW_GENERATION_MAX_CONCURRENT", "1"))
)
# After Google answers PUBLIC_ERROR_UNUSUAL_ACTIVITY, no generation is submitted
# for this long. The hold is written to FLOW_GENERATION_HOLD_PATH so a restart
# does not lift it (#67): retrying into the block may be what prolongs it.
FLOW_UNUSUAL_ACTIVITY_COOLDOWN_S = max(
    0.0, float(os.environ.get("FLOW_UNUSUAL_ACTIVITY_COOLDOWN_S", "3600"))
)
FLOW_GENERATION_HOLD_PATH = BASE_DIR / "flow_generation_hold.json"
FLOW_SESSION_PROJECT_IDLE_S = max(
    300.0, float(os.environ.get("FLOW_SESSION_PROJECT_IDLE_S", "7200"))
)

# The tier no longer picks a model — aspect is its own slot and the model names
# are fixed — so it is only carried for the DB column and the dashboard.
DEFAULT_PAYGATE_TIER = os.environ.get("DEFAULT_PAYGATE_TIER", "PAYGATE_TIER_TWO")

# ─── Media Provider ─────────────────────────────────────────
# "flow" (default): generate via Google Flow through the Chrome extension.
# "assistant": route all generation to the AI assistant instead — each request
# is published as a row in the provider_job table and the worker waits for an
# external worker (the assistant) to claim and complete it via
# /api/provider-jobs. See agent/sdk/services/assistant_provider.py and
# agent/worker/assistant_worker.py for the full protocol.
# Default media provider for requests that don't specify one ("flow" |
# "assistant" | "muse2api" | any registered provider name). MEDIA_PROVIDER is kept as a
# legacy alias — DEFAULT_PROVIDER wins if both are set.
DEFAULT_PROVIDER = os.environ.get(
    "DEFAULT_PROVIDER", os.environ.get("MEDIA_PROVIDER", "flow")
).strip().lower()
MEDIA_PROVIDER = DEFAULT_PROVIDER  # legacy alias
ASSISTANT_PROVIDER_TIMEOUT_S = int(os.environ.get("ASSISTANT_PROVIDER_TIMEOUT_S", "1800"))
ASSISTANT_PROVIDER_POLL_S = int(os.environ.get("ASSISTANT_PROVIDER_POLL_S", "15"))
ASSISTANT_MAX_CONCURRENT = int(os.environ.get("ASSISTANT_MAX_CONCURRENT", "2"))
ASSISTANT_COOLDOWN_S = float(os.environ.get("ASSISTANT_COOLDOWN_S", "0"))

# "muse2api": render through a muse2api gateway (https://github.com/crisng95/muse2api),
# which fronts the muse.ai web app with an OpenAI-compatible API. The provider
# is registered always and becomes available once MUSE2API_URL is set; the key
# is the gateway's own MUSE2API_API_KEY. See agent/sdk/services/muse2api_provider.py.
MUSE2API_URL = os.environ.get("MUSE2API_URL", "").strip().rstrip("/")
MUSE2API_KEY = os.environ.get("MUSE2API_KEY", "")
MUSE2API_IMAGE_MODEL = os.environ.get("MUSE2API_IMAGE_MODEL", "muse-image")
MUSE2API_VIDEO_MODEL = os.environ.get("MUSE2API_VIDEO_MODEL", "muse-video")
MUSE2API_VIDEO_SECONDS = int(os.environ.get("MUSE2API_VIDEO_SECONDS", "8"))
# Covers the gateway's own failover (up to 3 accounts x its 240s/600s timeouts).
MUSE2API_TIMEOUT_S = float(os.environ.get("MUSE2API_TIMEOUT_S", "1800"))
MUSE2API_POLL_S = float(os.environ.get("MUSE2API_POLL_S", "5"))
MUSE2API_MAX_CONCURRENT = int(os.environ.get("MUSE2API_MAX_CONCURRENT", "2"))
MUSE2API_COOLDOWN_S = float(os.environ.get("MUSE2API_COOLDOWN_S", "0"))
# muse.ai takes a first frame only. With this on, chained scenes drop the end
# frame and r2v renders as i2v; off, both fail loudly (same rule as Flow).
MUSE2API_ALLOW_DEGRADED = os.environ.get("MUSE2API_ALLOW_DEGRADED", "0") == "1"

# ─── Worker ──────────────────────────────────────────────────
POLL_INTERVAL = int(os.environ.get("POLL_INTERVAL", "5"))
VIDEO_POLL_INTERVAL = int(os.environ.get("VIDEO_POLL_INTERVAL", "10"))  # polling interval for video/upscale status
MAX_RETRIES = int(os.environ.get("MAX_RETRIES", "5"))
VIDEO_POLL_TIMEOUT = int(os.environ.get("VIDEO_POLL_TIMEOUT", "420"))
# Omni Flash defaults used by the worker when a project's video_model_family
# is "omni_flash". Duration must be 4/6/8/10; resolution 360p or 720p.
OMNI_FLASH_DURATION_S = int(os.environ.get("OMNI_FLASH_DURATION_S", "8"))
OMNI_FLASH_RESOLUTION = os.environ.get("OMNI_FLASH_RESOLUTION", "720p")
# Flow provider pacing. Every generate mints a reCAPTCHA inside the Flow tab;
# firing them back-to-back from a background tab degrades the session score
# until Google answers PUBLIC_ERROR_UNUSUAL_ACTIVITY. Slow down when that hits.
FLOW_MAX_CONCURRENT = int(os.environ.get("FLOW_MAX_CONCURRENT", "5"))
FLOW_COOLDOWN_S = float(os.environ.get("FLOW_COOLDOWN_S", "10"))
API_COOLDOWN = int(os.environ.get("API_COOLDOWN", "10"))  # DEPRECATED: per-provider cooldown_s in provider capabilities is authoritative
MAX_CONCURRENT_REQUESTS = int(os.environ.get("MAX_CONCURRENT_REQUESTS", "5"))  # DEPRECATED: per-provider max_concurrent in provider capabilities is authoritative
STALE_PROCESSING_TIMEOUT = int(os.environ.get("STALE_PROCESSING_TIMEOUT", "600"))  # 10 min

# ─── Model Keys (loaded from models.json for easy updates) ──
_MODELS_FILE = Path(__file__).parent / "models.json"
with open(_MODELS_FILE, encoding="utf-8") as _f:
    _MODELS = json.load(_f)

VIDEO_MODELS = _MODELS["video_models"]
UPSCALE_MODELS = _MODELS["upscale_models"]
IMAGE_MODELS = _MODELS["image_models"]
# Nickname from image_models. Known aliases live in models.json, while the
# batch path also accepts syntactically valid Flow wire model ids directly so
# newly introduced image models do not require a Flow Kit release.
DEFAULT_IMAGE_MODEL = _MODELS.get("default_image_model", "NANO_BANANA_PRO")

# ─── Output Directories ─────────────────────────────────────
OUTPUT_DIR = BASE_DIR / "output"
SHARED_OUTPUT_DIR = OUTPUT_DIR / "_shared"
TTS_TEMPLATES_DIR = SHARED_OUTPUT_DIR / "tts_templates"
MUSIC_OUTPUT_DIR = SHARED_OUTPUT_DIR / "music"

# ─── TTS (OmniVoice) ─────────────────────────────────────────
TTS_MODEL = os.environ.get("TTS_MODEL", "k2-fsa/OmniVoice")
TTS_DEVICE = os.environ.get("TTS_DEVICE", "cpu")  # MPS produces gibberish; CPU+fp32 works
TTS_SAMPLE_RATE = int(os.environ.get("TTS_SAMPLE_RATE", "24000"))

# ─── Review / Claude Vision ──────────────────────────────────
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
REVIEW_MODEL = os.environ.get("REVIEW_MODEL", "claude-haiku-4-5-20251001")
REVIEW_FPS_LIGHT = float(os.environ.get("REVIEW_FPS_LIGHT", "4"))
REVIEW_FPS_DEEP = float(os.environ.get("REVIEW_FPS_DEEP", "8"))
REVIEW_MAX_FRAMES = int(os.environ.get("REVIEW_MAX_FRAMES", "64"))
REVIEW_SHEET_COLS = int(os.environ.get("REVIEW_SHEET_COLS", "3"))
REVIEW_SHEET_ROWS = int(os.environ.get("REVIEW_SHEET_ROWS", "3"))

# ─── CLI Providers (video review vision analysis) ────────────
_PROVIDERS_FILE = Path(__file__).parent / "providers.json"
with open(_PROVIDERS_FILE, encoding="utf-8") as _pvf:
    CLI_PROVIDERS = json.load(_pvf)  # mutable dict, hot-reloaded like VIDEO_MODELS
REVIEW_CLI_TIMEOUT_S = float(os.environ.get("REVIEW_CLI_TIMEOUT_S", "120"))

# ─── Suno (Music Generation) — sunoapi.org ──────────────────
def _load_suno_key() -> str:
    """Load Suno API key: env var first, then channel_rules.json fallback."""
    key = os.environ.get("SUNO_API_KEY", "")
    if key:
        return key
    channels_dir = BASE_DIR / "youtube" / "channels"
    if channels_dir.exists():
        for rules_file in channels_dir.glob("*/channel_rules.json"):
            try:
                rules = json.loads(rules_file.read_text(encoding="utf-8"))
                key = rules.get("api_keys", {}).get("suno", "")
                if key:
                    return key
            except (json.JSONDecodeError, OSError):
                continue
    return ""

SUNO_API_KEY = _load_suno_key()
SUNO_BASE_URL = os.environ.get("SUNO_BASE_URL", "https://api.sunoapi.org")
SUNO_MODEL = os.environ.get("SUNO_MODEL", "V4")
SUNO_CALLBACK_URL = os.environ.get("SUNO_CALLBACK_URL", f"http://{API_HOST}:{API_PORT}/api/music/callback")
SUNO_POLL_INTERVAL = int(os.environ.get("SUNO_POLL_INTERVAL", "5"))
SUNO_POLL_TIMEOUT = int(os.environ.get("SUNO_POLL_TIMEOUT", "600"))

# ─── Cloudflare D1 SQL & R2 Object Storage ───────────────────
DB_BACKEND = os.environ.get("DB_BACKEND", "d1").strip().lower()
CF_ACCOUNT_ID = os.environ.get("CF_ACCOUNT_ID", "").strip()
CF_API_TOKEN = os.environ.get("CF_API_TOKEN", "").strip()
CF_D1_DATABASE_ID = os.environ.get("CF_D1_DATABASE_ID", "").strip()

R2_AUTO_UPLOAD = os.environ.get("R2_AUTO_UPLOAD", "1").strip() not in ("0", "false", "no")
R2_ACCOUNT_ID = os.environ.get("R2_ACCOUNT_ID", "").strip() or CF_ACCOUNT_ID
R2_ACCESS_KEY_ID = os.environ.get("R2_ACCESS_KEY_ID", "").strip()
R2_SECRET_ACCESS_KEY = os.environ.get("R2_SECRET_ACCESS_KEY", "").strip()
R2_BUCKET_NAME = os.environ.get("R2_BUCKET_NAME", "tiktok-series").strip()
R2_PUBLIC_URL = os.environ.get("R2_PUBLIC_URL", "").strip().rstrip("/")
R2_ENDPOINT_URL = os.environ.get("R2_ENDPOINT_URL", "").strip().rstrip("/")
R2_KEY_PREFIX = os.environ.get("R2_KEY_PREFIX", "series").strip().strip("/")


def get_cloud_config() -> dict:
    """Read live Cloudflare D1 & R2 configuration from environment and .env."""
    if _ENV_FILE.is_file():
        for _line in _ENV_FILE.read_text(encoding="utf-8").splitlines():
            _line = _line.strip()
            if _line and not _line.startswith("#") and "=" in _line:
                _k, _v = _line.split("=", 1)
                _k = _k.strip()
                _v = _v.strip().strip('"').strip("'")
                if _k in (
                    "DB_BACKEND",
                    "CF_ACCOUNT_ID",
                    "CF_API_TOKEN",
                    "CF_D1_DATABASE_ID",
                    "R2_AUTO_UPLOAD",
                    "R2_ACCOUNT_ID",
                    "R2_ACCESS_KEY_ID",
                    "R2_SECRET_ACCESS_KEY",
                    "R2_BUCKET_NAME",
                    "R2_PUBLIC_URL",
                    "R2_ENDPOINT_URL",
                    "R2_KEY_PREFIX",
                ):
                    os.environ[_k] = _v

    cf_acc = os.environ.get("CF_ACCOUNT_ID", "").strip()
    r2_acc = os.environ.get("R2_ACCOUNT_ID", "").strip() or cf_acc
    r2_endpoint = os.environ.get("R2_ENDPOINT_URL", "").strip().rstrip("/")
    if not r2_endpoint and r2_acc:
        r2_endpoint = f"https://{r2_acc}.r2.cloudflarestorage.com"

    return {
        "db_backend": os.environ.get("DB_BACKEND", "d1").strip().lower(),
        "cf_account_id": cf_acc,
        "cf_api_token": os.environ.get("CF_API_TOKEN", "").strip(),
        "cf_d1_database_id": os.environ.get("CF_D1_DATABASE_ID", "").strip(),
        "r2_auto_upload": os.environ.get("R2_AUTO_UPLOAD", "1").strip() not in ("0", "false", "no"),
        "r2_account_id": r2_acc,
        "r2_access_key_id": os.environ.get("R2_ACCESS_KEY_ID", "").strip(),
        "r2_secret_access_key": os.environ.get("R2_SECRET_ACCESS_KEY", "").strip(),
        "r2_bucket_name": os.environ.get("R2_BUCKET_NAME", "tiktok-series").strip() or "tiktok-series",
        "r2_public_url": os.environ.get("R2_PUBLIC_URL", "").strip().rstrip("/"),
        "r2_endpoint_url": r2_endpoint,
        "r2_key_prefix": os.environ.get("R2_KEY_PREFIX", "series").strip().strip("/"),
    }


def update_env_file(updates: dict[str, str]) -> None:
    """Persist key-value updates into flowkit/.env and os.environ."""
    lines: list[str] = []
    if _ENV_FILE.is_file():
        lines = _ENV_FILE.read_text(encoding="utf-8").splitlines()

    updated_keys: set[str] = set()
    new_lines: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith("#") and "=" in stripped:
            k, _ = stripped.split("=", 1)
            k = k.strip()
            if k in updates:
                val = str(updates[k]).strip()
                new_lines.append(f"{k}={val}")
                os.environ[k] = val
                updated_keys.add(k)
                continue
        new_lines.append(line)

    for k, v in updates.items():
        if k not in updated_keys:
            val = str(v).strip()
            new_lines.append(f"{k}={val}")
            os.environ[k] = val

    _ENV_FILE.write_text("\n".join(new_lines) + "\n", encoding="utf-8")


