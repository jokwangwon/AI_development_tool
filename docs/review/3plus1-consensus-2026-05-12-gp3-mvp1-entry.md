# GP-3 (Credential / Secret Hygiene) MVP-1 진입 합의 보고서 (Reviewer-only 단축 합의)

**합의 형태**: **단축 합의 (Reviewer-only)** — 사용자 명시 결정 답습 + 5/5 풀 3+1 승격 트리거 0건 발화 검증 후 확정 (§4 답습)
**합의 일자**: 2026-05-12 후속 (MVP-1 roadmap DRAFT APPROVE 후속, commit `95be2e5` push 완료 후속)
**검토 대상**: GP-3 MVP-1 진입 권고 수단 조합 = **S-1 (Group D custom scanner — R-4.1 Tier-1 42 catalog 직접 답습) + ST-3 (docker secret 단독) + PC-3 (CI-only enforcement) + AR-1 (CI step fail-closed 한정)** + **Observation O-1 흡수** (G3-7 CI secret management 신설)
**보조 참조**: `docs/architecture/implementation-runtime-roadmap-mvp1.md` §3 + §5 (commit `cddd22f`), `docs/review/3plus1-consensus-2026-05-12-implementation-runtime-roadmap-mvp1.md` §1.5 + §5.1 (commit `95be2e5`), `docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md` (Group D PoC), `docs/architecture/governance-preconditions.md` §5 (GP-3 Entry/Exit), `docs/decisions/ADR-008-hermes-adoption-decision.md` §A.2 R1-2 + §2.6.2 R2-1, `docs/decisions/ADR-010-sqlcipher-vault-key-management.md`, `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.1 (a)~(e), `docs/decisions/ADR-012-evidence-ledger-protection.md` §2.2 (event enum)
**검토 목적**: GP-3 MVP-1 구현 진입에 사용할 수단 조합 (S-1 + ST-3 + PC-3 + AR-1) 의 *진입 적격성* 판단 + Observation O-1 (G3-7 CI secret management 신설) 흡수 한정
**판정**: ✅ **APPROVE WITH CONDITIONS (단축 합의 — Reviewer-only) — GP-3 MVP-1 진입 가능, 4 conditions 명시 (C-1 G3-7 부분 분리 / C-2 1.5차 보강 풀 3+1 / C-3 T3 영역 별도 풀 3+1 / C-4 O-2 GP-5 합의 후속), 5/5 풀 3+1 승격 트리거 0건 발화**

---

## 0. 사전 점검

### 0.1 가동 사유

사용자 명시 진입 명령 답습 (2026-05-12 세 번째 명령):

> "MVP-1 roadmap Reviewer-only 단축 합의가 APPROVE AS DRAFT 되었으므로 ... GP-3 MVP-1 진입 합의로 진행합니다. 권고 수단 후보 = S-1 + ST-3 + PC-3 + AR-1. ... O-1 G3-7 CI secret management 흡수."

**사용자 명시 결정 답습**:
- 검토 형태 = Reviewer-only 단축 합의 적격성 우선 판단 + 5 트리거 1+ 발화 시 풀 3+1 승격
- 검토 대상 = S-1 + ST-3 + PC-3 + AR-1 권고 수단 조합 + G3-7 CI secret management 흡수
- 검토 목적 = **GP-3 MVP-1 진입 *가능 여부* + 수단 조합 *적격성* + G3-7 흡수** 한정
- 결론 형식 = APPROVE / APPROVE WITH CONDITIONS / PARTIAL / BLOCK 中 1
- 본 합의 = **GP-3 Implementation Evidence PASS *선언* / GP-5 진입 승인 / runtime 구현 / CI-hook 구현 / Operational Readiness PASS / Hermes PMO 격상 모두 *불가***

### 0.2 단축 채택 사유

| 조건 | 충족 |
|-----|------|
| 새 *권위 결정* 0건 (본 검토 = 권고 수단 조합 *진입 적격성* 한정, *Implementation Evidence PASS 선언* 0건 + *수단 본문 채택 commit* 0건) | ✅ |
| 직전 합의 (`3plus1-consensus-2026-05-12-implementation-runtime-roadmap-mvp1.md` Reviewer-only) 패턴 답습 | ✅ |
| ADR-011 §2.4 T2 분류 (사용자 승인 기반 — 진입 적격성) | ✅ |
| 사용자 명시 결정으로 단축 합의 형태 채택 | ✅ §0.1 답습 |
| **5 풀 3+1 승격 트리거 발화 0건** | ✅ §4 답습 |

### 0.3 메타 편향 인지

본 Reviewer = Claude Opus 4.7 메인 컨텍스트 = `implementation-runtime-roadmap-mvp1.md` §3 GP-3 deepening 작성자. 자기 작성 권고 수단 (S-1 / ST-3 / PC-3 / AR-1) 자기 검토 한계 인지.

**청산 매커니즘**:

1. **사후 외부 LLM 충족** — 본 검토 답습 출처 (Group D PoC + R-4.1 + ADR-008 §A.2 + ADR-010 + ADR-011) 모두 cross-vendor 외부 LLM 합산 4건 권위 *내부* 작업 (P2 v3 정식 채택 + ADR-012 발행 답습)
2. **격상 전 면제** — Hermes PMO 격상 *전*. 본 검토 = MVP-1 진입 *적격성* 한정
3. **합의 권위 내부 변경** — 본 검토 = `3plus1-consensus-2026-05-12-implementation-runtime-roadmap-mvp1.md` (DRAFT APPROVE) 답습 = *권위 내부* 작업 (deepening of deepening)
4. **자기 작성 한계 명시** — 본 §0.3 + §5 명시
5. **수단 조합 *진입 적격성* 한정** — 본 합의 ≠ 수단 *본문 채택* — Implementation Evidence PASS 발효 시점에 ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 결정 별도 합의 의무 답습

### 0.4 비검토 대상 (사용자 명시 답습)

| 항목 | 본 검토 범위 |
|-----|----------|
| GP-3 Implementation Evidence PASS 선언 | ❌ (별도 합의 영역 — ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 결정) |
| GP-5 MVP-1 진입 승인 | ❌ (별도 합의 영역) |
| MVP-1 1.5차 보강 (S-3 detect-secrets / ST-2 inotify / PC-1 framework / AR-3 통합) | ❌ (풀 3+1 합의 영역, 본 검토 §3.6 답습) |
| T3 영역 진입 (AR-2 branch protection / Vault HSM / Tier-2/3 catalog 확장) | ❌ (별도 풀 3+1 + 외부 LLM 1+ + 사용자 명시) |
| MVP-1 roadmap §5.4 통합 위험 sub-section 신설 (Observation O-2) | ❌ (GP-5 합의 후속 영역) |
| 실 runtime code / CI workflow 수정 / hook 구현 | ❌ |
| ADR 본문 자동 갱신 | ❌ (cross-reference 답습 한정) |
| Tier-2 / Tier-3 catalog 자동 확장 | ❌ |
| threshold *고정* | ❌ (FP/FN/latency 모두 *후보 한정*) |
| 실 API key / provider SDK / 외부 API 호출 | ❌ |
| Operational Readiness PASS 선언 | ❌ |
| Hermes PMO 격상 선언 | ❌ |

---

## 1. 권고 수단 조합 평가

### 1.1 S-1 (Group D custom scanner — R-4.1 Tier-1 45 patterns 직접 답습)

| 평가 항목 | 본 검토 | 충족 |
|----------|--------|------|
| PoC 답습 충실성 | Group D PoC `tools/secret_scanner.py` 261줄 + `--mode scan-source` D-1 + `--mode scan-log` D-2 직접 답습 | ✅ |
| Tier-1 catalog 답습 | R-4.1 Tier-1 42 catalog (Prefix 36 + regex 7 + alternation 2) + baseline 5 = 45 patterns 변경 0건 | ✅ |
| Tier-2 / Tier-3 자동 확장 위험 | 0건 (Group D §2.1 답습 — gitleaks/detect-secrets/trufflehog 미도입 + custom 단독 채택) | ✅ |
| 외부 의존성 | 0건 (stdlib `re` 단독) | ✅ |
| FP risk (PoC 답습) | 0건 (Group D actual run `25623028888` D-1 PASS rc=0 violations=0) | ✅ |
| FN risk (PoC 답습) | base64 evasion 1건 (known limitation, Hermes upstream R2-6 영역 분리 명시) — Group D §8 #1 답습 | ⚠️ 부분 (분리 영역 명시) |
| 알려진 한계 | 11건 분리 영역 명시 (Group D §8) — base64 evasion + Hermes upstream + git pre-commit / PR auto-reject T3 / log canary nightly / Tier-2/3 / gitleaks 도입 / redactor 본문 / fixture 확장안 / markdown 자기 검출 | ✅ (분리 영역 명시) |
| MVP-1 영역 적격성 | S-1 = MVP-1 1차 영역 적격 (1.5차 = S-3 부분 통합 = 풀 3+1 영역 분리) | ✅ |

→ **S-1 = MVP-1 1차 진입 적격** (1.5차 S-3 부분 통합은 별도 풀 3+1 영역).

### 1.2 ST-3 (docker secret 단독)

| 평가 항목 | 본 검토 | 충족 |
|----------|--------|------|
| ADR 권위 답습 | ADR-008 차단조건 #6 + 부록 B 직접 답습 (docker secret 정의) + GP-3 §5.3 답습 | ✅ |
| Hermes upstream 변경 | 0건 (ST-1 chmod 600 entrypoint stat / ST-5 통합은 Hermes upstream 변경 필요, 본 검토 회피) | ✅ |
| 운영 부담 | 低 (`docker-compose.yml` 갱신만, sidecar process 0건) | ✅ |
| Defense in depth | ⚠️ 부분 (ST-1 / ST-2 inotify / ST-4 Vault HSM 미진입) — 본 영역 = 1.5차 보강 (ST-2 sidecar) + Operational Readiness PASS (ST-4 Vault HSM, ADR-010 답습) 분리 영역 |
| 격리 PoC 실증 가능성 | docker-compose.yml `secrets:` 정의 + secret 파일 image layer 미포함 검증 + chmod 644 시뮬레이션 → 컨테이너 정지 검증 | ✅ |
| MVP-1 영역 적격성 | ST-3 = MVP-1 1차 영역 적격 (1.5차 = ST-2 inotify 추가 = 풀 3+1 영역 분리, ST-4 Vault HSM = Operational Readiness 영역) | ✅ |

→ **ST-3 = MVP-1 1차 진입 적격** (1.5차 ST-2 / Operational Readiness ST-4 = 별도 영역).

### 1.3 PC-3 (CI-only enforcement)

| 평가 항목 | 본 검토 | 충족 |
|----------|--------|------|
| PoC 답습 충실성 | Group A 1차/2차/3차 + Group D PoC 모두 CI-only enforcement 답습 (pre-commit framework 미도입) | ✅ |
| dev 환경 영향 | 0건 (PC-1 pre-commit framework 미도입, dev 환경 자동 강제 0) | ✅ |
| commit 자체 차단 | ⚠️ 부분 (commit 가능, push 시 CI 차단) — 본 영역 = 1.5차 보강 (PC-1 framework) 영역 분리 |
| T2 영역 적격성 | T2 (CI step) — ADR-011 §2.4 답습, T3 미진입 | ✅ |
| MVP-1 영역 적격성 | PC-3 = MVP-1 1차 영역 적격 (1.5차 = PC-4 = PC-1 + PC-3 병행 = 단축 합의 + 사용자 명시) | ✅ |

→ **PC-3 = MVP-1 1차 진입 적격** (1.5차 PC-4 = 단축 합의 적격, PC-1 단독 = T2 정책 영역 단축).

### 1.4 AR-1 (CI step fail-closed 한정)

| 평가 항목 | 본 검토 | 충족 |
|----------|--------|------|
| PoC 답습 충실성 | Group A 1차/2차/3차 + Group D PoC 모두 CI step fail-closed 답습 | ✅ |
| T3 영역 진입 | 0건 (AR-2 GitHub branch protection rule 변경 = T3 영역, 본 검토 회피) | ✅ |
| 시스템 외부 PR 우회 위험 | ⚠️ 부분 (CI bypass 가능 — T3 영역 미진입의 trade-off) — 본 영역 = 1.5차 보강 (AR-3 = AR-1 + AR-2 통합) = 풀 3+1 영역 분리 |
| Hermes-originated commit auto-reject (G3 §2.2 #20) | ⚠️ 별도 영역 (G3 영역, 본 GP-3 합의 범위 외) — Group A 2차 답습 (G3 합의 후속 영역) |
| MVP-1 영역 적격성 | AR-1 = MVP-1 1차 영역 적격 (1.5차 = AR-3 통합 = 풀 3+1 + 외부 LLM 1+ + 사용자 명시) | ✅ |

→ **AR-1 = MVP-1 1차 진입 적격** (1.5차 AR-3 = 풀 3+1 영역).

### 1.5 4 수단 조합 종합 평가

| # | 수단 | MVP-1 영역 | 1.5차 보강 영역 | T3 진입 |
|---|-----|----------|--------------|-------|
| 1 | S-1 (Group D custom scanner) | ✅ 1차 적격 | S-3 부분 통합 = 풀 3+1 | Tier-2/3 catalog 확장 = 풀 3+1 + 외부 LLM 1+ |
| 2 | ST-3 (docker secret 단독) | ✅ 1차 적격 | ST-2 inotify sidecar = 풀 3+1 (Hermes upstream 회피 시 단축 적격) | ST-4 Vault HSM = ADR-010 진입 합의 + 외부 LLM 1+ |
| 3 | PC-3 (CI-only enforcement) | ✅ 1차 적격 | PC-4 (PC-1 + PC-3 병행) = 단축 + 사용자 명시 | — (T3 영역 0) |
| 4 | AR-1 (CI step fail-closed) | ✅ 1차 적격 | AR-3 (AR-1 + AR-2 통합) = 풀 3+1 + 외부 LLM 1+ + 사용자 명시 | AR-2 단독 = T3 영역 |

→ **4/4 수단 모두 MVP-1 1차 진입 적격**. 1.5차 보강 / T3 진입 영역 = 별도 합의 영역 분리 명시 (Conditions §6 답습).

---

## 2. Observation O-1 흡수 — G3-7 CI Secret Management 신설

### 2.1 신설 영역 정의

`implementation-runtime-roadmap-mvp1.md` §3.1.2 gap 매트릭스에 신규 row 추가 (Observation O-1 흡수, MVP-1 roadmap 단축 합의 §5.1 답습):

```
| G3-7 | CI secret 관리 (GitHub Actions secret) | **MVP-1 진입 의사결정 영역** —
       GitHub Actions secrets 사용 / `secrets.*` 참조 감지 / CI 로그 secret
       노출 방지 / fork PR secret 접근 차단 / workflow permissions 최소화 /
       secret 사용 evidence 기록 방식 中 어느 영역까지 MVP-1 영역? | 본 합의 §2 답습 |
