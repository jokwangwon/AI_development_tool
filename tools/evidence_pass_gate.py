#!/usr/bin/env python3
"""Evidence / PASS Gate validator — Group B PoC (G3 통합).

답습 출처:
  - docs/architecture/implementation-runtime-roadmap.md §3.1 (G3 Hermes-originated commit auto-reject + Evidence 없는 PASS 차단)
  - docs/architecture/governance-preconditions.md §1.2 P10 (Evidence Forgery)
  - docs/architecture/hermes-not-root-of-trust-runtime.md §2.2 #20 (Hermes-originated commit 차단)
  - docs/decisions/ADR-012-evidence-ledger-protection.md §2.12 (Hermes 변조 차단 매트릭스 4항목)
  - docs/decisions/ADR-011-means-vs-ends-redaction.md §2.1 (a)~(e)
  - tools/provider_import_scanner.py (Group A 1차 시제 직접 답습)

본 validator 는 *Markdown governance 문서 내부* 의 두 위반을 통합 검출한다:

  검사 1 (Hermes-originated marker)
    - frontmatter / trailer / 본문의 'Generated-by: Hermes', 'Agent-Origin: Hermes',
      'Authored-by: Hermes', 'Co-Authored-By: Hermes' 등 marker
    - governance 표현 (PASS / APPROVE / Gate PASS / Implementation PASS) 와
      *공동 발생* 시 FAIL — Hermes 가 governance 승인 주체로 *오해* 차단

  검사 2 (Evidence 없는 PASS 차단)
    - PASS / APPROVE / Gate PASS / Implementation PASS / Design PASS 표현 검출 →
      evidence reference 최소 1건 검증
    - Implementation PASS 선언 시 → Design vs Implementation 구분 명시 의무

본 PoC 는 *형식적 차단* (Layer 1 답습) 한정. 실 git history 검증 / 실 hook
activation 은 별도 합의.
"""
from __future__ import annotations

import argparse
import re
import sys
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path

# --- Hermes marker patterns (검사 1) ---------------------------------------
# 본 PoC 는 frontmatter/trailer/본문 위치 무관 라인 단위 검출.
# 'Co-Authored-By: Claude' 등 *Worker Agent 가 아닌* 정상 Claude trailer 는 본 PoC 외.
HERMES_MARKER_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"^\s*Generated-by\s*:\s*Hermes\b", re.IGNORECASE),
    re.compile(r"^\s*Agent-Origin\s*:\s*Hermes\b", re.IGNORECASE),
    re.compile(r"^\s*Authored-by\s*:\s*Hermes\b", re.IGNORECASE),
    re.compile(r"^\s*Co-Authored-By\s*:\s*Hermes\b", re.IGNORECASE),
    re.compile(r"^\s*Approved-by\s*:\s*Hermes\b", re.IGNORECASE),
    re.compile(r"^\s*Signed-off-by\s*:\s*Hermes\b", re.IGNORECASE),
)

# --- Governance PASS expressions (검사 2 anchor) ---------------------------
# 본 PoC 는 *명시 선언 표현* 한정. 'PASS' 단독 단어는 ambiguity 회피 위해 제외.
PASS_DECLARATION_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"\bGate\s+PASS\b", re.IGNORECASE),
    re.compile(r"\bImplementation\s+PASS\b", re.IGNORECASE),
    re.compile(r"\bImplementation/Runtime\s+PASS\b", re.IGNORECASE),
    re.compile(r"\bDesign\s+PASS\b", re.IGNORECASE),
    re.compile(r"\bDesign/Governance\s+PASS\b", re.IGNORECASE),
    re.compile(r"\bAPPROVE\s+WITH\s+CONDITIONS\b", re.IGNORECASE),
    re.compile(r"^\s*##*\s*APPROVE\b", re.IGNORECASE | re.MULTILINE),
    re.compile(r"\bG[1-9]\w*\s+PASS\b", re.IGNORECASE),
    re.compile(r"\bGP-\d+\s+PASS\b", re.IGNORECASE),
)

# --- Implementation PASS strict subset (검사 2 추가 — Design 분리 의무) -----
IMPLEMENTATION_PASS_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"\bImplementation\s+PASS\b", re.IGNORECASE),
    re.compile(r"\bImplementation/Runtime\s+PASS\b", re.IGNORECASE),
)

# --- Design vs Implementation 구분 marker (PASS criterion) -----------------
DESIGN_VS_IMPL_MARKERS: tuple[re.Pattern[str], ...] = (
    re.compile(r"Implementation\s+Pending", re.IGNORECASE),
    re.compile(r"Design/Governance\s+PASS", re.IGNORECASE),
    re.compile(r"DESIGN\s+PASS\s*/\s*IMPLEMENTATION\s+PENDING", re.IGNORECASE),
)

