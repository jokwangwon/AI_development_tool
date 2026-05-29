# 3+1 합의 보고서 — HUD 계획 승인 UI 설계 brief (4 source)

> CLAUDE.md §3 3+1 합의. 검토 대상: `docs/phase0/jarvis-hud-plan-approval-design-brief.md` (DRAFT v1).
> 4 source: Agent A(구현) · Agent B(품질/안전) · Agent C(대안) · codex(cross-vendor). Phase 2 병렬 독립.

**작성일**: 2026-05-30
**종합 판정**: **REVISE → v1.1 정정(BLOCKING 6) 흡수 시 APPROVE WITH CONDITIONS**
**source별**: A=CONDITIONAL-GO · B=REVISE · C=조건부 APPROVE · codex=AWC. 방향(plan_approver HUD 통합, CB 패턴 답습)은 전원 타당 + PlanController default-deny 코드 확인. 그러나 **CB-5(XSS) 누락 + 이중 게이트 미명시 + over-claim 1**.

---

## Phase 3 — 교차 비교

### ① 일치 (Consensus)

| # | 합의 | 출처 |
|---|---|---|
| **CN-1** ⭐ | **CB-5(프론트 XSS) 답습 누락** — brief CB 목록(CB-1/3/4/6/7)에 CB-5(textContent/createElement, innerHTML 금지) 누락. plan 모달은 boss-authored desc + contract name(자연어 허용, plan_controller.py:57-60) 렌더 → task 보드(textContent 강제)보다 XSS 표면 큼. **scrub(secret)≠HTML escape**. GP-3 비절단이 XSS 표면 키움(`<img onerror=fetch('/api/jarvis/...')>` self-XSS→localhost 전권) | B(BL1 최우선)·codex(암시) |
| **CN-2** ⭐ | **이중 게이트 미명시** — PlanController.run step7 의 `self._dispatch`=Orchestrator.dispatch 이고 그 안에 *반영* 게이트(`_gate.request`, orchestrator.py:148). plan 게이트 후 subtask 마다 반영 게이트 N번 차단? brief 미명시. **해석1(반영 게이트 auto-accept, plan 게이트만 사람 차단=default-deny 단일화) 권장** — plan-then-execute "1회 승인" 성립. 기존 `_make_approver`(차단형) 재사용 불가, auto-accept 갈아끼움 | A(BL1) |
| **CN-3** | **plan_id/card/Event = plan thread 전 원자적 선생성**(CB-4) + 검증 실패(VALIDATION_FAILED) 시 즉시 deny-resolve. early-race 0, default-deny 보장 | codex(BL1)·A·B(R1) |
| **CN-4** ⭐ | **"실행 전 통제(더 강함)" over-claim 정정** — planner 추론(ollama/codex)은 승인 *전* 실행(plan_controller.py:151 `planner.plan`). `/plan` POST 자체가 LLM 구동 trigger. 정확히 "**subtask dispatch 전**" 통제(planner 실행 아님). §1 line 33·60 정정 | B(BL2) |
| **CN-5** | **/plan = 실행 trigger → same-origin 적용 + Origin 검증 정밀화** — 기존 `same_origin`(jarvis_tasks.py:386-396)은 Origin 부재 시 허용 + endswith. 신규는 **URL 파싱 scheme/host/port 정확 일치**(suffix 우회 차단). plan trigger(외부 vendor·토큰)는 Origin-부재 허용 비례 가정 약화 → 잔여 명시 | codex(BL2)·B(BL2) |
| **CN-6** | **contracts 명시/암묵 구분 표시 + allow_code_consume 모달 표시**(read-only) — 사람이 실제 능력 경계 인지. 단 **표시≠집행**(controller 가 검증 단계서 강제, 모달 승인 우회 불가 — `_consume_ok`). 모달에 능력 토글 버튼 금지 | codex(BL3)·B(R2) |
| **CN-7** | **Q1 신규 `jarvis_plan.py`**(기존 board 비대/혼선 회피) — C 변형: 상속 금지 + 기존 board dispatch 위임. same_origin/RedactionFilter/Event import 재사용 | A·B·C·codex = 4/4 |
| **CN-8** | **Q3 폴링**(기존 board 도 폴링 `setInterval(loadJarvisTasks,1000)`. WS `/stream`=plan 무관 단방향 daemon push, 양방향 안 됨 + CB-6 표면) | A·B·C·codex = 4/4 |
| **CN-9** | **Q5 subtask = 기존 dispatch 카드 N 분리**(sub_id `f"{task_id}.{i}"` 이미 파생, 카드/Event/취소/pane 재사용. 부모 plan_id 그룹핑) | A·B·C·codex = 4/4 |
| **CN-10** | **Q2 ollama 고정 + planner_builder 주입**(liquidity 충족, UI 토글 후속) / **Q4 file-only 기본 + code/real opt-in** | A·B·C·codex = 4/4 |

### ② 불일치 (Divergence)

