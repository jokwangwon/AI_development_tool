"""provider_import_scanner — facade allow-path (MT-1~MT-5) 단위 검증.

답습: docs/review/3plus1-consensus-2026-05-29-facade-scanner.md (3+1 합의 APPROVE WITH CONDITIONS)
  - MT-1: litellm 토큰 한정 면제 (정확 경로 × litellm만, glob/디렉터리 금지).
  - MT-2: 정확 경로 매칭(repo-root 상대 posix).
  - MT-3: 동적 import(importlib/__import__) 경유 litellm 은 facade 내라도 면제 제외.
  - MT-4: 음성 회귀 3종 — facade+openai→FAIL, facade외+litellm→FAIL, facade+litellm→PASS.
  - MT-5: fixture(facade_only.py)가 white-list 경로 밖이라 allow 검증 불가 → 본 단위 테스트가 oracle.
  - 배경: facade.py litellm lazy import = ADR-009 §2.2 #1 Provider Liquidity 단일 통로,
    import-linter 는 이미 ignore. scanner 만 facade 예외 누락이었음(SDD 명세 §2.4/§9.3 미구현).
"""
from __future__ import annotations

from pathlib import Path

from tools.provider_import_scanner import scan_file, scan_source

FACADE = "src/adapters/llm/facade.py"  # white-list 단일 통로
NON_FACADE = "src/adapters/llm/router.py"  # facade 아님


def _tokens(violations, detail):
    return [v for v in violations if v.detail == detail]


# --- MT-4 음성 3종 ---
def test_facade_litellm_direct_passes():
    v = scan_source("import litellm\n", FACADE)
    assert _tokens(v, "litellm") == []  # facade litellm 통로 면제


def test_facade_litellm_from_passes():
    v = scan_source("from litellm import Router\n", FACADE)
    assert _tokens(v, "litellm") == []


def test_facade_openai_still_fails():
    # MT-1 토큰 한정: facade 라도 litellm 외 provider 는 계속 검출
    v = scan_source("import openai\n", FACADE)
    assert _tokens(v, "openai")


def test_non_facade_litellm_fails():
    # facade 밖 litellm direct 는 여전히 위반
    v = scan_source("import litellm\n", NON_FACADE)
    assert _tokens(v, "litellm")


# --- MT-3 동적 import 면제 제외 ---
def test_facade_dynamic_litellm_not_exempt():
    src = "import importlib\nimportlib.import_module('litellm')\n"
    v = scan_source(src, FACADE)
    assert _tokens(v, "litellm")  # 정적 lazy 만 면제, 동적은 검출


def test_facade_dunder_litellm_not_exempt():
    v = scan_source("__import__('litellm')\n", FACADE)
    assert _tokens(v, "litellm")


# --- 실제 facade.py 회귀 (PR #3 BLOCK 원인 해소 증명) ---
def test_real_facade_litellm_no_direct_violation():
    v = scan_file(Path(FACADE))
    assert [x for x in v if x.detail == "litellm" and x.pattern == "direct-import"] == []


# --- 기존 fail fixture 회귀 (방어 손실 0) ---
def test_existing_fail_fixtures_still_detected():
    base = Path("tests/fixtures/provider_adapter_enforcement/fail")
    for name in ["direct_import", "from_import", "dynamic_importlib", "double_underscore_import"]:
        assert scan_file(base / f"{name}.py"), f"{name} 위반이 여전히 검출돼야 함"
