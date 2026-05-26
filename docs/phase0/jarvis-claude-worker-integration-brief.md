# Jarvis claude 워커 + OllamaBoss 통합 brief

> **scope**: TmuxWorker(shell) 단일 워커 → **CliWorker(claude headless) 추가** = 실 LLM 워커 통합. OllamaBoss(Qwen3) 가 claude 출력을 검토. Layer 0 누적.
> **DONE 기준**: claude 가 실 코딩 작업 1건(fizzbuzz.py 생성) → Qwen3 검토 → Layer 0 entry 1건 + 파일 검증 PASS.
> **답습**: [[jarvis-local-boss-direction]] "사장↔워커" 모델 첫 실 LLM 워커 입증, [[v00-sprint-pending]] "다중 워커" 후속 (d), [[ceremony-inflation]] 1-agent 직접 진행.

---

## 1. 기존 컴포넌트 재사용 (신규 코드 0 — 배선만)

| 컴포넌트 | 출처 | 변경 |
|----------|------|------|
| `CliWorker` | `src/jarvis/worker.py` (MVP-0 트랙 A 발효) | 0 |
| `LandlockIsolation` | `src/jarvis/isolation.py` (MVP-0 트랙 B 발효) | 0 |
| `OllamaBoss` | `src/jarvis/boss.py` (v0.0 sprint 단계 1) | 0 |
| `MemoryLog` | `src/jarvis/memory.py` (Layer 0 발효) | 0 |
| `Orchestrator` | `src/jarvis/orchestrator.py` (memory 주입 가능) | 0 |
| `_claude_runner` 패턴 | `examples/jarvis_e2e_demo.py` (cwd+TMPDIR=workdir) | 답습 |

**본 cycle 산출 = `examples/jarvis_v00_claude_worker.py` 신규 1파일**. src/ 변경 0.

---

## 2. 실 코딩 task 시나리오

- **prompt**: `"Create a Python file named fizzbuzz.py in the current directory that prints fizzbuzz output for numbers 1 to 15. Then stop. Do not run it."`
- **workdir**: tempdir (Landlock RW 영역).
- **claude argv**: `["claude", "--output-format", "json", "--dangerously-skip-permissions", "-p"]`.
- **격리**: LandlockIsolation + `CLAUDE_RO_PATHS` (e2e demo 답습 = `/usr`, `/lib`, `~`, etc.).
- **boss review**: claude JSON `result` 필드 텍스트 → OllamaBoss 한국어 요약.
- **gate**: 자동 승인(demo).
- **memory**: Layer 0 누적 (`/tmp/jarvis-v00-claude-worker-memory.jsonl`).

---

## 3. 검증 (DONE 기준)

| 조건 | 의미 |
|------|------|
| claude exit 0 | 워커 정상 종료 |
| `result.cost_usd > 0` | 실제 토큰 소비 확인 (실 LLM 호출 입증) |
| `workdir/fizzbuzz.py` 존재 | 실 코딩 결과물 입증 |
| 파일 내용에 "fizzbuzz" 또는 "Fizz" 포함 | 의미 있는 코드 생성 입증 |
| advice_summary non-empty | Qwen3 검토 발화 |
| advisory_failed=False | Boss endpoint 정상 |
| Layer 0 JSONL entry 1건 | 관찰 누적 발효 |
| applied=True | 게이트 통과 |

합격 = 8/8 PASS.

---

## 4. 비용

- claude headless 1회 호출 ≈ $0.02~$0.10 (sonnet 4.5 기준, fizzbuzz 단순 작업).
- Ollama Qwen3-30B-A3B 1회 호출 = 토큰 비용 0 (로컬 추론).
- 합계 1회 ≈ $0.05 예상.

---

## 5. 위험 + 완화

| 위험 | 완화 |
|------|------|
| claude 토큰 무한 소비 | --output-format json + 단순 prompt 1회 한정 |
| claude 가 fs 외부 쓰기 시도 | LandlockIsolation = 커널 강제 차단 (MVP-0 트랙 B 답습) |
| claude 인증 누락 | precheck 단계에서 `claude --version` 확인 |
| 모델 응답 불안정 (fizzbuzz 코드 누락) | DONE 조건 = 파일 존재 + "fizzbuzz" 키워드 (느슨한 의미 매칭) |
| Layer 0 JSONL 부풀어 오름 | 별도 path (`/tmp/`) 사용, sprint memory 와 분리 |

---

## 6. 비-scope (DEFER 영구)

- 다중 워커 동시 실행 / 워커 race / 부하 분산 — 별도 합의
- RO 경로 정밀화 (워커별 민감 파일 차단, [[v00-sprint-pending]] (e)) — 별도 cycle
- Layer 2 자동 prompt/policy 제안 (claude 의 prompt 를 boss 가 *제안*) — 사람 게이트 필수
- claude alternative 워커 (codex, opencode) — Provider Liquidity 추후
- E2E 비용 추적·rate limit — 별도 인프라

DONE 후 단일 commit + push + PR comment + memory 갱신.
