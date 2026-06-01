"""B복사 게이트 (단계3, #UI-4 산출물 반영) 테스트.

답습: docs/phase0/jarvis-plugin-architecture-design-brief.md (v2 §5-3/§7)
  [[3plus1-consensus-2026-06-01-jarvis-plugin-architecture]] (BLOCKING C-1·C-3 비협상).

확정 설계(§7 + C-1/C-3):
  - **C-1**: 복사 소스 = work/ 하위 명시 고정 + target = plugins/<name> realpath
    화이트리스트(traversal 차단) + 자동복사 금지(코드강제 — 이 함수는 명시 호출만,
    auto-dispatch 경로에서 호출 0) + 덮어쓰기 금지(기존 존재 시 거부).
  - **C-3**: 복사 범위 work/ 하위 엄격 제한(소스 realpath ⊄ work_root → 거부) +
    symlink 방어(트리 내 symlink → 거부) + secret scrub(민감 파일명 → fail-closed 거부).
  - **C-4 보존**: install ≠ 활성화. 복사만 — enabled.json 등록은 별도 명시 단계
    (enable_plugin). drop-in 자동활성 금지 불변식 유지.

트랙 A: tmp_path fixture로 work_root/plugins_dir 모사. 실 워커·격리 0.
"""
from __future__ import annotations

import json
import os

import pytest

from src.jarvis.plugin_install import (
    PluginInstallError,
    install_plugin_from_work,
    enable_plugin,
    disable_plugin,
)


def _manifest(name="tts_compare"):
    return {
        "name": name,
        "title": "TTS 비교",
        "panel_js": "panel.js",
        "permissions": ["measurement:write"],
    }


def _make_source(work_root, name="tts_compare", *, manifest=None, files=None):
    """work_root 하위에 플러그인 산출물 폴더 모사."""
    src = work_root / name
    src.mkdir(parents=True)
    (src / "plugin.json").write_text(
        json.dumps(manifest if manifest is not None else _manifest(name)), encoding="utf-8"
    )
    (src / "panel.js").write_text("// panel", encoding="utf-8")
    for rel, content in (files or {}).items():
        p = src / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
    return src


# ── happy path ────────────────────────────────────────────────────────
def test_install_copies_tree_and_returns_manifest(tmp_path):
    work = tmp_path / "work"
    work.mkdir()
    plugins = tmp_path / "plugins"
    plugins.mkdir()
    src = _make_source(work, files={"sub/util.js": "// util"})

    m = install_plugin_from_work(str(src), "tts_compare", work_root=str(work), plugins_dir=str(plugins))

    assert m.name == "tts_compare"
    target = plugins / "tts_compare"
    assert (target / "plugin.json").is_file()
    assert (target / "panel.js").is_file()
    assert (target / "sub" / "util.js").is_file()  # 중첩 일반 파일 복사


# ── C-1: target 화이트리스트 + 덮어쓰기 금지 + 이름 안전 ────────────────
@pytest.mark.parametrize("bad", ["../evil", "a/b", "..", "UPPER", ""])
def test_install_unsafe_name_rejected(tmp_path, bad):
    work = tmp_path / "work"; work.mkdir()
    plugins = tmp_path / "plugins"; plugins.mkdir()
    src = _make_source(work, "tts_compare")
    with pytest.raises(PluginInstallError):
        install_plugin_from_work(str(src), bad, work_root=str(work), plugins_dir=str(plugins))


def test_install_existing_target_rejected_no_overwrite(tmp_path):
    work = tmp_path / "work"; work.mkdir()
    plugins = tmp_path / "plugins"; plugins.mkdir()
    (plugins / "tts_compare").mkdir()  # 이미 존재
    src = _make_source(work, "tts_compare")
    with pytest.raises(PluginInstallError):
        install_plugin_from_work(str(src), "tts_compare", work_root=str(work), plugins_dir=str(plugins))


def test_install_manifest_name_must_match_target(tmp_path):
    work = tmp_path / "work"; work.mkdir()
    plugins = tmp_path / "plugins"; plugins.mkdir()
    src = _make_source(work, "tts_compare", manifest=_manifest("other"))  # manifest name != 인자
    with pytest.raises(PluginInstallError):
        install_plugin_from_work(str(src), "tts_compare", work_root=str(work), plugins_dir=str(plugins))


