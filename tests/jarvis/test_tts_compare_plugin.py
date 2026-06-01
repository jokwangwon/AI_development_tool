"""TTS 비교 플러그인 백엔드 라우트 (단계4 첫 사례) — hermetic.

답습: docs/phase0/jarvis-plugin-architecture-design-brief.md (v2 §6)
  [[3plus1-consensus-2026-06-01-jarvis-plugin-architecture]] (첫 사례 TTS).

설계: 플러그인 인터페이스를 끝까지 밟는 첫 사례. make_routes(ports, synth=, voices=)
— synth/voices 주입으로 실 F5 모델 로드 0(hermetic). 단계1 PoC 가 ref voice
파라미터화를 실증(702MB/176모델/PASS) — 여기선 라우트·계약만 검증.

음성 카드 그리드(UX 컨펌): voices 목록 → 다중 선택 → 음성별 결과 카드.
measurement:write 포트(최소권한)로 합성 측정 기록(fail-soft).
"""
from __future__ import annotations

import base64
import json

from starlette.applications import Starlette
from starlette.testclient import TestClient

from jarvis_hud.plugins.tts_compare.routes import VoiceSpec, make_routes


def _voices():
    return {
        "kss": VoiceSpec(key="kss", label="KSS", ref_file="/x/kss.wav", ref_text="ref1"),
        "hana": VoiceSpec(key="hana", label="Hana", ref_file="/x/hana.wav", ref_text="ref2"),
    }


def _fake_synth(text, voice):
    # 결정적 가짜 합성 — voice 별로 구별되는 바이트/메트릭
    payload = f"{voice.key}:{text}".encode()
    return {
        "audio": payload,
        "sample_rate": 24000,
        "samples": len(payload) * 10,
        "rms": 0.1 + 0.01 * len(voice.key),
        "ms": 5,
    }


def _client(ports=None, synth=None, voices=None):
    routes = make_routes(
        ports if ports is not None else {},
        synth=synth or _fake_synth,
        voices=voices if voices is not None else _voices(),
    )
    return TestClient(Starlette(routes=routes))


# ── voices 목록 ──────────────────────────────────────────────────────
def test_voices_lists_available():
    r = _client().get("/api/plugins/tts_compare/voices")
    assert r.status_code == 200
    keys = {v["key"] for v in r.json()["voices"]}
    assert keys == {"kss", "hana"}
    # label 노출, ref_file 같은 내부 경로는 미노출
    blob = json.dumps(r.json())
    assert "/x/kss.wav" not in blob


# ── synthesize ───────────────────────────────────────────────────────
def test_synthesize_returns_per_voice_results():
    r = _client().post(
        "/api/plugins/tts_compare/synthesize",
        json={"text": "안녕", "voices": ["kss", "hana"]},
    )
    assert r.status_code == 200
    results = r.json()["results"]
    assert [x["voice"] for x in results] == ["kss", "hana"]
    # audio base64 디코드 → fake_synth payload 복원
    first = results[0]
    assert base64.b64decode(first["audio_b64"]) == b"kss:\xec\x95\x88\xeb\x85\x95"
    assert first["sample_rate"] == 24000
    assert "rms" in first and "samples" in first and "ms" in first


def test_synthesize_empty_text_400():
    r = _client().post("/api/plugins/tts_compare/synthesize",
                       json={"text": "  ", "voices": ["kss"]})
    assert r.status_code == 400


def test_synthesize_unknown_voice_400():
    r = _client().post("/api/plugins/tts_compare/synthesize",
                       json={"text": "안녕", "voices": ["ghost"]})
    assert r.status_code == 400


def test_synthesize_no_voices_400():
    r = _client().post("/api/plugins/tts_compare/synthesize",
                       json={"text": "안녕", "voices": []})
    assert r.status_code == 400


# ── measurement:write 포트 (최소권한, fail-soft) ──────────────────────
def test_synthesize_records_measurement_when_port_present():
    recorded = []

    def _writer(measurement, *, kind):
        recorded.append((measurement, kind))
        return 1

    _client(ports={"measurement:write": _writer}).post(
        "/api/plugins/tts_compare/synthesize",
        json={"text": "안녕", "voices": ["kss", "hana"]},
    )
    # 음성별 1건씩 기록
    assert len(recorded) == 2
    m0, kind0 = recorded[0]
    assert kind0 == "tts_compare"
    assert m0["voice"] == "kss" and "ms" in m0 and "rms" in m0


def test_synthesize_no_port_still_succeeds():
    # measurement:write 미주입(선언 안 한 플러그인) → 기록 스킵, 합성은 성공
    r = _client(ports={}).post("/api/plugins/tts_compare/synthesize",
                               json={"text": "안녕", "voices": ["kss"]})
    assert r.status_code == 200


def test_synthesize_measurement_write_failure_fail_soft():
    def _boom(measurement, *, kind):
        raise RuntimeError("db down")

    # 측정 기록 실패해도 합성 응답은 정상(fail-soft, 측정이 본체 아님)
    r = _client(ports={"measurement:write": _boom}).post(
        "/api/plugins/tts_compare/synthesize",
        json={"text": "안녕", "voices": ["kss"]},
    )
    assert r.status_code == 200
    assert len(r.json()["results"]) == 1
