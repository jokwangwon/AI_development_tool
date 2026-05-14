# §C-5c PC-4 T2 sub — Backlog #1 + Backlog #2 통합 검토 *준비안* Brief (DRAFT)

> **본 brief = §C-5c (PC-4 local pre-commit framework) 中 T2 sub 영역 (`.pre-commit-config.yaml` config 정의 가능성) 의 *Backlog #1 + Backlog #2 공유 통합 검토* 준비안 (DRAFT)** — Backlog #1 단독 진입 (옵션 α) 가 아닌 통합 진입 (옵션 β) 방향 한정 검토.
>
> 본 brief 의 어떤 §도 그 자체로 (i) §C-5c Satisfied / 부분 Satisfied 갱신, (ii) Backlog #1 / #2 1.5차 Satisfied 갱신, (iii) MVP-1 PASS 재선언, (iv) `.pre-commit-config.yaml` 실 본문 작성, (v) `pre-commit install` 의무화 / dev 환경 강제, (vi) branch protection 변경, (vii) T3 영역 자동 진입, (viii) Operational Readiness PASS / Hermes PMO 격상, (ix) 다른 backlog 자동 진입을 발생시키지 않는다.

**작성일**: 2026-05-14 후속 1
**상태**: DRAFT (사용자 명시 승인 *전*)
**선행 brief**: `docs/phase0/backlog1-c5c-pc4-t2-sub-brief.md` (commit `11d7ebb`) — Backlog #1 단독 한정 가능성 분석 답습
**상위 권위**:
- §C-5a 갱신 합의 = `docs/review/3plus1-consensus-2026-05-13-st2-c5a-satisfaction.md` (commit `6fa87dc`) — §C-5 = `Partially Satisfied (C-5a only)` / C-5b·C-5c = `Deferred` 보존
- Backlog #1 진입 직전 사전 정비 합의 = `docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md` (commit `43b898c`)
- MVP-1 PASS (Layer D) 합의 = `docs/review/3plus1-consensus-2026-05-13-mvp1-pass.md` (commit `210c98f`, APPROVE WITH CONDITIONS)
- `docs/architecture/implementation-runtime-roadmap-mvp1.md` §3 (GP-3) + §4 (GP-5) + §4.3.1 (PC-1 ~ PC-4 매트릭스) + §4.5.2 (metric/threshold) + §4.7.3 (합의 형태 권고) + §5.5.1 (GP-3 4 sub-수단) + §5.5.2 (GP-5 3 sub-수단) — 양 GP PC-3 일관 채택 답습
- `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.4 (T1/T2/T3 3-tier 분류)
- ADR-011 §2.1 (a)~(e) 5조건 패턴
- Backlog #1 deepening brief §2.3.3 (PC-4 T2/T3 sub-영역 분리) + §2.3.4 (Backlog #1 + #2 통합 권고)

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습 (2026-05-14 후속 1)

> "PC-4 T2 sub 는 Backlog #1 단독이 아니라 Backlog #1 + Backlog #2 통합 검토 brief 로 이어가 주세요. 구현은 아직 하지 않습니다."

> 검토 영역 (사용자 명시):
> 1. GP-3 local hook 후보 (secret scanner / workflow secret usage check / workflow permissions check)
> 2. GP-5 local hook 후보 (provider import scanner / provider URL/model scanner / import-linter)
> 3. 공통 pre-commit config 구조 (repo-local hooks / pass·fail 기준 / runtime 비용 / false positive 위험 / CI-only enforcement 와의 관계)
> 4. T2/T3 분리 (`.pre-commit-config.yaml` 본문 정의 = T2 / `pre-commit install` 의무화 = T3 또는 별도 정책 / dev 환경 강제 = 이번 범위 밖)
> 5. 금지 사항 (`pre-commit install` 강제 / dev 환경 강제 / branch protection / Operational Readiness PASS / Hermes PMO 격상)

### 0.2 본 brief 가 *하는* 것

1. Backlog #1 (GP-3) + Backlog #2 (GP-5) 공유 PC-4 영역의 *통합 가능성* 검토 (§1 ~ §2)
2. GP-3 local hook 3 후보 + GP-5 local hook 3 후보 = 합산 6 후보 카탈로그 (§3)
3. 공통 `.pre-commit-config.yaml` config 구조 분석 (§4) — repo-local hooks / pass·fail 기준 / runtime 비용 / false positive 위험 / CI-only enforcement 와의 관계
4. T2/T3 분리 명시 (§5) — `.pre-commit-config.yaml` 본문 정의 = T2 / `pre-commit install` 의무화 = T3 또는 별도 정책 / dev 환경 강제 = 본 brief 범위 밖
5. 합의 형태 권고 + 풀 3+1 승격 트리거 검증 (§6)
6. T2 sub 통합 발효 *시점* 의무 정리 (Rollback Trigger / Evidence) — 본 brief 영역 외 명시 (§7)
7. 본 brief 자체 + 후속 단계 *금지 사항* enumerate (§8)
8. 다음 단계 결정 옵션 (사용자 결정 영역, §9)

### 0.3 본 brief 가 *하지 않는* 것 (사용자 명시 5 금지 답습)

- ❌ **`pre-commit install` 강제 0건** — 모든 개발자 dev 환경 install 의무 명시 0건
- ❌ **dev 환경 강제 0건** — `.pre-commit-config.yaml` 가 repo 에 존재해도 dev 환경 강제 의무 부여 0건 (opt-in 한정 검토)
- ❌ **branch protection 변경 0건** — AR-2 / AR-3 / GitHub repo policy 변경 검토 0건 (Backlog #3 T3 영역)
- ❌ **Operational Readiness PASS (Layer E) 선언 0건** — MVP-6 영역 (C-3 Deferred 답습)
- ❌ **Hermes PMO 격상 (Layer F) 0건** — MVP-6 영역 (C-4 Deferred 답습 + 외부 LLM cross-vendor blind + 사람 리뷰 의무)

### 0.4 본 brief 가 *하지 않는* 것 (사용자 명시 8 추가 금지 답습)

- ❌ **`.pre-commit-config.yaml` 실 본문 작성 0건** (본 brief = 통합 *검토* 한정 — 실 파일 작성 = 별도 단계)
- ❌ **`pre-commit install` 강제 0건** (사용자 명시 5 금지 中 1 — 본 항목 강조 답습)
- ❌ **hook 구현 0건** (실 hook 본문 작성 / hook actual run / hook 통합 시연 모두 0건)
- ❌ **GP-3 1.5차 Satisfied 갱신 0건** (§C-5b ST-1 / §C-5c PC-4 Deferred 그대로 유지)
- ❌ **GP-5 1.5차 Satisfied 갱신 0건** (§C-6 Deferred 그대로 유지)
- ❌ **MVP-1 PASS *재선언* 0건** (Layer D `210c98f` APPROVE WITH CONDITIONS 그대로 유지)
- ❌ **Operational Readiness PASS 선언 0건** (사용자 명시 5 금지 中 4 — 본 항목 강조 답습)
- ❌ **T3 영역 *자동 진입* 0건** (Hermes upstream / Vault HSM / Tier-2-3 catalog / branch protection / dev 환경 강제 / `pre-commit install` 의무화 모두 0건)

### 0.5 본 brief 가 *하지 않는* 것 (추가 답습)

- ❌ **§C-5c Satisfied / 부분 Satisfied 갱신 발효 0건** (본 brief = 준비안 한정)
- ❌ **§C-5 전체 표기 갱신 0건** (`Partially Satisfied (C-5a only)` 그대로 유지, `6fa87dc` 답습)
- ❌ **Backlog #1 / #2 진입 합의 발효 0건** (PC-4 T2 sub 통합 진입 결정 = 별도 합의 영역)
- ❌ **PC-4 *수단 결정* 0건** (PC-1 / PC-2 / PC-3 / PC-4 채택 변경 0건 — 본 brief = 통합 *분석* 한정)
- ❌ **§5.5 9 sub-수단 본문 채택 *변경* 0건** (PC-3 본문 채택 유지, Layer B `f40423f` + `55c5b4b` 답습 — 양 GP 일관 채택 답습)
- ❌ **threshold *고정* 0건** (commit_block_rate / dev_env_install_rate / hook_runtime / FP_rate 모두 *후보 한정* 유지)
- ❌ **Tier-2 / Tier-3 catalog 자동 확장 0건** (R-4.1 Tier-1 45 patterns 답습 + URL Tier-1 10 + Model Tier-1 19 답습)
- ❌ **ADR 본문 자동 갱신 0건** (ADR-008 / ADR-010 / ADR-011 / ADR-012 본문 변경 0건)
- ❌ **ADR-012 §2.2 enum 정식 등록 0건** (`pre_commit_config_local_definition_unified` 가칭 = candidate-only — Backlog #5 별도 합의 영역)
- ❌ **다른 backlog (#3/#4/#7) 자동 진입 0건**
- ❌ **C-2 / C-3 / C-4 / C-5a / C-5b / C-7 / C-8 자동 변경 0건** (C-5c T2 sub 통합 한정 분석)
- ❌ **C-6 자동 변경 0건** (Backlog #2 GP-5 1.5차 Deferred 그대로 유지)
- ❌ **합의 보고서 작성 0건** (본 brief = 준비안 한정)
- ❌ **CONTEXT / INDEX / SESSION 메타 갱신 0건** (별도 commit 분리)
- ❌ **git commit / push 0건** (본 brief 파일화 + commit = 사용자 명시 후속)
- ❌ **외부 LLM 자동 호출 0건**
- ❌ **실 API key / provider SDK / 외부 API 호출 0건**

### 0.6 본 brief 의 권위 한계

본 brief = **DRAFT — 준비안 한정**. 본 brief 의 어떤 §도:

- (i) §C-5c Satisfied / 부분 Satisfied 갱신 발효를 발생시키지 않으며,
- (ii) Backlog #1 / #2 1.5차 Satisfied 갱신을 발생시키지 않으며,
- (iii) MVP-1 PASS *재선언* / Layer D 본문 변경 / Layer E / Layer F 격상을 발생시키지 않으며,
- (iv) PC-4 T3 sub-영역 (`pre-commit install` 의무화 / dev 환경 강제 / branch protection) 진입을 *허용* 하지 않으며,
- (v) §5.5 9 sub-수단 본문 채택 + C-1~C-8 상태를 *변경* 하지 않으며,
- (vi) `.pre-commit-config.yaml` 실 본문을 *작성* 하지 않는다.

본 brief 가 발생시키는 *유일한* 효과는 **§C-5c PC-4 의 T2 sub-영역 (`.pre-commit-config.yaml` config 정의 가능성) 의 Backlog #1 + #2 *공유 통합 검토* + 6 hook 후보 카탈로그 + 공통 config 구조 분석 + T2/T3 분리 명시 + 합의 형태 권고**. 모든 *진입 결정* = *사용자 명시 결정 영역*.

---

## 1. 진입 컨텍스트 답습 (선행 brief 후 상태)

### 1.1 선행 brief 핵심 결과 답습 (`11d7ebb` Backlog #1 단독 brief)

| 항목 | 결과 |
|------|------|
| 기술적 가능성 | ✅ 명확 (기존 도구 모두 stateless · network-free · CLI-callable) |
| 효과 (T2 sub 단독) | repo-local config 파일 *추가* + opt-in 한정 (dev 환경 강제 효과 0건) |
| 옵션 (α) Backlog #1 단독 | T2 sub 단독 진입 의도 보존 + 1 파일 2 회 변경 (변경 ledger 분산) |
| 옵션 (β) Backlog #1 + #2 통합 | 1 파일 1 회 변경 (단일 source-of-truth) + 합의 효율 |
| 옵션 (γ) 보류 | 다른 backlog 우선 |
| 합의 형태 권고 | Reviewer-only 단축 합의 적격 (7/7 트리거 0건 발화) |

### 1.2 사용자 결정 답습 (옵션 (β) 통합 검토 방향)

```
선행 brief 작성 commit `11d7ebb`
   │
   ▼
