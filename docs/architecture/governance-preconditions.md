# 6 Governance Preconditions (G2) — Design/Governance Gate PASS (Bundled, 2026-05-09)

> **상태: Design/Governance Gate PASS (Bundled, 2026-05-09)**. Hermes PMO 격상 4 게이트 중 G2 — "헌법 8조·5조(Provider Liquidity) 위반 경로 P1~P8 강제 메커니즘 매핑 + 6 거버넌스 사전조건 GP-1~GP-6 정의 + 각 사전조건의 entry/exit 기준" 정의. **G2 + G3 + G4 통합 풀 3+1 합의 + 외부 LLM 2건 (GPT cross-vendor + Claude 인접 컨텍스트) APPROVE WITH CONDITIONS** (`docs/review/3plus1-consensus-2026-05-09-g2g3g4-formal-promotion.md`).
>
> **PASS 범위 한정 (P0 조건 C-A, 5/5 입력 일치)**: 본 PASS 는 *Design/Governance Gate PASS* 한정 — 문서 구조 / 권위 위계 / 6 GP 정의 / 강제 메커니즘 분류 매트릭스 / Entry·Exit 기준 정의의 *설계 승인* 에 한정한다. **Implementation/Runtime PASS 는 본 PASS 에 포함되지 않는다** — GP-2~GP-6 의 PoC 실증 / CI 강제 / runtime hook 구현 / Evidence Ledger 검증은 *별도 합의* 로만 발생.
>
> **GP 별 상태 (P0 조건 C-B, 5/5 입력 일치)**:
> - **GP-1**: PASS (G1b PASS evidence 흡수, 단 Tier-1 한정 — Tier-2/Tier-3 catalog 확장은 후속, Claude C-7)
> - **GP-2 ~ GP-6**: **DESIGN PASS / IMPLEMENTATION PENDING** (각 GP 의 PoC 실증 + (a)~(e) 5조건 충족 검증은 별도 합의)
>
> **§1.2.6 P10 Evidence Forgery 정식 등록 (2026-05-09 후속 5 단축 합의 APPROVE Reviewer-only)**: ADR-012 §1.4 cross-reference + Hermes 변조 차단 매트릭스 4항목 + Layer 1~5 enforcement.
>
> **P2 v3 (`hermes-adoption-design-v3.md`) = Adopted (Design Adoption only, 2026-05-09 후속 6)** 후속 권위. 본 G2 = P2 v3 §4 (G2 정의) + P2 v3 §3.1.4 Implementation Pending 표 + P2 v3 §10.1 Normative Constraints + §10.2 Archive Migration Note + §11.1 Hermes PMO 격상 전 인간 전문 리뷰 의무화 답습.
>
> **P2 v2 (`hermes-adoption-design.md`) = Archived (옵션 A 최소 침습, 2026-05-09 후속 7)** + **`system-identity-prequel.md` = Archived (옵션 A, 2026-05-09 후속 8)** — 본 G2 cross-reference 영향 0건 (path 변경 0건).
>
> **Hermes PMO 격상은 본 PASS 에 포함되지 않는다** (사용자 명시 답습) — 4 게이트 모두 Implementation/Runtime PASS + 외부 LLM 2개 또는 외부 LLM 1개 + 인간 전문 리뷰 (Human-in-the-loop) + 사용자 명시 결정 후 별도 (P2 v3 §2.6.1 12 조건 PMO 격상 체크리스트 답습). G2 운영 구현 PASS / ADR 본문 자동 갱신 / archive 자동 처리도 본 PASS 미포함.

