"""외부 관제형(External / Federated) 읽기측 레지스트리 테스트 — 패턴1 링크 허브 MVP.

답습: docs/phase0/jarvis-plugin-taxonomy-external-view-design-brief.md (v2.1 §1.5/§4 패턴1)
  docs/review/3plus1-consensus-2026-06-02-jarvis-plugin-external-taxonomy.md
    (REVISE — 읽기측 1단계만, 제어/자격증명/게이트 전부 DEFER, 풀3+1 불요).

확정 설계 (읽기측 MVP):
  - **링크 허브**: 외부 시스템을 가리키는 가벼운 레지스트리 = 이름 + URL + (선택) 아이콘.
    결과는 외부에서 본다(패턴1). 제어·자격증명·결과 pull 전부 범위 밖.
  - ⭐ **provenance fail-closed** (§1.5 G7, 비협상): 관제 대상 = 자비스가 도와 만든
    프로젝트 한정. origin == "jarvis" 가 아니면 거부(skip). origin 불명 = 대상 아님.
  - **URL 검증**: http(s) scheme 만 — javascript:/data: 등 XSS href 벡터 차단(읽기측
    실 표면, 합의 항목8 답습).
  - fail-soft: 불량 엔트리·깨진 JSON·없는 파일 = skip, crash 아님(레지스트리 컨벤션 답습).

이 모듈은 **순수 로직**(디스크 read 만, 부작용 0). 라우트·HUD 렌더는 별도(server/index).
플러그인과 달리 코드 실행 0 → 동적 import·포트 주입·B복사 전부 없음.
"""
from __future__ import annotations

import json

import pytest

from src.jarvis.external_registry import (
    ExternalEntry,
    ExternalRegistryError,
    JARVIS_ORIGIN,
    discover_external,
    parse_entry,
)


# ── parse_entry: 유효성 ───────────────────────────────────────────────
def _valid_data(name="tts_lab"):
    return {
        "name": name,
        "title": "TTS 모델 테스트",
        "url": "https://tts.example.com/dashboard",
        "icon": "🔊",
        "origin": "jarvis",
    }


def test_parse_entry_valid_returns_frozen():
    e = parse_entry(_valid_data())
    assert isinstance(e, ExternalEntry)
    assert e.name == "tts_lab"
    assert e.title == "TTS 모델 테스트"
    assert e.url == "https://tts.example.com/dashboard"
    assert e.icon == "🔊"
    assert e.origin == JARVIS_ORIGIN
    with pytest.raises(Exception):
        e.name = "x"  # type: ignore  # frozen


def test_parse_entry_missing_required_raises():
    for missing in ("name", "title", "url", "origin"):
        data = _valid_data()
        del data[missing]
        with pytest.raises(ExternalRegistryError):
            parse_entry(data)


def test_parse_entry_non_dict_raises():
    with pytest.raises(ExternalRegistryError):
        parse_entry(["not", "a", "dict"])  # type: ignore


def test_parse_entry_icon_optional_defaults_empty():
    data = _valid_data()
    del data["icon"]
    e = parse_entry(data)
    assert e.icon == ""


# ── provenance fail-closed (§1.5 G7) — 보안 핵심 ──────────────────────
def test_parse_entry_rejects_non_jarvis_origin():
    """origin 이 jarvis 가 아니면 거부 — 자비스 도움 프로젝트 한정(§1.5 비협상)."""
    for bad in ("third_party", "external", "user", "", "JARVIS", "jarvis "):
        data = _valid_data()
        data["origin"] = bad
        with pytest.raises(ExternalRegistryError):
            parse_entry(data)


def test_parse_entry_rejects_missing_origin_fail_closed():
    """origin 불명 = 관제 대상 아님 (fail-closed). missing 은 위 required 와 별개로 명시."""
    data = _valid_data()
    data["origin"] = None
    with pytest.raises(ExternalRegistryError):
        parse_entry(data)


# ── URL 검증 — XSS/스킴 차단 ───────────────────────────────────────────
def test_parse_entry_rejects_non_http_url():
    """링크 href 로 렌더되므로 http(s) 외 스킴 거부 (javascript:/data:/file: 차단)."""
    for bad in (
        "javascript:alert(1)",
        "data:text/html,<script>1</script>",
        "file:///etc/passwd",
        "ftp://host/x",
        "//evil.com",
        "not a url",
        "",
    ):
        data = _valid_data()
        data["url"] = bad
        with pytest.raises(ExternalRegistryError):
            parse_entry(data)


def test_parse_entry_accepts_http_and_https():
    for ok in ("http://localhost:9000/", "https://x.example.com/path?q=1"):
        data = _valid_data()
        data["url"] = ok
        assert parse_entry(data).url == ok


def test_parse_entry_rejects_unsafe_name():
    for bad in ("../etc", "a/b", "UPPER", "", "has space", ".", ".."):
        data = _valid_data(name=bad)
        with pytest.raises(ExternalRegistryError):
            parse_entry(data)


# ── discover_external: 파일 → 엔트리 리스트, fail-soft ────────────────
def _write_registry(path, entries):
    path.write_text(json.dumps({"entries": entries}), encoding="utf-8")


def test_discover_external_missing_file_returns_empty(tmp_path):
    assert discover_external(str(tmp_path / "nope.json")) == []


def test_discover_external_broken_json_returns_empty(tmp_path):
    f = tmp_path / "registry.json"
    f.write_text("{not json", encoding="utf-8")
    assert discover_external(str(f)) == []


def test_discover_external_parses_valid_entries_sorted(tmp_path):
    f = tmp_path / "registry.json"
    _write_registry(f, [
        _valid_data(name="zebra"),
        _valid_data(name="alpha"),
    ])
    out = discover_external(str(f))
    assert [e.name for e in out] == ["alpha", "zebra"]  # name 순 결정적


def test_discover_external_fail_soft_skips_bad_entries(tmp_path):
    """불량 엔트리 1개가 전체를 막지 않음 — 좋은 것만 통과(레지스트리 fail-soft 답습)."""
    f = tmp_path / "registry.json"
    _write_registry(f, [
        _valid_data(name="good"),
        {"name": "bad_origin", "title": "x", "url": "https://x.io", "origin": "evil"},
        {"name": "bad_url", "title": "x", "url": "javascript:1", "origin": "jarvis"},
        "not even a dict",
    ])
    out = discover_external(str(f))
    assert [e.name for e in out] == ["good"]


def test_discover_external_non_list_entries_returns_empty(tmp_path):
    f = tmp_path / "registry.json"
    f.write_text(json.dumps({"entries": "nope"}), encoding="utf-8")
    assert discover_external(str(f)) == []


def test_discover_external_missing_entries_key_returns_empty(tmp_path):
    f = tmp_path / "registry.json"
    f.write_text(json.dumps({}), encoding="utf-8")
    assert discover_external(str(f)) == []
