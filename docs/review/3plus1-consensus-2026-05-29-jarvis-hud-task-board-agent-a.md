# 3+1 합의 — Agent A (구현 분석가) — jarvis_hud 작업 카드보드 통합

> **cycle**: 2026-05-29 (75번째 entry) · **렌즈**: "실제로 동작하는가?" (구현가능성/동시성/의존성/실현가능성)
> **검토 대상**: `docs/phase0/jarvis-hud-task-board-integration-brief.md` (v1) + `jarvis_hud/server.py` + `jarvis_hud/index.html` + `src/jarvis/{orchestrator,approval,worker,review,memory}.py`
> **독립성(Phase 2)**: 단독 작성 — Agent B/C/codex 미참조. 직접 read + 실행 근거만.

---

## 판정: **APPROVE WITH CONDITIONS**

백그라운드 dispatch + `threading.Event` 승인 게이트 + 작업 보드(dict+Lock) 아키텍처는 **실측 PoC 로 동작 확인**(3 동시 작업 deadlock 0, race 0). 의존성(starlette/uvicorn/httpx/TestClient) 전부 설치됨. `from src.jarvis` import 가 repo root 실행에서 성립. TmuxWorker `on_session` hook 은 74 nonce lifecycle 변경 0 으로 삽입 가능. **단, BLOCKING 3 건 해소 조건부** — 모두 구현 디테일이며 설계 자체를 뒤엎지 않음.

---

## 실측 근거 (직접 실행)

| # | 검증 | 결과 | 근거 |
|---|------|------|------|
| V-1 | baseline `pytest tests/ -q` | **205 passed in 0.13s** (green) | brief §5.1 "205 test" 수치 정확 |
| V-2 | 의존성 설치 | starlette 0.52.1 / uvicorn 0.48.0 / **httpx 0.28.1** / fastapi 0.136.3 / `TestClient` import OK | TestClient 는 httpx 백엔드 필요 — **설치 확인** |
| V-3 | `from src.jarvis...` (repo root cwd) | OK (`'' in sys.path` True) — Orchestrator/ApprovalGate/TmuxWorker/OllamaWorker import 성공 | server.py = `python jarvis_hud/server.py` repo root 실행 시 정합 |
| V-4 | `import jarvis_hud.server` (namespace pkg, `__init__.py` 부재) | OK — `app=Starlette`, routes=12 | TestClient 주입 대상 import 가능 |
| V-5 | TestClient hermetic smoke (`/api/status`, `/`) | 200/200 — FileResponse `jarvis_hud/index.html` (cwd-relative) 50KB 반환 | 테스트는 **cwd=repo root 의존** (NOTE-1) |
| V-6 | **동시성 PoC** — 3 백그라운드 dispatch + per-task Event + Lock 보드 | `awaiting×3` → `/decision` set → `applied/denied/applied`. **deadlock 0, race 0** | brief §2 D1/D4 설계 실증 |
| V-7 | async route 가 thread 보드 폴링 (event loop 블록?) | submit→running, poll1→awaiting, decide→done. **loop 무블록**(Lock 빠른 획득, dispatch 는 off-loop thread) | brief 폴링 구조 정합 확인 |
| V-8 | 14 tmux 테스트 kwargs 생성 패턴 | `alias=/argv=/tmux_runner=/nonce_factory=` — trailing optional `on_session=None` 후방호환 | 74 회귀 0 가능 |

---

## BLOCKING (해소 조건)

### B-1 — 승인 Event 영구 대기 → dispatch 스레드 누수 + 테스트 hang (`orchestrator.py:150` × `approval.py:41~47`)
`Orchestrator.dispatch` 는 `gate.request(req)` → `approver(req)` 를 **inline 블로킹** 호출(`orchestrator.py:150`). UI approver 가 `threading.Event.wait()` 에 **timeout 없이** 들어가면, 사용자가 결정하지 않은 작업의 dispatch 스레드는 **영구 블록**(daemon 이라 서버 종료는 막지 않으나 스레드/메모리 누수). 더 치명적: **hermetic TestClient 테스트(T-2)** 에서 approver 가 동기 호출되면, 작업 제출이 백그라운드 thread 가 아니라 **테스트 스레드에서 동기로 돌면** TestClient 가 hang.
- **조건**: (a) `ui_approver` 의 `Event.wait()` 에 **명시 timeout** 필수(예 default-deny fallback) — brief §8 RT-2 가 "타임아웃/취소 경로" 를 *언급*하나 §2 D1 본문 approver 의사코드엔 timeout 부재 → **명문 고정**. (b) dispatch 는 **반드시 백그라운드 thread** 에서 — 제출 route 는 thread 시작 후 즉시 `{task_id}` 반환(절대 dispatch await/join 금지). PoC V-6/V-7 가 이 구조에서만 무hang 확인.