# --- Evidence reference patterns (검사 2 PASS 조건) ------------------------
EVIDENCE_REFERENCE_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"docs/review/[\w/.\-]+\.md"),
    re.compile(r"docs/evidence/[\w/.\-]+\.(?:jsonl|md)"),
    re.compile(r"actions/runs/\d{6,}"),
    re.compile(r"\b[0-9a-f]{7,40}\b"),  # commit SHA (7+ hex)
    re.compile(r"^\s*event\s*:\s*[a-z_]+", re.IGNORECASE | re.MULTILINE),
    re.compile(r"docs/phase0/[\w/.\-]+\.md"),
)


@dataclass(frozen=True)
class Violation:
    file: Path
    line: int
    pattern: str
    detail: str

    def format(self) -> str:
        return f"{self.file}:{self.line}:{self.pattern}:{self.detail}"


def _find_lines(source: str, patterns: tuple[re.Pattern[str], ...]) -> list[tuple[int, str, str]]:
    """Return (lineno, pattern_repr, matched_text) per match, line-anchored when MULTILINE."""
    hits: list[tuple[int, str, str]] = []
    for pat in patterns:
        if pat.flags & re.MULTILINE:
            for m in pat.finditer(source):
                lineno = source.count("\n", 0, m.start()) + 1
                hits.append((lineno, pat.pattern, m.group(0).strip()[:80]))
        else:
            for idx, line in enumerate(source.splitlines(), start=1):
                for m in pat.finditer(line):
                    hits.append((idx, pat.pattern, m.group(0).strip()[:80]))
    return hits


def _has_any(source: str, patterns: tuple[re.Pattern[str], ...]) -> bool:
    return any(pat.search(source) for pat in patterns)


def scan_file(path: Path) -> list[Violation]:
    try:
        source = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return []

    violations: list[Violation] = []

    pass_hits = _find_lines(source, PASS_DECLARATION_PATTERNS)
    has_pass_declaration = bool(pass_hits)

    # --- 검사 1: Hermes-originated marker + governance 공동 발생 ---
    marker_hits = _find_lines(source, HERMES_MARKER_PATTERNS)
    if marker_hits and has_pass_declaration:
        for lineno, pat, text in marker_hits:
            violations.append(
                Violation(
                    path,
                    lineno,
                    "hermes-originated-marker",
                    f"{text} (with PASS declaration in same file)",
                )
            )

    # --- 검사 2: Evidence 없는 PASS 차단 ---
    if has_pass_declaration:
        has_evidence = _has_any(source, EVIDENCE_REFERENCE_PATTERNS)
        if not has_evidence:
            for lineno, pat, text in pass_hits:
                violations.append(
                    Violation(
                        path,
                        lineno,
                        "pass-without-evidence",
                        f"{text} (no evidence reference found)",
                    )
                )

    # --- 검사 2 추가: Implementation PASS 선언 시 Design 분리 의무 ---
    if _has_any(source, IMPLEMENTATION_PASS_PATTERNS):
        has_design_split = _has_any(source, DESIGN_VS_IMPL_MARKERS)
        if not has_design_split:
            impl_hits = _find_lines(source, IMPLEMENTATION_PASS_PATTERNS)
            for lineno, pat, text in impl_hits:
                violations.append(
                    Violation(
                        path,
                        lineno,
                        "implementation-pass-unscoped",
                        f"{text} (no Design/Implementation split marker)",
                    )
                )

    return violations


def iter_markdown_files(root: Path) -> Iterator[Path]:
    if root.is_file() and root.suffix.lower() == ".md":
        yield root
        return
    for p in root.rglob("*.md"):
        if p.is_file():
            yield p


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Evidence / PASS Gate validator (Group B G3 통합 PoC)"
    )
    parser.add_argument(
        "target",
        type=Path,
        help="검사 대상 디렉터리 또는 .md 파일",
    )
    args = parser.parse_args(argv)

    if not args.target.exists():
        print(f"[ERROR] target not found: {args.target}", file=sys.stderr)
        return 2

    all_violations: list[Violation] = []
    for md_file in iter_markdown_files(args.target):
        all_violations.extend(scan_file(md_file))

    if not all_violations:
        print(f"[PASS] No violations found in: {args.target}")
        return 0

    for v in all_violations:
        print(v.format())
    print(f"[FAIL] {len(all_violations)} violation(s) found.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
