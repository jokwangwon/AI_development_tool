# Jarvis 디딤돌1e 설계 brief — HumanPlanner (사람 직접 plan 공급) (v1.1)

> **본 brief = 설계 정리 한정.** staged: brief v1 → **3+1 합의(4 source, 만장일치 AWC)** → **brief v1.1(본 문서, CN-1~6 흡수 + §5 Q 결정)** → 디딤돌1e TDD 구현. 코드 전 문서 먼저(SDD). 자동 다음 단계 진입 0.

---

**작성일**: 2026-05-30
**Status**: **v1.1 — 3+1 합의(만장일치 APPROVE WITH CONDITIONS, BLOCKING 0) 흡수(CN-1~6) + §5 Q1~Q5 결정(2026-05-30, Q2=boss.py). 디딤돌1e TDD 구현 진입 승인됨.**
**진입 단위**: `BossPlanner` Protocol(IN-2)의 **세 번째 구현** — 사람이 작성한 작업그래프(BossPlan)를 직접 공급. 약한 로컬 boss(StubBoss/OllamaBoss) + frontier CLI(CliPlanner, 1d) 외 **가장 직접적인 plan 공급원 = 사람 자신**.
**상위 문서**: `jarvis-stone1a-...`(plan-then-execute·PLAN-INV) · `jarvis-stone1b-...`(IN-2·artifact contract) · `jarvis-stone1c-...`(하네스 흡수) · `jarvis-stone1d-...`(frontier planner) · 94 entry(dogfooding) · `ADR-013`
**합의 보고서**: `docs/review/3plus1-consensus-2026-05-30-jarvis-stone1e-human-planner.md`(합의 시 생성)
**근거**: 94 dogfooding(약한 boss contract 미생성) · `feedback_boss_role_not_smartest`(IN-2 — 사람이 통제 위치) · `project_jarvis_collaborative_orchestration`(plan-then-execute + 사람 승인) · `feedback_pass_scope_overclaim`(신뢰 over-claim 차단) · `ADR-011` §2.1(means/ends) · `feedback_minimize_user_intervention`(사람 개입 ↔ 통제 trade)

---

## v1.1 변경 이력 (3+1 합의 흡수 — CN-1~6, BLOCKING 0)

> 4 source(A/B/C + codex) 만장일치 AWC. 설계 무효급 0 — 정정 = 정직성(over/under-claim 양방향) + 구조. 합의 보고서: `docs/review/3plus1-consensus-2026-05-30-jarvis-stone1e-human-planner.md`.

| # | v1 → v1.1 | 출처 |
|---|---|---|
| ⭐ CN-1 | **"`_PLAN_JSON_SCHEMA` 형식 *검증*" over-claim 정정** — `_parse_bossplan`(boss.py:449-487)은 **관대 파서**(depends_on/contracts 누락→`[]`, unknown field *무시·거부 아님*). schema `additionalProperties:False`는 ollama format grammar 경로 한정. → "동일 JSON shape + 방어 파싱, 의미검증(enum/DAG/범위)은 controller §3" | A·B·codex(4/4) |
| CN-2 | **"외부 주입 경로 아님" under-claim 정직화** — `from_file(path)`는 임의 path 수용. 현 1e=사람 직접 작성 가정. plan.json 이 워커/외부 산출이 되는 HUD 후속 시 가정 재검토. subprocess/net 실행면 0 은 정확 유지 | B·codex |
| CN-3 | **`from_file` 예외 단일 수렴** — OSError·빈/공백 파일·malformed JSON·UnicodeDecodeError → `RuntimeError`(run_from_planner PLAN_UNAVAILABLE 정합) + `_strip_code_fences` 답습(fence 무해 흡수) | A·C·codex·B |
| CN-4 | **객체/파일 진입 분리** — `HumanPlanner(plan)` + `HumanPlanner.from_file(path)` classmethod 분리(생성자 동시 지정 구조 회피) | A·C·codex |
| CN-5 | **StubBoss 차별화 명시** — HumanPlanner ≠ StubBoss(테스트 stub 의미오염·관찰필드 부재 = 프로덕션 plan 공급원) | C·codex |
| CN-6 | **게이트 실효·파일 크기 정직** — 게이트 *존재* ≠ *실효*(rubber-stamp approver 구조적으로 못 막음, 비례성 허용) + 파일 크기 상한 미적용(자기 파일 비례성) | B |
| Q2 결정 | **모듈 위치 = boss.py**(사용자 결정) — OllamaBoss 가 이미 HTTP IO 로 plan 취득 → HumanPlanner(파일 read)는 대칭("공급원 본체 IO"). planner.py 의 subprocess(실행면)와 이질. StubBoss 이웃 | 사용자 |

