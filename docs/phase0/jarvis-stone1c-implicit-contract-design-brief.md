# Jarvis 디딤돌1c 설계 brief — depends_on 암묵 contract (하네스 흡수) (v1.1)

> **본 brief = 설계 정리 한정.** staged: brief v1 → **3+1 합의(4 source, AWC)** → **brief v1.1(본 문서, BLOCKING 4 + §7 Q 결정)** → 디딤돌1c TDD 구현. 코드 전 문서 먼저(SDD).

---

**작성일**: 2026-05-30
**Status**: **v1.1 — 3+1 합의(AWC, 4/4) 흡수(BLOCKING 4) + §7 Q1~Q6 사용자 결정(2026-05-30, Q2 transitive 통일). 디딤돌1c TDD 구현 진입 승인됨**
**진입 단위**: 디딤돌1b(명시 Contract) → **암묵 contract** — controller 가 `depends_on` 에서 데이터 전달을 추론(boss 가 Contract 를 안 내도 선행 산출물 자동 전달).
**상위 문서**: `jarvis-stone1b-artifact-contract-design-brief.md` (v1.1) · `ADR-013` · `docs/sessions/SESSION_2026-05-30.md` 94 entry (dogfooding)
**합의 보고서**: `docs/review/3plus1-consensus-2026-05-30-jarvis-stone1c-implicit-contract.md`
**근거**: **dogfooding 실측**(94 entry — 약한 boss contracts 거의 미생성, depends_on 일관 생성) · CLAUDE.md §2 (**모델 의존 대신 하네스 흡수**) · `feedback_boss_role_not_smartest` · `feedback_pass_scope_overclaim` · `feedback_proportionate_security_personal_tool` · `ADR-011` §2.1

---

## v1.1 변경 이력 (3+1 합의 흡수 + 사용자 결정)

| # | v1 → v1.1 | 출처 |
|---|---|---|
| 🔴 BL-1 ⭐ | **능력 경계 "실 부작용 0" 정밀화** — `OllamaWorker` 는 `output_filename` 설정 시 **workdir 단일 파일 write 경로** 있음(worker.py:358-393). "fs 실행 능력 경로 부재"는 부정확 → **"임의 명령/경로 실행 0 + workdir 단일 파일 산출 잔여"**. consume-safe = file alias 가 *writer 없는* OllamaWorker 임을 harness 불변식으로. **1b §1·ADR-013 §2.2/§4 소급 보강.** | B·codex |
| 🔴 BL-2 | **회귀 범위 확장** — `test_no_contracts_behaves_like_1a`(1b) 외 `test_plan_controller.py` code+depends_on 다수가 능력 경계 충돌로 VALIDATION_FAILED. → `_build` 에 `implicit_contracts=False` 격리 + 신규 1c 테스트 | A·codex |
| 🔴 BL-3 | **dedup** — 명시+암묵 같은 `(produced_by, consumer)` 이중 주입 방지. dedup 키=`(produced_by, consumer)`, 명시 커버 시 암묵 suppress | A·B·codex |
| 🔴 BL-4 | **계획 게이트에 합성 암묵 contract 표시**(암묵/명시 구분) — 누락 시 "사람 1회 검토" 거짓 진행 | B·C·codex |
| 💡 Q2 | **transitive 통일** — 암묵도 명시(1b)와 동일 transitive(`_transitive_dependents` 재사용). v1 의 "직접만" 철회 | A·B·C(3:1) + 사용자 |
| R1~R3 | 명시 contract=name 힌트 격하(제거 안 함) / 타입 분류 거부(추론적, 계산적 우선 위반) / Q4 name 충돌 방지 | C |

---

## §0 배경 — dogfooding 발견

디딤돌1 dogfooding(94 entry)에서 확정: **약한 boss(qwen3-30b)는 `Contract` 비결정·거의 미생성**(직접 1회/데모 3회 0), **`depends_on` 은 일관 생성**. → 1b artifact 전달이 boss 주도로 사실상 미발동.

