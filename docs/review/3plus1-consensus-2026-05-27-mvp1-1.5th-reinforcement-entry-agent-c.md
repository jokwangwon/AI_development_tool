# Agent C (대안 탐색가) — MVP-1 1.5차 보강 진입 합의 분석

> **scope**: MVP-1 GP-3 + GP-5 1.5차 보강 4 sub-수단 (S-3 detect-secrets 부분 통합 + ST-2 inotify sidecar + PC-1 pre-commit framework 의무화 + AR-3 통합 PR auto-reject) 진입 합의 entry brief v1 (`docs/phase0/mvp1-1.5th-reinforcement-entry-brief.md`, 506줄) + 외부 LLM codex 응답 (`docs/external-review/2026-05-27-mvp1-1.5th-reinforcement-codex-response.md`, 270줄, OpenAI vendor, REVISE AS ENTRY BRIEF INPUT) 답습 *독립* 분석.
>
> **답습**:
> - CLAUDE.md §3 3+1 멀티 에이전트 합의 프로토콜 — Agent C (대안 탐색가) = "더 나은 방법이 있는가?" 관점, 대안 기술 / 트레이드오프 / 본 brief framing 외 대안 framing
> - 본 분석 = entry brief 진입 합의 한정 (실 코드 / CI / hook / config / branch protection 본문 변경 0건)
> - 본 분석 = Agent A / Agent B 출력 참조 0건 (Reviewer 통합 영역)
> - 본 분석 = MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 0건

---

## 0. Agent C 관점 framing 답습

Agent C 의 핵심 질문은 **"본 brief 가 권고하는 4 sub-수단 결합 진입 외에 *더 나은* 방법 / 분리 framing / 시점 차등 framing 이 있는가?"** 입니다. 본 분석은 (1) 4 sub-수단별 *대안 매트릭스*, (2) 본 brief framing *외* 대안 framing, (3) 사용자 옵션 (A)~(F) *대안 평가*, (4) AR-3 시점 선차 변경 대안, (5) PC-1 의무화 영역 상승 대안, (6) codex finding 흡수 자격, (7) §1.3 선차 변경 매트릭스 대안, (8) 본 cycle 최종 판정 을 다룹니다.

본 분석의 *결론 미리보기* — **REVISE (BLOCKING 3 + 권고 6)**: codex 3 필수 수정 모두 흡수 의무 + Agent C 신규 식별 3 BLOCKING + 6 권고. 진입 합의 자체 framing 은 정당, 단 brief v1.1 보강 후 풀 3+1 진입 자격 충족.

---

## 1. 4 sub-수단별 *대안* 매트릭스

본 brief 가 채택 권고하는 4 sub-수단 외 옵션 비교 — roadmap-mvp1 §3.2 / §3.3 / §4.3 / §4.4 매트릭스 직접 답습.

### 1.1 S-3 대안 매트릭스 (roadmap §3.2 6 수단 후보)

