# Jarvis 디딤돌1a 설계 brief — plan-then-execute (boss 계획 1회 + 사람 승인 + 결정적 controller) (v1.1)

> **본 brief = 설계 정리 한정.** 본 brief 의 어떤 §도 그 자체로 **코드 작성·런타임 설치·모델 다운로드·격리/sandbox 신설·게이트 신설·controller 구현** 을 발생시키지 않는다. staged: brief v1 → **3+1 합의(REVISE)** → **brief v1.1(본 문서, BLOCKING 8 흡수)** → 사용자 승인 + §10 Q 결정 → **디딤돌1a TDD 구현(별도 브랜치)**. 코드 전 문서 먼저(SDD).

---

**작성일**: 2026-05-29
**Status**: **v1.2 — v1.1(3+1 합의 REVISE 흡수 + §10 Q 결정) + 사용자 통찰 반영("사장≠가장 똑똑한 자", plan 공급원 유연성, 2026-05-29). 디딤돌1a TDD 구현 진입 승인됨**
**진입 단위**: jarvis 본체 확장 — 단발 단일 워커(`Orchestrator.dispatch`) → **다중 subtask 결정적 배치 실행**(boss 계획 1회 + 사람 승인 1회 + 결정적 controller). **산출물 워커 간 전달은 디딤돌1b 로 DEFER**(본 1a 에서 각 subtask 독립).
**상위 문서**: `docs/phase0/jarvis-collaborative-orchestration-design-brief.md` (v2)
**합의 보고서**: `docs/review/3plus1-consensus-2026-05-29-jarvis-stone1a-plan-then-execute.md`
**근거**: `project_jarvis_collaborative_orchestration` · `project_jarvis_controlled_child_then_friday` · `feedback_provider_liquidity` (헌법 5조) · `feedback_proportionate_security_personal_tool` (비례성) · `feedback_pass_scope_overclaim` (over-claim 차단) · `ADR-011` §2.1 (a)~(d) · CLAUDE.md §2·§3 · 기존 코드 `src/jarvis/{orchestrator,boss,worker,approval,ledger}.py`

---

## v1.2 변경 이력 (사용자 통찰 반영)

| # | v1.1 → v1.2 | 출처 |
|---|---|---|
| 💡 IN-1 | §1 **boss 역할 정정** — "사장(boss)이 직원(worker)보다 똑똑하다"는 가정 *명시적 부정*. 현 구조에서 worker(claude/codex CliWorker)=frontier 가능 → 직원이 더 똑똑할 수 있음. boss 가치 = **똑똑함이 아니라 "로컬 상주 통제 위치 + provider-agnostic 조율"**. plan-then-execute 정당화는 "사장이 똑똑해서"가 아니라 "사장이 *약하니까* 제어권 박탈, 제안만" | 사용자 (2026-05-29) |
| 💡 IN-2 | §2 **plan 공급원 유연성** — `boss.plan()` 은 plan 공급원 *중 하나*일 뿐(고정 아님). CN-2 plan 주입형 덕에 사람/frontier worker 도 plan 공급 가능. **불변식(PLAN-SOURCE)**: 누가 짠 plan 이든 controller 검증 + 사람 승인 거침 — **똑똑함 ≠ 신뢰**(frontier 도 untrusted, injection 표적) | 사용자 (2026-05-29) |

## v1.1 변경 이력 (3+1 합의 REVISE 흡수)

