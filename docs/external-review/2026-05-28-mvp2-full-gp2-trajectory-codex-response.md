OpenAI Codex v0.128.0 (research preview)
--------
workdir: /home/delangi/문서/project/category/AI_development_tool
model: gpt-5.5
provider: openai
approval: never
sandbox: danger-full-access
reasoning effort: none
reasoning summaries: none
session id: 019e6d7f-ff6f-7df0-8f40-1d26aaa8d7b2
--------
user
당신은 외부 LLM 검토자 (cross-vendor blind review)입니다. 응답 vendor = OpenAI (codex CLI), 본 cycle 풀 3+1 Agent vendor = Anthropic Claude. cross-vendor 충족 (헌법 5조-2).

## 본 cycle 개요

AI_development_tool 프로젝트 (SDD + TDD + 하네스 엔지니어링 + 3+1 멀티 에이전트 합의). 본 cycle = **full GP-2 PASS trajectory 진입 entry brief** (64 entry, 51 audit / 52 (α) / 55 entry brief 답습 동형 큰 cycle). 직전 세션 #2에서 MVP-2 Implementation Evidence PASS 발효 (G4 ledger 완전 + GP-2 detection-tier, prevention deferred). 본 cycle = prevention(R-1/R-2) 잔여 trajectory 진입.

본 cycle 발효 효과 (scope = "trajectory entry brief 한정", 사용자 명시):
- full GP-2 PASS trajectory 진입 자격 발효
- R-1/R-2 sub-cycle 진입 권한 발효 (조건부)
- R-1/R-2 경로 분석 + 합의 형태 권고

본 cycle 발효 *하지 않는 것*: full GP-2 PASS *발효* 0 / R-1 Hermes import *결정* 0 / R-2 facade real *구현* 0 (TR-1 미발화) / upstream PR 0 / sub-cycle 우선순위 *결정* 0 / LiteLLM 신규 도입 0 / ADR·헌법·governance 본문 변경 0 / 자동 후속 진입 0 (총 13 금지, brief §0.2).

## 검토 대상 (working directory 자료, codex 직접 read 의무 — 추측 금지)

PRIMARY:
- `docs/phase0/mvp2-full-gp2-pass-trajectory-entry-brief.md` (v1, §0~§13) ← 본 검토 핵심

