"""Layer 1 패턴 마이닝 — Layer 0 누적(JSONL) → PatternReport.

답습: docs/phase0/jarvis-layer1-pattern-mining-brief.md
  - §1 안전 등급: Layer 0 수정 0 / 자비스 동작 변경 경로 0 / 외부 호출 0.
    → 게이트 *불요* (보고서 출력은 안전 행위).
  - §3 decouple: mine() 는 `Iterable[dict]` 만 수신 — MemoryLog 미참조.
  - §3 불변: PatternReport / WorkerStats frozen + tuple.
  - §4 fail-soft: 빈 입력 / 손상 entry → silent skip.

본 모듈은 stdlib(dataclasses, collections, typing) 만 사용. 파일 IO·외부 호출 0.
자비스 동작 *변경* API 부재 — 출력은 frozen dataclass + 텍스트 한정.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from typing import Any, Iterable

# 손상 entry 식별용 — 필수 필드 누락 시 skip.
_REQUIRED_FIELDS = frozenset({
    "ts", "task_prompt", "worker_alias", "status",
    "exit_code", "is_error", "verdict_flags",
    "advice_summary", "advice_failed", "applied",
})


@dataclass(frozen=True)
class WorkerStats:
    """워커별 집계 (frozen 불변, brief §3)."""

    alias: str
    total: int
    applied: int
    denied: int
    worker_failed: int

    @property
    def success_rate(self) -> float:
        return self.applied / self.total if self.total else 0.0


@dataclass(frozen=True)
class PatternReport:
    """Layer 1 마이닝 결과 — frozen + tuple (불변, brief §3)."""

    total_entries: int
    first_ts: str | None
    last_ts: str | None
    status_counts: dict[str, int]
    workers: tuple[WorkerStats, ...]
    flag_frequency: dict[str, int]
    advice_total: int
    advice_failed: int
    recent_failures: tuple[dict[str, Any], ...]


def _is_failure(entry: dict[str, Any]) -> bool:
    """recent_failures 후보 판정 — 운영 신호 광폭(worker_failed / denied / advice_failed)."""
    if entry.get("status") in ("worker_failed", "denied"):
        return True
    if entry.get("is_error") is True:
        return True
    if entry.get("advice_failed") is True:
        return True
    return False


def _valid(entry: Any) -> bool:
    """필수 필드 체크 — 손상 entry skip (brief §4)."""
    if not isinstance(entry, dict):
        return False
    return _REQUIRED_FIELDS.issubset(entry.keys())


def mine(
    entries: Iterable[dict[str, Any]],
    recent_failure_limit: int = 5,
) -> PatternReport:
    """Layer 0 entry stream → 집계 패턴 PatternReport.

    - read-only: 입력 entry 본문 미수정.
    - 손상 entry: silent skip (`_REQUIRED_FIELDS` 누락).
    - 빈 입력: zero-state PatternReport (예외 없음).
    """
    valid: list[dict[str, Any]] = [e for e in entries if _valid(e)]
    total = len(valid)

    if total == 0:
        return PatternReport(
            total_entries=0, first_ts=None, last_ts=None,
            status_counts={}, workers=(), flag_frequency={},
            advice_total=0, advice_failed=0, recent_failures=(),
        )

    status_counts: dict[str, int] = dict(Counter(e["status"] for e in valid))

    # per-worker 집계
    worker_buckets: dict[str, dict[str, int]] = {}
    for e in valid:
        alias = e["worker_alias"]
        b = worker_buckets.setdefault(
            alias, {"total": 0, "applied": 0, "denied": 0, "worker_failed": 0}
        )
        b["total"] += 1
        s = e["status"]
        if s in b:
            b[s] += 1
    workers = tuple(
        WorkerStats(alias=alias, **counts)
        for alias, counts in sorted(worker_buckets.items())
    )

    # flag 빈도
    flag_counter: Counter[str] = Counter()
    for e in valid:
        for f in e.get("verdict_flags") or []:
            flag_counter[f] += 1
    flag_frequency = dict(flag_counter)

    # advice 집계 — boss 발화 entry 만 분모
    advice_total = sum(1 for e in valid if e.get("advice_summary"))
    advice_failed = sum(1 for e in valid if e.get("advice_failed"))

    # recent_failures — ts 내림차순 top N
    failures = [e for e in valid if _is_failure(e)]
    failures.sort(key=lambda e: e.get("ts", ""), reverse=True)
    recent_failures = tuple(failures[:max(0, recent_failure_limit)])

    # ts 범위 (string ISO 8601 사전순 = 시간순 — UTC offset 같은 정상 입력 가정)
    ts_list = [e["ts"] for e in valid if e.get("ts")]
    first_ts = min(ts_list) if ts_list else None
    last_ts = max(ts_list) if ts_list else None

    return PatternReport(
        total_entries=total,
        first_ts=first_ts,
        last_ts=last_ts,
        status_counts=status_counts,
        workers=workers,
        flag_frequency=flag_frequency,
        advice_total=advice_total,
        advice_failed=advice_failed,
        recent_failures=recent_failures,
    )


def format_report(report: PatternReport) -> str:
    """사람 가독 텍스트 보고서 — 빈 데이터 시 명시(거짓 안전감 차단, brief §4)."""
    lines: list[str] = []
    lines.append("=== Jarvis Layer 1 Pattern Report ===")
    lines.append(f"누적 entries : {report.total_entries}")
    if report.total_entries == 0:
        lines.append("(데이터 없음 — Layer 0 누적 0건)")
        return "\n".join(lines)

    lines.append(f"관찰 범위    : {report.first_ts} → {report.last_ts}")
    lines.append("")
    lines.append("Status 분포:")
    for st, cnt in sorted(report.status_counts.items()):
        lines.append(f"  {st:<16} {cnt}")

    lines.append("")
    lines.append("워커별:")
    for w in report.workers:
        lines.append(
            f"  {w.alias:<16} total={w.total} applied={w.applied} "
            f"denied={w.denied} worker_failed={w.worker_failed} "
            f"success={w.success_rate * 100:.1f}%"
        )

    lines.append("")
    lines.append("Verdict flag 빈도:")
    if report.flag_frequency:
        for flag, cnt in sorted(
            report.flag_frequency.items(), key=lambda kv: (-kv[1], kv[0])
        ):
            lines.append(f"  {flag:<24} {cnt}")
    else:
        lines.append("  (없음)")

    lines.append("")
    rate = (report.advice_failed / report.advice_total
            if report.advice_total else 0.0)
    lines.append(
        f"Boss advisory: total={report.advice_total} failed={report.advice_failed}"
        f" rate={rate * 100:.1f}%"
    )

    lines.append("")
    lines.append(f"최근 실패 (top {len(report.recent_failures)}):")
    if report.recent_failures:
        for e in report.recent_failures:
            lines.append(
                f"  [{e.get('ts')}] {e.get('status'):<14} "
                f"worker={e.get('worker_alias')} "
                f"prompt={(e.get('task_prompt') or '')[:60]}"
            )
    else:
        lines.append("  (없음)")

    return "\n".join(lines)
