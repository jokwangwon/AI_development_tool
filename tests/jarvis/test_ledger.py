"""LedgerLog — 디딤돌0 영속 레저 (append-only event-sourcing JSONL) 테스트.

답습: docs/phase0/jarvis-collaborative-orchestration-design-brief.md (v2)
  - §5 영속 레저 = LedgerLog (B6): MemoryLog 직접 재사용 불가(카드 상태 가변).
    별도 모듈, 같은 fail-soft JSONL *패턴* 답습. 상태 = 이벤트 fold 결과.
  - §5 재시작 고아: "마지막 상태=running/awaiting 인 task = interrupted" fold.
    자동 복구 없음(정직·단순).
  - §5 scrub 모순 해소(B5): 레저는 *덤 persister* — scrub/exfil 검사는 board(호출측)
    책무. 본 모듈은 주어진 필드를 그대로 적재(영속 *수단*만).
  - fold() = 공유 맥락 read API (디딤돌0).

본 test 는 실 디스크 쓰기(tmp_path) — append-only POSIX 동작 + fold 재구성 확인.
"""
from __future__ import annotations

import json
from pathlib import Path

from src.jarvis.ledger import LedgerLog


def _read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


# --- append-only 적재 + schema ---

def test_record_writes_event(tmp_path: Path) -> None:
    log = LedgerLog(path=tmp_path / "ledger.jsonl")
    log.record("t-001", "created", prompt="hello", worker_type="ollama", status="running")
    events = _read_jsonl(tmp_path / "ledger.jsonl")
    assert len(events) == 1
    e = events[0]
    assert e["task_id"] == "t-001"
    assert e["event"] == "created"
    assert e["prompt"] == "hello"
    assert e["status"] == "running"
    assert "ts" in e


def test_record_appends_preserve_order(tmp_path: Path) -> None:
    log = LedgerLog(path=tmp_path / "ledger.jsonl")
    log.record("t", "created", status="running")
    log.record("t", "awaiting", status="awaiting")
    log.record("t", "resolved", status="applied")
    events = list(log.read())
    assert [e["event"] for e in events] == ["created", "awaiting", "resolved"]


def test_record_creates_parent_dirs(tmp_path: Path) -> None:
    path = tmp_path / "deep" / "nested" / "ledger.jsonl"
    LedgerLog(path=path).record("t", "created", status="running")
    assert path.exists()


def test_read_empty_when_missing(tmp_path: Path) -> None:
    log = LedgerLog(path=tmp_path / "absent.jsonl")
    assert list(log.read()) == []


def test_corrupt_line_skipped(tmp_path: Path) -> None:
    path = tmp_path / "ledger.jsonl"
    log = LedgerLog(path=path)
    log.record("t", "created", status="running")
    with open(path, "a", encoding="utf-8") as fh:
        fh.write("{ not json\n")
    log.record("t", "resolved", status="applied")
    events = list(log.read())
    assert [e["event"] for e in events] == ["created", "resolved"]  # 손상 라인 skip


# --- fold (이벤트 재구성 = 공유 맥락 read API) ---

def test_fold_reconstructs_terminal_card(tmp_path: Path) -> None:
    log = LedgerLog(path=tmp_path / "ledger.jsonl")
    log.record("t1", "created", prompt="task A", worker_type="ollama", status="running")
    log.record("t1", "awaiting", flags=["x"], status="awaiting")
    log.record("t1", "resolved", status="applied", decision=True)
    cards = log.fold()
    assert set(cards) == {"t1"}
    card = cards["t1"]
    assert card["id"] == "t1"
    assert card["prompt"] == "task A"      # created 필드 보존
    assert card["flags"] == ["x"]           # awaiting 필드 병합
    assert card["status"] == "applied"      # 마지막 상태 승리
    assert card["decision"] is True


def test_fold_last_status_wins(tmp_path: Path) -> None:
    log = LedgerLog(path=tmp_path / "ledger.jsonl")
    log.record("t", "created", status="running")
    log.record("t", "resolved", status="denied")
    assert log.fold()["t"]["status"] == "denied"