```

**본 G3-7 신설 = MVP-1 roadmap §3.1.2 본문 갱신 영역** — 본 합의 자체는 *권고 한정*, 실 본문 갱신 = 사용자 명시 결정 영역 (§6.3 답습).

### 2.2 G3-7 6 검토 항목 평가 (사용자 명시 답습)

| # | 검토 항목 | 본 합의 평가 | MVP-1 / MVP-2/3 영역 |
|---|---------|----------|-------------------|
| (i) | GitHub Actions secrets 사용 여부 | 본 PoC = 사용 0건 (Group D fixture = fake canary 의무, F-금지 grep 자동 강제) | **MVP-1 영역** (현 시점 0건 답습 + 사용 시 별도 합의) |
| (ii) | `secrets.*` 참조 감지 | workflow grep 영역 — 단순 grep 가능 (custom scanner 확장 영역 또는 별도 도구) | **MVP-1 영역** (S-1 확장 또는 별도 grep step) |
| (iii) | CI 로그 secret 노출 방지 | redact filter (Hermes upstream 영역 분리, GP-2 송신 redaction 영역) + GitHub Actions log mask (built-in, `add-mask::` 답습) | **MVP-2 영역 (GP-2 redaction 분리)** + GitHub Actions built-in 부분 활용 |
| (iv) | fork PR 에서 secret 접근 차단 | GitHub default 정책 (fork PR = `secrets.*` 접근 X, `pull_request_target` 회피 의무) | **MVP-1 영역 (default 정책 명시 보존)** + 신규 `pull_request_target` workflow 도입 시 별도 합의 |
| (v) | workflow permissions 최소화 | `permissions: contents: read` 등 명시 강제 (R-6 답습 — `r2-canary.yml` 답습) | **MVP-1 영역** (모든 신규 workflow 의무 명시) |
| (vi) | secret 사용 evidence 기록 방식 | `event: ci_secret_used` 또는 `event: ci_secret_access_attempted` enum 후보 (ADR-012 §2.2 답습) | **MVP-1 영역** (4 enum 후보 §5.2 + 본 신규 enum 후보 합산 5 enum, 별도 합의 영역) |

**합산 = 4/6 MVP-1 영역 + 2/6 MVP-2/3 분리 영역** ((iii) GP-2 redaction 영역 분리 + (iv) `pull_request_target` 별도 합의 영역).

### 2.3 G3-7 enforcement 매트릭스 (MVP-1 영역 4 항목)

| 항목 | enforcement 수단 | T1/T2/T3 | 본 PoC 답습 |
|------|---------------|---------|-----------|
| (i) GitHub Actions secrets 사용 0건 | F-금지 grep step (Group D §9 #9 답습 — `sk-(?!FAKE)` / `AKIA(?!FAKE)` / `ghp_(?!FAKE)` 검출 시 `::error::` + exit 1) + `secrets.*` 참조 grep step (신규) | T2 (CI step) | Group D actual run `25623028888` 답습 |
| (ii) `secrets.*` 참조 감지 | workflow grep step (단순 `grep -r 'secrets\\.' .github/workflows/`) 또는 S-1 확장 (workflow file scan mode 신규) | T2 (CI step) | S-1 신규 mode 추가 가능 영역 (custom scanner 확장 영역) |
| (v) workflow permissions 최소화 | 모든 신규 workflow `permissions: contents: read` 명시 의무 + grep step (`grep -A 2 '^name:' .github/workflows/*.yml | grep -A 1 'permissions:'`) | T2 (CI step) | R-6 `r2-canary.yml` `permissions: contents: read` 직접 답습 |
| (vi) secret 사용 evidence 기록 | `event: ci_secret_access_attempted` enum 후보 신규 (ADR-012 §2.2 답습) — 본 PoC = 사용 0건이므로 enum 후보 발급만 (등록 0건) | T3 (event enum 정식 등록 = 별도 합의) | ADR-012 §2.2 + G4 §10.2 schema 진화 정책 답습 |

→ **G3-7 MVP-1 영역 4 항목 = MVP-1 1차 진입 적격** (모두 T2 영역 + 신규 enum 후보 = 권고 한정).

### 2.4 G3-7 분리 영역 2 항목 명시 (Condition C-1)

| 항목 | 분리 사유 | 분리 영역 |
|------|---------|---------|
| (iii) CI 로그 secret 노출 방지 | redact filter = GP-2 송신 redaction 영역 (Hermes upstream R2-6) + GitHub Actions log mask 일부 활용은 MVP-1 적격이지만 *전체 책무* = MVP-2 영역 | **MVP-2 (GP-2)** + GitHub Actions log mask 일부 MVP-1 부분 활용 |
| (iv) fork PR 에서 secret 접근 차단 (`pull_request_target` workflow 도입 시) | GitHub default 정책 보존 = MVP-1 영역 / 신규 `pull_request_target` workflow 도입 = secret 접근 활성화 trigger = T2/T3 영역 별도 합의 | **MVP-1 (default 정책 보존)** + **별도 합의 (`pull_request_target` 도입 시)** |

→ **2/2 분리 영역 명시 = Condition C-1**.

---

## 3. 사용자 명시 8 검토 기준 매트릭스

| # | 기준 | 평가 | 답습 |
|---|-----|----|----|
| 1 | S-1 이 GP-3 MVP-1 의 1차 secret source 관리 수단으로 적절한가 | ✅ 적격 | §1.1 표 (PoC 답습 + Tier-1 답습 + 외부 의존 0 + FP 0 + FN base64 분리) |
| 2 | ST-3 이 storage / secret boundary 수단으로 적절한가 | ✅ 적격 | §1.2 표 (ADR-008 §2.6.2 답습 + Hermes upstream 변경 0 + 운영 부담 低) |
| 3 | PC-3 이 pre-commit 또는 local verification 수단으로 적절한가 | ✅ 적격 (CI-only) | §1.3 표 (PoC 답습 + dev 환경 영향 0 + T2 영역) — 단 commit 자체 차단 부재 = 1.5차 보강 (PC-4) 영역 분리 |
| 4 | AR-1 이 PR auto-reject 또는 review enforcement 수단으로 적절한가 | ✅ 적격 (CI step) | §1.4 표 (T3 영역 진입 0) — 단 시스템 외부 PR 우회 위험 = 1.5차 보강 (AR-3) 영역 분리 |
| 5 | G3-7 CI secret management 를 포함했는가 | ✅ 포함 (Observation O-1 흡수) | §2 신설 — 6 항목 中 4 MVP-1 영역 + 2 분리 영역 = Condition C-1 |
| 6 | 실제 secret 을 사용하지 않는가 | ✅ 0건 | Group D PoC F-금지 grep step 자동 강제 (실 API key 0건) + 본 합의 = 사양 한정 (실 secret 0건) |
| 7 | secret scanner / evidence / rollback trigger 가 정의되어 있는가 | ✅ 정의 | scanner = S-1 §1.1 / evidence = §3.6.1 (5형식) + §2.3 G3-7 (`event: ci_secret_access_attempted` 신규 enum 후보) / rollback trigger = §3.5 (8개 R-MVP1-G3-1~7 + R-1) + 본 합의 §4 + §6.2 |
| 8 | Implementation Evidence PASS 와 Operational Readiness PASS 를 분리했는가 | ✅ 분리 | §1.2 ST-3 (Implementation Evidence) vs ST-4 Vault HSM (Operational Readiness, ADR-010 영역) 명시 + 본 합의 §0.4 비검토 대상 분리 |

→ **8/8 검토 기준 모두 충족** (#3, #4 = 부분 충족 항목 모두 1.5차 보강 영역 분리 명시).

---

## 4. 5 풀 3+1 승격 트리거 검증 (사용자 명시 답습)

| # | 트리거 | 본 검토 | 발화 |
|---|----|----|----|
| 1 | **secret handling 방식이 기존 정책을 바꾸는 경우** | 본 합의 = S-1 (R-4.1 Tier-1 catalog 답습 변경 0건) + ST-3 (ADR-008 차단조건 #6 + 부록 B 답습 변경 0건) + PC-3 / AR-1 (Group D PoC 답습 변경 0건). 기존 정책 변경 0건 | ❌ 0 |
| 2 | **GitHub Actions secret 사용 정책 변경이 필요한 경우** | 본 합의 = G3-7 (i)(iv) 답습 (현 시점 사용 0건 + fork PR default 정책 보존). 정책 변경 0건. 신규 `pull_request_target` workflow 도입 시 = 별도 합의 영역 분리 (§2.4 답습) | ❌ 0 |
| 3 | **Docker secret / local config / CI secret 경계가 불명확한 경우** | 본 합의 = ST-3 (Docker secret) + S-1 (local config + 코드 본문 secret 검출) + G3-7 (CI secret 관리) 영역 분리 명시 — §1 + §2 + §6.3 답습. 경계 명확 | ❌ 0 |
| 4 | **false positive / false negative risk 가 큰 경우** | S-1 = Group D PoC FP 0건 (D-1 PASS rc=0 violations=0) + FN 1건 (base64 evasion known limitation 분리 영역 명시). risk 측정 결과 = 본 PoC threshold 답습 (정량 측정 baseline = `secret_scanner --list-patterns` count=45). 신규 risk 0건 | ❌ 0 |
| 5 | **ADR-011 T3 영역에 닿는 경우** | 본 합의 = AR-1 (T2 CI step) + PC-3 (T2 CI step) + ST-3 (ADR-008 차단조건 #6 + 부록 B 답습 변경 0건) 모두 T2 영역. T3 영역 (AR-2 branch protection / Vault HSM ST-4 / Tier-2/3 catalog 확장) = 별도 풀 3+1 영역 분리 명시 (§0.4 + §6.3 = Condition C-3) | ❌ 0 |

→ **5/5 트리거 0건 발화** → **단축 합의 (Reviewer-only) 적격** 확정.

**G3-7 흡수가 트리거 발화 영역인가 검토**:
- (i) 사용 0건 = 정책 변경 0건 ❌
- (ii) `secrets.*` 참조 감지 = grep step 신규 = T2 영역 ❌
- (iii) 분리 영역 (MVP-2 GP-2 / GitHub log mask 부분) ❌
- (iv) default 정책 보존 + 별도 합의 영역 분리 ❌
- (v) `permissions: contents: read` 명시 = R-6 답습 = T2 영역 ❌
- (vi) `event: ci_secret_access_attempted` 신규 enum 후보 = 후보 한정 (정식 등록 = ADR-012 §2.2 + G4 §10.2 별도 합의 영역) ❌

→ **G3-7 흡수 = 트리거 발화 영역 아님** (모두 T2 영역 + 별도 합의 영역 분리 명시).

---

## 5. 메타 편향 자기진단

### 5.1 본 검토자의 컨텍스트 한계

본 Reviewer = Claude Opus 4.7 메인 컨텍스트 = `implementation-runtime-roadmap-mvp1.md` §3 GP-3 deepening 작성자 = 본 권고 수단 (S-1 / ST-3 / PC-3 / AR-1) 작성자. 자기 작성 권고 자기 검토 한계 인지.

### 5.2 본 한계의 청산

| # | 청산 원칙 | 본 검토 적용 |
|---|-------|--------|
| 1 | 사후 외부 LLM 충족 | 본 검토 답습 출처 (Group D + R-4.1 + ADR-008 + ADR-010 + ADR-011) 모두 cross-vendor 외부 LLM 합산 4건 권위 *내부* 작업 |
| 2 | 격상 전 면제 | Hermes PMO 격상 *전* — 본 검토 = MVP-1 진입 *적격성* 한정 |
| 3 | 합의 권위 내부 변경 | 본 검토 = `3plus1-consensus-2026-05-12-implementation-runtime-roadmap-mvp1.md` (DRAFT APPROVE) 답습 = *권위 내부* 작업 (deepening of deepening) |
| 4 | 자기 작성 한계 명시 | 본 §0.3 + §5 명시 |
| 5 | 진입 적격성 한정 (수단 본문 채택 ≠ 본 합의) | 본 합의 = *진입 적격성* — Implementation Evidence PASS 발효 시점 별도 합의 의무 답습 |

### 5.3 5 통제 답습

| # | 통제 | 본 검토 |
|---|-----|--------|
| 1 | 사용자 명시 절차 답습 | ✅ 사용자 명시 작업명 + 검토 형태 + 권고 수단 조합 + G3-7 흡수 + 8 검토 기준 + 5 트리거 + 결론 형식 + 8 금지 사항 모두 §0 + §1 + §2 + §3 + §4 + §6 답습 |
| 2 | R-7 SOP §0 핵심 선언 답습 | ✅ §0.4 비검토 대상 + §1 4 수단 평가 + §2 G3-7 흡수 + §3 8 검토 + §4 5 트리거 |
| 3 | ADR-011 §2.4 T1/T2/T3 답습 | ✅ §1.5 4 수단 모두 T2 영역 + T3 진입 영역 분리 + §2.3 G3-7 (vi) 신규 enum 후보 = T3 (정식 등록 = 별도 합의) |
| 4 | 수단/목적 분리 원칙 답습 | ✅ §1 + §2 + §3 모두 *수단 후보 평가* (목적 = Credential Hygiene 보호 + Provider Liquidity 보존) — ADR-011 §2.1 (a)~(e) 5조건 답습 |
| 5 | 본 합의가 *하지 않는* 것 명시 (§0.4 + §6.2) | ✅ 명시 |

### 5.4 본 단축 합의가 *하지 않는* 것

§6.2 답습.

---

## 6. 결론

```
✅ APPROVE WITH CONDITIONS (단축 합의, Reviewer-only)
   — GP-3 MVP-1 진입 가능 (S-1 + ST-3 + PC-3 + AR-1 4 수단 조합 1차 적격)
   — Observation O-1 흡수 (G3-7 CI secret management 신설 — MVP-1 영역 4 항목 + 분리 영역 2 항목)
   — 4 Conditions 명시:
     C-1: G3-7 6 항목 中 (iii)(iv) 분리 영역 명시
     C-2: 1.5차 보강 영역 (S-3 / ST-2 / PC-1+PC-3 = PC-4 / AR-3) = 풀 3+1 또는 단축 합의 영역 분리
     C-3: T3 영역 (AR-2 branch protection / Vault HSM / Tier-2/3 catalog) = 별도 풀 3+1 + 외부 LLM 1+ + 사용자 명시
     C-4: O-2 (GP-3 + GP-5 통합 위험) = GP-5 합의 후 §5.4 신설 영역 분리
   — 5/5 풀 3+1 승격 트리거 0건 발화 → 단축 합의 적격 확정
```

본 결론은 **GP-3 MVP-1 *진입 가능 여부* + 4 수단 조합 *적격성* + G3-7 흡수** 한정. **본 합의는 GP-3 Implementation Evidence PASS *선언* / GP-5 진입 승인 / runtime 구현 / CI-hook 구현 / Operational Readiness PASS / Hermes PMO 격상 / 수단 본문 채택 commit 모두 *불가***.

### 6.1 본 합의가 *발생시키는* 것

- ✅ GP-3 MVP-1 진입 *적격성* 권위 권고 발행 (4 수단 조합 = S-1 + ST-3 + PC-3 + AR-1)
- ✅ S-1 (Group D custom scanner R-4.1 Tier-1 45 patterns 답습) MVP-1 1차 영역 적격 권위 권고
- ✅ ST-3 (docker secret 단독, ADR-008 차단조건 #6 + 부록 B 답습) MVP-1 1차 영역 적격 권위 권고
- ✅ PC-3 (CI-only enforcement, T2 영역) MVP-1 1차 영역 적격 권위 권고
- ✅ AR-1 (CI step fail-closed, T3 미진입) MVP-1 1차 영역 적격 권위 권고
- ✅ **Observation O-1 흡수** = G3-7 CI secret management 신설 권위 권고 (6 항목 中 4 MVP-1 영역 + 2 분리 영역)
- ✅ G3-7 enforcement 매트릭스 4 항목 (F-금지 grep / `secrets.*` 참조 grep / `permissions: contents: read` 명시 / `event: ci_secret_access_attempted` 신규 enum 후보) 권위 권고
- ✅ G3-7 분리 영역 2 항목 (CI 로그 redact = MVP-2 GP-2 영역 / `pull_request_target` 도입 = 별도 합의) 명시 = Condition C-1
- ✅ 1.5차 보강 영역 4 후보 (S-3 / ST-2 / PC-4 / AR-3) 분리 영역 명시 = Condition C-2
- ✅ T3 영역 3 후보 (AR-2 / Vault HSM / Tier-2/3 catalog) 분리 영역 명시 = Condition C-3
- ✅ O-2 (GP-3 + GP-5 통합 위험) 영역 분리 명시 = Condition C-4 (GP-5 합의 후속 영역)
- ✅ MVP-1 roadmap §3.1.2 gap 매트릭스에 G3-7 row 추가 = 사용자 명시 결정 영역 (실 본문 갱신 = 별도 commit)
- ✅ Evidence Ledger enum 후보 5번째 신규 (`event: ci_secret_access_attempted`) = 후보 한정 (정식 등록 = 별도 합의)

### 6.2 본 합의가 *발생시키지 않는* 것 (사용자 명시 답습 — 2026-05-12 진입 명령 답습)

- ❌ GP-3 Implementation Evidence PASS 선언
- ❌ GP-5 MVP-1 진입 승인 (자동)
- ❌ runtime code 구현 (`tools/secret_scanner.py` 본문 변경 / `docker-compose.yml` secret 정의 / inotify sidecar / chmod 600 entrypoint script 등 0건)
- ❌ CI workflow 수정 / hook 구현 (`.github/workflows/secret-scan.yml` 신설 / `.pre-commit-config.yaml` 신설 / GitHub branch protection rule 변경 / `permissions: contents: read` 강제 grep step 신설 등 0건)
- ❌ Operational Readiness PASS 선언
- ❌ Hermes PMO 격상 선언
- ❌ 수단 *본문 채택* commit (S-1 / ST-3 / PC-3 / AR-1 = 진입 *적격성* 권위 권고 한정, 본문 채택 commit = 별도 합의 + ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시)
- ❌ ADR 본문 자동 갱신 (cross-reference 답습 한정 — ADR-008 §A.2 / ADR-010 / ADR-012 본문 변경 0건)
- ❌ Tier-2 / Tier-3 catalog 자동 확장 (R-4.1 Tier-1 45 patterns 답습 한정)
- ❌ threshold *고정* (FP/FN/scan_latency 모두 *후보 한정*)
- ❌ 1.5차 보강 자동 진입 (S-3 / ST-2 / PC-4 / AR-3 = Condition C-2 별도 합의 영역 분리)
- ❌ T3 영역 자동 진입 (AR-2 / Vault HSM / Tier-2/3 catalog = Condition C-3 별도 풀 3+1 영역 분리)
- ❌ MVP-1 roadmap §3.1.2 본문 자동 갱신 (G3-7 row 추가 권고 = 별도 commit + 사용자 명시 결정)
- ❌ MVP-1 roadmap §5.4 통합 위험 sub-section 자동 신설 (O-2 흡수 = Condition C-4 GP-5 합의 후속 영역)
- ❌ ADR-012 §2.2 `event` enum 정식 등록 (`event: ci_secret_access_attempted` = 후보 한정)
- ❌ 외부 LLM 자동 호출
- ❌ 실 API key / provider SDK / 외부 API 호출

### 6.3 다음 진입점 (사용자 결정 영역)

본 합의 APPROVE WITH CONDITIONS → GP-3 MVP-1 진입 *적격성* 권위 권고 발효 → 다음 작업 (사용자 결정 영역):

| 후보 | 영역 | 합의 형태 | Conditions 흡수 |
|------|------|---------|----------------|
| (b-1) | **MVP-1 roadmap §3.1.2 G3-7 row 본문 추가 commit** | 단축 commit (사용자 명시 결정) | C-1 흡수 (본 합의 §2 답습) |
| (c) | **GP-5 MVP-1 진입 합의 시작** (T-6 + PC-3 + AR-1) | Reviewer-only 단축 합의 | — |
| (b+c 통합 시점) | **MVP-1 roadmap §5.4 통합 위험 sub-section 신설** (Observation O-2 흡수) | 단축 합의 적격 (본 합의 §6.1 + GP-5 합의 후속 영역) | C-4 흡수 |
| (d-1) | **GP-3 MVP-1 1.5차 보강 합의** (S-3 detect-secrets 부분 통합) | 풀 3+1 합의 + Tier-2/3 catalog 확장 결정 (Group D §10 trigger #4 답습) | C-2 흡수 |
| (d-2) | **GP-3 MVP-1 1.5차 보강 합의** (ST-2 inotify sidecar) | 풀 3+1 합의 (Hermes upstream 변경 회피 시 단축 적격) | C-2 흡수 |
| (d-3) | **GP-3 MVP-1 1.5차 보강 합의** (PC-1 / PC-4 framework 도입) | 단축 합의 + 사용자 명시 (T2 정책 영역) | C-2 흡수 |
| (d-4) | **GP-3 MVP-1 1.5차 보강 합의** (AR-3 = AR-1 + AR-2 통합) | 풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시 (T3 영역) | C-2 + C-3 흡수 |
| (e-1) | **GP-3 Implementation Evidence PASS 발효 합의** | 별도 합의 + 사용자 명시 + ADR-011 §2.1 (a)~(e) 5/5 evidence | — (전체 conditions 충족 후) |
| (e-2) | **MVP-1 PASS 발효** (GP-3 + GP-5 통합) | 별도 합의 + 사용자 명시 + Implementation Evidence PASS 발효 | — (전체 conditions 충족 후) |

**권고 시작 명령** (사용자 권한 영역):

- **"MVP-1 roadmap §3.1.2 에 G3-7 row 추가 commit"** — Condition C-1 흡수 (단축 commit)
- **"GP-5 MVP-1 진입 합의 시작 (T-6 + PC-3 + AR-1)"** — GP-5 1차 합의 진입
- **"GP-5 합의 후 §5.4 통합 위험 sub-section 신설"** — Condition C-4 흡수 (Observation O-2)
- **"GP-3 1.5차 보강 합의 진입 (수단 d-1 ~ d-4 中 1)"** — Condition C-2 / C-3 흡수 (풀 3+1)
- **"GP-3 Implementation Evidence PASS 발효 합의"** — 전체 conditions 충족 후 (별도 합의)

본 합의 자체 = **GP-3 MVP-1 진입 *적격성* 권위 권고 발행 + Conditions 4 영역 분리 명시 + Observation O-1 흡수 권고**. 진입 결정 = 사용자 명시 결정 영역.

---

## 7. Conditions 매트릭스 (보강/분리 영역)

### 7.1 Condition C-1 — G3-7 6 항목 中 (iii)(iv) 분리 영역 명시

| 항목 | 분리 사유 | 분리 영역 | 처리 시점 |
|------|---------|---------|---------|
| (iii) CI 로그 secret 노출 방지 | redact filter = GP-2 송신 redaction 영역 (Hermes upstream R2-6) — *전체 책무* = MVP-2 영역 | MVP-2 (GP-2) + GitHub Actions log mask 부분 활용 (MVP-1 적격) | MVP-2 영역 deepening 합의 시점 |
| (iv) fork PR 에서 secret 접근 차단 (`pull_request_target` workflow 도입 시) | GitHub default 정책 보존 = MVP-1 영역 / `pull_request_target` 도입 = secret 접근 활성화 trigger = T2/T3 영역 별도 합의 | MVP-1 (default 정책 보존) + 별도 합의 (`pull_request_target` 도입 시) | MVP-1 진입 합의 진입 시점 (default 정책 보존) + `pull_request_target` 도입 시 별도 |

### 7.2 Condition C-2 — 1.5차 보강 영역 (S-3 / ST-2 / PC-4 / AR-3) 분리

| 후보 | 합의 형태 | 사유 |
|------|--------|------|
| S-3 detect-secrets 부분 통합 | 풀 3+1 + Tier-2/3 catalog 확장 결정 | Group D §10 trigger #4 답습 + 사용자 명시 풀 3+1 trigger #4 발화 위험 |
| ST-2 inotify sidecar | 풀 3+1 (Hermes upstream 변경 회피 시 단축 적격) | sidecar 분리 가능 = Hermes upstream 변경 회피 영역 |
| PC-4 (PC-1 + PC-3 병행) | 단축 합의 + 사용자 명시 | T2 정책 영역 (ADR-011 §2.4) |
| AR-3 (AR-1 + AR-2 통합) | 풀 3+1 + 외부 LLM 1+ + 사용자 명시 | T3 영역 (branch protection rule 변경) |

### 7.3 Condition C-3 — T3 영역 진입 분리

| 후보 | T3 영역 | 합의 형태 |
|------|-------|--------|
| AR-2 단독 (branch protection rule 변경) | branch protection rule = T3 (repo policy 수준) | 풀 3+1 + 외부 LLM 1+ + 사용자 명시 |
| Vault HSM (ST-4) | 외부 인프라 + Multi-host = T3 + Operational Readiness PASS 영역 | ADR-010 §X 진입 합의 + 외부 LLM 1+ |
| Tier-2 / Tier-3 catalog 확장 (Slack / GCP / Azure 등) | catalog 확장 = T3 (정책 영역) | 풀 3+1 + 외부 LLM 1+ |

### 7.4 Condition C-4 — Observation O-2 (GP-3 + GP-5 통합 위험) 분리

| 항목 | 처리 시점 | 합의 형태 |
|------|---------|--------|
| MVP-1 roadmap §5.4 통합 위험 sub-section 신설 | GP-5 합의 후속 영역 (b+c 통합 시점) | 단축 합의 적격 (양 GP Rollback 답습 + ADR-011 §2.1 5/5 답습 영역) |
| 통합 위험 3 row 본문화 | (i) provider key adapter 우회 / (ii) direct SDK + secret leakage 결합 / (iii) local-CI-Docker 일관성 | 본 §5.4 신설 시 통합 |

### 7.5 4 Conditions 합의 형태 권고 종합

| 합의 영역 | 합의 형태 | 사유 |
|---------|---------|------|
| 본 합의 자체 (GP-3 MVP-1 진입 적격성) | Reviewer-only 단축 합의 (본 보고서) | 사용자 명시 진입 명령 답습 + 5 트리거 0/5 발화 |
| C-1 흡수 (G3-7 row 본문 추가) | 단축 commit (사용자 명시 결정) | 본 합의 §2 답습 + 새 권위 결정 0건 |
| C-2 흡수 (1.5차 보강) | 풀 3+1 (S-3 / ST-2 / AR-3) + 단축 (PC-4) | 수단별 trade-off |
| C-3 흡수 (T3 영역 진입) | 풀 3+1 + 외부 LLM 1+ + 사용자 명시 | T3 영역 답습 |
| C-4 흡수 (O-2 §5.4 신설) | GP-5 합의 후속 단축 합의 | 양 GP Rollback 답습 영역 |

---

**합의 commit 권위**: 본 commit (`docs(review): record GP-3 MVP-1 entry consensus APPROVE WITH CONDITIONS`)
**본 commit + 직전 commits (`cddd22f` MVP-1 roadmap 본문 + `6c91980` references + `95be2e5` MVP-1 roadmap 단축 합의) = MVP-1 roadmap deepening 작성 + DRAFT 적격성 합의 + GP-3 진입 적격성 합의 완료**
**다음 세션 진입점**: 사용자 결정 영역 — (b-1) MVP-1 roadmap §3.1.2 G3-7 row 추가 commit (Condition C-1 흡수) / (c) GP-5 MVP-1 진입 합의 (T-6 + PC-3 + AR-1) / (b+c 통합 시점) §5.4 통합 위험 sub-section 신설 (Condition C-4 = Observation O-2 흡수) / (d-1~d-4) GP-3 1.5차 보강 합의 (Condition C-2/C-3 흡수, 풀 3+1) / (e-1, e-2) Implementation Evidence PASS / MVP-1 PASS 발효 합의 (전체 conditions 충족 후)
