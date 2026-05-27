# MVP-1 → MVP-6 진입 조건 Brief

> **본 brief는 C-7 line 378-383 (MVP-0 ~ MVP-6 단계화 권고) + `implementation-runtime-roadmap-mvp1.md` (MVP-1 deepening) 의 *6 단계 진입 조건* 일괄 정리이다.**
>
> 본 brief = **기존 합의 출처의 synthesis 한정**. **수단 결정 / threshold 고정 / 신규 MVP-2~6 deepening / PASS 선언 모두 0건**. 모든 *결정* 은 별도 합의.

**작성일**: 2026-05-19
**상태**: DRAFT — 사용자 승인 대기
**상위 권위**: ADR-011 §2.1 (a)~(e), ADR-008 부록 C §C.5 (Design/Governance ↔ Implementation/Runtime 분리), 외부 LLM GPT-5.5 Thinking 응답 §6 (3-layer PASS 분리)
**근거 합의**:
- `docs/review/3plus1-consensus-2026-05-07-g2-g3-g4-gate-adoption.md` §C-7 line 371-385 (MVP-0 ~ MVP-6 단계화 권고 등록)
- `docs/external-review/2026-05-07-g2-g3-g4-integrated-gate-review-response.md` §6 권장 MVP 단계 (line 237-262) + §7 PASS 의미 분리 (line 264-276)
- `docs/architecture/implementation-runtime-roadmap-mvp1.md` §2 (MVP-1 Entry/Exit 기준)
- `docs/architecture/implementation-runtime-roadmap.md` §6 (PASS 기준 통합 매트릭스 + ADR-011 §2.1 5조건)

---

## 0. 본 brief 범위

### 0.1 본 brief 가 *하는* 것

1. C-7 line 378-383 (MVP-0 ~ MVP-6 최소 구현 정의) 의 *진입 조건 매트릭스 형태* 통합
2. MVP-1 의 기존 Entry/Exit 기준 (`roadmap-mvp1.md` §2.1 / §2.2) 일괄 답습
3. MVP-2 ~ MVP-6 의 *최소 구현 = 답습 답안 한정* + **deepening 미진행 영역 명시** (각 단계 별도 합의 의무)
4. 3-layer PASS 분리 (Design / Implementation Evidence / Operational Readiness) 와 6 MVP 단계의 매핑 답습
5. ADR-011 §2.1 (a)~(e) 5조건 = 모든 MVP 단계 의무 답습 명시

### 0.2 본 brief 가 *하지 않는* 것 (사용자 명시 답습)

- ❌ MVP-2 ~ MVP-6 의 *deepening* (수단 후보 비교 / threshold 후보 / Rollback Trigger / Evidence Required 분해) — `roadmap-mvp1.md` 가 MVP-1 에 한정한 작업 답습, MVP-2 deepening = 별도 합의 영역
- ❌ MVP-1 → MVP-2 진입 *결정* (MVP-1 exit 발효 = 별도 합의 + GP-3 5/5 + GP-5 5/5 + 사용자 명시)
- ❌ MVP-2 진입 *시점* / MVP-3 ~ MVP-6 *시점* 결정 (사용자 결정 영역)
- ❌ MVP-2 ~ MVP-6 의 *수단 결정* (GP-2 / GP-4 / GP-6 / G3 운영 hook / G4 Layer 3 / Layer 5 모두 별도 합의)
- ❌ Hermes PMO 격상 / Operational Readiness PASS / 4 게이트 일괄 PASS 선언
- ❌ 신규 ADR / 새 P / 새 GP 발행
- ❌ 17 항목 우선순위 (`implementation-runtime-roadmap.md` §5.1) 변경
- ❌ 외부 LLM line 242 vs C-7 line 378 충돌 *재해석* (C-7 답습 영구, `roadmap-mvp1.md` §1.3 답습)
- ❌ Phase α-4 R-1 Stage 4 W-4 actual run trigger 영역 변경
- ❌ 본 brief 자체의 합의 자동 진입 (사용자 명시 승인 후 별도 단계)

