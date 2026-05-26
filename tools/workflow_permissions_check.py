#!/usr/bin/env python3
# Stage 5 Cycle 4 — 5.4 workflow permissions: contents: read 검증 도구
#
# 답습 출처:
#   - docs/review/3plus1-consensus-2026-05-13-stage5-g3-7-implementation-entry.md §1.4 + §3
#   - docs/phase0/backlog6-implementation-step-brief.md §2.2.5 (Stage 5 G3-7 영역)
#   - tools/workflow_secrets_usage_check.py / workflow_secrets_reference_check.py /
#     workflow_fork_pr_secret_policy_check.py (Cycle 1/2/3 답습)
#
# 검증 대상 (정적 분석):
#   - top-level ``permissions:`` block 존재 여부
#   - block 내 ``contents: read`` (또는 ``read-all``) 포함 여부
#   - 미포함 시: ``contents: write`` 또는 다른 broader 권한 검출
#   - top-level 부재 시: job-level ``permissions:`` block fallback 검사 (정보 한정)
#
# 본 도구가 *하지 않는* 것:
#   - 실 GitHub repo settings API 호출 0건
#   - permissions 정책 *변경* / 자동 fix 0건 (사용자 명시 답습 — provider-adapter-enforcement.yml 사전 fix 금지)
#   - 다른 permission key (actions / packages / id-token 등) 확장 검사 (단순 contents: read 기준)
#   - workflow_call / reusable workflow 호출 chain 검사 (out of scope)
#   - secrets / fork PR / trigger 검사 (Cycle 1/2/3 영역)
#
# stdlib 전용 (re + dataclasses + sys + argparse + pathlib) — 외부 의존성 0건.
#
# 종료 코드:
#   0 = 위반 0건 (PASS — 모든 workflow 가 top-level contents: read 보유)
#   1 = ≥1 위반 검출 (FAIL — top-level permissions 부재 또는 비호환 권한)
#   2 = 입력 오류 (path 부재 / 파일 읽기 실패)

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional, Tuple

# top-level ``permissions:`` (indent=0).
TOP_PERMISSIONS_PATTERN = re.compile(r"^permissions\s*:\s*(.*)$")
# job-level / nested ``permissions:`` (indent>=2).
NESTED_PERMISSIONS_PATTERN = re.compile(r"^(\s+)permissions\s*:\s*(.*)$")
# ``contents: <value>`` (any indent).
CONTENTS_KEY_PATTERN = re.compile(r"^(\s*)contents\s*:\s*([A-Za-z_-]+)\s*$")
# ``read-all`` inline value.
READ_ALL_INLINE = re.compile(r"^read-all\s*$")


@dataclass
class PermissionsState:
    file: Path
    top_level_present: bool = False
    top_level_inline: str = ""
    top_level_indent: int = -1
    top_level_block_lines: List[Tuple[int, str]] = field(default_factory=list)
    contents_value: Optional[str] = None  # top-level contents 값
    nested_permissions_count: int = 0


@dataclass
class Finding:
    file: Path
    line: int
    rule: str
    detail: str


@dataclass
class PermissionsReport:
    files_scanned: int = 0
    findings: List[Finding] = field(default_factory=list)
    states: List[PermissionsState] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)

    @property
    def violations(self) -> int:
        return len(self.findings)

    @property
    def files_with_violations(self) -> List[Path]:
        seen = []
        for f in self.findings:
            if f.file not in seen:
                seen.append(f.file)
        return seen


def _parse_state(path: Path) -> PermissionsState:
    state = PermissionsState(file=path)
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    in_top_block = False
    top_indent = -1
    top_start_line = -1

    for lineno, raw_line in enumerate(lines, start=1):
        stripped = raw_line.lstrip()
        if not stripped or stripped.startswith("#"):
            continue
        current_indent = len(raw_line) - len(stripped)

        if current_indent == 0:
            m = TOP_PERMISSIONS_PATTERN.match(raw_line)
            if m:
                state.top_level_present = True
                state.top_level_inline = m.group(1).strip()
                state.top_level_indent = 0
                top_start_line = lineno
                in_top_block = True
                top_indent = 0
                # inline value (예: ``permissions: read-all``)
                if state.top_level_inline:
                    if READ_ALL_INLINE.match(state.top_level_inline):
                        state.contents_value = "read-all"
                    elif state.top_level_inline.startswith("{}"):
                        state.contents_value = "{}"  # 빈 권한 (no access)
                continue

            # top-level ``permissions`` 외 다른 top-level key 발견 → top block 종료
            if in_top_block:
                in_top_block = False
                top_indent = -1

        if in_top_block and current_indent > 0:
            # child of permissions: — ``contents: <value>`` 검출
            state.top_level_block_lines.append((lineno, raw_line))
            m_contents = CONTENTS_KEY_PATTERN.match(raw_line)
            if m_contents and state.contents_value is None:
                state.contents_value = m_contents.group(2)
        else:
            # nested permissions count (job-level fallback 검사용)
            m_nested = NESTED_PERMISSIONS_PATTERN.match(raw_line)
            if m_nested:
                state.nested_permissions_count += 1
    return state


