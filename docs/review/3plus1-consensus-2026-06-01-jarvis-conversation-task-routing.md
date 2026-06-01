# 3+1 합의 보고서 — 대화→작업 라우팅 (발견 #UI-1)

> **일자**: 2026-06-01 (119 세션) · **대상 brief**: `docs/phase0/jarvis-conversation-task-routing-design-brief.md` §1~9
> **프로토콜**: CLAUDE.md §3 (Agent A/B/C 병렬 독립 → Reviewer 교차 비교)
> **합의 결과**: REVISE — 핵심 1건(B3→B2) 수정 권고 + BLOCKING 5건. 신뢰 경계 보존 확인.

---

## Phase 2 — 독립 분석 요약

| Agent | 관점 | 결론 |
|---|---|---|
| **A** 구현가능성 | "동작하는가" | **PASS-with-caveats** — 기존 자산만으로 배선 가능. boss grammar 분류 + fail-safe 파싱 필수 |
| **B** 안전/신뢰경계 | "안전한가" | **SAFE-with-conditions** — 게이트 우회 0 확인. 단 brief 문구 정정 + BLOCKING 5 |
| **C** 대안 | "더 나은가" | **부분 수정** — A3·C2·제안버튼 유지 옳음. **B3는 over-engineering → B2(항상 plan) 권고** |

---

## Phase 3 — 교차 비교

### ① 일치 (Consensus, 3자 동의)
- **A3 하이브리드 유지** (규칙 1차 필터 → 작업 의심 시에만 boss 호출, 잡담 0ms 통과·boss 호출 0). A·C 적극, B fail-safe 조건부.
- **C2 백엔드 감지 유지** — boss 호출·redaction·grammar 강제가 전부 백엔드 자산. 프론트 규칙만으론 불가.
- **제안 버튼 유지** — 자동 카드 생성 안 함 = 신뢰 경계(사용자 명시 전환) 정렬. 3자 모두 지지.
- **boss 구조화 출력은 기존 grammar 패턴으로 가능** — `boss.plan()`의 `_PLAN_JSON_SCHEMA`(`boss.py:361`)가 이미 grammar-constrained JSON 강제 중. 신규 schema/메서드 추가는 이 패턴 복제.
- **fail-safe = kind:chat 필수** — B(BLOCKING-2)·C(빈 결과→chat) 동의.

