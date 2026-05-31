# 3+1 합의 보고서 — 디딤돌1f silent semantic failure

**작성**: Reviewer (검토 에이전트) | 2026-05-31
**대상**: `docs/phase0/jarvis-stone1f-silent-semantic-failure-design-brief.md` (v1)
**입력 4 source**: Agent A(구현) + Agent B(품질/안전) + Agent C(대안) + codex(cross-vendor, gpt)
**최종 합의 판정**: **APPROVE WITH CONDITIONS** (brief v1.1 로 BL-1~10 흡수 후 구현 진입)

---

## 0. 코드 직접 검증 (Reviewer 독립 확인 — 방향 가르는 4개)

| 주장 | 검증 위치 | 결과 |
|------|-----------|------|
| HUD plan 경로 advisory 미활성 | `jarvis_plan.py:247-248` `Orchestrator(registry, ReviewGuard(), ApprovalGate(lambda r: True))` boss 인자 없음 | ✅ advise 는 `if self._boss`(orchestrator.py:138) 조건 → 미작동 |
| boss advisory 기배선("의도 부합" 평가축) | `boss.py:265-292` file 도메인 첫 축 = "의도 부합: 요청한 파일이 생성·수정됐는가" | ✅ |
| boss_plan_prompt가 worker_kind 의미 미설명 | `boss.py:388-401` enum 이름만 | ✅ 능력 설명 0 |
| HUD dogfooding이 boss에게 file-only만 제공 | `jarvis_plan.py:63` `("code","file") if real_workers else ("file",)` | ✅ |

→ Agent A "advisory 기배선"과 Agent C "feedforward 공백"은 **둘 다 사실, 서로 다른 layer** — 충돌 아님.

---

## 1. 4 source 판정 요약

| Source | 판정 | 권고 |
|--------|------|------|
| Agent A (구현) | AWC | C (advisory 경로 존재 — HUD에 boss 주입, 신규 NL 사전 0) |
| Agent B (품질/안전) | AWC | A 핵심 + C 조건부(advisory only), B 거부, D 보류 |
| Agent C (대안) | **REVISE** | 신규 E = A + E1(feedforward) + E2(능력 descriptor 매칭) |
| codex (cross-vendor) | AWC | C-prime (A 필수 + 차단은 구조적 신호만, NL은 advisory only) |

3개가 C 계열, C-agent만 REVISE(신규 E). Reviewer 종합: **세 권고가 상충이 아니라 다른 layer** → 통합이 정답.

---

## 2. 권고 방향: 다층 통합안 "F" (layer별 조합)

> brief의 A/B/C/D는 "한 지점에서 잡기" 경쟁으로 프레이밍됐으나, 교차 결과 **단일 원인(exit code = 의미 성공 가정)이 3 layer에 걸침**. 조치는 합산된다(CLAUDE.md §2 피드백 루프 계층 정합).

| Layer | 시점 | 조치 | 성격 | 수렴 |
|-------|------|------|------|------|
| **F1 feedforward** | plan 생성 前 | `boss_plan_prompt`에 worker_kind 능력 1줄("file=텍스트 생성만·실행 불가, code=실행 가능, 실행 필요시 code") | 가이드(결정적 prompt, 비용~0) | C(E1)·codex-5 + A·B 묵시 |
| **F2 결정적 검증** | plan 검증 時(승인 前) | `EXECUTING_KINDS` frozenset + 구성 invariant(실행가능 워커 0개+실행요구→거부) + boss schema `requires_execution` bool → "실행요구 subtask가 비실행 kind"면 게이트 경고 | 센서(계산적/구조적) | C(E2) 주도, B §5-2 수렴 |
| **F3 정직 표시** | 승인 게이트 + 완료 라벨 | COMPLETED/applied 의미를 "exit0+반영, 의미달성 아님"으로 정직화(controller+orchestrator+HUD label/card) | 투명성(결정적) | **4/4 필수** |
| **F4 advisory** | dispatch 後 | HUD plan 경로에 boss 주입 → 기배선 "의도 부합" advisory를 subtask 카드 표시(scrub 경유, 차단 아님) | 센서(추론적 보조) | A 주도, B/codex 조건부 |

**기각**: 후보 B(NL desc 휴리스틱 *차단*) = **4/4 만장일치 기각**(§2 위반, false neg 필연 — 탐지는 F2 구조적 선언으로 대체). 후보 D(전면 재설계) 보류(단 D 근본성을 frozenset+bool로 비례 달성 → F2 흡수).