**작성일**: 2026-05-07
**Status (2026-05-07 통합 합의)**: **Design/Governance Gate PASS (Bundled, 2026-05-07)** — `docs/review/3plus1-consensus-2026-05-07-g2-g3-g4-gate-adoption.md` (4/4 입력 만장일치 APPROVE WITH CONDITIONS — Agent A/B/C + 외부 LLM GPT-5.5 Thinking, 12 통합 조건 + Gap-N 6건 흡수 처리). 본 PASS 는 Design/Governance Gate 한정 — Implementation/Runtime PASS / Operational Readiness PASS / Hermes PMO 격상 / P2 v3 정식 채택 모두 미포함.
**정식 PASS 일자**: 2026-05-09 (Design/Governance Gate PASS, Bundled with G3 + G4 — 2026-05-07 통합 합의의 후속 reaffirmation)
**합의 권위**: `docs/review/3plus1-consensus-2026-05-09-g2g3g4-formal-promotion.md` (5/5 입력 APPROVE WITH CONDITIONS — Agent A/B/C 내부 + GPT cross-vendor + Claude 인접 컨텍스트)
**P10 정식 등록 합의**: `docs/review/3plus1-consensus-2026-05-09-g2-p10-evidence-forgery.md` (2026-05-09 후속 5 단축 합의 APPROVE Reviewer-only)
**상위 권위**: 헌법 제8조 (보안), 프로젝트 내 관용 "헌법 제5조 (Provider Liquidity)" — 본 §1.1 명명 정정 참조
**상위 결정**: ADR-008 (Hermes 도입 Option B) 6 차단조건, ADR-011 (수단/목적 분리, §2.3 권위 위계, §2.4 T1/T2/T3), **ADR-009 C-N (P1 facade MVP 진입조건 + Hermes PMO ↔ provider 분리 + Provider Liquidity 5-way 모법 ADR Layer 1, 2026-05-09 후속 4 갱신)**, **ADR-012 (Evidence Ledger Protection, 2026-05-09 후속 3 PR-2 신규 발행)**
**관련 설계**: **`hermes-adoption-design-v3.md` §4 (G2 정의 — P2 v3 Adopted Design Adoption only, 2026-05-09 후속 6)**, `hermes-adoption-design.md` (P2 v2, **Archived 2026-05-09 후속 7**), `system-identity-prequel.md` §3.3 / §4.2 (**Archived 2026-05-09 후속 8**, 본 ADR-011 §2.3 영구 권위 승격 답습으로 권위 보존), `redaction-pattern-equivalence.md` (R-4), `canary-recheck-design.md` (R-5), `llm-providers-design.md` (P1 v2 — Option β LiteLLM facade)
**근거 합의**: `docs/review/3plus1-consensus-2026-05-05-system-identity-redefinition.md` (Agent B 6 거버넌스 사전조건 + 8 위반 경로 P1~P8 식별), `docs/review/3plus1-consensus-2026-05-09-g2g3g4-formal-promotion.md` (G2 정식 PASS 합의), `docs/review/3plus1-consensus-2026-05-09-p2v3-formal-adoption.md` (P2 v3 정식 채택 풀 3+1 + 외부 LLM 2건 — 본 G2 = P2 v3 §4 답습 권위)
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

#### 1.2.3 정식 위반 경로 합산 (P1~P8 + P10, 2026-05-09 후속 5 갱신)

```
헌법 8조 (보안) 위반 경로 = 5건 (P1~P5)
Provider Liquidity 위반 경로 = 3건 (P6~P8)
Evidence Integrity 위반 경로 = 1건 (P10)            ← 2026-05-09 후속 5 정식 등록
─────────────────────────────────────────────────
정식 위반 경로 합계 = 9건 (P1~P8 + P10)            ← ✅ 합의 §29~§30 일치 + ADR-012 발행 시점 P10 흡수
Deferred candidates = 3건 (P9 / P11 / P12, §1.2.5)
```

P10 정식 등록 = ADR-012 (Evidence Ledger Protection) 발행 시점 (2026-05-09 후속 3 PR-2) 트리거 답습 — §1.2.5.2 명시 "P10 정식 등록 시점 = PR-2 신규 ADR-012 발행 시점" 답습. 본 §1.2.6 답습.

#### 1.2.4 본 §1.2 가 *다루지 않는* 위반 경로

본 §1.2는 *헌법 8조 + Provider Liquidity* 위반 경로에 한정. 다음은 본 G2 범위 외:
- 헌법 1조 (SDD) / 2조 (TDD) 위반 — 일반 Harness Layer 1~4 hook 가 다룸
- 헌법 4조 (3+1 합의) 위반 — Layer 5 + 사용자 결정
- 헌법 7조 (투명성) 위반 — Layer 0 (CLAUDE.md) + ADR 절차
- 헌법 10조 (문서 일관성) 위반 — `docs/INDEX.md` + 의존 관계 매트릭스
- ADR-011 §2.4 T3 (자동 정책 변경) 위반 자체 — **G3** ("Hermes ≠ root of trust" 운영 구현) 범위. 본 G2 §9 메타 안전장치에서 *interface*만 명시

