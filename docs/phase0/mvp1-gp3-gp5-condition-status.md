# MVP-1 GP-3 + GP-5 Condition Status (상태 정리 문서, 2026-05-12)

> **본 문서는 *상태 정리 문서* 한정 — 합의 보고서 아님, ADR 아님, 사양 아님**.
>
> GP-3 + GP-5 MVP-1 진입 합의 (`6dc5bdc` + `6808d17`) 이 모두 *APPROVE WITH CONDITIONS* 로 발효된 상태에서, 각 condition 의 *흡수 여부* 와 *후속 영역* 을 분류 정리한다.
>
> 본 문서는 **MVP-1 Implementation Entry 최종 합의 *진입 직전* 입력 정비 한정** — Implementation Evidence PASS / MVP-1 PASS / Operational Readiness PASS / Hermes PMO 격상 모두 *발생시키지 않는다*.

**작성일**: 2026-05-12 후속 7
**상태**: 정리 문서 (DRAFT 아님, 합의 아님 — 단순 *현 상태 enumerate*)
**상위 권위**: GP-3 진입 합의 (`docs/review/3plus1-consensus-2026-05-12-gp3-mvp1-entry.md`, commit `6dc5bdc`) + GP-5 진입 합의 (`docs/review/3plus1-consensus-2026-05-12-gp5-mvp1-entry.md`, commit `6808d17`) + MVP-1 roadmap (`docs/architecture/implementation-runtime-roadmap-mvp1.md`, commits `cddd22f` + `bbc05ca` + `5939c93`)
**답습 출처**:
- GP-3 진입 합의 §6 + §7 + §1.5 4 수단 평가 (S-1 + ST-3 + PC-3 + AR-1) + Conditions C-1 ~ C-4
- GP-5 진입 합의 §6 + §7 + §1.4 5 sub-수단 평가 (T-2 + T-5 + T-6 + PC-3 + AR-1) + Conditions C-1 ~ C-4
- MVP-1 roadmap §3.1.2 G3-7 row (commit `bbc05ca`) + §5.4 GP-3 + GP-5 Integrated Risk Matrix (commit `5939c93`)
- 사용자 명시 진입 명령 답습 (2026-05-12 일곱 번째 명령 — "GP-3 + GP-5 조건 충족 상태 정리")

---

## 0. 본 문서 범위

### 0.1 본 문서가 *하는* 것

1. GP-3 4 conditions (C-1 ~ C-4) 의 *현 상태* 분류 (Satisfied / Deferred / Requires separate consensus / Not applicable to MVP-1)
2. GP-5 4 conditions (C-1 ~ C-4) 의 *현 상태* 분류 (동일)
3. MVP-1 Entry Readiness 판단 (GP-3 / GP-5 각각 + MVP-1 Implementation Entry 통합)
4. 남은 후속 항목 backlog 정리 (1.5차 보강 / T3 영역 / P1 v2 facade MVP / ADR-012 evidence enum / Runtime / Operational Readiness)
5. 다음 합의로 넘길 항목 (MVP-1 implementation entry 최종 합의 준비) 명시

### 0.2 본 문서가 *하지 않는* 것 (사용자 명시 답습 — 2026-05-12 일곱 번째 명령)

- ❌ runtime code 구현
- ❌ CI/hook 구현
- ❌ GP-3 Implementation Evidence PASS 선언
- ❌ GP-5 Implementation Evidence PASS 선언
- ❌ MVP-1 PASS 선언
- ❌ Operational Readiness PASS 선언
- ❌ Hermes PMO 격상 선언
- ❌ GP-3 / GP-5 1.5차 보강 자동 진입 (Conditions C-1 / C-2 = 별도 합의 영역 분리 명시)
- ❌ T3 영역 자동 합의 (Conditions C-2 / C-3 = 별도 풀 3+1 + 외부 LLM 1+ + 사용자 명시 영역 분리)
- ❌ MVP-1 implementation entry 최종 합의 자동 진입 (= 본 문서 *후속* 단계, 별도 사용자 결정 영역)
- ❌ 본 문서를 합의 보고서로 취급 (본 문서 = *상태 정리* 한정, ADR-011 §2.1 (a)~(e) 5조건 evidence 발효 0건)

