# Jarvis 완성도·실작동 범위 분석 — 현황 스냅샷 (2026-06-06)

> **일자**: 2026-06-06 · **브랜치**: `feature/jarvis-output-application-loop`
> **유형**: 현황 분석(스냅샷) — 결정/합의 0건. 후속 brief(반영 루프)의 evidence 기반.
> **방법**: 2-스택 코드 직접 실측(서브에이전트 fan-out → 핵심 경로 직접 교차 검증).
> **북극성**: `[[project_jarvis_general_executor_northstar]]` — "내가 Claude에게 하듯 명령을 수행하는 일반 실행 에이전트".

> **답습**:
> - 메모리: `[[project_jarvis_output_application_gap]]`(본 분석이 재확인한 핵심 갭) · `[[project_jarvis_plugin_architecture]]`(현 해소책) · `[[feedback_pass_scope_overclaim]]`(작동≠완성 framing 분리) · `[[feedback_ceremony_inflation]]`(분석=직접 처리)

---

## 0. 분석 동기

사용자 질문: "자비스가 원하는 조건(북극성)처럼 작동하기 위해 **어느 정도 완성**됐고 **어디까지 실 작업**이 되는가?"

→ 북극성의 4축(명령→계획→승인→실행 + 실행도구)이 실제로 어디까지 **연결되어 작동**하는지를 코드 실측으로 판정.

---

## 1. 핵심 구조 발견 — 2-스택 (코어 + 가동 배선)

```
src/jarvis/     = 결정적 코어 라이브러리. approver·worker·launcher 를 "주입받도록" 설계 (DI)
jarvis_hud/     = 실제 가동 배선. UI approver·TmuxWorker·SubprocessLauncher 를 코어에 주입
```

**중요**: 코어(`src/jarvis/`)만 단독으로 읽으면 `approver=None → 항상 default-deny`로 보여
"실행 불가"로 오판하기 쉽다. 실제로는 `jarvis_hud/`가 구현체를 주입해 end-to-end로 작동한다.
둘은 분리된 게 아니라 **의존성 주입 관계**다.

> 분석 중 서브에이전트 2건이 코어만 보고 "approver 0건·셸 실행 0"으로 오판 → `jarvis_hud/jarvis_tasks.py`·`jarvis_plan.py` 직접 확인으로 정정. (정직 단서: 단일 디렉토리 분석의 함정)

### 배선 증거
| 코어 seam | 가동 배선 구현체 | 위치 |
|-----------|-----------------|------|
| `ApprovalGate(approver=…)` | `_make_approver`(threading.Event, timeout 300s, default-deny) | `jarvis_tasks.py:220-243` |
| `PlanController(plan_approver=…)` | `_make_plan_approver`(동형) | `jarvis_plan.py:165-207, 261` |
| `WorkerRegistry` 워커 | `OllamaWorker`(LLM) / `TmuxWorker`(셸) | `jarvis_tasks.py:51-78` |
| 제어측 `launcher` | `SubprocessLauncher`(Popen+setsid, killpg 자살가드) | `launcher.py:46-94` |

---

## 2. ✅ 실제로 작동하는 것 (북극성 축별)

| 축 | 상태 | 실측 근거 |
|----|------|----------|
| **① 명령→계획(boss)** | 작동 | `OllamaBoss.plan()`(로컬 LLM, grammar-constrained) / `CliPlanner`(codex·claude frontier, subprocess) / `HumanPlanner` 3종. 대화에서 작업 자동 감지 → proposal → `PlanController`가 schema/DAG(graphlib)/contract 결정적 검증 (`plan_controller.py:192-403`) |
| **② 사람 승인 게이트** | 작동 | UI approver = `threading.Event.wait(timeout=300s)`, **default-deny**(timeout·미주입·예외 전부 False). HUD ✅승인/✕거부 → POST `/decision`. plan은 "1회 승인" 후 subtask **auto-dispatch**(BL-2, `jarvis_plan.py:253`) |
| **③ 워커 실행 — LLM** | 작동 | `OllamaWorker`(worker.py:305-411) — 로컬 LLM 추론, 텍스트 또는 workdir 내 파일 1개 |
| **③ 워커 실행 — 셸** | 작동 | `TmuxWorker`(worker.py:151-227) — `isolation.wrap([bash,-lc,prompt])` → tmux new-session → send-keys → capture-pane 폴링(sentinel) → kill-session. **사용자 Pane 관전 + 실행 중 취소(실 kill)** |
| **④ 제어측 lifecycle** | 작동(최고 완성도) | probe(LOW 자율)·start/stop/restart(MEDIUM 1-클릭)·adopt(HIGH cutover). `(pid,starttime)` 소유권·PID recycling 방어·killpg 자살가드·rate 5/60s·누적 100. **미소유 프로세스 안 죽임**(실 voice_lab dogfood 검증) |

