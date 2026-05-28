"""SC-1 (65 entry) RedactionFilter test — R-2 GP-2 prevention 송신 redaction.

TDD RED→GREEN. 합의 `docs/review/3plus1-consensus-2026-05-28-mvp2-sc1.md` 답습:
  - B-2 group-aware 치환 (값만 마스킹, key명/JSON 구조 보존)
  - R-1 원본 불변성 / R-2 false positive edge case / R-4 spy redactor / B-1 equivalence
"""
from __future__ import annotations

import pytest

from src.adapters.llm.facade import LLMFacade, LLMRequest
from src.adapters.llm.redaction import RedactionFilter
from src.adapters.llm.redaction_patterns import ALL_PATTERNS, REDACTION_MARK


@pytest.fixture
def rf() -> RedactionFilter:
    return RedactionFilter()


# ── T-1: redact_text — secret 값 마스킹 (prefix = whole, key명 없음) ──────────
def test_t1_redact_text_prefix_token(rf: RedactionFilter) -> None:
    out = rf.redact_text("use sk-ant-ABCDEFGHIJ1234567890 now")
    assert "sk-ant-ABCDEFGHIJ1234567890" not in out
    assert REDACTION_MARK in out
    assert "use" in out and "now" in out  # 주변 문맥 보존


# ── T-2: redact_messages — content secret 값 redacted, key=구조 보존 ──────────
def test_t2_redact_messages_env_assignment(rf: RedactionFilter) -> None:
    msgs = [{"role": "user", "content": "config: API_KEY=sk-ant-SECRETVALUE123456 done"}]
    out = rf.redact_messages(msgs)
    content = out[0]["content"]
    assert "sk-ant-SECRETVALUE123456" not in content
    assert REDACTION_MARK in content
    assert "API_KEY" in content  # key명 보존 (group-aware)
    assert out[0]["role"] == "user"  # 구조 보존


# ── T-3: Tier-1 45 catalog 대표 패턴 (baseline/prefix/regex/alternation) ──────
@pytest.mark.parametrize(
    "secret",
    [
        "ghp_ABCDEFGHIJ1234567890",  # BL-3 prefix-baseline
        "gho_ABCDEFGHIJ1234567890",  # T1-002 prefix
        'token: "sk_live_ABCDEFGHIJ1234"',  # T1-033 JSON regex (group)
        "https://example.com/cb?access_token=eyJsecretvalue123",  # T1-041 alternation
    ],
)
def test_t3_catalog_representative_patterns(rf: RedactionFilter, secret: str) -> None:
    out = rf.redact_text(secret)
    assert REDACTION_MARK in out
    # secret 고유 값 (raw alphanum 시퀀스)이 평문 노출 0
    for leak in ("ABCDEFGHIJ1234567890", "sk_live_ABCDEFGHIJ1234", "eyJsecretvalue123"):
        if leak in secret:
            assert leak not in out


# ── T-4: false positive edge case — 정상 코드/텍스트 무변경 (R-2) ─────────────
@pytest.mark.parametrize(
    "benign",
    [
        "items.sort(key=lambda x: x.name)",  # paren delimiter — 매칭 0 (codex N-4)
        "import keyboard",
        "def f(monkeypatch): pass",
        "url = '/search?page=1&limit=20'",  # sensitive key 아님
        "the secret garden was lovely",  # 'secret' 단어 but =value 아님
    ],
)
def test_t4_false_positive_benign_unchanged(rf: RedactionFilter, benign: str) -> None:
    assert rf.redact_text(benign) == benign


# ── T-5: scrub dict 재귀 + KEY_BLACKLIST + 구조 무결성 ────────────────────────
def test_t5_scrub_dict_key_blacklist_and_structure(rf: RedactionFilter) -> None:
    obj = {
        "api_key": "sk-ant-DEEPSECRET1234567890",
        "user": "alice",
        "nested": {"token": "ghp_NESTEDSECRET12345", "count": 3},
    }
    out = rf.scrub(obj)
    # KEY_BLACKLIST: api_key/token 값 마스킹
    assert out["api_key"] == REDACTION_MARK
    assert out["nested"]["token"] == REDACTION_MARK
    # 구조 무결성: 비밀 아닌 key/값 보존
    assert out["user"] == "alice"
    assert out["nested"]["count"] == 3
    assert set(out.keys()) == {"api_key", "user", "nested"}


# ── T-6: facade complete() redaction 선행 (spy) + Router deferred ─────────────
def test_t6_facade_redaction_before_router_deferred() -> None:
    calls: list[str] = []

    class SpyRedactor:
        def redact_messages(self, messages):
            calls.append("redact_messages")
            return messages

        def scrub(self, obj):
            calls.append("scrub")
            return obj

    facade = LLMFacade(registry_path="dummy", redactor=SpyRedactor())
    req = LLMRequest(alias="agent_a", messages=[{"role": "user", "content": "hi"}])
    with pytest.raises(NotImplementedError):
        facade.complete(req)
    # redaction 이 Router deferred (NotImplementedError) *전* 호출됨
    assert "redact_messages" in calls


# ── T-7: 원본 불변성 — redact_messages in-place mutate 0 (R-1) ────────────────
def test_t7_redact_messages_no_inplace_mutation(rf: RedactionFilter) -> None:
    original = [{"role": "user", "content": "API_KEY=sk-ant-MUTATETEST1234567"}]
    snapshot = "API_KEY=sk-ant-MUTATETEST1234567"
    out = rf.redact_messages(original)
    assert original[0]["content"] == snapshot  # 입력 불변
    assert out is not original
    assert out[0]["content"] != snapshot  # 출력은 redacted


# ── T-8: equivalence — catalog single source 45 patterns (B-1) ────────────────
def test_t8_catalog_equivalence_45_patterns() -> None:
    assert len(ALL_PATTERNS) == 45
    ids = [p[0] for p in ALL_PATTERNS]
    assert len(set(ids)) == 45  # id 중복 0
    assert ids[:5] == ["BL-1", "BL-2", "BL-3", "BL-4", "BL-5"]
