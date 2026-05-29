# 3+1 합의 — jarvis_hud 작업 카드보드 통합 (Agent C: 대안 탐색가)

> **cycle**: 2026-05-29 (75번째 entry 진입) — jarvis_hud(하나) 에 jarvis 작업 파이프라인 통합
> **검토 대상**: docs/phase0/jarvis-hud-task-board-integration-brief.md (v1)
> **렌즈**: "더 나은 방법이 있는가?" — 대안 기술 / 트레이드오프 / scope 경계
> **독립성**: Phase 2 단독 — Agent A/B/codex 미참조. 직접 read 만. 작성 = Anthropic Claude.

---

## 판정: **APPROVE WITH CONDITIONS**

방향(하나에 통합 + 백그라운드 dispatch + 승인 게이트 Event + 카드보드 토글)은 **대안 비교상 타당**하다. 동시성·승인 전달·프론트 재사용 3개 영역에서 brief 가 채택한 수단이 **최적이 아니거나 부정확한 답습 주장**을 포함한다 → BLOCKING 3 + 권고 6. 전부 흡수 가능(아키텍처 재설계 불요).

---

## BLOCKING (file:line 근거 + 대안 제시)

### B-1. `.toggle` CSS 재사용 주장 = 부정확 (탭 ≠ on/off 스위치)
- **근거**: brief §4 line 83 "canvas 헤더에 토글/탭 추가: `정리 노트·도식` ↔ `작업` (기존 `.toggle` CSS 재사용 가능)". 그러나 index.html 의 `.toggle` (index.html:202~224) 은 **36×20px 슬라이딩 on/off 스위치** — TTS 켜기(`#tts-toggle` index.html:820)·AI 음성(`#tts-ai-toggle` index.html:824) *2곳에서만* 쓰이는 boolean 위젯이다. 2-way 탭(노트↔작업 *뷰 전환*)과 시각·의미가 다르다.
- **왜 BLOCKING**: 답습 주장이 틀리면 구현자가 `.toggle` 를 그대로 붙였다가 UX 가 깨진다(스위치가 탭처럼 안 보임). [[feedback_ui_design_confirm_first]] 답습 — UI 명칭 정확성은 디자인 컨펌 대상.
- **대안 (권고 채택)**: (a) **세그먼트 탭 신규 CSS** (canvas-title 영역에 2-pill, active 강조) — 가장 깔끔. 또는 (b) `.sidebar-item.active` 패턴(index.html:421) 재사용 — 이미 active/inactive 시각 토큰 보유. **(b) 가 진짜 재사용**(이미 존재하는 active 상태 패턴). brief 는 "`.toggle` 재사용" → "`.sidebar-item.active` 또는 신규 세그먼트 탭" 으로 정정 필요.

### B-2. `#canvas-list` 단일 컨테이너 = 뷰 분리 인프라 부재 (재사용 주장 과장)
- **근거**: index.html line 994 `<div id="canvas-list"></div>` = 카드를 *직접* 담는 단일 컨테이너. `renderCanvasCard` (index.html:1143) 가 `canvasList.appendChild` (index.html:1159) 로 무조건 여기 append. `loadInitial` (index.html:1191~1193) 도 동일. 뷰 전환(노트↔작업) 인프라 0 — show/hide 컨테이너도, 탭 상태 변수도 없다.
- **왜 BLOCKING**: brief §0.3 line 37 / §4 가 "canvas `#canvas-list`/`renderCanvasCard`/`.canvas-card` 재사용" 을 *기반*으로 깐다. 실제론 (1) `#jarvis-task-list` 신규 컨테이너 + (2) `#canvas-list` 와 상호 배타 show/hide + (3) 탭 상태 JS 가 *전부 신규*다. "재사용" 으로 분류하면 구현 scope 가 과소 추정된다.
- **대안 (권고 채택)**: 두 컨테이너(`#canvas-list`, `#jarvis-task-list`)를 형제로 두고 탭 클릭 시 `style.display` 토글. `.canvas-card` 시각 토큰(index.html:723~771)은 **카드 *스타일*만 재사용**(상태 배지 색은 `--success/--warning/--danger` index.html:25~27 재사용 가능) — 정직하게 "스타일 토큰 재사용, 뷰 분리 로직 신규" 로 명문.