### B-2 — 테스트 주입 설계가 brief 에 미명세 (`server.py` 전역 routes/handler 구조 × brief §5.1 line 105)
brief §5.1 line 105 "JarvisTaskBoard + ui_approver = 주입 가능 설계(orchestrator factory 주입)" 는 **목표만 선언, 메커니즘 0**. 현 `server.py` 는 **모든 handler 가 모듈 전역 함수 + 전역 `routes`/`app`**(line 536~550) 구조 — fake worker/orchestrator 주입 hook 이 **존재하지 않음**. TestClient 로 실 ollama/tmux 0 을 달성하려면 `OllamaWorker`(localhost:11434 실호출, `worker.py:242`) / `TmuxWorker`(실 tmux, `worker.py:182`) 가 **반드시** fake 로 치환돼야 하는데, 전역 import 한 orchestrator factory 를 테스트가 **monkeypatch 또는 의존성 주입**할 경로가 설계되지 않음.
- **조건**: orchestrator/worker 생성을 **factory 함수**(예 `_build_orchestrator(task_spec) -> Orchestrator`)로 모듈 레벨에 분리하고, 테스트가 `monkeypatch.setattr(server, "_build_orchestrator", fake_factory)` 또는 `JarvisTaskBoard` 인스턴스를 `app.state` 주입으로 치환 가능하게 **명문 고정**. 이 hook 없이는 §5.1 "fake worker 주입 — 실 ollama/tmux 0"(T-1~T-7) 가 **구현 불가**.

### B-3 — `/decision` 결정 후 set 했는데 Event 부재 시 race (`server.py` 신규 route × board 상태 전이)
`/decision` 이 Event 를 set 하려면 그 시점 보드에 per-task Event 가 이미 존재해야 한다. 그러나 dispatch 스레드가 아직 worker.run(`time.sleep` 또는 실 LLM 180s) 단계라 **approver 에 도달 전**이면 보드엔 Event 가 없음(`진행중` 상태). 이때 `/decision` 이 **early-arrival** 하면 결정이 유실(set 할 Event 없음) → 이후 approver 가 새 Event 를 만들어 영구 대기. PoC 는 `time.sleep(0.3)` 으로 awaiting 도달을 보장했으나 **실 운영은 타이밍 비결정적**.
- **조건**: `/decision` 은 (a) 보드에 결정을 **먼저 저장**(`decision='accept'`)하고 (b) Event 존재 시 set, **부재 시에도 저장된 결정을 approver 가 wait 진입 시 즉시 확인**(저장된 결정 우선 체크 → wait skip). 즉 approver 진입부에서 `if board[id].decision is not None: return ...` early-check. 또는 Event 를 작업 제출 시점에 미리 생성(per-task Event 를 board 항목과 동시 생성). **brief §2 D1 의사코드는 "approver 가 Event 생성"** 순서라 이 race 노출 — 순서 고정 필요.

---

## 권고 (non-blocking)

- **R-1 (WebSocket 재사용)**: 하나는 이미 `/stream` WS(`server.py:32~45`, `522`) 보유. brief 는 작업 보드를 1초 폴링(`§4`)하나, 기존 `/stream` 의 daemon/layer0 push 패턴에 task-board 이벤트를 합류시키면 폴링 N개 작업 갱신 비용 절감. 단 폴링도 개인 툴 소규모엔 충분 — **폴링 채택 합리, WS 는 후속 권고**.
- **R-2 (`/pane` to_thread)**: `/pane` 의 `tmux capture-pane` subprocess 를 async route 에서 직접 호출하면 event loop 블록. 단 **기존 server.py 가 이미 `urllib.urlopen(timeout=180)` 를 async route 에서 직접 블로킹**(line 138/222/512) — capture-pane(ms 단위)은 훨씬 가벼워 기존 baseline 대비 악화 0. 깔끔한 fix = `await asyncio.to_thread(...)`(line 470 TTS 패턴 답습) — **권고**.
- **R-3 (동시 작업 상한)**: brief §2 D4 "무제한 동시 0, 합리적 상한 권고" 만 언급 — 실 숫자 미고정. 백그라운드 thread 가 무제한 생성되면(실 LLM 워커 180s 점유) 자원 고갈. **단순 정수 상한(예 4) + 초과 시 거부/큐** 명문.
- **R-4 (`/pane` ollama 워커 처리)**: ollama 워커는 tmux session 부재 → `/pane` 는 `{pane: null, reason: "ollama 워커는 pane 없음"}` 명시 반환(brief §5.1 T-6 이미 인지, 구현 명문).
- **R-5 (CSRF same-origin)**: brief §3 가 "합의 채택 여부" 로 미정. localhost 단일 사용자 비례성 ↔ 브라우저 타 사이트 POST. 구현 비용 극소(Origin/Referer 헤더 1 체크) — **채택 권고**(웹↔명령실행 표면 신규 = 최소 방어 정당).

