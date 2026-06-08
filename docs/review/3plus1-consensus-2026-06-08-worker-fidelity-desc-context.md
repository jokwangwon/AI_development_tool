# 3+1 합의 — 워커 충실도(갭6) desc+원본 prompt 동봉 (옵션 B)

> 대상 brief: `docs/phase0/jarvis-worker-fidelity-desc-context-brief.md`
> Agent A(구현)·B(안전성)·C(대안) 병렬 독립 분석 → Reviewer 교차 비교.
> **판정: REVISE** — 방향은 유효하나 BLOCKING 3건 + 대안(frontier planner) 재평가 필요.

---

## Phase 3 — 교차 비교

### ① 일치 (Consensus)
- **구현 가능**: A 명확히 "가능"(`plan_controller.py` 3곳 — `run`/`run_from_planner` 시그니처 +
  dispatch 루프 조립). prompt 는 이미 `card["_prompt"]`(`jarvis_plan.py:160`)와
  `run_from_planner`(`:177`)에 살아있고, Orchestrator.dispatch 첫 인자로 워커까지 자동 관통.
- **⭐ 구분 토큰 위조 방어가 필수** (B·C 독립 수렴 = 만장일치급): `desc`는 boss(untrusted)가
  100% 통제(`boss.py:69`). boss 가 desc 안에 가짜 `[원본 사용자 명령]` 헤더를 써넣어
  **신뢰 표식을 위조**할 수 있다. 평문 delimiter 불충분. → harness 가 원본을 desc *앞*에
  결정적 배치 + boss 위조 불가 구분(별도 메시지 role 또는 desc 라벨 패턴 차단 필터).
- **다단계 Q3 위험 실재**: A·B 단일 subtask 한정 지지 / C 는 더 강하게 — 다단계서 워커가
  원본 전체 보면 "자기 subtask 넘어 전체 시도"(scope 확대, 최소권한 위반).
- **file-only(OllamaWorker) 한정이 안전 완화**: OllamaWorker 는 송신 전 redact(`worker.py:338`),
  CliWorker 는 raw argv(`worker.py:130`). 첫 슬라이스 file-only 면 redaction 커버.

### ② 부분 일치 (Partial)
- **"단일 subtask 우선" 슬라이스 적정성**: A·B = 적절한 Q3 회피책. **C 반대** — dogfood 의
  만화 시스템은 줄거리→대사 **다단계 파이프**(SESSION ③→④)라, 단일 한정 슬라이스는
  **실증 케이스를 못 덮는다**. 중요한 이견.

### ③ 불일치 (Divergence)
- **근본 방향**: B = 옵션 B 를 BLOCKING 충족 시 진행 가능. **C = "B 단독 최선 아님,
  frontier planner(대안 a) 우선 + B 보강"**. C 근거: 근본 원인은 "원본 미전달"이 아니라
  **약한 boss(qwen3-30b, `jarvis_plan.py:52`)의 요약 손실**. B 는 우회, a 는 근본 공략.

### ④ 누락 (Gap)
- **C 만**: frontier planner(대안 a) — `BossPlanner` Protocol(`boss.py:131`)+`planner_model`
  opt(`jarvis_plan.py:64`)가 이미 교체 지점 제공. **신뢰 경계 0 변경**, 합의 부담 가벼움.
  (단 제약: provider liquidity 만족하나 매 plan frontier 호출 = 비용/지연.)
- **B 만**: BLOCKING-3(사람 승인 게이트가 보는 desc ↔ 워커 받는 합성 desc 정합, GP-3),
  원본 prompt 길이 상한 부재(DoS·sentinel truncation), 합성 desc 의 ledger 영속 정책.
- **A 만**: 구체 회귀 지점 — 워커 prompt 동등성 단언 테스트(`test_plan_controller.py:91,104`).
  "user_prompt 없으면 조립 스킵" 분기로 결정적 회피. 최소 변경 3곳·하위호환(키워드+기본 None).

---

## Phase 4 — 합의 도출

### BLOCKING (옵션 B 를 구현한다면 반드시 충족)
- **BL-1 (최우선)**: 원본/desc 신뢰 위계의 **무결성 집행** — boss 가 구분 토큰을 위조 못 함.
  harness 결정적 배치(원본=desc 앞) + 위조 차단(별도 메시지 role 또는 desc 라벨 필터).
  *미충족 시 옵션 B 는 현 desc-only 보다 위험(B: net negative).*
