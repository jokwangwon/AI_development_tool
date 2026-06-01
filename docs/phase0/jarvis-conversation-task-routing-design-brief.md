# 설계 brief — 대화→작업 라우팅 (발견 #UI-1)

> **상태**: v3 (3+1 합의 REVISE 반영 — B3→B2 + BLOCKING 5 + 문구정정 / 구현 직전) · **출처**: 119 세션 dogfooding 발견 #UI-1
> **사용자 요청**: "대화를 통해 작업을 던지고 싶다" + "혹은 더 나은 방법 있으면 찾아 적용"
> **합의 보고서**: `docs/review/3plus1-consensus-2026-06-01-jarvis-conversation-task-routing.md`
> **다음 단계**: TDD 구현 → UI mockup 컨펌(§9) → 재테스트 (자동 진입 0)
> **v3 변경**: ① 라우팅 대상 B3(복잡도 분기)→**B2(항상 plan)** 사용자 재확인 채택 ② 신뢰 경계 문구 정정(BL-1) ③ BLOCKING 5건 §8에 명문화

---

## 1. 문제 (dogfooding 발견)

UI 대화창과 작업 실행이 **완전히 분리**되어 있어, 사용자가 대화로 작업을 시킬 수 없다.

```
대화창  (/api/respond)  → ollama 텍스트/노트/SVG 생성만, 실행 0
작업     (/api/jarvis/task | /api/jarvis/plan) → 별도 입구
```

사용자 멘탈모델("자비스에게 말하면 알아서 처리")과 실제 구현이 불일치. 작업 투입구("작업" 탭)는 흐릿한 탭(`opacity 0.45`) 뒤에 숨어 발견성도 낮다.

## 2. 현재 구조 (실측)

### 대화 경로 — `/api/respond` (server.py `respond_handler`)
- `mode` ∈ {chat, note, svg} (3종). 모두 ollama 1회 호출 → 텍스트/노트/SVG 반환·JSONL 저장.
- 프론트 `detectMode(text)` = **키워드 정규식**: `정리|노트|메모|요약`→note, `그림|그려|도식|flow|다이어그램`→svg, else→chat.
- **작업 의도(task) 분기 없음.**

### 작업 경로 — 두 갈래 (★ 통합 시 라우팅 대상 결정 필요)
| | `/api/jarvis/task` (75 entry) | `/api/jarvis/plan` (98 entry) |
|---|---|---|
| 단위 | 단일 작업 카드 | plan = subtask N 분해 |
| boss | advisory만 (BossAdvice) | BossPlanner 분해 (plan-then-execute) |
| 승인 | ui_approver default-deny 300s | plan_approver default-deny 300s |
| 워커 | Orchestrator 단일 dispatch | PlanController 다단계 dispatch |
| UI 연결 | ✅ "작업" 탭 `jarvis-prompt` | ⚠️ 제출 입구 UI 부재(decision/plans GET만) |
| 적합 작업 | "파일 하나 작성" | "코드 작성→그걸 import 실행"(다단계 의존) |

## 3. 목표 / 비목표

**목표**
- 대화창 입력에서 **작업 의도를 감지**하면 plan 경로로 라우팅 → 사용자 제안 → (수락 시) plan 생성·승인 대기.
- 사용자 제시 로직 3단계 충족: (1) 텍스트 분석 (2) 의도 파악 (3) 작업 분류. (※ B2 채택으로 (3)은 "작업이냐 아니냐"까지만 — single/multi 세분류 불요)

**비목표 (이번 범위 밖)**
- plan board 수동 입력 폼 신설(별도) — 단 대화 라우팅이 plan submit을 호출하는 최소 배선은 포함.
- 멀티턴 작업 대화(작업 진행 중 추가 대화로 조정) — 후속.
- plan board 영속성(`_restore`) 보완 — 별도 작은 후속(§8 별도 후속).

## 4. ★ 신뢰 경계 (비협상 제약) — BL-1 정정 반영

