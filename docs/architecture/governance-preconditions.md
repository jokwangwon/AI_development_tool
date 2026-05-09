# 6 Governance Preconditions (G2) — Design/Governance Gate PASS (Bundled, 2026-05-09)

> **상태: Design/Governance Gate PASS (Bundled, 2026-05-09)**. Hermes PMO 격상 4 게이트 중 G2 — "헌법 8조·5조(Provider Liquidity) 위반 경로 P1~P8 강제 메커니즘 매핑 + 6 거버넌스 사전조건 GP-1~GP-6 정의 + 각 사전조건의 entry/exit 기준" 정의. **G2 + G3 + G4 통합 풀 3+1 합의 + 외부 LLM 2건 (GPT cross-vendor + Claude 인접 컨텍스트) APPROVE WITH CONDITIONS** (`docs/review/3plus1-consensus-2026-05-09-g2g3g4-formal-promotion.md`).
>
> **PASS 범위 한정 (P0 조건 C-A, 5/5 입력 일치)**: 본 PASS 는 *Design/Governance Gate PASS* 한정 — 문서 구조 / 권위 위계 / 6 GP 정의 / 강제 메커니즘 분류 매트릭스 / Entry·Exit 기준 정의의 *설계 승인* 에 한정한다. **Implementation/Runtime PASS 는 본 PASS 에 포함되지 않는다** — GP-2~GP-6 의 PoC 실증 / CI 강제 / runtime hook 구현 / Evidence Ledger 검증은 *별도 합의* 로만 발생.
>
> **GP 별 상태 (P0 조건 C-B, 5/5 입력 일치)**:
> - **GP-1**: PASS (G1b PASS evidence 흡수, 단 Tier-1 한정 — Tier-2/Tier-3 catalog 확장은 후속, Claude C-7)
> - **GP-2 ~ GP-6**: **DESIGN PASS / IMPLEMENTATION PENDING** (각 GP 의 PoC 실증 + (a)~(e) 5조건 충족 검증은 별도 합의)
>
> **Hermes PMO 격상 / G2 운영 구현 PASS / P2 v3 정식 채택 / ADR 본문 자동 갱신 / archive 자동 처리는 본 PASS 에 포함되지 않는다** (사용자 명시 답습).

**작성일**: 2026-05-07
**정식 PASS 일자**: 2026-05-09 (Design/Governance Gate PASS, Bundled with G3 + G4)
**합의 권위**: `docs/review/3plus1-consensus-2026-05-09-g2g3g4-formal-promotion.md` (5/5 입력 APPROVE WITH CONDITIONS — Agent A/B/C 내부 + GPT cross-vendor + Claude 인접 컨텍스트)
**상위 권위**: 헌법 제8조 (보안), 프로젝트 내 관용 "헌법 제5조 (Provider Liquidity)" — 본 §1.1 명명 정정 참조
**상위 결정**: ADR-008 (Hermes 도입 Option B) 6 차단조건, ADR-011 (수단/목적 분리, §2.3 권위 위계, §2.4 T1/T2/T3)
**관련 설계**: `hermes-adoption-design-v3.md` §4 (G2 정의), `system-identity-prequel.md` §3.3 / §4.2, `redaction-pattern-equivalence.md` (R-4), `canary-recheck-design.md` (R-5), `llm-providers-design.md` (P1 v2)
**근거 합의**: `docs/review/3plus1-consensus-2026-05-05-system-identity-redefinition.md` (Agent B 6 거버넌스 사전조건 + 8 위반 경로 P1~P8 식별), `docs/review/3plus1-consensus-2026-05-09-g2g3g4-formal-promotion.md` (G2 정식 PASS 합의)
**관련 evidence**: R-2 ~ R-7 + R-6 actual run `25482284523` (G1b PASS)

---

## 0. 본 초안의 범위

### 0.1 본 초안이 *하는* 것

1. "헌법 5조 (Provider Liquidity)" 명명 정정 (프로젝트 관용 답습 + 1회 명시)
2. 헌법 8조 + Provider Liquidity 위반 경로 **P1~P8** 정의 (Agent B 합의 §29~§30 직접 기반)
3. **GP-1 ~ GP-6** 6 거버넌스 사전조건 정의 + P1~P8 매핑
4. 각 GP의 강제 메커니즘 분류 (계산적 / 추론적 / 자동 롤백) — 합의 §31 "Hermes 금지 8가지 × {계산적/추론적/자동 롤백}, 8 중 7 계산적 가능" 답습
5. 각 GP의 Entry / Exit 기준 (ADR-011 §2.1 (a)~(d) 4조건 패턴 답습 + (e) 합의 APPROVE)
6. 각 GP의 산출 후보 + 의존 ADR cross-reference 후보
7. 메타 안전장치 — 본 6 사전조건 자체의 무결성 보호 (Hermes 자기참조 차단)
8. G2 통합 entry/exit 기준 종합

### 0.2 본 초안이 *하지 않는* 것 (사용자 명시 답습)

1. ❌ **G2 PASS 선언** — 본 초안은 *정의*까지만, GP-1~GP-6 각각의 (a)~(e) Exit 기준 충족 검증은 후속
2. ❌ **G3 / G4 PASS 선언**
3. ❌ **Hermes PMO 격상 선언** — 4 게이트 모두 통과 + 사용자 명시 결정 후 별도
4. ❌ **P2 v3 정식 채택 선언** — `hermes-adoption-design-v3.md` 헤더 DRAFT 그대로 유지
5. ❌ **ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 자동 갱신** — 별도 PR 묶음
6. ❌ **P2 v2 (`hermes-adoption-design.md`) archive 처리** — v3 정식 채택 시점에
7. ❌ **`system-identity-prequel.md` archive 처리** — v3 정식 채택 시점에
8. ❌ **자동 정책 변경 (ADR-011 §2.4 T3)** — 절대 금지
9. ❌ **사전조건별 PoC 자동 실행** — 본 초안은 PoC 설계 *기준*까지, 실 PoC는 후속
10. ❌ **Tier-2 / Tier-3 catalog 확장** — 별도 합의

### 0.3 본 초안의 단계별 정식화 절차 (예정)

