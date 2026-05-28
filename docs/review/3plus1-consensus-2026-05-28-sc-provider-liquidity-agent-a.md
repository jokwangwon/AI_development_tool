# 3+1 합의 — SC-Provider Liquidity (facade Router 위임 real, core `complete()` 경로) — Agent A (구현 분석가)

> **작성**: 2026-05-28 (세션 #4, 69번째 entry 진입 cycle)
> **Agent**: A — 구현 분석가 ("실제로 동작하는가?")
> **lens**: 기술적 구현 가능성 / 의존성 / 성능 / 실현가능성
> **독립성**: Phase 2 독립 분석 — Agent B/C/codex 결론 미참조. 직접 filesystem read + 실행 근거만.
> **검토 대상**: `docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md` (v1, §0~§14)

---

## 0. 판정

**APPROVE WITH CONDITIONS**

brief v1의 D1~D8 + RT-1 + hermetic 전략은 구현 실현가능성이 **높다**. 핵심 가설 4건을 직접 실행으로 입증:

1. **D1 (async 전환)**: `grep -rn "\.complete(" src/` → **0 match** (실 caller 0 확인). async breaking 위험 = 사실상 0.
2. **D4 (lazy import + hermetic)**: litellm 미설치 확인 + grimp가 함수-레벨 lazy import를 facade 모듈에 정확히 귀속 + lazy import는 *모듈 import 시점* 미발화(*호출 시점*만) → **hermetic 테스트 실현 입증**.
3. **import-linter 경계**: lazy import도 `src.adapters.llm.facade -> *` ignore rule로 계약 PASS (grimp 그래프 직접 검증).
4. **성능**: redaction 45 패턴 = **0.193ms/call** (~250 word) → 네트워크 LLM latency 대비 무시 가능.

단, **BLOCKING 3건** (아래 §1) 해소가 GREEN 진입 전제. 모두 구현 *세부 명세* 정정이며 설계 본질 변경 아님 → APPROVE WITH CONDITIONS.

---

## 1. BLOCKING 항목 (GREEN 진입 전 해소 필수)

### B-A1. ⭐ `complete()`의 Router `acompletion(model=)` 인자 = **alias** 여야 함 (brief §6.2가 `litellm_model` 명시 → 설계 §5.1과 모순)

- **근거**:
  - brief line 186: `raw = await self._router.acompletion(model=litellm_model, messages=redacted["messages"], ...)` — `litellm_model`(예: `anthropic/claude-opus-4-7`)을 `model=`로 전달.
  - 설계 `llm-providers-design.md` line 341~344: `to_router_config`에서 `"model_name": alias` (예: `anthropic-claude-api`), `litellm_params.model: litellm_model`. 즉 **Router `model_list`의 키 = alias**.
- **문제**: LiteLLM `Router.acompletion(model=...)`은 `model_list`에 등록된 **`model_name`(=alias)으로 라우팅**한다. `litellm_model`을 직접 넘기면 (a) `model_list` 매칭 실패로 Router의 fallback/retry/cooldown 라우팅 메커니즘 우회 또는 (b) Router가 unknown model로 직접 호출 → 위반 패턴 #1(모델명 직접 사용)에 근접. 어느 쪽이든 D6 `to_router_config`의 alias 기반 라우팅이 무력화.
- **요구**: §6.2 flow line 186을 `acompletion(model=alias, ...)` 또는 `model=provider_key`(routing이 해소한 model_name)로 정정. brief §6.2 line 184~187의 `provider_key = routing[req.model_alias]` → 그 `provider_key`(=model_name=alias)를 `acompletion(model=...)`에 전달하는 것으로 일원화. `litellm_model`은 `to_router_config` 내부에서만 등장(Router 설정 시점), `complete()` 호출 경로에는 노출 0.
- **영향**: T-G(`to_router_config` model_list 구성) + T-B(정상 경로) 테스트가 이 정정을 반영해야 함. fake Router 주입 시에도 fake가 받는 `model` 인자 = alias임을 단언하는 것이 라우팅 정합성 증거.

### B-A2. T-6 기존 테스트 회귀 — `NotImplementedError` 의존 + `LLMRequest(alias=)` 동시 깨짐 (brief가 RT-3/D2에서 line 105만 언급, T-6 *동작* 깨짐 누락)

- **근거**:
  - `tests/adapters/llm/test_redaction_filter.py:92~109` (T-6 `test_t6_facade_redaction_before_router_deferred`):
    - line 105: `req = LLMRequest(alias="agent_a", messages=[...])` → D2 rename(`alias`→`model_alias`) 시 **TypeError**.
    - line 106~107: `with pytest.raises(NotImplementedError): facade.complete(req)` → 본 cycle이 `NotImplementedError`를 제거하고 Router 위임 real로 만들면 **이 단언 자체가 깨짐**. Router 주입이 없으면 `complete()`가 `_build_router()` → `import litellm` → `ModuleNotFoundError`(litellm 미설치), 주입되면 정상 반환 → 어느 쪽도 `NotImplementedError` 아님.
  - line 95~101 `SpyRedactor`는 `redact_messages`/`scrub`만 제공 → async `acompletion` 미보유. 본 cycle에서 `complete()`가 router를 호출하면 이 spy 단독으로는 부족.
- **문제**: brief §0.2(7) "65 SC-1 RedactionFilter 패턴 *내용* 변경 0"은 지켰으나, **T-6은 facade `complete()`의 deferred 동작을 검증하는 테스트**이므로 본 cycle 산출과 *필연적으로 충돌*. brief D2/RT-3는 line 105의 `alias=` rename만 언급하고 **T-6의 `pytest.raises(NotImplementedError)` 단언 폐기/이전을 명시 누락**.
- **요구**: T-6를 (a) 신규 T-A(RT-1, fake Router로 redacted body 동치 검증)로 *대체* 하거나 (b) `model_alias=` + fake Router 주입 + `NotImplementedError` 단언 제거로 *갱신*. §8.2 GREEN 단계에서 명문화. (brief E-4 "65 RedactionFilter 15 test 회귀 0"은 **T-1~T-5,T-7,T-8 = redaction *순수 함수* test 회귀 0**으로 범위 축소 정정 필요 — T-6은 facade 결합 test이므로 갱신 대상이지 "회귀 0" 대상 아님.)

### B-A3. `_redact_request`의 `metadata` 산출물이 `complete()` Router 위임 경로에서 사용처 미정의 (현 facade.py:44~51 + 설계 `metadata_in` rename 충돌)

- **근거**:
  - 현 `facade.py:44~51` `_redact_request`는 `{"messages": ..., "metadata": redactor.scrub(request.metadata)}` 반환. 현 `LLMRequest.metadata`(facade.py:28).
  - 설계 §4.1 line 217: 필드명은 `metadata_in`(요청 메타). brief D2 line 79 권고 필드 목록은 `metadata`(rename 방향 미고정 — 설계는 `metadata_in`, brief는 `metadata`).
  - brief §6.2 flow(line 184~188)는 `redacted["messages"]`만 `acompletion`에 전달 → **`redacted["metadata"]`의 행선지가 명세에 없음**. LiteLLM `acompletion`의 `metadata=` 파라미터(로깅/콜백용)로 전달할지, 버릴지, request_id 추출용인지 미정.
- **문제**: redaction된 metadata가 (a) Router로 전달 안 되면 `_redact_request`의 metadata scrub은 *dead path*(redaction은 했으나 사용 0) — RT-1 "미부착 window 0"의 *완결성*에 모호함. (b) 전달한다면 어느 파라미터로? 미정 시 GREEN 구현이 임의 결정 → 합의 우회.
- **요구**: §6.2에 `redacted["metadata"]`의 처리 명시 — Core MVP에서 (권고) **request_id만 추출하여 LLMMetadata로, 나머지는 LiteLLM `acompletion(metadata=)` 미전달**(콜백 deferred이므로 metadata sink 0) 또는 명시적 drop. + `LLMRequest` 필드명을 `metadata` vs `metadata_in` 중 하나로 고정(설계 §17 folding에서 설계 line 217 정정 여부 결정).

---

## 2. 권고 항목 (구현 품질 — 비차단)

### R-A1. `to_router_config`의 `api_key_env` → 실 키 보간 메커니즘 명시
- 설계 line 343 `litellm_params`에 `"api_key_env"`를 그대로 넣는 예시이나, **LiteLLM은 `api_key`(실 값) 또는 `os.environ` 참조를 기대** — `api_key_env`라는 키를 LiteLLM이 자동 해석하지 않음. Core MVP에서 `api_key=os.environ.get(provider["api_key_env"])` 보간을 `to_router_config` 내부에 명시. (auth_method=none인 ollama는 endpoint만, api_key 생략.) 실 키 부재 시(brief line 101) → Router 구성은 성공하되 호출 시 AuthenticationError(D7 경로) — mock 테스트는 무영향.

### R-A2. D8 `health()` dry probe = brief의 축소 fallback 채택 권고
- 설계 line 283 `self._router.health_check(dry=True)` 및 line 576~585 per-alias 루프 — **LiteLLM Router의 `health_check` 공개 API 형태/시그니처를 본 환경에서 실측 불가**(litellm 미설치, 호출 검증 deferred). brief §2 D8 line 108 + RT-6의 축소 fallback("active alias 목록 + 설정 검증 결과 반환")이 실현가능성 측면에서 **타당** — 실 API 형태 불명 상태로 dry probe를 강제하면 GREEN이 막힘(RT-6). Core MVP는 축소 fallback 채택, 실 health API 검증은 deferred로 명문화 권고.

### R-A3. runtime manifest 형식 = `requirements.txt`(runtime) 신설 권고 (pyproject 신설보다 비례적)
- `requirements-dev.txt`는 dev-dep 전용이며 "runtime 의존성 0건 / pyproject 신설 별도 합의" 명문(읽음). 본 cycle이 첫 runtime dep. **개인 툴 비례성**([[feedback_proportionate_security_personal_tool]]) 측면에서 `pyproject.toml [project] dependencies` 신설(PEP 621 빌드 메타 전반 도입)은 본 cycle 범위 대비 과대 — `requirements.txt`(runtime) 단일 파일 신설 + litellm 정확 핀 + (가능 시)`--require-hashes` 매니페스트가 더 비례적. hash 적용은 P11 (ii) "가능 범위"로 — litellm 의존성 트리가 크면 전체 hash pin이 무거우므로 litellm 직접 핀 우선, transitive hash는 best-effort.

### R-A4. T-H(hermetic) 검증을 자동 게이트로 — `sys.modules`에 litellm 부재 단언
- D4를 본 환경에서 실증(`/tmp/lazytest`): 함수-레벨 lazy import는 모듈 import 시 미발화. **T-H를 단순 "facade import 성공"이 아니라 `import facade; assert 'litellm' not in sys.modules` + fake router 주입 경로 전 test green으로 강화** 권고. 이로써 누군가 top-level import로 회귀시키면 T-H가 즉시 RED.

### R-A5. SpyRedactor를 RedactionFilter 실인스턴스로 — T-A의 RT-1 동치 검증 신뢰도
- T-6의 SpyRedactor(line 95~101)는 `redact_messages`가 입력을 *그대로 반환*(no-op) → "호출됨"만 검증. brief §3 line 117 "단순 호출 확인이 아니라 Router 입력=redacted output 동치"를 충족하려면 **T-A는 실 `RedactionFilter()` + 실제 secret(예: `sk-ant-...`) 포함 messages → fake Router가 받은 `messages`에 secret 평문 0 + `[REDACTED]` 존재**를 단언해야 함(spy redactor 아님). brief가 의도한 방향이나 §8.1 T-A 명세에 "실 RedactionFilter 사용" 명문 권고.

---

## 3. NOTE (참고 — 조치 선택)

- **N-A1**: `SKIP_DIRECT_REGISTER = {T1-040, T1-038}`이나 `COMPILED_PATTERNS`에 해당 id 부재 → skip이 **no-op**(전 45 패턴 적용). brief "45 패턴" 성능 주장은 정확(실제 45 run). 본 cycle 범위 외(SC-1 산출) — 패턴 *내용* 변경 0 의무([[feedback_pass_scope_overclaim]] 인접)로 본 cycle 손대지 말 것. 별도 SC-1 후속 cleanup 후보로만 기록.
- **N-A2**: `tests/fixtures/provider_adapter_enforcement/pass/facade_only.py:21` `LLMRequest(alias)` + `mvp1_entry/pass/stdlib_only.py:23` `alias` 는 **import-linter PoC 독립 fixture**(실 facade 무관). brief D2 line 80 판정("영향 0") **정확** — rename 시 손대지 말 것(fixture 의도 = scanner false-positive 검증).
- **N-A3**: pytest baseline = **167 passed, 0.12s** (`.venv/bin/python -m pytest tests/ -q`). 시스템 python엔 pytest 미설치 → `.venv` 사용 의무. brief의 "기존 회귀 0" 기준선 = 167(현). B-A2 갱신 후 T-6 1건 변형되므로 신규 회귀 0 기준 = (167 - 1 변형 + 신규 T-A~T-H) 로 재계산 필요.
- **N-A4**: litellm 미설치(`python3 -c "import litellm"` → ModuleNotFoundError, 시스템+venv 양쪽) 실측. brief D4 전제 정확. 실 설치 시도(§4.1 line 130)는 네트워크 의존 — 실패해도 mock CI 무영향(주입). litellm 의존성 트리가 방대하므로(google/openai/boto 등 다수 transitive) **설치 시도가 venv 오염/시간 소요 위험** → CI는 litellm 미설치 기준이 안전(brief 명시와 일치).
- **N-A5**: `redaction.py:62~74` `redact_messages`는 `content`가 str/list/dict만 처리. 설계 §4.1 multimodal `content: list[dict]`은 `scrub` 경유(line 70~71) → 기존 동작. tool_choice/response_format/stop_sequences 필드(brief D2 trivial passthrough)는 messages 외부이므로 redaction 무관 — 그대로 Router opts 전달 가능(실현 OK).

---

## 4. 구현 실현가능성 / 성능 판정

| 항목 | 판정 | 근거 |
|------|------|------|
| **D1 async 전환** | ✅ 실현 (breaking 0) | `grep .complete( src/` = 0 match (직접 실행) |
| **D2 LLMRequest rename** | ⚠️ 조건부 (B-A2) | test:105 `alias=` 1건 + T-6 동작 동시 갱신. src caller 0 |
| **D3 LLMResponse/Metadata 정규화** | ✅ 실현 (B-A3 metadata 행선지 정정) | LiteLLM OpenAI 포맷 통일 가정 합리 (실측 deferred), 화이트리스트 frozen dataclass 자명 |
| **D4 lazy import + hermetic** | ✅ 실증 | grimp 귀속 검증 + lazy 미발화 런타임 실증 (`/tmp/lazytest`) |
| **import-linter 경계** | ✅ 실증 | 그래프상 lazy import = facade 귀속 → ignore rule 적용 |
| **D5 validate_config** | ✅ 실현 | 설계 §3.3/§6.1 코드 그대로 (자명) |
| **D6 registry yaml** | ✅ 실현 (B-A1 라우팅 키 정정) | yaml 로드 자명, 단 acompletion model 인자 = alias |
| **D7 에러 분류** | ⚠️ 실측 deferred | `litellm.AuthenticationError` 등 import 경로 = litellm 미설치로 실측 불가. fake가 표준 예외 raise → re-raise 검증은 mock으로 가능 |
| **D8 health dry probe** | ⚠️ 축소 fallback 권고 (R-A2) | Router health_check API 실 형태 실측 불가 → RT-6 축소 채택 |
| **성능 (redaction)** | ✅ 무시 가능 | 45 패턴 0.193ms/call (실측). 네트워크 latency 대비 <0.1% |
| **TDD T-A~T-I 작성** | ✅ 실현 (B-A2 T-6 처리 명문) | fake Router 주입 hermetic 입증 — 전 항목 mock 가능 |

**종합**: 구현 실현가능성 = **높음**. 핵심 리스크(hermetic, async breaking, import 경계, 성능)는 직접 실행으로 해소. 잔여 리스크는 (a) litellm 표준 예외/Router health API의 *실 형태 실측 불가*(D7/D8 — mock 검증 한정이 brief scope와 일치) + (b) B-A1~B-A3의 *명세 미정밀*(구현 임의 결정 우회 방지). 모두 GREEN 전 명세 정정으로 해소 가능 → **APPROVE WITH CONDITIONS**.

---

## 5. 설계 §17 재합의 — Agent A 항목 판정 (folding)

| §17 Agent A 항목 | 판정 | 비고 |
|------|------|------|
| LLMRequest 신규 필드 5종 | 부분 (core만 본 cycle) | system/tool_choice/response_format/stop_sequences = 본 cycle 포함 가능, **stream = 명세 존속·구현 deferred** |
| AsyncIterator[StreamEvent] | 명세 존속·구현 deferred | 삭제 아님 (§7 RT-5) |
| tool_use 정규화 (LiteLLM 위임) | 명세 존속 | LiteLLM OpenAI 변환 위임 — 실측 deferred |
| health(provider_key) 모순 해소 | ✅ (§4.1 = 무인자 health) | 현 facade.py:62 `health()` 무인자와 일치. 단 D8 dry 형태 = R-A2 |
| 폴백 race 5종 완화 | 명세 존속·구현 deferred | §0.2 #5 |
| Phase 1 ollama 포함 | ✅ | yaml 기본 active 2종에 ollama 포함 (brief §5.1 line 155) |

**Agent A 관점 §17 판정**: deferred 항목 = "설계 명세 존속 + 구현 deferred"(brief §7 line 206 동의). 단 **B-A1(acompletion model=alias)** 정정이 설계 §5.1과의 정합 확보 후라야 §17 "확정" 승격이 구현 정합 기준 충족. health 무인자(§4.1 R10 보강) = 현 코드 일치 ✅.

---

## 6. Evidence (직접 실행 로그 요약)

- E-A1: `grep -rn "\.complete(" src/` → **0 match** (D1 caller 0)
- E-A2: `python3 -c "import litellm"` (시스템+venv) → **ModuleNotFoundError** (D4 미설치)
- E-A3: grimp `build_graph('src', include_external_packages=True)` → 현 그래프에 LLM SDK **0** (facade 미import 상태). `/tmp/lazytest`에서 함수-레벨 `import litellm` → `importers = {'src.adapters.llm.facade'}` (lazy 귀속 검증)
- E-A4: `import facade; 'litellm' not in sys.modules` → **True** (모듈 import 시 lazy 미발화), `_build()` 호출 시에만 ModuleNotFoundError (hermetic 입증)
- E-A5: `.venv/bin/python -m pytest tests/ -q` → **167 passed in 0.12s** (baseline green)
- E-A6: redaction 45 패턴 `redact_text` × 1000 (~250 word) → **0.193s (0.193ms/call)** (성능)
- E-A7: `ALL_PATTERNS=45, COMPILED=45, 적용=45` (SKIP no-op — N-A1)

---

**Agent A 판정 = APPROVE WITH CONDITIONS** (BLOCKING 3 + 권고 5 + NOTE 5). 구현 실현가능성 높음, 성능 무시 가능, BLOCKING은 명세 정밀화로 해소.
