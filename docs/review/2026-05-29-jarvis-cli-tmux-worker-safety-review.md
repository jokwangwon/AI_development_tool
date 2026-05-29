# jarvis CLI tmux 워커 통합 — 1-agent 경량 안전 점검

> **검토자**: 안전 reviewer (1-agent 경량, lens = "안전하고 견고한가?" — 명령 실행 능력 추가의 안전 경계)
> **일자**: 2026-05-29 (73번째 entry cycle, 세션 #4)
> **대상**: `docs/phase0/jarvis-cli-tmux-worker-brief.md` (v1)
> **근거**: 직접 read — `worker.py`, `isolation.py`, `orchestrator.py`, `__main__.py`, `review.py`, `approval.py`, `examples/jarvis_v00_round_trip.py`, `tests/jarvis/test_cli.py`, 실 `src/jarvis/sandbox/ll_sandbox`
> **합의 형태**: 1-agent 경량 (풀 3+1 아님, 사용자 명시) — 핵심 안전 위험 집중, nitpick 지양
> **vendor**: Anthropic Claude

---

## 판정: **APPROVE WITH CONDITIONS**

brief의 핵심 안전 framing(실행 시점 vs gate 경계, fail-closed, Passthrough 위험 명문, ReviewGuard 출력-검사 한계)은 코드와 정합하며 정직하다. over-claim 없음. 단 **BLOCKING 2건**(D3 fail-closed 검증 경로의 환경 의존 누락 1건, sentinel 위조 표면 미명문 1건)을 brief v1.1에 흡수 후 TDD 진입 조건.

---

## 안전 경계 독립 판단 (선)

**72와의 본질 차이는 정확히 식별됨.** OllamaWorker(`worker.py:251~354`)는 LLM 텍스트 수신 + workdir 안 단일 파일 쓰기(realpath traversal 차단, `worker.py:336~354`)로 **임의 명령 실행 경로가 구조적으로 부재**다. TmuxWorker(`worker.py:168~209`)는 `cd {workdir} && {inner}; echo __JARVIS_DONE_$?__`를 tmux 패널에서 **실제 실행**한다. 이는 능력(capability) escalation이 맞고, brief가 이를 1순위로 명문(brief line 11, §3)한 것은 정직하다.

**dispatch 흐름(`orchestrator.py:120~156`)에서 게이트는 실행을 막지 못한다.** `worker.run`(line 125, 명령 실행) → `guard.review`(126, 출력 검사) → `gate.request`(150, 반영 통제). 즉 ApprovalGate default-deny(`approval.py:41~47`)는 **결과 수용 통제**이지 **실행 차단**이 아니다. brief §3 line 70·72가 "게이트 = 반영 통제이지 실행 통제 아님"을 명문 — 코드와 정확히 일치, "실행 전 차단" over-claim 없음. ✅

---

## BLOCKING

### B-1 (D3 fail-closed 검증 경로 — 환경 의존 누락 / 테스트 dead path 위험)
**brief §2 D3 (line 63~66) + §4 T-11 (line 83)**

D3는 "`--isolation landlock` + sandboxer 미빌드 → RuntimeError → main catch → exit 1"을 명문하고, T-11은 "**sandboxer 미존재 시** RuntimeError catch"를 검증한다고 한다.

그러나 **본 머신에는 `src/jarvis/sandbox/ll_sandbox`가 이미 빌드·실행가능(ELF, executable, gitignored)으로 존재**한다. `LandlockIsolation.wrap`(`isolation.py:85~95`)은 default `_DEFAULT_SANDBOX_BIN`(`isolation.py:46`)이 `isfile and X_OK`이면 **RuntimeError를 던지지 않고 실제 wrap → 실 격리 실행**한다.

귀결 2가지 — 둘 다 brief에 미명문:
1. **T-11이 거짓 안전감을 줄 위험**: 기본 경로 그대로 테스트하면 이 머신에서는 RuntimeError가 발생하지 않아 catch 분기가 **실행되지 않거나(dead path)**, 더 나쁘게는 실 `ll_sandbox`가 spawn된다. T-11은 반드시 **존재하지 않는 `sandbox_bin` 주입**(또는 `LandlockIsolation(sandbox_bin="/nonexistent")` 경유)으로 fail-closed 분기를 결정적으로 강제해야 한다. brief는 이 주입 방식을 명문해야 한다.
2. **graceful catch가 RuntimeError "전파 경로"에 의존**: brief D3는 "TmuxWorker.run 내부 발생 → orchestrator 미포착 → main 전파"라 주장한다. `dispatch`(`orchestrator.py:120~156`)에 `worker.run`을 감싸는 try/except가 없음을 확인 — 전파 주장은 **정확하다**. 단 main(`__main__.py:118~125`)에는 **현재 어떤 try/except도 없다**. D3의 "main에서 catch"는 *추가 구현*이며 GREEN(brief line 87 "landlock RuntimeError catch")에 포함됨은 맞으나, **catch 범위가 RuntimeError로 한정**되어야 한다(광범위 `except Exception`은 워커 실 실패까지 삼켜 exit 1 + 빌드 안내라는 오인 메시지를 낼 수 있음). brief는 catch 대상을 `RuntimeError` 명시로 좁혀야 한다.

**조건**: brief v1.1에 (a) T-11의 fail-closed 강제 = `sandbox_bin` 부재 주입 명시, (b) main catch = `RuntimeError` 한정 + 메시지가 워커 일반 실패와 구분됨을 명문.

### B-2 (sentinel 위조 표면 — 누락된 안전 위험)
**brief §3 완화 계층 (line 71) + worker.py:127, 169~209**

완료 sentinel = `__JARVIS_DONE_<exit_code>__`이고 `_SENTINEL_RE`(`worker.py:127`)는 pane 텍스트 **어디서든** 이 패턴을 search(`worker.py:217`)한다. 그런데 sentinel은 워커가 실행하는 **사용자 명령의 출력과 같은 pane**에 섞인다. 사용자/하위 프로세스의 명령이 `__JARVIS_DONE_0__` 문자열을 stdout으로 내면(예: `echo __JARVIS_DONE_0__ && sleep 999`), TmuxWorker는 **실 명령 완료 전에 위조 exit 0으로 조기 종료**하고 `kill-session`(`worker.py:191`)으로 진짜 명령을 끊는다. 즉 **완료 신호 위조 + exit code 위조**가 가능하다.

이것은 brief가 안전 본질로 내세운 "exit code = 결정적 완료 권위"(`worker.py:36`)를 약화시킨다. 사용자 authority 명령이라 악의 시나리오는 낮으나, **prompt injection 체인**(ReviewGuard가 막으려는 바로 그 위협 모델, `review.py:5`)에서 LLM/하위 명령이 sentinel을 출력하면 거짓 완료가 성립한다.

**조건**: brief v1.1 §3에 이 한계를 NOTE로 명문(완화는 본 cycle scope 밖 — TmuxWorker 본문 변경 0 원칙 답습 가능하나, **거짓 권위 over-claim 방지**를 위해 "sentinel은 pane 출력과 분리되지 않으며 위조 가능 — exit code 권위는 비격리 신뢰 모델 하에서만 성립"을 정직 표기). 향후 강화 후보(nonce sentinel = `__JARVIS_DONE_<uuid>_<code>__`)를 후속으로 기록 권고.

---

## 권고 (non-blocking)

### R-1 tmux_argv shlex 인젝션 표면 — 안전하나 명문 권고
**brief D1 (line 45) + worker.py:169~173**

`full_cmd` 구성(`worker.py:173`)은 `shlex.quote(workdir)` + `shlex.join(inner)`를 쓴다. `inner = isolation.wrap([*argv, prompt], workdir)`이고 `shlex.join`은 각 토큰을 안전 quote한다. **prompt에 따옴표·`;`·`$()`·백틱이 들어가도 shlex.join이 single-quote 처리하므로 shell 메타 인젝션은 차단된다.** 단 `--tmux-argv`(brief D1)는 `shlex.split`(brief line 54)으로 사용자가 **의도적으로** argv 토큰을 나눈다 — 이는 인젝션이 아니라 authority(사용자가 prefix를 정함). full_cmd 구성은 **안전하다**(점검 통과). brief v1.1에 "shlex.join이 prompt 메타문자를 quote하여 shell 인젝션 차단, argv 분리는 사용자 authority"를 1줄 명문하면 안전 경계가 명확해짐.

다만 send-keys(`worker.py:188`)는 `full_cmd`를 단일 인자로 tmux에 넘기고 tmux가 키 입력으로 타이핑한다 — tmux send-keys 레벨의 메타(예: 토큰이 `Enter`/`C-c`로 해석되는 키 이름과 충돌)는 full_cmd가 단일 문자열 인자라 영향 없음(별도 `"Enter"` 토큰으로 전송, line 188). 점검 통과.

### R-2 Passthrough 기본 위험 명문 — 충분하나 CLI 노출 권고
brief line 13·71·72가 "Passthrough = 무격리, 사용자 명령 = 사용자 책임"을 명문 — **충분히 정직**하다(`isolation.py:32~42` no-op과 정합). 권고: `--isolation` default가 passthrough(brief D1 line 46)임을 **CLI help 텍스트**에도 "(무격리 — 사용자 책임; 커널 격리는 landlock)"로 노출하여, 문서뿐 아니라 실행 시점에 위험이 보이게 할 것(feedforward 가이드 강화).

### R-3 ReviewGuard 출력-검사 한계 — 정직, 1줄 보강 권고
brief line 71이 ReviewGuard를 "*출력*의 위험 패턴 flag → 게이트 노출"로 명문하고 `review.py:8~9`가 "거짓 안전감 없음, 사람 게이트가 최종 방어"를 자기 한정. **정직하다.** 단 본 cycle은 *실행* 능력을 더하므로, brief v1.1에 "ReviewGuard는 실행 *후* 출력 검사 — 명령 실행 자체를 막지 못함(B-1 게이트 경계와 동일 성질)"을 §3에 1줄 추가 권고(72에서는 실행이 없어 이 구분이 무의미했음).

### R-4 tmux 세션 정리 — 점검 통과
`kill-session`이 `try/finally`(`worker.py:187~191`)로 보장됨 — send-keys/poll 중 예외에도 세션 leak 0. 단 `new-session` 성공 후 `kill-session` 자체가 실패하면(드묾) leak 가능하나 fail-soft로 충분(점검 통과, 변경 불요).

### R-5 ollama 전용 옵션 무시 — silent보다 경고 권고
brief D1 line 48: `--output-filename` 등이 worker-type tmux 시 "무시(경고 또는 silent)". **경고를 택할 것** — 사용자가 산출 파일을 기대하고 tmux를 골랐다면 silent 무시는 혼란. 안전 영향은 없으나 사용자 의도-동작 불일치 방지.

---

## NOTE

- **N-1 workdir 격리**: `_default_workdir_factory`(`orchestrator.py:59~61`)는 `tempfile.mkdtemp`로 워커당 분리 경로 생성. Passthrough에서는 `cd {workdir}`만 하므로 **프로세스가 workdir 밖 fs를 자유 접근**(무격리 본질, 사용자 책임). Landlock에서는 workdir=RW, 나머지 deny-by-default(`isolation.py:85~95`)로 실 격리. 이 차이는 brief가 이미 명문(line 13). 추가 조치 불요.
- **N-2 round_trip 일관성**: brief가 답습한다는 배선 패턴(`examples/jarvis_v00_round_trip.py:51~57`)은 `argv=["bash","-lc"]` + PassthroughIsolation으로, brief D1/D2와 정합. 일관성 확인.
- **N-3 회귀 표면**: build_orchestrator 분기(brief D2)는 ollama default 보존(`__main__.py:90~103` 현 구조 + 기존 T-1~T-6 회귀). T-8~T-11 추가 = 기존 17 test 회귀 0 목표(brief line 84) 타당. 단 B-1의 T-11 dead-path 위험 해소 전 GREEN 진입 금지.
- **N-4 over-claim 점검**: brief §6(line 100~102) "안전한 명령 실행 보장 0", "tmux 워커 완성 0(bash -lc + Passthrough 한정)", "gate = 반영 통제 정직"은 모두 코드와 정합. PASS scope over-claim 보수성(MEMORY) 답습됨. ✅

---

## 결론

핵심 안전 framing은 정직하고 코드 정합적이며, gate≠실행차단 / fail-closed / Passthrough-책임 / ReviewGuard-출력검사 4대 경계가 모두 정확히 명문됐다. **APPROVE WITH CONDITIONS** — BLOCKING 2건(B-1 D3 fail-closed 검증 경로의 환경 의존[ll_sandbox 이미 존재] 흡수 + main catch RuntimeError 한정, B-2 sentinel 위조 표면 NOTE 명문)을 brief v1.1에 흡수 후 TDD 진입. 권고 5건 + NOTE 4건은 정직성·feedforward 강화용(non-blocking).

**1-agent 경량 점검 끝.**
