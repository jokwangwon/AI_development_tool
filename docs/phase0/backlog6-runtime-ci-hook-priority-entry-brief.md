# Backlog #6 Runtime + CI-hook 우선 진입 Brief (준비안 — DRAFT)

> **본 문서는 Backlog #3 Group α (AR-3 + PC-4 T3 sub) 단독 풀 3+1 합의 (`4880e88` APPROVE WITH CONDITIONS, 3/3 만장일치) 발효 후속, 합의 C-1 조건 ("Backlog #6 미진입 시 *실 강제 적용 시점* 의존성 명시") 답습 한정 *우선 진입* brief 의 준비안.**
>
> 본 brief = *준비안 (DRAFT)* — 사용자 명시 승인 *전* 단계. 본 brief 의 어떤 §도 그 자체로 (i) Backlog #6 실 진입을 발효시키지 않으며, (ii) 합의 보고서 권위를 갖지 않으며, (iii) Group α 합의 조건 C-1 ~ C-12 中 어느 것도 *해소* 시키지 않는다.

**작성일**: 2026-05-14 후속
**상태**: DRAFT (사용자 명시 승인 *전*)
**상위 권위 (답습 한정)**:
- `docs/review/3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md` (Group α 단독 풀 3+1, commit `4880e88` APPROVE WITH CONDITIONS, 3/3 만장일치)
- `docs/phase0/backlog3-group-alpha-standalone-3plus1-brief.md` (Group α brief, commit `db0e3ac`, 687줄)
- `docs/review/3plus1-consensus-2026-05-12-backlog6-implementation-entry.md` (Layer B APPROVE, commit `f40423f`)
- `docs/review/3plus1-consensus-2026-05-12-backlog6-runtime-ci-hook-entry.md` (Layer A APPROVE, commit `f1e0b23`)
- `docs/architecture/implementation-runtime-roadmap-mvp1.md` §5.5 (9 sub-수단 본문 채택, commit `55c5b4b`)
- ADR-011 §2.1 (a)~(e) 5조건 패턴 + §2.4 T3 영역

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습

> "Backlog #6 Runtime + CI-hook 우선 진입 brief 를 작성해주세요. 범위는 Group α 합의 C-1 조건에 따라 Runtime + CI-hook 의존성을 먼저 정리하는 것입니다. branch protection 변경, dev 환경 강제, pre-commit install 의무화, Operational Readiness PASS, Hermes PMO 격상은 하지 마세요."

### 0.2 본 brief 가 *하는* 것

1. Group α 합의 C-1 조건 답습 — "Backlog #6 (Runtime + CI-hook) 미진입 시 *실 강제 적용 시점* 의존성 명시" *해소 준비* (§1)
2. **Runtime + CI-hook 영역 정의** + 의존 항목 enumeration (§2)
3. **Group α 14 결정 영역 × Runtime/CI-hook 의존성 매트릭스** (§3)
4. **사용자 명시 5 금지 영역 × Runtime+CI-hook 분리 매트릭스** (§4)
5. **의존성 해소 *순서* 권고** (자동 진입 0건, §5)
6. **Rollback Trigger 의존성 답습** — Group α 7 단계 승격 trigger + Layer B 18 trigger 통합 (§6)
7. 본 brief + 본 brief 발효 후 단계의 *금지 사항* enumerate (§7)
8. 본 brief 의 *합의 형태 권고* + 풀 3+1 승격 트리거 (§8)
9. 다음 단계 결정 옵션 (사용자 결정 영역, §9)

### 0.3 본 brief 가 *하지 않는* 것 (사용자 명시 답습)

**사용자 명시 5 금지 영역**:

