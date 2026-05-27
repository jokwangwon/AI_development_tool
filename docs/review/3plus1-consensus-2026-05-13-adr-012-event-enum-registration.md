# Backlog #5 ADR-012 event enum 정식 등록 합의 보고서 (Reviewer-only 단축 합의)

**합의 형태**: **단축 합의 (Reviewer-only)** — 사용자 명시 결정 답습 ((1) brief 승인 / (2) A. APPROVE — Full 8 등록 / (3) R-A Reviewer-only 단축 합의 / (4) A-2 schema_version 0.2 MINOR 격상)
**합의 일자**: 2026-05-13 (MVP-1 PASS Layer D 발효 후속 — commit `210c98f` push 완료 + meta `1518596`)
**검토 대상**: **Backlog #5 ADR-012 event enum 정식 등록 적격성** — MVP-1 Stage 1~5 + IR-1/IR-2/IR-3 누적 8 candidate event enum → ADR-012 §2.2 17 enum 표 *정식 등록* (17 → 25건) + schema_version 0.1 → 0.2 MINOR 격상 + ADR-012 §3.2 단축 합의 권위 답습 + 6/6 풀 3+1 트리거 0건 발화 검증 + Conditions 분리 (C-1 / C-3~C-8 자동 진입 0건)
**보조 참조**:
- MVP-1 PASS (Layer D) 합의 = `docs/review/3plus1-consensus-2026-05-13-mvp1-pass.md` (commit `210c98f`, 533줄, APPROVE WITH CONDITIONS, §C-2 답습 — event enum 정식 등록 Backlog #5 분리)
- MVP-1 Implementation Evidence PASS (Layer C) 합의 = `docs/review/3plus1-consensus-2026-05-13-mvp1-implementation-evidence-pass.md` (commit `6973935`, 409줄, APPROVE)
- ADR-012 §2.2 11 필드 + 17 enum 표 (`docs/decisions/ADR-012-evidence-ledger-protection.md` line 107~149)
- ADR-012 §3.2 schema 진화 정책 — `event` enum 추가 = 단축 합의 + 호환성 보장 + MINOR (line 391)
- ADR-011 §2.4 T1/T2/T3 분류 권위 (`docs/decisions/ADR-011-means-vs-ends-redaction.md`)
- MVP-1 roadmap (deepening) = `docs/architecture/implementation-runtime-roadmap-mvp1.md` (Stage 1~5 + IR-1/IR-2/IR-3 정의)
- Stage 1 actual run PASS (run_id `25728590939` GP-3 secret-hygiene)
- Stage 2 actual run PASS (run_id `25731846625` GP-3 docker secret isolation)
- Stage 3a actual run PASS (run_id `25728590916` GP-5 provider-adapter AST)
- Stage 3b actual run PASS (run_id `25728590977` GP-5 URL/Model)
- Stage 4 actual run PASS (run_id `25738531295` PC-3 + AR-1 통합)
- Stage 5 actual run PASS (run_id `25744711391` G3-7 4 항목, Cycle 4 K-2 known baseline 보존)
- 외부 LLM 응답 (G2+G3+G4) = `docs/external-review/2026-05-07-g2-g3-g4-integrated-gate-review-response.md` §7.6 schema evolution policy 답습

**검토 목적**: Backlog #5 ADR-012 §2.2 event enum 17 → 25건 *정식 등록* + schema_version 0.1 → 0.2 MINOR 격상 한정 — MVP-1 PASS §C-2 Deferred 발효 *행사*

**판정**: ✅ **APPROVE — Full 8 등록 (Reviewer-only 단축 합의) — ADR-012 §2.2 17 → 25 enum + schema_version 0.1 → 0.2 MINOR 격상**

⚠️ **본 합의 = ADR-012 §2.2 schema 문서 갱신 한정** — Operational Readiness PASS (Layer E) / Hermes PMO 격상 (Layer F) / 다른 backlog 자동 진입 / runtime code / CI-hook 구현 *모두 아직 아님*

---

## 0. 사전 점검

### 0.1 가동 사유

사용자 명시 진입 명령 답습 (2026-05-13 — Backlog #5 ADR-012 event enum 정식 등록 합의 *준비* brief 승인 + 4 결정 답습):

> "(1) brief 승인 / (2) A. APPROVE — Full 8 등록 / (3) R-A Reviewer-only 단축 합의 / (4) A-2 schema_version 0.2 MINOR 격상"

**사용자 명시 결정 답습**:
- 검토 형태 = Reviewer-only 단축 합의 (사용자 명시 6 트리거 0건 발화 시)
- 검토 대상 = ADR-012 §2.2 17 → 25 event enum 정식 등록 적격성
- 판정 = **A. APPROVE — Full 8 등록** (8 candidate 전체 정식 등록, ADR-012 §3.2 단축 합의 권위 답습)
- 합의 형태 = (R-A) Reviewer-only 단축 합의 (ADR-012 §3.2 `event` enum 추가 = 단축 합의 본문 명시 답습)
- Schema 정책 = (A-2) 0.1 → 0.2 MINOR 격상 (12 → 25 enum 명백한 schema 확장, 외부 LLM 응답 §7.6 schema evolution policy 답습)
- **본 합의 = ADR-012 §2.2 schema 문서 *갱신* 한정** — Operational Readiness PASS *선언* (Layer E) / Hermes PMO 격상 *선언* (Layer F) / 다른 backlog (#1/#2/#3/#4/#6/#7) 자동 진입 / runtime code 구현 / ledger entry 작성 hook / CI step 추가 / Tier-2/3 catalog 자동 확장 / Hermes upstream 변경 / 외부 LLM 자동 호출 / K-2 baseline 사전 fix **모두 불가**

### 0.2 단축 채택 사유

| 조건 | 충족 |
|-----|------|
| 새 *권위 결정* 0건 (본 검토 = ADR-012 §2.2 기존 17 enum 표 *행사 확장* 한정 — 기존 enum 제거 0건 + rename 0건 + 의미 변경 0건 + 다른 backlog 자동 진입 0건) | ✅ |
| 직전 합의 (MVP-1 PASS Layer D / Layer C / Stage 1~5 entry 모두 Reviewer-only) 패턴 답습 | ✅ |
| ADR-012 §3.2 본문 권위 직접 답습 — "`event` enum 추가 \| 단축 합의 + 호환성 보장 \| MINOR" (line 391) | ✅ |
| ADR-011 §2.4 T2 분류 (사용자 승인 기반 — schema 문서 갱신 한정, T1 deterministic 자동 0 + T3 영역 침범 0) | ✅ |
| 사용자 명시 결정으로 단축 합의 형태 채택 ((R-A) 선택) | ✅ §0.1 답습 |
| **6/6 풀 3+1 승격 트리거 0건 발화** | ✅ §2 답습 |
| MVP-1 PASS (Layer D) 발효 완료 (commit `210c98f` push 완료, §C-2 명시) — 본 합의 = §C-2 *행사* | ✅ §1.0 답습 |
| 8 enum ↔ Stage 1~5 + IR-1/2/3 actual run evidence 1:1 mapping 명확 | ✅ §1.1 답습 |
| 8 enum 모두 provider-neutral + 명명 일관성 + T 분류 정당성 충족 | ✅ §1.2 + §1.3 + §1.4 답습 |
| 기존 17 enum 호환성 보장 (pure addition, 제거/rename 0건) | ✅ §1.5 답습 |

### 0.3 메타 편향 인지

본 Reviewer = Claude Opus 4.7 메인 컨텍스트 = ADR-012 본문 작성자 (2026-05-09 PR-2 합의) + MVP-1 roadmap deepening 작성자 + Stage 1~5 entry 합의 작성자 + Layer C/D 합의 작성자 + 본 Backlog #5 합의 *준비 brief* 작성자. 자기 작성 권위 누적 자기 검토 한계 인지.

**청산 매커니즘**:
1. **사후 외부 LLM 충족 보존** — 누적 cross-vendor blind 의뢰 4건 답습 (ADR-012 PR-2 외부 LLM 2건 포함) — 모두 권위 *내부* 작업으로 통합
2. **격상 전 면제 보존** — Hermes PMO 격상 *전 단계*. 본 검토 = ADR-012 §2.2 schema 문서 갱신 한정 — Operational Readiness PASS (Layer E) / Hermes PMO 격상 (Layer F) 미진입 (외부 LLM + 사람 리뷰 의무 보존)
3. **합의 권위 내부 변경 한정** — 본 검토 = ADR-012 §2.2 표 *행사 확장* + §3.2 단축 합의 권위 답습 — 권위 *내부 행사* 작업
4. **자기 작성 한계 명시** — 본 §0.3 + §5 명시
5. **schema 문서 갱신 한정** (Layer E~F 미진입 / runtime code 0건 / hook 추가 0건 / 다른 backlog 자동 진입 0건)
6. **MVP-1 PASS (Layer D) 발효 선행** — `210c98f` 발효 완료 답습 (§1.0) — 본 합의 = §C-2 *결과 행사* 한정
7. **외부 LLM cross-vendor blind 의뢰 미진입** — 6/6 단축 합의 적격 트리거 0건 발화 + ADR-012 §3.2 단축 합의 권위 명시 답습 + MVP-1 PASS 합의 패턴 일관성

### 0.4 비검토 대상 (사용자 명시 답습)

| 항목 | 본 검토 범위 |
|-----|----------|
| Operational Readiness PASS *선언* (Layer E) | ❌ (MVP-6 영역 — Backlog #7, MVP-1 PASS §C-3 답습) |
| Hermes PMO 격상 *선언* (Layer F) | ❌ (MVP-6 영역 — 외부 LLM + 사람 리뷰 의무, MVP-1 PASS §C-4 답습) |
| `provider-adapter-enforcement.yml` K-2 baseline *fix* | ❌ (별도 Backlog 신규 또는 GP-5 1.5차 흡수, MVP-1 PASS §C-1 답습) |
| GP-3 1.5차 보강 (Backlog #1) | ❌ (별도 합의, MVP-1 PASS §C-5 답습) |
| GP-5 1.5차 보강 (Backlog #2) | ❌ (별도 합의, MVP-1 PASS §C-6 답습) |
| T3 영역 catalog 확장 (Backlog #3) | ❌ (별도 풀 3+1 의무, MVP-1 PASS §C-7 답습) |
| P1 v2 facade MVP (Backlog #4) | ❌ (MVP-3 권고, MVP-1 PASS §C-8 답습) |
| Runtime code / ledger entry 작성 hook / CI step 추가 | ❌ (본 합의 = schema 문서 갱신 한정) |
| 기존 17 enum 제거 / rename / 의미 변경 | ❌ (ADR-012 §3.2 MAJOR 영역 — 본 합의 = pure addition) |
| Hash 알고리즘 변경 (sha256 → blake3 등) | ❌ (ADR-012 §3.2 MAJOR 영역, 별도 풀 3+1 + ADR Amendment 의무) |
| Canonical JSON 규칙 변경 (RFC 8785 JCS / jq fallback) | ❌ (ADR-012 §2.5 본문 — 별도 합의) |
| Hash chain 다층 강제 (Layer 1~5) 갱신 | ❌ (ADR-012 §2.3 본문 — 별도 합의) |
| Round-trip 검증 절차 (T1/T2/T3) 갱신 | ❌ (ADR-012 §2.9 본문 — 별도 합의) |
| Hermes upstream 변경 / 외부 LLM 자동 호출 | ❌ (ADR-008 차단조건 #6 + 부록 B 답습) |

---

## 1. 검토 기준 충족 분석 (8/8)

### 1.0 MVP-1 PASS (Layer D) §C-2 Deferred 답습

MVP-1 PASS (Layer D) `210c98f` §C-2 명시:

> **C-2**: event enum 8 후보 candidate-only → 정식 등록 (Deferred, Backlog #5 ADR-012 §2.2)

본 합의 = §C-2 *결과 행사* — 8 candidate 정식 등록 절차.

ADR-012 §3.2 본문 직접 답습:

> | `event` enum 추가 (12 → 17) | 단축 합의 + 호환성 보장 | MINOR |

본 합의 = 동일 패턴 답습 (17 → 25, schema_version 0.1 → 0.2 MINOR).

### 1.1 출처 정합성 (검토 기준 #1)

8 enum ↔ MVP-1 Stage 1~5 + IR-1/IR-2/IR-3 actual run evidence 1:1 mapping:

| # | enum | 출처 | actual run | commit |
|---|------|-----|----------|------|
| 1 | `secret_scan_layer1_implementation` | Stage 1 (GP-3 S-1) | `25728590939` SUCCESS | `72622409` |
| 2 | `docker_secret_isolation_layer1_implementation` | Stage 2 (GP-3 ST-3) | `25731846625` SUCCESS | `6c6b208` |
| 3 | `provider_adapter_enforcement_layer1_static` | Stage 3 (GP-5 T-6) | `25728590916` / `25728590977` SUCCESS | `72622409` |
| 4 | `pc3_ar1_integration_implementation` | Stage 4 (PC-3 + AR-1) | `25738531295` SUCCESS | `26bc2bb` |
| 5 | `g3_7_workflow_hygiene_implementation` | Stage 5 (G3-7) | `25744711391` SUCCESS | `de727de` |
| 6 | `provider_key_adapter_bypass_risk_detected` | IR-1 (Provider lock-in 위반 detect) | MVP-1 roadmap §IR-1 정의 | `1eab814` (MVP-1 entry 누적) |
| 7 | `direct_sdk_with_secret_leakage_detected` | IR-2 (Direct SDK + secret 검출) | MVP-1 roadmap §IR-2 정의 | `1eab814` (MVP-1 entry 누적) |
| 8 | `secret_handling_environment_mismatch_detected` | IR-3 (환경 secret mismatch detect) | MVP-1 roadmap §IR-3 정의 | `1eab814` (MVP-1 entry 누적) |

**검증 결과**: 8/8 enum 모두 actual run evidence 또는 MVP-1 roadmap 정식 정의와 1:1 mapping ✅

### 1.2 명명 일관성 (검토 기준 #2)

| 검증 항목 | 결과 |
|---------|---|
| snake_case 패턴 | ✅ 8/8 enum 모두 snake_case |
| `<scope>_<action>` 패턴 | ✅ 8/8 enum 모두 `_implementation` (5건) 또는 `_detected` (3건) suffix |
| ADR-012 §2.2 기존 17건과 명명 충돌 | ✅ 0건 (기존: `memory_write`, `skill_*`, `gate_*`, `roundtrip_*`, `chain_*`, `hash_*`, `policy_*`, `canonical_*`, `migration_*`, `evidence_*`, `external_*` / 신규 8건: `*_implementation`, `*_detected` 독립 prefix/suffix) |
| 의미 중복 검증 | ✅ 신규 8 enum 정체성 = MVP-1 *구현* / *검출* 영역, 기존 17 enum = *promotion / governance / roundtrip / migration* 영역 — 분리 명확 |

**검증 결과**: 명명 일관성 + 충돌 0건 ✅

### 1.3 T 분류 정당성 (검토 기준 #3)

ADR-011 §2.4 T1/T2/T3 + ADR-012 §2.2 기존 분류 패턴 답습:

| # | enum | T 분류 | 정당성 |
|---|------|----|---|
| 1 | `secret_scan_layer1_implementation` | **T1 audit** | 구현 audit ledger — deterministic 자동 (CI step 출력 ledger 기록) |
| 2 | `docker_secret_isolation_layer1_implementation` | **T1 audit** | 동일 패턴 (구현 audit) |
| 3 | `provider_adapter_enforcement_layer1_static` | **T1 audit** | 동일 패턴 (구현 audit) |
| 4 | `pc3_ar1_integration_implementation` | **T1 audit** | 동일 패턴 (구현 audit) |
| 5 | `g3_7_workflow_hygiene_implementation` | **T1 audit** | 동일 패턴 (구현 audit) |
| 6 | `provider_key_adapter_bypass_risk_detected` | **T2 사용자 review** | 위반 검출 → 사용자 명시 검토 필요 (ADR-011 §2.4 T2 = 사용자 승인 기반) |
| 7 | `direct_sdk_with_secret_leakage_detected` | **T3 BLOCK** | secret 누출 위험 = 자동 BLOCK + manual (ADR-012 §2.2 #9 `evidence_forgery_detected` T3 BLOCK 패턴 답습) |
| 8 | `secret_handling_environment_mismatch_detected` | **T2 사용자 review** | 환경 mismatch → 사용자 명시 검토 필요 (T2 패턴 답습) |

**T 분류 분포**: T1 audit 5건 + T2 사용자 review 2건 + T3 BLOCK 1건 = 8건

**검증 결과**: ADR-011 §2.4 + ADR-012 §2.2 기존 분류 패턴 일관 ✅

### 1.4 Provider-neutral 강제 (검토 기준 #4)

ADR-012 원칙 11 (provider-specific 식별자 미허용) 검증:

| # | enum | provider-specific 식별자 검증 |
|---|------|---|
| 1 | `secret_scan_layer1_implementation` | ✅ 추상 (secret_scan) |
| 2 | `docker_secret_isolation_layer1_implementation` | ✅ 추상 (docker 일반 명칭, 특정 vendor 0건) |
| 3 | `provider_adapter_enforcement_layer1_static` | ✅ 추상 (provider_adapter) |
| 4 | `pc3_ar1_integration_implementation` | ✅ 추상 (PC-3 + AR-1 내부 코드명) |
| 5 | `g3_7_workflow_hygiene_implementation` | ✅ 추상 (G3-7 내부 코드명) |
| 6 | `provider_key_adapter_bypass_risk_detected` | ✅ 추상 (provider_key, 특정 vendor 0건) |
| 7 | `direct_sdk_with_secret_leakage_detected` | ✅ 추상 (direct_sdk, 특정 vendor 0건) |
| 8 | `secret_handling_environment_mismatch_detected` | ✅ 추상 (secret_handling) |

**검증 결과**: 8/8 enum 모두 provider-neutral — vendor 명 (openai/claude/anthropic/hermes_v1 등) 0건 ✅

### 1.5 호환성 보장 (검토 기준 #5)

ADR-012 §3.2 MINOR 조건 (단축 합의 + 호환성 보장):

| 검증 항목 | 결과 |
|---------|---|
| 기존 17 enum 제거 | ✅ 0건 |
| 기존 17 enum rename | ✅ 0건 |
| 기존 17 enum 의미 변경 | ✅ 0건 |
| 기존 17 enum 타입 변경 | ✅ 0건 (모두 string enum 유지) |
| 신규 8 enum 추가 (17 → 25) | ✅ pure addition |
| schema_version 0.1 진입 시 점에서 backward compatibility | ✅ 0.1 ledger entry import 가능성 보장 (신규 enum 미사용 entry 는 0.1 호환) |
| Migration script 의무 | ✅ 미발생 (pure addition + ADR-012 §3.2 MINOR = migration script 필수 아님, MAJOR 만 의무) |

**검증 결과**: pure addition + backward compatibility 보장 ✅

### 1.6 Schema_version 정책 (검토 기준 #6)

사용자 명시 결정 = **A-2. 0.2 MINOR 격상** 답습.

**근거**:
- 12 MVP 의무 + 5 후속 확장 = 17건 → 17 + 8 신규 = 25건 (47% 확장)
- 외부 LLM 응답 §7.6 schema evolution policy 답습 — "field/enum 추가 시 schema_version bump 명시 권장"
- ADR-012 §3.2 본문 명시: `event` enum 추가 = MINOR semver
- ADR-012 §2.6 0.2 진입 시 새 chain 또는 schema_version 명시 권고 답습

**적용 절차** (본 합의 권위):
- ADR-012 §2.2 schema_version `"0.1"` → `"0.2"` 본문 갱신
- ADR-012 §2.2 17 enum 표 → 25 enum 표 본문 갱신
- ADR-012 §3.2 schema evolution 정책 표 신규 row 추가 (`event` enum 추가 (17 → 25) | 단축 합의 + 호환성 보장 | MINOR)
- ADR-012 §2.6 genesis_hash 정의 0.2 진입 절차 = 별도 합의 영역 (본 합의 범위 외 — schema enum 추가 한정)

**검증 결과**: A-2 0.2 MINOR 격상 정당 ✅

### 1.7 합의 형태 정당성 (검토 기준 #7)

ADR-012 §3.2 본문 권위 직접 답습:

| 변경 유형 | 절차 | semver |
|---------|---|---|
| `event` enum 추가 (12 → 17) | 단축 합의 + 호환성 보장 | MINOR |

본 합의 = 동일 패턴 답습 (17 → 25, MINOR). Reviewer-only 단축 합의 = ADR-012 §3.2 권위 직접 답습.

**6/6 풀 3+1 트리거 0건 발화** (§2 답습) → 풀 3+1 승격 0건.

**검증 결과**: Reviewer-only 단축 합의 = ADR-012 §3.2 권위 답습 + 6/6 트리거 0건 발화 → 정당 ✅

### 1.8 Conditions 분리 (검토 기준 #8)

MVP-1 PASS §C-1 / §C-3~§C-8 자동 진입 0건 검증:

| MVP-1 PASS Condition | 본 합의 진입 | 정체성 |
|------------------|----------|---|
| **C-1** K-2 baseline fix | ❌ 0건 | 별도 Backlog (GP-5 1.5차 흡수 영역) |
| **C-2** event enum 8 후보 정식 등록 | ✅ 본 합의 = §C-2 *행사* | Backlog #5 (본 합의) |
| **C-3** Layer E Operational Readiness PASS | ❌ 0건 | MVP-6 / Backlog #7 |
| **C-4** Layer F Hermes PMO 격상 | ❌ 0건 | MVP-6 / 외부 LLM + 사람 리뷰 의무 |
| **C-5** GP-3 1.5차 보강 | ❌ 0건 | Backlog #1 |
| **C-6** GP-5 1.5차 보강 | ❌ 0건 | Backlog #2 |
| **C-7** T3 영역 catalog 확장 | ❌ 0건 | Backlog #3 (별도 풀 3+1 의무) |
| **C-8** P1 v2 facade MVP | ❌ 0건 | Backlog #4 (MVP-3 권고) |

**검증 결과**: 7/8 Conditions 자동 진입 0건 + 1/8 (§C-2) 본 합의 *행사* 한정 ✅

---

## 2. 풀 3+1 승격 트리거 0/6 발화 검증

brief §4 본문 트리거 답습:

| # | 트리거 | 사후 평가 | 결론 |
|---|--------|---------|---|
| 1 | 1건 이상 enum 명명이 기존 17건과 *의미 중복* | §1.2 답습 — 신규 8 enum suffix (`_implementation` / `_detected`) 와 기존 17 enum suffix (`_write`, `_proposed`, `_approved`, `_promoted`, `_revoked`, `_pass`, `_fail`, `_received`, `_detected` (1건 — `evidence_forgery_detected`), `_lossy`, `_failed`, `_attempted`, `_fallback`, `_broken`) 비교 → `_detected` suffix 가 1건 중복 (`evidence_forgery_detected`) 이지만 의미 분리 명확 (evidence_forgery = P10 위반 / 신규 3건 = secret/SDK/env mismatch 위반). 정체성 영역 분리 명확. | **0건 발화** |
| 2 | 1건 이상 enum 의 T 분류가 ADR-011 §2.4 와 *불일관* | §1.3 답습 — T1 5건 / T2 2건 / T3 1건 모두 정당성 명시. | **0건 발화** |
| 3 | 1건 이상 enum 이 *provider-specific 식별자* 포함 | §1.4 답습 — 8/8 enum 모두 provider-neutral. | **0건 발화** |
| 4 | schema_version 0.1 → 0.2 격상이 *MAJOR 영향* 의심 | §1.5 답습 — pure addition (제거/rename/타입변경 0건) → MINOR 영역 명확. | **0건 발화** |
| 5 | 1건 이상 enum 이 **runtime code 구현** 의 *전제* 가 되는 새 정책 도입 | 8 enum 모두 *기존 구현 ledger entry 명명* 한정 — 새 hook / 새 CI step / 새 정책 도입 0건. ledger entry 작성 hook 자체는 별도 Backlog (Implementation Evidence 영역). | **0건 발화** |
| 6 | 8 enum 출처 (Stage 1~5 + IR-1/2/3) evidence 와 *1:1 mapping 불가* | §1.1 답습 — 8/8 enum actual run + commit hash mapping 명확. | **0건 발화** |

**결과**: **6/6 트리거 0건 발화** → Reviewer-only 단축 합의 적격 ✅

---

## 3. 8 enum 정식 등록 결정

### 3.1 ADR-012 §2.2 enum 표 갱신 본문 (17 → 25건)

본 합의 권위로 ADR-012 §2.2 11 필드 표 + enum 표 다음 본문 갱신 결정:

**MVP 의무 12 enum (변경 0건, schema_version 0.1 유지)**: 1~12 (기존 본문 그대로).

**후속 확장 5 enum (변경 0건, schema_version 0.2 진입 시 정식)**: 13~17 (기존 본문 그대로).

**신규 8 enum 추가 (schema_version 0.2 정식 등록, 본 합의 권위)**:

| # | enum | 정체성 | T 분류 | 출처 |
|---|------|------|------|---|
| 18 | `secret_scan_layer1_implementation` | Secret scan Layer 1 구현 ledger | T1 audit | MVP-1 Stage 1 (GP-3 S-1) |
| 19 | `docker_secret_isolation_layer1_implementation` | Docker secret 격리 Layer 1 구현 ledger | T1 audit | MVP-1 Stage 2 (GP-3 ST-3) |
| 20 | `provider_adapter_enforcement_layer1_static` | Provider adapter Layer 1 static 검출 ledger | T1 audit | MVP-1 Stage 3 (GP-5 T-6) |
| 21 | `pc3_ar1_integration_implementation` | pre-commit + auto-revert 통합 구현 ledger | T1 audit | MVP-1 Stage 4 (PC-3 + AR-1) |
| 22 | `g3_7_workflow_hygiene_implementation` | Workflow hygiene 4 항목 구현 ledger | T1 audit | MVP-1 Stage 5 (G3-7) |
| 23 | `provider_key_adapter_bypass_risk_detected` | Provider lock-in 위반 detect | T2 사용자 review | MVP-1 IR-1 |
| 24 | `direct_sdk_with_secret_leakage_detected` | Direct SDK + secret 검출 | T3 BLOCK + manual | MVP-1 IR-2 |
| 25 | `secret_handling_environment_mismatch_detected` | 환경 secret mismatch detect | T2 사용자 review | MVP-1 IR-3 |

**총 25 enum**: 12 MVP 의무 (0.1) + 5 후속 확장 (0.2) + **8 신규 (0.2, 본 합의 권위)** = 25건.

### 3.2 schema_version 0.1 → 0.2 MINOR 격상 (A-2 답습)

**격상 절차** (본 합의 권위):
- ADR-012 §2.2 11 필드 구조 본문 schema_version `"0.1"` → `"0.2"` 갱신 (예시 entry)
- ADR-012 §2.2 enum 표 25 enum 정식 등록 (위 §3.1 답습)
- ADR-012 §3.2 schema evolution 정책 표 신규 row 추가 — "`event` enum 추가 (17 → 25) | 단축 합의 + 호환성 보장 | MINOR"
- ADR-012 §2.6 genesis_hash 0.2 진입 시 새 chain 명시 = 별도 합의 영역 (본 합의 범위 외)

**Backward compatibility 보장**:
- 0.1 ledger entry 는 0.2 import 가능 (신규 enum 미사용 시)
- 0.2 entry 가 0.1 enum 1~17 만 사용 = 0.1 entry 와 의미 동일
- 새 enum 18~25 = 0.2 entry 에서만 사용 → 0.1 호환 ledger 에서 import 시 unknown enum → reject 권고 (별도 합의 영역)

**Hash chain 영향**:
- 본 합의 = ADR-012 §2.2 schema 본문 갱신 한정
- 기존 0.1 chain hash chain 영향 0건 (canonical JSON 영향 0건)
- 새 0.2 chain 도입 = 별도 합의 영역 (ADR-012 §2.6 답습)

### 3.3 본 합의 권위 적용 범위

| 적용 항목 | 본 합의 처리 |
|---------|---|
| ADR-012 §2.2 11 필드 본문 갱신 | ✅ 본 합의 권위 |
| ADR-012 §2.2 enum 표 17 → 25 갱신 | ✅ 본 합의 권위 |
| ADR-012 §3.2 schema evolution 표 신규 row 추가 | ✅ 본 합의 권위 |
| schema_version 0.1 → 0.2 격상 권위 | ✅ 본 합의 권위 (MINOR + 호환성 보장) |
| ADR-012 본문 갱신 commit | ⏳ 사용자 명시 진입 후 (본 합의 보고서 commit 후속 단계) |
| ledger entry 작성 hook / CI step 추가 | ❌ 본 합의 범위 밖 (별도 Backlog) |
| 0.2 chain 도입 / genesis_hash 0.2 절차 | ❌ 본 합의 범위 밖 (별도 합의) |
| MVP-1 actual run ledger entry 소급 작성 | ❌ 본 합의 범위 밖 (Implementation Evidence 영역, ledger writer 구현 후) |

### 3.4 후속 작업 권고 (사용자 결정 영역)

본 합의 발효 *후* 다음 후속 작업 권고 — 모두 사용자 명시 진입 의무:

1. **ADR-012 본문 갱신 commit** — §2.2 schema_version + 25 enum 표 + §3.2 evolution 정책 row 추가 (3 위치)
2. **MVP-1 roadmap (deepening) cross-reference 갱신** — 8 enum 정식 등록 완료 명시 (§candidate-only → §정식)
3. **CONTEXT/INDEX/SESSION 메타 갱신** — Backlog #5 발효 + MVP-1 PASS §C-2 충족 상태 반영
4. **MVP-1 PASS (Layer D) §C-2 상태 갱신** — Deferred → ✅ 충족 (Backlog #5 발효)
5. **K-2 baseline fix 합의** — 별도 Backlog 진입 (사용자 결정 영역)
6. **ledger entry 작성 hook / CI step 구현** — Implementation Evidence 영역 (별도 합의 후 MVP-N 진입)

각 후속 작업은 **사용자 명시 진입 명령 후** 만 진행 — 자동 chaining 0건.

---

## 4. 합의 형태 / Provenance

### 4.1 합의 형태

**Reviewer-only 단축 합의** (사용자 명시 결정 (R-A) 답습).

**근거 chain**:
1. ADR-012 §3.2 본문 권위 — "`event` enum 추가 \| 단축 합의 + 호환성 보장 \| MINOR" (line 391)
2. 6/6 풀 3+1 트리거 0건 발화 (§2 답습)
3. MVP-1 PASS (Layer D) 합의 패턴 답습 — Reviewer-only 단축 합의
4. 직전 합의 chain (Layer C / Stage 1~5 entry 모두 Reviewer-only) 일관성
5. 사용자 명시 결정 (R-A) 선택

### 4.2 Provenance 기록

**Approval provenance** (외부 LLM 응답 §7.4 답습):
- 승인자: 사용자
- 승인 일자: 2026-05-13
- 승인 대상 artifact: 본 합의 보고서 + ADR-012 §2.2 + §3.2 본문 갱신
- 승인 문구: "(1) brief 승인 / (2) A. APPROVE — Full 8 등록 / (3) R-A Reviewer-only 단축 합의 / (4) A-2 schema_version 0.2 MINOR 격상"
- 승인 commit: 본 합의 보고서 commit (후속 단계)

### 4.3 합의 권위 chain

| Layer | 발효 | 본 합의 권위 의존 |
|---|---|---|
| **MVP-1 PASS (Layer D)** | `210c98f` (2026-05-13) | §C-2 *행사* — 본 합의 = §C-2 발효 결과 |
| **ADR-012 §2.2** (PR-2 합의) | 2026-05-09 | 본 합의 = §2.2 enum 표 *행사 확장* |
| **ADR-012 §3.2** (PR-2 합의) | 2026-05-09 | 본 합의 = §3.2 단축 합의 권위 *직접 답습* |
| **ADR-011 §2.4 T1/T2/T3** | 2026-05-08 | 본 합의 = T 분류 정당성 (§1.3) |
| **외부 LLM 응답 §7.6 schema evolution** | 2026-05-07 | 본 합의 = schema_version bump 권위 (§1.6) |

---

## 5. 자기 편향 정직성 명시

본 Reviewer = Claude Opus 4.7 메인 컨텍스트 자기 작성 권위 누적 자기 검토 한계 인지 (§0.3 답습).

**자기 한계 정직성** (5 항목):

1. **본 합의 권위 = 자기 작성 누적 행사** — ADR-012 (2026-05-09 본문 작성자) + MVP-1 roadmap (deepening) + Stage 1~5 entry + Layer C/D 합의 모두 본 Reviewer 작성 → 본 합의 = 누적 자기 권위 *행사 확장*. 외부 LLM cross-vendor blind 의뢰 미진입 — 6/6 단축 합의 적격 트리거 0건 발화 + ADR-012 §3.2 단축 합의 권위 명시 답습 + MVP-1 PASS 합의 패턴 일관성 답습 → Reviewer 만으로 충분.
2. **격상 전 면제 보존** — Hermes PMO 격상 *전 단계*. 본 검토 = ADR-012 §2.2 schema 문서 갱신 한정 → Operational Readiness PASS (Layer E) / Hermes PMO 격상 (Layer F) 미진입. 외부 LLM + 사람 리뷰 의무 보존.
3. **합의 권위 내부 변경 한정** — 본 검토 = ADR-012 §2.2 표 *행사 확장* + §3.2 권위 답습. 권위 *외부 확장* 0건 + 새 권위 도입 0건.
4. **schema 문서 갱신 한정** — runtime code 0건 + hook 추가 0건 + CI step 추가 0건 + 다른 backlog 자동 진입 0건.
5. **8 enum 출처 정직성** — 5 enum (Stage 1~5) 은 actual run evidence + commit hash 명확. 3 enum (IR-1/2/3) 은 MVP-1 roadmap 정의 + entry 합의 commit `1eab814` 누적 기반 — actual run 의 직접 trigger 는 미발생. 본 합의 = 정의 등록 한정, IR-1/2/3 의 *실제 검출 trigger* 는 Implementation Evidence 영역 (별도 Backlog).

---

## 6. 권위 / 후속 영역

### 6.1 본 합의 발효 결과

✅ **Backlog #5 ADR-012 event enum 정식 등록 발효** — 8 candidate → 25 enum 정식 등록 + schema_version 0.1 → 0.2 MINOR 격상.

✅ **MVP-1 PASS (Layer D) §C-2 충족** — Deferred → 충족 (본 합의 발효 결과).

✅ **ADR-012 §3.2 권위 답습** — `event` enum 추가 = 단축 합의 + 호환성 보장 + MINOR.

### 6.2 본 합의 *미발효* 영역 (3/3 명시)

❌ **Operational Readiness PASS (Layer E)** — 본 합의 미진입. MVP-6 / Backlog #7 / 외부 LLM + multi-environment parity 의무.

❌ **Hermes PMO 격상 (Layer F)** — 본 합의 미진입. MVP-6 / 외부 LLM + 사람 리뷰 의무.

❌ **다른 backlog 자동 진입** (#1/#2/#3/#4/#6/#7) — 본 합의 미진입. 각 backlog 별도 사용자 명시 합의 의무.

### 6.3 다음 세션 권장 시작점

본 합의 발효 *후* 사용자 결정 영역 권장 우선순위:

1. **본 합의 보고서 commit + ADR-012 본문 갱신 commit + CONTEXT/INDEX/SESSION 메타 갱신 commit** (3 commit 분리 패턴 답습)
2. **사용자 명시 push 명령 후 push**
3. **K-2 baseline fix 합의** (Backlog 신규 또는 GP-5 1.5차 흡수, 사용자 결정 영역)
4. **GP-3 1.5차 보강 합의** (Backlog #1)
5. **GP-5 1.5차 보강 합의** (Backlog #2)
6. **P1 v2 facade MVP 합의** (Backlog #4, MVP-3 권고)
7. **T3 영역 별도 풀 3+1** (Backlog #3, AR-2 / Vault HSM / Tier-2/3)
8. **MVP-2 진입 합의** (G2 GP-2 + G4 §4.4 Layer 4, 외부 LLM line 242 + C-7 답습)
9. **Layer E Operational Readiness parity** (MVP-6, Backlog #7)
10. **Layer F Hermes PMO 격상** (MVP-6, 외부 LLM + 사람 리뷰 의무)

각 항목 모두 **사용자 명시 진입 명령 후** 만 진행 — 자동 chaining 0건.

---

## 7. 발생 / 미발생 매트릭스

### §7.1 발생 (본 합의 작업)

- 본 합의 보고서 1건 (본 파일)
- 8 enum 정식 등록 권위 결정 (§3.1)
- schema_version 0.1 → 0.2 MINOR 격상 권위 결정 (§3.2)
- ADR-012 §2.2 + §3.2 본문 갱신 권위 적용 (§3.3 — 후속 commit 단계)
- MVP-1 PASS (Layer D) §C-2 충족 발효 결과
- 6/6 풀 3+1 트리거 0건 발화 검증 (§2)
- 8/8 검토 기준 충족 검증 (§1)
- Conditions 분리 (C-1 / C-3~C-8 자동 진입 0건) 검증 (§1.8)

### §7.2 미발생 (금지 사항 0/N 위반 검증)

| 금지 항목 | 본 합의 처리 |
|---------|---|
| Operational Readiness PASS *선언* (Layer E) | ❌ 0건 |
| Hermes PMO 격상 *선언* (Layer F) | ❌ 0건 |
| 다른 backlog 자동 진입 (#1/#2/#3/#4/#6/#7) | ❌ 0건 |
| Runtime code / ledger entry 작성 hook / CI step 추가 | ❌ 0건 |
| K-2 baseline 사전 fix | ❌ 0건 |
| 기존 17 enum 제거 / rename / 의미 변경 / 타입 변경 | ❌ 0건 |
| Hash 알고리즘 변경 (sha256 → blake3 등) | ❌ 0건 |
| Canonical JSON 규칙 변경 | ❌ 0건 |
| Hash chain Layer 1~5 갱신 | ❌ 0건 |
| Round-trip 검증 절차 갱신 | ❌ 0건 |
| Hermes upstream 변경 / 외부 LLM 자동 호출 | ❌ 0건 |
| Tier-2/3 catalog 자동 확장 | ❌ 0건 |
| 합의 권위 외부 확장 / 새 권위 도입 | ❌ 0건 |
| 외부 LLM cross-vendor blind 의뢰 자동 진입 | ❌ 0건 |

**검증**: 14/14 금지 사항 0건 위반 ✅

---

## 8. 최종 판정

✅ **APPROVE — Full 8 등록 (Reviewer-only 단축 합의)**

- **본 합의 발효 영역**: Backlog #5 ADR-012 §2.2 17 → 25 event enum 정식 등록 + schema_version 0.1 → 0.2 MINOR 격상
- **합의 형태**: Reviewer-only 단축 합의 (ADR-012 §3.2 권위 답습 + 6/6 트리거 0건 발화)
- **검토 기준 충족**: 8/8 (§1)
- **금지 사항 위반**: 0/14 (§7.2)
- **MVP-1 PASS (Layer D) §C-2 상태**: Deferred → ✅ 충족

⚠️ **본 합의 ≠ Operational Readiness PASS (Layer E) ≠ Hermes PMO 격상 (Layer F) ≠ 다른 backlog 자동 진입** — 모두 별도 사용자 명시 합의 의무.

---

**합의 발효 일자**: 2026-05-13
**합의 보고서 commit**: (후속 단계)
**ADR-012 본문 갱신 commit**: (후속 단계 — 사용자 명시 진입 후)
**Push**: (후속 단계 — 사용자 명시 push 명령 후)
