# 3+1 합의 (Reviewer 통합) — jarvis_hud(하나) 작업 카드보드 통합

> **날짜**: 2026-05-29 (세션 #4, 75번째 entry 진입 cycle)
> **검토 대상**: `docs/phase0/jarvis-hud-task-board-integration-brief.md` (v1)
> **합의 형태**: 풀 3+1 + 외부 LLM 1+ (codex gpt-5.5 cross-vendor, `--sandbox danger-full-access`) — 보안(웹↔명령실행) + 동시성 + 아키텍처 + 프론트
> **4 source**: Agent A (구현) / Agent B (안전) / Agent C (대안) / codex

---

## 0. 최종 판정 — **REVISE → brief v1.1 흡수 후 TDD 적격**

| source | 판정 | BLOCKING |
|--------|------|----------|
| codex (gpt-5.5) | **REVISE** | 5 |
| Agent A (구현) | APPROVE WITH CONDITIONS | 3 |
| Agent B (안전) | **REVISE** (≈APPROVE w/ COND) | 3 |
| Agent C (대안) | APPROVE WITH CONDITIONS | 3 |

**방향(하나 통합 + 백그라운드 dispatch + 승인 Event + canvas 작업 카드보드)은 4 source 타당 판정** — 대안(subprocess CLI / BackgroundTask / grep 세션탐지) 모두 열위로 기각(C), 동시성 PoC 실증(A: 3 dispatch + Event + Lock deadlock 0). **그러나 brief v1 = 보안 표면(특히 *출력* redaction) 미달 → 2 source REVISE.** BLOCKING 흡수 후 brief v1.1 → TDD 적격. **재합의 불요**(v1.1 흡수 = 보안 강화, 방향 변경 0).

---

## 1. 통합 BLOCKING (brief v1.1 흡수 의무)

| ID | finding | source | 흡수 정정 |
|----|---------|--------|----------|
| **CB-1** ⭐⭐⭐⭐ | **보드/카드 출력 redaction 부재 — T-5 주장 거짓**. `output_preview=result.output[:200]` raw (orchestrator.py:143-149), `WorkerResult.output` = raw(worker.py:34-42), RedactionFilter = **송신만**(redaction.py:10). → 보드/카드가 워커 *출력*(secret echo / tmux `cat .env`) 웹 평문 노출 = GP-2 §4.1(governance:418-424) | **codex(B1) + Agent B(B1)** line-cited, A/C NOTE | `/tasks` output + 카드 표시 출력에 **`RedactionFilter.scrub` 적용**(표시 경로 응답 redaction 구현) + brief §5 T-5 "redaction 후" 정정 + board 필드 `redacted_output_preview` + `raw_available=false` |
| **CB-2** ⭐⭐⭐ | **tmux `/pane` raw secret 표시 표면**. capture-pane raw(worker.py:196-216) → `/pane` 그대로 제공(brief:56). 웹 표시 로그 = P2(governance:104-105) | codex(B2) | `/pane` 응답 **scrub 적용** + 길이 제한 + (raw reveal 기본 off) |
| **CB-3** ⭐⭐⭐ | **CSRF = MUST (선택 아님)**. localhost bind 라도 타 사이트가 `POST /api/jarvis/task`/`/decision` → 워커 *실행* trigger(default-deny는 *반영*만 통제) | **Agent B(B2) + codex(B3) + Agent A(R5) + Agent C(권고)** — 4 source 수렴 | `/task` + `/decision` = **same-origin(Origin/Referer) 체크 MUST**(비례성 검토 항목에서 의무로 승격) |
| **CB-4** ⭐⭐⭐ | **승인 Event 영구 대기 + /decision race**. ApprovalGate fail-closed = approver 예외 시만(approval.py:41-47) → Event 영구 대기 시 미발동. /decision early-arrival(Event 미생성) → 결정 유실 | **Agent A(B1/B3) + codex(B4)** | ui_approver **Event.wait(timeout)** + **dispatch=백그라운드 thread(`asyncio.to_thread`)** + Event **dispatch 전 선생성**(early-race fix) + cancel route + stale cleanup + timeout=default-deny |
| **CB-5** ⭐⭐⭐ | **프론트 XSS**. `escapeHtml`=`&<>`만(index.html:1083-1084), SVG raw innerHTML(:1147-1150). renderTaskCard 가 untrusted output/pane/advice 렌더 → self-XSS → localhost 전권 | **Agent B(B3) + codex(B5)** | renderTaskCard = **textContent/escape 강제, innerHTML 금지**(output/pane/advice/flags) + XSS 수동 검증 |
| **CB-6** ⭐⭐ | **동시성 모델 단일화** — brief §2 "threading.Thread *또는* asyncio.to_thread"(OR). asyncio.Event 사용 시 deadlock | Agent A(B1) + Agent C(B3) | **`asyncio.to_thread`(server.py:470 TTS 패턴 동형) + `threading.Event`(워커 스레드) + 동기 set**. asyncio.Event 금지 명문 |
| **CB-7** ⭐⭐ | **orchestrator 주입 seam 부재** — brief "주입 가능 설계" 목표만, 메커니즘 0 → TestClient hermetic test(T-1~T-7) 구현 불가 | Agent A(B2) | `JarvisTaskBoard` + **orchestrator/worker factory 주입** 명문(전역 handler → 주입 hook) |
| **CB-8** ⭐⭐ | **canvas 토글/컨테이너 신규** — `.toggle`(index.html:202-224)=TTS on/off **슬라이딩 스위치**(탭 아님). `#canvas-list`=단일 컨테이너(뷰 분리 인프라 0) | Agent C(B1/B2) | brief §4 "토글/.canvas-card 재사용" → **신규 탭(`.sidebar-item.active` 패턴) + 신규 컨테이너 `#jarvis-task-list` + show/hide**(스타일 토큰만 재사용) |

---

## 2. 통합 권고 (v1.1 흡수 권장)

| # | 권고 | source |
|---|------|--------|
| R-1 | 동시 작업 **상한 = 구현값 고정**("권고" → 명시 한계) | codex + A(R3) |
| R-2 | `JarvisTaskBoard` lifecycle 필드 고정(created/updated/status/session/decision/error/redacted_output_preview/raw_available) | codex |
| R-3 | `tmux_argv` 허용 범위 좁히기(웹 오입력 피해) | codex |
| R-4 | `/pane` session = **보드 task_id→session만**(path/query 금지) | codex |
| R-5 | `/pane` = `asyncio.to_thread`(기존 capture 180s 블로킹 baseline) | A(R2) |
| R-6 | ollama 워커 `/pane` = null/없음 처리 | A(R4) + C |
| R-7 | in-memory dict 정당 — **재시작=유실 + 고아 tmux 세션 명문** | C + B(R5) |
| R-8 | on_session hook 정당(grep 세션탐지 대비 결정적) / src.jarvis 경유 정답(자체 ollama=채팅, 이중 공존 정당) / 폴링 정당(WS=deferred 확장) / 작업 뷰 전용 입력(detectMode 충돌 회피) | C |
| R-9 | TDD에 CSRF 실패 / redacted output / pane redaction / approver timeout default-deny 케이스 추가 | codex |

---

## 3. NOTE / 정합 (positive)
- **방향·정직 정합** (4 source): 승인 게이트 "실행 전 아님"(반영 통제) 정직 명문 정확(codex NOTE, brief:11/74-78/121-123). localhost bind 유지 = 코드 일치(server.py:**553**, ⚠️ brief:54 off-by-one — NOTE). orchestrator 순서/default-deny/tmux 실행/nonce 인용 OK(codex 매트릭스). 하나 기존 기능 보존 방향 OK(구현 시 회귀 test 의무).
- **동시성 실증**(A): starlette 0.52.1/uvicorn 0.48.0/httpx 0.28.1/TestClient 설치 + `from src.jarvis` repo root 성립 + 3 dispatch PoC deadlock/race 0. baseline pytest **205**.
- **대안 기각**(C): subprocess CLI(stdin 게이트/--yes default-deny 무력화) / BackgroundTask(승인대기 부적합) / grep 세션탐지(uuid race) — in-process + on_session hook 우월.
- **over-claim catch**: brief §7 명칭 골격("jarvis UI/안전 명령실행/통제된 자식 완성" 회피)은 양호하나, **§5 T-5 "output redaction 후"가 *거짓 보안 주장*(CB-1)** — 본 cycle 핵심 정정. 응답 redaction(CC-6 deferred)이 웹 표시 표면에서 실 위험으로 surface.

---

## 4. 보안 독립 판단 (codex + Agent B 수렴)
웹↔명령실행 통합 = **승인 UX 통합**이지 **명령 실행 안전화 아님**(brief 정직). 단 v1 = "실행 후 output을 웹에 보여주는 표면" 과소평가 — 워커 *요청* redaction(70)은 있으나 워커 *응답/출력 + tmux pane*은 redaction 보장 0 → secret 이 localhost 웹 UI/브라우저 메모리/스크린/export 노출 가능. **CB-1(출력 scrub) + CB-2(pane scrub) + CB-3(CSRF MUST) + CB-5(XSS)** 이 핵심 보안 흡수.

---

## 5. 합의 결론
**REVISE (4 source — codex/B REVISE + A/C APPROVE WITH CONDITIONS)** — 방향 타당, brief v1 보안 미달(출력/pane redaction + CSRF + XSS + Event timeout). **BLOCKING 8 + 권고 9 brief v1.1 흡수 → TDD 적격**(재합의 불요, 보안 강화·방향 변경 0). CB-1(출력 redaction 거짓 주장) = 본 cycle 핵심 — 표시 경로 응답 redaction(scrub) 실구현으로 닫음.

**다음**: brief v1.1 흡수 → 사용자 TDD 승인 → TDD(백엔드 hermetic + 보안 케이스 + 수동 프론트 XSS/골든) → verify → commit + push.
