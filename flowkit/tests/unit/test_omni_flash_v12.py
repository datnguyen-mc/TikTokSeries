"""Omni 1.2 Flash (Nov 2026): 3–15s clips and the macaron_cookie_* wire keys.

The text-to-video key was seen in a live Flow UI capture on 2026-11-08
(``macaron_cookie_t2v_10s``, same YhhmEf slots as Omni 1.1). The Frames and
Ingredients keys follow the same naming and are listed as unverified in
agent/models.json until a UI capture confirms them (docs/CAPTURE.md).
"""
import json

import pytest

from agent.services import flow_batch as fb
from agent.services import omni_flash


def inner(freq: str):
    return json.loads(json.loads(freq)[0][0][1])


@pytest.fixture(autouse=True)
def _no_env_override(monkeypatch):
    monkeypatch.delenv("OMNI_FLASH_MODEL_VERSION", raising=False)


def test_models_json_defaults_to_omni_1_2():
    assert fb.omni_model_version() == "1.2"
    assert fb.omni_valid_durations() == tuple(range(3, 16))


@pytest.mark.parametrize(("mode", "expected"), [
    ("text_to_video", "macaron_cookie_t2v_15s"),
    ("frame_to_video", "macaron_cookie_i2v_15s"),
    ("start_end_frame_to_video", "macaron_cookie_i2v_15s_first_last"),
    ("reference_to_video", "macaron_cookie_r2v_15s"),
])
def test_15s_keys(mode, expected):
    assert fb.omni_model_key(mode, 15) == expected
    assert fb.omni_model_key(mode, 15, "360p") == expected + "_360p"


def test_reference_builder_uses_the_1_2_key_in_the_model_slot():
    req = inner(fb.omni_reference_video_request("p", "pid", ["m1"], duration_s=15))[0][0]
    assert req[2] == "macaron_cookie_r2v_15s"


def test_first_frame_builder_uses_the_1_2_key():
    req = inner(fb.omni_first_frame_request("p", "pid", "m1", duration_s=12))[0][0]
    assert req[1] == "macaron_cookie_i2v_12s"


def test_explicit_1_1_still_builds_the_captured_wire():
    req = inner(fb.omni_reference_video_request("p", "pid", ["m1"], duration_s=10, model_version="1.1"))[0][0]
    assert req[2] == "abra_r2v_10s"


def test_env_rollback_to_1_1(monkeypatch):
    monkeypatch.setenv("OMNI_FLASH_MODEL_VERSION", "1.1")
    assert fb.omni_model_key("reference_to_video", 10) == "abra_r2v_10s"
    with pytest.raises(ValueError, match="Omni 1.1 duration 15s is unsupported"):
        fb.omni_model_key("reference_to_video", 15)


@pytest.mark.parametrize("bad", [2, 16, 20])
def test_out_of_range_durations_fail_before_submit(bad):
    with pytest.raises(ValueError, match="unsupported"):
        fb.omni_reference_video_request("p", "pid", ["m1"], duration_s=bad)


def test_unknown_version_is_rejected():
    with pytest.raises(ValueError, match="Unknown Omni model version"):
        fb.omni_model_key("reference_to_video", 10, version="9.9")


def test_service_accepts_every_configured_duration():
    assert omni_flash.OMNI_FLASH_VALID_DURATIONS == tuple(range(3, 16))
    omni_flash._validate_duration(15)
    with pytest.raises(ValueError):
        omni_flash._validate_duration(15, "1.1")
