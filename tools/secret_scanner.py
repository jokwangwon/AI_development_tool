#!/usr/bin/env python3
"""Secret scanner — Group D PoC (G2 GP-3 Credential/Secret Hygiene + GP-2 Egress Redaction).

답습 출처:
  - docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md (본 PoC 사양)
  - docs/architecture/redaction-pattern-equivalence.md (R-4 — 패턴 동등성 카탈로그)
  - docs/phase0/r4-1-trigger-extension-evidence.md §4.1 (R-4.1 — Tier-1 42 catalog + baseline 5)
  - docker/r4-1-poc/r4_1_poc.py line 51~213 (Tier-1 42 patterns + baseline 5 직접 답습)
  - docs/architecture/governance-preconditions.md §4 (GP-2) + §5 (GP-3)
  - docs/decisions/ADR-011-means-vs-ends-redaction.md §2.1 (a)~(e)

핵심 강제 조건 (사용자 명시 답습):
  - R-4.1 Tier-1 42 catalog + baseline 5 = 45 patterns 직접 답습 (변경 0건)
  - Prefix 36 (baseline 5 + Tier-1 prefix 31) + 추가 regex 7 (H-A/B/C/E/F/G/K) + alternation 2 (H-J/H-L key 기반)
  - H-J / H-L 직접 등록 제외 (alternation 채택, R-4.1 §4.2 답습)
  - Tier-2 / Tier-3 catalog 확장 0건
  - 외부 의존성 0건 (custom scanner 단독, gitleaks/detect-secrets 미도입)

Mode (사용자 명시):
  --mode scan-source : code-side secret 검출 (D-1 GP-3 Credential/Secret Hygiene)
  --mode scan-log    : redaction 후 잔존 secret 검출 (D-2 GP-2 Egress Redaction)

  본 PoC = 형식적 검출 layer 한정. Hermes 컨테이너 chmod / inotify (R1-2) =
  Hermes upstream 영역, 본 PoC 미진입 (사용자 명시 #6).

종료 코드:
  0 = 위반 0건 (PASS)
  1 = ≥1 위반 검출 (FAIL — D-1 secret 검출 / D-2 잔존 leak 검출)
  2 = 입력 오류 (path 부재 등)

알려진 한계 (사용자 명시 — 사양 §8):
  - base64 / URL-encoded / 압축 등 advanced evasion 미커버 (Hermes upstream R2-6 영역)
"""
from __future__ import annotations

import argparse
import dataclasses
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

# SC-1 (65 entry, 합의 B-1 (ii)): Tier-1 catalog single source = src/adapters/llm/redaction_patterns.py
# (detection ↔ prevention drift 0). 본 scanner 는 `python3 tools/secret_scanner.py` 직접 실행 →
# sys.path[0]=tools/ 이므로 repo root 보강 후 import. 패턴 *내용* 변경 0건 (R-4.1 답습).
_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from src.adapters.llm.redaction_patterns import (  # noqa: E402
    ALL_PATTERNS,
    ALTERNATION_PATTERNS,
    BASELINE_PREFIX,
    COMPILED_PATTERNS,
    PREFIX_PATTERNS,
    REGEX_PATTERNS,
    SKIP_DIRECT_REGISTER,
)

# Tier-1 패턴 카탈로그 (45종) = src/adapters/llm/redaction_patterns.py (SC-1 B-1 (ii) single source).
# BASELINE_PREFIX(5) + PREFIX_PATTERNS(31) + REGEX_PATTERNS(7) + ALTERNATION_PATTERNS(2) = ALL_PATTERNS(45)
# + COMPILED_PATTERNS + SKIP_DIRECT_REGISTER 모두 위 import (line 상단) — 패턴 내용 변경 0 (R-4.1 답습).

# Redaction marker exclusion (scan-log mode 전용 — GP-2 D-2 contract 답습).
# 사양 §0 — D-2 = "redaction 후 잔존 secret 검증". 본 marker 가 매칭 substring 전체를
# 차지하면 *정상 redacted output* 로 분류, 위반 미카운트 (FP 회피).
REDACTION_MARKER_RE: re.Pattern[str] = re.compile(
    r"(?i)(\[REDACTED\]|\[FILTERED\]|\[MASKED\]|<REDACTED>|<MASKED>|<<masked>>|\*{5,})"
)

