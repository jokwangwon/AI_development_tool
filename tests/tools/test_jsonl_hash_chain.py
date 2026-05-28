"""jsonl_hash_chain Layer 1 violation_type 정밀화 테스트 (57 entry 실 구현 sub-cycle).

(β) sub-수단 결정 발효 답습 — HISTORY_REWRITE 는 Layer 1 (hash chain) 에서
외부 anchor 없이 검출 불가 (history rewrite = Layer 2 history_anchor_verifier
+ rewrite_defense 영역, 55 entry consensus B-1/B-2 답습). 따라서 Layer 1
ViolationType enum 은 Layer-1-검출가능 3종만 보유한다.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_ROOT / "tools"))

import jsonl_hash_chain as jhc  # noqa: E402

_LEDGER = _ROOT / "tests" / "fixtures" / "jsonl_ledger"

# Layer 1 (hash chain) 가 외부 anchor 없이 검출 가능한 violation_type 전체.
_LAYER1_TYPES = {"prev_hash_mismatch", "hash_recalculation", "genesis_mismatch"}


def test_violation_type_enum_is_layer1_only() -> None:
    """ViolationType = Layer-1-검출가능 3종 (history_rewrite 부재 — Layer 2 영역)."""
    actual = {v.value for v in jhc.ViolationType}
    assert actual == _LAYER1_TYPES
    assert "history_rewrite" not in actual


@pytest.mark.parametrize(
    "fixture, expected",
    [
        ("pass/minimal_chain", []),
        ("fail/prev_hash_mismatch", ["prev_hash_mismatch"]),
        ("fail/hash_recalculation", ["hash_recalculation"]),
        ("fail/genesis_mismatch", ["genesis_mismatch"]),
    ],
)
def test_validate_chain_fixture_regression(fixture: str, expected: list[str]) -> None:
    """fixture 별 validate_chain violation_type 회귀 (g4-hash-chain.yml 답습)."""
    entries, parse_vios = jhc.parse_jsonl(_LEDGER / f"{fixture}.jsonl")
    assert parse_vios == []
    chain_vios = [v.violation_type for v in jhc.validate_chain(entries)]
    assert chain_vios == expected


def test_history_rewrite_never_emitted_by_layer1() -> None:
    """invariant: Layer 1 validate_chain 은 history_rewrite 를 절대 emit 하지 않는다.

    history rewrite 검출 = Layer 2 (history_anchor_verifier.py + rewrite_defense_check.py)
    영역 — 외부 anchor / base branch 비교 의무 (55 entry B-1 답습).
    """
    for path in sorted(_LEDGER.rglob("*.jsonl")):
        entries, _ = jhc.parse_jsonl(path)
        vios = [v.violation_type for v in jhc.validate_chain(entries)]
        assert "history_rewrite" not in vios, f"{path.name}: unexpected history_rewrite"


def test_build_violation_entry_uses_layer1_types_only() -> None:
    """build_violation_entry chain violation 필터 = Layer-1 enum 한정 (dead enum 0)."""
    entries, _ = jhc.parse_jsonl(_LEDGER / "fail/prev_hash_mismatch.jsonl")
    vios = jhc.validate_chain(entries)
    entry = jhc.build_violation_entry(entries, vios)
    assert entry is not None
    assert entry["content"]["violation_type"] in _LAYER1_TYPES
