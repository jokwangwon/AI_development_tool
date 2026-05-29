OpenAI Codex v0.128.0 (research preview)
--------
workdir: /home/delangi/문서/project/category/AI_development_tool
model: gpt-5.5
provider: openai
approval: never
sandbox: danger-full-access
reasoning effort: none
reasoning summaries: none
session id: 019e6ce2-9bf2-7fe2-80f7-fe090432dd87
--------
user
당신은 외부 LLM 검토자 (cross-vendor blind review)입니다. 응답 vendor = OpenAI (codex CLI), 본 cycle 풀 3+1 Agent vendor = Anthropic Claude. cross-vendor 충족 (헌법 5조-2).

## 본 cycle 개요

AI_development_tool 프로젝트. 본 cycle = **(β) sub-수단 결정 entry brief** (57 entry). 51 audit brief 가 식별한 R-1~R-5 (GP-2 송신 redaction) + L-1~L-5 (G4 §4.4 Layer 4 CI 회귀 검증) + W-A~E (workflow 통합 방식) 후보를 *결정* 하는 cycle. 실 구현 *직전* 마지막 합의.

선행 chain (모두 발효 완료): 51 진입 자격 audit (R/L 후보 식별) → 52 (α) MVP-2 진입 합의 (W-A~E 5 대안 확장) → 53 (γ) Layer 분리 4 대안 → 54 (γ-c) Layer 1+2+4 동시 채택 결정 → 55 Layer 1+2+4 통합 PASS 격상 진입 합의 (조건부 승인 조건 6).

본 cycle 발효 효과: R / L / W sub-수단 *결정 발효* + 후속 실 구현 sub-cycle 진입 자격.
본 cycle 발효 *하지 않는 것* (총 24 금지): 실 코드 0 / tools 본문 0 / workflow 본문 0 / denyNonFastForwards 활성화 0 / R-6 actual run 0 / 외부 library (pyjcs/rfc8785) 도입 결정 0 / Hermes import (R-1) 0 / facade real (R-2, TR-1) 0 / R-5 evasion 진입 0 / threshold 고정 0 / Layer 통합 PASS 발효 0 / MVP-2 PASS 발효 0 / Layer 3+5 진입 0 / R-S1 정정 0 / 자동 실 구현 진입 0.

## 검토 대상 (working directory 자료, codex 직접 read 의무)

PRIMARY:
- `docs/phase0/mvp2-beta-submeans-decision-brief.md` (v1, 본 brief, §0~§12)

직접 입력 자료 (51/52/55 선행):
- `docs/phase0/mvp2-entry-eligibility-audit-brief.md` (51 audit, R-1~R-5 §2.3 + L-1~L-5 §3.4 + W-A/B §4.2)
- `docs/phase0/mvp2-entry-brief.md` (52 (α) v1.1, W-A~E 5 대안 §2.3.2)
- `docs/phase0/mvp2-layer-124-pass-entry-brief.md` (55 v1.1, 조건부 승인 조건 6 §11.1 B-4 + (γ-c) 특화 의무 4 §1.2)
- `docs/phase0/mvp2-gamma-decision-brief.md` (54 (γ-c) 채택)

선행 권위:
- `docs/decisions/ADR-011-means-vs-ends-redaction.md` (§2.1 (a)~(e) 수단/목적 분리 모법)
- `docs/decisions/ADR-012-evidence-ledger-protection.md` (§2.1 의존성 PoC 재실행 + §2.3/§2.5/§2.7/§2.8/§3.4)
- `docs/architecture/governance-preconditions.md` (§4 GP-2)
- `docs/architecture/provider-agnostic-memory-skill-design.md` (§4.4 Layer 1~5)

실 repo PoC 시제 (filesystem 직접 verify 의무 — 본 brief 의 핵심 주장 검증):
- `tools/secret_scanner.py` (GP-2 scan-log redaction, R-3 시제 주장)
- `tools/jsonl_hash_chain.py` (Layer 1 genesis + 4 violation_type, L-1 시제 주장)
- `tools/canonical_json.py` (rfc8785 + jcs + jq fallback + cross-check, L-1 fallback 주장)
- `tests/canonical/` (72 files / 8 카테고리 주장 — 직접 count verify)
- `.github/workflows/` (secret-hygiene-egress-redaction.yml + g4-hash-chain.yml + history-anchor-verifier.yml + rewrite-defense.yml + r2-canary.yml — W "보존 우선" 주장 검증)
- `src/adapters/llm/facade.py` (R-2 placeholder 주장 verify)
- `agent/redact.py` (R-1 부재 주장 verify — 본 repo 內 부재여야 함)

## 본 brief 핵심 권고 (검증 대상)

1. **R 결정 = R-4 (defense-in-depth)** + R-3 우선 발효 (시제 충족) + R-1(Hermes upstream)/R-2(facade real, TR-1) = 결과 의무이나 구현 경로 별도 trajectory
2. **L 결정 = L-4 (L-1 stdlib + L-3 CI step)** + L-2/L-5 (외부 JCS library) 영구 분리 (ADR-012 §2.1 trigger)
3. **W 결정 = 보존 우선 (W-A(ii) 변형)** + W-E 보조 — 51 audit W-A 단일통합 권고 vs 실 repo 5+ workflow 분리 운영 tension → 기존 보존, 신규 통합/신설 0

## 요청 사항

1. **verdict**: APPROVE / APPROVE WITH CONDITIONS / REVISE / REJECT 중 1
2. **BLOCKING findings** (각각 근거 + 정정 방향): 본 brief 의 R/L/W 권고가 means-vs-ends (ADR-011) 정합한지, 실 repo 시제 주장이 정확한지, (γ-c) 특화 의무 4 정합한지, 조건부 승인 조건 6 매핑이 정확한지, scope 침입 (수단 결정 cycle 인데 실 구현/외부 library/Hermes import 침입) 0건인지
3. **권고 (non-blocking)**
4. **NOTE / 누락 영역**

filesystem 직접 read 로 본 brief 의 시제 충족 주장 (R-3/L-1/L-3 시제 + W 보존 + agent/redact.py 부재 + facade placeholder + tests/canonical 72 files)을 cross-check 하여 부정확/과장 발견 시 BLOCKING 으로 분류하십시오. 한국어 응답.

codex
검토 범위가 문서 권위와 실제 repo 시제 검증을 모두 포함하므로, 먼저 지정 파일과 파일시스템 상태를 병렬로 읽고 숫자/존재 주장부터 확인하겠습니다. 이후 brief 권고가 ADR 및 선행 조건과 충돌하는지 findings 중심으로 정리하겠습니다.
exec
/bin/bash -lc "sed -n '1,240p' docs/phase0/mvp2-entry-eligibility-audit-brief.md" in /home/delangi/문서/project/category/AI_development_tool
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

exec
/bin/bash -lc "sed -n '1,260p' docs/phase0/mvp2-beta-submeans-decision-brief.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
# (β) sub-수단 결정 entry brief (v1)

> **작성**: 2026-05-28 (57번째 entry 진입 cycle — 신규 세션)
>
> **scope**: MVP-2 영역 sub-수단 *결정* — R-1~R-5 (GP-2 송신 redaction) + L-1~L-5 (G4 §4.4 Layer 4 CI 회귀 검증) + W-A~E (workflow 통합 방식)
>
> **본 cycle = 큰 cycle** (실 구현 *직전* 마지막 합의, 풀 3+1 + 외부 LLM 1+ 권고, 수단별 차등)
>
> **본 cycle 발효 자격** = **풀 3+1 합의 + 외부 LLM 1+ 응답 입력 (cross-vendor) + 사용자 명시 결정**
>
> **본 cycle 발효 효과** = R / L / W sub-수단 *결정 발효* + 후속 실 구현 sub-cycle 진입 자격 (조건부 승인 조건 6 입력). 실 구현 (denyNonFastForwards 활성화 + R-6 actual run + evidence 수집) = 별도 sub-cycle (본 cycle = 수단 결정 한정)
>
> **선행 답습**: 51 audit brief (R/L 후보 식별) + 52 (α) entry brief v1.1 (W-A~E 5 대안 확장) + 53 (γ) Layer 분리 + 54 (γ-c) 채택 발효 + 55 Layer 1+2+4 통합 PASS 격상 진입 합의 (조건부 승인 조건 6)

---

## §0 본 brief 의 범위

### §0.1 본 brief 가 *하는* 것 (51 audit brief = "수단 결정 0" 과 *대비* — 본 cycle = 수단 *결정* cycle)

1. **R sub-수단 결정** (GP-2 송신 redaction) — R-1~R-5 中 채택 결정 권고 + 실 구현 매핑 (§2)
2. **L sub-수단 결정** (G4 §4.4 Layer 4 CI 회귀 검증) — L-1~L-5 中 채택 결정 권고 (§3)
3. **W 통합 방식 결정** (workflow 통합) — W-A~E 中 채택 결정 권고 (실 repo 현 상태 핵심 반영) (§4)
4. **통합 수단 결정 매트릭스 + 의존 관계** (R ↔ L ↔ W cross-dependency) (§5)
5. **합의 형태 = 풀 3+1 + 외부 LLM 1+ 정당화 + 승격 트리거 검증** (§6)
6. **수단 결정 발효 후 실 구현 sub-cycle 입력 (조건부 승인 조건 6 매핑 + Rollback Trigger / Evidence)** (§7)
7. 금지 사항 + 외부 LLM 응답 영역 + 다음 단계 + cross-reference + 자기진단 (§8~§12)

### §0.2 본 brief 가 *하지 않는* 것 (55 entry §0.3 답습 + 본 cycle 한계)

| # | 영역 | 위반 시점 |
|---|------|----------|
| 1 | 실 코드 / runtime code 구현 | 0건 (수단 *결정* ≠ 구현) |
| 2 | `tools/*.py` 본문 변경 (jsonl_hash_chain / canonical_json / secret_scanner 등) | 0건 (PoC 시제 답습 보존) |
| 3 | `.github/workflows/*.yml` 본문 변경 | 0건 (기존 workflow 보존) |
| 4 | `tests/canonical/` + `tests/fixtures/` 본문 변경 | 0건 (72 files 답습 보존) |
| 5 | **`git config receive.denyNonFastForwards true` 활성화 실행** | 0건 (실 구현 sub-cycle 영역) |
| 6 | R-6 workflow actual run 트리거 | 0건 (실 구현 sub-cycle) |
| 7 | ledger 첫 entry (genesis hash) 작성 | 0건 (실 구현 sub-cycle) |
| 8 | **외부 library (`pyjcs` / `rfc8785`) 도입 결정** | 0건 (L-2 / L-5 = 별도 cycle, ADR-012 §2.1 R-2 / R-4.1 PoC 자동 재실행 trigger 답습) |
| 9 | **Hermes upstream `agent/redact.py` 본 repo 內 import 결정** (R-1 구현 경로) | 0건 (별도 cycle, 52 entry R-A-1 답습) |
| 10 | **`adapters/llm/facade.py` placeholder → real** (R-2 구현 경로, TR-1) | 0건 (별도 trajectory, (d) carry-over) |
| 11 | base64 / URL-encoded / 압축 evasion 영역 진입 (R-5) | 0건 (MVP-2/3 분리, G3-4 답습) |
| 12 | threshold 고정 (catalog 규모 / monotonicity tolerance 등) | 0건 |
| 13 | Tier-2 / Tier-3 vendor catalog 본문 확장 | 0건 |
| 14 | Layer 1+2+4 통합 PASS *발효* | 0건 (55 entry = 진입 권한, 발효 = 실 구현 + evidence + 합의 후 별도) |
| 15 | MVP-2 Implementation Evidence PASS 발효 | 0건 |
| 16 | MVP-1 PASS 재선언 | 0건 (32 entry 답습 유지) |
| 17 | Operational Readiness PASS / Hermes PMO 격상 | 0건 |
| 18 | ADR / 헌법 / roadmap / governance / G4 / ADR-012 본문 갱신 | 0건 |
| 19 | Layer 3 (Signed commit) + Layer 5 (External anchor) 영역 진입 결정 | 0건 ((γ-c) "부분 답습" framing 영구 답습) |
| 20 | (γ-a/b/d) + (γ-e/f/g) 대안 재평가 | 0건 (54 entry (γ-c) 채택 영구 발효) |
| 21 | R-S1 cross-reference 정정 (ADR-012 §2.3 vs §2.8) | 0건 (별도 cycle, RT-γ-6 평가 한정) |
| 22 | branch protection contexts 자동 추가 | 0건 (사용자 admin scope 영역) |
| 23 | 자동 후속 실 구현 sub-cycle 진입 | 0건 (사용자 명시 의무) |
| 24 | 본 brief 자체 영구화 / 권위 chain 등재 | 0건 |

### §0.3 권위 답습 source

- **ADR-011 §2.1 (a)~(d) 4조건 모법 + (e) 후속 운영조건** (수단/목적 분리) — `docs/decisions/ADR-011-means-vs-ends-redaction.md`
- **51 audit brief §2.3 (R-1~R-5) + §3.4 (L-1~L-5) + §4.2 (W-A/B)** — `docs/phase0/mvp2-entry-eligibility-audit-brief.md`
- **52 (α) entry brief v1.1 §2.3.2 (W-A~E 5 대안)** — `docs/phase0/mvp2-entry-brief.md`
- **55 Layer 1+2+4 통합 PASS 격상 brief v1.1 §2.4 + §4.4 + §11.1 B-4 (조건부 승인 조건 6)** — `docs/phase0/mvp2-layer-124-pass-entry-brief.md`
- **54 (γ-c) 채택 decision brief §1.3 (특화 의무 4)** — `docs/phase0/mvp2-gamma-decision-brief.md`
- **governance-preconditions.md §4** (GP-2) + **provider-agnostic-memory-skill-design.md §4.4** (Layer 1~5)
- **ADR-012 §2.3 + §2.5 + §2.7 + §2.8 + §3.4** — `docs/decisions/ADR-012-evidence-ledger-protection.md`
- **본 cycle audit (read-only, 2026-05-28 신규 세션)** — 실 repo PoC 시제 현 상태 직접 verify

---

## §1 진입 컨텍스트 + 실 repo PoC 시제 현 상태 (본 cycle audit)

### §1.1 선행 권위 chain 답습 (55 → 54 → 53 → 52 → 51)

| 합의 / 권위 | 본 cycle 답습 영역 |
|----------|-----------------|
| 55 Layer 1+2+4 통합 PASS 격상 진입 합의 (`311ca3b`, 4 source APPROVE WITH CONDITIONS) | Layer 1+2+4 PASS 격상 *진입 권한* 발효 답습 + 조건부 승인 조건 6 (실 구현 sub-cycle 입력) |
| 54 (γ-c) 채택 결정 발효 (`895a77b`) | (γ-c) 특화 의무 4 영구 답습 (Layer subsection 강제 + "부분 답습" framing + 통합 동시 + RT-γ-6) |
| 53 (γ) Layer 분리 4 대안 평가 (`f5cf584`) | (γ-c) 1순위 + (γ-d) 모순 CONFIRMED + R-S1 5 source verify |
| 52 (α) MVP-2 진입 합의 entry brief (`c739c53`) | MVP-2 영역 진입 권한 발효 + **W-A~E 5 대안 확장 (B-5/B-7 흡수)** + Agent A filesystem 발견 (agent/ 부재 + G4 workflow 분리 운영) |
| 51 진입 자격 audit brief (`f7ac61d`) | **R-1~R-5 + L-1~L-5 후보 식별** (수단 결정 0) — 본 cycle = 51 후보 → 결정 |

### §1.2 실 repo PoC 시제 현 상태 (2026-05-28 본 cycle audit, filesystem direct)

⭐ **본 cycle 핵심 발견 = GP-2 + G4 양 영역 PoC 시제 광범위 존재 (55 entry audit 답습 + GP-2 측 신규 확인)**:

| 영역 | PoC 시제 현 상태 | 수단 매핑 |
|------|----------------|---------|
| **GP-2 CI 회귀 검증** | ✅ `secret-hygiene-egress-redaction.yml` (51791B, D-2 scan-log redaction_pass/fail + base64 known limitation) + `tools/secret_scanner.py` (16802B, `--mode scan-log` redaction 잔존 검출, Tier-1 42 + baseline 5 = 45 patterns) | **R-3 (log canary CI) 시제 충족** |
| GP-2 Hermes native | ❌ `agent/redact.py` 본 repo 부재 (Hermes upstream HEAD v0.12.0, 52 R-A-1 답습) | R-1 = upstream 영역 |
| GP-2 facade redaction | ⚠️ `src/adapters/llm/facade.py` = placeholder (TR-1 발화 시 real, (d) carry-over) | R-2 = 별도 trajectory |
| Layer 1 hash chain | ✅ `tools/jsonl_hash_chain.py` (14038B, genesis + 4 violation_type) + `g4-hash-chain.yml` (10652B) | **L-1 (stdlib) 시제 충족** |
| canonical JSON | ✅ `tools/canonical_json.py` (10055B, rfc8785 + jcs + jq -S -c fallback + cross-check mode) + `tests/canonical/` 72 files / 8 카테고리 | **L-1 fallback + cross-check 시제 충족** |
| Layer 2 history | ✅ `history-anchor-verifier.yml` (19094B) + `rewrite-defense.yml` (16454B) + tools | L-3 영역 시제 충족 |
| Layer 4 CI step | ✅ 4 G4 workflow 분리 운영 (g4-hash-chain + history-anchor-verifier + rewrite-defense + r2-canary) | **L-3 (R-6 step) 시제 충족** |
| Layer 2a denyNonFastForwards | ⚠️ **미설정** (local + global 0건, 55 §1.3 답습) | 실 구현 sub-cycle 활성화 |

→ ⭐ **핵심 함의**: R-3 (log canary CI) + L-1 (stdlib hash chain) + L-3 (R-6 step) = **모두 PoC 시제 *이미 충족***. 본 (β) cycle 의 수단 결정 = "신규 구현 수단 선택" 보다 **"기존 PoC 시제 → MANDATORY 채택 + PASS 격상 경로 확정"** 성격. R-1 (Hermes upstream) + R-2 (facade real) = 별도 trajectory 의존 (본 cycle = 결정 영역 명시, 구현 경로 결정 0).

### §1.3 (γ-c) 특화 의무 4 영구 답습 (54 entry §1.3, 본 cycle 적용)

| # | 의무 | 본 brief 답습 |
|---|------|-----------|
| 1 | PASS evidence template Layer 1/2/4 subsection 강제 | §5 통합 매트릭스 Layer 별 분리 + §7 evidence Layer subsection |
| 2 | "defense-in-depth 부분 답습" framing 영구 (Layer 3+5 = scope 외) | §0.2 #19 + §4 W 결정 시 Layer 3+5 진입 0 |
| 3 | Layer 1+2+4 통합 PASS evidence 동시 발효 | §5 통합 의존 + W 결정이 통합 동시 발효 저해 0 |
| 4 | RT-γ-6 R-S1 PASS 시점 선행/동시 정정 *평가* 의무 | §7 + §10 #5 답습 (정정 = 별도 cycle) |

---

## §2 R sub-수단 결정 (GP-2 송신 redaction)

### §2.1 후보 비교 (51 audit §2.3 답습 + 본 cycle audit 갱신)

