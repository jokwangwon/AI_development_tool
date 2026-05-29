# Jarvis HUD 계획 승인 UI 설계 brief — PlanController plan_approver HUD 통합 (v1.1)

> **본 brief = 설계 정리 한정.** staged: brief v1 → **3+1 합의(REVISE)** → **brief v1.1(본 문서, BLOCKING 6 + §7 Q 결정)** → TDD 구현(백엔드 → 프론트) + 실 브라우저 검증. 코드 전 문서 먼저(SDD).

---

**작성일**: 2026-05-30
**Status**: **v1.1 — 3+1 합의(REVISE→AWC) 흡수(BLOCKING 6) + §7 Q1~Q6 결정(2026-05-30). UI mockup=전용 차단 모달 컨펌. TDD 구현 진입 승인됨**
**진입 단위**: PlanController 의 **계획 승인 게이트(plan_approver)**를 HUD 에 연결 — 사람이 browser 에서 boss plan(subtasks DAG + contracts + 능력 경계)을 시각 검토 후 1회 승인. plan-then-execute(디딤돌1a~1d) 사용성 완성.
**상위 문서**: `jarvis-stone1a-...` §4 · `jarvis-hud-task-board-integration-brief.md`(CB-1~7) · `docs/review/3plus1-consensus-2026-05-30-jarvis-hud-plan-approval.md`
**근거**: 기존 `jarvis_hud/jarvis_tasks.py`(CB-1~7 합의) · `src/jarvis/plan_controller.py` · `feedback_ui_design_confirm_first` · `feedback_pass_scope_overclaim` · CLAUDE.md §2·§3

---

## v1.1 변경 이력 (3+1 합의 흡수)

| # | v1 → v1.1 | 출처 |
|---|---|---|
| 🔴 BL-1 ⭐ | **CB-5(프론트 XSS) 답습 추가** — plan 모달은 boss-authored desc + contract name(자연어 허용) 렌더 → task 보드보다 XSS 표면 큼. **textContent/createElement 전용, innerHTML 금지**(desc·contract name·alias·flags 전부). scrub(secret)≠HTML escape. GP-3 비절단일수록 escape 필수 | B·codex |
| 🔴 BL-2 ⭐ | **이중 게이트 해소** — PlanController.dispatch=Orchestrator.dispatch(반영 게이트 내장). **plan 게이트만 사람 차단(default-deny), subtask dispatch=반영 게이트 auto-accept**(plan-then-execute "1회 승인" 단일화) | A |
| 🔴 BL-3 ⭐ | **over-claim 정정** — "실행 전 통제(더 강함)" → "**subtask dispatch 전** 통제. planner 추론(ollama/codex)은 승인 *전* 실행(/plan=trigger)" | B |
| 🔴 BL-4 | **plan_id/card/Event = plan thread 전 원자 선생성**(CB-4) + 검증 실패(VALIDATION_FAILED) 즉시 deny-resolve | codex·A·B |
| 🔴 BL-5 | **same_origin URL 파싱 정확 일치**(scheme/host/port, suffix 우회 차단) + /plan same-origin + Origin-부재 잔여 명시 | codex·B |
| 🔴 BL-6 | **모달 contracts 명시/암묵 구분 표시 + allow_code_consume read-only 표시**(표시≠집행, controller 강제) | codex·B |
| R1~R5 | abort DEFER 명시 / validation reason UI / /plan-decision idempotent(awaiting만, 409) / scrub 적용점(desc [:200] 금지) / 엣지(in-flight 가드·timeout 300s·동시 상한) | C·codex·A·B |

---

## §0 배경 — plan 승인 게이트가 아직 CLI/콜백뿐

디딤돌1a~1d 의 plan_approver(default-deny 콜백) = 데모(CLI)+테스트만. HUD 미통합. 기존 HUD(`jarvis_tasks.py`)는 *반영 전* 게이트를 CB-1~7 보안 패턴으로 합의 완료(75 entry). **HUD 계획 승인 UI = 그 패턴을 plan_approver 에 확장.**

---

## §1 핵심 결정 — CB 패턴 답습 + plan 게이트 (시점 정직화, BL-3)

```
사람이 작업 제출(명시 행위) → planner(ollama) plan 1회 실행 ← 이미 실행(승인 전!)
  → controller 검증(schema/DAG/table/budget/능력 경계)
    → [HUD 계획 승인 게이트] ← 신규: 자동 차단 모달 + 사람 1회 승인(default-deny)
      → 승인 시 controller 순차 dispatch(반영 게이트 auto-accept, BL-2)
      → 거부 시 전체 미실행
```