#### 1.2.5 P9 ~ P12 deferred candidates (C-I 흡수 — 2026-05-09 후속 2)

> **본 §1.2.5 는 합의 보고서 §11.2 P1 조건 C-I 흡수** (출처: GPT 조건 7 + Claude C-4). 본 §1.2.1 ~ §1.2.3 의 *현재 enumeration P1~P8* 외에 **누락 위반 경로 후보 4 ~ 6 건** 을 *deferred candidates* 로 명시 등록한다. **deferred candidate = 향후 합의에서 P9~P12 정식 등록 가능, 본 G2 PASS 시점 정식 enumeration 외**.

| 후보 ID | 위반 경로 (요약) | 핵심 위험 | 현 등록 상태 | 정식 등록 시점 |
|--------|-------------|--------|----------|----------|
| **P9 (후보)** | **Prompt Injection** — Hermes / Worker / LLM 출력 내 *지시 명령* 이 후속 LLM / Tool 에 의해 *명령* 으로 해석 (예: "ignore previous instructions ...") | 합의 결과 silent override / 자동 정책 변경 위장 / Skill escalation | deferred (GPT 조건 7) | 외부 입력 검증 GP-4 PoC 진입 시점에 P5 (외부 입력 검증) 와 *별 카테고리* 로 정식 등록 검토 |
| ~~**P10 (후보)**~~ → **P10 (정식 등록 완료, §1.2.6 답습, 2026-05-09 후속 5)** | **Evidence Forgery** — JSONL ledger / 합의 보고서 / GitHub Actions run artifact 위조 또는 변조 | PASS 위장 / Hermes-originated 변경 위장 / 합의 권위 침해 | ✅ **정식 등록 완료 (§1.2.6 답습)** | ✅ **2026-05-09 후속 5** — PR-2 ADR-012 발행 (2026-05-09 후속 3) 시점 트리거 답습 → 본 단축 합의 (Reviewer-only) 로 정식 등록 |
| **P11 (후보)** | **Supply-chain Compromise** — Hermes / pysqlcipher3 / litellm / Hermes-agent 의존성 또는 GitHub Actions runner / Docker base image 침해 | 자동 redaction 무력화 / SQLCipher trigger silent 깨짐 / canary catalog silent 변경 / R-6 actual run 위장 | deferred (GPT 조건 7) | 의존성 SBOM (Software Bill of Materials) + supply-chain 검증 PoC 합의 시점에 정식 등록 — Hermes PMO 격상 *전* 권장 (Claude C-3 + C-6 답습) |
| **P12 (후보)** | **Memory Poisoning Side-channel** — Memory / Skill 의 *우회 경로* (CLAUDE.md prompt-level lock-in / 외부 import skill / Memory 자동 흡수) 를 통한 Memory 오염 + 후속 결정 silent 영향 | 자동 학습 → 자동 정책 변경 위장 (T1 → T3 우회) / Skill 권한 escalation 우회 / Provider lock-in 우회 | deferred (Claude C-4 + GPT 조건 7) | G4 (provider-agnostic-memory-skill-design.md) Implementation/Runtime PASS 합의 시점에 정식 등록 — Memory boundary hook + Skill wrapper 실 구현 후 |

##### 1.2.5.1 추가 후보 (lower priority, 2 건)

| 후보 ID | 위반 경로 (요약) | 처리 |
|--------|-------------|----|
| **P13 (후보)** | **Provider-specific URL Hardcoding** — `https://api.anthropic.com/...` / `https://api.openai.com/...` 등 provider 도메인 하드코딩 (P1 facade 우회) | GP-5 / G3 §6.4 / G4 §3.5 (provider_bindings) *동작 측면* 충분 — 별도 P 등록 *불필요* (Claude C-9 답습) |
| **P14 (후보)** | **CLAUDE.md prompt-level Lock-in** — CLAUDE.md / system prompt 본문 내 특정 모델명 / vendor 분기 명시 | system-identity-prequel §7 ("메타포 강제 금지") 답습 + 헌법 5조 (Provider Liquidity) — 별도 P 등록 *불필요* (관용 권위로 흡수) |