---

## §0 배경 — IN-2 의 마지막 꼭짓점 (사람)

디딤돌1a §IN-2(사용자 통찰)는 **plan 공급원은 boss 로 고정되지 않는다**를 확립했다: 약한 로컬 boss / 더 똑똑한 frontier worker / **사람** 모두 `BossPlanner` 를 구현해 plan 을 공급할 수 있고, 누가 공급하든 **PLAN-SOURCE 불변식**(controller 검증 + 사람 승인)을 거친다 — "똑똑함≠신뢰".

지금까지 구현된 공급원:

| 공급원 | 구현 | 특성 | 한계 |
|---|---|---|---|
| 약한 로컬 boss | `StubBoss`/`OllamaBoss.plan` (boss.py) | provider-agnostic 상주, 토큰 0 | **94 dogfooding: contract 거의 미생성** — artifact 전달 미발동 |
| frontier CLI | `CliPlanner` (planner.py, 1d) | 더 똑똑함(codex/claude) | subprocess 신규 실행면(RO 격리 필요, BL-2) · untrusted |
| **사람** | **(미구현 — 본 brief)** | **의도 = 신뢰 원천 · contract 명시 확실** | **정확성≠보장(오타/실수) · 작성=승인 동일인 시 게이트 약화** |

**왜 1순위인가** (94 dogfooding 직접 해법):
- 94 entry 가 드러낸 "약한 boss 는 contracts 를 거의 안 낸다 → artifact 전달이 사실상 미발동"의 가장 직접적 해법. **사람이 직접 contract 를 명시**하면 artifact 전달이 확실히 발동한다(1b/1c 기능이 비로소 실사용).
- `feedback_boss_role_not_smartest`: boss 가치 = 똑똑함이 아니라 **통제 위치**. 사람은 통제 위치의 극단 — plan 의도를 직접 작성. plan-then-execute(`project_jarvis_collaborative_orchestration`)의 "사람 승인" 게이트와 합쳐, **사람이 plan 작성 + 사람이 승인**하는 완전 사람-통제 경로.

---

## §1 핵심 결정 — `HumanPlanner` (얇은 BossPlanner 어댑터)

사람이 작성한 BossPlan 을 controller 에 공급하는 **얇은 어댑터**. 신규 추론·subprocess·네트워크 0 — 입력을 `BossPlan` 으로 변환해 반환할 뿐.

```python
class HumanPlanner:                          # BossPlanner Protocol 구현 (plan(prompt) -> BossPlan)
    """사람이 직접 작성한 작업그래프를 공급하는 planner.

    plan 공급원의 극단 — 사람이 desc/worker_kind/depends_on/contracts 를 직접 명시.
    PLAN-INV (a) 준수: means 틀(argv/alias/isolation/workdir) 필드 *부재* — 사람도
    못 정한다(controller table 소유). PLAN-SOURCE 불변식: 사람이 짠 plan 이라도
    controller 결정적 검증 + 사람 승인 게이트를 거친다(정확성≠보장).
    """
    def plan(self, prompt: str) -> BossPlan: ...
```

