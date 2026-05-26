"""Layer 1 패턴 마이닝 — Layer 0 누적 → PatternReport (TDD).

답습: docs/phase0/jarvis-layer1-pattern-mining-brief.md
  - §1: Layer 0 수정 0 / 동작 변경 0 / 외부 호출 0.
  - §2: status / per-worker / flag freq / advice / recent failures.
  - §3: frozen dataclass + tuple (불변), mine(Iterable[dict]) decouple.
  - §4: 빈 입력·손상 entry 안전 처리.
"""
from __future__ import annotations

import dataclasses
from typing import Any

import pytest

from src.jarvis.layer1 import (
    PatternReport,
    WorkerStats,
    format_report,
    mine,
)


def _entry(
    *,
    ts: str = "2026-05-26T15:00:00+09:00",
    task_prompt: str = "p",
    worker_alias: str = "tmux-bash",
    status: str = "applied",
    exit_code: int = 0,
    is_error: bool = False,
    verdict_flags: list[str] | None = None,
    advice_summary: str | None = "ok",
    advice_failed: bool = False,
    applied: bool = True,
) -> dict[str, Any]:
    return {
        "ts": ts,
        "task_prompt": task_prompt,
        "worker_alias": worker_alias,
        "status": status,
        "exit_code": exit_code,
        "is_error": is_error,
        "verdict_flags": verdict_flags if verdict_flags is not None else [],
        "advice_summary": advice_summary,
        "advice_failed": advice_failed,
        "applied": applied,
    }


# --- §4 빈 입력 ---

def test_empty_input_returns_zero_report() -> None:
    rep = mine([])
    assert rep.total_entries == 0
    assert rep.first_ts is None and rep.last_ts is None
    assert rep.status_counts == {}
    assert rep.workers == ()
    assert rep.flag_frequency == {}
    assert rep.advice_total == 0 and rep.advice_failed == 0
    assert rep.recent_failures == ()


# --- §2 status_counts ---

def test_status_counts_aggregate() -> None:
    entries = [
        _entry(status="applied"),
        _entry(status="applied"),
        _entry(status="denied", applied=False),
        _entry(status="worker_failed", applied=False, exit_code=1, is_error=True),
    ]
    rep = mine(entries)
    assert rep.total_entries == 4
    assert rep.status_counts == {"applied": 2, "denied": 1, "worker_failed": 1}


# --- §2 per-worker stats ---

def test_per_worker_stats() -> None:
    entries = [
        _entry(worker_alias="A", status="applied"),
        _entry(worker_alias="A", status="applied"),
        _entry(worker_alias="A", status="denied", applied=False),
        _entry(worker_alias="B", status="worker_failed",
               applied=False, exit_code=1, is_error=True),
    ]
    rep = mine(entries)
    by_alias = {w.alias: w for w in rep.workers}
    a = by_alias["A"]
    b = by_alias["B"]
    assert a.total == 3 and a.applied == 2 and a.denied == 1 and a.worker_failed == 0
    assert b.total == 1 and b.applied == 0 and b.denied == 0 and b.worker_failed == 1
    assert abs(a.success_rate - (2 / 3)) < 1e-9
    assert b.success_rate == 0.0


def test_worker_with_zero_total_has_zero_success_rate() -> None:
    # WorkerStats 직접 구성 시 division-by-zero 회피 검증.
    w = WorkerStats(alias="x", total=0, applied=0, denied=0, worker_failed=0)
    assert w.success_rate == 0.0


# --- §2 flag_frequency ---

def test_flag_frequency_histogram() -> None:
    entries = [
        _entry(verdict_flags=["destructive-rm"]),
        _entry(verdict_flags=["destructive-rm", "privilege-sudo"]),
        _entry(verdict_flags=[]),
        _entry(verdict_flags=["privilege-sudo"]),
    ]
    rep = mine(entries)
    assert rep.flag_frequency == {"destructive-rm": 2, "privilege-sudo": 2}


# --- §2 advice_total / advice_failed ---

def test_advice_counts() -> None:
    entries = [
        _entry(advice_summary="ok", advice_failed=False),
        _entry(advice_summary="ok", advice_failed=False),
        _entry(advice_summary="⚠️ 실패", advice_failed=True),
        _entry(advice_summary=None, advice_failed=False),       # boss 미주입
    ]
    rep = mine(entries)
    assert rep.advice_total == 3       # advice_summary 있는 것만
    assert rep.advice_failed == 1


# --- §2 recent_failures (last N) ---