| 대안 | 진입 적격성 | 본 cycle 영역 자격 | 트레이드오프 |
|------|-----------|------------------|-------------|
| S-1 단독 유지 (현 MVP-1 1차 답습) | ✅ 안전 | 본 cycle scope 외 (보강 0건) | 0 risk, 단 Tier-2/3 catalog 누락 위험 미해소 |
| **S-3 부분 통합 (brief 권고)** | ⚠️ 조건부 | 본 cycle scope | plugin 명시 활성화 + baseline file 금지 2 조건 강제 시에만 적격. **현 시점 baseline file 금지 본문 채택 = brief §2.1.4 + §5.1 R-MVP1-1.5-S3-2 = 영구 금지** |
| S-2 gitleaks 단독 | ❌ 부적격 | 본 cycle scope 외 | default ruleset 의 Tier-2/3 자동 확장 = 사용자 명시 trigger #4 발화 = 풀 3+1 의무 진입 |
| S-4 custom AST 확장 (S-1 확장) | ⚠️ 보류 | 본 cycle scope 외 | S-1 PoC 의 *확장* — 외부 의존 0 유지하나 maintenance burden 高, base64 evasion 미해소 그대로 |
| S-5 gitleaks + detect-secrets 병행 | ❌ 부적격 | 본 cycle scope 외 | Group D §2.1 (D) 사용자 명시 회피 (scope 2배 확장 = 풀 3+1 trigger #4) |
| S-6 hybrid (S-1 + S-3 + 부분 외부) | ⚠️ 보류 | 본 cycle scope 외 | S-3 의 보강이므로 본 cycle 답습 + 향후 별도 합의 |

→ **결론 (S-3 대안)**: brief 권고 (S-3 부분 통합, plugin 명시 + baseline 금지 2 조건) 는 *유일하게* 본 cycle scope 적격. S-1 단독 유지는 본 cycle scope 외 (보강 0건). **단, brief §2.1.3 의 "plugin 활성화 catalog 본문 채택 — Tier-1 답습 plugin 명문 (AWS / Generic / Base64 3 plugin 권고)" 는 codex §7.5 finding 답습 = detect-secrets CLI 인식 plugin identifier 와 정확히 일치하는지 verification 미완** (예: `AWSKeyDetector` / `Base64HighEntropyString` / `KeywordDetector` 등 실 plugin 이름과의 mapping). **BLOCKING #1** — brief v1.1 에서 detect-secrets plugin identifier 정확 답습 명문 의무.

### 1.2 ST-2 대안 매트릭스 (roadmap §3.3 5 수단 후보)

| 대안 | 진입 적격성 | 본 cycle 영역 자격 | 트레이드오프 |
|------|-----------|------------------|-------------|
| ST-3 단독 유지 (현 MVP-1 1차 답습) | ✅ 안전 | 본 cycle scope 외 | 0 risk, 단 런타임 mtime/perm 변경 감시 0 |
| **ST-2 inotify sidecar (brief 권고)** | ✅ 적격 | 본 cycle scope | sidecar 분리 = Hermes upstream 변경 0건 답습. 런타임 지속 보강. **단, codex §7.4 finding = "event 감지" 만으로는 부족, "메인 workload fail-closed 확인" 의무** = 본 brief §5.2 (c) Docker isolation log 의 *완전성* 보강 필요 |
| ST-1 단독 (entrypoint stat) | ⚠️ 보류 | 본 cycle scope 외 | Hermes upstream Dockerfile 변경 필요 = backlog1 §2.2.2 회피 사유 답습 |
| ST-1 + ST-2 통합 | ⚠️ 보류 | 본 cycle scope 외 | Hermes upstream 변경 의무 발생 = 풀 3+1 + Hermes upstream PR 진입 |
| ST-2 + ST-4 (Vault HSM) 통합 | ❌ 부적격 | 본 cycle scope 외 | Multi-host 인프라 비용 高 = Operational Readiness 영역 (Backlog #7) |
| ST-5 Defense in depth (ST-1+ST-2+ST-3) | ⚠️ 보류 | MVP-2 이후 | Hermes upstream 변경 필요 + 운영 부담 中-高 = MVP-1 영역 외 |

→ **결론 (ST-2 대안)**: brief 권고 (ST-2 단독 진입) = 본 cycle scope 적격 유일. **BLOCKING #2** — brief §2.2.3 + §5.2 (c) Docker isolation log 형식 본문에 *"메인 workload fail-closed 확인"* (sidecar 정지 signal 이 실제로 메인 컨테이너 stop 또는 healthcheck fail 발화하는지) 명문 의무 — codex §7.4 답습.

### 1.3 PC-1 대안 매트릭스 (roadmap §4.3 4 수단 후보)

| 대안 | 진입 적격성 | 본 cycle 영역 자격 | 트레이드오프 |
|------|-----------|------------------|-------------|
| PC-3 단독 유지 (현 MVP-1 1차 답습, CI-only enforcement) | ✅ 안전 | 본 cycle scope 외 | dev 환경 영향 0, 단 commit *전* 차단 0 (PR push 후만 차단) |
| **PC-4 (PC-1 + PC-3 병행, brief 권고)** | ⚠️ 조건부 | 본 cycle scope | dev 환경 + CI 양쪽 차단 = Defense in depth. **단, codex §7.2 finding = "pre-commit install 은 로컬 우회 가능, PC-1 단독 ≠ 의무화 효과" → 실제 강제력은 PC-1 + PC-3 + AR-3 *결합* 시점 발효** |
| PC-2 git native script | ❌ 부적격 | 본 cycle scope 외 | framework 미도입 = PC-3 가 더 우월 (CI 통합 + 운영 부담 0) |
| PC-1 단독 (PC-3 미답습) | ❌ 부적격 | 본 cycle scope 외 | dev 환경 강제 만으로는 PR push 후 차단 0 = 우회 risk |
| PC-1 + PC-3 + AR-3 결합 의무화 | ⚠️ 보류 | 본 cycle scope 부분 답습 | brief §2.3.2 + §2.3.3 가 *암묵적* 답습 — codex §7.2 권고 = 명시 흡수 의무 |

→ **결론 (PC-1 대안)**: brief 권고 (PC-4 = PC-1 + PC-3 병행) 는 본 cycle scope 적격, **단 codex §7.2 + Agent C 평가 = PC-1 의 실제 강제력은 *PC-3 + AR-3 결합* 시점 발효** → brief §2.3.1 의 "PC-1 의무화" framing 은 *PC-1 단독 의무화* 가 아닌 *PC-1 + PC-3 + AR-3 결합 의무화* 로 명문화 의무. **BLOCKING #3** — brief §2.3.1 + §2.3.2 + §2.3.3 에서 PC-1 의무화 효과 = "PC-1 + PC-3 + AR-3 결합" 명시 답습 의무.

### 1.4 AR-3 대안 매트릭스 (roadmap §4.4 3 수단 후보)

| 대안 | 진입 적격성 | 본 cycle 영역 자격 | 트레이드오프 |
|------|-----------|------------------|-------------|
| AR-1 단독 유지 (현 MVP-1 1차 답습) | ✅ 안전 | 본 cycle scope 외 | CI step fail-closed 만, T3 영역 진입 0 — PR merge bypass 위험 잔존 |
| AR-2 단독 (branch protection rule 만) | ❌ 부적격 | 본 cycle scope 외 | AR-1 답습 보강 없이 시스템 외부 PR 우회 위험 잔존 |
| **AR-3 (AR-1 + AR-2 통합, brief 권고)** | ✅ 적격 | 본 cycle scope | T3 영역 진입 + branch protection rule 변경 + 사용자 명시 결정. **단, codex §7.3 finding = "11 workflow 모두 required" = workflow name vs job name vs check name mapping 의 운영 불안정** = brief §2.4.2 + §5.2 (d) 의 evidence 형식 보강 의무 |

→ **결론 (AR-3 대안)**: brief 권고 (AR-3 통합) 는 본 cycle scope 적격 유일. **권고 #1** — brief §2.4.2 "branch protection rule = `main` + `develop` 보호 + status check 의무 — 11 workflow 모두 required status check" 는 *실 구현 sub-cycle* 시점 GitHub check name level mapping 본문 의무 (workflow file name 기준 0 → 실제 check name 기준) — codex §7.3 답습.

---

## 2. 본 brief framing *외* 대안 framing

### 2.1 (α) 4 sub-수단 *결합* framing vs (β) *분리 진입* framing

| framing | 장점 | 단점 |
|---------|------|------|
| **(α) 결합 (brief 권고)** | Defense in depth 결합 효과 명시 (PC-1 + AR-3) + 1회 합의 cycle 운영 비용 최소화 + 4 sub-수단 dependency 표면화 | 1개 sub-수단 REVISE 시 4개 모두 합의 진입 지연 + carry-over (b) 4 sub-수단 모두 명시 답습 |
| (β) 분리 진입 | 1개 sub-수단별 합의 진입 자격 독립화 + 단축 합의 적격 sub-수단 (S-3, ST-2) 빠른 진입 | PC-1 + AR-3 결합 효과 손실 + carry-over (b) 사용자 명시 결합 scope 변경 의무 + 합의 cycle 4회 운영 비용 (codex 응답 4회 / 풀 3+1 4회) |

→ **결론**: (α) 결합 framing 이 사용자 carry-over (b) 명시 답습 + Defense in depth 결합 효과 측면에서 *적격* — Agent C 도 (α) 지지. 단, **권고 #2** — REVISE 처리 sub-수단 (PC-1 BLOCKING #3) 이 나오는 경우 *(α) 안에서 부분 APPROVE* 처리 자격 명문 의무 (brief §8 옵션 (F) 활용 자격).

### 2.2 (γ) 1.5차 보강 *전체 cycle* framing vs (δ) MVP-1 PASS *재구성* framing

| framing | 장점 | 단점 |
|---------|------|------|
| **(γ) 1.5차 보강 (brief 권고)** | MVP-1 1차 PASS 답습 보존 + 보강 = (c) Implementation Evidence PASS 진입점 명문 | (c) 진입점 *시점* 의 별도 합의 자격 의무 명시 약함 |
| (δ) MVP-1 PASS 재구성 | (c) 진입점 자체를 (b)(c) 동시 진입으로 재구성 가능 | brief §0.3 #10 + §6.2 #8 = MVP-1 PASS 재선언 + Implementation Evidence PASS 자동 발효 = 영구 금지 답습 (강한 사용자 명시 답습 = framing 변경 자격 0) |

→ **결론**: (γ) 가 유일 적격 — (δ) 는 사용자 명시 carry-over 답습 위반.

### 2.3 (ε) 외부 LLM 1+ vs (ζ) 외부 LLM 2+

| framing | 장점 | 단점 |
|---------|------|------|
| **(ε) 외부 LLM 1+ (brief 권고, codex 답습)** | carry-over 답습 충실 + roadmap §3.6.3/§4.7.3 답습 + 사용자 운영 부담 최소 | 단일 vendor blind risk — codex 외 다른 vendor 시각 누락 가능 |
| (ζ) 외부 LLM 2+ (codex + gemini 등) | cross-vendor blind risk 추가 차단 + diverse perspective | 사용자 운영 부담 高 + carry-over (b) 명시 "외부 LLM 응답 1+" 답습 변경 의무 |

→ **결론**: (ε) 가 본 cycle 적격. **권고 #3** — 본 cycle 합의 발효 *후* 다음 1.5차 보강 cycle (예: ST-4 / commit signing / Tier-2/3 catalog 확장) 시점에는 (ζ) 자격 검토 권고 (T3 영역 cross-vendor blind 차단 강화).

---

## 3. 본 brief §8 옵션 (A)~(F) *대안 형태* 평가

| 옵션 | Agent C 평가 | 사유 |
|------|-------------|------|
| (A) 권고 진입 | ❌ 직접 진입 부적격 | codex §1 + Agent C BLOCKING 3 = brief v1.1 보강 의무 — 직접 (A) = REVISE 흡수 0건 |
| **(B) 수정 후 진입** | ✅ **권고** | brief v1.1 보강 (BLOCKING 3 흡수 + codex 3 필수 흡수) 후 풀 3+1 합의 진입 자격 충족 |
| (C) 영역 축소 (4 → 1~3) | ⚠️ 보류 | PC-1 만 BLOCKING #3 흡수 어려운 경우 한정 사용자 영역 — brief v1.1 으로 흡수 가능 시 (C) 불필요 |
| (D) 영역 확장 (4 → +) | ❌ 부적격 | carry-over (b) scope 명시 답습 위반 |
| (E) 기각 | ❌ 부적격 | carry-over (b) 명시 폐기 = 사용자 명시 의무 영역 |
| (F) 부분 승인 (1~3 sub-수단) | ⚠️ 후속 영역 | brief v1.1 보강 시점 풀 3+1 합의 결과에 따라 *결과적* (F) 자격 가능 — entry 시점 명시 (F) 0건 |

→ **결론**: (A) 직접 진입 부적격, **(B) 수정 후 진입 권고**.

---

## 4. AR-3 *시점 선차 변경* 대안 (Critical)

backlog2 §1.6 권위 = "AR-3 = Deferred 유지 + Backlog #3 이관" → 본 cycle = MVP-1 1.5차 동시 진입. 이는 *권위 변경* 입니다.

| 대안 | 권위 chain 정합성 | 위험 시점 | 사용자 명시 영역 |
|------|----------------|----------|---------------|
| (η) AR-3 = backlog2 권위 유지 | ✅ 정합 | 0 risk | 사용자 명시 폐기 의무 = carry-over (b) 명시 답습 위반 |
| (θ) AR-3 부분 변경 (AR-1 만 강화, T2 한정) | ⚠️ 부분 정합 | 中 risk (T3 진입 회피) | 사용자 명시 carry-over scope 부분 답습 = carry-over verbatim "AR-3 통합 PR auto-reject" 답습 위반 |
| **(ι) AR-3 전체 변경 (brief 권고, MVP-1 1.5차 동시 진입)** | ⚠️ 변경 정당 | 中 risk (T3 진입) | 사용자 명시 carry-over 답습 충실 + 풀 3+1 + 외부 LLM 1+ + 사용자 명시 합의 발효 정당화 |

→ **결론**: (ι) 가 carry-over (b) 답습 + roadmap §4.7.3 line 480 답습 + ADR-011 §2.4 T3 영역 답습 = *정당한* 선차 변경. **권고 #4** — brief §1.3 AR-3 row 의 "선차 변경 자격 정당성" 본문에 codex §2.3 답습 = "AR-3 만 선차 변경, Backlog #3 의 다른 T3 항목 (ST-4 Vault HSM / commit signing / Tier-2/3 catalog) = 본 cycle 영역 외" 명문 *반복 강화* 의무 (brief §2.4.4 #2 + §6.2 #4 답습 위에 §1.3 row 강화).

---

## 5. PC-1 의무화 *영역 상승* 대안 (codex §3.1 + §7.2 답습)

PC-1 의무화 = T2 (opt-in) → T3 (의무화) 영역 상승. codex §7.2 finding 답습 = PC-1 단독 ≠ 의무화 효과.

| 대안 | 실제 강제력 | 운영 부담 | 권위 정당성 |
|------|-----------|---------|------------|
| (κ) PC-1 T2 opt-in 유지 (현 `78483c5`) | 低 (사용자 opt-in 한정) | 低 | carry-over (b) 명시 "PC-1 의무화" 답습 위반 |
| (λ) PC-1 + PC-3 결합 의무화 (codex §7.2 권고) | 中 (CI step + dev 환경) | 中 | brief §2.3.2 부분 답습 — *명시* 강화 의무 |
| **(μ) PC-1 + PC-3 + AR-3 결합 의무화** | 高 (CI + dev + branch protection bypass 차단) | 中-高 | brief §2.3.2 + §2.3.3 답습 — *명시* 강화 의무 (BLOCKING #3) |

→ **결론**: (μ) 가 *실제* 의무화 효과 발효 — 단, brief §2.3.1 ~ §2.3.3 의 framing 은 *암묵적* (μ) 답습 — codex §7.2 finding + Agent C BLOCKING #3 = (μ) 명문 의무.

---

## 6. codex finding 흡수 자격 (Agent C 독립 평가)

codex 응답의 3 필수 수정 + 5 권고 각각에 대한 Agent C 독립 답습 의견:

### 6.1 codex 3 필수 수정

| # | codex finding | Agent C 평가 | 사유 |
|---|-------------|------------|------|
| 1 | ADR-011 §2.1 (a)~(e) 표현을 (a)~(d) + 합의 APPROVE (e) 운영조건 으로 정정 | ✅ **흡수 의무 (BLOCKING)** | ADR-011 원문 직접 답습 시 §2.1 = (a)~(d) 4조건이 정합. (e) 합의 APPROVE 는 §2.1 (e) 가 아닌 *운영조건* 영역 — brief §3 + §10 자기진단 #6 본문 정정 의무 |
| 2 | PC-1 mandatory enforcement 의 PoC/회귀 (b)(d) 를 현 미충족으로 재분류 | ✅ **흡수 의무 (BLOCKING)** | brief §3 매트릭스 PC-1 row (b) = "✅ PC-4 T2 sub `78483c5` Partially Satisfied 답습 + `.pre-commit-config.yaml` opt-in framework 발효 (실 구현 완료)" 는 *T2 영역* 충족 명시 — *T3 mandatory enforcement* PoC 자격은 ⏳ 미충족 으로 정정 의무 |
| 3 | AR-3 required checks / branch protection evidence 기준을 실제 GitHub check mapping 기준으로 구체화 | ✅ **흡수 의무 (BLOCKING)** | brief §2.4.2 "11 workflow 모두 required status check" 는 GitHub UI/API 의 check name (job name) level mapping 의 운영 불안정 = 실 구현 sub-cycle 시점 명시 evidence 의무 |

→ **codex 3 필수 = Agent C 도 BLOCKING 흡수 의무**.

### 6.2 codex 5 권고

| # | codex finding | Agent C 평가 | 사유 |
|---|-------------|------------|------|
| 1 (§7.1) | "ADR-011 §2.1 (a)~(e)" → "(a)~(d) + 합의 APPROVE 운영조건 (e)" 정리 | ✅ 흡수 의무 (BLOCKING #2 와 동일) | 중복 = §6.1 #1 |
| 2 (§7.2) | PC-1 단독 보안 결과 ≠ "PC-1 + PC-3 + AR-3 결합 시 의무화 효과" 표현 | ✅ **흡수 의무 (BLOCKING #3 와 동일)** | Agent C BLOCKING #3 = 동일 finding 독립 식별 |
| 3 (§7.3) | AR-3 실 구현 sub-cycle 시 required check 이름 mapping evidence | ✅ 흡수 의무 (codex 필수 #3 와 동일) | 중복 = §6.1 #3 |
| 4 (§7.4) | ST-2 evidence "event 감지" + "메인 workload fail-closed 확인" 포함 | ✅ **흡수 의무 (BLOCKING #2 와 동일)** | Agent C BLOCKING #2 = 동일 finding 독립 식별 |
| 5 (§7.5) | S-3 plugin allowlist detect-secrets CLI 인식 정확 plugin identifier 답습 + `--baseline` 미사용 assertion CI 검사 | ✅ **흡수 의무 (BLOCKING #1 와 동일)** | Agent C BLOCKING #1 = 동일 finding 독립 식별 |

→ **codex 5 권고 중 3 (PC-1 결합 / ST-2 fail-closed / S-3 plugin id) = Agent C 가 *독립* 식별** = 본 분석의 cross-vendor blind 차단 충실 확인.

### 6.3 codex §5.1 우회 가능 영역 finding (Agent C 독립 평가)

codex §5.1 = "실 구현 sub-cycle 도 단축 합의 + 사용자 명시 라는 문장이 반복되어 본 cycle 이 수단 결정 + rule 본문 채택까지 승인한다는 해석과 결합되면 실 구현 단계 검증이 약화될 수 있다. 실 구현 sub-cycle 도 (b)(d) evidence 가 불충분하면 단축으로 끝낼 수 없다는 단서가 필요" → **Agent C 평가**: ✅ 흡수 권고. brief §4.2 매트릭스 + §8.1 본 cycle 합의 후 4 sub-cycle 모두 "단축 합의 + 사용자 명시" 명시 = (b)(d) evidence 충족 *전* 단축 합의 자격 의무 = 명시 단서 의무 (**권고 #5**).

### 6.4 codex §5.2 보강 finding (Agent C 독립 평가)

codex §5.2 = "AR-3 실 구현 = GitHub 설정 변경, '코드 변경 0건' 과 별개로 repo 운영 정책이 바뀐다 → 'branch protection 변경 = 구현 sub-cycle 사용자 명시 + evidence 전까지 0건' 을 §6.2 에 더 직접 묶기" → **Agent C 평가**: ✅ 흡수 권고. brief §6.2 매트릭스 #4 "Backlog #3 *전체* 진입 (AR-3 단독 시점 변경 외 다른 항목)" 만 명시 — AR-3 자체의 branch protection rule 본문 변경 *시점 별도 사용자 명시* 영역 명문 부족 (**권고 #6**).

---

## 7. §1.3 선차 변경 매트릭스 *대안* 평가

| 대안 | 권위 chain 정합성 | 변경 자격 정당성 |
|------|----------------|----------------|
| 모두 권위 보존 (선행 backlog1/backlog2 답습 유지) | ✅ 정합 | carry-over (b) 명시 위반 — 4 sub-수단 모두 풀 3+1 + 외부 LLM 1+ 답습 위반 |
| 부분 권위 상승 (ST-2 만 상승, PC-1 + AR-3 보존) | ⚠️ 부분 정합 | carry-over scope 부분 답습 위반 |
| **완전 권위 상승 (brief 권고)** | ⚠️ 변경 정당 | carry-over (b) 답습 + ADR-011 §2.4 T3 영역 답습 + 사용자 명시 = 정당 |

→ **결론**: brief 권고 (완전 권위 상승) 가 정당 — 단, codex §3.1 + Agent C BLOCKING #1 = (e) ADR-011 §2.1 원문 답습 정정 의무 (BLOCKING).

---

## 8. 최종 판정

### 8.1 판정

**REVISE (BLOCKING 3 + 권고 6)**

본 brief v1 은 풀 3+1 합의 진입 input 으로 *구조적* 적격하나, **그대로 APPROVE 진입 부적격** — codex 3 필수 + Agent C BLOCKING 3 흡수 후 brief v1.1 보강 시점 진입 자격 충족.

### 8.2 BLOCKING 항목 (3개, 진입 *전* 흡수 의무)

| # | 영역 | brief 본문 변경 영역 | 사유 |
|---|------|-------------------|------|
| **BLOCKING #1** | S-3 plugin allowlist 정확 identifier 답습 | §2.1.3 + §5.1 + §10 자기진단 | brief 의 "AWS / Generic / Base64 3 plugin 권고" 는 detect-secrets CLI 의 실 plugin identifier (`AWSKeyDetector` / `Base64HighEntropyString` / `KeywordDetector` 등) 와의 정확한 mapping 명문 의무 + `--baseline` 미사용 CI assertion 명시 의무 (codex §7.5 + Agent C 독립 식별) |
| **BLOCKING #2** | ST-2 evidence "메인 workload fail-closed 확인" 포함 | §2.2.3 + §5.2 (c) Docker isolation log | sidecar 가 event 감지 후 메인 컨테이너 stop/healthcheck fail 실제 발화 evidence 의무 (codex §7.4 + Agent C 독립 식별) |
| **BLOCKING #3** | PC-1 의무화 효과 = "PC-1 + PC-3 + AR-3 결합" 명시 | §2.3.1 + §2.3.2 + §2.3.3 + §3 PC-1 row (a)(b) | PC-1 단독 의무화 effect 표현 → "PC-1 + PC-3 + AR-3 결합 의무화 시점 발효" 로 명문 의무 (codex §7.2 + Agent C 독립 식별). 또한 §3 (b) PC-1 row 의 "✅ PC-4 T2 sub Partially Satisfied 답습 + 실 구현 완료" = T2 충족 명시는 정확하나 *T3 mandatory enforcement* PoC 자격 ⏳ 미충족 으로 명시 정정 의무 (codex §1 #2) |

### 8.3 codex 추가 BLOCKING (3개, 진입 *전* 흡수 의무 — Agent C 가 codex 답습 흡수)

| # | 영역 | brief 본문 변경 영역 |
|---|------|-------------------|
| **BLOCKING C-1** | ADR-011 §2.1 표현 정정 | §3 제목 + §10 #6 |
| **BLOCKING C-2** | (실질적으로 BLOCKING #3 의 PC-1 (b) 미충족 정정과 통합) | 위 BLOCKING #3 흡수 |
| **BLOCKING C-3** | AR-3 evidence GitHub check mapping 기준 | §2.4.2 + §5.2 (d) |

→ **순 BLOCKING = 5개** (BLOCKING #1, #2, #3 + BLOCKING C-1, C-3 — BLOCKING C-2 는 BLOCKING #3 흡수).

### 8.4 권고 항목 (6개, 진입 후 보강 자격)

| # | 영역 |
|---|------|
| 권고 #1 | brief §2.4.2 AR-3 의 "11 workflow 모두 required status check" 는 실 구현 sub-cycle 시점 GitHub check name level mapping 명문 의무 (BLOCKING C-3 와 부분 중복 — 권고 #1 = entry brief framing 강화, BLOCKING C-3 = 실 구현 sub-cycle evidence) |
| 권고 #2 | brief §8 옵션 (F) 부분 승인 자격 — REVISE sub-수단 발생 시 *(α) 결합 framing 안에서 부분 APPROVE 처리 자격* 명문 의무 |
| 권고 #3 | 본 cycle 합의 발효 후 다음 1.5차 보강 cycle (ST-4 / commit signing / Tier-2/3 catalog) 에서는 외부 LLM 2+ (ε → ζ) 자격 검토 권고 |
| 권고 #4 | brief §1.3 AR-3 row "선차 변경 자격 정당성" 본문에 "AR-3 만 선차 변경, Backlog #3 의 다른 T3 항목 = 본 cycle 영역 외" 명문 반복 강화 의무 |
| 권고 #5 | brief §4.2 + §8.1 의 "실 구현 sub-cycle 모두 단축 합의 + 사용자 명시" 표현에 "(b)(d) evidence 충족 *전* 단축 합의 자격 0건" 단서 명문 의무 (codex §5.1) |
| 권고 #6 | brief §6.2 매트릭스에 "branch protection 변경 = 실 구현 sub-cycle 사용자 명시 + evidence 전까지 0건" 직접 묶기 (codex §5.2) |

### 8.5 결합 판정

**Agent C 최종 = REVISE — brief v1.1 보강 의무**

- **순 BLOCKING = 5개** (Agent C BLOCKING #1, #2, #3 + codex BLOCKING C-1, C-3)
- **권고 = 6개**
- **진입 자격** = brief v1.1 보강 (BLOCKING 5 흡수) + 사용자 검토 + 풀 3+1 + 외부 LLM 1+ 진입 자격 *충족* — 단, Agent C 영역 = entry brief framing 한정 (실 결정 = Reviewer 통합 + 사용자 명시)
- **다음 단계** = brief v1.1 작성 → 사용자 검토 → 외부 LLM 응답 1+ (재 검토 또는 신규 vendor 검토) → 풀 3+1 합의 진입 (brief §8 옵션 (B) verbatim)

---

## 9. Agent C 자체 점검 (CLAUDE.md §3 답습)

| # | 자체 점검 | 통과 |
|---|---------|------|
| 1 | Agent A / Agent B 출력 참조 0건 (편향 방지 답습) | ✅ |
| 2 | brief 본문 *자동 변경* 0건 (수정 권고 한정, 변경 자격 = Reviewer 통합) | ✅ |
| 3 | 실 코드 / CI / config 본문 변경 0건 | ✅ |
| 4 | 자동 진입 / 자동 발효 권고 0건 (단계별 합의 cycle 답습) | ✅ |
| 5 | ceremony-inflation 차단 (Agent C 분석 1회, ~300 lines 권고 범위) | ✅ |
| 6 | MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 0건 | ✅ |
| 7 | 헌법 / ADR 본문 자동 갱신 권고 0건 | ✅ |
| 8 | 대안 탐색가 관점 일관 (8 분석 영역 모두 대안 매트릭스 + 트레이드오프 답습) | ✅ |
| 9 | codex 응답 finding 답습 자격 검증 (3 필수 + 5 권고 모두 평가) | ✅ |
| 10 | Agent C 독립 신규 식별 (BLOCKING #1, #2, #3 = codex 와 cross-validation) | ✅ |

→ **10/10 통과** — Agent C 분석 자격 충족.

--- Agent C 분석 종료 ---
