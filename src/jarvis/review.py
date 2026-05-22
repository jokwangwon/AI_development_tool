"""ReviewGuard — 무비판 수용 금지 결정적 가드.

답습: docs/phase0/jarvis-orchestrator-mvp-design-brief.md §6
  - 사장은 워커 출력을 결정적 가드로 검토(파괴적 명령 패턴·diff) 후 대표 보고.
  - prompt injection 체인 차단(워커 출력의 위험 명령을 그대로 신뢰 금지).
  - CLAUDE.md "계산적 검증 우선": 정규식(결정적) 매칭. 추론적 검토는 보조(후속).

본 가드는 거짓 안전감을 만들지 않는다: 패턴 매칭은 *알려진* 파괴 명령만
포착하며 완전성을 주장하지 않는다(§8 FN 우선 원칙). 사람 게이트가 최종 방어.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

from src.jarvis.worker import WorkerResult

# (name, pattern) — name 은 위험 종류 식별자(flags 에 노출). 모두 IGNORECASE.
DEFAULT_PATTERNS: list[tuple[str, str]] = [
    ("destructive-rm", r"\brm\s+-[rf]{1,2}\b"),
    ("force-push", r"git\s+push\b[^\n]*(--force|\s-f\b)"),
    ("history-rewrite", r"git\s+(filter-branch|filter-repo|rebase\b[^\n]*-i)"),
    ("remote-pipe-shell", r"(curl|wget)\b[^\n|]*\|\s*(sh|bash)\b"),
    ("privilege-sudo", r"\bsudo\b"),
    ("disk-mkfs", r"\bmkfs(\.\w+)?\b"),
    ("disk-dd", r"\bdd\s+if="),
    ("fork-bomb", r":\s*\(\s*\)\s*\{"),
    ("chmod-world", r"\bchmod\s+-?R?\s*0?777\b"),
    ("device-write", r">\s*/dev/(sd|nvme|hd)\w*"),
]


@dataclass(frozen=True)
class ReviewVerdict:
    ok: bool
    flags: list[str]


class ReviewGuard:
    def __init__(self, extra_patterns: list[tuple[str, str]] | None = None) -> None:
        patterns = [*DEFAULT_PATTERNS, *(extra_patterns or [])]
        self._compiled = [(name, re.compile(pat, re.IGNORECASE)) for name, pat in patterns]

    def review(self, result: WorkerResult) -> ReviewVerdict:
        text = result.output or ""
        flags = [name for name, rx in self._compiled if rx.search(text)]
        return ReviewVerdict(ok=not flags, flags=flags)
