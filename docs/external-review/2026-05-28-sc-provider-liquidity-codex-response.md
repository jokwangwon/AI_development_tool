Reading prompt from stdin...
OpenAI Codex v0.128.0 (research preview)
--------
workdir: /home/delangi/문서/project/category/AI_development_tool
model: gpt-5.5
provider: openai
approval: never
sandbox: danger-full-access
reasoning effort: none
reasoning summaries: none
session id: 019e6e79-3090-7641-ad4c-bca76fcfabcc
--------
user
당신은 외부 LLM 검토자 (cross-vendor blind review)입니다. 응답 vendor = OpenAI (codex CLI, gpt-5.5), 본 cycle 풀 3+1 Agent vendor = Anthropic Claude. cross-vendor 충족 (헌법 5조-2 Provider Liquidity).

## 본 cycle 개요

AI_development_tool 프로젝트 (SDD + TDD + 하네스 엔지니어링 + 3+1 멀티에이전트 합의). 본 cycle = **SC-Provider Liquidity — facade LiteLLM Router 위임 real (core complete() 경로) 구현 brief** (69번째 entry 예정, 세션 #4).

배경: 65 SC-1으로 `src/adapters/llm/facade.py`의 redaction layer는 real이나 LiteLLM Router 위임이 `NotImplementedError` 상태 → 실제 LLM 호출 0건. 본 cycle = Router 위임 deferred 해제 → facade `complete()` core 경로 operative. Provider Liquidity 헌법 5조-2 (코드 변경 없이 provider/model 교체) 핵심 + 자비스 "로컬 사장 + tmux 워커" 실 동작 기반.

scope (사용자 명시 AskUserQuestion 3건):
- 구현 범위 = **Core MVP**: complete() Router 실배선 + validate_config(Min 2 active + 동일 type 금지) + llm-providers.yaml registry + LiteLLM 설치·핀 + 응답 정규화(LLMResponse/LLMMetadata 화이트리스트) + RT-1(redaction 선부착).
- DEFER: streaming(StreamEvent) / OAuth single-flight / degraded 모드·R4 런타임 재검증 / DomainMetricsCallback / 폴백 race 완화.
- 검증 범위 = **Router mock만** (litellm.Router를 주입 fake로 대체, hermetic). 실 LLM 호출(credential/네트워크) = 수동/별도 trigger.
- 설계 v2 §17 재합의 = 본 풀 3+1이 겸함.

본 cycle 발효 *하지 않는* 것: full facade real 0 / 실 LLM 호출 검증 0 (mock만) / Provider Liquidity 완전 발효 0 / streaming·OAuth·degraded·metrics·폴백race 구현 0 / 65 RedactionFilter 패턴 *내용* 변경 0 / ADR·헌법·governance 본문 변경 0 (설계 v2 status flip + cross-ref만) / 자동 후속 sub-cycle 진입 0.

⚠️ **핵심 over-claim 경고**: 본 프로젝트는 over-claim cascade를 세션 #2에서 4회, 세션 #3에서 2회 (SC-2 R-6 자동회귀 + SC-3 "full" 명칭) 포착함. 본 cycle은 carry-over 후보명이 "full facade real"이었음 — "full" over-claim risk 최고조 (67 entry "GP-2 full PASS → GP-2 prevention PASS" 강등 선례 직접 동형). "full facade real / facade 완성 / Provider Liquidity 완전 발효 / 런타임 검증 완료" 표현이 deferred(streaming/OAuth/degraded/metrics/race) + mock-only 검증을 은폐하지 않아야 함.

## 검토 대상 (codex 직접 read 의무 — 추측 금지, line 인용 기반)

PRIMARY (본 검토 핵심):
- docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md (v1, §0~§14) ← 본 검토 핵심

권위/evidence source (직접 read cross-verify):
- docs/architecture/llm-providers-design.md (P1 v2 — §3 registry / §4 facade 인터페이스 / §5 Router 위임 / §6 Min 2 / §15 Phase 로드맵 / §17 재합의 체크리스트 / footer "3+1 재합의를 통과해야 확정" + 상태 "초안 v2 재합의 대기")
- docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md §2 (P1 facade MVP 진입조건 (a)~(d) 2026-05-04 충족 + §2.2 6 의무 + §2.3 Hermes PMO ↔ provider 분리 영구)
- docs/decisions/ADR-008-hermes-adoption-decision.md (차단조건 #3 v0.x 버전 핀 / #4 provider 어댑터 1개 추상화 + 분기 금지 / #5 Min 2 always-on)
- docs/architecture/governance-preconditions.md §1.2.7 P11 (supply-chain — dependency pinning integrity + checksum/hash + lock diff 회귀) + §4 GP-2 + §4.5(a) (facade redaction filter 검증)
- src/adapters/llm/facade.py (현 placeholder — redaction layer real + Router NotImplementedError, complete() sync) + src/adapters/llm/redaction.py + src/adapters/llm/redaction_patterns.py (65 SC-1 RedactionFilter)
- tests/adapters/llm/test_redaction_filter.py (65 test 15건 — LLMRequest(alias=...) 사용 line 105 영향 확인)
- .importlinter (no-direct-llm-sdk 계약 — litellm facade 외 금지 + include_external_packages=True) + requirements-dev.txt ("runtime application 의존성 0건 / pyproject.toml 신설 별도 합의")
- docs/review/3plus1-consensus-2026-05-04-p1-llm-providers.md (P1 합의 — "P1은 현재 상태로 승인 불가, 옵션 결정 + 12 보강 후" 판정)

## 검토 관점 (외부 cross-vendor 독립 — 추측 금지)

1. **명칭 over-claim 차단 (최우선)**: brief가 "full facade real"을 회피하고 "facade Router 위임 real (core complete() 경로)" 한정 + 5종 deferred + mock-only 검증을 정직하게 명문하는가? 67 "GP-2 full→prevention" cascade 답습이 충실한가? "full"/"완성"/"완전 발효" 단어가 deferred를 은폐하는 over-claim 잔존 여부?
2. **RT-1 redaction 선부착 (보안 핵심)**: brief §3 + §4.1 (lazy import + Router 주입) 설계가 redaction 미부착 window 0을 보장하는가? §8.1 T-A "Router가 받은 messages = redacted output 동치 검증"이 충분한가, 아니면 단순 "redaction 호출됨" 확인 함정에 빠지는가? redacted body가 실제로 Router 인자로 전달되는 경로가 명확한가?
3. **LiteLLM 첫 runtime dependency 도입 (D4, §4)**: manifest gate lift("pyproject 별도 합의" 해소) + 버전 핀(ADR-008 #3) + supply-chain hash(P11 (ii)) 처리가 정당+비례적인가? 개인 단일 사용자 툴 비례성 ↔ supply-chain 엄격성 균형이 적절한가? manifest 형식(requirements.txt vs pyproject.toml) 권고 근거?
4. **설계 v2 §17 재합의 folding (§7)**: 본 풀 3+1이 §17 겸함이 적절한가? deferred 항목(streaming/OAuth/degraded/race)을 "설계 명세 존속 + 구현 deferred"로 판정(삭제 아님)이 타당한가? 설계 §15 "v1.0(MVP) = 12 보강 모두" 문구 ↔ Core MVP 분할 사이 정합성 문제가 있는가?
5. **D1~D8 결정 타당성**: async 전환(src caller 0, test 1건) / LLMRequest rename(alias→model_alias) / LLMResponse+LLMMetadata 화이트리스트 / validate_config Min2+동일type / registry yaml / 에러분류 litellm 표준예외 / health dry probe. 각 결정에 누락·모순·실현가능성 문제?
6. **SDD 정합성**: 미확정 설계(footer "재합의 대기") 구현 진입 risk를 §7 folding으로 처리하는 것이 SDD 원칙(문서 우선, 미확정 설계 구현 금지)을 충족하는가?
7. **Provider Liquidity 보존**: facade 단일 진입점(litellm lazy import도 facade 한정 — import-linter PASS) + 모델명 코드 분기 0(yaml만) + LLMMetadata 화이트리스트(위반패턴 #2/#4) + ADR-009 §2.3 Hermes 분리. 위반 잠재?
8. **권위 인용 정확성** + **누락/risk**: brief가 인용한 권위(line/§)가 실제 문서와 일치하는가?

## 응답 형식 (필수)

1. **판정**: APPROVE / APPROVE WITH CONDITIONS / REVISE
2. **BLOCKING 항목** (있으면): 번호 + 근거 (직접 read한 파일/line 인용)
3. **권고 항목**: 번호 + 내용
4. **NOTE**: 관찰
5. **명칭 독립 판단**: "SC-Provider Liquidity — facade Router 위임 real (core complete() 경로)" 명칭이 적절한가, 아니면 더 정직한 명칭 제안?
6. **권위 인용 cross-verify 매트릭스**: brief 인용 vs 실제 문서 일치/모순

한국어로 응답하되 기술 용어는 영어 원문 유지. 반드시 직접 파일을 read하여 검증하고, 추측이 아닌 구체적 line 인용 기반으로 응답하세요.

codex
요청 범위가 문서/코드 cross-review라서 먼저 지정된 primary와 권위 문서를 직접 읽고 line 기준으로 대조하겠습니다. 변경은 하지 않고 review stance로 findings를 먼저 정리하겠습니다.
exec
/bin/bash -lc "nl -ba docs/architecture/llm-providers-design.md | sed -n '1,320p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# LLM Provider 추상화 설계 (LLM Providers Design)
     2	
     3	> **모든 LLM 호출이 LiteLLM facade를 거치며, provider/모델 교체가 코드 변경 없이 config 1줄로 가능한 구조**
     4	
     5	**최종 수정**: 2026-05-04 (Option β 채택, 3+1 합의 결과 반영)
     6	**상태**: 초안 v2 (Option β: LiteLLM facade 승격 + 12 보강 + 4 β-추가 적용. 재합의 대기)
     7	**상위 문서**: `ADR-008-hermes-adoption-decision.md` (차단조건 #4·#5 충족 메커니즘)
     8	**관련 ADR**: ADR-004 (생성 AI 확장성, **외부 SDK 우선 원칙 일치**), ADR-006 (환경 변수 + Docker), ADR-009 (자체 Adapter v2.0 진입조건)
     9	**관련 메모리**: `feedback_provider_liquidity.md` (영구 기억)
    10	**관련 합의**: `review/3plus1-consensus-2026-05-04-p1-llm-providers.md`
    11	
    12	---
    13	
    14	## 1. 개요
    15	
    16	### 1.1 문제 정의
    17	
    18	LLM 도구 도입(Hermes, 외부 LLM 호출 등)이 진행되면 다음 문제가 발생한다:
    19	
    20	```
    21	현재 (단일 LLM 의존):
    22	  애플리케이션 → Claude SDK 직접 호출 → Claude 응답
    23	                  ↑
    24	             모델 교체하려면 코드 곳곳을 수정
    25	
    26	목표 (Provider Liquidity):
    27	  애플리케이션 → LLM Facade (단일 인터페이스)
    28	                  ↓
    29	             LiteLLM (40k 스타, 200+ provider 정규화)
    30	                  ↓
    31	             config 기반 라우팅 → Claude / GPT / Ollama / ...
    32	```
    33	
    34	사용자의 비협상 제약은 **"모델/구독 교체가 코드 변경 없이 가능해야 한다"**(`feedback_provider_liquidity.md`).
    35	
    36	### 1.2 해결 방안 (Option β — LiteLLM facade 승격)
    37	
    38	ADR-004 본질("자체 어댑터 불필요 — 외부 SDK 활용") + 3+1 합의 권고에 따라 다음 구조 채택:
    39	
    40	1. **LiteLLM SDK가 외부 추상화 계층** — provider별 응답·에러 정규화는 LiteLLM이 자체 제공
    41	2. **얇은 facade (~100 LOC)** — LiteLLM 위에 본 프로젝트 도메인 보강(redaction, single-flight, active 재검증, 도메인 메트릭)
    42	3. **단일 config (`llm-providers.yaml`)** — provider/모델 등록은 ADR-004 패턴 그대로
    43	4. **LiteLLM Router 위임** — 라우팅·폴백·헬스체크·cooldown
    44	5. **정적 검사** — `litellm` 외 LLM SDK 직접 import 금지 1줄 룰
    45	
    46	### 1.3 Option β 채택 근거 (요약)
    47	
    48	| 비교 | 자체 Adapter (Option α) | LiteLLM facade (Option β, 채택) |
    49	|------|------------------------|--------------------------------|
    50	| 코드 LOC | ~600 + 차단 테스트 ~600 | ~100 facade + 보강 ~150 + 테스트 ~200 |
    51	| 연간 유지 | ~40~80h | ~5~10h |
    52	| 위반 패턴 차단 | 100% 자력 (depcruise 6종) | #1·#2·#5·#6 LiteLLM 자연 차단 |
    53	| ADR-004 정합성 | 본질 위반 | 본질 일치 |
    54	| 외부 종속성 | 없음 | LiteLLM (Apache 2.0) |
    55	
    56	### 1.4 하네스 위치
    57	
    58	```
    59	Layer 0:   CLAUDE.md (가이드 — provider 선택 정책)
    60	Layer 0.5: 본 설계 문서 (가이드 — facade 계약 + redaction 정책)
    61	Layer 1:   PostToolUse Hook (센서 — SDK 직접 import 검출)
    62	Layer 1.5: depcruise 정적 검사 (센서 — 회피 차단)
    63	Layer 5:   3+1 합의 (센서 — 신규 provider 추가 시 검토)
    64	```
    65	
    66	---
    67	
    68	## 2. 핵심 원칙
    69	
    70	| 원칙 | 설명 | 근거 |
    71	|------|------|------|
    72	| **External SDK First** | LiteLLM이 1차. 자체 코드는 facade 100 LOC + 도메인 보강만 | ADR-004 본질, Reviewer 권고 |
    73	| **Single Facade** | 모든 LLM 호출이 통과하는 facade는 정확히 1개 | ADR-008 차단조건 #4 + 위반 패턴 #2 |
    74	| **Config-Driven** | provider/모델 추가·교체·제거 = `llm-providers.yaml` 편집만 | ADR-004 패턴 일관 |
    75	| **API Key First, OAuth Second** | API 키 경로 우선. OAuth(구독)는 보조 옵션 | ADR-008 부록 A.1 + R4 |
    76	| **Min 2 Always-On (Runtime 재검증)** | 항상 active≥2. 시작 + 모든 강등 경로에서 재검증 | ADR-008 차단조건 #5 (3+1 합의 R4 보강) |
    77	| **Stateless Facade** | facade는 호출 컨텍스트만 받고 상태를 내부에 저장하지 않음. LiteLLM Router 상태는 Router 자체가 관리 | 락인 회피, 테스트 용이성 |
    78	| **Redaction Mandatory** | 모든 응답·예외·메트릭에서 token/key/auth 패턴 자동 strip | ADR-008 R1 + 헌법 제8조 |
    79	
    80	---
    81	
    82	## 3. Provider 레지스트리
    83	
    84	### 3.1 단일 설정 파일
    85	
    86	```yaml
    87	# llm-providers.yaml (단일 진실 원천)
    88	
    89	defaults:
    90	  primary: anthropic-claude-api    # 1순위
    91	  secondary: openai-gpt-api        # 폴백 (Min 2 Always-On)
    92	  tertiary: ollama-llama-local     # 비용 0, type 다양성
    93	
    94	# 라우팅 우선순위 — alias 기반
    95	routing:
    96	  consensus_agent_a: anthropic-claude-api
    97	  consensus_agent_b: openai-gpt-api
    98	  consensus_agent_c: ollama-llama-local
    99	  reviewer: anthropic-claude-api
   100	  background_jobs: ollama-llama-local
   101	  default: anthropic-claude-api
   102	
   103	providers:
   104	  anthropic-claude-api:
   105	    type: anthropic
   106	    litellm_model: anthropic/claude-opus-4-7   # LiteLLM model prefix
   107	    auth_method: api_key
   108	    api_key_env: ANTHROPIC_API_KEY
   109	    cost: per_token
   110	    cost_estimate: $15/1M_input + $75/1M_output
   111	    status: active
   112	    health_check: dry                          # dry probe (실 토큰 호출 안 함)
   113	
   114	  anthropic-claude-oauth:
   115	    type: anthropic
   116	    litellm_model: anthropic/claude-opus-4-7
   117	    auth_method: oauth_subscription
   118	    oauth_credentials_env: CLAUDE_CREDS_PATH   # ⚠️ 경로는 env로 보간 (R7)
   119	    cost: flat_subscription
   120	    cost_estimate: $100/month (Max 5x) + extra credits
   121	    status: standby
   122	    known_bugs:
   123	      - "ADR-008 R4: #15080, #6475, #12905, #10575"
   124	    notes: "API 키 경로 우선. OAuth는 폴백·비용 절감 시에만"
   125	
   126	  openai-gpt-api:
   127	    type: openai
   128	    litellm_model: openai/gpt-5.5
   129	    auth_method: api_key
   130	    api_key_env: OPENAI_API_KEY
   131	    cost: per_token
   132	    status: active
   133	    health_check: dry
   134	
   135	  openai-gpt-oauth:
   136	    type: openai
   137	    litellm_model: openai/gpt-5.5
   138	    auth_method: oauth_subscription
   139	    oauth_credentials_env: CODEX_CREDS_PATH
   140	    cost: flat_subscription
   141	    cost_estimate: $200/month (ChatGPT Pro)
   142	    status: standby
   143	    tos_notes: "개인 단일 사용자만. ADR-008 부록 A.1 정책 변동 모니터링"
   144	
   145	  ollama-llama-local:
   146	    type: ollama
   147	    litellm_model: ollama/llama-3.3-70b
   148	    auth_method: none
   149	    endpoint: http://localhost:11434
   150	    cost: free
   151	    status: active
   152	
   153	  openrouter-fallback:
   154	    type: openrouter
   155	    litellm_model: openrouter/anthropic/claude-opus-4.7
   156	    auth_method: api_key
   157	    api_key_env: OPENROUTER_API_KEY
   158	    cost: per_token
   159	    status: standby
   160	```
   161	
   162	### 3.2 status 필드
   163	
   164	| 값 | 의미 | facade 동작 |
   165	|---|------|-----------|
   166	| `active` | 정상 사용 가능 | 라우팅에 포함, 폴백 체인에 포함 |
   167	| `standby` | 명시 호출 또는 폴백 시에만 사용 | 라우팅 디폴트에서 제외, 폴백에 포함 |
   168	| `deprecated` | 사용 시 경고 | stderr 경고 + 메트릭 |
   169	| `blocked` | 즉시 차단 (장애·보안) | 즉시 폴백 + 알림 |
   170	
   171	### 3.3 cost 필드 + 동일 type active 강제 금지 (R5)
   172	
   173	`flat_subscription` 또는 동일 `type`은 active로 동시에 둘 수 없다. 시작 시 검증:
   174	
   175	```python
   176	# config 검증 (시작 시 fail-fast)
   177	def validate_config(config):
   178	    active = [(k, v) for k, v in config["providers"].items() if v["status"] == "active"]
   179	    if len(active) < 2:
   180	        raise ConfigError(f"Min 2 active 정책 위반. ADR-008 #5")
   181	
   182	    types = [v["type"] for k, v in active]
   183	    if len(set(types)) != len(types):
   184	        raise ConfigError(
   185	            f"동일 type 2개 active 금지 (정전 시 동시 실패). 현재 type 분포: {types}. "
   186	            f"3+1 합의 R5 강제."
   187	        )
   188	```
   189	
   190	---
   191	
   192	## 4. LLM Facade 인터페이스
   193	
   194	### 4.1 단일 facade — `LLMFacade` (~100 LOC)
   195	
   196	```python
   197	# adapters/llm/facade.py — 정확히 이 파일만 LiteLLM 직접 import
   198	
   199	import litellm
   200	from typing import AsyncIterator, Literal
   201	from dataclasses import dataclass, field
   202	
   203	# ===== Request/Response 표준 스키마 =====
   204	
   205	@dataclass(frozen=True)
   206	class LLMRequest:
   207	    messages: list[dict]                 # OpenAI 호환 messages 배열
   208	    model_alias: str                     # 라우팅 alias (예: "consensus_agent_a")
   209	    system: str | None = None            # ← R1 보강 (Anthropic system 분리 지원)
   210	    temperature: float = 0.7
   211	    max_tokens: int = 4096
   212	    tools: list[dict] | None = None
   213	    tool_choice: dict | str | None = None       # ← R1 보강
   214	    response_format: dict | None = None         # ← R1 보강 (json mode)
   215	    stop_sequences: list[str] | None = None     # ← R1 보강
   216	    stream: bool = False                        # ← R1 보강 (명시화)
   217	    metadata_in: dict | None = None             # 호출 메타 (요청 ID 등 — redaction 대상)
   218	
   219	@dataclass(frozen=True)
   220	class LLMMetadata:
   221	    """metadata는 화이트리스트 키만 (R2 보강). raw dict 금지."""
   222	    provider_used: str                   # 실제 사용된 provider key
   223	    fallback_chain: list[str]            # 시도된 provider 순서
   224	    finish_reason: str
   225	    request_id: str | None = None
   226	    # ↑ 화이트리스트 — 새 키 추가는 본 데이터클래스 수정 필요 (depcruise로 강제)
   227	
   228	@dataclass(frozen=True)
   229	class LLMResponse:
   230	    content: str                         # 정규화된 본문 (multimodal은 별도 — §4.4)
   231	    usage: dict                          # {input_tokens, output_tokens, cost_estimate}
   232	    metadata: LLMMetadata                # 구조화된 메타 (raw dict 아님)
   233	
   234	# ===== Stream 이벤트 합 타입 (R11 보강) =====
   235	
   236	@dataclass(frozen=True)
   237	class StreamTextDelta:
   238	    text: str
   239	
   240	@dataclass(frozen=True)
   241	class StreamToolCallDelta:
   242	    tool_call_id: str
   243	    name: str | None
   244	    arguments_delta: str
   245	
   246	@dataclass(frozen=True)
   247	class StreamUsageEnd:
   248	    usage: dict
   249	    finish_reason: str
   250	
   251	StreamEvent = StreamTextDelta | StreamToolCallDelta | StreamUsageEnd
   252	
   253	# ===== Facade =====
   254	
   255	class LLMFacade:
   256	    """모든 LLM 호출의 단일 진입점. 본 클래스 외 LiteLLM 직접 호출 금지."""
   257	
   258	    def __init__(self, config: dict):
   259	        validate_config(config)                  # Min 2 + 동일 type 강제
   260	        self._router = litellm.Router(...)       # LiteLLM Router에 위임
   261	        self._redactor = RedactionFilter(...)    # R3 보강
   262	        self._oauth_lock = SingleFlightLock(...) # R6 보강
   263	
   264	    async def complete(self, req: LLMRequest) -> LLMResponse:
   265	        provider_key = self._resolve(req.model_alias)
   266	        try:
   267	            raw = await self._router.acompletion(
   268	                model=self._litellm_model(provider_key),
   269	                messages=self._build_messages(req),
   270	                **self._build_options(req),
   271	            )
   272	        except litellm.AuthenticationError:
   273	            await self._on_active_degraded(provider_key)  # R4 재검증
   274	            raise
   275	        return self._normalize(raw, provider_key)
   276	
   277	    async def stream(self, req: LLMRequest) -> AsyncIterator[StreamEvent]:
   278	        # ... LiteLLM streaming + first-token 후 폴백 금지 (R8 보강)
   279	        ...
   280	
   281	    async def health(self) -> dict[str, bool]:   # ← R10 보강 (provider_key 인자 제거)
   282	        """전체 active provider 헬스 — facade 내부에서 alias 조회. 외부 분기 금지."""
   283	        return await self._router.health_check(dry=True)
   284	```
   285	
   286	### 4.2 응답 정규화 — LiteLLM 위임 (R2 보강)
   287	
   288	LiteLLM이 모든 provider 응답을 **OpenAI 포맷으로 자동 통일**하므로, 본 facade의 정규화는 다음에만 집중:
   289	
   290	| 항목 | 처리 |
   291	|-----|------|
   292	| `content` 정규화 | LiteLLM이 자동 — facade는 `raw["choices"][0]["message"]["content"]` 추출만 |
   293	| 토큰 카운트 (`usage`) | LiteLLM 통일 (`prompt_tokens`/`completion_tokens`) — facade가 cost_estimate 추가 |
   294	| `finish_reason` | LiteLLM 통일 — `LLMMetadata.finish_reason`로 격리 |
   295	| **provider 고유 메타** | **버림** — `LLMMetadata` 화이트리스트 외 키는 통과 못 함 (raw dict 누출 차단) |
   296	| `tool_use` 왕복 (R12) | OpenAI tool_calls 표준 사용. Anthropic tool_use는 LiteLLM이 자동 변환 |
   297	| multimodal (이미지) | OpenAI vision 포맷 표준 — `content`가 list[dict] 케이스만 별도 핸들링 |
   298	
   299	### 4.3 에러 분류 — LiteLLM 표준 예외 위임
   300	
   301	```python
   302	# LiteLLM 표준 예외만 catch
   303	litellm.AuthenticationError       # 401/403 → 즉시 폴백
   304	litellm.RateLimitError            # 429 → 백오프 후 재시도
   305	litellm.ServiceUnavailableError   # 5xx → 백오프 후 폴백
   306	litellm.BadRequestError           # 400 → 사용자 에러 (재시도 안 함)
   307	```
   308	
   309	provider 고유 예외는 **LiteLLM이 표준 예외로 변환**하므로 facade는 별도 매핑 불필요.
   310	
   311	### 4.4 호출 흐름
   312	
   313	```
   314	caller.code:
   315	  response = await llm.complete(LLMRequest(
   316	      messages=[{"role": "user", "content": "..."}],
   317	      model_alias="consensus_agent_a",
   318	      system="당신은 ...",
   319	  ))
   320	

exec
/bin/bash -lc "nl -ba docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md | sed -n '1,260p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# SC-Provider Liquidity — facade Router 위임 real (core `complete()` 경로) 구현 brief (v1)
     2	
     3	> **작성**: 2026-05-28 (69번째 entry 진입 cycle — 세션 #4)
     4	>
     5	> **scope** (사용자 명시, AskUserQuestion 3건):
     6	> - **구현 범위 = Core MVP**: `complete()` LiteLLM Router 실배선 + `validate_config`(Min 2 active + 동일 type 금지) + `llm-providers.yaml` registry + LiteLLM 설치·핀 + 응답 정규화(`LLMResponse`/`LLMMetadata` 화이트리스트) + RT-1(redaction 선부착). **DEFER**: streaming(`StreamEvent`) / OAuth single-flight(§7.2) / degraded 모드·R4 런타임 재검증(§6.2/6.3) / `DomainMetricsCallback`(§8.1) / 폴백 race 완화(§5.2).
     7	> - **검증 범위 = Router mock만**: `litellm.Router`를 주입 가능한 fake로 대체하여 위임 경로·redaction 선부착·정규화·Min2 검증을 hermetic하게 테스트. **실 LLM 호출(credential/네트워크 필요) = 수동/별도 trigger** (CI 안정성 우선).
     8	> - **설계 v2 재합의 = 본 풀 3+1이 §17 겸함**: `llm-providers-design.md` footer "재합의 대기" → 본 합의가 §17 검증 체크리스트(Agent A/B/C/Reviewer 항목)를 동시 수행 → 합의 통과 시 설계 상태 "확정" 승격.
     9	>
    10	> ⚠️ **명칭 정직성 (over-claim 차단 — 본 세션 #3 cascade 2회 + 세션 #2 4회 교훈 답습, [[feedback_pass_scope_overclaim]])**: 본 cycle = **facade Router 위임 real (core `complete()` 경로)** — **"full facade real" / "facade 완성" / "Provider Liquidity 완전 발효" 표현 영구 금지**. deferred = streaming/OAuth/degraded/metrics/폴백 race. **실 LLM 호출 = mock 검증** (실 end-to-end 미입증 → "런타임 검증 완료" 표현 금지). 67 entry "GP-2 full → prevention" 강등 선례 동형 주의.
    11	>
    12	> **본 cycle = 큰 cycle (실 코드 + 첫 runtime dependency 도입 + 보안/아키텍처 결정)** → 풀 3+1 + 외부 LLM 1+(codex) 의무 (CLAUDE.md §3: 아키텍처/SDD/보안 = 풀 3+1 필수).
    13	>
    14	> **본 cycle 발효 효과** = facade `complete()` core 경로 operative (config 기반 provider/model 교체가 *코드 경로상* 실동작 — 5조-2 비협상 실동작 기반) + 설계 v2 §17 재합의 통과 시 "확정" 승격. **단 실 호출 검증 = mock 한정** (실 end-to-end = 수동/별도).
    15	>
    16	> **선행 답습**: `llm-providers-design.md` (P1 v2 — §3 registry / §4 facade / §5 Router 위임 / §6 Min 2 / §17 재합의 체크리스트) + ADR-009 §2 (P1 facade MVP 진입조건 2026-05-04 충족, §2.2 6 의무 + §2.3 Hermes ↔ provider 분리) + ADR-008 차단조건 #3(버전 핀)·#4(단일 facade)·#5(Min 2) + 65 SC-1 (RedactionFilter in-repo operative — RT-1 협력자) + governance §1.2.7 P11 (supply-chain 핀/hash)
    17	
    18	---
    19	
    20	## §0 본 brief 의 범위
    21	
    22	### §0.1 본 brief 가 *하는* 것
    23	
    24	1. **핵심 설계 결정 8건 (D1~D8) 명세** — 풀 3+1 검증 대상 (§2)
    25	2. **RT-1 redaction 선부착 보장 경로** (Router 발효 시 미부착 window 0, §3)
    26	3. **LiteLLM 도입 — runtime manifest + 버전 핀 + supply-chain(P11) + import/설치 전략** (§4)
    27	4. **`llm-providers.yaml` registry + `validate_config`(Min 2 + 동일 type 금지)** (§5)
    28	5. **Router 위임 + 응답 정규화(LLMMetadata 화이트리스트)** (§6)
    29	6. **설계 v2 §17 재합의 folding** (§7)
    30	7. **TDD 계획 (Router mock, RED→GREEN→REFACTOR)** (§8)
    31	8. **합의 형태 + Provider Liquidity 보존 + 금지 + Rollback + Evidence + 자기진단** (§9~§14)
    32	
    33	### §0.2 본 brief 가 *하지 않는* 것 (Core MVP scope 경계)
    34	
    35	| # | 영역 | 본 cycle |
    36	|---|------|----|
    37	| 1 | **streaming** (`stream()` / `StreamEvent` 합 타입, §4.1) | 0 (deferred) |
    38	| 2 | **OAuth single-flight lock** (§7.2 `SingleFlightLock`) | 0 (deferred — 본 cycle은 api_key 경로만) |
    39	| 3 | **degraded 모드 + R4 런타임 재검증** (§6.2/§6.3 `_on_active_degraded`) | 0 (deferred — 시작 시 fail-fast만) |
    40	| 4 | **`DomainMetricsCallback`** (§8.1 — redaction 적용 메트릭 sink) | 0 (deferred) |
    41	| 5 | **폴백 race 5종 완화** (§5.2 — semaphore/jitter/snapshot) | 0 (deferred — LiteLLM Router 기본 fallback만) |
    42	| 6 | **실 LLM 호출 end-to-end 검증** (credential/네트워크) | 0 (mock만, 수동/별도) |
    43	| 7 | **65 SC-1 RedactionFilter 패턴 *내용* 변경** | 0 (협력자로 재사용만) |
    44	| 8 | **full GP-2 PASS 재선언 / R-1 canary / R-6 Hermes trigger** | 0 |
    45	| 9 | **ADR / 헌법 / governance 본문 변경** | 0 (설계 v2 status flip + cross-ref만) |
    46	| 10 | **자동 후속 sub-cycle 진입** (streaming / OAuth / MVP-3) | 0 (사용자 명시 의무) |
    47	
    48	### §0.3 권위 답습 source
    49	
    50	- **`llm-providers-design.md`** §3.1(registry yaml) / §3.3·§6.1(validate_config: Min 2 + 동일 type fail-fast) / §4.1(facade 인터페이스) / §4.2(정규화 — LiteLLM OpenAI 포맷 통일 + LLMMetadata 화이트리스트) / §4.3(에러 분류 — litellm 표준 예외) / §5.1(`to_router_config`) / §9.2(dry probe health) / §17(재합의 체크리스트)
    51	- **ADR-009 §2.1**(MVP 진입조건 (a)~(d) 2026-05-04 충족) / §2.2(6 의무 — litellm import facade 한정 등) / §2.3(Hermes PMO ↔ provider 분리 영구)
    52	- **ADR-008 차단조건** #3(v0.x 버전 핀) / #4(provider 어댑터 1개 추상화 + 분기 금지) / #5(Min 2 always-on)
    53	- **governance-preconditions.md** §1.2.7 P11(supply-chain — dependency pinning integrity + checksum/hash + lock diff 회귀) / §4.5(a)(facade redaction filter 검증 — RT-1 협력 대상)
    54	- **`.importlinter`** (no-direct-llm-sdk: `litellm` 등 facade 외 금지 + `include_external_packages=True` 미설치 검출)
    55	- **`requirements-dev.txt`** ("runtime application 의존성 0건 / pyproject.toml 신설 별도 합의" — 본 cycle이 첫 runtime dep 도입 → 해당 gate lift 결정 대상)
    56	- **65 SC-1** (`src/adapters/llm/redaction.py` RedactionFilter + `facade.py` `_redact_request` — RT-1 선부착 협력자)
    57	
    58	---
    59	
    60	## §1 진입 컨텍스트
    61	
    62	- 67 entry 🎉 GP-2 prevention PASS 발효 → 68 roadmap milestone 등록 → 세션 #3 종료. carry-over 1순위 후보 = **SC-Provider Liquidity** (사용자 carry-over 명시 진입, 세션 #4).
    63	- 현 facade(`facade.py`, 61 LOC): **redaction layer real (65 SC-1)** + **Router 위임 = `NotImplementedError`**. → 실제 LLM 호출 0건.
    64	- 본 cycle = Router 위임 deferred 해제 → facade `complete()` core 경로 operative. **자비스 "로컬 사장 + tmux 워커" 실 동작 기반** ([[project_jarvis_local_boss_direction]]) + 5조-2 config 기반 교체 *코드 경로* 실동작.
    65	
    66	---
    67	
    68	## §2 핵심 설계 결정 8건 (D1~D8) — 풀 3+1 검증 대상
    69	
    70	### D1. `complete()` async 전환 (sync → async)
    71	
    72	- 설계 §4.1 = `async def complete`. 현 SC-1 = `def complete`(sync). LiteLLM Router는 `acompletion`(async) + `completion`(sync) 둘 다 제공.
    73	- **권고 = async 전환** (설계 §4.1 충실 + 동시성/IO 적합). **breaking 위험 낮음**: Router가 `NotImplementedError`였으므로 *실제 caller 0* (확인 의무 — D1 검증: `grep -rn "\.complete(" src/`).
    74	- 대안: sync 유지(`Router.completion`) — 설계 §4.1 §17 Agent A 항목과 불일치. → 권고 비채택 시 §17 재합의에서 설계 §4.1 async 명세 정정 필요.
    75	
    76	### D2. `LLMRequest` 필드 정합 (alias → model_alias + core 필드)
    77	
    78	- 현 SC-1: `LLMRequest(alias, messages, metadata)`. 설계 §4.1: `LLMRequest(messages, model_alias, system, temperature, max_tokens, tools, tool_choice, response_format, stop_sequences, stream, metadata_in)`.
    79	- **권고 = core 비-stream 필드 정합**: `model_alias`(rename) + `messages` + `system` + `temperature`(default 0.7) + `max_tokens`(default 4096) + `tools` + `metadata`. **`stream` 관련 필드 deferred**(§0.2 #1). `tool_choice`/`response_format`/`stop_sequences` = trivial passthrough이므로 포함 가능(검증).
    80	- ⚠️ **65 SC-1 `LLMRequest.alias` rename 영향 (실측 2026-05-28)**: `src/` 실 caller **0** (확인). 단 **`tests/adapters/llm/test_redaction_filter.py:105`이 `LLMRequest(alias=...)` 사용 1건** → rename 시 해당 test 갱신 필요(trivial). `tests/fixtures/provider_adapter_enforcement/pass/facade_only.py`의 `LLMRequest`는 **import-linter PoC 독립 fixture**(실 facade 무관, 영향 0).
    81	
    82	### D3. `LLMResponse` 정규화 + `LLMMetadata` 화이트리스트 (§4.2 / 위반패턴 #2·#4)
    83	
    84	- 현 SC-1: `LLMResponse(content, metadata: dict[str,Any])`. 설계 §4.1/§4.2: `LLMResponse(content, usage: dict, metadata: LLMMetadata)` — `LLMMetadata`(frozen 화이트리스트: provider_used / fallback_chain / finish_reason / request_id).
    85	- **권고 = LLMMetadata 화이트리스트 도입** (raw provider 메타 누출 통로 차단 — 위반 패턴 #2/#4 + Liquidity 보존). LiteLLM이 OpenAI 포맷 통일 → `raw["choices"][0]["message"]["content"]` 추출 + usage 표준 필드 + finish_reason 격리.
    86	
    87	### D4. LiteLLM 도입 형식 — runtime manifest + 핀 + supply-chain (§4 상세)
    88	
    89	- 첫 runtime dependency 도입. `requirements-dev.txt`의 "runtime 의존성 0건 / pyproject 신설 별도 합의" gate **lift 결정**.
    90	- **권고**: runtime manifest 신설(`requirements.txt` runtime 또는 `pyproject.toml [project] dependencies`) + **LiteLLM 버전 정확 핀**(ADR-008 #3) + **`--require-hashes`/hash 매니페스트**(P11 (ii)) + **lock diff 회귀 검출**(P11 (v)).
    91	- manifest 형식(`requirements.txt` vs `pyproject.toml`) = 풀 3+1 권고 수렴 대상 (§4.2).
    92	
    93	### D5. `validate_config` — Min 2 active + 동일 type 금지 (§3.3 / §6.1)
    94	
    95	- 시작 시 fail-fast: active provider ≥ 2 (ADR-008 #5) + active 중 동일 `type` 2개 금지 (정전 동시 실패 회피, R5). degraded 런타임 재검증(§6.2)은 deferred — **시작 시 검증만**.
    96	
    97	### D6. `llm-providers.yaml` registry (§3.1)
    98	
    99	- 단일 설정 파일 신규. `defaults` + `routing`(alias→provider) + `providers`(type/litellm_model/auth_method/api_key_env/status). **api_key 평문 금지**(env 보간) + **OAuth credentials 경로 env 보간**(§7.3, OAuth 자체는 deferred지만 yaml 스키마는 standby 등록 허용).
   100	- 본 cycle 기본 active 2종(다른 type): 예 `anthropic-claude-api` + `ollama-llama-local` (api_key + none). 실 키 부재시 동작 = §4.3 검증.
   101	
   102	### D7. 에러 분류 — LiteLLM 표준 예외 위임 (§4.3)
   103	
   104	- `litellm.AuthenticationError`/`RateLimitError`/`ServiceUnavailableError`/`BadRequestError`만 인지. **Core MVP**: AuthenticationError → 즉시 re-raise(degraded 전환 `_on_active_degraded` deferred). Router 자체 fallback/num_retries는 Router 설정에 위임.
   105	
   106	### D8. `health()` — dry probe (§9.2)
   107	
   108	- 현 stub `return {}` → `router.health_check`(dry mode, 무토큰 endpoint 도달성). **권고**: LiteLLM Router health API 실제 형태 확인 후 dry 매핑 (실 API 형태 불명 시 Core MVP는 active alias 목록 + 설정 검증 결과 반환으로 축소 가능 — 검증).
   109	
   110	---
   111	
   112	## §3 RT-1 redaction 선부착 보장 (핵심 안전 제약)
   113	
   114	- **RT-1** (64 trajectory / 65 SC-1): "facade real 후 RedactionFilter 미부착 window 금지 (atomic)".
   115	- 현 `complete()`: `_redact_request(req)` → redacted messages/metadata 산출 → `NotImplementedError`. **redaction이 Router 위임 *전* 위치**.
   116	- 본 cycle 배선: `redacted = self._redact_request(req)` → `raw = await self._router.acompletion(model=..., messages=redacted["messages"], ...)`. **redacted body가 Router로 전달** → 미부착 window 0.
   117	- ⭐ **테스트 강제** (§8.1 T-A): spy/fake Router 주입 → Router가 받은 messages가 *redacted된 것*인지 검증 (원본 secret이 Router 인자에 도달 0). 단순 "redaction 호출됨" 확인이 아니라 **Router 입력 = redacted output** 동치 검증.
   118	- ⚠️ redaction은 송신 경로(request body)만 — **응답 redaction(`scrub`)은 metrics callback(deferred)과 함께**. Core MVP는 응답 본문을 사용자에게 그대로 반환(정상 대화 손상 회피), 단 응답이 로그/메트릭에 기록되는 경로 0(callback deferred)이므로 응답 redaction 미부착 = 누출 통로 0 (검증).
   119	
   120	---
   121	
   122	## §4 LiteLLM 도입 — manifest + 핀 + supply-chain + import 전략
   123	
   124	### §4.1 import / 설치 전략 (hermetic 테스트 보장 — 핵심)
   125	
   126	- 문제: facade.py 모듈 top-level `import litellm` 시 **litellm 미설치 환경에서 facade import 자체 실패** → 주입 기반 테스트도 실패.
   127	- **권고 = lazy import + Router 주입**: `LLMFacade.__init__(self, registry_path, *, redactor=None, router=None)`. `router is None`이면 `_build_router()` 내부에서 `import litellm` 후 `litellm.Router(...)` 구성. 테스트는 fake router 주입 → **litellm import 0 = 미설치에서도 hermetic**.
   128	- import-linter: lazy든 top-level이든 facade 모듈 내 `import litellm`은 AST 그래프에 잡히나 **facade 예외(`src.adapters.llm.facade -> *`) 처리** → 계약 PASS. `include_external_packages=True` → 미설치에서도 검출 정상.
   129	- ⚠️ 설계 §4.1은 top-level import 예시 → **lazy import = 설계 deviation** → §17 재합의에서 "facade 한정 import" 의무 충족(위치만 함수 내부)임을 명시 + 설계 §4.1 주석 정정.
   130	- 실 설치 시도(`pip install litellm==<pin>`): 네트워크 가용 시 수행(실 호출 수동 검증 대비), **실패해도 mock 테스트 무영향**(주입). 본 cycle CI 통과 = mock 기준.
   131	
   132	### §4.2 runtime manifest + 버전 핀 + supply-chain (P11)
   133	
   134	| 항목 | 본 cycle 처리 | 권위 |
   135	|------|----|----|
   136	| manifest 신설 | runtime manifest 신규(형식 = 풀 3+1 권고: `requirements.txt`(runtime) vs `pyproject.toml [project]`) — "별도 합의" gate lift | requirements-dev.txt 주석 + R-RF2 |
   137	| 버전 핀 | LiteLLM `==<정확 버전>` (v0.x or 최신 stable) | ADR-008 #3 |
   138	| Apache 2.0 확인 | 라이센스 재확인 (ADR-009 §2.1 (c) 답습) | ADR-009 §2.1 |
   139	| hash 검증 | `--require-hashes` 또는 hash 매니페스트 (가능 범위) | P11 (ii) |
   140	| lock diff 회귀 | manifest git diff 시 검토 의무 명문 (자동 R-2 재실행은 deferred) | P11 (v) |
   141	
   142	→ manifest 형식 + hash 적용 정도 = 풀 3+1 검증 대상 (과도한 ceremony vs 비례성 — [[feedback_proportionate_security_personal_tool]] 균형).
   143	
   144	---
   145	
   146	## §5 registry yaml + validate_config
   147	
   148	### §5.1 `llm-providers.yaml` (§3.1 축약 — Core MVP 필드)
   149	
   150	```yaml
   151	defaults: { primary: anthropic-claude-api, secondary: ollama-llama-local }
   152	routing: { default: anthropic-claude-api, background_jobs: ollama-llama-local }
   153	providers:
   154	  anthropic-claude-api: { type: anthropic, litellm_model: anthropic/claude-opus-4-7, auth_method: api_key, api_key_env: ANTHROPIC_API_KEY, status: active }
   155	  ollama-llama-local:    { type: ollama,    litellm_model: ollama/llama-3.3-70b,     auth_method: none, endpoint: http://localhost:11434, status: active }
   156	```
   157	
   158	- 기본 active 2종 = 다른 type(anthropic + ollama) → Min 2 + 동일 type 금지 동시 충족.
   159	- standby/blocked/deprecated status 스키마 포함(전이는 Core MVP에서 routing 제외/포함만, degraded deferred).
   160	
   161	### §5.2 `validate_config` (§3.3 / §6.1 fail-fast)
   162	
   163	```python
   164	def validate_config(config):
   165	    active = [(k,v) for k,v in config["providers"].items() if v["status"]=="active"]
   166	    if len(active) < 2: raise ConfigError("Min 2 active 위반 — ADR-008 #5")
   167	    types = [v["type"] for _,v in active]
   168	    if len(set(types)) != len(types): raise ConfigError("동일 type 2개 active 금지 — R5")
   169	```
   170	
   171	- 시작 시 1회(`__init__`). **런타임 재검증(R4)은 deferred** — degraded 모드 미구현 명시.
   172	
   173	---
   174	
   175	## §6 Router 위임 + 응답 정규화
   176	
   177	### §6.1 `to_router_config` (§5.1)
   178	
   179	- `llm-providers.yaml` → LiteLLM Router `model_list`(model_name=alias, litellm_params.model=litellm_model, api_key 환경변수) + `router_settings`(fallbacks, num_retries, timeout). cooldown/고급 튜닝 = v1.1 deferred.
   180	
   181	### §6.2 `complete()` 흐름 (Core MVP)
   182	
   183	```
   184	1. provider_key = routing[req.model_alias]   (없으면 routing.default)
   185	2. redacted = self._redact_request(req)       (RT-1 — Router 전)
   186	3. raw = await self._router.acompletion(model=litellm_model, messages=redacted["messages"], **opts)
   187	4. return self._normalize(raw, provider_key)   (LLMResponse + LLMMetadata 화이트리스트)
   188	   except litellm.AuthenticationError: raise   (degraded 전환 deferred)
   189	```
   190	
   191	### §6.3 `_normalize` (§4.2)
   192	
   193	- `content = raw.choices[0].message.content` / `usage = {input_tokens, output_tokens, cost_estimate?}` / `LLMMetadata(provider_used, fallback_chain, finish_reason, request_id)`. **raw dict 통과 0** (화이트리스트 외 키 버림).
   194	
   195	---
   196	
   197	## §7 설계 v2 §17 재합의 folding (사용자 명시 Q3)
   198	
   199	본 풀 3+1이 `llm-providers-design.md` §17 검증 체크리스트를 동시 수행 → 통과 시 설계 status `초안 v2 재합의 대기` → **`확정 v2`** flip (footer "재합의 통과해야 확정" 해소). 검증 대상:
   200	
   201	- **Agent A 항목** (§17): LLMRequest 신규 필드 / StreamEvent(본 cycle deferred — 설계 명세 존속 확인) / tool_use 정규화 / health 모순 해소 / 폴백 race(deferred) / Phase 1 ollama 포함
   202	- **Agent B 항목**: LLMMetadata 화이트리스트 / redaction 의무(65 충족) / OAuth credentials(deferred but 스키마) / single-flight(deferred) / 동일 type 금지 / R4 재검증(deferred) / dry probe
   203	- **Agent C 항목**: LiteLLM facade 승격 / depcruise 단순화(import-linter 충족) / redaction 통합(65) / ADR-009 작성(완료)
   204	- **Reviewer**: ADR-004 본질 일치 / ADR-008 #4·#5 / Hermes Option β 일관성
   205	
   206	⚠️ **deferred 항목(streaming/OAuth/degraded/race)은 "설계 명세 존속 + 구현 deferred"로 판정** — 설계에서 삭제 아님. 설계 §15 로드맵 v1.0 "12 보강 모두" 문구 ↔ Core MVP 분할 사이 정합성 = Reviewer 판단 대상(설계 §15 갱신 필요 여부).
   207	
   208	---
   209	
   210	## §8 TDD 계획 (Router mock — RED → GREEN → REFACTOR)
   211	
   212	### §8.1 RED (실패 test 먼저) — `tests/adapters/llm/test_facade_router.py` (신규)
   213	
   214	- **T-A ⭐ (RT-1)**: fake Router 주입 → secret 포함 messages로 `complete()` 호출 → **Router가 받은 messages = redacted** (원본 secret이 Router 인자 도달 0). redaction 선부착 입증.
   215	- **T-B**: `complete()` 정상 경로 → fake Router 응답 → `LLMResponse(content, usage, LLMMetadata)` 정규화 (raw dict 누출 0).
   216	- **T-C (D5)**: `validate_config` — active 1개 → `ConfigError`(Min 2); 동일 type 2개 active → `ConfigError`.
   217	- **T-D**: `validate_config` 정상 (anthropic + ollama 2 active 다른 type) → pass.
   218	- **T-E (D7)**: fake Router가 `AuthenticationError` raise → `complete()` re-raise (degraded 전환 0 — Core MVP).
   219	- **T-F (D2/D3)**: `LLMRequest(model_alias=...)` 필드 + `LLMMetadata` frozen 화이트리스트 (raw 키 거부).
   220	- **T-G (D6)**: `llm-providers.yaml` 로드 → routing alias → provider_key 매핑 + `to_router_config` model_list 구성.
   221	- **T-H (hermetic)**: litellm 미설치에서도 facade import + 위 test 전부 green (lazy import + 주입 입증).
   222	- **T-I (65 회귀)**: 기존 RedactionFilter 15 test + redaction layer 무회귀.
   223	
   224	### §8.2 GREEN (최소 구현)
   225	
   226	- `facade.py`: lazy litellm import + Router 주입 + `complete()` async 배선 + `validate_config` + `to_router_config` + `_normalize` + `LLMRequest`/`LLMResponse`/`LLMMetadata` 정합.
   227	- `src/adapters/llm/registry.py`(신규, 또는 facade 내부): yaml 로드 + validate.
   228	- `llm-providers.yaml`(신규, repo 루트 또는 `config/`).
   229	- runtime manifest(신규) + LiteLLM 핀.
   230	
   231	### §8.3 REFACTOR + verify
   232	
   233	- 커버리지 70%+ (CLAUDE.md §1). frozen/순수성 유지.
   234	- **verify**: pytest(신규 facade + 65 redaction 회귀 0 + jarvis 회귀 0) / **import-linter green(litellm = facade 한정)** / secret_scanner scan-source violations 0 / (선택) 실 litellm 설치 시도 + 설치 성공 시 ollama 없이 import smoke.
   235	
   236	---
   237	
   238	## §9 합의 형태 + 승격 트리거
   239	
   240	### §9.1 형태 = 풀 3+1 + 외부 LLM 1+ (codex cross-vendor)
   241	
   242	| # | trigger | 발화 |
   243	|---|---------|----|
   244	| 1 | 아키텍처 의사결정 (Router 위임 + manifest) | ✅ |
   245	| 2 | SDD 명세 검토 (설계 v2 §17 재합의 folding) | ✅ |
   246	| 3 | 보안 관련 변경 (RT-1 + supply-chain P11 + credential env) | ✅ |
   247	| 4 | 실 코드 + 첫 runtime dependency 도입 | ✅ |
   248	| 5 | Provider Liquidity 5조-2 직결 (cross-vendor 외부 LLM 의무) | ✅ |
   249	
   250	→ **5/5 → 풀 3+1 + 외부 LLM 1+ 의무**. 본 brief = 구현 *전* 설계 승인 (SDD 답습).
   251	
   252	---
   253	
   254	## §10 Provider Liquidity 보존 (ADR-009 §2.2, 5조-2 비협상)
   255	
   256	- LiteLLM 직접 import = facade.py 한정 (lazy import도 facade 내부, import-linter PASS).
   257	- 모델명/provider = `llm-providers.yaml`만 (코드 분기 0 — 위반 패턴 #1). alias = 의미 명칭(provider 인코딩 0).
   258	- `LLMMetadata` 화이트리스트 = raw provider 메타 누출 0 (위반 패턴 #2/#4).
   259	- Hermes PMO ↔ provider 분리 영구 (ADR-009 §2.3) — 본 facade가 단일 진입점.
   260	

exec
/bin/bash -lc "nl -ba docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md | sed -n '1,240p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# ADR-009: P1 Facade MVP 진입조건 + 자체 LLM Adapter v2.0 진입 트리거
     2	
     3	**상태**: 승인 (3+1 합의 결과 반영, Bβ-4) + **C-N 갱신 (단축 합의, 2026-05-09 후속 4)**
     4	**날짜**: 2026-05-04 (초기 승인) / **2026-05-09 (C-N 갱신 — P1 facade MVP 진입조건 명시 + Hermes PMO ↔ provider 분리 + Provider Liquidity 5-way 답습 + P2 v3 cross-reference)**
     5	**의사결정자**: 사용자 + 3+1 에이전트 합의 (초기) + **사용자 + Reviewer 단축 합의 (C-N 갱신, 2026-05-09)**
     6	**상위 권위**: 헌법 제5조-2 관용 (Provider Liquidity, 비협상), ADR-004 (외부 SDK 우선), ADR-008 (Hermes 도입 Option B), **ADR-011 §2.3 (Hermes ≠ root of trust)**, **ADR-012 §원칙 5 (Provider Liquidity 5-way Multi-layer Defense)**
     7	**관련 합의**: `docs/review/3plus1-consensus-2026-05-04-p1-llm-providers.md` (Bβ-4 출처), **`docs/review/3plus1-consensus-2026-05-09-c-n-adr-009-update.md` (C-N 갱신 단축 합의)**
     8	
     9	---
    10	
    11	## C-N 갱신 요약 (2026-05-09 후속 4)
    12	
    13	본 갱신은 다음 5 영역 흡수:
    14	
    15	1. **P1 facade MVP 진입조건 명시** (§2 신설) — 기존 ADR-009 는 *v2.0 진입 트리거* 만 명시. MVP 조건이 *부재* 하여 P2 v3 정식 채택 합의 참조 시 모호. 본 갱신으로 명료화.
    16	2. **Hermes PMO ≠ provider 직접 소유** (§2.3 신설) — Hermes PMO (활성화 후 후보 시점) 가 provider SDK 직접 import / 모델명 분기 코드 *금지*. P1 facade 단일 진입점 강제 (ADR-011 §2.3 + Provider Liquidity 5-way Layer 1 답습).
    17	3. **Provider Liquidity 5-way Multi-layer Defense 답습** (§5 갱신) — 본 ADR-009 가 5-way Layer 1 (코드 lock-in 차단) 의 *모법 ADR* 임을 명시 (ADR-012 §원칙 5 발행으로 확정).
    18	4. **자체 Adapter v2.0 진입 트리거 (T1~T4) vs P1 facade MVP 조건 명확 구분** (§3.0 신설) — 두 개념을 표 형식으로 분리. v2.0 트리거 4종 본문 변경 0건.
    19	5. **P2 v3 정식 채택 합의 cross-reference** (§8 갱신) — 본 ADR 이 P2 v3 §1.6 (P1 과의 관계) + §6 G4 + §10 영구 핵심 제약에서 참조 가능하도록 cross-reference 명시.
    20	
    21	**핵심 결정 변경 0건** + **자체 Adapter v2.0 트리거 (T1~T4) 본문 변경 0건** → 단축 합의 적격 (사용자 명시 답습).
    22	
    23	---
    24	
    25	## 1. 맥락 (Context)
    26	
    27	### 1.1 P1 v2 설계 채택 (2026-05-04)
    28	
    29	P1 설계(`llm-providers-design.md`)에서 LLM Provider 추상화 방안으로 **Option β (LiteLLM facade 승격)** 가 채택되었다. P1 facade 는 다음 핵심 보장:
    30	
    31	- **모든 Worker / Hermes Agent 의 LLM 호출 = P1 facade 단일 진입점 경유**
    32	- **LiteLLM 직접 import = `adapters/llm/facade.py` 한 파일 한정** (`llm-providers-design.md` §4 답습)
    33	- **provider SDK (anthropic / openai / gemini 등) 직접 import = 어떤 작성 주체도 금지** (`llm-providers-design.md` §9 답습 — depcruise 룰 + AST 스캐너)
    34	- **모델명 분기 코드 (`if model == "claude": ...`) = 어떤 작성 주체도 금지** (`llm-providers-design.md` §9)
    35	
    36	자체 Adapter 작성은 v2.0 백업 옵션으로 보존되며, 본 ADR 은 (a) **P1 facade MVP 진입조건** + (b) **v2.0 으로 전환할 때의 정량 트리거** 를 명세한다.
    37	
    38	### 1.2 본 ADR 부재 시 위험
    39	
    40	이 ADR 이 없으면 다음 위험 발생 가능:
    41	
    42	- 매몰비용·관성으로 LiteLLM 에 영구 종속 (P1 facade lock-in)
    43	- 일시적 불편을 이유로 v2.0 자체 작성 시작 → ADR-004 본질 ("외부 SDK 우선") 재위반
    44	- **P1 facade MVP 진입조건 부재 → P2 v3 정식 채택 합의 시 P1 ↔ Hermes ↔ provider 계층 모호** (C-N 갱신 사유)
    45	- **Hermes PMO 가 자체 provider 소유 시도 → Provider Liquidity (헌법 5조 관용) 위반** (Provider Liquidity 5-way Layer 1 차단 부재 시)
    46	
    47	---
    48	
    49	## 2. P1 Facade MVP 진입조건 (C-N 신설, 2026-05-09)
    50	
    51	### 2.1 MVP 진입 시점
    52	
    53	**P1 facade MVP 는 다음 *모든* 조건 충족 시점에 *즉시* 진입 가능**:
    54	
    55	| # | 조건 | 충족 시점 |
    56	|---|------|---------|
    57	| (a) | ADR-008 (Hermes 도입) Option B 합의 APPROVE | 2026-05-04 ✅ 충족 |
    58	| (b) | P1 v2 (`llm-providers-design.md`) Option β 합의 APPROVE | 2026-05-04 ✅ 충족 |
    59	| (c) | LiteLLM 라이센스 = Apache 2.0 (또는 동등 호환) 확인 | 2026-05-04 시점 ✅ |
    60	| (d) | LiteLLM `Min 2 Active` provider 충족 가능성 (`llm-providers-design.md` §6) | 2026-05-04 시점 ✅ |
    61	
    62	본 4 조건 모두 *2026-05-04 시점 이미 충족* — **별도 트리거 없음**. ADR-008 + P1 v2 합의 APPROVE = MVP 진입 의무 도화선 (자체 Adapter v2.0 진입 트리거와 *별도 개념*).
    63	
    64	### 2.2 MVP 진입 의미
    65	
    66	P1 facade MVP 진입 = 다음 의무 *즉시* 활성화:
    67	
    68	| # | 의무 | 강제 매커니즘 |
    69	|---|------|----------|
    70	| 1 | LiteLLM 직접 import = `adapters/llm/facade.py` 한 파일 한정 | depcruise 룰 + AST 스캐너 (`llm-providers-design.md` §9) |
    71	| 2 | provider SDK 직접 import (anthropic / openai / gemini 등) = 모든 작성 주체 금지 | depcruise 룰 + pre-commit hook |
    72	| 3 | 모델명 분기 코드 (`if model == "claude": ...`) = 모든 작성 주체 금지 | depcruise 룰 + AST 스캐너 |
    73	| 4 | `Min 2 Active` provider 의무 (런타임 재검증) | `llm-providers-design.md` §6 |
    74	| 5 | OAuth 직결 금지 (P1 facade 경유 의무) | `llm-providers-design.md` §7 |
    75	| 6 | provider 추가 시 P1 facade `adapters/llm/facade.py` 변경만으로 가능 (단일 진입점) | `llm-providers-design.md` §4 + §10 |
    76	
    77	### 2.3 Hermes PMO ↔ Provider 분리 (C-N 핵심)
    78	
    79	**Hermes PMO (활성화 후 후보 시점) 가 provider 를 직접 소유하지 않는다** — 본 ADR-009 §2.3 영구 권위.
    80	
    81	| 영역 | Hermes PMO 권한 | P1 Facade 권한 |
    82	|----|-------------|-------------|
    83	| LLM 호출 진입점 소유 | ❌ (provider SDK 직접 import 금지) | ✅ (`adapters/llm/facade.py` 한 파일 한정) |
    84	| Provider 라우팅 결정 | ❌ (LiteLLM Router 위임) | ✅ (`llm-providers-design.md` §5) |
    85	| 모델명 분기 | ❌ (`if model == "claude":` 등 금지) | ✅ (config 기반, `llm-providers-design.md` §3 `llm-providers.yaml`) |
    86	| 요청 / 응답 표준화 | ❌ | ✅ (Request/Response 표준 스키마, `llm-providers-design.md` §4) |
    87	| 비용 / 관측성 / Redaction | ❌ (Tier-1 42 catalog 강제) | ✅ (`llm-providers-design.md` §8) |
    88	| OAuth refresh single-flight | ❌ | ✅ (`llm-providers-design.md` §7) |
    89	| Provider 추가 / 제거 / 교체 | ❌ (자기 격상 금지 — ADR-011 §2.4 T3) | ✅ (config 변경 + 사용자 명시 승인 — T2) |
    90	
    91	**근거** (영구 권위):
    92	- ADR-011 §2.3 (Hermes ≠ root of trust) — Hermes 권한 위계 답습
    93	- ADR-008 차단조건 #4 (P1 Facade 위임 — `hermes-adoption-design.md` §2.4 답습)
    94	- ADR-012 §원칙 6 (provider-neutral 강제) — Hermes 가 evidence ledger entry 작성 시에도 `agent` 필드 = provider-neutral identifier
    95	- 헌법 5조 관용 (Provider Liquidity 비협상)
    96	
    97	**Hermes PMO 격상 (활성화) 시점** (P2 v3 §2.6 7 단계 답습):
    98	- 본 ADR-009 §2.3 분리는 *Hermes PMO 격상 후에도 영구 유지* — 격상 = 책임 활성화 *까지*, provider 소유 *아님*
    99	- 격상 후 Hermes 가 provider SDK 직접 import 시도 = T3 위반 + Hermes-originated commit auto-reject (G3 §2.2 #20 답습)
   100	
   101	---
   102	
   103	## 3. 자체 LLM Adapter v2.0 진입 트리거 (초기 결정 — 변경 0건)
   104	
   105	### 3.0 P1 Facade MVP vs v2.0 트리거 분리 (C-N 신설)
   106	
   107	본 ADR 은 두 *별도* 개념을 다룬다:
   108	
   109	| 개념 | 위치 | 진입 시점 | 트리거 |
   110	|----|----|---------|------|
   111	| **P1 facade MVP** | §2 | 2026-05-04 (ADR-008 + P1 v2 합의 APPROVE 시점) | 별도 트리거 없음 (4 충족 조건 § 2.1) |
   112	| **자체 LLM Adapter v2.0** | §3.1 ~ §3.5 | 미정 (트리거 1개 이상 충족 시) | T1 ~ T4 정량 트리거 (§3.1~§3.4) |
   113	
   114	**핵심**: P1 facade MVP 는 *현재 운영 중* (LiteLLM Option β). 자체 Adapter v2.0 은 *백업 옵션* — 트리거 충족 시점에만 진입.
   115	
   116	### 3.1 결정 (Decision) — 자체 LLM Adapter v2.0 진입 결정 (변경 0건)
   117	
   118	자체 LLM Adapter v2.0 작성은 다음 **트리거 중 1개 이상** 이 충족될 때에만 시작한다. 추측·선호·"느낌"으로는 진입할 수 없다.
   119	
   120	#### T1. LiteLLM 신규 provider 미지원 (강한 트리거)
   121	- 본 프로젝트가 도입하려는 신규 provider/모델을 **LiteLLM이 2분기(약 6개월) 내 지원하지 않음**
   122	- AND 본 프로젝트가 제출한 PR이 거부 또는 무대응 1분기 이상 지속
   123	- AND 해당 provider/모델이 본 프로젝트 핵심 워크플로의 필수 요소
   124	
   125	#### T2. LiteLLM 라이센스 변경 (즉시 트리거)
   126	- LiteLLM이 Apache 2.0에서 비호환 라이센스로 전환
   127	- AND 새 라이센스가 본 프로젝트 운영 모델과 충돌 (예: 상업적 사용 제한)
   128	
   129	#### T3. LiteLLM 정상화 불가 결함 (강한 트리거)
   130	- LiteLLM에서 다음 결함 중 하나가 **2분기 이상 미해결**:
   131	  - 보안 결함 (CVE 등급 HIGH 이상)
   132	  - 본 프로젝트 핵심 워크플로 차단 버그 (회피 불가능)
   133	  - 응답 정규화 결함으로 Provider Liquidity 위반 (역설적 lock-in)
   134	
   135	#### T4. LiteLLM 운영 부담 정량 역전 (정량 트리거)
   136	- 자체 Adapter 추정 유지 부담(40~80h/년)보다 **LiteLLM 통합/우회 부담이 더 커짐**
   137	- 측정 기간: 4분기 연속
   138	- 측정 방법: facade 보강 시간 + LiteLLM 버그 우회 시간 + 버전 추적 시간을 분기별 기록
   139	
   140	### 3.2 트리거 미충족 시 — 자동 NO-GO (변경 0건)
   141	
   142	위 4개 트리거 중 어느 것도 충족되지 않으면, 자체 Adapter 작성 제안은 **자동 반려** 한다. 다음 같은 사유는 트리거가 아니다:
   143	- "외부 종속성 줄이고 싶다" (선호)
   144	- "LiteLLM 업데이트가 잦다" (불편)
   145	- "모든 코드를 자가 통제하고 싶다" (취향)
   146	- "특정 provider만 사용하면 되니 LiteLLM 과잉" (단기적 판단)
   147	
   148	---
   149	
   150	## 4. 선택지 (Options Considered) — 변경 0건
   151	
   152	### 옵션 A: 트리거 없이 v2.0 시점만 명시 (예: "1년 후 재검토")
   153	- 장점: 단순
   154	- 단점: 시점 도달 시 정당성 없이 자동 진입 가능 → ADR-004 본질 재위반
   155	
   156	### 옵션 B: 정량 트리거 4종 명세 (T1~T4) ⭐ 채택
   157	- 장점: 객관적 의사결정, ADR-004 본질 보호, 매몰비용 회피
   158	- 단점: 트리거 측정 부담 (특히 T4의 시간 기록)
   159	
   160	### 옵션 C: "필요 시 결정"으로 미명세
   161	- 장점: 유연성
   162	- 단점: 본 ADR 작성 목적 자체가 무력화
   163	
   164	---
   165	
   166	## 5. Provider Liquidity 5-way Multi-layer Defense (C-N 갱신, 2026-05-09)
   167	
   168	본 ADR-009 는 **Provider Liquidity 5-way Multi-layer Defense 의 Layer 1 모법 ADR** 이다 (ADR-012 §원칙 5 발행으로 확정).
   169	
   170	| Layer | 책임 영역 | 모법 / 답습 |
   171	|------|--------|---------|
   172	| **Layer 1** (코드 lock-in 차단) | 모든 작성 주체의 provider SDK 직접 import / 모델명 분기 코드 차단 | **본 ADR-009 §2.2** + G2 GP-5 (depcruise 룰) + `llm-providers-design.md` §9 |
   173	| Layer 2 (Hermes-originated lock-in 변경 차단) | Hermes 작성 주체 한정 차단 | G3 §6.4 + 본 ADR-009 §2.3 |
   174	| Layer 3 (Skill 메타데이터 차원) | `provider_bindings` schema *required*/*exclusive* 금지 | G4 §3.5 |
   175	| Layer 4 (export format 차원) | JSONL Hermes 의존 0 + 최소 2 provider 재해석 가능 | G4 §4.3 |
   176	| Layer 5 (Evidence 형식 차원) | 11 필드 모두 provider-neutral 강제 | ADR-012 §2.1 원칙 6 + G4 §4.2 |
   177	
   178	**5 Layer 모두 충족** 시 Provider Liquidity 의 *완결성* 확보. 1 Layer 만 깨져도 lock-in 위험 잔존.
   179	
   180	### 5.1 자체 Adapter v2.0 진입 시 Provider Liquidity 보장
   181	
   182	자체 Adapter v2.0 진입 시점 (트리거 1+ 충족) 에도 **Provider Liquidity 5-way Layer 1~5 모두 보존 의무**:
   183	
   184	- Layer 1: v2.0 자체 Adapter 도 단일 진입점 강제 (provider SDK 직접 import 금지)
   185	- Layer 2 ~ Layer 5: 변경 없음 (Hermes / Skill / JSONL / Evidence 차원은 v2.0 무관)
   186	- v2.0 진입 = *수단 변경* (LiteLLM → 자체 Adapter), *목적 보존* (Provider Liquidity 비협상) — ADR-011 §2.1 (a)~(e) 5조건 답습 의무
   187	
   188	---
   189	
   190	## 6. 근거 (Rationale)
   191	
   192	### 6.1 초기 근거 (변경 0건)
   193	
   194	P1 v2 설계가 LiteLLM 의존을 채택하는 만큼, 그 의존을 끊는 의사결정도 동일한 엄격함으로 게이트되어야 한다. ADR-004는 "외부 SDK 부족 입증 후에만 v2.0"이라 명시했고, 본 ADR은 그 "입증"을 정량 트리거로 구체화한 것이다.
   195	
   196	### 6.2 C-N 갱신 근거 (2026-05-09)
   197	
   198	P2 v3 정식 채택 합의 진입 *전*, 다음 모호 영역 해소 의무:
   199	
   200	1. **P1 facade MVP 진입조건 부재** — P2 v3 §1.6 (P1 과의 관계) 참조 시 "MVP 가 언제 시작됐고 어떤 의무가 활성화되어 있는가" 모호 → 본 갱신 §2.1 + §2.2 명시
   201	2. **Hermes PMO ↔ provider 계층 분리 부재** — Hermes PMO 격상 후 provider 소유 가능성 시사 → 본 갱신 §2.3 영구 권위로 차단
   202	3. **Provider Liquidity 5-way Multi-layer Defense 모법 ADR 부재** — ADR-012 §원칙 5 가 "5-way" 명명을 발행했으나 Layer 1 의 *모법 ADR* 부재 → 본 갱신 §5 명시
   203	4. **v2.0 트리거 vs MVP 조건 분리 부재** — 두 개념 혼동 가능 → 본 갱신 §3.0 매트릭스 명시
   204	5. **P2 v3 cross-reference 부재** — 본 ADR 이 P2 v3 정식 채택 합의에서 인용 가능하도록 §8 강화
   205	
   206	본 갱신 = *MVP 조건 명시* + *cross-reference 강화* + *모법 ADR 권위 확정* 한정. **자체 Adapter v2.0 트리거 (T1~T4) 본문 변경 0건** + **핵심 결정 (옵션 B 채택) 변경 0건** → 단축 합의 적격 (사용자 명시 답습).
   207	
   208	---
   209	
   210	## 7. 합의 결과
   211	
   212	### 7.1 초기 3+1 합의 (2026-05-04, 변경 0건)
   213	
   214	P1 (Option β) 합의의 일부로 다뤄짐. 별도 ADR 작성 의무는 Bβ-4 항목.
   215	
   216	| 출처 | 핵심 |
   217	|------|------|
   218	| Agent C | "v2.0 진입조건을 정량 트리거로 명시 — 매몰비용 누적 회피" |
   219	| Reviewer | "Option β 채택 시 진입조건 ADR 작성 의무 (Bβ-4)" |
   220	
   221	### 7.2 C-N 갱신 단축 합의 (2026-05-09)
   222	
   223	세부: `docs/review/3plus1-consensus-2026-05-09-c-n-adr-009-update.md`
   224	
   225	| 차원 | 판정 | 핵심 근거 |
   226	|------|----|---------|
   227	| P1 facade MVP 진입조건 명시 (§2 신설) | **PASS** | 4 충족 조건 (a)~(d) 명시 + 6 의무 매커니즘 명시 + 진입 시점 = 2026-05-04 답습 |
   228	| Hermes PMO ↔ provider 분리 (§2.3) | **PASS** | ADR-011 §2.3 + ADR-008 차단조건 #4 + ADR-012 §원칙 6 + 헌법 5조 답습 |
   229	| Provider Liquidity 5-way 모법 ADR 권위 (§5) | **PASS** | ADR-012 §원칙 5 발행으로 5-way 명명 확정 + 본 ADR 이 Layer 1 모법 명시 |
   230	| v2.0 트리거 vs MVP 조건 분리 (§3.0) | **PASS** | 분리 매트릭스 명시 + 두 개념 *별도 진입 시점* 명료 |
   231	| P2 v3 cross-reference 강화 (§8) | **PASS** | P2 v3 §1.6 + §6 + §10 인용 가능 |
   232	| **자체 Adapter v2.0 트리거 (T1~T4) 변경** | **변경 0건** | 단축 합의 적격 (사용자 명시 답습) |
   233	| **핵심 결정 (옵션 B 채택) 변경** | **변경 0건** | 단축 합의 적격 |
   234	| **Provider Liquidity 영향** | **5-way 답습 강화** | 본 ADR 이 Layer 1 모법으로 영구 명시됨 (보호 강도 ↑) |
   235	| **메타 편향 통제** | **명시** | 본 갱신은 자체 코드 우호 결론 부재 — Hermes 권한 *축소* 답습 (Hermes ↔ provider 분리) |
   236	
   237	---
   238	
   239	## 8. 결과 (Consequences)
   240	

codex
primary brief는 scope와 deferred 경계를 상당히 명시하고 있습니다. 이제 설계 v2 후반부와 ADR/governance/code를 대조해서 인용 정확성, 실행 가능성, 누락된 blocking risk를 확인하겠습니다.
exec
/bin/bash -lc "nl -ba docs/architecture/llm-providers-design.md | sed -n '320,760p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
   320	
   321	Facade 내부:
   322	  1. routing[model_alias] → provider_key
   323	  2. validate_config() 통과 (Min 2 active)
   324	  3. LiteLLM Router에 위임 (model_id 매핑, fallback chain 적용)
   325	  4. 응답 정규화: LiteLLM 표준 → LLMResponse + LLMMetadata 화이트리스트
   326	  5. 메트릭 기록 (redaction 적용)
   327	  6. 응답 반환
   328	```
   329	
   330	---
   331	
   332	## 5. 라우팅 — LiteLLM Router 위임
   333	
   334	### 5.1 Router 설정 매핑
   335	
   336	본 설계의 `llm-providers.yaml`을 LiteLLM Router 형식으로 변환:
   337	
   338	```python
   339	def to_router_config(providers_yaml):
   340	    return {
   341	        "model_list": [
   342	            {
   343	                "model_name": alias,                          # routing alias
   344	                "litellm_params": {
   345	                    "model": providers[alias]["litellm_model"],
   346	                    "api_key_env": providers[alias].get("api_key_env"),
   347	                    # ...
   348	                },
   349	            }
   350	            for alias in providers_yaml["routing"].values()
   351	        ],
   352	        "router_settings": {
   353	            "fallbacks": build_fallbacks(providers_yaml),
   354	            "cooldown_time": 60,                              # blocked status 자동 전환 트리거
   355	            "num_retries": 3,
   356	            "timeout": 30,
   357	        },
   358	    }
   359	```
   360	
   361	### 5.2 폴백 race 완화 (R8 보강)
   362	
   363	LiteLLM Router의 fallback에 추가 보강:
   364	
   365	| Race | LiteLLM 기본 | 본 facade 보강 |
   366	|------|-------------|--------------|
   367	| 헬스체크 전이 race | cooldown_time으로 일부 흡수 | call 단위 immutable snapshot — 호출 시점 routing 캡처 |
   368	| Rate limit thundering herd | num_retries + 백오프 | per-provider semaphore + 지터 (jitter) |
   369	| OAuth refresh race | 없음 | **R6 single-flight lock** (§7.2) |
   370	| Streaming 폴백 이중 출력 | 없음 | **first-token 후 폴백 금지** 규칙 — facade가 stream 도중 끊기면 에러 발생, 폴백 안 함 |
   371	| active=2 검증 race | 없음 | 자동 강등 시 **R4 재검증** (§6.2) |
   372	
   373	### 5.3 명시 vs 자동
   374	
   375	```
   376	명시: llm.complete(LLMRequest(model_alias="consensus_agent_b", ...))
   377	자동: llm.complete(LLMRequest(messages=[...]))  → routing[default]
   378	```
   379	
   380	`model_alias`는 의미 없는 명칭만 허용. provider/모델명을 alias에 인코딩 금지(예: `claude_only_path` 같은 alias는 lint 룰로 차단 — 위반 패턴 #1 회피 차단).
   381	
   382	---
   383	
   384	## 6. Min 2 Always-On + 런타임 재검증 (R4 보강)
   385	
   386	### 6.1 시작 시점 검증 (불변)
   387	
   388	```python
   389	def validate_config(config):
   390	    active = [(k, v) for k, v in config["providers"].items() if v["status"] == "active"]
   391	
   392	    if len(active) < 2:
   393	        raise ConfigError("Min 2 active 정책 위반 (시작 시) — ADR-008 #5")
   394	
   395	    types = [v["type"] for k, v in active]
   396	    if len(set(types)) != len(types):
   397	        raise ConfigError(f"동일 type 2개 active 금지 — 3+1 합의 R5")
   398	```
   399	
   400	### 6.2 런타임 재검증 (R4 신규)
   401	
   402	**모든 강등 경로**에서 active 카운트를 재계산하고 부족하면 degraded 모드로 전환:
   403	
   404	```python
   405	async def _on_active_degraded(self, provider_key: str):
   406	    """헬스체크 자동 강등, 한도 도달 폴백, blocked 전환 등에서 호출."""
   407	    self._mark_provider_blocked(provider_key)
   408	    active_count = self._count_active()
   409	
   410	    if active_count < 2:
   411	        await self._enter_degraded_mode(reason=f"active={active_count} (need ≥2)")
   412	```
   413	
   414	### 6.3 Degraded 모드 (R4 신규)
   415	
   416	```
   417	Degraded 모드 진입 시:
   418	  1. stderr 경고 + 메트릭 알람 (전 시스템 알림)
   419	  2. 새 호출은 처리 가능한 alias만 수용 (degraded provider 의존 alias는 503)
   420	  3. 사용자 노출 방식 (P3 라이프사이클과 연계 결정 필요):
   421	     [선택지] UI 배너 / 로그만 / 메트릭 알람만 — 미해결 결정 #5
   422	  4. 강등 provider 복구 시 자동 active 복귀 + degraded 모드 해제
   423	  5. degraded 모드 30분 지속 시 운영자 호출 (escalation)
   424	```
   425	
   426	### 6.4 시나리오 — Claude Max 구독 취소
   427	
   428	```
   429	Step 1: 사용자가 llm-providers.yaml에서 anthropic-claude-oauth status=blocked
   430	Step 2: anthropic-claude-api는 별도 결제 → 영향 없음
   431	Step 3: ollama-llama-local 그대로 active → 시스템 정상
   432	
   433	만약 anthropic-claude-api도 미사용이라면:
   434	Step 1-2: oauth 차단 + api 미설정 시 동일 type 검증 통과 (anthropic 없음)
   435	Step 3: Min 2 검증 → openai + ollama 활성 시 통과
   436	```
   437	
   438	---
   439	
   440	## 7. OAuth 직결 금지 정책 + Credentials 처리 (R7 보강)
   441	
   442	### 7.1 우선순위
   443	
   444	| 순위 | 인증 | 사용 조건 |
   445	|-----|------|---------|
   446	| 1 | `api_key` | 기본. 모든 새 코드 |
   447	| 2 | `oauth_subscription` | 비용 절감 시. 단 §7.2~7.3 조건 충족 |
   448	
   449	### 7.2 OAuth 사용 시 필수 조건
   450	
   451	OAuth provider를 active로 전환하려면:
   452	1. ✅ 같은 type의 API 키 provider가 **최소 1개 standby** 등록 (즉시 폴백 가능)
   453	2. ✅ **Single-flight lock** 적용 — 동시 호출이 만료된 토큰을 동시에 refresh하지 못하도록 (R6 보강)
   454	3. ✅ 헬스체크 활성화 (dry probe만 — §9.2)
   455	4. ✅ 정책 변동 모니터링 task 등록 (월 1회 ToS 검토)
   456	5. ✅ ADR-008 R4 인지 (Claude OAuth 버그 4종)
   457	
   458	```python
   459	# OAuth refresh single-flight (R6)
   460	class SingleFlightLock:
   461	    async def refresh_with_lock(self, provider_key: str):
   462	        async with self._locks[provider_key]:   # provider별 lock
   463	            if not self._needs_refresh(provider_key):
   464	                return self._cached_token(provider_key)
   465	            new_token = await self._do_refresh(provider_key)
   466	            self._cache_token(provider_key, new_token)
   467	            return new_token
   468	```
   469	
   470	### 7.3 Credentials 처리 (R7 신규)
   471	
   472	| 항목 | 정책 |
   473	|-----|------|
   474	| **경로 환경변수화** | `oauth_credentials_env: CLAUDE_CREDS_PATH` — yaml에 절대 경로 평문 금지 |
   475	| **파일 권한** | `chmod 600` 강제 검증 (시작 시) — 권한 위반 시 fail-fast |
   476	| **Docker mount** | `:ro` (read-only) + 권한 검증 |
   477	| **로그/메트릭 echo 금지** | RedactionFilter가 `auth/token/key/secret` 패턴 자동 strip (§8.2) |
   478	| **테스트** | 토큰이 응답·로그·메트릭 어디에도 echo되지 않는지 단위 테스트 필수 |
   479	
   480	### 7.4 ChatGPT Pro Codex OAuth 특별 조항
   481	
   482	- **개인 단일 사용자만** (ToS — third-party 집계 금지)
   483	- 정책 변동 시 즉시 standby 전환
   484	- 변동 모니터링: OpenAI 정책 페이지 + 커뮤니티 (Reddit, GitHub)
   485	
   486	---
   487	
   488	## 8. 비용·관측성 + Redaction (R3 보강)
   489	
   490	### 8.1 LiteLLM Callback 활용
   491	
   492	LiteLLM의 callback 시스템에 본 도메인 메트릭 + redaction을 등록:
   493	
   494	```python
   495	litellm.success_callback = [DomainMetricsCallback(redactor=...)]
   496	litellm.failure_callback = [DomainMetricsCallback(redactor=...)]
   497	
   498	class DomainMetricsCallback:
   499	    def log_event(self, event):
   500	        # event는 LiteLLM의 표준 이벤트 객체
   501	        record = {
   502	            "request_id": event.request_id,
   503	            "timestamp": event.timestamp,
   504	            "model_alias": self._reverse_alias(event.model),
   505	            "provider_used": event.provider,
   506	            "fallback_chain": event.fallback_chain,
   507	            "input_tokens": event.usage.prompt_tokens,
   508	            "output_tokens": event.usage.completion_tokens,
   509	            "cost_estimate": event.cost,
   510	            "latency_ms": event.duration_ms,
   511	            "status": event.status,
   512	        }
   513	        # ⚠️ Redaction 의무 (R3) — 모든 필드를 redactor 통과
   514	        record = self._redactor.scrub(record)
   515	        self._sink.write(record)
   516	```
   517	
   518	### 8.2 Redaction 정책 (R3 신규)
   519	
   520	```python
   521	class RedactionFilter:
   522	    """모든 응답·예외·메트릭에서 비밀값 자동 strip."""
   523	
   524	    PATTERNS = [
   525	        re.compile(r"sk-[a-zA-Z0-9]{20,}"),         # OpenAI API key
   526	        re.compile(r"sk-ant-[a-zA-Z0-9]{20,}"),     # Anthropic API key
   527	        re.compile(r"Bearer [a-zA-Z0-9._-]+"),      # Bearer token
   528	        re.compile(r"\"(api_key|token|auth|secret|password|credential)\"\s*:\s*\"[^\"]+\""),
   529	    ]
   530	    KEY_BLACKLIST = {"api_key", "token", "secret", "auth", "credential", "authorization"}
   531	
   532	    def scrub(self, obj):
   533	        # dict는 키 기반 + 값 패턴 매칭
   534	        # str은 패턴 매칭으로 [REDACTED] 치환
   535	        # ...
   536	```
   537	
   538	**화이트리스트 vs 블랙리스트** (미해결 결정 #4): 본 설계는 **블랙리스트(패턴 + 키 매칭)** 채택. 화이트리스트는 운영 부담 ↑, 새 메타 추가 시마다 화이트리스트 갱신 필요. 단 `LLMResponse.metadata`는 데이터클래스로 화이트리스트화(R2)되어 있어 누출 통로 자체가 좁음.
   539	
   540	### 8.3 의사결정 대시보드
   541	
   542	월별 집계로 다음 지표 노출:
   543	- provider별 비용 (구독 취소/유지 결정용)
   544	- provider별 가용성 (failure rate)
   545	- alias별 평균 응답 시간
   546	- fallback 발생 빈도
   547	- OAuth refresh 빈도 (R6 lock 활용도)
   548	
   549	### 8.4 한도 알림
   550	
   551	`flat_subscription`:
   552	- 사용량 80% → 경고 + 메트릭 알람
   553	- 사용량 100% → 자동 폴백 → R4 재검증 트리거
   554	
   555	---
   556	
   557	## 9. Liquidity 위반 패턴 차단
   558	
   559	### 9.1 위반 패턴 카탈로그 — LiteLLM 자연 차단 활용
   560	
   561	| # | 패턴 | LiteLLM 채택 시 차단 | 추가 메커니즘 |
   562	|---|------|---------------------|-------------|
   563	| 1 | 모델명/provider 분기 코드 | 모델명은 LiteLLM 형식(`anthropic/...`)으로 yaml에만 존재 | depcruise: alias 외 모델명 문자열 금지 |
   564	| 2 | provider별 응답 후처리 함수 분리 | LiteLLM이 OpenAI 포맷으로 통일 → 후처리 단일 | `LLMResponse.metadata` 화이트리스트(R2) |
   565	| 3 | 스킬/프롬프트 안 특정 모델 가정 | LiteLLM 무관 | 코드 리뷰 + 테스트(다른 alias로도 통과해야 함) |
   566	| 4 | 메모리에 provider별 메타 저장 | LiteLLM이 raw 메타 통일 | `LLMMetadata` 화이트리스트(R2) |
   567	| 5 | provider 전용 인증 갱신 로직 | LiteLLM이 자체 처리 | facade 외 OAuth 코드 금지 + R6 single-flight |
   568	| 6 | 포맷별 다운스트림 파서 | LiteLLM 통일 | `LLMResponse.content` 단일 필드 |
   569	
   570	### 9.2 Health Check — Dry Probe (R9 보강)
   571	
   572	실 토큰을 매 60s마다 echo하면 인증 노출 (R6 위험). LiteLLM Router의 health_check를 **dry mode**로 사용:
   573	
   574	```python
   575	# 무토큰 헬스 검증
   576	async def health(self) -> dict[str, bool]:
   577	    """endpoint 도달성만 확인. 실 인증 토큰 사용 안 함."""
   578	    results = {}
   579	    for alias, provider in self._active_providers().items():
   580	        try:
   581	            await self._router.health_check(provider, dry=True)  # endpoint ping만
   582	            results[alias] = True
   583	        except Exception:
   584	            results[alias] = False
   585	    return results
   586	```
   587	
   588	MVP에 dry probe 헬스체크 포함 (이전 P1의 §6.3 시나리오와 일관성 확보 — A 발견 보강).
   589	
   590	### 9.3 정적 검사 — depcruise (단순화, Bβ-2)
   591	
   592	```javascript
   593	// .depcruise.cjs (개략, P5 문서로 상세화)
   594	{
   595	  forbidden: [
   596	    {
   597	      name: "no-direct-llm-sdk",
   598	      from: { pathNot: "^src/adapters/llm/facade\\.py$" },
   599	      to: { path: "^(litellm|anthropic|openai|@anthropic-ai|@openai|ollama)" }
   600	    },
   601	    {
   602	      name: "no-llm-via-httpx",
   603	      // grep 보조: src/ 안에서 'api.anthropic.com', 'api.openai.com' 등 endpoint 문자열 직접 사용 금지
   604	    },
   605	    {
   606	      name: "no-model-name-in-code",
   607	      // grep: 'claude-opus', 'gpt-' 등 모델 ID 패턴 src/ 안 금지 (yaml만 허용)
   608	    },
   609	  ]
   610	}
   611	```
   612	
   613	LiteLLM 채택 시 룰이 6종 → 3종으로 단순화 (Option α 대비).
   614	
   615	### 9.4 정적 검사 — AST 동적 import 차단 (R8/R9 보강)
   616	
   617	```python
   618	# pre-commit: ruff custom rule 또는 AST 스캐너
   619	# src/ 하위에서 다음 패턴 금지:
   620	#   importlib.import_module("anthropic")
   621	#   __import__("openai")
   622	#   exec("import litellm")
   623	```
   624	
   625	### 9.5 코드 리뷰 체크리스트
   626	
   627	- [ ] LLM 호출이 모두 facade를 거치는가?
   628	- [ ] 모델/provider 이름이 코드에 하드코딩되지 않았는가? (yaml만 허용)
   629	- [ ] 응답 처리가 `LLMResponse` 표준 필드만 사용하는가? (metadata raw dict 접근 금지)
   630	- [ ] 새 provider 추가 시 `llm-providers.yaml`만 수정했는가?
   631	- [ ] OAuth 사용 시 §7.2~7.3 조건을 충족하는가?
   632	- [ ] 메트릭/로그에 비밀값 echo 가능 경로가 없는가?
   633	
   634	---
   635	
   636	## 10. 마이그레이션 경로
   637	
   638	### 10.1 Provider 추가
   639	
   640	```
   641	새 모델 "Llama 4 70B" 추가:
   642	  Step 1: llm-providers.yaml에 항목 추가 (litellm_model: ollama/llama-4-70b)
   643	  Step 2: 검증 (테스트로 호출 동작 확인)
   644	  Step 3: status: active 전환 (또는 routing alias 할당)
   645	  Step 4: 끝.
   646	```
   647	
   648	### 10.2 Provider 제거
   649	
   650	```
   651	"openai-gpt-oauth" 제거 (정책 변동 등):
   652	  Step 1: status: blocked → 즉시 모든 호출 차단 → R4 재검증 트리거
   653	  Step 2: routing alias 재할당 확인
   654	  Step 3: 1주 모니터링
   655	  Step 4: yaml 항목 삭제
   656	```
   657	
   658	### 10.3 모델 변경
   659	
   660	```
   661	Claude Opus 4.7 → Claude Opus 5.0:
   662	  Step 1: yaml의 litellm_model 수정 (anthropic/claude-opus-5-0)
   663	  Step 2: 끝.
   664	```
   665	
   666	### 10.4 응급 폴백
   667	
   668	```
   669	Anthropic + OpenAI 동시 장애:
   670	  자동: LiteLLM Router fallback → openrouter-fallback 또는 ollama-llama-local 도달
   671	  수동: standby provider를 active로 임시 전환 (R4 재검증 자동 통과)
   672	```
   673	
   674	---
   675	
   676	## 11. 적용 시나리오
   677	
   678	### 11.1 Hermes Phase 1 (1~2주) — 3 active type 다양성 (A 발견 보강)
   679	
   680	```
   681	설정:
   682	  active: [anthropic-claude-api, openai-gpt-api, ollama-llama-local]
   683	  routing.default: anthropic-claude-api
   684	  routing.background_jobs: ollama-llama-local
   685	
   686	목적: API 키만 사용. OAuth 직결 금지 정책 검증. Min 2 + type 다양성 동시 충족.
   687	검증: 비핵심 작업을 Hermes로 수행, facade 정상 동작 확인.
   688	```
   689	
   690	**이전 P1의 Phase 1 문제 (ollama 미포함, §6.2 type 다양성 위반) 해소**.
   691	
   692	### 11.2 Hermes Phase 2 (2~4주) — 3+1 합의 다중 LLM
   693	
   694	```
   695	설정:
   696	  active: [anthropic-claude-api, openai-gpt-api, ollama-llama-local]
   697	  routing:
   698	    consensus_agent_a: anthropic-claude-api
   699	    consensus_agent_b: openai-gpt-api
   700	    consensus_agent_c: ollama-llama-local
   701	    reviewer: anthropic-claude-api
   702	
   703	목적: 3+1 합의의 메타 한계 해소 (전 에이전트 Claude → 다중 모델).
   704	검증: 3+1 다중 모델 합의 실행, 결과 품질 ≥ 단일 Claude.
   705	```
   706	
   707	### 11.3 Claude Max 취소 시나리오
   708	
   709	```
   710	사용자: Claude Max 비용 부담 → 취소.
   711	Step 1: anthropic-claude-oauth status=blocked → R4 재검증 → active 카운트 OK
   712	Step 2: anthropic-claude-api는 영향 없음 (별도 결제)
   713	Step 3: 끝. 코드 변경 0.
   714	```
   715	
   716	### 11.4 신규 provider 추가 (Gemini)
   717	
   718	```
   719	Step 1: yaml에 google-gemini-api 추가 (litellm_model: gemini/gemini-2.5-pro)
   720	Step 2: status: standby → 테스트
   721	Step 3: status: active (단 동일 type 검증 통과 시)
   722	Step 4: 끝. facade 코드 수정 0 (LiteLLM이 google_genai 자체 지원).
   723	```
   724	
   725	신규 provider type 추가도 LiteLLM이 처리 → facade 변경 불필요.
   726	
   727	---
   728	
   729	## 12. ADR-008 차단조건 매핑
   730	
   731	| 차단조건 | 본 설계의 충족 메커니즘 |
   732	|---------|----------------------|
   733	| #1 SQLCipher 암호화 | 본 문서 범위 외 (P2) |
   734	| #2 JSONL export | 본 문서 범위 외 (P2) |
   735	| #3 v0.x 버전 핀 | 본 문서 범위 외 (P2) |
   736	| **#4 provider 어댑터 1개 추상화 + 분기 금지** | **§4 LLMFacade (단일) + §9.3 depcruise + §9.4 AST 차단** |
   737	| **#5 최소 2 provider always-on** | **§6.1 시작 시 fail-fast + §6.2 런타임 재검증 + §6.3 degraded 모드** |
   738	| #6 Docker 격리 | 본 문서 범위 외 (P2) |
   739	
   740	---
   741	
   742	## 13. ADR-004 정합성 — 본질 일치
   743	
   744	ADR-004 핵심 원칙: **"자체 어댑터 불필요 — 외부 SDK 활용. 자체 어댑터는 외부 SDK 부족 입증 후에만(v2.0)"**
   745	
   746	본 P1은 ADR-004를 그대로 따른다:
   747	- LiteLLM(외부 SDK)이 1차
   748	- 자체 코드는 facade 100 LOC + 도메인 보강만
   749	- 자체 Adapter 작성은 v2.0 — 진입조건은 **ADR-009**에서 명세
   750	
   751	**3+1 합의 (Agent C) 결과**: 이전 초안(자체 Adapter 1차)은 ADR-004 본질 위반이었으나, Option β 채택으로 정합성 회복.
   752	
   753	---
   754	
   755	## 14. 다른 ADR과의 정합성
   756	
   757	| 관련 문서 | 정합성 |
   758	|---------|--------|
   759	| **ADR-004** (생성 AI 확장성) | **본질 일치** — 외부 SDK(LiteLLM) 우선 + config-driven |
   760	| **ADR-006** (환경 변수 + Docker) | API 키 환경 변수, OAuth credentials env 보간(R7) + Docker mount :ro |

exec
/bin/bash -lc "nl -ba docs/decisions/ADR-008-hermes-adoption-decision.md | sed -n '1,260p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# ADR-008: Hermes Agent 도입 결정 (Option B)
     2	
     3	**상태**: 승인 (3+1 합의 완료, 사용자 Option B 선택)
     4	**날짜**: 2026-05-04
     5	**의사결정자**: 사용자 + 3+1 에이전트 합의
     6	
     7	---
     8	
     9	## 맥락 (Context)
    10	
    11	사용자가 "Hermes Agent를 메인 오케스트레이터로 도입, Claude Opus 4.7과 GPT-5.5를 서브 LLM으로 활용"하는 시스템 진화를 제안. 현재 시스템은 Claude Code 단일 의존이며, 사용자는 모델/구독 교체의 자유를 강하게 요구함 (Provider Liquidity 하드 제약: "Claude Max 사용중이지만 모델 성능에 따라 구독 취소나 모델 변경이 용이해야함").
    12	
    13	## 결정 (Decision)
    14	
    15	**Option B 채택**: Hermes를 메인 오케스트레이터로 단계 도입하되, **6개 차단조건이 모두 충족된 후에만 다음 Phase로 진입**한다.
    16	
    17	### 6개 차단조건 (비협상)
    18	1. **SQLCipher**로 Hermes SQLite 암호화 + redaction 필터 (헌법 제8조 준수)
    19	2. **JSONL export 표준** + 메모리/스킬 마이그레이션 경로 정의 (Hermes lock-in 회피)
    20	3. v0.x API **버전 핀** + 회귀 테스트 + 카나리 환경
    21	4. **provider 어댑터 1개 추상화** + 분기 코드 금지 (depcruise로 강제)
    22	5. **최소 2 provider always-on** (단일 구독 의존 금지)
    23	6. Docker **격리 + egress 화이트리스트**
    24	
    25	### 단계 마이그레이션
    26	- **Phase 1** (1~2주): Hermes worktree 설치, **API 키만 사용**(OAuth 직결 금지), 비핵심 작업 검증
    27	- **Phase 2** (2~4주): Layer 5(3+1 합의)만 Hermes 서브에이전트로 이전 (A=Claude / B=GPT / C=로컬)
    28	- **Phase 3** (조건부): Hook 계층 watchexec 재구축 + provider 어댑터 본격 적용. **선결조건**: Phase 2 메트릭 ≥ 현 시스템
    29	
    30	## 선택지 (Options Considered)
    31	
    32	### Option A: LiteLLM 우선 + Hermes 좁은 PoC (3+1 권장 ★★★★★)
    33	- 장점: Provider Liquidity 본업 충족, 기존 SDD/TDD 자산 100% 보존, 즉시 시작
    34	- 단점: Hermes 셀프-임프루빙 가치 일부 늦게 확인
    35	
    36	### Option B: Hermes 메인 + 6개 차단조건 단계 도입 ⭐ **채택**
    37	- 장점: 사용자 원안 직접 실현, 셀프-임프루빙 빠른 체험
    38	- 단점: 차단조건 6개 미충족 위험, v0.x 불안정, Hook 재구축 공수 미지수
    39	
    40	### Option C: 6개월 보류
    41	- 장점: 신생 프레임워크 리스크 회피
    42	- 단점: 다중 LLM 활용·Liquidity 개선 지연
    43	
    44	## 근거 (Rationale)
    45	
    46	3+1 합의는 Option A를 1순위로 권장했으나, 사용자가 의식적으로 Option B를 선택. 사용자 의지·선호 존중. 단, 6개 차단조건은 **비협상** — 미충족 시 자동 NO-GO하며, Hermes 도입을 중단하고 Option A로 자동 폴백한다.
    47	
    48	## 3+1 에이전트 합의 결과
    49	
    50	| 에이전트 | 의견 | 핵심 근거 |
    51	|---------|------|----------|
    52	| Agent A (구현) | 조건부 GO | 8-Layer 통합 MEDIUM, Phase 1·2 즉시 가능, Phase 3는 Hook 재구축 PoC 성공 시 |
    53	| Agent B (품질) | GO with strict conditions | R1 학습루프 평문(CRITICAL), R2 Hermes lock-in(CRITICAL), 6개 차단조건 미충족 시 HOLD |
    54	| Agent C (대안) | LiteLLM 우선 권장 (Option A) | Liquidity는 도구 추상화 문제, Hermes만의 솔루션 아님 |
    55	| **Reviewer** | **Option A 1순위, B는 차단조건 충족 시 가능** | 메타 한계 보정으로 C에 가중치, 사용자 선호 시 B 진행 가능 |
    56	
    57	## CRITICAL 위험 (운영 중 상시 감시)
    58	
    59	- **R1 학습루프 평문 누적**: Hermes SQLite FTS5에 사용자 컨텍스트·LLM 응답·환경변수 echo가 평문 영구 저장. **헌법 제8조 직접 위반**. 차단조건 #1 미구현 시 자동 NO-GO.
    60	- **R2 Hermes 자체 lock-in**: 누적 학습 결과(스킬/메모리/프로필)는 Hermes 떠나면 손실. Provider Liquidity 정신 위반. 차단조건 #2 미정의 시 자동 NO-GO.
    61	- **A-meta ChatGPT Pro Codex CLI OAuth ToS 위반 가능성**: 위반 시 구독 강제 해지 → 시스템 정지. **API 키 경로만 사용**.
    62	- **R4 Claude Max OAuth race**: 다수 미해결 버그(#15080, #6475, #12905, #10575) — Hermes 동시 호출 시 무한 인증루프 가능. API 키 경로 우선.
    63	- **R8 단일 구독 의존**: 어떤 단계에서도 single point of failure 금지. 차단조건 #5로 강제.
    64	
    65	## 메타 한계 (사용자 인지 필요)
    66	
    67	본 합의는 3 Claude 에이전트가 작성. Hermes(외부 도구)에 대한 평가에 친화 편향 가능. Reviewer가 Agent C 회의적 입장에 의식적 가중치 부여로 보정함. Option B 진행 중에도 외부(비-Claude) 검증 권장.
    68	
    69	## 결과 (Consequences)
    70	
    71	- **긍정적**: 다중 LLM 환경 구축, 셀프-임프루빙 학습루프 도입 시도, Provider Liquidity 강제 메커니즘 정착
    72	- **부정적**: 신생 프레임워크 리스크 감수, Hook 재구축 공수 발생, v0.x API 변동 대응 부담, R1/R2 차단조건 미충족 시 전면 폴백 위험
    73	- **주의사항**:
    74	  - 6개 차단조건 중 1개라도 미충족 시 도입 중단 → Option A 자동 폴백
    75	  - 진행 중에도 정기적 재평가 (Phase 종료마다)
    76	  - 차단조건 충족 검증은 별도 SDD 문서로 명세 예정
    77	  - Provider Liquidity 위반 패턴 6종(모델명 분기/provider별 후처리/스킬 내 모델 가정 등)은 depcruise 룰로 정적 차단
    78	
    79	---
    80	
    81	**관련 문서** (2026-05-09 후속 9 cross-reference 갱신, 결정 내용 변경 0건 — 단축 합의 APPROVE Reviewer-only):
    82	
    83	### 합의 보고서 / 헌법
    84	
    85	- `docs/review/3plus1-consensus-2026-05-04-hermes.md` (3+1 합의 보고서 전문)
    86	- `docs/constitution/PROJECT_CONSTITUTION.md` 제8조 (보안), 제5조 관용 (Provider Liquidity, 비협상)
    87	- `~/.claude/projects/-home-delangi----project-category-AI-development-tool/memory/feedback_provider_liquidity.md` (Provider Liquidity 영구 기억)
    88	
    89	> **[Cross-reference Block — (g1-N-3-adr-008+sip+adr-012') R-7 (f) cross-ref block 만 채택 + R-S3 답습]**: 본 line 86 표기 "제5조 관용 (Provider Liquidity, 비협상)" = (g1-N-1) commit `148fbbe` 후 **헌법 제5조-2: Provider Liquidity 원칙 (비협상) (line 75~80)** 직접 모법 발효 — (g1-N-1) 이전 관용 표현 답습. 본 cycle = gov §1.1 line 78 verbatim 명문 4 source ("ADR-008 / ADR-011 / system-identity-prequel / 본 v3") 中 ADR-008 정정 자격 직접 발효 (R-S3 CRITICAL). ADR-008 = ADR-011 직접 모법 (ADR ↔ ADR 부록 B Amendment 패턴). (g1-N-3-pamsd) `ab96e30` 동형 패턴 답습, **본문 verbatim 변경 0건** ((f) cross-ref block 만 채택). 정정 후 형식 = ADR-011 line 245 모법 "제5조-2 관용 (Provider Liquidity, 비협상)" (R-rec-3 답습 + 사용자 명시 직접 확인). 추가 위치 line 87/98/107/274/329/366/370 (P2 cross-ref + P3 본문) = (P3) 본문 답습 본질 동형, 정정 자격 약함 ((P3) 약식 통일 cycle DEFER carry-over). 본 cycle 합의 = `209f04d`.
    90	
    91	### Hermes 도입 설계 (P2)
    92	
    93	- `docs/architecture/hermes-adoption-design.md` (P2 v2, **Archived 2026-05-09 후속 7** — 옵션 A 최소 침습 — 헤더 갱신 + 본문 보존, path 변경 0건. archive 합의: `docs/review/3plus1-consensus-2026-05-09-p2-v2-archive-decision.md`)
    94	- **`docs/architecture/hermes-adoption-design-v3.md`** (P2 v3, **Adopted — Design Adoption only, 2026-05-09 후속 6, 후속 권위**) — P2 v2 §2.1.3 가정 (외부 pre-record hook) 폐기 + R-2~R-7 evidence 흡수 + G1b PASS 권위 + Hermes PMO 구조 사전 정의 (활성화 *아님*) + G2/G3/G4 entry/exit. **본 ADR-008 의 Option B 단계 마이그레이션은 P2 v3 §2.6 + §11.1 + §2.6.1 12 조건 PMO 격상 체크리스트로 운영 절차화** (인간 전문 리뷰 의무 명문화, P2 v3 §2.6 단계 5.5)
    95	- `docs/architecture/system-identity-prequel.md` (**Archived 2026-05-09 후속 8** — AI Dev Company OS 정체성 직접 권위 출처 영구 보존. archive 합의: `docs/review/3plus1-consensus-2026-05-09-system-identity-prequel-archive-decision.md`)
    96	
    97	### Provider 추상화 / Adapter (차단조건 #4)
    98	
    99	- `docs/architecture/llm-providers-design.md` (P1 v2, LiteLLM facade — Option β 채택)
   100	- **`docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md`** (C-N 갱신 2026-05-09 후속 4 — P1 facade MVP 진입조건 명시 + **Hermes PMO ↔ provider 분리 영구 권위 (§2.3)** + **Provider Liquidity 5-way Multi-layer Defense 모법 ADR Layer 1 (§5)** + v2.0 트리거 vs MVP 조건 분리 + P2 v3 cross-reference). 본 ADR-008 차단조건 #4 (provider 어댑터 추상화) 의 *Hermes PMO ↔ provider 분리* 권위 출처
   101	
   102	### 차단조건 #1 충족 (수단/목적 분리)
   103	
   104	- **`docs/decisions/ADR-011-means-vs-ends-redaction.md`** (수단/목적 분리 원칙 — 본 ADR-008 부록 B Amendment R1 specific 갱신의 권위 근거. §2.1 (a)~(d) 4조건 + §2.2 G1a/G1b 분리 + §2.3 Hermes ≠ root of trust 영구 권위 + §2.4 T1/T2/T3 영구 권위)
   105	- `docs/decisions/ADR-010-sqlcipher-vault-key-management.md` (SQLCipher Vault HSM 키 관리 — 차단조건 #1 키 관리 측면)
   106	
   107	### Evidence 무결성 (2026-05-09 후속 3 PR-2 신규 발행)
   108	
   109	- **`docs/decisions/ADR-012-evidence-ledger-protection.md`** (Evidence Ledger Protection — 본 ADR-008 차단조건 #2 (JSONL export 표준) 의 *Evidence Ledger 무결성* 강화 권위. 12 보호 원칙 + Layer 1~5 다층 강제 + RFC 8785 JCS + Hermes 변조 차단 매트릭스 4항목 + Provider Liquidity 5-way Layer 5)
   110	- 신규 위반 경로 P10 (Evidence Forgery) 정식 등록 (G2 §1.2.6, 2026-05-09 후속 5)
   111	
   112	### 4 게이트 정식 산출 (2026-05-09 Design/Governance Gate PASS Bundled)
   113	
   114	- `docs/architecture/governance-preconditions.md` (G2, **Design/Governance Gate PASS Bundled, 2026-05-09**) — 6 거버넌스 사전조건 GP-1~GP-6 + §1.2.6 P10 Evidence Forgery 정식 등록. **GP-1 = G1b PASS evidence 흡수 (Implementation/Runtime PASS), GP-2~GP-6 = Design PASS / Implementation Pending**
   115	- `docs/architecture/hermes-not-root-of-trust-runtime.md` (G3, **Design/Governance Gate PASS Bundled**) — 권위 위계 운영 + Hermes 권한 22 항목 (T1 8 / T2 2 / T3 12) + Hermes 변조 차단 매트릭스 4항목. **운영 구현 = Design PASS / Implementation Pending**
   116	- `docs/architecture/provider-agnostic-memory-skill-design.md` (G4, **Design/Governance Gate PASS Bundled** + §4.2 11 필드 schema + §4.4 hash chain 사양 + §4.6 round-trip 검증 절차 보강 PR-2). **라운드트립 + migration script = Design PASS / Implementation Pending**
   117	- `docs/phase0/redaction-verification-sop.md` (R-7 SOP — G1b PASS 정식 충족 절차)
   118	
   119	### 부록 B §B.6 정식 충족 절차 cross-reference (G1b PASS + G2 GP-1 흡수)
   120	
   121	- 부록 B §B.6 R-3 ~ R-7 6단계 ✅ 완료 (2026-05-06 ~ 2026-05-07 Part 1) + R-6 GitHub Actions actual run `25482284523` PASS (24초, 42/42, leak 0) + R-7 SOP §7.3 단축 합의 APPROVE Reviewer-only (2026-05-07) → G1b CONDITIONALLY PASS → **PASS** 승격 + Phase 1 acceptance PARTIAL → **PASS** 선언. **G2 GP-1 = G1b PASS evidence 흡수** (Tier-1 한정, 2026-05-09 G2 정식 PASS 시점)
   122	
   123	---
   124	
   125	## 부록 A — 검증 결과 (2026-05-04)
   126	
   127	Phase 1 진입 전 사실 확인 작업 2건 완료. 결과 CRITICAL 위험 2건이 다운그레이드되었으나, 차단조건 6개는 그대로 유지(방어 자세).
   128	
   129	### A.1 ChatGPT Pro Codex CLI ToS 검증
   130	- **공식 지원**: Hermes는 OpenAI Codex `device code` OAuth flow를 정식 지원. credentials는 `~/.hermes/auth.json`에 저장, `~/.codex/auth.json`에서 import 가능
   131	- **개인 단일 사용자 시나리오**: ToS 위반 위험 **LOW** — Codex CLI 자체와 동등 사용
   132	- **금지 사례**: "Reselling access" 또는 "third-party services에 ChatGPT 전력 공급". 본 프로젝트는 개인 사용이므로 해당 없음
   133	- **정책 변동성**: OpenAI/Anthropic가 third-party 도구의 구독 집계를 최근 제한한 사례 존재 → API 키 경로 우선 정책은 그대로 유지
   134	- **A-meta 위험 등급**: CRITICAL → **MEDIUM** (정책 변동 모니터링 필요)
   135	
   136	### A.2 Hermes JSONL Export 검증
   137	- **공식 명령어**: `hermes sessions export backup.jsonl` 존재. 전체/플랫폼별/단일 세션 export 지원, full message history 포함
   138	- **데이터 저장소 정정**: ChromaDB는 사용하지 않음. **SQLite + FTS5 단일** — 암호화는 SQLCipher 단일 적용으로 충분 (차단조건 #1 단순화)
   139	- **마이그레이션 도구**: `hermes claw migrate` (OpenClaw → Hermes) 존재. 역방향 export는 sessions 단위로 가능
   140	- **스키마 버전 관리**: `schema_version` 테이블 존재
   141	- **R2 위험 등급**: CRITICAL → **HIGH** (skills/memory 범위는 P1 설계 단계에서 추가 검증)
   142	- **추가 검증 항목**: `hermes sessions export`가 sessions만 다루는지, agent-curated memory와 skills도 포함하는지 P1에서 확인 필요
   143	
   144	### A.3 차단조건 영향
   145	6개 차단조건은 **그대로 유지**. 검증 결과는 충족 가능성을 높였을 뿐 의무를 약화하지 않음.
   146	- #1 SQLCipher: 적용 대상이 SQLite 단일 → 구현 단순화
   147	- #2 JSONL export: 공식 명령어 활용. skills/memory 범위 보강 필요
   148	- #3 버전 핀: 그대로
   149	- #4 어댑터 추상화: 그대로 (P1 설계의 핵심)
   150	- #5 2 provider always-on: 그대로
   151	- #6 Docker 격리: 그대로
   152	
   153	---
   154	
   155	## 부록 B — Amendment (2026-05-06): R1 해석 갱신 (수단/목적 분리)
   156	
   157	**상태**: 갱신 (단축 합의 — Reviewer-only)
   158	**날짜**: 2026-05-06
   159	**근거 ADR**: `docs/decisions/ADR-011-means-vs-ends-redaction.md`
   160	**근거 Phase 0 evidence**: R-1 FAIL (`docs/phase0/day2-r1-redaction-location-verification.md`), R-2 PASS (`docs/phase0/day3-r2-sqlite-trigger-poc.md`)
   161	**근거 합의**: `docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md`
   162	
   163	### B.1 R1 비협상 핵심 재정의
   164	
   165	R1의 비협상 핵심은 **특정 외부 hook 구현이 아니라, AI 학습 루프/메모리 DB에 비밀값이 평문으로 영구 저장되지 않도록 차단하는 결과**이다.
   166	
   167	본 Amendment 이전 부록 A R1 텍스트는 "외부 pre-record hook"을 수단으로 가정한 표현을 포함했다. 본 Amendment는 그 가정을 ADR-011 §2.1 수단/목적 분리 원칙에 따라 갱신한다.
   168	
   169	### B.2 G1a / G1b 분리 관리
   170	
   171	Hermes native redaction이 DB INSERT 경로에 적용된다는 기존 가정은 **R-1에서 FAIL로 판정**되었다.
   172	
   173	그러나 R-2 PoC에서 SQLCipher BEFORE INSERT trigger 기반 DB-level fallback이 plaintext secret persistence를 차단할 수 있음이 실증되었으므로, G1은 다음과 같이 분리 관리한다:
   174	
   175	- **G1a**: Hermes native redaction applies before DB INSERT — **FAIL** (폐기)
   176	- **G1b**: DB-level fallback prevents plaintext secret persistence — **PASS by R-2 PoC** (정식 충족은 R-3~R-7 후)
   177	
   178	정식 충족 조건은 ADR-011 §2.2 G1b 정식 충족 조건 표를 따른다.
   179	
   180	### B.3 권위화 출처
   181	
   182	이 해석은 **ADR-011 Means-vs-Ends Redaction Principle**에 의해 권위화된다. 본 Amendment는 ADR-011 §2.1~§2.3을 ADR-008 R1 specific 갱신으로 적용한 것이며, 일반 원칙 본문 해석은 ADR-011을 우선 참조한다.
   183	
   184	### B.4 본 Amendment의 의미 (오해 방지)
   185	
   186	본 Amendment는 "Hermes가 안전하다"는 선언이 **아니다**. 정확한 의미는 다음과 같다:
   187	
   188	1. Hermes native redaction은 DB INSERT 보호 수단으로 **신뢰하지 않는다**.
   189	2. DB INSERT 경로는 SQLCipher trigger 기반 fallback으로 **별도 보호한다**.
   190	3. **Hermes는 root of trust가 아니다** (ADR-011 §2.3 권위 위계 명문화).
   191	
   192	### B.5 6 차단조건 영향
   193	
   194	ADR-008 결정 본문 §6 차단조건 #1 (SQLCipher + redaction 필터) 의 충족 메커니즘은 다음으로 갱신된다:
   195	
   196	| 메커니즘 | 위치 | 신뢰도 |
   197	|---------|------|------|
   198	| SQLCipher 암호화 (디스크) | DB 파일 | 기존대로 |
   199	| Hermes native redaction | 로그 / LLM 송신 / 도구 출력 | 보조 (DB 차단 책임 없음) |
   200	| **SQLCipher BEFORE INSERT trigger + REGEXP UDF** | **DB INSERT 경로** | **Primary (G1b)** |
   201	
   202	차단조건 #2~#6은 변경 없음. 6 차단조건 자체의 비협상성은 유지된다 — 본 Amendment는 #1 충족 *수단*을 ADR-011 (a)~(d) 4조건 하에 재정의한 것이다.
   203	
   204	### B.6 정식 충족 절차
   205	
   206	차단조건 #1 정식 exit 기준은 다음 6단계 완료를 요한다 (R-4.1 은 R-4 추가 격리 PoC 분기로 ADR-011 §2.1 (b) 직접 충족 산출):
   207	
   208	```
   209	R-3   ✅ 본 Amendment 발행 (2026-05-06)
   210	R-4   ✅ 패턴 동등성 비교 + gap 식별 + 보충 권고 — `docs/architecture/redaction-pattern-equivalence.md` (2026-05-06)
   211	R-4.1 ✅ Tier-1 42종 trigger UDF 확장 + 격리 환경 PoC PASS — `docs/phase0/r4-1-trigger-extension-evidence.md` (2026-05-06)
   212	R-5   ✅ canary 재검증 트리거 설계 — `docs/architecture/canary-recheck-design.md` (2026-05-06)
   213	R-6   ✅ CI/nightly canary regression workflow 구현 — `.github/workflows/r2-canary.yml` (2026-05-06, commit `bbcc1af`; **GitHub Actions actual run 은 push 후 별도 검증 의무**)
   214	R-7   ✅ Phase 1 합격 SOP — `docs/phase0/redaction-verification-sop.md` (2026-05-06)
   215	```
   216	
   217	**6단계 작성 완료 + R-6 actual run PASS + 단축 합의 APPROVE → G1b 정식 PASS 도달** (2026-05-07):
   218	
   219	- ✅ R-6 GitHub Actions 실제 run PASS — run ID `25482284523` (commit `939125b` 기준 24초 완료, 모든 step ✓)
   220	  - 1차 run (`25480443667`) FAIL 은 docker compose stdout prefix JSON parse infra bug — 보안 위반 / catalog drift / 실 secret 노출 / CI 자동 정책 변경 모두 *아님* (사용자 단축 합의 결정 답습). Fix `939125b` 는 workflow YAML 1 file 한정 (`r4_1_poc.py` / Tier-1 catalog / trigger UDF / redaction config 변경 0건)
   221	- ✅ Artifact `r2-r4-canary-evidence` 본문 검증 통과 — verdict = "PASS", tier1_pass_rate = "42/42", Tier-1 42/42 BLOCK, Safe 9/9 PASS, leak_observations = [], rollback_triggered = false
   222	- ✅ R-7 SOP §7.3 단축 합의 (Reviewer-only, ADR-011 §2.4 T2) APPROVE — `docs/review/3plus1-consensus-2026-05-07-g1b-phase1-acceptance.md` (13 Reviewer 항목 + 8 PASS 조건 + 5 통제 수단 명시)
   223	- ✅ G1b status: CONDITIONALLY PASS → **PASS** 승격
   224	- ✅ Phase 1 acceptance: PARTIAL → **PASS** 선언
   225	
   226	본 ADR-008 부록 B.6 갱신은 ADR-011 §2.4 T2 절차 (사용자 승인 + Reviewer-only 단축 합의) 답습. **자동 승격 아님**.
   227	
   228	R-4 / R-4.1 / R-5 / R-6 / R-7 진행 상태는 본 Amendment 가 아니라 ADR-011 §2.2 표 또는 `docs/CONTEXT.md` 의 4 게이트 진행 상태에서 추적한다.
   229	
   230	본 G1b PASS 는 *4 게이트 중 G1b 한정* — Hermes PMO 격상은 G2 / G3 / G4 추가 통과 후 별도 결정 (본 Amendment 범위 외).
   231	
   232	---
   233	
   234	## 부록 C — Hermes PMO Activation Cross-Reference (2026-05-09 후속 13 신설)
   235	
   236	**상태**: 신설 (단축 합의 — Reviewer-only)
   237	**날짜**: 2026-05-09 후속 13
   238	**근거 합의**: `docs/review/3plus1-consensus-2026-05-09-adr-008-update-pmo-activation-cross-ref.md` (Reviewer-only 단축 합의 APPROVE — 7 항목 분류 + 6/6 풀 3+1 승격 트리거 0건 발화)
   239	**근거 권위**:
   240	- P2 v3 §2.6 (격상 절차 7 단계) + §2.6.1 (12 조건 PMO 격상 체크리스트) + §11.1 (Hermes PMO 격상 전 인간 전문 리뷰 의무화)
   241	- ADR-009 C-N §2.3 (Hermes PMO ↔ provider 분리 영구 권위, 2026-05-09 후속 4)
   242	- ADR-011 §2.3 (Hermes ≠ root of trust) + §2.4 (T1/T2/T3 자동 학습 vs 정책 변경 분리)
   243	- ADR-012 §2.12 (Hermes 변조 차단 매트릭스 4항목, 2026-05-09 후속 3 PR-2)
   244	- G2 §1.2.6 (P10 Evidence Forgery 정식 등록, 2026-05-09 후속 5)
   245	- G3 §1.3 + §5 (Evidence decision principle: PASS 성립 4 요건)
   246	- G4 §4 (Memory/Skill JSONL hash chain + Tier-based round-trip)
   247	- 본 ADR-008 §결정 단계 마이그레이션 + 부록 B Amendment
   248	
   249	**ADR-013 대체 권위**: 본 부록 C = ADR-013 (Hermes PMO Activation 영구 권위) 신규 발행 *대체* (`docs/review/3plus1-consensus-2026-05-09-adr-013-014-candidate-decision.md` §1.1.3 답습 — ADR-013 현 시점 발행 보류).
   250	
   251	### C.1 본 부록 C 의 의미 (오해 방지)
   252	
   253	> **본 부록 C 는 Hermes PMO 격상 *선언이 아니다*.**
   254	>
   255	> 본 부록 C 는 P2 v3 §2.6 + §11.1 + §2.6.1 + ADR-008 부록 B + ADR-011 §2.3/§2.4 + ADR-009 C-N §2.3 + ADR-012 §2.12 의 *Hermes PMO 격상 조건 cross-reference 강화* 한정. 8 권위 layer 중첩 답습으로 *영구 권위 정착 가능* 하나, *현 시점 격상 발생 0건*.
   256	
   257	본 부록 C 의 정확한 의미는 다음과 같다:
   258	
   259	1. P2 v3 정식 채택 (2026-05-09 후속 6) = **Design Adoption only** — Hermes PMO Activation 미발생 (P2 v3 §2 Non-Activation Clause 답습)
   260	2. 본 부록 C 는 *Hermes PMO 격상 조건* 명시 강화 + ADR-009 C-N + ADR-011 + ADR-012 + G2/G3/G4 + P2 v3 *cross-reference* 매트릭스 제공

exec
/bin/bash -lc "nl -ba docs/architecture/governance-preconditions.md | sed -n '1,220p'; nl -ba docs/architecture/governance-preconditions.md | sed -n '520,700p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# 6 Governance Preconditions (G2) — Design/Governance Gate PASS (Bundled, 2026-05-09)
     2	
     3	> **상태: Design/Governance Gate PASS (Bundled, 2026-05-09)**. Hermes PMO 격상 4 게이트 중 G2 — "헌법 8조·5조-2(Provider Liquidity, 비협상) 위반 경로 P1~P8 강제 메커니즘 매핑 + 6 거버넌스 사전조건 GP-1~GP-6 정의 + 각 사전조건의 entry/exit 기준" 정의. **G2 + G3 + G4 통합 풀 3+1 합의 + 외부 LLM 2건 (GPT cross-vendor + Claude 인접 컨텍스트) APPROVE WITH CONDITIONS** (`docs/review/3plus1-consensus-2026-05-09-g2g3g4-formal-promotion.md`).
     4	>
     5	> **PASS 범위 한정 (P0 조건 C-A, 5/5 입력 일치)**: 본 PASS 는 *Design/Governance Gate PASS* 한정 — 문서 구조 / 권위 위계 / 6 GP 정의 / 강제 메커니즘 분류 매트릭스 / Entry·Exit 기준 정의의 *설계 승인* 에 한정한다. **Implementation/Runtime PASS 는 본 PASS 에 포함되지 않는다** — GP-2~GP-6 의 PoC 실증 / CI 강제 / runtime hook 구현 / Evidence Ledger 검증은 *별도 합의* 로만 발생.
     6	>
     7	> **GP 별 상태 (P0 조건 C-B, 5/5 입력 일치)**:
     8	> - **GP-1**: PASS (G1b PASS evidence 흡수, 단 Tier-1 한정 — Tier-2/Tier-3 catalog 확장은 후속, Claude C-7)
     9	> - **GP-2 ~ GP-6**: **DESIGN PASS / IMPLEMENTATION PENDING** (각 GP 의 PoC 실증 + (a)~(e) 5조건 충족 검증은 별도 합의)
    10	>
    11	> **§1.2.6 P10 Evidence Forgery 정식 등록 (2026-05-09 후속 5 단축 합의 APPROVE Reviewer-only)**: ADR-012 §1.4 cross-reference + Hermes 변조 차단 매트릭스 4항목 + Layer 1~5 enforcement.
    12	>
    13	> **§1.2.7 P11 Supply-chain Compromise 정식 등록 (2026-05-12 단축 합의 적격 — Reviewer-only)**: Gate Enforcement Layer 보호 보강 (G3 §2.6, 2026-05-12 commits `3e46440` + `fa2cbdb`) 시점 트리거 답습. 5 측면 (Dependency Pinning Integrity / Checksum / Action SHA Pin / Docker Digest Pin / Vendor Change Auto-recheck) + 5 Layer 다층 강제 + Enforcement Tool Self-protection + 5 기준 (감지/차단/Evidence/Rollback/사용자 승인). **Hermes PMO 격상 *전* precondition 권장 (blocking 아님)** — Implementation/Runtime PASS 영역의 우선 권장 항목 (Claude C-3 + C-6 답습). 외부 LLM Gap-N 중 N-5 (supply chain / dependency integrity) 답습. **본 §1.2.7 = P11 row 추가 한정 — runtime code 구현 / CI workflow 수정 / hook 구현 / 신규 GP 신설 / 신규 ADR 발행 / Hermes PMO 격상 / Operational Readiness PASS / Implementation/Runtime PASS / G2/G3/G4 PASS 재선언 / ADR 본문 자동 갱신 모두 본 작업 범위 외** (사용자 명시 답습).
    14	>
    15	> **P2 v3 (`hermes-adoption-design-v3.md`) = Adopted (Design Adoption only, 2026-05-09 후속 6)** 후속 권위. 본 G2 = P2 v3 §4 (G2 정의) + P2 v3 §3.1.4 Implementation Pending 표 + P2 v3 §10.1 Normative Constraints + §10.2 Archive Migration Note + §11.1 Hermes PMO 격상 전 인간 전문 리뷰 의무화 답습.
    16	>
    17	> **P2 v2 (`hermes-adoption-design.md`) = Archived (옵션 A 최소 침습, 2026-05-09 후속 7)** + **`system-identity-prequel.md` = Archived (옵션 A, 2026-05-09 후속 8)** — 본 G2 cross-reference 영향 0건 (path 변경 0건).
    18	>
    19	> **Hermes PMO 격상은 본 PASS 에 포함되지 않는다** (사용자 명시 답습) — 4 게이트 모두 Implementation/Runtime PASS + 외부 LLM 2개 또는 외부 LLM 1개 + 인간 전문 리뷰 (Human-in-the-loop) + 사용자 명시 결정 후 별도 (P2 v3 §2.6.1 12 조건 PMO 격상 체크리스트 답습). G2 운영 구현 PASS / ADR 본문 자동 갱신 / archive 자동 처리도 본 PASS 미포함.
    20	
    21	**작성일**: 2026-05-07
    22	**Status (2026-05-07 통합 합의)**: **Design/Governance Gate PASS (Bundled, 2026-05-07)** — `docs/review/3plus1-consensus-2026-05-07-g2-g3-g4-gate-adoption.md` (4/4 입력 만장일치 APPROVE WITH CONDITIONS — Agent A/B/C + 외부 LLM GPT-5.5 Thinking, 12 통합 조건 + Gap-N 6건 흡수 처리). 본 PASS 는 Design/Governance Gate 한정 — Implementation/Runtime PASS / Operational Readiness PASS / Hermes PMO 격상 / P2 v3 정식 채택 모두 미포함.
    23	**정식 PASS 일자**: 2026-05-09 (Design/Governance Gate PASS, Bundled with G3 + G4 — 2026-05-07 통합 합의의 후속 reaffirmation)
    24	**합의 권위**: `docs/review/3plus1-consensus-2026-05-09-g2g3g4-formal-promotion.md` (5/5 입력 APPROVE WITH CONDITIONS — Agent A/B/C 내부 + GPT cross-vendor + Claude 인접 컨텍스트)
    25	**P10 정식 등록 합의**: `docs/review/3plus1-consensus-2026-05-09-g2-p10-evidence-forgery.md` (2026-05-09 후속 5 단축 합의 APPROVE Reviewer-only)
    26	**상위 권위**: 헌법 제8조 (보안), 헌법 제5조-2 (Provider Liquidity, 비협상, `148fbbe` 신설) — 본 §1.1 명명 정정 *역할 종료* (cross-ref block 답습)
    27	**상위 결정**: ADR-008 (Hermes 도입 Option B) 6 차단조건, ADR-011 (수단/목적 분리, §2.3 권위 위계, §2.4 T1/T2/T3), **ADR-009 C-N (P1 facade MVP 진입조건 + Hermes PMO ↔ provider 분리 + Provider Liquidity 5-way 모법 ADR Layer 1, 2026-05-09 후속 4 갱신)**, **ADR-012 (Evidence Ledger Protection, 2026-05-09 후속 3 PR-2 신규 발행)**
    28	**관련 설계**: **`hermes-adoption-design-v3.md` §4 (G2 정의 — P2 v3 Adopted Design Adoption only, 2026-05-09 후속 6)**, `hermes-adoption-design.md` (P2 v2, **Archived 2026-05-09 후속 7**), `system-identity-prequel.md` §3.3 / §4.2 (**Archived 2026-05-09 후속 8**, 본 ADR-011 §2.3 영구 권위 승격 답습으로 권위 보존), `redaction-pattern-equivalence.md` (R-4), `canary-recheck-design.md` (R-5), `llm-providers-design.md` (P1 v2 — Option β LiteLLM facade)
    29	**근거 합의**: `docs/review/3plus1-consensus-2026-05-05-system-identity-redefinition.md` (Agent B 6 거버넌스 사전조건 + 8 위반 경로 P1~P8 식별), `docs/review/3plus1-consensus-2026-05-09-g2g3g4-formal-promotion.md` (G2 정식 PASS 합의), `docs/review/3plus1-consensus-2026-05-09-p2v3-formal-adoption.md` (P2 v3 정식 채택 풀 3+1 + 외부 LLM 2건 — 본 G2 = P2 v3 §4 답습 권위)
    30	**관련 evidence**: R-2 ~ R-7 + R-6 actual run `25482284523` (G1b PASS)
    31	
    32	---
    33	
    34	## 0. 본 초안의 범위
    35	
    36	### 0.1 본 초안이 *하는* 것
    37	
    38	1. "헌법 5조 (Provider Liquidity)" 명명 정정 (프로젝트 관용 답습 + 1회 명시)
    39	2. 헌법 8조 + Provider Liquidity 위반 경로 **P1~P8** 정의 (Agent B 합의 §29~§30 직접 기반)
    40	3. **GP-1 ~ GP-6** 6 거버넌스 사전조건 정의 + P1~P8 매핑
    41	4. 각 GP의 강제 메커니즘 분류 (계산적 / 추론적 / 자동 롤백) — 합의 §31 "Hermes 금지 8가지 × {계산적/추론적/자동 롤백}, 8 중 7 계산적 가능" 답습
    42	5. 각 GP의 Entry / Exit 기준 (ADR-011 §2.1 (a)~(d) 4조건 패턴 답습 + (e) 합의 APPROVE)
    43	6. 각 GP의 산출 후보 + 의존 ADR cross-reference 후보
    44	7. 메타 안전장치 — 본 6 사전조건 자체의 무결성 보호 (Hermes 자기참조 차단)
    45	8. G2 통합 entry/exit 기준 종합
    46	
    47	### 0.2 본 초안이 *하지 않는* 것 (사용자 명시 답습)
    48	
    49	1. ❌ **G2 PASS 선언** — 본 초안은 *정의*까지만, GP-1~GP-6 각각의 (a)~(e) Exit 기준 충족 검증은 후속
    50	2. ❌ **G3 / G4 PASS 선언**
    51	3. ❌ **Hermes PMO 격상 선언** — 4 게이트 모두 통과 + 사용자 명시 결정 후 별도
    52	4. ❌ **P2 v3 정식 채택 선언** — `hermes-adoption-design-v3.md` 헤더 DRAFT 그대로 유지
    53	5. ❌ **ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 자동 갱신** — 별도 PR 묶음
    54	6. ❌ **P2 v2 (`hermes-adoption-design.md`) archive 처리** — v3 정식 채택 시점에
    55	7. ❌ **`system-identity-prequel.md` archive 처리** — v3 정식 채택 시점에
    56	8. ❌ **자동 정책 변경 (ADR-011 §2.4 T3)** — 절대 금지
    57	9. ❌ **사전조건별 PoC 자동 실행** — 본 초안은 PoC 설계 *기준*까지, 실 PoC는 후속
    58	10. ❌ **Tier-2 / Tier-3 catalog 확장** — 별도 합의
    59	
    60	### 0.3 본 초안의 단계별 정식화 절차 (예정)
    61	
    62	| # | 단계 | 산출 | 시점 |
    63	|---|------|------|------|
    64	| 1 | 본 초안 작성 (현 단계) | 본 문서 (DRAFT) | 2026-05-07 |
    65	| 2 | 사용자 검토 + Reviewer-only 단축 검토 (DRAFT 적격) | 검토 보고서 | 사용자 명시 결정 후 |
    66	| 3 | 각 GP entry 진입 + PoC 작성 + Exit 기준 (a)~(e) 충족 검증 | 6 PoC 산출 + 각 GP별 evidence | GP별 순차 또는 병행 |
    67	| 4 | G2 PASS 합의 가동 (단축 또는 풀 3+1) | `docs/review/3plus1-consensus-YYYY-MM-DD-g2.md` | 단계 3 완료 후 |
    68	| 5 | G2 PASS 선언 + ADR cross-reference 갱신 (G3/G4와 묶음 가능) | 별도 PR | 단계 4 후 |
    69	
    70	본 초안 자체는 단계 1까지만 처리. 단계 2~5는 본 초안 범위 외.
    71	
    72	---
    73	
    74	## 1. 명명 정정 + 위반 경로 P1~P8 정의
    75	
    76	### 1.1 "헌법 5조 (Provider Liquidity)" 명명 정정 (선행, 1회 명시)
    77	
    78	**관용 표현**: ADR-008 / ADR-011 / system-identity-prequel / 본 v3 모두 "헌법 제5조-2 (Provider Liquidity, 비협상)" 표현 사용 ((g1-N-1) commit `148fbbe` 후 헌법 본문 직접 등재 완료).
    79	
    80	**실제 헌법 본문**:
    81	- `docs/constitution/PROJECT_CONSTITUTION.md` 제5조 본문: **"코드 품질 원칙"** (5개 항목, 단일 책임 / 가독성 / 중복 제거 / 외부 입력 검증 / 린터)
    82	- 제8조 본문: 보안 원칙 (4개 항목) — 관용과 일치
    83	
    84	**Provider Liquidity 실제 권위 출처**:
    85	- `~/.claude/projects/.../memory/feedback_provider_liquidity.md` (사용자 비협상 메모리)
    86	- ADR-008 본문 + 부록 A.1 (구독 교체 자유 + Hermes lock-in 차단)
    87	- 본 프로젝트 모든 헌법-동급 제약으로 보호됨 (관용 "헌법 5조"로 인용)
    88	
    89	**본 초안의 처리**:
    90	- 본 초안은 **프로젝트 관용 답습** — 본문 내 "헌법 5조 (Provider Liquidity)" 표현 그대로 사용
    91	- 단, 본 §1.1 1회 명시로 명명 불일치 인지 + 향후 *헌법 본문 갱신* 또는 *ADR-012 (가칭) Provider Liquidity 정관 흡수* 등 정정 후보 제시 (본 초안 범위 외)
    92	- 후속 작업: 헌법 본문 갱신 또는 ADR Amendment 결정은 풀 3+1 합의 영역 (T3 변경 — ADR-011 §2.4)
    93	
    94	**[Cross-reference Block — (g1-N-3-gov) (ii-c) verbatim 부분 정정 + R-4 답습]**: 본 §1.1 = (g1-N-1) commit `148fbbe` 후 **역할 종료**. 헌법 본문 line 75~80 "제5조-2: Provider Liquidity 원칙 (비협상)" 신설 완료 — 본 §1.1 line 91 "정정 후보 제시 (본 초안 범위 외)" 부분 obsolete. 단 본 §1.1 의 *역사적 의의* (관용 명명 불일치 *최초 명문 식별* + (g1-N) cycle chain 의 *직접 동기 출처*) 영구 보존. 후속 인용 chain (line 26 + line 38 + line 835) 모두 본 §1.1 cross-ref 답습 자격. (ii-a) 전체 삭제 / (ii-b) 본문 수정 / (ii-d) archive 표시 = 사전 기각 (합의 기각-3, A-B2 cascading failure risk + (10-f) sub-boundary).
    95	
    96	### 1.2 위반 경로 P1~P8 정의
    97	
    98	> **본 §1.2는 합의 §29~§30 (Agent B "헌법 8조·5조 위반 경로 8건 P1~P8" + B-P5/P7 cross-reference) 의 본 초안 명시 enumeration 이다.** 합의 보고서에는 P1~P8 enumeration 이 명시되지 않아 본 §1.2 가 *최초 명시* — 후속 합의 시 GP 매핑 적정성 검증 대상.
    99	
   100	#### 1.2.1 헌법 제8조 (보안) 위반 경로 5건 (P1~P5)
   101	
   102	| # | 경로 | 시나리오 | 헌법 8조 어느 항 | G1b 와 관계 |
   103	|---|------|---------|--------------|----------|
   104	| **P1** | **DB INSERT 평문 secret 누적** | Worker Agent 가 LLM 응답·환경변수 echo·tool output 을 SessionDB / Memory DB / Skill DB 에 INSERT 시 평문 secret 영구 저장 | 8조 #1 (하드코딩 차단) + 8조 #2 (비밀 관리) | **G1b PASS 로 차단** (SQLCipher trigger + Tier-1 42 catalog) |
   105	| **P2** | **로그/LLM 송신 경로 평문 노출** | Hermes / Worker 가 secret 을 stdout / stderr / log file / LLM API request body 에 노출 | 8조 #2 | Hermes native redaction 보조 (ADR-011 §2.3 운영 함의 #2) |
   106	| **P3** | **Credential / OAuth 파일 권한 노출** | API 키 파일 / OAuth credentials 파일이 world-readable / docker socket mount / inotify 미감시 | 8조 #2 | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 + entrypoint stat 검증 (35번째 entry R-S1 정정 답습) |
   107	| **P4** | **비밀값 하드코딩** | secret 이 git commit 본문 / 환경변수 default / docker-compose.yml 평문 / Skill 정의 평문 등에 영구 기록 | 8조 #1 (직접) | gitleaks / detect-secrets / pre-commit hook |
   108	| **P5** | **외부 입력 미검증/이스케이프** | Worker Agent 또는 Hermes 출력이 *내부* 처럼 취급되어 SQL injection / command injection / path traversal 등 발생 | 8조 #3 (직접) | **헌법 8조 #4 — 보안 변경은 3+1 합의** + 헌법 5조 #4 (외부 입력 검증) |
   109	
   110	#### 1.2.2 Provider Liquidity (관용 헌법 5조) 위반 경로 3건 (P6~P8)
   111	
   112	| # | 경로 | 시나리오 | Provider Liquidity 어느 측면 | 관련 ADR-008 차단조건 |
   113	|---|------|---------|--------------------------|------------------|
   114	| **P6** | **Hermes 자체 SDK 직접 import** | Worker Agent / Skill / Hermes plugin 코드가 `import hermes_agent.*` 또는 `import litellm` 직접 import 로 P1 facade 우회 | Provider 교체 자유 (코드 변경 없이) | **차단조건 #4** (provider 어댑터 추상화) |
   115	| **P7** | **모델명/Provider 분기 코드** | `if model == "claude-opus-4-7": ... elif model == "gpt-5.5": ...` 또는 provider 별 후처리 분기 / Skill 내 모델 가정 (ADR-008 §결과 §주의사항 6종) | Provider 교체 자유 (코드 변경 없이) | **차단조건 #4** (P1 v2 depcruise 룰) |
   116	| **P8** | **Memory / Skill Hermes 종속 형식** | Skill 정의 / Memory entry 가 Hermes 자체 schema (binary protocol / proprietary key) 사용으로 다른 오케스트레이터 import 불가 | Provider 교체 자유 (학습 자산 유지) | **차단조건 #2** (JSONL export) + **G4** (Provider-agnostic Memory/Skill 형식) |
   117	
   118	#### 1.2.3 정식 위반 경로 합산 (P1~P8 + P10 + P11, 2026-05-12 갱신)
   119	
   120	```
   121	헌법 8조 (보안) 위반 경로 = 5건 (P1~P5)
   122	Provider Liquidity 위반 경로 = 3건 (P6~P8)
   123	Evidence Integrity 위반 경로 = 1건 (P10)            ← 2026-05-09 후속 5 정식 등록
   124	Supply-chain Integrity 위반 경로 = 1건 (P11)        ← 2026-05-12 정식 등록
   125	─────────────────────────────────────────────────
   126	정식 위반 경로 합계 = 10건 (P1~P8 + P10 + P11)     ← ✅ 합의 §29~§30 일치 + ADR-012 발행 시점 P10 흡수 + Gate Enforcement Layer 보호 보강 시점 P11 흡수
   127	Deferred candidates = 2건 (P9 / P12, §1.2.5)
   128	```
   129	
   130	P10 정식 등록 = ADR-012 (Evidence Ledger Protection) 발행 시점 (2026-05-09 후속 3 PR-2) 트리거 답습 — §1.2.5.2 명시 "P10 정식 등록 시점 = PR-2 신규 ADR-012 발행 시점" 답습. 본 §1.2.6 답습.
   131	
   132	P11 정식 등록 = Gate Enforcement Layer 보호 보강 (2026-05-12, commits `3e46440` + `fa2cbdb`) 시점 트리거 — §1.2.5 명시 "P11 정식 등록 시점 = SBOM + supply-chain 검증 PoC 합의 시점, Hermes PMO 격상 *전* 권장" + 본 보강 작업의 Layer 2 (CI / hook / test) enforcement mechanism 이 supply-chain compromise 로 무력화 가능 + 외부 LLM Gap-N 중 N-5 supply chain / dependency integrity 답습. 본 §1.2.7 답습.
   133	
   134	#### 1.2.4 본 §1.2 가 *다루지 않는* 위반 경로
   135	
   136	본 §1.2는 *헌법 8조 + Provider Liquidity* 위반 경로에 한정. 다음은 본 G2 범위 외:
   137	- 헌법 1조 (SDD) / 2조 (TDD) 위반 — 일반 Harness Layer 1~4 hook 가 다룸
   138	- 헌법 4조 (3+1 합의) 위반 — Layer 5 + 사용자 결정
   139	- 헌법 7조 (투명성) 위반 — Layer 0 (CLAUDE.md) + ADR 절차
   140	- 헌법 10조 (문서 일관성) 위반 — `docs/INDEX.md` + 의존 관계 매트릭스
   141	- ADR-011 §2.4 T3 (자동 정책 변경) 위반 자체 — **G3** ("Hermes ≠ root of trust" 운영 구현) 범위. 본 G2 §9 메타 안전장치에서 *interface*만 명시
   142	
   143	#### 1.2.5 P9 ~ P12 deferred candidates (C-I 흡수 — 2026-05-09 후속 2)
   144	
   145	> **본 §1.2.5 는 합의 보고서 §11.2 P1 조건 C-I 흡수** (출처: GPT 조건 7 + Claude C-4). 본 §1.2.1 ~ §1.2.3 의 *현재 enumeration P1~P8* 외에 **누락 위반 경로 후보 4 ~ 6 건** 을 *deferred candidates* 로 명시 등록한다. **deferred candidate = 향후 합의에서 P9~P12 정식 등록 가능, 본 G2 PASS 시점 정식 enumeration 외**.
   146	
   147	| 후보 ID | 위반 경로 (요약) | 핵심 위험 | 현 등록 상태 | 정식 등록 시점 |
   148	|--------|-------------|--------|----------|----------|
   149	| **P9 (후보)** | **Prompt Injection** — Hermes / Worker / LLM 출력 내 *지시 명령* 이 후속 LLM / Tool 에 의해 *명령* 으로 해석 (예: "ignore previous instructions ...") | 합의 결과 silent override / 자동 정책 변경 위장 / Skill escalation | deferred (GPT 조건 7) | 외부 입력 검증 GP-4 PoC 진입 시점에 P5 (외부 입력 검증) 와 *별 카테고리* 로 정식 등록 검토 |
   150	| ~~**P10 (후보)**~~ → **P10 (정식 등록 완료, §1.2.6 답습, 2026-05-09 후속 5)** | **Evidence Forgery** — JSONL ledger / 합의 보고서 / GitHub Actions run artifact 위조 또는 변조 | PASS 위장 / Hermes-originated 변경 위장 / 합의 권위 침해 | ✅ **정식 등록 완료 (§1.2.6 답습)** | ✅ **2026-05-09 후속 5** — PR-2 ADR-012 발행 (2026-05-09 후속 3) 시점 트리거 답습 → 본 단축 합의 (Reviewer-only) 로 정식 등록 |
   151	| ~~**P11 (후보)**~~ → **P11 (정식 등록 완료, §1.2.7 답습, 2026-05-12)** | **Supply-chain Compromise** — Hermes / pysqlcipher3 / litellm / Hermes-agent 의존성 또는 GitHub Actions runner / Docker base image 침해 | 자동 redaction 무력화 / SQLCipher trigger silent 깨짐 / canary catalog silent 변경 / R-6 actual run 위장 / Gate Enforcement Layer Layer 1~4 (lint/test/hook/CI) 무력화 | ✅ **정식 등록 완료 (§1.2.7 답습)** | ✅ **2026-05-12** — Gate Enforcement Layer 보호 보강 (commits `3e46440` + `fa2cbdb`) 시점 트리거 답습 → 본 단축 합의 (Reviewer-only) 로 정식 등록. **Hermes PMO 격상 *전* precondition (권장)** — blocking 까지는 아님, Implementation/Runtime PASS 영역의 *우선 권장 항목* (Claude C-3 + C-6 답습) |
   152	| **P12 (후보)** | **Memory Poisoning Side-channel** — Memory / Skill 의 *우회 경로* (CLAUDE.md prompt-level lock-in / 외부 import skill / Memory 자동 흡수) 를 통한 Memory 오염 + 후속 결정 silent 영향 | 자동 학습 → 자동 정책 변경 위장 (T1 → T3 우회) / Skill 권한 escalation 우회 / Provider lock-in 우회 | deferred (Claude C-4 + GPT 조건 7) | G4 (provider-agnostic-memory-skill-design.md) Implementation/Runtime PASS 합의 시점에 정식 등록 — Memory boundary hook + Skill wrapper 실 구현 후 |
   153	
   154	##### 1.2.5.1 추가 후보 (lower priority, 2 건)
   155	
   156	| 후보 ID | 위반 경로 (요약) | 처리 |
   157	|--------|-------------|----|
   158	| **P13 (후보)** | **Provider-specific URL Hardcoding** — `https://api.anthropic.com/...` / `https://api.openai.com/...` 등 provider 도메인 하드코딩 (P1 facade 우회) | GP-5 / G3 §6.4 / G4 §3.5 (provider_bindings) *동작 측면* 충분 — 별도 P 등록 *불필요* (Claude C-9 답습) |
   159	| **P14 (후보)** | **CLAUDE.md prompt-level Lock-in** — CLAUDE.md / system prompt 본문 내 특정 모델명 / vendor 분기 명시 | system-identity-prequel §7 ("메타포 강제 금지") 답습 + 헌법 5조 (Provider Liquidity) — 별도 P 등록 *불필요* (관용 권위로 흡수) |
   160	
   161	##### 1.2.5.2 본 §1.2.5 의 권위 한계
   162	
   163	- 본 §1.2.5 는 *deferred candidates* 만 등록 — **본 G2 PASS 시점 P1~P8 enumeration 변경 0건**
   164	- P9 ~ P12 정식 등록은 *각 후보의 정식 등록 시점* (위 표 4 행) 에 별도 합의 (단축 또는 풀 3+1)
   165	- 본 §1.2.5 변경 (P9~P12 정식 등록 / 추가 후보) 자체는 풀 3+1 합의 + ADR Amendment 절차 (T3 변경)
   166	- 본 §1.2.5 등록 후보가 *현 시점* enforcement 의무화 대상 *아님* — deferred candidates 는 *위험 식별 + 후속 합의 진입 trigger*
   167	
   168	##### 1.2.5.3 본 §1.2.5 가 *하지 않는* 것
   169	
   170	- ❌ P9 / P12 자동 정식 등록 (각 후보 별도 합의 시점) — **P10 은 §1.2.6 답습 정식 등록 완료 (2026-05-09 후속 5) / P11 은 §1.2.7 답습 정식 등록 완료 (2026-05-12)**
   171	- ❌ 현 G2 PASS 무력화 (deferred 는 *후속* 영역)
   172	- ❌ Hermes PMO 격상 전 P9 / P12 enforcement 의무 (격상 합의 시점 또는 별도 합의) — **P11 = Hermes PMO 격상 전 precondition 권장 (blocking 아님, Implementation/Runtime PASS 영역, §1.2.7 답습)**
   173	- ❌ P13 ~ P14 정식 등록 (관용 권위로 흡수, 별도 P 불필요)
   174	
   175	#### 1.2.6 Evidence Integrity 위반 경로 1건 (P10) — 정식 등록 (2026-05-09 후속 5)
   176	
   177	> **본 §1.2.6 는 §1.2.5.2 명시 "P10 정식 등록 시점 = PR-2 신규 ADR-012 발행 시점" 답습 흡수.** ADR-012 (Evidence Ledger Protection, 2026-05-09 후속 3 PR-2 발행) 시점이 P10 정식 등록 *트리거*. 본 후속 5 단축 합의 (Reviewer-only) 로 정식 등록.
   178	
   179	##### 1.2.6.1 P10 정식 row
   180	
   181	| # | 경로 | 시나리오 | Evidence Integrity 측면 (5건) | 관련 ADR / 게이트 / 합의 |
   182	|---|------|---------|--------------------------|------------------|
   183	| **P10** | **Evidence Forgery** | Evidence Ledger entry / external-review 응답 / 합의 보고서 / hash chain / GitHub Actions run artifact / commit history 가 *위조* 또는 *변조* 되어 (a) 잘못된 PASS 판정 / (b) Hermes-originated 변경 silent 수용 / (c) 합의 권위 silent 침해 / (d) 자동 정책 변경 위장 / (e) 외부 LLM 응답 위조 발생 | (i) Ledger entry 형식적 무결성 (11 필드 schema, hash chain) / (ii) prev_hash 검증 실패 처리 / (iii) git history rewrite 차단 / (iv) Hermes-originated commit auto-reject (변조 차단 매트릭스 4항목) / (v) external LLM response `agent="user"` 강제 | **ADR-012 §2.1 ~ §2.12 + §3.1 ~ §3.5** (12 보호 원칙 + 4 매트릭스 + 5 추가 의무) + **G3 §5** (Evidence decision principle: PASS 성립 4 요건 — Tools 검증 + Evidence Ledger entry + 사용자 명시 승인 + 합의 보고서 commit) + **G4 §4.2 / §4.4 / §4.6** (11 필드 schema + Layer 1~5 다층 강제 + Tier-based round-trip) + 본 PR-2 합의 (`docs/review/3plus1-consensus-2026-05-09-pr2-evidence-ledger.md`) |
   184	
   185	##### 1.2.6.2 P10 enforcement layer 매핑
   186	
   187	본 P10 enforcement 는 **ADR-012 직접 권위** + **G3 §5 + G4 §4** 답습. *별도 GP 신설 부재* (사용자 명시 답습 — 본 §1.2.6 = P10 row 추가 한정, GP 신설은 별도 합의 영역):
   188	
   189	| Enforcement Layer | 책임 영역 | 권위 |
   190	|----|--------|----|
   191	| **Layer 1** (Hash chain) | Middle entry tampering 차단 | ADR-012 §2.3 + G4 §4.4 (sha256 + canonical JSON) |
   192	| **Layer 2** (Git append-only) | History 재작성 차단 (denyNonFastForwards) | ADR-012 §2.3 (Layer 2 MANDATORY) |
   193	| **Layer 3** (Signed commit) | Host compromise 후 위조 차단 | ADR-012 §2.3 (Layer 3 RECOMMENDED MVP / MANDATORY multi-host) |
   194	| **Layer 4** (CI 회귀 검증) | canonical JSON 위반 / prev_hash mismatch / timestamp monotonicity 자동 검출 | ADR-012 §2.3 + R-6 workflow 답습 확장 (Implementation 영역) |
   195	| **Layer 5** (External anchor) | 1인 SPOF 완화 + 침해 후 발견 | ADR-012 §2.3 (Layer 5 RECOMMENDED MVP / MANDATORY P2 v3 정식 채택) |
   196	| **Hermes 변조 차단 매트릭스 4항목** | Hermes-originated entry / 파일 변조 / git commit / 외부 LLM 응답 위조 차단 | ADR-012 §2.12 (Gap-17 HIGH 흡수) + G3 §2.5 #11 / §4.5 / §2.2 #20 cross-reference |
   197	| **External LLM `agent="user"` 강제** | 사용자 직접 paste 시 Hermes 위조 차단 | ADR-012 §2.1 원칙 7 + §3.1 |
   198	
   199	##### 1.2.6.3 P10 처리 범위 (사용자 명시 답습)
   200	
   201	| 차원 | 본 §1.2.6 처리 |
   202	|----|----|
   203	| **상태** | Deferred Candidate (§1.2.5) → **Formal P-row (§1.2.6)** |
   204	| **처리 범위** | Design/Governance row 추가 한정 |
   205	| **Implementation status** | **Pending** — ADR-012 §10.2 답습 (실 runtime hook / migration script / CI step / pre-commit hook 미구현, 별도 Implementation/Runtime PASS 합의) |
   206	| **GP 매핑** | 별도 합의 영역 (본 §1.2.6 = P10 row 추가 한정, GP 신설 또는 기존 GP 매핑 갱신은 별도) |
   207	
   208	##### 1.2.6.4 P10 정식 등록의 합의 권위
   209	
   210	본 P10 정식 등록 = **단축 합의 (Reviewer-only) 적격** (사용자 명시 답습):
   211	- ADR-012 발행 (PR-2 풀 3+1 합의, 2026-05-09 후속 3) 권위 *내부* 작업
   212	- ADR-012 §11.2 + §1.3 cross-reference 의무 답습
   213	- 본 §1.2.6 = §1.2.5.2 deferred candidate 정식 등록 시점 명시 답습
   214	- 본 P10 정식 row 본문 = ADR-012 §2.1 ~ §2.12 + §3.1 ~ §3.5 답습 한정 (새 권위 결정 0건)
   215	
   216	**4 풀 3+1 승격 트리거 검증** (사용자 명시 답습):
   217	
   218	| 트리거 | 본 §1.2.6 |
   219	|----|----|
   220	| P10 이 기존 P1~P12 구조와 충돌 | ❌ — §1.2.5 deferred 에 이미 등록, 정식 row 승격은 §1.2.5.2 명시 트리거 답습 |
   520	
   521	### 5.7 의존 ADR / 갱신 후보
   522	
   523	- ADR-008 cross-reference (차단조건 #1 + #6 + 부록 B): 본문 변경 없음, GP-3 cross-reference 추가 (35번째 entry R-S1 정정 답습)
   524	- 헌법 8조: 본문 변경 없음 (T3 — ADR Amendment 절차 영역, 본 G2 범위 외)
   525	
   526	---
   527	
   528	## 6. GP-4 — 외부 입력 검증 (Hermes / Worker 출력 포함)
   529	
   530	### 6.1 정의
   531	
   532	Hermes 출력 + Worker Agent 출력 + LLM 응답 + tool output 모두를 *외부 입력*으로 분류하여 명시 검증 layer 를 거친다. ADR-011 §2.3 운영 함의 #1 ("Hermes 출력은 Tools 로 검증된다") 의 *입력 검증 측면* 구체화.
   533	
   534	**중요**: GP-4 는 헌법 8조 #3 (사용자 입력 검증) 의 *내부 출력 적용* 확장. Hermes / Worker 가 *내부* 처럼 신뢰되어 SQL injection / command injection / path traversal 등이 발생하지 않도록.
   535	
   536	### 6.2 위반 경로
   537	
   538	- **P5** — 외부 입력 미검증/이스케이프
   539	
   540	### 6.3 강제 메커니즘
   541	
   542	| 분류 | 메커니즘 | 위치 |
   543	|-----|---------|-----|
   544	| 계산적 | 입력 schema validation (pydantic / typing) | Worker Agent 입출력 인터페이스 |
   545	| 계산적 | regex sanitizer + escape (path traversal / SQL / command) | tool wrapper layer |
   546	| 계산적 | 명시 quote / parameterize (SQL bind variable, shlex.quote) | DB / shell tool layer |
   547	| 추론적 보조 | Reviewer Agent 의 prompt injection 감지 | Layer 5 (3+1 합의) |
   548	| 자동 롤백 | 검증 실패 → BLOCK + Evidence Ledger 기록 | Worker Agent runtime |
   549	
   550	### 6.4 Entry 기준
   551	
   552	- ✅ 헌법 8조 #3 (외부 입력 검증) 권위 (충족됨)
   553	- ✅ 헌법 5조 #4 (코드 품질 — 외부 입력만 검증) 명시 (충족됨)
   554	- ⏳ 사용자 명시 GP-4 작업 진입 결정
   555	
   556	### 6.5 Exit 기준
   557	
   558	| # | 조건 | 검증 방식 |
   559	|---|------|---------|
   560	| (a) | 동등 이상의 보안 결과 | Hermes / Worker 출력 sanitizer 통과 검증 + 의도적 injection payload 차단 시연 |
   561	| (b) | 격리 환경 PoC 실증 | path traversal payload + SQL bind 우회 payload + command injection payload → 모두 BLOCK 격리 환경 시연 |
   562	| (c) | ADR / SDD 권위 명시 | ADR-011 §2.3 운영 함의 #1 + 헌법 8조 #3 + 헌법 5조 #4 + 본 §6 |
   563	| (d) | 자동 회귀 검증 경로 확보 | CI step + injection canary 자동 회귀 (R-6 workflow 확장) |
   564	| (e) | 합의 APPROVE | 단축 또는 풀 3+1 합의 (G2 GP-4 한정 또는 G2 통합) |
   565	
   566	### 6.6 산출 후보
   567	
   568	- `tests/integration/test_input_validation.py` (injection canary)
   569	- Worker Agent / tool wrapper 입출력 schema 정의 (pydantic)
   570	- R-6 workflow 확장 — injection canary step
   571	- 합의 보고서
   572	
   573	### 6.7 의존 ADR / 갱신 후보
   574	
   575	- ADR-011 §2.3 운영 함의 #1 cross-reference
   576	- ADR-008 본문: GP-4 cross-reference (격상 후)
   577	
   578	---
   579	
   580	## 7. GP-5 — Provider Adapter 강제 (코드 레벨 lock-in 차단)
   581	
   582	### 7.1 정의
   583	
   584	Worker Agent / Skill / Hermes plugin 코드가 Hermes 자체 SDK / litellm / anthropic / openai 직접 import 또는 모델명 / Provider 분기 코드를 포함하지 않도록 depcruise 룰 + P1 facade 단일 진입점 + PR auto-reject 가 정적으로 강제한다.
   585	
   586	### 7.2 위반 경로
   587	
   588	- **P6** — Hermes 자체 SDK 직접 import
   589	- **P7** — 모델명 / Provider 분기 코드
   590	
   591	### 7.3 강제 메커니즘
   592	
   593	| 분류 | 메커니즘 | 위치 |
   594	|-----|---------|-----|
   595	| 계산적 | depcruise 룰 — Hermes / litellm / anthropic / openai 직접 import 금지 | `.dependency-cruiser.cjs` |
   596	| 계산적 | depcruise 룰 — 모델명 분기 패턴 정적 차단 (`model == "claude"` 등) | depcruise custom rule |
   597	| 계산적 | P1 facade 단일 진입점 강제 (`src/llm/facade.py` 외 LLM 호출 금지) | P1 v2 |
   598	| 자동 롤백 | depcruise 위반 PR → CI step FAIL → auto-reject | GitHub Actions |
   599	| 자동 롤백 | 인위적 분기 코드 PR → depcruise FAIL 확인 (ADR-008 §2.4 검증 #2) | CI step |
   600	
   601	### 7.4 Entry 기준
   602	
   603	- ✅ ADR-008 차단조건 #4 명시 (충족됨)
   604	- ⏳ P1 v2 facade MVP 완료 (P1 v2 §X — 본 G2 범위 외, 의존)
   605	- ⏳ 사용자 명시 GP-5 작업 진입 결정
   606	
   607	### 7.5 Exit 기준
   608	
   609	| # | 조건 | 검증 방식 |
   610	|---|------|---------|
   611	| (a) | 동등 이상의 보안 결과 | (Provider Liquidity 측면) Hermes / litellm / anthropic / openai 직접 import 0건 + 모델명 분기 0건 |
   612	| (b) | 격리 환경 PoC 실증 | 인위적 분기 코드 PR → depcruise FAIL 확인 시연 |
   613	| (c) | ADR / SDD 권위 명시 | ADR-008 차단조건 #4 + P1 v2 + 본 §7 |
   614	| (d) | 자동 회귀 검증 경로 확보 | CI step (depcruise) + PR auto-reject 매 PR 강제 |
   615	| (e) | 합의 APPROVE | 단축 또는 풀 3+1 합의 (G2 GP-5 한정 또는 G2 통합) |
   616	
   617	### 7.6 산출 후보
   618	
   619	- `.dependency-cruiser.cjs` (Hermes / LLM SDK 직접 import 금지 룰 + 모델명 분기 패턴 차단 룰)
   620	- P1 v2 facade MVP (본 GP-5 의존 — P1 작업과 통합)
   621	- CI step (depcruise + 인위적 분기 코드 PR 시연)
   622	- 합의 보고서
   623	
   624	### 7.7 의존 ADR / 갱신 후보
   625	
   626	- ADR-008 차단조건 #4: 본문 변경 없음, GP-5 cross-reference 추가
   627	- ADR-009 (자체 Adapter v2.0 진입조건): GP-5 충족과 자체 Adapter 진입의 관계 갱신 (격상 후)
   628	- P1 v2 (`llm-providers-design.md`): facade 단일 진입점 권위 cross-reference
   629	
   630	---
   631	
   632	## 8. GP-6 — Memory / Skill Migration 가능성 (학습 자산 lock-in 차단)
   633	
   634	### 8.1 정의
   635	
   636	Hermes 가 누적한 Memory / Skill 이 Hermes 의존 schema / binary protocol 에 종속되지 않도록 JSONL append-only 표준 + 변환 스크립트 (Hermes ↔ Claude Code / GPT 등) 1회 시연이 보장된다.
   637	
   638	**중요**: GP-6 은 **G4** (Provider-agnostic Memory/Skill 형식) 와 *공동 책임* — GP-6 은 *마이그레이션 가능성* 측면, G4 는 *형식 표준화* 측면. 둘은 동일 검증 산출 일부 공유 가능.
   639	
   640	### 8.2 위반 경로
   641	
   642	- **P8** — Memory / Skill Hermes 종속 형식
   643	
   644	### 8.3 강제 메커니즘
   645	
   646	| 분류 | 메커니즘 | 위치 |
   647	|-----|---------|-----|
   648	| 계산적 | JSONL schema 검증 (jq 파싱 + schema_version 체크) | export script |
   649	| 계산적 | 변환 스크립트 자동 테스트 (Hermes JSONL → Claude / GPT format) | `scripts/hermes-migration/` + CI step |
   650	| 계산적 | hermes sessions export → import 라운드트립 검증 | `tests/hermes/test_export_import.py` |
   651	| 추론적 보조 | 다른 오케스트레이터 import 결과 의미 보존 검증 (부분 추론) | manual review (분기 1회) |
   652	| 자동 롤백 | schema_version 호환 실패 → export 차단 | export script |
   653	
   654	### 8.4 Entry 기준
   655	
   656	- ✅ ADR-008 차단조건 #2 (JSONL export 표준) 명시 (충족됨)
   657	- ✅ ADR-008 부록 A.2 (Hermes sessions export 공식 명령 검증) (충족됨)
   658	- ⏳ G4 작업 진입 또는 병행 (본 §8 은 *마이그레이션 가능성* 측면, G4 는 *형식 표준화* 측면)
   659	- ⏳ 사용자 명시 GP-6 작업 진입 결정
   660	
   661	### 8.5 Exit 기준
   662	
   663	| # | 조건 | 검증 방식 |
   664	|---|------|---------|
   665	| (a) | 동등 이상의 보안 결과 | (Provider Liquidity 측면) Hermes lock-in 차단 — 다른 오케스트레이터로 학습 자산 import 가능 |
   666	| (b) | 격리 환경 PoC 실증 | hermes sessions export → claude_to_hermes / hermes_to_gpt 변환 → 다른 오케스트레이터 import → 의미 보존 검증 (R2-5 답습) |
   667	| (c) | ADR / SDD 권위 명시 | ADR-008 차단조건 #2 + G4 cross-reference + 본 §8 |
   668	| (d) | 자동 회귀 검증 경로 확보 | CI step (export → 변환 → schema 검증) + Hermes 메이저 업데이트 시점 자동 회귀 |
   669	| (e) | 합의 APPROVE | 단축 또는 풀 3+1 합의 (G2 GP-6 + G4 통합 가능) |
   670	
   671	### 8.6 산출 후보
   672	
   673	- `scripts/hermes-migration/hermes_to_claude.py` (변환 스크립트, R2-5 답습)
   674	- `scripts/hermes-migration/hermes_to_gpt.py`
   675	- `tests/hermes/test_export_import.py` (라운드트립 검증)
   676	- CI step (export → 변환 → schema 검증)
   677	- 합의 보고서 (G4 와 통합 가능)
   678	
   679	### 8.7 의존 ADR / 갱신 후보
   680	
   681	- ADR-008 차단조건 #2: 본문 변경 없음, GP-6 + G4 cross-reference 추가
   682	- ADR-009 (자체 Adapter v2.0 진입조건): GP-6 / G4 충족과 자체 Adapter 진입의 관계 갱신
   683	- 신규 ADR 후보 (P2 v3 §6.7 등록): ADR-014 (Provider-agnostic Memory/Skill Format) — G4 통합 시점
   684	
   685	---
   686	
   687	## 9. 메타 안전장치 — Hermes 자기참조 차단
   688	
   689	### 9.1 문제 정의
   690	
   691	본 6 거버넌스 사전조건이 Hermes 자체에 의해 *변경* 또는 *우회* 될 수 있다면, GP-1 ~ GP-6 의 권위는 무력화된다 — *fox guarding the henhouse* 문제. 따라서 본 §9 는 6 GP 자체의 *무결성* 을 보호한다.
   692	
   693	### 9.2 강제 메커니즘 (G3 와의 인터페이스)
   694	
   695	> **본 §9 는 강제 메커니즘 *interface* 만 명시**. 본격적인 운영 구현은 **G3 ("Hermes ≠ root of trust" 운영 구현)** 범위 — 본 G2 는 *interface* 까지.
   696	
   697	| # | 메커니즘 | 권위 근거 | G3 위치 |
   698	|---|---------|--------|--------|
   699	| 1 | filesystem read-only on `docs/architecture/governance-preconditions.md` (Hermes container mount ro) | ADR-011 §2.4 T3 + system-identity-prequel §3.3 #1 | G3 §5.2 #5 |
   700	| 2 | 본 문서 변경은 *git commit* 으로만 권위 인정 (Hermes-originated commit auto-reject) | system-identity-prequel §3.3 #2 + G3 §5.5 (합의 인프라 순환 권위 해결) | G3 §5.5 |

exec
/bin/bash -lc 'rg -n "P11|Supply-chain|checksum|hash|lock diff|dependency" docs/architecture/governance-preconditions.md' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
13:> **§1.2.7 P11 Supply-chain Compromise 정식 등록 (2026-05-12 단축 합의 적격 — Reviewer-only)**: Gate Enforcement Layer 보호 보강 (G3 §2.6, 2026-05-12 commits `3e46440` + `fa2cbdb`) 시점 트리거 답습. 5 측면 (Dependency Pinning Integrity / Checksum / Action SHA Pin / Docker Digest Pin / Vendor Change Auto-recheck) + 5 Layer 다층 강제 + Enforcement Tool Self-protection + 5 기준 (감지/차단/Evidence/Rollback/사용자 승인). **Hermes PMO 격상 *전* precondition 권장 (blocking 아님)** — Implementation/Runtime PASS 영역의 우선 권장 항목 (Claude C-3 + C-6 답습). 외부 LLM Gap-N 중 N-5 (supply chain / dependency integrity) 답습. **본 §1.2.7 = P11 row 추가 한정 — runtime code 구현 / CI workflow 수정 / hook 구현 / 신규 GP 신설 / 신규 ADR 발행 / Hermes PMO 격상 / Operational Readiness PASS / Implementation/Runtime PASS / G2/G3/G4 PASS 재선언 / ADR 본문 자동 갱신 모두 본 작업 범위 외** (사용자 명시 답습).
118:#### 1.2.3 정식 위반 경로 합산 (P1~P8 + P10 + P11, 2026-05-12 갱신)
124:Supply-chain Integrity 위반 경로 = 1건 (P11)        ← 2026-05-12 정식 등록
126:정식 위반 경로 합계 = 10건 (P1~P8 + P10 + P11)     ← ✅ 합의 §29~§30 일치 + ADR-012 발행 시점 P10 흡수 + Gate Enforcement Layer 보호 보강 시점 P11 흡수
132:P11 정식 등록 = Gate Enforcement Layer 보호 보강 (2026-05-12, commits `3e46440` + `fa2cbdb`) 시점 트리거 — §1.2.5 명시 "P11 정식 등록 시점 = SBOM + supply-chain 검증 PoC 합의 시점, Hermes PMO 격상 *전* 권장" + 본 보강 작업의 Layer 2 (CI / hook / test) enforcement mechanism 이 supply-chain compromise 로 무력화 가능 + 외부 LLM Gap-N 중 N-5 supply chain / dependency integrity 답습. 본 §1.2.7 답습.
151:| ~~**P11 (후보)**~~ → **P11 (정식 등록 완료, §1.2.7 답습, 2026-05-12)** | **Supply-chain Compromise** — Hermes / pysqlcipher3 / litellm / Hermes-agent 의존성 또는 GitHub Actions runner / Docker base image 침해 | 자동 redaction 무력화 / SQLCipher trigger silent 깨짐 / canary catalog silent 변경 / R-6 actual run 위장 / Gate Enforcement Layer Layer 1~4 (lint/test/hook/CI) 무력화 | ✅ **정식 등록 완료 (§1.2.7 답습)** | ✅ **2026-05-12** — Gate Enforcement Layer 보호 보강 (commits `3e46440` + `fa2cbdb`) 시점 트리거 답습 → 본 단축 합의 (Reviewer-only) 로 정식 등록. **Hermes PMO 격상 *전* precondition (권장)** — blocking 까지는 아님, Implementation/Runtime PASS 영역의 *우선 권장 항목* (Claude C-3 + C-6 답습) |
170:- ❌ P9 / P12 자동 정식 등록 (각 후보 별도 합의 시점) — **P10 은 §1.2.6 답습 정식 등록 완료 (2026-05-09 후속 5) / P11 은 §1.2.7 답습 정식 등록 완료 (2026-05-12)**
172:- ❌ Hermes PMO 격상 전 P9 / P12 enforcement 의무 (격상 합의 시점 또는 별도 합의) — **P11 = Hermes PMO 격상 전 precondition 권장 (blocking 아님, Implementation/Runtime PASS 영역, §1.2.7 답습)**
183:| **P10** | **Evidence Forgery** | Evidence Ledger entry / external-review 응답 / 합의 보고서 / hash chain / GitHub Actions run artifact / commit history 가 *위조* 또는 *변조* 되어 (a) 잘못된 PASS 판정 / (b) Hermes-originated 변경 silent 수용 / (c) 합의 권위 silent 침해 / (d) 자동 정책 변경 위장 / (e) 외부 LLM 응답 위조 발생 | (i) Ledger entry 형식적 무결성 (11 필드 schema, hash chain) / (ii) prev_hash 검증 실패 처리 / (iii) git history rewrite 차단 / (iv) Hermes-originated commit auto-reject (변조 차단 매트릭스 4항목) / (v) external LLM response `agent="user"` 강제 | **ADR-012 §2.1 ~ §2.12 + §3.1 ~ §3.5** (12 보호 원칙 + 4 매트릭스 + 5 추가 의무) + **G3 §5** (Evidence decision principle: PASS 성립 4 요건 — Tools 검증 + Evidence Ledger entry + 사용자 명시 승인 + 합의 보고서 commit) + **G4 §4.2 / §4.4 / §4.6** (11 필드 schema + Layer 1~5 다층 강제 + Tier-based round-trip) + 본 PR-2 합의 (`docs/review/3plus1-consensus-2026-05-09-pr2-evidence-ledger.md`) |
194:| **Layer 4** (CI 회귀 검증) | canonical JSON 위반 / prev_hash mismatch / timestamp monotonicity 자동 검출 | ADR-012 §2.3 + R-6 workflow 답습 확장 (Implementation 영역) |
233:- ❌ P9 / P12 자동 정식 등록 (각 후보 별도 합의 시점 답습) — **P11 은 §1.2.7 답습 정식 등록 완료 (2026-05-12)**
241:#### 1.2.7 Supply-chain Integrity 위반 경로 1건 (P11) — 정식 등록 (2026-05-12)
243:> **본 §1.2.7 은 §1.2.5 명시 "P11 정식 등록 시점 = SBOM + supply-chain 검증 PoC 합의 시점, Hermes PMO 격상 *전* 권장" 답습 흡수.** Gate Enforcement Layer 보호 보강 (2026-05-12, commits `3e46440` + `fa2cbdb`) 시점이 P11 정식 등록 *트리거* — 본 보강 작업의 Layer 2 (CI / hook / test) enforcement mechanism 이 supply-chain compromise 로 무력화 가능 + 외부 LLM Gap-N 중 N-5 supply chain / dependency integrity 답습. 본 후속 단축 합의 (Reviewer-only) 로 정식 등록.
245:##### 1.2.7.1 P11 정식 row
247:| # | 경로 | 시나리오 | Supply-chain Integrity 측면 (5건) | 관련 ADR / 게이트 / 합의 |
249:| **P11** | **Supply-chain Compromise** | (a) Hermes / pysqlcipher3 / litellm / Hermes-agent / agents-sdk 의존성 (PyPI / 외부 소스) 침해 — 악성 코드 주입 / typosquatting / dependency confusion (b) GitHub Actions runner image / 3rd-party action 침해 — workflow step 위장 / artifact 변조 (c) Docker base image 침해 — 자동 redaction 무력화 / canary catalog silent 변경 / SQLCipher trigger silent 깨짐 (d) Vendor 변경 silent — `hermes-version.yaml` / `requirements.txt` / `pyproject.toml` / lock 파일의 silent drift (e) Tooling supply chain — `import-linter` / `grimp` / `rfc8785` / `jcs` / `gitleaks` 등 *enforcement tool 자체* 침해 → Gate Enforcement Layer Layer 1~4 무력화 | (i) **Dependency Pinning Integrity** — `hermes-version.yaml` v0.12.0 명시 + `requirements.txt` / `pyproject.toml` / `poetry.lock` 정확 핀 + lock 파일 git diff 회귀 검출 (G3 §3.2.2 #3 답습) / (ii) **Checksum / Hash Verification** — pip install `--require-hashes` + SBOM 정합성 + 패키지 sha256 매니페스트 검증 / (iii) **GitHub Actions Action SHA Pinning** — `uses: actions/checkout@<commit_sha>` (not `@v4` tag) + 3rd-party action 사용 시 commit SHA pin 강제 / (iv) **Docker Base Image / Runner Image Immutability** — `FROM python:3.11@sha256:<digest>` digest 고정 + reproducible build + cosign 또는 동등 image signing verification (별도 합의 영역) / (v) **Vendor Change Auto-recheck** — 의존성 lock diff 검출 시 R-6 actual run 자동 R-2 / R-4.1 PoC 재실행 + canary 자동 검증 PASS 후만 merge (G3 §3.2.3 #2 답습) | **G3 §3.2** (Upstream Silent Breakage 5 측면 + ROLLBACK trigger R6) + **G3 §2.5 #14** (`hermes-version.yaml` + dependency lock T2 사용자 명시 PR merge) + **G3 §2.6** (Gate Enforcement Layer 보호 — Layer 1~4 enforcement mechanism 무력화 위험 cross-reference) + **GP-2 / GP-3 / GP-5** (redaction / credential / provider lock-in supply-chain 침해 시 무력화 위험 cross-reference) + **ADR-008 차단조건 #3** (Hermes 의존성 업그레이드 자동 R-2 재실행) + **외부 LLM Gap-N 중 N-5** (supply chain / dependency integrity 답습) + 본 §1.2.7 단축 합의 (Reviewer-only) |
251:##### 1.2.7.2 P11 enforcement layer 매핑 (5 Layer 다층 강제)
253:본 P11 enforcement 는 **G3 §3.2 직접 권위** + **G3 §2.5 #14** + **GP-2/GP-3/GP-5 cross-reference** 답습. *별도 GP 신설 부재* (사용자 명시 답습 — 본 §1.2.7 = P11 row 추가 한정, GP 신설은 별도 합의 영역):
259:| **Layer 3** (Checksum / Hash Verification + SBOM) | Tampered package 차단 | pip `--require-hashes` + SBOM 정합성 (예: `pip-audit` / `safety` / `cyclonedx-py`) + 별도 합의 영역 (Implementation/Runtime PASS — SBOM 생성 / 검증 hook) |
260:| **Layer 4** (CI 회귀 검증 — Vendor Change Auto-recheck) | 의존성 lock diff 감지 시 자동 R-2 / R-4.1 PoC 재실행 + canary 자동 검증 + R-6 actual run PASS 후만 merge | G3 §3.2.2 #3 + §3.2.3 #2 (이미 G3 본문 권위) + R-6 workflow 답습 확장 (Implementation 영역) |
262:| **Enforcement Tool Self-protection** | `import-linter` / `grimp` / `rfc8785` / `jcs` / `gitleaks` 등 Gate Enforcement Layer 가 사용하는 도구 자체의 SBOM + pin 강제 | 본 P11 핵심 — Gate Enforcement Layer Layer 1~4 가 *사용하는 도구* 자체가 supply-chain 침해 시 Layer 1~4 무력화 위험. G3 §2.6.3 (b) Hook / CI workflow 비활성화 차단 답습 확장 |
264:##### 1.2.7.3 P11 5 기준 (감지 / 차단 / Evidence / Rollback / 사용자 승인)
268:| **감지 (Detection)** | (1) `requirements.txt` / `pyproject.toml` / `poetry.lock` / `hermes-version.yaml` git diff 자동 점검 (every commit + nightly) (2) GitHub Actions workflow `uses:` action 의 `@<tag>` vs `@<sha>` 패턴 자동 점검 (3) Docker `FROM` 의 `@sha256:<digest>` 정합성 점검 (4) `pip install --require-hashes` 강제 — hash 부재 시 install 차단 (5) SBOM diff 검출 (cyclonedx-py 등, 별도 합의) | G3 §3.2.2 답습 + Layer 2 / Layer 3 cross-reference |
269:| **차단 (Blocking)** | (1) `hermes-version.yaml` / lock 파일 미명시 또는 silent drift = PR auto-reject (2) Action `@<tag>` 형태 사용 = workflow 검증 step FAIL (3) Docker base image digest 부재 = image build BLOCK (4) `pip install` hash mismatch = install BLOCK (5) Vendor 변경 PR 시 R-2 / R-4.1 PoC 자동 재실행 FAIL = merge BLOCK (G3 §3.2.3 #2 답습) | G3 §3.2.3 + Layer 1 ~ Layer 4 |
270:| **Evidence** | (i) Markdown report: 의존성 변경 본문 + lock diff + SBOM diff (ii) JSONL ledger entry: `{"event": "upstream_recheck", "agent": "user", "result": "PASS"|"FAIL", "ref": "<run_id>", "content": {"diff": "<lock_diff_summary>", "sbom_delta": [...]}}` (G3 §3.2.4 답습) (iii) GitHub Actions run ID + verdict PASS evidence (iv) Artifact `r2-r4-canary-evidence` 답습 (canary-output.log + canary-evidence.json) (v) **`agent="user"` 강제** (ADR-012 §2.1 원칙 7 답습 — Hermes-originated dependency upgrade PR 자동 merge 차단) | G3 §3.2.4 + ADR-012 §2.1 + Layer 4 |
271:| **Rollback** | (1) R-7 SOP §5 ROLLBACK trigger R6 (upstream breakage) 답습 — `hermes-version.yaml` 변경 PR 의 R-6 actual run FAIL 시 (2) 이전 버전 핀 복귀 + canary catalog 재검증 + 사용자 명시 검토 (3) supply-chain 침해 의심 시 → 침해 의심 dependency 영구 격리 + 외부 LLM 의견 의무 (cross-vendor verification) (4) Gate Enforcement Layer Layer 1~4 무력화 의심 시 → Hermes 컨테이너 정지 + 사용자 명시 alert + G3 §2.6.5 답습 (`gate_enforcement_bypass_detected` rollback_trigger 발화) | G3 §3.2.5 + R-7 SOP §5 + G3 §2.6.5 |
274:##### 1.2.7.4 P11 처리 범위 (사용자 명시 답습)
280:| **Implementation status** | **Pending** — 별도 Implementation/Runtime PASS 합의 (실 SBOM 생성 / 검증 hook / Action SHA pin lint / Docker digest 검증 / pip --require-hashes 강제 / SBOM diff 회귀 검증 step 모두 미구현) |
281:| **GP 매핑** | 별도 합의 영역 (본 §1.2.7 = P11 row 추가 한정, GP 신설 또는 기존 GP 매핑 갱신은 별도) — 단, *enforcement 권위* = G3 §3.2 + §2.5 #14 + §2.6 직접 답습 |
282:| **Hermes PMO 격상 전 blocking 또는 precondition** | **Precondition 권장 (blocking 아님)** — Implementation/Runtime PASS 영역의 *우선 권장 항목* (Claude C-3 + C-6 답습). 격상 합의 시점에 P11 enforcement layer 5 layer 中 Layer 1 + Layer 4 *최소* 충족 의무 (Layer 2 + 3 + 5 = 격상 *후* 단계적 강화 권장) |
284:##### 1.2.7.5 P11 정식 등록의 합의 권위
286:본 P11 정식 등록 = **단축 합의 (Reviewer-only) 적격** (사용자 명시 답습):
288:- 외부 LLM Gap-N 중 N-5 (supply chain / dependency integrity) 답습 — *원안 도입 아님*
289:- §1.2.5 명시 "P11 정식 등록 시점 = SBOM + supply-chain 검증 PoC 합의 시점, Hermes PMO 격상 *전* 권장" → 본 시점 = Gate Enforcement Layer 보호 보강 + 외부 LLM Gap-N N-5 trigger 답습
290:- 본 P11 정식 row 본문 = G3 §3.2 / §2.5 #14 / §2.6 / ADR-008 차단조건 #3 / R-7 SOP §5 답습 한정 (새 권위 결정 0건)
296:| P11 이 기존 P1~P12 구조와 충돌 | ❌ — §1.2.5 deferred 에 이미 등록, 정식 row 승격은 §1.2.5 명시 트리거 답습 |
297:| Supply-chain Compromise 가 G3 §3.2 범위를 넘어 새 정책 변경 요구 | ❌ — G3 §3.2 + §2.5 #14 + §2.6 + ADR-008 차단조건 #3 답습 한정, 새 정책 0건 |
306:- ❌ runtime code 구현 (SBOM 생성 / 검증 hook / Action SHA pin lint / Docker digest 검증 / pip --require-hashes 강제 / SBOM diff 회귀 검증 step / cosign 통합 / sigstore Rekor 통합 등)
310:- ❌ 신규 ADR 발행 (Supply-chain Integrity ADR 후보 검토는 별도)
313:- ❌ Hermes PMO 격상 자동 선언 — P11 = **precondition 권장 (blocking 아님)**
324:본 P11 정식 등록은 Gate Enforcement Layer 보호 보강 (G3 §2.6) 의 **Layer 1~4 enforcement mechanism 무력화 위험** 흡수:
326:- **G3 §2.6.3 (b)** Hook / CI workflow 비활성화 차단 = P11 Layer 2 답습 (Action SHA pin + Docker digest pin)
327:- **G3 §2.6.5 위협 모델 TM-5 ~ TM-6** Layer 1~4 silent override / Hook 비활성화 = P11 supply-chain compromise 의 *직접 발생 경로* (의존성 침해 시 lint/test/CI/hook *도구 자체* 가 침해되어 silent PASS 가능)
329:- **G4 §3.8.2 #10** `gate_enforcement_bypass_detected` rollback_trigger = P11 침해 의심 시 자동 발화 + Skill `revoked` 자동 전이
331:본 cross-reference 강화로 **Gate Enforcement Layer 보호 (G3 §2.6) ↔ Supply-chain Integrity (P11)** 양방향 보호 *완결성* 확보 — 1 layer 만 깨져도 enforcement 무력화 위험 잔존 (예: Layer 1~4 hook 정상 + supply-chain 침해 시 hook *도구 자체* 가 침해되어 silent PASS).
595:| 계산적 | depcruise 룰 — Hermes / litellm / anthropic / openai 직접 import 금지 | `.dependency-cruiser.cjs` |
619:- `.dependency-cruiser.cjs` (Hermes / LLM SDK 직접 import 금지 룰 + 모델명 분기 패턴 차단 룰)
729:- (iii) 단일 GitHub remote 탈취 시 → push 후 force-push 로 합의 보고서 변조 가능 (hash chain 보강 후에도 origin replace 위험)
740:| (4) | 외부 LLM 의뢰·응답 자동화 | 외부 LLM 응답 hash 검증 + signed manifest 의무 |

exec
/bin/bash -lc "nl -ba src/adapters/llm/facade.py; nl -ba src/adapters/llm/redaction.py | sed -n '1,240p'; nl -ba src/adapters/llm/redaction_patterns.py | sed -n '1,220p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	"""LLMFacade — Provider-agnostic facade (G2 GP-5).
     2	
     3	본 파일은 *유일하게* LiteLLM 직접 import 가 *허용되는 경로* 입니다 (§4.1 답습).
     4	
     5	SC-1 (65 entry, TR-1 발효): **facade redaction layer real (R-2 GP-2 prevention)** —
     6	`complete()` 가 Router 위임 *전* request body 를 RedactionFilter 통과 (송신 secret strip).
     7	**LiteLLM Router 위임 = Provider Liquidity sub-cycle deferred** (full facade real 아님).
     8	
     9	답습 출처:
    10	  - docs/architecture/llm-providers-design.md §4.1 (정확히 이 파일만 LiteLLM 직접 import) + §8.2 (RedactionFilter)
    11	  - docs/architecture/governance-preconditions.md §4.1 (LLM API request body secret 차단)
    12	  - docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md §2.3 (Hermes PMO ↔ provider 영구 권위)
    13	  - docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md (SC-1 scope)
    14	  - docs/review/3plus1-consensus-2026-05-28-mvp2-sc1.md (B-1~B-4 흡수)
    15	"""
    16	from __future__ import annotations
    17	
    18	from dataclasses import dataclass
    19	from typing import Any
    20	
    21	from src.adapters.llm.redaction import RedactionFilter
    22	
    23	
    24	@dataclass(frozen=True)
    25	class LLMRequest:
    26	    alias: str
    27	    messages: list[dict[str, str]]
    28	    metadata: dict[str, Any] | None = None
    29	
    30	
    31	@dataclass(frozen=True)
    32	class LLMResponse:
    33	    content: str
    34	    metadata: dict[str, Any]
    35	
    36	
    37	class LLMFacade:
    38	    """LLM 호출 단일 진입점. redaction layer real, Router 위임 deferred (SC-1)."""
    39	
    40	    def __init__(self, registry_path: str, redactor: RedactionFilter | None = None) -> None:
    41	        self._registry_path = registry_path
    42	        self._redactor: RedactionFilter = redactor if redactor is not None else RedactionFilter()
    43	
    44	    def _redact_request(self, request: LLMRequest) -> dict[str, Any]:
    45	        """송신 전 request body redaction (GP-2 prevention — Router 위임 전 호출, B-4 범위 = messages + metadata)."""
    46	        return {
    47	            "messages": self._redactor.redact_messages(request.messages),
    48	            "metadata": (
    49	                self._redactor.scrub(request.metadata) if request.metadata is not None else None
    50	            ),
    51	        }
    52	
    53	    def complete(self, request: LLMRequest) -> LLMResponse:
    54	        # GP-2 prevention: 송신 전 secret strip (redaction layer operative)
    55	        redacted = self._redact_request(request)
    56	        # Router 위임 = Provider Liquidity sub-cycle deferred (RT-1: 실 송신 0 = 미부착 window 없음)
    57	        raise NotImplementedError(
    58	            "LiteLLM Router 위임 = Provider Liquidity sub-cycle deferred "
    59	            f"(SC-1 redaction layer operative — {len(redacted['messages'])} messages redacted)"
    60	        )
    61	
    62	    async def health(self) -> dict[str, bool]:
    63	        return {}
     1	"""RedactionFilter — GP-2 R-2 prevention (LLM 송신 request body secret strip).
     2	
     3	SC-1 (65 entry) 합의 산출 (`docs/review/3plus1-consensus-2026-05-28-mvp2-sc1.md`):
     4	  - 권위: governance §4.1 ("LLM API request body 에 secret 노출 차단") + 64 trajectory §3
     5	          (§8.2 RedactionFilter = egress scrub 보조)
     6	  - B-1 (ii): Tier-1 45 catalog single source = redaction_patterns (detection 과 공유)
     7	  - B-2: group-aware 치환 — secret *값* 만 마스킹, key명/JSON 구조 보존 (whole-match 금지)
     8	  - R-3: scrub() KEY_BLACKLIST (dict key 기반 redaction, §8.2 답습)
     9	
    10	GP-2 prevention 핵심 = 송신 (redact_messages). 응답/로그 redaction = 보조 (scrub).
    11	순수 함수 / 원본 불변 (R-1) — frozen 의도.
    12	"""
    13	from __future__ import annotations
    14	
    15	import re
    16	from typing import Any
    17	
    18	from src.adapters.llm.redaction_patterns import (
    19	    COMPILED_PATTERNS,
    20	    REDACTION_MARK,
    21	    REDACTION_VALUE_GROUP,
    22	    SKIP_DIRECT_REGISTER,
    23	)
    24	
    25	# §8.2 KEY_BLACKLIST — dict key 기반 redaction (값 통째 마스킹)
    26	KEY_BLACKLIST: frozenset[str] = frozenset(
    27	    {"api_key", "apikey", "token", "secret", "auth", "credential", "authorization", "password"}
    28	)
    29	
    30	
    31	def _redact_match(m: re.Match[str], value_group: int) -> str:
    32	    """단일 매칭 → group-aware 치환 (B-2). 값만 [REDACTED], key명/구분자 보존."""
    33	    if value_group == 0:
    34	        # whole match 가 secret 값 (prefix/JWT/private key — key명 없음)
    35	        return REDACTION_MARK
    36	    full = m.group(0)
    37	    if value_group == -1:
    38	        # alternation (capturing group 없음) → 첫 '=' 뒤만 (delimiter+key 보존)
    39	        eq = full.find("=")
    40	        return full[: eq + 1] + REDACTION_MARK if eq != -1 else REDACTION_MARK
    41	    # value_group > 0 → 해당 capturing group span 만 마스킹
    42	    if m.lastindex and value_group <= m.lastindex and m.group(value_group) is not None:
    43	        off = m.start()
    44	        start, end = m.span(value_group)
    45	        return full[: start - off] + REDACTION_MARK + full[end - off :]
    46	    return REDACTION_MARK
    47	
    48	
    49	class RedactionFilter:
    50	    """모든 LLM 송신/응답/로그에서 비밀값 자동 strip (GP-2 prevention)."""
    51	
    52	    def redact_text(self, text: str) -> str:
    53	        """str 에서 Tier-1 45 catalog 매칭 secret 값 group-aware 마스킹."""
    54	        result = text
    55	        for pid, _src, _cat, _vendor, pattern in COMPILED_PATTERNS:
    56	            if pid in SKIP_DIRECT_REGISTER:
    57	                continue
    58	            value_group = REDACTION_VALUE_GROUP.get(pid, 0)
    59	            result = pattern.sub(lambda m, vg=value_group: _redact_match(m, vg), result)
    60	        return result
    61	
    62	    def redact_messages(self, messages: list[dict[str, Any]]) -> list[dict[str, Any]]:
    63	        """송신 request body redaction (GP-2 prevention 핵심). 원본 불변 (R-1)."""
    64	        out: list[dict[str, Any]] = []
    65	        for msg in messages:
    66	            new_msg = dict(msg)  # shallow copy (원본 dict 불변)
    67	            content = new_msg.get("content")
    68	            if isinstance(content, str):
    69	                new_msg["content"] = self.redact_text(content)
    70	            elif isinstance(content, (list, dict)):
    71	                # multimodal/tool structured content → 재귀 (R-5)
    72	                new_msg["content"] = self.scrub(content)
    73	            out.append(new_msg)
    74	        return out
    75	
    76	    def scrub(self, obj: Any) -> Any:
    77	        """dict/list/str 재귀 redaction (응답/메트릭/로그, §8.2) + KEY_BLACKLIST (R-3). 원본 불변."""
    78	        if isinstance(obj, dict):
    79	            result: dict[Any, Any] = {}
    80	            for key, value in obj.items():
    81	                if isinstance(key, str) and key.lower() in KEY_BLACKLIST:
    82	                    # blacklist key → 값 통째 마스킹 (str) 또는 재귀
    83	                    result[key] = REDACTION_MARK if isinstance(value, str) else self.scrub(value)
    84	                else:
    85	                    result[key] = self.scrub(value)
    86	            return result
    87	        if isinstance(obj, list):
    88	            return [self.scrub(item) for item in obj]
    89	        if isinstance(obj, str):
    90	            return self.redact_text(obj)
    91	        return obj  # int / float / bool / None — 비밀 아님
     1	"""Tier-1 secret pattern catalog — single source (detection + prevention 공유).
     2	
     3	본 모듈은 SC-1 (65 entry) 합의 B-1 (ii) 공유 모듈 추출 산출:
     4	  - `tools/secret_scanner.py` (detection, GP-3 + GP-2 D-2 scan-log)
     5	  - `src/adapters/llm/redaction.py` (prevention, GP-2 R-2 facade RedactionFilter 송신 redaction)
     6	둘 다 본 catalog 를 import → detection ↔ prevention 패턴 drift 0 (single source).
     7	
     8	⚠️ 패턴 *내용* (id / source / category / vendor / regex) = R-4.1 §4.1 직접 답습 변경 0건.
     9	secret_scanner 에서 literal 그대로 이동 (equivalence test 강제: len(ALL_PATTERNS)==45 + snapshot 동일).
    10	
    11	답습 출처:
    12	  - docs/phase0/r4-1-trigger-extension-evidence.md §4.1 (Tier-1 42 + baseline 5 = 45)
    13	  - docs/architecture/redaction-pattern-equivalence.md (R-4 패턴 동등성)
    14	  - docs/architecture/llm-providers-design.md §8.2 (RedactionFilter 설계)
    15	  - docs/review/3plus1-consensus-2026-05-28-mvp2-sc1.md (B-1 (ii) + B-2 group-aware 치환)
    16	"""
    17	from __future__ import annotations
    18	
    19	import re
    20	
    21	# ============================================================================
    22	# Tier-1 패턴 카탈로그 (45종) — R-4.1 §4.1 직접 답습 (secret_scanner literal 이동, 변경 0)
    23	#
    24	# 형식: (id, source, category, vendor, regex)
    25	# ============================================================================
    26	
    27	# Baseline 5 prefix (R-2 PoC 보존 — R-4.1 §4.1)
    28	BASELINE_PREFIX: list[tuple[str, str, str, str, str]] = [
    29	    ("BL-1", "Hermes #1 (sk-ant-)", "prefix-baseline", "Anthropic",
    30	     r"sk-ant-[A-Za-z0-9_-]{10,}"),
    31	    ("BL-2", "Hermes #1 (sk-)", "prefix-baseline", "OpenAI/Anthropic/etc",
    32	     r"sk-[A-Za-z0-9_-]{10,}"),
    33	    ("BL-3", "Hermes #2", "prefix-baseline", "GitHub PAT classic",
    34	     r"ghp_[A-Za-z0-9]{10,}"),
    35	    ("BL-4", "Hermes #15", "prefix-baseline", "AWS Access Key ID",
    36	     r"AKIA[A-Z0-9]{16}"),
    37	    ("BL-5", "Hermes #8", "prefix-baseline", "Slack tokens",
    38	     r"xox[baprs]-[A-Za-z0-9-]{10,}"),
    39	]
    40	
    41	# Tier-1 prefix 31 (Hermes #3..#7, #9..#14, #16..#35) — R-4.1 §4.1 직접 답습
    42	PREFIX_PATTERNS: list[tuple[str, str, str, str, str]] = [
    43	    ("T1-001", "Hermes #3", "prefix", "GitHub PAT (fine-grained)",
    44	     r"github_pat_[A-Za-z0-9_]{10,}"),
    45	    ("T1-002", "Hermes #4", "prefix", "GitHub OAuth access token",
    46	     r"gho_[A-Za-z0-9]{10,}"),
    47	    ("T1-003", "Hermes #5", "prefix", "GitHub user-to-server",
    48	     r"ghu_[A-Za-z0-9]{10,}"),
    49	    ("T1-004", "Hermes #6", "prefix", "GitHub server-to-server",
    50	     r"ghs_[A-Za-z0-9]{10,}"),
    51	    ("T1-005", "Hermes #7", "prefix", "GitHub refresh token",
    52	     r"ghr_[A-Za-z0-9]{10,}"),
    53	    ("T1-006", "Hermes #9", "prefix", "Google API keys",
    54	     r"AIza[A-Za-z0-9_-]{30,}"),
    55	    ("T1-007", "Hermes #10", "prefix", "Perplexity",
    56	     r"pplx-[A-Za-z0-9]{10,}"),
    57	    ("T1-008", "Hermes #11", "prefix", "Fal.ai",
    58	     r"fal_[A-Za-z0-9_-]{10,}"),
    59	    ("T1-009", "Hermes #12", "prefix", "Firecrawl",
    60	     r"fc-[A-Za-z0-9]{10,}"),
    61	    ("T1-010", "Hermes #13", "prefix", "BrowserBase",
    62	     r"bb_live_[A-Za-z0-9_-]{10,}"),
    63	    ("T1-011", "Hermes #14", "prefix", "Codex encrypted tokens",
    64	     r"gAAAA[A-Za-z0-9_=-]{20,}"),
    65	    ("T1-012", "Hermes #16", "prefix", "Stripe secret key (live)",
    66	     r"sk_live_[A-Za-z0-9]{10,}"),
    67	    ("T1-013", "Hermes #17", "prefix", "Stripe secret key (test)",
    68	     r"sk_test_[A-Za-z0-9]{10,}"),
    69	    ("T1-014", "Hermes #18", "prefix", "Stripe restricted key",
    70	     r"rk_live_[A-Za-z0-9]{10,}"),
    71	    ("T1-015", "Hermes #19", "prefix", "SendGrid API key",
    72	     r"SG\.[A-Za-z0-9_-]{10,}"),
    73	    ("T1-016", "Hermes #20", "prefix", "HuggingFace token",
    74	     r"hf_[A-Za-z0-9]{10,}"),
    75	    ("T1-017", "Hermes #21", "prefix", "Replicate API token",
    76	     r"r8_[A-Za-z0-9]{10,}"),
    77	    ("T1-018", "Hermes #22", "prefix", "npm access token",
    78	     r"npm_[A-Za-z0-9]{10,}"),
    79	    ("T1-019", "Hermes #23", "prefix", "PyPI API token",
    80	     r"pypi-[A-Za-z0-9_-]{10,}"),
    81	    ("T1-020", "Hermes #24", "prefix", "DigitalOcean PAT",
    82	     r"dop_v1_[A-Za-z0-9]{10,}"),
    83	    ("T1-021", "Hermes #25", "prefix", "DigitalOcean OAuth",
    84	     r"doo_v1_[A-Za-z0-9]{10,}"),
    85	    ("T1-022", "Hermes #26", "prefix", "AgentMail API key",
    86	     r"am_[A-Za-z0-9_-]{10,}"),
    87	    ("T1-023", "Hermes #27", "prefix", "ElevenLabs TTS key",
    88	     r"sk_[A-Za-z0-9_]{10,}"),
    89	    ("T1-024", "Hermes #28", "prefix", "Tavily search API",
    90	     r"tvly-[A-Za-z0-9]{10,}"),
    91	    ("T1-025", "Hermes #29", "prefix", "Exa search API",
    92	     r"exa_[A-Za-z0-9]{10,}"),
    93	    ("T1-026", "Hermes #30", "prefix", "Groq Cloud API key",
    94	     r"gsk_[A-Za-z0-9]{10,}"),
    95	    ("T1-027", "Hermes #31", "prefix", "Matrix access token",
    96	     r"syt_[A-Za-z0-9]{10,}"),
    97	    ("T1-028", "Hermes #32", "prefix", "RetainDB API key",
    98	     r"retaindb_[A-Za-z0-9]{10,}"),
    99	    ("T1-029", "Hermes #33", "prefix", "Hindsight API key",
   100	     r"hsk-[A-Za-z0-9]{10,}"),
   101	    ("T1-030", "Hermes #34", "prefix", "Mem0 Platform API key",
   102	     r"mem0_[A-Za-z0-9]{10,}"),
   103	    ("T1-031", "Hermes #35", "prefix", "ByteRover API key",
   104	     r"brv_[A-Za-z0-9]{10,}"),
   105	]
   106	
   107	# Tier-1 추가 regex 7 (H-A, H-B, H-C, H-E, H-F, H-G, H-K — H-J/H-L 제외, R-4.1 §4.2 답습)
   108	REGEX_PATTERNS: list[tuple[str, str, str, str, str]] = [
   109	    ("T1-032", "Hermes H-A", "regex", "ENV assignment",
   110	     r"([A-Z0-9_]{0,50}(?:API_?KEY|TOKEN|SECRET|PASSWORD|PASSWD|CREDENTIAL|AUTH)[A-Z0-9_]{0,50})\s*=\s*(['\"]?)(\S+)\2"),
   111	    ("T1-033", "Hermes H-B", "regex", "JSON field with secret keys",
   112	     r'(?i)("(?:api_?[Kk]ey|token|secret|password|access_token|refresh_token|auth_token|bearer|secret_value|raw_secret|secret_input|key_material)")\s*:\s*"([^"]+)"'),
   113	    ("T1-034", "Hermes H-C", "regex", "Authorization header (Bearer)",
   114	     r"(?i)(Authorization:\s*Bearer\s+)(\S+)"),
   115	    ("T1-035", "Hermes H-E", "regex", "Private key block",
   116	     r"-----BEGIN[A-Z ]*PRIVATE KEY-----[\s\S]*?-----END[A-Z ]*PRIVATE KEY-----"),
   117	    ("T1-036", "Hermes H-F", "regex", "DB connstr password",
   118	     r"(?i)((?:postgres(?:ql)?|mysql|mongodb(?:\+srv)?|redis|amqp)://[^:]+:)([^@]+)(@)"),
   119	    ("T1-037", "Hermes H-G", "regex", "JWT token",
   120	     r"eyJ[A-Za-z0-9_-]{10,}(?:\.[A-Za-z0-9_=-]{4,}){0,2}"),
   121	    ("T1-039", "Hermes H-K", "regex", "URL userinfo (non-DB)",
   122	     r"(https?|wss?|ftp)://([^/\s:@]+):([^/\s@]+)@"),
   123	]
   124	
   125	# Tier-1 alternation 2 (H-J / H-L sensitive key 기반 변환, R-4.1 §4.1 답습)
   126	ALTERNATION_PATTERNS: list[tuple[str, str, str, str, str]] = [
   127	    ("T1-041", "Hermes _SENSITIVE_QUERY_PARAMS", "alternation", "URL query sensitive keys (16)",
   128	     r"(?i)(?:^|[?&\s'\";#])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|session|secret|key|code|signature|x-amz-signature)=[^&\s]+"),
   129	    ("T1-042", "Hermes _SENSITIVE_BODY_KEYS", "alternation", "Body/form sensitive keys (14)",
   130	     r"(?i)(?:^|[?&\s'\";#])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|secret|private_key|authorization|key)=[^&\s]+"),
   131	]
   132	
   133	ALL_PATTERNS: list[tuple[str, str, str, str, str]] = (
   134	    BASELINE_PREFIX + PREFIX_PATTERNS + REGEX_PATTERNS + ALTERNATION_PATTERNS
   135	)
   136	"""All registered patterns — 5 baseline + 31 prefix + 7 regex + 2 alternation = 45 patterns."""
   137	
   138	# Compiled regex objects (모듈 import 시 1회 컴파일)
   139	COMPILED_PATTERNS: list[tuple[str, str, str, str, re.Pattern[str]]] = [
   140	    (pid, src, cat, vendor, re.compile(rgx))
   141	    for (pid, src, cat, vendor, rgx) in ALL_PATTERNS
   142	]
   143	
   144	# 본 PoC 직접 등록 제외 (R-4.1 §4.2 답습 — alternation 채택, H-J/H-L 직접 등록 false-positive 회피)
   145	SKIP_DIRECT_REGISTER: frozenset[str] = frozenset({"T1-038", "T1-040"})
   146	
   147	# ============================================================================
   148	# Redaction value group 메타 (B-2 group-aware 치환 — prevention 전용, detection 무관)
   149	#
   150	# pattern_id → secret *값* 의 capturing group index.
   151	#   0   = whole match 가 secret 값 (prefix/JWT/private key — key명 없음, 구조 손상 0)
   152	#   N>0 = 해당 capturing group 만 마스킹 (key명/구분자 보존)
   153	#   -1  = alternation (capturing group 없음) → 첫 '=' 뒤만 마스킹 (delimiter+key 보존)
   154	# 미등재 = 0 (whole) default.
   155	#
   156	# 본 매핑 = redaction 처리 메타이며 패턴 *내용* 이 아님 (equivalence test snapshot 무관).
   157	# ============================================================================
   158	REDACTION_VALUE_GROUP: dict[str, int] = {
   159	    "T1-032": 3,   # ENV assignment — group 3 = value
   160	    "T1-033": 2,   # JSON field — group 2 = value
   161	    "T1-034": 2,   # Authorization Bearer — group 2 = token
   162	    "T1-036": 2,   # DB connstr — group 2 = password (group 3 = '@' 보존)
   163	    "T1-039": 3,   # URL userinfo — group 3 = password
   164	    "T1-041": -1,  # alternation — '=' 뒤
   165	    "T1-042": -1,  # alternation — '=' 뒤
   166	    # 그 외 (prefix/baseline, T1-035 private key, T1-037 JWT) = 0 (whole) default
   167	}
   168	
   169	# Redaction marker (RedactionFilter 출력 + secret_scanner scan-log FP 회피 정합).
   170	REDACTION_MARK: str = "[REDACTED]"

exec
/bin/bash -lc "nl -ba tests/adapters/llm/test_redaction_filter.py | sed -n '1,220p'; nl -ba .importlinter; nl -ba requirements-dev.txt | sed -n '1,180p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	"""SC-1 (65 entry) RedactionFilter test — R-2 GP-2 prevention 송신 redaction.
     2	
     3	TDD RED→GREEN. 합의 `docs/review/3plus1-consensus-2026-05-28-mvp2-sc1.md` 답습:
     4	  - B-2 group-aware 치환 (값만 마스킹, key명/JSON 구조 보존)
     5	  - R-1 원본 불변성 / R-2 false positive edge case / R-4 spy redactor / B-1 equivalence
     6	"""
     7	from __future__ import annotations
     8	
     9	import pytest
    10	
    11	from src.adapters.llm.facade import LLMFacade, LLMRequest
    12	from src.adapters.llm.redaction import RedactionFilter
    13	from src.adapters.llm.redaction_patterns import ALL_PATTERNS, REDACTION_MARK
    14	
    15	
    16	@pytest.fixture
    17	def rf() -> RedactionFilter:
    18	    return RedactionFilter()
    19	
    20	
    21	# ── T-1: redact_text — secret 값 마스킹 (prefix = whole, key명 없음) ──────────
    22	def test_t1_redact_text_prefix_token(rf: RedactionFilter) -> None:
    23	    out = rf.redact_text("use sk-ant-ABCDEFGHIJ1234567890 now")
    24	    assert "sk-ant-ABCDEFGHIJ1234567890" not in out
    25	    assert REDACTION_MARK in out
    26	    assert "use" in out and "now" in out  # 주변 문맥 보존
    27	
    28	
    29	# ── T-2: redact_messages — content secret 값 redacted, key=구조 보존 ──────────
    30	def test_t2_redact_messages_env_assignment(rf: RedactionFilter) -> None:
    31	    msgs = [{"role": "user", "content": "config: API_KEY=sk-ant-SECRETVALUE123456 done"}]
    32	    out = rf.redact_messages(msgs)
    33	    content = out[0]["content"]
    34	    assert "sk-ant-SECRETVALUE123456" not in content
    35	    assert REDACTION_MARK in content
    36	    assert "API_KEY" in content  # key명 보존 (group-aware)
    37	    assert out[0]["role"] == "user"  # 구조 보존
    38	
    39	
    40	# ── T-3: Tier-1 45 catalog 대표 패턴 (baseline/prefix/regex/alternation) ──────
    41	@pytest.mark.parametrize(
    42	    "secret",
    43	    [
    44	        "ghp_ABCDEFGHIJ1234567890",  # BL-3 prefix-baseline
    45	        "gho_ABCDEFGHIJ1234567890",  # T1-002 prefix
    46	        'token: "sk_live_ABCDEFGHIJ1234"',  # T1-033 JSON regex (group)
    47	        "https://example.com/cb?access_token=eyJsecretvalue123",  # T1-041 alternation
    48	    ],
    49	)
    50	def test_t3_catalog_representative_patterns(rf: RedactionFilter, secret: str) -> None:
    51	    out = rf.redact_text(secret)
    52	    assert REDACTION_MARK in out
    53	    # secret 고유 값 (raw alphanum 시퀀스)이 평문 노출 0
    54	    for leak in ("ABCDEFGHIJ1234567890", "sk_live_ABCDEFGHIJ1234", "eyJsecretvalue123"):
    55	        if leak in secret:
    56	            assert leak not in out
    57	
    58	
    59	# ── T-4: false positive edge case — 정상 코드/텍스트 무변경 (R-2) ─────────────
    60	@pytest.mark.parametrize(
    61	    "benign",
    62	    [
    63	        "items.sort(key=lambda x: x.name)",  # paren delimiter — 매칭 0 (codex N-4)
    64	        "import keyboard",
    65	        "def f(monkeypatch): pass",
    66	        "url = '/search?page=1&limit=20'",  # sensitive key 아님
    67	        "the secret garden was lovely",  # 'secret' 단어 but =value 아님
    68	    ],
    69	)
    70	def test_t4_false_positive_benign_unchanged(rf: RedactionFilter, benign: str) -> None:
    71	    assert rf.redact_text(benign) == benign
    72	
    73	
    74	# ── T-5: scrub dict 재귀 + KEY_BLACKLIST + 구조 무결성 ────────────────────────
    75	def test_t5_scrub_dict_key_blacklist_and_structure(rf: RedactionFilter) -> None:
    76	    obj = {
    77	        "api_key": "sk-ant-DEEPSECRET1234567890",
    78	        "user": "alice",
    79	        "nested": {"token": "ghp_NESTEDSECRET12345", "count": 3},
    80	    }
    81	    out = rf.scrub(obj)
    82	    # KEY_BLACKLIST: api_key/token 값 마스킹
    83	    assert out["api_key"] == REDACTION_MARK
    84	    assert out["nested"]["token"] == REDACTION_MARK
    85	    # 구조 무결성: 비밀 아닌 key/값 보존
    86	    assert out["user"] == "alice"
    87	    assert out["nested"]["count"] == 3
    88	    assert set(out.keys()) == {"api_key", "user", "nested"}
    89	
    90	
    91	# ── T-6: facade complete() redaction 선행 (spy) + Router deferred ─────────────
    92	def test_t6_facade_redaction_before_router_deferred() -> None:
    93	    calls: list[str] = []
    94	
    95	    class SpyRedactor:
    96	        def redact_messages(self, messages):
    97	            calls.append("redact_messages")
    98	            return messages
    99	
   100	        def scrub(self, obj):
   101	            calls.append("scrub")
   102	            return obj
   103	
   104	    facade = LLMFacade(registry_path="dummy", redactor=SpyRedactor())
   105	    req = LLMRequest(alias="agent_a", messages=[{"role": "user", "content": "hi"}])
   106	    with pytest.raises(NotImplementedError):
   107	        facade.complete(req)
   108	    # redaction 이 Router deferred (NotImplementedError) *전* 호출됨
   109	    assert "redact_messages" in calls
   110	
   111	
   112	# ── T-7: 원본 불변성 — redact_messages in-place mutate 0 (R-1) ────────────────
   113	def test_t7_redact_messages_no_inplace_mutation(rf: RedactionFilter) -> None:
   114	    original = [{"role": "user", "content": "API_KEY=sk-ant-MUTATETEST1234567"}]
   115	    snapshot = "API_KEY=sk-ant-MUTATETEST1234567"
   116	    out = rf.redact_messages(original)
   117	    assert original[0]["content"] == snapshot  # 입력 불변
   118	    assert out is not original
   119	    assert out[0]["content"] != snapshot  # 출력은 redacted
   120	
   121	
   122	# ── T-8: equivalence — catalog single source 45 patterns (B-1) ────────────────
   123	def test_t8_catalog_equivalence_45_patterns() -> None:
   124	    assert len(ALL_PATTERNS) == 45
   125	    ids = [p[0] for p in ALL_PATTERNS]
   126	    assert len(set(ids)) == 45  # id 중복 0
   127	    assert ids[:5] == ["BL-1", "BL-2", "BL-3", "BL-4", "BL-5"]
     1	; G2 GP-5 2차 PoC — Provider Adapter Enforcement Layer 1 (T-2 import-linter)
     2	;
     3	; 답습 출처:
     4	;   - docs/architecture/llm-providers-design.md §9.3 (allow path / forbidden path 시제 의도)
     5	;   - docs/review/3plus1-consensus-2026-05-10-g2-gp5-poc2-depcruise-full.md §5.2
     6	;   - docs/phase0/g2-gp5-poc2-depcruise-rule-scope.md §2.1, §3.1
     7	;
     8	; 책무 분담:
     9	;   - 본 룰: 4종 (openai, anthropic, litellm, ollama) direct/from/transitive 차단
    10	;   - google.generativeai: 1차 AST scanner 단독 책무 (각주 1 — import-linter 제약 답습)
    11	;   - 동적 import (importlib, __import__): 1차 AST scanner 전담 (책무 분리)
    12	;   - 모델명 분기 (문자열): 1차 AST scanner 전담
    13	;   - URL/endpoint 하드코딩: 3차 별도 합의 영역 외
    14	;   - 의미적 lock-in: 라운드트립 검증 (P2-5) 영역 외
    15	;
    16	; 핵심 옵션 — include_external_packages = True:
    17	;   forbidden 모듈 미설치 환경에서도 정상 검출 (C-9 RA-9 사전 검증 PASS, 2026-05-10).
    18	
    19	[importlinter]
    20	root_packages =
    21	    src
    22	include_external_packages = True
    23	
    24	[importlinter:contract:no-direct-llm-sdk]
    25	name = No direct LLM SDK imports outside facade
    26	type = forbidden
    27	source_modules =
    28	    src
    29	forbidden_modules =
    30	    openai
    31	    anthropic
    32	    litellm
    33	    ollama
    34	ignore_imports =
    35	    src.adapters.llm.facade -> *
     1	# Dev-only dependencies (G2 GP-5 2차 PoC — TR-2 발화 답습)
     2	#
     3	# 답습 출처:
     4	#   - docs/review/3plus1-consensus-2026-05-10-g2-gp5-poc2-depcruise-full.md §5.4 TR-2
     5	#   - docs/phase0/g2-gp5-poc2-depcruise-rule-scope.md §8.1 T-2 (import-linter)
     6	#   - C-9 RA-9 사전 검증 PASS (2026-05-10)
     7	#
     8	# 본 manifest 는 dev-dep 만 등재. runtime application 의존성 0건.
     9	# pyproject.toml (PEP 621) 신설은 *별도 합의* 답습 (R-RF2 답습).
    10	
    11	# Provider Adapter Enforcement Layer 1 (Static graph)
    12	# C-9 검증 환경: import-linter 2.11 + grimp 3.14
    13	import-linter==2.11
    14	
    15	# Group C PoC — RFC 8785 JCS Primary 1 + Primary 2 cross-check
    16	# 답습 출처:
    17	#   - docs/review/3plus1-consensus-2026-05-10-g4-jcs-library-selection.md (Q1 풀 3+1 합의 17 조건)
    18	#   - docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md §3 (사용자 명시 결정 갱신 — pyjcs PyPI 미존재 → jcs 대체)
    19	# 양 라이브러리 모두 Apache-2.0 + 의존성 0 + RA-9 §B.2 11/11 sanity 동등성 PASS
    20	rfc8785==0.1.4
    21	jcs==0.2.1
    22	
    23	# Jarvis 오케스트레이터 MVP-0 트랙 A — 단위 테스트 (TDD)
    24	# 답습 출처:
    25	#   - docs/phase0/jarvis-orchestrator-mvp-design-brief.md (v4, MVP-0 트랙 A)
    26	#   - docs/review/3plus1-consensus-2026-05-22-jarvis-orchestrator-mvp-v4-reviewer.md (APPROVE)
    27	# runtime application 의존성 0건 유지 (test-only).
    28	pytest==9.0.3
    29	pytest-cov==7.1.0
    30	
    31	# PC-1-T3 mandatory enforcement (MVP-1 1.5차 보강 sub-cycle)
    32	# 답습 출처:
    33	#   - docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md
    34	#   - docs/review/3plus1-consensus-2026-05-27-mvp1-pc1-t3-mandatory-enforcement.md (Reviewer-only APPROVE)
    35	# `.pre-commit-config.yaml` framework hook 6 (T2 opt-in 발효 `3c0a1c1`) → T3 dev 환경 mandatory enforcement
    36	# bin/setup.sh 가 `pre-commit install` 자동 실행 (Layer 2 framework hook 활성화)
    37	pre-commit==4.0.1
    38	
    39	# S-3 detect-secrets 부분 통합 (MVP-1 1.5차 보강 sub-cycle)
    40	# 답습 출처:
    41	#   - docs/phase0/mvp1-s3-detect-secrets-partial-integration-brief.md
    42	#   - docs/review/3plus1-consensus-2026-05-27-mvp1-s3-detect-secrets-partial-integration.md (Reviewer-only APPROVE)
    43	# Tier-1 답습 plugin 5종 한정 (AWSKeyDetector / KeywordDetector / Base64HighEntropyString
    44	#   / HexHighEntropyString / PrivateKeyDetector) — Tier-2/3 확장 = R-MVP1-1.5-S3-1 풀 3+1 trigger
    45	# --baseline 영구 금지 (R-MVP1-1.5-S3-2 silenceable risk)
    46	# S-1 (tools/secret_scanner.py) 답습 유지 영구 의무 (R-MVP1-1.5-S3-3 Defense in depth)
    47	detect-secrets==1.5.0

exec
/bin/bash -lc "nl -ba docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md | sed -n '260,420p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
   260	
   261	---
   262	
   263	## §11 금지 사항
   264	
   265	§0.2 (10) 답습. 추가: streaming/OAuth/degraded/metrics/race **구현 0** (설계 명세 존속) / "full facade real"·"facade 완성"·"Provider Liquidity 완전 발효"·"런타임 검증 완료" 표현 0 / 실 API 호출·credential 사용 0 / 65 RedactionFilter 패턴 *내용* 변경 0 / 자동 후속 sub-cycle 진입 0.
   266	
   267	---
   268	
   269	## §12 Rollback Trigger
   270	
   271	| # | trigger | 대응 |
   272	|---|---------|----|
   273	| RT-1 | redaction이 Router 위임 *후*로 밀림 (미부착 window) | §3 — redacted body를 Router 인자로 전달 + T-A 동치 검증 |
   274	| RT-2 | litellm 미설치 → facade import 실패 → 테스트 전체 red | §4.1 lazy import + Router 주입 (hermetic, T-H) |
   275	| RT-3 | `LLMRequest.alias` rename breaking (실 caller 존재) | 실측: src caller 0, test 1건(`test_redaction_filter.py:105`) → rename 시 동시 갱신 (D2) |
   276	| RT-4 | manifest 핀/hash 과도 ceremony (비례성 위반) | §4.2 — 풀 3+1 비례성 균형 ([[feedback_proportionate_security_personal_tool]]) |
   277	| RT-5 | 설계 §17 deferred 항목을 "삭제"로 오판 → 설계 훼손 | §7 — "명세 존속 + 구현 deferred" 판정 명문 |
   278	| RT-6 | LiteLLM Router health API 실 형태 불명 → D8 구현 막힘 | §2 D8 — active 목록 + 설정검증 반환으로 축소 fallback |
   279	
   280	---
   281	
   282	## §13 Evidence
   283	
   284	- E-1: facade test green (T-A~T-I) + 커버리지 70%+ (특히 RT-1 T-A 동치 검증)
   285	- E-2: `validate_config` Min 2 + 동일 type fail-fast (T-C/T-D)
   286	- E-3: import-linter green (litellm = facade 한정, 경계 보존)
   287	- E-4: 65 RedactionFilter 15 test + jarvis pytest 회귀 0
   288	- E-5: `llm-providers.yaml` 로드 + routing 매핑 (T-G) + secret_scanner scan-source 0
   289	- E-6: 설계 v2 §17 체크리스트 판정표 (합의 보고서) → status flip 근거
   290	- E-7: (선택) 실 litellm 설치 + import smoke (네트워크 가용 시) — 실 호출은 deferred
   291	
   292	---
   293	
   294	## §14 자기진단 (메타 편향 회피)
   295	
   296	| # | 위험 | 처리 |
   297	|---|------|----|
   298	| P-1 | "full facade real / 완성" over-claim | §0 헤더 명칭 정직성 — core `complete()` 경로 한정, 5종 deferred ([[feedback_pass_scope_overclaim]]) |
   299	| P-2 | "실 LLM 호출 검증 완료" over-claim | mock만 — 실 end-to-end 미입증 명문 (§0 scope) |
   300	| P-3 | "Provider Liquidity 발효/완전" over-claim | 코드 경로 operative ≠ 5-way 완결 (ADR-009 §5 5 Layer 별개) |
   301	| P-4 | 설계 §17 deferred 항목을 삭제로 처리 | §7 — 명세 존속 + 구현 deferred |
   302	| P-5 | manifest/hash 과도 ceremony | §4.2 비례성 균형 (개인 툴) |
   303	| P-6 | 65 RedactionFilter 변경 유혹 | 협력자 재사용만, 패턴 내용 0 |
   304	| P-7 | RT-1 window 간과 | T-A Router 입력 = redacted 동치 (단순 호출 확인 아님) |
   305	| P-8 | 작성자 = Claude single-vendor cascade | cross-vendor codex + 풀 3+1 독립 검증 (세션 #3 cascade 6회 교훈) |
   306	
   307	---
   308	
   309	**본 brief v1 끝.**
   310	
   311	**다음 단계**: 사용자 승인 → 풀 3+1 + 외부 LLM 1+(codex) 4 source 병렬 launch (설계 §17 재합의 folding 포함) → Reviewer 통합 → brief v1.1 흡수 → TDD 구현(Router mock) → verify → commit + push. **자동 진입 0 — 사용자 명시 의무** ([[feedback_staged_consensus_workflow]]).

exec
/bin/bash -lc "nl -ba docs/review/3plus1-consensus-2026-05-04-p1-llm-providers.md | sed -n '1,260p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# 3+1 합의 보고서: P1 (LLM Provider 추상화 설계) 검증
     2	
     3	**날짜**: 2026-05-04
     4	**검증 대상**: `docs/architecture/llm-providers-design.md` (P1, 665줄)
     5	**상위 결정**: ADR-008 (Hermes 도입, Option B). 본 P1은 차단조건 #4·#5 충족 메커니즘
     6	**관련 합의**: `3plus1-consensus-2026-05-04-hermes.md` (Reviewer가 Agent C에 메타 가중치 부여한 선례)
     7	
     8	---
     9	
    10	## 사전 점검 — Provider Liquidity 위반 여부
    11	
    12	본 안건은 다중 provider 추상화 설계 자체이며, Liquidity 원칙(2개 이상 active provider 의무)을 약화시키지 않는다. Agent B의 "최소 2 active 회피 가능" 지적은 Liquidity **강화** 방향, Agent C의 LiteLLM 승격안 또한 multi-provider liquidity를 보존(Router의 fallback/cooldown으로 강화). **반려 사유 없음 — 합의 진행.**
    13	
    14	---
    15	
    16	## Phase 2 — 3 에이전트 독립 분석 요약
    17	
    18	### Agent A (구현 분석가) — APPROVE with revisions
    19	- Adapter 인터페이스: 4 provider 조건부 수용 (system/tool_use 왕복/multimodal/streaming chunk 타입 정규화 누락)
    20	- 폴백 race 5종: 헬스체크 전이, active=2 검증, rate-limit thundering herd, OAuth refresh, streaming 이중 출력
    21	- depcruise 회피 6종: importlib 동적, 전이 의존, 테스트 예외, monkey-patch, 모델명 분할/base64/alias, alias에 의미 부여
    22	- 추가 발견: §4.1 health(provider_key) 외부 노출 모순, MVP에 헬스체크 빠진 §6.3 시나리오 모순, Phase 1 시나리오 ollama 미포함(§6.2 위반)
    23	
    24	### Agent B (품질·안전성) — APPROVE with revisions
    25	- 위반 패턴 6종 평가: #2/#6만 정규화로 강제, 나머지 4종(#1/#3/#4/#5) 가이드/체크리스트(추론적). 차단조건 #4 미충족
    26	- OAuth 누출 위험: yaml 평문, 메트릭 redaction 미명시, health_check 인증 echo, mount 권한 강제 없음
    27	- "최소 2 active" 회피 경로: 시작 시 1회만 검증, 자동 강등 후 재검증 없음, standby가 폴백 체인엔 들어가나 active 카운트 빠짐, 동일 type 2개 등록 시 권장만
    28	- 추가 위험 7종 (R1~R7): 메트릭 PII, metadata raw dict 누출, yaml 비밀, stateless 위반, alias 무결성, health_check 인증 노출, OpenRouter 분기 폭증
    29	
    30	### Agent C (대안 탐색가) — APPROVE with revisions (LiteLLM 승격 권장)
    31	- 자체 Adapter 비용: ~600 LOC + 신규 type ~80~150 LOC + SDK 추적 ~16~32h/년 + 테스트 ~600 LOC, 연간 ~40~80h
    32	- LiteLLM 통합 비용: facade ~100 LOC + 학습 ~4~8h, 연간 ~5~10h
    33	- LiteLLM이 §3·§4·§5·§6·§9의 80% 자체 제공 — 위반 패턴 #1·#2·#5·#6 자연 차단
    34	- ADR-004 본질 위반: P1은 외형(config-driven)만 차용, 본질("외부 SDK 우선") 정면 모순
    35	
    36	---
    37	
    38	## Phase 3 — 교차 비교
    39	
    40	### 일치 (3자 동의)
    41	1. 결론 등급: 전원 APPROVE with revisions (근본 폐기 없음, revision 폭에 합의 없음)
    42	2. **Adapter 스키마 결손 만장일치** — A(system/tool_use/multimodal/streaming), B(metadata raw dict), C(정규화 부족)
    43	3. **차단조건 #4 자기충족 미흡 만장일치** — A(depcruise 회피 6종), B(P5 위임+추론적), C(LiteLLM facade 1줄로 단순화)
    44	4. **차단조건 #5 충족 미흡 만장일치** — 시작 시 1회 검증만으로 부족
    45	5. 자동 강등/폴백 시 운영 안정성 공백 만장일치 (degraded 모드 명세 필요)
    46	
    47	### 부분 일치
    48	- **자체 Adapter 채택 정당성**: A·B 채택 자체엔 이견 없음 vs C 반대 (ADR-004 본질 위반) → **메타 한계 가중치로 사용자 결정 옵션 격상** (Option α/β)
    49	- **메트릭/메타 PII·토큰 누출**: A·B 합의 (필수 보강), C 미언급 → 양 옵션 모두 redaction 의무화
    50	- **헬스체크 인증 노출**: A·B 합의, C 미언급 → 헬스체크 명세 본 문서 자기충족화 필수
    51	
    52	### 불일치 — 본 합의 최대 분기점
    53	**§14 "v2.0 LiteLLM 검토" 일정 적정성**:
    54	- A·B: 침묵 (암묵적 수용, 적극적 동의 아님)
    55	- C: v1.0(MVP)로 승격 — 매몰비용 누적 회피
    56	- **결정**: 정량 근거(LOC, 유지부담) 제시한 C 의견에 가중치. **사용자 결정 옵션으로 분기**
    57	
    58	### 누락 (단독 발견 → 합의안 포함)
    59	- [A CRITICAL] 폴백 race 5종 (특히 OAuth refresh = ADR-008 R1 재현 통로)
    60	- [A HIGH] §4.1 health(provider_key) 인자 모순
    61	- [A MEDIUM] stream 합 타입화 (AsyncIterator[StreamEvent])
    62	- [B HIGH] OAuth credentials 처리 명세 부재 (mount/env/echo)
    63	- [B HIGH] 동일 type 2개 active 금지를 권장→강제 격상
    64	- [B HIGH] LLMResponse.metadata raw dict 화이트리스트화
    65	- [B HIGH] §6.1 fail-fast vs 자동 강등 결합 시 정전 → degraded 모드
    66	- [C CRITICAL] ADR-004 본질 위반 (외형만 차용)
    67	- [C HIGH] 이전 Hermes 합의 Reviewer 보정 정신과 P1 모순
    68	
    69	---
    70	
    71	## Phase 4 — 최종 합의
    72	
    73	### 합의된 결론 (한 문장)
    74	**P1은 현재 상태로 승인 불가이며, ADR-008 차단조건 #4·#5 충족을 위해 상위 2개 옵션 중 사용자 결정 후 필수 12개 보강을 적용해야 한다.**
    75	
    76	### 사용자 결정 옵션
    77	
    78	#### Option α — 자체 Adapter 유지 + 강화 보강 (P1 현행 노선)
    79	- **의미**: 자체 Adapter 4개 v1.0에 그대로 작성. 차단조건 #4·#5는 정적 룰 + runtime sentinel + active 재검증으로 자력 충족
    80	- **비용**: ~600 LOC + 차단 테스트 ~600 LOC + 연간 ~40~80h 유지
    81	- **장점**: 외부 SDK 종속성 회피, 모든 동작 자가 통제
    82	- **단점**: ADR-004 본질 위반 가능성, 위반 패턴 차단을 100% 자력 구현
    83	- **추가 의무**: ADR-004 정합성 별도 ADR 작성
    84	
    85	#### Option β — LiteLLM facade 1차 채택 (Agent C 승격안) ⭐ Reviewer 권고
    86	- **의미**: §14 v2.0 LiteLLM을 v1.0(MVP)로 승격. §4 Adapter는 LiteLLM facade ~100 LOC. ADR-008 차단조건 #4 "어댑터 1개"는 LiteLLM facade가 충족. 자체 Adapter는 v2.0 백업
    87	- **비용**: facade ~100 LOC + facade 보강 ~150 LOC + 테스트 ~200 LOC, 연간 ~5~10h
    88	- **장점**: 위반 패턴 #1·#2·#5·#6이 LiteLLM 정규화로 자연 차단, ADR-004 정신 보존, 연간 유지부담 1/3~1/5, P1 LOC 62% 감축
    89	- **단점**: latency +20~80ms (proxy 모드만), LiteLLM 신규 provider 지원 종속성
    90	- **추가 의무**: v2.0 자체 Adapter 진입조건 ADR 작성
    91	
    92	#### Reviewer 권고
    93	**메타 한계 보정 + Hermes 합의 일관성 + ADR-004 정합성 3중 가중치 적용 시 Option β 권장.** 단, Option α도 "ADR-004 정합성 ADR + 12개 보강 완전 이행" 조건부 유효.
    94	
    95	---
    96	
    97	### Revision 항목 통합
    98	
    99	#### 옵션 무관 — 양쪽 모두 필수 (12개)
   100	
   101	| # | 항목 | 우선순위 | 출처 |
   102	|---|------|---------|------|
   103	| R1 | LLMRequest 스키마 보강 (system/response_format/tool_choice/stop_sequences/stream) | CRITICAL | A |
   104	| R2 | LLMResponse.metadata raw dict 금지 → 화이트리스트 구조화 | CRITICAL | B |
   105	| R3 | 메트릭/예외/응답 redaction 필터 의무화 (PII·토큰) | CRITICAL | A,B |
   106	| R4 | 런타임 active≥2 재검증 (모든 강등 경로 + degraded 모드) | CRITICAL | A,B |
   107	| R5 | 동일 type 2개 active 금지를 권장→강제 | HIGH | B |
   108	| R6 | OAuth refresh single-flight 잠금 (R1 재현 차단) | CRITICAL | A |
   109	| R7 | OAuth credentials 처리 명세 (env/mount :ro+0600/echo 금지) | HIGH | B |
   110	| R8 | 폴백 race 5종 완화 (immutable snapshot/semaphore+지터/first-token 후 폴백 금지) | HIGH | A |
   111	| R9 | health_check dry probe + MVP 포함 일치화 | HIGH | A,B |
   112	| R10 | §4.1 health(provider_key) 모순 해소 | HIGH | A |
   113	| R11 | stream 반환 타입 AsyncIterator[StreamEvent] | MEDIUM | A |
   114	| R12 | tool_use·tool_result 정규화 명세 또는 명시 비지원 | HIGH | A |
   115	
   116	#### Option α 추가 (5개)
   117	| # | 항목 | 우선순위 |
   118	|---|------|---------|
   119	| Aα-1 | depcruise allowlist + httpx 직접 호출 차단 | CRITICAL |
   120	| Aα-2 | AST 동적 import 차단 룰 | CRITICAL |
   121	| Aα-3 | runtime sentinel (provider 모듈 wrapping 검증) | HIGH |
   122	| Aα-4 | routing alias 네이밍 컨벤션 + 의미 부여 금지 | HIGH |
   123	| Aα-5 | ADR-004 정합성 ADR 작성 | CRITICAL |
   124	
   125	#### Option β 추가 (4개)
   126	| # | 항목 | 우선순위 |
   127	|---|------|---------|
   128	| Bβ-1 | §4 Adapter를 LiteLLM facade로 재정의, §14 LiteLLM v1.0 승격 | CRITICAL |
   129	| Bβ-2 | depcruise 룰 단순화 (litellm 외 LLM SDK 직접 import 금지) | HIGH |
   130	| Bβ-3 | LiteLLM 자체 redaction 검증 + 부족분 facade 보강 | HIGH |
   131	| Bβ-4 | v2.0 자체 Adapter 진입조건 ADR 작성 | HIGH |
   132	
   133	---
   134	
   135	### 미해결 결정 (사용자 입력 필요)
   136	1. Option α vs β 선택 (본 합의 핵심)
   137	2. Option β 채택 시 LiteLLM SDK 모드 vs Proxy 모드 (SDK 권장)
   138	3. Option α 채택 시 ADR-004 정합성 ADR 작성 시점 (선결 vs 동시)
   139	4. R3 redaction의 화이트리스트/블랙리스트 방식 (화이트리스트 권장)
   140	5. R4 degraded 모드 사용자 노출 방식 (UI/로그/메트릭 — P3와 연계)
   141	
   142	---
   143	
   144	### 위험 알림
   145	
   146	#### CRITICAL
   147	- C-1: P1 채택은 ADR-004 사실상 무력화 (헌법 위계). ADR-004 정합성 ADR 없이 Option α 진행 위험
   148	- C-2: OAuth refresh race는 ADR-008 R1 재현 통로. R6 누락 시 재발 가능
   149	- C-3: 메트릭 PII + metadata 누출은 헌법 제8조 위반 직접 통로 (R2·R3 누락 시)
   150	- C-4: 시작 시 1회 검증만으로는 차단조건 #5 충족 불가 (자동 강등 후 1 active 전락 가능)
   151	
   152	#### HIGH
   153	- H-1: Option α 시 위반 패턴 #1·#3·#4가 추론적 검증 의존 — 헌법 제3조 위반 (Aα-1~3로 격상 필수)
   154	- H-2: 메타 한계 — 3 Claude 에이전트 → 자체 Adapter 친화 편향 가능. Reviewer는 C에 가중치 부여
   155	- H-3: Phase 1 시나리오 ollama 미포함으로 §6.2 type 다양성 위반 — P1 본문 정정 필수
   156	
   157	---
   158	
   159	## LiteLLM 승격(Option β) 채택 시 P1 재작성 가이드
   160	
   161	11개 섹션별 변경 사항:
   162	1. §3 Provider 정의: 유지 + LiteLLM model prefix 매핑
   163	2. §4 Adapter: 전면 재작성 (LiteLLMAdapter ~100 LOC)
   164	3. §5 Fallback: LiteLLM Router 위임
   165	4. §6 Liquidity: 유지 + R5+R4 추가
   166	5. §7 Health: dry probe + Router cooldown 통합
   167	6. §8 메트릭: LiteLLM callback + R3 redaction
   168	7. §9 OAuth: facade 격리 + R6+R7
   169	8. §13 ADR-004 정합성: 재작성 ("본질 따름")
   170	9. §14 v2.0 로드맵: "자체 Adapter 진입조건"으로 변경
   171	10. §16 차단 검증: LiteLLM 자연 차단 활용
   172	11. §4.1 health 모순: Router health 활용
   173	
   174	**LOC 영향**: 자체 Adapter ~1200 → LiteLLM facade ~450 (62% 감축)

exec
/bin/bash -lc 'rg -n "full|완성|완전|런타임 검증|실 LLM|실 호출|mock" docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
7:> - **검증 범위 = Router mock만**: `litellm.Router`를 주입 가능한 fake로 대체하여 위임 경로·redaction 선부착·정규화·Min2 검증을 hermetic하게 테스트. **실 LLM 호출(credential/네트워크 필요) = 수동/별도 trigger** (CI 안정성 우선).
10:> ⚠️ **명칭 정직성 (over-claim 차단 — 본 세션 #3 cascade 2회 + 세션 #2 4회 교훈 답습, [[feedback_pass_scope_overclaim]])**: 본 cycle = **facade Router 위임 real (core `complete()` 경로)** — **"full facade real" / "facade 완성" / "Provider Liquidity 완전 발효" 표현 영구 금지**. deferred = streaming/OAuth/degraded/metrics/폴백 race. **실 LLM 호출 = mock 검증** (실 end-to-end 미입증 → "런타임 검증 완료" 표현 금지). 67 entry "GP-2 full → prevention" 강등 선례 동형 주의.
14:> **본 cycle 발효 효과** = facade `complete()` core 경로 operative (config 기반 provider/model 교체가 *코드 경로상* 실동작 — 5조-2 비협상 실동작 기반) + 설계 v2 §17 재합의 통과 시 "확정" 승격. **단 실 호출 검증 = mock 한정** (실 end-to-end = 수동/별도).
30:7. **TDD 계획 (Router mock, RED→GREEN→REFACTOR)** (§8)
42:| 6 | **실 LLM 호출 end-to-end 검증** (credential/네트워크) | 0 (mock만, 수동/별도) |
44:| 8 | **full GP-2 PASS 재선언 / R-1 canary / R-6 Hermes trigger** | 0 |
130:- 실 설치 시도(`pip install litellm==<pin>`): 네트워크 가용 시 수행(실 호출 수동 검증 대비), **실패해도 mock 테스트 무영향**(주입). 본 cycle CI 통과 = mock 기준.
210:## §8 TDD 계획 (Router mock — RED → GREEN → REFACTOR)
265:§0.2 (10) 답습. 추가: streaming/OAuth/degraded/metrics/race **구현 0** (설계 명세 존속) / "full facade real"·"facade 완성"·"Provider Liquidity 완전 발효"·"런타임 검증 완료" 표현 0 / 실 API 호출·credential 사용 0 / 65 RedactionFilter 패턴 *내용* 변경 0 / 자동 후속 sub-cycle 진입 0.
290:- E-7: (선택) 실 litellm 설치 + import smoke (네트워크 가용 시) — 실 호출은 deferred
298:| P-1 | "full facade real / 완성" over-claim | §0 헤더 명칭 정직성 — core `complete()` 경로 한정, 5종 deferred ([[feedback_pass_scope_overclaim]]) |
299:| P-2 | "실 LLM 호출 검증 완료" over-claim | mock만 — 실 end-to-end 미입증 명문 (§0 scope) |
300:| P-3 | "Provider Liquidity 발효/완전" over-claim | 코드 경로 operative ≠ 5-way 완결 (ADR-009 §5 5 Layer 별개) |
311:**다음 단계**: 사용자 승인 → 풀 3+1 + 외부 LLM 1+(codex) 4 source 병렬 launch (설계 §17 재합의 folding 포함) → Reviewer 통합 → brief v1.1 흡수 → TDD 구현(Router mock) → verify → commit + push. **자동 진입 0 — 사용자 명시 의무** ([[feedback_staged_consensus_workflow]]).

codex
code 대조 결과 현재 facade는 말씀대로 redaction 후 `NotImplementedError`이고, `LLMRequest(alias=...)` 테스트 영향도 실제로 존재합니다. 마지막으로 호출자/manifest 상태를 빠르게 확인해 D1/D2의 실측 근거가 맞는지 확인하겠습니다.
exec
/bin/bash -lc "rg -n \"\\.complete\\(|LLMRequest\\(\" src tests --glob '*.py'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
tests/adapters/llm/test_redaction_filter.py:105:    req = LLMRequest(alias="agent_a", messages=[{"role": "user", "content": "hi"}])
tests/adapters/llm/test_redaction_filter.py:107:        facade.complete(req)

exec
/bin/bash -lc "rg --files -g 'pyproject.toml' -g 'requirements*.txt' -g '*lock*' -g 'llm-providers.yaml' -g '*.yaml' -g '*.yml' | sort" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
.pre-commit-config.yaml
docker/gp3-st2-poc/docker-compose.gp3-st2.yml
docker/gp3-st3-poc/docker-compose.gp3-st3.yml
docker/r2-poc/docker-compose.r2-poc.yml
docker/r4-1-poc/docker-compose.r4-1-poc.yml
docs/phase0/group-i-4axis-blocking-integration-brief.md
docs/phase0/phase-alpha-3-r7-docker-secret-block-entry-brief.md
docs/phase0/v1-poc-raw/phase3/2026-05-24T04-32-phase3-measure-attempt-blocked.log
docs/review/3plus1-consensus-2026-05-14-phase-alpha-3-r7-docker-secret-block-entry.md
docs/review/3plus1-consensus-2026-05-21-group-i-4axis-blocking-integration.md
requirements-dev.txt
tests/fixtures/boundary_guard/skill_escalation/fail/skill_yaml_invalid_action.yaml
tests/fixtures/boundary_guard/skill_escalation/pass/valid_skill_within_allowed.yaml
tests/fixtures/mvp1_pc3_ar1_integration/fail/ar1_violation_no_fail_closed.yml
tests/fixtures/mvp1_pc3_ar1_integration/fail/pc3_violation_continue_on_error.yml
tests/fixtures/mvp1_pc3_ar1_integration/pass/compliant_entry_step.yml
tests/fixtures/provider_url_scanner/model_name/pass/safe_model_config.yaml
tests/fixtures/provider_url_scanner/mvp1_entry/url_endpoint/pass/safe_endpoint_config.yaml
tests/fixtures/provider_url_scanner/url_endpoint/pass/safe_config.yaml
tests/fixtures/schema_validation/skill_schema/fail/invalid_action.yaml
tests/fixtures/schema_validation/skill_schema/fail/invalid_promotion_status.yaml
tests/fixtures/schema_validation/skill_schema/fail/missing_required.yaml
tests/fixtures/schema_validation/skill_schema/fail/provider_lockin.yaml
tests/fixtures/schema_validation/skill_schema/pass/valid_skill.yaml
tests/fixtures/secret_hygiene/fail/private_key_block.pem
tests/fixtures/stage5_g3_7/fork_pr_policy/fail/pull_request_target_trigger.yml
tests/fixtures/stage5_g3_7/fork_pr_policy/fail/workflow_run_trigger.yml
tests/fixtures/stage5_g3_7/fork_pr_policy/pass/clean_workflow.yml
tests/fixtures/stage5_g3_7/permissions/fail/contents_write_too_broad.yml
tests/fixtures/stage5_g3_7/permissions/fail/no_permissions_block.yml
tests/fixtures/stage5_g3_7/permissions/pass/contents_read_top_level.yml
tests/fixtures/stage5_g3_7/secrets_reference/fail/secrets_in_env_with_run_if.yml
tests/fixtures/stage5_g3_7/secrets_reference/pass/clean_workflow.yml
tests/fixtures/stage5_g3_7/secrets_usage/fail/secrets_block_header.yml
tests/fixtures/stage5_g3_7/secrets_usage/fail/secrets_interpolation_in_env.yml
tests/fixtures/stage5_g3_7/secrets_usage/pass/clean_workflow.yml

exec
/bin/bash -lc "rg -n \"health\\(|stream\\(|metadata_in|model_alias|LLMMetadata|DomainMetricsCallback|SingleFlightLock|degraded|fallback\" docs/architecture/llm-providers-design.md docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
docs/architecture/llm-providers-design.md:153:  openrouter-fallback:
docs/architecture/llm-providers-design.md:208:    model_alias: str                     # 라우팅 alias (예: "consensus_agent_a")
docs/architecture/llm-providers-design.md:217:    metadata_in: dict | None = None             # 호출 메타 (요청 ID 등 — redaction 대상)
docs/architecture/llm-providers-design.md:220:class LLMMetadata:
docs/architecture/llm-providers-design.md:223:    fallback_chain: list[str]            # 시도된 provider 순서
docs/architecture/llm-providers-design.md:232:    metadata: LLMMetadata                # 구조화된 메타 (raw dict 아님)
docs/architecture/llm-providers-design.md:262:        self._oauth_lock = SingleFlightLock(...) # R6 보강
docs/architecture/llm-providers-design.md:265:        provider_key = self._resolve(req.model_alias)
docs/architecture/llm-providers-design.md:273:            await self._on_active_degraded(provider_key)  # R4 재검증
docs/architecture/llm-providers-design.md:277:    async def stream(self, req: LLMRequest) -> AsyncIterator[StreamEvent]:
docs/architecture/llm-providers-design.md:281:    async def health(self) -> dict[str, bool]:   # ← R10 보강 (provider_key 인자 제거)
docs/architecture/llm-providers-design.md:294:| `finish_reason` | LiteLLM 통일 — `LLMMetadata.finish_reason`로 격리 |
docs/architecture/llm-providers-design.md:295:| **provider 고유 메타** | **버림** — `LLMMetadata` 화이트리스트 외 키는 통과 못 함 (raw dict 누출 차단) |
docs/architecture/llm-providers-design.md:317:      model_alias="consensus_agent_a",
docs/architecture/llm-providers-design.md:322:  1. routing[model_alias] → provider_key
docs/architecture/llm-providers-design.md:324:  3. LiteLLM Router에 위임 (model_id 매핑, fallback chain 적용)
docs/architecture/llm-providers-design.md:325:  4. 응답 정규화: LiteLLM 표준 → LLMResponse + LLMMetadata 화이트리스트
docs/architecture/llm-providers-design.md:353:            "fallbacks": build_fallbacks(providers_yaml),
docs/architecture/llm-providers-design.md:363:LiteLLM Router의 fallback에 추가 보강:
docs/architecture/llm-providers-design.md:376:명시: llm.complete(LLMRequest(model_alias="consensus_agent_b", ...))
docs/architecture/llm-providers-design.md:380:`model_alias`는 의미 없는 명칭만 허용. provider/모델명을 alias에 인코딩 금지(예: `claude_only_path` 같은 alias는 lint 룰로 차단 — 위반 패턴 #1 회피 차단).
docs/architecture/llm-providers-design.md:402:**모든 강등 경로**에서 active 카운트를 재계산하고 부족하면 degraded 모드로 전환:
docs/architecture/llm-providers-design.md:405:async def _on_active_degraded(self, provider_key: str):
docs/architecture/llm-providers-design.md:411:        await self._enter_degraded_mode(reason=f"active={active_count} (need ≥2)")
docs/architecture/llm-providers-design.md:419:  2. 새 호출은 처리 가능한 alias만 수용 (degraded provider 의존 alias는 503)
docs/architecture/llm-providers-design.md:422:  4. 강등 provider 복구 시 자동 active 복귀 + degraded 모드 해제
docs/architecture/llm-providers-design.md:423:  5. degraded 모드 30분 지속 시 운영자 호출 (escalation)
docs/architecture/llm-providers-design.md:460:class SingleFlightLock:
docs/architecture/llm-providers-design.md:495:litellm.success_callback = [DomainMetricsCallback(redactor=...)]
docs/architecture/llm-providers-design.md:496:litellm.failure_callback = [DomainMetricsCallback(redactor=...)]
docs/architecture/llm-providers-design.md:498:class DomainMetricsCallback:
docs/architecture/llm-providers-design.md:504:            "model_alias": self._reverse_alias(event.model),
docs/architecture/llm-providers-design.md:506:            "fallback_chain": event.fallback_chain,
docs/architecture/llm-providers-design.md:546:- fallback 발생 빈도
docs/architecture/llm-providers-design.md:566:| 4 | 메모리에 provider별 메타 저장 | LiteLLM이 raw 메타 통일 | `LLMMetadata` 화이트리스트(R2) |
docs/architecture/llm-providers-design.md:576:async def health(self) -> dict[str, bool]:
docs/architecture/llm-providers-design.md:670:  자동: LiteLLM Router fallback → openrouter-fallback 또는 ollama-llama-local 도달
docs/architecture/llm-providers-design.md:737:| **#5 최소 2 provider always-on** | **§6.1 시작 시 fail-fast + §6.2 런타임 재검증 + §6.3 degraded 모드** |
docs/architecture/llm-providers-design.md:801:- [ ] §4.1 health(provider_key) 모순 해소 — §4.1, §9.2
docs/architecture/llm-providers-design.md:811:- [ ] 런타임 active 재검증 + degraded 모드 — §6.2, §6.3
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:6:> - **구현 범위 = Core MVP**: `complete()` LiteLLM Router 실배선 + `validate_config`(Min 2 active + 동일 type 금지) + `llm-providers.yaml` registry + LiteLLM 설치·핀 + 응답 정규화(`LLMResponse`/`LLMMetadata` 화이트리스트) + RT-1(redaction 선부착). **DEFER**: streaming(`StreamEvent`) / OAuth single-flight(§7.2) / degraded 모드·R4 런타임 재검증(§6.2/6.3) / `DomainMetricsCallback`(§8.1) / 폴백 race 완화(§5.2).
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:10:> ⚠️ **명칭 정직성 (over-claim 차단 — 본 세션 #3 cascade 2회 + 세션 #2 4회 교훈 답습, [[feedback_pass_scope_overclaim]])**: 본 cycle = **facade Router 위임 real (core `complete()` 경로)** — **"full facade real" / "facade 완성" / "Provider Liquidity 완전 발효" 표현 영구 금지**. deferred = streaming/OAuth/degraded/metrics/폴백 race. **실 LLM 호출 = mock 검증** (실 end-to-end 미입증 → "런타임 검증 완료" 표현 금지). 67 entry "GP-2 full → prevention" 강등 선례 동형 주의.
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:28:5. **Router 위임 + 응답 정규화(LLMMetadata 화이트리스트)** (§6)
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:37:| 1 | **streaming** (`stream()` / `StreamEvent` 합 타입, §4.1) | 0 (deferred) |
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:38:| 2 | **OAuth single-flight lock** (§7.2 `SingleFlightLock`) | 0 (deferred — 본 cycle은 api_key 경로만) |
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:39:| 3 | **degraded 모드 + R4 런타임 재검증** (§6.2/§6.3 `_on_active_degraded`) | 0 (deferred — 시작 시 fail-fast만) |
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:40:| 4 | **`DomainMetricsCallback`** (§8.1 — redaction 적용 메트릭 sink) | 0 (deferred) |
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:41:| 5 | **폴백 race 5종 완화** (§5.2 — semaphore/jitter/snapshot) | 0 (deferred — LiteLLM Router 기본 fallback만) |
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:50:- **`llm-providers-design.md`** §3.1(registry yaml) / §3.3·§6.1(validate_config: Min 2 + 동일 type fail-fast) / §4.1(facade 인터페이스) / §4.2(정규화 — LiteLLM OpenAI 포맷 통일 + LLMMetadata 화이트리스트) / §4.3(에러 분류 — litellm 표준 예외) / §5.1(`to_router_config`) / §9.2(dry probe health) / §17(재합의 체크리스트)
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:76:### D2. `LLMRequest` 필드 정합 (alias → model_alias + core 필드)
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:78:- 현 SC-1: `LLMRequest(alias, messages, metadata)`. 설계 §4.1: `LLMRequest(messages, model_alias, system, temperature, max_tokens, tools, tool_choice, response_format, stop_sequences, stream, metadata_in)`.
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:79:- **권고 = core 비-stream 필드 정합**: `model_alias`(rename) + `messages` + `system` + `temperature`(default 0.7) + `max_tokens`(default 4096) + `tools` + `metadata`. **`stream` 관련 필드 deferred**(§0.2 #1). `tool_choice`/`response_format`/`stop_sequences` = trivial passthrough이므로 포함 가능(검증).
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:82:### D3. `LLMResponse` 정규화 + `LLMMetadata` 화이트리스트 (§4.2 / 위반패턴 #2·#4)
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:84:- 현 SC-1: `LLMResponse(content, metadata: dict[str,Any])`. 설계 §4.1/§4.2: `LLMResponse(content, usage: dict, metadata: LLMMetadata)` — `LLMMetadata`(frozen 화이트리스트: provider_used / fallback_chain / finish_reason / request_id).
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:85:- **권고 = LLMMetadata 화이트리스트 도입** (raw provider 메타 누출 통로 차단 — 위반 패턴 #2/#4 + Liquidity 보존). LiteLLM이 OpenAI 포맷 통일 → `raw["choices"][0]["message"]["content"]` 추출 + usage 표준 필드 + finish_reason 격리.
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:95:- 시작 시 fail-fast: active provider ≥ 2 (ADR-008 #5) + active 중 동일 `type` 2개 금지 (정전 동시 실패 회피, R5). degraded 런타임 재검증(§6.2)은 deferred — **시작 시 검증만**.
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:104:- `litellm.AuthenticationError`/`RateLimitError`/`ServiceUnavailableError`/`BadRequestError`만 인지. **Core MVP**: AuthenticationError → 즉시 re-raise(degraded 전환 `_on_active_degraded` deferred). Router 자체 fallback/num_retries는 Router 설정에 위임.
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:106:### D8. `health()` — dry probe (§9.2)
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:159:- standby/blocked/deprecated status 스키마 포함(전이는 Core MVP에서 routing 제외/포함만, degraded deferred).
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:171:- 시작 시 1회(`__init__`). **런타임 재검증(R4)은 deferred** — degraded 모드 미구현 명시.
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:179:- `llm-providers.yaml` → LiteLLM Router `model_list`(model_name=alias, litellm_params.model=litellm_model, api_key 환경변수) + `router_settings`(fallbacks, num_retries, timeout). cooldown/고급 튜닝 = v1.1 deferred.
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:184:1. provider_key = routing[req.model_alias]   (없으면 routing.default)
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:187:4. return self._normalize(raw, provider_key)   (LLMResponse + LLMMetadata 화이트리스트)
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:188:   except litellm.AuthenticationError: raise   (degraded 전환 deferred)
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:193:- `content = raw.choices[0].message.content` / `usage = {input_tokens, output_tokens, cost_estimate?}` / `LLMMetadata(provider_used, fallback_chain, finish_reason, request_id)`. **raw dict 통과 0** (화이트리스트 외 키 버림).
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:202:- **Agent B 항목**: LLMMetadata 화이트리스트 / redaction 의무(65 충족) / OAuth credentials(deferred but 스키마) / single-flight(deferred) / 동일 type 금지 / R4 재검증(deferred) / dry probe
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:206:⚠️ **deferred 항목(streaming/OAuth/degraded/race)은 "설계 명세 존속 + 구현 deferred"로 판정** — 설계에서 삭제 아님. 설계 §15 로드맵 v1.0 "12 보강 모두" 문구 ↔ Core MVP 분할 사이 정합성 = Reviewer 판단 대상(설계 §15 갱신 필요 여부).
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:215:- **T-B**: `complete()` 정상 경로 → fake Router 응답 → `LLMResponse(content, usage, LLMMetadata)` 정규화 (raw dict 누출 0).
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:218:- **T-E (D7)**: fake Router가 `AuthenticationError` raise → `complete()` re-raise (degraded 전환 0 — Core MVP).
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:219:- **T-F (D2/D3)**: `LLMRequest(model_alias=...)` 필드 + `LLMMetadata` frozen 화이트리스트 (raw 키 거부).
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:226:- `facade.py`: lazy litellm import + Router 주입 + `complete()` async 배선 + `validate_config` + `to_router_config` + `_normalize` + `LLMRequest`/`LLMResponse`/`LLMMetadata` 정합.
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:258:- `LLMMetadata` 화이트리스트 = raw provider 메타 누출 0 (위반 패턴 #2/#4).
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:265:§0.2 (10) 답습. 추가: streaming/OAuth/degraded/metrics/race **구현 0** (설계 명세 존속) / "full facade real"·"facade 완성"·"Provider Liquidity 완전 발효"·"런타임 검증 완료" 표현 0 / 실 API 호출·credential 사용 0 / 65 RedactionFilter 패턴 *내용* 변경 0 / 자동 후속 sub-cycle 진입 0.
docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:278:| RT-6 | LiteLLM Router health API 실 형태 불명 → D8 구현 막힘 | §2 D8 — active 목록 + 설정검증 반환으로 축소 fallback |

exec
/bin/bash -lc "nl -ba docs/architecture/llm-providers-design.md | sed -n '760,860p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
   760	| **ADR-006** (환경 변수 + Docker) | API 키 환경 변수, OAuth credentials env 보간(R7) + Docker mount :ro |
   761	| **ADR-005** (AI 백엔드 스택) | Python 분리 기준 따름 |
   762	| **ADR-008** (Hermes 도입) | 차단조건 #4·#5 충족 메커니즘 |
   763	| **ADR-009** (자체 Adapter v2.0 진입조건) | 본 문서 §15 v2.0 로드맵의 정량 트리거 |
   764	| **PROJECT_CONSTITUTION 제8조** | redaction 의무화(R3), 비밀값 echo 금지 테스트(R7) |
   765	| **harness-engineering-design** | Layer 1.5 정적 검사 + Layer 5 신규 provider 합의 |
   766	
   767	---
   768	
   769	## 15. Phase 로드맵
   770	
   771	| Phase | 내용 | 상태 | 진입 조건 |
   772	|-------|------|------|----------|
   773	| **MVP (v1.0)** | LiteLLM facade + `llm-providers.yaml` + Min 2 fail-fast + 동일 type 강제 + redaction + dry probe + 12 보강 모두 | **구현 대상** | 본 설계 재합의 통과 |
   774	| **v1.1** | LiteLLM Router 고급 기능 (cooldown 튜닝, custom retry strategy) + 의사결정 대시보드 | 필요 입증 후 | MVP 운영 1~2주 + 폴백/한도 이벤트 발생 |
   775	| **v1.2** | 자동 모델 추천 (성능/비용 학습 기반) + multi-modal 통합 | 필요 입증 후 | 사용 데이터 축적 |
   776	| **v2.0** | 자체 Adapter 작성 (LiteLLM 폐기) | **ADR-009 진입조건 충족 시에만** | LiteLLM이 신규 provider X를 N분기 내 미지원 + PR 거부 등 |
   777	
   778	> ADR-009에 v2.0 진입조건의 **정량 트리거**가 명세되어 있다. LiteLLM 사용은 v1.0~1.2까지의 기본 노선이며, v2.0으로의 전환은 명시 트리거 없이 발생하지 않는다.
   779	
   780	---
   781	
   782	## 16. Phase 2 검토 사항 (현재 미구현)
   783	
   784	| 항목 | 도입 조건 |
   785	|------|----------|
   786	| 추론 캐시 레이어 | 동일 요청 반복 비율 ≥ 20% |
   787	| Provider별 prompt 최적화 | 모델 간 결과 품질 편차 측정 후 |
   788	| Streaming 응답 표준화 보강 | streaming 사용 사례 발생 시 |
   789	| Multi-modal (이미지/오디오) 통합 | 별도 도메인 (ADR-003·004 참조) |
   790	
   791	---
   792	
   793	## 17. 검증 항목 (재합의용)
   794	
   795	본 v2 설계가 3+1 합의 12 보강 + 4 β-추가를 모두 반영했는지 재합의 시 검증:
   796	
   797	### Agent A (구현)
   798	- [ ] LLMRequest 신규 필드 5종 (system, response_format, tool_choice, stop_sequences, stream) — §4.1
   799	- [ ] AsyncIterator[StreamEvent] 합 타입 — §4.1
   800	- [ ] tool_use 정규화 (LiteLLM 위임 명시) — §4.2
   801	- [ ] §4.1 health(provider_key) 모순 해소 — §4.1, §9.2
   802	- [ ] 폴백 race 5종 완화 — §5.2
   803	- [ ] Phase 1 시나리오 ollama 포함 — §11.1
   804	
   805	### Agent B (안전)
   806	- [ ] LLMResponse.metadata 화이트리스트화 — §4.1, §4.2
   807	- [ ] Redaction 필터 의무화 (응답·예외·메트릭) — §8.2
   808	- [ ] OAuth credentials 처리 명세 — §7.3
   809	- [ ] OAuth refresh single-flight — §7.2
   810	- [ ] 동일 type 2개 active 금지 강제 — §3.3, §6.1
   811	- [ ] 런타임 active 재검증 + degraded 모드 — §6.2, §6.3
   812	- [ ] Health dry probe — §9.2
   813	
   814	### Agent C (대안)
   815	- [ ] LiteLLM facade 승격 — §1.2, §4
   816	- [ ] depcruise 단순화 — §9.3
   817	- [ ] LiteLLM redaction + facade 보강 통합 — §8.1, §8.2
   818	- [ ] ADR-009 진입조건 ADR 작성 (별도 파일)
   819	
   820	### Reviewer
   821	- [ ] ADR-004 본질 일치 — §13
   822	- [ ] ADR-008 차단조건 #4·#5 충족 — §12
   823	- [ ] Hermes 합의 일관성 (Option β로 외부 SDK 우선 정신 유지) — §1.3
   824	
   825	---
   826	
   827	**이 문서는 3+1 에이전트 재합의를 통과해야 확정됩니다.**

exec
/bin/bash -lc 'rg -n "## 15|## 17|재합의|v1.0|12" docs/architecture/llm-providers-design.md' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
6:**상태**: 초안 v2 (Option β: LiteLLM facade 승격 + 12 보강 + 4 β-추가 적용. 재합의 대기)
123:      - "ADR-008 R4: #15080, #6475, #12905, #10575"
296:| `tool_use` 왕복 (R12) | OpenAI tool_calls 표준 사용. Anthropic tool_use는 LiteLLM이 자동 변환 |
729:## 12. ADR-008 차단조건 매핑
769:## 15. Phase 로드맵
773:| **MVP (v1.0)** | LiteLLM facade + `llm-providers.yaml` + Min 2 fail-fast + 동일 type 강제 + redaction + dry probe + 12 보강 모두 | **구현 대상** | 본 설계 재합의 통과 |
778:> ADR-009에 v2.0 진입조건의 **정량 트리거**가 명세되어 있다. LiteLLM 사용은 v1.0~1.2까지의 기본 노선이며, v2.0으로의 전환은 명시 트리거 없이 발생하지 않는다.
793:## 17. 검증 항목 (재합의용)
795:본 v2 설계가 3+1 합의 12 보강 + 4 β-추가를 모두 반영했는지 재합의 시 검증:
822:- [ ] ADR-008 차단조건 #4·#5 충족 — §12
827:**이 문서는 3+1 에이전트 재합의를 통과해야 확정됩니다.**

codex
1. **판정**: APPROVE WITH CONDITIONS

Core 방향은 타당하지만, 구현 진입 전 2건은 brief v1.1에 반영해야 합니다.

2. **BLOCKING 항목**

1. **RT-1 redaction 범위가 `messages` 중심으로 좁다.**
   설계의 `LLMRequest`는 `messages`, `model_alias`, `system`, `tools`, `tool_choice`, `response_format`, `stop_sequences`, `metadata_in`까지 포함합니다: [llm-providers-design.md](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/llm-providers-design.md:205). 그런데 brief의 Router 위임 경로는 `messages=redacted["messages"]`만 명시합니다: [brief](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:116). T-A도 secret 포함 `messages`만 검증합니다: [brief](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:214).  
   Core MVP가 `system`/tools passthrough를 포함한다면, 모든 outbound request field가 Router 전달 전 redaction 대상이어야 합니다. 아니면 이번 MVP에서 해당 field passthrough를 제외한다고 명시해야 합니다.

2. **Router 호출 model 값이 registry mapping과 모순된다.**
   설계 §5.1은 LiteLLM Router `model_list[].model_name = alias`, 실제 provider model은 `litellm_params.model`에 둡니다: [llm-providers-design.md](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/llm-providers-design.md:339). brief도 `model_list(model_name=alias, litellm_params.model=litellm_model)`라고 씁니다: [brief](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:179). 그런데 `complete()` 흐름은 `model=litellm_model`을 Router에 넘긴다고 되어 있습니다: [brief](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:186).  
   Router 위임 경로는 Router의 configured `model_name`을 호출해야 fallback/routing이 살아납니다. `litellm_model`은 YAML 내부/provider adapter 내부 mapping으로만 남겨야 합니다.

3. **설계 v2 status flip 조건이 아직 과감하다.**
   설계 §15는 MVP(v1.0)를 “dry probe + 12 보강 모두”로 정의합니다: [llm-providers-design.md](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/llm-providers-design.md:773). §17 체크리스트도 streaming, fallback race, OAuth single-flight, 런타임 재검증/degraded를 포함합니다: [llm-providers-design.md](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/llm-providers-design.md:797). brief는 해당 항목을 deferred로 두고도 통과 시 “확정 v2” flip을 말합니다: [brief](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:199).  
   조건: `확정 v2`가 “전체 v1.0 구현 완료”가 아니라 “staged implementation을 허용하는 설계 확정”임을 §15/§17에 명시하거나, status를 `확정 v2 / Core MVP 구현분리 승인`처럼 제한해야 합니다.

3. **권고 항목**

1. D2는 `metadata`가 아니라 설계명 `metadata_in`으로 맞추는 편이 낫습니다. 설계는 `metadata_in`을 redaction 대상으로 명시합니다: [llm-providers-design.md](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/llm-providers-design.md:217).

2. `health()`는 Core MVP에서 실제 LiteLLM dry API 형태가 불명확하면 brief의 축소 fallback대로 “active alias + config validation result”로 제한하십시오. 설계의 dry probe는 명시되어 있지만 구현 API 형태는 문서 내부 근거만으로 확정하기 어렵습니다: [llm-providers-design.md](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/llm-providers-design.md:570).

3. runtime dependency는 `requirements.txt` + exact pin + hashes가 현재 repo 상태에 가장 비례적입니다. 현재 `requirements-dev.txt`는 dev-only이며 runtime dep 0과 pyproject 별도 합의를 명시합니다: [requirements-dev.txt](/home/delangi/문서/project/category/AI_development_tool/requirements-dev.txt:8). P11은 hash와 lock diff를 요구하되 Implementation Pending이라고도 합니다: [governance-preconditions.md](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/governance-preconditions.md:249), [governance-preconditions.md](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/governance-preconditions.md:280).

4. **NOTE**

- over-claim 방지는 양호합니다. “full facade real”, “Provider Liquidity 완전 발효”, “런타임 검증 완료” 금지를 반복 명시했고 mock-only도 분명합니다: [brief](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:10), [brief](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:265).
- 현 코드 상태 인용은 정확합니다. `complete()`는 redaction 후 `NotImplementedError`입니다: [facade.py](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:53). `LLMRequest(alias=...)` 테스트 1건도 확인됩니다: [test_redaction_filter.py](/home/delangi/문서/project/category/AI_development_tool/tests/adapters/llm/test_redaction_filter.py:105).
- `.importlinter`의 `litellm` facade 외 금지와 facade 예외도 실제와 일치합니다: [.importlinter](/home/delangi/문서/project/category/AI_development_tool/.importlinter:24).

5. **명칭 독립 판단**

“SC-Provider Liquidity — facade Router 위임 real (core `complete()` 경로)”는 적절합니다. 더 보수적으로는 다음이 가장 정직합니다:

**SC-Provider Liquidity — facade `complete()` Router delegation Core MVP (mock-verified)**

6. **권위 인용 cross-verify 매트릭스**

| brief 인용 | 실제 문서 대조 | 판정 |
|---|---:|---|
| P1 v2 상태 “재합의 대기” | 설계 header line 6, footer line 827 | 일치 |
| registry yaml §3.1 | 설계 line 84~160 | 일치 |
| facade async interface / LLMRequest / LLMMetadata | 설계 line 205~283 | 대체로 일치, `metadata` vs `metadata_in` 차이 |
| Router mapping `model_list` | 설계 line 339~358 | 일치하나 brief `complete()` model 값과 모순 |
| Min 2 + 동일 type 금지 | 설계 line 171~188, 386~398 | 일치 |
| deferred degraded/R4 | 설계 line 400~424 | 일치하나 status flip 조건 주의 |
| DomainMetricsCallback deferred | 설계 line 490~516 | 일치 |
| ADR-009 MVP 조건 + 6 의무 | ADR-009 line 51~75 | 일치 |
| ADR-009 Hermes/provider 분리 | ADR-009 line 77~90 | 일치 |
| ADR-008 #3/#4/#5 | ADR-008 line 17~23 | 일치 |
| P11 supply-chain hash/lock diff | governance line 249, 259~260, 268~280 | 일치하나 P11은 Implementation Pending/권장 성격 포함 |
| P1 합의 “현재 상태 승인 불가 + 12 보강” | consensus line 73~115 | 일치 |
tokens used
95,066
1. **판정**: APPROVE WITH CONDITIONS

Core 방향은 타당하지만, 구현 진입 전 2건은 brief v1.1에 반영해야 합니다.

2. **BLOCKING 항목**

1. **RT-1 redaction 범위가 `messages` 중심으로 좁다.**
   설계의 `LLMRequest`는 `messages`, `model_alias`, `system`, `tools`, `tool_choice`, `response_format`, `stop_sequences`, `metadata_in`까지 포함합니다: [llm-providers-design.md](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/llm-providers-design.md:205). 그런데 brief의 Router 위임 경로는 `messages=redacted["messages"]`만 명시합니다: [brief](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:116). T-A도 secret 포함 `messages`만 검증합니다: [brief](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:214).  
   Core MVP가 `system`/tools passthrough를 포함한다면, 모든 outbound request field가 Router 전달 전 redaction 대상이어야 합니다. 아니면 이번 MVP에서 해당 field passthrough를 제외한다고 명시해야 합니다.

2. **Router 호출 model 값이 registry mapping과 모순된다.**
   설계 §5.1은 LiteLLM Router `model_list[].model_name = alias`, 실제 provider model은 `litellm_params.model`에 둡니다: [llm-providers-design.md](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/llm-providers-design.md:339). brief도 `model_list(model_name=alias, litellm_params.model=litellm_model)`라고 씁니다: [brief](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:179). 그런데 `complete()` 흐름은 `model=litellm_model`을 Router에 넘긴다고 되어 있습니다: [brief](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:186).  
   Router 위임 경로는 Router의 configured `model_name`을 호출해야 fallback/routing이 살아납니다. `litellm_model`은 YAML 내부/provider adapter 내부 mapping으로만 남겨야 합니다.

3. **설계 v2 status flip 조건이 아직 과감하다.**
   설계 §15는 MVP(v1.0)를 “dry probe + 12 보강 모두”로 정의합니다: [llm-providers-design.md](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/llm-providers-design.md:773). §17 체크리스트도 streaming, fallback race, OAuth single-flight, 런타임 재검증/degraded를 포함합니다: [llm-providers-design.md](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/llm-providers-design.md:797). brief는 해당 항목을 deferred로 두고도 통과 시 “확정 v2” flip을 말합니다: [brief](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:199).  
   조건: `확정 v2`가 “전체 v1.0 구현 완료”가 아니라 “staged implementation을 허용하는 설계 확정”임을 §15/§17에 명시하거나, status를 `확정 v2 / Core MVP 구현분리 승인`처럼 제한해야 합니다.

3. **권고 항목**

1. D2는 `metadata`가 아니라 설계명 `metadata_in`으로 맞추는 편이 낫습니다. 설계는 `metadata_in`을 redaction 대상으로 명시합니다: [llm-providers-design.md](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/llm-providers-design.md:217).

2. `health()`는 Core MVP에서 실제 LiteLLM dry API 형태가 불명확하면 brief의 축소 fallback대로 “active alias + config validation result”로 제한하십시오. 설계의 dry probe는 명시되어 있지만 구현 API 형태는 문서 내부 근거만으로 확정하기 어렵습니다: [llm-providers-design.md](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/llm-providers-design.md:570).

3. runtime dependency는 `requirements.txt` + exact pin + hashes가 현재 repo 상태에 가장 비례적입니다. 현재 `requirements-dev.txt`는 dev-only이며 runtime dep 0과 pyproject 별도 합의를 명시합니다: [requirements-dev.txt](/home/delangi/문서/project/category/AI_development_tool/requirements-dev.txt:8). P11은 hash와 lock diff를 요구하되 Implementation Pending이라고도 합니다: [governance-preconditions.md](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/governance-preconditions.md:249), [governance-preconditions.md](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/governance-preconditions.md:280).

4. **NOTE**

- over-claim 방지는 양호합니다. “full facade real”, “Provider Liquidity 완전 발효”, “런타임 검증 완료” 금지를 반복 명시했고 mock-only도 분명합니다: [brief](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:10), [brief](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md:265).
- 현 코드 상태 인용은 정확합니다. `complete()`는 redaction 후 `NotImplementedError`입니다: [facade.py](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:53). `LLMRequest(alias=...)` 테스트 1건도 확인됩니다: [test_redaction_filter.py](/home/delangi/문서/project/category/AI_development_tool/tests/adapters/llm/test_redaction_filter.py:105).
- `.importlinter`의 `litellm` facade 외 금지와 facade 예외도 실제와 일치합니다: [.importlinter](/home/delangi/문서/project/category/AI_development_tool/.importlinter:24).

5. **명칭 독립 판단**

“SC-Provider Liquidity — facade Router 위임 real (core `complete()` 경로)”는 적절합니다. 더 보수적으로는 다음이 가장 정직합니다:

**SC-Provider Liquidity — facade `complete()` Router delegation Core MVP (mock-verified)**

6. **권위 인용 cross-verify 매트릭스**

| brief 인용 | 실제 문서 대조 | 판정 |
|---|---:|---|
| P1 v2 상태 “재합의 대기” | 설계 header line 6, footer line 827 | 일치 |
| registry yaml §3.1 | 설계 line 84~160 | 일치 |
| facade async interface / LLMRequest / LLMMetadata | 설계 line 205~283 | 대체로 일치, `metadata` vs `metadata_in` 차이 |
| Router mapping `model_list` | 설계 line 339~358 | 일치하나 brief `complete()` model 값과 모순 |
| Min 2 + 동일 type 금지 | 설계 line 171~188, 386~398 | 일치 |
| deferred degraded/R4 | 설계 line 400~424 | 일치하나 status flip 조건 주의 |
| DomainMetricsCallback deferred | 설계 line 490~516 | 일치 |
| ADR-009 MVP 조건 + 6 의무 | ADR-009 line 51~75 | 일치 |
| ADR-009 Hermes/provider 분리 | ADR-009 line 77~90 | 일치 |
| ADR-008 #3/#4/#5 | ADR-008 line 17~23 | 일치 |
| P11 supply-chain hash/lock diff | governance line 249, 259~260, 268~280 | 일치하나 P11은 Implementation Pending/권장 성격 포함 |
| P1 합의 “현재 상태 승인 불가 + 12 보강” | consensus line 73~115 | 일치 |
