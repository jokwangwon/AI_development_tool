# 3+1 합의 보고서 — 디딤돌1c depends_on 암묵 contract 설계 brief (4 source)

> CLAUDE.md §3 3+1 합의. 검토 대상: `docs/phase0/jarvis-stone1c-implicit-contract-design-brief.md` (DRAFT v1).
> 4 source: Agent A(구현) · Agent B(품질/안전) · Agent C(대안) · codex(cross-vendor). Phase 2 병렬 독립.

**작성일**: 2026-05-30
**종합 판정**: **APPROVE WITH CONDITIONS (4/4 만장일치)** — v1.1 정정(BLOCKING 4) 흡수 시 구현 진입.
**source별**: A=AWC · B=AWC · C=AWC · codex=AWC. 설계 무효급 BLOCKING 0 — 전원 "하네스 흡수(depends_on→암묵 contract) 방향은 CLAUDE.md §2 답습으로 옳고, 전파면 증가를 정직 인정"이라 평가. 정정 = 능력 경계 정밀화 + 회귀 범위 + dedup + 게이트 가시성.

---

## Phase 3 — 교차 비교

### ① 일치 (Consensus)

| # | 합의 | 출처 |
|---|---|---|
| **CN-1** ⭐ | **"file consume 실 부작용 0" over-claim 정정** — `OllamaWorker` 는 `output_filename` 설정 시 **workdir 단일 파일 write 경로**가 있다(worker.py:358-393). "fs 실행 능력 경로 부재"는 부정확 → **"임의 명령/경로 실행 0 + workdir 단일 파일 산출 잔여"**. 1c 가 전파면을 늘리므로(오염 텍스트가 workdir 파일로 물질화 가능) 명문화 필수. **1b §1·ADR-013 §2.2/§4 에도 소급 보강.** | B(BL)·codex(BL) = 핵심 |
| **CN-1b** | **`SAFE_CONSUME_KINDS={"file"}` 만으론 LLM-only 보장 못 함** — file alias 가 *writer 없는* OllamaWorker 인지를 harness 구성 불변식으로 문서화하거나, consume-safe capability 를 registry 메타/플래그로 검증 | codex |
| **CN-2** | **회귀가 brief 추정보다 큼** — `test_no_contracts_behaves_like_1a`(1b, 주입 회귀, COMPLETED 유지) 외에 **`test_plan_controller.py` 의 code+depends_on 다수**(happy_path/topo_reorder/subtask_failure)가 암묵 on + 능력 경계 충돌로 **VALIDATION_FAILED 로 상태 뒤집힘**. Q5 처방 확장 필요 | A·codex |
| **CN-3** | **dedup 필수** — 명시+암묵 같은 `(produced_by, consumer)` 가 *다른 name* 으로 이중 주입(동일 오염 텍스트 2회 + prompt 부피 2배). dedup 키 = `(produced_by, consumer)`(name 아님). 명시 커버 시 암묵 suppress | A·B·codex |
| **CN-4** | **계획 게이트에 합성 암묵 contract 표시** — 현 `PlanApprovalRequest.contracts`(plan_controller.py:78)는 boss 명시분만. 암묵은 controller 합성 → 게이트가 합성분 포함 + **암묵/명시 구분 표지**. 누락 시 "사람 1회 검토" 거짓 진행 | B·C·codex |
| **CN-5** | **Q5: `test_no_contracts_behaves_like_1a` 를 `implicit_contracts=False` 전용 회귀로 유지 + 신규 "암묵 on 발동" 테스트 추가** | A·B·C·codex = 4/4 |
| **CN-6** | **Q1 기본 on** (dogfooding 해결 목적, opt-in 이면 문제 재발) — 단 CN-1 능력 경계 조건 | A·B·C·codex = 4/4 |
| **CN-7** | **Q6 ADR-013 보강**(신규 아님) — 암묵은 1b 능력 경계의 적용 확장. "전파면 증가"를 consequence 에 추가. 신규 ADR = ceremony | A·B·C·codex = 4/4 |
| **CN-8** | **Q4 name `subtask_{produced_by}`** — `_CONTRACT_NAME_RE`(line 57) 통과. 명시 name 충돌 방지(reserved prefix 또는 uniqueness 검증) | A·C·codex |

### ② 불일치 (Divergence)

