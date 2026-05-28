OpenAI Codex v0.128.0 (research preview)
--------
workdir: /home/delangi/문서/project/category/AI_development_tool
model: gpt-5.5
provider: openai
approval: never
sandbox: danger-full-access
reasoning effort: none
reasoning summaries: none
session id: 019e6e46-60ff-7c10-8036-70bbe6c8f1a8
--------
user
당신은 외부 LLM 검토자 (cross-vendor blind review)입니다. 응답 vendor = OpenAI (codex CLI), 본 cycle 풀 3+1 Agent vendor = Anthropic Claude. cross-vendor 충족 (헌법 5조-2).

## 본 cycle 개요

AI_development_tool 프로젝트. 본 cycle = **SC-3 GP-2 full PASS 발효 합의 brief** (67 entry, PASS 발효 milestone). 65 SC-1 (R-2 facade RedactionFilter in-repo) + 66 SC-2 (R-1 Hermes 위임 검증 조건부) → GP-2 detection-tier(60) → prevention-tier 격상. 사용자 명시 진입.

본 cycle 발효 효과: GP-2 full PASS 발효 (Exit (a) prevention R-1 ∧ R-2 검증 충족). 단 prevention R-1 = 조건부 (실 격리 canary + R-6 Hermes lock trigger + HERMES_REDACT_SECRETS=true 활성화 = deferred).

본 cycle 발효 *하지 않는 것*: "GP-2 완전 PASS/prevention 완전 보증" over-claim 0 / Hermes 안전성 선언 0 (ADR-011 §7.3) / MVP-2 PASS(62) 재선언 0 / R-1 실 격리 canary 실행 0 / R-6 Hermes lock trigger 확장 0 / R-5 base64 0 / 실 코드 0 / 자동 후속 0.

⚠️ 핵심: 본 프로젝트는 over-claim cascade를 세션 #2에서 4회, 세션 #3(SC-2)에서 1회 포착함. 본 SC-3 = PASS *격상* (detection-tier → full)이라 명칭 over-claim risk 최고조 (60 "GP-2 full→detection 강등" 선례). "full GP-2 PASS"가 prevention R-1 조건부를 은폐하지 않아야 함.

## 검토 대상 (working directory 자료, codex 직접 read 의무 — 추측 금지)

PRIMARY (본 검토 핵심):
- `docs/phase0/mvp2-sc3-full-gp2-pass-activation-brief.md` (v1, §0~§11) ← 본 검토 핵심