권위 source (정확성 cross-verify — 직접 read하여 brief 인용이 정확한지 확인):
- `docs/architecture/governance-preconditions.md` §4 (GP-2, 특히 §4.5 Exit (a) line 451 = "Hermes native redaction Tier-1 42 catalog 적용 검증 + P1 facade redaction filter 검증")
- `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.3 (운영 함의 #2 line 113 = Hermes redaction 송신 방어 위임 / #4 R-6 자동 회귀 / 권위 위계 Hermes ≠ root of trust / §2.4 T3)
- `docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md` §2 (P1 facade MVP 진입조건) + §2.3 (Hermes PMO ≠ provider, facade 단일 진입점, LiteLLM 직접 import = facade.py 한정)
- `docs/architecture/redaction-pattern-equivalence.md` (R-4 설계 동등성, "Hermes 안전성 선언 금지" §7.3)
- `src/adapters/llm/facade.py` (현 placeholder 상태 — R-2 facade real 대상, 42 LOC, NotImplementedError)
- `docs/phase0/mvp2-gp2-pass-activation-brief.md` (60 GP-2 detection-layer PASS, §2 3축 분리)

선행 합의 (참고):
- 60 GP-2 detection-layer PASS 발효 (B-1 detection/prevention 3축 분리)
- 57 (β) R-4 결정 (R-1 import 별도 cycle, R-2 facade real 별도 trajectory)
- 62 MVP-2 PASS (prevention deferred scope 명문)
- 52 entry R-A-1 (agent/redact.py 본 repo 부재 = upstream v0.12.0 401 LOC)

## 검토 관점 (외부 cross-vendor 독립)

1. **권위 인용 정확성**: brief의 governance §4.5 (a) / ADR-011 §2.3 #2 / ADR-009 §2.3 / R-4 인용이 실제 문서와 일치하는가? verbatim 모순 0건인가?
2. **scope 정합**: trajectory 진입 한정 vs 실제 결정/구현/발효 0 경계가 명확한가? over-claim/scope creep 있는가?
3. **R-1/R-2 경로 분석 타당성**: R-1 = upstream 영역 분리 (직접 구현 불가) 판단이 정확한가? R-2 = TR-1 발화 + Provider Liquidity 직결 분석이 타당한가?
4. **full GP-2 PASS = R-1 ∧ R-2 (AND)** 격차 정의가 governance §4.5 (a) 와 정합하는가?
5. **prevention over-claim**: R-4 = 설계 동등성 ≠ prevention 입증 구분이 명확한가? (본 프로젝트 세션 #2에서 4회 over-claim cascade 포착된 핵심 risk)
6. **sub-cycle 분리/순서 권고**: SC-1(R-2)→SC-2(R-1)→SC-3 권고가 ≠ 결정으로 명확한가?
7. **누락/risk**: brief가 놓친 위험, 의존성, 대안이 있는가?

## 응답 형식 (필수)

1. **판정**: APPROVE / APPROVE WITH CONDITIONS / REVISE 중 하나 (명확히)
2. **BLOCKING 항목** (있으면): 발효 전 반드시 정정 — 번호 + 근거 (직접 read한 line 인용)
3. **권고 항목**: 개선 권고 — 번호 + 내용
4. **NOTE**: 참고/관찰
5. **권위 인용 cross-verify 결과**: brief 인용 vs 실제 문서 일치/모순 매트릭스

한국어로 응답하되 기술 용어는 영어 원문 유지. 직접 파일을 read하여 검증하고, 추측이나 일반론이 아닌 구체적 line 인용 기반으로 응답하세요.

codex
요청하신 대로 외부 검토자 관점에서 파일을 직접 읽고 line 근거로만 판정하겠습니다. 먼저 primary brief와 권위 문서의 관련 구간을 병렬로 확인합니다.
exec
/bin/bash -lc "nl -ba docs/phase0/mvp2-full-gp2-pass-trajectory-entry-brief.md | sed -n '1,260p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# full GP-2 PASS trajectory 진입 entry brief (v1)
     2	
     3	> **작성**: 2026-05-28 (64번째 entry 진입 cycle — 신규 세션 #3)
     4	>
     5	> **scope**: full GP-2 PASS trajectory **진입 자격 audit + R-1/R-2 경로 분석 + 합의 형태 권고**. 실제 sub-수단 *결정* 0 / 실 *구현* 0 / full GP-2 PASS *발효* 0. (사용자 명시 scope = "trajectory entry brief 한정")
     6	>
     7	> **본 cycle = 큰 cycle** (trajectory 진입 합의, 풀 3+1 + 외부 LLM 1+ 의무). 51 audit / 52 (α) entry brief / 55 Layer 통합 PASS entry brief 답습 동형 (entry brief = 진입 자격 + 경로 분석, sub-cycle 진입은 사용자 명시 별도)
     8	>
     9	> **본 cycle 발효 자격** = 진입 자격 audit + 경로 분석 + 합의 형태 권고 + 풀 3+1 + 외부 LLM 1+ 합의 APPROVE + 사용자 명시
    10	>
    11	> **본 cycle 발효 효과** = full GP-2 PASS trajectory **진입 자격 발효** + R-1/R-2 sub-cycle 진입 권한 발효 (조건부 승인 조건 우선). 실제 R-1 import *결정* / R-2 facade real *구현* / full GP-2 PASS *발효* = 각각 별도 sub-cycle (본 cycle = trajectory 진입 한정)
    12	>
    13	> **선행 답습**: 60 GP-2 detection-layer PASS 발효 (`92e9078`, B-1 detection/prevention 3축 분리) + 57 (β) R-4 결정 ((β) §0.2 #9 R-1 import 별도 cycle) + 62 MVP-2 Implementation Evidence PASS (prevention deferred scope 명문) + 52 entry R-A-1 (`agent/redact.py` 본 repo 부재 = upstream v0.12.0 401 LOC)
    14	
    15	---
    16	
    17	## §0 본 brief 의 범위
    18	
    19	### §0.1 본 brief 가 *하는* 것
    20	
    21	1. **detection-layer PASS → full GP-2 PASS 격차 정의** (Exit (a) prevention 검증 = R-1 + R-2, 60 §2 3축 답습) (§2)
    22	2. **R-1 경로 분석** (Hermes native redaction, upstream 영역 / import 결정 / 검증 evidence 후보) (§3)
    23	3. **R-2 경로 분석** (facade RedactionFilter, TR-1 발화 / Provider Liquidity 직결 / (d) carry-over 동일 trajectory) (§4)
    24	4. **R-1 ↔ R-2 의존 관계 + sub-cycle 분리 권고** (§5)
    25	5. **합의 형태 = 풀 3+1 + 외부 LLM 1+ + 승격 트리거** (§6)
    26	6. **trajectory 진입 자격 권고 + 조건** (§7)
    27	7. Rollback Trigger / Evidence 후보 / 금지 / 다음 단계 / cross-ref / 자기진단 (§8~§13)
    28	
    29	### §0.2 본 brief 가 *하지 않는* 것
    30	
    31	| # | 영역 | 위반 |
    32	|---|------|----|
    33	| 1 | full GP-2 PASS *발효* 자체 (본 brief = trajectory 진입 합의 입력) | 0 |
    34	| 2 | **R-1 Hermes upstream `agent/redact.py` 본 repo 內 import 결정** (별도 sub-cycle, 57 (β) §0.2 #9 답습) | 0 |
    35	| 3 | **R-2 facade real 구현** (TR-1 발화 = 별도 sub-cycle, `facade.py` placeholder → real 본문 작성 0) | 0 |
    36	| 4 | Hermes upstream PR 작성 / upstream `agent/redact.py` 본문 변경 (upstream 영역, 본 repo scope 외) | 0 |
    37	| 5 | R-1/R-2 中 *어느 sub-cycle 우선 진입* 결정 (§5 권고 ≠ 결정, 사용자 명시 별도) | 0 |
    38	| 6 | MVP-2 Implementation Evidence PASS 재선언 (62 답습 유지) / detection-layer PASS 재선언 (60 답습) | 0 |
    39	| 7 | R-5 base64/URL/압축 evasion 영역 진입 (영구 분리, G3-4) | 0 |
    40	| 8 | 신규 외부 library 도입 / secret_scanner Tier-2/3 catalog 확장 | 0 |
    41	| 9 | ADR / 헌법 / roadmap / governance / ADR-008/009/011/012 본문 갱신 | 0 |
    42	| 10 | `facade.py` / `secret_scanner.py` / secret-hygiene workflow 본문 변경 | 0 (PoC 시제 + placeholder 보존) |
    43	| 11 | Provider Liquidity 5-way Defense 본문 변경 / LiteLLM 도입 결정 (Q1 합의 보존) | 0 |
    44	| 12 | 자동 후속 sub-cycle 진입 (R-1 / R-2 / full GP-2 PASS) | 0 (사용자 명시 의무) |
    45	| 13 | 본 brief 자체 영구화 / 권위 chain 등재 | 0 |
    46	
    47	### §0.3 권위 답습 source
    48	
    49	- **governance-preconditions.md §4.5 Exit (a)** (line 451) — "Hermes native redaction Tier-1 42 catalog 적용 검증 + P1 facade redaction filter 검증" (= R-1 + R-2 prevention 검증, full GP-2 PASS Exit 핵심)
    50	- **ADR-011 §2.3 운영 함의 #2** (line 113) — "Hermes 자체 redaction은 로그/LLM 송신 방어로만 신뢰, 저장 경로 책임 0" (R-1 위임 권위) + 권위 위계 (Hermes ≠ root of trust, line 95~108)
    51	- **ADR-011 §2.4 T3** (line 133) — ADR/헌법/Harness Gates 정의 변경 = 풀 3+1 (facade real 코드 구현 ≠ T3, R-2 = TR-1 별도 trigger)
    52	- **ADR-009 §2** (line 49~62) — P1 facade MVP 진입조건 (2026-05-04 이미 충족) + §2.3 Hermes PMO ≠ provider 직접 소유 + LiteLLM 직접 import = `facade.py` 한정
    53	- **`redaction-pattern-equivalence.md` (R-4)** (line 33/39) — 설계 동등성 문서, "Hermes 안전성 선언 금지" (ADR-011 §7.3), prevention *입증* 아님
    54	- **60 GP-2 detection-layer PASS brief v1.1** (`docs/phase0/mvp2-gp2-pass-activation-brief.md`) — §2 3축 분리 (detection ✅ / 설계 동등성 ⚠️ / prevention upstream 위임)
    55	- **57 (β) brief v1.1** (`docs/phase0/mvp2-beta-submeans-decision-brief.md`) — R-4 결정 + R-1 import 별도 cycle + R-2 facade real 별도 trajectory
    56	- **62 MVP-2 PASS brief** (`docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md`) — prevention deferred scope 명문
    57	- **52 entry R-A-1** (`docs/review/3plus1-consensus-2026-05-28-mvp2-entry.md`) — `agent/redact.py` 본 repo 부재 = upstream HEAD v0.12.0 `/tmp/hermes-phase0/hermes-agent/agent/redact.py` 401 LOC
    58	- **본 cycle audit (read-only, 2026-05-28)** — `facade.py` placeholder + governance §4 + ADR-011 §2.3 filesystem direct
    59	
    60	---
    61	
    62	## §1 진입 컨텍스트
    63	
    64	### §1.1 선행 chain
    65	
    66	| 합의/구현 | 본 cycle 답습 |
    67	|----------|-----------|
    68	| 62 MVP-2 Implementation Evidence PASS (`82e1ee6`, 4 source APPROVE WITH CONDITIONS) | MVP-2 = G4 ledger 완전 + GP-2 **detection-tier**. **full GP-2 PASS (prevention R-1/R-2) = MVP-2 PASS 잔여 trajectory** (62 §결론 명문) → 본 cycle = 그 trajectory 진입 |
    69	| 60 GP-2 detection-layer PASS (`92e9078`, REVISE → detection reframe) | (b)(c)(d) detection ✅ operative + (a) 설계 동등성 partial. prevention (R-1/R-2) = in-repo 입증 0 (upstream 위임) → 본 cycle = prevention 경로 분석 |
    70	| 57 (β) R-4 결정 (`18e8ad1`) | GP-2 수단 = R-4 (R-3 detection 우선 + R-1/R-2 prevention deferred). **R-1 import = 별도 cycle ((β) §0.2 #9) / R-2 facade real = 별도 trajectory ((β) §0.2 #23)** |
    71	
    72	### §1.2 현 GP-2 상태 (60 §2 3축 답습)
    73	
    74	- **축 1 detection (operative ✅)**: R-3 (`secret-hygiene-egress-redaction.yml` D-2 + `secret_scanner.py --mode scan-log`) — 송신/로그 secret 잔존 회귀 검출. in-repo operative green (actual run `26517803107`).
    75	- **축 2 설계 동등성 (⚠️ partial)**: R-4 (`redaction-pattern-equivalence.md`) — Tier-1 42 catalog *패턴 동등성 문서*. prevention 입증 아님 (Hermes 안전성 선언 금지).
    76	- **축 3 prevention (in-repo 입증 0)**: R-1 (Hermes native, 본 repo 부재) + R-2 (facade placeholder). **본 cycle 대상 = 축 3 경로 분석**.
    77	
    78	→ **detection-layer PASS → full GP-2 PASS 격차 = 축 3 prevention 검증 (= Exit (a))**. 본 cycle = 이 격차를 메우는 trajectory 진입 자격 + 경로 분석 (실제 충족은 sub-cycle).
    79	
    80	---
    81	
    82	## §2 detection-layer PASS → full GP-2 PASS 격차 (Exit (a) prevention 검증)
    83	
    84	### §2.1 Exit 5조건 현 상태 (governance §4.5 + 60 §4)
    85	
    86	| # | 조건 | detection-layer (60 발효) | full GP-2 PASS 추가 요구 |
    87	|---|------|------|---------|
    88	| (a) | 동등 이상 보안 결과 | ⚠️ **partial (설계 동등성)** | ✅ 격상 = **R-1 Hermes native Tier-1 42 적용 검증 + R-2 facade redaction filter 검증** (governance §4.5 (a) verbatim) |
    89	| (b) | 격리 PoC 실증 | ✅ secret-hygiene D-2 (detection) | prevention PoC (R-1 실행 evidence + R-2 filter 단위 test) |
    90	| (c) | ADR/SDD 권위 | ✅ ADR-011 §2.3 #2 + governance §4 | (유지) |
    91	| (d) | 자동 회귀 검증 | ✅ secret-hygiene D-2 CI green (detection) | prevention 회귀 (R-1 upstream 변경 시 R-2/R-4.1 자동 재실행, ADR-011 §2.3 #4 R-6) |
    92	| (e) | 합의 APPROVE | ✅ 60 (detection-layer) | full GP-2 PASS 발효 합의 (별도) |
    93	
    94	### §2.2 핵심 격차 = (a) prevention 검증 2-pronged
    95	
    96	governance §4.5 (a) line 451 = **"Hermes native redaction Tier-1 42 catalog 적용 검증 + P1 facade redaction filter 검증"** — 2개 prevention 수단 모두 검증 요구:
    97	1. **R-1**: Hermes native redaction이 Tier-1 42 catalog를 실제 적용함을 *검증* (적용 *구현*은 upstream 영역).
    98	2. **R-2**: facade RedactionFilter가 LLM API request body redaction을 적용함을 *검증* (= facade real 선행).
    99	
   100	→ full GP-2 PASS = R-1 검증 + R-2 검증 둘 다. 본 cycle = 두 경로의 진입 자격 + 분석 (§3 + §4).
   101	
   102	---
   103	
   104	## §3 R-1 경로 분석 — Hermes native redaction (Tier-1 42 적용 검증)
   105	
   106	### §3.1 영역 분리 (52 entry R-A-1 답습 — 핵심)
   107	
   108	| 영역 | 내용 | 본 cycle scope |
   109	|------|----|------|
   110	| **(i) Hermes upstream 영역** | `agent/redact.py` (upstream HEAD v0.12.0, `/tmp/hermes-phase0/hermes-agent/agent/redact.py` 401 LOC) — **본 repo 內 ≠ 존재** | ❌ scope 외 (upstream PR 영역) |
   111	| **(ii) 본 repo import 결정 영역** | Hermes runtime redaction을 본 repo runtime 의존성에 *통합/위임 신뢰* 결정 (ADR-011 §2.3 #2 위임 권위 활용) | sub-cycle (본 cycle = 분석만) |
   112	| **(iii) 본 repo 검증 evidence 영역** | Hermes native가 Tier-1 42 catalog 적용함을 격리 환경 실행 검증 (E-1 답습, `agent/redact.py` 실행 evidence) | sub-cycle (본 cycle = 후보 식별) |
   113	
   114	### §3.2 R-1 권위 = ADR-011 §2.3 #2 위임 (이미 발효)
   115	
   116	- ADR-011 §2.3 #2 (line 113): "Hermes 자체 redaction은 **로그/LLM 송신 방어로만 신뢰**, 저장 경로(DB/파일) 차단 책임 없음."
   117	- 즉 R-1 runtime redaction은 **이미 ADR 권위로 위임됨** — full GP-2 PASS는 R-1을 *재구현*하는 것이 아니라 **위임이 실효함을 검증** (Tier-1 42 적용 evidence + upstream 변경 자동 회귀, §2.3 #4 R-6).
   118	- ⚠️ **Hermes ≠ root of trust** (권위 위계 line 95~108): Hermes 출력은 Tools로 검증된다 → R-1 검증 = canary/test가 Hermes 위에 위치 (R-5/R-6 근거).
   119	
   120	### §3.3 R-1 경로 후보 (sub-cycle 입력, 결정 0)
   121	
   122	- **(R-1-a) 위임 검증 한정**: 본 repo는 import 0, ADR-011 §2.3 #2 위임 유지 + Tier-1 42 적용 검증 evidence (격리 실행) + upstream 변경 R-6 자동 재실행. → 본 repo runtime code 변경 최소.
   123	- **(R-1-b) import 통합**: Hermes runtime redaction을 본 repo runtime 의존성으로 통합 (52 R-A-1 import 결정). → Provider Liquidity / Hermes PMO 경계 영향 (ADR-009 §2.3) 평가 필요.
   124	- ⭐ **권고 방향**: (R-1-a) 위임 검증 우선 — 본 repo = DESIGN/governance repo (60 §1.2), Hermes ≠ root of trust 답습. import (R-1-b)는 Hermes PMO 활성화 시점 별도. **(결정 = sub-cycle, 본 cycle = 권고만)**.
   125	
   126	---
   127	
   128	## §4 R-2 경로 분석 — facade RedactionFilter (facade real, TR-1)
   129	
   130	### §4.1 현 상태 = placeholder (filesystem direct verify)
   131	
   132	- `src/adapters/llm/facade.py` (42 LOC): `LLMFacade.complete()` = `raise NotImplementedError("Placeholder — TR-1 풀 3+1 합의 후 real 본문 작성")`. `health()` = `return {}`.
   133	- 헤더 명문: "본 파일은 *유일하게* LiteLLM 직접 import 가 *허용되는 경로* (§4.1 답습). 현 시점 placeholder — real 본문 작성 시 자동 풀 3+1 합의 trigger **TR-1** 발화."
   134	
   135	### §4.2 R-2 = full GP-2 PASS + (d) carry-over 동일 trajectory
   136	
   137	- **(d) facade real (TR-1)** = 63 entry carry-over #4 + 본 trajectory R-2 = **동일 작업** (별도 아님). full GP-2 PASS prevention 입증을 위해 facade real이 *선행 필수* (RedactionFilter는 real facade 진입점에만 부착 가능).
   138	- governance §4.3 (line 435): "P1 v2 LLM facade RedactionFilter" = 계산적 강제 메커니즘 (P1 facade layer).
   139	
   140	### §4.3 R-2 = Provider Liquidity 5조-2 직결 (비협상)
   141	
   142	- ADR-009 §2 (line 49~62): P1 facade MVP 진입조건 4개 **2026-05-04 이미 충족** — 별도 트리거 없음. ADR-008 + P1 v2 합의 APPROVE = MVP 진입 도화선.
   143	- ADR-009 §2.3: **Hermes PMO ≠ provider 직접 소유** — provider SDK 직접 import / 모델명 분기 *금지*, P1 facade 단일 진입점 강제. LiteLLM 직접 import = `facade.py` 한 파일 한정.
   144	- ⚠️ **R-2 facade real = Provider Liquidity 5-way Defense Layer 1 실 구현** (코드 변경 없이 모델/provider 교체 = 헌법 5조-2 비협상, [[feedback_provider_liquidity]]). LiteLLM 도입 자체는 Q1 합의 (2026-05-10) 보존 — 본 cycle 신규 도입 0.
   145	
   146	### §4.4 R-2 경로 후보 (sub-cycle 입력, 결정 0)
   147	
   148	- **(R-2-a) facade real + RedactionFilter 동시**: facade real 본문 (LiteLLM import + Router 위임) + RedactionFilter (request body Tier-1 42 redaction) 통합 구현. → TR-1 발화 = 풀 3+1 합의.
   149	- **(R-2-b) facade real 먼저 / RedactionFilter 후속**: facade real (Provider Liquidity Layer 1) 우선 발효 → RedactionFilter는 별도 step. → 2 sub-cycle.
   150	- ⭐ **권고 방향**: (R-2-a) 동시 — RedactionFilter는 facade 진입점 의존, 분리 시 facade real 후 redaction 미부착 window 발생. TDD 적용 (RED: redaction filter test → GREEN: filter 구현). **(결정 = sub-cycle, 본 cycle = 권고만)**.
   151	
   152	---
   153	
   154	## §5 R-1 ↔ R-2 의존 관계 + sub-cycle 분리 권고
   155	
   156	### §5.1 의존 관계
   157	
   158	| 관계 | 내용 |
   159	|------|----|
   160	| R-1 ⊥ R-2 (독립) | R-1 = Hermes runtime (upstream/위임 검증) / R-2 = facade layer (본 repo). 서로 다른 layer = defense-in-depth (R-4 §3.1 답습) |
   161	| full GP-2 PASS = R-1 ∧ R-2 | Exit (a) = "Hermes native 검증 **+** facade filter 검증" — 둘 다 (AND). 한쪽만 = full GP-2 PASS 미충족 |
   162	| R-2 = (d) carry-off 흡수 | R-2 facade real = (d) facade real 동일 작업 → R-2 진행 = (d) 동시 해소 |
   163	
   164	### §5.2 sub-cycle 분리 권고 (결정 0 — 사용자 명시 별도)
   165	
   166	| sub-cycle | 작업 | 규모 | 의존 |
   167	|-----------|----|----|----|
   168	| **SC-1 (R-2 facade real)** | facade real + RedactionFilter (TR-1) | 풀 3+1 (TR-1 trigger) + 실 코드 | (d) carry-over 흡수, Provider Liquidity Layer 1 |
   169	| **SC-2 (R-1 위임 검증)** | Hermes native Tier-1 42 적용 검증 evidence + R-6 자동 회귀 (import = (R-1-b) 시 추가 평가) | 풀 3+1 + 격리 실행 | ADR-011 §2.3 #2 위임 |
   170	| **SC-3 (full GP-2 PASS 발효)** | SC-1 + SC-2 evidence 완료 후 PASS 발효 합의 | 풀 3+1 + 외부 LLM 1+ + 사용자 명시 (32/60 답습) | SC-1 ∧ SC-2 |
   171	
   172	⭐ **순서 권고**: SC-1 (R-2) → SC-2 (R-1) → SC-3. 사유 = R-2 = 본 repo 영역 + (d) carry-over 흡수 + Provider Liquidity 직결 (즉시 가치). R-1 = upstream 위임 (이미 ADR 권위) → 검증 evidence 중심. **(순서 결정 = 사용자 명시 별도, 본 cycle = 권고)**.
   173	
   174	---
   175	
   176	## §6 합의 형태 + 풀 3+1 승격 트리거
   177	
   178	### §6.1 합의 형태 = 풀 3+1 + 외부 LLM 1+ (의무)
   179	
   180	**정당화**: trajectory 진입 합의 (52 (α) / 55 entry brief 답습) + 큰 결정 (full GP-2 PASS = MVP-2 잔여 trajectory) + 헌법 5조-2 cross-vendor + R-2 = Provider Liquidity 직결.
   181	
   182	### §6.2 7 승격 트리거
   183	
   184	| # | trigger | 발화 | 근거 |
   185	|---|---------|----|------|
   186	| 1 | 큰 결정 (trajectory 진입) | ✅ | full GP-2 PASS trajectory = MVP-2 prevention 잔여 |
   187	| 2 | 아키텍처/SDD/보안 본문 변경 | ❌ | brief = phase0 신규 1 |
   188	| 3 | ADR 본문 변경 | ❌ | 0 |
   189	| 4 | 권위 chain 다중 source 손상 | ❌ | 권위 인용 답습 (governance §4.5 + ADR-011 §2.3) |
   190	| 5 | 외부 LLM 통합 필요 | ✅ | cross-vendor 의무 (5조-2) |
   191	| 6 | Provider Liquidity 영향 | ✅ ⭐ | R-2 facade real = Provider Liquidity Layer 1 |
   192	| 7 | Hermes PMO 격상 | ❌ | 0 (R-1 import = sub-cycle, 본 cycle 결정 0) |
   193	
   194	→ **3/7 발화 → 풀 3+1 + 외부 LLM 1+ 적격**.
   195	
   196	### §6.3 외부 LLM = cross-vendor codex (E-α 답습)
   197	
   198	55/52/60 entry 답습 — Claude tmux + codex 직접 호출 (`--dangerously-bypass-approvals-and-sandbox`, gpt-5.5 cross-vendor).
   199	
   200	---
   201	
   202	## §7 trajectory 진입 자격 권고 + 조건
   203	
   204	⭐ **권고 = full GP-2 PASS trajectory 진입 APPROVE WITH CONDITIONS**:
   205	
   206	1. **trajectory 진입 자격 충족** — detection-layer PASS (60 ✅) + MVP-2 PASS prevention 잔여 trajectory 명문 (62 ✅) + 격차 = (a) prevention 검증 (§2.2).
   207	2. **조건**:
   208	   - (C-1) **R-1 = Hermes upstream 영역 분리 답습** — 본 repo `agent/redact.py` 부재 (52 R-A-1), 직접 구현 = upstream PR (scope 외). 본 repo = 위임 검증 (R-1-a 권고) 또는 import 결정 (R-1-b, Hermes PMO 경계 평가).
   209	   - (C-2) **R-2 facade real = TR-1 발화 = 별도 sub-cycle** — `facade.py` placeholder 보존, real 본문 = SC-1 합의 후. (d) carry-over 동시 해소.
   210	   - (C-3) **full GP-2 PASS = R-1 ∧ R-2 검증 (AND)** — 한쪽 단독 ≠ full GP-2 PASS (Exit (a) 2-pronged).
   211	   - (C-4) **Provider Liquidity 5조-2 비협상** — R-2 facade real = Layer 1 실 구현, LiteLLM 도입은 Q1 합의 보존 (신규 0).
   212	   - (C-5) **detection-layer PASS / MVP-2 PASS 재선언 0** (60/62 답습 유지) + **prevention over-claim 주의** (본 세션 #2 4회 cascade 교훈, [[feedback_pass_scope_overclaim]] — R-4 = 설계 동등성, prevention 입증 아님).
   213	3. **sub-cycle 진입 = 사용자 명시 의무** (SC-1/SC-2/SC-3 순서 §5.2 권고 ≠ 결정).
   214	
   215	→ **trajectory 진입 발효 자격 = 진입 자격 audit + R-1/R-2 경로 분석 + 합의 APPROVE + 사용자 명시**. **full GP-2 PASS 발효 = SC-1 + SC-2 evidence 완료 후 SC-3 (별도)**.
   216	
   217	---
   218	
   219	## §8 Rollback Trigger 후보 (sub-cycle 입력, 결정 0)
   220	
   221	| # | trigger | 영역 | 대응 |
   222	|---|---------|----|----|
   223	| RT-1 | facade real 후 RedactionFilter 미부착 window | SC-1 | (R-2-a) 동시 구현 (분리 금지) |
   224	| RT-2 | Hermes upstream redaction silent 깨짐 (Tier-1 42 미적용 회귀) | SC-2 | R-6 자동 재실행 (ADR-011 §2.3 #4) + R-5 canary 재검증 |
   225	| RT-3 | LiteLLM 도입이 Provider Liquidity 위반 (provider lock-in) | SC-1 | ADR-009 §2.3 facade 단일 진입점 강제 + 5-way Defense |
   226	| RT-4 | base64/URL evasion 발견 | R-5 영역 | known limitation 명문 (영구 분리, G3-4) |
   227	| RT-5 | R-1 import (R-1-b)이 Hermes ≠ root of trust 위반 | SC-2 | 위임 검증 (R-1-a) 환원 또는 Hermes PMO 경계 합의 |
   228	
   229	---
   230	
   231	## §9 Evidence 후보 (sub-cycle 입력, 결정 0)
   232	
   233	- E-1: Hermes native `agent/redact.py` Tier-1 42 catalog 적용 격리 실행 evidence (governance §4.4 R-1 Day 2 답습)
   234	- E-2: facade RedactionFilter 단위 test (request body Tier-1 42 redaction, TDD RED→GREEN)
   235	- E-3: facade real LiteLLM Router 위임 동작 evidence (Provider Liquidity Layer 1)
   236	- E-4: R-6 workflow upstream 변경 자동 재실행 actual run (ADR-011 §2.3 #4)
   237	- E-5: full GP-2 PASS Exit (a)~(e) evidence 매트릭스 (SC-3 입력)
   238	
   239	---
   240	
   241	## §10 금지 사항
   242	
   243	§0.2 답습 (13). 추가: R-1 import 결정 0 / R-2 facade real 구현 0 / upstream PR 0 / full GP-2 PASS 발효 0 / sub-cycle 우선순위 결정 0 / LiteLLM 신규 도입 0 / 자동 후속 0.
   244	
   245	---
   246	
   247	## §11 다음 단계 (사용자 명시 의무 — 자동 진입 0)
   248	
   249	1. 본 brief 승인 → 풀 3+1 + 외부 LLM 1+ (codex E-α) → Reviewer 통합 → v1.1 흡수 → commit + push → **trajectory 진입 자격 발효**
   250	2. **SC-1 (R-2 facade real + RedactionFilter, TR-1)** — facade real 본문 + filter 구현 (실 코드, TDD). (d) carry-over 동시 해소 (별도 sub-cycle)
   251	3. **SC-2 (R-1 위임 검증)** — Hermes native Tier-1 42 적용 검증 evidence + R-6 자동 회귀 (별도 sub-cycle)
   252	4. **SC-3 (full GP-2 PASS 발효 합의)** — SC-1 ∧ SC-2 evidence 후 (32/60 답습, 별도 cycle)
   253	
   254	---
   255	
   256	## §12 cross-reference 답습
   257	
   258	- governance-preconditions.md §4 (GP-2 정의 + §4.5 Exit (a) line 451)
   259	- ADR-011 §2.3 운영 함의 #2 (R-1 위임) + #4 (R-6 자동 회귀) + 권위 위계 (Hermes ≠ root of trust) + §2.4 T3
   260	- ADR-009 §2 (P1 facade MVP 진입조건) + §2.3 (Hermes PMO ≠ provider, facade 단일 진입점)

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

exec
/bin/bash -lc "nl -ba docs/decisions/ADR-011-means-vs-ends-redaction.md | sed -n '90,145p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
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

codex
primary brief의 핵심 scope/금지 문구와 governance/ADR 인용은 우선 확인했습니다. 이제 R-4 문서, facade 실제 상태, 60 detection-layer brief의 3축 구분을 대조해 남은 모순 여부를 확인합니다.
exec
/bin/bash -lc "nl -ba docs/architecture/redaction-pattern-equivalence.md | sed -n '1,220p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# Redaction Pattern Equivalence (R-4)
     2	
     3	> **ADR-011 §2.1 (a) "동등 이상 보장" 검증 의무의 직접 충족 작업 — 코드 변경 없는 패턴 비교 + gap 식별 + 보충 권고 문서화**
     4	
     5	**상태**: 작성 (R-4 단축 검증 — 코드 수정 미포함)
     6	**날짜**: 2026-05-06
     7	**상위 권위**: ADR-011 §2.1 (a) (대체 수단 동등 이상 보장 검증 의무), §3 R-4 매핑
     8	**모법 ADR**: `docs/decisions/ADR-011-means-vs-ends-redaction.md`
     9	**갱신 대상**: ADR-008 부록 B B.6 R-4 항목 ⏳ → 본 문서 발행 시 ✅
    10	**산출 의도**: trigger UDF 보충 권고 카탈로그 — 실제 보충 코드 작성은 별도 작업 (보충 자체도 ADR-011 §2.1 (a)~(d) 4조건 적용 대상)
    11	
    12	---
    13	
    14	## 1. 작업 정의
    15	
    16	### 1.1 본 R-4의 본질 (사용자 명시)
    17	
    18	> **이번 단계의 핵심은 "코드 수정"이 아니라 "패턴 추출 → 비교 → gap 식별 → 보충 권고 문서화"이다.**
    19	
    20	본 문서는 다음 4단계를 산출한다:
    21	
    22	| # | 단계 | 산출 §  |
    23	|---|------|--------|
    24	| 1 | **추출** — Hermes / P1_REDACTOR / R-2 trigger UDF 패턴 카탈로그 | §2 / §3 / §4 |
    25	| 2 | **비교** — 3-way 동등성 매트릭스 | §5 |
    26	| 3 | **gap 식별** — Tier 1/2/3 분류 | §6 |
    27	| 4 | **보충 권고** — trigger UDF 확장 카탈로그 (코드 미작성) | §7 |
    28	
    29	### 1.2 ADR-011 §2.1 (a) 충족 의무
    30	
    31	> **(a) 동등 이상의 보안 결과 — 명시적 비교표 (수단 A 보장 ↔ 수단 B 보장)**
    32	
    33	본 문서 §5의 3-way 비교표가 (a) 직접 충족 산출이다. 본 문서는 보안 결과를 *선언*하지 않으며, 비교 사실과 gap을 *기록*한다 — gap이 미보충 상태에서 G1b 정식 충족 (ADR-008 부록 B.6) 진입 불가.
    34	
    35	### 1.3 본 문서가 *하지 않는* 것
    36	
    37	- ❌ trigger UDF 패턴 코드 수정 — 본 문서는 *권고 카탈로그*이며 보충 작업은 별도 작업으로 분리 (ADR-011 §2.1 (b) "격리 환경 PoC 실증" 의무 별도 적용)
    38	- ❌ Hermes redaction 우회 가능성 평가 — base64 우회 등은 R-2 PoC §6 향후 검증 항목 + R-7 SOP 영역
    39	- ❌ Hermes 안전성 선언 — ADR-011 §7.3 "본 ADR은 Hermes 안전성을 선언하지 않는다" 위반 금지
    40	- ❌ P1_REDACTOR ↔ R-2 trigger UDF 직접 비교의 우선시 — P1_REDACTOR는 P1 facade 호출 경로 한정 (LiteLLM callback). DB INSERT 차단의 기준선은 Hermes 패턴 카탈로그 (광역 수단)
    41	
    42	---
    43	
    44	## 2. Hermes 패턴 카탈로그 추출
    45	
    46	**출처**: `/tmp/hermes-phase0/hermes-agent/agent/redact.py` (v0.12.0 main HEAD, 401 LOC)
    47	**docstring 명시 (line 1-2)**: "Regex-based secret redaction for logs and tool output"
    48	**적용 범위**: 로그/도구 출력/LLM 송신 — DB INSERT 미적용 (R-1 FAIL 확정, ADR-011 §2.2 G1a)
    49	
    50	### 2.1 `_PREFIX_PATTERNS` (35종, line 67-103)
    51	
    52	| # | Vendor / Type | Regex | 출처 라인 |
    53	|---|------|------|------|
    54	| 1 | OpenAI / OpenRouter / Anthropic (`sk-ant-*`) | `sk-[A-Za-z0-9_-]{10,}` | 68 |
    55	| 2 | GitHub PAT (classic) | `ghp_[A-Za-z0-9]{10,}` | 69 |
    56	| 3 | GitHub PAT (fine-grained) | `github_pat_[A-Za-z0-9_]{10,}` | 70 |
    57	| 4 | GitHub OAuth access token | `gho_[A-Za-z0-9]{10,}` | 71 |
    58	| 5 | GitHub user-to-server | `ghu_[A-Za-z0-9]{10,}` | 72 |
    59	| 6 | GitHub server-to-server | `ghs_[A-Za-z0-9]{10,}` | 73 |
    60	| 7 | GitHub refresh token | `ghr_[A-Za-z0-9]{10,}` | 74 |
    61	| 8 | Slack tokens | `xox[baprs]-[A-Za-z0-9-]{10,}` | 75 |
    62	| 9 | Google API keys | `AIza[A-Za-z0-9_-]{30,}` | 76 |
    63	| 10 | Perplexity | `pplx-[A-Za-z0-9]{10,}` | 77 |
    64	| 11 | Fal.ai | `fal_[A-Za-z0-9_-]{10,}` | 78 |
    65	| 12 | Firecrawl | `fc-[A-Za-z0-9]{10,}` | 79 |
    66	| 13 | BrowserBase | `bb_live_[A-Za-z0-9_-]{10,}` | 80 |
    67	| 14 | Codex encrypted tokens | `gAAAA[A-Za-z0-9_=-]{20,}` | 81 |
    68	| 15 | AWS Access Key ID | `AKIA[A-Z0-9]{16}` | 82 |
    69	| 16 | Stripe secret key (live) | `sk_live_[A-Za-z0-9]{10,}` | 83 |
    70	| 17 | Stripe secret key (test) | `sk_test_[A-Za-z0-9]{10,}` | 84 |
    71	| 18 | Stripe restricted key | `rk_live_[A-Za-z0-9]{10,}` | 85 |
    72	| 19 | SendGrid API key | `SG\.[A-Za-z0-9_-]{10,}` | 86 |
    73	| 20 | HuggingFace token | `hf_[A-Za-z0-9]{10,}` | 87 |
    74	| 21 | Replicate API token | `r8_[A-Za-z0-9]{10,}` | 88 |
    75	| 22 | npm access token | `npm_[A-Za-z0-9]{10,}` | 89 |
    76	| 23 | PyPI API token | `pypi-[A-Za-z0-9_-]{10,}` | 90 |
    77	| 24 | DigitalOcean PAT | `dop_v1_[A-Za-z0-9]{10,}` | 91 |
    78	| 25 | DigitalOcean OAuth | `doo_v1_[A-Za-z0-9]{10,}` | 92 |
    79	| 26 | AgentMail API key | `am_[A-Za-z0-9_-]{10,}` | 93 |
    80	| 27 | ElevenLabs TTS key | `sk_[A-Za-z0-9_]{10,}` | 94 |
    81	| 28 | Tavily search API | `tvly-[A-Za-z0-9]{10,}` | 95 |
    82	| 29 | Exa search API | `exa_[A-Za-z0-9]{10,}` | 96 |
    83	| 30 | Groq Cloud API key | `gsk_[A-Za-z0-9]{10,}` | 97 |
    84	| 31 | Matrix access token | `syt_[A-Za-z0-9]{10,}` | 98 |
    85	| 32 | RetainDB API key | `retaindb_[A-Za-z0-9]{10,}` | 99 |
    86	| 33 | Hindsight API key | `hsk-[A-Za-z0-9]{10,}` | 100 |
    87	| 34 | Mem0 Platform API key | `mem0_[A-Za-z0-9]{10,}` | 101 |
    88	| 35 | ByteRover API key | `brv_[A-Za-z0-9]{10,}` | 102 |
    89	
    90	**경계 강제 (line 182-184)**: `(?<![A-Za-z0-9_-])(...)(?![A-Za-z0-9_-])` — 앞뒤 단어 경계 부정 lookahead로 부분 매칭 회피.
    91	
    92	### 2.2 추가 Regex 패턴 (12종)
    93	
    94	| # | 이름 | 용도 | 출처 라인 |
    95	|---|------|------|------|
    96	| H-A | `_ENV_ASSIGN_RE` | `OPENAI_API_KEY=value` 형태 ENV 대입 | 107-109 |
    97	| H-B | `_JSON_FIELD_RE` | `"apiKey": "..."` JSON 필드 (12 키) | 113-116 |
    98	| H-C | `_AUTH_HEADER_RE` | `Authorization: Bearer <token>` | 119-122 |
    99	| H-D | `_TELEGRAM_RE` | `bot<digits>:<token>` Telegram bot | 126-128 |
   100	| H-E | `_PRIVATE_KEY_RE` | `-----BEGIN ... PRIVATE KEY-----` 블록 | 131-133 |
   101	| H-F | `_DB_CONNSTR_RE` | `postgres/mysql/mongodb/redis/amqp://user:pass@host` | 137-140 |
   102	| H-G | `_JWT_RE` | `eyJ...` JWT (1/2/3-part) | 144-147 |
   103	| H-H | `_DISCORD_MENTION_RE` | `<@<snowflake>>` (privacy) | 151 |
   104	| H-I | `_SIGNAL_PHONE_RE` | E.164 `+<country><number>` (privacy) | 155 |
   105	| H-J | `_URL_WITH_QUERY_RE` | URL 쿼리 스트링 — `_SENSITIVE_QUERY_PARAMS` 16종 redact | 160-166 |
   106	| H-K | `_URL_USERINFO_RE` | `https://user:pass@host` (DB 외 스킴) | 171-173 |
   107	| H-L | `_FORM_BODY_RE` | `k=v&k=v` 폼 바디 — `_SENSITIVE_BODY_KEYS` 14종 redact | 177-179 |
   108	
   109	### 2.3 Sensitive Key Frozenset (2종)
   110	
   111	#### `_SENSITIVE_QUERY_PARAMS` (16개, line 19-36)
   112	```
   113	access_token, refresh_token, id_token, token, api_key, apikey, client_secret,
   114	password, auth, jwt, session, secret, key, code, signature, x-amz-signature
   115	```
   116	
   117	#### `_SENSITIVE_BODY_KEYS` (14개, line 41-56)
   118	```
   119	access_token, refresh_token, id_token, token, api_key, apikey, client_secret,
   120	password, auth, jwt, secret, private_key, authorization, key
   121	```
   122	
   123	#### `_JSON_KEY_NAMES` (line 112)
   124	```
   125	api_?[Kk]ey, token, secret, password, access_token, refresh_token,
   126	auth_token, bearer, secret_value, raw_secret, secret_input, key_material
   127	```
   128	(`re.IGNORECASE` 적용)
   129	
   130	### 2.4 Hermes 측 총 카탈로그 요약
   131	
   132	| 카테고리 | 수 | 적용 게이트 |
   133	|---------|---|----------|
   134	| Prefix patterns | **35** | 단어 경계 강제 |
   135	| 추가 regex | **12** | 카테고리별 별도 정규식 |
   136	| Sensitive frozenset | **2** (16+14 키) | URL/form 키 매칭 |
   137	
   138	**기본값**: `HERMES_REDACT_SECRETS=false` (line 64) — opt-in. v0.12.0 breaking change로 default ON → OFF 전환됨 (Day 1 보고서 §2 기록).
   139	
   140	---
   141	
   142	## 3. P1_REDACTOR 패턴 카탈로그 추출
   143	
   144	**출처**: `docs/architecture/llm-providers-design.md` §8.2 (line 521-536)
   145	**적용 범위**: P1 facade의 LiteLLM `success_callback` / `failure_callback` (메트릭/메시지 — DB INSERT 미적용 + Day 1 §218 명시 "P1 facade 레벨 → 영향 없음")
   146	**상태**: P1 v2 *설계 명세* 단계 — 구현 코드 미존재
   147	
   148	### 3.1 `RedactionFilter.PATTERNS` (4종)
   149	
   150	| # | Vendor / Type | Regex |
   151	|---|------|------|
   152	| P-1 | OpenAI API key | `sk-[a-zA-Z0-9]{20,}` |
   153	| P-2 | Anthropic API key | `sk-ant-[a-zA-Z0-9]{20,}` |
   154	| P-3 | Bearer token | `Bearer [a-zA-Z0-9._-]+` |
   155	| P-4 | JSON field with secret keys | `"(api_key\|token\|auth\|secret\|password\|credential)"\s*:\s*"[^"]+"` |
   156	
   157	### 3.2 `KEY_BLACKLIST` (6개)
   158	```
   159	api_key, token, secret, auth, credential, authorization
   160	```
   161	
   162	### 3.3 P1_REDACTOR 측 총 카탈로그 요약
   163	
   164	| 카테고리 | 수 |
   165	|---------|---|
   166	| Patterns | **4** |
   167	| KEY_BLACKLIST | **6** 키 |
   168	
   169	P-1과 Hermes #1 모두 `sk-` prefix를 다루나 **문자 클래스 차이 존재** — Hermes는 `[A-Za-z0-9_-]` (`_`/`-` 허용), P1은 `[a-zA-Z0-9]` (`_`/`-` 미허용). Hermes가 **더 광범위**.
   170	
   171	---
   172	
   173	## 4. R-2 PoC trigger UDF 패턴 카탈로그 (현 baseline)
   174	
   175	**출처**: `docs/phase0/day3-r2-sqlite-trigger-poc.md` line 110-122 + `docker/r2-poc/r2_poc.py`
   176	**적용 범위**: SQLCipher BEFORE INSERT trigger (DB INSERT 직전, REGEXP UDF로 Python `re.search`)
   177	**작동 방식**: 매칭 시 `RAISE(ABORT, 'secret-pattern-detected: ...')` — 마스킹 미시도, INSERT 자체 거부 (사용자 선호 명시)
   178	**에러 메시지 고정 문자열**: `NEW.content` echo 안 함 → C6 만족 (에러 평문 미노출)
   179	
   180	### 4.1 현 trigger UDF 패턴 (5종)
   181	
   182	| # | Vendor / Type | Regex | Hermes 매핑 |
   183	|---|------|------|------|
   184	| T-1 | Anthropic | `sk-ant-[A-Za-z0-9_-]{10,}` | #1 (sk-) 부분집합 — 명시적 분리 |
   185	| T-2 | OpenAI / OpenRouter / Anthropic | `sk-[A-Za-z0-9_-]{10,}` | #1 동일 |
   186	| T-3 | GitHub PAT classic | `ghp_[A-Za-z0-9]{10,}` | #2 동일 |
   187	| T-4 | AWS Access Key ID | `AKIA[A-Z0-9]{16}` | #15 동일 |
   188	| T-5 | Slack tokens | `xox[baprs]-[A-Za-z0-9-]{10,}` | #8 동일 |
   189	
   190	### 4.2 R-2 trigger UDF 측 총 카탈로그 요약
   191	
   192	| 카테고리 | 수 |
   193	|---------|---|
   194	| Prefix patterns | **5** |
   195	| 추가 regex | **0** |
   196	| Sensitive frozenset | **0** |
   197	
   198	R-2 PoC는 *원리 실증*을 목표로 한 PoC였고, 패턴 5종은 canary 5종에 대응하는 최소 검증 세트. **본 R-4의 출발점은 이 5종이 G1b 정식 충족 기준선이 아님을 확정하는 데 있다.**
   199	
   200	---
   201	
   202	## 5. 3-way 동등성 비교 매트릭스
   203	
   204	### 5.1 Prefix patterns (35종 기준)
   205	
   206	| # | 패턴 | Hermes | P1_REDACTOR | R-2 trigger | gap 분류 |
   207	|---|------|------|------|------|------|
   208	| 1 | `sk-` (OpenAI/Anthropic/etc) | ✅ | ✅ (P-1, P-2) | ✅ (T-1, T-2) | — |
   209	| 2 | `ghp_` (GitHub PAT) | ✅ | ❌ | ✅ (T-3) | — |
   210	| 3 | `github_pat_` | ✅ | ❌ | ❌ | **Tier-1** |
   211	| 4 | `gho_` | ✅ | ❌ | ❌ | **Tier-1** |
   212	| 5 | `ghu_` | ✅ | ❌ | ❌ | **Tier-1** |
   213	| 6 | `ghs_` | ✅ | ❌ | ❌ | **Tier-1** |
   214	| 7 | `ghr_` | ✅ | ❌ | ❌ | **Tier-1** |
   215	| 8 | `xox[baprs]-` (Slack) | ✅ | ❌ | ✅ (T-5) | — |
   216	| 9 | `AIza` (Google) | ✅ | ❌ | ❌ | **Tier-1** |
   217	| 10 | `pplx-` (Perplexity) | ✅ | ❌ | ❌ | **Tier-1** |
   218	| 11 | `fal_` | ✅ | ❌ | ❌ | **Tier-1** |
   219	| 12 | `fc-` (Firecrawl) | ✅ | ❌ | ❌ | **Tier-1** |
   220	| 13 | `bb_live_` (BrowserBase) | ✅ | ❌ | ❌ | **Tier-1** |

