# 3+1 합의 보고서 — 디딤돌1a plan-then-execute 설계 brief (4 source)

> CLAUDE.md §3 3+1 멀티 에이전트 합의. 검토 대상: `docs/phase0/jarvis-stone1a-plan-then-execute-design-brief.md` (DRAFT v1).
> 4 source: **Agent A**(구현 분석가) · **Agent B**(품질/안전성 검증가) · **Agent C**(대안 탐색가) · **codex**(cross-vendor, 독립). Phase 2 병렬 독립 분석(서로 출력 미참조).

**작성일**: 2026-05-29
**종합 판정**: **REVISE → v1.1 BLOCKING 흡수 시 APPROVE WITH CONDITIONS**
**source별**: Agent A = AWC · Agent B = REVISE · Agent C = AWC · codex = REVISE
**핵심**: 설계 방향(plan-then-execute + 결정적 controller)은 4 source 전원 *구현 가능·견고* 판정. 그러나 brief 의 **안전 논증 서술이 over-claim**(4/4 수렴) → 정직화 필수. 설계 폐기 아님.

---

## Phase 3 — 교차 비교

### ① 일치 (Consensus — 4/4 동의)

| # | 합의 사항 | 출처 |
|---|---|---|
| **CN-1** | **over-claim 정정 필수**: "boss 가 argv/명령에 영향 줄 경로 구조적 부재" / "제어권 0 동등 이상 보존"은 **거짓**. 코드 실측 — `run_plan → dispatch(subtask.desc) → worker.run(prompt) → [*argv, prompt]`(orchestrator.py:120, worker.py:118-119,177-178). boss-authored `desc` 가 워커 실행 prompt(argv tail)가 됨. 정직 표현 = "boss 는 argv prefix·workdir·isolation backend·alias(means 의 *틀*) 불가. 단 `desc`(=worker prompt, untrusted instruction)·`worker_kind`(라우팅 종류)는 boss 제안 = **bounded, approved, non-adaptive control proposal**". 방어 = **계획 승인 게이트 + subtask 반영 게이트**(NOT redaction). | A·B·C·codex |
| **CN-2** | **신규 `PlanController` + plan 주입형 분리**(controller-first). `run_plan(plan: BossPlan)` 으로 *이미 만들어진 plan* 을 받아 boss.plan() 과 분리 → boss 신뢰성이 controller 출하를 인질로 잡지 않음. Orchestrator.run_plan 메서드 확장은 dispatch 와 책임 혼선·비대. (Q5) | A·B·C·codex |
| **CN-3** | **MAX_STEPS 기본값 = 5**. 순차 latency 상한 + 사람 검토 부하 + 약한 boss 과분해 방어. 생성자 override 가능(Provider Liquidity). (Q3) | A·B·C·codex |
| **CN-4** | **subtask 실패 default = 즉시 중단**. fail-closed 정합 + 1a 단순성. "독립 subtask 계속/DAG-aware skip"은 후속(1b 이후) 옵션. (Q4) | B·C·codex (A 도 default 중단 수용, skip 은 후속 제안) |
| **CN-5** | **`general` worker_kind 제외**. 라우팅 의미 모호 → table 매핑 불명확, enum "제약된 선택" 가치 희석. (Q1 일부) | A·B·C·codex |
| **CN-6** | **별도 `PlanApprovalRequest` dataclass**(기존 `ApprovalRequest` 와 분리 — 반영 게이트 전용 필드 구조). (Q6 일부) | A·B·C·codex |
| **CN-7** | **worker_kind→alias table 의 *값*은 harness/config(사람) 소유**. boss 가 alias 직접 출력 경로 금지 유지. (Q2) | A·B·C·codex |

### ② 부분 일치 (Partial — 2~3 동의)

