# 3+1 합의 — jarvis_hud 작업 카드보드 통합 (Agent B: 품질/안전성 검증가)

> **cycle**: 2026-05-29 (75번째 entry 진입 — 세션 #4)
> **대상**: `docs/phase0/jarvis-hud-task-board-integration-brief.md` (v1)
> **Lens**: "안전하고 견고한가?" — 보안 / 엣지케이스 / 문서 정합성 / over-claim 정직성
> **독립성**: Phase 2 단독 — Agent A/C/codex 미참조. 직접 read + file:line cross-verify.

---

## 판정: **REVISE** (APPROVE WITH CONDITIONS — BLOCKING 3건 해소 시 APPROVE)

방향(웹↔워커 통합) + 완화 계층(localhost + default-deny gate + ReviewGuard + isolation) + over-claim 차단(§7) 골격은 견고. 단 **보드/카드에 표시되는 워커 *출력* 의 secret 노출(응답 redaction 부재)** 을 brief 가 *정직하게 다루지 못함* — T-5 가 사실과 반대(BLOCKING-1). CSRF 가 합의로 미룬 채 *명령 실행 trigger* 표면을 열어둠(BLOCKING-2). 프론트 XSS 의무(escapeHtml) 미명문(BLOCKING-3).

---

## BLOCKING (해소 전 구현 금지)

### B-1. **보드/카드 출력 redaction 부재 — T-5 가 사실과 반대 (over-claim + 실 secret 노출)** ⚠️ 핵심
- **사실**: `RedactionFilter.redact_messages` 는 **송신(prompt/worker output→boss)만** redaction 함 (worker.py:294, boss.py:219). 워커 *응답/출력*(`result.output`)은 **어떤 redaction 경로도 거치지 않음**. orchestrator 가 그대로 `output_preview=result.output[:200]` 로 게이트에 노출(orchestrator.py:147) + `OutcomeReport.result` 에 full output 보존(orchestrator.py:152).
- **brief 주장 (틀림)**: §5.1 T-5 "output은 **redaction 후** 파이프라인 산출"(line 102) + §3 "ReviewGuard 출력 위험 flag"(line 76)는 redaction 을 함의. → **파이프라인에 응답 redaction 0건**. `redaction.py` 모듈 docstring 자체가 "GP-2 prevention 핵심 = 송신(redact_messages). **응답/로그 redaction = 보조(scrub)**"(redaction.py:10) 라 명시하나 `scrub()` 은 worker output 경로에 **연결돼 있지 않음**(grep: src/jarvis 에서 `scrub` 호출 0).
- **실 위험**: 워커(특히 OllamaWorker LLM-text)가 secret 을 생성/echo 하거나, tmux 워커가 `env`/`cat .env`/`echo $TOKEN` 류 출력을 pane 에 남기면 → 보드 카드 `output` + `/pane` capture 가 **평문 secret 을 웹에 표시**. 기존 채팅(`/api/respond`)은 사용자↔LLM 텍스트라 표면이 다르나, **작업 보드는 *워커 실행 산출물*(명령 출력 포함)을 노출** = 새 egress 표면.
- **권위 충돌**: governance §4.1 GP-2 = "stdout/stderr/log file/LLM request body 에 secret 노출 차단"(governance:422). 보드/`/pane` = stdout 노출 경로 → GP-2 범위. brief 가 이를 "보조 deferred" 로도 명문 안 함.
- **요구**: (택1) (a) `/tasks`·`/pane` 직렬화 시 `RedactionFilter.scrub()`/`redact_text()` 를 **응답 경로에 실제 연결** + T-5 를 "scrub 적용 후 직렬화" 로 정정 + test 가 inject-canary 검증, 또는 (b) 응답 redaction = **명시적으로 deferred(CC-6)** 임을 §3/§7 에 정직 명문 + "보드 출력은 redaction 미적용 — 사용자 책임" 표기. **현 T-5 문구(redaction 후 산출)는 어느 쪽이든 거짓이므로 반드시 정정.**

### B-2. **CSRF — 합의로 미룬 채 *명령 실행* trigger 표면 개방 (조건부 채택 → 채택 의무)**
- **사실**: §3(line 77) + RT-3(line 132) 이 same-origin 체크를 **"합의 채택 여부"** 로 미룸. 그러나 본 통합의 핵심 차이 = `POST /api/jarvis/task` 가 **워커 명령 실행을 trigger**(특히 tmux=실 명령). 브라우저가 열려 있으면 **타 악성 사이트의 `<form>`/`fetch` 가 localhost:8765 로 cross-origin POST → 사용자 모르게 워커 실행**. (기존 하나 = 채팅만이라 CSRF 영향이 "원치 않는 LLM 호출" 수준이었으나, 통합 후 = **명령 실행**으로 격상.)
- **반론 흡수 (정직)**: 승인 게이트 default-deny 라 *반영* 은 막힌다. 그러나 **명령은 dispatch 시 이미 실행됨**(brief line 11/75 스스로 인정) — CSRF 로 제출된 작업도 워커가 실행 → tmux 워커면 `rm`/네트워크 등 부작용이 **게이트 무관하게 발생**. default-deny 는 *반영* 만 통제 → CSRF 방어로 불충분.
- **요구**: same-origin(Origin/Referer 헤더 체크) 또는 토큰을 **state-changing route(`POST /task`, `POST /decision`) 에 본 cycle 필수 채택**(합의 옵션 아님). 개인 단일 사용자 비례성은 "0.0.0.0 미bind"로 충족되나, *브라우저 cross-origin* 은 localhost bind 로 못 막음(브라우저가 로컬에서 요청 발사). GET(`/tasks`,`/pane`)은 CSRF 대상 아니나 정보 노출이라 same-origin 권고. 비용 = Origin 헤더 1줄 체크 → 비례성 OK.

### B-3. **프론트 XSS — 워커 출력/flags/pane 의 escapeHtml 의무 미명문**
- **사실**: 기존 `renderCanvasCard` 는 `innerHTML` + `escapeHtml`(index.html:1148/1154/1156) 사용. 단 `escapeHtml` 은 **`& < >` 만 escape**(index.html:1084) — 속성 컨텍스트(따옴표)는 미escape. SVG 카드는 `entry.svg` 를 **escape 없이 raw innerHTML**(index.html:1149) — 기존 noted 위험.
- **brief 결함**: §4 `renderTaskCard` 가 `output`/`flags`/`boss 검토`/`tmux pane` 을 카드 상세에 렌더한다 명시(line 86)하나 **escapeHtml 적용을 의무화하지 않음**. 워커 출력 = **신뢰 불가 외부 입력**(LLM 생성 / 명령 stdout) → `<script>`/`<img onerror>` 포함 가능. innerHTML 직접 삽입 시 **self-XSS → localhost API 전권 탈취**(같은 origin 이라 모든 jarvis route 호출 가능 = 명령 실행).
- **요구**: §4 + §5.2 에 "**모든 워커 산출(output/flags/advice/pane)은 `textContent` 또는 escapeHtml 후 삽입, raw innerHTML 금지**" 명문 + 프론트 검증 항목 추가. pane(멀티라인)은 `<pre>` + `textContent` 권고.

---

## 권고 (non-blocking, 흡수 권장)

### R-1. 승인 Event 영구 대기 — default-deny 정합 명문 강화
- §2 D1 ui_approver = `threading.Event` 대기. RT-2(line 131)가 "타임아웃/취소 + default-deny" 언급하나 **타임아웃 시 반환값이 default-deny(False)임을 ApprovalGate fail-closed 와 일관**되게 명문 필요. `ApprovalGate.request` 는 approver 예외 시 False(approval.py:47) — ui_approver 가 **타임아웃을 예외/False 로 변환**해야 fail-closed 보존. "Event 무한 대기 = 작업 스레드 leak" → 상한 권고(D4 line 70 "합리적 상한"과 연결). 미결정=미반영(default-deny)은 OutcomeStatus.DENIED 로 귀결되므로 정합 — 단 **스레드/Event 자원 정리** 명문 권고.

### R-2. ReviewGuard 한계 재명문 (실행 못 막음)
- §3 가 "ReviewGuard 출력 flag"(line 76)를 완화 계층으로 나열. 73 brief §3 R-3(cli-tmux:78)이 이미 "ReviewGuard = *출력*(실행 후) 검사 → 실행 자체 못 막음" 명문. 본 brief 도 동일 1줄 명문 권고(완화 계층이 *실행* 통제로 오인되지 않게). ReviewGuard 패턴 = 10종 *알려진* 명령만(review.py:19-30, 완전성 비주장) — 보드 flag 가 "안전 판정"으로 보이지 않게 UI 문구 권고.

### R-3. tmux `/pane` capture 의 라이브 노출 = 추가 egress 표면
- §2 D2 `/pane = capture-pane -p` 가 **실시간 pane 전문**을 웹에 노출. B-1 redaction + B-3 escapeHtml 양쪽 적용 대상. nonce sentinel(74)은 평문 노출 전제(nonce-sentinel:63) — pane 에 nonce 잔존은 안전영향 0(권위 일치) 이나 **명령 출력 내 secret 은 별개**(B-1). `/pane` 도 scrub 경로 포함 권고.

### R-4. 동시성 스레드 예외 → 보드 `실패` (fail-soft) — test 명문
- D4(line 70)/RT-1(line 130) "스레드 예외 catch → 보드 실패" 양호. T-4(worker_failed)는 있으나 **dispatch 스레드 자체 예외(보드 코드 예외)** test 부재 — §5.1 에 "스레드 본문 예외 → 보드 실패 기록 + 서버 무중단" test 추가 권고.

### R-5. 보드 in-memory dict — 무한 누적 / 재시작 소실 명문
- §2 D1 보드 = in-memory dict. 장기 가동 시 누적(메모리) + 서버 재시작 시 진행중 작업 소실(Event 대기 스레드 orphan). 개인 툴 비례성상 수용 가능하나 "보드 = 휘발성, 영속 0" 명문 권고(over-claim 회피).

---

## NOTE (정합성 / cross-verify)

- **N-1 (정합 ✅)**: localhost bind = server.py:553 `uvicorn.run(app, host="127.0.0.1", port=8765)` 확인 — brief §3(line 76) "server.py:554" 인용은 **off-by-one**(실제 553). 사소하나 정정 권고.
- **N-2 (정합 ✅)**: 승인 게이트 default-deny = approval.py:38-47 확인(approver None → False, 예외 → False). ui_approver 주입 모델이 이 불변식 보존 가능(R-1 조건부).
- **N-3 (정합 ✅)**: orchestrator dispatch 순서 = worker.run(실행, :125) → guard.review(:126) → boss.advise(:138) → gate.request(:150) — brief "실행→review→boss→gate" 정확. "승인=반영 전 not 실행 전" 정직(line 75) — 코드 일치.
- **N-4 (정합 ✅)**: TmuxWorker 세션명 hook(D2) = 본문 최소 보강. session = `{prefix}-{uuid8}`(worker.py:172) 확인. `on_session` 콜백 추가는 lifecycle 변경 0 가능(74 동형). 단 "본문 변경 0"(§0.2 #1)과 "TmuxWorker 세션 hook 1건"(§7)은 **모순 아님**(hook=배선 1건) — 정합.
- **N-5 (over-claim 정직 ✅)**: §7 "jarvis UI 완성 0 / 안전 명령 실행 보장 0 / 통제된 자식 완성 0" + "승인=반영 통제(실행 아님)" = **정직**. MEMORY [feedback_pass_scope_overclaim] detection≠prevention 패턴 답습 양호. 단 B-1 의 T-5 문구가 이 정직성을 **국소적으로 위반**(redaction 미실증을 "redaction 후"로 표기) → over-claim cascade 재발 위험.
- **N-6 (회귀 ✅ 설계)**: §0.2 #2 + §5.1 "src 205 회귀 0" + 기존 채팅/노트/TTS/canvas route(server.py:536-549) 무변경 = 작업 route *추가*. 기존 `renderCanvasCard`/`#canvas-list` 재사용 + 토글 추가 → 기존 뷰 무변경 가능(정합). 단 토글 추가가 기존 canvas 렌더 경로(index.html:1143-1162) 를 건드리지 않는지 구현 시 검증 필요.
- **N-7 (권위 ✅)**: ADR-009 §2.2 facade 단일 진입점 — brief §0.3 이 "jarvis_hud는 트랙 B urllib 워커 경유((나) 일관)" 로 facade 우회를 정직 명문. worker.py:26 import 경로(`src.adapters.llm.redaction`, SDK 아님) 일치. Provider Liquidity(헌법 5조) = 워커 model 인자 교체 보존(worker.py:240) — 회귀 0.

---

## 보안 / over-claim 독립 판단 (Agent B)

1. **최대 위험 = 명령 실행 표면의 *2차 노출***: 웹↔명령실행(brief 인지) 자체보다, 그 **산출물(stdout/secret)이 redaction 없이 웹 보드로 재노출**(B-1) + **CSRF 로 trigger 가능**(B-2) + **XSS 로 산출물이 코드 실행**(B-3) 의 *조합* 이 핵심. 셋 다 brief 가 부분/미흡 처리 → BLOCKING.
2. **정직성**: §7/§10 over-claim 차단 골격은 우수(통제된 자식 완성 회피 명문). 단 T-5(redaction 후 산출)는 **실증 없는 prevention 주장** = MEMORY [feedback_pass_scope_overclaim] detection≠prevention 위반. 반드시 deferred 명문 또는 실 연결.
3. **비례성 ↔ 방어**: CSRF same-origin = 1줄 비용 → 명령 실행 표면엔 비례성상 **필수**(개인 툴이라도 브라우저 cross-origin 은 막아야 함). 인증 시스템은 불요(localhost 단일 사용자) — 동의.

---

## 권위 cross-verify 요약

| 주장 | 권위 | 검증 |
|------|------|------|
| 송신 redaction만 존재, 응답 미연결 | worker.py:294 / boss.py:219 / redaction.py:10 / scrub 호출 0 | ✅ B-1 |
| GP-2 = stdout/log secret 차단 | governance:422 (§4.1) | ✅ B-1 권위 |
| default-deny / fail-closed | approval.py:38-47 | ✅ N-2 |
| dispatch 순서 실행→review→boss→gate | orchestrator.py:125-150 | ✅ N-3 |
| localhost bind | server.py:553 (brief :554 = off-by-one) | ✅ N-1 |
| ReviewGuard 출력검사 한계 | review.py:9 / cli-tmux:78 | ✅ R-2 |
| nonce 평문 노출 무관(사전위조만 차단) | nonce-sentinel:63 / worker.py:168 | ✅ R-3 |
| escapeHtml = `&<>` 만 | index.html:1084 | ✅ B-3 |
