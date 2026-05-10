#!/usr/bin/env python3
"""JSONL ledger hash chain validator — Group C PoC (G4 통합).

답습 출처:
  - docs/decisions/ADR-012-evidence-ledger-protection.md §2.2 (event 11번째 필드 17 enum) /
    §2.3 (Append-only + Hash Chain Layer 1) / §2.6 (Genesis Hash MVP) /
    §2.7 (prev_hash 검증 실패 BLOCK + manual + violation entry)
  - docs/architecture/provider-agnostic-memory-skill-design.md §4.2 (11 필드) / §4.4 (hash chain)
  - docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md §2 / §4.2
  - tools/canonical_json.py (Q1 합의 답습 — rfc8785 + jcs 병렬 cross-check)

핵심 강제 조건:
  - 11 필드 schema (type / scope / id / schema_version / ts / agent / event / content / evidence_refs / prev_hash / hash)
  - schema_version != "0.1" → BLOCK (ADR-012 §2.10 답습)
  - Genesis hash = sha256("genesis:<scope>:<schema_version>") (ADR-012 §2.6 MVP)
  - hash 계산 = sha256(canonical_json(entry - "hash" field))
  - prev_hash 검증 실패 = BLOCK + chain_violation_detected entry 자동 작성
  - violation_type 4종: prev_hash_mismatch / hash_recalculation / history_rewrite / genesis_mismatch
  - timestamp monotonicity: 본 entry ts >= prev_hash entry ts (ADR-012 §3.4)
  - T3 자동 정책 변경 금지 (ADR-011 §2.4) — 자동 revert 0건, BLOCK + manual

종료 코드:
  0 = 모든 검사 PASS
  1 = 1+ violation 검출
  2 = invalid input (parse 실패 등)
"""
from __future__ import annotations

import argparse
import dataclasses
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

REQUIRED_FIELDS: tuple[str, ...] = (
    "type",
    "scope",
    "id",
    "schema_version",
    "ts",
    "agent",
    "event",
    "content",
    "evidence_refs",
    "prev_hash",
    "hash",
)

ALLOWED_TYPES: tuple[str, ...] = ("memory", "skill", "meta")
ALLOWED_SCOPES: tuple[str, ...] = ("global", "project", "session")
ALLOWED_AGENTS: tuple[str, ...] = ("user", "claude-code", "hermes", "external_llm")
SUPPORTED_SCHEMA_VERSION: str = "0.1"


class ViolationType(str, Enum):
    """Chain violation 4종 (ADR-012 §2.7 답습)."""

    PREV_HASH_MISMATCH = "prev_hash_mismatch"
    HASH_RECALCULATION = "hash_recalculation"
    HISTORY_REWRITE = "history_rewrite"
    GENESIS_MISMATCH = "genesis_mismatch"


@dataclass
class Violation:
    """Single violation report."""

    entry_index: int
    entry_id: str
    violation_type: str  # ViolationType.value or "schema_*" / "monotonicity_*"
    detail: str


def compute_genesis_hash(scope: str, schema_version: str) -> str:
    """Genesis hash MVP — sha256("genesis:<scope>:<schema_version>") (ADR-012 §2.6).

    schema_version 0.2 이상 진입 시 별도 chain (별도 chain_id 또는 schema_version) — 별도 합의 영역.
    """
    return hashlib.sha256(f"genesis:{scope}:{schema_version}".encode("utf-8")).hexdigest()


def compute_entry_hash(entry: dict[str, Any]) -> str:
    """Entry hash = sha256(canonical_json(entry - "hash" field)).

    Q1 합의 답습 — runtime mode = PRIMARY_1_ONLY (rfc8785 단독), corpus 시점 cross-check 별도.
    """
    payload = {k: v for k, v in entry.items() if k != "hash"}
    result = to_canonical(payload, mode=CrossCheckMode.PRIMARY_1_ONLY)
    return result.sha256_hex


def parse_iso8601(s: str) -> dt.datetime:
    """ISO 8601 timestamp parse — 'Z' suffix 정규화."""
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    return dt.datetime.fromisoformat(s)


