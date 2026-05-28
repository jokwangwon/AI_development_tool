"""LLMFacade — Provider-agnostic facade (G2 GP-5, Provider Liquidity 5조-2).

본 파일은 *유일하게* LiteLLM 직접 import 가 *허용되는 경로* 입니다
(`llm-providers-design.md` §4.1 + ADR-009 §2.2 #1 답습). import 는 `_build_router()`
함수 내부 lazy import — litellm 미설치 환경에서도 facade import + Router 주입 테스트가
hermetic 하게 동작 (CB-8). import-linter `ignore_imports = facade -> *` 로 계약 PASS.

SC-Provider Liquidity (69 entry): **facade `complete()` Router 위임 real (Core MVP, mock-verified)** —
65 SC-1 의 redaction layer real 위에 LiteLLM Router 위임을 실배선. RT-1: redaction 은
Router 위임 *전* 위치 (송신 secret strip, 미부착 window 0).

답습 출처:
  - docs/architecture/llm-providers-design.md §3(registry) / §4(facade) / §5(Router 위임) / §6(Min 2)
  - docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md §2.2 (facade 단일 진입점 6 의무)
  - docs/decisions/ADR-008-hermes-adoption-decision.md #4(단일 facade) / #5(Min 2)
  - docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md (v1.1)
  - docs/review/3plus1-consensus-2026-05-28-sc-provider-liquidity.md (BLOCKING 8 흡수)

scope (Core MVP): complete() + validate_config + 런타임 강등 감지(fail-loud) + 응답 정규화.
deferred (명세 존속): streaming / OAuth single-flight / degraded 모드·자동복구·UI / metrics callback / 폴백 race 완화.
"""
from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from typing import Any

from src.adapters.llm.redaction import RedactionFilter


class ConfigError(Exception):
    """registry 검증 실패 (Min 2 active / 동일 type / 필드 누락) — 시작 시 fail-fast."""


class DegradedError(Exception):
    """런타임 강등 감지 — active provider 실패로 always-on(≥2) 침해 (CB-7 fail-loud)."""


# litellm 표준 예외 = name 기반 감지 (hermetic — litellm import 0)
_DEGRADATION_EXC_NAMES = frozenset({"AuthenticationError", "ServiceUnavailableError"})


@dataclass(frozen=True)
class LLMRequest:
    messages: list[dict[str, Any]]
    model_alias: str = "default"
    system: str | None = None
    temperature: float = 0.7
    max_tokens: int = 4096
    tools: list[dict[str, Any]] | None = None
    tool_choice: dict[str, Any] | str | None = None
    response_format: dict[str, Any] | None = None
    stop_sequences: list[str] | None = None
    metadata_in: dict[str, Any] | None = None  # Core MVP: 미전달 (metrics callback deferred)


@dataclass(frozen=True)
class LLMMetadata:
    """화이트리스트 키만 (위반패턴 #2/#4 — raw provider 메타 누출 차단)."""

    provider_used: str
    fallback_chain: list[str]
    finish_reason: str
    request_id: str | None = None


@dataclass(frozen=True)
class LLMResponse:
    content: str
    usage: dict[str, Any]
    metadata: LLMMetadata


def validate_config(config: dict[str, Any]) -> None:
    """시작 시 fail-fast: Min 2 active + 동일 type 금지 + 필드 누락 (§3.3/§6.1, R-5)."""
    providers = config.get("providers") or {}
    active = [(k, v) for k, v in providers.items() if v.get("status") == "active"]
    if len(active) < 2:
        raise ConfigError(f"Min 2 active 위반 (active={len(active)}) — ADR-008 #5")
    types = [v.get("type") for _, v in active]
    if None in types:
        raise ConfigError("active provider type 필드 누락 — registry 정합성")
    if len(set(types)) != len(types):
        raise ConfigError(f"동일 type 2개 active 금지 (정전 동시 실패 회피) — R5 (types={types})")


def to_router_config(config: dict[str, Any]) -> dict[str, Any]:
    """llm-providers.yaml → LiteLLM Router model_list (CB-1: model_name = provider alias).

    litellm_model 은 litellm_params.model 내부에만 존재 (complete() 호출 경로 노출 0,
    위반패턴 #1 회피). api_key_env → os.environ 실값 보간 (R-12 — litellm 은 실값 기대).
    """
    providers = config["providers"]
    model_list: list[dict[str, Any]] = []
    for alias, p in providers.items():
        params: dict[str, Any] = {"model": p["litellm_model"]}
        env = p.get("api_key_env")
        if env:
            params["api_key"] = os.environ.get(env)
        if p.get("endpoint"):
            params["api_base"] = p["endpoint"]
        model_list.append({"model_name": alias, "litellm_params": params})
    return {"model_list": model_list}


