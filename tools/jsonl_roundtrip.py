#!/usr/bin/env python3
"""JSONL ledger round-trip validator — Group C PoC (G4 통합).

답습 출처:
  - docs/decisions/ADR-012-evidence-ledger-protection.md §2.9 (3 ledger entry 형식 — roundtrip_pass / roundtrip_lossy / roundtrip_fail)
  - docs/architecture/provider-agnostic-memory-skill-design.md §4.6 (Tier-based round-trip)
  - docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md §4.3 (JSONL → JSONL 동일 형식 한정)
  - tools/canonical_json.py + tools/jsonl_hash_chain.py 답습

핵심 강제 조건:
  - JSONL → JSONL 동일 형식 round-trip 한정 (cross-format = Group H 영역 — 사용자 명시 금지)
  - T2 strict: parse → re-serialize → byte/sha256 hash 100% 일치 → roundtrip_pass entry
  - T3 lossy: 의미 보존 + lossy 영역 (lost_fields enumeration 자동) → roundtrip_lossy entry
  - parse 실패 또는 의미 보존 실패 → roundtrip_fail entry
  - lost_fields = canonical JSON diff 자동 (필드 누락/추가/타입 변경 등)

종료 코드:
  0 = T2 strict PASS
  1 = T3 lossy (lossy entry 자동 작성)
  2 = T2/T3 모두 실패 (roundtrip_fail entry 자동 작성)
  3 = 입력 오류 (parse 실패 등)
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import sys
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any

from canonical_json import (  # type: ignore[import-not-found]
    CanonicalizationError,
    CrossCheckMode,
    to_canonical,
)
from jsonl_hash_chain import (  # type: ignore[import-not-found]
    SUPPORTED_SCHEMA_VERSION,
    compute_entry_hash,
    compute_genesis_hash,
    parse_jsonl,
)


class RoundtripVerdict(str, Enum):
    PASS = "roundtrip_pass"
    LOSSY = "roundtrip_lossy"
    FAIL = "roundtrip_fail"


@dataclass
class RoundtripResult:
    verdict: RoundtripVerdict
    entries_count: int
    export_1_sha256: str | None
    export_2_sha256: str | None
    lost_fields: list[str]
    detail: str


def serialize_entries(entries: list[dict[str, Any]]) -> bytes:
    """Entries → JSONL bytes — canonical JSON per line + newline.

    각 entry 는 canonical JSON (rfc8785) 으로 직렬화 후 newline join.
    """
    lines: list[bytes] = []
    for entry in entries:
        result = to_canonical(entry, mode=CrossCheckMode.PRIMARY_1_ONLY)
        lines.append(result.canonical)
    return b"\n".join(lines) + b"\n"


def diff_lost_fields(original: list[dict[str, Any]], reparsed: list[dict[str, Any]]) -> list[str]:
    """Canonical JSON diff — 필드 누락 / 추가 / 타입 변경 enumerate."""
    diffs: list[str] = []
    if len(original) != len(reparsed):
        diffs.append(f"entries_count_changed: {len(original)} -> {len(reparsed)}")
        return diffs
    for i, (orig, rep) in enumerate(zip(original, reparsed)):
        orig_keys = set(orig.keys())
        rep_keys = set(rep.keys())
        if orig_keys - rep_keys:
            diffs.append(f"entry[{i}] removed_fields: {sorted(orig_keys - rep_keys)}")
        if rep_keys - orig_keys:
            diffs.append(f"entry[{i}] added_fields: {sorted(rep_keys - orig_keys)}")
        for key in orig_keys & rep_keys:
            if type(orig[key]) is not type(rep[key]):
                diffs.append(
                    f"entry[{i}].{key} type_changed: {type(orig[key]).__name__} -> {type(rep[key]).__name__}"
                )
            elif orig[key] != rep[key]:
                diffs.append(f"entry[{i}].{key} value_changed")
    return diffs


def round_trip(entries: list[dict[str, Any]]) -> RoundtripResult:
    """Round-trip = serialize → parse → re-serialize → byte/sha256 비교."""
    if not entries:
        return RoundtripResult(
            verdict=RoundtripVerdict.PASS,
            entries_count=0,
            export_1_sha256=None,
            export_2_sha256=None,
            lost_fields=[],
            detail="empty ledger — vacuous PASS",
        )

    try:
        export_1 = serialize_entries(entries)
    except CanonicalizationError as e:
        return RoundtripResult(
            verdict=RoundtripVerdict.FAIL,
            entries_count=len(entries),
            export_1_sha256=None,
            export_2_sha256=None,
            lost_fields=[],
            detail=f"export_1 canonical_json failed: {e}",
        )

    sha256_1 = hashlib.sha256(export_1).hexdigest()

    # Re-parse
    reparsed: list[dict[str, Any]] = []
    for line in export_1.split(b"\n"):
        if not line.strip():
            continue
        try:
            obj = json.loads(line.decode("utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            return RoundtripResult(
                verdict=RoundtripVerdict.FAIL,
                entries_count=len(entries),
                export_1_sha256=sha256_1,
                export_2_sha256=None,
                lost_fields=[],
                detail=f"reparse failed: {e}",
            )
        if not isinstance(obj, dict):
            return RoundtripResult(
                verdict=RoundtripVerdict.FAIL,
                entries_count=len(entries),
                export_1_sha256=sha256_1,
                export_2_sha256=None,
                lost_fields=[],
                detail=f"reparsed entry not dict: type={type(obj).__name__}",
            )
        reparsed.append(obj)

    try:
        export_2 = serialize_entries(reparsed)
    except CanonicalizationError as e:
        return RoundtripResult(
            verdict=RoundtripVerdict.FAIL,
            entries_count=len(entries),
            export_1_sha256=sha256_1,
            export_2_sha256=None,
            lost_fields=[],
            detail=f"export_2 canonical_json failed: {e}",
        )

    sha256_2 = hashlib.sha256(export_2).hexdigest()

    if sha256_1 == sha256_2:
        return RoundtripResult(
            verdict=RoundtripVerdict.PASS,
            entries_count=len(entries),
            export_1_sha256=sha256_1,
            export_2_sha256=sha256_2,
            lost_fields=[],
            detail="T2 strict — byte/sha256 100% match",
        )

    lost = diff_lost_fields(entries, reparsed)
    return RoundtripResult(
        verdict=RoundtripVerdict.LOSSY,
        entries_count=len(entries),
        export_1_sha256=sha256_1,
        export_2_sha256=sha256_2,
        lost_fields=lost,
        detail=f"T3 lossy — sha256 diff {sha256_1[:16]} != {sha256_2[:16]}, lost_fields={len(lost)}",
    )


def build_roundtrip_entry(
    entries: list[dict[str, Any]],
    result: RoundtripResult,
) -> dict[str, Any]:
    """Roundtrip ledger entry 자동 작성 (ADR-012 §2.9 — 3 형식)."""
    if entries:
        last_entry = entries[-1]
        prev_hash = last_entry.get("hash", compute_genesis_hash(
            last_entry.get("scope", "global"), last_entry.get("schema_version", SUPPORTED_SCHEMA_VERSION)
        ))
        scope = last_entry.get("scope", "global")
    else:
        prev_hash = compute_genesis_hash("global", SUPPORTED_SCHEMA_VERSION)
        scope = "global"

    now_iso = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    content: dict[str, Any] = {
        "verdict": result.verdict.value,
        "entries_count": result.entries_count,
        "export_1_sha256": result.export_1_sha256,
        "export_2_sha256": result.export_2_sha256,
        "lost_fields_count": len(result.lost_fields),
        "lost_fields_sample": result.lost_fields[:5],
        "detail": result.detail[:300],
    }
    entry: dict[str, Any] = {
        "type": "meta",
        "scope": scope,
        "id": f"roundtrip-{result.verdict.value}-{now_iso}",
        "schema_version": SUPPORTED_SCHEMA_VERSION,
        "ts": now_iso,
        "agent": "user",
        "event": result.verdict.value,
        "content": content,
        "evidence_refs": [],
        "prev_hash": prev_hash,
    }
    entry["hash"] = compute_entry_hash(entry)
    return entry


def _cli() -> int:
    p = argparse.ArgumentParser(
        description="JSONL ledger round-trip validator — Group C PoC (G4 통합)"
    )
    p.add_argument("path", type=str, help="JSONL ledger 파일 경로")
    p.add_argument(
        "--emit-roundtrip-entry",
        action="store_true",
        help="roundtrip_pass/lossy/fail entry 를 stdout 에 출력 (ADR-012 §2.9)",
    )
    p.add_argument(
        "--require-strict",
        action="store_true",
        help="T2 strict 만 PASS — T3 lossy 는 rc=1 (CI strict mode)",
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
        print(f"PARSE_ERROR: {len(parse_vios)} parse violation(s) — round-trip skipped", file=sys.stderr)
        for v in parse_vios:
            print(f"  [{v.entry_index}] {v.violation_type}: {v.detail}", file=sys.stderr)
        return 3

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
        if len(result.lost_fields) > 10:
            print(f"  ... and {len(result.lost_fields) - 10} more", file=sys.stderr)
    print(f"detail: {result.detail}", file=sys.stderr)

    if args.emit_roundtrip_entry:
        entry = build_roundtrip_entry(entries, result)
        print(json.dumps(entry, ensure_ascii=False))

    if result.verdict == RoundtripVerdict.PASS:
        return 0
    if result.verdict == RoundtripVerdict.LOSSY:
        return 1 if args.require_strict else 1
    return 2


if __name__ == "__main__":
    sys.exit(_cli())