| # | 쟁점 | 입장 |
|---|---|---|
| **DV-1** | **Q2 직접 vs transitive** | **transitive 통일**: A(코드 `_transitive_dependents` 재사용=추가 0)·B(검증 표면 단일화)·C(의미 모델 단일, 강력) / **직접 유지**: codex(암묵=의도 안 한 보강이니 과주입 최소). → **3:1 transitive 통일**. 과주입은 능력 경계+bounded 가 흡수(이미 1b 비용). **사용자 결정(Q2)** |

### ③ 누락 (Gap)

| # | 사항 | 출처 |
|---|---|---|
| **GP-1** | 명시 contract = **"선택적 name 힌트"로 격하** 명문화(제거 안 함 — 제거 시 name 가독성 손실 + boss.py schema 회귀 리스크). 전달 트리거는 암묵 100%, 명시는 name 품질만 | C |
| **GP-2** | Q5 "produced 타입(코드/데이터)별 선택 전달" **거부** — 내용 분류는 추론적(휴리스틱/LLM), CLAUDE.md §2 "계산적 우선" 위반·오판 경로 신설. 능력 경계+bounded 흡수가 더 단순 | C |
| **GP-3** | `test_run_is_non_adaptive_no_planner_recall`(L270)은 `plan_calls==[]` 만 assert → VALIDATION_FAILED 여도 통과 가능(경계 케이스) | A |

---

## Phase 4 — 합의 도출 (Reviewer 최종 판단)

### BLOCKING (v1.1 정정 의무)
| # | 정정 | 근거 |
|---|---|---|
| **BL-1** ⭐ | CN-1/CN-1b — "file consume 실 부작용 0" → "임의 명령/경로 실행 0 + workdir 단일 파일 산출 잔여". OllamaWorker write 경로(worker.py:358-393) 명시. **1b §1·ADR-013 §2.2/§4 소급 보강**. consume-safe = file alias 가 writer 없는 OllamaWorker 임을 harness 불변식 문서화(또는 registry 메타 검증) | B·codex |
| **BL-2** | CN-2 — 회귀 처방 확장: `test_plan_controller.py` code+depends_on 다수가 능력 경계 충돌로 VALIDATION_FAILED. `_build` 에 `implicit_contracts=False` 주입(1a/1b 불변식 격리), 신규 1c 동작은 별도 테스트 | A·codex |
| **BL-3** | CN-3 — dedup 키 `(produced_by, consumer)`, 명시 커버 시 암묵 suppress | A·B·codex |
| **BL-4** | CN-4 — 계획 게이트에 합성 암묵 contract 표시(암묵/명시 구분) | B·C·codex |

### 채택 (일치 → v1.1)
CN-5(회귀 격리+신규 테스트) · CN-6(기본 on) · CN-7(ADR-013 보강) · CN-8(name) + GP-1(명시=name 힌트) + GP-2(타입 분류 거부).

### 갈림 해소
- **DV-1 (Q2)**: Reviewer 권고 = **transitive 통일**(3:1) — A/B/C 의 "코드 재사용+의미 단일+검증 표면 단일"이 codex 의 "과주입 최소"보다 비례적(과주입은 능력 경계+bounded 가 이미 흡수하는 1b 비용). **단 사용자 결정(Q2)** — codex 의 직접-only(과주입 최소) 안도 제시.

### 메타 편향 자기진단
1c brief 가 전파면 증가를 §4·§5 에서 정직 인정 → over-claim 차단 양호. 그러나 4 source 가 **1b/ADR-013 의 기존 over-claim("fs 실행 능력 0")을 소급 발견**(CN-1) — 능력 경계의 load-bearing 주장이 OllamaWorker 의 실제 write 경로를 놓쳤음. dogfooding(94)→1c→소급 정정의 연쇄가 [[feedback_pass_scope_overclaim]] 답습의 누적 효과를 보여줌(이전 단계 정직성도 재검증).

---

## §7 Q 합의 권고 (고정은 사용자)

| Q | 합의 권고 | 분포 |
|---|---|---|
| Q1 on/off | **기본 on** + opt-out | 4/4 |
| Q2 직접/transitive | **transitive 통일**(Reviewer 권고) vs 직접(codex) | 3:1 — 사용자 결정 |
| Q3 명시 관계 | **합집합 + dedup**(produced_by,consumer 키) + 명시=name 힌트 격하 | 4/4 |
| Q4 name | `subtask_{produced_by}` + 충돌 방지 | 3/4 |
| Q5 회귀 | implicit_contracts=False 격리 + 신규 on 테스트 | 4/4 |
| Q6 ADR | ADR-013 보강(+1b 소급) | 4/4 |
