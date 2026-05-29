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