### 0.3 본 brief 의 권위 한계

본 brief = **synthesis DRAFT 한정**. 본 brief 의 어떤 §도 그 자체로:

- (i) MVP-2 ~ MVP-6 의 수단을 *결정* 하지 않으며,
- (ii) MVP-1 의 exit / 어떤 MVP 의 PASS 를 *선언* 하지 않으며,
- (iii) 17 항목 우선순위를 *변경* 하지 않으며,
- (iv) 신규 ADR / P / GP 를 *발행* 하지 않으며,
- (v) Hermes PMO 격상 / Operational Readiness PASS / Implementation/Runtime PASS 를 *발생시키지 않는다*.

본 brief 가 발생시키는 *유일한* 효과는 **6 MVP 단계의 진입 조건 매트릭스 일괄 답습 한정**. 모든 *결정* 은 *별도 합의*.

---

## 1. 6 MVP 단계 일괄 매트릭스 (C-7 line 378-383 답습 + 본 brief synthesis)

| 단계 | 최소 구현 정의 (C-7 답습) | 합의 시점 | 3-layer 매핑 | 본 brief deepening 상태 |
|----|------------------------|----------|------------|------------------------|
| **MVP-0** | 본 통합 PASS (Design/Governance Gate PASS 발효) | ✅ **완료 (2026-05-07 + 2026-05-09 Bundled)** | Layer 1 | 답습 한정 (deepening 불필요) |
| **MVP-1** | G2 GP-3 (Credential / Secret Hygiene) + GP-5 (Provider Adapter Enforcement) 실 구현 | Implementation 1차 합의 | Layer 2 (1차) | ✅ **`roadmap-mvp1.md` deepening 완료** |
| **MVP-2** | G2 GP-2 (Egress Redaction) + G4 §4.4 Layer 4 (log canary + canonical JSON + R-6 workflow ledger 검증) | Implementation 2차 합의 | Layer 2 (2차) | ⏳ **deepening 미진행 — 별도 합의 의무** |
| **MVP-3** | G2 GP-6 (Memory / Skill 답습) + G4 §4.5 PoC (migration script 1건 라운드트립) | Implementation 3차 합의 | Layer 2 (3차) | ⏳ **deepening 미진행 — 별도 합의 의무** |
| **MVP-4** | G3 운영 hook (filesystem read-only + Hermes-originated commit auto-reject pre-commit) | Implementation 4차 합의 | Layer 2 (4차) | ⏳ **deepening 미진행 — 별도 합의 의무** |
| **MVP-5** | G4 §4.4 Layer 3 (Signed commit) + Layer 5 (External anchor) | Multi-host 전환 시점 | Layer 2 (5차) | ⏳ **deepening 미진행 — Multi-host trigger 5건 발화 의무** |
| **MVP-6 (PMO 격상)** | 4 게이트 모두 Implementation PASS + 외부 LLM 1+ + 인간 전문 리뷰 + 사용자 명시 | 별도 합의 | Layer 3 | ⏳ **deepening 미진행 — 4 게이트 전부 PASS 후만 가능** |

