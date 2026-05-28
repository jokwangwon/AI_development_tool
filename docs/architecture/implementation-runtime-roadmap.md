# Implementation / Runtime PASS Roadmap

> **본 문서는 Implementation/Runtime PASS 작업 *구현 코드가 아니라 우선순위 + PASS 기준 정리* 문서이다.** 사용자 명시 답습 — "이번 단계는 *구현* 이 아니라 *구현 순서와 PASS 기준 정리*".

**작성일**: 2026-05-09 (후속 15)
**상태**: DRAFT — Reviewer-only 단축 검토 진행 중 (`docs/review/3plus1-consensus-2026-05-09-implementation-runtime-roadmap.md`)
**상위 권위**: ADR-011 §2.1 (a)~(d) + (e) 5조건 패턴, ADR-008 부록 C §C.5 분리 매트릭스, P2 v3 §3.1.4 Implementation Pending 표
**근거 합의**:
- `docs/review/3plus1-consensus-2026-05-09-adr-013-014-candidate-decision.md` (ADR-013/014 후보 결정 — 분기 A 답습)
- `docs/review/3plus1-consensus-2026-05-09-adr-008-update-pmo-activation-cross-ref.md` (ADR-008 부록 C 신설)
- `docs/review/3plus1-consensus-2026-05-09-adr-010-011-followup-scope.md` (ADR-010/011 후속 보강 검토 — 분기 A 채택, 보강 불필요)
- `docs/review/3plus1-consensus-2026-05-09-implementation-runtime-roadmap.md` (본 roadmap 단축 합의)

---

## ⭐ Implementation Evidence PASS 발효 milestone 이력

| 단계 | 발효 | 범위 / 자격 | 근거 합의 |
|------|------|-----------|---------|
| **MVP-1** (G2 GP-3 + GP-5) | ✅ 2026-05-27 (32번째 entry) | MVP-1 Implementation Evidence PASS **완전 발효 (α)** — GP-3 5/5 + GP-5 5/5 | `docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md` (풀 3+1 + 외부 LLM 1+ APPROVE WITH CONDITIONS) + roadmap-mvp1.md §9 |
| **MVP-2** (G2 GP-2 + G4 §4.4 Layer 1+2+4) | ✅ 2026-05-28 (62번째 entry, commit `82e1ee6`) | MVP-2 Implementation Evidence PASS — **G4 ledger 무결성 *완전* (Layer 1+2+4) + GP-2 송신 redaction *detection-tier*, prevention(R-1/R-2)/Layer 3·5/2a denyNonFastForwards *deferred*** (⚠️ full GP-2 PASS 아님) | `docs/review/3plus1-consensus-2026-05-28-mvp2-final-pass.md` (풀 3+1 + 외부 LLM 1+ APPROVE WITH CONDITIONS, 4 source) — 의존: 59 Layer 통합 PASS (`0f49eb9`) + 60 GP-2 detection-layer PASS (`92e9078`) + 61 R-S1 정정 (`bb59342`) |

> **MVP-2 PASS 후속 trajectory (deferred, 자동 진입 0)**: full GP-2 PASS (R-1 Hermes runtime redaction import / R-2 facade real TR-1 prevention) + Layer 3 (Signed commit) + Layer 5 (External anchor) + Layer 2a denyNonFastForwards (실 bare/server 배포 시점) — 별도 cycle 사용자 명시.

---

## 0. 본 문서 범위

### 0.1 본 문서가 *하는* 것

1. G2 GP-2 ~ GP-6 / G3 5 영역 / G4 7 영역 = **합산 17 항목** Implementation/Runtime PASS 작업 분해
2. 각 항목 별 PASS 기준 + Evidence Required + Dependency + Risk + Suggested Order 명시
3. 5 우선순위 판단 기준 답습 + Claude 재평가
4. R-2 / R-4.1 PoC 패턴 답습 의무 명시 (ADR-011 §2.1 (b) 5조건 답습)

### 0.2 본 문서가 *하지 않는* 것 (사용자 명시 답습)

- ❌ Hermes PMO 격상 선언
- ❌ Implementation/Runtime PASS 자동 선언 (각 항목 PASS = 별도 합의 + PoC evidence 후 발생)
- ❌ G2 / G3 / G4 Implementation PASS 일괄 선언
- ❌ 실 runtime code / migration script / hook 구현
- ❌ ADR 본문 자동 갱신
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ 본 roadmap 의 우선순위 자동 *고정* (사용자 명시 결정 + Claude 재평가 영역, 본 문서 = 권고 한정)

### 0.3 본 문서의 권위 한계

본 문서는 **DRAFT** — Reviewer-only 단축 검토 후 사용자 명시 결정으로 *권고 권위* 발행. 각 항목 PASS = *별도 합의* (단축 또는 풀 3+1, ADR-011 §2.1 (a)~(e) 5조건 답습) + PoC evidence + 사용자 명시 결정.