| # | 단계 | 산출 | 시점 |
|---|------|------|------|
| 1 | 본 초안 작성 (현 단계) | 본 문서 (DRAFT) | 2026-05-07 |
| 2 | 사용자 검토 + Reviewer-only 단축 검토 (DRAFT 적격) | 검토 보고서 | 사용자 명시 결정 후 |
| 3 | 각 GP entry 진입 + PoC 작성 + Exit 기준 (a)~(e) 충족 검증 | 6 PoC 산출 + 각 GP별 evidence | GP별 순차 또는 병행 |
| 4 | G2 PASS 합의 가동 (단축 또는 풀 3+1) | `docs/review/3plus1-consensus-YYYY-MM-DD-g2.md` | 단계 3 완료 후 |
| 5 | G2 PASS 선언 + ADR cross-reference 갱신 (G3/G4와 묶음 가능) | 별도 PR | 단계 4 후 |

본 초안 자체는 단계 1까지만 처리. 단계 2~5는 본 초안 범위 외.

---

## 1. 명명 정정 + 위반 경로 P1~P8 정의

### 1.1 "헌법 5조 (Provider Liquidity)" 명명 정정 (선행, 1회 명시)

**관용 표현**: ADR-008 / ADR-011 / system-identity-prequel / 본 v3 모두 "헌법 제5조 (Provider Liquidity)" 표현 사용.

**실제 헌법 본문**:
- `docs/constitution/PROJECT_CONSTITUTION.md` 제5조 본문: **"코드 품질 원칙"** (5개 항목, 단일 책임 / 가독성 / 중복 제거 / 외부 입력 검증 / 린터)
- 제8조 본문: 보안 원칙 (4개 항목) — 관용과 일치

**Provider Liquidity 실제 권위 출처**:
- `~/.claude/projects/.../memory/feedback_provider_liquidity.md` (사용자 비협상 메모리)
- ADR-008 본문 + 부록 A.1 (구독 교체 자유 + Hermes lock-in 차단)
- 본 프로젝트 모든 헌법-동급 제약으로 보호됨 (관용 "헌법 5조"로 인용)

**본 초안의 처리**:
- 본 초안은 **프로젝트 관용 답습** — 본문 내 "헌법 5조 (Provider Liquidity)" 표현 그대로 사용
- 단, 본 §1.1 1회 명시로 명명 불일치 인지 + 향후 *헌법 본문 갱신* 또는 *ADR-012 (가칭) Provider Liquidity 정관 흡수* 등 정정 후보 제시 (본 초안 범위 외)
- 후속 작업: 헌법 본문 갱신 또는 ADR Amendment 결정은 풀 3+1 합의 영역 (T3 변경 — ADR-011 §2.4)

### 1.2 위반 경로 P1~P8 정의

> **본 §1.2는 합의 §29~§30 (Agent B "헌법 8조·5조 위반 경로 8건 P1~P8" + B-P5/P7 cross-reference) 의 본 초안 명시 enumeration 이다.** 합의 보고서에는 P1~P8 enumeration 이 명시되지 않아 본 §1.2 가 *최초 명시* — 후속 합의 시 GP 매핑 적정성 검증 대상.

#### 1.2.1 헌법 제8조 (보안) 위반 경로 5건 (P1~P5)

| # | 경로 | 시나리오 | 헌법 8조 어느 항 | G1b 와 관계 |
|---|------|---------|--------------|----------|
| **P1** | **DB INSERT 평문 secret 누적** | Worker Agent 가 LLM 응답·환경변수 echo·tool output 을 SessionDB / Memory DB / Skill DB 에 INSERT 시 평문 secret 영구 저장 | 8조 #1 (하드코딩 차단) + 8조 #2 (비밀 관리) | **G1b PASS 로 차단** (SQLCipher trigger + Tier-1 42 catalog) |
| **P2** | **로그/LLM 송신 경로 평문 노출** | Hermes / Worker 가 secret 을 stdout / stderr / log file / LLM API request body 에 노출 | 8조 #2 | Hermes native redaction 보조 (ADR-011 §2.3 운영 함의 #2) |
| **P3** | **Credential / OAuth 파일 권한 노출** | API 키 파일 / OAuth credentials 파일이 world-readable / docker socket mount / inotify 미감시 | 8조 #2 | ADR-008 §2.6.4 R1-2 + entrypoint stat 검증 |
| **P4** | **비밀값 하드코딩** | secret 이 git commit 본문 / 환경변수 default / docker-compose.yml 평문 / Skill 정의 평문 등에 영구 기록 | 8조 #1 (직접) | gitleaks / detect-secrets / pre-commit hook |
| **P5** | **외부 입력 미검증/이스케이프** | Worker Agent 또는 Hermes 출력이 *내부* 처럼 취급되어 SQL injection / command injection / path traversal 등 발생 | 8조 #3 (직접) | **헌법 8조 #4 — 보안 변경은 3+1 합의** + 헌법 5조 #4 (외부 입력 검증) |

#### 1.2.2 Provider Liquidity (관용 헌법 5조) 위반 경로 3건 (P6~P8)

| # | 경로 | 시나리오 | Provider Liquidity 어느 측면 | 관련 ADR-008 차단조건 |
|---|------|---------|--------------------------|------------------|
| **P6** | **Hermes 자체 SDK 직접 import** | Worker Agent / Skill / Hermes plugin 코드가 `import hermes_agent.*` 또는 `import litellm` 직접 import 로 P1 facade 우회 | Provider 교체 자유 (코드 변경 없이) | **차단조건 #4** (provider 어댑터 추상화) |
| **P7** | **모델명/Provider 분기 코드** | `if model == "claude-opus-4-7": ... elif model == "gpt-5.5": ...` 또는 provider 별 후처리 분기 / Skill 내 모델 가정 (ADR-008 §결과 §주의사항 6종) | Provider 교체 자유 (코드 변경 없이) | **차단조건 #4** (P1 v2 depcruise 룰) |
| **P8** | **Memory / Skill Hermes 종속 형식** | Skill 정의 / Memory entry 가 Hermes 자체 schema (binary protocol / proprietary key) 사용으로 다른 오케스트레이터 import 불가 | Provider 교체 자유 (학습 자산 유지) | **차단조건 #2** (JSONL export) + **G4** (Provider-agnostic Memory/Skill 형식) |

