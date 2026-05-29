OpenAI Codex v0.128.0 (research preview)
--------
workdir: /home/delangi/문서/project/category/AI_development_tool
model: gpt-5.5
provider: openai
approval: never
sandbox: danger-full-access
reasoning effort: none
reasoning summaries: none
session id: 019e6dc1-01a8-77a3-b40d-b74612b52c8c
--------
user
당신은 외부 LLM 검토자 (cross-vendor blind review)입니다. 응답 vendor = OpenAI (codex CLI), 본 cycle 풀 3+1 Agent vendor = Anthropic Claude. cross-vendor 충족 (헌법 5조-2).

## 본 cycle 개요

AI_development_tool 프로젝트 (SDD + TDD + 하네스 엔지니어링 + 3+1 합의). 본 cycle = **SC-1 facade RedactionFilter (R-2 GP-2 prevention) 실 구현 brief** (65 entry, TR-1 풀 3+1 합의 trigger 발화). 직전 64 entry에서 full GP-2 PASS trajectory 진입 합의 발효 → carry-over 1순위 SC-1 진입. 사용자 scope 명시 = "RedactionFilter 집중".

본 cycle 발효 효과:
- RedactionFilter 완전 구현 (secret_scanner Tier-1 45 catalog 재사용 R-2-c) + facade complete() 송신 전 redaction 통합
- GP-2 Exit (a) "facade redaction filter 검증" R-2 prong 충족 (R-1 = SC-2 별도)

본 cycle = 구현 *전* 설계 승인 (SDD "문서 검토 후 코드 구현"). 합의 APPROVE 후 TDD 구현.

본 cycle 발효 *하지 않는 것*: LiteLLM 설치 0 / Router 위임 구현 0 (deferred = Provider Liquidity 별도 sub-cycle) / full facade real 0 (Min2+registry+에러분류+정규화 deferred) / full GP-2 PASS 발효 0 (SC-2 R-1 + SC-3 후) / secret_scanner 패턴 변경 0 (R-4.1 "변경 0건" 답습) / Tier-2/3 확장 0 / 자동 후속 0.

⚠️ 명칭 정직성 핵심: 본 cycle = "facade *redaction layer* real" — **full facade real 아님**. 본 프로젝트 세션 #2에서 over-claim cascade 4회 포착됨.

## 검토 대상 (working directory 자료, codex 직접 read 의무 — 추측 금지)

PRIMARY (본 검토 핵심):
- `docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md` (v1, §0~§11) ← 본 검토 핵심

권위/설계 source (정확성 cross-verify + 구현 타당성 검증 — 직접 read):
- `docs/architecture/llm-providers-design.md` §4.1 (facade complete() 설계, line 192~284) + §8.2 (RedactionFilter 설계, line 518~538) + §4.4 (호출 흐름)
- `docs/architecture/governance-preconditions.md` §4.1 (line 422 "LLM API request body에 secret 노출 차단" 송신 경로) + §4.5 (a)
- `docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md` §2.2 (facade 단일 진입점 의무)
- `src/adapters/llm/facade.py` (현 placeholder, 41 LOC — 통합 대상)
- `tools/secret_scanner.py` (Tier-1 45 catalog = ALL_PATTERNS/COMPILED_PATTERNS/scan_text, 외부 의존성 0 stdlib — R-2-c 재사용 대상)
- `.importlinter` (root=src, forbidden=LLM SDK facade 예외 — src↔tools 경계 결정 입력)

## 검토 관점 (외부 cross-vendor 독립)

1. **catalog 재사용 설계 결정 (§2.1, 핵심)**: 4 옵션 (i) src→tools import / (ii) 공유 모듈 추출 / (iii) 복제 / (iv) §8.2 자체. brief 권고 = (i) 우선 + (ii) fallback. **(i) src(런타임)→tools(개발도구) 역방향 의존이 아키텍처적으로 타당한가?** import-linter root=src 밖이라 미차단이나 nonidiomatic. (ii) secret_scanner 변경 = R-4.1 "변경 0건" 위반 trade-off. 당신의 독립 권고는?
2. **송신 redaction 역할 정합 (§3)**: §8.2 RedactionFilter는 scrub (응답/메트릭 redaction)인데, brief는 redact_messages (송신 request body)를 GP-2 prevention 핵심으로 명세. governance §4.1 송신 경로와 정합하는가? 정상 대화 내용 손상 risk (false positive)?
3. **RT-1 window 회피 (§4.2)**: Router deferred = 송신 0 = window 없음 + 선부착 보장 논리가 타당한가?
4. **명칭 정직성**: "facade redaction layer real" vs "full facade real" 구분이 명확한가? over-claim 있는가?
5. **TDD 계획 (§5)**: RED T-1~T-6 + GREEN + REFACTOR 타당성. 누락 test?
6. **Provider Liquidity 보존 (§7)**: Router deferred이므로 litellm import 0 → import-linter 보존. RedactionFilter provider-agnostic 정합?
7. **누락/risk**: brief가 놓친 위험, 의존성, 대안?

## 응답 형식 (필수)

1. **판정**: APPROVE / APPROVE WITH CONDITIONS / REVISE 중 하나 (명확히)
2. **BLOCKING 항목** (있으면): 구현 전 반드시 정정 — 번호 + 근거 (직접 read한 line 인용)
3. **권고 항목**: 번호 + 내용
4. **NOTE**: 참고/관찰
5. **catalog 재사용 (i)/(ii) 독립 권고**: 당신의 추천 + 근거
6. **권위/설계 인용 cross-verify 결과**: brief 인용 vs 실제 문서 일치/모순 매트릭스

한국어로 응답하되 기술 용어는 영어 원문 유지. 직접 파일을 read하여 검증하고, 추측이 아닌 구체적 line 인용 기반으로 응답하세요.

