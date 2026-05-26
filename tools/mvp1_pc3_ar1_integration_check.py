#!/usr/bin/env python3
# Stage 4 — PC-3 (CI-only enforcement) + AR-1 (CI step fail-closed) 통합 검증 도구
#
# 답습 출처:
#   - docs/phase0/backlog6-implementation-step-brief.md §2.2.4 (Stage 4 sub-step 4.1 + 4.2)
#   - docs/architecture/implementation-runtime-roadmap-mvp1.md §4.3 + §4.4
#   - docs/review/3plus1-consensus-2026-05-12-backlog6-implementation-entry.md §1.1 + §1.2
#   - docs/review/3plus1-consensus-2026-05-12-stage4-pc3-ar1-implementation-entry.md
#
# 본 도구는 *Stage 4 정적 통합 검증* 한정:
#   - PC-3: MVP-1 entry / Stage 2 step 에 `continue-on-error: true` 적용 0건 검증
#   - AR-1: MVP-1 entry / Stage 2 step body 에 `exit 1` fail-closed 패턴 존재 검증
#
# Stage 1/3 의 기존 entry step + Stage 2 의 추가 step 답습 변경 0건 — 정적 분석만.
#
# stdlib 전용 (re + dataclasses + sys + argparse) — pyyaml 미사용 (다른 tools/ 와 답습 일관).
#
# 본 도구가 *하지 않는* 것:
#   - 실 workflow 실행 (GitHub Actions 실행 미진입)
#   - branch protection rule API 호출 (AR-2 = T3 영역 분리)
#   - local pre-commit hook 검증 (PC-4 = Backlog #1+#2 분리)
#   - workflow YAML 의 완전 schema validation (구조 검증 한정)
#   - scanner tool 본문 변경 (답습 변경 0건 보존)

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional

# Entry step 식별 규칙 (브리프 §2.2.4 답습)
#  - Stage 1 + Stage 3 MVP-1 entry step: name 에 "MVP-1 entry" 포함
#  - Stage 2 / Stage 4 / Stage 5 추가 step: name 이 "Stage N" 로 시작 (괄호 + 설명 허용)
ENTRY_NAME_PATTERNS: List[re.Pattern] = [
    re.compile(r"MVP-1\s*entry", re.IGNORECASE),
    re.compile(r"^Stage\s*\d+\b", re.IGNORECASE),
]

PC3_VIOLATION_PATTERN = re.compile(r"^\s*continue-on-error\s*:\s*true\s*$", re.IGNORECASE)
# AR-1 fail-closed = 명시적 `exit 1` 또는 `set -e` (shell propagation, 외부 script 의 exit code 가 step rc 로 전파).
# 둘 중 하나만 있어도 PR check failure 의무 답습 (Stage 2 docker_secret_*.sh 패턴).
AR1_EXIT_PATTERN = re.compile(r"\bexit\s+1\b")
AR1_SET_E_PATTERN = re.compile(r"^\s*set\s+-e(?:\s|$)", re.MULTILINE)
STEP_HEAD_PATTERN = re.compile(r"^(\s*)-\s+name:\s*(.+)$")


@dataclass
class StepBlock:
    file: Path
    line_start: int
    line_end: int
    name: str
    body: str  # 전체 step block 텍스트


@dataclass
class CheckResult:
    file: Path
    step_name: str
    rule: str  # "PC-3" or "AR-1"
    status: str  # "PASS" or "FAIL"
    detail: str = ""

    def is_violation(self) -> bool:
        return self.status == "FAIL"


@dataclass
class IntegrationReport:
    entry_steps_total: int = 0
    pc3_results: List[CheckResult] = field(default_factory=list)
    ar1_results: List[CheckResult] = field(default_factory=list)

    @property
    def violations(self) -> List[CheckResult]:
        return [r for r in (self.pc3_results + self.ar1_results) if r.is_violation()]


