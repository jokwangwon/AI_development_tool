#!/usr/bin/env python3
# Stage 5 Cycle 3 — 5.3 fork PR secret 접근 차단 default 정책 검증 도구
#
# 답습 출처:
#   - docs/review/3plus1-consensus-2026-05-13-stage5-g3-7-implementation-entry.md §1.4 + §3
#   - docs/phase0/backlog6-implementation-step-brief.md §2.2.5 (Stage 5 G3-7 영역)
#   - tools/workflow_secrets_usage_check.py / workflow_secrets_reference_check.py (Cycle 1/2 답습)
#
# 검출 대상 (fork PR secret 접근 위험 trigger):
#   - ``pull_request_target`` — fork PR 가 repo secrets 권한으로 실행 (HIGH RISK)
#   - ``workflow_run`` — 다른 workflow 실행 후 repo secrets 권한으로 실행
#     (fork PR 의 run 이 trigger 가능 — 간접적 secret 노출 위험)
#
# 본 도구가 *하지 않는* 것:
#   - 실 GitHub repo settings API 호출 0건
#   - 실 fork PR 발사 / branch protection rule 검사 (T3 영역 — AR-2 / Backlog #3 분리)
#   - secrets 사용 자체 검출 (Cycle 1/2 영역)
#   - permissions 검사 (Cycle 4 영역)
#   - workflow_run / pull_request_target 의 *적격 사용* 분류 (단순 부재 검증 한정 —
#     적격 사용 시 별도 합의 영역, 본 도구 범위 외)
#
# stdlib 전용 (re + dataclasses + sys + argparse + pathlib) — 외부 의존성 0건.
#
# 종료 코드:
#   0 = 위반 0건 (PASS — 위험 trigger 0건)
#   1 = ≥1 위반 검출 (FAIL — pull_request_target 또는 workflow_run 검출)
#   2 = 입력 오류 (path 부재 / 파일 읽기 실패)

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional

# 위험 trigger 식별 (top-level ``on:`` block 또는 list/map child 한정).
RISKY_TRIGGERS = ("pull_request_target", "workflow_run")

# ``on:`` block 시작 검출 (top-level key, indent 0).
ON_HEADER_PATTERN = re.compile(r"^on\s*:\s*(.*)$")
# Trigger 식별 (list item ``- xxx`` 또는 map key ``xxx:``).
LIST_ITEM_PATTERN = re.compile(r"^(\s*)-\s+(\S+)\s*$")
MAP_KEY_PATTERN = re.compile(r"^(\s*)([A-Za-z_][\w-]*)\s*:\s*(.*)$")


@dataclass
class Finding:
    file: Path
    line: int
    trigger: str
    risk: str  # "HIGH" (pull_request_target) or "MEDIUM" (workflow_run)
    text: str


@dataclass
class PolicyReport:
    files_scanned: int = 0
    findings: List[Finding] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)

    @property
    def violations(self) -> int:
        return len(self.findings)


def _risk_level(trigger: str) -> str:
    if trigger == "pull_request_target":
        return "HIGH"
    if trigger == "workflow_run":
        return "MEDIUM"
    return "UNKNOWN"


