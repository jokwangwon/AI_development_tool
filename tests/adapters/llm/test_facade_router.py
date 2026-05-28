"""SC-Provider Liquidity — facade complete() Router 위임 real (Core MVP, mock-verified) test.

TDD RED→GREEN. 합의 `docs/review/3plus1-consensus-2026-05-28-sc-provider-liquidity.md` 답습:
  - CB-1 model=alias (Router model_name) / CB-4 RT-1 T-A 양방향 (test_t6 대체)
  - CB-5 redaction 범위 messages+system / CB-6 set_verbose=False / CB-7 강등 감지 fail-loud
  - CB-8 lazy import hermetic / R-3 _normalize 속성접근 / R-5 validate_config 엣지케이스

hermetic: litellm 미설치 — Router 주입 fake + asyncio.run() (pytest-asyncio 의존 0, R-8 비례 대안).
"""
from __future__ import annotations

import asyncio
import sys
import types

import pytest

from src.adapters.llm.facade import (
    ConfigError,
    DegradedError,
    LLMFacade,
    LLMMetadata,
    LLMRequest,
    LLMResponse,
    to_router_config,
    validate_config,
)
from src.adapters.llm.redaction import RedactionFilter
from src.adapters.llm.redaction_patterns import REDACTION_MARK

# ── 공유 fixture 자료 ─────────────────────────────────────────────────────────

CFG_OK = {
    "routing": {"default": "anthropic-claude-api", "background_jobs": "ollama-llama-local"},
    "providers": {
        "anthropic-claude-api": {
            "type": "anthropic",
            "litellm_model": "anthropic/claude-opus-4-7",
            "auth_method": "api_key",
            "api_key_env": "ANTHROPIC_API_KEY",
            "status": "active",
        },
        "ollama-llama-local": {
            "type": "ollama",
            "litellm_model": "ollama/llama-3.3-70b",
            "auth_method": "none",
            "endpoint": "http://localhost:11434",
            "status": "active",
        },
    },
}


def _fake_response(content: str = "ok"):
    """litellm ModelResponse 형태 모사 — 속성 접근 (R-3, dict mock 금지)."""
    msg = types.SimpleNamespace(content=content)
    choice = types.SimpleNamespace(message=msg, finish_reason="stop")
    usage = types.SimpleNamespace(prompt_tokens=11, completion_tokens=22)
    return types.SimpleNamespace(choices=[choice], usage=usage, id="req-123")


class FakeRouter:
    """litellm.Router 주입 대체 — acompletion 인자 캡처 (속성 인터페이스)."""

    def __init__(self, *, raise_exc: Exception | None = None) -> None:
        self.received: dict = {}
        self._raise = raise_exc

    async def acompletion(self, *, model, messages, **opts):
        self.received = {"model": model, "messages": messages, "opts": opts}
        if self._raise is not None:
            raise self._raise
        return _fake_response()


# litellm 표준 예외 모사 (name 기반 감지 — hermetic)
class AuthenticationError(Exception):
    pass


class ServiceUnavailableError(Exception):
    pass


# ── T-A ⭐ (RT-1 양방향, CB-4 — test_t6 대체): Router 입력 = redacted output ──
def test_a_rt1_router_receives_redacted_messages_and_system() -> None:
    facade = LLMFacade(config=CFG_OK, redactor=RedactionFilter(), router=FakeRouter())
    req = LLMRequest(
        messages=[{"role": "user", "content": "my key sk-ant-LEAKSECRET1234567890 here"}],
        model_alias="default",
        system="system prompt API_KEY=sk-ant-SYSLEAK1234567890 trailing",
    )
    asyncio.run(facade.complete(req))
    sent = facade._router.received["messages"]  # type: ignore[attr-defined]
    blob = str(sent)
    # 양방향: 원본 secret 부재 AND REDACTION_MARK 존재 (한쪽만 = trap)
    assert "sk-ant-LEAKSECRET1234567890" not in blob
    assert "sk-ant-SYSLEAK1234567890" not in blob
    assert REDACTION_MARK in blob
    # system 이 redacted 된 채 messages 에 포함
    assert any(m.get("role") == "system" for m in sent)


# ── T-B (CB-1): model=alias(provider_key) + 정규화 (raw 누출 0) ───────────────
def test_b_router_model_is_alias_and_normalized_response() -> None:
    facade = LLMFacade(config=CFG_OK, router=FakeRouter())
    resp = asyncio.run(
        facade.complete(LLMRequest(messages=[{"role": "user", "content": "hi"}], model_alias="default"))
    )
    # CB-1: Router 가 받은 model = routing 해소 alias(=model_name), litellm_model 아님
    assert facade._router.received["model"] == "anthropic-claude-api"  # type: ignore[attr-defined]
    assert facade._router.received["model"] != "anthropic/claude-opus-4-7"  # type: ignore[attr-defined]
    # 정규화: LLMResponse(content, usage, LLMMetadata) — 속성접근, raw 누출 0
    assert isinstance(resp, LLMResponse)
    assert resp.content == "ok"
    assert resp.usage == {"input_tokens": 11, "output_tokens": 22}
    assert isinstance(resp.metadata, LLMMetadata)
    assert resp.metadata.provider_used == "anthropic-claude-api"
    assert resp.metadata.finish_reason == "stop"
    assert resp.metadata.request_id == "req-123"