# Scan 대상 file extension (사양 §4.1~§4.2 답습)
#
# scope 정책 (49 entry 발효): docs/architecture/secret-scanner-scope-policy.md
#   - hook entry scope: src + .github 한정 (.pre-commit-config.yaml 답습)
#   - docs/ 영역 영구 금지 (~800+ 잠재 false positive 답습 — fake canary / redaction 예시 / codex 응답 sample)
#   - scope 확장 의무 절차: 정책 §2 답습 (별도 sub-cycle + 풀 3+1 + R-7(b) 차등)
#   - 본 SCAN_SOURCE_EXTENSIONS 변경 = catalog 본문 변경 = R-7(b) 차등 자격
SCAN_SOURCE_EXTENSIONS: tuple[str, ...] = (
    ".py", ".json", ".yaml", ".yml", ".toml", ".sh", ".bash",
    ".env", ".ini", ".cfg", ".pem", ".key", ".txt", ".md",
)
SCAN_LOG_EXTENSIONS: tuple[str, ...] = (".txt", ".log", ".json", ".jsonl", ".md", ".pem")


@dataclass(frozen=True)
class Violation:
    """Single secret detection."""

    file: Path
    line: int
    pattern_id: str
    pattern_source: str
    pattern_category: str
    pattern_vendor: str
    matched_text: str

    def format_short(self) -> str:
        # Truncate matched_text to avoid leaking full canary in CI log (defensive)
        sample = self.matched_text[:30] + ("..." if len(self.matched_text) > 30 else "")
        return (
            f"{self.file}:{self.line}:{self.pattern_id}:"
            f"{self.pattern_category}:{self.pattern_vendor}: {sample!r}"
        )


def is_redaction_marker_match(matched_text: str) -> bool:
    """Scan-log mode 한정 — 매칭 텍스트가 redaction marker 만 포함하면 정상 redacted (FP 회피).

    GP-2 D-2 contract — 'redaction 후 잔존 secret 검증' (사양 §0).
    예: `OPENAI_API_KEY=[REDACTED]` 의 H-A regex 매칭은 [REDACTED] marker → 위반 미카운트.
    """
    return REDACTION_MARKER_RE.search(matched_text) is not None


def scan_text(text: str, file_path: Path, mode: str | None = None) -> list[Violation]:
    """Apply all 45 patterns to text and return violations.

    Line number = 1-indexed (file::line 표기 답습).
    mode='scan-log' 시 redaction marker 매칭은 위반 미카운트 (FP 회피, 사양 §0).
    """
    vios: list[Violation] = []
    for pid, src, cat, vendor, pattern in COMPILED_PATTERNS:
        if pid in SKIP_DIRECT_REGISTER:
            continue
        for m in pattern.finditer(text):
            matched = m.group(0)
            if mode == "scan-log" and is_redaction_marker_match(matched):
                continue
            line_no = text[: m.start()].count("\n") + 1
            vios.append(
                Violation(
                    file=file_path,
                    line=line_no,
                    pattern_id=pid,
                    pattern_source=src,
                    pattern_category=cat,
                    pattern_vendor=vendor,
                    matched_text=matched,
                )
            )
    return vios


def iter_files(root: Path, allowed_exts: tuple[str, ...]) -> list[Path]:
    """Recursively iter target files under root, filtered by extension."""
    if root.is_file():
        return [root] if root.suffix in allowed_exts else []
    out: list[Path] = []
    for p in sorted(root.rglob("*")):
        if p.is_file() and p.suffix in allowed_exts:
            out.append(p)
    return out


