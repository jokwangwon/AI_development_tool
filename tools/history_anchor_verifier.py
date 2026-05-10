#!/usr/bin/env python3
"""History rewrite anchor verifier — Group C 후속 PoC (G4 Layer 5 External Anchor).

답습 출처:
  - docs/phase0/g4-history-rewrite-layer5-anchor-poc.md (본 PoC 사양)
  - docs/decisions/ADR-012-evidence-ledger-protection.md §2.8 (Full Rewrite 5 Layer 방어 — Layer 5 External Anchor) / §2.12 (Hermes 변조 차단 매트릭스)
  - docs/architecture/provider-agnostic-memory-skill-design.md §4.4.5
  - docs/decisions/ADR-011-means-vs-ends-redaction.md §2.1 (a)~(e)
  - tools/jsonl_hash_chain.py (Group C — `parse_jsonl` + `validate_chain` + `compute_entry_hash` + `compute_genesis_hash` import 직접)

핵심 강제 조건 (사용자 명시 답습):
  - stdlib `re` + `json` + `dataclasses` 단독 (외부 의존 0건)
  - Group C `validate_chain` import 직접 (리팩토링 0건)
  - signed commit / branch protection / external timestamping service 0건
  - 실 GitHub API 호출 0건 (literal 비교만)

Mode (사용자 명시):
  --mode chain-only      : Group C `validate_chain` 단독 호출 — Layer 1 baseline 답습 시연
                           (full rewrite 시 *의도된 PASS* 처리 — Layer 5 의무성 evidence)
  --mode anchor-verify   : 11-field anchor metadata + ledger 비교 — Layer 5 검출

종료 코드:
  0 = anchor matched (PASS) 또는 chain-only PASS
  1 = anchor mismatch detected (FAIL — 5 attack scenarios)
  2 = 입력 오류 (anchor/ledger 부재 / parse 실패)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from jsonl_hash_chain import (  # type: ignore[import-not-found]
    SUPPORTED_SCHEMA_VERSION,
    compute_genesis_hash,
    parse_jsonl,
    validate_chain,
    validate_schema,
)

# ============================================================================
# Anchor metadata 11-field schema (사양 §3.1 답습)
# ============================================================================

ANCHOR_REQUIRED_FIELDS: tuple[str, ...] = (
    "anchor_id", "anchor_ts", "anchor_method", "ledger_path",
    "expected_entry_count", "expected_tail_hash",
    "expected_genesis_hash", "schema_version", "external_run_id",
)
"""필수 9 필드."""

ANCHOR_OPTIONAL_FIELDS: tuple[str, ...] = ("external_run_url", "notes")
"""MVP-권장 2 필드."""

ALL_ANCHOR_FIELDS: tuple[str, ...] = ANCHOR_REQUIRED_FIELDS + ANCHOR_OPTIONAL_FIELDS
"""합산 11 필드."""

ALLOWED_ANCHOR_METHODS: tuple[str, ...] = ("ci_run_id",)
"""본 PoC 한정. signed_tag / external_snapshot = 별도 합의."""

# Field validators (regex)
SLUG_RE: re.Pattern[str] = re.compile(r"^[a-z0-9][a-z0-9-]{2,63}$")
ISO8601_RE: re.Pattern[str] = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z$")
SHA256_HEX_RE: re.Pattern[str] = re.compile(r"^[0-9a-f]{64}$")
SEMVER_RE: re.Pattern[str] = re.compile(r"^\d+\.\d+(?:\.\d+)?$")

# 5 attack scenarios (사양 §2.1 답습)
ATTACK_SCENARIOS: tuple[tuple[str, str], ...] = (
    ("full_rewrite", "Full rewrite — 모든 entry 재작성, prev_hash 모두 재계산 (chain 일관, tail hash 다름)"),
    ("tail_truncation", "Tail truncation — 마지막 N entry 제거, 남은 chain valid"),
    ("middle_deletion", "Middle deletion + 재계산 — 중간 entry 제거 후 prev_hash 재계산"),
    ("substitution", "Substitution — 전체 ledger 를 다른 valid chain 으로 교체"),
    ("anchor_tampered", "Anchor 자체 변조 (signature 부재 시 한계 — known limitation)"),
)


@dataclass(frozen=True)
class Violation:
    """Single anchor violation (Group D/E/G 답습)."""

    file: Path
    line: int
    pattern_id: str
    detail: str

    def format_short(self) -> str:
        return f"{self.file}:{self.line}:{self.pattern_id}: {self.detail[:120]}"


# ============================================================================
# Anchor metadata schema validation
# ============================================================================

def validate_anchor_schema(data: dict[str, Any], anchor_path: Path) -> list[Violation]:
    """11-field anchor schema validation."""
    vios: list[Violation] = []

    if not isinstance(data, dict):
        vios.append(Violation(anchor_path, 0, "anchor-not-object",
                              f"top-level not object: {type(data).__name__}"))
        return vios

    # Required 9 fields
    for f in ANCHOR_REQUIRED_FIELDS:
        if f not in data:
            vios.append(Violation(anchor_path, 0, "anchor-missing-required",
                                  f"required field missing: {f!r}"))

    # anchor_id
    aid = data.get("anchor_id")
    if isinstance(aid, str) and not SLUG_RE.match(aid):
        vios.append(Violation(anchor_path, 0, "anchor-invalid-id",
                              f"anchor_id={aid!r} not slug format"))

    # anchor_ts
    ats = data.get("anchor_ts")
    if isinstance(ats, str) and not ISO8601_RE.match(ats):
        vios.append(Violation(anchor_path, 0, "anchor-invalid-ts",
                              f"anchor_ts={ats!r} not ISO 8601"))

    # anchor_method
    am = data.get("anchor_method")
    if am is not None and am not in ALLOWED_ANCHOR_METHODS:
        vios.append(Violation(anchor_path, 0, "anchor-invalid-method",
                              f"anchor_method={am!r} not in {ALLOWED_ANCHOR_METHODS} "
                              f"(signed_tag / external_snapshot = 별도 합의)"))

    # expected_entry_count
    eec = data.get("expected_entry_count")
    if eec is not None and (not isinstance(eec, int) or eec < 1):
        vios.append(Violation(anchor_path, 0, "anchor-invalid-entry-count",
                              f"expected_entry_count={eec!r} not positive int"))

    # expected_tail_hash
    eth = data.get("expected_tail_hash")
    if isinstance(eth, str) and not SHA256_HEX_RE.match(eth):
        vios.append(Violation(anchor_path, 0, "anchor-invalid-tail-hash",
                              f"expected_tail_hash={eth!r} not 64-char sha256 hex"))

    # expected_genesis_hash
    egh = data.get("expected_genesis_hash")
    if isinstance(egh, str) and not SHA256_HEX_RE.match(egh):
        vios.append(Violation(anchor_path, 0, "anchor-invalid-genesis-hash",
                              f"expected_genesis_hash={egh!r} not 64-char sha256 hex"))

    # schema_version
    sv = data.get("schema_version")
    if sv is not None and sv != SUPPORTED_SCHEMA_VERSION:
        vios.append(Violation(anchor_path, 0, "anchor-invalid-schema-version",
                              f"schema_version={sv!r} != {SUPPORTED_SCHEMA_VERSION!r}"))

    return vios


# ============================================================================
# Anchor verification (Layer 5 검출 — 5 attack scenarios)
# ============================================================================

def verify_anchor(anchor_path: Path, ledger_path_override: Path | None = None) -> tuple[list[Violation], dict[str, Any]]:
    """Layer 5 anchor verification — 5 attack scenarios cover.

    Returns:
        (violations, anchor_data) — anchor_data 는 디버깅 보조.
    """
    vios: list[Violation] = []

    # Load anchor
    try:
        text = anchor_path.read_text(encoding="utf-8")
        anchor = json.loads(text)
    except (OSError, json.JSONDecodeError) as e:
        vios.append(Violation(anchor_path, 0, "anchor-parse-error",
                              f"anchor parse failed: {e}"))
        return vios, {}

    # Validate anchor schema
    vios.extend(validate_anchor_schema(anchor, anchor_path))
    if vios:
        return vios, anchor

    # Load ledger
    ledger_path_str = anchor.get("ledger_path", "")
    if ledger_path_override is not None:
        ledger_path = ledger_path_override
    else:
        # Resolve relative to anchor file directory
        ledger_path = (anchor_path.parent / ledger_path_str).resolve()
        if not ledger_path.exists():
            # Try as repo-relative path
            ledger_path = Path(ledger_path_str)

    if not ledger_path.exists():
        vios.append(Violation(anchor_path, 0, "anchor-ledger-not-found",
                              f"ledger_path={ledger_path_str!r} not found"))
        return vios, anchor

    try:
        entries, parse_vios = parse_jsonl(ledger_path)
    except OSError as e:
        vios.append(Violation(anchor_path, 0, "ledger-read-error", f"ledger read failed: {e}"))
        return vios, anchor

    # Layer 1 baseline check (Group C `validate_chain` import 직접 답습)
    chain_vios = validate_chain(entries)
    if chain_vios:
        vios.append(Violation(
            anchor_path, 0, "ledger-chain-broken",
            f"ledger fails Layer 1 chain validation (Group C): {len(chain_vios)} violations"
        ))
        # Continue with Layer 5 checks anyway

    # Layer 5 #1: entry count check
    expected_count = anchor.get("expected_entry_count")
    actual_count = len(entries)
    appended_only = False
    if expected_count is not None and actual_count != expected_count:
        if actual_count > expected_count:
            # extended ledger — Layer 5 정상 시제 (anchor_outdated_appended)
            # But still check that first N entries match
            appended_only = True
        else:
            vios.append(Violation(
                anchor_path, 0, "entry-count-mismatch",
                f"expected_entry_count={expected_count}, actual={actual_count} "
                f"(scenario: tail_truncation or middle_deletion)"
            ))

    # Layer 5 #2: tail hash check
    expected_tail_hash = anchor.get("expected_tail_hash")
    if expected_tail_hash and entries:
        if appended_only and expected_count is not None:
            # Compare against entry at expected_count - 1 (anchor 시점 마지막 entry)
            anchor_tail_idx = expected_count - 1
            if 0 <= anchor_tail_idx < len(entries):
                actual_tail = entries[anchor_tail_idx].get("hash")
                if actual_tail != expected_tail_hash:
                    vios.append(Violation(
                        anchor_path, 0, "tail-hash-mismatch",
                        f"anchor 시점 entry[{anchor_tail_idx}] hash={actual_tail!r} "
                        f"!= expected_tail_hash={expected_tail_hash!r} "
                        f"(scenario: history rewrite — extended 라도 prefix 일치 의무)"
                    ))
        else:
            actual_tail = entries[-1].get("hash") if entries else None
            if actual_tail != expected_tail_hash:
                vios.append(Violation(
                    anchor_path, 0, "tail-hash-mismatch",
                    f"actual_tail_hash={actual_tail!r} != expected={expected_tail_hash!r} "
                    f"(scenario: full_rewrite / substitution / middle_deletion / tail_truncation)"
                ))

    # Layer 5 #3: genesis hash check
    expected_genesis = anchor.get("expected_genesis_hash")
    if expected_genesis and entries:
        first = entries[0]
        scope = first.get("scope", "global")
        sver = first.get("schema_version", SUPPORTED_SCHEMA_VERSION)
        actual_genesis = compute_genesis_hash(scope, sver)
        if actual_genesis != expected_genesis:
            vios.append(Violation(
                anchor_path, 0, "genesis-hash-mismatch",
                f"actual_genesis={actual_genesis!r} != expected={expected_genesis!r} "
                f"(scenario: substitution — different scope/schema_version)"
            ))

    # Special case: anchor self-inconsistent (fixture #5 anchor_tampered)
    # If anchor's expected_tail_hash claims to come from this ledger but the ledger
    # passes Layer 1 AND has a different tail hash, that's anchor-side tampering.
    if (expected_tail_hash and entries and not chain_vios
            and not appended_only and expected_count == actual_count):
        actual_tail = entries[-1].get("hash")
        if actual_tail and actual_tail != expected_tail_hash:
            vios.append(Violation(
                anchor_path, 0, "anchor-self-inconsistent",
                "anchor expected_tail_hash 가 ledger의 실 tail 과 불일치 — "
                "anchor 자체 변조 가능성 (known limitation: anchor signing 부재)"
            ))

    return vios, anchor


# ============================================================================
# Mode: chain-only — Layer 1 inadequacy demo
# ============================================================================

def chain_only_check(ledger_path: Path) -> list[Violation]:
    """Group C `validate_chain` 단독 호출 — Layer 1 baseline 답습 시연.

    full rewrite 시 *의도된 PASS* 처리됨을 명시 (Layer 5 의무성 evidence).
    """
    vios: list[Violation] = []
    try:
        entries, parse_vios = parse_jsonl(ledger_path)
    except OSError as e:
        vios.append(Violation(ledger_path, 0, "ledger-read-error", f"read failed: {e}"))
        return vios

    if parse_vios:
        for v in parse_vios:
            vios.append(Violation(ledger_path, v.entry_index + 1, "ledger-parse-error",
                                  f"{v.violation_type}: {v.detail}"))
        return vios

    # Schema check
    for i, entry in enumerate(entries):
        schema_vios = validate_schema(entry, i)
        for sv in schema_vios:
            vios.append(Violation(ledger_path, i + 1, "ledger-schema-error",
                                  f"{sv.violation_type}: {sv.detail}"))

    # Chain check (Group C 답습)
    chain_vios = validate_chain(entries)
    for cv in chain_vios:
        vios.append(Violation(ledger_path, cv.entry_index + 1, "ledger-chain-violation",
                              f"{cv.violation_type}: {cv.detail}"))

    return vios


# ============================================================================
# Mode dispatch + CLI
# ============================================================================

def list_attack_models() -> int:
    """`--list-attack-models` self-check (사용자 명시 검증 9 답습)."""
    print(f"attack_scenarios={len(ATTACK_SCENARIOS)}", file=sys.stderr)
    for sid, desc in ATTACK_SCENARIOS:
        print(f"  {sid}\t{desc}", file=sys.stderr)
    print(f"anchor_required_fields={len(ANCHOR_REQUIRED_FIELDS)}", file=sys.stderr)
    print(f"  fields={list(ANCHOR_REQUIRED_FIELDS)}", file=sys.stderr)
    print(f"anchor_optional_fields={len(ANCHOR_OPTIONAL_FIELDS)}", file=sys.stderr)
    print(f"  fields={list(ANCHOR_OPTIONAL_FIELDS)}", file=sys.stderr)
    print(f"total_anchor_fields={len(ALL_ANCHOR_FIELDS)}", file=sys.stderr)
    print(f"allowed_anchor_methods={list(ALLOWED_ANCHOR_METHODS)}", file=sys.stderr)
    print(
        f"known_limitations=1 (anchor 자체 signing 부재 — multi-host MANDATORY 영역, ADR-012 §2.8)",
        file=sys.stderr,
    )
    print(f"layer_5_compliant={len(ATTACK_SCENARIOS) == 5}", file=sys.stderr)
    print(f"anchor_field_count_compliant={len(ALL_ANCHOR_FIELDS) == 11}", file=sys.stderr)
    print("layer_1_inadequacy_demo_supported=True (chain-only mode)", file=sys.stderr)
    return 0


def _cli() -> int:
    p = argparse.ArgumentParser(
        description="History anchor verifier — Group C 후속 PoC (G4 Layer 5 External Anchor)"
    )
    p.add_argument("path", type=str, nargs="?", default=None,
                   help="anchor.json (anchor-verify) 또는 ledger.jsonl (chain-only) 경로")
    p.add_argument("--mode", choices=("chain-only", "anchor-verify"), default=None,
                   help="chain-only = Layer 1 baseline / anchor-verify = Layer 5 검출")
    p.add_argument("--list-attack-models", action="store_true",
                   help="5 attack scenarios + 11 anchor fields + known limitations enumerate")
    p.add_argument("--max-lines", type=int, default=20)
    args = p.parse_args()

    if args.list_attack_models:
        return list_attack_models()

    if not args.path or not args.mode:
        print("ERROR: path 와 --mode 필수 (--list-attack-models 단독 외)", file=sys.stderr)
        return 2

    target = Path(args.path)
    if not target.exists():
        print(f"PATH_NOT_FOUND: {target}", file=sys.stderr)
        return 2

    if args.mode == "chain-only":
        # If target is a directory, scan all .jsonl files in it
        if target.is_dir():
            jsonl_files = sorted(target.rglob("*.jsonl"))
        else:
            jsonl_files = [target]
        all_vios: list[Violation] = []
        for f in jsonl_files:
            all_vios.extend(chain_only_check(f))

        if not all_vios:
            print(f"[PASS] mode=chain-only target={target} violations=0", file=sys.stderr)
            print(
                "  NOTE: Layer 1 단독으로는 full rewrite / tail truncation / middle deletion / substitution 검출 불가",
                file=sys.stderr,
            )
            print("        Layer 5 (anchor-verify) 의무성 evidence — ADR-012 §2.8 답습", file=sys.stderr)
            return 0

        print(f"[FAIL] mode=chain-only target={target} violations={len(all_vios)}",
              file=sys.stderr)
        for v in all_vios[: args.max_lines]:
            print(v.format_short(), file=sys.stderr)
        if len(all_vios) > args.max_lines:
            print(f"  ... and {len(all_vios) - args.max_lines} more", file=sys.stderr)
        return 1

    # anchor-verify mode
    if target.is_dir():
        anchor_files = sorted(target.rglob("*.json"))
    elif target.suffix == ".json":
        anchor_files = [target]
    else:
        print(f"ERROR: anchor-verify mode expects .json file, got {target.suffix!r}",
              file=sys.stderr)
        return 2

    all_vios = []
    seen_pattern_ids: set[str] = set()
    for af in anchor_files:
        vios, _ = verify_anchor(af)
        all_vios.extend(vios)
        for v in vios:
            seen_pattern_ids.add(v.pattern_id)

    if not all_vios:
        print(f"[PASS] mode=anchor-verify target={target} violations=0", file=sys.stderr)
        print("  anchor matched (entry_count + tail_hash + genesis_hash 모두 일치)",
              file=sys.stderr)
        # Detect "extended append" warning case via re-checking
        # (handled inline in verify_anchor, but signal it here too if applicable)
        return 0

    print(f"[FAIL] mode=anchor-verify target={target} violations={len(all_vios)}",
          file=sys.stderr)
    for v in all_vios[: args.max_lines]:
        print(v.format_short(), file=sys.stderr)
    if len(all_vios) > args.max_lines:
        print(f"  ... and {len(all_vios) - args.max_lines} more", file=sys.stderr)
    print(f"  pattern_ids_cover={sorted(seen_pattern_ids)}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(_cli())
