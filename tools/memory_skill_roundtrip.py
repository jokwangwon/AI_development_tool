#!/usr/bin/env python3
"""Memory/Skill JSONL ledger round-trip validator — Group F PoC (G2 GP-6 feasibility).

답습 출처:
  - docs/phase0/g2-gp6-memory-skill-migration-feasibility-poc.md (본 PoC 사양)
  - tools/canonical_json.py (RFC 8785 JCS canonical JSON — Group C)
  - tools/jsonl_hash_chain.py (11 필드 schema + Genesis + chain 검증 — Group C)
  - tools/jsonl_roundtrip.py (T2 strict / T3 lossy / 3 ledger entry — Group C)
  - docs/architecture/provider-agnostic-memory-skill-design.md §4.2 (11 필드)
  - docs/decisions/ADR-012-evidence-ledger-protection.md §2.9 (3 ledger entry 형식) / §2.10 (Migration BLOCK)

핵심 강제 조건 (사용자 명시 F-범위 / F-금지 답습):
  - 공유 모듈 import 직접 (리팩토링 0건 / 복제 0건)
  - 토이 dict 변환 한정 (실 provider SDK 호출 0 / 실 Hermes 디스크 0)
  - feasibility 한정 (실 migration script 미진입 — Group H 영역)
  - vendor-specific 필드 prefix `_hermes_*` 1건 한정 (Tier-2/3 catalog 확장 금지)

Default mode (chain + round-trip):
  - jsonl_hash_chain validate_chain → chain_violation_detected ledger entry 자동 작성
  - jsonl_roundtrip round_trip → roundtrip_pass / roundtrip_lossy / roundtrip_fail

Feasibility mode (`--feasibility-mode hermes-to-claude`):
  - Step 1: 원본 entries chain 검증 (정합 의무)
  - Step 2: hermes_to_canonical projection (`_hermes_*` drop)
  - Step 3: canonical_to_claude (toy identity)
  - Step 4: claude_to_canonical (toy identity)
  - Step 5: lost_fields enum 감지 + roundtrip_lossy ledger entry 자동 작성

Exit codes:
  0 = roundtrip_pass (T2 strict, lost_fields=0)
  1 = roundtrip_lossy (lost_fields >= 1)
  2 = chain_violation_detected or roundtrip_fail
  3 = input / parse / schema error
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from typing import Any

from canonical_json import CanonicalizationError  # type: ignore[import-not-found]
from jsonl_hash_chain import (  # type: ignore[import-not-found]
    SUPPORTED_SCHEMA_VERSION,
    build_violation_entry,
    compute_entry_hash,
    compute_genesis_hash,
    parse_jsonl,
    validate_chain,
    validate_schema,
)
from jsonl_roundtrip import (  # type: ignore[import-not-found]
    RoundtripVerdict,
    build_roundtrip_entry,
    diff_lost_fields,
    round_trip,
)

HERMES_VENDOR_FIELD_PREFIX: str = "_hermes_"
"""Group F PoC 토이 vendor catalog — Tier-2/3 catalog 확장 금지 답습 (1건 한정)."""

ALLOWED_FEASIBILITY_MODES: tuple[str, ...] = ("hermes-to-claude",)
"""F-범위 #4 = "1개 이상" 충족 (Memory hermes→claude 단독). 추가 모드 = Group H 영역."""