---

## 1. 5 우선순위 판단 기준 (사용자 명시 답습)

| # | 기준 | 가중치 (본 문서 권고) |
|---|------|----|
| 1 | **보안 위험이 큰 것** | HIGH (3 가중치) — 5 영구 핵심 제약 직접 영향 |
| 2 | **기존 PoC 패턴 재사용 가능** | MEDIUM (2) — R-2 / R-4.1 / R-6 / R-7 답습 가능 시 운영 부담 ↓ |
| 3 | **다른 작업의 선행 조건** | MEDIUM (2) — 의존성 사슬 단축 |
| 4 | **CI 자동화 쉬움** | LOW (1) — 계산적 검증 우선 |
| 5 | **Hermes PMO 격상 조건 직접 연결** | HIGH (3) — P2 v3 §2.6.1 12 조건 답습 |

각 항목의 점수 합산 = 우선순위 (총 11 점 만점). 각 항목 평가는 §2 + §3 + §4 답습.

---

## 2. G2 Implementation/Runtime PASS 작업 분해 (5 항목)

### 2.1 GP-2 ~ GP-6 매트릭스

| Area | Item | Type | Dependency | Evidence Required | PASS Criteria | Risk | Suggested Order |
|---|---|---|---|---|---|---|---|
| **G2** | **GP-2 Egress Redaction** (로그 / LLM 송신 차단) | PoC + CI | ADR-011 §2.3 운영 함의 #2, ADR-008 부록 B + §A.2, P1 v2 §8.2 RedactionFilter, R-4 patterns | (a) 동등 이상 보안 결과 (Hermes native + P1 facade redaction 비교) / (b) 격리 PoC (Docker isolation) / (c) ADR 권위 (ADR-011 §2.3 #2) / (d) 자동 회귀 (R-2 답습 nightly) / (e) 합의 APPROVE | log/송신 redaction 6 patterns BLOCK 100% + base64 evasion BLOCK + R-2 답습 PoC PASS | **HIGH** (P2 헌법 8조 위반 경로) | **5 (10/11)** |
| **G2** | **GP-3 Credential / Secret Hygiene** (저장 + 코드) | PoC + CI | ADR-008 §A.2 (`~/.hermes/auth.json`), ADR-010 (Vault HSM), R-4 catalog | (a) gitleaks / detect-secrets pre-commit + chmod 600 entrypoint stat + inotify (저장) / (b) 격리 PoC (Docker isolation) / (c) ADR-008 §A.2 + ADR-010 / (d) CI step (gitleaks GitHub Actions) / (e) 합의 APPROVE | gitleaks / detect-secrets 100% scan + chmod 600 검증 + Docker stop on inotify violation | **HIGH** (P3 + P4 헌법 8조 위반 경로) | **4 (10/11)** |
| **G2** | **GP-4 External Input Validation** (Hermes / Worker 출력 포함) | PoC + CI + recommended Reviewer agent | ADR-011 §2.3 운영 함의 #1 (Tools verify Hermes 출력), GP-4 §6.3, G3 §1.3 | (a) 입력 schema validation + regex sanitizer + 명시 escape (sql/shell) / (b) Reviewer Agent prompt injection 감지 PoC / (c) ADR-011 §2.3 #1 + GP-4 / (d) CI (pydantic test + escape unit test) / (e) 합의 APPROVE | input schema validation 100% + sql injection BLOCK + command injection BLOCK + path traversal BLOCK | **MEDIUM-HIGH** (P5 헌법 8조 #3) | **6 (8/11)** |
| **G2** | **GP-5 Provider Adapter Enforcement** (코드 lock-in 차단) | PoC + CI | ADR-009 C-N §5 (Layer 1 모법 ADR), `llm-providers-design.md` §9 depcruise + AST scanner, P1 facade 단일 진입점 | (a) depcruise rule + AST scanner + pre-commit hook + CI step / (b) PR auto-reject 격리 시뮬레이션 / (c) ADR-009 C-N + ADR-008 차단조건 #4 / (d) CI step (depcruise GitHub Actions) / (e) 합의 APPROVE | depcruise rule 100% lock-in 차단 + provider SDK 직접 import / 모델명 분기 PR auto-reject 100% | **HIGH** (헌법 5조-2 Provider Liquidity 5-way Layer 1 모법) | **1 (11/11)** |
| **G2** | **GP-6 Memory / Skill Migration Feasibility** (학습 자산 lock-in 차단) | PoC | ADR-008 차단조건 #2 (JSONL export), G4 §4.2 + §4.4 + §4.6, ADR-012 §2.10 | (a) JSONL append-only + hash chain + 변환 스크립트 (hermes_to_claude / hermes_to_openai 1+) / (b) 라운드트립 PoC (R2-5 답습) / (c) ADR-008 차단조건 #2 + G4 + ADR-012 / (d) CI step (round-trip nightly) / (e) 합의 APPROVE | round-trip hash 일치 STRICT (T2) + 의미 보존 (T3, lossy entry 명시) + 외부 오케스트레이터 import 검증 (claude / openai / gemini / local 최소 2+) | **MEDIUM** (P8 + 헌법 5조-2 Provider Liquidity Layer 4 — Provider 교체 자유) | **7 (8/11)** |