**입력 형태** (§5 Q1 ✅ — A+B 둘 다):
- **(A) JSON 파일** `HumanPlanner.from_file(path)`: 사람이 `plan.json`(`_PLAN_JSON_SCHEMA` 와 **동일 JSON shape**) 작성 → 파일 read → `_strip_code_fences` → `_parse_bossplan` *재사용*해 파싱. 실 사람 작성 경로. `CliPlanner.output_file`(planner.py:129-141) 읽기 패턴 답습.
- **(B) BossPlan 객체 직접** `HumanPlanner(plan: BossPlan)`: 프로그래매틱 — 이미 만든 `BossPlan` 을 그대로 반환. 트랙 A 결정성.

→ **CN-4**: 생성자(`plan`)와 팩토리(`from_file`)를 *분리*(동시 지정 구조 회피, codex 권고4).

**CN-1 — `_parse_bossplan` 은 *방어 파서*지 schema 검증기가 아니다**: `_parse_bossplan`(boss.py:449-487)은 데이터 모델 적합성(타입·구조)만 본다 — `depends_on` 누락→`[]`, `contracts` 누락→`[]`, **unknown field 무시**(`item.get(...)` 기반, line 466-468). `_PLAN_JSON_SCHEMA` 의 `additionalProperties:False`(boss.py:286)는 ollama format grammar 경로에서만 발효되며 *파일 경로엔 강제 안 됨*. **의미검증(worker_kind enum·depends_on 범위·DAG 사이클·produced_by 범위)은 전부 controller `run()` §3 책임**(plan_controller.py:162-223). 따라서 사람이 잘못 쓴 plan 도 controller 가 reject — PLAN-SOURCE.

**CN-5 — HumanPlanner ≠ StubBoss**: `StubBoss`(boss.py:142-176)도 객체 직접 반환 + prompt 무시지만, **테스트용**(docstring "결정적 테스트용") + 관찰 필드(`plan_calls`/`fail`/`plan_fail`) 보유 → 프로덕션 사람-공급원으로 쓰면 의미 오염. HumanPlanner 는 (1) `from_file` 실사람 경로 (2) 관찰 필드 *부재*(codex 권고5 — `plan_calls` 불요) = **프로덕션 plan 공급원**으로 명명 분리.

**핵심 정직성** — `prompt` 인자 무시(§5 Q5 ✅): `plan(prompt)` 의 `prompt` 는 약한 boss/frontier 가 "이 작업을 계획하라"고 받는 입력이지만, **사람 공급원은 plan 을 이미 손에 들고 있다** → `prompt` 를 무시하고 사전 작성 plan 을 반환한다(서명 호환만 유지). docstring 에 "서명 호환용이며 반영하지 않음" 명시(거짓 "prompt 반영" 암시 금지). StubBoss.plan(boss.py:172)과 동일 선례.

---

## §2 신뢰 논증 — "사람이 짰으니 안전" over-claim 차단 (⭐ 핵심)

`feedback_pass_scope_overclaim` 답습. 사람 planner 의 가장 큰 함정은 **"사람이 직접 작성 → 신뢰됨 → controller 검증/승인 불필요"** 라는 over-claim 이다. **명시적으로 거부**한다:

| 흔한 over-claim | 정직한 사실 | 방어 |
|---|---|---|
| "사람 plan = 신뢰 → 검증 스킵 가능" | 사람도 **오타·범위초과 depends_on·잘못된 worker_kind·DAG 사이클** 작성 가능 | controller §3 **결정적 검증 그대로**(schema/DAG/table/능력경계) — PLAN-SOURCE |
| "사람이 짰으니 승인 게이트 불필요" | 작성=승인 동일인이면 게이트는 "독립 검토"가 아닌 **"재확인"으로 약화** — 그래도 desc 전문 재확인(작성 시점≠승인 시점)은 *유지*하되 약화를 정직 명시 | 승인 게이트 §4 **유지**(스킵 옵션 도입 0 — §7 Q4) |
| "사람 plan 은 non-adaptive 예외" | 아님 — PLAN-INV (c) 그대로(워커 결과가 plan 갱신 경로 0) | 변경 없음(어댑터일 뿐) |
| "스킵 옵션 0 → 게이트 실효 보장" (CN-6) | 게이트 *존재*는 보장하나 *실효*는 아니다 — 사람이 항상 `True` 반환 approver 를 주입하면 **rubber-stamp**(형식상만 존재). 구조적으로 막을 수 없음 | 비례성상 허용(`feedback_proportionate_security_personal_tool`) + **"존재 ≠ 실효" 정직 명시**. `_approve` default-deny(plan_controller.py:312-313)는 유지 |

