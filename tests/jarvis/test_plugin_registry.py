"""플러그인 레지스트리 (단계2 인프라) 테스트.

답습: docs/phase0/jarvis-plugin-architecture-design-brief.md (v2 §5-2)
  [[3plus1-consensus-2026-06-01-jarvis-plugin-architecture]] (REVISE, C-2/C-4).

확정 설계(§5-2 + BLOCKING C-4):
  - **데이터 레지스트리**: jarvis_hud/plugins/<name>/plugin.json (manifest = 데이터,
    코어 코드 불변). 코어는 discover_enabled_plugins() 1회 호출만.
  - ⭐ **탐색 ≠ 활성화** (C-4 self-mod 우회 차단): 폴더에 drop-in 한다고 자동
    활성화 금지. 활성화는 enabled.json(명시 사람 등록)에 등재된 것만.
  - 보안: name 안전(path traversal 차단) + name == 폴더명 + panel_js basename only
    + permissions 화이트리스트. fail-soft(불량 manifest = skip, crash 아님).

이 모듈은 **순수 로직**(부작용 0 — 디스크 read만). 동적 import/라우트 조립은
별도(server 배선). 트랙 A: tmp_path fixture, 실 import 0.
"""
from __future__ import annotations

import json

import pytest

from src.jarvis.plugin_registry import (
    PluginManifest,
    PluginError,
    parse_manifest,
    discover_plugins,
    load_enabled,
    discover_enabled_plugins,
    select_ports,
    build_plugin_routes,
)


# ── parse_manifest: 유효성 ────────────────────────────────────────────
def _valid_data(name="tts_compare"):
    return {
        "name": name,
        "title": "TTS 비교",
        "panel_js": "panel.js",
        "icon": "🔊",
        "routes_module": "jarvis_hud.plugins.tts_compare.routes",
        "permissions": ["measurement:write", "conversation:read"],
    }


def test_parse_manifest_valid_returns_frozen():
    m = parse_manifest(_valid_data(), dir_name="tts_compare")
    assert isinstance(m, PluginManifest)
    assert m.name == "tts_compare"
    assert m.title == "TTS 비교"
    assert m.panel_js == "panel.js"
    assert m.permissions == ("measurement:write", "conversation:read")
    # frozen
    with pytest.raises(Exception):
        m.name = "x"  # type: ignore


def test_parse_manifest_missing_required_raises():
    for missing in ("name", "title", "panel_js"):
        data = _valid_data()
        del data[missing]
        with pytest.raises(PluginError):
            parse_manifest(data, dir_name="tts_compare")


# ── C-4 보안: name/경로 traversal 차단 ────────────────────────────────
@pytest.mark.parametrize("bad", ["../evil", "a/b", "..", "x..y", "UPPER", "with space", ""])
def test_parse_manifest_unsafe_name_raises(bad):
    data = _valid_data(name=bad)
    with pytest.raises(PluginError):
        parse_manifest(data, dir_name=bad)


def test_parse_manifest_name_must_equal_dir_name():
    # manifest 가 폴더명과 다른 name 을 주장 → 거부 (스푸핑 차단)
    with pytest.raises(PluginError):
        parse_manifest(_valid_data(name="tts_compare"), dir_name="other_dir")


@pytest.mark.parametrize("bad_js", ["../x.js", "/abs/x.js", "sub/x.js", "..", "x.txt"])
def test_parse_manifest_panel_js_traversal_raises(bad_js):
    data = _valid_data()
    data["panel_js"] = bad_js
    with pytest.raises(PluginError):
        parse_manifest(data, dir_name="tts_compare")


def test_parse_manifest_unknown_permission_raises():
    data = _valid_data()
    data["permissions"] = ["measurement:write", "core:admin"]  # core:admin 미허용
    with pytest.raises(PluginError):
        parse_manifest(data, dir_name="tts_compare")


