OpenAI Codex v0.128.0 (research preview)
--------
workdir: /home/delangi/문서/project/category/AI_development_tool
model: gpt-5.5
provider: openai
approval: never
sandbox: danger-full-access
reasoning effort: none
reasoning summaries: none
session id: 019e6c1b-7564-7810-92aa-47358601ce2f
--------
user
당신은 외부 LLM 검토자 (cross-vendor blind review)입니다. 본 평가의 vendor = OpenAI (codex CLI), 본 cycle 의 풀 3+1 Agent vendor = Anthropic Claude. cross-vendor 충족 (헌법 5조-2 Provider Liquidity 비협상 + ADR-011 §2.1 (e) + §2.4 T3 영역 답습).

## 본 cycle 개요

AI_development_tool 프로젝트 (SDD + TDD 방법론, 한국어 소통). 본 cycle = **MVP-2 진입 합의 entry brief** (24 entry MVP-1 1.5차 보강 entry brief 답습 형식, 풀 3+1 + 외부 LLM 1+ + 사용자 명시 3 조건 모두 충족 시점 발효).

본 cycle 발효 효과:
- MVP-2 영역 (G2 GP-2 송신 redaction + G4 §4.4 Layer 4 CI 회귀 검증) 진입 권한 발효
- (β) sub-수단 결정 cycle 진입 자격 발효 (R-1~R-5 + L-1~L-5)
- (γ) 분리 영역 결정 cycle 진입 자격 발효 (G4 §4.4 Layer 1+2 의존 vs Layer 4 동시)
- Rollback Trigger / Evidence 본문 채택

본 cycle 발효 *하지 않는 것*: 수단 결정 0 / threshold 고정 0 / 실 코드 0 / MVP-2 Implementation Evidence PASS 발효 0 / Operational Readiness PASS 0 / Hermes PMO 격상 0 (총 27 금지 사항, §0.3 답습).

## 검토 대상 (working directory 자료, codex 직접 read 의무)

본 검토 대상 (PRIMARY):
- `docs/phase0/mvp2-entry-brief.md` (v1, 480줄, §0~§10 — **본 검토 PRIMARY**)

본 brief 의 직접 입력 자료 (51 entry audit brief + 합의 보고서):
- `docs/phase0/mvp2-entry-eligibility-audit-brief.md` (51 entry, 372줄)
- `docs/review/3plus1-consensus-2026-05-28-mvp2-entry-eligibility-audit.md` (51 entry, 184줄)

선행 권위 (답습 source):
- `docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md` (32 entry MVP-1 PASS 발효 합의)
- `docs/phase0/mvp1-1.5th-reinforcement-entry-brief.md` (24 entry, 570줄 — 본 brief 구조 답습 source)
- `docs/architecture/implementation-runtime-roadmap-mvp1.md` (§1.2 + §1.3 + §2.2 + §5.1)
- `docs/architecture/governance-preconditions.md` (§4 GP-2 정의 + Entry/Exit)
- `docs/architecture/provider-agnostic-memory-skill-design.md` (§4.4 Layer 1~5)
- `docs/decisions/ADR-012-evidence-ledger-protection.md` (§2.3 + §2.5 + §2.7 + §3.4)
- `docs/decisions/ADR-011-means-vs-ends-redaction.md` (§2.1 (a)~(d) + (e) 합의 APPROVE 운영조건 5조건 모법)

상위 권위:
- `docs/constitution/PROJECT_CONSTITUTION.md` (헌법 제8조 보안 + 제5조-2 Provider Liquidity 비협상)

## 검토 의무 (7 기준)

본 brief 의 진입 합의 *입력* 자격을 평가:

1. **cross-vendor 충족 명시** — 응답 vendor = OpenAI codex / 본 cycle 풀 3+1 Agent vendor = Anthropic Claude (cross-vendor blind risk 차단 요건 형식상 충족 명시 의무)

2. **본 brief v1 직접 읽기 evidence** — 응답 본문 내 brief §X verbatim 인용 또는 영역 식별 다층 (24 entry codex 답습 패턴)

3. **ADR-011 §2.1 (a)~(e) 5조건 답습 정확성 검증** — ⚠️ **24 entry codex 응답 답습**: 원문 ADR-011 §2.1 = (a)~(d) 4조건 / (e) 합의 APPROVE 운영조건 = 후속 권위 (§3 또는 §5). 본 brief = "(a)~(e) 5조건" 표현 사용 — 표현 일관성 + 원문 답습 정확성 검증 의무

4. **두 영역 (GP-2 + G4 §4.4 Layer 4) 진입 자격 평가** — 각 영역별 평가 본문 + governance-preconditions §4.4 (Entry 3 조건) + §4.5 (Exit 5조건) + G4 §4.4.1 line 649~653 (Layer 4 정의) + ADR-012 §2.3 (다층 강제) verbatim 인용 평가

5. **(β) sub-수단 결정 분리 답습 정확성** — 본 cycle = 영역 진입 한정, sub-수단 결정 (R-1~R-5 + L-1~L-5) = (β) 별도 cycle 분리 인식 검증 의무. 24 entry (sub-수단 채택 결정 통합) 과의 차이 답습 정확성 검증

6. **Rollback Trigger / Evidence 요건 평가** — RT-1~RT-7 / E-1~E-9 본문 후보 평가 (governance-preconditions §4.6 + ADR-012 §2.7 / §3.4 답습 정확성)

7. ⚠️ **R-S1 잠재 risk 검증** — 본 brief §10 P-4 자기진단 영역 (ADR-012 §2.3 line 182 verbatim = "Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)" 인지 / 또는 G4 §4.4.1 line 649~653 verbatim = "Layer 4 — CI 회귀 검증 (MANDATORY)" 인지). 두 source 의 "Layer 4" 정의 *충돌* 검증 — 권위 chain 다중 source 손상 위험 (24 entry R-S1 답습 패턴, ADR-008 §A.2 R1-2 권위 chain 다중 source 손상 확정 유형). codex 가 ADR-012 §2.3 line 182 verbatim 직접 read + G4 §4.4.1 line 649~653 verbatim 직접 read 후 비교 평가 의무

## 판정 형식

- **총평**: APPROVE / APPROVE WITH CONDITIONS / REVISE AS ENTRY BRIEF INPUT / REJECT (24 entry codex 답습 4 단계)
- **BLOCKING N건**: brief input 으로 쓰기 전 명확화 필수 항목 (R-1, R-2, ... 식별자)
- **권고 N건**: 정확성 / 명료성 / 안전성 권고 (N-1, N-2, ... 식별자)
- **NOTE N건**: 기타 관찰 (필요 시)

## 응답 형식

응답 길이: ~250~400 줄. 한국어 + 영문 기술 용어 혼용 가능. Markdown 형식.

응답 구조:
- 검토자 / Vendor (cross-vendor 명시)
- 직접 검토한 working directory 자료 (path 목록)
- §0 총평 (판정 + BLOCKING 수 + 권고 수)
- §1 BLOCKING N건 (각 R-x 식별자 + 본문 + 권고 변경)
- §2 권고 N건 (각 N-x 식별자 + 본문)
- §3 NOTE N건 (필요 시)
- §4 7 검토 기준별 평가 (cross-check)
- §5 R-S1 잠재 risk 검증 결과 (verbatim 인용 + 충돌 분석)

codex
요청하신 형식에 맞춰 working directory 자료를 직접 읽고, brief 입력 자격 관점으로만 검토하겠습니다. 먼저 PRIMARY와 권위 문서에서 지정된 조항을 확인한 뒤 판정과 blocking 항목을 분리하겠습니다.
exec
/bin/bash -lc "sed -n '1,420p' docs/phase0/mvp2-entry-eligibility-audit-brief.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
# MVP-2 진입 자격 audit brief (v1)

> **작성**: 2026-05-28 (51번째 entry 진입 cycle)
>
> **scope**: G2 GP-2 송신 redaction + G4 §4.4 Layer 4 (CI 회귀 검증) 진입 자격 audit
>
> **본 brief = audit 한정** (23 entry `mvp1-gp3-gp5-current-state-audit-brief.md` 답습 — 작은 cycle)
>
> **본 cycle 발효 = brief commit + 합의 commit + SESSION/INDEX commit 한정** (수단 결정 0, MVP-2 진입 발효 0, ADR/헌법/roadmap 본문 변경 0)

---

## §0 본 brief 의 scope

### §0.1 본 brief 가 *하는* 것

1. MVP-1 PASS 답습 상태 + MVP-2 영역 정의 확정 (50 entry carry-over §4 답습)
2. G2 GP-2 (송신 redaction) 진입 자격 audit (Entry 충족 자격 + Exit 5조건 매핑 권고)
3. G4 §4.4 Layer 4 (CI 회귀 검증) 진입 자격 audit (Entry 충족 자격 + Exit 5조건 매핑 권고)
4. 두 영역 통합 R-6 workflow 확장 권고 (단일 workflow 통합 vs 분리 대안)
5. sub-수단 후보 식별 (수단 *결정* 아님 — 별도 합의 영역)
6. Rollback Trigger 후보 + Evidence 요건 + 합의 형태 권고
7. 금지 사항 명시 + 다음 단계 (단계별 cycle 답습)

### §0.2 본 brief 가 *하지 않는* 것 (사용자 명시 답습)

- ❌ 수단 결정 (R-1~R-5 / L-1~L-5 中 채택 결정 = 별도 cycle)
- ❌ threshold 고정 (catalog 규모 / monotonicity tolerance 등)
- ❌ MVP-2 진입 발효 (본 brief = audit, MVP-2 진입 = 별도 cycle)
- ❌ ADR 본문 갱신 (ADR-011 / 012 / 008 / 009 / 010 본문 변경 0)
- ❌ 헌법 본문 갱신 (T3 영역, ADR Amendment 절차 별도)
- ❌ roadmap-mvp1 본문 갱신 (MVP-1 영역 답습 유지)
- ❌ governance-preconditions.md §4 본문 갱신 (GP-2 정의 답습)
- ❌ provider-agnostic-memory-skill-design.md §4.4 본문 갱신 (Layer 정의 답습)
- ❌ ADR-012 본문 갱신 (Layer 1~5 권위 답습)
- ❌ 실 코드 변경 (`tools/` / `src/` / `.github/workflows/` / `.pre-commit-config.yaml` / `agent/redact.py` / `adapters/llm/facade.py`)
- ❌ MVP-1 Implementation Evidence PASS 재선언 (32 entry 답습 유지)
- ❌ Operational Readiness PASS 발효
- ❌ Hermes PMO 격상
- ❌ adapters/llm/facade.py placeholder → real (별도 (d) carry-over)
- ❌ Tier-2/3 catalog 확장 (별도 합의 영역)

### §0.3 권위 답습 source

- **ADR-011 §2.1 (a)~(e) 5조건** (수단/목적 분리, 모법) — `docs/decisions/ADR-011-means-vs-ends-redaction.md`
- **governance-preconditions.md §4** (GP-2 Egress Redaction) — `docs/architecture/governance-preconditions.md`
- **provider-agnostic-memory-skill-design.md §4.4** (Layer 1~5 다층 강제) — `docs/architecture/provider-agnostic-memory-skill-design.md`
- **ADR-012 §2.3 + §2.5 + §2.7** (Append-only + Hash Chain + RFC 8785 JCS + prev_hash 실패 처리) — `docs/decisions/ADR-012-evidence-ledger-protection.md`
- **implementation-runtime-roadmap-mvp1.md §1.2 + §1.3** (3-layer PASS + GP-2 = MVP-2 분리 사유) — `docs/architecture/implementation-runtime-roadmap-mvp1.md`
- **implementation-runtime-roadmap.md §3 + §4 + §6** (G2 + G4 영역 + 9 그룹) — `docs/architecture/implementation-runtime-roadmap.md`
- **32 entry MVP-1 Implementation Evidence PASS 발효 합의** — `docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md`
- **50 entry carry-over §4** (다음 세션 진입 후보) — `docs/sessions/SESSION_2026-05-27.md`

---

## §1 MVP-1 PASS 답습 + MVP-2 영역 정의

### §1.1 MVP-1 답습 상태 (2026-05-27 32 entry 답습)

⭐⭐⭐ **MVP-1 Implementation Evidence PASS *완전 발효 (α)*** — GP-3 5/5 + GP-5 5/5 양쪽 충족 + 사용자 명시 결정 + 풀 3+1 + 외부 LLM 1+ APPROVE WITH CONDITIONS.

- 4 sub-cycle 완료: PC-1-T3 (`3a63a5b`) + S-3 (`4451716`) + ST-2 (`1edc5bb`) + AR-3 (`7f57323`/`7c294bb`/`73ed20d`/`9837298`)
- 31 entry 첫 PR (head SHA `9837298befdeda6c7e170879cc9f15e331c52bce`) 11/11 SUCCESS + mergeable CLEAN
- 32 entry 합의: `docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md` (BLOCKING 6 + 권고 5 1pass 흡수)
- PR #2 MERGED → main `eb51284` 영구 통합 (31 commits / 21,095 줄, 44 entry)
- 후속 정리 entry chain (40~50): D-6 workflow 4 entry full cycle + Actions Node.js 24 마이그레이션 + secret-scanner 정밀화

### §1.2 본 brief 시점 상태

- **HEAD**: `3517453` (50 entry 정리 commit, branch `feature/jarvis-mvp0`)
- **branch**: feature/jarvis-mvp0 (clean), main `eb51284` 답습
- **세션**: 2026-05-28 (51 entry 진입 cycle, 본 brief = 51 entry 첫 산출)

### §1.3 MVP-2 영역 정의 (50 entry carry-over §4 답습)

50 entry carry-over §4: "MVP-2 진입 자격 검토 (G2 GP-2 송신 redaction + G4 §4.4 Layer 4)".

**G2 GP-2 송신 redaction** (governance-preconditions §4):
- Hermes / Worker Agent 가 stdout / stderr / log file / LLM API request body 에 secret 노출 차단
- ADR-011 §2.3 운영 함의 #2 의 *보조* 역할 (DB INSERT 차단 = GP-1 책임, GP-2 = 송신/로그 경로 한정)

**G4 §4.4 Layer 4 — CI 회귀 검증** (provider-agnostic-memory-skill-design §4.4.1):
- Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증
- canonical JSON 위반 검출
- timestamp monotonicity 검증 (ADR-012 §3.4)
- R-6 workflow (`.github/workflows/r2-canary.yml`) 답습 확장 (별도 PR — Implementation 영역)
- MANDATORY 등급 (Layer 5 中 4번째, Layer 1 + 2 + 4 MANDATORY, Layer 3 + 5 RECOMMENDED MVP)

### §1.4 두 영역 공통 통합 영역 (핵심 발견)

⭐ **두 영역 모두 R-6 workflow (`.github/workflows/r2-canary.yml`) 답습 확장 영역**:

- **GP-2 §4.6 산출 후보**: R-6 workflow 확장 — log file canary inject step
- **G4 §4.4 Layer 4**: R-6 workflow 답습 확장 (Layer 1+2 자동 회귀 + canonical JSON 위반 + timestamp monotonicity)

→ **단일 R-6 workflow 확장으로 두 영역 동시 진행 가능** (§4 권고 답습).

### §1.5 MVP-2 영역 분리 사유 답습 (roadmap-mvp1.md §1.3)

GP-2 = MVP-2 로 분리한 사유 (32 entry 답습 전 결정):

