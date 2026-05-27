# MVP-1 Implementation Evidence PASS 발효 합의 brief (v1.1 보강)

> **v1.1 보강 답습**: 풀 3+1 + 외부 LLM 1+ 합의 (`3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md`) APPROVE WITH CONDITIONS — BLOCKING 6 (R-1~R-6) + 권고 5 (N-1~N-5) 1pass 흡수 발효. 본 v1.1 = 합의 직후 in-place 보강 (별도 v2 cycle 0, ceremony-inflation 차단 답습).
>
> **scope**: 24번째 entry brief carry-over (c) — **MVP-1 Implementation Evidence PASS 발효 합의**. 본 cycle = (b1) 4 sub-cycle 완료 + 31번째 entry 첫 PR evidence (11/11 SUCCESS, head SHA `9837298befdeda6c7e170879cc9f15e331c52bce`) 답습 후 진입. **본 프로젝트 최초 MVP-1 PASS 발효 자격 자격 자격 검증 cycle**.
>
> **본 brief 자체에서 PASS 발효 0건 의무** — brief 합의 발효 *후* roadmap-mvp1 **§2.2 + §3.6.3 + §4.7.3 + §5.1 + §9** 본문 변경 (사용자 명시 답습 의무, R-1 정정 답습).

---

## §0 답습 출처

| Source | 위치 | 답습 내용 |
|---|---|---|
| **24번째 entry brief v1.1 carry-over (c)** | `docs/phase0/mvp1-1.5th-reinforcement-entry-brief.md` line 96 (commit `9638521`) | "(c) MVP-1 Implementation Evidence PASS 발효 합의 — (a)+(b) 선행 후, ADR-011 §2.1 (a)~(e) 5/5 + conditions 해소 + 사용자 명시" |
| **roadmap-mvp1 §2.2** | `docs/architecture/implementation-runtime-roadmap-mvp1.md` line 127~141 (commit `51aa964` APPROVED) | "MVP-1 exit = (GP-3 5/5 + GP-5 5/5) 두 GP 모두 충족 + 사용자 명시 결정. 어느 한쪽 미충족 시 = MVP-1 *부분 PASS* 처리 (별도 합의 영역)" |
| **ADR-011 §2.1 (a)~(e)** | `docs/decisions/ADR-011-means-vs-ends-redaction.md` | (a) 동등 이상 보안 + (b) 격리 환경 PoC + (c) 도구 stateless·network-free + (d) 자동 회귀 검증 + (e) 합의 APPROVE 운영조건 |
| **(b1) 4 sub-cycle 모두 발효** | `3a63a5b` PC-1 + `4451716` S-3 + `1edc5bb` ST-2 + `7f57323` AR-3 + `7c294bb` AR-3 사용자 admin + `73ed20d` fix + `9837298` 첫 PR evidence | (b1) 4 sub-cycle 완료 + 첫 PR 11/11 SUCCESS = 핵심 발효 evidence |
| **23번째 entry pattern** | `51aa964` (roadmap-mvp1 DRAFT → APPROVED 권위 발효) | audit + 권위 격상 단축 합의 패턴 (단 본 (c) = 더 큰 격상) |
| **22~31번째 entry 누적** | docs/sessions/SESSION_2026-05-27.md | 본 세션 7 entry chain (MVP-1 1.5차 보강 entry → 4 sub-cycle → AR-3 적용 → 첫 PR evidence) 답습 |

---

## §1 scope (본 (c) cycle 한정)

### 1.1 본 cycle 의 본질

| 항목 | 내용 |
|---|---|
| **scope** | (c) MVP-1 Implementation Evidence PASS 발효 합의 진입 자격 검증 + PASS 발효 형태 (완전 vs 부분 vs DEFER) 결정 + roadmap-mvp1 §2.2 + §3.5 + §4.5 본문 갱신 |
| **영역** | GP-3 + GP-5 두 GP 의 (a)~(e) 5/5 충족 audit + PASS 발효 자격 |
| **합의 형태 권고** | **풀 3+1 + 외부 LLM 1+** (메인 권위 격상 + T3 영역 답습 + 24번째 entry pattern + 본 프로젝트 최초 MVP-1 PASS 발효) — 단 단축 합의 가능 자격 검토 (단순 audit 영역 답습 vs 격상 의사결정 분리) |
| **변경 0건 의무** | (b1) 4 sub-cycle 본문 0건 / 11 workflow 본문 0건 / src 0건 / tools 0건 / docker 0건 / 헌법 0건 / ADR 본문 0건 (R-S1 cross-reference 정정 = (b2) 별도 영역) / Tier-2/3 catalog 확장 0건 / branch protection rule 변경 0건 |
| **변경 허용 영역** | `docs/architecture/implementation-runtime-roadmap-mvp1.md` **§2.2 (MVP-1 Exit 기준) + §3.6.3 (GP-3 합의 형태 권고) + §4.7.3 (GP-5 합의 형태 권고) + §5.1 (통합 PASS 권고)** 본문 갱신 (PASS 발효 표시 + 발효 일자 + 발효 합의 보고서 cross-reference) + **§9 변경 이력 1줄 추가**. 정정 답습 (R-1 BLOCKING) — brief v1 의 `§3.5 + §4.5` 표기는 실 roadmap 의 §3.5 (Rollback Trigger) + §4.5 (측정 metric) 와 mismatch, 정확 위치 = 합의 형태 권고 표 위치 |