def test_parse_manifest_permissions_default_empty():
    data = _valid_data()
    del data["permissions"]
    m = parse_manifest(data, dir_name="tts_compare")
    assert m.permissions == ()


# ── discover_plugins: 폴더 스캔 + fail-soft ───────────────────────────
def _make_plugin(plugins_dir, name, data=None, *, raw=None):
    d = plugins_dir / name
    d.mkdir(parents=True)
    content = raw if raw is not None else json.dumps(data if data is not None else _valid_data(name))
    (d / "plugin.json").write_text(content, encoding="utf-8")
    return d


def test_discover_plugins_scans_subdirs(tmp_path):
    pd = tmp_path / "plugins"
    pd.mkdir()
    _make_plugin(pd, "tts_compare")
    _make_plugin(pd, "calc", data=_valid_data("calc"))
    found = discover_plugins(str(pd))
    names = sorted(m.name for m in found)
    assert names == ["calc", "tts_compare"]


def test_discover_plugins_skips_invalid_fail_soft(tmp_path):
    pd = tmp_path / "plugins"
    pd.mkdir()
    _make_plugin(pd, "good")
    _make_plugin(pd, "broken", raw="{not json")  # 깨진 JSON
    _make_plugin(pd, "spoof", data=_valid_data("different"))  # name != dir
    found = discover_plugins(str(pd))
    # 불량은 skip, crash 아님. good 만 남음.
    assert [m.name for m in found] == ["good"]


def test_discover_plugins_missing_dir_returns_empty(tmp_path):
    assert discover_plugins(str(tmp_path / "nope")) == []


def test_discover_plugins_ignores_dir_without_manifest(tmp_path):
    pd = tmp_path / "plugins"
    pd.mkdir()
    (pd / "no_manifest").mkdir()
    _make_plugin(pd, "good")
    assert [m.name for m in discover_plugins(str(pd))] == ["good"]


# ── load_enabled: 명시 등록 (데이터) ──────────────────────────────────
def test_load_enabled_reads_list(tmp_path):
    f = tmp_path / "enabled.json"
    f.write_text(json.dumps({"enabled": ["tts_compare", "calc"]}), encoding="utf-8")
    assert load_enabled(str(f)) == frozenset({"tts_compare", "calc"})


def test_load_enabled_missing_file_empty(tmp_path):
    assert load_enabled(str(tmp_path / "nope.json")) == frozenset()


def test_load_enabled_malformed_empty_fail_soft(tmp_path):
    f = tmp_path / "enabled.json"
    f.write_text("{bad", encoding="utf-8")
    assert load_enabled(str(f)) == frozenset()


# ── ⭐ C-4 핵심 불변식: 탐색 ≠ 활성화 ─────────────────────────────────
def test_discover_enabled_only_returns_enabled(tmp_path):
    pd = tmp_path / "plugins"
    pd.mkdir()
    _make_plugin(pd, "tts_compare")
    _make_plugin(pd, "calc", data=_valid_data("calc"))
    _make_plugin(pd, "sneaky", data=_valid_data("sneaky"))  # drop-in 됐지만 미등록
    enabled = tmp_path / "enabled.json"
    enabled.write_text(json.dumps({"enabled": ["tts_compare", "calc"]}), encoding="utf-8")

    active = discover_enabled_plugins(str(pd), str(enabled))
    names = sorted(m.name for m in active)
    # sneaky 는 폴더에 있어도(탐색됨) 활성화 안 됨 (self-mod 우회 차단)
    assert names == ["calc", "tts_compare"]
    assert "sneaky" not in names


def test_discover_enabled_enabled_name_without_manifest_excluded(tmp_path):
    pd = tmp_path / "plugins"
    pd.mkdir()
    _make_plugin(pd, "tts_compare")
    enabled = tmp_path / "enabled.json"
    enabled.write_text(json.dumps({"enabled": ["tts_compare", "ghost"]}), encoding="utf-8")
    # ghost 는 manifest 없음 → 조용히 제외 (crash 아님)
    active = discover_enabled_plugins(str(pd), str(enabled))
    assert [m.name for m in active] == ["tts_compare"]