def scan_path(root: Path, mode: str) -> list[Violation]:
    """Scan all matching files under root and return aggregated violations."""
    if mode == "scan-source":
        exts = SCAN_SOURCE_EXTENSIONS
    elif mode == "scan-log":
        exts = SCAN_LOG_EXTENSIONS
    else:
        raise ValueError(f"unknown mode: {mode!r}")

    vios: list[Violation] = []
    for file_path in iter_files(root, exts):
        try:
            text = file_path.read_text(encoding="utf-8", errors="replace")
        except OSError as e:
            print(f"READ_ERROR: {file_path}: {e}", file=sys.stderr)
            continue
        vios.extend(scan_text(text, file_path, mode=mode))
    return vios


def list_patterns() -> int:
    """Print Tier-1 catalog summary (사용자 명시 검증 5 — Tier-1 pattern count 자기 검증)."""
    n_baseline = len(BASELINE_PREFIX)
    n_prefix = len(PREFIX_PATTERNS)
    n_regex = len(REGEX_PATTERNS)
    n_alt = len(ALTERNATION_PATTERNS)
    total_registered = n_baseline + n_prefix + n_regex + n_alt
    n_active = total_registered - len(SKIP_DIRECT_REGISTER & {p[0] for p in ALL_PATTERNS})

    print(f"registered_patterns_count={total_registered}", file=sys.stderr)
    print(f"  baseline_prefix={n_baseline}", file=sys.stderr)
    print(f"  tier1_prefix={n_prefix}", file=sys.stderr)
    print(f"  tier1_regex={n_regex}", file=sys.stderr)
    print(f"  tier1_alternation={n_alt}", file=sys.stderr)
    print(f"  skip_direct_register={sorted(SKIP_DIRECT_REGISTER)}", file=sys.stderr)
    print(f"  active_patterns={n_active}", file=sys.stderr)
    print(
        f"  tier1_42_catalog_compliant={total_registered >= 42}", file=sys.stderr
    )

    for pid, src, cat, vendor, rgx in ALL_PATTERNS:
        flag = " (skipped)" if pid in SKIP_DIRECT_REGISTER else ""
        print(f"  {pid}\t{cat}\t{vendor}\t{src}{flag}", file=sys.stderr)

    return 0


def _cli() -> int:
    p = argparse.ArgumentParser(
        description="Secret scanner — Group D PoC (G2 GP-3 + GP-2, R-4.1 Tier-1 42 catalog 답습)"
    )
    p.add_argument(
        "path", type=str, nargs="?", default=None,
        help="대상 파일/디렉토리 경로 (재귀). --list-patterns 시 생략 가능."
    )
    p.add_argument(
        "--mode", choices=("scan-source", "scan-log"), default=None,
        help=(
            "scan-source = code-side secret 검출 (D-1). "
            "scan-log = redaction 후 잔존 secret 검출 (D-2)."
        ),
    )
    p.add_argument(
        "--list-patterns", action="store_true",
        help="등록된 45 patterns enumerate + Tier-1 42 catalog count 자기 검증",
    )
    p.add_argument(
        "--max-lines", type=int, default=20,
        help="violation 출력 최대 라인 수 (default 20, CI log 폭주 방지)",
    )
    args = p.parse_args()

    if args.list_patterns:
        return list_patterns()

    if not args.path or not args.mode:
        print("ERROR: path 와 --mode 필수 (--list-patterns 단독 모드 외)", file=sys.stderr)
        return 2

    root = Path(args.path)
    if not root.exists():
        print(f"PATH_NOT_FOUND: {root}", file=sys.stderr)
        return 2

    vios = scan_path(root, args.mode)

    if not vios:
        print(f"[PASS] mode={args.mode} target={root} violations=0", file=sys.stderr)
        return 0

    print(
        f"[FAIL] mode={args.mode} target={root} violations={len(vios)}",
        file=sys.stderr,
    )
    seen_categories: set[str] = set()
    for v in vios[: args.max_lines]:
        seen_categories.add(v.pattern_category)
        print(v.format_short(), file=sys.stderr)
    if len(vios) > args.max_lines:
        print(f"  ... and {len(vios) - args.max_lines} more", file=sys.stderr)
    print(
        f"  pattern_categories_cover={sorted(seen_categories)}", file=sys.stderr
    )

    return 1


if __name__ == "__main__":
    sys.exit(_cli())
