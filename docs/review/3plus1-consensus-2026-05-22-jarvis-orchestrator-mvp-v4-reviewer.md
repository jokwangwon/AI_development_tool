# 단축 재합의 보고서 (Reviewer-only) — Jarvis 오케스트레이터 brief v4

**작성일**: 2026-05-22 (세션 3)
**대상**: `docs/phase0/jarvis-orchestrator-mvp-design-brief.md` (DRAFT v4)
**프로토콜**: **Reviewer-only 단축 재합의** (CLAUDE.md §3 적용 기준 "SDD 명세 검토")
**최종 판정**: **APPROVE — MVP-0 구현 진입 가능**

---

## 1. 단축(Reviewer-only) 채택 근거

풀 3+1(Agent A/B/C 병렬)을 생략한 근거:
- brief v1 = **이미 풀 3+1 수행**([[3plus1-consensus-2026-05-22-jarvis-orchestrator-mvp]], REVISE, 12 修正/BLOCKING 5). v2~v4는 그 BLOCKING을 텍스트로 반영 + V-2 실증을 추가한 *증분*.
- 따라서 본 재합의 = "12 修正 반영 검증 + v3 검토 지점 + v4 V-2 정합성 + 잔여 BLOCKING 탐색" = 교차 검증 성격 → Reviewer 역할.
- **편향 방지 장치**: 독립 검토자 1명(general-purpose, read-only) 투입 — brief 작성자 주장을 신뢰하지 않고 findings 원 데이터 + **PoC 산출물(`/tmp/jarvis-v2-poc/ll_sandbox`) 직접 재실행**으로 독립 판단.

## 2. 독립 검토자 실측 대조 (편향 방지)

검토자가 PoC를 직접 재실행하여 작성자 주장과 무관하게 검증:
- `ll_sandbox` 런타임 **Landlock ABI=7** 확인 (V2-2 일치)
- `apparmor_restrict_unprivileged_userns=1` 확인 (P-9/V2-5 일치)
- **격리 재현 성공**: workspace 쓰기 OK / `CLAUDE.md` 읽기 차단 / `~/.ssh` 차단 / 밖 쓰기 차단(PWNED 미생성) = **deny-by-default 실동작 = V2-3 진실**

## 3. 항목별 판정

| 항목 | 판정 | 요지 |
|------|------|------|
| **A. 합의 12 修正 반영** | ✅충족 | BLOCKING 5(修正1·2·3·5·6) + 권고 7개 전부 반영, 누락/왜곡 0 |
| **B. v3 검토 지점** | ✅충족 | MVP-0↔V-2 2-트랙·Q-6"반영 전"·이중격리 효용 서술 일관, 트랙 A/B 분리 모순 0 |
| **C. v4 V-2 정합성** | ⚠️경미→정정 | fs 격리 주장 진실. 단 "claude sandbox 막힘=확정"은 정황(strings)→톤다운 / "~110줄"→90줄 정정 |
| **D. 내부 모순·잔여 BLOCKING** | ✅충족 | 잔여 BLOCKING 0. net(ABI4 후속)·V-1(MVP-1 선결) 모두 MVP-0 진입 비차단 |
| **E. 비례성·헌법** | ✅충족 | Provider Liquidity(사장도 추상)·비례성(~90줄, k3s/HW서명 회피) 정합 |

## 4. 발견 이슈 & 처리

| # | 이슈 | 출처 | 처리 |
|---|------|------|------|
| 1 | "claude 자체 sandbox도 막힘" = 확정 표현, 근거는 strings 정황(V2-6 ⚠️) | C | **정정 반영** — brief v4-3/§6 + findings V-F2를 "막힐 *가능성*(정황)" + "결정적 근거는 커널 강제(정황 독립)"로 톤다운 |
| 2 | "~110줄" vs 실제 `ll_sandbox.c` 90줄(코드 75줄) | C | **정정 반영** — brief·findings "~90줄(코드 75줄)" |
| 3 | 검증된 격리 = **fs-only**, 워커 net egress 미차단(클라우드 CLI 워커가 코드 유출 가능) | D | brief §0/B-3 인정 범위 = BLOCKING 아님. findings **V-F4 신설**로 명문화 + 구현 착수 시 재확인 권고 |

## 5. 최종 판정 — APPROVE (구현 진입 가능)

- BLOCKING 5 전부 반영 + V-2 격리 주장이 **PoC 산출물 직접 재실행으로 fs 격리 실동작 확인**(deny-by-default 진실).
- 트랙 A = V-1/V-2 없이 즉시 진입 가능, 트랙 B 격리 backend 위험도 실증 해소.
- 발견 이슈 3건 모두 경미(표현·줄수·이미 인정된 net 한계) → 정정 완료, 잔여 BLOCKING 0.

**구현 착수 시 재확인 권고**: (1) 트랙 B 격리 = **fs-only**, net egress 차단은 MVP-1+ egress 정책에 의존 / (2) net 포트 제한(ABI4)은 후속 별도 검증.

**범위 한정**: 본 재합의 = "MVP-0 구현 진입 가능 여부" 판단. 사장/워커 모델 결정(Q-1)·런타임 설치(V-1)는 별도 승인 단계.

---
**출처**: brief v4 / [[3plus1-consensus-2026-05-22-jarvis-orchestrator-mvp]](v1 풀 3+1) / [[jarvis-safety-layer-poc-findings]] §6 V-2 / 독립 검토자(read-only, PoC 직접 재실행) / 머신 실측. 답습: `project_jarvis_local_boss_direction` / `feedback_provider_liquidity` / `feedback_proportionate_security_personal_tool` / `project_minimize_user_intervention` / `feedback_staged_consensus_workflow`.
