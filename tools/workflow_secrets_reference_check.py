#!/usr/bin/env python3
# Stage 5 Cycle 2 — 5.2 secrets.* 참조 감지 (context 분류) 도구
#
# 답습 출처:
#   - docs/review/3plus1-consensus-2026-05-13-stage5-g3-7-implementation-entry.md §1.4 + §3
#   - docs/phase0/backlog6-implementation-step-brief.md §2.2.5 (Stage 5 G3-7 영역)
#   - tools/workflow_secrets_usage_check.py (Cycle 1 — binary 0건 검증 답습)
#   - tools/mvp1_pc3_ar1_integration_check.py (Stage 4 도구 답습 — indent + name 패턴 분류)
#
# Cycle 1 (5.1) 과의 차이:
#   - Cycle 1 = secrets 사용 0건 *binary* 검증 (broad)
#   - Cycle 2 = `secrets.*` 참조 *context 분류* (env / with / run / if + secrets-block)
#
# 검출 대상 (5 context):
#   - env block 내 ``${{ secrets.NAME }}``
#   - with block 내 ``${{ secrets.NAME }}``
#   - run block (shell) 내 ``${{ secrets.NAME }}``
#   - if expression 내 ``secrets.NAME`` (with or without ${{ }} — if 는 wrapping 불필요)
#   - top-level / job-level ``secrets:`` block header
#
# 본 도구가 *하지 않는* 것:
#   - 실 GitHub Actions secret 호출 / repo settings API 호출 0건
#   - secret 값 자체 검사 0건 (식별자 검사 한정)
#   - permissions / fork PR policy / GITHUB_TOKEN 권한 검사 (Cycle 3/4 영역)
#   - workflow YAML 완전 schema validation (indent-based 분류 한정)
#
# stdlib 전용 (re + dataclasses + sys + argparse + pathlib) — 외부 의존성 0건.
#
# 종료 코드:
#   0 = 위반 0건 (PASS — secrets 참조 0건)
#   1 = ≥1 위반 검출 (FAIL)
#   2 = 입력 오류 (path 부재 / 파일 읽기 실패)

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional

# ``${{ secrets.NAME }}`` interpolation (any context).
SECRETS_INTERP_PATTERN = re.compile(
    r"\$\{\{\s*secrets\.([A-Za-z_][A-Za-z0-9_]*)\s*\}\}"
)
# Bare ``secrets.NAME`` (used in `if:` expressions — no ${{ }} wrapping required).
SECRETS_BARE_PATTERN = re.compile(
    r"\bsecrets\.([A-Za-z_][A-Za-z0-9_]*)\b"
)
# Key header line: `<indent>key:` (no value or value on same line).
KEY_HEADER_PATTERN = re.compile(r"^(\s*)([A-Za-z_][\w-]*)\s*:\s*(.*)$")
# ``secrets:`` block header (top-level / reusable workflow input).
SECRETS_BLOCK_PATTERN = re.compile(r"^(\s*)secrets\s*:\s*(.*)$")

# Tracked context keys (5종).
CONTEXT_KEYS = {"env", "with", "run", "if"}


@dataclass
class Finding:
    file: Path
    line: int
    context: str  # env / with / run / if / secrets-block / unknown
    secret_name: str
    text: str


@dataclass
class ReferenceReport:
    files_scanned: int = 0
    findings: List[Finding] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)

    @property
    def violations(self) -> int:
        return len(self.findings)

    def by_context(self) -> dict:
        counts: dict = {}
        for f in self.findings:
            counts[f.context] = counts.get(f.context, 0) + 1
        return counts


def _classify_context(
    indent_stack: List[tuple], line: str, line_stripped: str
) -> str:
    """Indent stack 의 nearest ancestor context key 반환."""
    # if: 는 inline value 형태 (`if: secrets.X != ''`) — 본 line 자체 검사.
    if line_stripped.startswith("if:") or line_stripped.startswith("if "):
        return "if"
    # run: | 또는 run: > 또는 run: <inline> — 본 line 또는 ancestor.
    if line_stripped.startswith("run:"):
        return "run"
    # env: / with: — block 형태이며 본 line 은 header. 본 line 자체는 secrets.* 미포함.
    # 따라서 본 helper 는 secrets.* 가 검출된 line 의 ancestor 분류 한정.
    for indent_n, key in reversed(indent_stack):
        if key in CONTEXT_KEYS:
            return key
    return "unknown"