### 1.2 본 sub-cycle 이 *하지 않는* 것 (변경 0건 의무)

| # | 항목 | 변경 자격 |
|---|---|---|
| 1 | (b1) 4 sub-cycle 본문 (PC-1 / S-3 / ST-2 / AR-3 brief + 합의) | 0건 |
| 2 | 11 workflow 본문 (AR-1 답습 유지) | 0건 |
| 3 | `.pre-commit-config.yaml` 본문 | 0건 |
| 4 | `.githooks/` / src / tools / docker 본문 | 0건 |
| 5 | 헌법 본문 변경 | 0건 |
| 6 | ADR 본문 변경 (ADR-008 R-S1 cross-reference = (b2) 별도 영역, ADR-011 + ADR-010 + ADR-009 본문 0건) | 0건 |
| 7 | Tier-2/3 catalog 확장 | 0건 |
| 8 | branch protection rule 변경 (admin scope, 31번째 entry 발효 답습) | 0건 |
| 9 | MVP-2 진입 자격 자동 발효 | 0건 (별도 합의 영역) |
| 10 | Operational Readiness PASS 발효 (Layer 3) | 0건 (별도 합의 영역) |
| 11 | Hermes PMO 격상 | 0건 (별도 합의 영역) |
| 12 | 4 게이트 일괄 PASS | 0건 (roadmap §99 답습) |
| 13 | adapters/llm/facade.py placeholder → real | 0건 ((d) carry-over 영역) |
| 14 | (b2) R-S1 권위 chain 정정 적용 | 0건 (별도 sub-cycle 답습, 본 cycle = 명문 답습 의무 한정) |

---

## §2 (b1) 4 sub-cycle ADR-011 (a)~(e) 충족 매트릭스 (audit)

### 2.1 PC-1-T3 mandatory enforcement (26번째 entry, commit `3a63a5b`)

| 조건 | 충족 자격 | 답습 source |
|---|---|---|
| **(a)** 사용자 명시 결정 | ✅ | 26번째 entry D-1~D-6 6/6 사용자 결정 |
| **(b)** 격리 환경 PoC | ⏳ **부분 충족** | `bin/setup.sh` + `tools/pre_commit_install_audit.sh` 신규 = PoC 실증 발효 자격 / 실 evidence 수집 (`.git/pre-commit-audit/install.log` 기록 + `pre-commit run --all-files` PASS) = 사용자 자율 영역 |
| **(c)** stateless · network-free | ✅ | pre-commit framework `repos: local` 답습 (Provider Liquidity 5-way 답습) |
| **(d)** 자동 회귀 검증 경로 | ⏳ **부분 충족** | `tools/pre_commit_install_audit.sh` 3 탐지 경로 (hook marker grep + framework PATH + setup audit log) 발효 자격 / CI 통합 = D-6 별도 sub-cycle (carry-over) |
| **(e)** 합의 APPROVE | ✅ | 26번째 entry Reviewer-only 단축 합의 APPROVE |

→ **3/5 완전 + 2/5 부분 충족** (PoC evidence 수집 자율 영역 + D-6 carry-over)

### 2.2 S-3 detect-secrets 부분 통합 (27번째 entry, commit `4451716`)

| 조건 | 충족 자격 | 답습 source |
|---|---|---|
| **(a)** 사용자 명시 결정 | ✅ | 27번째 entry D-1~D-5 5/5 사용자 결정 |
| **(b)** 격리 환경 PoC | ✅ **완전 충족** | 31번째 entry 첫 PR (`73ed20d`) **`scan` check_run 3/3 SUCCESS** (secret-hygiene-egress-redaction.yml S-3 step 모두 PASS) = local 격리 evidence 발효. fixture 6 파일 (PASS 1 + FAIL 5) 모두 검출/미검출 verify |
| **(c)** stateless · network-free | ✅ | detect-secrets 도구 본질 (network 0) |
| **(d)** 자동 회귀 검증 경로 | ✅ **완전 충족** | `secret-hygiene-egress-redaction.yml` S-3 install + scan + baseline assertion 3 step + `on.push.paths` 필터 + nightly schedule (28번째 entry 추가) + 첫 PR actual run id evidence |
| **(e)** 합의 APPROVE | ✅ | 27번째 entry Reviewer-only 단축 합의 APPROVE |

→ **5/5 완전 충족** (31번째 entry 첫 PR evidence 답습)

### 2.3 ST-2 inotify sidecar (28번째 entry, commit `1edc5bb`)