| # | v1 → v1.1 | 출처 |
|---|---|---|
| 🔴 BL-1 | §1·§6.1·§7 **over-claim 정정** — "boss 가 argv/명령 영향 *구조적 부재*" / "제어권 0 동등 이상" 은 **거짓**(코드 실측: `dispatch(subtask.desc)→worker.run(prompt)→[*argv,prompt]`). boss-authored `desc` = worker 실행 prompt. → "bounded, approved, non-adaptive control proposal" + 방어를 게이트에 귀속 | A·B·C·codex (4/4) |
| 🔴 BL-2 | §6 **"실증" → "실증 계획 / acceptance criteria"** — (b)(d) 구현단계, (c) 미정 | codex·B·A (3/4) |
| 🔴 BL-3 | §6(b)(iv) **공허참 PoC → 3-part 의미검증** | B·codex |
| 🔴 BL-4 | §1·§2 **R2 서술 정정** — plan()=새 invariant(worker_kind/depends_on=구조적 제어입력), 보존축 (i)직접 means 제어 0 (ii)adaptive loop 0 명시 | B·codex |
| 🔴 BL-5 | §3·§6 **"중간 boss 호출 0" → "중간 control-affecting boss call 0"** + sub-dispatch advisory 정책 | codex |
| 🔴 BL-6 | §3 **controller = `run_plan(plan: BossPlan)` 주입형 + 신규 PlanController** (boss.plan 분리, controller-first) | A·B·C·codex (4/4) |
| 🔴 BL-7 | §3 **sub_task_id 고유 파생 규칙 명시** (LedgerLog fold 덮어쓰기 방지) | A·codex |
| 🔴 BL-8 | §6(d)·§9 **grimp "유지" → 신규 import-linter contract 추가** | A |
| R1~R5 | desc 전문 비절단 게이트 표시 / LedgerLog plan scrub·exfil 책임 / schema 강건성(additionalProperties:false 등) / ollama format 버전 pin+실측 PoC / budget 사전·사후 분리 | B·codex·A |

---

## §0 배경 — 디딤돌0 완료 → 디딤돌1a 진입

