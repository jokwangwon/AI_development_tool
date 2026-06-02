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


def _entry(name="tts_lab"):
    return {"name": name, "title": "TTS 모델 테스트",
            "url": "https://tts.example.com/x", "icon": "🔊", "origin": "jarvis"}


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