| # | 사항 | 분포 |
|---|---|---|
| **PT-1** | **§6 "실증" → "실증 계획 / acceptance criteria"**. (b) PoC·(d) 자동회귀는 *구현 단계*, (c) ADR 권위는 미정 → 현 §6 의 "실증" 단정은 over-claim. ADR-011 (a)~(d) 는 아직 *계획*. | codex(명시)·B(동조)·A(grimp (d) 공허 지적) = 3/4 |
| **PT-2** | **§6(b)(iv) PoC 공허참 교체**. "boss 가 argv 를 바꿔도 실행 argv 불변"은 schema 에 argv 필드가 *애초에 없어* vacuously true → 실효 위협 미검증. 3-part 의미검증(① argv prefix·alias·isolation 이 plan 무관 고정 ② desc 전문이 게이트 도달 ③ subtask 결과 boss 환류 0)으로 교체. | B(명시)·codex((b) 실증계획화로 흡수) = 2/4 |
| **PT-3** | **R2 불변식 서술 정정**. plan() 은 `BossAdvice`(텍스트 전용 R2) 가 아니라 **새 판단 지점** — `worker_kind`/`depends_on` = 구조적 제어 입력. 상위 brief 의 "R2 두 축 글자 그대로 연장"은 부정확. 보존되는 것은 (i) 직접 means 제어 0 (ii) adaptive control loop 0 (NOT 모든 boss output 의 worker 입력 영향 0). | B·codex = 2/4 (핵심) |
| **PT-4** | **`shell` worker_kind 위험도**. codex = 1a 기본 enum 제외 또는 opt-in+allowlist(가장 위험 — boss 가 shell prompt 에 명령 텍스트). B·C = `{code,shell,file}` 유지하되 `general` 만 제외. → **갈림: 사용자 결정 영역(Q1)**. Reviewer 권고는 PT-4 해소(아래). | codex(제외/opt-in) vs B·C(유지) |
| **PT-5** | **sub_task_id 고유 파생 규칙 명시**. 미규정 시 LedgerLog.fold()(ledger.py:116-119) 가 task_id 단위 병합 → subtask 상태 덮어쓰기(데이터 손실). `f"{task_id}.{i}"` + plan 자체는 별도 task_id 이벤트. | A(명시)·codex(task_id 충돌 언급) = 2/4 |
| **PT-6** | **Q7 ADR 등록**. A·B·C = brief 권위 충분(over-claim 정정 후) + ceremony 회피. codex = ADR/amendment 권고(ADR-011 (c)). → 3:1 brief 충분. | A·B·C vs codex |

### ③ 불일치 (Divergence)

| # | 쟁점 | 입장 |
|---|---|---|
| **DV-1** | 계획 게이트 *메커니즘* | A·codex = 신규 `PlanApprovalGate` 클래스 / C = 기존 `ApprovalGate` 메커니즘 재사용 + 별도 request(코드 중복 회피, fail-closed 상속). → Reviewer 절충(아래). |
| **DV-2** | subtask 실패 세부 | A = DAG-aware skip(실패 노드의 transitive descendant 만 skip, 독립 분기 계속) / B·C·codex = 즉시 전체 중단. → default 중단 합의(CN-4), skip 은 후속. |

### ④ 누락 (Gap — 단일 source)