class LLMFacade:
    """LLM 호출 단일 진입점. Router 위임 real (Core MVP). litellm import = 본 파일 한정."""

    def __init__(
        self,
        config_path: str | None = None,
        *,
        config: dict[str, Any] | None = None,
        redactor: RedactionFilter | None = None,
        router: Any | None = None,
    ) -> None:
        if config is None:
            if config_path is None:
                raise ConfigError("config 또는 config_path 필요")
            config = self._load_config(config_path)
        validate_config(config)
        self._config = config
        self._providers: dict[str, Any] = config["providers"]
        self._routing: dict[str, str] = config.get("routing", {})
        self._redactor: RedactionFilter = redactor if redactor is not None else RedactionFilter()
        self._router = router  # None → lazy build (litellm import 시점)

    @staticmethod
    def _load_config(path: str) -> dict[str, Any]:
        import yaml  # stdlib 외 (forbidden 아님)

        with open(path, encoding="utf-8") as f:
            return yaml.safe_load(f)

    def _build_router(self) -> Any:
        import litellm  # lazy — facade 한정 (ADR-009 §2.2 #1, import-linter ignore)

        litellm.set_verbose = False  # CB-6: 내장 로깅 비활성 (응답/요청 stdout 누출 차단)
        rc = to_router_config(self._config)
        return litellm.Router(model_list=rc["model_list"], num_retries=3, timeout=30)

    def _get_router(self) -> Any:
        if self._router is None:
            self._router = self._build_router()
        return self._router

    def _resolve(self, model_alias: str) -> str:
        """routing alias → provider key (= model_list model_name, CB-1)."""
        if model_alias in self._routing:
            return self._routing[model_alias]
        if model_alias in self._providers:
            return model_alias
        return self._routing.get("default") or next(iter(self._providers))

    def _redact_request(self, request: LLMRequest) -> dict[str, Any]:
        """송신 전 redaction (RT-1, CB-5 범위 = messages + system). Router 위임 전 호출."""
        messages = self._redactor.redact_messages(request.messages)
        if request.system:
            redacted_system = self._redactor.redact_text(request.system)
            messages = [{"role": "system", "content": redacted_system}, *messages]
        return {"messages": messages}

    def _build_opts(self, request: LLMRequest) -> dict[str, Any]:
        opts: dict[str, Any] = {"temperature": request.temperature, "max_tokens": request.max_tokens}
        if request.tools:
            opts["tools"] = self._redactor.scrub(request.tools)  # CB-5 outbound text
        if request.tool_choice is not None:
            opts["tool_choice"] = request.tool_choice
        if request.response_format is not None:
            opts["response_format"] = request.response_format
        if request.stop_sequences:
            opts["stop"] = request.stop_sequences
        return opts

    def _active_keys(self) -> list[str]:
        return [k for k, v in self._providers.items() if v.get("status") == "active"]

    def _on_provider_failure(self, failed_key: str) -> bool:
        """런타임 강등 감지 (CB-7 fail-loud). 실패한 provider 제외 active < 2 → True + stderr.

        degraded *모드*/자동복구/UI/timer 는 deferred — 감지+fail-loud 만 (차단조건 #5 부분 충족).
        """
        remaining = [k for k in self._active_keys() if k != failed_key]
        if len(remaining) < 2:
            sys.stderr.write(
                f"[DEGRADED] active provider '{failed_key}' 실패 — remaining active "
                f"{len(remaining)} < 2 (차단조건 #5 always-on 침해 — fail-loud)\n"
            )
            return True
        return False

    async def complete(self, request: LLMRequest) -> LLMResponse:
        provider_key = self._resolve(request.model_alias)
        # RT-1: 송신 전 redaction (Router 위임 전 — 미부착 window 0)
        redacted = self._redact_request(request)
        router = self._get_router()
        try:
            raw = await router.acompletion(
                model=provider_key,  # CB-1: alias(=model_name), litellm_model 아님
                messages=redacted["messages"],
                **self._build_opts(request),
            )
        except Exception as exc:
            if type(exc).__name__ in _DEGRADATION_EXC_NAMES and self._on_provider_failure(provider_key):
                raise DegradedError(
                    f"런타임 강등 — '{provider_key}' 실패 후 active < 2 (차단조건 #5)"
                ) from exc
            raise
        return self._normalize(raw, provider_key)

    def _normalize(self, raw: Any, provider_key: str) -> LLMResponse:
        """LiteLLM ModelResponse(OpenAI 포맷 통일) → LLMResponse. 속성 접근 (R-3), raw 누출 0 (R-4)."""
        choice = raw.choices[0]
        content = choice.message.content
        finish_reason = getattr(choice, "finish_reason", "stop")
        usage_obj = getattr(raw, "usage", None)
        usage = {
            "input_tokens": getattr(usage_obj, "prompt_tokens", None),
            "output_tokens": getattr(usage_obj, "completion_tokens", None),
        }
        metadata = LLMMetadata(
            provider_used=provider_key,
            fallback_chain=[provider_key],
            finish_reason=finish_reason,
            request_id=getattr(raw, "id", None),
        )
        return LLMResponse(content=content, usage=usage, metadata=metadata)

    async def health(self) -> dict[str, bool]:
        """축소 fallback (R-2): active alias + config 검증 결과 (dry probe 실배선 deferred, §9.2 명세 존속)."""
        return {alias: True for alias in self._active_keys()}