##### 1.2.5.2 본 §1.2.5 의 권위 한계

- 본 §1.2.5 는 *deferred candidates* 만 등록 — **본 G2 PASS 시점 P1~P8 enumeration 변경 0건**
- P9 ~ P12 정식 등록은 *각 후보의 정식 등록 시점* (위 표 4 행) 에 별도 합의 (단축 또는 풀 3+1)
- 본 §1.2.5 변경 (P9~P12 정식 등록 / 추가 후보) 자체는 풀 3+1 합의 + ADR Amendment 절차 (T3 변경)
- 본 §1.2.5 등록 후보가 *현 시점* enforcement 의무화 대상 *아님* — deferred candidates 는 *위험 식별 + 후속 합의 진입 trigger*

##### 1.2.5.3 본 §1.2.5 가 *하지 않는* 것

- ❌ P9 / P11 / P12 자동 정식 등록 (각 후보 별도 합의 시점) — **P10 은 §1.2.6 답습 정식 등록 완료 (2026-05-09 후속 5)**
- ❌ 현 G2 PASS 무력화 (deferred 는 *후속* 영역)
- ❌ Hermes PMO 격상 전 P9 / P11 / P12 enforcement 의무 (격상 합의 시점 또는 별도 합의)
- ❌ P13 ~ P14 정식 등록 (관용 권위로 흡수, 별도 P 불필요)

#### 1.2.6 Evidence Integrity 위반 경로 1건 (P10) — 정식 등록 (2026-05-09 후속 5)

> **본 §1.2.6 는 §1.2.5.2 명시 "P10 정식 등록 시점 = PR-2 신규 ADR-012 발행 시점" 답습 흡수.** ADR-012 (Evidence Ledger Protection, 2026-05-09 후속 3 PR-2 발행) 시점이 P10 정식 등록 *트리거*. 본 후속 5 단축 합의 (Reviewer-only) 로 정식 등록.

##### 1.2.6.1 P10 정식 row

| # | 경로 | 시나리오 | Evidence Integrity 측면 (5건) | 관련 ADR / 게이트 / 합의 |
|---|------|---------|--------------------------|------------------|
| **P10** | **Evidence Forgery** | Evidence Ledger entry / external-review 응답 / 합의 보고서 / hash chain / GitHub Actions run artifact / commit history 가 *위조* 또는 *변조* 되어 (a) 잘못된 PASS 판정 / (b) Hermes-originated 변경 silent 수용 / (c) 합의 권위 silent 침해 / (d) 자동 정책 변경 위장 / (e) 외부 LLM 응답 위조 발생 | (i) Ledger entry 형식적 무결성 (11 필드 schema, hash chain) / (ii) prev_hash 검증 실패 처리 / (iii) git history rewrite 차단 / (iv) Hermes-originated commit auto-reject (변조 차단 매트릭스 4항목) / (v) external LLM response `agent="user"` 강제 | **ADR-012 §2.1 ~ §2.12 + §3.1 ~ §3.5** (12 보호 원칙 + 4 매트릭스 + 5 추가 의무) + **G3 §5** (Evidence decision principle: PASS 성립 4 요건 — Tools 검증 + Evidence Ledger entry + 사용자 명시 승인 + 합의 보고서 commit) + **G4 §4.2 / §4.4 / §4.6** (11 필드 schema + Layer 1~5 다층 강제 + Tier-based round-trip) + 본 PR-2 합의 (`docs/review/3plus1-consensus-2026-05-09-pr2-evidence-ledger.md`) |

##### 1.2.6.2 P10 enforcement layer 매핑

본 P10 enforcement 는 **ADR-012 직접 권위** + **G3 §5 + G4 §4** 답습. *별도 GP 신설 부재* (사용자 명시 답습 — 본 §1.2.6 = P10 row 추가 한정, GP 신설은 별도 합의 영역):

