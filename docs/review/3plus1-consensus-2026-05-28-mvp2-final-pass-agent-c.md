# Agent C (대안 탐색가) 독립 분석 — MVP-2 Implementation Evidence PASS 발효 (62 entry, 최종 milestone)

> **관점**: "MVP-2 PASS 발효 형태가 최선인가? 더 정직한/더 나은 명칭·구조·판단이 있는가?"
>
> **검토 대상**: `docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md` (v1, §0~§9)
> **입력**: 32 entry MVP-1 PASS 발효 합의 (PASS 형태 답습) + 60 GP-2 detection-layer PASS reframe 합의 (명칭 강등 선례) + 59 Layer 통합 PASS brief + roadmap-mvp1 §1.3/§2.2
> **독립성**: Agent A/B 및 외부 LLM (codex) 응답 미참조. 본 분석 = filesystem + git log + 권위 문서 direct verify + 대안 매트릭스 기반.
> **작성**: 2026-05-28 (Agent C 단독)

---

## §0 verdict

**APPROVE WITH CONDITIONS**

brief 의 PASS 발효 형태(권고 = "MVP-2 Implementation Evidence PASS 발효 APPROVE WITH CONDITIONS + (C-1) deferred trajectory 명문")는 32 entry MVP-1 PASS 발효 형태와 **형태(verdict 종류 + 풀 3+1 + 조건부) 차원에서 일관**하며, 발효 형태 4 대안 ((a) 무조건 APPROVE / (b) full GP-2 선행 REVISE / (c) detection-tier 강등 / (d) G4·GP-2 분리 발효) 중 **brief 채택안이 dominant** 이다. 3 의존성 commit (`0f49eb9`/`92e9078`/`bb59342`) 전수 direct verify 통과 (§1).

단 **핵심 BLOCKING 1건**: 60 entry 가 "GP-2 PASS" → "**GP-2 detection-layer PASS**" 로 명칭을 강등한 직접 선례가 있음에도, 그 강등된 GP-2 를 *구성 요소로 포함하는* MVP-2 의 명칭은 무수식 "**MVP-2 Implementation Evidence PASS**" 그대로다. **하위 구성요소가 detection-layer 한정인데 상위 milestone 명칭이 그 한정을 흡수하지 않으면, 60 이 차단한 framing over-claim 이 한 layer 위에서 재발한다** (β B-1 / 59 B-2 / 60 B-1 framing over-claim cascade 의 4번째 재발 risk). 정정은 명칭 1건의 자격(suffix) 추가이며 발효 자격을 약화하지 않고 *정직성을 강화*한다 (1pass 흡수 가능, 별도 v2 cycle 불요).

- **BLOCKING: 1건** (R-C-1)
- **권고: 3건** (N-C-1 ~ N-C-3)
- **NOTE: 3건** (NT-C-1 ~ NT-C-3)

---

## §1 사실 기반 direct verify (대안 판단 전)

대안 판단의 사실 기반 확보를 위해 brief §1 의 3 의존성 + 명칭 선례를 read-only direct 검증했다 (Agent C 독립):

| brief 주장 | verify 방법 | 결과 |
|----------|----------|------|
| 의존성 1: Layer 1+2+4 통합 PASS `0f49eb9` | `git log --oneline -1 0f49eb9` | ✅ "59번째 entry — Layer 1+2+4 통합 Implementation Evidence PASS 발효 (e2)" 일치 |
| 의존성 2: GP-2 detection-layer PASS `92e9078` | `git log --oneline -1 92e9078` | ✅ "60번째 entry — **GP-2 detection-layer PASS** 발효 ... REVISE → v1.1 (**detection-layer reframe**)" — **명칭 강등 commit 확정** |
| 의존성 3: R-S1 정정 `bb59342` | `git log --oneline -1 bb59342` | ✅ "61번째 entry — R-S1 cross-reference 정정 ... Reviewer-only 단축 APPROVE" 일치 |
| 3 의존성 = 현 branch head 직속 chain | `git log --oneline -8` | ✅ `bb59342`(head=61) ← `92e9078`(60) ← `0f49eb9`(59) 선형 |
| 59 명칭 = 무수식 "통합 PASS" (Layer 3+5 = "부분 답습") | 59 commit msg + brief §0.2 #3 | ✅ Layer 3+5 미충족을 "부분 답습" framing 으로 흡수 (suffix 무, scope 명문으로 처리) |
| 60 명칭 = "detection-layer" suffix 강등 | 60 commit msg + 합의 §3 B-1 | ✅ "GP-2 PASS" + "(a) ✅" = over-claim → suffix 강등 (명칭 차원 정정) |
| roadmap-mvp1 §2.2 line 141 "부분 PASS 처리 (부분 발효)" 개념 존재 | direct read | ✅ "어느 한쪽 미충족 시 ... Implementation Evidence PASS *부분 발효*" 명문 — 구조적 분리 어휘 선례 보유 |
| MVP-1 PASS 명칭 = "*완전 발효* (α)" 수식 보유 | roadmap-mvp1 line 143 | ✅ MVP-1 도 milestone 명칭에 자격 수식("완전 발효 (α)") 부착 선례 |