1. **R-4 / R-4.1 답습 책임 분담** — GP-2 의 송신 redaction = R-4.1 Tier-1 42 catalog 의 *런타임 적용* 영역. Group D PoC = *형식적 검출 layer 한정*. 실 송신 redaction = Hermes upstream 영역 (Group D PoC §1.2 #6 답습) + P1 facade RedactionFilter 본문 (Group D PoC §1.2 마지막 항목 답습).
2. **MVP-1 부담 경감** — GP-3 + GP-5 만으로도 의사결정 부담 충분. GP-2 추가 시 4 영역 동시 진입 — 1인 개발자 환경에서 운영 부담 ↑.
3. **외부 LLM line 242 vs C-7 line 378 충돌 해소 = C-7 답습** — GP-2 = **MVP-2** 의 Implementation Evidence PASS 영역 *우선순위 1* (C-7 line 379 답습) — 본 분리 = *시점* 분리이지 *영구 제외* 아님.

---

## §2 G2 GP-2 진입 자격 audit

### §2.1 Entry 기준 충족 자격 (governance-preconditions.md §4.4)

| # | 조건 | 현 상태 (2026-05-28) | 충족 자격 |
|---|------|---------------------|---------|
| 1 | R-4 pattern equivalence 작성 완료 | ✅ `docs/architecture/redaction-pattern-equivalence.md` (ADR-011 §2.1 (a) 충족, 2026-05-06) | 충족 |
| 2 | Hermes native redaction `agent/redact.py` 존재 확인 | ✅ R-1 Day 2 evidence | 충족 |
| 3 | 사용자 명시 GP-2 작업 진입 결정 | ⏳ 본 brief = 진입 *자격* 평가, 진입 *결정* = 별도 cycle | 사용자 영역 |

→ **현 시점 Entry 충족 = 2/3 충족 + 1 사용자 영역** (Entry 자체는 기술적 gap 0).

### §2.2 Exit 기준 5조건 매핑 권고 (ADR-011 §2.1 (a)~(e) + governance-preconditions §4.5 답습)

| # | 조건 | GP-2 영역 현 상태 | 충족 경로 권고 (수단 결정 0) |
|---|------|----------------|----------------------|
| (a) | 동등 이상 보안 결과 | ✅ R-4 답습 (충족) — `redaction-pattern-equivalence.md` | Hermes native redaction Tier-1 42 catalog 적용 검증 evidence + P1 facade RedactionFilter 검증 evidence (둘 다 *실행* 시점 evidence 추가 수집) |
| (b) | 격리 환경 PoC 실증 | ⚠️ Group D PoC 부분 (`g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md` — 형식적 검출 layer 한정, 송신 redaction 영역 미커버) | log file canary inject + grep 검증 PoC (Docker 격리) 추가 — *송신 redaction* 영역 확장 |
| (c) | ADR / SDD 권위 명시 | ✅ ADR-011 §2.3 + 본 §4 권위 (충족) | ADR-008 차단조건 #1 보조 메커니즘 cross-reference 추가 (본문 변경 0, cross-reference 한정) |
| (d) | 자동 회귀 검증 경로 확보 | ❌ gap | **R-6 workflow 에 log file canary inject step 추가 — §4 통합 권고 (G4 §4.4 Layer 4 와 단일 workflow 확장)** |
| (e) | 합의 APPROVE | ❌ gap | 단축 또는 풀 3+1 합의 (G2 GP-2 한정 또는 G2 통합) — §7 합의 형태 권고 답습 |

→ **현 시점 5조건 충족 자격 = 2.5/5** ((a) + (c) 충족 / (b) 부분 / (d) + (e) gap).

### §2.3 sub-수단 후보 식별 (수단 결정 0, 후보 비교만)

| # | 수단 | 영역 | base64 evasion 처리 | 호환성 | 비고 |
|---|------|----|------------------|------|----|
| **R-1** | Hermes native redaction (`agent/redact.py`) | 송신 직전 redaction | known limitation (G3-4 영역, MVP-2/3 분리 답습) | Tier-1 42 catalog 답습 | MANDATORY (ADR-011 §2.3 #2) |
| **R-2** | P1 facade RedactionFilter | LLM API 진입점 redaction | 별도 layer | P1 v2 §8.2 답습 | MANDATORY (facade single entry point) |
| **R-3** | log file canary inject + grep CI step | CI 회귀 검증 | 별도 layer | R-6 workflow 답습 확장 | MANDATORY ((d) 충족 경로) |
| **R-4** | R-1 + R-2 + R-3 병행 (defense-in-depth) | 다층 redaction | 보조 | 양쪽 활용 | **본 brief 권고 — 5/5 입력 패턴 답습** |
| **R-5** | base64 / URL-encoded / 압축 evasion 별도 영역 | Hermes upstream R2-6 또는 P1 facade RedactionFilter 확장 | MVP-2/3 분리 영역 (G3-4 답습) | 본 cycle 범위 외 | 분리 영역 명시 |

→ **수단 *결정* = 별도 합의 영역** (MVP-2 entry 합의 시점). 본 brief 권고: **R-4 (R-1 + R-2 + R-3 병행)** = MVP-2 진입 시점 채택.

---

## §3 G4 §4.4 Layer 4 진입 자격 audit

### §3.1 영역 정의 답습 (G4 §4.4.1 + ADR-012 §2.3)

**Layer 4 — CI 회귀 검증 (MANDATORY)**:
- Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증
- canonical JSON 위반 검출 (RFC 8785 JCS Primary + fallback 동등성)
- timestamp monotonicity 검증 (ADR-012 §3.4 답습)
- R-6 workflow (`.github/workflows/r2-canary.yml`) 답습 확장 (별도 PR — Implementation 영역)

**참고**: 본 audit = Layer 4 영역 한정. Layer 1 / Layer 2 / Layer 3 / Layer 5 = 본 brief 직접 scope 외 (단, Layer 4 검증 대상 = Layer 1 + Layer 2 이므로 *의존 영역* 으로 명시).

### §3.2 Entry 자격 (현 상태)

| # | 조건 | 현 상태 (2026-05-28) | 충족 자격 |
|---|------|---------------------|---------|
| 1 | Design/Governance Gate PASS 답습 | ✅ G4 = PASS Bundled (2026-05-07 + 2026-05-09 후속) | 충족 |
| 2 | ADR-012 §2.3 Layer 1~5 권위 정의 발효 | ✅ 2026-05-09 PR-2 풀 3+1 + 외부 LLM 2건 APPROVE WITH CONDITIONS | 충족 |
| 3 | G4 §4.4 본문 P-1 (RFC 8785 JCS) 흡수 완료 | ✅ 2026-05-11 흡수 완료 | 충족 |
| 4 | Layer 1 (hash chain) 실 구현 (`tools/jsonl_chain_verify.py` 또는 동등) | ❌ gap (의존 영역) | 미충족 |
| 5 | canonical JSON test corpus (≥ 20개 RFC 8785 reference) | ❌ gap (`tests/canonical/` 미존재) | 미충족 |
| 6 | Layer 4 CI step 실 구현 (R-6 workflow 확장) | ❌ gap | 미충족 |
| 7 | ledger 첫 entry (genesis hash) 작성 | ❌ gap (의존 영역) | 미충족 |
| 8 | 사용자 명시 작업 진입 결정 | ⏳ 본 brief = 진입 *자격* 평가, 진입 *결정* = 별도 cycle | 사용자 영역 |

→ **현 시점 Entry 충족 자격 = 3/8 충족 + 1 사용자 영역** (Design Gate + Layer 정의 + JCS 채택만 충족, 4 의존 영역 + Layer 4 자체 구현 gap).

### §3.3 Exit 기준 5조건 매핑 권고 (ADR-011 §2.1 (a)~(e))

| # | 조건 | G4 §4.4 Layer 4 현 상태 | 충족 경로 권고 (수단 결정 0) |
|---|------|--------------------|----------------------|
| (a) | 동등 이상 보안 결과 | ❌ gap (실 구현 부재) | Layer 1+2+4 결합 보안 결과 vs 기존 (없음) 비교표 — middle entry tampering / canonical 위반 / timestamp 위반 차단 |
| (b) | 격리 환경 PoC 실증 | ❌ gap | Docker 격리 PoC 3종 — middle entry tampering 차단 + canonical JSON 위반 차단 + timestamp monotonicity 위반 차단 |
| (c) | ADR / SDD 권위 명시 | ✅ ADR-012 §2.3 + G4 §4.4 (충족) | (충족 — 추가 작업 0, cross-reference 만 보강) |
| (d) | 자동 회귀 검증 경로 확보 | ❌ gap | **R-6 workflow 답습 확장 step 추가 — §4 통합 권고 (GP-2 와 단일 workflow)** |
| (e) | 합의 APPROVE | ❌ gap | **풀 3+1 합의 권고** (G4 §4.4 Layer 1+2+4 통합 + Layer 5 권고 영역 추가 의사결정) |

→ **현 시점 5조건 충족 자격 = 1/5** ((c) 만 충족, (a)/(b)/(d)/(e) 모두 gap).

### §3.4 sub-수단 후보 식별 (수단 결정 0, 후보 비교만)

| # | 수단 | 영역 | Library | 비고 |
|---|------|----|---------|----|
| **L-1** | Layer 1 (hash chain) Python stdlib 단독 (`hashlib.sha256` + `json.dumps(sort_keys=True, separators=(",",":"))`) | hash chain 검증 | stdlib | fallback canonical JSON, RFC 8785 동등성 test corpus 의무 |
| **L-2** | Layer 1 + RFC 8785 JCS Primary (`pyjcs` / `rfc8785` library) | hash chain + canonical | 외부 library 1+ (의존성 추가 trigger — R-2 / R-4.1 PoC 자동 재실행 의무 ADR-012 §2.1 답습) | Primary 채택, fallback 보조 |
| **L-3** | Layer 4 R-6 workflow step (canonical JSON 위반 + prev_hash mismatch + timestamp monotonicity) | CI 회귀 | shell + Python (stdlib) | R-6 답습 확장 |
| **L-4** | L-1 + L-3 병행 (MVP 권고) | Layer 1+4 동시 | stdlib 단독 | **본 brief 권고 — MVP 단계 답습 (5/5 입력 권고 답습)** |
| **L-5** | L-2 + L-3 병행 (정식 권고) | Layer 1+4 + JCS Primary | 외부 library 1+ | 정식 채택 시점 (Operational Readiness 영역 또는 별도 cycle) |

→ **수단 *결정* = 별도 합의 영역** (MVP-2 entry 합의 시점). 본 brief 권고: **L-4 (L-1 + L-3 병행)** = MVP-2 진입 시점 채택, L-5 = 별도 cycle (외부 library 의존성 추가 = ADR-012 §2.1 답습 R-2 / R-4.1 PoC 자동 재실행 trigger).

---

## §4 두 영역 통합 R-6 workflow 확장 권고

### §4.1 통합 가능성 분석

| 영역 | 산출 후보 | R-6 workflow 답습 확장 |
|----|----------|-----------------------|
| GP-2 §4.6 | log file canary inject + grep CI step | ✅ R-6 답습 확장 (governance-preconditions §4.6 line 460 답습) |
| G4 §4.4 Layer 4 | Layer 1 + Layer 2 자동 회귀 + canonical 위반 + timestamp monotonicity CI step | ✅ R-6 답습 확장 (provider-agnostic-memory-skill-design §4.4.1 line 653 답습) |

→ **두 영역 모두 동일 R-6 workflow (`.github/workflows/r2-canary.yml`) 확장 대상**.

### §4.2 통합 vs 분리 대안 비교

| 대안 | 장점 | 단점 | 권고 |
|----|----|----|----|
| **W-A: 단일 R-6 확장 (GP-2 + G4 §4.4 Layer 4 통합)** | ceremony-inflation 차단 / CI 자원 효율 / evidence 통합 / R-6 답습 한 PR | step 수 증가 / 실패 영역 식별 복잡도 ↑ (step name 분리로 완화 가능) | **✅ 본 brief 권고** |
| W-B: 별도 workflow 2개 분리 (`secret-egress-redaction.yml` 신설 + `ledger-chain-verify.yml` 신설) | 영역 분리 명확 / 실패 영역 식별 즉시 | ceremony-inflation 위험 / R-6 답습 미답습 / branch protection contexts 추가 부담 (43 entry 8 contexts 답습) | ❌ 비권고 |

### §4.3 통합 시 R-6 workflow 확장 step 후보 (예시, 결정 0)

```yaml
# .github/workflows/r2-canary.yml (R-6 답습 확장, 본 brief = 예시 수준 결정 0)
jobs:
  # 기존 R-2 / R-4.1 canary step (보존)
  ...

  # 신규 GP-2 step (R-3 답습)
  gp2-log-canary-grep:
    - canary fake secret inject (Docker 격리)
    - log file generate (Hermes / Worker Agent 시뮬레이션)
    - grep canary in log → 검출 시 FAIL

  # 신규 G4 §4.4 Layer 4 step (L-3 답습)
  g4-ledger-chain-verify:
    - jsonl chain verify (Python stdlib)
    - canonical JSON RFC 8785 reference 동등성 (test corpus)
    - timestamp monotonicity check
```

**중요**: 위 예시 = *구조 권고* 한정, 실제 step 정의 / 입력 변수 / threshold = 별도 cycle.

---

## §5 Rollback Trigger 후보 (수단 결정 0, 후보 식별만)

| # | Trigger | 발화 조건 | 권위 답습 |
|---|---------|---------|---------|
| RT-1 | Hermes native redaction 우회 검출 | log file canary inject grep PASS 후 평문 leak 발견 | ADR-011 §2.3 #2 + R-7 SOP §5 ROLLBACK trigger R5 |
| RT-2 | P1 facade RedactionFilter 우회 | LLM API request body 평문 secret 검출 | P1 v2 §8.2 + ADR-008 차단조건 #1 보조 |
| RT-3 | base64 / URL-encoded evasion 신규 발견 | Tier-1 42 catalog 미커버 evasion 발견 | G3-4 답습 → MVP-2/3 영역 분리 (본 cycle 범위 외) |
| RT-4 | hash chain middle entry tampering 검출 | Layer 1 검증 실패 | ADR-012 §2.7 (`chain_violation_detected` ledger entry) |
| RT-5 | canonical JSON 위반 검출 | Layer 4 CI step FAIL | ADR-012 §2.5 + §원칙 5/6 + R-6 답습 (`canonical_json_fallback` 또는 BLOCK) |
| RT-6 | timestamp monotonicity 위반 | Layer 4 CI step FAIL → BLOCK | ADR-012 §3.4 + R-6 답습 |
| RT-7 | R-6 workflow 자체 silent override | gate enforcement bypass detected | G3 §2.6 + G4 §3.8.2 #10 + 43 entry 8 contexts (`bypass-detect`) 답습 |

---

## §6 Evidence 요건 후보 (수단 결정 0, 후보 식별만)

| # | Evidence | 출처 |
|---|---------|------|
| E-1 | Hermes native redaction Tier-1 42 catalog 적용 검증 | `agent/redact.py` 실행 evidence (R-4 답습) |
| E-2 | P1 facade RedactionFilter 적용 검증 | facade 진입점 evidence (TR-1 (d) carry-over 의존) |
| E-3 | log file canary inject + grep PASS evidence | Docker 격리 PoC (R-1 / R-4.1 답습) |
| E-4 | hash chain 검증 PoC PASS evidence | middle tampering 차단 PoC (Docker 격리) |
| E-5 | canonical JSON test corpus PASS (≥ 20 RFC 8785 reference) | `tests/canonical/` (G4 §4.4.2 답습) |
| E-6 | timestamp monotonicity 위반 차단 PoC | Docker 격리 (ADR-012 §3.4 답습) |
| E-7 | R-6 workflow 확장 step actual run PASS | GitHub Actions run ID + verdict PASS (43 entry actual run id 답습 유의 — 42 entry `25623028888` 답습) |
| E-8 | 합의 보고서 commit | `docs/review/3plus1-consensus-2026-05-XX-mvp2-entry.md` (별도 cycle) |
| E-9 | 외부 LLM 응답 1+ (cross-vendor) | `docs/external-review/2026-05-XX-mvp2-entry-codex-response.md` (또는 동등, 별도 cycle, 24 entry (α) 답습) |

---

## §7 합의 형태 권고

### §7.1 본 audit brief 합의 (본 cycle)

- **Reviewer-only 단축 합의** 권고 (1-agent 직접 또는 Reviewer-only)
- **근거**:
  - audit 한정, 수단 결정 0, MVP-2 진입 발효 0
  - ADR 본문 변경 0 / 헌법 본문 0 / roadmap 본문 0 / 실 코드 0
  - ADR-011 §2.1 5/5 풀 3+1 승격 trigger 0건 발화 (자체 검증, §7.3 답습)
  - 23 entry `mvp1-gp3-gp5-current-state-audit-brief.md` 답습 (Reviewer-only 단축 진행)
  - ceremony-inflation 차단 메모리 답습

### §7.2 MVP-2 진입 합의 (별도 cycle, 본 brief 후속, 사용자 영역)

- **풀 3+1 + 외부 LLM 1+** 권고 (cross-vendor 의무)
- **근거**:
  - MVP-1 entry 합의 (24 entry) + 32 entry MVP-1 PASS 발효 합의 패턴 답습
  - MVP-2 = MVP-1 동격 큰 cycle (Implementation Evidence PASS 영역 신규 영역)
  - GP-2 + G4 §4.4 Layer 4 = 두 영역 통합 합의 (단일 R-6 workflow 확장)
- **사용자 영역**: 외부 LLM 응답 1+ (또는 Claude 가 tmux + codex 직접 호출, 24 entry (α) 자격 답습 — bypass sandbox 자격 사용자 명시 시점)

### §7.3 본 audit brief 풀 3+1 승격 trigger 검증 (자체 평가)

ADR-011 §2.1 (a)~(e) 5조건 답습 — 본 brief 가 풀 3+1 승격 trigger 발화 자격이 있는지 자체 검증:

| # | trigger | 본 brief 발화 여부 | 자체 평가 근거 |
|---|---------|---------------|--------------|
| 1 | 큰 결정 (수단 결정 / threshold 고정 / 발효) | ❌ 미발화 | 본 brief = audit 한정, 결정 0 / 고정 0 / 발효 0 |
| 2 | 아키텍처 / SDD / 보안 본문 변경 | ❌ 미발화 | 본 brief = 신규 phase0 파일 1개, 본문 변경 0 |
| 3 | ADR 본문 변경 | ❌ 미발화 | 본 brief = ADR 본문 0 |
| 4 | 권위 chain 다중 source 손상 위험 | ❌ 미발화 | 본 brief = cross-reference 답습 한정 |
| 5 | 외부 LLM 응답 통합 필요성 | ❌ 미발화 | 본 brief = 자체 audit, 외부 LLM 0 |

→ **5/5 풀 3+1 승격 trigger 0건 발화 — Reviewer-only 단축 합의 적격**.

---

## §8 금지 사항 (본 cycle 영구 유지)

§0.2 답습 (전체 14 항목 재명시 생략, §0.2 참조).

추가 본 cycle 한정 금지:

- ❌ 두 영역 분리 W-B 대안 채택 (§4.2 권고 W-A 답습)
- ❌ 외부 library (`pyjcs` / `rfc8785`) 도입 결정 (L-5 = 별도 cycle, ADR-012 §2.1 R-2 / R-4.1 PoC 자동 재실행 trigger)
- ❌ G4 §4.4 Layer 1 / Layer 2 / Layer 3 / Layer 5 영역 진입 결정 (본 brief = Layer 4 한정, 다른 Layer = 별도 cycle 또는 자동 의존 영역)
- ❌ GP-1 / GP-4 / GP-6 / G3 / G4 (Layer 4 외) 영역 진입 결정 (MVP-3 ~ MVP-5 영역 답습)

---

## §9 다음 단계 (단계별 cycle 답습, 자동 진입 0)

1. **본 brief v1 commit** (사용자 승인 후 — 단계별 cycle 답습)
2. **합의 진입** (Reviewer-only 단축 또는 1-agent 직접 — 사용자 영역 명시 시점)
3. **합의 후 SESSION + INDEX commit** (51 entry 등록)
4. **(다음 cycle, 별도 영역, 사용자 명시 시점)**:
   - **(α)** MVP-2 진입 합의 entry brief 작성 (24 entry MVP-1 1.5차 보강 entry brief 답습) — 풀 3+1 + 외부 LLM 1+
   - **(β)** sub-수단 결정 cycle (R-1/2/3/4/5 + L-1/2/3/4/5 결정) — 별도 합의 영역
   - **(γ)** 분리 영역 결정 (예: G4 §4.4 Layer 1/2 의존 영역 우선 진입 vs Layer 4 동시 진입)
5. **본 brief = (α) entry brief 의 *입력 자료***. (α) entry brief 작성 시 본 brief §1 ~ §6 직접 답습 가능.

---

## §10 cross-reference 답습

- **ADR-011 §2.1 (a)~(e) 5조건** (수단/목적 분리, 모법) — `docs/decisions/ADR-011-means-vs-ends-redaction.md`
- **ADR-008 차단조건 #1 보조** (Egress Redaction 인접 영역) — `docs/decisions/ADR-008-hermes-adoption-decision.md`
- **ADR-012 §2.3 + §2.5 + §2.7 + §3.4** (Append-only + Hash Chain + RFC 8785 JCS + prev_hash 실패 + timestamp monotonicity) — `docs/decisions/ADR-012-evidence-ledger-protection.md`
- **governance-preconditions.md §4** (GP-2 정의 + Entry/Exit + 산출 후보 + 의존 ADR)
- **provider-agnostic-memory-skill-design.md §4.4** (Layer 1~5 다층 강제 + Canonical JSON RFC 8785 + Genesis Hash + prev_hash 실패)
- **implementation-runtime-roadmap-mvp1.md §1.2 (3-layer PASS) + §1.3 (GP-2 = MVP-2 분리 사유) + §2.2 (MVP-1 PASS 답습)**
- **implementation-runtime-roadmap.md §3 (G2 영역) + §4 (G4 영역) + §6 (그룹 D 답습)**
- **redaction-pattern-equivalence.md** (R-4 답습, ADR-011 §2.1 (a) 충족)
- **g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md** (Group D PoC — 형식적 검출 layer 한정)
- **r4-1-trigger-extension-evidence.md** (R-4.1 PoC PASS, ADR-011 §2.1 (b) 충족)
- **32 entry 합의** — `docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md` (MVP-1 Implementation Evidence PASS 발효)
- **23 entry audit brief** — `docs/phase0/mvp1-gp3-gp5-current-state-audit-brief.md` (본 brief 답습 source)
- **24 entry entry brief** — `docs/phase0/mvp1-1.5th-reinforcement-entry-brief.md` (본 brief 의 (α) 후속 cycle 답습 source)
- **42 entry actual run id** = `25623028888` (R-6 workflow 답습)
- **43 entry 8 contexts** — main branch protection (`bypass-detect` 포함)
- **50 entry carry-over §4** — `docs/sessions/SESSION_2026-05-27.md` (다음 세션 진입 후보 #4)

---

## §11 자기진단 (메타 편향 회피)

본 brief 작성자 (Claude Opus 4.7) 의 자기 발견 잠재 위험:

| # | 위험 | 본 brief 의 처리 |
|---|------|--------------|
| P-1 | 본 audit 가 MVP-2 진입을 *권유* 하는 방향으로 편향 | §0.2 + §8 금지 사항 다층 명시, "권고 ≠ 결정" 영구 분리 답습 |
| P-2 | 두 영역 통합 권고 (§4) 가 ceremony-inflation 회피를 명분으로 *실패 영역 식별 복잡도* 를 과소평가 | §4.2 단점 명시 + step name 분리 완화 명시 |
| P-3 | sub-수단 후보 (R-4 / L-4) 권고 가 사용자 결정 영역에 무단 침입 | "수단 *결정* = 별도 합의 영역" 영구 분리 답습 (§2.3 + §3.4) |
| P-4 | 50 entry carry-over "G4 §4.4 Layer 4" 해석 (Layer 4 = CI 회귀 검증) 가 사용자 의도와 다를 가능성 | §1.3 + §3.1 해석 명시 + 사용자 검토 시 정정 가능 영역 |
| P-5 | Layer 4 의 의존 영역 (Layer 1 + Layer 2) 미진입 시 Layer 4 단독 진입 의미 부재 | §3.2 Entry 자격 4/5/7 = Layer 1 / test corpus / genesis hash *의존 영역* 명시, §9 (γ) "분리 영역 결정" 명시 |

---

**본 brief v1 끝.**

**다음 단계**: 사용자 승인 → 합의 진입 (Reviewer-only 단축 권고) → SESSION + INDEX commit.

exec
/bin/bash -lc "sed -n '1,520p' docs/phase0/mvp2-entry-brief.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
# MVP-2 진입 합의 entry brief (v1)

> **작성**: 2026-05-28 (52번째 entry 진입 cycle)
>
> **scope**: MVP-2 영역 (G2 GP-2 송신 redaction + G4 §4.4 Layer 4 CI 회귀 검증) 본격 진입 합의
>
> **본 cycle = 큰 cycle** — 24 entry `mvp1-1.5th-reinforcement-entry-brief.md` 답습 형식 (entry brief = 진입 권한 발효 + 후속 sub-cycle 진입 자격 발효)
>
> **본 cycle 발효 자격** = **풀 3+1 합의 + 외부 LLM 1+ 응답 입력 (cross-vendor) + 사용자 명시 결정** 3 조건 모두 충족 시점
>
> **본 cycle 발효 효과** = MVP-2 영역 진입 권한 발효 + (β) sub-수단 결정 cycle 진입 자격 발효 + (γ) 분리 영역 결정 cycle 진입 자격 발효 (수단 결정 / threshold 고정 / 실 코드 = 후속 별도 cycle)

---

## §0 본 brief 의 범위

### §0.1 사용자 진입 명령 답습 (carry-over from 51 entry, commit `f7ac61d`)

51 entry `mvp2-entry-eligibility-audit-brief.md` §9 다음 단계:
- **(α) MVP-2 진입 합의 entry brief 작성** (24 entry MVP-1 1.5차 보강 entry brief 답습) — 풀 3+1 + 외부 LLM 1+ (cross-vendor 의무, 사용자 영역)
- (β) sub-수단 결정 cycle — R-1/2/3/4/5 (GP-2) + L-1/2/3/4/5 (G4 §4.4 Layer 4) — 별도 합의 또는 (α) 內 흡수
- (γ) 분리 영역 결정 — G4 §4.4 Layer 1+2 의존 영역 우선 진입 vs Layer 4 동시 진입

본 (α) cycle 진입 사용자 명시 (2026-05-28, 51 entry commit 후) — "4번으로 진행". 본 brief = (α) 영역 한정. (β) + (γ) = 별도 cycle (본 cycle 발효 후 사용자 명시 시점 진입).

### §0.2 본 brief 가 *하는* 것

1. **MVP-2 영역 정의 답습** — 51 entry audit brief §1.3 (GP-2 송신 redaction + G4 §4.4 Layer 4 CI 회귀 검증) 직접 답습 (§1)
2. **51 entry audit brief 답습 cross-check** — 진입 자격 매트릭스 (GP-2 Entry 2/3 + Exit 2.5/5 / G4 §4.4 Layer 4 Entry 3/8 + Exit 1/5) 정합성 검증 (§2)
3. **선행 권위 답습** — 32 entry MVP-1 Implementation Evidence PASS *완전 발효 (α)* + roadmap-mvp1 §1.2 (3-layer PASS) + §1.3 (GP-2 = MVP-2 분리 사유) + ADR-011 §2.1 (a)~(e) 5조건 모법 (§1.1)
4. **선차 변경 매트릭스** — 선행 권위 (roadmap-mvp1 / governance-preconditions §4.5 / G4 §4.4 / ADR-012 §2.3) vs 본 cycle 결정 사이의 *변경 차이* 명시 (§1.3 ~ 본 brief 핵심 framing)
5. **두 영역 *진입 자격* 분석** — ADR-011 §2.1 (a)~(d) + 합의 APPROVE 운영조건 (e) 5조건 매트릭스 (§3)
6. **본 cycle 합의 형태 = 풀 3+1 + 외부 LLM 1+ *정당화*** (carry-over 답습 + roadmap-mvp1 §1.3 답습) (§4.1)
7. **두 영역 *발효 시점* 합의 형태 권고** (선행 권위 답습) (§4.2)
8. **7 풀 3+1 승격 트리거 *발화 검증*** (본 cycle 자체 ↔ 두 영역별) (§4.3)
9. **Rollback Trigger / Evidence 기준 본문 후보** (§5)
10. **외부 LLM 응답 요구 *입력 자료* 정의 + *응답 자격 검증 기준*** (사용자 준비 영역) (§7)
11. **본 cycle 합의 발효 후 (β) sub-수단 결정 cycle 진입 권한 + (γ) 분리 영역 결정 cycle 진입 권한 발효 자격 명문** (§8)

### §0.3 본 brief 가 *하지 않는* 것 (사용자 명시 답습 + 본 brief 영역 한계)

| # | 영역 | 위반 시점 |
|---|------|----------|
| 1 | 실 코드 / runtime code 구현 | 0건 (Hermes native redaction / P1 facade RedactionFilter / R-6 workflow 확장 / JSONL hash chain verify 본문 모두 0건) |
| 2 | `agent/redact.py` 본문 변경 | 0건 |
| 3 | P1 facade RedactionFilter 본문 변경 | 0건 |
| 4 | `.github/workflows/r2-canary.yml` 본문 변경 | 0건 |
| 5 | `tools/jsonl_chain_verify.py` 또는 동등 신규 생성 | 0건 |
| 6 | `tests/canonical/` 디렉토리 신규 생성 (RFC 8785 reference test corpus) | 0건 |
| 7 | ledger 첫 entry (genesis hash) 작성 | 0건 |
| 8 | 외부 library (`pyjcs` / `rfc8785` / `inotify-tools`) 설치 / 도입 | 0건 (L-5 별도 cycle, ADR-012 §2.1 R-2 / R-4.1 PoC 자동 재실행 trigger) |
| 9 | Tier-2 / Tier-3 vendor catalog 본문 확장 | 0건 |
| 10 | threshold *고정* (canary FP/FN/monotonicity tolerance 등) | 0건 |
| 11 | **GP-2 sub-수단 결정** (R-1 / R-2 / R-3 / R-4 / R-5 中 채택) | 0건 ((β) 별도 cycle, 51 entry brief §9 답습) |
| 12 | **G4 §4.4 Layer 4 sub-수단 결정** (L-1 / L-2 / L-3 / L-4 / L-5 中 채택) | 0건 ((β) 별도 cycle) |
| 13 | **G4 §4.4 Layer 4 분리 영역 결정** (Layer 1+2 의존 영역 우선 vs Layer 4 동시) | 0건 ((γ) 별도 cycle) |
| 14 | **MVP-1 PASS *재선언*** | 0건 (32 entry 답습 그대로 유지) |
| 15 | **MVP-2 Implementation Evidence PASS *발효*** | 0건 ((c) 진입점 = 본 (α) 진입 합의 → (β) sub-수단 결정 → 실 구현 sub-cycle → Implementation Evidence PASS 합의, 다층 분리) |
| 16 | **Operational Readiness PASS (Layer 3)** | 0건 |
| 17 | **Hermes PMO 격상** | 0건 |
| 18 | 외부 LLM 호출 자동 진입 (Claude 영역) | 0건 (사용자 명시 외부 LLM 응답 1+ 별도 첨부 영역 또는 사용자 명시 (α) tmux+codex 자격 답습) |
| 19 | ADR 본문 갱신 (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012) | 0건 (cross-reference 한정도 0건 — 본 brief 발효 후 별도 commit 영역) |
| 20 | 헌법 본문 갱신 (`PROJECT_CONSTITUTION.md`) | 0건 |
| 21 | roadmap-mvp1 §1~§8 본문 변경 | 0건 (cross-reference 답습 한정) |
| 22 | governance-preconditions.md §4 본문 변경 | 0건 |
| 23 | provider-agnostic-memory-skill-design.md §4.4 본문 변경 | 0건 |
| 24 | `src/adapters/llm/facade.py` placeholder → real 본문 (TR-1) | 0건 (별도 trajectory, (d) carry-over) |
| 25 | G4 §4.4 Layer 1 / Layer 2 / Layer 3 / Layer 5 영역 진입 자동 결정 | 0건 (본 brief = Layer 4 한정, 다른 Layer = 별도 cycle 또는 의존 영역 자동) |
| 26 | GP-1 / GP-4 / GP-6 / G3 / G4 (Layer 4 외) 영역 진입 자동 결정 | 0건 (MVP-3 ~ MVP-5 영역 답습) |
| 27 | 본 brief *자체* 영구화 / 권위 chain 등재 | 0건 (본 brief = 본 cycle 합의 input 한정) |

### §0.4 본 brief 의 권위 한계

- ✅ 본 brief 발효 자격 = **풀 3+1 합의 + 외부 LLM 1+ 응답 입력 (cross-vendor) + 사용자 명시 결정** 3 조건 모두 충족 시점
- ✅ 본 brief 발효 결과 = **MVP-2 영역 진입 권한 발효** + (β) sub-수단 결정 cycle 진입 자격 발효 + (γ) 분리 영역 결정 cycle 진입 자격 발효 + Rollback Trigger 본문 채택 + Evidence 형식 본문 채택
- ❌ 본 brief 자체에서 sub-수단 *결정* 0건 (본 brief = entry input, sub-수단 결정 자격은 (β) 별도 cycle)
- ❌ 본 brief 자체에서 threshold *고정* 0건 (후보 한정)
- ❌ 본 brief 자체에서 실 구현 0건 (별도 sub-cycle)
- ❌ 본 brief 자체에서 MVP-2 Implementation Evidence PASS 발효 0건 (실 구현 + 합의 evidence 후 별도 합의)
- ⚠️ 본 brief 합의 후 *자동 sub-수단 결정 / 실 구현 진입 금지* — 사용자 명시 결정 의무 (단계별 합의 cycle 패턴 답습)

---

## §1 진입 컨텍스트 답습

### §1.1 선행 권위 답습 (32 entry + 51 entry + roadmap-mvp1 §1.3)

| 합의 / 권위 | 일자 | 판정 / 본문 | 본 cycle 답습 영역 |
|----------|------|------------|-----------------|
| `3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md` (32 entry) | 2026-05-27 | ✅ **APPROVE WITH CONDITIONS** (풀 3+1 + 외부 LLM 1+) — MVP-1 Implementation Evidence PASS *완전 발효 (α)* | MVP-1 PASS 답습 그대로 유지 (재선언 0). MVP-2 = "Layer 2 Implementation Evidence PASS *2차*" 영역 답습 (roadmap-mvp1 §1.2 line 90 "MVP-2 ~ MVP-5 = GP-2 / GP-4 / GP-6 / G3 / G4 의 본 PASS 단계"). |
| `3plus1-consensus-2026-05-28-mvp2-entry-eligibility-audit.md` (51 entry) | 2026-05-28 | ✅ **APPROVE** (Reviewer-only 단축) — `mvp2-entry-eligibility-audit-brief.md` v1 audit 권위 발효 | 본 (α) brief 의 **직접 입력 자료**. 51 entry audit = "MVP-2 영역 진입 자격 평가 한정", 본 (α) = "MVP-2 영역 진입 합의" (한 단계 격상). |
| `implementation-runtime-roadmap-mvp1.md §1.3` | 2026-05-12 (APPROVED 2026-05-27) | 본문 line 101~107 = "GP-2 = MVP-1 vs MVP-2 분리 사유 (C-7 답습)" — "GP-2 는 **MVP-2** 의 Implementation Evidence PASS 영역 *우선순위 1* (C-7 line 379 답습) — 본 분리는 *시점* 분리이지 *영구 제외* 아님" | 본 cycle = GP-2 시점 진입 자격 발효 (분리 *해제* — *영구 제외* 아님 답습 정확). |
| `implementation-runtime-roadmap.md §6` | 2026-05-09 (APPROVED) | 그룹 D (Order 4+5): G2 GP-3 + G2 GP-2. GP-3 = MVP-1 완료, **GP-2 잔존**. 그룹 C (Order 3 tie): G4 JSONL hash chain + JCS + Round-trip PoC (G4 §4.4 영역) | 본 cycle = 그룹 D 잔존 GP-2 진입 + 그룹 C G4 §4.4 Layer 4 진입 통합. |
| `ADR-011 §2.1 (a)~(e)` | 2026-05-06 | 5조건 모법 — (a) 동등 보안 결과 / (b) 격리 PoC / (c) ADR/SDD 권위 / (d) 자동 회귀 검증 / (e) 합의 APPROVE | 본 cycle = MVP-2 영역 진입 자격 = 5조건 *경로* 권고 (충족 자체는 실 구현 sub-cycle 후 별도 합의). |

### §1.2 두 영역 답습 (51 entry audit brief §1.3 답습)

| 영역 | GP / G | 영역 정의 | 권위 출처 |
|------|--------|---------|---------|
| **GP-2 송신 redaction** | G2 GP-2 | Hermes / Worker Agent stdout / stderr / log file / LLM API request body secret 노출 차단 (Hermes native redaction `agent/redact.py` + P1 facade RedactionFilter + log file canary inject CI step). ADR-011 §2.3 운영 함의 #2 의 *보조* 역할 (DB INSERT 차단 = GP-1 책임, GP-2 = 송신/로그 경로 한정) | `governance-preconditions.md §4` (정의 + Entry §4.4 + Exit §4.5 + 산출 §4.6 + 의존 ADR §4.7) |
| **G4 §4.4 Layer 4 — CI 회귀 검증** | G4 | Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증 + canonical JSON 위반 검출 + timestamp monotonicity 검증 + R-6 workflow 답습 확장. MANDATORY 등급 (Layer 5 中 4번째, Layer 1+2+4 MANDATORY, Layer 3+5 RECOMMENDED MVP) | `provider-agnostic-memory-skill-design.md §4.4.1 line 649~653` (Layer 4 정의) + `ADR-012 §2.3` (다층 강제) + `ADR-012 §3.4` (timestamp monotonicity) |

### §1.3 ⭐ 선차 변경 매트릭스 (선행 권위 vs 본 cycle 결정)

> **본 §1.3 = 본 brief 의 *핵심 framing*** — 선행 권위 (51 entry audit brief / roadmap-mvp1 §1.3 / governance-preconditions §4 / G4 §4.4 / ADR-012 §2.3) 와 본 (α) cycle (2026-05-28) 결정 사이의 *변경 차이* 를 명시. 변경 자격 정당성 = (a) 사용자 명시 권위 우선 + (b) 본 cycle 합의 형태 = 풀 3+1 + 외부 LLM 1+ + 사용자 명시 = ADR-011 §2.1 (e) + §2.4 T3 영역 답습 충실성.

| 영역 | 선행 권위 | 본 cycle 결정 | 권위 정당성 |
|------|---------|--------------|------------|
| **GP-2 시점 분리** | roadmap-mvp1 §1.3 line 103~107 — "GP-2 = MVP-2 로 분리 (C-7 답습) — *시점* 분리이지 *영구 제외* 아님" + governance-preconditions §4.4 line 445 — "⏳ 사용자 명시 GP-2 작업 진입 결정" | **GP-2 시점 분리 해제 — MVP-2 영역 진입 자격 발효** | **✅ 정당** — roadmap-mvp1 §1.3 답습 line 107 "*영구 제외* 아님" 직접 답습. 사용자 명시 + 51 entry audit brief Entry 2/3 충족 + 본 (α) 합의 발효 시 §4.4 line 445 "사용자 명시 GP-2 작업 진입 결정" 충족. |
| **G4 §4.4 Layer 4 진입 자격** | provider-agnostic-memory-skill-design §4.4 line 624 (Layer 1~5 MANDATORY/RECOMMENDED 매트릭스) + ADR-012 §2.3 line 165 "Layer 1 MANDATORY 모든 환경" + line 182 "Layer 4 RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점" | **Layer 4 = MANDATORY 등급, MVP-2 진입 영역 채택** | **⚠️ 권위 미세 충돌 흡수 — ADR-012 §2.3 line 182 = "Layer 4 RECOMMENDED MVP" vs G4 §4.4.1 line 649 = "Layer 4 MANDATORY"**. 본 cycle = G4 §4.4.1 line 649 답습 (Layer 4 = MANDATORY). ADR-012 §2.3 line 182 = Layer 4 *External anchor* (Layer 5 영역) 와 혼동 위험 (line 182 verbatim 재확인 의무, R-S1 유형 잠재 risk → 본 brief §10 P-? 자기진단 영역). 본 (α) 합의 발효 시 cross-reference 정정 cycle 후속 영역. |
| **두 영역 통합 R-6 workflow 확장** | 51 entry audit brief §4 (W-A 통합 권고) — "단일 R-6 workflow 확장으로 두 영역 동시 진행 가능" | **W-A 통합 채택 (본 (α) 합의 발효 시점)** | **✅ 정당** — 51 entry audit brief §4 W-A 권고 직접 답습. 단점 = "step 수 증가 / 실패 영역 식별 복잡도 ↑" 명시 (51 brief §4.2) — step name 분리 완화 답습. |
| **sub-수단 결정 vs 진입 합의 분리** | 51 entry audit brief §9 — "(α) 진입 합의 / (β) sub-수단 결정 cycle" 분리 명시 | **본 (α) cycle = MVP-2 영역 *진입* 합의만, sub-수단 결정 = (β) 별도** | **✅ 정당** — 51 entry brief §9 답습. 단, 24 entry 답습과의 *차이* 명시: 24 entry = "sub-수단 진입 자격 + sub-수단 채택 결정" 통합 / 본 (α) = "영역 진입 자격" 한정 (sub-수단 결정 = (β) 분리). 분리 사유 = MVP-2 영역 sub-수단 매트릭스 (R-1~R-5 × L-1~L-5 = 25 조합) 가 24 entry 4 sub-수단 보다 복잡 + 24 entry "진입 자격 + 채택 결정 통합" 부담 회피 + 단계별 cycle 답습 충실. |

→ **요약**: 본 (α) cycle = "MVP-2 영역 *진입* 합의" 한정 (수단 결정 = (β) 분리). 두 영역 모두 풀 3+1 + 외부 LLM 1+ + 사용자 명시 일관. R-S1 유형 잠재 risk (ADR-012 §2.3 line 182 verbatim 재확인) = §10 자기진단 명시 영역.

---

## §2 두 영역 진입 자격 분석

### §2.1 GP-2 송신 redaction — 진입 자격

#### §2.1.1 영역 정의 (51 entry audit brief §1.3 + governance-preconditions §4 답습)

| 항목 | 내용 |
|------|------|
| **목적** | Hermes / Worker Agent stdout / stderr / log file / LLM API request body secret 노출 차단 (P2 위반 경로 차단) |
| **검증 시점** | Hermes container 운영 시점 (native redaction) + LLM facade 진입점 (RedactionFilter) + CI step (log file canary inject grep, 매 PR + nightly) |
| **메커니즘** | (R-1) Hermes native redaction `agent/redact.py` + (R-2) P1 facade RedactionFilter + (R-3) log file canary inject + grep CI step + (R-4) R-1+R-2+R-3 병행 + (R-5) base64/URL-encoded evasion 별도 (MVP-2/3 분리) |
| **권위 출처** | governance-preconditions.md §4 + ADR-011 §2.3 운영 함의 #2 + roadmap-mvp1 §1.3 (GP-2 = MVP-2 분리 사유) + R-4 답습 (`redaction-pattern-equivalence.md`) + R-4.1 답습 (`r4-1-trigger-extension-evidence.md`) |

#### §2.1.2 진입 자격 (51 entry audit brief §2.1 답습)

| Entry 조건 | 현 상태 | 본 (α) 합의 발효 후 |
|----------|--------|------------------|
| R-4 pattern equivalence 작성 완료 | ✅ 충족 | (그대로 유지) |
| Hermes native redaction `agent/redact.py` 존재 확인 | ✅ 충족 | (그대로 유지) |
| **사용자 명시 GP-2 작업 진입 결정** | ⏳ 본 (α) 합의 영역 | **✅ 본 (α) 합의 발효 시점 충족** |

→ **본 (α) 합의 발효 후 Entry 3/3 모두 충족 → 실 구현 sub-cycle 진입 권한 발효**.

#### §2.1.3 본 cycle 합의 발효 시 채택 결정 영역

✅ **GP-2 영역 진입 발효 자격** — 본 (α) 합의 APPROVE 시점 발효
✅ **(β) sub-수단 결정 cycle 진입 자격 발효** — R-1 / R-2 / R-3 / R-4 / R-5 中 결정 cycle 진입 자격 (별도 합의)
✅ **Rollback Trigger 본문 채택** (§5.1 답습 — RT-1 / RT-2 / RT-3)
✅ **Evidence 형식 본문 채택** (§5.2 답습 — E-1 / E-2 / E-3 / E-7 / E-8 / E-9)

#### §2.1.4 미발효 영역 (deferred)

❌ R-1~R-5 中 sub-수단 결정 = (β) 별도 cycle (51 entry brief §9 답습)
❌ base64 / URL-encoded / 압축 evasion 영역 = R-5 별도 (MVP-2/3 분리, G3-4 답습)
❌ Tier-2 / Tier-3 vendor catalog 본문 확장 = 별도 풀 3+1 + 외부 LLM 1+
❌ Implementation Evidence PASS 발효 = 실 구현 + (b) PoC + (d) R-6 actual run PASS + (e) 합의 APPROVE 후 별도 합의

### §2.2 G4 §4.4 Layer 4 — CI 회귀 검증 — 진입 자격

#### §2.2.1 영역 정의 (51 entry audit brief §3.1 + G4 §4.4.1 + ADR-012 §2.3 답습)

| 항목 | 내용 |
|------|------|
| **목적** | Evidence Ledger 무결성 자동 회귀 검증 — Layer 1 (hash chain) + Layer 2 (history) + canonical JSON 위반 + timestamp monotonicity 위반 자동 검출 |
| **검증 시점** | CI step (매 PR + nightly) — R-6 workflow (`r2-canary.yml`) 답습 확장 |
| **메커니즘** | (L-1) Python stdlib 단독 (`hashlib.sha256` + `json.dumps(sort_keys=True, separators=(",",":"))`) + (L-2) RFC 8785 JCS Primary (`pyjcs` / `rfc8785`) + (L-3) Layer 4 R-6 workflow step + (L-4) L-1+L-3 병행 (MVP 권고) + (L-5) L-2+L-3 병행 (정식) |
| **권위 출처** | provider-agnostic-memory-skill-design.md §4.4.1 line 649~653 (Layer 4 정의) + ADR-012 §2.3 (Append-only + Hash Chain 다층 강제) + §2.5 (RFC 8785 JCS) + §2.7 (prev_hash 실패 처리) + §3.4 (timestamp monotonicity) |

#### §2.2.2 진입 자격 (51 entry audit brief §3.2 답습)

| Entry 조건 | 현 상태 | 본 (α) 합의 발효 후 |
|----------|--------|------------------|
| Design/Governance Gate PASS 답습 (G4 = PASS Bundled) | ✅ 충족 | (그대로) |
| ADR-012 §2.3 Layer 1~5 권위 정의 발효 | ✅ 충족 | (그대로) |
| G4 §4.4 본문 P-1 (RFC 8785 JCS) 흡수 완료 | ✅ 충족 | (그대로) |
| Layer 1 (hash chain) 실 구현 (의존 영역) | ❌ gap | (β) sub-수단 결정 + 실 구현 sub-cycle 영역 |
| canonical JSON test corpus (≥ 20개 RFC 8785 reference) | ❌ gap | 실 구현 sub-cycle 영역 |
| Layer 4 CI step 실 구현 | ❌ gap | 실 구현 sub-cycle 영역 |
| ledger 첫 entry (genesis hash) | ❌ gap | (γ) 분리 영역 결정 cycle 영역 — Layer 1 의존 |
| **사용자 명시 작업 진입 결정** | ⏳ 본 (α) 합의 영역 | **✅ 본 (α) 합의 발효 시점 충족** |

→ **본 (α) 합의 발효 후 Entry 사용자 명시 부분 충족 → 4 gap 의존 영역 = 후속 (β) / (γ) cycle 결정 + 실 구현 sub-cycle 진입 권한 발효**.

#### §2.2.3 본 cycle 합의 발효 시 채택 결정 영역

✅ **G4 §4.4 Layer 4 영역 진입 발효 자격** — 본 (α) 합의 APPROVE 시점 발효
✅ **(β) sub-수단 결정 cycle 진입 자격 발효** — L-1 / L-2 / L-3 / L-4 / L-5 中 결정 cycle 진입 자격 (별도 합의)
✅ **(γ) 분리 영역 결정 cycle 진입 자격 발효** — Layer 1+2 의존 영역 우선 진입 vs Layer 4 동시 진입 (별도 합의)
✅ **Rollback Trigger 본문 채택** (§5.1 답습 — RT-4 / RT-5 / RT-6)
✅ **Evidence 형식 본문 채택** (§5.2 답습 — E-4 / E-5 / E-6 / E-7 / E-8 / E-9)

#### §2.2.4 미발효 영역 (deferred)

❌ L-1~L-5 中 sub-수단 결정 = (β) 별도 cycle
❌ Layer 1 / Layer 2 / Layer 3 / Layer 5 영역 진입 결정 = (γ) 분리 영역 결정 cycle (Layer 1+2 의존 영역 우선 진입 vs Layer 4 동시 결정)
❌ 외부 library (`pyjcs` / `rfc8785`) 도입 결정 = L-5 별도 (ADR-012 §2.1 R-2 / R-4.1 PoC 자동 재실행 trigger)
❌ Implementation Evidence PASS 발효 = 실 구현 + PoC + R-6 actual run PASS + 합의 후 별도

### §2.3 두 영역 통합 R-6 workflow 확장 — 진입 자격

#### §2.3.1 영역 정의 (51 entry audit brief §4 답습)

| 항목 | 내용 |
|------|------|
| **목적** | GP-2 §4.6 산출 후보 (log file canary inject step) + G4 §4.4 Layer 4 (Layer 1+2 자동 회귀 + canonical 위반 + timestamp monotonicity step) **단일 R-6 workflow (`r2-canary.yml`) 확장 통합** |
| **권위 출처** | 51 entry audit brief §4 W-A 권고 (단일 R-6 확장) + governance-preconditions §4.6 line 460 + G4 §4.4.1 line 653 직접 답습 |

#### §2.3.2 진입 자격 (51 entry audit brief §4.2 답습)

✅ 두 영역 모두 R-6 workflow 답습 확장 동일 영역 = W-A 통합 자격 충족
✅ ceremony-inflation 차단 + CI 자원 효율 + evidence 통합 + branch protection contexts 추가 부담 회피 (43 entry 8 contexts 답습) — W-A 정당
⚠️ 단점 명시: step 수 증가 / 실패 영역 식별 복잡도 ↑ (step name 분리 완화)

#### §2.3.3 본 cycle 합의 발효 시 채택 결정 영역

✅ **W-A 통합 채택 결정 발효** — 본 (α) 합의 APPROVE 시점 발효
✅ **R-6 workflow 확장 step name 분리 의무 채택** — 실패 영역 식별 복잡도 완화 답습 (51 brief §4.2 답습)
✅ **branch protection contexts 추가 영역 결정 사용자 영역 carry-over** (8 contexts 답습 유지, 신규 contexts 추가 사용자 영역, 43 entry 답습)

---

## §3 ADR-011 §2.1 (a)~(d) + 합의 APPROVE 운영조건 (e) — 5조건 매트릭스 (두 영역별)

본 §3 = 51 entry audit brief §2.2 + §3.3 매트릭스 답습 (재정리 + 본 (α) 합의 발효 시점 격상 명시).

| # | 조건 | GP-2 (§2.1) | G4 §4.4 Layer 4 (§2.2) |
|---|------|-------------|----------------------|
| (a) | 동등 이상 보안 결과 | ✅ R-4 답습 (`redaction-pattern-equivalence.md`) — 충족 | ❌ gap — 실 구현 sub-cycle 영역 |
| (b) | 격리 환경 PoC 실증 | ⚠️ 부분 (Group D PoC `g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md` 형식적 검출 layer 한정, 송신 redaction PoC = 실 구현 sub-cycle 영역) | ❌ gap — Docker 격리 PoC 3종 (middle entry tampering + canonical 위반 + timestamp monotonicity) = 실 구현 sub-cycle 영역 |
| (c) | ADR / SDD 권위 명시 | ✅ ADR-011 §2.3 + governance-preconditions §4 — 충족 | ✅ ADR-012 §2.3 + G4 §4.4 — 충족 |
| (d) | 자동 회귀 검증 경로 확보 | ❌ gap — **R-6 workflow 답습 확장 (§2.3 W-A 통합)** = 실 구현 sub-cycle 영역 | ❌ gap — **R-6 workflow 답습 확장 (§2.3 W-A 통합)** = 실 구현 sub-cycle 영역 |
| (e) | 합의 APPROVE | ❌ gap — 본 (α) 합의 APPROVE → 진입 권한 발효 / Implementation Evidence PASS 발효 = 별도 합의 (실 구현 + (a)~(d) evidence 완료 후) | ❌ gap — 동일 |

→ **본 (α) cycle 합의 발효 시점 — 두 영역 모두 (e) 진입 *권한* 충족 (Implementation Evidence PASS 발효 ≠ 본 (α), 별도 합의 영역)**.

본 (α) 합의 발효 후 후속 cycle:
- (β) sub-수단 결정 cycle → R-1~R-5 + L-1~L-5 결정 발효
- (γ) 분리 영역 결정 cycle → Layer 1+2 의존 영역 vs Layer 4 동시 결정
- 실 구현 sub-cycle → (a)~(d) evidence 생성 + R-6 workflow 확장 step 통합
- MVP-2 Implementation Evidence PASS 발효 합의 → (a)~(e) 5/5 evidence + 사용자 명시 + 별도 합의

---

## §4 합의 형태 + 풀 3+1 승격 트리거 검증

### §4.1 본 cycle 합의 형태 = 풀 3+1 + 외부 LLM 1+ (carry-over 답습 정당화)

**합의 형태**: **풀 3+1 + 외부 LLM 1+ (cross-vendor 의무)**

**정당화 출처**:
1. 51 entry audit brief §7.2 — "후속 MVP-2 진입 합의 = 풀 3+1 + 외부 LLM 1+" 권고 직접 답습
2. roadmap-mvp1.md §1.3 — "GP-2 = MVP-2 의 Implementation Evidence PASS 영역 *우선순위 1*" (큰 영역 = 풀 3+1 + 외부 LLM 1+ 의무)
3. 32 entry MVP-1 Implementation Evidence PASS 발효 합의 = 풀 3+1 + 외부 LLM 1+ 답습 패턴 (MVP-2 = 동격 영역)
4. 24 entry MVP-1 1.5차 보강 entry brief 합의 = 풀 3+1 + 외부 LLM 1+ 답습 (entry brief 동형 패턴)
5. ADR-011 §2.1 (e) + §2.4 T3 영역 답습 = "큰 결정 (MVP-2 진입) = 풀 3+1 + 외부 LLM 1+ + 사용자 명시"

### §4.2 두 영역 *발효 시점* 합의 형태 권고 (선행 권위 답습)

| 영역 | 본 (α) 합의 (진입 권한) | 실 구현 sub-cycle (수단 결정 + 구현) | Implementation Evidence PASS 발효 |
|------|----------------------|--------------------------------|----------------------------|
| **GP-2** | **풀 3+1 + 외부 LLM 1+** (본 (α)) | **(β) sub-수단 결정 cycle = 풀 3+1** (R-1~R-5 中 R-4 권고, 51 brief §2.3 답습) + 실 구현 별도 sub-cycle (수단별 합의 형태 차등) | **풀 3+1 + 외부 LLM 1+ + 사용자 명시** (32 entry 답습) |
| **G4 §4.4 Layer 4** | **풀 3+1 + 외부 LLM 1+** (본 (α)) | **(γ) 분리 영역 결정 = 풀 3+1** (Layer 1+2 의존 영역 우선 vs Layer 4 동시) + **(β) sub-수단 결정 = 풀 3+1** (L-1~L-5 中 L-4 MVP 권고, 51 brief §3.4 답습) + 실 구현 별도 sub-cycle | **풀 3+1 + 외부 LLM 1+ + 사용자 명시** (32 entry 답습) |

### §4.3 7 풀 3+1 승격 트리거 검증 (본 cycle 자체 ↔ 두 영역별)

본 cycle 자체:

| # | trigger | 본 (α) 발화 | 근거 |
|---|---------|---------|------|
| 1 | 큰 결정 (영역 진입 발효 / 수단 결정 / threshold 고정) | ✅ **발화** | MVP-2 영역 진입 발효 = 큰 결정 (Layer 2 Implementation Evidence PASS 영역 *2차* 진입, roadmap-mvp1 §1.2 답습) |
| 2 | 아키텍처 / SDD / 보안 본문 변경 | ❌ 미발화 | brief = phase0 신규 1 파일, 본문 변경 0 (governance / G4 / ADR-012 본문 0) |
| 3 | ADR 본문 변경 | ❌ 미발화 | brief = ADR 본문 0 (cross-reference 답습 한정) |
| 4 | 권위 chain 다중 source 손상 위험 | ⚠️ **부분 발화 (R-S1 유형 잠재)** | §1.3 G4 §4.4 Layer 4 항목 = ADR-012 §2.3 line 182 verbatim 재확인 의무 (Layer 4 vs Layer 5 혼동 risk). 본 brief §10 P-? 자기진단 영역 명시. Reviewer 단독 verify 자격 (24 entry R-S1 답습 패턴) |
| 5 | 외부 LLM 응답 통합 필요성 | ✅ **발화** | MVP-2 진입 = 큰 영역, cross-vendor 외부 LLM 1+ 의무 (carry-over 답습) |
| 6 | Tier-2/3 catalog 자동 확장 | ❌ 미발화 | brief §0.3 #9 명시 금지 |
| 7 | Hermes PMO 격상 | ❌ 미발화 | brief §0.3 #17 명시 금지 |

→ **3/7 발화 + 1 부분 발화** → **풀 3+1 + 외부 LLM 1+ 합의 적격 (정당화)**.

두 영역별 trigger:

| 영역 | trigger 발화 | 합의 형태 |
|------|----------|---------|
| GP-2 | (1) 큰 결정 (영역 진입) + (5) 외부 LLM (큰 영역) | 풀 3+1 + 외부 LLM 1+ |
| G4 §4.4 Layer 4 | (1) 큰 결정 + (4) 잠재 R-S1 (Layer 4 vs Layer 5 혼동) + (5) 외부 LLM | 풀 3+1 + 외부 LLM 1+ |

---

## §5 Rollback Trigger / Evidence 기준 (본 cycle 합의 발효 시점 의무)

### §5.1 두 영역별 Rollback Trigger 본문 후보 (51 entry audit brief §5 답습)

| # | Trigger | 영역 | 발화 조건 | 권위 답습 |
|---|---------|----|---------|---------|
| RT-1 | Hermes native redaction 우회 검출 | GP-2 | log file canary inject grep PASS 후 평문 leak 발견 | ADR-011 §2.3 #2 + R-7 SOP §5 ROLLBACK trigger R5 |
| RT-2 | P1 facade RedactionFilter 우회 | GP-2 | LLM API request body 평문 secret 검출 | P1 v2 §8.2 + ADR-008 차단조건 #1 보조 |
| RT-3 | base64 / URL-encoded evasion 신규 발견 | GP-2 (R-5 영역) | Tier-1 42 catalog 미커버 evasion 발견 | G3-4 답습 → MVP-2/3 영역 분리 (본 cycle 범위 외) |
| RT-4 | hash chain middle entry tampering 검출 | G4 §4.4 Layer 4 | Layer 1 검증 실패 | ADR-012 §2.7 (`chain_violation_detected` ledger entry) |
| RT-5 | canonical JSON 위반 검출 | G4 §4.4 Layer 4 | Layer 4 CI step FAIL | ADR-012 §2.5 + §원칙 5/6 + R-6 답습 (`canonical_json_fallback` 또는 BLOCK) |
| RT-6 | timestamp monotonicity 위반 | G4 §4.4 Layer 4 | Layer 4 CI step FAIL → BLOCK | ADR-012 §3.4 + R-6 답습 |
| RT-7 | R-6 workflow 자체 silent override | 통합 | gate enforcement bypass detected | G3 §2.6 + G4 §3.8.2 #10 + 43 entry 8 contexts (`bypass-detect`) 답습 |

### §5.2 Evidence Required (51 entry audit brief §6 답습)

| # | Evidence | 출처 |
|---|---------|------|
| E-1 | Hermes native redaction Tier-1 42 catalog 적용 검증 | `agent/redact.py` 실행 evidence (R-4 답습) |
| E-2 | P1 facade RedactionFilter 적용 검증 | facade 진입점 evidence (TR-1 (d) carry-over 의존) |
| E-3 | log file canary inject + grep PASS evidence | Docker 격리 PoC (R-1 / R-4.1 답습) |
| E-4 | hash chain 검증 PoC PASS evidence | middle tampering 차단 PoC (Docker 격리) |
| E-5 | canonical JSON test corpus PASS (≥ 20 RFC 8785 reference) | `tests/canonical/` (G4 §4.4.2 답습) |
| E-6 | timestamp monotonicity 위반 차단 PoC | Docker 격리 (ADR-012 §3.4 답습) |
| E-7 | R-6 workflow 확장 step actual run PASS | GitHub Actions run ID + verdict PASS (43 entry 답습) |
| E-8 | 합의 보고서 commit | 본 (α) 합의 + (β) + (γ) + 실 구현 sub-cycle 별 |
| E-9 | 외부 LLM 응답 1+ (cross-vendor) | `docs/external-review/2026-05-28-mvp2-entry-codex-response.md` 등 |

### §5.3 JSONL Ledger event enum 후보 (본 cycle 합의 발효 시점 신규 등록 영역)

본 cycle 합의 발효 시 신규 등록 자격 (ADR-012 §2.2 답습 + G4 §4.2 11 필드 schema event enum):

| # | event enum 후보 | 영역 | 답습 |
|---|--------------|----|----|
| 1 | `gp2_redaction_layer1_implementation` | GP-2 | ADR-012 §2.2 line 150~152 답습 패턴 (MVP-1 Stage 1/2/3 답습) |
| 2 | `g4_ledger_chain_verify_layer4_implementation` | G4 §4.4 Layer 4 | 동일 답습 |
| 3 | `r6_workflow_extension_mvp2` | 통합 | R-6 답습 확장 시점 |

→ 본 enum 후보 = ADR-012 §2.2 후속 합의 영역 (본 (α) 합의 후 ADR-012 §2.2 cross-reference 갱신 별도 commit).

---

## §6 금지 사항

### §6.1 본 brief 자체 금지 사항

§0.3 답습 (27 항목 재명시 생략).

### §6.2 본 brief 발효 *후* 후속 cycle 진입 시점 금지 사항 (의무 답습)

본 (α) 합의 APPROVE 후 (β) / (γ) / 실 구현 sub-cycle 진입 시:

| # | 금지 영역 | 의무 답습 |
|---|---------|---------|
| 1 | 자동 (β) sub-수단 결정 cycle 진입 | 사용자 명시 의무 (단계별 합의 cycle 답습) |
| 2 | 자동 (γ) 분리 영역 결정 cycle 진입 | 사용자 명시 의무 |
| 3 | 자동 실 구현 sub-cycle 진입 | 사용자 명시 의무 |
| 4 | MVP-2 Implementation Evidence PASS *자동* 선언 | 실 구현 + (a)~(d) evidence + (e) 합의 APPROVE + 사용자 명시 (별도 합의) |
| 5 | 외부 library (`pyjcs` / `rfc8785`) 자동 도입 | ADR-012 §2.1 R-2 / R-4.1 PoC 자동 재실행 trigger 발화 + 별도 cycle |
| 6 | G4 §4.4 Layer 1/2/3/5 영역 자동 진입 | 별도 cycle 또는 의존 영역 자동 (사용자 명시) |
| 7 | GP-1 / GP-4 / GP-6 / G3 / G4 (Layer 4 외) 자동 진입 | MVP-3~MVP-5 영역 (별도 합의) |
| 8 | branch protection contexts 자동 추가 | 사용자 admin scope 영역 (43 entry 답습) |
| 9 | ADR 본문 갱신 자동 cross-reference 변경 | 별도 commit 영역 (R-S1 잠재 정정 영역 포함) |
| 10 | Tier-2/3 catalog 자동 확장 | 별도 풀 3+1 + 외부 LLM 1+ |

---

## §7 외부 LLM 응답 요구 영역 (사용자 준비 자료)

### §7.1 외부 LLM 응답 1+ 의무 답습 출처

1. **51 entry audit brief §7.2** — "후속 MVP-2 진입 합의 = 풀 3+1 + **외부 LLM 1+** 권고 (cross-vendor 의무)" 직접 답습
2. **24 entry MVP-1 1.5차 보강 entry brief** — entry brief 동형 패턴 외부 LLM 1+ 답습
3. **32 entry MVP-1 Implementation Evidence PASS 발효 합의** — 외부 LLM 1+ (codex via tmux cross-vendor) 답습
4. **헌법 5조-2 Provider Liquidity (비협상)** — cross-vendor 검증 의무 (OpenAI ≠ Anthropic)
5. **ADR-011 §2.1 (e) + §2.4 T3 영역** — 큰 결정 = 외부 LLM 1+ + 사용자 명시

### §7.2 외부 LLM 응답 *입력 자료* 정의 (사용자 준비 영역 또는 Claude tmux+codex 직접 호출 영역)

본 (α) cycle 외부 LLM 응답 *입력 자료*:

| 필수 입력 | 자료 위치 |
|---------|---------|
| 본 brief v1 (mvp2-entry-brief.md) | `docs/phase0/mvp2-entry-brief.md` |
| 51 entry audit brief (입력 자료 직접 답습) | `docs/phase0/mvp2-entry-eligibility-audit-brief.md` |
| 51 entry 합의 보고서 | `docs/review/3plus1-consensus-2026-05-28-mvp2-entry-eligibility-audit.md` |
| 32 entry MVP-1 PASS 발효 합의 | `docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md` |
| roadmap-mvp1.md §1.3 (GP-2 = MVP-2 분리 사유) | `docs/architecture/implementation-runtime-roadmap-mvp1.md` |
| governance-preconditions.md §4 (GP-2 정의) | `docs/architecture/governance-preconditions.md` |
| provider-agnostic-memory-skill-design.md §4.4 (Layer 1~5) | `docs/architecture/provider-agnostic-memory-skill-design.md` |
| ADR-012 §2.3 (Append-only + Hash Chain) + §2.5 (RFC 8785 JCS) + §2.7 (prev_hash 실패) + §3.4 (timestamp monotonicity) | `docs/decisions/ADR-012-evidence-ledger-protection.md` |
| ADR-011 §2.1 (a)~(e) 5조건 | `docs/decisions/ADR-011-means-vs-ends-redaction.md` |

**외부 LLM 호출 자격 옵션**:
- **(α) Claude tmux + codex bypass sandbox 직접 호출** (24 entry (α) 답습) — Claude 가 직접 호출, OpenAI ≠ Anthropic cross-vendor 자격 충족
- **(β) 사용자 직접 외부 LLM 호출** (24 entry 답습 외 옵션) — 사용자가 본 brief + 입력 자료 첨부 후 응답 1+ 회수

### §7.3 외부 LLM 응답 *자격 검증* 기준 (Reviewer 검토 영역)

외부 LLM 응답 입력 시 Reviewer 직접 검증 7 기준 (24 entry §7.3 답습):

| # | 기준 | 검증 영역 |
|---|------|---------|
| 1 | cross-vendor 충족 (OpenAI ≠ Anthropic) | vendor identifier 명시 검증 (gpt-X / codex / claude / gemini) |
| 2 | 본 brief v1 입력 자료 직접 읽기 evidence | 응답 본문 내 brief §X verbatim 인용 또는 영역 식별 |
| 3 | ADR-011 §2.1 (a)~(e) 5조건 답습 정확성 | 5조건 매트릭스 검증 |
| 4 | 두 영역 (GP-2 + G4 §4.4 Layer 4) 진입 자격 평가 | 두 영역별 평가 본문 |
| 5 | (β) sub-수단 결정 분리 답습 정확성 | 본 cycle = 영역 진입 한정, sub-수단 결정 = (β) 분리 인식 |
| 6 | Rollback Trigger / Evidence 요건 평가 | RT-1~RT-7 / E-1~E-9 평가 |
| 7 | R-S1 잠재 risk 인식 (ADR-012 §2.3 line 182 Layer 4 vs Layer 5 혼동) | §1.3 자기진단 영역 cross-reference 답습 |

---

## §8 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

### §8.1 본 brief 발효 *후* (= 본 cycle 합의 APPROVE 시점) 다음 단계 (사용자 결정 영역)

본 (α) 합의 APPROVE 발효 후:

1. **(β) sub-수단 결정 cycle** — R-1/2/3/4/5 (GP-2) + L-1/2/3/4/5 (G4 §4.4 Layer 4) — 풀 3+1 합의
   - 본 (α) 권고 (51 brief 답습): GP-2 = R-4 (R-1+R-2+R-3 병행) / G4 §4.4 Layer 4 = L-4 (L-1+L-3 병행 MVP)
2. **(γ) 분리 영역 결정 cycle** — G4 §4.4 Layer 1+2 의존 영역 우선 진입 vs Layer 4 동시 진입 — 풀 3+1 합의
3. **실 구현 sub-cycle** ((β) + (γ) 후) — Hermes native redaction evidence + facade RedactionFilter (TR-1 (d) carry-over 의존) + Layer 1 (hash chain) 구현 + canonical JSON test corpus + R-6 workflow 확장 step + 합의 형태 별 (수단별 차등)
4. **MVP-2 Implementation Evidence PASS 발효 합의** — 실 구현 + (a)~(d) evidence + (e) 합의 APPROVE + 사용자 명시 (32 entry 답습 패턴)
5. **ADR 본문 cross-reference 갱신 별도 commit** — ADR-008 차단조건 #1 보조 cross-reference 추가 + ADR-012 §2.2 event enum 신규 등록 + ADR-011 §8.5 후속 작업에 GP-2 등록 (R-S1 정정 영역 포함)

본 brief 합의는 다음 단계 진입을 *발생시키지 않음* — 사용자 명시 의무 (단계별 합의 cycle 답습).

---

## §9 답습 참조

### §9.1 상위 권위

- **헌법 제8조 (보안)** — `docs/constitution/PROJECT_CONSTITUTION.md`
- **헌법 제5조-2 (Provider Liquidity, 비협상)** — 동상
- **ADR-011 §2.1 (a)~(e) 5조건** (수단/목적 분리, 모법) — `docs/decisions/ADR-011-means-vs-ends-redaction.md`
- **ADR-011 §2.3** (Hermes ≠ root of trust) — 동상
- **ADR-011 §2.4** (T1/T2/T3) — 동상

### §9.2 직접 선행 자료

- **51 entry audit brief** (본 brief 의 직접 입력 자료) — `docs/phase0/mvp2-entry-eligibility-audit-brief.md`
- **51 entry 합의 보고서** — `docs/review/3plus1-consensus-2026-05-28-mvp2-entry-eligibility-audit.md`
- **32 entry MVP-1 PASS 발효 합의** — `docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md`
- **24 entry MVP-1 1.5차 보강 entry brief** (본 brief 구조 답습 source) — `docs/phase0/mvp1-1.5th-reinforcement-entry-brief.md`
- **24 entry 합의 보고서** — `docs/review/3plus1-consensus-2026-05-27-mvp1-1.5th-reinforcement-entry.md`
- **`implementation-runtime-roadmap-mvp1.md`** (특히 §1.2 + §1.3 + §2.2 + §5.1) — `docs/architecture/implementation-runtime-roadmap-mvp1.md`
- **`implementation-runtime-roadmap.md`** (특히 §3 + §4 + §6 그룹 C+D) — `docs/architecture/implementation-runtime-roadmap.md`
- **`governance-preconditions.md §4`** (GP-2 정의) — `docs/architecture/governance-preconditions.md`
- **`provider-agnostic-memory-skill-design.md §4.4`** (Layer 1~5) — `docs/architecture/provider-agnostic-memory-skill-design.md`
- **`ADR-012-evidence-ledger-protection.md §2.3 + §2.5 + §2.7 + §3.4`** — `docs/decisions/ADR-012-evidence-ledger-protection.md`

### §9.3 메타 영역

- `redaction-pattern-equivalence.md` (R-4 답습, ADR-011 §2.1 (a) 충족) — `docs/architecture/redaction-pattern-equivalence.md`
- `r4-1-trigger-extension-evidence.md` (R-4.1 PoC PASS, ADR-011 §2.1 (b) 충족) — `docs/phase0/r4-1-trigger-extension-evidence.md`
- `g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md` (Group D PoC, 형식적 검출 layer 한정)
- ADR-008 차단조건 #1 보조 (`docs/decisions/ADR-008-hermes-adoption-decision.md`)

### §9.4 관련 도구 / workflow (51 entry audit brief §10 답습)

- `agent/redact.py` (Hermes native redaction) — R-1 영역
- P1 facade RedactionFilter — R-2 영역 (TR-1 (d) carry-over 의존)
- `.github/workflows/r2-canary.yml` (R-6 workflow) — R-3 + L-3 영역 (W-A 통합 확장 대상)
- `tools/secret_scanner.py` (Group D Tier-1 42 catalog 답습) — 본 cycle 외 (MVP-1 답습)

### §9.5 본 brief 발효 후 cross-reference 갱신 영역 (별도 commit)

- ADR-008 차단조건 #1 보조 cross-reference 추가 (governance-preconditions §4.7 line 466 답습)
- ADR-012 §2.2 event enum 신규 등록 (gp2_redaction_layer1_implementation / g4_ledger_chain_verify_layer4_implementation / r6_workflow_extension_mvp2)
- ADR-011 §8.5 후속 작업에 GP-2 + G4 §4.4 Layer 4 등록
- **R-S1 정정 영역** (§1.3 ADR-012 §2.3 line 182 Layer 4 vs Layer 5 혼동 verbatim 재확인 + cross-reference 정정) — 본 (α) 합의 발효 후 사용자 명시 시 별도 cycle

---

## §10 본 brief v1 작성 자격 자기진단 (메타 편향 회피)

본 brief 작성자 (Claude Opus 4.7) 의 자기 발견 잠재 위험:

| # | 위험 | 본 brief 의 처리 |
|---|------|--------------|
| **P-1** | 본 brief 가 MVP-2 진입을 *권유* 하는 방향으로 편향 | §0.3 + §6.2 27+10 금지 사항 다층 명시, "본 brief = entry input, 결정 자격은 풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시 3 조건 모두 충족 시점" 영구 분리 (§0.4) |
| **P-2** | (α) cycle 자체에서 sub-수단 결정 (β) 무단 침입 | §0.3 #11 #12 + §1.3 "sub-수단 결정 = (β) 분리" 명시 + §2.1.3 + §2.2.3 "본 cycle = 영역 진입 한정, sub-수단 결정 = (β) 별도 cycle" 다층 답습 |
| **P-3** | 51 entry audit brief 답습이 단방향 (audit → entry) — 51 brief 결함 잔존 시 본 brief 에 cascade | 51 brief 자체 = Reviewer-only 단축 합의 APPROVE 발효 (5/5 trigger 0건 + 14/14 verbatim) — 본 brief = 51 brief 직접 답습 + cross-check (§2 매트릭스 정합성 검증) |
| **P-4** | **⚠️ R-S1 유형 잠재 risk 1 — ADR-012 §2.3 line 182 verbatim 재확인 부족 — Layer 4 vs Layer 5 혼동 위험** | §1.3 G4 §4.4 Layer 4 항목 명시 + §4.3 trigger (4) 부분 발화 명시. 본 brief 발효 후 Reviewer 단독 verify 자격 (24 entry R-S1 답습 패턴, 권위 chain 다중 source 손상 확정 시 §9.5 별도 cycle 영역). 본 brief 의 Layer 4 정의 = G4 §4.4.1 line 649~653 답습 (Reviewer Read 확인 evidence 본 brief 작성 시점 read 완료) |
| **P-5** | 24 entry 답습 동형 패턴 적용이 본 (α) cycle 특수성 무시 위험 | 24 entry = MVP-1 1.5차 보강 (4 sub-수단 진입 + 채택 결정 통합) / 본 (α) = MVP-2 영역 진입 한정 (sub-수단 결정 = (β) 분리) — §1.3 "sub-수단 결정 vs 진입 합의 분리" 명시 + 25 조합 (R-1~R-5 × L-1~L-5) 복잡도 답습 |
| **P-6** | "W-A 통합" 권고 (§2.3) 가 사용자 영역 침입 위험 | §2.3.2 "단점 명시" + 51 brief §4.2 답습 + §6.2 #1 "(β) sub-수단 결정 cycle 자동 진입 0" |
| **P-7** | 두 영역 통합 진행이 GP-2 / G4 §4.4 Layer 4 *각각* 의 영역 특성 무시 위험 | §2.1 + §2.2 각각 별도 분석 + §3 매트릭스 별도 컬럼 + §4.2 발효 시점 합의 형태 권고 각각 명시 |

---

**본 brief v1 끝.**

**다음 단계**: 사용자 승인 → 외부 LLM 자격 옵션 결정 ((α) Claude tmux+codex 직접 호출 또는 (β) 사용자 직접 호출) → 외부 LLM 응답 capture → 풀 3+1 합의 (Agent A/B/C 3 병렬 독립 → Reviewer 통합 + R-S1 verify) → brief v1.1 1pass 흡수 보강 → SESSION + INDEX commit + push.

exec
/bin/bash -lc "sed -n '1,240p' docs/review/3plus1-consensus-2026-05-28-mvp2-entry-eligibility-audit.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
# MVP-2 진입 자격 audit brief APPROVE 합의 보고서 (Reviewer-only 단축 합의)

> **본 합의는 추론적 검증(권고) 한정이며 — 본 합의의 어떤 §도 그 자체로 (i) 실 runtime code / CI workflow / hook 구현 / 변경, (ii) MVP-2 진입 발효, (iii) Implementation Evidence PASS / Operational Readiness PASS 발효, (iv) ADR 본문 갱신, (v) 헌법 본문 갱신, (vi) roadmap-mvp1 본문 갱신, (vii) governance-preconditions / provider-agnostic-memory-skill-design / ADR-012 본문 갱신, (viii) GP-2 / G4 §4.4 sub-수단 *결정* (R-1~R-5 / L-1~L-5), (ix) threshold *고정*, (x) Tier-2/3 catalog 자동 확장, (xi) Hermes PMO 격상, (xii) MVP-1 PASS 재선언, (xiii) `adapters/llm/facade.py` placeholder → real, (xiv) 외부 library (`pyjcs` / `rfc8785`) 도입 결정, (xv) MVP-2 진입 자동 진입 — 어떤 행위도 자동 발생시키지 않는다. 본 합의 = `mvp2-entry-eligibility-audit-brief.md` (372줄) 의 audit 한정 권위 발효 한정 (본문 변경 0건).**

---

**작성일**: 2026-05-28
**합의 형태**: **단축 합의 (Reviewer-only)** — 사용자 명시 결정 답습 + 5/5 풀 3+1 승격 트리거 0건 발화 검증 (§1 답습)
**합의 입력**: `docs/phase0/mvp2-entry-eligibility-audit-brief.md` (v1, 372줄, 2026-05-28)
**1차 권위 답습**: brief §7.1 + §7.3 합의 형태 권고 + ADR-011 §2.1 (a)~(e) 5조건 + 23 entry `3plus1-consensus-2026-05-27-implementation-runtime-roadmap-mvp1-authority.md` 답습 (Reviewer-only 단축 패턴 동형)
**판정**: ✅ **APPROVE (단축 합의 — Reviewer-only) — `mvp2-entry-eligibility-audit-brief.md` v1 audit 권위 발효 가능, 5/5 풀 3+1 승격 트리거 0건 발화**

---

## 0. 합의 대상 + 권위 한계

**대상**: `docs/phase0/mvp2-entry-eligibility-audit-brief.md` (v1, 372줄, §0~§11) audit 권위 발효 한정.

**본 합의가 *발생시키는 것***:
- brief v1 audit 권위 발효 (Reviewer-only 단축 답습)
- 50 entry carry-over #4 "MVP-2 진입 자격 검토" 처리 (audit 산출 = 본 brief)
- 51 entry SESSION log + INDEX 등록
- 본 합의 보고서 commit

**본 합의가 *발생시키지 않는 것*** (brief §0.2 + §8 답습):
- ❌ 실 runtime code / CI workflow / hook 구현 / 변경
- ❌ MVP-2 진입 발효 / Implementation Evidence PASS / Operational Readiness PASS 발효
- ❌ ADR 본문 갱신 (ADR-011 / 012 / 008 / 009 / 010)
- ❌ 헌법 본문 갱신 (T3 영역)
- ❌ roadmap-mvp1.md / governance-preconditions.md / provider-agnostic-memory-skill-design.md 본문 갱신
- ❌ GP-2 sub-수단 결정 (R-1 / R-2 / R-3 / R-4 / R-5)
- ❌ G4 §4.4 Layer 4 sub-수단 결정 (L-1 / L-2 / L-3 / L-4 / L-5)
- ❌ threshold 고정 (catalog 규모 / monotonicity tolerance 등)
- ❌ Tier-2/3 catalog 자동 확장
- ❌ Hermes PMO 격상 / MVP-1 PASS 재선언
- ❌ `adapters/llm/facade.py` placeholder → real (별도 (d) carry-over)
- ❌ 외부 library (`pyjcs` / `rfc8785`) 도입 결정 (L-5 별도 cycle, ADR-012 §2.1 R-2 / R-4.1 PoC 자동 재실행 trigger)
- ❌ G4 §4.4 Layer 1 / Layer 2 / Layer 3 / Layer 5 영역 진입 결정
- ❌ GP-1 / GP-4 / GP-6 / G3 / G4 (Layer 4 외) 영역 진입 결정
- ❌ MVP-2 진입 합의 entry brief 작성 진입 (다음 cycle (α) 사용자 명시 영역)

---

## 1. 5/5 풀 3+1 승격 트리거 검증 결과

brief §7.3 자체 평가 cross-confirm (Reviewer 독립 verify):

| # | trigger | 발화 | 근거 |
|---|---------|------|------|
| 1 | 큰 결정 (수단 결정 / threshold 고정 / 발효) | ❌ 미발화 | brief §0.2 + §8 14+ 금지 명시. 본 brief = audit 한정, 결정 0 / 고정 0 / 발효 0 |
| 2 | 아키텍처 / SDD / 보안 본문 변경 | ❌ 미발화 | brief = 신규 phase0 파일 1개 (`docs/phase0/mvp2-entry-eligibility-audit-brief.md`), 본문 변경 0 (governance-preconditions / provider-agnostic-memory-skill-design / ADR-012 본문 0) |
| 3 | ADR 본문 변경 | ❌ 미발화 | brief = ADR 본문 0 (ADR-011 / 012 / 008 / 009 / 010 cross-reference 답습 한정) |
| 4 | 권위 chain 다중 source 손상 위험 | ❌ 미발화 | brief = cross-reference 답습 한정 (§10 17 source 명시), 24 entry R-S1 유형 손상 0건 |
| 5 | 외부 LLM 응답 통합 필요성 | ❌ 미발화 | brief = 자체 audit, 외부 LLM 응답 0. 외부 LLM 필요 영역 = 후속 (α) MVP-2 entry brief (§7.2 권고) 별도 cycle |

→ **5/5 미발화** = 단축 합의 (Reviewer-only) 적격.

---

## 2. 본 brief 권위 발효 적격성 평가

**(a) 50 entry carry-over §4 답습 정합성**: ✅
- carry-over §4 "MVP-2 진입 자격 검토 (G2 GP-2 송신 redaction + G4 §4.4 Layer 4)" = brief §1.3 영역 정의 정확 답습
- "G4 §4.4 Layer 4" 해석 = provider-agnostic-memory-skill-design §4.4.1 line 649 "Layer 4 — CI 회귀 검증 (MANDATORY)" = brief §3.1 답습
- 본 brief = "audit 한정" scope = 사용자 선택 (a) 답습 (`AskUserQuestion` 답변)

**(b) 의존 권위 source 답습 정확성**: ✅ — 7/7 verify
- ADR-011 §2.1 (a)~(e) 5조건 → brief §2.2 + §3.3 매핑 정확
- governance-preconditions.md §4.4 (Entry) + §4.5 (Exit) → brief §2.1 + §2.2 직접 답습
- provider-agnostic-memory-skill-design.md §4.4.1 Layer 1~5 → brief §3.1 + §3.4 직접 답습
- ADR-012 §2.3 (Append-only + Hash Chain) + §2.5 (RFC 8785 JCS) + §2.7 (prev_hash 실패) + §3.4 (timestamp monotonicity) → brief §3.1 + §5 RT-4/5/6 직접 답습
- roadmap-mvp1.md §1.2 (3-layer PASS) + §1.3 (GP-2 = MVP-2 분리 사유) → brief §1.1 + §1.5 정확 답습
- roadmap.md §3.1 (G2 영역) + §4 (G4 영역) + §6 (그룹 D) → brief §1.3 + §1.4 답습
- 32 entry MVP-1 Implementation Evidence PASS 발효 합의 → brief §1.1 정확 답습 (재선언 0건)

**(c) ADR-011 §2.1 (a)~(e) 충족 자격 매핑 정확성**: ✅
- GP-2 Exit 5조건 매트릭스 (brief §2.2): (a)+(c) 충족 / (b) 부분 / (d)+(e) gap → governance-preconditions §4.5 + R-4 답습 일치
- G4 §4.4 Layer 4 Exit 5조건 매트릭스 (brief §3.3): (c) 만 충족 / (a)/(b)/(d)/(e) gap → ADR-012 §2.3 답습 일치
- 두 영역 모두 (d) 충족 경로 = R-6 workflow 답습 확장 (단일 통합 가능) → brief §4 핵심 발견 정합

**(d) sub-수단 후보 식별 = 결정 0 영구 분리 답습**: ✅
- GP-2 R-1~R-5 (brief §2.3) = 후보 비교만, R-4 권고 = "수단 *결정* = 별도 합의 영역" 영구 분리 답습
- G4 §4.4 Layer 4 L-1~L-5 (brief §3.4) = 후보 비교만, L-4 권고 = "수단 *결정* = 별도 합의 영역" 영구 분리 답습
- L-5 외부 library 도입 = ADR-012 §2.1 R-2 / R-4.1 PoC 자동 재실행 trigger 명시 (brief §8 추가 금지) — 충돌 회피 답습

**(e) 23 entry audit brief 답습 동형 패턴**: ✅
- 23 entry `mvp1-gp3-gp5-current-state-audit-brief.md` (작은 cycle, 1-agent 직접 + Reviewer-only 단축 합의) 답습 패턴 일치
- 본 brief v1 = 372줄 (23 entry audit brief 답습 수준 규모)
- 본 합의 = Reviewer-only 단축 (23 entry 동형)

---

## 3. cross-check verbatim

| brief line / § | verbatim | 평가 |
|---------------|---------|------|
| §0.1 (lines 11~19) | "본 brief 가 *하는* 것 = audit 한정 7 항목" | ✅ audit scope 정확 명시 |
| §0.2 (lines 21~36) | "본 brief 가 *하지 않는* 것 = 14 금지 사항" | ✅ 14 금지 사항 망라적 명시 |
| §1.1 (lines 65~71) | "MVP-1 Implementation Evidence PASS *완전 발효 (α)* — GP-3 5/5 + GP-5 5/5" | ✅ 32 entry 답습 정확 (PR #2 MERGED + main `eb51284` 통합) |
| §1.3 (lines 80~89) | "G2 GP-2 송신 redaction + G4 §4.4 Layer 4 — CI 회귀 검증" | ✅ 50 entry carry-over §4 직접 답습 |
| §1.4 (lines 91~96) | "두 영역 모두 R-6 workflow 답습 확장 영역" 핵심 발견 | ✅ governance-preconditions §4.6 + G4 §4.4.1 Layer 4 line 653 verbatim 일치 |
| §2.1 (lines 109~114) | "Entry 충족 = 2/3 + 1 사용자 영역" | ✅ governance-preconditions §4.4 답습 일치 |
| §2.2 (lines 119~125) | "Exit 5조건 충족 자격 = 2.5/5" | ✅ ADR-011 §2.1 답습 + R-4 충족 / R-6 gap 정확 |
| §3.1 (lines 137~141) | "Layer 4 = CI 회귀 검증 (MANDATORY)" | ✅ provider-agnostic-memory-skill-design §4.4.1 line 649~653 verbatim 일치 |
| §3.2 (lines 146~156) | "Entry 충족 = 3/8 + 1 사용자 영역 (의존 영역 4 gap)" | ✅ Layer 1+2+test corpus+genesis 의존 영역 명시 정확 |
| §3.3 (lines 160~166) | "Exit 5조건 충족 = 1/5 ((c) 만 충족)" | ✅ ADR-012 §2.3 답습 정확 |
| §4 (lines 173~206) | "W-A 통합 권고 (단일 R-6 workflow 확장)" | ✅ ceremony-inflation 차단 메모리 답습 + R-6 직접 답습 |
| §7 (lines 254~278) | "본 cycle = Reviewer-only 단축 / 후속 MVP-2 진입 = 풀 3+1 + 외부 LLM 1+" | ✅ 본 합의 형태 일치 + 24 entry 답습 정확 |
| §7.3 (lines 270~278) | "5/5 풀 3+1 승격 trigger 0건 발화 (자체 검증)" | ✅ 본 §1 Reviewer 독립 verify cross-confirm 일치 |
| §11 (lines 350~358) | "P-1~P-5 자기진단 (편향 / 통합 복잡도 / 권고 무단 침입 / Layer 4 해석 / 의존 영역)" | ✅ 메타 편향 회피 답습 정확 (특히 P-4 Layer 4 해석 사용자 검토 정정 가능 영역 명시) |

→ 14/14 verbatim 확인 완료, 모순 0건.

---

## 4. deferred 영역 명시 (본 합의 *영역 외*)

brief §8 + §9 답습:

- ❌ **(α) MVP-2 진입 합의 entry brief** (24 entry MVP-1 1.5차 보강 entry brief 답습) — 풀 3+1 + 외부 LLM 1+ (cross-vendor)
- ❌ **(β) sub-수단 결정 cycle** — R-1/2/3/4/5 (GP-2) + L-1/2/3/4/5 (G4 §4.4 Layer 4) 결정 cycle (별도 합의 영역)
- ❌ **(γ) 분리 영역 결정** — G4 §4.4 Layer 1/2 의존 영역 우선 진입 vs Layer 4 동시 진입 (Entry 자격 매트릭스 §3.2 답습)
- ❌ 외부 library (`pyjcs` / `rfc8785`) 도입 결정 — ADR-012 §2.1 R-2 / R-4.1 PoC 자동 재실행 trigger
- ❌ G4 §4.4 Layer 1 / Layer 2 / Layer 3 / Layer 5 영역 진입 결정 (의존 영역 또는 별도 권위)
- ❌ GP-1 / GP-4 / GP-6 / G3 / G4 (Layer 4 외) 영역 진입 결정 (MVP-3 ~ MVP-5 영역 답습)
- ❌ `adapters/llm/facade.py` placeholder → real ((d) carry-over, TR-1 trigger)
- ❌ Implementation Evidence PASS 발효 (GP-2 / G4 §4.4 Layer 4 각각) — ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 + 별도 합의
- ❌ Operational Readiness PASS / Hermes PMO 격상 — 별도 권위 영역
- ❌ Tier-2/3 catalog 자동 확장 — 별도 합의 + 외부 LLM 1+

---

## 5. 판정

**판정: APPROVE (단축 합의 — Reviewer-only)**

**근거**:
- §1: 5/5 풀 3+1 승격 trigger 미발화 (자체 + Reviewer 독립 verify cross-confirm)
- §2: 의존 권위 source 답습 7/7 정확 + ADR-011 §2.1 5조건 매핑 정확 + sub-수단 결정 0 영구 분리 + 23 entry 동형 패턴
- §3: 14/14 verbatim 모순 0건
- §4: deferred 영역 명시 (본 cycle 영역 외 모두 분리)
- brief §7.1 권고 (Reviewer-only 단축) + §7.3 자체 평가 (5/5 trigger 0건) 답습

**발효 효과**:
- `docs/phase0/mvp2-entry-eligibility-audit-brief.md` v1 (372줄) audit 권위 발효
- 50 entry carry-over #4 처리 (audit 산출 = 본 brief)
- 51 entry SESSION log 등록 + INDEX 등록
- 본 합의 보고서 commit

**발효되지 않는 영역**: §0 권위 한계 답습 (15+ 금지 사항). MVP-2 진입 발효 / 수단 결정 / threshold 고정 / Implementation Evidence PASS / 외부 library 도입 / 다른 Layer 진입 결정 / 다른 GP 영역 진입 / Hermes PMO 격상 / `facade.py` real 본문 — 모두 별도 합의 + 사용자 명시 결정 의무 영역.

---

## 6. 다음 단계 (사용자 결정 영역)

brief §9 답습 — 본 합의 발효 후:

- (1) ✅ **본 합의로 발효** — brief v1 audit 권위 + 50 entry carry-over #4 처리
- (2) **(α) MVP-2 진입 합의 entry brief 작성** — 24 entry 답습, 풀 3+1 + 외부 LLM 1+ (사용자 영역)
- (3) **(β) sub-수단 결정 cycle** — R-1/2/3/4/5 + L-1/2/3/4/5 결정 (별도 합의)
- (4) **(γ) 분리 영역 결정** — G4 §4.4 Layer 1+2 의존 영역 우선 vs Layer 4 동시 (Entry 자격 매트릭스 답습)
- (5) **(d) `facade.py` placeholder → real** — TR-1 trigger (별도 trajectory, 50 entry carry-over #3)

권고 순서: (α) 또는 (γ) 사용자 결정. (β) = (α) 또는 (γ) 內 흡수 또는 별도. (d) = 다른 trajectory.

본 합의는 다음 단계 진입을 *발생시키지 않음* — 사용자 명시 의무 (단계별 합의 cycle 답습).

---

## 7. 메타 편향 자기진단 (Reviewer 단독)

| # | 잠재 편향 | 본 합의 처리 |
|---|--------|----------|
| M-1 | Reviewer 가 brief 작성자 (Claude) 와 동일 LLM 인 경우 자기 우호 결론 위험 | §1 5 trigger 독립 verify + §3 14 verbatim cross-check 다층 답습 + brief §7.3 자체 평가와 cross-confirm 일치 검증 |
| M-2 | "Reviewer-only 단축" 자체가 풀 3+1 회피 수단 위험 | §1 5/5 trigger 0건 명시 evidence + §7.2 후속 MVP-2 진입 = 풀 3+1 + 외부 LLM 1+ 권고 답습 (회피 영구 차단) |
| M-3 | brief §4 W-A 통합 권고 가 사용자 영역 침입 위험 | brief §4.2 단점 명시 + §11 P-2 자기진단 답습 + §6 다음 단계 = 사용자 결정 명시 |
| M-4 | brief §1.3 "G4 §4.4 Layer 4" 해석 정확성 검증 부족 | provider-agnostic-memory-skill-design §4.4.1 line 649~653 verbatim 직접 read + §3 cross-check 일치 + brief §11 P-4 사용자 정정 영역 명시 |
| M-5 | 23 entry 답습 동형 패턴 적용이 본 cycle 특수성 무시 위험 | 23 entry = roadmap-mvp1 권위 표시 격상 / 본 cycle = MVP-2 진입 자격 audit (영역 다름). 단 합의 *형태* (Reviewer-only 단축 + 본문 변경 0건 + 5 trigger 0건) 동일성 검증 (§1) + 답습 source 정확 매핑 (§2 (e)) |

---

**본 합의 보고서 v1 끝.**

**다음 단계**: SESSION + INDEX commit + 본 합의 보고서 commit (51 entry 답습).

codex
PRIMARY와 51 entry 입력 자료는 확인했습니다. 이제 사용자가 지정한 권위 조항의 실제 문구를 직접 대조해서, 특히 ADR-011의 “(a)~(e)” 표현과 R-S1 Layer 4 충돌 가능성을 판정하겠습니다.
exec
/bin/bash -lc "nl -ba docs/decisions/ADR-011-means-vs-ends-redaction.md | sed -n '1,220p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# ADR-011: Means-vs-Ends Redaction Principle (수단/목적 분리 원칙)
     2	
     3	**상태**: 승인 (단축 합의 — Reviewer-only, 2026-05-06)
     4	**날짜**: 2026-05-06
     5	**의사결정자**: 사용자 + Reviewer 합의 — `docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md`
     6	**상위 권위**: 헌법 제8조 (보안), 헌법 제5조-2 (Provider Liquidity, 비협상), `docs/architecture/system-identity-prequel.md` §3
     7	**갱신 대상**: ADR-008 부록 B Amendment (동시 발행)
     8	**모법 역할**: R-4 / R-5 / R-6 / R-7 작업의 권위 근거
     9	
    10	---
    11	
    12	## 1. 맥락 (Context)
    13	
    14	### 1.1 P2 v2 가정의 붕괴
    15	
    16	ADR-008 부록 A는 R1 (학습루프 평문 누적)을 비협상 CRITICAL 위험으로 명시했다. P2 v2 §2.1.3은 R1 차단 메커니즘으로 "외부 pre-record hook" 형태를 가정 채택했다.
    17	
    18	Phase 0 Day 1 사실 확인(`docs/phase0/day1-environment-and-fact-check.md`)에서 Hermes v0.12.0 main HEAD에 `pre_record` / `add_pre_record_hook` / `before_record` API가 존재하지 않음이 grep 0건으로 확정되었다 (15종 `VALID_HOOKS` 중 DB 기록 직전 가로채기 hook 0개).
    19	
    20	### 1.2 Phase 0 R-1 / R-2 evidence
    21	
    22	- **R-1 검증**(`docs/phase0/day2-r1-redaction-location-verification.md`): Hermes 자체 redaction(`agent/redact.py`)이 LLM 송신/도구 출력/로깅 전용이고 DB INSERT 경로 미적용 확정 → **G1a FAIL**.
    23	  - `agent/redact.py:1-8` docstring 명시: "Regex-based secret redaction for logs and tool output"
    24	  - redact 모듈 import 25개 모두 비-DB 경로
    25	  - `hermes_state.py` (SessionDB) redact import 0건
    26	
    27	- **R-2 PoC**(`docs/phase0/day3-r2-sqlite-trigger-poc.md`): SQLCipher BEFORE INSERT trigger + REGEXP UDF 조합이 Docker 격리 환경(network_mode: none + read_only + cap_drop ALL)에서 6항목 모두 PASS → **G1b PASS by R-2 PoC**.
    28	
    29	### 1.3 ADR 권위 해석 요청 사항
    30	
    31	위 결과는 다음 질문에 대한 ADR 권위 해석을 요구한다:
    32	
    33	> **R1의 "비협상" 본질은 무엇인가 — 특정 구현 수단인가, 보안 결과인가?**
    34	
    35	본 ADR은 이 질문에 답하고, 동시에 다음 3개 인접 안건을 ADR 권위로 정착한다:
    36	- G1a/G1b 게이트 분리 공식화
    37	- "Hermes ≠ root of trust" 권위 위계 영구화 (prequel §3 → ADR 승격)
    38	- 자동 학습 vs 자동 정책 변경 분리
    39	
    40	---
    41	
    42	## 2. 결정 (Decision)
    43	
    44	본 ADR은 다음 4가지를 권위로 선언한다.
    45	
    46	### 2.1 수단/목적 분리 원칙 (Means-vs-Ends Separation)
    47	
    48	**비협상 조건의 본질은 특정 구현 수단이 아니라, 달성해야 하는 안전 결과(safety outcome)이다.**
    49	
    50	- 헌법 제8조 (보안)의 본질은 **DB 평문 저장 차단이라는 결과**이다.
    51	- 외부 hook, redaction 호출, trigger, 암호화 등은 **수단**이다.
    52	- 대체 수단은 다음 4조건을 **모두** 충족할 때 기존 수단을 대체할 수 있다:
    53	
    54	  | # | 조건 | 검증 방식 |
    55	  |---|------|---------|
    56	  | (a) | 동등 이상의 보안 결과 | 명시적 비교표 (수단 A 보장 ↔ 수단 B 보장) |
    57	  | (b) | 격리 환경 PoC로 실증 | Docker isolation + 자동 검증 항목 |
    58	  | (c) | ADR 권위로 명시 | 본 ADR 또는 후속 ADR |
    59	  | (d) | 자동 회귀 검증 경로 확보 | CI/nightly 재실행 (R-6) |
    60	
    61	**원칙 위반**: "수단이 비협상이다"는 텍스트 해석으로 본질 회귀를 차단하는 것은 본 ADR로 무효화된다. 동시에 (a)~(d) 4조건 미충족 시 수단 대체도 금지된다 — 본 ADR은 *수단 자유*가 아니라 *목적 달성 검증 의무*를 강제한다.
    62	
    63	### 2.2 G1a / G1b 게이트 분리 공식화
    64	
    65	P2 v2의 단일 G1 게이트는 본 ADR로 다음 두 게이트로 분해된다.
    66	
    67	```
    68	G1a: Hermes native redaction applies before DB INSERT
    69	   Result: FAIL (R-1 확정)
    70	   Evidence: agent/redact.py docstring "for logs and tool output",
    71	             redact import 25개 모두 비-DB,
    72	             hermes_state.py redact import 0건
    73	   Status: 폐기 (이 경로로 헌법 8조 충족 시도 금지)
    74	
    75	G1b: DB-level fallback prevents plaintext secret persistence
    76	   Result: PASS by R-2 PoC
    77	   Evidence: Docker 격리 환경 (network_mode: none + read_only + cap_drop ALL)
    78	             + SQLCipher BEFORE INSERT trigger + REGEXP UDF
    79	             + 6항목 자동 검증 (C1~C6 모두 PASS)
    80	   Status: PoC PASS, 정식 충족은 R-3~R-5 완료 후
    81	```
    82	
    83	#### G1b 정식 충족 조건 (Phase 1 차단조건 #1 exit 기준)
    84	
    85	| # | 조건 | 산출 |
    86	|---|------|------|
    87	| R-3 | 본 ADR-011 발행 + ADR-008 Amendment | `ADR-011`, `ADR-008` 부록 B |
    88	| R-4 | Hermes redact pattern ↔ P1_REDACTOR 패턴 동등성 검증, gap 발견 시 trigger UDF 보충 | `docs/architecture/redaction-pattern-equivalence.md` |
    89	| R-5 | canary 재검증 트리거 설계 (T13 강화 — config + 주기적 inject) | `docs/architecture/canary-recheck-design.md` |
    90	| R-6 | CI/nightly 회귀 검증 (Hermes 업그레이드 자동 R-2 재실행) | `.github/workflows/r2-canary.yml` |
    91	| R-7 | Phase 1 합격 SOP (canary 패턴/주입/검증/PASS·FAIL 기준) | `docs/phase0/redaction-verification-sop.md` |
    92	
    93	R-3~R-7 모두 완료 시 G1b는 PoC 단계를 벗어나 Phase 1 차단조건 #1 정식 exit 기준이 된다.
    94	
    95	### 2.3 Hermes ≠ Root of Trust
    96	
    97	**Hermes는 시스템의 최종 신뢰 근거가 아니라 검증 대상이다.**
    98	
    99	#### 권위 위계 (Authority Hierarchy)
   100	
   101	```
   102	Constitution
   103	  > ADR
   104	  > SDD
   105	  > Harness Gates
   106	  > Hermes
   107	  > Worker Agents
   108	```
   109	
   110	#### 운영 함의 (Operational Implications)
   111	
   112	1. **Hermes 출력은 Tools로 검증된다**: 린터/타입체커/테스트/trigger/canary가 Hermes 출력 위에 위치한다.
   113	2. **Hermes 자체 redaction은 로그/LLM 송신 방어로만 신뢰**: 저장 경로(DB/파일) 차단 책임 없음.
   114	3. **DB INSERT 경로는 Hermes 외부에서 별도 보호**: SQLCipher trigger 기반 fallback (G1b).
   115	4. **Hermes 의존성 업그레이드는 자동 R-2 재실행으로 회귀 검증**: 신뢰 경계 외부 변경의 자동 검출 (R-6).
   116	5. **Hermes 학습 결과의 자동 정책 반영 금지**: §2.4와 결합.
   117	
   118	#### prequel과의 관계
   119	
   120	본 §2.3은 `docs/architecture/system-identity-prequel.md` §3 ("Hermes ≠ root of trust") 의 prequel(임시) 선언을 ADR 영구 권위로 승격한다. prequel은 R-7 완료 후 P2 v3로 흡수되며 폐기되지만, 본 ADR-011 §2.3은 영구 유지된다.
   121	
   122	### 2.4 자동 학습과 자동 정책 변경 분리
   123	
   124	- **자동 학습은 허용**: Worker Agent가 도구 사용/패턴/실패 사례를 누적 학습하는 것은 시스템 가치의 핵심.
   125	- **자동 정책 변경은 금지**: Constitution / ADR / Harness Gates / Hermes 설정의 변경은 사용자 승인 경로(3+1 합의 또는 단축 합의)를 거쳐야 한다.
   126	
   127	#### 3-tier 분류 (T1 / T2 / T3)
   128	
   129	| Tier | 정의 | 예시 | 승인 경로 |
   130	|------|------|------|---------|
   131	| **T1** | 자동 허용 | Worker Agent 패턴 학습, 도구 사용 빈도 누적, 실패 회피 휴리스틱 | 자동 |
   132	| **T2** | 사용자 승인 필수 | Skill/Memory promotion, 새 도구 등록, 합의 형태 결정 | 사용자 명시 결정 |
   133	| **T3** | 자동 금지 (절대) | Constitution / ADR / Harness Gates 정의 자체의 변경 | 단축 또는 풀 3+1 합의 |
   134	
   135	본 분리는 prequel §6의 3-tier 선언을 ADR 권위로 승격한 것이며, R-5 (canary 재검증) / R-6 (CI 회귀)의 권위 근거이기도 하다 — Hermes 내부 학습 또는 upstream 변경으로 redaction 동작이 silent 깨짐 발생 가능성을 자동 검증으로 차단.
   136	
   137	---
   138	
   139	## 3. R-4 ~ R-7 모법 역할 (Governing Precedent)
   140	
   141	본 ADR은 다음 후속 작업의 권위 근거로 기능한다.
   142	
   143	| 작업 | 산출 | 본 ADR §과의 관계 |
   144	|------|------|----------------|
   145	| **R-4** | `docs/architecture/redaction-pattern-equivalence.md` | §2.1 (a) — 대체 수단(R-2 trigger)이 기존 수단(Hermes redaction) 대비 패턴 커버리지 동등 이상임을 명시적 비교표로 실증 |
   146	| **R-5** | `docs/architecture/canary-recheck-design.md` | §2.4 — Hermes 학습 또는 upstream 변경으로 redaction silent 깨짐 발생 가능성 자동 검증 + §2.3 운영 함의 #4 구현 |
   147	| **R-6** | `.github/workflows/r2-canary.yml` | §2.1 (d) + §2.3 — Hermes 의존성 업그레이드의 자동 회귀 검증 |
   148	| **R-7** | `docs/phase0/redaction-verification-sop.md` | §2.2 G1b 정식 충족 절차의 SOP화 |
   149	
   150	후속 작업은 본 ADR §2를 명시 인용하고, 본 ADR 위반(예: "수단이 비협상이다" 텍스트 회귀, T3 자동 변경 시도) 시 단축 합의 + ADR Amendment 절차로만 갱신 가능하다.
   151	
   152	---
   153	
   154	## 4. 선택지 (Options Considered)
   155	
   156	### 옵션 A: ADR-011 단독 (Amendment 없음)
   157	
   158	- 장점: 일반 원칙 ADR 단일 산출 — 작성 부담 최소
   159	- 단점: ADR-008 부록 A R1 표면 텍스트("외부 pre-record hook 공식 지원")가 갱신되지 않아 ADR-008 본문과 ADR-011 사이 표면 모순. 이력 추적 시 혼란.
   160	
   161	### 옵션 B: ADR-008 Amendment 단독 (ADR-011 없음)
   162	
   163	- 장점: ADR-008 한 문서로 일관
   164	- 단점:
   165	  - "수단/목적 분리"는 R1을 넘어선 일반 원칙 — Amendment에 일반 원칙을 담는 것은 Amendment 형식 위반
   166	  - "Hermes ≠ root of trust" 운영 ADR화는 ADR-008 (Hermes 도입 결정) 범위 초과
   167	  - R-4~R-7이 Amendment를 권위 근거로 인용하는 것은 비표준 (Amendment는 specific 갱신 한정)
   168	
   169	### 옵션 C: ADR-011 신규 + ADR-008 Amendment ⭐ **채택**
   170	
   171	- 장점:
   172	  - 일반 원칙(수단/목적 분리, G1a/G1b 분리, Hermes ≠ root of trust, 학습/정책 분리)은 ADR-011로 권위화
   173	  - ADR-008 부록 A R1 specific 갱신은 Amendment로 짧게 처리 + ADR-011 cross-reference
   174	  - R-4~R-7이 ADR-011을 명확한 모법으로 인용
   175	  - ADR-008 본문 read 시 즉시 R-1 FAIL 후 갱신 사항 파악 가능
   176	- 단점: 작성 분량 2배 (수용)
   177	
   178	---
   179	
   180	## 5. 근거 (Rationale)
   181	
   182	### 5.1 헌법 제8조 본질 재해석의 정당성
   183	
   184	헌법 제8조의 비협상 본질은 "특정 hook이 존재해야 함"이 아니라 "비밀이 평문 영구 저장되지 않음"이다. R-2 PoC는 SQLCipher trigger 기반 fallback이 이 본질을 충족함을 실증했다.
   185	
   186	수단을 비협상으로 굳히면, 수단이 부재한 시점(현 Hermes v0.12.0)에 헌법 제8조 자체를 충족할 수 없는 모순이 발생한다. 본 ADR은 이 모순을 수단/목적 분리로 해소하되, 동시에 (a)~(d) 4조건으로 자의적 수단 대체를 차단한다.
   187	
   188	### 5.2 "Hermes ≠ root of trust" ADR 권위화 필요성
   189	
   190	system-identity-prequel은 임시 선언(Pre-Declaration)으로, R-7 완료 후 P2 v3 흡수와 함께 폐기된다. 그러나 "Hermes ≠ root of trust"는 폐기되어서는 안 되는 영구 권위 원칙이다. 본 ADR-011 §2.3으로 권위 승격하여 prequel 폐기 후에도 보존한다.
   191	
   192	### 5.3 G1a/G1b 분리의 영구화 필요성
   193	
   194	R-1 FAIL과 R-2 PASS는 Phase 0 evidence 보고서에 기록되어 있으나, 이는 보고서이지 ADR 권위가 아니다. G1a/G1b 분리를 ADR로 권위화하지 않으면 미래 합의에서 "G1 단일 게이트로 회귀 가능" 해석 위험이 발생한다. 본 ADR §2.2가 이를 차단한다.
   195	
   196	### 5.4 단축 합의(Reviewer-only)의 정당성
   197	
   198	본 R-3은 새 설계 안건이 아니라 R-1 FAIL + R-2 PASS + 단축 합의 §R-3 (`docs/review/3plus1-consensus-2026-05-05-p2-n1-redaction-reinterpretation.md`) + 풀 합의 §3 권위 위계 (`docs/review/3plus1-consensus-2026-05-05-system-identity-redefinition.md`) 의 ADR 형식화 작업이다. 새 합의 검증이 아니므로 풀 3+1은 과잉. 직전 R-1 단축 합의 패턴 답습.
   199	
   200	---
   201	
   202	## 6. 합의 결과 (단축 합의 — Reviewer-only)
   203	
   204	세부: `docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md`
   205	
   206	| 차원 | 판정 | 핵심 근거 |
   207	|------|------|---------|
   208	| 헌법 제8조 본질 충족 권위화 | **PASS** | §2.1 수단/목적 분리 + (a)~(d) 4조건 명시로 자의적 회귀·자의적 수단 대체 양방향 차단 |
   209	| G1a/G1b 분리 공식화 | **PASS** | R-1 FAIL evidence + R-2 PASS evidence 모두 인용, 정식 충족 조건 명시 |
   210	| Hermes ≠ root of trust 권위 승격 | **PASS** | prequel §3 → ADR §2.3 영구화, 운영 함의 5항목 명문화 |
   211	| 자동 학습 vs 정책 변경 분리 | **PASS** | T1/T2/T3 3-tier 분류 본문 흡수, R-5/R-6 권위 근거화 |
   212	| Provider Liquidity 영향 | **무관** | 본 ADR은 redaction 수단 해석이며 모델/구독 교체 자유와 무관 |
   213	| 메타 편향 통제 | **명시** | 본 ADR은 자체 코드 우호 결론(R-2 PASS)을 반영하나, (a)~(d) 4조건과 R-4~R-7 모법으로 회귀 견제 — 합의 보고서 §메타 편향 자기진단 참조 |
   214	
   215	---
   216	
   217	## 7. 결과 (Consequences)
   218	
   219	### 7.1 긍정적
   220	

exec
/bin/bash -lc "nl -ba docs/architecture/governance-preconditions.md | sed -n '400,490p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
   400	|---|------|------------|
   401	| (a) | 동등 이상의 보안 결과 | R-4 redaction-pattern-equivalence.md (3-way 비교 + Tier-1 42 gap 식별) |
   402	| (b) | 격리 환경 PoC 실증 | R-2 (`docker/r2-poc/`) + R-4.1 (`docker/r4-1-poc/`) |
   403	| (c) | ADR / SDD 권위 명시 | ADR-011 §2.1 + ADR-008 부록 B Amendment |
   404	| (d) | 자동 회귀 검증 경로 확보 | R-6 actual run `25482284523` PASS (24초, 42/42, leak 0) |
   405	| (e) | 합의 APPROVE | R-7 SOP §7.3 단축 합의 (Reviewer-only) `3plus1-consensus-2026-05-07-g1b-phase1-acceptance.md` |
   406	
   407	### 3.6 산출 후보 (보강 — 본 GP-1 범위 *내*)
   408	
   409	본 GP-1 은 G1b 흡수이므로 *추가 산출 0건*. 단, G2 통합 검증 시점에 **본 §3 자체를 G1b cross-reference 형태로 합의 보고서에 인용** — 이중 보호.
   410	
   411	### 3.7 의존 ADR / 갱신 후보
   412	
   413	- ADR-011 §2.1: 본문 변경 없음, §8.5 후속 작업에 G2 GP-1 흡수 등록 (G2 PASS 시점)
   414	- ADR-008 부록 B: 본문 변경 없음, B.6 결과를 G2 GP-1 cross-reference 추가 (G2 PASS 시점)
   415	
   416	---
   417	
   418	## 4. GP-2 — Egress Redaction (로그/LLM 송신)
   419	
   420	### 4.1 정의
   421	
   422	Hermes / Worker Agent 가 stdout / stderr / log file / LLM API request body 에 secret 을 노출하지 않도록 native redaction (`agent/redact.py`) + LLM facade redaction filter (P1 v2 §8.2) 가 사전 차단한다.
   423	
   424	**중요**: GP-2 는 ADR-011 §2.3 운영 함의 #2 의 *보조* 역할. **DB INSERT 차단은 GP-1 의 책임이며, GP-2 는 송신/로그 경로만 다룸**. GP-2 단독으로 헌법 8조 본질 충족 시도 금지.
   425	
   426	### 4.2 위반 경로
   427	
   428	- **P2** — 로그/LLM 송신 경로 평문 노출
   429	
   430	### 4.3 강제 메커니즘
   431	
   432	| 분류 | 메커니즘 | 위치 |
   433	|-----|---------|-----|
   434	| 계산적 | Hermes native redaction `agent/redact.py` (Tier-1 catalog 적용) | Hermes container |
   435	| 계산적 | P1 v2 LLM facade RedactionFilter | P1 facade layer |
   436	| 계산적 | base64 evasion test (R2-6) | `tests/hermes/redaction/test_base64_evasion.py` |
   437	| 계산적 | log file grep canary 자동 검증 | CI step (R-6 확장) |
   438	| 자동 회귀 | Hermes 의존성 업그레이드 시 R-2 / R-4.1 PoC 자동 재실행 (ADR-011 §2.3 운영 함의 #4) | R-6 workflow trigger 확장 |
   439	| 자동 롤백 | R-7 SOP §5 ROLLBACK trigger R5 (Hermes 학습 평문 검출) | R-7 SOP |
   440	
   441	### 4.4 Entry 기준
   442	
   443	- ✅ R-4 pattern equivalence 작성 완료 (충족됨)
   444	- ✅ Hermes native redaction `agent/redact.py` 존재 확인 (R-1 Day 2 evidence)
   445	- ⏳ 사용자 명시 GP-2 작업 진입 결정
   446	
   447	### 4.5 Exit 기준
   448	
   449	| # | 조건 | 검증 방식 |
   450	|---|------|---------|
   451	| (a) | 동등 이상의 보안 결과 | Hermes native redaction Tier-1 42 catalog 적용 검증 + P1 facade redaction filter 검증 |
   452	| (b) | 격리 환경 PoC 실증 | log file canary inject + grep 검증 PoC (Docker 격리) |
   453	| (c) | ADR / SDD 권위 명시 | ADR-011 §2.3 운영 함의 #2 cross-reference + 본 §4 권위 |
   454	| (d) | 자동 회귀 검증 경로 확보 | R-6 workflow 에 log file canary inject step 추가 |
   455	| (e) | 합의 APPROVE | 단축 또는 풀 3+1 합의 (G2 GP-2 한정 또는 G2 통합) |
   456	
   457	### 4.6 산출 후보
   458	
   459	- `tests/hermes/redaction/test_log_canary.py` (log file inject + grep)
   460	- R-6 workflow 확장 — log file canary inject step
   461	- 합의 보고서
   462	
   463	### 4.7 의존 ADR / 갱신 후보
   464	
   465	- ADR-011 §2.3: 본문 변경 없음, §8.5 후속 작업에 GP-2 산출 등록 (G2 PASS 시점)
   466	- ADR-008 차단조건 #1 보조 메커니즘 cross-reference
   467	
   468	---
   469	
   470	## 5. GP-3 — Credential / Secret Hygiene (저장 + 코드)
   471	
   472	### 5.1 정의
   473	
   474	API 키 / OAuth credentials 의 *저장 경로* (런타임) 와 *코드 본문* (개발/배포 시점) 양쪽에서 secret 노출이 차단된다.
   475	
   476	- **저장 경로** (P3): docker secret + chmod 600 + entrypoint stat 검증 + inotify 런타임 감시
   477	- **코드 본문** (P4): pre-commit hook (gitleaks / detect-secrets) + CI step + PR auto-reject
   478	
   479	### 5.2 위반 경로
   480	
   481	- **P3** — Credential / OAuth 파일 권한 노출
   482	- **P4** — 비밀값 하드코딩
   483	
   484	### 5.3 강제 메커니즘
   485	
   486	| 분류 | 메커니즘 | 위치 |
   487	|-----|---------|-----|
   488	| 계산적 | docker secret 정의 | `docker-compose.yml` (ADR-008 차단조건 #6 답습, 35번째 entry R-S1 정정 답습) |
   489	| 계산적 | chmod 600 강제 + entrypoint stat 검증 (R1-2) | Hermes Dockerfile entrypoint |
   490	| 계산적 | inotify 런타임 감시 (mtime/perm 변경 → 컨테이너 정지) | Hermes runtime |

exec
/bin/bash -lc "nl -ba docs/architecture/provider-agnostic-memory-skill-design.md | sed -n '620,670p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
   620	
   621	**P-3 흡수 완료** (2026-05-11): G4 DRAFT 검토 §3.1 P-3 (자기 발견 잠재 위험 — "§4.5 외부 형식 → 본 G4 import 시 schema_version 호환성 (§4.3 #3) — 호환 부재 시 처리 절차 부재") 흡수 완료. **schema_version declaration 절차 = T2 사용자 명시 승인 + §10.2 합의 절차 + §4.5.3 정밀 import 검증 단계**. 본 절차 충족 *전* import = BLOCK (§4.6.5 #1~#3 답습).
   622	
   623	### 4.4 Hash Chain 변조 방지 (**ADR-012 §2.3 + §2.5 + §2.6 + §2.7 + §2.8 답습 — 2026-05-09 PR-2 풀 3+1 합의 보강 + 2026-05-11 P-1 흡수 완료**)
   624	
   625	> **ADR-012 §2.3~§2.8 갱신**: 본 §4.4 = ADR-012 §2.3 (Append-only + Hash Chain 다층 강제) + §2.5 (RFC 8785 JCS) + §2.6 (Genesis Hash) + §2.7 (prev_hash 검증 실패 처리) + §2.8 (Full Rewrite 방어) 답습. 이전 (보강 전) "둘 중 하나 의무" 약 사양 → 다층 강제 사양 + canonical JSON 표준 인용 + 실패 처리 + full rewrite 방어 명시.
   626	>
   627	> **P-1 흡수 완료** (2026-05-11): G4 DRAFT 검토 §3.1 P-1 (자기 발견 잠재 위험 — "JSON canonicalization 표준은 RFC 8785 (JCS) 등 명시 표준 존재. 본 초안은 JCS 직접 인용 안 함") 흡수 완료. **canonical JSON 표준 = RFC 8785 (JCS) IETF informational track 명시 인용** — §4.4.2 Primary 정의 + ADR-012 §2.5 권위. 본 §4.4 의 모든 hash 계산은 RFC 8785 (https://www.rfc-editor.org/rfc/rfc8785) 기준 canonical 형식에 SHA-256 적용. fallback (RFC 8259 escape + lex sort + `jq -S -c` 등) 은 RFC 8785 reference output 동등성 의무 (§4.4.2 답습).
   628	
   629	#### 4.4.1 다층 강제 (Layer 1 ~ Layer 5)
   630	
   631	**Layer 1 — Hash Chain (MANDATORY 모든 환경)**:
   632	- `prev_hash` = 직전 entry 의 `hash` (chain 형성)
   633	- `hash` = 본 entry 의 canonical JSON sha256
   634	- 첫 entry 의 `prev_hash` = `genesis_hash` (§4.4.3)
   635	- SHA-256 hardcode (schema_version 0.1) — `hash_algo` 필드 후속 격상 영역 (ADR-012 §3.2 답습)
   636	- JSONL append-only — entry 수정 / 삭제 / 재작성 금지 (T3 영역, ADR-011 §2.4)
   637	
   638	**Layer 2 — Git Append-only Branch (MANDATORY)**:
   639	- `git config receive.denyNonFastForwards true` (force-push 차단)
   640	- branch protection rule
   641	- pre-commit hook: `git rebase` / `git filter-branch` / `git reset --hard` 감지 시 reject (T3 자동 *방어* 권한, T3 자동 *변경* 금지의 비대칭 활용 — ADR-012 §2.8 답습)
   642	- CI 회귀 검증: base branch 대비 JSONL line deletion / rewrite 감지
   643	
   644	**Layer 3 — Signed Commit (RECOMMENDED MVP, MANDATORY multi-host)**:
   645	- GPG / SSH key signed commit
   646	- 1인 동일 호스트 = SHOULD (G3 §5.5 SPOF 면책)
   647	- Multi-host 전환 / 외부 공유 / 팀 사용 / Hermes PMO 격상 시점 = MUST 승격 (G3 §5.5.3 트리거 답습)
   648	
   649	**Layer 4 — CI 회귀 검증 (MANDATORY)**:
   650	- Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증
   651	- canonical JSON 위반 검출
   652	- timestamp monotonicity 검증 (ADR-012 §3.4)
   653	- R-6 workflow (`.github/workflows/r2-canary.yml`) 답습 확장 (별도 PR — Implementation 영역)
   654	
   655	**Layer 5 — External Anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)**:
   656	- 월 1회 external snapshot (별도 외부 git remote / cloud storage push)
   657	- GitHub Actions run ID + signed tag (ADR-012 §2.8 답습)
   658	- 1인 SPOF 완화 + 침해 후 발견 가능
   659	
   660	**사용자 명시 옵션 답습 (D-1, ADR-012 §2.4)**: "signed commit OR git append commit (둘 중 하나) 의무" — 사용자 결정 영역. 5/5 입력 권고는 *다층 동시 의무* (Layer 1 + 2 MANDATORY, Layer 3 RECOMMENDED). **본 §4.4 = Layer 1 + Layer 2 MANDATORY 답습** (D-1A / D-1B / D-1C 모두 호환).
   661	
   662	#### 4.4.2 Canonical JSON — RFC 8785 JCS Primary + Fallback
   663	
   664	**Primary**: **RFC 8785 JCS** (https://www.rfc-editor.org/rfc/rfc8785) — *informational track*, IETF 권위.
   665	
   666	**Fallback**: `jq -S -c` (lex sort + compact + UTF-8 + RFC 8259 escape) 또는 자체 구현 동등성 의무 + test corpus 검증 (ADR-012 §2.5 답습).
   667	
   668	**구현 라이브러리 후보**:
   669	- Python: `pyjcs` / `rfc8785` / 또는 stdlib `json.dumps(sort_keys=True, separators=(",",":"))` 동등 보장
   670	- Node: `canonicalize` npm

exec
/bin/bash -lc "nl -ba docs/decisions/ADR-012-evidence-ledger-protection.md | sed -n '130,230p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
   130	
   131	| # | enum | 정체성 | T 분류 |
   132	|---|------|------|------|
   133	| 1 | `memory_write` | Memory entry 작성 | T1 (Hermes) / T2 (사용자 promotion) |
   134	| 2 | `skill_proposed` | Skill 후보 추출 | T1 (Hermes 자동) |
   135	| 3 | `skill_approved` | Skill `proposed` → `approved` | T2 (사용자 명시) |
   136	| 4 | `skill_promoted` | Skill `approved` → `promoted` | T2 + Evidence |
   137	| 5 | `skill_revoked` | Skill `promoted` → `revoked` | T3 자동 안전 (rollback_trigger) |
   138	| 6 | `gate_pass` | Gate (G1b/G2/G3/G4 등) PASS 선언 | T2 사용자 명시 |
   139	| 7 | `gate_fail` | Gate FAIL 선언 | T2 사용자 명시 |
   140	| 8 | `external_llm_received` | External LLM response 적재 | **T2 + agent="user" 강제** (원칙 7) |
   141	| 9 | `evidence_forgery_detected` | P10 위반 검출 | T3 BLOCK |
   142	| 10 | `roundtrip_pass` | Round-trip hash 일치 | T1 자동 |
   143	| 11 | `roundtrip_lossy` | Round-trip 의미 보존 (lossy) | T3 사용자 review |
   144	| 12 | `roundtrip_fail` | Round-trip 정책/권한/증거 손실 | T3 BLOCK |
   145	| 13 | `migration_failed` | Migration 검증 실패 (Agent A 권고) | T3 BLOCK + manual |
   146	| 14 | `chain_violation_detected` | prev_hash mismatch 또는 hash 재계산 검출 (외부 LLM 2 C-3) | T3 BLOCK + manual |
   147	| 15 | `hash_chain_broken` | Hash chain 자체 단절 (외부 LLM 1) | T3 BLOCK |
   148	| 16 | `policy_change_attempted` | Hermes 가 정책 변경 시도 (T3 위반) | T3 BLOCK + audit |
   149	| 17 | `canonical_json_fallback` | Canonical JSON `jq -S -c` fallback 사용 | T1 audit |
   150	| 18 | `secret_scan_layer1_implementation` | Secret scan Layer 1 구현 ledger (MVP-1 Stage 1, GP-3 S-1) | T1 audit |
   151	| 19 | `docker_secret_isolation_layer1_implementation` | Docker secret 격리 Layer 1 구현 ledger (MVP-1 Stage 2, GP-3 ST-3) | T1 audit |
   152	| 20 | `provider_adapter_enforcement_layer1_static` | Provider adapter Layer 1 static 검출 ledger (MVP-1 Stage 3, GP-5 T-6) | T1 audit |
   153	| 21 | `pc3_ar1_integration_implementation` | pre-commit + auto-revert 통합 구현 ledger (MVP-1 Stage 4) | T1 audit |
   154	| 22 | `g3_7_workflow_hygiene_implementation` | Workflow hygiene 4 항목 구현 ledger (MVP-1 Stage 5, G3-7) | T1 audit |
   155	| 23 | `provider_key_adapter_bypass_risk_detected` | Provider lock-in 위반 detect (MVP-1 IR-1) | T2 사용자 review |
   156	| 24 | `direct_sdk_with_secret_leakage_detected` | Direct SDK + secret 검출 (MVP-1 IR-2) | T3 BLOCK + manual |
   157	| 25 | `secret_handling_environment_mismatch_detected` | 환경 secret mismatch detect (MVP-1 IR-3) | T2 사용자 review |
   158	
   159	**MVP 의무 12 enum** (1~12, schema_version 0.1 도입). **후속 확장 5 enum** (13~17, schema_version 0.2 진입). **MVP-1 신규 8 enum** (18~25, schema_version 0.2 정식 등록 — Backlog #5 합의 `docs/review/3plus1-consensus-2026-05-13-adr-012-event-enum-registration.md` 권위, MVP-1 PASS §C-2 충족).
   160	
   161	**Provider-neutral 강제** (Agent B C-16): 11 필드 모두 provider-specific 식별자 미허용.
   162	
   163	### 2.3 Append-only 원칙 + Hash Chain (다층 강제)
   164	
   165	**Layer 1 — Hash Chain (MANDATORY 모든 환경)**:
   166	- `prev_hash` = 직전 entry 의 `hash` (chain 형성)
   167	- `hash` = 본 entry 의 canonical JSON sha256
   168	- 첫 entry 의 `prev_hash` = `genesis_hash` (§2.6)
   169	- SHA-256 hardcode (schema_version 0.1) — `hash_algo` 필드 후속 격상 영역 (§3.2 답습)
   170	
   171	**Layer 2 — Git append-only branch (MANDATORY)**:
   172	- `git config receive.denyNonFastForwards true` (force-push 차단)
   173	- branch protection rule
   174	- pre-commit hook: `git rebase` / `git filter-branch` / `git reset --hard` 감지 시 reject
   175	- CI 회귀 검증: base branch 대비 JSONL line deletion / rewrite 감지
   176	
   177	**Layer 3 — Signed commit (RECOMMENDED MVP, MANDATORY multi-host)**:
   178	- GPG / SSH key signed commit
   179	- 1인 동일 호스트 = SHOULD (SPOF 면책)
   180	- Multi-host 전환 / 외부 공유 / 팀 사용 / Hermes PMO 격상 시점 = MUST 승격 (G3 §5.5.3 트리거 답습)
   181	
   182	**Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)**:
   183	- 월 1회 external snapshot (별도 외부 git remote / cloud storage push)
   184	- GitHub Actions run ID + signed tag (Agent B C-4 권고)
   185	- 1인 SPOF 완화 + 침해 후 발견 가능
   186	
   187	### 2.4 Signed commit OR Git append commit (사용자 명시 답습)
   188	
   189	**사용자 명시 결정 답습**: "signed commit 또는 git append commit (둘 중 하나) 의무".
   190	
   191	**5/5 입력 권고**: Layer 1 + Layer 2 동시 의무 (Hash chain + Git append-only) + Layer 3 RECOMMENDED.
   192	
   193	**옵션** (사용자 결정 영역 — D-1):
   194	
   195	| 옵션 | 정체성 | 적용 |
   196	|-----|------|---|
   197	| **D-1A** (사용자 명시 답습) | "둘 중 하나 의무" 그대로 — 최소 = git append-only, signed = 권장 | 사용자 결정 |
   198	| **D-1B** (5 입력 권고) | "Hash chain + Git append-only MANDATORY + Signed RECOMMENDED" 다층 | 사용자 결정 |
   199	| **D-1C** (절충, Reviewer 권고) | MVP = "둘 중 하나 의무" + Implementation 시점 다층 격상 | 사용자 결정 |
   200	
   201	**본 ADR 의 권위 결정**: D-1A / D-1B / D-1C 모두 본 ADR §2.3 Layer 1 + Layer 2 동시 의무 *호환*. 단 사용자 명시 결정 영역 — 본 ADR 갱신은 단축 합의 가능.
   202	
   203	### 2.5 RFC 8785 JCS Canonicalization (채택 + Fallback)
   204	
   205	**Primary**: RFC 8785 JCS (https://www.rfc-editor.org/rfc/rfc8785) — *informational track*, IETF 권위.
   206	
   207	**Fallback**: `jq -S -c` (lex sort + compact + UTF-8 + RFC 8259 escape) 또는 자체 구현 동등성 의무 + test corpus 검증.
   208	
   209	**구현 라이브러리 후보** (Agent C C-3 권고):
   210	- Python: `pyjcs` / `rfc8785` / 또는 stdlib `json.dumps(sort_keys=True, separators=(",",":"))` 동등 보장
   211	- Node: `canonicalize` npm
   212	- Go: `cyberphone/json-canonicalization` / `gowebpki/jcs`
   213	
   214	**Test corpus 의무** (외부 LLM 2 C-6):
   215	- `tests/canonical/` 디렉토리에 RFC 8785 reference 출력 ≥ 20개 포함
   216	- CI 회귀 검증: 입력 → 자체 canonical → JCS reference output 비교
   217	- 불일치 시 BLOCK
   218	
   219	**Fallback 사용 시 의무**:
   220	- `event: canonical_json_fallback` ledger entry 작성 의무
   221	- Reviewer 알림 + 사용자 review 권장
   222	
   223	### 2.6 Genesis Hash 정의
   224	
   225	**MVP (schema_version 0.1) — 현 G4 §4.4 정의 유지**:
   226	
   227	```
   228	genesis_hash = sha256("genesis:<scope>:<schema_version>")
   229	```
   230	

exec
/bin/bash -lc "nl -ba docs/decisions/ADR-012-evidence-ledger-protection.md | sed -n '230,360p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
   230	
   231	**0.2 진입 또는 multi-chain 도입 시 (외부 LLM 2 C-7)**:
   232	
   233	```python
   234	genesis_hash = sha256("genesis:" + canonical_json({
   235	  "scope": <scope>,
   236	  "schema_version": <version>,
   237	  "created_at": <ISO 8601>,
   238	  "agent": "user"
   239	}))
   240	```
   241	
   242	**전이 절차**: 0.1 chain 의 첫 entry 는 MVP 정의로 유지. 0.2 진입 시 새 chain (별도 `chain_id` 또는 schema_version) 생성, 기존 0.1 chain 은 read-only.
   243	
   244	### 2.7 prev_hash 검증 실패 처리 (BLOCK + Manual Review)
   245	
   246	**처리 절차** (4/5 합의 답습 — 합의 §2.2 #8):
   247	
   248	1. **즉시 BLOCK** — import / export / migration 중단
   249	2. **기존 원본 JSONL 보존** — 자동 revert 금지 (T3 위반 위험)
   250	3. **새 violation entry append** — `event: chain_violation_detected` ledger entry 작성:
   251	   ```jsonl
   252	   {"type":"meta","scope":"<scope>","event":"chain_violation_detected","content":{"violation_type":"prev_hash_mismatch|hash_recalculation|history_rewrite","detected_at":"<ts>","affected_entry":"<id>","prev_hash_expected":"<sha256>","prev_hash_actual":"<sha256>"},...}
   253	   ```
   254	4. **사용자 명시 review 의무** — 자동 PASS 금지
   255	5. **자동 revert 금지** (T3 위반 — ADR-011 §2.4)
   256	6. **Dual write 금지** (silent failure 위험)
   257	
   258	**검출 layer**:
   259	- Layer 1: pre-commit hook (입력 entry 의 `prev_hash` 검증)
   260	- Layer 2: pre-push hook (chain 전체 재검증)
   261	- Layer 3: CI nightly 회귀 검증 (R-6 답습 확장)
   262	- Layer 4: import script (`scripts/hermes-migration/import.py` — 향후 Implementation 시점)
   263	
   264	### 2.8 Full Rewrite 방어 (다층)
   265	
   266	**5 Layer 강제** (합의 §3.5 답습):
   267	
   268	- **Layer 1**: Hash chain (middle entry tampering 차단)
   269	- **Layer 2**: Git append-only branch + denyNonFastForwards (history 재작성 차단)
   270	- **Layer 3**: pre-commit hook — `git rebase` / `git filter-branch` / `git reset --hard` 감지 시 reject (T3 자동 *방어* 권한, T3 자동 *변경* 금지의 비대칭 활용 — 외부 LLM 2 §3.3)
   271	- **Layer 4**: CI 회귀 검증 — base branch 대비 JSONL line deletion / rewrite 감지
   272	- **Layer 5 (RECOMMENDED MVP, MANDATORY multi-host)**: External anchor — GitHub Actions run ID + signed tag (Agent B C-4) 또는 월 1회 external snapshot (외부 LLM 2 C-4)
   273	
   274	**1인 동일 호스트 SPOF 한계 명시** (외부 LLM 1 권고 5 직접 인용):
   275	
   276	> 동일 호스트 전체 침해 상황은 본 ADR-012 의 완전 방어 범위 밖이다. 본 ADR 은 Hermes container compromise, middle-entry tampering, accidental rewrite, migration 손실, evidence forgery 시도에 대한 탐지와 차단을 목표로 한다.
   277	
   278	### 2.9 Round-trip Lossy 검출 (Tier-based)
   279	
   280	**검증 PASS 조건** (4/5 합의 답습 — 합의 §3.3):
   281	
   282	| Tier | 정체성 | PASS 조건 |
   283	|-----|------|------|
   284	| **Genesis (신규 chain)** | 첫 entry 작성 | (round-trip 무관) |
   285	| **T2 (Skill/Memory promoted, 로컬)** | 로컬 promotion 절차 | **hash 일치 STRICT** — 손실 0건. 위반 시 BLOCK + `event: roundtrip_fail` |
   286	| **T3 (Cross-vendor migration)** | 외부 형식 변환 + 재import | 의미 보존 허용 — (i) 손실 영역 자동 enumeration / (ii) `event: roundtrip_lossy` 의무 / (iii) 사용자 명시 review + ADR-011 §2.4 사용자 승인 / (iv) 정책/권한/증거 손실 BLOCK |
   287	
   288	**Ledger entry 3 형식**:
   289	
   290	```jsonl
   291	{"type":"meta","scope":"<scope>","event":"roundtrip_pass","content":{"source_chain":"<id>","target_provider":"openai","hash_match":true},...}
   292	{"type":"meta","scope":"<scope>","event":"roundtrip_lossy","content":{"source_chain":"<id>","target_provider":"openai","lost_fields":["evidence_refs.confidence_score"],"semantic_diff":"<user-review-summary>"},...}
   293	{"type":"meta","scope":"<scope>","event":"roundtrip_fail","content":{"source_chain":"<id>","target_provider":"openai","failure_reason":"chain_violation_detected|policy_loss|permission_loss|evidence_loss"},...}
   294	```
   295	
   296	**자동화 vs 사용자 review 분리**:
   297	- `lost_fields` enumeration = 자동 (canonical JSON diff)
   298	- `semantic_diff` 판단 = 사용자 명시 review (ADR-011 §2.4 T2/T3 사용자 승인)
   299	- **의미 보존 review 자동화 절대 금지** (Agent A R-4)
   300	
   301	### 2.10 JSONL Export / Import 무결성
   302	
   303	**Export** (Hermes 의존 0 — ADR-008 차단조건 #2 답습):
   304	- `scripts/hermes-migration/` 변환 스크립트 = `import hermes_agent` 0건 (depcruise 검증, G2 GP-5 답습)
   305	- 표준 도구 (`jq` + `sha256sum`) 만으로 검증 가능
   306	- 외부 오케스트레이터 (claude / openai / gemini / local) 최소 2+ 재해석 가능
   307	
   308	**Import 의무 검증** (외부 LLM 2 C-11):
   309	1. `schema_version` 필드 존재 확인 (없으면 BLOCK)
   310	2. 호환성 매트릭스 조회 — 현 MVP 0.1 only, 외부 형식 매핑은 별도 (Implementation 영역)
   311	3. 미일치 시 BLOCK + 사용자 명시 manual approval 요구
   312	4. Hash chain 검증 (§2.7 답습)
   313	
   314	**Migration 검증 실패 = `event: migration_failed`** (Agent A 권고 + 합의 §4.3):
   315	1. BLOCK
   316	2. 원본 보존
   317	3. 새 `event: migration_failed` entry append:
   318	   ```jsonl
   319	   {"type":"meta","scope":"<scope>","event":"migration_failed","content":{"source_provider":"hermes","target_provider":"openai","failure_step":"export|conversion|import|reverify","error_summary":"..."},...}
   320	   ```
   321	4. 사용자 명시 manual review 의무
   322	5. 자동 revert 금지
   323	
   324	### 2.11 Evidence Forgery 방지 (P10 정식 등록 트리거)
   325	
   326	**P10 정식 등록 트리거** = 본 ADR-012 발행 시점 (G2 §1.2.5.2 답습).
   327	
   328	**G2 §1.2 본문 P10 row 추가는 별도 G2 update PR** (본 ADR 범위 외 — 합의 §4.2):
   329	- 사용자 명시 결정 답습 — PR-2 = ADR-012 + G4 §4.4/§4.6 한정
   330	- G2 본문 변경 = T3 변경 + 별도 합의 (단축 가능)
   331	- 본 ADR §1.3 cross-reference 명시는 의무
   332	
   333	**Evidence Forgery 공격 모델 5종** (외부 LLM 2 §6 답습):
   334	
   335	| # | 공격 | 본 ADR 방어 유효성 | 보강 |
   336	|---|------|--------------|----|
   337	| (a) | 1인 호스트 침해 | **약** — host 전체 침해 시 모든 layer 우회 | Layer 5 external snapshot (월 1회) |
   338	| (b) | Hermes container compromise | **강** — Hermes 는 ledger write 권한 0 (G3 §2 T3) | (그대로) |
   339	| (c) | Git history rewrite | **중** — Layer 2~4 차단, 그러나 host 권한 상승 시 force push 가능 | (a) 동일 + Layer 5 |
   340	| (d) | JSONL middle tampering | **강** — Layer 1 (hash chain) 정확히 이 케이스 차단 | (그대로) |
   341	| (e) | External LLM response 위조 | **약** — vendor API key / signed response 부재 시 검증 부족 | 원칙 7 (`agent="user"` 강제) + Layer 3 권장 |
   342	
   343	### 2.12 Hermes 변조 차단 매트릭스 4항목 (Agent B Gap-17 HIGH)
   344	
   345	본 §2.12 = Agent B Gap-17 HIGH 흡수 — Hermes ≠ root of trust 운영 매커니즘:
   346	
   347	| # | 변조 영역 | 차단 매커니즘 | G3 cross-reference |
   348	|---|--------|---------|----|
   349	| 1 | **Hermes-originated ledger entry** (Hermes 자기 entry 작성 시도 — T1 자동 학습 vs T2 사용자 승인 분기) | Hermes container `~/.claude/global/` write 권한 0 + Hermes-originated commit auto-reject | G3 §2.5 #11 + G3 §2.2 #20 |
   350	| 2 | **파일 변조 (filesystem 직접 변경)** | `evidence/<scope>.jsonl` filesystem read-only + audit log + 컨테이너 정지 | G3 §4.5 |
   351	| 3 | **Git commit (Hermes 가 ledger commit 시도)** | Hermes-originated commit auto-reject (commit author = Hermes 검출 시 차단) | G3 §2.2 #20 |
   352	| 4 | **외부 LLM 응답 위조 (Hermes 가 외부 LLM response 를 자기 제안으로 위조)** | External LLM response ledger entry `agent = "user"` 강제 (수동 paste 시) + signed commit 권장 (multi-host 시 의무) | G3 §2.5 #9 + 본 §2.1 원칙 7 |
   353	
   354	**4 항목 모두 본 ADR 권위로 차단**. ADR-011 §2.3 (Hermes ≠ root of trust) 운영 매커니즘 흡수.
   355	
   356	---
   357	
   358	## 3. 추가 의무 (5)
   359	
   360	### 3.1 External LLM Response Ledger Entry (N-1)

exec
/bin/bash -lc "nl -ba docs/constitution/PROJECT_CONSTITUTION.md | sed -n '1,180p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# 프로젝트 헌법 (Project Constitution)
     2	
     3	> **AI 자동화 개발 도구의 최상위 원칙 — 모든 개발은 이 문서를 기준으로 한다**
     4	
     5	**제정일**: 2026-04-06
     6	**상태**: 시행 중
     7	
     8	---
     9	
    10	## 제1조: 설계 문서 우선 원칙 (SDD)
    11	
    12	1. 모든 기능 구현 전에 설계 문서가 존재해야 한다
    13	2. 코드와 문서가 불일치할 경우 **문서가 기준**이며, 코드를 수정한다
    14	3. 설계 문서 없이 코드를 작성하는 것은 금지한다
    15	4. 설계 문서의 변경은 반드시 이력이 추적되어야 한다
    16	
    17	## 제2조: 테스트 우선 원칙 (TDD)
    18	
    19	1. 모든 코드는 TDD 사이클(RED → GREEN → REFACTOR)을 따른다
    20	2. 테스트 커버리지 목표: **최소 70%**
    21	3. 테스트 없는 코드는 프로덕션에 배포할 수 없다
    22	4. 테스트는 명세(specification)의 실행 가능한 형태이다
    23	
    24	## 제3조: 하네스 엔지니어링 원칙
    25	
    26	1. **Agent = Model + Harness**: 모델의 능력만으로는 불충분하며, 하네스가 품질을 보장한다
    27	2. 가이드(Feedforward)와 센서(Feedback)를 균형 있게 설계한다
    28	3. 계산적(Computational) 검증을 추론적(Inferential) 검증보다 우선한다
    29	4. 하네스의 모든 구성요소는 **왜 필요한지** 근거가 있어야 한다
    30	5. 모델이 발전하면 더 이상 필요 없는 하네스 요소는 제거한다
    31	
    32	## 제4조: 멀티 에이전트 합의 원칙
    33	
    34	1. 아키텍처, 보안, SDD 명세에 관한 결정은 **3+1 에이전트 합의**를 거친다
    35	2. **아이디어 검증** 요청 시 반드시 3개 에이전트가 병렬로 독립 분석한다
    36	3. 에이전트 간 출력은 서로 참조하지 않는다 (편향 방지)
    37	4. 검토 에이전트의 합의 보고서에는 채택/미채택 근거가 반드시 포함된다
    38	5. 일반 코딩/버그 수정은 에이전트 프로토콜 없이 직접 수행한다
    39	
    40	## 제5조: 코드 품질 원칙
    41	
    42	1. 코드는 읽기 쉬워야 한다 — 주석이 필요하면 코드가 복잡한 것이다
    43	2. 단일 책임 원칙(SRP)을 준수한다
    44	3. 중복을 제거하되, 조기 추상화는 피한다
    45	4. 외부 입력(사용자 입력, API 응답)만 검증한다. 내부 코드는 신뢰한다
    46	5. 린터/포매터 규칙을 자동 적용한다
    47	
    48	## 제6조: 모듈 독립성 원칙
    49	
    50	1. 모듈 간 직접 의존은 최소화한다
    51	2. 모듈 간 통신은 명확한 인터페이스(API/이벤트)를 통한다
    52	3. 순환 의존은 금지한다
    53	
    54	## 제7조: 투명성 원칙
    55	
    56	1. 모든 의사결정은 ADR(Architecture Decision Record)로 기록한다
    57	2. 에이전트 합의 과정의 개별 의견과 최종 판단 근거가 공개된다
    58	3. 세션 로그를 통해 작업 이력을 추적할 수 있어야 한다
    59	
    60	## 제8조: 보안 원칙
    61	
    62	1. 비밀값(API 키, 토큰)은 코드에 하드코딩하지 않는다
    63	2. 환경 변수 또는 비밀 관리 서비스를 사용한다 (개발: `.env`, 프로덕션: 시크릿 매니저)
    64	3. 사용자 입력은 항상 검증하고 이스케이프한다
    65	4. 보안 관련 변경은 반드시 3+1 에이전트 합의를 거친다
    66	
    67	## 제8-2조: 환경 관리 원칙
    68	
    69	1. **하드코딩 제로**: 포트, URL, 모델명 등 모든 설정값은 환경 변수로 관리한다
    70	2. **중앙 관리**: `.env` + `.env.example` 2-파일 전략. 한 곳에서 수정한다
    71	3. **Docker-First**: `docker compose up`이 기본 실행 환경이다
    72	4. **Fail-Fast**: 필수 환경 변수 누락 시 앱 시작을 즉시 중단한다
    73	5. **점진적 확장**: MVP 최소 변수로 시작, 서비스 추가 시 변수를 추가한다
    74	
    75	## 제5조-2: Provider Liquidity 원칙 (비협상)
    76	
    77	1. 모든 LLM/AI 도구 관련 결정은 Provider Liquidity 제약을 만족해야 한다 — 어떤 모델, 구독, 오케스트레이터에도 락인되지 않아야 하며, 교체가 코드 변경 없이 가능해야 한다 (메모리 line 7 답습)
    78	2. LLM provider 선택은 코드가 아닌 설정 파일(YAML 등)에서만 — 모델명·provider 분기 코드는 금지 (메모리 line 12 답습)
    79	3. 단일 provider 의존 시스템 금지 — 최소 2 provider always-on 원칙 (메모리 line 14 답습)
    80	4. 본 원칙은 비협상 — ADR-011 line 6 **상위 권위 매핑 답습** ("헌법 제8조 (보안), 헌법 제5조 (Provider Liquidity)"). **다른 권위 위계 (예: 8-2조 환경 관리 원칙 vs 5조-2) 자격 평가 = 본 cycle 범위 외, 별도 cycle 의무**
    81	
    82	## 제9조: Git 워크플로우 원칙
    83	
    84	1. Conventional Commits 형식을 따른다
    85	2. 의미 있는 단위로 커밋한다 (한 커밋 = 하나의 논리적 변경)
    86	3. main 브랜치는 항상 배포 가능한 상태를 유지한다
    87	4. 설계 문서와 구현은 별도 브랜치로 분리 가능하다
    88	
    89	## 제10조: 문서 일관성 원칙
    90	
    91	1. 모든 문서는 동일한 구조와 형식을 따른다
    92	2. 문서 수정 시 의존 관계에 있는 문서를 연쇄 확인한다
    93	3. 문서 인덱스(`docs/INDEX.md`)를 항상 최신 상태로 유지한다
    94	4. 사용하지 않는 문서는 `docs/history/`로 이동한다
    95	
    96	## 제11조: 지속적 개선 원칙
    97	
    98	1. 하네스 설정은 실제 개발 경험에 기반하여 지속적으로 개선한다
    99	2. 에이전트 합의 결과의 품질을 추적하고, 프롬프트를 개선한다
   100	3. 피드백 루프의 각 계층이 실제로 가치를 제공하는지 정기 검토한다
   101	
   102	---
   103	
   104	**이 헌법은 프로젝트의 모든 활동에 우선한다.**
   105	**헌법 수정은 반드시 3+1 에이전트 합의를 거쳐야 한다.**

exec
/bin/bash -lc "nl -ba docs/architecture/implementation-runtime-roadmap-mvp1.md | sed -n '70,140p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
    70	| 본 문서 §1.1 (통합) | **MVP-1 = G2 GP-3 (Credential / Secret Hygiene) + GP-5 (Provider Adapter Enforcement) 실 구현 + R-7 SOP / G1b 회귀 유지** |
    71	
    72	**MVP-1 본질** (3 합의 출처 통합):
    73	- (i) **GP-3 + GP-5** 두 GP 의 *Implementation Evidence PASS* 를 1차로 확보
    74	- (ii) **G1b** (R-7 redaction SOP) 회귀 유지 (이미 PASS 상태, MVP-1 *기준선*)
    75	- (iii) **GP-2 redaction** (외부 LLM 답습) = MVP-1 vs MVP-2 사이의 *경계* — 본 문서는 GP-2 = MVP-2 로 분리 답습 (C-7 line 379 답습 — "MVP-2 \| G2 GP-2 + G4 §4.4 Layer 4")
    76	  - 두 출처 간 미세 충돌: 외부 LLM line 242 = GP-2 포함 / C-7 line 378 = GP-3 + GP-5 한정. 본 문서는 **C-7 답습** (GP-2 = MVP-2 로 분리), 사유 §1.3 답습.
    77	
    78	### 1.2 3-layer PASS 분리 (외부 LLM 답습 §7.1)
    79	
    80	```
    81	┌─────────────────────────────────────────────────────────────────┐
    82	│  Layer 1: Design/Governance Gate PASS                          │
    83	│  → 문서 정의 + 권위 위계 + GP/Skill/Schema *설계* 승인         │
    84	│  → 4 게이트 모두 = ✅ 2026-05-07 + 2026-05-09 후속 (Bundled)    │
    85	│  → 본 문서 = 본 PASS 답습 한정 (변경 0건)                       │
    86	├─────────────────────────────────────────────────────────────────┤
    87	│  Layer 2: Implementation Evidence PASS  ← MVP-1 = 본 layer 1차  │
    88	│  → 각 GP 별 실 구현 + PoC evidence + 자동 회귀 + 합의 APPROVE  │
    89	│  → MVP-1 = GP-3 + GP-5 의 본 PASS 진입                          │
    90	│  → MVP-2 ~ MVP-5 = GP-2 / GP-4 / GP-6 / G3 / G4 의 본 PASS 단계 │
    91	├─────────────────────────────────────────────────────────────────┤
    92	│  Layer 3: Operational Readiness PASS                           │
    93	│  → 4 게이트 모두 Implementation Evidence PASS + 외부 LLM 1+    │
    94	│  → 인간 전문 리뷰 + 사용자 명시 + Multi-host external service  │
    95	│  → 본 문서 범위 외 (MVP-6 = PMO 격상 검토, 별도 합의)          │
    96	└─────────────────────────────────────────────────────────────────┘
    97	```
    98	
    99	**본 문서 = Layer 2 (Implementation Evidence PASS) 의 *MVP-1 단계* deepening 한정.** Layer 3 (Operational Readiness PASS) / Hermes PMO 격상 / 4 게이트 일괄 PASS = 본 문서 범위 외.
   100	
   101	### 1.3 GP-2 = MVP-1 vs MVP-2 분리 사유 (C-7 답습)
   102	
   103	본 문서는 GP-2 (Egress Redaction) 를 **MVP-2** 로 분리. 사유:
   104	
   105	1. **R-4 / R-4.1 답습 책임 분담** — GP-2 의 송신 redaction = R-4.1 Tier-1 42 catalog 의 *런타임 적용* 영역. 본 PoC (Group D) 는 *형식적 검출 layer 한정* (D-2 = redacted output 잔존 검증). 실 송신 redaction = Hermes upstream 영역 (Group D PoC §1.2 #6 답습) + P1 facade RedactionFilter 본문 (Group D PoC §1.2 마지막 항목 답습).
   106	2. **MVP-1 부담 경감** — GP-3 + GP-5 만으로도 의사결정 부담 충분. GP-2 추가 시 4 영역 동시 진입 (GP-3 source + GP-3 storage + GP-5 + GP-2) — 1인 개발자 환경에서 운영 부담 ↑.
   107	3. **외부 LLM line 242 vs C-7 line 378 충돌 해소 = C-7 답습** — 본 문서 §1.1 답습. 단, GP-2 는 **MVP-2** 의 Implementation Evidence PASS 영역 *우선순위 1* (C-7 line 379 답습) — 본 분리는 *시점* 분리이지 *영구 제외* 아님.
   108	
   109	---
   110	
   111	## 2. MVP-1 Entry / Exit 기준
   112	
   113	### 2.1 MVP-1 Entry 기준
   114	
   115	본 문서의 MVP-1 진입은 다음 5 조건이 모두 충족되어야 적격:
   116	
   117	| # | 조건 | 현 상태 (2026-05-12) | 검증 |
   118	|---|------|---------------------|------|
   119	| 1 | Layer 1 (Design/Governance Gate) PASS 발효 | ✅ G2/G3/G4 = PASS Bundled (2026-05-09) | `docs/review/3plus1-consensus-2026-05-07-g2-g3-g4-gate-adoption.md` |
   120	| 2 | GP-3 PoC 완료 (형식적 검출 layer 시제) | ✅ Group D 통합 PoC PASS 6/6 (2026-05-10) | `docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md` |
   121	| 3 | GP-5 PoC 완료 (Layer 1a/1b/1c 시제) | ✅ Group A 1차/2차/3차 PASS (2026-05-09 ~ 2026-05-10) | `docs/phase0/g2-gp5-provider-adapter-enforcement-poc.md` + `g2-gp5-poc2-import-linter-implementation.md` + `g2-gp5-poc3-url-endpoint-model-name-scanner.md` |
   122	| 4 | R-4.1 Tier-1 42 catalog 등록 PASS | ✅ R-4.1 PoC PASS (2026-05-07) | `docs/phase0/r4-1-trigger-extension-evidence.md` |
   123	| 5 | 본 문서 (MVP-1 roadmap) Reviewer-only 단축 합의 APPROVE | ⏳ 본 문서 작성 후 후속 합의 | `docs/review/3plus1-consensus-2026-05-12-implementation-runtime-roadmap-mvp1.md` (작성 예정) |
   124	
   125	**현 시점 충족 = 4/5** (#5 만 본 문서 후속 작성 후 발효).
   126	
   127	### 2.2 MVP-1 Exit 기준 (= Implementation Evidence PASS 진입 조건)
   128	
   129	MVP-1 exit = GP-3 + GP-5 두 GP 의 **Implementation Evidence PASS** 발효. 본 문서 범위에서는 *진입 조건 권고* 한정 (실 PASS 발효 = 별도 합의 영역).
   130	
   131	각 GP 별 Implementation Evidence PASS 진입 5 조건 = ADR-011 §2.1 (a)~(e) 답습 (§5 답습):
   132	
   133	| # | 조건 | GP-3 | GP-5 |
   134	|---|------|------|------|
   135	| (a) | 동등 이상의 보안 결과 | gitleaks/detect-secrets/custom scanner 결과 R-4.1 Tier-1 42 catalog 답습 동등 이상 | depcruise/import-linter 결과 §9.3 답습 동등 이상 |
   136	| (b) | 격리 환경 PoC 실증 | docker secret + chmod 600 + inotify (저장) PoC + gitleaks PR auto-reject (코드) PoC | depcruise/import-linter PR auto-reject + facade single entry point PoC |
   137	| (c) | ADR / SDD 권위 명시 | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 + R-4 + 본 §3 (36번째 entry R-S1 정정 답습) | ADR-008 차단조건 #4 + 부록 B + ADR-009 C-N §5 + ADR-011 + P1 v2 + 본 §4 (36번째 entry R-S1 정정 답습) |
   138	| (d) | 자동 회귀 검증 경로 확보 | `.github/workflows/secret-scan.yml` (또는 R-6 통합) + nightly | `.github/workflows/provider-adapter-enforcement.yml` 기존 + depcruise/import-linter step 추가 + 매 PR + nightly |
   139	| (e) | 합의 APPROVE | 단축 또는 풀 3+1 (수단 결정 시 풀 3+1 권고 — §3.6 답습) | 단축 또는 풀 3+1 (T-1 vs T-2 vs T-9 결정 시 풀 3+1 권고 — §4.6 답습) |
   140	

exec
/bin/bash -lc "nl -ba docs/phase0/mvp1-1.5th-reinforcement-entry-brief.md | sed -n '1,140p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# MVP-1 1.5차 보강 진입 합의 entry brief — 4 sub-수단 (S-3 + ST-2 + PC-1 + AR-3)
     2	
     3	> **scope**: MVP-1 GP-3 + GP-5 1.5차 보강 4 sub-수단 (S-3 detect-secrets 부분 통합 + ST-2 inotify sidecar + PC-1 pre-commit framework 의무화 + AR-3 통합 PR auto-reject) **진입 합의 entry brief**. 본 brief 발효 = 4 sub-수단 *채택 결정 발효 자격* + 실 구현 단계 진입 권한 발효 자격. **본 brief 자체에서 실 코드 / CI / hook / branch protection rule / `.pre-commit-config.yaml` 본문 변경 0건 의무**.
     4	>
     5	> **답습**:
     6	> - 진입 합의 carry-over 명시 = `docs/sessions/SESSION_2026-05-27.md` 23번째 entry carry-over (b) (commit `c2bcb19` 답습, scope = 4 sub-수단 모두 + 풀 3+1 + 외부 LLM 1+)
     7	> - 선행 1.5차 brief = [[backlog1-gp3-1.5-deepening-brief]] + [[backlog2-gp5-1.5-remaining-items-brief]] (영역 분류 한정, 수단 결정 0건)
     8	> - 선행 1.5차 합의 = `docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md` (APPROVE AS BRIEF, ST-2 단독 우선 권고) + `docs/review/3plus1-consensus-2026-05-13-backlog2-gp5-1.5-remaining-items.md` (APPROVE Deferred 유지 + AR-3 Backlog #3 이관)
     9	> - roadmap-mvp1 권위 = [[implementation-runtime-roadmap-mvp1]] APPROVED (`c2bcb19` line 826/827 답습) §3.2 / §3.3 / §3.6.3 / §4.3 / §4.4 / §4.7.3
    10	> - 최상위 모법 = [[ADR-011-means-vs-ends-redaction]] §2.1 (a)~(e) 5조건 + §2.4 T1/T2/T3 분리
    11	> - 메타 = [[ceremony-inflation]] 차단 + [[meta-cycle-warning]] (정정의 정정 자격 0 self-check 통과)
    12	>
    13	> **DONE 기준** (본 brief 의 *최종 산출 자격*):
    14	> 1. 4 sub-수단 각각의 *진입 자격* 분석 + ADR-011 §2.1 (a)~(d) + 합의 APPROVE 운영조건 (e) 5/5 충족 매트릭스 (ADR-011 §3 후속 권위 답습 — R-1 BLOCKING 흡수)
    15	> 2. 선행 1.5차 brief 합의 권위 vs 본 cycle 결정 *선차 변경 매트릭스* (3 sub-수단 권위 상승 명문)
    16	> 3. 본 cycle 합의 형태 = 풀 3+1 + 외부 LLM 1+ 답습 정당화 (4 sub-수단별)
    17	> 4. Rollback Trigger 본문 / Evidence 형식 / JSONL Ledger event enum 후보 (발효 시점 의무)
    18	> 5. 외부 LLM 응답 요구 *입력 자료* 정의 (사용자 준비 영역)
    19	> 6. 7 풀 3+1 승격 트리거 발화 검증 (본 cycle 자체 ↔ 4 sub-수단별)
    20	> 7. 다음 단계 결정 옵션 (사용자 결정 영역)
    21	
    22	---
    23	
    24	## 0. 본 brief 의 범위
    25	
    26	### 0.1 사용자 진입 명령 답습 (carry-over from SESSION_2026-05-27 23번째 entry, commit `c2bcb19`)
    27	
    28	> **(b) MVP-1 1.5차 보강 합의 — 사용자 명시 scope 확정 (2026-05-27)**:
    29	> - scope = **4 sub-수단 모두 (S-3 + ST-2 + PC-1 + AR-3)** (사용자 명시 결정 답습)
    30	>   - S-3 detect-secrets 부분 통합 (GP-3 Tier-2/3 catalog 확장)
    31	>   - ST-2 inotify sidecar (GP-3 저장 경로 실시간 감지)
    32	>   - PC-1 pre-commit framework 의무화 (GP-3/GP-5 T3 dev 환경 강제)
    33	>   - AR-3 통합 PR auto-reject (GP-3/GP-5 branch protection rule 변경)
    34	> - 합의 형태: **풀 3+1 + 외부 LLM 1+** (roadmap-mvp1 §3.6.3 line 289 + §4.7.3 line 480 답습)
    35	> - 사용자 준비 영역: **외부 LLM 응답 1+** (Claude 가 외부 LLM 호출 못 함, 사용자 직접 호출 의무)
    36	> - 다음 세션 진입 명령 (사용자 영역): "(b) 1.5차 보강 풀 3+1 진입 — S-3 + ST-2 + PC-1 + AR-3" + 외부 LLM 자료 첨부
    37	
    38	### 0.2 본 brief 가 *하는* 것
    39	
    40	1. 4 sub-수단 (S-3 + ST-2 + PC-1 + AR-3) *진입 자격* 분석 — ADR-011 §2.1 (a)~(d) + 합의 APPROVE 운영조건 (e) 5조건 매트릭스 (§3, ADR-011 §3 후속 권위 답습)
    41	2. 선행 1.5차 brief 합의 권위 (2026-05-13 backlog1 / backlog2) 와의 *선차 변경 매트릭스* (§1.3)
    42	3. 4 sub-수단 각각의 *수단 후보 비교* + threshold 후보 + Rollback Trigger 본문 후보 (§2 + §5)
    43	4. 본 cycle 합의 형태 = 풀 3+1 + 외부 LLM 1+ *정당화* (carry-over 답습 + roadmap-mvp1 §3.6.3/§4.7.3 답습) (§4.1)
    44	5. 4 sub-수단 *발효 시점* 합의 형태 권고 (선행 권위 답습) (§4.2)
    45	6. 7 풀 3+1 승격 트리거 *발화 검증* (본 cycle 자체 ↔ 4 sub-수단별) (§4.3)
    46	7. 외부 LLM 응답 요구 *입력 자료* 정의 + *응답 자격 검증 기준* (사용자 준비 영역) (§7)
    47	8. 본 cycle 합의 발효 후 *실 구현 sub-cycle 진입 권한* 발효 자격 명문 (§8)
    48	
    49	### 0.3 본 brief 가 *하지 않는* 것 (사용자 명시 답습 + 본 brief 영역 한계)
    50	
    51	| # | 영역 | 위반 시점 |
    52	|---|------|----------|
    53	| 1 | 실 코드 / runtime code 구현 | 0건 (S-3 plugin / ST-2 sidecar / PC-1 framework / AR-3 branch protection 본문 모두 0건) |
    54	| 2 | `.pre-commit-config.yaml` 본문 변경 / 신규 hook 추가 | 0건 |
    55	| 3 | `.importlinter` config 변경 | 0건 |
    56	| 4 | `.github/workflows/*.yml` 본문 변경 | 0건 |
    57	| 5 | `branch protection rule` 변경 / GitHub API 호출 | 0건 |
    58	| 6 | `pre-commit install` 실행 | 0건 |
    59	| 7 | detect-secrets / inotify-tools 설치 | 0건 |
    60	| 8 | Tier-2 / Tier-3 catalog 본문 확장 | 0건 (S-3 plugin 명시 활성화 후보 영역 명시 한정, 본문 확장 0건) |
    61	| 9 | threshold *고정* (FP/FN/latency 등) | 0건 (후보 한정 유지) |
    62	| 10 | **MVP-1 PASS *재선언*** | 0건 (Layer D `210c98f` 판정 그대로 유지) |
    63	| 11 | **Implementation Evidence PASS 발효** | 0건 ((c) 진입점 별도 단계 답습) |
    64	| 12 | **Operational Readiness PASS (Layer E)** | 0건 |
    65	| 13 | **Hermes PMO 격상 (Layer F)** | 0건 |
    66	| 14 | 외부 LLM 호출 (Claude 영역) | 0건 (사용자 명시 외부 LLM 응답 1+ 별도 첨부 영역) |
    67	| 15 | ADR 본문 갱신 (ADR-008 / ADR-010 / ADR-011 / ADR-012) | 0건 (cross-reference 한정도 0건 — 본 brief 발효 후 별도 commit 영역) |
    68	| 16 | 헌법 본문 갱신 (`PROJECT_CONSTITUTION.md`) | 0건 |
    69	| 17 | roadmap-mvp1 §1~§8 본문 변경 | 0건 (cross-reference 답습 한정) |
    70	| 18 | `src/adapters/llm/facade.py` placeholder → real 본문 (G5-4) | 0건 (TR-1 자동 풀 3+1 별도 trajectory) |
    71	| 19 | Backlog #3 / #4 / #7 *자동* 진입 | 0건 (AR-3 의 Backlog #3 이관 → 본 cycle 동시 진입 결정 = 사용자 명시 권위 변경 — Backlog #3 *전체* 진입 ≠ 본 cycle) |
    72	| 20 | 본 brief *자체* 영구화 / 권위 chain 등재 | 0건 (본 brief = 본 cycle 합의 input 한정) |
    73	
    74	### 0.4 본 brief 의 권위 한계
    75	
    76	- ✅ 본 brief 발효 자격 = **풀 3+1 합의 + 외부 LLM 1+ 응답 입력 + 사용자 명시 결정** 3 조건 모두 충족 시점
    77	- ✅ 본 brief 발효 결과 = 4 sub-수단 *채택 결정 발효* + 실 구현 sub-cycle 진입 권한 발효 + Rollback Trigger 본문 채택 + Evidence 형식 본문 채택
    78	- ❌ 본 brief 자체에서 4 sub-수단 *결정* 0건 (본 brief = entry input, 결정 자격은 풀 3+1 합의 결과에 의존)
    79	- ❌ 본 brief 자체에서 threshold *고정* 0건 (후보 한정)
    80	- ❌ 본 brief 자체에서 실 구현 0건 (별도 sub-cycle)
    81	- ⚠️ 본 brief 합의 후 *자동 실 구현 진입 금지* — 사용자 명시 결정 의무 (단계별 합의 cycle 패턴 답습)
    82	
    83	---
    84	
    85	## 1. 진입 컨텍스트 답습
    86	
    87	### 1.1 선행 1.5차 brief 합의 권위 답습 (2026-05-13 backlog1 + backlog2)
    88	
    89	| 합의 | 일자 | 판정 | 본 cycle 답습 영역 |
    90	|------|------|------|------------------|
    91	| `3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md` | 2026-05-13 | ✅ **APPROVE AS BRIEF** (Reviewer-only 단축) | Backlog #1 진입 *직전* 정비 한정. ST-1/ST-2/PC-4 *채택 결정 0건*. ST-2 단독 우선 권고 (T3 자동 진입 0건 조건 충족 유일). PC-4 = T2 + T3 sub 영역 분리. |
    92	| `3plus1-consensus-2026-05-13-backlog2-gp5-1.5-remaining-items.md` | 2026-05-13 | ✅ **APPROVE Keep Deferred** (Reviewer-only 단축) | T-1/T-3/T-4/T-5/AR-3 5 항목 *Deferred 유지 권위화 한정*. **AR-3 = Deferred 유지 + Backlog #3 이관 명시**. PC-4 T2 sub = 별도 합의 (`78483c5`) Partially Satisfied 완료. |
    93	| `3plus1-consensus-2026-05-13-pc4-t2-c5c-c6-satisfaction.md` (참조) | 2026-05-13 | ✅ APPROVE (`78483c5`) | PC-4 T2 sub (`.pre-commit-config.yaml` opt-in framework) §C-5c + §C-6 Partially Satisfied 갱신. **PC-1 T2 정책 영역은 이미 부분 발효**, T3 dev 환경 강제 = Backlog #3 영역. |
    94	
    95	### 1.2 4 sub-수단 답습 (roadmap-mvp1 §3.2 + §3.3 + §4.3 + §4.4)
    96	
    97	| sub-수단 | GP | 영역 정의 | roadmap-mvp1 본문 line |
    98	|---------|----|---------|----------------------|
    99	| **S-3** | GP-3 | **detect-secrets** plugin-based (~20+ plugins, 활성화 선택). 코드 본문 secret 검출 (G3-2). Tier-2/3 catalog 확장 영역. | §3.2.1 line 180 + §3.2.2 line 189 ("plugin 명시 활성화 + baseline file 금지 2 조건 강제 시에만 채택 적격") |
   100	| **ST-2** | GP-3 | **inotify sidecar** (mtime/perm 변경 → 컨테이너 정지). 런타임 지속 검증. 저장 경로 secret 검출 (G3-1). | §3.3.1 line 204 + §3.3.2 line 214 ("MVP-1 1.5차 (보강) = ST-3 + **ST-2 inotify sidecar**, Hermes upstream 변경 회피 유지") |
   101	| **PC-1** | GP-3 + GP-5 | **pre-commit framework** (`.pre-commit-config.yaml` + `pre-commit install`). hook 정의 통일 + dev 환경 자동 설치. | §4.3.1 line 370 ("T2 정책 영역, ADR-011 §2.4 답습") + §4.3.2 line 380 ("MVP-1 1.5차 보강 = PC-4 = PC-1 + PC-3 병행, dev 환경 강제 추가 시 Defense in depth") |
   102	| **AR-3** | GP-3 + GP-5 | **AR-1 (CI step fail-closed) + AR-2 (branch protection rule 강제) 통합** PR auto-reject runtime. | §4.4.1 line 393 + §4.4.2 line 400 ("MVP-1 1.5차 보강 = AR-3 (AR-1 + AR-2 통합) — T3 영역 진입 + branch protection rule 변경 + 사용자 명시 결정") |
   103	
   104	### 1.3 ⭐ 선차 변경 매트릭스 (선행 권위 vs 본 cycle 결정)
   105	
   106	> **본 §1.3 = 본 brief 의 *핵심 framing*** — 선행 1.5차 brief 합의 (2026-05-13) 의 권위와 본 cycle (2026-05-27) carry-over 사용자 명시 결정 사이의 *변경 차이* 를 명시. 변경 자격 정당성 = (a) 사용자 명시 권위 우선 + (b) 본 cycle 합의 형태 = 풀 3+1 + 외부 LLM 1+ + 사용자 명시 = ADR-011 §2.1 (e) + §2.4 T3 영역 답습 충실성.
   107	
   108	| sub-수단 | 선행 권위 (2026-05-13) | roadmap-mvp1 line | 본 cycle 결정 | 권위 정당성 |
   109	|---------|---------------------|------------------|--------------|------------|
   110	| **S-3** | backlog1 §1.3 미언급 (Backlog #1 = ST-1/ST-2/PC-4 한정, S-3 = Group D PoC §2.1 (D) 답습 영역) | §3.6.3 **line 289** — "MVP-1 1.5차 (S-3 detect-secrets 부분 통합) \| **풀 3+1 합의 + 외부 LLM 1+** \| Tier-2/3 catalog 확장 영역 + 사용자 명시 풀 3+1 trigger #4 발화 (Group D §2.1 (D) 답습)" | **풀 3+1 + 외부 LLM 1+** | **✅ 일치 답습** (roadmap §3.6.3 line 289 verbatim 답습) |
   111	| **ST-2** | backlog1 §1.5 + §2.2.4 — "ST-2 단독 우선 권고 (T3 자동 진입 0건 유일)" + "T2 영역, **단축 합의 + 사용자 명시 결정** *또는* **보수적 풀 3+1 합의**" | §3.6.3 **line 290** — "ST-1 / **ST-2** / ST-5 진입 (Hermes upstream 변경) \| 풀 3+1 합의 + Hermes upstream PR 검토 \| Hermes upstream 영역" | **풀 3+1 + 외부 LLM 1+** | **⚠️ 사용자 명시 상승 + framing 미세 충돌 흡수**. backlog1 권고 = T2 + 보수적 풀 3+1 옵션 → 본 cycle = 풀 3+1 + 외부 LLM 1+. roadmap §3.6.3 line 290 framing 미세 충돌 (ST-2 = "Hermes upstream 변경 ❌ 불필요", backlog1 §2.2.2 verbatim) — 단, 사용자 명시 carry-over = "GP-3 저장 경로 실시간 감지" 영역 = sidecar 운영 = 풀 3+1 + 외부 LLM 1+ 권한 영역. 본 cycle 합의 발효 시 backlog1 §2.2.4 권고 *상위 변경* 자격 발효. |
   112	| **PC-1** | roadmap §4.7.3 **line 479** — "MVP-1 1.5차 (PC-1 pre-commit framework 도입) \| **단축 합의 + 사용자 명시** \| T2 정책 영역 (ADR-011 §2.4 답습)" + PC-4 T2 sub `78483c5` Partially Satisfied (`.pre-commit-config.yaml` opt-in framework 발효) | §4.7.3 line 479 | **풀 3+1 + 외부 LLM 1+** | **⚠️ 권위 상승 — 사용자 명시 carry-over 답습**. carry-over verbatim = "PC-1 pre-commit framework **의무화** (GP-3/GP-5 T3 dev 환경 강제)". opt-in (T2, line 479) → 의무화 (T3 dev 환경 강제) 영역 상승 = ADR-011 §2.4 T3 영역 진입 = 풀 3+1 + 외부 LLM 1+ + 사용자 명시 의무 (roadmap §4.7.3 line 480 AR-3 = T3 영역 답습 패턴). |
   113	| **AR-3** | backlog2 §1.6 — "**AR-3 = Deferred 유지 + Backlog #3 이관 명시**" (T3 영역 진입 BLOCKING + Backlog #3 보존 의무) | §4.7.3 **line 480** — "AR-2 / AR-3 진입 (branch protection rule 변경) \| **풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시** \| T3 영역" | **풀 3+1 + 외부 LLM 1+ + MVP-1 1.5차 동시 진입** | **⚠️ 선차 변경 — 사용자 명시 권위 변경**. backlog2 합의 = Deferred 유지 + Backlog #3 이관 → 본 cycle = MVP-1 1.5차 동시 진입. 합의 *형태* 자체는 roadmap §4.7.3 line 480 와 일치 답습. *시점* 변경 = backlog2 §1.6 권위의 사용자 명시 변경 자격 (ADR-011 §2.1 (e) 합의 APPROVE + §2.4 T3 영역 답습 + 사용자 명시 결정 = 정당). |
   114	
   115	→ **요약**: 본 cycle 합의 형태 = 4 sub-수단 모두 **풀 3+1 + 외부 LLM 1+ + 사용자 명시** 일관. S-3 = 일치 답습 / ST-2 = 권위 상승 / PC-1 = 권위 상승 / AR-3 = 시점 선차 변경 (Backlog #3 이관 → MVP-1 1.5차 동시 진입). 모든 변경 자격 = 사용자 명시 + ADR-011 §2.1 (a)~(d) + 합의 APPROVE 운영조건 (e) 5/5 충족 + §2.4 T3 영역 답습 + 본 cycle 합의 APPROVE 시 발효.
   116	
   117	---
   118	
   119	## 2. 4 sub-수단 진입 자격 분석
   120	
   121	### 2.1 S-3 — detect-secrets 부분 통합 (GP-3 Tier-2/3 catalog 확장)
   122	
   123	#### 2.1.1 영역 정의
   124	
   125	| 항목 | 내용 |
   126	|------|------|
   127	| **목적** | 코드 본문 secret 검출 (G3-2) Tier-2/3 catalog 확장 — plugin-based ~20+ plugins (Tier-1 42 catalog 답습 외 확장 영역) |
   128	| **검증 시점** | CI step (매 PR + nightly) + opt-in pre-commit hook |
   129	| **메커니즘** | `detect-secrets scan --baseline <baseline>.json --exclude-files <regex>` — plugin 활성화 선택 (Slack / GCP / Azure / Generic / Base64 / Hex 등) |
   130	| **권위 출처** | roadmap-mvp1 §3.2 6 수단 후보 매트릭스 / Group D PoC §2.1 (D) sub-수단 #5 ("detect-secrets baseline silenceable risk 명시") |
   131	
   132	#### 2.1.2 채택 조건 (roadmap §3.2.2 line 189 답습)
   133	
   134	✅ **plugin 명시 활성화 한정** — Tier-1 답습 plugin 활성화 (실 plugin identifier 예: `AWSKeyDetector` / `KeywordDetector` / `Base64HighEntropyString` / `HexHighEntropyString` / `PrivateKeyDetector` — 실 구현 sub-cycle 정확 mapping 영역, R-4 BLOCKING 흡수). Slack / GCP / Azure 등 추가 활성화 = **별도 합의** (Tier-2/3 catalog 확장 = 풀 3+1 + 외부 LLM 1+ 의무, R-MVP1-G3-1 답습)
   135	✅ **baseline file 금지** — `--baseline` 옵션 0건 (silenceable 위험 차단, Group D §2.1 (D) 답습)
   136	✅ **secret_scanner.py (S-1) 답습 유지** — S-3 = *추가* layer (S-1 미대체, Defense in depth)
   137	✅ **`.github/workflows/secret-hygiene-egress-redaction.yml` step 통합** — 현 secret_scanner.py 답습 *후속* step
   138	
   139	#### 2.1.3 본 cycle 합의 발효 시 채택 결정 영역
   140	

codex
R-S1의 핵심 대조점이 확인됐습니다. ADR-012 §2.3의 Layer 4는 External anchor이고, G4 §4.4.1의 Layer 4는 CI 회귀 검증입니다. 같은 “Layer 4” 라벨이 서로 다른 의미로 쓰여 있어, brief가 이를 “미세 충돌”로만 처리해도 되는지 별도 blocking으로 판단하겠습니다.
exec
/bin/bash -lc 'rg -n "R1-2|권위 chain|다중 source|source 손상|R-S1" docs/decisions docs/review docs/phase0 docs/architecture | head -80' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
docs/architecture/hermes-adoption-design.md:63:- R1-2 §2.6.3 OAuth 권한 검증 (entrypoint stat + inotify)
docs/architecture/hermes-adoption-design.md:423:#### 2.6.4 OAuth Credentials 처리 강화 (R1-2)
docs/architecture/hermes-adoption-design.md:430:| **inotify 런타임 감시 (R1-2)** | mtime/perm 변경 시 즉시 컨테이너 정지 |
docs/architecture/hermes-adoption-design.md:431:| 만료 임박 알림 (R1-2) | 토큰 만료 7일 전 알림 |
docs/architecture/hermes-adoption-design.md:923:| **B-N7** | OAuth perm 변경 미탐지 | HIGH | §2.6.4 R1-2 entrypoint stat + inotify |
docs/architecture/hermes-adoption-design.md:960:- [x] OAuth credentials 권한 검증 시작+런타임 (§2.6.4 R1-2 inotify)
docs/architecture/governance-preconditions.md:106:| **P3** | **Credential / OAuth 파일 권한 노출** | API 키 파일 / OAuth credentials 파일이 world-readable / docker socket mount / inotify 미감시 | 8조 #2 | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 + entrypoint stat 검증 (35번째 entry R-S1 정정 답습) |
docs/architecture/governance-preconditions.md:343:| **GP-3** | Credential / Secret Hygiene (저장 + 코드) | P3, P4 | (저장) docker secret + chmod 600 + entrypoint stat + inotify, (코드) gitleaks / detect-secrets pre-commit hook + CI step | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 + 헌법 8조 #1 (35번째 entry R-S1 정정 답습) |
docs/architecture/governance-preconditions.md:356:| GP-3 | ✅ gitleaks / detect-secrets / chmod check / entrypoint stat | ❌ 추론 불필요 | ✅ inotify 감시 즉시 컨테이너 정지 (R1-2) |
docs/architecture/governance-preconditions.md:488:| 계산적 | docker secret 정의 | `docker-compose.yml` (ADR-008 차단조건 #6 답습, 35번째 entry R-S1 정정 답습) |
docs/architecture/governance-preconditions.md:489:| 계산적 | chmod 600 강제 + entrypoint stat 검증 (R1-2) | Hermes Dockerfile entrypoint |
docs/architecture/governance-preconditions.md:493:| 자동 롤백 | inotify 감시 hit → 컨테이너 정지 (R1-2) | Hermes runtime |
docs/architecture/governance-preconditions.md:498:- ✅ ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 (OAuth credentials 처리 강화) 명시 (충족됨, 35번째 entry R-S1 정정 답습)
docs/architecture/governance-preconditions.md:508:| (c) | ADR / SDD 권위 명시 | ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + 헌법 8조 #1 + 본 §5 (35번째 entry R-S1 정정 답습) |
docs/architecture/governance-preconditions.md:523:- ADR-008 cross-reference (차단조건 #1 + #6 + 부록 B): 본문 변경 없음, GP-3 cross-reference 추가 (35번째 entry R-S1 정정 답습)
docs/architecture/hermes-adoption-design-v3.md:390:| 4 | OAuth 직결 사용 차단 (Phase 1) | A-meta 위험 (구독 강제 해지) | API 키 경로 강제 + entrypoint stat + inotify 감시 | ADR-008 차단조건 #4 + R1-2 |
docs/architecture/jarvis-mvp1-boss-abstraction-design.md:5:**선행**: (4-way) brief v1.1 (`35e0e8c`, 588줄) + 풀 3+1 합의 (`5dcbbdb`, 267줄, APPROVE w/ COND BLOCKING 15 + R-S1~R-S4) + 기존 `src/jarvis/boss.py` 99줄 (commit `83aebad`, 2026-05-22, "feat(jarvis): MVP-1 트랙 A — Boss LLM advisory 판단 지점 (TDD)")
docs/architecture/jarvis-mvp1-boss-abstraction-design.md:6:**scope**: 기존 `src/jarvis/boss.py` 99줄 design doc *추출* + Backend 후보 매트릭스 *신규* — **신규 코드 0건, 기존 변경 0건** (R-S1 발효 BLOCKING-1 답습 영구)
docs/architecture/jarvis-mvp1-boss-abstraction-design.md:10:## 1. 본 design doc 의 자격 (R-9 + R-15 + R-S1 답습)
docs/architecture/jarvis-mvp1-boss-abstraction-design.md:398:- ⭐⭐⭐ **본 design doc = 기존 `src/jarvis/boss.py` 99줄 (commit `83aebad`) design doc *추출* + Backend 후보 매트릭스 *신규* only** (신규 코드 0건, 기존 변경 0건, R-S1 발효 답습 영구)
docs/architecture/jarvis-mvp1-boss-abstraction-design.md:417:| R-S1 발효 (boss.py:24~98 verbatim 인용) | ✓ §2.1~§2.5 verbatim 인용 완료 |
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification.md:3:> **합의 cycle (f-K)**: Provider Liquidity deep-dive 합의 (`a9e1e88`, BLOCKING 13) 의 **R-26 (C-R2) + R-11** 답습 후속 cycle. brief v1 (`f305174`, 556줄) → 풀 3+1 합의 (Agent A/B/C 병렬 독립 → Reviewer 통합) 산출. **APPROVE w/ COND**, BLOCKING 16 + 권고 21 + NOTE 24, **기각 0**, **Reviewer 단독 격상 BLOCKING 3** (R-S1 / R-S2 / R-S3). 본 합의는 brief v1 의 진술을 BLOCKING 으로 정정하는 *권한* 을 가지나, **(1) ADR-011 §6 본문 정정 자격 0 + (2) Provider Liquidity 본질 약화 자격 0 + (3) MVP-1 합의 본문 정정 자격 0 + (4) 헌법 본문 정정 자격 0 + (5) 메모리 본문 정정 자격 0 + (6) 4 가족 분류 자체의 영구 framing 정착 자격 0 (R-12 답습) + (7) 자동 다음 단계 진입 자격 0 (R-29 + R-30 답습)** 의 **7 권한 한계 영구 답습**.
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification.md:35:| evidence "GGUF 한정" 더 좁은 한정 (시점 부정합 vs 분류 축) | A-B2 + A-S1 ⭐ / C-B1 + C-S1 ⭐ | A 시점 부정합 + C 분류 축 = 본질 부정 *분리* 동형 → R-S1 통합 |
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification.md:75:- **R-S1 (A-S1 격상)** ⭐: Phase 3 raw line 25~32 결론 verbatim 직접 확인 — "Ollama 다운로드 GGUF = 더 오래된 conversion (`.ssm_dt.bias` 미저장) + llama.cpp `c0c7e147` master = `.dt_bias` → `.dt_proj.bias` rename + `.bias` flag=0 required 강제". 본 evidence 의 본질 = **시점 부정합** (Ollama blob 동기화 미수행 + llama.cpp conversion lineage backward-incompatible 변경) ≠ "GGUF 가족 본질 부정". A-S1 = Reviewer 단독 직접 raw 확인으로 격상 BLOCKING.
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification.md:163:P3-F1 evidence 의 일반화 자격 = "GGUF 가족 한정" + "sub-차원 (1) tensor naming 한정" + **"1 conversion script lineage × 1 시점" 한정** 3 layer 답습 의무. **R-S1 통합 답습**.
docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification.md:397:**End of consensus report** — 작성 2026-05-24, 3 Agent 병렬 독립 PASS + Reviewer 단독 격상 3건 (R-S1·R-S2·R-S3) + 정합성 매트릭스 + BLOCKING 16 + 권고 21 + NOTE 24 + 기각 0
docs/architecture/mvp-1-to-6-entry-conditions-brief.md:93:| (c) | ADR / SDD 권위 명시 | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 + R-4 + `roadmap-mvp1.md` §3 (36번째 entry R-S1 정정 답습) | ADR-008 차단조건 #4 + 부록 B + ADR-009 C-N §5 + ADR-011 + P1 v2 + `roadmap-mvp1.md` §4 (36번째 entry R-S1 정정 답습) |
docs/architecture/hermes-not-root-of-trust-runtime.md:25:> **[Cross-reference Block — (g1-N-3-adr-008+sip+adr-012') R-7 (f) cross-ref block 만 채택 + R-S1 (CRITICAL) 답습]**: 본 line 23 (상위 권위) + line 176 (cross-ref 표) + line 1040 (영구 핵심 제약 표) 표기 "헌법 제5조 관용 (Provider Liquidity)" / "헌법 5조 (관용 — Provider Liquidity)" / "헌법 5조 (관용)" = (g1-N-1) commit `148fbbe` 후 **헌법 제5조-2: Provider Liquidity 원칙 (비협상) (line 75~80)** 직접 모법 발효 — (g1-N-1) 이전 관용 표현 답습. 본 cycle = gov §1.1 line 78 verbatim 명문 4 source ("ADR-008 / ADR-011 / system-identity-prequel / 본 v3") *외* **유일 추가 동형 source** 신규 식별 (R-S1 CRITICAL, Reviewer raw cross-check 강화 — bash grep `"헌법 제5조 (Provider Liquidity\|헌법 제5조 관용 (Provider Liquidity"` = ADR-012 + 본 source 단 2 파일 verify). Agent C 단독 발견 + Reviewer raw cross-check 직접 verify (line 176/1040 단독 추가 식별). (g1-N-3-pamsd) `ab96e30` 동형 패턴 답습, **본문 verbatim 변경 0건** ((f) cross-ref block 만 채택). 정정 후 형식 = ADR-011 line 245 모법 "제5조-2 관용 (Provider Liquidity, 비협상)" (R-rec-3 답습 + 사용자 명시 직접 확인). 추가 위치 line 7/897/1073 (P3 본문) = 본질 답습, 정정 자격 약함 ((P3) 약식 통일 cycle DEFER carry-over). 본 cycle 합의 = `209f04d`.
docs/phase0/mvp1-r-s1-framing-correction-brief.md:1:# MVP-1 R-S1 cross-reference 정정 + framing 정정 sub-cycle brief ((b2) + (b3) 병렬)
docs/phase0/mvp1-r-s1-framing-correction-brief.md:3:> **scope**: 24번째 entry brief v1.1 carry-over (b2) R-S1 권위 chain 정정 + (b3) roadmap-mvp1 §3.6.3 line 290 framing 정정 (병렬 sub-cycle). 33번째 entry R-S1 raw verify (Agent B + codex 일치) + Reviewer 통합 R-3 답습 (multi-source 재기술).
docs/phase0/mvp1-r-s1-framing-correction-brief.md:15:| 24번째 entry brief v1.1 carry-over (b2) | `docs/phase0/mvp1-1.5th-reinforcement-entry-brief.md` line 159~163 | "governance-preconditions.md 5 위치 + backlog1 합의 본문 §A.2 R1-2 + §2.6.2 R2-1 인용 정정 + 정확한 R1-2 source 위치 확인 + 일관 정정. ADR-008 본문 변경 0건 의무 답습" |
docs/phase0/mvp1-r-s1-framing-correction-brief.md:17:| 33번째 entry 합의 보고서 R-3 (multi-source 재기술) | `docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md` §2.1 R-3 | "ADR-008 §A.2 R1-2 직접 인용 = source attribution 손상. 권고 정정: ADR-008 차단조건 #1 (SQLCipher) + #4 (어댑터 추상화) + #6 (Docker 격리 + egress 화이트리스트) + 부록 B + ADR-010 + ADR-009 + ADR-011 + roadmap-mvp1 §3 다층 답습으로 재기술" |
docs/phase0/mvp1-r-s1-framing-correction-brief.md:18:| 33번째 entry 합의 보고서 R-MVP1-PASS-2 | brief v1.1 §6 | "R-S1 정정 = cross-reference 정정 한정, ADR-008 본문 변경 영구 금지. 본문 변경 시 풀 3+1 합의 + ADR 권위 영역" |
docs/phase0/mvp1-r-s1-framing-correction-brief.md:19:| 33번째 entry Reviewer R-S1 raw verify | Agent B + codex 일치 | ADR-008 본문 line 136 = §A.2 = "Hermes JSONL Export 검증" + "R1-2" + "§2.6.4" + "§2.6.2" 식별자 ADR-008 본문 0건 |
docs/phase0/mvp1-r-s1-framing-correction-brief.md:31:| **scope** | (b2) R-S1 cross-reference 정정 + (b3) roadmap-mvp1 §3.6.3 line 290 framing 정정 (병렬 단일 sub-cycle, cross-reference 정정 영역 유사 = Agent C C-N-6 답습) |
docs/phase0/mvp1-r-s1-framing-correction-brief.md:41:| 1 | ADR-008 본문 변경 (`§A.2` / `§2.6.4` / `§2.6.2` / "R1-2" / "R2-1" 라벨 본문 추가/변경) | **0건 영구 금지** (R-MVP1-PASS-2 답습, R-MVP1-PASS-10 답습) |
docs/phase0/mvp1-r-s1-framing-correction-brief.md:58:## §2 R-S1 cross-reference 정정 매트릭스 (R-3 multi-source 재기술 답습)
docs/phase0/mvp1-r-s1-framing-correction-brief.md:68:| 부록 B | line 240~ | Hermes PMO 격상 절차 + 12 조건 + cross-reference Amendment | 권위 chain 통합 |
docs/phase0/mvp1-r-s1-framing-correction-brief.md:69:| "R1-2" 식별자 | **본문 0건** | (식별자 부재) | source 손상 |
docs/phase0/mvp1-r-s1-framing-correction-brief.md:70:| "§2.6.4" 식별자 | **본문 0건** | (식별자 부재) | source 손상 |
docs/phase0/mvp1-r-s1-framing-correction-brief.md:71:| "§2.6.2" 식별자 | **본문 0건** | (식별자 부재) | source 손상 |
docs/phase0/mvp1-r-s1-framing-correction-brief.md:75:**정정 전 (source 손상 인용)**:
docs/phase0/mvp1-r-s1-framing-correction-brief.md:76:- `ADR-008 §A.2 R1-2` (저장 경로 secret 보호 권위로 인용)
docs/phase0/mvp1-r-s1-framing-correction-brief.md:77:- `ADR-008 §2.6.4 R1-2` (OAuth credentials 처리 강화로 인용)
docs/phase0/mvp1-r-s1-framing-correction-brief.md:92:| 1 | 106 (P3 row) | `ADR-008 §2.6.4 R1-2 + entrypoint stat 검증` | `ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + ADR-010 + ADR-011 + entrypoint stat 검증` |
docs/phase0/mvp1-r-s1-framing-correction-brief.md:93:| 2 | 343 (GP-3 row) | `ADR-008 §2.6.4 R1-2 + R2-1 + 헌법 8조 #1` | `ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 + 헌법 8조 #1` |
docs/phase0/mvp1-r-s1-framing-correction-brief.md:95:| 4 | 498 | `ADR-008 §2.6.4 R1-2 (OAuth credentials 처리 강화) 명시 (충족됨)` | `ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 (OAuth credentials 처리 강화) 명시 (충족됨)` |
docs/phase0/mvp1-r-s1-framing-correction-brief.md:96:| 5 | 508 ((c) cell) | `ADR-008 §2.6.4 R1-2 + 헌법 8조 #1 + 본 §5` | `ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + 헌법 8조 #1 + 본 §5` |
docs/phase0/mvp1-r-s1-framing-correction-brief.md:97:| 6 | 523 | `ADR-008 §2.6.4 R1-2: 본문 변경 없음, GP-3 cross-reference 추가` | `ADR-008 cross-reference (차단조건 #1 + #6 + 부록 B): 본문 변경 없음, GP-3 cross-reference 추가 (33번째 entry R-S1 정정 답습)` |
docs/phase0/mvp1-r-s1-framing-correction-brief.md:103:| 1 | 12 | `ADR-008 §A.2 R1-2 + §2.6.2 R2-1 (저장 경로 secret 보호 권위)` | `ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 (저장 경로 secret 보호 권위, 35번째 entry R-S1 정정 답습)` |
docs/phase0/mvp1-r-s1-framing-correction-brief.md:105:| 3 | 390 | `ADR-008 §A.2 R1-2 + §2.6.2 R2-1 답습 \| ✅ (cross-reference 답습 한정 — 본문 변경 0건)` | `ADR-008 차단조건 #1 + #6 + 부록 B 답습 \| ✅ (cross-reference 답습 한정 — 본문 변경 0건, 35번째 entry R-S1 정정 답습)` |
docs/phase0/mvp1-r-s1-framing-correction-brief.md:138:| **D-2** | 정정 형태 | (A) multi-source 재기술 (R-3 답습) / (B) 단순 인용 정정 (governance-preconditions 자체 R1-2 정의로 변환) | **(A) multi-source 재기술** — 33번째 entry R-3 BLOCKING 답습. ADR-008 본문 실 권위 (차단조건 #1/#4/#6 + 부록 B) + ADR-010/ADR-011/ADR-009 multi-source 정확 attribution |
docs/phase0/mvp1-r-s1-framing-correction-brief.md:175:| 2 | R-S1 raw verify 답습 명문 (33번째 Reviewer + Agent B + codex 일치) + ADR-008 본문 §A.2 = "Hermes JSONL Export 검증" + R1-2 식별자 부재 cross-check | ✅ §2.1 |
docs/architecture/implementation-runtime-roadmap-mvp1.md:137:| (c) | ADR / SDD 권위 명시 | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 + R-4 + 본 §3 (36번째 entry R-S1 정정 답습) | ADR-008 차단조건 #4 + 부록 B + ADR-009 C-N §5 + ADR-011 + P1 v2 + 본 §4 (36번째 entry R-S1 정정 답습) |
docs/architecture/implementation-runtime-roadmap-mvp1.md:143:> ⭐⭐⭐ **2026-05-27 발효 (32번째 entry)**: **GP-3 5/5 + GP-5 5/5 모두 충족 자격 자격 인정 + 사용자 명시 결정 = MVP-1 Implementation Evidence PASS *완전 발효* (α)**. 본 발효 = (b1) 4 sub-cycle 완료 (PC-1-T3 `3a63a5b` + S-3 `4451716` + ST-2 `1edc5bb` + AR-3 `7f57323`/`7c294bb`/`73ed20d`/`9837298`) + 31번째 entry 첫 PR (head SHA `9837298befdeda6c7e170879cc9f15e331c52bce`) 11/11 SUCCESS + mergeable CLEAN + main branch protection 7 contexts 발효 evidence + 본 cycle 풀 3+1 + 외부 LLM 1+ APPROVE WITH CONDITIONS 답습 (`docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md`). carry-over (PASS 효과 영향 0건): (b2) R-S1 cross-reference 정정 + PC-1-T3 PoC evidence 자율 수집 + ST-2 nightly actual run id 자율 수집 + paths-aware workflow audit (R-6 답습).
docs/architecture/implementation-runtime-roadmap-mvp1.md:205:| **ST-1** | **Hermes Dockerfile entrypoint stat 검증** (chmod 600 강제) | 컨테이너 시작 시 | ✅ 필요 (Hermes upstream Dockerfile 수정) | ❌ | 低 | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + GP-3 §5.3 답습 (36번째 entry R-S1 정정 답습) |
docs/architecture/implementation-runtime-roadmap-mvp1.md:206:| **ST-2** | **inotify sidecar** (mtime/perm 변경 → 컨테이너 정지) | 런타임 지속 | ❌ (sidecar 분리 가능) | ✅ | 中 (sidecar process 운영) | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + GP-3 §5.3 답습 (36번째 entry R-S1 정정 답습) |
docs/architecture/implementation-runtime-roadmap-mvp1.md:207:| **ST-3** | **docker secret 직접 사용** | 런타임 (file system 통한 노출 회피) | 부분 (docker-compose.yml 갱신) | ❌ | 低 | ADR-008 차단조건 #6 (Docker 격리) + GP-3 §5.3 답습 (36번째 entry R-S1 정정 답습) |
docs/architecture/implementation-runtime-roadmap-mvp1.md:209:| **ST-5** | **ST-1 + ST-2 + ST-3 통합** (Defense in depth) | 시작 + 런타임 + file system | ✅ 필요 | ✅ | 中-高 | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + GP-3 §5.3 통합 답습 (36번째 entry R-S1 정정 답습) |
docs/architecture/implementation-runtime-roadmap-mvp1.md:283:| ADR-008 cross-reference 갱신 (차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011) | ADR-008 본문 답습 (cross-reference 한정, R-MVP1-PASS-2 영구 금지 답습) | ✅ 35번째 entry (b2) gov + backlog1 + 36번째 entry (b2-roadmap) roadmap-mvp1 본문 R-S1 정정 완료 답습 |
docs/architecture/implementation-runtime-roadmap-mvp1.md:506:> ⭐⭐⭐ **2026-05-27 발효 완료 (32번째 entry, commit `(본 commit)`)**: 본 5/5 매트릭스 양 GP 모두 충족 자격 자격 인정 + 사용자 명시 결정 + 본 cycle 풀 3+1 + 외부 LLM 1+ APPROVE WITH CONDITIONS 답습 = **MVP-1 Implementation Evidence PASS *완전 발효 (α)***. 답습 source: (b1) 4 sub-cycle (PC-1-T3 + S-3 + ST-2 + AR-3) + 31번째 entry 첫 PR (head SHA `9837298befdeda6c7e170879cc9f15e331c52bce`) 11/11 SUCCESS + mergeable CLEAN + 본 cycle 합의 (`docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md`, BLOCKING 6 + 권고 5 1pass 흡수). carry-over (PASS 효과 영향 0건): (b2) R-S1 cross-reference 정정 (별도 sub-cycle, ADR-008 본문 변경 0건 영구 의무 R-MVP1-PASS-2 답습) + PC-1-T3 PoC evidence 자율 수집 + ST-2 nightly actual run id 자율 수집 + paths-aware workflow audit (R-MVP1-PASS-8 답습 + R-6 BLOCKING 답습 = 다음 cycle 우선순위).
docs/architecture/implementation-runtime-roadmap-mvp1.md:660:| **ST-3** | docker secret (저장 경로 isolation) | GP-3 저장 경로 secret 검출 (G3-1) | ADR-008 차단조건 #6 (Docker 격리) 답습 + Layer A §1.2 + Layer B §1.1 답습 (36번째 entry R-S1 정정 답습) | Vault HSM ST-4 미진입 (Backlog #7 분리) / entrypoint stat ST-1 / inotify ST-2 미진입 (Backlog #1 1.5차 보강 분리) |
docs/architecture/implementation-runtime-roadmap-mvp1.md:827:| 2026-05-27 (32번째 entry) | ⭐⭐⭐ **MVP-1 Implementation Evidence PASS 완전 발효 (α)** — §2.2 (line 141 영역) + §3.6.3 (GP-3 합의 형태 권고 표) + §4.7.3 (GP-5 합의 형태 권고 표) + §5.1 (통합 PASS 권고) 각 영역에 "2026-05-27 발효 완료" 행 추가 | (b1) 4 sub-cycle 완료 (PC-1-T3 `3a63a5b` + S-3 `4451716` + ST-2 `1edc5bb` + AR-3 chain `7f57323`/`7c294bb`/`73ed20d`/`9837298`) + 31번째 entry 첫 PR (head SHA `9837298befdeda6c7e170879cc9f15e331c52bce`) 11/11 SUCCESS + mergeable CLEAN + main branch protection 7 contexts 발효 evidence + 본 cycle 풀 3+1 + 외부 LLM 1+ APPROVE WITH CONDITIONS (`docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md`, BLOCKING 6 + 권고 5 1pass 흡수). 본 흡수 = §2.2 + §3.6.3 + §4.7.3 + §5.1 + §9 갱신 한정 — §3 GP-3 / §4 GP-5 / §5.2~§5.5 / §6 / §7 본문 변경 0건. carry-over (PASS 효과 영향 0건): (b2) R-S1 + PC-1-T3 PoC 자율 + ST-2 nightly 자율 + paths-aware audit (R-6 BLOCKING 답습) |
docs/architecture/implementation-runtime-roadmap-mvp1.md:837:**다음 단계** (2026-05-27 32번째 entry 후): ✅ (b) MVP-1 1.5차 보강 합의 완료 (24번째 entry) → ✅ (b1) 4 sub-cycle 완료 (PC-1-T3 + S-3 + ST-2 + AR-3) → ✅ (c) **Implementation Evidence PASS 완전 발효 완료** (32번째 entry, 본 commit) → ⏳ (D-5 재조정 R-6 BLOCKING 답습): paths-aware workflow audit (R-MVP1-PASS-8 답습) → (b2) R-S1 cross-reference 정정 + (b3) framing 정정 (병렬) → Markdown evidence 통합 (D-3 carry-over) → (b1-PC1-D6) bypass detection CI 통합 → PR #2 merge 결정 (사용자 자율) → (d) facade real → MVP-2 진입 자격 검토 (별도 합의 영역)
docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:3:> **본 brief v1.1 = (R4-evidence) brief v1 (`12a3191`, 381줄) 의 풀 3+1 합의 (`f7ed37d`, 346줄, APPROVE w/ COND + BLOCKING 9 + R-S1~R-S5 + 권고 16 + NOTE 15 + 기각 5) verbatim 본문 직접 반영.** v1.1 진입 자격 = (1) BLOCKING 9 verbatim 100% 반영 (R-21 답습 영구) / (2) R-S1~R-S5 정정 흡수 11+곳 / (3) 명명 일관성 통일 = "(R4-evidence)" 단일 + 후속 본문 정정 cycle = "**(R4-body)**" 변경 (R-S2 발효, (g1-N) chain 영구 종결 의무 답습 영구 framing 정합) / (4) §2.2 line 33 → **line 63** verbatim 정정 (R-S1 발효) / (5) §3.5 Phase 1 행 추가 (5-way framing, R-S5 발효) / (6) §11 v→v1.1 변경 일람 신규 / (7) 본 cycle = read-only analysis only (단 brief commit + raw report 단계 R-1 anchor 24회 sudo 1회 의무 자격 별도 분리 명문, R-S4 발효). 자동 다음 단계 진입 0건 (chain 영구 종결 의무 답습 영구).
docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:10:- **(R4-evidence) 풀 3+1 합의** (`docs/review/3plus1-consensus-2026-05-25-jarvis-mvp1-r4-framing-evidence-entry.md`, commit `f7ed37d`, 346줄, BLOCKING 9 + R-S1~R-S5 + 권고 16 + NOTE 15 + 기각 5) — **본 brief v1.1 의 직접 input 자격 영구**
docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:15:- **MVP-1 합의 보고서** (`docs/review/3plus1-consensus-2026-05-22-jarvis-mvp1-local-boss.md`, R4 verbatim **line 63**, R-S1 발효 정정)
docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:25:1. MVP-1 합의 R4 본문 verbatim read (MVP-1 brief line 20/124~125/141 + MVP-1 합의 보고서 **line 63**, R-S1 발효 정정) + 현재 framing 명문
docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:62:  - F-2 ⭐⭐⭐: R-S1 완벽 raw evidence (Ollama 자체 standard copy + 별도 inode + content-addressable sha256)
docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:65:  - **R4 본문 verbatim (MVP-1 합의 보고서 line 63, R-S1 발효 정정 확정)**: "**R4** | M3 런타임 재조정 — **llama.cpp ↔ Ollama 동급**(MoE 실측 llama.cpp ~31 tok/s, Ollama MoE 미공개), V-1에서 둘 다 MoE 측정. **vLLM \"제외(#36821)\" → \"MVP-1 비채택, MVP-2 재검토\"**(sm_120/121 binary-compat·0.17 해소 흐름; 영구배제는 C-2 충돌) | C | 🔴 정합"
docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:95:## 2. MVP-1 합의 R4 본문 verbatim (read-only, R-S1 발효 line 63 + R-S3 발효 nested quote 정직성)
docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:108:### 2.2 MVP-1 합의 보고서 R4 verbatim (R-S1 발효 line 63 정정)
docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:110:> **R4 행 verbatim (line 63, R-S1 발효 line 33 → line 63 정정 확정)**: "**R4** | M3 런타임 재조정 — **llama.cpp ↔ Ollama 동급**(MoE 실측 llama.cpp ~31 tok/s, Ollama MoE 미공개), V-1에서 둘 다 MoE 측정. **vLLM \"제외(#36821)\" → \"MVP-1 비채택, MVP-2 재검토\"**(sm_120/121 binary-compat·0.17 해소 흐름; 영구배제는 C-2 충돌) | C | 🔴 정합"
docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:159:- **R-S1 발효 완벽 evidence**: **Ollama 자체 standard copy** ((h-OM) raw line 44 답습 영구, Ollama issue #1450 closed-as-not-planned + docs.ollama.com/import "regular copy" 답습)
docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:169:| Source | Ollama library (다른 conversion) | bartowski Q4_K_M | bartowski Q4_K_M | Ollama library blob | **(h) bartowski blob (R-S1 발효 Ollama 자체 standard copy)** |
docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:203:- **"동급" 단언 부적정성 자격 강함** (S1 confirmed + R-S1 완벽 raw evidence 답습 영구)
docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:213:  - Ollama **(h-OM) Qwen3-30B-A3B bartowski Modelfile** decode generation = **14.69 t/s** (R-S1 발효 standard copy 답습)
docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:238:| evidence 강도 (3 차원 a/b/c + 4 차원 격차 + model variant) | ⭐⭐⭐ HIGH (4-way + Phase 1 5-way confirmed, S1 + R-S1 답습 영구) |
docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:251:  - MVP-1 합의 보고서 R4 행 **line 63** 답습 (R-S1 발효 정정)
docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:279:   - (h-O) ↔ (h-OM): source conversion lineage 변수 (R-S1 발효 Ollama 자체 standard copy)

exec
/bin/bash -lc "nl -ba docs/decisions/ADR-008-hermes-adoption-decision.md | sed -n '1,180p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# ADR-008: Hermes Agent 도입 결정 (Option B)
     2	
     3	**상태**: 승인 (3+1 합의 완료, 사용자 Option B 선택)
     4	**날짜**: 2026-05-04
     5	**의사결정자**: 사용자 + 3+1 에이전트 합의
     6	
     7	---
     8	
     9	## 맥락 (Context)
    10	
    11	사용자가 "Hermes Agent를 메인 오케스트레이터로 도입, Claude Opus 4.7과 GPT-5.5를 서브 LLM으로 활용"하는 시스템 진화를 제안. 현재 시스템은 Claude Code 단일 의존이며, 사용자는 모델/구독 교체의 자유를 강하게 요구함 (Provider Liquidity 하드 제약: "Claude Max 사용중이지만 모델 성능에 따라 구독 취소나 모델 변경이 용이해야함").
    12	
    13	## 결정 (Decision)
    14	
    15	**Option B 채택**: Hermes를 메인 오케스트레이터로 단계 도입하되, **6개 차단조건이 모두 충족된 후에만 다음 Phase로 진입**한다.
    16	
    17	### 6개 차단조건 (비협상)
    18	1. **SQLCipher**로 Hermes SQLite 암호화 + redaction 필터 (헌법 제8조 준수)
    19	2. **JSONL export 표준** + 메모리/스킬 마이그레이션 경로 정의 (Hermes lock-in 회피)
    20	3. v0.x API **버전 핀** + 회귀 테스트 + 카나리 환경
    21	4. **provider 어댑터 1개 추상화** + 분기 코드 금지 (depcruise로 강제)
    22	5. **최소 2 provider always-on** (단일 구독 의존 금지)
    23	6. Docker **격리 + egress 화이트리스트**
    24	
    25	### 단계 마이그레이션
    26	- **Phase 1** (1~2주): Hermes worktree 설치, **API 키만 사용**(OAuth 직결 금지), 비핵심 작업 검증
    27	- **Phase 2** (2~4주): Layer 5(3+1 합의)만 Hermes 서브에이전트로 이전 (A=Claude / B=GPT / C=로컬)
    28	- **Phase 3** (조건부): Hook 계층 watchexec 재구축 + provider 어댑터 본격 적용. **선결조건**: Phase 2 메트릭 ≥ 현 시스템
    29	
    30	## 선택지 (Options Considered)
    31	
    32	### Option A: LiteLLM 우선 + Hermes 좁은 PoC (3+1 권장 ★★★★★)
    33	- 장점: Provider Liquidity 본업 충족, 기존 SDD/TDD 자산 100% 보존, 즉시 시작
    34	- 단점: Hermes 셀프-임프루빙 가치 일부 늦게 확인
    35	
    36	### Option B: Hermes 메인 + 6개 차단조건 단계 도입 ⭐ **채택**
    37	- 장점: 사용자 원안 직접 실현, 셀프-임프루빙 빠른 체험
    38	- 단점: 차단조건 6개 미충족 위험, v0.x 불안정, Hook 재구축 공수 미지수
    39	
    40	### Option C: 6개월 보류
    41	- 장점: 신생 프레임워크 리스크 회피
    42	- 단점: 다중 LLM 활용·Liquidity 개선 지연
    43	
    44	## 근거 (Rationale)
    45	
    46	3+1 합의는 Option A를 1순위로 권장했으나, 사용자가 의식적으로 Option B를 선택. 사용자 의지·선호 존중. 단, 6개 차단조건은 **비협상** — 미충족 시 자동 NO-GO하며, Hermes 도입을 중단하고 Option A로 자동 폴백한다.
    47	
    48	## 3+1 에이전트 합의 결과
    49	
    50	| 에이전트 | 의견 | 핵심 근거 |
    51	|---------|------|----------|
    52	| Agent A (구현) | 조건부 GO | 8-Layer 통합 MEDIUM, Phase 1·2 즉시 가능, Phase 3는 Hook 재구축 PoC 성공 시 |
    53	| Agent B (품질) | GO with strict conditions | R1 학습루프 평문(CRITICAL), R2 Hermes lock-in(CRITICAL), 6개 차단조건 미충족 시 HOLD |
    54	| Agent C (대안) | LiteLLM 우선 권장 (Option A) | Liquidity는 도구 추상화 문제, Hermes만의 솔루션 아님 |
    55	| **Reviewer** | **Option A 1순위, B는 차단조건 충족 시 가능** | 메타 한계 보정으로 C에 가중치, 사용자 선호 시 B 진행 가능 |
    56	
    57	## CRITICAL 위험 (운영 중 상시 감시)
    58	
    59	- **R1 학습루프 평문 누적**: Hermes SQLite FTS5에 사용자 컨텍스트·LLM 응답·환경변수 echo가 평문 영구 저장. **헌법 제8조 직접 위반**. 차단조건 #1 미구현 시 자동 NO-GO.
    60	- **R2 Hermes 자체 lock-in**: 누적 학습 결과(스킬/메모리/프로필)는 Hermes 떠나면 손실. Provider Liquidity 정신 위반. 차단조건 #2 미정의 시 자동 NO-GO.
    61	- **A-meta ChatGPT Pro Codex CLI OAuth ToS 위반 가능성**: 위반 시 구독 강제 해지 → 시스템 정지. **API 키 경로만 사용**.
    62	- **R4 Claude Max OAuth race**: 다수 미해결 버그(#15080, #6475, #12905, #10575) — Hermes 동시 호출 시 무한 인증루프 가능. API 키 경로 우선.
    63	- **R8 단일 구독 의존**: 어떤 단계에서도 single point of failure 금지. 차단조건 #5로 강제.
    64	
    65	## 메타 한계 (사용자 인지 필요)
    66	
    67	본 합의는 3 Claude 에이전트가 작성. Hermes(외부 도구)에 대한 평가에 친화 편향 가능. Reviewer가 Agent C 회의적 입장에 의식적 가중치 부여로 보정함. Option B 진행 중에도 외부(비-Claude) 검증 권장.
    68	
    69	## 결과 (Consequences)
    70	
    71	- **긍정적**: 다중 LLM 환경 구축, 셀프-임프루빙 학습루프 도입 시도, Provider Liquidity 강제 메커니즘 정착
    72	- **부정적**: 신생 프레임워크 리스크 감수, Hook 재구축 공수 발생, v0.x API 변동 대응 부담, R1/R2 차단조건 미충족 시 전면 폴백 위험
    73	- **주의사항**:
    74	  - 6개 차단조건 중 1개라도 미충족 시 도입 중단 → Option A 자동 폴백
    75	  - 진행 중에도 정기적 재평가 (Phase 종료마다)
    76	  - 차단조건 충족 검증은 별도 SDD 문서로 명세 예정
    77	  - Provider Liquidity 위반 패턴 6종(모델명 분기/provider별 후처리/스킬 내 모델 가정 등)은 depcruise 룰로 정적 차단
    78	
    79	---
    80	
    81	**관련 문서** (2026-05-09 후속 9 cross-reference 갱신, 결정 내용 변경 0건 — 단축 합의 APPROVE Reviewer-only):
    82	
    83	### 합의 보고서 / 헌법
    84	
    85	- `docs/review/3plus1-consensus-2026-05-04-hermes.md` (3+1 합의 보고서 전문)
    86	- `docs/constitution/PROJECT_CONSTITUTION.md` 제8조 (보안), 제5조 관용 (Provider Liquidity, 비협상)
    87	- `~/.claude/projects/-home-delangi----project-category-AI-development-tool/memory/feedback_provider_liquidity.md` (Provider Liquidity 영구 기억)
    88	
    89	> **[Cross-reference Block — (g1-N-3-adr-008+sip+adr-012') R-7 (f) cross-ref block 만 채택 + R-S3 답습]**: 본 line 86 표기 "제5조 관용 (Provider Liquidity, 비협상)" = (g1-N-1) commit `148fbbe` 후 **헌법 제5조-2: Provider Liquidity 원칙 (비협상) (line 75~80)** 직접 모법 발효 — (g1-N-1) 이전 관용 표현 답습. 본 cycle = gov §1.1 line 78 verbatim 명문 4 source ("ADR-008 / ADR-011 / system-identity-prequel / 본 v3") 中 ADR-008 정정 자격 직접 발효 (R-S3 CRITICAL). ADR-008 = ADR-011 직접 모법 (ADR ↔ ADR 부록 B Amendment 패턴). (g1-N-3-pamsd) `ab96e30` 동형 패턴 답습, **본문 verbatim 변경 0건** ((f) cross-ref block 만 채택). 정정 후 형식 = ADR-011 line 245 모법 "제5조-2 관용 (Provider Liquidity, 비협상)" (R-rec-3 답습 + 사용자 명시 직접 확인). 추가 위치 line 87/98/107/274/329/366/370 (P2 cross-ref + P3 본문) = (P3) 본문 답습 본질 동형, 정정 자격 약함 ((P3) 약식 통일 cycle DEFER carry-over). 본 cycle 합의 = `209f04d`.
    90	
    91	### Hermes 도입 설계 (P2)
    92	
    93	- `docs/architecture/hermes-adoption-design.md` (P2 v2, **Archived 2026-05-09 후속 7** — 옵션 A 최소 침습 — 헤더 갱신 + 본문 보존, path 변경 0건. archive 합의: `docs/review/3plus1-consensus-2026-05-09-p2-v2-archive-decision.md`)
    94	- **`docs/architecture/hermes-adoption-design-v3.md`** (P2 v3, **Adopted — Design Adoption only, 2026-05-09 후속 6, 후속 권위**) — P2 v2 §2.1.3 가정 (외부 pre-record hook) 폐기 + R-2~R-7 evidence 흡수 + G1b PASS 권위 + Hermes PMO 구조 사전 정의 (활성화 *아님*) + G2/G3/G4 entry/exit. **본 ADR-008 의 Option B 단계 마이그레이션은 P2 v3 §2.6 + §11.1 + §2.6.1 12 조건 PMO 격상 체크리스트로 운영 절차화** (인간 전문 리뷰 의무 명문화, P2 v3 §2.6 단계 5.5)
    95	- `docs/architecture/system-identity-prequel.md` (**Archived 2026-05-09 후속 8** — AI Dev Company OS 정체성 직접 권위 출처 영구 보존. archive 합의: `docs/review/3plus1-consensus-2026-05-09-system-identity-prequel-archive-decision.md`)
    96	
    97	### Provider 추상화 / Adapter (차단조건 #4)
    98	
    99	- `docs/architecture/llm-providers-design.md` (P1 v2, LiteLLM facade — Option β 채택)
   100	- **`docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md`** (C-N 갱신 2026-05-09 후속 4 — P1 facade MVP 진입조건 명시 + **Hermes PMO ↔ provider 분리 영구 권위 (§2.3)** + **Provider Liquidity 5-way Multi-layer Defense 모법 ADR Layer 1 (§5)** + v2.0 트리거 vs MVP 조건 분리 + P2 v3 cross-reference). 본 ADR-008 차단조건 #4 (provider 어댑터 추상화) 의 *Hermes PMO ↔ provider 분리* 권위 출처
   101	
   102	### 차단조건 #1 충족 (수단/목적 분리)
   103	
   104	- **`docs/decisions/ADR-011-means-vs-ends-redaction.md`** (수단/목적 분리 원칙 — 본 ADR-008 부록 B Amendment R1 specific 갱신의 권위 근거. §2.1 (a)~(d) 4조건 + §2.2 G1a/G1b 분리 + §2.3 Hermes ≠ root of trust 영구 권위 + §2.4 T1/T2/T3 영구 권위)
   105	- `docs/decisions/ADR-010-sqlcipher-vault-key-management.md` (SQLCipher Vault HSM 키 관리 — 차단조건 #1 키 관리 측면)
   106	
   107	### Evidence 무결성 (2026-05-09 후속 3 PR-2 신규 발행)
   108	
   109	- **`docs/decisions/ADR-012-evidence-ledger-protection.md`** (Evidence Ledger Protection — 본 ADR-008 차단조건 #2 (JSONL export 표준) 의 *Evidence Ledger 무결성* 강화 권위. 12 보호 원칙 + Layer 1~5 다층 강제 + RFC 8785 JCS + Hermes 변조 차단 매트릭스 4항목 + Provider Liquidity 5-way Layer 5)
   110	- 신규 위반 경로 P10 (Evidence Forgery) 정식 등록 (G2 §1.2.6, 2026-05-09 후속 5)
   111	
   112	### 4 게이트 정식 산출 (2026-05-09 Design/Governance Gate PASS Bundled)
   113	
   114	- `docs/architecture/governance-preconditions.md` (G2, **Design/Governance Gate PASS Bundled, 2026-05-09**) — 6 거버넌스 사전조건 GP-1~GP-6 + §1.2.6 P10 Evidence Forgery 정식 등록. **GP-1 = G1b PASS evidence 흡수 (Implementation/Runtime PASS), GP-2~GP-6 = Design PASS / Implementation Pending**
   115	- `docs/architecture/hermes-not-root-of-trust-runtime.md` (G3, **Design/Governance Gate PASS Bundled**) — 권위 위계 운영 + Hermes 권한 22 항목 (T1 8 / T2 2 / T3 12) + Hermes 변조 차단 매트릭스 4항목. **운영 구현 = Design PASS / Implementation Pending**
   116	- `docs/architecture/provider-agnostic-memory-skill-design.md` (G4, **Design/Governance Gate PASS Bundled** + §4.2 11 필드 schema + §4.4 hash chain 사양 + §4.6 round-trip 검증 절차 보강 PR-2). **라운드트립 + migration script = Design PASS / Implementation Pending**
   117	- `docs/phase0/redaction-verification-sop.md` (R-7 SOP — G1b PASS 정식 충족 절차)
   118	
   119	### 부록 B §B.6 정식 충족 절차 cross-reference (G1b PASS + G2 GP-1 흡수)
   120	
   121	- 부록 B §B.6 R-3 ~ R-7 6단계 ✅ 완료 (2026-05-06 ~ 2026-05-07 Part 1) + R-6 GitHub Actions actual run `25482284523` PASS (24초, 42/42, leak 0) + R-7 SOP §7.3 단축 합의 APPROVE Reviewer-only (2026-05-07) → G1b CONDITIONALLY PASS → **PASS** 승격 + Phase 1 acceptance PARTIAL → **PASS** 선언. **G2 GP-1 = G1b PASS evidence 흡수** (Tier-1 한정, 2026-05-09 G2 정식 PASS 시점)
   122	
   123	---
   124	
   125	## 부록 A — 검증 결과 (2026-05-04)
   126	
   127	Phase 1 진입 전 사실 확인 작업 2건 완료. 결과 CRITICAL 위험 2건이 다운그레이드되었으나, 차단조건 6개는 그대로 유지(방어 자세).
   128	
   129	### A.1 ChatGPT Pro Codex CLI ToS 검증
   130	- **공식 지원**: Hermes는 OpenAI Codex `device code` OAuth flow를 정식 지원. credentials는 `~/.hermes/auth.json`에 저장, `~/.codex/auth.json`에서 import 가능
   131	- **개인 단일 사용자 시나리오**: ToS 위반 위험 **LOW** — Codex CLI 자체와 동등 사용
   132	- **금지 사례**: "Reselling access" 또는 "third-party services에 ChatGPT 전력 공급". 본 프로젝트는 개인 사용이므로 해당 없음
   133	- **정책 변동성**: OpenAI/Anthropic가 third-party 도구의 구독 집계를 최근 제한한 사례 존재 → API 키 경로 우선 정책은 그대로 유지
   134	- **A-meta 위험 등급**: CRITICAL → **MEDIUM** (정책 변동 모니터링 필요)
   135	
   136	### A.2 Hermes JSONL Export 검증
   137	- **공식 명령어**: `hermes sessions export backup.jsonl` 존재. 전체/플랫폼별/단일 세션 export 지원, full message history 포함
   138	- **데이터 저장소 정정**: ChromaDB는 사용하지 않음. **SQLite + FTS5 단일** — 암호화는 SQLCipher 단일 적용으로 충분 (차단조건 #1 단순화)
   139	- **마이그레이션 도구**: `hermes claw migrate` (OpenClaw → Hermes) 존재. 역방향 export는 sessions 단위로 가능
   140	- **스키마 버전 관리**: `schema_version` 테이블 존재
   141	- **R2 위험 등급**: CRITICAL → **HIGH** (skills/memory 범위는 P1 설계 단계에서 추가 검증)
   142	- **추가 검증 항목**: `hermes sessions export`가 sessions만 다루는지, agent-curated memory와 skills도 포함하는지 P1에서 확인 필요
   143	
   144	### A.3 차단조건 영향
   145	6개 차단조건은 **그대로 유지**. 검증 결과는 충족 가능성을 높였을 뿐 의무를 약화하지 않음.
   146	- #1 SQLCipher: 적용 대상이 SQLite 단일 → 구현 단순화
   147	- #2 JSONL export: 공식 명령어 활용. skills/memory 범위 보강 필요
   148	- #3 버전 핀: 그대로
   149	- #4 어댑터 추상화: 그대로 (P1 설계의 핵심)
   150	- #5 2 provider always-on: 그대로
   151	- #6 Docker 격리: 그대로
   152	
   153	---
   154	
   155	## 부록 B — Amendment (2026-05-06): R1 해석 갱신 (수단/목적 분리)
   156	
   157	**상태**: 갱신 (단축 합의 — Reviewer-only)
   158	**날짜**: 2026-05-06
   159	**근거 ADR**: `docs/decisions/ADR-011-means-vs-ends-redaction.md`
   160	**근거 Phase 0 evidence**: R-1 FAIL (`docs/phase0/day2-r1-redaction-location-verification.md`), R-2 PASS (`docs/phase0/day3-r2-sqlite-trigger-poc.md`)
   161	**근거 합의**: `docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md`
   162	
   163	### B.1 R1 비협상 핵심 재정의
   164	
   165	R1의 비협상 핵심은 **특정 외부 hook 구현이 아니라, AI 학습 루프/메모리 DB에 비밀값이 평문으로 영구 저장되지 않도록 차단하는 결과**이다.
   166	
   167	본 Amendment 이전 부록 A R1 텍스트는 "외부 pre-record hook"을 수단으로 가정한 표현을 포함했다. 본 Amendment는 그 가정을 ADR-011 §2.1 수단/목적 분리 원칙에 따라 갱신한다.
   168	
   169	### B.2 G1a / G1b 분리 관리
   170	
   171	Hermes native redaction이 DB INSERT 경로에 적용된다는 기존 가정은 **R-1에서 FAIL로 판정**되었다.
   172	
   173	그러나 R-2 PoC에서 SQLCipher BEFORE INSERT trigger 기반 DB-level fallback이 plaintext secret persistence를 차단할 수 있음이 실증되었으므로, G1은 다음과 같이 분리 관리한다:
   174	
   175	- **G1a**: Hermes native redaction applies before DB INSERT — **FAIL** (폐기)
   176	- **G1b**: DB-level fallback prevents plaintext secret persistence — **PASS by R-2 PoC** (정식 충족은 R-3~R-7 후)
   177	
   178	정식 충족 조건은 ADR-011 §2.2 G1b 정식 충족 조건 표를 따른다.
   179	
   180	### B.3 권위화 출처

exec
/bin/bash -lc "rg -n \"RT-|E-[1-9]|Rollback|Evidence|R-S1|P-4|ADR-011 §2.1|\\(a\\)~\\(e\\)|Layer 4\" docs/phase0/mvp2-entry-brief.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
5:> **scope**: MVP-2 영역 (G2 GP-2 송신 redaction + G4 §4.4 Layer 4 CI 회귀 검증) 본격 진입 합의
21:- (β) sub-수단 결정 cycle — R-1/2/3/4/5 (GP-2) + L-1/2/3/4/5 (G4 §4.4 Layer 4) — 별도 합의 또는 (α) 內 흡수
22:- (γ) 분리 영역 결정 — G4 §4.4 Layer 1+2 의존 영역 우선 진입 vs Layer 4 동시 진입
28:1. **MVP-2 영역 정의 답습** — 51 entry audit brief §1.3 (GP-2 송신 redaction + G4 §4.4 Layer 4 CI 회귀 검증) 직접 답습 (§1)
29:2. **51 entry audit brief 답습 cross-check** — 진입 자격 매트릭스 (GP-2 Entry 2/3 + Exit 2.5/5 / G4 §4.4 Layer 4 Entry 3/8 + Exit 1/5) 정합성 검증 (§2)
30:3. **선행 권위 답습** — 32 entry MVP-1 Implementation Evidence PASS *완전 발효 (α)* + roadmap-mvp1 §1.2 (3-layer PASS) + §1.3 (GP-2 = MVP-2 분리 사유) + ADR-011 §2.1 (a)~(e) 5조건 모법 (§1.1)
32:5. **두 영역 *진입 자격* 분석** — ADR-011 §2.1 (a)~(d) + 합의 APPROVE 운영조건 (e) 5조건 매트릭스 (§3)
36:9. **Rollback Trigger / Evidence 기준 본문 후보** (§5)
55:| 12 | **G4 §4.4 Layer 4 sub-수단 결정** (L-1 / L-2 / L-3 / L-4 / L-5 中 채택) | 0건 ((β) 별도 cycle) |
56:| 13 | **G4 §4.4 Layer 4 분리 영역 결정** (Layer 1+2 의존 영역 우선 vs Layer 4 동시) | 0건 ((γ) 별도 cycle) |
58:| 15 | **MVP-2 Implementation Evidence PASS *발효*** | 0건 ((c) 진입점 = 본 (α) 진입 합의 → (β) sub-수단 결정 → 실 구현 sub-cycle → Implementation Evidence PASS 합의, 다층 분리) |
68:| 25 | G4 §4.4 Layer 1 / Layer 2 / Layer 3 / Layer 5 영역 진입 자동 결정 | 0건 (본 brief = Layer 4 한정, 다른 Layer = 별도 cycle 또는 의존 영역 자동) |
69:| 26 | GP-1 / GP-4 / GP-6 / G3 / G4 (Layer 4 외) 영역 진입 자동 결정 | 0건 (MVP-3 ~ MVP-5 영역 답습) |
75:- ✅ 본 brief 발효 결과 = **MVP-2 영역 진입 권한 발효** + (β) sub-수단 결정 cycle 진입 자격 발효 + (γ) 분리 영역 결정 cycle 진입 자격 발효 + Rollback Trigger 본문 채택 + Evidence 형식 본문 채택
79:- ❌ 본 brief 자체에서 MVP-2 Implementation Evidence PASS 발효 0건 (실 구현 + 합의 evidence 후 별도 합의)
90:| `3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md` (32 entry) | 2026-05-27 | ✅ **APPROVE WITH CONDITIONS** (풀 3+1 + 외부 LLM 1+) — MVP-1 Implementation Evidence PASS *완전 발효 (α)* | MVP-1 PASS 답습 그대로 유지 (재선언 0). MVP-2 = "Layer 2 Implementation Evidence PASS *2차*" 영역 답습 (roadmap-mvp1 §1.2 line 90 "MVP-2 ~ MVP-5 = GP-2 / GP-4 / GP-6 / G3 / G4 의 본 PASS 단계"). |
92:| `implementation-runtime-roadmap-mvp1.md §1.3` | 2026-05-12 (APPROVED 2026-05-27) | 본문 line 101~107 = "GP-2 = MVP-1 vs MVP-2 분리 사유 (C-7 답습)" — "GP-2 는 **MVP-2** 의 Implementation Evidence PASS 영역 *우선순위 1* (C-7 line 379 답습) — 본 분리는 *시점* 분리이지 *영구 제외* 아님" | 본 cycle = GP-2 시점 진입 자격 발효 (분리 *해제* — *영구 제외* 아님 답습 정확). |
93:| `implementation-runtime-roadmap.md §6` | 2026-05-09 (APPROVED) | 그룹 D (Order 4+5): G2 GP-3 + G2 GP-2. GP-3 = MVP-1 완료, **GP-2 잔존**. 그룹 C (Order 3 tie): G4 JSONL hash chain + JCS + Round-trip PoC (G4 §4.4 영역) | 본 cycle = 그룹 D 잔존 GP-2 진입 + 그룹 C G4 §4.4 Layer 4 진입 통합. |
94:| `ADR-011 §2.1 (a)~(e)` | 2026-05-06 | 5조건 모법 — (a) 동등 보안 결과 / (b) 격리 PoC / (c) ADR/SDD 권위 / (d) 자동 회귀 검증 / (e) 합의 APPROVE | 본 cycle = MVP-2 영역 진입 자격 = 5조건 *경로* 권고 (충족 자체는 실 구현 sub-cycle 후 별도 합의). |
101:| **G4 §4.4 Layer 4 — CI 회귀 검증** | G4 | Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증 + canonical JSON 위반 검출 + timestamp monotonicity 검증 + R-6 workflow 답습 확장. MANDATORY 등급 (Layer 5 中 4번째, Layer 1+2+4 MANDATORY, Layer 3+5 RECOMMENDED MVP) | `provider-agnostic-memory-skill-design.md §4.4.1 line 649~653` (Layer 4 정의) + `ADR-012 §2.3` (다층 강제) + `ADR-012 §3.4` (timestamp monotonicity) |
105:> **본 §1.3 = 본 brief 의 *핵심 framing*** — 선행 권위 (51 entry audit brief / roadmap-mvp1 §1.3 / governance-preconditions §4 / G4 §4.4 / ADR-012 §2.3) 와 본 (α) cycle (2026-05-28) 결정 사이의 *변경 차이* 를 명시. 변경 자격 정당성 = (a) 사용자 명시 권위 우선 + (b) 본 cycle 합의 형태 = 풀 3+1 + 외부 LLM 1+ + 사용자 명시 = ADR-011 §2.1 (e) + §2.4 T3 영역 답습 충실성.
110:| **G4 §4.4 Layer 4 진입 자격** | provider-agnostic-memory-skill-design §4.4 line 624 (Layer 1~5 MANDATORY/RECOMMENDED 매트릭스) + ADR-012 §2.3 line 165 "Layer 1 MANDATORY 모든 환경" + line 182 "Layer 4 RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점" | **Layer 4 = MANDATORY 등급, MVP-2 진입 영역 채택** | **⚠️ 권위 미세 충돌 흡수 — ADR-012 §2.3 line 182 = "Layer 4 RECOMMENDED MVP" vs G4 §4.4.1 line 649 = "Layer 4 MANDATORY"**. 본 cycle = G4 §4.4.1 line 649 답습 (Layer 4 = MANDATORY). ADR-012 §2.3 line 182 = Layer 4 *External anchor* (Layer 5 영역) 와 혼동 위험 (line 182 verbatim 재확인 의무, R-S1 유형 잠재 risk → 본 brief §10 P-? 자기진단 영역). 본 (α) 합의 발효 시 cross-reference 정정 cycle 후속 영역. |
114:→ **요약**: 본 (α) cycle = "MVP-2 영역 *진입* 합의" 한정 (수단 결정 = (β) 분리). 두 영역 모두 풀 3+1 + 외부 LLM 1+ + 사용자 명시 일관. R-S1 유형 잠재 risk (ADR-012 §2.3 line 182 verbatim 재확인) = §10 자기진단 명시 영역.
145:✅ **Rollback Trigger 본문 채택** (§5.1 답습 — RT-1 / RT-2 / RT-3)
146:✅ **Evidence 형식 본문 채택** (§5.2 답습 — E-1 / E-2 / E-3 / E-7 / E-8 / E-9)
153:❌ Implementation Evidence PASS 발효 = 실 구현 + (b) PoC + (d) R-6 actual run PASS + (e) 합의 APPROVE 후 별도 합의
155:### §2.2 G4 §4.4 Layer 4 — CI 회귀 검증 — 진입 자격
161:| **목적** | Evidence Ledger 무결성 자동 회귀 검증 — Layer 1 (hash chain) + Layer 2 (history) + canonical JSON 위반 + timestamp monotonicity 위반 자동 검출 |
163:| **메커니즘** | (L-1) Python stdlib 단독 (`hashlib.sha256` + `json.dumps(sort_keys=True, separators=(",",":"))`) + (L-2) RFC 8785 JCS Primary (`pyjcs` / `rfc8785`) + (L-3) Layer 4 R-6 workflow step + (L-4) L-1+L-3 병행 (MVP 권고) + (L-5) L-2+L-3 병행 (정식) |
164:| **권위 출처** | provider-agnostic-memory-skill-design.md §4.4.1 line 649~653 (Layer 4 정의) + ADR-012 §2.3 (Append-only + Hash Chain 다층 강제) + §2.5 (RFC 8785 JCS) + §2.7 (prev_hash 실패 처리) + §3.4 (timestamp monotonicity) |
175:| Layer 4 CI step 실 구현 | ❌ gap | 실 구현 sub-cycle 영역 |
183:✅ **G4 §4.4 Layer 4 영역 진입 발효 자격** — 본 (α) 합의 APPROVE 시점 발효
185:✅ **(γ) 분리 영역 결정 cycle 진입 자격 발효** — Layer 1+2 의존 영역 우선 진입 vs Layer 4 동시 진입 (별도 합의)
186:✅ **Rollback Trigger 본문 채택** (§5.1 답습 — RT-4 / RT-5 / RT-6)
187:✅ **Evidence 형식 본문 채택** (§5.2 답습 — E-4 / E-5 / E-6 / E-7 / E-8 / E-9)
192:❌ Layer 1 / Layer 2 / Layer 3 / Layer 5 영역 진입 결정 = (γ) 분리 영역 결정 cycle (Layer 1+2 의존 영역 우선 진입 vs Layer 4 동시 결정)
194:❌ Implementation Evidence PASS 발효 = 실 구현 + PoC + R-6 actual run PASS + 합의 후 별도
202:| **목적** | GP-2 §4.6 산출 후보 (log file canary inject step) + G4 §4.4 Layer 4 (Layer 1+2 자동 회귀 + canonical 위반 + timestamp monotonicity step) **단일 R-6 workflow (`r2-canary.yml`) 확장 통합** |
219:## §3 ADR-011 §2.1 (a)~(d) + 합의 APPROVE 운영조건 (e) — 5조건 매트릭스 (두 영역별)
223:| # | 조건 | GP-2 (§2.1) | G4 §4.4 Layer 4 (§2.2) |
229:| (e) | 합의 APPROVE | ❌ gap — 본 (α) 합의 APPROVE → 진입 권한 발효 / Implementation Evidence PASS 발효 = 별도 합의 (실 구현 + (a)~(d) evidence 완료 후) | ❌ gap — 동일 |
231:→ **본 (α) cycle 합의 발효 시점 — 두 영역 모두 (e) 진입 *권한* 충족 (Implementation Evidence PASS 발효 ≠ 본 (α), 별도 합의 영역)**.
235:- (γ) 분리 영역 결정 cycle → Layer 1+2 의존 영역 vs Layer 4 동시 결정
237:- MVP-2 Implementation Evidence PASS 발효 합의 → (a)~(e) 5/5 evidence + 사용자 명시 + 별도 합의
249:2. roadmap-mvp1.md §1.3 — "GP-2 = MVP-2 의 Implementation Evidence PASS 영역 *우선순위 1*" (큰 영역 = 풀 3+1 + 외부 LLM 1+ 의무)
250:3. 32 entry MVP-1 Implementation Evidence PASS 발효 합의 = 풀 3+1 + 외부 LLM 1+ 답습 패턴 (MVP-2 = 동격 영역)
252:5. ADR-011 §2.1 (e) + §2.4 T3 영역 답습 = "큰 결정 (MVP-2 진입) = 풀 3+1 + 외부 LLM 1+ + 사용자 명시"
256:| 영역 | 본 (α) 합의 (진입 권한) | 실 구현 sub-cycle (수단 결정 + 구현) | Implementation Evidence PASS 발효 |
259:| **G4 §4.4 Layer 4** | **풀 3+1 + 외부 LLM 1+** (본 (α)) | **(γ) 분리 영역 결정 = 풀 3+1** (Layer 1+2 의존 영역 우선 vs Layer 4 동시) + **(β) sub-수단 결정 = 풀 3+1** (L-1~L-5 中 L-4 MVP 권고, 51 brief §3.4 답습) + 실 구현 별도 sub-cycle | **풀 3+1 + 외부 LLM 1+ + 사용자 명시** (32 entry 답습) |
267:| 1 | 큰 결정 (영역 진입 발효 / 수단 결정 / threshold 고정) | ✅ **발화** | MVP-2 영역 진입 발효 = 큰 결정 (Layer 2 Implementation Evidence PASS 영역 *2차* 진입, roadmap-mvp1 §1.2 답습) |
270:| 4 | 권위 chain 다중 source 손상 위험 | ⚠️ **부분 발화 (R-S1 유형 잠재)** | §1.3 G4 §4.4 Layer 4 항목 = ADR-012 §2.3 line 182 verbatim 재확인 의무 (Layer 4 vs Layer 5 혼동 risk). 본 brief §10 P-? 자기진단 영역 명시. Reviewer 단독 verify 자격 (24 entry R-S1 답습 패턴) |
282:| G4 §4.4 Layer 4 | (1) 큰 결정 + (4) 잠재 R-S1 (Layer 4 vs Layer 5 혼동) + (5) 외부 LLM | 풀 3+1 + 외부 LLM 1+ |
286:## §5 Rollback Trigger / Evidence 기준 (본 cycle 합의 발효 시점 의무)
288:### §5.1 두 영역별 Rollback Trigger 본문 후보 (51 entry audit brief §5 답습)
292:| RT-1 | Hermes native redaction 우회 검출 | GP-2 | log file canary inject grep PASS 후 평문 leak 발견 | ADR-011 §2.3 #2 + R-7 SOP §5 ROLLBACK trigger R5 |
293:| RT-2 | P1 facade RedactionFilter 우회 | GP-2 | LLM API request body 평문 secret 검출 | P1 v2 §8.2 + ADR-008 차단조건 #1 보조 |
294:| RT-3 | base64 / URL-encoded evasion 신규 발견 | GP-2 (R-5 영역) | Tier-1 42 catalog 미커버 evasion 발견 | G3-4 답습 → MVP-2/3 영역 분리 (본 cycle 범위 외) |
295:| RT-4 | hash chain middle entry tampering 검출 | G4 §4.4 Layer 4 | Layer 1 검증 실패 | ADR-012 §2.7 (`chain_violation_detected` ledger entry) |
296:| RT-5 | canonical JSON 위반 검출 | G4 §4.4 Layer 4 | Layer 4 CI step FAIL | ADR-012 §2.5 + §원칙 5/6 + R-6 답습 (`canonical_json_fallback` 또는 BLOCK) |
297:| RT-6 | timestamp monotonicity 위반 | G4 §4.4 Layer 4 | Layer 4 CI step FAIL → BLOCK | ADR-012 §3.4 + R-6 답습 |
298:| RT-7 | R-6 workflow 자체 silent override | 통합 | gate enforcement bypass detected | G3 §2.6 + G4 §3.8.2 #10 + 43 entry 8 contexts (`bypass-detect`) 답습 |
300:### §5.2 Evidence Required (51 entry audit brief §6 답습)
302:| # | Evidence | 출처 |
304:| E-1 | Hermes native redaction Tier-1 42 catalog 적용 검증 | `agent/redact.py` 실행 evidence (R-4 답습) |
305:| E-2 | P1 facade RedactionFilter 적용 검증 | facade 진입점 evidence (TR-1 (d) carry-over 의존) |
306:| E-3 | log file canary inject + grep PASS evidence | Docker 격리 PoC (R-1 / R-4.1 답습) |
307:| E-4 | hash chain 검증 PoC PASS evidence | middle tampering 차단 PoC (Docker 격리) |
308:| E-5 | canonical JSON test corpus PASS (≥ 20 RFC 8785 reference) | `tests/canonical/` (G4 §4.4.2 답습) |
309:| E-6 | timestamp monotonicity 위반 차단 PoC | Docker 격리 (ADR-012 §3.4 답습) |
310:| E-7 | R-6 workflow 확장 step actual run PASS | GitHub Actions run ID + verdict PASS (43 entry 답습) |
311:| E-8 | 합의 보고서 commit | 본 (α) 합의 + (β) + (γ) + 실 구현 sub-cycle 별 |
312:| E-9 | 외부 LLM 응답 1+ (cross-vendor) | `docs/external-review/2026-05-28-mvp2-entry-codex-response.md` 등 |
321:| 2 | `g4_ledger_chain_verify_layer4_implementation` | G4 §4.4 Layer 4 | 동일 답습 |
343:| 4 | MVP-2 Implementation Evidence PASS *자동* 선언 | 실 구현 + (a)~(d) evidence + (e) 합의 APPROVE + 사용자 명시 (별도 합의) |
346:| 7 | GP-1 / GP-4 / GP-6 / G3 / G4 (Layer 4 외) 자동 진입 | MVP-3~MVP-5 영역 (별도 합의) |
348:| 9 | ADR 본문 갱신 자동 cross-reference 변경 | 별도 commit 영역 (R-S1 잠재 정정 영역 포함) |
359:3. **32 entry MVP-1 Implementation Evidence PASS 발효 합의** — 외부 LLM 1+ (codex via tmux cross-vendor) 답습
361:5. **ADR-011 §2.1 (e) + §2.4 T3 영역** — 큰 결정 = 외부 LLM 1+ + 사용자 명시
377:| ADR-011 §2.1 (a)~(e) 5조건 | `docs/decisions/ADR-011-means-vs-ends-redaction.md` |
391:| 3 | ADR-011 §2.1 (a)~(e) 5조건 답습 정확성 | 5조건 매트릭스 검증 |
392:| 4 | 두 영역 (GP-2 + G4 §4.4 Layer 4) 진입 자격 평가 | 두 영역별 평가 본문 |
394:| 6 | Rollback Trigger / Evidence 요건 평가 | RT-1~RT-7 / E-1~E-9 평가 |
395:| 7 | R-S1 잠재 risk 인식 (ADR-012 §2.3 line 182 Layer 4 vs Layer 5 혼동) | §1.3 자기진단 영역 cross-reference 답습 |
405:1. **(β) sub-수단 결정 cycle** — R-1/2/3/4/5 (GP-2) + L-1/2/3/4/5 (G4 §4.4 Layer 4) — 풀 3+1 합의
406:   - 본 (α) 권고 (51 brief 답습): GP-2 = R-4 (R-1+R-2+R-3 병행) / G4 §4.4 Layer 4 = L-4 (L-1+L-3 병행 MVP)
407:2. **(γ) 분리 영역 결정 cycle** — G4 §4.4 Layer 1+2 의존 영역 우선 진입 vs Layer 4 동시 진입 — 풀 3+1 합의
409:4. **MVP-2 Implementation Evidence PASS 발효 합의** — 실 구현 + (a)~(d) evidence + (e) 합의 APPROVE + 사용자 명시 (32 entry 답습 패턴)
410:5. **ADR 본문 cross-reference 갱신 별도 commit** — ADR-008 차단조건 #1 보조 cross-reference 추가 + ADR-012 §2.2 event enum 신규 등록 + ADR-011 §8.5 후속 작업에 GP-2 등록 (R-S1 정정 영역 포함)
422:- **ADR-011 §2.1 (a)~(e) 5조건** (수단/목적 분리, 모법) — `docs/decisions/ADR-011-means-vs-ends-redaction.md`
441:- `redaction-pattern-equivalence.md` (R-4 답습, ADR-011 §2.1 (a) 충족) — `docs/architecture/redaction-pattern-equivalence.md`
442:- `r4-1-trigger-extension-evidence.md` (R-4.1 PoC PASS, ADR-011 §2.1 (b) 충족) — `docs/phase0/r4-1-trigger-extension-evidence.md`
457:- ADR-011 §8.5 후속 작업에 GP-2 + G4 §4.4 Layer 4 등록
458:- **R-S1 정정 영역** (§1.3 ADR-012 §2.3 line 182 Layer 4 vs Layer 5 혼동 verbatim 재확인 + cross-reference 정정) — 본 (α) 합의 발효 후 사용자 명시 시 별도 cycle
471:| **P-4** | **⚠️ R-S1 유형 잠재 risk 1 — ADR-012 §2.3 line 182 verbatim 재확인 부족 — Layer 4 vs Layer 5 혼동 위험** | §1.3 G4 §4.4 Layer 4 항목 명시 + §4.3 trigger (4) 부분 발화 명시. 본 brief 발효 후 Reviewer 단독 verify 자격 (24 entry R-S1 답습 패턴, 권위 chain 다중 source 손상 확정 시 §9.5 별도 cycle 영역). 본 brief 의 Layer 4 정의 = G4 §4.4.1 line 649~653 답습 (Reviewer Read 확인 evidence 본 brief 작성 시점 read 완료) |
474:| **P-7** | 두 영역 통합 진행이 GP-2 / G4 §4.4 Layer 4 *각각* 의 영역 특성 무시 위험 | §2.1 + §2.2 각각 별도 분석 + §3 매트릭스 별도 컬럼 + §4.2 발효 시점 합의 형태 권고 각각 명시 |
480:**다음 단계**: 사용자 승인 → 외부 LLM 자격 옵션 결정 ((α) Claude tmux+codex 직접 호출 또는 (β) 사용자 직접 호출) → 외부 LLM 응답 capture → 풀 3+1 합의 (Agent A/B/C 3 병렬 독립 → Reviewer 통합 + R-S1 verify) → brief v1.1 1pass 흡수 보강 → SESSION + INDEX commit + push.

codex
## 검토자 / Vendor

- **검토자 역할**: 외부 LLM 검토자, cross-vendor blind review
- **응답 vendor**: **OpenAI / Codex CLI**
- **본 cycle 풀 3+1 Agent vendor**: **Anthropic Claude**
- **cross-vendor 충족 여부**: **충족**  
  OpenAI reviewer가 Anthropic Claude 작성/풀 합의 후보를 검토하므로, 헌법 제5조-2 Provider Liquidity 비협상 및 ADR-011 §2.4 T3 영역의 cross-vendor blind risk 차단 형식 요건은 충족합니다.

## 직접 검토한 working directory 자료

- `docs/phase0/mvp2-entry-brief.md`
- `docs/phase0/mvp2-entry-eligibility-audit-brief.md`
- `docs/review/3plus1-consensus-2026-05-28-mvp2-entry-eligibility-audit.md`
- `docs/phase0/mvp1-1.5th-reinforcement-entry-brief.md`
- `docs/architecture/implementation-runtime-roadmap-mvp1.md`
- `docs/architecture/governance-preconditions.md`
- `docs/architecture/provider-agnostic-memory-skill-design.md`
- `docs/decisions/ADR-011-means-vs-ends-redaction.md`
- `docs/decisions/ADR-012-evidence-ledger-protection.md`
- `docs/decisions/ADR-008-hermes-adoption-decision.md`
- `docs/constitution/PROJECT_CONSTITUTION.md`

## §0 총평

**판정: REVISE AS ENTRY BRIEF INPUT**

**BLOCKING 3건 / 권고 5건 / NOTE 3건**

본 brief v1은 전체적으로 “MVP-2 영역 진입 합의 input”의 형식, 금지 사항, sub-cycle 분리, Rollback/Evidence 후보를 충분히 담고 있습니다.

다만 entry brief input으로 쓰기 전, 아래 3개는 명확화가 필요합니다.

1. **ADR-011 §2.1 (a)~(e) 표현**이 원문 권위와 다릅니다.
2. **R-S1 Layer 4 충돌**은 잠재 risk가 아니라 실제 source divergence로 판정해야 합니다.
3. **(β) sub-수단 결정 분리**가 일부 문장에서 “(α) 내 흡수 가능”으로 남아 있어 본 cycle 한계와 충돌합니다.

따라서 현재 v1은 곧바로 APPROVE input으로 쓰기보다, v1.1에서 위 3개를 1pass 정정한 뒤 entry brief input으로 사용하는 것이 안전합니다.

## §1 BLOCKING

### R-1. ADR-011 §2.1 “(a)~(e) 5조건” 표현 정정 필요

**문제**

brief v1은 여러 곳에서 다음 표현을 사용합니다.

- `ADR-011 §2.1 (a)~(e) 5조건 모법`
- `ADR-011 §2.1 (e) + §2.4 T3 영역`
- `ADR-011 §2.1 (a)~(e) 5조건`

그러나 직접 확인한 ADR-011 원문은 다릅니다.

ADR-011 §2.1 원문은 다음과 같습니다.

> “대체 수단은 다음 4조건을 모두 충족할 때 기존 수단을 대체할 수 있다”

그리고 표는 다음 4개입니다.

- `(a) 동등 이상의 보안 결과`
- `(b) 격리 환경 PoC로 실증`
- `(c) ADR 권위로 명시`
- `(d) 자동 회귀 검증 경로 확보`

ADR-011 §2.1 line 61도 명시적으로 `(a)~(d) 4조건`이라고 합니다.

즉 **ADR-011 §2.1 자체에는 (e)가 없습니다.**

**평가**

24 entry 답습 패턴은 정확합니다.

- ADR-011 §2.1 = `(a)~(d) 4조건`
- 후속 합의/운영조건 = `(e) 합의 APPROVE`
- 합쳐서 operational matrix = 5조건

brief v1도 일부 문장에서는 이를 올바르게 씁니다.

예: brief §0.2 #5  
`ADR-011 §2.1 (a)~(d) + 합의 APPROVE 운영조건 (e) 5조건 매트릭스`

그러나 §1.1, §7.2, §9.1 등에서는 다시 “ADR-011 §2.1 (a)~(e)”라고 표기합니다.

이는 source attribution 정확성 문제입니다.

**권고 변경**

모든 표현을 아래 형태로 통일해야 합니다.

- 금지: `ADR-011 §2.1 (a)~(e) 5조건`
- 권장: `ADR-011 §2.1 (a)~(d) 4조건 + 후속 합의 APPROVE 운영조건 (e)`
- 권장: `operational 5-condition matrix = ADR-011 §2.1 (a)~(d) + consensus APPROVE (e)`

특히 brief §1.1 표의 ADR-011 행, §7.2 외부 LLM 입력 자료 표, §9.1 상위 권위 항목은 반드시 정정해야 합니다.

### R-2. R-S1 Layer 4 충돌은 “잠재 risk”가 아니라 실제 source divergence로 격상 필요

**문제**

brief §1.3은 다음 충돌을 인식합니다.

- ADR-012 §2.3 line 182: `Layer 4 — External anchor`
- G4 §4.4.1 line 649: `Layer 4 — CI 회귀 검증`

직접 확인 결과:

ADR-012 §2.3 line 182:

> `Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)`

G4 §4.4.1 line 649~653:

> `Layer 4 — CI 회귀 검증 (MANDATORY)`
> `Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증`
> `canonical JSON 위반 검출`
> `timestamp monotonicity 검증`
> `R-6 workflow ... 답습 확장`

따라서 동일한 “Layer 4” 라벨이 서로 다른 의미를 갖습니다.

추가로 ADR-012 §2.8 line 266~272에는 5 Layer 강제가 따로 존재합니다.

- Layer 1: Hash chain
- Layer 2: Git append-only
- Layer 3: pre-commit hook
- **Layer 4: CI 회귀 검증**
- **Layer 5: External anchor**

즉 현재 source chain은 다음과 같이 갈라져 있습니다.

- **ADR-012 §2.3**: 4-layer 모델, Layer 4 = External anchor
- **ADR-012 §2.8 + G4 §4.4.1**: 5-layer 모델, Layer 4 = CI 회귀 검증, Layer 5 = External anchor

brief v1은 이를 “미세 충돌”, “잠재 risk”로 낮춰 표현합니다. 하지만 직접 read 결과 이는 실제 권위 chain divergence입니다.

**평가**

brief가 G4 §4.4.1 line 649~653을 MVP-2 진입 대상 Layer 4 정의로 채택하는 것은 실무적으로 타당합니다.

다만 그 근거를 `ADR-012 §2.3`이라고 계속 부르면 source attribution이 손상됩니다.

정확한 framing은 다음이어야 합니다.

- MVP-2 진입 대상: **G4 §4.4.1 / ADR-012 §2.8 계열의 Layer 4 CI 회귀 검증**
- 충돌 source: **ADR-012 §2.3의 옛/축약 layer numbering**
- 후속 정정 대상: **ADR-012 §2.3 layer numbering cross-reference 정합화 또는 brief 내 한정 선언**

**권고 변경**

brief §1.3, §2.2.1, §4.3, §7.3, §10 P-4를 아래 의미로 정정해야 합니다.

- “R-S1 잠재 risk” → “R-S1 confirmed source divergence”
- “ADR-012 §2.3 line 182 = Layer 5 영역과 혼동 위험” → “ADR-012 §2.3 자체는 Layer 4를 External anchor로 명명하므로, G4 §4.4.1/ADR-012 §2.8의 5-layer 모델과 numbering divergence 발생”
- “본 cycle은 G4 §4.4.1 line 649~653 및 ADR-012 §2.8 line 266~272를 MVP-2 Layer 4 CI 회귀 검증의 직접 권위로 사용한다”
- “ADR-012 §2.3은 hash chain / append-only 원칙 권위로만 인용하고, Layer 4 numbering 권위로는 인용하지 않는다”

이 정정 없이는 entry brief input으로 사용 시 권위 chain 다중 source 손상 유형에 해당할 수 있습니다.

### R-3. (β) sub-수단 결정 분리 문구의 내부 충돌 정정 필요

**문제**

사용자 요청과 brief 다수 본문은 본 cycle을 다음처럼 정의합니다.

- 본 cycle = 영역 진입 한정
- sub-수단 결정 = (β) 별도 cycle
- 분리 영역 결정 = (γ) 별도 cycle
- 수단 결정 0건

하지만 brief §0.1에는 다음 문장이 남아 있습니다.

> `(β) sub-수단 결정 cycle ... 별도 합의 또는 (α) 內 흡수`

이는 현재 사용자 명시 조건과 충돌합니다.

이번 사용자 요청은 명확히 말합니다.

- `(β) sub-수단 결정 cycle 진입 자격 발효`
- `(γ) 분리 영역 결정 cycle 진입 자격 발효`
- 수단 결정 0
- threshold 고정 0
- 실 코드 0

즉 이번 cycle에서는 “(α) 내 흡수”가 허용되지 않습니다.

**평가**

brief 전체 방향은 분리 답습이 정확합니다.

예: §0.3 #11~#13, §1.3, §2.1.4, §2.2.4, §8.1은 모두 분리를 잘 유지합니다.

문제는 §0.1의 한 문장입니다.

entry brief input은 앞부분 scope 문구가 특히 중요하므로, 이 잔여 표현은 blocking으로 봅니다.

**권고 변경**

§0.1을 아래처럼 정정해야 합니다.

- 금지: `별도 합의 또는 (α) 內 흡수`
- 권장: `본 cycle에서는 (β) 별도 cycle로 분리한다. (α) 내 흡수는 본 cycle에서 채택하지 않는다.`
- 권장: `본 cycle 발효 효과는 (β)/(γ) 진입 자격 발효까지이며, 실제 (β)/(γ) 진입은 사용자 명시 후 별도 합의로만 가능하다.`

## §2 권고

### N-1. “Rollback Trigger 본문 채택”과 “후보” 표현을 더 선명히 분리 권고

brief §0.4는 발효 결과에 `Rollback Trigger 본문 채택 + Evidence 형식 본문 채택`을 둡니다.

§5 제목은 `본문 후보`입니다.

둘 다 의도는 이해됩니다.

다만 entry brief input 단계에서는 “후보를 본 cycle 합의로 채택한다”와 “구현 rollback policy를 발효한다”가 혼동될 수 있습니다.

권장 표현:

- `Rollback Trigger / Evidence 후보 문안을 본 cycle 합의 input으로 채택`
- `실제 runtime rollback enforcement 발효는 실 구현 sub-cycle 이후`
- `RT/E 문안은 MVP-2 Implementation Evidence PASS 합의 때 evidence checklist로 재검증`

### N-2. G4 Entry “3/8 + 사용자 영역”과 본 cycle 발효 후 효과를 더 정확히 표현 권고

51 entry audit 기준 G4 Layer 4는 `3/8 + 1 사용자 영역`입니다.

본 α 합의 발효 후 사용자 명시 조건은 충족되지만, 기술 gap 4개는 남습니다.

brief는 이를 대체로 잘 씁니다.

다만 `G4 §4.4 Layer 4 영역 진입 발효 자격`이라는 표현은 독자가 “Layer 4 구현 착수 가능”으로 읽을 수 있습니다.

권장 표현:

- `G4 §4.4 Layer 4 planning/decision track 진입 권한 발효`
- `Implementation track 진입은 (β)/(γ) 이후`
- `Layer 1/hash chain, canonical corpus, genesis hash 의존성은 unresolved gap으로 유지`

### N-3. RT-5의 `canonical_json_fallback 또는 BLOCK` 표현 보강 권고

ADR-012 §2.5는 fallback 사용 시 ledger entry와 review를 요구합니다.

canonical JSON “위반 검출”은 보통 BLOCK이어야 합니다.

fallback은 “위반”이라기보다 “primary unavailable 또는 fallback path 사용”에 가깝습니다.

권장 분리:

- `canonical JSON reference mismatch` → BLOCK
- `fallback canonicalizer used` → `canonical_json_fallback` ledger entry + reviewer/user review
- `primary JCS unavailable` → degraded path evidence 필요

### N-4. E-9 외부 LLM evidence의 agent/user attribution 명시 권고

ADR-012 §2.2 line 140은 `external_llm_received`를 `T2 + agent="user" 강제`로 둡니다.

E-9는 cross-vendor 응답 파일만 언급합니다.

권장 보강:

- `external_llm_received` ledger 사용 시 `agent="user"` 강제
- Codex 응답 raw capture path
- 입력 prompt와 검토 대상 commit/hash 포함
- vendor/model identifier 포함

### N-5. JSONL event enum 후보는 ADR-012 §2.2 갱신 전 “reserved candidate”로 낮춰 표현 권고

brief §5.3은 신규 enum 후보 3개를 제안합니다.

이는 적절하지만, ADR-012 §2.2 event enum은 권위 schema 영역입니다.

현재 cycle은 ADR 본문 갱신 0건이므로, `신규 등록 자격`이라는 말은 다소 강합니다.

권장 표현:

- `reserved candidate`
- `ADR-012 §2.2 amendment 또는 schema_version 갱신 전까지 non-authoritative`
- `실제 ledger write 금지`

## §3 NOTE

### NOTE-1. GP-2 진입 자격 평가는 대체로 정확합니다

governance-preconditions §4.4 직접 확인 결과 Entry 조건은 다음 3개입니다.

- R-4 pattern equivalence 작성 완료
- Hermes native redaction `agent/redact.py` 존재 확인
- 사용자 명시 GP-2 작업 진입 결정

brief의 `2/3 + 사용자 영역`, α 합의 후 `3/3` framing은 적절합니다.

Exit 조건도 governance-preconditions §4.5의 5조건과 일치합니다.

### NOTE-2. 24 entry 답습 차이 인식은 적절합니다

24 entry는 4 sub-수단의 진입 자격과 채택 결정 발효 자격을 더 강하게 결합했습니다.

이번 MVP-2 entry brief는 R-1~R-5와 L-1~L-5 조합이 크고, G4 Layer 1+2 의존성도 있어 분리하는 것이 더 안전합니다.

brief §1.3의 “24 entry와의 차이” 설명은 방향이 맞습니다.

단, R-3 blocking의 §0.1 잔여 문구만 제거하면 됩니다.

### NOTE-3. cross-vendor 요건은 형식상 충족합니다

현재 응답은 OpenAI/Codex CLI vendor에서 생성되었습니다.

본 cycle pool 3+1 vendor가 Anthropic Claude라는 사용자 명시와 충돌하지 않습니다.

따라서 외부 LLM 1+ cross-vendor input 자격은 형식상 충족합니다.

## §4 7 검토 기준별 평가

### 1. cross-vendor 충족 명시

**평가: PASS**

- 응답 vendor: OpenAI / Codex CLI
- cycle pool vendor: Anthropic Claude
- cross-vendor blind review 형식 충족

헌법 제5조-2는 다음을 말합니다.

> 모든 LLM/AI 도구 관련 결정은 Provider Liquidity 제약을 만족해야 한다

이번 응답은 단일 Anthropic 판단에 OpenAI 검토를 추가하므로 해당 취지에 부합합니다.

### 2. 본 brief v1 직접 읽기 evidence

**평가: PASS**

직접 확인한 brief v1의 주요 식별 evidence:

- §0.3: 27개 금지 사항
- §0.4: 발효 자격과 발효 결과 한계
- §1.3: 선차 변경 매트릭스
- §2.1: GP-2 진입 자격
- §2.2: G4 §4.4 Layer 4 진입 자격
- §3: ADR-011 5조건 매트릭스
- §5: RT-1~RT-7 / E-1~E-9
- §7.3: 외부 LLM 응답 자격 검증 7 기준
- §10 P-4: R-S1 잠재 risk 자기진단

brief §0.3 verbatim 식별:

> `본 brief 가 *하지 않는* 것`

brief §5.1 verbatim 식별:

> `RT-1 | Hermes native redaction 우회 검출`

brief §10 P-4 verbatim 식별:

> `ADR-012 §2.3 line 182 verbatim 재확인 부족 — Layer 4 vs Layer 5 혼동 위험`

직접 read evidence 기준은 충족합니다.

### 3. ADR-011 §2.1 (a)~(e) 5조건 답습 정확성

**평가: PARTIAL / BLOCKING R-1**

원문 ADR-011 §2.1은 `(a)~(d) 4조건`입니다.

직접 확인한 문구:

> `대체 수단은 다음 4조건을 모두 충족할 때 기존 수단을 대체할 수 있다`

표 항목은 (a)~(d)까지만 있습니다.

(e) 합의 APPROVE는 ADR-011 §2.1 원문 조건이 아니라, 후속 합의/운영조건으로 붙은 5번째 operational condition입니다.

brief가 일부는 정확히 씁니다.

- `ADR-011 §2.1 (a)~(d) + 합의 APPROVE 운영조건 (e)`

하지만 다수 위치에서 부정확하게 씁니다.

- `ADR-011 §2.1 (a)~(e)`

따라서 24 entry codex 답습 기준으로는 정정 필요입니다.

### 4. GP-2 + G4 §4.4 Layer 4 진입 자격 평가

**평가: GP-2 PASS / G4 PARTIAL WITH R-S1 BLOCKING**

**GP-2**

governance-preconditions §4.4 Entry 3조건:

> `R-4 pattern equivalence 작성 완료`
> `Hermes native redaction agent/redact.py 존재 확인`
> `사용자 명시 GP-2 작업 진입 결정`

brief의 `2/3 + 사용자 영역`, α 합의 후 `3/3`은 정확합니다.

governance-preconditions §4.5 Exit 5조건:

- (a) Hermes native + P1 facade 검증
- (b) log file canary Docker PoC
- (c) ADR-011 §2.3 + 본 §4 권위
- (d) R-6 workflow log canary step
- (e) 합의 APPROVE

brief가 이를 정확히 반영했습니다.

**G4 §4.4 Layer 4**

G4 §4.4.1 line 649~653은 다음입니다.

> `Layer 4 — CI 회귀 검증 (MANDATORY)`
> `Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증`
> `canonical JSON 위반 검출`
> `timestamp monotonicity 검증`
> `R-6 workflow ... 답습 확장`

brief의 G4 목표 정의는 이 문구와 일치합니다.

다만 ADR-012 §2.3 line 182는 다음입니다.

> `Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)`

따라서 “ADR-012 §2.3 + G4 §4.4.1”을 Layer 4 numbering 권위로 동시에 쓰면 충돌합니다.

정확한 근거 chain은 다음이어야 합니다.

- Layer 4 CI 정의: G4 §4.4.1 + ADR-012 §2.8
- Hash chain / append-only 원칙: ADR-012 §2.3
- timestamp monotonicity: ADR-012 §3.4
- prev_hash 실패 처리: ADR-012 §2.7

### 5. (β) sub-수단 결정 분리 답습 정확성

**평가: PARTIAL / BLOCKING R-3**

brief 대부분은 정확합니다.

- 본 cycle = 영역 진입 한정
- R-1~R-5 결정 = (β)
- L-1~L-5 결정 = (β)
- Layer 1+2 의존 vs Layer 4 동시 = (γ)
- 실 구현 = 후속 sub-cycle

그러나 §0.1의 `별도 합의 또는 (α) 內 흡수`는 현재 사용자 명시 조건과 충돌합니다.

이 문장만 정정하면 PASS입니다.

### 6. Rollback Trigger / Evidence 요건 평가

**평가: PASS WITH RECOMMENDATIONS**

RT-1~RT-7은 대체로 51 entry audit brief와 권위 문서를 잘 답습합니다.

- RT-1~RT-3: GP-2 redaction/evasion 영역
- RT-4~RT-6: hash chain / canonical JSON / timestamp 영역
- RT-7: R-6 workflow silent override

ADR-012 §2.7 직접 확인 결과 prev_hash 실패 처리는 다음을 요구합니다.

> `즉시 BLOCK`
> `기존 원본 JSONL 보존`
> `chain_violation_detected ledger entry`
> `사용자 명시 review 의무`
> `자동 revert 금지`

brief의 RT-4는 이 방향과 일치합니다.

E-1~E-9도 적절합니다.

다만 N-1~N-5의 표현 보강은 권고합니다.

### 7. R-S1 잠재 risk 검증

**평가: FAIL AS “POTENTIAL”; PASS AS “CONFIRMED DIVERGENCE”**

직접 read 결과, 충돌은 실제입니다.

ADR-012 §2.3 line 182:

> `Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)`

G4 §4.4.1 line 649:

> `Layer 4 — CI 회귀 검증 (MANDATORY)`

ADR-012 §2.8 line 271~272는 또 다음처럼 정리합니다.

> `Layer 4: CI 회귀 검증`
> `Layer 5: External anchor`

따라서 source chain은 다음 상태입니다.

- ADR-012 §2.3: 4-layer numbering
- ADR-012 §2.8: 5-layer numbering
- G4 §4.4.1: 5-layer numbering

brief가 이 divergence를 감지한 것은 좋습니다.

하지만 `potential`, `미세 충돌`, `혼동 위험`으로만 두는 것은 부족합니다.

entry brief input 전에는 confirmed R-S1로 격상하고, 본 cycle이 사용하는 Layer numbering 권위를 명시해야 합니다.

## §5 R-S1 잠재 risk 검증 결과

### §5.1 Verbatim 대조

**ADR-012 §2.3 line 165~182**

- `Layer 1 — Hash Chain (MANDATORY 모든 환경)`
- `Layer 2 — Git append-only branch (MANDATORY)`
- `Layer 3 — Signed commit (RECOMMENDED MVP, MANDATORY multi-host)`
- `Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)`

**G4 §4.4.1 line 649~653**

- `Layer 4 — CI 회귀 검증 (MANDATORY)`
- `Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증`
- `canonical JSON 위반 검출`
- `timestamp monotonicity 검증`
- `R-6 workflow ... 답습 확장`

**ADR-012 §2.8 line 266~272**

- `Layer 1: Hash chain`
- `Layer 2: Git append-only branch`
- `Layer 3: pre-commit hook`
- `Layer 4: CI 회귀 검증`
- `Layer 5: External anchor`

### §5.2 충돌 분석

동일 문서 ADR-012 안에서도 §2.3과 §2.8의 numbering이 다릅니다.

§2.3은 External anchor를 Layer 4로 둡니다.

§2.8은 External anchor를 Layer 5로 둡니다.

G4 §4.4.1은 §2.8과 같은 5-layer 모델을 따릅니다.

따라서 brief가 “G4 Layer 4 CI 회귀 검증”을 MVP-2 진입 대상으로 삼는 것은 가능합니다.

하지만 권위 인용은 아래처럼 제한해야 합니다.

- `G4 §4.4.1 line 649~653` = 직접 정의 권위
- `ADR-012 §2.8 line 266~272` = ADR 내부 5-layer 보강 권위
- `ADR-012 §2.3` = hash chain / append-only 원칙 권위, 단 Layer 4 numbering 권위로는 사용 금지

### §5.3 최종 R-S1 판정

**R-S1 = CONFIRMED**

유형:

- 권위 chain 다중 source divergence
- 동일 label “Layer 4”의 semantic collision
- ADR-012 §2.3과 G4 §4.4.1 간 source attribution 손상 위험

필수 정정:

1. brief v1.1에서 R-S1을 confirmed로 격상
2. MVP-2 진입 대상 Layer 4를 `G4 §4.4.1 / ADR-012 §2.8` 기반으로 한정
3. ADR-012 §2.3은 numbering 근거가 아니라 원칙 근거로만 인용
4. 후속 ADR-012 cross-reference 정정 cycle을 별도 사용자 명시 영역으로 유지

## 최종 판정

**REVISE AS ENTRY BRIEF INPUT**

현재 brief v1은 구조와 방향은 좋지만, entry brief input으로 사용하기 전 다음 3개를 반영해야 합니다.

- R-1: ADR-011 §2.1은 `(a)~(d)`, `(e)`는 후속 합의 운영조건으로 정정
- R-2: R-S1은 잠재 risk가 아니라 confirmed source divergence로 격상
- R-3: `(β) 별도 합의 또는 (α) 내 흡수` 잔여 문구 제거

이 3개가 v1.1에 반영되면, 본 brief는 **APPROVE WITH CONDITIONS** 또는 **APPROVE** input 후보로 격상 가능하다고 봅니다.
tokens used
133,364
## 검토자 / Vendor

- **검토자 역할**: 외부 LLM 검토자, cross-vendor blind review
- **응답 vendor**: **OpenAI / Codex CLI**
- **본 cycle 풀 3+1 Agent vendor**: **Anthropic Claude**
- **cross-vendor 충족 여부**: **충족**  
  OpenAI reviewer가 Anthropic Claude 작성/풀 합의 후보를 검토하므로, 헌법 제5조-2 Provider Liquidity 비협상 및 ADR-011 §2.4 T3 영역의 cross-vendor blind risk 차단 형식 요건은 충족합니다.

## 직접 검토한 working directory 자료

- `docs/phase0/mvp2-entry-brief.md`
- `docs/phase0/mvp2-entry-eligibility-audit-brief.md`
- `docs/review/3plus1-consensus-2026-05-28-mvp2-entry-eligibility-audit.md`
- `docs/phase0/mvp1-1.5th-reinforcement-entry-brief.md`
- `docs/architecture/implementation-runtime-roadmap-mvp1.md`
- `docs/architecture/governance-preconditions.md`
- `docs/architecture/provider-agnostic-memory-skill-design.md`
- `docs/decisions/ADR-011-means-vs-ends-redaction.md`
- `docs/decisions/ADR-012-evidence-ledger-protection.md`
- `docs/decisions/ADR-008-hermes-adoption-decision.md`
- `docs/constitution/PROJECT_CONSTITUTION.md`

## §0 총평

**판정: REVISE AS ENTRY BRIEF INPUT**

**BLOCKING 3건 / 권고 5건 / NOTE 3건**

본 brief v1은 전체적으로 “MVP-2 영역 진입 합의 input”의 형식, 금지 사항, sub-cycle 분리, Rollback/Evidence 후보를 충분히 담고 있습니다.

다만 entry brief input으로 쓰기 전, 아래 3개는 명확화가 필요합니다.

1. **ADR-011 §2.1 (a)~(e) 표현**이 원문 권위와 다릅니다.
2. **R-S1 Layer 4 충돌**은 잠재 risk가 아니라 실제 source divergence로 판정해야 합니다.
3. **(β) sub-수단 결정 분리**가 일부 문장에서 “(α) 내 흡수 가능”으로 남아 있어 본 cycle 한계와 충돌합니다.

따라서 현재 v1은 곧바로 APPROVE input으로 쓰기보다, v1.1에서 위 3개를 1pass 정정한 뒤 entry brief input으로 사용하는 것이 안전합니다.

## §1 BLOCKING

### R-1. ADR-011 §2.1 “(a)~(e) 5조건” 표현 정정 필요

**문제**

brief v1은 여러 곳에서 다음 표현을 사용합니다.

- `ADR-011 §2.1 (a)~(e) 5조건 모법`
- `ADR-011 §2.1 (e) + §2.4 T3 영역`
- `ADR-011 §2.1 (a)~(e) 5조건`

그러나 직접 확인한 ADR-011 원문은 다릅니다.

ADR-011 §2.1 원문은 다음과 같습니다.

> “대체 수단은 다음 4조건을 모두 충족할 때 기존 수단을 대체할 수 있다”

그리고 표는 다음 4개입니다.

- `(a) 동등 이상의 보안 결과`
- `(b) 격리 환경 PoC로 실증`
- `(c) ADR 권위로 명시`
- `(d) 자동 회귀 검증 경로 확보`

ADR-011 §2.1 line 61도 명시적으로 `(a)~(d) 4조건`이라고 합니다.

즉 **ADR-011 §2.1 자체에는 (e)가 없습니다.**

**평가**

24 entry 답습 패턴은 정확합니다.

- ADR-011 §2.1 = `(a)~(d) 4조건`
- 후속 합의/운영조건 = `(e) 합의 APPROVE`
- 합쳐서 operational matrix = 5조건

brief v1도 일부 문장에서는 이를 올바르게 씁니다.

예: brief §0.2 #5  
`ADR-011 §2.1 (a)~(d) + 합의 APPROVE 운영조건 (e) 5조건 매트릭스`

그러나 §1.1, §7.2, §9.1 등에서는 다시 “ADR-011 §2.1 (a)~(e)”라고 표기합니다.

이는 source attribution 정확성 문제입니다.

**권고 변경**

모든 표현을 아래 형태로 통일해야 합니다.

- 금지: `ADR-011 §2.1 (a)~(e) 5조건`
- 권장: `ADR-011 §2.1 (a)~(d) 4조건 + 후속 합의 APPROVE 운영조건 (e)`
- 권장: `operational 5-condition matrix = ADR-011 §2.1 (a)~(d) + consensus APPROVE (e)`

특히 brief §1.1 표의 ADR-011 행, §7.2 외부 LLM 입력 자료 표, §9.1 상위 권위 항목은 반드시 정정해야 합니다.

### R-2. R-S1 Layer 4 충돌은 “잠재 risk”가 아니라 실제 source divergence로 격상 필요

**문제**

brief §1.3은 다음 충돌을 인식합니다.

- ADR-012 §2.3 line 182: `Layer 4 — External anchor`
- G4 §4.4.1 line 649: `Layer 4 — CI 회귀 검증`

직접 확인 결과:

ADR-012 §2.3 line 182:

> `Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)`

G4 §4.4.1 line 649~653:

> `Layer 4 — CI 회귀 검증 (MANDATORY)`
> `Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증`
> `canonical JSON 위반 검출`
> `timestamp monotonicity 검증`
> `R-6 workflow ... 답습 확장`

따라서 동일한 “Layer 4” 라벨이 서로 다른 의미를 갖습니다.

추가로 ADR-012 §2.8 line 266~272에는 5 Layer 강제가 따로 존재합니다.

- Layer 1: Hash chain
- Layer 2: Git append-only
- Layer 3: pre-commit hook
- **Layer 4: CI 회귀 검증**
- **Layer 5: External anchor**

즉 현재 source chain은 다음과 같이 갈라져 있습니다.

- **ADR-012 §2.3**: 4-layer 모델, Layer 4 = External anchor
- **ADR-012 §2.8 + G4 §4.4.1**: 5-layer 모델, Layer 4 = CI 회귀 검증, Layer 5 = External anchor

brief v1은 이를 “미세 충돌”, “잠재 risk”로 낮춰 표현합니다. 하지만 직접 read 결과 이는 실제 권위 chain divergence입니다.

**평가**

brief가 G4 §4.4.1 line 649~653을 MVP-2 진입 대상 Layer 4 정의로 채택하는 것은 실무적으로 타당합니다.

다만 그 근거를 `ADR-012 §2.3`이라고 계속 부르면 source attribution이 손상됩니다.

정확한 framing은 다음이어야 합니다.

- MVP-2 진입 대상: **G4 §4.4.1 / ADR-012 §2.8 계열의 Layer 4 CI 회귀 검증**
- 충돌 source: **ADR-012 §2.3의 옛/축약 layer numbering**
- 후속 정정 대상: **ADR-012 §2.3 layer numbering cross-reference 정합화 또는 brief 내 한정 선언**

**권고 변경**

brief §1.3, §2.2.1, §4.3, §7.3, §10 P-4를 아래 의미로 정정해야 합니다.

- “R-S1 잠재 risk” → “R-S1 confirmed source divergence”
- “ADR-012 §2.3 line 182 = Layer 5 영역과 혼동 위험” → “ADR-012 §2.3 자체는 Layer 4를 External anchor로 명명하므로, G4 §4.4.1/ADR-012 §2.8의 5-layer 모델과 numbering divergence 발생”
- “본 cycle은 G4 §4.4.1 line 649~653 및 ADR-012 §2.8 line 266~272를 MVP-2 Layer 4 CI 회귀 검증의 직접 권위로 사용한다”
- “ADR-012 §2.3은 hash chain / append-only 원칙 권위로만 인용하고, Layer 4 numbering 권위로는 인용하지 않는다”

이 정정 없이는 entry brief input으로 사용 시 권위 chain 다중 source 손상 유형에 해당할 수 있습니다.

### R-3. (β) sub-수단 결정 분리 문구의 내부 충돌 정정 필요

**문제**

사용자 요청과 brief 다수 본문은 본 cycle을 다음처럼 정의합니다.

- 본 cycle = 영역 진입 한정
- sub-수단 결정 = (β) 별도 cycle
- 분리 영역 결정 = (γ) 별도 cycle
- 수단 결정 0건

하지만 brief §0.1에는 다음 문장이 남아 있습니다.

> `(β) sub-수단 결정 cycle ... 별도 합의 또는 (α) 內 흡수`

이는 현재 사용자 명시 조건과 충돌합니다.

이번 사용자 요청은 명확히 말합니다.

- `(β) sub-수단 결정 cycle 진입 자격 발효`
- `(γ) 분리 영역 결정 cycle 진입 자격 발효`
- 수단 결정 0
- threshold 고정 0
- 실 코드 0

즉 이번 cycle에서는 “(α) 내 흡수”가 허용되지 않습니다.

**평가**

brief 전체 방향은 분리 답습이 정확합니다.

예: §0.3 #11~#13, §1.3, §2.1.4, §2.2.4, §8.1은 모두 분리를 잘 유지합니다.

문제는 §0.1의 한 문장입니다.

entry brief input은 앞부분 scope 문구가 특히 중요하므로, 이 잔여 표현은 blocking으로 봅니다.

**권고 변경**

§0.1을 아래처럼 정정해야 합니다.

- 금지: `별도 합의 또는 (α) 內 흡수`
- 권장: `본 cycle에서는 (β) 별도 cycle로 분리한다. (α) 내 흡수는 본 cycle에서 채택하지 않는다.`
- 권장: `본 cycle 발효 효과는 (β)/(γ) 진입 자격 발효까지이며, 실제 (β)/(γ) 진입은 사용자 명시 후 별도 합의로만 가능하다.`

## §2 권고

### N-1. “Rollback Trigger 본문 채택”과 “후보” 표현을 더 선명히 분리 권고

brief §0.4는 발효 결과에 `Rollback Trigger 본문 채택 + Evidence 형식 본문 채택`을 둡니다.

§5 제목은 `본문 후보`입니다.

둘 다 의도는 이해됩니다.

다만 entry brief input 단계에서는 “후보를 본 cycle 합의로 채택한다”와 “구현 rollback policy를 발효한다”가 혼동될 수 있습니다.

권장 표현:

- `Rollback Trigger / Evidence 후보 문안을 본 cycle 합의 input으로 채택`
- `실제 runtime rollback enforcement 발효는 실 구현 sub-cycle 이후`
- `RT/E 문안은 MVP-2 Implementation Evidence PASS 합의 때 evidence checklist로 재검증`

### N-2. G4 Entry “3/8 + 사용자 영역”과 본 cycle 발효 후 효과를 더 정확히 표현 권고

51 entry audit 기준 G4 Layer 4는 `3/8 + 1 사용자 영역`입니다.

본 α 합의 발효 후 사용자 명시 조건은 충족되지만, 기술 gap 4개는 남습니다.

brief는 이를 대체로 잘 씁니다.

다만 `G4 §4.4 Layer 4 영역 진입 발효 자격`이라는 표현은 독자가 “Layer 4 구현 착수 가능”으로 읽을 수 있습니다.

권장 표현:

- `G4 §4.4 Layer 4 planning/decision track 진입 권한 발효`
- `Implementation track 진입은 (β)/(γ) 이후`
- `Layer 1/hash chain, canonical corpus, genesis hash 의존성은 unresolved gap으로 유지`

### N-3. RT-5의 `canonical_json_fallback 또는 BLOCK` 표현 보강 권고

ADR-012 §2.5는 fallback 사용 시 ledger entry와 review를 요구합니다.

canonical JSON “위반 검출”은 보통 BLOCK이어야 합니다.

fallback은 “위반”이라기보다 “primary unavailable 또는 fallback path 사용”에 가깝습니다.

권장 분리:

- `canonical JSON reference mismatch` → BLOCK
- `fallback canonicalizer used` → `canonical_json_fallback` ledger entry + reviewer/user review
- `primary JCS unavailable` → degraded path evidence 필요

### N-4. E-9 외부 LLM evidence의 agent/user attribution 명시 권고

ADR-012 §2.2 line 140은 `external_llm_received`를 `T2 + agent="user" 강제`로 둡니다.

E-9는 cross-vendor 응답 파일만 언급합니다.

권장 보강:

- `external_llm_received` ledger 사용 시 `agent="user"` 강제
- Codex 응답 raw capture path
- 입력 prompt와 검토 대상 commit/hash 포함
- vendor/model identifier 포함

### N-5. JSONL event enum 후보는 ADR-012 §2.2 갱신 전 “reserved candidate”로 낮춰 표현 권고

brief §5.3은 신규 enum 후보 3개를 제안합니다.

이는 적절하지만, ADR-012 §2.2 event enum은 권위 schema 영역입니다.

현재 cycle은 ADR 본문 갱신 0건이므로, `신규 등록 자격`이라는 말은 다소 강합니다.

권장 표현:

- `reserved candidate`
- `ADR-012 §2.2 amendment 또는 schema_version 갱신 전까지 non-authoritative`
- `실제 ledger write 금지`

## §3 NOTE

### NOTE-1. GP-2 진입 자격 평가는 대체로 정확합니다

governance-preconditions §4.4 직접 확인 결과 Entry 조건은 다음 3개입니다.

- R-4 pattern equivalence 작성 완료
- Hermes native redaction `agent/redact.py` 존재 확인
- 사용자 명시 GP-2 작업 진입 결정

brief의 `2/3 + 사용자 영역`, α 합의 후 `3/3` framing은 적절합니다.

Exit 조건도 governance-preconditions §4.5의 5조건과 일치합니다.

### NOTE-2. 24 entry 답습 차이 인식은 적절합니다

24 entry는 4 sub-수단의 진입 자격과 채택 결정 발효 자격을 더 강하게 결합했습니다.

이번 MVP-2 entry brief는 R-1~R-5와 L-1~L-5 조합이 크고, G4 Layer 1+2 의존성도 있어 분리하는 것이 더 안전합니다.

brief §1.3의 “24 entry와의 차이” 설명은 방향이 맞습니다.

단, R-3 blocking의 §0.1 잔여 문구만 제거하면 됩니다.

### NOTE-3. cross-vendor 요건은 형식상 충족합니다

현재 응답은 OpenAI/Codex CLI vendor에서 생성되었습니다.

본 cycle pool 3+1 vendor가 Anthropic Claude라는 사용자 명시와 충돌하지 않습니다.

따라서 외부 LLM 1+ cross-vendor input 자격은 형식상 충족합니다.

## §4 7 검토 기준별 평가

### 1. cross-vendor 충족 명시

**평가: PASS**

- 응답 vendor: OpenAI / Codex CLI
- cycle pool vendor: Anthropic Claude
- cross-vendor blind review 형식 충족

헌법 제5조-2는 다음을 말합니다.

> 모든 LLM/AI 도구 관련 결정은 Provider Liquidity 제약을 만족해야 한다

이번 응답은 단일 Anthropic 판단에 OpenAI 검토를 추가하므로 해당 취지에 부합합니다.

### 2. 본 brief v1 직접 읽기 evidence

**평가: PASS**

직접 확인한 brief v1의 주요 식별 evidence:

- §0.3: 27개 금지 사항
- §0.4: 발효 자격과 발효 결과 한계
- §1.3: 선차 변경 매트릭스
- §2.1: GP-2 진입 자격
- §2.2: G4 §4.4 Layer 4 진입 자격
- §3: ADR-011 5조건 매트릭스
- §5: RT-1~RT-7 / E-1~E-9
- §7.3: 외부 LLM 응답 자격 검증 7 기준
- §10 P-4: R-S1 잠재 risk 자기진단

brief §0.3 verbatim 식별:

> `본 brief 가 *하지 않는* 것`

brief §5.1 verbatim 식별:

> `RT-1 | Hermes native redaction 우회 검출`

brief §10 P-4 verbatim 식별:

> `ADR-012 §2.3 line 182 verbatim 재확인 부족 — Layer 4 vs Layer 5 혼동 위험`

직접 read evidence 기준은 충족합니다.

### 3. ADR-011 §2.1 (a)~(e) 5조건 답습 정확성

**평가: PARTIAL / BLOCKING R-1**

원문 ADR-011 §2.1은 `(a)~(d) 4조건`입니다.

직접 확인한 문구:

> `대체 수단은 다음 4조건을 모두 충족할 때 기존 수단을 대체할 수 있다`

표 항목은 (a)~(d)까지만 있습니다.

(e) 합의 APPROVE는 ADR-011 §2.1 원문 조건이 아니라, 후속 합의/운영조건으로 붙은 5번째 operational condition입니다.

brief가 일부는 정확히 씁니다.

- `ADR-011 §2.1 (a)~(d) + 합의 APPROVE 운영조건 (e)`

하지만 다수 위치에서 부정확하게 씁니다.

- `ADR-011 §2.1 (a)~(e)`

따라서 24 entry codex 답습 기준으로는 정정 필요입니다.

### 4. GP-2 + G4 §4.4 Layer 4 진입 자격 평가

**평가: GP-2 PASS / G4 PARTIAL WITH R-S1 BLOCKING**

**GP-2**

governance-preconditions §4.4 Entry 3조건:

> `R-4 pattern equivalence 작성 완료`
> `Hermes native redaction agent/redact.py 존재 확인`
> `사용자 명시 GP-2 작업 진입 결정`

brief의 `2/3 + 사용자 영역`, α 합의 후 `3/3`은 정확합니다.

governance-preconditions §4.5 Exit 5조건:

- (a) Hermes native + P1 facade 검증
- (b) log file canary Docker PoC
- (c) ADR-011 §2.3 + 본 §4 권위
- (d) R-6 workflow log canary step
- (e) 합의 APPROVE

brief가 이를 정확히 반영했습니다.

**G4 §4.4 Layer 4**

G4 §4.4.1 line 649~653은 다음입니다.

> `Layer 4 — CI 회귀 검증 (MANDATORY)`
> `Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증`
> `canonical JSON 위반 검출`
> `timestamp monotonicity 검증`
> `R-6 workflow ... 답습 확장`

brief의 G4 목표 정의는 이 문구와 일치합니다.

다만 ADR-012 §2.3 line 182는 다음입니다.

> `Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)`

따라서 “ADR-012 §2.3 + G4 §4.4.1”을 Layer 4 numbering 권위로 동시에 쓰면 충돌합니다.

정확한 근거 chain은 다음이어야 합니다.

- Layer 4 CI 정의: G4 §4.4.1 + ADR-012 §2.8
- Hash chain / append-only 원칙: ADR-012 §2.3
- timestamp monotonicity: ADR-012 §3.4
- prev_hash 실패 처리: ADR-012 §2.7

### 5. (β) sub-수단 결정 분리 답습 정확성

**평가: PARTIAL / BLOCKING R-3**

brief 대부분은 정확합니다.

- 본 cycle = 영역 진입 한정
- R-1~R-5 결정 = (β)
- L-1~L-5 결정 = (β)
- Layer 1+2 의존 vs Layer 4 동시 = (γ)
- 실 구현 = 후속 sub-cycle

그러나 §0.1의 `별도 합의 또는 (α) 內 흡수`는 현재 사용자 명시 조건과 충돌합니다.

이 문장만 정정하면 PASS입니다.

### 6. Rollback Trigger / Evidence 요건 평가

**평가: PASS WITH RECOMMENDATIONS**

RT-1~RT-7은 대체로 51 entry audit brief와 권위 문서를 잘 답습합니다.

- RT-1~RT-3: GP-2 redaction/evasion 영역
- RT-4~RT-6: hash chain / canonical JSON / timestamp 영역
- RT-7: R-6 workflow silent override

ADR-012 §2.7 직접 확인 결과 prev_hash 실패 처리는 다음을 요구합니다.

> `즉시 BLOCK`
> `기존 원본 JSONL 보존`
> `chain_violation_detected ledger entry`
> `사용자 명시 review 의무`
> `자동 revert 금지`

brief의 RT-4는 이 방향과 일치합니다.

E-1~E-9도 적절합니다.

다만 N-1~N-5의 표현 보강은 권고합니다.

### 7. R-S1 잠재 risk 검증

**평가: FAIL AS “POTENTIAL”; PASS AS “CONFIRMED DIVERGENCE”**

직접 read 결과, 충돌은 실제입니다.

ADR-012 §2.3 line 182:

> `Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)`

G4 §4.4.1 line 649:

> `Layer 4 — CI 회귀 검증 (MANDATORY)`

ADR-012 §2.8 line 271~272는 또 다음처럼 정리합니다.

> `Layer 4: CI 회귀 검증`
> `Layer 5: External anchor`

따라서 source chain은 다음 상태입니다.

- ADR-012 §2.3: 4-layer numbering
- ADR-012 §2.8: 5-layer numbering
- G4 §4.4.1: 5-layer numbering

brief가 이 divergence를 감지한 것은 좋습니다.

하지만 `potential`, `미세 충돌`, `혼동 위험`으로만 두는 것은 부족합니다.

entry brief input 전에는 confirmed R-S1로 격상하고, 본 cycle이 사용하는 Layer numbering 권위를 명시해야 합니다.

## §5 R-S1 잠재 risk 검증 결과

### §5.1 Verbatim 대조

**ADR-012 §2.3 line 165~182**

- `Layer 1 — Hash Chain (MANDATORY 모든 환경)`
- `Layer 2 — Git append-only branch (MANDATORY)`
- `Layer 3 — Signed commit (RECOMMENDED MVP, MANDATORY multi-host)`
- `Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)`

**G4 §4.4.1 line 649~653**

- `Layer 4 — CI 회귀 검증 (MANDATORY)`
- `Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증`
- `canonical JSON 위반 검출`
- `timestamp monotonicity 검증`
- `R-6 workflow ... 답습 확장`

**ADR-012 §2.8 line 266~272**

- `Layer 1: Hash chain`
- `Layer 2: Git append-only branch`
- `Layer 3: pre-commit hook`
- `Layer 4: CI 회귀 검증`
- `Layer 5: External anchor`

### §5.2 충돌 분석

동일 문서 ADR-012 안에서도 §2.3과 §2.8의 numbering이 다릅니다.

§2.3은 External anchor를 Layer 4로 둡니다.

§2.8은 External anchor를 Layer 5로 둡니다.

G4 §4.4.1은 §2.8과 같은 5-layer 모델을 따릅니다.

따라서 brief가 “G4 Layer 4 CI 회귀 검증”을 MVP-2 진입 대상으로 삼는 것은 가능합니다.

하지만 권위 인용은 아래처럼 제한해야 합니다.

- `G4 §4.4.1 line 649~653` = 직접 정의 권위
- `ADR-012 §2.8 line 266~272` = ADR 내부 5-layer 보강 권위
- `ADR-012 §2.3` = hash chain / append-only 원칙 권위, 단 Layer 4 numbering 권위로는 사용 금지

### §5.3 최종 R-S1 판정

**R-S1 = CONFIRMED**

유형:

- 권위 chain 다중 source divergence
- 동일 label “Layer 4”의 semantic collision
- ADR-012 §2.3과 G4 §4.4.1 간 source attribution 손상 위험

필수 정정:

1. brief v1.1에서 R-S1을 confirmed로 격상
2. MVP-2 진입 대상 Layer 4를 `G4 §4.4.1 / ADR-012 §2.8` 기반으로 한정
3. ADR-012 §2.3은 numbering 근거가 아니라 원칙 근거로만 인용
4. 후속 ADR-012 cross-reference 정정 cycle을 별도 사용자 명시 영역으로 유지

## 최종 판정

**REVISE AS ENTRY BRIEF INPUT**

현재 brief v1은 구조와 방향은 좋지만, entry brief input으로 사용하기 전 다음 3개를 반영해야 합니다.

- R-1: ADR-011 §2.1은 `(a)~(d)`, `(e)`는 후속 합의 운영조건으로 정정
- R-2: R-S1은 잠재 risk가 아니라 confirmed source divergence로 격상
- R-3: `(β) 별도 합의 또는 (α) 내 흡수` 잔여 문구 제거

이 3개가 v1.1에 반영되면, 본 brief는 **APPROVE WITH CONDITIONS** 또는 **APPROVE** input 후보로 격상 가능하다고 봅니다.