사용자 결정: Backlog #1 단독 진입 ❌ → Backlog #1 + Backlog #2 통합 검토 ✅
   │
   ├ 사유: PC-4 = GP-3 + GP-5 공유 영역 (Backlog #1 단독 진입 시 Backlog #2 진입 시점 재합의 위험)
   └ 더 안전한 방향: 처음부터 통합 config 정의 영역으로 검토
   │
   ▼
■ 본 brief = §C-5c PC-4 T2 sub 의 *Backlog #1 + #2 통합 검토* 준비안 (DRAFT)         ← 현 위치
   │
   ▼ (사용자 명시 승인 후)
brief 그대로 승인 합의 보고서 작성 또는 일부 조정 또는 보류
   │
   ▼ (사용자 명시 결정 후, T2 sub 통합 진입 결정 시)
■ §C-5c PC-4 T2 sub 통합 진입 합의 (옵션 β 한정)         ← 본 brief 영역 외
   │
   ▼ (T2 sub 통합 진입 결정 후, `.pre-commit-config.yaml` 실 본문 작성)
실 구현 진입 (Cycle 1~N + actual run + evidence)         ← 본 brief 영역 외
   │
   ▼ (구현 + actual run SUCCESS + evidence 후)
§C-5c 부분 Satisfied 갱신 합의 (T2 sub 통합 한정 — T3 sub 보존)         ← 본 brief 영역 외
```

### 1.3 §C-5 sub-condition + §C-6 답습 (`6fa87dc` 직후 시점)

| Condition | 항목 | 영역 | 상태 | 본 brief 관계 |
|-----------|------|------|------|------------|
| C-5a | ST-2 (inotify sidecar) | GP-3 저장 경로 isolation 보강 (T2) | ✅ Satisfied (`6fa87dc`) | 답습 한정 |
| C-5b | ST-1 (Hermes Dockerfile entrypoint stat) | GP-3 저장 경로 isolation 보강 (T3) | ⏳ Deferred (Backlog #3 T3 영역) | 답습 한정 — 본 brief 영역 외 |
| **C-5c** | **PC-4 (local pre-commit framework)** | GP-3 + GP-5 공유 (T2 + T3 혼합) | ⏳ **Deferred** (Backlog #1 + #2 공유) | **본 brief = T2 sub 통합 검토** |
| **C-6** | **GP-5 1.5차 보강 (T-1/T-3/T-4/T-5 단독 / PC-4)** | GP-5 1.5차 영역 | ⏳ **Deferred** | **본 brief = PC-4 부분 영향 답습** |
| C-5 전체 | (3 sub-condition 합산) | — | ⏳ Partially Satisfied (C-5a only) | 답습 한정 — 본 brief 영역 외 |

---

## 2. PC-4 의 *공유* 본질 답습

### 2.1 양 GP PC-3 일관 채택 답습 (Layer B `55c5b4b` §5.5.1 + §5.5.2)

| GP | 영역 | PC-3 본문 채택 답습 (Layer B) |
|----|------|------------------------|
| GP-3 | G3-2 부분 / G5-2 부분 공유 (`55c5b4b` §5.5.1 PC-3 row) | ✅ 본문 채택 (CI-only enforcement, T2 영역) |
| GP-5 | G5-2 (`55c5b4b` §5.5.2 PC-3 row) | ✅ 본문 채택 (CI-only enforcement, T2 영역, GP-3 동일 채택 답습) |

→ **양 GP 일관성 답습**: PC-3 = 양 GP 공통 본문 채택 답습 (Layer B). PC-4 T2 sub (`.pre-commit-config.yaml` 본문 정의) = PC-3 답습 위에서 *추가* repo-local hook 정의 영역 — 양 GP 공유 일관성 자연 답습.

### 2.2 `.pre-commit-config.yaml` = 1 파일 본질 답습

mvp1.md §4.3.1 답습 — PC-4 = 양 GP 공유 영역. 표준 [pre-commit framework](https://pre-commit.com) 의 `.pre-commit-config.yaml` = repo 1 파일 본질 답습 → GP-3 hook + GP-5 hook 합산 정의 가능 (별도 파일 분리 필요 0건).

### 2.3 통합 검토의 *합의 효율*

| 영역 | Backlog #1 단독 (옵션 α) | Backlog #1 + #2 통합 (옵션 β, 본 brief) |
|------|--------------------|----------------------------|
| `.pre-commit-config.yaml` 변경 횟수 | 2 회 (Backlog #1 진입 시 GP-3 hook + Backlog #2 진입 시 GP-5 hook 추가) | **1 회** (양 GP hook 합산 정의) |
| 합의 횟수 | 2 회 (Backlog #1 단독 + Backlog #2 단독) | **1 회** (통합 합의 — Reviewer-only 단축 적격 답습) |
| 변경 ledger 분산 | ⚠️ 분산 (2 commit) | ✅ 단일 source-of-truth (1 commit) |
| Backlog #2 합의 시점 PC-4 부분 재합의 위험 | ⚠️ 高 (1차 정의 후 2차 추가 시 일관성 검증 의무) | ✅ 0건 (1 회 정의 한정) |
| §5.5 PC-3 본문 채택 답습 충돌 | 양쪽 PC-3 답습 + 양쪽 hook 추가 = 일관성 검증 2 회 | ✅ 양쪽 PC-3 답습 + 양쪽 hook 통합 추가 = 일관성 검증 1 회 |

→ **통합 검토 (옵션 β) = *합의 효율* + *일관성* + *변경 ledger 단일화* 답습**.

---

## 3. GP-3 + GP-5 local hook 6 후보 카탈로그 (사용자 명시 답습)

### 3.1 GP-3 local hook 후보 (사용자 명시 3 후보)

#### 3.1.1 hook #1 — secret scanner

| 항목 | 후보 |
|------|------|
| hook id 후보 | `secret-scanner` |
| 도구 답습 | `tools/secret_scanner.py` (Group D PoC + Layer B `55c5b4b` 본문 채택 S-1 답습, 261줄) |
| files 패턴 후보 | `\.(py|js|ts|md|yml|yaml|sh|toml)$` (Tier-1 45 patterns 답습 한정) |
| stages 후보 | `[pre-commit]` (commit-msg / pre-push 등 추가 stage 0건) |
| pass 기준 후보 | exit 0 + Tier-1 45 patterns 中 매칭 0건 |
| fail 기준 후보 | exit ≠ 0 (1+ 매칭 시 hook fail-closed) |
| runtime 비용 후보 | < 5초 (Group D PoC actual run 답습 — `25623028888` SUCCESS) |
| FP 위험 후보 | < 0.5건 / 1000 line (mvp1.md §4.5.2 답습, 정량 *결정* 영역 외) |
| CI 답습 | `secret-hygiene-egress-redaction.yml` 의 secret scanner step 과 *동등* 정의 (이중 정의 회피, 단일 source-of-truth 답습) |
| 본문 채택 권위 | S-1 본문 채택 답습 (`55c5b4b` §5.5.1) |

#### 3.1.2 hook #2 — workflow secret usage check (G3-7 (i) + (ii) 답습)

| 항목 | 후보 |
|------|------|
| hook id 후보 | `workflow-secret-usage-check` |
| 도구 답습 | grep step 본문 (G3-7 (i) GitHub Actions secrets 사용 0건 검증 + (ii) `secrets.*` 참조 감지) — `55c5b4b` §5.5.1 추가 본문 채택 영역 답습 |
| files 패턴 후보 | `^\.github/workflows/.*\.(yml|yaml)$` |
| stages 후보 | `[pre-commit]` |
| pass 기준 후보 | workflow 본문에 `secrets\.[A-Z_]+` 참조 0건 + GitHub Actions secrets 사용 0건 (F-금지 답습) |
| fail 기준 후보 | 1+ secrets 참조 시 hook fail-closed |
| runtime 비용 후보 | < 1초 (workflow 디렉토리 한정 grep) |
| FP 위험 후보 | 매우 낮음 (workflow yaml 한정 + grep pattern 명확) — 단, 필요한 secret 사용 (예: GITHUB_TOKEN) 의 false positive 가능성 검토 의무 (T2 sub 진입 시 별도 합의 영역) |
| CI 답습 | 본 hook = G3-7 row workflow grep step 의 local 실행 형태 — CI step 과 *동등* 정의 |
| 본문 채택 권위 | G3-7 row (i) + (ii) 추가 본문 채택 답습 (`55c5b4b` §5.5.1) |

#### 3.1.3 hook #3 — workflow permissions check (G3-7 (v) 답습)

| 항목 | 후보 |
|------|------|
| hook id 후보 | `workflow-permissions-check` |
| 도구 답습 | grep step 본문 (G3-7 (v) workflow `permissions: contents: read` 명시 강제 — R-6 답습) — `55c5b4b` §5.5.1 추가 본문 채택 영역 답습 |
| files 패턴 후보 | `^\.github/workflows/.*\.(yml|yaml)$` |
| stages 후보 | `[pre-commit]` |
| pass 기준 후보 | 모든 workflow 에 `permissions:` 명시 + `contents: read` 답습 (default-deny 답습, R-6) |
| fail 기준 후보 | `permissions:` 누락 또는 `contents: write` 명시 (예외 영역 한정 별도 합의 의무) |
| runtime 비용 후보 | < 1초 (workflow 디렉토리 한정 grep) |
| FP 위험 후보 | 매우 낮음 (yaml 구조 grep 명확) |
| CI 답습 | 본 hook = G3-7 row R-6 답습 step 의 local 실행 형태 |
| 본문 채택 권위 | G3-7 row (v) 추가 본문 채택 답습 (`55c5b4b` §5.5.1) |

### 3.2 GP-5 local hook 후보 (사용자 명시 3 후보)

#### 3.2.1 hook #4 — provider import scanner

| 항목 | 후보 |
|------|------|
| hook id 후보 | `provider-import-scanner` |
| 도구 답습 | `tools/provider_import_scanner.py` (Group A 1차 답습 — AST 5종 패턴: direct / from / dynamic / double-underscore / model-name) |
| files 패턴 후보 | `^src/.*\.py$` |
| stages 후보 | `[pre-commit]` |
| pass 기준 후보 | exit 0 + 5/5 pattern 매칭 0건 (실 src/ 영역 한정) |
| fail 기준 후보 | exit ≠ 0 (1+ pattern 매칭 시 hook fail-closed) |
| runtime 비용 후보 | < 10초 (Group A 1차 actual run 답습) |
| FP 위험 후보 | < 0.5건 / 1000 line (mvp1.md §4.5.1 답습) — 단, src/ 0건 환경 시 측정 불가 (별도 합의 영역) |
| CI 답습 | `provider-adapter-enforcement.yml` 의 import scanner step 과 *동등* 정의 |
| 본문 채택 권위 | T-6 (T-2 + T-5 병행) 中 T-5 본문 채택 답습 (`55c5b4b` §5.5.2) — Group A 1차/3차 답습 |

#### 3.2.2 hook #5 — provider URL/model scanner

| 항목 | 후보 |
|------|------|
| hook id 후보 | `provider-url-model-scanner` |
| 도구 답습 | `tools/provider_url_scanner.py` (Group A 3차 답습 — URL Tier-1 10 vendor + Model Tier-1 19 모델) |
| files 패턴 후보 | `^src/.*\.py$` |
| stages 후보 | `[pre-commit]` |
| pass 기준 후보 | exit 0 + URL Tier-1 + Model Tier-1 매칭 0건 |
| fail 기준 후보 | exit ≠ 0 (1+ URL / Model 매칭 시 hook fail-closed) |
| runtime 비용 후보 | < 5초 (Group A 3차 actual run 답습 — `25629390384` SUCCESS) |
| FP 위험 후보 | 매우 낮음 (URL / Model name 정확 매칭) — Tier-2/3 catalog 자동 확장 0건 답습 |
| CI 답습 | `provider-url-scanner.yml` 의 step 과 *동등* 정의 |
| 본문 채택 권위 | T-6 中 T-5 본문 채택 답습 (`55c5b4b` §5.5.2) — Group A 3차 답습 |

#### 3.2.3 hook #6 — import-linter

| 항목 | 후보 |
|------|------|
| hook id 후보 | `import-linter` |
| 도구 답습 | `lint-imports` (T-2 답습, Group A 2차 답습 — `.importlinter` TR-1~TR-5 답습) |
| files 패턴 후보 | `^src/.*\.py$` (또는 hook 자체가 entire repo scan 형태인지 hook 정의 결정 시 검토) |
| stages 후보 | `[pre-commit]` |
| pass 기준 후보 | exit 0 + `.importlinter` 모든 contract PASS |
| fail 기준 후보 | exit ≠ 0 (contract 1+ 위반 시 hook fail-closed) |
| runtime 비용 후보 | < 30초 (Group A 2차 actual run 답습 — `25605665191` SUCCESS) |
| FP 위험 후보 | 낮음 (TR-1~TR-5 answer 답습 — `include_external_packages = True` 옵션 답습) |
| CI 답습 | `provider-adapter-enforcement.yml` 의 import-linter step 과 *동등* 정의 |
| 본문 채택 권위 | T-6 中 T-2 본문 채택 답습 (`55c5b4b` §5.5.2) — Group A 2차 답습 |

### 3.3 6 후보 합산 매트릭스

| # | hook id 후보 | GP | 본문 채택 답습 | runtime 후보 | FP 위험 후보 |
|---|----------|-----|----------|---------|----------|
| 1 | `secret-scanner` | GP-3 | S-1 (`55c5b4b` §5.5.1) | < 5초 | < 0.5건 / 1000 line |
| 2 | `workflow-secret-usage-check` | GP-3 | G3-7 (i) + (ii) (`55c5b4b` §5.5.1 추가) | < 1초 | 매우 낮음 (필요 secret FP 검토 의무) |
| 3 | `workflow-permissions-check` | GP-3 | G3-7 (v) (`55c5b4b` §5.5.1 추가, R-6 답습) | < 1초 | 매우 낮음 |
| 4 | `provider-import-scanner` | GP-5 | T-5 부분 (`55c5b4b` §5.5.2) | < 10초 | < 0.5건 / 1000 line |
| 5 | `provider-url-model-scanner` | GP-5 | T-5 부분 (`55c5b4b` §5.5.2) | < 5초 | 매우 낮음 |
| 6 | `import-linter` | GP-5 | T-2 부분 (`55c5b4b` §5.5.2) | < 30초 | 낮음 |

**합산 = 6 hook 후보** (GP-3 3 + GP-5 3, 양 GP 균등). 본 카탈로그 = *통합 검토 한정 enumerate* — 채택 *결정* 0건. 실 채택 = T2 sub 통합 진입 합의 영역.

### 3.4 추가 후보 (본 brief 권고 — 사용자 명시 6 후보 외 부가 옵션)

선행 brief §3.1.3 답습 — 사용자 명시 6 후보 외 부가 후보가 있음:

| # | hook id 후보 | 도구 답습 | 본 brief 권고 |
|---|----------|---------|----------|
| 7 (부가) | `secret-inotify-sidecar-check` | `tools/docker_secret_inotify_sidecar_check.sh` (Cycle 6 답습) | ⚠️ **부가 후보 한정** — local 실행 의미 약함 (사이드카 영역 한정), CI 의존도 高 → 통합 합의 시 *제외 권고* (사용자 명시 6 후보 한정) |

본 §3.4 = 부가 enumeration 한정. 실 카탈로그 = 사용자 명시 6 후보 한정 (1~6).

### 3.5 본 §3 의 *범위 한계*

본 §3 = *6 hook 후보 카탈로그 enumerate 한정*. 다음은 본 §3 영역 외:

- ❌ hook 후보 中 *최종 채택 결정* (6 후보 中 어느 hook 채택?)
- ❌ files 패턴 / stages / pass·fail 기준 *최종 결정* (T2 sub 통합 진입 합의 영역)
- ❌ runtime / FP 후보 정량 *고정* (모두 *후보 한정* 유지)
- ❌ 실 hook entry 본문 작성

---

## 4. 공통 `.pre-commit-config.yaml` config 구조 분석

### 4.1 repo-local hooks 구조 후보

표준 [pre-commit framework](https://pre-commit.com) `repo: local` hook 정의 형식 답습 — 본 brief = 형식 *검토 한정*, 실 본문 작성 0건:

| 영역 | 후보 |
|------|------|
| `repos[*].repo` | `local` (외부 repo 의존 0건 — 본 repo 도구 한정 답습) |
| `repos[*].hooks[*].id` | hook id (§3 답습 6 후보) |
| `repos[*].hooks[*].name` | human-readable name |
| `repos[*].hooks[*].entry` | 도구 실행 명령 (§3 답습 도구 path) |
| `repos[*].hooks[*].language` | `system` (system-level command, Python venv 의존성 회피 — 단 `import-linter` 는 Python 의존성 필요 시 별도 검토) |
| `repos[*].hooks[*].files` | files 패턴 (§3 답습 후보) |
| `repos[*].hooks[*].stages` | `[pre-commit]` (commit-msg / pre-push 등 추가 stage 0건 권고) |
| `repos[*].hooks[*].pass_filenames` | true (default — git diff 변경 파일 한정 전달) 또는 false (전체 scan 필요 시 — 예: import-linter) |
| `repos[*].hooks[*].always_run` | false (default — 변경 파일 없으면 skip) — `always_run: true` 는 dev 환경 영향 中 (본 brief 영역 외 권고) |

### 4.2 pass / fail 기준

#### 4.2.1 pass 기준 (모든 hook 공통)

- exit code 0
- stderr / stdout 에 명시 violation 0건
- (hook 별 도구 자체의 추가 기준 — §3 답습)

#### 4.2.2 fail 기준 (모든 hook 공통)

- exit code ≠ 0
- (hook 별 도구 자체의 fail 기준 — §3 답습)
- pre-commit framework 의 default 동작 = 1+ hook fail 시 commit *block* — 단, 본 brief 영역 = `.pre-commit-config.yaml` *정의 한정*, 실 commit block *강제* = `pre-commit install` 의무화 시점 (T3 영역 — 본 brief 영역 외)

### 4.3 runtime 비용 합산 후보

| hook | runtime 후보 | 합산 |
|------|---------|------|
| 1. secret-scanner | < 5초 | — |
| 2. workflow-secret-usage-check | < 1초 | — |
| 3. workflow-permissions-check | < 1초 | — |
| 4. provider-import-scanner | < 10초 | — |
| 5. provider-url-model-scanner | < 5초 | — |
| 6. import-linter | < 30초 | — |
| **합산 (순차 실행)** | | **< 52초** (worst case 후보) |
| **합산 (병렬 실행 — pre-commit framework default)** | | **< 30초** (max hook = import-linter 한정 — pre-commit framework 의 hook 병렬 실행 default 답습) |

⚠️ **runtime threshold *고정* 0건** — 본 §4.3 = 후보 한정. 정량 결정 = T2 sub 통합 진입 합의 영역 (mvp1.md §4.5.2 답습).

### 4.4 false positive 위험 매트릭스

| hook | FP 위험 | 답습 |
|------|---------|------|
| 1. secret-scanner | < 0.5건 / 1000 line | mvp1.md §4.5.2 답습 (정량 결정 영역 외) |
| 2. workflow-secret-usage-check | 매우 낮음 (필요 secret FP 검토 의무) | 본 brief 권고 — 별도 합의 영역 |
| 3. workflow-permissions-check | 매우 낮음 | yaml 구조 grep 명확 답습 |
| 4. provider-import-scanner | < 0.5건 / 1000 line | mvp1.md §4.5.1 답습 |
| 5. provider-url-model-scanner | 매우 낮음 | URL / Model name 정확 매칭 답습 |
| 6. import-linter | 낮음 | TR-1~TR-5 답습 |

⚠️ FP 정량 *고정* 0건 — 본 §4.4 = 후보 한정.

### 4.5 CI-only enforcement 와의 관계 (PC-3 답습)

#### 4.5.1 PC-3 본문 채택 답습 (Layer B `55c5b4b`)

| 영역 | PC-3 답습 |
|------|---------|
| GP-3 CI step | `secret-hygiene-egress-redaction.yml` (Stage 1+3 SUCCESS 답습) |
| GP-5 CI step | `provider-adapter-enforcement.yml` + `provider-url-scanner.yml` (Group A 1차/2차/3차 SUCCESS 답습) |
| AR-1 본문 채택 답습 | CI step fail-closed (양 GP 일관 본문 채택, `55c5b4b` 답습) |

#### 4.5.2 본 brief T2 sub 통합 검토 = PC-3 답습 위 *추가* 영역

| 차원 | PC-3 (현 본문 채택) | PC-4 T2 sub 통합 (본 brief) |
|------|----------------|-----------------------|
| 영역 | CI step (PR push 시 차단) | repo-local config 정의 (opt-in 한정) |
| dev 환경 영향 | 0건 (CI 한정) | opt-in 한정 (강제 0건 답습) |
| 강제 효과 | ✅ CI gating (PR auto-reject, AR-1 답습) | ❌ 강제 효과 0건 (opt-in 한정 — 사용자 명시 1 + 2 금지 답습) |
| Defense in depth | 1 layer (CI) | 2 layer 가능성 (CI + dev opt-in) — *opt-in 한정 답습* |
| 변경 ledger 답습 | `55c5b4b` 본문 채택 답습 + actual run SUCCESS 답습 | 본 brief 후속 합의 (T2 sub 통합 진입 시) |
| 양 GP 일관성 | ✅ 양 GP PC-3 일관 채택 답습 | ✅ 양 GP hook 통합 (1 파일 / 1 합의) — 일관성 자연 답습 |

#### 4.5.3 CI step 과 hook entry 의 *단일 source-of-truth* 답습

본 brief 권고: T2 sub 통합 진입 시점에서 hook entry = CI step 의 *동등* 명령 사용 (이중 정의 회피). 예:

| 영역 | CI step 답습 | local hook entry 후보 |
|------|---------|----------------|
| GP-3 secret scanner | `python tools/secret_scanner.py ${changed_files}` | `python tools/secret_scanner.py` (pre-commit framework 가 `${changed_files}` 자동 전달) |

→ **단일 source-of-truth 답습**: 도구 본문 변경 시 CI step + hook entry 양쪽 자동 일관성 답습 (이중 정의 회피).

### 4.6 본 §4 의 *범위 한계*

본 §4 = *공통 config 구조 분석 한정*. 다음은 본 §4 영역 외:

- ❌ 실 `.pre-commit-config.yaml` 본문 작성 (T2 sub 통합 진입 시점 별도 작업)
- ❌ runtime / FP threshold *고정*
- ❌ pass / fail 기준 *최종 결정*
- ❌ `pass_filenames` / `always_run` 등 hook 옵션 *최종 결정*

---

## 5. T2 / T3 분리 명시 (사용자 명시 답습)

### 5.1 T2 vs T3 sub-영역 분류 매트릭스 (본 brief 한정 범위 표시)

| sub-영역 | 분류 | 본 brief 처리 | 사유 답습 |
|---------|------|------------|---------|
| **`.pre-commit-config.yaml` 본문 정의** | **T2** | ✅ **본 brief 영역 (통합 검토)** | ADR-011 §2.4 답습 — 정책 영역 / Skill·Memory promotion / 새 도구 등록 / 합의 형태 결정 |
| `pre-commit install` 의무 명시 (dev 환경 강제) | **T3 또는 별도 정책 영역** | ❌ **본 brief 영역 외** (사용자 명시 4 = 이번 범위 밖) | dev 환경 강제 = 사용자 명시 1 + 2 금지 — Backlog #3 T3 영역 부분 중첩 가능성 답습 |
| dev 환경 강제 (모든 dev 환경 hook 강제 동작 / install 검증) | T3 | ❌ **본 brief 영역 외** (사용자 명시 4 = 이번 범위 밖) | 사용자 명시 1 금지 답습 |
| PC-3 부분 답습 (CI step fail-closed) | T2 (이미 본문 채택, `55c5b4b` 답습) | 답습 한정 (변경 0건) | §5.5 9 sub-수단 본문 채택 답습 답습 |
| AR-2 (branch protection rule 변경 — required check / commit signing / CODEOWNERS) | T3 | ❌ **본 brief 영역 외** (사용자 명시 3 금지) | Backlog #3 T3 영역 별도 풀 3+1 합의 의무 |

### 5.2 본 §5 사용자 명시 답습 4 영역

사용자 명시 진입 명령 §0.1 검토 영역 #4 답습:

| # | 영역 | 본 brief 처리 |
|---|------|------------|
| 4.1 | `.pre-commit-config.yaml` 본문 정의 = T2 | ✅ §3 + §4 답습 |
| 4.2 | `pre-commit install` 의무화 = T3 또는 별도 정책 | ✅ §5.1 명시 — 본 brief 영역 외 |
| 4.3 | dev 환경 강제 = 이번 범위 밖 | ✅ §0.3 + §5.1 명시 |
| 4.4 | (T2 sub 통합 진입 결과 = repo-local opt-in 한정 효과) | ✅ §4.5.2 답습 |

### 5.3 T3 영역 *자동 진입 0건* 의무 답습

본 brief = 모든 T3 sub-영역 자동 진입 0건. T3 sub 진입 = 별도 풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시 결정 의무 (사용자 명시 4 + 5 + 6 금지 답습).

### 5.4 본 §5 의 *범위 한계*

본 §5 = *T2 / T3 분리 명시 한정*. 다음은 본 §5 영역 외:

- ❌ T3 sub-영역 진입 권고 / 결정 (사용자 명시 4 금지)
- ❌ `pre-commit install` 의무화 정책 *권고* (사용자 명시 2 금지)
- ❌ dev 환경 강제 정책 *권고* (사용자 명시 1 금지)
- ❌ branch protection 변경 *권고* (사용자 명시 3 금지)

---

## 6. 합의 형태 권고 + 풀 3+1 승격 트리거 검증

### 6.1 본 brief 자체의 합의 형태

| 영역 | 합의 형태 권고 | 사유 |
|------|----------|------|
| 본 brief 자체 (DRAFT — 준비안) | **사용자 명시 승인 한정 (합의 보고서 0건)** | 본 brief = 준비안 한정 (`backlog1-st2-c5a-satisfaction-brief.md` §0.4 + 선행 brief `11d7ebb` §0.4 패턴 답습) |
| brief 승인 후 후속 합의 (T2 sub 통합 진입 결정 시) | **사용자 명시 결정 영역** | 옵션별 합의 형태 분리 (§6.2 답습) |

### 6.2 통합 옵션 합의 형태 권고

| 영역 | 합의 형태 권고 | 사유 | 답습 출처 |
|------|----------|------|---------|
| (β) Backlog #1 + #2 통합 진입 (`.pre-commit-config.yaml` GP-3 + GP-5 hook 합산 본문 정의) | **단축 합의 + 사용자 명시 결정** | T2 정책 영역 한정 + 양 GP PC-3 일관 채택 답습 + §5.5 본문 채택 변경 0건 답습 | mvp1.md §4.7.3 + ADR-011 §2.4 답습 + 양 GP 일관 답습 (`55c5b4b`) |
| §C-5c 부분 Satisfied 갱신 (T2 sub 통합 발효 후) | **단축 합의 + A-1 답습** | C-5a `6fa87dc` A-1 답습 패턴 — Layer D 본문 변경 0건, 부분 Satisfied 표기 한정 | `1dd1036` + `6fa87dc` 답습 |
| §C-5c 전체 Satisfied 갱신 (본 brief 영역 외) | (T2 sub 통합 + T3 sub 진입 모두 Satisfied 시 가능) | T3 sub 진입 = 별도 풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시 의무 | mvp1.md §4.7.3 답습 |

### 6.3 풀 3+1 승격 트리거 검증 (7 트리거 답습 — 0/7 발화 권고)

본 brief 가 풀 3+1 합의로 *승격* 되어야 할 trigger 후보 (deepening brief §3.3 + c5a brief §7.2 + 선행 brief §4.3 답습):

| # | 트리거 | 본 brief 검토 결과 |
|---|----|------------|
| 1 | 본 brief 가 9 sub-수단 *외* 수단 *재결정* 을 권고하는 경우 | ❌ 0건 발화 — 본 brief = PC-4 T2 sub 통합 *분석* 한정 (PC-3 본문 채택 답습 변경 0건) |
| 2 | 본 brief 가 T3 영역 (Hermes upstream / Vault HSM / Tier-2-3 catalog / branch protection / dev 환경 강제 / `pre-commit install` 의무화) 자동 진입을 권고하는 경우 | ❌ 0건 발화 — 사용자 명시 5 금지 + 8 추가 금지 답습, T3 영역 권고 0건 |
| 3 | 본 brief 가 §5.5 9 sub-수단 *재결정* 을 권고하는 경우 | ❌ 0건 발화 — 양 GP PC-3 본문 채택 유지 (`55c5b4b` 답습) |
| 4 | 본 brief 가 Provider Liquidity 5-way 약화 가능성을 포함하는 경우 | ❌ 0건 발화 — pre-commit framework 영역, Provider Liquidity 영향 0건 |
| 5 | 본 brief 가 5 영구 핵심 제약 약화를 포함하는 경우 | ❌ 0건 발화 — Hermes ≠ root of trust 보존 + T3 분리 보존 + 수단/목적 분리 보존 + 메타포 강제 금지 보존 + Provider Liquidity 보존 |
| 6 | 본 brief 가 MVP-1 PASS *재선언* / Layer E / Layer F 격상을 포함하는 경우 | ❌ 0건 발화 — 사용자 명시 5 + 8 추가 금지 답습 |
| 7 | 본 brief 가 외부 LLM cross-vendor blind 의뢰 *없이* T3 영역 결정을 권고하는 경우 | ❌ 0건 발화 — T3 영역 권고 0건 |

**본 brief 검토 결과 = 7/7 트리거 0건 발화** → 본 brief 승인 후 후속 합의 = **Reviewer-only 단축 합의 적격** (사용자 명시 결정 시).

### 6.4 본 §6 의 *범위 한계*

본 §6 = *합의 형태 권고 한정*. 실 합의 형태 결정 + 통합 진입 결정 = 사용자 명시 결정 영역.

---

## 7. Rollback Trigger / Evidence 기준 (T2 sub 통합 발효 시점 의무 — 본 brief 영역 외)

### 7.1 본 §7 의 *명확한 한계*

본 §7 = **T2 sub 통합 *발효 시점* 의무 정리 한정**. 본 brief 자체 시점에서:

- ❌ 실 `.pre-commit-config.yaml` *본문 작성* 0건
- ❌ 실 hook actual run 0건
- ❌ commit_block_rate / hook_runtime / FP_rate threshold *고정* 0건 (모두 *후보 한정* 유지)
- ❌ 실 evidence artifact 생성 0건
- ❌ event enum 정식 등록 0건 (`pre_commit_config_local_definition_unified` 가칭 = candidate-only)

### 7.2 PC-4 T2 sub 통합 별 Rollback Trigger 답습 (mvp1.md §3.5 + §4.6 답습)

| Trigger ID | 발화 조건 (T2 sub 통합 한정) | 발화 시 행동 |
|----------|----------------------|-------------|
| R-MVP1-G3-4 | PC-3 부분 CI runtime 폭증 (>2분) — pre-commit hook 정의가 CI step 과 *불일치* 시 발화 (단일 source-of-truth 위반) | threshold 재결정 합의 (단축 적격) |
| R-MVP1-G3-5 | AR-1 hook 우회 시도 패턴 검출 | T3 영역 → 풀 3+1 합의 + branch protection rule 변경 검토 (Backlog #3) |
| R-MVP1-G5-6 | T-9 (pre-commit hook PC-1) 도입 별도 합의 (Group A 2차 §8 TR-5 답습) | 본 PoC 와의 책무 분리 재합의 |
| (신규 후보) R-MVP1-G3-PC4-T2-INTG-1 | `.pre-commit-config.yaml` 본문 정의 후 dev 환경 *간접 강제* 시도 검출 | T3 영역 부분 진입 거부 + 본 brief §0.3 답습 (사용자 명시 1 + 2 금지) |
| (신규 후보) R-MVP1-G3-PC4-T2-INTG-2 | hook entry 와 CI step *불일치* 검출 (단일 source-of-truth 위반) | 합의 재진입 + hook entry 동기화 의무 |
| (신규 후보) R-MVP1-G3-PC4-T2-INTG-3 | hook runtime 합산 폭증 (예: > 60초 — threshold 후보) | hook 분리 / 도구 최적화 합의 |
| (신규 후보) R-MVP1-G3-PC4-T2-INTG-4 | FP_rate 폭증 (예: > 5건 / 1000 line — threshold 후보) | hook pattern 재검토 합의 |

### 7.3 Evidence 기준 답습 (mvp1.md §3.6.1 + ADR-011 §2.1 (a)~(e) 답습)

T2 sub 통합 *발효 시점* 의무 evidence (본 brief 영역 외):

| Evidence | 형식 | T2 sub 통합 적용 한정 |
|----------|------|---------------|
| (a) 동등 이상의 보안 결과 | `.pre-commit-config.yaml` 본문 정의가 PC-3 답습 (CI gating) 위에서 opt-in defense in depth *추가* 가능성 명시 (강제 효과 0건 명시) | ✅ T2 sub 통합 발효 시 |
| (b) 격리 환경 PoC 실증 | local repo 격리 환경에서 6 hook 정의 + opt-in 시 hook 동작 시연 (강제 환경 시연 0건) | ✅ T2 sub 통합 발효 시 (opt-in 한정 시연) |
| (c) ADR / SDD 권위 명시 | mvp1.md §4.3 + §5.5.1 / §5.5.2 + ADR-011 §2.4 + 선행 brief + 본 brief 답습 | ✅ T2 sub 통합 발효 시 |
| (d) 자동 회귀 검증 경로 확보 | `.pre-commit-config.yaml` schema 검증 (CI step 통한 yaml syntax + hook id 중복 검출) — 본문 *opt-in* 답습 한정 | ✅ T2 sub 통합 발효 시 (강제 install 검증 0건) |
| (e) 합의 APPROVE | 옵션 (β) 통합 진입 단축 합의 + 사용자 명시 | T2 sub 통합 발효 시 (본 brief 영역 외) |

### 7.4 JSONL Ledger entry 형식 후보 (Backlog #5 답습 — `b705370`)

T2 sub 통합 발효 시점 evidence ledger entry *후보* (Backlog #5 ADR-012 §2.2 정식 등록 8 enum 답습 + 추가 후보):

| event enum (후보) | trigger | T1/T2/T3 | Backlog #5 등록 상태 |
|------------------|---------|---------|------------------|
| `pre_commit_config_local_definition_unified` (가칭 — T2 sub 통합 한정) | `.pre-commit-config.yaml` GP-3 + GP-5 hook 합산 본문 정의 발효 시 | T2 한정 | ❌ 미등록 (Backlog #5 추가 등록 별도 합의 영역) |

본 enum 후보 = **본 brief 권고 한정** — 정식 등록 = Backlog #5 ADR-012 §2.2 schema 갱신 별도 합의 영역.

### 7.5 본 §7 의 *범위 한계*

본 §7 = **T2 sub 통합 *발효 시점* 의무 정리 한정**. 다음은 본 §7 영역 외:

- ❌ 실 rollback fixture 생성 (T2 sub 통합 *발효 시점* 별도 작업)
- ❌ 실 trigger 발화 시연 (동상)
- ❌ Trigger threshold 정량 *고정* (commit_block_rate / hook_runtime / FP_rate 등 모두 *후보 한정* 유지)
- ❌ 실 evidence artifact 생성 (동상)
- ❌ 신규 event enum 정식 등록 (Backlog #5 별도 합의 영역)
- ❌ T3 sub-영역 (dev 환경 강제 / `pre-commit install` 의무화) 의 evidence / trigger / threshold 정리 (사용자 명시 1 + 2 + 4 금지)

---

## 8. 금지 사항

### 8.1 본 brief 자체 금지 사항 (사용자 명시 5 + 8 추가 + 추가 답습)

| # | 금지 영역 | 본 brief 위반 | 답습 출처 |
|---|---------|------------|---------|
| 1 | **`pre-commit install` 강제** | 0건 | 사용자 명시 5 금지 中 1 + 8 추가 中 2 |
| 2 | **dev 환경 강제** (모든 dev 환경 hook 강제 동작) | 0건 | 사용자 명시 5 금지 中 2 |
| 3 | **branch protection 변경** (AR-2 / AR-3 / repo policy 변경 검토) | 0건 | 사용자 명시 5 금지 中 3 |
| 4 | **Operational Readiness PASS (Layer E) 선언** | 0건 | 사용자 명시 5 금지 中 4 + 8 추가 中 7 |
| 5 | **Hermes PMO 격상 (Layer F)** | 0건 | 사용자 명시 5 금지 中 5 |
| 6 | **`.pre-commit-config.yaml` 실 본문 작성** | 0건 | 사용자 명시 8 추가 中 1 |
| 7 | **hook 구현** (실 hook 본문 작성 / hook actual run / hook 통합 시연) | 0건 | 사용자 명시 8 추가 中 3 |
| 8 | **GP-3 1.5차 Satisfied 갱신** (§C-5b ST-1 / §C-5c PC-4 Deferred 변경) | 0건 | 사용자 명시 8 추가 中 4 |
| 9 | **GP-5 1.5차 Satisfied 갱신** (§C-6 Deferred 변경) | 0건 | 사용자 명시 8 추가 中 4 (대칭) |
| 10 | **MVP-1 PASS 재선언** (Layer D `210c98f` 본문 변경) | 0건 | 사용자 명시 8 추가 中 5 |
| 11 | **T3 영역 자동 진입** (Hermes upstream / Vault HSM / Tier-2-3 catalog / branch protection / dev 환경 강제 / `pre-commit install` 의무화) | 0건 | 사용자 명시 8 추가 中 6 |
| 12 | §C-5c Satisfied / 부분 Satisfied 갱신 발효 | 0건 | 본 brief = 준비안 한정 |
| 13 | §C-5 전체 표기 갱신 (`Partially Satisfied (C-5a only)` 변경) | 0건 | `6fa87dc` 답습 |
| 14 | Backlog #1 / #2 진입 합의 발효 | 0건 | 본 brief = 통합 분석 한정 |
| 15 | PC-4 *수단 결정* (PC-1 ~ PC-4 채택 변경) | 0건 | 본 brief = 통합 분석 한정 |
| 16 | §5.5 9 sub-수단 본문 채택 *변경* (PC-3 본문 채택 유지) | 0건 | `f40423f` + `55c5b4b` 답습 |
| 17 | threshold *고정* (commit_block_rate / dev_env_install_rate / hook_runtime / FP_rate) | 0건 | 답습 |
| 18 | Tier-2 / Tier-3 catalog 자동 확장 (R-4.1 Tier-1 / URL Tier-1 / Model Tier-1 변경) | 0건 | 답습 |
| 19 | ADR 본문 자동 갱신 (ADR-008 / ADR-010 / ADR-011 / ADR-012 본문 변경) | 0건 | cross-reference 답습 한정 |
| 20 | ADR-012 §2.2 enum 정식 등록 (`pre_commit_config_local_definition_unified` 가칭) | 0건 | candidate-only 유지 — Backlog #5 별도 |
| 21 | 다른 backlog (#3/#4/#7) 자동 진입 | 0건 | 답습 |
| 22 | C-2 / C-3 / C-4 / C-5a / C-5b / C-7 / C-8 자동 변경 | 0건 | C-5c T2 sub 통합 한정 분석 |
| 23 | C-6 자동 변경 (Backlog #2 GP-5 1.5차 Deferred) | 0건 | 본 brief = PC-4 부분 영향 답습 한정 |
| 24 | 합의 보고서 작성 (본 brief = 준비안 한정) | 0건 | 답습 |
| 25 | CONTEXT / INDEX / SESSION 메타 갱신 | 0건 | 별도 commit 분리 |
| 26 | git commit / push (본 brief 파일화 + commit = 사용자 명시 후속) | 0건 | 답습 |
| 27 | 외부 LLM 자동 호출 | 0건 | 답습 |
| 28 | 실 API key / provider SDK / 외부 API 호출 | 0건 | 영구 금지 답습 |
| 29 | Provider Liquidity 5-way / 5 영구 핵심 제약 약화 | 0건 | 답습 |

### 8.2 본 brief 발효 *후* T2 sub 통합 진입 단계 금지 사항 (진입 시 의무 답습)

본 §8.2 는 사용자 명시 5 + 8 추가 답습 한정 — T2 sub 통합 진입 *결정 후* 단계에서도 위반 0건 의무:

| # | 금지 영역 | 사유 |
|---|---------|------|
| 1 | dev 환경 강제 (`pre-commit install` 의무화 / 모든 dev 환경 hook 강제) | 사용자 명시 1 + 2 + 8-2 답습 |
| 2 | branch protection rule 변경 (AR-2 진입) | 사용자 명시 3 답습 (Backlog #3 T3 영역) |
| 3 | T3 영역 자동 진입 (Hermes upstream / Vault HSM / Tier-2-3 catalog / dev 환경 강제) | 사용자 명시 4 + 8-6 답습 |
| 4 | Operational Readiness PASS / Hermes PMO 격상 | 사용자 명시 5 + 8-7 답습 |
| 5 | hook entry 통한 *간접* dev 환경 강제 (예: CI 가 dev install 검증 step 추가) | 사용자 명시 1 답습 (간접 강제 회피) |
| 6 | commit signing / commit-msg stage hook 통한 간접 강제 | 사용자 명시 3 답습 (branch protection 영역) |
| 7 | Hermes upstream Dockerfile 변경 통한 hook 사전 install | 사용자 명시 4 답습 (T3 영역) |
| 8 | hook entry 와 CI step *불일치* (단일 source-of-truth 위반) | R-MVP1-G3-PC4-T2-INTG-2 답습 |
| 9 | 실 secret 본문 commit | R-4.1 + Group D §1.2 #1 답습 (영구 금지) |
| 10 | F-금지 위반 (workflow 본문 secret 토큰 사용 등) | G3-7 (i) 답습 (영구 금지) |
| 11 | 외부 LLM 자동 호출 | 사용자 명시 결정 없이 외부 LLM 호출 0건 답습 |
| 12 | Tier-2 / Tier-3 catalog 확장 (R-4.1 Tier-1 / URL Tier-1 / Model Tier-1 변경) | Backlog #3 별도 합의 영역 |

본 §8 = **사용자 명시 5 + 8 추가 + 영구 답습 한정** — 본 brief 발효 후 T2 sub 통합 진입 단계에서 위 12 금지 영역 위반 0건 유지 의무.

---

## 9. 다음 단계 결정 옵션 (사용자 결정 영역)

본 brief 작성 후 다음 작업 (사용자 결정 영역, 자동 진입 0건):

| 옵션 | 영역 | 다음 단계 |
|-----|------|--------|
| **(A)** | **본 brief 그대로 승인 → Reviewer-only 단축 합의 보고서 작성** (PC-4 T2 sub Backlog #1 + #2 통합 검토 결과 권위 source — T2 sub *통합 진입* 은 별도 합의) | 합의 보고서 작성 (`docs/review/3plus1-consensus-2026-05-14-c5c-pc4-t2-integrated-review.md` 가칭) |
| (B) | 본 brief 일부 수정 요청 → 수정 후 승인 | brief v2 작성 (사용자 명시 수정 영역 반영) |
| (C) | 본 brief 그대로 승인 → 후속 합의 보류 → T2 sub 통합 진입 합의 brief 작성 (실 진입 결정 직전 정비) | T2 sub 통합 진입 합의 brief 작성 |
| (D) | 본 brief 그대로 승인 → 후속 합의 보류 → 다른 backlog 우선 (예: MVP-2 / Backlog #2 단독 / Backlog #3) | 우선 backlog 결정 |
| (E) | 본 brief 작성 한정 → 세션 종료 | 다음 세션에서 사용자 명시 결정 |

### 9.1 권고 시작 명령 (사용자 권한 영역)

- **(A) 권고**: "옵션 (A)로 진행해주세요. 본 brief 를 그대로 승인하고, Reviewer-only 단축 합의 보고서 작성 단계로 진입하겠습니다."
- (B): "옵션 (B)로 진행해주세요. 본 brief 의 §X 를 다음과 같이 수정해주세요: ..."
- (C): "옵션 (C)로 진행해주세요. T2 sub 통합 진입 합의 brief 작성으로 진입합니다."
- (D): "옵션 (D)로 진행해주세요. 우선 backlog 결정으로 전환합니다."
- (E): "옵션 (E)로 진행해주세요. 세션 종료."

### 9.2 본 §9 의 *범위 한계*

본 §9 = *결정 옵션 enumeration 한정*. 실 다음 단계 결정 = 사용자 명시 결정 영역 (자동 진입 0건).

---

## 10. 본 brief 메타 검증

| 메타 검증 | 본 brief |
|---------|--------|
| 사용자 명시 진입 명령 답습 (통합 검토 방향 + 5 검토 영역 + 5 금지 + 8 추가 금지) | ✅ |
| 사용자 명시 5 검토 영역 답습 (GP-3 hook 3 / GP-5 hook 3 / 공통 config 구조 / T2·T3 분리 / 금지) | ✅ (§3.1 / §3.2 / §4 / §5 / §8) |
| 사용자 명시 5 금지 답습 (`pre-commit install` 강제 / dev 환경 강제 / branch protection / Operational Readiness PASS / Hermes PMO 격상) | ✅ (§0.3 + §8.1) |
| 사용자 명시 8 추가 금지 답습 (`.pre-commit-config.yaml` 작성 / `pre-commit install` 강제 / hook 구현 / GP-3·GP-5 1.5차 Satisfied 갱신 / MVP-1 PASS 재선언 / Operational Readiness PASS 선언 / T3 영역 자동 진입) | ✅ (§0.4 + §8.1) |
| §C-5 sub-condition 답습 (C-5a Satisfied / C-5b Deferred / C-5c Deferred / 전체 Partially Satisfied) | ✅ (변경 0건 — `6fa87dc` 답습) |
| §C-6 답습 (GP-5 1.5차 Deferred) | ✅ (변경 0건) |
| §5.5 9 sub-수단 본문 채택 답습 | ✅ (변경 0건 — 양 GP PC-3 본문 채택 유지) |
| C-1~C-8 상태 답습 | ✅ (변경 0건) |
| MVP-1 PASS Layer D 본문 답습 | ✅ (`210c98f` APPROVE WITH CONDITIONS 그대로 유지) |
| ADR-011 §2.4 T1/T2/T3 분류 답습 | ✅ (T2 sub 통합 한정 + T3 sub 자동 진입 0건 명시) |
| 5 영구 핵심 제약 보존 | ✅ (Provider Liquidity 5-way / Hermes ≠ root of trust / 메타포 강제 금지 / T3 분리 / 수단/목적 분리 모두 답습) |
| 7 backlog 분리 매트릭스 답습 | ✅ (Backlog #2 = 통합 검토 영역 답습 / #3/#4/#7 분리 명시 — 자동 진입 0건) |
| 양 GP PC-3 일관 채택 답습 (`55c5b4b`) | ✅ (§2.1 답습) |
| 풀 3+1 승격 트리거 0/7 발화 | ✅ (§6.3 답습) |
| 자동 진입 0건 | ✅ (모든 다음 단계 = 사용자 명시 결정 영역) |
| 합의 보고서 0건 / commit 0건 / push 0건 | ✅ (본 brief = 준비안 한정) |
| 실 `.pre-commit-config.yaml` 본문 작성 0건 | ✅ (통합 *검토* 한정) |
| 실 hook actual run 0건 | ✅ |
| ADR-012 §2.2 enum 정식 등록 0건 (candidate-only 유지) | ✅ |
| 선행 brief 답습 (`11d7ebb` Backlog #1 단독 brief) | ✅ (§1.1 + §1.2 답습) |

---

## 11. 본 brief 요약 (한 단락)

본 brief 는 **§C-5a Satisfied 갱신 (`6fa87dc`) 발효 후속, 선행 Backlog #1 단독 brief (`11d7ebb`) 위에서 사용자 결정 (옵션 β 통합 검토 방향) 답습한 §C-5c (PC-4 local pre-commit framework) 中 T2 sub-영역 (`.pre-commit-config.yaml` config 정의 가능성) 의 *Backlog #1 + Backlog #2 공유 통합 검토* 준비안 (DRAFT)** 이다. 사용자 명시 5 검토 영역 답습: (1) GP-3 local hook 3 후보 = secret-scanner / workflow-secret-usage-check / workflow-permissions-check (S-1 + G3-7 (i)+(ii)+(v) 본문 채택 답습) / (2) GP-5 local hook 3 후보 = provider-import-scanner / provider-url-model-scanner / import-linter (T-6 中 T-2 + T-5 본문 채택 답습) / (3) 공통 config 구조 = `repo: local` 한정 + `[pre-commit]` stage 한정 + 단일 source-of-truth (CI step 동등 명령) + runtime 합산 후보 < 30초 (병렬) / (4) T2/T3 분리 = `.pre-commit-config.yaml` 본문 정의 한정 T2 / `pre-commit install` 의무화 + dev 환경 강제 = T3 또는 별도 정책 (본 brief 영역 외) / (5) 금지 = 사용자 명시 5 + 8 추가 답습 + 추가 답습 = 합산 29 영역 0건 위반. 양 GP PC-3 일관 채택 답습 (`55c5b4b`) 위에서 통합 합의 = 변경 ledger 단일화 + Backlog #2 진입 시점 PC-4 부분 재합의 위험 0건. 합의 형태 권고 = **Reviewer-only 단축 합의 적격** (7/7 풀 3+1 트리거 0건 발화). T2 sub 통합 발효 시점 의무 정리 (Rollback Trigger 4 신규 후보 + Evidence ADR-011 (a)~(e) 답습) = 본 brief 영역 외 명시. **본 brief ≠ §C-5c 갱신 / Backlog #1 #2 진입 합의 / PC-4 수단 결정 / 실 `.pre-commit-config.yaml` 본문 작성 / hook 구현 / `pre-commit install` 의무화 / dev 환경 강제 / branch protection 변경 / T3 영역 진입 / GP-3·GP-5 1.5차 Satisfied 갱신 / MVP-1 PASS 재선언 / Layer E·F 격상 / 다른 backlog 자동 진입 / ADR 본문 자동 갱신** (사용자 명시 답습). 다음 단계 = 사용자 명시 결정 영역 (옵션 A~E, §9 답습).

---

**작성일**: 2026-05-14 후속 1
**상태**: DRAFT (사용자 명시 승인 *전*, 파일화 + commit 0건)
**다음 단계**: 사용자 명시 결정 영역 (옵션 A~E, §9 답습)
**금지 (사용자 명시 5 + 8 추가 + 추가 답습 — 본 brief 영역, 변동 없음)**:
- ❌ `pre-commit install` 강제 (사용자 명시 5-1 + 8-2)
- ❌ dev 환경 강제 (사용자 명시 5-2)
- ❌ branch protection 변경 (사용자 명시 5-3)
- ❌ Operational Readiness PASS (Layer E) 선언 (사용자 명시 5-4 + 8-7)
- ❌ Hermes PMO 격상 (Layer F) (사용자 명시 5-5)
- ❌ `.pre-commit-config.yaml` 실 본문 작성 (사용자 명시 8-1)
- ❌ hook 구현 (사용자 명시 8-3)
- ❌ GP-3 1.5차 Satisfied 갱신 (사용자 명시 8-4)
- ❌ GP-5 1.5차 Satisfied 갱신 (사용자 명시 8-4 대칭)
- ❌ MVP-1 PASS *재선언* (사용자 명시 8-5)
- ❌ T3 영역 *자동 진입* (사용자 명시 8-6)
- ❌ §C-5c Satisfied / 부분 Satisfied 갱신 발효
- ❌ §C-5 전체 표기 갱신 (`Partially Satisfied (C-5a only)` 변경)
- ❌ Backlog #1 / #2 진입 합의 발효
- ❌ PC-4 *수단 결정* (PC-1 ~ PC-4 채택 변경)
- ❌ §5.5 9 sub-수단 본문 채택 *변경* (PC-3 본문 채택 유지)
- ❌ threshold *고정*
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ ADR 본문 자동 갱신
- ❌ ADR-012 §2.2 enum 정식 등록 (`pre_commit_config_local_definition_unified` 가칭 = candidate-only)
- ❌ 다른 backlog (#3/#4/#7) 자동 진입
- ❌ C-2 / C-3 / C-4 / C-5a / C-5b / C-6 / C-7 / C-8 자동 변경
- ❌ 합의 보고서 작성
- ❌ CONTEXT / INDEX / SESSION 메타 갱신
- ❌ git commit / push
- ❌ 외부 LLM 자동 호출
- ❌ 실 API key / provider SDK / 외부 API 호출