# ── C-3: work/ 하위 엄격 제한 + symlink + secret ───────────────────────
def test_install_source_outside_work_root_rejected(tmp_path):
    work = tmp_path / "work"; work.mkdir()
    plugins = tmp_path / "plugins"; plugins.mkdir()
    outside = tmp_path / "outside"  # work_root 밖
    src = _make_source(outside, "tts_compare")
    with pytest.raises(PluginInstallError):
        install_plugin_from_work(str(src), "tts_compare", work_root=str(work), plugins_dir=str(plugins))


def test_install_source_symlink_escape_rejected(tmp_path):
    work = tmp_path / "work"; work.mkdir()
    plugins = tmp_path / "plugins"; plugins.mkdir()
    real = _make_source(tmp_path / "elsewhere", "tts_compare")
    link = work / "tts_compare"
    os.symlink(str(real), str(link))  # work 안에 있어 보이지만 realpath 는 밖
    with pytest.raises(PluginInstallError):
        install_plugin_from_work(str(link), "tts_compare", work_root=str(work), plugins_dir=str(plugins))


def test_install_symlink_in_tree_rejected(tmp_path):
    work = tmp_path / "work"; work.mkdir()
    plugins = tmp_path / "plugins"; plugins.mkdir()
    src = _make_source(work, "tts_compare")
    os.symlink("/etc/passwd", str(src / "sneaky.js"))  # 트리 내 symlink
    with pytest.raises(PluginInstallError):
        install_plugin_from_work(str(src), "tts_compare", work_root=str(work), plugins_dir=str(plugins))
    # fail-closed: 부분 복사물 잔존 금지
    assert not (plugins / "tts_compare").exists()


@pytest.mark.parametrize("sensitive", [".credentials.json", "id_ed25519", "key.pem", ".env"])
def test_install_sensitive_file_rejected_fail_closed(tmp_path, sensitive):
    work = tmp_path / "work"; work.mkdir()
    plugins = tmp_path / "plugins"; plugins.mkdir()
    src = _make_source(work, "tts_compare", files={sensitive: "SECRET"})
    with pytest.raises(PluginInstallError):
        install_plugin_from_work(str(src), "tts_compare", work_root=str(work), plugins_dir=str(plugins))
    assert not (plugins / "tts_compare").exists()


# ── ⭐ C-4 보존: install ≠ 활성화 ──────────────────────────────────────
def test_install_does_not_auto_enable(tmp_path):
    work = tmp_path / "work"; work.mkdir()
    plugins = tmp_path / "plugins"; plugins.mkdir()
    enabled = plugins / "enabled.json"
    enabled.write_text(json.dumps({"enabled": []}), encoding="utf-8")
    src = _make_source(work, "tts_compare")

    install_plugin_from_work(str(src), "tts_compare", work_root=str(work), plugins_dir=str(plugins))
    # 복사됐지만 enabled.json 변화 0 (drop-in 자동활성 금지)
    assert json.loads(enabled.read_text())["enabled"] == []


# ── enable / disable: 명시 활성화 게이트 (C-4) ─────────────────────────
def test_enable_plugin_adds_to_enabled(tmp_path):
    enabled = tmp_path / "enabled.json"
    enabled.write_text(json.dumps({"enabled": []}), encoding="utf-8")
    enable_plugin("tts_compare", enabled_file=str(enabled))
    assert json.loads(enabled.read_text())["enabled"] == ["tts_compare"]


def test_enable_plugin_idempotent(tmp_path):
    enabled = tmp_path / "enabled.json"
    enabled.write_text(json.dumps({"enabled": ["tts_compare"]}), encoding="utf-8")
    enable_plugin("tts_compare", enabled_file=str(enabled))
    assert json.loads(enabled.read_text())["enabled"] == ["tts_compare"]  # 중복 없음


def test_enable_plugin_unsafe_name_rejected(tmp_path):
    enabled = tmp_path / "enabled.json"
    enabled.write_text(json.dumps({"enabled": []}), encoding="utf-8")
    with pytest.raises(PluginInstallError):
        enable_plugin("../evil", enabled_file=str(enabled))


def test_enable_plugin_creates_file_if_missing(tmp_path):
    enabled = tmp_path / "enabled.json"  # 없음
    enable_plugin("tts_compare", enabled_file=str(enabled))
    assert json.loads(enabled.read_text())["enabled"] == ["tts_compare"]


def test_disable_plugin_removes(tmp_path):
    enabled = tmp_path / "enabled.json"
    enabled.write_text(json.dumps({"enabled": ["tts_compare", "calc"]}), encoding="utf-8")
    disable_plugin("tts_compare", enabled_file=str(enabled))
    assert json.loads(enabled.read_text())["enabled"] == ["calc"]
