"""외부 관제형 읽기측 HTTP 라우트 (`/api/jarvis/external` GET) — hermetic.

답습: docs/phase0/jarvis-plugin-taxonomy-external-view-design-brief.md (v2.1 §4 패턴1)
  docs/review/3plus1-consensus-2026-06-02-jarvis-plugin-external-taxonomy.md (REVISE 읽기측).

설계: external_registry(순수 로직)를 HTTP GET 으로 노출하는 얇은 레이어. 읽기 전용 —
write/제어/자격증명 0(제어측 별도 풀3+1). registry_file 주입 = hermetic test seam.
provenance(origin) 는 내부 게이트라 응답에 비노출(이름·URL·아이콘만).
"""
from __future__ import annotations

import json

from starlette.applications import Starlette
from starlette.testclient import TestClient

from jarvis_hud.external_routes import make_external_routes
from src.jarvis.process_control import ProbeStatus, ProcessController


def _entry(name="tts_lab"):
    return {"name": name, "title": "TTS 모델 테스트",
            "url": "https://tts.example.com/x", "icon": "🔊", "origin": "jarvis"}


def _local_entry(name="voice_lab", port=8777):
    return {"name": name, "title": "음성 랩", "url": f"http://127.0.0.1:{port}",
            "icon": "🎙️", "origin": "jarvis"}


def _probe_client(tmp_path, entries, controller):
    reg = tmp_path / "registry.json"
    reg.write_text(json.dumps({"entries": entries}), encoding="utf-8")
    routes = make_external_routes(registry_file=str(reg), controller=controller)
    return TestClient(Starlette(routes=routes))


def _client(tmp_path, entries):
    reg = tmp_path / "registry.json"
    reg.write_text(json.dumps({"entries": entries}), encoding="utf-8")
    routes = make_external_routes(registry_file=str(reg))
    return TestClient(Starlette(routes=routes)), reg


def test_external_list_happy(tmp_path):
    client, _ = _client(tmp_path, [_entry("zebra"), _entry("alpha")])
    r = client.get("/api/jarvis/external")
    assert r.status_code == 200
    items = r.json()["external"]
    assert [x["name"] for x in items] == ["alpha", "zebra"]  # name 순
    assert items[0]["url"] == "https://tts.example.com/x"
    assert items[0]["icon"] == "🔊"


def test_external_list_hides_origin(tmp_path):
    """provenance(origin)는 내부 게이트 — 응답에 노출하지 않음."""
    client, _ = _client(tmp_path, [_entry()])
    items = client.get("/api/jarvis/external").json()["external"]
    assert "origin" not in items[0]


def test_external_list_filters_bad_provenance(tmp_path):
    """fail-closed: origin != jarvis 엔트리는 노출 0(레지스트리가 거른 결과)."""
    bad = {"name": "thirdparty", "title": "x", "url": "https://x.io", "origin": "evil"}
    client, _ = _client(tmp_path, [_entry("good"), bad])
    items = client.get("/api/jarvis/external").json()["external"]
    assert [x["name"] for x in items] == ["good"]


def test_external_list_missing_file_empty(tmp_path):
    routes = make_external_routes(registry_file=str(tmp_path / "nope.json"))
    client = TestClient(Starlette(routes=routes))
    r = client.get("/api/jarvis/external")
    assert r.status_code == 200
    assert r.json()["external"] == []


# ── 제어측 slice-1a: 상태 probe (localhost 카드만, ProcessController 경유) ──────
def test_probe_localhost_listening(tmp_path):
    """localhost 카드 = health probe(저위험·자율) → listening 반환."""
    ctrl = ProcessController(prober=lambda t: ProbeStatus(listening=True))
    client = _probe_client(tmp_path, [_local_entry()], ctrl)
    r = client.get("/api/jarvis/external/probe?name=voice_lab")
    assert r.status_code == 200
    body = r.json()
    assert body["probeable"] is True
    assert body["listening"] is True
    assert body["grade"] == "LOW"
    assert body["outcome"] == "executed"


def test_probe_localhost_down(tmp_path):
    ctrl = ProcessController(prober=lambda t: ProbeStatus(listening=False))
    client = _probe_client(tmp_path, [_local_entry()], ctrl)
    body = client.get("/api/jarvis/external/probe?name=voice_lab").json()
    assert body["probeable"] is True
    assert body["listening"] is False


def test_probe_non_localhost_not_probeable(tmp_path):
    """외부 호스트 카드 = probe 미지원(B-4 localhost 한정). 점 없음."""
    ctrl = ProcessController(prober=lambda t: ProbeStatus(listening=True))
    client = _probe_client(tmp_path, [_entry("remote")], ctrl)
    body = client.get("/api/jarvis/external/probe?name=remote").json()
    assert body["probeable"] is False
    assert "listening" not in body


def test_probe_unknown_name_404(tmp_path):
    ctrl = ProcessController(prober=lambda t: ProbeStatus(listening=True))
    client = _probe_client(tmp_path, [_local_entry()], ctrl)
    assert client.get("/api/jarvis/external/probe?name=nope").status_code == 404


def test_probe_provenance_only_registry_entries(tmp_path):
    """레지스트리에 없는 임의 대상은 probe 불가(provenance — registry가 유일 출처)."""
    ctrl = ProcessController(prober=lambda t: ProbeStatus(listening=True))
    # bad provenance 엔트리는 registry가 이미 제외 → probe도 not found
    bad = {"name": "evil", "title": "x", "url": "http://127.0.0.1:8777", "origin": "third_party"}
    client = _probe_client(tmp_path, [bad], ctrl)
    assert client.get("/api/jarvis/external/probe?name=evil").status_code == 404


def test_probe_default_controller_real_socket(tmp_path):
    """controller 미주입 시 기본 ProcessController(실 socket). 죽은 포트 → listening False."""
    reg = tmp_path / "registry.json"
    reg.write_text(json.dumps({"entries": [_local_entry(port=59999)]}), encoding="utf-8")
    routes = make_external_routes(registry_file=str(reg))
    client = TestClient(Starlette(routes=routes))
    body = client.get("/api/jarvis/external/probe?name=voice_lab").json()
    assert body["probeable"] is True
    assert body["listening"] is False
