# Backlog #6 Runtime Enforcement / CI-hook Implementation Entry 합의 보고서 (Layer B — Reviewer-only 단축 합의)

**합의 형태**: **단축 합의 (Reviewer-only)** — 사용자 명시 결정 답습 (옵션 (A) brief 그대로 승인) + 6/6 풀 3+1 승격 트리거 0건 발화 검증 후 확정 (§2 답습)
**합의 일자**: 2026-05-12 후속 10 (Backlog #6 Layer A 합의 발효 (`f1e0b23` + `ca7b24e`, `df20b15..f1e0b23..ca7b24e`) 후속 + 본 Layer B brief 옵션 (A) 승인 후속)
**검토 대상**: **Backlog #6 Runtime Enforcement / CI-hook Implementation Entry 합의 (Layer B)** — 즉 9 sub-수단 *권고 → 본문 채택* 격상 + 실 runtime code / CI workflow / hook 구현 *시작 권한* 발효 적격성 판단
**보조 참조**: brief §3 입력 자료 9 항목 (commits `cddd22f → ca7b24e` 합산 14 commits push 완료, `docs/architecture/implementation-runtime-roadmap-mvp1.md` + `docs/review/3plus1-consensus-2026-05-12-mvp1-implementation-entry.md` + `docs/review/3plus1-consensus-2026-05-12-backlog6-runtime-ci-hook-entry.md` (Layer A) + `docs/review/3plus1-consensus-2026-05-12-gp3-mvp1-entry.md` + `docs/review/3plus1-consensus-2026-05-12-gp5-mvp1-entry.md` + `docs/phase0/mvp1-gp3-gp5-condition-status.md` + Group A 1차/2차/3차 PoC + Group D PoC + ADR-008/009/010/011/012 + ADR-011 §2.1 (a)~(e))
**검토 목적**: Backlog #6 implementation entry 합의 (Layer B) — runtime code / CI workflow / hook 구현 *시작 권한 발효* 적격성 판단 (Implementation Evidence PASS *발효 자체* 가 아님 — Layer C 별도 합의 영역)
**판정**: ✅ **APPROVE — Backlog #6 Layer B Implementation Entry 합의 발효 가능 (단축 합의 — Reviewer-only) — 9 sub-수단 권고 → 본문 채택 격상 적격, runtime code / CI workflow / hook 구현 시작 권한 발효 가능, 8/8 검토 기준 모두 충족, 6/6 풀 3+1 승격 트리거 0건 발화**

---

## 0. 사전 점검

### 0.1 가동 사유

사용자 명시 진입 명령 답습 (2026-05-12 열 번째 명령 — 옵션 (1) Layer B brief 준비 → 옵션 (A) brief 그대로 승인):

> "옵션 (A)로 진행해주세요. 본 brief를 그대로 승인하고, Layer B 합의 보고서 작성 단계로 진입하겠습니다 ... 산출 경로 = `docs/review/3plus1-consensus-2026-05-12-backlog6-implementation-entry.md`."

**사용자 명시 결정 답습**:
- 검토 형태 = Reviewer-only 단축 합의 적격성 우선 판단 + 6 트리거 1+ 발화 시 풀 3+1 승격 (brief §5 답습)
- 검토 대상 = Backlog #6 Layer B implementation entry 합의 적격성 (brief §1.1 답습)
- 검토 목적 = runtime code / CI workflow / hook 구현 *시작 권한 발효* 적격성 (brief §1 답습)
- 8 검토 기준 = brief §2 그대로 채택
- 4 판정 옵션 = brief §4.1 그대로 채택
- 6 풀 3+1 승격 트리거 = brief §4.2 그대로 채택
- 9 금지 사항 = brief §8 그대로 채택
- **Layer B APPROVE 이후 주의 답습** = "Layer B가 APPROVE되더라도, 바로 구현을 자동 시작하지 말고 사용자 명시 결정 후 다음 단계로 넘어가세요" (사용자 명시 강조 — §5.3 + §5.4 답습)
- 산출 경로 = `docs/review/3plus1-consensus-2026-05-12-backlog6-implementation-entry.md` (사용자 명시 답습)
- 본 합의 = **Implementation Evidence PASS *발효* (Layer C) / runtime code *자동 진입* / CI workflow *자동 신설* / hook *자동 구현* / 9 sub-수단 *본문 채택 commit 자동 진입* / 7 backlog *자동 진입* / MVP-1 PASS / Operational Readiness PASS / Hermes PMO 격상 / ADR 본문 자동 갱신 모두 *불가***

### 0.2 단축 채택 사유

| 조건 | 충족 |
|-----|------|
| 9 sub-수단 모두 prior 합의 (GP-3 진입 / GP-5 진입 / MVP-1 Implementation Entry / Layer A) 에서 *권고 한정* 확정 답습 (새 수단 발명 0건) | ✅ |
| 본 합의 = 권고 → 본문 채택 격상 + 시작 권한 발효 한정 (Layer A APPROVE 답습 한 layer 하위) | ✅ |
| ADR-011 §2.4 T2 분류 (사용자 승인 기반 — Implementation Entry 시작 권한) | ✅ |
| 사용자 명시 결정으로 단축 합의 형태 채택 (옵션 (A) brief 그대로 승인) | ✅ §0.1 답습 |
| **6 풀 3+1 승격 트리거 발화 0건** | ✅ §2 답습 |
| Layer A → Layer B 진입 = Entry 패턴 답습 한 layer 하위 (`f1e0b23` Layer A APPROVE 답습) | ✅ |

### 0.3 메타 편향 인지

본 Reviewer = Claude Opus 4.7 메인 컨텍스트 = MVP-1 roadmap 작성자 + GP-3 / GP-5 / MVP-1 Implementation Entry / Backlog #6 Layer A 합의 보고서 작성자 + 본 brief v1 → 본 brief 작성자. 자기 작성 권위 누적 자기 검토 한계 인지.

**청산 매커니즘**:

1. **사후 외부 LLM 충족** — 본 검토 답습 출처 (외부 LLM 응답 line 242 + C-7 line 378 + Group A 2차 풀 3+1 합의 + cross-vendor 외부 LLM 합산 4건) 모두 권위 *내부* 작업
2. **격상 전 면제** — Hermes PMO 격상 *전*. 본 검토 = Layer B *시작 권한 발효* 한정 (Implementation Evidence PASS 미진입 / MVP-1 PASS 미진입 / Operational Readiness PASS 미진입 / PMO 격상 미진입)
3. **합의 권위 내부 변경** — 본 검토 = Layer A 합의 + brief 답습 = *권위 내부* 작업 (Layer A → Layer B 단계 답습)
4. **자기 작성 한계 명시** — 본 §0.3 + §4 명시
5. **Layer B *시작 권한 발효* 한정** (Implementation Evidence PASS 발효 / runtime code 작성 / CI workflow 신설 / hook 구현 / 9 sub-수단 본문 채택 commit 모두 본 합의 발효 *후* 사용자 명시 결정 영역) — 본 합의 = *Layer B 시작 권한 발효 적격성*
6. **누적 권위 검증** — 본 검토 = 14 commits push 완료 후 진입 (origin 동기화 검증 — `ca7b24e (HEAD -> feature/hermes-phase0, origin/feature/hermes-phase0)` 답습)
7. **brief 옵션 (A) 그대로 승인 답습** — 본 합의 = brief §1~§4 + 6 트리거 + 4 판정 옵션 + 9 금지 사항 그대로 채택 (사용자 변경 0건)
8. **Layer B APPROVE 후 자동 구현 진입 금지 답습** — 사용자 명시 (§0.1 답습) — 본 §5.3 + §5.4 답습

### 0.4 비검토 대상 (사용자 명시 답습 — brief §1.6 + §8 답습)

| 항목 | 본 검토 범위 |
|-----|----------|
| **Implementation Evidence PASS *발효*** (Layer C) | ❌ (Layer B 종료 후 별도 합의 영역 — ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시) |
| **MVP-1 PASS *선언*** (Layer D) | ❌ (별도 합의 영역) |
| **Operational Readiness PASS *선언*** (Layer E) | ❌ (MVP-6 영역) |
| **Hermes PMO 격상 *선언*** (Layer F) | ❌ (MVP-6 영역) |
| **runtime code 실 구현** (Layer B 발효 후 영역) | ❌ (본 합의 = 시작 권한 발효 *적격성* 한정, 사용자 명시 후 별도 진입) |
| **CI workflow 실 신설 / hook 실 구현** (Layer B 발효 후 영역) | ❌ (동상) |
| **9 sub-수단 본문 채택 commit** (Layer B 발효 후 영역) | ❌ (동상) |
| **7 backlog 자동 진입** (#1 GP-3 1.5차 / #2 GP-5 1.5차 / #3 T3 / #4 P1 v2 facade / #5 ADR-012 enum / #7 Operational Readiness) | ❌ (모두 별도 합의 영역) |
| **GP-3 / GP-5 / MVP-1 Implementation Entry / Layer A 진입 합의 자체 변경** (재합의) | ❌ (각 합의 발효 답습 — 변경 0건) |
| **ADR 본문 자동 갱신** | ❌ (cross-reference 답습 한정 — ADR-008/009/010/011/012 본문 변경 0건) |
| **Tier-2 / Tier-3 catalog 자동 확장** | ❌ (Tier-1 답습 한정) |
| **외부 LLM 자동 호출 / 실 API key / 실 provider SDK / 실 외부 API 호출** | ❌ |

---

## 1. 8 검토 기준 평가 매트릭스 (brief §2 답습)

### 1.1 검토 기준 #1 — GP-3 구현 진입 기준

| 항목 | 본 검토 답습 | 충족 |
|------|----------|------|
| **S-1 본문 채택 적격성** | Group D PoC (`tools/secret_scanner.py` 261줄) 답습 변경 0건 + R-4.1 Tier-1 45 patterns 답습 변경 0건 + actual run `25623028888` SUCCESS 답습 + Layer A §1.2 답습 | ✅ |
| **ST-3 본문 채택 적격성** | docker secret 단독 (ADR-008 차단조건 #6 (Docker 격리) 답습) + Tier-2 (Vault HSM) 미진입 (Backlog #7 Operational Readiness 분리) + Layer A §1.2 답습 (37번째 entry R-S1 정정 답습) | ✅ |
| **PC-3 본문 채택 적격성** | CI-only enforcement (T2 영역) + local pre-commit framework PC-4 미진입 (Backlog #1 1.5차 보강 분리) + Layer A §1.2 답습 | ✅ |
| **AR-1 본문 채택 적격성** | CI step fail-closed (T2 영역) + branch protection AR-2 미진입 (Backlog #3 T3 영역 분리) + Layer A §1.2 답습 | ✅ |
| **G3-7 row 4 항목** | MVP-1 영역 4 항목 ((i) GitHub Actions secrets 사용 0건 grep / (ii) `secrets.*` 참조 감지 / (iv) fork PR secret 접근 차단 default / (v) workflow `permissions: contents: read` 명시) — 본문 채택 적격 / 분리 영역 2 항목 ((iii)(`pull_request_target`)) — Backlog #1 + T2/T3 별도 합의 분리 | ✅ |

→ **GP-3 구현 진입 기준 5/5 충족**.

### 1.2 검토 기준 #2 — GP-5 구현 진입 기준

| 항목 | 본 검토 답습 | 충족 |
|------|----------|------|
| **T-6 (T-2 + T-5 병행) 본문 채택 적격성** | Group A 2차 풀 3+1 합의 (Agent A/B/C 1206줄 + Reviewer 380줄) T-2 import-linter 채택 답습 + Group A 1차/3차 답습 T-5 custom AST 답습 변경 0건 + actual run `25605665191` + `25629390384` SUCCESS 답습 + Layer A §1.3 답습 | ✅ |
| **`.importlinter` 본문 확정 적격성** | TR-1~TR-5 답습 + 5-vendor (anthropic / openai / litellm / google.generativeai / ollama) 차단 답습 변경 0건 + Group A 2차 합의 §C-9 RA-9 사전 검증 PASS 답습 | ✅ |
| **PC-3 + AR-1 본문 채택 적격성** | §1.1 동일 (양 GP 일관성 답습 — GP-3 / GP-5 모두 PC-3 + AR-1 동일 채택) | ✅ |
| **Layer 1 정적 범위 한정** | Layer 2 runtime block (G5-5) 미진입 + 의미적 lock-in (G4 §4.6) 미진입 (MVP-3 분리) + 책무 분담 매트릭스 7/8 cover 답습 (GP-5 진입 합의 §5.1 답습) | ✅ |
| **GP-3 ↔ GP-5 일관성** | PC-3 + AR-1 양 GP 동일 채택 (충돌 0건) — MVP-1 Implementation Entry 합의 §1.2 답습 | ✅ |

→ **GP-5 구현 진입 기준 5/5 충족**.

### 1.3 검토 기준 #3 — 채택 수단 후보의 lock-in 위험

| 수단 | lock-in 위험 평가 | 충족 |
|------|--------------|------|
| **S-1 custom regex** | R-4.1 Tier-1 45 patterns 한정 답습 — vendor lock-in 영향 0건 (5-vendor 모두 동일 catalog) | ✅ |
| **ST-3 docker secret** | Docker 표준 (vendor agnostic) — lock-in 0건 | ✅ |
| **PC-3 CI-only** | GitHub Actions 답습 시 vendor 일치 의무 → 본문 cross-reference 답습 (P11 supply-chain compromise 답습 — Layer 1 Lockfile + Layer 4 CI Auto-recheck 답습). GitLab CI / CircleCI / 기타 CI 호환 영역 = 미진입 (1.5차 보강 영역 분리) | ✅ |
| **AR-1 CI step** | 동상 | ✅ |
| **T-2 import-linter** | OSS BSD license (P11 supply-chain 5 Layer 답습 — Lockfile + Action SHA Pin + Checksum/SBOM + CI Auto-recheck + External SBOM 의무) + Python 표준 + Group A 2차 풀 3+1 채택 답습 — lock-in 0건 | ✅ |
| **T-5 custom AST** | stdlib `ast` 답습 — lock-in 0건 | ✅ |
| **T-6 병행** | T-2 + T-5 모두 lock-in 0건 + facade single entry 강제 = Provider Liquidity 5-way Layer 1 모법 답습 변경 0건 | ✅ |

→ **7/7 수단 lock-in 위험 0건 충족**.

### 1.4 검토 기준 #4 — Provider Liquidity 보존 여부 ([[feedback_provider_liquidity]] 답습)

| 보존 검증 | 본 합의 답습 | 충족 |
|---------|--------|------|
| **모델/구독 교체가 코드 변경 없이 가능** | T-6 (T-2 + T-5) = facade single entry 강제 = Provider Liquidity 5-way Layer 1 모법 답습 변경 0건. `.importlinter` rule 본문 채택 시 5-vendor 동등 차단 답습 | ✅ |
| **5-vendor 동등 차단** | anthropic / openai / litellm / google.generativeai / ollama 모두 동일 차단 매트릭스 답습 (Group A 2차 풀 3+1 합의 §5.1 + Group A 3차 PoC URL Tier-1 catalog 10 + Model Tier-1 catalog 19 답습) | ✅ |
| **facade *real 본문* 변경** | Backlog #4 영역 분리 (G5-4 P1 v2 facade MVP 합의) — 본 합의 = facade *placeholder* 답습 한정 (Group A 2차 §8 TR-1 답습 — facade real 본문 작성 = T-2 룰 ignore_imports 검증 재합의 trigger) | ✅ |
| **메타포 강제 금지** | 9 sub-수단 中 의미적 lock-in 일으키는 수단 0건 (Layer A §1.4 답습 — 5 영구 핵심 제약 보존 5/5) | ✅ |

→ **Provider Liquidity 5-way 보존 4/4 충족** (facade real 본문 = Backlog #4 분리 명시 의무).

### 1.5 검토 기준 #5 — Secret handling 정책 변경 여부

| 영역 | 정책 변경 여부 | 충족 |
|------|------------|------|
| **R-4.1 Tier-1 45 patterns** | 변경 0건 (Group D 답습 그대로 — Prefix 36 + regex 7 + alternation 2) | ✅ |
| **Tier-2 / Tier-3 catalog 자동 확장** | 0건 (Tier-1 한정 — 별도 합의 영역) | ✅ |
| **Docker secret 도입** | ADR-008 차단조건 #6 (Docker 격리) 답습 (정책 변경 0건) — entrypoint stat / inotify watch (ST-1 / ST-2) = 1.5차 보강 영역 분리 (37번째 entry R-S1 정정 답습) | ✅ |
| **`pull_request_target` workflow** | 미도입 (G3-7 row 분리 영역 답습 — T2/T3 별도 합의) | ✅ |
| **Vault HSM ST-4** | Operational Readiness 분리 (T3 영역 — Backlog #7) — 정책 변경 0건 | ✅ |
| **외부 LLM 자동 호출 / 실 API key / provider SDK 호출** | 0건 (본 합의 = 시작 권한 발효 *적격성* 한정) | ✅ |

→ **Secret handling 정책 변경 0/6 — 변경 0건 충족**.

### 1.6 검토 기준 #6 — CI / hook 구현 범위 T2 / T3 분류 (ADR-011 §2.4 답습)

| 영역 | T1 / T2 / T3 | 본 합의 영역 | 충족 |
|------|-------------|----------|------|
| **CI workflow step (GP-3 + GP-5)** | T2 | ✅ 본 합의 영역 (사용자 명시 기반) | ✅ |
| **Pre-commit hook (CI-only PC-3)** | T2 | ✅ 본 합의 영역 | ✅ |
| **PR auto-reject (CI step AR-1)** | T2 | ✅ 본 합의 영역 | ✅ |
| **local pre-commit framework (PC-4)** | T2 | ❌ Backlog #1 + #2 1.5차 보강 분리 | ✅ (분리 명시) |
| **Branch protection (AR-2)** | T3 | ❌ Backlog #3 T3 영역 별도 풀 3+1 분리 | ✅ (분리 명시) |
| **Vault HSM (ST-4)** | T3 | ❌ Operational Readiness 분리 | ✅ (분리 명시) |
| **Auto revoke (provider key 자동 비활성화)** | T3 | ❌ Backlog #3 분리 | ✅ (분리 명시) |
| **Tier-2 / Tier-3 catalog 확장** | T3 | ❌ 별도 합의 영역 | ✅ (분리 명시) |

→ **본 합의 영역 = T2 한정 (3/3) — T3 영역 5/5 모두 분리 명시 + T3 영역 침범 0건 충족**.

### 1.7 검토 기준 #7 — Rollback Trigger 정의 가능 여부

| GP | Rollback Trigger 본문 확정 가능성 | 충족 |
|----|-----------------------------|------|
| **GP-3 8개** | MVP-1 roadmap §3.5 답습 — 8개 모두 본문 확정 가능: (1) S-1 FP_rate 폭증 (>5%) / (2) S-2 gitleaks 라이선스 변경 또는 maintenance 중단 / (3) ST-3 Docker secret 도입 실패 / (4) PC-3 CI runtime 폭증 (>2분) / (5) AR-1 hook 우회 시도 패턴 검출 / (6) R-4.1 Tier-1 catalog 변경 / (7) Tier-2 확장 필요 (1.5차 보강 trigger) / (8) Operational Readiness parity 필요 trigger | ✅ |
| **GP-5 10개** | MVP-1 roadmap §4.5 답습 — 10개 모두 본문 확정 가능: (1) T-2 FP_rate 폭증 / (2) T-5 단독 FN 폭증 / (3) T-6 병행 충돌 (T-2 ↔ T-5 결과 불일치) / (4) `.importlinter` rule 충돌 (TR-1~TR-5 갈등) / (5) PC-3 hook 우회 시도 / (6) AR-1 fail-closed 폭증 / (7) P1 v2 facade real 본문 필요 (Backlog #4 trigger) / (8) branch protection 필요 (T3 trigger) / (9) 의미적 lock-in 검출 (MVP-3 trigger) / (10) Layer 2 runtime 진입 필요 trigger | ✅ |
| **발화 시연** | Layer C 발효 시점 영역 (본 합의 = 본문 확정 한정, 발화 시연 = 별도 영역) | ✅ |

→ **18/18 Rollback Trigger 본문 확정 가능 충족**.

### 1.8 검토 기준 #8 — Evidence Artifact 요구사항

| Evidence | 요구 형태 (Layer C 발효 시점 의무 명문 cross-reference) | 충족 |
|----------|--------------------------------------------|------|
| **GP-3 (a) Implementation Evidence** | `tools/secret_scanner.py` 확장 + `.github/workflows/secret-hygiene-egress-redaction.yml` 확장 + 실행 log + actual run SUCCESS URL + 코드 diff + 4 patterns cover (alternation/prefix-baseline/regex/private-key T1-035) | ✅ |
| **GP-3 (b) Rollback Evidence** | 8 rollback trigger 발화 시연 fixture + rollback artifact (CI run + summary.json + 30일 retention) | ✅ |
| **GP-5 (a) Implementation Evidence** | `tools/provider_import_scanner.py` + `tools/provider_url_scanner.py` 확장 + `.importlinter` 본문 + `.github/workflows/provider-*.yml` + 실행 log + actual run SUCCESS URL + 5-vendor + URL Tier-1 10 + Model Tier-1 19 cover | ✅ |
| **GP-5 (b) Rollback Evidence** | 10 rollback trigger 발화 시연 fixture + rollback artifact | ✅ |
| **양 GP (c) Independent Verification** | Reviewer-only 단축 또는 풀 3+1 합의 보고서 (Layer C 시점, ADR-010 + ADR-009 답습) | ✅ |
| **양 GP (d) Permanent Constraint Preservation** | 5 영구 핵심 제약 보존 검증 본문 (각 합의 §1.7 답습) + Provider Liquidity 5-way + Hermes ≠ root of trust + 메타포 강제 금지 + T3 분리 + 수단/목적 분리 | ✅ |
| **양 GP (e) No Auto-Promotion** | Layer C 발효 후에도 MVP-1 PASS / Operational Readiness PASS / Hermes PMO 격상 0건 유지 evidence (Layer D/E/F 별도 합의) | ✅ |

→ **7 evidence 요구 형태 본문 확정 + Layer C 시점 evidence 의무 명문 cross-reference 7/7 충족**.

### 1.9 8 검토 기준 종합 매트릭스

| # | 기준 | 평가 |
|---|------|------|
| 1 | GP-3 구현 진입 기준 | ✅ 충족 (§1.1 — 5/5) |
| 2 | GP-5 구현 진입 기준 | ✅ 충족 (§1.2 — 5/5) |
| 3 | 채택 수단 후보의 lock-in 위험 | ✅ 충족 (§1.3 — 7/7) |
| 4 | Provider Liquidity 보존 여부 | ✅ 충족 (§1.4 — 4/4) |
| 5 | Secret handling 정책 변경 여부 | ✅ 충족 (§1.5 — 0/6 변경, 변경 0건) |
| 6 | CI / hook 구현 범위 T2 / T3 분류 | ✅ 충족 (§1.6 — T2 한정 3/3 + T3 분리 5/5) |
| 7 | Rollback Trigger 정의 가능 여부 | ✅ 충족 (§1.7 — 18/18 본문 확정 가능) |
| 8 | Evidence Artifact 요구사항 | ✅ 충족 (§1.8 — 7/7) |

**합산: 8/8 검토 기준 모두 충족** → 본 합의 = APPROVE 적격.

---

## 2. 6 풀 3+1 승격 트리거 검증 (brief §4.2 답습)

| # | 트리거 | 본 검토 | 발화 |
|---|----|----|----|
| 1 | **Runtime code 구현 범위 예상 초과** | §1.1 + §1.2 답습 — 본 합의 영역 = GP-3 (A1)+(A2) + GP-5 (B1)+(B2) 한정. G3-7 (iii)(`pull_request_target`) 자동 진입 0건 / Layer 2 runtime block (G5-5) 자동 진입 0건 / 의미적 lock-in (G4 §4.6) 자동 진입 0건. 모두 분리 영역 명시 | ❌ 0 |
| 2 | **CI / hook 구현 T3 영역 침범** | §1.6 답습 — 본 합의 영역 = T2 한정 (CI workflow step + PC-3 CI-only + AR-1 CI step). T3 영역 5/5 (AR-2 branch protection / Vault HSM ST-4 / Auto revoke / Tier-2/3 catalog 확장 / `pull_request_target`) 모두 분리 명시 + 침범 0건 | ❌ 0 |
| 3 | **Provider Liquidity 약화 가능성** | §1.4 답습 — T-6 (T-2 + T-5) = facade single entry 강제 = Provider Liquidity 5-way Layer 1 모법 답습 변경 0건. 5-vendor 동등 차단 답습. facade real 본문 = Backlog #4 분리 명시. 약화 0건 | ❌ 0 |
| 4 | **Secret handling 정책 변경 필요** | §1.5 답습 — 정책 변경 0건 (R-4.1 Tier-1 45 patterns / Tier-2/3 catalog / Docker secret / `pull_request_target` / Vault HSM / 외부 LLM 호출 모두 변경 0건 또는 분리 명시) | ❌ 0 |
| 5 | **Evidence PASS vs Operational Readiness PASS 구분 모호** | §0.4 + §1.8 + §5.2 답습 — 6-layer 분리 매트릭스 답습 (Layer A 답습 한 layer 하위). 본 합의 = Layer B 한정. Layer C (Implementation Evidence PASS) / Layer D (MVP-1 PASS) / Layer E (Operational Readiness PASS) / Layer F (Hermes PMO 격상) 모두 본 합의 권위 외 명시. 모호 0건 | ❌ 0 |
| 6 | **Rollback trigger 불명확** | §1.7 답습 — 18 trigger (GP-3 8 + GP-5 10) 모두 본문 확정 가능 (MVP-1 roadmap §3.5 + §4.5 답습). 발화 조건 명확 + 본문 확정 가능. 불명확 0건 | ❌ 0 |

→ **6/6 트리거 0건 발화** → **단축 합의 (Reviewer-only) 적격** 확정.

---

## 3. 7 Backlog Blocker / 후속 분리 매트릭스 (Layer A §3 답습 + Layer B 영역 추가 deepening)

본 §은 Layer A §3 매트릭스의 *Layer B 영역 deepening* — 각 backlog 항목이 *Layer B 발효 후 어느 단계* 에 처리 적격한지 명시 (Layer B 자동 진입 vs 분리):

| # | Backlog | blocker / 후속 / 본 합의 영역 | 처리 시점 (Layer B 발효 후) | 합의 형태 |
|---|------|----|----|----|
| 1 | GP-3 1.5차 보강 (S-3 detect-secrets / ST-2 inotify / PC-4 framework / AR-3 통합) | **후속** | Layer B 발효 후 → Layer C 진입 *전* 또는 *후* (사용자 명시 결정) — Defense in depth 보강 영역 | 풀 3+1 + 외부 LLM 1+ (수단별) 또는 단축 (PC-4 한정) |
| 2 | GP-5 1.5차 보강 (T-1 / T-3 / T-4 / T-5 단독 / PC-4 / AR-3) | **후속** | 동상 | 풀 3+1 + 외부 LLM 1+ (수단별) 또는 단축 (PC-4 한정) |
| 3 | T3 영역 별도 풀 3+1 (AR-2 / Vault HSM ST-4 / Tier-2/3 catalog) | **후속** | T3 영역 진입 시점 (T3 정책 변경 결정 시) — Operational Readiness 단계 일부 (Vault HSM) | 풀 3+1 + 외부 LLM 1+ + 사용자 명시 |
| 4 | P1 v2 facade MVP 합의 (G5-4) | **후속** | P1 v2 facade MVP 진입 시점 (사용자 명시 결정 시) — Group A 2차 §8 TR-1 답습 (facade real 본문 작성 = T-2 룰 ignore_imports 검증 재합의 trigger) | 별도 P1 v2 facade MVP 합의 |
| 5 | ADR-012 §2.2 evidence enum 정식 등록 (4 + 3 = 7 enum 후보) | **후속** | Layer C 발효 시점 권고 (Implementation Evidence PASS 발효 시점 — enum 정식 등록 의무) | G4 §10.2 schema 진화 정책 별도 합의 |
| 6 | **Runtime enforcement / CI-hook implementation** | **본 합의 영역 (Layer B)** + 후속 Layer C | Layer A 발효 (`f1e0b23`) → **Layer B 발효 (본 합의)** → 사용자 명시 결정 → runtime code / CI workflow / hook 구현 시작 → Layer C 발효 (Implementation Evidence PASS) | Layer B = 본 합의 (단축 Reviewer-only) / Layer C = 별도 합의 + ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 |
| 7 | Operational Readiness parity check (Multi-environment + Vault HSM ST-4) | **후속** | MVP-6 영역 (Multi-host 전환 + Vault HSM ST-4 도입) — Operational Readiness PASS 발효 시점 | 별도 합의 (MVP-6 영역, ADR-010 답습) |

**Blocker 합산: 0/7** (Layer B 발효 차단 사유 0건 — 본 합의 = APPROVE 적격 확정).
**후속 합산: 6/7** (모두 Layer B 발효 후 단계적 처리 영역).
**본 합의 영역 합산: 1/7** (Backlog #6 Layer B = 본 합의 영역).

### 3.1 Layer B 발효 후 처리 우선순위 권고 (사용자 결정 영역 — Layer B APPROVE 後 *자동 진입 금지* 강조 답습)

| 권고 우선순위 | 다음 단계 | 영역 | 주의 |
|----|------|------|----|
| **1** | **사용자 명시 결정 → 9 sub-수단 본문 채택 commit + CI workflow 신설 + runtime code 작성 진입** (Layer B 발효 결과 행사) | runtime code / CI workflow / hook 구현 시작 권한 행사 | **Layer B APPROVE 직후 자동 진입 금지** — 사용자 명시 결정 의무 (사용자 명시 답습) |
| 2 | (#1) GP-3 1.5차 보강 또는 (#2) GP-5 1.5차 보강 | Defense in depth — Layer C 진입 *전* 또는 *후* 사용자 명시 | Backlog #1 또는 Backlog #2 |
| 3 | (#4) P1 v2 facade MVP 합의 | G5-4 영역 — facade real 본문 작성 진입 시 | Backlog #4 |
| 4 | (#5) ADR-012 evidence enum 정식 등록 | Layer C 발효 시점 권고 | Backlog #5 |
| 5 | (#3) T3 영역 별도 풀 3+1 | T3 정책 변경 결정 시 | Backlog #3 |
| 6 | (#7) Operational Readiness parity check | MVP-6 영역 (Layer E 발효 시점) | Backlog #7 |
| — | **Layer C 진입** (Implementation Evidence PASS 발효 합의) | Layer C — runtime code 작성 완료 + actual run SUCCESS + evidence 5/5 충족 후 | 별도 합의 + ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 (단축 또는 풀 3+1 + 외부 LLM 1+) |

본 권고 = *권고 한정* — 사용자 명시 결정 영역 (본 합의 §5.3 답습).

---

## 4. 메타 편향 자기진단

### 4.1 본 검토자의 컨텍스트 한계

본 Reviewer = Claude Opus 4.7 메인 컨텍스트 = MVP-1 roadmap 작성자 + GP-3 / GP-5 / MVP-1 Implementation Entry / Backlog #6 Layer A 합의 보고서 작성자 + brief v1 → v2 → 본 brief 작성자 + 본 합의 보고서 작성자. 자기 작성 권위 누적 자기 검토 한계 인지.

### 4.2 본 한계의 청산

| # | 청산 원칙 | 본 검토 적용 |
|---|-------|--------|
| 1 | 사후 외부 LLM 충족 | 본 합의 답습 출처 모두 cross-vendor 외부 LLM 합산 4건 권위 *내부* 작업 + 외부 LLM 응답 line 242 (MVP-1 정의) + C-7 line 378 (4 입력 만장일치) + Group A 2차 풀 3+1 합의 답습 |
| 2 | 격상 전 면제 | Hermes PMO 격상 *전* — 본 검토 = Layer B *시작 권한 발효* 한정 |
| 3 | 합의 권위 내부 변경 | 본 검토 = Layer A 합의 + brief 답습 = *권위 내부* 작업 (Layer A → Layer B 단계 답습) |
| 4 | 자기 작성 한계 명시 | 본 §0.3 + §4 명시 |
| 5 | Layer B *시작 권한 발효* 한정 | 본 합의 = *Layer B 시작 권한 발효 적격성* — runtime code / CI workflow / hook 구현 / 9 sub-수단 본문 채택 commit / Layer C 발효 모두 본 합의 발효 *후* 사용자 명시 결정 영역 |
| 6 | 누적 권위 검증 | 본 검토 = 14 commits push 완료 후 진입 (origin 동기화 검증 — `ca7b24e` 답습) |
| 7 | brief 옵션 (A) 그대로 승인 답습 | 본 합의 = brief §1~§4 + 6 트리거 + 4 판정 옵션 + 9 금지 사항 그대로 채택 (사용자 변경 0건) |
| 8 | Layer B APPROVE 후 자동 구현 진입 금지 답습 | 사용자 명시 (§0.1 답습) — 본 §5.3 + §5.4 답습 |

### 4.3 5 통제 답습

| # | 통제 | 본 검토 |
|---|-----|--------|
| 1 | 사용자 명시 절차 답습 | ✅ 사용자 명시 brief 옵션 (A) + 8 검토 기준 + 4 판정 옵션 + 6 트리거 + 9 금지 사항 + 합의 형태 + 산출 경로 + Layer B APPROVE 후 자동 진입 금지 모두 §0 + §1 + §2 + §3 + §5 답습 |
| 2 | R-7 SOP §0 핵심 선언 답습 | ✅ §0.4 비검토 대상 + §1 8 평가 + §2 6 트리거 + §3 7 backlog 분리 |
| 3 | ADR-011 §2.4 T1/T2/T3 답습 | ✅ §1.6 (T2 한정 + T3 영역 5/5 분리 명시) + §1.5 (정책 변경 0건) + §1.7 (Rollback Trigger 본문 확정) |
| 4 | 수단/목적 분리 원칙 답습 | ✅ §1.4 (Provider Liquidity 5-way 모법 답습) + §1.3 (9 sub-수단 lock-in 0건) + 본 합의 = (b) Rollback Evidence 본문 + (e) No Auto-Promotion 명시 (Layer C 시점 (a)~(e) 5/5 별도 합의) |
| 5 | 본 합의가 *하지 않는* 것 명시 (§0.4 + §5.2) | ✅ 명시 |

### 4.4 본 단축 합의가 *하지 않는* 것

§5.2 답습.

---

## 5. 결론

```
✅ APPROVE — Backlog #6 Layer B Implementation Entry 합의 발효 가능
   (단축 합의, Reviewer-only)
   — runtime code / CI workflow / hook 구현 시작 권한 발효 (시작 권한 발효 적격성)
   — 9 sub-수단 권고 → 본문 채택 격상 적격
   — 8/8 검토 기준 모두 충족
   — 6/6 풀 3+1 승격 트리거 0건 발화 → 단축 합의 적격 확정
   — 7 backlog 모두 분리 (blocker 0/7 + 후속 6/7 + 본 합의 영역 1/7)
   — 12/12 위반 0건 (사용자 명시 9 + 본 합의 추가 3 금지 사항 모두 준수)
   — 다음 단계 = 사용자 명시 결정 → runtime code / CI workflow / hook 구현 진입 (Layer B 결과 행사) → Layer C 진입 적격 (별도 합의 영역)

   ⚠️  Layer B APPROVE 직후 자동 구현 진입 금지 — 사용자 명시 결정 의무
```

본 결론은 **Backlog #6 Runtime Enforcement / CI-hook Implementation Entry *시작 권한 발효 적격성 권위 권고 발행*** 한정 (Layer B). **본 합의는 runtime code *실 구현* / CI workflow *실 신설* / hook *실 구현* / 9 sub-수단 *본문 채택 commit* / Implementation Evidence PASS *발효* (Layer C) / MVP-1 PASS 선언 / Operational Readiness PASS / Hermes PMO 격상 / 7 backlog 자동 진입 / GP-3 / GP-5 / MVP-1 Implementation Entry / Layer A 진입 합의 자체 변경 / ADR 본문 자동 갱신 모두 *불가***.

### 5.1 본 합의가 *발생시키는* 것

- ✅ **Backlog #6 Runtime Enforcement / CI-hook Implementation Entry *시작 권한 발효 적격성 권위 권고 발행*** (Layer B)
- ✅ 9 sub-수단 권고 → *본문 채택 격상 적격성* 권위 권고 (GP-3 S-1 + ST-3 + PC-3 + AR-1 + GP-5 T-6 (T-2 + T-5) + PC-3 + AR-1 + `.importlinter` 본문 + G3-7 row 4 항목)
- ✅ 18 Rollback Trigger 본문 확정 가능성 권위 권고 (GP-3 8 + GP-5 10)
- ✅ 7 evidence 요구 형태 본문 확정 권위 권고 (Layer C 시점 evidence 의무 명문 cross-reference)
- ✅ T2 한정 / T3 분리 명시 매트릭스 권위 권고 (T2 3/3 + T3 5/5 분리)
- ✅ Provider Liquidity 5-way 보존 검증 권위 권고 (4/4 충족)
- ✅ Secret handling 정책 변경 0건 검증 권위 권고 (0/6 변경)
- ✅ 7 backlog blocker vs 후속 분리 매트릭스 권위 권고 (blocker 0/7 + 후속 6/7 + 본 합의 영역 1/7)
- ✅ Layer B 발효 후 사용자 명시 결정 의무 명시 + 자동 진입 금지 명시
- ✅ 본 합의의 *다음 단계* (사용자 명시 결정 → 구현 진입 → Layer C 발효 합의) 진입 *적격성* 권위 권고
- ✅ 8 검토 기준 모두 충족 + 6 트리거 0/6 발화 + 12/12 위반 0건 = 단축 합의 (Reviewer-only) 적격 확정

### 5.2 본 합의가 *발생시키지 않는* 것 (사용자 명시 답습 — 옵션 (A) brief 그대로 승인 답습)

- ❌ **runtime code 실 구현** (Layer B 발효 후 사용자 명시 결정 의무 영역)
- ❌ **CI workflow 실 신설 / hook 실 구현** (동상)
- ❌ **9 sub-수단 본문 채택 commit** (동상 — Layer B 발효 후 별도 commit 영역)
- ❌ **Implementation Evidence PASS *발효*** (Layer C — Layer B 종료 후 별도 합의 영역)
- ❌ MVP-1 PASS *선언* (Layer D)
- ❌ Operational Readiness PASS *선언* (Layer E)
- ❌ Hermes PMO 격상 *선언* (Layer F)
- ❌ 7 backlog 자동 진입 (1.5차 보강 / T3 / P1 v2 facade / ADR-012 enum / Operational Readiness — 모두 별도 합의 영역)
- ❌ GP-3 / GP-5 / MVP-1 Implementation Entry / Layer A 진입 합의 자체 변경 (재합의 0건 — 각 합의 권위 답습 한정)
- ❌ ADR 본문 자동 갱신 (cross-reference 답습 한정 — ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012 본문 변경 0건)
- ❌ Tier-2 / Tier-3 catalog 자동 확장 (Tier-1 답습 한정)
- ❌ threshold *고정* (FP/FN/latency 모두 *후보 한정*)
- ❌ 신규 ADR / 신규 P / 신규 GP 발행
- ❌ ADR-012 §2.2 `event` enum 정식 등록 (4 + 3 = 7 enum *후보 한정* + Layer C 시점 정식 등록 권고)
- ❌ 외부 LLM 자동 호출
- ❌ 실 API key / provider SDK / 외부 API 호출
- ❌ **Layer B APPROVE 직후 자동 구현 진입** (사용자 명시 결정 의무 — §5.3 + §5.4 답습)
- ❌ MVP-2 ~ MVP-6 본문 deepening (별도 합의 영역)

### 5.3 Layer B APPROVE 직후 자동 구현 진입 금지 (사용자 명시 강조 답습)

사용자 명시 (옵션 (A) 결정 답습):

> "Layer B가 APPROVE되더라도, 바로 구현을 자동 시작하지 말고 사용자 명시 결정 후 다음 단계로 넘어가세요. 즉: Layer B 합의 APPROVE → 사용자 확인 → runtime code / CI workflow / hook 구현 착수 여부 별도 결정"

본 합의 결과 = **Layer B 합의 발효 (APPROVE) — *시작 권한 발효 적격성 권위 권고***. **합의 발효 직후 자동 구현 진입 0건** — 다음 단계는 **반드시 사용자 명시 결정 후** 진입.

3-step 명시 답습:
```
1. Layer B 합의 APPROVE 발효 (본 합의 — 시작 권한 발효 적격성 권위)
   │
   ▼
2. 사용자 확인 / 명시 결정
   │  (runtime code / CI workflow / hook 구현 착수 여부 별도 결정)
   │  (다른 backlog 우선 결정 가능 / 세션 종료 가능 / Layer C 직진 가능)
   │
   ▼
3. 사용자 명시 결정 후에만 다음 단계 진입
   (9 sub-수단 본문 채택 commit + runtime code 작성 + CI workflow 신설 + hook 구현)
```

### 5.4 다음 진입점 (사용자 결정 영역 — 자동 진입 0건 강조)

본 합의 APPROVE → Backlog #6 Layer B *시작 권한 발효 적격성 권위 권고 발효* → 다음 작업 (사용자 결정 영역, 본 §3.1 권고 우선순위 답습):

| 후보 | 영역 | Layer | 합의 형태 |
|------|------|-------|---------|
| **(1)** | **9 sub-수단 본문 채택 commit + runtime code / CI workflow / hook 구현 진입** (Layer B 발효 결과 행사) | Layer B 발효 결과 행사 → Layer C 진입 준비 | 별도 단계 (구현 commit 분리) |
| **(2)** | **Layer B 발효 메타 갱신 commit** (CONTEXT / INDEX / SESSION) — 본 합의 발효 기록 | Layer B 메타 | 별도 commit (사용자 명시 답습) |
| **(3)** | **GP-3 1.5차 보강 합의** (S-3 / ST-2 / PC-4 / AR-3) — Backlog #1 | 후속 (Layer C 전 또는 후) | 풀 3+1 + 외부 LLM 1+ (수단별) 또는 단축 (PC-4 한정) |
| **(4)** | **GP-5 1.5차 보강 합의** (T-1 / T-3 / T-4 / T-5 단독 / PC-4 / AR-3) — Backlog #2 | 후속 (Layer C 전 또는 후) | 풀 3+1 + 외부 LLM 1+ (수단별) 또는 단축 (PC-4 한정) |
| **(5)** | **P1 v2 facade MVP 합의** (G5-4) — Backlog #4 | 후속 | 별도 P1 v2 facade MVP 합의 영역 |
| **(6)** | **ADR-012 evidence enum 정식 등록** (7 enum 후보) — Backlog #5 | 후속 (Layer C 시점 권고) | G4 §10.2 schema 진화 정책 별도 합의 |
| **(7)** | **T3 영역 별도 풀 3+1** (AR-2 / Vault HSM / Tier-2/3) — Backlog #3 | 후속 | 풀 3+1 + 외부 LLM 1+ + 사용자 명시 |
| **(8)** | **Operational Readiness parity check** — Backlog #7 | 후속 (Layer E, MVP-6) | MVP-6 영역 (Multi-host + Vault HSM ST-4) |
| **(9)** | **세션 종료 후 다음 세션에서 결정** | — | 다음 세션 사용자 명시 결정 영역 |

**권고 시작 명령** (사용자 권한 영역, 본 §3.1 우선순위 답습):

- **"Layer B 발효 메타 갱신 (CONTEXT / INDEX / SESSION) 진입"** — 권고 우선순위 1 (본 합의 발효 직후 표준 단계)
- **"9 sub-수단 본문 채택 commit 진입"** — 메타 갱신 후 사용자 명시
- **"runtime code / CI workflow / hook 구현 진입"** — 사용자 명시 결정 영역
- **"다른 backlog 우선 진입"** — 사용자 명시 결정 영역
- **"세션 종료"** — 사용자 명시 결정 영역

본 합의 자체 = **Backlog #6 Runtime Enforcement / CI-hook Implementation Entry *시작 권한 발효 적격성 권위 권고 발행* (Layer B) + 9 sub-수단 본문 채택 격상 적격성 권위 권고 + 18 Rollback Trigger 본문 확정 권위 권고 + T2 한정 / T3 분리 매트릭스 권위 권고 + 7 backlog 분리 매트릭스 + Layer B 발효 후 자동 진입 금지 명시 + Layer C (Implementation Evidence PASS) 진입 *적격성 경로* 권위 권고**. 다음 진입 결정 = **사용자 명시 결정 영역** (자동 진입 0건).

---

**합의 commit 권위**: 본 commit (`docs(review): record Backlog 6 implementation entry consensus`)
**본 commit + 직전 14 commits 합산 (`cddd22f` MVP-1 roadmap 본문 + `6c91980` references + `95be2e5` MVP-1 roadmap 단축 합의 + `6dc5bdc` GP-3 진입 합의 + `bbc05ca` G3-7 row + `ed1b6d6` GP-3 condition absorption + `6808d17` GP-5 진입 합의 + `5939c93` §5.4 신설 + `f234f97` integrated risk absorption + `1e90d7b` 상태 정리 + `99018c1` condition status summary + `1eab814` MVP-1 Implementation Entry 최종 합의 + `df20b15` MVP-1 readiness CONTEXT + `f1e0b23` Backlog #6 Layer A 합의 + `ca7b24e` Layer A status 메타 갱신) = Backlog #6 Layer B *시작 권한 발효* 단계 완료**
**다음 세션 진입점**: 사용자 결정 영역 — Layer B 발효 메타 갱신 / 9 sub-수단 본문 채택 / runtime code 구현 진입 / 7 backlog 中 사용자 명시 결정 영역 / 세션 종료

---

⚠️ **Layer B APPROVE 직후 자동 구현 진입 금지** — 사용자 명시 결정 의무 (§5.3 답습).