def validate_schema(entry: dict[str, Any], index: int) -> list[Violation]:
    """11 필드 schema validation."""
    vios: list[Violation] = []
    entry_id = str(entry.get("id", f"<index={index}>"))

    missing = [f for f in REQUIRED_FIELDS if f not in entry]
    if missing:
        vios.append(
            Violation(
                entry_index=index,
                entry_id=entry_id,
                violation_type="schema_missing_field",
                detail=f"missing required fields: {missing}",
            )
        )
        return vios

    if entry["type"] not in ALLOWED_TYPES:
        vios.append(
            Violation(index, entry_id, "schema_invalid_type", f"type={entry['type']!r} not in {ALLOWED_TYPES}")
        )
    if entry["scope"] not in ALLOWED_SCOPES:
        vios.append(
            Violation(index, entry_id, "schema_invalid_scope", f"scope={entry['scope']!r} not in {ALLOWED_SCOPES}")
        )
    if entry["agent"] not in ALLOWED_AGENTS:
        vios.append(
            Violation(index, entry_id, "schema_invalid_agent", f"agent={entry['agent']!r} not in {ALLOWED_AGENTS}")
        )
    if entry["schema_version"] != SUPPORTED_SCHEMA_VERSION:
        vios.append(
            Violation(
                index,
                entry_id,
                "schema_version_unsupported",
                f"schema_version={entry['schema_version']!r} != {SUPPORTED_SCHEMA_VERSION!r} (ADR-012 §2.10)",
            )
        )
    if not isinstance(entry["evidence_refs"], list):
        vios.append(
            Violation(index, entry_id, "schema_invalid_evidence_refs", "evidence_refs must be list")
        )
    if not isinstance(entry["content"], (dict, list, str, int, float, bool)) and entry["content"] is not None:
        vios.append(
            Violation(index, entry_id, "schema_invalid_content", "content must be JSON-serializable")
        )

    try:
        parse_iso8601(entry["ts"])
    except (ValueError, TypeError) as e:
        vios.append(Violation(index, entry_id, "schema_invalid_ts", f"ts parse error: {e}"))

    return vios


def validate_chain(entries: list[dict[str, Any]]) -> list[Violation]:
    """Genesis + prev_hash ↔ hash chain + timestamp monotonicity 검증."""
    vios: list[Violation] = []
    if not entries:
        return vios

    prev_ts: dt.datetime | None = None
    prev_hash_actual: str | None = None

    for i, entry in enumerate(entries):
        entry_id = str(entry.get("id", f"<index={i}>"))

        # Hash recalculation 검증
        try:
            recomputed = compute_entry_hash(entry)
        except CanonicalizationError as e:
            vios.append(
                Violation(i, entry_id, "schema_canonical_error", f"canonical_json failed: {e}")
            )
            continue

        if recomputed != entry.get("hash"):
            vios.append(
                Violation(
                    i,
                    entry_id,
                    ViolationType.HASH_RECALCULATION.value,
                    f"hash field={entry.get('hash')!r} != recomputed={recomputed!r}",
                )
            )

        # prev_hash 검증
        if i == 0:
            expected_genesis = compute_genesis_hash(entry["scope"], entry["schema_version"])
            if entry["prev_hash"] != expected_genesis:
                vios.append(
                    Violation(
                        i,
                        entry_id,
                        ViolationType.GENESIS_MISMATCH.value,
                        f"first entry prev_hash={entry['prev_hash']!r} != genesis={expected_genesis!r}",
                    )
                )
        else:
            if entry["prev_hash"] != prev_hash_actual:
                vios.append(
                    Violation(
                        i,
                        entry_id,
                        ViolationType.PREV_HASH_MISMATCH.value,
                        f"prev_hash={entry['prev_hash']!r} != prior entry hash={prev_hash_actual!r}",
                    )
                )

        # Timestamp monotonicity (ADR-012 §3.4)
        try:
            cur_ts = parse_iso8601(entry["ts"])
        except (ValueError, TypeError):
            cur_ts = None  # schema_invalid_ts 가 이미 등록됨
        if cur_ts is not None and prev_ts is not None and cur_ts < prev_ts:
            vios.append(
                Violation(
                    i,
                    entry_id,
                    "monotonicity_violation",
                    f"ts={entry['ts']!r} < prior ts (ADR-012 §3.4 monotonicity)",
                )
            )
        if cur_ts is not None:
            prev_ts = cur_ts

        # 다음 iteration 위해 hash field 값 (recompute 와 같으면 그대로, 아니면 chain 깨짐 → mismatch 보고됨)
        prev_hash_actual = entry.get("hash")

    return vios