#### 1.2.3 P1~P8 합산

```
헌법 8조 (보안) 위반 경로 = 5건 (P1~P5)
Provider Liquidity 위반 경로 = 3건 (P6~P8)
합계 = 8건 (P1~P8)  ✅ 합의 §29~§30 일치
```

#### 1.2.4 본 §1.2 가 *다루지 않는* 위반 경로

본 §1.2는 *헌법 8조 + Provider Liquidity* 위반 경로에 한정. 다음은 본 G2 범위 외:
- 헌법 1조 (SDD) / 2조 (TDD) 위반 — 일반 Harness Layer 1~4 hook 가 다룸
- 헌법 4조 (3+1 합의) 위반 — Layer 5 + 사용자 결정
- 헌법 7조 (투명성) 위반 — Layer 0 (CLAUDE.md) + ADR 절차
- 헌법 10조 (문서 일관성) 위반 — `docs/INDEX.md` + 의존 관계 매트릭스
- ADR-011 §2.4 T3 (자동 정책 변경) 위반 자체 — **G3** ("Hermes ≠ root of trust" 운영 구현) 범위. 본 G2 §9 메타 안전장치에서 *interface*만 명시

---

## 2. 6 거버넌스 사전조건 (GP-1 ~ GP-6) 정의 + 매핑

### 2.1 GP 정의 + P1~P8 매핑 매트릭스