### B-3. 동시성 모델 — `asyncio.to_thread` 가 `threading.Thread` 보다 정합 (deadlock 경로 명문 필요)
- **근거**: orchestrator.dispatch 는 **sync** (orchestrator.py:120~156) 이고 내부에서 `gate.request(req)` (orchestrator.py:150) → `ApprovalGate.request` → `self._approver(req)` (approval.py:45) 를 **블로킹 호출**한다. ui_approver 는 `threading.Event.wait()` 로 막혀야 하는데, 이 Event 를 set 하는 것은 `/decision` route(이벤트 루프에서 실행)다. brief §2 D1 line 50 이 "`threading.Thread` 또는 `asyncio.to_thread`" 를 *동격 OR* 로 제시 — 두 선택의 트레이드오프·deadlock 경로가 명문화 안 됨.
- **왜 BLOCKING**: 잘못 고르면 deadlock 또는 이벤트루프 블로킹. 구체적으로:
  - **순수 `threading.Thread`(daemon)**: dispatch 가 별도 OS 스레드. `Event.wait()` 가 그 스레드를 막고, `/decision` route 가 event 루프에서 `event.set()`. **동작함** — 단 스레드 lifecycle·예외 회수(RT-1)를 수동 관리.
  - **`asyncio.to_thread`**: starlette 가 이미 동기 blocking 작업(TTS)을 `asyncio.to_thread(_synthesize_wav_sync,...)` (server.py:470) 으로 처리하는 **기존 패턴과 동형**. dispatch 를 `asyncio.to_thread(orchestrator.dispatch, ...)` 로 던지면 anyio 워커 스레드에서 sync dispatch 실행 → `threading.Event.wait()` 로 막힘. `/decision` 가 동기 `event.set()` 호출(루프 비블로킹). **이벤트 루프는 자유** → 폴링/`/decision` 응답 정상. **단 anyio 기본 스레드풀 상한(40)** 미만이어야 하며, 미결정 작업이 스레드를 점유(RT-2 timeout 필수).
  - **deadlock 함정**: ui_approver 안에서 `asyncio.Event` 를 쓰면 안 됨(워커 스레드엔 루프 없음) → 반드시 `threading.Event`. brief D1 line 51 은 "`threading.Event`" 명시 → 정합. 단 D1 line 50 의 "`asyncio.Event`" 언급(요약 프롬프트)과 혼동 금지.
- **대안 (권고 채택)**: **`asyncio.to_thread` 우선** — server.py:470 기존 패턴 답습(일관) + 스레드 lifecycle 을 anyio 가 관리(수동 daemon 스레드 회수 불요). dispatch 던질 때 `try/except` 로 감싸 보드 `실패` 기록(RT-1). brief 가 OR 을 **"asyncio.to_thread + threading.Event(워커 스레드 내부), `/decision` 는 동기 set"** 로 단일화하고 deadlock 경로(asyncio.Event 금지)를 §2/§8 에 명문화할 것.
- **대안 (subprocess 호출, 비채택 근거)**: "jarvis CLI(`python -m src.jarvis`)를 subprocess 로 호출" 은 거부. (1) 승인 게이트가 CLI 의 stdin prompt(`make_interactive_approver` __main__.py:50~71)라 웹에서 stdin 주입 = 추악함. (2) `--yes`(auto_approver __main__.py:45) 쓰면 default-deny 무력화 = §3 보안 핵심 위배. (3) 작업 상태(진행중/승인대기) 가시성 0(프로세스 종료까지 black box). → **in-process 배선이 명백히 우월**. brief 가 subprocess 를 *고려조차 안 함*은 정당하나, "왜 in-process 인가" 1줄 근거는 권고.
- **대안 (Starlette BackgroundTask, 비채택 근거)**: `BackgroundTask` 는 응답 *반환 후* 실행되며 작업 보드 폴링과 무관하고 승인 대기 동안 connection 점유 불가 → 부적합. brief 가 안 쓴 것 정당.

---

## 권고 (대안 제시, 비차단)