| # | 수단 | 영역 | 본 repo 구현 상태 | 의존 | 등급 |
|---|------|----|----------------|----|----|
| **R-1** | Hermes native redaction (`agent/redact.py`) | 송신 직전 redaction | ❌ 본 repo 부재 (Hermes upstream v0.12.0) | Hermes import 결정 (별도 cycle) | MANDATORY (ADR-011 §2.3 #2) — *결과* 의무, 구현 경로 = upstream |
| **R-2** | P1 facade RedactionFilter | LLM API 진입점 redaction | ⚠️ facade placeholder | facade real (TR-1, (d) carry-over) | MANDATORY (single entry point) — 구현 경로 = TR-1 trajectory |
| **R-3** | log canary inject + grep CI step | CI 회귀 검증 | ✅ **시제 충족** (`secret-hygiene-egress-redaction.yml` + `secret_scanner.py --mode scan-log`) | 없음 (즉시 PASS 격상 가능) | MANDATORY ((d) 자동 회귀 경로) |
| **R-4** | R-1 + R-2 + R-3 병행 (defense-in-depth) | 다층 redaction | 부분 (R-3 충족, R-1/R-2 trajectory) | R-1 + R-2 의존 | **51 audit 권고** |
| **R-5** | base64 / URL-encoded / 압축 evasion | Hermes upstream R2-6 또는 facade 확장 | ❌ known limitation | MVP-2/3 분리 (G3-4) | **본 cycle 범위 외 (영구 분리)** |

### §2.2 R 결정 권고

⭐ **권고 R 결정 = R-4 (defense-in-depth 목적) 채택 + 구현 경로 차등 명시**:

1. **R-3 = MVP-2 PASS gating 수단** (CI 회귀 검증, 시제 충족 — 즉시 PASS 격상 경로). GP-2 의 자동 회귀 검증 경로 (ADR-011 §2.1 (d)) = R-3 가 단독 충족.
2. **R-1 (Hermes upstream) + R-2 (facade real) = *결과* 의무이나 구현 경로 = 별도 trajectory**. 본 cycle = R-1/R-2 를 R-4 defense-in-depth 의 *목표 수단* 으로 채택하되, **구현 경로 결정 (Hermes import / facade real) = 별도 cycle** 명시 (§0.2 #9 #10).
3. **R-5 = 영구 분리** (base64 evasion = MVP-2/3, G3-4 답습).

→ **means-vs-ends 정합 (ADR-011)**: GP-2 의 *ends* (secret 송신/로그 leak 0) = R-4 다층으로 달성. 본 repo 內 *즉시 발효 가능 means* = R-3 (CI). R-1/R-2 = ends 충족 *보조 means*, 구현 = cross-trajectory 의존. **MVP-2 PASS 시점 GP-2 (a)~(e) 충족 = R-3 actual run PASS + R-1/R-2 evidence 가용 시점 합산** (실 구현 sub-cycle 영역).

### §2.3 R 결정 시 trade-off

| 결정 | 장점 | 단점 / risk |
|------|----|----------|
| R-4 (권고) | defense-in-depth ends 충족 / R-3 즉시 발효 / 기존 시제 답습 | R-1/R-2 cross-trajectory 의존 → MVP-2 PASS 시점 GP-2 완전 충족이 Hermes import + facade real 에 부분 종속 (단, R-3 단독으로 (d) 자동 회귀 충족) |
| R-3 단독 | 즉시 발효 / 의존 0 | defense-in-depth 약화 (단일 layer) — ADR-011 §2.3 #2 R-1 MANDATORY 미충족 risk |
| R-1 우선 | Hermes native 정공 | Hermes import 결정 선행 의무 (본 cycle 범위 외) → MVP-2 진입 지연 |

→ **R-4 채택 + R-3 우선 발효 + R-1/R-2 cross-trajectory 의존 명시** 가 ceremony-inflation 차단 + 즉시 진전 + ends 충족 정합.

---

## §3 L sub-수단 결정 (G4 §4.4 Layer 4 CI 회귀 검증)

### §3.1 후보 비교 (51 audit §3.4 답습 + 본 cycle audit 갱신)

| # | 수단 | 영역 | Library | 본 repo 구현 상태 | 등급 |
|---|------|----|---------|----------------|----|
| **L-1** | Layer 1 hash chain Python stdlib 단독 (`hashlib.sha256` + `json.dumps(sort_keys, separators)`) | hash chain 검증 | stdlib | ✅ **시제 충족** (`jsonl_hash_chain.py` + `canonical_json.py` fallback) | fallback canonical, RFC 8785 동등성 test corpus 의무 (72 files 충족) |
| **L-2** | Layer 1 + RFC 8785 JCS Primary (`pyjcs` / `rfc8785` 외부 library) | hash chain + canonical | 외부 library 1+ | ⚠️ canonical_json.py 에 rfc8785/jcs import 시도 + jq fallback 이미 존재 (의존성 *결정* 0) | 의존성 추가 trigger (ADR-012 §2.1 R-2 / R-4.1 PoC 자동 재실행) |
| **L-3** | Layer 4 R-6 workflow step (canonical 위반 + prev_hash mismatch + timestamp monotonicity) | CI 회귀 | shell + Python stdlib | ✅ **시제 충족** (4 G4 workflow 분리 운영) | R-6 답습 확장 |
| **L-4** | L-1 + L-3 병행 (MVP 권고) | Layer 1+4 동시 | stdlib 단독 | ✅ 양쪽 시제 충족 | **51 audit 권고** |
| **L-5** | L-2 + L-3 병행 (정식 권고) | Layer 1+4 + JCS Primary | 외부 library 1+ | 부분 | 정식 채택 시점 (Operational Readiness 또는 별도 cycle) |

### §3.2 L 결정 권고

⭐ **권고 L 결정 = L-4 (L-1 stdlib + L-3 CI step) 채택**:

1. **L-1 (stdlib hash chain) = MVP 단계 정합** — 외부 의존성 0, `jsonl_hash_chain.py` + `canonical_json.py` (rfc8785 *시도* + jq fallback + cross-check mode) 시제 충족. RFC 8785 동등성 = `tests/canonical/` 72 files corpus 로 검증 (≥ 20 reference 충족).
2. **L-3 (R-6 step) = CI 회귀 검증** — 4 G4 workflow 분리 운영 시제 충족.
3. **L-2 / L-5 (외부 library JCS Primary) = 별도 cycle 영구 분리** — 외부 library (`pyjcs` / `rfc8785`) 도입 = ADR-012 §2.1 R-2 / R-4.1 PoC 자동 재실행 trigger 발화 (Provider Liquidity 와 무관하나 의존성 추가 거버넌스 발화). 단, **canonical_json.py 가 이미 rfc8785/jcs *조건부 import + fallback* 구조** → L-1 의 RFC 8785 정합성은 fallback 동등성으로 확보, 외부 library *강제 의존* 0.

→ **means-vs-ends 정합**: Layer 4 의 *ends* (ledger 무결성 자동 회귀 검증) = L-4 로 달성. stdlib 단독 (L-1) = "동등 이상 보안 결과" (ADR-011 §2.1 (a)) — RFC 8785 reference corpus 동등성으로 입증. 외부 library = MVP 단계 불필요 (L-5 = 정식 단계 deferred).

### §3.3 L 결정 시 trade-off

| 결정 | 장점 | 단점 / risk |
|------|----|----------|
| L-4 (권고) | 외부 의존 0 / 시제 충족 / Provider Liquidity·거버넌스 마찰 0 / 즉시 PASS 격상 | RFC 8785 strict 정합 = fallback 동등성 의존 (corpus 72 files 로 완화) |
| L-5 (외부 JCS) | RFC 8785 strict Primary | 외부 library 의존성 추가 → ADR-012 §2.1 PoC 자동 재실행 + 거버넌스 cycle 부담 (MVP 단계 과잉) |

---

## §4 W 통합 방식 결정 (workflow 통합) — 실 repo 현 상태 핵심

### §4.1 후보 비교 (52 entry §2.3.2 답습 + 본 cycle audit 현 상태)

⭐ **본 cycle 핵심 tension (52 entry B-5 답습)**: 51 audit §4.2 = "W-A 단일 R-6 통합" 권고. 그러나 **실 repo 는 이미 workflow 분리 운영** (g4-hash-chain.yml + history-anchor-verifier.yml + rewrite-defense.yml + r2-canary.yml + secret-hygiene-egress-redaction.yml). W-A "일괄 통합" = **기존 5+ workflow 병합 = 대규모 파괴적 변경**.

| # | 수단 | 영역 | 실 repo 현 상태 정합 | 비고 |
|---|------|----|------------------|----|
| **W-A** | 단일 R-6 확장 (GP-2 + G4 §4.4 Layer 4 통합) | 통합 | ⚠️ 3 sub-옵션: (i) 일괄 통합 = 파괴적 / (ii) 보존 + 중복 step 추가 / (iii) 분산 추가 | (i) 비권고 (기존 분리 운영 파괴) |
| **W-B** | 별도 workflow 2개 신설 (`secret-egress-redaction.yml` + `ledger-chain-verify.yml`) | 분리 | ⚠️ 기존 workflow 와 중복 신설 (ceremony-inflation) | 비권고 (기존 secret-hygiene + g4-hash-chain 중복) |
| **W-C** | 단계 분리 (GP-2 우선 진입 + G4 §4.4 Layer 4 후속 진입) | 시간 분리 | 합의 cycle 2회 부담 | (γ-c) 통합 동시 의무와 trade-off 검토 |
| **W-D** | roadmap.md §5.3 답습 별도 progression (그룹 D + 그룹 C 별도) | progression | roadmap 권위 답습 / 통합 효율 손실 | 검토 |
| **W-E** | pre-commit hook 활용 (CI workflow 외 보조) | dev 즉시 | CI 회귀 검증 ≠ pre-commit (CI 영역 필수) | **보조 동시 가능** (CI workflow 와 병행) |

### §4.2 W 결정 권고

⭐ **권고 W 결정 = "기존 workflow 보존 우선" (W-A(ii) 변형) + W-E 보조 병행**:

1. **기존 5+ workflow 보존** (g4-hash-chain.yml + history-anchor-verifier.yml + rewrite-defense.yml + r2-canary.yml + secret-hygiene-egress-redaction.yml) — 신규 통합 workflow 생성 0, 기존 파괴 0. 이는 W-A(ii) "보존 + 중복 step 추가" 의 *최소 변형* = "보존 + (필요 시) 누락 step 추가".
2. **Layer 4 CI 회귀 검증 (L-3) = 기존 G4 workflow 답습 확장** — g4-hash-chain.yml (Layer 1) + history-anchor-verifier.yml + rewrite-defense.yml (Layer 2) 이 이미 Layer 4 회귀 검증 역할 수행. 누락 영역 (예: timestamp monotonicity step / HISTORY_REWRITE enum fixture) = 기존 workflow 內 step 추가 (실 구현 sub-cycle).
3. **GP-2 (R-3) = 기존 secret-hygiene-egress-redaction.yml 답습** — D-2 scan-log redaction 검증 이미 운영. 신규 step 불필요 (또는 canary inject 보강 = 실 구현 sub-cycle).
4. **W-E (pre-commit) = 보조 병행** — dev 환경 즉시 검증 (CI 회귀와 병행, 대체 아님).
5. **W-A(i) 일괄 통합 + W-B 신설 = 비권고** (파괴적 / ceremony-inflation). **W-C 단계 분리 = 비권고** ((γ-c) 통합 동시 의무 3 와 trade-off — Layer 1+2+4 통합 동시 발효 의무가 GP-2 와 G4 의 *동시* 진행을 요구하지는 않으나, 55 entry 진입 권한이 통합 영역으로 발효되어 분리 cycle 2회 부담은 ceremony-inflation).

→ ⭐ **W 결정 핵심 = "기존 분산 구조 보존, 신규 통합/신설 0, 누락 step 만 기존 workflow 內 보강"**. 이는 51 audit W-A 권고의 *정신* (단일 R-6 spirit = ceremony-inflation 차단)을 *실 repo 현 상태* (이미 분산 운영)에 맞춰 정밀화한 것. **명칭상 W-A(ii) 채택이나 실질 = "보존 우선 minimal"**.

### §4.3 W 결정 시 (γ-c) 특화 의무 정합 확인

- 의무 2 ("부분 답습" framing): W 결정이 Layer 3 (Signed commit) + Layer 5 (External anchor) 진입 유발 0. (단, history-anchor-verifier.yml = Layer 5 External anchor PoC 시제 *이미 운영* — 55 B-2 답습. "보존" = PoC 시제 보존이지 Layer 5 *결정 영역 진입* 0).
- 의무 3 (통합 동시 발효): W "보존 우선" 이 Layer 1+2+4 통합 PASS evidence 동시 발효 저해 0 (기존 workflow 가 Layer 1+2 분담, Layer 4 = 회귀 검증 통합).

---

## §5 통합 수단 결정 매트릭스 + 의존 관계

### §5.1 R ↔ L ↔ W cross-dependency

| 수단 | 결정 권고 | 즉시 발효 가능 | cross-trajectory 의존 |
|------|--------|------------|-------------------|
| **R** | R-4 (R-3 우선 + R-1/R-2 결과 의무) | R-3 ✅ (시제 충족) | R-1 = Hermes import / R-2 = facade real (TR-1) |
| **L** | L-4 (L-1 stdlib + L-3 step) | ✅ (양쪽 시제 충족) | 없음 (L-5 외부 library = 별도) |
| **W** | 보존 우선 (W-A(ii) minimal) + W-E 보조 | ✅ (기존 workflow 보존) | 없음 |

### §5.2 통합 결정 발효 시 채택 영역 (본 cycle 합의 APPROVE 시점)

✅ **R-4 / L-4 / W 보존우선 sub-수단 *결정 발효*** (51 후보 → 결정)
✅ **후속 실 구현 sub-cycle 진입 자격 발효** (조건부 승인 조건 6 입력, §7)
✅ **R-3 + L-1 + L-3 = MVP-2 PASS gating 즉시 발효 가능 means 확정** (시제 충족)
✅ **R-1 / R-2 = 결과 의무 + cross-trajectory 구현 경로 명시** (별도 cycle)
✅ **L-2 / L-5 (외부 library) + R-5 (evasion) = 영구 분리 확정** (deferred)

### §5.3 미발효 영역 (deferred)

❌ 실 구현 자체 (denyNonFastForwards 활성화 / R-6 actual run / step 추가 / evidence 수집) = 실 구현 sub-cycle
❌ Hermes import (R-1) / facade real (R-2, TR-1) 구현 경로 결정 = 별도 cycle
❌ 외부 library (L-2/L-5) 도입 결정 = 별도 cycle
❌ Layer 1+2+4 통합 PASS 발효 = 실 구현 + evidence + 합의 후 별도
❌ MVP-2 Implementation Evidence PASS 발효 = Layer 통합 PASS + GP-2 PASS + 통합 합의 후 별도

---

## §6 합의 형태 + 풀 3+1 승격 트리거 검증

### §6.1 본 cycle 합의 형태 = 풀 3+1 + 외부 LLM 1+ (권고)

**정당화 출처**:
1. 55 entry §8 #1 "(β) sub-수단 결정 cycle — R-1~R-5 + L-1~L-5 + W-A~E — 풀 3+1" 직접 답습
2. 56 entry 다음 세션 가이드 #1 "(β) sub-수단 결정 cycle … 풀 3+1 (수단별 차등) … 1순위 (실 구현 선행 의무)"
3. 큰 결정 (수단 *결정* = ADR-011 §2.1 (e) + §2.4 T3 영역, audit/52/55 "수단 결정 0" 과 대비)
4. 헌법 5조-2 Provider Liquidity (cross-vendor 의무) — 단 L-2/L-5 외부 library *결정 0* 이므로 Provider Liquidity 직접 충돌 0

### §6.2 7 풀 3+1 승격 트리거 검증

| # | trigger | 본 cycle 발화 | 근거 |
|---|---------|---------|------|
| 1 | 큰 결정 (sub-수단 *결정* / threshold 고정) | ✅ **발화** | R-4 / L-4 / W 수단 *결정* = 실 구현 직전 마지막 합의 |
| 2 | 아키텍처 / SDD / 보안 본문 변경 | ❌ 미발화 | brief = phase0 신규 1 파일, 본문 변경 0 |
| 3 | ADR 본문 변경 | ❌ 미발화 | ADR 본문 0 |
| 4 | 권위 chain 다중 source 손상 위험 | ⚠️ **부분 발화** | R-S1 후행 영향 (RT-γ-6, 평가 한정) — 정정 = 별도 cycle |
| 5 | 외부 LLM 응답 통합 필요성 | ✅ **발화** | 큰 결정 + cross-vendor 의무 (55 답습) |
| 6 | Tier-2/3 catalog 자동 확장 | ❌ 미발화 | §0.2 #13 금지 |
| 7 | Hermes PMO 격상 | ❌ 미발화 | §0.2 #17 금지 |

→ **2/7 발화 + 1 부분 발화 → 풀 3+1 + 외부 LLM 1+ 합의 적격**.


exec
/bin/bash -lc "sed -n '1,220p' docs/phase0/mvp2-entry-brief.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
# MVP-2 진입 합의 entry brief (v1.1)

> **작성**: 2026-05-28 (52번째 entry 진입 cycle)
>
> **v1 → v1.1 갱신**: 풀 3+1 + 외부 LLM 1+ (codex cross-vendor) 통합 합의 (`docs/review/3plus1-consensus-2026-05-28-mvp2-entry.md`) BLOCKING 7 + 권고 13 1pass 흡수 (별도 v2 cycle 0, ceremony-inflation 차단 답습). §11 v1.1 보강 매트릭스 추가.
>
> **scope**: MVP-2 영역 (G2 GP-2 송신 redaction + G4 §4.4 Layer 4 CI 회귀 검증) 본격 진입 합의
>
> **본 cycle = 큰 cycle** — 24 entry `mvp1-1.5th-reinforcement-entry-brief.md` 답습 형식 (entry brief = 진입 권한 발효 + 후속 sub-cycle 진입 자격 발효)
>
> **본 cycle 발효 자격** = **풀 3+1 합의 + 외부 LLM 1+ 응답 입력 (cross-vendor) + 사용자 명시 결정** 3 조건 모두 충족 시점
>
> **본 cycle 발효 효과** = MVP-2 영역 진입 권한 발효 + (β) sub-수단 결정 cycle 진입 자격 발효 + (γ) 분리 영역 결정 cycle 진입 자격 발효 (수단 결정 / threshold 고정 / 실 코드 / Rollback Trigger 구현 발효 / Evidence 구현 발효 = 후속 별도 cycle)

---

## §0 본 brief 의 범위

### §0.1 사용자 진입 명령 답습 (carry-over from 51 entry, commit `f7ac61d`)

51 entry `mvp2-entry-eligibility-audit-brief.md` §9 다음 단계:
- **(α) MVP-2 진입 합의 entry brief 작성** (24 entry MVP-1 1.5차 보강 entry brief 답습) — 풀 3+1 + 외부 LLM 1+ (cross-vendor 의무, 사용자 영역)
- **(β) sub-수단 결정 cycle** — R-1/2/3/4/5 (GP-2) + L-1/2/3/4/5 (G4 §4.4 Layer 4) — **별도 합의 (본 cycle 內 흡수 0).** 본 cycle 발효 효과는 (β)/(γ) 진입 자격 발효까지이며, 실제 (β)/(γ) 진입은 사용자 명시 후 별도 합의로만 가능 ⭐ (B-3 흡수)
- (γ) 분리 영역 결정 — G4 §4.4 Layer 1+2 의존 영역 우선 진입 vs Layer 4 동시 진입

본 (α) cycle 진입 사용자 명시 (2026-05-28, 51 entry commit 후) — "4번으로 진행". 본 brief = (α) 영역 한정. (β) + (γ) = 별도 cycle (본 cycle 발효 후 사용자 명시 시점 진입).

### §0.2 본 brief 가 *하는* 것

1. **MVP-2 영역 정의 답습** — 51 entry audit brief §1.3 (GP-2 송신 redaction + G4 §4.4 Layer 4 CI 회귀 검증) 직접 답습 (§1)
2. **51 entry audit brief 답습 cross-check** — 진입 자격 매트릭스 (GP-2 Entry 2/3 + Exit 2.5/5 / G4 §4.4 Layer 4 Entry 3/8 + Exit 1/5) 정합성 검증 (§2)
3. **선행 권위 답습** — 32 entry MVP-1 Implementation Evidence PASS *완전 발효 (α)* + roadmap-mvp1 §1.2 (3-layer PASS) + §1.3 (GP-2 = MVP-2 분리 사유) + **ADR-011 §2.1 (a)~(d) 4조건 모법 + (e) 합의 APPROVE 후속 운영조건 (§3 또는 governance §4.5 Exit)** (B-2 흡수) (§1.1)
4. **선차 변경 매트릭스** — 선행 권위 (roadmap-mvp1 / governance-preconditions §4.5 / G4 §4.4 / ADR-012 §2.3 / roadmap.md §5.4 그룹 C+D) vs 본 cycle 결정 사이의 *변경 차이* 명시 (§1.3 ~ 본 brief 핵심 framing)
5. **두 영역 *진입 자격* 분석** — **ADR-011 §2.1 (a)~(d) 4조건 모법 + (e) 합의 APPROVE 후속 운영조건** 5조건 매트릭스 (§3) (B-2 흡수)
6. **본 cycle 합의 형태 = 풀 3+1 + 외부 LLM 1+ *정당화*** (carry-over 답습 + roadmap-mvp1 §1.3 답습) (§4.1)
7. **두 영역 *발효 시점* 합의 형태 권고** (선행 권위 답습) (§4.2)
8. **7 풀 3+1 승격 트리거 *발화 검증*** (본 cycle 자체 ↔ 두 영역별) (§4.3)
9. **Rollback Trigger / Evidence *후보* 본문** (구현 발효 ≠ 본 합의, 별도 sub-cycle) (§5) (N-1 흡수)
10. **외부 LLM 응답 요구 *입력 자료* 정의 + *응답 자격 검증 기준*** (사용자 준비 영역) (§7)
11. **본 cycle 합의 발효 후 (β) sub-수단 결정 cycle 진입 권한 + (γ) 분리 영역 결정 cycle 진입 권한 발효 자격 명문** (§8)

### §0.3 본 brief 가 *하지 않는* 것 (사용자 명시 답습 + 본 brief 영역 한계)

| # | 영역 | 위반 시점 |
|---|------|----------|
| 1 | 실 코드 / runtime code 구현 | 0건 (Hermes native redaction / P1 facade RedactionFilter / R-6 workflow 확장 / JSONL hash chain verify 본문 모두 0건) |
| 2 | `agent/redact.py` 본문 변경 | 0건 (**본 repo 內 ≠ 존재. Hermes upstream `/tmp/hermes-phase0/hermes-agent/agent/redact.py` 401 LOC**, B-4 흡수) |
| 3 | P1 facade RedactionFilter 본문 변경 | 0건 |
| 4 | `.github/workflows/r2-canary.yml` 본문 변경 | 0건 |
| 5 | `tools/jsonl_hash_chain.py` / `tools/canonical_json.py` / `tests/canonical/` 본문 변경 | 0건 (**실 repo 內 PoC 시제 *이미 운영 중*** — 본 cycle = 진입 권한 한정, 변경 0건, B-6 흡수) |
| 6 | ledger 첫 entry (genesis hash) 작성 | 0건 (PoC 시제 답습) |
| 7 | 외부 library (`pyjcs` / `rfc8785` / `inotify-tools`) 설치 / 도입 | 0건 (L-5 별도 cycle, ADR-012 §2.1 R-2 / R-4.1 PoC 자동 재실행 trigger) |
| 8 | Tier-2 / Tier-3 vendor catalog 본문 확장 | 0건 |
| 9 | threshold *고정* (canary FP/FN/monotonicity tolerance 등) | 0건 |
| 10 | **GP-2 sub-수단 결정** (R-1 / R-2 / R-3 / R-4 / R-5 中 채택) | 0건 ((β) 별도 cycle) |
| 11 | **G4 §4.4 Layer 4 sub-수단 결정** (L-1 / L-2 / L-3 / L-4 / L-5 中 채택) | 0건 ((β) 별도 cycle) |
| 12 | **G4 §4.4 Layer 4 분리 영역 결정** (Layer 1+2 의존 영역 우선 vs Layer 4 동시) | 0건 ((γ) 별도 cycle) |
| 13 | **MVP-1 PASS *재선언*** | 0건 (32 entry 답습 그대로 유지) |
| 14 | **MVP-2 Implementation Evidence PASS *발효*** | 0건 (다층 분리 — (α) 진입 → (β) sub-수단 → 실 구현 → Implementation Evidence PASS 합의) |
| 15 | **Operational Readiness PASS (Layer 3)** | 0건 |
| 16 | **Hermes PMO 격상** | 0건 |
| 17 | 외부 LLM 호출 자동 진입 (Claude 영역) | 0건 (사용자 명시 또는 (α) tmux+codex 자격 답습) |
| 18 | ADR 본문 갱신 (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012) | 0건 (cross-reference 한정도 0건 — 본 brief 발효 후 별도 commit 영역) |
| 19 | 헌법 본문 갱신 (`PROJECT_CONSTITUTION.md`) | 0건 |
| 20 | roadmap-mvp1 §1~§8 본문 변경 | 0건 |
| 21 | governance-preconditions.md §4 본문 변경 | 0건 |
| 22 | provider-agnostic-memory-skill-design.md §4.4 본문 변경 | 0건 |
| 23 | `src/adapters/llm/facade.py` placeholder → real 본문 (TR-1) | 0건 (별도 trajectory, (d) carry-over) |
| 24 | G4 §4.4 Layer 1 / Layer 2 / Layer 3 / Layer 5 영역 진입 자동 결정 | 0건 |
| 25 | GP-1 / GP-4 / GP-6 / G3 / G4 (Layer 4 외) 영역 진입 자동 결정 | 0건 (MVP-3 ~ MVP-5 영역) |
| 26 | **Rollback Trigger / Evidence *구현 발효*** | 0건 (본 cycle = *후보 채택* 한정, 구현 발효 = 별도 sub-cycle, N-1 흡수) |
| 27 | **R-S1 cross-reference 정정 cycle 자동 진입** | 0건 (별도 사용자 명시 영역, §4.4 답습) |
| 28 | 51 audit brief carry-over 결함 정정 자동 진입 | 0건 (별도 cross-reference 정정 cycle) |
| 29 | 본 brief *자체* 영구화 / 권위 chain 등재 | 0건 (본 brief = 본 cycle 합의 input 한정) |

### §0.4 본 brief 의 권위 한계

- ✅ 본 brief 발효 자격 = **풀 3+1 합의 + 외부 LLM 1+ 응답 입력 (cross-vendor) + 사용자 명시 결정** 3 조건 모두 충족 시점
- ✅ 본 brief 발효 결과 = **MVP-2 영역 진입 권한 발효** + (β) sub-수단 결정 cycle 진입 자격 발효 + (γ) 분리 영역 결정 cycle 진입 자격 발효 + **Rollback Trigger 본문 *후보 채택*** + **Evidence 형식 본문 *후보 채택*** (N-1 흡수 — 구현 발효 ≠ 본 합의)
- ❌ 본 brief 자체에서 sub-수단 *결정* 0건 (본 brief = entry input, sub-수단 결정 자격은 (β) 별도 cycle)
- ❌ 본 brief 자체에서 threshold *고정* 0건 (후보 한정)
- ❌ 본 brief 자체에서 실 구현 0건 (별도 sub-cycle)
- ❌ 본 brief 자체에서 MVP-2 Implementation Evidence PASS 발효 0건
- ❌ 본 brief 자체에서 **ADR-011 §2.1 (a)~(d) 4조건 자동 충족 선언 0건** (본 cycle = 진입 자격, 충족 evidence = 실 구현 sub-cycle 영역, B-2 흡수)
- ⚠️ 본 brief 합의 후 *자동 sub-수단 결정 / 실 구현 진입 금지* — 사용자 명시 결정 의무

---

## §1 진입 컨텍스트 답습

### §1.1 선행 권위 답습 (32 entry + 51 entry + roadmap-mvp1 §1.3 + 헌법 + ADR-011 §2.1 + §3)

| 합의 / 권위 | 일자 | 판정 / 본문 | 본 cycle 답습 영역 |
|----------|------|------------|-----------------|
| `3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md` (32 entry) | 2026-05-27 | ✅ **APPROVE WITH CONDITIONS** (풀 3+1 + 외부 LLM 1+) — MVP-1 Implementation Evidence PASS *완전 발효 (α)* | MVP-1 PASS 답습 그대로 유지 (재선언 0). MVP-2 = "Layer 2 Implementation Evidence PASS *2차*" 영역 답습 (roadmap-mvp1 §1.2 line 90 "MVP-2 ~ MVP-5 = GP-2 / GP-4 / GP-6 / G3 / G4 의 본 PASS 단계"). |
| `3plus1-consensus-2026-05-28-mvp2-entry-eligibility-audit.md` (51 entry) | 2026-05-28 | ✅ **APPROVE** (Reviewer-only 단축) — `mvp2-entry-eligibility-audit-brief.md` v1 audit 권위 발효 | 본 (α) brief 의 **직접 입력 자료**. 51 entry audit = "MVP-2 영역 진입 자격 평가 한정", 본 (α) = "MVP-2 영역 진입 합의" (한 단계 격상). ⚠️ 51 audit brief 자체에 carry-over 결함 (`agent/redact.py` "✅ 충족" 표기 = 본 repo 內 부재) — B-4 답습 framing 정정 영역. |
| `implementation-runtime-roadmap-mvp1.md §1.3` | 2026-05-12 (APPROVED 2026-05-27) | 본문 line 101~107 = "GP-2 = MVP-1 vs MVP-2 분리 사유 (C-7 답습)" — "*시점* 분리이지 *영구 제외* 아님" | 본 cycle = GP-2 시점 진입 자격 발효 (분리 *해제*). |
| `implementation-runtime-roadmap.md §6` | 2026-05-09 (APPROVED) | 그룹 D (Order 4+5): G2 GP-3 + G2 GP-2. GP-3 = MVP-1 완료, **GP-2 잔존**. 그룹 C (Order 3 tie): G4 JSONL hash chain + JCS + Round-trip PoC | 본 cycle = 그룹 D 잔존 GP-2 진입 + 그룹 C G4 §4.4 Layer 4 진입 통합. **roadmap.md §5.4 = "단축 합의 + PoC evidence" 권고 vs 본 cycle = "풀 3+1 + 외부 LLM 1+" 격상** (B-7 흡수, §1.3 항목 5 답습) |
| `PROJECT_CONSTITUTION.md 제8조 (보안)` | 모법 | 보안 = 본질, 수단 ≠ 본질 (ADR-011 §2.1 답습) | GP-2 송신 redaction + G4 §4.4 Layer 4 evidence 무결성 = **헌법 8조 본질 충족 보조 영역** (DB INSERT 차단 = GP-1 본질 책임). 본 cycle = 보조 영역 진입 권한 발효 (N-9 흡수) |
| `PROJECT_CONSTITUTION.md 제5조-2 (Provider Liquidity 비협상)` | 모법 | LLM/AI 도구 결정 = Provider Liquidity 제약 만족 의무 | GP-2 R-1~R-5 + G4 §4.4 L-1~L-5 sub-수단 = **Provider Liquidity 자격 평가 영역** ((β) cycle 시점 평가, 본 cycle = 영역 진입 자격 한정, N-10 흡수) |
| `ADR-011 §2.1` | 2026-05-06 | **본문 line 52~60 verbatim = (a)~(d) 4조건 모법**. "대체 수단은 다음 4조건을 모두 충족할 때 기존 수단을 대체할 수 있다." (B-2 흡수) | 본 cycle = (a)~(d) 4조건 답습. |
| `ADR-011 §3` (후속 권위) + `governance-preconditions §4.5 Exit` (line 455) | 2026-05-06 ~ 2026-05-12 | **(e) 합의 APPROVE = 후속 운영조건 (별도 layer)**. governance §4.5 Exit 표 line 455 = "(e) 합의 APPROVE \| 단축 또는 풀 3+1 합의" | 본 cycle = (e) 후속 운영조건 답습 (본 (α) 합의 = (e) 진입 *권한* 충족, *Exit 5조건 자동 충족 ≠* 본 cycle). |

### §1.2 두 영역 답습 (51 entry audit brief §1.3 답습)

| 영역 | GP / G | 영역 정의 | 권위 출처 |
|------|--------|---------|---------|
| **GP-2 송신 redaction** | G2 GP-2 | Hermes / Worker Agent stdout / stderr / log file / LLM API request body secret 노출 차단. **Hermes native redaction = Hermes upstream `agent/redact.py` 영역** (본 repo 內 부재, B-4 흡수). 본 repo 영역 = P1 facade RedactionFilter (TR-1 (d) carry-over 의존) + R-6 workflow 답습 확장 step. ADR-011 §2.3 운영 함의 #2 의 *보조* 역할 | `governance-preconditions.md §4` (정의 + Entry §4.4 + Exit §4.5 + 산출 §4.6 + 의존 ADR §4.7) |
| **G4 §4.4 Layer 4 — CI 회귀 검증** | G4 | Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증 + canonical JSON 위반 검출 + timestamp monotonicity 검증 + R-6 workflow 답습 확장. **MANDATORY 등급 5-layer 체계 內 Layer 4** (G4 §4.4.1 + ADR-012 §2.8 동형, B-1 답습 §4.4 권위 인용 정정 답습) | **PRIMARY**: `provider-agnostic-memory-skill-design.md §4.4.1 line 629~660` (G4 직접 정의) + **SUPPORTING**: `ADR-012 §2.8 line 264~272` (5-layer 동형) + **PRINCIPLE ONLY**: `ADR-012 §2.3 line 165~185` (Append-only + Hash Chain 원칙, **numbering 근거 아님** — §4.4 R-S1 답습) + `ADR-012 §3.4` (timestamp monotonicity) + `ADR-012 §2.7` (prev_hash 실패) + `ADR-012 §2.5` (RFC 8785 JCS) |

### §1.3 ⭐ 선차 변경 매트릭스 (선행 권위 vs 본 cycle 결정)

> **본 §1.3 = 본 brief 의 *핵심 framing*** — 선행 권위 와 본 (α) cycle (2026-05-28) 결정 사이의 *변경 차이* 명시.

| # | 영역 | 선행 권위 | 본 cycle 결정 | 권위 정당성 |
|---|------|---------|--------------|------------|
| 1 | **GP-2 시점 분리** | roadmap-mvp1 §1.3 line 103~107 — "GP-2 = MVP-2 로 분리 (C-7 답습) — *시점* 분리이지 *영구 제외* 아님" + governance-preconditions §4.4 line 445 — "⏳ 사용자 명시 GP-2 작업 진입 결정" | **GP-2 시점 분리 해제 — MVP-2 영역 진입 자격 발효** | ✅ 정당 |
| 2 | **G4 §4.4 Layer 4 진입 자격** | provider-agnostic-memory-skill-design §4.4 (5-layer) + ADR-012 §2.3 (4-layer) + §2.8 (5-layer) | **Layer 4 = CI 회귀 검증 (MANDATORY), MVP-2 진입 영역 채택** | **R-S1 CONFIRMED divergence — 권위 인용 chain 정정 답습 (§4.4)** (B-1 흡수) |
| 3 | **두 영역 통합 R-6 workflow 확장** | 51 entry audit brief §4 W-A 권고 — "단일 R-6 workflow 확장 통합" | **W-A 권고 시점 = framing 정밀화** — 실 repo 기존 G4 workflow (`g4-hash-chain.yml` 10652B + `history-anchor-verifier.yml` 19094B + `rewrite-defense.yml` 16454B) 분리 운영 답습 + 3 옵션 명시: (i) 일괄 통합 / (ii) 보존 + 중복 step 추가 / (iii) 분산 추가 | **W 대안 매트릭스 5 (W-A/B/C/D/E, §2.3 답습) (B-5 + B-7 흡수)** |
| 4 | **sub-수단 결정 vs 진입 합의 분리** | 51 entry audit brief §9 + 24 entry MVP-1 1.5차 보강 entry brief (sub-수단 채택 결정 통합) | **본 (α) cycle = MVP-2 영역 *진입* 합의만, sub-수단 결정 = (β) 별도** | **✅ 정당 + 24 entry 답습 형태 변경 자격 명시** (N-8 흡수). 사유 = 25 조합 (R-1~R-5 × L-1~L-5) 복잡도 답습 (24 entry 4 sub-수단 보다 복잡), 1-cycle 內 흡수 부담 회피 + 단계별 cycle 답습 충실 (N-11 흡수). 본 변경 자격 = 사용자 명시 + roadmap-mvp1 §1.3 답습 + ADR-011 §2.1 (e) 후속 운영조건 답습 |
| 5 | **roadmap.md §5.4 그룹 C+D 합의 형태 격상** ⭐ (B-7 흡수, Agent C R-C-2) | roadmap.md §5.4 = "단축 합의 + PoC evidence" 권고 (그룹 D = GP-3 + GP-2 / 그룹 C = G4 §4.4 영역) | **풀 3+1 + 외부 LLM 1+ 격상** | **⚠️ 격상 변경 — 사용자 명시 + roadmap-mvp1 §1.3 답습 + 32 entry MVP-1 PASS 발효 합의 패턴 (풀 3+1 + 외부 LLM 1+) 동격 답습**. roadmap.md §5.4 = 그룹 D 일반 영역 "권고" / 본 cycle = MVP-1 동격 큰 영역 = roadmap-mvp1 §1.3 + 32 entry 답습 패턴 우선 |

→ **요약**: 본 (α) cycle = "MVP-2 영역 *진입* 합의" 한정 (수단 결정 = (β) 분리). 두 영역 모두 풀 3+1 + 외부 LLM 1+ + 사용자 명시 일관. R-S1 = **CONFIRMED divergence** (§4.4 답습 5 source verify).

---

## §2 두 영역 진입 자격 분석

### §2.1 GP-2 송신 redaction — 진입 자격

#### §2.1.1 영역 정의 (51 entry audit brief §1.3 + governance-preconditions §4 답습 + B-4 framing 정밀화)

| 항목 | 내용 |
|------|------|
| **목적** | Hermes / Worker Agent stdout / stderr / log file / LLM API request body secret 노출 차단 (P2 위반 경로 차단) |
| **영역 분리 framing** ⭐ (B-4 흡수) | **(i) Hermes upstream 영역**: `agent/redact.py` (Hermes upstream HEAD v0.12.0, `/tmp/hermes-phase0/hermes-agent/agent/redact.py` 401 LOC) — **본 repo 內 ≠ 존재**. 본 cycle scope 外 (Hermes upstream PR 영역). **(ii) 본 repo 영역**: P1 facade RedactionFilter (TR-1 (d) carry-over 의존, `adapters/llm/facade.py` placeholder → real) + R-6 workflow 답습 확장 step (log file canary inject + grep). **(iii) CI step 영역**: 본 repo `.github/workflows/r2-canary.yml` 답습 확장 |
| **검증 시점** | Hermes container 운영 시점 (native redaction, Hermes upstream 영역) + LLM facade 진입점 (본 repo P1 facade) + CI step (본 repo R-6 workflow 확장) |
| **메커니즘** | (R-1) Hermes native redaction `agent/redact.py` (Hermes upstream 영역) + (R-2) P1 facade RedactionFilter (본 repo, TR-1 의존) + (R-3) log file canary inject + grep CI step (본 repo R-6 확장) + (R-4) R-1+R-2+R-3 병행 + (R-5) base64/URL-encoded evasion 별도 (MVP-2/3 분리) |
| **권위 출처** | governance-preconditions.md §4 + ADR-011 §2.3 운영 함의 #2 + roadmap-mvp1 §1.3 + R-4 답습 (`redaction-pattern-equivalence.md`) + R-4.1 답습 (`r4-1-trigger-extension-evidence.md`) |

#### §2.1.2 진입 자격 (51 entry audit brief §2.1 답습 + B-4 framing 정밀화)

| Entry 조건 | 현 상태 | 본 (α) 합의 발효 후 |
|----------|--------|------------------|
| R-4 pattern equivalence 작성 완료 | ✅ 충족 | (그대로 유지) |
| Hermes native redaction `agent/redact.py` 존재 확인 | **⚠️ Hermes upstream 영역 충족** (Hermes upstream HEAD v0.12.0 401 LOC 답습, 본 repo 內 ≠ 존재. **51 audit brief carry-over 결함 framing 정정**, B-4 흡수) | (그대로 유지 — Hermes upstream 영역 답습) |
| **사용자 명시 GP-2 작업 진입 결정** | ⏳ 본 (α) 합의 영역 | **✅ 본 (α) 합의 발효 시점 충족** |

→ **본 (α) 합의 발효 후 Entry 3/3 모두 충족 (단, R-1 영역 = Hermes upstream 영역 분리 답습 framing) → 본 repo 內 sub-cycle 진입 권한 발효** (Hermes upstream PR = 본 cycle scope 外).

#### §2.1.3 본 cycle 합의 발효 시 채택 결정 영역

✅ **GP-2 영역 진입 발효 자격** — 본 (α) 합의 APPROVE 시점 발효
✅ **(β) sub-수단 결정 cycle 진입 자격 발효** — R-1 / R-2 / R-3 / R-4 / R-5 中 결정 cycle 진입 자격 (별도 합의)
✅ **Rollback Trigger 본문 *후보 채택*** (§5.1 답습 — RT-1 / RT-2 / RT-3, 구현 발효 ≠ 본 합의, N-1 흡수)
✅ **Evidence 형식 본문 *후보 채택*** (§5.2 답습 — E-1 / E-2 / E-3 / E-7 / E-8 / E-9)

#### §2.1.4 미발효 영역 (deferred)

❌ R-1~R-5 中 sub-수단 결정 = (β) 별도 cycle
❌ base64 / URL-encoded / 압축 evasion 영역 = R-5 별도 (MVP-2/3 분리, G3-4 답습)
❌ Tier-2 / Tier-3 vendor catalog 본문 확장 = 별도 풀 3+1 + 외부 LLM 1+
❌ Implementation Evidence PASS 발효 = 실 구현 + (b) PoC + (d) R-6 actual run PASS + (e) 합의 APPROVE 후 별도 합의
❌ Hermes upstream `agent/redact.py` 본 repo 內 import 결정 = 별도 합의

### §2.2 G4 §4.4 Layer 4 — CI 회귀 검증 — 진입 자격

#### §2.2.1 영역 정의 (51 entry audit brief §3.1 + G4 §4.4.1 + ADR-012 §2.8 답습 + §4.4 권위 인용 정정 답습)

| 항목 | 내용 |
|------|------|
| **목적** | Evidence Ledger 무결성 자동 회귀 검증 — Layer 1 (hash chain) + Layer 2 (history) + canonical JSON 위반 + timestamp monotonicity 위반 자동 검출 |
| **검증 시점** | CI step (매 PR + nightly) — R-6 workflow (`r2-canary.yml`) 답습 확장 (또는 실 repo 기존 `g4-hash-chain.yml` 답습 확장, W-A/B/C/D/E §2.3 답습) |
| **메커니즘** | (L-1) Python stdlib 단독 (`hashlib.sha256` + `json.dumps(sort_keys=True, separators=(",",":"))`) + (L-2) RFC 8785 JCS Primary (`pyjcs` / `rfc8785`) + (L-3) Layer 4 R-6 workflow step + (L-4) L-1+L-3 병행 (MVP 권고) + (L-5) L-2+L-3 병행 (정식) |
| **권위 출처** ⭐ (B-1 R-S1 정정 답습) | **PRIMARY**: `provider-agnostic-memory-skill-design.md §4.4.1 line 629~660` (G4 직접 정의 5-layer) + **SUPPORTING**: `ADR-012 §2.8 line 264~272` (5-layer 동형) + **PRINCIPLE ONLY (numbering 근거 아님)**: `ADR-012 §2.3 line 165~185` (Append-only + Hash Chain 원칙) + `ADR-012 §3.4` (timestamp monotonicity) + `ADR-012 §2.7` (prev_hash 실패) + `ADR-012 §2.5` (RFC 8785 JCS) |

#### §2.2.2 진입 자격 (51 entry audit brief §3.2 답습 + B-6 PoC 시제 격상 답습)

| Entry 조건 | 현 상태 | 본 (α) 합의 발효 후 |
|----------|--------|------------------|
| Design/Governance Gate PASS 답습 (G4 = PASS Bundled) | ✅ 충족 | (그대로) |
| ADR-012 §2.3 + §2.8 Layer 1~5 권위 정의 발효 (R-S1 정정 답습) | ✅ 충족 | (그대로) |
| G4 §4.4 본문 P-1 (RFC 8785 JCS) 흡수 완료 | ✅ 충족 | (그대로) |
| Layer 1 (hash chain) 실 구현 (의존 영역) | ⚠️ **PoC 시제 충족 / PASS 시제 미충족** ⭐ (B-6 흡수) | (β) sub-수단 결정 + 실 구현 sub-cycle 영역 |
| canonical JSON test corpus (≥ 20개 RFC 8785 reference) | ⚠️ **PoC 시제 충족 (`tests/canonical/` 24 fixtures = 8 카테고리 × 3) / PASS 시제 미충족** ⭐ (B-6 흡수) | 실 구현 sub-cycle 영역 |
| Layer 4 CI step 실 구현 | ⚠️ **PoC 시제 충족 (`g4-hash-chain.yml`) / PASS 시제 미충족** ⭐ (B-6 흡수) | 실 구현 sub-cycle 영역 |
| ledger 첫 entry (genesis hash) | ⚠️ **PoC 시제 충족 (`tools/jsonl_hash_chain.py` genesis hash 함수 + 4 violation_type) / PASS 시제 미충족** ⭐ (B-6 흡수) | (γ) 분리 영역 결정 cycle 영역 |
| **사용자 명시 작업 진입 결정** | ⏳ 본 (α) 합의 영역 | **✅ 본 (α) 합의 발효 시점 충족** |

→ **본 (α) 합의 발효 후 Entry 사용자 명시 부분 충족 → 4 의존 영역 PoC 시제 충족 / PASS 시제 후속 (β) / (γ) cycle 결정 + 실 구현 sub-cycle 진입 권한 발효**.

#### §2.2.3 본 cycle 합의 발효 시 채택 결정 영역

✅ **G4 §4.4 Layer 4 *planning/decision track* 진입 발효 자격** ⭐ (N-2 흡수) — 본 (α) 합의 APPROVE 시점 발효
✅ **(β) sub-수단 결정 cycle 진입 자격 발효** — L-1 / L-2 / L-3 / L-4 / L-5 中 결정 cycle 진입 자격 (별도 합의)
✅ **(γ) 분리 영역 결정 cycle 진입 자격 발효** — Layer 1+2 의존 영역 우선 진입 vs Layer 4 동시 진입 (별도 합의)
✅ **Rollback Trigger 본문 *후보 채택*** (§5.1 답습 — RT-4 / RT-5 / RT-6)
✅ **Evidence 형식 본문 *후보 채택*** (§5.2 답습 — E-4 / E-5 / E-6 / E-7 / E-8 / E-9)
⚠️ **Implementation track 진입 = (β)/(γ) 이후** (N-2 흡수)

#### §2.2.4 미발효 영역 (deferred) + (γ) 4 대안 매트릭스 (N-12 흡수)

❌ L-1~L-5 中 sub-수단 결정 = (β) 별도 cycle
❌ (γ) 분리 영역 결정 cycle = 4 대안:
- **(γ-a) Layer 1+2 의존 영역 우선 진입 후 Layer 4 추가** (단계적, 안전)
- **(γ-b) Layer 4 단독 진입** (Layer 1+2 = 의존 영역 자동 동시 진입)
- **(γ-c) Layer 1+2+4 동시 진입** (defense-in-depth 답습)
- **(γ-d) Layer 4 단독 + Layer 1+2 = (γ) 별도 cycle 분리** (현 brief framing)
❌ 외부 library (`pyjcs` / `rfc8785`) 도입 결정 = L-5 별도 + **L-1.5 alternative** (stdlib + 자체 RFC 8785 reference test corpus 검증 충분성, N-12 흡수) — ADR-012 §2.1 R-2 / R-4.1 PoC 자동 재실행 trigger
❌ Implementation Evidence PASS 발효 = 실 구현 + PoC + R-6 actual run PASS + 합의 후 별도

### §2.3 두 영역 통합 R-6 workflow 확장 — 진입 자격 + W 5 대안 매트릭스 (B-5 + B-7 흡수)

#### §2.3.1 영역 정의 (51 entry audit brief §4 답습 + B-5 framing 정밀화)

| 항목 | 내용 |
|------|------|
| **목적** | GP-2 §4.6 산출 후보 (log file canary inject step) + G4 §4.4 Layer 4 (Layer 1+2 자동 회귀 + canonical 위반 + timestamp monotonicity step) **단일 R-6 workflow (`r2-canary.yml`) 확장 통합 또는 분리 운영** |
| **실 repo 기존 G4 workflow 답습** ⭐ (B-5 흡수) | `.github/workflows/g4-hash-chain.yml` (10652B) + `history-anchor-verifier.yml` (19094B) + `rewrite-defense.yml` (16454B) **이미 분리 운영 중** (PoC 시제 답습). 본 cycle = 통합 vs 분리 결정 framing 정밀화 영역 |
| **권위 출처** | 51 entry audit brief §4 W-A 권고 + governance-preconditions §4.6 line 460 + G4 §4.4.1 line 653 |

exec
/bin/bash -lc "sed -n '1,260p' docs/phase0/mvp2-layer-124-pass-entry-brief.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
# Layer 1+2+4 통합 PASS 격상 entry brief (v1.1)

> **작성**: 2026-05-28 (55번째 entry 진입 cycle)
>
> **v1 → v1.1 갱신**: 풀 3+1 + 외부 LLM 1+ (codex gpt-5.5 cross-vendor) 통합 합의 (`docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass.md`) BLOCKING 9 + 권고 18 1pass 흡수 (별도 v2 cycle 0, ceremony-inflation 차단). §11 v1.1 보강 매트릭스 추가.
>
> **scope**: G4 §4.4 Layer 1+2+4 통합 PASS 격상 진입 합의 ((γ-c) 채택 발효 답습)
>
> **본 cycle = 큰 cycle** (54 entry (γ-c) 채택 발효 후 carry-over 5번, 풀 3+1 + 외부 LLM 1+, 24/52 entry entry brief 답습 동형)
>
> **본 cycle 발효 자격** = **풀 3+1 합의 + 외부 LLM 1+ 응답 입력 (cross-vendor) + 사용자 명시 결정**
>
> **본 cycle 발효 효과** = Layer 1+2+4 통합 PASS 격상 진입 권한 발효 + 후속 실 구현 sub-cycle 진입 자격 발효 (evidence 평가 + (γ-c) 특화 의무 4 답습 + RT-γ-6 평가). 실 구현 + R-6 actual run + PASS 발효 = 별도 sub-cycle (본 cycle = 진입 합의 한정)

---

## §0 본 brief 의 범위

### §0.1 사용자 진입 명령 답습 (carry-over from 54 entry, commit `895a77b`)

54 entry `mvp2-gamma-decision-brief.md` §4 + SESSION carry-over #5 답습:
- (α) ✅ **54 entry 발효** ((γ-c) Layer 1+2+4 동시 채택 결정 발효)
- (β) sub-수단 결정 cycle — 별도 합의
- **5번: Layer 1+2+4 통합 PASS 격상 cycle ((γ-c) 채택 발효 답습) — 풀 3+1 + 외부 LLM 1+, Layer subsection 강제 + "부분 답습" framing 영구 + RT-γ-6 답습**

본 cycle 진입 사용자 명시 (2026-05-28, 54 entry commit `895a77b` push 후) — "5번 Layer 1+2+4 통합 PASS 격상 진입". 본 brief = (γ-c) 채택 발효 답습 한정. (β) sub-수단 결정 + 실 구현 sub-cycle + MVP-2 PASS 발효 합의 = 별도 cycle.

### §0.2 본 brief 가 *하는* 것

1. **54 entry (γ-c) 채택 발효 답습** ((γ-c) 특화 의무 4 답습 cross-check) (§1)
2. **PoC 시제 충족 자격 평가** (Layer 1+2+4 각 영역별, 53 entry §2.5 + 본 cycle audit 답습) (§2)
3. **Layer 별 PASS 격상 영역 분석** — Layer 1 (hash chain) + Layer 2 (Git append-only, 2a local + 2b remote 분리) + Layer 4 (CI 회귀 검증) (§2)
4. **ADR-011 §2.1 (a)~(d) 4조건 모법 + (e) 후속 운영조건 매트릭스 (Layer 별 + 통합)** (§3, 52 entry B-2 framing 답습)
5. **본 cycle 합의 형태 = 풀 3+1 + 외부 LLM 1+ 정당화** (53/54 entry 답습) (§4.1)
6. **(γ-c) 특화 의무 4 영구 답습** — Layer subsection 강제 + "부분 답습" framing + 통합 동시 + RT-γ-6 (§4.2)
7. **7 풀 3+1 승격 트리거 발화 검증** (§4.3)
8. **Rollback Trigger / Evidence *후보 채택*** (구현 발효 ≠ 본 합의, 52/53 entry N-1 답습) (§5)
9. **RT-γ-6 R-S1 PASS 시점 선행/동시 정정 평가** ((γ-c) 특화 의무 4 답습, §5.2 영구 의무) (§5)
10. **외부 LLM 응답 요구 영역** (사용자 영역) (§7)
11. **후속 실 구현 sub-cycle 진입 자격 명문** (§8)

### §0.3 본 brief 가 *하지 않는* 것 (사용자 명시 답습 + 본 brief 영역 한계)

| # | 영역 | 위반 시점 |
|---|------|----------|
| 1 | 실 코드 / runtime code 구현 | 0건 |
| 2 | `tools/jsonl_hash_chain.py` / `tools/canonical_json.py` 본문 변경 | 0건 (PoC 시제 답습 보존) |
| 3 | `tests/canonical/` test corpus 본문 변경 | 0건 (72 files / 8 카테고리 답습 보존) |
| 4 | `.github/workflows/*.yml` 본문 변경 | 0건 (4 G4 workflow 답습 보존) |
| 5 | **`git config receive.denyNonFastForwards true` 활성화 실행** ⭐ (53 entry B-3 답습) | 0건 (활성화 = 별도 실 구현 sub-cycle 영역, 본 brief = evidence 평가 + 활성화 계획 권고 한정) |
| 6 | ledger 첫 entry (genesis hash) 작성 | 0건 |
| 7 | R-6 workflow actual run 트리거 | 0건 (별도 실 구현 sub-cycle) |
| 8 | **GP-2 sub-수단 결정** (R-1~R-5) | 0건 ((β) 별도 cycle) |
| 9 | **G4 §4.4 Layer 4 sub-수단 결정** (L-1~L-5) | 0건 ((β) 별도 cycle) |
| 10 | **W 통합 결정** (W-A~E) | 0건 ((β) 별도 cycle) |
| 11 | 외부 library (`pyjcs` / `rfc8785`) 도입 결정 | 0건 (L-5 별도) |
| 12 | threshold 고정 | 0건 |
| 13 | Tier-2 / Tier-3 vendor catalog 본문 확장 | 0건 |
| 14 | **Layer 1+2+4 통합 PASS 발효** ⭐ | 0건 (본 cycle = 진입 합의, PASS 발효 = 실 구현 + (a)~(d) evidence + (e) 합의 APPROVE + 사용자 명시 후 별도 합의) |
| 15 | **MVP-2 Implementation Evidence PASS 발효** | 0건 (Layer 통합 PASS + GP-2 PASS + 통합 합의 후 별도) |
| 16 | **MVP-1 PASS 재선언** | 0건 (32 entry 답습 유지) |
| 17 | Operational Readiness PASS / Hermes PMO 격상 | 0건 |
| 18 | ADR / 헌법 / roadmap / governance / G4 / ADR-012 본문 갱신 | 0건 |
| 19 | `adapters/llm/facade.py` placeholder → real 본문 (TR-1) | 0건 (별도 trajectory) |
| 20 | G4 §4.4 Layer 3 (Signed commit) + Layer 5 (External anchor) 영역 진입 결정 | 0건 ((γ-c) "부분 답습" framing 영구 답습, 54 entry §1.3 의무 2) |
| 21 | (γ-a/b/d) 대안 재평가 | 0건 (54 entry (γ-c) 채택 결정 영구 발효 답습) |
| 22 | (γ-e/f/g) hybrid 대안 결정 | 0건 (53 entry B-8 답습) |
| 23 | R-S1 cross-reference 정정 자동 진입 (ADR-012 §2.3 vs §2.8) | 0건 (별도 cycle, RT-γ-6 답습 — 단, 본 cycle = PASS 시점 선행/동시 정정 *평가* 의무) |
| 24 | branch protection contexts 자동 추가 | 0건 (사용자 admin scope 영역, 43 entry 답습) |
| 25 | Hermes upstream `agent/redact.py` 본 repo 內 import 결정 | 0건 |
| 26 | 자동 후속 실 구현 sub-cycle 진입 | 0건 (사용자 명시 의무) |
| 27 | Layer 4 PASS 선발효 (Layer 1+2 PASS 부재 시, (γ-d) 모순 답습) | 0건 (영구 금지, 54 entry §5 #3 답습) |
| 28 | Layer 4 evidence 內 Layer 1+2 evidence 합산 (Layer subsection 미준수) | 0건 ((γ-c) 특화 의무 1 영구 답습, 54 entry §5 #9) |
| 29 | "defense-in-depth 충실 답습" 또는 "완전 답습" 표현 사용 | 0건 ((γ-c) 특화 의무 2 영구 답습, 54 entry §5 #8) |
| 30 | 본 brief 자체 영구화 / 권위 chain 등재 | 0건 |

### §0.4 본 brief 의 권위 한계

- ✅ 본 brief 발효 자격 = **풀 3+1 합의 + 외부 LLM 1+ 응답 입력 (cross-vendor) + 사용자 명시 결정**
- ✅ 본 brief 발효 결과:
  1. Layer 1+2+4 통합 PASS 격상 *진입 권한 발효*
  2. 후속 실 구현 sub-cycle 진입 자격 발효
  3. (γ-c) 특화 의무 4 답습 영구 보존 (Layer subsection 강제 + "부분 답습" framing + 통합 동시 + RT-γ-6)
  4. PASS evidence template *후보 채택* (Layer 1/2/4 subsection 분리 강제)
  5. Rollback Trigger / Evidence 후보 채택
- ❌ 본 brief 자체에서 Layer 1+2+4 통합 PASS *발효* 0건 (실 구현 + (a)~(d) evidence + (e) 합의 APPROVE 후 별도)
- ❌ 본 brief 자체에서 sub-수단 결정 0건
- ❌ 본 brief 자체에서 실 구현 0건 (denyNonFastForwards 활성화 0 / R-6 actual run 0)
- ❌ 본 brief 자체에서 MVP-2 Implementation Evidence PASS 발효 0건
- ❌ 본 brief 자체에서 R-S1 cross-reference 정정 0건 (RT-γ-6 평가 한정, 정정 = 별도 cycle)
- ❌ 본 brief 자체에서 ADR-011 §2.1 (a)~(d) 4조건 자동 충족 선언 0건
- ⚠️ 본 brief 합의 후 *자동 실 구현 sub-cycle 진입 금지* — 사용자 명시 결정 의무

---

## §1 진입 컨텍스트 답습

### §1.1 선행 권위 답습 (54 entry + 53 entry + 52 entry + 32 entry)

| 합의 / 권위 | 본 cycle 답습 영역 |
|----------|-----------------|
| 54 entry decision brief + 1-agent 직접 합의 (`895a77b` 발효) — (γ-c) Layer 1+2+4 동시 채택 결정 발효 | 본 brief 의 **직접 입력 자료** (54 entry §1.3 (γ-c) 특화 의무 4 답습 source) |
| 53 entry (γ) brief v1.1 + Reviewer 통합 합의 — 4 source consensus + R-S1 5 source verify CONFIRMED | 4 source consensus 권고 답습 (Reviewer 통합 (γ-c) 1순위) + R-S1 후행 영향 RT-γ-6 답습 source |
| 52 entry (α) entry brief v1.1 + Reviewer 통합 합의 — MVP-2 진입 권한 발효 | MVP-2 영역 (GP-2 + G4 §4.4 Layer 4) 진입 권한 발효 답습 |
| 32 entry MVP-1 Implementation Evidence PASS *완전 발효 (α)* | MVP-1 PASS 답습 그대로 유지 (재선언 0). MVP-2 PASS = Layer 통합 PASS + GP-2 PASS + 통합 합의 후 별도 |
| `provider-agnostic-memory-skill-design.md §4.4.1 line 629~660` (PRIMARY, 5-layer) | Layer 1~5 정의 |
| `ADR-012 §2.8 line 264~272` (SUPPORTING, 5-layer 동형) | Layer numbering 권위 |
| `ADR-012 §2.3 line 165~185` (PRINCIPLE ONLY) | Hash chain + Append-only 원칙 (numbering 근거 아님, R-S1 답습) |
| `ADR-012 §2.7` (prev_hash 실패 BLOCK + Manual Review) | RT-γ-4 답습 |
| `ADR-012 §3.4` (timestamp monotonicity) | RT-γ-6 답습 |
| `ADR-012 §2.5` (RFC 8785 JCS) | canonical JSON test corpus 답습 |
| `ADR-011 §2.1 (a)~(d) 4조건 모법 + (e) 후속 운영조건` (52 entry B-2 답습) | 5조건 매트릭스 §3 |
| **본 cycle audit (read-only, 2026-05-28)** | PoC 시제 현 상태 cross-check (§2.5 답습) |

### §1.2 54 entry (γ-c) 특화 의무 4 영구 답습 (본 brief 핵심 framing)

| # | 의무 | 본 cycle 답습 |
|---|------|-----------|
| 1 | PASS evidence template Layer 1/Layer 2/Layer 4 subsection 강제 | §2 Layer 별 분리 분석 + §3 매트릭스 Layer 별 컬럼 + §5.2 evidence template 후보 (Layer subsection 강제) |
| 2 | "defense-in-depth 부분 답습" framing 영구 유지 (Layer 3+5 = scope 외) | §0.3 #20 명시 + §2.1 영역 정의 "부분 답습" 표현 사용 + §6 #6 영구 답습 |
| 3 | Layer 1+2+4 통합 PASS evidence 동시 발효 | §2.4 통합 영역 + §3 통합 매트릭스 + §4.2 통합 발효 |
| 4 | RT-γ-6 R-S1 PASS 시점 선행/동시 정정 평가 의무 | §5.2 RT-γ-6 평가 + §8 다음 단계 #5 명문 |

### §1.3 ⭐ PoC 시제 현 상태 cross-check (본 cycle audit 발견)

본 cycle 시점 (2026-05-28) audit 결과:

| 영역 | 현 상태 | 답습 |
|------|--------|----|
| `tools/jsonl_hash_chain.py` | ✅ 14038B (genesis hash + 4 violation_type: PREV_HASH_MISMATCH + HASH_RECALCULATION + HISTORY_REWRITE + GENESIS_MISMATCH) | 53 entry Agent A NT-A-1 + B-6 답습 |
| `tools/canonical_json.py` | ✅ 10055B (rfc8785 + jcs + jq -S -c fallback + cross-check mode) | 53 entry codex NOTE-5 답습 |
| `tests/canonical/` | ✅ **72 files / 8 카테고리** (array, escape, hash_stability, key_ordering, lossy, nested, number, unicode = 8 × 3 case × 3 파일 = 72 = 24 fixtures input) | 53 entry codex NOTE-5 verify (8 × 3 × 3 = 72) + 52 entry Agent A R-A-2 carry-over 해소 |
| `.github/workflows/g4-hash-chain.yml` | ✅ 10652B (7 step 분리) | 53 entry Agent A N-A-1 + N-A-3 답습 |
| `.github/workflows/history-anchor-verifier.yml` | ✅ 19094B | 53 entry Agent A N-A-3 답습 |
| `.github/workflows/rewrite-defense.yml` | ✅ 16454B | 동상 |
| `.github/workflows/r2-canary.yml` | ✅ 5476B | 동상 (N-7 흡수) |
| **`git config receive.denyNonFastForwards`** ⭐ | ⚠️ **미설정** (local + global 모두 출력 0건) — 53 entry B-3 답습 (Layer 2a local workflow evidence 별도 verify 의무) | 53 entry B-3 답습 — 본 cycle = 활성화 evidence 별도 verify 의무 명문 + 실 구현 sub-cycle 활성화 의무 |
| `tests/fixtures/jsonl_ledger/{pass,fail}/` | ✅ 다수 (minimal_chain + roundtrip_t2_strict + genesis_mismatch + hash_recalculation + prev_hash_mismatch + missing_event_field) | 본 cycle audit 신규 발견 |
| `tests/fixtures/history_anchor_verifier/` | ✅ 다수 (original_ledger + extended_ledger + full_rewrite_ledger + middle_deletion_ledger) | 본 cycle audit 신규 발견 |

→ **PoC 시제 전 영역 충족 (Layer 2a denyNonFastForwards 1 영역 미설정 = 실 구현 sub-cycle 활성화 의무)**. tests/canonical 24 fixture 정량 = 본 cycle audit 직접 verify 완료 (72 files / 8 × 3 × 3, 52 entry Agent A R-A-2 carry-over 해소).

---

## §2 Layer 별 PASS 격상 영역 분석

### §2.1 영역 정의 ((γ-c) 특화 의무 2 답습 — "부분 답습" framing)

본 brief = **G4 §4.4 Layer 1+2+4 통합 *부분 답습*** (Layer 3 Signed commit + Layer 5 External anchor = 본 cycle scope 외, 별도 cycle 영역, 54 entry §1.3 의무 2 영구 답습).

### §2.2 Layer 1 — Hash Chain (MANDATORY)

| 항목 | 내용 |
|------|------|
| **PoC 시제** | ✅ `tools/jsonl_hash_chain.py` 14038B (genesis hash 함수 + 4 violation_type: PREV_HASH_MISMATCH + HASH_RECALCULATION + HISTORY_REWRITE + GENESIS_MISMATCH) |
| **권위** | G4 §4.4.1 line 631~636 + ADR-012 §2.3 line 165~169 (PRINCIPLE) + §2.8 line 268 (numbering) |
| **PASS 격상 영역** | (a) hash chain 검증 PoC PASS (middle tampering 차단 PoC, Docker 격리) + (b) canonical JSON sha256 동등성 검증 + (c) genesis hash 첫 entry 작성 evidence + (d) Layer 4 CI step 內 hash chain 검증 actual run PASS |
| **fixtures** | `tests/fixtures/jsonl_ledger/{pass,fail}/` (minimal_chain + roundtrip_t2_strict + genesis_mismatch + hash_recalculation + prev_hash_mismatch + missing_event_field) |
| **violation_type Layer 매핑** (53 entry N-6 답습) | PREV_HASH_MISMATCH + HASH_RECALCULATION + GENESIS_MISMATCH = Layer 1 |

### §2.3 Layer 2 — Git Append-only Branch (MANDATORY, 2a + 2b 분리, 53 entry B-3 답습)

#### §2.3.1 Layer 2a — local workflow

| 항목 | 내용 |
|------|------|
| **PoC 시제** | ⚠️ **`git config receive.denyNonFastForwards` 미설정** (local + global 모두 0건 verify, 본 cycle §1.3 답습) — Layer 2a evidence 별도 verify 의무 |
| **권위** | G4 §4.4.1 line 638~642 + ADR-012 §2.3 line 171~175 + §2.8 line 269 |
| **PASS 격상 영역** | (a) `git config --system receive.denyNonFastForwards true` 활성화 + entrypoint 또는 pre-receive hook 강제 + (b) Docker 격리 PoC (force-push 시도 → reject) + (c) Layer 4 CI step base branch 대비 JSONL line deletion / rewrite 감지 actual run PASS |
| **fixtures** | `tests/fixtures/history_anchor_verifier/{pass,fail}/` (original_ledger + extended_ledger + middle_deletion_ledger + full_rewrite_ledger) |
| **실 구현 sub-cycle 의무** | denyNonFastForwards 활성화 = 본 cycle scope 외, 실 구현 sub-cycle 영역 (별도 사용자 명시) |
| **violation_type Layer 매핑** (53 entry N-6 답습) | HISTORY_REWRITE = Layer 2 |

#### §2.3.2 Layer 2b — remote / admin

| 항목 | 내용 |
|------|------|
| **PoC 시제** | ✅ branch protection rule (43 entry 8 contexts 답습) |
| **권위** | G4 §4.4.1 line 640 + ADR-012 §2.3 line 173 |
| **PASS 격상 영역** | (a) main branch protection 8 contexts + force push/delete false + required_approving_review_count + (b) admin scope 신규 contexts 추가 (사용자 영역) |
| **fixtures** | main branch protection rule (43 entry 답습) |

### §2.4 Layer 4 — CI 회귀 검증 (MANDATORY)

| 항목 | 내용 |
|------|------|
| **PoC 시제** | ✅ 4 workflows 분리 운영: `g4-hash-chain.yml` (10652B, 7 step) + `history-anchor-verifier.yml` (19094B) + `rewrite-defense.yml` (16454B) + `r2-canary.yml` (5476B) |
| **권위** | G4 §4.4.1 line 649~653 (PRIMARY) + ADR-012 §2.8 line 271 (SUPPORTING) |
| **PASS 격상 영역** | (a) Layer 1 (hash chain) 자동 회귀 검증 + Layer 2 (history) 자동 회귀 검증 + (b) canonical JSON 위반 검출 (RFC 8785 reference 동등성) + (c) timestamp monotonicity 검증 (ADR-012 §3.4) + (d) R-6 workflow 답습 확장 step (사용자 결정 영역, W-A/B/C/D/E 中 결정 = (β) 별도 cycle, 53 entry §2.3.2 답습) |
| **step prefix 권고** (53 entry N-5 답습) | g4-hash-chain.yml 7 step 답습 시 step prefix `[Layer N]` 권고 |
| **canonical test corpus** | ✅ `tests/canonical/` 72 files / 8 카테고리 (RFC 8785 reference ≥ 20 충족, 본 cycle §1.3 audit verify) |

#### §2.4.1 ⭐ workflow ↔ violation_type Layer 분담 매트릭스 (B-1 + B-5 흡수 — codex N-1 + Agent A R-A-1/R-A-2/R-A-3 답습)

⭐⭐⭐ **HISTORY_REWRITE enum fixture 미커버 + workflow internal numbering 명칭 충돌 + history-anchor-verifier.yml Layer 5 성격** (4 source filesystem direct cross-confirm):

| workflow | FAIL fixture cover | violation_type Layer 매핑 | 명칭 / 성격 주의 |
|---------|------------------|------------------------|---------------|
| `g4-hash-chain.yml` (10652B) | prev_hash + hash_recalc + **missing_event_field (schema)** + genesis_mismatch | PREV_HASH_MISMATCH + HASH_RECALCULATION + GENESIS_MISMATCH = **Layer 1** + schema 1종 | ⚠️ **HISTORY_REWRITE 미cover** (Layer 1 영역 3종 + schema 한정) |
| `rewrite-defense.yml` (16454B) | append-only / rewrite-command / line-regression | **HISTORY_REWRITE = Layer 2** | ⚠️ **workflow internal numbering "(Layer 2/3/4)" ≠ G4 §4.4.1 Layer 1~5 모델** (B-5 흡수, evidence ownership 혼선 방지 명문 — workflow 自체 numbering 은 별도 의미) |
| `history-anchor-verifier.yml` (19094B) | 5 FAIL 패턴 (middle deletion 등) | history anchor 검증 | ⚠️ **workflow name = "(Layer 5)" — Layer 5 External anchor PoC 시제 *이미 운영 中*** (B-2 흡수). "부분 답습" framing = *결정 영역 진입 0* 의미이지 *PoC 시제 0* 아님. 본 cycle Layer 5 결정 영역 진입 0 (PoC 시제 존재 ≠ Layer 5 PASS 진입) |
| `r2-canary.yml` (5476B) | R-6 canary regression | R-6 workflow 답습 | (W 결정 = (β) 영역) |

→ ⭐ **HISTORY_REWRITE Layer 분담**: g4-hash-chain.yml (Layer 1 3종 + schema) ↔ rewrite-defense.yml + history-anchor-verifier.yml (Layer 2 HISTORY_REWRITE) cross-reference 명문. fixture 추가 권고 (N-1): history_rewrite enum jsonl_ledger/fail fixture 추가 = 실 구현 sub-cycle 영역.

→ ⭐ **history-anchor-verifier.yml Layer 5 성격 명시** (B-2): Layer 5 External anchor PoC 시제 19094B 이미 운영. "4 G4 workflows 시제" 언급 시 Layer 5 PASS 진입 오해 방지 제한 문구 유지 (N-2 답습). 본 cycle = "부분 답습" framing = Layer 1+2+4 *결정 영역* 한정 (Layer 3 Signed commit + Layer 5 External anchor *결정 영역 진입 0*, PoC 시제 존재는 별개).

→ ⭐ **rewrite-defense.yml "(Layer 2/3/4)" internal numbering 명칭 충돌** (B-5): workflow 自체 numbering ≠ G4 §4.4.1 Layer 1~5 모델. evidence ownership 혼선 방지 — PASS evidence template 작성 시 G4 §4.4.1 Layer numbering PRIMARY 기준 (workflow internal numbering 별도 의미 명시).

### §2.5 통합 PASS 격상 ((γ-c) 특화 의무 3 답습 — 통합 동시 발효)

본 (γ-c) 채택 발효 답습 — Layer 1+2+4 **통합** PASS evidence 동시 발효 의무 (54 entry §1.3 의무 3 영구 답습):

| 통합 영역 | evidence template ((γ-c) 특화 의무 1 답습 — Layer subsection 강제) |
|---------|-----------------------------------------------|
| Layer 1 evidence subsection | hash chain 검증 PoC PASS + 4 violation_type 검출 actual run + canonical JSON sha256 동등성 |
| Layer 2a evidence subsection | denyNonFastForwards 활성화 evidence + Docker 격리 PoC (force-push reject) + JSONL line deletion / rewrite 감지 actual run |
| Layer 2b evidence subsection | branch protection rule actual state (43 entry 8 contexts + force push/delete false) |
| Layer 4 evidence subsection | 4 G4 workflow actual run PASS + canonical 위반 BLOCK + timestamp monotonicity 위반 BLOCK + R-6 workflow 통합 step (W 결정 답습) |
| 통합 evidence subsection | Layer 1+2+4 동시 actual run PASS evidence (Layer evidence 합산 금지, 54 entry §1.3 의무 1 영구 답습) |

⚠️ **Layer 4 evidence 內 Layer 1+2 evidence 합산 영구 금지** (54 entry §5 #9 답습).

### §2.6 본 cycle 합의 발효 시 채택 결정 영역

✅ **Layer 1+2+4 통합 PASS 격상 진입 발효 자격** — 본 cycle 합의 APPROVE 시점 발효
✅ **후속 실 구현 sub-cycle 진입 자격 발효** — denyNonFastForwards 활성화 + R-6 workflow 확장 step + actual run PASS evidence 수집 sub-cycle (별도 사용자 명시)
✅ **PASS evidence template *후보 채택*** (Layer subsection 강제, 구현 발효 ≠ 본 합의)
✅ **Rollback Trigger 본문 *후보 채택*** (§5.1 답습, RT-γ-1~6 + RT-PASS-1~3 신규)
✅ **(γ-c) 특화 의무 4 영구 답습 보존** (Layer subsection 강제 + "부분 답습" framing + 통합 동시 + RT-γ-6)
✅ **RT-γ-6 R-S1 PASS 시점 선행/동시 정정 *평가*** (정정 자체 = 별도 cycle)

### §2.7 미발효 영역 (deferred)

❌ Layer 1+2+4 통합 PASS 발효 자체 = 실 구현 + (a)~(d) evidence + (e) 합의 APPROVE + 사용자 명시 후 별도
❌ MVP-2 Implementation Evidence PASS 발효 = Layer 통합 PASS + GP-2 PASS + 통합 합의 후 별도
❌ (β) sub-수단 결정 (R-1~R-5 + L-1~L-5 + W-A~E) = 별도 cycle
❌ Layer 3 + Layer 5 영역 진입 = "부분 답습" framing 영구 답습 (54 entry §1.3 의무 2)
❌ R-S1 cross-reference 정정 자체 = 별도 cycle (RT-γ-6 평가 한정)

---

## §3 ADR-011 §2.1 (a)~(d) 4조건 모법 + (e) 후속 운영조건 — 5조건 매트릭스 (Layer 별 + 통합, 52 entry B-2 framing 답습)

| # | 조건 | Layer 1 | Layer 2 (2a+2b) | Layer 4 | 통합 |
|---|------|------|------|------|----|
| (a) | 동등 이상 보안 결과 | hash chain middle tampering 차단 (PoC 시제 충족) | 2a force-push 차단 + 2b branch protection / history 재작성 차단 (2a 미설정 verify 의무) | CI 회귀 검증 (Layer 1+2 통합 회귀, PoC 시제 충족) | Layer 1+2+4 통합 (각 subsection 분리) |
| (b) | 격리 환경 PoC 실증 | ✅ tools/jsonl_hash_chain.py + fixtures (PoC 시제 충족) | 2a ⚠️ denyNonFastForwards 활성화 + Docker 격리 PoC (실 구현 sub-cycle 의무) / 2b ✅ branch protection 답습 | ✅ 4 G4 workflow PoC 시제 충족 + R-6 actual run (실 구현 sub-cycle 의무) | 통합 evidence (Layer subsection 분리 강제) |
| (c) | ADR / SDD 권위 명시 | ✅ G4 §4.4.1 + ADR-012 §2.3 + §2.8 | ✅ 동상 | ✅ 동상 | ✅ 동상 |
| (d) | 자동 회귀 검증 경로 확보 | Layer 4 CI step 內 hash chain 검증 (R-6 workflow 답습) | Layer 4 CI step 內 base branch JSONL line deletion / rewrite 감지 | R-6 workflow 답습 확장 step (W 결정 = (β) 영역) | 통합 R-6 확장 step |
| (e) | 합의 APPROVE | ❌ gap — 본 cycle (α) 진입 합의 → 발효 ≠ 본 cycle (Layer 통합 PASS 발효 = 별도) | ❌ 동상 | ❌ 동상 | ❌ 동상 |

⭐ **(e) row 분리 (B-6 흡수 — Agent B R-B-1 답습, 자가 모순 정정)**:
- **(e1) 진입 권한** = ✅ **본 cycle 충족** (PASS 격상 *진입* 합의 발효)
- **(e2) PASS 발효** = ❌ **gap** (Layer 통합 PASS *발효* = 실 구현 + (a)~(d) evidence + 합의 APPROVE + 사용자 명시 후 별도 합의)

→ **본 cycle (e1) 진입 권한 충족 / (e2) PASS 발효 ≠ 본 합의 (별도 합의)**. "동일 (e)가 gap이면서 충족" 자가 모순 정정 (Agent B R-B-1 답습).

→ **PoC 시제 충족 영역 = (a)+(b)+(c)+(d) 부분 충족**. PASS 시제 = 실 구현 sub-cycle (denyNonFastForwards 활성화 + R-6 actual run + evidence 수집) 후 (e2) 통합 PASS 발효 합의.


codex
1차 확인상 문서들은 “결정”과 “실 구현”을 강하게 분리하고 있습니다. 지금은 실제 파일 존재/카운트/내용을 대조하면서, 특히 `tests/canonical` 수량과 workflow 보존 주장, `agent/redact.py` 부재 여부가 과장 없이 맞는지 확인 중입니다.
exec
/bin/bash -lc "sed -n '260,620p' docs/phase0/mvp2-beta-submeans-decision-brief.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:

### §6.3 수단별 차등 합의 깊이 (56 entry "수단별 차등" 답습)

| 수단 | 합의 깊이 | 근거 |
|------|--------|----|
| R-4 / L-4 (defense-in-depth + stdlib) | 풀 검토 | 51 audit 권고 답습이나 cross-trajectory 의존 (R-1/R-2) = 검증 필요 |
| W 보존 우선 | 풀 검토 | 51 audit W-A 권고 vs 실 repo 현 상태 tension = 핵심 검증 영역 |
| R-5 / L-2 / L-5 (evasion + 외부 library) | 분리 확정 (얕은 검토) | 영구 분리 = 결정 단순 |

---

## §7 실 구현 sub-cycle 입력 (조건부 승인 조건 6 + Rollback Trigger / Evidence)

### §7.1 조건부 승인 조건 6 매핑 (55 entry B-4 답습 — 수단 결정 후 실 구현 sub-cycle 의무)

| # | 조건 | 수단 매핑 | 영역 |
|---|------|--------|----|
| 1 | denyNonFastForwards (c) per-repo + (d) entrypoint/Dockerfile 활성화 | Layer 2a (L 영역) | 실 구현 sub-cycle |
| 2 | R-6 actual run PASS | W 보존 (r2-canary.yml) | 실 구현 sub-cycle |
| 3 | 4 G4 workflow actual run PASS | W 보존 (L-3) | 실 구현 sub-cycle |
| 4 | violation_type 정밀화 | Layer 1 (L-1) | 실 구현 sub-cycle |
| 5 | history_rewrite enum fixture 추가 | Layer 2 (L-3) | 실 구현 sub-cycle |
| 6 | Layer subsection 분리 (PASS evidence template) | 통합 ((γ-c) 의무 1) | Layer 통합 PASS 발효 cycle |

→ **본 (β) cycle = 위 6 조건의 *수단 기반* 확정** (어느 수단으로 충족할지). *실행* = 실 구현 sub-cycle.

### §7.2 Rollback Trigger 후보 (수단 결정 후 실 구현 입력, 51 §5 + 55 §5.1 답습)

| # | Trigger | 수단 | 발화 조건 |
|---|---------|----|---------|
| RT-R-1 | R-3 log canary grep PASS 후 평문 leak | R-3 | secret-hygiene workflow PASS 후 잔존 secret |
| RT-R-2 | R-1/R-2 cross-trajectory 미충족 시 GP-2 defense-in-depth 약화 | R-1/R-2 | Hermes import / facade real 지연 시 단일 layer 한정 명시 |
| RT-L-1 | Layer 1 violation_type 검출 실패 | L-1 | 4 violation_type 미작동 |
| RT-L-2 | canonical JSON 위반 미검출 (fallback 동등성 실패) | L-1 | RFC 8785 reference corpus mismatch |
| RT-W-1 | 기존 workflow 보존 위반 (파괴적 병합 발생) | W | 신규 통합 workflow 가 기존 workflow 무력화 |
| RT-γ-6 | R-S1 cross-reference 정정 후행 영향 (평가 한정) | 통합 | MVP-2 PASS 시점 선행/동시 정정 *자격* 평가 (정정 = 별도 cycle) |

### §7.3 Evidence 요건 (수단 결정 후 실 구현 sub-cycle 수집, 55 §5.2 답습)

- R 영역: R-3 actual run PASS (secret-hygiene workflow run ID) + R-1/R-2 가용 시 evidence 합산
- L 영역: L-1 4 violation_type 검출 actual run + canonical 72 files 동등성 + L-3 4 G4 workflow actual run PASS
- W 영역: 기존 workflow 보존 verify + 누락 step 추가 후 actual run PASS
- 통합: Layer 1/2/4 subsection 분리 evidence ((γ-c) 의무 1) + 외부 LLM 1+ (cross-vendor)

---

## §8 금지 사항

§0.2 답습 (24 항목). 추가 본 cycle 한정:

- ❌ W-A(i) 일괄 통합 채택 (기존 workflow 파괴, §4.2 비권고)
- ❌ 외부 library (L-2/L-5) 도입 결정 (별도 cycle)
- ❌ Hermes import (R-1) / facade real (R-2) 구현 경로 결정 (별도 cycle/trajectory)
- ❌ R-5 evasion 영역 진입 (MVP-2/3 분리)
- ❌ 자동 실 구현 sub-cycle 진입 (사용자 명시 의무)
- ❌ 본 cycle 수단 결정을 Layer 통합 PASS 발효 / MVP-2 PASS 발효로 확대 해석

---

## §9 외부 LLM 응답 요구 영역 (사용자 영역)

### §9.1 외부 LLM 자격 옵션 (55 §7.2 답습 — (E-α/β/γ))

| 옵션 | 영역 | 합의 형태 |
|------|----|---------|
| **(E-α)** Claude tmux + codex 직접 호출 (network-isolated 환경, `--dangerously-bypass-approvals-and-sandbox` = externally-sandboxed 전용) | 24/52/53/55 entry 답습 | 풀 3+1 + 외부 LLM 1+ |
| **(E-β)** 사용자 직접 외부 LLM 호출 | 추가 cross-vendor | 풀 3+1 + 외부 LLM 2+ |
| **(E-γ)** 외부 LLM 0 (작은 영역) | 작은 영역 | 풀 3+1만 |

→ 본 cycle = 큰 결정 (수단 결정) → **(E-α) 권고** (55 entry 동형). 사용자 명시 영역.

### §9.2 외부 LLM *입력 자료*

- 본 brief v1 (`docs/phase0/mvp2-beta-submeans-decision-brief.md`)
- 51 audit brief + 52 (α) brief v1.1 + 55 Layer 124 PASS brief v1.1 + 54 (γ-c) decision
- governance-preconditions §4 + provider-agnostic-memory-skill-design §4.4 + ADR-011 §2.1 + ADR-012 §2.3~§3.4
- 실 repo PoC 시제 (secret_scanner.py + jsonl_hash_chain.py + canonical_json.py + 5 workflows + tests/canonical 72)

---

## §10 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

1. **본 brief v1 commit** (사용자 승인 후)
2. **합의 진입** (풀 3+1 + 외부 LLM 1+ (E-α 권고) — 사용자 명시)
3. **brief v1.1 흡수** (BLOCKING/권고 1pass, ceremony-inflation 차단)
4. **SESSION + INDEX commit + push** (57 entry 등록) → **R-4 / L-4 / W 보존우선 수단 결정 발효**
5. **(다음 cycle, 사용자 명시)**:
   - **실 구현 sub-cycle** (조건부 승인 조건 6: denyNonFastForwards 활성화 + R-6 actual run + 4 G4 workflow run + violation_type 정밀화 + history_rewrite fixture + Layer subsection 분리)
   - Layer 1+2+4 통합 PASS 발효 합의 → MVP-2 Implementation Evidence PASS 발효 합의
   - R-S1 cross-reference 정정 cycle (RT-γ-6, MVP-2 PASS 전 hard gate 3 옵션)
   - R-1 Hermes import / R-2 facade real (TR-1) = 별도 trajectory

본 brief 합의는 다음 단계 진입을 *발생시키지 않음* — 사용자 명시 의무.

---

## §11 cross-reference 답습

- ADR-011 §2.1 (a)~(e) (수단/목적 분리 모법) — `docs/decisions/ADR-011-means-vs-ends-redaction.md`
- ADR-012 §2.1 (의존성 추가 PoC 재실행) + §2.3 + §2.5 + §2.7 + §2.8 + §3.4 — `docs/decisions/ADR-012-evidence-ledger-protection.md`
- governance-preconditions.md §4 (GP-2) — `docs/architecture/governance-preconditions.md`
- provider-agnostic-memory-skill-design.md §4.4 (Layer 1~5) — `docs/architecture/provider-agnostic-memory-skill-design.md`
- 51 audit brief — `docs/phase0/mvp2-entry-eligibility-audit-brief.md`
- 52 (α) entry brief v1.1 — `docs/phase0/mvp2-entry-brief.md`
- 53 (γ) layer separation brief — `docs/phase0/mvp2-gamma-layer-separation-brief.md`
- 54 (γ-c) decision brief — `docs/phase0/mvp2-gamma-decision-brief.md`
- 55 Layer 124 PASS brief v1.1 — `docs/phase0/mvp2-layer-124-pass-entry-brief.md`
- redaction-pattern-equivalence.md (R-4) + r4-1-trigger-extension-evidence.md (R-4.1) + g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md (Group D PoC)
- 실 repo PoC: `tools/secret_scanner.py` + `tools/jsonl_hash_chain.py` + `tools/canonical_json.py` + `.github/workflows/{secret-hygiene-egress-redaction,g4-hash-chain,history-anchor-verifier,rewrite-defense,r2-canary}.yml` + `tests/canonical/` 72 files

---

## §12 자기진단 (메타 편향 회피)

| # | 위험 | 본 brief 의 처리 |
|---|------|--------------|
| P-1 | 본 brief 가 R-4/L-4/W 권고를 사용자 결정 영역에 *기정사실화* | "권고 ≠ 결정" — 발효 = 풀 3+1 + 외부 LLM + 사용자 명시 후 (§5.2 + §10) |
| P-2 | 51 audit W-A 권고 vs 실 repo 현 상태 tension 을 본 brief 작성자가 *임의 재해석* | §4.1 tension 명시 + §4.2 "명칭상 W-A(ii), 실질 보존 우선" 투명 + 풀 3+1 검증 영역 (§6.3) |
| P-3 | R-3 시제 충족 발견이 GP-2 PASS *단순화* (R-1/R-2 cross-trajectory 의존 은폐) | §2.2 #2 + §5.1 cross-trajectory 명시 + RT-R-2 (defense-in-depth 약화 trigger) |
| P-4 | L-1 stdlib 권고가 RFC 8785 strict 정합 *과소평가* | §3.2 #3 fallback 동등성 + corpus 72 files + RT-L-2 (mismatch trigger) |
| P-5 | 본 brief 작성자 = 51/52/55 brief 작성자 (Claude Opus 4.7) → cascade risk | §1.1 선행 권위 답습 + cross-vendor (E-α) codex 호출로 독립 검증 (55 동형) |
| P-6 | "수단 결정 cycle" 이 실 구현 자동 진입 유발 | §0.2 #23 + §10 "자동 진입 0건, 사용자 명시 의무" |
| P-7 | (γ-c) 특화 의무 4 (Layer subsection / 부분 답습 framing) 위반 risk | §1.3 + §4.3 정합 확인 (Layer 3+5 진입 0, 통합 동시 발효 저해 0) |

---

**본 brief v1 끝.**

**다음 단계**: 사용자 승인 → 합의 진입 (풀 3+1 + 외부 LLM 1+, (E-α) 권고) → brief v1.1 흡수 → SESSION + INDEX commit + push (57 entry) → R-4 / L-4 / W 보존우선 수단 결정 발효.

exec
/bin/bash -lc "sed -n '1,220p' docs/phase0/mvp2-gamma-decision-brief.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
# (γ-c) 채택 결정 decision brief (v1)

> **작성**: 2026-05-28 (54번째 entry 진입 cycle)
>
> **scope**: (γ) 4 대안 中 **(γ-c) Layer 1+2+4 동시 채택 결정 발효** 한정 (53 entry Reviewer 통합 권고 답습)
>
> **본 cycle = 작은 영역** (1-agent 직접, Reviewer 통합 권고 답습 한정, ceremony-inflation 차단)
>
> **본 cycle 발효 자격** = **1-agent 직접 합의 + 사용자 명시 결정** + 5/5 풀 3+1 승격 trigger 0건 자체 검증
>
> **본 cycle 발효 효과** = (γ-c) Layer 1+2+4 동시 채택 결정 발효 + 후속 Layer 1+2+4 통합 PASS 격상 cycle 진입 자격 발효 (구현 발효 ≠ 본 합의)

---

## §0 본 brief 의 범위

### §0.1 사용자 진입 명령 답습 (carry-over from 53 entry, commit `f5cf584`)

53 entry `mvp2-gamma-layer-separation-brief.md` (v1.1) §8.1 다음 단계 항목 1:
- **(γ) 4 대안 中 채택 결정** — Reviewer 통합 권고 ((γ-c) 1순위 + (γ-a) 2순위) 답습 + 사용자 명시 결정 (별도 cycle)

본 cycle 진입 사용자 명시 (2026-05-28, 53 entry commit `f5cf584` push 후):
- **대안 선택**: **(γ-c) Layer 1+2+4 동시** (Reviewer 통합 권고 1순위 답습, 4 source consensus)
- **합의 형태**: **1-agent 직접** (Reviewer 권고 답습 한정, ceremony-inflation 차단)

본 brief = (γ-c) 채택 결정 영역 한정. (β) sub-수단 결정 + Layer 1+2+4 통합 PASS 격상 + 실 구현 = 후속 별도 cycle.

### §0.2 본 brief 가 *하는* 것

1. (γ-c) 채택 결정 발효 정당성 (53 entry Reviewer 통합 권고 + 4 source consensus 답습 cross-check) (§1)
2. (γ-c) 채택 결정 발효 효과 명문 (Layer 1+2+4 통합 PASS 격상 cycle 진입 자격 발효) (§2)
3. 5/5 풀 3+1 승격 trigger 0건 발화 자체 검증 (1-agent 직접 적격성) (§3)
4. 후속 cycle 진입 자격 + 금지 사항 (§4 + §5)
5. 답습 참조 (§6)

### §0.3 본 brief 가 *하지 않는* 것

| # | 영역 | 위반 시점 |
|---|------|----------|
| 1 | 실 코드 / runtime code 구현 | 0건 |
| 2 | `tools/` / `tests/canonical/` / `.github/workflows/` 본문 변경 | 0건 (PoC 시제 답습 보존) |
| 3 | ledger 첫 entry (genesis hash) 작성 | 0건 |
| 4 | Layer 1+2+4 통합 PASS 격상 sub-cycle 자동 진입 | 0건 (사용자 명시 의무) |
| 5 | (β) sub-수단 결정 cycle 자동 진입 (R-1~R-5 + L-1~L-5 + W-A~E) | 0건 |
| 6 | 외부 library 도입 결정 | 0건 |
| 7 | threshold 고정 | 0건 |
| 8 | MVP-2 Implementation Evidence PASS 발효 | 0건 |
| 9 | MVP-1 PASS 재선언 | 0건 |
| 10 | Operational Readiness PASS / Hermes PMO 격상 | 0건 |
| 11 | ADR / 헌법 / roadmap / governance / G4 / ADR-012 본문 갱신 | 0건 |
| 12 | G4 §4.4 Layer 3 (Signed commit) + Layer 5 (External anchor) 영역 진입 결정 | 0건 (본 (γ-c) = Layer 1+2+4 한정) |
| 13 | (γ-a/b/d) 대안 재평가 | 0건 (Reviewer 통합 권고 답습 한정) |
| 14 | (γ-e/f/g) hybrid 대안 결정 | 0건 (53 entry B-8 답습, 별도 cycle) |
| 15 | R-S1 cross-reference 정정 자동 진입 (ADR-012 §2.3 vs §2.8) | 0건 (별도 cycle, RT-γ-6 답습) |
| 16 | `adapters/llm/facade.py` placeholder → real 본문 (TR-1) | 0건 (별도 trajectory) |
| 17 | Hermes upstream `agent/redact.py` 본 repo 內 import 결정 | 0건 |
| 18 | branch protection contexts 자동 추가 | 0건 (사용자 admin scope 영역) |
| 19 | Tier-2/3 vendor catalog 본문 확장 | 0건 |
| 20 | GP-1/GP-4/GP-6/G3/G4 (Layer 4 외) 영역 진입 결정 | 0건 |
| 21 | 본 brief 자체 영구화 / 권위 chain 등재 | 0건 |

### §0.4 본 brief 의 권위 한계

- ✅ 본 brief 발효 자격 = **1-agent 직접 합의 + 사용자 명시 결정** + 5/5 풀 3+1 승격 trigger 0건 자체 검증
- ✅ 본 brief 발효 결과 = **(γ-c) Layer 1+2+4 동시 채택 결정 발효** + 후속 Layer 1+2+4 통합 PASS 격상 cycle 진입 자격 발효 + (γ-c) 특화 의무 명문 ((γ-c) PASS evidence template Layer 1/2/4 subsection 강제 + "부분 답습" framing 영구 유지)
- ❌ 본 brief 자체에서 sub-수단 결정 (L-1~L-5 + R-1~R-5) 0건
- ❌ 본 brief 자체에서 Layer 1+2+4 통합 PASS 격상 sub-cycle 자동 진입 0건
- ❌ 본 brief 자체에서 실 구현 0건
- ❌ 본 brief 자체에서 MVP-2 Implementation Evidence PASS 발효 0건
- ⚠️ 본 brief 합의 후 *자동 sub-cycle 진입 금지* — 사용자 명시 결정 의무

---

## §1 (γ-c) 채택 결정 발효 정당성

### §1.1 Reviewer 통합 권고 답습 (53 entry §1 답습)

53 entry `3plus1-consensus-2026-05-28-mvp2-gamma.md` §1.4 (4 source 권고 순위 cross-vendor confirm):

| 대안 | codex 권고 | Agent A 권고 | Agent B | Agent C | Reviewer 통합 |
|------|---------|---------|---------|---------|------------|
| **(γ-c) Layer 1+2+4 동시** | **1순위** | **1순위** | (부분 답습 정정 후 권고) | (R-C-3 framing fragile 경고) | **1순위 (3/4 source consensus + Agent B 부분)** |
| (γ-a) 단계적 | 2순위 | 2순위 | (정합) | (정합) | 2순위 (4/4 consensus) |
| (γ-b) 단독 | 3순위 | 3순위 | (evidence 분리 risk) | (정합) | 3순위 |
| (γ-d) 분리 | 비권고 | 비권고 | 비권고 | 비권고 | 비권고 (5 source 모순 CONFIRMED) |

→ **(γ-c) 1순위 = 4 source consensus (3/4 직접 명시 + Agent B 부분 답습 정정 후 권고)**.

### §1.2 (γ-c) 채택 결정 발효 근거

| 근거 | 답습 |
|------|----|
| 4 source consensus 1순위 | codex §6 + Agent A §6 + Agent B (부분 답습 정정 후 권고) + Reviewer 통합 §1.4 |
| ADR-011 §2.1 (a)~(d) + (e) 5조건 충족 정합 | 53 entry §3 매트릭스 — (γ-c) 모든 조건 충족 정합 |
| PoC 시제 답습 충실 | 53 entry §2.5 + Agent A filesystem direct inspection 5 PoC 영역 size verify (tools/jsonl_hash_chain.py 14038B + canonical_json.py 10055B + tests/canonical 8 카테고리 + g4-hash-chain.yml 10652B 7 step + 3 보조 workflow) |
| defense-in-depth 부분 답습 정합 | 53 entry §2.3.2 + B-6 흡수 — Layer 1+2+4 한정 (Layer 3+5 = scope 외) |
| 합의 cycle 효율 | 1 cycle 등가 (Layer 1+2+4 동시 PASS evidence 분리) vs (γ-a) 4 cycle |
| ceremony-inflation 차단 | (γ-a) 4 cycle 대비 (γ-c) 3 cycle 등가 |
| (γ-d) 모순 회피 | 5 source verify CONFIRMED (53 entry §4.4) — (γ-d) 비권고 정합 |
| 사용자 명시 결정 | 2026-05-28, AskUserQuestion (γ-c) Recommended 답습 |

### §1.3 (γ-c) 특화 의무 명문 (53 entry N-1 + B-6 답습 + 영구 유지)

본 (γ-c) 채택 결정 발효 시 다음 의무 영구 유지:

1. **PASS evidence template Layer 1/Layer 2/Layer 4 subsection 강제** (53 entry N-1 흡수 답습)
   - Layer 1 (hash chain) evidence + Layer 2 (Git append-only) evidence + Layer 4 (CI 회귀 검증) evidence 각각 분리 명시
   - Layer 4 evidence 內 Layer 1+2 evidence 합산 금지 ((γ-b) risk 회피)
2. **"defense-in-depth 부분 답습" framing 영구 유지** (53 entry B-6 흡수 답습)
   - "부분 답습" 표현 = Layer 1+2+4 한정, Layer 3 (Signed commit) + Layer 5 (External anchor) = 본 cycle scope 외
   - "충실 답습" 또는 "완전 답습" 표현 금지 영구
3. **Layer 1+2+4 통합 PASS evidence 동시 발효** ((γ-a) 단계적 vs (γ-c) 통합 차이)
4. **R-S1 후행 영향 RT-γ-6 답습** (53 entry §5.1 답습) — Layer 1+2+4 통합 PASS 발효 시 R-S1 정정 영향 평가 의무

---

## §2 (γ-c) 채택 결정 발효 효과

### §2.1 본 cycle 발효 효과

본 (γ-c) 채택 결정 발효 시:

1. **(γ-c) Layer 1+2+4 동시 채택 결정 발효** — (γ-a/b/d) 대안 = 비채택 (Reviewer 통합 권고 답습 한정)
2. **Layer 1+2+4 통합 PASS 격상 cycle 진입 자격 발효** — 후속 sub-cycle 진입 권한 (사용자 명시 의무)
3. **(γ-c) 특화 의무 영구 유지 발효** (§1.3 답습)
4. **(γ-d) 비권고 + Layer 4 PASS 선발효 금지 명문 답습 보존** (53 entry §2.4.5 + B-1 답습)

### §2.2 본 cycle 발효 *하지 않는* 영역

§0.3 답습 (21 항목). 핵심:
- ❌ Layer 1+2+4 통합 PASS 격상 sub-cycle 자동 진입 (사용자 명시 의무)
- ❌ (β) sub-수단 결정 cycle 자동 진입
- ❌ 실 구현 / MVP-2 Implementation Evidence PASS 발효
- ❌ (γ-e/f/g) hybrid 대안 결정 (B-8 답습)

---

## §3 5/5 풀 3+1 승격 trigger 0건 발화 자체 검증 (1-agent 직접 적격성)

본 §3 = 본 cycle 1-agent 직접 합의 적격성 자체 검증 (Reviewer 통합 권고 답습 한정 = ceremony-inflation 차단).

| # | trigger | 본 cycle 발화 | 근거 |
|---|---------|---------|------|
| 1 | 큰 결정 (신규 영역 결정 / 수단 결정 / threshold 고정) | ❌ 미발화 | (γ-c) 채택 결정 = Reviewer 통합 권고 답습 한정 (53 entry 4 source consensus 발효 답습). 신규 영역 결정 0 / 수단 결정 0 |
| 2 | 아키텍처 / SDD / 보안 본문 변경 | ❌ 미발화 | brief = phase0 신규 1 파일 + SESSION + INDEX, 본문 변경 0 |
| 3 | ADR 본문 변경 | ❌ 미발화 | brief = ADR 본문 0 |
| 4 | 권위 chain 다중 source 손상 위험 | ❌ 미발화 | R-S1 = 52/53 entry 발견 + RT-γ-6 답습 (별도 cycle, 본 cycle scope 외) |
| 5 | 외부 LLM 응답 통합 필요성 | ❌ 미발화 | 본 cycle = Reviewer 통합 권고 답습 한정, 외부 LLM 응답 = 53 entry codex 이미 발효 (재호출 불필요) |
| 6 | Tier-2/3 catalog 자동 확장 | ❌ 미발화 | §0.3 #19 명시 금지 |
| 7 | Hermes PMO 격상 | ❌ 미발화 | §0.3 명시 금지 |

→ **0/7 발화 → 1-agent 직접 합의 적격 (Reviewer 통합 권고 답습 한정, ceremony-inflation 차단 메모리 답습)**.

---

## §4 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

본 (γ-c) 채택 결정 발효 후 (사용자 명시 의무):

1. **(β) sub-수단 결정 cycle** — R-1~R-5 (GP-2) + L-1~L-5 (G4 §4.4 Layer 4) + W-A~E — 풀 3+1 (수단별 차등)
2. **Layer 1+2+4 통합 PASS 격상 cycle** — Layer 1 hash chain + Layer 2 Git append-only + Layer 4 CI 회귀 검증 동시 PASS evidence (각 layer subsection 분리 강제, §1.3 답습) — 풀 3+1 + 외부 LLM 1+
3. **실 구현 sub-cycle** ((β) + (γ-c) 채택 후) — Hermes upstream `agent/redact.py` 영역 + 본 repo P1 facade RedactionFilter (TR-1 (d) carry-over 의존) + Layer 1+2+4 PoC → PASS + R-6 workflow 확장 step (Layer 2a `denyNonFastForwards` 활성화 evidence 별도 verify 의무, 53 entry B-3 답습)
4. **MVP-2 Implementation Evidence PASS 발효 합의** — (a)~(d) 4조건 evidence + (e) 후속 운영조건 + 사용자 명시 + RT-γ-6 R-S1 PASS 시점 선행/동시 정정 평가 (32 entry 답습 패턴)
5. **(γ-e/f/g) hybrid 대안 결정 cycle** (53 entry B-8 답습, 선택) — 본 (γ-c) 채택 결정 후 hybrid 영역 검토 가능
6. **R-S1 cross-reference 정정 cycle** — ADR-012 §2.3 본문 정정 또는 §2.8 동형 답습 강화 (RT-γ-6 답습)
7. **ADR 본문 cross-reference 갱신 별도 commit** — ADR-008/012/011

본 brief 합의는 다음 단계 진입을 *발생시키지 않음* — 사용자 명시 의무.

---

## §5 금지 사항

§0.3 답습 (21 항목). 핵심 강화:

| # | 금지 영역 | 의무 답습 |
|---|---------|---------|
| 1 | 자동 Layer 1+2+4 통합 PASS 격상 sub-cycle 진입 | 사용자 명시 의무 |
| 2 | 자동 (β) sub-수단 결정 cycle 진입 | 사용자 명시 의무 |
| 3 | Layer 4 PASS 선발효 ((γ-d) 모순 답습) | 영구 금지 (53 entry §2.4.5 + B-1 답습) |
| 4 | (γ-a/b/d) 대안 재평가 자동 진입 | 본 (γ-c) 채택 결정 영구 발효 (재평가 = 별도 cycle 사용자 명시) |
| 5 | (γ-e/f/g) hybrid 대안 결정 자동 진입 | 사용자 명시 의무 |
| 6 | R-S1 cross-reference 정정 자동 진입 | 별도 cycle (RT-γ-6 답습) |
| 7 | Layer 3 (Signed commit) + Layer 5 (External anchor) 자동 진입 | 별도 cycle ("부분 답습" framing 영구 유지) |
| 8 | "defense-in-depth 충실 답습" 또는 "완전 답습" 표현 사용 | 영구 금지 (§1.3 (γ-c) 특화 의무 답습) |
| 9 | Layer 4 evidence 內 Layer 1+2 evidence 합산 | 영구 금지 (PASS evidence template Layer subsection 강제 §1.3 답습) |

---

## §6 답습 참조

### §6.1 상위 권위

- 헌법 제8조 (보안) — `docs/constitution/PROJECT_CONSTITUTION.md`
- 헌법 제5조-2 (Provider Liquidity 비협상) — 동상
- ADR-011 §2.1 (a)~(d) 4조건 모법 + §3 후속 권위 (e) — `docs/decisions/ADR-011-means-vs-ends-redaction.md`

### §6.2 직접 선행 자료

- 53 entry (γ) brief v1.1 — `docs/phase0/mvp2-gamma-layer-separation-brief.md` (522줄)
- 53 entry Reviewer 통합 합의 — `docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md` (264줄, APPROVE WITH CONDITIONS, BLOCKING 8 + 권고 16, (γ-c) 1순위 + (γ-a) 2순위 + (γ-b) 3순위 + (γ-d) 비권고 4 source consensus)
- 53 entry codex 응답 — `docs/external-review/2026-05-28-mvp2-gamma-codex-response.md` (3284줄)
- 53 entry Agent A/B/C 응답 — `docs/review/3plus1-consensus-2026-05-28-mvp2-gamma-agent-{a,b,c}.md`
- 52 entry (α) entry brief v1.1 — `docs/phase0/mvp2-entry-brief.md`
- 52 entry Reviewer 통합 합의 — `docs/review/3plus1-consensus-2026-05-28-mvp2-entry.md`
- `provider-agnostic-memory-skill-design.md §4.4` (Layer 1~5)
- `ADR-012-evidence-ledger-protection.md §2.3 + §2.8`

### §6.3 메타 영역 (53 entry §9.3 답습)

실 repo PoC 시제:
- `tools/jsonl_hash_chain.py` (14038B, genesis hash + 4 violation_type)
- `tools/canonical_json.py` (10055B)
- `tests/canonical/` (8 카테고리 verify 충족 / 24 fixture 정량 = 52 entry carry-over)
- `.github/workflows/g4-hash-chain.yml` (10652B, 7 step 분리)
- `.github/workflows/history-anchor-verifier.yml` (19094B)
- `.github/workflows/rewrite-defense.yml` (16454B)
- `.github/workflows/r2-canary.yml` (5476B)

### §6.4 cross-reference 갱신 영역 (별도 commit, 본 cycle scope 외)

exec
/bin/bash -lc "sed -n '1,220p' docs/decisions/ADR-011-means-vs-ends-redaction.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
# ADR-011: Means-vs-Ends Redaction Principle (수단/목적 분리 원칙)

**상태**: 승인 (단축 합의 — Reviewer-only, 2026-05-06)
**날짜**: 2026-05-06
**의사결정자**: 사용자 + Reviewer 합의 — `docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md`
**상위 권위**: 헌법 제8조 (보안), 헌법 제5조-2 (Provider Liquidity, 비협상), `docs/architecture/system-identity-prequel.md` §3
**갱신 대상**: ADR-008 부록 B Amendment (동시 발행)
**모법 역할**: R-4 / R-5 / R-6 / R-7 작업의 권위 근거

---

## 1. 맥락 (Context)

### 1.1 P2 v2 가정의 붕괴

ADR-008 부록 A는 R1 (학습루프 평문 누적)을 비협상 CRITICAL 위험으로 명시했다. P2 v2 §2.1.3은 R1 차단 메커니즘으로 "외부 pre-record hook" 형태를 가정 채택했다.

Phase 0 Day 1 사실 확인(`docs/phase0/day1-environment-and-fact-check.md`)에서 Hermes v0.12.0 main HEAD에 `pre_record` / `add_pre_record_hook` / `before_record` API가 존재하지 않음이 grep 0건으로 확정되었다 (15종 `VALID_HOOKS` 중 DB 기록 직전 가로채기 hook 0개).

### 1.2 Phase 0 R-1 / R-2 evidence

- **R-1 검증**(`docs/phase0/day2-r1-redaction-location-verification.md`): Hermes 자체 redaction(`agent/redact.py`)이 LLM 송신/도구 출력/로깅 전용이고 DB INSERT 경로 미적용 확정 → **G1a FAIL**.
  - `agent/redact.py:1-8` docstring 명시: "Regex-based secret redaction for logs and tool output"
  - redact 모듈 import 25개 모두 비-DB 경로
  - `hermes_state.py` (SessionDB) redact import 0건

- **R-2 PoC**(`docs/phase0/day3-r2-sqlite-trigger-poc.md`): SQLCipher BEFORE INSERT trigger + REGEXP UDF 조합이 Docker 격리 환경(network_mode: none + read_only + cap_drop ALL)에서 6항목 모두 PASS → **G1b PASS by R-2 PoC**.

### 1.3 ADR 권위 해석 요청 사항

위 결과는 다음 질문에 대한 ADR 권위 해석을 요구한다:

> **R1의 "비협상" 본질은 무엇인가 — 특정 구현 수단인가, 보안 결과인가?**

본 ADR은 이 질문에 답하고, 동시에 다음 3개 인접 안건을 ADR 권위로 정착한다:
- G1a/G1b 게이트 분리 공식화
- "Hermes ≠ root of trust" 권위 위계 영구화 (prequel §3 → ADR 승격)
- 자동 학습 vs 자동 정책 변경 분리

---

## 2. 결정 (Decision)

본 ADR은 다음 4가지를 권위로 선언한다.

### 2.1 수단/목적 분리 원칙 (Means-vs-Ends Separation)

**비협상 조건의 본질은 특정 구현 수단이 아니라, 달성해야 하는 안전 결과(safety outcome)이다.**

- 헌법 제8조 (보안)의 본질은 **DB 평문 저장 차단이라는 결과**이다.
- 외부 hook, redaction 호출, trigger, 암호화 등은 **수단**이다.
- 대체 수단은 다음 4조건을 **모두** 충족할 때 기존 수단을 대체할 수 있다:

  | # | 조건 | 검증 방식 |
  |---|------|---------|
  | (a) | 동등 이상의 보안 결과 | 명시적 비교표 (수단 A 보장 ↔ 수단 B 보장) |
  | (b) | 격리 환경 PoC로 실증 | Docker isolation + 자동 검증 항목 |
  | (c) | ADR 권위로 명시 | 본 ADR 또는 후속 ADR |
  | (d) | 자동 회귀 검증 경로 확보 | CI/nightly 재실행 (R-6) |

**원칙 위반**: "수단이 비협상이다"는 텍스트 해석으로 본질 회귀를 차단하는 것은 본 ADR로 무효화된다. 동시에 (a)~(d) 4조건 미충족 시 수단 대체도 금지된다 — 본 ADR은 *수단 자유*가 아니라 *목적 달성 검증 의무*를 강제한다.

### 2.2 G1a / G1b 게이트 분리 공식화

P2 v2의 단일 G1 게이트는 본 ADR로 다음 두 게이트로 분해된다.

```
G1a: Hermes native redaction applies before DB INSERT
   Result: FAIL (R-1 확정)
   Evidence: agent/redact.py docstring "for logs and tool output",
             redact import 25개 모두 비-DB,
             hermes_state.py redact import 0건
   Status: 폐기 (이 경로로 헌법 8조 충족 시도 금지)

G1b: DB-level fallback prevents plaintext secret persistence
   Result: PASS by R-2 PoC
   Evidence: Docker 격리 환경 (network_mode: none + read_only + cap_drop ALL)
             + SQLCipher BEFORE INSERT trigger + REGEXP UDF
             + 6항목 자동 검증 (C1~C6 모두 PASS)
   Status: PoC PASS, 정식 충족은 R-3~R-5 완료 후
```

#### G1b 정식 충족 조건 (Phase 1 차단조건 #1 exit 기준)

| # | 조건 | 산출 |
|---|------|------|
| R-3 | 본 ADR-011 발행 + ADR-008 Amendment | `ADR-011`, `ADR-008` 부록 B |
| R-4 | Hermes redact pattern ↔ P1_REDACTOR 패턴 동등성 검증, gap 발견 시 trigger UDF 보충 | `docs/architecture/redaction-pattern-equivalence.md` |
| R-5 | canary 재검증 트리거 설계 (T13 강화 — config + 주기적 inject) | `docs/architecture/canary-recheck-design.md` |
| R-6 | CI/nightly 회귀 검증 (Hermes 업그레이드 자동 R-2 재실행) | `.github/workflows/r2-canary.yml` |
| R-7 | Phase 1 합격 SOP (canary 패턴/주입/검증/PASS·FAIL 기준) | `docs/phase0/redaction-verification-sop.md` |

R-3~R-7 모두 완료 시 G1b는 PoC 단계를 벗어나 Phase 1 차단조건 #1 정식 exit 기준이 된다.

### 2.3 Hermes ≠ Root of Trust

**Hermes는 시스템의 최종 신뢰 근거가 아니라 검증 대상이다.**

#### 권위 위계 (Authority Hierarchy)

```
Constitution
  > ADR
  > SDD
  > Harness Gates
  > Hermes
  > Worker Agents
```

#### 운영 함의 (Operational Implications)

1. **Hermes 출력은 Tools로 검증된다**: 린터/타입체커/테스트/trigger/canary가 Hermes 출력 위에 위치한다.
2. **Hermes 자체 redaction은 로그/LLM 송신 방어로만 신뢰**: 저장 경로(DB/파일) 차단 책임 없음.
3. **DB INSERT 경로는 Hermes 외부에서 별도 보호**: SQLCipher trigger 기반 fallback (G1b).
4. **Hermes 의존성 업그레이드는 자동 R-2 재실행으로 회귀 검증**: 신뢰 경계 외부 변경의 자동 검출 (R-6).
5. **Hermes 학습 결과의 자동 정책 반영 금지**: §2.4와 결합.

#### prequel과의 관계

본 §2.3은 `docs/architecture/system-identity-prequel.md` §3 ("Hermes ≠ root of trust") 의 prequel(임시) 선언을 ADR 영구 권위로 승격한다. prequel은 R-7 완료 후 P2 v3로 흡수되며 폐기되지만, 본 ADR-011 §2.3은 영구 유지된다.

### 2.4 자동 학습과 자동 정책 변경 분리

- **자동 학습은 허용**: Worker Agent가 도구 사용/패턴/실패 사례를 누적 학습하는 것은 시스템 가치의 핵심.
- **자동 정책 변경은 금지**: Constitution / ADR / Harness Gates / Hermes 설정의 변경은 사용자 승인 경로(3+1 합의 또는 단축 합의)를 거쳐야 한다.

#### 3-tier 분류 (T1 / T2 / T3)

| Tier | 정의 | 예시 | 승인 경로 |
|------|------|------|---------|
| **T1** | 자동 허용 | Worker Agent 패턴 학습, 도구 사용 빈도 누적, 실패 회피 휴리스틱 | 자동 |
| **T2** | 사용자 승인 필수 | Skill/Memory promotion, 새 도구 등록, 합의 형태 결정 | 사용자 명시 결정 |
| **T3** | 자동 금지 (절대) | Constitution / ADR / Harness Gates 정의 자체의 변경 | 단축 또는 풀 3+1 합의 |

본 분리는 prequel §6의 3-tier 선언을 ADR 권위로 승격한 것이며, R-5 (canary 재검증) / R-6 (CI 회귀)의 권위 근거이기도 하다 — Hermes 내부 학습 또는 upstream 변경으로 redaction 동작이 silent 깨짐 발생 가능성을 자동 검증으로 차단.

---

## 3. R-4 ~ R-7 모법 역할 (Governing Precedent)

본 ADR은 다음 후속 작업의 권위 근거로 기능한다.

| 작업 | 산출 | 본 ADR §과의 관계 |
|------|------|----------------|
| **R-4** | `docs/architecture/redaction-pattern-equivalence.md` | §2.1 (a) — 대체 수단(R-2 trigger)이 기존 수단(Hermes redaction) 대비 패턴 커버리지 동등 이상임을 명시적 비교표로 실증 |
| **R-5** | `docs/architecture/canary-recheck-design.md` | §2.4 — Hermes 학습 또는 upstream 변경으로 redaction silent 깨짐 발생 가능성 자동 검증 + §2.3 운영 함의 #4 구현 |
| **R-6** | `.github/workflows/r2-canary.yml` | §2.1 (d) + §2.3 — Hermes 의존성 업그레이드의 자동 회귀 검증 |
| **R-7** | `docs/phase0/redaction-verification-sop.md` | §2.2 G1b 정식 충족 절차의 SOP화 |

후속 작업은 본 ADR §2를 명시 인용하고, 본 ADR 위반(예: "수단이 비협상이다" 텍스트 회귀, T3 자동 변경 시도) 시 단축 합의 + ADR Amendment 절차로만 갱신 가능하다.

---

## 4. 선택지 (Options Considered)

### 옵션 A: ADR-011 단독 (Amendment 없음)

- 장점: 일반 원칙 ADR 단일 산출 — 작성 부담 최소
- 단점: ADR-008 부록 A R1 표면 텍스트("외부 pre-record hook 공식 지원")가 갱신되지 않아 ADR-008 본문과 ADR-011 사이 표면 모순. 이력 추적 시 혼란.

### 옵션 B: ADR-008 Amendment 단독 (ADR-011 없음)

- 장점: ADR-008 한 문서로 일관
- 단점:
  - "수단/목적 분리"는 R1을 넘어선 일반 원칙 — Amendment에 일반 원칙을 담는 것은 Amendment 형식 위반
  - "Hermes ≠ root of trust" 운영 ADR화는 ADR-008 (Hermes 도입 결정) 범위 초과
  - R-4~R-7이 Amendment를 권위 근거로 인용하는 것은 비표준 (Amendment는 specific 갱신 한정)

### 옵션 C: ADR-011 신규 + ADR-008 Amendment ⭐ **채택**

- 장점:
  - 일반 원칙(수단/목적 분리, G1a/G1b 분리, Hermes ≠ root of trust, 학습/정책 분리)은 ADR-011로 권위화
  - ADR-008 부록 A R1 specific 갱신은 Amendment로 짧게 처리 + ADR-011 cross-reference
  - R-4~R-7이 ADR-011을 명확한 모법으로 인용
  - ADR-008 본문 read 시 즉시 R-1 FAIL 후 갱신 사항 파악 가능
- 단점: 작성 분량 2배 (수용)

---

## 5. 근거 (Rationale)

### 5.1 헌법 제8조 본질 재해석의 정당성

헌법 제8조의 비협상 본질은 "특정 hook이 존재해야 함"이 아니라 "비밀이 평문 영구 저장되지 않음"이다. R-2 PoC는 SQLCipher trigger 기반 fallback이 이 본질을 충족함을 실증했다.

수단을 비협상으로 굳히면, 수단이 부재한 시점(현 Hermes v0.12.0)에 헌법 제8조 자체를 충족할 수 없는 모순이 발생한다. 본 ADR은 이 모순을 수단/목적 분리로 해소하되, 동시에 (a)~(d) 4조건으로 자의적 수단 대체를 차단한다.

### 5.2 "Hermes ≠ root of trust" ADR 권위화 필요성

system-identity-prequel은 임시 선언(Pre-Declaration)으로, R-7 완료 후 P2 v3 흡수와 함께 폐기된다. 그러나 "Hermes ≠ root of trust"는 폐기되어서는 안 되는 영구 권위 원칙이다. 본 ADR-011 §2.3으로 권위 승격하여 prequel 폐기 후에도 보존한다.

### 5.3 G1a/G1b 분리의 영구화 필요성

R-1 FAIL과 R-2 PASS는 Phase 0 evidence 보고서에 기록되어 있으나, 이는 보고서이지 ADR 권위가 아니다. G1a/G1b 분리를 ADR로 권위화하지 않으면 미래 합의에서 "G1 단일 게이트로 회귀 가능" 해석 위험이 발생한다. 본 ADR §2.2가 이를 차단한다.

### 5.4 단축 합의(Reviewer-only)의 정당성

본 R-3은 새 설계 안건이 아니라 R-1 FAIL + R-2 PASS + 단축 합의 §R-3 (`docs/review/3plus1-consensus-2026-05-05-p2-n1-redaction-reinterpretation.md`) + 풀 합의 §3 권위 위계 (`docs/review/3plus1-consensus-2026-05-05-system-identity-redefinition.md`) 의 ADR 형식화 작업이다. 새 합의 검증이 아니므로 풀 3+1은 과잉. 직전 R-1 단축 합의 패턴 답습.

---

## 6. 합의 결과 (단축 합의 — Reviewer-only)

세부: `docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md`

| 차원 | 판정 | 핵심 근거 |
|------|------|---------|
| 헌법 제8조 본질 충족 권위화 | **PASS** | §2.1 수단/목적 분리 + (a)~(d) 4조건 명시로 자의적 회귀·자의적 수단 대체 양방향 차단 |
| G1a/G1b 분리 공식화 | **PASS** | R-1 FAIL evidence + R-2 PASS evidence 모두 인용, 정식 충족 조건 명시 |
| Hermes ≠ root of trust 권위 승격 | **PASS** | prequel §3 → ADR §2.3 영구화, 운영 함의 5항목 명문화 |
| 자동 학습 vs 정책 변경 분리 | **PASS** | T1/T2/T3 3-tier 분류 본문 흡수, R-5/R-6 권위 근거화 |
| Provider Liquidity 영향 | **무관** | 본 ADR은 redaction 수단 해석이며 모델/구독 교체 자유와 무관 |
| 메타 편향 통제 | **명시** | 본 ADR은 자체 코드 우호 결론(R-2 PASS)을 반영하나, (a)~(d) 4조건과 R-4~R-7 모법으로 회귀 견제 — 합의 보고서 §메타 편향 자기진단 참조 |

---

## 7. 결과 (Consequences)

### 7.1 긍정적


exec
/bin/bash -lc "sed -n '1,280p' docs/decisions/ADR-012-evidence-ledger-protection.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
# ADR-012: Evidence Ledger Protection (Evidence Ledger 보호 강화)

**상태**: 승인 (풀 3+1 + 외부 LLM 2건 — 2026-05-09)
**날짜**: 2026-05-09
**의사결정자**: 사용자 + Reviewer 종합 합의 — `docs/review/3plus1-consensus-2026-05-09-pr2-evidence-ledger.md`
**상위 권위**: 헌법 제8조 (보안), 헌법 제5조 (Provider Liquidity, 관용), ADR-011 §2.1 (수단/목적 분리), §2.3 (Hermes ≠ root of trust), §2.4 (T1/T2/T3)
**모법 ADR**: ADR-011 (Means-vs-Ends Redaction Principle)
**갱신 대상**: G4 §4.2 schema (10 → 11 필드), G4 §4.4 hash chain 사양 보강, G4 §4.6 round-trip 검증 절차 보강 (동일 PR — `provider-agnostic-memory-skill-design.md`)
**P10 트리거**: 본 ADR-012 발행 시점 = G2 §1.2.5 P10 (Evidence Forgery) 정식 등록 *트리거* (정식 row 추가는 별도 G2 update PR — 본 ADR 범위 외)
**합의 권위**: `docs/review/3plus1-consensus-2026-05-09-pr2-evidence-ledger.md` (5/5 입력 APPROVE WITH CONDITIONS — Agent A/B/C + cross-vendor 외부 LLM + Claude 인접 컨텍스트)

**[Cross-reference Block — (g1-N-3-adr-008+sip+adr-012') R-7 (f) cross-ref block 만 채택 + R-S4 답습 + R-1 (P4) 신설 *기각* 답습]**: 본 ADR-012 line 6 (상위 권위) + line 61 (§1.4 cross-ref 표 cell) + line 579 (영구 핵심 제약 표) + line 665 (관련 문서) 표기 "헌법 제5조 (Provider Liquidity, 관용)" / "헌법 제5조 관용" / "헌법 5조 (관용)" = (g1-N-1) commit `148fbbe` 후 **헌법 제5조-2: Provider Liquidity 원칙 (비협상) (line 75~80)** 직접 모법 발효 — (g1-N-1) 이전 관용 표현 답습. **line 61 = (P2) cross-ref 표 cell 처리** ((P4) 신규 verbatim 유형 신설 *기각* — R-1 + 기각-2 답습, Reviewer 권한 한계 (11) sub-boundary 신설 *기각*). 본 cycle = gov §1.1 line 78 verbatim 명문 4 source *외* 추가 동형 source 자격 식별 (R-S4 HIGH, ADR-012 = 명문 4 source 외 추가 동형 매핑 자격 강함). (g1-N-3-pamsd) `ab96e30` 동형 패턴 답습, **본문 verbatim 변경 0건** ((f) cross-ref block 만 채택). 정정 후 형식 = ADR-011 line 245 모법 "제5조-2 관용 (Provider Liquidity, 비협상)" (R-rec-3 답습 + 사용자 명시 직접 확인). 추가 위치 line 62/455/513/552/555/561/583/597 (P2 ADR-011 cross-ref + P3 "Provider Liquidity 4-way → 5-way" 본문 다수) = (P3) 본문 답습 본질 동형, 정정 자격 약함 ((P3) 약식 통일 cycle DEFER carry-over). 본 cycle 합의 = `209f04d`.

---

## 1. 맥락 (Context)

### 1.1 본 ADR 발행 트리거 (prequel §6.4 재해석)

`docs/architecture/system-identity-prequel.md` §6.4 는 "Phase 1 종료 시점에 Evidence Ledger schema 의 ADR 권위화" 를 명시했다. **본 ADR-012 는 그 트리거를 *4 게이트 Design/Governance PASS + PR-1/PR-2 묶음 안정화 시점* 으로 재해석하여 발행** (합의 보고서 §5.2 Agent C C-1 답습).

재해석 사유:
- Phase 1 acceptance PASS = 2026-05-07 (G1b PASS, R-7 SOP §7.3 단축 합의)
- G2 / G3 / G4 Design/Governance Gate PASS (Bundled) = 2026-05-09
- PR-1 6건 본문 흡수 완료 = 2026-05-09 후속 2 (`commit 750faaf`)
- 본 PR-2 = G2/G3/G4 정식 PASS 합의 §11.2 P1 조건 흡수 (C-C + C-G) — **권위 내부 작업**

### 1.2 G3 "Evidence decides" 운영 규칙의 근거 강화 필요성

`docs/architecture/hermes-not-root-of-trust-runtime.md` §5 Evidence 결정 5 운영 규칙:

```
Agent proposes.       (제안)
Hermes orchestrates.  (조율 — 격상 후)
Tools verify.         (검증 — 계산적 우선)
Evidence decides.     (결정 — 기록 없으면 PASS 미성립)
Human overrides.      (사람이 최종 방향)
```

**PASS 성립 4 요건** (G3 §5.3):
- (i) Tools 검증
- (ii) **Evidence Ledger entry** ← 본 ADR-012 보호 강화 대상
- (iii) (T2/T3) 사용자 명시 승인
- (iv) (해당 시) 합의 보고서 commit

Evidence Ledger 변조 가능성 = G3 root-of-trust 직접 훼손 → 본 ADR 권위로 보호.

### 1.3 G2 §1.2.5 P10 (Evidence Forgery) 정식 등록 트리거 명시

PR-1 §1.4 (C-I 흡수, `commit 750faaf`) 에서 G2 §1.2.5 P9~P12 deferred candidates 4건 등록:
- P9 (Prompt Injection)
- **P10 (Evidence Forgery)** ← **본 ADR-012 발행 시점 = 정식 등록 트리거** (G2 §1.2.5.2 명시)
- P11 (Supply-chain)
- P12 (Memory Poisoning Side-channel)

본 ADR-012 발행은 P10 의 *정식 위반 경로 등록 트리거*. 단 **G2 §1.2 본문 P10 row 추가는 별도 G2 update PR** (본 ADR 범위 외, 합의 §4.2 답습).

### 1.4 Cross-reference (헌법 + ADR + G + 5 영구 핵심 제약)

| 연결 대상 | 연결 사유 |
|--------|--------|
| **헌법 제8조 (보안)** | Evidence Ledger entry 자체에 평문 secret 포함 가능 (P1 변종) — GP-1 SQLCipher trigger 보호 범위에 ledger DB 명시 포함 의무 (외부 LLM 2 C-1) |
| **헌법 제5조 관용 (Provider Liquidity)** | Ledger 형식 = Hermes 의존 0 (ADR-008 차단조건 #2 답습) + provider-neutral 강제 (Provider Liquidity 4-way Multi-layer Defense → **5-way** Evidence 형식 layer 추가) |
| **ADR-011 §2.1 (수단/목적 분리)** | 본 ADR 자체가 Evidence 무결성 = 목적, hash chain + signed/append commit + JCS = 수단. (a)~(d) + (e) 5조건 답습 (§4) |
| **ADR-011 §2.3 (Hermes ≠ root of trust)** | Hermes 는 ledger entry 생성 가능 (T1 자동 학습), 단 promotion / approval 은 사용자 명시 (T2). Hash chain + signed/append commit = Hermes 변조 차단 운영 매커니즘. **본 ADR-012 는 Hermes 안전성을 선언하지 않는다** (ADR-011 §7.3 직접 답습 — 외부 LLM 2 C-15 / Agent B Gap-18) |
| **ADR-011 §2.4 (T1/T2/T3)** | prev_hash 검증 실패 자동 revert = T3 위반 위험 → BLOCK + manual review 채택 (외부 LLM 2 C-3 / Agent B C-3) |
| **ADR-008 차단조건 #2** | JSONL export 표준 — 본 ADR §2.10 흡수 |
| **ADR-010 (SQLCipher Vault)** | secret 처리 cross-reference — Evidence Ledger DB 가 secret 포함 가능 시 GP-1 보호 범위 명시 의무 |
| **G3 §1.3 + §5.3** | Evidence 결정 5 운영 규칙 + PASS 성립 4 요건 |
| **G4 §4.4 + §4.6** | Hash chain + canonical JSON + round-trip 검증 (본 ADR §2.3 + §2.5 + §2.7 + §2.8 + §2.9 와 동시 보강) |
| **system-identity-prequel §6.3** | Evidence Ledger schema 후보 권위 근거 — 본 ADR §2.2 답습 |

### 1.5 메타포 회피 명시 (외부 LLM 2 §1)

본 ADR-012 는 *형식적 무결성* (hash chain / canonical / append-only / signed) 까지만 보호. *의미적 정확성* (예: 사용자가 위조된 사실을 본인이 작성한 것처럼 ledger 에 기록) 은 본 ADR 방어 범위 외 (§11 한계 명시 답습). "Ledger 를 *불변의 진리* 로 비유" 같은 메타포 회피 — `system-identity-prequel §7` 답습.

---

## 2. 결정 (Decision)

본 ADR-012 는 다음 12 보호 원칙 + 4 매트릭스 항목 + 5 추가 의무 을 권위로 선언한다.

### 2.1 Evidence Ledger 보호 원칙 (12)

**원칙 1**: Evidence Ledger 는 PASS 의 *보조 기록* 이 아니라 **PASS 성립 조건** 이다.

**원칙 2**: Evidence 가 없으면 PASS 는 *존재하지 않는다*.

**원칙 3**: Evidence Ledger 는 Hermes 가 *승인하거나 수정* 할 수 없다 (T3 영역).

**원칙 4**: Evidence Ledger 의 변조 가능성은 G3 root-of-trust 구조를 직접 훼손한다.

**원칙 5**: Evidence Ledger 는 *Hermes 의존 0* — 모든 entry 가 표준 도구 (`jq` + `sha256sum` + 표준 라이브러리) 만으로 검증 가능 (ADR-008 차단조건 #2 답습).

**원칙 6**: Evidence Ledger entry 작성 주체는 `agent` 필드로 *provider-neutral* 식별 — `user` / `<worker_name>` / `hermes` 등.

**원칙 7**: External LLM response 적재 시 entry `agent = "user"` (수동 paste 주체) 강제 (외부 LLM 2 C-9). Hermes 가 외부 LLM response 를 자기 제안으로 위조 차단 (Gap-17 #4).

**원칙 8**: Evidence Ledger 는 *append-only* — entry 수정 / 삭제 / 재작성 금지 (T3 영역, ADR-011 §2.4).

**원칙 9**: Hash chain 검증 실패 = 즉시 BLOCK. 자동 복구 / 자동 revert 금지 (T3 위반 위험 답습).

**원칙 10**: Round-trip 검증은 tier-based — T2 (로컬 promotion) strict / T3 (cross-vendor migration) 의미 보존 + 사용자 명시 review (§2.9 답습).

**원칙 11**: Evidence Ledger 보호 범위 = *형식적 무결성* — *의미적 정확성* (content-level forgery) 은 본 ADR 방어 범위 외 (§11 답습).

**원칙 12**: 1인 동일 호스트 SPOF 한계 인지 (G3 §5.5 답습) — 동일 호스트 전체 침해는 본 ADR 의 완전 방어 범위 밖. multi-host 전환 시 Layer 3 / Layer 5 의무 발동 트리거.

### 2.2 11 필드 구조 (G4 §4.2 schema 갱신, 10 → 11 필드)

```jsonl
{
  "type": "memory|skill|meta",
  "scope": "global|project|session|team",
  "id": "<uuid-v4-or-slug>",
  "schema_version": "0.2",
  "ts": "2026-05-09T10:00:00Z",
  "agent": "user|<worker_name>|hermes",
  "event": "<event-enum>",
  "content": {...},
  "evidence_refs": ["docs/evidence/<path>.md"],
  "prev_hash": "<sha256>",
  "hash": "<sha256>"
}
```

**11번째 필드 = `event`** (4/5 합의, Agent A enumeration 결과적 일치 — 합의 §3.1).

**`event` enum 후보 (25건, MVP 의무 12건 + 후속 확장 5건 + MVP-1 신규 8건 — schema_version 0.2)**:

| # | enum | 정체성 | T 분류 |
|---|------|------|------|
| 1 | `memory_write` | Memory entry 작성 | T1 (Hermes) / T2 (사용자 promotion) |
| 2 | `skill_proposed` | Skill 후보 추출 | T1 (Hermes 자동) |
| 3 | `skill_approved` | Skill `proposed` → `approved` | T2 (사용자 명시) |
| 4 | `skill_promoted` | Skill `approved` → `promoted` | T2 + Evidence |
| 5 | `skill_revoked` | Skill `promoted` → `revoked` | T3 자동 안전 (rollback_trigger) |
| 6 | `gate_pass` | Gate (G1b/G2/G3/G4 등) PASS 선언 | T2 사용자 명시 |
| 7 | `gate_fail` | Gate FAIL 선언 | T2 사용자 명시 |
| 8 | `external_llm_received` | External LLM response 적재 | **T2 + agent="user" 강제** (원칙 7) |
| 9 | `evidence_forgery_detected` | P10 위반 검출 | T3 BLOCK |
| 10 | `roundtrip_pass` | Round-trip hash 일치 | T1 자동 |
| 11 | `roundtrip_lossy` | Round-trip 의미 보존 (lossy) | T3 사용자 review |
| 12 | `roundtrip_fail` | Round-trip 정책/권한/증거 손실 | T3 BLOCK |
| 13 | `migration_failed` | Migration 검증 실패 (Agent A 권고) | T3 BLOCK + manual |
| 14 | `chain_violation_detected` | prev_hash mismatch 또는 hash 재계산 검출 (외부 LLM 2 C-3) | T3 BLOCK + manual |
| 15 | `hash_chain_broken` | Hash chain 자체 단절 (외부 LLM 1) | T3 BLOCK |
| 16 | `policy_change_attempted` | Hermes 가 정책 변경 시도 (T3 위반) | T3 BLOCK + audit |
| 17 | `canonical_json_fallback` | Canonical JSON `jq -S -c` fallback 사용 | T1 audit |
| 18 | `secret_scan_layer1_implementation` | Secret scan Layer 1 구현 ledger (MVP-1 Stage 1, GP-3 S-1) | T1 audit |
| 19 | `docker_secret_isolation_layer1_implementation` | Docker secret 격리 Layer 1 구현 ledger (MVP-1 Stage 2, GP-3 ST-3) | T1 audit |
| 20 | `provider_adapter_enforcement_layer1_static` | Provider adapter Layer 1 static 검출 ledger (MVP-1 Stage 3, GP-5 T-6) | T1 audit |
| 21 | `pc3_ar1_integration_implementation` | pre-commit + auto-revert 통합 구현 ledger (MVP-1 Stage 4) | T1 audit |
| 22 | `g3_7_workflow_hygiene_implementation` | Workflow hygiene 4 항목 구현 ledger (MVP-1 Stage 5, G3-7) | T1 audit |
| 23 | `provider_key_adapter_bypass_risk_detected` | Provider lock-in 위반 detect (MVP-1 IR-1) | T2 사용자 review |
| 24 | `direct_sdk_with_secret_leakage_detected` | Direct SDK + secret 검출 (MVP-1 IR-2) | T3 BLOCK + manual |
| 25 | `secret_handling_environment_mismatch_detected` | 환경 secret mismatch detect (MVP-1 IR-3) | T2 사용자 review |

**MVP 의무 12 enum** (1~12, schema_version 0.1 도입). **후속 확장 5 enum** (13~17, schema_version 0.2 진입). **MVP-1 신규 8 enum** (18~25, schema_version 0.2 정식 등록 — Backlog #5 합의 `docs/review/3plus1-consensus-2026-05-13-adr-012-event-enum-registration.md` 권위, MVP-1 PASS §C-2 충족).

**Provider-neutral 강제** (Agent B C-16): 11 필드 모두 provider-specific 식별자 미허용.

### 2.3 Append-only 원칙 + Hash Chain (다층 강제)

**Layer 1 — Hash Chain (MANDATORY 모든 환경)**:
- `prev_hash` = 직전 entry 의 `hash` (chain 형성)
- `hash` = 본 entry 의 canonical JSON sha256
- 첫 entry 의 `prev_hash` = `genesis_hash` (§2.6)
- SHA-256 hardcode (schema_version 0.1) — `hash_algo` 필드 후속 격상 영역 (§3.2 답습)

**Layer 2 — Git append-only branch (MANDATORY)**:
- `git config receive.denyNonFastForwards true` (force-push 차단)
- branch protection rule
- pre-commit hook: `git rebase` / `git filter-branch` / `git reset --hard` 감지 시 reject
- CI 회귀 검증: base branch 대비 JSONL line deletion / rewrite 감지

**Layer 3 — Signed commit (RECOMMENDED MVP, MANDATORY multi-host)**:
- GPG / SSH key signed commit
- 1인 동일 호스트 = SHOULD (SPOF 면책)
- Multi-host 전환 / 외부 공유 / 팀 사용 / Hermes PMO 격상 시점 = MUST 승격 (G3 §5.5.3 트리거 답습)

**Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)**:
- 월 1회 external snapshot (별도 외부 git remote / cloud storage push)
- GitHub Actions run ID + signed tag (Agent B C-4 권고)
- 1인 SPOF 완화 + 침해 후 발견 가능

### 2.4 Signed commit OR Git append commit (사용자 명시 답습)

**사용자 명시 결정 답습**: "signed commit 또는 git append commit (둘 중 하나) 의무".

**5/5 입력 권고**: Layer 1 + Layer 2 동시 의무 (Hash chain + Git append-only) + Layer 3 RECOMMENDED.

**옵션** (사용자 결정 영역 — D-1):

| 옵션 | 정체성 | 적용 |
|-----|------|---|
| **D-1A** (사용자 명시 답습) | "둘 중 하나 의무" 그대로 — 최소 = git append-only, signed = 권장 | 사용자 결정 |
| **D-1B** (5 입력 권고) | "Hash chain + Git append-only MANDATORY + Signed RECOMMENDED" 다층 | 사용자 결정 |
| **D-1C** (절충, Reviewer 권고) | MVP = "둘 중 하나 의무" + Implementation 시점 다층 격상 | 사용자 결정 |

**본 ADR 의 권위 결정**: D-1A / D-1B / D-1C 모두 본 ADR §2.3 Layer 1 + Layer 2 동시 의무 *호환*. 단 사용자 명시 결정 영역 — 본 ADR 갱신은 단축 합의 가능.

### 2.5 RFC 8785 JCS Canonicalization (채택 + Fallback)

**Primary**: RFC 8785 JCS (https://www.rfc-editor.org/rfc/rfc8785) — *informational track*, IETF 권위.

**Fallback**: `jq -S -c` (lex sort + compact + UTF-8 + RFC 8259 escape) 또는 자체 구현 동등성 의무 + test corpus 검증.

**구현 라이브러리 후보** (Agent C C-3 권고):
- Python: `pyjcs` / `rfc8785` / 또는 stdlib `json.dumps(sort_keys=True, separators=(",",":"))` 동등 보장
- Node: `canonicalize` npm
- Go: `cyberphone/json-canonicalization` / `gowebpki/jcs`

**Test corpus 의무** (외부 LLM 2 C-6):
- `tests/canonical/` 디렉토리에 RFC 8785 reference 출력 ≥ 20개 포함
- CI 회귀 검증: 입력 → 자체 canonical → JCS reference output 비교
- 불일치 시 BLOCK

**Fallback 사용 시 의무**:
- `event: canonical_json_fallback` ledger entry 작성 의무
- Reviewer 알림 + 사용자 review 권장

### 2.6 Genesis Hash 정의

**MVP (schema_version 0.1) — 현 G4 §4.4 정의 유지**:

```
genesis_hash = sha256("genesis:<scope>:<schema_version>")
```

**0.2 진입 또는 multi-chain 도입 시 (외부 LLM 2 C-7)**:

```python
genesis_hash = sha256("genesis:" + canonical_json({
  "scope": <scope>,
  "schema_version": <version>,
  "created_at": <ISO 8601>,
  "agent": "user"
}))
```

**전이 절차**: 0.1 chain 의 첫 entry 는 MVP 정의로 유지. 0.2 진입 시 새 chain (별도 `chain_id` 또는 schema_version) 생성, 기존 0.1 chain 은 read-only.

### 2.7 prev_hash 검증 실패 처리 (BLOCK + Manual Review)

**처리 절차** (4/5 합의 답습 — 합의 §2.2 #8):

1. **즉시 BLOCK** — import / export / migration 중단
2. **기존 원본 JSONL 보존** — 자동 revert 금지 (T3 위반 위험)
3. **새 violation entry append** — `event: chain_violation_detected` ledger entry 작성:
   ```jsonl
   {"type":"meta","scope":"<scope>","event":"chain_violation_detected","content":{"violation_type":"prev_hash_mismatch|hash_recalculation|history_rewrite","detected_at":"<ts>","affected_entry":"<id>","prev_hash_expected":"<sha256>","prev_hash_actual":"<sha256>"},...}
   ```
4. **사용자 명시 review 의무** — 자동 PASS 금지
5. **자동 revert 금지** (T3 위반 — ADR-011 §2.4)
6. **Dual write 금지** (silent failure 위험)

**검출 layer**:
- Layer 1: pre-commit hook (입력 entry 의 `prev_hash` 검증)
- Layer 2: pre-push hook (chain 전체 재검증)
- Layer 3: CI nightly 회귀 검증 (R-6 답습 확장)
- Layer 4: import script (`scripts/hermes-migration/import.py` — 향후 Implementation 시점)

### 2.8 Full Rewrite 방어 (다층)

**5 Layer 강제** (합의 §3.5 답습):

- **Layer 1**: Hash chain (middle entry tampering 차단)
- **Layer 2**: Git append-only branch + denyNonFastForwards (history 재작성 차단)
- **Layer 3**: pre-commit hook — `git rebase` / `git filter-branch` / `git reset --hard` 감지 시 reject (T3 자동 *방어* 권한, T3 자동 *변경* 금지의 비대칭 활용 — 외부 LLM 2 §3.3)
- **Layer 4**: CI 회귀 검증 — base branch 대비 JSONL line deletion / rewrite 감지
- **Layer 5 (RECOMMENDED MVP, MANDATORY multi-host)**: External anchor — GitHub Actions run ID + signed tag (Agent B C-4) 또는 월 1회 external snapshot (외부 LLM 2 C-4)

**1인 동일 호스트 SPOF 한계 명시** (외부 LLM 1 권고 5 직접 인용):

> 동일 호스트 전체 침해 상황은 본 ADR-012 의 완전 방어 범위 밖이다. 본 ADR 은 Hermes container compromise, middle-entry tampering, accidental rewrite, migration 손실, evidence forgery 시도에 대한 탐지와 차단을 목표로 한다.

### 2.9 Round-trip Lossy 검출 (Tier-based)

**검증 PASS 조건** (4/5 합의 답습 — 합의 §3.3):

exec
/bin/bash -lc "find tests/canonical -type f | sort | wc -l && find tests/canonical -mindepth 1 -maxdepth 1 -type d -printf '%f\\n' | sort && find tests/canonical -type f | sed 's#tests/canonical/##' | sort | head -40" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
72
array
escape
hash_stability
key_ordering
lossy
nested
number
unicode
array/01.expected.canonical
array/01.expected.sha256
array/01.input.json
array/02.expected.canonical
array/02.expected.sha256
array/02.input.json
array/03.expected.canonical
array/03.expected.sha256
array/03.input.json
escape/01.expected.canonical
escape/01.expected.sha256
escape/01.input.json
escape/02.expected.canonical
escape/02.expected.sha256
escape/02.input.json
escape/03.expected.canonical
escape/03.expected.sha256
escape/03.input.json
hash_stability/01.expected.canonical
hash_stability/01.expected.sha256
hash_stability/01.input.json
hash_stability/02.expected.canonical
hash_stability/02.expected.sha256
hash_stability/02.input.json
hash_stability/03.expected.canonical
hash_stability/03.expected.sha256
hash_stability/03.input.json
key_ordering/01.expected.canonical
key_ordering/01.expected.sha256
key_ordering/01.input.json
key_ordering/02.expected.canonical
key_ordering/02.expected.sha256
key_ordering/02.input.json
key_ordering/03.expected.canonical
key_ordering/03.expected.sha256
key_ordering/03.input.json
lossy/01.expected.canonical
lossy/01.expected.sha256
lossy/01.input.json
lossy/02.expected.canonical

exec
/bin/bash -lc "ls -l tools/secret_scanner.py tools/jsonl_hash_chain.py tools/canonical_json.py src/adapters/llm/facade.py .github/workflows/secret-hygiene-egress-redaction.yml .github/workflows/g4-hash-chain.yml .github/workflows/history-anchor-verifier.yml .github/workflows/rewrite-defense.yml .github/workflows/r2-canary.yml; test -e agent/redact.py; printf 'agent_redact_exists=%s\\n' \""'$?"' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
-rw-rw-r-- 1 delangi delangi 10652 May 27 22:37 .github/workflows/g4-hash-chain.yml
-rw-rw-r-- 1 delangi delangi 19094 May 27 22:37 .github/workflows/history-anchor-verifier.yml
-rw-rw-r-- 1 delangi delangi  5476 May 27 22:37 .github/workflows/r2-canary.yml
-rw-rw-r-- 1 delangi delangi 16454 May 27 22:37 .github/workflows/rewrite-defense.yml
-rw-rw-r-- 1 delangi delangi 51791 May 27 22:37 .github/workflows/secret-hygiene-egress-redaction.yml
-rw-rw-r-- 1 delangi delangi  1390 May 10 00:27 src/adapters/llm/facade.py
-rw-rw-r-- 1 delangi delangi 10055 May 10 04:09 tools/canonical_json.py
-rw-rw-r-- 1 delangi delangi 14038 May 10 04:10 tools/jsonl_hash_chain.py
-rw-rw-r-- 1 delangi delangi 16802 May 27 23:28 tools/secret_scanner.py
agent_redact_exists=1

exec
/bin/bash -lc 'rg -n "scan-log|redaction|base64|Tier-1|known limitation|baseline|patterns|PATTERN|secret" tools/secret_scanner.py .github/workflows/secret-hygiene-egress-redaction.yml' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
tools/secret_scanner.py:5:  - docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md (본 PoC 사양)
tools/secret_scanner.py:6:  - docs/architecture/redaction-pattern-equivalence.md (R-4 — 패턴 동등성 카탈로그)
tools/secret_scanner.py:7:  - docs/phase0/r4-1-trigger-extension-evidence.md §4.1 (R-4.1 — Tier-1 42 catalog + baseline 5)
tools/secret_scanner.py:8:  - docker/r4-1-poc/r4_1_poc.py line 51~213 (Tier-1 42 patterns + baseline 5 직접 답습)
tools/secret_scanner.py:10:  - docs/decisions/ADR-011-means-vs-ends-redaction.md §2.1 (a)~(e)
tools/secret_scanner.py:13:  - R-4.1 Tier-1 42 catalog + baseline 5 = 45 patterns 직접 답습 (변경 0건)
tools/secret_scanner.py:14:  - Prefix 36 (baseline 5 + Tier-1 prefix 31) + 추가 regex 7 (H-A/B/C/E/F/G/K) + alternation 2 (H-J/H-L key 기반)
tools/secret_scanner.py:17:  - 외부 의존성 0건 (custom scanner 단독, gitleaks/detect-secrets 미도입)
tools/secret_scanner.py:20:  --mode scan-source : code-side secret 검출 (D-1 GP-3 Credential/Secret Hygiene)
tools/secret_scanner.py:21:  --mode scan-log    : redaction 후 잔존 secret 검출 (D-2 GP-2 Egress Redaction)
tools/secret_scanner.py:28:  1 = ≥1 위반 검출 (FAIL — D-1 secret 검출 / D-2 잔존 leak 검출)
tools/secret_scanner.py:32:  - base64 / URL-encoded / 압축 등 advanced evasion 미커버 (Hermes upstream R2-6 영역)
tools/secret_scanner.py:45:# Tier-1 패턴 카탈로그 (45종) — R-4.1 §4.1 직접 답습
tools/secret_scanner.py:48:#   - id: BL-N (baseline) 또는 T1-NNN (Tier-1)
tools/secret_scanner.py:50:#   - category: prefix-baseline / prefix / regex / alternation
tools/secret_scanner.py:57:    ("BL-1", "Hermes #1 (sk-ant-)", "prefix-baseline", "Anthropic",
tools/secret_scanner.py:59:    ("BL-2", "Hermes #1 (sk-)", "prefix-baseline", "OpenAI/Anthropic/etc",
tools/secret_scanner.py:61:    ("BL-3", "Hermes #2", "prefix-baseline", "GitHub PAT classic",
tools/secret_scanner.py:63:    ("BL-4", "Hermes #15", "prefix-baseline", "AWS Access Key ID",
tools/secret_scanner.py:65:    ("BL-5", "Hermes #8", "prefix-baseline", "Slack tokens",
tools/secret_scanner.py:69:# Tier-1 prefix 31 (Hermes #3..#7, #9..#14, #16..#35) — R-4.1 §4.1 직접 답습
tools/secret_scanner.py:70:PREFIX_PATTERNS: list[tuple[str, str, str, str, str]] = [
tools/secret_scanner.py:93:    ("T1-012", "Hermes #16", "prefix", "Stripe secret key (live)",
tools/secret_scanner.py:95:    ("T1-013", "Hermes #17", "prefix", "Stripe secret key (test)",
tools/secret_scanner.py:135:# Tier-1 추가 regex 7 (H-A, H-B, H-C, H-E, H-F, H-G, H-K — H-J/H-L 제외, R-4.1 §4.2 답습)
tools/secret_scanner.py:136:REGEX_PATTERNS: list[tuple[str, str, str, str, str]] = [
tools/secret_scanner.py:139:    ("T1-033", "Hermes H-B", "regex", "JSON field with secret keys",
tools/secret_scanner.py:140:     r'(?i)("(?:api_?[Kk]ey|token|secret|password|access_token|refresh_token|auth_token|bearer|secret_value|raw_secret|secret_input|key_material)")\s*:\s*"([^"]+)"'),
tools/secret_scanner.py:153:# Tier-1 alternation 2 (H-J / H-L sensitive key 기반 변환, R-4.1 §4.1 답습)
tools/secret_scanner.py:154:ALTERNATION_PATTERNS: list[tuple[str, str, str, str, str]] = [
tools/secret_scanner.py:161:     r"(?i)(?:^|[?&\s'\";#])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|session|secret|key|code|signature|x-amz-signature)=[^&\s]+"),
tools/secret_scanner.py:163:     r"(?i)(?:^|[?&\s'\";#])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|secret|private_key|authorization|key)=[^&\s]+"),
tools/secret_scanner.py:166:ALL_PATTERNS: list[tuple[str, str, str, str, str]] = (
tools/secret_scanner.py:167:    BASELINE_PREFIX + PREFIX_PATTERNS + REGEX_PATTERNS + ALTERNATION_PATTERNS
tools/secret_scanner.py:169:"""All registered patterns — 5 baseline + 31 prefix + 7 regex + 2 alternation = 45 patterns."""
tools/secret_scanner.py:172:COMPILED_PATTERNS: list[tuple[str, str, str, str, re.Pattern[str]]] = [
tools/secret_scanner.py:174:    for (pid, src, cat, vendor, rgx) in ALL_PATTERNS
tools/secret_scanner.py:180:# Redaction marker exclusion (scan-log mode 전용 — GP-2 D-2 contract 답습).
tools/secret_scanner.py:181:# 사양 §0 — D-2 = "redaction 후 잔존 secret 검증". 본 marker 가 매칭 substring 전체를
tools/secret_scanner.py:189:# scope 정책 (49 entry 발효): docs/architecture/secret-scanner-scope-policy.md
tools/secret_scanner.py:191:#   - docs/ 영역 영구 금지 (~800+ 잠재 false positive 답습 — fake canary / redaction 예시 / codex 응답 sample)
tools/secret_scanner.py:203:    """Single secret detection."""
tools/secret_scanner.py:222:def is_redaction_marker_match(matched_text: str) -> bool:
tools/secret_scanner.py:223:    """Scan-log mode 한정 — 매칭 텍스트가 redaction marker 만 포함하면 정상 redacted (FP 회피).
tools/secret_scanner.py:225:    GP-2 D-2 contract — 'redaction 후 잔존 secret 검증' (사양 §0).
tools/secret_scanner.py:232:    """Apply all 45 patterns to text and return violations.
tools/secret_scanner.py:235:    mode='scan-log' 시 redaction marker 매칭은 위반 미카운트 (FP 회피, 사양 §0).
tools/secret_scanner.py:238:    for pid, src, cat, vendor, pattern in COMPILED_PATTERNS:
tools/secret_scanner.py:243:            if mode == "scan-log" and is_redaction_marker_match(matched):
tools/secret_scanner.py:275:    elif mode == "scan-log":
tools/secret_scanner.py:291:def list_patterns() -> int:
tools/secret_scanner.py:292:    """Print Tier-1 catalog summary (사용자 명시 검증 5 — Tier-1 pattern count 자기 검증)."""
tools/secret_scanner.py:293:    n_baseline = len(BASELINE_PREFIX)
tools/secret_scanner.py:294:    n_prefix = len(PREFIX_PATTERNS)
tools/secret_scanner.py:295:    n_regex = len(REGEX_PATTERNS)
tools/secret_scanner.py:296:    n_alt = len(ALTERNATION_PATTERNS)
tools/secret_scanner.py:297:    total_registered = n_baseline + n_prefix + n_regex + n_alt
tools/secret_scanner.py:298:    n_active = total_registered - len(SKIP_DIRECT_REGISTER & {p[0] for p in ALL_PATTERNS})
tools/secret_scanner.py:300:    print(f"registered_patterns_count={total_registered}", file=sys.stderr)
tools/secret_scanner.py:301:    print(f"  baseline_prefix={n_baseline}", file=sys.stderr)
tools/secret_scanner.py:306:    print(f"  active_patterns={n_active}", file=sys.stderr)
tools/secret_scanner.py:311:    for pid, src, cat, vendor, rgx in ALL_PATTERNS:
tools/secret_scanner.py:320:        description="Secret scanner — Group D PoC (G2 GP-3 + GP-2, R-4.1 Tier-1 42 catalog 답습)"
tools/secret_scanner.py:324:        help="대상 파일/디렉토리 경로 (재귀). --list-patterns 시 생략 가능."
tools/secret_scanner.py:327:        "--mode", choices=("scan-source", "scan-log"), default=None,
tools/secret_scanner.py:329:            "scan-source = code-side secret 검출 (D-1). "
tools/secret_scanner.py:330:            "scan-log = redaction 후 잔존 secret 검출 (D-2)."
tools/secret_scanner.py:334:        "--list-patterns", action="store_true",
tools/secret_scanner.py:335:        help="등록된 45 patterns enumerate + Tier-1 42 catalog count 자기 검증",
tools/secret_scanner.py:343:    if args.list_patterns:
tools/secret_scanner.py:344:        return list_patterns()
tools/secret_scanner.py:347:        print("ERROR: path 와 --mode 필수 (--list-patterns 단독 모드 외)", file=sys.stderr)
.github/workflows/secret-hygiene-egress-redaction.yml:4:#   - docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md (본 PoC 사양 §9 — 12 step CI 설계)
.github/workflows/secret-hygiene-egress-redaction.yml:5:#   - docs/architecture/redaction-pattern-equivalence.md (R-4 — 패턴 동등성 카탈로그)
.github/workflows/secret-hygiene-egress-redaction.yml:6:#   - docs/phase0/r4-1-trigger-extension-evidence.md §4.1 (R-4.1 — 45 patterns trigger 등록)
.github/workflows/secret-hygiene-egress-redaction.yml:12:#   - D-2 PASS redaction residual (scan-log redaction_pass/) rc=0 + 0 잔존
.github/workflows/secret-hygiene-egress-redaction.yml:13:#   - D-2 FAIL redaction leak (scan-log redaction_fail/) rc=1 + partial leak 검출 (base64 = known limitation)
.github/workflows/secret-hygiene-egress-redaction.yml:14:#   - Tier-1 pattern count self-check (--list-patterns) registered_patterns_count=45 + tier1_42_catalog_compliant=True
.github/workflows/secret-hygiene-egress-redaction.yml:30:      - "tools/secret_scanner.py"
.github/workflows/secret-hygiene-egress-redaction.yml:31:      - "tools/docker_secret_image_layer_check.sh"
.github/workflows/secret-hygiene-egress-redaction.yml:32:      - "tools/docker_secret_restart_recovery.sh"
.github/workflows/secret-hygiene-egress-redaction.yml:34:      - "tools/workflow_secrets_usage_check.py"
.github/workflows/secret-hygiene-egress-redaction.yml:35:      - "tools/workflow_secrets_reference_check.py"
.github/workflows/secret-hygiene-egress-redaction.yml:36:      - "tools/workflow_fork_pr_secret_policy_check.py"
.github/workflows/secret-hygiene-egress-redaction.yml:38:      - "tools/docker_secret_inotify_sidecar_check.sh"
.github/workflows/secret-hygiene-egress-redaction.yml:39:      - "tests/fixtures/secret_hygiene/**"
.github/workflows/secret-hygiene-egress-redaction.yml:46:      - "tests/fixtures/secret_hygiene/mvp1_s3/**"
.github/workflows/secret-hygiene-egress-redaction.yml:48:      - ".github/workflows/secret-hygiene-egress-redaction.yml"
.github/workflows/secret-hygiene-egress-redaction.yml:57:    # ST-2 inotify sidecar PoC + S-3 detect-secrets 일관 nightly 발화 의무
.github/workflows/secret-hygiene-egress-redaction.yml:62:    #     tools/docker_secret_inotify_sidecar_check.sh nightly workflow 통합")
.github/workflows/secret-hygiene-egress-redaction.yml:85:      - name: Tier-1 pattern count self-check (--list-patterns)
.github/workflows/secret-hygiene-egress-redaction.yml:89:          python tools/secret_scanner.py --list-patterns \
.github/workflows/secret-hygiene-egress-redaction.yml:90:            > group-d-logs/list-patterns.stdout 2> group-d-logs/list-patterns.stderr
.github/workflows/secret-hygiene-egress-redaction.yml:93:          cat group-d-logs/list-patterns.stderr
.github/workflows/secret-hygiene-egress-redaction.yml:95:            echo "::error::--list-patterns expected rc=0, got rc=$rc"
.github/workflows/secret-hygiene-egress-redaction.yml:98:          if ! grep -q "registered_patterns_count=45" group-d-logs/list-patterns.stderr; then
.github/workflows/secret-hygiene-egress-redaction.yml:99:            echo "::error::registered_patterns_count != 45 (expected R-4.1 답습)"
.github/workflows/secret-hygiene-egress-redaction.yml:102:          if ! grep -q "tier1_42_catalog_compliant=True" group-d-logs/list-patterns.stderr; then
.github/workflows/secret-hygiene-egress-redaction.yml:107:          echo "Tier-1 pattern count self-check OK (registered=45, compliant=True)"
.github/workflows/secret-hygiene-egress-redaction.yml:113:          python tools/secret_scanner.py --mode scan-source \
.github/workflows/secret-hygiene-egress-redaction.yml:114:            tests/fixtures/secret_hygiene/pass/ \
.github/workflows/secret-hygiene-egress-redaction.yml:134:          python tools/secret_scanner.py --mode scan-source \
.github/workflows/secret-hygiene-egress-redaction.yml:135:            tests/fixtures/secret_hygiene/fail/ \
.github/workflows/secret-hygiene-egress-redaction.yml:150:          # 3 카테고리 cover (prefix-baseline + regex + alternation; private-key 는 regex sub-type T1-035)
.github/workflows/secret-hygiene-egress-redaction.yml:151:          for cat in "prefix-baseline" "regex" "alternation"; do
.github/workflows/secret-hygiene-egress-redaction.yml:165:      - name: D-2 PASS redaction residual — scan-log redaction_pass/ (rc=0 + 0 잔존)
.github/workflows/secret-hygiene-egress-redaction.yml:169:          python tools/secret_scanner.py --mode scan-log \
.github/workflows/secret-hygiene-egress-redaction.yml:170:            tests/fixtures/secret_hygiene/redaction_pass/ \
.github/workflows/secret-hygiene-egress-redaction.yml:176:            echo "::error::D-2 PASS expected rc=0 (redaction marker 인식 OK), got rc=$rc"
.github/workflows/secret-hygiene-egress-redaction.yml:184:          echo "D-2 PASS redaction residual OK (rc=0, 잔존=0, [REDACTED] 마커 인식)"
.github/workflows/secret-hygiene-egress-redaction.yml:186:      - name: D-2 FAIL redaction leak — scan-log redaction_fail/ (rc=1 + partial leak 검출)
.github/workflows/secret-hygiene-egress-redaction.yml:190:          python tools/secret_scanner.py --mode scan-log \
.github/workflows/secret-hygiene-egress-redaction.yml:191:            tests/fixtures/secret_hygiene/redaction_fail/ \
.github/workflows/secret-hygiene-egress-redaction.yml:205:          # base64_evasion.txt 미검출 = 의도된 known limitation (PoC 사양 §8 #1 답습)
.github/workflows/secret-hygiene-egress-redaction.yml:206:          if grep -q "base64_evasion.txt" group-d-logs/d2-fail.stderr; then
.github/workflows/secret-hygiene-egress-redaction.yml:207:            echo "::warning::base64_evasion.txt 가 검출됨 — known limitation 영역 변경 가능성 (사양 §8 #1 검토 필요)"
.github/workflows/secret-hygiene-egress-redaction.yml:209:            echo "base64 evasion = known limitation 답습 (Hermes upstream R2-6 영역, 본 PoC 미검출 의도)"
.github/workflows/secret-hygiene-egress-redaction.yml:212:          echo "D-2 FAIL redaction leak OK (rc=1, partial_redact 검출, base64 미검출 = known limitation)"
.github/workflows/secret-hygiene-egress-redaction.yml:218:          # F-금지 #1: 실 API key 0건 (fake canary 의무 — 모든 secret 은 FAKE / NOTAREAL / fakecanary marker 포함)
.github/workflows/secret-hygiene-egress-redaction.yml:219:          # 검사 대상 = fixture + scanner. scanner regex catalog 자체는 정의이므로 *fake marker 없는 raw secret*
.github/workflows/secret-hygiene-egress-redaction.yml:222:          for f in tests/fixtures/secret_hygiene/pass/*.py \
.github/workflows/secret-hygiene-egress-redaction.yml:223:                   tests/fixtures/secret_hygiene/pass/*.json \
.github/workflows/secret-hygiene-egress-redaction.yml:224:                   tests/fixtures/secret_hygiene/fail/*.py \
.github/workflows/secret-hygiene-egress-redaction.yml:225:                   tests/fixtures/secret_hygiene/fail/*.json \
.github/workflows/secret-hygiene-egress-redaction.yml:226:                   tests/fixtures/secret_hygiene/fail/*.pem \
.github/workflows/secret-hygiene-egress-redaction.yml:227:                   tests/fixtures/secret_hygiene/redaction_pass/*.txt \
.github/workflows/secret-hygiene-egress-redaction.yml:228:                   tests/fixtures/secret_hygiene/redaction_fail/*.txt; do
.github/workflows/secret-hygiene-egress-redaction.yml:251:          if grep -E "^(import|from)\s+(openai|anthropic|google\.generativeai|litellm|ollama)" tools/secret_scanner.py; then
.github/workflows/secret-hygiene-egress-redaction.yml:262:      - name: MVP-1 entry — secret_scanner coverage check (mvp1_entry/ fixtures)
.github/workflows/secret-hygiene-egress-redaction.yml:266:          # MVP-1 entry fail scan — expect rc=1 + cover H-C/H-F/H-G/H-K + Tier-1 prefix variety
.github/workflows/secret-hygiene-egress-redaction.yml:267:          python tools/secret_scanner.py --mode scan-source \
.github/workflows/secret-hygiene-egress-redaction.yml:268:            tests/fixtures/secret_hygiene/mvp1_entry/fail/ \
.github/workflows/secret-hygiene-egress-redaction.yml:272:          python tools/secret_scanner.py --mode scan-source \
.github/workflows/secret-hygiene-egress-redaction.yml:273:            tests/fixtures/secret_hygiene/mvp1_entry/pass/ \
.github/workflows/secret-hygiene-egress-redaction.yml:287:          # Verify additional Tier-1 pattern IDs cover (regex H-C/H-F/H-G/H-K + prefix variety)
.github/workflows/secret-hygiene-egress-redaction.yml:296:          echo "ledger_event_candidate=secret_scan_layer1_implementation" >> $GITHUB_OUTPUT
.github/workflows/secret-hygiene-egress-redaction.yml:297:          echo "MVP-1 entry scan OK — fail rc=1 + 10 Tier-1 IDs cover, pass rc=0"
.github/workflows/secret-hygiene-egress-redaction.yml:299:      # === S-3 detect-secrets 부분 통합 (MVP-1 1.5차 보강 sub-cycle, Defense in depth) ===
.github/workflows/secret-hygiene-egress-redaction.yml:301:      #   - docs/phase0/mvp1-s3-detect-secrets-partial-integration-brief.md
.github/workflows/secret-hygiene-egress-redaction.yml:302:      #   - docs/review/3plus1-consensus-2026-05-27-mvp1-s3-detect-secrets-partial-integration.md (Reviewer-only APPROVE)
.github/workflows/secret-hygiene-egress-redaction.yml:303:      #   - 24번째 entry R-4 BLOCKING (plugin identifier 정확 mapping + --baseline 미사용 assertion)
.github/workflows/secret-hygiene-egress-redaction.yml:304:      # S-1 (tools/secret_scanner.py) 답습 유지 + S-3 추가 layer (R-MVP1-1.5-S3-3 영구 의무)
.github/workflows/secret-hygiene-egress-redaction.yml:306:      - name: S-3 install detect-secrets (Tier-1 답습 plugin 5종 한정)
.github/workflows/secret-hygiene-egress-redaction.yml:310:          pip install detect-secrets==1.5.0
.github/workflows/secret-hygiene-egress-redaction.yml:311:          detect-secrets --version
.github/workflows/secret-hygiene-egress-redaction.yml:313:      - name: S-3 detect-secrets scan — Tier-1 plugin 5종 enable (R-4 BLOCKING 본문 채택)
.github/workflows/secret-hygiene-egress-redaction.yml:314:        id: s3_detect_secrets
.github/workflows/secret-hygiene-egress-redaction.yml:317:          # plugin allowlist hardcoded (brief §1.3 본문 채택, Tier-1 답습 한정).
.github/workflows/secret-hygiene-egress-redaction.yml:322:          # baseline file 옵션 사용 0건 (R-MVP1-1.5-S3-2 영구 금지, silenceable risk)
.github/workflows/secret-hygiene-egress-redaction.yml:323:          detect-secrets scan \
.github/workflows/secret-hygiene-egress-redaction.yml:346:            tests/fixtures/secret_hygiene/mvp1_s3/ \
.github/workflows/secret-hygiene-egress-redaction.yml:347:            > group-d-logs/s3-detect-secrets.json 2> group-d-logs/s3-detect-secrets.stderr
.github/workflows/secret-hygiene-egress-redaction.yml:350:          cat group-d-logs/s3-detect-secrets.stderr
.github/workflows/secret-hygiene-egress-redaction.yml:352:            echo "::error::S-3 detect-secrets scan unexpected error (rc=$rc)"
.github/workflows/secret-hygiene-egress-redaction.yml:360:          with open('group-d-logs/s3-detect-secrets.json') as f:
.github/workflows/secret-hygiene-egress-redaction.yml:363:          pass_findings = [k for k in results if k.startswith('tests/fixtures/secret_hygiene/mvp1_s3/pass/')]
.github/workflows/secret-hygiene-egress-redaction.yml:368:              'tests/fixtures/secret_hygiene/mvp1_s3/fail/aws_key.py',
.github/workflows/secret-hygiene-egress-redaction.yml:369:              'tests/fixtures/secret_hygiene/mvp1_s3/fail/keyword.py',
.github/workflows/secret-hygiene-egress-redaction.yml:370:              'tests/fixtures/secret_hygiene/mvp1_s3/fail/base64_entropy.py',
.github/workflows/secret-hygiene-egress-redaction.yml:371:              'tests/fixtures/secret_hygiene/mvp1_s3/fail/hex_entropy.py',
.github/workflows/secret-hygiene-egress-redaction.yml:372:              'tests/fixtures/secret_hygiene/mvp1_s3/fail/private_key.py',
.github/workflows/secret-hygiene-egress-redaction.yml:384:          echo "s3_detect_secrets=PASS" >> $GITHUB_OUTPUT
.github/workflows/secret-hygiene-egress-redaction.yml:385:          echo "S-3 detect-secrets scan OK — Tier-1 plugin 5종 PASS evidence"
.github/workflows/secret-hygiene-egress-redaction.yml:387:      - name: S-3 baseline file 미사용 assertion (R-MVP1-1.5-S3-2 영구 금지 답습)
.github/workflows/secret-hygiene-egress-redaction.yml:388:        id: s3_baseline_assertion
.github/workflows/secret-hygiene-egress-redaction.yml:391:          # workflow 본문에서 detect-secrets 의 baseline file flag (CLI argument) 사용 시 fail.
.github/workflows/secret-hygiene-egress-redaction.yml:395:          BASELINE_FLAG=$(printf '%s' '--baseline')
.github/workflows/secret-hygiene-egress-redaction.yml:397:               .github/workflows/secret-hygiene-egress-redaction.yml; then
.github/workflows/secret-hygiene-egress-redaction.yml:398:            echo "::error::R-MVP1-1.5-S3-2 위반 — baseline file CLI flag 사용 검출 (영구 금지, silenceable risk)"
.github/workflows/secret-hygiene-egress-redaction.yml:401:          echo "s3_baseline_assertion=PASS" >> $GITHUB_OUTPUT
.github/workflows/secret-hygiene-egress-redaction.yml:402:          echo "[OK] S-3 baseline file 미사용 assertion PASS (R-MVP1-1.5-S3-2 답습)"
.github/workflows/secret-hygiene-egress-redaction.yml:409:          tools/docker_secret_image_layer_check.sh \
.github/workflows/secret-hygiene-egress-redaction.yml:414:          # PASS fixture — expect clean (no secret baked)
.github/workflows/secret-hygiene-egress-redaction.yml:415:          tools/docker_secret_image_layer_check.sh \
.github/workflows/secret-hygiene-egress-redaction.yml:427:          tools/docker_secret_restart_recovery.sh docker/gp3-st3-poc \
.github/workflows/secret-hygiene-egress-redaction.yml:431:          echo "stage2_ledger_event_candidate=docker_secret_isolation_layer1_implementation" >> $GITHUB_OUTPUT
.github/workflows/secret-hygiene-egress-redaction.yml:432:          echo "Stage 2 restart recovery OK — secret sha256 일치 + isolation_check=PASS (2회)"
.github/workflows/secret-hygiene-egress-redaction.yml:440:            .github/workflows/secret-hygiene-egress-redaction.yml \
.github/workflows/secret-hygiene-egress-redaction.yml:478:      - name: Stage 5 cycle 1 — workflow secrets usage 0건 검증 (5.1)
.github/workflows/secret-hygiene-egress-redaction.yml:479:        id: stage5_5_1_secrets_usage
.github/workflows/secret-hygiene-egress-redaction.yml:482:          # 1) Real .github/workflows/ 전체 — 0건 baseline 검증 (rc=0 기대)
.github/workflows/secret-hygiene-egress-redaction.yml:483:          python3 tools/workflow_secrets_usage_check.py .github/workflows/ \
.github/workflows/secret-hygiene-egress-redaction.yml:484:            | tee group-d-logs/stage5-5.1-secrets-usage-real.log
.github/workflows/secret-hygiene-egress-redaction.yml:486:          python3 tools/workflow_secrets_usage_check.py \
.github/workflows/secret-hygiene-egress-redaction.yml:487:            tests/fixtures/stage5_g3_7/secrets_usage/pass/ \
.github/workflows/secret-hygiene-egress-redaction.yml:488:            | tee group-d-logs/stage5-5.1-secrets-usage-fixture-pass.log
.github/workflows/secret-hygiene-egress-redaction.yml:491:          python3 tools/workflow_secrets_usage_check.py \
.github/workflows/secret-hygiene-egress-redaction.yml:492:            tests/fixtures/stage5_g3_7/secrets_usage/fail/ \
.github/workflows/secret-hygiene-egress-redaction.yml:493:            > group-d-logs/stage5-5.1-secrets-usage-fixture-fail.log
.github/workflows/secret-hygiene-egress-redaction.yml:496:          cat group-d-logs/stage5-5.1-secrets-usage-fixture-fail.log
.github/workflows/secret-hygiene-egress-redaction.yml:501:          violations=$(grep -oE "violations = [0-9]+" group-d-logs/stage5-5.1-secrets-usage-fixture-fail.log | head -1 | grep -oE "[0-9]+")
.github/workflows/secret-hygiene-egress-redaction.yml:507:          if ! grep -q "kind=interpolation" group-d-logs/stage5-5.1-secrets-usage-fixture-fail.log; then
.github/workflows/secret-hygiene-egress-redaction.yml:511:          if ! grep -q "kind=block" group-d-logs/stage5-5.1-secrets-usage-fixture-fail.log; then
.github/workflows/secret-hygiene-egress-redaction.yml:516:          python3 tools/workflow_secrets_usage_check.py --list-checks \
.github/workflows/secret-hygiene-egress-redaction.yml:517:            | tee group-d-logs/stage5-5.1-secrets-usage-list-checks.log
.github/workflows/secret-hygiene-egress-redaction.yml:518:          echo "stage5_5_1_secrets_usage=PASS" >> $GITHUB_OUTPUT
.github/workflows/secret-hygiene-egress-redaction.yml:523:      - name: Stage 5 cycle 2 — workflow secrets.* 참조 감지 (5.2)
.github/workflows/secret-hygiene-egress-redaction.yml:524:        id: stage5_5_2_secrets_dot_ref
.github/workflows/secret-hygiene-egress-redaction.yml:527:          # 1) Real .github/workflows/ 전체 — 0건 baseline 검증 (rc=0 기대)
.github/workflows/secret-hygiene-egress-redaction.yml:528:          python3 tools/workflow_secrets_reference_check.py .github/workflows/ \
.github/workflows/secret-hygiene-egress-redaction.yml:529:            | tee group-d-logs/stage5-5.2-secrets-ref-real.log
.github/workflows/secret-hygiene-egress-redaction.yml:531:          python3 tools/workflow_secrets_reference_check.py \
.github/workflows/secret-hygiene-egress-redaction.yml:532:            tests/fixtures/stage5_g3_7/secrets_reference/pass/ \
.github/workflows/secret-hygiene-egress-redaction.yml:533:            | tee group-d-logs/stage5-5.2-secrets-ref-fixture-pass.log
.github/workflows/secret-hygiene-egress-redaction.yml:536:          python3 tools/workflow_secrets_reference_check.py \
.github/workflows/secret-hygiene-egress-redaction.yml:537:            tests/fixtures/stage5_g3_7/secrets_reference/fail/ \
.github/workflows/secret-hygiene-egress-redaction.yml:538:            > group-d-logs/stage5-5.2-secrets-ref-fixture-fail.log
.github/workflows/secret-hygiene-egress-redaction.yml:541:          cat group-d-logs/stage5-5.2-secrets-ref-fixture-fail.log
.github/workflows/secret-hygiene-egress-redaction.yml:546:          violations=$(grep -oE "violations = [0-9]+" group-d-logs/stage5-5.2-secrets-ref-fixture-fail.log | head -1 | grep -oE "[0-9]+")
.github/workflows/secret-hygiene-egress-redaction.yml:553:            if ! grep -qE "$ctx" group-d-logs/stage5-5.2-secrets-ref-fixture-fail.log; then
.github/workflows/secret-hygiene-egress-redaction.yml:559:          python3 tools/workflow_secrets_reference_check.py --list-checks \
.github/workflows/secret-hygiene-egress-redaction.yml:560:            | tee group-d-logs/stage5-5.2-secrets-ref-list-checks.log
.github/workflows/secret-hygiene-egress-redaction.yml:561:          echo "stage5_5_2_secrets_dot_ref=PASS" >> $GITHUB_OUTPUT
.github/workflows/secret-hygiene-egress-redaction.yml:564:      - name: Stage 5 cycle 3 — fork PR secret 정책 검증 (5.3)
.github/workflows/secret-hygiene-egress-redaction.yml:568:          # 1) Real .github/workflows/ 전체 — 위험 trigger 0건 baseline 검증 (rc=0 기대)
.github/workflows/secret-hygiene-egress-redaction.yml:569:          python3 tools/workflow_fork_pr_secret_policy_check.py .github/workflows/ \
.github/workflows/secret-hygiene-egress-redaction.yml:572:          python3 tools/workflow_fork_pr_secret_policy_check.py \
.github/workflows/secret-hygiene-egress-redaction.yml:577:          python3 tools/workflow_fork_pr_secret_policy_check.py \
.github/workflows/secret-hygiene-egress-redaction.yml:602:          python3 tools/workflow_fork_pr_secret_policy_check.py --list-checks \
.github/workflows/secret-hygiene-egress-redaction.yml:611:          # 1) Real .github/workflows/ — K-2 baseline fix 후속 (Backlog #5 발효 후 K-2 fix 합의 답습).
.github/workflows/secret-hygiene-egress-redaction.yml:623:            echo "::error::Cycle 4 real workflows 예상 rc=0 (K-2 fix 후 clean baseline), got rc=$rc_real"
.github/workflows/secret-hygiene-egress-redaction.yml:624:            echo "::error::K-2 baseline 회귀 또는 새 violation 발생 — 사용자 명시 합의 필요"
.github/workflows/secret-hygiene-egress-redaction.yml:629:            echo "::error::Cycle 4 real workflows 예상 violations=0 (K-2 fix 후 clean baseline), got '$real_violations'"
.github/workflows/secret-hygiene-egress-redaction.yml:632:          echo "::notice::Cycle 4 real workflows clean — 11/11 workflow permissions: contents: read 일관 (K-2 baseline = resolved, K-2 fix 합의 권위 답습)"
.github/workflows/secret-hygiene-egress-redaction.yml:670:          echo "Stage 5 cycle 4 OK — real workflows clean (11/11 일관, K-2 baseline = resolved) + PASS fixture violations=0 + FAIL fixture violations=$fixture_violations (missing + broader cover)"
.github/workflows/secret-hygiene-egress-redaction.yml:677:        #   #3 /run/secrets/* / #5 inotifywait / #8 init grace 10s / #9 interval 5s
.github/workflows/secret-hygiene-egress-redaction.yml:678:        # 영구 강제: secret 본문 출력 0건 (event tag 비교 한정) +
.github/workflows/secret-hygiene-egress-redaction.yml:682:          tools/docker_secret_inotify_sidecar_check.sh \
.github/workflows/secret-hygiene-egress-redaction.yml:692:          tools/docker_secret_inotify_sidecar_check.sh --list-checks \
.github/workflows/secret-hygiene-egress-redaction.yml:710:            "mvp1_entry_ledger_event_candidate": "${{ steps.mvp1_entry_scan.outputs.ledger_event_candidate || 'secret_scan_layer1_implementation' }}",
.github/workflows/secret-hygiene-egress-redaction.yml:715:            "stage2_ledger_event_candidate": "${{ steps.stage2_restart_recovery.outputs.stage2_ledger_event_candidate || 'docker_secret_isolation_layer1_implementation' }}",
.github/workflows/secret-hygiene-egress-redaction.yml:718:            "stage2_scope": "GP-3 Stage 2 (ST-3 docker secret) 단독 구현 진입 — Hermes upstream 변경 0건 + production docker-compose 변경 0건 + Implementation Evidence PASS / MVP-1 PASS / Operational Readiness / Hermes PMO 격상 0건",
.github/workflows/secret-hygiene-egress-redaction.yml:724:            "stage5_5_1_secrets_usage": "${{ steps.stage5_5_1_secrets_usage.outputs.stage5_5_1_secrets_usage || 'FAIL' }}",
.github/workflows/secret-hygiene-egress-redaction.yml:725:            "stage5_5_2_secrets_dot_ref": "${{ steps.stage5_5_2_secrets_dot_ref.outputs.stage5_5_2_secrets_dot_ref || 'FAIL' }}",
.github/workflows/secret-hygiene-egress-redaction.yml:728:            "stage5_5_4_known_baseline": "resolved — K-2 baseline fix 합의 답습 (provider-adapter-enforcement.yml top-level permissions: contents: read 추가, 11/11 workflow 일관 도달). MVP-1 PASS §C-1 충족 갱신은 별도 합의 단계.",
.github/workflows/secret-hygiene-egress-redaction.yml:729:            "stage5_ledger_event_candidate": "${{ steps.stage5_5_1_secrets_usage.outputs.stage5_ledger_event_candidate || 'g3_7_workflow_hygiene_implementation' }}",
.github/workflows/secret-hygiene-egress-redaction.yml:732:            "stage5_scope": "Stage 5 G3-7 4 항목 구현 진입 — cycle 1 (5.1 secrets usage 0건) + cycle 2 (5.2 secrets.* 참조 감지) + cycle 3 (5.3 fork PR secret 정책) + cycle 4 (5.4 workflow permissions: contents: read 검증 — K-2 baseline = resolved, 11/11 workflow 일관 도달) 통합. K-2 fix 적격성 권위 권고 발효 답습. MVP-1 PASS §C-1 충족 갱신 합의는 별도 단계. Operational Readiness PASS / Hermes PMO 격상 / 다른 backlog 자동 진입 0건",
.github/workflows/secret-hygiene-egress-redaction.yml:736:            "gp3_st2_ledger_event_candidate": "secret_storage_inotify_isolation",
.github/workflows/secret-hygiene-egress-redaction.yml:738:            "gp3_st2_evidence_form": "Markdown step summary + JSONL stub (st2-inotify-sidecar.log + st2-inotify-sidecar-list-checks.log) + actual run URL — Layer C 발효 시점 의무. F-B status file → hermes-mock healthcheck unhealthy (primary) + F-C sidecar pgrep healthcheck + depends_on: service_healthy 보조 + F-A 비채택 (docker socket 0건, privileged false, cap_drop ALL) + /run/secrets/* 감시 (사용자 #3) + init grace 10초 (사용자 #8) + healthcheck interval 5초 (사용자 #9) + secret rotation 별도 합의 (사용자 #4)",
.github/workflows/secret-hygiene-egress-redaction.yml:742:            "registered_patterns_count": "45",
.github/workflows/secret-hygiene-egress-redaction.yml:749:            "known_limitation": "base64 / URL-encoded / 압축 등 advanced evasion 미커버 (Hermes upstream R2-6 영역)"
.github/workflows/secret-hygiene-egress-redaction.yml:754:      - name: Upload secret hygiene logs (artifact)
.github/workflows/secret-hygiene-egress-redaction.yml:758:          name: secret-hygiene-egress-redaction-evidence
.github/workflows/secret-hygiene-egress-redaction.yml:770:            echo "- event: g2_gp3_gp2_secret_hygiene_egress_redaction_layer1"
.github/workflows/secret-hygiene-egress-redaction.yml:772:            echo "- ledger_layer: Layer 1 — Custom Tier-1 catalog scanner (R-4.1 답습 직접)"
.github/workflows/secret-hygiene-egress-redaction.yml:779:            echo "- mvp1_entry_scan: ${{ steps.mvp1_entry_scan.outputs.mvp1_entry_scan || 'FAIL' }} (regex H-C/H-F/H-G/H-K + Tier-1 prefix variety cover)"
.github/workflows/secret-hygiene-egress-redaction.yml:780:            echo "- mvp1_entry_ledger_event_candidate: ${{ steps.mvp1_entry_scan.outputs.ledger_event_candidate || 'secret_scan_layer1_implementation' }} (후보 한정 — Backlog #5 별도 합의 영역)"
.github/workflows/secret-hygiene-egress-redaction.yml:783:            echo "- stage2_restart_recovery: ${{ steps.stage2_restart_recovery.outputs.stage2_restart_recovery || 'FAIL' }} (secret sha256 2회 일치 + isolation_check=PASS 2회)"
.github/workflows/secret-hygiene-egress-redaction.yml:784:            echo "- stage2_ledger_event_candidate: ${{ steps.stage2_restart_recovery.outputs.stage2_ledger_event_candidate || 'docker_secret_isolation_layer1_implementation' }} (후보 한정 — Backlog #5 별도 합의 영역)"
.github/workflows/secret-hygiene-egress-redaction.yml:786:            echo "- stage2_scope: GP-3 Stage 2 (ST-3 docker secret) 단독 구현 진입 — Hermes upstream 0건 + production docker-compose 0건 + PASS 발효 / 격상 0건"
.github/workflows/secret-hygiene-egress-redaction.yml:791:            echo "- stage5_5_1_secrets_usage: ${{ steps.stage5_5_1_secrets_usage.outputs.stage5_5_1_secrets_usage || 'FAIL' }} (real .github/workflows/ 11 files violations=0 + PASS fixture violations=0 + FAIL fixture violations>=2 interpolation+block cover)"
.github/workflows/secret-hygiene-egress-redaction.yml:792:            echo "- stage5_5_2_secrets_dot_ref: ${{ steps.stage5_5_2_secrets_dot_ref.outputs.stage5_5_2_secrets_dot_ref || 'FAIL' }} (real 11 files violations=0 + PASS fixture violations=0 + FAIL fixture violations>=4 env+with+run+if context cover)"
.github/workflows/secret-hygiene-egress-redaction.yml:795:            echo "- stage5_5_4_known_baseline: resolved — K-2 baseline fix 합의 답습 (11/11 workflow permissions: contents: read 일관). MVP-1 PASS §C-1 충족 갱신은 별도 합의 단계."
.github/workflows/secret-hygiene-egress-redaction.yml:796:            echo "- stage5_ledger_event_candidate: ${{ steps.stage5_5_1_secrets_usage.outputs.stage5_ledger_event_candidate || 'g3_7_workflow_hygiene_implementation' }} (후보 한정 — Backlog #5 별도 합의 영역)"
.github/workflows/secret-hygiene-egress-redaction.yml:798:            echo "- stage5_scope: Stage 5 G3-7 cycle 1+2+3+4 통합 — cycle 4 K-2 baseline = resolved (11/11 workflow 일관) — K-2 fix 적격성 권위 권고 발효 답습. MVP-1 PASS §C-1 충족 갱신은 별도 단계 / Operational Readiness PASS / Hermes PMO 격상 / 다른 backlog 자동 진입 0건"
.github/workflows/secret-hygiene-egress-redaction.yml:802:            echo "- gp3_st2_ledger_event_candidate: secret_storage_inotify_isolation (후보 한정 — Backlog #5 분리, ADR-012 §2.2 enum 정식 등록 별도 합의)"
.github/workflows/secret-hygiene-egress-redaction.yml:803:            echo "- gp3_st2_evidence_form: F-B status file → hermes-mock healthcheck unhealthy (primary) + F-C sidecar pgrep + depends_on: service_healthy 보조 + F-A 비채택 (docker socket 0건) + /run/secrets/* 감시 + init grace 10s + healthcheck interval 5s + secret rotation 별도 합의 (Layer C 발효 시점 의무)"
.github/workflows/secret-hygiene-egress-redaction.yml:807:            echo "- known_limitation: base64 advanced evasion (Hermes upstream R2-6 영역)"
.github/workflows/secret-hygiene-egress-redaction.yml:808:            echo "- gitleaks_detect_secrets_introduction: 0건 (custom scanner 단독, Tier-2/3 catalog 확장 위험 회피)"

exec
/bin/bash -lc 'rg -n "genesis|violation_type|PREV_HASH_MISMATCH|HASH_RECALCULATION|HISTORY_REWRITE|GENESIS_MISMATCH|canonical|timestamp|monotonic" tools/jsonl_hash_chain.py tools/canonical_json.py .github/workflows/g4-hash-chain.yml .github/workflows/history-anchor-verifier.yml .github/workflows/rewrite-defense.yml .github/workflows/r2-canary.yml' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
.github/workflows/rewrite-defense.yml:60:          # parse_jsonl → canonical_json → rfc8785 의존성 답습
.github/workflows/history-anchor-verifier.yml:59:          # validate_chain → compute_entry_hash → canonical_json → rfc8785 의존성 답습
.github/workflows/history-anchor-verifier.yml:211:      - name: Anchor FAIL — substitution (rc=1 + tail_hash + genesis_hash)
.github/workflows/history-anchor-verifier.yml:225:          for pid in "tail-hash-mismatch" "genesis-hash-mismatch"; do
.github/workflows/history-anchor-verifier.yml:232:          echo "Anchor FAIL substitution OK (rc=1, tail-hash + genesis-hash mismatch)"
.github/workflows/history-anchor-verifier.yml:282:          # F-금지: 실 signed commit / external timestamping 도구 import 0건
.github/workflows/history-anchor-verifier.yml:284:            echo "::error::F-금지 위반 — signed commit / external timestamping 도구 import"
.github/workflows/history-anchor-verifier.yml:334:            "external_dependencies": "0 (stdlib re + json + dataclasses 단독, signed commit / branch protection / external timestamping 미진입)",
.github/workflows/history-anchor-verifier.yml:371:            echo "- external_dependencies: 0 (stdlib 단독, signed commit / external timestamping 미진입)"
tools/canonical_json.py:17:  - Fallback 사용 시 = `event: canonical_json_fallback` ledger entry 작성 의무 (caller 책임)
tools/canonical_json.py:50:    - FALLBACK_JQ: jq -S -c subprocess (Primary install 실패 시, canonical_json_fallback entry 의무)
tools/canonical_json.py:71:    canonical: bytes
tools/canonical_json.py:78:def _to_canonical_rfc8785(obj: Any) -> bytes:
tools/canonical_json.py:86:def _to_canonical_jcs(obj: Any) -> bytes:
tools/canonical_json.py:90:    out = jcs.canonicalize(obj)
tools/canonical_json.py:94:def _to_canonical_jq_fallback(obj: Any) -> bytes:
tools/canonical_json.py:98:    `event: canonical_json_fallback` ledger entry 작성 의무.
tools/canonical_json.py:122:def to_canonical(obj: Any, mode: CrossCheckMode = CrossCheckMode.PRIMARY_1_ONLY) -> CanonicalResult:
tools/canonical_json.py:130:        CanonicalResult (canonical bytes + sha256 hex + mode used + fallback/cross-check flag)
tools/canonical_json.py:140:        canonical = _to_canonical_rfc8785(obj)
tools/canonical_json.py:142:        canonical = _to_canonical_jcs(obj)
tools/canonical_json.py:144:        out_p1 = _to_canonical_rfc8785(obj)
tools/canonical_json.py:145:        out_p2 = _to_canonical_jcs(obj)
tools/canonical_json.py:151:        canonical = out_p1
tools/canonical_json.py:154:        canonical = _to_canonical_jq_fallback(obj)
tools/canonical_json.py:159:    sha256_hex = hashlib.sha256(canonical).hexdigest()
tools/canonical_json.py:161:        canonical=canonical,
tools/canonical_json.py:187:        "--expected-canonical",
tools/canonical_json.py:190:        help="기대 canonical 출력 파일 (있으면 byte 비교)",
tools/canonical_json.py:217:        result = to_canonical(obj, mode=CrossCheckMode(args.mode))
tools/canonical_json.py:225:    sys.stdout.buffer.write(result.canonical)
tools/canonical_json.py:235:    if args.expected_canonical:
tools/canonical_json.py:237:            with open(args.expected_canonical, "rb") as f:
tools/canonical_json.py:242:        if result.canonical != expected:
tools/canonical_json.py:244:                f"CANONICAL_MISMATCH: got={result.canonical!r} expected={expected!r}",
tools/canonical_json.py:265:            fb_result = to_canonical(obj, mode=CrossCheckMode.FALLBACK_JQ)
tools/canonical_json.py:266:            if fb_result.canonical != result.canonical:
tools/canonical_json.py:268:                    f"FALLBACK_EQUIV_FAIL: primary={result.canonical[:80]!r} jq={fb_result.canonical[:80]!r}",
tools/jsonl_hash_chain.py:10:  - tools/canonical_json.py (Q1 합의 답습 — rfc8785 + jcs 병렬 cross-check)
tools/jsonl_hash_chain.py:15:  - Genesis hash = sha256("genesis:<scope>:<schema_version>") (ADR-012 §2.6 MVP)
tools/jsonl_hash_chain.py:16:  - hash 계산 = sha256(canonical_json(entry - "hash" field))
tools/jsonl_hash_chain.py:18:  - violation_type 4종: prev_hash_mismatch / hash_recalculation / history_rewrite / genesis_mismatch
tools/jsonl_hash_chain.py:19:  - timestamp monotonicity: 본 entry ts >= prev_hash entry ts (ADR-012 §3.4)
tools/jsonl_hash_chain.py:40:from canonical_json import (  # type: ignore[import-not-found]
tools/jsonl_hash_chain.py:43:    to_canonical,
tools/jsonl_hash_chain.py:69:    PREV_HASH_MISMATCH = "prev_hash_mismatch"
tools/jsonl_hash_chain.py:70:    HASH_RECALCULATION = "hash_recalculation"
tools/jsonl_hash_chain.py:71:    HISTORY_REWRITE = "history_rewrite"
tools/jsonl_hash_chain.py:72:    GENESIS_MISMATCH = "genesis_mismatch"
tools/jsonl_hash_chain.py:81:    violation_type: str  # ViolationType.value or "schema_*" / "monotonicity_*"
tools/jsonl_hash_chain.py:85:def compute_genesis_hash(scope: str, schema_version: str) -> str:
tools/jsonl_hash_chain.py:86:    """Genesis hash MVP — sha256("genesis:<scope>:<schema_version>") (ADR-012 §2.6).
tools/jsonl_hash_chain.py:90:    return hashlib.sha256(f"genesis:{scope}:{schema_version}".encode("utf-8")).hexdigest()
tools/jsonl_hash_chain.py:94:    """Entry hash = sha256(canonical_json(entry - "hash" field)).
tools/jsonl_hash_chain.py:99:    result = to_canonical(payload, mode=CrossCheckMode.PRIMARY_1_ONLY)
tools/jsonl_hash_chain.py:104:    """ISO 8601 timestamp parse — 'Z' suffix 정규화."""
tools/jsonl_hash_chain.py:121:                violation_type="schema_missing_field",
tools/jsonl_hash_chain.py:166:    """Genesis + prev_hash ↔ hash chain + timestamp monotonicity 검증."""
tools/jsonl_hash_chain.py:182:                Violation(i, entry_id, "schema_canonical_error", f"canonical_json failed: {e}")
tools/jsonl_hash_chain.py:191:                    ViolationType.HASH_RECALCULATION.value,
tools/jsonl_hash_chain.py:198:            expected_genesis = compute_genesis_hash(entry["scope"], entry["schema_version"])
tools/jsonl_hash_chain.py:199:            if entry["prev_hash"] != expected_genesis:
tools/jsonl_hash_chain.py:204:                        ViolationType.GENESIS_MISMATCH.value,
tools/jsonl_hash_chain.py:205:                        f"first entry prev_hash={entry['prev_hash']!r} != genesis={expected_genesis!r}",
tools/jsonl_hash_chain.py:214:                        ViolationType.PREV_HASH_MISMATCH.value,
tools/jsonl_hash_chain.py:219:        # Timestamp monotonicity (ADR-012 §3.4)
tools/jsonl_hash_chain.py:229:                    "monotonicity_violation",
tools/jsonl_hash_chain.py:230:                    f"ts={entry['ts']!r} < prior ts (ADR-012 §3.4 monotonicity)",
tools/jsonl_hash_chain.py:258:        if v.violation_type in {vt.value for vt in ViolationType}
tools/jsonl_hash_chain.py:261:        # schema/monotonicity 위반만 — chain_violation_detected 자동 작성 영역 외
tools/jsonl_hash_chain.py:267:        prev_hash = last_entry.get("hash", compute_genesis_hash(
tools/jsonl_hash_chain.py:272:        prev_hash = compute_genesis_hash("global", SUPPORTED_SCHEMA_VERSION)
tools/jsonl_hash_chain.py:285:            "violation_type": chain_violations[0].violation_type,
tools/jsonl_hash_chain.py:314:                        violation_type="parse_error",
tools/jsonl_hash_chain.py:324:                        violation_type="parse_error",
tools/jsonl_hash_chain.py:375:            f"PASS: {path.name} — {len(entries)} entries, all checks passed (schema + chain + monotonicity)",
tools/jsonl_hash_chain.py:383:            f"  [{v.entry_index}] id={v.entry_id} type={v.violation_type}",
.github/workflows/g4-hash-chain.yml:15:#   - FAIL fixture × 4: jsonl_hash_chain.py rc=1 + 4 violation_type cover
.github/workflows/g4-hash-chain.yml:28:      - "tools/canonical_json.py"
.github/workflows/g4-hash-chain.yml:31:      - "tests/canonical/**"
.github/workflows/g4-hash-chain.yml:76:          for inp in tests/canonical/*/*.input.json; do
.github/workflows/g4-hash-chain.yml:78:            exp_canonical="${base}.expected.canonical"
.github/workflows/g4-hash-chain.yml:81:            if ! python tools/canonical_json.py --mode primary_1_only --input "$inp" \
.github/workflows/g4-hash-chain.yml:82:                  --expected-canonical "$exp_canonical" \
.github/workflows/g4-hash-chain.yml:101:          for inp in tests/canonical/*/*.input.json; do
.github/workflows/g4-hash-chain.yml:103:            exp_canonical="${base}.expected.canonical"
.github/workflows/g4-hash-chain.yml:106:            if ! python tools/canonical_json.py --mode primary_2_only --input "$inp" \
.github/workflows/g4-hash-chain.yml:107:                  --expected-canonical "$exp_canonical" >/dev/null 2>err.log; then
.github/workflows/g4-hash-chain.yml:125:          for inp in tests/canonical/*/*.input.json; do
.github/workflows/g4-hash-chain.yml:127:            exp_canonical="${base}.expected.canonical"
.github/workflows/g4-hash-chain.yml:129:            if ! python tools/canonical_json.py --mode cross_check --input "$inp" \
.github/workflows/g4-hash-chain.yml:130:                  --expected-canonical "$exp_canonical" >/dev/null 2>err.log; then
.github/workflows/g4-hash-chain.yml:148:          for inp in tests/canonical/*/*.input.json; do
.github/workflows/g4-hash-chain.yml:150:            exp_canonical="${base}.expected.canonical"
.github/workflows/g4-hash-chain.yml:152:            if ! python tools/canonical_json.py --mode primary_1_only --input "$inp" \
.github/workflows/g4-hash-chain.yml:153:                  --expected-canonical "$exp_canonical" \
.github/workflows/g4-hash-chain.yml:172:                                  ("jcs", lambda v: jcs.canonicalize({"n": v}))]:
.github/workflows/g4-hash-chain.yml:197:      - name: FAIL fixture — jsonl_hash_chain rc=1 + 4 violation_type cover
.github/workflows/g4-hash-chain.yml:200:          # Expected violation_type per fixture (4 패턴 cover 강제)
.github/workflows/g4-hash-chain.yml:205:            [genesis_mismatch.jsonl]=genesis_mismatch
.github/workflows/g4-hash-chain.yml:220:              echo "::error::FAIL fixture $name missing violation_type=$expected"
.github/workflows/g4-hash-chain.yml:223:            echo "  $name OK (rc=1, violation_type=$expected)"
.github/workflows/g4-hash-chain.yml:226:          echo "FAIL fixtures verified — 4 violation_type cover (chain violation 4 패턴 답습)"
.github/workflows/g4-hash-chain.yml:254:          echo "- chain violation cover: 4 패턴 (prev_hash_mismatch + hash_recalculation + schema_missing_field + genesis_mismatch)" >> $GITHUB_STEP_SUMMARY

exec
/bin/bash -lc "sed -n '1,220p' src/adapters/llm/facade.py" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
"""LLMFacade — Provider-agnostic facade (G2 GP-5 placeholder).

본 파일은 *유일하게* LiteLLM 직접 import 가 *허용되는 경로* 입니다 (§4.1 답습).
현 시점은 **placeholder** — real 본문 작성 시 자동 풀 3+1 합의 trigger TR-1 발화.

답습 출처:
  - docs/architecture/llm-providers-design.md §4.1 (정확히 이 파일만 LiteLLM 직접 import)
  - docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md §2.3 (Hermes PMO ↔ provider 영구 권위)
  - docs/review/3plus1-consensus-2026-05-10-g2-gp5-poc2-depcruise-full.md §5.4 TR-1
  - docs/phase0/g2-gp5-poc2-depcruise-rule-scope.md §2.1
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class LLMRequest:
    alias: str
    messages: list[dict[str, str]]
    metadata: dict[str, Any] | None = None


@dataclass(frozen=True)
class LLMResponse:
    content: str
    metadata: dict[str, Any]


class LLMFacade:
    """Placeholder — real LiteLLM import + Router 위임은 TR-1 발화 시 작성."""

    def __init__(self, registry_path: str) -> None:
        self._registry_path = registry_path

    def complete(self, request: LLMRequest) -> LLMResponse:
        raise NotImplementedError("Placeholder — TR-1 풀 3+1 합의 후 real 본문 작성")

    async def health(self) -> dict[str, bool]:
        return {}

exec
/bin/bash -lc "find agent -maxdepth 2 -type f -print 2>/dev/null || true; find .github/workflows -maxdepth 1 -type f -printf '%f\\n' | sort" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
boundary-guard.yml
evidence-pass-gate.yml
g4-hash-chain.yml
history-anchor-verifier.yml
memory-skill-migration-feasibility.yml
pre-commit-bypass-detection.yml
provider-adapter-enforcement.yml
provider-url-scanner.yml
r2-canary.yml
rewrite-defense.yml
schema-validation.yml
secret-hygiene-egress-redaction.yml

exec
/bin/bash -lc "git config --local --get receive.denyNonFastForwards; printf 'local_rc=%s\\n' \""'$?"; git config --global --get receive.denyNonFastForwards; printf '"'global_rc=%s\\n' \""'$?"' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
local_rc=1
global_rc=1

exec
/bin/bash -lc 'rg -n "pyjcs|rfc8785|jcs|jq|import rfc8785|import jcs|subprocess|fallback|cross_check|primary_" tools/canonical_json.py requirements* pyproject.toml setup.cfg setup.py 2>/dev/null || true' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
requirements-dev.txt:17:#   - docs/review/3plus1-consensus-2026-05-10-g4-jcs-library-selection.md (Q1 풀 3+1 합의 17 조건)
requirements-dev.txt:18:#   - docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md §3 (사용자 명시 결정 갱신 — pyjcs PyPI 미존재 → jcs 대체)
requirements-dev.txt:20:rfc8785==0.1.4
requirements-dev.txt:21:jcs==0.2.1
tools/canonical_json.py:5:  - docs/decisions/ADR-012-evidence-ledger-protection.md §2.5 (RFC 8785 JCS Primary + jq fallback + corpus 검증 ≥20개)
tools/canonical_json.py:7:  - docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md §3 (사용자 명시 결정 갱신 — rfc8785 + jcs 병렬 cross-check)
tools/canonical_json.py:8:  - docs/review/3plus1-consensus-2026-05-10-g4-jcs-library-selection.md (Q1 풀 3+1 합의 17 조건)
tools/canonical_json.py:12:  - Primary 1: rfc8785 (Trail of Bits, Apache-2.0, RA-9 §B.2 11/11 sanity PASS)
tools/canonical_json.py:13:  - Primary 2: jcs (titusz, Apache-2.0, RA-9 §B.2 11/11 sanity PASS)
tools/canonical_json.py:14:  - Fallback: jq -S -c (POSIX 표준, ADR-012 §2.5 명시 답습)
tools/canonical_json.py:17:  - Fallback 사용 시 = `event: canonical_json_fallback` ledger entry 작성 의무 (caller 책임)
tools/canonical_json.py:27:import subprocess
tools/canonical_json.py:34:    import rfc8785  # Primary 1 (Trail of Bits)
tools/canonical_json.py:36:    rfc8785 = None  # type: ignore[assignment]
tools/canonical_json.py:39:    import jcs  # Primary 2 (titusz)
tools/canonical_json.py:41:    jcs = None  # type: ignore[assignment]
tools/canonical_json.py:47:    - PRIMARY_1_ONLY: rfc8785 단독 사용 (runtime 1× 권고)
tools/canonical_json.py:48:    - PRIMARY_2_ONLY: jcs 단독 사용 (테스트/디버깅용)
tools/canonical_json.py:49:    - CROSS_CHECK: rfc8785 + jcs 동시 호출, 출력 byte 동등성 + sha256 동등성 강제 (corpus 시점 권고)
tools/canonical_json.py:50:    - FALLBACK_JQ: jq -S -c subprocess (Primary install 실패 시, canonical_json_fallback entry 의무)
tools/canonical_json.py:53:    PRIMARY_1_ONLY = "primary_1_only"
tools/canonical_json.py:54:    PRIMARY_2_ONLY = "primary_2_only"
tools/canonical_json.py:55:    CROSS_CHECK = "cross_check"
tools/canonical_json.py:56:    FALLBACK_JQ = "fallback_jq"
tools/canonical_json.py:64:    """rfc8785 + jcs cross-check 출력 불일치 — TR-C-2 escalation trigger."""
tools/canonical_json.py:74:    fallback_used: bool = False
tools/canonical_json.py:75:    cross_check_passed: bool | None = None  # None = N/A, True/False = cross-check 결과
tools/canonical_json.py:78:def _to_canonical_rfc8785(obj: Any) -> bytes:
tools/canonical_json.py:79:    """Primary 1 — rfc8785 (Trail of Bits)."""
tools/canonical_json.py:80:    if rfc8785 is None:
tools/canonical_json.py:81:        raise CanonicalizationError("rfc8785 라이브러리 미설치 — `pip install rfc8785==0.1.4`")
tools/canonical_json.py:82:    out = rfc8785.dumps(obj)
tools/canonical_json.py:86:def _to_canonical_jcs(obj: Any) -> bytes:
tools/canonical_json.py:87:    """Primary 2 — jcs (titusz)."""
tools/canonical_json.py:88:    if jcs is None:
tools/canonical_json.py:89:        raise CanonicalizationError("jcs 라이브러리 미설치 — `pip install jcs==0.2.1`")
tools/canonical_json.py:90:    out = jcs.canonicalize(obj)
tools/canonical_json.py:94:def _to_canonical_jq_fallback(obj: Any) -> bytes:
tools/canonical_json.py:95:    """Fallback — jq -S -c subprocess.
tools/canonical_json.py:98:    `event: canonical_json_fallback` ledger entry 작성 의무.
tools/canonical_json.py:100:    jq_path = shutil.which("jq")
tools/canonical_json.py:101:    if jq_path is None:
tools/canonical_json.py:103:            "jq fallback 불가 — `jq` POSIX 도구 미설치 (apt install jq / brew install jq)"
tools/canonical_json.py:107:        result = subprocess.run(
tools/canonical_json.py:108:            [jq_path, "-S", "-c", "."],
tools/canonical_json.py:114:    except subprocess.CalledProcessError as e:
tools/canonical_json.py:116:            f"jq fallback subprocess 실패 — rc={e.returncode} stderr={e.stderr.decode('utf-8', 'replace')[:200]}"
tools/canonical_json.py:127:        mode: CrossCheckMode (기본 PRIMARY_1_ONLY — rfc8785 단독, runtime 1× 권고)
tools/canonical_json.py:130:        CanonicalResult (canonical bytes + sha256 hex + mode used + fallback/cross-check flag)
tools/canonical_json.py:133:        CanonicalizationError: NaN/Inf reject 또는 라이브러리 미설치 또는 jq 실패
tools/canonical_json.py:134:        CrossCheckMismatchError: CROSS_CHECK 모드에서 rfc8785 ↔ jcs 출력 불일치 (TR-C-2 trigger)
tools/canonical_json.py:136:    fallback_used = False
tools/canonical_json.py:137:    cross_check_passed: bool | None = None
tools/canonical_json.py:140:        canonical = _to_canonical_rfc8785(obj)
tools/canonical_json.py:142:        canonical = _to_canonical_jcs(obj)
tools/canonical_json.py:144:        out_p1 = _to_canonical_rfc8785(obj)
tools/canonical_json.py:145:        out_p2 = _to_canonical_jcs(obj)
tools/canonical_json.py:148:                f"rfc8785 ↔ jcs cross-check 불일치 — TR-C-2 escalation. "
tools/canonical_json.py:149:                f"rfc8785={out_p1[:80]!r} jcs={out_p2[:80]!r}"
tools/canonical_json.py:152:        cross_check_passed = True
tools/canonical_json.py:154:        canonical = _to_canonical_jq_fallback(obj)
tools/canonical_json.py:155:        fallback_used = True
tools/canonical_json.py:164:        fallback_used=fallback_used,
tools/canonical_json.py:165:        cross_check_passed=cross_check_passed,
tools/canonical_json.py:170:    """CLI — corpus 회귀 + cross-check + fallback 동등성 검증."""
tools/canonical_json.py:178:        help="Cross-check mode (default: cross_check)",
tools/canonical_json.py:199:        "--verify-fallback-equiv",
tools/canonical_json.py:201:        help="jq fallback 출력과 byte 동등성 검증",
tools/canonical_json.py:229:        f"fallback_used={result.fallback_used} cross_check_passed={result.cross_check_passed}",
tools/canonical_json.py:263:    if args.verify_fallback_equiv:
tools/canonical_json.py:268:                    f"FALLBACK_EQUIV_FAIL: primary={result.canonical[:80]!r} jq={fb_result.canonical[:80]!r}",
tools/canonical_json.py:273:                print("# fallback equivalence: OK", file=sys.stderr)

exec
/bin/bash -lc "sed -n '1,280p' .github/workflows/g4-hash-chain.yml" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
# G4 JSONL Hash Chain + RFC 8785 JCS + Round-trip — Group C PoC
#
# 답습 출처:
#   - docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md (본 PoC 사양 §6)
#   - docs/review/3plus1-consensus-2026-05-10-g4-jcs-library-selection.md (Q1 풀 3+1 합의 17 조건)
#   - docs/review/3plus1-consensus-2026-05-10-g4-corpus-poc-scope-short.md (Q2/Q3 단축 합의 6 조건)
#   - docs/decisions/ADR-012-evidence-ledger-protection.md §2.5 (RFC 8785 JCS Primary + jq fallback + corpus 검증)
#   - docs/architecture/provider-agnostic-memory-skill-design.md §4.4 (hash chain) + §4.6 (round-trip)
#   - .github/workflows/evidence-pass-gate.yml (Group B 시제 직접 답습)
#
# 본 workflow 의 양방향 검증:
#   - corpus 24 회귀 (Primary 1 rfc8785 + Primary 2 jcs cross-check + sha256 일관성)
#   - NaN/Inf reject 2건 (양 라이브러리 모두 raise 검증)
#   - PASS fixture × 2: jsonl_hash_chain.py rc=0
#   - FAIL fixture × 4: jsonl_hash_chain.py rc=1 + 4 violation_type cover
#   - Round-trip PASS fixture: jsonl_roundtrip.py rc=0 (T2 strict)
#
# 본 PoC 는 G4 *부분 충족 시제* 한정 — G4 전체 PASS 권한 0건 (사용자 명시 답습).
name: G4 Hash Chain + JCS

on:
  push:
    branches:
      - main
      - develop
      - "feature/**"
    paths:
      - "tools/canonical_json.py"
      - "tools/jsonl_hash_chain.py"
      - "tools/jsonl_roundtrip.py"
      - "tests/canonical/**"
      - "tests/fixtures/jsonl_ledger/**"
      - ".github/workflows/g4-hash-chain.yml"
      - "requirements-dev.txt"
  pull_request:
    branches:
      - main
      - develop

permissions:
  contents: read

jobs:
  enforce:
    runs-on: ubuntu-latest
    timeout-minutes: 10
    env:
      PYTHONPATH: tools
    steps:
      - name: Checkout
        uses: actions/checkout@v6

      - name: Set up Python
        uses: actions/setup-python@v6
        with:
          python-version: "3.12"

      - name: Install jq (POSIX fallback)
        run: |
          sudo apt-get update -qq
          sudo apt-get install -y jq
          jq --version

      - name: Install Primary 1 + Primary 2 (Q1 합의 R-A2 답습)
        run: |
          python -m pip install --upgrade pip
          # 본 PoC 한정 의존만 설치 (import-linter 등 G2 전용 dep 제외)
          pip install rfc8785==0.1.4 jcs==0.2.1
          python -c "import rfc8785, jcs; print('rfc8785:', rfc8785.__file__); print('jcs:', jcs.__file__)"

      - name: Corpus regression — Primary 1 (rfc8785) byte + sha256
        run: |
          set -e
          fail=0
          total=0
          for inp in tests/canonical/*/*.input.json; do
            base="${inp%.input.json}"
            exp_canonical="${base}.expected.canonical"
            exp_sha256="${base}.expected.sha256"
            total=$((total + 1))
            if ! python tools/canonical_json.py --mode primary_1_only --input "$inp" \
                  --expected-canonical "$exp_canonical" \
                  --expected-sha256 "$exp_sha256" >/dev/null 2>err.log; then
              echo "::error::Primary 1 regression FAIL: $inp"
              cat err.log
              fail=$((fail + 1))
            fi
          done
          rm -f err.log
          echo "Primary 1 corpus: ${total} cases, ${fail} fail"
          if [ "$fail" -ne 0 ]; then
            echo "::error::Primary 1 (rfc8785) corpus regression: $fail / $total cases failed"
            exit 1
          fi

      - name: Corpus regression — Primary 2 (jcs) cross-check (TR-C-2 답습)
        run: |
          set -e
          fail=0
          total=0
          for inp in tests/canonical/*/*.input.json; do
            base="${inp%.input.json}"
            exp_canonical="${base}.expected.canonical"
            total=$((total + 1))
            # Primary 2 단독 + expected 비교 (Q1 합의 D-1 — corpus 시점 cross-check 강제)
            if ! python tools/canonical_json.py --mode primary_2_only --input "$inp" \
                  --expected-canonical "$exp_canonical" >/dev/null 2>err.log; then
              echo "::error::Primary 2 regression FAIL: $inp"
              cat err.log
              fail=$((fail + 1))
            fi
          done
          rm -f err.log
          echo "Primary 2 corpus: ${total} cases, ${fail} fail"
          if [ "$fail" -ne 0 ]; then
            echo "::error::Primary 2 (jcs) corpus regression: $fail / $total cases failed (TR-C-2 escalation)"
            exit 1
          fi

      - name: Corpus regression — cross_check mode (Primary 1 ↔ Primary 2 byte equivalence)
        run: |
          set -e
          fail=0
          total=0
          for inp in tests/canonical/*/*.input.json; do
            base="${inp%.input.json}"
            exp_canonical="${base}.expected.canonical"
            total=$((total + 1))
            if ! python tools/canonical_json.py --mode cross_check --input "$inp" \
                  --expected-canonical "$exp_canonical" >/dev/null 2>err.log; then
              echo "::error::cross_check FAIL: $inp"
              cat err.log
              fail=$((fail + 1))
            fi
          done
          rm -f err.log
          echo "cross_check corpus: ${total} cases, ${fail} fail"
          if [ "$fail" -ne 0 ]; then
            echo "::error::cross_check corpus: $fail / $total cases failed (TR-C-2 escalation)"
            exit 1
          fi

      - name: Fallback equivalence — jq -S -c vs Primary 1
        run: |
          set -e
          fail=0
          total=0
          for inp in tests/canonical/*/*.input.json; do
            base="${inp%.input.json}"
            exp_canonical="${base}.expected.canonical"
            total=$((total + 1))
            if ! python tools/canonical_json.py --mode primary_1_only --input "$inp" \
                  --expected-canonical "$exp_canonical" \
                  --verify-fallback-equiv >/dev/null 2>err.log; then
              echo "::warning::jq fallback equivalence DIFF: $inp"
              cat err.log
              fail=$((fail + 1))
            fi
          done
          rm -f err.log
          echo "jq fallback equivalence: ${total} cases, ${fail} differ"
          # jq fallback 동등성 실패는 warning 한정 (ADR-012 §2.5 — `Fallback 사용 빈도 > 10%` 별도 합의 trigger 답습)

      - name: NaN/Inf reject (Q1 합의 C-B8 + 본 합의 C-Q2 답습)
        run: |
          python - <<'PY'
          import sys
          import rfc8785, jcs
          fail = 0
          for label, val in [("nan", float("nan")), ("inf", float("inf")), ("-inf", float("-inf"))]:
              for libname, fn in [("rfc8785", lambda v: rfc8785.dumps({"n": v})),
                                  ("jcs", lambda v: jcs.canonicalize({"n": v}))]:
                  try:
                      fn(val)
                      print(f"FAIL: {libname} accepted {label} (RFC 8785 §3.2.2.2 violation)")
                      fail += 1
                  except (ValueError, Exception) as e:
                      print(f"OK: {libname} rejected {label}: {type(e).__name__}")
          sys.exit(1 if fail else 0)
          PY

      - name: PASS fixture — jsonl_hash_chain rc=0 (× 2)
        run: |
          set -e
          for f in tests/fixtures/jsonl_ledger/pass/*.jsonl; do
            set +e
            python tools/jsonl_hash_chain.py "$f"
            rc=$?
            set -e
            if [ "$rc" -ne 0 ]; then
              echo "::error::PASS fixture $f returned rc=$rc (expected 0)"
              exit 1
            fi
          done
          echo "PASS fixtures verified (rc=0 for all)"

      - name: FAIL fixture — jsonl_hash_chain rc=1 + 4 violation_type cover
        run: |
          set -e
          # Expected violation_type per fixture (4 패턴 cover 강제)
          declare -A EXPECTED=(
            [prev_hash_mismatch.jsonl]=prev_hash_mismatch
            [hash_recalculation.jsonl]=hash_recalculation
            [missing_event_field.jsonl]=schema_missing_field
            [genesis_mismatch.jsonl]=genesis_mismatch
          )
          for f in tests/fixtures/jsonl_ledger/fail/*.jsonl; do
            name=$(basename "$f")
            expected="${EXPECTED[$name]:-}"
            set +e
            python tools/jsonl_hash_chain.py "$f" 2> chain_out.txt
            rc=$?
            set -e
            cat chain_out.txt
            if [ "$rc" -ne 1 ]; then
              echo "::error::FAIL fixture $name returned rc=$rc (expected 1)"
              exit 1
            fi
            if [ -n "$expected" ] && ! grep -q "type=$expected" chain_out.txt; then
              echo "::error::FAIL fixture $name missing violation_type=$expected"
              exit 1
            fi
            echo "  $name OK (rc=1, violation_type=$expected)"
          done
          rm -f chain_out.txt
          echo "FAIL fixtures verified — 4 violation_type cover (chain violation 4 패턴 답습)"

      - name: Round-trip — T2 strict on PASS fixtures
        run: |
          set -e
          for f in tests/fixtures/jsonl_ledger/pass/*.jsonl; do
            set +e
            python tools/jsonl_roundtrip.py --require-strict "$f"
            rc=$?
            set -e
            if [ "$rc" -ne 0 ]; then
              echo "::error::Round-trip T2 strict FAIL on $f (rc=$rc, TR-C-4 trigger)"
              exit 1
            fi
            echo "  $(basename $f) — T2 strict PASS"
          done

      - name: Evidence summary
        if: always()
        run: |
          echo "## G4 Hash Chain + JCS — Evidence" >> $GITHUB_STEP_SUMMARY
          echo "- commit: ${{ github.sha }}" >> $GITHUB_STEP_SUMMARY
          echo "- ref: ${{ github.ref }}" >> $GITHUB_STEP_SUMMARY
          echo "- run: ${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}" >> $GITHUB_STEP_SUMMARY
          echo "- event: g4_hash_chain_jcs_layer1" >> $GITHUB_STEP_SUMMARY
          echo "- agent: user" >> $GITHUB_STEP_SUMMARY
          echo "- ledger_layer: Layer 1 — Hash Chain + Canonical JSON + Round-trip (Group C PoC)" >> $GITHUB_STEP_SUMMARY
          echo "- corpus: 24 cases × 4 axes (Primary 1 + Primary 2 + cross_check + jq fallback)" >> $GITHUB_STEP_SUMMARY
          echo "- chain violation cover: 4 패턴 (prev_hash_mismatch + hash_recalculation + schema_missing_field + genesis_mismatch)" >> $GITHUB_STEP_SUMMARY
          echo "- round-trip: T2 strict (PASS fixtures)" >> $GITHUB_STEP_SUMMARY
          echo "- numeric reject: NaN + Inf + -Inf (rfc8785 + jcs)" >> $GITHUB_STEP_SUMMARY
          echo "- PASS scope: G4 *부분 충족 시제* 한정 (G4 전체 PASS 권한 0건, 사용자 명시 답습)" >> $GITHUB_STEP_SUMMARY

exec
/bin/bash -lc "sed -n '1,120p' requirements-dev.txt" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
# Dev-only dependencies (G2 GP-5 2차 PoC — TR-2 발화 답습)
#
# 답습 출처:
#   - docs/review/3plus1-consensus-2026-05-10-g2-gp5-poc2-depcruise-full.md §5.4 TR-2
#   - docs/phase0/g2-gp5-poc2-depcruise-rule-scope.md §8.1 T-2 (import-linter)
#   - C-9 RA-9 사전 검증 PASS (2026-05-10)
#
# 본 manifest 는 dev-dep 만 등재. runtime application 의존성 0건.
# pyproject.toml (PEP 621) 신설은 *별도 합의* 답습 (R-RF2 답습).

# Provider Adapter Enforcement Layer 1 (Static graph)
# C-9 검증 환경: import-linter 2.11 + grimp 3.14
import-linter==2.11

# Group C PoC — RFC 8785 JCS Primary 1 + Primary 2 cross-check
# 답습 출처:
#   - docs/review/3plus1-consensus-2026-05-10-g4-jcs-library-selection.md (Q1 풀 3+1 합의 17 조건)
#   - docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md §3 (사용자 명시 결정 갱신 — pyjcs PyPI 미존재 → jcs 대체)
# 양 라이브러리 모두 Apache-2.0 + 의존성 0 + RA-9 §B.2 11/11 sanity 동등성 PASS
rfc8785==0.1.4
jcs==0.2.1

# Jarvis 오케스트레이터 MVP-0 트랙 A — 단위 테스트 (TDD)
# 답습 출처:
#   - docs/phase0/jarvis-orchestrator-mvp-design-brief.md (v4, MVP-0 트랙 A)
#   - docs/review/3plus1-consensus-2026-05-22-jarvis-orchestrator-mvp-v4-reviewer.md (APPROVE)
# runtime application 의존성 0건 유지 (test-only).
pytest==9.0.3
pytest-cov==7.1.0

# PC-1-T3 mandatory enforcement (MVP-1 1.5차 보강 sub-cycle)
# 답습 출처:
#   - docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md
#   - docs/review/3plus1-consensus-2026-05-27-mvp1-pc1-t3-mandatory-enforcement.md (Reviewer-only APPROVE)
# `.pre-commit-config.yaml` framework hook 6 (T2 opt-in 발효 `3c0a1c1`) → T3 dev 환경 mandatory enforcement
# bin/setup.sh 가 `pre-commit install` 자동 실행 (Layer 2 framework hook 활성화)
pre-commit==4.0.1

# S-3 detect-secrets 부분 통합 (MVP-1 1.5차 보강 sub-cycle)
# 답습 출처:
#   - docs/phase0/mvp1-s3-detect-secrets-partial-integration-brief.md
#   - docs/review/3plus1-consensus-2026-05-27-mvp1-s3-detect-secrets-partial-integration.md (Reviewer-only APPROVE)
# Tier-1 답습 plugin 5종 한정 (AWSKeyDetector / KeywordDetector / Base64HighEntropyString
#   / HexHighEntropyString / PrivateKeyDetector) — Tier-2/3 확장 = R-MVP1-1.5-S3-1 풀 3+1 trigger
# --baseline 영구 금지 (R-MVP1-1.5-S3-2 silenceable risk)
# S-1 (tools/secret_scanner.py) 답습 유지 영구 의무 (R-MVP1-1.5-S3-3 Defense in depth)
detect-secrets==1.5.0

exec
/bin/bash -lc 'rg -n "pip install|requirements-dev|rfc8785|jcs|jq" .github/workflows/g4-hash-chain.yml .github/workflows/history-anchor-verifier.yml .github/workflows/rewrite-defense.yml' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
.github/workflows/rewrite-defense.yml:6:#   - .github/workflows/history-anchor-verifier.yml (Group C 후속 형식 직접 답습 — rfc8785+jcs install 포함)
.github/workflows/rewrite-defense.yml:57:      - name: Install Group C deps (rfc8785 + jcs — Group C `parse_jsonl` 의존)
.github/workflows/rewrite-defense.yml:59:          python -m pip install --upgrade pip
.github/workflows/rewrite-defense.yml:60:          # parse_jsonl → canonical_json → rfc8785 의존성 답습
.github/workflows/rewrite-defense.yml:61:          pip install rfc8785==0.1.4 jcs==0.2.1
.github/workflows/rewrite-defense.yml:62:          python -c "import rfc8785, jcs; print('rfc8785 + jcs OK')"
.github/workflows/history-anchor-verifier.yml:56:      - name: Install Group C deps (rfc8785 + jcs — Group C `compute_entry_hash` 의존)
.github/workflows/history-anchor-verifier.yml:58:          python -m pip install --upgrade pip
.github/workflows/history-anchor-verifier.yml:59:          # validate_chain → compute_entry_hash → canonical_json → rfc8785 의존성 답습
.github/workflows/history-anchor-verifier.yml:60:          pip install rfc8785==0.1.4 jcs==0.2.1
.github/workflows/history-anchor-verifier.yml:61:          python -c "import rfc8785, jcs; print('rfc8785 + jcs OK')"
.github/workflows/g4-hash-chain.yml:4:#   - docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md (본 PoC 사양 §6)
.github/workflows/g4-hash-chain.yml:5:#   - docs/review/3plus1-consensus-2026-05-10-g4-jcs-library-selection.md (Q1 풀 3+1 합의 17 조건)
.github/workflows/g4-hash-chain.yml:7:#   - docs/decisions/ADR-012-evidence-ledger-protection.md §2.5 (RFC 8785 JCS Primary + jq fallback + corpus 검증)
.github/workflows/g4-hash-chain.yml:12:#   - corpus 24 회귀 (Primary 1 rfc8785 + Primary 2 jcs cross-check + sha256 일관성)
.github/workflows/g4-hash-chain.yml:34:      - "requirements-dev.txt"
.github/workflows/g4-hash-chain.yml:58:      - name: Install jq (POSIX fallback)
.github/workflows/g4-hash-chain.yml:61:          sudo apt-get install -y jq
.github/workflows/g4-hash-chain.yml:62:          jq --version
.github/workflows/g4-hash-chain.yml:66:          python -m pip install --upgrade pip
.github/workflows/g4-hash-chain.yml:68:          pip install rfc8785==0.1.4 jcs==0.2.1
.github/workflows/g4-hash-chain.yml:69:          python -c "import rfc8785, jcs; print('rfc8785:', rfc8785.__file__); print('jcs:', jcs.__file__)"
.github/workflows/g4-hash-chain.yml:71:      - name: Corpus regression — Primary 1 (rfc8785) byte + sha256
.github/workflows/g4-hash-chain.yml:92:            echo "::error::Primary 1 (rfc8785) corpus regression: $fail / $total cases failed"
.github/workflows/g4-hash-chain.yml:96:      - name: Corpus regression — Primary 2 (jcs) cross-check (TR-C-2 답습)
.github/workflows/g4-hash-chain.yml:116:            echo "::error::Primary 2 (jcs) corpus regression: $fail / $total cases failed (TR-C-2 escalation)"
.github/workflows/g4-hash-chain.yml:143:      - name: Fallback equivalence — jq -S -c vs Primary 1
.github/workflows/g4-hash-chain.yml:155:              echo "::warning::jq fallback equivalence DIFF: $inp"
.github/workflows/g4-hash-chain.yml:161:          echo "jq fallback equivalence: ${total} cases, ${fail} differ"
.github/workflows/g4-hash-chain.yml:162:          # jq fallback 동등성 실패는 warning 한정 (ADR-012 §2.5 — `Fallback 사용 빈도 > 10%` 별도 합의 trigger 답습)
.github/workflows/g4-hash-chain.yml:168:          import rfc8785, jcs
.github/workflows/g4-hash-chain.yml:171:              for libname, fn in [("rfc8785", lambda v: rfc8785.dumps({"n": v})),
.github/workflows/g4-hash-chain.yml:172:                                  ("jcs", lambda v: jcs.canonicalize({"n": v}))]:
.github/workflows/g4-hash-chain.yml:250:          echo "- event: g4_hash_chain_jcs_layer1" >> $GITHUB_STEP_SUMMARY
.github/workflows/g4-hash-chain.yml:253:          echo "- corpus: 24 cases × 4 axes (Primary 1 + Primary 2 + cross_check + jq fallback)" >> $GITHUB_STEP_SUMMARY
.github/workflows/g4-hash-chain.yml:256:          echo "- numeric reject: NaN + Inf + -Inf (rfc8785 + jcs)" >> $GITHUB_STEP_SUMMARY

exec
/bin/bash -lc "python tools/secret_scanner.py --list-patterns >/tmp/secret_patterns.out 2>/tmp/secret_patterns.err; cat /tmp/secret_patterns.err; printf 'rc=%s\\n' \""'$?"' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
/bin/bash: line 1: python: command not found
rc=0

codex
실제 G4 PoC는 “stdlib 단독”이 아니라 이미 `rfc8785`와 `jcs`를 설치·사용하는 Group C PoC 흐름이 남아 있습니다. 이 부분은 brief의 L-4 명명/근거와 충돌 가능성이 커서, blocking 여부를 중심으로 판정하겠습니다.
exec
/bin/bash -lc 'rg -n "R-4|L-4|stdlib|외부 library|rfc8785|jcs|L-2|L-5|조건부 승인 조건 6|denyNonFastForwards|actual run|history_rewrite|violation_type" docs/phase0/mvp2-beta-submeans-decision-brief.md' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
5:> **scope**: MVP-2 영역 sub-수단 *결정* — R-1~R-5 (GP-2 송신 redaction) + L-1~L-5 (G4 §4.4 Layer 4 CI 회귀 검증) + W-A~E (workflow 통합 방식)
11:> **본 cycle 발효 효과** = R / L / W sub-수단 *결정 발효* + 후속 실 구현 sub-cycle 진입 자격 (조건부 승인 조건 6 입력). 실 구현 (denyNonFastForwards 활성화 + R-6 actual run + evidence 수집) = 별도 sub-cycle (본 cycle = 수단 결정 한정)
13:> **선행 답습**: 51 audit brief (R/L 후보 식별) + 52 (α) entry brief v1.1 (W-A~E 5 대안 확장) + 53 (γ) Layer 분리 + 54 (γ-c) 채택 발효 + 55 Layer 1+2+4 통합 PASS 격상 진입 합의 (조건부 승인 조건 6)
22:2. **L sub-수단 결정** (G4 §4.4 Layer 4 CI 회귀 검증) — L-1~L-5 中 채택 결정 권고 (§3)
26:6. **수단 결정 발효 후 실 구현 sub-cycle 입력 (조건부 승인 조건 6 매핑 + Rollback Trigger / Evidence)** (§7)
37:| 5 | **`git config receive.denyNonFastForwards true` 활성화 실행** | 0건 (실 구현 sub-cycle 영역) |
38:| 6 | R-6 workflow actual run 트리거 | 0건 (실 구현 sub-cycle) |
40:| 8 | **외부 library (`pyjcs` / `rfc8785`) 도입 결정** | 0건 (L-2 / L-5 = 별도 cycle, ADR-012 §2.1 R-2 / R-4.1 PoC 자동 재실행 trigger 답습) |
61:- **51 audit brief §2.3 (R-1~R-5) + §3.4 (L-1~L-5) + §4.2 (W-A/B)** — `docs/phase0/mvp2-entry-eligibility-audit-brief.md`
63:- **55 Layer 1+2+4 통합 PASS 격상 brief v1.1 §2.4 + §4.4 + §11.1 B-4 (조건부 승인 조건 6)** — `docs/phase0/mvp2-layer-124-pass-entry-brief.md`
77:| 55 Layer 1+2+4 통합 PASS 격상 진입 합의 (`311ca3b`, 4 source APPROVE WITH CONDITIONS) | Layer 1+2+4 PASS 격상 *진입 권한* 발효 답습 + 조건부 승인 조건 6 (실 구현 sub-cycle 입력) |
81:| 51 진입 자격 audit brief (`f7ac61d`) | **R-1~R-5 + L-1~L-5 후보 식별** (수단 결정 0) — 본 cycle = 51 후보 → 결정 |
92:| Layer 1 hash chain | ✅ `tools/jsonl_hash_chain.py` (14038B, genesis + 4 violation_type) + `g4-hash-chain.yml` (10652B) | **L-1 (stdlib) 시제 충족** |
93:| canonical JSON | ✅ `tools/canonical_json.py` (10055B, rfc8785 + jcs + jq -S -c fallback + cross-check mode) + `tests/canonical/` 72 files / 8 카테고리 | **L-1 fallback + cross-check 시제 충족** |
96:| Layer 2a denyNonFastForwards | ⚠️ **미설정** (local + global 0건, 55 §1.3 답습) | 실 구현 sub-cycle 활성화 |
98:→ ⭐ **핵심 함의**: R-3 (log canary CI) + L-1 (stdlib hash chain) + L-3 (R-6 step) = **모두 PoC 시제 *이미 충족***. 본 (β) cycle 의 수단 결정 = "신규 구현 수단 선택" 보다 **"기존 PoC 시제 → MANDATORY 채택 + PASS 격상 경로 확정"** 성격. R-1 (Hermes upstream) + R-2 (facade real) = 별도 trajectory 의존 (본 cycle = 결정 영역 명시, 구현 경로 결정 0).
120:| **R-4** | R-1 + R-2 + R-3 병행 (defense-in-depth) | 다층 redaction | 부분 (R-3 충족, R-1/R-2 trajectory) | R-1 + R-2 의존 | **51 audit 권고** |
125:⭐ **권고 R 결정 = R-4 (defense-in-depth 목적) 채택 + 구현 경로 차등 명시**:
128:2. **R-1 (Hermes upstream) + R-2 (facade real) = *결과* 의무이나 구현 경로 = 별도 trajectory**. 본 cycle = R-1/R-2 를 R-4 defense-in-depth 의 *목표 수단* 으로 채택하되, **구현 경로 결정 (Hermes import / facade real) = 별도 cycle** 명시 (§0.2 #9 #10).
131:→ **means-vs-ends 정합 (ADR-011)**: GP-2 의 *ends* (secret 송신/로그 leak 0) = R-4 다층으로 달성. 본 repo 內 *즉시 발효 가능 means* = R-3 (CI). R-1/R-2 = ends 충족 *보조 means*, 구현 = cross-trajectory 의존. **MVP-2 PASS 시점 GP-2 (a)~(e) 충족 = R-3 actual run PASS + R-1/R-2 evidence 가용 시점 합산** (실 구현 sub-cycle 영역).
137:| R-4 (권고) | defense-in-depth ends 충족 / R-3 즉시 발효 / 기존 시제 답습 | R-1/R-2 cross-trajectory 의존 → MVP-2 PASS 시점 GP-2 완전 충족이 Hermes import + facade real 에 부분 종속 (단, R-3 단독으로 (d) 자동 회귀 충족) |
141:→ **R-4 채택 + R-3 우선 발효 + R-1/R-2 cross-trajectory 의존 명시** 가 ceremony-inflation 차단 + 즉시 진전 + ends 충족 정합.
151:| **L-1** | Layer 1 hash chain Python stdlib 단독 (`hashlib.sha256` + `json.dumps(sort_keys, separators)`) | hash chain 검증 | stdlib | ✅ **시제 충족** (`jsonl_hash_chain.py` + `canonical_json.py` fallback) | fallback canonical, RFC 8785 동등성 test corpus 의무 (72 files 충족) |
152:| **L-2** | Layer 1 + RFC 8785 JCS Primary (`pyjcs` / `rfc8785` 외부 library) | hash chain + canonical | 외부 library 1+ | ⚠️ canonical_json.py 에 rfc8785/jcs import 시도 + jq fallback 이미 존재 (의존성 *결정* 0) | 의존성 추가 trigger (ADR-012 §2.1 R-2 / R-4.1 PoC 자동 재실행) |
153:| **L-3** | Layer 4 R-6 workflow step (canonical 위반 + prev_hash mismatch + timestamp monotonicity) | CI 회귀 | shell + Python stdlib | ✅ **시제 충족** (4 G4 workflow 분리 운영) | R-6 답습 확장 |
154:| **L-4** | L-1 + L-3 병행 (MVP 권고) | Layer 1+4 동시 | stdlib 단독 | ✅ 양쪽 시제 충족 | **51 audit 권고** |
155:| **L-5** | L-2 + L-3 병행 (정식 권고) | Layer 1+4 + JCS Primary | 외부 library 1+ | 부분 | 정식 채택 시점 (Operational Readiness 또는 별도 cycle) |
159:⭐ **권고 L 결정 = L-4 (L-1 stdlib + L-3 CI step) 채택**:
161:1. **L-1 (stdlib hash chain) = MVP 단계 정합** — 외부 의존성 0, `jsonl_hash_chain.py` + `canonical_json.py` (rfc8785 *시도* + jq fallback + cross-check mode) 시제 충족. RFC 8785 동등성 = `tests/canonical/` 72 files corpus 로 검증 (≥ 20 reference 충족).
163:3. **L-2 / L-5 (외부 library JCS Primary) = 별도 cycle 영구 분리** — 외부 library (`pyjcs` / `rfc8785`) 도입 = ADR-012 §2.1 R-2 / R-4.1 PoC 자동 재실행 trigger 발화 (Provider Liquidity 와 무관하나 의존성 추가 거버넌스 발화). 단, **canonical_json.py 가 이미 rfc8785/jcs *조건부 import + fallback* 구조** → L-1 의 RFC 8785 정합성은 fallback 동등성으로 확보, 외부 library *강제 의존* 0.
165:→ **means-vs-ends 정합**: Layer 4 의 *ends* (ledger 무결성 자동 회귀 검증) = L-4 로 달성. stdlib 단독 (L-1) = "동등 이상 보안 결과" (ADR-011 §2.1 (a)) — RFC 8785 reference corpus 동등성으로 입증. 외부 library = MVP 단계 불필요 (L-5 = 정식 단계 deferred).
171:| L-4 (권고) | 외부 의존 0 / 시제 충족 / Provider Liquidity·거버넌스 마찰 0 / 즉시 PASS 격상 | RFC 8785 strict 정합 = fallback 동등성 의존 (corpus 72 files 로 완화) |
172:| L-5 (외부 JCS) | RFC 8785 strict Primary | 외부 library 의존성 추가 → ADR-012 §2.1 PoC 자동 재실행 + 거버넌스 cycle 부담 (MVP 단계 과잉) |
215:| **R** | R-4 (R-3 우선 + R-1/R-2 결과 의무) | R-3 ✅ (시제 충족) | R-1 = Hermes import / R-2 = facade real (TR-1) |
216:| **L** | L-4 (L-1 stdlib + L-3 step) | ✅ (양쪽 시제 충족) | 없음 (L-5 외부 library = 별도) |
221:✅ **R-4 / L-4 / W 보존우선 sub-수단 *결정 발효*** (51 후보 → 결정)
222:✅ **후속 실 구현 sub-cycle 진입 자격 발효** (조건부 승인 조건 6 입력, §7)
225:✅ **L-2 / L-5 (외부 library) + R-5 (evasion) = 영구 분리 확정** (deferred)
229:❌ 실 구현 자체 (denyNonFastForwards 활성화 / R-6 actual run / step 추가 / evidence 수집) = 실 구현 sub-cycle
231:❌ 외부 library (L-2/L-5) 도입 결정 = 별도 cycle
242:1. 55 entry §8 #1 "(β) sub-수단 결정 cycle — R-1~R-5 + L-1~L-5 + W-A~E — 풀 3+1" 직접 답습
245:4. 헌법 5조-2 Provider Liquidity (cross-vendor 의무) — 단 L-2/L-5 외부 library *결정 0* 이므로 Provider Liquidity 직접 충돌 0
251:| 1 | 큰 결정 (sub-수단 *결정* / threshold 고정) | ✅ **발화** | R-4 / L-4 / W 수단 *결정* = 실 구현 직전 마지막 합의 |
265:| R-4 / L-4 (defense-in-depth + stdlib) | 풀 검토 | 51 audit 권고 답습이나 cross-trajectory 의존 (R-1/R-2) = 검증 필요 |
267:| R-5 / L-2 / L-5 (evasion + 외부 library) | 분리 확정 (얕은 검토) | 영구 분리 = 결정 단순 |
271:## §7 실 구현 sub-cycle 입력 (조건부 승인 조건 6 + Rollback Trigger / Evidence)
273:### §7.1 조건부 승인 조건 6 매핑 (55 entry B-4 답습 — 수단 결정 후 실 구현 sub-cycle 의무)
277:| 1 | denyNonFastForwards (c) per-repo + (d) entrypoint/Dockerfile 활성화 | Layer 2a (L 영역) | 실 구현 sub-cycle |
278:| 2 | R-6 actual run PASS | W 보존 (r2-canary.yml) | 실 구현 sub-cycle |
279:| 3 | 4 G4 workflow actual run PASS | W 보존 (L-3) | 실 구현 sub-cycle |
280:| 4 | violation_type 정밀화 | Layer 1 (L-1) | 실 구현 sub-cycle |
281:| 5 | history_rewrite enum fixture 추가 | Layer 2 (L-3) | 실 구현 sub-cycle |
292:| RT-L-1 | Layer 1 violation_type 검출 실패 | L-1 | 4 violation_type 미작동 |
293:| RT-L-2 | canonical JSON 위반 미검출 (fallback 동등성 실패) | L-1 | RFC 8785 reference corpus mismatch |
299:- R 영역: R-3 actual run PASS (secret-hygiene workflow run ID) + R-1/R-2 가용 시 evidence 합산
300:- L 영역: L-1 4 violation_type 검출 actual run + canonical 72 files 동등성 + L-3 4 G4 workflow actual run PASS
301:- W 영역: 기존 workflow 보존 verify + 누락 step 추가 후 actual run PASS
311:- ❌ 외부 library (L-2/L-5) 도입 결정 (별도 cycle)
345:4. **SESSION + INDEX commit + push** (57 entry 등록) → **R-4 / L-4 / W 보존우선 수단 결정 발효**
347:   - **실 구현 sub-cycle** (조건부 승인 조건 6: denyNonFastForwards 활성화 + R-6 actual run + 4 G4 workflow run + violation_type 정밀화 + history_rewrite fixture + Layer subsection 분리)
367:- redaction-pattern-equivalence.md (R-4) + r4-1-trigger-extension-evidence.md (R-4.1) + g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md (Group D PoC)
376:| P-1 | 본 brief 가 R-4/L-4/W 권고를 사용자 결정 영역에 *기정사실화* | "권고 ≠ 결정" — 발효 = 풀 3+1 + 외부 LLM + 사용자 명시 후 (§5.2 + §10) |
379:| P-4 | L-1 stdlib 권고가 RFC 8785 strict 정합 *과소평가* | §3.2 #3 fallback 동등성 + corpus 72 files + RT-L-2 (mismatch trigger) |
388:**다음 단계**: 사용자 승인 → 합의 진입 (풀 3+1 + 외부 LLM 1+, (E-α) 권고) → brief v1.1 흡수 → SESSION + INDEX commit + push (57 entry) → R-4 / L-4 / W 보존우선 수단 결정 발효.

exec
/bin/bash -lc 'rg -n "Layer 4|Layer 5|External anchor|CI 회귀|Signed commit|history-anchor|Layer 1|Layer 2" docs/architecture/provider-agnostic-memory-skill-design.md docs/decisions/ADR-012-evidence-ledger-protection.md' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
docs/decisions/ADR-012-evidence-ledger-protection.md:107:**원칙 12**: 1인 동일 호스트 SPOF 한계 인지 (G3 §5.5 답습) — 동일 호스트 전체 침해는 본 ADR 의 완전 방어 범위 밖. multi-host 전환 시 Layer 3 / Layer 5 의무 발동 트리거.
docs/decisions/ADR-012-evidence-ledger-protection.md:150:| 18 | `secret_scan_layer1_implementation` | Secret scan Layer 1 구현 ledger (MVP-1 Stage 1, GP-3 S-1) | T1 audit |
docs/decisions/ADR-012-evidence-ledger-protection.md:151:| 19 | `docker_secret_isolation_layer1_implementation` | Docker secret 격리 Layer 1 구현 ledger (MVP-1 Stage 2, GP-3 ST-3) | T1 audit |
docs/decisions/ADR-012-evidence-ledger-protection.md:152:| 20 | `provider_adapter_enforcement_layer1_static` | Provider adapter Layer 1 static 검출 ledger (MVP-1 Stage 3, GP-5 T-6) | T1 audit |
docs/decisions/ADR-012-evidence-ledger-protection.md:165:**Layer 1 — Hash Chain (MANDATORY 모든 환경)**:
docs/decisions/ADR-012-evidence-ledger-protection.md:171:**Layer 2 — Git append-only branch (MANDATORY)**:
docs/decisions/ADR-012-evidence-ledger-protection.md:175:- CI 회귀 검증: base branch 대비 JSONL line deletion / rewrite 감지
docs/decisions/ADR-012-evidence-ledger-protection.md:177:**Layer 3 — Signed commit (RECOMMENDED MVP, MANDATORY multi-host)**:
docs/decisions/ADR-012-evidence-ledger-protection.md:182:**Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)**:
docs/decisions/ADR-012-evidence-ledger-protection.md:187:### 2.4 Signed commit OR Git append commit (사용자 명시 답습)
docs/decisions/ADR-012-evidence-ledger-protection.md:191:**5/5 입력 권고**: Layer 1 + Layer 2 동시 의무 (Hash chain + Git append-only) + Layer 3 RECOMMENDED.
docs/decisions/ADR-012-evidence-ledger-protection.md:201:**본 ADR 의 권위 결정**: D-1A / D-1B / D-1C 모두 본 ADR §2.3 Layer 1 + Layer 2 동시 의무 *호환*. 단 사용자 명시 결정 영역 — 본 ADR 갱신은 단축 합의 가능.
docs/decisions/ADR-012-evidence-ledger-protection.md:216:- CI 회귀 검증: 입력 → 자체 canonical → JCS reference output 비교
docs/decisions/ADR-012-evidence-ledger-protection.md:259:- Layer 1: pre-commit hook (입력 entry 의 `prev_hash` 검증)
docs/decisions/ADR-012-evidence-ledger-protection.md:260:- Layer 2: pre-push hook (chain 전체 재검증)
docs/decisions/ADR-012-evidence-ledger-protection.md:262:- Layer 4: import script (`scripts/hermes-migration/import.py` — 향후 Implementation 시점)
docs/decisions/ADR-012-evidence-ledger-protection.md:268:- **Layer 1**: Hash chain (middle entry tampering 차단)
docs/decisions/ADR-012-evidence-ledger-protection.md:269:- **Layer 2**: Git append-only branch + denyNonFastForwards (history 재작성 차단)
docs/decisions/ADR-012-evidence-ledger-protection.md:271:- **Layer 4**: CI 회귀 검증 — base branch 대비 JSONL line deletion / rewrite 감지
docs/decisions/ADR-012-evidence-ledger-protection.md:272:- **Layer 5 (RECOMMENDED MVP, MANDATORY multi-host)**: External anchor — GitHub Actions run ID + signed tag (Agent B C-4) 또는 월 1회 external snapshot (외부 LLM 2 C-4)
docs/decisions/ADR-012-evidence-ledger-protection.md:337:| (a) | 1인 호스트 침해 | **약** — host 전체 침해 시 모든 layer 우회 | Layer 5 external snapshot (월 1회) |
docs/decisions/ADR-012-evidence-ledger-protection.md:339:| (c) | Git history rewrite | **중** — Layer 2~4 차단, 그러나 host 권한 상승 시 force push 가능 | (a) 동일 + Layer 5 |
docs/decisions/ADR-012-evidence-ledger-protection.md:340:| (d) | JSONL middle tampering | **강** — Layer 1 (hash chain) 정확히 이 케이스 차단 | (그대로) |
docs/decisions/ADR-012-evidence-ledger-protection.md:446:| Middle entry tampering 차단 | ✅ Hash chain | ✅ Hash chain (Layer 1) |
docs/decisions/ADR-012-evidence-ledger-protection.md:447:| History 재작성 차단 | ⚠️ git append commit *권고* | ✅ Layer 2 MANDATORY (git append-only + denyNonFastForwards) |
docs/decisions/ADR-012-evidence-ledger-protection.md:448:| Force-push 차단 | ❌ 미명시 | ✅ Layer 2 (denyNonFastForwards) |
docs/decisions/ADR-012-evidence-ledger-protection.md:450:| CI 회귀 검증 | ❌ 미명시 | ✅ Layer 4 (line deletion/rewrite 감지) |
docs/decisions/ADR-012-evidence-ledger-protection.md:451:| External anchor | ❌ 미명시 | ✅ Layer 5 RECOMMENDED |
docs/decisions/ADR-012-evidence-ledger-protection.md:459:**결론**: 본 ADR-012 강화 chain 은 현 G4 §4.4 대비 *동등 이상의 보안 결과* — 12 보안 차원 중 11/12 ↑, 1/12 동등 (Hash chain Layer 1).
docs/decisions/ADR-012-evidence-ledger-protection.md:518:- Layer 5: Evidence 형식 차원 — ledger entry 11 필드 모두 provider-neutral 강제 (원칙 6)
docs/decisions/ADR-012-evidence-ledger-protection.md:565:- Layer 5 (External anchor) MVP RECOMMENDED → multi-host MANDATORY 전환 시점 의무 발동 — 별도 합의
docs/decisions/ADR-012-evidence-ledger-protection.md:659:본 6 즉시 강제는 **Hermes 가 4 게이트 통과 전 ADR-008 합의 자동화 + R-6 CI 회귀 검증 + 본 PR-2 풀 3+1 합의** 책임 한정으로 작동하는 현 상태에 적용.
docs/architecture/provider-agnostic-memory-skill-design.md:9:> **PR-2 보강 흡수 (2026-05-09 풀 3+1 합의 + 외부 LLM 2건)**: **§4.2 schema 11 필드 (10 → 10 + `event` 신규) + §4.4 hash chain 사양 보강 (Layer 1~5 다층 강제 + RFC 8785 JCS Primary + fallback + Genesis Hash + prev_hash 검증 실패 BLOCK + manual + Full Rewrite 5 Layer 방어) + §4.6 round-trip 검증 절차 보강 (Tier-based + 3 ledger entry 형식 + Migration 검증 실패 rollback 조건) — `docs/decisions/ADR-012-evidence-ledger-protection.md` 와 동일 PR commit. 합의 권위: `docs/review/3plus1-consensus-2026-05-09-pr2-evidence-ledger.md` (5/5 입력 APPROVE WITH CONDITIONS). G4 §11.4 P-1 (RFC 8785 JCS) + P-2 (schema 진화 정책) + P-3 (import schema_version) 처리 완료** — P-4 / P-5 는 PR-1 또는 후속 합의 영역 (PR-1 §11.4 답습).
docs/architecture/provider-agnostic-memory-skill-design.md:11:> **ADR-012 (Evidence Ledger Protection) Mandatory Reference (2026-05-09 후속 3 PR-2 신규 발행)**: 본 G4 §4.2 11 필드 schema (`event` 신규) + §4.4 hash chain 사양 (Layer 1~5 + RFC 8785 JCS Primary + Genesis Hash + prev_hash 검증 실패 BLOCK + Full Rewrite 5 Layer) + §4.6 round-trip 검증 절차 (Tier-based + 3 ledger entry 형식 + Migration rollback) 의 *권위 출처*. **G4 §4 = ADR-012 §2.1 ~ §3.5 답습 권위**.
docs/architecture/provider-agnostic-memory-skill-design.md:13:> **Gate Enforcement Layer 보호 cross-reference (2026-05-12)**: 본 G4 §3.7.3 #18 (`GATE_ENFORCEMENT_LAYER_MODIFY` T3) + §3.8.2 #10 (`gate_enforcement_bypass_detected` rollback_trigger) + §6.1 매트릭스 row + 인터페이스 Layer 4 신설 = **G3 §2.6 권위 정의 답습 cross-reference 한정**. *권위 정의 = G3 §2.6* (Gate 자체 5 기준 + Layer 0~6 5 기준 + 위협 모델 TM-1~TM-8 + 10 보호 항목 매트릭스 + Rollback Trigger 발화 매트릭스). 본 G4 = Skill permission schema 차원 연결 한정 — **Skill permission 이 `WRITE_CODE` / `RUN_LOCAL_TOOLS` (T2) 를 갖더라도 Gate definition / Gate verdict / Evidence ledger / CI policy 변경 권한은 자동 포함되지 *않는다*** (§3.7.3 #18 = T3 `forbidden_actions` 자동 포함 강제). 본 cross-reference 흡수 = G4 Design/Governance Gate PASS 권위 변경 0건. 본 §11.6 답습.
docs/architecture/provider-agnostic-memory-skill-design.md:15:> **P2 v3 (`hermes-adoption-design-v3.md`) = Adopted (Design Adoption only, 2026-05-09 후속 6)** 후속 권위. 본 G4 = P2 v3 §6 (G4 정의 + ADR-012 Mandatory Reference cross-reference) + §10.1 #1 (Provider Liquidity 5-way Multi-layer Defense 5 Layer — 본 G4 §3.5 + §4.3 Layer 3/4 + ADR-012 §원칙 6 Layer 5) + §10.2 Archive Migration Note + §11.1 Hermes PMO 격상 전 인간 전문 리뷰 의무화 답습.
docs/architecture/provider-agnostic-memory-skill-design.md:27:**상위 권위**: 헌법 제5조-2 관용 (Provider Liquidity, 비협상), 헌법 제8조 (보안), ADR-008 차단조건 #2 (JSONL export 표준), **ADR-009 C-N §5 (Provider Liquidity 5-way Multi-layer Defense 모법 ADR Layer 1, 2026-05-09 후속 4 갱신)**, **ADR-012 §원칙 5 + §원칙 6 (Provider Liquidity 5-way Layer 5 — Evidence 형식 차원 provider-neutral 강제)**
docs/architecture/provider-agnostic-memory-skill-design.md:537:| 10 | `gate_enforcement_bypass_detected` (**G3 §2.6 cross-reference — 2026-05-12**) | Gate enforcement layer 우회 검출 — Gate 정의 변경 / Gate verdict 변조 / Evidence ledger `event: gate_pass` forge / Gate 순서 skip / Layer 1~4 결과 silent override / Hook 비활성화 / Skill 통한 Gate enforcement 우회 / Memory 통한 Gate verdict 대체 (G3 §2.6 위협 모델 TM-1 ~ TM-8 통합 trigger) | 모든 T1+T2 권한 자동 revoke + Skill 완전 비활성화 | 사용자 명시 review + G3 §2.6.5 답습 (Hermes 컨테이너 정지 + audit log + Gate enforcement 분석) + ADR-008 부록 C §C.2 답습 |
docs/architecture/provider-agnostic-memory-skill-design.md:629:#### 4.4.1 다층 강제 (Layer 1 ~ Layer 5)
docs/architecture/provider-agnostic-memory-skill-design.md:631:**Layer 1 — Hash Chain (MANDATORY 모든 환경)**:
docs/architecture/provider-agnostic-memory-skill-design.md:638:**Layer 2 — Git Append-only Branch (MANDATORY)**:
docs/architecture/provider-agnostic-memory-skill-design.md:642:- CI 회귀 검증: base branch 대비 JSONL line deletion / rewrite 감지
docs/architecture/provider-agnostic-memory-skill-design.md:649:**Layer 4 — CI 회귀 검증 (MANDATORY)**:
docs/architecture/provider-agnostic-memory-skill-design.md:650:- Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증
docs/architecture/provider-agnostic-memory-skill-design.md:655:**Layer 5 — External Anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)**:
docs/architecture/provider-agnostic-memory-skill-design.md:660:**사용자 명시 옵션 답습 (D-1, ADR-012 §2.4)**: "signed commit OR git append commit (둘 중 하나) 의무" — 사용자 결정 영역. 5/5 입력 권고는 *다층 동시 의무* (Layer 1 + 2 MANDATORY, Layer 3 RECOMMENDED). **본 §4.4 = Layer 1 + Layer 2 MANDATORY 답습** (D-1A / D-1B / D-1C 모두 호환).
docs/architecture/provider-agnostic-memory-skill-design.md:675:- CI 회귀 검증: 입력 → 자체 canonical → JCS reference output 비교
docs/architecture/provider-agnostic-memory-skill-design.md:720:- Layer 1: pre-commit hook (입력 entry 의 `prev_hash` 검증)
docs/architecture/provider-agnostic-memory-skill-design.md:721:- Layer 2: pre-push hook (chain 전체 재검증)
docs/architecture/provider-agnostic-memory-skill-design.md:723:- Layer 4: import script (`scripts/hermes-migration/import.py` — 향후 Implementation 시점)
docs/architecture/provider-agnostic-memory-skill-design.md:727:**Layer 1**: Hash chain (middle entry tampering 차단)
docs/architecture/provider-agnostic-memory-skill-design.md:728:**Layer 2**: Git append-only branch + denyNonFastForwards (history 재작성 차단)
docs/architecture/provider-agnostic-memory-skill-design.md:730:**Layer 4**: CI 회귀 검증 — base branch 대비 JSONL line deletion / rewrite 감지
docs/architecture/provider-agnostic-memory-skill-design.md:731:**Layer 5 (RECOMMENDED MVP, MANDATORY multi-host)**: External anchor — GitHub Actions run ID + signed tag 또는 월 1회 external snapshot
docs/architecture/provider-agnostic-memory-skill-design.md:947:- **Layer 1 (schema-level)** — G4 §3.7 13-category enum (12 Permission Granularity + 1 Gate Enforcement #18) + §3.2 #9/#10 schema validation 필드 *정의* + T3 8-category 자동 차단 *형식*
docs/architecture/provider-agnostic-memory-skill-design.md:948:- **Layer 2 (self-escalation)** — G4 §3.8.1 6 차단 메커니즘 *규칙* + §3.8.2 10 rollback_trigger × revoke 매트릭스 *연결* (9 Permission Granularity + 1 Gate Enforcement #10)
docs/architecture/provider-agnostic-memory-skill-design.md:950:- **Layer 4 (Gate Enforcement)** — **G3 §2.6** 권위 정의 (Gate 정의 / verdict / evidence / sequence / failure override + Layer 0~6 enforcement mechanism 보호) — G4 §3.7.3 #18 + §3.8.2 #10 cross-reference
docs/architecture/provider-agnostic-memory-skill-design.md:1250:본 5건 즉시 강제는 **본 G4 가 정식 채택되지 않더라도** 현 시점에서 유효 — *Hermes 가 4 게이트 통과 전 ADR-008 합의 자동화 + R-6 CI 회귀 검증* 책임 한정으로 작동하는 현 상태에 적용.
docs/architecture/provider-agnostic-memory-skill-design.md:1293:- Layer 1: G2 GP-5 (depcruise 룰 + P1 facade 단일 진입점) — *모든 작성 주체* 의 코드 lock-in 차단
docs/architecture/provider-agnostic-memory-skill-design.md:1294:- Layer 2: G3 §6.4 (Hermes-originated lock-in 변경 시도 차단) — *Hermes 작성 주체* 한정
docs/architecture/provider-agnostic-memory-skill-design.md:1296:- Layer 4: G4 §4.3 (JSONL Hermes 의존 0 + 최소 2 provider 재해석 가능) — *export format* 차원
docs/architecture/provider-agnostic-memory-skill-design.md:1302:**[Cross-reference Block — (g1-N-3-pamsd) HIGH carry-over, R-7 (vi-γ) 답습]**: 본 §11.4.2 "Provider Liquidity 4-way Multi-layer Defense" 명명 = 헌법-동급 권위 (R-S4 (g1-N-3) 답습). (g1-N-1) commit `148fbbe` 후 **헌법 제5조-2 (Provider Liquidity, 비협상) line 75~80** 직접 모법 발효 — Layer 1~4 모두 헌법 제5조-2 line 80 "본 원칙은 비협상 — ADR-011 line 6 상위 권위 매핑 답습" 답습 형식 직접 활용 자격. 본문 verbatim 변경 0건 (R-7 (vi-α) 사전 기각 + (vi-β) DEFER 양립, (vi-γ) cross-reference 추가만 채택).
docs/architecture/provider-agnostic-memory-skill-design.md:1393:| 3 | §6.1 매트릭스 row + Layer 4 신설 | §6.1 표 row 추가 + 인터페이스 본문 (3-layer → 4-layer Gate Enforcement Layer 추가) | G3 §2.6 = Layer 4 (Gate Enforcement Layer) 권위 정의 명시 cross-reference | ✅ **RESOLVED** (2026-05-12) |
docs/architecture/provider-agnostic-memory-skill-design.md:1409:- ❌ **hook 구현** — pre-commit / pre-push / Husky / Layer 1~4 자동 차단 hook 본문 (Implementation 영역)

exec
/bin/bash -lc 'python3 tools/secret_scanner.py --list-patterns >/tmp/secret_patterns.out 2>/tmp/secret_patterns.err; rc=$?; cat /tmp/secret_patterns.err; printf '"'rc=%s\\n' \""'$rc"' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
registered_patterns_count=45
  baseline_prefix=5
  tier1_prefix=31
  tier1_regex=7
  tier1_alternation=2
  skip_direct_register=['T1-038', 'T1-040']
  active_patterns=45
  tier1_42_catalog_compliant=True
  BL-1	prefix-baseline	Anthropic	Hermes #1 (sk-ant-)
  BL-2	prefix-baseline	OpenAI/Anthropic/etc	Hermes #1 (sk-)
  BL-3	prefix-baseline	GitHub PAT classic	Hermes #2
  BL-4	prefix-baseline	AWS Access Key ID	Hermes #15
  BL-5	prefix-baseline	Slack tokens	Hermes #8
  T1-001	prefix	GitHub PAT (fine-grained)	Hermes #3
  T1-002	prefix	GitHub OAuth access token	Hermes #4
  T1-003	prefix	GitHub user-to-server	Hermes #5
  T1-004	prefix	GitHub server-to-server	Hermes #6
  T1-005	prefix	GitHub refresh token	Hermes #7
  T1-006	prefix	Google API keys	Hermes #9
  T1-007	prefix	Perplexity	Hermes #10
  T1-008	prefix	Fal.ai	Hermes #11
  T1-009	prefix	Firecrawl	Hermes #12
  T1-010	prefix	BrowserBase	Hermes #13
  T1-011	prefix	Codex encrypted tokens	Hermes #14
  T1-012	prefix	Stripe secret key (live)	Hermes #16
  T1-013	prefix	Stripe secret key (test)	Hermes #17
  T1-014	prefix	Stripe restricted key	Hermes #18
  T1-015	prefix	SendGrid API key	Hermes #19
  T1-016	prefix	HuggingFace token	Hermes #20
  T1-017	prefix	Replicate API token	Hermes #21
  T1-018	prefix	npm access token	Hermes #22
  T1-019	prefix	PyPI API token	Hermes #23
  T1-020	prefix	DigitalOcean PAT	Hermes #24
  T1-021	prefix	DigitalOcean OAuth	Hermes #25
  T1-022	prefix	AgentMail API key	Hermes #26
  T1-023	prefix	ElevenLabs TTS key	Hermes #27
  T1-024	prefix	Tavily search API	Hermes #28
  T1-025	prefix	Exa search API	Hermes #29
  T1-026	prefix	Groq Cloud API key	Hermes #30
  T1-027	prefix	Matrix access token	Hermes #31
  T1-028	prefix	RetainDB API key	Hermes #32
  T1-029	prefix	Hindsight API key	Hermes #33
  T1-030	prefix	Mem0 Platform API key	Hermes #34
  T1-031	prefix	ByteRover API key	Hermes #35
  T1-032	regex	ENV assignment	Hermes H-A
  T1-033	regex	JSON field with secret keys	Hermes H-B
  T1-034	regex	Authorization header (Bearer)	Hermes H-C
  T1-035	regex	Private key block	Hermes H-E
  T1-036	regex	DB connstr password	Hermes H-F
  T1-037	regex	JWT token	Hermes H-G
  T1-039	regex	URL userinfo (non-DB)	Hermes H-K
  T1-041	alternation	URL query sensitive keys (16)	Hermes _SENSITIVE_QUERY_PARAMS
  T1-042	alternation	Body/form sensitive keys (14)	Hermes _SENSITIVE_BODY_KEYS
rc=0

exec
/bin/bash -lc "python3 - <<'PY'
from pathlib import Path
from collections import Counter
files=list(Path('tests/canonical').glob('*/*'))
print('files', len(files))
print('suffixes', Counter(p.name.split('.',1)[1] for p in files))
print('cases', len(list(Path('tests/canonical').glob('*/*.input.json'))))
PY" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
files 72
suffixes Counter({'expected.canonical': 24, 'input.json': 24, 'expected.sha256': 24})
cases 24

codex
verdict: **REVISE**

**BLOCKING findings**

1. **L 권고의 핵심 전제가 실제 repo와 불일치합니다.**  
   brief는 L-4를 “L-1 stdlib + L-3”, “외부 의존성 0”, “L-2/L-5 외부 library 별도 cycle”로 권고합니다: [mvp2-beta-submeans-decision-brief.md](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-beta-submeans-decision-brief.md:159).  
   하지만 실제 repo의 G4 PoC는 이미 `rfc8785==0.1.4`와 `jcs==0.2.1`를 dev dependency로 고정하고, CI도 이를 설치해 Primary 1/2 + cross-check를 수행합니다: [requirements-dev.txt](/home/delangi/문서/project/category/AI_development_tool/requirements-dev.txt:20), [g4-hash-chain.yml](/home/delangi/문서/project/category/AI_development_tool/.github/workflows/g4-hash-chain.yml:64).  
   정정 방향: L-4를 “stdlib 단독”으로 발효시키려면 `canonical_json.py`/G4 workflows/requirements의 기존 Group C JCS Primary 사용과의 관계를 먼저 분리해야 합니다. 보존 우선 원칙을 유지하려면 권고는 “신규 외부 library 도입 0, 기존 rfc8785+jcs PoC 보존”으로 바꾸고, L-2/L-5 “별도” 표현을 “신규 도입/승격 결정은 별도”로 좁혀야 합니다.

2. **“외부 library 도입 결정 0”은 맞지만, “외부 의존성 0 / stdlib 단독 시제 충족” 주장은 과장입니다.**  
   `tools/canonical_json.py`는 조건부 import가 아니라 primary path로 `rfc8785`와 `jcs`를 명시합니다: [canonical_json.py](/home/delangi/문서/project/category/AI_development_tool/tools/canonical_json.py:34). `history-anchor-verifier.yml`와 `rewrite-defense.yml`도 `rfc8785 + jcs` 설치를 직접 수행합니다.  
   정정 방향: “본 cycle에서 새 외부 library를 도입하지 않는다”와 “현 PoC가 외부 library를 사용하지 않는다”를 분리해 쓰십시오. 현재 후자는 false입니다.

3. **L-1/L-3 시제의 evidence 표현을 조정해야 합니다.**  
   `tests/canonical/` 72 files / 8 카테고리, `jsonl_hash_chain.py` genesis + violation_type, G4 workflow 존재는 확인됐습니다. 그러나 현재 `g4-hash-chain.yml`의 FAIL fixture 4 cover는 `prev_hash_mismatch`, `hash_recalculation`, `schema_missing_field`, `genesis_mismatch`이고, `history_rewrite` fixture 추가는 후속 조건으로 남아 있습니다: [g4-hash-chain.yml](/home/delangi/문서/project/category/AI_development_tool/.github/workflows/g4-hash-chain.yml:197).  
   정정 방향: “4 violation_type actual run”을 현 시제 claim으로 쓰지 말고, “history_rewrite enum fixture 추가”가 조건부 승인 조건 6의 미충족 실 구현 입력임을 더 선명히 분리하십시오.

**확인된 사항**

- `tests/canonical/` = 72 files, 8 categories, 24 input cases 확인.
- `agent/redact.py`는 본 repo 내 부재 확인.
- `src/adapters/llm/facade.py`는 placeholder 확인.
- 지정 5 workflow는 존재하고 보존 상태 확인.
- `tools/secret_scanner.py --list-patterns`는 registered 45, tier1_42 compliant 확인.
- `receive.denyNonFastForwards` local/global 미설정 확인.
- R 권고(R-4 + R-3 우선, R-1/R-2 별도 trajectory)는 ADR-011 means-vs-ends와 대체로 정합합니다.
- W 권고(기존 workflow 보존 우선 + W-E 보조)는 51 W-A 단일통합 권고를 repo 현실에 맞춘 정밀화로 볼 수 있어 정합합니다.
- (γ-c) 특화 의무 4와 조건부 승인 조건 6 매핑은 큰 틀에서 맞습니다. 다만 위 L evidence 표현 정정이 필요합니다.

**non-blocking 권고**

- “Tier-1 42 + baseline 5 = 45”는 산술상 혼란이 있으므로 “registered 45, Tier-1 42 catalog compliant, skip-direct 2 포함”처럼 표현을 바꾸는 편이 안전합니다.
- “L-2/L-5 영구 분리”보다 “신규 외부 JCS library 도입/운영 승격은 별도 cycle”이 현재 repo 상태와 더 정확합니다.
tokens used
159,105
verdict: **REVISE**

**BLOCKING findings**

1. **L 권고의 핵심 전제가 실제 repo와 불일치합니다.**  
   brief는 L-4를 “L-1 stdlib + L-3”, “외부 의존성 0”, “L-2/L-5 외부 library 별도 cycle”로 권고합니다: [mvp2-beta-submeans-decision-brief.md](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-beta-submeans-decision-brief.md:159).  
   하지만 실제 repo의 G4 PoC는 이미 `rfc8785==0.1.4`와 `jcs==0.2.1`를 dev dependency로 고정하고, CI도 이를 설치해 Primary 1/2 + cross-check를 수행합니다: [requirements-dev.txt](/home/delangi/문서/project/category/AI_development_tool/requirements-dev.txt:20), [g4-hash-chain.yml](/home/delangi/문서/project/category/AI_development_tool/.github/workflows/g4-hash-chain.yml:64).  
   정정 방향: L-4를 “stdlib 단독”으로 발효시키려면 `canonical_json.py`/G4 workflows/requirements의 기존 Group C JCS Primary 사용과의 관계를 먼저 분리해야 합니다. 보존 우선 원칙을 유지하려면 권고는 “신규 외부 library 도입 0, 기존 rfc8785+jcs PoC 보존”으로 바꾸고, L-2/L-5 “별도” 표현을 “신규 도입/승격 결정은 별도”로 좁혀야 합니다.

2. **“외부 library 도입 결정 0”은 맞지만, “외부 의존성 0 / stdlib 단독 시제 충족” 주장은 과장입니다.**  
   `tools/canonical_json.py`는 조건부 import가 아니라 primary path로 `rfc8785`와 `jcs`를 명시합니다: [canonical_json.py](/home/delangi/문서/project/category/AI_development_tool/tools/canonical_json.py:34). `history-anchor-verifier.yml`와 `rewrite-defense.yml`도 `rfc8785 + jcs` 설치를 직접 수행합니다.  
   정정 방향: “본 cycle에서 새 외부 library를 도입하지 않는다”와 “현 PoC가 외부 library를 사용하지 않는다”를 분리해 쓰십시오. 현재 후자는 false입니다.

3. **L-1/L-3 시제의 evidence 표현을 조정해야 합니다.**  
   `tests/canonical/` 72 files / 8 카테고리, `jsonl_hash_chain.py` genesis + violation_type, G4 workflow 존재는 확인됐습니다. 그러나 현재 `g4-hash-chain.yml`의 FAIL fixture 4 cover는 `prev_hash_mismatch`, `hash_recalculation`, `schema_missing_field`, `genesis_mismatch`이고, `history_rewrite` fixture 추가는 후속 조건으로 남아 있습니다: [g4-hash-chain.yml](/home/delangi/문서/project/category/AI_development_tool/.github/workflows/g4-hash-chain.yml:197).  
   정정 방향: “4 violation_type actual run”을 현 시제 claim으로 쓰지 말고, “history_rewrite enum fixture 추가”가 조건부 승인 조건 6의 미충족 실 구현 입력임을 더 선명히 분리하십시오.

**확인된 사항**

- `tests/canonical/` = 72 files, 8 categories, 24 input cases 확인.
- `agent/redact.py`는 본 repo 내 부재 확인.
- `src/adapters/llm/facade.py`는 placeholder 확인.
- 지정 5 workflow는 존재하고 보존 상태 확인.
- `tools/secret_scanner.py --list-patterns`는 registered 45, tier1_42 compliant 확인.
- `receive.denyNonFastForwards` local/global 미설정 확인.
- R 권고(R-4 + R-3 우선, R-1/R-2 별도 trajectory)는 ADR-011 means-vs-ends와 대체로 정합합니다.
- W 권고(기존 workflow 보존 우선 + W-E 보조)는 51 W-A 단일통합 권고를 repo 현실에 맞춘 정밀화로 볼 수 있어 정합합니다.
- (γ-c) 특화 의무 4와 조건부 승인 조건 6 매핑은 큰 틀에서 맞습니다. 다만 위 L evidence 표현 정정이 필요합니다.

**non-blocking 권고**

- “Tier-1 42 + baseline 5 = 45”는 산술상 혼란이 있으므로 “registered 45, Tier-1 42 catalog compliant, skip-direct 2 포함”처럼 표현을 바꾸는 편이 안전합니다.
- “L-2/L-5 영구 분리”보다 “신규 외부 JCS library 도입/운영 승격은 별도 cycle”이 현재 repo 상태와 더 정확합니다.