### 0.3 본 문서의 권위 한계

본 문서는 **상태 정리 한정 — 권위 발행 0건**. 본 문서의 어떤 §도:

- (i) 새로운 합의를 *발생시키지 않으며*,
- (ii) condition 의 *Status* 를 임의로 변경하지 않으며 (Satisfied = 이미 commit 으로 흡수된 영역만 / Deferred = 별도 합의 영역 / Requires separate consensus = 별도 풀 3+1 영역 / Not applicable = MVP-1 영역 외),
- (iii) MVP-1 implementation entry 최종 합의를 *대체하지 않으며*,
- (iv) GP-3 / GP-5 / MVP-1 PASS 를 *선언하지 않으며*,
- (v) 신규 backlog 항목을 임의로 *결정하지 않는다* (모두 GP-3 + GP-5 진입 합의 §6 + §7 답습 한정).

본 문서가 발생시키는 *유일한* 효과는 **현 상태 enumerate + MVP-1 implementation entry 최종 합의 진입 *직전* 입력 정비**.

---

## 1. GP-3 조건 상태 (4 conditions)

### 1.1 GP-3 합의 결과 답습

| 영역 | 답습 |
|------|------|
| 합의 보고서 | `docs/review/3plus1-consensus-2026-05-12-gp3-mvp1-entry.md` (commit `6dc5bdc`, 385줄, push 완료 `95be2e5..6dc5bdc`) |
| 판정 | **APPROVE WITH CONDITIONS — GP-3 MVP-1 진입 가능** |
| 4 수단 조합 | S-1 (Group D custom scanner R-4.1 Tier-1 45 patterns) + ST-3 (docker secret 단독) + PC-3 (CI-only enforcement) + AR-1 (CI step fail-closed) |
| 8 검토 기준 | 8/8 충족 |
| 5 풀 3+1 트리거 | 0/5 발화 → 단축 합의 적격 확정 |

### 1.2 GP-3 4 conditions 현 상태 분류

| Condition | 영역 | **현 상태** | 흡수 commit / 후속 영역 |
|-----------|------|----------|----------------------|
| **C-1** | G3-7 CI secret management row 추가 | ✅ **Satisfied** | commit `bbc05ca` (`docs(runtime): add CI secret management gap to GP-3 roadmap`) + commit `ed1b6d6` (`docs(context): record GP-3 roadmap condition absorption`) — push 완료 `6dc5bdc..ed1b6d6`. mvp1.md §3.1.2 G3-7 row + 핵심 요약 갱신 + 변경 이력 §9 추가. MVP-1 영역 4 항목 + 분리 영역 2 항목 ((iii) MVP-2 GP-2 + `pull_request_target` 별도 합의) |
| **C-2** | 1.5차 보강 영역 (S-3 detect-secrets / ST-2 inotify / PC-4 framework / AR-3 통합) 분리 | ⏳ **Deferred / 1.5차 보강** | 별도 합의 영역 (수단별 풀 3+1 + 외부 LLM 1+ 또는 단축) — `mvp1-gp3-gp5-condition-status.md` §4 backlog #1 답습 |
| **C-3** | T3 영역 (AR-2 branch protection / Vault HSM ST-4 / Tier-2/3 catalog 확장) 분리 | ⏳ **Requires separate full 3+1** | 별도 풀 3+1 + 외부 LLM 1+ + 사용자 명시 영역 (T3 = ADR-011 §2.4 답습) — backlog #3 답습 |
| **C-4** | O-2 (GP-3 + GP-5 통합 위험) §5.4 신설 | ✅ **Satisfied by §5.4 after GP-5 consensus** | commit `5939c93` (`docs(runtime): add GP-3 GP-5 integrated risk matrix`) + commit `f234f97` (`docs(context): record MVP-1 integrated risk absorption`) — push 완료 `6808d17..f234f97`. mvp1.md §5.4 신설 (110 line, 3 통합 위험 IR-1/IR-2/IR-3 + 3 신규 evidence enum 후보 + MVP-1 Handling vs Deferred Handling 분리 + §5.4.4 *범위 한계*) |

