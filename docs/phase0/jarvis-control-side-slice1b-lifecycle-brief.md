# Jarvis 제어측 slice-1b brief — 프로세스 lifecycle (start / stop / restart) + 인수

> **일자**: 2026-06-04 · **브랜치**: `feature/jarvis-control-side-slice1b`
> **상태 (v2, 합의 REVISE 반영)**: 풀 3+1 합의 완료(REVISE 만장일치) + 사용자 검토(L-1~L-11 OK · HUD OK · adopt=**cutover-재기동**) → 합의 BLOCKING **CB-1~CB-9** + over-claim 정정 **OC-1~5** 반영. 다음 = **TDD** (자동 진입 0)
> **합의 보고서**: `docs/review/3plus1-consensus-2026-06-04-jarvis-control-side-slice1b.md`

> **답습 (비협상 불변 — 재론 금지)**:
> - `docs/phase0/jarvis-control-side-general-executor-brief.md` v2 §5 (slice-1 구현 범위, 1a→1b 분할) · §7 (갈림길 결정) · §8 (Provider Liquidity + Rollback Trigger)
> - `docs/review/3plus1-consensus-2026-06-04-jarvis-control-side-slice1.md` (REVISE, B-1~B-6, CO-1~7, PA-1~3, DI-1~3, GP-1~9)
> - `src/jarvis/process_control.py` (slice-1a 구현 — ProcessController seam·capability 등급·probe)
> - 메모리: `[[project_jarvis_general_executor_northstar]]` · `[[feedback_provider_liquidity]]` · `[[feedback_staged_consensus_workflow]]` · `[[feedback_ui_design_confirm_first]]` · `[[feedback_pass_scope_overclaim]]`
>
> **북극성**: Jarvis = 내가 Claude에게 명령을 주면 수행되듯, 어떤 프로젝트든 만들고·고치고·관리·실행하는 일반 실행 에이전트. 이번 세션 voice_lab 예시에서 Claude가 손으로 한 **"PID 정확 종료 → 포트 해제 대기 → 재기동"**(pkill 금지·bind 충돌 교훈)을 자비스의 결정적 절차로 박는 것이 slice-1b다 (레퍼런스 모티브 ③ 실행 도구의 두 번째 조각).

---

## 합의 반영 (v2, 풀 3+1 REVISE) — 비협상 통합 BLOCKING

판정 = **REVISE(조건부 승인)**, 3개(구현·안전·대안) 만장일치. 방향·게이트 구조 건전 + 기존 선례(ApprovalGate·process_control seam·ledger·external_registry) 실재. 단 아래 **CB-1~CB-9 충족 후** TDD 진입. 상세 = 합의 보고서.

**통합 BLOCKING (TDD 진입 전 필수)**:
- **CB-1 PID recycling 차단** (⭐ A·B·C 독립 수렴) — 소유권 키 = `(pid, start_time)`(`/proc/<pid>/stat`). signal(stop/restart) 직전 starttime 재대조, 불일치 = PID 재사용 → 거부+referred. **자비스가 spawn한 소유 PID에도 적용**(재기동 사이 recycling 가능).
- **CB-2 누적 영속 = LedgerLog 파생** (⭐ A·B·C 수렴) — 누적(가동 후 10회)은 `read()` 순회로 target executed lifecycle 이벤트 count. in-memory 단독 금지(controller 재시작 0 리셋 = 우회). rate(60s/2)=in-memory 허용(재시작=더 보수적).
- **CB-3 Launcher long-lived 인터페이스** — `spawn(argv,cwd,env)->pid`(non-blocking `Popen`+`start_new_session`) / `signal(pid,sig)` 분리(기존 blocking `subprocess.run` 재사용 금지). 종료 = `os.killpg(getpgid(pid))`(손자 회수). start 성공 판정 = LISTEN probe(1a 재사용). 백엔드 주입 = registry/코어만(boss 불가).
- **CB-4 lifecycle ledger 적합화** — (a) task_id 합성(`target:action:ts`) (b) lifecycle 경로 = 기록 성공 확인 후 집행(**fail-closed**, 감사가 유일 센서) (c) cmdline 기록 secret 필터.
- **CB-5 atomicity** — per-target lock critical section = {C-3 2축 검사 + 동시1 + 카운터 증가 + PID/starttime + `_execute`} 원자. 검사-집행 사이 lock 해제 금지.
- **CB-6 seam 구조 강제** — L-1 테스트 = (a) propose 외 경로로 MEDIUM 집행 도달 불가 + (b) `_execute`가 게이트/lock 통과 증거 없이 호출되면 raise/no-op.
- **CB-7 adopt 경로 = cutover-재기동** (사용자 확정) — 사람 승인(HIGH) → 미소유 정지 → controller 재spawn으로 소유 전환(자기 `(pid,starttime)` 기록). **무중단 표시-only 인수 = 1b' DEFER**(실측 후). cmdline = best-effort 보조(신원 증명 아님). ⭐ cutover라 CB-1의 adopt 적용·TOCTOU·cmdline deny가 1b에서 대부분 불필요.
- **CB-8 dangling 처리** — 부분 실패 → referred + lock 해제(영구차단 방지) + 소유 PID 'dead' 표시(stale signal 금지) + 다음 start는 LISTEN/PID 부재 확인 후.
- **CB-9 L-4 vs 인수 우선순위 테이블** — 미소유 LISTEN 존재 시 start = 거부 vs 인수(cutover) 권유 결정 테이블로 `_decide` 분기 명확화.