**CLAUDE.md §2 해법**: few-shot 으로 "boss 에게 잘하라"(모델 의존)가 아니라 **controller 가 `depends_on` 에서 데이터 전달을 흡수**(하네스 보장, 모델 무관).

---

## §1 핵심 결정 — depends_on 암묵 contract

```
boss: subtasks + depends_on (일관 생성) — Contract 선언 불필요(있으면 name 힌트)
                  │
controller(PlanController 확장):
  암묵 규칙 — produced subtask 를 transitive depends_on 하는 subtask 에 산출물 자동 주입
  (명시 Contract 와 동일 추출·검사·능력 경계·transitive 경로 재사용. boss Contract 0 이어도 동작)
```

- **하네스 흡수**: artifact 전달이 boss 의 Contract 생성 능력에 의존하지 않음 → 약한 boss 로도 동작.
- **명시 Contract = "선택적 name 힌트"로 격하(R1)**: 전달 트리거는 암묵(depends_on)이 담당. 명시 Contract 가 있으면 *읽기 좋은 name* 제공(없으면 default `subtask_{produced_by}`). dogfooding 상 실전 default 는 자동 name. 명시 제거 안 함(boss.py schema 회귀 리스크 + name 가독성).
- **dedup(BL-3)**: 명시 contract 가 이미 `(produced_by, consumer)` 를 커버하면 암묵 합성 skip(이중 주입 방지). dedup 키 = `(produced_by, consumer)`(name 아님).

### ⭐ 능력 경계 정밀화 (BL-1 — over-claim 정정, 1b/ADR-013 소급)
consume 워커 기본 `file`(OllamaWorker). **단 "fs 실행 능력 0"은 부정확** — OllamaWorker 는 `output_filename` 설정 시 workdir 단일 파일을 쓴다(worker.py:358-393, realpath traversal 차단). 정확한 능력 경계:
- ✅ **임의 명령/경로 실행 0** + **workdir escape 0**(결정적 차단).
- ⚠️ **workdir 단일 파일 산출 잔여**: 오염된 주입 artifact 가 file consume 워커를 통해 *workdir 안 파일로 물질화*될 수 있음(`output_filename` 설정 시). 임의 실행은 아니나 "실 부작용 절대 0"은 아님.
- **consume-safe 불변식(CN-1b)**: `SAFE_CONSUME_KINDS={"file"}` 만으론 부족 → **file alias 가 *writer 없는*(`output_filename=None`) OllamaWorker 임을 harness 구성 불변식**으로 문서화(또는 registry capability 메타 검증). 구현 시 명문화.

---

## §2 consume 범위 = transitive (Q2 결정)

- **암묵도 명시(1b)와 동일 transitive**: produced subtask 를 (직접/간접) depends_on 하는 subtask 모두 산출물 받음(A→B→C 에서 C 도 A 받음). 기존 `_transitive_dependents`(plan_controller.py:274-295) 재사용 — 코드 추가 0, 의미 모델 단일("depends_on 있으면 선행 산출물 받음"), 검증 표면 단일.
- 과주입(transitive 광범위)은 **능력 경계(§1) + bounded(2000자)**가 흡수(이미 1b 비용). 타입 분류 같은 추론적 완화는 거부(R2 — 계산적 우선).

---

## §3 controller 확장 (PlanController)

| 단계 | 동작 |
|---|---|
| 검증(사람 승인 전) | 기존 1b 명시 contract 검증 + **암묵 합성**: 명시 contract 가 없는 produced(=depends_on 의 모든 선행) 마다 암묵 contract 합성(`subtask_{produced_by}`, transitive consumer). **dedup**: 명시가 이미 `(produced_by, consumer)` 커버 시 skip. 능력 경계 검증은 암묵분에도 동일(code consume = opt-in reject) |
| 계획 게이트(BL-4) | `PlanApprovalRequest` 에 **합성 암묵 + 명시 contract 모두 표시 + 구분 표지**("암묵: B←A depends_on 추론"). 사람이 boss 선언 흐름과 controller 보강 흐름을 구분 검토 |
| 실행 | 명시와 동일 — produced 완료 → `_extract_artifact`(redact→truncate) → consume desc 주입. raw value 레저 미영속(런타임 extracted only) |