자동 라우팅이 **plan 승인 게이트(default-deny)를 우회하면 안 된다.**
- `[[project_minimize_user_intervention]]`(개입 최소화 목표) ↔ trust boundary 직접 충돌 지점.
- ★ **정정(BL-1, 합의 Agent B)**: 코드의 게이트는 "**효과 *반영*(apply) 전**" 게이트지 "실행 전" 게이트가 아니다. 워커는 **승인 *전에* 이미 격리(`isolation.wrap` workdir)에서 실행**되고, 승인 게이트(`ApprovalGate`)는 worker.run *이후* 결과 *반영 전*에 걸린다 (`approval.py:1-6`, `orchestrator.py:125 vs 150`, `jarvis_tasks.py:15`). 보호 대상 = 효과 반영(파일 쓰기/code consume).
- 설계 불변식(정정판): **"의도 감지·분류는 자동, 효과 *반영*은 여전히 사람 승인"**. 라우팅은 "plan을 *생성*해 승인 대기 큐에 올리는 것"까지만 자동. 승인 모달은 그대로.
- ★ **enforcement 지점(BL-1)**: `respond_handler`는 board.create/run을 **서버 내부에서 직접 호출하지 않는다** — 제안 페이로드만 반환, 실제 plan 제출은 프론트가 same-origin 엔드포인트(`POST /api/jarvis/plan`)를 재호출. 이로써 게이트·CSRF·redaction 경로를 우회하지 않는다.
- **2단계 분리 유지**: 제안 버튼 클릭(=대화→작업 *전환* 동의, `submit`) 과 승인 모달(=*반영* 동의, `decision`)은 코드상 별도 라우트. 합치지 말 것.
- 오분류 시에도 안전: 작업 아닌데 제안 → 버튼 안 누르면 무해. 누르면 격리 실행 후 승인 모달에서 거부 가능(노이즈만). 작업인데 대화 처리 → 사용자가 다시 명령(복구 가능).
- ★ **plan auto-accept 주의(합의 Agent B)**: plan은 subtask dispatch가 auto-accept(`jarvis_plan.py:254`, BL-2)라 "단일 plan 승인 → N subtask 자동 반영". plan 모달이 subtask 전체를 **비절단 표시(GP-3)** 하므로 사람이 보고 승인 — 이 비절단 표시가 multi 안전의 핵심.

## 5. 설계 갈림길 + 대안

### 갈림길 A — 의도 파악 수단 (3단계의 핵심)
| 안 | 방식 | 장점 | 단점 |
|---|---|---|---|
| **A1 규칙/키워드** | 기존 `detectMode` 확장(`해줘\|만들어\|작성\|실행\|구현`→task) | 0ms·결정적·계산적(CLAUDE.md 우선원칙) | 자연어 변형에 취약, 오분류 |
| **A2 LLM 분류** | ollama에 "이건 잡담? 작업?" 1회 질의 | 견고, 의도+분류 통합 | 매 대화 LLM 호출 지연, 비용, 비결정 |
| **A3 하이브리드** | A1 규칙 1차 필터 → 의심 시에만 A2 boss 확인 | 흔한 케이스 빠름 + 모호 시 견고, 비용 절감 | 구현 복잡도 ↑ |

### 갈림길 B — 라우팅 대상
- **B1 항상 task board**(단일) — 단순. 다단계 작업은 부적합.
- **B2 항상 plan board**(분해) — 다단계 대응. 단순 작업엔 과함 + UI 제출 배선 필요.
- **B3 복잡도 분류 → 분기** (3단계 "작업 분류"의 본뜻) — 단일=task, 다단계=plan. 가장 사용자 의도 부합, 분류 1단계 추가.

### 갈림길 C — 감지 위치
- **C1 프론트(JS)** — `detectMode`에 task 추가. 빠르나 규칙만 가능(A1 전용).
- **C2 백엔드(`/api/respond`)** — LLM 분류 가능(A2/A3), 단일 진실 지점. 권장(보안·테스트 용이).

## 6. "더 나은 방법" 후보 (사용자 요청 반영)

> 사용자 3단계(분석→파악→분류)는 **별도 분류기**를 함의. 대안:

- **후보 ①: boss 단일 호출 통합** — `/api/respond`가 대화를 boss에게 줄 때, boss가 `{kind: chat|task, complexity: single|multi, (task면) plan}`을 **한 번에** 반환. 의도파악+분류+분해를 1 LLM 왕복으로 통합 → 별도 분류 단계 제거. 단, 모든 대화에 boss 호출(잡담도) = 지연. → **A3 하이브리드와 결합**(규칙으로 잡담 빠르게 거르고, 작업 의심 시에만 boss 통합 호출)이 비용·견고 균형 최적 후보.
- **후보 ②: 명시적 트리거 + 자동 보조** — 대화는 기본 chat, 단 작업 키워드 감지 시 "이거 작업으로 실행할까요? [작업 카드 생성]" **제안 버튼**을 띄움(자동 라우팅 대신 1-클릭). 신뢰 경계와 가장 잘 정렬(사용자가 명시 전환), 오분류 비용 0. UX 변경 작음.

## 7. 결정 확정 (사용자 119 + 합의 REVISE)