### 1.3 GP-3 conditions 합산

| Status | Count | Conditions |
|--------|-------|-----------|
| ✅ Satisfied | 2 / 4 | C-1, C-4 |
| ⏳ Deferred / 1.5차 보강 | 1 / 4 | C-2 |
| ⏳ Requires separate full 3+1 | 1 / 4 | C-3 |
| ⏳ Not applicable to MVP-1 | 0 / 4 | (해당 없음) |

→ **GP-3 = 2/4 Satisfied + 2/4 Deferred / Separate consensus**.

---

## 2. GP-5 조건 상태 (4 conditions)

### 2.1 GP-5 합의 결과 답습

| 영역 | 답습 |
|------|------|
| 합의 보고서 | `docs/review/3plus1-consensus-2026-05-12-gp5-mvp1-entry.md` (commit `6808d17`, 397줄, push 완료 `ed1b6d6..6808d17`) |
| 판정 | **APPROVE WITH CONDITIONS — GP-5 MVP-1 진입 가능** |
| 5 sub-수단 조합 | T-6 = T-2 (import-linter, transitive 강점) + T-5 (custom AST, dynamic + model-name + URL) 병행 + PC-3 (CI-only enforcement) + AR-1 (CI step fail-closed) |
| 책무 분담 매트릭스 | 7/8 cover (의미적 lock-in = MVP-3 G4 §4.6 분리) |
| 8 검토 기준 | 8/8 충족 |
| 5 풀 3+1 트리거 | 0/5 발화 → 단축 합의 적격 확정 |

### 2.2 GP-5 4 conditions 현 상태 분류

| Condition | 영역 | **현 상태** | 흡수 commit / 후속 영역 |
|-----------|------|----------|----------------------|
| **C-1** | 1.5차 보강 영역 (T-1 dependency-cruiser / T-3 grimp / T-4 ruff / T-5 단독 / PC-4 / AR-3) 분리 | ⏳ **Deferred / 1.5차 보강** | 별도 합의 영역 (수단별 풀 3+1 + 외부 LLM 1+ 또는 단축) — backlog #2 답습 |
| **C-2** | T3 영역 (AR-2 branch protection / Tier-2/3 vendor 확장) 분리 | ⏳ **Requires separate full 3+1** | 별도 풀 3+1 + 외부 LLM 1+ + 사용자 명시 영역 — backlog #3 답습 |
| **C-3** | G5-4 P1 v2 facade real 본문 (`src/adapters/llm/facade.py` LiteLLM 실 import) 분리 | ⏳ **Deferred / P1 v2 facade MVP consensus** | 별도 P1 v2 facade MVP 합의 영역 (`llm-providers-design.md` 작업 영역, Group A 2차 §8 TR-1 답습) — backlog #4 답습 |
| **C-4** | O-2 (GP-3 + GP-5 통합 위험) §5.4 신설 | ✅ **Satisfied by §5.4** | commit `5939c93` + `f234f97` (GP-3 C-4 와 동일 commit — 양 GP 합산 흡수) — push 완료 `6808d17..f234f97`. mvp1.md §5.4 신설 |

### 2.3 GP-5 conditions 합산

| Status | Count | Conditions |
|--------|-------|-----------|
| ✅ Satisfied | 1 / 4 | C-4 |
| ⏳ Deferred / 1.5차 보강 | 1 / 4 | C-1 |
| ⏳ Requires separate full 3+1 | 1 / 4 | C-2 |
| ⏳ Deferred / P1 v2 facade MVP consensus | 1 / 4 | C-3 |
| ⏳ Not applicable to MVP-1 | 0 / 4 | (해당 없음) |

→ **GP-5 = 1/4 Satisfied + 3/4 Deferred / Separate consensus**.

---

## 3. MVP-1 Entry Readiness 판단

### 3.1 GP-3 MVP-1 Entry 판단

