# (β) sub-수단 결정 entry brief (v1.1)

> **작성**: 2026-05-28 (57번째 entry 진입 cycle — 신규 세션)
>
> **v1 → v1.1 갱신**: 풀 3+1 + 외부 LLM 1+ (codex gpt-5.5 cross-vendor) 통합 합의 (`docs/review/3plus1-consensus-2026-05-28-mvp2-beta.md`) **REVISE → BLOCKING 6 + 권고 7 1pass 흡수** (별도 v2 cycle 0, ceremony-inflation 차단). 핵심 정정: **B-1 L-1 stdlib 시제 충족 주장 = 거짓** (실 시제 rfc8785/jcs Primary, Q1 합의 2026-05-10 이미 채택) → L 결정 "기존 rfc8785/jcs PoC 보존, 신규 도입 0" / B-3 R-1 권위 전도 / B-5 W-F 라벨. §13 v1.1 흡수 매트릭스 추가.
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
| 8 | **신규 외부 library 도입 결정** (B-4 정정: rfc8785/jcs = Q1 합의 2026-05-10 *이미 채택*, 신규 도입 아님) | 0건 (신규 외부 JCS library 도입/운영 승격 = 별도 cycle. 의존성 변경 trigger 권위 = **ADR-011 §2.3 운영 함의 #4** "Hermes 의존성 업그레이드 → R-2/R-6 자동 재실행" — *ADR-012 §2.1 아님*, B-4 흡수) |
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
| **GP-2 CI 회귀 검증** | ✅ `secret-hygiene-egress-redaction.yml` (51791B, D-2 scan-log redaction_pass/fail + base64 known limitation) + `tools/secret_scanner.py` (16802B, `--mode scan-log` redaction 잔존 검출, **registered 45 (Tier-1 42 catalog compliant + baseline 포함)**, N-1 정정) | **R-3 (log canary CI) 시제 충족** |
| GP-2 Hermes native | ❌ `agent/redact.py` 본 repo 부재 (Hermes upstream HEAD v0.12.0, 52 R-A-1 답습) | R-1 = upstream 영역 |
| GP-2 facade redaction | ⚠️ `src/adapters/llm/facade.py` = placeholder (TR-1 발화 시 real, (d) carry-over) | R-2 = 별도 trajectory |
| Layer 1 hash chain | ✅ `tools/jsonl_hash_chain.py` (14038B, genesis + **3 violation_type actual emission** PREV_HASH_MISMATCH + HASH_RECALCULATION + GENESIS_MISMATCH + **HISTORY_REWRITE = enum 정의만, emission 0**, B-2 정정) + `g4-hash-chain.yml` (10652B) | **rfc8785/jcs Primary 시제 충족** (B-1 정정 — stdlib 아님) |
| canonical JSON | ✅ `tools/canonical_json.py` (10055B, **rfc8785 + jcs = Primary, jq -S -c = corpus cross-check fallback**, runtime `jsonl_hash_chain.py:99` = `PRIMARY_1_ONLY` rfc8785 단독) + `requirements-dev.txt:20-21` rfc8785==0.1.4 + jcs==0.2.1 고정 + `tests/canonical/` 72 files / 8 카테고리 (24 input) | **외부 library Primary 시제 충족 (Q1 합의 2026-05-10 채택)** — B-1 정정 |
| Layer 2 history | ✅ `history-anchor-verifier.yml` (19094B) + `rewrite-defense.yml` (16454B) + tools | L-3 영역 시제 충족 |
| Layer 4 CI step | ✅ 4 G4 workflow 분리 운영 (g4-hash-chain + history-anchor-verifier + rewrite-defense + r2-canary), 실 repo 총 12 workflow | **L-3 (R-6 step) 시제 충족** |
| Layer 2a denyNonFastForwards | ⚠️ **미설정** (local + global 0건, 55 §1.3 답습) | 실 구현 sub-cycle 활성화 |

→ ⭐ **핵심 함의 (B-1 정정)**: R-3 (log canary CI) + Layer 1/4 (rfc8785/jcs Primary hash chain + R-6 step) = **모두 PoC 시제 *이미 충족***. 본 (β) cycle 의 수단 결정 = "신규 구현 수단 선택" 보다 **"기존 PoC 시제 → MANDATORY 채택 + PASS 격상 경로 확정"** 성격. ⚠️ **실 시제 = stdlib 단독 아님** — runtime 은 rfc8785 (`PRIMARY_1_ONLY`), 외부 library 는 Q1 합의 2026-05-10 (`3plus1-consensus-2026-05-10-g4-jcs-library-selection.md`) 로 *이미 채택*. 본 cycle = **신규 외부 library 도입 0 (기존 보존)**. R-1 (Hermes upstream) + R-2 (facade real) = 별도 trajectory 의존 (본 cycle = 결정 영역 명시, 구현 경로 결정 0).

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
| **R-1** | Hermes native redaction (`agent/redact.py`) | 송신 직전 redaction | ❌ 본 repo 부재 (Hermes upstream v0.12.0) | Hermes import 결정 (별도 cycle) | GP-2 송신/로그 방어 **신뢰 수단** (ADR-011 §2.3 운영 함의 #2 — "로그/LLM 송신 방어로만 신뢰, 저장 경로 책임 0", B-3 정정 — "MANDATORY" 아님) — *결과* 보조 means, 구현 경로 = upstream |
| **R-2** | P1 facade RedactionFilter | LLM API 진입점 redaction | ⚠️ facade placeholder | facade real (TR-1, (d) carry-over) | facade single entry point redaction means — 구현 경로 = TR-1 trajectory |
| **R-3** | log canary inject + grep CI step | CI 회귀 검증 | ✅ **시제 충족** (`secret-hygiene-egress-redaction.yml` + `secret_scanner.py --mode scan-log`) | 없음 (즉시 PASS 격상 가능) | MANDATORY ((d) 자동 회귀 경로) |
| **R-4** | R-1 + R-2 + R-3 병행 (defense-in-depth) | 다층 redaction | 부분 (R-3 충족, R-1/R-2 trajectory) | R-1 + R-2 의존 | **51 audit 권고** |
| **R-5** | base64 / URL-encoded / 압축 evasion | Hermes upstream R2-6 또는 facade 확장 | ❌ known limitation | MVP-2/3 분리 (G3-4) | **본 cycle 범위 외 (영구 분리)** |

### §2.2 R 결정 권고

⭐ **권고 R 결정 = R-4 (defense-in-depth 목적) 채택 + 구현 경로 차등 명시**:

1. **R-3 = MVP-2 PASS gating 수단** (CI 회귀 검증, 시제 충족 — 즉시 PASS 격상 경로). ⚠️ **R-3 = GP-2 (d) *detection* (자동 회귀 검증) 충족** (N-5 정정). *prevention* (능동 송신 redaction) = R-1/R-2 의존 — facade placeholder 현 시점 능동 redaction 0.
2. **R-1 (Hermes upstream) + R-2 (facade real) = ends (prevention) 보조 means, 구현 경로 = 별도 trajectory**. 본 cycle = R-1/R-2 를 R-4 defense-in-depth 구성요소로 채택하되, **구현 경로 결정 (Hermes import / facade real) = 별도 cycle** 명시 (§0.2 #9 #10).
3. **R-5 = 영구 분리** (base64 evasion = MVP-2/3, G3-4 답습).

→ ⭐ **R-4 ≡ "R-3 (즉시 발효) + R-1/R-2 (deferred trajectory)" framing 선택지** (N-4): "R-4 채택" 과 "R-3 단독 채택 + R-1/R-2 deferred 명시" = 실질 동형 (현 시점 능동 means = R-3 한정). 본 brief = R-4 라벨 채택 (defense-in-depth ends 지향) + R-3 우선 발효 명시.

→ **means-vs-ends 정합 (ADR-011)**: GP-2 의 *ends* (secret 송신/로그 leak 0) = R-4 다층 지향. 본 repo 內 *즉시 발효 가능 means* = R-3 (CI detection). R-1/R-2 = prevention 보조 means, 구현 = cross-trajectory 의존. **MVP-2 PASS 시점 GP-2 (a)~(e) 충족 = R-3 actual run PASS (detection) + R-1/R-2 evidence 가용 시점 (prevention) 합산** (실 구현 sub-cycle 영역).

### §2.3 R 결정 시 trade-off

| 결정 | 장점 | 단점 / risk |
|------|----|----------|
| R-4 (권고) | defense-in-depth ends 충족 / R-3 즉시 발효 / 기존 시제 답습 | R-1/R-2 cross-trajectory 의존 → MVP-2 PASS 시점 GP-2 완전 충족이 Hermes import + facade real 에 부분 종속 (단, R-3 단독으로 (d) 자동 회귀 충족) |
| R-3 단독 | 즉시 발효 / 의존 0 | prevention 부재 (detection-only) — R-1/R-2 deferred 시 능동 송신 redaction 0 (단, R-4 와 실질 동형 — R-1/R-2 deferred 명시 시) |
| R-1 우선 | Hermes native 정공 | Hermes import 결정 선행 의무 (본 cycle 범위 외) → MVP-2 진입 지연 |

→ **R-4 채택 + R-3 우선 발효 + R-1/R-2 cross-trajectory 의존 명시** 가 ceremony-inflation 차단 + 즉시 진전 + ends 충족 정합.

---

## §3 L sub-수단 결정 (G4 §4.4 Layer 4 CI 회귀 검증)

### §3.1 후보 비교 (51 audit §3.4 답습 + 본 cycle audit 갱신)

⚠️ **B-1 핵심 정정**: v1 은 L-4 (L-1 stdlib) 를 시제 충족으로 권고했으나, 실 시제는 **rfc8785/jcs Primary** (runtime `PRIMARY_1_ONLY`). stdlib 단독 경로는 runtime 미사용 (auto-degrade 0). rfc8785/jcs = **Q1 합의 2026-05-10 이미 채택**. 후보 분류 재정렬:

| # | 수단 | 영역 | Library | 본 repo 구현 상태 | 등급 |
|---|------|----|---------|----------------|----|
| **L-1** | Layer 1 hash chain Python stdlib 단독 (`hashlib.sha256` + `json.dumps`) | hash chain 검증 | stdlib | ❌ **시제 미충족** (runtime = PRIMARY_1_ONLY rfc8785, stdlib 경로 미사용) | 가설적 (auto-degrade 부재) |
| **L-1.5** ⭐ (N-2 신규) | Layer 1 + stdlib auto-degrade fallback (rfc8785 부재 시 json.dumps degrade) | hash chain | stdlib fallback | ❌ 미구현 (현 PRIMARY_1_ONLY = degrade 없음) | 별도 실 구현 sub-cycle 선택 (Provider Liquidity 강화 옵션) |
| **L-2** | Layer 1 + RFC 8785 JCS Primary (`rfc8785` / `jcs`) | hash chain + canonical | 외부 library | ✅ **시제 충족** (`requirements-dev.txt:20-21` 고정 + `canonical_json.py` Primary + Q1 합의 채택) | 기존 PoC 운영 중 |
| **L-3** | Layer 4 R-6 workflow step (canonical 위반 + prev_hash mismatch + timestamp monotonicity) | CI 회귀 | shell + Python | ✅ **시제 충족** (4 G4 workflow 분리 운영) | R-6 답습 확장 |
| **L-4** | L-1 + L-3 병행 (stdlib MVP) | Layer 1+4 | stdlib | ❌ 시제 미충족 (L-1 미충족) | ~~51 audit 권고~~ → 재분류 |
| **L-5** | L-2 + L-3 병행 (외부 JCS Primary) | Layer 1+4 + JCS | 외부 library | ✅ **양쪽 시제 충족 (기존 PoC = 실질 L-5)** | **본 cycle 실 상태 = L-5** |

### §3.2 L 결정 권고 (B-1 정정)

⭐ **권고 L 결정 = "기존 rfc8785/jcs Primary PoC 보존 (Q1 합의 2026-05-10 답습) + L-3 CI step" — 실질 L-5, 본 cycle 신규 외부 library 도입 0**:

1. **기존 rfc8785/jcs Primary 보존** — Q1 합의 (`3plus1-consensus-2026-05-10-g4-jcs-library-selection.md`, 17 조건) 로 *이미 채택*. `requirements-dev.txt:20-21` 고정 + `canonical_json.py` Primary + `jsonl_hash_chain.py:99` runtime PRIMARY_1_ONLY + `g4-hash-chain.yml:64` CI 설치. 본 cycle = **보존, 신규 도입 0**.
2. **L-3 (R-6 step) = CI 회귀 검증** — 4 G4 workflow 분리 운영 시제 충족.
3. **신규 외부 JCS library 도입/운영 승격 = 별도 cycle** (N-7 정정 — "L-2/L-5 영구 분리" 아님). 의존성 *변경* trigger = ADR-011 §2.3 #4 (Hermes 의존성 → R-2/R-6 재실행). rfc8785/jcs 는 Q1 합의 채택이므로 본 cycle trigger 발화 0.
4. **L-1.5 (stdlib auto-degrade) = 별도 실 구현 sub-cycle 선택** (N-2) — Provider Liquidity 강화 옵션 (rfc8785 부재 시 degrade), 현 시제 미구현. 본 cycle 결정 0.

→ ⭐ **"본 cycle 신규 외부 library 도입 0" (true) ≠ "현 PoC 외부 library 미사용" (false)** 분리 (B-1/codex BL-2). 현 PoC = rfc8785/jcs Primary 사용 중.

→ **means-vs-ends 정합 (N-3)**: Layer 4 의 *ends* = ledger 무결성 (middle tampering / canonical 위반 / timestamp 위반 차단). **RFC 8785 JCS = canonical *interop* 수단 (means), 무결성 ends 자체 아님**. 기존 rfc8785/jcs Primary + cross-check corpus (72 files) = ends 충족 입증. L-1.5 (stdlib degrade) = 동일 ends 의 Provider-liquidity 강화 *대안 means* (별도 선택).

### §3.3 L 결정 시 trade-off

| 결정 | 장점 | 단점 / risk |
|------|----|----------|
| 기존 rfc8785/jcs 보존 (권고, 실질 L-5) | 시제 충족 (Q1 합의 채택) / 즉시 PASS 격상 / 신규 도입 0 (trigger 발화 0) | 외부 library 의존 (단 Q1 합의 발효 답습, 신규 결정 아님) / rfc8785 부재 시 degrade 0 (L-1.5 별도 보강 영역) |
| L-1.5 stdlib auto-degrade 추가 | Provider Liquidity 강화 (외부 library 부재 내성) | 실 구현 부담 (별도 sub-cycle) + degrade 경로 canonical 동등성 재검증 의무 |
| L-1 stdlib 단독 전환 | 외부 의존 0 | 기존 PoC + Q1 합의 파괴 + runtime canonical 재작성 (과잉, 비권고) |

---

## §4 W 통합 방식 결정 (workflow 통합) — 실 repo 현 상태 핵심

### §4.1 후보 비교 (52 entry §2.3.2 답습 + 본 cycle audit 현 상태)

⭐ **본 cycle 핵심 tension (52 entry B-5 답습)**: 51 audit §4.2 = "W-A 단일 R-6 통합" 권고. 그러나 **실 repo 는 이미 workflow 분리 운영** (g4-hash-chain.yml + history-anchor-verifier.yml + rewrite-defense.yml + r2-canary.yml + secret-hygiene-egress-redaction.yml). W-A "일괄 통합" = **기존 5+ workflow 병합 = 대규모 파괴적 변경**.

⚠️ **B-5 정정**: v1 은 권고를 "보존 우선 = W-A(ii) 변형" 으로 명명했으나, W-A 본질 = *단일 통합* 이고 권고 실질 = *분산 보존 (신규 0)* = 정반대. 명칭 혼선 차단 위해 **2축 분류 (통합/분리)×(신설/보존)** + **W-F (분산 보존, 신규 통합/신설 0) 신규 라벨** 도입:

| # | 수단 | 축 (통합·분리 / 신설·보존) | 실 repo 현 상태 정합 | 비고 |
|---|------|------------------|------------------|----|
| **W-A** | 단일 R-6 확장 (GP-2 + G4 통합) | 통합 / 신설·병합 | ⚠️ (i) 일괄 통합 = 파괴적 / (ii) 보존 + 중복 step | 비권고 (기존 분리 운영 파괴) |
| **W-B** | 별도 workflow 2개 신설 | 분리 / 신설 | ⚠️ 기존 workflow 와 중복 신설 (ceremony-inflation) | 비권고 (기존 secret-hygiene + g4-hash-chain 중복) |
| **W-C** | 단계 분리 (GP-2 우선 + G4 후속) | 시간 분리 | 합의 cycle 2회 부담 | (γ-c) 통합 동시 의무와 trade-off |
| **W-D** | roadmap.md §5.3 별도 progression | progression | roadmap 답습 / 통합 효율 손실 | 검토 |
| **W-E** | pre-commit hook (CI 외 보조) | 보조 layer | CI 회귀 검증 ≠ pre-commit | **보조 동시 가능** (CI 와 병행) |
| **W-F** ⭐ (B-5 신규) | **기존 분산 workflow 보존 (신규 통합/신설 0), 누락 step 만 기존 workflow 內 보강** | 분리 / 보존 | ✅ **실 repo 12 workflow 분산 운영 정합** | **본 brief 권고** |

### §4.2 W 결정 권고

⭐ **권고 W 결정 = W-F (기존 분산 workflow 보존, 신규 통합/신설 0) + W-E 보조 병행** (B-5 정정 — "W-A(ii) 변형" 명칭 폐기):

1. **기존 5+ workflow 보존** (g4-hash-chain.yml + history-anchor-verifier.yml + rewrite-defense.yml + r2-canary.yml + secret-hygiene-egress-redaction.yml) — 신규 통합 workflow 생성 0, 기존 파괴 0. 이는 W-A(ii) "보존 + 중복 step 추가" 의 *최소 변형* = "보존 + (필요 시) 누락 step 추가".
2. **Layer 4 CI 회귀 검증 (L-3) = 기존 G4 workflow 답습 확장** — g4-hash-chain.yml (Layer 1) + history-anchor-verifier.yml + rewrite-defense.yml (Layer 2) 이 이미 Layer 4 회귀 검증 역할 수행. 누락 영역 (예: timestamp monotonicity step / HISTORY_REWRITE enum fixture) = 기존 workflow 內 step 추가 (실 구현 sub-cycle).
3. **GP-2 (R-3) = 기존 secret-hygiene-egress-redaction.yml 답습** — D-2 scan-log redaction 검증 이미 운영. 신규 step 불필요 (또는 canary inject 보강 = 실 구현 sub-cycle).
4. **W-E (pre-commit) = 보조 병행** — dev 환경 즉시 검증 (CI 회귀와 병행, 대체 아님).
5. **W-A(i) 일괄 통합 + W-B 신설 = 비권고** (파괴적 / ceremony-inflation). **W-C 단계 분리 = 비권고** ((γ-c) 통합 동시 의무 3 와 trade-off — Layer 1+2+4 통합 동시 발효 의무가 GP-2 와 G4 의 *동시* 진행을 요구하지는 않으나, 55 entry 진입 권한이 통합 영역으로 발효되어 분리 cycle 2회 부담은 ceremony-inflation).

→ ⭐ **W 결정 핵심 = W-F "기존 분산 구조 보존, 신규 통합/신설 0, 누락 step 만 기존 workflow 內 보강"**. 이는 51 audit W-A 권고의 *정신* (ceremony-inflation 차단)을 *실 repo 현 상태* (이미 12 workflow 분산 운영)에 맞춰 정밀화한 신규 라벨. codex = "W-A 권고를 repo 현실에 맞춘 정밀화로 정합" 판정 + Agent C = "명칭 W-A(ii) 부정확" 지적 → **실질 권고 정합 + 라벨 W-F 정정** 동시 충족 (B-5).

### §4.3 W 결정 시 (γ-c) 특화 의무 정합 확인

- 의무 2 ("부분 답습" framing): W 결정이 Layer 3 (Signed commit) + Layer 5 (External anchor) 진입 유발 0. (단, history-anchor-verifier.yml = Layer 5 External anchor PoC 시제 *이미 운영* — 55 B-2 답습. "보존" = PoC 시제 보존이지 Layer 5 *결정 영역 진입* 0).
- 의무 3 (통합 동시 발효): W "보존 우선" 이 Layer 1+2+4 통합 PASS evidence 동시 발효 저해 0 (기존 workflow 가 Layer 1+2 분담, Layer 4 = 회귀 검증 통합).

---

## §5 통합 수단 결정 매트릭스 + 의존 관계

### §5.1 R ↔ L ↔ W cross-dependency

| 수단 | 결정 권고 | 즉시 발효 가능 | cross-trajectory 의존 |
|------|--------|------------|-------------------|
| **R** | R-4 (R-3 detection 우선 + R-1/R-2 prevention deferred) | R-3 ✅ (시제 충족) | R-1 = Hermes import / R-2 = facade real (TR-1) |
| **L** | 기존 rfc8785/jcs Primary PoC 보존 (실질 L-5, Q1 합의 답습) + L-3, 신규 도입 0 | ✅ (시제 충족) | 없음 (신규 외부 JCS 도입/L-1.5 degrade = 별도) |
| **W** | W-F (분산 보존, 신규 0) + W-E 보조 | ✅ (기존 12 workflow 보존) | 없음 |

### §5.2 통합 결정 발효 시 채택 영역 (본 cycle 합의 APPROVE 시점)

✅ **R-4 / L 보존(실질 L-5) / W-F sub-수단 *결정 발효*** (51 후보 → 결정)
✅ **후속 실 구현 sub-cycle 진입 자격 발효** (조건부 승인 조건 6 입력, §7)
✅ **R-3 + L (rfc8785/jcs Primary) + L-3 = MVP-2 PASS gating 즉시 발효 가능 means 확정** (시제 충족)
✅ **R-1 / R-2 = prevention 보조 means + cross-trajectory 구현 경로 명시** (별도 cycle)
✅ **신규 외부 JCS library 도입/L-1.5 degrade + R-5 (evasion) = deferred 확정** (별도 cycle)

### §5.3 미발효 영역 (deferred)

❌ 실 구현 자체 (denyNonFastForwards 활성화 / R-6 actual run / step 추가 / evidence 수집) = 실 구현 sub-cycle
❌ Hermes import (R-1) / facade real (R-2, TR-1) 구현 경로 결정 = 별도 cycle
❌ 신규 외부 JCS library 도입/운영 승격 결정 + L-1.5 stdlib auto-degrade 구현 = 별도 cycle (기존 rfc8785/jcs = Q1 합의 답습 보존)
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
| 2 | R-6 actual run PASS | W-F 보존 (r2-canary.yml) — R-2 canary 영역 (GP-2 R-3 와 별개) | 실 구현 sub-cycle |
| 3 | 4 G4 workflow actual run PASS | W-F 보존 (L-3, g4-hash-chain + history-anchor-verifier + rewrite-defense + r2-canary) | 실 구현 sub-cycle |
| **3b** ⭐ (B-6 신규) | **R-3 secret-hygiene-egress-redaction.yml actual run PASS** (GP-2 (d) detection 핵심 gating) | **R-3 (GP-2)** | 실 구현 sub-cycle |
| 4 | violation_type 정밀화 (HISTORY_REWRITE emission 구현) | Layer 1 (rfc8785/jcs Primary) | 실 구현 sub-cycle |
| 5 | history_rewrite enum fixture 추가 (B-2 — 현 emission 0) | Layer 2 (L-3) | 실 구현 sub-cycle |
| 6 | Layer subsection 분리 (PASS evidence template) | 통합 ((γ-c) 의무 1) | Layer 통합 PASS 발효 cycle |

→ **본 (β) cycle = 위 6+1 조건의 *수단 기반* 확정** (어느 수단으로 충족할지). *실행* = 실 구현 sub-cycle. (B-6 정정 — R-3 secret-hygiene actual run = GP-2 (d) 핵심 gating, 조건 2 r2-canary 와 별개 명시).

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
- ❌ 신규 외부 JCS library 도입/승격 + L-1.5 stdlib degrade 구현 결정 (별도 cycle, 기존 rfc8785/jcs = Q1 합의 보존)
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
4. **SESSION + INDEX commit + push** (57 entry 등록) → **R-4 / L 보존(실질 L-5, rfc8785/jcs) / W-F 수단 결정 발효**
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
| P-4 | ⚠️ **v1 의 L-1 stdlib 시제 충족 주장 = 실측 거짓** (B-1) — brief 작성자 filesystem audit 부정확 (runtime PRIMARY_1_ONLY 미확인) | **풀 3+1 + cross-vendor codex 4 source 가 포착** (process 가치 입증) → v1.1 "기존 rfc8785/jcs PoC 보존" 정정. 향후 시제 주장 = runtime mode 직접 verify 의무 |
| P-5 | 본 brief 작성자 = 51/52/55 brief 작성자 (Claude Opus 4.7) → cascade risk | §1.1 선행 권위 답습 + cross-vendor (E-α) codex 호출로 독립 검증 (55 동형) |
| P-6 | "수단 결정 cycle" 이 실 구현 자동 진입 유발 | §0.2 #23 + §10 "자동 진입 0건, 사용자 명시 의무" |
| P-7 | (γ-c) 특화 의무 4 (Layer subsection / 부분 답습 framing) 위반 risk | §1.3 + §4.3 정합 확인 (Layer 3+5 진입 0, 통합 동시 발효 저해 0) |

---

---

## §13 v1.1 흡수 매트릭스 (BLOCKING 6 + 권고 7 1pass)

본 v1.1 = `docs/review/3plus1-consensus-2026-05-28-mvp2-beta.md` 답습 1pass 흡수 (별도 v2 cycle 0, ceremony-inflation 차단, 52/55 entry 동형).

### §13.1 BLOCKING 6 흡수

| # | 흡수 영역 | 답습 |
|---|---------|-----|
| B-1 ⭐⭐⭐ (4-way) | §1.2 + §3.1 + §3.2 + §3.3 + §5.1/5.2 | L-1 stdlib 시제 충족 거짓 → "기존 rfc8785/jcs Primary PoC 보존 (Q1 합의 2026-05-10 답습), 신규 도입 0" 전면 정정. 실 시제 = PRIMARY_1_ONLY (R-A-2+R-B-3+R-C-1+codex BL-1/2) |
| B-2 ⭐⭐ (2-way) | §1.2 + §7.1 | HISTORY_REWRITE dead enum (emission 0) → "3 violation_type actual emission + HISTORY_REWRITE fixture = 조건 6 #5 실 구현 입력" 분리 (R-A-1+codex BL-3) |
| B-3 ⭐⭐ | §2.1 + §2.2 + §2.3 | R-1 "MANDATORY (§2.3 #2)" 권위 전도 → "GP-2 송신/로그 방어 신뢰 수단 (저장 경로 책임 0)" (Agent B R-B-1, Reviewer raw verify) |
| B-4 | §0.2 #8 + §3.2 + §8 | "ADR-012 §2.1 trigger" misattribution → "ADR-011 §2.3 #4 (의존성 → R-2/R-6 재실행)" (Agent B R-B-2) |
| B-5 | §4.1 + §4.2 + §5.1 | "W-A(ii) 변형" 명칭 부정확 → W-F (분산 보존, 신규 0) 신규 라벨 + 2축 분류 (Agent C R-C-2) |
| B-6 | §7.1 | 조건 6 표 R-3 (secret-hygiene) actual run 누락 → 조건 3b 추가 + 조건 2 r2-canary 매핑 정정 (Agent A R-A-3) |

### §13.2 권고 7 흡수

N-1 (45 산술 → registered 45) §1.2 / N-2 (L-1.5 stdlib degrade) §3.1/3.2 / N-3 (RFC 8785 = interop means ≠ ends) §3.2 / N-4 (R-4 ≡ R-3+deferred framing) §2.2 / N-5 (R-3 detection vs prevention) §2.2 / N-6 (library drift + 성능 NOTE) §7 / N-7 ("영구 분리" → "신규 도입/승격 별도") §3.2.

### §13.3 4 source 정합 확인 (BLOCKING 아님)

tests/canonical 72/8/24 + agent/redact.py 부재 + facade placeholder + 5 workflow 보존 (총 12) + secret_scanner 45 patterns + denyNonFastForwards 미설정 + (γ-c) 특화 의무 4 정합 + scope 침입 0 + R-5 evasion 영구 분리 정당 + history-anchor-verifier Layer 5 PoC 시제 ≠ Layer 5 진입 = 4 source 일치 확인.

---

**본 brief v1.1 끝.**

**다음 단계**: SESSION + INDEX commit + push (57 entry) → 본 cycle 합의 발효 (REVISE → v1.1 흡수) → **R-4 / L 보존(실질 L-5, rfc8785/jcs Q1 합의 답습) / W-F + W-E 보조 수단 결정 발효** → 실 구현 sub-cycle (조건부 승인 조건 6+1: denyNonFastForwards 활성화 + R-6 actual run + 4 G4 workflow run + **R-3 secret-hygiene actual run** + violation_type(HISTORY_REWRITE emission) 정밀화 + history_rewrite fixture + Layer subsection) = 사용자 명시 별도 cycle.
