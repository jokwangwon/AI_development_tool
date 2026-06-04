"""자비스(하나) 읽어주기 합성 — 외부 voice_lab(Qwen3 디자인) 연계 (hermetic).

답습: 내부 F5-TTS 제거 후 읽어주기를 외부 관제형 voice_lab 음성 생성으로 연계(연계형).
고정 페르소나(instruct+seed)로 일관된 '하나' 목소리. voice_lab 위치 = 주입(Provider Liquidity).
http_json/fetch_bytes 주입 = hermetic test seam(실 voice_lab 호출 0).
"""
from __future__ import annotations

import pytest

from jarvis_hud.readaloud import (
    HANA_INSTRUCT,
    HANA_SEED,
    ReadAloudError,
    synth_via_voicelab,
)


def test_synth_happy_returns_wav_bytes():
    calls = {}

    def fake_json(url, payload, timeout=60):
        calls["url"] = url
        calls["payload"] = payload
        return {"url": "http://127.0.0.1:8778/outputs/abc.wav", "id": "abc"}

    def fake_fetch(url, timeout=30):
        calls["wav_url"] = url
        return b"RIFFWAVE"

    out = synth_via_voicelab(
        "안녕하세요", design_url="http://127.0.0.1:8778/api/design",
        http_json=fake_json, fetch_bytes=fake_fetch,
    )
    assert out == b"RIFFWAVE"
    assert calls["url"] == "http://127.0.0.1:8778/api/design"
    assert calls["wav_url"] == "http://127.0.0.1:8778/outputs/abc.wav"


def test_synth_uses_fixed_hana_persona():
    """고정 페르소나(instruct+seed) → 일관된 '하나' 목소리(매 호출 동일)."""
    seen = {}

    def fake_json(url, payload, timeout=60):
        seen.update(payload)
        return {"url": "http://x/out.wav"}

    synth_via_voicelab("텍스트", design_url="http://x/api/design",
                       http_json=fake_json, fetch_bytes=lambda u, timeout=30: b"w")
    assert seen["text"] == "텍스트"
    assert seen["instruct"] == HANA_INSTRUCT
    assert seen["seed"] == HANA_SEED
    assert seen["language"] == "Korean"


def test_synth_missing_url_raises():
    def fake_json(url, payload, timeout=60):
        return {"id": "x"}  # url 누락
    with pytest.raises(ReadAloudError):
        synth_via_voicelab("t", design_url="http://x", http_json=fake_json,
                           fetch_bytes=lambda u, timeout=30: b"w")


def test_synth_non_dict_response_raises():
    with pytest.raises(ReadAloudError):
        synth_via_voicelab("t", design_url="http://x",
                           http_json=lambda u, p, timeout=60: "nope",
                           fetch_bytes=lambda u, timeout=30: b"w")


def test_synth_propagates_transport_error():
    """voice_lab 다운/네트워크 오류는 전파(핸들러가 잡아 502 → 프론트 Web Speech 폴백)."""
    def boom(url, payload, timeout=60):
        raise OSError("connection refused")
    with pytest.raises(OSError):
        synth_via_voicelab("t", design_url="http://x", http_json=boom,
                           fetch_bytes=lambda u, timeout=30: b"w")


def test_synth_custom_persona_override():
    seen = {}

    def fake_json(url, payload, timeout=60):
        seen.update(payload)
        return {"url": "http://x/o.wav"}

    synth_via_voicelab("t", design_url="http://x", http_json=fake_json,
                       fetch_bytes=lambda u, timeout=30: b"w",
                       instruct="custom voice", seed=7)
    assert seen["instruct"] == "custom voice"
    assert seen["seed"] == 7
