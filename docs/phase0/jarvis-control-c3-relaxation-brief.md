# Jarvis 제어측 C-3 자율완화 brief — dogfood 실측 근거 + 임계 후보

> **일자**: 2026-06-05 · **브랜치**: `feature/control-c3-autorelax`
> **상태**: brief 작성 완료 → **사용자 검토 대기** → [승인 시] 풀 3+1 합의 → [합의 후] TDD. **자동 진입 0**.
> **선행**: slice-1b(PR #52) 머지 + 본 세션 **dogfood 실측 완료**(아래 §2 Evidence).

> **답습 (비협상 불변 — 재론 금지)**:
> - `docs/phase0/jarvis-control-side-slice1b-lifecycle-brief.md` §2 C-3 (OC-4: "C-3 수치=**잠정**, 1b dogfood 후 재조정") · L-5 (2축 게이트 비협상)
> - `docs/review/3plus1-consensus-2026-06-04-jarvis-control-side-slice1b.md` (CB-2 누적=ledger 파생, DI-2 "임계를 dogfood 실측으로 확정")
> - `src/jarvis/process_control.py` (현 구현 — `rate_limit=2, rate_window=60.0, cumulative_limit=10`)
> - 메모리: `[[feedback_staged_consensus_workflow]]` · `[[project_mvp_staged_roadmap]]`(threshold 고정 0건) · `[[feedback_proportionate_security_personal_tool]]` · `[[feedback_ceremony_inflation]]` · `[[feedback_pass_scope_overclaim]]`

> **북극성**: C-3은 제어측 lifecycle 의 빈도/누적 게이트. 잠정 보수값(2/60s, 누적 10)이 정상 운영을
> 막는지 **실측으로 확인**하고, 폭주 방어는 유지하면서 인간 cadence 를 수용하도록 완화한다.
> **이 brief 는 evidence + 후보만 제시** — threshold *고정* 은 사용자 결정 + 3+1 합의 영역(자율완화의 역설:
> "자율 완화"도 사람이 *한 번* 풀어주는 결정으로 시작한다, C-2 답습).

---

## 0. 왜 지금 — 진입 조건 충족

slice-1b brief OC-4 + 합의 DI-2 가 "C-3 수치는 **잠정**, 1b dogfood 실측 후 재조정"으로 명시했다.
본 세션에서 그 dogfood 를 **실 배선**(server.py 동형 controller: 실 Popen+setsid, 실 `/proc`,
실 `find_listener_pid`, ledger 파생 누적)으로 수행 — 진입 조건 충족.

→ **사용자가 자율완화 합의 진입을 명시(2026-06-05).** 자동 진입 0 충족.

---

## 1. 현 상태 (잠정값)

| 축 | 현 값 | 코드 | 방어 목적 |
|----|-------|------|-----------|
| **rate** | 60s 윈도 내 **2회** | `rate_limit=2, rate_window=60.0` (in-memory) | crash-loop/폭주(초당 다회) 차단 |
| **누적** | 가동 후 총 **10회** | `cumulative_limit=10` (ledger `read()` 파생, CB-2) | controller 재시작으로 rate 우회 차단 |
| **동시1** | 1 인스턴스 | port_pid + `_owned` | 중복 기동 차단 |

3축 중 어느 하나라도 초과 = **사람 회부(referred)**. 2축 비협상(L-5: rate 단독 금지).

---

## 2. Evidence — dogfood 실측 (2026-06-05)

server.py 와 **동일 배선** controller. 안전 가드(사용자 실가동 voice_lab 502419 · HUD 2044777
signal 거부) 하에 실측. 소유 cycle = 무해 stand-in(`http.server`, 자유 포트), 안전 경계 = 실 voice_lab.

| ID | 측정 | 결과 | 의미 |
|----|------|------|------|
| **M1** | 소유 start/restart 실 latency | start **109ms** · restart **209ms** (실 LISTEN probe 포함, pid 변경 확인) | 실 lifecycle op = sub-200ms |
| **M2** | rate 경계 (한 name) | `start→restart` executed, **3번째 op = referred** (`rate 2/60s`) | ⚠ **단일 작업 시퀀스(3-op)가 막힘** |
| **M3** | 누적 경계 (ledger 10건 선적재) | **11번째 executed = referred** (`누적 ≥ 10`, CB-2 파생) | lifetime 총 10회 cap |
| **M4** | CB-9 동시1 (실 voice_lab 8777 점유) | start = **referred** (안 죽임), 502419 생존 | ✅ 동시1 작동 |
| **M5** | L-2 안전 (실 voice_lab 미소유 stop) | **referred**, `launcher.signal` 도달 0, **502419 before=after=alive** | ✅ 안전 경계 **실 1일+ 프로세스로 입증** |

**핵심 발견**:

- **F-1 (rate 너무 타이트, HIGH)**: `start → restart → restart`(또는 start/stop/start 디버깅) 같은
  **정상 단일 작업이 op#3에서 referred**. C-3 rate 의 방어 표적은 *폭주*(초당 수십 회·게이트 미경유)이지
  인간 클릭(분당 2~3회·매 op 승인)이 아니다 → 인간 cadence 를 폭주로 오판.
- **F-2 (누적 lifetime cap 의미론 긴장, MEDIUM)**: `cumulative_count` 는 **time-window 없는 전체
  executed 카운트**. voice_lab 하루 개발에 restart 10회는 쉽게 초과 → 이후 영구 referred(ledger
  clear 전까지). CB-2 의 *원래 목적*(controller 재시작으로 rate 우회 차단)과 "lifetime 절대 10회"가
  섞임 — 정상 운영자도 봉쇄.

**정직 단서 (scope, `[[feedback_pass_scope_overclaim]]`)**:
- M1 timing 은 `http.server`(즉시 기동) 기준. **실 voice_lab(GPT-SoVITS)은 모델 콜드 로드로 start
  latency 가 초 단위** → op-count 기반 rate 가 더욱 부적절(시간 아닌 횟수로 셈). 완화 방향을 *강화*.
- 소유 full-cycle 을 voice_lab *자체* 대상으론 실측 못 함(점유 + 사용자 프로세스 종료 불가).
  adopt cutover 도 동일 사유 스킵(더미 e2e 는 PR #52 에서 완료). → **본 완화는 임계 *값* 한정**,
  소유/회부 *경계 로직*은 1b 합의대로 불변(M4·M5 가 실 프로세스로 재확증).

---

## 3. 임계 후보 비교 (수단 후보 — 결정은 합의/사용자)

> `[[project_mvp_staged_roadmap]]` "수단 결정 / threshold 고정 0건" 답습 — 아래는 *후보*이며
> 본 brief 는 어느 것도 고정하지 않는다. 합의가 후보를 평가하고 사용자가 값을 확정한다.

### 3.1 rate 축

| 후보 | 값 | 장점 | 단점/리스크 |
|------|-----|------|-------------|
| R-a (현 유지) | 2/60s | 최대 보수 | F-1: 정상 작업 봉쇄 |
| **R-b (권고 후보)** | **5/60s** | 인간 cadence(분당 2~5) 수용 + 폭주(초당 수십=분당 수백)는 여전히 차단 | 값 근거 = 실측 아닌 운영 추정(여전히 보수) |
| R-c | 10/60s | 더 여유 | 폭주 판정 둔감(초당 0.17회까지 허용) |

### 3.2 누적 축 (F-2 가 구조 질문을 던짐 — 값 조정 vs 의미론 재정의)

| 후보 | 형태 | 장점 | 단점/리스크 |
|------|------|------|-------------|
| C-a (값만 ↑) | lifetime cap 10 → 100 | 최소 변경 | lifetime 의미론 유지(언젠가 봉쇄) — 미봉책 |
| **C-b (권고 후보)** | **windowed 누적** (예: 1시간 내 N회) — `cumulative_count` 에 시간 필터 추가 | CB-2 원래 목적(재시작 우회 차단)은 보존하되 정상 운영자 영구 봉쇄 해소 | ledger 파생 로직 변경 → 합의 검토 필요(보안 표면) |
| C-c | 누적 축 제거, rate 만 | 단순 | L-5 2축 비협상 위반 → **기각**(재시작 우회 재노출) |

### 3.3 동시1 / 게이트

**변경 없음.** M4 정상. 1-클릭 게이트(C-2)·default-deny(L-6)·소유/회부 경계 전부 불변.

---

## 4. 비협상 (완화 후에도 보존)

- **L-5 2축 게이트 비협상**: 완화 후에도 rate **또는** 누적 어느 한 축 초과 = 사람 회부. rate 단독 금지.
- **CB-2 누적 = ledger 파생**: in-memory 단독 회귀 금지(재시작 우회). windowed 로 가도 출처는 ledger.
- **소유/회부 경계(L-2/CB-1/CB-9)**: 값 변경이 경계 로직을 건드리지 않음(M4·M5 실증).
- **Provider Liquidity**: 임계는 주입 파라미터(`rate_limit` 등 생성자 인자) — 코어 분기 추가 0.

---

## 5. Rollback Trigger (LedgerLog 검출 — 완화 후 회귀 감시)

- (a) 완화값에서 **폭주(초당 다회 lifecycle executed)** 가 referred 없이 통과 = rate 완화 과다, 즉시 환원.
- (b) windowed 누적 도입 시 **controller 재시작 직후 rate 리셋 우회** 재현 = CB-2 회귀, 중단.
- (c) 어느 한 축이라도 "2축 동시 검사" 없이 단독 판정 = L-5 회귀, 중단.

---

## 6. 합의 형태 권고 (`[[feedback_ceremony_inflation]]` 비례)

**권고 = 풀 3+1 합의.** 근거: C-3 = **보안 게이트 변경**(CLAUDE.md §3 매트릭스 "보안 관련 변경 = 3+1 필수").
값만 바꾸는 게 아니라 F-2 가 **누적 축 의미론 재정의(C-b windowed)** 라는 구조 질문을 포함 →
대안 탐색(Agent C)·안전 검증(Agent B) 가치 실재. 단 범위는 **임계 값/누적 형태 한정**(경계 로직 불변)
이라 합의 산출물은 집중적일 것.

**합의에 회부할 질문**:
1. rate 후보 R-b(5/60s) vs R-c(10/60s) — 폭주 판정 민감도 trade-off.
2. 누적 후보 C-a(값↑) vs C-b(windowed) — 미봉책 vs 의미론 재정의(보안 표면 변경) trade-off.
3. windowed 채택 시 시간창·횟수 후보 + ledger 파생 변경의 안전성(CB-2 보존 입증 방법).

---

## 7. 구현 범위 예고 (합의 후 TDD — 본 brief 가 고정하지 않음)

- `ProcessController` 생성자 기본값 조정(`rate_limit`/`cumulative_limit`) — 1줄 수준 + 회귀 테스트.
- (C-b 채택 시) `make_lifecycle_wiring.cumulative_count` 에 시간창 필터 + 테스트.
- server.py 배선 값 동기화(현재 default 사용 — 명시 인자화 여부 합의 결정).
- **RED→GREEN→REFACTOR**: 완화값 경계 테스트(N번째 referred) + 폭주 차단 유지 테스트 + windowed 시간창 테스트.

---

## 부록 — dogfood 재현 메모

throwaway 하네스(`tmp_dogfood_slice1b.py`, 커밋 안 함)로 측정. 핵심: GuardedLauncher 가 보호 PID
(502419·2044777) signal 시도를 RuntimeError 로 차단 → 로직 회귀 시에도 사용자 프로세스 보호.
rate 는 name별 키라 시나리오마다 다른 name 으로 cross-contamination 0. 재현 시 동일 가드 필수.