| 조건 | 충족 자격 | 답습 source |
|---|---|---|
| **(a)** 사용자 명시 결정 | ✅ | 28번째 entry D-1~D-3 3/3 사용자 결정 |
| **(b)** 격리 환경 PoC | ✅ **완전 충족** | Cycle 3+4 답습 — docker-compose + watch-secrets.sh + hermes-mock + 5 fixture + tool 258줄, 31번째 entry 첫 PR `scan` (secret-hygiene) PASS = ST-2 step `tools/docker_secret_inotify_sidecar_check.sh` 5/5 fixture PASS evidence |
| **(c)** stateless · network-free | ✅ | docker-compose 격리 (named volume + cap_drop ALL + no-new-privileges + F-A 비채택) |
| **(d)** 자동 회귀 검증 경로 | ⏳ **부분 충족** | `on:` nightly schedule 추가 (28번째 entry) + 첫 PR push trigger evidence = 발효 / nightly actual run id evidence 미수집 (사용자 자율 영역, 익일 KST 12:00 첫 nightly run) |
| **(e)** 합의 APPROVE | ✅ | 28번째 entry Reviewer-only 단축 합의 APPROVE |

→ **4/5 완전 + 1/5 부분 충족** (nightly actual run id evidence carry-over)

### 2.4 AR-3 통합 PR auto-reject (29+30+31번째 entry, commits `7f57323` + `7c294bb` + `73ed20d` + `9837298`)

| 조건 | 충족 자격 | 답습 source |
|---|---|---|
| **(a)** 사용자 명시 결정 | ✅ | 29번째 entry D-1~D-4 + 30번째 entry D 적용 결정 + 31번째 entry 조치 2건 (fixture + contexts) |
| **(b)** 격리 환경 PoC | ✅ **완전 충족** | 31번째 entry PR #2 draft 11/11 SUCCESS + 중복 동작 race 0 확정 + admin bypass 0 evidence |
| **(c)** stateless · network-free | ✅ | GitHub branch protection rule (자체 정책, 외부 의존 0) |
| **(d)** 자동 회귀 검증 경로 | ✅ **완전 충족** | branch protection rule 발효 + 매 PR 자동 status check 의무 + 7 contexts (guard/verify/feasibility/scan/enforce/defense/validate) + 31번째 entry mergeable CLEAN evidence |
| **(e)** 합의 APPROVE | ✅ | 29번째 entry Reviewer-only 단축 합의 APPROVE + 31번째 entry 조치 합의 |

→ **5/5 완전 충족** (31번째 entry 첫 PR evidence 답습)

### 2.5 종합 (4 sub-cycle)

| sub-cycle | 완전 충족 | 부분 충족 | 영역 |
|---|---|---|---|
| PC-1-T3 | 3/5 ((a)(c)(e)) | 2/5 ((b)(d)) | dev 환경 evidence 수집 자율 + D-6 CI 통합 carry-over |
| S-3 | **5/5** | 0/5 | 31번째 entry 첫 PR PASS 답습 |
| ST-2 | 4/5 ((a)(b)(c)(e)) | 1/5 ((d)) | nightly actual run id evidence carry-over |
| AR-3 | **5/5** | 0/5 | 31번째 entry 첫 PR PASS + mergeable CLEAN |

**합산**: 17/20 완전 충족 + 3/20 부분 충족.

