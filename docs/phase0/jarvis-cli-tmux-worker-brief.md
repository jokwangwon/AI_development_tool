# jarvis CLI tmux 워커 통합 구현 brief (v1.1)

> **작성**: 2026-05-29 (73번째 entry 진입 cycle — 세션 #4)
>
> **v1 → v1.1 흡수 (1 agent 안전 점검, `docs/review/2026-05-29-jarvis-cli-tmux-worker-safety-review.md`, APPROVE WITH CONDITIONS, BLOCKING 2 + 권고 5)**:
> - **B-1**: `src/jarvis/sandbox/ll_sandbox` 가 **이미 빌드·실행가능**(ELF, gitignored) — `--isolation landlock` 가 본 머신에서 *실제 커널 격리 동작*함(dead path 아님). T-11 fail-closed 테스트는 **부재 `sandbox_bin` 주입**(`LandlockIsolation(sandbox_bin="/nonexistent")`)으로 검증(default 경로는 실 격리). main catch는 **`RuntimeError` 한정**(일반 워커 실패 삼킴 금지).
> - **B-2**: `_SENTINEL_RE`(worker.py:127)가 pane 텍스트 *어디서든* `__JARVIS_DONE_<code>__` search → 명령/하위명령이 sentinel echo 시 **거짓 완료 + exit code 위조** 가능("exit code = 결정적 권위" 약화). §3 한계 NOTE 명문 + nonce sentinel = 후속 권고(본 cycle 0, TmuxWorker 본문 변경 0).
> - **권고 흡수**: R-2(Passthrough 위험 CLI `--help` 노출) / R-3(ReviewGuard 실행후-검사 한계 1줄) / R-5(ollama 전용 옵션 + tmux 시 경고). R-1(shlex.join이 메타 quote — 점검 통과, 명문만) / R-4(kill-session finally — 통과).
>
> **방향**: [[project_jarvis_local_boss_direction]] "로컬 사장 + tmux 워커" — vision의 tmux 워커를 72 CLI에 통합. [[project_jarvis_controlled_child_then_friday]] 통제된 자식 함께 쓰기.
>
> **scope**: 72 CLI(`python -m src.jarvis`)에 **`--worker-type {ollama,tmux}`** 추가 — tmux 워커(사용자 관전 가능한 패널 워커) 선택 가능. 기존 `TmuxWorker`(구현+9 test 완료) 배선 + 실 tmux smoke. **새 워커 클래스 0**(TmuxWorker 재사용).
>
> **합의 형태**: 1-2 agent 경량 안전 점검 (사용자 명시 — 실행 능력 escalation 때문에 안전 관점 1 agent 점검 후 TDD). 풀 3+1 아님.
>
> ⚠️ **실행 능력 추가 (핵심 안전 — 72와 차이)**: 72 ollama 워커 = LLM 텍스트 전용(명령 실행 경로 0 = 구조적 안전). tmux 워커 = **명령을 실제 실행**(`bash -lc "<prompt>"` 등). 승인 게이트는 **"반영 전"이지 "실행 전"이 아님** → 명령은 review/gate 무관하게 *실행됨*. 완화: (1) 명령 argv = 사용자 작성(authority) (2) ReviewGuard 위험패턴 flag(출력) (3) isolation.
>
> **isolation**: **Passthrough 기본**(round_trip example 일관 — 비격리 실행 = 사용자 명령 = 사용자 책임) + **`--isolation landlock`** 옵션(LandlockIsolation = 커널 격리, **fail-closed**: sandboxer 미빌드 시 거부, 무격리 fallback 금지).
>
> **선행 답습**: `src/jarvis/worker.py`(TmuxWorker — sentinel/poll/kill, 9 test) + `isolation.py`(Passthrough/Landlock fail-closed) + `src/jarvis/__main__.py`(72 CLI) + `examples/jarvis_v00_round_trip.py`(TmuxWorker 배선 패턴 — argv=["bash","-lc"]+Passthrough)

---

## §1 범위

### 하는 것
1. `--worker-type {ollama,tmux}` (default ollama — 72 동작 보존) + tmux 옵션(`--tmux-argv`/`--isolation`/`--poll-attempts`/`--poll-interval`) (§2)
2. `build_orchestrator` worker-type 분기 — tmux 시 TmuxWorker 배선 (§2)
3. 실행 능력 + isolation 안전 명문 (§3)
4. TDD (worker-type 분기 + tmux 배선 + fake tmux_runner) + 실 tmux smoke (§4)
5. 1 agent 안전 점검 + 금지 + over-claim (§5~§6)

### 하지 않는 것
| # | 영역 | 본 cycle |
|---|------|----|
| 1 | TmuxWorker/isolation/orchestrator **본문 변경** | 0 (배선만, TmuxWorker 재사용) |
| 2 | 새 워커 클래스 / claude CliWorker CLI 통합 | 0 (TmuxWorker 한정) |
| 3 | 무격리 fallback (landlock 실패 시) | 0 (fail-closed — RuntimeError 거부) |
| 4 | 실행 *전* 게이트 / 명령 사전 검열 | 0 (기존 모델 = 반영 전 게이트; 명령=사용자 authority) |
| 5 | net egress 차단 (Landlock ABI4) | 0 (fs 격리 한정, MVP+ 후속) |
| 6 | gate 거버넌스 / 프라이데이 | 0 |
| 7 | 자동 후속 | 0 |

---

## §2 설계 (`__main__.py` 확장)

### D1. args 추가
- `--worker-type {ollama,tmux}` default `ollama`.
- `--tmux-argv` default `"bash -lc"` (shlex.split → argv prefix; positional prompt 가 뒤에 append). 예: `jarvis --worker-type tmux "echo hi"` → tmux 패널에서 `bash -lc "echo hi"`. `--tmux-argv "claude -p"` → `claude -p "<prompt>"`.
- `--isolation {passthrough,landlock}` default `passthrough`.
- `--poll-attempts` int default 60 / `--poll-interval` float default 1.0 (TmuxWorker 기본 답습).
- ollama 전용 옵션(`--output-filename` 등)은 worker-type ollama 시에만 의미(tmux 시 무시 — 경고 또는 silent).

### D2. build_orchestrator worker-type 분기
```
isolation = PassthroughIsolation() if ns.isolation=="passthrough" else LandlockIsolation()
if ns.worker_type == "tmux":
    worker = TmuxWorker(alias=ns.worker_alias, argv=shlex.split(ns.tmux_argv),
                        isolation=isolation, poll_attempts=ns.poll_attempts,
                        poll_interval_s=ns.poll_interval)
else:
    worker = OllamaWorker(alias=ns.worker_alias, model=ns.worker_model,
                          output_filename=ns.output_filename)  # 72 그대로
```
- 나머지 배선(guard/gate/boss/memory/Orchestrator) 동일.

### D3. landlock fail-closed 처리 (graceful)
- `--isolation landlock` + sandboxer 미빌드 → `LandlockIsolation.wrap` 이 RuntimeError(fail-closed). TmuxWorker.run 내부에서 발생 → orchestrator 미포착 → main 까지 전파.
- **main 에서 RuntimeError catch → 명확한 메시지(`make -C src/jarvis/sandbox` 빌드 안내) + exit 1**. 무격리 fallback 0(fail-closed 보존).

---

## §3 실행 능력 + isolation 안전 명문 (핵심)
- **실행 시점**: TmuxWorker.run = 명령 *실행*(worker.run 단계). 승인 게이트(ApprovalGate)는 그 *뒤* "반영 전" = 결과 *수용* 통제이지 *실행* 차단 아님. → **명령은 게이트 무관하게 실행됨**.
- **완화 계층**: (1) argv = 사용자가 CLI에 직접 작성(authority — 사용자가 의도한 명령만) (2) ReviewGuard 가 *출력*의 위험 패턴(rm -rf/sudo/curl|sh 등 10종) flag → 게이트에 노출(반영 통제) (3) isolation = Passthrough(무격리, 사용자 책임) / Landlock(커널 fs 격리, fail-closed).
- **정직 명문**: 본 통합은 "안전한 명령 실행"을 *보장하지 않음*. Passthrough = 무격리(사용자 명령 = 사용자 책임). 커널 격리 원하면 `--isolation landlock`(sandboxer 빌드 선결). gate = 반영 통제이지 실행 통제 아님.
- ReviewGuard/gate 불변식 보존 (72 동일) — tmux 출력도 review→gate 경로. ⚠️ **R-3**: ReviewGuard 는 *출력*(실행 후) 검사 → 위험 명령의 *실행 자체*를 막지 못함(반영만 통제). 정직 표기.
- ⚠️ **B-2 sentinel 위조 한계 (정직 명문)**: TmuxWorker 완료 판정 = pane 텍스트에서 `__JARVIS_DONE_<code>__` search(worker.py:217). 실행 명령/하위 프로세스가 동일 문자열을 echo 하면 **거짓 완료 + exit code 위조** 가능 → "exit code = 결정적 완료 권위"가 *비적대적 명령* 전제에서만 성립. 사용자 authority(명령 작성자=사용자) 맥락에선 수용하나, **nonce sentinel**(세션별 무작위 토큰)로 위조 표면 제거 = 후속 권고(본 cycle TmuxWorker 본문 변경 0).
- ✅ **B-1 landlock 실 동작**: `ll_sandbox` 빌드됨 → `--isolation landlock` = 본 머신에서 실 커널 fs 격리 가능(workdir RW + DEFAULT_RO_PATHS RO + deny-by-default). Passthrough 기본이나 landlock = 실효 옵션(dead 아님).

---

## §4 TDD 계획 (hermetic — fake tmux_runner)

`tests/jarvis/test_cli.py` 확장:
- **T-8 worker-type 분기**: `build_orchestrator(ns(worker_type="tmux", tmux_argv="bash -lc", isolation="passthrough"))` → registry 워커가 TmuxWorker (alias/argv 확인). default(ollama) → OllamaWorker.
- **T-9 arg parse**: `--worker-type tmux --tmux-argv "claude -p" --isolation landlock --poll-attempts 10` 파싱.
- **T-10 main 통합 (fake tmux_runner)**: monkeypatch TmuxWorker 의 default runner 또는 주입 → sentinel pane → applied. (실 tmux 0.) — TmuxWorker 는 tmux_runner 주입 인자가 있으나 build_orchestrator 는 default(real) 사용 → test 는 `monkeypatch.setattr(cli, "TmuxWorker", FakeTmuxWorker)` 로 주입(72 OllamaWorker monkeypatch 패턴 답습).
- **T-11 landlock fail-closed (B-1)**: `ll_sandbox` 가 *빌드돼 있으므로* default 경로는 실 격리 → fail-closed 검증은 **부재 bin 주입**. build_orchestrator 가 `--isolation landlock` 시 `LandlockIsolation()`(default bin) 사용하나, 테스트는 sandboxer 미존재 상황을 모사하기 위해 main 의 RuntimeError catch 를 직접 검증(예: monkeypatch 로 LandlockIsolation 을 항상 RuntimeError raise 하는 fake 로 치환 → main exit 1 + 빌드 안내). main catch = **`RuntimeError` 한정**(일반 워커 실패 삼킴 0).
- **기존 17 + 72 회귀 0**.

### GREEN
- `__main__.py`: args 추가(+ R-5 ollama 전용 옵션 + tmux 시 경고, + R-2 `--help` Passthrough 무격리 경고) + build_orchestrator 분기 + landlock **RuntimeError 한정** catch. import TmuxWorker + PassthroughIsolation/LandlockIsolation + shlex.

### verify
- `.venv/bin/python -m pytest tests/ -q`(회귀 0) + 커버리지 + grimp SDK 경계 0 + scan-source 0.
- ⭐ **실 tmux smoke**: `python -m src.jarvis --worker-type tmux "echo SMOKE_OK" --yes --no-boss --no-memory` → 실 tmux 세션 spawn → `bash -lc "echo SMOKE_OK"` → sentinel capture → applied + "SMOKE_OK" + exit 0. (TmuxWorker 9 test 가 mock-only 였던 실 tmux lifecycle 검증.)

---

## §5 1 agent 안전 점검
- 1 agent(안전 관점) brief 검토 — 초점: (1) 실행 시점 vs 게이트 경계 정확성 (2) landlock fail-closed(무격리 fallback 0) (3) Passthrough 기본의 위험 명문 충분성 (4) ReviewGuard 출력 flag 가 실행을 막지 못함의 정직 표기 (5) tmux_argv shlex 인젝션 표면(사용자 authority지만 따옴표/특수문자). → 점검 후 brief v1.1 흡수 → TDD.

---

## §6 금지 / over-claim
- 금지: TmuxWorker/isolation 본문 0 / 무격리 fallback 0(fail-closed) / 실행 전 게이트 0(기존 모델) / 새 워커 0 / 풀 3+1 0(1 agent 경량) / 자동 후속 0.
- over-claim 차단: "안전한 명령 실행 보장" 0 / "tmux 워커 완성" 0 (bash -lc 기본 + Passthrough; claude/codex CLI 워커 + Landlock 상시 = 별도). "tmux 워커 CLI 선택 + 실 tmux 검증" 한정. gate = 반영 통제(실행 통제 아님) 정직.

---

## §7 다음 단계
사용자 승인 → 1 agent 안전 점검 → brief v1.1 흡수 → TDD → verify + 실 tmux smoke → commit + push + 73 entry. 자동 진입 0.

**본 brief v1 끝.**