def evaluate(state: PermissionsState) -> List[Finding]:
    findings: List[Finding] = []

    if not state.top_level_present:
        findings.append(
            Finding(
                file=state.file,
                line=1,
                rule="permissions-missing",
                detail=(
                    f"top-level permissions: block 부재 "
                    f"(job-level fallback count = {state.nested_permissions_count}; "
                    f"본 도구 = top-level 기준 strict)"
                ),
            )
        )
        return findings

    # top-level 존재 — contents: 값 검증
    value = state.contents_value
    if value is None:
        findings.append(
            Finding(
                file=state.file,
                line=1,
                rule="permissions-contents-missing",
                detail=(
                    f"top-level permissions: 존재하지만 contents: 키 부재 "
                    f"(inline='{state.top_level_inline}', child_lines={len(state.top_level_block_lines)})"
                ),
            )
        )
        return findings

    # 허용 값: read, read-all, {} (empty = no access)
    if value in ("read", "read-all", "{}"):
        return findings

    # write / admin / 기타 broader → FAIL
    findings.append(
        Finding(
            file=state.file,
            line=1,
            rule="permissions-contents-broader",
            detail=(
                f"top-level contents: '{value}' (허용: read / read-all / {{}}). "
                f"contents: read 기준 초과"
            ),
        )
    )
    return findings


def run_check(paths: List[Path]) -> PermissionsReport:
    report = PermissionsReport()
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
                state = _parse_state(f)
            except OSError as e:
                report.errors.append(f"read failed: {f}: {e}")
                continue
            report.states.append(state)
            report.findings.extend(evaluate(state))
    return report


def print_report(report: PermissionsReport) -> None:
    print(f"# Stage 5 Cycle 4 — workflow permissions: contents: read check")
    print(f"# files_scanned = {report.files_scanned}")
    print(f"# violations = {report.violations}")
    print(f"# files_with_violations = {len(report.files_with_violations)}")
    for state in report.states:
        marker = "PASS" if state.contents_value in ("read", "read-all", "{}") else (
            "FAIL" if state.top_level_present else "MISSING"
        )
        print(
            f"  [{marker}] {state.file} top_level={state.top_level_present} "
            f"contents={state.contents_value or '-'} nested_jobs={state.nested_permissions_count}"
        )
    for f in report.findings:
        print(f"  [FAIL] {f.file}:{f.line} rule={f.rule} :: {f.detail}")
    for e in report.errors:
        print(f"  [ERROR] {e}", file=sys.stderr)


def list_checks() -> None:
    print("Stage 5 Cycle 4 — workflow permissions: contents: read check tool")
    print("")
    print("Checks:")
    print("  5.4 workflow top-level permissions 가 contents: read 기준 충족 여부")
    print("    - top-level permissions: block 존재 의무")
    print("    - 허용 값: contents: read / permissions: read-all / permissions: {}")
    print("    - 비허용 값: contents: write / admin / 기타 broader → FAIL")
    print("    - top-level 부재: 위반 검출 (job-level fallback 정보 한정)")
    print("")
    print("Exit codes:")
    print("  0 = PASS (violations=0)")
    print("  1 = FAIL (violations>=1)")
    print("  2 = input error (path 부재 / 읽기 실패)")
    print("")
    print("Out of scope (본 도구가 하지 않는 것):")
    print("  - permissions 정책 변경 / 자동 fix 0건 (사용자 명시 답습)")
    print("  - 다른 permission key (actions/packages/id-token) 확장 검사")
    print("  - reusable workflow 호출 chain 검사")
    print("  - 실 GitHub API 호출 0건")
    print("  - secrets / fork PR / trigger 검사 (Cycle 1/2/3 영역)")


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Stage 5 Cycle 4 — workflow top-level permissions: contents: read 검증 (정적)",
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