exec
/bin/bash -lc "nl -ba src/adapters/llm/facade.py | sed -n '1,120p'" in /home/delangi/문서/project/category/AI_development_tool
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
/bin/bash -lc "nl -ba docs/phase0/mvp2-gp2-pass-activation-brief.md | sed -n '1,190p'" in /home/delangi/문서/project/category/AI_development_tool
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

exec
/bin/bash -lc "nl -ba docs/phase0/mvp2-full-gp2-pass-trajectory-entry-brief.md | sed -n '260,380p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
   260	- ADR-009 §2 (P1 facade MVP 진입조건) + §2.3 (Hermes PMO ≠ provider, facade 단일 진입점)
   261	- redaction-pattern-equivalence.md (R-4 설계 동등성, Hermes 안전성 선언 금지 §7.3)
   262	- 60 GP-2 detection-layer PASS brief v1.1 + 57 (β) brief v1.1 + 62 MVP-2 PASS brief
   263	- 52 entry R-A-1 (`agent/redact.py` 본 repo 부재 = upstream v0.12.0 401 LOC)
   264	- 실 자료: `src/adapters/llm/facade.py` (placeholder) + `tools/secret_scanner.py` + `secret-hygiene-egress-redaction.yml`
   265	
   266	---
   267	
   268	## §13 자기진단 (메타 편향 회피)
   269	
   270	| # | 위험 | 처리 |
   271	|---|------|----|
   272	| P-1 | full GP-2 PASS *기정사실화* | 발효 = SC-3 (SC-1 ∧ SC-2 evidence 후 합의 + 사용자 명시), 본 cycle = trajectory 진입 한정 (§0.2 #1) |
   273	| P-2 | R-1 = 본 repo 구현 가능 *오인* | §3.1 영역 분리 — `agent/redact.py` 본 repo 부재 (52 R-A-1), 직접 구현 = upstream PR (scope 외) |
   274	| P-3 | R-2 facade real *우회 구현* (TR-1 미발화) | §4.1 + (C-2) — placeholder 보존, real = SC-1 풀 3+1 합의 후 |
   275	| P-4 | prevention over-claim (R-4 = prevention 입증 *오인*) | §1.2 + (C-5) — R-4 = 설계 동등성 (Hermes 안전성 선언 금지), prevention 입증 아님 ([[feedback_pass_scope_overclaim]], 본 세션 #2 4회 cascade 교훈) |
   276	| P-5 | DESIGN repo vs runtime redaction 혼동 | §3.2 — 본 repo = 설계/검증, 실 runtime = Hermes upstream (위임) |
   277	| P-6 | sub-cycle 순서 권고 = *결정* 오인 | §5.2 + (C-1~C-3) — 권고 ≠ 결정, 사용자 명시 별도 |
   278	| P-7 | 작성자 = 60/62 작성자 (Claude) cascade | cross-vendor codex + 풀 3+1 독립 검증 (본 세션 #2 over-claim 4회 포착 입증) |
   279	| P-8 | Provider Liquidity 영향 과소 | §4.3 + (C-4) — R-2 = 5조-2 비협상 Layer 1, trigger 6 발화 |
   280	
   281	---
   282	
   283	**본 brief v1 끝.**
   284	
   285	**다음 단계**: 사용자 승인 → 풀 3+1 + 외부 LLM 1+ (codex E-α) → Reviewer 통합 → v1.1 흡수 → commit + push → **full GP-2 PASS trajectory 진입 자격 발효**. 후속: SC-1 (R-2 facade real) / SC-2 (R-1 위임 검증) / SC-3 (full GP-2 PASS 발효) = 사용자 명시 별도 sub-cycle.

codex
R-4와 facade 상태는 brief 서술과 대체로 맞습니다. 마지막으로 `agent/redact.py` 부재 및 62 MVP-2 PASS의 prevention deferred 문구를 확인해 R-1/R-2 경로 판단의 전제를 닫겠습니다.
exec
/bin/bash -lc "rg --files | rg '("'^|/)agent/redact'"\\.py"'$|src/adapters/llm/facade'"\\.py"'$|mvp2-implementation-evidence-pass-activation-brief'"\\.md"'$'"'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md
src/adapters/llm/facade.py

exec
/bin/bash -lc "nl -ba docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md | sed -n '1,130p'" in /home/delangi/문서/project/category/AI_development_tool
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
   121	
   122	→ **2/7 발화 → 풀 3+1 + 외부 LLM 1+ 적격**.
   123	
   124	---
   125	
   126	## §5 PASS 발효 권고 + 발효 시 효과
   127	
   128	⭐ **권고 = MVP-2 Implementation Evidence PASS (G4 ledger 완전 + GP-2 detection-tier, prevention/Layer 3·5/2a deferred) 발효 APPROVE WITH CONDITIONS** (B-1: 복합 자격 부착, 무수식 "MVP-2 PASS" 회피):
   129	
   130	1. **3 의존성 충족** (Layer 통합 PASS 59 + GP-2 detection-layer PASS 60 + R-S1 61) + (a)~(d) 충족.

exec
/bin/bash -lc 'rg -n "prevention|full GP-2|R-1|R-2|deferred|facade" docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
1:# MVP-2 Implementation Evidence PASS (G4 ledger 완전 + GP-2 detection-tier, prevention/Layer 3·5/2a deferred) 발효 합의 entry brief (v1.1)
5:> **v1 → v1.1 갱신**: 풀 3+1 + 외부 LLM 1+ (codex gpt-5.5 cross-vendor) 통합 합의 (`docs/review/3plus1-consensus-2026-05-28-mvp2-final-pass.md`) **APPROVE WITH CONDITIONS (4 source 전원) → BLOCKING 3 + 권고 3 1pass 흡수**. ⭐ **핵심 정정 (B-1)**: 무수식 "MVP-2 PASS" 명칭 → **복합 자격 부착** (G4 ledger 완전 + GP-2 detection-tier, prevention R-1/R-2 + Layer 3·5 + 2a deferred) — 60 GP-2 detection-layer 강등 cascade 상위 재발 방지 (β B-1 / 59 B-2 / 60 B-1 4번째). B-2 "trajectory" 진행성 완화 + B-3 citation 정정. evidence 차단급 over-claim 0. §10 흡수 매트릭스 추가.
7:> **scope**: MVP-2 Implementation Evidence PASS **발효** (G4 ledger 무결성 *완전* + GP-2 송신 redaction *detection-tier*, prevention/Layer 3·5/2a *deferred*) — MVP-2 영역 (G2 GP-2 + G4 §4.4 Layer 1+2+4) 최종 milestone. ⚠️ **full GP-2 PASS (prevention) 아님**
13:> **본 cycle 발효 효과** = **MVP-2 Implementation Evidence PASS 발효** (in-repo governance/CI 구현 evidence). **full GP-2 prevention (R-1 Hermes runtime redaction / R-2 facade real) + Layer 3+5 = MVP-2 PASS 후속 trajectory (deferred, 자동 진입 0)**
25:3. **MVP-2 PASS scope 정직 명문** — Implementation Evidence PASS (in-repo evidence) + full GP-2 prevention + Layer 3+5 = deferred trajectory (60 over-claim 교훈 답습) (§3)
35:| 2 | **full GP-2 PASS 발효** (prevention R-1/R-2 = deferred trajectory) | 0 |
37:| 4 | R-1 Hermes import / R-2 facade real (TR-1) | 0 |
63:| **GP-2 detection-layer PASS** | ✅ 60 entry (REVISE → v1.1 detection-layer reframe, 4 source) | `92e9078` | R-3 detection operative (secret-hygiene D-2 CI green) + R-4 설계 동등성 + ADR 권위. **prevention (R-1 Hermes / R-2 facade) = deferred trajectory (in-repo 입증 0, Hermes upstream 위임)** |
76:| (a) 동등 이상 보안 결과 | ✅ ledger 무결성 (hash chain + append-only + CI 회귀) | ⚠️ detection ✅ / prevention (R-1/R-2) deferred (60 답습) | ✅ ledger 완전 + GP-2 detection (prevention deferred 명문) |
82:→ **(a)~(d) = Implementation Evidence scope 충족** (B-1 정정): G4 축 (a) = 무결성 *완전* / **GP-2 축 (a) = detection + 설계 동등성, prevention (R-1/R-2) deferred** (60 답습 — full prevention 충족 아님). (e2) = 본 cycle MVP-2 통합 PASS 합의.
94:**deferred (명문, 자동 진입 0)** — ⚠️ B-2: "trajectory" 진행성 함의 회피 (R-1 = import 결정조차 미진입, R-2 = placeholder):
95:- ⚠️ **GP-2 prevention (능동 redaction)**: R-1 Hermes runtime redaction (upstream 위임, ADR-011 §2.3 #2) + R-2 facade real (TR-1) — **in-repo 입증 0 + Hermes safety 미선언** (ADR-011 §7.3 / ADR-012 §3.3 답습 — redaction-pattern-equivalence = 설계 동등성, 안전 선언 아님). R-1 import 미결정 / R-2 placeholder. **full GP-2 PASS = MVP-2 PASS 후속 (deferred)**
100:→ **MVP-2 PASS = ledger 무결성 완전 + GP-2 detection operative + 설계/CI 권위. prevention runtime + Layer 3/5 + denyNonFastForwards = solo 1-host 비례 보안 + upstream 위임 deferred (over-claim 0, 정직 scope)**.
128:⭐ **권고 = MVP-2 Implementation Evidence PASS (G4 ledger 완전 + GP-2 detection-tier, prevention/Layer 3·5/2a deferred) 발효 APPROVE WITH CONDITIONS** (B-1: 복합 자격 부착, 무수식 "MVP-2 PASS" 회피):
132:   - (C-1) **MVP-2 PASS scope = Implementation Evidence (in-repo). full GP-2 prevention (R-1/R-2) + Layer 3/5 + 2a = deferred trajectory 명문** (§3, over-claim 0)
139:- governance-preconditions §4 (GP-2): detection-layer PASS + prevention deferred cross-reference (선택)
142:→ **MVP-2 PASS 발효 자격 = 3 의존성 + (a)~(d) + (e2) 합의 APPROVE + 사용자 명시 + (C-1) deferred trajectory 명문**.
148:§0.2 답습 (12). 추가: full GP-2 PASS 자동 발효 0 / Layer 3/5 진입 0 / R-1 import 0 / R-2 facade 0 / MVP-3~6 자동 진입 0 / roadmap 본문 자동 갱신 0 (발효 후 별도) / 자동 후속 0.
154:1. 본 brief 승인 → 풀 3+1 + 외부 LLM 1+ (codex (E-α)) → Reviewer 통합 → v1.1 흡수 → commit + push → 🎉 **MVP-2 Implementation Evidence PASS 발효 (G4 ledger 완전 + GP-2 detection-tier, prevention/Layer 3·5/2a deferred — ⚠️ full GP-2 PASS 아님)**
156:3. **full GP-2 PASS trajectory** (R-1 Hermes runtime redaction import / R-2 facade real TR-1 prevention)
175:| P-2 | **MVP-2 "full PASS" over-claim (60 GP-2 over-claim 재발)** | §3 정직 scope 명문 — Implementation Evidence PASS (in-repo), full GP-2 prevention + Layer 3/5 + 2a = deferred trajectory. "runtime 완전 보증" 표현 0 |
176:| P-3 | GP-2 detection-layer 를 MVP-2 통합 시 "full GP-2" 로 격상 | §1 + §2 (a) + §3 = GP-2 detection-layer + prevention deferred 일관 명문 |
191:| B-1 ⭐ (4 source 수렴) | 무수식 "MVP-2 PASS" → 복합 자격 "(G4 ledger 완전 + GP-2 detection-tier, prevention/Layer 3·5/2a deferred)" 부착 (title + §2 결론 + §5 + §7) + "GP-2 detection-layer PASS" 고정 — 60 cascade 상위 재발 방지 | Agent C R-C-1 + Agent B R-B-1 + codex 권고 1/2/3 | title/§2/§3/§5/§7 |
192:| B-2 | "deferred trajectory" → "deferred (R-1 import 미결정 / R-2 placeholder, in-repo 입증 0 + Hermes safety 미선언)" | Agent B R-B-2 | §3 |
195:| N-2 | deferred 진입 trigger 매트릭스 | Agent C | §3 (선택) |
204:**다음 단계**: SESSION + INDEX commit + push → 🎉 **MVP-2 Implementation Evidence PASS 발효 (G4 ledger 완전 + GP-2 detection-tier, prevention/Layer 3·5/2a deferred)**. 후속: roadmap/governance MVP-2 PASS 등록 (발효 후 별도 commit) + full GP-2 PASS trajectory (R-1/R-2) = 사용자 명시 별도 cycle.

codex
1. **판정: APPROVE WITH CONDITIONS**

BLOCKING 항목: 없음.  
직접 read 기준으로 brief의 trajectory entry 한정 scope, full GP-2 PASS 미발효, R-1/R-2 별도 sub-cycle 분리는 권위 문서와 충돌하지 않습니다.

2. **권고 항목**

1. `§0.3`의 ADR-011 §2.4 T3 인용은 직접 인용과 해석을 분리하세요. 실제 ADR-011은 T3를 “Constitution / ADR / Harness Gates 정의 자체의 변경”으로만 둡니다 (`ADR-011` lines 127-133). brief line 51의 “facade real 코드 구현 ≠ T3, R-2 = TR-1 별도 trigger”는 타당한 inference로 보이나 verbatim 권위 인용은 아닙니다.

2. R-1 경로에서 “upstream 영역 / 본 repo import 0” 권고는 타당하지만, full GP-2 PASS Exit (a)는 “Hermes native redaction Tier-1 42 catalog 적용 검증”을 요구합니다 (`governance-preconditions.md` line 451). 따라서 SC-2에서 “import 0 위임 검증”을 택할 경우에도, 실행 가능한 Hermes artifact/version pin, canary evidence, R-6 재실행 조건을 반드시 evidence contract로 명문화하는 조건이 필요합니다.

3. `§5.1` line 162의 “carry-off”는 “carry-over” 오타로 보입니다. 의미 혼동 방지를 위해 정정 권고합니다.

4. `§11` line 249와 마지막 line 285의 “commit + push → trajectory 진입 자격 발효”는 사용자 명시 조건을 계속 붙여야 합니다. brief line 215에는 사용자 명시가 있으므로 모순은 아니지만, 마지막 문장에서도 같은 조건을 반복하면 over-claim risk가 줄어듭니다.

3. **NOTE**

- `src/adapters/llm/facade.py`는 실제로 placeholder입니다. `complete()`는 `NotImplementedError`이고 `health()`는 `{}`를 반환합니다 (`facade.py` lines 31-41). brief lines 132-133의 설명은 일치합니다.
- repo 내 `agent/redact.py`는 `rg --files` 결과 존재하지 않았고, `facade.py`만 확인되었습니다. R-1을 upstream/Hermes artifact 영역으로 분리한 판단은 현재 workspace 기준 타당합니다.
- prevention over-claim 방지는 잘 되어 있습니다. 60 brief도 full GP-2가 아니라 detection-layer PASS로 강등되어 있으며 (`mvp2-gp2-pass-activation-brief.md` lines 5-13, 82-105), 62 brief도 full GP-2 prevention deferred를 명시합니다 (`mvp2-implementation-evidence-pass-activation-brief.md` lines 7, 13, 94-95).

4. **권위 인용 cross-verify 결과**

| brief 주장 | 실제 문서 | 판정 |
|---|---|---|
| governance §4.5 Exit (a) = “Hermes native redaction Tier-1 42 catalog 적용 검증 + P1 facade redaction filter 검증” | `governance-preconditions.md` line 451 동일 | 일치 |
| GP-2는 로그/LLM 송신 경로만, DB INSERT 책임 없음 | `governance-preconditions.md` lines 422-424, `ADR-011` lines 112-115 | 일치 |
| ADR-011: Hermes ≠ root of trust | `ADR-011` lines 95-108 | 일치 |
| ADR-011 #2: Hermes redaction은 로그/LLM 송신 방어로만 신뢰 | `ADR-011` line 113 | 일치 |
| ADR-011 #4: Hermes 업그레이드 자동 R-2 재실행 | `ADR-011` line 115 | 일치 |
| ADR-009 §2: P1 facade MVP 조건 4개 2026-05-04 충족, 별도 트리거 없음 | `ADR-009` lines 49-62 | 일치 |
| ADR-009 §2.3: Hermes PMO는 provider 직접 소유 금지, facade 단일 진입점 | `ADR-009` lines 77-89 | 일치 |
| LiteLLM 직접 import = facade.py 한정 | `ADR-009` lines 31-33, 70 | 일치 |
| R-4 = 설계/패턴 동등성 문서, Hermes 안전성 선언 금지 | `redaction-pattern-equivalence.md` lines 29-39 | 일치 |
| R-4가 prevention 입증은 아님 | `redaction-pattern-equivalence.md` lines 33, 35-40 및 60 brief lines 92-105 | 일치 |
| R-2 facade real은 현재 미구현 placeholder | `facade.py` lines 31-41 | 일치 |

결론: 조건부 승인 가능. 차단 모순은 없고, v1.1에는 “직접 인용 vs inference” 표시와 SC-2 evidence contract 조건을 보강하는 것이 적절합니다.
tokens used
77,937
1. **판정: APPROVE WITH CONDITIONS**

BLOCKING 항목: 없음.  
직접 read 기준으로 brief의 trajectory entry 한정 scope, full GP-2 PASS 미발효, R-1/R-2 별도 sub-cycle 분리는 권위 문서와 충돌하지 않습니다.

2. **권고 항목**

1. `§0.3`의 ADR-011 §2.4 T3 인용은 직접 인용과 해석을 분리하세요. 실제 ADR-011은 T3를 “Constitution / ADR / Harness Gates 정의 자체의 변경”으로만 둡니다 (`ADR-011` lines 127-133). brief line 51의 “facade real 코드 구현 ≠ T3, R-2 = TR-1 별도 trigger”는 타당한 inference로 보이나 verbatim 권위 인용은 아닙니다.

2. R-1 경로에서 “upstream 영역 / 본 repo import 0” 권고는 타당하지만, full GP-2 PASS Exit (a)는 “Hermes native redaction Tier-1 42 catalog 적용 검증”을 요구합니다 (`governance-preconditions.md` line 451). 따라서 SC-2에서 “import 0 위임 검증”을 택할 경우에도, 실행 가능한 Hermes artifact/version pin, canary evidence, R-6 재실행 조건을 반드시 evidence contract로 명문화하는 조건이 필요합니다.

3. `§5.1` line 162의 “carry-off”는 “carry-over” 오타로 보입니다. 의미 혼동 방지를 위해 정정 권고합니다.

4. `§11` line 249와 마지막 line 285의 “commit + push → trajectory 진입 자격 발효”는 사용자 명시 조건을 계속 붙여야 합니다. brief line 215에는 사용자 명시가 있으므로 모순은 아니지만, 마지막 문장에서도 같은 조건을 반복하면 over-claim risk가 줄어듭니다.

3. **NOTE**

- `src/adapters/llm/facade.py`는 실제로 placeholder입니다. `complete()`는 `NotImplementedError`이고 `health()`는 `{}`를 반환합니다 (`facade.py` lines 31-41). brief lines 132-133의 설명은 일치합니다.
- repo 내 `agent/redact.py`는 `rg --files` 결과 존재하지 않았고, `facade.py`만 확인되었습니다. R-1을 upstream/Hermes artifact 영역으로 분리한 판단은 현재 workspace 기준 타당합니다.
- prevention over-claim 방지는 잘 되어 있습니다. 60 brief도 full GP-2가 아니라 detection-layer PASS로 강등되어 있으며 (`mvp2-gp2-pass-activation-brief.md` lines 5-13, 82-105), 62 brief도 full GP-2 prevention deferred를 명시합니다 (`mvp2-implementation-evidence-pass-activation-brief.md` lines 7, 13, 94-95).

4. **권위 인용 cross-verify 결과**

| brief 주장 | 실제 문서 | 판정 |
|---|---|---|
| governance §4.5 Exit (a) = “Hermes native redaction Tier-1 42 catalog 적용 검증 + P1 facade redaction filter 검증” | `governance-preconditions.md` line 451 동일 | 일치 |
| GP-2는 로그/LLM 송신 경로만, DB INSERT 책임 없음 | `governance-preconditions.md` lines 422-424, `ADR-011` lines 112-115 | 일치 |
| ADR-011: Hermes ≠ root of trust | `ADR-011` lines 95-108 | 일치 |
| ADR-011 #2: Hermes redaction은 로그/LLM 송신 방어로만 신뢰 | `ADR-011` line 113 | 일치 |
| ADR-011 #4: Hermes 업그레이드 자동 R-2 재실행 | `ADR-011` line 115 | 일치 |
| ADR-009 §2: P1 facade MVP 조건 4개 2026-05-04 충족, 별도 트리거 없음 | `ADR-009` lines 49-62 | 일치 |
| ADR-009 §2.3: Hermes PMO는 provider 직접 소유 금지, facade 단일 진입점 | `ADR-009` lines 77-89 | 일치 |
| LiteLLM 직접 import = facade.py 한정 | `ADR-009` lines 31-33, 70 | 일치 |
| R-4 = 설계/패턴 동등성 문서, Hermes 안전성 선언 금지 | `redaction-pattern-equivalence.md` lines 29-39 | 일치 |
| R-4가 prevention 입증은 아님 | `redaction-pattern-equivalence.md` lines 33, 35-40 및 60 brief lines 92-105 | 일치 |
| R-2 facade real은 현재 미구현 placeholder | `facade.py` lines 31-41 | 일치 |

결론: 조건부 승인 가능. 차단 모순은 없고, v1.1에는 “직접 인용 vs inference” 표시와 SC-2 evidence contract 조건을 보강하는 것이 적절합니다.
