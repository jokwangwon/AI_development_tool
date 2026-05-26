#!/usr/bin/env python3
# Stage 5 Cycle 1 — 5.1 GitHub Actions secrets 사용 0건 검증 도구
#
# 답습 출처:
#   - docs/review/3plus1-consensus-2026-05-13-stage5-g3-7-implementation-entry.md §1.4 + §3
#   - docs/phase0/backlog6-implementation-step-brief.md §2.2.5 (Stage 5 G3-7 영역)
#   - tools/mvp1_pc3_ar1_integration_check.py (Stage 4 도구 답습 — stdlib + dataclasses + argparse 패턴)
#   - tools/provider_url_scanner.py (URL/model scanner — regex + Path 답습)
#
# 본 도구는 *Stage 5 Cycle 1 정적 검증* 한정:
#   - 모든 입력 workflow YAML 에 GitHub Actions secrets 사용 0건 검증
#   - 검출 대상 = ``${{ secrets.* }}`` 표현식 + ``secrets:`` block (reusable workflow input)
#
# 본 도구가 *하지 않는* 것:
#   - 실 GitHub Actions secret 호출 / repo settings API 호출 0건
#   - secret 값 자체 검사 0건 (식별자 검사 한정)
#   - secrets.* 의 context 분류 (env/with/run/if 별도 — Cycle 2 영역)
#   - permissions / fork PR policy / GITHUB_TOKEN 권한 검사 (Cycle 3/4 영역)
#   - workflow YAML 완전 schema validation (구조 검증 한정)
#
# stdlib 전용 (re + dataclasses + sys + argparse + pathlib) — 외부 의존성 0건.
#
# 종료 코드:
#   0 = 위반 0건 (PASS — secrets 사용 0건)
#   1 = ≥1 위반 검출 (FAIL)
#   2 = 입력 오류 (path 부재 / 파일 읽기 실패)

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional

# ``${{ secrets.<NAME> }}`` interpolation pattern.
# - ``\$\{\{`` opening interpolation (literal)
# - ``\s*secrets\.`` secrets context access
# - ``[A-Za-z_][A-Za-z0-9_]*`` GitHub Actions secret name grammar
# - ``\s*\}\}`` closing
# 참고: `${{ env.SECRETS }}` 같은 false positive 회피 — `secrets.` (literal) 만 검출.
SECRETS_INTERP_PATTERN = re.compile(
    r"\$\{\{\s*secrets\.([A-Za-z_][A-Za-z0-9_]*)\s*\}\}"
)

# ``secrets:`` top-level / reusable workflow block.
# - line 시작 들여쓰기 허용
# - inline value 가 없는 block header 한정 (e.g., ``secrets:`` or ``secrets: inherit``)
SECRETS_BLOCK_PATTERN = re.compile(
    r"^(\s*)secrets\s*:\s*(.*)$"
)


@dataclass
class Finding:
    file: Path
    line: int
    kind: str  # "interpolation" or "block"
    text: str
    secret_name: str = ""


@dataclass
class UsageReport:
    files_scanned: int = 0
    findings: List[Finding] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)

    @property
    def violations(self) -> int:
        return len(self.findings)


def scan_file(path: Path) -> List[Finding]:
    """단일 workflow YAML 파일 line-by-line 정적 스캔."""
    findings: List[Finding] = []
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as e:
        raise RuntimeError(f"read failed: {path}: {e}") from e

    for lineno, line in enumerate(text.splitlines(), start=1):
        # 1) ``${{ secrets.NAME }}`` interpolation
        for m in SECRETS_INTERP_PATTERN.finditer(line):
            findings.append(
                Finding(
                    file=path,
                    line=lineno,
                    kind="interpolation",
                    text=line.strip(),
                    secret_name=m.group(1),
                )
            )
        # 2) ``secrets:`` block header — reusable workflow secrets input
        m = SECRETS_BLOCK_PATTERN.match(line)
        if m:
            # 본 검출은 `on:` 또는 `jobs.<id>.with:` / `jobs.<id>.secrets:` block 모두 cover.
            # 단, comment 영역 (`#`) 또는 YAML key 안의 `secrets:` 문자열은 제외 (line.lstrip().startswith)
            stripped = line.lstrip()
            if stripped.startswith("#"):
                continue
            findings.append(
                Finding(
                    file=path,
                    line=lineno,
                    kind="block",
                    text=line.strip(),
                    secret_name="",
                )
            )
    return findings


def run_check(paths: List[Path]) -> UsageReport:
    report = UsageReport()
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


def print_report(report: UsageReport) -> None:
    print(f"# Stage 5 Cycle 1 — workflow secrets usage check")
    print(f"# files_scanned = {report.files_scanned}")
    print(f"# violations = {report.violations}")
    for f in report.findings:
        print(
            f"  [FAIL] {f.file}:{f.line} kind={f.kind} "
            f"name={f.secret_name or '-'} :: {f.text}"
        )
    for e in report.errors:
        print(f"  [ERROR] {e}", file=sys.stderr)


def list_checks() -> None:
    print("Stage 5 Cycle 1 — workflow secrets usage check tool")
    print("")
    print("Checks:")
    print("  5.1 GitHub Actions secrets 사용 0건 검증")
    print(f"    - interpolation pattern: /{SECRETS_INTERP_PATTERN.pattern}/")
    print(f"    - block header pattern: /{SECRETS_BLOCK_PATTERN.pattern}/m")
    print("")
    print("Exit codes:")
    print("  0 = PASS (violations=0)")
    print("  1 = FAIL (violations>=1)")
    print("  2 = input error (path 부재 / 읽기 실패)")
    print("")
    print("Out of scope (본 도구가 하지 않는 것):")
    print("  - 실 secret value 검사 (식별자 검사 한정)")
    print("  - secrets.* 의 context 분류 (Cycle 2 영역)")
    print("  - permissions / fork PR policy / GITHUB_TOKEN 권한 (Cycle 3/4 영역)")
    print("  - 실 GitHub API 호출 0건")


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Stage 5 Cycle 1 — workflow secrets usage 0건 검증 (정적)",
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