- **통제 시점 정직화(BL-3)**: 본 게이트는 "**subtask dispatch 전**" 통제. **planner 추론(ollama/codex 실행)은 승인 *전* 이미 발생**(plan_controller.py:151) — `/plan` POST 자체가 LLM 구동 trigger. "실행 전(더 강함)" over-claim 금지 — 정확히 *반영 대상 워커 명령(subtask dispatch) 전* 통제(반영 게이트보다 *앞선* 지점이나, planner 실행은 이미 일어남).
- **이중 게이트 해소(BL-2)**: PlanController step7 의 dispatch=Orchestrator.dispatch 에 *반영* 게이트 내장(orchestrator.py:148). → **plan 게이트만 사람 차단(default-deny). subtask dispatch 용 Orchestrator 는 `ApprovalGate(approver=lambda r: True)` auto-accept** 로 구성(반영 게이트 무력화). plan-then-execute "계획 1회 승인" = 유일 사람 차단점. (트레이드오프: 반영 전 워커 출력 미리보기 미표시 — plan desc 사전 검토로 대체, plan 게이트=실행 전 의도 승인.)
- **CB-4 답습**: plan_approver=`threading.Event.wait(timeout=300s)`(default-deny). **plan_id/card/Event = plan thread 시작 전 원자 선생성**(BL-4), 검증 실패 시 즉시 deny-resolve(/plan-decision early-race 0). CB-6: threading.Event.
- **CB-3 답습+BL-5**: /plan·/plan-decision same-origin. **URL 파싱 scheme/host/port 정확 일치**(기존 endswith suffix 우회 차단). Origin-부재 허용(비브라우저)은 잔여로 명시(plan trigger=토큰 소모이므로 단일 사용자 localhost 비례 수용).
- **CB-7 답습**: planner_builder 주입(TestClient hermetic).

## §2 plan 모달 UI (전용 차단, mockup 컨펌 — XSS·표시 정직화)

- **자동 차단 모달**(BL/Q6): 작업 제출 → "계획 생성 중" → 검증 통과 시 "승인 대기" 모달 자동(배경 차단). subtasks DAG(위상정렬+depends_on) + **명시/암묵 contracts 구분**(BL-6) + 능력 경계(allow_code_consume read-only 표시) + [전체 승인][거부]. ESC=거부 + "나중에"=보류. 검토 버튼=재시도용.
- **CB-5(BL-1) ⭐**: 모달 렌더 = **textContent/createElement 전용, innerHTML 금지**. desc·contract name·alias·flags 등 boss/planner-authored 전부 escape. (boss desc 에 `<img onerror=…>` self-XSS→localhost 전권 차단.)
- **CB-1 + GP-3**: 표시 데이터 = `RedactionFilter.scrub`(secret strip) — **"UI 표시 전 + ledger 기록 전" 양쪽**(GP-4). desc 는 **비절단 전문**(GP-3, `[:200]` truncate 금지). **scrub(secret)≠escape(HTML)≠truncate** — 셋 별개. secret strip + HTML escape + 전문.
- **BL-6 표시≠집행**: allow_code_consume·능력 경계는 모달에 *read-only 표시*(사람 인지). 집행은 controller 검증 단계(`_consume_ok`, 승인 전) — 모달 승인이 우회 불가. 모달에 능력 토글 버튼 *금지*.
- 기존 index.html 📊 모달·다크 테마 패턴 답습(외부 라이브러리 0).

## §3 보드 통합 (신규 jarvis_plan.py — 위임, Q1)

- **신규 `jarvis_plan.py`**(JarvisPlanBoard) — 기존 JarvisTaskBoard *상속 금지*, dispatch 는 위임(주입). same_origin/RedactionFilter/Event 패턴 import 재사용(중복 0). plan 게이트(dispatch 전)와 반영 게이트(dispatch 후)의 시점·위협 모델 분리 → CB-5 검증 명료화.
- run_from_planner 백그라운드 thread(`asyncio.to_thread`). plan_approver=ui_plan_approver(Event.wait). 승인 후 controller 순차 dispatch(auto-accept Orchestrator) → 각 subtask = **기존 dispatch 카드 N 분리**(sub_id `f"{task_id}.{i}"`, plan_id 그룹핑, Q5). subtask 반영 게이트는 auto-accept(BL-2).
- 레저(디딤돌0): plan_proposed/plan_approved/plan_denied/plan_failed + subtask 이벤트.
- **validation reason UI(GP-2)**: PLAN_UNAVAILABLE/VALIDATION_FAILED(모달 전 반환) → plan 카드 failed + reason(scrub) 표시.