### 2.2 G2 우선순위 합산

```
G2 GP-5 Provider Adapter Enforcement   = 11/11 (HIGH 보안 + 기존 PoC + 선행 조건 + CI 자동화 쉬움 + PMO 직접 연결)
G2 GP-3 Credential / Secret Hygiene    = 10/11 (HIGH 보안 + 기존 PoC + CI 자동화 쉬움 + PMO 연결)
G2 GP-2 Egress Redaction               = 10/11 (HIGH 보안 + R-2 답습 + CI 자동화 쉬움 + PMO 연결)
G2 GP-4 External Input Validation      =  8/11 (MEDIUM-HIGH + Reviewer Agent 추론 보조 + 부분 자동화)
G2 GP-6 Memory/Skill Migration         =  8/11 (MEDIUM + R2-5 답습 + 다른 작업과 병행 가능)
```

---

## 3. G3 Implementation/Runtime PASS 작업 분해 (5 영역)

### 3.1 G3 영역 매트릭스

| Area | Item | Type | Dependency | Evidence Required | PASS Criteria | Risk | Suggested Order |
|---|---|---|---|---|---|---|---|
| **G3** | **Hermes 권한 22 항목 runtime enforcement** (T1 8 / T2 2 / T3 12) | hook + wrapper + sidecar + CI | ADR-011 §2.4 T1/T2/T3, G3 §2 22 권한, ADR-009 C-N §2.3 (PMO ↔ provider) | (a) 22 권한 별 enforcement matrix / (b) 격리 PoC (Docker — Hermes container 권한 검증) / (c) ADR-011 §2.4 + G3 §2 / (d) CI nightly + GitHub Actions / (e) 합의 APPROVE | T3 12 권한 100% BLOCK (CI 회귀 검증) + T2 2 권한 사용자 명시 강제 + T1 8 권한 자동 OK | **HIGH** (Hermes ≠ root of trust 핵심 운영) | 11 (분리 권고 — 22 권한 각자 PoC 부담 ↑) |
| **G3** | **Hermes-originated commit auto-reject** (Hermes 변조 차단 매트릭스 4항목 #3) | git pre-commit hook + GitHub Actions branch protection | ADR-012 §2.12 #3, G3 §2.2 #20, P2 v3 §10.2 | (a) commit author = Hermes 검출 시 reject (git pre-commit hook 또는 server-side hook) / (b) 격리 PoC (test commit author 시뮬레이션) / (c) ADR-012 §2.12 + G3 §2.2 #20 / (d) GitHub Actions branch protection rule (CODEOWNERS or commit signing) / (e) 합의 APPROVE | Hermes-originated commit 100% reject + audit log + 사용자 alert | **HIGH** (Evidence Forgery P10 + 합의 권위 침해) | **2 (10/11)** |
| **G3** | **Evidence 없는 PASS 차단** (PASS 성립 4 요건 강제) | hook + CI | G3 §1.3 + §5, ADR-012 §2.1 원칙 1~12 | (a) PASS 선언 시 (i) Tools 검증 + (ii) Evidence Ledger entry + (iii) 사용자 명시 승인 + (iv) 합의 보고서 commit 모두 검증 / (b) 격리 PoC (PASS without evidence 시뮬레이션 → BLOCK) / (c) G3 §1.3 + ADR-012 §1.4 / (d) CI step (PASS 선언 PR 검증 hook) / (e) 합의 APPROVE | Evidence 없는 PASS 100% BLOCK + Ledger entry 강제 + 사용자 alert | **HIGH** (Evidence Integrity 핵심) | **2 (10/11)** — Hermes-originated commit auto-reject 와 동일 우선순위 |
| **G3** | **Skill escalation 차단 / runtime wrapper** | hook + wrapper + sandbox | G4 §3.1 (Skill schema 17 필드, allowed_actions / forbidden_actions), G3 §3.3 (Skill escalation 차단) | (a) Skill wrapper 권한 검증 + Docker cap_drop / read_only / tmpfs noexec / (b) 격리 PoC (Skill `forbidden_actions` 위반 시도 → BLOCK) / (c) G4 §3.1 + G3 §3.3 / (d) CI step + runtime audit / (e) 합의 APPROVE | Skill `allowed_actions` 강제 100% + escalation 시도 100% BLOCK + 자동 비활성화 + 사용자 alert | **MEDIUM-HIGH** (Skill 권한 escalation 위험) | **8 (7/11)** — 사용자 명시 후순위 답습 (구현 난이도 ↑) |
| **G3** | **합의 자기참조 차단** (Hermes 가 합의 인프라 자기 격상 차단) | governance hook | G3 §4 합의 인프라 순환 권위 + ADR-011 §2.3 + ADR-009 C-N §2.3 | (a) Hermes 단독 합의 차단 (Reviewer-only 또는 외부 LLM 의견 의무) / (b) 격리 PoC (Hermes 단독 합의 시도 → BLOCK) / (c) G3 §4 / (d) CI step (commit author + Reviewer 체크) / (e) 합의 APPROVE | Hermes 단독 합의 100% BLOCK + Reviewer-only 또는 외부 LLM 의견 강제 검증 | **HIGH** (메타-순환 권위 침해) | **9 (7/11)** — 합의 보고서 검증 영역, 부분 수동 |

### 3.2 G3 우선순위 합산

```
G3 Hermes-originated commit auto-reject = 10/11 (HIGH 보안 + git hook 답습 + Hermes ≠ root 핵심)
G3 Evidence 없는 PASS 차단                = 10/11 (HIGH Evidence Integrity + ADR-012 답습)
G3 Skill escalation 차단                  =  7/11 (MEDIUM-HIGH + 구현 난이도 ↑ — 후순위 권고)
G3 합의 자기참조 차단                     =  7/11 (HIGH + 부분 수동 + 합의 보고서 검증 영역)
G3 Hermes 권한 22 항목 runtime            = 11/11 합산이지만 22 권한 분산 시 분리 PoC 부담 — 본 roadmap 에서 별도 *분해 작업* 필요 (G3 분리 후속 합의)
```

---

## 4. G4 Implementation/Runtime PASS 작업 분해 (7 영역)

### 4.1 G4 영역 매트릭스

| Area | Item | Type | Dependency | Evidence Required | PASS Criteria | Risk | Suggested Order |
|---|---|---|---|---|---|---|---|
| **G4** | **JSONL hash chain verification PoC** (Layer 1 — sha256 + canonical JSON) | PoC + CI | ADR-012 §2.3 (Layer 1) + §2.5 (Canonical JSON), G4 §4.4 | (a) sha256 + canonical JSON 일관성 100% / (b) Docker 격리 PoC (R2-5 답습) / (c) ADR-012 §2.3 / (d) CI step (chain integrity nightly) / (e) 합의 APPROVE | hash chain 검증 100% PASS + middle entry tampering 100% 차단 | **HIGH** (Evidence Integrity 핵심) | **3 (10/11)** |
| **G4** | **RFC 8785 JCS canonicalization 구현** (Primary + jq fallback) | PoC + library + test corpus | ADR-012 §2.5, G4 §4.4 | (a) RFC 8785 JCS Python `pyjcs` / `rfc8785` 또는 stdlib `json.dumps(sort_keys=True, separators=(",",":"))` 동등 보장 / (b) test corpus ≥ 20 reference outputs (Docker 격리 PoC) / (c) ADR-012 §2.5 / (d) CI step (canonical 위반 BLOCK) / (e) 합의 APPROVE | canonical JSON 출력 RFC 8785 reference 100% 일치 (test corpus 20+) + fallback 동등성 검증 | **HIGH** (Provider-agnostic 형식 표준) | **3 (10/11)** — JSONL hash chain verification 과 동시 진행 가능 |
| **G4** | **Round-trip validation PoC** (R2-5 답습, hermes_to_claude / hermes_to_openai 1+) | PoC + migration script + CI | G4 §4.6 (Tier-based) + ADR-012 §2.9 (3 ledger entry 형식) | (a) export → 변환 → import → re-export → hash 일치 100% (T2) 또는 의미 보존 + lossy entry (T3) / (b) Docker 격리 PoC (R2-5 답습) / (c) G4 §4.6 + ADR-012 §2.9 / (d) CI step (nightly round-trip) / (e) 합의 APPROVE | round-trip hash 일치 100% (T2 strict) + lossy 영역 명시 + `event: roundtrip_lossy` ledger entry 자동 생성 | **HIGH** (Provider Liquidity Layer 4 — JSONL Hermes 의존 0) | **3 (10/11)** — JSONL hash chain + JCS canonical 과 동시 진행 가능 |
| **G4** | **Migration script implementation** (`scripts/hermes-migration/*.py`) | code + CI | G4 §4.5 + ADR-012 §2.10, ADR-014 발행 가능 영역 | (a) Hermes 의존 0 (depcruise 검증) + provider SDK 직접 import 0 / (b) 라운드트립 PoC + checksum 검증 / (c) G4 §4.5 + ADR-014 발행 후 cross-reference / (d) CI step (`--dry-run` 모드) / (e) 합의 APPROVE + ADR-014 신규 발행 합의 (별도 풀 3+1) | hermes_to_claude.py + hermes_to_openai.py + import.py 실 구현 + 라운드트립 PoC PASS | **HIGH** (ADR-014 발행 trigger) | **10 (8/11)** — ADR-014 발행 시점 (Implementation/Runtime PASS PoC 완료 후) |
| **G4** | **provider_bindings lint rule enforcement** (G2 GP-5 답습) | depcruise + CI | G4 §3.5 (Layer 3), G2 GP-5 (Layer 1 모법) | G2 GP-5 답습 — 본 항목은 GP-5 의 G4 차원 답습 (별도 작업 아님) | GP-5 와 동일 | **HIGH** | (G2 GP-5 와 통합 — Order 1) |
| **G4** | **Memory/Skill schema validation** (17 필드 + 11 필드 + provider-neutral 강제) | pydantic + CI | G4 §3.1 (17 Skill 필드) + §4.2 (11 JSONL 필드), ADR-012 §2.2 | (a) pydantic schema validation 100% + provider-neutral identifier 검증 / (b) Docker 격리 PoC (Skill 정의 + JSONL entry 생성 → 검증) / (c) G4 §3 + §4.2 + ADR-012 §2.2 / (d) CI step (schema validation) / (e) 합의 APPROVE | 17 필드 / 11 필드 schema 100% validation + provider-neutral 강제 100% | **MEDIUM** (Provider Liquidity Layer 3) | **6 (8/11)** — GP-4 와 동일 우선순위 |
| **G4** | **Memory boundary hook** (4 금지 사항 강제) | hook + sandbox | G4 §5 (Memory/Skill Boundary 4 금지) + G3 §2.5 #11 + ADR-009 C-N §2.3 | (a) 4 금지 사항 (Memory→policy / Skill→ADR / Session→Global / Hermes→skill 자기 승인) 100% BLOCK / (b) 격리 PoC / (c) G4 §5 + G3 + ADR-009 / (d) CI step / (e) 합의 APPROVE | Memory poisoning 100% 차단 + Skill auto-approval 100% 차단 + Session→Global 자동 promotion 100% 차단 | **HIGH** (Memory Poisoning Side-channel — P12 deferred) | **9 (7/11)** — 합의 자기참조 차단 과 동일 우선순위 |

### 4.2 G4 우선순위 합산

```
G4 JSONL hash chain verification PoC      = 10/11
G4 RFC 8785 JCS canonicalization 구현      = 10/11   ← 동시 진행 가능
G4 Round-trip validation PoC               = 10/11   ← 동시 진행 가능
G4 Memory/Skill schema validation          =  8/11
G4 Memory boundary hook                    =  7/11
G4 Migration script implementation         =  8/11   ← Implementation PoC 완료 후 (ADR-014 발행 trigger)
G4 provider_bindings lint                  = (G2 GP-5 와 통합)
```

---

## 5. 종합 우선순위 매트릭스 (Suggested Order)

### 5.1 본 roadmap 권고 우선순위 (사용자 명시 답습 + Claude 재평가)

| Order | Item | Area | Score (11점) | Rationale (보안 / PoC / 선행 / CI / PMO) |
|----|----|----|----|----|
| **1** | **G2 GP-5 Provider Adapter Enforcement** | G2 | 11/11 | HIGH 보안 (Provider Liquidity 5-way Layer 1 모법) + R-4 답습 + 다른 작업 선행 (P1 facade 단일 진입점) + CI 자동화 (depcruise) + PMO 직접 연결 |
| **2 (tie)** | **G3 Hermes-originated commit auto-reject** | G3 | 10/11 | HIGH 보안 (Evidence Forgery P10) + git pre-commit hook 답습 + 다른 G3 작업 선행 + GitHub Actions branch protection + PMO 직접 연결 |
| **2 (tie)** | **G3 Evidence 없는 PASS 차단** | G3 | 10/11 | HIGH 보안 (PASS 성립 4 요건) + ADR-012 답습 + 다른 작업 선행 + CI step + PMO 직접 연결 |
| **3 (tie)** | **G4 JSONL hash chain verification PoC** | G4 | 10/11 | HIGH 보안 (Evidence Integrity Layer 1) + R-2 답습 + 다른 G4 작업 선행 + CI nightly + PMO 직접 연결 |
| **3 (tie)** | **G4 RFC 8785 JCS canonicalization** | G4 | 10/11 | HIGH (Provider-agnostic 형식 표준) + test corpus 답습 + JSONL hash chain 동시 + CI 위반 BLOCK + PMO 연결 |
| **3 (tie)** | **G4 Round-trip validation PoC** | G4 | 10/11 | HIGH (Provider Liquidity Layer 4) + R2-5 답습 + JSONL + JCS 동시 + CI nightly + PMO 직접 연결 |
| **4** | **G2 GP-3 Credential / Secret Hygiene** | G2 | 10/11 | HIGH 보안 (P3 + P4) + gitleaks 답습 + CI 자동화 쉬움 + PMO 연결 |
| **5** | **G2 GP-2 Egress Redaction** | G2 | 10/11 | HIGH 보안 (P2) + R-2 답습 + CI 자동화 쉬움 (R-6 nightly) + PMO 연결 |
| **6 (tie)** | **G2 GP-4 External Input Validation** | G2 | 8/11 | MEDIUM-HIGH (P5) + 부분 자동화 (Reviewer Agent 추론 보조) + Schema validation CI |
| **6 (tie)** | **G4 Memory/Skill schema validation** | G4 | 8/11 | MEDIUM (Provider Liquidity Layer 3) + pydantic 답습 + CI 자동화 쉬움 |
| **7** | **G2 GP-6 Memory/Skill Migration Feasibility** | G2 | 8/11 | MEDIUM (Provider Liquidity Layer 4) + R2-5 답습 (G4 round-trip 와 통합 가능) |
| **8** | **G3 Skill escalation 차단 / runtime wrapper** | G3 | 7/11 | MEDIUM-HIGH + 구현 난이도 ↑ + Skill wrapper + Docker cap_drop + sandbox |
| **9 (tie)** | **G3 합의 자기참조 차단** | G3 | 7/11 | HIGH 메타-순환 권위 + 부분 수동 + 합의 보고서 검증 영역 |
| **9 (tie)** | **G4 Memory boundary hook** | G4 | 7/11 | HIGH (P12 Memory Poisoning Side-channel) + 4 금지 강제 + 격리 PoC |
| **10** | **G4 Migration script implementation** | G4 | 8/11 | HIGH (ADR-014 발행 trigger) — Implementation/Runtime PASS PoC 완료 후 발행 검토 |
| **11** | **G3 Hermes 권한 22 항목 runtime enforcement** | G3 | 11/11 합산 | 22 권한 분산 PoC 부담 ↑ — **별도 분해 후속 합의 의무** (본 roadmap 에서 우선순위 결정 보류, G3 분리 작업) |

### 5.2 Claude 재평가 (사용자 예상 우선순위 vs 본 roadmap)

| 사용자 예상 | 본 roadmap | 평가 |
|----|----|----|
| 1. G2 GP-5 Provider Adapter Enforcement | 1. (동일) | ✅ 일치 (11/11 최고 점수) |
| 2. G3 Evidence 없는 PASS 차단 / Hermes-originated commit auto-reject | 2. (동일, tie 처리) | ✅ 일치 (10/11) |
| 3. G4 JSONL hash chain / round-trip PoC | 3. (동일, tie + JCS canonical 추가 동시) | ✅ 일치 + 보강 (JCS canonical 동시 진행 권고) |
| 4. G2 GP-3 Credential / Secret Hygiene | 4. (동일) | ✅ 일치 |
| 5. G2 GP-2 Egress Redaction | 5. (동일) | ✅ 일치 |
| 6. G2 GP-4 External Input Validation | 6. (동일, tie + G4 Memory/Skill schema validation 추가 동시) | ✅ 일치 + 보강 |
| 7. G2 GP-6 Memory/Skill Migration Feasibility | 7. (동일) | ✅ 일치 |
| 8. G3 Skill escalation 차단 / runtime wrapper | 8. (동일) | ✅ 일치 |
| (사용자 미명시) | **9 G3 합의 자기참조 차단 + G4 Memory boundary hook** | 본 roadmap 추가 (8 항목 외) |
| (사용자 미명시) | **10 G4 Migration script implementation** | ADR-014 발행 trigger — 본 roadmap 추가 |
| (사용자 미명시) | **11 G3 Hermes 권한 22 항목 — 별도 분해 후속 합의** | 본 roadmap 추가 |

**Claude 재평가 결론**: 사용자 예상 8 우선순위 = **유지** (모두 본 roadmap 권고와 일치). 추가 3 항목 (Order 9 ~ 11) = 본 roadmap 신규 추가 영역 (사용자 명시 8 항목 외).

### 5.3 PoC 동시 진행 가능 영역 (병렬 작업 효율 ↑)

본 roadmap 권고 — 다음 그룹 동시 진행 가능 (의존성 0건 + R-2 / R-4.1 / R-2-5 격리 PoC 패턴 답습):

| 그룹 | 동시 진행 항목 | 의존성 |
|----|----|----|
| **그룹 A** (Order 1) | G2 GP-5 Provider Adapter Enforcement | (선행 없음 — 모든 작업의 root 의존성) |
| **그룹 B** (Order 2 tie) | G3 Hermes-originated commit auto-reject + G3 Evidence 없는 PASS 차단 | 그룹 A 완료 후 |
| **그룹 C** (Order 3 tie) | G4 JSONL hash chain + RFC 8785 JCS + Round-trip PoC | 그룹 A 완료 후 (G2 GP-5 의 P1 facade 단일 진입점 답습) |
| **그룹 D** (Order 4 + 5) | G2 GP-3 + G2 GP-2 | 그룹 A 완료 후 (R-4 catalog 답습) |
| **그룹 E** (Order 6 tie) | G2 GP-4 + G4 Memory/Skill schema validation | 그룹 B + 그룹 C 완료 후 |
| **그룹 F** (Order 7) | G2 GP-6 | 그룹 C (G4 round-trip) 완료 후 |
| **그룹 G** (Order 8 + 9 tie) | G3 Skill escalation + G3 합의 자기참조 차단 + G4 Memory boundary hook | 그룹 B + 그룹 E 완료 후 |
| **그룹 H** (Order 10) | G4 Migration script implementation | **그룹 C 완료 + ADR-014 발행 합의 (풀 3+1) 후** |
| **그룹 I** (Order 11) | G3 Hermes 권한 22 항목 runtime enforcement | **별도 분해 후속 합의 의무** (G3 분리 작업) |

### 5.4 합의 형태 권고 (각 그룹 별)

| 그룹 | 합의 형태 권고 | 사유 |
|----|----|----|
| **그룹 A** | 단축 합의 (Reviewer-only) + PoC evidence | G2 GP-5 = ADR-009 C-N §5 모법 ADR 답습, 새 권위 결정 0건 |
| **그룹 B** | 단축 합의 + PoC evidence | G3 답습 한정 |
| **그룹 C** | 단축 합의 + PoC evidence | G4 §4 + ADR-012 답습 한정 |
| **그룹 D** | 단축 합의 + PoC evidence | R-4 catalog 답습 |
| **그룹 E** | 단축 합의 + PoC evidence | GP-4 + G4 schema 답습 |
| **그룹 F** | 단축 합의 + PoC evidence (R2-5 답습) | G4 round-trip 답습 |
| **그룹 G** | 단축 합의 + PoC evidence | G3/G4 답습 |
| **그룹 H** | **풀 3+1 + 외부 LLM 1+** (ADR-014 신규 발행) | T3 변경 + 영구 권위 발행 |
| **그룹 I** | **풀 3+1 + 외부 LLM 1+** (G3 22 권한 분해) | T3 변경 영역, 분해 결정 자체가 새 권위 |

각 그룹 PASS 시 **ADR-011 §2.1 (a)~(e) 5조건 답습 의무** + Evidence Ledger entry (`event: gate_pass` 또는 `event: skill_promoted` 등) + Adoption decision commit.

---

## 6. PASS 기준 통합 매트릭스 (각 항목 공통)

### 6.1 ADR-011 §2.1 (a)~(e) 5조건 답습 (모든 항목 의무)

| # | 조건 | 검증 방식 |
|---|----|----|
| (a) | 동등 이상의 보안 결과 | 명시 비교표 (수단 A 보장 ↔ 수단 B 보장) |
| (b) | 격리 환경 PoC 실증 | Docker isolation + 자동 검증 항목 (R-2 / R-4.1 답습 — `network_mode: none` + `read_only` + `cap_drop ALL`) |
| (c) | ADR / SDD 권위 명시 | 본 roadmap 각 항목 Dependency 답습 |
| (d) | 자동 회귀 검증 경로 확보 | CI step + nightly cron (R-6 답습) |
| (e) | 합의 APPROVE | 단축 합의 또는 풀 3+1 (그룹 별 권고) |

### 6.2 Rollback Trigger (각 항목 공통)

본 roadmap 답습 — 각 항목 PASS 후 *rollback trigger* 명시 의무:

| Trigger | 발화 시 |
|----|----|
| R-1 | secret pattern catalog 변경 (Tier-1 42 catalog 답습) — Tier-2/Tier-3 확장 trigger |
| R-2 | Hermes upstream version 변경 (R-6 GitHub Actions actual run 답습) |
| R-3 | hash chain 검증 실패 (`event: chain_violation_detected`) — ADR-012 §2.7 답습 |
| R-4 | round-trip 검증 실패 (`event: roundtrip_fail`) — G4 §4.6.6 답습 |
| R-5 | provider_bindings 위반 PR 검출 — G2 GP-5 답습 |
| R-6 | Hermes-originated commit 검출 — G3 §2.2 #20 답습 |
| R-7 | Skill `forbidden_actions` 위반 — G4 §3.1 + G3 §3.3 답습 |
| R-8 | Memory boundary 4 금지 위반 — G4 §5 답습 |
| R-9 | 합의 자기참조 시도 (Hermes 단독 합의) — G3 §4 답습 |

### 6.3 Evidence Required (각 항목 공통)

본 roadmap 답습 — 각 항목 PoC + PASS 합의 시 다음 evidence 의무:

| Evidence | 형식 |
|----|----|
| Markdown report | `docs/phase0/<task-id>-evidence.md` 또는 `docs/evidence/<task-id>.md` |
| JSONL ledger entry | `docs/evidence/ledger.jsonl` (`event` enum: `memory_write` / `skill_promoted` / `gate_pass` / 등) |
| Docker isolation log | PoC 실행 결과 + canary catalog 검증 |
| GitHub Actions run | R-6 답습 (`actions/runs/<run_id>` cross-reference) |
| 합의 보고서 | `docs/review/<consensus-name>.md` |

---

## 7. 본 roadmap 의 *발생* / *미발생* 사항

### 7.1 본 roadmap 이 *발생시키는* 것

- ✅ Implementation/Runtime PASS 작업 17 항목 분해 + 우선순위 매트릭스
- ✅ 5 우선순위 판단 기준 답습 + Claude 재평가
- ✅ PoC 동시 진행 가능 그룹 (A ~ I) 분류
- ✅ 합의 형태 권고 (단축 vs 풀 3+1)
- ✅ ADR-011 §2.1 (a)~(e) 5조건 답습 매트릭스
- ✅ Rollback Trigger 9 항목 매트릭스
- ✅ Evidence Required 5 형식 명시

### 7.2 본 roadmap 이 *발생시키지 않는* 것 (사용자 명시 답습)

- ❌ Hermes PMO 격상 자동 선언
- ❌ Implementation/Runtime PASS 자동 선언 (각 항목 PASS = 별도 합의 + PoC evidence)
- ❌ G2 / G3 / G4 Implementation PASS 일괄 선언
- ❌ 실 runtime code / migration script / hook 구현
- ❌ ADR 본문 자동 갱신 (cross-reference 답습 한정)
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ 본 roadmap 의 우선순위 자동 *고정* (사용자 명시 결정 + 각 그룹 별 합의 영역)
- ❌ ADR-014 신규 발행 자동 (그룹 H = 풀 3+1 + 외부 LLM 1+ 별도 합의 + Implementation/Runtime PASS PoC 완료 후)

---

## 8. 다음 진입점 (사용자 결정 영역)

본 roadmap 단축 검토 APPROVE 후 다음 작업 (사용자 결정 영역):

1. **그룹 A (Order 1) — G2 GP-5 Provider Adapter Enforcement 첫 PoC 착수** (다음 진입점) — 단축 합의 + PoC evidence (R-4 답습 + depcruise rule + AST scanner + pre-commit hook + CI step)
2. **그룹 B / C / D 동시 진행** (그룹 A 완료 후) — 의존성 0건 영역 병렬 작업
3. **그룹 H (ADR-014 신규 발행)** = 그룹 C (G4 JSONL hash chain + JCS + round-trip PoC) 완료 후 별도 풀 3+1 합의
4. **그룹 I (G3 22 권한 분해)** = 별도 분해 후속 합의 (G3 분리 작업)
5. **Hermes PMO 격상 적격성 검토** = 4 게이트 모두 Implementation/Runtime PASS (그룹 A ~ G + ADR-014 발행) 후 별도 합의 (사용자 명시 답습)

**권고 시작 명령**: "G2 GP-5 Provider Adapter Enforcement 첫 PoC 착수해주세요 (depcruise rule + AST scanner + pre-commit hook + CI step + Docker 격리 PoC)" — 그룹 A 진입.

---

**작성일**: 2026-05-09 후속 15 (DRAFT)
**상태**: DRAFT — Reviewer-only 단축 검토 진행 중
**다음 단계**: 본 roadmap 단축 합의 APPROVE 후 그룹 A (G2 GP-5) 첫 PoC 착수 또는 사용자 명시 결정으로 그룹 우선순위 조정
**금지 (사용자 명시 답습, 변동 없음)**:
- ❌ Hermes PMO 격상 선언
- ❌ Implementation/Runtime PASS 자동 선언
- ❌ G2 / G3 / G4 Implementation PASS 일괄 선언
- ❌ 실 runtime code / migration script / hook 구현
- ❌ ADR 본문 자동 갱신
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ 본 roadmap 의 우선순위 자동 *고정*