**over-claim 정정 (OC-1~5)**: ledger "그대로"→키합성+fail-closed(CB-4) · subprocess "기본"→non-blocking detached spawn(CB-3) · cmdline "신원 확인"→best-effort 대조(증명 아님) · C-3 수치=**잠정**(1b dogfood 후 재조정) · pkill 금지→+starttime 재대조(CB-1).

---

## 0. 이 slice가 생긴 이유 + 진입 조건 충족

slice-1a(probe, 자율)는 PR #50에서 머지됐고, 본 세션에서 **dogfood 실측**을 마쳤다:

| 1a dogfood 실측 (2026-06-04, 실가동 :8765→:8777) | 결과 |
|---|---|
| `probe?name=voice_lab` | `executed · LOW · listening=true` (0.6~1.3ms) — B-1 seam·B-5 등급 정상 |
| `probe?name=nonexistent` | 404 — B-2 provenance(registry 유일 출처) |
| 외부/비-localhost | `probeable=false` — B-4 SSRF 차단 |

**합의 DI-2 진입 조건 충족**: "1b 게이트 임계(C-3)를 1a dogfood 실측으로 확정." 단 **정직 단서** — 1a probe는 부작용 0(저위험)이라 lifecycle 빈도를 *직접* 실측하진 못한다. C-3 수치 근거 = (a) seam/provenance/localhost 실가동 확증 + (b) 운영상 lifecycle 빈도(세션 history: 재시작은 코드 변경/크래시 시에만, 정상 분당 0~1회. 분당 다회 = 비정상 크래시 루프/폭주).

→ **사용자가 slice-1b 진입을 명시(2026-06-04).** 자동 진입 0 충족.

---

## 1. 범위 — 1a와 무엇이 달라지는가 (위험 상승의 본질)

| | slice-1a (머지됨) | **slice-1b (본 brief)** |
|---|---|---|
| 동작 | `health` (probe) | `start` / `stop` / `restart` + `adopt`(인수, L-11) |
| capability | `probe` (읽기) | `spawn` / `signal` (쓰기) |
| 등급 | LOW (자율) | **MEDIUM (게이트)** / 인수 = **항상 HIGH(사람 승인)** |
| 부작용 | 0 (포트 LISTEN 조회) | **실 프로세스 기동/종료** — 비가역성 잠재(GPU OOM·디스크·고아 프로세스) |
| 집행 경로 | `_execute` → probe만 | `_execute` → **Launcher**(subprocess/systemd-run) → 실 OS 연산 |

**핵심**: 1a는 "보는" 동작이라 게이트 없이 자율이었다. 1b는 "건드리는" 동작이라 **게이트·PID 소유권·빈도 누적·감사**가 전부 동시에 붙어야 한다(brief v2 §2 결론: "실행 도구엔 반드시 게이트가 붙는다"). 1a가 박은 seam(propose-only)을 그대로 쓰되, `_execute`의 MEDIUM 분기를 **게이트 통과 시에만** 채운다.

---

## 2. 갈림길 — 이미 결정됨 (재론 금지)