→ **brief §1 citation = 전수 실증 (over-claim 0, P-5 clean)**. 대안 판단의 사실 기반 확보. 핵심 발견: **60 의 명칭 강등은 commit 레벨로 확정된 직접 선례**이며, **roadmap 은 이미 "부분 발효" 라는 분리 어휘를 보유**한다 — R-C-1 명칭 정정의 선례 근거 두 축 확보.

---

## §2 BLOCKING

### R-C-1 ⭐⭐ — 명칭 비일관: 60 이 "GP-2 PASS"→"GP-2 detection-layer PASS" 로 강등한 한정이, 그 GP-2 를 포함하는 상위 milestone 명칭 "MVP-2 Implementation Evidence PASS" 에 흡수되지 않음 (framing over-claim cascade 4번째 재발 risk)

**근거 (direct verify + 선례 논리)**:

- 60 합의 §3 B-1 (3-way consensus, codex + Agent B + Agent C): "GP-2 (full) PASS" + "(a) ✅" = over-claim → **명칭 차원** 에서 "GP-2 **detection-layer** PASS" 로 강등. 강등 사유 = "prevention (R-1/R-2) 부재를 detection 으로 대체하는 framing over-claim, evidence 실증이나 *명칭*이 scope 과장". 이 강등은 `92e9078` commit 으로 확정.
- 본 MVP-2 brief 는 GP-2 를 정확히 그 강등된 형태("GP-2 **detection-layer** PASS", §1 의존성 2 + §3)로 포함한다. 즉 **MVP-2 = Layer 통합 PASS (완전) + GP-2 *detection-layer* PASS (한정) + R-S1**.
- 그러나 brief §3/§5/title 의 상위 milestone 명칭 = 무수식 "**MVP-2 Implementation Evidence PASS**". MVP-2 의 한 축(GP-2)이 detection-tier 한정인데, 그 한정이 milestone 명칭에 *반영되지 않는다*.

**문제점 (60 강등 논리의 직접 cascade)**: 60 이 차단한 것은 "evidence 는 실증이나 *명칭*이 prevention 부재를 가린다" 였다. MVP-2 명칭이 무수식이면, **"MVP-2 PASS" 라는 label 만 읽는 후속 reader (roadmap 등록 후 미래의 자기 자신 포함)는 GP-2 prevention 이 충족된 것으로 오독**한다. 60 이 GP-2 한 layer 에서 막은 over-claim 이, MVP-2 라는 한 layer 위에서 그대로 재상속된다. brief §9 P-2/P-3 가 *본문 scope 명문*으로 이를 다루나 — **명칭 자체는 본문보다 멀리·오래 인용**된다 (commit msg, roadmap row, INDEX, 미래 cycle 의 "MVP-2 PASS 답습"). 60 의 교훈은 정확히 "본문 scope 명문으로 부족, *명칭* 차원에서 강등하라" 였다 (그래서 commit msg 까지 detection-layer 가 박힘).