def build_violation_entry(
    entries: list[dict[str, Any]],
    violations: list[Violation],
) -> dict[str, Any] | None:
    """chain_violation_detected ledger entry 자동 작성 (ADR-012 §2.7).

    Returns:
        새 ledger entry dict (caller 가 ledger 에 append 가능 형식) 또는 None (위반 0건)
    """
    if not violations:
        return None

    # 첫 violation 이 history_rewrite 가능성 ↔ 그 외 분류
    first_vio = violations[0]
    chain_violations = [
        v for v in violations
        if v.violation_type in {vt.value for vt in ViolationType}
    ]
    if not chain_violations:
        # schema/monotonicity 위반만 — chain_violation_detected 자동 작성 영역 외
        return None

    # 마지막 entry 의 hash 를 prev_hash 로 사용 (chain 연속성 — append-only 답습)
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
    entry: dict[str, Any] = {
        "type": "meta",
        "scope": scope,
        "id": f"chain-violation-{now_iso}",
        "schema_version": SUPPORTED_SCHEMA_VERSION,
        "ts": now_iso,
        "agent": "user",  # ADR-012 §2.12 — Hermes 자기 작성 금지, 외부 트리거 한정
        "event": "chain_violation_detected",
        "content": {
            "violation_type": chain_violations[0].violation_type,
            "detected_at": now_iso,
            "affected_entry": chain_violations[0].entry_id,
            "violations_count": len(chain_violations),
            "first_detail": chain_violations[0].detail[:200],
        },
        "evidence_refs": [],
        "prev_hash": prev_hash,
    }
    entry["hash"] = compute_entry_hash(entry)
    return entry


def parse_jsonl(path: Path) -> tuple[list[dict[str, Any]], list[Violation]]:
    """JSONL 파일 파싱 — line-by-line (Group A 답습)."""
    entries: list[dict[str, Any]] = []
    parse_vios: list[Violation] = []
    with open(path, "r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            stripped = line.strip()
            if not stripped:
                continue
            try:
                entry = json.loads(stripped)
            except json.JSONDecodeError as e:
                parse_vios.append(
                    Violation(
                        entry_index=lineno - 1,
                        entry_id=f"<line={lineno}>",
                        violation_type="parse_error",
                        detail=f"JSON parse failed: {e}",
                    )
                )
                continue
            if not isinstance(entry, dict):
                parse_vios.append(
                    Violation(
                        entry_index=lineno - 1,
                        entry_id=f"<line={lineno}>",
                        violation_type="parse_error",
                        detail=f"entry not dict: type={type(entry).__name__}",
                    )
                )
                continue
            entries.append(entry)
    return entries, parse_vios


def _cli() -> int:
    p = argparse.ArgumentParser(
        description="JSONL ledger hash chain validator — Group C PoC (G4 통합)"
    )
    p.add_argument("path", type=str, help="JSONL ledger 파일 경로")
    p.add_argument(
        "--emit-violation-entry",
        action="store_true",
        help="chain violation 검출 시 chain_violation_detected entry 를 stdout 에 출력",
    )
    args = p.parse_args()

    try:
        path = Path(args.path)
    except OSError as e:
        print(f"PATH_ERROR: {e}", file=sys.stderr)
        return 2

    if not path.exists():
        print(f"FILE_NOT_FOUND: {path}", file=sys.stderr)
        return 2

    try:
        entries, parse_vios = parse_jsonl(path)
    except OSError as e:
        print(f"READ_ERROR: {e}", file=sys.stderr)
        return 2

    all_vios: list[Violation] = list(parse_vios)
    schema_vios: list[Violation] = []
    for i, entry in enumerate(entries):
        schema_vios.extend(validate_schema(entry, i))
    all_vios.extend(schema_vios)

    # schema 위반된 entry 는 chain 검증 skip (cascading 회피)
    valid_indices = set(range(len(entries))) - {v.entry_index for v in schema_vios}
    valid_entries = [entries[i] for i in sorted(valid_indices)]
    chain_vios = validate_chain(valid_entries)
    all_vios.extend(chain_vios)

    if not all_vios:
        print(
            f"PASS: {path.name} — {len(entries)} entries, all checks passed (schema + chain + monotonicity)",
            file=sys.stderr,
        )
        return 0

    print(f"FAIL: {path.name} — {len(all_vios)} violation(s):", file=sys.stderr)
    for v in all_vios:
        print(
            f"  [{v.entry_index}] id={v.entry_id} type={v.violation_type}",
            file=sys.stderr,
        )
        print(f"      detail: {v.detail}", file=sys.stderr)

    if args.emit_violation_entry:
        violation_entry = build_violation_entry(entries, all_vios)
        if violation_entry is not None:
            print(json.dumps(violation_entry, ensure_ascii=False))

    return 1


if __name__ == "__main__":
    sys.exit(_cli())
