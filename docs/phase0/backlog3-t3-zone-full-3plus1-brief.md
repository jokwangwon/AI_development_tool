# Backlog #3 T3 영역 풀 3+1 합의 *준비* Brief (DRAFT)

> **본 brief = Backlog #3 (T3 영역) 풀 3+1 합의 *진입 전* 정비를 위한 *준비안* (DRAFT)** — 6 sub-영역 (AR-3 / T-5 (β) / PC-4 T3 sub / C-5b ST-1 / Vault HSM ST-4 / Tier-2-3 catalog 자동 확장 *가능성*) 의 *진입 적격성*, *합의 단위*, *합의 형태*, *Agent 관점 분배*, *외부 LLM cross-vendor 의뢰 형식*, *우선순위*, *차단 요인*, *후속 단계 권고* 를 *합의 *직전* 의사결정 입력* 으로 정비한다.
>
> 본 brief 의 어떤 §도 그 자체로 (i) **실제 T3 영역 진입**, (ii) **branch protection rule 변경** (CODEOWNERS / required check / commit signing 등), (iii) **dev 환경 강제** (`pre-commit install` 의무화 / 개발자 환경 정책), (iv) **Hermes upstream Dockerfile 변경** (entrypoint stat / chmod 강제 / inotify 본문 흡수), (v) **Vault HSM 구현** (실 Vault 클라이언트 / 실 HSM 환경 / ADR-010 본문 변경), (vi) **Operational Readiness PASS (Layer E) 선언**, (vii) **Hermes PMO 격상 (Layer F) 선언**, (viii) Tier-2 / Tier-3 catalog *본문 확장* (URL 10 → 20+ / Model 19 → 50+ / R-4.1 42 catalog → 확장), (ix) 풀 3+1 합의 보고서 *작성* / commit / push, (x) 외부 LLM *자동 호출*, (xi) 실 API key / provider SDK / 외부 API 호출, (xii) ADR 본문 자동 갱신 (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012), (xiii) §C-5 / §C-5b / §C-5c / §C-6 상태 표기 *재변경*, (xiv) Layer D 합의 보고서 (`210c98f`) 본문 변경, (xv) §5.5 9 sub-수단 본문 채택 변경, (xvi) Backlog #1 / #2 / #4 / #6 / #7 자동 진입 을 발생시키지 않는다.

