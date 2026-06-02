"""플러그인 관리 HTTP 라우트 (단계3 #UI-4 install 엔드포인트) — hermetic.

답습: docs/phase0/jarvis-plugin-architecture-design-brief.md (v2 §5-3/§7)
  [[3plus1-consensus-2026-06-01-jarvis-plugin-architecture]] (C-1·C-3·C-4).

설계: B복사 게이트(plugin_install)를 HTTP 로 노출. same-origin 가드(CSRF) +
work_root/plugins_dir/enabled_file 주입(test seam). install ≠ enable(C-4 분리).
preview = 복사 전 사람 diff 검토(scrub 적용).

실 워커·격리 0 — tmp_path 로 work_root/plugins_dir 모사.
"""
from __future__ import annotations

import json
import os

from starlette.applications import Starlette
from starlette.testclient import TestClient

from jarvis_hud.plugin_routes import make_plugin_admin_routes

_SAME_ORIGIN = {"origin": "http://localhost:8765", "host": "localhost:8765"}
_CROSS = {"origin": "http://evil.example", "host": "localhost:8765"}


def _manifest(name="tts_compare"):
    return {"name": name, "title": "TTS 비교", "panel_js": "panel.js",
            "permissions": ["measurement:write"]}


def _make_source(work, name="tts_compare", *, files=None):
    src = work / name
    src.mkdir(parents=True)
    (src / "plugin.json").write_text(json.dumps(_manifest(name)), encoding="utf-8")
    (src / "panel.js").write_text("// panel", encoding="utf-8")
    for rel, content in (files or {}).items():
        (src / rel).write_text(content, encoding="utf-8")
    return src


def _client(tmp_path):
    work = tmp_path / "work"; work.mkdir()
    plugins = tmp_path / "plugins"; plugins.mkdir()
    enabled = plugins / "enabled.json"
    enabled.write_text(json.dumps({"enabled": []}), encoding="utf-8")
    routes = make_plugin_admin_routes(
        work_root=str(work), plugins_dir=str(plugins), enabled_file=str(enabled)
    )
    return TestClient(Starlette(routes=routes)), work, plugins, enabled


# ── install ────────────────────────────────────────────────────────────
def test_install_happy(tmp_path):
    client, work, plugins, enabled = _client(tmp_path)
    _make_source(work, "tts_compare")
    r = client.post("/api/jarvis/plugin/install",
                    json={"source": "tts_compare", "name": "tts_compare"}, headers=_SAME_ORIGIN)
    assert r.status_code == 200
    assert r.json()["name"] == "tts_compare"
    assert (plugins / "tts_compare" / "panel.js").is_file()
    # C-4: install 은 활성화 안 함
    assert json.loads(enabled.read_text())["enabled"] == []


def test_install_cross_origin_forbidden(tmp_path):
    client, work, _, _ = _client(tmp_path)
    _make_source(work, "tts_compare")
    r = client.post("/api/jarvis/plugin/install",
                    json={"source": "tts_compare", "name": "tts_compare"}, headers=_CROSS)
    assert r.status_code == 403


def test_install_bad_name_400(tmp_path):
    client, work, _, _ = _client(tmp_path)
    _make_source(work, "tts_compare")
    r = client.post("/api/jarvis/plugin/install",
                    json={"source": "tts_compare", "name": "../evil"}, headers=_SAME_ORIGIN)
    assert r.status_code == 400


def test_install_source_traversal_400(tmp_path):
    client, work, _, _ = _client(tmp_path)
    r = client.post("/api/jarvis/plugin/install",
                    json={"source": "../../etc", "name": "tts_compare"}, headers=_SAME_ORIGIN)
    assert r.status_code == 400


def test_install_sensitive_file_400(tmp_path):
    client, work, plugins, _ = _client(tmp_path)
    # 거부는 *파일명*(.env) 기준 — 내용은 무관(스캐너 오탐 방지 위해 무해 값).
    _make_source(work, "tts_compare", files={".env": "x"})
    r = client.post("/api/jarvis/plugin/install",
                    json={"source": "tts_compare", "name": "tts_compare"}, headers=_SAME_ORIGIN)
    assert r.status_code == 400
    assert not (plugins / "tts_compare").exists()


# ── enable / disable (C-4 명시 활성화) ─────────────────────────────────
def test_enable_then_disable(tmp_path):
    client, work, plugins, enabled = _client(tmp_path)
    _make_source(work, "tts_compare")
    client.post("/api/jarvis/plugin/install",
                json={"source": "tts_compare", "name": "tts_compare"}, headers=_SAME_ORIGIN)
    r = client.post("/api/jarvis/plugin/enable", json={"name": "tts_compare"}, headers=_SAME_ORIGIN)
    assert r.status_code == 200
    assert json.loads(enabled.read_text())["enabled"] == ["tts_compare"]
    r = client.post("/api/jarvis/plugin/disable", json={"name": "tts_compare"}, headers=_SAME_ORIGIN)
    assert r.status_code == 200
    assert json.loads(enabled.read_text())["enabled"] == []


def test_enable_cross_origin_forbidden(tmp_path):
    client, *_ = _client(tmp_path)
    r = client.post("/api/jarvis/plugin/enable", json={"name": "tts_compare"}, headers=_CROSS)
    assert r.status_code == 403


# ── list ────────────────────────────────────────────────────────────────
def test_list_shows_discovered_and_enabled_flag(tmp_path):
    client, work, plugins, enabled = _client(tmp_path)
    # 두 플러그인 설치, 하나만 enable
    for n in ("tts_compare", "calc"):
        _make_source(work, n)
        client.post("/api/jarvis/plugin/install", json={"source": n, "name": n}, headers=_SAME_ORIGIN)
    client.post("/api/jarvis/plugin/enable", json={"name": "tts_compare"}, headers=_SAME_ORIGIN)
    r = client.get("/api/jarvis/plugins")
    assert r.status_code == 200
    items = {p["name"]: p for p in r.json()["plugins"]}
    assert items["tts_compare"]["enabled"] is True
    assert items["calc"]["enabled"] is False  # 설치됐지만 미활성(탐색≠활성화)


# ── preview (복사 전 diff 검토 + scrub) ────────────────────────────────
def test_preview_lists_files_and_scrubs_secrets(tmp_path):
    client, work, _, _ = _client(tmp_path)
    # secret 리터럴을 소스에 두지 않도록 런타임 조합(secret_scanner 오탐 방지).
    # redactor 가 실제 값을 scrub 하는지 검증하는 게 목적.
    fake_secret = "sk-" + "ant-" + "api03-" + ("A" * 24)
    _make_source(work, "tts_compare",
                 files={"config.js": "const k = '%s';" % fake_secret})
    r = client.get("/api/jarvis/plugin/preview", params={"source": "tts_compare"})
    assert r.status_code == 200
    body = r.json()
    names = {f["path"] for f in body["files"]}
    assert "plugin.json" in names and "config.js" in names
    # raw secret 가 그대로 노출되지 않아야(scrub)
    blob = json.dumps(body, ensure_ascii=False)
    assert fake_secret not in blob


def test_preview_source_traversal_400(tmp_path):
    client, *_ = _client(tmp_path)
    r = client.get("/api/jarvis/plugin/preview", params={"source": "../../etc"})
    assert r.status_code == 400