**우선순위(§2 계산적 우선)**: F3 = F2 > F1 > F4.

---

## 3. 교차 비교

### ① 일치 (Consensus 4/4)
| 항목 | 근거 |
|---|---|
| 후보 B(NL 차단) 거부 | A·B(B-2)·C·codex(BL2) **만장일치**. NL 휴리스틱 false neg 필연 → "잘못 불가능" 불성립 |
| 후보 A 라벨 "file=텍스트만" 부정확 | B-1·codex-1·C-⭐5 (3/4). worker.py output_filename write 잔여(ADR-013 §2.2 자인) |
| COMPLETED/applied 정직화 필요 | 4/4. 문서뿐 아니라 controller+orchestrator+HUD label/card |
| scope = file 한정 아님, code 동형 갭(#3) | 4/4 |
| 완전 해결 불가(결정 불가 본질) | 4/4 + brief §3 자인 |
| boss_plan_prompt worker_kind 의미 미설명 | C(E1)·codex-5 직접 + 코드 실증 |

### ② 부분 일치 (Partial)
- **P-1** advisory(F4): A 적극 / B·codex 조건부(표시만) / C 구조선언 우선 → **양립**(다른 layer).
- **P-2** 발견#2 ledger: A·codex "별건" / B "동반 권장" → **동반 fix**(사용자 Q3 결정).
- **P-3** ADR-013 소급: B·C "보강" / A "보안만 주장해 불요, 개념갭 미문서화" → **§6 보강**.
- **P-4** COMPLETED 정직화 범위: codex-3 가 controller+orchestrator+HUD 전체 / 나머지 더 가볍게 → **codex-3 채택**(코드 실측상 다지점).

### ③ 불일치 (Divergence)
| 쟁점 | 갈림 | Reviewer 판단 | 사용자 결정 |
|---|---|---|---|
| requires_execution(E2) 시점 | C=1f포함 / B=보류 / A=거부(과잉) / codex=구조신호 차단만 허용 | 후속 분리 권고(feedforward가 더 즉효) | **1f 포함**(Q1=(a)+(b), §2 원칙 우선) |
| advisory 위치 | codex=ReviewGuard 확장 금지·PlanController/HUD 분리 / A=HUD에 boss 주입 | **codex 채택** | F4 표시전용 채택(Q2) |

### ④ 누락 (Gap — 단일 source)
- **G-1** ⭐ HUD dogfooding 구성 오류 — boss에 file-only 옵션만 줘서(jarvis_plan.py:63) 실행 작업이 *애초에 성공 불가 구성*(C-agent ⭐4) → **채택, §1 정직 단서 명기**.
- **G-2** requires_execution = ends 속성(argv 아님)이라 PLAN-INV 위반 아님(C) → F2 정당화.
- **G-3** ReviewGuard semantic 확장 금지(codex-4) → F2=PlanController, F4=HUD 분리.
- **G-4** advisory scrub 의무(B-5) → F4 조건.

---

## 4. 핵심 통합 통찰
**Agent A와 C는 충돌하지 않는다 — 같은 코드의 다른 layer.** brief 오류 = A/B/C/D를 상호배타 경쟁으로 둔 것. 단일 원인(exit code=의미성공, orchestrator.py:130)이 3 layer에 걸치고 각 조치(F1~F4)는 합산. 가장 싼 layer(F1, ~0ms 가이드)부터 채우고 결정적 센서(F2) 얹고 투명성(F3) 깔고 추론적 보조(F4)로 마감.

---

## 5. BLOCKING 목록 (brief v1.1 흡수)

| # | BLOCKING | 출처 | 흡수 |
|---|----------|------|------|
| **BL-1** | 후보 A 라벨 "file=텍스트만" 부정확 | B·codex·C (3/4) | "현 HUD file alias = writer 없는 OllamaWorker(output_filename=None) → 파일 미작성, 배선 의존" ADR-013 §2.2 답습 |
| **BL-2** | 후보 B 차단 권한 = §2 위반 | B·codex (4/4) | B "차단" 폐기, 탐지는 F2 구조적 선언으로 대체(결정적). NL은 F4 표시만 |
| **BL-3** | feedforward(F1) 누락 — 후보공간 편향 | C·codex | §4를 layer 통합안(F1~F4)으로 재구성, boss_plan_prompt 능력 1줄 1f 포함 |
| **BL-4** | COMPLETED 정직화 범위(문서만 부족) | codex | controller(PlanStatus/status)+orchestrator(OutcomeStatus)+HUD(label/tooltip/card) |
| **BL-5** | advisory 책임 분리 | codex·A | ReviewGuard 불변, 기존 orchestrator.advise + HUD plan 카드 재사용 |
| **BL-6** | scope=code 워커 동형 명문화 | 4/4 | §5-5 "file=capability absence, code=execution protocol absence, 근본 동일" + applied 라벨 worker_kind-무관 일반화. #3 결정적 차단은 후속(Q4) |
| **BL-7** | §1 정직 단서 — 실측이 file-only 구성에도 기인 | C-agent ⭐4 | jarvis_plan.py:63 file-only dogfooding 구성 명기 |
| **BL-8** | E2(requires_execution) = D의 비례적 대안 | C | 1f 포함(사용자 Q1=(a)+(b)). ends 속성이라 PLAN-INV 위반 아님(G-2) |
| **BL-9** | ADR-013 produce 사각지대 미문서화 | B·C | ADR-013 §6에 "능력 경계=consume 안전만, produce 적합성 미보장" 1줄. §7 의존: ADR-011 §2.1 교차확인(영향 0) |
| **BL-10** | 발견#2 ledger 이중기록 = detection 기준선 오염 | B-3 | 1f 검증 *선행* fix(plan_approved 중복 제거) |

---

## 6. 사용자 결정 (2026-05-31 확정)

| Q | 질문 | 결정 |
|---|------|------|
| **Q1** | F2(결정적 능력 검증) 범위 | **(a)+(b) 둘 다** — EXECUTING_KINDS frozenset + 구성 invariant + requires_execution bool |
| **Q2** | F4(boss advisory) 채택 | **채택, 표시 전용**(HUD boss 주입, scrub 경유) |
| **Q3** | 발견#2 ledger 이중기록 | **1f 동반 fix** |
| **Q4** | 발견#3 code 되묻기 | **별건 후속**(F3 정직표시는 #3 공통 커버) |
| **Q5** | ADR 처리 | **ADR-013 §6 보강(1줄)** — 신규 ADR 안 만듦([[feedback_ceremony_inflation]]) |

→ **F1~F4 전부 + E2 구조필드 채택**(가장 견고). Reviewer는 E2 후속 분리 권고했으나 사용자가 §2 "계산적 우선" 원칙을 강하게 따라 1f 포함 결정.

---

## 7. 정직 단서 (합의 자체의 한계)
- **검증 범위**: 방향 가르는 4곳(boss_plan_prompt·orchestrator.advise 게이팅·plan_controller.run·plan schema)을 Reviewer 직접 재확인. 나머지 라인 번호는 source 신뢰 — **불일치 다수**(예: advise 434-478/434-481, jarvis_plan.py:247 vs 63). v1.1 작성 시 라인 전수 재확인 필요.
- ⚠️ **F2 핵심 미검증 가정**: `requires_execution`이 약한 boss(OllamaBoss)에서 신뢰성 있게 생성되는지 **미실측**. 94 dogfooding("약한 boss는 contracts 거의 미생성")상 requires_execution도 누락 가능 → default False면 silent pass 재발. **→ F2(a) 결정적 효과가 약한 boss에서 제한될 수 있고, 그땐 F1(feedforward)+구성 invariant(b)+F4가 실질 방어. 구현 시 dogfooding 재검증 필수.**
- **A의 "advisory 100% 배선"은 부분 과장**: advise는 orchestrator.dispatch 안 `if self._boss` 조건. plan 경로(controller)는 advise를 직접 호출 안 함(BL-5 non-adaptive). "boss 주입만 하면 됨"은 맞으나 "100% 배선"보다 "경로 존재, 활성화 미배선".
- **"해결" 아님**: F1~F4 전부 채택해도 "워커가 의미적으로 옳은 일 했는가"는 일반적 결정 불가(§3 유지). "흔한 불일치 결정적 표시/예방 + 나머지 정직 노출"이며 "silent failure 해결"로 부르면 over-claim.
- **비례성 경계**: F2 schema 변경(requires_execution)이 frontier(1d CliPlanner)/human(1e HumanPlanner) plan shape에 미치는 영향 미검증 — 구현 시 회귀 확인.
- 합의는 **방향**만 정함. TDD 구현·커버리지·회귀는 별도 단계.