### 부가 작동 기능 (HUD)
대화/노트/도식 생성, 다중 대화 관리, 모델 벤치마크 **측정 실행**(PR #53), 플러그인
install/enable/disable/preview(plugin_routes.py), TTS 읽어주기(voice_lab 연계), Layer0/1 자가관찰,
실시간 상태 스트리밍(WS `/stream`).

**결론(작동 골격)**: 명령 → 계획(LLM) → 사람 승인 → 워커 실행(LLM 또는 셸)이 **end-to-end로 실작동**.
HUD 작업 탭에 명령을 넣으면 실제로 실행된다.

---

## 3. ⚠️ 막혀 있거나 미완성인 것 (핵심 갭)

### 갭 1 — 산출물 자동 반영 루프 부재 ★ (최대 갭, 의도된 안전)
- 워커는 **격리 환경(가짜 홈/workdir)에서 실행** → 산출물(파일·코드)이 원본 프로젝트로
  반영되는 **자동 경로가 0**.
- 승인 게이트는 "실행"이 아니라 **"applied 상태 마킹"만 통제**:
  `jarvis_tasks.py:15` — *"승인 게이트 = 반영 전 (실행 통제 아님) — 워커는 dispatch 시 이미 실행"*.
- 결과: **워커가 코드를 짜도 그 결과가 실제 repo에 적용되지 않는다.** 유일한 반영 게이트는
  **plugin install**(work_root → plugins_dir 복사) 경로뿐.
- → 북극성 "명령 수행"의 **후반부(결과를 실제로 적용)가 plugin 외에는 사람 수동 중개 필요**.
- 메모리 `[[project_jarvis_output_application_gap]]`이 기록한 그 갭. 현 해소책 = 플러그인 아키텍처.

### 갭 2 — TmuxWorker 기본 격리 = Passthrough(격리 없음)
- `isolation == "landlock"` 명시 시에만 Landlock, 아니면 `PassthroughIsolation`
  (`jarvis_tasks.py:62-67`). 미지정 시 bash가 격리 없이 실행 — 단 단일 사용자 로컬이라 비례적.

### 갭 3 — boss(로컬 LLM) 계획 품질 한계
- 94 dogfood에서 약한 local boss 한계 기록. frontier CLI(codex/claude) planner로 보완 가능하나
  **HUD 토글이 후속(Q2)** — 현재 기본은 로컬 boss.

### 갭 4 — 재시작 휘발성
- task board가 in-memory. 재시작 시 진행 중 작업 = `interrupted` 고아(자동 복구 없음).
  ledger fold로 **역사만** 복원(`jarvis_tasks.py:159-171`).

---

## 4. 완성도 종합

| 영역 | 완성도 |
|------|--------|
| 명령 → 계획 → 승인 → **실행** | **거의 완성** — 실작동 |
| 실행 결과 → **자동 반영** | **미완성** — plugin 경로만, 나머지 사람 중개 |
| 제어측(외부 프로세스 관리) | **완성** — 안전 경계까지 dogfood 검증 |
| 자가관찰/측정/부가 | 작동 |

**한 줄 결론**: 자비스는 "명령을 받아 격리 환경에서 **실제로 실행하고 사람이 관전·승인하는**"
단계까지 실작동한다. 북극성과의 결정적 갭은 **실행 산출물을 실제 환경에 자동 반영하는 루프**가
(안전상 의도적으로) plugin 경로 외에는 없다는 점이다.

---

## 5. 후속 (자동 진입 0)

- **반영 루프 정면 공략**(갭 1) → 별도 brief → 사용자 검토 → 3+1 합의 → TDD.
  본 분석이 그 evidence.
- 갭 2(격리 기본 강화)·갭 3(frontier planner 토글)·갭 4(재시작 복원)은 독립 소슬라이스 후보.