```
GP-3 MVP-1 Entry = CONDITIONALLY READY
```

**근거**:
- C-1 (G3-7 CI secret management) Satisfied — MVP-1 영역 4 항목 흡수 완료
- C-4 (O-2 통합 위험) Satisfied — §5.4 신설 완료
- C-2 (1.5차 보강) Deferred — MVP-1 *1차* 진입 영역 외, *후속 보강* 영역 분리
- C-3 (T3 영역) Requires separate full 3+1 — MVP-1 진입 영역 외, T3 정책 변경 영역 분리

**해석**: GP-3 의 *MVP-1 1차 진입 적격성* 은 **충족** (4 수단 조합 S-1 + ST-3 + PC-3 + AR-1 + G3-7 흡수). C-2 / C-3 = MVP-1 *후속* 영역으로 분리 명시되어 진입 차단 사유 아님.

### 3.2 GP-5 MVP-1 Entry 판단

```
GP-5 MVP-1 Entry = CONDITIONALLY READY
```

**근거**:
- C-4 (O-2 통합 위험) Satisfied — §5.4 신설 완료
- C-1 (1.5차 보강) Deferred — MVP-1 *1차* 진입 영역 외
- C-2 (T3 영역) Requires separate full 3+1 — MVP-1 진입 영역 외
- C-3 (G5-4 P1 v2 facade real 본문) Deferred — P1 v2 facade MVP 합의 영역 분리. **단, GP-5 MVP-1 진입 자체는 facade *placeholder* 한정으로 적격** (Group A 2차 PoC 답습 — `src/adapters/llm/facade.py` placeholder 시제)

**해석**: GP-5 의 *MVP-1 1차 진입 적격성* 은 **충족** (5 sub-수단 조합 T-6 + PC-3 + AR-1 + 책무 분담 매트릭스 7/8 cover). C-1 / C-2 / C-3 = MVP-1 *후속* / 별도 합의 영역으로 분리 명시되어 진입 차단 사유 아님.

### 3.3 MVP-1 Implementation Entry 통합 판단

```
MVP-1 Implementation Entry = READY FOR FINAL ENTRY CONSENSUS
```

**근거**:
- GP-3 MVP-1 Entry = CONDITIONALLY READY (§3.1)
- GP-5 MVP-1 Entry = CONDITIONALLY READY (§3.2)
- O-2 통합 위험 §5.4 신설 = Satisfied (양 GP 합산 흡수)
- 8 deferred conditions (GP-3 2 + GP-5 3) 모두 *MVP-1 영역 외* 분리 명시 — *진입 차단 사유 아님*
- MVP-1 implementation entry 최종 합의 *진입 직전 입력 정비* 완료 (본 문서 자체)

### 3.4 혼동 금지 — 본 판단의 한계

본 §3 의 *Entry Readiness* 판단은 다음과 *다르다* (사용자 명시 답습):

| 본 §3 판단 | 본 §3 판단 *아님* |
|----------|---------------|
| MVP-1 Implementation Entry = *최종 합의 진입 적격성* | ❌ Implementation Evidence PASS *발효* |
| GP-3 / GP-5 MVP-1 Entry = *진입 적격성* | ❌ MVP-1 PASS *선언* |
| 본 문서 = *상태 정리* | ❌ Operational Readiness PASS *선언* |
| Conditions 흡수 매트릭스 = *현 상태 enumerate* | ❌ Hermes PMO 격상 *선언* |
| READY FOR FINAL ENTRY CONSENSUS = *후속 합의 진입 적격* | ❌ 후속 합의 자동 *발효* |

---

## 4. 남은 후속 항목 (Backlog)

본 §은 GP-3 + GP-5 진입 합의 §6.3 + §7 답습 — 별도 backlog 정리.