---

## NOTE

- **NOTE-1 (cwd 의존)**: `index` route 의 `FileResponse("jarvis_hud/index.html")`(`server.py:520`)는 cwd-relative. 테스트/실행 모두 **cwd=repo root** 전제. CI 가 다른 cwd 면 `/` 와 신규 routes 의 src import 동시 실패 — 테스트에서 cwd 고정 또는 `Path(__file__).parent` 절대경로화 고려(기존 코드라 본 cycle scope 밖, 명시).
- **NOTE-2 (conftest 부재)**: repo 에 `conftest.py`/`pytest.ini`/`pyproject [tool.pytest]` **전무**. `from src.jarvis` 가 pytest 에서 동작하는 건 rootdir 기반 `sys.path` 삽입(rootdir=repo root) 덕. 신규 `tests/hud/test_jarvis_task_routes.py` 도 같은 메커니즘으로 `from src.jarvis` + `import jarvis_hud.server` 동시 성립(V-3/V-4 확인). 단 `jarvis_hud` namespace pkg 라 `tests/hud/` 에서 import 시 동일 rootdir 필요 — **NOTE-1 과 연동**.
- **NOTE-3 (boss/memory 선택성)**: `Orchestrator(boss=None, memory=None)` 하위호환(`orchestrator.py:78~81`). UI 가 `OllamaBoss`(line 184) + `MemoryLog` 주입 시 advisory/Layer0 활성. boss 실호출은 또 180s 블록 — B-1 timeout 과 동일 risk 표면(dispatch thread 내라 무관, 단 작업 장기 점유).
- **NOTE-4 (승인=반영 통제 정직)**: brief §3/§7 over-claim 차단 정확 — 워커는 dispatch 시 *이미 실행*(`orchestrator.py:125` worker.run 이 gate 보다 앞). 승인은 OutcomeReport `applied` 플래그만 통제(`orchestrator.py:151~154`). tmux 명령은 send-keys 시 실행됨. **"실행 전 게이트 아님" 명문 정확**.

---

## 동시성 / 실현가능성 판정

| 항목 | 판정 | 근거 |
|------|------|------|
| 백그라운드 dispatch (thread) | **실현 가능** | PoC V-6 — 3 동시 무deadlock. daemon thread + fail-soft(예외→보드 `실패`) |
| threading.Event 승인 게이트 | **실현 가능 (조건부)** | V-6 동작. **단 B-1 timeout + B-3 early-arrival 순서 고정 필수** |
| 보드 dict + Lock | **실현 가능** | V-6/V-7 — Lock 빠른 획득, async route 무블록 |
| async route ↔ thread 보드 폴링 | **정합** | V-7 — event loop 무블록 확인 |
| `from src.jarvis` import | **실현 가능** | V-3 — repo root cwd 전제(NOTE-1) |
| TmuxWorker `on_session` hook | **실현 가능** | `worker.py:182~192` new-session 성공 직후 삽입, kwargs 후방호환(V-8), 74 lifecycle 변경 0 |
| hermetic TestClient 테스트 | **조건부** | 의존성 OK(V-2/V-4/V-5). **단 B-2 주입 설계 명문 없으면 T-1~T-7 구현 불가** |
| 누락 구현 위험 | **B-2/B-3** | factory 주입 hook + decision early-arrival 순서가 brief 에 미명세 |

---

**Agent A 판정 끝.** APPROVE WITH CONDITIONS (BLOCKING 3 — B-1 Event timeout+백그라운드 강제 / B-2 테스트 주입 factory 명문 / B-3 decision early-arrival 순서 고정). 권고 5 + NOTE 4. baseline 205 green.