def extract_steps(file: Path) -> List[StepBlock]:
    """GitHub Actions workflow YAML 에서 ``- name: ...`` step 블록 추출.

    YAML 전체 파서가 아니라 들여쓰기 + 'name:' 기반 휴리스틱.
    workflow step 정의 형식 (들여쓰기 일관) 답습.
    """
    if not file.exists():
        return []
    text = file.read_text(encoding="utf-8")
    lines = text.splitlines()
    steps: List[StepBlock] = []
    n = len(lines)
    i = 0
    while i < n:
        m = STEP_HEAD_PATTERN.match(lines[i])
        if not m:
            i += 1
            continue
        indent = len(m.group(1))
        name = m.group(2).strip().strip('"').strip("'")
        start = i
        j = i + 1
        # step body = 다음 동일 또는 더 얕은 indent 의 `- name:` 또는 다른 top-level key 까지
        while j < n:
            line = lines[j]
            if not line.strip():
                j += 1
                continue
            current_indent = len(line) - len(line.lstrip())
            stripped = line.lstrip()
            if current_indent <= indent and (
                stripped.startswith("- name:") or (stripped.endswith(":") and ":" in stripped and not stripped.startswith("#"))
            ):
                # 동일/얕은 indent + 새 step head OR top-level key → 본 step 종료
                break
            j += 1
        body = "\n".join(lines[start:j])
        steps.append(StepBlock(file=file, line_start=start + 1, line_end=j, name=name, body=body))
        i = j
    return steps


def is_entry_step(step: StepBlock) -> bool:
    return any(p.search(step.name) for p in ENTRY_NAME_PATTERNS)


def check_pc3(step: StepBlock) -> CheckResult:
    """PC-3: entry step 에 `continue-on-error: true` 적용 0건."""
    for line in step.body.splitlines():
        if PC3_VIOLATION_PATTERN.match(line):
            return CheckResult(
                file=step.file,
                step_name=step.name,
                rule="PC-3",
                status="FAIL",
                detail=f"`continue-on-error: true` found on entry step (CI-only enforcement broken)",
            )
    return CheckResult(file=step.file, step_name=step.name, rule="PC-3", status="PASS")


def _strip_comments(body: str) -> str:
    """shell `#` 주석 제거 — `# exit 1` 와 같은 텍스트 false positive 회피.

    문자열 내 `#` 보존 (큰따옴표 / 작은따옴표 안 # 은 검출 한정 단순화 — # 의 시작 위치만 보아 line cut).
    """
    out_lines: List[str] = []
    for line in body.splitlines():
        stripped = line.lstrip()
        # YAML key (예: id:, run:) 의 콜론 뒤 # 는 보존 — 본 휴리스틱 = run: block 의 shell 라인 한정
        # shell line 의 leading `#` 또는 `<공백> #` 부분만 cut
        if stripped.startswith("#"):
            continue
        # inline comment (` # ...`)
        idx = -1
        in_single = False
        in_double = False
        for k, ch in enumerate(line):
            if ch == "'" and not in_double:
                in_single = not in_single
            elif ch == '"' and not in_single:
                in_double = not in_double
            elif ch == "#" and not in_single and not in_double:
                # leading whitespace 다음 # 만 cut (column ≥ 1 AND preceding char = whitespace)
                if k > 0 and line[k - 1].isspace():
                    idx = k
                    break
        if idx > 0:
            line = line[:idx].rstrip()
        out_lines.append(line)
    return "\n".join(out_lines)


def check_ar1(step: StepBlock) -> CheckResult:
    """AR-1: entry step body 에 fail-closed 패턴 존재.

    인정 패턴 (둘 중 하나):
      - 명시적 ``exit 1`` (직접 차단)
      - ``set -e`` (외부 script / subprocess exit code propagation)

    Shell `#` 주석은 사전 제거 → 주석 내 텍스트 false positive 회피.
    """
    body_no_comments = _strip_comments(step.body)
    has_exit = bool(AR1_EXIT_PATTERN.search(body_no_comments))
    has_set_e = bool(AR1_SET_E_PATTERN.search(body_no_comments))
    if has_exit or has_set_e:
        detail = []
        if has_exit:
            detail.append("explicit exit 1")
        if has_set_e:
            detail.append("set -e (shell propagation)")
        return CheckResult(
            file=step.file,
            step_name=step.name,
            rule="AR-1",
            status="PASS",
            detail=" + ".join(detail),
        )
    return CheckResult(
        file=step.file,
        step_name=step.name,
        rule="AR-1",
        status="FAIL",
        detail="entry step missing fail-closed pattern (no `exit 1` and no `set -e`)",
    )


