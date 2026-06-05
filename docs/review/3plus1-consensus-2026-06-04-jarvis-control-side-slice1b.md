# 3+1 합의 보고서 — Jarvis 제어측 slice-1b (프로세스 lifecycle + 인수)

> **대상 brief**: `docs/phase0/jarvis-control-side-slice1b-lifecycle-brief.md`
> **프로토콜**: CLAUDE.md §3 (제어측 = 보안 다중검증 필수)
> **일자**: 2026-06-04
> **Phase 2 독립 분석**: Agent A(구현 가능성) · Agent B(품질/안전) · Agent C(대안) — 병렬·상호 미참조, 코드 직접 검증
> **Phase 3-4**: Reviewer(메인) 교차 비교 — 핵심 쟁점 `ledger.py`/`process_control.py` 직접 확인
> **최종 판단**: **REVISE (조건부 승인)** — 3개 모두 REVISE 만장일치
> **사용자 결정 대기**: adopt(인수) 경로 갈림길 (CB-7) — cutover-재기동 vs 무중단 표시-only

---

## 1. 일치 (Consensus — 3개 모두 동의) → 채택

| # | 항목 | 근거 (코드 검증) | 출처 |
|---|---|---|---|
| CO-1 | 종합 = **REVISE** (REJECT 아님). 방향(seam 확장·게이트 2축·인수 신중)은 모법/합의와 정합 | 3개 | A·B·C |
| **CO-2** ⭐ | **PID 재사용(recycling) race 차단 = 소유권 키 `(pid, start_time)`** + signal 직전 starttime 재대조. 소유 spawn·인수 공통. cmdline보다 강한 표준 수단 | `/proc/<pid>/stat` starttime (A 실증) | A·B·C 독립 수렴 |
| **CO-3** ⭐ | **누적 카운터 = LedgerLog append-only 파생** (in-memory 단독 금지). controller 재시작 시 누적 0 리셋 = L-5 "리셋 우회 금지" 자기부정 | `ledger.py:60·99-131`(fold=마지막승리라 read() 순회 count 필요) | A·B·C 수렴 |
| CO-4 | cmdline 매칭 = **best-effort detection, prevention 아님**. "✓일치"를 신뢰 신호로 표시 = over-claim | `/proc/<pid>/cmdline` 위조 가능 | B 명시·C·A 동의 |
| CO-5 | L-1 seam / L-7 자동롤백금지 / L-8 argv·shell=False / L-10 제어필드 분리 = **건전·최선** | `process_control.py:264-277` 자연 확장 | A 자연·C 동의·B 정합 |
| CO-6 | **평면 capability→Grade 유지** (동작별 등급 오버라이드 반대). adopt=새 capability HIGH 등재 | `_CAP_GRADE:68-72` max-병합 | C 명시·A·B 정합 |
| CO-7 | B-2 provenance·B-4 localhost·B-6 자격증명 0 = lifecycle/adopt에서 약화 없음(정합) | `process_control.py:140-143·251` | B 검증 |

## 2. 부분 일치 (Partial) → 결정

- **PA-1 LedgerLog 재사용 방식**: 셋 다 "누적을 ledger 파생"으로 수렴하나 A가 인터페이스 부적합을 더 깊이 지적 — (a) `record`는 task_id 필수 → lifecycle용 키 합성(`target:action` 또는 `target` + 이벤트) (b) `fold`는 마지막상태 승리라 count엔 부적합 → `read()` 순회 count (c) `record`는 fail-soft silent인데 **lifecycle 감사는 Rollback Trigger 검출 유일 센서** → lifecycle 경로는 **기록 성공 확인 후 집행(fail-closed)**. → **결정: ledger를 누적/감사 단일 출처로 쓰되 lifecycle 전용 키 합성 + fail-closed 래핑**(CB-2·CB-4).
- **PA-2 신원 확인 수단**: A=`ss -ltnp`(same-UID PID 노출 실증) / C=`/proc/net/tcp` inode 1차(커널 사실, 외부명령·argv injection 표면 0) / B=starttime 강조. → **결정: 포트 점유 사실(`/proc/net/tcp` inode 우선, ss 폴백) + (pid,starttime) recycling 차단 + cmdline은 보조 표시만**. 외부명령 회피는 비BLOCKING 구현 선택.

## 3. 불일치 (Divergence) → 최선 선택