| # | 쟁점 | 입장 |
|---|---|---|
| **DV-1** | **Q6 모달 트리거** | 자동 모달: C·codex(default-deny 강제, mockup 일치 — 단 "생성중→승인대기" 상태 분리, 검토 버튼=재시도) / 버튼: A·B(자동=즉시 planner 구동 trigger, 토큰 소모·race). → **절충: 자동 차단 모달 + 상태 분리 + ESC=거부 + (선택)보류**. planner 구동은 명시 행위(작업 제출), 모달은 검증 통과 후 자동 |

### ③ 누락 (Gap)

| # | 사항 | 출처 |
|---|---|---|
| **GP-1** | plan-level abort(승인 후 순차 dispatch 중 중단) 누락 — run() 동기 루프, 중간 hook 없음. **DEFER 명시**([[feedback_pass_scope_overclaim]] scope 누락 인지) | C |
| **GP-2** | PLAN_UNAVAILABLE/VALIDATION_FAILED UI 피드백 — 모달 전 반환(plan_controller.py:96-101). plan 카드 denied/failed 에 reason(scrub) 표시 | C |
| **GP-3** | `/plan-decision` idempotent — awaiting_plan 만 수락, 승인/거부/timeout 된 plan = reject/409 | codex |
| **GP-4** | scrub 적용점 — desc 는 `create()` 의 `[:200]` truncate(jarvis_tasks.py:192) 적용 금지(GP-3 비절단). secret strip 만, "UI 표시 전 + ledger 기록 전" 양쪽 | A·codex |
| **GP-5** | 엣지 — 중복 `/plan` in-flight 가드(동시 planner 토큰 2배), plan 게이트 timeout 값(task 보드 300s 답습), 동시 plan 상한 | B |

---

## Phase 4 — 합의 도출 (Reviewer 최종 판단)

### BLOCKING (v1.1 정정 의무)
| # | 정정 | 근거 |
|---|---|---|
| **BL-1** ⭐ | CN-1 — §4 표에 **CB-5(plan 모달 textContent/createElement 전용, innerHTML 금지 — desc·contract name·alias·flags 전부) 추가**. scrub≠escape 명시. GP-3 비절단일수록 escape 필수 | B·codex |
| **BL-2** ⭐ | CN-2 — 이중 게이트 해소: **plan 게이트만 사람 차단(default-deny), subtask dispatch 는 반영 게이트 auto-accept**. §3/§4 명시 | A |
| **BL-3** ⭐ | CN-4 — "실행 전 통제(더 강함)" → "**subtask dispatch 전** 통제. planner 추론은 승인 전 실행(/plan=trigger)". §1 정정 | B |
| **BL-4** | CN-3 — plan_id/card/Event plan thread 전 원자 선생성 + 검증 실패 deny-resolve | codex·A·B |
| **BL-5** | CN-5 — same_origin **URL 파싱 정확 일치**(scheme/host/port) + /plan same-origin + Origin-부재 잔여 명시 | codex·B |
| **BL-6** | CN-6 — 모달 contracts 명시/암묵 구분 + allow_code_consume read-only 표시(표시≠집행) | codex·B |

### 채택 (일치 → v1.1)
CN-7(신규 jarvis_plan.py 위임) · CN-8(폴링) · CN-9(subtask 카드 N) · CN-10(ollama 고정·file-only opt-in) + GP-1(abort DEFER) · GP-2(reason UI) · GP-3(idempotent) · GP-4(scrub 적용점) · GP-5(엣지).

### 갈림 해소
- **DV-1 (Q6)**: **자동 차단 모달 + 상태 분리("계획 생성 중"→"승인 대기") + ESC=거부 + 검토 버튼=재시도**. planner 구동은 작업 제출(명시 행위), 검증 통과 후 모달 자동(default-deny 강제, mockup 일치). A/B 의 trigger 우려는 "작업 제출=명시 구동"으로 해소.

### 메타 편향 자기진단
brief 가 CB 패턴 답습을 표방하면서 **CB-5(XSS)·CB-2 를 목록에서 누락** — 가장 위험한 웹 표면(boss-authored untrusted 렌더)을 빠뜨림. B 가 최우선 포착. plan-then-execute 의 "강한 통제" 서술이 planner 실행(승인 전)을 가린 over-claim(CN-4)도 B 가 정정 — 안전 source 의 다관점 가치.

---

## §7 Q 합의 권고 (고정은 사용자)

| Q | 합의 권고 | 분포 |
|---|---|---|
| Q1 보드 위치 | **신규 jarvis_plan.py(상속 금지, 기존 board dispatch 위임)** | 4/4 |
| Q2 planner UI | **ollama 고정 + builder 주입**(토글 후속) | 4/4 |
| Q3 plan 푸시 | **폴링**(/api/jarvis/tasks 합류 or /plan-status) | 4/4 |
| Q4 실 워커 | **file-only 기본 + code/real opt-in** | 4/4 |
| Q5 카드 | **subtask = 기존 dispatch 카드 N 분리**(plan_id 그룹핑) | 4/4 |
| Q6 트리거 | **자동 차단 모달 + 상태 분리 + ESC 거부 + 검토 버튼 재시도** | 절충 |