### ② ★ 핵심 쟁점 — B3(복잡도 분기) vs B2(항상 plan)
**세 Agent가 독립적으로 같은 방향으로 수렴**(편향 없는 강한 신호):
- **C(직접 논거)**: plan board는 ① 승인 모달이 **이미 전역 폴링으로 자동 표출**(`index.html:1759` `setInterval(loadJarvisPlans,1000)`, 활성 탭 무관) → multi→plan 라우팅은 **신규 프론트 배선 ≈ 0**. ② plan은 single도 정상 처리(subtask 1개, `boss.py` 구조검증 개수무관) = task의 **상위집합**. ③ task board는 다단계 불가(`Orchestrator` 단일 dispatch).
- **A(독립 발견, 미해결#5)**: single→task 경로의 승인 카드는 **"작업" 탭이 활성일 때만 폴링**(`index.html:2093` `startJarvisPoll`). 흐린 탭(`opacity 0.45`)을 사용자가 직접 켜야 승인 카드가 보임 → **라우팅 UX와 정면 충돌**. ← C의 ②논거를 독립적으로 뒷받침.
- **B(안전 분석)**: task와 plan은 **안전 모델이 다름** — plan은 subtask auto-accept(`jarvis_plan.py:254`, BL-2)라 "단일 승인 → N subtask 자동 반영". B3은 두 경로를 같은 게이트인 양 다룸. 또한 인젝션이 `complexity` 조작 시 plan 경로 유도 가능(BLOCKING-3).

→ **판정: B3 → B2 (항상 plan board) 수정 권고.** 연쇄 효과:
  - `complexity` 필드 제거 → **BLOCKING-3(인젝션 complexity 조작)의 핵심 표면 소멸**.
  - 프론트 분기(`single?/task:/plan`) 제거, 분류·분해를 `boss.plan()` 1회로 통합(C-γ) → 추가 호출 0.
  - task board는 수동 "작업" 탭 입구로 잔존(라우팅과 무관, 제거 아님).

### ③ 불일치 (Divergence)
- 실질 없음. C의 최대 변경(B2 단일화)을 A·B 발견이 오히려 뒷받침 → 진정한 합의.

### ④ 누락 (Gap, 단일 Agent만 포착)
- **B**: ★ brief §3·§4 "실행 착수=사람 승인" 문구가 **코드와 어긋남**. 코드 게이트는 "효과 *반영* 전(before-apply)"이며 **워커는 승인 *전에* 이미 격리 실행**됨(`approval.py:1-6`, `orchestrator.py:125 vs 150`). → 문구 정정 필수.
- **B**: 외부 `CliWorker`(claude/codex)는 송신 redaction 부재(`worker.py:129-131`, OllamaWorker만 redact). 대화 입력이 외부 워커 prompt로 확대되는 경로.
- **A**: `respond_handler` 테스트 seam 부재(분류 함수 monkeypatch 분리 필요) + 분류 호출 timeout 단축(180s→~60s).
- **C**: plan board in-memory 영속성 부재(`_restore` 없음, task엔 있음) — 별도 작은 후속.
- **A+B**: 규칙 1차 필터 키워드(`해줘|만들어|작성…`)와 기존 detectMode(`정리|노트|그림`) **우선순위 충돌** 미정의("보고서 정리해서 파일로 만들어줘"=note? task?).

---

## Phase 4 — 합의 (Consensus Resolution)

### 채택 설계 (REVISE 반영)
```
chat 입력 → /api/respond
  └ [C2] 규칙 1차 필터 (A3-1, 잡담 0ms 통과 · boss 0)
       └ 작업 의심 → boss.plan(message) 1회   ← 분류·분해 통합 (complexity 없음)
            ├ subtasks 공집합 / 파싱 실패 → chat 응답 (fail-CLOSED)
            └ subtasks≥1 → 응답에 {propose:true, prompt} 동봉
  └ 프론트: 제안 버튼 "[작업으로 실행]"
       └ 클릭 → POST /api/jarvis/plan  (분기 없음)
            → 기존 전역 plan 폴링(:1759)이 awaiting 감지 → 승인 모달 자동 표출
```
- **A3·C2·제안버튼**: 확정 유지.
- **B3 → B2**: 항상 plan board. complexity 분류 단계 제거.

### 확정 BLOCKING (구현 전 해소)
| # | 심각도 | 출처 | 내용 |
|---|---|---|---|
| **BL-1** | 高 | B | brief §3·§4 문구 정정: "효과 *반영* 전 승인, 워커 격리 실행은 승인 전". + 구현 제약: **`respond_handler`는 board.create/run 서버 내부 직접 호출 금지** — 제안 페이로드만 반환, 실제 제출은 프론트가 same-origin 엔드포인트 재호출(게이트·CSRF 우회 0 enforcement 지점). |
| **BL-2** | 高 | B·C | boss 응답 파싱 실패·빈 subtasks → **fail-CLOSED = chat**(제안 버튼 미표출). fail-open(실패 시 작업 라우팅) 금지. note/svg except 폴백(`server.py:248,256`) 답습. |
| **BL-3** | 中 | B | 대화 입력이 plan prompt → 외부 `CliWorker` 시 redaction 미적용(`worker.py:129-131`). 입력원이 대화창까지 확대되는지 평가 + 잔여 명시(boss 로컬 분류는 무영향). |
| **BL-4** | 中 | A·B | 규칙 1차 필터 키워드 ↔ detectMode(note/svg) **우선순위 규칙 정의** + 필터 위치 확정(C2 백엔드, detectMode 프론트 자산 재활용 여부 결정). |
| **BL-5** | 中 | A | `respond_handler` 분류 호출 **테스트 seam**(monkeypatch 가능한 모듈 함수 분리) + 분류 timeout 단축(~60s). |

**B2 채택으로 자연 해소**: 旧 BLOCKING-3(인젝션 complexity 조작) 핵심 표면 소멸 · 旧 BLOCKING-5(complexity 분기 배선) 제거.

### 별도 후속 (이번 범위 밖)
- plan board 영속성 부재 → task `_restore` fold 패턴(`jarvis_tasks.py:159`) 이식 (작은 갭).
- qwen3-30b "작업/잡담" 분류 정확도(한국어 변형) 실측 — grammar≠정확도.
- §10 능력 기반 오케스트레이션 (옵션 Y 분리, 별도 brief).

### 신뢰 경계 최종 판정
**보존 확인** — 라우팅은 기존 승인 게이트를 우회하지 않음(respond는 분류만, 제출은 프론트가 same-origin 엔드포인트 재호출). 단 brief 문구가 "실행"과 "반영"을 혼동(BL-1). 제안 버튼(전환) + 승인 모달(반영) 2단계는 코드상 분리 유지(`submit` vs `decision` 별도 라우트).

---

## Reviewer 권고
**REVISE 후 진행** — B3→B2 단순화는 사용자 결정(B3)을 뒤집는 권고이므로 **사용자 재확인 필요**. 재확인 후 BL-1~5 반영해 brief v3 갱신 → TDD 구현 → UI mockup 컨펌(§9) → 재테스트.