def scan_file(path: Path) -> List[Finding]:
    """단일 workflow YAML 파일 indent-based context 분류 스캔."""
    findings: List[Finding] = []
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as e:
        raise RuntimeError(f"read failed: {path}: {e}") from e

    indent_stack: List[tuple] = []  # list of (indent, key)
    in_run_block: tuple = (-1, False)  # (indent of `run:`, active)

    for lineno, raw_line in enumerate(text.splitlines(), start=1):
        # Skip pure comment lines.
        stripped = raw_line.lstrip()
        if not stripped or stripped.startswith("#"):
            continue
        current_indent = len(raw_line) - len(stripped)

        # Update indent_stack — pop entries with indent >= current_indent.
        while indent_stack and indent_stack[-1][0] >= current_indent:
            indent_stack.pop()

        # `run:` block 종료 검출 — indent 하향 시 비활성화.
        if in_run_block[1] and current_indent <= in_run_block[0]:
            in_run_block = (-1, False)

        # Detect ``secrets:`` block header (jobs.<id>.secrets 또는 on.workflow_call.secrets).
        m_block = SECRETS_BLOCK_PATTERN.match(raw_line)
        if m_block:
            inline = m_block.group(2).strip()
            findings.append(
                Finding(
                    file=path,
                    line=lineno,
                    context="secrets-block",
                    secret_name=inline if inline else "",
                    text=stripped,
                )
            )
            # `secrets:` 자체를 stack 에 push (자식 secrets.NAME: 도 별도 검출).
            indent_stack.append((current_indent, "secrets"))
            continue

        # Key header 추적 (env / with / run / if 등).
        m_key = KEY_HEADER_PATTERN.match(raw_line)
        if m_key:
            key = m_key.group(2)
            value = m_key.group(3).strip()
            # `run:` block 시작 검출 — `run: |` 또는 `run: >` 또는 multi-line.
            if key == "run":
                if value in ("|", ">", "|-", ">-", "|+", ">+", ""):
                    in_run_block = (current_indent, True)
            indent_stack.append((current_indent, key))

        # Find secrets references on this line.
        interp_matches = list(SECRETS_INTERP_PATTERN.finditer(raw_line))
        # `if:` expression — bare `secrets.NAME` allowed.
        if_inline = stripped.startswith("if:") or stripped.startswith("if ")
        if if_inline:
            bare_matches = list(SECRETS_BARE_PATTERN.finditer(raw_line))
            # Dedupe with interp_matches by name + position.
            interp_spans = {m.span() for m in interp_matches}
            for bm in bare_matches:
                if bm.span() in interp_spans:
                    continue
                findings.append(
                    Finding(
                        file=path,
                        line=lineno,
                        context="if",
                        secret_name=bm.group(1),
                        text=stripped,
                    )
                )

        for im in interp_matches:
            # Classify context for this interpolation.
            if if_inline:
                ctx = "if"
            elif in_run_block[1]:
                ctx = "run"
            else:
                # Look at nearest ancestor context key.
                ctx = "unknown"
                for _, key in reversed(indent_stack):
                    if key in CONTEXT_KEYS:
                        ctx = key
                        break
            findings.append(
                Finding(
                    file=path,
                    line=lineno,
                    context=ctx,
                    secret_name=im.group(1),
                    text=stripped,
                )
            )
    return findings


def run_check(paths: List[Path]) -> ReferenceReport:
    report = ReferenceReport()
    for p in paths:
        if not p.exists():
            report.errors.append(f"path not found: {p}")
            continue
        files: List[Path]
        if p.is_dir():
            files = sorted(p.rglob("*.yml")) + sorted(p.rglob("*.yaml"))
        else:
            files = [p]
        for f in files:
            report.files_scanned += 1
            try:
                report.findings.extend(scan_file(f))
            except RuntimeError as e:
                report.errors.append(str(e))
    return report


def print_report(report: ReferenceReport) -> None:
    print(f"# Stage 5 Cycle 2 — workflow secrets reference check")
    print(f"# files_scanned = {report.files_scanned}")
    print(f"# violations = {report.violations}")
    by_ctx = report.by_context()
    for ctx in sorted(by_ctx):
        print(f"# context[{ctx}] = {by_ctx[ctx]}")
    for f in report.findings:
        print(
            f"  [FAIL] {f.file}:{f.line} context={f.context} "
            f"name={f.secret_name or '-'} :: {f.text}"
        )
    for e in report.errors:
        print(f"  [ERROR] {e}", file=sys.stderr)


def list_checks() -> None:
    print("Stage 5 Cycle 2 — workflow secrets reference check tool")
    print("")
    print("Checks:")
    print("  5.2 secrets.* 참조 감지 (context 분류 — env / with / run / if + secrets-block)")
    print(f"    - interpolation pattern: /{SECRETS_INTERP_PATTERN.pattern}/")
    print(f"    - bare pattern (if expression): /{SECRETS_BARE_PATTERN.pattern}/")
    print(f"    - block header pattern: /{SECRETS_BLOCK_PATTERN.pattern}/")
    print(f"    - tracked context keys: {sorted(CONTEXT_KEYS)}")
    print("")
    print("Exit codes:")
    print("  0 = PASS (violations=0)")
    print("  1 = FAIL (violations>=1)")
    print("  2 = input error (path 부재 / 읽기 실패)")
    print("")
    print("Out of scope (본 도구가 하지 않는 것):")
    print("  - 실 secret value 검사 (식별자 검사 한정)")
    print("  - permissions / fork PR policy / GITHUB_TOKEN 권한 (Cycle 3/4 영역)")
    print("  - YAML 완전 schema validation (indent-based 분류 한정)")
    print("  - 실 GitHub API 호출 0건")


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Stage 5 Cycle 2 — workflow secrets.* 참조 감지 (context 분류, 정적)",
    )
    parser.add_argument("paths", nargs="*", help="workflow YAML 파일 또는 디렉토리 (1+ 개)")
    parser.add_argument("--list-checks", action="store_true", help="검사 항목 self-check 출력")
    args = parser.parse_args(argv)

    if args.list_checks:
        list_checks()
        return 0

    if not args.paths:
        parser.error("workflow YAML 파일 또는 디렉토리 1개 이상 지정")

    paths = [Path(p) for p in args.paths]
    report = run_check(paths)
    print_report(report)

    if report.errors:
        for e in report.errors:
            print(f"::error::{e}", file=sys.stderr)
        return 2
    if report.files_scanned == 0:
        print("::error::no YAML files scanned", file=sys.stderr)
        return 2
    return 1 if report.violations > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