| # | 갈림길 | 결정 | 주체 |
|---|---|---|---|
| C-1 | controller 형태 | **(a) 본체 내 모듈 + Launcher 추상**(기본 subprocess, systemd-run 주입). 독립 데몬 기각 | 합의 |
| C-2 | lifecycle 기본 게이트 | **초기 1-클릭 → dogfood 후 자율 완화** | 사용자 확정 |
| **C-3** | 빈도/누적 임계 | **rate = 60초 윈도 내 2회 / 누적 = 프로세스 가동 후 총 10회 / 동시 1인스턴스.** 초과 = 사람 회부. **잠정 — 1b dogfood 실측 후 재조정**(OC-4) | **사용자 확정 (2026-06-04, 보수적)** |
| C-4 | 대상 등록 | external_registry 확장 + **제어 필드 분리 dataclass** + provenance 상속. 별도 신설 기각 | 합의 |
| G5 | 채널 | probe=HTTP / lifecycle=Launcher(subprocess·signal), systemctl은 launcher 백엔드로 흡수 | 합의 |
| G6 | 등급 소유권 | 코어 고정(G6(a)) + capability 한겹 분리. start/stop/restart → spawn/signal → MEDIUM | 합의 |

---

## 3. BLOCKING 후보 (1b 신규 — 합의에서 확정 필요) — L-1 ~ L-11

> B-1~B-6(1a)은 불변 상속. 아래는 lifecycle 실집행이 새로 만드는 표면에 대한 **1b 신규 BLOCKING 후보**. **합의 완료 → 상단 CB-1~CB-9가 권위**(본 L 표는 초기 후보, CB와 충돌 시 CB 우선).

| # | BLOCKING 후보 | 근거 (답습) |
|---|---|---|
| **L-1** | **seam 확장** — `_execute`의 MEDIUM(spawn/signal) 분기는 **게이트 승인 + C-3 통과 시에만** 도달. boss가 propose()로 MEDIUM 동작을 우회 집행할 수 없음을 *우회불가 단위테스트*로 고정 | B-1 확장 |
| **L-2** | **PID 소유권 (GP-2 + CB-1)** — controller가 **자기가 spawn한 `(pid, starttime)` 일치**에만 signal(signal 직전 starttime 재대조 = PID 재사용 차단). 미소유 기존 프로세스(예: 현 502419)는 인수(L-11) 전엔 signal 불가 = **사람 회부**. **pkill/포트 전체 kill 금지**(CO-4, voice_lab 교훈) | GP-2, CO-4, CB-1 |
| **L-3** | **Launcher 추상 (C-1)** — `Launcher` 인터페이스(기본 `subprocess`, `systemd-run` 주입형). `setsid` detach로 본체 종료 시 고아화 방지. 대상별 launch cmd/cwd는 registry 주입(하드코딩 0) | C-1, DI-1 |
| **L-4** | **per-target lock + 동시 1인스턴스 (GP-4, B-3)** — 동시 lifecycle 변경 직렬화. `start` 시 기존 PID/LISTEN 존재하면 **거부**(중복 기동 차단) | GP-4, PA-3 |
| **L-5** | **C-3 2축 게이트** — rate(60s/2회 슬라이딩 윈도) **+** 누적(가동 후 총 10회) **+** 동시 1인스턴스. 어느 한 축이라도 초과 = **사람 회부**(자율 완화 후에도). rate 단독 금지(리셋 우회) | B-3, PA-3, C-3 |
| **L-6** | **게이트 = ApprovalGate 재사용** — default-deny + fail-closed(`approval.py:41-47`). C-2 초기 1-클릭. 게이트 콜백 부재/오류 = 거부 | CO-2, C-2 |
| **L-7** | **부분 실패 자동 롤백 금지 (GP-5)** — restart 중 stop 성공·start 실패 시 자동 재기동 금지 → **사람 회부**(통제 보존) | GP-5 |
| **L-8** | **boss 페이로드 strict + argv (GP-6)** — 대상 이름 allowlist + 동작 enum만. launch cmd는 **argv 리스트**(쉘 문자열 금지, `shell=False`). boss가 cmd를 정하지 않음(registry 소유) | GP-6 |
| **L-9** | **감사 = LedgerLog append-only (GP-7)** — 모든 lifecycle 결정(동작·등급·outcome·PID·게이트 결과)을 append-only 기록. Rollback Trigger 검출 기반 | GP-7, `ledger.py` |
| **L-10** | **registry 제어 필드 분리 dataclass (C-4) + provenance 상속(B-2)** — 읽기측 ExternalEntry 스키마 오염 금지. 제어 필드(launch cmd/cwd/pid)는 분리 구조체. origin==jarvis fail-closed 상속 | C-4, GP-9, B-2 |
| **L-11** | **인수(adopt) = cutover-재기동** (사용자 확정 CB-7) — 미소유 LISTEN PID를 **사람 승인(HIGH) → 정지 → controller 재spawn**으로 소유 전환. controller가 직접 spawn하니 `(pid, starttime)` 자기 기록 → PID recycling·cmdline 위장 우회. cmdline = best-effort 보조(신원 증명 아님, 거부 근거 = 사람승인+포트 한정). **무중단 표시-only 인수 = 1b' DEFER**(실측 후). LedgerLog 기록 | CB-7, 사용자 결정 |
| (불변) | **controller 자격증명 0 (B-6)** — lifecycle도 자격증명 보유 0 유지 | B-6 |
| (불변) | **controller 크래시 fail-closed (GP-3)** — controller 다운 = 모든 dispatch 거부 | GP-3 |