- **디딤돌0 완료**(PR #3 MERGED, 79번째 entry): `LedgerLog`(append-only event-sourcing JSONL) + `JarvisTaskBoard` 영속화 + 재시작 `interrupted` fold + 실행 중 취소. 협업 0.
- **1a/1b 분리**(사용자 결정 2026-05-29): 비례성 — 위험·규모를 쪼개 즉시 가치 먼저 출하.

| 단위 | 능력 | 산출물 전달 | 규모 |
|---|---|---|---|
| **디딤돌1a (본 brief)** | boss 계획 1회 + 사람 승인 1회 + 결정적 controller(schema validate + DAG + worker_kind table + budget/step limit + 순차 dispatch) | **없음 — 각 subtask 독립** | 중간 |
| 디딤돌1b (후속) | + typed artifact contract + contract-first 계약 고정 → 워커 양쪽 주입 | typed artifact(bounded fields) | 중간 |
| (범위 밖) | 자율 재계획·동적 재분배 (L4) | — | 프라이데이 영역 |

**1a 즉시 가치**: "이 작업을 N개 subtask 로 쪼개 순서대로 실행"을 *사람이 1회 승인 후 결정적으로* 자동 배치 실행 → 반복 승인 피로 제거 + 작업그래프 히스토리.

---

## §1 핵심 결정 — plan-then-execute (over-claim 정정, BL-1·BL-4)

### boss 의 가치 = 통제 위치, *똑똑함 아님* (IN-1)
**"사장(boss)이 직원(worker)보다 똑똑하다"는 가정은 명시적으로 부정한다.** 현 구조에서 worker = `CliWorker(claude/codex)` = **frontier 가능** vs boss = `OllamaBoss`(로컬 LLM) = 약함 → **직원이 더 똑똑할 수 있다**. 따라서:
- boss 의 가치 = 똑똑함이 아니라 **로컬 상주 통제 위치 + provider-agnostic 조율점**(헌법 5조). 사장은 "가장 똑똑한 자"여서가 아니라 *통제·라우팅·히스토리를 담당하는 위치*여서 사장이다.
- **plan-then-execute 정당화의 방향**: "사장이 똑똑해서 계획을 잘 짠다"가 *아니라* 정반대 — "사장이 *약하므로* 사장에게 **제어권**을 주면 위험 → 사장은 **제안(proposal)만**, 통제는 사람 + 결정적 controller". (CLAUDE.md §2: 똑똑한 자에게 권한을 주는 게 아니라 *구조로 통제*.)


```
boss (untrusted planner):  작업 prompt 1개 → 작업그래프(subtasks + 의존성 DAG)를
                           JSON schema 로 *1회* 제안.  ← proposal, 권위 0
                                  │
사람 게이트:                계획 전체(각 subtask 의 desc 전문·순서·worker_kind·매핑
                           alias)를 *1회* 승인/거부 (계획 1회, 매-subtask 아님)
                                  │
결정적 controller(PlanController):  schema validation + DAG 검증 + worker_kind →
                           worker_alias table 룩업 + capability allowlist +
                           budget/step limit → 위상정렬 순서로 dispatch 반복
                           ← 중간 control-affecting boss call 0, 워커 간 통신 0, 산출물 전달 0(1a)
                                  │
각 subtask:                기존 `dispatch(desc, sub_task_id, alias)` 재사용 —
                           ReviewGuard + (선택) boss advisory + 반영 게이트 보존
```

### boss 제어권의 정직한 범위 (BL-1)
boss plan 은 **(가) 실행 여부·순서 (나) worker_kind(라우팅 종류) (다) `desc`(= 각 워커에 전달되는 실행 prompt = untrusted instruction text)** 를 *제안*한다. 코드 실측: `desc` 는 `dispatch` 의 `prompt` 인자(orchestrator.py:120) → `worker.run(prompt)` → `[*argv, prompt]`(worker.py:118-119,177-178) 의 argv tail 로 들어간다. 따라서:

- ❌ **"boss 가 argv/명령에 영향 줄 경로 구조적 부재" 는 거짓** — 특히 `shell` 워커에서 boss 는 shell prompt 안에 명령 텍스트를 넣을 수 있다.
- ✅ **정직 표현**: boss 는 **argv prefix·workdir·isolation backend·worker alias(means 의 *틀*)를 바꿀 수 없다**(harness table 소유). boss 의 제어권 = **bounded(MAX_STEPS·enum·DAG 검증으로 한정), approved(사람 1회 승인), non-adaptive(워커 결과가 다음 결정을 바꾸는 루프 부재)** 한 *제안*.
- **방어 귀속**: boss 가 정하는 `desc`/`worker_kind` 의 위험은 **(1) 계획 승인 게이트(사람이 desc 전문 검토, §4) + (2) 각 subtask 의 기존 ReviewGuard + 반영 게이트** 가 책임. RT-1 redaction 은 **아님**(secret-only, injection 미차단 — 상위 §3 B1).

### 보존되는 안전 축 (BL-4)
plan-then-execute 가 보존하는 것은 (i) **직접 means 제어 0**(boss 가 argv 틀·alias·isolation 을 못 정함) + (ii) **adaptive control loop 0**(워커 출력 → boss → 다음 실행 결정 환류 경로 부재). 이는 상위 brief v1 의 "boss 직접 제어"가 닫지 못한 두 위험을 *구조적으로* 닫는다. 단 "모든 boss output 이 worker 입력에 영향 0" 은 **아니다**(desc 경로).

---

## §2 boss.plan() — untrusted planner (새 판단 지점, R2 와 별개 invariant)

현 `BossLLM` Protocol 은 `advise()` 1개. 디딤돌1a 는 **`plan()` 두 번째 판단 지점** 추가:

```python
@dataclass(frozen=True)
class PlanSubtask:
    desc: str                    # = worker prompt (untrusted instruction text — 표시용 아님)
    worker_kind: str             # 허용 enum (§5 table 키)
    depends_on: tuple[int, ...]  # 선행 subtask 인덱스 (DAG edge)

@dataclass(frozen=True)
class BossPlan:
    subtasks: tuple[PlanSubtask, ...]
    # argv·경로·명령·workdir·격리 backend·alias 필드 *부재* (means 의 틀은 harness)
```

### plan 공급원 유연성 (IN-2 — boss 고정 아님)
`boss.plan()` 은 plan 공급원 *중 하나*일 뿐이다. CN-2 의 **plan 주입형**(`PlanController.run(plan: BossPlan)`) 덕에 controller 는 plan 을 *누가 만들었든* 무관하게 소비한다 — **약한 boss / 사람 / 똑똑한 frontier worker** 모두 plan 공급 가능(똑똑한 직원이 더 나은 계획을 낼 수도 있음, IN-1). 디딤돌1a 의 기본 공급원은 `boss.plan()` 이되, *공급원이 boss 로 고정되지 않음*을 설계 여지로 둔다(frontier-worker-plan·사람-편집-plan 은 후속 옵션).

> **PLAN-SOURCE 불변식**: plan 공급원이 무엇이든(똑똑하든 약하든) — ① controller 결정적 검증(§3 1~4) + ② 사람 승인 게이트(§4)를 *반드시* 거친다. **똑똑함 ≠ 신뢰**: frontier worker 가 더 똑똑해도 그 출력은 여전히 untrusted(injection 표적)이므로 검증·승인을 면제받지 못한다. 이것이 "구조로 통제"(IN-1)의 핵심 — 신뢰는 똑똑함이 아니라 *통과한 검증*에서 나온다.

### R2 와의 관계 (BL-4 — 새 invariant)
기존 `BossAdvice`(boss.py:45-57)의 R2(텍스트 전용, 제어 흐름 필드 금지)는 `advise()` 에 *그대로 유지*. `plan()` 은 `BossAdvice` 가 아니라 **새 판단 지점** — `worker_kind`/`depends_on` 이라는 *구조적 제어 입력*을 낸다. 이는 R2 위반이 아니라 **R2 의 범위를 보완하는 새 invariant**:
> **PLAN-INV**: BossPlan 은 (a) means 의 *틀*(argv·alias·isolation) 필드를 갖지 않고 (b) controller 의 결정적 검증(§3) 을 거쳐야만 소비되며 (c) 워커 결과가 plan 을 갱신하는 경로가 없다(non-adaptive).

### schema 강제 + 강건성 (R3·R4 권고 흡수)
- ollama `/api/chat` `"format": <JSON schema>` grammar 강제(공식 지원 — https://docs.ollama.com/api/chat). **단 grammar 는 *문법*만 — 의미 타당성은 controller 재검증(§3)이 권위.** provider liquidity: grammar 미지원 provider 도 대상이므로 controller schema validation 이 *유일 방어선*(grammar 는 보조).
- schema 강건성: `additionalProperties: false` + `desc` 길이 상한 + `depends_on` 중복 제거·정렬 + 빈 plan 금지.
- **ollama 버전 pin + `format` schema 응답 실측 PoC 1회**(구현 단계 — grammar 가 실제 강제되는지 트랙 B 확인).
- **provider 교체(헌법 5조)**: `StubBoss.plan()` scripted → 트랙 A 결정성. `OllamaBoss.plan()` = stdlib urllib. 신규 dep 0.
- **실패 처리**: plan 호출 실패(timeout/malformed/schema 위반 재시도 후도 실패) = **계획 부재 → 전체 중단**(사람 명시 경고). plan 은 실행의 전제이므로 "부재=중단"(거짓 진행 금지).

---

## §3 결정적 controller — PlanController(주입형) (BL-6·BL-7·BL-5)

**신규 `PlanController` 클래스**(Orchestrator.run_plan 메서드 확장 아님 — dispatch 회귀 표면·비대 회피). `Orchestrator`(또는 dispatch 콜러블)를 *주입*받아 조립:

```
PlanController.run(plan: BossPlan, task_id) -> PlanOutcome    # ← plan 주입형 (boss 와 분리)
```

> **controller-first 분리(BL-6)**: controller 는 *이미 만들어진 plan* 을 받는다. boss.plan() 호출은 *바깥*(또는 별도 진입점 `run_from_boss(prompt)`)에서 수행 → boss 신뢰성(약한 로컬 LLM 의 plan 품질)이 controller 출하를 인질로 잡지 않음. 트랙 A 테스트 = 직접 구성한 BossPlan 주입으로 결정적.

| 단계 | 검증/동작 | 실패 시 |
|---|---|---|
| 1. schema validation | 각 subtask: `worker_kind ∈ 허용 enum`(§5) / `desc` 비어있지 않음·길이 상한 / 빈 plan 금지 | reject → 중단 |
| 2. DAG 검증 | `depends_on` 인덱스 범위 내(`0≤idx<len`) + 자기참조 0 + 중복 제거 + **사이클 0**(`graphlib.TopologicalSorter`, stdlib) | reject → 중단 |
| 3. worker mapping | `worker_kind` → `worker_alias` *table 룩업*(§5) → registry 등록 확인 | 미등록 = reject → 중단 |
| 4. budget/step limit | `len(subtasks) ≤ MAX_STEPS`(§10 Q3) + budget **사전(예상치)/사후(observed) 분리**(R5 — OllamaWorker cost_usd=0.0 로 로컬 무의미, CliWorker 만 유효; 실 누적 초과 시 중단) | 초과 = reject → 중단 |
| 5. 사람 승인 게이트 | 계획 전체(각 subtask **desc 전문 비절단** + worker_kind + 매핑 alias + 순서)를 1회 표시 → 승인/거부(§4) | 거부 = 전체 미실행 |
| 6. 순차 dispatch | 위상정렬 순서로 `dispatch(subtask.desc, sub_task_id_i, alias)` 반복. subtask 실패 = **즉시 중단**(default, §10 Q4) | 중단 |
| 7. 레저 기록 | plan = 별도 task_id 의 `plan_proposed`/`plan_approved` 이벤트. 각 subtask = **고유 파생 `sub_task_id = f"{task_id}.{i}"`**(BL-7 — fold task_id 단위 병합 충돌 방지) | fail-soft(디딤돌0 동형) |

- **검증 순서**: 1~4 는 *사람 승인 전*(5) 전부 → 사람은 구조적으로 타당한 계획만 승인("잘못하는 것이 불가능하게", CLAUDE.md §2).
- **"중간 control-affecting boss call 0"(BL-5)**: 6 의 순차 dispatch 는 controller 결정적 루프. 기존 dispatch 가 성공 워커마다 `_advise()`(orchestrator.py:137-138)를 호출할 수 있으나(advisory = 사람용, 제어 환류 0), **제어 결정을 바꾸는 boss 호출은 0**. sub-dispatch advisory 정책 = 켜되 제어 비환류(또는 1a 에서 끔 — §10 검토). 문자 그대로 "boss 호출 0"이 아님을 정직 명시.
- **dispatch 재사용 회귀 0**: dispatch(orchestrator.py:120-156)는 무상태 메서드(생성자 주입만, 호출 간 mutation 0) → 순차 반복 호출이 단발 동작 불변. 342 passed 보존 목표.

---

## §4 사람 승인 게이트 — 계획 1회 (DV-1 절충, GP-3)

- **별도 `PlanApprovalRequest` dataclass**(기존 `ApprovalRequest`=반영 게이트 전용 필드와 분리) + **기존 `ApprovalGate` 의 fail-closed/default-deny *패턴* 답습**(approval.py:38-47). 거대 신규 클래스 중복도, 의미 혼선도 회피(합의 절충).
- **desc 전문 비절단 표시(GP-3, BLOCKING 불변식)**: 계획 게이트는 모든 subtask 의 `desc` 전문 + worker_kind + 매핑 alias 를 *truncate 없이* 표시. (기존 `output_preview[:200]` 같은 절단 금지 — 긴 desc 후미 injection 누락 방지.) ApprovalGate 의 "사람이 raw 직접 검토" 답습.
- **통제 형태전환**(상위 §5 R6): 인간 통제 = 계획 1회 승인 + harness 능력 봉쇄(§3 1~4) + adaptive loop 부재. 매-subtask 승인 대비 *전체 의도*를 봄.
- **default-deny**: 게이트 실패/타임아웃 = 거부(fail-closed).

---

## §5 worker_kind → worker_alias table (means/ends, PT-4)

```
WORKER_KIND_TABLE = {            # 값 = 사람/config 소유 (boss 발명 불가)
    "code":  "<code worker alias>",   # 예: CliWorker(claude/codex)
    "file":  "<file worker alias>",   # 예: OllamaWorker(output_filename=...)
    # "shell": "<shell worker alias>" # ⚠️ 가장 위험 — §10 Q1 (기본 제외 + opt-in 권고)
}
```

- boss 선택 = **enum 1개(worker_kind)** = 제약된 ends 선택. **argv·경로·격리 backend·alias = means 의 틀 = harness table 룩업**(상위 §4 B2). 자연어 subtask→워커를 "결정적"이라 부르지 않음 — 결정적인 것은 *enum→alias 룩업* 뿐.
- **`general` 제외**(4/4) — 라우팅 모호.
- **`shell` 위험(PT-4)**: boss 가 shell prompt 에 임의 명령 텍스트 → 가장 위험. 합의 권고 = **기본 enum `{code, file}` + `shell` opt-in/경고**(codex 보수안). 최종 집합 = **사용자 결정(Q1)**.

---

## §6 means/ends acceptance criteria — ADR-011 §2.1 (a)~(d) (BL-2 — "실증"→"실증 계획")

> **정직화(BL-2)**: 본 §은 (a)~(d) 의 *완료된 실증*이 아니라 **실증 계획 / acceptance criteria**다. (b) PoC·(d) 자동회귀는 *구현 단계*, (c) ADR 권위는 §10 Q7. 디딤돌1a 가 대체하는 "수단"=boss 직접 제어(상위 v1 폐기), 보존할 "목적"=**직접 means 제어 0 + adaptive loop 0**(BL-4).

| # | 조건 | acceptance criterion (구현 시 충족) |
|---|---|---|
| **(a)** 동등 이상 보안 결과 | §6.1 비교표(정정판) — "boss 직접 제어" vs "boss plan + PlanController" 가 *직접 means 제어 0 + adaptive loop 0* 를 동등 이상 보존 | 본 §6.1 |
| **(b)** 격리 PoC 실증 (구현 단계) | TDD PoC: ① plan 에 means 틀 필드(argv 등) 주입 시도 → schema `additionalProperties:false` 로 reject ② 미등록 worker_kind/alias → reject ③ DAG 사이클/범위초과/자기참조 → reject ④ **(BL-3 교체) boss 가 `desc` 에 임의 NL(파괴 명령·injection payload)을 넣어도 → (i) 해당 subtask 의 argv prefix·alias·isolation 이 plan 무관하게 table/registry 로 고정 (ii) desc 전문이 계획 게이트에 도달 (iii) subtask 결과가 boss 로 환류 0** | 구현 |
| **(c)** ADR 권위 명시 | brief 권위(3/4) + means/ends 정직화. 1b typed contract 도입 시 ADR 권위화 검토 | §10 Q7 |
| **(d)** 자동 회귀 검증 경로 (구현 단계) | pytest 회귀(controller 검증 ①~④) + **신규 import-linter contract: boss(또는 PlanController→boss 단방향) forbidden → orchestrator 역방향**(BL-8 — 현재 미존재, *신규 추가*) + 기존 CI | 구현 |

### §6.1 비교표 (a) — 보존 축 (정정판, BL-1)

| 위협 | boss 직접 제어 (상위 v1, 폐기) | boss plan + PlanController (1a) |
|---|---|---|
| boss 가 **argv 틀·alias·isolation** 지정 | 산문 제약 의존 | **schema 에 해당 필드 부재 + table 소유 = 불가** |
| boss 가 **desc(=worker prompt)** 결정 | 동일하게 가능 | **동일하게 가능 — 단 계획 게이트(desc 전문) + subtask 반영 게이트가 방어**(구조적 불가 아님, 정직) |
| 워커출력 → boss → 다음 실행 결정 (adaptive injection) | 제어루프 존재 → 위험 | **루프 부재 = 재진입 0**(코드: 순차 dispatch 가 boss 재호출 안 함) |
| boss 가 미등록 워커 호출 | 런타임 체크 | **table 룩업 + registry 확인 = 발명 불가** |
| boss 가 무한/폭주 실행 | step limit 필요 | **MAX_STEPS 사람 승인 전 적용** |

→ 5 위협 중 **4개는 1a 가 구조적으로 닫음**. `desc` 1개는 plan-then-execute 의 *본질적 한계*(현 단발 dispatch 도 prompt 출처가 사람 아니면 동일)이며 게이트로 방어 — **이 점을 over-claim 하지 않는 것이 (a) 정직성의 핵심**.

---

## §7 안전 경계 (상위 §3 답습, RT-1 정정)

| # | 경계 | 1a 적용 |
|---|---|---|
| 1 | **adaptive 제어루프 부재** | ✅ §1·§3 — 워커결과→boss→다음결정 환류 0 (injection 제어흐름 1차 방어) |
| 2 | 도구 화이트리스트 | ✅ worker_kind enum → alias table(§5), 미등록 reject |
| 3 | OS sandbox | ✅ 각 subtask = 기존 dispatch workdir 격리 그대로 |
| 4 | permission 게이트 | ✅ 계획 승인 게이트(desc 전문, §4) + 각 subtask 반영 게이트(기존) |
| 5 | RT-1 redaction | ✅ secret-only 보조 — **injection 방어 아님**(상위 B1). plan() 입력·desc 의 NL injection 미차단 — 방어는 #4 게이트 |

- **산출물 전달 0(1a)** → 워커 간 데이터흐름 injection 전파면 *애초에 없음*(1b 에서 typed artifact contract 도입). 1a = 표면 최소 단계.
- **LedgerLog plan 영속 책임(GP-4)**: plan/subtask 이벤트 영속 시 상위 brief §5(B5) "영속 전 exfil 검사"·scrub 책임자 = **board(호출측)**. LedgerLog 는 덤 persister(ledger.py:60). raw desc/output 영속 범위는 구현 시 board 가 scrub 후 적재.

---

## §8 비례성 — 무엇을 *안* 하는가

- **산출물 워커 간 전달 = 디딤돌1b** — 1a 각 subtask 독립.
- **자율 재계획·동적 재분배(L4) = 범위 밖**(프라이데이).
- **"boss → 워커 실행 직결" 영원히 부재** — 항상 PlanController 경유.
- **adaptive boss 호출 0** — plan 1회. 워커 결과 검토는 기존 advise()(사람용 advisory, 제어 환류 0)로 한정.
- **DAG-aware skip·부분 실행 0** — subtask 실패 = 즉시 중단(default). skip 은 1b 이후.

---

## §9 변경 영향 + 다음 단계

### 변경 영향 (구현 단계 — 본 brief 실 변경 0)
- 신규: `BossPlan`/`PlanSubtask` + `BossLLM.plan()`(boss.py) / **`PlanController`(신규 모듈 또는 orchestrator.py)** / `PlanApprovalRequest`(approval.py) / `WORKER_KIND_TABLE` / **신규 import-linter contract**(.importlinter, BL-8).
- 재사용: `Orchestrator.dispatch`(동작 불변), `LedgerLog`(plan/subtask 이벤트), `ApprovalGate` fail-closed 패턴, `StubBoss`(plan scripted).
- 회귀 목표: 기존 342 passed 보존 + 신규 controller 검증 테스트(§6 (b) ①~④).

### 다음 단계
1. brief v1 → 3+1 합의(REVISE) → **brief v1.1**(본 문서) ← 완료
2. **사용자 승인 + §10 Q 결정** ← 현재
3. **디딤돌1a TDD 구현**(별도 브랜치) — RED→GREEN→REFACTOR
4. 구현 후 → CONTEXT/SESSION/INDEX 반영 + 디딤돌1b 상세화(typed artifact contract)

---

## §10 열린 질문 — ✅ 사용자 결정 완료 (2026-05-29, [[project_jarvis_collaborative_orchestration]])

| # | 질문 | ✅ 결정 (사용자 2026-05-29) | 근거 |
|---|---|---|---|
| **Q1** | worker_kind enum 집합 | ✅ **`{code, file}` 기본 + `shell` opt-in/경고**(codex 보수안). `general` 제외 | 사용자 결정 (안전·비례 우선) |
| **Q2** | table 값 | ✅ harness/config 소유. code→CliWorker(claude/codex), file→OllamaWorker(output_filename), shell→TmuxWorker(opt-in 시). boss 발명 불가 | 사용자 구성 |
| **Q3** | MAX_STEPS 기본값 | ✅ **5** (생성자 override 가능) | 4/4 합의 |
| **Q4** | subtask 실패 정책 | ✅ **즉시 중단** (default). DAG-aware skip 은 1b 이후 | 4/4 합의 |
| **Q5** | controller 위치 | ✅ **신규 PlanController + plan 주입형** | 4/4 합의 |
| **Q6** | 계획 승인 게이트 | ✅ **별도 PlanApprovalRequest + ApprovalGate fail-closed 패턴 답습** | 절충 합의 |
| **Q7** | ADR 등록 | ✅ **brief 권위 충분** + means/ends 정직화. 1b typed contract 시 ADR 검토 | 3:1 합의 |

---

## 부록 — 답습 교차 확인
상위 brief v2 §1·§2·§4·§5 / ADR-011 §2.1 (a)~(d) / 헌법 5조 / CLAUDE.md §2·§3 / 합의 보고서 `3plus1-consensus-2026-05-29-jarvis-stone1a-plan-then-execute.md` / [[project_jarvis_collaborative_orchestration]] · [[feedback_pass_scope_overclaim]] (over-claim 차단 — 본 v1.1 핵심) · [[feedback_proportionate_security_personal_tool]] · [[feedback_provider_liquidity]].
