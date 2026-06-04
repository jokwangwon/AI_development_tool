# 3+1 합의 보고서 — Jarvis 제어측 slice-1 (프로세스 제어 도구)

> **대상 brief**: `docs/phase0/jarvis-control-side-general-executor-brief.md`
> **프로토콜**: CLAUDE.md §3 (3+1 멀티에이전트 합의 — 제어측 = 보안 다중검증 필수)
> **일자**: 2026-06-04
> **Phase 2 독립 분석**: Agent A(구현 가능성) · Agent B(품질/안전) · Agent C(대안 탐색) — 병렬·상호 미참조
> **Phase 3-4**: Reviewer 교차 비교 (핵심 쟁점 직접 코드 검증)
> **최종 판단**: **REVISE (조건부 승인)**
> **사용자 결정(2026-06-04)**: C-2 = 초기 1-클릭 → 자율 완화. 진행 = brief REVISE + 합의doc + 커밋.

---

## 1. 일치 (Consensus — 3개 모두 동의) → 채택

| # | 항목 | 근거(코드 검증) |
|---|---|---|
| CO-1 | 종합 = 조건부(REVISE), REJECT 아님. 방향(controller seam + 코어 고정 등급 + boss 제안만)은 X-1~3 정합 | 3개 모두 |
| CO-2 | **ApprovalGate(default-deny + fail-closed)가 우회불가 단일 seam 코드 선례** — slice-1 답습 | `approval.py:41-47`, `plan_controller.py:406-413` |
| CO-3 | **등급은 실제 원시 연산(spawn/signal/probe)에 바인딩**, 동작 이름 문자열 금지(위장 차단) | B 명시, A·C 동의 |
| CO-4 | **PID 소유권 / pkill 금지** — 소유 PID에만 signal (voice_lab 교훈) | 3개 동의 |
| CO-5 | **Provider Liquidity 불변** — boss 제안만, boss 교체 시 controller 변경 0 | `run_from_planner` 주입형 실증(#17 codex) |
| CO-6 | **G5 HTTP(읽기)·G6(a) 코어 고정·미등재 fail-closed·boss 제안만** = 비협상 불변 | 3개 동의 |
| CO-7 | 성능 무시 가능 | A 명시 |

## 2. 부분 일치 (Partial) → 결정

- **PA-1 기존 PlanController 재사용**: 코드 검증 결과 PlanController는 *plan-step DAG dispatcher*(worker subtask)지 *process-lifecycle dispatcher*가 아니다. → **재사용 대상 = 게이트/seam *패턴*(kind_table allowlist + default-deny + fail-closed + 제안만)**, `run()` 직접 아님. **신규 `ProcessController`가 PlanController 검증 골격을 복제/공유**(A·C 수렴).
- **PA-2 C-2 게이트 기본값**: **초기 1-클릭 → dogfood 후 자율 완화**(proportionate). 최종값 사용자 결정 → **사용자 확정: 초기 1-클릭**.
- **PA-3 빈도 게이트**: 단독 불충분 → **rate + 누적(절대 총량) 2축 + 동시 1인스턴스 강제** (BLOCKING).

## 3. 불일치 (Divergence) → 최선 선택

- **DI-1 C-1 controller 형태**: **(a) 본체 내 모듈 + launcher 추상**(기본 subprocess, systemd-run 주입). GB10 systemd 미확인을 비차단화, (a)→(c) 코드 변경 0. C의 systemctl 교훈(포트 해제/pkill 회피)은 launcher 백엔드로 보존. **(b) 독립 데몬 기각**(과설계, 데몬 감독 회귀 — A·C 동의).
- **DI-2 slice 분할**: **1a(포트 LISTEN probe, 자율) → 1b(start/stop/restart, 2축 게이트)**. probe 먼저 박아 C-3 임계를 실측으로 확정. 1b는 1a dogfood 후 명시 진입(자동 진입 0).
- **DI-3 등급 형태**: **평면 테이블 + `Action(name, capabilities=frozenset)` 한겹 분리**. 코어가 capability→등급 매핑(G6(a) 위반 0, slice-2+ 무손실 확장). select_ports(permission→port)가 선례.

## 4. 누락 (Gap) → 포함 판정

| # | Gap | 출처 | 중요도 | 판정 |
|---|---|---|---|---|
| GP-1 | **`/health` 부재**(코드 전수 확인) — §5.2 fiction | A | HIGH | 포함(BLOCKING B-4): probe = 포트 LISTEN + 선택적 HTTP(주입형, 부재 시 LISTEN-only) |
| GP-2 | PID 소유권 비대칭(미소유 프로세스 stop 경로 0) | A | MEDIUM | 포함: 소유 PID만 signal, 미소유=사람 회부 |
| GP-3 | controller 자체 크래시 → 모든 dispatch 거부(fail-closed, open 금지) | B | HIGH | 포함 |
| GP-4 | 동시 race → per-target lock + 동시 1인스턴스 | B | HIGH | 포함(PA-3과 묶음) |
| GP-5 | 부분 실패 시 자동 롤백 금지(통제 보존) | B | MEDIUM | 포함 |
| GP-6 | boss 제안 페이로드 = injection 벡터 → strict 검증, shell 미경유(argv) | B | HIGH | 포함 |
| GP-7 | Rollback Trigger 검출 센서 미명세 → LedgerLog append-only 감사 | B | MEDIUM | 포함 |
| GP-8 | `Action(name, capabilities)` 한겹 분리 | C | MEDIUM | 포함(DI-3) |
| GP-9 | C-4 = external_registry 확장(U-3) 우세, 단 제어 필드 분리 dataclass + provenance 상속 | C, A(스키마 오염) | MEDIUM | 조건부 포함 |

## 5. 최종 판단: **REVISE (조건부 승인)**

방향 건전 + 기존 코드 선례 실재. 단 (1)seam 코드 강제 약속 수준 (2)`/health` 실측 불일치 (3)빈도 게이트 단축 (4)provenance 상속 누락 → BLOCKING 충족 후 slice-1a TDD 진입.

## 6. BLOCKING (구현 진입 전 brief 반영)

| # | 조건 |
|---|---|
| B-1 | **seam 코드 강제** — controller 공개표면=propose-only, `_execute`는 게이트 통과 시 내부 호출. boss 직접 집행 차단을 *우회불가 단위테스트*로 고정(문서 약속 불충분) |
| B-2 | **provenance 상속** — 제어 대상 `origin==jarvis` fail-closed (제어측 > 읽기측 위험, 약화 = 비협상 회귀) |
| B-3 | **빈도+누적 2축 + 동시 1인스턴스** — rate 단독 금지 |
| B-4 | **`/health` 의존 제거** — probe = 포트 LISTEN + HTTP 선택적(주입형) |
| B-5 | **등급 = 원시 연산/capability 바인딩** (이름 문자열 금지) |
| B-6 | **controller 자격증명 0 단위테스트** (slice-4 자격 미끄럼 방지 센서) |

**비BLOCKING(개선)**: controller 크래시 fail-closed(GP-3), 자동 롤백 금지(GP-5), boss 페이로드 strict·argv(GP-6), append-only 감사(GP-7), launcher 추상(DI-1), C-4 제어 필드 분리 dataclass(GP-9).

## 7. 갈림길 결정

| 갈림길 | 권고 | 결정 주체 |
|---|---|---|
| C-1 | (a) 본체 모듈 + launcher 추상(기본 subprocess, systemd-run 주입). 독립 데몬 기각 | 합의 결정 |
| C-2 | 초기 1-클릭 → dogfood 후 자율 완화 | **사용자 확정: 초기 1-클릭** |
| C-3 | 2축 구조 + 동시 1인스턴스 고정. 임계 수치는 1a dogfood 실측 후 | 구조=합의, 수치=사용자(1a 후) |
| C-4 | external_registry 확장 + 제어 필드 분리 dataclass + provenance 상속. 별도 신설 기각 | 합의 결정(provenance 비협상) |
| slice 분할 | 1a(probe, 자율) → 1b(lifecycle, 게이트) | 합의 권고 + 1b 진입 사용자 명시 |
| 채널(G5) | HTTP(probe) + controller subprocess/signal(lifecycle), launcher가 systemctl 흡수 가능 | 합의 재확인(불변) |
| 등급(G6) | 평면 + capability 한겹 분리, G6(a) 코어 고정 | 합의 결정 |

**검증 메모(Reviewer 직접 확인)**: `/health` 부재(server.py 라우트 전수), 127.0.0.1 바인딩(server.py:464 영역), PlanController 게이트 골격(plan_controller.py:144-413), ApprovalGate default-deny/fail-closed(approval.py:41-47), external_registry provenance fail-closed(external_registry.py:83-86), select_ports allowlist(plugin_registry.py:171-182). "PlanController 재사용"은 *패턴* 재사용으로 정확, *클래스 직접* 재사용으로는 부정확(PA-1 수렴 처리).
