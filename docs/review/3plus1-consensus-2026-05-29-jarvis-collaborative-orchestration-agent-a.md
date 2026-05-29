# 3+1 합의 — Agent A (구현 분석가) — jarvis 협업 오케스트레이션 brief

**일자**: 2026-05-29 · **관점**: "실제로 동작하는가?" (구현 가능성·의존성·성능)
**대상**: `docs/phase0/jarvis-collaborative-orchestration-design-brief.md` (DRAFT v1)

---

## Agent A 분석 (구현 가능성)

### 질문 1 — D-1 boss 직접 제어 + schema 매핑: 로컬 모델이 목적 schema 안정 출력?
**⚠️ 조건부 가능 (brief 가 핵심 수단 미명시)**
- 현 `OllamaBoss.advise`(boss.py:211-255) body 에 구조화 출력 강제 필드(`format`) 없음. Ollama `/api/chat` 는 `"format":<JSON schema>` 로 grammar-constrained sampling 지원 → Qwen 30B급도 schema 준수 강제 가능(prompt 설득 아님, 문법상 잘못된 JSON 불가).
- brief §4 schema 예시 최상위 array → ollama `format` 은 object 권장(`{"type":"object","properties":{"subtasks":{...}}}` wrapping). brief 미명시.
- 남는 실패 = 문법 준수 ≠ 의미 타당. depends_on 인덱스 존재/순환은 harness 결정적 검증 + 재시도 1회.

### 질문 2 — §4 수단/목적 매핑의 결정성
**🔴 난점 (현 코드 구조에서 "결정적 매핑" 미성립)**
- `WorkerRegistry.select(alias)`(orchestrator.py:51-56) = alias dict 룩업뿐. "백엔드 REST API" 자연어→워커는 본질적 분류(추론).
- 결정적이 되려면 boss schema 가 **워커 능력 enum(worker_kind: code|shell|file)** 출력 → harness 는 enum→Worker dict 룩업만 결정적. 단 "워커 종류 선택" 주체 = boss(LLM) → brief "수단은 harness 가 정한다"와 부분 모순. **워커 종류 선택은 ends 에 가깝고, argv/경로/격리가 means** 라는 정밀 경계 재정의 필요.

### 질문 3 — §5 L1 영속 레저: memory.py 재사용 정합
**⚠️ 조건부 (read/append 정합, 쓰기 의미 충돌)**
- `MemoryLog`(memory.py:59-107) = append-only JSONL + fail-soft + read iter. 읽기 재사용 정합.
- **결정적 충돌**: MemoryLog 는 read-only 관찰 누적. 카드 상태(running→awaiting→applied)는 가변 → event-sourcing 별도 `LedgerLog` 필요. brief "read API 참조"는 과소평가.
- 고아 마킹/재시작 복구 = event fold("마지막 상태=running → interrupted")로 자연 도출.

### 질문 4 — §5 취소: OllamaWorker 취소 불가?
**✅ brief 진단 정확 (자원 한계 추가 권고)**
- TmuxWorker(worker.py:204-208) try/finally kill-session + on_session 통지 → 외부 kill 가능.
- OllamaWorker(worker.py:320-324) urllib 단발 blocking → 진행 중 취소 핸들 없음. "포기 마킹" 정확.
- 한계: 포기 마킹해도 백그라운드 ollama 추론(GPU/메모리)은 timeout(180s)까지 점유. 진정 취소는 stream:True 전환(L1 범위 밖).

### 질문 5 — L1→L2→L3 순서 강제: 재작성 규모
**⚠️ 조건부 (L1 점진 가능, L2/L3 전면 재설계)**
- L1: dispatch 시그니처 불변 + LedgerLog 주입 + 세션 kill 활용 + 고아 fold = 점진 가능.
- L2: dispatch 위에 orchestrate() 얹기 + boss `plan` 판단 지점 추가(Protocol 확장) = 중간 규모.
- L3: mkdtemp 격리=고립이라 A→B 경로 부재 + 위상정렬 스케줄러 신설 + injection 전파면 = 전면.
- "첫 구현 L1 한정" = 공학적으로 정확. L2/L3 한 cycle 묶지 말 것.

### 질문 6 — 성능/비용: boss 13~18s × N회
**🔴 난점 (L3 실용성 의심, L1 영향 0)**
- 현 dispatch boss 호출 1회. L1 추가 0. L2 = N+1회. L3 제어결정마다 = 1 워크플로우 5~10회, 누적 1~3분.
- 완화(brief 미언급): 분해 1회 고정 + 검토는 ReviewGuard(~0ms) 우선, boss 검토는 flag 시에만(is_error skip 패턴 답습).

## 구현 blocker
1. (질문2) "결정적 매핑" 주장 vs 실제 구조 모순 — enum-constrained schema 로 재정의 필수.
2. (질문3) MemoryLog 직접 재사용 불가 — 별도 LedgerLog(event-sourcing) 필요.
3. (비-blocker) ollama `format` 미언급, boss 호출 횟수 비용 미산정.

## 권고
1. **§4 재서술(필수)**: "boss 가 워커 능력 enum 선택(ends) → harness 가 enum→{argv,경로,격리} 결정적 룩업(means)". WorkerRegistry 능력-enum 룩업 메서드 신설.
2. **structured output 수단 명시(필수)**: ollama `"format"` grammar 강제 + object wrapping + DAG 검증 결정적.
3. **별도 ledger 모듈 명시(필수)**: MemoryLog 와 책무 분리, append-only event-sourcing LedgerLog.
4. **취소 자원 한계 1줄(권고)**.
5. **boss 호출 예산 항목(권고)**.
6. **§2 단계화 지지**: L1 한정 정확, L2·L3 분리 유지.