**현 시점 (2026-05-19) = MVP-0 ✅ 완료, MVP-1 진입 4/5** (`roadmap-mvp1.md` §2.1 답습 — #5 만 본 roadmap-mvp1 후속 합의 후 발효).

---

## 2. MVP-1 Entry / Exit 기준 (`roadmap-mvp1.md` §2 답습)

### 2.1 MVP-1 Entry 기준 (5 조건)

| # | 조건 | 현 상태 (2026-05-19) | 검증 출처 |
|---|------|---------------------|----------|
| 1 | Layer 1 (Design/Governance Gate) PASS 발효 | ✅ G2/G3/G4 = PASS Bundled (2026-05-09) | `docs/review/3plus1-consensus-2026-05-07-g2-g3-g4-gate-adoption.md` |
| 2 | GP-3 PoC 완료 (형식적 검출 layer 시제) | ✅ Group D 통합 PoC PASS 6/6 (2026-05-10) | `docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md` |
| 3 | GP-5 PoC 완료 (Layer 1a/1b/1c 시제) | ✅ Group A 1차/2차/3차 PASS (2026-05-09 ~ 2026-05-10) | `docs/phase0/g2-gp5-provider-adapter-enforcement-poc.md` + `g2-gp5-poc2-import-linter-implementation.md` + `g2-gp5-poc3-url-endpoint-model-name-scanner.md` |
| 4 | R-4.1 Tier-1 42 catalog 등록 PASS | ✅ R-4.1 PoC PASS (2026-05-07) | `docs/phase0/r4-1-trigger-extension-evidence.md` |
| 5 | 본 `roadmap-mvp1.md` Reviewer-only 단축 합의 APPROVE | ⏳ 후속 합의 (작성 예정) | `docs/review/3plus1-consensus-2026-05-12-implementation-runtime-roadmap-mvp1.md` |

**현 시점 충족 = 4/5** — #5 만 본 roadmap-mvp1 후속 합의 발효 시 적격.

### 2.2 MVP-1 Exit 기준 (= Implementation Evidence PASS 진입 조건)

각 GP 별 Implementation Evidence PASS = **ADR-011 §2.1 (a)~(e) 5 조건 답습 모두 충족 의무**:

| # | 조건 | GP-3 | GP-5 |
|---|------|------|------|
| (a) | 동등 이상의 보안 결과 | gitleaks/detect-secrets/custom scanner 결과 R-4.1 Tier-1 42 catalog 답습 동등 이상 | depcruise/import-linter 결과 §9.3 답습 동등 이상 |
| (b) | 격리 환경 PoC 실증 | docker secret + chmod 600 + inotify (저장) PoC + gitleaks PR auto-reject (코드) PoC | depcruise/import-linter PR auto-reject + facade single entry point PoC |
| (c) | ADR / SDD 권위 명시 | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 + R-4 + `roadmap-mvp1.md` §3 (36번째 entry R-S1 정정 답습) | ADR-008 차단조건 #4 + 부록 B + ADR-009 C-N §5 + ADR-011 + P1 v2 + `roadmap-mvp1.md` §4 (36번째 entry R-S1 정정 답습) |
| (d) | 자동 회귀 검증 경로 확보 | `.github/workflows/secret-scan.yml` (또는 R-6 통합) + nightly | `.github/workflows/provider-adapter-enforcement.yml` 기존 + depcruise/import-linter step 추가 + 매 PR + nightly |
| (e) | 합의 APPROVE | 단축 또는 풀 3+1 (수단 결정 시 풀 3+1 권고 — `roadmap-mvp1.md` §3.6 답습) | 단축 또는 풀 3+1 (T-1 vs T-2 vs T-9 결정 시 풀 3+1 권고 — `roadmap-mvp1.md` §4.6 답습) |

**MVP-1 exit = (GP-3 5/5 + GP-5 5/5) 두 GP 모두 충족 + 사용자 명시 결정**. 어느 한쪽이라도 미충족 시 MVP-1 부분 PASS 처리 (Implementation Evidence PASS *부분 발효* — 별도 합의 영역).

---

## 3. MVP-2 진입 조건 (synthesis — deepening 미진행)

### 3.1 최소 구현 (C-7 line 379 답습)

**G2 GP-2 (Egress Redaction) + G4 §4.4 Layer 4 (log canary + canonical JSON + R-6 workflow ledger 검증)**

### 3.2 Entry 기준 (synthesis 추정 — 별도 합의 의무)

| # | 조건 (synthesis 추정) | 검증 출처 |
|---|--------------------|----------|
| 1 | **MVP-1 exit 발효** (GP-3 5/5 + GP-5 5/5 + 사용자 명시) | MVP-1 후속 합의 |
| 2 | GP-2 PoC 완료 (Group D §1.2 #6 / P1 facade RedactionFilter 답습) | `docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md` D-2 (partial) |
| 3 | G4 §4.4 Layer 4 PoC 완료 (canonical JSON + R-6 workflow ledger 검증) | G4 §4.4 답습 영역 (PoC 미발화) |
| 4 | R-4 / R-4.1 Tier-1 42 catalog **런타임 적용** layer 시제 (Hermes upstream R2-6 또는 P1 facade RedactionFilter) | Group D PoC §8 #1 답습 |
| 5 | 본 MVP-2 deepening roadmap 합의 APPROVE | ⏳ **본 brief 범위 외 — 미작성** |

### 3.3 deepening 미진행 영역 명시

본 brief 범위 외 (별도 합의 의무):
- 수단 후보 비교 (GP-2 송신 redaction = Hermes upstream R2-6 vs sidecar vs P1 facade RedactionFilter)
- threshold 후보 (FN rate / FP rate / canary detection latency)
- Rollback Trigger + Evidence Required
- 합의 형태 권고 (단축 vs 풀 3+1)

---

## 4. MVP-3 진입 조건 (synthesis — deepening 미진행)

### 4.1 최소 구현 (C-7 line 380 답습)

**G2 GP-6 (Memory / Skill 답습) + G4 §4.5 PoC (migration script 1건 라운드트립)**

### 4.2 Entry 기준 (synthesis 추정 — 별도 합의 의무)

| # | 조건 (synthesis 추정) | 검증 출처 |
|---|--------------------|----------|
| 1 | **MVP-2 exit 발효** (GP-2 5/5 + G4 §4.4 Layer 4 5/5 + 사용자 명시) | MVP-2 별도 합의 |
| 2 | GP-6 PoC 완료 (`docs/phase0/g2-gp6-memory-skill-migration-feasibility-poc.md` 발효) | ✅ PoC 일부 PASS (라운드트립 시제 영역) |
| 3 | G4 §4.5 라운드트립 1건 PoC 완료 | G4 §4.5 답습 영역 |
| 4 | G5-6 의미적 lock-in 영역 일부 검증 (`roadmap-mvp1.md` G5-6 답습) | Backlog #2 이후 영역 |
| 5 | 본 MVP-3 deepening roadmap 합의 APPROVE | ⏳ **본 brief 범위 외 — 미작성** |

### 4.3 deepening 미진행 영역 명시

본 brief 범위 외 (별도 합의 의무):
- Memory / Skill migration script 수단 비교
- 라운드트립 검증 threshold 후보
- G5-6 의미적 lock-in 검출 알고리즘 결정
- Rollback Trigger + Evidence Required
- 합의 형태 권고

---

## 5. MVP-4 진입 조건 (synthesis — deepening 미진행)

### 5.1 최소 구현 (C-7 line 381 답습)

**G3 운영 hook (filesystem read-only + Hermes-originated commit auto-reject pre-commit)**

### 5.2 Entry 기준 (synthesis 추정 — 별도 합의 의무)

| # | 조건 (synthesis 추정) | 검증 출처 |
|---|--------------------|----------|
| 1 | **MVP-3 exit 발효** (GP-6 5/5 + G4 §4.5 5/5 + 사용자 명시) | MVP-3 별도 합의 |
| 2 | G3 §5.5.3 트리거 5건 자동 검출 hook 구현 완료 | C-9 답습 (`roadmap-mvp1.md` 외 영역) |
| 3 | Hermes-originated commit 판정 알고리즘 명시 + PoC (git author / committer + Hermes audit log cross-reference) | C-9 답습 |
| 4 | filesystem read-only enforcement layer (Layer 2 runtime block — `g2-gp5-provider-adapter-enforcement-poc.md` §9 영역) | G5-5 답습 (Layer 2 분리) |
| 5 | 본 MVP-4 deepening roadmap 합의 APPROVE | ⏳ **본 brief 범위 외 — 미작성** |

### 5.3 deepening 미진행 영역 명시

본 brief 범위 외 (별도 합의 의무):
- pre-commit hook 수단 비교 (custom Python vs git hook framework)
- Hermes-originated 판정 알고리즘 결정 (git author 단독 vs audit log cross-reference vs hybrid)
- 5 트리거 자동 검출 hook threshold 후보
- Rollback Trigger + Evidence Required
- 합의 형태 권고

---

## 6. MVP-5 진입 조건 (synthesis — deepening 미진행 + Multi-host trigger 의무)

### 6.1 최소 구현 (C-7 line 382 답습)

**G4 §4.4 Layer 3 (Signed commit) + Layer 5 (External anchor)**

### 6.2 Entry 기준 (synthesis 추정 — 별도 합의 의무)

| # | 조건 (synthesis 추정) | 검증 출처 |
|---|--------------------|----------|
| 1 | **MVP-4 exit 발효** (G3 운영 hook 5/5 + 사용자 명시) | MVP-4 별도 합의 |
| 2 | **Multi-host external service 전환 trigger 5건 中 1+ 발화** (CO-6 답습 — 단일 호스트 SPOF 의도적 수용 영역 종료) | `3plus1-consensus-2026-05-07-g2-g3-g4-gate-adoption.md` CO-6 답습 |
| 3 | G4 §4.4 Layer 3 (Signed commit) PoC 완료 (GPG / sigstore 수단 결정) | G4 §4.4 Layer 3 답습 영역 |
| 4 | G4 §4.4 Layer 5 (External anchor) PoC 완료 (timestamping authority / public ledger 수단 결정) | G4 §4.4 Layer 5 답습 영역 |
| 5 | 본 MVP-5 deepening roadmap 합의 APPROVE | ⏳ **본 brief 범위 외 — 미작성** |

### 6.3 deepening 미진행 영역 명시

본 brief 범위 외 (별도 합의 의무):
- Signed commit 수단 비교 (GPG vs sigstore vs ssh signing)
- External anchor 수단 비교 (RFC 3161 TSA vs OpenTimestamps vs blockchain anchor)
- Multi-host external service 5 trigger 검증 threshold
- Rollback Trigger + Evidence Required (특히 다중 호스트 SPOF 영역)
- 합의 형태 권고 (Multi-host = 풀 3+1 + 외부 LLM 1+ 의무 권고)

---

## 7. MVP-6 (Hermes PMO 격상) 진입 조건 (synthesis — 최종)

### 7.1 최소 구현 (C-7 line 383 답습)

**4 게이트 모두 Implementation PASS + 외부 LLM 1+ + 인간 전문 리뷰 + 사용자 명시**

### 7.2 Entry 기준 (synthesis — 별도 합의 의무, 최고 엄격 영역)

| # | 조건 (C-7 답습 직접) | 검증 출처 |
|---|--------------------|----------|
| 1 | **G1 (R-7 redaction SOP) Implementation PASS** | G1 답습 영역 (이미 PASS, 회귀 유지) |
| 2 | **G2 (Hermes adoption) Implementation PASS** | MVP-1 + MVP-2 + MVP-3 exit 합산 (GP-2 + GP-3 + GP-4 + GP-5 + GP-6 + R-4 + R-4.1) |
| 3 | **G3 (운영 hook) Implementation PASS** | MVP-4 exit 합산 |
| 4 | **G4 (Evidence forgery 방지) Implementation PASS** | MVP-2 + MVP-3 + MVP-5 exit 합산 (§4.4 Layer 1~5 + §4.5 + §4.6) |
| 5 | **외부 LLM 1+ blind 의뢰 PASS** (T-6 / T-10 / T-13 발화 시) | C-7 답습 + ADR-011 §2.1 (e) 답습 |
| 6 | **인간 전문 리뷰 PASS** (보안 / 운영 / 컴플라이언스 영역) | C-7 답습 |
| 7 | **사용자 명시 결정** (PMO 격상 = 비가역 전환 = 풀 3+1 의무) | C-7 답습 |
| 8 | **P11 Supply-chain Compromise 정식 등록** (Hermes PMO 격상 *전* 권장 — C-10 답습) | C-10 답습 |
| 9 | **P12 Memory Poisoning Side-channel 정식 등록** (G4 Implementation/Runtime PASS 합의 시점 — C-10 답습) | C-10 답습 |
| 10 | **본 MVP-6 deepening roadmap 합의 APPROVE** (별도 합의 영역) | ⏳ **본 brief 범위 외 — 미작성** |

### 7.3 deepening 미진행 영역 명시

본 brief 범위 외 (별도 합의 의무, 최고 엄격):
- 4 게이트 일괄 PASS 발효 절차 (단계별 vs 일괄)
- 외부 LLM 1+ blind 의뢰 형태 (T-6 / T-10 / T-13 trigger 발화 영역 결정)
- 인간 전문 리뷰 영역 분담 (보안 / 운영 / 컴플라이언스 / 법무)
- PMO 격상 후 Hermes ≠ root of trust 답습 영구 보존 (ADR-011 §2.1 (d) 답습)
- Rollback Trigger (PMO 격상 후 회귀 영역 = 비가역 + Multi-host external service 전환 후 단일 호스트 회귀 = 별도 합의)
- 합의 형태 (풀 3+1 + 외부 LLM 1+ + 인간 전문 리뷰 + 사용자 명시 = 4중 의무)

---

## 8. 3-layer PASS ↔ 6 MVP 단계 매핑 (외부 LLM 답습 §7.1 + `roadmap-mvp1.md` §1.2 답습)

```
┌─────────────────────────────────────────────────────────────────┐
│  Layer 1: Design/Governance Gate PASS                          │
│  → 문서 정의 + 권위 위계 + GP/Skill/Schema *설계* 승인         │
│  → 4 게이트 모두 = ✅ 2026-05-07 + 2026-05-09 (Bundled)         │
│  → MVP-0 = ✅ 완료                                              │
├─────────────────────────────────────────────────────────────────┤
│  Layer 2: Implementation Evidence PASS                         │
│  → 각 GP 별 실 구현 + PoC evidence + 자동 회귀 + 합의 APPROVE  │
│  → MVP-1 = GP-3 + GP-5 (1차)         ← 현재 진입 4/5 충족        │
│  → MVP-2 = GP-2 + G4 §4.4 Layer 4 (2차)                         │
│  → MVP-3 = GP-6 + G4 §4.5 (3차)                                 │
│  → MVP-4 = G3 운영 hook (4차)                                   │
│  → MVP-5 = G4 §4.4 Layer 3 + Layer 5 (5차, Multi-host)          │
├─────────────────────────────────────────────────────────────────┤
│  Layer 3: Operational Readiness PASS                           │
│  → 4 게이트 모두 Implementation Evidence PASS + 외부 LLM 1+    │
│  → 인간 전문 리뷰 + 사용자 명시 + Multi-host external service  │
│  → MVP-6 (PMO 격상) = 본 layer 완료 시점                        │
└─────────────────────────────────────────────────────────────────┘
```

---

## 9. ADR-011 §2.1 (a)~(e) 5 조건 = 모든 MVP 단계 의무 답습

`implementation-runtime-roadmap.md` §6.1 답습 — 6 MVP 모든 단계가 다음 5 조건 충족 의무:

| 조건 | 영역 | MVP-1 ~ MVP-6 적용 |
|------|------|-------------------|
| (a) | 동등 이상의 보안 결과 | 각 GP / 각 layer 의 PoC 결과가 이전 layer 보안 결과 동등 이상 |
| (b) | 격리 환경 PoC 실증 | docker / 격리 환경 PoC 의무 (production 직접 진입 0건) |
| (c) | ADR / SDD 권위 명시 | 각 단계 = ADR / SDD cross-reference 명시 의무 |
| (d) | 자동 회귀 검증 경로 확보 | 각 단계 = CI workflow / nightly job / pre-commit 의무 |
| (e) | 합의 APPROVE | 단축 또는 풀 3+1 + (T-6/T-10/T-13 발화 시) 외부 LLM 1+ blind 의뢰 |

---

## 10. 본 brief 가 *발생시킨* 것 (synthesis 한정)

- 6 MVP 단계 (MVP-0 ~ MVP-6) 의 진입 조건 일괄 매트릭스 답습
- MVP-1 Entry/Exit 기준 답습 (`roadmap-mvp1.md` §2 답습)
- MVP-2 ~ MVP-6 의 *최소 구현 = C-7 답습 답안* + **deepening 미진행 영역 명시**
- 3-layer PASS ↔ 6 MVP 단계 매핑 답습
- ADR-011 §2.1 (a)~(e) 5 조건 = 모든 MVP 단계 의무 답습

---

## 11. 본 brief 가 *발생시키지 않은* 것 (사용자 명시 답습)

- ❌ MVP-2 ~ MVP-6 deepening (수단 후보 비교 / threshold 후보 / Rollback Trigger / Evidence Required 분해)
- ❌ MVP-1 → MVP-2 진입 결정
- ❌ MVP-2 ~ MVP-6 진입 시점 결정
- ❌ MVP-2 ~ MVP-6 수단 결정 (GP-2 / GP-4 / GP-6 / G3 운영 hook / G4 Layer 3 / Layer 5 모두)
- ❌ Hermes PMO 격상 / Operational Readiness PASS / 4 게이트 일괄 PASS 선언
- ❌ 신규 ADR / 새 P / 새 GP 발행
- ❌ 17 항목 우선순위 변경
- ❌ 외부 LLM line 242 vs C-7 line 378 충돌 재해석 (C-7 답습 영구)
- ❌ Phase α-4 R-1 Stage 4 W-4 actual run trigger 영역 변경
- ❌ Phase α-4 / Stage 4 / W-1 / W-2 / W-3 / W-4 본문 변경 / 재진입
- ❌ 본 brief 자체의 합의 자동 진입 (사용자 명시 승인 후 별도 단계)
- ❌ R-1 / R-4 / R-5 / R-7 / `src/` runtime code 본문 변경
- ❌ 3 fixture / CI workflow / integration tool 본문 변경
- ❌ LVE 3/3 fixture PASS evidence 자동 재집계
- ❌ Provider Liquidity 5-way 영역 변경 / F-금지 #1 영역 변경
- ❌ Layer A / B / C / D / E / F 본문 변경 / 재발효 / 재선언

---

## 12. 다음 단계 — 사용자 결정 영역 (자동 진입 0건)

본 brief 작성 후 다음 단계 (사용자 결정 영역, 자동 진입 0건):

1. **본 brief 승인** (단계 cycle 패턴 — brief → 승인 → 합의 → commit → push)
2. **본 brief 합의 진입** (Reviewer-only 단축 합의 권고 — 본 brief = synthesis 한정 + 신규 결정 0건)
3. **Phase α-4 R-1 Stage 4 W-4 actual run 결과 확인** (`d4a0107` trigger 발효 후 결과 영역)
4. **MVP-1 → MVP-2 진입 결정** (MVP-1 exit 발효 = GP-3 5/5 + GP-5 5/5 + 사용자 명시 후)
5. **MVP-2 deepening roadmap 작성** (별도 합의 영역 — 본 brief 범위 외)
6. **본 brief 폐기** (synthesis 한정 = 영구 답습 불필요 시)

### 금지 사항 영구 답습 (다음 세션 권위 답습)

- ❌ MVP-2 ~ MVP-6 deepening 자동 진입 (별도 합의 영역)
- ❌ MVP-1 exit 자동 발효 (GP-3 5/5 + GP-5 5/5 + 사용자 명시 의무)
- ❌ 본 brief 자체의 합의 자동 진입 (사용자 명시 승인 후 별도 단계)
- ❌ Phase α-4 / Stage 4 / W-4 영역 변경
