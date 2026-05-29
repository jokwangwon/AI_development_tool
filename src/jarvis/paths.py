"""통합 데이터 레이어 §10-2 — 영속 위치 일원화 + 권한.

답습: docs/phase0/jarvis-unified-data-layer-design-brief.md
  - §8 영속 위치: `JARVIS_DATA_DIR` env override 필수(헌법 8조-2 하드코딩 제로) —
    9개 흩어진 /tmp 경로를 단일 base 하위로 일원화.
  - §8/§11 Q4 해소(2026-05-29 사용자): 기본값 precedence =
    JARVIS_DATA_DIR > $XDG_DATA_HOME/jarvis > ~/.local/share/jarvis
    (Linux 표준 + 백업/state 분리 + ~/.local/share 이미 0700).
  - §8: 디렉터리 0700 / 데이터 파일 0600.
  - Q7 해소: 대화 raw 저장(저장 redaction 없음) — 영속 위치 권한이 1차 방어.

stdlib only. 모든 jarvis 영속 데이터 경로의 single source of truth.
"""
from __future__ import annotations

import os
from pathlib import Path

_APP_DIR_NAME = "jarvis"

_DIR_MODE = 0o700
_FILE_MODE = 0o600

# --- 파일명 상수 (기존 /tmp 파일명 그대로 유지 — base 만 이동) ---
CONVERSATIONS = "jarvis-conversations.jsonl"
CONVERSATIONS_DB = "jarvis-conversations.db"  # §10-4a SQLite backing
CONVERSATIONS_ARCHIVE = "jarvis-conversations-archive"
TASKS_LEDGER = "jarvis-stone0-tasks.jsonl"
LAYER0_MEMORY = "jarvis-v00-layer0-memory.jsonl"
LAYER1_REPORT = "jarvis-v00-layer1-report.json"
MULTI_MODEL_MEASUREMENT = "jarvis-v00-multi-model-measurement.json"
BOSS_MEASUREMENT = "jarvis-v00-boss-measurement.json"


def data_dir() -> Path:
    """영속 데이터 base 디렉터리 (생성하지 않음 — 경로만 계산).

    precedence: JARVIS_DATA_DIR > $XDG_DATA_HOME/jarvis > ~/.local/share/jarvis.
    """
    override = os.environ.get("JARVIS_DATA_DIR")
    if override:
        return Path(override).expanduser()
    xdg = os.environ.get("XDG_DATA_HOME")
    if xdg:
        return Path(xdg).expanduser() / _APP_DIR_NAME
    return Path.home() / ".local" / "share" / _APP_DIR_NAME


def ensure_data_dir() -> Path:
    """base 디렉터리 생성 + 0700 보장."""
    d = data_dir()
    d.mkdir(parents=True, exist_ok=True)
    os.chmod(d, _DIR_MODE)
    return d


def data_file(name: str) -> Path:
    """base 하위 파일 경로. base 디렉터리 0700 보장 + 기존 파일이면 0600 보장.

    (신규 파일은 호출자가 생성 — 다음 data_file 호출 시 0600 적용된다.)
    """
    d = ensure_data_dir()
    p = d / name
    if p.is_file():
        os.chmod(p, _FILE_MODE)
    return p


def data_subdir(name: str) -> Path:
    """base 하위 디렉터리 생성 + 0700 보장."""
    ensure_data_dir()
    sub = data_dir() / name
    sub.mkdir(parents=True, exist_ok=True)
    os.chmod(sub, _DIR_MODE)
    return sub


# --- 명명 헬퍼 (사용처는 이 함수만 호출 — 경로 하드코딩 0) ---
def conversations_path() -> Path:
    return data_file(CONVERSATIONS)


def conversations_archive_dir() -> Path:
    return data_subdir(CONVERSATIONS_ARCHIVE)


def conversations_db_path() -> Path:
    """§10-4a 대화 SQLite backing. legacy jarvis-conversations.jsonl 은 마이그레이션 원본으로 보존."""
    return data_file(CONVERSATIONS_DB)


def tasks_ledger_path() -> Path:
    return data_file(TASKS_LEDGER)


def layer0_memory_path() -> Path:
    return data_file(LAYER0_MEMORY)


def layer1_report_path() -> Path:
    return data_file(LAYER1_REPORT)


def multi_model_measurement_path() -> Path:
    return data_file(MULTI_MODEL_MEASUREMENT)


def boss_measurement_path() -> Path:
    return data_file(BOSS_MEASUREMENT)


def worker_raw_log_path(worker: str, backend: str) -> Path:
    """워커별 raw 로그 — jarvis-v00-{worker}-worker-{backend}-raw.log."""
    return data_file(f"jarvis-v00-{worker}-worker-{backend}-raw.log")