- **DI-1 adopt 처리 (핵심 쟁점)**:
  - **C**: adopt를 **1b'로 분리**, 1b는 소유 lifecycle만. adopt 1차 경로 = **cutover-재기동**(사람 승인→미소유 정지→controller 재spawn으로 소유 전환). 무중단 "살아있는 표시-only 인수"는 1b' DEFER (AC-1+AC-5).
  - **B**: 1b 내 유지하되 무중단 인수의 TOCTOU(SB-3)·cmdline 위장(SB-2)·PID recycling(SB-1) 강화.
  - **A**: 1b 내 유지하되 L-4(동시1인스턴스 거부) vs L-11(인수권유) 우선순위 테이블 필요(A-BL-4).
  - **사용자 결정**: (B) 인수 능력 포함 (단 형태 미정).
  - → **Reviewer 판단**: C의 cutover-재기동이 **사용자 의도(미소유 502419 관리)를 충족하면서 무중단 인수의 본질적 불확실성(B가 정확히 짚은 TOCTOU·cmdline 위장)을 회피**. 그러나 사용자가 "인수"를 명시 선택 → 완전 제거는 사용자 결정 무시. **→ adopt를 두 경로로 분리하고 사용자에게 회부(CB-7)**: (1) cutover-재기동 인수(1b) / (2) 무중단 표시-only 인수(1b' DEFER, B의 SB-1~3 전부 필요).
- **DI-2 신원 수단**: PA-2로 흡수(포트 inode 1차 + starttime + cmdline 보조).

## 4. 누락 (Gap) → 포함 판정

| # | Gap | 출처 | 중요도 | 판정 |
|---|---|---|---|---|
| GP-A1 | **Launcher ≠ 기존 blocking `subprocess.run`** — lifecycle long-lived는 `Popen+start_new_session`(non-blocking) + `spawn(argv,cwd,env)->pid`/`signal(pid,sig)` 분리. 기존 worker subprocess는 전부 run-to-completion(`worker.py:97-100`) | A | HIGH | 포함(CB-3) |
| GP-A4 | L-4 거부 ⊃ L-11 인수권유 우선순위 결정 테이블(미소유 LISTEN 시 거부 vs 인수모달) | A | MEDIUM | 포함(CB-9) |
| GP-B5 | **check-then-act atomicity** — per-target lock critical section = {C-3 검사 + 동시1 + 카운터증가 + PID/starttime + _execute} 원자 | B | HIGH | 포함(CB-5) |
| GP-B6 | seam **구조** 강제 — `_execute`가 게이트/lock 통과 증거 없이 호출되면 raise/no-op (관례 `_`-prefix 불충분) | B | HIGH | 포함(CB-6) |
| GP-B7 | **dangling 상태** — 부분 실패 시 lock 해제 + PID 'dead' 표시 + 다음 start LISTEN/PID 부재 확인 (영구 차단·stale signal 방지) | B | HIGH | 포함(CB-8) |
| GP-C3 | **`os.killpg(pgid)`** 종료 명시 — setsid는 detach지 회수 아님. 손자(GPT-SoVITS 워커) 누수 차단. systemd-run cgroup 회수는 장래 trigger | C | MEDIUM | 포함(CB-3에 흡수) |
| GP-AB | **start 성공 판정 = spawn 반환 아니라 LISTEN probe**(1a 재사용). setsid detach면 waitpid 불가 | A·B·C | MEDIUM | 포함(CB-3에 흡수) |
| GP-B2 | ledger cmdline 기록 시 secret 필터(`_SENSITIVE_NAMES` 답습, B-6 정합) | B | LOW | 포함(CB-4에 흡수) |
| GP-NB3 | launcher 백엔드 주입은 **코어/registry만**(boss 주입 불가 — Provider Liquidity가 공격표면 되지 않게) | B | MEDIUM | 포함(CB-3에 흡수) |

## 5. 최종 판단: **REVISE (조건부 승인)**

방향·게이트 구조·인수 신중론 건전 + 기존 선례(ApprovalGate·process_control seam·ledger·external_registry) 실재. 단 (1)PID recycling race (2)누적 카운터 영속 (3)Launcher long-lived 패턴 (4)atomicity (5)adopt 경로 미확정 → 아래 BLOCKING 충족 + 사용자 adopt 경로 결정 후 TDD.

## 6. 통합 BLOCKING (TDD 진입 전 brief 반영) — CB-1 ~ CB-9

| # | 조건 | 출처 |
|---|---|---|
| **CB-1** | **PID recycling 차단** — 소유권 키 = `(pid, start_time)`(`/proc/<pid>/stat` btime 기반). signal(stop/restart/adopt) 직전 starttime 재대조, 불일치 = PID 재사용 간주 → 거부 + referred. L-2/L-11 공통 | CO-2 (A·B·C) |
| **CB-2** | **누적 영속 = LedgerLog 파생** — 누적(가동 후 10회)은 `read()` 순회로 해당 target executed lifecycle 이벤트 count. in-memory 단독 금지(재시작 리셋=우회). rate(60s/2)=in-memory 허용(재시작=더 보수적) | CO-3 (A·B·C) |
| **CB-3** | **Launcher long-lived 인터페이스** — `spawn(argv,cwd,env)->pid`(non-blocking `Popen`+`start_new_session`) / `signal(pid,sig)` 분리(기존 blocking `subprocess.run` 재사용 금지). 종료 = `os.killpg(getpgid(pid))` (손자 회수, setsid 전제). start 성공 판정 = LISTEN probe(1a 재사용). 백엔드 주입 = registry/코어만(boss 불가) | A(GP-A1)·C(GP-C3)·AB(GP-AB)·B(NB3) |
| **CB-4** | **lifecycle ledger 적합화** — (a) task_id 합성(`target:action:ts`) (b) lifecycle 경로 = **기록 성공 확인 후 집행(fail-closed)**(감사가 유일 센서, `record` 기본 fail-soft와 분리) (c) cmdline 기록 secret 필터 | A(A-BL-3)·B(SB-4·NB-2) |
| **CB-5** | **atomicity** — per-target lock critical section = {C-3 2축 검사 + 동시1인스턴스 + 카운터 증가 + PID/starttime 검사 + `_execute`} 원자. 검사-집행 사이 lock 해제 금지. 동시성 race 테스트 | B(SB-5) |
| **CB-6** | **seam 구조 강제** — L-1 테스트 = (a) boss가 propose 외 경로로 MEDIUM 집행 도달 불가 + (b) `_execute`가 게이트/lock 통과 증거 없이 호출되면 raise/no-op | B(SB-6)·A |
| **CB-7** | **adopt 경로 분리 — ⚠ 사용자 결정 회부** — (1) cutover-재기동 인수(1b: 승인→정지→재spawn 소유전환) / (2) 무중단 표시-only 인수(1b' DEFER, CB-1+TOCTOU 캡처+cmdline deny 필요). cmdline = best-effort 보조(deny 근거 = 사람승인+포트한정) | C(AC-1·AC-5)·B(SB-2·SB-3) |
| **CB-8** | **dangling 처리** — 부분 실패 → referred 전이 + lock 해제(영구차단 방지) + 소유 PID 'dead/uncertain' 표시(stale signal 금지) + 다음 start는 LISTEN/PID 부재 확인 후 진행 | B(SB-7) |
| **CB-9** | **L-4 vs L-11 우선순위 테이블** — 미소유 LISTEN 존재 시 start = 거부인가 인수권유인가 결정 테이블로 `_decide` 분기 명확화 | A(A-BL-4) |

## 7. over-claim 정정 (brief 반영)

| # | 위치 | 정정 |
|---|---|---|
| OC-1 | L-9 "ledger.py 그대로" | "task_id 합성 + fail 정책 fail-closed 재결정 후" (CB-4) |
| OC-2 | L-3 "subprocess 기본" | "기존 blocking run-to-completion과 본질 다름 — non-blocking detached spawn" (CB-3) |
| OC-3 | §5 HUD "✓일치" / L-11 "신원 확인" | "cmdline 대조(best-effort, 신원 증명 아님)" + ✓ → "대조 통과(보조)". 인수 안전 근거 = 사람승인+포트한정 | 
| OC-4 | §2 C-3 표 | "**잠정** — 1b dogfood 실측 후 재조정" 1줄 추가 (`[[feedback_pass_scope_overclaim]]`) |
| OC-5 | L-2 "pkill 금지" | "+ signal 직전 starttime 재대조(PID 재사용 차단)" (CB-1) |

## 8. 동의 — 이미 최선 (대안 불요)

L-1 seam 확장(propose-only→MEDIUM 분기) · L-7 자동롤백금지 · L-8 argv·shell=False · L-10 제어필드 분리 dataclass · 평면 capability 등급(오버라이드 반대) · C-1 subprocess 기본+systemd 주입(s6/runit 과설계 기각) · L-6 ApprovalGate 재사용. (A·B·C 교차 동의)

---

**검증 메모 (Reviewer 직접 확인)**: `ledger.py:60` record task_id 필수 + `:70-79` fail-soft silent + `:99-131` fold 마지막상태승리(count 부적합) → CB-2/CB-4 근거 확증. `process_control.py:264-277` _decide LOW-only→_execute, 나머지 fail-closed → CB-6 seam 확장 지점 확증. `_CAP_GRADE:68-72` SPAWN/SIGNAL=MEDIUM 이미 등재 → start/stop/restart는 Action만 추가, adopt는 새 capability HIGH 등재(CO-6).