| GP | 명칭 | 위반 경로 | 핵심 강제 메커니즘 | 관련 G* / ADR |
|----|------|---------|----------------|-------------|
| **GP-1** | DB-level Secret Persistence 차단 | P1 | SQLCipher BEFORE INSERT trigger + REGEXP UDF + Tier-1 42 catalog | G1b PASS (이미 충족) + ADR-011 §2.1 |
| **GP-2** | Egress Redaction (로그/LLM 송신) | P2 | Hermes native redaction (보조 — ADR-011 §2.3 #2) + LLM facade redaction filter (P1) | ADR-008 차단조건 #1 보조 + ADR-011 §2.3 |
| **GP-3** | Credential / Secret Hygiene (저장 + 코드) | P3, P4 | (저장) docker secret + chmod 600 + entrypoint stat + inotify, (코드) gitleaks / detect-secrets pre-commit hook + CI step | ADR-008 §2.6.4 R1-2 + R2-1 + 헌법 8조 #1 |
| **GP-4** | 외부 입력 검증 (Hermes/Worker 출력 포함) | P5 | Hermes / Worker Agent 출력을 *외부 입력*으로 분류 + 검증 layer 강제 (헌법 5조 #4 + 8조 #3) | ADR-011 §2.3 운영 함의 #1 (Tools verify Hermes 출력) |
| **GP-5** | Provider Adapter 강제 (코드 레벨 lock-in 차단) | P6, P7 | depcruise 룰 정적 차단 + P1 facade 단일 진입점 + 분기 코드 PR 자동 reject | ADR-008 차단조건 #4 + P1 v2 |
| **GP-6** | Memory / Skill Migration 가능성 (학습 자산 lock-in 차단) | P8 | JSONL append-only 표준 + 변환 스크립트 (Hermes ↔ Claude / GPT) 1회 시연 (R2-5 답습) | ADR-008 차단조건 #2 + **G4** (depend) |

### 2.2 강제 메커니즘 분류 매트릭스 (계산적 / 추론적 / 자동 롤백)

> **합의 §31 답습**: "Hermes 금지 8가지 × {계산적/추론적/자동 롤백}, 8 중 7 계산적 가능". 본 §2.2 는 6 GP 각각에 동일 분류 적용.

| GP | 계산적 (Computational) | 추론적 (Inferential) | 자동 롤백 (Auto Rollback) |
|----|---------------------|------------------|----------------------|
| GP-1 | ✅ Tier-1 42 trigger UDF + R-6 actual run regex test | ⚠️ 보조 (LLM 기반 sensitive content 감지 — 본 G2 범위 외) | ✅ ROLLBACK trigger R1~R3 (R-7 SOP §5) |
| GP-2 | ✅ test_redaction.py + base64 evasion test (R2-6) | ⚠️ 보조 | ✅ ROLLBACK trigger R5 (Hermes 학습 평문 검출) |
| GP-3 | ✅ gitleaks / detect-secrets / chmod check / entrypoint stat | ❌ 추론 불필요 | ✅ inotify 감시 즉시 컨테이너 정지 (R1-2) |
| GP-4 | ✅ 입력 schema validation + regex sanitizer + 명시 escape | ✅ 보조 (LLM 기반 prompt injection 감지 — Reviewer Agent) | ✅ Worker 출력 검증 실패 시 BLOCK |
| GP-5 | ✅ depcruise 정적 분석 + PR auto-reject | ❌ 추론 불필요 | ✅ depcruise 위반 PR auto-reject (CI 강제) |
| GP-6 | ✅ JSONL schema 검증 + 변환 스크립트 자동 테스트 | ⚠️ 보조 (다른 오케스트레이터 import 검증 — 부분 추론) | ✅ schema_version 호환 실패 시 export 차단 |

**합산**:
- 계산적 가능: 6/6 (모든 GP 가 계산적 우선 가능)
- 추론적 보조: 4/6 (GP-1, GP-2, GP-4, GP-6)
- 자동 롤백: 6/6 (모든 GP 가 자동 롤백 경로 명시)

→ "8 중 7 계산적 가능" 보다 본 6 GP 분류는 **6/6 계산적 가능** — 합의 §31 보다 계산적 비중 높음. 사유: 본 6 GP 는 *Path-level (P1~P8)* 보다 *Enforcement-level* 추상화로 계산적 메커니즘 집계 가능.

---

## 3. GP-1 — DB-level Secret Persistence 차단

### 3.1 정의

DB INSERT 경로 (SessionDB / Memory DB / Skill DB) 에 평문 secret 이 영구 저장되지 않도록 SQLCipher BEFORE INSERT trigger + REGEXP UDF 가 모든 INSERT 를 사전 검사하여 secret 패턴 일치 시 reject 한다.

### 3.2 위반 경로

- **P1** — DB INSERT 평문 secret 누적

### 3.3 강제 메커니즘

| 분류 | 메커니즘 | 위치 |
|-----|---------|-----|
| 계산적 | SQLCipher BEFORE INSERT trigger + REGEXP UDF + Tier-1 42 catalog | DB layer |
| 계산적 | R-2 PoC 6 자동 검증 항목 (C1~C6) | `docker/r2-poc/` |
| 계산적 | R-4.1 Tier-1 42 trigger UDF 격리 PoC | `docker/r4-1-poc/` |
| 자동 회귀 | R-6 GitHub Actions workflow (push/PR/nightly) | `.github/workflows/r2-canary.yml` |
| 자동 롤백 | R-7 SOP §5 ROLLBACK trigger R1~R3 | `docs/phase0/redaction-verification-sop.md` |

### 3.4 Entry 기준

- ✅ G1b PASS (2026-05-07, 이미 충족)
- ⏳ 사용자 명시 GP-1 작업 진입 결정 (단, GP-1 은 G1b PASS 로 대부분 이미 충족)

### 3.5 Exit 기준

> 본 GP-1 은 **G1b PASS 의 직접 흡수** — Exit (a)~(e) 5조건이 G1b 승격 시점에 모두 충족된 상태. 본 §3.5 는 그 *증거 cross-reference* 만 명시.

| # | 조건 | 충족 evidence |
|---|------|------------|
| (a) | 동등 이상의 보안 결과 | R-4 redaction-pattern-equivalence.md (3-way 비교 + Tier-1 42 gap 식별) |
| (b) | 격리 환경 PoC 실증 | R-2 (`docker/r2-poc/`) + R-4.1 (`docker/r4-1-poc/`) |
| (c) | ADR / SDD 권위 명시 | ADR-011 §2.1 + ADR-008 부록 B Amendment |
| (d) | 자동 회귀 검증 경로 확보 | R-6 actual run `25482284523` PASS (24초, 42/42, leak 0) |
| (e) | 합의 APPROVE | R-7 SOP §7.3 단축 합의 (Reviewer-only) `3plus1-consensus-2026-05-07-g1b-phase1-acceptance.md` |

### 3.6 산출 후보 (보강 — 본 GP-1 범위 *내*)

본 GP-1 은 G1b 흡수이므로 *추가 산출 0건*. 단, G2 통합 검증 시점에 **본 §3 자체를 G1b cross-reference 형태로 합의 보고서에 인용** — 이중 보호.

### 3.7 의존 ADR / 갱신 후보

- ADR-011 §2.1: 본문 변경 없음, §8.5 후속 작업에 G2 GP-1 흡수 등록 (G2 PASS 시점)
- ADR-008 부록 B: 본문 변경 없음, B.6 결과를 G2 GP-1 cross-reference 추가 (G2 PASS 시점)

---

## 4. GP-2 — Egress Redaction (로그/LLM 송신)

### 4.1 정의

Hermes / Worker Agent 가 stdout / stderr / log file / LLM API request body 에 secret 을 노출하지 않도록 native redaction (`agent/redact.py`) + LLM facade redaction filter (P1 v2 §8.2) 가 사전 차단한다.

**중요**: GP-2 는 ADR-011 §2.3 운영 함의 #2 의 *보조* 역할. **DB INSERT 차단은 GP-1 의 책임이며, GP-2 는 송신/로그 경로만 다룸**. GP-2 단독으로 헌법 8조 본질 충족 시도 금지.

### 4.2 위반 경로

- **P2** — 로그/LLM 송신 경로 평문 노출

### 4.3 강제 메커니즘

| 분류 | 메커니즘 | 위치 |
|-----|---------|-----|
| 계산적 | Hermes native redaction `agent/redact.py` (Tier-1 catalog 적용) | Hermes container |
| 계산적 | P1 v2 LLM facade RedactionFilter | P1 facade layer |
| 계산적 | base64 evasion test (R2-6) | `tests/hermes/redaction/test_base64_evasion.py` |
| 계산적 | log file grep canary 자동 검증 | CI step (R-6 확장) |
| 자동 회귀 | Hermes 의존성 업그레이드 시 R-2 / R-4.1 PoC 자동 재실행 (ADR-011 §2.3 운영 함의 #4) | R-6 workflow trigger 확장 |
| 자동 롤백 | R-7 SOP §5 ROLLBACK trigger R5 (Hermes 학습 평문 검출) | R-7 SOP |

### 4.4 Entry 기준

- ✅ R-4 pattern equivalence 작성 완료 (충족됨)
- ✅ Hermes native redaction `agent/redact.py` 존재 확인 (R-1 Day 2 evidence)
- ⏳ 사용자 명시 GP-2 작업 진입 결정

### 4.5 Exit 기준

| # | 조건 | 검증 방식 |
|---|------|---------|
| (a) | 동등 이상의 보안 결과 | Hermes native redaction Tier-1 42 catalog 적용 검증 + P1 facade redaction filter 검증 |
| (b) | 격리 환경 PoC 실증 | log file canary inject + grep 검증 PoC (Docker 격리) |
| (c) | ADR / SDD 권위 명시 | ADR-011 §2.3 운영 함의 #2 cross-reference + 본 §4 권위 |
| (d) | 자동 회귀 검증 경로 확보 | R-6 workflow 에 log file canary inject step 추가 |
| (e) | 합의 APPROVE | 단축 또는 풀 3+1 합의 (G2 GP-2 한정 또는 G2 통합) |

### 4.6 산출 후보

- `tests/hermes/redaction/test_log_canary.py` (log file inject + grep)
- R-6 workflow 확장 — log file canary inject step
- 합의 보고서

### 4.7 의존 ADR / 갱신 후보

- ADR-011 §2.3: 본문 변경 없음, §8.5 후속 작업에 GP-2 산출 등록 (G2 PASS 시점)
- ADR-008 차단조건 #1 보조 메커니즘 cross-reference

---

## 5. GP-3 — Credential / Secret Hygiene (저장 + 코드)

### 5.1 정의

API 키 / OAuth credentials 의 *저장 경로* (런타임) 와 *코드 본문* (개발/배포 시점) 양쪽에서 secret 노출이 차단된다.

- **저장 경로** (P3): docker secret + chmod 600 + entrypoint stat 검증 + inotify 런타임 감시
- **코드 본문** (P4): pre-commit hook (gitleaks / detect-secrets) + CI step + PR auto-reject

### 5.2 위반 경로

- **P3** — Credential / OAuth 파일 권한 노출
- **P4** — 비밀값 하드코딩

### 5.3 강제 메커니즘

| 분류 | 메커니즘 | 위치 |
|-----|---------|-----|
| 계산적 | docker secret 정의 (R2-1) | `docker-compose.yml` (ADR-008 §2.6.2) |
| 계산적 | chmod 600 강제 + entrypoint stat 검증 (R1-2) | Hermes Dockerfile entrypoint |
| 계산적 | inotify 런타임 감시 (mtime/perm 변경 → 컨테이너 정지) | Hermes runtime |
| 계산적 | gitleaks / detect-secrets pre-commit hook | git pre-commit |
| 계산적 | PR auto-reject CI step (gitleaks --no-git) | GitHub Actions |
| 자동 롤백 | inotify 감시 hit → 컨테이너 정지 (R1-2) | Hermes runtime |
| 자동 롤백 | pre-commit hook 차단 → commit reject | git layer |

### 5.4 Entry 기준

- ✅ ADR-008 §2.6.4 R1-2 (OAuth credentials 처리 강화) 명시 (충족됨)
- ✅ 헌법 8조 #1 (하드코딩 금지) 권위 (충족됨)
- ⏳ 사용자 명시 GP-3 작업 진입 결정

### 5.5 Exit 기준

| # | 조건 | 검증 방식 |
|---|------|---------|
| (a) | 동등 이상의 보안 결과 | (저장) docker secret + chmod 600 + inotify 동작 확인, (코드) gitleaks / detect-secrets 회귀 0건 |
| (b) | 격리 환경 PoC 실증 | (저장) docker secret 누락 / chmod 644 / mtime 변경 → 컨테이너 정지 시연, (코드) 의도적 secret hardcode → pre-commit reject 시연 |
| (c) | ADR / SDD 권위 명시 | ADR-008 §2.6.4 R1-2 + 헌법 8조 #1 + 본 §5 |
| (d) | 자동 회귀 검증 경로 확보 | CI step 추가 (gitleaks --no-git in PR) + entrypoint stat 검증 매 컨테이너 시작 시 강제 |
| (e) | 합의 APPROVE | 단축 또는 풀 3+1 합의 (G2 GP-3 한정 또는 G2 통합) |

### 5.6 산출 후보

- `.github/workflows/secret-scan.yml` (gitleaks PR step) 또는 R-6 workflow 통합
- `.pre-commit-config.yaml` (gitleaks / detect-secrets hook)
- Hermes Dockerfile entrypoint stat 검증 step
- inotify 감시 사이드카 또는 entrypoint script
- PoC 산출 (저장 / 코드 양쪽 시연)
- 합의 보고서

### 5.7 의존 ADR / 갱신 후보

- ADR-008 §2.6.4 R1-2: 본문 변경 없음, GP-3 cross-reference 추가
- 헌법 8조: 본문 변경 없음 (T3 — ADR Amendment 절차 영역, 본 G2 범위 외)

---

## 6. GP-4 — 외부 입력 검증 (Hermes / Worker 출력 포함)

### 6.1 정의

Hermes 출력 + Worker Agent 출력 + LLM 응답 + tool output 모두를 *외부 입력*으로 분류하여 명시 검증 layer 를 거친다. ADR-011 §2.3 운영 함의 #1 ("Hermes 출력은 Tools 로 검증된다") 의 *입력 검증 측면* 구체화.

**중요**: GP-4 는 헌법 8조 #3 (사용자 입력 검증) 의 *내부 출력 적용* 확장. Hermes / Worker 가 *내부* 처럼 신뢰되어 SQL injection / command injection / path traversal 등이 발생하지 않도록.

### 6.2 위반 경로

- **P5** — 외부 입력 미검증/이스케이프

### 6.3 강제 메커니즘

| 분류 | 메커니즘 | 위치 |
|-----|---------|-----|
| 계산적 | 입력 schema validation (pydantic / typing) | Worker Agent 입출력 인터페이스 |
| 계산적 | regex sanitizer + escape (path traversal / SQL / command) | tool wrapper layer |
| 계산적 | 명시 quote / parameterize (SQL bind variable, shlex.quote) | DB / shell tool layer |
| 추론적 보조 | Reviewer Agent 의 prompt injection 감지 | Layer 5 (3+1 합의) |
| 자동 롤백 | 검증 실패 → BLOCK + Evidence Ledger 기록 | Worker Agent runtime |

### 6.4 Entry 기준

- ✅ 헌법 8조 #3 (외부 입력 검증) 권위 (충족됨)
- ✅ 헌법 5조 #4 (코드 품질 — 외부 입력만 검증) 명시 (충족됨)
- ⏳ 사용자 명시 GP-4 작업 진입 결정

### 6.5 Exit 기준

| # | 조건 | 검증 방식 |
|---|------|---------|
| (a) | 동등 이상의 보안 결과 | Hermes / Worker 출력 sanitizer 통과 검증 + 의도적 injection payload 차단 시연 |
| (b) | 격리 환경 PoC 실증 | path traversal payload + SQL bind 우회 payload + command injection payload → 모두 BLOCK 격리 환경 시연 |
| (c) | ADR / SDD 권위 명시 | ADR-011 §2.3 운영 함의 #1 + 헌법 8조 #3 + 헌법 5조 #4 + 본 §6 |
| (d) | 자동 회귀 검증 경로 확보 | CI step + injection canary 자동 회귀 (R-6 workflow 확장) |
| (e) | 합의 APPROVE | 단축 또는 풀 3+1 합의 (G2 GP-4 한정 또는 G2 통합) |

### 6.6 산출 후보

- `tests/integration/test_input_validation.py` (injection canary)
- Worker Agent / tool wrapper 입출력 schema 정의 (pydantic)
- R-6 workflow 확장 — injection canary step
- 합의 보고서

### 6.7 의존 ADR / 갱신 후보

- ADR-011 §2.3 운영 함의 #1 cross-reference
- ADR-008 본문: GP-4 cross-reference (격상 후)

---

## 7. GP-5 — Provider Adapter 강제 (코드 레벨 lock-in 차단)

### 7.1 정의

Worker Agent / Skill / Hermes plugin 코드가 Hermes 자체 SDK / litellm / anthropic / openai 직접 import 또는 모델명 / Provider 분기 코드를 포함하지 않도록 depcruise 룰 + P1 facade 단일 진입점 + PR auto-reject 가 정적으로 강제한다.

### 7.2 위반 경로

- **P6** — Hermes 자체 SDK 직접 import
- **P7** — 모델명 / Provider 분기 코드

### 7.3 강제 메커니즘

| 분류 | 메커니즘 | 위치 |
|-----|---------|-----|
| 계산적 | depcruise 룰 — Hermes / litellm / anthropic / openai 직접 import 금지 | `.dependency-cruiser.cjs` |
| 계산적 | depcruise 룰 — 모델명 분기 패턴 정적 차단 (`model == "claude"` 등) | depcruise custom rule |
| 계산적 | P1 facade 단일 진입점 강제 (`src/llm/facade.py` 외 LLM 호출 금지) | P1 v2 |
| 자동 롤백 | depcruise 위반 PR → CI step FAIL → auto-reject | GitHub Actions |
| 자동 롤백 | 인위적 분기 코드 PR → depcruise FAIL 확인 (ADR-008 §2.4 검증 #2) | CI step |

### 7.4 Entry 기준

- ✅ ADR-008 차단조건 #4 명시 (충족됨)
- ⏳ P1 v2 facade MVP 완료 (P1 v2 §X — 본 G2 범위 외, 의존)
- ⏳ 사용자 명시 GP-5 작업 진입 결정

### 7.5 Exit 기준

| # | 조건 | 검증 방식 |
|---|------|---------|
| (a) | 동등 이상의 보안 결과 | (Provider Liquidity 측면) Hermes / litellm / anthropic / openai 직접 import 0건 + 모델명 분기 0건 |
| (b) | 격리 환경 PoC 실증 | 인위적 분기 코드 PR → depcruise FAIL 확인 시연 |
| (c) | ADR / SDD 권위 명시 | ADR-008 차단조건 #4 + P1 v2 + 본 §7 |
| (d) | 자동 회귀 검증 경로 확보 | CI step (depcruise) + PR auto-reject 매 PR 강제 |
| (e) | 합의 APPROVE | 단축 또는 풀 3+1 합의 (G2 GP-5 한정 또는 G2 통합) |

### 7.6 산출 후보

- `.dependency-cruiser.cjs` (Hermes / LLM SDK 직접 import 금지 룰 + 모델명 분기 패턴 차단 룰)
- P1 v2 facade MVP (본 GP-5 의존 — P1 작업과 통합)
- CI step (depcruise + 인위적 분기 코드 PR 시연)
- 합의 보고서

### 7.7 의존 ADR / 갱신 후보

- ADR-008 차단조건 #4: 본문 변경 없음, GP-5 cross-reference 추가
- ADR-009 (자체 Adapter v2.0 진입조건): GP-5 충족과 자체 Adapter 진입의 관계 갱신 (격상 후)
- P1 v2 (`llm-providers-design.md`): facade 단일 진입점 권위 cross-reference

---

## 8. GP-6 — Memory / Skill Migration 가능성 (학습 자산 lock-in 차단)

### 8.1 정의

Hermes 가 누적한 Memory / Skill 이 Hermes 의존 schema / binary protocol 에 종속되지 않도록 JSONL append-only 표준 + 변환 스크립트 (Hermes ↔ Claude Code / GPT 등) 1회 시연이 보장된다.

**중요**: GP-6 은 **G4** (Provider-agnostic Memory/Skill 형식) 와 *공동 책임* — GP-6 은 *마이그레이션 가능성* 측면, G4 는 *형식 표준화* 측면. 둘은 동일 검증 산출 일부 공유 가능.

### 8.2 위반 경로

- **P8** — Memory / Skill Hermes 종속 형식

### 8.3 강제 메커니즘

| 분류 | 메커니즘 | 위치 |
|-----|---------|-----|
| 계산적 | JSONL schema 검증 (jq 파싱 + schema_version 체크) | export script |
| 계산적 | 변환 스크립트 자동 테스트 (Hermes JSONL → Claude / GPT format) | `scripts/hermes-migration/` + CI step |
| 계산적 | hermes sessions export → import 라운드트립 검증 | `tests/hermes/test_export_import.py` |
| 추론적 보조 | 다른 오케스트레이터 import 결과 의미 보존 검증 (부분 추론) | manual review (분기 1회) |
| 자동 롤백 | schema_version 호환 실패 → export 차단 | export script |

### 8.4 Entry 기준

- ✅ ADR-008 차단조건 #2 (JSONL export 표준) 명시 (충족됨)
- ✅ ADR-008 부록 A.2 (Hermes sessions export 공식 명령 검증) (충족됨)
- ⏳ G4 작업 진입 또는 병행 (본 §8 은 *마이그레이션 가능성* 측면, G4 는 *형식 표준화* 측면)
- ⏳ 사용자 명시 GP-6 작업 진입 결정

### 8.5 Exit 기준

| # | 조건 | 검증 방식 |
|---|------|---------|
| (a) | 동등 이상의 보안 결과 | (Provider Liquidity 측면) Hermes lock-in 차단 — 다른 오케스트레이터로 학습 자산 import 가능 |
| (b) | 격리 환경 PoC 실증 | hermes sessions export → claude_to_hermes / hermes_to_gpt 변환 → 다른 오케스트레이터 import → 의미 보존 검증 (R2-5 답습) |
| (c) | ADR / SDD 권위 명시 | ADR-008 차단조건 #2 + G4 cross-reference + 본 §8 |
| (d) | 자동 회귀 검증 경로 확보 | CI step (export → 변환 → schema 검증) + Hermes 메이저 업데이트 시점 자동 회귀 |
| (e) | 합의 APPROVE | 단축 또는 풀 3+1 합의 (G2 GP-6 + G4 통합 가능) |

### 8.6 산출 후보

- `scripts/hermes-migration/hermes_to_claude.py` (변환 스크립트, R2-5 답습)
- `scripts/hermes-migration/hermes_to_gpt.py`
- `tests/hermes/test_export_import.py` (라운드트립 검증)
- CI step (export → 변환 → schema 검증)
- 합의 보고서 (G4 와 통합 가능)

### 8.7 의존 ADR / 갱신 후보

- ADR-008 차단조건 #2: 본문 변경 없음, GP-6 + G4 cross-reference 추가
- ADR-009 (자체 Adapter v2.0 진입조건): GP-6 / G4 충족과 자체 Adapter 진입의 관계 갱신
- 신규 ADR 후보 (P2 v3 §6.7 등록): ADR-014 (Provider-agnostic Memory/Skill Format) — G4 통합 시점

---

## 9. 메타 안전장치 — Hermes 자기참조 차단

### 9.1 문제 정의

본 6 거버넌스 사전조건이 Hermes 자체에 의해 *변경* 또는 *우회* 될 수 있다면, GP-1 ~ GP-6 의 권위는 무력화된다 — *fox guarding the henhouse* 문제. 따라서 본 §9 는 6 GP 자체의 *무결성* 을 보호한다.

### 9.2 강제 메커니즘 (G3 와의 인터페이스)

> **본 §9 는 강제 메커니즘 *interface* 만 명시**. 본격적인 운영 구현은 **G3 ("Hermes ≠ root of trust" 운영 구현)** 범위 — 본 G2 는 *interface* 까지.

| # | 메커니즘 | 권위 근거 | G3 위치 |
|---|---------|--------|--------|
| 1 | filesystem read-only on `docs/architecture/governance-preconditions.md` (Hermes container mount ro) | ADR-011 §2.4 T3 + system-identity-prequel §3.3 #1 | G3 §5.2 #5 |
| 2 | 본 문서 변경은 *git commit* 으로만 권위 인정 (Hermes-originated commit auto-reject) | system-identity-prequel §3.3 #2 + G3 §5.5 (합의 인프라 순환 권위 해결) | G3 §5.5 |
| 3 | 본 문서 변경의 audit log (Hermes-originated 변경 시 별도 로그) | system-identity-prequel §3.3 #3 | G3 §5.2 #5 |
| 4 | T3 변경 감지 hook → 자동 reject + 사용자 alert | ADR-011 §2.4 T3 | G3 §5.2 #5 |

### 9.3 본 §9 가 *하지 않는* 것

- ❌ G3 운영 구현 (본 §9 는 interface 까지)
- ❌ 합의 인프라 순환 권위 해결의 본문 (G3 §5.5 위임)
- ❌ Hermes-originated commit 자동 reject 의 구현 (G3 산출)

### 9.4 본 §9 가 *지금 강제하는* 것 (DRAFT 상태에서도)

본 초안 자체에 다음을 *즉시 강제*:

1. 본 문서 변경은 사용자 명시 결정 + git commit 만 권위 인정
2. Hermes 또는 Worker Agent 가 본 문서 본문 자동 변경 시도 시 *자동 reject* 권위 (현 시점 hook 미구현 — 사용자 검토에 의존)
3. 본 §9 자체의 변경은 **풀 3+1 합의 + ADR Amendment 절차** (T3 변경)
4. 본 §9 가 본 G2 PASS 의 *전제* — §9 미충족 시 G2 PASS 불가

---

## 10. G2 통합 Entry / Exit 기준 종합

### 10.1 G2 통합 Entry

- ✅ G1b PASS (2026-05-07, 충족됨)
- ✅ ADR-011 §2.3 권위 확정 (2026-05-06, 충족됨)
- ⏳ 사용자 명시 G2 작업 진입 결정

### 10.2 G2 통합 Exit (모든 GP 충족 + 메타 안전장치 인터페이스)

| GP | Exit (a)~(e) | 현 상태 |
|----|------------|------|
| GP-1 | (a)~(e) 모두 G1b PASS evidence 로 충족 (§3.5) | ✅ 본 초안 정식 채택 시 흡수 가능 |
| GP-2 | (a)~(e) 미충족 — PoC + 합의 필요 | ⏳ |
| GP-3 | (a)~(e) 미충족 — PoC + 합의 필요 | ⏳ |
| GP-4 | (a)~(e) 미충족 — PoC + 합의 필요 | ⏳ |
| GP-5 | (a)~(e) 미충족 — P1 v2 facade MVP 의존 + PoC + 합의 필요 | ⏳ |
| GP-6 | (a)~(e) 미충족 — G4 와 공동 진행 가능, PoC + 합의 필요 | ⏳ |
| §9 메타 안전장치 | interface 명시 완료 (본 §9), 본격 운영 구현은 G3 범위 | 🟡 (interface 한정) |

**G2 PASS 조건**:
- GP-1 ~ GP-6 모든 (a)~(e) 충족
- §9 메타 안전장치 interface 명시 + G3 작업 동시 진입 (또는 G3 PASS 후)
- 합의 보고서 (단축 또는 풀 3+1) APPROVE

**G2 PASS 합의 형태**:
- 옵션 1: GP-1 ~ GP-6 각각 별도 단축 합의 (Reviewer-only) → 6 합의 보고서 + G2 통합 단축 합의 1건
- 옵션 2: GP-1 ~ GP-6 통합 풀 3+1 합의 1건
- 옵션 3: GP-1 ~ GP-6 + G3 + G4 통합 풀 3+1 합의 1건 (PR 묶음)

**권고 형태** (사용자 결정 후보, 본 초안은 *권고 단정 금지*): 옵션 3 — G2/G3/G4 통합 풀 3+1 합의가 PR 묶음 + 메타 안전장치 (§9) 의 G3 의존성 감안 시 비용 효율적. 단, 옵션 1 / 2 도 사용자 결정 시 정당.

### 10.3 G2 통합 Exit *선언* 절차 (사용자 명시 답습)

본 G2 PASS 합의 APPROVE 시점에 다음이 *발생*:
- ✅ G2 status: 미작성 → PASS (CONTEXT.md 4 게이트 진행 상태 갱신)
- ✅ 본 문서 헤더 "DRAFT" 제거 + 합의 보고서 cross-reference 추가
- ✅ ADR-008 / ADR-011 cross-reference 갱신 (별도 PR)

본 G2 PASS 합의 APPROVE 시점에 *발생하지 않는* 것:
- ❌ G3 / G4 자동 PASS
- ❌ Hermes PMO 격상 자동 활성화
- ❌ P2 v3 정식 채택 자동
- ❌ system-identity-prequel.md / P2 v2 자동 archive

---

## 11. 영구 핵심 제약 (변동 없음)

본 G2 작업 + G2 PASS + Hermes PMO 격상(미래) 전 과정에서 다음은 **무조건 영구 유지**:

| 제약 | 권위 근거 |
|------|---------|
| **Provider Liquidity** | 헌법 제5조 (관용) + `feedback_provider_liquidity.md` + ADR-008 본문 |
| **Hermes ≠ root of trust** | ADR-011 §2.3 (영구 권위) |
| **메타포 강제 금지** | system-identity-prequel §7 (P2 v3 §10 흡수) |
| **자동 정책 변경 금지 (T3)** | ADR-011 §2.4 |
| **수단/목적 분리 원칙** | ADR-011 §2.1 (a)~(d) 4조건 → 본 §3~§8 Exit 기준 (a)~(e) 패턴 답습 |

본 5건 제약은 본 §9 메타 안전장치로 *추가* 보호 — 6 GP 자체의 무결성과 동시 보호.

---

## 12. 본 초안의 변경 절차

본 G2 거버넌스 사전조건 초안은 DRAFT 상태에서 다음 절차를 따른다:

| 변경 유형 | 절차 |
|---------|------|
| 단순 오타 / 문구 정리 | 사용자 단독 결정 가능 |
| §1.2 P1~P8 정의 본문 갱신 | 사용자 명시 결정 + Reviewer-only 단축 검토 |
| §2 ~ §8 GP-1 ~ GP-6 본문 갱신 | 단축 합의 (Reviewer-only) |
| §9 메타 안전장치 본문 갱신 | **풀 3+1 합의 + ADR Amendment 절차** (T3 변경 — 매우 신중) |
| **DRAFT 상태 해제 → 정식 채택** | **단축 합의 또는 풀 3+1 합의 APPROVE** + 각 GP (a)~(e) Exit 기준 충족 검증 |
| §11 영구 핵심 제약 변경 | **풀 3+1 합의 + ADR Amendment 절차** (T3 변경 — 매우 신중) |

---

## 13. 본 초안의 메타 편향 자기진단

본 초안은 다음 5 통제 수단을 명시 답습한다:

1. **사용자 명시 절차 답습**: G2 PASS 선언 / G3 / G4 PASS 선언 / Hermes PMO 격상 / P2 v3 정식 채택 / ADR 본문 갱신 / archive 처리 모두 본 초안 범위 외 (§0.2).
2. **R-7 SOP §0 핵심 선언 답습**: 각 GP Exit 기준 (a)~(e) 5조건은 ADR-011 §2.1 (a)~(d) 4조건 + 합의 APPROVE (e) 패턴 답습 — 본 초안이 새 권위 구조 트리거하지 않음.
3. **ADR-011 §2.4 T1/T2/T3 답습**: 본 §3~§8 산출 후보는 모두 사용자 명시 결정 (T2) 후 진입. §9 메타 안전장치는 T3 변경 절차 명시.
4. **수단/목적 분리 원칙 답습**: §1.1 ("헌법 5조 (Provider Liquidity)" 명명 정정) + §2.2 (계산적 우선 분류) + 각 GP 강제 메커니즘 표 모두 *본질=결과* 우선, *수단*은 (a)~(e) 검증 후 채택.
5. **본 초안이 *하지 않는* 것 명시 (§0.2 + §10.3)**: 10건 명시 부정.

본 5 통제는 P2 v3 DRAFT 검토 5 통제 + G1b PASS 단축 합의 5 통제 답습 — G2 → G3 → G4 → Hermes PMO 격상 전 과정 동일 패턴 유지.

### 13.1 본 초안의 메타 한계

- 본 초안은 *자기 작성 산출* (P2 v3 와 동일 컨텍스트). 외부 Reviewer 검토는 본 초안 대체 불가.
- §1.2 P1~P8 enumeration 은 *최초 명시* — 합의 §29~§30 의 Agent B 원안은 enumeration 없음. 본 §1.2 가 P1~P8 의 *원안* 으로 권위화되려면 후속 합의 검증 필요.
- §2.1 6 GP 매핑은 본 초안 *원안* — 합의 §164 ("B의 6 거버넌스 사전조건 전건 채택") 의 6 항목 enumeration 도 합의 보고서에 명시되지 않아, 본 §2.1 이 *6 항목의 원안*. 후속 합의에서 GP 분류 / 매핑 적정성 검증 대상.

### 13.2 본 초안의 *PASS 판정 트리거하지 않는 것*

본 초안은 G2 PASS 판정을 *준비* 만 하며 *발생시키지 않는다*. 다음 모두 본 초안 범위 외:
- ❌ G2 PASS 선언
- ❌ Hermes PMO 격상
- ❌ G3 / G4 PASS 선언
- ❌ ADR-008/009/010/011 갱신
- ❌ P2 v2 / prequel archive
- ❌ INDEX / CONTEXT 갱신
- ❌ Phase 진입 결정
- ❌ Tier-2 / Tier-3 catalog 확장

본 초안 정식 채택 (§12 절차) 도 *G2 PASS* 가 아니라 *G2 사전조건 정의 + 검증 기준 작성* 의 채택 한정.

---

**작성일**: 2026-05-07
**상태**: DRAFT (초안)
**다음 진입점**: 사용자 결정 — Reviewer-only 단축 검토 (DRAFT 적격 판정) → DRAFT 커밋 → 각 GP entry 진입 (PoC + (a)~(e) 충족 검증) → G2 PASS 합의
**금지 (사용자 명시 답습, 변동 없음)**:
- ❌ G2 PASS 선언 자동
- ❌ G3 / G4 PASS 선언 자동
- ❌ Hermes PMO 격상 선언 자동
- ❌ P2 v3 정식 채택 자동
- ❌ ADR 본문 자동 갱신
- ❌ P2 v2 / prequel archive 자동 처리
