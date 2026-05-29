# jarvis_hud(하나) 작업 카드보드 통합 구현 brief (v1.1)

> **작성**: 2026-05-29 (75번째 entry 진입 cycle — 세션 #4)
>
> **v1 → v1.1 흡수 (풀 3+1 + codex `docs/review/3plus1-consensus-2026-05-29-jarvis-hud-task-board.md`, REVISE — codex/B REVISE + A/C APPROVE WITH CONDITIONS, BLOCKING 8 + 권고 9)**. 방향 타당, brief v1 *보안 미달* → 흡수 후 TDD 적격(재합의 불요):
> - **CB-1 ⭐⭐⭐⭐ (출력 redaction 거짓 주장 정정)**: `output_preview=result.output[:200]` raw(orchestrator.py:143-149), RedactionFilter=송신만(redaction.py:10) → 보드/카드가 워커 *출력* 평문 노출(secret echo/`cat .env`). §5 T-5 "redaction 후" **거짓** → `/tasks` output + 카드 표시에 **`RedactionFilter().scrub` 적용**(표시 경로 응답 redaction 실구현) + board 필드 `redacted_output_preview`/`raw_available=false`.
> - **CB-2 ⭐⭐⭐ (pane redaction)**: `/pane` capture-pane raw → **scrub 적용** + 길이 제한 + raw reveal 기본 off.
> - **CB-3 ⭐⭐⭐ (CSRF MUST, 4 source)**: `/task`+`/decision` = **same-origin(Origin/Referer) 체크 *의무***(선택 아님 — cross-origin POST=명령 실행 trigger).
> - **CB-4 ⭐⭐⭐ (Event timeout/race)**: dispatch=**백그라운드 `asyncio.to_thread`** + ui_approver **Event.wait(timeout)** + Event **dispatch 전 선생성**(/decision early-race) + cancel route + stale cleanup + timeout=default-deny.
> - **CB-5 ⭐⭐⭐ (XSS)**: renderTaskCard = **textContent/escape 강제, innerHTML 금지**(output/pane/advice/flags) + XSS 수동 검증.
> - **CB-6 ⭐⭐ (동시성 단일화)**: `asyncio.to_thread`(server.py:470 TTS 패턴) + **`threading.Event`(asyncio.Event 금지=deadlock)** + 동기 set.
> - **CB-7 ⭐⭐ (주입 seam)**: `JarvisTaskBoard` + **orchestrator/worker factory 주입**(TestClient hermetic).
> - **CB-8 ⭐⭐ (canvas 신규 탭/컨테이너)**: `.toggle`=TTS 슬라이딩 스위치(탭 아님), `#canvas-list`=단일 컨테이너 → **신규 탭(`.sidebar-item.active` 패턴) + 신규 `#jarvis-task-list` + show/hide**(스타일 토큰만 재사용).
> - **권고 흡수**: 동시 작업 상한 구현값(R-1) / board lifecycle 필드(R-2) / tmux_argv 범위(R-3) / `/pane` task_id→session만(R-4) / `/pane` to_thread(R-5) / ollama pane null(R-6) / in-memory 휘발성+고아 tmux 명문(R-7) / TDD CSRF·redacted·pane·timeout 케이스(R-9). NOTE: server.py bind = **553**(brief 본문 :554 → 553 정정).
>
> **방향**: [[project_jarvis_controlled_child_then_friday]] 통제된 자식 함께 쓰기 — UI로 명령·흐름·승인. [[feedback_ui_design_confirm_first]] 답습(디자인 컨펌 완료: 하나 레이아웃 참고 + canvas 작업 카드보드 토글 뷰 + 수락/거절 + tmux 라이브 + 백그라운드 dispatch).
>
> **scope**: 기존 **`jarvis_hud/`(하나, Starlette/uvicorn, localhost:8765)** 에 **jarvis 작업 파이프라인**(`src.jarvis.orchestrator.dispatch`: 워커→ReviewGuard→boss→**승인 게이트**→memory) 통합. UI = canvas 우측에 **"작업 카드보드" 토글 뷰**(기존 정리노트·도식과 별도 칸) — 작업 카드가 알람처럼 생성·클릭 가능, 진행중/승인대기/종료 상태 표시 + **수락/거절** 버튼 + tmux **라이브 보기**(capture-pane 폴링).
>
> **합의 형태**: 풀 3+1 + 외부 LLM 1+(codex) — **웹↔명령 실행 보안 표면** + 동시성(threading/Event) + 아키텍처(백그라운드 dispatch + 승인 경로) + 프론트. (사용자 명시.)
>
> ⚠️ **보안 핵심 (웹이 명령 실행을 trigger)**: 하나 현 상태 = ollama 채팅만(명령 실행 0). 본 통합 후 = **웹 요청이 워커(ollama LLM-text 또는 tmux 명령실행)를 실행**. 승인 게이트는 **"반영 전"이지 "실행 전"이 아님** → 워커는 dispatch 시 *이미 실행*(73/74 CLI tmux 동형). 완화 = localhost bind + 명령=사용자 authority + ReviewGuard 출력 flag + 승인 게이트(default-deny) + CSRF(로컬 단일 사용자, 명문).
>
> **선행 답습**: `jarvis_hud/server.py`(Starlette routes + ollama urllib + canvas) + `jarvis_hud/index.html`(canvas `#canvas-list`/`renderCanvasCard`/`.canvas-card`/`.toggle`) + `src/jarvis/orchestrator.py`(dispatch + WorkerRegistry) + `approval.py`(ApprovalGate, Approver 콜백) + `worker.py`(OllamaWorker/TmuxWorker nonce, 74) + 72/73/74 CLI(동형 배선 + 실행능력 + 안전 패턴).

---

## §0 범위

### 하는 것
1. 백엔드: `server.py` 에 jarvis 작업 routes(제출/보드/결정/pane) + 백그라운드 dispatch + 승인 게이트 Event + 작업 보드 상태 (§2)
2. TmuxWorker 세션명 노출 hook(라이브 보기) — 최소 보강 (§2 D2)
3. 보안: localhost + 웹↔명령실행 표면 명문 + 승인게이트(default-deny) + CSRF (§3)
4. 프론트: canvas 작업 카드보드 토글 뷰 + 카드(상태/클릭) + 수락/거절 + tmux 라이브 (§4)
5. TDD(백엔드 hermetic Starlette TestClient) + 프론트 수동 브라우저 검증 (§5)

### 하지 않는 것
| # | 영역 | 본 cycle |
|---|------|----|
| 1 | orchestrator/worker/boss/approval/review 본문 변경 | 0 (배선만; TmuxWorker는 세션 hook 1건 한정) |
| 2 | 하나 기존 기능(채팅/노트/svg/TTS/Layer0/대화 관리) 변경 | 0 (작업 카드보드 *추가*) |
| 3 | 외부 노출(0.0.0.0 bind) / 인증 시스템 | 0 (localhost 유지) |
| 4 | 실행 *전* 게이트 / 명령 사전 검열 | 0 (기존 모델=반영 전) |
| 5 | 다중 사용자 / 원격 접속 / WebSocket 작업 스트림(폴링으로 충분) | 0 |
| 6 | 자동 후속 | 0 |

### §0.3 권위 답습
- `jarvis_hud/server.py`(routes/canvas_handler/respond) + `index.html`(canvas 렌더) / `src/jarvis/orchestrator.py`·`approval.py`·`worker.py`·`review.py`·`memory.py` / ADR-009 §2.2(facade 단일 진입점 — 단 jarvis_hud는 트랙 B urllib 워커 경유, (나) 일관) / 72·73·74 CLI 답습.

---

## §1 진입 컨텍스트
- 72 CLI / 73 tmux 워커 / 74 nonce 후 사용자 "UI로 명령+결과+흐름" → 디자인 컨펌(하나 레이아웃 + canvas 작업 카드보드 토글 + 수락/거절 + tmux 라이브 capture-pane poll + 경량 프레임워크) → jarvis_hud(하나, 이미 가동) 발견 → "하나에 직접 통합" 확정.
- 하나 현재 = 채팅/노트/svg + Layer0 관찰 표시(자체 ollama urllib). 빠진 것 = jarvis 작업 파이프라인(통제된 워커 실행 + 승인).

---

## §2 백엔드 아키텍처

### D1. 백그라운드 dispatch + 승인 게이트 Event
- `orchestrator.dispatch`는 sync + 내부에서 `approver()` inline 호출(블로킹). 웹은 요청-응답이라 → **작업을 백그라운드 스레드(`threading.Thread` 또는 `asyncio.to_thread`)로 dispatch** + **작업 보드(in-memory dict, lock 보호)** 가 상태 추적.
- **UI approver**: `ApprovalGate(approver=ui_approver)`. `ui_approver(req)` = 보드에 `승인대기` + `req`(flags/advice/output_preview) 저장 → **`threading.Event` 대기** → `/decision` 이 Event set + 결정 저장 → approver 가 bool 반환.
- 상태 전이: 제출 → `진행중` → (worker_failed) `실패` / (approver 호출) `승인대기`[flags+boss검토+출력] → (decision) `수락`/`거절` → 최종 OutcomeReport 반영. memory(MemoryLog)도 기록(기존 파이프라인).

### D2. TmuxWorker 세션명 hook (라이브 보기)
- TmuxWorker.run 의 `session`(`{prefix}-{uuid8}`)을 외부가 알아야 capture-pane 라이브 가능. **`on_session: Callable[[str], None] | None`** 추가 — new-session 직후 호출(보드가 session 저장). 본문 최소 보강(74 nonce 동형, lifecycle 변경 0).
- `/pane` = `tmux capture-pane -p -t <session>` (보드에 저장된 session). 종료 후엔 마지막 캡처 또는 결과.

### D3. routes (server.py 확장)
| route | 메서드 | 동작 |
|---|---|---|
| `/api/jarvis/task` | POST `{prompt, worker_type, worker_model?, tmux_argv?, isolation?, no_boss?}` | 백그라운드 dispatch 시작, `{task_id}` 반환 |
| `/api/jarvis/tasks` | GET | 보드 카드 list(id/prompt/worker/status/flags/advice/output/ts) — 폴링 |
| `/api/jarvis/task/{id}/decision` | POST `{decision: "accept"\|"reject"}` | 승인 Event set + 결정 저장 |
| `/api/jarvis/task/{id}/pane` | GET | tmux capture-pane 라이브(tmux 워커 한정) |

- orchestrator 연결: `from src.jarvis...` (server.py = repo root 실행, sys.path 루트). 워커=OllamaWorker(텍스트)/TmuxWorker(명령, isolation) + ReviewGuard + ApprovalGate(ui_approver) + OllamaBoss + MemoryLog.
- 보드 = `JarvisTaskBoard` 클래스(dict + Lock + per-task Event) — 테스트 주입 가능 설계.

### D4. 동시성/안전
- 보드 dict 접근 = `threading.Lock`. per-task `threading.Event`. 다중 작업 = 다중 스레드(개인 툴 소규모 — 무제한 동시 0, 합리적 상한 권고). dispatch 스레드 예외 = 보드 `실패` 기록(fail-soft, 서버 무중단).

---

## §3 보안 (핵심 — 웹↔명령 실행)
- **표면 변화**: 하나 현 = ollama 채팅(실행 0). 통합 후 = 웹 요청 → 워커 실행. 특히 **tmux 워커 = 명령 실제 실행**(73). 승인 게이트 = 반영 통제(실행 통제 아님) → 명령은 dispatch 시 실행됨(정직 명문).
- **완화 계층**: (1) **localhost bind 유지**(127.0.0.1 — 외부 접속 0, server.py:554 답습) (2) 명령 argv = 사용자가 UI에 직접 입력(authority) (3) ReviewGuard 출력 위험 flag → 카드/게이트 노출 (4) **승인 게이트 default-deny**(수락 버튼 없이는 반영 0) (5) isolation(Passthrough/Landlock).
- **CSRF**: 로컬 단일 사용자라 위험 낮음. 단 브라우저 타 사이트가 localhost:8765로 POST 가능 → 최소 방어 = **same-origin 확인(Origin/Referer 헤더 체크)** 또는 간단 토큰. 본 cycle 채택 여부 = 합의 검증(개인 툴 비례성 ↔ 방어).
- **정직**: "안전한 명령 실행 보장" 0. 승인 게이트 = 반영 통제. tmux 명령 실행은 사용자 책임 + isolation.

---

## §4 프론트 (`index.html` 확장)
- canvas 헤더(`canvas-title`)에 **토글/탭** 추가: `정리 노트·도식` ↔ `작업` (기존 `.toggle` CSS 재사용 가능).
- `작업` 뷰 = 신규 `#jarvis-task-list` 컨테이너. `renderTaskCard(task)`:
  - 카드 = `.canvas-card`(기존 스타일 재사용) + 상태 배지(진행중 ▶ / 승인대기 ⏳ / 수락 ✅ / 거절 ✖ / 실패 ⚠).
  - 클릭 → 상세(flags / boss 검토 / 출력 / tmux pane).
  - 승인대기 시 **[수락] [거절]** 버튼 → `POST /api/jarvis/task/{id}/decision`.
  - tmux 워커 + 진행중 → **[👁 라이브]** → `/pane` 폴링 표시.
- 폴링: `작업` 뷰 활성 시 `GET /api/jarvis/tasks` ~1초 주기 → 카드 갱신(알람처럼 생성/상태 변화).
- 입력: 작업 제출 경로 = 기존 입력바에 `작업` 모드 추가 또는 작업 뷰 전용 입력(디자인 컨펌 세부 — 합의/구현 시 확정, 하나 입력바 패턴 재사용).
- ⚠️ 기존 채팅/노트 뷰 무변경(작업 뷰 *추가*).

---

## §5 TDD 계획
### §5.1 백엔드 (hermetic — Starlette TestClient + fake orchestrator)
- `tests/hud/test_jarvis_task_routes.py`(신규):
  - T-1: `POST /api/jarvis/task` → task_id + 보드에 `진행중` (fake worker 주입 — 실 ollama/tmux 0).
  - T-2: 승인대기 전이 — fake worker 정상 → approver 호출 → 보드 `승인대기` + flags/advice/output 노출.
  - T-3: `/decision accept` → Event set → 보드 `수락`/applied; `reject` → `거절`.
  - T-4: worker_failed(fake error) → `실패`, approver 미호출.
  - T-5 ⭐ (CB-1, 정정): `/tasks` 보드 output = **`RedactionFilter().scrub` 적용 후** 직렬화. secret 포함 워커 출력 → `redacted_output_preview`에 `[REDACTED]` (원본 secret 부재) 검증. ⚠️ 워커 *출력*은 파이프라인이 redaction 안 함(송신만, redaction.py:10) → **표시 경로에서 scrub 실적용**이 본 cycle 의무(거짓 "redaction 후" 주장 정정).
  - T-6 (CB-2): `/pane` — fake session capture-pane → **scrub 적용** 후 반환(secret 평문 0) + 길이 제한. ollama 워커는 pane 없음(null) 처리.
  - T-7: 동시성 — 2 작업 보드 독립(per-task Event/state, Lock).
  - T-8 ⭐ (CB-3): CSRF — cross-origin(다른 Origin 헤더) `POST /api/jarvis/task`·`/decision` → **거부(403)**; same-origin → 정상.
  - T-9 ⭐ (CB-4): approver Event.wait timeout → **default-deny(미반영)**; /decision early-arrival(Event 선생성) → 결정 유실 0.
  - `JarvisTaskBoard` + ui_approver = 주입 가능 설계(orchestrator factory 주입) → 실 LLM/tmux 0.
- 기존 src 205 test 회귀 0.

### §5.2 프론트 (수동 브라우저 검증 — UI guidance 답습)
- dev 서버(`python jarvis_hud/server.py`) → 브라우저 골든 패스: 작업 제출 → 카드 진행중 → 승인대기(flags/boss/출력) → 수락 → 종료. tmux 워커 라이브 보기. 토글(노트↔작업). 엣지: 거절, 실패, 동시 2건. **"브라우저에서 못 돌리면 명시"**.

### §5.3 verify
- pytest(신규 hud + src 회귀 0) + grimp SDK 경계 0(server.py가 src.jarvis import — SDK 아님) + scan-source(src + jarvis_hud) 0 + (수동) 브라우저 골든/엣지.

---

## §6 합의 형태 + 승격
풀 3+1 + 외부 LLM 1+(codex). 트리거: 보안(웹↔명령실행) ✅ + 아키텍처(백그라운드 dispatch+승인경로) ✅ + 동시성 ✅ + 실 코드 ✅ + Provider Liquidity(워커 경유) ✅ → 5/5. 합의 APPROVE 후 TDD.

---

## §7 금지 / over-claim
- 금지: orchestrator/worker/boss 본문 0(TmuxWorker 세션 hook 1건만) / 하나 기존 기능 0 / 0.0.0.0 bind 0 / 실행 전 게이트 0 / 자동 후속 0.
- over-claim 차단: "jarvis UI 완성" 0 / "안전한 명령 실행 보장" 0 / "통제된 자식 완성" 0 — **canvas 작업 카드보드 + 승인 + tmux 라이브 통합** 한정(다중 워커 라우팅/출력 UX 고도화/인증 별도). 승인 게이트 = 반영 통제(실행 통제 아님).

---

## §8 Rollback Trigger
| # | trigger | 대응 |
|---|---------|----|
| RT-1 | 백그라운드 dispatch 예외 → 서버 중단 | 스레드 예외 catch → 보드 `실패` fail-soft(서버 무중단) |
| RT-2 | 승인 Event 영구 대기(미결정 작업) | 타임아웃/취소 경로 + default-deny(미결정=미반영) |
| RT-3 | CSRF(타 사이트 POST) | same-origin 헤더 체크(합의 채택 시) + localhost |
| RT-4 | tmux 세션 hook 이 lifecycle 깸 | 74 동형 — hook은 new-session 후 통지만(lifecycle 변경 0) |
| RT-5 | 보드 dict race | Lock 보호 |
| RT-6 | "안전 명령 실행" over-claim | §3/§7 — 승인=반영 통제, 실행 사용자 책임 정직 |

---

## §9 Evidence
- E-1: hud task routes test(T-1~T-7) green + src 205 회귀 0
- E-2: 승인 게이트 default-deny(미결정/거절 = 미반영) test
- E-3: 보안 — localhost bind 유지 + (채택 시) same-origin 체크 + scan-source 0
- E-4: TmuxWorker 세션 hook test(74 회귀 0)
- E-5: (수동) 브라우저 골든 패스(제출→진행→승인→종료) + tmux 라이브 + 토글 + 엣지(거절/실패/동시)

---

## §10 자기진단
| # | 위험 | 처리 |
|---|------|----|
| P-1 | "jarvis UI/통제된 자식 완성" over-claim | 카드보드+승인+라이브 통합 한정(§7) |
| P-2 | "안전 명령 실행 보장" over-claim | 승인=반영 통제(실행 아님), 사용자 authority+isolation(§3) |
| P-3 | 웹↔명령실행 표면 경시 | §3 명문(localhost+게이트+ReviewGuard+CSRF) |
| P-4 | 동시성 race/스레드 예외 | Lock + per-task Event + fail-soft(§2 D4) |
| P-5 | 하나 기존 기능 회귀 | 작업 뷰 *추가*, 기존 무변경(§0.2 #2) |
| P-6 | TmuxWorker 본문 과변경 | 세션 hook 1건 한정(§2 D2) |
| P-7 | 작성자 = Claude single-vendor | cross-vendor codex + 풀 3+1 |

---

## §11 다음 단계
사용자 승인 → 풀 3+1 + codex(`--sandbox danger-full-access`) 4 source → Reviewer 통합 → brief v1.1 흡수 → TDD(백엔드 + 수동 프론트) → verify → commit + push + 75 entry. 자동 진입 0.

**본 brief v1 끝.**