## §4 안전 경계 (CB-1~7 + plan 특이)

| # | 경계 | 적용 |
|---|---|---|
| CB-1 | redaction | plan 카드/모달 desc·contracts scrub(secret, UI+ledger 양쪽) + desc 비절단(GP-3) |
| **CB-5** ⭐ | **프론트 XSS** | **모달 textContent/createElement, innerHTML 금지**(BL-1) — scrub≠escape |
| CB-3 | same-origin | /plan·/plan-decision URL 파싱 정확 일치(BL-5), Origin-부재 잔여 명시 |
| CB-4 | default-deny | plan_approver Event.wait(300s), Event 원자 선생성(BL-4), 검증 실패 deny-resolve |
| CB-6 | threading.Event | asyncio 금지 |
| CB-7 | builder 주입 | planner_builder hermetic |
| 신규 | plan 게이트=dispatch 전 | subtask dispatch 전 통제(BL-3 — planner 추론은 승인 전). 반영 게이트 auto-accept(BL-2) |
| 답습 | 능력 경계(Q7) | code consume opt-in 모달 read-only 표시(BL-6, 표시≠집행) |

## §5 비례성 — 무엇을 *안* 하는가

- **plan-level abort(승인 후 순차 dispatch 중 중단) = DEFER**(run() 동기 루프, 중간 hook 없음 — 후속, GP-1 scope 누락 명시). **실시간 plan 편집·재계획 = 안 함**(승인/거부만). **WebSocket = 후속**(폴링 시작, Q3). **codex planner UI 토글 = 후속**(ollama 고정, Q2). **실 워커 = file-only 기본**(code/real opt-in, Q4).

## §6 변경 영향 + 다음 단계

### 변경 영향
- 신규 `jarvis_hud/jarvis_plan.py`: JarvisPlanBoard(위임) + ui_plan_approver + plan 카드 + make_jarvis_plan_routes(/plan·/plan-decision·/plan-status). `server.py` 라우트 등록.
- `index.html`: 자동 차단 모달(textContent/createElement, CB-5) + subtasks DAG + contracts 구분 + 능력 표시 + 폴링.
- 재사용: PlanController(변경 0 — auto-accept Orchestrator 주입은 board 책임), build_worker_registry(실 워커 opt-in), LedgerLog, RedactionFilter, 기존 dispatch 카드, same_origin(정밀화).
- 검증: 트랙 A(planner_builder/worker_builder 주입 hermetic, TestClient) + **실 브라우저 playwright**(격리 포트, 90 entry 패턴 — 모달·승인/거부·XSS 수동 검증).

### 다음 단계
1. brief v1 → 3+1 합의(REVISE) → **brief v1.1** + §7 Q 결정 ← 완료
2. **TDD 구현**(백엔드 jarvis_plan.py → 프론트 모달) + 실 브라우저 검증
3. 구현 후 → 문서 반영

## §7 열린 질문 — ✅ 사용자 결정 (2026-05-30, §7 4/4 합의)

| # | 질문 | ✅ 결정 |
|---|---|---|
| Q1 | 보드 위치 | **신규 jarvis_plan.py**(상속 금지, 기존 board dispatch 위임) |
| Q2 | planner UI | **ollama 고정 + planner_builder 주입**(codex 토글 후속) |
| Q3 | plan 푸시 | **폴링**(/plan-status 또는 tasks 합류) |
| Q4 | 실 워커 | **file-only 기본 + code/real opt-in** |
| Q5 | 카드 | **subtask = 기존 dispatch 카드 N 분리**(plan_id 그룹핑) |
| Q6 | 트리거 | **자동 차단 모달 + 상태 분리(생성중→승인대기) + ESC 거부 + 검토 버튼 재시도** |

---

## 부록 — 답습 교차
1a §4(plan 게이트) / jarvis-hud-task-board CB-1~7(특히 CB-5 XSS) / 1b~1d(contracts·능력 경계·planner) / 합의 보고서 / [[feedback_ui_design_confirm_first]] · [[feedback_pass_scope_overclaim]](over-claim·scope 누락) / CLAUDE.md §2·§3.