| # | 결정 | 채택 |
|---|---|---|
| 1 | 의도 수단 | **A3 하이브리드** — 규칙 1차 필터 → 작업 의심 시에만 boss 호출 (3자 일치 유지) |
| 2 | 라우팅 대상 | ~~B3~~ → **B2 항상 plan board** (합의 REVISE, 사용자 재확인 채택) |
| 3 | 자동 vs 제안 | **제안 버튼 1-클릭** — 자동 카드 생성 안 함, 사용자 명시 전환 (신뢰 경계 정렬) |
| 4 | 감지 위치 | **C2 백엔드 `/api/respond`** — 단일 진실 지점, LLM 분류·redaction 경로 유지 |

> **B2 채택 근거(합의 Phase 3, 3자 독립 수렴)**: ① plan 승인 모달은 이미 전역 폴링 자동 표출(`index.html:1759`) → 배선 ≈ 0. task 모달은 "작업" 탭 활성 시에만 폴링(`index.html:2093`)이라 라우팅 UX와 충돌. ② plan은 single도 정상 처리(subtask 1개) = task의 상위집합. ③ complexity 분류 제거 → 인젝션 조작 표면 소멸. ④ 분류·분해를 `boss.plan()` 1회로 통합(추가 호출 0).

### 확정 흐름 (B2)
```
사용자 대화 입력 → /api/respond
  └ [C2] 규칙 1차 필터 (A3-1, 잡담 0ms 통과 · boss 호출 0)
       ├ 미해당 → 기존 chat/note/svg 처리
       └ 작업 의심 → [A3-2] boss.plan(message) 1회   ← 분류·분해 통합 (complexity 없음)
            (↳ hook: boss가 확신 못 하면 워커 자문 — §10 별도 brief, 여기선 자리만)
            ├ subtasks 공집합 / 파싱 실패 → chat 응답 (★ fail-CLOSED, BL-2)
            └ subtasks ≥ 1 → 응답에 {propose:true, prompt} 동봉
  └ 프론트: 제안이면 "이거 작업으로 실행할까요? [작업으로 실행]" 버튼 렌더 (createElement, XSS 회피)
       └ 클릭(사용자 명시) → POST /api/jarvis/plan  (분기 없음)
            → 기존 전역 plan 폴링(:1759)이 awaiting 감지 → 승인 모달 자동 표출 (게이트 우회 0)
```

### 구현 시 확정 디테일
- 제안 버튼(전환) + 승인 모달(반영)은 **2단계 게이트 유지** (§4, 합치지 말 것). UX는 §9 mockup 컨펌.
- 규칙 1차 필터 키워드 집합 + `boss.plan` 호출 timeout 단축(~60s, BL-5) + 키워드 우선순위(BL-4).

## 8. 합의 결과 (3+1 REVISE — 구현 전 해소할 BLOCKING)

> 전문: `docs/review/3plus1-consensus-2026-06-01-jarvis-conversation-task-routing.md`. A=PASS-w/caveats, B=SAFE-w/conditions, C=부분수정(B3→B2). 신뢰 경계 보존 확인.

### 확정 BLOCKING (구현 전 필수)
| # | 심각도 | 출처 | 내용 | 검증 |
|---|---|---|---|---|
| **BL-1** | 高 | B | §4 문구 정정(반영 전 게이트 ≠ 실행 전) + `respond_handler`는 board.create/run **직접 호출 금지**, 제안 페이로드만 반환 | §4 정정 완료 ✓ / 구현 시 enforce |
| **BL-2** | 高 | B·C | boss 응답 파싱 실패·빈 subtasks → **fail-CLOSED = chat**(제안 미표출). fail-open 금지. note/svg except 폴백(`server.py:248,256`) 답습 | 테스트로 강제 |
| **BL-3** | 中 | B | 대화 입력→plan prompt→외부 `CliWorker` 시 redaction 미적용(`worker.py:129-131`, OllamaWorker만 redact). 입력원 확대 평가 + 잔여 명시 | 구현 시 평가 |
| **BL-4** | 中 | A·B | 규칙 1차 필터 키워드 ↔ detectMode(note/svg) **우선순위 규칙 정의**. 예: "보고서 정리해서 파일로 만들어줘"=note? task? | 규칙 확정 + 테스트 |
| **BL-5** | 中 | A | `respond_handler` 분류 호출 **테스트 seam**(monkeypatch 가능 분리) + `boss.plan` timeout 단축(~60s) | 구현 |

**B2 채택으로 자연 해소**: 旧 인젝션 complexity 조작 표면 소멸 · 旧 complexity 분기 배선 제거.