**이 정정이 발효를 약화하지 않고 *강화*하는 이유** (Agent C 핵심 판단):
- 무수식 "MVP-2 PASS" → 미래 reader 의 over-read 여지 + 60 강등 선례와 명칭 비일관 (왜 GP-2 는 강등하고 그것을 포함한 MVP-2 는 안 하는가 라는 논리 균열).
- 자격 부착 → **GP-2 강등(60)이 상위로 일관 전파**되어 chain 전체 framing 정합. MVP-1 도 "*완전 발효* (α)" 수식을 붙인 선례(roadmap line 143) — milestone 명칭에 자격을 붙이는 것은 *이미 본 프로젝트 표준*이다.

**정정 (조건 처리 흡수, 별도 v2 cycle 불요) — 3 옵션 중 택1**:
- **옵션 1 (권장)**: 상위 명칭은 "**MVP-2 Implementation Evidence PASS**" 유지하되, 발효 시 **명문 자격 suffix 를 *명칭과 동격으로* 고정** — "MVP-2 Implementation Evidence PASS **(G4 ledger 완전 + GP-2 detection-tier 한정, prevention/Layer 3·5 deferred)**" 를 title + §5 권고 + 발효 commit msg + roadmap row 의 *명칭 옆 고정 수식*으로 박는다. 60 의 commit-level 강등과 동형 (명칭이 단독 인용돼도 한정이 따라감).
- **옵션 2**: 명칭 자체를 "**MVP-2 detection-tier Implementation Evidence PASS**" 로 강등 (60 의 "GP-2 detection-layer PASS" 와 완전 평행). 단 G4 ledger 축은 detection 이 아니라 *무결성 완전* 이므로 "detection-tier" 가 MVP-2 *전체*를 수식하면 G4 축을 과소 표현 (부정확) → 옵션 1 우월.
- **옵션 3 (기각)**: 본문 scope 명문만 유지 (현 brief §3/§9) — 60 교훈이 정확히 이를 불충분으로 판정했으므로 채택 불가.

→ **MVP-2 PASS 발효 자격 자체 = 유지** (3 의존성 + (a)~(d) + (e2) 충족, R-C-1 은 발효 *명칭*의 정직성 정정). 정정 = title + §5 + 발효 commit msg + roadmap row 의 명칭 수식 1건. APPROVE WITH CONDITIONS 의 신규 조건 (C-3) 으로 흡수.

---

## §3 권고 (N-C-N)

### N-C-1 — PASS 발효 형태 4 대안 매트릭스: brief 채택안 = dominant (32 + 60 일관)

임무 1 (발효 형태 대안) 검토 결과. brief 가 발효 *형태* 대안 매트릭스를 명문화하지 않았으므로(NT-C-1 누락 답습), 본 권고가 그 공백을 메운다:

| 대안 | 평가 | 기각/채택 근거 |
|------|------|------------|
| **(a) 무조건 APPROVE (조건 0)** | ❌ 기각 | 32 entry / 59 / 60 모두 "APPROVE WITH CONDITIONS". 조건 0 = (C-1) deferred trajectory 명문 + R-C-1 명칭 정정을 누락 → 60 over-claim 재발 직격. 답습 비일관 |
| **(b) full GP-2 prevention 선행 REVISE** (R-1 Hermes import / R-2 facade real 후 MVP-2 PASS) | ❌ 기각 | 본 repo = DESIGN/governance repo (60 §1.2), 실 runtime redaction = Hermes upstream 위임 (ADR-011 §2.3 #2). R-1 import / R-2 facade real = 별도 trajectory + Provider Liquidity·비례 보안 영역. prevention 선행 강제 = (i) DESIGN repo 에서 입증 불가능한 것을 gate 로 삼음 + (ii) ceremony-inflation + (iii) 60 이 이미 "detection-layer PASS = 정당, prevention deferred" 로 합의 발효한 결론을 뒤집음. 기각 |
| **(c) "MVP-2 detection-tier PASS" 전면 강등** | ⚠️ 부분 타당하나 부정확 | 60 평행성은 매력적이나, MVP-2 의 G4 ledger 축 = detection 아닌 *무결성 완전* (Layer 1+2+4 operative). "detection-tier" 가 MVP-2 *전체* 수식 = G4 축 과소 표현. → R-C-1 옵션 1 (G4 완전 + GP-2 detection-tier 한정 *복합* 수식) 이 정확. 단 *명칭 자격 부착 필요성* 자체는 타당 (R-C-1 채택) |
| **(d) G4 부분 + GP-2 부분 분리 발효** | ❌ 기각 | G4 Layer 통합 PASS = 59 에서 *이미 단독 발효*(`0f49eb9`), GP-2 detection-layer PASS = 60 에서 *이미 단독 발효*(`92e9078`). MVP-2 PASS = 이 둘을 *통합 milestone* 으로 묶는 행위 (32 가 GP-3+GP-5 를 MVP-1 으로 통합 발효한 것과 동형). 재-분리 = 59/60 답습 무효화 + ceremony-inflation. 기각 |

→ **brief 채택안 (APPROVE WITH CONDITIONS + deferred trajectory 명문) = 32 + 59 + 60 형태 일관, dominant**. R-C-1 명칭 정정 1건 추가 외 발효 형태 변경 불요. 권고: brief §5 또는 §4 에 위 4 대안 기각 근거 1 매트릭스 명문 (후속 동형 milestone 시 표준).

### N-C-2 — deferred trajectory 처리: "deferred" 평면 나열 vs 구조화 — 현 brief 의 평면 나열 정당, 단 "MVP-2.5" 같은 신규 milestone 신설은 기각

임무 3 (deferred trajectory 처리 대안) 검토:

brief §3 = deferred trajectory 를 4 항목 평면 나열 (① GP-2 prevention R-1/R-2 / ② Layer 2a denyNonFastForwards / ③ Layer 3+5 / ④ R-5 base64). 대안 = 이를 별도 milestone (예 "MVP-2.5" 또는 "full GP-2 PASS milestone") 으로 구조화.

| 처리안 | 평가 | 근거 |
|------|------|------|
| **평면 나열 (현 brief)** | ✅ 채택 | 4 항목이 *이질적 trajectory* (R-1/R-2 = Hermes upstream + facade / 2a = bare-server 배포 trigger / Layer 3+5 = RECOMMENDED→MANDATORY multi-host / R-5 = G3-4 MVP-3 분리). 단일 후속 milestone 으로 묶을 *공통 진입 조건 부재*. 각자 *다른 trigger* 로 별도 cycle 진입 → 평면 나열이 정직 |
| **신규 "MVP-2.5" milestone 신설** | ❌ 기각 | (i) 4 항목 trigger 이질 → 인위적 묶음 = ceremony-inflation / (ii) roadmap MVP-N 체계(MVP-3~6 = 다른 GP/G 영역, roadmap-mvp1 line 90)와 충돌 — MVP-2.5 = 체계 외 신규 layer 도입 / (iii) [[feedback_ceremony_inflation]] 위반. 단 *어휘* 차원에서는 roadmap §2.2 line 141 "부분 발효" 선례가 이미 "한 GP 미충족 = 부분 처리" 어휘 보유 → 신규 milestone 불요, R-C-1 명칭 자격으로 충분 |
| **trajectory 별 trigger 명문 강화** | ⚠️ 권고 | 현 brief §3/§7 이 "자동 진입 0 (사용자 명시)" 만 명문. *각 deferred 항목의 진입 trigger* (R-1 = Hermes import 결정 / 2a = bare-server 배포 / Layer 3 = RECOMMENDED→MANDATORY 전환 / R-5 = MVP-3) 를 1 매트릭스로 명문하면 "deferred 가 영구 방치"로 오독되는 것을 차단. 권고 (비차단) |

→ **deferred trajectory = 평면 나열 채택 (구조화 신규 milestone 기각)**. 권고: §3 또는 §7 에 deferred 4 항목별 *진입 trigger* 1 매트릭스 추가 (영구 방치 오독 차단). R-C-1 명칭 자격이 "한정 PASS" 임을 명칭에 박으므로 deferred 의 존재 자체는 명칭으로 신호됨.

### N-C-3 — 비례성 / ceremony: 본 MVP-2 최종 PASS cycle 풀 3+1 = 과잉 아님 (비례성 PASS), 단 roadmap 등록은 발효 *후* 별도 commit 유지가 정확

임무 4 (비례성 / ceremony) 검토:

- [[feedback_ceremony_inflation]] / [[feedback_meta_cycle_warning]] self-check: 본 cycle = "정정의 정정" 아닌 **실 milestone (MVP-2 최종 PASS, 32 MVP-1 PASS 동형)**. 59(Layer)→60(GP-2)→61(R-S1)→62(MVP-2 통합) = 선형 진행 (meta-cycle 차수 0). 3 의존성이 *각자 별도 발효* 된 것을 *통합*하는 최종 milestone = ceremony 아닌 실 결정.
- 풀 3+1 + 외부 LLM 1+ 정당화: brief §4.2 trigger 1(큰 결정 = MVP-2 최종 PASS) + trigger 5(cross-vendor) 발화. 32 entry 도 동형. 헌법 5조-2 cross-vendor. **단 Claude 단독 cascade risk(brief P-4)** = 59/60 에서 framing over-claim 을 codex/Agent 가 포착한 process 가치 실증 → 본 cycle 도 R-C-1 (명칭 over-claim) 포착이 그 가치 증명. → **과잉 ceremony 아님, 풀 3+1 정당**.
- **roadmap 등록 시점**: brief (C-2) = "roadmap/governance MVP-2 PASS 등록 = 발효 후 별도 commit (사용자 명시)". 32 entry 도 동형 (합의 = 자격 인정, roadmap 본문 갱신 = 후속 단계). → **정확** (발효 = 합의 APPROVE + 사용자 명시, roadmap 본문 = 별도). 단 R-C-1 채택 시 roadmap row 명칭에도 자격 suffix 가 박혀야 함 (등록 단계로 carry).
- **더 가벼운 경로 존재 여부**: 3 의존성이 *모두 별도 발효 완료* 된 상태에서 MVP-2 통합 = 실질 신규 판단 = "(e2) 통합 발효 합의 + 명칭 정직성(R-C-1)" 뿐. 그럼에도 풀 3+1 유지는 (i) 최종 milestone = 최고 ceremony 등급 + (ii) cross-vendor 의무 + (iii) cascade risk 회피로 정당. **경로 단축 불요, 현 형태 채택**.

---

## §4 NOTE (NT-C-N, 참고 한정)

### NT-C-1 — *발효 형태* 대안 매트릭스가 brief 에 부재 (59 와 동일 누락 답습)

59 activation brief 도 발효 형태 대안 매트릭스 부재(59 Agent C NT-C-1)였고, 본 MVP-2 brief 도 동일 누락. N-C-1 의 4 대안 기각 근거가 그 공백을 메운다. 후속 동형 milestone PASS 발효 시 §5 에 발효 형태 대안 매트릭스 표준 포함 권고. 본 cycle = N-C-1 로 충분 (별도 cycle 불요).

### NT-C-2 — "Implementation Evidence" prefix 는 60 over-claim 의 *부분* 방어막 (단 GP-2 detection 한정까지는 미흡)

brief 가 milestone 명칭에 "**Implementation Evidence**" prefix 를 일관 부착한 것 자체가 "runtime 보증 아닌 in-repo 구현 evidence" 라는 1차 over-claim 방어막이다 (P-2 처리). 이는 *적절*하며 MVP-1 명칭(roadmap line 143)과 일관. 단 이 prefix 는 "runtime vs in-repo" 축만 방어하고, **"GP-2 prevention vs detection" 축(R-C-1)은 방어하지 못한다** — 두 over-claim 축이 독립이므로 prefix 만으로 R-C-1 해소 불가. R-C-1 = prefix 와 *별개*의 명칭 자격 필요. NOTE 한정 (R-C-1 이 본 발견 흡수).

### NT-C-3 — GP-2 detection-layer ↔ MVP-2 detection-tier 어휘 통일 권고 (혼선 차단)

60 = "detection-**layer**", 본 R-C-1 옵션 2 후보 = "detection-**tier**", brief task 문 = "detection-tier". 동일 개념(prevention 부재, detection 한정)에 layer/tier 2 어휘 병존 = 향후 cross-reference 혼선 risk (R-S1 numbering divergence 와 동형 risk). 권고: R-C-1 채택 시 60 의 "detection-layer" 어휘로 통일 (GP-2 detection-layer 를 포함 → MVP-2 의 GP-2 축도 "detection-layer 한정"). 발효 commit msg + roadmap row 에서 동일 어휘. NOTE 한정 (어휘 통일, 결정 아님).

---

## §5 자기진단 (메타 편향 회피)

| # | 위험 | 처리 |
|---|------|----|
| C-P-1 | Agent C 가 발효 형태/명칭 변경을 *과도 제안* (대안 탐색가 편향) | N-C-1 = 4 대안 *기각* 결론 (brief 채택안 dominant 확인). N-C-2 = 신규 milestone *기각*. 변경 제안 = R-C-1 명칭 자격 1건 한정 (발효 자격 불변) |
| C-P-2 | R-C-1 (명칭 강등)이 MVP-2 발효를 *뒤집는* 것으로 오해 | §2 명시 = 발효 자격 유지·정직성 강화 (60 의 GP-2 강등이 발효를 막지 않은 것과 동형). PASS 발효 비차단 |
| C-P-3 | R-C-1 명칭 주장이 추론적 (선례 부재) | direct verify: `92e9078` commit msg = "GP-2 detection-layer PASS" + "detection-layer reframe" (명칭 강등 commit-level 확정) + roadmap line 143 "완전 발효 (α)" (milestone 명칭 자격 선례). 계산적 근거 |
| C-P-4 | Agent C = 59/60/61 작성자(Claude) cascade | filesystem + git log + 권위 문서 direct (brief 주장 재현 검증), cross-vendor codex 병렬 (60 에서 codex 가 GP-2 명칭 over-claim 주도 포착한 process 답습) |
| C-P-5 | ceremony-inflation self (본 합의·R-C-1 자체가 과잉?) | N-C-3 = 비례성 PASS (최종 milestone + cross-vendor, meta-cycle 차수 0). R-C-1 = 명칭 1건 1pass 흡수 (별도 cycle 0) = 비-inflation |

→ **자기진단 5/5 통과**.

---

## §6 결론 요약

- **verdict: APPROVE WITH CONDITIONS**
- **BLOCKING 1**: R-C-1 (명칭 비일관 — 60 의 "GP-2 detection-layer PASS" 강등이 상위 "MVP-2 Implementation Evidence PASS" 명칭에 흡수되지 않아 framing over-claim cascade 4번째 재발 risk. 정정 = title + §5 권고 + 발효 commit msg + roadmap row 에 "G4 ledger 완전 + GP-2 detection-tier 한정, prevention/Layer 3·5 deferred" 명칭 자격 부착 [옵션 1 권장]. 발효 자격 불변, 정직성 강화, 1pass 흡수)
- **권고 3**: N-C-1 (발효 형태 4 대안 기각 근거 = 32+59+60 일관, brief 채택안 dominant) + N-C-2 (deferred trajectory = 평면 나열 채택, 신규 milestone 기각, 단 항목별 진입 trigger 매트릭스 권고) + N-C-3 (비례성 PASS, roadmap 등록 = 발효 후 별도 commit 정확)
- **NOTE 3**: NT-C-1 (발효 형태 대안 매트릭스 누락) + NT-C-2 ("Implementation Evidence" prefix = over-claim 부분 방어막, GP-2 detection 축은 R-C-1 별도 필요) + NT-C-3 (detection-layer/tier 어휘 통일 권고)
- **명칭 판단 (임무 2 핵심)**: 무수식 "MVP-2 Implementation Evidence PASS" = **불충분** (60 강등 선례와 명칭 비일관). 단 전면 "detection-tier" 강등(옵션 2)도 부정확 (G4 ledger 축 = 무결성 완전, detection 아님) → **복합 자격(G4 완전 + GP-2 detection-tier 한정)** 부착(옵션 1)이 정직·정확. 60 의 commit-level 강등 + MVP-1 "완전 발효 (α)" 수식 = 두 선례가 명칭 자격 부착을 표준화.
- **발효 형태 판단**: brief 채택안 = 32 entry MVP-1 PASS + 59 + 60 과 **형태 일관, dominant**. 더 나은 발효 *형태* 미발견. R-C-1 명칭 정정 1건 (별도 v2 cycle 불요, 1pass 흡수 가능).

**본 Agent C 분석 끝.**