권위/evidence source (직접 read cross-verify):
- `docs/phase0/mvp2-gp2-pass-activation-brief.md` (60 GP-2 detection-layer PASS — §2 3축, prevention deferred)
- `docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md` (65 SC-1 — R-2 in-repo operative)
- `docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md` (66 SC-2 — R-1 조건부/문서 기반)
- `docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md` (62 MVP-2 PASS — 명칭 복합 자격 패턴 + GP-2 detection-tier)
- `docs/architecture/governance-preconditions.md` §4.5 Exit (a)~(e)
- `src/adapters/llm/redaction.py` + `tests/adapters/llm/test_redaction_filter.py` (65 R-2 evidence 실재)
- `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.3 #2 + §7.3 (안전성 선언 금지)

## 검토 관점 (외부 cross-vendor 독립)

1. **명칭 over-claim 차단 (최우선)**: brief가 "GP-2 full PASS"를 복합 자격 (prevention R-1 조건부 + 실 canary/R-6 deferred)으로 정직하게 명문하는가? 60 "full→detection 강등" / 62 "복합 자격" cascade 답습이 충실한가? "full"이라는 단어 자체가 R-1 조건부를 은폐하는 over-claim 아닌가?
2. **Exit (a) R-1 ∧ R-2 충족 판정**: governance §4.5 (a) = "Hermes native + facade 검증" (AND). R-2(in-repo) + R-1(조건부)로 (a) 충족 주장이 정직한가? R-1 조건부인데 "충족"으로 격상 가능한가, 아니면 (a)도 조건부인가?
3. **prevention 조건부 scope**: §4 R-1 조건부 (활성화 전제 + R-6 Tier-1 한정 + 실 canary deferred) 명문이 충분한가? §2 매트릭스에서 R-1 ⚠️ 표기 일관성?
4. **detection-tier → prevention-tier 격상 정당성**: §3 (R-2 in-repo cover 1 확보 → 60 비대칭 해소)이 타당한가?
5. **MVP-2 PASS(62) 재선언 0**: 본 cycle이 GP-2 prevention-tier 격상 한정인가, MVP-2 PASS 격상 over-claim 아닌가?
6. **PASS 발효 자격**: detection(60) + R-2(65) + R-1(66) + (e) 합의로 GP-2 full PASS 발효 자격 충실한가?
7. **권위 인용 정확성** + **누락/risk**.

## 응답 형식 (필수)

1. **판정**: APPROVE / APPROVE WITH CONDITIONS / REVISE
2. **BLOCKING 항목** (있으면): 번호 + 근거 (직접 read한 line 인용)
3. **권고 항목**: 번호 + 내용
4. **NOTE**: 관찰
5. **명칭 독립 판단**: "GP-2 full PASS" 명칭이 적절한가, 아니면 "GP-2 prevention PASS (R-1 조건부)" 등 다른 명칭이 더 정직한가?
6. **권위 인용 cross-verify 매트릭스**: brief 인용 vs 실제 문서 일치/모순

한국어로 응답하되 기술 용어는 영어 원문 유지. 직접 파일을 read하여 검증하고, 추측이 아닌 구체적 line 인용 기반으로 응답하세요.

codex
검토 대상과 권위 문서를 직접 읽어 line 근거를 잡겠습니다. 먼저 핵심 brief와 governance/ADR/선행 brief의 관련 구간을 병렬로 확인합니다.
exec
/bin/bash -lc "nl -ba docs/phase0/mvp2-sc3-full-gp2-pass-activation-brief.md | sed -n '1,260p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# GP-2 full PASS (detection + prevention R-2 in-repo + R-1 조건부 위임, 실 canary/R-6 Hermes trigger deferred) 발효 합의 entry brief (v1)
     2	
     3	> **작성**: 2026-05-28 (67번째 entry 진입 cycle — 세션 #3, SC-3)
     4	>
     5	> **scope**: **GP-2 송신 redaction PASS 발효 — detection-tier → prevention-tier 격상** (60 GP-2 detection-layer PASS 의 deferred prevention trajectory 완성). **복합 자격 (62 명칭 패턴 답습, over-claim 차단)**: detection operative (R-3) + prevention **R-2 in-repo operative** (65 SC-1) + prevention **R-1 조건부/문서 기반 위임 검증** (66 SC-2, 활성화 전제 + R-6 Tier-1 한정 + 실 격리 canary deferred).
     6	>
     7	> ⚠️ **명칭 정직성 (본 세션 #3 1회 + 세션 #2 4회 over-claim cascade 교훈)**: "GP-2 full PASS" = **detection + prevention 양 prong 충족** (Exit (a) R-1 ∧ R-2). 단 **prevention R-1 = 조건부** (실 격리 canary + R-6 Hermes dependency lock trigger + HERMES_REDACT_SECRETS=true 활성화 검증 = deferred). 무수식 "GP-2 완전 PASS" 또는 "prevention 완전 보증" 표현 금지.
     8	>
     9	> **본 cycle = 큰 cycle / PASS 발효 milestone** (60 GP-2 detection-layer PASS + 62 MVP-2 PASS + 32 MVP-1 PASS 답습 동형, 풀 3+1 + 외부 LLM 1+ + 사용자 명시 의무).
    10	>
    11	> **본 cycle 발효 자격** = detection (60 ✅) + R-2 in-repo (65 ✅) + R-1 조건부 위임 (66 ✅) + (e) 풀 3+1 + 외부 LLM 1+ APPROVE + 사용자 명시.
    12	>
    13	> **본 cycle 발효 효과** = **GP-2 full PASS 발효** (Exit (a) prevention R-1 ∧ R-2 검증 충족) — 60 detection-layer PASS 의 prevention 완성. **잔여 deferred (자동 진입 0)**: R-1 실 격리 canary 실행 + R-6 Hermes dependency lock trigger 확장 + R-5 base64 evasion (영구 분리).
    14	>
    15	> **선행 답습**: 60 GP-2 detection-layer PASS (`92e9078`) + 65 SC-1 (R-2 facade RedactionFilter in-repo operative) + 66 SC-2 (R-1 위임 검증 조건부/문서 기반) + 62 MVP-2 PASS (명칭 복합 자격 패턴) + governance §4.5 Exit (a)~(e)
    16	
    17	---
    18	
    19	## §0 본 brief 의 범위
    20	
    21	### §0.1 본 brief 가 *하는* 것
    22	
    23	1. **GP-2 Exit 5조건 통합 evidence 매트릭스** (detection + prevention R-2 + R-1) (§2)
    24	2. **detection-tier → prevention-tier 격상 정당성** (60 deferred 완성) (§3)
    25	3. **명칭 복합 자격 + prevention 조건부 scope 정직 명문** (62 답습, over-claim 차단) (§4)
    26	4. **GP-2 full PASS 발효 권고 + 조건** (§5)
    27	5. **합의 형태 + 잔여 deferred + 금지 + Rollback + 자기진단** (§6~§10)
    28	
    29	### §0.2 본 brief 가 *하지 않는* 것
    30	
    31	| # | 영역 | 위반 |
    32	|---|------|----|
    33	| 1 | **"GP-2 완전 PASS / prevention 완전 보증" over-claim** (R-1 조건부 명문 — 실 canary/R-6 Hermes trigger deferred) | 0 |
    34	| 2 | **Hermes 안전성 선언** (ADR-011 §7.3) / runtime egress 완전 PASS | 0 |
    35	| 3 | **MVP-2 PASS (62) 재선언** (답습 유지 — 본 cycle = GP-2 prevention-tier 격상 한정) | 0 |
    36	| 4 | R-1 실 격리 canary 실행 (artifact 재확보 deferred) / R-6 Hermes lock trigger 확장 | 0 |
    37	| 5 | R-5 base64/URL evasion (영구 분리, G3-4) | 0 |
    38	| 6 | detection-layer PASS (60) / SC-1 (65) / SC-2 (66) 재선언 | 0 |
    39	| 7 | Layer 3·5 / 2a / SC-Provider Liquidity (Router 위임) 진입 | 0 |
    40	| 8 | ADR / 헌법 / governance / roadmap 본문 갱신 (발효 후 별도) | 0 |
    41	| 9 | 실 코드 / CI / config 본문 변경 | 0 |
    42	| 10 | 자동 후속 (MVP-3 / R-6 확장 / 실 canary) 진입 | 0 (사용자 명시 의무) |
    43	
    44	### §0.3 권위 답습 source
    45	
    46	- **governance §4.5 Exit (a)~(e)** — (a) "Hermes native redaction Tier-1 42 catalog 적용 검증 + facade redaction filter 검증" (R-1 ∧ R-2)
    47	- **60 GP-2 detection-layer PASS brief** (`mvp2-gp2-pass-activation-brief.md`) — §2 3축 (detection ✅ / 설계 동등성 / prevention deferred), §6 발효 권고
    48	- **65 SC-1 brief + 합의** (`mvp2-sc1-facade-redaction-implementation-brief.md`) — R-2 facade RedactionFilter in-repo operative (group-aware 치환, 15 test, 커버리지 92%)
    49	- **66 SC-2 brief + 합의** (`mvp2-sc2-r1-hermes-delegation-verification-brief.md`) — R-1 조건부/문서 기반 위임 검증 (4축, 활성화 전제 + R-6 Tier-1 한정)
    50	- **62 MVP-2 PASS brief** (`mvp2-implementation-evidence-pass-activation-brief.md`) — 명칭 복합 자격 패턴 (over-claim 차단) + GP-2 detection-tier deferred trajectory
    51	- **ADR-011 §2.1 (a)~(d) + §2.3 #2 (위임) + §7.3 (안전성 선언 금지)** + **ADR-012 §4 (e2 확장)**
    52	
    53	---
    54	
    55	## §1 진입 컨텍스트
    56	
    57	- 60 GP-2 detection-layer PASS 발효 (R-3 detection operative + prevention R-1/R-2 deferred).
    58	- 62 MVP-2 PASS = G4 ledger 완전 + GP-2 **detection-tier** (full GP-2 prevention = 후속 trajectory).
    59	- 65 SC-1 → R-2 (facade RedactionFilter) **in-repo operative** (placeholder → real, deferred 해소).
    60	- 66 SC-2 → R-1 (Hermes 위임) **조건부/문서 기반 검증** (위치 ✅ + 동등성 ✅ + 자동회귀 Tier-1 한정 + 활성화 전제).
    61	- → 본 SC-3 = GP-2 prevention (R-1 ∧ R-2) trajectory 완성 → **GP-2 detection-tier → full PASS 격상**.
    62	
    63	---
    64	
    65	## §2 GP-2 Exit 5조건 통합 evidence 매트릭스 (detection + prevention)
    66	
    67	| # | 조건 | detection (60) | prevention R-2 (65 SC-1) | prevention R-1 (66 SC-2) | 통합 판정 |
    68	|---|------|------|------|------|------|
    69	| (a) | 동등 이상 보안 결과 | R-4 설계 동등성 (Tier-1 42) | ✅ **facade RedactionFilter in-repo** (group-aware, Tier-1 45 catalog 공유) | ⚠️ **조건부** (Hermes 47 ⊇ Tier-1, 활성화 전제) | ✅ **R-1 ∧ R-2 prevention 검증 충족** (R-2 강 + R-1 조건부) |
    70	| (b) | 격리 PoC 실증 | ✅ secret-hygiene D-2 | ✅ **redaction 15 test (커버리지 92%)** | ⚠️ 실 격리 canary deferred (day2-r1 코드 분석) | ✅ in-repo PoC 충족 / R-1 실 canary deferred |
    71	| (c) | ADR/SDD 권위 | ✅ ADR-011 §2.3 #2 + governance §4 | ✅ ADR-009 §2.2 (facade 단일 진입점) | ✅ ADR-011 §2.3 #2 (위임) | ✅ |
    72	| (d) | 자동 회귀 검증 | ✅ secret-hygiene D-2 CI | ✅ **redaction test (pytest 167)** | ⚠️ R-6 Tier-1 canary (Hermes lock trigger 미구현) | ✅ in-repo 회귀 / R-1 Hermes trigger deferred |
    73	| (e) | 합의 APPROVE | ✅ 60 | ✅ 65 | ✅ 66 | ⏳ **본 SC-3** |
    74	
    75	→ **(a)~(d) prevention 검증 충족** (R-2 in-repo operative + R-1 조건부 위임). (e) = 본 cycle. **GP-2 full PASS = detection + prevention 양 prong** (R-1 조건부 명문).
    76	
    77	---
    78	
    79	## §3 detection-tier → prevention-tier 격상 정당성 (60 deferred 완성)
    80	
    81	- 60 GP-2 detection-layer PASS = R-3 detection operative + **prevention (R-1/R-2) deferred trajectory** (in-repo 입증 0).
    82	- 본 SC-3 = 그 deferred trajectory 완성:
    83	  - **R-2 deferred 해소**: 65 SC-1 → facade RedactionFilter in-repo operative (placeholder → real, group-aware 치환 + 15 test). **in-repo 능동 redaction 보증 1 확보** (60 §3.2 B-2 "in-repo 능동 redaction 보증 0" 해소).
    84	  - **R-1 조건부 충족**: 66 SC-2 → Hermes 위임 검증 (위치 + 동등성 + 권위, 조건부).
    85	- → GP-2 = detection (R-3) + prevention (R-2 in-repo + R-1 위임) = **full PASS scope** (Exit (a) R-1 ∧ R-2).
    86	
    87	⚠️ **cover 구조 (60 B-2 답습 — 비대칭 해소)**: 60 = prevention in-repo cover 0 (Hermes 단독 위임). 65 SC-1 → **in-repo prevention cover 1 (R-2 facade)** + Hermes 위임 (R-1) = 이중 cover (비대칭 부분 해소).
    88	
    89	---
    90	
    91	## §4 명칭 복합 자격 + prevention 조건부 scope 정직 명문 (62 답습, over-claim 차단)
    92	
    93	⭐ **명칭 = "GP-2 full PASS (detection operative + prevention: R-2 in-repo operative + R-1 조건부/문서 기반 위임; 실 격리 canary + R-6 Hermes lock trigger deferred)"** — 62 복합 자격 패턴 답습.
    94	
    95	**발효 범위 (operative)**:
    96	- ✅ detection (R-3 secret-hygiene D-2 CI green)
    97	- ✅ prevention R-2 (facade RedactionFilter in-repo, group-aware 치환, 15 test, pytest 167)
    98	
    99	**조건부 (정직 명문)**:
   100	- ⚠️ prevention R-1 (Hermes 위임) = **조건부/문서 기반** — 위치 (day2-r1 2026-05-05 코드 분석) + 동등성 (R-4 §5 Hermes ⊇ Tier-1) + 권위 (ADR-011 §2.3 #2). **활성화 전제 (HERMES_REDACT_SECRETS=true)** + **R-6 Tier-1 canary 한정 (Hermes dependency lock trigger 미구현)** + **실 격리 canary deferred** (artifact 재확보).
   101	
   102	**deferred (자동 진입 0)**:
   103	- ⚠️ R-1 실 격리 canary 실행 (Hermes re-clone, URL 확보 선결)
   104	- ⚠️ R-6 Hermes dependency lock trigger 확장 (hermes-version.yaml 파일 + lock diff)
   105	- ⚠️ R-5 base64/URL/압축 evasion (영구 분리, G3-4 — Tier-1 42 평문 한정)
   106	
   107	→ **GP-2 full PASS = detection + prevention 충족 (Exit (a) R-1 ∧ R-2). prevention R-1 조건부 + R-5 evasion + 실 canary = 정직 scope (over-claim 0)**.
   108	
   109	---
   110	
   111	## §5 GP-2 full PASS 발효 권고 + 조건
   112	
   113	⭐ **권고 = GP-2 full PASS 발효 APPROVE WITH CONDITIONS** (복합 자격, prevention R-1 조건부 명문):
   114	
   115	1. **detection (60 ✅) + prevention R-2 in-repo (65 ✅) + R-1 조건부 위임 (66 ✅) + (e) 본 cycle** → Exit (a)~(e) 충족 (R-1 조건부).
   116	2. **조건**:
   117	   - (C-1) **명칭 복합 자격 부착** — 무수식 "GP-2 완전 PASS" 금지, prevention R-1 조건부 + deferred 명문 (62 B-1 답습)
   118	   - (C-2) **R-1 = 조건부/문서 기반** (활성화 전제 + R-6 Tier-1 한정 + 실 canary deferred, 66 답습)
   119	   - (C-3) **R-5 base64 evasion = known limitation** (Tier-1 42 평문 한정)
   120	   - (C-4) **MVP-2 PASS (62) 재선언 0** — 본 cycle = GP-2 detection-tier → prevention-tier 격상 한정 (MVP-2 PASS 명칭 갱신 = 발효 후 별도 chore)
   121	3. **잔여 deferred 명문** (§4) — 자동 진입 0.
   122	
   123	→ **GP-2 full PASS 발효 자격 = detection + prevention (R-2 in-repo + R-1 조건부) + (e) 합의 APPROVE + 사용자 명시 + (C-1) 복합 자격**.
   124	
   125	---
   126	
   127	## §6 합의 형태 + 승격 트리거
   128	
   129	### §6.1 합의 형태 = 풀 3+1 + 외부 LLM 1+ (의무)
   130	
   131	**정당화**: PASS 발효 milestone (60/62/32 답습) + 큰 결정 (ADR-011 §2.4 T3) + 보안 (GP-2 prevention) + 5조-2 cross-vendor + 사용자 명시.
   132	
   133	### §6.2 승격 트리거
   134	
   135	| # | trigger | 발화 |
   136	|---|---------|----|
   137	| 1 | 큰 결정 (GP-2 full PASS milestone) | ✅ |
   138	| 2 | 보안 (GP-2 prevention 발효) | ✅ |
   139	| 3 | 외부 LLM cross-vendor (5조-2) | ✅ |
   140	| 4 | 명칭 over-claim risk (60/62 cascade 답습) | ✅ |
   141	
   142	→ **4/4 발화 → 풀 3+1 + 외부 LLM 1+**.
   143	
   144	---
   145	
   146	## §7 잔여 deferred (자동 진입 0)
   147	
   148	1. **R-1 실 격리 canary 실행** — Hermes re-clone (URL 확보) + HERMES_REDACT_SECRETS=true + canary 주입 (SC-2 C-3 SOP). GP-2 full PASS 강한 보강.
   149	2. **R-6 Hermes dependency lock trigger 확장** — hermes-version.yaml 파일 + lock diff trigger (SC-2 B-1 잔여).
   150	3. **R-5 base64 evasion** — 영구 분리 (G3-4).
   151	4. **MVP-2 PASS 명칭 갱신** — GP-2 detection-tier → full PASS (roadmap/62 cross-reference, 발효 후 chore).
   152	
   153	---
   154	
   155	## §8 금지 사항
   156	
   157	§0.2 답습 (10). 추가: "GP-2 완전 PASS" 무수식 0 / Hermes 안전성 선언 0 / R-1 "실 canary 완료" 주장 0 / MVP-2 PASS 재선언 0 / 자동 후속 0.
   158	
   159	---
   160	
   161	## §9 Rollback Trigger
   162	
   163	| # | trigger | 대응 |
   164	|---|---------|----|
   165	| RT-1 | "GP-2 완전 PASS" over-claim 발생 | §4 복합 자격 명문 (prevention R-1 조건부 + deferred) |
   166	| RT-2 | R-2 facade redaction 회귀 (15 test FAIL) | pytest CI + RedactionFilter 불변성 (65 답습) |
   167	| RT-3 | R-1 실 격리 canary 실행 시 day2-r1 결론 불일치 | C-3 SOP 결과 우선 → R-1 위임 검증 재평가 |
   168	| RT-4 | Hermes upstream redaction silent 깨짐 | R-6 Tier-1 canary + R-5 재검증 (단 Hermes trigger deferred) |
   169	| RT-5 | base64 evasion 발견 | known limitation (R-5 영구 분리) |
   170	
   171	---
   172	
   173	## §10 Evidence
   174	
   175	- E-1: detection (60, secret-hygiene D-2 CI green)
   176	- E-2: prevention R-2 (65 SC-1, facade RedactionFilter 15 test + 커버리지 92% + pytest 167)
   177	- E-3: prevention R-1 (66 SC-2, 위치 + 동등성 + 권위 조건부)
   178	- E-4: Exit (a)~(e) 통합 매트릭스 (§2)
   179	- E-5: 복합 자격 명칭 (over-claim 0)
   180	
   181	---
   182	
   183	## §11 자기진단 (메타 편향 회피)
   184	
   185	| # | 위험 | 처리 |
   186	|---|------|----|
   187	| P-1 | "GP-2 완전 PASS" over-claim (60/62 cascade 재발) | §4 복합 자격 (prevention R-1 조건부 + deferred), [[feedback_pass_scope_overclaim]] |
   188	| P-2 | prevention "충족"이 R-1 실 canary 미실행 은폐 | §2/§4 — R-1 조건부/문서 기반 명문 (66 답습), 실 canary deferred |
   189	| P-3 | Hermes 안전성 선언 격상 | §0.2 #2 — 위임 검증 ≠ 안전 선언 (ADR-011 §7.3) |
   190	| P-4 | MVP-2 PASS (62) 재선언 | §0.2 #3 + (C-4) — GP-2 prevention-tier 격상 한정 |
   191	| P-5 | R-2 in-repo = full runtime 보증 오인 | §4 — R-2 = facade redaction layer (Router deferred, 65 답습) |
   192	| P-6 | 작성자 = 60/62/65/66 작성자 (Claude) cascade | cross-vendor codex + 풀 3+1 독립 검증 (본 세션 over-claim 5회 포착 입증) |
   193	| P-7 | R-1 조건부를 "충족"으로 단순화 | §4 — R-1 활성화 전제 + R-6 Tier-1 한정 + 실 canary deferred 3중 명문 |
   194	
   195	---
   196	
   197	**본 brief v1 끝.**
   198	
   199	**다음 단계**: 사용자 승인 → 풀 3+1 + 외부 LLM 1+ (codex E-α) → Reviewer 통합 → v1.1 흡수 → commit + push → **GP-2 full PASS 발효 (detection + prevention R-2 in-repo + R-1 조건부 위임, 실 canary/R-6 Hermes trigger deferred)**. 후속: R-1 실 격리 canary 실행 / R-6 Hermes lock trigger 확장 / MVP-2 PASS 명칭 갱신 (chore) / MVP-3 영역 진입 = 사용자 명시 별도 cycle.

exec
/bin/bash -lc "nl -ba docs/architecture/governance-preconditions.md | sed -n '1,220p'" in /home/delangi/문서/project/category/AI_development_tool
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

exec
/bin/bash -lc "nl -ba docs/decisions/ADR-011-means-vs-ends-redaction.md | sed -n '1,260p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# ADR-011: Means-vs-Ends Redaction Principle (수단/목적 분리 원칙)
     2	
     3	**상태**: 승인 (단축 합의 — Reviewer-only, 2026-05-06)
     4	**날짜**: 2026-05-06
     5	**의사결정자**: 사용자 + Reviewer 합의 — `docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md`
     6	**상위 권위**: 헌법 제8조 (보안), 헌법 제5조-2 (Provider Liquidity, 비협상), `docs/architecture/system-identity-prequel.md` §3
     7	**갱신 대상**: ADR-008 부록 B Amendment (동시 발행)
     8	**모법 역할**: R-4 / R-5 / R-6 / R-7 작업의 권위 근거
     9	
    10	---
    11	
    12	## 1. 맥락 (Context)
    13	
    14	### 1.1 P2 v2 가정의 붕괴
    15	
    16	ADR-008 부록 A는 R1 (학습루프 평문 누적)을 비협상 CRITICAL 위험으로 명시했다. P2 v2 §2.1.3은 R1 차단 메커니즘으로 "외부 pre-record hook" 형태를 가정 채택했다.
    17	
    18	Phase 0 Day 1 사실 확인(`docs/phase0/day1-environment-and-fact-check.md`)에서 Hermes v0.12.0 main HEAD에 `pre_record` / `add_pre_record_hook` / `before_record` API가 존재하지 않음이 grep 0건으로 확정되었다 (15종 `VALID_HOOKS` 중 DB 기록 직전 가로채기 hook 0개).
    19	
    20	### 1.2 Phase 0 R-1 / R-2 evidence
    21	
    22	- **R-1 검증**(`docs/phase0/day2-r1-redaction-location-verification.md`): Hermes 자체 redaction(`agent/redact.py`)이 LLM 송신/도구 출력/로깅 전용이고 DB INSERT 경로 미적용 확정 → **G1a FAIL**.
    23	  - `agent/redact.py:1-8` docstring 명시: "Regex-based secret redaction for logs and tool output"
    24	  - redact 모듈 import 25개 모두 비-DB 경로
    25	  - `hermes_state.py` (SessionDB) redact import 0건
    26	
    27	- **R-2 PoC**(`docs/phase0/day3-r2-sqlite-trigger-poc.md`): SQLCipher BEFORE INSERT trigger + REGEXP UDF 조합이 Docker 격리 환경(network_mode: none + read_only + cap_drop ALL)에서 6항목 모두 PASS → **G1b PASS by R-2 PoC**.
    28	
    29	### 1.3 ADR 권위 해석 요청 사항
    30	
    31	위 결과는 다음 질문에 대한 ADR 권위 해석을 요구한다:
    32	
    33	> **R1의 "비협상" 본질은 무엇인가 — 특정 구현 수단인가, 보안 결과인가?**
    34	
    35	본 ADR은 이 질문에 답하고, 동시에 다음 3개 인접 안건을 ADR 권위로 정착한다:
    36	- G1a/G1b 게이트 분리 공식화
    37	- "Hermes ≠ root of trust" 권위 위계 영구화 (prequel §3 → ADR 승격)
    38	- 자동 학습 vs 자동 정책 변경 분리
    39	
    40	---
    41	
    42	## 2. 결정 (Decision)
    43	
    44	본 ADR은 다음 4가지를 권위로 선언한다.
    45	
    46	### 2.1 수단/목적 분리 원칙 (Means-vs-Ends Separation)
    47	
    48	**비협상 조건의 본질은 특정 구현 수단이 아니라, 달성해야 하는 안전 결과(safety outcome)이다.**
    49	
    50	- 헌법 제8조 (보안)의 본질은 **DB 평문 저장 차단이라는 결과**이다.
    51	- 외부 hook, redaction 호출, trigger, 암호화 등은 **수단**이다.
    52	- 대체 수단은 다음 4조건을 **모두** 충족할 때 기존 수단을 대체할 수 있다:
    53	
    54	  | # | 조건 | 검증 방식 |
    55	  |---|------|---------|
    56	  | (a) | 동등 이상의 보안 결과 | 명시적 비교표 (수단 A 보장 ↔ 수단 B 보장) |
    57	  | (b) | 격리 환경 PoC로 실증 | Docker isolation + 자동 검증 항목 |
    58	  | (c) | ADR 권위로 명시 | 본 ADR 또는 후속 ADR |
    59	  | (d) | 자동 회귀 검증 경로 확보 | CI/nightly 재실행 (R-6) |
    60	
    61	**원칙 위반**: "수단이 비협상이다"는 텍스트 해석으로 본질 회귀를 차단하는 것은 본 ADR로 무효화된다. 동시에 (a)~(d) 4조건 미충족 시 수단 대체도 금지된다 — 본 ADR은 *수단 자유*가 아니라 *목적 달성 검증 의무*를 강제한다.
    62	
    63	### 2.2 G1a / G1b 게이트 분리 공식화
    64	
    65	P2 v2의 단일 G1 게이트는 본 ADR로 다음 두 게이트로 분해된다.
    66	
    67	```
    68	G1a: Hermes native redaction applies before DB INSERT
    69	   Result: FAIL (R-1 확정)
    70	   Evidence: agent/redact.py docstring "for logs and tool output",
    71	             redact import 25개 모두 비-DB,
    72	             hermes_state.py redact import 0건
    73	   Status: 폐기 (이 경로로 헌법 8조 충족 시도 금지)
    74	
    75	G1b: DB-level fallback prevents plaintext secret persistence
    76	   Result: PASS by R-2 PoC
    77	   Evidence: Docker 격리 환경 (network_mode: none + read_only + cap_drop ALL)
    78	             + SQLCipher BEFORE INSERT trigger + REGEXP UDF
    79	             + 6항목 자동 검증 (C1~C6 모두 PASS)
    80	   Status: PoC PASS, 정식 충족은 R-3~R-5 완료 후
    81	```
    82	
    83	#### G1b 정식 충족 조건 (Phase 1 차단조건 #1 exit 기준)
    84	
    85	| # | 조건 | 산출 |
    86	|---|------|------|
    87	| R-3 | 본 ADR-011 발행 + ADR-008 Amendment | `ADR-011`, `ADR-008` 부록 B |
    88	| R-4 | Hermes redact pattern ↔ P1_REDACTOR 패턴 동등성 검증, gap 발견 시 trigger UDF 보충 | `docs/architecture/redaction-pattern-equivalence.md` |
    89	| R-5 | canary 재검증 트리거 설계 (T13 강화 — config + 주기적 inject) | `docs/architecture/canary-recheck-design.md` |
    90	| R-6 | CI/nightly 회귀 검증 (Hermes 업그레이드 자동 R-2 재실행) | `.github/workflows/r2-canary.yml` |
    91	| R-7 | Phase 1 합격 SOP (canary 패턴/주입/검증/PASS·FAIL 기준) | `docs/phase0/redaction-verification-sop.md` |
    92	
    93	R-3~R-7 모두 완료 시 G1b는 PoC 단계를 벗어나 Phase 1 차단조건 #1 정식 exit 기준이 된다.
    94	
    95	### 2.3 Hermes ≠ Root of Trust
    96	
    97	**Hermes는 시스템의 최종 신뢰 근거가 아니라 검증 대상이다.**
    98	
    99	#### 권위 위계 (Authority Hierarchy)
   100	
   101	```
   102	Constitution
   103	  > ADR
   104	  > SDD
   105	  > Harness Gates
   106	  > Hermes
   107	  > Worker Agents
   108	```
   109	
   110	#### 운영 함의 (Operational Implications)
   111	
   112	1. **Hermes 출력은 Tools로 검증된다**: 린터/타입체커/테스트/trigger/canary가 Hermes 출력 위에 위치한다.
   113	2. **Hermes 자체 redaction은 로그/LLM 송신 방어로만 신뢰**: 저장 경로(DB/파일) 차단 책임 없음.
   114	3. **DB INSERT 경로는 Hermes 외부에서 별도 보호**: SQLCipher trigger 기반 fallback (G1b).
   115	4. **Hermes 의존성 업그레이드는 자동 R-2 재실행으로 회귀 검증**: 신뢰 경계 외부 변경의 자동 검출 (R-6).
   116	5. **Hermes 학습 결과의 자동 정책 반영 금지**: §2.4와 결합.
   117	
   118	#### prequel과의 관계
   119	
   120	본 §2.3은 `docs/architecture/system-identity-prequel.md` §3 ("Hermes ≠ root of trust") 의 prequel(임시) 선언을 ADR 영구 권위로 승격한다. prequel은 R-7 완료 후 P2 v3로 흡수되며 폐기되지만, 본 ADR-011 §2.3은 영구 유지된다.
   121	
   122	### 2.4 자동 학습과 자동 정책 변경 분리
   123	
   124	- **자동 학습은 허용**: Worker Agent가 도구 사용/패턴/실패 사례를 누적 학습하는 것은 시스템 가치의 핵심.
   125	- **자동 정책 변경은 금지**: Constitution / ADR / Harness Gates / Hermes 설정의 변경은 사용자 승인 경로(3+1 합의 또는 단축 합의)를 거쳐야 한다.
   126	
   127	#### 3-tier 분류 (T1 / T2 / T3)
   128	
   129	| Tier | 정의 | 예시 | 승인 경로 |
   130	|------|------|------|---------|
   131	| **T1** | 자동 허용 | Worker Agent 패턴 학습, 도구 사용 빈도 누적, 실패 회피 휴리스틱 | 자동 |
   132	| **T2** | 사용자 승인 필수 | Skill/Memory promotion, 새 도구 등록, 합의 형태 결정 | 사용자 명시 결정 |
   133	| **T3** | 자동 금지 (절대) | Constitution / ADR / Harness Gates 정의 자체의 변경 | 단축 또는 풀 3+1 합의 |
   134	
   135	본 분리는 prequel §6의 3-tier 선언을 ADR 권위로 승격한 것이며, R-5 (canary 재검증) / R-6 (CI 회귀)의 권위 근거이기도 하다 — Hermes 내부 학습 또는 upstream 변경으로 redaction 동작이 silent 깨짐 발생 가능성을 자동 검증으로 차단.
   136	
   137	---
   138	
   139	## 3. R-4 ~ R-7 모법 역할 (Governing Precedent)
   140	
   141	본 ADR은 다음 후속 작업의 권위 근거로 기능한다.
   142	
   143	| 작업 | 산출 | 본 ADR §과의 관계 |
   144	|------|------|----------------|
   145	| **R-4** | `docs/architecture/redaction-pattern-equivalence.md` | §2.1 (a) — 대체 수단(R-2 trigger)이 기존 수단(Hermes redaction) 대비 패턴 커버리지 동등 이상임을 명시적 비교표로 실증 |
   146	| **R-5** | `docs/architecture/canary-recheck-design.md` | §2.4 — Hermes 학습 또는 upstream 변경으로 redaction silent 깨짐 발생 가능성 자동 검증 + §2.3 운영 함의 #4 구현 |
   147	| **R-6** | `.github/workflows/r2-canary.yml` | §2.1 (d) + §2.3 — Hermes 의존성 업그레이드의 자동 회귀 검증 |
   148	| **R-7** | `docs/phase0/redaction-verification-sop.md` | §2.2 G1b 정식 충족 절차의 SOP화 |
   149	
   150	후속 작업은 본 ADR §2를 명시 인용하고, 본 ADR 위반(예: "수단이 비협상이다" 텍스트 회귀, T3 자동 변경 시도) 시 단축 합의 + ADR Amendment 절차로만 갱신 가능하다.
   151	
   152	---
   153	
   154	## 4. 선택지 (Options Considered)
   155	
   156	### 옵션 A: ADR-011 단독 (Amendment 없음)
   157	
   158	- 장점: 일반 원칙 ADR 단일 산출 — 작성 부담 최소
   159	- 단점: ADR-008 부록 A R1 표면 텍스트("외부 pre-record hook 공식 지원")가 갱신되지 않아 ADR-008 본문과 ADR-011 사이 표면 모순. 이력 추적 시 혼란.
   160	
   161	### 옵션 B: ADR-008 Amendment 단독 (ADR-011 없음)
   162	
   163	- 장점: ADR-008 한 문서로 일관
   164	- 단점:
   165	  - "수단/목적 분리"는 R1을 넘어선 일반 원칙 — Amendment에 일반 원칙을 담는 것은 Amendment 형식 위반
   166	  - "Hermes ≠ root of trust" 운영 ADR화는 ADR-008 (Hermes 도입 결정) 범위 초과
   167	  - R-4~R-7이 Amendment를 권위 근거로 인용하는 것은 비표준 (Amendment는 specific 갱신 한정)
   168	
   169	### 옵션 C: ADR-011 신규 + ADR-008 Amendment ⭐ **채택**
   170	
   171	- 장점:
   172	  - 일반 원칙(수단/목적 분리, G1a/G1b 분리, Hermes ≠ root of trust, 학습/정책 분리)은 ADR-011로 권위화
   173	  - ADR-008 부록 A R1 specific 갱신은 Amendment로 짧게 처리 + ADR-011 cross-reference
   174	  - R-4~R-7이 ADR-011을 명확한 모법으로 인용
   175	  - ADR-008 본문 read 시 즉시 R-1 FAIL 후 갱신 사항 파악 가능
   176	- 단점: 작성 분량 2배 (수용)
   177	
   178	---
   179	
   180	## 5. 근거 (Rationale)
   181	
   182	### 5.1 헌법 제8조 본질 재해석의 정당성
   183	
   184	헌법 제8조의 비협상 본질은 "특정 hook이 존재해야 함"이 아니라 "비밀이 평문 영구 저장되지 않음"이다. R-2 PoC는 SQLCipher trigger 기반 fallback이 이 본질을 충족함을 실증했다.
   185	
   186	수단을 비협상으로 굳히면, 수단이 부재한 시점(현 Hermes v0.12.0)에 헌법 제8조 자체를 충족할 수 없는 모순이 발생한다. 본 ADR은 이 모순을 수단/목적 분리로 해소하되, 동시에 (a)~(d) 4조건으로 자의적 수단 대체를 차단한다.
   187	
   188	### 5.2 "Hermes ≠ root of trust" ADR 권위화 필요성
   189	
   190	system-identity-prequel은 임시 선언(Pre-Declaration)으로, R-7 완료 후 P2 v3 흡수와 함께 폐기된다. 그러나 "Hermes ≠ root of trust"는 폐기되어서는 안 되는 영구 권위 원칙이다. 본 ADR-011 §2.3으로 권위 승격하여 prequel 폐기 후에도 보존한다.
   191	
   192	### 5.3 G1a/G1b 분리의 영구화 필요성
   193	
   194	R-1 FAIL과 R-2 PASS는 Phase 0 evidence 보고서에 기록되어 있으나, 이는 보고서이지 ADR 권위가 아니다. G1a/G1b 분리를 ADR로 권위화하지 않으면 미래 합의에서 "G1 단일 게이트로 회귀 가능" 해석 위험이 발생한다. 본 ADR §2.2가 이를 차단한다.
   195	
   196	### 5.4 단축 합의(Reviewer-only)의 정당성
   197	
   198	본 R-3은 새 설계 안건이 아니라 R-1 FAIL + R-2 PASS + 단축 합의 §R-3 (`docs/review/3plus1-consensus-2026-05-05-p2-n1-redaction-reinterpretation.md`) + 풀 합의 §3 권위 위계 (`docs/review/3plus1-consensus-2026-05-05-system-identity-redefinition.md`) 의 ADR 형식화 작업이다. 새 합의 검증이 아니므로 풀 3+1은 과잉. 직전 R-1 단축 합의 패턴 답습.
   199	
   200	---
   201	
   202	## 6. 합의 결과 (단축 합의 — Reviewer-only)
   203	
   204	세부: `docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md`
   205	
   206	| 차원 | 판정 | 핵심 근거 |
   207	|------|------|---------|
   208	| 헌법 제8조 본질 충족 권위화 | **PASS** | §2.1 수단/목적 분리 + (a)~(d) 4조건 명시로 자의적 회귀·자의적 수단 대체 양방향 차단 |
   209	| G1a/G1b 분리 공식화 | **PASS** | R-1 FAIL evidence + R-2 PASS evidence 모두 인용, 정식 충족 조건 명시 |
   210	| Hermes ≠ root of trust 권위 승격 | **PASS** | prequel §3 → ADR §2.3 영구화, 운영 함의 5항목 명문화 |
   211	| 자동 학습 vs 정책 변경 분리 | **PASS** | T1/T2/T3 3-tier 분류 본문 흡수, R-5/R-6 권위 근거화 |
   212	| Provider Liquidity 영향 | **무관** | 본 ADR은 redaction 수단 해석이며 모델/구독 교체 자유와 무관 |
   213	| 메타 편향 통제 | **명시** | 본 ADR은 자체 코드 우호 결론(R-2 PASS)을 반영하나, (a)~(d) 4조건과 R-4~R-7 모법으로 회귀 견제 — 합의 보고서 §메타 편향 자기진단 참조 |
   214	
   215	---
   216	
   217	## 7. 결과 (Consequences)
   218	
   219	### 7.1 긍정적
   220	
   221	- 헌법 제8조 본질 충족이 specific 수단에 종속되지 않음 → 미래 Hermes API 변경 / upstream 변경 시에도 본질 보존 경로 확보
   222	- G1a/G1b 분리로 R-2 PASS evidence가 P2 v3에 직접 흡수 가능
   223	- "Hermes ≠ root of trust" ADR 권위화 → prequel 폐기 후에도 운영 원칙 영구 보존
   224	- R-4~R-7이 권위 근거 명확화 → 후속 작업 의사결정 비용 감소
   225	- 자동 학습/자동 정책 분리(T1/T2/T3)의 ADR 권위화 → silent 깨짐 자동 차단의 권위 근거
   226	
   227	### 7.2 부정적
   228	
   229	- ADR-008 부록 A R1의 표면 텍스트와 본 ADR §2.1 사이 텍스트 차이 존재 (Amendment로 동시 갱신하여 완화)
   230	- "수단/목적 분리"가 일반화되어 미래 다른 비협상 조항 해석에도 적용 시 합의 비용 발생 가능 (대체 수단 검증 부담 — 의도된 비용)
   231	- (a)~(d) 4조건 검증 부담은 본 ADR이 의도하는 안전 비용 — 회피 시도는 본 ADR 위반
   232	
   233	### 7.3 주의사항
   234	
   235	- 본 ADR의 (a)~(d) 4조건 미충족 시 수단 대체 불가 — "동등 이상의 보장" 검증을 PoC로 실증하지 않은 채 텍스트 해석만으로 수단 변경 금지
   236	- §2.4 자동 정책 변경 금지(T3) 위반 감지 시 Layer 1~2 hook(설정 파일 변경 감지)에서 차단 — CI/nightly 강제 (R-6 범위)
   237	- **본 ADR은 Hermes 안전성을 선언하지 않는다** — Hermes는 검증 대상이며, 본 ADR은 검증 외부화의 권위 근거이다.
   238	- ADR-009 (자체 Adapter v2.0 entry) / ADR-010 (SQLCipher Vault) 도 미래 본 ADR §2.1 (a)~(d) 4조건 적용 대상이 될 수 있음 — 적용 시점은 별도 합의로 결정
   239	
   240	---
   241	
   242	## 8. 관련 문서 (2026-05-09 후속 9 cross-reference 갱신, 결정 내용 변경 0건 — 단축 합의 APPROVE Reviewer-only)
   243	
   244	### 8.1 상위 권위
   245	- `docs/constitution/PROJECT_CONSTITUTION.md` 제8조 (보안), 제5조-2 관용 (Provider Liquidity, 비협상)
   246	- `docs/architecture/system-identity-prequel.md` §3 (권위 위계 prequel — 본 ADR §2.3으로 영구 권위 승격, prequel §6의 3-tier 선언 → 본 ADR §2.4 영구 권위 승격) — **Archived 2026-05-09 후속 8**, 본 ADR §2.3 / §2.4 영구 권위 승격 직접 명시 답습으로 archive 후에도 권위 보존. archive 합의: `docs/review/3plus1-consensus-2026-05-09-system-identity-prequel-archive-decision.md`
   247	
   248	### 8.2 갱신 대상 / 후속 권위
   249	- `docs/decisions/ADR-008-hermes-adoption-decision.md` 부록 B Amendment (R-3 동시 발행, 2026-05-06)
   250	- `docs/architecture/hermes-adoption-design.md` (P2 v2, **Archived 2026-05-09 후속 7** — 옵션 A 최소 침습)
   251	- **`docs/architecture/hermes-adoption-design-v3.md`** (P2 v3, **Adopted — Design Adoption only, 2026-05-09 후속 6, 후속 권위**) — 본 ADR §2.1 (수단/목적 분리) / §2.2 (G1a/G1b 분리) / §2.3 (Hermes ≠ root of trust) / §2.4 (T1/T2/T3) 모두 답습 권위 발행. P2 v3 §10.1 Normative Constraints + §10.2 Archive Migration Note + §3 dual-structure + §6 G4 + §7 ADR 매트릭스 + §11 변경 절차 + §11.1 Hermes PMO 격상 전 인간 전문 리뷰 의무화
   252	
   253	### 8.3 Phase 0 evidence
   254	- `docs/phase0/day1-environment-and-fact-check.md` (Hermes v0.12.0 사실 확인)
   255	- `docs/phase0/day2-r1-redaction-location-verification.md` (R-1 FAIL)
   256	- `docs/phase0/day3-r2-sqlite-trigger-poc.md` (R-2 PASS)
   257	- `docker/r2-poc/` (R-2 PoC Docker 격리 환경 + 6항목 자동 검증 스크립트)
   258	
   259	### 8.4 합의 보고서
   260	- `docs/review/3plus1-consensus-2026-05-05-p2-n1-redaction-reinterpretation.md` (단축 합의 §R-3 권고)

codex
핵심 brief 자체는 조건부 문구가 반복되어 있지만, Exit (a)를 “충족”으로 쓰는 부분이 실제 governance 기준과 충돌하는지 확인해야 합니다. 이제 §4.5와 선행 60/65/66/62의 해당 evidence 문구를 좁혀서 대조합니다.
exec
/bin/bash -lc 'rg -n "GP-2|Exit|Hermes native|facade|redaction|prevention|detection-tier|detection-layer|조건부|deferred|full|MVP-2" docs/architecture/governance-preconditions.md docs/phase0/mvp2-gp2-pass-activation-brief.md docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:1:# MVP-2 Implementation Evidence PASS (G4 ledger 완전 + GP-2 detection-tier, prevention/Layer 3·5/2a deferred) 발효 합의 entry brief (v1.1)
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:5:> **v1 → v1.1 갱신**: 풀 3+1 + 외부 LLM 1+ (codex gpt-5.5 cross-vendor) 통합 합의 (`docs/review/3plus1-consensus-2026-05-28-mvp2-final-pass.md`) **APPROVE WITH CONDITIONS (4 source 전원) → BLOCKING 3 + 권고 3 1pass 흡수**. ⭐ **핵심 정정 (B-1)**: 무수식 "MVP-2 PASS" 명칭 → **복합 자격 부착** (G4 ledger 완전 + GP-2 detection-tier, prevention R-1/R-2 + Layer 3·5 + 2a deferred) — 60 GP-2 detection-layer 강등 cascade 상위 재발 방지 (β B-1 / 59 B-2 / 60 B-1 4번째). B-2 "trajectory" 진행성 완화 + B-3 citation 정정. evidence 차단급 over-claim 0. §10 흡수 매트릭스 추가.
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:7:> **scope**: MVP-2 Implementation Evidence PASS **발효** (G4 ledger 무결성 *완전* + GP-2 송신 redaction *detection-tier*, prevention/Layer 3·5/2a *deferred*) — MVP-2 영역 (G2 GP-2 + G4 §4.4 Layer 1+2+4) 최종 milestone. ⚠️ **full GP-2 PASS (prevention) 아님**
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:11:> **본 cycle 발효 자격** = 3 의존성 충족 (Layer 통합 PASS + GP-2 detection-layer PASS + R-S1) + 풀 3+1 + 외부 LLM 1+ APPROVE + 사용자 명시
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:13:> **본 cycle 발효 효과** = **MVP-2 Implementation Evidence PASS 발효** (in-repo governance/CI 구현 evidence). **full GP-2 prevention (R-1 Hermes runtime redaction / R-2 facade real) + Layer 3+5 = MVP-2 PASS 후속 trajectory (deferred, 자동 진입 0)**
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:15:> **선행 답습 (3 의존성 모두 발효)**: 59 Layer 1+2+4 통합 PASS (`0f49eb9`) + 60 GP-2 detection-layer PASS (`92e9078`) + 61 R-S1 정정 (`bb59342`)
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:23:1. **3 의존성 충족 audit** (Layer 통합 PASS + GP-2 detection-layer PASS + R-S1) (§1)
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:24:2. **MVP-2 영역 ADR-011 §2.1 (a)~(d) 모법 + (e2) ADR-012 §4 확장 통합 매핑** (59 B-2 framing 답습) (§2)
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:25:3. **MVP-2 PASS scope 정직 명문** — Implementation Evidence PASS (in-repo evidence) + full GP-2 prevention + Layer 3+5 = deferred trajectory (60 over-claim 교훈 답습) (§3)
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:34:| 1 | MVP-2 PASS *발효* 자체 (본 brief = 합의 입력, 발효 = 합의 APPROVE + 사용자 명시 후) | 0 |
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:35:| 2 | **full GP-2 PASS 발효** (prevention R-1/R-2 = deferred trajectory) | 0 |
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:37:| 4 | R-1 Hermes import / R-2 facade real (TR-1) | 0 |
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:38:| 5 | Layer 통합 PASS / GP-2 detection-layer PASS / R-S1 재선언 | 0 (59/60/61 답습) |
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:42:| 9 | ADR / 헌법 / ADR-012 본문 갱신 (roadmap MVP-2 PASS 등록 = 발효 후 §5) | 0 |
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:51:- **60 GP-2 detection-layer PASS 발효 brief v1.1 + 합의** (`92e9078`) — `docs/phase0/mvp2-gp2-pass-activation-brief.md`
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:54:- **implementation-runtime-roadmap-mvp1.md §1.3** (GP-2 = MVP-2 분리) + **`3plus1-consensus-2026-05-07-g2-g3-g4-gate-adoption.md §C-7`** (line 378~379, GP-2 = MVP-2 우선순위 1 — B-3 정정: roadmap.md 아님)
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:63:| **GP-2 detection-layer PASS** | ✅ 60 entry (REVISE → v1.1 detection-layer reframe, 4 source) | `92e9078` | R-3 detection operative (secret-hygiene D-2 CI green) + R-4 설계 동등성 + ADR 권위. **prevention (R-1 Hermes / R-2 facade) = deferred trajectory (in-repo 입증 0, Hermes upstream 위임)** |
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:64:| **R-S1 cross-reference 정정** | ✅ 61 entry (Reviewer-only 단축 APPROVE) | `bb59342` | ADR-012 §2.3/§2.8 canonical numbering 선언 (§2.8/G4 §4.4.1 5-layer = canonical). MVP-2 "Layer 1+2+4" = 5-layer 기준 확정 |
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:66:→ **3 의존성 모두 발효** — MVP-2 Implementation Evidence PASS 발효 자격 충족 ((e2) = 본 cycle).
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:70:## §2 MVP-2 영역 ADR-011 §2.1 (a)~(d) + (e2) 통합 매핑 (59 B-2 framing 답습)
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:74:| 조건 | G4 §4.4 Layer 1+2+4 | G2 GP-2 (detection-layer) | MVP-2 통합 |
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:76:| (a) 동등 이상 보안 결과 | ✅ ledger 무결성 (hash chain + append-only + CI 회귀) | ⚠️ detection ✅ / prevention (R-1/R-2) deferred (60 답습) | ✅ ledger 완전 + GP-2 detection (prevention deferred 명문) |
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:80:| **(e2) 합의 APPROVE** | ✅ 59 | ✅ 60 (detection-layer) | ⏳ **본 cycle (MVP-2 통합 PASS)** |
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:82:→ **(a)~(d) = Implementation Evidence scope 충족** (B-1 정정): G4 축 (a) = 무결성 *완전* / **GP-2 축 (a) = detection + 설계 동등성, prevention (R-1/R-2) deferred** (60 답습 — full prevention 충족 아님). (e2) = 본 cycle MVP-2 통합 PASS 합의.
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:86:## §3 MVP-2 PASS scope 정직 명문 (60 over-claim 교훈 답습)
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:88:⭐ **MVP-2 Implementation Evidence PASS = in-repo governance/CI 구현 evidence PASS** (MVP-1 PASS 32 동형 — "Implementation Evidence" = 구현 evidence, runtime 보증 아님).
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:92:- ✅ GP-2 송신 redaction **detection**: secret-hygiene D-2 CI (redaction residual 검출) operative green
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:94:**deferred (명문, 자동 진입 0)** — ⚠️ B-2: "trajectory" 진행성 함의 회피 (R-1 = import 결정조차 미진입, R-2 = placeholder):
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:95:- ⚠️ **GP-2 prevention (능동 redaction)**: R-1 Hermes runtime redaction (upstream 위임, ADR-011 §2.3 #2) + R-2 facade real (TR-1) — **in-repo 입증 0 + Hermes safety 미선언** (ADR-011 §7.3 / ADR-012 §3.3 답습 — redaction-pattern-equivalence = 설계 동등성, 안전 선언 아님). R-1 import 미결정 / R-2 placeholder. **full GP-2 PASS = MVP-2 PASS 후속 (deferred)**
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:98:- ⚠️ **R-5 base64 evasion**: known limitation (G3-4 MVP-2/3 분리)
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:100:→ **MVP-2 PASS = ledger 무결성 완전 + GP-2 detection operative + 설계/CI 권위. prevention runtime + Layer 3/5 + denyNonFastForwards = solo 1-host 비례 보안 + upstream 위임 deferred (over-claim 0, 정직 scope)**.
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:108:**정당화**: MVP-2 최종 milestone (32 MVP-1 PASS 발효 답습) + 큰 결정 (ADR-011 §2.4 T3) + 헌법 5조-2 cross-vendor + 사용자 명시 (32 답습).
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:114:| 1 | 큰 결정 (MVP-2 최종 PASS milestone) | ✅ |
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:128:⭐ **권고 = MVP-2 Implementation Evidence PASS (G4 ledger 완전 + GP-2 detection-tier, prevention/Layer 3·5/2a deferred) 발효 APPROVE WITH CONDITIONS** (B-1: 복합 자격 부착, 무수식 "MVP-2 PASS" 회피):
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:130:1. **3 의존성 충족** (Layer 통합 PASS 59 + GP-2 detection-layer PASS 60 + R-S1 61) + (a)~(d) 충족.
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:132:   - (C-1) **MVP-2 PASS scope = Implementation Evidence (in-repo). full GP-2 prevention (R-1/R-2) + Layer 3/5 + 2a = deferred trajectory 명문** (§3, over-claim 0)
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:133:   - (C-2) **roadmap/governance MVP-2 PASS 등록 = 발효 후 별도 commit** (사용자 명시, 32 동형 — roadmap-mvp1 §2.2 갱신 패턴)
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:138:- `implementation-runtime-roadmap.md` / `-mvp1.md`: MVP-2 Implementation Evidence PASS 발효 등록 (별도 commit, 발효 후)
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:139:- governance-preconditions §4 (GP-2): detection-layer PASS + prevention deferred cross-reference (선택)
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:140:- MVP-2 PASS = MVP-3 (다른 GP/G 영역) 진입 자격 (별도 cycle)
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:142:→ **MVP-2 PASS 발효 자격 = 3 의존성 + (a)~(d) + (e2) 합의 APPROVE + 사용자 명시 + (C-1) deferred trajectory 명문**.
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:148:§0.2 답습 (12). 추가: full GP-2 PASS 자동 발효 0 / Layer 3/5 진입 0 / R-1 import 0 / R-2 facade 0 / MVP-3~6 자동 진입 0 / roadmap 본문 자동 갱신 0 (발효 후 별도) / 자동 후속 0.
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:154:1. 본 brief 승인 → 풀 3+1 + 외부 LLM 1+ (codex (E-α)) → Reviewer 통합 → v1.1 흡수 → commit + push → 🎉 **MVP-2 Implementation Evidence PASS 발효 (G4 ledger 완전 + GP-2 detection-tier, prevention/Layer 3·5/2a deferred — ⚠️ full GP-2 PASS 아님)**
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:155:2. roadmap/governance MVP-2 PASS 등록 (발효 후 별도 commit, 사용자 명시)
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:156:3. **full GP-2 PASS trajectory** (R-1 Hermes runtime redaction import / R-2 facade real TR-1 prevention)
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:164:- 59 Layer 통합 PASS (`0f49eb9`) + 60 GP-2 detection-layer PASS (`92e9078`) + 61 R-S1 (`bb59342`)
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:166:- implementation-runtime-roadmap-mvp1.md §1.3 + `3plus1-consensus-2026-05-07-g2-g3-g4-gate-adoption.md §C-7` (GP-2 = MVP-2, B-3 정정)
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:174:| P-1 | MVP-2 PASS *기정사실화* | 발효 = 합의 APPROVE + 사용자 명시 후 (§0.2 #1 + §7) |
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:175:| P-2 | **MVP-2 "full PASS" over-claim (60 GP-2 over-claim 재발)** | §3 정직 scope 명문 — Implementation Evidence PASS (in-repo), full GP-2 prevention + Layer 3/5 + 2a = deferred trajectory. "runtime 완전 보증" 표현 0 |
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:176:| P-3 | GP-2 detection-layer 를 MVP-2 통합 시 "full GP-2" 로 격상 | §1 + §2 (a) + §3 = GP-2 detection-layer + prevention deferred 일관 명문 |
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:191:| B-1 ⭐ (4 source 수렴) | 무수식 "MVP-2 PASS" → 복합 자격 "(G4 ledger 완전 + GP-2 detection-tier, prevention/Layer 3·5/2a deferred)" 부착 (title + §2 결론 + §5 + §7) + "GP-2 detection-layer PASS" 고정 — 60 cascade 상위 재발 방지 | Agent C R-C-1 + Agent B R-B-1 + codex 권고 1/2/3 | title/§2/§3/§5/§7 |
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:192:| B-2 | "deferred trajectory" → "deferred (R-1 import 미결정 / R-2 placeholder, in-repo 입증 0 + Hermes safety 미선언)" | Agent B R-B-2 | §3 |
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:195:| N-2 | deferred 진입 trigger 매트릭스 | Agent C | §3 (선택) |
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:204:**다음 단계**: SESSION + INDEX commit + push → 🎉 **MVP-2 Implementation Evidence PASS 발효 (G4 ledger 완전 + GP-2 detection-tier, prevention/Layer 3·5/2a deferred)**. 후속: roadmap/governance MVP-2 PASS 등록 (발효 후 별도 commit) + full GP-2 PASS trajectory (R-1/R-2) = 사용자 명시 별도 cycle.
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:5:> **v1 → v1.1 갱신 (reframe)**: 풀 3+1 + 외부 LLM 1+ (codex gpt-5.5 cross-vendor) 통합 합의 (`docs/review/3plus1-consensus-2026-05-28-mvp2-sc2.md`) **APPROVE WITH CONDITIONS (4 source 전원) → BLOCKING 4 + 권고 4 reframe 흡수** (60 detection reframe 동형). **핵심 정정 (60 over-claim cascade 재발)**: **B-1 축 3 R-6 자동 회귀 over-claim** (Reviewer verify: r2-canary.yml = R-4.1 Tier-1 42 catalog canary, **Hermes dependency lock trigger 미구현** — Hermes egress 자동 회귀 아님) → "ADR 의무 *요구* / 현 R-6 Tier-1 catalog operative" / **B-2 HERMES_REDACT_SECRETS opt-in 활성화 전제** (기본 false, v0.12.0 ON→OFF) → "활성화된 Hermes redaction" / **B-3** artifact 부재 완화 (docker/r2-poc 골격 존재) + URL 출처 불명 / **B-4** 위치 evidence 시점성. **"충족" → "조건부/문서 기반 충족"** (R-1 prong = Exit (a) Hermes-native sub-evidence). evidence 실증 (위치+동등성), framing over-claim 정정. §11 흡수 매트릭스 추가.
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:7:> **scope** (사용자 명시 "문서 종합 위임 검증 + contract"): **R-1 (Hermes native redaction) 위임 검증 종합** — day2-r1 (위치) + R-4 §5 (동등성) + R-6 (Tier-1 canary, Hermes 자동 회귀 *의무*) + ADR-011 §2.3 #2 (위임 권위) 종합 + **evidence contract 명문** (version pin v0.12.0 + R-6 + 격리 실행 SOP). **실 격리 canary 실행 = artifact 재확보 시점 deferred** (day2-r1 "코드 분석 충분" 선례). 실 코드 0.
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:9:> ⚠️ **over-claim 경계 (본 세션 #2 4회 cascade 교훈 + R-4 §7.3 답습)**: 본 cycle = **R-1 위임 *검증* (Hermes 가 GP-2 영역에 redaction 적용 + Tier-1 동등 이상 커버 + 자동 회귀)**. ≠ **"Hermes 안전성 선언"** (ADR-011 §7.3 "본 ADR 은 Hermes 안전성을 선언하지 않는다" 금지). 위치/동등성 *사실* 검증이지 "Hermes redaction 완벽" 선언 아님.
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:11:> **본 cycle = 큰 cycle** (full GP-2 PASS Exit (a) R-1 prong, 풀 3+1 + 외부 LLM 1+).
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:13:> **본 cycle 발효 효과** = full GP-2 PASS Exit (a) **R-1 prong 위임 검증 충족** (Hermes upstream 위임 실효 확인). R-2 prong = SC-1 (facade RedactionFilter) ✅ 이미 발효 → **full GP-2 PASS = R-1 ∧ R-2 충족 → SC-3 발효 합의 (별도)**.
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:15:> **선행 답습**: 65 SC-1 (R-2 facade RedactionFilter operative) + 64 trajectory §3 (R-1 = upstream 위임, (R-1-a) 권고 + evidence contract 의무) + day2-r1 (R-1 위치 검증) + R-4 §5 (Hermes ⊇ Tier-1) + ADR-011 §2.3 #2 (위임 권위)
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:25:3. **실 격리 canary 실행 deferred 정당화** (day2-r1 선례 + artifact 부재) (§4)
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:34:| 2 | **full GP-2 PASS 발효** (SC-3 별도 cycle — R-1 ∧ R-2 충족 후) | 0 |
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:36:| 4 | **실 격리 canary 실행** (artifact 부재 → 재확보 시점 deferred, SOP 명문만) | 0 |
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:41:| 9 | SC-1 (R-2) 재선언 / detection-layer PASS (60) 재선언 | 0 |
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:46:- **day2-r1** (`docs/phase0/day2-r1-redaction-location-verification.md`) — R-1 *위치* 검증 (Hermes redaction = 로그/도구출력/gateway 통신 전용, 25 import 비-DB, docstring "mask API keys/tokens/credentials before log/output/gateway"). ⚠️ day2-r1 "FAIL" = **G1a (DB INSERT 경로) 맥락** (DB = GP-1 책임). **GP-2 (송신/로그) 맥락에서는 Hermes redaction 적용 ✅** (위임 근거).
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:47:- **R-4 §5** (`docs/architecture/redaction-pattern-equivalence.md`) — Hermes **47 카테고리 + 2 frozenset ⊇ Tier-1 45 catalog** (Hermes ⊇ P1_REDACTOR ⊇ baseline). §7.3 "Hermes 안전성 선언 금지".
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:49:- **ADR-011 §2.3 #2** (line 113) — "Hermes 자체 redaction 은 로그/LLM 송신 방어로만 신뢰" (R-1 위임 권위) + §2.3 #4 (자동 회귀) + §7.3 (안전성 선언 금지).
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:50:- **governance §4.5 (a)** — "Hermes native redaction Tier-1 42 catalog 적용 검증 + facade redaction filter 검증" (R-1 + R-2). **§1.2.7 P11 / Layer 1** — hermes-version.yaml v0.12.0 pin.
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:51:- **65 SC-1** — R-2 prong (facade RedactionFilter) operative.
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:58:- 65 SC-1 (R-2 facade RedactionFilter) operative → full GP-2 PASS Exit (a) R-2 prong ✅.
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:59:- 본 SC-2 = R-1 prong (Hermes native redaction 위임 검증). full GP-2 PASS = R-1 ∧ R-2 (AND, 64 trajectory §2.2).
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:66:### §2.1 축 1 — 위치 검증 (활성화된 Hermes redaction = GP-2 영역 적용) ✅ (시점성 명시)
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:69:- **사실 1**: `agent/redact.py:1-8` docstring = "Regex-based secret redaction **for logs and tool output** ... mask API keys, tokens, and credentials **before they reach log files, verbose output, or gateway logs**".
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:70:- **사실 2**: redaction import 25개 위치 = 로깅/도구출력/통신 경로 (DB write 0).
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:71:- **사실 3**: `hermes_state.py` (SessionDB) redaction import 0 (DB INSERT 미적용).
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:73:→ **활성화된 Hermes redaction = GP-2 영역 (로그/LLM 송신/도구출력) 적용 ✅**. day2-r1 "FAIL" = G1a (DB INSERT) 맥락 (DB = GP-1 책임, ADR-011 §2.3 #2/#3) — **GP-2 위임 근거와 모순 0** (GP-2 영역 적용 입증).
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:75:⚠️ **B-2 활성화 전제 (위임 실효 필수 조건)**: `HERMES_REDACT_SECRETS=false` = **기본 opt-in** (R-4 line 138, v0.12.0 breaking change default ON→OFF). day2-r1 §2 "security.redact_secrets: true 활성화 후" 전제. → 위임 검증 = **`HERMES_REDACT_SECRETS=true` 활성화 전제** (미활성화 시 redaction 미작동). evidence contract C-5 (활성화 config 검증, §3) 신설.
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:86:→ **활성화된 Hermes native redaction 이 Tier-1 42 catalog 를 동등 이상 커버 ✅** (governance §4.5 (a) "Tier-1 42 catalog 적용" 충족). ⚠️ R-4 = 설계 동등성 비교 (§7.3 안전성 선언 아님) — "Hermes 가 Tier-1 패턴을 *포함*" 사실 검증. **출처 (R-2 정정)**: R-4 §5 동등성 매트릭스 **+ R-4.1/R-6 catalog 체계** (R-4 §5 단독 아님 — Tier-1 42/45 = R-4.1 확장).
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:91:- **현 R-6 (r2-canary.yml) = "R-4.1 Tier-1 42 catalog canary regression"** (nightly cron `0 18 * * *` + PR). paths trigger = `docker/r4-1-poc` + `docker/r2-poc` + canary-recheck-design.md + workflow. **`hermes-version.yaml` / Hermes dependency lock diff trigger 0** → **Hermes native redaction egress 자동 회귀 *아님*** (우리 Tier-1 catalog canary).
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:98:- ADR-011 §2.3 #2: "Hermes 자체 redaction 은 로그/LLM 송신 방어로만 신뢰, 저장 경로 책임 0".
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:113:| C-3 | **격리 실행 SOP** | day2-r1 §7 R-2 PoC 절차 + docker/r2-poc 골격 (B-3) | SOP 명문 (실 실행 deferred, §4) |
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:120:3. Hermes redaction 경로 (로그/송신) 통과 → `[REDACTED]` 또는 부분 마스킹 확인
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:126:## §4 실 격리 canary 실행 deferred 정당화
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:128:⚠️ **현 상태**: Hermes `agent/redact.py` artifact 부재 (/tmp/hermes-phase0 휘발 + 본 repo 부재) + Hermes upstream clone URL 문서 미명시. **단 R-2 PoC 격리 골격 `docker/r2-poc/` 존재** (Dockerfile + compose + r2_poc.py, B-3 — "artifact 완전 부재" 아님, 우리 PoC 골격은 보존) → Hermes native 실 격리 canary 실행 *미시행*.
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:130:**deferred 정당화 (day2-r1 선례 답습)**:
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:135:→ **R-1 위임 검증 = 코드/문서 분석 기반 충족** (day2-r1 동형). 실 격리 canary = deferred (C-3 SOP, artifact 재확보 trigger).
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:141:⭐ **판정 = R-1 위임 검증 *조건부/문서 기반 충족* (Exit (a) Hermes-native sub-evidence, R-1+codex reframe)**:
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:143:- governance §4.5 (a) "Hermes native redaction Tier-1 42 catalog 적용 검증" = **Exit (a)의 Hermes-native sub-evidence 조건부 충족** (축 1+2, 활성화 전제 + R-6 Tier-1 한정 + 위치 시점성 + URL 불명). GP-2 Exit (b) 격리 PoC / (d) R-6 log canary step = SC-3 또는 별도 (R-3 경계).
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:146:- **R-1 위임 검증 ≠ Hermes 안전성 선언** (ADR-011 §7.3). "활성화된 Hermes 가 GP-2 영역에 redaction 적용 + Tier-1 동등 이상 커버" *사실* 검증.
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:147:- **조건부/문서 기반 충족** (실 격리 canary 실행 deferred, 활성화 전제, R-6 Tier-1 한정) — day2-r1 동형, "실 실행 완료" 0, "Hermes 자동 회귀 operative" 0.
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:148:- **full GP-2 PASS ≠ 본 cycle** — R-1 (SC-2 조건부) ∧ R-2 (SC-1 in-repo) → SC-3 발효 합의 (별도).
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:150:→ **full GP-2 PASS Exit (a) = R-1 prong (SC-2 조건부/문서 기반) + R-2 prong (SC-1 ✅ in-repo operative) → SC-3 발효 자격** (실 격리 canary + Hermes 자동 회귀 R-6 확장 = SC-3 강한 보강 또는 별도 trigger).
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:158:**정당화**: full GP-2 PASS Exit (a) R-1 prong (보안 영역) + 큰 결정 (위임 검증 milestone) + 5조-2 cross-vendor + Hermes ≠ root of trust (다중 검증 의무).
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:164:| 1 | 큰 결정 (full GP-2 PASS R-1 prong) | ✅ |
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:165:| 2 | 보안 (GP-2 prevention 위임) | ✅ |
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:175:§0.2 답습 (10). 추가: Hermes 안전성 선언 0 / 실 격리 canary "실행 완료" 주장 0 / agent/redact.py import 0 / full GP-2 PASS 발효 0 / hermes-version.yaml 파일 생성 0 (절충안 deferred) / 자동 SC-3 진입 0.
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:183:| RT-1 | Hermes upstream v0.12.0 redaction silent 깨짐 | R-6 자동 재실행 (r2-canary.yml) + R-5 canary 재검증 |
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:192:- E-1: day2-r1 위치 검증 (Hermes redaction = GP-2 영역, 25 import 비-DB)
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:196:- E-5: C-3 격리 실행 SOP (artifact 재확보 시, deferred)
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:205:| P-2 | day2-r1 "FAIL" 을 GP-2 위임 부정으로 오인 | §2.1 — "FAIL" = G1a (DB) 맥락, GP-2 (송신) 적용 ✅ (모순 0) |
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:206:| P-3 | 실 격리 canary 미실행 → 검증 미충족 오인 | §4 — day2-r1 "코드 분석 충분" 선례 + deferred 명문 ("실 실행 완료" 0) |
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:207:| P-4 | full GP-2 PASS 기정사실화 | §5 — R-1 ∧ R-2 → SC-3 별도 (§0.2 #2) |
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:208:| P-5 | R-4 설계 동등성을 prevention 입증으로 격상 | §2.2 — R-4 = 패턴 *포함* 사실 (§7.3 안전성 선언 금지) |
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:221:| B-2 ⭐ | HERMES_REDACT_SECRETS opt-in (기본 false) → "활성화된 Hermes redaction" + C-5 활성화 검증 전제 신설 | codex+A+B | §2.1 + §3 C-5 |
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:224:| R-1 | "R-1 prong 충족" → "Exit (a) Hermes-native sub-evidence 조건부/문서 기반 충족" | codex 3 | §5 + title |
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:226:| R-3 | GP-2 Exit (b)/(d) = SC-3 또는 별도 (R-1 prong 경계) | codex 3 | §5 |
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:229:**4 source 정합 (positive)**: over-claim 1차 경계 (Hermes 안전성 선언/full GP-2 PASS 격상/실 실행 완료 주장) 견고 / day2-r1 FAIL 재해석 타당 (G1a DB ≠ GP-2 송신, 4 source 공통) / R-2 prong (SC-1) 발효 filesystem 실측 / 권위 인용 일치 (codex 6/8, R-6 dependency trigger 부분만).
docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:235:**다음 단계**: SESSION + INDEX commit + push → **R-1 위임 검증 조건부/문서 기반 충족 (활성화 전제 HERMES_REDACT_SECRETS=true + R-6 Tier-1 한정 + 위치 시점성)**. 후속: **SC-3 (full GP-2 PASS 발효 합의)** — R-1 (SC-2 조건부) ∧ R-2 (SC-1 in-repo) + 실 격리 canary + Hermes 자동 회귀 R-6 확장 보강 = 사용자 명시 별도 cycle.
docs/phase0/mvp2-gp2-pass-activation-brief.md:1:# GP-2 detection-layer PASS 발효 합의 entry brief (v1.1)
docs/phase0/mvp2-gp2-pass-activation-brief.md:5:> **v1 → v1.1 갱신**: 풀 3+1 + 외부 LLM 1+ (codex gpt-5.5 cross-vendor) 통합 합의 (`docs/review/3plus1-consensus-2026-05-28-mvp2-gp2-pass-activation.md`) **REVISE (3-way framing over-claim) → BLOCKING 2 + 권고 4 1pass 흡수**. ⭐ **핵심 정정 (B-1)**: "GP-2 (full) 송신 redaction PASS" + "(a) ✅" = over-claim → **"GP-2 detection-layer PASS"** 강등. (a) 동등 이상 보안 결과 = governance §4 상 R-1/R-2 prevention 검증인데 deferred (redaction-pattern-equivalence = 설계 동등성 문서, Hermes safety 선언 아님). evidence 자체는 실증 (over-claim 0, β B-1 / 59 B-2 framing 동형). §11 흡수 매트릭스 추가.
docs/phase0/mvp2-gp2-pass-activation-brief.md:7:> **scope**: G2 GP-2 **detection-layer** PASS **발효 (e2)** — R-3/D-2 자동 회귀 검증 operative. **full GP-2 PASS (prevention R-1/R-2) = 잔여 trajectory (deferred)**
docs/phase0/mvp2-gp2-pass-activation-brief.md:13:> **본 cycle 발효 효과** = **GP-2 detection-layer PASS 발효** (R-3/D-2 회귀 검증 + R-4 설계 동등성 + ADR 권위). prevention (R-1 Hermes runtime / R-2 facade real) = in-repo 입증 0, Hermes upstream 위임 (ADR-011 §2.3 #2). MVP-2 Implementation Evidence PASS = Layer 통합 PASS (59 ✅) + GP-2 detection-layer PASS (본 cycle) + R-S1 hard gate → **full GP-2 PASS (prevention) = MVP-2 PASS 잔여 trajectory (별도 cycle)**
docs/phase0/mvp2-gp2-pass-activation-brief.md:15:> **선행 답습**: 51 audit (GP-2 Exit 5조건, R-1~R-5 후보) + 57 ((β) R-4 = R-3 detection 우선 + R-1/R-2 prevention deferred) + 59 (Layer 통합 PASS 발효, means-vs-ends + DEFER 패턴 답습)
docs/phase0/mvp2-gp2-pass-activation-brief.md:23:1. **GP-2 Exit 5조건 evidence 매트릭스** ((a)~(d) + (e2)) — 51 audit §2.2 현행화 (§2)
docs/phase0/mvp2-gp2-pass-activation-brief.md:24:2. **R-3 detection (operative) + R-1/R-2 prevention (deferred trajectory) 분리** (57 (β) + 59 Layer 2a DEFER 패턴 답습) (§3)
docs/phase0/mvp2-gp2-pass-activation-brief.md:28:6. **GP-2 PASS 발효 권고 + 조건** (§6)
docs/phase0/mvp2-gp2-pass-activation-brief.md:35:| 1 | GP-2 PASS *발효* 자체 (본 brief = 합의 입력, 발효 = 합의 APPROVE + 사용자 명시 후) | 0 |
docs/phase0/mvp2-gp2-pass-activation-brief.md:36:| 2 | **MVP-2 Implementation Evidence PASS 발효** (Layer 통합 PASS + GP-2 PASS + R-S1 후 별도) | 0 |
docs/phase0/mvp2-gp2-pass-activation-brief.md:37:| 3 | **R-1 Hermes import 결정** (prevention 구현 경로, 별도 cycle) | 0 |
docs/phase0/mvp2-gp2-pass-activation-brief.md:38:| 4 | **R-2 facade real (TR-1)** (prevention 구현 경로, 별도 trajectory) | 0 |
docs/phase0/mvp2-gp2-pass-activation-brief.md:39:| 5 | R-5 base64/URL-encoded/압축 evasion 영역 진입 (MVP-2/3 분리, G3-4) | 0 |
docs/phase0/mvp2-gp2-pass-activation-brief.md:41:| 7 | R-S1 cross-reference 정정 (MVP-2 PASS 전 hard gate, 별도 cycle) | 0 |
docs/phase0/mvp2-gp2-pass-activation-brief.md:44:| 10 | secret_scanner.py / secret-hygiene-egress-redaction.yml 본문 변경 | 0 (PoC 시제 보존) |
docs/phase0/mvp2-gp2-pass-activation-brief.md:45:| 11 | 자동 후속 cycle 진입 (MVP-2 PASS / R-S1) | 0 (사용자 명시 의무) |
docs/phase0/mvp2-gp2-pass-activation-brief.md:50:- **ADR-011 §2.1 (a)~(d) 4조건 모법** (line 52~61) — `docs/decisions/ADR-011-means-vs-ends-redaction.md`
docs/phase0/mvp2-gp2-pass-activation-brief.md:51:- **ADR-011 §2.3 운영 함의 #2** (Hermes redaction = 로그/LLM 송신 방어 신뢰, 저장 경로 책임 0) — 동상 line 112
docs/phase0/mvp2-gp2-pass-activation-brief.md:53:- **governance-preconditions.md §4** (GP-2 Egress Redaction Entry/Exit) — `docs/architecture/governance-preconditions.md`
docs/phase0/mvp2-gp2-pass-activation-brief.md:54:- **`docs/architecture/redaction-pattern-equivalence.md`** (R-4, (a) 설계 동등성) + **`docs/phase0/r4-1-trigger-extension-evidence.md`** (R-4.1, (b) PoC — N-2 경로 정정: phase0, architecture 아님)
docs/phase0/mvp2-gp2-pass-activation-brief.md:55:- **51 audit §2** (GP-2 Exit 5조건) — `docs/phase0/mvp2-entry-eligibility-audit-brief.md`
docs/phase0/mvp2-gp2-pass-activation-brief.md:56:- **57 (β) brief v1.1** (R-4 = R-3 detection + R-1/R-2 prevention deferred) — `docs/phase0/mvp2-beta-submeans-decision-brief.md`
docs/phase0/mvp2-gp2-pass-activation-brief.md:68:| 59 Layer 1+2+4 통합 PASS 발효 (`0f49eb9`, 4 source APPROVE WITH CONDITIONS) | MVP-2 = Layer 통합 PASS ✅ + **GP-2 PASS (본 cycle)** + R-S1. means-vs-ends + DEFER 패턴 + B-2 (a)~(d)/(e2) framing 답습 |
docs/phase0/mvp2-gp2-pass-activation-brief.md:69:| 57 (β) R-4 결정 (`18e8ad1`) | GP-2 수단 = R-4 (R-3 detection 우선 + R-1/R-2 prevention deferred trajectory). R-5 영구 분리 |
docs/phase0/mvp2-gp2-pass-activation-brief.md:70:| 51 audit §2 (`f7ac61d`) | GP-2 Exit 5조건 — 본 cycle 현행화 (51 audit "(d) gap" = 부정확, secret-hygiene D-2 이미 운영) |
docs/phase0/mvp2-gp2-pass-activation-brief.md:72:### §1.2 GP-2 = 송신 redaction 영역 정의 (governance §4)
docs/phase0/mvp2-gp2-pass-activation-brief.md:75:- ADR-011 §2.3 #2: "Hermes 자체 redaction은 로그/LLM 송신 방어로만 신뢰, 저장 경로 차단 책임 0" (DB INSERT = GP-1 책임).
docs/phase0/mvp2-gp2-pass-activation-brief.md:76:- 본 repo = DESIGN/governance repo (docs + tools + CI). 실 runtime redaction = Hermes upstream (R-1). 본 repo GP-2 PASS = redaction 패턴 정의 (R-4) + CI 회귀 검출 (R-3) + 설계 권위 (ADR-011 §2.3).
docs/phase0/mvp2-gp2-pass-activation-brief.md:80:## §2 Evidence 매트릭스 (GP-2 Exit 5조건, 51 audit §2.2 현행화)
docs/phase0/mvp2-gp2-pass-activation-brief.md:82:⭐ **B-1 정정**: GP-2 Exit 조건을 **3축 분리** (detection-layer PASS scope 명확화) — (a) 설계 동등성 ≠ prevention 입증, prevention 능동 redaction 은 in-repo 입증 0 (Hermes upstream 위임).
docs/phase0/mvp2-gp2-pass-activation-brief.md:84:**축 1 — detection-layer (본 cycle PASS scope, operative ✅)**:
docs/phase0/mvp2-gp2-pass-activation-brief.md:88:| (b) | 격리 환경 PoC 실증 (detection) | ✅ | secret-hygiene D-2 scan-log redaction PoC (`redaction_pass/env_redacted.txt` rc=0 잔존 0 + `redaction_fail/partial_redact.txt` rc=1 leak 검출) + `r4-1-trigger-extension-evidence.md` (R-4.1 PoC) — N-3: 51 "(b) 부분" → ✅ 격상 근거 = secret-hygiene D-2 송신 redaction residual CI |
docs/phase0/mvp2-gp2-pass-activation-brief.md:89:| (d) | 자동 회귀 검증 경로 (detection) | ✅ ⭐ | **`secret-hygiene-egress-redaction.yml` D-2 step (scan-log redaction residual, `secret_scanner.py --mode scan-log`) — 51 audit "❌ gap" 부정확 정정 (52 entry PoC 시제 발견 동형). actual run `26517803107` success (headSha `4fec6485`). secret-hygiene = `workflow_dispatch` 미지원 (schedule cron `0 3 * * *` 만) — secret_scanner.py + workflow + redaction fixtures = 49 entry (`4fec6485`) 이후 변경 0 (불변) → 유효 evidence** |
docs/phase0/mvp2-gp2-pass-activation-brief.md:90:| (c) | ADR/SDD 권위 명시 | ✅ | ADR-011 §2.3 #2 (송신 방어 신뢰, 저장 경로 책임 0) + governance §4 (GP-2 정의) |
docs/phase0/mvp2-gp2-pass-activation-brief.md:92:**축 2 — 설계 동등성 (⚠️ partial, prevention 입증 아님)**:
docs/phase0/mvp2-gp2-pass-activation-brief.md:96:| (a) | 동등 이상 보안 결과 | ⚠️ **partial (설계 동등성 한정)** | `redaction-pattern-equivalence.md` (R-4 — Tier-1 42 catalog 패턴 *동등성 문서*). ⚠️ **B-1**: governance §4 (a) (line 451) = "Hermes native redaction 적용 검증 + facade redaction filter 검증" = **prevention (R-1/R-2) 검증** — 현 상태 R-1 부재 + R-2 placeholder. redaction-pattern-equivalence = 설계 비교 문서 (line 33 Hermes safety 선언 *금지*), prevention *입증* 아님. → (a) full 충족 = R-1/R-2 prevention 선행 (deferred) |
docs/phase0/mvp2-gp2-pass-activation-brief.md:98:**축 3 — prevention (능동 redaction, in-repo 입증 0 = Hermes upstream 위임)**:
docs/phase0/mvp2-gp2-pass-activation-brief.md:102:| R-1 Hermes native redaction | ❌ 본 repo 부재 | Hermes upstream runtime operative (ADR-011 §2.3 #2 위임 권위), import 결정 별도 cycle |
docs/phase0/mvp2-gp2-pass-activation-brief.md:103:| R-2 facade RedactionFilter | ⚠️ placeholder | facade real (TR-1) deferred trajectory |
docs/phase0/mvp2-gp2-pass-activation-brief.md:105:→ **detection-layer PASS = (b)(d)(c) ✅ operative + (a) 설계 동등성 partial. prevention (R-1/R-2) = in-repo 입증 0 (upstream 위임)**. (e2) = 본 cycle 풀 3+1 + 외부 LLM 1+ + 사용자 명시. **full GP-2 PASS = detection-layer + prevention (R-1/R-2) 선행 (별도 trajectory)**.
docs/phase0/mvp2-gp2-pass-activation-brief.md:109:## §3 R-3 detection (operative) + R-1/R-2 prevention (deferred) 분리 (57 (β) + 59 Layer 2a 답습)
docs/phase0/mvp2-gp2-pass-activation-brief.md:115:| **R-3** log canary CI (`secret-hygiene-egress-redaction.yml` + `secret_scanner.py --mode scan-log`) | **detection (회귀 검증)** | ✅ operative green | GP-2 (d) 자동 회귀 충족 — in-repo operative means |
docs/phase0/mvp2-gp2-pass-activation-brief.md:116:| **R-1** Hermes native redaction (`agent/redact.py`) | **prevention (능동 redaction)** | ❌ 본 repo 부재 (Hermes upstream v0.12.0) | runtime prevention = Hermes upstream operative (import 결정 별도 cycle). ADR-011 §2.3 #2 송신 방어 신뢰 |
docs/phase0/mvp2-gp2-pass-activation-brief.md:117:| **R-2** facade RedactionFilter | prevention (LLM API 진입점) | ⚠️ facade placeholder | facade real (TR-1) 시점 추가 layer (deferred trajectory) |
docs/phase0/mvp2-gp2-pass-activation-brief.md:118:| **R-5** base64/URL/압축 evasion | (out of scope) | ❌ known limitation (`base64_evasion.txt` fixture) | 영구 분리 (MVP-2/3, G3-4) |
docs/phase0/mvp2-gp2-pass-activation-brief.md:124:- **prevention ends** = R-1 (Hermes upstream native redaction, 실 runtime operative — 본 repo DESIGN repo 이므로 import 미결정) + R-2 (facade real deferred). **본 repo in-repo 능동 redaction 보증 0**.
docs/phase0/mvp2-gp2-pass-activation-brief.md:125:- ⚠️ **B-2 — 59 Layer 2a 와 *부분 동형* (의사결정 형식만, cover 구조 비대칭)**: 59 = DEFER ends (history rewrite 차단) 가 **in-repo 2 operative layer** (2b branch protection + rewrite-defense CI) 이중 cover. GP-2 = DEFER prevention (능동 redaction) ends 를 cover 하는 **in-repo layer 0** — Hermes upstream (repo 외부) 단독 위임 (ADR-011 §2.3 #2). 즉 보안 cover 구조 비대칭, "완전 동형" 표현 회피.
docs/phase0/mvp2-gp2-pass-activation-brief.md:127:→ **GP-2 detection-layer PASS = detection (R-3 in-repo operative) + 설계 권위 + 패턴 동등성 (설계 한정). prevention 능동 redaction = in-repo 보증 0, Hermes upstream 위임 (R-1) + facade real (R-2) deferred trajectory = full GP-2 PASS 선행** (57 (β) 결정 답습, 59 DEFER *부분* 동형).
docs/phase0/mvp2-gp2-pass-activation-brief.md:135:| 조건 | 출처 | GP-2 detection-layer 충족 |
docs/phase0/mvp2-gp2-pass-activation-brief.md:137:| (a) 동등 이상 보안 결과 | ADR-011 §2.1 | ⚠️ **partial (설계 동등성 한정)** — R-4 패턴 동등성 문서. full = R-1/R-2 prevention 검증 선행 (B-1) |
docs/phase0/mvp2-gp2-pass-activation-brief.md:143:→ **detection-layer PASS = (b)(c)(d) ✅ + (a) partial. full GP-2 PASS = (a) prevention (R-1/R-2) 선행**.
docs/phase0/mvp2-gp2-pass-activation-brief.md:147:`tests/fixtures/secret_hygiene/redaction_fail/base64_evasion.txt` 존재 — secret-hygiene D-2 가 base64 evasion 미검출 (known limitation 명문, workflow line 13). R-5 = MVP-2/3 분리 (G3-4), GP-2 PASS scope 외. GP-2 PASS = Tier-1 42 catalog 평문 redaction 한정 (base64 evasion 제외 명문).
docs/phase0/mvp2-gp2-pass-activation-brief.md:155:**정당화**: PASS *발효* milestone (59 Layer PASS + 32 MVP-1 PASS 답습) + 큰 결정 (ADR-011 §2.4 T3) + 헌법 5조-2 cross-vendor + MVP-2 PASS 직전 단계.
docs/phase0/mvp2-gp2-pass-activation-brief.md:161:| 1 | 큰 결정 (PASS 발효 milestone) | ✅ | GP-2 PASS 발효 = MVP-2 PASS 절반 |
docs/phase0/mvp2-gp2-pass-activation-brief.md:164:| 4 | 권위 chain 다중 source 손상 | ⚠️ 부분 | R-S1 (MVP-2 PASS 전 hard gate, 본 cycle 비차단) |
docs/phase0/mvp2-gp2-pass-activation-brief.md:173:## §6 GP-2 PASS 발효 권고 + 조건
docs/phase0/mvp2-gp2-pass-activation-brief.md:175:⭐ **권고 = GP-2 detection-layer PASS 발효 APPROVE WITH CONDITIONS** (B-1: "full GP-2 PASS" 아닌 detection-layer 강등):
docs/phase0/mvp2-gp2-pass-activation-brief.md:177:1. **detection-layer (b)(c)(d) ✅ operative + (a) 설계 동등성 partial** — secret-hygiene D-2 PoC + ADR 권위 + R-3 CI 회귀 green + R-4 패턴 동등성 (설계 한정). (e2) = 본 cycle.
docs/phase0/mvp2-gp2-pass-activation-brief.md:179:   - (C-1) **R-1 (Hermes runtime redaction 검증) / R-2 (facade real) = prevention 잔여 trajectory 명문 — full GP-2 PASS 선행** (detection-layer PASS = in-repo 능동 redaction 0, Hermes upstream 위임 ADR-011 §2.3 #2, B-1/B-2)
docs/phase0/mvp2-gp2-pass-activation-brief.md:182:3. **R-S1 = GP-2 detection-layer PASS 비차단** (MVP-2 PASS 전 hard gate, 별도 cycle).
docs/phase0/mvp2-gp2-pass-activation-brief.md:184:→ **GP-2 detection-layer PASS 발효 자격 = (b)(c)(d) detection 충족 + (a) 설계 동등성 + (e2) 합의 APPROVE + 사용자 명시 + (C-1) prevention 잔여 trajectory 명문**. **full GP-2 PASS = + R-1/R-2 prevention 검증 (별도 trajectory)**.
docs/phase0/mvp2-gp2-pass-activation-brief.md:190:§0.2 답습 (12). 추가: MVP-2 PASS 자동 선언 0 / R-1 Hermes import 결정 0 / R-2 facade real 0 / R-5 evasion 진입 0 / R-S1 자동 정정 0 / 자동 후속 0.
docs/phase0/mvp2-gp2-pass-activation-brief.md:196:1. 본 brief 승인 → 풀 3+1 + 외부 LLM 1+ (codex (E-α)) → Reviewer 통합 → v1.1 흡수 → commit + push → **GP-2 detection-layer PASS 발효**
docs/phase0/mvp2-gp2-pass-activation-brief.md:197:2. **MVP-2 Implementation Evidence PASS 발효 합의** (Layer 통합 PASS ✅ + GP-2 **detection-layer** PASS ✅ + R-S1 hard gate 후, 32 답습) — ⚠️ **full GP-2 PASS (prevention R-1/R-2) = MVP-2 PASS 잔여 trajectory** (MVP-2 PASS 도 prevention deferred scope 명문 또는 prevention 선행 — MVP-2 PASS cycle 에서 결정)
docs/phase0/mvp2-gp2-pass-activation-brief.md:198:3. R-S1 cross-reference 정정 cycle (MVP-2 PASS 전 hard gate 3 옵션)
docs/phase0/mvp2-gp2-pass-activation-brief.md:199:4. **full GP-2 PASS trajectory** — R-1 Hermes runtime redaction 검증 (import) / R-2 facade real (TR-1) prevention (별도 cycle)
docs/phase0/mvp2-gp2-pass-activation-brief.md:205:- ADR-011 §2.1 (a)~(d) 모법 + §2.3 #2 (송신 방어 신뢰) — `docs/decisions/ADR-011-means-vs-ends-redaction.md`
docs/phase0/mvp2-gp2-pass-activation-brief.md:207:- governance-preconditions.md §4 (GP-2)
docs/phase0/mvp2-gp2-pass-activation-brief.md:208:- redaction-pattern-equivalence.md (R-4) + r4-1-trigger-extension-evidence.md (R-4.1) + g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md (Group D PoC)
docs/phase0/mvp2-gp2-pass-activation-brief.md:210:- 실 evidence: `secret-hygiene-egress-redaction.yml` (D-2) + `tools/secret_scanner.py` (--mode scan-log) + `tests/fixtures/secret_hygiene/{redaction_pass,redaction_fail}/`
docs/phase0/mvp2-gp2-pass-activation-brief.md:218:| P-1 | GP-2 PASS *기정사실화* | 발효 = 합의 APPROVE + 사용자 명시 후 (§0.2 #1 + §8) |
docs/phase0/mvp2-gp2-pass-activation-brief.md:219:| P-2 | R-3 detection 만으로 GP-2 PASS *단순화* (prevention R-1/R-2 부재 은폐) | §3 detection/prevention 분리 명시 + (C-1) deferred 명문 (59 Layer 2a DEFER 답습, β B-1 cascade 교훈) |
docs/phase0/mvp2-gp2-pass-activation-brief.md:221:| P-4 | DESIGN repo GP-2 PASS vs runtime redaction 혼동 | §1.2 + §3.2 = 본 repo = 설계/CI, 실 runtime redaction = Hermes upstream (R-1) 명시 |
docs/phase0/mvp2-gp2-pass-activation-brief.md:230:## §11 v1.1 흡수 매트릭스 (BLOCKING 2 + 권고 4 1pass — detection-layer reframe)
docs/phase0/mvp2-gp2-pass-activation-brief.md:236:| B-1 ⭐ (3-way) | "GP-2 (full) PASS" + "(a) ✅" over-claim → **GP-2 detection-layer PASS** 강등 + §2 3축 분리 ((a) 설계 동등성 ⚠️ / (b)(d) detection ✅ / prevention upstream 위임 입증 0) + full GP-2 PASS = R-1/R-2 선행 | codex + Agent C + Agent B | title + §2 + §4 + §6 + 발효 효과 |
docs/phase0/mvp2-gp2-pass-activation-brief.md:237:| B-2 | "59 동형" → "부분 동형 (cover 비대칭, in-repo 능동 redaction 보증 0)" | Agent B R-B-1 | §3.2 |
docs/phase0/mvp2-gp2-pass-activation-brief.md:241:| N-4 | C-1 prevention deferred + workflow_dispatch 한계 유지 | Agent A + codex | §6 |
docs/phase0/mvp2-gp2-pass-activation-brief.md:249:**다음 단계**: SESSION + INDEX commit + push → 본 cycle 합의 발효 (REVISE → v1.1 흡수) → **GP-2 detection-layer PASS 발효**. 후속: MVP-2 Implementation Evidence PASS 발효 합의 (Layer 통합 PASS + GP-2 detection-layer PASS + R-S1, full GP-2 PASS prevention = 잔여 trajectory) = 사용자 명시 별도 cycle.
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:1:# SC-1 facade RedactionFilter (R-2 GP-2 prevention) 실 구현 brief (v1.1)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:5:> **v1 → v1.1 갱신**: 풀 3+1 + 외부 LLM 1+ (codex gpt-5.5 cross-vendor) 통합 합의 (`docs/review/3plus1-consensus-2026-05-28-mvp2-sc1.md`) **APPROVE WITH CONDITIONS (4 source 전원) → BLOCKING 4 + 권고 6 1pass 흡수**. 핵심 정정: **B-1 catalog 재사용 (i) src→tools import → (ii) 공유 모듈 추출** (Reviewer verify: (i) namespace package 동작하나 의존 방향 부적절, 3:1 majority) / **B-2 `[REDACTED]` whole-match → group-aware 치환** (값만 마스킹, key/구조 보존 — secret_scanner = 검출 전용 치환 함수 0) / **B-3 송신 redaction 권위 = governance §4.1 + 64 trajectory** (§8.2 = egress 보조) / **B-4 범위 = messages + metadata** (full fields deferred). §12 흡수 매트릭스 추가.
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:7:> **scope** (사용자 명시 "RedactionFilter 집중"): **RedactionFilter 완전 구현 (secret_scanner Tier-1 45 catalog 공유 모듈 추출 재사용, R-2-c (ii)) + facade `complete()` 송신 전 redaction 적용 layer 통합**. **LiteLLM Router 위임 = deferred (Provider Liquidity 별도 sub-cycle)**. TDD 적용.
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:9:> ⚠️ **명칭 정직성 (over-claim 차단, 본 세션 #2 4회 cascade 교훈 답습)**: 본 cycle = **facade redaction layer real (R-2 GP-2 prevention)** — **full facade real 아님** (LiteLLM Router 위임 + Min 2 검증 + registry yaml = deferred). "facade real 완성" 표현 금지.
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:11:> **본 cycle = 큰 cycle (실 코드 + TR-1)** — facade.py 헤더 명시 "real 본문 작성 시 자동 풀 3+1 합의 trigger TR-1 발화". 64 entry SC-1 = 풀 3+1 (TR-1) + 실 코드.
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:13:> **본 cycle 발효 효과** = R-2 facade RedactionFilter prevention layer **in-repo operative** + GP-2 (a) "facade redaction filter 검증" 충족 (full GP-2 PASS Exit (a)의 R-2 prong). **full GP-2 PASS 발효 = SC-2 (R-1 위임 검증) + SC-3 후 (별도)**.
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:15:> **선행 답습**: 64 trajectory entry brief (SC-1 정의 + R-2-a 동시 + R-2-c catalog 재사용 + RedactionFilter = facade 내부 협력자 + RT-1 atomic) + llm-providers-design §4.1/§8.2 (설계 명세) + ADR-009 §2.2 (facade 단일 진입점 의무) + secret_scanner Tier-1 45 catalog
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:24:2. **송신 redaction 역할 명세** (GP-2 prevention = request body secret strip, §3)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:25:3. **facade 통합 지점 + Router deferred 처리** (RT-1 window 회피, §4)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:34:| 1 | **LiteLLM 설치 + Router 위임 구현** (Provider Liquidity 별도 sub-cycle, deferred) | 0 |
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:35:| 2 | **full facade real** (Min 2 검증 + registry yaml + 에러분류 + 정규화 + OAuth lock + callback) | 0 |
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:36:| 3 | **full GP-2 PASS 발효** (SC-2 R-1 위임 검증 + SC-3 후) | 0 |
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:40:| 7 | detection-layer PASS (60) / MVP-2 PASS (62) 재선언 | 0 |
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:42:| 9 | llm-providers.yaml registry 작성 (Min 2 검증 의존, Router deferred와 함께) | 0 |
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:47:- ⭐ **송신 redaction 권위 (B-3 정정)**: **governance-preconditions.md §4.1** (line 422 — "LLM API request body 에 secret 노출 차단" 송신 경로) + **64 trajectory brief §3** = 송신 redaction PRIMARY 권위. **§8.2 RedactionFilter (docstring "응답·예외·메트릭") = egress(응답/로그) scrub 보조** (송신 redaction은 §8.2 직접 문구 아님, governance 정합 확장).
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:48:- **llm-providers-design.md §8.2** (RedactionFilter 설계 — PATTERNS 4 + KEY_BLACKLIST 6, 블랙리스트 채택, egress scrub) + **§4.1** (facade `complete()` 흐름) + **§4.4** (호출 흐름 — redaction 적용 지점 step 5)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:49:- **governance-preconditions.md §4.5 (a)** (facade redaction filter 검증)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:50:- **ADR-009 §2.2** (facade 단일 진입점 의무 — LiteLLM 직접 import = facade.py 한정, provider SDK 직접 import 금지)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:52:- **.importlinter** (root=src, forbidden=LLM SDK facade 예외 — src↔tools 경계 결정 입력)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:53:- **64 trajectory entry brief §4.4** (R-2-a/c 권고 + RedactionFilter = facade 내부 협력자 + RT-1 atomic)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:54:- **redaction-pattern-equivalence.md** (R-4 — Tier-1 catalog 설계 동등성, Hermes 안전성 선언 금지 §7.3)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:61:- GP-2 현 상태: detection-layer PASS (60, R-3 secret-hygiene D-2 CI operative). prevention (R-1/R-2) deferred.
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:62:- 본 cycle = **R-2 prevention prong** (facade redaction filter) in-repo 구현 → GP-2 Exit (a)의 R-2 검증 충족 (R-1 = SC-2 별도).
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:70:secret_scanner Tier-1 45 catalog 재사용 (R-2-c, single source detection↔prevention) — import 경계 4 옵션:
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:75:| (ii) ⭐ catalog 공유 모듈 추출 | Tier-1 catalog를 `src/adapters/llm/redaction_patterns.py` (또는 공유 위치) 추출, secret_scanner + RedactionFilter 공유 | single source + 런타임 정합 | **secret_scanner 변경 = R-4.1 "변경 0건" 위반 = R-7(b) 차등 자격** (별도 평가) |
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:76:| (iii) RedactionFilter 자체 복제 | Tier-1 45 패턴 복사 | 경계 깔끔 | **중복 → detection↔prevention drift 위험** (single source 위반) |
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:81:**(ii) 구체화**: Tier-1 catalog literal을 **src 하위 공유 모듈** (`src/adapters/llm/redaction_patterns.py`)로 추출 → `RedactionFilter`(src) + `secret_scanner`(tools) 둘 다 import (**tools→src = 도구가 런타임 참조 = 정방향**). **secret_scanner 패턴 *내용* 변경 0건** (id/src/cat/vendor/regex 동일, R-4.1 충실) + **equivalence test 필수** (`len(ALL_PATTERNS)==45` + pattern snapshot 동일 + scan-source/scan-log pass/fail fixture 유지). secret_scanner 구조 변경 (literal 정의 → import)은 패턴 내용 0이므로 **detection 동작 불변** (R-7(b) = 패턴 *내용* 변경 아님).
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:87:    """LLM 송신/응답/로그에서 비밀값 자동 strip (GP-2 prevention)."""
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:89:    def redact_messages(self, messages: list[dict]) -> list[dict]: ...  # 송신 request body redaction (GP-2 핵심)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:93:- 패턴 source = `src/adapters/llm/redaction_patterns.py` 공유 모듈 (Tier-1 45 catalog, §2.1 (ii)).
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:94:- ⭐ **B-2 흡수 — group-aware 치환 (값만 마스킹, 구조 보존)**: secret_scanner 패턴 = *검출*용 (prefix `key=` 포함 매칭 / regex group / alternation). **whole-match `[REDACTED]` 치환 시 key명·JSON 구조 소거 + word-joining artifact** (3 Agent 실증). → redaction = **매칭된 secret *값* 부분만** 마스킹 (key명/구조 보존). detection 패턴 ≠ redaction 치환 — 값 추출/group 분리 로직 별도 (R-6: `sk-***last4` 부분 마스킹 평가, 또는 `[REDACTED]` 값 한정).
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:95:- ⭐ **R-3 흡수 — `scrub()` KEY_BLACKLIST**: §8.2 `KEY_BLACKLIST` (api_key/token/secret/auth/credential/authorization) dict key 기반 redaction 구현 (Tier-1 regex만으론 key 기반 누락).
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:100:## §3 송신 redaction 역할 명세 (GP-2 prevention)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:102:⭐ **핵심 = 송신 경로 (request body) redaction** (권위 = governance §4.1 line 422 verbatim "LLM API request body 에 secret 노출 차단" + 64 trajectory §3, B-3 정정):
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:104:- ⭐ **B-4 흡수 — 범위 명시**: 본 cycle 최소 = **`req.messages` + `req.metadata`** redaction (현 placeholder `LLMRequest(alias, messages, metadata)` 기준 — `system` 필드 없음). 설계 §4.1 full fields (`system`/`tools`/`tool_choice`/`response_format`/`stop_sequences`/`metadata_in`)는 **Router 위임 sub-cycle과 함께 deferred** (시그니처 전면 개편 deferred 명시).
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:106:- §4.4 호출 흐름 step 5 "메트릭 기록 (redaction 적용)" = 응답/로그 redaction (`scrub`).
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:107:- **GP-2 prevention 핵심 = 송신 (request body)**. 응답/로그 redaction = 보조 (§8.2 scrub).
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:109:⚠️ **redaction 의미 명확화**: GP-2 = "secret이 *실수로* LLM request body에 포함되는 것 차단" (예: 메시지에 API key 평문 노출). 정상 대화 내용 손상 아님 — Tier-1 catalog는 secret 패턴 (sk-/Bearer/api_key 등) 한정 매칭.
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:113:## §4 facade 통합 지점 + Router deferred (RT-1 window 회피)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:115:### §4.1 통합 설계 (현 placeholder → redaction layer real)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:117:현 `facade.py` (41 LOC placeholder):
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:119:- `complete(req)` → **redaction 적용 후 Router deferred**:
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:120:  1. `redacted = self._redactor.redact_messages(req.messages)` (송신 전 redaction — GP-2 prevention operative)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:121:  2. Router 위임 = **deferred** → `raise NotImplementedError("LiteLLM Router 위임 = Provider Liquidity sub-cycle deferred")` (redaction *후* 명시적 deferred)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:125:- 64 brief RT-1 = "facade real 후 RedactionFilter 미부착 window 금지 (atomic)".
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:126:- 본 cycle: **Router deferred = 실제 LLM 송신 0 = redaction 미부착 window 없음** (송신 자체가 deferred). RedactionFilter는 complete() 진입 시 부착 → Router 발효 (SC-Provider Liquidity) 시점에 이미 redaction layer 존재 (선부착).
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:127:- ⭐ **선부착 보장**: SC-Provider Liquidity (Router 위임)가 본 SC-1 (redaction layer) *후* 진입 → Router 발효 시 redaction 이미 operative (window 0).
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:132:- 본 cycle = **redaction 통합 최소 변경** — 시그니처 전면 개편 (설계 §4.1 full)은 Router 위임 sub-cycle과 함께 (deferred). 현 placeholder 시그니처 기반 redaction layer 추가 (over-engineering 회피).
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:140:`tests/adapters/llm/test_redaction_filter.py` (신규):
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:143:- T-3: Tier-1 45 catalog 대표 패턴 (baseline + prefix + regex + alternation 각 1+) redaction 검증
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:145:- T-5: `scrub(dict)` 재귀 (nested) + **KEY_BLACKLIST** (R-3) redaction + **dict 구조 무결성** (B-2 — key명/구조 보존 검증)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:146:- T-6 ⭐ (R-4): facade `complete()` — **spy/fake redactor 주입**으로 redaction *선행* 검증 (Router deferred NotImplementedError 전 redaction 호출 입증, 단순 NotImplementedError 확인만으론 순서 미입증)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:148:- T-8 (B-1): **equivalence test** — `src/adapters/llm/redaction_patterns.py` 추출 후 `len(ALL_PATTERNS)==45` + pattern snapshot 동일 + secret_scanner scan-source/scan-log 동작 불변
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:152:- `src/adapters/llm/redaction_patterns.py` (Tier-1 45 catalog 공유 모듈 추출, §2.1 (ii)) + `secret_scanner.py` import 전환 (패턴 내용 0 변경)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:153:- `src/adapters/llm/redaction.py` (RedactionFilter — redact_text/redact_messages/scrub, group-aware 치환 + KEY_BLACKLIST)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:154:- `facade.py` complete() redaction 통합 (messages + metadata, Router deferred)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:163:- pytest (신규 redaction test + 기존 회귀 0)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:164:- import-linter (LLM SDK 경계 보존 — litellm import 0, Router deferred)
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:174:**정당화**: facade.py 헤더 명시 TR-1 (real 본문 작성 풀 3+1 trigger) + GP-2 prevention 보안 영역 (CLAUDE.md §3 보안 = 풀 3+1 필수) + 실 코드 + Provider Liquidity 직결.
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:180:| 1 | TR-1 (facade real 본문) | ✅ |
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:181:| 2 | 보안 관련 변경 (GP-2 prevention) | ✅ |
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:182:| 3 | 실 코드 (런타임 redaction) | ✅ |
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:183:| 4 | Provider Liquidity 영향 (facade 단일 진입점) | ✅ |
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:196:- LiteLLM 직접 import = facade.py 한정 (Router deferred이므로 본 cycle litellm import 0 — import-linter 보존).
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:197:- RedactionFilter = facade 내부 협력자 (provider-agnostic, 모델명 분기 0).
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:198:- facade 단일 진입점 의무 보존 ([[feedback_provider_liquidity]]).
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:204:§0.2 답습 (10). 추가: LiteLLM 설치 0 / Router 위임 구현 0 / secret_scanner 패턴 변경 0 / litellm import 0 / full facade real 표현 0 / full GP-2 PASS 발효 0 / 자동 SC-2/SC-3 진입 0.
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:212:| RT-1 | Router 발효가 redaction layer *전* 진입 (window) | SC-Provider Liquidity는 본 SC-1 후 진입 (선부착 §4.2) |
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:214:| RT-3 | redaction false positive (정상 내용 손상) | Tier-1 catalog = secret 패턴 한정 + T-4 test |
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:216:| RT-5 | redaction 성능 (매 송신 45 패턴 매칭) | COMPILED_PATTERNS 재사용 (사전 compile) |
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:222:- E-1: redaction test green (T-1~T-6) + 커버리지 70%+
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:223:- E-2: facade complete() redaction 적용 + Router deferred 순서 검증
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:234:| P-1 | "facade real 완성" over-claim | §0 명칭 정직성 — facade *redaction layer* real, Router deferred ([[feedback_pass_scope_overclaim]]) |
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:235:| P-2 | full GP-2 PASS 기정사실화 | full GP-2 PASS = SC-2 (R-1) + SC-3 후 (§0.2 #3) |
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:238:| P-5 | 송신 redaction 정상 내용 손상 | §3 — Tier-1 secret 패턴 한정 + T-4 false positive test |
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:239:| P-6 | RT-1 window | §4.2 선부착 보장 (Router deferred = 송신 0) |
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:252:| B-3 | 송신 redaction 권위 = **governance §4.1 + 64 trajectory** (§8.2 = egress 보조) | codex + Agent B | §0.3 + §3 |
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:253:| B-4 | redaction 범위 = **messages + metadata** (full fields system/tools/... deferred) | codex | §3 |
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:257:| R-4 | T-6 spy/fake redactor (redaction 선행 입증) | codex 4 | §5.1 T-6 |
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:261:**4 source 정합 (positive)**: 명칭 정직성 양호 (facade redaction layer real, full facade real / full GP-2 PASS 아님 — over-claim 0) / RT-1 window 회피 타당 (Router deferred) / Provider Liquidity 보존 (litellm import 0) / 권위 인용 일치 (codex 6/7, §8.2 부분 확장만). pytest 152 green (Agent A 실측) + redaction 성능 ~2.1ms/request.
docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:267:**다음 단계**: **TDD 구현 (RED→GREEN→REFACTOR, catalog (ii) 공유 모듈 + group-aware 치환)** → verify (pytest + import-linter + secret_scanner equivalence + jarvis 회귀) → commit + push → **R-2 facade RedactionFilter prevention layer in-repo operative**. 후속: SC-2 (R-1 위임 검증) / SC-3 (full GP-2 PASS 발효) / SC-Provider Liquidity (Router 위임) = 사용자 명시 별도 sub-cycle.
docs/architecture/governance-preconditions.md:5:> **PASS 범위 한정 (P0 조건 C-A, 5/5 입력 일치)**: 본 PASS 는 *Design/Governance Gate PASS* 한정 — 문서 구조 / 권위 위계 / 6 GP 정의 / 강제 메커니즘 분류 매트릭스 / Entry·Exit 기준 정의의 *설계 승인* 에 한정한다. **Implementation/Runtime PASS 는 본 PASS 에 포함되지 않는다** — GP-2~GP-6 의 PoC 실증 / CI 강제 / runtime hook 구현 / Evidence Ledger 검증은 *별도 합의* 로만 발생.
docs/architecture/governance-preconditions.md:9:> - **GP-2 ~ GP-6**: **DESIGN PASS / IMPLEMENTATION PENDING** (각 GP 의 PoC 실증 + (a)~(e) 5조건 충족 검증은 별도 합의)
docs/architecture/governance-preconditions.md:27:**상위 결정**: ADR-008 (Hermes 도입 Option B) 6 차단조건, ADR-011 (수단/목적 분리, §2.3 권위 위계, §2.4 T1/T2/T3), **ADR-009 C-N (P1 facade MVP 진입조건 + Hermes PMO ↔ provider 분리 + Provider Liquidity 5-way 모법 ADR Layer 1, 2026-05-09 후속 4 갱신)**, **ADR-012 (Evidence Ledger Protection, 2026-05-09 후속 3 PR-2 신규 발행)**
docs/architecture/governance-preconditions.md:28:**관련 설계**: **`hermes-adoption-design-v3.md` §4 (G2 정의 — P2 v3 Adopted Design Adoption only, 2026-05-09 후속 6)**, `hermes-adoption-design.md` (P2 v2, **Archived 2026-05-09 후속 7**), `system-identity-prequel.md` §3.3 / §4.2 (**Archived 2026-05-09 후속 8**, 본 ADR-011 §2.3 영구 권위 승격 답습으로 권위 보존), `redaction-pattern-equivalence.md` (R-4), `canary-recheck-design.md` (R-5), `llm-providers-design.md` (P1 v2 — Option β LiteLLM facade)
docs/architecture/governance-preconditions.md:42:5. 각 GP의 Entry / Exit 기준 (ADR-011 §2.1 (a)~(d) 4조건 패턴 답습 + (e) 합의 APPROVE)
docs/architecture/governance-preconditions.md:49:1. ❌ **G2 PASS 선언** — 본 초안은 *정의*까지만, GP-1~GP-6 각각의 (a)~(e) Exit 기준 충족 검증은 후속
docs/architecture/governance-preconditions.md:66:| 3 | 각 GP entry 진입 + PoC 작성 + Exit 기준 (a)~(e) 충족 검증 | 6 PoC 산출 + 각 GP별 evidence | GP별 순차 또는 병행 |
docs/architecture/governance-preconditions.md:105:| **P2** | **로그/LLM 송신 경로 평문 노출** | Hermes / Worker 가 secret 을 stdout / stderr / log file / LLM API request body 에 노출 | 8조 #2 | Hermes native redaction 보조 (ADR-011 §2.3 운영 함의 #2) |
docs/architecture/governance-preconditions.md:114:| **P6** | **Hermes 자체 SDK 직접 import** | Worker Agent / Skill / Hermes plugin 코드가 `import hermes_agent.*` 또는 `import litellm` 직접 import 로 P1 facade 우회 | Provider 교체 자유 (코드 변경 없이) | **차단조건 #4** (provider 어댑터 추상화) |
docs/architecture/governance-preconditions.md:143:#### 1.2.5 P9 ~ P12 deferred candidates (C-I 흡수 — 2026-05-09 후속 2)
docs/architecture/governance-preconditions.md:145:> **본 §1.2.5 는 합의 보고서 §11.2 P1 조건 C-I 흡수** (출처: GPT 조건 7 + Claude C-4). 본 §1.2.1 ~ §1.2.3 의 *현재 enumeration P1~P8* 외에 **누락 위반 경로 후보 4 ~ 6 건** 을 *deferred candidates* 로 명시 등록한다. **deferred candidate = 향후 합의에서 P9~P12 정식 등록 가능, 본 G2 PASS 시점 정식 enumeration 외**.
docs/architecture/governance-preconditions.md:149:| **P9 (후보)** | **Prompt Injection** — Hermes / Worker / LLM 출력 내 *지시 명령* 이 후속 LLM / Tool 에 의해 *명령* 으로 해석 (예: "ignore previous instructions ...") | 합의 결과 silent override / 자동 정책 변경 위장 / Skill escalation | deferred (GPT 조건 7) | 외부 입력 검증 GP-4 PoC 진입 시점에 P5 (외부 입력 검증) 와 *별 카테고리* 로 정식 등록 검토 |
docs/architecture/governance-preconditions.md:151:| ~~**P11 (후보)**~~ → **P11 (정식 등록 완료, §1.2.7 답습, 2026-05-12)** | **Supply-chain Compromise** — Hermes / pysqlcipher3 / litellm / Hermes-agent 의존성 또는 GitHub Actions runner / Docker base image 침해 | 자동 redaction 무력화 / SQLCipher trigger silent 깨짐 / canary catalog silent 변경 / R-6 actual run 위장 / Gate Enforcement Layer Layer 1~4 (lint/test/hook/CI) 무력화 | ✅ **정식 등록 완료 (§1.2.7 답습)** | ✅ **2026-05-12** — Gate Enforcement Layer 보호 보강 (commits `3e46440` + `fa2cbdb`) 시점 트리거 답습 → 본 단축 합의 (Reviewer-only) 로 정식 등록. **Hermes PMO 격상 *전* precondition (권장)** — blocking 까지는 아님, Implementation/Runtime PASS 영역의 *우선 권장 항목* (Claude C-3 + C-6 답습) |
docs/architecture/governance-preconditions.md:152:| **P12 (후보)** | **Memory Poisoning Side-channel** — Memory / Skill 의 *우회 경로* (CLAUDE.md prompt-level lock-in / 외부 import skill / Memory 자동 흡수) 를 통한 Memory 오염 + 후속 결정 silent 영향 | 자동 학습 → 자동 정책 변경 위장 (T1 → T3 우회) / Skill 권한 escalation 우회 / Provider lock-in 우회 | deferred (Claude C-4 + GPT 조건 7) | G4 (provider-agnostic-memory-skill-design.md) Implementation/Runtime PASS 합의 시점에 정식 등록 — Memory boundary hook + Skill wrapper 실 구현 후 |
docs/architecture/governance-preconditions.md:158:| **P13 (후보)** | **Provider-specific URL Hardcoding** — `https://api.anthropic.com/...` / `https://api.openai.com/...` 등 provider 도메인 하드코딩 (P1 facade 우회) | GP-5 / G3 §6.4 / G4 §3.5 (provider_bindings) *동작 측면* 충분 — 별도 P 등록 *불필요* (Claude C-9 답습) |
docs/architecture/governance-preconditions.md:163:- 본 §1.2.5 는 *deferred candidates* 만 등록 — **본 G2 PASS 시점 P1~P8 enumeration 변경 0건**
docs/architecture/governance-preconditions.md:166:- 본 §1.2.5 등록 후보가 *현 시점* enforcement 의무화 대상 *아님* — deferred candidates 는 *위험 식별 + 후속 합의 진입 trigger*
docs/architecture/governance-preconditions.md:171:- ❌ 현 G2 PASS 무력화 (deferred 는 *후속* 영역)
docs/architecture/governance-preconditions.md:213:- 본 §1.2.6 = §1.2.5.2 deferred candidate 정식 등록 시점 명시 답습
docs/architecture/governance-preconditions.md:220:| P10 이 기존 P1~P12 구조와 충돌 | ❌ — §1.2.5 deferred 에 이미 등록, 정식 row 승격은 §1.2.5.2 명시 트리거 답습 |
docs/architecture/governance-preconditions.md:249:| **P11** | **Supply-chain Compromise** | (a) Hermes / pysqlcipher3 / litellm / Hermes-agent / agents-sdk 의존성 (PyPI / 외부 소스) 침해 — 악성 코드 주입 / typosquatting / dependency confusion (b) GitHub Actions runner image / 3rd-party action 침해 — workflow step 위장 / artifact 변조 (c) Docker base image 침해 — 자동 redaction 무력화 / canary catalog silent 변경 / SQLCipher trigger silent 깨짐 (d) Vendor 변경 silent — `hermes-version.yaml` / `requirements.txt` / `pyproject.toml` / lock 파일의 silent drift (e) Tooling supply chain — `import-linter` / `grimp` / `rfc8785` / `jcs` / `gitleaks` 등 *enforcement tool 자체* 침해 → Gate Enforcement Layer Layer 1~4 무력화 | (i) **Dependency Pinning Integrity** — `hermes-version.yaml` v0.12.0 명시 + `requirements.txt` / `pyproject.toml` / `poetry.lock` 정확 핀 + lock 파일 git diff 회귀 검출 (G3 §3.2.2 #3 답습) / (ii) **Checksum / Hash Verification** — pip install `--require-hashes` + SBOM 정합성 + 패키지 sha256 매니페스트 검증 / (iii) **GitHub Actions Action SHA Pinning** — `uses: actions/checkout@<commit_sha>` (not `@v4` tag) + 3rd-party action 사용 시 commit SHA pin 강제 / (iv) **Docker Base Image / Runner Image Immutability** — `FROM python:3.11@sha256:<digest>` digest 고정 + reproducible build + cosign 또는 동등 image signing verification (별도 합의 영역) / (v) **Vendor Change Auto-recheck** — 의존성 lock diff 검출 시 R-6 actual run 자동 R-2 / R-4.1 PoC 재실행 + canary 자동 검증 PASS 후만 merge (G3 §3.2.3 #2 답습) | **G3 §3.2** (Upstream Silent Breakage 5 측면 + ROLLBACK trigger R6) + **G3 §2.5 #14** (`hermes-version.yaml` + dependency lock T2 사용자 명시 PR merge) + **G3 §2.6** (Gate Enforcement Layer 보호 — Layer 1~4 enforcement mechanism 무력화 위험 cross-reference) + **GP-2 / GP-3 / GP-5** (redaction / credential / provider lock-in supply-chain 침해 시 무력화 위험 cross-reference) + **ADR-008 차단조건 #3** (Hermes 의존성 업그레이드 자동 R-2 재실행) + **외부 LLM Gap-N 중 N-5** (supply chain / dependency integrity 답습) + 본 §1.2.7 단축 합의 (Reviewer-only) |
docs/architecture/governance-preconditions.md:253:본 P11 enforcement 는 **G3 §3.2 직접 권위** + **G3 §2.5 #14** + **GP-2/GP-3/GP-5 cross-reference** 답습. *별도 GP 신설 부재* (사용자 명시 답습 — 본 §1.2.7 = P11 row 추가 한정, GP 신설은 별도 합의 영역):
docs/architecture/governance-preconditions.md:296:| P11 이 기존 P1~P12 구조와 충돌 | ❌ — §1.2.5 deferred 에 이미 등록, 정식 row 승격은 §1.2.5 명시 트리거 답습 |
docs/architecture/governance-preconditions.md:342:| **GP-2** | Egress Redaction (로그/LLM 송신) | P2 | Hermes native redaction (보조 — ADR-011 §2.3 #2) + LLM facade redaction filter (P1) | ADR-008 차단조건 #1 보조 + ADR-011 §2.3 |
docs/architecture/governance-preconditions.md:345:| **GP-5** | Provider Adapter 강제 (코드 레벨 lock-in 차단) | P6, P7 | depcruise 룰 정적 차단 + P1 facade 단일 진입점 + 분기 코드 PR 자동 reject | ADR-008 차단조건 #4 + P1 v2 |
docs/architecture/governance-preconditions.md:355:| GP-2 | ✅ test_redaction.py + base64 evasion test (R2-6) | ⚠️ 보조 | ✅ ROLLBACK trigger R5 (Hermes 학습 평문 검출) |
docs/architecture/governance-preconditions.md:363:- 추론적 보조: 4/6 (GP-1, GP-2, GP-4, GP-6)
docs/architecture/governance-preconditions.md:388:| 자동 롤백 | R-7 SOP §5 ROLLBACK trigger R1~R3 | `docs/phase0/redaction-verification-sop.md` |
docs/architecture/governance-preconditions.md:395:### 3.5 Exit 기준
docs/architecture/governance-preconditions.md:397:> 본 GP-1 은 **G1b PASS 의 직접 흡수** — Exit (a)~(e) 5조건이 G1b 승격 시점에 모두 충족된 상태. 본 §3.5 는 그 *증거 cross-reference* 만 명시.
docs/architecture/governance-preconditions.md:401:| (a) | 동등 이상의 보안 결과 | R-4 redaction-pattern-equivalence.md (3-way 비교 + Tier-1 42 gap 식별) |
docs/architecture/governance-preconditions.md:418:## 4. GP-2 — Egress Redaction (로그/LLM 송신)
docs/architecture/governance-preconditions.md:422:Hermes / Worker Agent 가 stdout / stderr / log file / LLM API request body 에 secret 을 노출하지 않도록 native redaction (`agent/redact.py`) + LLM facade redaction filter (P1 v2 §8.2) 가 사전 차단한다.
docs/architecture/governance-preconditions.md:424:**중요**: GP-2 는 ADR-011 §2.3 운영 함의 #2 의 *보조* 역할. **DB INSERT 차단은 GP-1 의 책임이며, GP-2 는 송신/로그 경로만 다룸**. GP-2 단독으로 헌법 8조 본질 충족 시도 금지.
docs/architecture/governance-preconditions.md:434:| 계산적 | Hermes native redaction `agent/redact.py` (Tier-1 catalog 적용) | Hermes container |
docs/architecture/governance-preconditions.md:435:| 계산적 | P1 v2 LLM facade RedactionFilter | P1 facade layer |
docs/architecture/governance-preconditions.md:436:| 계산적 | base64 evasion test (R2-6) | `tests/hermes/redaction/test_base64_evasion.py` |
docs/architecture/governance-preconditions.md:444:- ✅ Hermes native redaction `agent/redact.py` 존재 확인 (R-1 Day 2 evidence)
docs/architecture/governance-preconditions.md:445:- ⏳ 사용자 명시 GP-2 작업 진입 결정
docs/architecture/governance-preconditions.md:447:### 4.5 Exit 기준
docs/architecture/governance-preconditions.md:451:| (a) | 동등 이상의 보안 결과 | Hermes native redaction Tier-1 42 catalog 적용 검증 + P1 facade redaction filter 검증 |
docs/architecture/governance-preconditions.md:455:| (e) | 합의 APPROVE | 단축 또는 풀 3+1 합의 (G2 GP-2 한정 또는 G2 통합) |
docs/architecture/governance-preconditions.md:459:- `tests/hermes/redaction/test_log_canary.py` (log file inject + grep)
docs/architecture/governance-preconditions.md:465:- ADR-011 §2.3: 본문 변경 없음, §8.5 후속 작업에 GP-2 산출 등록 (G2 PASS 시점)
docs/architecture/governance-preconditions.md:502:### 5.5 Exit 기준
docs/architecture/governance-preconditions.md:556:### 6.5 Exit 기준
docs/architecture/governance-preconditions.md:584:Worker Agent / Skill / Hermes plugin 코드가 Hermes 자체 SDK / litellm / anthropic / openai 직접 import 또는 모델명 / Provider 분기 코드를 포함하지 않도록 depcruise 룰 + P1 facade 단일 진입점 + PR auto-reject 가 정적으로 강제한다.
docs/architecture/governance-preconditions.md:597:| 계산적 | P1 facade 단일 진입점 강제 (`src/llm/facade.py` 외 LLM 호출 금지) | P1 v2 |
docs/architecture/governance-preconditions.md:604:- ⏳ P1 v2 facade MVP 완료 (P1 v2 §X — 본 G2 범위 외, 의존)
docs/architecture/governance-preconditions.md:607:### 7.5 Exit 기준
docs/architecture/governance-preconditions.md:620:- P1 v2 facade MVP (본 GP-5 의존 — P1 작업과 통합)
docs/architecture/governance-preconditions.md:628:- P1 v2 (`llm-providers-design.md`): facade 단일 진입점 권위 cross-reference
docs/architecture/governance-preconditions.md:661:### 8.5 Exit 기준
docs/architecture/governance-preconditions.md:752:## 10. G2 통합 Entry / Exit 기준 종합
docs/architecture/governance-preconditions.md:760:### 10.2 G2 통합 Exit (모든 GP 충족 + 메타 안전장치 인터페이스)
docs/architecture/governance-preconditions.md:762:| GP | Exit (a)~(e) | 현 상태 |
docs/architecture/governance-preconditions.md:765:| GP-2 | (a)~(e) 미충족 — PoC + 합의 필요 | ⏳ |
docs/architecture/governance-preconditions.md:768:| GP-5 | (a)~(e) 미충족 — P1 v2 facade MVP 의존 + PoC + 합의 필요 | ⏳ |
docs/architecture/governance-preconditions.md:784:### 10.3 G2 통합 Exit *선언* 절차 (사용자 명시 답습)
docs/architecture/governance-preconditions.md:809:| **수단/목적 분리 원칙** | ADR-011 §2.1 (a)~(d) 4조건 → 본 §3~§8 Exit 기준 (a)~(e) 패턴 답습 |
docs/architecture/governance-preconditions.md:825:| **DRAFT 상태 해제 → 정식 채택** | **단축 합의 또는 풀 3+1 합의 APPROVE** + 각 GP (a)~(e) Exit 기준 충족 검증 |
docs/architecture/governance-preconditions.md:835:2. **R-7 SOP §0 핵심 선언 답습**: 각 GP Exit 기준 (a)~(e) 5조건은 ADR-011 §2.1 (a)~(d) 4조건 + 합의 APPROVE (e) 패턴 답습 — 본 초안이 새 권위 구조 트리거하지 않음.

exec
/bin/bash -lc "nl -ba docs/phase0/mvp2-gp2-pass-activation-brief.md | sed -n '1,220p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# GP-2 detection-layer PASS 발효 합의 entry brief (v1.1)
     2	
     3	> **작성**: 2026-05-28 (60번째 entry 진입 cycle — 신규 세션 #2)
     4	>
     5	> **v1 → v1.1 갱신**: 풀 3+1 + 외부 LLM 1+ (codex gpt-5.5 cross-vendor) 통합 합의 (`docs/review/3plus1-consensus-2026-05-28-mvp2-gp2-pass-activation.md`) **REVISE (3-way framing over-claim) → BLOCKING 2 + 권고 4 1pass 흡수**. ⭐ **핵심 정정 (B-1)**: "GP-2 (full) 송신 redaction PASS" + "(a) ✅" = over-claim → **"GP-2 detection-layer PASS"** 강등. (a) 동등 이상 보안 결과 = governance §4 상 R-1/R-2 prevention 검증인데 deferred (redaction-pattern-equivalence = 설계 동등성 문서, Hermes safety 선언 아님). evidence 자체는 실증 (over-claim 0, β B-1 / 59 B-2 framing 동형). §11 흡수 매트릭스 추가.
     6	>
     7	> **scope**: G2 GP-2 **detection-layer** PASS **발효 (e2)** — R-3/D-2 자동 회귀 검증 operative. **full GP-2 PASS (prevention R-1/R-2) = 잔여 trajectory (deferred)**
     8	>
     9	> **본 cycle = 큰 cycle** (PASS *발효* milestone, 풀 3+1 + 외부 LLM 1+ 의무, 59 Layer 통합 PASS 발효 + 32 MVP-1 PASS 발효 답습 동형)
    10	>
    11	> **본 cycle 발효 자격** = (b)(d) detection evidence + (a) 설계 동등성 + (e2) 풀 3+1 + 외부 LLM 1+ 합의 APPROVE + 사용자 명시
    12	>
    13	> **본 cycle 발효 효과** = **GP-2 detection-layer PASS 발효** (R-3/D-2 회귀 검증 + R-4 설계 동등성 + ADR 권위). prevention (R-1 Hermes runtime / R-2 facade real) = in-repo 입증 0, Hermes upstream 위임 (ADR-011 §2.3 #2). MVP-2 Implementation Evidence PASS = Layer 통합 PASS (59 ✅) + GP-2 detection-layer PASS (본 cycle) + R-S1 hard gate → **full GP-2 PASS (prevention) = MVP-2 PASS 잔여 trajectory (별도 cycle)**
    14	>
    15	> **선행 답습**: 51 audit (GP-2 Exit 5조건, R-1~R-5 후보) + 57 ((β) R-4 = R-3 detection 우선 + R-1/R-2 prevention deferred) + 59 (Layer 통합 PASS 발효, means-vs-ends + DEFER 패턴 답습)
    16	
    17	---
    18	
    19	## §0 본 brief 의 범위
    20	
    21	### §0.1 본 brief 가 *하는* 것
    22	
    23	1. **GP-2 Exit 5조건 evidence 매트릭스** ((a)~(d) + (e2)) — 51 audit §2.2 현행화 (§2)
    24	2. **R-3 detection (operative) + R-1/R-2 prevention (deferred trajectory) 분리** (57 (β) + 59 Layer 2a DEFER 패턴 답습) (§3)
    25	3. **ADR-011 §2.1 (a)~(d) 모법 + (e2) ADR-012 §4 확장 매핑** (59 B-2 정정 framing 답습) (§4)
    26	4. **R-5 base64 evasion = known limitation 명문** (R-5 영구 분리) (§4)
    27	5. **합의 형태 = 풀 3+1 + 외부 LLM 1+ + 승격 트리거** (§5)
    28	6. **GP-2 PASS 발효 권고 + 조건** (§6)
    29	7. 금지 / 다음 단계 / cross-ref / 자기진단 (§7~§10)
    30	
    31	### §0.2 본 brief 가 *하지 않는* 것
    32	
    33	| # | 영역 | 위반 |
    34	|---|------|----|
    35	| 1 | GP-2 PASS *발효* 자체 (본 brief = 합의 입력, 발효 = 합의 APPROVE + 사용자 명시 후) | 0 |
    36	| 2 | **MVP-2 Implementation Evidence PASS 발효** (Layer 통합 PASS + GP-2 PASS + R-S1 후 별도) | 0 |
    37	| 3 | **R-1 Hermes import 결정** (prevention 구현 경로, 별도 cycle) | 0 |
    38	| 4 | **R-2 facade real (TR-1)** (prevention 구현 경로, 별도 trajectory) | 0 |
    39	| 5 | R-5 base64/URL-encoded/압축 evasion 영역 진입 (MVP-2/3 분리, G3-4) | 0 |
    40	| 6 | 신규 외부 library 도입 / secret_scanner Tier-2/3 catalog 확장 | 0 |
    41	| 7 | R-S1 cross-reference 정정 (MVP-2 PASS 전 hard gate, 별도 cycle) | 0 |
    42	| 8 | Layer 통합 PASS 재선언 (59 답습 유지) / MVP-1 PASS 재선언 (32 답습) | 0 |
    43	| 9 | ADR / 헌법 / roadmap / governance / ADR-008/011/012 본문 갱신 | 0 |
    44	| 10 | secret_scanner.py / secret-hygiene-egress-redaction.yml 본문 변경 | 0 (PoC 시제 보존) |
    45	| 11 | 자동 후속 cycle 진입 (MVP-2 PASS / R-S1) | 0 (사용자 명시 의무) |
    46	| 12 | 본 brief 자체 영구화 / 권위 chain 등재 | 0 |
    47	
    48	### §0.3 권위 답습 source
    49	
    50	- **ADR-011 §2.1 (a)~(d) 4조건 모법** (line 52~61) — `docs/decisions/ADR-011-means-vs-ends-redaction.md`
    51	- **ADR-011 §2.3 운영 함의 #2** (Hermes redaction = 로그/LLM 송신 방어 신뢰, 저장 경로 책임 0) — 동상 line 112
    52	- **ADR-012 §4 (a)~(d) + (e) 5조건 답습 확장** (PASS 발효 (e2) 권위) — `docs/decisions/ADR-012-evidence-ledger-protection.md`
    53	- **governance-preconditions.md §4** (GP-2 Egress Redaction Entry/Exit) — `docs/architecture/governance-preconditions.md`
    54	- **`docs/architecture/redaction-pattern-equivalence.md`** (R-4, (a) 설계 동등성) + **`docs/phase0/r4-1-trigger-extension-evidence.md`** (R-4.1, (b) PoC — N-2 경로 정정: phase0, architecture 아님)
    55	- **51 audit §2** (GP-2 Exit 5조건) — `docs/phase0/mvp2-entry-eligibility-audit-brief.md`
    56	- **57 (β) brief v1.1** (R-4 = R-3 detection + R-1/R-2 prevention deferred) — `docs/phase0/mvp2-beta-submeans-decision-brief.md`
    57	- **59 Layer 통합 PASS 발효 brief v1.1 + 합의** (means-vs-ends + DEFER + B-2 framing 답습) — `docs/phase0/mvp2-layer-124-pass-activation-brief.md`
    58	- **본 cycle audit (read-only, 2026-05-28)** — secret-hygiene CI + fixtures + secret_scanner filesystem direct
    59	
    60	---
    61	
    62	## §1 진입 컨텍스트
    63	
    64	### §1.1 선행 chain
    65	
    66	| 합의/구현 | 본 cycle 답습 |
    67	|----------|-----------|
    68	| 59 Layer 1+2+4 통합 PASS 발효 (`0f49eb9`, 4 source APPROVE WITH CONDITIONS) | MVP-2 = Layer 통합 PASS ✅ + **GP-2 PASS (본 cycle)** + R-S1. means-vs-ends + DEFER 패턴 + B-2 (a)~(d)/(e2) framing 답습 |
    69	| 57 (β) R-4 결정 (`18e8ad1`) | GP-2 수단 = R-4 (R-3 detection 우선 + R-1/R-2 prevention deferred trajectory). R-5 영구 분리 |
    70	| 51 audit §2 (`f7ac61d`) | GP-2 Exit 5조건 — 본 cycle 현행화 (51 audit "(d) gap" = 부정확, secret-hygiene D-2 이미 운영) |
    71	
    72	### §1.2 GP-2 = 송신 redaction 영역 정의 (governance §4)
    73	
    74	- Hermes / Worker Agent 가 stdout/stderr/log file/LLM API request body 에 secret 노출 차단 (송신/로그 경로 한정).
    75	- ADR-011 §2.3 #2: "Hermes 자체 redaction은 로그/LLM 송신 방어로만 신뢰, 저장 경로 차단 책임 0" (DB INSERT = GP-1 책임).
    76	- 본 repo = DESIGN/governance repo (docs + tools + CI). 실 runtime redaction = Hermes upstream (R-1). 본 repo GP-2 PASS = redaction 패턴 정의 (R-4) + CI 회귀 검출 (R-3) + 설계 권위 (ADR-011 §2.3).
    77	
    78	---
    79	
    80	## §2 Evidence 매트릭스 (GP-2 Exit 5조건, 51 audit §2.2 현행화)
    81	
    82	⭐ **B-1 정정**: GP-2 Exit 조건을 **3축 분리** (detection-layer PASS scope 명확화) — (a) 설계 동등성 ≠ prevention 입증, prevention 능동 redaction 은 in-repo 입증 0 (Hermes upstream 위임).
    83	
    84	**축 1 — detection-layer (본 cycle PASS scope, operative ✅)**:
    85	
    86	| # | 조건 | 상태 | evidence |
    87	|---|------|------|---------|
    88	| (b) | 격리 환경 PoC 실증 (detection) | ✅ | secret-hygiene D-2 scan-log redaction PoC (`redaction_pass/env_redacted.txt` rc=0 잔존 0 + `redaction_fail/partial_redact.txt` rc=1 leak 검출) + `r4-1-trigger-extension-evidence.md` (R-4.1 PoC) — N-3: 51 "(b) 부분" → ✅ 격상 근거 = secret-hygiene D-2 송신 redaction residual CI |
    89	| (d) | 자동 회귀 검증 경로 (detection) | ✅ ⭐ | **`secret-hygiene-egress-redaction.yml` D-2 step (scan-log redaction residual, `secret_scanner.py --mode scan-log`) — 51 audit "❌ gap" 부정확 정정 (52 entry PoC 시제 발견 동형). actual run `26517803107` success (headSha `4fec6485`). secret-hygiene = `workflow_dispatch` 미지원 (schedule cron `0 3 * * *` 만) — secret_scanner.py + workflow + redaction fixtures = 49 entry (`4fec6485`) 이후 변경 0 (불변) → 유효 evidence** |
    90	| (c) | ADR/SDD 권위 명시 | ✅ | ADR-011 §2.3 #2 (송신 방어 신뢰, 저장 경로 책임 0) + governance §4 (GP-2 정의) |
    91	
    92	**축 2 — 설계 동등성 (⚠️ partial, prevention 입증 아님)**:
    93	
    94	| # | 조건 | 상태 | evidence |
    95	|---|------|------|---------|
    96	| (a) | 동등 이상 보안 결과 | ⚠️ **partial (설계 동등성 한정)** | `redaction-pattern-equivalence.md` (R-4 — Tier-1 42 catalog 패턴 *동등성 문서*). ⚠️ **B-1**: governance §4 (a) (line 451) = "Hermes native redaction 적용 검증 + facade redaction filter 검증" = **prevention (R-1/R-2) 검증** — 현 상태 R-1 부재 + R-2 placeholder. redaction-pattern-equivalence = 설계 비교 문서 (line 33 Hermes safety 선언 *금지*), prevention *입증* 아님. → (a) full 충족 = R-1/R-2 prevention 선행 (deferred) |
    97	
    98	**축 3 — prevention (능동 redaction, in-repo 입증 0 = Hermes upstream 위임)**:
    99	
   100	| 수단 | 상태 | 위임 |
   101	|------|------|----|
   102	| R-1 Hermes native redaction | ❌ 본 repo 부재 | Hermes upstream runtime operative (ADR-011 §2.3 #2 위임 권위), import 결정 별도 cycle |
   103	| R-2 facade RedactionFilter | ⚠️ placeholder | facade real (TR-1) deferred trajectory |
   104	
   105	→ **detection-layer PASS = (b)(d)(c) ✅ operative + (a) 설계 동등성 partial. prevention (R-1/R-2) = in-repo 입증 0 (upstream 위임)**. (e2) = 본 cycle 풀 3+1 + 외부 LLM 1+ + 사용자 명시. **full GP-2 PASS = detection-layer + prevention (R-1/R-2) 선행 (별도 trajectory)**.
   106	
   107	---
   108	
   109	## §3 R-3 detection (operative) + R-1/R-2 prevention (deferred) 분리 (57 (β) + 59 Layer 2a 답습)
   110	
   111	### §3.1 수단별 상태 (R-4 defense-in-depth)
   112	
   113	| 수단 | 역할 | 본 repo 상태 | PASS 영향 |
   114	|------|----|-----------|---------|
   115	| **R-3** log canary CI (`secret-hygiene-egress-redaction.yml` + `secret_scanner.py --mode scan-log`) | **detection (회귀 검증)** | ✅ operative green | GP-2 (d) 자동 회귀 충족 — in-repo operative means |
   116	| **R-1** Hermes native redaction (`agent/redact.py`) | **prevention (능동 redaction)** | ❌ 본 repo 부재 (Hermes upstream v0.12.0) | runtime prevention = Hermes upstream operative (import 결정 별도 cycle). ADR-011 §2.3 #2 송신 방어 신뢰 |
   117	| **R-2** facade RedactionFilter | prevention (LLM API 진입점) | ⚠️ facade placeholder | facade real (TR-1) 시점 추가 layer (deferred trajectory) |
   118	| **R-5** base64/URL/압축 evasion | (out of scope) | ❌ known limitation (`base64_evasion.txt` fixture) | 영구 분리 (MVP-2/3, G3-4) |
   119	
   120	### §3.2 means-vs-ends 정합 (59 Layer 2a DEFER **부분 동형** — B-2 정정)
   121	
   122	- **ends** = secret 송신/로그 leak 0.
   123	- **detection ends** = R-3 (secret-hygiene D-2 CI) ✅ operative green — 송신/로그에 secret 잔존 시 BLOCK (회귀 검증). **본 repo in-repo operative**.
   124	- **prevention ends** = R-1 (Hermes upstream native redaction, 실 runtime operative — 본 repo DESIGN repo 이므로 import 미결정) + R-2 (facade real deferred). **본 repo in-repo 능동 redaction 보증 0**.
   125	- ⚠️ **B-2 — 59 Layer 2a 와 *부분 동형* (의사결정 형식만, cover 구조 비대칭)**: 59 = DEFER ends (history rewrite 차단) 가 **in-repo 2 operative layer** (2b branch protection + rewrite-defense CI) 이중 cover. GP-2 = DEFER prevention (능동 redaction) ends 를 cover 하는 **in-repo layer 0** — Hermes upstream (repo 외부) 단독 위임 (ADR-011 §2.3 #2). 즉 보안 cover 구조 비대칭, "완전 동형" 표현 회피.
   126	
   127	→ **GP-2 detection-layer PASS = detection (R-3 in-repo operative) + 설계 권위 + 패턴 동등성 (설계 한정). prevention 능동 redaction = in-repo 보증 0, Hermes upstream 위임 (R-1) + facade real (R-2) deferred trajectory = full GP-2 PASS 선행** (57 (β) 결정 답습, 59 DEFER *부분* 동형).
   128	
   129	---
   130	
   131	## §4 ADR-011 §2.1 (a)~(d) 모법 + (e2) ADR-012 §4 확장 (59 B-2 framing 답습)
   132	
   133	> ⚠️ 59 B-2 답습: ADR-011 §2.1 = (a)~(d) 4조건 모법, "(e) 합의 APPROVE" = ADR-012 §4 "(a)~(d)+(e) 5조건 답습" 확장. **N-1**: "(e2)" = 59 B-2 도입 *프로젝트 내부 label* ((e2) PASS 발효 / (e1) 진입 권한 분리), ADR 본문 문자열 아님.
   134	
   135	| 조건 | 출처 | GP-2 detection-layer 충족 |
   136	|------|------|---------|
   137	| (a) 동등 이상 보안 결과 | ADR-011 §2.1 | ⚠️ **partial (설계 동등성 한정)** — R-4 패턴 동등성 문서. full = R-1/R-2 prevention 검증 선행 (B-1) |
   138	| (b) 격리 PoC (detection) | ADR-011 §2.1 | ✅ secret-hygiene D-2 + r4-1 PoC |
   139	| (c) ADR/SDD 권위 | ADR-011 §2.1 | ✅ ADR-011 §2.3 #2 + governance §4 |
   140	| (d) 자동 회귀 검증 (detection) | ADR-011 §2.1 | ✅ secret-hygiene D-2 CI green |
   141	| (e2) 합의 APPROVE | ADR-012 §4 확장 (내부 label) | ⏳ 본 cycle |
   142	
   143	→ **detection-layer PASS = (b)(c)(d) ✅ + (a) partial. full GP-2 PASS = (a) prevention (R-1/R-2) 선행**.
   144	
   145	### §4.1 R-5 base64 evasion = known limitation (영구 분리)
   146	
   147	`tests/fixtures/secret_hygiene/redaction_fail/base64_evasion.txt` 존재 — secret-hygiene D-2 가 base64 evasion 미검출 (known limitation 명문, workflow line 13). R-5 = MVP-2/3 분리 (G3-4), GP-2 PASS scope 외. GP-2 PASS = Tier-1 42 catalog 평문 redaction 한정 (base64 evasion 제외 명문).
   148	
   149	---
   150	
   151	## §5 합의 형태 + 풀 3+1 승격 트리거
   152	
   153	### §5.1 합의 형태 = 풀 3+1 + 외부 LLM 1+ (의무)
   154	
   155	**정당화**: PASS *발효* milestone (59 Layer PASS + 32 MVP-1 PASS 답습) + 큰 결정 (ADR-011 §2.4 T3) + 헌법 5조-2 cross-vendor + MVP-2 PASS 직전 단계.
   156	
   157	### §5.2 7 승격 트리거
   158	
   159	| # | trigger | 발화 | 근거 |
   160	|---|---------|----|------|
   161	| 1 | 큰 결정 (PASS 발효 milestone) | ✅ | GP-2 PASS 발효 = MVP-2 PASS 절반 |
   162	| 2 | 아키텍처/SDD/보안 본문 변경 | ❌ | brief = phase0 신규 1 |
   163	| 3 | ADR 본문 변경 | ❌ | 0 |
   164	| 4 | 권위 chain 다중 source 손상 | ⚠️ 부분 | R-S1 (MVP-2 PASS 전 hard gate, 본 cycle 비차단) |
   165	| 5 | 외부 LLM 통합 필요 | ✅ | cross-vendor 의무 |
   166	| 6 | Tier-2/3 catalog 확장 | ❌ | 0 |
   167	| 7 | Hermes PMO 격상 | ❌ | 0 |
   168	
   169	→ **2/7 발화 + 1 부분 → 풀 3+1 + 외부 LLM 1+ 적격**.
   170	
   171	---
   172	
   173	## §6 GP-2 PASS 발효 권고 + 조건
   174	
   175	⭐ **권고 = GP-2 detection-layer PASS 발효 APPROVE WITH CONDITIONS** (B-1: "full GP-2 PASS" 아닌 detection-layer 강등):
   176	
   177	1. **detection-layer (b)(c)(d) ✅ operative + (a) 설계 동등성 partial** — secret-hygiene D-2 PoC + ADR 권위 + R-3 CI 회귀 green + R-4 패턴 동등성 (설계 한정). (e2) = 본 cycle.
   178	2. **조건**:
   179	   - (C-1) **R-1 (Hermes runtime redaction 검증) / R-2 (facade real) = prevention 잔여 trajectory 명문 — full GP-2 PASS 선행** (detection-layer PASS = in-repo 능동 redaction 0, Hermes upstream 위임 ADR-011 §2.3 #2, B-1/B-2)
   180	   - (C-2) **R-5 base64 evasion = known limitation 명문** (Tier-1 42 평문 한정)
   181	   - (C-3) secret-hygiene D-2 actual run = `26517803107` green (`4fec6485`) + 코드 불변 (49 entry 이후 변경 0) = 유효 evidence. workflow_dispatch 미지원 → fresh run = schedule/path 변경 시 (비차단)
   182	3. **R-S1 = GP-2 detection-layer PASS 비차단** (MVP-2 PASS 전 hard gate, 별도 cycle).
   183	
   184	→ **GP-2 detection-layer PASS 발효 자격 = (b)(c)(d) detection 충족 + (a) 설계 동등성 + (e2) 합의 APPROVE + 사용자 명시 + (C-1) prevention 잔여 trajectory 명문**. **full GP-2 PASS = + R-1/R-2 prevention 검증 (별도 trajectory)**.
   185	
   186	---
   187	
   188	## §7 금지 사항
   189	
   190	§0.2 답습 (12). 추가: MVP-2 PASS 자동 선언 0 / R-1 Hermes import 결정 0 / R-2 facade real 0 / R-5 evasion 진입 0 / R-S1 자동 정정 0 / 자동 후속 0.
   191	
   192	---
   193	
   194	## §8 다음 단계 (사용자 명시 의무 — 자동 진입 0)
   195	
   196	1. 본 brief 승인 → 풀 3+1 + 외부 LLM 1+ (codex (E-α)) → Reviewer 통합 → v1.1 흡수 → commit + push → **GP-2 detection-layer PASS 발효**
   197	2. **MVP-2 Implementation Evidence PASS 발효 합의** (Layer 통합 PASS ✅ + GP-2 **detection-layer** PASS ✅ + R-S1 hard gate 후, 32 답습) — ⚠️ **full GP-2 PASS (prevention R-1/R-2) = MVP-2 PASS 잔여 trajectory** (MVP-2 PASS 도 prevention deferred scope 명문 또는 prevention 선행 — MVP-2 PASS cycle 에서 결정)
   198	3. R-S1 cross-reference 정정 cycle (MVP-2 PASS 전 hard gate 3 옵션)
   199	4. **full GP-2 PASS trajectory** — R-1 Hermes runtime redaction 검증 (import) / R-2 facade real (TR-1) prevention (별도 cycle)
   200	
   201	---
   202	
   203	## §9 cross-reference 답습
   204	
   205	- ADR-011 §2.1 (a)~(d) 모법 + §2.3 #2 (송신 방어 신뢰) — `docs/decisions/ADR-011-means-vs-ends-redaction.md`
   206	- ADR-012 §4 (e 확장) — `docs/decisions/ADR-012-evidence-ledger-protection.md`
   207	- governance-preconditions.md §4 (GP-2)
   208	- redaction-pattern-equivalence.md (R-4) + r4-1-trigger-extension-evidence.md (R-4.1) + g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md (Group D PoC)
   209	- 51 audit §2 + 57 (β) brief v1.1 + 59 Layer PASS brief v1.1 + 합의
   210	- 실 evidence: `secret-hygiene-egress-redaction.yml` (D-2) + `tools/secret_scanner.py` (--mode scan-log) + `tests/fixtures/secret_hygiene/{redaction_pass,redaction_fail}/`
   211	
   212	---
   213	
   214	## §10 자기진단 (메타 편향 회피)
   215	
   216	| # | 위험 | 처리 |
   217	|---|------|----|
   218	| P-1 | GP-2 PASS *기정사실화* | 발효 = 합의 APPROVE + 사용자 명시 후 (§0.2 #1 + §8) |
   219	| P-2 | R-3 detection 만으로 GP-2 PASS *단순화* (prevention R-1/R-2 부재 은폐) | §3 detection/prevention 분리 명시 + (C-1) deferred 명문 (59 Layer 2a DEFER 답습, β B-1 cascade 교훈) |
   220	| P-3 | 51 audit "(d) gap" → 본 brief "(d) ✅" 격상 over-claim risk | §2 (d) = secret-hygiene D-2 CI green actual run 근거 (filesystem + run direct verify), 52 entry PoC 시제 발견 동형 (gap 표기 부정확 정정) |

exec
/bin/bash -lc "nl -ba docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md | sed -n '1,240p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# SC-2 R-1 Hermes 위임 검증 brief (v1.1)
     2	
     3	> **작성**: 2026-05-28 (66번째 entry 진입 cycle — 세션 #3)
     4	>
     5	> **v1 → v1.1 갱신 (reframe)**: 풀 3+1 + 외부 LLM 1+ (codex gpt-5.5 cross-vendor) 통합 합의 (`docs/review/3plus1-consensus-2026-05-28-mvp2-sc2.md`) **APPROVE WITH CONDITIONS (4 source 전원) → BLOCKING 4 + 권고 4 reframe 흡수** (60 detection reframe 동형). **핵심 정정 (60 over-claim cascade 재발)**: **B-1 축 3 R-6 자동 회귀 over-claim** (Reviewer verify: r2-canary.yml = R-4.1 Tier-1 42 catalog canary, **Hermes dependency lock trigger 미구현** — Hermes egress 자동 회귀 아님) → "ADR 의무 *요구* / 현 R-6 Tier-1 catalog operative" / **B-2 HERMES_REDACT_SECRETS opt-in 활성화 전제** (기본 false, v0.12.0 ON→OFF) → "활성화된 Hermes redaction" / **B-3** artifact 부재 완화 (docker/r2-poc 골격 존재) + URL 출처 불명 / **B-4** 위치 evidence 시점성. **"충족" → "조건부/문서 기반 충족"** (R-1 prong = Exit (a) Hermes-native sub-evidence). evidence 실증 (위치+동등성), framing over-claim 정정. §11 흡수 매트릭스 추가.
     6	>
     7	> **scope** (사용자 명시 "문서 종합 위임 검증 + contract"): **R-1 (Hermes native redaction) 위임 검증 종합** — day2-r1 (위치) + R-4 §5 (동등성) + R-6 (Tier-1 canary, Hermes 자동 회귀 *의무*) + ADR-011 §2.3 #2 (위임 권위) 종합 + **evidence contract 명문** (version pin v0.12.0 + R-6 + 격리 실행 SOP). **실 격리 canary 실행 = artifact 재확보 시점 deferred** (day2-r1 "코드 분석 충분" 선례). 실 코드 0.
     8	>
     9	> ⚠️ **over-claim 경계 (본 세션 #2 4회 cascade 교훈 + R-4 §7.3 답습)**: 본 cycle = **R-1 위임 *검증* (Hermes 가 GP-2 영역에 redaction 적용 + Tier-1 동등 이상 커버 + 자동 회귀)**. ≠ **"Hermes 안전성 선언"** (ADR-011 §7.3 "본 ADR 은 Hermes 안전성을 선언하지 않는다" 금지). 위치/동등성 *사실* 검증이지 "Hermes redaction 완벽" 선언 아님.
    10	>
    11	> **본 cycle = 큰 cycle** (full GP-2 PASS Exit (a) R-1 prong, 풀 3+1 + 외부 LLM 1+).
    12	>
    13	> **본 cycle 발효 효과** = full GP-2 PASS Exit (a) **R-1 prong 위임 검증 충족** (Hermes upstream 위임 실효 확인). R-2 prong = SC-1 (facade RedactionFilter) ✅ 이미 발효 → **full GP-2 PASS = R-1 ∧ R-2 충족 → SC-3 발효 합의 (별도)**.
    14	>
    15	> **선행 답습**: 65 SC-1 (R-2 facade RedactionFilter operative) + 64 trajectory §3 (R-1 = upstream 위임, (R-1-a) 권고 + evidence contract 의무) + day2-r1 (R-1 위치 검증) + R-4 §5 (Hermes ⊇ Tier-1) + ADR-011 §2.3 #2 (위임 권위)
    16	
    17	---
    18	
    19	## §0 본 brief 의 범위
    20	
    21	### §0.1 본 brief 가 *하는* 것
    22	
    23	1. **R-1 위임 검증 4축 종합** (위치 / 동등성 / 자동 회귀 / 권위) (§2)
    24	2. **evidence contract 명문** (version pin v0.12.0 + R-6 자동 재실행 + 격리 실행 SOP) (§3)
    25	3. **실 격리 canary 실행 deferred 정당화** (day2-r1 선례 + artifact 부재) (§4)
    26	4. **R-1 prong 충족 판정 + over-claim 경계** (§5)
    27	5. **합의 형태 + Rollback + Evidence + 자기진단** (§6~§10)
    28	
    29	### §0.2 본 brief 가 *하지 않는* 것
    30	
    31	| # | 영역 | 위반 |
    32	|---|------|----|
    33	| 1 | **"Hermes 안전성 선언"** (ADR-011 §7.3 금지 — 위임 *검증* ≠ 안전 선언) | 0 |
    34	| 2 | **full GP-2 PASS 발효** (SC-3 별도 cycle — R-1 ∧ R-2 충족 후) | 0 |
    35	| 3 | **R-1 Hermes `agent/redact.py` 본 repo import** (위임 검증 = import 0, R-1-a) | 0 |
    36	| 4 | **실 격리 canary 실행** (artifact 부재 → 재확보 시점 deferred, SOP 명문만) | 0 |
    37	| 5 | Hermes upstream re-clone / agent/redact.py 본문 변경 | 0 |
    38	| 6 | hermes-version.yaml **파일 생성** (governance 명문 답습 — 파일화는 절충안, 본 cycle contract 명문만) | 0 |
    39	| 7 | R-4 / day2-r1 / governance / ADR-011 본문 변경 | 0 |
    40	| 8 | 실 코드 / CI / r2-canary.yml 본문 변경 | 0 |
    41	| 9 | SC-1 (R-2) 재선언 / detection-layer PASS (60) 재선언 | 0 |
    42	| 10 | 자동 SC-3 진입 | 0 (사용자 명시 의무) |
    43	
    44	### §0.3 권위 답습 source
    45	
    46	- **day2-r1** (`docs/phase0/day2-r1-redaction-location-verification.md`) — R-1 *위치* 검증 (Hermes redaction = 로그/도구출력/gateway 통신 전용, 25 import 비-DB, docstring "mask API keys/tokens/credentials before log/output/gateway"). ⚠️ day2-r1 "FAIL" = **G1a (DB INSERT 경로) 맥락** (DB = GP-1 책임). **GP-2 (송신/로그) 맥락에서는 Hermes redaction 적용 ✅** (위임 근거).
    47	- **R-4 §5** (`docs/architecture/redaction-pattern-equivalence.md`) — Hermes **47 카테고리 + 2 frozenset ⊇ Tier-1 45 catalog** (Hermes ⊇ P1_REDACTOR ⊇ baseline). §7.3 "Hermes 안전성 선언 금지".
    48	- **R-6** (`.github/workflows/r2-canary.yml`) — Tier-1 42 canary regression (nightly cron + PR), Hermes 의존성 변경 시 R-2/R-4.1 자동 재실행 (ADR-011 §2.3 #4).
    49	- **ADR-011 §2.3 #2** (line 113) — "Hermes 자체 redaction 은 로그/LLM 송신 방어로만 신뢰" (R-1 위임 권위) + §2.3 #4 (자동 회귀) + §7.3 (안전성 선언 금지).
    50	- **governance §4.5 (a)** — "Hermes native redaction Tier-1 42 catalog 적용 검증 + facade redaction filter 검증" (R-1 + R-2). **§1.2.7 P11 / Layer 1** — hermes-version.yaml v0.12.0 pin.
    51	- **65 SC-1** — R-2 prong (facade RedactionFilter) operative.
    52	- **canary-recheck-design.md (R-5)** — canary 재검증 trigger 설계 (HERMES_REDACT_SECRETS config 체크).
    53	
    54	---
    55	
    56	## §1 진입 컨텍스트
    57	
    58	- 65 SC-1 (R-2 facade RedactionFilter) operative → full GP-2 PASS Exit (a) R-2 prong ✅.
    59	- 본 SC-2 = R-1 prong (Hermes native redaction 위임 검증). full GP-2 PASS = R-1 ∧ R-2 (AND, 64 trajectory §2.2).
    60	- R-1 = Hermes upstream 위임 (ADR-011 §2.3 #2). 본 repo = DESIGN/governance repo → R-1 *재구현/import* 0, **위임 실효 검증** ((R-1-a), 64 §3.3).
    61	
    62	---
    63	
    64	## §2 R-1 위임 검증 4축 종합
    65	
    66	### §2.1 축 1 — 위치 검증 (활성화된 Hermes redaction = GP-2 영역 적용) ✅ (시점성 명시)
    67	
    68	day2-r1 (**2026-05-05 코드 분석 시점**, Hermes v0.12.0) 결정적 사실 3건:
    69	- **사실 1**: `agent/redact.py:1-8` docstring = "Regex-based secret redaction **for logs and tool output** ... mask API keys, tokens, and credentials **before they reach log files, verbose output, or gateway logs**".
    70	- **사실 2**: redaction import 25개 위치 = 로깅/도구출력/통신 경로 (DB write 0).
    71	- **사실 3**: `hermes_state.py` (SessionDB) redaction import 0 (DB INSERT 미적용).
    72	
    73	→ **활성화된 Hermes redaction = GP-2 영역 (로그/LLM 송신/도구출력) 적용 ✅**. day2-r1 "FAIL" = G1a (DB INSERT) 맥락 (DB = GP-1 책임, ADR-011 §2.3 #2/#3) — **GP-2 위임 근거와 모순 0** (GP-2 영역 적용 입증).
    74	
    75	⚠️ **B-2 활성화 전제 (위임 실효 필수 조건)**: `HERMES_REDACT_SECRETS=false` = **기본 opt-in** (R-4 line 138, v0.12.0 breaking change default ON→OFF). day2-r1 §2 "security.redact_secrets: true 활성화 후" 전제. → 위임 검증 = **`HERMES_REDACT_SECRETS=true` 활성화 전제** (미활성화 시 redaction 미작동). evidence contract C-5 (활성화 config 검증, §3) 신설.
    76	
    77	⚠️ **B-4 시점성**: 위치 evidence = 2026-05-05 day2-r1 코드 분석 (Hermes v0.12.0). **artifact 부재로 현 시점 재확인 = C-3 SOP (artifact 재확보) 시점**. day2-r1 "코드 분석 충분" 선례 답습 (실 재확인 = 동일 결론 강화).
    78	
    79	### §2.2 축 2 — 패턴 동등성 (Hermes ⊇ Tier-1) ✅
    80	
    81	R-4 §5 3-way 비교:
    82	- Hermes **35 prefix + 12 regex + 2 frozenset (16+14 키) = 47 카테고리 + 2 frozenset**.
    83	- Tier-1 catalog (secret_scanner, R-4.1) = baseline 5 + prefix 31 + regex 7 + alternation 2 = 45.
    84	- **Hermes ⊇ P1_REDACTOR + Hermes ⊇ Tier-1** (Hermes superset — R-4 §5.3 "핵심 관찰 #1").
    85	
    86	→ **활성화된 Hermes native redaction 이 Tier-1 42 catalog 를 동등 이상 커버 ✅** (governance §4.5 (a) "Tier-1 42 catalog 적용" 충족). ⚠️ R-4 = 설계 동등성 비교 (§7.3 안전성 선언 아님) — "Hermes 가 Tier-1 패턴을 *포함*" 사실 검증. **출처 (R-2 정정)**: R-4 §5 동등성 매트릭스 **+ R-4.1/R-6 catalog 체계** (R-4 §5 단독 아님 — Tier-1 42/45 = R-4.1 확장).
    87	
    88	### §2.3 축 3 — 자동 회귀 검증 (현 R-6 = Tier-1 canary operative / Hermes lock trigger 미구현) ⚠️
    89	
    90	⚠️ **B-1 over-claim 정정 (60 cascade 재발, 4 source + Reviewer verify CONFIRMED)**:
    91	- **현 R-6 (r2-canary.yml) = "R-4.1 Tier-1 42 catalog canary regression"** (nightly cron `0 18 * * *` + PR). paths trigger = `docker/r4-1-poc` + `docker/r2-poc` + canary-recheck-design.md + workflow. **`hermes-version.yaml` / Hermes dependency lock diff trigger 0** → **Hermes native redaction egress 자동 회귀 *아님*** (우리 Tier-1 catalog canary).
    92	- **ADR-011 §2.3 #4 + governance §1.2.7 Layer 1 = Hermes 의존성 변경 시 R-2/R-4.1 자동 재실행 *의무 요구***. 단 **현 R-6 = Tier-1 catalog canary까지만 operative** (Hermes dependency lock trigger 미구현 = 잔여 작업).
    93	
    94	→ **현 operative = Tier-1 42 catalog silent 깨짐 자동 검출 ✅ / Hermes upstream 변경 자동 회귀 = ADR 의무 요구, 미구현 (R-6 확장 잔여)**. R-1 자동 보증 착시 제거 (R-6 ≠ Hermes egress canary).
    95	
    96	### §2.4 축 4 — 위임 권위 (ADR-011 §2.3 #2) ✅
    97	
    98	- ADR-011 §2.3 #2: "Hermes 자체 redaction 은 로그/LLM 송신 방어로만 신뢰, 저장 경로 책임 0".
    99	- ⚠️ **Hermes ≠ root of trust** (권위 위계): Hermes 출력은 Tools (canary/R-6)로 검증 → 위임 ≠ 맹신 (R-6 자동 회귀가 위임 위에 위치).
   100	
   101	→ **R-1 = ADR 권위로 위임된 영역** (본 repo 재구현 불요), 위임 실효 = 축 1+2+3 검증.
   102	
   103	---
   104	
   105	## §3 Evidence Contract (version pin + R-6 + SOP)
   106	
   107	R-1 위임 검증의 *지속 유효성* contract (64 §3.3 evidence contract 의무 답습):
   108	
   109	| # | contract | 현 상태 | 본 cycle |
   110	|---|----------|------|------|
   111	| C-1 | **version pin v0.12.0** | governance §1.2.7 P11/Layer 1 **문서 명문** (hermes-version.yaml 파일 부재 = enforcement 미실체) | contract 명문 수준 (파일화 enforcement = 절충안, 별도) — R-4 정정 |
   112	| C-2 | **Tier-1 catalog 회귀** | r2-canary.yml operative (nightly + PR, Tier-1 42 canary) | 답습 유지 (변경 0) |
   113	| C-3 | **격리 실행 SOP** | day2-r1 §7 R-2 PoC 절차 + docker/r2-poc 골격 (B-3) | SOP 명문 (실 실행 deferred, §4) |
   114	| C-4 | **Hermes 의존성 변경 trigger** | ADR-011 §2.3 #4 + governance Layer 1 = **의무 요구 (미구현 = R-6 확장 잔여)** | 답습 유지 (B-1) |
   115	| C-5 ⭐ | **HERMES_REDACT_SECRETS=true 활성화 검증** (B-2) | R-4 line 138 = 기본 false opt-in | 활성화 config 검증 의무 명문 (위임 실효 전제) |
   116	
   117	⭐ **격리 실행 SOP (C-3, artifact 재확보 시 실행 절차)**:
   118	1. Hermes upstream v0.12.0 re-clone (⚠️ **clone URL 출처 확보 선결** — day2-r1 §3.1 = grep 명령 (URL 아님), ADR-008 미확인, B-3)
   119	2. `HERMES_REDACT_SECRETS=true` 활성화 (C-5 전제) + 격리 환경 (Docker, docker/r2-poc 골격 답습) canary 주입 (`sk-ant-CANARY-XXXXX` 등 Tier-1 대표 패턴)
   120	3. Hermes redaction 경로 (로그/송신) 통과 → `[REDACTED]` 또는 부분 마스킹 확인
   121	4. Tier-1 42 catalog 대표 패턴 커버 검증 (R-4 §5 답습)
   122	5. evidence = canary-output.log + 적용 결과 (r2-canary.yml artifact 형식 답습)
   123	
   124	---
   125	
   126	## §4 실 격리 canary 실행 deferred 정당화
   127	
   128	⚠️ **현 상태**: Hermes `agent/redact.py` artifact 부재 (/tmp/hermes-phase0 휘발 + 본 repo 부재) + Hermes upstream clone URL 문서 미명시. **단 R-2 PoC 격리 골격 `docker/r2-poc/` 존재** (Dockerfile + compose + r2_poc.py, B-3 — "artifact 완전 부재" 아님, 우리 PoC 골격은 보존) → Hermes native 실 격리 canary 실행 *미시행*.
   129	
   130	**deferred 정당화 (day2-r1 선례 답습)**:
   131	- day2-r1 §3.2 "PoC 미시행 정당성": 코드 분석 (docstring + grep + 시그니처)만으로 **결정적 결론** — "PoC 는 동일 결과 확인이며 시간·환경 비용 대비 추가 정보 가치 0".
   132	- 본 SC-2 = 위치 (day2-r1 ✅) + 동등성 (R-4 §5 ✅) + 자동 회귀 (R-6 ✅) **코드/문서 분석 기반 검증**. 실 격리 canary = 동일 결론 강화 (가치 보강이나 결론 변경 0).
   133	- ⚠️ **단 over-claim 경계**: 본 검증 = "코드/문서 분석 기반" 명시. 실 격리 canary 실행 = artifact 재확보 시 C-3 SOP 실행 (강한 보강 evidence). "실 실행 완료" 주장 0.
   134	
   135	→ **R-1 위임 검증 = 코드/문서 분석 기반 충족** (day2-r1 동형). 실 격리 canary = deferred (C-3 SOP, artifact 재확보 trigger).
   136	
   137	---
   138	
   139	## §5 R-1 prong 충족 판정 + over-claim 경계
   140	
   141	⭐ **판정 = R-1 위임 검증 *조건부/문서 기반 충족* (Exit (a) Hermes-native sub-evidence, R-1+codex reframe)**:
   142	- 축 1 위치 ✅ (활성화 전제) + 축 2 동등성 ✅ + 축 3 = **현 Tier-1 canary operative / Hermes 자동 회귀 의무 미구현** + 축 4 권위 ✅.
   143	- governance §4.5 (a) "Hermes native redaction Tier-1 42 catalog 적용 검증" = **Exit (a)의 Hermes-native sub-evidence 조건부 충족** (축 1+2, 활성화 전제 + R-6 Tier-1 한정 + 위치 시점성 + URL 불명). GP-2 Exit (b) 격리 PoC / (d) R-6 log canary step = SC-3 또는 별도 (R-3 경계).
   144	
   145	⚠️ **over-claim 경계 (4 source 검증 + reframe)**:
   146	- **R-1 위임 검증 ≠ Hermes 안전성 선언** (ADR-011 §7.3). "활성화된 Hermes 가 GP-2 영역에 redaction 적용 + Tier-1 동등 이상 커버" *사실* 검증.
   147	- **조건부/문서 기반 충족** (실 격리 canary 실행 deferred, 활성화 전제, R-6 Tier-1 한정) — day2-r1 동형, "실 실행 완료" 0, "Hermes 자동 회귀 operative" 0.
   148	- **full GP-2 PASS ≠ 본 cycle** — R-1 (SC-2 조건부) ∧ R-2 (SC-1 in-repo) → SC-3 발효 합의 (별도).
   149	
   150	→ **full GP-2 PASS Exit (a) = R-1 prong (SC-2 조건부/문서 기반) + R-2 prong (SC-1 ✅ in-repo operative) → SC-3 발효 자격** (실 격리 canary + Hermes 자동 회귀 R-6 확장 = SC-3 강한 보강 또는 별도 trigger).
   151	
   152	---
   153	
   154	## §6 합의 형태 + 승격 트리거
   155	
   156	### §6.1 합의 형태 = 풀 3+1 + 외부 LLM 1+
   157	
   158	**정당화**: full GP-2 PASS Exit (a) R-1 prong (보안 영역) + 큰 결정 (위임 검증 milestone) + 5조-2 cross-vendor + Hermes ≠ root of trust (다중 검증 의무).
   159	
   160	### §6.2 승격 트리거
   161	
   162	| # | trigger | 발화 |
   163	|---|---------|----|
   164	| 1 | 큰 결정 (full GP-2 PASS R-1 prong) | ✅ |
   165	| 2 | 보안 (GP-2 prevention 위임) | ✅ |
   166	| 3 | 외부 LLM cross-vendor (5조-2) | ✅ |
   167	| 4 | Hermes 위임 검증 (≠ root of trust 다중 검증) | ✅ |
   168	
   169	→ **4/4 발화 → 풀 3+1 + 외부 LLM 1+**.
   170	
   171	---
   172	
   173	## §7 금지 사항
   174	
   175	§0.2 답습 (10). 추가: Hermes 안전성 선언 0 / 실 격리 canary "실행 완료" 주장 0 / agent/redact.py import 0 / full GP-2 PASS 발효 0 / hermes-version.yaml 파일 생성 0 (절충안 deferred) / 자동 SC-3 진입 0.
   176	
   177	---
   178	
   179	## §8 Rollback Trigger
   180	
   181	| # | trigger | 대응 |
   182	|---|---------|----|
   183	| RT-1 | Hermes upstream v0.12.0 redaction silent 깨짐 | R-6 자동 재실행 (r2-canary.yml) + R-5 canary 재검증 |
   184	| RT-2 | 실 격리 canary 실행 시 day2-r1 결론과 불일치 | C-3 SOP 실행 결과 우선 → R-1 위임 검증 재평가 (코드 분석 < 실 실행) |
   185	| RT-3 | Hermes 의존성 변경 (hermes-version.yaml drift) | governance Layer 1 (lock diff → R-2/R-4.1 재실행 + merge BLOCK) |
   186	| RT-4 | "Hermes 안전성 선언" over-claim 발생 | §5 over-claim 경계 명문 (위임 검증 ≠ 안전 선언) |
   187	
   188	---
   189	
   190	## §9 Evidence
   191	
   192	- E-1: day2-r1 위치 검증 (Hermes redaction = GP-2 영역, 25 import 비-DB)
   193	- E-2: R-4 §5 동등성 (Hermes 47 ⊇ Tier-1 45)
   194	- E-3: r2-canary.yml R-6 operative (nightly + PR)
   195	- E-4: ADR-011 §2.3 #2 위임 권위 + #4 자동 회귀
   196	- E-5: C-3 격리 실행 SOP (artifact 재확보 시, deferred)
   197	
   198	---
   199	
   200	## §10 자기진단 (메타 편향 회피)
   201	
   202	| # | 위험 | 처리 |
   203	|---|------|----|
   204	| P-1 | "Hermes 안전성 선언" over-claim | §0 + §5 — 위임 *검증* (사실) ≠ 안전 선언 (ADR-011 §7.3), [[feedback_pass_scope_overclaim]] |
   205	| P-2 | day2-r1 "FAIL" 을 GP-2 위임 부정으로 오인 | §2.1 — "FAIL" = G1a (DB) 맥락, GP-2 (송신) 적용 ✅ (모순 0) |
   206	| P-3 | 실 격리 canary 미실행 → 검증 미충족 오인 | §4 — day2-r1 "코드 분석 충분" 선례 + deferred 명문 ("실 실행 완료" 0) |
   207	| P-4 | full GP-2 PASS 기정사실화 | §5 — R-1 ∧ R-2 → SC-3 별도 (§0.2 #2) |
   208	| P-5 | R-4 설계 동등성을 prevention 입증으로 격상 | §2.2 — R-4 = 패턴 *포함* 사실 (§7.3 안전성 선언 금지) |
   209	| P-6 | 작성자 = 64/65 작성자 (Claude) cascade | cross-vendor codex + 풀 3+1 독립 검증 |
   210	| P-7 | hermes-version.yaml 파일 부재 = contract 미충족 오인 | §3 C-1 — governance 명문 답습 (파일화 = 절충안 별도), contract 명문 유효 |
   211	
   212	---
   213	
   214	## §11 v1.1 흡수 매트릭스 (BLOCKING 4 + 권고 4 reframe)
   215	
   216	본 v1.1 = `docs/review/3plus1-consensus-2026-05-28-mvp2-sc2.md` 답습 1pass reframe 흡수 (60 detection reframe 동형). **4 source 전원 APPROVE WITH CONDITIONS** (codex BLOCKING 0 조건3 + Agent A 2 + Agent B 2 + Agent C 3). **60 over-claim cascade 재발** — 4 source가 R-6/activation framing over-claim 포착 (본 세션 #3 첫 cascade). evidence 실증 (위치+동등성), framing 정정.
   217	
   218	| # | 흡수 | source | 정정 위치 |
   219	|---|------|--------|------|
   220	| B-1 ⭐ | 축 3 R-6 자동 회귀 over-claim → "현 R-6 = Tier-1 42 catalog canary operative / Hermes dependency lock trigger 미구현 (ADR 의무 요구)" (Reviewer verify: r2-canary = R-4.1 Tier-1 canary) | codex+A+B+C (Reviewer CONFIRMED) | §2.3 + C-4 |
   221	| B-2 ⭐ | HERMES_REDACT_SECRETS opt-in (기본 false) → "활성화된 Hermes redaction" + C-5 활성화 검증 전제 신설 | codex+A+B | §2.1 + §3 C-5 |
   222	| B-3 | artifact 부재 완화 (docker/r2-poc 골격 존재) + Hermes clone URL 출처 불명 (day2-r1 §3.1 ≠ URL) | Agent C (Reviewer 부분 정정) | §3 C-3 + §4 |
   223	| B-4 | 위치 evidence 시점성 (2026-05-05 day2-r1, artifact 재확인 = C-3) | Agent A | §2.1 |
   224	| R-1 | "R-1 prong 충족" → "Exit (a) Hermes-native sub-evidence 조건부/문서 기반 충족" | codex 3 | §5 + title |
   225	| R-2 | 동등성 출처 = R-4 §5 + R-4.1/R-6 catalog 체계 | codex 4 | §2.2 |
   226	| R-3 | GP-2 Exit (b)/(d) = SC-3 또는 별도 (R-1 prong 경계) | codex 3 | §5 |
   227	| R-4 | version pin = 문서 명문 vs 파일 enforcement 구분 | codex NOTE | §3 C-1 |
   228	
   229	**4 source 정합 (positive)**: over-claim 1차 경계 (Hermes 안전성 선언/full GP-2 PASS 격상/실 실행 완료 주장) 견고 / day2-r1 FAIL 재해석 타당 (G1a DB ≠ GP-2 송신, 4 source 공통) / R-2 prong (SC-1) 발효 filesystem 실측 / 권위 인용 일치 (codex 6/8, R-6 dependency trigger 부분만).
   230	
   231	---
   232	
   233	**본 brief v1.1 끝.**
   234	
   235	**다음 단계**: SESSION + INDEX commit + push → **R-1 위임 검증 조건부/문서 기반 충족 (활성화 전제 HERMES_REDACT_SECRETS=true + R-6 Tier-1 한정 + 위치 시점성)**. 후속: **SC-3 (full GP-2 PASS 발효 합의)** — R-1 (SC-2 조건부) ∧ R-2 (SC-1 in-repo) + 실 격리 canary + Hermes 자동 회귀 R-6 확장 보강 = 사용자 명시 별도 cycle.

exec
/bin/bash -lc "nl -ba docs/architecture/governance-preconditions.md | sed -n '418,466p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
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

exec
/bin/bash -lc "nl -ba docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md | sed -n '1,280p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# SC-1 facade RedactionFilter (R-2 GP-2 prevention) 실 구현 brief (v1.1)
     2	
     3	> **작성**: 2026-05-28 (65번째 entry 진입 cycle — 세션 #3)
     4	>
     5	> **v1 → v1.1 갱신**: 풀 3+1 + 외부 LLM 1+ (codex gpt-5.5 cross-vendor) 통합 합의 (`docs/review/3plus1-consensus-2026-05-28-mvp2-sc1.md`) **APPROVE WITH CONDITIONS (4 source 전원) → BLOCKING 4 + 권고 6 1pass 흡수**. 핵심 정정: **B-1 catalog 재사용 (i) src→tools import → (ii) 공유 모듈 추출** (Reviewer verify: (i) namespace package 동작하나 의존 방향 부적절, 3:1 majority) / **B-2 `[REDACTED]` whole-match → group-aware 치환** (값만 마스킹, key/구조 보존 — secret_scanner = 검출 전용 치환 함수 0) / **B-3 송신 redaction 권위 = governance §4.1 + 64 trajectory** (§8.2 = egress 보조) / **B-4 범위 = messages + metadata** (full fields deferred). §12 흡수 매트릭스 추가.
     6	>
     7	> **scope** (사용자 명시 "RedactionFilter 집중"): **RedactionFilter 완전 구현 (secret_scanner Tier-1 45 catalog 공유 모듈 추출 재사용, R-2-c (ii)) + facade `complete()` 송신 전 redaction 적용 layer 통합**. **LiteLLM Router 위임 = deferred (Provider Liquidity 별도 sub-cycle)**. TDD 적용.
     8	>
     9	> ⚠️ **명칭 정직성 (over-claim 차단, 본 세션 #2 4회 cascade 교훈 답습)**: 본 cycle = **facade redaction layer real (R-2 GP-2 prevention)** — **full facade real 아님** (LiteLLM Router 위임 + Min 2 검증 + registry yaml = deferred). "facade real 완성" 표현 금지.
    10	>
    11	> **본 cycle = 큰 cycle (실 코드 + TR-1)** — facade.py 헤더 명시 "real 본문 작성 시 자동 풀 3+1 합의 trigger TR-1 발화". 64 entry SC-1 = 풀 3+1 (TR-1) + 실 코드.
    12	>
    13	> **본 cycle 발효 효과** = R-2 facade RedactionFilter prevention layer **in-repo operative** + GP-2 (a) "facade redaction filter 검증" 충족 (full GP-2 PASS Exit (a)의 R-2 prong). **full GP-2 PASS 발효 = SC-2 (R-1 위임 검증) + SC-3 후 (별도)**.
    14	>
    15	> **선행 답습**: 64 trajectory entry brief (SC-1 정의 + R-2-a 동시 + R-2-c catalog 재사용 + RedactionFilter = facade 내부 협력자 + RT-1 atomic) + llm-providers-design §4.1/§8.2 (설계 명세) + ADR-009 §2.2 (facade 단일 진입점 의무) + secret_scanner Tier-1 45 catalog
    16	
    17	---
    18	
    19	## §0 본 brief 의 범위
    20	
    21	### §0.1 본 brief 가 *하는* 것
    22	
    23	1. **RedactionFilter 인터페이스 + catalog 재사용 (R-2-c) 설계 결정** (§2)
    24	2. **송신 redaction 역할 명세** (GP-2 prevention = request body secret strip, §3)
    25	3. **facade 통합 지점 + Router deferred 처리** (RT-1 window 회피, §4)
    26	4. **TDD 계획** (RED → GREEN → REFACTOR, §5)
    27	5. **합의 형태 + 승격 트리거** (§6)
    28	6. **Provider Liquidity 보존 + 금지 + Rollback Trigger + Evidence + 자기진단** (§7~§11)
    29	
    30	### §0.2 본 brief 가 *하지 않는* 것
    31	
    32	| # | 영역 | 위반 |
    33	|---|------|----|
    34	| 1 | **LiteLLM 설치 + Router 위임 구현** (Provider Liquidity 별도 sub-cycle, deferred) | 0 |
    35	| 2 | **full facade real** (Min 2 검증 + registry yaml + 에러분류 + 정규화 + OAuth lock + callback) | 0 |
    36	| 3 | **full GP-2 PASS 발효** (SC-2 R-1 위임 검증 + SC-3 후) | 0 |
    37	| 4 | **R-1 Hermes 위임 검증** (SC-2 별도 sub-cycle) | 0 |
    38	| 5 | secret_scanner Tier-1 45 catalog **패턴 내용 변경** (R-4.1 답습 "변경 0건", R-7(b) 차등) | 0 |
    39	| 6 | Tier-2/3 catalog 확장 / base64 evasion (R-5 영구 분리) | 0 |
    40	| 7 | detection-layer PASS (60) / MVP-2 PASS (62) 재선언 | 0 |
    41	| 8 | ADR / 헌법 / governance / llm-providers-design 본문 변경 | 0 |
    42	| 9 | llm-providers.yaml registry 작성 (Min 2 검증 의존, Router deferred와 함께) | 0 |
    43	| 10 | 자동 후속 sub-cycle (SC-2/SC-3) 진입 | 0 (사용자 명시 의무) |
    44	
    45	### §0.3 권위 답습 source
    46	
    47	- ⭐ **송신 redaction 권위 (B-3 정정)**: **governance-preconditions.md §4.1** (line 422 — "LLM API request body 에 secret 노출 차단" 송신 경로) + **64 trajectory brief §3** = 송신 redaction PRIMARY 권위. **§8.2 RedactionFilter (docstring "응답·예외·메트릭") = egress(응답/로그) scrub 보조** (송신 redaction은 §8.2 직접 문구 아님, governance 정합 확장).
    48	- **llm-providers-design.md §8.2** (RedactionFilter 설계 — PATTERNS 4 + KEY_BLACKLIST 6, 블랙리스트 채택, egress scrub) + **§4.1** (facade `complete()` 흐름) + **§4.4** (호출 흐름 — redaction 적용 지점 step 5)
    49	- **governance-preconditions.md §4.5 (a)** (facade redaction filter 검증)
    50	- **ADR-009 §2.2** (facade 단일 진입점 의무 — LiteLLM 직접 import = facade.py 한정, provider SDK 직접 import 금지)
    51	- **secret_scanner.py** (Tier-1 45 catalog = baseline 5 + prefix 31 + regex 7 + alternation 2, `ALL_PATTERNS`/`COMPILED_PATTERNS`/`scan_text()`, 외부 의존성 0 stdlib)
    52	- **.importlinter** (root=src, forbidden=LLM SDK facade 예외 — src↔tools 경계 결정 입력)
    53	- **64 trajectory entry brief §4.4** (R-2-a/c 권고 + RedactionFilter = facade 내부 협력자 + RT-1 atomic)
    54	- **redaction-pattern-equivalence.md** (R-4 — Tier-1 catalog 설계 동등성, Hermes 안전성 선언 금지 §7.3)
    55	
    56	---
    57	
    58	## §1 진입 컨텍스트
    59	
    60	- 64 entry trajectory 진입 합의 (APPROVE WITH CONDITIONS 4 source) → carry-over 1순위 SC-1 진입 (사용자 명시).
    61	- GP-2 현 상태: detection-layer PASS (60, R-3 secret-hygiene D-2 CI operative). prevention (R-1/R-2) deferred.
    62	- 본 cycle = **R-2 prevention prong** (facade redaction filter) in-repo 구현 → GP-2 Exit (a)의 R-2 검증 충족 (R-1 = SC-2 별도).
    63	
    64	---
    65	
    66	## §2 RedactionFilter 인터페이스 + catalog 재사용 (R-2-c) 설계 결정
    67	
    68	### §2.1 catalog 재사용 방식 (핵심 설계 결정 — 풀 3+1 검증 대상)
    69	
    70	secret_scanner Tier-1 45 catalog 재사용 (R-2-c, single source detection↔prevention) — import 경계 4 옵션:
    71	
    72	| 옵션 | 방식 | 장점 | 단점 |
    73	|------|----|----|----|
    74	| (i) src → tools.secret_scanner import | RedactionFilter가 `tools.secret_scanner.COMPILED_PATTERNS` import | 즉시 single source, 변경 0 | **src(런타임) → tools(개발도구) 역방향 의존** (아키텍처 부적절, .importlinter root=src 밖이라 미차단이나 nonidiomatic) |
    75	| (ii) ⭐ catalog 공유 모듈 추출 | Tier-1 catalog를 `src/adapters/llm/redaction_patterns.py` (또는 공유 위치) 추출, secret_scanner + RedactionFilter 공유 | single source + 런타임 정합 | **secret_scanner 변경 = R-4.1 "변경 0건" 위반 = R-7(b) 차등 자격** (별도 평가) |
    76	| (iii) RedactionFilter 자체 복제 | Tier-1 45 패턴 복사 | 경계 깔끔 | **중복 → detection↔prevention drift 위험** (single source 위반) |
    77	| (iv) §8.2 자체 패턴 | RedactionFilter = §8.2 4 패턴 + 6 키 | 설계 명세 직접 답습 | Tier-1 45 catalog 미사용 (R-2-c 비채택, 커버리지 ↓) |
    78	
    79	⭐ **결정 = (ii) 공유 모듈 추출** (B-1 흡수, 4 source 3:1 majority + codex BLOCKING). **Reviewer verify**: (i) `from tools.secret_scanner import` = namespace package 동작하나 (pyproject 부재 run-from-source), **src(런타임)→tools(개발도구 PoC) 의존 방향 nonidiomatic** (.importlinter root=src 미제어 = "미차단 ≠ 승인").
    80	
    81	**(ii) 구체화**: Tier-1 catalog literal을 **src 하위 공유 모듈** (`src/adapters/llm/redaction_patterns.py`)로 추출 → `RedactionFilter`(src) + `secret_scanner`(tools) 둘 다 import (**tools→src = 도구가 런타임 참조 = 정방향**). **secret_scanner 패턴 *내용* 변경 0건** (id/src/cat/vendor/regex 동일, R-4.1 충실) + **equivalence test 필수** (`len(ALL_PATTERNS)==45` + pattern snapshot 동일 + scan-source/scan-log pass/fail fixture 유지). secret_scanner 구조 변경 (literal 정의 → import)은 패턴 내용 0이므로 **detection 동작 불변** (R-7(b) = 패턴 *내용* 변경 아님).
    82	
    83	### §2.2 RedactionFilter 인터페이스 (§8.2 답습)
    84	
    85	```
    86	class RedactionFilter:
    87	    """LLM 송신/응답/로그에서 비밀값 자동 strip (GP-2 prevention)."""
    88	    def redact_text(self, text: str) -> str: ...          # str 패턴 매칭 → secret 값만 마스킹
    89	    def redact_messages(self, messages: list[dict]) -> list[dict]: ...  # 송신 request body redaction (GP-2 핵심)
    90	    def scrub(self, obj) -> ...: ...                       # dict/str 재귀 (응답/메트릭/로그, §8.2 + KEY_BLACKLIST)
    91	```
    92	
    93	- 패턴 source = `src/adapters/llm/redaction_patterns.py` 공유 모듈 (Tier-1 45 catalog, §2.1 (ii)).
    94	- ⭐ **B-2 흡수 — group-aware 치환 (값만 마스킹, 구조 보존)**: secret_scanner 패턴 = *검출*용 (prefix `key=` 포함 매칭 / regex group / alternation). **whole-match `[REDACTED]` 치환 시 key명·JSON 구조 소거 + word-joining artifact** (3 Agent 실증). → redaction = **매칭된 secret *값* 부분만** 마스킹 (key명/구조 보존). detection 패턴 ≠ redaction 치환 — 값 추출/group 분리 로직 별도 (R-6: `sk-***last4` 부분 마스킹 평가, 또는 `[REDACTED]` 값 한정).
    95	- ⭐ **R-3 흡수 — `scrub()` KEY_BLACKLIST**: §8.2 `KEY_BLACKLIST` (api_key/token/secret/auth/credential/authorization) dict key 기반 redaction 구현 (Tier-1 regex만으론 key 기반 누락).
    96	- **frozen / 순수 함수** (Layer 1 자가진화 패턴 답습, 부작용 0 — R-1 불변성).
    97	
    98	---
    99	
   100	## §3 송신 redaction 역할 명세 (GP-2 prevention)
   101	
   102	⭐ **핵심 = 송신 경로 (request body) redaction** (권위 = governance §4.1 line 422 verbatim "LLM API request body 에 secret 노출 차단" + 64 trajectory §3, B-3 정정):
   103	- `complete(req)` 흐름에서 **Router 위임 *전*** request 입력을 `redact_messages()` 통과 → secret strip 후 송신.
   104	- ⭐ **B-4 흡수 — 범위 명시**: 본 cycle 최소 = **`req.messages` + `req.metadata`** redaction (현 placeholder `LLMRequest(alias, messages, metadata)` 기준 — `system` 필드 없음). 설계 §4.1 full fields (`system`/`tools`/`tool_choice`/`response_format`/`stop_sequences`/`metadata_in`)는 **Router 위임 sub-cycle과 함께 deferred** (시그니처 전면 개편 deferred 명시).
   105	- ⭐ **R-5 흡수 — content list/structured 재귀**: OpenAI-compatible message content가 `str` 외 `list[dict]`(multimodal/tool) 가능 → `scrub()` 기반 재귀 처리 (str 단독 가정 회피).
   106	- §4.4 호출 흐름 step 5 "메트릭 기록 (redaction 적용)" = 응답/로그 redaction (`scrub`).
   107	- **GP-2 prevention 핵심 = 송신 (request body)**. 응답/로그 redaction = 보조 (§8.2 scrub).
   108	
   109	⚠️ **redaction 의미 명확화**: GP-2 = "secret이 *실수로* LLM request body에 포함되는 것 차단" (예: 메시지에 API key 평문 노출). 정상 대화 내용 손상 아님 — Tier-1 catalog는 secret 패턴 (sk-/Bearer/api_key 등) 한정 매칭.
   110	
   111	---
   112	
   113	## §4 facade 통합 지점 + Router deferred (RT-1 window 회피)
   114	
   115	### §4.1 통합 설계 (현 placeholder → redaction layer real)
   116	
   117	현 `facade.py` (41 LOC placeholder):
   118	- `LLMFacade.__init__(registry_path)` → RedactionFilter 인스턴스 추가 (`self._redactor = RedactionFilter(...)`)
   119	- `complete(req)` → **redaction 적용 후 Router deferred**:
   120	  1. `redacted = self._redactor.redact_messages(req.messages)` (송신 전 redaction — GP-2 prevention operative)
   121	  2. Router 위임 = **deferred** → `raise NotImplementedError("LiteLLM Router 위임 = Provider Liquidity sub-cycle deferred")` (redaction *후* 명시적 deferred)
   122	
   123	### §4.2 RT-1 window 회피
   124	
   125	- 64 brief RT-1 = "facade real 후 RedactionFilter 미부착 window 금지 (atomic)".
   126	- 본 cycle: **Router deferred = 실제 LLM 송신 0 = redaction 미부착 window 없음** (송신 자체가 deferred). RedactionFilter는 complete() 진입 시 부착 → Router 발효 (SC-Provider Liquidity) 시점에 이미 redaction layer 존재 (선부착).
   127	- ⭐ **선부착 보장**: SC-Provider Liquidity (Router 위임)가 본 SC-1 (redaction layer) *후* 진입 → Router 발효 시 redaction 이미 operative (window 0).
   128	
   129	### §4.3 시그니처 정합 (설계 §4.1 vs 현 placeholder)
   130	
   131	- 현 placeholder: `LLMRequest(alias, messages, metadata)`. 설계 §4.1: `LLMRequest(messages, model_alias, system, ...)`.
   132	- 본 cycle = **redaction 통합 최소 변경** — 시그니처 전면 개편 (설계 §4.1 full)은 Router 위임 sub-cycle과 함께 (deferred). 현 placeholder 시그니처 기반 redaction layer 추가 (over-engineering 회피).
   133	
   134	---
   135	
   136	## §5 TDD 계획 (RED → GREEN → REFACTOR)
   137	
   138	### §5.1 RED (실패 test 먼저)
   139	
   140	`tests/adapters/llm/test_redaction_filter.py` (신규):
   141	- T-1: `redact_text("sk-ant-..." secret)` → secret 값 마스킹 (group-aware, key명 보존)
   142	- T-2: `redact_messages([{role, content: "key=sk-..."}])` → content secret 값 redacted (key 구조 보존)
   143	- T-3: Tier-1 45 catalog 대표 패턴 (baseline + prefix + regex + alternation 각 1+) redaction 검증
   144	- T-4 ⭐ (R-2): false positive **edge case fixture** — 정상 내용 (`sort(key=...)`, `keyboard`, `monkeypatch`, 일반 URL query) → 무변경 (secret_scanner line 157-158 `sort(key=)` 회피 의도 답습)
   145	- T-5: `scrub(dict)` 재귀 (nested) + **KEY_BLACKLIST** (R-3) redaction + **dict 구조 무결성** (B-2 — key명/구조 보존 검증)
   146	- T-6 ⭐ (R-4): facade `complete()` — **spy/fake redactor 주입**으로 redaction *선행* 검증 (Router deferred NotImplementedError 전 redaction 호출 입증, 단순 NotImplementedError 확인만으론 순서 미입증)
   147	- T-7 ⭐ (R-1): **원본 불변성** — `redact_messages()` 입력 list/dict in-place mutate 0 (재시도/로그 부작용 차단)
   148	- T-8 (B-1): **equivalence test** — `src/adapters/llm/redaction_patterns.py` 추출 후 `len(ALL_PATTERNS)==45` + pattern snapshot 동일 + secret_scanner scan-source/scan-log 동작 불변
   149	
   150	### §5.2 GREEN (최소 구현)
   151	
   152	- `src/adapters/llm/redaction_patterns.py` (Tier-1 45 catalog 공유 모듈 추출, §2.1 (ii)) + `secret_scanner.py` import 전환 (패턴 내용 0 변경)
   153	- `src/adapters/llm/redaction.py` (RedactionFilter — redact_text/redact_messages/scrub, group-aware 치환 + KEY_BLACKLIST)
   154	- `facade.py` complete() redaction 통합 (messages + metadata, Router deferred)
   155	
   156	### §5.3 REFACTOR
   157	
   158	- frozen / 순수 함수 정리 + test 유지 green
   159	- **커버리지 목표 70%+** (CLAUDE.md §1)
   160	
   161	### §5.4 verify (구현 후)
   162	
   163	- pytest (신규 redaction test + 기존 회귀 0)
   164	- import-linter (LLM SDK 경계 보존 — litellm import 0, Router deferred)
   165	- secret_scanner scan-source (src + .github, violations 0)
   166	- jarvis pytest 회귀 0
   167	
   168	---
   169	
   170	## §6 합의 형태 + 승격 트리거
   171	
   172	### §6.1 합의 형태 = 풀 3+1 + 외부 LLM 1+ (TR-1)
   173	
   174	**정당화**: facade.py 헤더 명시 TR-1 (real 본문 작성 풀 3+1 trigger) + GP-2 prevention 보안 영역 (CLAUDE.md §3 보안 = 풀 3+1 필수) + 실 코드 + Provider Liquidity 직결.
   175	
   176	### §6.2 승격 트리거
   177	
   178	| # | trigger | 발화 |
   179	|---|---------|----|
   180	| 1 | TR-1 (facade real 본문) | ✅ |
   181	| 2 | 보안 관련 변경 (GP-2 prevention) | ✅ |
   182	| 3 | 실 코드 (런타임 redaction) | ✅ |
   183	| 4 | Provider Liquidity 영향 (facade 단일 진입점) | ✅ |
   184	| 5 | 외부 LLM cross-vendor (5조-2) | ✅ |
   185	
   186	→ **5/5 발화 → 풀 3+1 + 외부 LLM 1+ 의무**.
   187	
   188	### §6.3 합의 시점
   189	
   190	본 brief = **구현 *전* 설계 승인** (SDD "문서 검토 완료 후 코드 구현" 답습). 합의 APPROVE 후 TDD 구현 (§5).
   191	
   192	---
   193	
   194	## §7 Provider Liquidity 보존 (ADR-009 §2.2, 5조-2 비협상)
   195	
   196	- LiteLLM 직접 import = facade.py 한정 (Router deferred이므로 본 cycle litellm import 0 — import-linter 보존).
   197	- RedactionFilter = facade 내부 협력자 (provider-agnostic, 모델명 분기 0).
   198	- facade 단일 진입점 의무 보존 ([[feedback_provider_liquidity]]).
   199	
   200	---
   201	
   202	## §8 금지 사항
   203	
   204	§0.2 답습 (10). 추가: LiteLLM 설치 0 / Router 위임 구현 0 / secret_scanner 패턴 변경 0 / litellm import 0 / full facade real 표현 0 / full GP-2 PASS 발효 0 / 자동 SC-2/SC-3 진입 0.
   205	
   206	---
   207	
   208	## §9 Rollback Trigger
   209	
   210	| # | trigger | 대응 |
   211	|---|---------|----|
   212	| RT-1 | Router 발효가 redaction layer *전* 진입 (window) | SC-Provider Liquidity는 본 SC-1 후 진입 (선부착 §4.2) |
   213	| RT-2 | catalog 재사용 (i) src→tools 의존 방향 BLOCKING | (ii) 공유 모듈 추출 fallback (R-7(b) 차등) |
   214	| RT-3 | redaction false positive (정상 내용 손상) | Tier-1 catalog = secret 패턴 한정 + T-4 test |
   215	| RT-4 | base64 evasion (Tier-1 미커버) | known limitation 명문 (R-5 영구 분리) |
   216	| RT-5 | redaction 성능 (매 송신 45 패턴 매칭) | COMPILED_PATTERNS 재사용 (사전 compile) |
   217	
   218	---
   219	
   220	## §10 Evidence
   221	
   222	- E-1: redaction test green (T-1~T-6) + 커버리지 70%+
   223	- E-2: facade complete() redaction 적용 + Router deferred 순서 검증
   224	- E-3: import-linter green (litellm import 0, 경계 보존)
   225	- E-4: secret_scanner scan-source violations 0
   226	- E-5: jarvis pytest 회귀 0
   227	
   228	---
   229	
   230	## §11 자기진단 (메타 편향 회피)
   231	
   232	| # | 위험 | 처리 |
   233	|---|------|----|
   234	| P-1 | "facade real 완성" over-claim | §0 명칭 정직성 — facade *redaction layer* real, Router deferred ([[feedback_pass_scope_overclaim]]) |
   235	| P-2 | full GP-2 PASS 기정사실화 | full GP-2 PASS = SC-2 (R-1) + SC-3 후 (§0.2 #3) |
   236	| P-3 | catalog 재사용 import 경계 임의 결정 | §2.1 4 옵션 풀 3+1 검증 (권고 (i), fallback (ii)) |
   237	| P-4 | secret_scanner 변경 (R-4.1 위반) | §0.2 #5 — 패턴 변경 0 (재사용만) |
   238	| P-5 | 송신 redaction 정상 내용 손상 | §3 — Tier-1 secret 패턴 한정 + T-4 false positive test |
   239	| P-6 | RT-1 window | §4.2 선부착 보장 (Router deferred = 송신 0) |
   240	| P-7 | 작성자 = 64 작성자 (Claude) cascade | cross-vendor codex + 풀 3+1 독립 검증 |
   241	
   242	---
   243	
   244	## §12 v1.1 흡수 매트릭스 (BLOCKING 4 + 권고 6 1pass)
   245	
   246	본 v1.1 = `docs/review/3plus1-consensus-2026-05-28-mvp2-sc1.md` 답습 1pass 흡수 (별도 v2 cycle 0). **4 source 전원 APPROVE WITH CONDITIONS** (codex BLOCKING 2 + Agent A 2 + Agent B 3 + Agent C 2). 방향 견고, 구현 *방식* 정정.
   247	
   248	| # | 흡수 | source | 정정 위치 |
   249	|---|------|--------|------|
   250	| B-1 ⭐ | catalog 재사용 (i) src→tools import → **(ii) 공유 모듈 추출** (src 하위 + tools import + 패턴 내용 0 + equivalence test) | codex + Agent B + Agent C (3:1, Reviewer verify) | §2.1 + §5.2 |
   251	| B-2 ⭐ | `[REDACTED]` whole-match → **group-aware 치환** (값만 마스킹, key/구조 보존, secret_scanner = 검출 전용) | Agent A + Agent B + Agent C | §2.2 + §5.1 T-5 |
   252	| B-3 | 송신 redaction 권위 = **governance §4.1 + 64 trajectory** (§8.2 = egress 보조) | codex + Agent B | §0.3 + §3 |
   253	| B-4 | redaction 범위 = **messages + metadata** (full fields system/tools/... deferred) | codex | §3 |
   254	| R-1 | 원본 불변성 test (in-place mutate 0) | codex 1 | §5.1 T-7 |
   255	| R-2 | T-4 false positive edge case fixture | codex 2 + Agent A | §5.1 T-4 |
   256	| R-3 | scrub() KEY_BLACKLIST | codex 3 | §2.2 |
   257	| R-4 | T-6 spy/fake redactor (redaction 선행 입증) | codex 4 | §5.1 T-6 |
   258	| R-5 | redact_messages content list/structured 재귀 | codex 5 | §3 |
   259	| R-6 | group-aware 값 마스킹 (B-2 연계) | Agent C | §2.2 |
   260	
   261	**4 source 정합 (positive)**: 명칭 정직성 양호 (facade redaction layer real, full facade real / full GP-2 PASS 아님 — over-claim 0) / RT-1 window 회피 타당 (Router deferred) / Provider Liquidity 보존 (litellm import 0) / 권위 인용 일치 (codex 6/7, §8.2 부분 확장만). pytest 152 green (Agent A 실측) + redaction 성능 ~2.1ms/request.
   262	
   263	---
   264	
   265	**본 brief v1.1 끝.**
   266	
   267	**다음 단계**: **TDD 구현 (RED→GREEN→REFACTOR, catalog (ii) 공유 모듈 + group-aware 치환)** → verify (pytest + import-linter + secret_scanner equivalence + jarvis 회귀) → commit + push → **R-2 facade RedactionFilter prevention layer in-repo operative**. 후속: SC-2 (R-1 위임 검증) / SC-3 (full GP-2 PASS 발효) / SC-Provider Liquidity (Router 위임) = 사용자 명시 별도 sub-cycle.

exec
/bin/bash -lc "nl -ba src/adapters/llm/redaction.py | sed -n '1,260p' && nl -ba tests/adapters/llm/test_redaction_filter.py | sed -n '1,260p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
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

codex
R-2 실재성은 코드와 테스트로 확인됐고, 테스트 함수 수가 아니라 parametrized case 기준 15건입니다. 최종 판정 전에 SC-3의 “충족” 표현이 조건부를 충분히 붙였는지 기준별로 정리합니다.
exec
/bin/bash -lc "nl -ba src/adapters/llm/redaction_patterns.py | sed -n '1,260p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
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
/bin/bash -lc 'pytest -q tests/adapters/llm/test_redaction_filter.py' in /home/delangi/문서/project/category/AI_development_tool
 exited 127 in 0ms:
/bin/bash: line 1: pytest: command not found

exec
/bin/bash -lc "nl -ba docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md | sed -n '1,120p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# MVP-2 Implementation Evidence PASS (G4 ledger 완전 + GP-2 detection-tier, prevention/Layer 3·5/2a deferred) 발효 합의 entry brief (v1.1)
     2	
     3	> **작성**: 2026-05-28 (62번째 entry 진입 cycle — 신규 세션 #2)
     4	>
     5	> **v1 → v1.1 갱신**: 풀 3+1 + 외부 LLM 1+ (codex gpt-5.5 cross-vendor) 통합 합의 (`docs/review/3plus1-consensus-2026-05-28-mvp2-final-pass.md`) **APPROVE WITH CONDITIONS (4 source 전원) → BLOCKING 3 + 권고 3 1pass 흡수**. ⭐ **핵심 정정 (B-1)**: 무수식 "MVP-2 PASS" 명칭 → **복합 자격 부착** (G4 ledger 완전 + GP-2 detection-tier, prevention R-1/R-2 + Layer 3·5 + 2a deferred) — 60 GP-2 detection-layer 강등 cascade 상위 재발 방지 (β B-1 / 59 B-2 / 60 B-1 4번째). B-2 "trajectory" 진행성 완화 + B-3 citation 정정. evidence 차단급 over-claim 0. §10 흡수 매트릭스 추가.
     6	>
     7	> **scope**: MVP-2 Implementation Evidence PASS **발효** (G4 ledger 무결성 *완전* + GP-2 송신 redaction *detection-tier*, prevention/Layer 3·5/2a *deferred*) — MVP-2 영역 (G2 GP-2 + G4 §4.4 Layer 1+2+4) 최종 milestone. ⚠️ **full GP-2 PASS (prevention) 아님**
     8	>
     9	> **본 cycle = 큰 cycle / 최종 milestone** (32 MVP-1 Implementation Evidence PASS 발효 답습 동형, 풀 3+1 + 외부 LLM 1+ + 사용자 명시 의무)
    10	>
    11	> **본 cycle 발효 자격** = 3 의존성 충족 (Layer 통합 PASS + GP-2 detection-layer PASS + R-S1) + 풀 3+1 + 외부 LLM 1+ APPROVE + 사용자 명시
    12	>
    13	> **본 cycle 발효 효과** = **MVP-2 Implementation Evidence PASS 발효** (in-repo governance/CI 구현 evidence). **full GP-2 prevention (R-1 Hermes runtime redaction / R-2 facade real) + Layer 3+5 = MVP-2 PASS 후속 trajectory (deferred, 자동 진입 0)**
    14	>
    15	> **선행 답습 (3 의존성 모두 발효)**: 59 Layer 1+2+4 통합 PASS (`0f49eb9`) + 60 GP-2 detection-layer PASS (`92e9078`) + 61 R-S1 정정 (`bb59342`)
    16	
    17	---
    18	
    19	## §0 본 brief 의 범위
    20	
    21	### §0.1 본 brief 가 *하는* 것
    22	
    23	1. **3 의존성 충족 audit** (Layer 통합 PASS + GP-2 detection-layer PASS + R-S1) (§1)
    24	2. **MVP-2 영역 ADR-011 §2.1 (a)~(d) 모법 + (e2) ADR-012 §4 확장 통합 매핑** (59 B-2 framing 답습) (§2)
    25	3. **MVP-2 PASS scope 정직 명문** — Implementation Evidence PASS (in-repo evidence) + full GP-2 prevention + Layer 3+5 = deferred trajectory (60 over-claim 교훈 답습) (§3)
    26	4. **합의 형태 + 승격 트리거** (§4)
    27	5. **PASS 발효 권고 + 조건 + 발효 시 효과 (roadmap/governance 등록 — 사용자 명시 후)** (§5)
    28	6. 금지 / 다음 단계 / cross-ref / 자기진단 (§6~§9)
    29	
    30	### §0.2 본 brief 가 *하지 않는* 것
    31	
    32	| # | 영역 | 위반 |
    33	|---|------|----|
    34	| 1 | MVP-2 PASS *발효* 자체 (본 brief = 합의 입력, 발효 = 합의 APPROVE + 사용자 명시 후) | 0 |
    35	| 2 | **full GP-2 PASS 발효** (prevention R-1/R-2 = deferred trajectory) | 0 |
    36	| 3 | Layer 3 (Signed commit) + Layer 5 (External anchor) PASS 발효 | 0 ("부분 답습" 영구) |
    37	| 4 | R-1 Hermes import / R-2 facade real (TR-1) | 0 |
    38	| 5 | Layer 통합 PASS / GP-2 detection-layer PASS / R-S1 재선언 | 0 (59/60/61 답습) |
    39	| 6 | MVP-1 PASS 재선언 (32 답습) | 0 |
    40	| 7 | MVP-3~6 영역 진입 | 0 |
    41	| 8 | Operational Readiness PASS / Hermes PMO 격상 | 0 |
    42	| 9 | ADR / 헌법 / ADR-012 본문 갱신 (roadmap MVP-2 PASS 등록 = 발효 후 §5) | 0 |
    43	| 10 | 신규 외부 library / Tier-2/3 catalog 확장 | 0 |
    44	| 11 | 자동 후속 cycle 진입 | 0 (사용자 명시) |
    45	| 12 | 본 brief 자체 영구화 / 권위 chain 등재 | 0 |
    46	
    47	### §0.3 권위 답습 source
    48	
    49	- **ADR-011 §2.1 (a)~(d) 4조건 모법** + **ADR-012 §4 (a)~(d)+(e) 확장** (PASS 발효 권위) — `docs/decisions/`
    50	- **59 Layer 1+2+4 통합 PASS 발효 brief v1.1 + 합의** (`0f49eb9`) — `docs/phase0/mvp2-layer-124-pass-activation-brief.md`
    51	- **60 GP-2 detection-layer PASS 발효 brief v1.1 + 합의** (`92e9078`) — `docs/phase0/mvp2-gp2-pass-activation-brief.md`
    52	- **61 R-S1 cross-reference 정정** (`bb59342`) — `docs/decisions/ADR-012-evidence-ledger-protection.md` §2.3 + §2.8 note
    53	- **32 MVP-1 Implementation Evidence PASS 발효 합의** (최종 milestone 패턴 답습) — `docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md`
    54	- **implementation-runtime-roadmap-mvp1.md §1.3** (GP-2 = MVP-2 분리) + **`3plus1-consensus-2026-05-07-g2-g3-g4-gate-adoption.md §C-7`** (line 378~379, GP-2 = MVP-2 우선순위 1 — B-3 정정: roadmap.md 아님)
    55	
    56	---
    57	
    58	## §1 3 의존성 충족 audit
    59	
    60	| 의존성 | 발효 | commit | scope |
    61	|--------|------|--------|------|
    62	| **G4 §4.4 Layer 1+2+4 통합 PASS** | ✅ 59 entry (APPROVE WITH CONDITIONS, 4 source) | `0f49eb9` | Layer 1 완전 + Layer 2 (2b operative + rewrite-defense CI 이중 cover, 2a DEFER no-op) + Layer 4 (3 ledger workflow green + canonical/timestamp BLOCK). "부분 답습" (Layer 3+5 scope 외) |
    63	| **GP-2 detection-layer PASS** | ✅ 60 entry (REVISE → v1.1 detection-layer reframe, 4 source) | `92e9078` | R-3 detection operative (secret-hygiene D-2 CI green) + R-4 설계 동등성 + ADR 권위. **prevention (R-1 Hermes / R-2 facade) = deferred trajectory (in-repo 입증 0, Hermes upstream 위임)** |
    64	| **R-S1 cross-reference 정정** | ✅ 61 entry (Reviewer-only 단축 APPROVE) | `bb59342` | ADR-012 §2.3/§2.8 canonical numbering 선언 (§2.8/G4 §4.4.1 5-layer = canonical). MVP-2 "Layer 1+2+4" = 5-layer 기준 확정 |
    65	
    66	→ **3 의존성 모두 발효** — MVP-2 Implementation Evidence PASS 발효 자격 충족 ((e2) = 본 cycle).
    67	
    68	---
    69	
    70	## §2 MVP-2 영역 ADR-011 §2.1 (a)~(d) + (e2) 통합 매핑 (59 B-2 framing 답습)
    71	
    72	> ⚠️ 59 B-2 답습: ADR-011 §2.1 = (a)~(d) 모법, "(e2) 합의 APPROVE" = ADR-012 §4 확장 + 프로젝트 내부 label.
    73	
    74	| 조건 | G4 §4.4 Layer 1+2+4 | G2 GP-2 (detection-layer) | MVP-2 통합 |
    75	|------|------|------|----|
    76	| (a) 동등 이상 보안 결과 | ✅ ledger 무결성 (hash chain + append-only + CI 회귀) | ⚠️ detection ✅ / prevention (R-1/R-2) deferred (60 답습) | ✅ ledger 완전 + GP-2 detection (prevention deferred 명문) |
    77	| (b) 격리 PoC | ✅ 59 (jsonl_hash_chain + fixtures + 3 G4 actual run) | ✅ 60 (secret-hygiene D-2 PoC) | ✅ |
    78	| (c) ADR/SDD 권위 | ✅ G4 §4.4.1 + ADR-012 §2.3/§2.8 (R-S1 정정 후 canonical 명확) | ✅ ADR-011 §2.3 #2 + governance §4 | ✅ |
    79	| (d) 자동 회귀 검증 | ✅ 3 ledger workflow CI green | ✅ secret-hygiene D-2 CI green | ✅ |
    80	| **(e2) 합의 APPROVE** | ✅ 59 | ✅ 60 (detection-layer) | ⏳ **본 cycle (MVP-2 통합 PASS)** |
    81	
    82	→ **(a)~(d) = Implementation Evidence scope 충족** (B-1 정정): G4 축 (a) = 무결성 *완전* / **GP-2 축 (a) = detection + 설계 동등성, prevention (R-1/R-2) deferred** (60 답습 — full prevention 충족 아님). (e2) = 본 cycle MVP-2 통합 PASS 합의.
    83	
    84	---
    85	
    86	## §3 MVP-2 PASS scope 정직 명문 (60 over-claim 교훈 답습)
    87	
    88	⭐ **MVP-2 Implementation Evidence PASS = in-repo governance/CI 구현 evidence PASS** (MVP-1 PASS 32 동형 — "Implementation Evidence" = 구현 evidence, runtime 보증 아님).
    89	
    90	**발효 범위 (operative in-repo)**:
    91	- ✅ G4 ledger 무결성: Layer 1 (hash chain) + Layer 2 (2b branch protection + rewrite-defense CI) + Layer 4 (CI 회귀 검증) operative green
    92	- ✅ GP-2 송신 redaction **detection**: secret-hygiene D-2 CI (redaction residual 검출) operative green
    93	
    94	**deferred (명문, 자동 진입 0)** — ⚠️ B-2: "trajectory" 진행성 함의 회피 (R-1 = import 결정조차 미진입, R-2 = placeholder):
    95	- ⚠️ **GP-2 prevention (능동 redaction)**: R-1 Hermes runtime redaction (upstream 위임, ADR-011 §2.3 #2) + R-2 facade real (TR-1) — **in-repo 입증 0 + Hermes safety 미선언** (ADR-011 §7.3 / ADR-012 §3.3 답습 — redaction-pattern-equivalence = 설계 동등성, 안전 선언 아님). R-1 import 미결정 / R-2 placeholder. **full GP-2 PASS = MVP-2 PASS 후속 (deferred)**
    96	- ⚠️ **Layer 2a denyNonFastForwards**: non-bare clone no-op (2b + rewrite-defense CI 이중 cover), 실 bare/server 배포 시점
    97	- ⚠️ **Layer 3 (Signed commit) + Layer 5 (External anchor)**: "부분 답습" scope 외 (RECOMMENDED MVP, MANDATORY multi-host)
    98	- ⚠️ **R-5 base64 evasion**: known limitation (G3-4 MVP-2/3 분리)
    99	
   100	→ **MVP-2 PASS = ledger 무결성 완전 + GP-2 detection operative + 설계/CI 권위. prevention runtime + Layer 3/5 + denyNonFastForwards = solo 1-host 비례 보안 + upstream 위임 deferred (over-claim 0, 정직 scope)**.
   101	
   102	---
   103	
   104	## §4 합의 형태 + 승격 트리거
   105	
   106	### §4.1 합의 형태 = 풀 3+1 + 외부 LLM 1+ (의무)
   107	
   108	**정당화**: MVP-2 최종 milestone (32 MVP-1 PASS 발효 답습) + 큰 결정 (ADR-011 §2.4 T3) + 헌법 5조-2 cross-vendor + 사용자 명시 (32 답습).
   109	
   110	### §4.2 7 승격 트리거
   111	
   112	| # | trigger | 발화 |
   113	|---|---------|----|
   114	| 1 | 큰 결정 (MVP-2 최종 PASS milestone) | ✅ |
   115	| 2 | 아키텍처/SDD 본문 변경 | ❌ (brief = phase0 신규 1, roadmap 등록 = 발효 후) |
   116	| 3 | ADR 본문 변경 | ❌ (R-S1 = 61 완료) |
   117	| 4 | 권위 chain 다중 source 손상 | ❌ (R-S1 해소) |
   118	| 5 | 외부 LLM 통합 필요 | ✅ cross-vendor 의무 |
   119	| 6 | Tier-2/3 확장 | ❌ |
   120	| 7 | Hermes PMO 격상 | ❌ |

exec
/bin/bash -lc 'python -m pytest -q tests/adapters/llm/test_redaction_filter.py' in /home/delangi/문서/project/category/AI_development_tool
 exited 127 in 0ms:
/bin/bash: line 1: python: command not found

exec
/bin/bash -lc 'python3 -m pytest -q tests/adapters/llm/test_redaction_filter.py' in /home/delangi/문서/project/category/AI_development_tool
 exited 1 in 0ms:
/usr/bin/python3: No module named pytest

codex
1. **판정: APPROVE WITH CONDITIONS**

SC-3 brief는 “GP-2 full PASS”를 무수식 완전 보증으로 쓰지 않고, 대부분의 핵심 위치에서 R-1 조건부와 deferred를 명시합니다. 다만 `full` 명칭은 여전히 오독 위험이 높으므로, 발효/commit/ledger/INDEX 등 모든 후속 표기에서 반드시 parenthetical qualification을 붙이는 조건부 승인입니다.

2. **BLOCKING 항목**

없음.

단, 아래 조건을 어기면 BLOCKING으로 격상해야 합니다.

1. `GP-2 full PASS` 단독 표기 금지. SC-3는 title부터 “R-1 조건부 위임, 실 canary/R-6 Hermes trigger deferred”를 붙이고 있음: [mvp2-sc3-full-gp2-pass-activation-brief.md:1](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-sc3-full-gp2-pass-activation-brief.md:1)
2. `Exit (a) 충족`은 항상 `R-1 조건부`를 함께 붙여야 함. 현재 §2는 R-1을 `⚠️ 조건부`로 표기하면서 통합 판정을 “R-2 강 + R-1 조건부”로 한정함: [mvp2-sc3-full-gp2-pass-activation-brief.md:69](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-sc3-full-gp2-pass-activation-brief.md:69)
3. R-1 실 canary/R-6 Hermes lock trigger/HERMES_REDACT_SECRETS 활성화 검증이 완료된 것처럼 쓰면 안 됨. SC-3 §4는 이를 deferred로 명시함: [mvp2-sc3-full-gp2-pass-activation-brief.md:99](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-sc3-full-gp2-pass-activation-brief.md:99)

3. **권고 항목**

1. `GP-2 full PASS`보다 `GP-2 prevention PASS (R-2 operative + R-1 conditional delegation)` 또는 `GP-2 full-scope PASS, R-1 conditional`가 더 정직합니다.
2. SC-3 line 13, 75, 107, 115의 “충족” 표현은 모두 “조건부 충족” 또는 “qualified satisfaction”으로 고정 권고합니다. 특히 line 13의 “R-1 ∧ R-2 검증 충족”은 괄호 안에 `R-1 conditional/document-based`를 즉시 붙이는 편이 안전합니다.
3. §2 matrix의 (b), (d) 통합 판정은 `✅ in-repo 충족 / R-1 deferred` 구조라 적절하나, “(a)~(d) prevention 검증 충족” 문장은 “R-2 operative + R-1 conditional basis”로 완화 권고합니다: [mvp2-sc3-full-gp2-pass-activation-brief.md:75](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-sc3-full-gp2-pass-activation-brief.md:75)
4. 후속 MVP-2 문서 갱신 시 “MVP-2 PASS 재선언”이 아니라 cross-reference 갱신/chore로만 처리해야 합니다. SC-3도 이를 금지함: [mvp2-sc3-full-gp2-pass-activation-brief.md:120](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-sc3-full-gp2-pass-activation-brief.md:120)

4. **NOTE**

R-2 evidence는 실재합니다. `RedactionFilter`는 Tier-1 catalog 공유 모듈을 import하고 group-aware redaction을 수행합니다: [redaction.py:18](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/redaction.py:18), [redaction.py:31](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/redaction.py:31). 테스트도 parametrized case 기준 15건 구조입니다: T-3 4 cases [test_redaction_filter.py:40](/home/delangi/문서/project/category/AI_development_tool/tests/adapters/llm/test_redaction_filter.py:40), T-4 5 cases [test_redaction_filter.py:59](/home/delangi/문서/project/category/AI_development_tool/tests/adapters/llm/test_redaction_filter.py:59), 기타 T-1/T-2/T-5~T-8.

테스트 실행은 환경에 `pytest`가 없어 직접 수행하지 못했습니다 (`python3 -m pytest`: `No module named pytest`).

5. **명칭 독립 판단**

`GP-2 full PASS`는 단독으로는 부적절합니다. 다만 SC-3처럼 “detection + prevention R-2 operative + R-1 조건부/문서 기반 위임, 실 canary/R-6 trigger deferred”를 title과 발효 문구에 계속 붙이면 조건부 허용 가능합니다.

더 정직한 명칭은 다음입니다.

`GP-2 prevention PASS (R-2 in-repo operative + R-1 conditional delegation; canary/R-6 Hermes trigger deferred)`

6. **권위 인용 cross-verify 매트릭스**

| SC-3 인용/주장 | 실제 문서 대조 | 판정 |
|---|---|---|
| governance §4.5 (a) = Hermes native + facade filter | 실제 Exit (a): “Hermes native redaction Tier-1 42 catalog 적용 검증 + P1 facade redaction filter 검증” [governance-preconditions.md:451](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/governance-preconditions.md:451) | 일치 |
| 60 = detection-layer PASS, prevention deferred | 60은 “full GP-2 PASS = prevention 선행” 및 R-1/R-2 deferred 명시 [mvp2-gp2-pass-activation-brief.md:105](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-gp2-pass-activation-brief.md:105) | 일치 |
| 65 = R-2 facade RedactionFilter operative | 65는 “R-2 facade RedactionFilter prevention layer in-repo operative” 효과 명시 [mvp2-sc1-facade-redaction-implementation-brief.md:13](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:13) | 일치 |
| 66 = R-1 조건부/문서 기반 | 66은 “조건부/문서 기반 충족”, 활성화 전제/R-6 한정/실 canary deferred 명시 [mvp2-sc2-r1-hermes-delegation-verification-brief.md:141](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:141) | 일치 |
| ADR-011 = Hermes 안전성 선언 금지 | ADR-011 §7.3: “본 ADR은 Hermes 안전성을 선언하지 않는다” [ADR-011-means-vs-ends-redaction.md:237](/home/delangi/문서/project/category/AI_development_tool/docs/decisions/ADR-011-means-vs-ends-redaction.md:237) | 일치 |
| MVP-2 PASS 재선언 0 | SC-3가 “MVP-2 PASS (62) 재선언 0” 명시 [mvp2-sc3-full-gp2-pass-activation-brief.md:35](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-sc3-full-gp2-pass-activation-brief.md:35); 62도 full GP-2 아님을 명시 [mvp2-implementation-evidence-pass-activation-brief.md:7](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:7) | 일치 |

최종 판단: **APPROVE WITH CONDITIONS**. `full` 명칭은 qualified parenthetical 없이는 over-claim입니다. 현재 brief v1은 그 위험을 대부분 통제하지만, 후속 발효 문구에서 조건부 수식을 절대 탈락시키면 안 됩니다.
tokens used
87,358
1. **판정: APPROVE WITH CONDITIONS**

SC-3 brief는 “GP-2 full PASS”를 무수식 완전 보증으로 쓰지 않고, 대부분의 핵심 위치에서 R-1 조건부와 deferred를 명시합니다. 다만 `full` 명칭은 여전히 오독 위험이 높으므로, 발효/commit/ledger/INDEX 등 모든 후속 표기에서 반드시 parenthetical qualification을 붙이는 조건부 승인입니다.

2. **BLOCKING 항목**

없음.

단, 아래 조건을 어기면 BLOCKING으로 격상해야 합니다.

1. `GP-2 full PASS` 단독 표기 금지. SC-3는 title부터 “R-1 조건부 위임, 실 canary/R-6 Hermes trigger deferred”를 붙이고 있음: [mvp2-sc3-full-gp2-pass-activation-brief.md:1](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-sc3-full-gp2-pass-activation-brief.md:1)
2. `Exit (a) 충족`은 항상 `R-1 조건부`를 함께 붙여야 함. 현재 §2는 R-1을 `⚠️ 조건부`로 표기하면서 통합 판정을 “R-2 강 + R-1 조건부”로 한정함: [mvp2-sc3-full-gp2-pass-activation-brief.md:69](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-sc3-full-gp2-pass-activation-brief.md:69)
3. R-1 실 canary/R-6 Hermes lock trigger/HERMES_REDACT_SECRETS 활성화 검증이 완료된 것처럼 쓰면 안 됨. SC-3 §4는 이를 deferred로 명시함: [mvp2-sc3-full-gp2-pass-activation-brief.md:99](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-sc3-full-gp2-pass-activation-brief.md:99)

3. **권고 항목**

1. `GP-2 full PASS`보다 `GP-2 prevention PASS (R-2 operative + R-1 conditional delegation)` 또는 `GP-2 full-scope PASS, R-1 conditional`가 더 정직합니다.
2. SC-3 line 13, 75, 107, 115의 “충족” 표현은 모두 “조건부 충족” 또는 “qualified satisfaction”으로 고정 권고합니다. 특히 line 13의 “R-1 ∧ R-2 검증 충족”은 괄호 안에 `R-1 conditional/document-based`를 즉시 붙이는 편이 안전합니다.
3. §2 matrix의 (b), (d) 통합 판정은 `✅ in-repo 충족 / R-1 deferred` 구조라 적절하나, “(a)~(d) prevention 검증 충족” 문장은 “R-2 operative + R-1 conditional basis”로 완화 권고합니다: [mvp2-sc3-full-gp2-pass-activation-brief.md:75](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-sc3-full-gp2-pass-activation-brief.md:75)
4. 후속 MVP-2 문서 갱신 시 “MVP-2 PASS 재선언”이 아니라 cross-reference 갱신/chore로만 처리해야 합니다. SC-3도 이를 금지함: [mvp2-sc3-full-gp2-pass-activation-brief.md:120](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-sc3-full-gp2-pass-activation-brief.md:120)

4. **NOTE**

R-2 evidence는 실재합니다. `RedactionFilter`는 Tier-1 catalog 공유 모듈을 import하고 group-aware redaction을 수행합니다: [redaction.py:18](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/redaction.py:18), [redaction.py:31](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/redaction.py:31). 테스트도 parametrized case 기준 15건 구조입니다: T-3 4 cases [test_redaction_filter.py:40](/home/delangi/문서/project/category/AI_development_tool/tests/adapters/llm/test_redaction_filter.py:40), T-4 5 cases [test_redaction_filter.py:59](/home/delangi/문서/project/category/AI_development_tool/tests/adapters/llm/test_redaction_filter.py:59), 기타 T-1/T-2/T-5~T-8.

테스트 실행은 환경에 `pytest`가 없어 직접 수행하지 못했습니다 (`python3 -m pytest`: `No module named pytest`).

5. **명칭 독립 판단**

`GP-2 full PASS`는 단독으로는 부적절합니다. 다만 SC-3처럼 “detection + prevention R-2 operative + R-1 조건부/문서 기반 위임, 실 canary/R-6 trigger deferred”를 title과 발효 문구에 계속 붙이면 조건부 허용 가능합니다.

더 정직한 명칭은 다음입니다.

`GP-2 prevention PASS (R-2 in-repo operative + R-1 conditional delegation; canary/R-6 Hermes trigger deferred)`

6. **권위 인용 cross-verify 매트릭스**

| SC-3 인용/주장 | 실제 문서 대조 | 판정 |
|---|---|---|
| governance §4.5 (a) = Hermes native + facade filter | 실제 Exit (a): “Hermes native redaction Tier-1 42 catalog 적용 검증 + P1 facade redaction filter 검증” [governance-preconditions.md:451](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/governance-preconditions.md:451) | 일치 |
| 60 = detection-layer PASS, prevention deferred | 60은 “full GP-2 PASS = prevention 선행” 및 R-1/R-2 deferred 명시 [mvp2-gp2-pass-activation-brief.md:105](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-gp2-pass-activation-brief.md:105) | 일치 |
| 65 = R-2 facade RedactionFilter operative | 65는 “R-2 facade RedactionFilter prevention layer in-repo operative” 효과 명시 [mvp2-sc1-facade-redaction-implementation-brief.md:13](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md:13) | 일치 |
| 66 = R-1 조건부/문서 기반 | 66은 “조건부/문서 기반 충족”, 활성화 전제/R-6 한정/실 canary deferred 명시 [mvp2-sc2-r1-hermes-delegation-verification-brief.md:141](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md:141) | 일치 |
| ADR-011 = Hermes 안전성 선언 금지 | ADR-011 §7.3: “본 ADR은 Hermes 안전성을 선언하지 않는다” [ADR-011-means-vs-ends-redaction.md:237](/home/delangi/문서/project/category/AI_development_tool/docs/decisions/ADR-011-means-vs-ends-redaction.md:237) | 일치 |
| MVP-2 PASS 재선언 0 | SC-3가 “MVP-2 PASS (62) 재선언 0” 명시 [mvp2-sc3-full-gp2-pass-activation-brief.md:35](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-sc3-full-gp2-pass-activation-brief.md:35); 62도 full GP-2 아님을 명시 [mvp2-implementation-evidence-pass-activation-brief.md:7](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md:7) | 일치 |

최종 판단: **APPROVE WITH CONDITIONS**. `full` 명칭은 qualified parenthetical 없이는 over-claim입니다. 현재 brief v1은 그 위험을 대부분 통제하지만, 후속 발효 문구에서 조건부 수식을 절대 탈락시키면 안 됩니다.