**신규 실행면 — subprocess·네트워크 0** (1d 대비 *더 안전*, CN-2 정직화): CliPlanner(1d)는 plan *생성*에 frontier CLI subprocess 를 실행해 fs 쓰기·명령 실행 능력이 신규 실행면이었다(BL-1/BL-2 → RO 격리). **HumanPlanner 는 subprocess·네트워크 실행면 0** — 파일 *읽기*(B는 객체) 뿐 → 1d 의 RO 격리 요구 *불필요*.
- **CN-2 단서**: `from_file(path)`는 임의 path 를 수용하는 일반 read 경로다. "외부 주입 경로 아님"은 *값*이 아니라 **현 1e 사용 가정**(사람이 plan.json 을 직접 작성)에 근거한다. plan.json 이 다른 워커/외부 산출이 되는 순간(§4 HUD plan 편집 후속) 이 가정은 재검토 대상 — 그때 `_parse_bossplan` 은 적대적 JSON 에 견고하나(타입 가드·재귀 0, 단 **파일 크기 상한 미적용** = 자기 파일 비례성상 허용) controller §3 의미검증이 권위.

**means/ends**(`ADR-011` §2.1): HumanPlanner 도 PLAN-INV (a) 준수 — 사람은 `desc`/`worker_kind`/`depends_on`/`contracts`(ends·작업그래프)만 명시하고, **argv prefix·worker alias·격리 backend·workdir(means 틀)는 못 정한다**(controller table 소유). 사람이 임의 argv 를 주입할 구조적 경로 0 — `BossPlan` dataclass 가 means 필드를 *애초에* 갖지 않으므로.

**단서 — desc = 실행 prompt**: 1a BL-1 그대로, `desc` 는 워커 실행 prompt 로 흘러 argv tail 이 된다. 사람이 작성하므로 **사람이 자신의 머신에 자신의 명령을 내리는 것**(공격 모델: 외부 공격자 아님). `feedback_proportionate_security_personal_tool` — solo 개인 툴 비례성: 사람 자기 입력에 대한 추가 sanitize 불필요(승인 게이트 = 자기 desc 재확인).

---

## §3 비례성 — 무엇을 *안* 하는가

| 안 함 | 이유 |
|---|---|
| 대화형 TUI/wizard(단계별 질문) | 파일/객체로 충분 — raw JSON 작성 + controller 게이트가 검증. wizard = 과한 ceremony(`feedback_ceremony_inflation`) |
| HUD UI 통합(브라우저 plan 편집) | 별도 큰 작업 = "실 사용 dogfooding(HUD plan→협업)" 후속 후보. 1e 는 *공급원 추가*에 한정 |
| plan 사전 검증/린트 도구 | controller §3 가 이미 결정적 검증 — 중복. 사람이 raw 작성 → controller 가 reject 메시지로 피드백 |
| 승인 게이트 스킵 옵션 | PLAN-SOURCE 불변식 위반(§2). 작성=승인 동일인이어도 게이트 *유지* |
| JSON schema 신규 정의 | `_PLAN_JSON_SCHEMA`(boss.py) *재사용* — 공급원 간 형식 일관(1d BL-3 답습) |

---

## §4 변경 영향 + 다음 단계