codex
요청하신 외부 검토 범위에 맞춰 관련 문서와 구현 파일을 직접 읽겠습니다. 먼저 primary brief와 권위 문서의 지정 구간, 현재 facade와 scanner/import-linter 상태를 확인합니다.
exec
/bin/bash -lc "nl -ba docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md | sed -n '1,260p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# SC-1 facade RedactionFilter (R-2 GP-2 prevention) 실 구현 brief (v1)
     2	
     3	> **작성**: 2026-05-28 (65번째 entry 진입 cycle — 세션 #3)
     4	>
     5	> **scope** (사용자 명시 "RedactionFilter 집중"): **RedactionFilter 완전 구현 (secret_scanner Tier-1 45 catalog 재사용, R-2-c) + facade `complete()` 송신 전 redaction 적용 layer 통합**. **LiteLLM Router 위임 = deferred (Provider Liquidity 별도 sub-cycle)**. TDD 적용.
     6	>
     7	> ⚠️ **명칭 정직성 (over-claim 차단, 본 세션 #2 4회 cascade 교훈 답습)**: 본 cycle = **facade redaction layer real (R-2 GP-2 prevention)** — **full facade real 아님** (LiteLLM Router 위임 + Min 2 검증 + registry yaml = deferred). "facade real 완성" 표현 금지.
     8	>
     9	> **본 cycle = 큰 cycle (실 코드 + TR-1)** — facade.py 헤더 명시 "real 본문 작성 시 자동 풀 3+1 합의 trigger TR-1 발화". 64 entry SC-1 = 풀 3+1 (TR-1) + 실 코드.
    10	>
    11	> **본 cycle 발효 효과** = R-2 facade RedactionFilter prevention layer **in-repo operative** + GP-2 (a) "facade redaction filter 검증" 충족 (full GP-2 PASS Exit (a)의 R-2 prong). **full GP-2 PASS 발효 = SC-2 (R-1 위임 검증) + SC-3 후 (별도)**.
    12	>
    13	> **선행 답습**: 64 trajectory entry brief (SC-1 정의 + R-2-a 동시 + R-2-c catalog 재사용 + RedactionFilter = facade 내부 협력자 + RT-1 atomic) + llm-providers-design §4.1/§8.2 (설계 명세) + ADR-009 §2.2 (facade 단일 진입점 의무) + secret_scanner Tier-1 45 catalog
    14	
    15	---
    16	
    17	## §0 본 brief 의 범위
    18	
    19	### §0.1 본 brief 가 *하는* 것
    20	
    21	1. **RedactionFilter 인터페이스 + catalog 재사용 (R-2-c) 설계 결정** (§2)
    22	2. **송신 redaction 역할 명세** (GP-2 prevention = request body secret strip, §3)
    23	3. **facade 통합 지점 + Router deferred 처리** (RT-1 window 회피, §4)
    24	4. **TDD 계획** (RED → GREEN → REFACTOR, §5)
    25	5. **합의 형태 + 승격 트리거** (§6)
    26	6. **Provider Liquidity 보존 + 금지 + Rollback Trigger + Evidence + 자기진단** (§7~§11)
    27	
    28	### §0.2 본 brief 가 *하지 않는* 것
    29	
    30	| # | 영역 | 위반 |
    31	|---|------|----|
    32	| 1 | **LiteLLM 설치 + Router 위임 구현** (Provider Liquidity 별도 sub-cycle, deferred) | 0 |
    33	| 2 | **full facade real** (Min 2 검증 + registry yaml + 에러분류 + 정규화 + OAuth lock + callback) | 0 |
    34	| 3 | **full GP-2 PASS 발효** (SC-2 R-1 위임 검증 + SC-3 후) | 0 |
    35	| 4 | **R-1 Hermes 위임 검증** (SC-2 별도 sub-cycle) | 0 |
    36	| 5 | secret_scanner Tier-1 45 catalog **패턴 내용 변경** (R-4.1 답습 "변경 0건", R-7(b) 차등) | 0 |
    37	| 6 | Tier-2/3 catalog 확장 / base64 evasion (R-5 영구 분리) | 0 |
    38	| 7 | detection-layer PASS (60) / MVP-2 PASS (62) 재선언 | 0 |
    39	| 8 | ADR / 헌법 / governance / llm-providers-design 본문 변경 | 0 |
    40	| 9 | llm-providers.yaml registry 작성 (Min 2 검증 의존, Router deferred와 함께) | 0 |
    41	| 10 | 자동 후속 sub-cycle (SC-2/SC-3) 진입 | 0 (사용자 명시 의무) |
    42	
    43	### §0.3 권위 답습 source
    44	
    45	- **llm-providers-design.md §8.2** (RedactionFilter 설계 — PATTERNS 4 + KEY_BLACKLIST 6, 블랙리스트 채택) + **§4.1** (facade `complete()` 흐름) + **§4.4** (호출 흐름 — redaction 적용 지점 step 5)
    46	- **governance-preconditions.md §4.1** (line 422 — "LLM API request body 에 secret 노출 차단" 송신 경로) + **§4.5 (a)** (facade redaction filter 검증)
    47	- **ADR-009 §2.2** (facade 단일 진입점 의무 — LiteLLM 직접 import = facade.py 한정, provider SDK 직접 import 금지)
    48	- **secret_scanner.py** (Tier-1 45 catalog = baseline 5 + prefix 31 + regex 7 + alternation 2, `ALL_PATTERNS`/`COMPILED_PATTERNS`/`scan_text()`, 외부 의존성 0 stdlib)
    49	- **.importlinter** (root=src, forbidden=LLM SDK facade 예외 — src↔tools 경계 결정 입력)
    50	- **64 trajectory entry brief §4.4** (R-2-a/c 권고 + RedactionFilter = facade 내부 협력자 + RT-1 atomic)
    51	- **redaction-pattern-equivalence.md** (R-4 — Tier-1 catalog 설계 동등성, Hermes 안전성 선언 금지 §7.3)
    52	
    53	---
    54	
    55	## §1 진입 컨텍스트
    56	
    57	- 64 entry trajectory 진입 합의 (APPROVE WITH CONDITIONS 4 source) → carry-over 1순위 SC-1 진입 (사용자 명시).
    58	- GP-2 현 상태: detection-layer PASS (60, R-3 secret-hygiene D-2 CI operative). prevention (R-1/R-2) deferred.
    59	- 본 cycle = **R-2 prevention prong** (facade redaction filter) in-repo 구현 → GP-2 Exit (a)의 R-2 검증 충족 (R-1 = SC-2 별도).
    60	
    61	---
    62	
    63	## §2 RedactionFilter 인터페이스 + catalog 재사용 (R-2-c) 설계 결정
    64	
    65	### §2.1 catalog 재사용 방식 (핵심 설계 결정 — 풀 3+1 검증 대상)
    66	
    67	secret_scanner Tier-1 45 catalog 재사용 (R-2-c, single source detection↔prevention) — import 경계 4 옵션:
    68	
    69	| 옵션 | 방식 | 장점 | 단점 |
    70	|------|----|----|----|
    71	| (i) src → tools.secret_scanner import | RedactionFilter가 `tools.secret_scanner.COMPILED_PATTERNS` import | 즉시 single source, 변경 0 | **src(런타임) → tools(개발도구) 역방향 의존** (아키텍처 부적절, .importlinter root=src 밖이라 미차단이나 nonidiomatic) |
    72	| (ii) ⭐ catalog 공유 모듈 추출 | Tier-1 catalog를 `src/adapters/llm/redaction_patterns.py` (또는 공유 위치) 추출, secret_scanner + RedactionFilter 공유 | single source + 런타임 정합 | **secret_scanner 변경 = R-4.1 "변경 0건" 위반 = R-7(b) 차등 자격** (별도 평가) |
    73	| (iii) RedactionFilter 자체 복제 | Tier-1 45 패턴 복사 | 경계 깔끔 | **중복 → detection↔prevention drift 위험** (single source 위반) |
    74	| (iv) §8.2 자체 패턴 | RedactionFilter = §8.2 4 패턴 + 6 키 | 설계 명세 직접 답습 | Tier-1 45 catalog 미사용 (R-2-c 비채택, 커버리지 ↓) |
    75	
    76	⭐ **권고 = (i) tools import (잠정) 또는 (ii) 공유 모듈 추출** — **풀 3+1 결정 대상**. (i) = 변경 0건 충실하나 의존 방향 / (ii) = 정합하나 secret_scanner 변경 R-7(b). **본 brief 권고 = (i) 우선** (변경 최소 + R-4.1 "변경 0건" 보존), (ii)는 의존 방향 BLOCKING 시 fallback.
    77	
    78	### §2.2 RedactionFilter 인터페이스 (§8.2 답습)
    79	
    80	```
    81	class RedactionFilter:
    82	    """LLM 송신/응답/로그에서 비밀값 자동 strip (GP-2 prevention)."""
    83	    def redact_text(self, text: str) -> str: ...          # str 패턴 매칭 → [REDACTED]
    84	    def redact_messages(self, messages: list[dict]) -> list[dict]: ...  # 송신 request body redaction (GP-2 핵심)
    85	    def scrub(self, obj) -> ...: ...                       # dict/str 재귀 (응답/메트릭/로그, §8.2)
    86	```
    87	
    88	- 패턴 source = secret_scanner Tier-1 45 catalog (R-2-c, §2.1 결정 후).
    89	- `[REDACTED]` 치환 (secret_scanner `is_redaction_marker_match` 답습 — redaction marker 정합).
    90	- **frozen / 순수 함수** (Layer 1 자가진화 패턴 답습, 부작용 0).
    91	
    92	---
    93	
    94	## §3 송신 redaction 역할 명세 (GP-2 prevention)
    95	
    96	⭐ **핵심 = 송신 경로 (request body) redaction** (governance §4.1 line 422 verbatim "LLM API request body 에 secret 노출 차단"):
    97	- `complete(req)` 흐름에서 **Router 위임 *전*** `req.messages` (+ `system`)을 `redact_messages()` 통과 → secret strip 후 송신.
    98	- §4.4 호출 흐름 step 5 "메트릭 기록 (redaction 적용)" = 응답/로그 redaction (`scrub`).
    99	- **GP-2 prevention 핵심 = 송신 (request body)**. 응답/로그 redaction = 보조 (§8.2 scrub).
   100	
   101	⚠️ **redaction 의미 명확화**: GP-2 = "secret이 *실수로* LLM request body에 포함되는 것 차단" (예: 메시지에 API key 평문 노출). 정상 대화 내용 손상 아님 — Tier-1 catalog는 secret 패턴 (sk-/Bearer/api_key 등) 한정 매칭.
   102	
   103	---
   104	
   105	## §4 facade 통합 지점 + Router deferred (RT-1 window 회피)
   106	
   107	### §4.1 통합 설계 (현 placeholder → redaction layer real)
   108	
   109	현 `facade.py` (41 LOC placeholder):
   110	- `LLMFacade.__init__(registry_path)` → RedactionFilter 인스턴스 추가 (`self._redactor = RedactionFilter(...)`)
   111	- `complete(req)` → **redaction 적용 후 Router deferred**:
   112	  1. `redacted = self._redactor.redact_messages(req.messages)` (송신 전 redaction — GP-2 prevention operative)
   113	  2. Router 위임 = **deferred** → `raise NotImplementedError("LiteLLM Router 위임 = Provider Liquidity sub-cycle deferred")` (redaction *후* 명시적 deferred)
   114	
   115	### §4.2 RT-1 window 회피
   116	
   117	- 64 brief RT-1 = "facade real 후 RedactionFilter 미부착 window 금지 (atomic)".
   118	- 본 cycle: **Router deferred = 실제 LLM 송신 0 = redaction 미부착 window 없음** (송신 자체가 deferred). RedactionFilter는 complete() 진입 시 부착 → Router 발효 (SC-Provider Liquidity) 시점에 이미 redaction layer 존재 (선부착).
   119	- ⭐ **선부착 보장**: SC-Provider Liquidity (Router 위임)가 본 SC-1 (redaction layer) *후* 진입 → Router 발효 시 redaction 이미 operative (window 0).
   120	
   121	### §4.3 시그니처 정합 (설계 §4.1 vs 현 placeholder)
   122	
   123	- 현 placeholder: `LLMRequest(alias, messages, metadata)`. 설계 §4.1: `LLMRequest(messages, model_alias, system, ...)`.
   124	- 본 cycle = **redaction 통합 최소 변경** — 시그니처 전면 개편 (설계 §4.1 full)은 Router 위임 sub-cycle과 함께 (deferred). 현 placeholder 시그니처 기반 redaction layer 추가 (over-engineering 회피).
   125	
   126	---
   127	
   128	## §5 TDD 계획 (RED → GREEN → REFACTOR)
   129	
   130	### §5.1 RED (실패 test 먼저)
   131	
   132	`tests/adapters/llm/test_redaction_filter.py` (신규):
   133	- T-1: `redact_text("sk-ant-..." secret)` → `[REDACTED]` 치환
   134	- T-2: `redact_messages([{role, content: "key=sk-..."}])` → content redacted
   135	- T-3: Tier-1 45 catalog 대표 패턴 (baseline + prefix + regex + alternation 각 1+) redaction 검증
   136	- T-4: 정상 내용 (secret 0) → 무변경 (false positive 0)
   137	- T-5: `scrub(dict)` 재귀 (nested) redaction
   138	- T-6: facade `complete()` redaction 적용 + Router deferred NotImplementedError 검증 (redaction *후* deferred 순서)
   139	
   140	### §5.2 GREEN (최소 구현)
   141	
   142	- `src/adapters/llm/redaction.py` (RedactionFilter) + catalog 재사용 (§2.1 결정)
   143	- `facade.py` complete() redaction 통합
   144	
   145	### §5.3 REFACTOR
   146	
   147	- frozen / 순수 함수 정리 + test 유지 green
   148	- **커버리지 목표 70%+** (CLAUDE.md §1)
   149	
   150	### §5.4 verify (구현 후)
   151	
   152	- pytest (신규 redaction test + 기존 회귀 0)
   153	- import-linter (LLM SDK 경계 보존 — litellm import 0, Router deferred)
   154	- secret_scanner scan-source (src + .github, violations 0)
   155	- jarvis pytest 회귀 0
   156	
   157	---
   158	
   159	## §6 합의 형태 + 승격 트리거
   160	
   161	### §6.1 합의 형태 = 풀 3+1 + 외부 LLM 1+ (TR-1)
   162	
   163	**정당화**: facade.py 헤더 명시 TR-1 (real 본문 작성 풀 3+1 trigger) + GP-2 prevention 보안 영역 (CLAUDE.md §3 보안 = 풀 3+1 필수) + 실 코드 + Provider Liquidity 직결.
   164	
   165	### §6.2 승격 트리거
   166	
   167	| # | trigger | 발화 |
   168	|---|---------|----|
   169	| 1 | TR-1 (facade real 본문) | ✅ |
   170	| 2 | 보안 관련 변경 (GP-2 prevention) | ✅ |
   171	| 3 | 실 코드 (런타임 redaction) | ✅ |
   172	| 4 | Provider Liquidity 영향 (facade 단일 진입점) | ✅ |
   173	| 5 | 외부 LLM cross-vendor (5조-2) | ✅ |
   174	
   175	→ **5/5 발화 → 풀 3+1 + 외부 LLM 1+ 의무**.
   176	
   177	### §6.3 합의 시점
   178	
   179	본 brief = **구현 *전* 설계 승인** (SDD "문서 검토 완료 후 코드 구현" 답습). 합의 APPROVE 후 TDD 구현 (§5).
   180	
   181	---
   182	
   183	## §7 Provider Liquidity 보존 (ADR-009 §2.2, 5조-2 비협상)
   184	
   185	- LiteLLM 직접 import = facade.py 한정 (Router deferred이므로 본 cycle litellm import 0 — import-linter 보존).
   186	- RedactionFilter = facade 내부 협력자 (provider-agnostic, 모델명 분기 0).
   187	- facade 단일 진입점 의무 보존 ([[feedback_provider_liquidity]]).
   188	
   189	---
   190	
   191	## §8 금지 사항
   192	
   193	§0.2 답습 (10). 추가: LiteLLM 설치 0 / Router 위임 구현 0 / secret_scanner 패턴 변경 0 / litellm import 0 / full facade real 표현 0 / full GP-2 PASS 발효 0 / 자동 SC-2/SC-3 진입 0.
   194	
   195	---
   196	
   197	## §9 Rollback Trigger
   198	
   199	| # | trigger | 대응 |
   200	|---|---------|----|
   201	| RT-1 | Router 발효가 redaction layer *전* 진입 (window) | SC-Provider Liquidity는 본 SC-1 후 진입 (선부착 §4.2) |
   202	| RT-2 | catalog 재사용 (i) src→tools 의존 방향 BLOCKING | (ii) 공유 모듈 추출 fallback (R-7(b) 차등) |
   203	| RT-3 | redaction false positive (정상 내용 손상) | Tier-1 catalog = secret 패턴 한정 + T-4 test |
   204	| RT-4 | base64 evasion (Tier-1 미커버) | known limitation 명문 (R-5 영구 분리) |
   205	| RT-5 | redaction 성능 (매 송신 45 패턴 매칭) | COMPILED_PATTERNS 재사용 (사전 compile) |
   206	
   207	---
   208	
   209	## §10 Evidence
   210	
   211	- E-1: redaction test green (T-1~T-6) + 커버리지 70%+
   212	- E-2: facade complete() redaction 적용 + Router deferred 순서 검증
   213	- E-3: import-linter green (litellm import 0, 경계 보존)
   214	- E-4: secret_scanner scan-source violations 0
   215	- E-5: jarvis pytest 회귀 0
   216	
   217	---
   218	
   219	## §11 자기진단 (메타 편향 회피)
   220	
   221	| # | 위험 | 처리 |
   222	|---|------|----|
   223	| P-1 | "facade real 완성" over-claim | §0 명칭 정직성 — facade *redaction layer* real, Router deferred ([[feedback_pass_scope_overclaim]]) |
   224	| P-2 | full GP-2 PASS 기정사실화 | full GP-2 PASS = SC-2 (R-1) + SC-3 후 (§0.2 #3) |
   225	| P-3 | catalog 재사용 import 경계 임의 결정 | §2.1 4 옵션 풀 3+1 검증 (권고 (i), fallback (ii)) |
   226	| P-4 | secret_scanner 변경 (R-4.1 위반) | §0.2 #5 — 패턴 변경 0 (재사용만) |
   227	| P-5 | 송신 redaction 정상 내용 손상 | §3 — Tier-1 secret 패턴 한정 + T-4 false positive test |
   228	| P-6 | RT-1 window | §4.2 선부착 보장 (Router deferred = 송신 0) |
   229	| P-7 | 작성자 = 64 작성자 (Claude) cascade | cross-vendor codex + 풀 3+1 독립 검증 |
   230	
   231	---
   232	
   233	**본 brief v1 끝.**
   234	
   235	**다음 단계**: 사용자 승인 → 풀 3+1 + 외부 LLM 1+ (codex E-α, TR-1) → Reviewer 통합 → (필요시 v1.1 흡수) → **TDD 구현 (RED→GREEN→REFACTOR)** → verify → commit + push → **R-2 facade RedactionFilter prevention layer in-repo operative**. 후속: SC-2 (R-1 위임 검증) / SC-3 (full GP-2 PASS 발효) / SC-Provider Liquidity (Router 위임) = 사용자 명시 별도 sub-cycle.

exec
/bin/bash -lc "nl -ba docs/architecture/llm-providers-design.md | sed -n '180,295p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
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

exec
/bin/bash -lc "nl -ba docs/architecture/llm-providers-design.md | sed -n '500,545p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
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

exec
/bin/bash -lc "nl -ba docs/architecture/governance-preconditions.md | sed -n '400,470p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
   400	|---|------|------------|
   401	| (a) | 동등 이상의 보안 결과 | R-4 redaction-pattern-equivalence.md (3-way 비교 + Tier-1 42 gap 식별) |
   402	| (b) | 격리 환경 PoC 실증 | R-2 (`docker/r2-poc/`) + R-4.1 (`docker/r4-1-poc/`) |
   403	| (c) | ADR / SDD 권위 명시 | ADR-011 §2.1 + ADR-008 부록 B Amendment |
   404	| (d) | 자동 회귀 검증 경로 확보 | R-6 actual run `25482284523` PASS (24초, 42/42, leak 0) |
   405	| (e) | 합의 APPROVE | R-7 SOP §7.3 단축 합의 (Reviewer-only) `3plus1-consensus-2026-05-07-g1b-phase1-acceptance.md` |
   406	
   407	### 3.6 산출 후보 (보강 — 본 GP-1 범위 *내*)
   408	
   409	본 GP-1 은 G1b 흡수이므로 *추가 산출 0건*. 단, G2 통합 검증 시점에 **본 §3 자체를 G1b cross-reference 형태로 합의 보고서에 인용** — 이중 보호.
   410	
   411	### 3.7 의존 ADR / 갱신 후보
   412	
   413	- ADR-011 §2.1: 본문 변경 없음, §8.5 후속 작업에 G2 GP-1 흡수 등록 (G2 PASS 시점)
   414	- ADR-008 부록 B: 본문 변경 없음, B.6 결과를 G2 GP-1 cross-reference 추가 (G2 PASS 시점)
   415	
   416	---
   417	
   418	## 4. GP-2 — Egress Redaction (로그/LLM 송신)
   419	
   420	### 4.1 정의
   421	
   422	Hermes / Worker Agent 가 stdout / stderr / log file / LLM API request body 에 secret 을 노출하지 않도록 native redaction (`agent/redact.py`) + LLM facade redaction filter (P1 v2 §8.2) 가 사전 차단한다.
   423	
   424	**중요**: GP-2 는 ADR-011 §2.3 운영 함의 #2 의 *보조* 역할. **DB INSERT 차단은 GP-1 의 책임이며, GP-2 는 송신/로그 경로만 다룸**. GP-2 단독으로 헌법 8조 본질 충족 시도 금지.
   425	
   426	### 4.2 위반 경로
   427	
   428	- **P2** — 로그/LLM 송신 경로 평문 노출
   429	
   430	### 4.3 강제 메커니즘
   431	
   432	| 분류 | 메커니즘 | 위치 |
   433	|-----|---------|-----|
   434	| 계산적 | Hermes native redaction `agent/redact.py` (Tier-1 catalog 적용) | Hermes container |
   435	| 계산적 | P1 v2 LLM facade RedactionFilter | P1 facade layer |
   436	| 계산적 | base64 evasion test (R2-6) | `tests/hermes/redaction/test_base64_evasion.py` |
   437	| 계산적 | log file grep canary 자동 검증 | CI step (R-6 확장) |
   438	| 자동 회귀 | Hermes 의존성 업그레이드 시 R-2 / R-4.1 PoC 자동 재실행 (ADR-011 §2.3 운영 함의 #4) | R-6 workflow trigger 확장 |
   439	| 자동 롤백 | R-7 SOP §5 ROLLBACK trigger R5 (Hermes 학습 평문 검출) | R-7 SOP |
   440	
   441	### 4.4 Entry 기준
   442	
   443	- ✅ R-4 pattern equivalence 작성 완료 (충족됨)
   444	- ✅ Hermes native redaction `agent/redact.py` 존재 확인 (R-1 Day 2 evidence)
   445	- ⏳ 사용자 명시 GP-2 작업 진입 결정
   446	
   447	### 4.5 Exit 기준
   448	
   449	| # | 조건 | 검증 방식 |
   450	|---|------|---------|
   451	| (a) | 동등 이상의 보안 결과 | Hermes native redaction Tier-1 42 catalog 적용 검증 + P1 facade redaction filter 검증 |
   452	| (b) | 격리 환경 PoC 실증 | log file canary inject + grep 검증 PoC (Docker 격리) |
   453	| (c) | ADR / SDD 권위 명시 | ADR-011 §2.3 운영 함의 #2 cross-reference + 본 §4 권위 |
   454	| (d) | 자동 회귀 검증 경로 확보 | R-6 workflow 에 log file canary inject step 추가 |
   455	| (e) | 합의 APPROVE | 단축 또는 풀 3+1 합의 (G2 GP-2 한정 또는 G2 통합) |
   456	
   457	### 4.6 산출 후보
   458	
   459	- `tests/hermes/redaction/test_log_canary.py` (log file inject + grep)
   460	- R-6 workflow 확장 — log file canary inject step
   461	- 합의 보고서
   462	
   463	### 4.7 의존 ADR / 갱신 후보
   464	
   465	- ADR-011 §2.3: 본문 변경 없음, §8.5 후속 작업에 GP-2 산출 등록 (G2 PASS 시점)
   466	- ADR-008 차단조건 #1 보조 메커니즘 cross-reference
   467	
   468	---
   469	
   470	## 5. GP-3 — Credential / Secret Hygiene (저장 + 코드)

codex
초기 확인상 brief의 scope/over-claim 구분은 문서 안에서 반복적으로 방어되어 있습니다. 이제 호출 흐름 §4.4, ADR 단일 진입점, 실제 placeholder와 scanner API를 대조해 catalog 재사용 결정을 판단하겠습니다.
exec
/bin/bash -lc "nl -ba docs/architecture/llm-providers-design.md | sed -n '330,410p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
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

exec
/bin/bash -lc "nl -ba docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md | sed -n '1,170p'" in /home/delangi/문서/project/category/AI_development_tool
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

exec
/bin/bash -lc 'nl -ba src/adapters/llm/facade.py' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	"""LLMFacade — Provider-agnostic facade (G2 GP-5 placeholder).
     2	
     3	본 파일은 *유일하게* LiteLLM 직접 import 가 *허용되는 경로* 입니다 (§4.1 답습).
     4	현 시점은 **placeholder** — real 본문 작성 시 자동 풀 3+1 합의 trigger TR-1 발화.
     5	
     6	답습 출처:
     7	  - docs/architecture/llm-providers-design.md §4.1 (정확히 이 파일만 LiteLLM 직접 import)
     8	  - docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md §2.3 (Hermes PMO ↔ provider 영구 권위)
     9	  - docs/review/3plus1-consensus-2026-05-10-g2-gp5-poc2-depcruise-full.md §5.4 TR-1
    10	  - docs/phase0/g2-gp5-poc2-depcruise-rule-scope.md §2.1
    11	"""
    12	from __future__ import annotations
    13	
    14	from dataclasses import dataclass
    15	from typing import Any
    16	
    17	
    18	@dataclass(frozen=True)
    19	class LLMRequest:
    20	    alias: str
    21	    messages: list[dict[str, str]]
    22	    metadata: dict[str, Any] | None = None
    23	
    24	
    25	@dataclass(frozen=True)
    26	class LLMResponse:
    27	    content: str
    28	    metadata: dict[str, Any]
    29	
    30	
    31	class LLMFacade:
    32	    """Placeholder — real LiteLLM import + Router 위임은 TR-1 발화 시 작성."""
    33	
    34	    def __init__(self, registry_path: str) -> None:
    35	        self._registry_path = registry_path
    36	
    37	    def complete(self, request: LLMRequest) -> LLMResponse:
    38	        raise NotImplementedError("Placeholder — TR-1 풀 3+1 합의 후 real 본문 작성")
    39	
    40	    async def health(self) -> dict[str, bool]:
    41	        return {}

exec
/bin/bash -lc "nl -ba tools/secret_scanner.py | sed -n '1,260p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	#!/usr/bin/env python3
     2	"""Secret scanner — Group D PoC (G2 GP-3 Credential/Secret Hygiene + GP-2 Egress Redaction).
     3	
     4	답습 출처:
     5	  - docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md (본 PoC 사양)
     6	  - docs/architecture/redaction-pattern-equivalence.md (R-4 — 패턴 동등성 카탈로그)
     7	  - docs/phase0/r4-1-trigger-extension-evidence.md §4.1 (R-4.1 — Tier-1 42 catalog + baseline 5)
     8	  - docker/r4-1-poc/r4_1_poc.py line 51~213 (Tier-1 42 patterns + baseline 5 직접 답습)
     9	  - docs/architecture/governance-preconditions.md §4 (GP-2) + §5 (GP-3)
    10	  - docs/decisions/ADR-011-means-vs-ends-redaction.md §2.1 (a)~(e)
    11	
    12	핵심 강제 조건 (사용자 명시 답습):
    13	  - R-4.1 Tier-1 42 catalog + baseline 5 = 45 patterns 직접 답습 (변경 0건)
    14	  - Prefix 36 (baseline 5 + Tier-1 prefix 31) + 추가 regex 7 (H-A/B/C/E/F/G/K) + alternation 2 (H-J/H-L key 기반)
    15	  - H-J / H-L 직접 등록 제외 (alternation 채택, R-4.1 §4.2 답습)
    16	  - Tier-2 / Tier-3 catalog 확장 0건
    17	  - 외부 의존성 0건 (custom scanner 단독, gitleaks/detect-secrets 미도입)
    18	
    19	Mode (사용자 명시):
    20	  --mode scan-source : code-side secret 검출 (D-1 GP-3 Credential/Secret Hygiene)
    21	  --mode scan-log    : redaction 후 잔존 secret 검출 (D-2 GP-2 Egress Redaction)
    22	
    23	  본 PoC = 형식적 검출 layer 한정. Hermes 컨테이너 chmod / inotify (R1-2) =
    24	  Hermes upstream 영역, 본 PoC 미진입 (사용자 명시 #6).
    25	
    26	종료 코드:
    27	  0 = 위반 0건 (PASS)
    28	  1 = ≥1 위반 검출 (FAIL — D-1 secret 검출 / D-2 잔존 leak 검출)
    29	  2 = 입력 오류 (path 부재 등)
    30	
    31	알려진 한계 (사용자 명시 — 사양 §8):
    32	  - base64 / URL-encoded / 압축 등 advanced evasion 미커버 (Hermes upstream R2-6 영역)
    33	"""
    34	from __future__ import annotations
    35	
    36	import argparse
    37	import dataclasses
    38	import re
    39	import sys
    40	from dataclasses import dataclass
    41	from pathlib import Path
    42	from typing import Callable
    43	
    44	# ============================================================================
    45	# Tier-1 패턴 카탈로그 (45종) — R-4.1 §4.1 직접 답습
    46	#
    47	# 형식: (id, source, category, vendor, regex)
    48	#   - id: BL-N (baseline) 또는 T1-NNN (Tier-1)
    49	#   - source: Hermes 측 출처 식별자
    50	#   - category: prefix-baseline / prefix / regex / alternation
    51	#   - vendor: 사람이 읽을 수 있는 vendor/유형 라벨
    52	#   - regex: scanner 등록용 정규식 문자열
    53	# ============================================================================
    54	
    55	# Baseline 5 prefix (R-2 PoC 보존 — R-4.1 §4.1)
    56	BASELINE_PREFIX: list[tuple[str, str, str, str, str]] = [
    57	    ("BL-1", "Hermes #1 (sk-ant-)", "prefix-baseline", "Anthropic",
    58	     r"sk-ant-[A-Za-z0-9_-]{10,}"),
    59	    ("BL-2", "Hermes #1 (sk-)", "prefix-baseline", "OpenAI/Anthropic/etc",
    60	     r"sk-[A-Za-z0-9_-]{10,}"),
    61	    ("BL-3", "Hermes #2", "prefix-baseline", "GitHub PAT classic",
    62	     r"ghp_[A-Za-z0-9]{10,}"),
    63	    ("BL-4", "Hermes #15", "prefix-baseline", "AWS Access Key ID",
    64	     r"AKIA[A-Z0-9]{16}"),
    65	    ("BL-5", "Hermes #8", "prefix-baseline", "Slack tokens",
    66	     r"xox[baprs]-[A-Za-z0-9-]{10,}"),
    67	]
    68	
    69	# Tier-1 prefix 31 (Hermes #3..#7, #9..#14, #16..#35) — R-4.1 §4.1 직접 답습
    70	PREFIX_PATTERNS: list[tuple[str, str, str, str, str]] = [
    71	    ("T1-001", "Hermes #3", "prefix", "GitHub PAT (fine-grained)",
    72	     r"github_pat_[A-Za-z0-9_]{10,}"),
    73	    ("T1-002", "Hermes #4", "prefix", "GitHub OAuth access token",
    74	     r"gho_[A-Za-z0-9]{10,}"),
    75	    ("T1-003", "Hermes #5", "prefix", "GitHub user-to-server",
    76	     r"ghu_[A-Za-z0-9]{10,}"),
    77	    ("T1-004", "Hermes #6", "prefix", "GitHub server-to-server",
    78	     r"ghs_[A-Za-z0-9]{10,}"),
    79	    ("T1-005", "Hermes #7", "prefix", "GitHub refresh token",
    80	     r"ghr_[A-Za-z0-9]{10,}"),
    81	    ("T1-006", "Hermes #9", "prefix", "Google API keys",
    82	     r"AIza[A-Za-z0-9_-]{30,}"),
    83	    ("T1-007", "Hermes #10", "prefix", "Perplexity",
    84	     r"pplx-[A-Za-z0-9]{10,}"),
    85	    ("T1-008", "Hermes #11", "prefix", "Fal.ai",
    86	     r"fal_[A-Za-z0-9_-]{10,}"),
    87	    ("T1-009", "Hermes #12", "prefix", "Firecrawl",
    88	     r"fc-[A-Za-z0-9]{10,}"),
    89	    ("T1-010", "Hermes #13", "prefix", "BrowserBase",
    90	     r"bb_live_[A-Za-z0-9_-]{10,}"),
    91	    ("T1-011", "Hermes #14", "prefix", "Codex encrypted tokens",
    92	     r"gAAAA[A-Za-z0-9_=-]{20,}"),
    93	    ("T1-012", "Hermes #16", "prefix", "Stripe secret key (live)",
    94	     r"sk_live_[A-Za-z0-9]{10,}"),
    95	    ("T1-013", "Hermes #17", "prefix", "Stripe secret key (test)",
    96	     r"sk_test_[A-Za-z0-9]{10,}"),
    97	    ("T1-014", "Hermes #18", "prefix", "Stripe restricted key",
    98	     r"rk_live_[A-Za-z0-9]{10,}"),
    99	    ("T1-015", "Hermes #19", "prefix", "SendGrid API key",
   100	     r"SG\.[A-Za-z0-9_-]{10,}"),
   101	    ("T1-016", "Hermes #20", "prefix", "HuggingFace token",
   102	     r"hf_[A-Za-z0-9]{10,}"),
   103	    ("T1-017", "Hermes #21", "prefix", "Replicate API token",
   104	     r"r8_[A-Za-z0-9]{10,}"),
   105	    ("T1-018", "Hermes #22", "prefix", "npm access token",
   106	     r"npm_[A-Za-z0-9]{10,}"),
   107	    ("T1-019", "Hermes #23", "prefix", "PyPI API token",
   108	     r"pypi-[A-Za-z0-9_-]{10,}"),
   109	    ("T1-020", "Hermes #24", "prefix", "DigitalOcean PAT",
   110	     r"dop_v1_[A-Za-z0-9]{10,}"),
   111	    ("T1-021", "Hermes #25", "prefix", "DigitalOcean OAuth",
   112	     r"doo_v1_[A-Za-z0-9]{10,}"),
   113	    ("T1-022", "Hermes #26", "prefix", "AgentMail API key",
   114	     r"am_[A-Za-z0-9_-]{10,}"),
   115	    ("T1-023", "Hermes #27", "prefix", "ElevenLabs TTS key",
   116	     r"sk_[A-Za-z0-9_]{10,}"),
   117	    ("T1-024", "Hermes #28", "prefix", "Tavily search API",
   118	     r"tvly-[A-Za-z0-9]{10,}"),
   119	    ("T1-025", "Hermes #29", "prefix", "Exa search API",
   120	     r"exa_[A-Za-z0-9]{10,}"),
   121	    ("T1-026", "Hermes #30", "prefix", "Groq Cloud API key",
   122	     r"gsk_[A-Za-z0-9]{10,}"),
   123	    ("T1-027", "Hermes #31", "prefix", "Matrix access token",
   124	     r"syt_[A-Za-z0-9]{10,}"),
   125	    ("T1-028", "Hermes #32", "prefix", "RetainDB API key",
   126	     r"retaindb_[A-Za-z0-9]{10,}"),
   127	    ("T1-029", "Hermes #33", "prefix", "Hindsight API key",
   128	     r"hsk-[A-Za-z0-9]{10,}"),
   129	    ("T1-030", "Hermes #34", "prefix", "Mem0 Platform API key",
   130	     r"mem0_[A-Za-z0-9]{10,}"),
   131	    ("T1-031", "Hermes #35", "prefix", "ByteRover API key",
   132	     r"brv_[A-Za-z0-9]{10,}"),
   133	]
   134	
   135	# Tier-1 추가 regex 7 (H-A, H-B, H-C, H-E, H-F, H-G, H-K — H-J/H-L 제외, R-4.1 §4.2 답습)
   136	REGEX_PATTERNS: list[tuple[str, str, str, str, str]] = [
   137	    ("T1-032", "Hermes H-A", "regex", "ENV assignment",
   138	     r"([A-Z0-9_]{0,50}(?:API_?KEY|TOKEN|SECRET|PASSWORD|PASSWD|CREDENTIAL|AUTH)[A-Z0-9_]{0,50})\s*=\s*(['\"]?)(\S+)\2"),
   139	    ("T1-033", "Hermes H-B", "regex", "JSON field with secret keys",
   140	     r'(?i)("(?:api_?[Kk]ey|token|secret|password|access_token|refresh_token|auth_token|bearer|secret_value|raw_secret|secret_input|key_material)")\s*:\s*"([^"]+)"'),
   141	    ("T1-034", "Hermes H-C", "regex", "Authorization header (Bearer)",
   142	     r"(?i)(Authorization:\s*Bearer\s+)(\S+)"),
   143	    ("T1-035", "Hermes H-E", "regex", "Private key block",
   144	     r"-----BEGIN[A-Z ]*PRIVATE KEY-----[\s\S]*?-----END[A-Z ]*PRIVATE KEY-----"),
   145	    ("T1-036", "Hermes H-F", "regex", "DB connstr password",
   146	     r"(?i)((?:postgres(?:ql)?|mysql|mongodb(?:\+srv)?|redis|amqp)://[^:]+:)([^@]+)(@)"),
   147	    ("T1-037", "Hermes H-G", "regex", "JWT token",
   148	     r"eyJ[A-Za-z0-9_-]{10,}(?:\.[A-Za-z0-9_=-]{4,}){0,2}"),
   149	    ("T1-039", "Hermes H-K", "regex", "URL userinfo (non-DB)",
   150	     r"(https?|wss?|ftp)://([^/\s:@]+):([^/\s@]+)@"),
   151	]
   152	
   153	# Tier-1 alternation 2 (H-J / H-L sensitive key 기반 변환, R-4.1 §4.1 답습)
   154	ALTERNATION_PATTERNS: list[tuple[str, str, str, str, str]] = [
   155	    # (b1-PC1-D6-false-positives) 합의 2026-05-27 APPROVE WITH CONDITIONS (R-1 BLOCKING 흡수)
   156	    # (b1-PC1-D6-fp-edge-extensions) 합의 2026-05-27 APPROVE (단축 + codex cross-vendor, semicolon + fragment 확장)
   157	    # word boundary `(?:^|[?&\s'\";#])` prefix — Python keyword arg FP 해소 + quoted body literal cover + Cookie semicolon + OAuth fragment cover
   158	    # `(` paren delimiter 추가 0 = `sort(key=...)` / `WorkerResult(exit_code=...)` FP 재발 회피 (codex N-4 답습)
   159	    # carry-over: (b1-PC1-D6-ast-context) AST SAFE_CONTEXT
   160	    ("T1-041", "Hermes _SENSITIVE_QUERY_PARAMS", "alternation", "URL query sensitive keys (16)",
   161	     r"(?i)(?:^|[?&\s'\";#])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|session|secret|key|code|signature|x-amz-signature)=[^&\s]+"),
   162	    ("T1-042", "Hermes _SENSITIVE_BODY_KEYS", "alternation", "Body/form sensitive keys (14)",
   163	     r"(?i)(?:^|[?&\s'\";#])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|secret|private_key|authorization|key)=[^&\s]+"),
   164	]
   165	
   166	ALL_PATTERNS: list[tuple[str, str, str, str, str]] = (
   167	    BASELINE_PREFIX + PREFIX_PATTERNS + REGEX_PATTERNS + ALTERNATION_PATTERNS
   168	)
   169	"""All registered patterns — 5 baseline + 31 prefix + 7 regex + 2 alternation = 45 patterns."""
   170	
   171	# Compiled regex objects (모듈 import 시 1회 컴파일)
   172	COMPILED_PATTERNS: list[tuple[str, str, str, str, re.Pattern[str]]] = [
   173	    (pid, src, cat, vendor, re.compile(rgx))
   174	    for (pid, src, cat, vendor, rgx) in ALL_PATTERNS
   175	]
   176	
   177	# 본 PoC 직접 등록 제외 (R-4.1 §4.2 답습 — alternation 채택, H-J/H-L 직접 등록 false-positive 회피)
   178	SKIP_DIRECT_REGISTER: frozenset[str] = frozenset({"T1-038", "T1-040"})
   179	
   180	# Redaction marker exclusion (scan-log mode 전용 — GP-2 D-2 contract 답습).
   181	# 사양 §0 — D-2 = "redaction 후 잔존 secret 검증". 본 marker 가 매칭 substring 전체를
   182	# 차지하면 *정상 redacted output* 로 분류, 위반 미카운트 (FP 회피).
   183	REDACTION_MARKER_RE: re.Pattern[str] = re.compile(
   184	    r"(?i)(\[REDACTED\]|\[FILTERED\]|\[MASKED\]|<REDACTED>|<MASKED>|<<masked>>|\*{5,})"
   185	)
   186	
   187	# Scan 대상 file extension (사양 §4.1~§4.2 답습)
   188	#
   189	# scope 정책 (49 entry 발효): docs/architecture/secret-scanner-scope-policy.md
   190	#   - hook entry scope: src + .github 한정 (.pre-commit-config.yaml 답습)
   191	#   - docs/ 영역 영구 금지 (~800+ 잠재 false positive 답습 — fake canary / redaction 예시 / codex 응답 sample)
   192	#   - scope 확장 의무 절차: 정책 §2 답습 (별도 sub-cycle + 풀 3+1 + R-7(b) 차등)
   193	#   - 본 SCAN_SOURCE_EXTENSIONS 변경 = catalog 본문 변경 = R-7(b) 차등 자격
   194	SCAN_SOURCE_EXTENSIONS: tuple[str, ...] = (
   195	    ".py", ".json", ".yaml", ".yml", ".toml", ".sh", ".bash",
   196	    ".env", ".ini", ".cfg", ".pem", ".key", ".txt", ".md",
   197	)
   198	SCAN_LOG_EXTENSIONS: tuple[str, ...] = (".txt", ".log", ".json", ".jsonl", ".md", ".pem")
   199	
   200	
   201	@dataclass(frozen=True)
   202	class Violation:
   203	    """Single secret detection."""
   204	
   205	    file: Path
   206	    line: int
   207	    pattern_id: str
   208	    pattern_source: str
   209	    pattern_category: str
   210	    pattern_vendor: str
   211	    matched_text: str
   212	
   213	    def format_short(self) -> str:
   214	        # Truncate matched_text to avoid leaking full canary in CI log (defensive)
   215	        sample = self.matched_text[:30] + ("..." if len(self.matched_text) > 30 else "")
   216	        return (
   217	            f"{self.file}:{self.line}:{self.pattern_id}:"
   218	            f"{self.pattern_category}:{self.pattern_vendor}: {sample!r}"
   219	        )
   220	
   221	
   222	def is_redaction_marker_match(matched_text: str) -> bool:
   223	    """Scan-log mode 한정 — 매칭 텍스트가 redaction marker 만 포함하면 정상 redacted (FP 회피).
   224	
   225	    GP-2 D-2 contract — 'redaction 후 잔존 secret 검증' (사양 §0).
   226	    예: `OPENAI_API_KEY=[REDACTED]` 의 H-A regex 매칭은 [REDACTED] marker → 위반 미카운트.
   227	    """
   228	    return REDACTION_MARKER_RE.search(matched_text) is not None
   229	
   230	
   231	def scan_text(text: str, file_path: Path, mode: str | None = None) -> list[Violation]:
   232	    """Apply all 45 patterns to text and return violations.
   233	
   234	    Line number = 1-indexed (file::line 표기 답습).
   235	    mode='scan-log' 시 redaction marker 매칭은 위반 미카운트 (FP 회피, 사양 §0).
   236	    """
   237	    vios: list[Violation] = []
   238	    for pid, src, cat, vendor, pattern in COMPILED_PATTERNS:
   239	        if pid in SKIP_DIRECT_REGISTER:
   240	            continue
   241	        for m in pattern.finditer(text):
   242	            matched = m.group(0)
   243	            if mode == "scan-log" and is_redaction_marker_match(matched):
   244	                continue
   245	            line_no = text[: m.start()].count("\n") + 1
   246	            vios.append(
   247	                Violation(
   248	                    file=file_path,
   249	                    line=line_no,
   250	                    pattern_id=pid,
   251	                    pattern_source=src,
   252	                    pattern_category=cat,
   253	                    pattern_vendor=vendor,
   254	                    matched_text=matched,
   255	                )
   256	            )
   257	    return vios
   258	
   259	
   260	def iter_files(root: Path, allowed_exts: tuple[str, ...]) -> list[Path]:

exec
/bin/bash -lc 'nl -ba .importlinter' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
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

exec
/bin/bash -lc "rg --files -g '__init__.py' | sed -n '1,120p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
src/__init__.py
src/jarvis/__init__.py
src/adapters/__init__.py
src/adapters/llm/__init__.py
tests/jarvis/__init__.py

exec
/bin/bash -lc "find tools -maxdepth 2 -type f -print | sort | sed -n '1,120p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
tools/__pycache__/canonical_json.cpython-312.pyc
tools/__pycache__/history_anchor_verifier.cpython-312.pyc
tools/__pycache__/jsonl_hash_chain.cpython-312.pyc
tools/__pycache__/jsonl_roundtrip.cpython-312.pyc
tools/__pycache__/rewrite_defense_check.cpython-312.pyc
tools/__pycache__/schema_validator.cpython-312.pyc
tools/__pycache__/secret_scanner.cpython-312.pyc
tools/boundary_guard.py
tools/canonical_json.py
tools/docker_secret_image_layer_check.sh
tools/docker_secret_inotify_sidecar_check.sh
tools/docker_secret_restart_recovery.sh
tools/evidence_pass_gate.py
tools/history_anchor_verifier.py
tools/jsonl_hash_chain.py
tools/jsonl_roundtrip.py
tools/memory_skill_roundtrip.py
tools/mvp1_pc3_ar1_integration_check.py
tools/pre_commit_install_audit.sh
tools/provider_import_scanner.py
tools/provider_url_scanner.py
tools/rewrite_defense_check.py
tools/schema_validator.py
tools/secret_scanner.py
tools/workflow_fork_pr_secret_policy_check.py
tools/workflow_permissions_check.py
tools/workflow_secrets_reference_check.py
tools/workflow_secrets_usage_check.py

exec
/bin/bash -lc "rg -n \"RedactionFilter|redact_messages|secret_scanner|COMPILED_PATTERNS|scan_text\" -S src tests docs/phase0 docs/architecture docs/decisions | sed -n '1,220p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
docs/architecture/mvp-1-to-6-entry-conditions-brief.md:112:| 2 | GP-2 PoC 완료 (Group D §1.2 #6 / P1 facade RedactionFilter 답습) | `docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md` D-2 (partial) |
docs/architecture/mvp-1-to-6-entry-conditions-brief.md:114:| 4 | R-4 / R-4.1 Tier-1 42 catalog **런타임 적용** layer 시제 (Hermes upstream R2-6 또는 P1 facade RedactionFilter) | Group D PoC §8 #1 답습 |
docs/architecture/mvp-1-to-6-entry-conditions-brief.md:120:- 수단 후보 비교 (GP-2 송신 redaction = Hermes upstream R2-6 vs sidecar vs P1 facade RedactionFilter)
docs/architecture/implementation-runtime-roadmap.md:72:| **G2** | **GP-2 Egress Redaction** (로그 / LLM 송신 차단) | PoC + CI | ADR-011 §2.3 운영 함의 #2, ADR-008 부록 B + §A.2, P1 v2 §8.2 RedactionFilter, R-4 patterns | (a) 동등 이상 보안 결과 (Hermes native + P1 facade redaction 비교) / (b) 격리 PoC (Docker isolation) / (c) ADR 권위 (ADR-011 §2.3 #2) / (d) 자동 회귀 (R-2 답습 nightly) / (e) 합의 APPROVE | log/송신 redaction 6 patterns BLOCK 100% + base64 evasion BLOCK + R-2 답습 PoC PASS | **HIGH** (P2 헌법 8조 위반 경로) | **5 (10/11)** |
docs/architecture/governance-preconditions.md:435:| 계산적 | P1 v2 LLM facade RedactionFilter | P1 facade layer |
docs/architecture/implementation-runtime-roadmap-mvp1.md:105:1. **R-4 / R-4.1 답습 책임 분담** — GP-2 의 송신 redaction = R-4.1 Tier-1 42 catalog 의 *런타임 적용* 영역. 본 PoC (Group D) 는 *형식적 검출 layer 한정* (D-2 = redacted output 잔존 검증). 실 송신 redaction = Hermes upstream 영역 (Group D PoC §1.2 #6 답습) + P1 facade RedactionFilter 본문 (Group D PoC §1.2 마지막 항목 답습).
docs/architecture/implementation-runtime-roadmap-mvp1.md:155:| code-side secret 검출 (D-1, source scan) | ✅ PASS 6/6 | `tools/secret_scanner.py --mode scan-source` (R-4.1 Tier-1 45 patterns 직접 답습) |
docs/architecture/implementation-runtime-roadmap-mvp1.md:156:| redacted output 잔존 secret 검증 (D-2) | ✅ PASS 6/6 (partial leak 검출 + base64 evasion known limitation) | `tools/secret_scanner.py --mode scan-log` |
docs/architecture/implementation-runtime-roadmap-mvp1.md:167:| G3-4 | base64 / URL-encoded / 압축 evasion | **MVP-1 → MVP-2/3 영역** — Hermes upstream R2-6 또는 P1 facade RedactionFilter 영역 (Group D PoC §8 #1 답습) | 본 문서 범위 외 (분리 영역 명시) |
docs/architecture/implementation-runtime-roadmap-mvp1.md:279:| Group D PoC `tools/secret_scanner.py` 직접 재사용 | Group D PoC 산출물 | ✅ |
docs/architecture/implementation-runtime-roadmap-mvp1.md:659:| **S-1** | custom regex secret scanner (R-4.1 Tier-1 45 patterns) | GP-3 코드 본문 secret 검출 (G3-2) | Group D PoC `tools/secret_scanner.py` 261줄 답습 + actual run `25623028888` SUCCESS + Layer A §1.2 + Layer B §1.1 답습 | Tier-2/3 catalog 확장 0건 / 외부 의존 도입 0건 / runtime code *실 구현* 0건 (별도 단계) |
tests/fixtures/schema_validation/external_input/pass/safe_worker_output.json:8:  "files_changed": ["tools/secret_scanner.py", "tests/fixtures/secret_hygiene/pass/safe_config.py"]
docs/architecture/secret-scanner-scope-policy.md:25:### 1.3 secret_scanner.py 자체 scope
docs/architecture/secret-scanner-scope-policy.md:80:| `secret_scanner.py` `SCAN_SOURCE_EXTENSIONS` | catalog 본문 변경 자격 = R-7(b) PC1-2 차등 답습 |
docs/architecture/redaction-pattern-equivalence.md:148:### 3.1 `RedactionFilter.PATTERNS` (4종)
docs/architecture/hermes-adoption-design.md:176:P1의 `RedactionFilter`(P1 §8.2)를 Hermes 학습루프 기록 직전에 적용:
docs/architecture/hermes-adoption-design.md:432:| 로그/메트릭 echo 금지 | RedactionFilter 자동 strip |
docs/architecture/llm-providers-design.md:261:        self._redactor = RedactionFilter(...)    # R3 보강
docs/architecture/llm-providers-design.md:477:| **로그/메트릭 echo 금지** | RedactionFilter가 `auth/token/key/secret` 패턴 자동 strip (§8.2) |
docs/architecture/llm-providers-design.md:521:class RedactionFilter:
tests/fixtures/secret_hygiene/mvp1_entry/fail/regex_categories_extra.py:6:# 답습 변경 0건 — tools/secret_scanner.py 본문 / R-4.1 Tier-1 45 patterns 변경 0건.
docs/phase0/g2-gp3-mvp1-evidence.md:31:- **S-1** (Group D scanner, R-4.1 Tier-1 45 patterns) — `tools/secret_scanner.py` (368줄) 발효 (R-MVP1-1.5-S3-3 영구 의무 답습)
docs/phase0/backlog1-2-pc4-t2-implementation-brief.md:17:- 도구 검증 답습: `tools/secret_scanner.py` (Group D `25623028888`) / `tools/provider_import_scanner.py` (Group A 1차) / `tools/provider_url_scanner.py` (Group A 3차 `25629390384`) / `lint-imports` + `.importlinter` (Group A 2차 `25605665191`)
docs/phase0/backlog1-2-pc4-t2-implementation-brief.md:80:- ❌ 도구 본문 변경 0건 (`tools/secret_scanner.py` / `tools/provider_import_scanner.py` / `tools/provider_url_scanner.py` / `.importlinter` 모두 변경 0건)
docs/phase0/backlog1-2-pc4-t2-implementation-brief.md:219:| 도구 entry | `python tools/secret_scanner.py` |
docs/phase0/backlog1-2-pc4-t2-implementation-brief.md:273:| 기존 도구 본문 변경 | ❌ 0건 (`tools/secret_scanner.py` 답습) |
docs/phase0/backlog1-2-pc4-t2-implementation-brief.md:523:| `tools/secret_scanner.py` | `secret-hygiene-egress-redaction.yml` | `python tools/secret_scanner.py` | ✅ 도구 본문 = 단일 source-of-truth |
docs/phase0/backlog1-2-pc4-t2-implementation-brief.md:730:| 6 | 도구 본문 변경 (`tools/secret_scanner.py` / `tools/provider_*.py`) | Layer B `55c5b4b` 본문 채택 답습 |
docs/phase0/mvp2-gamma-decision-brief.md:162:3. **실 구현 sub-cycle** ((β) + (γ-c) 채택 후) — Hermes upstream `agent/redact.py` 영역 + 본 repo P1 facade RedactionFilter (TR-1 (d) carry-over 의존) + Layer 1+2+4 PoC → PASS + R-6 workflow 확장 step (Layer 2a `denyNonFastForwards` 활성화 evidence 별도 verify 의무, 53 entry B-3 답습)
docs/phase0/g2-gp5-poc3-url-endpoint-model-name-scanner.md:318:| 9 | URL fragment / query string 분석 (예: `?api_key=...`) | Group D `secret_scanner.py` 영역 — 별도 책무 분리 | Group D 답습 분리 |
docs/phase0/backlog1-c5c-pc4-t2-sub-brief.md:199:| GP-3 secret scanner | `tools/secret_scanner.py` (Group D PoC 답습 + Layer B `55c5b4b` 본문 채택 S-1) | hook entry 후보 — 동일 도구가 CI 와 local 에서 동일하게 동작 가능 (`55c5b4b` 답습) |
docs/phase0/backlog1-c5c-pc4-t2-sub-brief.md:214:| 1 | `secret-scanner` | `tools/secret_scanner.py` | `\.(py|js|ts|md|yml|yaml|sh|toml)$` (Tier-1 45 patterns 답습 한정) | T2 sub 채택 시 *우선 후보* (S-1 본문 채택 답습) |
docs/phase0/backlog6-implementation-step-brief.md:38:- ❌ **실 runtime code 구현 (0건)** — `tools/secret_scanner.py` 본문 변경 / `tools/provider_import_scanner.py` 본문 변경 / `tools/provider_url_scanner.py` 본문 변경 / `src/adapters/llm/facade.py` 본문 작성 / inotify sidecar 본문 / chmod 600 entrypoint script 본문 0건
docs/phase0/backlog6-implementation-step-brief.md:112:| **GP-3** | **S-1** | 코드 본문 secret 검출 (custom regex, R-4.1 Tier-1 45 patterns) | Group D PoC `tools/secret_scanner.py` 261줄 답습 |
docs/phase0/backlog6-implementation-step-brief.md:136:| **Stage 1** | **GP-3 코드 본문 검출 확장** | S-1 | Group D `tools/secret_scanner.py` 261줄 답습 + MVP-1 entry 확장 (CI workflow 호환 + ledger entry 형식) |
docs/phase0/backlog6-implementation-step-brief.md:148:| 1.1 | `tools/secret_scanner.py` 본문 답습 검증 | Group D PoC §2.1 (A) | 261줄 답습 변경 0건 + R-4.1 Tier-1 45 patterns 답습 변경 0건 |
docs/phase0/backlog6-implementation-step-brief.md:286:| `tools/secret_scanner.py` (Group D PoC 261줄) | Stage 1 | Stage 1 | Group D PoC 답습 | 0건 — 본 brief 는 답습 검증 한정 |
docs/phase0/backlog6-implementation-step-brief.md:332:| (a) GP-3 Implementation Evidence | `tools/secret_scanner.py` 확장 + workflow 확장 + 실행 log + actual run SUCCESS URL + 코드 diff + 4 patterns cover (alternation/prefix-baseline/regex/private-key T1-035) | Markdown report 형태 |
docs/phase0/mvp2-gp2-pass-activation-brief.md:40:| 6 | 신규 외부 library 도입 / secret_scanner Tier-2/3 catalog 확장 | 0 |
docs/phase0/mvp2-gp2-pass-activation-brief.md:44:| 10 | secret_scanner.py / secret-hygiene-egress-redaction.yml 본문 변경 | 0 (PoC 시제 보존) |
docs/phase0/mvp2-gp2-pass-activation-brief.md:58:- **본 cycle audit (read-only, 2026-05-28)** — secret-hygiene CI + fixtures + secret_scanner filesystem direct
docs/phase0/mvp2-gp2-pass-activation-brief.md:89:| (d) | 자동 회귀 검증 경로 (detection) | ✅ ⭐ | **`secret-hygiene-egress-redaction.yml` D-2 step (scan-log redaction residual, `secret_scanner.py --mode scan-log`) — 51 audit "❌ gap" 부정확 정정 (52 entry PoC 시제 발견 동형). actual run `26517803107` success (headSha `4fec6485`). secret-hygiene = `workflow_dispatch` 미지원 (schedule cron `0 3 * * *` 만) — secret_scanner.py + workflow + redaction fixtures = 49 entry (`4fec6485`) 이후 변경 0 (불변) → 유효 evidence** |
docs/phase0/mvp2-gp2-pass-activation-brief.md:103:| R-2 facade RedactionFilter | ⚠️ placeholder | facade real (TR-1) deferred trajectory |
docs/phase0/mvp2-gp2-pass-activation-brief.md:115:| **R-3** log canary CI (`secret-hygiene-egress-redaction.yml` + `secret_scanner.py --mode scan-log`) | **detection (회귀 검증)** | ✅ operative green | GP-2 (d) 자동 회귀 충족 — in-repo operative means |
docs/phase0/mvp2-gp2-pass-activation-brief.md:117:| **R-2** facade RedactionFilter | prevention (LLM API 진입점) | ⚠️ facade placeholder | facade real (TR-1) 시점 추가 layer (deferred trajectory) |
docs/phase0/mvp2-gp2-pass-activation-brief.md:210:- 실 evidence: `secret-hygiene-egress-redaction.yml` (D-2) + `tools/secret_scanner.py` (--mode scan-log) + `tests/fixtures/secret_hygiene/{redaction_pass,redaction_fail}/`
docs/phase0/day1-environment-and-fact-check.md:218:- P1 v2 §8.2 RedactionFilter는 P1 facade 레벨 → **영향 없음** (Hermes 자체 redaction과 별개)
docs/phase0/backlog1-2-c5c-pc4-t2-integrated-brief.md:189:| 도구 답습 | `tools/secret_scanner.py` (Group D PoC + Layer B `55c5b4b` 본문 채택 S-1 답습, 261줄) |
docs/phase0/backlog1-2-c5c-pc4-t2-integrated-brief.md:397:| GP-3 secret scanner | `python tools/secret_scanner.py ${changed_files}` | `python tools/secret_scanner.py` (pre-commit framework 가 `${changed_files}` 자동 전달) |
docs/phase0/phase-alpha-4-r1-local-validation-evidence.md:209:  [PASS] PC-3 secret-hygiene-egress-redaction.yml: MVP-1 entry — secret_scanner coverage check (mvp1_entry/ fixtures)
docs/phase0/mvp1-1.5th-reinforcement-entry-brief.md:136:✅ **secret_scanner.py (S-1) 답습 유지** — S-3 = *추가* layer (S-1 미대체, Defense in depth)
docs/phase0/mvp1-1.5th-reinforcement-entry-brief.md:137:✅ **`.github/workflows/secret-hygiene-egress-redaction.yml` step 통합** — 현 secret_scanner.py 답습 *후속* step
docs/phase0/mvp1-1.5th-reinforcement-entry-brief.md:486:- `tools/secret_scanner.py` (S-1 답습) + `tools/docker_secret_inotify_sidecar_check.sh` (ST-2 실 구현) + `.pre-commit-config.yaml` (PC-4 T2 sub) + `.github/workflows/*.yml` (11 workflow, AR-1 답습)
docs/phase0/mvp2-beta-submeans-decision-brief.md:36:| 2 | `tools/*.py` 본문 변경 (jsonl_hash_chain / canonical_json / secret_scanner 등) | 0건 (PoC 시제 답습 보존) |
docs/phase0/mvp2-beta-submeans-decision-brief.md:91:| **GP-2 CI 회귀 검증** | ✅ `secret-hygiene-egress-redaction.yml` (51791B, D-2 scan-log redaction_pass/fail + base64 known limitation) + `tools/secret_scanner.py` (16802B, `--mode scan-log` redaction 잔존 검출, **registered 45 (Tier-1 42 catalog compliant + baseline 포함)**, N-1 정정) | **R-3 (log canary CI) 시제 충족** |
docs/phase0/mvp2-beta-submeans-decision-brief.md:120:| **R-2** | P1 facade RedactionFilter | LLM API 진입점 redaction | ⚠️ facade placeholder | facade real (TR-1, (d) carry-over) | facade single entry point redaction means — 구현 경로 = TR-1 trajectory |
docs/phase0/mvp2-beta-submeans-decision-brief.md:121:| **R-3** | log canary inject + grep CI step | CI 회귀 검증 | ✅ **시제 충족** (`secret-hygiene-egress-redaction.yml` + `secret_scanner.py --mode scan-log`) | 없음 (즉시 PASS 격상 가능) | MANDATORY ((d) 자동 회귀 경로) |
docs/phase0/mvp2-beta-submeans-decision-brief.md:351:- 실 repo PoC 시제 (secret_scanner.py + jsonl_hash_chain.py + canonical_json.py + 5 workflows + tests/canonical 72)
docs/phase0/mvp2-beta-submeans-decision-brief.md:383:- 실 repo PoC: `tools/secret_scanner.py` + `tools/jsonl_hash_chain.py` + `tools/canonical_json.py` + `.github/workflows/{secret-hygiene-egress-redaction,g4-hash-chain,history-anchor-verifier,rewrite-defense,r2-canary}.yml` + `tests/canonical/` 72 files
docs/phase0/mvp2-beta-submeans-decision-brief.md:424:tests/canonical 72/8/24 + agent/redact.py 부재 + facade placeholder + 5 workflow 보존 (총 12) + secret_scanner 45 patterns + denyNonFastForwards 미설정 + (γ-c) 특화 의무 4 정합 + scope 침입 0 + R-5 evasion 영구 분리 정당 + history-anchor-verifier Layer 5 PoC 시제 ≠ Layer 5 진입 = 4 source 일치 확인.
docs/phase0/phase-alpha-123-local-validation-evidence.md:144:| α-1 (R-4) | `tools/secret_scanner.py` | 368 | `1719a01` (2026-05-09) | 0건 |
docs/phase0/phase-alpha-123-local-validation-evidence.md:181:| 1.1 | secret_scanner — scan-source PASS fixture | `tools/secret_scanner.py` | `tests/fixtures/secret_hygiene/pass/` | violations=0 | violations=0 | 0 | ✅ |
docs/phase0/phase-alpha-123-local-validation-evidence.md:182:| 1.2 | secret_scanner — scan-source FAIL fixture | `tools/secret_scanner.py` | `tests/fixtures/secret_hygiene/fail/` | violations 검출 (3 category cover) | violations 검출 (alternation + prefix-baseline + regex) | 1 | ✅ |
docs/phase0/phase-alpha-123-local-validation-evidence.md:193:`tools/secret_scanner.py --list-patterns` 실행 결과:
docs/phase0/phase-alpha-123-local-validation-evidence.md:268:$ git diff --stat HEAD -- tools/secret_scanner.py tools/provider_import_scanner.py tools/provider_url_scanner.py .importlinter docker/gp3-st3-poc/ tools/docker_secret_image_layer_check.sh tools/docker_secret_restart_recovery.sh tests/fixtures/gp3_st3/
docs/phase0/phase-alpha-123-local-validation-evidence.md:442:본 evidence 는 **Phase α-1 + α-2 + α-3 parallel actual implementation entry 합의 (`7917e4a` Reviewer-only 단축 합의 APPROVE — 25 조건 C-ξ-1 ~ C-ξ-25) 발효 후속**, 사용자 명시 결정 옵션 (A) 답습 — **현재 local 검증 결과 자체를 "Phase α-1 + α-2 + α-3 실 진입 완료 evidence" 로 고정 한정 문서**. **사용자 명시 8 금지** (R-4/R-5/R-7 본문 수정 / 새 도구 / 새 fixture / 새 docker block / CI workflow 변경 / runtime code 변경 / Operational Readiness PASS / Hermes PMO 격상) 8/8 답습. **R-4 + R-5 + R-7 본문 = 이미 구현되어 있음** — R-4 829 (3 file: `secret_scanner.py` 368 + `provider_import_scanner.py` 178 + `provider_url_scanner.py` 283) + R-5 35 (`.importlinter` 1 file) + R-7 328 (9 file: `docker/gp3-st3-poc/` 4 file 92 + `tools/docker_secret_image_layer_check.sh` 99 + `tools/docker_secret_restart_recovery.sh` 118 + `tests/fixtures/gp3_st3/` 3 file 18 + secrets/api_key.placeholder 1) = **합산 1192줄 (13 file) brief 명세 100% 일치 + 변경 0건 영구 답습**. **합산 12/12 Local 검증 PASS** — Phase α-1 R-4 = 8/8 (3 scanner × pass+fail × mode 분기 + 2 자기 검증) + Phase α-2 R-5 = INI 구조 8 항목 통합 PASS (sections + root_packages + include_external_packages + 4 contract 항목 + forbidden 4종 + ignore_imports 1종) + Phase α-3 R-7 = 3/3 (image layer clean + image layer leak + restart recovery sha256=`5529cec0...8aeb84be` 2회 일치). **변경 0건 검증**: `git status` clean + `git diff --stat` 0 + 8 금지 영역 위반 0/8 + R-4.1 Tier-1 45 / URL Tier-1 / Model Tier-1 / `.importlinter` forbidden 4 / include_external_packages / root_packages / ignore_imports / R-7 docker secret block / image layer check / restart recovery / Tier-2/3 자동 확장 / threshold 고정 / event enum 정식 등록 / facade real 본문 / ADR 갱신 / 신규 ADR / 외부 LLM / 실 API/SDK / 신규 actual run trigger 모두 0건. **5 영구 핵심 제약 5/5 보존** + **Provider Liquidity 5-way 100% 보존** + **F-금지 #1 영구 답습 (GitHub Actions secrets 사용 도입 0건)**. **합산 222 합의 조건 변경 0건** (Group α 12 + Backlog #6 11 + Phase α-1 15 + Phase α-2 26 + Phase α-3 28 + Layer C 30 + Layer D 25 + Stage 1 25 + Stage 2 25 + Stage 3 25) + ADR-011 §2.1 모법 변경 0건. **본 evidence 는 R-4 / R-5 / R-7 본문 어느 줄도 *수정* 시키지 않으며, 새 도구 / fixture / docker block 어느 것도 *추가* 시키지 않으며, CI workflow / runtime code 어느 것도 *변경* 시키지 않으며, Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 어느 것도 *발생시키지 않으며*, Phase α-4 / Phase β / γ 어느 것도 *자동 진입* 시키지 않으며, 새 합의 / 새 ADR / 새 P / 새 GP 어느 것도 *발행* 시키지 않는다**. 본 evidence 가 발생시키는 *유일한* 효과는 **2026-05-16 시점 Phase α-1 + α-2 + α-3 local 검증 결과 12/12 PASS 기록 한정**. 다음 단계는 사용자 명시 결정 영역 (옵션 1 ~ 13, §8 답습).
docs/phase0/w1-caveat-8-paths-filter-followup-brief.md:272:| 1 | `tools/secret_scanner.py` | Phase α-1 R-4 도구 본문 | Phase α-1 답습 영구 |
docs/phase0/mvp2-entry-eligibility-audit-brief.md:102:1. **R-4 / R-4.1 답습 책임 분담** — GP-2 의 송신 redaction = R-4.1 Tier-1 42 catalog 의 *런타임 적용* 영역. Group D PoC = *형식적 검출 layer 한정*. 실 송신 redaction = Hermes upstream 영역 (Group D PoC §1.2 #6 답습) + P1 facade RedactionFilter 본문 (Group D PoC §1.2 마지막 항목 답습).
docs/phase0/mvp2-entry-eligibility-audit-brief.md:124:| (a) | 동등 이상 보안 결과 | ✅ R-4 답습 (충족) — `redaction-pattern-equivalence.md` | Hermes native redaction Tier-1 42 catalog 적용 검증 evidence + P1 facade RedactionFilter 검증 evidence (둘 다 *실행* 시점 evidence 추가 수집) |
docs/phase0/mvp2-entry-eligibility-audit-brief.md:137:| **R-2** | P1 facade RedactionFilter | LLM API 진입점 redaction | 별도 layer | P1 v2 §8.2 답습 | MANDATORY (facade single entry point) |
docs/phase0/mvp2-entry-eligibility-audit-brief.md:140:| **R-5** | base64 / URL-encoded / 압축 evasion 별도 영역 | Hermes upstream R2-6 또는 P1 facade RedactionFilter 확장 | MVP-2/3 분리 영역 (G3-4 답습) | 본 cycle 범위 외 | 분리 영역 명시 |
docs/phase0/mvp2-entry-eligibility-audit-brief.md:247:| RT-2 | P1 facade RedactionFilter 우회 | LLM API request body 평문 secret 검출 | P1 v2 §8.2 + ADR-008 차단조건 #1 보조 |
docs/phase0/mvp2-entry-eligibility-audit-brief.md:261:| E-2 | P1 facade RedactionFilter 적용 검증 | facade 진입점 evidence (TR-1 (d) carry-over 의존) |
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:1:# SC-1 facade RedactionFilter (R-2 GP-2 prevention) 실 구현 brief (v1)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:5:> **scope** (사용자 명시 "RedactionFilter 집중"): **RedactionFilter 완전 구현 (secret_scanner Tier-1 45 catalog 재사용, R-2-c) + facade `complete()` 송신 전 redaction 적용 layer 통합**. **LiteLLM Router 위임 = deferred (Provider Liquidity 별도 sub-cycle)**. TDD 적용.
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:11:> **본 cycle 발효 효과** = R-2 facade RedactionFilter prevention layer **in-repo operative** + GP-2 (a) "facade redaction filter 검증" 충족 (full GP-2 PASS Exit (a)의 R-2 prong). **full GP-2 PASS 발효 = SC-2 (R-1 위임 검증) + SC-3 후 (별도)**.
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:13:> **선행 답습**: 64 trajectory entry brief (SC-1 정의 + R-2-a 동시 + R-2-c catalog 재사용 + RedactionFilter = facade 내부 협력자 + RT-1 atomic) + llm-providers-design §4.1/§8.2 (설계 명세) + ADR-009 §2.2 (facade 단일 진입점 의무) + secret_scanner Tier-1 45 catalog
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:21:1. **RedactionFilter 인터페이스 + catalog 재사용 (R-2-c) 설계 결정** (§2)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:36:| 5 | secret_scanner Tier-1 45 catalog **패턴 내용 변경** (R-4.1 답습 "변경 0건", R-7(b) 차등) | 0 |
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:45:- **llm-providers-design.md §8.2** (RedactionFilter 설계 — PATTERNS 4 + KEY_BLACKLIST 6, 블랙리스트 채택) + **§4.1** (facade `complete()` 흐름) + **§4.4** (호출 흐름 — redaction 적용 지점 step 5)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:48:- **secret_scanner.py** (Tier-1 45 catalog = baseline 5 + prefix 31 + regex 7 + alternation 2, `ALL_PATTERNS`/`COMPILED_PATTERNS`/`scan_text()`, 외부 의존성 0 stdlib)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:50:- **64 trajectory entry brief §4.4** (R-2-a/c 권고 + RedactionFilter = facade 내부 협력자 + RT-1 atomic)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:63:## §2 RedactionFilter 인터페이스 + catalog 재사용 (R-2-c) 설계 결정
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:67:secret_scanner Tier-1 45 catalog 재사용 (R-2-c, single source detection↔prevention) — import 경계 4 옵션:
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:71:| (i) src → tools.secret_scanner import | RedactionFilter가 `tools.secret_scanner.COMPILED_PATTERNS` import | 즉시 single source, 변경 0 | **src(런타임) → tools(개발도구) 역방향 의존** (아키텍처 부적절, .importlinter root=src 밖이라 미차단이나 nonidiomatic) |
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:72:| (ii) ⭐ catalog 공유 모듈 추출 | Tier-1 catalog를 `src/adapters/llm/redaction_patterns.py` (또는 공유 위치) 추출, secret_scanner + RedactionFilter 공유 | single source + 런타임 정합 | **secret_scanner 변경 = R-4.1 "변경 0건" 위반 = R-7(b) 차등 자격** (별도 평가) |
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:73:| (iii) RedactionFilter 자체 복제 | Tier-1 45 패턴 복사 | 경계 깔끔 | **중복 → detection↔prevention drift 위험** (single source 위반) |
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:74:| (iv) §8.2 자체 패턴 | RedactionFilter = §8.2 4 패턴 + 6 키 | 설계 명세 직접 답습 | Tier-1 45 catalog 미사용 (R-2-c 비채택, 커버리지 ↓) |
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:76:⭐ **권고 = (i) tools import (잠정) 또는 (ii) 공유 모듈 추출** — **풀 3+1 결정 대상**. (i) = 변경 0건 충실하나 의존 방향 / (ii) = 정합하나 secret_scanner 변경 R-7(b). **본 brief 권고 = (i) 우선** (변경 최소 + R-4.1 "변경 0건" 보존), (ii)는 의존 방향 BLOCKING 시 fallback.
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:78:### §2.2 RedactionFilter 인터페이스 (§8.2 답습)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:81:class RedactionFilter:
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:84:    def redact_messages(self, messages: list[dict]) -> list[dict]: ...  # 송신 request body redaction (GP-2 핵심)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:88:- 패턴 source = secret_scanner Tier-1 45 catalog (R-2-c, §2.1 결정 후).
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:89:- `[REDACTED]` 치환 (secret_scanner `is_redaction_marker_match` 답습 — redaction marker 정합).
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:97:- `complete(req)` 흐름에서 **Router 위임 *전*** `req.messages` (+ `system`)을 `redact_messages()` 통과 → secret strip 후 송신.
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:110:- `LLMFacade.__init__(registry_path)` → RedactionFilter 인스턴스 추가 (`self._redactor = RedactionFilter(...)`)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:112:  1. `redacted = self._redactor.redact_messages(req.messages)` (송신 전 redaction — GP-2 prevention operative)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:117:- 64 brief RT-1 = "facade real 후 RedactionFilter 미부착 window 금지 (atomic)".
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:118:- 본 cycle: **Router deferred = 실제 LLM 송신 0 = redaction 미부착 window 없음** (송신 자체가 deferred). RedactionFilter는 complete() 진입 시 부착 → Router 발효 (SC-Provider Liquidity) 시점에 이미 redaction layer 존재 (선부착).
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:134:- T-2: `redact_messages([{role, content: "key=sk-..."}])` → content redacted
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:142:- `src/adapters/llm/redaction.py` (RedactionFilter) + catalog 재사용 (§2.1 결정)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:154:- secret_scanner scan-source (src + .github, violations 0)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:186:- RedactionFilter = facade 내부 협력자 (provider-agnostic, 모델명 분기 0).
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:193:§0.2 답습 (10). 추가: LiteLLM 설치 0 / Router 위임 구현 0 / secret_scanner 패턴 변경 0 / litellm import 0 / full facade real 표현 0 / full GP-2 PASS 발효 0 / 자동 SC-2/SC-3 진입 0.
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:205:| RT-5 | redaction 성능 (매 송신 45 패턴 매칭) | COMPILED_PATTERNS 재사용 (사전 compile) |
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:214:- E-4: secret_scanner scan-source violations 0
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:226:| P-4 | secret_scanner 변경 (R-4.1 위반) | §0.2 #5 — 패턴 변경 0 (재사용만) |
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:235:**다음 단계**: 사용자 승인 → 풀 3+1 + 외부 LLM 1+ (codex E-α, TR-1) → Reviewer 통합 → (필요시 v1.1 흡수) → **TDD 구현 (RED→GREEN→REFACTOR)** → verify → commit + push → **R-2 facade RedactionFilter prevention layer in-repo operative**. 후속: SC-2 (R-1 위임 검증) / SC-3 (full GP-2 PASS 발효) / SC-Provider Liquidity (Router 위임) = 사용자 명시 별도 sub-cycle.
docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md:12:> - `docs/decisions/ADR-012-evidence-ledger-protection.md` (Evidence Ledger 보호 — secret_scanner 결과 evidence summary 형식)
docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md:25:- **D-1 (GP-3)** = code-side secret 검출만 (`tools/secret_scanner.py --mode scan-source`). Hermes 컨테이너 *저장 경로* (chmod 600 / entrypoint stat / inotify — R1-2) = **Hermes upstream 영역**, 본 PoC 미진입.
docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md:26:- **D-2 (GP-2)** = redaction 후 *잔존 secret 검증* 만 (`tools/secret_scanner.py --mode scan-log`). Hermes native `agent/redact.py` 본 호출 = **Hermes upstream 영역**. 본 PoC = *contract 검증* (R-4.1 Tier-1 42 catalog 패턴이 redacted output 에 잔존 시 FAIL).
docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md:41:| Validator | `tools/secret_scanner.py` | 단일 도구 + 2 mode (scan-source / scan-log) + 45 patterns (R-4.1 Tier-1 catalog 직접 답습 — Prefix 36 + regex 7 + alternation 2) + violation reporter |
docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md:70:| LLM API request body 실 송신 redaction | P1 facade RedactionFilter — 별도 합의 |
docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md:156:**예상**: `secret_scanner --mode scan-source pass/` → rc=0 + 위반 0건 (FP 0).
docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md:169:**예상**: `secret_scanner --mode scan-source fail/` → rc=1 + ≥4 violations + 4 패턴 cover 검증.
docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md:177:**예상**: `secret_scanner --mode scan-log redaction_pass/` → rc=0 + 잔존 0건.
docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md:200:| 1 | D-1 PASS scan | `pass/` | `python tools/secret_scanner.py --mode scan-source tests/fixtures/secret_hygiene/pass/` | 0 | 위반 0건 (FP 0) |
docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md:201:| 2 | D-1 FAIL scan | `fail/` | `python tools/secret_scanner.py --mode scan-source tests/fixtures/secret_hygiene/fail/` | 1 | ≥4 violations + 4 패턴 cover (prefix / regex / alternation / private-key) |
docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md:202:| 3 | D-2 PASS redaction residual scan | `redaction_pass/` | `python tools/secret_scanner.py --mode scan-log tests/fixtures/secret_hygiene/redaction_pass/` | 0 | 잔존 0건 |
docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md:203:| 4 | D-2 FAIL redaction leak scan | `redaction_fail/` | `python tools/secret_scanner.py --mode scan-log tests/fixtures/secret_hygiene/redaction_fail/` | 1 | partial leak 검출 (base64 미검출 = known limitation) |
docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md:204:| 5 | Tier-1 pattern count 자기 검증 | `--list-patterns` | `python tools/secret_scanner.py --list-patterns` | 0 | `registered_patterns_count` ≥ 42 (R-4.1 답습) + Tier-1 prefix 31 + regex 7 + alternation 2 enumerate |
docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md:267:| 6 | LLM API request body 실 송신 redaction | P1 facade RedactionFilter | 별도 합의 |
docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md:296:| 4 | D-1 PASS — secret_scanner --mode scan-source pass/ | rc=0 + 위반 0건 grep |
docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md:297:| 5 | D-1 FAIL — secret_scanner --mode scan-source fail/ | rc=1 + ≥4 violations + 4 패턴 cover grep (prefix / regex / alternation / private-key) |
docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md:298:| 6 | D-2 PASS — secret_scanner --mode scan-log redaction_pass/ | rc=0 + 잔존 0건 grep |
docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md:299:| 7 | D-2 FAIL — secret_scanner --mode scan-log redaction_fail/ | rc=1 + partial leak 검출 grep (base64 미검출 = known limitation) |
docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md:312:  - tools/secret_scanner.py
docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md:340:| JSONL ledger entry | secret_scanner 결과 evidence summary (옵션, ADR-012 §2.9 답습 — 본 PoC 미강제) | summary.json (단순화) |
docs/phase0/mvp1-secret-scanner-docs-scope-policy-brief.md:15:| **현 `.pre-commit-config.yaml` secret-scanner hook entry** | `.pre-commit-config.yaml` line 답습 | `for d in src .github; do python3 tools/secret_scanner.py --mode scan-source "$d" || exit 1; done` (hardcoded scope) |
docs/phase0/mvp1-secret-scanner-docs-scope-policy-brief.md:16:| **현 `tools/secret_scanner.py`** | 47 entry secret_scanner.py 답습 유지 | `SCAN_SOURCE_EXTENSIONS` 에 `.md` 포함 = docs/ markdown 모두 scan 대상 자격 (기술적) |
docs/phase0/mvp1-secret-scanner-docs-scope-policy-brief.md:35:- `python3 tools/secret_scanner.py --mode scan-source docs` = **~800+ violations** 검출
docs/phase0/mvp1-secret-scanner-docs-scope-policy-brief.md:73:| `tools/secret_scanner.py` 주석 1~2줄 (정책 문서 cross-reference) | ✅ comment 추가 (code 본문 변경 0) |
docs/phase0/mvp1-secret-scanner-docs-scope-policy-brief.md:137:4. ⏳ `.pre-commit-config.yaml` + `tools/secret_scanner.py` 주석 추가
docs/phase0/phase-alpha-1-r4-tools-body-entry-brief.md:30:2. **R-4 영역 = 3 도구 (`secret_scanner.py` + `provider_import_scanner.py` + `provider_url_scanner.py`) 정의** + 현 상태 enumeration (§2)
docs/phase0/phase-alpha-1-r4-tools-body-entry-brief.md:43:- ❌ **실 runtime code 구현 (0건)** — `tools/secret_scanner.py` / `tools/provider_import_scanner.py` / `tools/provider_url_scanner.py` 본문 변경 / 추가 / 삭제 0건
docs/phase0/phase-alpha-1-r4-tools-body-entry-brief.md:87:- (v) R-4 도구 본문 (`tools/secret_scanner.py` / `tools/provider_import_scanner.py` / `tools/provider_url_scanner.py`) 어느 줄도 *변경* 하지 않으며,
docs/phase0/phase-alpha-1-r4-tools-body-entry-brief.md:103:| Phase α-1 정의 (합의 §5.2 답습) | R-4 도구 본문 (Stage 1 + Stage 3) — Stage 1 (S-1 `secret_scanner.py`) + Stage 3 (T-6 `provider_import_scanner.py` + `provider_url_scanner.py`) 병렬 진입 적격 |
docs/phase0/phase-alpha-1-r4-tools-body-entry-brief.md:164:| `tools/secret_scanner.py` | GP-3 S-1 — 코드 본문 secret 검출 (R-4.1 Tier-1 45 patterns) | Group D PoC (`docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md`) 답습 | 368 | Stage 1 |
docs/phase0/phase-alpha-1-r4-tools-body-entry-brief.md:174:| S-1 | 코드 본문 secret 검출 (R-4.1 Tier-1 45 patterns) | Group D PoC 답습 | `secret_scanner.py` |
docs/phase0/phase-alpha-1-r4-tools-body-entry-brief.md:195:### 3.1 Stage 1 — `secret_scanner.py` (S-1) sub-step 분할 (Layer B §2.2.1 답습)
docs/phase0/phase-alpha-1-r4-tools-body-entry-brief.md:225:| Stage 1 | `secret_scanner.py` | 4 | 中 (CI 통합 인터페이스 + ledger 형식) | 高 (Group D 답습) | enumerate 한정 |
docs/phase0/phase-alpha-1-r4-tools-body-entry-brief.md:242:| `tools/secret_scanner.py` 본문 변경 | ❌ (영역 외) | Phase α-1 실 진입 후 영역 |
docs/phase0/phase-alpha-1-r4-tools-body-entry-brief.md:352:| R-MVP1-G3-1 | S-1 FP_rate 폭증 (>5%) | `secret_scanner.py` 본문 영향 | 의존성 *enumerate 한정* (발화 0건) |
docs/phase0/phase-alpha-1-r4-tools-body-entry-brief.md:355:| R-MVP1-G3-4 | PC-3 CI runtime 폭증 (>2분) | `secret_scanner.py` 성능 영향 | 의존성 *enumerate 한정* (발화 0건) |
docs/phase0/phase-alpha-1-r4-tools-body-entry-brief.md:357:| R-MVP1-G3-6 | R-4.1 Tier-1 catalog 변경 | `secret_scanner.py` 본문 영향 | 영역 외 (Backlog #3 별도 합의) |
docs/phase0/phase-alpha-1-r4-tools-body-entry-brief.md:358:| R-MVP1-G3-7 | Tier-2 확장 필요 | `secret_scanner.py` 본문 영향 | 영역 외 (Backlog #1 1.5차 보강) |
docs/phase0/phase-alpha-1-r4-tools-body-entry-brief.md:410:| 13 | R-4 도구 본문 (`secret_scanner.py` / `provider_import_scanner.py` / `provider_url_scanner.py`) 어느 줄도 변경 | 0건 |
docs/phase0/phase-alpha-1-r4-tools-body-entry-brief.md:545:본 brief 는 **Backlog #6 Runtime + CI-hook 우선 진입 합의 (`c7ddfdd` APPROVE AS BRIEF, Reviewer-only 단축) 발효 후속**, 합의 §6.1 1순위 (Phase α-1 + α-2 + α-3 병렬 진입 적격) 中 **Phase α-1 = R-4 도구 본문 영역 *진입 가능성 검토 한정* 준비안 (DRAFT)** 이다. **사용자 명시 7 금지** (실 runtime code 구현 / CI workflow 변경 / branch protection 변경 / dev 환경 강제 / `pre-commit install` 의무화 / Operational Readiness PASS / Hermes PMO 격상) 7/7 답습. **R-4 = 3 도구 정의** (`tools/secret_scanner.py` Group D 368줄 답습 / `tools/provider_import_scanner.py` Group A 1차 178줄 답습 / `tools/provider_url_scanner.py` Group A 3차 283줄 답습 — 합산 829줄 PoC 답습 변경 0건) + **3 도구 × Phase α-1 본문 작업 후보 분할 매트릭스** (Stage 1 4 sub-step + Stage 3 T-2 3 sub-step + Stage 3 T-5 4 sub-step = 11 sub-step) + **7 금지 영역 × R-4 분리 매트릭스** (7/7 분리 — 충돌 0) + **Phase α-1 진입 적격성 5 조건 검토** (C-α1-1 7 금지 충돌 0/7 + C-α1-2 PoC 답습 100% 보존 + C-α1-3 의존성 0 병렬 진입 적격 + C-α1-4 Provider Liquidity 5-way 100% 보존 + C-α1-5 5 영구 핵심 제약 5/5 보존 = 5/5 충족) + **8 풀 3+1 승격 트리거 0/8 발화** + **R-4 영역 영향 Rollback Trigger 의존성 답습** (18 trigger 中 R-4 직접 영향 5 + 간접 영향 3 + 영향 0 10 — 발화 0건) + **본 brief 자체 금지 37 + Phase α-1 실 진입 단계 금지 17** + **합의 형태 권고** (Reviewer-only 단축 — 8/8 트리거 0건 발화) 를 정리한다. **본 brief 는 Phase α-1 실 진입을 *시작* 시키지 않으며, R-4 도구 본문 어느 줄도 *변경* 하지 않으며, 7 금지 영역 *해소* / Layer C 발효 / MVP-1 PASS / Operational Readiness PASS / Hermes PMO 격상 / Group α 합의 본문 변경 / 14 결정 영역 *재결정* / Phase α-2 / α-3 / α-4 자동 진입 / 합의 보고서 작성 / 메타 갱신 / commit / push 모두 본 brief 영역 외**. 다음 단계는 사용자 명시 결정 영역 (옵션 A~J, §9 답습).
docs/phase0/phase-alpha-1-r4-tools-body-entry-brief.md:564:- ❌ R-4 도구 본문 (`secret_scanner.py` / `provider_import_scanner.py` / `provider_url_scanner.py`) 어느 줄도 변경
docs/phase0/phase-alpha-2-r5-importlinter-body-entry-brief.md:60:- ❌ **R-4 도구 본문 변경 (0건)** — Phase α-1 R-4 영역 (`tools/secret_scanner.py` / `tools/provider_import_scanner.py` / `tools/provider_url_scanner.py`) 본문 변경 모두 0건 (Phase α-1 = 별도 영역)
docs/phase0/phase-alpha-2-r5-importlinter-body-entry-brief.md:285:| 도구 | T-5 (custom AST scanner) — 3 도구 (`secret_scanner.py` + `provider_import_scanner.py` + `provider_url_scanner.py`) | T-2 (import-linter) — `.importlinter` config |
docs/phase0/phase-alpha-2-r5-importlinter-body-entry-brief.md:483:| 11 | R-4 도구 본문 (`secret_scanner.py` / `provider_import_scanner.py` / `provider_url_scanner.py`) 변경 | 0건 |
docs/phase0/mvp1-pc1-d6-false-positives-correction-brief.md:15:| **secret-scanner Tier-1 catalog** | `tools/secret_scanner.py` line 153~159 (ALTERNATION_PATTERNS 2건) | T1-041 = `(?i)(?:access_token\|refresh_token\|id_token\|token\|api_key\|apikey\|client_secret\|password\|auth\|jwt\|session\|secret\|key\|code\|signature\|x-amz-signature)=[^&\s]+` / T1-042 = `(?i)(?:access_token\|refresh_token\|id_token\|token\|api_key\|apikey\|client_secret\|password\|auth\|jwt\|secret\|private_key\|authorization\|key)=[^&\s]+` |
docs/phase0/mvp1-pc1-d6-false-positives-correction-brief.md:57:# tools/secret_scanner.py line 154~159
docs/phase0/mvp1-pc1-d6-false-positives-correction-brief.md:139:| **⭐ (a) word boundary 추가** | T1-041/T1-042 alternation 직전 `[?&]\|^\|\s` prefix 추가 → URL query/body 컨텍스트 한정 | `tools/secret_scanner.py` line 155~158 본문 변경 (3~6 줄) | G3 R-4.1 Tier-1 catalog 본문 = 권위 라인 (단, 결함 정정 = R-MVP1-PASS-2 자격 영향 없음, ADR-008 본문 변경 0) + Hermes upstream 답습 본질 유지 (key 목록 보존, prefix 만 추가) | T1-038/T1-040 canary 차단 cover 유지 (T1-038 = `?api_key=...` → `?` prefix 매칭 / T1-040 = line start → `^\|\s` 매칭) | **풀 3+1 + 외부 LLM 1+** (R-7(b) PC1-2 차등 답습 — alternation 패턴 본문 변경 = catalog 영역) + T1-038/T1-040 canary 재발화 evidence 의무 | **⭐ 신 1차 권고 (사용자 D-FP-1 채택)** |
docs/phase0/mvp1-pc1-d6-false-positives-correction-brief.md:142:| (d) | secret_scanner.py 에 SAFE_CONTEXT (Python AST context) 추가 — function call keyword arg 자동 skip | `tools/secret_scanner.py` 본문 변경 (large diff, ast import + check 추가) | G3 PoC 본문 변경 (24~50 줄 추가) + Hermes 답습 유지 | Hermes pattern cover 보존 + Python source code 정밀 분리 | 풀 3+1 (도구 본문 변경, 복잡도 증가) | △ (큰 cycle, 향후 영구 정밀화 carry-over 자격) |
docs/phase0/mvp1-pc1-d6-false-positives-correction-brief.md:143:| (e) | scan-source mode에서 `.py` extension에 alternation 패턴 skip — `SCAN_SOURCE_EXTENSIONS` 분리 또는 alternation context별 file ext filter | `tools/secret_scanner.py` 본문 변경 (5~15 줄) | G3 PoC 본문 변경 | `.py` 의 실제 URL query string 패턴도 skip = FN risk (단, `.py` 내 URL hardcoding 자체가 R-MVP1-PASS-9 영향 가능성 = anti-pattern) | 풀 3+1 (Hermes 답습 scope 변경) | △ (scope 좁힘, 검토 의무) |
docs/phase0/mvp1-pc1-d6-false-positives-correction-brief.md:149:**현 패턴 (tools/secret_scanner.py line 155~158)**:
docs/phase0/mvp1-pc1-d6-false-positives-correction-brief.md:263:| **D-FP-4** | 회귀 verification 범위 | (1) 본 D-6 workflow re-run + `secret-scanner` PASS verify / (2) `tools/secret_scanner.py` self-test + T1-038/T1-040 canary 재발화 PASS / (3) jarvis 144/144 pytest green 답습 보존 (src/ 본문 변경 0 영역 = 영향 0 예상, 단 secret_scanner.py 자체는 jarvis 의존 0 = 영향 0) |
docs/phase0/phase-alpha-4-r1-entry-condition-check-brief.md:220:| `.github/workflows/secret-hygiene-egress-redaction.yml` (694줄) | Stage 1 R-4 secret_scanner step + Stage 2 R-7 docker check step + Stage 4 integration step | R-4 `tools/secret_scanner.py` (368줄, R-4.1 Tier-1 45 patterns) + R-7 `docker/gp3-st3-poc/` 4 file (92줄) + R-7 `tools/docker_secret_image_layer_check.sh` (99줄) + R-7 `tools/docker_secret_restart_recovery.sh` (118줄) + R-7 `tests/fixtures/gp3_st3/` 3 file (18줄) | α-1 R-4 8/8 PASS (3.1.1~3.1.2) + α-3 R-7 3/3 PASS (3.3.1~3.3.3) — **합산 11/11 PASS** ✅ | **연결 충족** — workflow 가 호출하는 도구 / fixture / docker block 모두 local 12/12 PASS evidence 답습 |
docs/phase0/phase-alpha-4-r1-entry-condition-check-brief.md:234:| **AR-1 (CI step fail-closed = PR auto-reject)** | T2 영역 + 양 GP 공유 채택 — `exit 1` propagation + `${{ failure() }}` 패턴 | R-4 / R-5 / R-7 도구 본문이 local FAIL fixture 5/5 검출 (R-4.1.2 secret_scanner FAIL + 2.2 provider_import_scanner FAIL + 3.2 provider_url_scanner url FAIL + 3.4 model-name FAIL + R-7 4.2 docker layer leak FAIL) = **CI step 의 fail-closed 정합성 = local evidence 답습** → AR-1 정합성 강화 |
docs/phase0/phase-alpha-4-r1-entry-condition-check-brief.md:241:| Phase α-1 R-4 | 도구 본문 (`secret_scanner.py` + `provider_import_scanner.py` + `provider_url_scanner.py`) | actual run PASS 선행 evidence (`25728590939` + `25728590916` + `25728590977`) 답습 | **+ local 8/8 PASS evidence 답습 추가 확정** (α-1+2+3 evidence §3.1) |
docs/phase0/phase-alpha-4-r1-entry-condition-check-brief.md:517:본 brief 는 **Phase α-1 + α-2 + α-3 Local Validation Evidence (`68d010a` HEAD, 2026-05-16 후속 22, 486줄, 12/12 PASS — Phase α-1 R-4 8/8 + Phase α-2 R-5 INI 구조 8 항목 + Phase α-3 R-7 3/3, 13 file × 1192줄 본문 변경 0건) 발효 후속**, 사용자 명시 진입 명령 답습 — **Phase α-4 (R-1 CI workflow 통합 = PC-3 + AR-1) *진입 조건 점검 한정* 의 brief 준비안 (DRAFT)**. **사용자 명시 5 금지** (CI workflow 변경 / runtime code 변경 / actual run 재실행 / Operational Readiness PASS / Hermes PMO 격상) 5/5 답습. **직전 Phase α-4 R-1 진입 brief (`f91ef4b`, 751줄) + 직전 α-4 합의 (`e59a565` APPROVE AS BRIEF, 29 조건 C-ε-1 ~ C-ε-29) 변경 0건 + α-1+2+3 evidence 발효 영향 *enumerate 한정***. **R-1 영역 = 3 MVP-1 workflow (`secret-hygiene-egress-redaction.yml` 694 + `provider-adapter-enforcement.yml` 186 + `provider-url-scanner.yml` 326 = 1206줄) + integration tool (`tools/mvp1_pc3_ar1_integration_check.py` 298줄) + integration fixture (`tests/fixtures/mvp1_pc3_ar1_integration/` 3 파일 89줄) = **7 artifacts × 1593줄 본문 답습 변경 0건**. **PC-3 + AR-1 양 GP 공유 답습 채택** (Layer B §5.5.1 + §5.5.2 sub-step 4.1 + 4.2 한정) + **PC-4 / AR-2 / AR-3 / Stage 5 분리** (sub-step 4.3 / 4.4 / Backlog #3 / Stage 4 후속 권고 분리 명시) + **3 MVP-1 workflow 한정 답습** (G2/G3/G4 PoC 8 workflow 분리). **R-1 ↔ α-1+2+3 evidence 연결 매트릭스** (§2): workflow 가 호출하는 도구 (`secret_scanner.py` 368 + `provider_import_scanner.py` 178 + `provider_url_scanner.py` 283 + `.importlinter` 35 + docker block 4 file 92 + `docker_secret_image_layer_check.sh` 99 + `docker_secret_restart_recovery.sh` 118 + `tests/fixtures/gp3_st3/` 18) = R-4/R-5/R-7 합산 **1192줄 + local 12/12 PASS evidence 답습** → PC-3 (exit 0/1 정합성) + AR-1 (fail-closed 정합성) 의미적 강화 (단, 실 actual run 재실행 0건). **5 진입 적격성 조건 (C-α4-1 ~ C-α4-5) 재검토 5/5 충족** — 특히 **C-α4-3 = 의존성 *이중 evidence 충족*** (직전 시점 4 prerequisite runs PASS actual run evidence + 본 brief 시점 추가 local 12/12 PASS evidence 답습) + **C-α4-2/4/5 = 답습 강화 (α-1+2+3 evidence §5/§6 답습)**. **15/15 풀 3+1 승격 트리거 0건 발화** (직전 14 + 본 brief 신규 #15 미발화) → **Reviewer-only 단축 합의 적격 후보 확정**. **5 영구 핵심 제약 5/5 보존** (Hermes ≠ root of trust / 단일 source-of-truth / 수단/목적 분리 / T1/T2/T3 분리 / SPOF 의도적 수용) + **Provider Liquidity 5-way 100% 보존** (R-1 = CI integration Layer = catalog / provider 영역과 직교, CI workflow = vendor-agnostic 표준 GitHub Actions) + **F-금지 #1 영구 답습** (GitHub Actions secrets 사용 도입 0건). **합산 251 합의 조건 변경 0건** (Group α 12 + Backlog #6 11 + Phase α-1 15 + Phase α-2 26 + Phase α-3 28 + **Phase α-4 29** + Layer C 30 + Layer D 25 + Stage 1 25 + Stage 2 25 + Stage 3 25). **본 brief 는 Phase α-4 실 진입을 *시작* 시키지 않으며, 합산 251 합의 조건 어느 것도 *해소* 시키지 않으며, 사용자 명시 5 금지 영역 어느 것도 *해소* 시키지 않으며, R-1 영역 본문 (1593줄, 7 artifacts) 어느 줄도 *변경* 하지 않으며, R-4 / R-5 / R-7 본문 (1192줄, 13 file) 어느 줄도 *변경* 하지 않으며, `src/` runtime code / facade.py placeholder 어느 줄도 *변경* 하지 않으며, PC-4 / AR-2 / AR-3 / Stage 5 / Layer E / Layer F 어느 영역도 *진입* 시키지 않으며, Phase α-1 / α-2 / α-3 actual run 어느 것도 *자동 재실행* 시키지 않으며, 합의 보고서 / 새 합의 / 새 ADR / 새 P / 새 GP 어느 것도 *발행* 시키지 않는다**. 본 brief 가 발생시키는 *유일한* 효과는 **Phase α-4 R-1 CI workflow 통합 영역의 *진입 조건 점검 권위 권고 한정* — α-1+2+3 evidence 발효 후속 PC-3 + AR-1 연결 매트릭스 + 직전 α-4 합의 29 조건 답습 + 진입 적격성 5 조건 재검토 + 5 금지 분리 매트릭스 + 다음 단계 권고**. 다음 단계 = **사용자 결정 영역** (자동 진입 0건) — (A) 본 brief 그대로 승인 → Reviewer-only 단축 합의 (권고 시작점) / (B) brief 수정 요청 / (C) Phase α-4 실 진입 step 분할 brief / (D) Phase α-4 실 진입 / (E)~(N) 별도 backlog/MVP 영역 / (O) 세션 종료.
docs/phase0/phase-alpha-123-parallel-implementation-brief.md:57:  - R-4: `tools/secret_scanner.py` (368) + `tools/provider_import_scanner.py` (178) + `tools/provider_url_scanner.py` (283) = 829줄 답습
docs/phase0/phase-alpha-123-parallel-implementation-brief.md:352:| S-1 secret scanner | `tools/secret_scanner.py` | 368 | (i) 답습 검증 한정 (변경 0건) / (ii) minor 인터페이스 정렬 (CLI 인자 / exit code / 출력 포맷) — *사용자 명시 결정 영역* |
docs/phase0/phase-alpha-123-parallel-implementation-brief.md:431:| `tests/fixtures/secret_scanner/{pass,fail}/` (S-1) | Group D PoC fixture | 답습 검증 한정 |
docs/phase0/phase-alpha-123-parallel-implementation-brief.md:465:| α-1 (R-4) | 3 도구 fixture (Group D + Group A 1차 + 3차) | `secret_scanner.py` / `provider_import_scanner.py` / `provider_url_scanner.py` dry-run | `25728590939` + `25728590916` + `25728590977` (재실행 0건) | minor 인터페이스 정렬 시 재실행 결정 |
docs/phase0/phase-alpha-4-r1-stage4-entry-brief.md:319:| R-4 = `tools/secret_scanner.py` 등 (Phase α-1 영역) | 1192줄 합산 13 file | **0건** | **0건 영구 답습** (Phase α-1 영역 분리) |
docs/phase0/backlog3-t3-zone-full-3plus1-brief-v2.md:74:| (추가) | `tools/secret_scanner.py` / `tools/provider_*.py` 본문 변경 | 0건 |
docs/phase0/mvp1-gp3-gp5-current-state-audit-brief.md:27:| `secret_scanner.py` (368줄) | GP-3 S-1 (coverage 기반 코드 본문 secret 검출) | 실 구현 |
docs/phase0/mvp1-gp3-gp5-current-state-audit-brief.md:103:| (a) | 동등 이상의 보안 결과 | ✅ Tier-1 42 catalog 답습 + secret_scanner.py 실 구현 | ✅ Tier-1 URL 10 + Model 19 + provider_import/url_scanner 실 구현 |
docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md:39:| 3 | tools/ 본문 변경 (secret_scanner / workflow_secrets_usage_check / 등) | 0건 |
docs/phase0/mvp1-s3-detect-secrets-partial-integration-brief.md:18:| **secret_scanner.py (S-1)** | `tools/secret_scanner.py` (368줄, Tier-1 45 patterns) | S-3 = *추가* layer (S-1 답습 유지, 미대체, Defense in depth) |
docs/phase0/mvp1-s3-detect-secrets-partial-integration-brief.md:32:| **변경 0건 의무** | `tools/secret_scanner.py` 본문 변경 0건 (S-1 답습 유지) / `.pre-commit-config.yaml` 본문 변경 0건 / src/ 0건 / ADR 0건 / 헌법 0건 / roadmap 본문 0건 / Tier-2/3 catalog 0건 (Tier-1 답습 plugin 한정) / baseline file 영구 금지 |
docs/phase0/mvp1-s3-detect-secrets-partial-integration-brief.md:39:| 1 | `tools/secret_scanner.py` 본문 변경 (S-1 답습 유지) | 0건 (R-MVP1-1.5-S3-3 영구 금지 답습 — Defense in depth) |
docs/phase0/mvp1-s3-detect-secrets-partial-integration-brief.md:84:| `tools/secret_scanner.py` (S-1, 368줄, Tier-1 45 patterns) | ✅ 발효 (Group D PoC) | R-MVP1-1.5-S3-3 답습 유지 의무 (Defense in depth) |
docs/phase0/mvp1-s3-detect-secrets-partial-integration-brief.md:102:| 항목 | S-1 (`tools/secret_scanner.py`) | S-3 (`detect-secrets`) |
docs/phase0/mvp1-s3-detect-secrets-partial-integration-brief.md:234:| **R-MVP1-1.5-S3-3** | S-1 (`tools/secret_scanner.py`) 답습 step 제거 / 대체 시도 | **영구 금지** (Defense in depth 답습) |
docs/phase0/mvp1-s3-detect-secrets-partial-integration-brief.md:255:| **D-2** | workflow step 위치 | (i) `Tier-1 pattern count` step 직후 (line 97) / (ii) 마지막 `MVP-1 entry secret_scanner coverage check` step 직후 (line 287) / (iii) 신규 별도 job | **(ii) MVP-1 entry step 직후** — S-1 답습 step 들 모두 통과 후 S-3 추가 layer (Defense in depth 답습 순서) |
docs/phase0/mvp1-s3-detect-secrets-partial-integration-brief.md:272:| **변경 0건 의무** | `tools/secret_scanner.py` (S-1) / `.pre-commit-config.yaml` / src / 기존 tools 21 도구 본문 모두 0건. 변경 = `requirements-dev.txt` + workflow step + testfile + (선택) wrapper 한정 |
docs/phase0/mvp1-s3-detect-secrets-partial-integration-brief.md:293:| 2 | `tools/secret_scanner.py` (S-1) 답습 유지 명문 (R-MVP1-1.5-S3-3 영구 금지) | ✅ §1.2 #1 + §3.3 |
docs/phase0/phase-alpha-integrated-implementation-plan-brief.md:66:  - R-4: `tools/secret_scanner.py` (368) + `tools/provider_import_scanner.py` (178) + `tools/provider_url_scanner.py` (283) = 829줄 답습
docs/phase0/phase-alpha-integrated-implementation-plan-brief.md:258:| **α-1 (R-4)** | 3 도구 본문 | 3 file | **829** | Group D PoC + Group A 1차 + Group A 3차 | S-1 (`secret_scanner.py` 368) + T-2 (`provider_import_scanner.py` 178) + T-5 (`provider_url_scanner.py` 283) |
docs/phase0/phase-alpha-integrated-implementation-plan-brief.md:358:| Stage 1 | `secret_scanner.py` | 1.1 | 본문 답습 검증 (368줄) | Group D PoC §2.1 (A) | enumerate 한정 |
docs/phase0/phase-alpha-integrated-implementation-plan-brief.md:359:| Stage 1 | `secret_scanner.py` | 1.2 | MVP-1 entry CI 통합 인터페이스 정렬 (CLI / exit code / 출력 포맷 답습 검증) | Group D 12 step + Layer B §1.1 | 실 workflow 변경 = R-1 영역 (Phase α-4) |
docs/phase0/phase-alpha-integrated-implementation-plan-brief.md:360:| Stage 1 | `secret_scanner.py` | 1.3 | ledger entry 형식 (`event: secret_scan_layer1_implementation` 후보 한정) | mvp1.md §5.2 enum 후보 | 정식 등록 0건 (Backlog #5 분리) |
docs/phase0/phase-alpha-integrated-implementation-plan-brief.md:361:| Stage 1 | `secret_scanner.py` | 1.4 | Evidence Artifact 형식 (Markdown report 출력 후보) | Layer B §1.8 (a) | 실 생성 = Layer C 시점 (이미 완) |
docs/phase0/backlog1-2-pc4-t2-c5c-c6-satisfaction-brief.md:19:- 도구 검증 답습: `tools/secret_scanner.py` (Group D `25623028888`) / `tools/provider_import_scanner.py` (Group A 1차) / `tools/provider_url_scanner.py` (Group A 3차 `25629390384`) / `lint-imports` + `.importlinter` (Group A 2차 `25605665191`)
docs/phase0/backlog1-2-pc4-t2-c5c-c6-satisfaction-brief.md:57:| (추가) | 도구 본문 (`tools/secret_scanner.py` / `tools/provider_*.py` / `tools/workflow_*.py`) 변경 | 0건 |
docs/phase0/backlog1-2-pc4-t2-c5c-c6-satisfaction-brief.md:441:- ❌ 도구 본문 (`tools/secret_scanner.py` / `tools/provider_import_scanner.py` / `tools/provider_url_scanner.py` / `tools/workflow_secrets_usage_check.py` / `tools/workflow_permissions_check.py`) 변경 0건
docs/phase0/phase-alpha-4-r1-ci-workflow-integration-entry-brief.md:21:- `docs/architecture/implementation-runtime-roadmap-mvp1.md` §3.4.1 (G3-2 secret_scanner CI 통합) + §4.3 (GP-5 PC-3 CI-only enforcement) + §4.4 (GP-5 AR-1 PR auto-reject) + §5.4 (GP-3 + GP-5 Integrated Risk Matrix IR-1/IR-2/IR-3) + §5.5.1 PC-3 + AR-1 본문 채택 (commit `55c5b4b`)
docs/phase0/phase-alpha-4-r1-ci-workflow-integration-entry-brief.md:76:- ❌ **R-4 도구 본문 변경 (0건)** — Phase α-1 R-4 영역 (`tools/secret_scanner.py` / `tools/provider_import_scanner.py` / `tools/provider_url_scanner.py`) 본문 변경 모두 0건 (Phase α-1 = 별도 영역, `1b3090b` 합의 답습)
docs/phase0/phase-alpha-4-r1-ci-workflow-integration-entry-brief.md:265:| Phase α-1 R-4 | 도구 본문 (`tools/secret_scanner.py` + `provider_import_scanner.py` + `provider_url_scanner.py`) | Phase α-4 = α-1 actual run PASS 선행 evidence 의존 (run_id `25728590939` + `25728590916` + `25728590977` 후속 — `72622409` 기준 — 답습 완료) |
docs/phase0/mvp1-pc1-d6-fp-edge-extensions-brief.md:17:| **secret_scanner.py 현 상태** | `tools/secret_scanner.py` line 155~158 (42 entry 정정 답습) | T1-041/T1-042 prefix `(?:^|[?&\s'\"])` 발효 |
docs/phase0/mvp1-pc1-d6-fp-edge-extensions-brief.md:31:| 변경 영역 | `tools/secret_scanner.py` line 155~158 (2 line prefix character class 확장) |
docs/phase0/mvp1-pc1-d6-fp-edge-extensions-brief.md:167:4. ⏳ 실 구현 (`tools/secret_scanner.py` line 155~158 prefix `[?&\s'\";#]` 확장)
docs/phase0/backlog6-runtime-ci-hook-priority-entry-brief.md:49:- ❌ **실 runtime code 구현 (0건)** — `tools/secret_scanner.py` / `tools/provider_import_scanner.py` / `tools/provider_url_scanner.py` / `src/adapters/llm/facade.py` / inotify sidecar / chmod 600 entrypoint script 본문 *0건*
docs/phase0/backlog6-runtime-ci-hook-priority-entry-brief.md:174:| **R-4 도구 본문 (tools/*.py)** | `tools/secret_scanner.py` (Group D 261줄 답습) / `tools/provider_import_scanner.py` (Group A 1차 답습) / `tools/provider_url_scanner.py` (Group A 3차 답습) | Layer B §5.5 + backlog6-implementation-step-brief §4.3 답습 |
docs/phase0/phase-alpha-4-r1-stage4-w4-trigger-brief.md:287:| 1 | `25728590939` | `secret-hygiene-egress-redaction.yml` (Phase α-1 R-4 — secret_scanner 도구 본문) | 2026-05-16 (α-1+2+3 parallel actual entry) | **SUCCESS** ✅ | jobs.conclusion=success | group-d-logs |
docs/phase0/phase-alpha-4-r1-stage4-w4-trigger-brief.md:995:**4 prerequisite GitHub Actions runs 답습 매트릭스** (read-only, §3) — `25728590939` (α-1 R-4 secret_scanner) + `25728590916` (α-2 R-5 importlinter) + `25728590977` (α-1 R-4 provider_import_scanner) + `25731846625` (α-1 R-4 provider_url_scanner + R-7 docker block) = **4/4 SUCCESS** + 모든 jobs.conclusion=success + 4 artifact 답습 보존 + W-4 신규 run = *답습* + Stage 4 step 신규 검증 (사용자 결정 후 발화).
docs/phase0/layer-c-implementation-evidence-pass-entry-brief.md:74:- ❌ **R-4 도구 본문 변경 0건** — `tools/secret_scanner.py` (368줄) / `tools/provider_import_scanner.py` (178줄) / `tools/provider_url_scanner.py` (283줄) 어느 줄도 변경 0건
docs/phase0/layer-c-implementation-evidence-pass-entry-brief.md:247:| (a) | 동등 이상의 보안 결과 | Group D `tools/secret_scanner.py` (368줄) — R-4.1 Tier-1 45 patterns 직접 답습 (Prefix 36 + regex 7 + alternation 2) — gitleaks/detect-secrets 동등 이상 + 답습 변경 0건 | ✅ **충족** |
docs/phase0/layer-c-implementation-evidence-pass-entry-brief.md:657:본 brief 는 **Phase α 4 단계 brief 모두 APPROVE AS BRIEF 완료 milestone 후속** (α-1 `1b3090b` + α-2 `6a79247` + α-3 `3f6306d` + α-4 `e59a565`), **Layer C (Implementation Evidence PASS) 발효 합의 *진입 가능성 검토 한정* 준비안 (DRAFT)** 이다. **사용자 명시 7 금지** (실 Layer C 발효 / CI workflow 변경 / branch protection 변경 / dev 환경 강제 / `pre-commit install` 의무화 / Operational Readiness PASS / Hermes PMO 격상) Phase α-1 / α-2 / α-3 / α-4 패턴 답습 (사용자 명시 enumerate 0건 — 본 brief = 패턴 보존 + 사용자 검토 시 prohibition 추가/축소 권위 영역). **Layer C 정의 = mvp1.md §2.2 (Implementation Evidence PASS) + ADR-011 §2.1 (a)~(e) 5 조건 패턴 답습** ((a) 동등 이상의 보안 결과 / (b) 격리 환경 PoC 실증 / (c) ADR/SDD 권위 명시 / (d) 자동 회귀 검증 경로 / (e) 합의 APPROVE — 양 GP 공통) + **GP-3 × 5/5 evidence 적격** (Group D `tools/secret_scanner.py` 368줄 + Stage 2 ST-3 PoC `docker/gp3-st3-poc/` 4 파일 93줄 + ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + §2.6.2 R2-1 + ADR-010 + R-4 + mvp1.md §3 + Layer B §5.5.1 + `.github/workflows/secret-hygiene-egress-redaction.yml` 694줄 + GP-3 MVP-1 진입 합의 + GP-3 Stage 2 합의 + Phase α-3 합의 APPROVE AS BRIEF — (a)~(d) 4/4 현 충족 + (e) Layer C 시점 발효 적격) + **GP-5 × 5/5 evidence 적격** (Group A 1차 `tools/provider_import_scanner.py` 178줄 + Group A 2차 `.importlinter` 35줄 + Group A 3차 `tools/provider_url_scanner.py` 283줄 + ADR-008 차단조건 #4 + ADR-009 C-N §5 + P1 v2 + P2 v3 §10.1 + mvp1.md §4 + Layer B §5.5.2 T-6 + Group A 2차 풀 3+1 합의 + `.github/workflows/provider-adapter-enforcement.yml` 186줄 + `provider-url-scanner.yml` 326줄 + GP-5 MVP-1 진입 합의 + Stage 4 합의 + Phase α-1 / α-2 / α-4 합의 APPROVE AS BRIEF — (a)~(d) 4/4 현 충족 + (e) Layer C 시점 발효 적격) = **양 GP × 5 조건 = 10/10 evidence 적격성 권위 권고** + **4 prerequisite actual runs PASS 답습** (Stage 1 `25728590939` + Stage 2 `25731846625` + Stage 3 `25728590916` + `25728590977` 모두 SUCCESS) + **7 금지 영역 × Layer C 발효 합의 분리 매트릭스** (7/7 분리 — 충돌 0) + **Layer C 발효 합의 진입 적격성 5 조건 검토** (C-ζ-1 7 금지 충돌 0/7 + C-ζ-2 10/10 evidence 적격 + C-ζ-3 4 prerequisite runs PASS 답습 + C-ζ-4 Phase α 4 단계 brief 4/4 APPROVE AS BRIEF + C-ζ-5 5 영구 핵심 제약 5/5 보존 = 5/5 충족) + **15 풀 3+1 승격 트리거 0/15 발화** + **Layer C 발효 시점 영향 Rollback Trigger 의존성 답습** (18 trigger 中 Layer C 직접 영향 8 + 간접 영향 1 + 영향 0 9 — 발화 0건) + **외부 LLM 1+ 요구사항 검토** (mvp1.md 본문 explicit 의무 명시 0건 — 권고 한정, 사용자 명시 결정 영역) + **합의 형태 권고 = Reviewer-only 단축 합의 적격 후보** (Phase α-1/2/3/4 패턴 답습, 사용자 명시 결정 시 풀 3+1 + 외부 LLM 1+ 옵션 권위 영역) + **본 brief 자체 금지 56 + Layer C 발효 단계 금지 26** 을 정리한다. **본 brief 는 Layer C 발효를 *시작* 시키지 않으며, GP-3 / GP-5 PASS 를 *발효* 시키지 않으며, MVP-1 PASS 를 *선언* 하지 않으며, 외부 LLM 호출을 *자동 발화* 시키지 않으며, ADR-011 §2.1 (a)~(e) 5 조건 / Phase α-1/2/3/4 합의 / Group α 합의 / Backlog #6 우선 진입 합의 / Layer A / Layer B / GP-3 Stage 2 / Stage 4 / 5 Stage 분할안 합의 본문 변경 / R-4 / R-5 / R-7 / R-1 영역 본문 변경 / 14 결정 영역 *재결정* / Phase α-1 / α-2 / α-3 / α-4 실 진입 자동 진입 / Layer D / Layer E / Layer F 발효 / 7 금지 영역 *해소* / 4 prerequisite actual runs 자동 재실행 / 신규 actual run 자동 trigger / 외부 LLM blind 의뢰 자동 발송 / 합의 보고서 작성 / 메타 갱신 / commit / push 모두 본 brief 영역 외**. 다음 단계는 사용자 명시 결정 영역 (옵션 A~I, §9 답습) — **(A) Reviewer-only 단축 합의 진입 (권고) / (A') 풀 3+1 + 외부 LLM 1+ 합의 진입 (선택) / (F) Layer C 발효 합의 실 진입 brief 작성 / 기타 옵션**.
docs/phase0/mvp2-full-gp2-pass-trajectory-entry-brief.md:5:> **v1 → v1.1 갱신**: 풀 3+1 + 외부 LLM 1+ (codex gpt-5.5 cross-vendor) 통합 합의 (`docs/review/3plus1-consensus-2026-05-28-mvp2-full-gp2-trajectory.md`) **APPROVE WITH CONDITIONS (4 source 전원) → BLOCKING 3 + 권고 10 1pass 흡수** (별도 v2 cycle 0, ceremony-inflation 차단, 52/55/60 동형). 핵심 정정: **B-1 citation 오귀속** ("(β) §0.2 #23" → **#10**, #23 = 자동 후속) / **B-2** R-2 후보 (R-2-c) secret_scanner 재사용 + (R-2-d) LiteLLM callback hook 추가 / **B-3** "R-1 ∧ R-2 (AND)" 단정 → 대안 해석 병기 (governance §4.1 "GP-2 = 보조" + ADR-011 §2.3 위임). evidence 차단급 over-claim 0 (R-4 = 설계 동등성 일관). §14 흡수 매트릭스 추가.
docs/phase0/mvp2-full-gp2-pass-trajectory-entry-brief.md:25:3. **R-2 경로 분석** (facade RedactionFilter, TR-1 발화 / Provider Liquidity 직결 / (d) carry-over 동일 trajectory) (§4)
docs/phase0/mvp2-full-gp2-pass-trajectory-entry-brief.md:42:| 8 | 신규 외부 library 도입 / secret_scanner Tier-2/3 catalog 확장 | 0 |
docs/phase0/mvp2-full-gp2-pass-trajectory-entry-brief.md:44:| 10 | `facade.py` / `secret_scanner.py` / secret-hygiene workflow 본문 변경 | 0 (PoC 시제 + placeholder 보존) |
docs/phase0/mvp2-full-gp2-pass-trajectory-entry-brief.md:76:- **축 1 detection (operative ✅)**: R-3 (`secret-hygiene-egress-redaction.yml` D-2 + `secret_scanner.py --mode scan-log`) — 송신/로그 secret 잔존 회귀 검출. in-repo operative green (actual run `26517803107`).
docs/phase0/mvp2-full-gp2-pass-trajectory-entry-brief.md:100:2. **R-2**: facade RedactionFilter가 LLM API request body redaction을 적용함을 *검증* (= facade real 선행).
docs/phase0/mvp2-full-gp2-pass-trajectory-entry-brief.md:137:## §4 R-2 경로 분석 — facade RedactionFilter (facade real, TR-1)
docs/phase0/mvp2-full-gp2-pass-trajectory-entry-brief.md:146:- **(d) facade real (TR-1)** = 63 entry carry-over #4 + 본 trajectory R-2 = **동일 작업** (별도 아님). full GP-2 PASS prevention 입증을 위해 facade real이 *선행 필수* (RedactionFilter는 real facade 진입점에만 부착 가능).
docs/phase0/mvp2-full-gp2-pass-trajectory-entry-brief.md:147:- governance §4.3 (line 435): "P1 v2 LLM facade RedactionFilter" = 계산적 강제 메커니즘 (P1 facade layer).
docs/phase0/mvp2-full-gp2-pass-trajectory-entry-brief.md:157:- **(R-2-a) facade real + RedactionFilter 동시**: facade real 본문 (LiteLLM import + Router 위임) + RedactionFilter (request body Tier-1 42 redaction) 통합 구현. → TR-1 발화 = 풀 3+1 합의.
docs/phase0/mvp2-full-gp2-pass-trajectory-entry-brief.md:158:- **(R-2-b) facade real 먼저 / RedactionFilter 후속**: facade real (Provider Liquidity Layer 1) 우선 발효 → RedactionFilter는 별도 step. → 2 sub-cycle.
docs/phase0/mvp2-full-gp2-pass-trajectory-entry-brief.md:159:- **(R-2-c) `secret_scanner.py` Tier-1 catalog 재사용** (B-2, Agent C C1): 기존 in-repo `tools/secret_scanner.py` Tier-1 catalog (detection 시제)를 RedactionFilter redaction 로직에 재사용 — 신규 catalog 중복 회피, detection ↔ prevention 패턴 단일 source.
docs/phase0/mvp2-full-gp2-pass-trajectory-entry-brief.md:161:- ⭐ **권고 방향**: (R-2-a) 동시 + (R-2-c) catalog 재사용 — **RedactionFilter = facade *내부 협력자*** (R-5, Agent A): facade 진입점이 LLM API request body 통과 지점이므로 redaction은 facade real에 부착 필수. 분리 시 facade real 후 redaction 미부착 window 발생 (RT-1). TDD 적용 (RED: redaction filter test → GREEN: filter 구현). **(결정 = sub-cycle, 본 cycle = 권고만)**.
docs/phase0/mvp2-full-gp2-pass-trajectory-entry-brief.md:179:| **SC-1 (R-2 facade real)** | facade real + RedactionFilter (TR-1) | 풀 3+1 (TR-1 trigger) + 실 코드 | (d) carry-over 흡수, Provider Liquidity Layer 1 |
docs/phase0/mvp2-full-gp2-pass-trajectory-entry-brief.md:234:| RT-1 ⭐ | facade real 후 RedactionFilter 미부착 window (R-7 강화) | SC-1 | **(R-2-a) 동시 구현 안전 제약 명문 — facade real 발효 ∧ RedactionFilter 발효 = 단일 atomic step (분리 발효 금지). facade real PR에 redaction filter test green 필수 gate** |
docs/phase0/mvp2-full-gp2-pass-trajectory-entry-brief.md:246:- E-2: facade RedactionFilter 단위 test (request body Tier-1 42 redaction, TDD RED→GREEN)
docs/phase0/mvp2-full-gp2-pass-trajectory-entry-brief.md:262:2. **SC-1 (R-2 facade real + RedactionFilter, TR-1)** — facade real 본문 + filter 구현 (실 코드, TDD). (d) carry-over 동시 해소 (별도 sub-cycle)

exec
/bin/bash -lc "nl -ba docs/architecture/llm-providers-design.md | sed -n '450,485p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
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

codex
**판정: APPROVE WITH CONDITIONS**

brief의 방향은 대체로 타당합니다. 다만 구현 전 `src -> tools.secret_scanner` 런타임 의존을 기본안으로 두는 부분은 그대로 승인하기 어렵습니다. 승인 조건은 아래 BLOCKING 2건을 v1.1 또는 구현 지침에 반영하는 것입니다.

**BLOCKING 항목**

1. **catalog 재사용 기본안을 (i)에서 (ii)로 전환해야 함**
   - brief는 (i) `src -> tools.secret_scanner import`를 “본 brief 권고 = (i) 우선”으로 둡니다: [mvp2-sc1...brief.md:76](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:76).
   - 하지만 `tools/secret_scanner.py`는 CLI/PoC 도구 성격이 강하고, 자체 header도 “Secret scanner — Group D PoC” 및 `--mode scan-source/scan-log` 도구 contract를 명시합니다: [tools/secret_scanner.py:2](/home/delangi/문서/project/category/AI_development_tool/tools/secret_scanner.py:2), [tools/secret_scanner.py:19](/home/delangi/문서/project/category/AI_development_tool/tools/secret_scanner.py:19).
   - `.importlinter`는 root가 `src`뿐이라 `src -> tools` 의존을 검출하지 못합니다: [.importlinter:19](/home/delangi/문서/project/category/AI_development_tool/.importlinter:19). “미차단”은 “아키텍처 승인”이 아닙니다.
   - 권고: Tier-1 catalog를 runtime-safe shared module로 추출하고, `tools/secret_scanner.py`와 `RedactionFilter`가 같은 source를 쓰게 하세요. 이 변경은 “패턴 내용 변경 0건”으로 관리하고, pattern count/equivalence test를 필수 evidence로 추가해야 합니다.

2. **request body redaction 범위를 `messages`만으로 닫지 말고, 설계상 request 입력 전체로 명시해야 함**
   - brief §3은 `req.messages`와 `system`을 Router 전 redaction한다고 합니다: [mvp2-sc1...brief.md:96](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:96), [mvp2-sc1...brief.md:97](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:97).
   - 설계 `LLMRequest`에는 `system`뿐 아니라 `tools`, `tool_choice`, `response_format`, `stop_sequences`, `metadata_in`도 있고, 특히 `metadata_in`은 “호출 메타”로 명시됩니다: [llm-providers-design.md:209](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/llm-providers-design.md:209), [llm-providers-design.md:212](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/llm-providers-design.md:212), [llm-providers-design.md:217](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/llm-providers-design.md:217).
   - 현재 placeholder에는 `system`이 없고 `metadata`만 있습니다: [facade.py:18](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:18), [facade.py:22](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:22). 따라서 본 cycle 최소 구현은 `messages + metadata`를 다루거나, `metadata` 제외를 명시적으로 deferred해야 합니다. “LLM API request body” 차단이라는 governance 문구와 맞추려면 request-bound fields 전체 redaction contract가 더 정직합니다: [governance-preconditions.md:422](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/governance-preconditions.md:422).

**권고 항목**

1. TDD에 “원본 request/message 불변성” 테스트를 추가하세요. `redact_messages()`가 입력 list/dict를 in-place mutate하면 호출자 로그나 재시도 경로에 예상치 못한 부작용이 생깁니다.

2. T-4 false positive는 단일 정상 문장보다 edge case fixture가 필요합니다. `sort(key=...)` 회피 의도가 scanner 주석에 이미 존재합니다: [tools/secret_scanner.py:157](/home/delangi/문서/project/category/AI_development_tool/tools/secret_scanner.py:157), [tools/secret_scanner.py:158](/home/delangi/문서/project/category/AI_development_tool/tools/secret_scanner.py:158). 해당 케이스와 `keyboard`, `monkeypatch`, 일반 URL query 예시를 넣는 편이 좋습니다.

3. `scrub()`는 dict key blacklist까지 구현해야 §8.2와 정합합니다. 원 설계는 `KEY_BLACKLIST`를 둡니다: [llm-providers-design.md:530](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/llm-providers-design.md:530). Tier-1 regex만 재사용하면 key 기반 redaction 일부가 누락될 수 있습니다.

4. T-6 “redaction 후 deferred”는 결과가 외부로 송신되지 않으므로 spy/fake redactor 주입으로 순서를 검증해야 합니다. 단순히 `NotImplementedError`만 확인하면 redaction 선행을 증명하지 못합니다.

5. `redact_messages()`는 OpenAI-compatible message content가 `str`뿐 아니라 list/structured content일 수 있음을 고려해 `scrub()` 기반 재귀 처리가 더 안전합니다. 현재 placeholder typing은 `dict[str, str]`지만 설계는 `list[dict]`입니다: [llm-providers-design.md:207](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/llm-providers-design.md:207).

**NOTE**

- 명칭 정직성은 양호합니다. brief는 “facade redaction layer real”이고 “full facade real 아님”을 반복 명시합니다: [mvp2-sc1...brief.md:7](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:7), [mvp2-sc1...brief.md:33](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:33).
- RT-1 window 회피 논리는 타당합니다. 현재 `complete()`는 placeholder이고 실제 Router 송신이 없습니다: [facade.py:37](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:37). Router deferred 상태에서 redaction layer를 먼저 붙이는 것은 “송신 전 미부착 window”를 만들지 않습니다.
- Provider Liquidity 보존도 타당합니다. 본 cycle에서 `litellm import 0`이면 `.importlinter`의 SDK 금지 contract와 충돌하지 않습니다: [.importlinter:24](/home/delangi/문서/project/category/AI_development_tool/.importlinter:24), [.importlinter:34](/home/delangi/문서/project/category/AI_development_tool/.importlinter:34).

**catalog 재사용 (i)/(ii) 독립 권고**

추천은 **(ii) 공유 모듈 추출**입니다.

`src` runtime code가 `tools` CLI/PoC 모듈을 import하는 (i)는 단기 구현은 쉽지만 packaging, import boundary, ownership 면에서 좋지 않습니다. 특히 `.importlinter`가 root=`src`라 이 역방향 의존을 제어하지 못합니다. 반대로 (ii)는 `tools/secret_scanner.py` 변경이 생기지만, pattern literal을 옮기고 scanner가 import하게 만드는 refactor라면 “패턴 내용 변경 0건”과 양립 가능합니다. 단, equivalence test가 조건입니다: `len(ALL_PATTERNS) == 45`, pattern id/category/vendor/regex snapshot 동일, scanner pass/fail fixture 유지.

**권위/설계 인용 cross-verify 결과**

| brief 주장 | 실제 문서 대조 | 판정 |
|---|---|---|
| facade 단일 진입점 | `LLMFacade`가 “모든 LLM 호출의 단일 진입점”으로 명시됨: [llm-providers-design.md:255](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/llm-providers-design.md:255), [llm-providers-design.md:256](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/llm-providers-design.md:256) | 일치 |
| LiteLLM 직접 import facade 한정 | ADR-009 §2.2 의무 #1: [ADR-009...md:70](/home/delangi/문서/project/category/AI_development_tool/docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md:70) | 일치 |
| GP-2가 LLM API request body secret 차단 포함 | governance §4.1에 `LLM API request body` 명시: [governance-preconditions.md:422](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/governance-preconditions.md:422) | 일치 |
| §8.2 RedactionFilter는 응답/예외/메트릭 scrub 중심 | 원 설계 docstring은 “응답·예외·메트릭” 중심: [llm-providers-design.md:521](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/llm-providers-design.md:521), [llm-providers-design.md:522](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/llm-providers-design.md:522) | 부분 확장. 송신 redaction은 governance와 정합하지만 §8.2 자체만의 직접 문구는 아님 |
| Tier-1 45 catalog 재사용 | scanner가 45 patterns를 명시: [tools/secret_scanner.py:166](/home/delangi/문서/project/category/AI_development_tool/tools/secret_scanner.py:166), [tools/secret_scanner.py:169](/home/delangi/문서/project/category/AI_development_tool/tools/secret_scanner.py:169) | 일치 |
| Router deferred / litellm import 0 | 현재 facade는 placeholder이고 Router 없음: [facade.py:31](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:31), [facade.py:38](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:38) | 일치 |
| full GP-2 PASS 아님 | governance Exit (a)는 Hermes native + P1 facade 둘 다 요구: [governance-preconditions.md:451](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/governance-preconditions.md:451). brief는 R-2 prong만 충족한다고 제한: [mvp2-sc1...brief.md:11](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:11) | 일치, over-claim 없음 |
tokens used
88,538
**판정: APPROVE WITH CONDITIONS**

brief의 방향은 대체로 타당합니다. 다만 구현 전 `src -> tools.secret_scanner` 런타임 의존을 기본안으로 두는 부분은 그대로 승인하기 어렵습니다. 승인 조건은 아래 BLOCKING 2건을 v1.1 또는 구현 지침에 반영하는 것입니다.

**BLOCKING 항목**

1. **catalog 재사용 기본안을 (i)에서 (ii)로 전환해야 함**
   - brief는 (i) `src -> tools.secret_scanner import`를 “본 brief 권고 = (i) 우선”으로 둡니다: [mvp2-sc1...brief.md:76](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:76).
   - 하지만 `tools/secret_scanner.py`는 CLI/PoC 도구 성격이 강하고, 자체 header도 “Secret scanner — Group D PoC” 및 `--mode scan-source/scan-log` 도구 contract를 명시합니다: [tools/secret_scanner.py:2](/home/delangi/문서/project/category/AI_development_tool/tools/secret_scanner.py:2), [tools/secret_scanner.py:19](/home/delangi/문서/project/category/AI_development_tool/tools/secret_scanner.py:19).
   - `.importlinter`는 root가 `src`뿐이라 `src -> tools` 의존을 검출하지 못합니다: [.importlinter:19](/home/delangi/문서/project/category/AI_development_tool/.importlinter:19). “미차단”은 “아키텍처 승인”이 아닙니다.
   - 권고: Tier-1 catalog를 runtime-safe shared module로 추출하고, `tools/secret_scanner.py`와 `RedactionFilter`가 같은 source를 쓰게 하세요. 이 변경은 “패턴 내용 변경 0건”으로 관리하고, pattern count/equivalence test를 필수 evidence로 추가해야 합니다.

2. **request body redaction 범위를 `messages`만으로 닫지 말고, 설계상 request 입력 전체로 명시해야 함**
   - brief §3은 `req.messages`와 `system`을 Router 전 redaction한다고 합니다: [mvp2-sc1...brief.md:96](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:96), [mvp2-sc1...brief.md:97](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:97).
   - 설계 `LLMRequest`에는 `system`뿐 아니라 `tools`, `tool_choice`, `response_format`, `stop_sequences`, `metadata_in`도 있고, 특히 `metadata_in`은 “호출 메타”로 명시됩니다: [llm-providers-design.md:209](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/llm-providers-design.md:209), [llm-providers-design.md:212](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/llm-providers-design.md:212), [llm-providers-design.md:217](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/llm-providers-design.md:217).
   - 현재 placeholder에는 `system`이 없고 `metadata`만 있습니다: [facade.py:18](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:18), [facade.py:22](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:22). 따라서 본 cycle 최소 구현은 `messages + metadata`를 다루거나, `metadata` 제외를 명시적으로 deferred해야 합니다. “LLM API request body” 차단이라는 governance 문구와 맞추려면 request-bound fields 전체 redaction contract가 더 정직합니다: [governance-preconditions.md:422](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/governance-preconditions.md:422).

**권고 항목**

1. TDD에 “원본 request/message 불변성” 테스트를 추가하세요. `redact_messages()`가 입력 list/dict를 in-place mutate하면 호출자 로그나 재시도 경로에 예상치 못한 부작용이 생깁니다.

2. T-4 false positive는 단일 정상 문장보다 edge case fixture가 필요합니다. `sort(key=...)` 회피 의도가 scanner 주석에 이미 존재합니다: [tools/secret_scanner.py:157](/home/delangi/문서/project/category/AI_development_tool/tools/secret_scanner.py:157), [tools/secret_scanner.py:158](/home/delangi/문서/project/category/AI_development_tool/tools/secret_scanner.py:158). 해당 케이스와 `keyboard`, `monkeypatch`, 일반 URL query 예시를 넣는 편이 좋습니다.

3. `scrub()`는 dict key blacklist까지 구현해야 §8.2와 정합합니다. 원 설계는 `KEY_BLACKLIST`를 둡니다: [llm-providers-design.md:530](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/llm-providers-design.md:530). Tier-1 regex만 재사용하면 key 기반 redaction 일부가 누락될 수 있습니다.

4. T-6 “redaction 후 deferred”는 결과가 외부로 송신되지 않으므로 spy/fake redactor 주입으로 순서를 검증해야 합니다. 단순히 `NotImplementedError`만 확인하면 redaction 선행을 증명하지 못합니다.

5. `redact_messages()`는 OpenAI-compatible message content가 `str`뿐 아니라 list/structured content일 수 있음을 고려해 `scrub()` 기반 재귀 처리가 더 안전합니다. 현재 placeholder typing은 `dict[str, str]`지만 설계는 `list[dict]`입니다: [llm-providers-design.md:207](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/llm-providers-design.md:207).

**NOTE**

- 명칭 정직성은 양호합니다. brief는 “facade redaction layer real”이고 “full facade real 아님”을 반복 명시합니다: [mvp2-sc1...brief.md:7](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:7), [mvp2-sc1...brief.md:33](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:33).
- RT-1 window 회피 논리는 타당합니다. 현재 `complete()`는 placeholder이고 실제 Router 송신이 없습니다: [facade.py:37](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:37). Router deferred 상태에서 redaction layer를 먼저 붙이는 것은 “송신 전 미부착 window”를 만들지 않습니다.
- Provider Liquidity 보존도 타당합니다. 본 cycle에서 `litellm import 0`이면 `.importlinter`의 SDK 금지 contract와 충돌하지 않습니다: [.importlinter:24](/home/delangi/문서/project/category/AI_development_tool/.importlinter:24), [.importlinter:34](/home/delangi/문서/project/category/AI_development_tool/.importlinter:34).

**catalog 재사용 (i)/(ii) 독립 권고**

추천은 **(ii) 공유 모듈 추출**입니다.

`src` runtime code가 `tools` CLI/PoC 모듈을 import하는 (i)는 단기 구현은 쉽지만 packaging, import boundary, ownership 면에서 좋지 않습니다. 특히 `.importlinter`가 root=`src`라 이 역방향 의존을 제어하지 못합니다. 반대로 (ii)는 `tools/secret_scanner.py` 변경이 생기지만, pattern literal을 옮기고 scanner가 import하게 만드는 refactor라면 “패턴 내용 변경 0건”과 양립 가능합니다. 단, equivalence test가 조건입니다: `len(ALL_PATTERNS) == 45`, pattern id/category/vendor/regex snapshot 동일, scanner pass/fail fixture 유지.

**권위/설계 인용 cross-verify 결과**

| brief 주장 | 실제 문서 대조 | 판정 |
|---|---|---|
| facade 단일 진입점 | `LLMFacade`가 “모든 LLM 호출의 단일 진입점”으로 명시됨: [llm-providers-design.md:255](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/llm-providers-design.md:255), [llm-providers-design.md:256](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/llm-providers-design.md:256) | 일치 |
| LiteLLM 직접 import facade 한정 | ADR-009 §2.2 의무 #1: [ADR-009...md:70](/home/delangi/문서/project/category/AI_development_tool/docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md:70) | 일치 |
| GP-2가 LLM API request body secret 차단 포함 | governance §4.1에 `LLM API request body` 명시: [governance-preconditions.md:422](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/governance-preconditions.md:422) | 일치 |
| §8.2 RedactionFilter는 응답/예외/메트릭 scrub 중심 | 원 설계 docstring은 “응답·예외·메트릭” 중심: [llm-providers-design.md:521](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/llm-providers-design.md:521), [llm-providers-design.md:522](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/llm-providers-design.md:522) | 부분 확장. 송신 redaction은 governance와 정합하지만 §8.2 자체만의 직접 문구는 아님 |
| Tier-1 45 catalog 재사용 | scanner가 45 patterns를 명시: [tools/secret_scanner.py:166](/home/delangi/문서/project/category/AI_development_tool/tools/secret_scanner.py:166), [tools/secret_scanner.py:169](/home/delangi/문서/project/category/AI_development_tool/tools/secret_scanner.py:169) | 일치 |
| Router deferred / litellm import 0 | 현재 facade는 placeholder이고 Router 없음: [facade.py:31](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:31), [facade.py:38](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:38) | 일치 |
| full GP-2 PASS 아님 | governance Exit (a)는 Hermes native + P1 facade 둘 다 요구: [governance-preconditions.md:451](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/governance-preconditions.md:451). brief는 R-2 prong만 충족한다고 제한: [mvp2-sc1...brief.md:11](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:11) | 일치, over-claim 없음 |