def test_fold_running_orphan_marked_interrupted(tmp_path: Path) -> None:
    """재시작 고아: 마지막 상태=running → interrupted (자동 복구 없음)."""
    log = LedgerLog(path=tmp_path / "ledger.jsonl")
    log.record("t", "created", prompt="p", status="running")
    assert log.fold()["t"]["status"] == "interrupted"


def test_fold_awaiting_orphan_marked_interrupted(tmp_path: Path) -> None:
    log = LedgerLog(path=tmp_path / "ledger.jsonl")
    log.record("t", "created", status="running")
    log.record("t", "awaiting", status="awaiting")
    assert log.fold()["t"]["status"] == "interrupted"


def test_fold_terminal_states_not_interrupted(tmp_path: Path) -> None:
    log = LedgerLog(path=tmp_path / "ledger.jsonl")
    for tid, final in (("a", "applied"), ("d", "denied"), ("f", "failed"), ("c", "cancelled")):
        log.record(tid, "created", status="running")
        log.record(tid, "resolved", status=final)
    cards = log.fold()
    assert cards["a"]["status"] == "applied"
    assert cards["d"]["status"] == "denied"
    assert cards["f"]["status"] == "failed"
    assert cards["c"]["status"] == "cancelled"


def test_fold_multiple_tasks_independent(tmp_path: Path) -> None:
    log = LedgerLog(path=tmp_path / "ledger.jsonl")
    log.record("a", "created", status="running")
    log.record("b", "created", status="running")
    log.record("a", "resolved", status="applied")
    cards = log.fold()
    assert cards["a"]["status"] == "applied"
    assert cards["b"]["status"] == "interrupted"  # b 는 미완 고아


def test_fold_preserves_first_seen_order(tmp_path: Path) -> None:
    log = LedgerLog(path=tmp_path / "ledger.jsonl")
    log.record("z", "created", status="running")
    log.record("a", "created", status="running")
    assert list(log.fold()) == ["z", "a"]


# --- dismissed (UI 제거 — append-only 존중, fold 제외) ---

def test_fold_excludes_dismissed_task(tmp_path: Path) -> None:
    """dismissed 이벤트 = fold 결과에서 task 완전 제외(레저엔 기록 보존)."""
    log = LedgerLog(path=tmp_path / "ledger.jsonl")
    log.record("t", "created", status="running")
    log.record("t", "resolved", status="applied")
    log.record("t", "dismissed")
    assert "t" not in log.fold()                 # fold 제외
    # 레저 원본엔 기록 보존(append-only)
    assert any(e["event"] == "dismissed" for e in log.read())


def test_fold_dismissed_only_target_excluded(tmp_path: Path) -> None:
    log = LedgerLog(path=tmp_path / "ledger.jsonl")
    log.record("keep", "created", status="running")
    log.record("keep", "resolved", status="applied")
    log.record("gone", "created", status="running")
    log.record("gone", "resolved", status="failed")
    log.record("gone", "dismissed")
    cards = log.fold()
    assert set(cards) == {"keep"}


# --- append-only API (modify/delete 없음) ---

def test_ledger_has_no_modify_or_delete_methods() -> None:
    public = {name for name in dir(LedgerLog) if not name.startswith("_")}
    for forbidden in ("delete", "modify", "update", "clear", "remove", "pop", "edit"):
        assert forbidden not in public, f"LedgerLog.{forbidden} 금지(append-only 답습)"


# --- fail-soft ---

def test_fail_soft_on_io_error(tmp_path: Path, monkeypatch) -> None:
    """디스크 쓰기 예외 → silent (board dispatch 차단 X 책무)."""
    log = LedgerLog(path=tmp_path / "ledger.jsonl")

    def boom(*a, **kw):  # type: ignore[no-untyped-def]
        raise OSError("disk full 모사")

    monkeypatch.setattr("builtins.open", boom)
    log.record("t", "created", status="running")  # 예외 전파 0