### 변경 영향
- **신규**: `HumanPlanner` 클래스 + `from_file` classmethod — **boss.py**(Q2 ✅, StubBoss/OllamaBoss 이웃). `BossPlan`/`_parse_bossplan`/`_strip_code_fences` 사용. `_strip_code_fences`(worker.py)를 boss.py 가 import 하면 layers 영향 → **boss.py 내 동등 fence-strip 사용 또는 import 방향 확인 필수**(구현 시 grimp 검증). 신규 외부 dep 0.
- **수정 0(코어)**: `run_from_planner`(plan_controller.py)는 `BossPlanner` Protocol 만 알므로 HumanPlanner 를 *그대로* 받는다 — controller 변경 0. 승인/검증 게이트 변경 0.
- **import-linter**: boss.py 배치 → HumanPlanner 가 boss.py 내부 심볼만 쓰면 신규 import 0(기존 layers 유지). 단 `_strip_code_fences`(worker.py 소재) 사용 시 boss→worker import 가 layers(`plan_controller > orchestrator > boss`, boss 최하층) 위반 가능 → **구현 시 boss.py 에 fence-strip 로컬 처리**로 회피(CN-3 답습 — fence 흡수는 단순 문자열 처리).
- **테스트**: 신규(파일 파싱·객체 반환·prompt 무시·예외 수렴·run_from_planner 통합·검증 reject 통과·Protocol 만족·StubBoss 비-혼동).

### 다음 단계 (1e 이후 디딤돌1 후속 잔여)
- 구조화 JSON artifact(평문 bounded→타입드) / plan-level abort / claude planner argv 검증 / exfil 경로·URL catalog — 본 brief 범위 외(별도 진입).
- 실 dogfooding: 사람이 작성한 plan.json → controller → 실 워커 end-to-end(1e 구현 후 별도).

---

## §5 열린 질문 — ✅ 사용자 결정 (2026-05-30)

| # | 질문 | ✅ 결정 | 근거 |
|---|---|---|---|
| **Q1** | 입력 형태 | **(A)+(B) 둘 다** | 파일=실사람 경로, 객체=프로그래매틱. CN-4 로 진입 분리 |
| **Q2** | 모듈 위치 | **boss.py** (StubBoss/OllamaBoss 이웃) | 3+1 2:2 분기 → 사용자 결정. OllamaBoss 가 이미 HTTP IO 로 plan 취득(boss.py:432) → HumanPlanner(파일 read)는 "공급원 본체 IO" 로 대칭. planner.py 의 subprocess(실행면)와 이질 |
| **Q3** | 파일 포맷 | **`_PLAN_JSON_SCHEMA` 와 동일 shape** | 공급원 간 일관. 단 CN-1 — 파일 경로는 schema *강제*가 아닌 `_parse_bossplan` *방어 파싱*(관대) |
| **Q4** | 작성=승인 동일인 시 승인 게이트 | **유지(스킵 0)** | PLAN-SOURCE 불변식. 약화(독립검토 아님·rubber-stamp CN-6)는 정직 명시 |
| **Q5** | `prompt` 무시 처리 | **무시(서명 호환만)** | 불일치 검사 = 추론적 over-engineering(CLAUDE.md §2). StubBoss 선례 |

---

## 부록 — 답습 교차

- `feedback_pass_scope_overclaim`: §2 "사람=신뢰" over-claim 4 함정 사전 차단(brief 단계 선반영).
- `feedback_boss_role_not_smartest` / `project_jarvis_collaborative_orchestration`: IN-2 사람 꼭짓점 = 통제 위치 극단.
- `ADR-011` §2.1 means/ends: PLAN-INV (a) 사람도 means 틀 못 정함.
- `feedback_proportionate_security_personal_tool`: 사람 자기 입력 = solo 개인 툴 공격모델(외부 아님) → 추가 sanitize 불요.
- `feedback_ceremony_inflation`: wizard/UI = 과한 ceremony 회피(§3).
- 1d brief: 어댑터 패턴·`_parse_bossplan` 단일 수렴·열린 질문 형식 답습.