def run_checks(files: List[Path], mode: str) -> IntegrationReport:
    report = IntegrationReport()
    for f in files:
        steps = extract_steps(f)
        entry_steps = [s for s in steps if is_entry_step(s)]
        report.entry_steps_total += len(entry_steps)
        for s in entry_steps:
            if mode in ("pc3", "integration"):
                report.pc3_results.append(check_pc3(s))
            if mode in ("ar1", "integration"):
                report.ar1_results.append(check_ar1(s))
    return report


def print_report(report: IntegrationReport, mode: str) -> None:
    print(f"# Stage 4 — PC-3 + AR-1 integration check (mode={mode})")
    print(f"# entry_steps_total = {report.entry_steps_total}")
    if mode in ("pc3", "integration"):
        print(f"# PC-3 results ({len(report.pc3_results)} entry steps):")
        for r in report.pc3_results:
            line = f"  [{r.status}] {r.rule} {r.file.name}: {r.step_name}"
            if r.detail:
                line += f" — {r.detail}"
            print(line)
    if mode in ("ar1", "integration"):
        print(f"# AR-1 results ({len(report.ar1_results)} entry steps):")
        for r in report.ar1_results:
            line = f"  [{r.status}] {r.rule} {r.file.name}: {r.step_name}"
            if r.detail:
                line += f" — {r.detail}"
            print(line)
    print(f"# violations = {len(report.violations)}")


def list_checks() -> None:
    print("Stage 4 — PC-3 + AR-1 integration check tool")
    print("")
    print("Checks:")
    print("  PC-3 (CI-only enforcement): no `continue-on-error: true` on entry steps")
    print("  AR-1 (CI step fail-closed): entry step body contains `exit 1` pattern")
    print("")
    print("Entry step identification (brief §2.2.4 답습):")
    for p in ENTRY_NAME_PATTERNS:
        print(f"  - name 패턴: /{p.pattern}/{'i' if p.flags & re.IGNORECASE else ''}")
    print("")
    print("Out of scope (본 도구가 하지 않는 것):")
    print("  - 실 workflow 실행 미진입")
    print("  - branch protection rule API 호출 (AR-2 = T3 영역 분리)")
    print("  - local pre-commit hook 검증 (PC-4 = Backlog #1+#2 분리)")
    print("  - scanner tool 본문 변경 (답습 변경 0건 보존)")
    print("  - workflow YAML 완전 schema validation (구조 검증 한정)")


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Stage 4 PC-3 + AR-1 통합 정적 검증 도구 (CI-only enforcement + fail-closed)",
    )
    parser.add_argument("files", nargs="*", help="workflow YAML 파일 경로 (1+ 개)")
    parser.add_argument(
        "--mode",
        choices=["pc3", "ar1", "integration"],
        default="integration",
        help="검사 모드 (default: integration)",
    )
    parser.add_argument("--list-checks", action="store_true", help="검사 항목 self-check 출력")
    args = parser.parse_args(argv)

    if args.list_checks:
        list_checks()
        return 0

    if not args.files:
        parser.error("workflow YAML 파일 경로를 1개 이상 지정 (예: .github/workflows/secret-hygiene-egress-redaction.yml)")

    paths = [Path(p) for p in args.files]
    missing = [p for p in paths if not p.exists()]
    if missing:
        for m in missing:
            print(f"::error::file not found: {m}", file=sys.stderr)
        return 1

    report = run_checks(paths, args.mode)
    print_report(report, args.mode)
    if report.entry_steps_total == 0:
        print("::error::no entry steps found — Stage 4 통합 검증 부적격 (Stage 1/2/3 PASS 선행 의무)", file=sys.stderr)
        return 1
    return 1 if report.violations else 0


if __name__ == "__main__":
    sys.exit(main())