def scan_file(path: Path) -> List[Finding]:
    """단일 workflow YAML 파일 ``on:`` block 파싱 + 위험 trigger 검출."""
    findings: List[Finding] = []
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as e:
        raise RuntimeError(f"read failed: {path}: {e}") from e

    lines = text.splitlines()
    in_on_block = False
    on_indent = -1

    for lineno, raw_line in enumerate(lines, start=1):
        stripped = raw_line.lstrip()
        if not stripped or stripped.startswith("#"):
            continue
        current_indent = len(raw_line) - len(stripped)

        # ``on:`` block 종료 — current_indent <= on_indent 가 도달하면 block 종료.
        if in_on_block and current_indent <= on_indent and lineno > 1:
            # 본 line 이 더 얕은 indent 이거나 top-level key 면 on block 종료.
            if current_indent == 0 and ":" in stripped:
                in_on_block = False
                on_indent = -1
            elif current_indent < on_indent + 2:
                # children 보다 얕은 indent (= map key 가 아닌 sibling) → on block 종료
                # 본 분기 = 들여쓰기 2-space 표준 가정 (workflow 파일 답습)
                pass

        # ``on:`` 시작 검출 (top-level, indent=0).
        if current_indent == 0:
            m_on = ON_HEADER_PATTERN.match(raw_line)
            if m_on:
                inline = m_on.group(1).strip()
                # ``on: <trigger>`` (single inline trigger) 형태 검출.
                if inline:
                    # ``on: [push, pull_request]`` 또는 ``on: push`` 형태
                    # remove brackets and split
                    inline_clean = inline.strip("[]").strip()
                    items = [x.strip() for x in inline_clean.split(",") if x.strip()]
                    for it in items:
                        if it in RISKY_TRIGGERS:
                            findings.append(
                                Finding(
                                    file=path,
                                    line=lineno,
                                    trigger=it,
                                    risk=_risk_level(it),
                                    text=stripped,
                                )
                            )
                in_on_block = True
                on_indent = 0
                continue
            # ``on:`` 외 다른 top-level key 면 on block 종료.
            if in_on_block:
                in_on_block = False
                on_indent = -1

        if in_on_block:
            # ``- trigger`` (list item) 형태.
            m_list = LIST_ITEM_PATTERN.match(raw_line)
            if m_list:
                trig = m_list.group(2)
                if trig in RISKY_TRIGGERS:
                    findings.append(
                        Finding(
                            file=path,
                            line=lineno,
                            trigger=trig,
                            risk=_risk_level(trig),
                            text=stripped,
                        )
                    )
                continue
            # ``trigger:`` (map key) 형태 — but skip nested keys (only direct children of ``on:``).
            m_key = MAP_KEY_PATTERN.match(raw_line)
            if m_key and current_indent <= 2:
                # direct child of ``on:`` (2-space indent 가정)
                key = m_key.group(2)
                if key in RISKY_TRIGGERS:
                    findings.append(
                        Finding(
                            file=path,
                            line=lineno,
                            trigger=key,
                            risk=_risk_level(key),
                            text=stripped,
                        )
                    )

    return findings


def run_check(paths: List[Path]) -> PolicyReport:
    report = PolicyReport()
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


def print_report(report: PolicyReport) -> None:
    print(f"# Stage 5 Cycle 3 — workflow fork PR secret policy check")
    print(f"# files_scanned = {report.files_scanned}")
    print(f"# violations = {report.violations}")
    for f in report.findings:
        print(
            f"  [FAIL] {f.file}:{f.line} risk={f.risk} trigger={f.trigger} "
            f":: {f.text}"
        )
    for e in report.errors:
        print(f"  [ERROR] {e}", file=sys.stderr)


def list_checks() -> None:
    print("Stage 5 Cycle 3 — workflow fork PR secret policy check tool")
    print("")
    print("Checks:")
    print("  5.3 fork PR secret 접근 차단 default 정책 검증")
    print(f"    - 위험 trigger 목록: {list(RISKY_TRIGGERS)}")
    print("        HIGH: pull_request_target (fork PR 가 repo secrets 권한으로 실행)")
    print("        MEDIUM: workflow_run (다른 workflow 실행 후 repo secrets 권한 — fork 간접 노출)")
    print("    - 검출 영역: top-level ``on:`` block (list / map / inline)")
    print("")
    print("Exit codes:")
    print("  0 = PASS (violations=0)")
    print("  1 = FAIL (violations>=1)")
    print("  2 = input error (path 부재 / 읽기 실패)")
    print("")
    print("Out of scope (본 도구가 하지 않는 것):")
    print("  - 실 GitHub repo settings API 호출 0건")
    print("  - branch protection rule 검사 (T3 — AR-2 / Backlog #3 분리)")
    print("  - secrets 사용 자체 검출 (Cycle 1/2 영역)")
    print("  - permissions 검사 (Cycle 4 영역)")
    print("  - 위험 trigger 의 *적격 사용* 분류 (단순 부재 검증 한정)")


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Stage 5 Cycle 3 — fork PR secret 접근 차단 default 정책 검증 (정적)",
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