| Enforcement Layer | 책임 영역 | 권위 |
|----|--------|----|
| **Layer 1** (Hash chain) | Middle entry tampering 차단 | ADR-012 §2.3 + G4 §4.4 (sha256 + canonical JSON) |
| **Layer 2** (Git append-only) | History 재작성 차단 (denyNonFastForwards) | ADR-012 §2.3 (Layer 2 MANDATORY) |
| **Layer 3** (Signed commit) | Host compromise 후 위조 차단 | ADR-012 §2.3 (Layer 3 RECOMMENDED MVP / MANDATORY multi-host) |
| **Layer 4** (CI 회귀 검증) | canonical JSON 위반 / prev_hash mismatch / timestamp monotonicity 자동 검출 | ADR-012 §2.3 + R-6 workflow 답습 확장 (Implementation 영역) |
| **Layer 5** (External anchor) | 1인 SPOF 완화 + 침해 후 발견 | ADR-012 §2.3 (Layer 5 RECOMMENDED MVP / MANDATORY P2 v3 정식 채택) |
| **Hermes 변조 차단 매트릭스 4항목** | Hermes-originated entry / 파일 변조 / git commit / 외부 LLM 응답 위조 차단 | ADR-012 §2.12 (Gap-17 HIGH 흡수) + G3 §2.5 #11 / §4.5 / §2.2 #20 cross-reference |
| **External LLM `agent="user"` 강제** | 사용자 직접 paste 시 Hermes 위조 차단 | ADR-012 §2.1 원칙 7 + §3.1 |

##### 1.2.6.3 P10 처리 범위 (사용자 명시 답습)

| 차원 | 본 §1.2.6 처리 |
|----|----|
| **상태** | Deferred Candidate (§1.2.5) → **Formal P-row (§1.2.6)** |
| **처리 범위** | Design/Governance row 추가 한정 |
| **Implementation status** | **Pending** — ADR-012 §10.2 답습 (실 runtime hook / migration script / CI step / pre-commit hook 미구현, 별도 Implementation/Runtime PASS 합의) |
| **GP 매핑** | 별도 합의 영역 (본 §1.2.6 = P10 row 추가 한정, GP 신설 또는 기존 GP 매핑 갱신은 별도) |

##### 1.2.6.4 P10 정식 등록의 합의 권위

본 P10 정식 등록 = **단축 합의 (Reviewer-only) 적격** (사용자 명시 답습):
- ADR-012 발행 (PR-2 풀 3+1 합의, 2026-05-09 후속 3) 권위 *내부* 작업
- ADR-012 §11.2 + §1.3 cross-reference 의무 답습
- 본 §1.2.6 = §1.2.5.2 deferred candidate 정식 등록 시점 명시 답습
- 본 P10 정식 row 본문 = ADR-012 §2.1 ~ §2.12 + §3.1 ~ §3.5 답습 한정 (새 권위 결정 0건)

**4 풀 3+1 승격 트리거 검증** (사용자 명시 답습):

| 트리거 | 본 §1.2.6 |
|----|----|
| P10 이 기존 P1~P12 구조와 충돌 | ❌ — §1.2.5 deferred 에 이미 등록, 정식 row 승격은 §1.2.5.2 명시 트리거 답습 |
| Evidence Forgery 가 ADR-012 범위를 넘어 새 정책 변경 요구 | ❌ — ADR-012 §2.1 ~ §3.5 답습 한정, 새 정책 0건 |
| G2 / G3 / G4 Design PASS 상태를 흔드는 내용 | ❌ — §1.2 본문 추가, GP 매핑 변경 0건, 게이트 PASS 상태 영향 0 |
| T3 자동 정책 변경 영역 발생 | ❌ — 정식 row 등록 자체는 T3 변경이지만 *ADR-012 발행 권위 내부* 작업, 사용자 명시 결정 답습 |

→ **4/4 트리거 0건 발화** → **단축 합의 (Reviewer-only) 적격**.

##### 1.2.6.5 본 §1.2.6 이 *하지 않는* 것

