# Jarvis 자가진화 Layer 0 brief — 메모리 누적 (append-only)

> **scope**: 자가진화 가장 안전한 첫 단계 = 운영 관찰(`OutcomeReport`)을 영구 누적.
> **safety class**: read-only (관찰 기록만, 동작 변경 0). 게이트 *불요*.
> **DONE 기준**: 3회 dispatch 누적 → JSONL 파일에 3 entry 적재 evidence.
> **답습**: `[[jarvis-local-boss-direction]]` ("자가진화 학습루프 = Layer 0 메모리 누적부터") + `[[proportionate-security-personal-tool]]` + `[[ceremony-inflation-stop]]` (1-agent 직접 진행, 풀 3+1 트리거 0).

---

## 1. Layer 단계 분리

| Layer | 책무 | 안전 등급 | 게이트 |
|-------|------|-----------|--------|
| **0** | 관찰 누적(JSONL append-only) | read-only, 동작 변경 0 | **불요** (관찰만) |
| 1 | 패턴 마이닝 (read Layer 0, 패턴 추출) | read-only Layer 0, 결과 = 보고만 | 보고 ≠ 적용 |
| 2 | 자동 prompt/policy 제안 | 제안 = 텍스트 산출물 | 사람 게이트 *필수* |
| 3 | self-modification (코드/설정 갱신) | git+테스트+사람 승인 강제 | 본격 안전 인프라 |

본 brief = **Layer 0 단독**. Layer 1+ = DEFER (별도 cycle, 자동 진입 0건).

---

## 2. 설계 고정

- **저장 형식**: JSONL (1 entry = 1 line, append-only, 부분 쓰기 방지).
- **저장 경로**: 사용자 주입(`MemoryLog(path=...)`). default 없음(=명시 주입 강제).
- **entry schema** (`OutcomeReport` 의 가독 사본):
  ```json
  {
    "ts": "2026-05-26T15:00:00+09:00",
    "task_id": "...",
    "task_prompt": "...",            // truncated to N chars
    "worker_alias": "...",
    "status": "applied|denied|worker_failed",
    "exit_code": 0,
    "is_error": false,
    "verdict_flags": ["..."],
    "advice_summary": "...",         // truncated, null if no boss
    "advice_failed": false,
    "applied": true
  }
  ```
- **truncation**: `task_prompt` / `advice_summary` 각 2048 chars 상한 (저장량 폭주 차단).
- **민감 정보 차단**: workdir 경로·tmux pane raw·cost_usd 미저장 (Layer 0 = 관찰 *요약* 한정, raw 는 별도 `/tmp/` 로그가 권위).
- **append-only API**:
  - `append(report: OutcomeReport) -> None` — 1 entry 적재
  - `read() -> Iterator[dict]` — 순서 보존 읽기
  - **modify / delete API 없음** (read-only 답습)
- **fail-soft**: 디스크 가득·permission 오류 등 = silent log (orchestrator 진행 정지 X). Layer 0 부재 ≠ 차단 사유.
- **동시성**: 단일 프로세스 가정(`open(..., "a")` POSIX append). 다중 프로세스 = DEFER.

---

## 3. Orchestrator 통합

- `Orchestrator.__init__(memory: MemoryLog | None = None)` 추가 — 미주입 = 누적 0(하위 호환).
- `dispatch` 종료 직전 `self._memory.append(report)` 호출 (`if self._memory`).
- 실패 흡수: `try/except Exception` (fail-soft, 위 §2 답습).
- ApprovalGate / ReviewGuard / Boss 와 동형 = optional 주입, 부재 = 기능만 제거.

---

## 4. 비-scope (DEFER 영구)

- Layer 1+ (마이닝·제안·self-modification) — 별도 cycle, 자동 진입 0.
- 다중 프로세스 동시 쓰기, 파일 회전(rotation), TTL, 압축 — 후속 cycle.
- 외부 시스템 forward (DB, observability platform) — 별도 합의.
- 검색·필터 API (Layer 1 책무, 본 layer 는 raw read 한정).

---

## 5. 위험 + 완화

| 위험 | 완화 |
|------|------|
| JSONL 파일 무한 증가 | task_prompt / advice 2048 chars 상한 + path 사용자 주입(rotation 책임 사용자) |
| 민감 정보 leak (cost·workdir) | schema 에서 제외 |
| 쓰기 실패가 작업 차단 | fail-soft (orchestrator 진행 정지 X, silent log) |
| 다중 프로세스 race | 단일 프로세스 가정 명시 (DEFER 영구) |
| memory 기능이 정책 강제 효과 흉내 | Layer 0 = read-only 관찰 / 정책 강제 = ReviewGuard·ApprovalGate 책무 (책무 분리 답습) |

---

## 6. 합격 조건

- MemoryLog TDD 5+ test green
- Orchestrator 통합 (memory 주입 / 미주입 양립) test green
- 실 evidence = 3회 dispatch → JSONL 3 entry 적재 확인
- 회귀 0 (기존 75 test green 보존)
- import-linter KEPT 유지

DONE 후 commit (단일) + push.
