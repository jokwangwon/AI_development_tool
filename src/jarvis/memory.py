"""MemoryLog — 자가진화 Layer 0 (관찰 누적, append-only JSONL).

답습: docs/phase0/jarvis-layer0-memory-accumulation-brief.md
  - §1: Layer 0 = read-only 관찰 누적. 동작 변경 0 → 게이트 *불요*.
  - §2: JSONL append-only, modify/delete API 없음(read-only 답습).
  - §2: schema 고정 + truncation 2048 chars + 민감 정보(cost/workdir/raw) 제외.
  - §2: fail-soft — 디스크 쓰기 실패가 dispatch 를 차단하지 않는다.
  - §3: Orchestrator.memory 주입(optional, 미주입=하위 호환).

본 모듈은 외부 SDK import 0 — stdlib(json, pathlib, datetime) 만 사용.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import TYPE_CHECKING, Any, Iterator

if TYPE_CHECKING:
    from src.jarvis.orchestrator import OutcomeReport

# 저장량 폭주 차단 — task_prompt / advice_summary 각 상한.
_MAX_TEXT_CHARS = 2048


def _truncate(s: str | None) -> str | None:
    if s is None:
        return None
    if len(s) <= _MAX_TEXT_CHARS:
        return s
    return s[:_MAX_TEXT_CHARS]


def _now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def _report_to_entry(report: "OutcomeReport") -> dict[str, Any]:
    """OutcomeReport → JSONL entry dict (schema 고정 + 민감 정보 제외).

    민감 정보 제외: cost_usd, workdir, result.raw, result.output(raw 본문) —
    Layer 0 = 관찰 *요약* 한정. raw 는 별도 /tmp 로그가 권위(brief §2 답습).
    """
    advice = report.advice
    return {
        "ts": _now_iso(),
        "task_prompt": _truncate(report.task_prompt),
        "worker_alias": report.worker_alias,
        "status": report.status.value,
        "exit_code": report.result.exit_code,
        "is_error": bool(report.result.is_error),
        "verdict_flags": list(report.verdict.flags),
        "advice_summary": _truncate(advice.summary) if advice else None,
        "advice_failed": bool(advice.advisory_failed) if advice else False,
        "applied": bool(report.applied),
    }


class MemoryLog:
    """append-only JSONL 관찰 누적기 — read-only API 한정.

    `append(report)` = 1 entry 적재 (fail-soft, 예외 흡수).
    `read()` = 적재 순서 보존 iter (raw 파일 미존재 시 빈 iter).
    modify / delete / clear 등 *변경 API 부재* = brief §2 read-only 답습.
    """

    def __init__(self, path: str | Path) -> None:
        self._path = Path(path)

    @property
    def path(self) -> Path:
        return self._path

    def append(self, report: "OutcomeReport") -> None:
        """1 entry 적재. 디스크/직렬화 실패 = silent (fail-soft 답습).

        Layer 0 부재(쓰기 실패)가 dispatch 를 차단하면 layer 의 안전 등급이
        깨진다. 호출측(Orchestrator) 도 dispatch 본문은 try/except 로 흡수
        — 두 겹 fail-soft 가 책무 분리(brief §2).
        """
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            line = json.dumps(_report_to_entry(report), ensure_ascii=False)
            with open(self._path, "a", encoding="utf-8") as fh:
                fh.write(line + "\n")
        except Exception:
            # silent — Layer 0 = 관찰 부재가 차단 사유 0건
            return

    def read(self) -> Iterator[dict[str, Any]]:
        """JSONL 파일을 순서 보존 iter 로 반환. 파일 미존재 = 빈 iter."""
        if not self._path.exists():
            return iter(())
        return self._iter_lines()

    def _iter_lines(self) -> Iterator[dict[str, Any]]:
        with open(self._path, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    yield json.loads(line)
                except (json.JSONDecodeError, TypeError):
                    # 손상 라인 = skip (관찰 누적 권위는 정상 라인만)
                    continue
