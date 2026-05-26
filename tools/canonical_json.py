#!/usr/bin/env python3
"""Canonical JSON (RFC 8785 JCS) — Group C PoC (G4 통합).

답습 출처:
  - docs/decisions/ADR-012-evidence-ledger-protection.md §2.5 (RFC 8785 JCS Primary + jq fallback + corpus 검증 ≥20개)
  - docs/architecture/provider-agnostic-memory-skill-design.md §4.4.2 (Canonical JSON 보강)
  - docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md §3 (사용자 명시 결정 갱신 — rfc8785 + jcs 병렬 cross-check)
  - docs/review/3plus1-consensus-2026-05-10-g4-jcs-library-selection.md (Q1 풀 3+1 합의 17 조건)
  - docs/review/3plus1-consensus-2026-05-10-g4-corpus-poc-scope-short.md (Q2/Q3 단축 합의 6 조건)

핵심 강제 조건:
  - Primary 1: rfc8785 (Trail of Bits, Apache-2.0, RA-9 §B.2 11/11 sanity PASS)
  - Primary 2: jcs (titusz, Apache-2.0, RA-9 §B.2 11/11 sanity PASS)
  - Fallback: jq -S -c (POSIX 표준, ADR-012 §2.5 명시 답습)
  - cross-check 시점 = corpus 시점 강제 (TR-C-2 trigger 답습 — Q1 합의 D-1)
  - cross-check 시점 runtime = 본 PoC 호출자 결정 (Mode 옵션 제공, 기본 = Mode 1 단독 + corpus 시점 cross-check)
  - Fallback 사용 시 = `event: canonical_json_fallback` ledger entry 작성 의무 (caller 책임)

본 모듈 = Hermes 의존 0 (ADR-008 차단조건 #2 답습) — POSIX + Python stdlib + provider-neutral PyPI 한정.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from enum import Enum
from typing import Any

try:
    import rfc8785  # Primary 1 (Trail of Bits)
except ImportError:
    rfc8785 = None  # type: ignore[assignment]

try:
    import jcs  # Primary 2 (titusz)
except ImportError:
    jcs = None  # type: ignore[assignment]


class CrossCheckMode(str, Enum):
    """Cross-check mode — Q1 합의 D-1 답습 (corpus 시점 강제 + runtime 호출자 결정).

    - PRIMARY_1_ONLY: rfc8785 단독 사용 (runtime 1× 권고)
    - PRIMARY_2_ONLY: jcs 단독 사용 (테스트/디버깅용)
    - CROSS_CHECK: rfc8785 + jcs 동시 호출, 출력 byte 동등성 + sha256 동등성 강제 (corpus 시점 권고)
    - FALLBACK_JQ: jq -S -c subprocess (Primary install 실패 시, canonical_json_fallback entry 의무)
    """

    PRIMARY_1_ONLY = "primary_1_only"
    PRIMARY_2_ONLY = "primary_2_only"
    CROSS_CHECK = "cross_check"
    FALLBACK_JQ = "fallback_jq"


class CanonicalizationError(Exception):
    """Canonical JSON 생성 실패 (NaN/Inf/cross-check mismatch 등)."""


class CrossCheckMismatchError(CanonicalizationError):
    """rfc8785 + jcs cross-check 출력 불일치 — TR-C-2 escalation trigger."""


@dataclass
class CanonicalResult:
    """Canonicalization 결과 + audit trail."""

    canonical: bytes
    sha256_hex: str
    mode_used: CrossCheckMode
    fallback_used: bool = False
    cross_check_passed: bool | None = None  # None = N/A, True/False = cross-check 결과


def _to_canonical_rfc8785(obj: Any) -> bytes:
    """Primary 1 — rfc8785 (Trail of Bits)."""
    if rfc8785 is None:
        raise CanonicalizationError("rfc8785 라이브러리 미설치 — `pip install rfc8785==0.1.4`")
    out = rfc8785.dumps(obj)
    return out if isinstance(out, bytes) else out.encode("utf-8")


def _to_canonical_jcs(obj: Any) -> bytes:
    """Primary 2 — jcs (titusz)."""
    if jcs is None:
        raise CanonicalizationError("jcs 라이브러리 미설치 — `pip install jcs==0.2.1`")
    out = jcs.canonicalize(obj)
    return out if isinstance(out, bytes) else out.encode("utf-8")


def _to_canonical_jq_fallback(obj: Any) -> bytes:
    """Fallback — jq -S -c subprocess.

    POSIX 표준 도구, ADR-012 §2.5 명시. 본 함수 호출 후 caller 는
    `event: canonical_json_fallback` ledger entry 작성 의무.
    """
    jq_path = shutil.which("jq")
    if jq_path is None:
        raise CanonicalizationError(
            "jq fallback 불가 — `jq` POSIX 도구 미설치 (apt install jq / brew install jq)"
        )
    input_json = json.dumps(obj, allow_nan=False).encode("utf-8")
    try:
        result = subprocess.run(
            [jq_path, "-S", "-c", "."],
            input=input_json,
            capture_output=True,
            check=True,
            timeout=30,
        )
    except subprocess.CalledProcessError as e:
        raise CanonicalizationError(
            f"jq fallback subprocess 실패 — rc={e.returncode} stderr={e.stderr.decode('utf-8', 'replace')[:200]}"
        ) from e
    out = result.stdout.rstrip(b"\n")
    return out


def to_canonical(obj: Any, mode: CrossCheckMode = CrossCheckMode.PRIMARY_1_ONLY) -> CanonicalResult:
    """Canonical JSON 생성 + audit trail.

    Args:
        obj: 입력 Python object (dict / list / str / int / float / bool / None)
        mode: CrossCheckMode (기본 PRIMARY_1_ONLY — rfc8785 단독, runtime 1× 권고)

    Returns:
        CanonicalResult (canonical bytes + sha256 hex + mode used + fallback/cross-check flag)

    Raises:
        CanonicalizationError: NaN/Inf reject 또는 라이브러리 미설치 또는 jq 실패
        CrossCheckMismatchError: CROSS_CHECK 모드에서 rfc8785 ↔ jcs 출력 불일치 (TR-C-2 trigger)
    """
    fallback_used = False
    cross_check_passed: bool | None = None

    if mode == CrossCheckMode.PRIMARY_1_ONLY:
        canonical = _to_canonical_rfc8785(obj)
    elif mode == CrossCheckMode.PRIMARY_2_ONLY:
        canonical = _to_canonical_jcs(obj)
    elif mode == CrossCheckMode.CROSS_CHECK:
        out_p1 = _to_canonical_rfc8785(obj)
        out_p2 = _to_canonical_jcs(obj)
        if out_p1 != out_p2:
            raise CrossCheckMismatchError(
                f"rfc8785 ↔ jcs cross-check 불일치 — TR-C-2 escalation. "
                f"rfc8785={out_p1[:80]!r} jcs={out_p2[:80]!r}"
            )
        canonical = out_p1
        cross_check_passed = True
    elif mode == CrossCheckMode.FALLBACK_JQ:
        canonical = _to_canonical_jq_fallback(obj)
        fallback_used = True
    else:
        raise CanonicalizationError(f"알 수 없는 mode: {mode}")

    sha256_hex = hashlib.sha256(canonical).hexdigest()
    return CanonicalResult(
        canonical=canonical,
        sha256_hex=sha256_hex,
        mode_used=mode,
        fallback_used=fallback_used,
        cross_check_passed=cross_check_passed,
    )


def _cli() -> int:
    """CLI — corpus 회귀 + cross-check + fallback 동등성 검증."""
    p = argparse.ArgumentParser(
        description="Canonical JSON (RFC 8785 JCS) — Group C PoC validator"
    )
    p.add_argument(
        "--mode",
        choices=[m.value for m in CrossCheckMode],
        default=CrossCheckMode.CROSS_CHECK.value,
        help="Cross-check mode (default: cross_check)",
    )
    p.add_argument(
        "--input",
        type=str,
        default="-",
        help="입력 JSON 파일 경로 (- = stdin)",
    )
    p.add_argument(
        "--expected-canonical",
        type=str,
        default=None,
        help="기대 canonical 출력 파일 (있으면 byte 비교)",
    )
    p.add_argument(
        "--expected-sha256",
        type=str,
        default=None,
        help="기대 sha256 hex 파일 (있으면 비교)",
    )
    p.add_argument(
        "--verify-fallback-equiv",
        action="store_true",
        help="jq fallback 출력과 byte 동등성 검증",
    )
    args = p.parse_args()

    try:
        if args.input == "-":
            input_text = sys.stdin.read()
        else:
            with open(args.input, "r", encoding="utf-8") as f:
                input_text = f.read()
        obj = json.loads(input_text)
    except (OSError, json.JSONDecodeError) as e:
        print(f"INPUT_ERROR: {e}", file=sys.stderr)
        return 2

    try:
        result = to_canonical(obj, mode=CrossCheckMode(args.mode))
    except CrossCheckMismatchError as e:
        print(f"CROSS_CHECK_MISMATCH: {e}", file=sys.stderr)
        return 3
    except CanonicalizationError as e:
        print(f"CANONICAL_ERROR: {e}", file=sys.stderr)
        return 4

    sys.stdout.buffer.write(result.canonical)
    sys.stdout.buffer.write(b"\n")
    print(
        f"# mode={result.mode_used.value} sha256={result.sha256_hex} "
        f"fallback_used={result.fallback_used} cross_check_passed={result.cross_check_passed}",
        file=sys.stderr,
    )

    rc = 0

    if args.expected_canonical:
        try:
            with open(args.expected_canonical, "rb") as f:
                expected = f.read().rstrip(b"\n")
        except OSError as e:
            print(f"EXPECTED_CANONICAL_READ_ERROR: {e}", file=sys.stderr)
            return 5
        if result.canonical != expected:
            print(
                f"CANONICAL_MISMATCH: got={result.canonical!r} expected={expected!r}",
                file=sys.stderr,
            )
            rc = 1

    if args.expected_sha256:
        try:
            with open(args.expected_sha256, "r", encoding="utf-8") as f:
                expected_hex = f.read().strip().split()[0]
        except OSError as e:
            print(f"EXPECTED_SHA256_READ_ERROR: {e}", file=sys.stderr)
            return 5
        if result.sha256_hex != expected_hex:
            print(
                f"SHA256_MISMATCH: got={result.sha256_hex} expected={expected_hex}",
                file=sys.stderr,
            )
            rc = 1

    if args.verify_fallback_equiv:
        try:
            fb_result = to_canonical(obj, mode=CrossCheckMode.FALLBACK_JQ)
            if fb_result.canonical != result.canonical:
                print(
                    f"FALLBACK_EQUIV_FAIL: primary={result.canonical[:80]!r} jq={fb_result.canonical[:80]!r}",
                    file=sys.stderr,
                )
                rc = 1
            else:
                print("# fallback equivalence: OK", file=sys.stderr)
        except CanonicalizationError as e:
            print(f"FALLBACK_VERIFY_ERROR: {e}", file=sys.stderr)
            rc = 1

    return rc


if __name__ == "__main__":
    sys.exit(_cli())