---

## 4. 아키텍처 스케치 (1a 위에 얹기)

```
 사용자 명령 → boss/HUD
    │ propose("restart", target)   ← untrusted, argv·enum only (L-8)
    ▼
┌──────────────────────────────────────────────────────────┐
│ ProcessController._decide()                                 │
│  1. provenance(B-2) + localhost(B-4) 재검증                 │
│  2. allowlist 조회 → start/stop/restart (미등재=고 fail-closed)│
│  3. capability 등급 → MEDIUM(spawn/signal)                   │
│  4. ── MEDIUM 분기 (1b 신규) ──                              │
│     a. per-target lock 획득 (L-4)                           │
│     b. C-3 2축 검사: rate 60s/2 · 누적 10 · 동시1 (L-5)      │
│        └ 초과 → outcome=referred (사람 회부)                 │
│     c. ApprovalGate.request() — 초기 1-클릭 (L-6)           │
│        └ deny/fail → outcome=rejected                       │
│     d. PID 소유권 검사 (L-2) — 미소유 = referred(인수 권유)  │
│     e. _execute() → Launcher (L-3, L-7 부분실패 회부)       │
│  4'. ── adopt 분기 (L-11=cutover, 항상 HIGH) ──              │
│     · registry 포트 한정 역추적 + cmdline 대조(보조)         │
│     · 사람 승인 → 정지 → 재spawn → 소유(pid,starttime) 전환  │
│  5. LedgerLog append (L-9)                                  │
└──────────────────────────────────────────────────────────┘
    │ ControlDecision(outcome ∈ {executed, rejected, referred})
    ▼ HUD: start/stop/restart 버튼 + 1-클릭 승인 모달
```

- **`_execute` MEDIUM 분기는 a~d 전부 통과 시에만 e 도달** — L-1 우회불가 테스트의 대상.
- `ControlDecision.outcome`에 **`referred`**(사람 회부) 추가 — 1a는 {executed, rejected}만.

---

## 5. HUD (UI — mockup 컨펌 먼저, `[[feedback_ui_design_confirm_first]]`)

> ⚠️ UI는 코드 진입 전 mockup 컨펌 필수. 아래 와이어프레임 컨펌 후 구현.

외부 탭 voice_lab 카드(현 ●작동/○정지 + 🔄)에 lifecycle 컨트롤 추가:

```
┌──────────────────────────────────────────┐
│ 🎙️ 음성 생성 랩 (GPT-SoVITS)      ● 작동  │
│ localhost:8777                       🔄   │
│ ┌─────────┐ ┌─────────┐ ┌──────────┐     │
│ │ ▶ start │ │ ■ stop  │ │ ↻ restart│     │  ← MEDIUM = 클릭 시 승인 모달
│ └─────────┘ └─────────┘ └──────────┘     │
└──────────────────────────────────────────┘
    │ 클릭
    ▼
┌─ 승인 필요 (차단 모달) ──────────────────┐
│ voice_lab 을(를) restart 하시겠습니까?   │
│ 등급: MEDIUM · 최근 60초 0/2회·누적 0/10  │
│      [ 승인 ]        [ 취소 ]            │
└──────────────────────────────────────────┘

  ※ 미소유 PID(예: 502419)일 때 = 인수 모달(L-11, cutover-재기동):
┌─ 인수 필요 (HIGH) ───────────────────────┐
│ PID 502419 는 자비스가 켠 게 아닙니다.    │
│ 포트 8777 점유 · cmdline 대조 통과(보조)  │
│ 정지 후 자비스가 다시 켜서 맡을까요?      │
│ (잠깐 다운타임) [ 인수(꺼다 켜기) ][취소] │
└──────────────────────────────────────────┘
```