### R-1. 승인 대기 전달 — 폴링 채택 정당, 단 기존 `/stream` WS 도 *대안으로 명문*
- 하나는 이미 `/stream` WebSocket(server.py:32~45, 522~523, routes line 538)을 **보유**하고 index.html(line 1219~1238)이 자동 재연결로 소비 중. brief §0.2 #5 line 33 은 "WebSocket 작업 스트림(폴링으로 충분)" 을 *하지 않는 것*으로 분류.
- **트레이드오프 판단**: 개인 단일 사용자 + ~1초 폴링(brief §4 line 89) = **폴링이 비례적**(WS 작업 스트림 추가 = stream_status 루프 분기 복잡도↑, 메시지 타입 라우팅↑). **폴링 채택 동의.** 단 (a) 폴링은 `작업` 뷰 활성 시에만(brief line 89 명시 — 좋음), (b) 미래 다중 워커 시 `/stream` 에 `{"type":"task"}` 분기 추가가 *자연스러운 확장 경로*임을 §0 deferred 에 1줄 남길 것(폐기 아닌 보류). 현 cycle WS 미채택 = 정당.

### R-2. 작업 보드 저장 — in-memory dict 채택 정당, 서버 재시작 행동 명문 필요
- brief §2 D1 line 50 "in-memory dict, lock 보호" + per-task Event(D4 line 70). MemoryLog(memory.py:74~)는 **OutcomeReport 완료본만** append(append-only, modify 0, memory.py 답습) — 진행중/승인대기 *중간 상태* 저장 용도 아님. conversations.jsonl 은 채팅 전용(server.py:155).
- **판단**: in-memory dict = **올바른 선택**(중간 상태는 휘발성이 자연스럽다 — 서버 죽으면 진행중 작업도 죽음). MemoryLog/conversations.jsonl 재사용은 부적합(스키마·책무 불일치). 단 **RT-2 보강**: 서버 재시작 시 (a) 진행중 dispatch 스레드 소멸 → 작업 유실(승인대기 Event 도 소멸), (b) tmux 세션은 *서버와 독립*으로 살아남음(kill-session 은 dispatch 스레드 finally worker.py:198 — 스레드 죽으면 미실행) → **고아 tmux 세션** 가능. → §8 에 "서버 재시작 = 진행중 작업 유실 + 고아 tmux 세션 수동 정리(`tmux kill-server`)" 정직 명문. 영속화는 deferred 정당(비례성).

### R-3. TmuxWorker 세션 노출 — `on_session` hook(brief 채택) vs grep 대안 비교
- brief §2 D2 line 55 = `on_session: Callable[[str], None]` hook 을 TmuxWorker.run 에 추가(new-session 직후 호출). 본문 변경 1건.
- **대안 (grep, 비채택 근거)**: "session_prefix=task_id 로 주고 `tmux list-sessions | grep task_id`" 는 본문 변경 0이나 (a) session = `{prefix}-{uuid4[:8]}` (worker.py:172) 라 prefix 만으론 정확 매칭 불가(uuid 부분 미지), (b) race(grep 시점에 세션 미생성/이미 kill), (c) prefix 에 task_id 주입 = 생성자 인자 변경이라 "본문 변경 0" 도 거짓. → **hook 이 더 깔끔**(결정적, race 0). brief 채택 정당.
- **권고**: hook signature 를 `on_session: Callable[[str], None] | None = None` (기본 None = 74 회귀 0, brief line 55 의도와 일치)로 명시. hook 호출은 `new-session` rc==0 *직후*(worker.py:182~192 사이) — 실패 세션은 미호출(정합). **session 저장이 곧 capture-pane 대상**이므로 hook 이 보드에 session 기록 → `/pane`(brief D3 line 64)이 그 session 으로 capture. 이 데이터 흐름을 §2 에 1줄 명문.

### R-4. CSRF — 개인 툴 비례성상 same-origin(Origin/Referer) 체크 *채택* 권고
- brief §3 line 77 + RT-3 line 132 가 "same-origin 체크 또는 토큰, 본 cycle 채택 여부 = 합의" 로 *미결* 남김.
- **판단 (대안 비교)**: 본 통합의 핵심 위협은 §3 line 75 자인대로 **웹 요청 → tmux 명령 *실제 실행***. 브라우저의 타 악성 사이트가 `localhost:8765/api/jarvis/task` 로 POST 하면(CSRF) — 사용자가 그 사이트 방문 중이면 — *명령 dispatch* 가 trigger된다(승인 게이트는 *반영* 통제일 뿐 dispatch=실행은 이미 됨, §3 line 75). 즉 CSRF = **명령 실행 trigger**. 무방어는 비례성 밖. **토큰보다 same-origin(Origin/Referer 헤더 체크)이 비례적** — localhost 단일 사용자라 토큰 발급/저장 ceremony 불요, Origin 헤더 부재/불일치 시 403 한 줄로 충분. 단 POST 라우트(`/task`, `/decision`)에만. GET(`/tasks`,`/pane`)은 부작용 0이라 면제 가능. → **same-origin 체크 채택 권고** (RT-3 를 "채택" 으로 확정). 단 `Origin` 헤더 부재(직접 curl·동일 출처 일부 케이스) 처리 정책(부재=허용 or 거부) 명문 필요 — localhost 면 부재=허용이 실용적(브라우저 cross-origin 은 항상 Origin 부착).