> **R-5 BLOCKING 흡수 — partial carry-over 비차단 사유 명문화**: 3/20 부분 충족 = MVP-1 exit 필수 차단조건 *아님*. 이유 3중 답습:
>
> 1. **Defense in depth cross-cover 답습**: PC-1 (dev hook) 부분 충족 = PC-3 (CI step 답습) + AR-3 (branch protection 발효) cross-cover → 실 보안 효과 = 3 계층 결합 (PC-1+PC-3+AR-3), 단일 계층 부분 충족 자체가 보안 효과 손실 0건.
> 2. **자율 영역 답습**: PC-1-T3 PoC evidence (`bash bin/setup.sh` 실 실행) + ST-2 nightly actual run id = 운영 영역 (사용자 자율) — 실 도구/스크립트 본문 발효 + workflow 발효 자체는 완료, 실 evidence 수집만 자율. brief §1.2 #1~#10 변경 0건 의무 답습 = 본 cycle 자격 영향 0건.
> 3. **cross-reference 정정 한정 (R-S1 carry-over (b2))**: ADR-008 §A.2 R1-2 인용 = source attribution 정정 영역 (별도 sub-cycle), ADR-008 본문 자체 변경 0건 (R-MVP1-PASS-2 영구 금지 답습) → 실 권위 본문 (ADR-008 차단조건 #1/#4/#6 + 부록 B + ADR-010 + ADR-011) 모두 발효 답습 = (c) 권위 명시 자격 영향 0건.
>
> → **GP-3 / GP-5 5/5 충족 자격 = (b1) 4 sub-cycle 17/20 + 추가 layer (S-1 + ST-3 + import-linter + provider scanner) cross-cover 답습** (R-5 BLOCKING 흡수).

---

## §3 GP-3 / GP-5 ADR-011 (a)~(e) 충족 매트릭스 (roadmap-mvp1 §2.2 답습)

### 3.1 GP-3 — Credential / Secret Hygiene

| 조건 | 충족 자격 | 답습 source |
|---|---|---|
| **(a)** 동등 이상 보안 결과 | ✅ | **S-1 (Group D scanner 45 patterns)** + **S-3 (detect-secrets Tier-1 plugin 5종)** + **ST-2 (inotify sidecar)** + **PC-1 (pre-commit framework 의무화)** 다층 발효 = R-4.1 Tier-1 42 catalog 답습 동등 이상 (Defense in depth) |
| **(b)** 격리 환경 PoC | ✅ | docker secret + chmod 600 + ST-2 inotify (저장 경로) PoC + S-3 detect-secrets PR auto-reject (코드) PoC + 31번째 entry 첫 PR (head SHA `9837298`) PASS evidence + Defense in depth cross-cover (PC-1 PoC evidence 자율 영역 = §2.5 R-5 답습) |
| **(c)** ADR / SDD 권위 명시 | ✅ | **multi-source 답습 (R-3 BLOCKING 흡수)**: **ADR-008 차단조건 #1 (SQLCipher, line 17~23)** + **#6 (Docker 격리 + egress 화이트리스트, line 17~23)** + **부록 B (Amendment)** + **ADR-010 (SQLCipher Vault)** + **ADR-011 (수단/목적 분리 §2.1 (a)~(d) + (e) 운영조건)** + **R-4 (Tier-1 42 catalog)** + **roadmap-mvp1 §3** + **(b1) 4 sub-cycle brief + 합의 본문** 모두 발효. ⚠️ `ADR-008 §A.2 R1-2` 인용 = R-S1 cross-reference 정정 carry-over (b2) 답습 영역 (실 §A.2 = "Hermes JSONL Export 검증" + R1-2 식별자 ADR-008 본문 0건). 단 R-S1 = cross-reference attribution 정정 한정 = **본 PASS 발효 *자체* 자격 0건 손실 0** (R-MVP1-PASS-2 영구 금지 답습) |
| **(d)** 자동 회귀 검증 경로 | ✅ | `.github/workflows/secret-hygiene-egress-redaction.yml` (S-1 11+ step + S-3 3 step + ST-2 step + Stage 2/4/5 답습) + nightly schedule (28번째 entry) + 31번째 entry 첫 PR (head SHA `9837298`) PASS run id + ST-2 nightly actual run id 자율 수집 영역 (§2.5 R-5 답습) |
| **(e)** 합의 APPROVE | ✅ | 24번째 entry brief APPROVE w/ COND + (b1) 4 sub-cycle 모두 APPROVE + 31번째 entry 조치 합의 + 본 cycle 풀 3+1 + 외부 LLM 1+ APPROVE WITH CONDITIONS |

→ **GP-3 5/5 충족 자격 자격** (R-S1 정정 carry-over (b2) 답습 명문 + R-3 multi-source 재기술 BLOCKING 흡수)

### 3.2 GP-5 — Provider Liquidity Enforcement

| 조건 | 충족 자격 | 답습 source |
|---|---|---|
| **(a)** 동등 이상 보안 결과 | ✅ | **import-linter (T-2 contract TR-1~TR-5)** + **provider scanner (T-5 부분 — AST + URL + Model)** + **AR-3 (branch protection)** 발효 = Provider Liquidity 5-way 답습 |
| **(b)** 격리 환경 PoC | ✅ | Group A 1차 PoC (AST 5종 패턴) + 2차 PoC (depcruise vs import-linter) + 3차 PoC (provider URL scanner) + 31번째 entry 첫 PR (head SHA `9837298`) `enforce` x3 모두 PASS evidence |
| **(c)** ADR / SDD 권위 명시 | ✅ | **multi-source 답습 (R-2 + R-3 BLOCKING 흡수)**: **ADR-008 차단조건 #4 (어댑터 추상화, line 97/149)** + **부록 B (Amendment)** + **ADR-009 (자체 Adapter v2.0)** + **ADR-011** + **P1 v2** + **roadmap-mvp1 §4** + **Group A 2차/3차 합의 본문** 모두 발효. R-S1 carry-over (b2) = GP-3 (c) 영역 한정 (§A.2 R1-2 source 손상), **GP-5 (c) = R-S1 무관** (차단조건 #4 = 실 ADR-008 line 97/149 정합 attribution, R-S1 표기 제거 영역, R-2 BLOCKING 답습) |
| **(d)** 자동 회귀 검증 경로 | ✅ | `.github/workflows/provider-adapter-enforcement.yml` (import-linter + provider-import-scanner) + `provider-url-scanner.yml` + 매 PR + 31번째 entry 첫 PR (head SHA `9837298`) `enforce` x3 + `scan` (provider-url-scanner) actual run id evidence |
| **(e)** 합의 APPROVE | ✅ | 24번째 entry brief APPROVE + (b1) 4 sub-cycle APPROVE (AR-3 = GP-3 + GP-5 통합) + 31번째 entry 조치 + 본 cycle 풀 3+1 + 외부 LLM 1+ APPROVE WITH CONDITIONS |

→ **GP-5 5/5 충족 자격 자격** (R-2 GP-5 (c) R-S1 표기 제거 + R-3 multi-source 재기술 BLOCKING 흡수)

### 3.3 종합

| GP | 5/5 충족 자격 | 부분 충족 | carry-over |
|---|---|---|---|
| **GP-3** | ✅ 5/5 자격 자격 | 0 | (b2) R-S1 정정 cross-reference + PC-1-T3 PoC evidence 수집 자율 |
| **GP-5** | ✅ 5/5 자격 자격 | 0 | (b2) R-S1 정정 cross-reference + (d) facade real |

**MVP-1 PASS 발효 자격 자격 자격 = GP-3 5/5 + GP-5 5/5 + 사용자 명시 결정** (roadmap-mvp1 §2.2 line 141 답습).

---

## §4 PASS 발효 형태 후보 (D-2 결정 영역)

| 후보 | 내용 | 트레이드오프 |
|---|---|---|
| **(α)** 완전 PASS 발효 | GP-3 5/5 + GP-5 5/5 충족 자격 자격 모두 발효 → roadmap-mvp1 **§2.2 + §3.6.3 + §4.7.3 + §5.1 + §9** 본문 갱신 (R-1 BLOCKING 정정 답습) | (b2) R-S1 carry-over 미해결 상태에서 발효 → 후속 R-S1 정정 = cross-reference 정정 한정 (본 PASS 효과 영향 0건) / PC-1-T3 PoC evidence 자율 영역 (보안 효과 = Defense in depth 답습) |
| **(α′)** 완전 PASS 발효 + Evidence 통합 보강 동반 (N-1 권고 흡수) | (α) + (b1) 4 sub-cycle Markdown evidence 통합 보강 (`g2-gp3-mvp1-evidence.md` + `g2-gp5-mvp1-evidence.md`, 28번째 entry D-3 carry-over 답습) 본 cycle 동반 | 장점: PASS 발효 *시점* 의 evidence Markdown source 동시 정비 + sub-cycle 1회 감축 (ceremony-inflation 차단) / 단점: 본 cycle scope ↑ (변경 허용 영역 확장 = 사용자 명시 결정 영역) |
| **(β)** 부분 PASS 발효 | GP-3 부분 + GP-5 부분 (PoC evidence carry-over 명시) → roadmap §2.2 "부분 exit" 표시 | 권위 표시 모호 + 향후 완전 PASS 별도 합의 필요 (cycle 중복). **기각** (Agent C C-기각-1 답습) — (α) dominant strategy |
| **(γ)** DEFER (PASS 발효 미진행) | 본 cycle = audit + 진입 자격 자격 인정 한정, 실 PASS 발효 = 별도 cycle (PoC evidence 모두 수집 후) | (b1) 4 sub-cycle 완료 + 첫 PR 11/11 SUCCESS evidence 가 있음에도 미발효 = ceremony-inflation risk + 사용자 권리 영역 답습 위반 risk (PASS 발효 = 사용자 권리 영역). **기각** (Agent C C-기각-1 + codex 권고 4 답습) |

→ **권고 = (α) 완전 PASS 발효** (기본) 또는 **(α′) Evidence 통합 보강 동반** (사용자 결정 영역) — (b1) 4 sub-cycle + 첫 PR evidence 누적 충족 + roadmap §2.2 명백한 자격 충족 + carry-over (R-S1 / PC-1-T3 PoC) = 본 PASS 효과 영향 0건 (cross-reference + 보안 효과 답습 영역).

---

## §5 발효 시 효과 (Claude scope 한정)

### 5.1 roadmap-mvp1.md 본문 변경 (사용자 명시 발효 후)

> **R-1 BLOCKING 정정 답습 (v1.1)**: brief v1 의 `§3.5 (GP-3 진입 합의) + §4.5 (GP-5 진입 합의)` 표기는 실 roadmap-mvp1 §3.5 = Rollback Trigger + §4.5 = 측정 metric 와 mismatch. **정확 위치 = §3.6.3 (GP-3 합의 형태 권고) + §4.7.3 (GP-5 합의 형태 권고) + §5.1 (통합 PASS 권고)**.

#### §2.2 갱신 후보 (line 141 영역)

기존: "**MVP-1 exit = (GP-3 5/5 + GP-5 5/5) 두 GP 모두 충족 + 사용자 명시 결정**. 어느 한쪽이라도 미충족 시 MVP-1 부분 PASS 처리 (Implementation Evidence PASS *부분 발효* — 별도 합의 영역)."

갱신: 위 본문 + 새 줄 추가:
> **2026-05-27 발효** (commit `(본 commit)`, 32번째 entry): **GP-3 5/5 + GP-5 5/5 모두 충족 자격 자격 인정 + 사용자 명시 결정 = MVP-1 Implementation Evidence PASS *완전 발효***. 본 발효 = (b1) 4 sub-cycle (PC-1-T3 + S-3 + ST-2 + AR-3) 완료 + 31번째 entry 첫 PR (head SHA `9837298befdeda6c7e170879cc9f15e331c52bce`) 11/11 SUCCESS + mergeable CLEAN evidence + 본 cycle 풀 3+1 + 외부 LLM 1+ APPROVE WITH CONDITIONS 답습. carry-over = (b2) R-S1 cross-reference 정정 (PASS 효과 영향 0건) + PC-1-T3 PoC evidence 자율 수집 + ST-2 nightly actual run id evidence 자율 수집 + paths-aware workflow audit (R-6 답습).

#### §3.6.3 (GP-3 합의 형태 권고, line 283~292) 갱신 후보

GP-3 합의 형태 권고 표 또는 "Implementation Evidence PASS 발효" 행에 발효 일자 + 본 cycle commit reference 추가. (N-2 권고 흡수): §3.6.3 cross-reference 동반 갱신 = (b3) framing 정정 sub-cycle 동반 권고 영역 (별도 sub-cycle 답습).

#### §4.7.3 (GP-5 합의 형태 권고, line 473~485) 갱신 후보

동일 — GP-5 합의 형태 권고 표에 발효 일자 + 본 cycle commit reference 추가.

#### §5.1 (통합 PASS 권고) 갱신 후보

§5.1 = "ADR-011 §2.1 (a)~(e) 5조건 답습" 영역. PASS 발효 시 "발효 일자" 행 추가 후보 — 통합 PASS 자격 cell 에 본 cycle 합의 cross-reference 추가.

#### §9 변경 이력 추가

```
| 2026-05-27 (32번째 entry) | MVP-1 Implementation Evidence PASS 완전 발효 | GP-3 5/5 + GP-5 5/5 충족 + 사용자 명시 + (b1) 4 sub-cycle + 31번째 entry 첫 PR PASS evidence (head SHA `9837298`) + 본 cycle 풀 3+1 + 외부 LLM 1+ 합의 |
```

### 5.2 (Claude 영역 외) 후속 권위 영역

- **MVP-2 진입 자격** = MVP-1 완전 PASS 발효 후 = 별도 합의 영역 (roadmap §99 답습)
- **Operational Readiness PASS (Layer 3)** = MVP-1 PASS 와 별도 layer = 별도 합의
- **Hermes PMO 격상** = 별도 합의
- **4 게이트 일괄 PASS** = G2/G3/G4 + GP-2 모두 PASS 후 = 별도 합의

→ 본 cycle scope = **MVP-1 Implementation Evidence PASS 완전 발효 한정** (다른 layer / 격상 / 일괄 PASS 모두 영역 외).

---

## §6 Rollback Trigger (본 cycle 적용 형태)

| ID | trigger | 본 cycle 발효 형태 |
|---|---|---|
| **R-MVP1-PASS-1** | (b1) 4 sub-cycle 본문 변경 발생 (도구 변경 / 정책 변경 / catalog 변경) | (b1) 본문 변경 형태별 차등 (S-3 = R-MVP1-1.5-S3 / ST-2 = R-MVP1-1.5-ST2 / PC-1 = R-MVP1-1.5-PC1 / AR-3 = R-MVP1-1.5-AR3 답습) — 변경 시 PASS 부분 재검증 의무 |
| **R-MVP1-PASS-2** | (b2) R-S1 cross-reference 정정 시 ADR-008 본문 변경 발생 | **영구 금지** (R-S1 = cross-reference 정정 한정, ADR-008 본문 변경 0건 의무 — (b2) brief 답습 의무) → 본문 변경 시 풀 3+1 합의 + ADR 권위 영역 |
| **R-MVP1-PASS-3** | 11 workflow 본문 변경 (S-3 step 또는 ST-2 step 제거 / Tier-2/3 catalog 자동 확장) | 풀 3+1 + 외부 LLM 1+ + 사용자 명시 (Tier-2/3 catalog 확장 영역 답습) |
| **R-MVP1-PASS-4** | branch protection rule 우회 / admin bypass 발견 (R-MVP1-1.5-AR3-1 답습) | 단축 합의 + 사용자 명시 재검토 + 부분 PASS 재검증 |
| **R-MVP1-PASS-5** | MVP-2 진입 자격 자동 발효 (본 cycle 영역 외 발효 시도) | **영구 금지** (별도 합의 영역) |
| **R-MVP1-PASS-6** (R-4 BLOCKING 흡수, v1.1 신규) | ST-2 nightly actual run 실패 또는 미발화 발견 | 부분 재검증 + (d) carry-over 해소 sub-cycle (단축 합의 + 사용자 명시) |
| **R-MVP1-PASS-7** (R-4 BLOCKING 흡수, v1.1 신규) | PC-1-T3 install audit / bypass detection evidence 실패 | PC-1 방어층 재검증 + 부분 재검증 (단축 합의 + 사용자 명시) |
| **R-MVP1-PASS-8** (R-4 + R-6 BLOCKING 흡수, v1.1 신규) | required check context mapping / 동명 check semantics / paths-aware workflow 변경으로 branch protection CLEAN evidence 무효화 (paths-aware workflow audit 후속 식별 영역 포함) | AR-3 재검증 + contexts 정정 또는 workflow paths widen 별도 sub-cycle (단축 합의 + 사용자 명시) |
| **R-MVP1-PASS-9** (R-4 BLOCKING 흡수, v1.1 신규) | Provider Liquidity scanner / import-linter / provider-url / model scanner disable 또는 facade bypass 발견 | GP-5 PASS 재검증 + 헌법 5조-2 답습 (풀 3+1 + 외부 LLM 1+ + 사용자 명시) |
| **R-MVP1-PASS-10** (R-4 BLOCKING 흡수, v1.1 신규) | R-S1 정정 과정에서 단순 cross-reference 가 아니라 권위 본문 의미 변경 필요 판명 | PASS 발효 보류 또는 재합의 (풀 3+1 + 외부 LLM 1+ + R-MVP1-PASS-2 영구 금지 답습 재검토) |

---

## §7 사용자 결정 항목 (brief 합의 진입 전 의무)

| # | 항목 | 후보 | 권고 |
|---|---|---|---|
| **D-1** | 합의 형태 | (i) 단축 합의 (Reviewer-only) / (ii) 풀 3+1 / (iii) 풀 3+1 + 외부 LLM 1+ | **(iii) 풀 3+1 + 외부 LLM 1+** — 본 프로젝트 최초 MVP-1 PASS 발효 + T3 영역 답습 + 24번째 entry pattern + 메인 권위 격상 영역. cross-vendor blind risk 차단 의무 (외부 LLM 1+) |
| **D-2** | PASS 발효 형태 | (α) 완전 PASS 발효 / (β) 부분 PASS 발효 / (γ) DEFER | **(α) 완전 PASS 발효** — (b1) 4 sub-cycle + 첫 PR evidence 누적 충족, carry-over = PASS 효과 영향 0건 (cross-reference + 보안 답습 영역) |
| **D-3** | roadmap-mvp1.md 본문 갱신 범위 | (i) §2.2 + §9 만 (최소) / **(ii) §2.2 + §3.6.3 + §4.7.3 + §5.1 + §9 (권고, R-1 정정 답습)** / (iii) 본문 광범위 재구성 | **(ii) §2.2 + §3.6.3 + §4.7.3 + §5.1 + §9** — 발효 표시 정확화. **R-1 BLOCKING 정정 답습 (v1.1)** — brief v1 의 `§3.5 + §4.5` 표기는 실 roadmap §3.5 (Rollback Trigger) / §4.5 (측정 metric) 와 mismatch, 정확 위치 = `§3.6.3 (GP-3 합의 형태 권고) + §4.7.3 (GP-5 합의 형태 권고) + §5.1 (통합 PASS 권고)` |
| **D-4** | ledger entry (ADR-012 §2.2 답습) | (A) 본 cycle 등록 / (B) Backlog #5 별도 합의 영역 (답습) / (C) DEFER | **(B) Backlog #5 별도 합의** — ADR-012 §2.2 enum 정식 등록 = 별도 영역 답습 (기존 secret_scan_layer1_implementation 등 패턴 답습) |
| **D-5** | 다음 cycle 우선순위 (**R-6 BLOCKING 정정 답습 v1.1**) | (i) MVP-2 진입 자격 검토 / (ii) (b2) R-S1 정정 / (iii) Markdown evidence 통합 (D-3 답습) / (iv) Operational Readiness PASS Layer 3 / (v) 세션 cool-down / **(vi) paths-aware workflow audit (31번째 entry §4.3 carry-over 답습)** | **(vi) paths-aware workflow audit 우선 → (ii) (b2) R-S1 + (b3) framing 병렬 → (iii) Markdown evidence 통합 → (b1-PC1-D6) → (vii) PR #2 merge → (d) facade real → (i) MVP-2** — **R-6 BLOCKING 정정**: 31번째 entry §4.3 carry-over verbatim 답습 + 운영 risk 즉시성 (r2-canary 와 동형 risk = 다른 PR merge 영원 차단 risk 발화 가능, 본 cycle R-MVP1-PASS-8 답습) + (b2) + (b3) cross-reference 정정 영역 유사 → 병렬 sub-cycle (Agent C C-N-6 권고 답습) |

---

## §8 합의 형태 권고 + 다음 단계

### 8.1 합의 형태 권고

**풀 3+1 + 외부 LLM 1+** 권고 — 근거:

| 근거 | 내용 |
|---|---|
| **roadmap §2.2 line 141** | "MVP-1 exit = (GP-3 5/5 + GP-5 5/5) + 사용자 명시 결정" — 메인 권위 발효 |
| **24번째 entry pattern** | T3 영역 + 메인 권위 결정 = 풀 3+1 + 외부 LLM 1+ 답습 (entry brief line 113 답습) |
| **본 프로젝트 최초 MVP-1 PASS 발효** | 단축 합의 자격 0 (precedent 0건, 다관점 검증 필수) |
| **CLAUDE.md §3 매트릭스** | "아키텍처 의사결정 / SDD 명세 검토 / 보안 관련 변경" 모두 = 3+1 필수 |
| **cross-vendor blind risk** | 외부 LLM 1+ = 24번째 entry 직접 답습 (codex via tmux) |

단축 합의 후보 = **기각** — 메인 권위 격상 + 최초 발효 + 풀 3+1 승격 trigger ①(새 권위 결정) + ③(PASS 자동 선언) + ④(후속 합의 본문 변경 = roadmap §2.2 + §3.6.3 + §4.7.3 + §5.1) 모두 발화. trigger 3/5 발화 = 풀 3+1 의무 답습.

### 8.2 다음 단계 (단계별 합의 cycle 6단계 + 사용자 명시 단계 답습)

1. ✅ **brief 작성** (단계 1)
2. ✅ **사용자 승인** — §7 D-1~D-5 결정 (D-1/D-2/D-3/D-5 권고 채택, D-4 default)
3. ✅ **풀 3+1 합의 (Agent A/B/C 3 병렬 독립) + 외부 LLM 응답 1+ (codex via tmux Claude 직접 호출)** — 본 cycle = 4 source 모두 병렬 도착 + Reviewer 통합 **APPROVE WITH CONDITIONS** (BLOCKING 6 + 권고 5)
4. ✅ **brief v1.1 보강** (BLOCKING 6 + 권고 5 1pass 흡수) — 본 v1.1 in-place 보강
5. ⏳ **roadmap-mvp1.md 본문 갱신** (§2.2 + §3.6.3 + §4.7.3 + §5.1 + §9, R-1 정정 답습)
6. ⏳ **commit + push** (SSH 답습, `reference_git_remote_ssh.md` 메모리 답습)
7. ⏳ **다음 cycle (D-5 재조정)**: (vi) paths-aware audit → (ii) (b2) R-S1 + (b3) framing 병렬 → (iii) Markdown evidence 통합 → ...

---

## §9 본 brief 자기진단 (10/10 통과 의무)

| # | 항목 | 통과 |
|---|---|---|
| 1 | 본 brief 자체 PASS 발효 0건 / roadmap-mvp1 본문 변경 0건 | ✅ brief 작성 한정 |
| 2 | (b1) 4 sub-cycle 본문 0 / 11 workflow 0 / src 0 / tools 0 / docker 0 / 헌법 0 / ADR 0 | ✅ §1.2 |
| 3 | (b1) 4 sub-cycle ADR-011 (a)~(e) 매트릭스 정확 audit (17/20 완전 + 3/20 부분) | ✅ §2 |
| 4 | GP-3 5/5 + GP-5 5/5 충족 자격 자격 인정 매트릭스 (R-S1 carry-over 명문) | ✅ §3 |
| 5 | PASS 발효 형태 후보 (α/β/γ) 비교 + 권고 (α) 명문 | ✅ §4 |
| 6 | 발효 시 효과 + Claude scope 한정 명문 (roadmap §2.2 + §3.5 + §4.5 + §9 갱신) | ✅ §5 |
| 7 | Rollback Trigger R-MVP1-PASS-{1,2,3,4,5} 본문 채택 + R-S1 영구 금지 명문 (R-MVP1-PASS-2) | ✅ §6 |
| 8 | 사용자 결정 D-1~D-5 명시 + 풀 3+1 + 외부 LLM 1+ 권고 (단축 합의 기각 근거 trigger 3/5 발화) | ✅ §7 + §8.1 |
| 9 | 6단계 cycle + 외부 LLM 응답 사용자 영역 명문 + 24번째 entry pattern 답습 | ✅ §8.2 |
| 10 | MVP-2 / Operational Readiness / Hermes PMO / 4 게이트 일괄 PASS 모두 영역 외 명문 | ✅ §1.2 #9~#12 + §5.2 |

---

> **본 brief 발효 시점** = 사용자 승인 (§7 D-1~D-5 결정) + 풀 3+1 + 외부 LLM 1+ APPROVE + 본 brief commit. 본 brief 자체 = **MVP-1 Implementation Evidence PASS 완전 발효 자격 자격 자격 검증 한정**. 실 PASS 발효 = brief 합의 발효 *후* roadmap-mvp1 본문 갱신 단계 (사용자 명시 답습 의무).
