# 3+1 합의 보고서 (Reviewer 통합) — jarvis 협업 오케스트레이션 brief

**일자**: 2026-05-29 · **대상**: `docs/phase0/jarvis-collaborative-orchestration-design-brief.md` (DRAFT v1)
**구성**: Agent A(구현) / Agent B(안전) / Agent C(대안) / codex(외부 cross-vendor) → Reviewer 교차비교
**판정**: **REVISE** · **사용자 결정**: 제어모델 plan-then-execute 전환 + 단계화 디딤돌0 분리 (둘 다 동의, 2026-05-29)

> Reviewer 코드 실측: RedactionFilter=secret 값·key 마스킹 한정, WorkerRegistry.select=alias dict 룩업, LandlockIsolation=fs 한정+/etc RO, dispatch=단일 워커 — 4개 핵심 인용 사실 확인.

---

## 1. 교차비교 분류

### ① 일치 (4/4 — 강한 신호, 확정 채택)
| 항목 | A | B | C | codex |
|---|---|---|---|---|
| RT-1 redaction ≠ injection 방어 (secret scrubber, NL payload 통과) | 🔴 | 🔴 | 🔴 | 🔴 "가장 큰 결함" |
| §4 "결정적 매핑" 미정 설계, 현 코드 미성립 | 🔴 | ⚠️ | (전제) | 🔴 |
| §6② 산출물 전달 = 최대 위험 (injection propagation) | (함의) | 🔴 | ★대안 | 🔴 "가장 위험" |
| 워커출력→boss→제어결정 루프 = injection 재진입 | 🔴 | 🔴 | ★루프제거 | 🔴 |
| 첫 구현 L1 한정 / L2·L3 묶지 말 것 | ✅ | (동의) | 디딤돌 분리 | "계획1회+controller" |

### ② 부분일치 (2-3개)
- §4 R2 over-claim (B,A,codex): (i)필드부재 보존 / (ii)사후위치 폐기를 "정신 연장" 표기.
- boss 를 제어루프 밖/untrusted planner (C★★★, codex★, A 함의): C·codex 독립 수렴.
- data exfiltration 누락 (B 명시, codex "typed artifact" 함의).

### ③ 불일치 (상충)
- **D-1 직접제어 유지 여부** = 유일한 진짜 분기. brief/사용자(production 표준) vs C(D-1 인용 부정확, LangGraph 실체는 LLM 제어루프 밖) vs codex(조건부 건전, planner 격하 권고) vs A(enum 출력 주체=boss면 경계 재정의). → "직접제어 degree" 스펙트럼, codex/C 가 planner 격하로 수렴. **사용자 결정 영역**.

### ④ 누락 (1개만)
- data exfil via RO 비-secret (B, 채택) / L3 boss 호출 비용 (A, 채택) / OllamaWorker GPU 점유 (A) / **MemoryLog 재사용 불가→LedgerLog** (A, L1 직결, 채택) / ADR-011 selective citation (B, 채택).

## 2. 최종 판정: **REVISE**
4/4 핵심 결함 BLOCKING 일치, codex "REVISE 후 채택", C 강력 대안, A "L1 한정 정확", B BLOCKING 다수이나 방향 부정 안 함 → REJECT 아님. 문제의식·단계화·means/ends 시도 건전, 제어모델·injection 서술 구조 수정 필요. (brief=실 변경 0건 SDD 정리 — REVISE=v2 수정+사전 정비.)

## 3. brief 修正 (BLOCKING vs 권고)

### 🔴 BLOCKING (v2/L1 구현 전 필수)
| # | 修正 | 출처 |
|---|---|---|
| B1 | §3·§6② "RT-1=injection 방어" 삭제/격하 → secret exfil 축소 보조로만. injection 방어는 (c)능력경계+제어모델 구조 책임 | 4/4 |
| B2 | §4 매핑 정직화 — boss schema 가 worker_kind enum 출력 → harness enum→argv 룩업. "워커 종류 선택 주체=boss" 인정, means/ends 재정의 | A,codex,B |
| B3 | 제어모델 재정의 → boss 계획 1회(untrusted proposal) + deterministic controller. 워커출력→boss 제어루프 제거(advisory 격리) | C★★★,codex★,A,B |
| B4 | §6② 산출물 전달 = typed artifact contract. raw NL 전달 금지, NL=untrusted commentary 분리 | codex,B,C |
| B5 | §5 scrub 모순 해소 — raw 전달 vs scrub 영속의 권위·생명주기·injection 검사 시점 명문화 | B |
| B6 | MemoryLog 재사용 불가 → event-sourcing LedgerLog 분리 | A |

### ⚠️ 권고
| # | 修正 | 출처 |
|---|---|---|
| R1 | §4 R2 정직 서술 ((i)보존/(ii)능력경계 대체) | B,A,codex |
| R2 | data exfiltration 위험 추가 (RO 경로 비-secret) | B |
| R3 | ADR-011 (a)~(d) 4조건/검증의무 인용 보강 | B |
| R4 | L3 boss 호출 비용·상한 + OllamaWorker GPU 점유 한계 | A |
| R5 | 단계화 — 통제·히스토리 디딤돌0 독립 출하 | C |
| R6 | "통제된 자식" 인간통제 형태전환 명문화 | B |

## 4. 수렴된 핵심 방향 — boss 를 제어루프 밖으로
C(plan-then-execute+contract-first)와 codex(untrusted planner+deterministic kernel)가 *서로 참조 없이* 동일 아키텍처 수렴, A(L1 한정·호출 상한)·B(D-3 BLOCKING)가 보강. 합의 형태: **boss(약한 로컬 LLM)는 최초 1회 작업그래프+인터페이스 계약을 schema 제안 → 사람 1회 승인 → 의존성/재시도/중단/산출물전달은 결정적 controller (중간 boss 0, 워커간 통신 0).** boss 워커출력 관여=사람용 advisory(_advise)만. 이 단일 변경이 D-3(루프 없어 발생 안 함)·쟁점③(게이트=계획1회)·쟁점②(typed contract)·R2(글자그대로 연장)를 동시에 닫음.

## 5. 불일치/판단 보류 (사용자 결정 → 확정됨 2026-05-29)
1. D-1 직접제어 vs plan-then-execute → **사용자: plan-then-execute 전환 동의**.
2. 단계화 L1 통째 vs 디딤돌0/1 분리 → **사용자: 디딤돌0 분리 동의**.
3. §6③ 재조정 게이트 T1/T2/T3 → plan-then-execute 채택으로 게이트=계획1회 축소, L1 deferred 유지.