- **opt-out**: `PlanController(implicit_contracts=False)` = 1b 명시-only 복원. 기본 **on**(Q1).

---

## §4 안전 경계 (전파면 변화 — over-claim 차단)

- ⚠️ **암묵 contract 는 전파 채널을 늘린다**(transitive depends_on 마다 전달) → injection 전파면 *증가*. 정직 인정.
- **방어 = 능력 경계(결정적, BL-1 정밀화)**: consume 워커 LLM-only(writer 없는 OllamaWorker) → 오염 데이터의 **임의 실행·workdir escape 0**. 단 `output_filename` 설정 시 workdir 파일 산출은 잔여. code opt-in 시 실 실행 위험 재노출(인정).
- bounded·redaction·계획 게이트는 **추론적 보조**(차단 주장 안 함, ADR-013 답습). 짧은 injection 통과, redaction=secret-only.
- means/ends: boss `depends_on`(ends 순서) → controller 데이터 전달(means).

## §5 비례성 — 무엇을 *안* 하는가

- **few-shot 으로 boss 짜내기 안 함**(하네스 흡수 우선). **타입 기반 선택 전달 안 함**(추론적, 계산적 우선 위반, R2). **암묵 강제 안 함**(opt-out). **2차 injection 완전 차단 주장 안 함**.

## §6 변경 영향 + 다음 단계

### 변경 영향
- `PlanController`: 암묵 contract 합성(transitive 재사용) + dedup + `implicit_contracts` 옵션 + 게이트 표시 확장. 1b 명시 경로·검증·추출·주입 재사용.
- **회귀(BL-2)**: `test_plan_controller.py` 의 code+depends_on 테스트(happy_path/topo_reorder/subtask_failure 등)가 암묵 on + 능력 경계 충돌로 VALIDATION_FAILED → `_build` 에 `implicit_contracts=False` 주입(1a/1b 불변식 격리). `test_no_contracts_behaves_like_1a`(1b)도 `implicit_contracts=False` 전용 회귀로. 신규 `test_implicit_contract.py` 에서 1c 동작 검증.
- grimp 단방향 유지. **dogfooding 데모 재실행**(약한 boss 로 artifact 전달 발동 실증).

### 다음 단계
1. brief v1 → 3+1 합의(AWC) → **brief v1.1** + §7 Q 결정 ← 완료
2. **TDD 구현** + dogfooding 재검증
3. 구현 후 → **ADR-013 보강**(암묵 contract 전파면 + 능력 경계 정밀화 + 1b 소급) + CONTEXT/SESSION/INDEX

## §7 열린 질문 — ✅ 사용자 결정 (2026-05-30)

| # | 질문 | ✅ 결정 | 근거 |
|---|---|---|---|
| Q1 | 암묵 기본 on/off | ✅ **기본 on** + opt-out(`implicit_contracts=False`) | 4/4 |
| Q2 | 직접 vs transitive | ✅ **transitive 통일**(명시와 동일, `_transitive_dependents` 재사용) | 3:1 + 사용자 |
| Q3 | 명시 contract 관계 | ✅ **합집합 + dedup**(produced_by,consumer 키) + 명시=name 힌트 격하 | 4/4 |
| Q4 | 암묵 name | ✅ `subtask_{produced_by}` + 명시 name 충돌 방지(uniqueness 검증) | 3/4 |
| Q5 | 회귀 | ✅ implicit_contracts=False 격리 + 신규 on 테스트 | 4/4 |
| Q6 | ADR | ✅ **ADR-013 보강**(암묵 전파면 + 능력 경계 정밀화 + 1b 소급) | 4/4 |

---

## 부록 — 답습 교차
1b brief v1.1 / ADR-013(능력 경계) / 94 entry dogfooding / CLAUDE.md §2(하네스 흡수) / 합의 보고서 / [[feedback_boss_role_not_smartest]] · [[feedback_pass_scope_overclaim]] · [[feedback_proportionate_security_personal_tool]] · [[project_jarvis_collaborative_orchestration]].