| # | 사항 | 출처 |
|---|---|---|
| **GP-1** | **"중간 boss 호출 0" 충돌**: 기존 dispatch 가 성공 워커마다 `_advise()` 호출 가능(orchestrator.py:137-138). §3/§6 "중간 boss 호출 0"은 문자 그대로 false → "중간 **control-affecting** boss call 0"로 정정 + sub-dispatch advisory 정책 명시(켜되 제어 환류 0 / 또는 끔). | codex |
| **GP-2** | **grimp boss→orchestrator contract 미존재**: `.importlinter` 에 해당 forbidden contract 0(현 단방향은 *우연*). §6(d)/§9 "유지" → **신규 import-linter contract 추가** 필수(센서 부재 시 plan() 회귀 가드 0). | A |
| **GP-3** | **계획 게이트 desc 전문 비절단 표시**: 기존 output_preview[:200](orchestrator.py:147) truncate 가 계획 게이트에 적용되면 긴 desc 후미 injection 누락. desc 전문 + worker_kind + alias 비절단 표시를 BLOCKING 불변식으로. | B |
| **GP-4** | **LedgerLog plan 영속 scrub/exfil 책임자 명시**: plan/subtask 이벤트에 raw desc/output 영속 시 상위 brief §5(B5) "영속 전 exfil 검사" 적용 시점·책임자(board) 명시. | B·codex |
| **GP-5** | **ollama `format` JSON schema 공식 지원 확인**: codex 가 공식 문서(https://docs.ollama.com/api/chat) 로 `format`=json/JSON schema 지원 확인 → A 의 "미검증 신규 기능" 우려 *완화*. 단 grammar 는 문법만, 의미검증은 controller(둘 다 동의). 버전 pin + 실측 PoC 는 여전히 권고. | codex(완화)·A(버전 pin) |
| **GP-6** | **schema 강건성**: `additionalProperties:false` + 문자열 길이 제한 + depends_on 중복 제거/정렬 + 빈 plan 금지 + budget 사전(예상)/사후(observed) 분리(OllamaWorker cost_usd=0.0 로 로컬 무의미). | codex·B·A |

---

## Phase 4 — 합의 도출 (Reviewer 최종 판단)

### 채택 (일치 → 그대로 v1.1 반영)
CN-1 ~ CN-7 전원 채택.

### 갈림 해소
- **DV-1 (게이트 메커니즘)** → **절충 채택**: 별도 `PlanApprovalRequest` dataclass(CN-6, 4/4) + **기존 `ApprovalGate` 의 fail-closed/default-deny *패턴* 답습**(C 의 코드중복 회피 이점) + 계획 전용 게이트 진입점은 얇게(A·codex 의 의미 분리 이점). 즉 "별 dataclass + 패턴 재사용". 신규 거대 클래스 중복도, 의미 혼선도 회피.
- **PT-4 (shell 위험)** → **codex 손 들어 보수적 채택 권고**: `shell` 은 가장 위험(boss 가 shell prompt 에 임의 명령 텍스트). 1a 기본 enum = **`{code, file}`** + `shell` 은 **계획 게이트 별도 경고 표시 + 명시 opt-in** 조건부. 단 최종 enum 집합은 **사용자 결정(Q1)** — Reviewer 는 codex 보수안을 권고로 제시.
- **DV-2 (실패 세부)** → default 중단(CN-4), DAG-aware skip 은 1b 이후 옵션.
- **PT-6 (ADR)** → brief 권위 + means/ends 정직화로 1a 충분(3:1). codex 우려는 "1b typed contract 도입 시 ADR 권위화" 로 흡수.

### BLOCKING (v1.1 정정 의무 — 흡수 시 AWC)
| # | 정정 | 근거 |
|---|---|---|
| **BL-1** | §1·§6.1·§7 over-claim 정정 (CN-1) — "구조적 부재"/"제어권 0" → "bounded approved non-adaptive control proposal", 방어 게이트 귀속 | 4/4 |
| **BL-2** | §6 "실증" → "실증 계획 / acceptance criteria" (PT-1) | 3/4 |
| **BL-3** | §6(b)(iv) 공허참 → 3-part 의미검증 (PT-2) | 2/4 |
| **BL-4** | R2 서술 정정 — plan()=새 invariant, 보존축 (i)(ii) 명시 (PT-3) | 2/4 |
| **BL-5** | "중간 boss 호출 0" → "중간 control-affecting boss call 0" + advisory 정책 (GP-1) | codex |
| **BL-6** | §3 controller = `run_plan(plan: BossPlan)` 주입형 + 신규 PlanController (CN-2) | 4/4 |
| **BL-7** | sub_task_id 고유 파생 규칙 §3 step7-8 명시 (PT-5) | 2/4 |
| **BL-8** | §6(d)/§9 grimp "유지" → 신규 import-linter contract 추가 (GP-2) | A |

### 권고 (v1.1 반영, 구현 흡수)
desc 전문 비절단 게이트 표시(GP-3) · LedgerLog plan scrub/exfil 책임 명시(GP-4) · schema 강건성 additionalProperties:false 등(GP-6) · ollama 버전 pin + format 실측 PoC(GP-5) · budget 사전/사후 분리(GP-6).

### 메타 편향 자기진단
본 합의는 자체 brief 우호 결론을 경계. over-claim(CN-1)이 4/4 수렴으로 포착된 것은 [[feedback_pass_scope_overclaim]] 답습이 작동한 증거 — brief 작성자(메인 컨텍스트)의 "구조적 불가" framing 을 4 source 가 코드 실측으로 반증. 설계 자체는 견고하나 *서술 정직성*이 BLOCKING.

---

## §10 Q1~Q7 합의 권고 (고정은 사용자 영역 — [[project_jarvis_collaborative_orchestration]])

| Q | 합의 권고 | 분포 |
|---|---|---|
| Q1 enum | **`{code, file}` 기본 + `shell` opt-in/경고** (codex 보수) vs `{code,shell,file}`(B·C). `general` 제외 4/4. → **사용자 결정** |
| Q2 table 값 | harness/config 소유. 후보: code→CliWorker(claude/codex), file→OllamaWorker(output_filename), shell→TmuxWorker. boss 발명 불가 |
| Q3 MAX_STEPS | **5** (4/4) |
| Q4 실패정책 | **즉시 중단** (4/4 default) |
| Q5 controller | **신규 PlanController + plan 주입형** (4/4) |
| Q6 게이트 | **별도 PlanApprovalRequest + ApprovalGate fail-closed 패턴 답습** (절충) |
| Q7 ADR | **brief 권위 충분** + means/ends 정직화 (3:1) |