- ❌ ADR-012 본문 재작성 (cross-reference 만 가능)
- ❌ ADR-009 추가 갱신 (C-N 별도)
- ❌ G3 / G4 본문 자동 갱신 (cross-reference 만)
- ❌ 신규 GP 신설 (별도 합의 영역)
- ❌ P9 / P11 / P12 자동 정식 등록 (각 후보 별도 합의 시점 답습)
- ❌ P10 enforcement Implementation 자동 (Implementation/Runtime PASS 별도)
- ❌ R-6 workflow ledger 검증 step 자동 추가 (Implementation 영역)
- ❌ Hermes-originated commit auto-reject 자동 구현 (Implementation 영역)
- ❌ Hermes PMO 격상 자동 선언
- ❌ P2 v3 정식 채택 자동 선언 (다음 진입점 풀 3+1 합의)
- ❌ P2 v2 / system-identity-prequel archive 자동 처리

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

### 9.5 SPOF Accepted Risk — 본 §9 자기참조 차단의 *단일 사용자 의존성* (C-F 흡수 — 2026-05-09 후속 2)

> **본 §9.5 는 합의 보고서 §11.2 P1 조건 C-F 흡수** (출처: Claude C-6). 본 §9 ("Hermes 자기참조 차단") 의 *기준 인격* 인 "사용자 명시 결정" 이 **단일 사용자 + 단일 호스트** 모델에 의존하는 SPOF 위험을 명시 기록한다. 운영 측면 본문은 G3 §5.5 위임.

#### 9.5.1 본 §9 의 단일 사용자 의존성

본 §9.2 #1 (filesystem read-only) / #2 (git commit Hermes-originated auto-reject) / #4 (T3 변경 감지 hook → 사용자 alert) 모두 *기준 인격* 으로 **단일 사용자** (`jokwangwon` git author) 를 전제. 이 전제가 침해 시 본 §9 무결성 보호 무력화 가능:

- (i) 사용자 호스트 침해 시 → Hermes-originated 자동 reject 의 *기준* 자체 위변조 가능
- (ii) 단일 GPG / SSH 키 탈취 시 → "사용자 명시 결정 commit author" 위장 가능
- (iii) 단일 GitHub remote 탈취 시 → push 후 force-push 로 합의 보고서 변조 가능 (hash chain 보강 후에도 origin replace 위험)

#### 9.5.2 의도적 수용 + Multi-host / 다인 전환 트리거

본 SPOF 는 **의도적으로 수용** (1인 개발자 + 단일 호스트 MVP 범위 답습). 의무 발동 트리거는 **G3 §5.5.3** 답습 (5 조건). 본 G2 §9.5 는 *보호 대상 무결성 측면* 만 명시:

| # | 트리거 (G3 §5.5.3 답습) | G2 §9 측면 의무 발동 |
|---|---------|-----------|
| (1) | 두 번째 사용자 (다른 git author) commit 시도 | GPG signed commit 강제 + branch protection multi-author 룰 + 본 6 GP 본문 변경의 multi-stakeholder 합의 강제 |
| (2) | Hermes container 분산 (multi-host) | 정책 파일 distributed read-only (signed manifest) + 분산 audit log sync |
| (3) | Production 환경 전환 | KMS-backed encryption + 6 GP 본문 secrets vault 백업 |
| (4) | 외부 LLM 의뢰·응답 자동화 | 외부 LLM 응답 hash 검증 + signed manifest 의무 |
| (5) | Hermes PMO 격상 합의 시점 | 본 §9.5 multi-layer 전환 PASS 동시 충족 의무 (Claude C-3 + C-6 답습) |

#### 9.5.3 본 §9.5 가 *하지 않는* 것

- ❌ SPOF 정당화 (본 §9.5 는 *수용 + 트리거 명시* 까지, 본 §9 무력화 사유 아님)
- ❌ Multi-host 전환 의무 자동 강제 (본 §9.5 는 *조건* 명시까지, 실 구현 별도 합의)
- ❌ G3 §5.5 본문 흡수 (운영 측면은 G3 §5.5 위임, 본 §9.5 는 *6 GP 무결성 측면* 만)
- ❌ 본 G2 PASS 무력화 (본 §9.5 는 *명시 기록* 으로 책무 분리, G2 PASS 자체는 본 §9.5 충족 의존성 아님)

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
