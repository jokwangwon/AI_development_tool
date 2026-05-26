# Jarvis v0.0 동작 sprint brief — Ollama 직결 + tmux worker + round-trip 1회

> **scope**: 자비스 *실 사용 진입* 차단 = 실 LLM Boss 통합 0건 (`src/jarvis/boss.py` StubBoss 한정) 해소.
> **DONE 기준**: boss → worker 실 명령 1회 round-trip 동작 evidence 1건 (실 LLM 응답 raw + tmux log raw).
> **ceremony 압축**: sprint 전체 brief 1회 + 1-agent 진행. 풀 3+1 = 헌법·아키텍처 변경 시만.
> **답습 출처**: `[[v00-sprint-pending]]` + `[[jarvis-local-boss-direction]]` + `[[ceremony-inflation-stop]]` + `[[proportionate-security-personal-tool]]`.

---

## 1. 3 단계 lockdown

| 단계 | 산출 | commit | 사이 cycle |
|------|------|--------|-----------|
| (1) Ollama Qwen3-30B-A3B 직결 1건 | `OllamaBoss(BossLLM)` (stdlib urllib, HTTP `/api/chat`) + TDD + 실 endpoint smoke 1회 | 단일 | 없음 |
| (2) tmux worker 1 spawn | `TmuxWorker(Worker)` — `new-session -d` + `send-keys` + `capture-pane` 회수 | 단일 | 없음 |
| (3) boss → worker round-trip evidence | `examples/jarvis_v00_round_trip.py` — Boss advice ⊕ tmux worker 실 명령 1회 + raw 로그 2건 | 단일 | 없음 |

---

## 2. 단계 (1) 직결 — 설계 고정

- **신규 dep 0** — `httpx` 미설치 + `.importlinter` `ollama` package 금지 답습. stdlib `urllib.request` 단독.
- **endpoint**: `POST http://localhost:11434/api/chat` (Ollama 네이티브 chat). OpenAI 호환 `/v1/chat/completions` 도 candidate 이나 stdlib 호출 단순도 우선.
- **모델 고정**: `qwen3-30b-a3b-instruct-2507-bartowski:latest` (Q4_K_M, 30.5B, MoE 활성 3B). 답습 = `[[v00-sprint-pending]]` Phase 3.5-B 측정 모델.
- **`OllamaBoss` 책무**:
  - `BossLLM` Protocol 구현 (`name`, `advise(AdviceRequest) -> BossAdvice`)
  - 시스템 prompt = "워커 출력 검토 요약 텍스트만 — 명령·콜백 금지" (R2 답습)
  - HTTP 실패 → `RuntimeError` raise (R3: 호출측이 누락→경고 변환)
  - 응답 text → `BossAdvice(summary=text, extra_flags=[], advisory_failed=False)`
- **트랙 A 양립**: StubBoss 변경 0건. 기존 59 test green 보존. OllamaBoss 단위 test = HTTP mock (`urllib.request` patching).
- **실 endpoint smoke**: `python -m src.jarvis.boss_smoke` (or `examples/`) 1회 — Ollama 응답 raw 1건 stdout 출력 (commit log 첨부 0건, evidence 는 단계 (3) round-trip 에서 통합 수집).

## 3. 단계 (2) tmux worker — 설계 고정

- **`TmuxWorker(Worker)`**: alias = 인자, `run(prompt, workdir) -> WorkerResult`.
- **흐름**: `tmux new-session -d -s <task_id> -x 200 -y 50` → `send-keys "<command>" Enter` → 완료 sentinel 대기 (간단: 종료 마커 echo) → `capture-pane -p` → `kill-session`.
- **headless 워커와 직교**: 기존 `CliWorker` (claude `-p` headless) 보존. `TmuxWorker` 는 `Worker` Protocol 별도 구현.
- **격리 위임**: 기존 `LandlockIsolation` 주입점 그대로 (`isolation.wrap(cmd, workdir)` 답습). tmux 실행 자체는 격리 *밖* — workdir 격리는 안에서 실행되는 명령에 적용.
- **MVP-0 답습**: tmux = "관전용" 강등 (헤드리스 우월)이지만, v0.0 *조직 모델* 답습 = 패널 spawn 실 시연 1건 = `[[jarvis-local-boss-direction]]` 워커 모델 입증. 헤드리스 vs tmux *선택* = 후속.

## 4. 단계 (3) round-trip evidence — DONE 기준

- **시나리오**: 사용자 prompt "현재 시간을 echo 해줘" → Orchestrator → TmuxWorker 실행 → 출력 회수 → OllamaBoss advise → ApprovalGate (사람 게이트, default-deny but auto-approve in demo).
- **raw evidence 2건**: (a) Ollama 응답 raw text (advice summary) (b) tmux capture-pane raw output.
- **저장**: `examples/jarvis_v00_round_trip.py` 실행 후 stdout + 별도 log 파일 (`/tmp/jarvis-v00-*.log`) — git tracked 0건 (raw 측정 evidence = 답습 commit log 한정).
- **합격**: exit 0 + Ollama HTTP 200 + tmux capture-pane non-empty + advice summary non-empty.

---

## 5. 비-scope (DEFER 영구)

- 보안 hardening (egress 정책 발효·credential 서명 격리·Layer E/F·multi-host) — `[[v00-sprint-pending]]` 답습. 동작 후 단계.
- M3·M4 결정 *고정* (모델·런타임 freeze) — `[[mvp-staged-roadmap]]` 후속 cycle 영역.
- Phase α defer-lockdown 변경, MVP-1 exit 합의, Operational Readiness PASS, Hermes PMO 격상 — 0건.
- 다중 워커, 자가진화 Layer 1+ — v0.1+ 영역.

---

## 6. 위험 + 완화

| 위험 | 완화 |
|------|------|
| Ollama HTTP 응답 lat ≫ test timeout | (1) test = mock 한정 / 실 호출은 smoke 1회 한정. timeout 60s. |
| stdlib `urllib.request` SSRF 노출 | endpoint = `localhost:11434` 하드코딩 + scheme=http 한정. |
| tmux 세션 leak | `try/finally` `kill-session` + `task_id` UUID prefix. |
| 모델명 hardcoded → Provider Liquidity 위반 | OllamaBoss(model="..." 인자 default 한정. `name` 필드는 BossLLM 답습. 헌법 5조 = 교체 *가능성* 답습 = 인자 주입 충족. |
| `.importlinter` `ollama` 차단 위반 | `urllib.request` 만 사용. `ollama` python SDK import 0건. |

---

## 7. 다음 cycle (sprint 후)

- round-trip 동작 *후* = M3·M4 결정 *고정* cycle 진입 자격 evidence (`[[v00-sprint-pending]]` line 23).
- 또는 Layer D 8 조건 충족 cycle.
- Sprint 종료 marker commit 후 사용자 명시 결정 영역.