def test_recent_failures_includes_worker_failed_denied_and_advice_failed() -> None:
    entries = [
        _entry(ts="2026-05-26T10:00:00+09:00", task_prompt="ok"),
        _entry(ts="2026-05-26T10:01:00+09:00", task_prompt="bad",
               status="worker_failed", applied=False, exit_code=1, is_error=True),
        _entry(ts="2026-05-26T10:02:00+09:00", task_prompt="declined",
               status="denied", applied=False),
        _entry(ts="2026-05-26T10:03:00+09:00", task_prompt="boss down",
               advice_failed=True, advice_summary="⚠️"),
    ]
    rep = mine(entries)
    failures = [e["task_prompt"] for e in rep.recent_failures]
    # 정상 1건 제외, 3건 모두 failure 로 분류 + 최신순(desc)
    assert failures == ["boss down", "declined", "bad"]


def test_recent_failures_limited_to_N() -> None:
    failure_entries = [
        _entry(ts=f"2026-05-26T10:{i:02d}:00+09:00", task_prompt=f"f{i}",
               status="worker_failed", applied=False, exit_code=1, is_error=True)
        for i in range(10)
    ]
    rep = mine(failure_entries, recent_failure_limit=3)
    assert len(rep.recent_failures) == 3
    assert [e["task_prompt"] for e in rep.recent_failures] == ["f9", "f8", "f7"]


# --- §2 first/last ts ---

def test_first_last_ts_taken_from_input_order_min_max() -> None:
    entries = [
        _entry(ts="2026-05-26T10:00:00+09:00"),
        _entry(ts="2026-05-26T09:00:00+09:00"),
        _entry(ts="2026-05-26T11:00:00+09:00"),
    ]
    rep = mine(entries)
    assert rep.first_ts == "2026-05-26T09:00:00+09:00"
    assert rep.last_ts == "2026-05-26T11:00:00+09:00"


# --- §3 frozen 불변 ---

def test_pattern_report_is_frozen() -> None:
    rep = mine([])
    with pytest.raises(dataclasses.FrozenInstanceError):
        rep.total_entries = 5  # type: ignore[misc]
    # 컬렉션은 tuple/dict(immutable for tuple, dict는 mutable 이지만 위 frozen 으로
    # 재할당 차단). recent_failures = tuple 강제.
    assert isinstance(rep.workers, tuple)
    assert isinstance(rep.recent_failures, tuple)


def test_worker_stats_is_frozen() -> None:
    w = WorkerStats(alias="x", total=1, applied=1, denied=0, worker_failed=0)
    with pytest.raises(dataclasses.FrozenInstanceError):
        w.total = 99  # type: ignore[misc]


# --- §4 손상 entry skip ---

def test_malformed_entry_skipped_silently() -> None:
    entries = [
        _entry(),
        {"missing": "required-keys"},     # 필수 필드 누락
        _entry(),
    ]
    rep = mine(entries)
    assert rep.total_entries == 2     # 손상된 1건 skip


# --- §1 decouple: MemoryLog 미참조 ---

def test_layer1_module_does_not_import_memorylog() -> None:
    """Layer 1 은 Layer 0 와 decouple (Iterable[dict] 만 수신 — brief §1·§3 답습).

    Docstring 내 'MemoryLog' 언급은 허용(설명용). 금지 = 실제 import.
    """
    import ast
    import src.jarvis.layer1 as m
    tree = ast.parse(open(m.__file__, encoding="utf-8").read())
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            assert node.module != "src.jarvis.memory"
            assert not (node.module or "").startswith("src.jarvis.memory")
        elif isinstance(node, ast.Import):
            for alias in node.names:
                assert alias.name != "src.jarvis.memory"
    # 실 모듈 namespace 에 MemoryLog 미주입
    assert not hasattr(m, "MemoryLog")


# --- §3 format_report 텍스트 ---

def test_format_report_returns_non_empty_text_even_for_empty_input() -> None:
    rep = mine([])
    out = format_report(rep)
    assert isinstance(out, str) and out.strip()
    # 빈 데이터 시 사용자에게 명시 (거짓 안전감 차단, brief §4)
    assert "0" in out or "없음" in out or "empty" in out.lower() or "데이터" in out


def test_format_report_mentions_status_and_worker_stats() -> None:
    entries = [
        _entry(worker_alias="A"),
        _entry(worker_alias="A", status="denied", applied=False),
        _entry(worker_alias="B", verdict_flags=["destructive-rm"]),
    ]
    rep = mine(entries)
    out = format_report(rep)
    assert "A" in out and "B" in out
    assert "applied" in out
    assert "destructive-rm" in out
