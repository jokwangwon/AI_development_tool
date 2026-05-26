# Backlog #3 T3 영역 풀 3+1 합의 *준비* Brief v2 (DRAFT — 외부 LLM 응답 흡수)

> **본 brief v2 = v1 `ad9a02d` 의 *후속* — 외부 LLM cross-vendor blind 응답 2건 (`8b5b626` 회수, Gemini 3 Flash + GPT-5.5 Thinking) 의 지적 사항 8건 흡수** + **GPT 권고 Group γ 분리 (γ-1 ST-1 / γ-2 Vault HSM ST-4) 답습** + **양 vendor 수렴 정책 (audit-only / hard-block deferred / provider lock-in 역효과 완화) 흡수**. v1 본문 변경 0건 — v1 보존 + v2 = 별도 권위 source.
>
> 본 brief v2 의 어떤 §도 그 자체로 (i) **실제 T3 영역 진입**, (ii) **branch protection rule 변경** (CODEOWNERS / required check / commit signing / merge restriction / direct push 차단 / force push 차단 / admin bypass 정책), (iii) **dev 환경 강제** (`pre-commit install` 의무화 / `.git/hooks` 자동 install / 개발자 환경 정책), (iv) **Hermes upstream Dockerfile 변경** (entrypoint stat / chmod 강제 / inotify 본문 흡수 / 실 image 빌드), (v) **Vault HSM 구현** (실 Vault 클라이언트 통합 / 실 HSM 환경 / ADR-010 §X 본문 변경 / 실 secret 이전), (vi) **Operational Readiness PASS (Layer E) 선언**, (vii) **Hermes PMO 격상 (Layer F) 선언**, (viii) Tier-2 / Tier-3 catalog *본문 확장* (URL 10 / Model 19 / R-4.1 42 보존), (ix) 풀 3+1 합의 보고서 *작성* / commit / push, (x) 외부 LLM 추가 *자동 호출*, (xi) 실 API key / provider SDK / 외부 API 호출, (xii) ADR 본문 자동 갱신, (xiii) **v1 brief (`ad9a02d`) 본문 변경**, (xiv) §C-5 / §C-5b / §C-5c / §C-6 상태 표기 *재변경*, (xv) Layer D 합의 보고서 (`210c98f`) 본문 변경, (xvi) §5.5 9 sub-수단 본문 채택 변경, (xvii) Backlog #1 / #2 / #4 / #6 / #7 자동 진입 을 발생시키지 않는다.