# ── T-C (R-5): validate_config fail-fast 엣지케이스 ───────────────────────────
def test_c_validate_config_failfast() -> None:
    # active 1개 → Min 2 위반
    with pytest.raises(ConfigError, match="Min 2"):
        validate_config({"providers": {"a": {"type": "anthropic", "status": "active"}}})
    # 동일 type 2개 active 금지
    with pytest.raises(ConfigError, match="동일 type"):
        validate_config(
            {
                "providers": {
                    "a": {"type": "anthropic", "status": "active"},
                    "b": {"type": "anthropic", "status": "active"},
                }
            }
        )
    # type 필드 누락
    with pytest.raises(ConfigError, match="type 필드 누락"):
        validate_config(
            {"providers": {"a": {"status": "active"}, "b": {"type": "ollama", "status": "active"}}}
        )


# ── T-D: 정상 2 active 다른 type → pass ───────────────────────────────────────
def test_d_validate_config_ok() -> None:
    validate_config(CFG_OK)  # 예외 0


# ── T-E (CB-7): 런타임 강등 감지 fail-loud ────────────────────────────────────
def test_e_runtime_degradation_failloud() -> None:
    # 2 active 중 1개 auth 실패 → remaining active < 2 → DegradedError + stderr
    facade = LLMFacade(config=CFG_OK, router=FakeRouter(raise_exc=AuthenticationError("401")))
    with pytest.raises(DegradedError, match="차단조건 #5"):
        asyncio.run(facade.complete(LLMRequest(messages=[{"role": "user", "content": "x"}])))


def test_e2_degradation_reraise_when_spare_active() -> None:
    # 3 active → 1개 실패해도 remaining 2 ≥ 2 → 원 예외 re-raise (DegradedError 아님)
    cfg = {
        "routing": {"default": "p1"},
        "providers": {
            "p1": {"type": "anthropic", "litellm_model": "anthropic/x", "status": "active"},
            "p2": {"type": "ollama", "litellm_model": "ollama/y", "status": "active"},
            "p3": {"type": "openai", "litellm_model": "openai/z", "status": "active"},
        },
    }
    facade = LLMFacade(config=cfg, router=FakeRouter(raise_exc=ServiceUnavailableError("503")))
    with pytest.raises(ServiceUnavailableError):
        asyncio.run(facade.complete(LLMRequest(messages=[{"role": "user", "content": "x"}], model_alias="default")))


# ── T-F (D2/D3): LLMRequest/LLMMetadata frozen 화이트리스트 ────────────────────
def test_f_dataclass_whitelist_frozen() -> None:
    req = LLMRequest(messages=[{"role": "user", "content": "hi"}], model_alias="default", metadata_in={"x": 1})
    assert req.model_alias == "default"
    meta = LLMMetadata(provider_used="p", fallback_chain=["p"], finish_reason="stop")
    with pytest.raises(Exception):  # frozen — 변경 불가
        meta.provider_used = "q"  # type: ignore[misc]
    # 화이트리스트 외 키 거부
    with pytest.raises(TypeError):
        LLMMetadata(provider_used="p", fallback_chain=[], finish_reason="s", raw="leak")  # type: ignore[call-arg]


# ── T-G (D6/CB-1): to_router_config model_name=alias + api_key 보간 ───────────
def test_g_to_router_config_model_name_is_alias(monkeypatch) -> None:
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-ant-REALKEY")
    rc = to_router_config(CFG_OK)
    entries = {e["model_name"]: e for e in rc["model_list"]}
    # model_name = provider key(alias), litellm_params.model = litellm_model
    assert "anthropic-claude-api" in entries
    assert entries["anthropic-claude-api"]["litellm_params"]["model"] == "anthropic/claude-opus-4-7"
    assert entries["anthropic-claude-api"]["litellm_params"]["api_key"] == "sk-ant-REALKEY"
    # ollama auth_method=none → endpoint(api_base)만, api_key 0
    assert entries["ollama-llama-local"]["litellm_params"]["api_base"] == "http://localhost:11434"
    assert "api_key" not in entries["ollama-llama-local"]["litellm_params"]


# ── T-H (CB-8 hermetic): litellm 미설치에서 facade 동작 + import 0 ────────────
def test_h_hermetic_no_litellm_import() -> None:
    sys.modules.pop("litellm", None)
    facade = LLMFacade(config=CFG_OK, router=FakeRouter())
    asyncio.run(facade.complete(LLMRequest(messages=[{"role": "user", "content": "hi"}])))
    # 주입 경로 = litellm import 0 (top-level 회귀 시 RED)
    assert "litellm" not in sys.modules


# ── T-I (CB-6): _build_router 가 litellm.set_verbose=False 설정 ───────────────
def test_i_build_router_disables_litellm_verbose(monkeypatch) -> None:
    fake_litellm = types.ModuleType("litellm")
    fake_litellm.set_verbose = True  # type: ignore[attr-defined]

    class _Router:
        def __init__(self, **kw):
            self.kw = kw

    fake_litellm.Router = _Router  # type: ignore[attr-defined]
    monkeypatch.setitem(sys.modules, "litellm", fake_litellm)

    facade = LLMFacade(config=CFG_OK)  # router=None → lazy build
    router = facade._build_router()  # type: ignore[attr-defined]
    assert fake_litellm.set_verbose is False  # CB-6 내장 로깅 비활성
    # model_list 가 Router 에 전달 (model_name=alias)
    names = {e["model_name"] for e in router.kw["model_list"]}
    assert names == {"anthropic-claude-api", "ollama-llama-local"}


# ── T-K (R-2): health() 축소 fallback — dict[str, bool] ───────────────────────
def test_k_health_reduced_fallback() -> None:
    facade = LLMFacade(config=CFG_OK, router=FakeRouter())
    h = asyncio.run(facade.health())
    assert isinstance(h, dict)
    assert h == {"anthropic-claude-api": True, "ollama-llama-local": True}
