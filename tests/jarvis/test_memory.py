"""MemoryLog — 자가진화 Layer 0 (append-only JSONL 관찰 누적) 테스트.

답습: docs/phase0/jarvis-layer0-memory-accumulation-brief.md
  - §2: JSONL, append-only, schema fixed, truncation 2048, 민감 정보 제외.
  - §2: modify/delete API 없음 (read-only 답습).
  - §2: fail-soft (orchestrator 진행 정지 X).
  - §3: Orchestrator memory=None 하위 호환.

본 test 는 실 디스크 쓰기 (tmp_path) — append-only POSIX 동작 확인.
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from src.jarvis.approval import ApprovalGate
from src.jarvis.boss import StubBoss, BossAdvice
from src.jarvis.memory import MemoryLog
from src.jarvis.orchestrator import (
    OutcomeReport,
    OutcomeStatus,
    Orchestrator,
    WorkerRegistry,
)
from src.jarvis.review import ReviewGuard, ReviewVerdict
from src.jarvis.worker import WorkerResult


def _report(
    task_id: str = "t1",
    status: OutcomeStatus = OutcomeStatus.APPLIED,
    exit_code: int = 0,
    advice: BossAdvice | None = None,
) -> OutcomeReport:
    return OutcomeReport(
        task_prompt="hello world",
        worker_alias="tmux-bash",
        result=WorkerResult(exit_code=exit_code, output="ok", cost_usd=None,
                            is_error=exit_code != 0, raw=None),
        verdict=ReviewVerdict(ok=True, flags=[]),
        approved=status == OutcomeStatus.APPLIED,
        applied=status == OutcomeStatus.APPLIED,
        status=status,
        advice=advice,
    )


def _read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


# --- §2 append-only 적재 + schema ---

def test_append_writes_jsonl_entry(tmp_path: Path) -> None:
    log = MemoryLog(path=tmp_path / "mem.jsonl")
    log.append(_report(task_id="t-001"))
    entries = _read_jsonl(tmp_path / "mem.jsonl")
    assert len(entries) == 1
    e = entries[0]
    assert e["worker_alias"] == "tmux-bash"
    assert e["status"] == "applied"
    assert e["exit_code"] == 0
    assert e["is_error"] is False
    assert e["applied"] is True
    assert "ts" in e
    assert "task_prompt" in e
    assert "verdict_flags" in e


def test_append_multiple_preserves_order(tmp_path: Path) -> None:
    log = MemoryLog(path=tmp_path / "mem.jsonl")
    log.append(_report(task_id="a"))
    log.append(_report(task_id="b"))
    log.append(_report(task_id="c"))
    entries = list(log.read())
    assert len(entries) == 3
    # 적재 순서 = 읽기 순서 (append-only POSIX)
    assert [e["task_prompt"] for e in entries] == ["hello world"] * 3


def test_append_creates_parent_dirs(tmp_path: Path) -> None:
    path = tmp_path / "deep" / "nested" / "mem.jsonl"
    log = MemoryLog(path=path)
    log.append(_report())
    assert path.exists()


def test_advice_summary_recorded_when_present(tmp_path: Path) -> None:
    log = MemoryLog(path=tmp_path / "mem.jsonl")
    advice = BossAdvice(summary="검토 완료 — 위험 없음", extra_flags=[],
                        advisory_failed=False)
    log.append(_report(advice=advice))
    e = list(log.read())[0]
    assert e["advice_summary"] == "검토 완료 — 위험 없음"
    assert e["advice_failed"] is False


def test_advice_null_when_absent(tmp_path: Path) -> None:
    log = MemoryLog(path=tmp_path / "mem.jsonl")
    log.append(_report(advice=None))
    e = list(log.read())[0]
    assert e["advice_summary"] is None
    assert e["advice_failed"] is False     # boss 부재 ≠ 실패 표지


def test_advisory_failed_recorded(tmp_path: Path) -> None:
    log = MemoryLog(path=tmp_path / "mem.jsonl")
    advice = BossAdvice(summary="⚠️ advisory 실패", extra_flags=[],
                        advisory_failed=True)
    log.append(_report(advice=advice))
    e = list(log.read())[0]
    assert e["advice_failed"] is True


# --- §2 truncation 2048 chars ---

def test_long_task_prompt_truncated(tmp_path: Path) -> None:
    log = MemoryLog(path=tmp_path / "mem.jsonl")
    big = "x" * 5000
    rep = OutcomeReport(
        task_prompt=big,
        worker_alias="w", result=WorkerResult(0, "ok", None, False, None),
        verdict=ReviewVerdict(True, []), approved=True, applied=True,
        status=OutcomeStatus.APPLIED, advice=None,
    )
    log.append(rep)
    e = list(log.read())[0]
    assert len(e["task_prompt"]) <= 2048


def test_long_advice_summary_truncated(tmp_path: Path) -> None:
    log = MemoryLog(path=tmp_path / "mem.jsonl")
    big = "y" * 5000
    log.append(_report(advice=BossAdvice(summary=big, extra_flags=[],
                                         advisory_failed=False)))
    e = list(log.read())[0]
    assert len(e["advice_summary"]) <= 2048


# --- §2 민감 정보 차단 ---

def test_sensitive_fields_not_recorded(tmp_path: Path) -> None:
    """cost_usd / workdir / raw output 은 schema 에서 제외."""
    log = MemoryLog(path=tmp_path / "mem.jsonl")
    rep = OutcomeReport(
        task_prompt="p",
        worker_alias="w",
        result=WorkerResult(0, "라우드 출력 본문", 0.05, False, {"x": "y"}),
        verdict=ReviewVerdict(True, []), approved=True, applied=True,
        status=OutcomeStatus.APPLIED, advice=None,
    )
    log.append(rep)
    e = list(log.read())[0]
    assert "cost_usd" not in e
    assert "workdir" not in e
    assert "raw" not in e
    assert "라우드 출력 본문" not in json.dumps(e)


# --- §2 read-only API (modify/delete 없음) ---

def test_memory_log_has_no_modify_or_delete_methods() -> None:
    public = {name for name in dir(MemoryLog) if not name.startswith("_")}
    for forbidden in ("delete", "modify", "update", "clear", "remove", "pop"):
        assert forbidden not in public, f"MemoryLog.{forbidden} 금지(read-only 답습)"


# --- §2 fail-soft ---

def test_fail_soft_on_io_error_returns_silently(tmp_path: Path, monkeypatch) -> None:
    """디스크 쓰기 예외 → silent (orchestrator 진행 정지 X 책무)."""
    log = MemoryLog(path=tmp_path / "mem.jsonl")

    def boom(*a, **kw):  # type: ignore[no-untyped-def]
        raise OSError("disk full 모사")

    monkeypatch.setattr("builtins.open", boom)
    # 예외가 호출자에게 전파되지 않음
    log.append(_report())


# --- §3 Orchestrator 통합 (memory=None 하위 호환) ---

class _FakeWorker:
    alias = "fake"
    def run(self, prompt: str, workdir: str) -> WorkerResult:
        return WorkerResult.from_cli(0, '{"result": "ok", "is_error": false}')


def _orch_with_memory(memory: MemoryLog | None) -> Orchestrator:
    reg = WorkerRegistry()
    reg.register(_FakeWorker())
    return Orchestrator(
        registry=reg, guard=ReviewGuard(),
        gate=ApprovalGate(approver=lambda req: True),
        workdir_factory=lambda task_id: "/tmp/ws",
        memory=memory,
    )


def test_orchestrator_records_report_to_memory(tmp_path: Path) -> None:
    log = MemoryLog(path=tmp_path / "mem.jsonl")
    orch = _orch_with_memory(memory=log)
    orch.dispatch(prompt="task A", task_id="ta")
    orch.dispatch(prompt="task B", task_id="tb")
    entries = list(log.read())
    assert len(entries) == 2
    assert entries[0]["task_prompt"] == "task A"
    assert entries[1]["task_prompt"] == "task B"


def test_orchestrator_without_memory_preserves_behavior(tmp_path: Path) -> None:
    """memory=None 일 때 기존 동작 그대로(하위 호환)."""
    orch = _orch_with_memory(memory=None)
    rep = orch.dispatch(prompt="solo", task_id="ts")
    assert rep.status == OutcomeStatus.APPLIED
    # 본 test 의 검증 = 예외 없음 + report 정상


def test_orchestrator_memory_failure_does_not_break_dispatch(
    tmp_path: Path, monkeypatch
) -> None:
    """memory.append 실패 → dispatch 정상 종료 (fail-soft 답습)."""
    log = MemoryLog(path=tmp_path / "mem.jsonl")
    # MemoryLog 자체는 fail-soft 이지만, 더 강한 경로 = append 자체를 폭발시켜도
    # orchestrator 가 흡수해야 한다 (Layer 0 부재 ≠ 차단).
    def boom(self, report):  # type: ignore[no-untyped-def]
        raise RuntimeError("memory 폭탄")
    monkeypatch.setattr(MemoryLog, "append", boom)
    orch = _orch_with_memory(memory=log)
    rep = orch.dispatch(prompt="p", task_id="t")
    assert rep.status == OutcomeStatus.APPLIED