- XSS 방어 = textContent 전용(99 entry CB-5 답습). same-origin.
- `referred`(미소유 PID·C-3 초과) = 모달에 사유 표시 + 승인 비활성/경고.
- 인수 모달 = "정지→재기동(cutover)" 명시. cmdline = **대조 통과(보조, 신원 증명 아님)**. 인수는 자율 완화 토글에 *안* 걸림(항상 HIGH).

---

## 6. Provider Liquidity + Rollback Trigger (§8 답습)

- **Provider Liquidity (헌법 5조-2, 비협상)**: Launcher·등급·게이트는 boss LLM·워커 CLI·모델 교체와 무관. boss는 propose만 → boss 교체 시 controller 변경 0. 대상 launch cmd = registry 주입(하드코딩 0). systemd 전환 = launcher 백엔드 교체(코드 변경 0). `[[feedback_provider_liquidity]]`
- **Rollback Trigger (LedgerLog 검출)**: (a) MEDIUM 동작이 게이트 없이 집행 = L-1 회귀, 즉시 중단. (b) 미소유 PID에 signal = L-2 회귀, 중단. (c) C-3 2축 무력화로 폭주 = 중단. (d) 부분 실패 자동 롤백 발생 = L-7 회귀, 중단. (e) controller 자격증명 보유 = B-6 회귀, 중단. (f) 인수가 사람 승인 없이/신원 미확인으로 발생 = L-11 회귀, 중단.

---

## 7. 검증 / TDD 계획 (센서)

- **L-1 우회불가**: boss가 propose("restart")로 MEDIUM 집행에 게이트 없이 도달 불가(seam 테스트).
- **L-5 C-3**: rate 3번째 호출 거부(60s/2) · 누적 11번째 거부(10) · 동시 1인스턴스(기존 PID 시 start 거부).
- **L-2 PID 소유권**: 미소유 PID stop = referred. pkill 경로 부재.
- **L-11 인수(cutover)**: adopt = 항상 사람 승인(approver 없음 = deny). 비-registry 포트 역추적 거부. 승인 → 정지 → controller 재spawn → 소유 `(pid,starttime)` 기록. 무중단 표시-only 경로 부재(1b' DEFER).
- **CB-1 PID recycling**: 소유 PID 죽고 starttime 불일치 시 signal 거부+referred. **CB-2 누적 영속**: controller 재시작 후 ledger 집계로 누적 복원(in-memory 리셋 우회 차단). **CB-5 atomicity**: 동시 propose race 시 한쪽만 통과. **CB-8 dangling**: 부분 실패 후 lock 해제·다음 start LISTEN 부재 확인.
- **L-6 게이트**: approver 없음 = deny(default-deny). approver 예외 = deny(fail-closed).
- **L-3 Launcher**: subprocess 기본 + 주입 launcher 대체(hermetic, 실 spawn 없이). argv `shell=False` 검증.
- **L-7**: restart 중 start 실패 = referred(자동 롤백 0).
- **L-9**: 모든 결정 append-only 기록 assert.
- **B-6 불변**: controller env 자격증명 0 assert 유지.
- **실 e2e (dogfood)**: voice_lab :8777 대상 — controller가 소유 spawn → restart → stop → start, 미소유 502419 = 회부 경로. grimp 단방향 + secret PASS + 기존 전체 green 회귀 0.

---

## 8. 정직 단서 (사전)

- C-3 수치(60s/2·누적10)는 1a probe로 *직접* 실측 불가(부작용 0) → 운영 빈도 근거 + 보수적 사용자 결정. 자율 완화·임계 조정은 1b dogfood 실측 누적 후.
- lifecycle 음색/실효 검증은 사용자 브라우저·실 e2e. 미소유 PID 인수 게이트는 설계만(자동 인수 금지).
- 본 brief = 설계 정리. **코드 변경 0.** 합의 BLOCKING 확정 후 TDD.