| # | Backlog 항목 | 영역 | 합의 형태 | 영향 condition |
|---|----------|------|---------|--------------|
| 1 | **GP-3 1.5차 보강 합의** (S-3 detect-secrets 부분 통합 / ST-2 inotify sidecar / PC-4 framework / AR-3 통합) | GP-3 | 풀 3+1 + 외부 LLM 1+ (수단별) 또는 단축 + 사용자 명시 (PC-4 한정) | GP-3 C-2 |
| 2 | **GP-5 1.5차 보강 합의** (T-1 dependency-cruiser / T-3 grimp / T-4 ruff / T-5 custom AST 단독 / PC-4 / AR-3) | GP-5 | 풀 3+1 + 외부 LLM 1+ (수단별) 또는 단축 + 사용자 명시 (PC-4 한정) | GP-5 C-1 |
| 3 | **T3 영역 별도 풀 3+1** (AR-2 branch protection rule 변경 / Vault HSM ST-4 / Tier-2/3 vendor 확장) | GP-3 + GP-5 공통 | 풀 3+1 + 외부 LLM 1+ + 사용자 명시 (T3 영역 답습) | GP-3 C-3 + GP-5 C-2 |
| 4 | **P1 v2 facade MVP 합의** (G5-4 = `src/adapters/llm/facade.py` LiteLLM 실 import 본문 작성) | P1 v2 | 별도 P1 v2 facade MVP 합의 영역 (Group A 2차 §8 TR-1 답습) | GP-5 C-3 |
| 5 | **ADR-012 §2.2 evidence enum 정식 등록** (4 + 3 = 7 enum 후보: `secret_scan_layer1_implementation` / `secret_storage_isolation_implementation` / `provider_adapter_enforcement_layer1_static` / `mvp1_gate_pass` / `provider_key_adapter_bypass_risk_detected` / `direct_sdk_with_secret_leakage_detected` / `secret_handling_environment_mismatch_detected`) | G4 + ADR-012 | 별도 합의 (G4 §10.2 schema 진화 정책 답습 — 추가 필드 MINOR-호환 영역 + 사용자 명시) | MVP-1 roadmap §5.2 + §5.4 |
| 6 | **Runtime enforcement / CI-hook implementation** | GP-3 + GP-5 + G5-5 Layer 2 | 별도 합의 + ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 결정 (Implementation Evidence PASS 발효 시점) | MVP-1 → MVP-3/4 영역 |
| 7 | **Operational Readiness parity check** (Multi-environment local/CI/Docker parity + Vault HSM ST-4 단일 source) | Operational Readiness | 별도 합의 (MVP-6 영역, ADR-010 답습 + Multi-host 인프라) | MVP-1 → Operational Readiness PASS 영역 |

→ **합산 7 backlog 항목** — 모두 *MVP-1 implementation entry 최종 합의 진입* 후 단계적 처리 영역.

---

## 5. 다음 합의로 넘길 항목 — MVP-1 Implementation Entry 최종 합의 준비

### 5.1 다음 합의 정의

본 상태 정리 후 다음 단계 = **MVP-1 implementation entry 최종 합의 준비**.

| 영역 | 정의 |
|------|------|
| 합의 명 | MVP-1 Implementation Entry 최종 합의 |
| 검토 대상 | GP-3 + GP-5 *통합* MVP-1 implementation entry 적격성 |
| 검토 목적 | GP-3 + GP-5 가 MVP-1 Implementation Entry 에 *들어갈 준비* 가 되었는지 *최종 확인* |
| 검토 기준 | (사용자 명시 결정 영역 — 본 문서 권고 한정) |
| 합의 형태 | (사용자 명시 결정 영역 — 단축 합의 적격성 우선 판단 + 5 트리거 1+ 발화 시 풀 3+1 승격) |
| 결론 형식 | (사용자 명시 결정 영역) |

### 5.2 본 합의가 *아닌* 것 (사용자 명시 답습)

- ❌ Implementation Evidence PASS *발효* 아님 (별도 합의 영역)
- ❌ MVP-1 PASS *선언* 아님 (별도 합의 영역)
- ❌ Operational Readiness PASS *선언* 아님 (MVP-6 영역)
- ❌ Hermes PMO 격상 *선언* 아님 (MVP-6 영역)
- ❌ 실 runtime code 구현 자동 진입 아님 (별도 합의)
- ❌ CI/hook 구현 자동 진입 아님 (별도 합의)

