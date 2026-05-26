# Backlog #3 T3 영역 후속 Brief — Group β + γ-1 + γ-2 풀 3+1 진입 정비

> **본 brief는 Backlog #3 (T3 영역) 中 *Group α 풀 3+1 합의 발효 이후 잔여* (Group β + γ-1 + γ-2) 의 풀 3+1 합의 *진입 정비* 한정이다.** Group α (AR-3 + PC-4 T3 sub) = 2026-05-14 풀 3+1 합의 (`3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md`, 657줄, 3/3 만장일치 APPROVE WITH CONDITIONS) 로 *수단 결정 적격성 권위 권고* 발효 完. 본 brief = 그 외 **잔여 4 sub-영역 (Group β 2 + Group γ-1 1 + Group γ-2 1)** 의 진입 정비 + GP-3 진입 condition C-3 / GP-5 진입 condition C-2 ("T3 영역 별도 풀 3+1") 와의 직결 매핑.
>
> 본 brief = **기존 합의 출처 + 외부 LLM 응답 2건의 synthesis + 진입 정비 한정**. **수단 결정 / threshold 고정 / 합의 보고서 작성 / commit / push / 실 진입 모두 0건**. 모든 *결정* 은 별도 풀 3+1 합의 (사용자 명시 승인 후).
>
> ⚠️ **T3 영역 = 보안 enforcement → CLAUDE.md §3 풀 3+1 (Agent A + Agent B + Agent C + Reviewer) *의무* 영역. Reviewer-only 단축 합의 *부적격*** (§5 답습).

**작성일**: 2026-05-20
**상태**: DRAFT — 사용자 승인 대기 (합의 미진입)
**상위 권위**: ADR-011 §2.4 (T3 영역 = 풀 3+1 + 외부 LLM 1+ cross-vendor blind + 사용자 명시 의무), ADR-011 §2.1 (a)~(e) 5조건, ADR-008 부록 B (외부 LLM 응답 = 입력 한정) + 부록 C (Hermes PMO Activation Cross-Reference), ADR-012 §원칙 9 (Hermes ≠ root of trust)
**근거 합의 / 입력**:
- `docs/review/3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md` (Group α 단독 풀 3+1, 3/3 만장일치 APPROVE WITH CONDITIONS, 12 조건 C-1~C-12 + §8 옵션 F/G/H 잔여 진입 후보)
- `docs/external-review/2026-05-13-backlog3-t3-zone-review-response-gemini.md` (Gemini 3 Flash — 19 질문, 종합 (C) PARTIAL)
- `docs/external-review/2026-05-13-backlog3-t3-zone-review-response-gpt.md` (GPT-5.5 Thinking — 19 질문, 종합 (C) PARTIAL + Group γ → γ-1/γ-2 분리 권고)
- `docs/external-review/2026-05-13-backlog3-t3-zone-review-request.md` (cross-vendor blind 의뢰서, 19 질문 / 3 Group × 6 + 종합 1)
- `docs/review/3plus1-consensus-2026-05-12-gp3-mvp1-entry.md` (GP-3 MVP-1 진입 — **C-3 = T3 영역 별도 풀 3+1**)
- `docs/review/3plus1-consensus-2026-05-12-gp5-mvp1-entry.md` (GP-5 MVP-1 진입 — **C-2 = T3 영역 별도 풀 3+1**)
- prep brief 계보: v1 `ad9a02d` (828줄) → v2 `2a9d02d` (969줄) → Group α brief `db0e3ac` (687줄)

---

## 0. 본 brief 범위

### 0.1 본 brief 가 *하는* 것

1. Group α 풀 3+1 합의 발효 후 **Backlog #3 T3 영역 잔여 sub-영역 status 정리** (§1)
2. **GP-3 진입 condition C-3 + GP-5 진입 condition C-2 ("T3 영역 별도 풀 3+1") 미해소 직결 매핑** — 어느 잔여 sub-영역이 두 condition 을 해소하는지 (§2)
3. 잔여 4 sub-영역 (Group β 2 + γ-1 1 + γ-2 1) 의 *진입 단위 / 책무 영역 / 진입 적합성* 정비 (§3)
4. 외부 LLM 응답 2건 (Gemini + GPT, 2026-05-13) 의 잔여 그룹 판정 *입력 한정* synthesis (§4)
5. **T3 영역 = 풀 3+1 의무 영역 (Reviewer-only 단축 부적격) 명시 + 풀 3+1 트리거 발화 매트릭스** (§5)
6. 잔여 그룹 *권고 진입 순서 / 그룹화 후보* + GPT γ-1/γ-2 분리 권고 흡수 (§6)
7. Rollback Trigger / cross-reference 영역 정리 (§7)
8. 다음 단계 (사용자 결정 영역, 자동 진입 0건) (§8)