- **BL-2**: 원본 prompt 도 redaction 경로 통과. **file-only 첫 슬라이스 시 OllamaWorker
  내부 redact 가 커버(완화)**. code/shell opt-in 확장 시 BLOCKING 승격.
- **BL-3**: 사람 승인 게이트 표시 desc ↔ 워커 실 dispatch desc 정합(GP-3). 원본 동봉 사실을
  `PlanApprovalRequest` 에 노출.
- (non-blocking 권고): 원본 길이 상한, 다단계는 후속 슬라이스 분리, ledger 영속 정책 명시.

### 핵심 판단 — 방향 재정렬
1. **문제의 근본 원인 = 약한 boss 의 요약 손실**(C, 코드 근거 `_DEFAULT_MODEL`=qwen3-30b).
   B(원본 우회 전달)는 증상 완화, **frontier planner(a)는 근본 공략**이며 인프라 이미 존재.
2. **B 단독은 dogfood 다단계 케이스를 못 덮는다** — "단일 subtask 우선"은 만화 파이프
   (줄거리→대사)에 적용 불가. 실증하려면 다단계가 필요한데 다단계는 Q3 위험.
3. **옵션 A 기각은 정당**(효과 약함 — boss capacity 병목)하나 brief 의 기각 *이유*("untrusted
   텍스트 증가")는 부정확(A 는 신뢰 경계 무변 = 장점). A 는 frontier planner 의 약한 버전.
4. **옵션 C(구조화 계약) 기각 지지** — 단 이유는 "비결정"이 아니라 **스키마 출처**(범용
   자비스에서 boss 가 임의 도메인 스키마 즉석 정의는 비현실). 기존 `Contract`(name+produced_by
   2필드, `boss.py:100`)는 설계 스키마 그릇이 아님(전용 불가).

### 합의 권고 (Reviewer)
**순수 옵션 B 단독 → TDD 직행은 비권장.** 다음 중 사용자 결정:

- **(가) C 권고 — frontier planner(a) 우선 + B 보강** ★ Reviewer 1순위
  순서: ① `_default_planner_builder` 에 frontier(claude/codex) planner 토글 추가(신뢰 경계 0,
  합의 가벼움) → desc 품질 자체 향상 검증 → ② 잔여 손실 있으면 B(첫 subtask 한정 + BL-1
  구분토큰)를 별도 합의로 추가. dogfood 다단계에 무관하게 작동.
- **(나) 옵션 B 진행하되 brief REVISE** — BL-1~3 흡수 + 슬라이스를 명확히(단일 한정의
  한계를 dogfood 비적용으로 명시, 다단계는 후속). 신뢰 위계 무결성(BL-1)이 핵심 신규 설계.
- **(다) 조합** — a 먼저(이번), B 는 a 실측 후 잔여 손실 기준 재판단.

---

## Phase 5 — 사용자 결정 (2026-06-08)

⭐ **사용자 결정 = (가)·(나)·(다) 모두 재정렬**. Agent C 의 "frontier planner 교체" 권고는
**기각**. 근거(사용자): **자비스 존재 이유 = 로컬 모델만으로 동작하는 자율 프로세스**(에르메스
에이전트 참고 + 하네스 도입으로 구축). frontier 의존은 이 철학과 정면 충돌.

- **재정렬된 방향**: C 의 통찰("근본 원인 = 약한 planner 모델, `planner_model` 교체 지점 존재")은
  **유효**하되, 교체 대상 = frontier ❌ → **더 나은 로컬(상업 사용 가능) 모델 ✅**. provider
  liquidity(`planner_model` opt) 그대로 활용, 코드 변경 0.
- **dogfood 증거**: planner `qwen3-30b` → `qwen3-coder-next`(로컬 79.7B) 교체로 step limit 통과
  = 로컬 내 planner 품질차 실재. 기존 V-1 측정(속도 tok/s)과 별개로 **planner 품질(분해·desc
  충실도) 측정**이 신규 차원.
- **옵션 B 보류**: 로컬 planner 개선으로 desc 품질이 충분해지면 B(원본 동봉, BLOCKING 3건) 불요
  가능. 잔여 손실 시 B 를 BL-1~3 흡수해 재합의.
- **다음**: 보유 로컬 모델(qwen3-30b·qwen3:30b-q4·qwen3-coder-next) planner 품질 비교 → 부족 시
  상업가능 로컬 후보 탐색·테스트. → [[project_jarvis_local_boss_direction]] 2026-06-08 후속.