def test_discover_enabled_empty_enabled_returns_nothing(tmp_path):
    pd = tmp_path / "plugins"
    pd.mkdir()
    _make_plugin(pd, "tts_compare")
    enabled = tmp_path / "enabled.json"
    enabled.write_text(json.dumps({"enabled": []}), encoding="utf-8")
    # 폴더에 있어도 enabled 비면 0개 (drop-in 자동 활성화 금지)
    assert discover_enabled_plugins(str(pd), str(enabled)) == []


# ── 갈림길5: 최소권한 포트 주입 (select_ports) ────────────────────────
def test_select_ports_only_declared_permissions():
    available = {
        "conversation:read": "CONV_RO",
        "measurement:read": "MEAS_RO",
        "measurement:write": "MEAS_W",
    }
    m = parse_manifest(_valid_data(), dir_name="tts_compare")  # measurement:write + conversation:read
    ports = select_ports(m, available)
    assert set(ports) == {"measurement:write", "conversation:read"}
    assert "measurement:read" not in ports  # 미선언 = 미주입 (최소권한)
    assert ports["measurement:write"] == "MEAS_W"


def test_select_ports_no_permissions_empty():
    data = _valid_data()
    del data["permissions"]
    m = parse_manifest(data, dir_name="tts_compare")
    assert select_ports(m, {"measurement:write": "X"}) == {}


def test_select_ports_unavailable_port_skipped():
    # 선언했으나 코어가 제공 안 하는 포트 → 조용히 제외 (crash 아님)
    m = parse_manifest(_valid_data(), dir_name="tts_compare")
    ports = select_ports(m, {"conversation:read": "C"})  # measurement:write 미제공
    assert set(ports) == {"conversation:read"}


# ── §5-2: 동적 라우트 조립 (build_plugin_routes) ──────────────────────
class _FakeModule:
    def __init__(self, routes, *, capture=None):
        self._routes = routes
        self._capture = capture

    def make_routes(self, ports):
        if self._capture is not None:
            self._capture["ports"] = ports
        return list(self._routes)


def test_build_plugin_routes_imports_and_injects_ports():
    captured = {}
    mods = {"plug.tts.routes": _FakeModule(["R1", "R2"], capture=captured)}
    m = parse_manifest(
        {**_valid_data(), "routes_module": "plug.tts.routes"}, dir_name="tts_compare"
    )
    routes = build_plugin_routes([m], {"measurement:write": "W", "conversation:read": "C"},
                                  importer=lambda name: mods[name])
    assert routes == ["R1", "R2"]
    # 최소권한: 선언한 2개만 주입됨
    assert set(captured["ports"]) == {"measurement:write", "conversation:read"}


def test_build_plugin_routes_no_routes_module_skipped():
    data = _valid_data()
    del data["routes_module"]
    m = parse_manifest(data, dir_name="tts_compare")
    # routes_module 없는 플러그인(프론트 전용 패널) → 백엔드 라우트 0
    assert build_plugin_routes([m], {}, importer=lambda n: None) == []


def test_build_plugin_routes_import_failure_fail_soft():
    def _boom(name):
        raise ImportError("no module")
    m = parse_manifest(
        {**_valid_data(), "routes_module": "missing.mod"}, dir_name="tts_compare"
    )
    # import 실패해도 전체 조립이 죽지 않음 (fail-soft, 다른 플러그인 보호)
    assert build_plugin_routes([m], {}, importer=_boom) == []


def test_build_plugin_routes_missing_make_routes_fail_soft():
    class _Empty:
        pass
    m = parse_manifest(
        {**_valid_data(), "routes_module": "x"}, dir_name="tts_compare"
    )
    assert build_plugin_routes([m], {}, importer=lambda n: _Empty()) == []