- ❌ **branch protection 변경 (0건)** — AR-2 (CODEOWNERS + required status check) / direct push 차단 / force push 차단 / admin bypass OFF / required PR review count / linear history / deployments 모두 *변경 0건* (Group α 합의 5.1 #6 답습)
- ❌ **dev 환경 강제 (0건)** — `tools/doctor.py` 신규 도구 본문 작성 / dev 환경 검증 강제 / `pre-commit run` 의무 실행 모두 *0건*
- ❌ **`pre-commit install` 의무화 도입 (0건)** — `.pre-commit-config.yaml` 본문 작성 / opt-in → doctor → required 단계 진입 / `default_install_hook_types` 본문 결정 모두 *0건* (Group α 합의 5.2 #9 답습)
- ❌ **Operational Readiness PASS (Layer E) 선언 (0건)** — MVP-6 영역 분리 답습
- ❌ **Hermes PMO 격상 (Layer F) (0건)** — ADR-008 부록 C Hermes PMO Activation Cross-Reference 12 조건 미진입 답습

**추가 금지 영역 (본 brief 영역 외)**:

- ❌ **실 runtime code 구현 (0건)** — `tools/secret_scanner.py` / `tools/provider_import_scanner.py` / `tools/provider_url_scanner.py` / `src/adapters/llm/facade.py` / inotify sidecar / chmod 600 entrypoint script 본문 *0건*
- ❌ **실 CI workflow 구현 (0건)** — `.github/workflows/*.yml` 신설 / 본문 변경 *0건*
- ❌ **실 hook 구현 (0건)** — `.git/hooks/pre-commit` 본문 작성 / `.importlinter` 본문 변경 *0건*
- ❌ **Implementation Evidence PASS (Layer C) 발효 0건** + **MVP-1 PASS (Layer D) 선언 0건**
- ❌ **Group α 합의 C-1 ~ C-12 자동 변경 (0건)** — Group α 합의 본문 변경 0건
- ❌ **Group α 14 결정 영역 *재결정* (0건)** — 본 brief = Group α 합의 답습 한정
- ❌ **Layer A / Layer B / Layer C / Layer D 본문 변경 (0건)**
- ❌ **§5.5 9 sub-수단 본문 채택 변경 (0건)**
- ❌ **Group I (Hermes-originated commit auto-reject) 자동 진입 (0건)** — Group α 합의 C-2 답습 (별도 합의 영역)
- ❌ **Group β / γ-1 / γ-2 자동 진입 (0건)**
- ❌ **token rotation 정책 자동 결정 (0건)** — Group α 합의 C-3 답습 (별도 합의 영역)
- ❌ **GitHub plan / ruleset 가용성 자동 확인 (0건)** — Group α 합의 C-4 답습 (사용자 명시 확인 영역)
- ❌ **commit signing 도입 (0건)** — MVP-6 영역 답습
- ❌ **`pull_request_target` workflow 도입 (0건)** — T2/T3 별도 합의 영역
- ❌ **Tier-2 / Tier-3 catalog 자동 확장 (0건)**
- ❌ **threshold *고정* (0건)** — FP / FN / latency / `dev_env_install_rate ≥ 90%` 모두 *후보 한정* 유지
- ❌ **ADR 본문 자동 갱신 (0건)** — cross-reference 답습 한정
- ❌ **신규 ADR / 신규 P / 신규 GP 발행 (0건)**
- ❌ **합의 보고서 작성 (0건)** — 본 brief = *준비안 한정*
- ❌ **CONTEXT / INDEX / SESSION 메타 갱신 (0건)**
- ❌ **git commit / push (0건)**
- ❌ **외부 LLM 자동 호출 (0건)** — Group α 합의 C-11 답습 (응답 = 입력 한정)
- ❌ **실 API key / provider SDK / 외부 API 호출 (0건)**
- ❌ **인간 리뷰 의무 자동 발화 (0건)**

### 0.4 본 brief 의 권위 한계

본 brief = **준비안 (DRAFT)**. 본 brief 의 어떤 §도:

- (i) Backlog #6 실 진입을 *시작* 시키지 않으며,
- (ii) Group α 합의 C-1 ~ C-12 의 어느 조건도 *해소* 시키지 않으며 (의존성 *정리* 한정 — 해소 = Backlog #6 *실 진입 후* 영역),
- (iii) 5 금지 영역 (branch protection / dev 환경 강제 / `pre-commit install` 의무화 / Operational Readiness PASS / Hermes PMO 격상) 어느 것도 진입시키지 않으며,
- (iv) Layer A / Layer B / Layer C / Layer D / Group α 합의 본문을 *변경* 하지 않으며,
- (v) MVP-1 PASS / MVP-2 진입 / Operational Readiness PASS / Hermes PMO 격상을 *발생시키지 않는다*.

본 brief 가 발생시키는 *유일한* 효과는 **Group α 합의 C-1 답습 → Runtime + CI-hook 의존성 *정리* — 영역 정의 + 의존성 매트릭스 + 분리 매트릭스 + 순서 권고 + Rollback Trigger 의존성 + 금지 영역**. 모든 *진입 결정* 은 *사용자 명시 결정 영역*.

---

## 1. 진입 컨텍스트 답습

### 1.1 Group α 합의 발효 결과 답습 (`4880e88`)

| 영역 | 답습 |
|------|----|
| 합의 판정 | APPROVE WITH CONDITIONS (3/3 만장일치 — Agent A + B + C) |
| 합의 단위 | Group α 단독 (AR-3 + PC-4 T3 sub) |
| 합의 형태 | (가) 풀 3+1 + 외부 LLM 응답 답습 (입력 한정) + 사용자 명시 |
| 14 결정 영역 | AR-3 8 + PC-4 T3 sub 6 (3/3 만장일치 + P-1/P-2/P-3 부분 일치 통합 + G-1~G-6 누락 흡수) |
| 12 합의 조건 | C-1 ~ C-12 (모두 충족 시 = 본 합의 진입 적합) |
| 본 합의 권위 | "옵션 채택 권위 권고" 한정 — 실 적용 = Backlog #6 + 사용자 명시 결정 영역 |

### 1.2 C-1 조건 본문 답습

> **C-1**: Backlog #6 (Runtime + CI-hook) 미진입 시 ***실 강제 적용 시점*** 의존성 명시
> — A + B + C 일치 (3/3 만장일치 답습)

본 C-1 조건의 의미:

- (a) Group α 합의 발효 *자체* = 가능 (Backlog #6 미진입 무관 답습)
- (b) Group α 합의가 권고하는 *실 강제 적용* (branch protection rule 활성화 / `pre-commit install` 단계적 도입 / `pre-commit run --all-files` CI step 도입 / `tools/doctor.py` 신규 도구) = **모두 Backlog #6 영역**
- (c) C-1 *해소* = Backlog #6 진입 + 사용자 명시 결정 영역
- (d) 본 brief = C-1 *해소* 가 아닌 *의존성 정리 한정* — Backlog #6 진입 *직전* 의사결정 정비 영역

### 1.3 양 vendor 권고 답습 (Gemini + GPT 응답 — 입력 한정)

| 영역 | 양 vendor 답습 |
|------|------------|
| Backlog #6 우선 진입 권고 | 양 vendor 권고 답습 + 3 Agent 일치 (Group α 합의 §6.2) |
| 진입 우선순위 | 1순위 (실 강제 적용 의존성 해소) |
| 진입 조건 | Group α 합의 발효 후 (`4880e88` 완료) |

### 1.4 본 brief 의 진입점

본 brief 의 진입점:

```
Layer A APPROVE (f1e0b23) — Backlog #6 진입 기준 정의
Layer B APPROVE (f40423f) — 9 sub-수단 본문 채택 격상
§5.5 9 sub-수단 본문 채택 (55c5b4b) — 문서상 확정
   │
   ▼
backlog6-implementation-step-brief.md (Layer B 발효 후 — 5 Stage 22 sub-step 분할안)
   │
   ▼
Group α 단독 풀 3+1 합의 (4880e88 APPROVE WITH CONDITIONS 3/3 만장일치)
   │
   ▼
■ 본 brief = Group α 합의 C-1 답습 → Runtime + CI-hook 우선 진입 *준비안* (DRAFT)   ← 현 위치
   │
   ▼ (사용자 명시 승인 후)
brief 그대로 승인 합의 보고서 작성 또는 별도 결정
   │
   ▼ (사용자 명시 결정 후)
■ Backlog #6 실 진입 (Runtime + CI-hook 영역)                                       ← 본 brief 영역 외
   │
   ▼ (구현 + actual run SUCCESS + evidence 5/5 후)
Layer C 발효 합의 — Implementation Evidence PASS                                    ← 본 brief 영역 외
```

### 1.5 6-Layer 분리 매트릭스 현 상태 (2026-05-14 후속 9)

| Layer | 영역 | 상태 | 본 brief 관계 |
|-------|------|------|------------|
| Layer A | Backlog #6 Implementation Entry 기준 정의 | ✅ APPROVE (`f1e0b23`) | 답습 한정 |
| Layer B | 9 sub-수단 본문 채택 격상 | ✅ APPROVE (`f40423f` + §5.5 `55c5b4b`) | 답습 한정 (재결정 0건) |
| **Group α** | **AR-3 + PC-4 T3 sub 단독 풀 3+1 (T3 영역 권위 권고)** | ✅ **APPROVE WITH CONDITIONS (`4880e88`, 3/3 만장일치)** | **본 brief = C-1 답습 → Runtime + CI-hook 의존성 *정리*** |
| Layer C | Implementation Evidence PASS 발효 | ⏳ 아직 아님 | 본 brief 영역 외 |
| Layer D | MVP-1 PASS 선언 | ⏳ 아직 아님 | 본 brief 영역 외 |
| Layer E | Operational Readiness PASS 선언 | ⏳ 아직 아님 | 본 brief 영역 외 (사용자 명시 5 금지 #4) |
| Layer F | Hermes PMO 격상 | ⏳ 아직 아님 | 본 brief 영역 외 (사용자 명시 5 금지 #5) |

---

## 2. Runtime + CI-hook 영역 정의

### 2.1 Runtime + CI-hook 의 *범위* (Group α 합의 §6.2 답습)

본 brief 의 **Runtime + CI-hook 영역** = Group α 합의 §6.2 答습 + Layer A / Layer B 답습:

| 영역 | 정의 | 출처 |
|------|----|----|
| **R-1 CI workflow 영역** | `.github/workflows/*.yml` 신설 / 본문 변경 (Stage 1 + Stage 3 + Stage 4 + Stage 5 통합) | Layer B §5.5 + backlog6-implementation-step-brief §2 답습 |
| **R-2 CI step `pre-commit run --all-files`** | CI에서 `pre-commit run --all-files` 전체 리포트 실행 step 추가 | Group α 합의 5.2 #11 (`fail_fast: false` + CI `--all-files`) 답습 |
| **R-3 CI step `pre-commit run --files <changed>`** | 로컬 자연 빠른 피드백 (CI 영역 외 — 로컬 영역 분리) | Group α 합의 5.2 #11 답습 |
| **R-4 도구 본문 (tools/*.py)** | `tools/secret_scanner.py` (Group D 261줄 답습) / `tools/provider_import_scanner.py` (Group A 1차 답습) / `tools/provider_url_scanner.py` (Group A 3차 답습) | Layer B §5.5 + backlog6-implementation-step-brief §4.3 답습 |
| **R-5 `.importlinter` 본문** | TR-1~TR-5 답습 (5-vendor 차단 rule) | Group A 2차 합의 §5.5 답습 |
| **R-6 `.pre-commit-config.yaml` 본문** | `default_install_hook_types` + `fail_fast: false` + `minimum_pre_commit_version` 4.6.0 답습 | Group α 합의 5.2 #10 + #11 + #12 답습 |
| **R-7 docker secret block** | `docker-compose.yml` (또는 동등 매니페스트) docker secret 정의 | ADR-008 차단조건 #6 + 부록 B + Layer B Stage 2 답습 |
| **R-8 Evidence Artifact 생성** | Markdown report + JSONL entry + actual run SUCCESS URL | Layer B §1.8 (a)~(g) 답습 |
| **R-9 hook 실행 환경** | `pre-commit` framework 4.6.0 + 의존성 install | Group α 합의 5.2 #12 답습 |
| **R-10 `tools/doctor.py` 신규 도구** | dev 환경 검증 도구 (PC-4 T3 sub 단계적 진입 시 활용) | Group α 합의 5.2 #9 답습 |

### 2.2 사용자 명시 5 금지 영역 × Runtime + CI-hook 영역 분리

| 금지 영역 | Runtime + CI-hook 영역 *영향* | 본 brief 영역 |
|---------|-------------------------|------------|
| **branch protection 변경** | R-1 / R-2 / R-3 / R-4 / R-5 / R-6 / R-7 / R-8 / R-9 / R-10 *모두 영향 0건* (branch protection = GitHub Web UI / settings / ruleset 영역 — 코드 영역 분리) | 0건 |
| **dev 환경 강제** | R-10 `tools/doctor.py` 영역 *영향* — 본 brief = R-10 *의존성 enumerate 한정* (실 도구 본문 작성 / 실 강제 0건) | 0건 (의존성 정리 한정) |
| **`pre-commit install` 의무화** | R-6 `.pre-commit-config.yaml` 영역 *영향* — 본 brief = R-6 *의존성 enumerate 한정* (본문 작성 / 실 install 0건) | 0건 (의존성 정리 한정) |
| **Operational Readiness PASS** | R-1 ~ R-10 *모두 영향 0건* (Layer E = 운영 영역, R-1~R-10 = 구현 영역 — 영역 분리) | 0건 |
| **Hermes PMO 격상** | R-1 ~ R-10 *모두 영향 0건* (Layer F = governance 영역, R-1~R-10 = 코드 영역 — 영역 분리) | 0건 |

### 2.3 본 brief 영역 *내* Runtime + CI-hook 영역 (의존성 정리 적격)

| 영역 | 본 brief 영역 *내* 작업 | 본 brief 영역 *외* (Backlog #6 실 진입 후) |
|------|----------------------|--------------------------------------|
| R-1 (CI workflow) | 영향 받는 워크플로우 *enumerate 한정* | 실 신설 / 본문 변경 |
| R-2 (CI step `--all-files`) | step 추가 *의존성 enumerate 한정* | 실 step 추가 |
| R-3 (CI step `--files <changed>`) | 영역 분리 명시 (로컬 영역 답습 한정) | 본 brief 영역 외 (로컬 영역) |
| R-4 (도구 본문) | 답습 출처 *enumerate 한정* | 실 본문 변경 |
| R-5 (`.importlinter`) | TR-1~TR-5 답습 출처 *enumerate 한정* | 실 본문 변경 |
| R-6 (`.pre-commit-config.yaml`) | 의존성 *enumerate 한정* (사용자 명시 금지 #3 답습) | 본 brief 영역 외 (`pre-commit install` 의무화 = 별도 합의) |
| R-7 (docker secret block) | ADR-008 §2.6.2 답습 *enumerate 한정* | 실 본문 변경 |
| R-8 (Evidence Artifact) | Layer B §1.8 7 evidence 답습 *enumerate 한정* | 실 생성 (Layer C 시점) |
| R-9 (hook 실행 환경) | 의존성 *enumerate 한정* | 실 install |
| R-10 (`tools/doctor.py`) | 답습 출처 *enumerate 한정* (사용자 명시 금지 #2 답습) | 본 brief 영역 외 (dev 환경 강제 = 별도 합의) |

---

## 3. Group α 14 결정 영역 × Runtime/CI-hook 의존성 매트릭스

### 3.1 AR-3 8 결정 영역 × Runtime/CI-hook 의존성

| Group α 결정 # | 영역 | Runtime/CI-hook 의존성 | 본 brief 영역 (의존성 정리) | 5 금지 영역 충돌 |
|------------|------|---------------------|---------------------|--------------|
| #1 AR-2 형태 (e) | CODEOWNERS + required status check | R-1 (CI workflow required check 등록) | enumerate 한정 | **금지 #1 충돌** (실 branch protection 활성화 = 영역 외) |
| #2 AR-1 + AR-2 (e) 통합 | (e) → (g) 단계적 승격 trigger | R-1 + Rollback Trigger 답습 | enumerate 한정 | **금지 #1 충돌** (실 활성화 = 영역 외) |
| #3 Hermes auto-reject (β) | Group I 별도 합의 분리 | R-1 (workflow grep step 후속 가능성) | enumerate 한정 (Group I 자동 진입 0건) | 영향 0건 |
| #4 commit signing (Y) MVP-6 | 미진입 한정 (gap 근거 명시) | 영향 0건 | enumerate 한정 (MVP-6 영역 답습) | **금지 #4 #5 충돌** (MVP-6 = Operational Readiness / Hermes PMO 격상 영역 = 영역 외) |
| #5 fork PR (3) default + `pull_request_target` BLOCK | 현 default 정책 유지 | R-1 (workflow header 검증 가능성) | enumerate 한정 (`pull_request_target` 도입 0건) | 영향 0건 (default 답습 한정) |
| #6 branch protection 6 옵션 | (i)~(vi) 옵션별 채택 권고 | 영향 0건 (코드 영역 분리) | enumerate 한정 (옵션 권고 답습 한정) | **금지 #1 충돌** (실 활성화 = 영역 외) |
| #7 AI agent 권한 = (b) GitHub App | 최소 권한 + 서명 미적용 (현 시점) + 영역 분리 (α/β) | 영향 0건 (GitHub App 영역 = 인프라 영역) | enumerate 한정 | 영향 0건 (현 시점 미적용 답습) |
| #8 CODEOWNERS 핵심 경로 + GitHub plan (d) | 10 경로 + 현 plan 확인 (C-4) | R-1 (CODEOWNERS file 생성 후속 가능성) | enumerate 한정 (실 CODEOWNERS 생성 0건) | 영향 0건 (확인 영역) |

### 3.2 PC-4 T3 sub 6 결정 영역 × Runtime/CI-hook 의존성

| Group α 결정 # | 영역 | Runtime/CI-hook 의존성 | 본 brief 영역 (의존성 정리) | 5 금지 영역 충돌 |
|------------|------|---------------------|---------------------|--------------|
| #9 `pre-commit install` 단계적 | opt-in → doctor → required + STAGE 1~3차 trigger | R-6 + R-9 + R-10 | enumerate 한정 | **금지 #3 충돌** (`pre-commit install` 의무화 = 영역 외) |
| #10 `default_install_hook_types` | `pre-commit` + `commit-msg` 중심 + `pre-push` smoke check only | R-6 (`.pre-commit-config.yaml` 본문) | enumerate 한정 (본문 작성 0건) | **금지 #3 충돌** |
| #11 `fail_fast` | `false` + 로컬 `--files <changed>` + CI `--all-files` | R-2 + R-6 (`.pre-commit-config.yaml` 본문) | enumerate 한정 | **금지 #3 충돌** (R-6 본문 = 영역 외) |
| #12 `minimum_pre_commit_version` | 4.6.0 명시 | R-6 + R-9 (의존성 버전) | enumerate 한정 (실 명시 0건) | **금지 #3 충돌** |
| #13 로컬 hook 실패 시 정책 | "빠른 실패 + 명확한 복구 명령" | R-6 (`.pre-commit-config.yaml` 본문 또는 doctor 메시지) | enumerate 한정 | **금지 #2 #3 충돌** (dev 강제 / install 의무화 영역) |
| #14 `--no-verify` 차단 | branch protection + required CI 결합 (로컬 단독 차단 BLOCK) | R-1 (CI required check) | enumerate 한정 | **금지 #1 충돌** (branch protection 변경 = 영역 외) |

### 3.3 14 결정 영역 합산 — 본 brief 영역 *내 의존성 정리 적격* vs *외 (Backlog #6 실 진입 후 영역)*

| 영역 분류 | 결정 # 합산 | 본 brief 영역 |
|---------|---------|------------|
| 본 brief 영역 *내 의존성 정리 적격* (5 금지 충돌 0) | #3 / #5 / #7 / #8 (3 + 부분 답습 영역 포함 = 4건) | R-1 / R-4 / R-5 / R-7 / R-8 enumerate 한정 |
| 본 brief 영역 *외* (5 금지 충돌 — 별도 합의 영역) | #1 / #2 / #4 / #6 / #9 / #10 / #11 / #12 / #13 / #14 (10건) | 의존성 *enumerate 한정* (실 작업 = Backlog #6 실 진입 후 + 5 금지 해소 합의 후 영역) |

**합산**: 14 결정 영역 中 **10건 = 5 금지 영역 충돌** (실 적용 = 별도 합의 영역) + **4건 = 본 brief 영역 *내 의존성 정리 적격* (실 작업 0건 한정)**.

### 3.4 본 §3 의 *범위 한계*

본 §3 = **의존성 매트릭스 *정리 한정***. Group α 14 결정 영역 *재결정* 0건 + Group α 합의 본문 변경 0건 + 5 금지 영역 *해소* 0건.

---

## 4. 5 금지 영역 × Runtime+CI-hook 분리 매트릭스

### 4.1 금지 #1 — branch protection 변경 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 합의) |
|------|----------------|------------------------|
| AR-2 형태 (e) CODEOWNERS + required check 실 활성화 | ❌ (영역 외) | Group α 합의 발효 후 Backlog #6 진입 + 사용자 명시 결정 영역 |
| direct push 차단 / force push 차단 / admin bypass OFF | ❌ (영역 외) | 동상 |
| required PR review count = 0 | ❌ (영역 외) | 동상 (Group α 합의 5.1 #6 답습 — 옵션 권고 한정) |
| linear history / deployments | ❌ (영역 외) | 동상 (MVP-6 후속 영역) |
| **본 brief 영역 *내* 적격 작업** | **답습 *enumerate 한정* — 옵션 권고 답습 + Group α 합의 §6.2 의존성 매트릭스 정리** | — |

### 4.2 금지 #2 — dev 환경 강제 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 합의) |
|------|----------------|------------------------|
| `tools/doctor.py` 신규 도구 본문 작성 | ❌ (영역 외) | Backlog #6 실 진입 후 영역 |
| dev 환경 검증 강제 (doctor warning → required) | ❌ (영역 외) | R-MVP1-G3-PC4T3-STAGE 1~3차 trigger 발화 영역 |
| `pre-commit run` 의무 실행 | ❌ (영역 외) | 동상 |
| **본 brief 영역 *내* 적격 작업** | **R-10 도구 *의존성 enumerate 한정* (답습 출처 정리)** | — |

### 4.3 금지 #3 — `pre-commit install` 의무화 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 합의) |
|------|----------------|------------------------|
| `.pre-commit-config.yaml` 본문 작성 | ❌ (영역 외) | Backlog #6 실 진입 후 영역 |
| `default_install_hook_types` 본문 결정 | ❌ (영역 외) | 동상 |
| `pre-commit install` opt-in → doctor → required 단계 진입 | ❌ (영역 외) | 동상 (R-MVP1-G3-PC4T3-STAGE 1~3차) |
| `minimum_pre_commit_version` 4.6.0 명시 | ❌ (영역 외) | 동상 |
| **본 brief 영역 *내* 적격 작업** | **R-6 본문 *의존성 enumerate 한정* (Group α 합의 5.2 #9~#13 답습 출처 정리)** | — |

### 4.4 금지 #4 — Operational Readiness PASS (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 합의) |
|------|----------------|------------------------|
| Layer E (Operational Readiness PASS) 선언 | ❌ (영역 외) | MVP-6 영역 / Backlog #7 영역 |
| MVP-6 진입 (commit signing / Vault HSM / hosting provider alternative) | ❌ (영역 외) | 동상 |
| Operational parity check | ❌ (영역 외) | 동상 (Group α 합의 §6.3 답습) |
| **본 brief 영역 *내* 적격 작업** | **MVP-6 영역 *분리 명시 한정* (영역 외 답습)** | — |

### 4.5 금지 #5 — Hermes PMO 격상 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 합의) |
|------|----------------|------------------------|
| Layer F (Hermes PMO 격상) | ❌ (영역 외) | ADR-008 부록 C 12 조건 충족 + 별도 풀 3+1 + 외부 LLM 2+ + 인간 리뷰 의무 영역 |
| Hermes-originated commit auto-reject (Group I) | ❌ (영역 외) | Group α 합의 C-2 답습 (별도 합의 영역) |
| commit signing MVP-6 + Hermes PMO 격상 동시 발효 | ❌ (영역 외) | Group γ-2 cross-reference 영역 (Group α 합의 §6.3 답습) |
| **본 brief 영역 *내* 적격 작업** | **Hermes PMO 격상 영역 *분리 명시 한정* + Hermes ≠ root of trust 보존 답습** | — |

### 4.6 본 §4 의 *범위 한계*

본 §4 = **5 금지 영역 *분리 매트릭스 한정***. 5 금지 영역 어느 것도 *해소* 0건 + Backlog #6 실 진입 자동 진입 0건.

---

## 5. 의존성 해소 *순서* 권고

### 5.1 의존성 해소 그래프 (자동 진입 0건 — 사용자 명시 결정 영역)

```
Group α 합의 발효 (4880e88) ✅
   │
   ▼
■ 본 brief = Runtime + CI-hook 의존성 *정리* (DRAFT)        ← 현 위치 (사용자 명시 승인 영역)
   │
   ▼ (사용자 명시 승인 후 — 자동 진입 0건)
brief 그대로 승인 합의 보고서 작성 (Reviewer-only 단축 적격) OR 별도 결정
   │
   ▼ (사용자 명시 결정 후 — 자동 진입 0건)
┌─────────────────────────────────────────────────┐
│ Backlog #6 실 진입 단계 (5 금지 영역 분리 답습)        │
│                                                  │
│  Phase α (5 금지 충돌 0 영역 — 본 brief 권고)        │
│    ├── R-4 도구 본문 (Stage 1 + Stage 3)            │
│    ├── R-5 .importlinter 본문 (Stage 3)             │
│    ├── R-7 docker secret block (Stage 2)            │
│    └── R-1 CI workflow (Stage 4 통합)               │
│                                                  │
│  Phase β (5 금지 영역 의존 — 별도 합의 후 진입)         │
│    ├── R-6 .pre-commit-config.yaml (금지 #3 해소 후)  │
│    ├── R-10 tools/doctor.py (금지 #2 해소 후)        │
│    ├── R-2 CI step pre-commit --all-files            │
│    │       (금지 #3 해소 + R-6 후)                  │
│    └── branch protection 활성화 (금지 #1 해소 후)     │
│                                                  │
│  Phase γ (MVP-6 영역 분리 — 영역 외)                  │
│    ├── commit signing (금지 #4 / #5 해소 후)         │
│    ├── Vault HSM (금지 #4 해소 후)                   │
│    └── Operational Readiness PASS (금지 #4 해소 후)   │
└─────────────────────────────────────────────────┘
   │
   ▼ (Phase α 완료 + actual run SUCCESS + evidence 5/5 후 — 별도 합의 영역)
Layer C 발효 합의 — Implementation Evidence PASS              ← 본 brief 영역 외
```

### 5.2 Phase α 의 *진입 적격성* (5 금지 충돌 0 영역)

| 단계 | 영역 | 의존성 | 본 brief 권고 |
|-----|------|------|----------|
| α-1 | R-4 도구 본문 (Stage 1 + Stage 3) | Layer B §5.5 답습 + Group D + Group A PoC 답습 | Stage 1 + Stage 3 *병렬 진입 적격* (backlog6-implementation-step-brief §3 순서 A 답습) |
| α-2 | R-5 `.importlinter` 본문 (Stage 3) | TR-1~TR-5 답습 + Group A 2차 답습 | α-1 R-4 (provider_import_scanner) 와 *동시 진입 적격* |
| α-3 | R-7 docker secret block (Stage 2) | ADR-008 차단조건 #6 + 부록 B 답습 | α-1 / α-2 와 *독립 진입 적격* |
| α-4 | R-1 CI workflow (Stage 4 통합) | α-1 + α-2 + α-3 완료 후 통합 | α-1 ~ α-3 *완료 후* 진입 |

**Phase α 합산**: 4 단계 (α-1 ~ α-4) — 5 금지 영역 충돌 0건 + Layer B §5.5 답습 한정 + 본 brief 권고 영역 (실 진입 = Backlog #6 + 사용자 명시 결정 영역).

### 5.3 Phase β 의 *별도 합의 의존성* (5 금지 영역 해소 의존)

| 단계 | 영역 | 의존 5 금지 | 해소 합의 영역 |
|-----|------|---------|-----------|
| β-1 | R-6 `.pre-commit-config.yaml` 본문 | 금지 #3 (`pre-commit install` 의무화) | 별도 합의 + 사용자 명시 결정 영역 |
| β-2 | R-10 `tools/doctor.py` 신규 도구 | 금지 #2 (dev 환경 강제) | 별도 합의 + R-MVP1-G3-PC4T3-STAGE 1차 발화 영역 |
| β-3 | R-2 CI step `pre-commit run --all-files` | 금지 #3 (R-6 본문 의존) | β-1 후 + 별도 합의 |
| β-4 | branch protection 활성화 (AR-2 (e)) | 금지 #1 (branch protection 변경) | Backlog #3 Group α 합의 발효 후 + 사용자 명시 결정 영역 (Group α 합의 §6.2 답습) |

**Phase β 합산**: 4 단계 (β-1 ~ β-4) — 5 금지 영역 의존 (별도 합의 영역) + 본 brief 영역 외.

### 5.4 Phase γ 의 *MVP-6 영역 분리* (영역 외)

| 단계 | 영역 | 분리 사유 |
|-----|------|------|
| γ-1 | commit signing 도입 (AR-3 #4) | MVP-6 영역 답습 (금지 #4 + #5 동시 의존) |
| γ-2 | Vault HSM ST-4 통합 | MVP-6 영역 답습 (Group γ-2 분리) |
| γ-3 | Operational Readiness PASS (Layer E) | 금지 #4 답습 (MVP-6 영역) |
| γ-4 | Hermes PMO 격상 (Layer F) | 금지 #5 답습 (ADR-008 부록 C 12 조건 영역) |

**Phase γ 합산**: 4 단계 (γ-1 ~ γ-4) — MVP-6 영역 답습 + 본 brief 영역 외.

### 5.5 권고 진입 순서 (사용자 명시 결정 영역 — 자동 진입 0건)

| 우선순위 | 영역 | 본 brief 권고 |
|--------|------|----------|
| 1순위 | **Phase α-1 + α-2 + α-3** (5 금지 충돌 0 + 양 GP 본문 검출 + 저장 isolation) | 병렬 진입 적격 (backlog6-implementation-step-brief §3 순서 A 답습) |
| 2순위 | **Phase α-4** (R-1 CI workflow 통합) | α-1 ~ α-3 완료 후 |
| 3순위 | **Layer C 발효 합의 진입** (Implementation Evidence PASS) | α-1 ~ α-4 완료 + evidence 5/5 후 (별도 합의 영역) |
| 4순위 | **Phase β** (5 금지 #1~#3 해소 의존) | 별도 합의 + 사용자 명시 결정 영역 (본 brief 권고 0건) |
| 5순위 | **Phase γ** (MVP-6 영역) | 영역 외 답습 |

### 5.6 본 §5 의 *범위 한계*

본 §5 = **의존성 해소 *순서 권고 한정***. 자동 진입 0건 + 5 금지 영역 *해소* 0건 + Layer C 발효 0건.

---

## 6. Rollback Trigger 의존성 답습

### 6.1 Group α 합의 7 단계 승격 Trigger 답습 (Agent C 신규 흡수)

본 §은 **Group α 합의 §7.2 7 단계 승격 trigger 답습 한정** — *발화 0건* + 본 brief 영역 *내 의존성 정리 한정*:

| Trigger | 단계 | 발화 조건 | Runtime + CI-hook 의존성 | 본 brief 영역 |
|--------|----|----|---------------------|------------|
| R-MVP1-G5-AR3-STAGE 1차 | required status check 도입 | Group α 합의 발효 + Backlog #6 연결 | R-1 (CI required check 등록) | 의존성 *enumerate 한정* (5 금지 #1 충돌 — 실 발화 = 영역 외) |
| R-MVP1-G5-AR3-STAGE 2차 | CODEOWNERS 핵심 경로 적용 | required check 안정화 후 | R-1 (CODEOWNERS file) | 동상 |
| R-MVP1-G5-AR3-SIGNING | commit signing 도입 | MVP-6 발효 시 | 영향 0건 (MVP-6 영역) | 영역 외 (금지 #4 답습) |
| R-MVP1-G5-AR3-MERGE-RESTRICT | merge restriction 도입 | Hermes PMO 격상 시 | 영향 0건 (Layer F 영역) | 영역 외 (금지 #5 답습) |
| R-MVP1-G3-PC4T3-STAGE 1차 | opt-in → doctor warning | Implementation Evidence PASS 발효 | R-10 (`tools/doctor.py`) | 영역 외 (금지 #2 답습) |
| R-MVP1-G3-PC4T3-STAGE 2차 | doctor → required check | `dev_env_install_rate ≥ 90%` 측정 후 (정량 *후보 한정*) | R-1 + R-6 + R-10 | 영역 외 (금지 #2 #3 답습) |
| R-MVP1-G3-PC4T3-STAGE 3차 | required → hook stage 확장 | MVP-6 발효 시 + commit signing 동시 | R-6 (`default_install_hook_types` 확장) | 영역 외 (금지 #3 #4 #5 답습) |

### 6.2 Layer B 18 Rollback Trigger 답습 (backlog6-implementation-step-brief §6 답습)

| Trigger 합산 | 본문 확정 | 본 brief 영역 |
|-----------|------|------------|
| GP-3 8 trigger (R-MVP1-G3-1 ~ G3-8) | 18/18 본문 확정 답습 (Layer B §1.7 답습) | 답습 한정 — 발화 0건 |
| GP-5 10 trigger (R-MVP1-G5-1 ~ G5-10) | 동상 | 동상 |

### 6.3 본 §6 의 *범위 한계*

본 §6 = **Rollback Trigger *본문 확정 답습 한정***. 발화 0건 + threshold 정량 *고정 0건* (`dev_env_install_rate ≥ 90%` 포함 모두 *후보 한정* 유지).

---

## 7. 금지 사항

### 7.1 본 brief 자체 금지 사항 (사용자 명시 답습)

| # | 금지 영역 | 본 brief 위반 |
|---|---------|------------|
| 1 | **branch protection 변경** (사용자 명시 5 금지 #1) | 0건 |
| 2 | **dev 환경 강제** (사용자 명시 5 금지 #2) | 0건 |
| 3 | **`pre-commit install` 의무화 도입** (사용자 명시 5 금지 #3) | 0건 |
| 4 | **Operational Readiness PASS (Layer E) 선언** (사용자 명시 5 금지 #4) | 0건 |
| 5 | **Hermes PMO 격상 (Layer F)** (사용자 명시 5 금지 #5) | 0건 |
| 6 | 실 runtime code 구현 | 0건 |
| 7 | 실 CI workflow 구현 | 0건 |
| 8 | 실 hook 구현 | 0건 |
| 9 | Implementation Evidence PASS (Layer C) 발효 | 0건 |
| 10 | MVP-1 PASS (Layer D) 선언 | 0건 |
| 11 | Group α 합의 C-1 ~ C-12 자동 변경 | 0건 |
| 12 | Group α 14 결정 영역 *재결정* | 0건 |
| 13 | Layer A / Layer B / Layer C / Layer D 본문 변경 | 0건 |
| 14 | §5.5 9 sub-수단 본문 채택 변경 | 0건 |
| 15 | Group I (Hermes-originated commit auto-reject) 자동 진입 | 0건 |
| 16 | Group β / γ-1 / γ-2 자동 진입 | 0건 |
| 17 | token rotation 정책 자동 결정 | 0건 |
| 18 | GitHub plan / ruleset 가용성 자동 확인 | 0건 |
| 19 | commit signing 도입 | 0건 |
| 20 | `pull_request_target` workflow 도입 | 0건 |
| 21 | Tier-2 / Tier-3 catalog 자동 확장 | 0건 |
| 22 | threshold *고정* (FP / FN / latency / `dev_env_install_rate ≥ 90%` 등 = 후보 한정) | 0건 |
| 23 | ADR 본문 자동 갱신 (cross-reference 답습 한정) | 0건 |
| 24 | 신규 ADR / 신규 P / 신규 GP 발행 | 0건 |
| 25 | 합의 보고서 작성 (본 brief = 준비안 한정) | 0건 |
| 26 | CONTEXT / INDEX / SESSION 메타 갱신 | 0건 |
| 27 | git commit / push | 0건 |
| 28 | 외부 LLM 자동 호출 (Group α 합의 C-11 답습 — 응답 = 입력 한정) | 0건 |
| 29 | 외부 LLM 응답 결론 강제 채택 (Group α 합의 C-11 답습) | 0건 |
| 30 | 실 API key / provider SDK / 외부 API 호출 | 0건 |
| 31 | 인간 리뷰 의무 자동 발화 | 0건 |
| 32 | 17 항목 우선순위 자동 *재고정* | 0건 |
| 33 | MVP-2 ~ MVP-6 본문 deepening | 0건 |

### 7.2 본 brief 발효 *후* Backlog #6 실 진입 단계 금지 사항 (Phase α 한정 — 의무 답습)

| # | 금지 영역 | 사유 |
|---|---------|------|
| 1 | Phase β 영역 진입 (R-6 본문 작성 / R-10 본문 작성 / R-2 step 추가 / branch protection 활성화) | 사용자 명시 5 금지 #1 #2 #3 답습 — 별도 합의 영역 |
| 2 | Phase γ 영역 진입 (commit signing / Vault HSM / Operational Readiness PASS / Hermes PMO 격상) | 사용자 명시 5 금지 #4 #5 답습 — MVP-6 영역 |
| 3 | 9 sub-수단 외 수단 도입 (gitleaks / detect-secrets / trufflehog / depcruise / grimp / ruff 등) | Backlog #1 + #2 1.5차 보강 영역 분리 |
| 4 | `src/adapters/llm/facade.py` real 본문 작성 | Backlog #4 P1 v2 facade MVP 합의 영역 분리 |
| 5 | Hermes upstream Dockerfile 변경 (ST-1 / ST-2 / ST-5) | Backlog #1 1.5차 보강 영역 분리 (풀 3+1 합의) |
| 6 | Tier-2 / Tier-3 catalog 확장 (R-4.1 Tier-1 / URL Tier-1 10 / Model Tier-1 19 변경) | Backlog #3 별도 합의 영역 (Group β 별도 합의) |
| 7 | ADR 본문 자동 갱신 (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012) | cross-reference 답습 한정 — Layer C 발효 후 별도 commit 영역 |
| 8 | event enum 정식 등록 (`event:` field) | Backlog #5 ADR-012 §2.2 schema 진화 정책 별도 합의 |
| 9 | `pull_request_target` workflow 도입 | T2/T3 별도 합의 영역 (Group α 합의 5.1 #5 (3) 답습) |
| 10 | local pre-commit framework 활성화 (PC-1 / PC-4 실 install) | Backlog #1 + #2 1.5차 보강 영역 분리 (사용자 명시 5 금지 #3 답습) |
| 11 | Layer 2 runtime block (G5-5) 진입 | MVP-3/4 영역 분리 |
| 12 | 의미적 lock-in (G4 §4.6 라운드트립 검증) 진입 | MVP-3 영역 분리 |
| 13 | 실 API key / provider SDK / 외부 API 호출 | 영구 금지 (fake canary 의무 답습) |
| 14 | 실 secret 본문 commit | 영구 금지 (R-4.1 + Group D §1.2 #1 답습) |
| 15 | F-금지 위반 (workflow 본문 secret 토큰 사용 등) | 영구 금지 (G3-7 (i) 답습) |
| 16 | Layer C (Implementation Evidence PASS) 자동 발효 (사용자 명시 결정 미충족 시) | ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 결정 영역 |
| 17 | Hermes-originated commit auto-reject (Group I) 자동 진입 | Group α 합의 C-2 답습 (Group I 별도 합의 영역) |
| 18 | token rotation 정책 자동 결정 | Group α 합의 C-3 답습 (별도 합의 영역) |

본 §7 = **사용자 명시 답습 한정** — 본 brief 발효 후 Phase α 단계에서 위 18 금지 영역 위반 0건 유지 의무.

---

## 8. 합의 형태 권고 + 풀 3+1 승격 트리거

### 8.1 본 brief 의 합의 형태 권고

| 합의 영역 | 합의 형태 권고 | 사유 |
|---------|----------|------|
| 본 brief 자체 (DRAFT — 준비안) | **사용자 명시 승인 한정 (합의 보고서 0건)** | 본 brief = 준비안 한정 — 합의 보고서 권위 갖지 않음 |
| brief 승인 후 합의 진입 | **Reviewer-only 단축 합의 적격** | Group α 합의 답습 한정 + 5 금지 영역 *재결정* 0건 + 본 brief = 의존성 *정리 한정* (의존성 *해소* 0건) |
| Phase α 진입 시 합의 | **별도 합의 — Reviewer-only 단축 또는 풀 3+1** | Layer B §5.5 9 sub-수단 본문 채택 답습 + Phase α = 5 금지 충돌 0 영역 한정 (사용자 명시 결정 영역) |
| Phase β / γ 진입 시 합의 | **별도 풀 3+1 + 사용자 명시** | 5 금지 영역 해소 의존 — 사용자 명시 결정 영역 |

### 8.2 풀 3+1 승격 트리거 후보 (본 brief 영역)

본 brief 가 풀 3+1 합의로 *승격* 되어야 할 trigger 후보:

| # | 트리거 | 본 brief 발화 |
|---|----|----------|
| 1 | 본 brief 가 Group α 합의 C-1 ~ C-12 어느 것의 *재결정* 을 권고하는 경우 | 0건 — 본 brief = Group α 합의 답습 한정 |
| 2 | 본 brief 가 사용자 명시 5 금지 영역 (branch protection / dev 환경 강제 / `pre-commit install` 의무화 / Operational Readiness PASS / Hermes PMO 격상) 中 1+ 의 *해소* 를 권고하는 경우 | 0건 — 본 brief = 5 금지 영역 *분리 매트릭스 한정* (해소 0건) |
| 3 | 본 brief 가 Layer B §5.5 9 sub-수단 *재결정* 을 권고하는 경우 | 0건 — 본 brief = 답습 한정 |
| 4 | 본 brief 가 Provider Liquidity 5-way 약화 가능성을 포함하는 경우 | 0건 — 본 brief = enforcement layer 영역 (catalog / provider 영역과 직교 답습) |
| 5 | 본 brief 가 5 영구 핵심 제약 (Hermes ≠ root of trust / 단일 source-of-truth / 수단/목적 분리 / T1/T2/T3 분리 / SPOF 의도적 수용) 中 1+ 의 약화를 포함하는 경우 | 0건 — 본 brief = 5/5 보존 답습 |
| 6 | 본 brief 가 T3 영역 진입을 권고하는 경우 (branch protection / Vault HSM / Tier-2/3 catalog 확장 등) | 0건 — 본 brief = T3 영역 *분리 명시 한정* (진입 0건) |
| 7 | 본 brief 가 ADR-008 부록 C Hermes PMO Activation 12 조건 중 1+ 의 충족을 발생시키는 경우 | 0건 — 본 brief = Hermes PMO 격상 영역 *분리 명시 한정* |

**본 brief 검토 결과 = 7/7 트리거 0건 발화** (본 brief = Group α 합의 답습 + 5 금지 분리 매트릭스 + Layer B §5.5 답습 한정 + 5 영구 핵심 제약 5/5 보존 + Provider Liquidity 5-way 100% 보존).

→ 본 brief 승인 후 합의 = **Reviewer-only 단축 합의 적격** 확정 (사용자 명시 결정 시).

### 8.3 본 §8 의 *범위 한계*

본 §8 = *합의 형태 권고 한정*. 실 합의 형태 결정 = 사용자 명시 결정 영역.

---

## 9. 다음 단계 결정 옵션 (사용자 결정 영역)

본 brief 작성 후 다음 작업 (사용자 결정 영역, 자동 진입 0건):

| 옵션 | 영역 | 다음 단계 |
|-----|------|--------|
| **(A)** | **본 brief 그대로 승인 → Reviewer-only 단축 합의 진입** | 합의 보고서 작성 (`docs/review/3plus1-consensus-2026-05-14-backlog6-runtime-ci-hook-priority-entry.md`) |
| (B) | 본 brief 수정 요청 → 수정 후 승인 | brief v2 작성 (사용자 명시 수정 영역 반영) |
| (C) | 본 brief 일부만 채택 → 부분 합의 | brief 부분 채택 영역 명시 + 합의 보고서 작성 |
| (D) | 본 brief 승인 → 합의 보류 → **Phase α (R-4 + R-5 + R-7 + R-1) 실 진입 brief 작성** | Phase α 실 진입 단계 brief 작성 (사용자 명시 결정 영역) |
| (E) | 본 brief 승인 → **Group I (Hermes-originated commit auto-reject) 별도 합의 진입 brief 작성** | Defense in depth 결합 권고 (Group α 합의 §6.1 + C-2 답습) |
| (F) | 본 brief 승인 → **token rotation 정책 별도 합의 진입 brief 작성** | Group α 합의 C-3 답습 |
| (G) | 본 brief 승인 → **GitHub plan / ruleset 가용성 확인 단계 진입** | Group α 합의 C-4 답습 (사용자 명시 확인 영역) |
| (H) | 본 brief 보류 → 다른 backlog 우선 진입 | Backlog 中 사용자 명시 결정 영역 진입 |
| (I) | 본 brief 폐기 → 별도 접근 | 별도 brief 또는 별도 합의 영역 |
| (J) | 본 brief 작성 한정 → 세션 종료 | 다음 세션에서 사용자 명시 결정 |

### 9.1 권고 시작 명령 (사용자 권한 영역)

- **(A) 권고**: "옵션 (A) 로 진행해주세요. 본 brief 를 그대로 승인하고, Reviewer-only 단축 합의 보고서 작성 단계로 진입하겠습니다."
- (B): "옵션 (B) 로 진행해주세요. 본 brief 의 §X 를 다음과 같이 수정해주세요: ..."
- (C): "옵션 (C) 로 진행해주세요. 본 brief 中 §X, §Y 만 채택하고 합의 보고서를 작성해주세요."
- (D): "옵션 (D) 로 진행해주세요. Phase α (R-4 + R-5 + R-7 + R-1) 실 진입 brief 작성으로 전환합니다."
- (E): "옵션 (E) 로 진행해주세요. Group I (Hermes-originated commit auto-reject) 별도 합의 진입 brief 작성."
- (F): "옵션 (F) 로 진행해주세요. token rotation 정책 별도 합의 진입 brief 작성."
- (G): "옵션 (G) 로 진행해주세요. GitHub plan / ruleset 가용성 확인 단계 진입."
- (H): "옵션 (H) 로 진행해주세요. Backlog #X 진입 brief 작성으로 전환합니다."
- (I): "옵션 (I) 로 진행해주세요. 본 brief 폐기 + 별도 brief 작성."
- (J): "옵션 (J) 로 진행해주세요. 세션 종료."

### 9.2 본 §9 의 *범위 한계*

본 §9 = *결정 옵션 enumeration 한정*. 실 다음 단계 결정 = 사용자 명시 결정 영역 (자동 진입 0건).

---

## 10. 본 brief 메타 검증

| 메타 검증 | 본 brief |
|---------|--------|
| 사용자 명시 진입 명령 답습 | ✅ (2/2 — Group α 합의 C-1 답습 / Runtime + CI-hook 의존성 *정리*) |
| 사용자 명시 5 금지 답습 | ✅ (5/5 — branch protection 변경 0건 / dev 환경 강제 0건 / `pre-commit install` 의무화 0건 / Operational Readiness PASS 0건 / Hermes PMO 격상 0건) |
| Group α 합의 C-1 답습 | ✅ (의존성 *정리 한정*, 해소 0건) |
| Group α 합의 C-2 ~ C-12 답습 | ✅ (C-2 Group I 자동 진입 0건 / C-3 token rotation 자동 결정 0건 / C-4 GitHub plan 자동 확인 0건 / C-5~C-12 답습) |
| Group α 14 결정 영역 답습 | ✅ (재결정 0건 — 의존성 매트릭스 정리 한정) |
| Layer A / Layer B / §5.5 답습 | ✅ (본문 변경 0건) |
| Layer B 18 Rollback Trigger 답습 | ✅ (발화 0건) |
| Group α 7 단계 승격 Trigger 답습 | ✅ (발화 0건) |
| 5 영구 핵심 제약 보존 | ✅ (Hermes ≠ root of trust / 단일 source-of-truth / 수단/목적 분리 / T1/T2/T3 분리 / SPOF 의도적 수용 5/5 보존) |
| Provider Liquidity 5-way 100% 보존 | ✅ (본 brief = enforcement layer 영역 = catalog / provider 영역과 직교) |
| 7 backlog 분리 매트릭스 답습 | ✅ (Backlog #1 / #2 / #3 / #4 / #5 / #7 모두 분리 명시) |
| 풀 3+1 승격 트리거 0/7 발화 | ✅ (§8.2 답습) |
| 자동 진입 0건 | ✅ (모든 다음 단계 = 사용자 명시 결정 영역) |

---

## 11. 본 brief 요약 (한 단락)

본 brief 는 **Backlog #3 Group α (AR-3 + PC-4 T3 sub) 단독 풀 3+1 합의 (`4880e88` APPROVE WITH CONDITIONS 3/3 만장일치) 발효 후속**, 합의 C-1 조건 ("Backlog #6 미진입 시 *실 강제 적용 시점* 의존성 명시") 답습 한정 *우선 진입* 준비안 (DRAFT) 이다. **사용자 명시 5 금지** (branch protection 변경 / dev 환경 강제 / `pre-commit install` 의무화 / Operational Readiness PASS / Hermes PMO 격상) 5/5 답습. **Runtime + CI-hook 영역을 R-1 ~ R-10 (10 영역) 으로 정의** + **Group α 14 결정 영역 × Runtime/CI-hook 의존성 매트릭스** (5 금지 충돌 0 영역 4건 + 충돌 영역 10건) + **5 금지 영역 × Runtime+CI-hook 분리 매트릭스** + **의존성 해소 순서 권고** (Phase α 5 금지 충돌 0 영역 = R-4 + R-5 + R-7 + R-1 / Phase β 5 금지 의존 영역 = 별도 합의 / Phase γ MVP-6 영역 = 영역 외) + **Rollback Trigger 의존성 답습** (Group α 7 단계 승격 + Layer B 18 trigger 발화 0건) + **본 brief 자체 금지 33 + Phase α 단계 금지 18** + **합의 형태 권고** (Reviewer-only 단축 — 7 풀 3+1 트리거 0/7 발화) 를 정리한다. **본 brief 는 Backlog #6 실 진입을 *시작* 시키지 않으며, 5 금지 영역 *해소* / Layer C 발효 / MVP-1 PASS / Operational Readiness PASS / Hermes PMO 격상 / Group α 합의 본문 변경 / 14 결정 영역 *재결정* / 합의 보고서 작성 / 메타 갱신 / commit / push 모두 본 brief 영역 외**. 다음 단계는 사용자 명시 결정 영역 (옵션 A~J, §9 답습).

---

**작성일**: 2026-05-14 후속
**상태**: DRAFT (사용자 명시 승인 *전*)
**다음 단계**: 사용자 명시 결정 영역 (옵션 A~J, §9 답습)
**금지 (사용자 명시 답습 — 본 brief 영역)**:
- ❌ **branch protection 변경** (사용자 명시 5 금지 #1)
- ❌ **dev 환경 강제** (사용자 명시 5 금지 #2)
- ❌ **`pre-commit install` 의무화 도입** (사용자 명시 5 금지 #3)
- ❌ **Operational Readiness PASS (Layer E) 선언** (사용자 명시 5 금지 #4)
- ❌ **Hermes PMO 격상 (Layer F)** (사용자 명시 5 금지 #5)
- ❌ 실 runtime code 구현
- ❌ 실 CI workflow 구현
- ❌ 실 hook 구현
- ❌ Implementation Evidence PASS (Layer C) 발효
- ❌ Group α 합의 C-1 ~ C-12 자동 변경
- ❌ Group α 14 결정 영역 *재결정*
- ❌ 합의 보고서 작성 (본 brief = 준비안 한정)
- ❌ CONTEXT / INDEX / SESSION 메타 갱신
- ❌ git commit / push
- ❌ §5.5 9 sub-수단 본문 채택 변경
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ threshold 자동 고정
- ❌ Group I / Group β / γ-1 / γ-2 자동 진입
- ❌ token rotation 정책 자동 결정
- ❌ commit signing 도입
- ❌ `pull_request_target` workflow 도입
- ❌ 외부 LLM 자동 호출
- ❌ 실 API key / provider SDK / 외부 API 호출
- ❌ 인간 리뷰 의무 자동 발화