def hermes_to_canonical(entry: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    """Hermes vendor-specific 필드 (`_hermes_*`) 제거 → canonical projection.

    Returns:
        (canonical_entry, dropped_field_names)
    """
    canonical = {k: v for k, v in entry.items() if not k.startswith(HERMES_VENDOR_FIELD_PREFIX)}
    dropped = sorted(k for k in entry.keys() if k.startswith(HERMES_VENDOR_FIELD_PREFIX))
    return canonical, dropped


def canonical_to_claude(entry: dict[str, Any]) -> dict[str, Any]:
    """Canonical 11 필드 → Claude toy format (PoC = identity 한정).

    실 Claude format (예: `~/.claude/memory.jsonl` 형식) 은 Group H 영역 — 본 PoC 미진입.
    """
    return dict(entry)


def claude_to_canonical(entry: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    """Claude toy format → canonical (역방향, PoC = identity 한정).

    Returns:
        (canonical_entry, dropped_field_names) — toy 환경 = lost_fields 0.
    """
    return dict(entry), []


def build_feasibility_lossy_entry(
    entries: list[dict[str, Any]],
    lost_fields: list[str],
    mode: str,
) -> dict[str, Any]:
    """Feasibility-mode 전용 roundtrip_lossy ledger entry 자동 작성 (ADR-012 §2.9 답습).

    `lost_fields_sample` 에 dropped 필드 enum 명시 + `feasibility_mode` 명시.
    """
    if entries:
        last_entry = entries[-1]
        prev_hash = last_entry.get(
            "hash",
            compute_genesis_hash(
                last_entry.get("scope", "global"),
                last_entry.get("schema_version", SUPPORTED_SCHEMA_VERSION),
            ),
        )
        scope = last_entry.get("scope", "global")
    else:
        prev_hash = compute_genesis_hash("global", SUPPORTED_SCHEMA_VERSION)
        scope = "global"

    now_iso = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    entry: dict[str, Any] = {
        "type": "meta",
        "scope": scope,
        "id": f"feasibility-lossy-{mode}-{now_iso}",
        "schema_version": SUPPORTED_SCHEMA_VERSION,
        "ts": now_iso,
        "agent": "user",
        "event": RoundtripVerdict.LOSSY.value,
        "content": {
            "feasibility_mode": mode,
            "entries_count": len(entries),
            "lost_fields_count": len(lost_fields),
            "lost_fields_sample": lost_fields[:10],
        },
        "evidence_refs": [],
        "prev_hash": prev_hash,
    }
    entry["hash"] = compute_entry_hash(entry)
    return entry


def feasibility_hermes_to_claude(
    entries: list[dict[str, Any]],
) -> tuple[RoundtripVerdict, list[str], str]:
    """Hermes → canonical → Claude → canonical 토이 매핑 검증.

    Returns:
        (verdict, lost_fields, detail)
    """
    if not entries:
        return RoundtripVerdict.PASS, [], "empty ledger — vacuous PASS (feasibility)"

    all_dropped: list[str] = []
    canonical_entries: list[dict[str, Any]] = []
    for i, entry in enumerate(entries):
        canonical, dropped = hermes_to_canonical(entry)
        canonical_entries.append(canonical)
        all_dropped.extend(f"entry[{i}].{f}" for f in dropped)

    claude_entries = [canonical_to_claude(e) for e in canonical_entries]

    final_canonical: list[dict[str, Any]] = []
    for entry in claude_entries:
        rev, _ = claude_to_canonical(entry)
        final_canonical.append(rev)

    diff_back = diff_lost_fields(canonical_entries, final_canonical)
    if diff_back:
        return (
            RoundtripVerdict.FAIL,
            all_dropped + diff_back,
            f"claude→canonical 역변환 비-identity (toy 매핑 위반): {len(diff_back)}",
        )

    if all_dropped:
        return (
            RoundtripVerdict.LOSSY,
            all_dropped,
            f"hermes→canonical projection 시 vendor-specific 필드 drop: {len(all_dropped)}",
        )

    return RoundtripVerdict.PASS, [], "feasibility hermes-to-claude T2 strict (lost_fields=0)"


def _cli() -> int:
    p = argparse.ArgumentParser(
        description="Memory/Skill JSONL ledger round-trip validator — Group F PoC (G2 GP-6 feasibility)"
    )
    p.add_argument("path", type=str, help="JSONL ledger 파일 경로")
    p.add_argument(
        "--feasibility-mode",
        choices=ALLOWED_FEASIBILITY_MODES,
        default=None,
        help=(
            "Feasibility 토이 매핑 모드. 미지정 시 default = chain + round-trip. "
            "`hermes-to-claude` = 본 PoC 한정 토이 매핑 (Group H 영역 미진입)."
        ),
    )
    p.add_argument(
        "--emit-ledger-entry",
        action="store_true",
        help="검증 verdict 에 따라 자동 ledger entry (`roundtrip_pass/lossy/fail` 또는 `chain_violation_detected`) 를 stdout 에 출력",
    )
    args = p.parse_args()

    path = Path(args.path)
    if not path.exists():
        print(f"FILE_NOT_FOUND: {path}", file=sys.stderr)
        return 3

    try:
        entries, parse_vios = parse_jsonl(path)
    except OSError as e:
        print(f"READ_ERROR: {e}", file=sys.stderr)
        return 3

    if parse_vios:
        print(f"PARSE_ERROR: {len(parse_vios)} parse violation(s)", file=sys.stderr)
        for v in parse_vios:
            print(f"  [{v.entry_index}] {v.violation_type}: {v.detail}", file=sys.stderr)
        return 3

    schema_vios = []
    for i, entry in enumerate(entries):
        schema_vios.extend(validate_schema(entry, i))
    if schema_vios:
        print(f"SCHEMA_ERROR: {len(schema_vios)} schema violation(s)", file=sys.stderr)
        for v in schema_vios:
            print(f"  [{v.entry_index}] {v.violation_type}: {v.detail}", file=sys.stderr)
        return 3

    chain_vios = validate_chain(entries)
    if chain_vios:
        print(f"CHAIN_VIOLATION: {len(chain_vios)} violation(s)", file=sys.stderr)
        for v in chain_vios:
            print(f"  [{v.entry_index}] {v.violation_type}: {v.detail}", file=sys.stderr)
        if args.emit_ledger_entry:
            try:
                ve = build_violation_entry(entries, chain_vios)
            except CanonicalizationError as e:
                print(f"CANONICAL_ERROR: build_violation_entry failed: {e}", file=sys.stderr)
                return 3
            if ve is not None:
                print(json.dumps(ve, ensure_ascii=False))
        return 2

    if args.feasibility_mode == "hermes-to-claude":
        verdict, lost_fields, detail = feasibility_hermes_to_claude(entries)
        print(
            f"verdict={verdict.value} entries={len(entries)} lost_fields={len(lost_fields)} "
            f"feasibility_mode=hermes-to-claude",
            file=sys.stderr,
        )
        if lost_fields:
            for f in lost_fields[:10]:
                print(f"  lost: {f}", file=sys.stderr)
            if len(lost_fields) > 10:
                print(f"  ... and {len(lost_fields) - 10} more", file=sys.stderr)
        print(f"detail: {detail}", file=sys.stderr)

        if args.emit_ledger_entry and verdict == RoundtripVerdict.LOSSY:
            ledger = build_feasibility_lossy_entry(entries, lost_fields, "hermes-to-claude")
            print(json.dumps(ledger, ensure_ascii=False))

        if verdict == RoundtripVerdict.PASS:
            return 0
        if verdict == RoundtripVerdict.LOSSY:
            return 1
        return 2

    # Default mode = round-trip on as-is entries (canonical layer T2 strict)
    result = round_trip(entries)
    print(
        f"verdict={result.verdict.value} entries={result.entries_count} "
        f"sha256_1={result.export_1_sha256} sha256_2={result.export_2_sha256} "
        f"lost_fields={len(result.lost_fields)}",
        file=sys.stderr,
    )
    if result.lost_fields:
        for f in result.lost_fields[:10]:
            print(f"  lost: {f}", file=sys.stderr)
    print(f"detail: {result.detail}", file=sys.stderr)

    if args.emit_ledger_entry:
        ledger = build_roundtrip_entry(entries, result)
        print(json.dumps(ledger, ensure_ascii=False))

    if result.verdict == RoundtripVerdict.PASS:
        return 0
    if result.verdict == RoundtripVerdict.LOSSY:
        return 1
    return 2


if __name__ == "__main__":
    sys.exit(_cli())
