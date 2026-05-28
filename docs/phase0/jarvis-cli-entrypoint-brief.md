# jarvis 통합 CLI entrypoint 구현 brief (v1)

> **작성**: 2026-05-28 (72번째 entry 진입 cycle — 세션 #4)
>
> **방향**: [[project_jarvis_controlled_child_then_friday]] — jarvis = 나와 함께하는 **통제된 자식**으로 완성 우선. 현재 jarvis 파이프라인(`orchestrator.dispatch`)은 동작하나 **CLI/entrypoint 부재**(작업마다 example 스크립트 수기) → 터미널에서 호출 가능한 통합 entrypoint 추가 = "함께 쓰기"의 직접 결손 해소.
>
> **scope**: `python -m src.jarvis "작업"` — **기존 컴포넌트 배선만** (새 아키텍처/보안 0). ollama 워커 + boss advisory + **인터랙티브 인간 승인 게이트(default-deny)** + memory. 통제 = 승인 게이트, 함께 = 터미널 호출.
>
> **합의 형태**: 경량 — brief + 직접 TDD + self-review (사용자 명시, 중간 규모 배선 + 기존 컴포넌트 이미 검증 + 새 아키텍처 0 → 풀 3+1 생략, ceremony-inflation 차단 [[feedback_ceremony_inflation]]).
>
> **선행 답습**: `src/jarvis/orchestrator.py`(dispatch + WorkerRegistry) + `approval.py`(ApprovalGate, Approver 콜백 default-deny + fail-closed) + `review.py`(ReviewGuard) + `memory.py`(MemoryLog) + `worker.py`(OllamaWorker, 70 redaction) + `boss.py`(OllamaBoss, 70 redaction) + 71 ollama 실동작 검증.

---

## §1 범위

### 하는 것
1. `src/jarvis/__main__.py` — `python -m src.jarvis "작업"` entrypoint (argparse).
2. 인터랙티브 인간 승인 approver (flags/advice/output **분리 표시**, default-deny, `--yes` 자동 승인).
3. 표준 jarvis 배선 (WorkerRegistry + OllamaWorker + ReviewGuard + ApprovalGate + OllamaBoss + MemoryLog).
4. dispatch 실행 + OutcomeReport 출력 + exit code.
5. (선택적) `bin/jarvis` 얇은 래퍼.

### 하지 않는 것
| # | 영역 | 본 cycle |
|---|------|----|
| 1 | orchestrator/approval/review/memory/worker/boss **본문 변경** | 0 (배선만) |
| 2 | facade.complete() 경유 (CC-0 — boss/worker는 트랙 B urllib 유지, (나) 일관) | 0 |
| 3 | 신규 워커 타입 / tmux 워커 / claude 워커 통합 | 0 (OllamaWorker 한정) |
| 4 | gate 거버넌스(G3) / Hermes PMO / 프라이데이 | 0 (방향상 jarvis 사용성 우선) |
| 5 | 새 아키텍처/보안 결정 | 0 |
| 6 | 자동 후속 | 0 |

---

## §2 설계

### D1. entrypoint = `src/jarvis/__main__.py`
- `python -m src.jarvis "작업 프롬프트"`. 선택적 `bin/jarvis` 래퍼(`exec python -m src.jarvis "$@"`).
- argparse: `prompt`(positional) + `--worker-alias`(default "ollama") + `--worker-model`(default `DEFAULT_MODEL`) + `--boss-model`(default `DEFAULT_MODEL`) + `--no-boss` + `--yes`(자동 승인) + `--memory-path`(default `~/.jarvis/memory.jsonl`) + `--no-memory` + `--output-filename`(워커 파일 작성, default None=텍스트만) + `--task-id`(default = 자동 생성).
- `DEFAULT_MODEL` = 71 검증 모델(`qwen3-30b-a3b-instruct-2507-bartowski:latest`) — **default + override = m3-m4 Liquidity-compliant**(arg 주입, 하드코딩 분기 0).

### D2. 인터랙티브 approver (통제 핵심)
- `make_interactive_approver(input_fn=input, out=...) -> Approver`:
  - ApprovalRequest 표시 — ⚠️ **R10 분리 노출**: (1) 위험 flags (결정적, 별도) (2) boss advisory summary (보조 표시) (3) output_preview (raw). advice에만 의존 금지(green-washing 방어).
  - `input_fn("반영 승인? [y/N] ")` → `{"y","yes"}` (소문자 strip) 만 True, **그 외(빈 입력 포함) False = default-deny**.
- `auto_approver(req) -> bool`: `--yes` 시 True 반환(비대화형).
- ApprovalGate(approver=선택된 approver). approver None 경로는 게이트가 default-deny(이중 안전).

### D3. 배선 (`build_orchestrator(ns) -> Orchestrator`)
- WorkerRegistry + register OllamaWorker(alias, model, output_filename, redactor=RedactionFilter()) — 70 송신 redaction 자동 적용.
- ReviewGuard() (위험 패턴 10종 내장).
- ApprovalGate(approver).
- OllamaBoss(boss_model, redactor=...) unless `--no-boss`.
- MemoryLog(memory_path) unless `--no-memory`.
- Orchestrator(registry, guard, gate, boss=boss, memory=memory).

### D4. 보고 출력 + exit code (`print_report(report, out)`)
- 출력: status + worker_alias + flags + advice(있으면) + output(전체 또는 preview) + applied 여부.
- exit code: APPLIED→0 / DENIED→2 / WORKER_FAILED→1 (스크립트 연동용 구분).

### D5. main(argv=None) -> int
- parse → build_orchestrator → dispatch(prompt, task_id, worker_alias) → print_report → exit code 반환.

---

## §3 TDD 계획 (hermetic — 실 ollama 불요)

`tests/jarvis/test_cli.py` (신규):
- **T-1 auto_approver**: True 반환.
- **T-2 interactive default-deny**: `input_fn`="" / "n" / "no" → False; "y" / "yes" / "Y" → True.
- **T-3 분리 표시 (R10)**: approver 호출 시 out에 flags + advice.summary + output_preview 각각 노출(advice 단독 의존 아님).
- **T-4 arg parse**: prompt + 플래그 파싱 (--yes / --no-boss / --no-memory / --worker-model).
- **T-5 print_report**: APPLIED/DENIED/WORKER_FAILED 각 status + flags + advice 출력.
- **T-6 main 통합 (fake worker 주입)**: `monkeypatch.setattr` 로 OllamaWorker→FakeWorker(canned WorkerResult) + OllamaBoss→StubBoss → `main(["task","--yes"])` → exit 0(applied) / FakeWorker error → exit 1 / `--no-boss`+approver deny → exit 2. (실 ollama/urllib 0 — monkeypatch 주입.)
- **T-7 회귀**: 기존 jarvis 144+ test 무영향.

### GREEN
- `src/jarvis/__main__.py`: DEFAULT_MODEL + build_parser + make_interactive_approver + auto_approver + build_orchestrator + print_report + main. + (선택) `bin/jarvis`.

### verify
- `.venv/bin/python -m pytest tests/ -q`(회귀 0) + 커버리지 70%+ + import-linter(SDK import 0 — __main__은 jarvis 컴포넌트만 import) + scan-source 0 + (선택) 실 ollama smoke 1회(`python -m src.jarvis "say SMOKE" --yes --worker-model qwen...`).

---

## §4 over-claim / 금지
- 명칭 정직: 본 cycle = **CLI entrypoint 배선** 한정. "jarvis 완성 / 통제된 자식 완성" 아님(워커=ollama 1종, tmux/claude 워커 별도, gate 거버넌스 별도). "함께 쓸 수 있는 *기본* 경로 추가" 수준.
- 금지: 컴포넌트 본문 변경 0 / facade 경유 0 / 새 워커 타입 0 / 자동 승인 기본값 0(default-deny 불변) / 프라이데이/Hermes PMO 진입 0 / 자동 후속 0.
- 통제 불변식 보존: ApprovalGate default-deny + fail-closed + R10 분리 표시 — 자동 승인은 `--yes` 명시 시에만(사람 의도).

---

## §5 다음 단계
사용자 승인 → 직접 TDD(RED→GREEN) + self-review → verify(회귀 0 + 선택 실 smoke) → commit + push + 72 entry. 자동 진입 0.

**본 brief v1 끝.**
