#!/usr/bin/env python3
"""Rewrite defense check — Group C 후속 후속 PoC (G4 ADR-012 §2.8 Layer 2/3/4).

답습 출처:
  - docs/phase0/g4-rewrite-defense-layer234-poc.md (본 PoC 사양)
  - docs/decisions/ADR-012-evidence-ledger-protection.md §2.8 (Full Rewrite 5 Layer
    중 Layer 2 git append-only + Layer 3 pre-commit hook + Layer 4 CI 회귀 검증)
  - docs/architecture/provider-agnostic-memory-skill-design.md §4.4.5
  - docs/decisions/ADR-011-means-vs-ends-redaction.md §2.1 (a)~(e)
  - tools/jsonl_hash_chain.py (Group C — `parse_jsonl` import 직접)
  - tools/history_anchor_verifier.py (Group C 후속 — Layer 1/5 답습 cross-reference)

핵심 강제 조건 (사용자 명시 답습):
  - stdlib `re` + `json` + `dataclasses` 단독 (외부 의존 0건)
  - 실 shell git command 실행 0건 (subprocess 호출 미사용 — fixture text 비교만)
  - 실 GitHub API 호출 0건 (HTTP client 미사용)
  - 실 git hook 활성화 0건 + 실 repo history rewrite 0건

Mode (사용자 명시):
  --mode append-only       : L2 — commit history before/after fixture pair 비교
  --mode rewrite-command   : L3 — git command log fixture 의 dangerous pattern grep
  --mode line-regression   : L4 — base.jsonl/head.jsonl fixture pair entry-level diff

종료 코드:
  0 = violations 0 (PASS) 또는 list-defenses 정상
  1 = ≥1 violation 검출 (FAIL)
  2 = 입력 오류 (path 부재 / parse 실패)
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from jsonl_hash_chain import parse_jsonl  # type: ignore[import-not-found]

# ============================================================================
# Layer 3 — Dangerous git command catalog (4 patterns, ADR-012 §2.8 답습)
# ============================================================================

DANGEROUS_COMMAND_PATTERNS: tuple[tuple[str, str, re.Pattern[str]], ...] = (
    ("rebase", "git rebase",
     re.compile(r"\bgit\s+rebase\b")),
    ("filter-branch", "git filter-branch / filter-repo",
     re.compile(r"\bgit\s+filter[- ](?:branch|repo)\b")),
    ("reset-hard", "git reset --hard",
     re.compile(r"\bgit\s+reset\s+--hard\b")),
    ("push-force-or-amend", "git push --force or commit --amend",
     re.compile(r"\bgit\s+push\s+(?:--force\b|-f\b)|\bgit\s+commit\s+--amend\b")),
)
"""(pattern_id, description, regex) — 4 dangerous patterns.
   사양 §7.1 답습: rebase + filter-branch + reset --hard + push --force/amend."""

LINE_REGRESSION_TYPES: tuple[tuple[str, str], ...] = (
    ("line_deletion_detected", "head 의 entry 수가 base 보다 적음 (line 삭제)"),
    ("line_rewrite_detected", "head[i] != base[i] (in-place rewrite)"),
    ("line_reorder_detected", "shared prefix 내 entry 순서 변경 (in-place rewrite sub-case)"),
)
"""사양 §8.2 답습 — 3 line regression types."""


@dataclass(frozen=True)
class Violation:
    """Single rewrite defense violation (Group D/E/G/A3/CF 답습)."""

    file: Path
    line: int
    pattern_id: str
    detail: str

    def format_short(self) -> str:
        return f"{self.file}:{self.line}:{self.pattern_id}: {self.detail[:120]}"


# ============================================================================
# Layer 2 — append-only commit history diff
# ============================================================================

def parse_commit_history(file_path: Path) -> list[tuple[str, str]] | None:
    """Parse `<short-sha> <message>` per line. Returns None on read error."""
    try:
        text = file_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    out: list[tuple[str, str]] = []
    for raw in text.split("\n"):
        line = raw.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        parts = line.split(maxsplit=1)
        if not parts:
            continue
        sha = parts[0]
        msg = parts[1] if len(parts) > 1 else ""
        out.append((sha, msg))
    return out


def scan_append_only(target_dir: Path) -> list[Violation]:
    """L2 — fixture dir 의 before/after pair 비교."""
    vios: list[Violation] = []

    before_path = target_dir / "commit_history_before.txt"
    after_path = target_dir / "commit_history_after.txt"

    if not before_path.exists():
        vios.append(Violation(target_dir, 0, "fixture-missing",
                              f"required file missing: {before_path.name}"))
        return vios
    if not after_path.exists():
        vios.append(Violation(target_dir, 0, "fixture-missing",
                              f"required file missing: {after_path.name}"))
        return vios

    before = parse_commit_history(before_path)
    after = parse_commit_history(after_path)
    if before is None or after is None:
        vios.append(Violation(target_dir, 0, "fixture-read-error",
                              "before/after read failed"))
        return vios

    # check 1: after must be at least as long as before
    if len(after) < len(before):
        vios.append(Violation(
            after_path, 0, "non_fast_forward_detected",
            f"after has fewer commits than before ({len(after)} < {len(before)}) — possible truncation/reset"
        ))

    # check 2: shared prefix must be identical (sha + position)
    shared_len = min(len(before), len(after))
    reorder_seen = False
    for i in range(shared_len):
        b_sha, b_msg = before[i]
        a_sha, a_msg = after[i]
        if a_sha != b_sha:
            # Check if sha appears elsewhere in before (reorder vs force-push)
            other_idx = next((j for j, (s, _) in enumerate(before) if s == a_sha), None)
            if other_idx is not None and other_idx != i:
                if not reorder_seen:
                    vios.append(Violation(
                        after_path, i + 1, "history_reorder_detected",
                        f"after[{i}] sha={a_sha!r} appears at before[{other_idx}] — commit reorder detected"
                    ))
                    reorder_seen = True
            else:
                vios.append(Violation(
                    after_path, i + 1, "non_fast_forward_detected",
                    f"after[{i}] sha={a_sha!r} != before[{i}] sha={b_sha!r} — force-push / commit hash 변조"
                ))

    return vios


# ============================================================================
# Layer 3 — dangerous git command pattern grep
# ============================================================================

def scan_rewrite_command(file_path: Path) -> list[Violation]:
    """L3 — git command log fixture 의 dangerous pattern grep."""
    vios: list[Violation] = []
    try:
        text = file_path.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        vios.append(Violation(file_path, 0, "read-error", f"read failed: {e}"))
        return vios

    for line_no, raw in enumerate(text.split("\n"), start=1):
        line = raw.lstrip()
        if not line or line.startswith("#"):
            continue
        for pid, desc, regex in DANGEROUS_COMMAND_PATTERNS:
            if regex.search(line):
                vios.append(Violation(
                    file_path, line_no, pid,
                    f"dangerous command detected ({desc}): {raw.strip()[:80]}"
                ))

    return vios


# ============================================================================
# Layer 4 — JSONL line regression detector
# ============================================================================

def scan_line_regression(target_dir: Path) -> list[Violation]:
    """L4 — base.jsonl/head.jsonl entry-level diff."""
    vios: list[Violation] = []

    base_path = target_dir / "base.jsonl"
    head_path = target_dir / "head.jsonl"

    if not base_path.exists():
        vios.append(Violation(target_dir, 0, "fixture-missing",
                              f"required file missing: {base_path.name}"))
        return vios
    if not head_path.exists():
        vios.append(Violation(target_dir, 0, "fixture-missing",
                              f"required file missing: {head_path.name}"))
        return vios

    try:
        base_entries, base_parse_vios = parse_jsonl(base_path)
        head_entries, head_parse_vios = parse_jsonl(head_path)
    except OSError as e:
        vios.append(Violation(target_dir, 0, "read-error", f"jsonl read failed: {e}"))
        return vios

    for v in base_parse_vios:
        vios.append(Violation(base_path, v.entry_index + 1, "base-parse-error",
                              f"{v.violation_type}: {v.detail}"))
    for v in head_parse_vios:
        vios.append(Violation(head_path, v.entry_index + 1, "head-parse-error",
                              f"{v.violation_type}: {v.detail}"))
    if base_parse_vios or head_parse_vios:
        return vios

    # check 1: head must be at least as long as base
    if len(head_entries) < len(base_entries):
        vios.append(Violation(
            head_path, 0, "line_deletion_detected",
            f"head has fewer entries than base ({len(head_entries)} < {len(base_entries)}) — entry deletion"
        ))

    # check 2: shared prefix entries must be identical (all fields)
    shared_len = min(len(base_entries), len(head_entries))
    for i in range(shared_len):
        b = base_entries[i]
        h = head_entries[i]
        if b == h:
            continue
        # Find first differing field
        diff_fields: list[str] = []
        all_keys = set(b.keys()) | set(h.keys())
        for k in sorted(all_keys):
            if b.get(k) != h.get(k):
                diff_fields.append(k)
        # Check reorder (h[i] sha appears at base[j] for some j != i)
        h_id = h.get("id")
        b_other_idx = next((j for j, e in enumerate(base_entries) if e.get("id") == h_id), None)
        reorder = b_other_idx is not None and b_other_idx != i
        if reorder:
            vios.append(Violation(
                head_path, i + 1, "line_reorder_detected",
                f"head[{i}] id={h_id!r} appears at base[{b_other_idx}] — entry reorder detected"
            ))
        else:
            vios.append(Violation(
                head_path, i + 1, "line_rewrite_detected",
                f"head[{i}] differs from base[{i}] in fields: {diff_fields[:5]}"
            ))

    return vios


# ============================================================================
# Mode dispatch + CLI
# ============================================================================

def list_defenses() -> int:
    """`--list-defenses` self-check (사용자 명시 검증 9 답습)."""
    layers = (
        ("L1", "Hash chain (single entry tampering)", "Group C `validate_chain`",
         "답습 완료"),
        ("L2", "Append-only branch (force-push / reorder)",
         "본 PoC `--mode append-only`", "본 PoC"),
        ("L3", "Pre-commit hook (rebase / filter-branch / reset-hard / push-force/amend)",
         "본 PoC `--mode rewrite-command`", "본 PoC"),
        ("L4", "CI 회귀 검증 (line deletion / in-place rewrite)",
         "본 PoC `--mode line-regression`", "본 PoC"),
        ("L5", "External anchor (substitution / full rewrite)",
         "Group C 후속 `history_anchor_verifier`", "답습 완료"),
    )

    print(f"adr_012_section_2_8_layers={len(layers)}", file=sys.stderr)
    for layer_id, desc, tool, status in layers:
        print(f"  {layer_id}\t{desc}\t({tool}, {status})", file=sys.stderr)

    print(f"dangerous_git_commands={len(DANGEROUS_COMMAND_PATTERNS)}", file=sys.stderr)
    for pid, desc, _ in DANGEROUS_COMMAND_PATTERNS:
        print(f"  {pid}\t{desc}", file=sys.stderr)

    print(f"line_regression_types={len(LINE_REGRESSION_TYPES)}", file=sys.stderr)
    for tid, desc in LINE_REGRESSION_TYPES:
        print(f"  {tid}\t{desc}", file=sys.stderr)

    print(f"five_layer_compliant={len(layers) == 5}", file=sys.stderr)
    print(f"dangerous_command_count_compliant={len(DANGEROUS_COMMAND_PATTERNS) == 4}",
          file=sys.stderr)
    print(f"line_regression_type_count_compliant={len(LINE_REGRESSION_TYPES) == 3}",
          file=sys.stderr)
    print(f"poc_layer_coverage=L2+L3+L4 (L1=Group C, L5=Group C 후속)",
          file=sys.stderr)
    return 0


def _cli() -> int:
    p = argparse.ArgumentParser(
        description="Rewrite defense check — Group C 후속 후속 PoC (G4 ADR-012 §2.8 Layer 2/3/4)"
    )
    p.add_argument("path", type=str, nargs="?", default=None,
                   help="fixture 디렉토리 (append-only / line-regression) "
                   "또는 파일 (rewrite-command). --list-defenses 시 생략.")
    p.add_argument(
        "--mode",
        choices=("append-only", "rewrite-command", "line-regression"),
        default=None,
        help="append-only = L2 / rewrite-command = L3 / line-regression = L4",
    )
    p.add_argument("--list-defenses", action="store_true",
                   help="3 layers + 4 dangerous commands + 3 regression types enumerate")
    p.add_argument("--max-lines", type=int, default=20)
    args = p.parse_args()

    if args.list_defenses:
        return list_defenses()

    if not args.path or not args.mode:
        print("ERROR: path 와 --mode 필수 (--list-defenses 단독 외)", file=sys.stderr)
        return 2

    target = Path(args.path)
    if not target.exists():
        print(f"PATH_NOT_FOUND: {target}", file=sys.stderr)
        return 2

    all_vios: list[Violation] = []

    if args.mode == "append-only":
        # Iterate sub-directories that contain commit_history_before/after.txt
        if (target / "commit_history_before.txt").exists():
            all_vios.extend(scan_append_only(target))
        else:
            for sub in sorted(target.iterdir()):
                if sub.is_dir():
                    all_vios.extend(scan_append_only(sub))
    elif args.mode == "rewrite-command":
        if target.is_file():
            all_vios.extend(scan_rewrite_command(target))
        else:
            for f in sorted(target.rglob("*.txt")):
                if f.is_file():
                    all_vios.extend(scan_rewrite_command(f))
    else:  # line-regression
        if (target / "base.jsonl").exists():
            all_vios.extend(scan_line_regression(target))
        else:
            for sub in sorted(target.iterdir()):
                if sub.is_dir():
                    all_vios.extend(scan_line_regression(sub))

    if not all_vios:
        print(f"[PASS] mode={args.mode} target={target} violations=0", file=sys.stderr)
        return 0

    print(f"[FAIL] mode={args.mode} target={target} violations={len(all_vios)}",
          file=sys.stderr)
    seen_pattern_ids: set[str] = set()
    for v in all_vios:
        seen_pattern_ids.add(v.pattern_id)
    for v in all_vios[: args.max_lines]:
        print(v.format_short(), file=sys.stderr)
    if len(all_vios) > args.max_lines:
        print(f"  ... and {len(all_vios) - args.max_lines} more", file=sys.stderr)
    print(f"  pattern_ids_cover={sorted(seen_pattern_ids)}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(_cli())