### 구현 시 활용할 기존 자산 (Agent A·C 실측)
- `boss.plan()` + `_PLAN_JSON_SCHEMA`(`boss.py:361`): grammar-constrained JSON 강제 — 분류·분해 통합에 그대로 복제.
- plan submit 라우트(`jarvis_plan.py:346`) + 프론트 승인모달·전역폴링·decision(`index.html:1729,1742,1759`): **이미 존재** → 신규는 "제안 버튼 클릭 → `POST /api/jarvis/plan`" 1개.
- `create_plan(data)`는 `{prompt}` 하나로 생성(`jarvis_plan.py:148`).

### 별도 후속 (이번 범위 밖)
- plan board 영속성 부재 → task `_restore` fold 패턴(`jarvis_tasks.py:159`) 이식 (작은 갭).
- qwen3-30b "작업/잡담" 분류 정확도(한국어 변형) 실측 — grammar≠정확도.

## 9. UX 컨펌 (`[[feedback_ui_design_confirm_first]]`)
대화창에서 작업 감지 시 화면 표현(자동 카드 / 제안 버튼 / mode-tag "작업")은 **구현 전 mockup 컨펌** 필요. 7-③ 결정과 묶임.

---

## 10. 범위 확장 요청 (119 세션 추가 — ★ 별도 축, 범위 결정 대기)

> 사용자 추가 2건. **라우팅(대화→작업 *진입*)과 다른 축** = "능력 기반 오케스트레이션"(작업 *수행* 시 누가 무엇을). `[[feedback_boss_role_not_smartest]]`(boss≠가장 똑똑, 직원이 더 똑똑할 수 있음, boss=통제 위치) + `[[project_jarvis_collaborative_orchestration]]`와 직결.

### 10-1. boss → worker 자문 ("boss가 모르는 걸 워커에게 물어볼까요")
- boss(로컬 ollama)가 자기 능력 밖을 인식하면 워커(claude/frontier)에게 질의 → 답을 받아 활용.
- 접점: 라우팅 A3-2 boss 분류 단계에서 boss가 **분류/분해를 확신 못 하면** 워커 자문으로 escalate.
- **신뢰 경계**: 워커는 똑똑하나 untrusted(`똑똑함≠신뢰`). boss가 워커 답을 **그대로 신뢰 금지**, 사람 승인 경계 유지. boss=통제 위치(라우팅·승인·기록), 워커=능력 공급원.
- UX 해석 미정: (a) boss가 모르면 자동 워커 자문 vs (b) "워커에게 물어볼까요?" 사용자 **제안 버튼**(제안 패턴 일관). → 결정 필요.

### 10-2. 능력 기반 역할 분담 ("성능 다르니 각자 장점을 써먹고 싶다")
- boss(로컬): 빠름·저렴·항상가용·프라이버시 → 조율/라우팅/분류/단순판단/민감데이터 로컬처리에 강점.
- 워커(frontier): 똑똑함·강력 but 비쌈·외부 → 복잡추론/코드생성/도메인지식에 강점.
- 목표: 작업 특성에 맞는 능력으로 분배 (capability-aware dispatch).
- **데이터 레이어 연계**: `[[project_jarvis_data_layer]]` §10-5 모델 측정 repo가 이미 모델별 실측을 쌓음 → 능력 프로파일의 *증거* 소스 후보.

### 10-3. 미해결 설계 질문 (이 축 합의 시)
1. 능력 프로파일 표현: 정적 config(모델별 강점 선언) vs §10-5 실측 기반 동적 vs 하이브리드?
2. boss "모름" 판단 신호: confidence threshold / 명시적 unknown / self-assessment 프롬프트?
3. 자문 비용·지연: 워커 호출은 비쌈 → 언제 자문할지 게이트(라우팅처럼 사람 제안?).
4. 자문 결과 신뢰: boss가 워커 답을 검증 없이 채택 금지 — 어떤 검증/표시?

### 10-4. ★ 범위 결정 — **옵션 Y 확정 (사용자, 119)**
- 라우팅(§1~9) **먼저** 합의·구현·재테스트로 닫음 → §10은 **별도 brief**로 분리(단계화, `[[feedback_staged_consensus_workflow]]`).
- 라우팅 흐름엔 A3-2 자문 **hook 자리만** 남김(§7 흐름 주석). §10 자체 구현·합의는 라우팅 완료 후 진입.
- §10-1 UX(자동 자문 vs 제안 버튼) 결정은 **§10 별도 brief로 이월**(미정).