**작성일**: 2026-05-14 후속 7
**상태**: DRAFT (사용자 명시 승인 *전*, 파일화 + commit 0건)
**상위 권위**:
- Backlog #2 *잔여 5 항목* Deferred 유지 합의 = `8ba5182 docs(review): defer Backlog 2 GP-5 remaining items` (Reviewer-only 단축 합의 APPROVE — AR-3 + T-5 (β) Backlog #3 이관 명시)
- Backlog #2 *잔여 5 항목* brief = `59adef3 docs(phase0): add Backlog 2 GP-5 remaining items brief`
- PC-4 T2 sub Partially Satisfied 합의 = `78483c5 docs(review): approve PC-4 T2 C-5c C-6 partial satisfaction` (C-5b ST-1 / PC-4 T3 sub / GP-5 1.5차 나머지 Deferred 유지)
- MVP-1 Implementation Entry = `1eab814 docs(review): approve MVP-1 implementation entry` (READY, Backlog 우선순위 1 = #6 Runtime+CI-hook)
- Backlog #6 Implementation Entry 합의 (Layer B) = `f40423f` (9 sub-수단 본문 채택 — Backlog #3 T3 영역 분리 명시)
- MVP-1 roadmap deepening = `cddd22f` + `bbc05ca` + `5939c93` (mvp1.md §3.3 ST-1~ST-5 + §4.4 AR-1~AR-3 + §4.6 R-MVP1-G3-7~8 + R-MVP1-G5-7~9 + §5.5)
- ADR-010 (Vault HSM 권위 본문) — 진입 시점 = Operational Readiness 영역 / Multi-host 환경 권고
- ADR-011 §2.4 T3 영역 분리 (정책 / branch protection / Vault HSM / Tier-2/3 catalog 확장 = T3 영역 답습)
- ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 (entrypoint stat) + §2.6.2 R2-1 (docker secret) + R-4 catalog (R-4.1 Tier-1 42 patterns)
- 5 영구 핵심 제약 (Hermes ≠ root of trust / 수단-목적 분리 / 메타포 강제 금지 / 단일 source-of-truth / Provider Liquidity)

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습 (2026-05-14 후속 7)

> "Backlog #3 T3 영역 풀 3+1 brief를 작성해주세요. 범위는 AR-3, T-5 β, PC-4 T3 sub, C-5b ST-1, Vault HSM ST-4, Tier-2/3 catalog 자동 확장 가능성을 통합 검토하는 것입니다. 단, 실제 T3 진입, branch protection 변경, dev 환경 강제, Hermes upstream 변경, Vault HSM 구현, Operational Readiness PASS, Hermes PMO 격상은 하지 마세요."

### 0.2 본 brief 가 *하는* 것

1. Backlog #3 T3 영역 정의 (§1) — 다른 6 backlog 와 책무 경계 + Layer B `f40423f` 분리 명시 답습
2. 6 sub-영역 정의 + T3 진입 속성 매트릭스 (§2)
   - §2.1: AR-3 (AR-1 + AR-2 통합 — branch protection rule)
   - §2.2: T-5 (β) (provider URL/model name Tier-2/3 catalog 확장 — GP-5 specific)
   - §2.3: PC-4 T3 sub (`pre-commit install` 의무화 + dev 환경 강제)
   - §2.4: C-5b ST-1 (Hermes upstream Dockerfile entrypoint stat chmod 600 강제)
   - §2.5: Vault HSM ST-4 (ADR-010 통합)
   - §2.6: Tier-2/3 catalog 자동 확장 *가능성 일반* (GP-3 R-4.1 + GP-5 Provider catalog 통합)
3. 6 sub-영역 *결합 위험* / *책무 중첩* / *분리 가능성* 매트릭스 (§3)
4. 합의 *단위* 권고 — 6 단일 bundled vs 책무 기반 N 분리 (§4.1)
5. 합의 *형태* 권고 — 풀 3+1 + 외부 LLM 1+ + 사용자 명시 (T3 영역 의무) (§4.2)
6. 풀 3+1 Agent A / B / C 관점 분배 권고 (§5)
7. 외부 LLM cross-vendor blind 의뢰 형식 + 의뢰 핵심 질문 권고 (§6)
8. Rollback Trigger 통합 매트릭스 (R-MVP1-G3-7/8 + R-MVP1-G5-7/8/9 + ADR-010 답습) (§7)
9. 7/7 풀 3+1 승격 트리거 *재검증* — 모두 발화 (§8) — 본 6 영역 *전체* = T3 영역 의무
10. 우선순위 권고 + 차단 요인 (§9)
11. 메타 검증 (§10)
12. 요약 한 단락 (§11)
13. 다음 단계 결정 옵션 (부록 A)
14. 금지 사항 (부록 B) — 사용자 명시 7 금지 + 추가 답습

### 0.3 본 brief 가 *하지 않는* 것 (사용자 명시 7 금지 + 추가)

| # | 금지 | 본 brief 위반 |
|---|------|------------|
| 1 | **실제 T3 영역 진입** | 0건 (본 brief = 합의 *준비안* — 합의 자체 0건 + commit 0건) |
| 2 | **branch protection rule 변경** (CODEOWNERS / required check / commit signing / merge restriction) | 0건 (AR-3 = 검토 영역, GitHub repo 정책 자동 변경 0건) |
| 3 | **dev 환경 강제** (`pre-commit install` 의무화 / `.git/hooks` 자동 install / 개발자 환경 정책) | 0건 (PC-4 T3 sub = 검토 영역) |
| 4 | **Hermes upstream Dockerfile 변경** (entrypoint stat / chmod 강제 / inotify 본문 흡수 / 실 image 빌드) | 0건 (C-5b ST-1 = 검토 영역, Hermes upstream PR 0건) |
| 5 | **Vault HSM 구현** (실 Vault 클라이언트 통합 / 실 HSM 환경 / ADR-010 §X 본문 변경 / 실 secret 이전) | 0건 (ST-4 = 검토 영역) |
| 6 | **Operational Readiness PASS (Layer E) 선언** | 0건 (MVP-6 + Backlog #7 별도 영역) |
| 7 | **Hermes PMO 격상 (Layer F) 선언** | 0건 (MVP-6 + 외부 LLM 2 또는 1+사람 리뷰 의무) |
| (추가) | **Tier-2 / Tier-3 catalog *본문 확장*** (URL 10 / Model 19 / R-4.1 42 보존) | 0건 (확장 *가능성* 검토 한정, 본문 *변경* 0건) |
| (추가) | T3 sub-영역 *수단 결정* / *도입* / *본문 채택 commit* | 0건 (본 brief = 검토 준비안) |
| (추가) | 풀 3+1 합의 보고서 *작성* / commit / push | 0건 (합의 = 별도 단계, 사용자 명시 후속) |
| (추가) | 외부 LLM *자동 호출* / cross-vendor blind 의뢰 자동 발송 | 0건 (의뢰 형식 *권고 한정*) |
| (추가) | 실 API key / provider SDK / 외부 API 호출 / 실 secret 처리 | 0건 |
| (추가) | ADR 본문 자동 갱신 (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012) | 0건 |
| (추가) | §C-5 / §C-5b / §C-5c / §C-6 상태 표기 *재변경* | 0건 (`78483c5` + `8ba5182` 권위 source 보존) |
| (추가) | Layer D 합의 보고서 (`210c98f`) 본문 변경 | 0건 (A-1 답습) |
| (추가) | §5.5 9 sub-수단 본문 채택 변경 | 0건 (Layer B `f40423f` 그대로 유지) |
| (추가) | `tools/secret_scanner.py` / `tools/provider_*.py` 본문 변경 | 0건 |
| (추가) | `.importlinter` / `.pre-commit-config.yaml` 본문 변경 / 신규 hook 추가 | 0건 |
| (추가) | CI workflow 변경 (secret-hygiene-egress-redaction.yml / provider-adapter-enforcement.yml / etc.) | 0건 |
| (추가) | Production `docker-compose.yml` / Hermes upstream Dockerfile / requirements*.txt 변경 | 0건 |
| (추가) | Backlog #1 (GP-3 1.5차) / #2 (GP-5 1.5차) / #4 (P1 v2 facade MVP) / #6 (Runtime+CI-hook) / #7 (Operational Readiness) 자동 진입 | 0건 |
| (추가) | MVP-1 PASS *재선언* | 0건 (Layer D `210c98f` APPROVE WITH CONDITIONS 그대로 유지) |
| (추가) | MVP-2 자동 진입 | 0건 (MVP-1 Implementation Evidence PASS 미발효 + 사용자 명시 후속) |
| (추가) | 5 영구 핵심 제약 약화 / Provider Liquidity 5-way 약화 | 0건 |
| (추가) | 사용자 명시 3 결정 (α/ii/(가)) *재변경* | 0건 (PC-4 T2 sub Cycle 4 답습 한정) |

### 0.4 본 brief 의 권위 한계

본 brief = **DRAFT — 준비안 한정**. 본 brief 가 발생시키는 *유일한* 효과 = **Backlog #3 T3 영역 풀 3+1 합의 *진입 직전* 의사결정 입력 정비** — (i) 6 sub-영역 *경계 명시*, (ii) *결합 위험* / *분리 가능성* 매트릭스, (iii) *합의 단위 / 형태 / Agent 관점 / 외부 LLM 의뢰 형식 권고*. *합의 발효* / *수단 결정* / *본문 채택* / *T3 영역 진입* / *Tier-2/3 catalog 본문 확장* / *Hermes upstream 변경* / *Vault HSM 구현* / *branch protection rule 변경* / *dev 환경 강제* 모두 0건.

---

## 1. Backlog #3 T3 영역 정의

### 1.1 7 backlog 중 본 brief 의 위치 (Layer B `f40423f` + Layer D `210c98f` 답습)

| Backlog # | 영역 | 본 brief 와 관계 |
|---------|------|---------------|
| #1 | GP-3 1.5차 보강 (S-3 detect-secrets 부분 / ST-2 inotify sidecar) | 별도 영역 (Backlog #1 brief 답습 분리) |
| #2 | GP-5 1.5차 보강 (T-1/T-3/T-4 단독 + T-5 강화 + AR-3 + PC-4 T2 sub) | PC-4 T2 sub 처리됨 (`78483c5`) + 잔여 5 Deferred (`8ba5182`) — AR-3 + T-5 (β) **본 brief 이관** |
| **#3** | **T3 영역 — AR-2 / Vault HSM / Tier-2/3 / PC-4 T3 sub / C-5b ST-1** | ✅ **본 brief 영역** (6 sub-영역) |
| #4 | P1 v2 facade MVP (G5-4 — `src/adapters/llm/facade.py` LiteLLM 실 import) | 별도 영역 (Group A 2차 §8 TR-1 답습) |
| #5 | ADR-012 §2.2 `event` enum 정식 등록 | 별도 합의 영역 (G4 §10.2 schema 진화 답습) |
| #6 | Runtime enforcement / CI-hook implementation | MVP-1 Implementation Entry 우선순위 1 (`1eab814` 답습) |
| #7 | Operational Readiness parity check | MVP-6 영역 — Backlog #3 ST-4 진입 시 부분 cross-reference |

### 1.2 Backlog #3 T3 영역 본 brief 의 *대상* 6 sub-영역

| sub-영역 | mvp1.md 출처 | T3 진입 속성 | 본 brief § |
|--------|----------|-----------|----------|
| **(1) AR-3** (AR-1 + AR-2 통합) | §4.4 row AR-3 + §4.7.3 line 480 ("AR-2 / AR-3 진입 = 풀 3+1 + 외부 LLM 1+ + 사용자 명시") | branch protection rule 변경 (T3) | §2.1 |
| **(2) T-5 (β)** (provider URL/model name Tier-2/3 catalog 확장) | §4.3 row T-5 + §4.6 R-MVP1-G5-7 + R-MVP1-G5-8 (URL/Model Tier-2/Tier-3 추가 결정 = 풀 3+1 + Tier-2/3 catalog 확장 결정) | catalog 본문 확장 (T3) — `78483c5` 답습 (catalog 자동 확장 0건) | §2.2 |
| **(3) PC-4 T3 sub** (`pre-commit install` 의무화 + dev 환경 강제) | §4.3 row PC-4 + §4.4.2 권고 (PC-4 MVP-1 1.5차 보강 영역) + ADR-011 §2.4 (dev 환경 강제 = T3) | dev 환경 정책 / `default_install_hook_types` / `fail_fast` (T3) | §2.3 |
| **(4) C-5b ST-1** (Hermes upstream Dockerfile entrypoint stat chmod 600 강제) | §3.3 row ST-1 + §3.5 R-MVP1-G3-7 (Hermes upstream Dockerfile 변경 = 풀 3+1 + Hermes upstream PR 검토) + ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 답습 | Hermes upstream Dockerfile (T3) — repo 책무 경계 변경 | §2.4 |
| **(5) Vault HSM ST-4** (ADR-010 통합) | §3.3 row ST-4 + §3.5 R-MVP1-G3-8 (Vault HSM 도입 = ADR-010 §X 진입 + Multi-host 인프라) + line 291 ("ST-4 진입 = ADR-010 §X + 외부 LLM 1+ + T3 영역 + Multi-host") | ADR-010 §X 진입 + Multi-host 인프라 (T3) | §2.5 |
| **(6) Tier-2/3 catalog 자동 확장 *가능성* 일반** | GP-3 R-4.1 Tier-1 42 + GP-5 URL Tier-1 10 + Model Tier-1 19 → Tier-2/3 일반 정책 | catalog *정책* 변경 (T3) — Group D §2.1 (D) 답습 (catalog 변경 = 풀 3+1 trigger #4) | §2.6 |

### 1.3 본 brief 의 *대상 외* (이미 처리 / 분리 영역)

| 영역 | 처리 위치 | 이유 |
|------|--------|-----|
| **PC-4 T2 sub** | ✅ 이미 처리 — `78483c5` Partially Satisfied (PC-4 T2 sub only) | Backlog #1 + Backlog #2 답습 (`3d3cd21` + `b2f99f4`) |
| **T-1 / T-3 / T-4 단독** | Backlog #2 *잔여* `8ba5182` Deferred 유지 확정 | Backlog #2 영역 (T2 도구 단독 진입 — R-MVP1-G5-1 발화 시) |
| **T-5 (α)** (자체 transitive 분석 추가) | Backlog #2 *잔여* `8ba5182` Deferred 유지 (T-2 와 책무 중복) | T2 영역 (Layer 1 정적 도구) |
| **T-5 (γ)** (실 운영 FN evidence 기반 추가 패턴) | Implementation Evidence PASS 후 별도 합의 | Implementation Evidence PASS 의존 |
| **AR-1 단독** | Layer B `f40423f` 본문 채택 답습 (GP-3 + GP-5 일관성) | T2 영역 (CI step fail-closed) — `8ba5182` 답습 |
| **ST-2 inotify sidecar** | Backlog #1 1.5차 보강 별도 영역 | Hermes upstream 변경 0건 (sidecar 분리 가능) |
| **ST-3 docker secret** | Layer B `f40423f` 본문 채택 답습 | T2 영역 (docker-compose.yml 수준) |
| **ST-5 (ST-1 + ST-2 + ST-3 통합)** | MVP-2 이후 Defense in depth 영역 | C-5b ST-1 본 brief 처리 후 별도 단계 |
| **P1 v2 facade real 본문** (G5-4) | Backlog #4 별도 영역 | Group A 2차 §8 TR-1 답습 |
| **Layer 2 runtime block** (G5-5) | MVP-3 분리 영역 | MVP-1 영역 외 |
| **의미적 lock-in** (G4 §4.6) | MVP-3 분리 영역 | 라운드트립 영역 |
| **Multi-host parity check** | Backlog #7 (Operational Readiness PASS Layer E) | ST-4 Vault HSM 진입 시 부분 cross-reference 한정 |

---

## 2. 6 sub-영역 검토

### 2.1 AR-3 (AR-1 + AR-2 통합 — branch protection rule 변경)

#### 2.1.1 정의 + 출처

| 영역 | 답습 |
|------|------|
| 정의 | AR-1 (CI step fail-closed — 현 PoC + Layer B 채택) + AR-2 (GitHub branch protection rule 강제 — CODEOWNERS / required check / commit signing / merge restriction) 통합 |
| mvp1.md §4.4.1 row | AR-3 = T2 + T3 / 우회 차단 강화 / 본 문서 신규 후보 |
| mvp1.md §4.4.2 권고 | "MVP-1 1.5차 (보강) = AR-3 (AR-1 + AR-2 통합) — T3 영역 진입 + branch protection rule 변경 + 사용자 명시 결정. 사유: Hermes-originated commit auto-reject (G3 §2.2 #20 답습) 와 통합 시 AR-2 단계적 진입 권고" |
| mvp1.md §4.6 R-MVP1-G5-9 | "branch protection rule 변경 결정 (AR-2 진입) — T3 영역 + 풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시" |
| mvp1.md §4.7.3 line 480 | "AR-2 / AR-3 진입 (branch protection rule 변경) = 풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시 — T3 영역" |
| Backlog #2 답습 (`8ba5182`) | AR-3 = Backlog #3 이관 명시 (T3 영역 진입 BLOCKING) |

#### 2.1.2 T3 진입 속성 매트릭스

| 속성 | 발화 |
|----|------|
| GitHub repo 정책 변경 (branch protection / CODEOWNERS / required check) | ✅ HIGH |
| 사용자 명시 결정 의무 (T3 영역 답습) | ✅ HIGH |
| 외부 LLM 1+ cross-vendor blind 의무 (Provider Liquidity 답습) | ✅ HIGH |
| 풀 3+1 합의 의무 (R-MVP1-G5-9 답습) | ✅ HIGH |
| Hermes upstream 변경 0건 (CI / branch protection = GitHub repo 영역, Hermes container 외) | ❌ (Hermes upstream 0건) |
| 실 PR / 실 commit / 실 push 영향 | ⚠️ 후속 진입 시 (현 brief 영역에서 0건) |

#### 2.1.3 핵심 결정 영역 (풀 3+1 합의 시 결정 항목)

| 결정 | 옵션 후보 |
|----|--------|
| AR-2 본문 형태 | (a) CODEOWNERS only / (b) required status check only / (c) commit signing only / (d) merge restriction only / (e) (a) + (b) 통합 / (f) (a)+(b)+(c) 통합 / (g) (a)+(b)+(c)+(d) 통합 |
| AR-1 + AR-2 통합 형태 | (i) AR-1 + AR-2 (b) only / (ii) AR-1 + AR-2 (e) / (iii) AR-1 + AR-2 (g) (Defense in depth) |
| Hermes-originated commit auto-reject (G3 §2.2 #20 답습) 통합 | (α) 본 AR-3 합의에 포함 / (β) Group I 별도 합의 분리 (현재 권고) |
| commit signing 의무화 시점 | (X) MVP-1 1.5차 진입 시 / (Y) Operational Readiness 발효 시 (MVP-6) / (Z) Hermes PMO 격상 시 (MVP-6 + 외부 LLM 의무) |
| fork PR / external contributor 정책 | (1) `pull_request_target` 도입 (별도 합의 — mvp1.md §5.5.1 G3-7 row 답습) / (2) PR 차단 (T3) / (3) 현 default 정책 유지 (`secrets`= fork PR 차단 답습) |

#### 2.1.4 §2.1 판정

⚠️ **AR-3 = T3 영역 진입 BLOCKING + 풀 3+1 + 외부 LLM 1+ + 사용자 명시 의무 발화**. 본 brief 영역에서 *진입 결정 0건* — 합의 *준비안* 한정. 합의 시 결정 항목 = 5 영역 (§2.1.3) — *현 brief 에서 권고 0건* (Agent A/B/C 독립 분석 영역).

### 2.2 T-5 (β) — provider URL/model name Tier-2/3 catalog 확장 (GP-5)

#### 2.2.1 정의 + 출처

| 영역 | 답습 |
|------|------|
| 정의 | Group A 3차 `tools/provider_url_scanner.py` Tier-1 URL catalog 10 (Anthropic/OpenAI/Azure-OpenAI/Google-AI/Replicate/Perplexity/Cohere/HuggingFace/Together/OpenRouter) 및 Tier-1 Model catalog 19 (Anthropic 5 + OpenAI 5 + Google 3 + Meta 3 + Mistral 3) 를 Tier-2 (베타/소규모 vendor) / Tier-3 (legacy / 비주류 vendor) 까지 확장 |
| Backlog #2 *잔여* (`8ba5182`) | T-5 (β) Backlog #3 이관 명시 (T3 영역) |
| mvp1.md §4.6 R-MVP1-G5-7 | "URL Tier-2 / Tier-3 vendor 추가 결정 — 풀 3+1 합의 + Tier-2/3 catalog 확장 결정" |
| mvp1.md §4.6 R-MVP1-G5-8 | "모델 Tier-2 / Tier-3 vendor 추가 결정 — 풀 3+1 합의 + Tier-2/3 catalog 확장 결정" |
| Group D §2.1 (D) 답습 | "Tier-2/3 catalog 확장 = 풀 3+1 trigger #4 — gitleaks default ruleset Tier-2/3 자동 확장 위험 회피 + Python 환경 정합성 우선" |

#### 2.2.2 T3 진입 속성 매트릭스

| 속성 | 발화 |
|----|------|
| catalog *본문* 변경 (URL 10 / Model 19 → 확장) | ✅ HIGH (T3 정책 답습) |
| Provider Liquidity 5-way 영향 | ⚠️ MEDIUM (Tier-2/3 vendor 추가 시 5-way 책무 영향 — vendor 추가/제거 시점) |
| 풀 3+1 합의 의무 (R-MVP1-G5-7/8 답습) | ✅ HIGH |
| 외부 LLM 1+ cross-vendor blind 의무 | ✅ HIGH (vendor 다양성 검토 — vendor *자체* 가 의뢰 대상이므로 blind 의무) |
| Group A 3차 PoC `tools/provider_url_scanner.py` 본문 변경 0건 (현 brief 영역) | ❌ (본 brief 0건) |
| Tier-2/3 확장 시 FP 폭증 위험 | ⚠️ HIGH (catalog 확장 = pattern 충돌 가능성 ↑) |

#### 2.2.3 핵심 결정 영역 (풀 3+1 합의 시 결정 항목)

| 결정 | 옵션 후보 |
|----|--------|
| Tier 분류 기준 | (a) vendor 시장 점유율 / (b) ADR-009 (자체 Adapter v2.0) C-N 답습 / (c) Provider Liquidity 5-way 답습 / (d) (a)+(b)+(c) 통합 매트릭스 |
| Tier-2 URL catalog 확장 범위 | (i) 5 vendor 추가 (예: Mistral / AI21 / Inflection / Aleph Alpha / Stability) / (ii) 10 vendor 추가 / (iii) 0건 (Tier-1 보존 + Tier-3 만 분리) |
| Tier-3 URL catalog | (X) legacy / deprecated vendor 분리 / (Y) Tier-2 와 통합 / (Z) Tier-3 도입 보류 |
| Model Tier-2 catalog | (1) vendor 별 5 모델 추가 / (2) Provider Liquidity 5-way 답습 5 vendor × 3 모델 = 15 추가 / (3) 본 brief 결정 보류 |
| catalog 본문 *형식* | (α) `tools/provider_url_scanner.py` 내장 / (β) `provider_catalog.yaml` 분리 / (γ) `provider_catalog.json` 분리 (canonical_json 답습) |
| FP 폭증 mitigation | (M-1) extension allowlist 확장 / (M-2) comment line 회피 강화 / (M-3) Tier 별 별도 step 분리 |

#### 2.2.4 §2.2 판정

⚠️ **T-5 (β) = T3 영역 진입 + 풀 3+1 + 외부 LLM 1+ + 사용자 명시 의무 발화**. 본 brief 영역에서 *진입 결정 0건* + *catalog 본문 변경 0건*. 합의 시 결정 항목 = 6 영역 (§2.2.3). **AR-3 와 cross-reference 가능성** = 책무 영역 분리 (AR-3 = enforcement layer, T-5 (β) = scanner catalog 영역) — 합의 단위 분리 또는 통합 결정 = §3 + §4.1 권고 영역.

### 2.3 PC-4 T3 sub — `pre-commit install` 의무화 + dev 환경 강제

#### 2.3.1 정의 + 출처

| 영역 | 답습 |
|------|------|
| 정의 | PC-4 (PC-1 + PC-3 병행 — Defense in depth) 中 T3 sub = `pre-commit install` 의무화 / `default_install_hook_types` / `fail_fast` / dev 환경 강제 / `commit-msg` / `pre-push` stage 도입 |
| `78483c5` 답습 | "PC-4 T3 sub (`pre-commit install` 의무화 / dev 환경 강제) = ⏳ Deferred (Backlog #3 T3 영역)" |
| mvp1.md §4.3.1 PC-1 row | "pre-commit framework (`.pre-commit-config.yaml` + `pre-commit install`) — dev 환경 자동 설치 + framework 도입 + dev 환경 강제 — T2 (정책 영역, ADR-011 §2.4 답습)" |
| mvp1.md §4.4.2 line 380 | "MVP-1 1.5차 (보강) = PC-4 (PC-1 + PC-3 병행) — dev 환경 강제 추가 시 Defense in depth" |
| ADR-011 §2.4 답습 | "dev 환경 강제 정책 = T3 영역" |
| Cycle 4 답습 (`b2f99f4` + `3d3cd21`) | `.pre-commit-config.yaml` 작성 완료 (110 lines) — **`pre-commit install` 의무화 0건 / `default_install_hook_types` 0건 / `fail_fast` 0건 / `commit-msg` 0건 / `pre-push` 0건** (사용자 명시 답습) |

#### 2.3.2 T3 진입 속성 매트릭스

| 속성 | 발화 |
|----|------|
| dev 환경 *정책* 변경 (`pre-commit install` 의무화) | ✅ HIGH (T3 — ADR-011 §2.4 답습) |
| `default_install_hook_types` / `fail_fast` / `minimum_pre_commit_version` 도입 | ✅ HIGH (T3 — dev 환경 정책) |
| `commit-msg` / `pre-push` stage 추가 (현 PC-4 T2 sub = `pre-commit` only) | ⚠️ HIGH (T3 — hook stage 변경) |
| README 강제 install 안내 / 가이드 | ⚠️ MEDIUM (T2 영역일 수 있음 — 가이드 문서 만 / install 자동화 = T3) |
| 개발자 *우회* 가능성 (`--no-verify` 등) | ⚠️ HIGH (T3 — branch protection rule 결합 시에만 완전 차단 — AR-3 와 cross-reference) |
| 합의 시 외부 LLM 의무 | ⚠️ MEDIUM (dev 환경 정책 = 내부 정책 영역 — 외부 LLM 의무성 *부분* 발화) |

#### 2.3.3 핵심 결정 영역 (풀 3+1 합의 시 결정 항목)

| 결정 | 옵션 후보 |
|----|--------|
| `pre-commit install` 의무화 시점 | (a) MVP-1 1.5차 (현 PC-4 T2 sub 발효 후) / (b) Operational Readiness 발효 시 / (c) Hermes PMO 격상 시 / (d) 보류 (Backlog #6 Runtime 우선) |
| `default_install_hook_types` 옵션 | (i) `["pre-commit"]` only / (ii) `["pre-commit", "commit-msg"]` / (iii) `["pre-commit", "commit-msg", "pre-push"]` |
| `fail_fast: true` 도입 | (X) 도입 / (Y) 미도입 (현 Cycle 4 답습) |
| README / DEVELOPMENT_GUIDE.md 강제 install 안내 | (1) 신설 / (2) 본문 갱신 / (3) 미설치 시 CI step 경고 (T2 영역 통합) |
| `--no-verify` 차단 정책 | (α) branch protection rule 통합 시 차단 (AR-3 dependence) / (β) git hook 자체 차단 (별도 합의 — `.git/hooks/commit-msg` 자동 install 의무화) / (γ) 정책 한정 (dev 가이드만) |
| `minimum_pre_commit_version` 강제 | (M-1) 강제 (현 4.6.0 답습) / (M-2) 미강제 |

#### 2.3.4 §2.3 판정

⚠️ **PC-4 T3 sub = T3 영역 진입 + 풀 3+1 + 사용자 명시 의무 발화**. 외부 LLM 의무성 = *부분* (dev 환경 정책 영역 — Provider Liquidity 책무 없음). **AR-3 와 cross-reference** = `--no-verify` 차단 = AR-3 branch protection + PC-4 T3 sub 모두 의존 (Defense in depth) — 합의 단위 통합 또는 분리 결정 = §3 + §4.1 권고 영역.

### 2.4 C-5b ST-1 — Hermes upstream Dockerfile entrypoint stat chmod 600 강제

#### 2.4.1 정의 + 출처

| 영역 | 답습 |
|------|------|
| 정의 | Hermes upstream Dockerfile entrypoint 시점에 `~/.hermes/auth.json` (또는 동등) 의 `stat` 검증 (chmod 600 강제) — 644 등 위반 시 컨테이너 정지 |
| `78483c5` 답습 | "C-5b (ST-1) = ⏳ Deferred — Backlog #3 T3 영역" |
| mvp1.md §3.3.1 row ST-1 | "Hermes Dockerfile entrypoint stat 검증 (chmod 600 강제) — 컨테이너 시작 시 — ✅ Hermes upstream Dockerfile 수정 필요 — 비용 低 — ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + GP-3 §5.3 답습" |
| mvp1.md §3.5 R-MVP1-G3-7 | "Hermes upstream Dockerfile 변경 결정 (ST-1 / ST-5 진입 시) = 풀 3+1 합의 + Hermes upstream PR 검토" |
| mvp1.md §3.6.3 line 290 | "ST-1 / ST-2 / ST-5 진입 (Hermes upstream 변경) = 풀 3+1 합의 + Hermes upstream PR 검토 — Hermes upstream 영역 진입 = 책무 경계 변경" |
| ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 답습 | "entrypoint stat 검증 (chmod 600 강제) — Hermes upstream Dockerfile 본문 영역" |

#### 2.4.2 T3 진입 속성 매트릭스

| 속성 | 발화 |
|----|------|
| Hermes upstream Dockerfile *본문* 변경 | ✅ HIGH (T3 — Hermes upstream 영역) |
| Hermes ≠ root of trust 보존 (5 영구 핵심 제약 #1) | ✅ HIGH (Hermes upstream 변경 = 책무 경계 변경 — root of trust 영역 침범 위험 검토 의무) |
| Hermes upstream PR 절차 / 외부 Hermes maintainer 협의 의무 | ⚠️ HIGH (Hermes PMO 영역 — 사용자 명시 결정) |
| sidecar 대안 (ST-2 inotify) 와 책무 분담 | ⚠️ MEDIUM (sidecar = Hermes upstream 변경 0건, ST-1 = Hermes upstream 변경 ✅) |
| Vault HSM ST-4 와 책무 중첩 (저장 경로 isolation) | ⚠️ MEDIUM (ST-1 = file system perm, ST-4 = HSM secret source) — 책무 분리 검토 의무 |
| 외부 LLM 1+ cross-vendor blind 의무 | ⚠️ HIGH (Hermes upstream 변경 = 외부 책무 경계 결정 — 외부 LLM 의무성 발화) |

#### 2.4.3 핵심 결정 영역 (풀 3+1 합의 시 결정 항목)

| 결정 | 옵션 후보 |
|----|--------|
| ST-1 진입 시점 | (a) MVP-1 1.5차 (현 PC-4 T2 sub 발효 후) / (b) MVP-2 이후 / (c) Operational Readiness 발효 시 (MVP-6) / (d) 보류 (ST-2 inotify sidecar 우선 — Backlog #1 답습) |
| Hermes upstream PR 절차 | (i) 사용자 명시 PR 작성 / (ii) Hermes maintainer 협의 후 본 repo upstream / (iii) fork + downstream patch (Hermes upstream 변경 0건 유지) |
| chmod 강제 형태 | (X) entrypoint script 단독 (init.sh) / (Y) Dockerfile `USER` directive + `chmod` / (Z) (X)+(Y) 통합 |
| 위반 시 동작 | (1) 컨테이너 정지 (`exit 1`) / (2) 자동 chmod 600 + 경고 / (3) audit log + 계속 진행 |
| ST-2 (inotify sidecar) / ST-3 (docker secret) 와 통합 | (α) ST-1 단독 / (β) ST-1 + ST-2 + ST-3 = ST-5 통합 (Defense in depth) / (γ) ST-1 + ST-3 부분 통합 (Layer B 답습 — ST-3 본문 채택) |
| Vault HSM ST-4 와 책무 분담 | (P) ST-1 (file system perm) + ST-4 (HSM secret source) 분리 / (Q) ST-4 도입 시 ST-1 무력화 / (R) ST-4 미도입 시 ST-1 단독 |

#### 2.4.4 §2.4 판정

⚠️ **C-5b ST-1 = T3 영역 진입 + Hermes upstream 변경 + 풀 3+1 + 외부 LLM 1+ + 사용자 명시 의무 발화**. **5 영구 핵심 제약 #1 (Hermes ≠ root of trust) 검토 의무 발화** — Hermes upstream 변경 = 책무 경계 변경. **Vault HSM ST-4 와 책무 분담 결정 의무** = §3 + §4.1 권고 영역.

### 2.5 Vault HSM ST-4 — ADR-010 통합

#### 2.5.1 정의 + 출처

| 영역 | 답습 |
|------|------|
| 정의 | HashiCorp Vault + HSM (Hardware Security Module) 통합 — Hermes 가 Vault 클라이언트 호출, secret 저장 = 외부 HSM (Multi-host 환경 권고) |
| `78483c5` 답습 | C-5b ST-1 / ST-2 / ST-4 = ⏳ Deferred (Backlog #3 T3 영역) |
| mvp1.md §3.3.1 row ST-4 | "Vault HSM 통합 (ADR-010) — 런타임 (외부 HSM) — Hermes upstream 변경 ❌ (Hermes 가 Vault 클라이언트 호출) — sidecar 부분 (Vault 자체가 외부 service) — 비용 高 (Vault 인프라 운영 비용) — ADR-010 §2 답습 — Multi-host 환경 권고" |
| mvp1.md §3.3.2 line 216 | "Operational Readiness PASS 시점 (Multi-host 전환) = ST-4 (Vault HSM) 진입 검토 — ADR-010 답습" |
| mvp1.md §3.5 R-MVP1-G3-8 | "Vault HSM 도입 결정 (ST-4 진입 시) = ADR-010 §X 진입 합의 + Multi-host 인프라 검토" |
| mvp1.md §3.6.3 line 291 | "ST-4 (Vault HSM) 진입 = ADR-010 §X 진입 합의 + 외부 LLM 1+ — T3 영역 + Multi-host 인프라" |
| ADR-010 본문 답습 | Vault HSM 권위 본문 — 진입 시점 = Operational Readiness 영역 / Multi-host 환경 권고 |

#### 2.5.2 T3 진입 속성 매트릭스

| 속성 | 발화 |
|----|------|
| ADR-010 §X 진입 합의 의무 | ✅ HIGH (T3 — ADR 본문 진입) |
| Multi-host 인프라 의무 | ✅ HIGH (T3 — single-host 환경에서 의미 약화) |
| Operational Readiness PASS 영역 cross-reference | ✅ HIGH (Backlog #7 / MVP-6 영역 cross-reference) |
| 외부 LLM 1+ cross-vendor blind 의무 | ✅ HIGH |
| Vault 인프라 운영 비용 高 | ⚠️ HIGH (운영 부담 — single-developer 환경 부적합) |
| ST-1 / ST-2 / ST-3 와 책무 분담 결정 의무 | ⚠️ HIGH (Defense in depth vs 단일 source-of-truth) |
| 5 영구 핵심 제약 #1 (Hermes ≠ root of trust) 보존 | ✅ HIGH — Vault HSM = secret source 외부 / Hermes = client 한정 → root of trust 보존 ✅ |
| 5 영구 핵심 제약 #4 (단일 source-of-truth) | ⚠️ MEDIUM — Vault HSM 도입 시 secret source 가 Vault 단일화 → 정합성 ↑ |

#### 2.5.3 핵심 결정 영역 (풀 3+1 합의 시 결정 항목)

| 결정 | 옵션 후보 |
|----|--------|
| ST-4 진입 시점 | (a) MVP-2 (조기 진입) / (b) MVP-6 Operational Readiness 발효 시 (현 권고) / (c) Hermes PMO 격상 후 (별도 합의) / (d) 보류 (single-host 환경 유지) |
| Vault 인프라 형태 | (i) HashiCorp Vault OSS + HSM (강력) / (ii) HashiCorp Vault Enterprise (운영 비용 高) / (iii) 클라우드 KMS (AWS KMS / Google KMS / Azure Key Vault) / (iv) self-hosted HSM (PKCS#11) |
| Vault client 통합 방식 | (X) Hermes 직접 호출 (Vault SDK) / (Y) sidecar 통한 호출 / (Z) Vault Agent injector |
| ADR-010 §X 본문 형태 | (1) ADR-010 신규 §X 추가 / (2) ADR-010 본문 갱신 / (3) ADR-015 신설 (Vault HSM specific) |
| ST-1 / ST-2 / ST-3 와 통합 정책 | (α) ST-4 단독 (다른 ST 무력화) / (β) ST-4 + ST-3 docker secret 부분 통합 (transition period) / (γ) ST-4 + ST-1 + ST-2 + ST-3 통합 (overkill 위험) |
| Multi-host 전환 시점 | (P) ST-4 도입과 동시 / (Q) ST-4 도입 후 별도 단계 / (R) Multi-host 전환 미실시 (single-host 유지) |

#### 2.5.4 §2.5 판정

⚠️ **Vault HSM ST-4 = T3 영역 진입 + ADR-010 §X 본문 진입 + Multi-host 인프라 + 풀 3+1 + 외부 LLM 1+ + 사용자 명시 의무 발화**. **운영 비용 高** + **Operational Readiness PASS 영역 cross-reference** (Backlog #7 / MVP-6) — 본 brief 영역에서 *진입 결정 0건* + *ADR-010 본문 변경 0건*. **현 시점 권고** = MVP-1 / MVP-2 영역 *진입 부적합* (Operational Readiness 발효 후 별도 합의 영역) — 단, 본 풀 3+1 합의에서 *진입 시점 결정* 영역으로 검토 가치 발화 (다른 5 sub-영역과의 cross-reference 정비).

### 2.6 Tier-2/3 catalog 자동 확장 *가능성 일반* (GP-3 + GP-5 통합)

#### 2.6.1 정의 + 출처

| 영역 | 답습 |
|------|------|
| 정의 | GP-3 R-4.1 Tier-1 42 catalog (45 patterns 답습) + GP-5 URL Tier-1 10 + Model Tier-1 19 → Tier-2 (베타/소규모) + Tier-3 (legacy / 비주류) 자동 확장 가능성 *일반 정책* 결정 |
| `78483c5` 답습 | "Tier-2 / Tier-3 catalog 자동 확장 = 0건" |
| `8ba5182` 답습 | "Tier-2 / Tier-3 catalog 자동 확장 = 0건" |
| Group D §2.1 (D) 답습 | "Tier-2/3 catalog 확장 = 풀 3+1 trigger #4 — gitleaks default ruleset Tier-2/3 자동 확장 위험 회피 + Python 환경 정합성 우선" |
| ADR-011 §2.4 답습 | "Tier-2/3 catalog 확장 = T3 영역" |
| mvp1.md §3.5 R-MVP1-G3-1 | "gitleaks/detect-secrets/trufflehog 도입 결정 = 풀 3+1 합의 + Tier-2/3 catalog 확장 결정 후 채택 trigger" |
| mvp1.md §4.6 R-MVP1-G5-7/8 | "URL/모델 Tier-2 / Tier-3 vendor 추가 결정 = 풀 3+1 합의 + Tier-2/3 catalog 확장 결정" |

#### 2.6.2 T-5 (β) (§2.2) 와 *책무 분리*

본 §2.6 = **일반 정책** 영역 (Tier-2/3 catalog 자동 확장 *정책* 자체) ; §2.2 = **specific subset** (GP-5 provider URL / model name Tier-2/3 확장).

| 영역 | §2.2 (T-5 β) | §2.6 (일반 정책) |
|----|----------|----------|
| 대상 | GP-5 URL / Model catalog | GP-3 + GP-5 + 미래 catalog 일반 |
| 결정 영역 | URL / Model Tier-2/3 vendor 추가 | catalog 확장 *정책* + *형식* + *프로세스* |
| 합의 단위 | T-5 (β) 합의 단독 / §2.6 통합 가능 | §2.2 와 통합 가능 / 분리 가능 |

#### 2.6.3 T3 진입 속성 매트릭스

| 속성 | 발화 |
|----|------|
| catalog *정책* 변경 (Tier 정책 일반) | ✅ HIGH (T3) |
| GP-3 + GP-5 영역 통합 결정 영역 | ✅ HIGH (단일 정책 vs 영역 분리 정책) |
| 풀 3+1 합의 의무 (Group D §2.1 (D) + R-MVP1-G3-1 + R-MVP1-G5-7/8 답습) | ✅ HIGH |
| 외부 LLM 1+ cross-vendor blind 의무 | ✅ HIGH (vendor 다양성 = cross-vendor 평가 의무) |
| FP / FN 폭증 위험 | ⚠️ HIGH (catalog 확장 = pattern 충돌 + FN 회피 의무) |
| Implementation Evidence PASS 의존 (실 운영 evidence 의무) | ⚠️ HIGH (실 src/ 도입 후 측정 baseline 의무) |

#### 2.6.4 핵심 결정 영역 (풀 3+1 합의 시 결정 항목)

| 결정 | 옵션 후보 |
|----|--------|
| Tier 정의 기준 (일반 정책) | (a) vendor 시장 점유율 + popularity / (b) Provider Liquidity 5-way 답습 / (c) ADR-009 C-N 답습 / (d) GP-3 R-4.1 vs GP-5 분리 정책 |
| Tier-2/3 확장 *프로세스* | (i) 단일 풀 3+1 합의로 일괄 확장 / (ii) Tier 별 별도 합의 / (iii) vendor 별 별도 합의 (가장 보수적) |
| catalog 본문 *형식* | (X) 도구 내장 (현 Group A 3차 답습) / (Y) 외부 YAML/JSON 분리 / (Z) 외부 + 도구 내장 dual-track |
| Tier-2/3 *자동 동기화* (vendor catalog 외부 source — 예: LiteLLM vendor list) 도입 | (1) 도입 (Provider Liquidity 답습) / (2) 도입 보류 (수동 catalog 유지) / (3) part-auto (vendor 식별 자동 + 패턴 추가 수동) |
| FP/FN mitigation 정책 | (M-1) Tier 별 별도 PASS 기준 / (M-2) Tier 1+2 통합 PASS / (M-3) Tier 3 비활성화 default |
| Implementation Evidence PASS 의존 | (P) Implementation Evidence PASS 발효 후 진입 / (Q) MVP-1 1.5차 진입 (Evidence baseline 없이) / (R) MVP-2 이후 |

#### 2.6.5 §2.6 판정

⚠️ **Tier-2/3 catalog 자동 확장 *가능성 일반* = T3 영역 진입 + 풀 3+1 + 외부 LLM 1+ + 사용자 명시 의무 발화**. **§2.2 T-5 (β) 와 책무 분리** = T-5 (β) = GP-5 specific subset / §2.6 = GP-3+GP-5+미래 catalog 일반 정책. **합의 단위 결정 영역** = §3 + §4.1 권고 영역.

---

## 3. 6 sub-영역 *결합 위험* / *책무 중첩* / *분리 가능성* 매트릭스

### 3.1 책무 영역 매트릭스 (6 sub-영역 × 7 책무 차원)

| sub-영역 | enforcement layer | catalog 본문 | dev 환경 정책 | Hermes upstream | secret source | Multi-host | ADR 진입 |
|--------|----|----|----|----|----|----|----|
| (1) AR-3 | ✅ HIGH (T3) | ❌ | ⚠️ MEDIUM (PC-4 T3 sub 통합 시) | ❌ | ❌ | ❌ | (ADR-008 cross-reference) |
| (2) T-5 (β) | ❌ (catalog ⊂ enforcement) | ✅ HIGH (T3) | ❌ | ❌ | ❌ | ❌ | ❌ |
| (3) PC-4 T3 sub | ⚠️ MEDIUM (AR-3 통합 시) | ❌ | ✅ HIGH (T3) | ❌ | ❌ | ❌ | (ADR-011 cross-reference) |
| (4) C-5b ST-1 | ❌ | ❌ | ❌ | ✅ HIGH (T3) | ⚠️ MEDIUM (file perm) | ❌ | (ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 cross-reference) |
| (5) Vault HSM ST-4 | ❌ | ❌ | ❌ | ❌ (Hermes client 한정) | ✅ HIGH (외부 HSM) | ✅ HIGH | ✅ ADR-010 §X 진입 |
| (6) Tier-2/3 자동 확장 일반 | ❌ | ✅ HIGH (T3) | ❌ | ❌ | ❌ | ❌ | (ADR-011 §2.4 cross-reference) |

### 3.2 *결합 위험* 매트릭스 (sub-영역 페어 결합 시 발생하는 추가 위험)

| 페어 | 결합 위험 | 분리 가능성 |
|----|-------|---------|
| (1) AR-3 × (3) PC-4 T3 sub | **Defense in depth** — `--no-verify` 우회 차단 = AR-3 + PC-4 T3 sub 모두 의존 / `--no-verify` 우회 시 PC-4 T3 sub 무력화 (AR-3 단독 차단 가능) | ⚠️ 부분 분리 (책무 영역 다름, 우회 차단 효과 결합) |
| (1) AR-3 × (2) T-5 (β) | AR-3 = enforcement, T-5 (β) = catalog source — **책무 분리 명확** | ✅ 분리 가능 |
| (2) T-5 (β) × (6) Tier-2/3 일반 | T-5 (β) ⊂ Tier-2/3 일반 정책 — **subset / superset 관계** | ⚠️ 부분 분리 (일반 정책 후 specific subset 적용 권고) |
| (4) C-5b ST-1 × (5) Vault HSM ST-4 | **secret source 책무 분담** — ST-1 = file perm / ST-4 = HSM source / 결합 시 책무 중첩 + 단일 source-of-truth 위반 가능 | ⚠️ HIGH 분리 의무 (책무 분담 결정 의무) |
| (4) C-5b ST-1 × (1) AR-3 | **Hermes upstream vs GitHub repo policy** — 책무 영역 다름 | ✅ 분리 가능 |
| (5) Vault HSM ST-4 × (6) Tier-2/3 일반 | secret HSM vs catalog 일반 — **책무 영역 다름** | ✅ 분리 가능 |
| (3) PC-4 T3 sub × (2) T-5 (β) | dev 환경 정책 vs catalog — **책무 영역 다름** | ✅ 분리 가능 |
| (3) PC-4 T3 sub × (4) C-5b ST-1 | dev 환경 vs Hermes upstream — **책무 영역 다름** | ✅ 분리 가능 |
| (3) PC-4 T3 sub × (5) Vault HSM ST-4 | dev 환경 vs HSM — **책무 영역 다름** | ✅ 분리 가능 |
| (3) PC-4 T3 sub × (6) Tier-2/3 일반 | dev 환경 vs catalog — **책무 영역 다름** | ✅ 분리 가능 |
| (1) AR-3 × (4) C-5b ST-1 | GitHub repo vs Hermes upstream — **책무 영역 다름** | ✅ 분리 가능 |
| (1) AR-3 × (5) Vault HSM ST-4 | GitHub repo vs HSM — **책무 영역 다름** | ✅ 분리 가능 |
| (1) AR-3 × (6) Tier-2/3 일반 | enforcement vs catalog — **책무 영역 다름** | ✅ 분리 가능 |
| (2) T-5 (β) × (4) C-5b ST-1 | catalog vs Hermes upstream — **책무 영역 다름** | ✅ 분리 가능 |
| (2) T-5 (β) × (5) Vault HSM ST-4 | catalog vs HSM — **책무 영역 다름** | ✅ 분리 가능 |

### 3.3 *분리 가능성* 합산

| 페어 합계 | 분리 가능 | 부분 분리 | 분리 어려움 |
|---------|--------|--------|---------|
| 15 페어 (C(6,2)) | 11 | 3 ((1)×(3), (2)×(6), (4)×(5)) | 0 |

### 3.4 *책무 그룹화* 권고

3.2 매트릭스 답습:

- **Group α** (enforcement / dev 환경 차단 통합) = (1) AR-3 + (3) PC-4 T3 sub — 결합 위험 = `--no-verify` 차단 Defense in depth
- **Group β** (catalog source 정책) = (2) T-5 (β) + (6) Tier-2/3 자동 확장 일반 — subset / superset 관계
- **Group γ** (secret source / Hermes upstream) = (4) C-5b ST-1 + (5) Vault HSM ST-4 — 책무 분담 결정 의무

위 그룹화 = **3 그룹 / 6 sub-영역** 분리 권고 (각 그룹 = 2 sub-영역).

---

## 4. 합의 *단위* + 합의 *형태* 권고

### 4.1 합의 *단위* 옵션 매트릭스

| 옵션 | 단위 | 책무 합산 | 합의 부담 | 적합성 |
|-----|----|-------|---------|------|
| **(I)** 6 sub-영역 *단일 통합* 합의 (1 합의) | 1 합의 | 7/7 책무 차원 동시 결정 | 매우 高 (single PR / single approve 부담 / Reviewer 분석 부담) | ⚠️ 가능 — 합의 부담 高 |
| **(II)** 3 그룹 분리 (Group α / β / γ, 3 합의) | 3 합의 | 그룹 별 책무 차원 동시 결정 | 中 (그룹 별 분담) | ✅ **권고 후보 1** — §3.4 답습 |
| **(III)** 6 sub-영역 *각각* 분리 (6 합의) | 6 합의 | sub-영역 단독 결정 | 低-中 (각 단독) | ⚠️ 가능 — 합의 부담 분산 / 결합 위험 분석 분리 부담 |
| **(IV)** Group α 통합 + 나머지 4 분리 (5 합의) | 5 합의 | α 만 통합, 나머지 단독 | 中 | ⚠️ 가능 — 책무 그룹화 부분 답습 |
| **(V)** Group α + Group β 통합 + Group γ 분리 (3 합의, 다른 그룹화) | 3 합의 | 다른 그룹화 | 中 | ⚠️ 가능 — §3.4 답습 |
| **(VI)** 책무 영역 별 분리 (enforcement 1 + catalog 1 + dev 환경 1 + Hermes upstream 1 + HSM 1 = 5 합의) | 5 합의 | 책무 영역 별 단독 결정 | 中 | ⚠️ 가능 — sub-영역 책무 영역 매트릭스 답습 |

**본 brief 권고**: **(II) 3 그룹 분리** — §3.4 책무 그룹화 답습 + 합의 부담 중간 + 결합 위험 분석 책무 영역 별 처리 + cross-reference 명시 가능.

#### 4.1.1 권고 합의 단위 (II) 답습 시 합의 보고서 경로

| 그룹 | 경로 후보 |
|----|--------|
| Group α (AR-3 + PC-4 T3 sub) | `docs/review/3plus1-consensus-2026-05-<TBD>-backlog3-enforcement-defense.md` |
| Group β (T-5 (β) + Tier-2/3 일반) | `docs/review/3plus1-consensus-2026-05-<TBD>-backlog3-catalog-tier23-policy.md` |
| Group γ (C-5b ST-1 + Vault HSM ST-4) | `docs/review/3plus1-consensus-2026-05-<TBD>-backlog3-secret-source-hermes-upstream.md` |

### 4.2 합의 *형태* 권고

| 합의 형태 | 적합성 | 사유 |
|--------|------|------|
| **(가) 풀 3+1 합의 + 외부 LLM 1+ cross-vendor blind + 사용자 명시** | ✅ **권고** | (i) 6 sub-영역 *모두 T3 영역* 의무 발화 — ADR-011 §2.4 답습 / (ii) R-MVP1-G3-7/8 + R-MVP1-G5-7/8/9 모두 풀 3+1 + 외부 LLM 1+ 답습 / (iii) Group α / β / γ 모두 T3 영역 진입 = 풀 3+1 의무 / (iv) Layer B `f40423f` Backlog #3 T3 영역 분리 명시 답습 |
| (나) 풀 3+1 합의 (외부 LLM 미의무) | ❌ 부적합 | T3 영역 = 외부 LLM 1+ cross-vendor blind 의무 답습 — Provider Liquidity 책무 발화 |
| (다) Reviewer-only 단축 합의 | ❌ 부적합 | T3 영역 = 풀 3+1 의무 |
| (라) (가) + 인간 리뷰 의무 (mvp1.md §4.7.3 답습 / G3 §4.4.2 답습) | ⚠️ MVP-6 영역 (Hermes PMO 격상 시 의무) | 본 brief 영역 외 (Hermes PMO 격상 시 의무 — Backlog #7 / MVP-6 영역) |

**본 brief 권고**: **(가) 풀 3+1 합의 + 외부 LLM 1+ cross-vendor blind + 사용자 명시** (3 그룹 각각).

### 4.3 합의 발효 시점 (사용자 명시 결정 의무 영역)

| 시점 | 합의 발효 영역 | 후속 단계 |
|-----|----------|--------|
| Group α 합의 발효 | AR-3 + PC-4 T3 sub *수단 결정* 한정 (실 branch protection 변경 / 실 `pre-commit install` 의무화 0건) | 사용자 명시 결정 → 별도 실 적용 단계 |
| Group β 합의 발효 | T-5 (β) + Tier-2/3 일반 *정책 결정* 한정 (실 catalog 본문 확장 0건) | 사용자 명시 결정 → 별도 실 catalog 본문 변경 단계 |
| Group γ 합의 발효 | C-5b ST-1 + Vault HSM ST-4 *수단 결정* 한정 (실 Hermes upstream 변경 / 실 Vault 통합 0건) | 사용자 명시 결정 → 별도 실 적용 단계 |

**합의 발효 = *수단 결정* 한정** (실 변경 = 별도 단계, 사용자 명시 결정 의무).

---

## 5. 풀 3+1 Agent A / B / C 관점 분배 권고

### 5.1 표준 풀 3+1 Agent 역할 답습 (CLAUDE.md §3 답습)

| Agent | 관점 | 핵심 질문 |
|-------|------|--------|
| Agent A | 구현 분석가 | "실제로 동작하는가?" — 기술적 구현 가능성, 의존성, 성능 |
| Agent B | 품질 / 안전성 검증가 | "안전하고 견고한가?" — 보안, 엣지케이스, 문서 정합성 |
| Agent C | 대안 탐색가 | "더 나은 방법이 있는가?" — 대안 기술, 트레이드오프 |
| Reviewer | 검토 에이전트 | "최선의 합의는?" — 교차 비교, 최종 판단 |

### 5.2 Group α (AR-3 + PC-4 T3 sub) — Agent 관점 분배

| Agent | 핵심 분석 영역 |
|------|----------|
| Agent A | AR-3 + PC-4 T3 sub 기술 통합 (CODEOWNERS / required check / commit signing / `default_install_hook_types` / `fail_fast` 옵션 동작 검증) + `--no-verify` 우회 차단 효과 분석 + GitHub Actions integration / pre-commit framework 호환성 |
| Agent B | 보안 (T3 정책 변경 = 책무 경계 변경 / fork PR 보안 / `pull_request_target` 위험 / commit signing key 관리 / `--no-verify` 우회 가능성 잔존) + 엣지케이스 (개발자 우회 / external contributor 정책 / hook stage 충돌) + 문서 정합성 (mvp1.md §4.4.2 + §4.6 + ADR-011 §2.4 답습 정합) |
| Agent C | 대안 (CODEOWNERS only vs required check only vs 통합 / pre-commit framework 외 대안 = `husky` Node 환경 / `lefthook` 등) + 트레이드오프 (Defense in depth 부담 vs 우회 차단 효과 / dev 환경 강제 vs 개발자 friction) |

### 5.3 Group β (T-5 (β) + Tier-2/3 일반) — Agent 관점 분배

| Agent | 핵심 분석 영역 |
|------|----------|
| Agent A | Tier 분류 기준 기술 구현 (vendor 시장 점유율 + ADR-009 답습) + Tier-2/3 catalog 본문 형식 (yaml/json/도구 내장) + 자동 동기화 가능성 (LiteLLM vendor list 답습) + FP/FN 측정 방법 |
| Agent B | 보안 (Tier-2/3 vendor 추가 시 보안 평가 / 외부 catalog 의존 시 supply chain 위험 / vendor revocation 정책) + 엣지케이스 (vendor 중복 / vendor 이름 변경 / deprecated vendor) + 문서 정합성 (ADR-009 + Provider Liquidity 5-way + GP-5 §9.3 답습) |
| Agent C | 대안 (LiteLLM vendor list 직접 의존 vs 자체 catalog 유지 / vendor-agnostic pattern vs vendor-specific catalog) + 트레이드오프 (catalog 확장 부담 vs FN cover / 자동 동기화 vs 안정성) |

### 5.4 Group γ (C-5b ST-1 + Vault HSM ST-4) — Agent 관점 분배

| Agent | 핵심 분석 영역 |
|------|----------|
| Agent A | Hermes upstream Dockerfile PR 절차 기술 검토 + Vault SDK 통합 형태 (Hermes 직접 호출 / sidecar / Vault Agent injector) + Multi-host 인프라 구성 + ADR-010 §X 본문 형태 (신규 §X vs 갱신 vs ADR-015 신설) |
| Agent B | 보안 (Hermes ≠ root of trust 보존 검증 / Vault HSM 보안 평가 / HSM key 관리 / Vault transit / Vault audit log 통합) + 엣지케이스 (Hermes upstream maintainer 거부 / Vault inaccessible 시 fallback / HSM SPOF) + 문서 정합성 (ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + ADR-010 §2 + ADR-011 §2.4 + 5 영구 핵심 제약 #1 답습) |
| Agent C | 대안 (ST-1 entrypoint stat vs ST-2 inotify sidecar 책무 분담 / Vault HSM vs 클라우드 KMS vs PKCS#11 self-hosted / fork+downstream patch vs upstream PR) + 트레이드오프 (Hermes upstream 변경 vs sidecar / Vault 운영 비용 vs 보안 강도) |

### 5.5 Reviewer 검토 의무 영역 (3 그룹 공통)

| 검토 영역 | 의무 발화 |
|---------|-------|
| 일치 (Consensus) — 3 Agent 모두 동의 영역 | ✅ 의무 |
| 부분 일치 (Partial) — 2 Agent 동의, 1 Agent 이견 영역 | ✅ 의무 |
| 불일치 (Divergence) — 3 Agent 모두 다른 의견 | ✅ 의무 |
| 누락 (Gap) — 특정 Agent 만 언급한 사항 | ✅ 의무 |
| 외부 LLM 1+ cross-vendor blind 응답 통합 (T3 영역 의무) | ✅ 의무 |
| 5 영구 핵심 제약 5/5 보존 검증 | ✅ 의무 |
| ADR-011 §2.1 (a)~(e) 5 조건 발화 / 미발화 평가 | ✅ 의무 |
| 7/7 풀 3+1 승격 트리거 검증 (모두 발화) | ✅ 의무 |
| Provider Liquidity 5-way 보존 검증 | ✅ 의무 |
| Backlog #1 / #2 / #4 / #6 / #7 자동 진입 0건 검증 | ✅ 의무 |

---

## 6. 외부 LLM cross-vendor blind 의뢰 형식 + 핵심 질문 권고

### 6.1 외부 LLM 의뢰 의무성 (T3 영역 답습)

본 brief 6 sub-영역 *모두* = T3 영역 + ADR-011 §2.4 답습 → **외부 LLM 1+ cross-vendor blind 의뢰 의무 발화** (R-MVP1-G3-7/8 + R-MVP1-G5-7/8/9 답습).

### 6.2 의뢰 형식 답습 출처

| 출처 | 답습 영역 |
|------|--------|
| `docs/external-review/2026-05-10-cross-vendor-evidence-ledger-protection-request.md` (411줄, 6 질문) | 최신 cross-vendor 의뢰 형식 답습 — Group C 후속 영역 |
| `docs/external-review/2026-05-09-c14-cross-vendor-p2v3-pre-adoption-request.md` (~340줄) | C-14 cross-vendor blind 의뢰 형식 답습 (응답 2건 회수 후 흡수 — §C-14 11 핵심 조건 추적) |
| §부록 B 명시 답습 | 응답 = *입력* 한정, 자동 운영 적용 / Hermes PMO 격상 / ADR 본문 자동 갱신 모두 *불가* |

### 6.3 의뢰 vendor 권고 (cross-vendor blind 의무 답습)

| vendor | 의뢰 의무성 | 사유 |
|-------|---------|-----|
| Anthropic (Claude) | ❌ (내부 작업 도구 — blind 위반) | 본 repo Claude 사용 답습 |
| OpenAI (GPT) | ✅ 의뢰 후보 (Provider Liquidity 5-way 답습) | cross-vendor 평가 |
| Google (Gemini) | ✅ 의뢰 후보 (C-14 응답 2 답습) | cross-vendor 평가 + 사고모델 다양성 |
| Meta (Llama) / Mistral | ⚠️ 부분 (vendor 평가 다양성 의무 시) | T-5 (β) Group β 의뢰 시 추가 |
| Cohere | ⚠️ 부분 | T-5 (β) Group β 의뢰 시 추가 |

**본 brief 권고**: 각 그룹별로 **1+ vendor 의뢰** (최소 의무). 권고 = **GPT + Gemini 2 vendor 의뢰** (C-14 답습) — 의뢰 부담 / cross-vendor 책무 균형.

### 6.4 의뢰 *영원 격리* 보장 (§부록 B 답습)

| 보장 | 영역 |
|----|----|
| 응답 = *입력* 한정 | 응답 자동 운영 적용 / Hermes PMO 격상 / ADR 본문 자동 갱신 *불가* |
| 응답 회수 후 처리 | (a) 응답 1건 + 단순 검토 → Reviewer-only 단축 합의 적격 / (b) 응답 1건 이상 BLOCK 또는 PARTIAL 시 → 풀 3+1 + 외부 LLM 의무 |
| 응답 저장 영역 | `docs/external-review/2026-05-<TBD>-backlog3-<group>-{request,response,response-gemini,response-claude,response-<vendor>}.md` |
| 의뢰 발송 방식 | 사용자 명시 외부 LLM 호출 (claude code 자동 호출 0건) |

### 6.5 의뢰 핵심 질문 권고 (3 그룹 각각)

#### 6.5.1 Group α (AR-3 + PC-4 T3 sub) 의뢰 핵심 질문

1. AR-3 (CI step fail-closed + GitHub branch protection rule 통합) 의 7 결정 영역 (§2.1.3) 中 어느 옵션이 (i) Provider Liquidity 5-way 보존 (ii) Hermes ≠ root of trust 보존 (iii) 우회 차단 효과 측면에서 최선인가?
2. PC-4 T3 sub (`pre-commit install` 의무화 + dev 환경 강제) 의 6 결정 영역 (§2.3.3) 中 (i) 개발자 friction 최소화 (ii) 우회 가능성 최소화 측면에서 최선 옵션은?
3. AR-3 × PC-4 T3 sub 결합 (Defense in depth) 시 `--no-verify` 우회 차단 효과 평가 — 효과 / 한계?
4. 외부 contributor / fork PR 정책 — `pull_request_target` 도입 vs PR 차단 vs default 정책 유지 中 최선?
5. commit signing 의무화 시점 — MVP-1 1.5차 / Operational Readiness / Hermes PMO 격상 中 권고?
6. 본 합의가 *진입 부적합* 인 시점 또는 *차단 의무* 인 영역이 있는가?

#### 6.5.2 Group β (T-5 (β) + Tier-2/3 일반) 의뢰 핵심 질문

1. Tier-2/3 catalog 자동 확장 *정책 일반* 의 6 결정 영역 (§2.6.4) 中 (i) FP/FN 균형 (ii) catalog 유지 부담 (iii) Provider Liquidity 보존 측면에서 최선?
2. T-5 (β) (URL Tier-1 10 / Model Tier-1 19 → Tier-2/3 확장) 의 6 결정 영역 (§2.2.3) 中 권고 vendor catalog 확장 범위?
3. LiteLLM vendor list 자동 동기화 vs 자체 catalog 유지 中 권고 — Provider Liquidity 답습?
4. Tier-2/3 도입 시 GP-3 R-4.1 42 catalog 확장 정책 / GP-5 URL/Model 확장 정책 분리 vs 통합?
5. Implementation Evidence PASS 의존 시점 — MVP-1 1.5차 진입 (Evidence baseline 없이) vs MVP-2 이후 中 권고?
6. 본 합의가 *진입 부적합* 인 시점 또는 *차단 의무* 인 영역이 있는가?

#### 6.5.3 Group γ (C-5b ST-1 + Vault HSM ST-4) 의뢰 핵심 질문

1. C-5b ST-1 (Hermes upstream Dockerfile entrypoint stat chmod 600 강제) 의 6 결정 영역 (§2.4.3) 中 (i) Hermes ≠ root of trust 보존 (ii) Hermes upstream 변경 최소화 측면에서 최선 옵션은?
2. Vault HSM ST-4 (ADR-010 통합) 의 6 결정 영역 (§2.5.3) 中 (i) Multi-host 인프라 부담 (ii) 운영 비용 (iii) 단일 source-of-truth 보존 측면에서 최선?
3. ST-1 / ST-2 inotify sidecar / ST-3 docker secret / ST-4 통합 정책 中 권고 — Defense in depth vs 단일 source-of-truth 트레이드오프?
4. ST-4 진입 시점 — MVP-2 / MVP-6 Operational Readiness / Hermes PMO 격상 후 中 권고?
5. ST-1 + ST-4 결합 시 책무 중첩 / 단일 source-of-truth 위반 위험 — 분리 / 통합 / 무력화 中 권고?
6. 본 합의가 *진입 부적합* 인 시점 또는 *차단 의무* 인 영역이 있는가?

---

## 7. Rollback Trigger 통합 매트릭스

### 7.1 6 sub-영역 *각* Rollback Trigger 답습 (mvp1.md §3.5 + §4.6 답습)

| Trigger | sub-영역 | 발화 조건 | 발화 시 행동 |
|--------|---------|---------|----------|
| R-MVP1-G3-7 | (4) C-5b ST-1 | Hermes upstream Dockerfile 변경 결정 (ST-1 / ST-5 진입 시) | 풀 3+1 합의 + Hermes upstream PR 검토 |
| R-MVP1-G3-8 | (5) Vault HSM ST-4 | Vault HSM 도입 결정 (ST-4 진입 시) | ADR-010 §X 진입 합의 + Multi-host 인프라 검토 |
| R-MVP1-G5-7 | (2) T-5 (β) + (6) Tier-2/3 일반 | URL Tier-2 / Tier-3 vendor 추가 결정 | 풀 3+1 합의 + Tier-2/3 catalog 확장 결정 |
| R-MVP1-G5-8 | (2) T-5 (β) + (6) Tier-2/3 일반 | 모델 Tier-2 / Tier-3 vendor 추가 결정 | 풀 3+1 합의 + Tier-2/3 catalog 확장 결정 |
| R-MVP1-G5-9 | (1) AR-3 | branch protection rule 변경 결정 (AR-2 진입) | T3 영역 + 풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시 |
| R-MVP1-G3-3 | (4) C-5b ST-1 + (5) Vault HSM ST-4 | 실 secret 처리 정책 변경 (ADR-008 §A.2 / ADR-010 본문 변경) | T3 영역 → 풀 3+1 합의 + 외부 LLM 1+ + 인간 리뷰 + 사용자 명시 |
| R-1 (`implementation-runtime-roadmap.md` §6.2) | (6) Tier-2/3 일반 | secret pattern catalog 변경 (Tier-1 42 catalog 답습) | 풀 3+1 합의 + 외부 LLM 1+ |
| R-MVP1-G3-1 | (6) Tier-2/3 일반 | gitleaks/detect-secrets/trufflehog 도입 결정 | 풀 3+1 합의 + Tier-2/3 catalog 확장 결정 후 채택 trigger |

### 7.2 통합 Rollback Trigger 합산

| sub-영역 | 발화 Trigger 수 | 합의 부담 |
|--------|-----------|--------|
| (1) AR-3 | 1 (R-MVP1-G5-9) | 中 |
| (2) T-5 (β) | 2 (R-MVP1-G5-7/8) | 中 |
| (3) PC-4 T3 sub | 0 (개별 trigger 없음 — ADR-011 §2.4 + mvp1.md §4.4.2 영역) | 低-中 |
| (4) C-5b ST-1 | 2 (R-MVP1-G3-7 + R-MVP1-G3-3) | 中-高 |
| (5) Vault HSM ST-4 | 2 (R-MVP1-G3-8 + R-MVP1-G3-3) | 高 (ADR-010 §X 진입 의무) |
| (6) Tier-2/3 일반 | 3 (R-1 + R-MVP1-G3-1 + R-MVP1-G5-7/8 부분) | 高 |

---

## 8. 7/7 풀 3+1 승격 트리거 *재검증*

### 8.1 본 brief 6 sub-영역 *모두* 발화 — Reviewer-only 단축 합의 *부적합*

| # | 트리거 | 본 brief 6 sub-영역 발화 |
|---|----|--------------------|
| 1 | 9 sub-수단 외 수단 *재결정* | ⚠️ 부분 — (2) T-5 (β) catalog 확장 / (4) ST-1 / (5) ST-4 = 추가 수단 결정 |
| 2 | **T3 영역 자동 진입** | ✅ HIGH (BLOCKING) — 본 brief 6 sub-영역 모두 T3 영역 |
| 3 | 사용자 명시 3 결정 (α/ii/(가)) *재변경* | ❌ 0건 (PC-4 T2 sub Cycle 4 답습 한정 — 본 brief 영역 외) |
| 4 | Provider Liquidity 5-way 약화 | ⚠️ 부분 — (2) T-5 (β) Tier-2/3 vendor 추가 시 / (5) Vault HSM 도입 시 (Provider Liquidity 책무 영향 검토 의무) |
| 5 | 5 영구 핵심 제약 약화 | ⚠️ HIGH — (4) C-5b ST-1 = Hermes ≠ root of trust 검토 의무 / (5) Vault HSM = 단일 source-of-truth 영향 검토 의무 |
| 6 | **MVP-1 PASS 재선언 / Layer E (Operational Readiness PASS) / Layer F (Hermes PMO 격상)** | ❌ 0건 (사용자 명시 7 금지 답습) |
| 7 | 외부 LLM cross-vendor blind 없는 T3 결정 | ✅ HIGH — 본 brief 권고 = 외부 LLM 1+ cross-vendor blind 의뢰 의무 발화 (§6 답습) |

**합산**: 7/7 트리거 中 **트리거 #2 = HIGH BLOCKING** + 트리거 #5 = HIGH + 트리거 #7 = HIGH + 부분 #1 + #4 → **풀 3+1 + 외부 LLM 1+ + 사용자 명시 의무 발화 확정**.

### 8.2 Reviewer-only 단축 합의 *적격성 0/6 sub-영역*

본 brief 6 sub-영역 *모두* Reviewer-only 단축 합의 *부적격* (T3 영역 진입 의무 답습). 합의 형태 = **풀 3+1 + 외부 LLM 1+ + 사용자 명시** (§4.2 답습).

---

## 9. 우선순위 권고 + 차단 요인

### 9.1 6 sub-영역 *합의 진입 우선순위*

| 순위 | sub-영역 | 사유 |
|----|--------|-----|
| 1순위 | (3) PC-4 T3 sub | PC-4 T2 sub Cycle 4 완료 후 자연 후속 + dev 환경 정책 (Hermes upstream 변경 0건) — 합의 부담 최저 + Group α 1/2 |
| 2순위 | (1) AR-3 | Group α 2/2 (PC-4 T3 sub 통합 가능) — GitHub repo 정책 변경 + 외부 contributor / fork PR 정책 결정 |
| 3순위 | (6) Tier-2/3 자동 확장 일반 | Group β 1/2 (T-5 β 와 통합 가능) — 정책 일반 결정 + Implementation Evidence PASS 의존 |
| 4순위 | (2) T-5 (β) | Group β 2/2 — specific subset (GP-5 URL/Model 확장) |
| 5순위 | (4) C-5b ST-1 | Group γ 1/2 — Hermes upstream 변경 + 5 영구 핵심 제약 #1 검토 의무 |
| 6순위 | (5) Vault HSM ST-4 | Group γ 2/2 — ADR-010 §X 진입 + Multi-host 인프라 + 운영 비용 高 (Operational Readiness 영역 cross-reference) |

### 9.2 우선순위 *조정 권고* (Group 기반 합의 (II) 답습 시)

(II) 3 그룹 분리 권고 답습:

```
1순위: Group α (AR-3 + PC-4 T3 sub) — Defense in depth, dev 환경 + GitHub repo
2순위: Group β (T-5 (β) + Tier-2/3 일반) — catalog 정책 + specific subset
3순위: Group γ (C-5b ST-1 + Vault HSM ST-4) — secret source + Hermes upstream
```

### 9.3 *차단 요인* (본 brief 6 sub-영역 전체 합의 진입 전 차단 요인)

| # | 차단 요인 | 발화 |
|---|--------|-----|
| 1 | Backlog #6 (Runtime + CI-hook implementation) 미진입 | ⚠️ MEDIUM — MVP-1 Implementation Entry `1eab814` 권고 우선순위 1 답습 |
| 2 | Implementation Evidence PASS 미발효 | ⚠️ MEDIUM — Group β 의 FP/FN baseline 측정 의무 발화 시 차단 |
| 3 | 외부 LLM 1+ cross-vendor blind 의뢰 발송 미실시 | ⚠️ HIGH — T3 영역 합의 진입 전 의뢰 발송 의무 |
| 4 | Backlog #1 (GP-3 1.5차 — ST-2 inotify sidecar) 미진입 | ⚠️ MEDIUM — Group γ ST-1 / ST-4 책무 분담 결정 시 ST-2 답습 의존 |
| 5 | Operational Readiness PASS (Layer E) 미발효 | ⚠️ HIGH — Group γ ST-4 Vault HSM 진입 영역 의존 (Backlog #7 / MVP-6) |
| 6 | C-14 cross-vendor 11 핵심 조건 흡수 미완 | ⚠️ MEDIUM — P2 v3 정식 채택 합의 영역 답습 (별도 영역) |

### 9.4 본 brief 후속 다음 단계 우선순위 권고

| 우선순위 | 다음 단계 | 사유 |
|--------|--------|------|
| **(I)** | **본 brief 그대로 승인 → 사용자 명시 후속 단계 결정 영역** | 본 brief = DRAFT 한정, 합의 진입 결정 = 사용자 명시 |
| (II) | Backlog #6 (Runtime + CI-hook implementation) 우선 진입 — MVP-1 Implementation Entry `1eab814` 권고 우선순위 1 답습 → Backlog #3 합의 후 진입 | 본 brief 6 sub-영역 = T3 영역 — Backlog #6 (T2 영역) 우선 진입 권고 답습 |
| (III) | 본 brief 그대로 승인 + Group α 풀 3+1 합의 *발송* 진입 (외부 LLM 의뢰 동시 진행) | Group α = 1순위 + Hermes upstream 변경 0건 |
| (IV) | 본 brief 보류 → MVP-2 진입 brief 작성 | Implementation Evidence PASS 미발효 — 부적합 |
| (V) | 본 brief 보류 → C-14 cross-vendor 11 조건 흡수 작업 우선 | P2 v3 정식 채택 영역 — 별도 영역 |
| (VI) | 본 brief 보류 → 세션 종료 | 사용자 명시 결정 영역 |

---

## 10. 메타 검증

| 메타 검증 | 본 brief |
|---------|--------|
| 사용자 명시 검토 범위 답습 (AR-3 / T-5 β / PC-4 T3 sub / C-5b ST-1 / Vault HSM ST-4 / Tier-2/3 catalog 자동 확장 가능성 통합 검토) | ✅ §2.1 ~ §2.6 |
| 사용자 명시 7 금지 답습 (T3 진입 / branch protection / dev 환경 강제 / Hermes upstream / Vault HSM / Operational Readiness / Hermes PMO) | ✅ §0.3 + 부록 B |
| 본 brief = DRAFT 한정 (commit 0건 / push 0건) | ✅ 헤더 + §0.4 |
| 6 sub-영역 모두 T3 영역 진입 의무 발화 명시 | ✅ §2.1.2 ~ §2.6.3 |
| 7/7 풀 3+1 승격 트리거 검증 (모두 발화) → 풀 3+1 + 외부 LLM 1+ + 사용자 명시 의무 발화 | ✅ §8 |
| Reviewer-only 단축 합의 *부적격* 확정 (6/6 sub-영역) | ✅ §8.2 |
| 합의 단위 권고 ((II) 3 그룹 분리) + 합의 형태 권고 ((가) 풀 3+1 + 외부 LLM 1+ + 사용자 명시) | ✅ §4.1 + §4.2 |
| 풀 3+1 Agent A/B/C 관점 분배 (3 그룹 각각) | ✅ §5.2 ~ §5.4 |
| 외부 LLM cross-vendor blind 의뢰 형식 + 핵심 질문 권고 (3 그룹 각각) | ✅ §6 |
| Rollback Trigger 통합 매트릭스 (mvp1.md §3.5 + §4.6 답습) | ✅ §7 |
| 우선순위 권고 + 차단 요인 | ✅ §9 |
| 본 brief 영역 외 항목 분리 명시 (PC-4 T2 sub / T-5 α/γ / ST-2 inotify / ST-3 docker secret / Layer 2 runtime / 의미적 lock-in / Multi-host parity) | ✅ §1.3 |
| 7 backlog 中 본 brief 의 위치 명시 | ✅ §1.1 |
| **본 brief = 풀 3+1 합의 보고서 *작성 0건*** (합의 = 사용자 명시 후속 단계) | ✅ 헤더 + §0.4 + 부록 B |
| **실제 T3 영역 진입 0건** (사용자 명시 금지 #1) | ✅ |
| **branch protection rule 변경 0건** (사용자 명시 금지 #2) | ✅ |
| **dev 환경 강제 0건** (사용자 명시 금지 #3) | ✅ |
| **Hermes upstream Dockerfile 변경 0건** (사용자 명시 금지 #4) | ✅ |
| **Vault HSM 구현 0건** (사용자 명시 금지 #5) | ✅ |
| **Operational Readiness PASS (Layer E) 0건** (사용자 명시 금지 #6) | ✅ |
| **Hermes PMO 격상 (Layer F) 0건** (사용자 명시 금지 #7) | ✅ |
| Tier-2 / Tier-3 catalog 본문 확장 0건 (URL 10 / Model 19 / R-4.1 42 보존) | ✅ |
| T3 sub-영역 *수단 결정* / *도입* / *본문 채택 commit* 0건 | ✅ |
| 풀 3+1 합의 보고서 *작성* / commit / push 0건 | ✅ |
| 외부 LLM *자동 호출* 0건 (의뢰 형식 *권고 한정*) | ✅ |
| 실 API key / provider SDK / 외부 API 호출 / 실 secret 처리 0건 | ✅ |
| ADR 본문 자동 갱신 0건 (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012) | ✅ |
| §C-5 / §C-5b / §C-5c / §C-6 상태 표기 재변경 0건 (`78483c5` + `8ba5182` 권위 source 보존) | ✅ |
| Layer D 합의 보고서 (`210c98f`) 본문 변경 0건 (A-1 답습) | ✅ |
| §5.5 9 sub-수단 본문 채택 변경 0건 (Layer B `f40423f` 그대로 유지) | ✅ |
| `tools/*.py` 본문 변경 0건 | ✅ |
| `.importlinter` / `.pre-commit-config.yaml` / CI workflow 변경 0건 | ✅ |
| Production `docker-compose.yml` / Hermes upstream Dockerfile / requirements*.txt 변경 0건 | ✅ |
| Backlog #1 / #2 / #4 / #6 / #7 자동 진입 0건 | ✅ |
| MVP-1 PASS 재선언 0건 (Layer D `210c98f` 그대로 유지) | ✅ |
| MVP-2 자동 진입 0건 | ✅ |
| 5 영구 핵심 제약 5/5 보존 (Hermes ≠ root of trust / 수단-목적 분리 / 메타포 강제 금지 / 단일 source-of-truth / Provider Liquidity) | ✅ |
| Provider Liquidity 5-way 약화 0건 | ✅ |
| 사용자 명시 3 결정 (α/ii/(가)) 재변경 0건 | ✅ |
| ADR-011 §2.1 (a)~(e) / §2.4 답습 | ✅ |
| ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 / §2.6.2 R2-1 / R-4.1 답습 | ✅ |
| ADR-010 §2 답습 + §X 진입 의무 명시 (본문 변경 0건) | ✅ |
| mvp1.md §3.3 + §3.5 + §3.6 + §4.3 + §4.4 + §4.6 + §4.7 답습 | ✅ |
| Layer B `f40423f` Backlog #3 T3 영역 분리 명시 답습 | ✅ |

---

## 11. 본 brief 요약 (한 단락)

본 brief 는 **Backlog #3 (T3 영역) 풀 3+1 합의 *진입 전* 정비를 위한 *준비안* (DRAFT)** — 사용자 명시 검토 범위 6 sub-영역 통합: (1) AR-3 (AR-1 + AR-2 통합, branch protection rule), (2) T-5 (β) (provider URL/model Tier-2/3 catalog 확장 — GP-5 specific), (3) PC-4 T3 sub (`pre-commit install` 의무화 + dev 환경 강제), (4) C-5b ST-1 (Hermes upstream Dockerfile entrypoint stat chmod 600 강제), (5) Vault HSM ST-4 (ADR-010 통합), (6) Tier-2/3 catalog 자동 확장 가능성 *일반*. **6 sub-영역 모두 T3 영역 진입 의무 발화 — 풀 3+1 + 외부 LLM 1+ cross-vendor blind + 사용자 명시 의무 확정** (§8 7/7 트리거 #2 + #5 + #7 HIGH BLOCKING 발화 / R-MVP1-G3-7/8 + R-MVP1-G5-7/8/9 답습). **6 sub-영역 *결합 위험* / *책무 중첩* / *분리 가능성* 매트릭스** (§3): 15 페어 中 11 페어 ✅ 분리 가능 + 3 페어 ⚠️ 부분 분리 ((1)×(3) Defense in depth + (2)×(6) subset/superset + (4)×(5) 책무 분담) + 0 페어 분리 어려움 → **3 그룹 권고**: Group α (AR-3 + PC-4 T3 sub — enforcement/dev 환경 차단), Group β (T-5 β + Tier-2/3 일반 — catalog source 정책), Group γ (C-5b ST-1 + Vault HSM ST-4 — secret source/Hermes upstream). **합의 단위 권고** = (II) 3 그룹 분리 (3 합의) + **합의 형태 권고** = (가) 풀 3+1 + 외부 LLM 1+ cross-vendor blind + 사용자 명시. **풀 3+1 Agent A/B/C 관점 분배** (§5) = 3 그룹 각각 구현/안전성/대안 관점 분배 + **외부 LLM cross-vendor blind 의뢰 형식 + 핵심 질문 권고** (§6) = GPT + Gemini 2 vendor 의뢰 + 각 그룹 6 질문 권고. **Rollback Trigger 통합 매트릭스** (§7) = mvp1.md §3.5 + §4.6 답습 (R-MVP1-G3-7/8 + R-MVP1-G5-7/8/9 + R-1 + R-MVP1-G3-1/3 + R-MVP1-G3-3 8개 trigger 매핑). **우선순위 권고** (§9) = Group α (1순위) → Group β (2순위) → Group γ (3순위, Vault HSM ST-4 = Operational Readiness 영역 cross-reference). **차단 요인** (§9.3) = 외부 LLM 1+ 의뢰 발송 미실시 (HIGH) + Operational Readiness PASS 미발효 (HIGH — Group γ ST-4 의존) + Backlog #6 Runtime+CI-hook 미진입 (MEDIUM) + Implementation Evidence PASS 미발효 (MEDIUM — Group β baseline) + Backlog #1 미진입 (MEDIUM — Group γ ST-2 답습 의존) + C-14 11 조건 흡수 미완 (MEDIUM). **본 brief ≠ 합의 발효** + **§C-5/§C-5b/§C-5c/§C-6 재변경 0건** + **Layer D 본문 변경 0건** + **§5.5 9 sub-수단 본문 채택 변경 0건** + **실제 T3 영역 진입 0건** + **branch protection 변경 0건** + **dev 환경 강제 0건** + **Hermes upstream Dockerfile 변경 0건** + **Vault HSM 구현 0건** + **Operational Readiness PASS 0건** + **Hermes PMO 격상 0건** + **Tier-2/3 catalog 본문 확장 0건** + **풀 3+1 합의 보고서 작성 0건** + **외부 LLM 자동 호출 0건** + **ADR 본문 자동 갱신 0건** + **Backlog #1/#2/#4/#6/#7 자동 진입 0건** + **MVP-1 PASS 재선언 0건** + **MVP-2 자동 진입 0건**. 다음 단계 = 사용자 결정 영역 (부록 A 옵션 A~H).

---

## 부록 A. 다음 단계 결정 옵션 (사용자 결정 영역)

| 옵션 | 영역 | 후속 단계 |
|-----|------|--------|
| **(A)** | **본 brief 그대로 승인 → 파일화 + commit + push (`docs/phase0/backlog3-t3-zone-full-3plus1-brief.md`) → 사용자 명시 후속 단계 결정 영역** | 본 brief 파일화 + 메타 commit + push (2 commit chain — brief + 메타) |
| (B) | 본 brief 일부 수정 요청 → 수정 후 승인 | brief v2 작성 |
| (C) | 본 brief 그대로 승인 → 파일화 + commit *까지만* (push 보류) | 1 commit |
| (D) | 본 brief 그대로 승인 → Group α 풀 3+1 합의 *진입* (Agent A/B/C 발송 + 외부 LLM 2 vendor 의뢰 발송) | Group α 풀 3+1 진입 — 본 brief 답습 |
| (E) | 본 brief 그대로 승인 → Group β 풀 3+1 합의 *진입* (Agent A/B/C 발송 + 외부 LLM 2 vendor 의뢰 발송) | Group β 풀 3+1 진입 — 본 brief 답습 |
| (F) | 본 brief 그대로 승인 → Group γ 풀 3+1 합의 *진입* (Agent A/B/C 발송 + 외부 LLM 2 vendor 의뢰 발송) | Group γ 풀 3+1 진입 — 본 brief 답습 |
| (G) | 본 brief 보류 → Backlog #6 (Runtime + CI-hook implementation) 우선 진입 brief 작성 | MVP-1 Implementation Entry `1eab814` 권고 우선순위 1 답습 |
| (H) | 본 brief 보류 → MVP-2 진입 brief 작성 | 본 brief 의 후속으로 적합하지 않음 (Implementation Evidence PASS 미발효) |
| (I) | 본 brief 보류 → C-14 cross-vendor 11 핵심 조건 흡수 작업 우선 진입 | P2 v3 정식 채택 영역 — 별도 영역 |
| (J) | 본 brief 보류 → 세션 종료 | — |

### A.1 권고 시작 명령 (사용자 명시 결정 영역)

- (A) 시작 명령 후보: "옵션 (A) 로 진행해주세요. 본 brief 그대로 승인하고, `docs/phase0/backlog3-t3-zone-full-3plus1-brief.md` 파일화 + 메타 commit + push 까지 2-commit chain 으로 진행."
- (D) 시작 명령 후보 (Group α 우선 진입): "옵션 (D) 로 진행해주세요. 본 brief 답습 + Group α (AR-3 + PC-4 T3 sub) 풀 3+1 합의 진입. Agent A/B/C 발송 + 외부 LLM 2 vendor 의뢰 (GPT + Gemini) 발송 + Reviewer 검토 까지."
- (G) 시작 명령 후보 (Backlog #6 우선): "옵션 (G) 로 진행해주세요. 본 brief 보류 후 Backlog #6 (Runtime + CI-hook implementation) 우선 진입 brief 작성."

---

## 부록 B. 금지 사항 (사용자 명시 7 금지 + 추가 답습)

### B.1 사용자 명시 7 금지 답습 (이번 진입 명령)

| # | 금지 | 본 brief 위반 |
|---|------|------------|
| 1 | **실제 T3 영역 진입** | 0건 (본 brief = 합의 *준비안* — 합의 자체 0건 + commit 0건) |
| 2 | **branch protection rule 변경** (CODEOWNERS / required check / commit signing / merge restriction) | 0건 (AR-3 = 검토 영역, GitHub repo 정책 자동 변경 0건) |
| 3 | **dev 환경 강제** (`pre-commit install` 의무화 / `.git/hooks` 자동 install / 개발자 환경 정책) | 0건 (PC-4 T3 sub = 검토 영역) |
| 4 | **Hermes upstream Dockerfile 변경** (entrypoint stat / chmod 강제 / inotify 본문 흡수 / 실 image 빌드) | 0건 (C-5b ST-1 = 검토 영역, Hermes upstream PR 0건) |
| 5 | **Vault HSM 구현** (실 Vault 클라이언트 통합 / 실 HSM 환경 / ADR-010 §X 본문 변경 / 실 secret 이전) | 0건 (ST-4 = 검토 영역) |
| 6 | **Operational Readiness PASS (Layer E) 선언** | 0건 (MVP-6 + Backlog #7 별도 영역) |
| 7 | **Hermes PMO 격상 (Layer F) 선언** | 0건 (MVP-6 + 외부 LLM 2 또는 1+사람 리뷰 의무) |

### B.2 추가 금지 (본 brief 자체)

- ❌ Tier-2 / Tier-3 catalog *본문 확장* 0건 (URL 10 / Model 19 / R-4.1 42 보존)
- ❌ T3 sub-영역 *수단 결정* / *도입* / *본문 채택 commit* 0건
- ❌ 풀 3+1 합의 보고서 *작성* / commit / push 0건 (합의 = 사용자 명시 후속)
- ❌ Reviewer-only 단축 합의 적격성 발화 0건 (T3 영역 의무 — 풀 3+1 의무)
- ❌ 외부 LLM *자동 호출* / cross-vendor blind 의뢰 자동 발송 0건 (의뢰 형식 *권고 한정*)
- ❌ 실 API key / provider SDK / 외부 API 호출 / 실 secret 처리 0건
- ❌ ADR 본문 자동 갱신 0건 (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012)
- ❌ §C-5 / §C-5b / §C-5c / §C-6 상태 표기 *재변경* 0건 (`78483c5` + `8ba5182` 권위 source 보존)
- ❌ Layer D 합의 보고서 (`210c98f`) 본문 변경 0건 (A-1 답습)
- ❌ §5.5 9 sub-수단 본문 채택 변경 0건 (Layer B `f40423f` 그대로 유지)
- ❌ `tools/secret_scanner.py` / `tools/provider_*.py` / `tools/workflow_*.py` 본문 변경 0건
- ❌ `.importlinter` / `.pre-commit-config.yaml` 본문 변경 / 신규 hook 추가 0건
- ❌ CI workflow 변경 (secret-hygiene-egress-redaction.yml / provider-adapter-enforcement.yml / etc.) 0건
- ❌ Production `docker-compose.yml` / Hermes upstream Dockerfile / requirements*.txt 변경 0건
- ❌ Backlog #1 (GP-3 1.5차) / #2 (GP-5 1.5차) / #4 (P1 v2 facade MVP) / #6 (Runtime+CI-hook) / #7 (Operational Readiness) 자동 진입 0건
- ❌ MVP-1 PASS *재선언* 0건 (Layer D `210c98f` APPROVE WITH CONDITIONS 그대로 유지)
- ❌ MVP-2 자동 진입 0건 (Implementation Evidence PASS 미발효 + 사용자 명시 후속)
- ❌ 5 영구 핵심 제약 약화 / Provider Liquidity 5-way 약화 0건
- ❌ 사용자 명시 3 결정 (α/ii/(가)) *재변경* 0건 (PC-4 T2 sub Cycle 4 답습 한정)
- ❌ CONTEXT / INDEX / SESSION 메타 갱신 0건 (별도 commit 분리, 본 brief 파일화 commit 와 분리)
- ❌ ADR-010 §X 본문 신규 추가 / ADR-015 신설 0건 (Vault HSM ST-4 = 진입 *시점 검토* 한정)
- ❌ 인간 리뷰 의무 자동 발화 0건 (Hermes PMO 격상 시 의무 — 본 brief 영역 외)
- ❌ C-14 cross-vendor 11 핵심 조건 흡수 자동 진입 0건 (P2 v3 정식 채택 별도 영역)

---

**상태**: DRAFT (사용자 명시 승인 *전*, 파일화 + commit 0건)
**다음 단계**: 사용자 명시 결정 영역 (부록 A 옵션 A~J)
**주요 결정 필요 영역**:
- (a) **6 sub-영역 모두 T3 영역 진입 의무 발화** + **풀 3+1 + 외부 LLM 1+ + 사용자 명시 의무 확정** 적절성 확인
- (b) **합의 단위** = (II) 3 그룹 분리 vs (I) 단일 통합 vs (III) 6 분리 vs (IV)/(V)/(VI) 中 선택
- (c) **합의 형태** = (가) 풀 3+1 + 외부 LLM 1+ + 사용자 명시 적절성 확인 (T3 영역 의무 답습)
- (d) **3 그룹 책무 분할** = Group α (AR-3 + PC-4 T3 sub) + Group β (T-5 β + Tier-2/3 일반) + Group γ (C-5b ST-1 + Vault HSM ST-4) 적절성 확인
- (e) **Agent A/B/C 관점 분배** (§5.2 ~ §5.4) 적절성 확인 (3 그룹 각각)
- (f) **외부 LLM cross-vendor blind 의뢰 vendor** = GPT + Gemini 2 vendor 권고 적절성 확인 (의뢰 발송 = 사용자 명시 외부 LLM 호출, 자동 호출 0건)
- (g) **외부 LLM 의뢰 핵심 질문** (§6.5) 적절성 확인 (3 그룹 각각 6 질문)
- (h) **우선순위 권고** = Group α (1순위) → Group β (2순위) → Group γ (3순위) 적절성 확인
- (i) **차단 요인** (§9.3) — 외부 LLM 의뢰 미실시 / Operational Readiness PASS 미발효 / Backlog #6 미진입 / Implementation Evidence PASS 미발효 / Backlog #1 미진입 / C-14 11 조건 흡수 미완 解 적절성 확인
- (j) **후속 다음 단계 우선순위** = (I) 본 brief 그대로 승인 / (II) Backlog #6 우선 진입 / (III) Group α 풀 3+1 진입 / (IV) MVP-2 brief / (V) C-14 흡수 / (VI) 세션 종료 中 권고 영역 (사용자 결정 한정)