### 0.2 본 brief 가 *하지 않는* 것 (사용자 명시 영구 답습)

- ❌ **풀 3+1 합의 보고서 작성** (Agent A/B/C 분석 / Reviewer 종합 = 별도 합의 단계 — 사용자 명시 승인 후)
- ❌ **commit / push** (본 brief = untracked DRAFT 한정)
- ❌ **수단 *결정*** (Group β catalog Tier 정의 / γ-1 chmod 강제 형태 / γ-2 Vault 인프라 형태 모두 별도 풀 3+1)
- ❌ **threshold 고정** (FP/FN rate / dev_env_install_rate / Tier 분류 기준 등)
- ❌ **Tier-2/3 catalog 본문 확장** (URL Tier-1 10 / Model Tier-1 19 / R-4.1 Tier-1 42 보존)
- ❌ **Hermes upstream Dockerfile 변경** (entrypoint stat / chmod / image 빌드)
- ❌ **Vault HSM 구현** (실 Vault 클라이언트 / 실 HSM / ADR-010 §X 본문 변경)
- ❌ **branch protection rule 실 변경** (Group α C-1 답습 — 실 활성화 = Backlog #6 + 사용자 명시)
- ❌ **Operational Readiness PASS (Layer E) 선언** / **Hermes PMO 격상 (Layer F) 선언**
- ❌ **MVP-1 exit 발효** (GP-3 5/5 + GP-5 5/5 + 사용자 명시 — 본 brief 영역 외)
- ❌ **actual run 재실행 / CI workflow 변경 / workflow_dispatch 추가 / paths 필터 변경**
- ❌ **Phase α defer-lockdown 변경** (별개 트랙 — 충돌 0건, 본 brief 영향 0건)
- ❌ **외부 LLM 응답 결론 *강제 채택*** (응답 = 입력 한정 + 풀 3+1 평가 대상)
- ❌ **외부 LLM 추가 자동 호출 / cross-vendor blind 의뢰 자동 재발송**
- ❌ Group α 합의 / prep brief 계보 (`ad9a02d` / `2a9d02d` / `db0e3ac`) 본문 변경
- ❌ ADR 본문 자동 갱신 (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012)
- ❌ 본 brief 자체의 합의 자동 진입 (사용자 명시 승인 후 별도 단계 — staged cycle 답습)

### 0.3 본 brief 의 권위 한계

본 brief = **synthesis + 진입 정비 DRAFT 한정**. 본 brief 의 어떤 §도 그 자체로:

- (i) Group β / γ-1 / γ-2 의 수단을 *결정* 하지 않으며,
- (ii) GP-3 C-3 / GP-5 C-2 를 *해소* 하지 않으며 (해소 = 잔여 풀 3+1 합의 발효 + 사용자 명시 후),
- (iii) T3 영역 *실 진입* / 어떤 PASS 를 *선언* 하지 않으며,
- (iv) 외부 LLM 응답 결론을 *강제 채택* 하지 않으며 (입력 한정),
- (v) Phase α defer-lockdown / actual run / CI workflow / Operational Readiness PASS / Hermes PMO 격상을 *발생시키지 않는다*.

본 brief 가 발생시키는 *유일한* 효과 = **잔여 4 sub-영역의 풀 3+1 합의 *진입 정비* 답습 한정** (Layer 0.5 가이드). 모든 *결정* 은 *별도 풀 3+1 합의*.

---

## 1. 본 brief 의 위치 — Backlog #3 T3 영역 진행 status

### 1.1 Backlog #3 T3 영역 6 sub-영역 → 4 그룹 → 진행 status

Backlog #3 T3 영역 = 6 sub-영역 (의뢰서 §3 답습). prep brief v2 (`2a9d02d`) 및 GPT γ 분리 권고 흡수 시 **4 진입 단위**:

| 진입 단위 | 구성 sub-영역 | 책무 영역 | 진행 status |
|---|---|---|---|
| **Group α** | (1) AR-3 + (3) PC-4 T3 sub | enforcement / dev 환경 차단 | ✅ **풀 3+1 합의 발효 完** (`2026-05-14`, 3/3 만장일치 APPROVE WITH CONDITIONS, 14 결정 영역 수단 권고) |
| **Group β** | (2) T-5 (β) + (6) Tier-2/3 catalog 일반 | catalog source 정책 (GP-3 + GP-5) | ⏳ **풀 3+1 미진입** (본 brief 잔여 영역) |
| **Group γ-1** | (4) C-5b ST-1 (Hermes upstream chmod 600) | secret source / Hermes upstream | ⏳ **풀 3+1 미진입** (GPT 분리 권고 흡수) |
| **Group γ-2** | (5) Vault HSM ST-4 (ADR-010 통합) | secret source / Multi-host 인프라 | ⏳ **풀 3+1 미진입** (양 vendor DEFER/BLOCK to MVP-6 권고) |

> **GPT γ-1/γ-2 분리 권고 흡수 근거** (GPT 응답 §Q19): "ST-1은 비교적 작은 file permission guard이지만, ST-4는 인프라/운영/비용/PMO 경계가 모두 걸린 큰 결정. 둘을 같은 합의 단위로 묶으면 ST-1까지 불필요하게 지연되거나, 반대로 ST-4가 너무 빨리 끌려올 위험." → 본 brief = Group γ = γ-1 + γ-2 분리 진입 단위로 정비 (Group α 합의 §8 옵션 G/H 가 이미 γ-1/γ-2 분리 표기 답습).

### 1.2 Group α 합의가 *남긴* 잔여 진입 후보 (합의 §8 옵션 F/G/H)

Group α 합의 §8 (다음 단계, 자동 진입 0건) 이 명시한 잔여 진입 후보 — 본 brief 가 정비하는 대상:

| 합의 §8 옵션 | 영역 | 본 brief 정비 |
|---|---|---|
| (F) | **Group β (T-5 β + Tier-2/3 일반) policy/audit-only 합의 진입 brief** | ✅ §3.1 + §6 |
| (G) | **Group γ-1 (C-5b ST-1) 분리 합의 진입 brief** (downstream wrapper preflight) | ✅ §3.2 + §6 |
| (H) | **Group γ-2 (Vault HSM ST-4) MVP-6 보류 확정 합의** | ✅ §3.3 + §6 (단, ⚠️ §5 — Reviewer-only 단축 부적격 재평가) |

---

## 2. GP-3 C-3 + GP-5 C-2 미해소 직결 매핑

### 2.1 두 condition 의 원문 답습

| condition | 출처 | 원문 (답습) | 상태 |
|---|---|---|---|
| **GP-3 진입 C-3** | `3plus1-consensus-2026-05-12-gp3-mvp1-entry.md` §판정 | "C-3 **T3 영역 별도 풀 3+1**" — AR-2 branch protection / Vault HSM / Tier-2/3 catalog 확장 = 별도 풀 3+1 + 외부 LLM 1+ + 사용자 명시 | ⏳ **미해소** |
| **GP-5 진입 C-2** | `3plus1-consensus-2026-05-12-gp5-mvp1-entry.md` §판정 | "C-2 **T3 영역 별도 풀 3+1**" — AR-2 branch protection / facade real 본문 P1 v2 / Tier-2/3 vendor 확장 = 별도 풀 3+1 + 외부 LLM 1+ + 사용자 명시 | ⏳ **미해소** |

> 두 condition 모두 GP-3 / GP-5 MVP-1 진입 합의 (2026-05-12, Reviewer-only 단축) 가 진입을 *허용하면서* T3 영역을 *별도 풀 3+1* 로 분리·이연한 결과. 즉 **Backlog #3 T3 영역 = 두 condition 의 해소 vehicle**.

### 2.2 각 condition 해소에 필요한 잔여 진입 단위 매핑

| condition 의 T3 영역 항목 | 해소 진입 단위 | Group α 합의로 이미 다룬가? |
|---|---|---|
| AR-2 branch protection (GP-3 C-3 / GP-5 C-2 공통) | **Group α** | ✅ 다룸 (수단 권고 발효 — 실 활성화 = Backlog #6 + 사용자 명시) |
| Tier-2/3 catalog 확장 (GP-3 C-3) / Tier-2/3 vendor 확장 (GP-5 C-2) | **Group β** | ❌ 미진입 — **GP-3 C-3 / GP-5 C-2 직접 잔여 영역** |
| Vault HSM (GP-3 C-3) | **Group γ-2** | ❌ 미진입 (양 vendor DEFER to MVP-6 권고) |
| Hermes upstream chmod (C-5b ST-1) | **Group γ-1** | ❌ 미진입 (Backlog #3 §3.4 답습) |
| facade real 본문 P1 v2 (GP-5 C-2) | Backlog #4 (별도 영역) | — 본 brief 영역 외 (Backlog #3 ≠ #4) |

### 2.3 해소 판정 (synthesis — 결정 아님)

- **GP-3 C-3 / GP-5 C-2 의 *완전* 해소** = (i) Group α (AR-2, 발효 完) + (ii) **Group β (Tier-2/3 catalog/vendor 확장 정책)** 풀 3+1 발효 의무. → 즉 **Group β 가 두 condition 의 *핵심 잔여* 매듭**.
- Group γ-1 (Hermes upstream chmod) 는 GP-3 C-3 의 *Vault HSM* 항목과 별개 (file system perm). Group γ-2 (Vault HSM) 가 GP-3 C-3 의 Vault HSM 항목 직접 대응 — 단 양 vendor = MVP-6 이후 보류 권고.
- 본 §2.3 = synthesis 추정 한정. *해소 선언* = 잔여 풀 3+1 합의 발효 + GP-3 / GP-5 condition row 갱신 합의 + 사용자 명시 (별도 단계).

---

## 3. 잔여 4 sub-영역 진입 정비

### 3.1 Group β — T-5 (β) + Tier-2/3 catalog 일반

| 영역 | 정비 |
|---|---|
| 책무 | catalog source 정책 (GP-3 R-4.1 42 + GP-5 URL 10 / Model 19 → Tier-2/3 확장 정책 일반 + provider URL/model Tier-2/3 vendor subset) |
| T3 진입 속성 | catalog 본문/정책 변경 ✅ HIGH / Provider Liquidity 5-way ⚠️ HIGH / FP 폭증 ⚠️ HIGH / Implementation Evidence PASS 의존 ⚠️ HIGH |
| 5 영구 핵심 제약 영향 | 단일 source-of-truth ⚠️ HIGH (catalog 형식 분리 / 자동 동기화 시) + Provider Liquidity 5-way ⚠️ HIGH (Tier-2/3 차단 강화 = 신규 vendor 채택 부담 ↑ *역효과*) |
| 외부 LLM 수렴 (입력) | 양 vendor (C) PARTIAL — **정책/schema/audit-only 진입 가능 + Tier-2/3 hard-block = Implementation Evidence PASS 후** (§4 답습) |
| 진입 적합성 (synthesis) | 정책 frame 합의는 진입 가능 / hard-block 확장 = Evidence PASS 의존 → **진입 시 audit-first 정책 + schema 한정 권고** (수단 *결정* 은 풀 3+1) |
| GP-3 C-3 / GP-5 C-2 직결 | ✅ **핵심 잔여 매듭** (§2.2) |

### 3.2 Group γ-1 — C-5b ST-1 (Hermes upstream Dockerfile chmod 600 강제)

| 영역 | 정비 |
|---|---|
| 책무 | secret source / Hermes upstream (file system perm) |
| T3 진입 속성 | Hermes upstream 본문 변경 ✅ HIGH / **Hermes ≠ root of trust 검토 의무** ✅ HIGH (5 영구 핵심 제약 #1) |
| 5 영구 핵심 제약 영향 | Hermes ≠ root of trust ✅ HIGH (Hermes 자기 검증 = root of trust 침범 위험) + 수단-목적 분리 ⚠️ HIGH |
| 외부 LLM 수렴 (입력) | 양 vendor APPROVE WITH CONDITIONS — **upstream 직접 수정 *전* downstream wrapper / entrypoint preflight / CI container test 형태 검증 권고 + dev=warn / CI=fail-closed 분리 + "Hermes 자기 검증으로 안전" 금지** (§4 답습) |
| 진입 적합성 (synthesis) | downstream preflight 형태 진입 가능 / Hermes upstream PR = evidence 확보 후 + PMO 격상과 자동 연결 금지 |
| GP-3 C-3 직결 | 부분 (Vault HSM 항목과 별개 file system perm) |

### 3.3 Group γ-2 — Vault HSM ST-4 (ADR-010 통합)

| 영역 | 정비 |
|---|---|
| 책무 | secret source (외부 HSM) / Multi-host 인프라 |
| T3 진입 속성 | ADR-010 §X 진입 ✅ HIGH / Multi-host 인프라 ✅ HIGH / 운영 비용 高 ⚠️ HIGH / Operational Readiness (MVP-6) 경계 ⚠️ HIGH / Hermes PMO 격상 경계 ⚠️ HIGH |
| 5 영구 핵심 제약 영향 | 단일 source-of-truth ⚠️ MEDIUM (HSM 단일화 시 ↑) |
| 외부 LLM 수렴 (입력) | 양 vendor **BLOCK / DEFER to MVP-6** — single-host SPOF 의도적 수용 (ADR-012 §2.8) 상태에서 HSM 실효성 낮음 + 운영 비용 高 + Operational Readiness PASS 선행 (§4 답습) |
| 진입 적합성 (synthesis) | **현 시점 실 진입 부적합** — ADR-010 참조 유지 + 구현 진입 금지 + MVP-6 Operational Readiness / Multi-host 전환 시점 재검토 |
| GP-3 C-3 직결 | Vault HSM 항목 직접 대응 (단, MVP-6 이후 보류 권고) |

### 3.4 잔여 4 sub-영역 진입 적합성 합산 (synthesis — 결정 아님)

| 진입 단위 | 외부 LLM 수렴 | 현 시점 진입 적합성 (synthesis) |
|---|---|---|
| Group β | (C) PARTIAL | 정책/schema/audit-first 진입 *가능* / hard-block = Evidence PASS 의존 |
| Group γ-1 | APPROVE WITH CONDITIONS | downstream preflight 형태 진입 *가능* / upstream PR = evidence 후 |
| Group γ-2 | BLOCK / DEFER | 현 시점 실 진입 *부적합* — MVP-6 보류 확정이 핵심 의제 |

---

## 4. 외부 LLM 응답 2건 synthesis (입력 한정 — 결론 강제 채택 0건)

### 4.1 잔여 그룹 판정 정합 매트릭스

| 영역 | Gemini 3 Flash | GPT-5.5 Thinking | 수렴 |
|---|---|---|---|
| **종합 (Q19)** | (C) PARTIAL — α+β 진입 / γ 보류 | (C) PARTIAL — α 우선 / β audit / γ ST-1·ST-4 분리 | ✅ **(C) PARTIAL** |
| Group β catalog 형식 | YAML 자체 catalog + 수동 트리거 | 별도 yaml/json manifest + provenance/fixture/allowlist | ✅ 자체 manifest + 수동 |
| Group β Tier-2 범위 | Tier-2 확장 (Mistral/AI21/HuggingFace) / Tier-3 보류 | Tier-2 hard-block 0건 (audit-only 등록) / 후보 기준 제시 | ⚠️ 차이 — Gemini=Tier-2 확장 / GPT=audit-only 우선 |
| Group β LiteLLM 자동 동기화 | 자체 catalog (LiteLLM 참조용) | BLOCK auto-sync / advisory snapshot | ✅ 자체 source-of-truth + 외부=참조 |
| Group β lock-in 역효과 | 실재 HIGH — Sandboxed Tier 완화 | 실재 HIGH — allowlist/expiry/adapter stub 완화 | ✅ 실재 HIGH + 완화책 필요 |
| Group β Evidence 의존 | Implementation Evidence PASS 후 hard-block | Implementation Evidence PASS 후 hard-block | ✅ Evidence PASS 선행 |
| Group γ-1 ST-1 | entrypoint chmod 검증 + Dockerfile layer 추가 대안 | downstream wrapper/preflight/CI test + dev=warn/CI=fail-closed | ✅ downstream 검증 우선 |
| Group γ-2 ST-4 | 현 시점 보류 (MVP-6 이후) | BLOCK until MVP-6 | ✅ MVP-6 보류 |
| Group γ 묶음 | 3그룹 분리 적절 | γ-1/γ-2 분리 권고 (위험 규모 다름) | ⚠️ GPT γ 추가 분리 권고 |

### 4.2 외부 LLM 이 지적한 prep brief 결함 / 누락 (풀 3+1 흡수 후보)

| # | 출처 | 결함 / 누락 |
|---|---|---|
| 1 | 양 vendor | **FP 복구 / 비상 탈출구 정책** — Group β 오탐으로 핵심 vendor 접근 차단 시 bypass (ADR-011 위반 없이) 정의 필요 |
| 2 | Gemini | **AI agent 권한 위임** — bot 계정/App 권한 범위 + 서명 방식 (Group α C-10 부분 답습) |
| 3 | GPT | **Tier-2/3 예외 경로** — allowlist / expiry exception / adapter stub 생성 경로 필수 (Provider Liquidity 보존) |
| 4 | GPT | **Group γ 과도 묶음** — ST-1/ST-4 위험 규모 다름 → 별도 합의 단위 (본 brief §1.1 흡수) |
| 5 | GPT | **Operational Readiness 1인 개발자 정의** — enterprise HA 아닌 rotation/backup/restore/audit/fallback 기준 |

> 본 §4 = 외부 LLM 응답 *입력 한정 정리*. 어떤 판정도 *강제 채택* 0건 — 잔여 풀 3+1 합의 시 Agent A/B/C 의 독립 평가 대상.

---

## 5. T3 영역 = 풀 3+1 *의무* 영역 (Reviewer-only 단축 *부적격*)

### 5.1 의무 근거 (영구 답습)

- **CLAUDE.md §3 적용 기준**: "보안 관련 변경 = 3+1 (필수) — 보안은 다중 검증 필수". Backlog #3 T3 영역 = enforcement / secret source / catalog 차단 정책 = **보안 enforcement 영역** → 풀 3+1 (Agent A + Agent B + Agent C + Reviewer) 의무.
- **ADR-011 §2.4**: T3 영역 = 풀 3+1 + 외부 LLM 1+ cross-vendor blind + 사용자 명시 *의무*.
- **GP-3 C-3 / GP-5 C-2 원문**: "T3 영역 *별도 풀 3+1*" 명시 (§2.1).
- **선례**: Group α (동일 Backlog #3 T3 영역) = 풀 3+1 (Agent A/B/C + Reviewer) 가동 — 잔여 그룹도 동일 형식 의무.

### 5.2 풀 3+1 의무 발화 트리거 (의뢰서 §6.1 7/7 매트릭스 잔여 그룹 답습)

| # | 트리거 | 잔여 그룹 발화 |
|---|---|---|
| 2 | **T3 영역 자동 진입** | ✅ **HIGH (BLOCKING)** — Group β / γ-1 / γ-2 *모두* T3 영역 |
| 4 | Provider Liquidity 5-way 약화 | ⚠️ HIGH — Group β (Tier-2/3 차단 강화 역효과) / γ-2 (Vault HSM) |
| 5 | 5 영구 핵심 제약 약화 | ⚠️ **HIGH** — γ-1 (Hermes ≠ root of trust) / β (단일 source-of-truth) / γ-2 (단일 source-of-truth) |
| 7 | **외부 LLM cross-vendor blind 없는 T3 결정** | ✅ HIGH — 단, 응답 2건 (Gemini + GPT) 이미 회수 完 → 풀 3+1 *입력* 으로 답습 |

**합산**: 트리거 #2 (BLOCKING) + #5 (HIGH) 발화 → **잔여 3 진입 단위 모두 풀 3+1 의무 확정. Reviewer-only 단축 합의 부적격.**

### 5.3 Group γ-2 (Vault HSM "MVP-6 보류 확정") 의 합의 형태 주의

> Group α 합의 §8 옵션 (H) 는 Group γ-2 를 "Reviewer-only 단축 합의 적격 여부 *검토*" 로 표기. **단, 본 brief 는 사용자 명시 (2026-05-20) 답습 — T3 영역 = 풀 3+1 의무 영역.** Vault HSM 의 "MVP-6 보류 확정" 도 (a) Vault HSM = T3 영역 + (b) ADR-010 §X 진입 경계 + (c) Operational Readiness / Hermes PMO 격상 경계가 걸린 *T3 정책 결정* → **풀 3+1 의무**. "보류 확정 = 수단 결정 0건이므로 단축 적격" 여부 자체도 *풀 3+1 안에서* 판정할 사항 (사전 단축 추정 금지).

---

## 6. 잔여 그룹 권고 진입 순서 / 그룹화 (synthesis — 결정 아님)

### 6.1 진입 순서 후보

| 순위 후보 | 근거 (synthesis) |
|---|---|
| **1순위 = Group β** | GP-3 C-3 / GP-5 C-2 *핵심 잔여 매듭* (§2.3) + 외부 LLM 정책/schema/audit-first 진입 가능 수렴 + Group α 합의 §8 옵션 (F) |
| **2순위 = Group γ-1** | downstream preflight 진입 가능 + Hermes ≠ root of trust 검토 의무 (5 영구 핵심 제약 #1) + Group α 합의 §8 옵션 (G) |
| **3순위 = Group γ-2** | 외부 LLM 양 vendor BLOCK/DEFER to MVP-6 수렴 → "MVP-6 보류 확정" 풀 3+1 (현 실 진입 부적합) + Group α 합의 §8 옵션 (H) |

### 6.2 그룹화 후보 (사용자 결정 영역)

| 옵션 | 단위 | 합의 부담 |
|---|---|---|
| (I) 잔여 3 단위 *각각* 분리 (3 풀 3+1) | β / γ-1 / γ-2 분리 | 中 — GPT γ-1/γ-2 분리 권고 정합 (**본 brief 권고 후보**) |
| (II) Group β + γ-1 통합 (2 풀 3+1) | (β+γ-1) / γ-2 | 中 — 책무 영역 다름 (catalog vs Hermes upstream) ⚠️ |
| (III) 잔여 3 단위 *단일 통합* (1 풀 3+1) | β+γ-1+γ-2 | 高 — 위험 규모 비대칭 (GPT 결함 #4) ⚠️ |

> 본 §6 = synthesis 권고 *후보* 한정. *결정* (진입 순서 / 그룹화 / 진입 시점) = 사용자 명시 결정 영역 + 각 단위 풀 3+1.

---

## 7. Rollback Trigger / cross-reference

### 7.1 잔여 그룹 풀 3+1 진입 Rollback Trigger (답습)

| Trigger | 진입 단위 | 발화 조건 | 발화 시 행동 |
|---|---|---|---|
| **ADR-011 §2.4** | β / γ-1 / γ-2 전체 | T3 영역 진입 결정 | 풀 3+1 + 외부 LLM 1+ (회수 完, 입력 답습) + 사용자 명시 |
| GP-3 §3.5 (Tier-2 확장 필요) | Group β | Tier-2/3 catalog 확장 결정 | 풀 3+1 합의 |
| GP-5 §4.6 (URL Tier-2/3 / branch protection) | Group β | Tier-2/3 vendor 확장 결정 | 풀 3+1 합의 |
| C-5b ST-1 | Group γ-1 | Hermes upstream Dockerfile 변경 결정 | 풀 3+1 + Hermes ≠ root of trust 검토 |
| ADR-010 §X | Group γ-2 | Vault HSM 진입 결정 | 풀 3+1 + 외부 LLM 1+ + Operational Readiness (MVP-6) 경계 |

### 7.2 cross-reference 영역

| 영역 | 답습 |
|---|---|
| **GP-3 C-3 / GP-5 C-2** | 잔여 풀 3+1 발효 + condition row 갱신 합의 시 해소 (별도 단계) |
| **Backlog #6** (Runtime + CI-hook) | Group α C-1 답습 — 실 강제 적용 시점 의존성 (잔여 그룹 실 적용도 동일) |
| **Backlog #1** (ST-2 inotify sidecar) | Group γ-1 ST-1 과 책무 분담 결정 의무 (Defense in depth) |
| **Backlog #4** (P1 v2 facade real 본문) | GP-5 C-2 의 "facade real 본문 P1 v2" 항목 = Backlog #4 영역 (본 brief ≠ #4) |
| **Backlog #7 / MVP-6** (Operational Readiness) | Group γ-2 Vault HSM 진입 시점 경계 |
| **ADR-008 부록 C** (Hermes PMO Activation 12 조건) | Group γ-1 upstream 변경 / γ-2 Vault HSM = PMO 격상 경계 cross-reference |
| **Phase α defer-lockdown** | 별개 트랙 — 본 brief 충돌 0건 / 영향 0건 |

---

## 8. 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

| 옵션 | 영역 | 후속 단계 |
|---|---|---|
| **(A)** | 본 brief 그대로 승인 → **Group β 풀 3+1 합의 진입** (Agent A/B/C + Reviewer, 외부 LLM 응답 입력 답습) | 1순위 잔여 (§6.1) |
| (B) | 본 brief 승인 → **Group γ-1 (C-5b ST-1) 풀 3+1 합의 진입** | 2순위 |
| (C) | 본 brief 승인 → **Group γ-2 (Vault HSM ST-4 MVP-6 보류 확정) 풀 3+1 합의 진입** | 3순위 |
| (D) | 본 brief 일부 수정 요청 → 수정 후 승인 | v2 작성 |
| (E) | 본 brief 승인 → commit (`docs/phase0/backlog3-t3-zone-followup-brief.md`) *까지만* (합의 보류) | 1 commit (사용자 명시 시) |
| (F) | 본 brief 보류 → 세션 종료 | — |

> 본 brief = **brief 단계 한정** (staged cycle: brief → 승인 → 합의 → commit → push). 합의 / commit / push = 사용자 명시 승인 후 별도 단계. T3 영역 합의 = **풀 3+1 의무** (§5).

---

## 9. 한 단락 요약

Backlog #3 T3 영역은 6 sub-영역 → 4 진입 단위 (Group α / β / γ-1 / γ-2) 로 정비되며, Group α (AR-3 + PC-4 T3 sub) 는 2026-05-14 풀 3+1 합의 (3/3 만장일치 APPROVE WITH CONDITIONS) 로 *수단 결정 적격성 권위 권고* 발효 完. 본 follow-up brief 는 잔여 3 진입 단위 (Group β = T-5 β + Tier-2/3 catalog 일반 / γ-1 = C-5b ST-1 Hermes upstream chmod / γ-2 = Vault HSM ST-4) 의 풀 3+1 진입 정비 + GP-3 진입 condition C-3 / GP-5 진입 condition C-2 ("T3 영역 별도 풀 3+1") 미해소 직결 매핑 한정이다. 두 condition 의 *핵심 잔여 매듭* = Group β (Tier-2/3 catalog/vendor 확장 정책). 외부 LLM 응답 2건 (Gemini 3 Flash + GPT-5.5 Thinking, 2026-05-13) 은 잔여 그룹에 대해 (C) PARTIAL 로 수렴 — Group β = 정책/schema/audit-first 진입 가능 (hard-block = Implementation Evidence PASS 후), γ-1 = downstream preflight 진입 가능 (Hermes ≠ root of trust 보존), γ-2 = MVP-6 이후 BLOCK/DEFER (single-host SPOF 의도적 수용 + 운영 비용 高). 권고 진입 순서 후보 = β → γ-1 → γ-2 (synthesis 한정, 결정 아님). **T3 영역 = 보안 enforcement → 풀 3+1 (Agent A/B/C + Reviewer) 의무 영역이며 Reviewer-only 단축 합의는 부적격** (Vault HSM "MVP-6 보류 확정" 도 T3 정책 결정 → 풀 3+1 의무). 본 brief 는 synthesis + 진입 정비 DRAFT 한정 — 수단 결정 / threshold 고정 / 합의 보고서 작성 / commit / push / 실 진입 / Tier-2/3 catalog 확장 / Hermes upstream 변경 / Vault HSM 구현 / branch protection 실 변경 / Operational Readiness PASS / Hermes PMO 격상 / MVP-1 exit 발효 / actual run 재실행 / CI workflow 변경 / Phase α defer-lockdown 변경 / 외부 LLM 응답 강제 채택 모두 0건이며, 모든 *결정* 은 별도 풀 3+1 합의 (사용자 명시 승인 후).

---

## 부록 A — 본 brief 답습 출처

| 출처 | 답습 영역 |
|---|---|
| `3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md` | Group α 합의 (657줄) — §8 옵션 F/G/H 잔여 진입 후보 + γ-1/γ-2 분리 표기 |
| `2026-05-13-backlog3-t3-zone-review-response-gemini.md` | Gemini 응답 (19 질문, (C) PARTIAL) — 입력 한정 |
| `2026-05-13-backlog3-t3-zone-review-response-gpt.md` | GPT 응답 (19 질문, (C) PARTIAL + γ 분리 권고) — 입력 한정 |
| `2026-05-13-backlog3-t3-zone-review-request.md` | cross-vendor blind 의뢰서 (19 질문 / §6.1 트리거 매트릭스) |
| `3plus1-consensus-2026-05-12-gp3-mvp1-entry.md` | GP-3 진입 C-3 원문 (T3 영역 별도 풀 3+1) |
| `3plus1-consensus-2026-05-12-gp5-mvp1-entry.md` | GP-5 진입 C-2 원문 (T3 영역 별도 풀 3+1) |
| prep brief 계보 `ad9a02d` / `2a9d02d` / `db0e3ac` | 6 sub-영역 정의 + 그룹화 + 위험 매트릭스 (본문 변경 0건) |

## 부록 B — 금지 사항 (사용자 명시 영구 답습)

본 brief 의 어떤 §도 그 자체로 다음을 발생시키지 않는다:
풀 3+1 합의 보고서 작성 / commit / push / 수단 결정 / threshold 고정 / Tier-2/3 catalog 본문 확장 / Hermes upstream Dockerfile 변경 / Vault HSM 구현 / ADR-010 §X 본문 변경 / branch protection rule 실 변경 / dev 환경 실 강제 / Operational Readiness PASS (Layer E) 선언 / Hermes PMO 격상 (Layer F) 선언 / MVP-1 exit 발효 / MVP-2 자동 진입 / actual run 재실행 / CI workflow 변경 / workflow_dispatch 추가 / paths 필터 변경 / Phase α defer-lockdown 변경 / 외부 LLM 응답 결론 강제 채택 / 외부 LLM 추가 자동 호출 / ADR 본문 자동 갱신 / Group α 합의·prep brief 계보 본문 변경 / GP-3 C-3·GP-5 C-2 해소 선언 / 5 영구 핵심 제약·Provider Liquidity 5-way 약화 / 본 brief 자체의 합의 자동 진입.