### 5.3 다음 합의 *진입 적격성* (본 문서 §3 답습)

| 적격성 | 본 문서 답습 |
|--------|-----------|
| GP-3 + GP-5 진입 합의 모두 APPROVE WITH CONDITIONS 발효 | §1.1 + §2.1 답습 (commits `6dc5bdc` + `6808d17` push 완료) |
| Conditions C-1 (GP-3) + C-4 (양 GP 공통) Satisfied | §1.2 + §2.2 답습 (commits `bbc05ca` + `ed1b6d6` + `5939c93` + `f234f97` push 완료) |
| 8 deferred / separate consensus conditions 모두 *MVP-1 영역 외* 분리 명시 | §1.2 + §2.2 답습 (Conditions C-2, C-3 GP-3 + C-1, C-2, C-3 GP-5) |
| MVP-1 Implementation Entry = READY FOR FINAL ENTRY CONSENSUS | §3.3 답습 |
| 본 상태 정리 문서 발행 | 본 문서 (commit 예정 — `docs(runtime): summarize GP-3 GP-5 MVP-1 condition status`) |

→ **다음 합의 진입 *적격*** — 사용자 명시 결정 영역.

---

## 6. 본 문서가 *발생시키지 않는* 사항 (사용자 명시 9 금지 답습)

| # | 금지 영역 | 본 문서 위반 |
|---|---------|----------|
| 1 | runtime code 구현 | 0건 |
| 2 | CI/hook 구현 | 0건 |
| 3 | GP-3 Implementation Evidence PASS 선언 | 0건 |
| 4 | GP-5 Implementation Evidence PASS 선언 | 0건 |
| 5 | MVP-1 PASS 선언 | 0건 |
| 6 | Operational Readiness PASS 선언 | 0건 |
| 7 | Hermes PMO 격상 선언 | 0건 |
| 8 | GP-3 / GP-5 1.5차 보강 자동 진입 (Conditions C-1 / C-2 = 별도 합의 영역 분리 명시) | 0건 |
| 9 | T3 영역 자동 합의 (Conditions C-2 / C-3 = 별도 풀 3+1 + 외부 LLM 1+ + 사용자 명시 영역 분리) | 0건 |

→ **9/9 위반 0건**.

---

## 7. 변경 이력

| 일자 | 변경 | 비고 |
|------|------|------|
| 2026-05-12 후속 7 | 신규 작성 (상태 정리 문서) | 사용자 명시 진입 명령 답습 (2026-05-12 일곱 번째 — "GP-3 + GP-5 조건 충족 상태 정리"). GP-3 4 conditions (C-1 Satisfied / C-2 Deferred 1.5차 보강 / C-3 Requires separate full 3+1 / C-4 Satisfied by §5.4) + GP-5 4 conditions (C-1 Deferred 1.5차 / C-2 Requires separate full 3+1 / C-3 Deferred P1 v2 facade MVP / C-4 Satisfied by §5.4) + MVP-1 Entry Readiness (GP-3/GP-5 = CONDITIONALLY READY / MVP-1 Implementation Entry = READY FOR FINAL ENTRY CONSENSUS) + 7 backlog (1 GP-3 1.5차 / 2 GP-5 1.5차 / 3 T3 영역 / 4 P1 v2 facade MVP / 5 ADR-012 evidence enum / 6 Runtime / 7 Operational Readiness parity). 본 문서 = 상태 정리 한정 — 합의 보고서 아님 / Implementation Evidence PASS 0건 / MVP-1 PASS 0건 / Operational Readiness PASS 0건 / Hermes PMO 격상 0건 / runtime 0건 / CI-hook 0건 / 1.5차 보강 자동 진입 0건 / T3 영역 자동 합의 0건. |

---

**다음 단계** (사용자 결정 영역, 본 §5 답습):
**MVP-1 Implementation Entry 최종 합의 준비** — 본 상태 정리 문서 발행 후 사용자 명시 결정으로 진입.
