"""paths — 통합 데이터 레이어 §10-2 영속 위치 일원화 + 권한 테스트.

답습: docs/phase0/jarvis-unified-data-layer-design-brief.md
  - §8 영속 위치: `JARVIS_DATA_DIR` env override 필수(헌법 8조-2 하드코딩 제로).
  - §8/§11 Q4 해소(2026-05-29 사용자): 기본 = $XDG_DATA_HOME/jarvis →
    (미설정 시) ~/.local/share/jarvis. Linux 표준 + 백업/state 분리.
  - §8: DB 파일 0600 / 디렉터리 0700.
  - precedence: JARVIS_DATA_DIR > XDG_DATA_HOME/jarvis > ~/.local/share/jarvis.

본 test 는 실 디스크(tmp_path) + monkeypatch env 격리.
"""
from __future__ import annotations

import os
from pathlib import Path

from src.jarvis import paths


def test_data_dir_prefers_jarvis_data_dir(monkeypatch, tmp_path):
    monkeypatch.setenv("JARVIS_DATA_DIR", str(tmp_path / "custom"))
    monkeypatch.setenv("XDG_DATA_HOME", str(tmp_path / "xdg"))
    assert paths.data_dir() == tmp_path / "custom"


def test_data_dir_uses_xdg_when_no_override(monkeypatch, tmp_path):
    monkeypatch.delenv("JARVIS_DATA_DIR", raising=False)
    monkeypatch.setenv("XDG_DATA_HOME", str(tmp_path / "xdg"))
    assert paths.data_dir() == tmp_path / "xdg" / "jarvis"


def test_data_dir_defaults_to_local_share(monkeypatch):
    monkeypatch.delenv("JARVIS_DATA_DIR", raising=False)
    monkeypatch.delenv("XDG_DATA_HOME", raising=False)
    assert paths.data_dir() == Path.home() / ".local" / "share" / "jarvis"


def test_data_dir_expanduser(monkeypatch):
    monkeypatch.setenv("JARVIS_DATA_DIR", "~/jarvis-test-expand-xyz")
    assert paths.data_dir() == Path.home() / "jarvis-test-expand-xyz"


def test_ensure_data_dir_creates_with_0700(monkeypatch, tmp_path):
    monkeypatch.setenv("JARVIS_DATA_DIR", str(tmp_path / "d"))
    d = paths.ensure_data_dir()
    assert d.is_dir()
    assert (d.stat().st_mode & 0o777) == 0o700


def test_data_file_under_data_dir_with_parent(monkeypatch, tmp_path):
    monkeypatch.setenv("JARVIS_DATA_DIR", str(tmp_path / "d"))
    p = paths.data_file("x.jsonl")
    assert p == tmp_path / "d" / "x.jsonl"
    assert p.parent.is_dir()


def test_data_file_chmods_existing_to_0600(monkeypatch, tmp_path):
    monkeypatch.setenv("JARVIS_DATA_DIR", str(tmp_path / "d"))
    paths.ensure_data_dir()
    target = tmp_path / "d" / "x.jsonl"
    target.write_text("{}", encoding="utf-8")
    os.chmod(target, 0o644)
    returned = paths.data_file("x.jsonl")
    assert (returned.stat().st_mode & 0o777) == 0o600


def test_data_subdir_created_with_0700(monkeypatch, tmp_path):
    monkeypatch.setenv("JARVIS_DATA_DIR", str(tmp_path / "d"))
    sub = paths.data_subdir("archive")
    assert sub.is_dir()
    assert sub == tmp_path / "d" / "archive"
    assert (sub.stat().st_mode & 0o777) == 0o700


def test_named_helpers_point_under_data_dir(monkeypatch, tmp_path):
    monkeypatch.setenv("JARVIS_DATA_DIR", str(tmp_path / "d"))
    base = tmp_path / "d"
    assert paths.conversations_path() == base / "jarvis-conversations.jsonl"
    assert paths.tasks_ledger_path() == base / "jarvis-stone0-tasks.jsonl"
    assert paths.layer0_memory_path() == base / "jarvis-v00-layer0-memory.jsonl"
    assert paths.layer1_report_path() == base / "jarvis-v00-layer1-report.json"
    assert paths.multi_model_measurement_path() == base / "jarvis-v00-multi-model-measurement.json"
    assert paths.boss_measurement_path() == base / "jarvis-v00-boss-measurement.json"


def test_conversations_archive_dir_is_dir(monkeypatch, tmp_path):
    monkeypatch.setenv("JARVIS_DATA_DIR", str(tmp_path / "d"))
    arch = paths.conversations_archive_dir()
    assert arch.is_dir()
    assert arch == tmp_path / "d" / "jarvis-conversations-archive"


def test_worker_raw_log_path_naming(monkeypatch, tmp_path):
    monkeypatch.setenv("JARVIS_DATA_DIR", str(tmp_path / "d"))
    assert paths.worker_raw_log_path("claude", "ollama").name == "jarvis-v00-claude-worker-ollama-raw.log"
    assert paths.worker_raw_log_path("codex", "codex").name == "jarvis-v00-codex-worker-codex-raw.log"
    assert paths.worker_raw_log_path("glm", "glm").name == "jarvis-v00-glm-worker-glm-raw.log"