### R-5. src.jarvis 재사용 vs jarvis_hud 자체 ollama — 작업 파이프라인은 src.jarvis 경유가 *정답*
- 하나는 자체 urllib ollama 클라이언트(server.py:128~140, respond_handler:217~222, chat_handler:506~514)를 보유. brief §0.3 line 37 이 작업 파이프라인은 `src.jarvis.orchestrator` 경유로 명시.
- **판단**: **src.jarvis 경유가 명백히 정답.** 자체 ollama 는 *채팅/노트/svg*(통제 불요, 실행 0) 전용으로 *보존*(brief §0.2 #2 line 30 무변경 정당). *작업*(통제된 워커 실행 + ReviewGuard + 승인 게이트 + memory)은 src.jarvis 의 game(ApprovalGate default-deny approval.py:38, ReviewGuard review.py, 송신 redaction worker.py:26)을 *반드시* 거쳐야 안전 본질이 산다. 자체 ollama 로 작업 파이프라인을 *중복 구현*하면 게이트·redaction·guard 가 빠진 평행 경로 = 보안 회귀. → **이중 ollama 클라이언트 공존은 의도적·정당**(책무 분리: 채팅=자체, 작업=src.jarvis). 단 §0.3 line 37 의 "ADR-009 facade 단일 진입점 — jarvis_hud는 트랙 B urllib 워커 경유" 주석은 정확(facade.py 는 LiteLLM 경로, OllamaWorker/OllamaBoss 는 트랙 B urllib worker.py:242/boss.py:100 — (나) 일관). CC-0 회피 답습 정합.

### R-6. scope 경계 — 카드보드 토글 적정, 입력 경로는 *작업 뷰 전용 입력* 권고
- brief §4 line 90 이 입력 경로를 "기존 입력바에 `작업` 모드 추가 *또는* 작업 뷰 전용 입력" *미결*.
- **판단 (대안 비교)**: 기존 입력바(index.html:982~989)는 `detectMode`(index.html:1076 정규식 note/svg/chat)로 채팅·노트·svg 자동 분기. 여기에 `작업` 모드를 끼우면 (a) detectMode 정규식 충돌(어떤 발화가 "작업"인가 모호), (b) 작업은 worker_type/tmux_argv/isolation(brief D3 line 61) 등 *구조화 인자*가 필요한데 단일 텍스트 입력바로 표현 불가. → **작업 뷰 전용 입력 권고** (작업 뷰 활성 시 prompt + worker_type 드롭다운 + (tmux 시) argv/isolation 필드). 채팅 입력바와 분리 = 책무 명확 + detectMode 무변경(기존 회귀 0). 다중 워커/출력 UX·인증 deferred(brief §7 line 123) = **정당**(비례성, over-claim 차단).

---

## NOTE (관찰 — 차단/권고 아님)

- **N-1 (MemoryLog 동시성)**: memory.py:84 `append` 는 호출마다 `open(path,"a")` — 내부 Lock 0. 다중 dispatch 스레드가 동일 memory 경로에 동시 append 시 POSIX 의 작은 write 는 대체로 atomic 이나 *보장 아님*. 개인 툴 소규모(brief D4 line 70 "무제한 동시 0")면 실무 무해하나, 보드 dict Lock(D4)과 *별개로* MemoryLog 는 비보호임을 인지. 권고: 작업당 별도 memory 인스턴스 or 단일 직렬화 — 단 비례성상 현 cycle deferred 가능.
- **N-2 (sys.path 검증)**: `python3 -c "import src.jarvis.orchestrator"` 가 repo root 에서 OK. server.py:520 의 `FileResponse("jarvis_hud/index.html")` 상대경로 = repo root 실행 전제 = `from src.jarvis import ...` 정합(brief D3 line 66 정확). 단 server.py 최상단 import 가 무거운 src 트리(redaction_patterns 등)를 끌어옴 → 시작 지연 미미하나 인지.
- **N-3 (anyio 스레드풀)**: server.py:470 의 기존 `asyncio.to_thread` 패턴 = anyio 기본 capacity_limiter(40). dispatch 가 *승인 대기 동안 스레드 점유*(threading.Event.wait) → 미결정 작업이 누적되면 TTS·신규 dispatch 가 스레드 고갈 가능(RT-2 timeout 이 이를 완화). 개인 툴 소규모면 실무 무해. §8 RT-2 에 "미결정 작업 = 스레드 점유" 1줄 추가 권고.
- **N-4 (보드 직렬화 redaction)**: brief T-5 line 102 가 "output 은 redaction 후 파이프라인 산출" 주장 — 정확히는 OllamaWorker/OllamaBoss 의 redaction 은 **송신**(worker.py:294, boss.py:219) redaction 이지 *수신 output* redaction 아님. `/tasks`(D3 line 62)가 `output_preview`(orchestrator.py:148 `result.output[:200]`)를 그대로 직렬화하면 워커가 *생성한* secret 은 미redact. 개인 localhost 면 위협 낮으나 T-5 의 "민감정보 0" 주장은 *송신* 한정임을 정직 표기(over-claim 차단, [[feedback_pass_scope_overclaim]] 답습).

---

## scope / 대안 독립 판단 (요약)

| 영역 | brief 채택 | Agent C 독립 판단 |
|------|-----------|------------------|
| 동시성 | threading.Thread OR asyncio.to_thread (OR) | **asyncio.to_thread 단일화** (server.py:470 동형) + threading.Event(워커 스레드) + 동기 set. asyncio.Event 금지 명문 (B-3) |
| 승인 전달 | 폴링 | **폴링 정당** (비례성). `/stream` WS 는 deferred 확장 경로로 1줄 (R-1) |
| 보드 저장 | in-memory dict | **dict 정당**. 재시작=유실+고아 tmux 명문 (R-2) |
| 세션 노출 | on_session hook | **hook 정당** (grep 대비 결정적). signature 명시 (R-3) |
| CSRF | 미결 | **same-origin 체크 채택** (CSRF=명령실행 trigger, 비례성 내) (R-4) |
| 카드보드 토글 | canvas 토글 뷰 | **적정**. 단 `.toggle` 재사용 부정확(B-1), 컨테이너 신규(B-2) |
| 입력 경로 | 미결 | **작업 뷰 전용 입력** (detectMode 충돌·구조화 인자) (R-6) |
| src.jarvis 경유 | src.jarvis | **정답** — 자체 ollama=채팅, src.jarvis=작업(게이트+guard+redaction). 이중 공존 정당 (R-5) |
| 다중 워커/인증 | deferred | **정당** (비례성, over-claim 차단) |

---

## 합의 입력 요약 (Reviewer 용)

- **판정**: APPROVE WITH CONDITIONS
- **BLOCKING 3**: (B-1) `.toggle` = on/off 스위치이지 탭 아님, 재사용 주장 부정확 → `.sidebar-item.active` or 신규 세그먼트 탭. (B-2) `#canvas-list` 단일 컨테이너, 뷰 분리 인프라 신규(스타일 토큰만 재사용). (B-3) 동시성 OR 단일화 — asyncio.to_thread(server.py:470 동형) + threading.Event, asyncio.Event 금지 deadlock 경로 명문.
- **권고 6**: 폴링 정당(WS deferred 1줄) / dict 정당(재시작=유실+고아 tmux 명문) / hook 정당(signature 명시) / **same-origin CSRF 채택** / src.jarvis 경유 정답(이중 ollama 공존 정당) / 작업 뷰 전용 입력.
- **NOTE 4**: MemoryLog 비Lock / sys.path OK / anyio 스레드풀 점유 / `/tasks` output 은 *송신* redaction 한정(수신 미redact, over-claim 차단).
- **주요 대안 거부**: subprocess CLI 호출(stdin 게이트·--yes default-deny 무력화·black box) / Starlette BackgroundTask(응답 후 실행·승인대기 부적합) / grep 세션 탐지(uuid 미지·race) — 전부 in-process+hook 이 우월.