**작성일**: 2026-05-14 후속 8
**상태**: DRAFT (사용자 명시 승인 *전*, 파일화 + commit 0건)
**관계**: v1 후속 — v1 본문 변경 0건 + v2 = 별도 권위 source (외부 LLM 응답 흡수 한정)
**상위 권위**:
- **외부 LLM 응답 회수** = `8b5b626 docs(review): record external responses for Backlog 3 T3 zone` (Gemini 3 Flash 114줄 + GPT-5.5 Thinking 390줄, 양 vendor 종합 = PARTIAL)
- **외부 LLM 검토 의뢰서** = `6a0ba21 docs(review): prepare external review for Backlog 3 T3 zone`
- **v1 prep brief** = `ad9a02d docs(phase0): add Backlog 3 T3 zone full consensus brief` (828줄 — 본 v2 가 흡수하는 base)
- Backlog #2 *잔여 5 항목* Deferred 유지 합의 = `8ba5182 docs(review): defer Backlog 2 GP-5 remaining items` (AR-3 + T-5 (β) Backlog #3 이관 명시)
- PC-4 T2 sub Partially Satisfied 합의 = `78483c5 docs(review): approve PC-4 T2 C-5c C-6 partial satisfaction`
- MVP-1 Implementation Entry = `1eab814 docs(review): approve MVP-1 implementation entry` (Backlog #6 우선순위 1)
- Backlog #6 Implementation Entry 합의 (Layer B) = `f40423f` (Backlog #3 T3 영역 분리 명시)
- ADR-010 (Vault HSM) — 본문 변경 0건 + §X 진입 의무 명시
- ADR-011 §2.4 T3 영역 분리 답습
- 5 영구 핵심 제약 + Provider Liquidity 5-way

---

## 0. 본 brief v2 의 범위

### 0.1 사용자 진입 명령 답습 (2026-05-14 후속 8)

> "(A) 후 (E) 로 진행해주세요. 외부 LLM 응답 2건을 먼저 commit/push. 그 다음 외부 지적 사항을 흡수한 Backlog #3 T3 prep brief v2 를 작성. 풀 3+1 합의와 T3 실제 진입은 아직 하지 않음."

### 0.2 본 brief v2 가 *하는* 것

1. v1 후속 정의 + v1 본문 변경 0건 명시 (§0.4)
2. 외부 LLM 응답 8 지적 사항 흡수 매트릭스 (§1)
3. GPT 권고 Group γ 분리 흡수 (§2.4 ↔ §2.5 책무 분리 강화) → **4 그룹화** (α / β / γ-1 / γ-2)
4. Group α 보강 (§2.1 + §3.1) — branch protection 세부 + AI agent/bot 권한 + CODEOWNERS 1인 한계
5. Group β 보강 (§2.2 + §2.6 + §3.2) — audit/warn-only 우선 + FP 비상 탈출구 + provider lock-in 역효과 완화책 + LiteLLM advisory only
6. Group γ-1 신설 (§2.4 + §3.3) — ST-1 downstream wrapper preflight 권고 (GPT) + dev warn / CI fail-closed 분리
7. Group γ-2 신설 (§2.5 + §3.4) — Vault HSM ST-4 = MVP-6 보류 + Operational Readiness 1인 개발자 정의 흡수
8. 4 그룹 결합 위험 / 분리 가능성 매트릭스 (§4)
9. 합의 *단위* 권고 v2 — (II') **4 그룹 분리** (§5.1)
10. 합의 *형태* 권고 — 풀 3+1 + 외부 LLM 1+ + 사용자 명시 (변경 0건) (§5.2)
11. Agent A/B/C 관점 분배 (4 그룹) (§6)
12. 외부 LLM 응답 양 vendor 수렴 합산 + 차이 영역 (§7)
13. Rollback Trigger 통합 매트릭스 (v1 §7 답습) + audit-first cycle 추가 (§8)
14. 7/7 풀 3+1 승격 트리거 재검증 — 4 그룹 *모두* 발화 (§9)
15. 우선순위 권고 v2 — α → β (policy/audit-only) → γ-1 (ST-1 downstream) → γ-2 (Vault HSM MVP-6+) (§10)
16. 메타 검증 (§11)
17. 요약 한 단락 (§12)
18. 다음 단계 결정 옵션 (부록 A)
19. 금지 사항 (부록 B)
20. **외부 LLM 응답 흡수 추적 매트릭스 (부록 C)** ⭐ 신규

### 0.3 본 brief v2 가 *하지 않는* 것 (사용자 명시 9 금지 + 추가)

| # | 금지 | 본 brief v2 위반 |
|---|------|------------|
| 1 | **내부 Agent A/B/C + Reviewer 풀 3+1 합의 보고서 작성** | 0건 (합의 = v2 작성 후 별도 사용자 승인) |
| 2 | **T3 영역 실제 진입** | 0건 (본 brief v2 = 합의 *준비안 v2* — 합의 자체 0건) |
| 3 | **branch protection rule 변경** | 0건 (Group α = 검토 영역) |
| 4 | **dev 환경 강제** (`pre-commit install` 의무화 / `.git/hooks` 자동 install) | 0건 (Group α PC-4 T3 sub = 검토 영역) |
| 5 | **Hermes upstream Dockerfile 변경** | 0건 (Group γ-1 = 검토 영역, downstream wrapper preflight 답습) |
| 6 | **Vault HSM 구현** | 0건 (Group γ-2 = MVP-6 보류 답습) |
| 7 | **Tier-2/3 catalog 본문 확장** (URL 10 / Model 19 / R-4.1 42 보존) | 0건 |
| 8 | **Operational Readiness PASS (Layer E) 선언** | 0건 (MVP-6 + Backlog #7 별도 영역) |
| 9 | **Hermes PMO 격상 (Layer F) 선언** | 0건 (MVP-6 + 외부 LLM 2 또는 1+사람 리뷰 의무) |
| (추가) | **v1 brief (`ad9a02d`) 본문 변경** | 0건 (v1 = 보존 / v2 = 별도 권위 source) |
| (추가) | T3 sub-영역 *수단 결정* / *도입* / *본문 채택 commit* | 0건 |
| (추가) | 외부 LLM *추가 자동 호출* / cross-vendor blind 의뢰 자동 재발송 | 0건 |
| (추가) | 실 API key / provider SDK / 외부 API 호출 / 실 secret 처리 | 0건 |
| (추가) | ADR 본문 자동 갱신 (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012) | 0건 |
| (추가) | §C-5 / §C-5b / §C-5c / §C-6 상태 표기 *재변경* | 0건 (`78483c5` + `8ba5182` 권위 source 보존) |
| (추가) | Layer D 합의 보고서 (`210c98f`) 본문 변경 | 0건 (A-1 답습) |
| (추가) | §5.5 9 sub-수단 본문 채택 변경 | 0건 (Layer B `f40423f` 그대로 유지) |
| (추가) | `tools/secret_scanner.py` / `tools/provider_*.py` 본문 변경 | 0건 |
| (추가) | `.importlinter` / `.pre-commit-config.yaml` 본문 변경 / 신규 hook 추가 | 0건 |
| (추가) | CI workflow 변경 | 0건 |
| (추가) | Production `docker-compose.yml` / Hermes upstream Dockerfile / requirements*.txt 변경 | 0건 |
| (추가) | Backlog #1 / #2 / #4 / #6 / #7 자동 진입 | 0건 |
| (추가) | MVP-1 PASS *재선언* | 0건 (Layer D `210c98f` 그대로 유지) |
| (추가) | MVP-2 자동 진입 | 0건 |
| (추가) | 5 영구 핵심 제약 약화 / Provider Liquidity 5-way 약화 | 0건 |
| (추가) | 외부 LLM 응답 *결론 강제 채택* (응답 = 입력 한정, 내부 풀 3+1 합의 시 평가 대상) | 0건 (응답 = *입력* 한정 보존) |

### 0.4 v1 ↔ v2 관계 + v1 본문 변경 0건 명시

| 영역 | v1 (`ad9a02d`) | v2 (본 문서) |
|------|------|------|
| 본문 변경 | ❌ 0건 (보존) | ⭐ 신규 (별도 권위 source) |
| 6 sub-영역 정의 | 그대로 답습 | 그대로 답습 + γ 분리 흡수 (책무 강화) |
| 그룹화 | 3 그룹 (α / β / γ) | **4 그룹 (α / β / γ-1 / γ-2)** ⭐ |
| 외부 LLM 응답 영역 | "응답 미수신, 의뢰 형식 권고" | "응답 2건 수신, 8 지적 흡수" ⭐ |
| 합의 단위 권고 | (II) 3 그룹 분리 | (II') **4 그룹 분리** ⭐ |
| 합의 형태 권고 | 풀 3+1 + 외부 LLM 1+ + 사용자 명시 | **변경 0건** (양 vendor 답습 후에도 동일) |
| 우선순위 권고 | α → β → γ | **α → β → γ-1 → γ-2** (audit-first 강화) ⭐ |
| Reviewer-only 단축 합의 적격 | 0/6 sub-영역 | **0/7** (γ 분리 후 sub-영역 7개) — 변경 0건 |

본 brief v2 = **v1 보존** + **외부 LLM 응답 흡수 한정**. v1 본문 변경 0건 (사용자 명시 답습 — v1 commit `ad9a02d` 권위 source 그대로 유지).

---

## 1. 외부 LLM 응답 8 지적 사항 흡수 매트릭스

### 1.1 양 vendor 응답 요약 (`8b5b626` 답습)

| Vendor | 종합 판정 | Group α | Group β | Group γ |
|--------|---------|---------|---------|---------|
| Gemini 3 Flash | (C) PARTIAL — α + β 진입 / γ 보류 | APPROVE (우선순위 1) | APPROVE WITH CONDITIONS (Evidence PASS 후) | 보류 (MVP-6 이후) |
| GPT-5.5 Thinking | (C) PARTIAL — α 우선 / β audit-only / γ-1·γ-2 분리 | APPROVE WITH CONDITIONS (Backlog #6 연결) | PARTIAL (audit-only) | **ST-1 vs ST-4 분리 권고** ⭐ |

**양 vendor 수렴**: PARTIAL 판정 + Group α 우선 + Group β audit-only + Vault HSM ST-4 MVP-6 보류 + provider lock-in 역효과 HIGH + Tier-2/3 자동 동기화 BLOCK.

### 1.2 8 지적 사항 흡수 매트릭스

| # | 지적 영역 | 출처 vendor | 흡수 위치 (본 v2) | 흡수 형태 |
|---|--------|---------|-----------|--------|
| 1 | AR-3 시 AI agent / bot / GitHub App 권한 범위 + 서명 방식 가이드 누락 | Gemini | §2.1.4 + §3.1.5 신설 | Group α 결정 영역 추가 |
| 2 | Group β FP 발생 시 비상 탈출구 (emergency escape hatch) 정책 부족 | Gemini | §2.2.4 + §2.6.4 + §3.2.4 신설 | Group β 결정 영역 추가 |
| 3 | branch protection 세부 (direct push / force push / admin bypass) 누락 | GPT | §2.1.3 + §3.1.3 신설 | Group α 결정 영역 추가 |
| 4 | GitHub plan / 권한 제약 (private repo / branch protection / ruleset / required reviewers 가용성) 누락 | GPT | §2.1.5 + §3.1.6 신설 | Group α 결정 영역 추가 |
| 5 | CODEOWNERS 1인 한계 명시 — "독립 리뷰" 아닌 "중요 변경 재확인 friction" | GPT | §2.1.3 + §3.1.4 + §11 흡수 | Group α 결정 영역 + 메타 답습 |
| 6 | Tier-2/3 catalog 예외 경로 (allowlist / expiry / adapter stub generator) 부족 | GPT | §2.2.4 + §2.6.4 + §3.2.3 신설 | Group β 결정 영역 추가 |
| 7 | **Group γ 과도 묶음 — ST-1 (작은 file perm) vs ST-4 (큰 인프라/PMO) 위험 규모 다름** | GPT | **§2.4 ↔ §2.5 책무 분리 강화 + 그룹화 (II') 4 그룹 답습** | **그룹화 구조 변경** ⭐ |
| 8 | Operational Readiness 1인 개발자 기준 정의 필요 — enterprise HA 아닌 rotation / backup / restore / audit / fallback | GPT | §2.5.4 + §3.4.4 신설 | Group γ-2 결정 영역 + 메타 답습 |

**합산**: **8/8 지적 흡수** — 본 v2 가 발생시키는 핵심 효과.

### 1.3 양 vendor 추가 수렴 권고 흡수 (gap 외 영역)

| 영역 | 양 vendor 수렴 | 흡수 위치 (본 v2) |
|----|----|----|
| commit signing 의무화 시점 | MVP-6 권고 (1인 GPG/SSH 운영 비용 高) | §2.1.3 + §10.3 |
| fork PR / `pull_request_target` 도입 | BLOCK (default 보수적 정책 유지) | §2.1.6 |
| Tier-2/3 catalog 자동 동기화 | BLOCK (LiteLLM advisory only) | §2.6.4 |
| provider lock-in 강화 역효과 | 실재 HIGH 위험 — 완화책 필수 | §2.2.5 + §2.6.5 |
| hard-block vs audit-only 분리 | audit-first → Evidence PASS 후 hard-block | §2.2.4 + §2.6.4 + §10.3 |
| Vault HSM ST-4 진입 시점 | MVP-6 Operational Readiness 발효 후 | §2.5.4 + §3.4 |
| `--no-verify` 차단 | 로컬 pre-commit 단독 불가 / branch protection + required CI 결합 필수 | §2.3.4 + §3.1.7 |
| AR-3 × PC-4 결합 효과 | 양쪽 결합 = 유일하게 유효한 차단책 | §3.1.7 + §4.2 |

---

## 2. 6 sub-영역 검토 (v1 §2 답습 + 외부 LLM 응답 흡수)

### 2.1 (1) AR-3 (AR-1 + AR-2 통합 — branch protection rule) — *v1 §2.1 + 외부 LLM 흡수*

#### 2.1.1 v1 답습 (변경 0건)

v1 §2.1 정의 + T3 진입 속성 매트릭스 그대로 답습. 본 §은 외부 LLM 응답 흡수에 의한 *결정 영역 추가* 한정.

#### 2.1.2 외부 LLM 응답 합산

| Vendor | 권고 |
|------|----|
| Gemini Q1 | (g) (a)+(b)+(c)+(d) 통합 — Provider Liquidity 보존 + Hermes ≠ root of trust 강화 + 메타-슬로건 충실 |
| GPT Q1 | (e) CODEOWNERS + required status check (commit signing 후속) — 1인 환경 균형 권고 |
| **수렴** | required status check = 우회 차단의 중심 (양쪽 동의) / commit signing 시점 = 양쪽 후순위 권고 |
| **차이** | Gemini = 완전 통합 (g) / GPT = 단계적 (e → 후속) |

#### 2.1.3 *추가* 결정 영역 (외부 LLM 흡수 — Gap #3 + #5)

| 결정 | 옵션 후보 (v2 신규 흡수) |
|----|------|
| **branch protection 세부 정책** (Gap #3) | (i) direct push 차단 / (ii) force push 차단 / (iii) admin bypass 허용 여부 / (iv) required PR review count (1인 = 0 또는 self-review 허용) / (v) required linear history / (vi) required deployments |
| **CODEOWNERS 적용 범위** (Gap #5) | (a) 전체 repo / **(b) 핵심 경로 한정** (`docs/decisions/**` / `tools/**` / `.github/workflows/**` / `.pre-commit-config.yaml` / catalog 파일) ⭐ GPT 권고 |
| **CODEOWNERS 의미** (Gap #5) | "독립 리뷰" 아닌 **"중요 변경 재확인 friction"** ⭐ — 1인 개발자 환경 명시 |

#### 2.1.4 *추가* 결정 영역 (외부 LLM 흡수 — Gap #1)

| 결정 | 옵션 후보 |
|----|------|
| **AI agent / bot / GitHub App 권한 범위** (Gap #1) | (a) bot 계정 별도 / (b) GitHub App (예: Claude Code App) 한정 / (c) personal token + 권한 최소화 / (d) bot 계정 + GitHub App 결합 |
| **AI agent 서명 방식** | (i) bot 계정 GPG signing / (ii) bot 계정 SSH signing / (iii) GitHub App auto-sign / (iv) commit signing 미적용 (commit signing 의무화 시점에 결합) |
| **bot 권한 영역 분리** | (α) `tools/**` write only / (β) `docs/**` write only / (γ) 전체 write + required status check 차단 |

#### 2.1.5 *추가* 결정 영역 (외부 LLM 흡수 — Gap #4)

| 결정 | 옵션 후보 |
|----|------|
| **GitHub plan 가용성** (Gap #4) | (a) private repo + free plan = branch protection 제한 / (b) private repo + paid plan = 전체 가능 / (c) public repo = 전체 가능 / **(d) 현 plan 확인 후 옵션 가용성 명시** ⭐ |
| **ruleset (branch protection 후속)** | (i) Repository ruleset 도입 / (ii) Organization ruleset 도입 / (iii) default branch protection 한정 |
| **required reviewers** | (1) 1인 = self-review 허용 (limited) / (2) 1인 = 0 reviewer (PR auto-merge) / (3) bot 계정 reviewer 도입 |

#### 2.1.6 v1 §2.1.3 결정 영역 + 양 vendor 수렴 답습

| v1 결정 | v2 수렴 권고 (양 vendor 답습) |
|----|----|
| AR-2 본문 형태 | required status check **중심** (양 vendor 동의) + CODEOWNERS 핵심 경로 한정 (GPT 권고) |
| AR-1 + AR-2 통합 형태 | (ii) AR-1 + AR-2 (e) = required check + CODEOWNERS (GPT 권고) — Gemini (g) 통합은 후속 |
| Hermes-originated commit auto-reject 통합 | (β) Group I 별도 합의 분리 — 양 vendor 답습 0건 (분리 영역) |
| commit signing 의무화 시점 | (Y) **Operational Readiness 발효 시 (MVP-6) — 양 vendor 수렴** ⭐ |
| fork PR / external contributor 정책 | **(3) 현 default 정책 유지 (`secrets`= fork PR 차단)** + `pull_request_target` 도입 **BLOCK** — 양 vendor 수렴 ⭐ |

#### 2.1.7 §2.1 판정 v2

⚠️ **AR-3 = T3 영역 진입 BLOCKING + 풀 3+1 + 외부 LLM 1+ + 사용자 명시 의무 발화** (v1 §2.1.4 답습). **추가**: 양 vendor 권고 답습 — required status check 중심 + CODEOWNERS 핵심 경로 한정 + commit signing 후속 (MVP-6) + fork PR `pull_request_target` BLOCK. **AI agent / bot 권한 범위 + branch protection 세부 + GitHub plan 가용성 추가 결정 영역 흡수 완료**.

### 2.2 (2) T-5 (β) — provider URL/model name Tier-2/3 catalog 확장 (GP-5) — *v1 §2.2 + 외부 LLM 흡수*

#### 2.2.1 v1 답습 (변경 0건)

v1 §2.2 정의 + T3 진입 속성 매트릭스 그대로 답습.

#### 2.2.2 외부 LLM 응답 합산

| Vendor | 권고 |
|------|----|
| Gemini Q8 | Tier-2 확장 (Mistral / AI21 / HuggingFace 포함) + Tier-3 보류 |
| GPT Q8 | **Tier-2 URL/model hard-block 확장 0건** + Tier-2 후보 audit-only 등록 |
| **수렴** | Tier-1 보존 + Tier-3 보류 (양 vendor 동의) / Mistral 후보 양 vendor 동의 |
| **차이** | Gemini = Tier-2 hard-block 적극 / **GPT = Tier-2 hard-block BLOCK + audit-only 우선** ⭐ |

**본 v2 권고**: **GPT 권고 답습** (audit-only 우선) — 보수적 + Implementation Evidence PASS 의존 답습.

#### 2.2.3 *추가* 결정 영역 (양 vendor 수렴 흡수)

| 결정 | v2 권고 |
|----|----|
| Tier 강도 분리 (양 vendor 수렴) | **Tier-1 = hard-block / Tier-2 = audit/warn-only (시작) / Tier-3 = observe-only 또는 후보군 문서** ⭐ |
| Tier-2 hard-block 승격 조건 | **Implementation Evidence PASS 발효 후** (실 src/ FP/FN baseline 후) — 양 vendor 수렴 |
| Tier-2 후보 (양 vendor 동의) | Mistral (양쪽), HuggingFace (Gemini), AI21 (양쪽) |
| Tier-2 후보 (GPT 추가) | Stability (image model 범위 별도 정의 필요) — 별도 합의 |
| Tier-2 보류 (GPT 권고) | Inflection / Aleph Alpha (실 사용 가능성 낮음 → Tier-3 observe-only) |

#### 2.2.4 *추가* 결정 영역 (외부 LLM 흡수 — Gap #2 + #6)

| 결정 | 옵션 후보 (v2 신규 흡수) |
|----|------|
| **FP 비상 탈출구 (emergency escape hatch)** (Gap #2 — Gemini) | (i) `# scanner-allow: <reason>` line comment / (ii) `provider_catalog_allowlist.yaml` 파일 / (iii) ADR-011 위반 없이 긴급 bypass 정책 / **(iv) (i) + (ii) 통합 + expiry date 의무 + owner / rationale 의무** ⭐ GPT 권고 답습 |
| **catalog 예외 경로 정책** (Gap #6 — GPT) | (a) allowlist (`src/providers/**` 또는 공식 adapter 경로 = allowlist) / (b) 실험 디렉터리 (`experiments/**` = audit-only) / (c) expiry exception (예외 = 1 cycle 후 자동 만료) / (d) adapter stub generator (신규 provider 도입 시 stub 자동 생성) |
| **catalog 변경 시 의무 evidence** | provenance + rationale + test fixture + allowlist (GPT 권고 답습) |

#### 2.2.5 *provider lock-in 강화 역효과 완화책* (양 vendor 수렴 흡수)

| Vendor 권고 | 본 v2 흡수 |
|----------|----|
| Gemini: "Sandboxed Tier" (T1 영역) | T-5 강화 시 별도 T1 영역 = 신규 vendor 한시 허용 + 검증 후 catalog 편입 |
| GPT: 6 완화책 통합 | (i) `src/providers/**` allowlist / (ii) `experiments/**` audit-only / (iii) Tier-2 최소 1 cycle warn-only / (iv) 예외 = expiry + owner / (v) 새 provider 도입 시 adapter stub generator / (vi) 차단 메시지 = "어디에 adapter 만들면 되는지" 안내 |
| **본 v2 권고** | **양 vendor 통합 흡수** — Sandboxed Tier (T1) + 6 완화책 모두 풀 3+1 합의 시 결정 영역 |

#### 2.2.6 §2.2 판정 v2

⚠️ **T-5 (β) = T3 영역 진입 + 풀 3+1 + 외부 LLM 1+ + 사용자 명시 의무 발화** (v1 §2.2.4 답습). **추가**: 양 vendor 수렴 — **Tier-2 hard-block 확장 0건 (audit-only 우선)** + Tier-3 보류 + Tier-2 후보 Mistral / AI21 (양 동의) + **FP 비상 탈출구 + catalog 예외 경로 + provider lock-in 역효과 완화책 흡수 완료**.

### 2.3 (3) PC-4 T3 sub — `pre-commit install` 의무화 + dev 환경 강제 — *v1 §2.3 + 외부 LLM 흡수*

#### 2.3.1 v1 답습 (변경 0건)

v1 §2.3 정의 + T3 진입 속성 매트릭스 그대로 답습.

#### 2.3.2 외부 LLM 응답 합산

| Vendor | 권고 |
|------|----|
| Gemini Q2 | `fail_fast: true` + `commit-msg/pre-push` + `--no-verify` 차단 (서버사이드 결합) |
| GPT Q2 | `pre-commit install` = README + bootstrap script + doctor check / `default_install_hook_types` = `pre-commit` + `commit-msg` 중심 / `pre-push` = 빠른 smoke check only / `fail_fast` = 로컬 true + CI 별도 / `minimum_pre_commit_version` 명시 / `--no-verify` 차단 = branch protection 보완 |
| **수렴** | `--no-verify` 차단은 로컬 단독 불가 (양 vendor 동의) / branch protection + required CI 결합 필수 (양 vendor 동의) |
| **차이** | Gemini = 즉시 강제 / **GPT = 단계적 (opt-in → doctor warning → required check)** ⭐ |

#### 2.3.3 *추가* 결정 영역 (양 vendor 수렴 흡수)

| 결정 | v2 권고 |
|----|----|
| `pre-commit install` 강제 형태 | **(GPT 권고) 단계적: opt-in → doctor warning → required check** ⭐ (즉시 강제 BLOCK) |
| `default_install_hook_types` | `pre-commit` + `commit-msg` 중심 (GPT 권고 답습) / `pre-push` = smoke check only |
| `fail_fast` | **로컬 = true (Gemini 권고)** / CI = 전체 리포트 (GPT 권고 — 별도 설계) |
| `minimum_pre_commit_version` | **명시 (현 4.6.0 답습 — GPT 권고)** |
| 로컬 hook 실패 시 정책 | "빠른 실패 + 명확한 복구 명령" (GPT 권고) — 개발 차단 회피 |
| `--no-verify` 차단 | **branch protection + required CI 보완** (양 vendor 수렴) — 로컬 단독 차단 시도 BLOCK |

#### 2.3.4 §2.3 판정 v2

⚠️ **PC-4 T3 sub = T3 영역 진입 + 풀 3+1 + 사용자 명시 의무 발화** (v1 §2.3.4 답습). **추가**: 양 vendor 수렴 — `pre-commit install` 단계적 (opt-in → doctor → required) + `--no-verify` 차단 = branch protection 보완 (AR-3 dependence 강화). **AR-3 와 cross-reference 확정** — Defense in depth = 유일하게 유효한 차단책 (양 vendor 수렴).

### 2.4 (4) C-5b ST-1 — Hermes upstream Dockerfile entrypoint stat chmod 600 강제 — *v1 §2.4 + 외부 LLM 흡수 + Group γ-1 신설 답습*

#### 2.4.1 v1 답습 (변경 0건)

v1 §2.4 정의 + T3 진입 속성 매트릭스 그대로 답습.

#### 2.4.2 외부 LLM 응답 합산

| Vendor | 권고 |
|------|----|
| Gemini Q13 | entrypoint 내 chmod 600 검증 (실패 시 즉시 중지) — Dockerfile layer 추가 검증 = 1인 부담 ↓ 대안 |
| GPT Q13 | **Hermes upstream 직접 수정 BLOCK** + **downstream wrapper / entrypoint preflight / CI container test 우선** ⭐ — dev = warning / CI = fail-closed |
| **수렴** | Hermes 자기 자신 검증 → "안전" 아님 (양 vendor 동의 — Hermes ≠ root of trust 답습) |
| **차이** | Gemini = entrypoint 변경 (단순) / **GPT = downstream wrapper 우선 + upstream PR 후속 (downstream evidence 확보 후 최소 패치)** ⭐ |

**본 v2 권고**: **GPT 권고 답습** (downstream wrapper preflight 우선) — Hermes ≠ root of trust 보존 강화.

#### 2.4.3 *추가* 결정 영역 (양 vendor 수렴 흡수)

| 결정 | v2 권고 |
|----|----|
| ST-1 진입 형태 | **(GPT 권고) downstream wrapper / entrypoint preflight / CI container test** ⭐ — Hermes upstream 직접 수정 BLOCK |
| 환경별 동작 | **(GPT 권고) dev = warning + 복구 안내 / CI = fail-closed** ⭐ |
| 위반 메시지 형식 | 어떤 파일이 어떤 permission 이어야 하는지 명시 |
| Hermes upstream PR 시점 | **downstream evidence 확보 후 최소 패치 권고** (GPT 권고) |
| Hermes 자기 검증 ≠ "안전" | **검증 주체 = 외부 harness (Hermes container 행동 검증)** — 양 vendor 수렴 |

#### 2.4.4 v1 §2.4.3 결정 영역 + 양 vendor 수렴 답습

| v1 결정 | v2 수렴 권고 (양 vendor 답습) |
|----|----|
| ST-1 진입 시점 | (a) MVP-1 1.5차 (downstream wrapper preflight 형태) — GPT 권고 |
| Hermes upstream PR 절차 | **(iii) fork + downstream patch (Hermes upstream 변경 0건 유지)** ⭐ — GPT 권고 |
| chmod 강제 형태 | (X) entrypoint script 단독 (downstream wrapper 형식) |
| 위반 시 동작 | **(1) dev = warning + (X) CI = `exit 1`** ⭐ — GPT 권고 (환경별 분리) |
| ST-2 / ST-3 와 통합 | **(γ) ST-1 + ST-3 부분 통합 (Layer B 답습 — ST-3 본문 채택)** — GPT 권고 (ST-2 = Backlog #1 영역) |
| Vault HSM ST-4 와 책무 분담 | **(P) ST-1 (file system perm) + ST-4 (HSM secret source) 분리** ⭐ — 양 vendor 수렴 → **그룹화 (II') γ 분리 답습** |

#### 2.4.5 §2.4 판정 v2

⚠️ **C-5b ST-1 = T3 영역 진입 + Hermes upstream 변경 + 풀 3+1 + 외부 LLM 1+ + 사용자 명시 의무 발화** (v1 §2.4.4 답습). **추가**: GPT 권고 답습 — **downstream wrapper preflight 우선** (Hermes upstream 직접 수정 BLOCK) + 환경별 분리 (dev warning / CI fail-closed) + Hermes 자기 검증 ≠ "안전" (양 vendor 수렴). **Group γ 분리 답습** → Group γ-1 으로 흡수.

### 2.5 (5) Vault HSM ST-4 — ADR-010 통합 — *v1 §2.5 + 외부 LLM 흡수 + Group γ-2 신설 답습*

#### 2.5.1 v1 답습 (변경 0건)

v1 §2.5 정의 + T3 진입 속성 매트릭스 그대로 답습.

#### 2.5.2 외부 LLM 응답 합산

| Vendor | 권고 |
|------|----|
| Gemini Q14 | 현 시점 도입 보류 (MVP-6 이후 재검토) — single-host + SPOF 의도적 수용 (ADR-012) 답습 |
| GPT Q14 | **BLOCK / DEFER** — single-host 부적합 + Vault Enterprise / HCP Vault Dedicated 요구 |
| **수렴** | MVP-6 이후 + 1인 single-host 환경 부적합 (양 vendor 동의) ⭐ |
| **차이** | (없음 — 양 vendor 완전 수렴) |

**본 v2 권고**: **양 vendor 수렴 답습** — Vault HSM ST-4 = MVP-6 Operational Readiness 발효 후 진입 + 본 brief 영역에서 *진입 결정 0건*.

#### 2.5.3 *추가* 결정 영역 (양 vendor 수렴 흡수)

| 결정 | v2 권고 |
|----|----|
| ST-4 진입 시점 | **(b) MVP-6 Operational Readiness 발효 시 (양 vendor 수렴)** ⭐ — MVP-2 조기 진입 BLOCK + Hermes PMO 격상 후만은 너무 늦음 |
| ST-1 / ST-4 책무 분담 | **(P) 분리** (ST-1 = file perm preflight, ST-4 = production-grade root secret source) — GPT 권고 |
| 1인 환경에서의 핵심 | **HSM 보다 secret 파일 권한 / docker secret / audit log / backup·restore / rotation 절차** ⭐ — GPT 권고 |

#### 2.5.4 *추가* 결정 영역 (외부 LLM 흡수 — Gap #8)

| 결정 | 옵션 후보 (v2 신규 흡수) |
|----|------|
| **Operational Readiness 1인 개발자 정의** (Gap #8 — GPT) | enterprise HA ≠ Operational Readiness / **1인 개발자 기준 = (i) secret rotation 가능 / (ii) backup·restore 가능 / (iii) Vault 장애 시 fallback 정책 / (iv) audit log 확인 가능 / (v) 비용·복구 절차 감당 가능 / (vi) single-host SPOF 수용 범위 문서화** ⭐ |
| **single-host SPOF 의도적 수용 답습** (ADR-012 §2.8 답습) | ST-4 = "지금 해야 할 보안" 아님 / **"운영 단계 전환 신호"** ⭐ — GPT 권고 |

#### 2.5.5 §2.5 판정 v2

⚠️ **Vault HSM ST-4 = T3 영역 진입 + ADR-010 §X 본문 진입 + Multi-host 인프라 + 풀 3+1 + 외부 LLM 1+ + 사용자 명시 의무 발화** (v1 §2.5.4 답습). **추가**: 양 vendor 수렴 완전 — **MVP-6 보류 + 1인 single-host 부적합 + Operational Readiness 1인 정의 (6 기준) 흡수 완료**. **Group γ 분리 답습** → Group γ-2 으로 흡수.

### 2.6 (6) Tier-2/3 catalog 자동 확장 *가능성 일반* — *v1 §2.6 + 외부 LLM 흡수*

#### 2.6.1 v1 답습 (변경 0건)

v1 §2.6 정의 + T3 진입 속성 매트릭스 그대로 답습.

#### 2.6.2 외부 LLM 응답 합산

| Vendor | 권고 |
|------|----|
| Gemini Q7 | YAML 기반 자체 catalog + 수동 트리거 업데이트 / 자동 동기화 = 제어 어려움 |
| GPT Q7 | **자동 확장 금지** + **수동 curated catalog + audit-first** ⭐ — Tier-1 hard-block / Tier-2 audit/warn-only / Tier-3 observe-only |
| Gemini Q9 | 자체 catalog 유지 (LiteLLM 참조용) |
| GPT Q9 | **BLOCK for auto-sync** + APPROVE for advisory snapshot — 자동 PR 가능 + 자동 merge / hard-block BLOCK |
| **수렴** | 자체 catalog 단일 source-of-truth + LiteLLM = advisory only + audit-first 우선 (양 vendor 수렴) ⭐ |

#### 2.6.3 *추가* 결정 영역 (양 vendor 수렴 흡수)

| 결정 | v2 권고 |
|----|----|
| Tier 강도 정책 | **Tier-1 = hard-block / Tier-2 = audit/warn-only 시작 / Tier-3 = observe-only 또는 문서 후보군** ⭐ |
| catalog 본문 형식 | **별도 `yaml/json` manifest 권고** (도구 코드 내장 보다) — GPT 권고 |
| catalog 변경 시 의무 | **provenance + rationale + test fixture + allowlist** ⭐ — GPT 권고 |
| hard-block 승격 시점 | **Implementation Evidence PASS 이후** — 양 vendor 수렴 |
| LiteLLM 자동 동기화 | **BLOCK** ⭐ — 양 vendor 수렴 |
| LiteLLM 사용 형태 | **advisory input only + 자동 PR 가능 + 자동 merge / hard-block BLOCK** ⭐ — GPT 권고 |
| vendor rename / deprecation 대응 | **별도 changelog + fixture 의무** — GPT 권고 |

#### 2.6.4 *추가* 결정 영역 (외부 LLM 흡수 — Gap #2 + #6, T-5 (β) 와 통합)

§2.2.4 답습 (Group β 통합 영역) — FP 비상 탈출구 + catalog 예외 경로 = T-5 (β) 와 Tier-2/3 일반 모두 적용.

#### 2.6.5 *provider lock-in 강화 역효과 완화책* (T-5 (β) 와 통합)

§2.2.5 답습.

#### 2.6.6 §2.6 판정 v2

⚠️ **Tier-2/3 catalog 자동 확장 *가능성 일반* = T3 영역 진입 + 풀 3+1 + 외부 LLM 1+ + 사용자 명시 의무 발화** (v1 §2.6.5 답습). **추가**: 양 vendor 수렴 — **자동 확장 BLOCK + 수동 curated + audit-first + LiteLLM advisory only + Tier 강도 정책 (hard / audit / observe)** ⭐ + Group β T-5 (β) 와 통합 결정 영역.

---

## 3. 4 그룹화 (II') 답습 — Group γ 분리 흡수

### 3.1 Group α (AR-3 + PC-4 T3 sub) — v1 §3.4 + 외부 LLM 흡수

#### 3.1.1 책무 정의 (v1 답습)

enforcement / dev 환경 차단 layer — `--no-verify` 우회 차단 Defense in depth.

#### 3.1.2 핵심 결합 위험 (v1 §3.2 답습)

`--no-verify` 우회 차단 = AR-3 + PC-4 T3 sub 모두 의존 (Defense in depth).

#### 3.1.3 v2 추가 — branch protection 세부 결정 (Gap #3)

| 옵션 | 설명 |
|----|----|
| direct push 차단 | default branch 직접 push 차단 (PR 의무화) |
| force push 차단 | force-with-lease / force 차단 (history 무결성 보존) |
| admin bypass 허용 | admin = branch protection 우회 가능 여부 (1인 = self admin 위험) |
| required linear history | merge commit 차단 (rebase only) |
| required deployments | 배포 환경 통과 의무 (단계 환경 통과 시 merge) |

#### 3.1.4 v2 추가 — CODEOWNERS 1인 한계 (Gap #5)

| 영역 | 1인 개발자 환경 의미 |
|----|----|
| "독립 리뷰" | ❌ 1인 = self-review 불가 또는 self-review 의미 약화 |
| **"중요 변경 재확인 friction"** | ✅ 1인 환경에서도 의미 — 핵심 경로 변경 시 다시 보게 만드는 friction |
| 적용 범위 | 전체 repo 적용 = 의미 약화 / **핵심 경로 한정 (GPT 권고)** ⭐ |

#### 3.1.5 v2 추가 — AI agent / bot / GitHub App 권한 범위 (Gap #1)

§2.1.4 답습 — bot 계정 / GitHub App / personal token 옵션 + 서명 방식 + 권한 영역 분리.

#### 3.1.6 v2 추가 — GitHub plan / 권한 제약 (Gap #4)

§2.1.5 답습 — private repo + plan 종류 별 branch protection / ruleset / required reviewers 가용성.

#### 3.1.7 v2 추가 — `--no-verify` 차단 = 양 vendor 수렴 권고

| 형태 | 우회 차단 강도 |
|----|----|
| pre-commit 단독 | 가장 약함 (`--no-verify` 우회 가능) |
| branch protection + required CI 단독 | 핵심 방어선 (로컬 우회와 무관하게 merge 차단) |
| **pre-commit + branch protection 결합** | **가장 강함** ⭐ — 양 vendor 수렴 |

**잔존 우회**: admin bypass, force push 허용, required check 미등록, GitHub token 탈취, workflow 자체 변조 — §3.1.3 답습 권고로 완화.

### 3.2 Group β (T-5 (β) + Tier-2/3 일반) — v1 §3.4 + 외부 LLM 흡수

#### 3.2.1 책무 정의 (v1 답습)

catalog source 정책 — subset (T-5 β) / superset (Tier-2/3 일반) 관계.

#### 3.2.2 핵심 결합 위험 (v1 §3.2 답습)

T-5 (β) ⊂ Tier-2/3 일반 정책 — 동시 결정 권고.

#### 3.2.3 v2 추가 — catalog 예외 경로 (Gap #6)

§2.2.4 답습 — allowlist + 실험 디렉터리 + expiry exception + adapter stub generator + 의무 evidence.

#### 3.2.4 v2 추가 — FP 비상 탈출구 (Gap #2)

§2.2.4 답습 — `# scanner-allow: <reason>` + `provider_catalog_allowlist.yaml` + expiry date + owner / rationale 의무.

#### 3.2.5 v2 추가 — provider lock-in 강화 역효과 완화책

§2.2.5 답습 — Sandboxed Tier (T1) + 6 완화책 (allowlist / 실험 / 1 cycle warn / expiry / stub generator / 안내 메시지).

### 3.3 Group γ-1 (C-5b ST-1) — *신설* (GPT 권고 답습 — Group γ 분리)

#### 3.3.1 책무 정의

**file permission preflight guard** — Hermes upstream 변경 *최소화* (downstream wrapper 우선) + Hermes ≠ root of trust 보존 강화.

#### 3.3.2 핵심 결정 영역

§2.4 답습 — downstream wrapper / entrypoint preflight / CI container test + 환경별 분리 (dev warning / CI fail-closed) + Hermes upstream PR = downstream evidence 확보 후 최소 패치.

#### 3.3.3 분리 사유 (GPT 권고 답습)

ST-1 = **작은** file permission guard (비용 低, 위험 규모 中) ↔ ST-4 = **큰** 인프라 / 운영 / Vault HSM / PMO 경계 (비용 高, 위험 규모 高). **둘을 같은 합의 단위로 묶으면**:
- ST-1 까지 불필요하게 지연
- ST-4 가 너무 빨리 끌려올 위험

→ Group γ 분리 권고 = **본 v2 핵심 흡수 영역** ⭐.

#### 3.3.4 진입 시점 권고 (양 vendor 수렴)

- **MVP-1 1.5차 진입 가능** (downstream wrapper 형태) — Hermes upstream PR 미진입
- Hermes upstream PR = downstream evidence 확보 후 별도 합의

### 3.4 Group γ-2 (Vault HSM ST-4) — *신설* (GPT 권고 답습 — Group γ 분리)

#### 3.4.1 책무 정의

**production-grade root secret source** (multi-host / HSM 기반) — single-host 환경 부적합 + Operational Readiness 발효 의존 (MVP-6).

#### 3.4.2 핵심 결정 영역

§2.5 답습 — MVP-6 Operational Readiness 발효 시 진입 + ST-1 / ST-4 책무 분담 (분리) + 1인 환경에서는 HSM 보다 secret 파일 권한 / docker secret / audit log / backup·restore / rotation 우선.

#### 3.4.3 v2 추가 — Operational Readiness 1인 개발자 정의 (Gap #8)

§2.5.4 답습 — enterprise HA ≠ Operational Readiness / 1인 개발자 6 기준 (rotation / backup·restore / fallback / audit log / 비용·복구 / single-host SPOF 수용 범위 문서화).

#### 3.4.4 진입 시점 권고 (양 vendor 완전 수렴)

- **MVP-1 1.5차 진입 BLOCK** (1인 single-host 부적합)
- **MVP-6 Operational Readiness 발효 시 진입** (양 vendor 수렴) — Multi-host 전환 시점 또는 PMO 격상 조건 검토 시
- Hermes PMO 격상 후만 미루는 것은 너무 늦음 (GPT 권고)

### 3.5 4 그룹 결합 위험 / 책무 분리 매트릭스 (v1 §3.2 답습 + γ 분리 반영)

| 페어 | 결합 위험 | 분리 가능성 |
|----|-------|---------|
| Group α × Group β | 책무 영역 다름 (enforcement vs catalog) | ✅ 분리 가능 |
| Group α × Group γ-1 | 책무 영역 다름 (GitHub repo vs Hermes upstream) | ✅ 분리 가능 |
| Group α × Group γ-2 | 책무 영역 다름 (GitHub repo vs HSM) | ✅ 분리 가능 |
| Group β × Group γ-1 | 책무 영역 다름 (catalog vs Hermes upstream) | ✅ 분리 가능 |
| Group β × Group γ-2 | 책무 영역 다름 (catalog vs HSM) | ✅ 분리 가능 |
| **Group γ-1 × Group γ-2** | **secret source 책무 분담** — γ-1 (file perm) + γ-2 (HSM source) / **위험 규모 다름** (GPT 권고 답습) | ⚠️ **HIGH 분리 의무** ⭐ |

**합산**: 6 페어 中 5 ✅ 분리 가능 + 1 ⚠️ HIGH 분리 의무 (γ-1 × γ-2) — **분리 어려움 0건**.

---

## 4. 합의 *단위* + 합의 *형태* 권고 v2

### 4.1 합의 *단위* 옵션 매트릭스 v2

| 옵션 | 단위 | 책무 합산 | 합의 부담 | 적합성 |
|-----|----|-------|---------|------|
| (I) 6 sub-영역 *단일 통합* | 1 합의 | 7/7 책무 차원 동시 결정 | 매우 高 | ⚠️ 가능 |
| (II) v1 권고 — 3 그룹 분리 (α / β / γ) | 3 합의 | 그룹 별 책무 차원 | 中 | ⚠️ Group γ 과도 묶음 (GPT 권고 답습) |
| **(II') v2 권고 — 4 그룹 분리 (α / β / γ-1 / γ-2)** ⭐ | **4 합의** | 그룹 별 책무 차원 | 中 | ✅ **권고** — GPT 권고 답습 + 위험 규모 분리 |
| (III) 6 sub-영역 *각각* 분리 | 6 합의 | sub-영역 단독 결정 | 低-中 (각 단독) | ⚠️ 가능 — 결합 위험 분석 분리 부담 |
| (IV) Group α 통합 + 나머지 4 분리 | 5 합의 | α 만 통합, 나머지 단독 | 中 | ⚠️ 가능 |
| (V) Group α + β 통합 + Group γ 분리 (다른 그룹화) | 3 합의 | 다른 그룹화 | 中 | ⚠️ 가능 |
| (VI) 책무 영역 별 분리 | 5 합의 | 책무 영역 별 단독 결정 | 中 | ⚠️ 가능 |

**본 v2 권고**: **(II') 4 그룹 분리** — GPT 권고 답습 (Group γ 분리) + v1 책무 그룹화 답습 + 위험 규모 분리.

#### 4.1.1 권고 합의 단위 (II') 답습 시 합의 보고서 경로

| 그룹 | 경로 후보 |
|----|--------|
| Group α (AR-3 + PC-4 T3 sub) | `docs/review/3plus1-consensus-2026-05-<TBD>-backlog3-enforcement-defense.md` |
| Group β (T-5 (β) + Tier-2/3 일반) | `docs/review/3plus1-consensus-2026-05-<TBD>-backlog3-catalog-tier23-policy.md` |
| **Group γ-1 (C-5b ST-1)** ⭐ | `docs/review/3plus1-consensus-2026-05-<TBD>-backlog3-st1-downstream-preflight.md` |
| **Group γ-2 (Vault HSM ST-4)** ⭐ | `docs/review/3plus1-consensus-2026-05-<TBD>-backlog3-vault-hsm-mvp6-defer.md` |

### 4.2 합의 *형태* 권고 v2 (v1 답습 — 변경 0건)

| 합의 형태 | 적합성 | 사유 |
|--------|------|------|
| **(가) 풀 3+1 합의 + 외부 LLM 1+ cross-vendor blind + 사용자 명시** | ✅ **권고 (v1 답습)** | (i) 4 그룹 모두 T3 영역 진입 의무 / (ii) R-MVP1-G3-7/8 + R-MVP1-G5-7/8/9 답습 / (iii) Layer B `f40423f` Backlog #3 분리 명시 / (iv) 외부 LLM 2 vendor 응답 회수 완료 (8b5b626) — 응답 = 입력 한정 |
| (나) 풀 3+1 합의 (외부 LLM 미의무) | ❌ 부적합 | T3 영역 = 외부 LLM 1+ 의무 — Provider Liquidity 책무 |
| (다) Reviewer-only 단축 합의 | ❌ 부적합 | T3 영역 = 풀 3+1 의무 |
| (라) (가) + 인간 리뷰 의무 | ⚠️ MVP-6 영역 | 본 brief 영역 외 |

**본 v2 권고**: **(가) 풀 3+1 + 외부 LLM 1+ + 사용자 명시** (4 그룹 각각) — 단, **외부 LLM 응답은 이미 회수 완료** (`8b5b626`) → 풀 3+1 합의 진입 시 *외부 LLM 응답 추가 발송 0건* (응답 = 입력 한정).

### 4.3 합의 발효 시점 v2 (v1 답습 + γ 분리 반영)

| 시점 | 합의 발효 영역 | 후속 단계 |
|-----|----------|--------|
| Group α 합의 발효 | AR-3 + PC-4 T3 sub *수단 결정* 한정 (실 변경 0건) | 사용자 명시 결정 → 별도 실 적용 단계 |
| Group β 합의 발효 | T-5 (β) + Tier-2/3 일반 *정책 결정* 한정 (실 catalog 본문 확장 0건) | 사용자 명시 결정 → 별도 실 catalog 본문 변경 단계 (Implementation Evidence PASS 후) |
| **Group γ-1 합의 발효** | **C-5b ST-1 downstream wrapper preflight *수단 결정* 한정** (실 Hermes upstream 변경 0건) | 사용자 명시 결정 → downstream wrapper 적용 단계 |
| **Group γ-2 합의 발효** | **Vault HSM ST-4 *MVP-6 보류 확정* 한정** (수단 결정 0건 + 보류 확정 = MVP-6 진입 시점 별도 합의) | MVP-6 Operational Readiness 발효 후 별도 합의 |

---

## 5. 풀 3+1 Agent A / B / C 관점 분배 v2 (4 그룹)

### 5.1 표준 풀 3+1 Agent 역할 답습 (v1 §5.1 답습)

| Agent | 관점 | 핵심 질문 |
|-------|------|--------|
| Agent A | 구현 분석가 | "실제로 동작하는가?" |
| Agent B | 품질 / 안전성 검증가 | "안전하고 견고한가?" |
| Agent C | 대안 탐색가 | "더 나은 방법이 있는가?" |
| Reviewer | 검토 에이전트 | "최선의 합의는?" |

### 5.2 Group α (AR-3 + PC-4 T3 sub) — v1 §5.2 + 외부 LLM 흡수

| Agent | 핵심 분석 영역 (v2 추가) |
|------|----------|
| Agent A | (v1 답습) AR-3 + PC-4 T3 sub 기술 통합 + `--no-verify` 우회 차단 효과 + GitHub Actions integration / pre-commit 호환성 / **(v2 추가) branch protection 세부 (direct push / force push / admin bypass) 옵션 동작 + GitHub plan 가용성 검증 + AI agent / bot 권한 범위 옵션** |
| Agent B | (v1 답습) 보안 + 엣지케이스 + 문서 정합성 / **(v2 추가) CODEOWNERS 1인 한계 명시 (독립 리뷰 아닌 friction) + AI agent 서명 방식 보안 평가 + fork PR `pull_request_target` BLOCK 답습** |
| Agent C | (v1 답습) 대안 + 트레이드오프 / **(v2 추가) commit signing 시점 (MVP-6 권고 답습) + `pre-commit install` 단계적 (opt-in → doctor → required) 답습** |

### 5.3 Group β (T-5 (β) + Tier-2/3 일반) — v1 §5.3 + 외부 LLM 흡수

| Agent | 핵심 분석 영역 (v2 추가) |
|------|----------|
| Agent A | (v1 답습) Tier 분류 기준 + catalog 본문 형식 + 자동 동기화 + FP/FN 측정 / **(v2 추가) audit-only 도입 기술 (warn-only flag + report-only mode + threshold 별 step 분리) + adapter stub generator 구현** |
| Agent B | (v1 답습) 보안 + 엣지케이스 + 문서 정합성 / **(v2 추가) FP 비상 탈출구 (escape hatch) 보안 평가 + LiteLLM advisory only 검증 + provider lock-in 역효과 완화책 evaluation + Implementation Evidence PASS 의무성 답습** |
| Agent C | (v1 답습) 대안 + 트레이드오프 / **(v2 추가) Sandboxed Tier (T1) 도입 / 6 완화책 트레이드오프 + Tier-2/3 hard-block 보류 답습 + Mistral / AI21 후보 검토 (양 vendor 동의)** |

### 5.4 Group γ-1 (C-5b ST-1) — 신설 (v1 §5.4 부분 답습)

| Agent | 핵심 분석 영역 |
|------|----------|
| Agent A | downstream wrapper / entrypoint preflight / CI container test 기술 검토 + 환경별 분리 (dev warning / CI fail-closed) 구현 + Hermes upstream PR 절차 (downstream evidence 확보 후) |
| Agent B | Hermes ≠ root of trust 보존 검증 (외부 harness 검증 주체 답습) + chmod 600 위반 시 동작 + sidecar (ST-2) / docker secret (ST-3) 와 책무 분담 + ST-4 와 책무 분담 (분리 권고 답습) |
| Agent C | 대안 (entrypoint script vs Dockerfile layer vs sidecar) + Hermes upstream 변경 vs downstream wrapper 트레이드오프 (downstream evidence 확보 후 최소 패치 권고) |

### 5.5 Group γ-2 (Vault HSM ST-4) — 신설 (v1 §5.4 부분 답습)

| Agent | 핵심 분석 영역 |
|------|----------|
| Agent A | MVP-6 Operational Readiness 발효 시점 인프라 검토 + Vault SDK 통합 형태 + ADR-010 §X 본문 형태 (별도 합의) + Multi-host 전환 시점 |
| Agent B | Vault HSM 보안 평가 + 5 영구 핵심 제약 #1 (Hermes ≠ root of trust) 보존 + HSM key 관리 / Vault audit log 통합 + 1인 환경 부적합 사유 답습 (양 vendor 수렴) |
| Agent C | 대안 (Vault OSS + HSM / Vault Enterprise / 클라우드 KMS / self-hosted PKCS#11) + Vault Agent injector vs Hermes 직접 호출 / Operational Readiness 1인 정의 6 기준 답습 + ST-1/ST-2/ST-3 우선 + ST-4 후순위 (양 vendor 수렴) |

### 5.6 Reviewer 검토 의무 영역 (4 그룹 공통) — v1 §5.5 답습

v1 §5.5 답습 + 추가:

| 검토 영역 (v2 추가) | 의무 발화 |
|-----|----|
| 외부 LLM 응답 양 vendor (Gemini + GPT) 합산 / 차이 / 수렴 결론 통합 | ✅ 의무 |
| Gap #1 ~ #8 흡수 적절성 검증 | ✅ 의무 |
| Group γ 분리 (γ-1 / γ-2) 권고 적절성 평가 | ✅ 의무 |
| audit-first / hard-block 분리 정책 평가 | ✅ 의무 |
| provider lock-in 역효과 완화책 평가 | ✅ 의무 |
| Operational Readiness 1인 정의 (6 기준) 평가 | ✅ 의무 |

---

## 6. 외부 LLM 응답 양 vendor 수렴 합산 + 차이 영역

### 6.1 수렴 영역 (양 vendor 동의)

| 영역 | 양 vendor 수렴 |
|----|----|
| 종합 판정 | (C) PARTIAL (양쪽 동일) |
| Group α 진입 가능성 | APPROVE / APPROVE WITH CONDITIONS (양쪽 동의 — 우선순위 1) |
| Group β 진입 형태 | audit-only / policy-only (양쪽 동의) — hard-block 보류 |
| Vault HSM ST-4 진입 시점 | MVP-6 이후 (양쪽 동의 — 1인 single-host 부적합) |
| Tier-2/3 catalog 자동 동기화 | BLOCK (양쪽 동의 — LiteLLM advisory only) |
| provider lock-in 강화 역효과 | 실재 HIGH 위험 (양쪽 동의) |
| commit signing 시점 | MVP-6 권고 (양쪽 동의 — 1인 운영 비용 高) |
| `--no-verify` 차단 | 로컬 단독 불가 + branch protection 결합 필수 (양쪽 동의) |
| fork PR `pull_request_target` 도입 | BLOCK (양쪽 동의 — default 보수적 정책 유지) |
| Group α × PC-4 결합 효과 | Defense in depth = 유일하게 유효한 차단책 (양쪽 동의) |

### 6.2 차이 영역 (vendor 별 권고 다름)

| 영역 | Gemini 권고 | GPT 권고 | v2 권고 |
|----|----|----|----|
| Q1 AR-3 옵션 | (g) 전체 통합 | (e) CODEOWNERS + required check (단계적) | **GPT 답습 (단계적)** ⭐ (1인 환경 균형) |
| Q2 PC-4 T3 sub 강제 형태 | 즉시 강제 | 단계적 (opt-in → doctor → required) | **GPT 답습 (단계적)** ⭐ (개발자 friction 회피) |
| Q8 T-5 (β) hard-block | Tier-2 적극 확장 | Tier-2 hard-block 확장 0건 + audit-only | **GPT 답습 (audit-only)** ⭐ (보수적) |
| Q13 ST-1 진입 형태 | entrypoint chmod 검증 (단순) | **downstream wrapper preflight** | **GPT 답습 (downstream)** ⭐ (Hermes ≠ root of trust 보존) |
| Q15 ST 통합 정책 | Defense in depth (ST-1/2/3 우선) | 환경별 canonical 분담 (ST-3 primary / ST-1 preflight / ST-2 drift / ST-4 production) | **GPT 답습 (환경별 분담)** ⭐ (책무 분리 강화) |
| Group γ 묶음 | 통합 묶음 유지 | **분리 권고 (γ-1 / γ-2)** | **GPT 답습 (분리)** ⭐ (위험 규모 분리) |

**v2 차이 영역 권고 패턴**: 모든 차이 영역에서 **GPT 권고 답습** — 보수적 / 단계적 / Hermes ≠ root of trust 보존 / 책무 분리 강화 / 1인 개발자 환경 부담 최소화 일관성.

### 6.3 양 vendor 미언급 / 추가 검토 필요 영역 (내부 풀 3+1 합의 시 결정)

| 영역 | 사유 |
|----|----|
| ADR-010 §X 본문 형태 (신규 §X 추가 vs 갱신 vs ADR-015 신설) | Vault HSM ST-4 = MVP-6 이후 — 양 vendor 미언급 (분리 영역) |
| Hermes upstream PR vs fork+downstream patch 책무 분담 (Group γ-1) | GPT 부분 언급 + 내부 풀 3+1 합의 시 결정 영역 |
| AI agent / bot 권한 영역 분리 세부 (`tools/**` vs `docs/**` vs 전체) | Gemini Gap #1 지적 + 내부 결정 영역 |
| Operational Readiness 6 기준 우선순위 (rotation / backup / audit / fallback / 비용 / SPOF 문서화) | GPT Gap #8 지적 + 내부 결정 영역 |
| Sandboxed Tier (T1) 구체 설계 | Gemini 권고 + 내부 결정 영역 |

---

## 7. Rollback Trigger 통합 매트릭스 v2 (v1 §7 답습 + audit-first 추가)

### 7.1 v1 §7 답습 (변경 0건)

R-MVP1-G3-7 (ST-1) + R-MVP1-G3-8 (Vault HSM ST-4) + R-MVP1-G5-7/8 (T-5 β) + R-MVP1-G5-9 (AR-3) + R-MVP1-G3-3 (ST-1 / ST-4) + R-1 (Tier-2/3 catalog) + R-MVP1-G3-1 (Tier-2/3 일반) — v1 답습.

### 7.2 v2 추가 — audit-first cycle Trigger

| Trigger (v2 신규) | sub-영역 | 발화 조건 | 발화 시 행동 |
|--------|---------|---------|----------|
| **R-MVP1-G5-AUDIT-1** | (2) T-5 (β) + (6) Tier-2/3 일반 | Tier-2 audit-only → hard-block 승격 결정 | Implementation Evidence PASS 발효 후 + 별도 풀 3+1 합의 |
| **R-MVP1-G5-AUDIT-2** | (2) T-5 (β) + (6) Tier-2/3 일반 | LiteLLM advisory snapshot 자동 PR 도입 결정 | 별도 합의 (자동 merge / 자동 hard-block 금지 답습) |
| **R-MVP1-G5-ESCAPE-1** | (2) T-5 (β) + (6) Tier-2/3 일반 | FP 비상 탈출구 (escape hatch) 발화 | 단축 합의 적격 (FP 검출 + 긴급 bypass 한정) — provider lock-in 역효과 완화 |

### 7.3 v2 추가 — Group γ 분리 Trigger

| Trigger (v2 신규) | sub-영역 | 발화 조건 | 발화 시 행동 |
|--------|---------|---------|----------|
| **R-MVP1-G3-GAMMA-1** | (4) C-5b ST-1 / Group γ-1 | Hermes upstream 직접 PR 결정 (downstream wrapper 미충분 시) | 풀 3+1 합의 + downstream evidence 확보 의무 + Hermes upstream maintainer 협의 |
| **R-MVP1-G3-GAMMA-2** | (5) Vault HSM ST-4 / Group γ-2 | MVP-6 Operational Readiness 발효 + ST-4 진입 결정 | ADR-010 §X 진입 합의 + Multi-host 인프라 검토 + 외부 LLM 1+ |

---

## 8. 7/7 풀 3+1 승격 트리거 *재검증* v2 (v1 §8 답습)

### 8.1 본 brief v2 4 그룹 *모두* 발화 — Reviewer-only 단축 합의 *부적격* (v1 답습)

v1 §8 답습 + γ 분리 답습:

| # | 트리거 | 본 v2 4 그룹 발화 |
|---|----|--------------------|
| 1 | 9 sub-수단 외 수단 *재결정* | ⚠️ 부분 — (2) T-5 (β) + (4) ST-1 + (5) ST-4 = 추가 수단 결정 |
| 2 | **T3 영역 자동 진입** | ✅ HIGH (BLOCKING) — 4 그룹 모두 T3 영역 |
| 3 | 사용자 명시 3 결정 (α/ii/(가)) *재변경* | ❌ 0건 |
| 4 | Provider Liquidity 5-way 약화 | ⚠️ HIGH — Group β + Group γ-2 |
| 5 | 5 영구 핵심 제약 약화 | ⚠️ **HIGH** — Group γ-1 (Hermes ≠ root of trust) / Group γ-2 (단일 source-of-truth) |
| 6 | **MVP-1 PASS 재선언 / Layer E / Layer F** | ❌ 0건 |
| 7 | 외부 LLM cross-vendor blind 없는 T3 결정 | ⚠️ **부분** — 외부 LLM 응답 회수 완료 (`8b5b626`, Gemini + GPT) — 응답 = 입력 한정 |

**합산**: v1 답습 — 트리거 #2 + #5 = HIGH BLOCKING + 부분 #1 + #4 + #7 → **풀 3+1 + 사용자 명시 의무 발화 확정**.

### 8.2 v2 추가 — 외부 LLM 응답 회수 후 트리거 #7 변화

| 영역 | v1 | v2 |
|----|----|----|
| 외부 LLM 응답 회수 상태 | 미수신 | **수신 완료** (`8b5b626`, Gemini + GPT) ⭐ |
| 트리거 #7 발화 강도 | HIGH (의무) | **부분 발화** — 응답 *결론 강제 채택 0건* + 응답 = 입력 한정 + 내부 풀 3+1 합의 시 평가 대상 |
| 풀 3+1 합의 시 외부 LLM 추가 발송 의무 | ⚠️ 의무 (의뢰서 발송 필요) | ❌ 0건 (응답 회수 완료) — 단, 결함 수정 / 재의뢰 시 추가 발송 영역 |
| 합의 형태 | 풀 3+1 + 외부 LLM 1+ + 사용자 명시 | **풀 3+1 + (외부 LLM 응답 입력 답습) + 사용자 명시** — 변경 0건 |

---

## 9. 우선순위 권고 v2 + 차단 요인

### 9.1 4 그룹 *합의 진입 우선순위* v2 (양 vendor 수렴 답습)

| 순위 | 그룹 | 사유 |
|----|----|-----|
| **1순위** | **Group α (AR-3 + PC-4 T3 sub)** | 양 vendor 수렴 진입 가능성 1순위 / dev 환경 + GitHub repo 정책 / Backlog #6 연결 시 실 강제 가능 |
| **2순위** | **Group β (T-5 (β) + Tier-2/3 일반)** | 양 vendor 수렴 audit-only 진입 가능 / hard-block 보류 (Implementation Evidence PASS 후) / FP 비상 탈출구 + provider lock-in 역효과 완화책 흡수 |
| **3순위** | **Group γ-1 (C-5b ST-1)** ⭐ | GPT 권고 답습 — downstream wrapper preflight 형태 진입 가능 / Hermes upstream 변경 0건 유지 / Hermes ≠ root of trust 보존 |
| **4순위** | **Group γ-2 (Vault HSM ST-4)** ⭐ | 양 vendor 완전 수렴 — MVP-6 Operational Readiness 발효 후 진입 + **현 시점 진입 부적합 (BLOCK / DEFER)** |

### 9.2 우선순위 *조정 권고* (4 그룹 합의 (II') 답습 시)

```
1순위: Group α (AR-3 + PC-4 T3 sub)      — Defense in depth, dev 환경 + GitHub repo
2순위: Group β (T-5 β + Tier-2/3 일반)    — audit-only + policy + FP escape hatch
3순위: Group γ-1 (C-5b ST-1)              — downstream wrapper preflight
4순위: Group γ-2 (Vault HSM ST-4)         — MVP-6 보류 확정 (양 vendor 수렴)
```

### 9.3 *차단 요인* v2 (v1 §9.3 답습 + 외부 LLM 흡수)

| # | 차단 요인 | 발화 | v2 변화 |
|---|--------|-----|----|
| 1 | Backlog #6 (Runtime + CI-hook) 미진입 | ⚠️ MEDIUM | 양 vendor 권고 답습 — Group α 진입 = Backlog #6 연결 필수 → **MEDIUM → HIGH** ⭐ |
| 2 | Implementation Evidence PASS 미발효 | ⚠️ MEDIUM | 양 vendor 권고 답습 — Group β hard-block 보류 의무 → **MEDIUM → HIGH** ⭐ |
| 3 | 외부 LLM 1+ cross-vendor blind 의뢰 발송 미실시 | ⚠️ HIGH (v1) | **❌ 0건** (v2 — 양 vendor 응답 회수 완료 `8b5b626`) ⭐ |
| 4 | Backlog #1 (ST-2 inotify sidecar) 미진입 | ⚠️ MEDIUM | Group γ-1 책무 분담 결정 시 ST-2 답습 의존 — 변경 0건 |
| 5 | Operational Readiness PASS (Layer E) 미발효 | ⚠️ HIGH | Group γ-2 진입 영역 의존 — 변경 0건 (양 vendor 수렴 답습) |
| 6 | C-14 cross-vendor 11 핵심 조건 흡수 미완 | ⚠️ MEDIUM | P2 v3 정식 채택 별도 영역 — 변경 0건 |

### 9.4 본 brief v2 후속 다음 단계 우선순위 권고

| 우선순위 | 다음 단계 | 사유 |
|--------|--------|------|
| **(I)** | **본 v2 그대로 승인 → 사용자 명시 후속 단계 결정 영역** | v2 = DRAFT 한정 |
| (II) | 본 v2 승인 → Group α 풀 3+1 합의 *진입* (Agent A/B/C 분석 + 외부 LLM 응답 답습 + Reviewer 종합) | 양 vendor 수렴 우선순위 1 답습 |
| (III) | 본 v2 승인 → Backlog #6 (Runtime + CI-hook) 우선 진입 brief 작성 — Group α 진입 *전* | 양 vendor 권고 답습 (Backlog #6 연결 필수) |
| (IV) | 본 v2 승인 → Group γ-2 *MVP-6 보류 확정* 단독 합의 (Reviewer-only 단축 합의 적격 여부 검토 — 양 vendor 완전 수렴 → 단축 적격 가능성 검토) | 양 vendor 완전 수렴 답습 |
| (V) | 본 v2 보류 → MVP-2 진입 brief | Implementation Evidence PASS 미발효 — 부적합 |
| (VI) | 본 v2 보류 → 세션 종료 | 사용자 명시 결정 영역 |

---

## 10. 메타 검증 v2

| 메타 검증 | 본 brief v2 |
|---------|--------|
| 사용자 명시 진입 명령 답습 ((A) 외부 LLM 응답 commit + push / (E) 외부 지적 흡수 brief v2 작성) | ✅ Step 1 = `8b5b626` commit/push 완료 / Step 2 = 본 v2 |
| 사용자 명시 9 금지 답습 (풀 3+1 합의 / T3 진입 / branch protection / dev 환경 강제 / Hermes upstream / Vault HSM / Tier-2/3 확장 / Operational Readiness PASS / Hermes PMO 격상) | ✅ §0.3 + 부록 B |
| 본 brief v2 = DRAFT 한정 (commit 0건 / push 0건) | ✅ 헤더 + §0.4 |
| **v1 (`ad9a02d`) 본문 변경 0건 (v1 보존 + v2 별도 권위 source)** | ✅ §0.4 |
| 외부 LLM 응답 8 지적 흡수 매트릭스 | ✅ §1.2 + 부록 C |
| 양 vendor 수렴 / 차이 영역 합산 | ✅ §6.1 + §6.2 |
| **GPT 권고 Group γ 분리 흡수 → 4 그룹화** ⭐ | ✅ §1.2 #7 + §3.3 + §3.4 + §4.1 (II') |
| Group α 보강 (branch protection 세부 + AI agent 권한 + CODEOWNERS 1인 한계) | ✅ §2.1.3~§2.1.5 + §3.1.3~§3.1.6 |
| Group β 보강 (audit-only + FP escape hatch + 예외 경로 + provider lock-in 완화) | ✅ §2.2.3~§2.2.5 + §2.6.3~§2.6.5 + §3.2.3~§3.2.5 |
| Group γ-1 신설 (downstream wrapper preflight) | ✅ §2.4 + §3.3 |
| Group γ-2 신설 (Vault HSM MVP-6 보류 + Operational Readiness 1인 정의) | ✅ §2.5 + §3.4 |
| Agent A/B/C 관점 분배 (4 그룹) | ✅ §5.2~§5.5 |
| 7/7 풀 3+1 트리거 재검증 (v1 답습 + 트리거 #7 변화) | ✅ §8 |
| 우선순위 권고 v2 (α → β → γ-1 → γ-2) | ✅ §9.1 + §9.2 |
| 차단 요인 v2 (외부 LLM 응답 회수 완료 — 차단 #3 ❌) | ✅ §9.3 |
| Rollback Trigger v2 (audit-first + γ 분리 trigger 추가) | ✅ §7.2 + §7.3 |
| 외부 LLM 응답 *결론 강제 채택 0건* (응답 = 입력 한정 보존) | ✅ §0.3 + §4.2 |
| **§C-5 / §C-5b / §C-5c / §C-6 상태 표기 *재변경* 0건** | ✅ |
| Layer D 본문 변경 0건 (A-1 답습) | ✅ |
| §5.5 9 sub-수단 본문 채택 변경 0건 (Layer B `f40423f` 그대로 유지) | ✅ |
| `tools/*.py` / `.importlinter` / `.pre-commit-config.yaml` / CI workflow 변경 0건 | ✅ |
| ADR 본문 자동 갱신 0건 (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012) | ✅ |
| Backlog #1 / #2 / #4 / #6 / #7 자동 진입 0건 | ✅ |
| 5 영구 핵심 제약 5/5 보존 | ✅ — γ-1 (Hermes ≠ root of trust 보존 강화) + γ-2 (단일 source-of-truth 영향 검토 의무) |
| MVP-1 PASS 재선언 0건 / MVP-2 자동 진입 0건 | ✅ |

### 10.1 v1 ↔ v2 핵심 변경 사항 요약

| 영역 | v1 (`ad9a02d`) | v2 (본 문서) |
|------|------|------|
| 그룹화 | 3 그룹 (α / β / γ) | **4 그룹 (α / β / γ-1 / γ-2)** ⭐ |
| 외부 LLM 응답 | 미수신 | **수신 완료** (Gemini + GPT `8b5b626`) |
| 8 지적 흡수 | (해당 없음) | **8/8 흡수** |
| Group α 결정 영역 | 5 영역 | **8 영역** (branch protection 세부 + AI agent 권한 + GitHub plan) |
| Group β 결정 영역 | 6 영역 | **8 영역** (audit-only + FP escape hatch + 예외 경로) |
| Group γ 결정 영역 | 6 영역 통합 | **γ-1 = 5 영역 + γ-2 = 4 영역 분리** |
| 우선순위 | α → β → γ | **α → β → γ-1 → γ-2** |
| 트리거 #7 (외부 LLM blind) | HIGH (의무) | **부분 발화** (응답 회수 완료) |
| 차단 요인 #3 (외부 LLM 의뢰 미실시) | ⚠️ HIGH | **❌ 0건** |
| 본문 변경 | (v1 본문) | v1 본문 변경 0건 + v2 별도 권위 source |

### 10.2 v1 본문 변경 0건 의무 답습

본 brief v2 = **v1 (`ad9a02d`) 본문 변경 0건**. v1 = 보존 + v2 = 외부 LLM 응답 흡수 한정 별도 권위 source. 사용자 명시 답습 — v1 본문 *변경* 시 v1 commit 답습 충실성 ↓.

### 10.3 양 vendor 수렴 핵심 답습 (v2 흡수 결과)

| 영역 | 양 vendor 수렴 | v2 본문 흡수 위치 |
|----|----|----|
| 종합 판정 = PARTIAL | 양쪽 동일 | §6.1 + §9.1 |
| Group α 우선 진입 + Backlog #6 연결 | 양쪽 동의 | §9.1 + §9.3 #1 |
| Group β audit-only + hard-block 보류 | 양쪽 동의 | §2.2.3 + §2.6.3 + §9.1 |
| Vault HSM ST-4 MVP-6 이후 | 양쪽 완전 수렴 | §2.5.5 + §3.4.4 + §9.1 |
| Tier-2/3 자동 동기화 BLOCK | 양쪽 동의 | §2.6.3 |
| provider lock-in 역효과 HIGH | 양쪽 동의 | §2.2.5 + §2.6.5 |
| commit signing = MVP-6 권고 | 양쪽 동의 | §2.1.6 |
| fork PR `pull_request_target` BLOCK | 양쪽 동의 | §2.1.6 |
| `--no-verify` 차단 = branch protection 결합 | 양쪽 동의 | §2.3.3 + §3.1.7 |
| AR-3 × PC-4 Defense in depth | 양쪽 동의 | §3.1.2 + §3.1.7 + §4.2 |

---

## 11. 본 brief v2 요약 (한 단락)

본 brief v2 는 **Backlog #3 (T3 영역) 풀 3+1 합의 *준비안* v1 (`ad9a02d`) 의 *후속*** — 외부 LLM cross-vendor blind 응답 2건 (`8b5b626`, **Gemini 3 Flash** + **GPT-5.5 Thinking**, 양쪽 종합 판정 = **(C) PARTIAL** 수렴) 의 **8 지적 사항 흡수** + **GPT 권고 Group γ 분리 (γ-1 ST-1 / γ-2 Vault HSM ST-4)** 답습 + **양 vendor 수렴 정책** (audit-only / hard-block deferred / provider lock-in 역효과 완화 / Vault HSM MVP-6 보류 / commit signing MVP-6 / fork PR `pull_request_target` BLOCK / `--no-verify` = branch protection 결합) 흡수. **v1 본문 변경 0건** (v1 = 보존 + v2 = 별도 권위 source). **8 지적 흡수**: (1) AR-3 시 AI agent / bot / GitHub App 권한 + 서명 (Gemini) → §2.1.4 / (2) Group β FP 비상 탈출구 (Gemini) → §2.2.4 / (3) branch protection 세부 (direct push / force push / admin bypass) (GPT) → §2.1.3 / (4) GitHub plan / 권한 제약 (GPT) → §2.1.5 / (5) CODEOWNERS 1인 한계 ("재확인 friction") (GPT) → §2.1.3 + §3.1.4 / (6) Tier-2/3 예외 경로 (allowlist + expiry + adapter stub generator) (GPT) → §2.2.4 + §2.6.4 / (7) **Group γ 과도 묶음 (위험 규모 다름)** (GPT) → **§3.3 + §3.4 + §4.1 (II') 4 그룹화** ⭐ / (8) Operational Readiness 1인 개발자 정의 (rotation / backup / fallback / audit / 비용 / SPOF 문서화) (GPT) → §2.5.4 + §3.4.3. **합의 단위 권고 v2** = (II') **4 그룹 분리** (Group α / β / γ-1 / γ-2) — GPT 권고 답습 + 위험 규모 분리. **합의 형태 권고 v2** = (가) 풀 3+1 + 외부 LLM 1+ + 사용자 명시 (v1 답습 — 변경 0건, 외부 LLM 응답 = 입력 한정 + 추가 발송 0건). **우선순위 권고 v2** = α (1순위) → β (audit-only, 2순위) → γ-1 (downstream wrapper preflight, 3순위) → γ-2 (MVP-6 보류, 4순위). **양 vendor 차이 영역 6건** (Q1 AR-3 / Q2 PC-4 / Q8 T-5 β / Q13 ST-1 / Q15 ST 통합 / Group γ 묶음) — v2 모두 **GPT 권고 답습** (보수적 / 단계적 / Hermes ≠ root of trust 보존 / 책무 분리 강화 / 1인 환경 부담 최소화). **차단 요인 v2** = 외부 LLM 의뢰 미실시 ❌ 0건 (회수 완료) / Backlog #6 미진입 HIGH (양 vendor 권고 — Group α 진입 = Backlog #6 연결 필수) / Implementation Evidence PASS 미발효 HIGH (양 vendor 권고 — Group β hard-block 보류) / Operational Readiness PASS 미발효 HIGH (양 vendor 수렴 — Group γ-2 진입 의존). **본 brief v2 ≠ 합의 발효** + **v1 본문 변경 0건** + **§C-5/§C-5b/§C-5c/§C-6 재변경 0건** + **Layer D 본문 변경 0건** + **§5.5 9 sub-수단 본문 채택 변경 0건** + **실제 T3 영역 진입 0건** + **branch protection 변경 0건** + **dev 환경 강제 0건** + **Hermes upstream Dockerfile 변경 0건** + **Vault HSM 구현 0건** + **Tier-2/3 catalog 본문 확장 0건** + **Operational Readiness PASS 0건** + **Hermes PMO 격상 0건** + **풀 3+1 합의 보고서 작성 0건** + **외부 LLM 추가 자동 호출 0건** + **외부 LLM 응답 결론 강제 채택 0건** + **ADR 본문 자동 갱신 0건** + **Backlog #1/#2/#4/#6/#7 자동 진입 0건** + **MVP-1 PASS 재선언 0건** + **MVP-2 자동 진입 0건**. 다음 단계 = 사용자 결정 영역 (부록 A 옵션 A~H).

---

## 부록 A. 다음 단계 결정 옵션 (사용자 결정 영역)

| 옵션 | 영역 | 후속 단계 |
|-----|------|--------|
| **(A)** | **본 v2 그대로 승인 → 파일화 + commit + push (`docs/phase0/backlog3-t3-zone-full-3plus1-brief-v2.md`) → 사용자 명시 후속 단계 결정** | 본 v2 commit + push (1 commit) |
| (B) | 본 v2 일부 수정 요청 → 수정 후 승인 | v3 작성 |
| (C) | 본 v2 그대로 승인 → 파일화 + commit *까지만* (push 보류) | 1 commit |
| (D) | 본 v2 승인 + push → **Group α 풀 3+1 합의 *진입*** (Agent A/B/C 분석 + 외부 LLM 응답 답습 + Reviewer 종합) | 양 vendor 수렴 우선순위 1 답습 |
| (E) | 본 v2 승인 + push → **Backlog #6 (Runtime + CI-hook) 우선 진입 brief 작성** — Group α 진입 *전* | 양 vendor 권고 답습 (Backlog #6 연결 필수) |
| (F) | 본 v2 승인 + push → **Group γ-2 *MVP-6 보류 확정* 단독 합의** (Reviewer-only 단축 합의 적격 여부 검토) | 양 vendor 완전 수렴 답습 |
| (G) | 본 v2 보류 → 추가 vendor 응답 회수 (Claude / Llama / Mistral 등) → 3+ vendor 종합 후 v3 | 추가 vendor blind |
| (H) | 본 v2 보류 → 세션 종료 | — |

### A.1 권고 시작 명령 (사용자 명시 결정 영역)

- (A) 시작 명령 후보: "옵션 (A) 로 진행해주세요. 본 v2 그대로 승인하고, `docs/phase0/backlog3-t3-zone-full-3plus1-brief-v2.md` commit + push."
- (D) 시작 명령 후보 (Group α 우선 진입): "옵션 (D) 로 진행해주세요. 본 v2 답습 + Group α (AR-3 + PC-4 T3 sub) 풀 3+1 합의 진입. Agent A/B/C 분석 + 외부 LLM 응답 답습 + Reviewer 종합."
- (E) 시작 명령 후보 (Backlog #6 우선): "옵션 (E) 로 진행해주세요. 본 v2 보존 + Backlog #6 (Runtime + CI-hook implementation) 우선 진입 brief 작성."

---

## 부록 B. 금지 사항 (사용자 명시 9 금지 + 추가 답습)

### B.1 사용자 명시 9 금지 답습 (이번 진입 명령)

| # | 금지 | 본 v2 위반 |
|---|------|------------|
| 1 | **내부 Agent A/B/C + Reviewer 풀 3+1 합의 보고서 작성** | 0건 (합의 = v2 작성 후 별도 사용자 승인) |
| 2 | **T3 영역 실제 진입** | 0건 |
| 3 | **branch protection rule 변경** | 0건 |
| 4 | **dev 환경 강제** (`pre-commit install` 의무화) | 0건 |
| 5 | **Hermes upstream Dockerfile 변경** | 0건 |
| 6 | **Vault HSM 구현** | 0건 |
| 7 | **Tier-2/3 catalog 본문 확장** | 0건 |
| 8 | **Operational Readiness PASS (Layer E) 선언** | 0건 |
| 9 | **Hermes PMO 격상 (Layer F) 선언** | 0건 |

### B.2 추가 금지 (본 v2 자체)

- ❌ **v1 brief (`ad9a02d`) 본문 변경** 0건 (v1 = 보존 + v2 = 별도 권위 source)
- ❌ T3 sub-영역 *수단 결정* / *도입* / *본문 채택 commit* 0건
- ❌ 풀 3+1 합의 보고서 *작성* / commit / push 0건 (합의 = 별도 사용자 승인)
- ❌ Reviewer-only 단축 합의 적격성 발화 0건 (T3 영역 의무 — 풀 3+1 의무)
- ❌ 외부 LLM *추가 자동 호출* / cross-vendor blind 의뢰 자동 재발송 0건
- ❌ **외부 LLM 응답 *결론 강제 채택* 0건** (응답 = 입력 한정 보존 — 내부 풀 3+1 합의 시 평가 대상)
- ❌ 실 API key / provider SDK / 외부 API 호출 / 실 secret 처리 0건
- ❌ ADR 본문 자동 갱신 0건 (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012)
- ❌ §C-5 / §C-5b / §C-5c / §C-6 상태 표기 *재변경* 0건
- ❌ Layer D 합의 보고서 (`210c98f`) 본문 변경 0건
- ❌ §5.5 9 sub-수단 본문 채택 변경 0건 (Layer B `f40423f` 그대로 유지)
- ❌ `tools/*.py` 본문 변경 0건
- ❌ `.importlinter` / `.pre-commit-config.yaml` 본문 변경 / 신규 hook 추가 0건
- ❌ CI workflow 변경 0건
- ❌ Production `docker-compose.yml` / Hermes upstream Dockerfile / requirements*.txt 변경 0건
- ❌ Backlog #1 / #2 / #4 / #6 / #7 자동 진입 0건
- ❌ MVP-1 PASS *재선언* 0건
- ❌ MVP-2 자동 진입 0건
- ❌ 5 영구 핵심 제약 약화 / Provider Liquidity 5-way 약화 0건
- ❌ CONTEXT / INDEX / SESSION 메타 갱신 0건 (별도 commit 분리)
- ❌ ADR-010 §X 본문 신규 추가 / ADR-015 신설 0건
- ❌ 인간 리뷰 의무 자동 발화 0건

---

## 부록 C. 외부 LLM 응답 흡수 추적 매트릭스 (v2 신규 ⭐)

### C.1 8 지적 흡수 추적 매트릭스

| Gap # | 지적 영역 | vendor | v2 흡수 위치 | 흡수 형태 | 흡수 상태 |
|---|----|----|----|----|----|
| 1 | AI agent / bot / GitHub App 권한 범위 + 서명 방식 | Gemini | §2.1.4 + §3.1.5 | Group α 결정 영역 추가 (3 옵션 × 4 서명 × 3 권한 분리) | ✅ 흡수 |
| 2 | Group β FP 비상 탈출구 정책 | Gemini | §2.2.4 + §2.6.4 + §3.2.4 | Group β 결정 영역 추가 (4 옵션 + expiry + owner) | ✅ 흡수 |
| 3 | branch protection 세부 (direct push / force push / admin bypass) | GPT | §2.1.3 + §3.1.3 | Group α 결정 영역 추가 (6 옵션) | ✅ 흡수 |
| 4 | GitHub plan / 권한 제약 | GPT | §2.1.5 + §3.1.6 | Group α 결정 영역 추가 (4 plan × 3 ruleset × 3 reviewer) | ✅ 흡수 |
| 5 | CODEOWNERS 1인 한계 ("재확인 friction") | GPT | §2.1.3 + §3.1.4 + §11 | Group α 결정 영역 + 메타 답습 | ✅ 흡수 |
| 6 | Tier-2/3 예외 경로 (allowlist / expiry / adapter stub generator) | GPT | §2.2.4 + §2.6.4 + §3.2.3 | Group β 결정 영역 추가 (4 옵션 + 의무 evidence) | ✅ 흡수 |
| 7 | **Group γ 과도 묶음 — γ-1 / γ-2 분리** ⭐ | GPT | **§3.3 + §3.4 + §4.1 (II')** | **그룹화 구조 변경 — 4 그룹화** | ✅ 흡수 (핵심 변경) |
| 8 | Operational Readiness 1인 개발자 정의 (6 기준) | GPT | §2.5.4 + §3.4.3 | Group γ-2 결정 영역 + 메타 답습 | ✅ 흡수 |

### C.2 양 vendor 수렴 권고 흡수 추적 매트릭스

| 영역 | 양 vendor 수렴 | v2 흡수 위치 | 흡수 상태 |
|----|----|----|----|
| 종합 판정 = PARTIAL | 양쪽 | §6.1 + §9.1 | ✅ |
| Group α 우선 진입 + Backlog #6 연결 | 양쪽 | §9.1 + §9.3 #1 | ✅ |
| Group β audit-only + hard-block 보류 | 양쪽 | §2.2.3 + §2.6.3 + §9.1 | ✅ |
| Vault HSM ST-4 MVP-6 이후 | 양쪽 완전 | §2.5.5 + §3.4.4 + §9.1 | ✅ |
| Tier-2/3 자동 동기화 BLOCK | 양쪽 | §2.6.3 | ✅ |
| LiteLLM advisory only | 양쪽 | §2.6.3 | ✅ |
| provider lock-in 역효과 HIGH | 양쪽 | §2.2.5 + §2.6.5 | ✅ |
| commit signing = MVP-6 | 양쪽 | §2.1.6 | ✅ |
| fork PR `pull_request_target` BLOCK | 양쪽 | §2.1.6 | ✅ |
| `--no-verify` = branch protection 결합 | 양쪽 | §2.3.3 + §3.1.7 | ✅ |
| AR-3 × PC-4 = 유일 차단책 | 양쪽 | §3.1.2 + §3.1.7 + §4.2 | ✅ |

### C.3 양 vendor 차이 영역 권고 패턴 매트릭스

| 영역 | Gemini 권고 | GPT 권고 | v2 채택 | 채택 사유 |
|----|----|----|----|----|
| Q1 AR-3 옵션 | (g) 전체 통합 | (e) 단계적 | **GPT** | 1인 환경 균형 |
| Q2 PC-4 강제 형태 | 즉시 | 단계적 | **GPT** | 개발자 friction 회피 |
| Q8 T-5 β hard-block | 적극 확장 | audit-only | **GPT** | 보수적 + Evidence PASS 의존 |
| Q13 ST-1 형태 | entrypoint 변경 | downstream wrapper | **GPT** | Hermes ≠ root of trust 보존 |
| Q15 ST 통합 | Defense in depth | 환경별 분담 | **GPT** | 책무 분리 강화 |
| Group γ 묶음 | 통합 유지 | 분리 권고 | **GPT** | 위험 규모 분리 |

**패턴**: v2 차이 영역 권고 = **6/6 GPT 답습** — 일관성 (보수적 + 단계적 + Hermes ≠ root of trust 보존 + 책무 분리 강화 + 1인 환경 부담 최소화).

### C.4 양 vendor 미언급 / 추가 검토 영역 매트릭스 (내부 풀 3+1 합의 영역)

| 영역 | 사유 | 내부 합의 시 처리 |
|----|----|----|
| ADR-010 §X 본문 형태 | Vault HSM ST-4 = MVP-6 분리 영역 | Group γ-2 합의 시 결정 |
| Hermes upstream PR vs fork+downstream 책무 분담 | GPT 부분 언급 | Group γ-1 합의 시 결정 |
| AI agent / bot 권한 영역 분리 세부 | Gemini 부분 언급 | Group α 합의 시 결정 |
| Operational Readiness 6 기준 우선순위 | GPT 6 기준 답습 | Group γ-2 합의 시 결정 |
| Sandboxed Tier (T1) 구체 설계 | Gemini 권고 | Group β 합의 시 결정 |

---

**상태**: DRAFT (사용자 명시 승인 *전*, 파일화 + commit 0건)
**다음 단계**: 사용자 명시 결정 영역 (부록 A 옵션 A~H)
**주요 결정 필요 영역**:
- (a) **v1 보존 + v2 별도 권위 source** 접근 적절성 확인 (Amendment section vs 별도 v2 中 v2 선택 답습)
- (b) **8 지적 흡수 매트릭스** 적절성 확인 (Gap #1 ~ #8)
- (c) **GPT 권고 Group γ 분리 (γ-1 / γ-2) 흡수** 적절성 확인 ⭐
- (d) **4 그룹화 (II')** vs v1 (II) 3 그룹화 中 선택
- (e) **양 vendor 차이 영역 6/6 GPT 답습** 패턴 적절성 확인
- (f) **우선순위 v2** (α → β → γ-1 → γ-2) 적절성 확인
- (g) **차단 요인 v2** (외부 LLM 의뢰 ❌ 0건 + Backlog #6 미진입 HIGH + Implementation Evidence PASS 미발효 HIGH + Operational Readiness PASS 미발효 HIGH) 적절성 확인
- (h) **트리거 #7 부분 발화** (외부 LLM 응답 회수 완료) 평가 적절성 확인
- (i) **합의 형태 변경 0건** (풀 3+1 + 외부 LLM 1+ + 사용자 명시 + 외부 LLM 응답 입력 답습) 적절성 확인
- (j) **후속 다음 단계 우선순위** = (I) v2 commit / (II) Group α 풀 3+1 진입 / (III) Backlog #6 우선 진입 / (IV) Group γ-2 단축 / (V) MVP-2 / (VI) 세션 종료 中 권고
