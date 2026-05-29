OpenAI Codex v0.128.0 (research preview)
--------
workdir: /home/delangi/문서/project/category/AI_development_tool
model: gpt-5.5
provider: openai
approval: never
sandbox: danger-full-access
reasoning effort: none
reasoning summaries: none
session id: 019e6d35-0ed9-76b1-b109-151c12043c12
--------
user
당신은 외부 LLM 검토자 (cross-vendor blind review)입니다. 응답 vendor = OpenAI (codex CLI), 본 cycle 풀 3+1 Agent vendor = Anthropic Claude. cross-vendor 충족 (헌법 5조-2).

## 본 cycle 개요

AI_development_tool 프로젝트. 본 cycle = **G4 §4.4 Layer 1+2+4 통합 Implementation Evidence PASS 발효 (e2)** (59 entry). 55 entry = PASS 격상 *진입 권한* (e1) → 본 cycle = 실제 PASS *발효* (e2). 32 entry MVP-1 PASS 발효 답습 동형 큰 milestone.

선행 chain (모두 발효): 55 (통합 PASS 격상 진입 권한, APPROVE WITH CONDITIONS) → 57 ((β) 수단 결정: R-4 / L 보존(rfc8785/jcs) / W-F) → 58 (실 구현: violation_type 정밀화 HISTORY_REWRITE Layer 1 제거, 3 G4 actual run green) → 59 C-1 (timestamp monotonicity fixture 보강, g4-hash-chain actual run 26557936920 green).

본 cycle 발효 효과: Layer 1+2+4 통합 PASS 발효 (G4 §4.4 부분 답습 — Layer 3+5 scope 외).
본 cycle 발효 *하지 않는 것*: MVP-2 Implementation Evidence PASS 발효 0 / GP-2 PASS 0 / denyNonFastForwards 활성화 0 (DEFER) / Layer 3+5 진입 0 / R-S1 정정 0 / 신규 외부 library 0 / 자동 후속 0.

## 검토 대상 (working directory 자료, codex 직접 read 의무)

PRIMARY:
- `docs/phase0/mvp2-layer-124-pass-activation-brief.md` (v1, 본 brief, §0~§11)

직접 입력 자료:
- `docs/phase0/mvp2-layer-124-pass-entry-brief.md` (55 진입 권한 brief v1.1, E-PASS-1~15 + (γ-c) 특화 의무 4)
- `docs/phase0/mvp2-beta-submeans-decision-brief.md` (57 (β) 수단 결정 v1.1)
- `docs/review/3plus1-consensus-2026-05-28-mvp2-beta.md` (57 Reviewer 통합)
- `docs/sessions/SESSION_2026-05-28.md` (58 + 59 C-1 entry — 실 구현 + actual run)

선행 권위:
- `docs/decisions/ADR-011-means-vs-ends-redaction.md` (§2.1 (a)~(e) PASS 발효 5조건 모법)
- `docs/decisions/ADR-012-evidence-ledger-protection.md` (§2.3/§2.5/§2.7/§2.8/§3.4)
- `docs/architecture/provider-agnostic-memory-skill-design.md` (§4.4 Layer 1~5)
- `docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md` (32 MVP-1 PASS 발효 패턴 답습)

실 evidence (filesystem + CI 직접 verify 의무 — brief 의 evidence 매트릭스 검증):
- `tools/jsonl_hash_chain.py` (Layer 1, ViolationType 3종 + monotonicity 검출 line 224)
- `.github/workflows/g4-hash-chain.yml` (FAIL fixture 5 violation_type cover, PASS fixture, corpus 회귀)
- `.github/workflows/rewrite-defense.yml` + `history-anchor-verifier.yml` (Layer 2)
- `tests/fixtures/jsonl_ledger/fail/` (5 fixture: prev_hash + hash_recalc + genesis + missing_event + timestamp_monotonicity)
- `tests/fixtures/{history_anchor_verifier,rewrite_defense}/` (Layer 2 fixtures)
- `tests/canonical/` (72 files corpus)
- `git config receive.denyNonFastForwards` (Layer 2a — 미설정 DEFER 확인)

## 본 brief 핵심 주장 (검증 대상)

1. **PASS 발효 권고 = APPROVE WITH CONDITIONS** (Layer 1 완전 + Layer 2 충족(2b operative, 2a DEFER) + Layer 4 충족(C-1 보강 완료))
2. **Layer subsection 강제** (E-PASS-12, (γ-c) 의무 1) — Layer 간 evidence 합산 0
3. **Layer 2a denyNonFastForwards DEFER** (비례 보안 — 2b branch protection 8 contexts 가 operative append-only 보호, 2a = 컨테이너 배포 trigger 시점)
4. **R-S1 = Layer 통합 PASS 비차단** (MVP-2 PASS 전 hard gate, 별도 cycle — §5)
5. **"부분 답습" framing** (Layer 3+5 scope 외)

## 요청 사항

1. **verdict**: APPROVE / APPROVE WITH CONDITIONS / REVISE / REJECT 중 1
2. **BLOCKING findings** (근거 + 정정): evidence 매트릭스가 실제 repo/CI 상태와 일치하는가 (특히 E-PASS-10 timestamp C-1 actual run 26557936920 green / E-PASS-8 3 G4 run / E-PASS-7 branch protection 8 contexts)? Layer 2a DEFER 가 means-vs-ends (ADR-011 §2.1 (a) 동등 이상 보안 결과)를 약화시키는가, 아니면 2b 가 operative 충족인가? (γ-c) 특화 의무 4 (Layer subsection / 부분 답습 / 통합 동시 / RT-γ-6) 정합? PASS *발효* 와 진입 권한 혼동 0? scope 침입 (MVP-2 PASS / GP-2 PASS 합산 / denyNonFastForwards 활성화) 0?
3. **권고 (non-blocking)**
4. **NOTE / 누락**

filesystem + CI(`gh run view 26557936920`) 직접 verify 로 brief evidence 주장의 부정확/과장을 BLOCKING 분류하십시오. 특히 "Layer 4 충족" / "2a DEFER 가 2b 로 충족" 주장의 보안 타당성을 비판적으로 평가하십시오. 한국어 응답.

codex
검토 모드로 진행하겠습니다. 먼저 brief와 선행 권위 문서를 읽고, 그 다음 실제 파일/fixture/CI run 상태를 대조해서 blocking 여부를 판단하겠습니다.
exec
/bin/bash -lc "sed -n '1,260p' docs/phase0/mvp2-beta-submeans-decision-brief.md" in /home/delangi/문서/project/category/AI_development_tool
exec
/bin/bash -lc "sed -n '1,260p' docs/phase0/mvp2-layer-124-pass-entry-brief.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
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


exec
/bin/bash -lc "sed -n '1,260p' docs/phase0/mvp2-layer-124-pass-activation-brief.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
# Layer 1+2+4 통합 PASS 발효 합의 entry brief (v1)

> **작성**: 2026-05-28 (59번째 entry 진입 cycle — 신규 세션 #2)
>
> **scope**: G4 §4.4 Layer 1+2+4 통합 Implementation Evidence PASS **발효 (e2)** — 55 entry 진입 권한 (e1) → 본 cycle 발효 (e2)
>
> **본 cycle = 큰 cycle** (PASS *발효* milestone, 풀 3+1 + 외부 LLM 1+ 의무, 32 entry MVP-1 PASS 발효 답습 동형)
>
> **본 cycle 발효 자격** = (a)~(d) evidence + (e2) 풀 3+1 + 외부 LLM 1+ 합의 APPROVE + 사용자 명시
>
> **본 cycle 발효 효과** = **Layer 1+2+4 통합 PASS 발효** (G4 §4.4 Layer 1+2+4 부분 답습 — Layer 3+5 scope 외). MVP-2 Implementation Evidence PASS = Layer 통합 PASS + GP-2 PASS + R-S1 hard gate 후 별도 cycle
>
> **선행 답습**: 55 (Layer 1+2+4 통합 PASS 격상 진입 권한, `311ca3b`) + 57 ((β) R-4/L 보존/W-F 결정, `18e8ad1`) + 58 (실 구현 violation_type 정밀화, `6ebc634`, 3 G4 workflow actual run green)

---

## §0 본 brief 의 범위

### §0.1 본 brief 가 *하는* 것

1. **Layer 1/2a/2b/4 evidence 매트릭스 — Layer subsection 강제** ((γ-c) 특화 의무 1, E-PASS-12) (§2)
2. **ADR-011 §2.1 (a)~(d) 모법 + (e2) PASS 발효 자격 매핑** (Layer 별 + 통합) (§3)
3. **gap / DEFER 처리** — Layer 2a denyNonFastForwards DEFER (57/58 비례 보안 결정) + E-PASS-10 timestamp fixture + r2-canary (§4)
4. **R-S1 hard gate (RT-γ-6) PASS 시점 선행/동시 정정 *자격* 평가** ((γ-c) 특화 의무 4) (§5)
5. **합의 형태 = 풀 3+1 + 외부 LLM 1+ 정당화 + 승격 트리거** (§6)
6. **PASS 발효 권고 + 조건** (§7)
7. 금지 / 다음 단계 / cross-ref / 자기진단 (§8~§11)

### §0.2 본 brief 가 *하지 않는* 것

| # | 영역 | 위반 시점 |
|---|------|----------|
| 1 | Layer 통합 PASS *발효* 자체 (본 brief = 합의 입력, 발효 = 합의 APPROVE + 사용자 명시 후) | 0건 |
| 2 | **MVP-2 Implementation Evidence PASS 발효** (Layer 통합 PASS + GP-2 PASS + R-S1 후 별도) | 0건 |
| 3 | GP-2 송신 redaction PASS 발효 (별도 영역 — R-3 secret-hygiene actual run + R-1/R-2 trajectory) | 0건 |
| 4 | denyNonFastForwards 활성화 실행 (57/58 DEFER 답습, 비례 보안) | 0건 |
| 5 | Layer 3 (Signed commit) + Layer 5 (External anchor) 영역 진입 ("부분 답습" framing 영구) | 0건 |
| 6 | R-S1 cross-reference 정정 자체 (RT-γ-6 = 평가 한정, 정정 = 별도 cycle) | 0건 |
| 7 | 신규 외부 library 도입 (rfc8785/jcs = Q1 합의 보존, 57 (β) 답습) | 0건 |
| 8 | Hermes import (R-1) / facade real (R-2, TR-1) | 0건 |
| 9 | ADR / 헌법 / roadmap / governance / G4 / ADR-012 본문 갱신 | 0건 |
| 10 | threshold 고정 / Tier-2/3 catalog 확장 | 0건 |
| 11 | MVP-1 PASS 재선언 (32 entry 답습 유지) | 0건 |
| 12 | (γ-a/b/d) + (γ-e/f/g) 재평가 | 0건 |
| 13 | 자동 후속 cycle 진입 (MVP-2 PASS / R-S1 정정) | 0건 (사용자 명시 의무) |
| 14 | 본 brief 자체 영구화 / 권위 chain 등재 | 0건 |

### §0.3 권위 답습 source

- **ADR-011 §2.1 (a)~(d) 4조건 모법 + (e) 후속 운영조건** — `docs/decisions/ADR-011-means-vs-ends-redaction.md`
- **55 Layer 1+2+4 통합 PASS 격상 brief v1.1 §2.5 (통합) + §3 ((e1)/(e2) 분리) + §5.2 (E-PASS-1~15)** — `docs/phase0/mvp2-layer-124-pass-entry-brief.md`
- **57 (β) sub-수단 결정 brief v1.1 (R-4/L 보존/W-F) + 합의** — `docs/phase0/mvp2-beta-submeans-decision-brief.md`
- **58 실 구현 (violation_type 정밀화)** — SESSION 58 entry + `tools/jsonl_hash_chain.py` + `tests/tools/test_jsonl_hash_chain.py` + 3 G4 actual run (`26557460199` + `26557460227` + `26557460197`)
- **32 entry MVP-1 Implementation Evidence PASS 발효 합의** (PASS 발효 패턴 답습) — `docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md`
- **provider-agnostic-memory-skill-design.md §4.4** (Layer 1~5) + **ADR-012 §2.3/§2.5/§2.7/§2.8/§3.4**
- **본 cycle audit (read-only, 2026-05-28)** — evidence 가용 상태 filesystem + gh api + CI run direct

---

## §1 진입 컨텍스트 + (e1) → (e2) 전이

### §1.1 선행 chain (55 → 57 → 58)

| 합의/구현 | 본 cycle 답습 |
|----------|-----------|
| 55 통합 PASS 격상 **진입 권한 (e1)** (`311ca3b`, 4 source APPROVE WITH CONDITIONS, BLOCKING 9 + 권고 18) | (e1) 진입 권한 발효 답습 → 본 cycle = (e2) PASS 발효 |
| 57 (β) **수단 결정** (`18e8ad1`, R-4 / L 보존(rfc8785/jcs) / W-F + W-E 보조) | PASS 발효 시 채택 수단 = R-4/L 보존/W-F 답습 |
| 58 **실 구현** violation_type 정밀화 (`6ebc634`, HISTORY_REWRITE Layer 1 제거, 3 G4 workflow actual run green) | Layer 1 evidence 강화 + Layer 4 actual run 증거 (E-PASS-2/8) |

### §1.2 (γ-c) 특화 의무 4 영구 답습

| # | 의무 | 본 brief 답습 |
|---|------|-----------|
| 1 | PASS evidence template Layer 1/2/4 subsection 강제 | §2 Layer subsection 분리 (E-PASS-12) |
| 2 | "defense-in-depth 부분 답습" framing (Layer 3+5 = scope 외) | §0.2 #5 + §2 "부분 답습" 표현 |
| 3 | Layer 1+2+4 통합 PASS evidence 동시 발효 (evidence 합산 금지) | §2.5 통합 (Layer subsection 분리 유지) |
| 4 | RT-γ-6 R-S1 PASS 시점 선행/동시 정정 *평가* 의무 | §5 평가 (정정 = 별도 cycle) |

---

## §2 Evidence 매트릭스 (Layer subsection 강제 — E-PASS-12, (γ-c) 의무 1)

⚠️ **Layer 별 evidence subsection 분리 강제, Layer 간 evidence 합산 금지** (54 entry §5 #9 / RT-PASS-2 답습).

### §2.1 Layer 1 — Hash Chain (MANDATORY) ✅

| Evidence | 상태 | 출처 |
|---------|------|------|
| E-PASS-1: hash chain PASS fixture rc=0 (× 2) | ✅ | `g4-hash-chain.yml:182` PASS fixture step (minimal_chain + roundtrip_t2_strict), 58 actual run `26557460199` green |
| E-PASS-2: violation_type 검출 actual run | ✅ | `g4-hash-chain.yml:197` FAIL fixture (prev_hash_mismatch + hash_recalculation + genesis_mismatch + schema_missing_field), 58 entry violation_type 정밀화 (HISTORY_REWRITE Layer 1 제거 → 3 Layer-1 type + schema) |
| E-PASS-3: canonical JSON sha256 동등성 | ✅ | corpus 회귀 Primary 1 (rfc8785) + Primary 2 (jcs) byte+sha256 + jq fallback equivalence (`tests/canonical/` 72 files / 8 카테고리) + NaN/Inf reject |
| E-PASS-4: genesis hash 첫 entry | ✅ | `compute_genesis_hash` + genesis_mismatch fixture |

→ **Layer 1 = 완전 충족** (PoC 시제 + actual run green + 58 violation_type 정밀화).

### §2.2 Layer 2a — local denyNonFastForwards ⚠️ DEFER

| Evidence | 상태 | 출처 |
|---------|------|------|
| E-PASS-5: denyNonFastForwards 활성화 + force-push reject PoC | ⚠️ **DEFER** | 57/58 사용자 비례 보안 결정 — per-repo local config = 컨테이너 미배포 상태 ceremony, GitHub branch protection (Layer 2b) 이 operative 보호 제공 |

→ **Layer 2a = DEFER** (비례 보안). Layer 2 의 append-only 보호 = Layer 2b (§2.3) 가 operative 충족. 2a = 실 컨테이너 배포 trigger 시점 활성화 (별도, [[feedback_proportionate_security_personal_tool]] 답습).

### §2.3 Layer 2b — remote branch protection ✅

| Evidence | 상태 | 출처 |
|---------|------|------|
| E-PASS-7: branch protection rule actual state | ✅ | gh api main protection 8 contexts = `["guard","verify","feasibility","scan","enforce","defense","validate","bypass-detect"]` + force push/delete false (43 entry 답습) |

### §2.4 Layer 2 — history (rewrite/deletion 검출) ✅

| Evidence | 상태 | 출처 |
|---------|------|------|
| E-PASS-6: base branch JSONL line deletion/rewrite 감지 actual run | ✅ | `rewrite-defense.yml` (58 actual run `26557460227` green) + `history-anchor-verifier.yml` (58 actual run `26557460197` green) + FAIL fixtures 8 (append_only force_push/reorder + line_regression deletion/rewrite + anchor full_rewrite/middle_deletion/substitution/tail_truncation) |

→ **Layer 2 = 충족** (2b operative + history 검출 actual run green, 2a DEFER 문서화).

### §2.5 Layer 4 — CI 회귀 검증 (MANDATORY) ✅ 부분

| Evidence | 상태 | 출처 |
|---------|------|------|
| E-PASS-8: 4 G4 workflow actual run PASS | ✅ 3/4 | 58 entry: g4-hash-chain `26557460199` + rewrite-defense `26557460227` + history-anchor-verifier `26557460197` 전원 green. r2-canary (R-6/R-2 canary) = path 미트리거 (별도 §4.3) |
| E-PASS-9: canonical 위반 BLOCK | ✅ | corpus 회귀 Primary 1/2 byte+sha256 mismatch BLOCK + NaN/Inf reject (RFC 8785 §3.2.2.2) |
| E-PASS-10: timestamp monotonicity 위반 BLOCK | ✅ | 코드 검출 (`jsonl_hash_chain.py:224` monotonicity_violation) + **C-1 보강 (59 entry): `timestamp_monotonicity.jsonl` fixture 추가 (valid chain + ts 역행) → g4-hash-chain.yml 5 violation_type cover, actual run `26557936920` green** |
| E-PASS-11: R-6 workflow 확장 step actual run | ⚠️ W-F | W-F (기존 보존, 신규 step 0) 답습 — 별도 R-6 step 미추가. Layer 4 회귀 = 3 ledger workflow 가 충족 |

→ **Layer 4 = 충족** (3 ledger workflow green + canonical BLOCK ✅ + timestamp monotonicity ✅ C-1 보강, r2-canary 미트리거는 R-6/R-2 영역).

### §2.6 통합 evidence ((γ-c) 의무 3 — 동시 발효, Layer subsection 분리 유지)

| Evidence | 상태 |
|---------|------|
| E-PASS-12: 통합 evidence (Layer subsection 분리 명시) | ✅ 본 §2 (Layer 1/2a/2b/2/4 subsection 분리, 합산 0) |
| E-PASS-13: 합의 보고서 commit | ⏳ 본 cycle 합의 |
| E-PASS-14: 외부 LLM 1+ (cross-vendor) | ⏳ 본 cycle codex |
| E-PASS-15: R-S1 정정 자격 평가 (RT-γ-6) | §5 |

---

## §3 ADR-011 §2.1 (a)~(e2) PASS 발효 자격 매핑

| # | 조건 | Layer 1 | Layer 2 (2a+2b) | Layer 4 | 통합 |
|---|------|------|------|------|----|
| (a) | 동등 이상 보안 결과 | ✅ middle tampering 차단 (3 violation type) | ✅ 2b force push/delete 차단 + history 재작성 차단 (2a DEFER, 2b operative) | ✅ CI 회귀 (canonical BLOCK + timestamp monotonicity, C-1 보강) | Layer 1+2+4 통합 (subsection 분리) |
| (b) | 격리 환경 PoC 실증 | ✅ jsonl_hash_chain + fixtures | ✅ 2b actual state + history fixtures 8 | ✅ 3 G4 actual run green | 통합 (합산 0) |
| (c) | ADR/SDD 권위 명시 | ✅ G4 §4.4.1 + ADR-012 §2.3/§2.8 | ✅ 동상 | ✅ 동상 | ✅ |
| (d) | 자동 회귀 검증 경로 | ✅ g4-hash-chain CI | ✅ rewrite-defense + history-anchor CI | ✅ 3 ledger workflow CI green | ✅ |
| **(e2)** | **PASS 발효 합의 APPROVE** | ⏳ 본 cycle | ⏳ 본 cycle | ⏳ 본 cycle | ⏳ **본 cycle 풀 3+1 + 외부 LLM + 사용자 명시** |

→ **(a)~(d) 충족 = Layer 1 완전 / Layer 2 충족 (2a DEFER 문서화, 2b operative) / Layer 4 충족 (C-1 timestamp 보강 완료, r2-canary = R-6/R-2 영역)**. (e2) = 본 cycle 합의.

---

## §4 gap / DEFER 처리

### §4.1 Layer 2a denyNonFastForwards = DEFER (비례 보안)

- 57/58 사용자 결정: per-repo local config + Dockerfile/entrypoint = 컨테이너 미배포 상태 ceremony. GitHub branch protection (Layer 2b, 8 contexts + force push/delete false) = operative append-only 보호.
- **PASS 발효 영향**: Layer 2 의 append-only *결과* = 2b 가 충족. 2a = 실 컨테이너 배포 시점 활성화 (별도 trigger). PASS 발효 = 2b operative 기반 + 2a DEFER 명문.

### §4.2 E-PASS-10 timestamp monotonicity fixture (C-1) — ✅ 보강 완료 (합의 전 미리 보강, 사용자 명시)

- 코드 검출 확인 (`validate_chain:224` — `cur_ts < prev_ts` → monotonicity_violation).
- **C-1 보강 완료 (59 entry, commit `4c48099`)**: `tests/fixtures/jsonl_ledger/fail/timestamp_monotonicity.jsonl` 추가 (valid chain genesis/prev_hash/entry hash + ts 역행 → monotonicity_violation 단독) + g4-hash-chain.yml FAIL fixture step 4→5 violation_type cover (W-F 기존 workflow 內 보강) + TDD test (test_validate_chain_monotonicity_violation). **actual run `26557936920` green** → E-PASS-10 CI 입증.

### §4.3 r2-canary (E-PASS-11) 미트리거

- r2-canary = R-6/R-2 redaction canary (paths = docker/r4-1-poc, docker/r2-poc, canary docs). Layer 1+2+4 *ledger* 검증 핵심 아님 (3 ledger workflow 가 Layer 4 충족).
- **권고**: r2-canary 는 GP-2 영역 (R-3) 또는 workflow_dispatch 로 별도 actual run. 본 Layer 통합 PASS 영향 = 3 ledger workflow 로 충족.

---

## §5 R-S1 hard gate (RT-γ-6) PASS 시점 선행/동시 정정 *자격* 평가

- R-S1 = ADR-012 *자체 내부* §2.3 (4-layer numbering) vs §2.8 / G4 §4.4.1 (5-layer numbering) divergence (52/53 entry 5 source verify CONFIRMED).
- **RT-γ-6 평가** (54 §1.3 의무 4): MVP-2 Implementation Evidence PASS 발효 시점 R-S1 정정 선행/동시 *자격* 평가 의무. **단 본 cycle = Layer 통합 PASS 발효 (MVP-2 PASS 아님)**. R-S1 정정 = MVP-2 PASS 전 hard gate (3 옵션: ADR-012 §2.3 정정 / §2.8 강화 / 권위 선언) — **별도 cycle**.
- **본 cycle 영향**: Layer 통합 PASS 는 G4 §4.4.1 numbering (PRIMARY, 5-layer) 답습 — R-S1 정정 *전*에도 G4 §4.4.1 권위로 Layer 1+2+4 정의 명확 (52 brief v1.1 답습). **Layer 통합 PASS 발효 = R-S1 정정 미종속** (MVP-2 PASS 가 종속, B-8 답습 "평가 의무" framing).

→ **R-S1 = Layer 통합 PASS 발효 비차단** (MVP-2 PASS 전 hard gate, 별도 cycle). 본 cycle = 평가 한정.

---

## §6 합의 형태 + 풀 3+1 승격 트리거

### §6.1 합의 형태 = 풀 3+1 + 외부 LLM 1+ (의무)

**정당화**: PASS *발효* milestone (32 entry MVP-1 PASS 발효 답습 동형) + 55 §8 #3 "Layer 통합 PASS 발효 합의 = 풀 3+1 + 외부 LLM 1+" + 큰 결정 (ADR-011 §2.4 T3) + 헌법 5조-2 cross-vendor.

### §6.2 7 풀 3+1 승격 트리거

| # | trigger | 발화 | 근거 |
|---|---------|----|------|
| 1 | 큰 결정 (PASS 발효 milestone) | ✅ | Layer 1+2+4 통합 PASS 발효 = MVP-2 PASS 직전 |
| 2 | 아키텍처/SDD/보안 본문 변경 | ❌ | brief = phase0 신규 1, 본문 0 |
| 3 | ADR 본문 변경 | ❌ | 0 |
| 4 | 권위 chain 다중 source 손상 | ⚠️ 부분 | R-S1 (RT-γ-6 평가 한정) |
| 5 | 외부 LLM 통합 필요 | ✅ | cross-vendor 의무 |
| 6 | Tier-2/3 catalog 확장 | ❌ | 0 |
| 7 | Hermes PMO 격상 | ❌ | 0 |

→ **2/7 발화 + 1 부분 → 풀 3+1 + 외부 LLM 1+ 적격**.

---

## §7 PASS 발효 권고 + 조건

⭐ **권고 = Layer 1+2+4 통합 PASS 발효 APPROVE WITH CONDITIONS**:

1. **Layer 1 + Layer 2 + Layer 4 (3 ledger workflow) = (a)~(d) 충족** — actual run green (58 entry 3 G4 run + 59 C-1 g4-hash-chain `26557936920`) + Layer subsection 분리 evidence.
2. **조건 처리 상태**:
   - (C-1) E-PASS-10 timestamp monotonicity FAIL fixture = ✅ **보강 완료** (`4c48099`, actual run `26557936920` green, 합의 전 미리 보강 사용자 명시)
   - (C-2) Layer 2a denyNonFastForwards DEFER 명문 (2b operative 충족 근거) — 비례 보안 답습 (잔여 문서화 조건)
   - (C-3) r2-canary = R-6/R-2 영역 명시 (Layer 통합 PASS 비차단), workflow_dispatch 별도
3. **R-S1 = Layer 통합 PASS 비차단** (MVP-2 PASS 전 hard gate, 별도 cycle, §5).
4. **"부분 답습" framing 영구** (Layer 3+5 scope 외).

→ **PASS 발효 자격 = (a)~(d) 충족 (C-1 완료) + (e2) 합의 APPROVE + 사용자 명시 + (C-2) 2a DEFER 명문**.

---

## §8 금지 사항

§0.2 답습 (14). 추가: MVP-2 PASS 자동 선언 0 / GP-2 PASS 합산 0 / denyNonFastForwards 자동 활성화 0 / R-S1 자동 정정 0 / Layer 3+5 진입 0 / 자동 후속 cycle 0.

---

## §9 다음 단계 (사용자 명시 의무 — 자동 진입 0)

1. 본 brief 승인 → 풀 3+1 + 외부 LLM 1+ (codex (E-α)) → Reviewer 통합 → brief v1.1 흡수 → commit + push → **Layer 1+2+4 통합 PASS 발효**
2. (C-1) timestamp fixture 보강 (PASS 발효 조건 또는 후속 자율)
3. **MVP-2 Implementation Evidence PASS 발효 합의** (Layer 통합 PASS + GP-2 PASS + R-S1 hard gate 후 별도, 32 entry 답습)
4. R-S1 cross-reference 정정 cycle (MVP-2 PASS 전 hard gate 3 옵션)
5. GP-2 PASS 영역 (R-3 secret-hygiene actual run + R-1/R-2 trajectory)

---

## §10 cross-reference 답습

- ADR-011 §2.1 (a)~(e) — `docs/decisions/ADR-011-means-vs-ends-redaction.md`
- ADR-012 §2.3/§2.5/§2.7/§2.8/§3.4 — `docs/decisions/ADR-012-evidence-ledger-protection.md`
- provider-agnostic-memory-skill-design.md §4.4 (Layer 1~5)
- 55 통합 PASS 격상 진입 brief v1.1 — `docs/phase0/mvp2-layer-124-pass-entry-brief.md`
- 57 (β) 결정 brief v1.1 + 합의 — `docs/phase0/mvp2-beta-submeans-decision-brief.md` + `docs/review/3plus1-consensus-2026-05-28-mvp2-beta.md`
- 58 실 구현 — `tools/jsonl_hash_chain.py` + `tests/tools/test_jsonl_hash_chain.py` + 3 G4 actual run
- 32 MVP-1 PASS 발효 합의 — `docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md`
- 실 evidence: `g4-hash-chain.yml` + `rewrite-defense.yml` + `history-anchor-verifier.yml` + branch protection 8 contexts + `tests/fixtures/{jsonl_ledger,history_anchor_verifier,rewrite_defense}` + `tests/canonical/` 72

---

## §11 자기진단 (메타 편향 회피)

| # | 위험 | 처리 |
|---|------|----|
| P-1 | 본 brief 가 PASS 발효를 *기정사실화* | 발효 = 합의 APPROVE + 사용자 명시 후 (§0.2 #1 + §9) |
| P-2 | evidence gap (timestamp fixture / 2a DEFER) 은폐 | §2.5 + §4 명시 (honest matrix, 57 (β) B-1 cascade 교훈 — 시제 주장 over-claim 방지) |
| P-3 | 2a DEFER 가 Layer 2 충족 *과대* | §2.2 + §4.1 = 2b operative 충족 근거 명시, 2a = 컨테이너 배포 trigger 시점 |
| P-4 | 본 brief 작성자 = 55/57/58 작성자 (Claude) cascade risk | cross-vendor (E-α) codex + 풀 3+1 독립 검증 (57 (β) 동형 — codex/Agent 가 B-1 포착한 process 가치) |
| P-5 | timestamp fixture gap 을 BLOCKING vs 자율 보강 판단 | §7 (C-1) 조건 명시, 풀 3+1 판정 위임 |
| P-6 | R-S1 RT-γ-6 = Layer 통합 PASS 차단 오해 | §5 = MVP-2 PASS 전 hard gate (Layer 통합 PASS 비차단), B-8 "평가 의무" 답습 |


codex
1차 확인으로 activation brief는 55/57의 범위 분리 문구를 대부분 계승하고 있습니다. 이제 실제 구현 파일, fixture 수량, workflow step, branch protection, 해당 run `26557936920`를 직접 확인해서 과장 여부를 가르겠습니다.
exec
/bin/bash -lc "sed -n '1,260p' docs/review/3plus1-consensus-2026-05-28-mvp2-beta.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
# 3+1 합의 통합 보고서 — (β) sub-수단 결정 entry brief (57 entry)

> **작성**: 2026-05-28 (Reviewer 통합)
>
> **대상**: `docs/phase0/mvp2-beta-submeans-decision-brief.md` (v1)
>
> **합의 형태**: 풀 3+1 + 외부 LLM 1+ (cross-vendor codex gpt-5.5) — 4 source
>
> **입력**: Agent A (구현 분석가, filesystem direct) + Agent B (품질/안전성) + Agent C (대안 탐색) + codex (OpenAI gpt-5.5, cross-vendor blind) — 3 Agent 병렬 독립 (상호 미참조) + codex 독립

---

## §1 4 source verdict 요약

| source | verdict | BLOCKING | 핵심 |
|--------|---------|---------|------|
| Agent A (구현 분석가) | APPROVE WITH CONDITIONS | 3 (R-A-1/2/3) | filesystem 17건 verify — 시제 framing 이 실 동작 범위보다 넓음 |
| Agent B (품질/안전성) | REVISE | 3 (R-B-1/2/3) | 권위 인용 전도 (R-1 MANDATORY / ADR-012 §2.1) + L-1 stdlib 불일치 |
| Agent C (대안 탐색) | REVISE | 2 (R-C-1/2) | L-1 시제 거짓 (실측) + W-A(ii) 명칭 부정확 |
| codex (cross-vendor) | REVISE | 3 (BL-1/2/3) | L 권고 전제 repo 불일치 + 외부 의존성 0 과장 + violation_type evidence |

→ **Reviewer 통합 verdict = REVISE** (3 REVISE + 1 APPROVE WITH CONDITIONS). **결정 방향 (R-4 / L 보존 / W 보존)은 4 source 전원 정합 판정** → REJECT 아님, **brief v1.1 1pass 흡수** (ceremony-inflation 차단, 52/55 entry 동형).

---

## §2 cross-validation 매트릭스

### §2.1 Consensus BLOCKING (multi-source 일치)

| # | BLOCKING | source | 근거 (Reviewer verify) | 정정 방향 |
|---|----------|--------|---------------------|---------|
| **B-1** ⭐⭐⭐ (4-way) | **L-1 stdlib 시제 충족 / 외부 의존성 0 주장 = 거짓** | R-A-2 + R-B-3 + R-C-1 + codex BL-1/BL-2 | Reviewer 직접 verify: `requirements-dev.txt:20-21` = `rfc8785==0.1.4` + `jcs==0.2.1` 고정 / `jsonl_hash_chain.py:99` runtime = `CrossCheckMode.PRIMARY_1_ONLY` (rfc8785 단독, stdlib json.dumps 미사용) / `canonical_json.py:33-42` rfc8785/jcs Primary (try-import) / `g4-hash-chain.yml:64-69` CI `pip install rfc8785 jcs`. **rfc8785/jcs = Q1 합의 2026-05-10 (`3plus1-consensus-2026-05-10-g4-jcs-library-selection.md`) 이미 채택**. 실 시제 = L-5 (외부 library Primary), L-4 (stdlib) 아님 | L 결정 = **"기존 rfc8785/jcs Primary PoC 보존 (Q1 합의 답습) + L-3, 본 cycle 신규 외부 library 도입 0"** 으로 정정. "외부 의존성 0 / stdlib 단독 시제 충족" 삭제. "현 PoC 외부 library 미사용" (false) vs "본 cycle 신규 도입 0" (true) 분리 |
| **B-2** ⭐⭐ (2-way) | **HISTORY_REWRITE dead enum + "4 violation_type 시제 충족" 과장** | R-A-1 + codex BL-3 | `jsonl_hash_chain.py` HISTORY_REWRITE = enum 정의만 (validate_chain emission 0). `g4-hash-chain.yml:197` FAIL 4 cover = prev_hash_mismatch + hash_recalculation + **schema_missing_field** + genesis_mismatch (history_rewrite 아님). brief §1.2 "4 violation_type 시제 충족" vs §7.1 조건 5 "history_rewrite fixture 추가" 자기모순 | "3 violation_type actual emission (PREV_HASH_MISMATCH + HASH_RECALCULATION + GENESIS_MISMATCH) + HISTORY_REWRITE enum 정의만 (fixture 추가 = 조건 6 #5 실 구현 입력)" 분리 |

### §2.2 단독 격상 BLOCKING (Reviewer raw verify 격상)

| # | BLOCKING | source | 근거 (Reviewer verify) | 정정 방향 |
|---|----------|--------|---------------------|---------|
| **B-3** ⭐⭐ | **R-1 "MANDATORY (ADR-011 §2.3 #2)" 권위 전도** | Agent B R-B-1 | Reviewer 직접 verify: ADR-011 §2.3 운영 함의 #2 (line 112) verbatim = "**Hermes 자체 redaction은 로그/LLM 송신 방어로만 신뢰**: 저장 경로(DB/파일) 차단 책임 없음." = *신뢰 범위 한정* 진술, "MANDATORY" 근거 아님. R-4 채택 핵심 정당화가 모법 과장 | R-1 등급 "MANDATORY (ADR-011 §2.3 #2)" → "GP-2 송신/로그 방어 신뢰 수단 (§2.3 #2 — 저장 경로 책임 0)". R-4 정당화 = defense-in-depth (ends) 기반, "R-1 MANDATORY" 미사용 |
| **B-4** | **"ADR-012 §2.1 = 의존성 추가 PoC 재실행 trigger" misattribution** | Agent B R-B-2 | Reviewer 직접 verify: ADR-012 §2.1 (line 6/64) = "수단/목적 분리" 참조, 의존성 trigger 아님. 정확 권위 = **ADR-011 §2.3 운영 함의 #4 (line 113) "Hermes 의존성 업그레이드는 자동 R-2 재실행으로 회귀 검증 (R-6)"** + governance. brief 다수 위치 답습 | "ADR-012 §2.1 trigger" → "ADR-011 §2.3 #4 (의존성 변경 → R-2/R-6 자동 재실행)". 단 rfc8785/jcs = Q1 합의 이미 채택이므로 본 L 영역 = 신규 도입 0 (trigger 발화 0) |
| **B-5** | **"보존 우선 = W-A(ii) 변형" 명칭 부정확** | Agent C R-C-2 | W-A 본질 = *단일 통합*, 권고 실질 = *분산 보존 (신규 0)* = 정반대 framing. brief 스스로 "명칭상 W-A(ii), 실질 보존우선" 자인 → 명칭 혼선 후속 전가 | **W-F (분산 보존, 신규 통합/신설 0) 신규 라벨** 정의 또는 (통합/분리)×(신설/보존) 2축 분류 명시. 권고 = W-F + W-E 보조 |
| **B-6** | **조건 6 §7.1 표 R-3 (secret-hygiene) actual run 누락 + 조건 2 매핑 모호** | Agent A R-A-3 | 조건부 승인 조건 6 표가 R-3 (GP-2 (d) 핵심 gating) actual run 을 조건에서 누락. 조건 2 (r2-canary) = R-2 영역이라 R/W 매핑 모호 | 조건 6 표에 R-3 (secret-hygiene-egress-redaction.yml actual run) 명시 + 조건 2 r2-canary 매핑 정정 |

### §2.3 Partial / Divergence

| 영역 | divergence | Reviewer 판정 |
|------|-----------|-------------|
| **W 권고 정합성** | codex = "W-A 단일통합 권고를 repo 현실에 맞춘 정밀화로 정합" vs Agent C = "명칭 부정확 BLOCKING" | **Partial → B-5 로 해소**. 실질 권고 (기존 분산 보존, 신규 0) = 4 source 정합, *라벨* 만 W-F 로 정정 (Agent C 명칭 지적 채택 + codex 실질 정합 판정 동시 충족) |
| **R 권고 정합성** | codex/Agent A/C = "R-4 means-vs-ends 정합" vs Agent B = "R-1 MANDATORY framing 정정 필요" | **Partial → B-3 로 해소**. R-4 결정 자체 = 정합, R-1 *등급 표현* 만 정정 |

### §2.4 Consensus 정합 확인 (BLOCKING 아님 — 4 source 일치)

- ✅ `tests/canonical/` = 72 files / 8 카테고리 / 24 input cases (Agent A + codex 직접 count, B/C 확인)
- ✅ `agent/redact.py` 본 repo 부재 (R-1 upstream 주장 정확) — 4 source
- ✅ `src/adapters/llm/facade.py` placeholder (R-2 trajectory 주장 정확) — 4 source
- ✅ 5 workflow 보존 상태 (실 repo 총 12 workflow, Agent A 발견 — W 보존 권고 강화)
- ✅ `secret_scanner.py --mode scan-log` + registered 45 patterns (R-3 시제 정확) — Agent A/B/C/codex
- ✅ `receive.denyNonFastForwards` local/global 미설정 (실 구현 sub-cycle 입력 정확) — 4 source
- ✅ (γ-c) 특화 의무 4 전원 정합 (Layer subsection / "부분 답습" framing / 통합 동시 / RT-γ-6) — Agent B + codex
- ✅ scope 침입 0건 (실 구현 / 외부 library 도입 / Hermes import / facade real 침입 0) — Agent B
- ✅ R-5 base64 evasion 영구 분리 = known limitation 정당 (secret_scanner.py docstring + 모법) — Agent B
- ✅ history-anchor-verifier.yml = Layer 5 PoC 시제 존재가 Layer 5 진입 유발 0 (55 B-2 답습 정확) — Agent B

---

## §3 권고 (non-blocking, 통합)

| # | 권고 | source | v1.1 흡수 |
|---|------|--------|---------|
| N-1 | "45 = Tier-1 42 + baseline 5" 산술 혼란 → "registered 45 (Tier-1 42 catalog compliant)" | codex | §1.2 표현 정정 |
| N-2 | L-1.5 (stdlib auto-degrade) 중간 대안 추가 (현 PRIMARY_1_ONLY = degrade 없음) | Agent C | §3 대안 + 별도 실 구현 sub-cycle 선택 명시 |
| N-3 | RFC 8785 strict = interop 목적, ≠ 무결성 ends — ends/means 구분 | Agent C | §3.2 means-vs-ends 정합 보강 |
| N-4 | R-4 ≡ "R-3 단독 + R-1/R-2 deferred" framing 선택지화 | Agent C | §2.2 framing 명시 |
| N-5 | R-3 = GP-2 (d) detection 충족 / (a) prevention = R-1/R-2 의존 (facade placeholder 시 능동 redaction 0) | Agent B + Agent A NT | §2.2 + RT-R-2 보강 |
| N-6 | library 버전 drift risk + 성능 미평가 NOTE | Agent A | §7 NOTE |
| N-7 | "L-2/L-5 영구 분리" → "신규 외부 JCS library 도입/운영 승격 = 별도 cycle" | codex | §3 표현 정정 |

---

## §4 v1.1 흡수 매트릭스 (BLOCKING 6 + 권고 7 1pass)

| 흡수 영역 | brief v1.1 정정 |
|---------|---------------|
| B-1 (L stdlib 거짓) | §1.2 + §3.1 + §3.2 + §3.3 + §5.1 — L 결정 "기존 rfc8785/jcs PoC 보존 (Q1 합의 답습), 신규 도입 0" 으로 전면 정정 |
| B-2 (HISTORY_REWRITE dead enum) | §1.2 + §7.1 — "3 emission + HISTORY_REWRITE fixture = 조건 6 실 구현 입력" 분리 |
| B-3 (R-1 권위 전도) | §2.1 + §2.2 — R-1 등급 정정 (§2.3 #2 = 신뢰 범위 한정) |
| B-4 (ADR-012 §2.1 misattribution) | §0.2 #8 + §3.2 + §11 — "ADR-011 §2.3 #4" 정정 |
| B-5 (W 명칭) | §4.1 + §4.2 + §5.1 — W-F (분산 보존, 신규 0) 라벨 정의 |
| B-6 (조건 6 R-3 누락) | §7.1 — R-3 actual run 추가 + 조건 2 매핑 정정 |
| 권고 N-1~N-7 | §1.2 / §2.2 / §3 / §7 in-place |

---

## §5 메타 자기진단 (Reviewer)

| # | 위험 | 처리 |
|---|------|----|
| M-1 | 3 Agent 병렬 독립 미보장 risk | Agent A/B/C 상호 미참조 명시 (각 응답 헤더) + codex 독립 (cross-vendor blind) |
| M-2 | cross-vendor 형식 미충족 | codex = OpenAI gpt-5.5, Agent = Anthropic Claude — 헌법 5조-2 충족 |
| M-3 | Reviewer 격상 (B-3/B-4) 자체 권위 over-reach | Reviewer 직접 raw verify (ADR-011 §2.3 line 112/113 + ADR-012 §2.1 line 6/64 + requirements-dev:20 + jsonl_hash_chain:99) — single-source 격상은 verify 후만 |
| M-4 | REVISE → REJECT 회피 편향 | 4 source 전원 "결정 방향 정합" 판정 명시 (R-4/L 보존/W 보존) — 방향 타당 → 1pass 흡수 정당 |
| M-5 | ceremony-inflation (v2 cycle) | 1pass 흡수 (52/55 entry 동형), 별도 v2 cycle 0 |
| M-6 | 본 cycle 자체 진행 (수단 결정 발효를 실 구현/PASS 발효로 확대) | 본 합의 = 수단 결정 진입 자격 한정, 실 구현 0 / PASS 발효 0 / 외부 library 신규 도입 0 |

---

**본 합의 verdict = REVISE → brief v1.1 1pass 흡수 (BLOCKING 6 + 권고 7) → 수단 결정 발효 자격 충실 (R-4 + L 보존 + W-F + W-E 보조)**.

**본 합의 발효 = brief v1.1 commit + SESSION + INDEX commit + push 후** (단계별 합의 cycle 답습).

exec
/bin/bash -lc "sed -n '1,360p' docs/sessions/SESSION_2026-05-28.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
# SESSION 2026-05-28 — 51번째 entry: MVP-2 진입 자격 audit brief (G2 GP-2 + G4 §4.4 Layer 4) Reviewer-only 단축 합의 APPROVE

> **세션 시작**: 2026-05-28 (50 entry 종료 marker 직후 carry-over 진입). 사용자 carry-over #4 명시 "4번 MVP-2 진입 자격 검토로 진행" → audit brief 작성 cycle 진입.
>
> **본 entry 흐름**: 의존 자료 audit (현 상태 + governance §4 + G4 §4.4 + ADR-012 §2.3 + roadmap-mvp1 + ADR-011 §2.1) → 사용자에게 scope 확인 (`AskUserQuestion` (a)/(b)/(c) 3 옵션) → 사용자 명시 (a) audit brief 한정 선택 → brief v1 작성 (372줄) → 사용자 승인 → Reviewer-only 단축 합의 APPROVE (184줄) → SESSION + INDEX commit.

## 결과 요약

⭐⭐ **51번째 entry — MVP-2 진입 자격 audit brief Reviewer-only 단축 합의 APPROVE 발효**. 50 entry carry-over #4 "MVP-2 진입 자격 검토 (G2 GP-2 송신 redaction + G4 §4.4 Layer 4)" 처리 = 본 entry audit 산출 한정. **본 cycle = audit 한정, 23 entry `mvp1-gp3-gp5-current-state-audit-brief.md` 답습 작은 cycle**.

- brief v1 작성 (`docs/phase0/mvp2-entry-eligibility-audit-brief.md`, 372줄, §0~§11): scope/MVP-1 답습 답습/MVP-2 영역 정의/GP-2 Entry+Exit audit/G4 §4.4 Layer 4 Entry+Exit audit/통합 R-6 workflow 확장 권고/Rollback Trigger 7/Evidence 9/합의 형태 권고/금지 사항/다음 단계/cross-reference 17 source/자기진단 5
- Reviewer-only 단축 합의 APPROVE (`docs/review/3plus1-consensus-2026-05-28-mvp2-entry-eligibility-audit.md`, 184줄): 5/5 풀 3+1 승격 trigger 0건 발화 (자체 + Reviewer 독립 verify cross-confirm) + 의존 권위 source 7/7 정확 답습 + 14/14 verbatim 모순 0건 + sub-수단 결정 0 영구 분리 + 23 entry 동형 패턴

**원칙 준수**: 실 코드 0 / CI 0 / hook 0 / branch protection 0 / config 본문 변경 0 / ADR 본문 갱신 0 / 헌법 0 / roadmap-mvp1 본문 0 / governance-preconditions 본문 0 / provider-agnostic-memory-skill-design 본문 0 / ADR-012 본문 0 / MVP-2 진입 발효 0 / MVP-1 PASS 재선언 0 / Operational Readiness PASS 0 / Hermes PMO 격상 0 / sub-수단 결정 0 (R-1~R-5 + L-1~L-5 후보 식별만) / threshold 고정 0 / Tier-2/3 catalog 확장 0 / 외부 library 도입 결정 0 / 다른 Layer 진입 결정 0 / 다른 GP 진입 결정 0 / `adapters/llm/facade.py` placeholder 변경 0 / 자동 진입 0 (단계별 cycle 답습) — **23/23 유지**.

## 흐름

| 단계 | 산출 | commit |
|---|---|---|
| 세션 시작 + carry-over #4 명시 | (대화) | — |
| 의존 자료 audit (현 상태 + governance §4 + provider-agnostic-memory-skill-design §4.4 + ADR-012 §2.3 + roadmap-mvp1 §1.2/§1.3 + ADR-011 §2.1 + 33/50 entry) | (read-only) | — |
| ⭐ G4 §4.4 Layer 4 = CI 회귀 검증 (MANDATORY) 해석 확정 + **두 영역 통합 R-6 workflow 답습 확장 핵심 발견** | (audit 결과) | — |
| 사용자 scope 확인 (`AskUserQuestion` (a) audit brief / (b) entry brief / (c) roadmap-mvp2 신규) | 사용자 명시 (a) 선택 | — |
| ⭐ brief v1 작성 | `docs/phase0/mvp2-entry-eligibility-audit-brief.md` (372줄) | (본 정리 commit) |
| 사용자 승인 | (대화) | — |
| ⭐ Reviewer-only 단축 합의 APPROVE | `docs/review/3plus1-consensus-2026-05-28-mvp2-entry-eligibility-audit.md` (184줄, 5/5 trigger 0건 + 14/14 verbatim + 7/7 source + M-1~M-5 메타 편향 자기진단) | (본 정리 commit) |
| 본 정리 commit | SESSION + INDEX | (본 commit) |

## carry-over (51번째 entry — 신규)

**해소 누적 (본 entry)**:
- ✅ 50 entry carry-over #4 "MVP-2 진입 자격 검토" (본 audit brief 발효로 처리)

**다음 세션 진입 후보 (carry-over 5건 — 50 entry 답습 유지 + 본 entry 신규)**:

| # | 후보 | 영역 | 규모 |
|---|---|---|---|
| 1 | (b1-PC1-D6-ast-context) AST SAFE_CONTEXT 영구 정밀화 (42 entry, 50 entry 답습) | 별도 cycle | 풀 3+1 |
| 2 | FORCE_JAVASCRIPT_ACTIONS_TO_NODE24 사전 evidence (47 entry codex 권고 1, 50 entry 답습) | chore | 1-agent 직접 |
| 3 | (d) facade real (TR-1, `adapters/llm/facade.py` placeholder → real, 50 entry 답습) | **큰 cycle** | 풀 3+1 + 외부 LLM 1+ |
| 4 | ⭐ **(α) MVP-2 진입 합의 entry brief** (24 entry 답습 — 본 audit brief = 입력 자료) | **큰 cycle** (메인 권위) | **풀 3+1 + 외부 LLM 1+ (cross-vendor 의무)** |
| 5 | (β) sub-수단 결정 cycle — R-1/2/3/4/5 (GP-2) + L-1/2/3/4/5 (G4 §4.4 Layer 4) — 별도 합의 영역 또는 (α) 內 흡수 | 별도 cycle | 풀 3+1 |
| 6 | (γ) 분리 영역 결정 — G4 §4.4 Layer 1+2 의존 영역 우선 진입 vs Layer 4 동시 진입 (Entry 자격 매트릭스 답습) | 별도 cycle | 풀 3+1 |
| 7 | 32 entry 프라이데이 D-1~D-8 합의 (자비스 4 invariant 영구 보존 + 5 layer 격리, 50 entry 답습) | **큰 cycle** | 풀 3+1 + 외부 LLM 1+ |

**자율 영역 carry-over** (PASS 효과 영향 0건 — 50 entry 답습 유지):
- (E-D6-2) nightly schedule 첫 발화 actual run id capture (2026-05-28 KST 12:00 이후, 48 entry)
- (b1-PC1-D6-evidence-workflow-dispatch) workflow_dispatch 수동 발화 evidence (선택)
- (b1-AR3 develop) develop branch 생성 시점 8 contexts 적용 (사용자 영역)
- (docs/ evidence convention 의무화) fake canary marker + redaction wrapping (49 entry, 향후 scope 확장 시점)

**메모리 답습 의무** (다음 세션 시작 시 — 50 entry 답습):
- 세션 시작 프로토콜: `docs/CONTEXT.md` + 최신 `docs/sessions/SESSION_*.md` 읽기 (CLAUDE.md §4)
- 단계별 합의 cycle 패턴: brief → 승인 → 합의 → commit → push 6단계, 자동 다음 단계 진입 금지
- Ceremony 인플레이션 차단: 동형 cycle 중복 ceremony 회피
- Provider Liquidity 하드 요구: 헌법 5조-2 비협상
- UI/UX 작업 시 디자인 mockup 컨펌 먼저

## 변경 매트릭스

| 파일 | 변경 종류 |
|---|---|
| `docs/phase0/mvp2-entry-eligibility-audit-brief.md` | 신규 (v1, 372줄) |
| `docs/review/3plus1-consensus-2026-05-28-mvp2-entry-eligibility-audit.md` | 신규 (Reviewer-only 단축 합의 보고서, 184줄) |
| `docs/sessions/SESSION_2026-05-28.md` | 신규 (본 51번째 entry) |
| `docs/INDEX.md` | 본 51번째 entry 등록 |

## 본 51번째 entry 머신 변경 0건 (메인 권위 라인)

`src/` 0건 변경, `tools/` 0건 변경, `.github/workflows/` 0건 변경, `.pre-commit-config.yaml` 0건 변경, `.importlinter` 0건 변경, `.githooks/` 0건 변경, ADR 본문 0건 갱신 (ADR-011 / 012 / 008 / 009 / 010 모두 cross-reference 답습 한정), 헌법 0건 (T3 영역), roadmap-mvp1 본문 0건, governance-preconditions 본문 0건, provider-agnostic-memory-skill-design 본문 0건, ADR-012 본문 0건, branch protection rule 0건 (43 답습 유지, 8 contexts), MVP-1 Implementation Evidence PASS 재선언 0건 (32 entry 답습 유지), Operational Readiness PASS 0건, Hermes PMO 격상 0건, `adapters/llm/facade.py` placeholder 0건 변경, Tier-2/3 catalog 확장 0건, 외부 library 도입 결정 0건, GP-2 sub-수단 결정 0건 (R-1~R-5 후보 식별만), G4 §4.4 Layer 4 sub-수단 결정 0건 (L-1~L-5 후보 식별만), 다른 Layer 진입 결정 0건, 다른 GP 진입 결정 0건, MVP-2 진입 발효 0건. **본 cycle = audit brief 발효 한정 (메인 권위 라인 변경 0건)**.

---

## 52번째 entry — (α) MVP-2 진입 합의 entry brief 풀 3+1 + 외부 LLM 1+ (cross-vendor codex) **REVISE AS ENTRY BRIEF INPUT** → v1.1 1pass 흡수 (BLOCKING 7 + 권고 13)

> **흐름**: 51 entry commit `f7ac61d` push 후 사용자 carry-over #4 명시 "4번 (α) 진입" → 24 entry brief 구조 audit → (α) entry brief v1 작성 (480줄) → 사용자 승인 (Recommended (1) + 외부 LLM (α) Claude tmux+codex 직접 호출) → codex 호출 (`--dangerously-bypass-approvals-and-sandbox`, gpt-5.5, 3597줄 transcript) → codex 응답 분석 (REVISE AS ENTRY BRIEF INPUT, BLOCKING 3 + 권고 5 + NOTE 3) → 풀 3+1 합의 (Agent A/B/C 3 병렬 독립 동시 launch) → Agent A 응답 (APPROVE WITH CONDITIONS, 338줄, BLOCKING 2 + 권고 4, **filesystem 직접 inspection 매우 중요한 발견 3건** R-A-1/R-A-2/N-A-1) → Agent B 응답 (REVISE, 306줄, BLOCKING 2 + 권고 4 + NOTE 3) → Agent C 응답 (APPROVE WITH CONDITIONS, 374줄, BLOCKING 2 + 권고 6 + NOTE 3) → Reviewer 통합 합의 (257줄, **REVISE AS ENTRY BRIEF INPUT, BLOCKING 7 + 권고 13**, 5 source verify R-S1 CONFIRMED + Consensus 2 + Unique 5 매트릭스) → brief v1.1 1pass 흡수 (480 → 602줄, +122) → 본 정리 commit + push.

### 결과 요약 (52번째 entry)

⭐⭐⭐⭐ **(α) MVP-2 진입 합의 entry brief 풀 3+1 + 외부 LLM 1+ cycle 발효 합의 진행** — 24 entry MVP-1 1.5차 보강 entry brief 답습 동형 패턴 (큰 cycle). 본 cycle 발효 자격 = brief v1.1 commit + 본 정리 commit + push 후 본 cycle 합의 발효 (REVISE → v1.1 보강 후 APPROVE WITH CONDITIONS 격상 자격 충실).

- (α) entry brief v1 작성 (`docs/phase0/mvp2-entry-brief.md`, 480줄 → v1.1 602줄, §0~§11)
- codex 호출 + 응답 capture (`docs/external-review/2026-05-28-mvp2-entry-codex-response.md`, 3597줄 full transcript, OpenAI gpt-5.5 cross-vendor, REVISE AS ENTRY BRIEF INPUT)
- 풀 3+1 합의 3 병렬 독립 (Agent A 338줄 + Agent B 306줄 + Agent C 374줄 = 1018줄, codex 응답 + 다른 Agent 응답 참조 0건)
- Reviewer 통합 합의 (`docs/review/3plus1-consensus-2026-05-28-mvp2-entry.md`, 257줄): **REVISE AS ENTRY BRIEF INPUT, BLOCKING 7 + 권고 13** + 4 source cross-validation 매트릭스 + R-S1 CONFIRMED (5 source verify) + v1.1 보강 매트릭스
- brief v1.1 1pass 흡수 (BLOCKING 7 + 권고 13, 별도 v2 cycle 0, ceremony-inflation 차단, 24 entry 동형 패턴)

⭐⭐⭐⭐ **R-S1 CONFIRMED divergence 발효** (5 source verify): codex + Agent A + Agent B + Agent C + Reviewer 단독 verbatim verify = 5/5. **ADR-012 *자체 내부* §2.3 (4-layer numbering, Layer 4 = External anchor) vs §2.8 (5-layer numbering, Layer 4 = CI 회귀 검증, Layer 5 = External anchor) divergence** + G4 §4.4.1 = §2.8 답습 동형. 본 brief v1.1 = 권위 인용 chain 정정 한정 (G4 §4.4.1 + ADR-012 §2.8 PRIMARY, §2.3 = principle only). 다중 source 정정 (ADR-012 §2.3 본문 정정 또는 §2.8 동형 답습 cross-reference 강화) = 별도 cross-reference 정정 cycle 사용자 명시 영역 (§9.5 답습).

⭐⭐⭐ **Agent A filesystem 직접 inspection 매우 중요한 발견** (Unique 3건, 51 audit brief 답습 결함 cascade 정정 영역):
- R-A-1: `agent/` directory 본 repo 內 **부재** (실 위치 Hermes upstream HEAD v0.12.0 `/tmp/hermes-phase0/hermes-agent/agent/redact.py` 401 LOC). 51 audit brief carry-over 결함.
- R-A-2: W-A 통합 권고 vs 실 repo 기존 G4 workflow 분리 운영 (`g4-hash-chain.yml` 10652B + `history-anchor-verifier.yml` 19094B + `rewrite-defense.yml` 16454B) **충돌**
- N-A-1: `tools/jsonl_hash_chain.py` (genesis hash + 4 violation_type) + `tools/canonical_json.py` + `tests/canonical/` 24 fixtures + `g4-hash-chain.yml` **PoC 시제 이미 운영 중** → brief §2.2.2 "❌ gap" 4 row → "⚠️ PoC 시제 충족 / PASS 시제 미충족" 격상

**원칙 준수**: 실 코드 0 / CI 0 / hook 0 / branch protection 0 / config 본문 변경 0 / ADR 본문 갱신 0 / 헌법 0 / roadmap-mvp1 본문 0 / governance-preconditions 본문 0 / G4 본문 0 / ADR-012 본문 0 / MVP-1 PASS 재선언 0 / MVP-2 Implementation Evidence PASS 발효 0 / Operational Readiness PASS 0 / Hermes PMO 격상 0 / GP-2 sub-수단 결정 0 (R-1~R-5 후보 식별만) / G4 §4.4 Layer 4 sub-수단 결정 0 (L-1~L-5 후보 식별만) / threshold 고정 0 / Tier-2/3 catalog 확장 0 / 외부 library 도입 결정 0 / 다른 Layer 진입 결정 0 / 다른 GP 진입 결정 0 / `adapters/llm/facade.py` placeholder 0 변경 / Hermes upstream `agent/redact.py` 본 repo 內 import 결정 0 / ADR-012 §2.3 본문 정정 자동 진입 0 / 자동 (β)/(γ)/실 구현 진입 0 (단계별 cycle 답습) — **25/25 유지**.

### 흐름 (52번째 entry)

| 단계 | 산출 | commit |
|---|---|---|
| 51 entry commit `f7ac61d` push (3517453..f7ac61d) | (push 완료) | — |
| 사용자 carry-over #4 명시 "4번 (α) 진입" | (대화) | — |
| 24 entry brief 구조 audit (570줄 v1.1) | (read-only) | — |
| ⭐ (α) entry brief v1 작성 | `docs/phase0/mvp2-entry-brief.md` (480줄, §0~§10) | (본 정리 commit) |
| 사용자 승인 (Recommended (1) + 외부 LLM (α) Claude tmux+codex 직접 호출) | (사용자 명시) | — |
| ⭐ codex 호출 + 응답 capture (`--dangerously-bypass-approvals-and-sandbox`, gpt-5.5, background) | `docs/external-review/2026-05-28-mvp2-entry-codex-response.md` (3597줄 full transcript, REVISE AS ENTRY BRIEF INPUT, BLOCKING 3 + 권고 5 + NOTE 3) | (본 정리 commit) |
| ⭐ 풀 3+1 합의 (Agent A/B/C 3 병렬 독립 동시 launch) | Agent A 338줄 (APPROVE w/ COND, BLOCKING 2 + 권고 4, **filesystem 직접 inspection 3 unique 발견**) + Agent B 306줄 (REVISE, BLOCKING 2 + 권고 4 + NOTE 3) + Agent C 374줄 (APPROVE w/ COND, BLOCKING 2 + 권고 6 + NOTE 3) | (본 정리 commit) |
| ⭐⭐⭐ Reviewer 통합 합의 (5 source verify, R-S1 CONFIRMED 격상) | `docs/review/3plus1-consensus-2026-05-28-mvp2-entry.md` (257줄, **REVISE AS ENTRY BRIEF INPUT, BLOCKING 7 + 권고 13**, Consensus 2 + Unique 5 매트릭스, ADR-012 §2.3 vs §2.8 자체 내부 divergence verbatim 직접 read) | (본 정리 commit) |
| ⭐⭐ brief v1.1 1pass 흡수 (BLOCKING 7 + 권고 13) | brief v1 480 → v1.1 602줄 (+122, in-place 보강) + §11 v1.1 보강 매트릭스 신설 | (본 정리 commit) |
| 본 정리 commit + push | SESSION + INDEX | (본 commit) |

### carry-over (52번째 entry — 신규 + 해소)

**해소 누적 (본 entry)**:
- ✅ 51 entry carry-over #4 (α) "MVP-2 진입 합의 entry brief" (본 (α) 합의 REVISE → v1.1 commit 후 발효)

**다음 세션 진입 후보 (carry-over — 51 entry 답습 유지 + 본 entry 신규)**:

| # | 후보 | 영역 | 규모 |
|---|---|---|---|
| 1 | (b1-PC1-D6-ast-context) AST SAFE_CONTEXT 영구 정밀화 (42 entry, 50/51 entry 답습) | 별도 cycle | 풀 3+1 |
| 2 | FORCE_JAVASCRIPT_ACTIONS_TO_NODE24 사전 evidence (47 entry codex 권고 1, 50/51 entry 답습) | chore | 1-agent 직접 |
| 3 | (d) facade real (TR-1, `adapters/llm/facade.py` placeholder → real, 50/51 entry 답습) | **큰 cycle** | 풀 3+1 + 외부 LLM 1+ |
| 4 ⭐ | **(β) sub-수단 결정 cycle — GP-2 R-1/2/3/4/5 + G4 §4.4 Layer 4 L-1/2/3/4/5 + W-A/B/C/D/E** | **큰 cycle** | 풀 3+1 (수단별 차등) |
| 5 ⭐ | **(γ) 분리 영역 결정 cycle — G4 §4.4 Layer 1+2 의존 영역 우선 진입 vs Layer 4 동시 진입 ((γ-a/b/c/d) 4 대안)** | **큰 cycle** | 풀 3+1 |
| 6 ⭐ | **R-S1 cross-reference 정정 cycle** — ADR-012 §2.3 본문 정정 또는 §2.8 동형 답습 cross-reference 강화 | **별도 cycle** | 풀 3+1 + 사용자 명시 |
| 7 ⭐ | **실 구현 sub-cycle** ((β)+(γ) 후) — Hermes upstream `agent/redact.py` 영역 + 본 repo P1 facade RedactionFilter (TR-1 (d) 의존) + Layer 1 PoC → PASS 격상 + R-6 workflow 확장 step + 합의 형태 별 | **큰 cycle (다단계)** | 수단별 차등 |
| 8 ⭐ | **MVP-2 Implementation Evidence PASS 발효 합의** ((β)+(γ)+실 구현 evidence 완료 후) | **큰 cycle** (메인 권위) | 풀 3+1 + 외부 LLM 1+ + 사용자 명시 (32 entry 답습 패턴) |
| 9 | ADR 본문 cross-reference 갱신 별도 commit (ADR-008 차단조건 #1 보조 + ADR-012 §2.2 event enum amendment + ADR-011 §8.5 후속 작업 등록) | chore + 별도 합의 | 단축 또는 1-agent |
| 10 | 51 audit brief carry-over 결함 정정 (선택, B-4 답습 — `agent/redact.py` 본 repo 內 표기 framing 정정) | chore | 1-agent 직접 |
| 11 | 32 entry 프라이데이 D-1~D-8 합의 (자비스 4 invariant 영구 보존 + 5 layer 격리, 50/51 entry 답습) | **큰 cycle** | 풀 3+1 + 외부 LLM 1+ |

**자율 영역 carry-over** (PASS 효과 영향 0건 — 50/51 entry 답습 유지):
- (E-D6-2) nightly schedule 첫 발화 actual run id capture (2026-05-28 KST 12:00 이후, 48 entry)
- (b1-PC1-D6-evidence-workflow-dispatch) workflow_dispatch 수동 발화 evidence (선택)
- (b1-AR3 develop) develop branch 생성 시점 8 contexts 적용 (사용자 영역)
- (docs/ evidence convention 의무화) fake canary marker + redaction wrapping (49 entry)

**메모리 답습 의무** (다음 세션 시작 시 — 50/51 entry 답습 유지):
- 세션 시작 프로토콜: `docs/CONTEXT.md` + 최신 `docs/sessions/SESSION_*.md` 읽기 (CLAUDE.md §4)
- 단계별 합의 cycle 패턴: brief → 승인 → 합의 → commit → push 6단계, 자동 다음 단계 진입 금지
- Ceremony 인플레이션 차단: 동형 cycle 중복 ceremony 회피 (본 cycle 1pass 흡수 답습)
- Provider Liquidity 하드 요구: 헌법 5조-2 비협상
- UI/UX 작업 시 디자인 mockup 컨펌 먼저

### 변경 매트릭스 (52번째 entry)

| 파일 | 변경 종류 |
|---|---|
| `docs/phase0/mvp2-entry-brief.md` | 신규 (v1, 480줄) → in-place 보강 (v1.1, 602줄, +122) |
| `docs/external-review/2026-05-28-mvp2-entry-codex-response.md` | 신규 (codex 응답 3597줄 full transcript, OpenAI gpt-5.5 cross-vendor) |
| `docs/review/3plus1-consensus-2026-05-28-mvp2-entry-agent-a.md` | 신규 (Agent A 응답, 338줄) |
| `docs/review/3plus1-consensus-2026-05-28-mvp2-entry-agent-b.md` | 신규 (Agent B 응답, 306줄) |
| `docs/review/3plus1-consensus-2026-05-28-mvp2-entry-agent-c.md` | 신규 (Agent C 응답, 374줄) |
| `docs/review/3plus1-consensus-2026-05-28-mvp2-entry.md` | 신규 (Reviewer 통합 합의 보고서, 257줄, REVISE AS ENTRY BRIEF INPUT BLOCKING 7 + 권고 13) |
| `docs/sessions/SESSION_2026-05-28.md` | 52번째 entry 추가 |
| `docs/INDEX.md` | 52번째 entry 등록 |

### 본 52번째 entry 머신 변경 0건 (메인 권위 라인)

`src/` 0건 변경, `tools/` 0건 변경 (PoC 시제 발견은 read-only audit 한정, 본문 변경 0), `.github/workflows/` 0건 변경 (실 repo G4 workflow 발견은 read-only audit 한정), `.pre-commit-config.yaml` 0건 변경, `.importlinter` 0건 변경, `.githooks/` 0건 변경, ADR 본문 0건 갱신, 헌법 0건, roadmap-mvp1 본문 0건, governance-preconditions 본문 0건, provider-agnostic-memory-skill-design 본문 0건, ADR-012 본문 0건 (R-S1 CONFIRMED divergence 발견 = 정정 자체는 별도 cross-reference 정정 cycle 사용자 명시 영역, 본 cycle 권위 인용 chain 정정 한정), branch protection rule 0건 (43 답습 유지, 8 contexts), MVP-1 Implementation Evidence PASS 재선언 0건 (32 entry 답습 유지), MVP-2 Implementation Evidence PASS 발효 0건, Operational Readiness PASS 0건, Hermes PMO 격상 0건, `adapters/llm/facade.py` placeholder 0건 변경, Tier-2/3 catalog 확장 0건, 외부 library 도입 결정 0건, GP-2 sub-수단 결정 0건, G4 §4.4 Layer 4 sub-수단 결정 0건, 다른 Layer 진입 결정 0건, 다른 GP 진입 결정 0건, Hermes upstream `agent/redact.py` 본 repo 內 import 결정 0건, ADR-012 §2.3 본문 정정 자동 진입 0건. **본 cycle = entry brief v1 + 외부 LLM 응답 + 3 Agent + Reviewer 통합 + brief v1.1 1pass 흡수 = MVP-2 진입 합의 발효 자격 충실 (REVISE → v1.1 commit 후 APPROVE WITH CONDITIONS 격상 자격, 본 정리 commit 후 본 cycle 합의 발효)**.

---

## 53번째 entry — (γ) MVP-2 G4 §4.4 Layer 분리 영역 결정 brief 풀 3+1 + 외부 LLM 1+ (cross-vendor codex gpt-5.5) **APPROVE WITH CONDITIONS** → v1.1 1pass 흡수 (BLOCKING 8 + 권고 16)

> **흐름**: 52 entry commit `c739c53` push 후 사용자 carry-over 5번 명시 "(γ) 진입" → (γ) brief v1 작성 (482줄, 4 대안 (γ-a/b/c/d)) → 사용자 승인 + (α) Claude tmux+codex 답습 → 4 source 병렬 launch (codex + Agent A/B/C 동시) → codex 응답 (3284줄, APPROVE WITH CONDITIONS, BLOCKING 2 + 권고 6 + NOTE 5) → Agent A 응답 (312줄, APPROVE WITH CONDITIONS, BLOCKING 2 + 권고 3 + NOTE 2, **filesystem 직접 inspection 5 PoC 영역 size verify**) → Agent B 응답 (413줄, APPROVE WITH CONDITIONS, BLOCKING 4 + 권고 6 + NOTE 2) → Agent C 응답 (426줄, REVISE, BLOCKING 3 + 권고 5 + NOTE 2) → Reviewer 통합 합의 (264줄, **APPROVE WITH CONDITIONS, BLOCKING 8 + 권고 16**, 4 source cross-validation 매트릭스 + (γ-d) 모순 CONFIRMED 5 source verify + (γ-c) 1순위 + (γ-a) 2순위 + (γ-d) 비권고 consensus) → brief v1.1 1pass 흡수 (482 → 522줄, +40) → 본 정리 commit + push.

### 결과 요약 (53번째 entry)

⭐⭐⭐⭐ **(γ) MVP-2 G4 §4.4 Layer 분리 영역 결정 brief 풀 3+1 + 외부 LLM 1+ cycle 발효 합의** — 본 cycle 발효 효과 = (γ) 4 대안 평가 권고 발효 + (γ-d) 모순 risk CONFIRMED 발효 + 후속 sub-cycle 진입 자격 발효 + Rollback Trigger/Evidence 후보 채택. 수단 *결정* = 별도 cycle (Reviewer 통합 권고 ≠ 결정).

- (γ) brief v1 작성 (`docs/phase0/mvp2-gamma-layer-separation-brief.md`, 482줄 → v1.1 522줄, +40, §0~§11)
- codex 호출 + 응답 capture (`docs/external-review/2026-05-28-mvp2-gamma-codex-response.md`, 3284줄 full transcript, OpenAI gpt-5.5 cross-vendor, APPROVE WITH CONDITIONS)
- 풀 3+1 합의 3 병렬 독립 (Agent A 312줄 + Agent B 413줄 + Agent C 426줄 = 1151줄, codex 응답 + 다른 Agent 응답 참조 0건)
- Reviewer 통합 합의 (`docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md`, 264줄): **APPROVE WITH CONDITIONS, BLOCKING 8 + 권고 16** + 4 source cross-validation 매트릭스 + (γ-d) 모순 CONFIRMED 5 source verify + v1.1 보강 매트릭스

⭐⭐⭐⭐ **(γ-d) 모순 risk CONFIRMED 발효** (5 source verify: codex + Agent A + Agent B + Agent C + Reviewer 단독 verbatim verify = 5/5). Layer 4 = "Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증" (G4 §4.4.1 line 650 verbatim) → Layer 1+2 미발효 시 Layer 4 회귀 검증 *대상 부재*. (γ-d) 환원 정합화: planning-only 제한 또는 (γ-a)/(γ-c) 환원. brief v1.1 = "비권고" 표현 보존 + 모순 CONFIRMED 격상 + **Layer 4 PASS 선발효 금지 명문** (planning-only 제한).

⭐⭐⭐⭐ **4 source consensus 권고**: **(γ-c) Layer 1+2+4 동시 1순위 + (γ-a) Layer 1+2 우선 → Layer 4 후속 2순위 + (γ-b) Layer 4 단독 3순위 + (γ-d) 비권고** (codex + Agent A 일치 / Agent B (γ-c) framing 정정 답습 / Agent C R-C-3 framing fragile 경고 흡수).

⭐⭐⭐ **Agent A filesystem direct inspection 5 PoC 영역 size verify**: tools/jsonl_hash_chain.py 14038B + tools/canonical_json.py 10055B + tests/canonical 8 카테고리 (24 fixture 정량은 52 entry carry-over 한정, 본 cycle Bash 권한 거부 정직 명시) + g4-hash-chain.yml 10652B 7 step + history-anchor-verifier.yml 19094B + rewrite-defense.yml 16454B + r2-canary.yml 5476B = 4 workflow 분리 운영 답습.

**원칙 준수**: 실 코드 0 / CI 0 / hook 0 / branch protection 0 / config 본문 0 / ADR 본문 0 / 헌법 0 / roadmap 본문 0 / governance 본문 0 / G4 본문 0 / ADR-012 본문 0 / MVP-1 PASS 재선언 0 / MVP-2 Implementation Evidence PASS 발효 0 / Operational Readiness PASS 0 / Hermes PMO 격상 0 / **GP-2 sub-수단 결정 0 / G4 §4.4 Layer 4 sub-수단 결정 0 / W 통합 결정 0** ((β) 별도 cycle) / **(γ) 4 대안 中 채택 결정 0** (Reviewer 통합 권고 ≠ 결정, 별도 cycle 사용자 영역) / threshold 고정 0 / Tier-2/3 catalog 확장 0 / 외부 library 도입 결정 0 / Layer 3+5 영역 진입 결정 0 / 다른 GP 진입 결정 0 / facade.py 0 / Hermes upstream import 결정 0 / ADR-012 §2.3 본문 정정 자동 진입 0 / 자동 후속 sub-cycle 진입 0 — **27/27 유지**.

### 흐름 (53번째 entry)

| 단계 | 산출 | commit |
|---|---|---|
| 52 entry commit `c739c53` push (f7ac61d..c739c53) | (push 완료) | — |
| 사용자 carry-over 5번 명시 "(γ) 진입" | (대화) | — |
| (γ) brief v1 작성 | `docs/phase0/mvp2-gamma-layer-separation-brief.md` (482줄, §0~§10) | (본 정리 commit) |
| 사용자 승인 + (α) Claude tmux+codex 직접 호출 답습 | (사용자 명시) | — |
| ⭐ 4 source 병렬 launch 동시 (codex + Agent A/B/C) | 4 응답 파일 신규 | — |
| codex 응답 (gpt-5.5 cross-vendor) | `docs/external-review/2026-05-28-mvp2-gamma-codex-response.md` (3284줄, APPROVE WITH CONDITIONS, BLOCKING 2 + 권고 6 + NOTE 5) | (본 정리 commit) |
| Agent A (구현 분석가) — **filesystem 직접 inspection 5 PoC 영역 verify** | `docs/review/3plus1-consensus-2026-05-28-mvp2-gamma-agent-a.md` (312줄, APPROVE WITH CONDITIONS, BLOCKING 2 + 권고 3 + NOTE 2) | (본 정리 commit) |
| Agent B (안전 검증가) | `docs/review/3plus1-consensus-2026-05-28-mvp2-gamma-agent-b.md` (413줄, APPROVE WITH CONDITIONS, BLOCKING 4 + 권고 6 + NOTE 2) | (본 정리 commit) |
| Agent C (대안 탐색가) | `docs/review/3plus1-consensus-2026-05-28-mvp2-gamma-agent-c.md` (426줄, REVISE, BLOCKING 3 + 권고 5 + NOTE 2) | (본 정리 commit) |
| ⭐⭐⭐ Reviewer 통합 합의 (5 source verify, (γ-d) 모순 CONFIRMED) | `docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md` (264줄, **APPROVE WITH CONDITIONS, BLOCKING 8 + 권고 16**, 4 source cross-validation 매트릭스 + (γ-c) 1순위 + (γ-a) 2순위 + (γ-d) 비권고 consensus) | (본 정리 commit) |
| ⭐⭐ brief v1.1 1pass 흡수 (BLOCKING 8 + 권고 16) | brief v1 482 → v1.1 522줄 (+40, in-place 보강) + §11 v1.1 보강 매트릭스 신설 | (본 정리 commit) |
| 본 정리 commit + push | SESSION + INDEX | (본 commit) |

### carry-over (53번째 entry — 신규 + 해소)

**해소 누적 (본 entry)**:
- ✅ 52 entry carry-over 5번 (γ) 분리 영역 결정 cycle (본 (γ) 합의 APPROVE WITH CONDITIONS → v1.1 commit 후 발효)

**다음 세션 진입 후보 (carry-over — 52/51 entry 답습 유지 + 본 entry 신규)**:

| # | 후보 | 영역 | 규모 |
|---|---|---|---|
| 1 | (b1-PC1-D6-ast-context) AST SAFE_CONTEXT 영구 정밀화 | 별도 cycle | 풀 3+1 |
| 2 | FORCE_JAVASCRIPT_ACTIONS_TO_NODE24 사전 evidence | chore | 1-agent 직접 |
| 3 | (d) facade real (TR-1, `adapters/llm/facade.py`) | **큰 cycle** | 풀 3+1 + 외부 LLM 1+ |
| 4 ⭐ | **(γ) 4 대안 中 채택 결정 cycle** — Reviewer 통합 권고 ((γ-c) 1순위 + (γ-a) 2순위) 답습 + 사용자 명시 결정 | 별도 cycle | 풀 3+1 (작은 영역) |
| 5 ⭐ | **(β) sub-수단 결정 cycle** — R-1~R-5 + L-1~L-5 + W-A~E | **큰 cycle** | 풀 3+1 (수단별 차등) |
| 6 ⭐ | **Layer 1+2+4 통합 PASS 격상 cycle** ((γ-c) 채택 시) 또는 **Layer 1+2 PASS 격상 + Layer 4 PASS 격상 단계적** ((γ-a) 채택 시) | **큰 cycle** | 풀 3+1 + 외부 LLM 1+ |
| 7 ⭐ | **(γ-e/f/g) hybrid 대안 결정 cycle** (B-8 답습) — (γ-e) (γ-a)+(γ-d) hybrid / (γ-f) PoC 시제 보존 / (γ-g) 시점 vs evidence 분리 | 별도 cycle | 풀 3+1 (선택) |
| 8 ⭐ | **R-S1 cross-reference 정정 cycle** (ADR-012 §2.3 vs §2.8) | 별도 cycle | 풀 3+1 + 사용자 명시 |
| 9 ⭐ | **실 구현 sub-cycle** ((β)+(γ) 후) | **큰 cycle (다단계)** | 수단별 차등 |
| 10 ⭐ | **MVP-2 Implementation Evidence PASS 발효 합의** ((β)+(γ)+실 구현 evidence 완료 + RT-γ-6 R-S1 PASS 시점 선행/동시 정정 평가 후) | **큰 cycle** (메인 권위) | 풀 3+1 + 외부 LLM 1+ + 사용자 명시 (32 entry 답습) |
| 11 | ADR 본문 cross-reference 갱신 별도 commit | chore + 별도 합의 | 단축 또는 1-agent |
| 12 | 51 audit brief carry-over 결함 정정 (B-4 답습) | chore | 1-agent 직접 |
| 13 | 32 entry 프라이데이 D-1~D-8 합의 | **큰 cycle** | 풀 3+1 + 외부 LLM 1+ |

**자율 영역 carry-over** (PASS 효과 영향 0건 — 50/51/52 entry 답습 유지):
- (E-D6-2) nightly schedule 첫 발화 actual run id capture (48 entry)
- (b1-PC1-D6-evidence-workflow-dispatch) workflow_dispatch 수동 발화 evidence
- (b1-AR3 develop) develop branch 생성 시점 8 contexts 적용
- (docs/ evidence convention 의무화) fake canary marker + redaction wrapping (49 entry)

**메모리 답습 의무** (다음 세션 시작 시):
- 세션 시작 프로토콜
- 단계별 합의 cycle 패턴 (자동 진입 0)
- Ceremony 인플레이션 차단
- Provider Liquidity 하드 요구
- UI/UX 디자인 mockup 컨펌 먼저

### 변경 매트릭스 (53번째 entry)

| 파일 | 변경 종류 |
|---|---|
| `docs/phase0/mvp2-gamma-layer-separation-brief.md` | 신규 (v1, 482줄) → in-place 보강 (v1.1, 522줄, +40) |
| `docs/external-review/2026-05-28-mvp2-gamma-codex-response.md` | 신규 (codex 응답 3284줄 full transcript, OpenAI gpt-5.5 cross-vendor) |
| `docs/review/3plus1-consensus-2026-05-28-mvp2-gamma-agent-a.md` | 신규 (Agent A 응답, 312줄, filesystem direct inspection) |
| `docs/review/3plus1-consensus-2026-05-28-mvp2-gamma-agent-b.md` | 신규 (Agent B 응답, 413줄) |
| `docs/review/3plus1-consensus-2026-05-28-mvp2-gamma-agent-c.md` | 신규 (Agent C 응답, 426줄) |
| `docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md` | 신규 (Reviewer 통합 합의, 264줄, APPROVE WITH CONDITIONS BLOCKING 8 + 권고 16) |
| `docs/sessions/SESSION_2026-05-28.md` | 53번째 entry 추가 |
| `docs/INDEX.md` | 53번째 entry 등록 |

### 본 53번째 entry 머신 변경 0건 (메인 권위 라인)

`src/` 0 / `tools/` 0 (PoC 시제 발견 read-only audit + filesystem size inspection 한정, 본문 변경 0) / `.github/workflows/` 0 (4 workflow 분리 운영 발견 read-only) / `tests/canonical/` 0 (24 fixture 정량 carry-over 정직 명시, 본문 변경 0) / `.pre-commit-config.yaml` 0 / `.importlinter` 0 / `.githooks/` 0 / ADR 본문 0 / 헌법 0 / roadmap-mvp1 본문 0 / governance 본문 0 / G4 본문 0 / ADR-012 본문 0 (R-S1 CONFIRMED + (γ-d) 모순 CONFIRMED 발견 = 정정 자체는 별도 cycle 사용자 명시 영역) / branch protection rule 0 (43 답습 유지 8 contexts) / MVP-1 PASS 재선언 0 / MVP-2 Implementation Evidence PASS 발효 0 / Operational Readiness PASS 0 / Hermes PMO 격상 0 / GP-2 sub-수단 결정 0 / G4 §4.4 Layer 4 sub-수단 결정 0 / W 통합 결정 0 / **(γ) 4 대안 中 채택 결정 0** (Reviewer 통합 권고 한정) / threshold 고정 0 / Tier-2/3 catalog 확장 0 / 외부 library 도입 결정 0 / Layer 3+5 영역 진입 결정 0 / 다른 GP 진입 결정 0 / facade.py 0 / Hermes upstream import 결정 0 / ADR-012 §2.3 본문 정정 자동 진입 0 / 자동 후속 sub-cycle 진입 0. **본 cycle = (γ) brief v1 + 4 source 풀 3+1 합의 + brief v1.1 1pass 흡수 = (γ) 4 대안 평가 권고 발효 + (γ-d) 모순 CONFIRMED 발효 자격 충실 (APPROVE WITH CONDITIONS → v1.1 commit 후 본 cycle 합의 발효)**.

---

## 54번째 entry — (γ-c) Layer 1+2+4 동시 채택 결정 발효 (1-agent 직접 합의, 53 entry Reviewer 통합 권고 답습 한정)

> **흐름**: 53 entry commit `f5cf584` push 후 사용자 carry-over 4번 명시 "(γ) 채택 결정" → 사용자 명시 (γ-c) Recommended + 1-agent 직접 (X) → decision brief v1 작성 (241줄) → 사용자 승인 → 1-agent 직접 합의 보고서 작성 (181줄, 5/5 풀 3+1 승격 trigger 0/7 발화 자체 검증 + 53 entry Reviewer 통합 권고 답습 9/9 cross-check) → 본 정리 commit + push.

### 결과 요약 (54번째 entry)

⭐⭐⭐ **(γ-c) Layer 1+2+4 동시 채택 결정 발효** — 53 entry Reviewer 통합 권고 답습 한정 (4 source consensus 1순위) + 1-agent 직접 합의 (작은 영역, ceremony-inflation 차단). (γ-a/b/d) = 비채택, 재평가 = 별도 cycle 사용자 명시 영구 보존.

- decision brief v1 작성 (`docs/phase0/mvp2-gamma-decision-brief.md`, 241줄, §0~§7): (γ-c) 채택 결정 발효 정당성 + (γ-c) 특화 의무 4 + 5/5 trigger 0/7 자체 검증
- 1-agent 직접 합의 보고서 작성 (`docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md`, 181줄, APPROVE): 0/7 trigger 발화 + 53 entry 답습 5/5 cross-check + 9/9 verbatim 모순 0건 + 메타 편향 자기진단 M-1~M-7

⭐⭐ **(γ-c) 특화 의무 4 영구 유지 발효**:
1. PASS evidence template Layer 1/Layer 2/Layer 4 subsection 강제 (53 entry N-1 답습)
2. "defense-in-depth 부분 답습" framing 영구 유지 (Layer 3+5 = scope 외, 53 entry B-6 답습)
3. Layer 1+2+4 통합 PASS evidence 동시 발효
4. RT-γ-6 R-S1 PASS 시점 선행/동시 정정 평가 의무 답습

⭐⭐ **(γ-d) 비권고 + Layer 4 PASS 선발효 금지 명문 답습 보존** (53 entry §2.4.5 + B-1 답습).

**원칙 준수**: 실 코드 0 / CI 0 / hook 0 / branch protection 0 / config 본문 0 / ADR 본문 0 / 헌법 0 / roadmap 본문 0 / governance 본문 0 / G4 본문 0 / ADR-012 본문 0 / MVP-1 PASS 재선언 0 / MVP-2 Implementation Evidence PASS 발효 0 / Operational Readiness PASS 0 / Hermes PMO 격상 0 / GP-2 sub-수단 결정 0 / G4 §4.4 Layer 4 sub-수단 결정 0 / W 통합 결정 0 / Layer 3+5 영역 진입 결정 0 / 다른 GP 진입 결정 0 / threshold 고정 0 / Tier-2/3 catalog 확장 0 / 외부 library 도입 결정 0 / facade.py 0 / Hermes upstream import 결정 0 / ADR-012 §2.3 본문 정정 자동 진입 0 / Layer 1+2+4 통합 PASS 격상 sub-cycle 자동 진입 0 / (β) sub-수단 결정 cycle 자동 진입 0 / (γ-a/b/d) 대안 재평가 자동 진입 0 / (γ-e/f/g) hybrid 대안 결정 자동 진입 0 / Layer 4 PASS 선발효 (영구 금지) — **29/29 유지**.

### 흐름 (54번째 entry)

| 단계 | 산출 | commit |
|---|---|---|
| 53 entry commit `f5cf584` push (c739c53..f5cf584) | (push 완료) | — |
| 사용자 carry-over 4번 명시 "(γ) 채택 결정" | (대화) | — |
| 사용자 명시 (γ-c) Recommended + (X) 1-agent 직접 답습 | (AskUserQuestion) | — |
| decision brief v1 작성 | `docs/phase0/mvp2-gamma-decision-brief.md` (241줄) | (본 정리 commit) |
| 사용자 승인 | (AskUserQuestion (1) Recommended) | — |
| ⭐ 1-agent 직접 합의 보고서 작성 (0/7 trigger 자체 검증 + 53 entry 답습 5/5 + 9/9 verbatim) | `docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md` (181줄, APPROVE) | (본 정리 commit) |
| 본 정리 commit + push | SESSION + INDEX | (본 commit) |

### carry-over (54번째 entry — 신규 + 해소)

**해소 누적 (본 entry)**:
- ✅ 53 entry carry-over 4번 (γ) 채택 결정 cycle — (γ-c) Layer 1+2+4 동시 채택 결정 발효

**다음 세션 진입 후보 (carry-over — 53/52/51 entry 답습 유지 + 본 entry 신규/갱신)**:

| # | 후보 | 영역 | 규모 |
|---|---|---|---|
| 1 | (b1-PC1-D6-ast-context) AST SAFE_CONTEXT 영구 정밀화 | 별도 cycle | 풀 3+1 |
| 2 | FORCE_JAVASCRIPT_ACTIONS_TO_NODE24 사전 evidence | chore | 1-agent 직접 |
| 3 | (d) facade real (TR-1) | **큰 cycle** | 풀 3+1 + 외부 LLM 1+ |
| 4 ⭐ | **(β) sub-수단 결정 cycle** — R-1~R-5 + L-1~L-5 + W-A~E (수단별 차등) | **큰 cycle** | 풀 3+1 |
| 5 ⭐ | **Layer 1+2+4 통합 PASS 격상 cycle** (γ-c 채택 발효 답습) — Layer subsection 강제 + "부분 답습" framing 영구 + RT-γ-6 답습 | **큰 cycle** | 풀 3+1 + 외부 LLM 1+ |
| 6 ⭐ | **실 구현 sub-cycle** ((β) + Layer 통합 PASS 격상 후) — Hermes upstream + facade + PoC → PASS + R-6 확장 (Layer 2a denyNonFastForwards 활성화 evidence 별도 verify 의무) | **큰 cycle (다단계)** | 수단별 차등 |
| 7 ⭐ | **MVP-2 Implementation Evidence PASS 발효 합의** — RT-γ-6 R-S1 PASS 시점 선행/동시 정정 평가 답습 | **큰 cycle** (메인 권위) | 풀 3+1 + 외부 LLM 1+ + 사용자 명시 (32 entry 답습) |
| 8 | (γ-e/f/g) hybrid 대안 결정 cycle (선택) | 별도 cycle | 풀 3+1 |
| 9 | R-S1 cross-reference 정정 cycle (ADR-012 §2.3 vs §2.8) | 별도 cycle | 풀 3+1 + 사용자 명시 |
| 10 | ADR 본문 cross-reference 갱신 별도 commit | chore + 별도 합의 | 단축 또는 1-agent |
| 11 | 51 audit brief carry-over 결함 정정 (B-4 답습) | chore | 1-agent 직접 |
| 12 | 32 entry 프라이데이 D-1~D-8 합의 | **큰 cycle** | 풀 3+1 + 외부 LLM 1+ |

### 변경 매트릭스 (54번째 entry)

| 파일 | 변경 종류 |
|---|---|
| `docs/phase0/mvp2-gamma-decision-brief.md` | 신규 (v1, 241줄) |
| `docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md` | 신규 (1-agent 직접 합의 보고서, 181줄, APPROVE) |
| `docs/sessions/SESSION_2026-05-28.md` | 54번째 entry 추가 |
| `docs/INDEX.md` | 54번째 entry 등록 |

### 본 54번째 entry 머신 변경 0건 (메인 권위 라인)

`src/` 0 / `tools/` 0 / `tests/canonical/` 0 / `.github/workflows/` 0 / `.pre-commit-config.yaml` 0 / `.importlinter` 0 / `.githooks/` 0 / ADR 본문 0 / 헌법 0 / roadmap 본문 0 / governance 본문 0 / G4 본문 0 / ADR-012 본문 0 / branch protection rule 0 (43 답습 유지) / MVP-1 PASS 재선언 0 / MVP-2 Implementation Evidence PASS 발효 0 / Operational Readiness PASS 0 / Hermes PMO 격상 0 / GP-2 sub-수단 결정 0 / G4 §4.4 Layer 4 sub-수단 결정 0 / W 통합 결정 0 / Layer 3+5 영역 진입 결정 0 / threshold 고정 0 / Tier-2/3 catalog 확장 0 / 외부 library 도입 결정 0 / facade.py 0 / Hermes upstream import 결정 0 / ADR-012 §2.3 본문 정정 자동 진입 0 / **Layer 1+2+4 통합 PASS 격상 sub-cycle 자동 진입 0** / **(β) sub-수단 결정 cycle 자동 진입 0** / **(γ-a/b/d) 대안 재평가 자동 진입 0** / (γ-e/f/g) hybrid 대안 결정 자동 진입 0 / **Layer 4 PASS 선발효 영구 금지 답습 보존**. **본 cycle = decision brief + 1-agent 직접 합의 = (γ-c) Layer 1+2+4 동시 채택 결정 발효 + (γ-c) 특화 의무 4 영구 유지 발효**.

---

## 55번째 entry — Layer 1+2+4 통합 PASS 격상 entry brief 풀 3+1 + 외부 LLM 1+ (cross-vendor codex gpt-5.5) **APPROVE WITH CONDITIONS** → v1.1 1pass 흡수 (BLOCKING 9 + 권고 18, 4 source 전원 APPROVE WITH CONDITIONS)

> **흐름**: 54 entry commit `895a77b` push 후 사용자 carry-over 5번 명시 "Layer 1+2+4 통합 PASS 격상 진입" → audit (read-only, PoC 시제 현 상태 + denyNonFastForwards 미설정 발견) → 사용자 scope 명시 (a) entry brief → entry brief v1 작성 (443줄) → 사용자 승인 + (E-α) codex 답습 → 4 source 병렬 launch (codex + Agent A/B/C) → codex 응답 (3340줄, APPROVE WITH CONDITIONS, **실 venv 실행 + gh api direct query verify**) → Agent A 응답 (304줄, APPROVE WITH CONDITIONS, filesystem direct) → Agent B 응답 (425줄, APPROVE WITH CONDITIONS) → Agent C 응답 (348줄, APPROVE WITH CONDITIONS) → Reviewer 통합 합의 (213줄, **APPROVE WITH CONDITIONS, BLOCKING 9 + 권고 18**, 4 source 전원 APPROVE WITH CONDITIONS consensus) → brief v1.1 1pass 흡수 (443 → 533줄, +90) → 본 정리 commit + push.

### 결과 요약 (55번째 entry)

⭐⭐⭐⭐ **Layer 1+2+4 통합 PASS 격상 entry brief 풀 3+1 + 외부 LLM 1+ cycle 발효 합의** — (γ-c) 채택 발효 답습 한정 (24/52 entry entry brief 답습 동형 큰 cycle). 본 cycle 발효 효과 = Layer 1+2+4 통합 PASS 격상 *진입 권한* 발효 + 후속 실 구현 sub-cycle 진입 자격 발효 (조건부 승인 조건 6 우선). PASS *발효* = 별도 합의.

- entry brief v1 작성 (`docs/phase0/mvp2-layer-124-pass-entry-brief.md`, 443줄 → v1.1 533줄, +90, §0~§11)
- codex 호출 + 응답 capture (`docs/external-review/2026-05-28-mvp2-layer-124-pass-codex-response.md`, 3340줄 full transcript, OpenAI gpt-5.5 cross-vendor, APPROVE WITH CONDITIONS + 조건부 승인 조건 6)
- 풀 3+1 합의 3 병렬 독립 (Agent A 304줄 + Agent B 425줄 + Agent C 348줄 = 1077줄, 모두 APPROVE WITH CONDITIONS)
- Reviewer 통합 합의 (`docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass.md`, 213줄): **APPROVE WITH CONDITIONS, BLOCKING 9 (Consensus 4 + Unique 5) + 권고 18** + 4 source cross-validation 매트릭스

⭐⭐⭐⭐ **4 source 전원 APPROVE WITH CONDITIONS strong consensus** (codex + Agent A + Agent B + Agent C). codex 실 venv 실행 (`tools/jsonl_hash_chain.py` pass/fail fixtures + `tools/canonical_json.py --mode cross_check` 전체 PASS) + `gh api` direct query branch protection 8 contexts verify.

⭐⭐⭐ **52 entry Agent A R-A-2 carry-over 해소** (tests/canonical 72 files / 8 카테고리 × 3 case × 3 file = 24 input fixtures) — codex + Agent A + Agent B 3 source filesystem direct cross-confirm.

⭐⭐⭐ **Consensus 발견 (cross-confirm)**:
- HISTORY_REWRITE enum fixture 미커버 (g4-hash-chain.yml = Layer 1 3종 + schema 1종, HISTORY_REWRITE = rewrite-defense.yml + history-anchor-verifier.yml Layer 2 분담) — codex N-1 + Agent A R-A-1
- history-anchor-verifier.yml = Layer 5 External anchor PoC 시제 19094B 이미 운영 ("부분 답습" = 결정 영역 진입 0, PoC 시제 0 아님) — codex N-8 + Agent A R-A-3
- denyNonFastForwards local+global+system 3/3 미설정 CONFIRMED — codex + Agent A + Agent B
- RT-PASS-2/3 계산적 sensor 우선 (grep/lint) — Agent B R-B-2 + Agent C N-C-2

⭐⭐ **조건부 승인 조건 6** (실 구현 sub-cycle 우선 처리): denyNonFastForwards 활성화 + R-6 actual run + 4 G4 workflow actual run + R-S1 정정 평가 + violation_type 정밀화 + Layer subsection 분리.

⭐⭐ **R-S1 RT-γ-6 = entry 단계 PASS / MVP-2 PASS 전 hard gate** (3 옵션: ADR-012 §2.3 정정 / §2.8 강화 / 권위 선언). B-8 흡수 — "선행/동시 *의무*" → "*평가* 의무" framing 정정 (MVP-2 PASS 합의 R-S1 종속 회피).

**원칙 준수**: 실 코드 0 / CI 0 / hook 0 / branch protection 0 / config 본문 0 / ADR 본문 0 / 헌법 0 / roadmap 본문 0 / governance 본문 0 / G4 본문 0 / ADR-012 본문 0 / MVP-1 PASS 재선언 0 / **Layer 1+2+4 통합 PASS 발효 0** / MVP-2 Implementation Evidence PASS 발효 0 / Operational Readiness PASS 0 / Hermes PMO 격상 0 / **denyNonFastForwards 활성화 0** / **R-6 actual run 0** / GP-2 sub-수단 결정 0 / G4 Layer 4 sub-수단 결정 0 / W 통합 결정 0 / Layer 3+5 영역 진입 결정 0 / (γ-a/b/d) 재평가 0 / threshold 고정 0 / Tier-2/3 catalog 확장 0 / 외부 library 도입 결정 0 / facade.py 0 / Hermes upstream import 결정 0 / R-S1 cross-reference 정정 0 / 자동 후속 sub-cycle 진입 0 — **30/30 유지**.

### 흐름 (55번째 entry)

| 단계 | 산출 | commit |
|---|---|---|

exec
/bin/bash -lc "sed -n '1,240p' docs/decisions/ADR-011-means-vs-ends-redaction.md" in /home/delangi/문서/project/category/AI_development_tool
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

- 헌법 제8조 본질 충족이 specific 수단에 종속되지 않음 → 미래 Hermes API 변경 / upstream 변경 시에도 본질 보존 경로 확보
- G1a/G1b 분리로 R-2 PASS evidence가 P2 v3에 직접 흡수 가능
- "Hermes ≠ root of trust" ADR 권위화 → prequel 폐기 후에도 운영 원칙 영구 보존
- R-4~R-7이 권위 근거 명확화 → 후속 작업 의사결정 비용 감소
- 자동 학습/자동 정책 분리(T1/T2/T3)의 ADR 권위화 → silent 깨짐 자동 차단의 권위 근거

### 7.2 부정적

- ADR-008 부록 A R1의 표면 텍스트와 본 ADR §2.1 사이 텍스트 차이 존재 (Amendment로 동시 갱신하여 완화)
- "수단/목적 분리"가 일반화되어 미래 다른 비협상 조항 해석에도 적용 시 합의 비용 발생 가능 (대체 수단 검증 부담 — 의도된 비용)
- (a)~(d) 4조건 검증 부담은 본 ADR이 의도하는 안전 비용 — 회피 시도는 본 ADR 위반

### 7.3 주의사항

- 본 ADR의 (a)~(d) 4조건 미충족 시 수단 대체 불가 — "동등 이상의 보장" 검증을 PoC로 실증하지 않은 채 텍스트 해석만으로 수단 변경 금지
- §2.4 자동 정책 변경 금지(T3) 위반 감지 시 Layer 1~2 hook(설정 파일 변경 감지)에서 차단 — CI/nightly 강제 (R-6 범위)
- **본 ADR은 Hermes 안전성을 선언하지 않는다** — Hermes는 검증 대상이며, 본 ADR은 검증 외부화의 권위 근거이다.
- ADR-009 (자체 Adapter v2.0 entry) / ADR-010 (SQLCipher Vault) 도 미래 본 ADR §2.1 (a)~(d) 4조건 적용 대상이 될 수 있음 — 적용 시점은 별도 합의로 결정

---

exec
/bin/bash -lc "sed -n '150,330p' docs/decisions/ADR-012-evidence-ledger-protection.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
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

| Tier | 정체성 | PASS 조건 |
|-----|------|------|
| **Genesis (신규 chain)** | 첫 entry 작성 | (round-trip 무관) |
| **T2 (Skill/Memory promoted, 로컬)** | 로컬 promotion 절차 | **hash 일치 STRICT** — 손실 0건. 위반 시 BLOCK + `event: roundtrip_fail` |
| **T3 (Cross-vendor migration)** | 외부 형식 변환 + 재import | 의미 보존 허용 — (i) 손실 영역 자동 enumeration / (ii) `event: roundtrip_lossy` 의무 / (iii) 사용자 명시 review + ADR-011 §2.4 사용자 승인 / (iv) 정책/권한/증거 손실 BLOCK |

**Ledger entry 3 형식**:

```jsonl
{"type":"meta","scope":"<scope>","event":"roundtrip_pass","content":{"source_chain":"<id>","target_provider":"openai","hash_match":true},...}
{"type":"meta","scope":"<scope>","event":"roundtrip_lossy","content":{"source_chain":"<id>","target_provider":"openai","lost_fields":["evidence_refs.confidence_score"],"semantic_diff":"<user-review-summary>"},...}
{"type":"meta","scope":"<scope>","event":"roundtrip_fail","content":{"source_chain":"<id>","target_provider":"openai","failure_reason":"chain_violation_detected|policy_loss|permission_loss|evidence_loss"},...}
```

**자동화 vs 사용자 review 분리**:
- `lost_fields` enumeration = 자동 (canonical JSON diff)
- `semantic_diff` 판단 = 사용자 명시 review (ADR-011 §2.4 T2/T3 사용자 승인)
- **의미 보존 review 자동화 절대 금지** (Agent A R-4)

### 2.10 JSONL Export / Import 무결성

**Export** (Hermes 의존 0 — ADR-008 차단조건 #2 답습):
- `scripts/hermes-migration/` 변환 스크립트 = `import hermes_agent` 0건 (depcruise 검증, G2 GP-5 답습)
- 표준 도구 (`jq` + `sha256sum`) 만으로 검증 가능
- 외부 오케스트레이터 (claude / openai / gemini / local) 최소 2+ 재해석 가능

**Import 의무 검증** (외부 LLM 2 C-11):
1. `schema_version` 필드 존재 확인 (없으면 BLOCK)
2. 호환성 매트릭스 조회 — 현 MVP 0.1 only, 외부 형식 매핑은 별도 (Implementation 영역)
3. 미일치 시 BLOCK + 사용자 명시 manual approval 요구
4. Hash chain 검증 (§2.7 답습)

**Migration 검증 실패 = `event: migration_failed`** (Agent A 권고 + 합의 §4.3):
1. BLOCK
2. 원본 보존
3. 새 `event: migration_failed` entry append:
   ```jsonl
   {"type":"meta","scope":"<scope>","event":"migration_failed","content":{"source_provider":"hermes","target_provider":"openai","failure_step":"export|conversion|import|reverify","error_summary":"..."},...}
   ```
4. 사용자 명시 manual review 의무
5. 자동 revert 금지

### 2.11 Evidence Forgery 방지 (P10 정식 등록 트리거)

**P10 정식 등록 트리거** = 본 ADR-012 발행 시점 (G2 §1.2.5.2 답습).

**G2 §1.2 본문 P10 row 추가는 별도 G2 update PR** (본 ADR 범위 외 — 합의 §4.2):
- 사용자 명시 결정 답습 — PR-2 = ADR-012 + G4 §4.4/§4.6 한정
- G2 본문 변경 = T3 변경 + 별도 합의 (단축 가능)

exec
/bin/bash -lc "nl -ba tools/jsonl_hash_chain.py | sed -n '1,280p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	#!/usr/bin/env python3
     2	"""JSONL ledger hash chain validator — Group C PoC (G4 통합).
     3	
     4	답습 출처:
     5	  - docs/decisions/ADR-012-evidence-ledger-protection.md §2.2 (event 11번째 필드 17 enum) /
     6	    §2.3 (Append-only + Hash Chain Layer 1) / §2.6 (Genesis Hash MVP) /
     7	    §2.7 (prev_hash 검증 실패 BLOCK + manual + violation entry)
     8	  - docs/architecture/provider-agnostic-memory-skill-design.md §4.2 (11 필드) / §4.4 (hash chain)
     9	  - docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md §2 / §4.2
    10	  - tools/canonical_json.py (Q1 합의 답습 — rfc8785 + jcs 병렬 cross-check)
    11	
    12	핵심 강제 조건:
    13	  - 11 필드 schema (type / scope / id / schema_version / ts / agent / event / content / evidence_refs / prev_hash / hash)
    14	  - schema_version != "0.1" → BLOCK (ADR-012 §2.10 답습)
    15	  - Genesis hash = sha256("genesis:<scope>:<schema_version>") (ADR-012 §2.6 MVP)
    16	  - hash 계산 = sha256(canonical_json(entry - "hash" field))
    17	  - prev_hash 검증 실패 = BLOCK + chain_violation_detected entry 자동 작성
    18	  - violation_type 3종 (Layer 1): prev_hash_mismatch / hash_recalculation / genesis_mismatch
    19	    (history rewrite = Layer 2 history_anchor_verifier — 외부 anchor 비교 의무)
    20	  - timestamp monotonicity: 본 entry ts >= prev_hash entry ts (ADR-012 §3.4)
    21	  - T3 자동 정책 변경 금지 (ADR-011 §2.4) — 자동 revert 0건, BLOCK + manual
    22	
    23	종료 코드:
    24	  0 = 모든 검사 PASS
    25	  1 = 1+ violation 검출
    26	  2 = invalid input (parse 실패 등)
    27	"""
    28	from __future__ import annotations
    29	
    30	import argparse
    31	import dataclasses
    32	import datetime as dt
    33	import hashlib
    34	import json
    35	import sys
    36	from dataclasses import dataclass
    37	from enum import Enum
    38	from pathlib import Path
    39	from typing import Any
    40	
    41	from canonical_json import (  # type: ignore[import-not-found]
    42	    CanonicalizationError,
    43	    CrossCheckMode,
    44	    to_canonical,
    45	)
    46	
    47	REQUIRED_FIELDS: tuple[str, ...] = (
    48	    "type",
    49	    "scope",
    50	    "id",
    51	    "schema_version",
    52	    "ts",
    53	    "agent",
    54	    "event",
    55	    "content",
    56	    "evidence_refs",
    57	    "prev_hash",
    58	    "hash",
    59	)
    60	
    61	ALLOWED_TYPES: tuple[str, ...] = ("memory", "skill", "meta")
    62	ALLOWED_SCOPES: tuple[str, ...] = ("global", "project", "session")
    63	ALLOWED_AGENTS: tuple[str, ...] = ("user", "claude-code", "hermes", "external_llm")
    64	SUPPORTED_SCHEMA_VERSION: str = "0.1"
    65	
    66	
    67	class ViolationType(str, Enum):
    68	    """Layer 1 (hash chain) chain violation 3종 (ADR-012 §2.7 답습).
    69	
    70	    history rewrite 는 외부 anchor / base branch 비교 의무이므로 Layer 1 에서
    71	    검출 불가 — Layer 2 (history_anchor_verifier.py + rewrite_defense_check.py)
    72	    영역 (57 entry (β) sub-수단 결정 + 55 entry consensus B-1 답습).
    73	    """
    74	
    75	    PREV_HASH_MISMATCH = "prev_hash_mismatch"
    76	    HASH_RECALCULATION = "hash_recalculation"
    77	    GENESIS_MISMATCH = "genesis_mismatch"
    78	
    79	
    80	@dataclass
    81	class Violation:
    82	    """Single violation report."""
    83	
    84	    entry_index: int
    85	    entry_id: str
    86	    violation_type: str  # ViolationType.value or "schema_*" / "monotonicity_*"
    87	    detail: str
    88	
    89	
    90	def compute_genesis_hash(scope: str, schema_version: str) -> str:
    91	    """Genesis hash MVP — sha256("genesis:<scope>:<schema_version>") (ADR-012 §2.6).
    92	
    93	    schema_version 0.2 이상 진입 시 별도 chain (별도 chain_id 또는 schema_version) — 별도 합의 영역.
    94	    """
    95	    return hashlib.sha256(f"genesis:{scope}:{schema_version}".encode("utf-8")).hexdigest()
    96	
    97	
    98	def compute_entry_hash(entry: dict[str, Any]) -> str:
    99	    """Entry hash = sha256(canonical_json(entry - "hash" field)).
   100	
   101	    Q1 합의 답습 — runtime mode = PRIMARY_1_ONLY (rfc8785 단독), corpus 시점 cross-check 별도.
   102	    """
   103	    payload = {k: v for k, v in entry.items() if k != "hash"}
   104	    result = to_canonical(payload, mode=CrossCheckMode.PRIMARY_1_ONLY)
   105	    return result.sha256_hex
   106	
   107	
   108	def parse_iso8601(s: str) -> dt.datetime:
   109	    """ISO 8601 timestamp parse — 'Z' suffix 정규화."""
   110	    if s.endswith("Z"):
   111	        s = s[:-1] + "+00:00"
   112	    return dt.datetime.fromisoformat(s)
   113	
   114	
   115	def validate_schema(entry: dict[str, Any], index: int) -> list[Violation]:
   116	    """11 필드 schema validation."""
   117	    vios: list[Violation] = []
   118	    entry_id = str(entry.get("id", f"<index={index}>"))
   119	
   120	    missing = [f for f in REQUIRED_FIELDS if f not in entry]
   121	    if missing:
   122	        vios.append(
   123	            Violation(
   124	                entry_index=index,
   125	                entry_id=entry_id,
   126	                violation_type="schema_missing_field",
   127	                detail=f"missing required fields: {missing}",
   128	            )
   129	        )
   130	        return vios
   131	
   132	    if entry["type"] not in ALLOWED_TYPES:
   133	        vios.append(
   134	            Violation(index, entry_id, "schema_invalid_type", f"type={entry['type']!r} not in {ALLOWED_TYPES}")
   135	        )
   136	    if entry["scope"] not in ALLOWED_SCOPES:
   137	        vios.append(
   138	            Violation(index, entry_id, "schema_invalid_scope", f"scope={entry['scope']!r} not in {ALLOWED_SCOPES}")
   139	        )
   140	    if entry["agent"] not in ALLOWED_AGENTS:
   141	        vios.append(
   142	            Violation(index, entry_id, "schema_invalid_agent", f"agent={entry['agent']!r} not in {ALLOWED_AGENTS}")
   143	        )
   144	    if entry["schema_version"] != SUPPORTED_SCHEMA_VERSION:
   145	        vios.append(
   146	            Violation(
   147	                index,
   148	                entry_id,
   149	                "schema_version_unsupported",
   150	                f"schema_version={entry['schema_version']!r} != {SUPPORTED_SCHEMA_VERSION!r} (ADR-012 §2.10)",
   151	            )
   152	        )
   153	    if not isinstance(entry["evidence_refs"], list):
   154	        vios.append(
   155	            Violation(index, entry_id, "schema_invalid_evidence_refs", "evidence_refs must be list")
   156	        )
   157	    if not isinstance(entry["content"], (dict, list, str, int, float, bool)) and entry["content"] is not None:
   158	        vios.append(
   159	            Violation(index, entry_id, "schema_invalid_content", "content must be JSON-serializable")
   160	        )
   161	
   162	    try:
   163	        parse_iso8601(entry["ts"])
   164	    except (ValueError, TypeError) as e:
   165	        vios.append(Violation(index, entry_id, "schema_invalid_ts", f"ts parse error: {e}"))
   166	
   167	    return vios
   168	
   169	
   170	def validate_chain(entries: list[dict[str, Any]]) -> list[Violation]:
   171	    """Genesis + prev_hash ↔ hash chain + timestamp monotonicity 검증."""
   172	    vios: list[Violation] = []
   173	    if not entries:
   174	        return vios
   175	
   176	    prev_ts: dt.datetime | None = None
   177	    prev_hash_actual: str | None = None
   178	
   179	    for i, entry in enumerate(entries):
   180	        entry_id = str(entry.get("id", f"<index={i}>"))
   181	
   182	        # Hash recalculation 검증
   183	        try:
   184	            recomputed = compute_entry_hash(entry)
   185	        except CanonicalizationError as e:
   186	            vios.append(
   187	                Violation(i, entry_id, "schema_canonical_error", f"canonical_json failed: {e}")
   188	            )
   189	            continue
   190	
   191	        if recomputed != entry.get("hash"):
   192	            vios.append(
   193	                Violation(
   194	                    i,
   195	                    entry_id,
   196	                    ViolationType.HASH_RECALCULATION.value,
   197	                    f"hash field={entry.get('hash')!r} != recomputed={recomputed!r}",
   198	                )
   199	            )
   200	
   201	        # prev_hash 검증
   202	        if i == 0:
   203	            expected_genesis = compute_genesis_hash(entry["scope"], entry["schema_version"])
   204	            if entry["prev_hash"] != expected_genesis:
   205	                vios.append(
   206	                    Violation(
   207	                        i,
   208	                        entry_id,
   209	                        ViolationType.GENESIS_MISMATCH.value,
   210	                        f"first entry prev_hash={entry['prev_hash']!r} != genesis={expected_genesis!r}",
   211	                    )
   212	                )
   213	        else:
   214	            if entry["prev_hash"] != prev_hash_actual:
   215	                vios.append(
   216	                    Violation(
   217	                        i,
   218	                        entry_id,
   219	                        ViolationType.PREV_HASH_MISMATCH.value,
   220	                        f"prev_hash={entry['prev_hash']!r} != prior entry hash={prev_hash_actual!r}",
   221	                    )
   222	                )
   223	
   224	        # Timestamp monotonicity (ADR-012 §3.4)
   225	        try:
   226	            cur_ts = parse_iso8601(entry["ts"])
   227	        except (ValueError, TypeError):
   228	            cur_ts = None  # schema_invalid_ts 가 이미 등록됨
   229	        if cur_ts is not None and prev_ts is not None and cur_ts < prev_ts:
   230	            vios.append(
   231	                Violation(
   232	                    i,
   233	                    entry_id,
   234	                    "monotonicity_violation",
   235	                    f"ts={entry['ts']!r} < prior ts (ADR-012 §3.4 monotonicity)",
   236	                )
   237	            )
   238	        if cur_ts is not None:
   239	            prev_ts = cur_ts
   240	
   241	        # 다음 iteration 위해 hash field 값 (recompute 와 같으면 그대로, 아니면 chain 깨짐 → mismatch 보고됨)
   242	        prev_hash_actual = entry.get("hash")
   243	
   244	    return vios
   245	
   246	
   247	def build_violation_entry(
   248	    entries: list[dict[str, Any]],
   249	    violations: list[Violation],
   250	) -> dict[str, Any] | None:
   251	    """chain_violation_detected ledger entry 자동 작성 (ADR-012 §2.7).
   252	
   253	    Returns:
   254	        새 ledger entry dict (caller 가 ledger 에 append 가능 형식) 또는 None (위반 0건)
   255	    """
   256	    if not violations:
   257	        return None
   258	
   259	    # chain violation (Layer 1 enum) 만 분류 — schema/monotonicity 위반 제외
   260	    chain_violations = [
   261	        v for v in violations
   262	        if v.violation_type in {vt.value for vt in ViolationType}
   263	    ]
   264	    if not chain_violations:
   265	        # schema/monotonicity 위반만 — chain_violation_detected 자동 작성 영역 외
   266	        return None
   267	
   268	    # 마지막 entry 의 hash 를 prev_hash 로 사용 (chain 연속성 — append-only 답습)
   269	    if entries:
   270	        last_entry = entries[-1]
   271	        prev_hash = last_entry.get("hash", compute_genesis_hash(
   272	            last_entry.get("scope", "global"), last_entry.get("schema_version", SUPPORTED_SCHEMA_VERSION)
   273	        ))
   274	        scope = last_entry.get("scope", "global")
   275	    else:
   276	        prev_hash = compute_genesis_hash("global", SUPPORTED_SCHEMA_VERSION)
   277	        scope = "global"
   278	
   279	    now_iso = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
   280	    entry: dict[str, Any] = {

exec
/bin/bash -lc "nl -ba .github/workflows/g4-hash-chain.yml | sed -n '1,300p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# G4 JSONL Hash Chain + RFC 8785 JCS + Round-trip — Group C PoC
     2	#
     3	# 답습 출처:
     4	#   - docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md (본 PoC 사양 §6)
     5	#   - docs/review/3plus1-consensus-2026-05-10-g4-jcs-library-selection.md (Q1 풀 3+1 합의 17 조건)
     6	#   - docs/review/3plus1-consensus-2026-05-10-g4-corpus-poc-scope-short.md (Q2/Q3 단축 합의 6 조건)
     7	#   - docs/decisions/ADR-012-evidence-ledger-protection.md §2.5 (RFC 8785 JCS Primary + jq fallback + corpus 검증)
     8	#   - docs/architecture/provider-agnostic-memory-skill-design.md §4.4 (hash chain) + §4.6 (round-trip)
     9	#   - .github/workflows/evidence-pass-gate.yml (Group B 시제 직접 답습)
    10	#
    11	# 본 workflow 의 양방향 검증:
    12	#   - corpus 24 회귀 (Primary 1 rfc8785 + Primary 2 jcs cross-check + sha256 일관성)
    13	#   - NaN/Inf reject 2건 (양 라이브러리 모두 raise 검증)
    14	#   - PASS fixture × 2: jsonl_hash_chain.py rc=0
    15	#   - FAIL fixture × 5: jsonl_hash_chain.py rc=1 + 5 violation_type cover
    16	#   - Round-trip PASS fixture: jsonl_roundtrip.py rc=0 (T2 strict)
    17	#
    18	# 본 PoC 는 G4 *부분 충족 시제* 한정 — G4 전체 PASS 권한 0건 (사용자 명시 답습).
    19	name: G4 Hash Chain + JCS
    20	
    21	on:
    22	  push:
    23	    branches:
    24	      - main
    25	      - develop
    26	      - "feature/**"
    27	    paths:
    28	      - "tools/canonical_json.py"
    29	      - "tools/jsonl_hash_chain.py"
    30	      - "tools/jsonl_roundtrip.py"
    31	      - "tests/canonical/**"
    32	      - "tests/fixtures/jsonl_ledger/**"
    33	      - ".github/workflows/g4-hash-chain.yml"
    34	      - "requirements-dev.txt"
    35	  pull_request:
    36	    branches:
    37	      - main
    38	      - develop
    39	
    40	permissions:
    41	  contents: read
    42	
    43	jobs:
    44	  enforce:
    45	    runs-on: ubuntu-latest
    46	    timeout-minutes: 10
    47	    env:
    48	      PYTHONPATH: tools
    49	    steps:
    50	      - name: Checkout
    51	        uses: actions/checkout@v6
    52	
    53	      - name: Set up Python
    54	        uses: actions/setup-python@v6
    55	        with:
    56	          python-version: "3.12"
    57	
    58	      - name: Install jq (POSIX fallback)
    59	        run: |
    60	          sudo apt-get update -qq
    61	          sudo apt-get install -y jq
    62	          jq --version
    63	
    64	      - name: Install Primary 1 + Primary 2 (Q1 합의 R-A2 답습)
    65	        run: |
    66	          python -m pip install --upgrade pip
    67	          # 본 PoC 한정 의존만 설치 (import-linter 등 G2 전용 dep 제외)
    68	          pip install rfc8785==0.1.4 jcs==0.2.1
    69	          python -c "import rfc8785, jcs; print('rfc8785:', rfc8785.__file__); print('jcs:', jcs.__file__)"
    70	
    71	      - name: Corpus regression — Primary 1 (rfc8785) byte + sha256
    72	        run: |
    73	          set -e
    74	          fail=0
    75	          total=0
    76	          for inp in tests/canonical/*/*.input.json; do
    77	            base="${inp%.input.json}"
    78	            exp_canonical="${base}.expected.canonical"
    79	            exp_sha256="${base}.expected.sha256"
    80	            total=$((total + 1))
    81	            if ! python tools/canonical_json.py --mode primary_1_only --input "$inp" \
    82	                  --expected-canonical "$exp_canonical" \
    83	                  --expected-sha256 "$exp_sha256" >/dev/null 2>err.log; then
    84	              echo "::error::Primary 1 regression FAIL: $inp"
    85	              cat err.log
    86	              fail=$((fail + 1))
    87	            fi
    88	          done
    89	          rm -f err.log
    90	          echo "Primary 1 corpus: ${total} cases, ${fail} fail"
    91	          if [ "$fail" -ne 0 ]; then
    92	            echo "::error::Primary 1 (rfc8785) corpus regression: $fail / $total cases failed"
    93	            exit 1
    94	          fi
    95	
    96	      - name: Corpus regression — Primary 2 (jcs) cross-check (TR-C-2 답습)
    97	        run: |
    98	          set -e
    99	          fail=0
   100	          total=0
   101	          for inp in tests/canonical/*/*.input.json; do
   102	            base="${inp%.input.json}"
   103	            exp_canonical="${base}.expected.canonical"
   104	            total=$((total + 1))
   105	            # Primary 2 단독 + expected 비교 (Q1 합의 D-1 — corpus 시점 cross-check 강제)
   106	            if ! python tools/canonical_json.py --mode primary_2_only --input "$inp" \
   107	                  --expected-canonical "$exp_canonical" >/dev/null 2>err.log; then
   108	              echo "::error::Primary 2 regression FAIL: $inp"
   109	              cat err.log
   110	              fail=$((fail + 1))
   111	            fi
   112	          done
   113	          rm -f err.log
   114	          echo "Primary 2 corpus: ${total} cases, ${fail} fail"
   115	          if [ "$fail" -ne 0 ]; then
   116	            echo "::error::Primary 2 (jcs) corpus regression: $fail / $total cases failed (TR-C-2 escalation)"
   117	            exit 1
   118	          fi
   119	
   120	      - name: Corpus regression — cross_check mode (Primary 1 ↔ Primary 2 byte equivalence)
   121	        run: |
   122	          set -e
   123	          fail=0
   124	          total=0
   125	          for inp in tests/canonical/*/*.input.json; do
   126	            base="${inp%.input.json}"
   127	            exp_canonical="${base}.expected.canonical"
   128	            total=$((total + 1))
   129	            if ! python tools/canonical_json.py --mode cross_check --input "$inp" \
   130	                  --expected-canonical "$exp_canonical" >/dev/null 2>err.log; then
   131	              echo "::error::cross_check FAIL: $inp"
   132	              cat err.log
   133	              fail=$((fail + 1))
   134	            fi
   135	          done
   136	          rm -f err.log
   137	          echo "cross_check corpus: ${total} cases, ${fail} fail"
   138	          if [ "$fail" -ne 0 ]; then
   139	            echo "::error::cross_check corpus: $fail / $total cases failed (TR-C-2 escalation)"
   140	            exit 1
   141	          fi
   142	
   143	      - name: Fallback equivalence — jq -S -c vs Primary 1
   144	        run: |
   145	          set -e
   146	          fail=0
   147	          total=0
   148	          for inp in tests/canonical/*/*.input.json; do
   149	            base="${inp%.input.json}"
   150	            exp_canonical="${base}.expected.canonical"
   151	            total=$((total + 1))
   152	            if ! python tools/canonical_json.py --mode primary_1_only --input "$inp" \
   153	                  --expected-canonical "$exp_canonical" \
   154	                  --verify-fallback-equiv >/dev/null 2>err.log; then
   155	              echo "::warning::jq fallback equivalence DIFF: $inp"
   156	              cat err.log
   157	              fail=$((fail + 1))
   158	            fi
   159	          done
   160	          rm -f err.log
   161	          echo "jq fallback equivalence: ${total} cases, ${fail} differ"
   162	          # jq fallback 동등성 실패는 warning 한정 (ADR-012 §2.5 — `Fallback 사용 빈도 > 10%` 별도 합의 trigger 답습)
   163	
   164	      - name: NaN/Inf reject (Q1 합의 C-B8 + 본 합의 C-Q2 답습)
   165	        run: |
   166	          python - <<'PY'
   167	          import sys
   168	          import rfc8785, jcs
   169	          fail = 0
   170	          for label, val in [("nan", float("nan")), ("inf", float("inf")), ("-inf", float("-inf"))]:
   171	              for libname, fn in [("rfc8785", lambda v: rfc8785.dumps({"n": v})),
   172	                                  ("jcs", lambda v: jcs.canonicalize({"n": v}))]:
   173	                  try:
   174	                      fn(val)
   175	                      print(f"FAIL: {libname} accepted {label} (RFC 8785 §3.2.2.2 violation)")
   176	                      fail += 1
   177	                  except (ValueError, Exception) as e:
   178	                      print(f"OK: {libname} rejected {label}: {type(e).__name__}")
   179	          sys.exit(1 if fail else 0)
   180	          PY
   181	
   182	      - name: PASS fixture — jsonl_hash_chain rc=0 (× 2)
   183	        run: |
   184	          set -e
   185	          for f in tests/fixtures/jsonl_ledger/pass/*.jsonl; do
   186	            set +e
   187	            python tools/jsonl_hash_chain.py "$f"
   188	            rc=$?
   189	            set -e
   190	            if [ "$rc" -ne 0 ]; then
   191	              echo "::error::PASS fixture $f returned rc=$rc (expected 0)"
   192	              exit 1
   193	            fi
   194	          done
   195	          echo "PASS fixtures verified (rc=0 for all)"
   196	
   197	      - name: FAIL fixture — jsonl_hash_chain rc=1 + 5 violation_type cover
   198	        run: |
   199	          set -e
   200	          # Expected violation_type per fixture (5 패턴 cover 강제 — 59 entry C-1 timestamp 보강)
   201	          declare -A EXPECTED=(
   202	            [prev_hash_mismatch.jsonl]=prev_hash_mismatch
   203	            [hash_recalculation.jsonl]=hash_recalculation
   204	            [missing_event_field.jsonl]=schema_missing_field
   205	            [genesis_mismatch.jsonl]=genesis_mismatch
   206	            [timestamp_monotonicity.jsonl]=monotonicity_violation
   207	          )
   208	          for f in tests/fixtures/jsonl_ledger/fail/*.jsonl; do
   209	            name=$(basename "$f")
   210	            expected="${EXPECTED[$name]:-}"
   211	            set +e
   212	            python tools/jsonl_hash_chain.py "$f" 2> chain_out.txt
   213	            rc=$?
   214	            set -e
   215	            cat chain_out.txt
   216	            if [ "$rc" -ne 1 ]; then
   217	              echo "::error::FAIL fixture $name returned rc=$rc (expected 1)"
   218	              exit 1
   219	            fi
   220	            if [ -n "$expected" ] && ! grep -q "type=$expected" chain_out.txt; then
   221	              echo "::error::FAIL fixture $name missing violation_type=$expected"
   222	              exit 1
   223	            fi
   224	            echo "  $name OK (rc=1, violation_type=$expected)"
   225	          done
   226	          rm -f chain_out.txt
   227	          echo "FAIL fixtures verified — 5 violation_type cover (chain violation 4 패턴 + timestamp monotonicity)"
   228	
   229	      - name: Round-trip — T2 strict on PASS fixtures
   230	        run: |
   231	          set -e
   232	          for f in tests/fixtures/jsonl_ledger/pass/*.jsonl; do
   233	            set +e
   234	            python tools/jsonl_roundtrip.py --require-strict "$f"
   235	            rc=$?
   236	            set -e
   237	            if [ "$rc" -ne 0 ]; then
   238	              echo "::error::Round-trip T2 strict FAIL on $f (rc=$rc, TR-C-4 trigger)"
   239	              exit 1
   240	            fi
   241	            echo "  $(basename $f) — T2 strict PASS"
   242	          done
   243	
   244	      - name: Evidence summary
   245	        if: always()
   246	        run: |
   247	          echo "## G4 Hash Chain + JCS — Evidence" >> $GITHUB_STEP_SUMMARY
   248	          echo "- commit: ${{ github.sha }}" >> $GITHUB_STEP_SUMMARY
   249	          echo "- ref: ${{ github.ref }}" >> $GITHUB_STEP_SUMMARY
   250	          echo "- run: ${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}" >> $GITHUB_STEP_SUMMARY
   251	          echo "- event: g4_hash_chain_jcs_layer1" >> $GITHUB_STEP_SUMMARY
   252	          echo "- agent: user" >> $GITHUB_STEP_SUMMARY
   253	          echo "- ledger_layer: Layer 1 — Hash Chain + Canonical JSON + Round-trip (Group C PoC)" >> $GITHUB_STEP_SUMMARY
   254	          echo "- corpus: 24 cases × 4 axes (Primary 1 + Primary 2 + cross_check + jq fallback)" >> $GITHUB_STEP_SUMMARY
   255	          echo "- chain violation cover: 5 패턴 (prev_hash_mismatch + hash_recalculation + schema_missing_field + genesis_mismatch + monotonicity_violation)" >> $GITHUB_STEP_SUMMARY
   256	          echo "- round-trip: T2 strict (PASS fixtures)" >> $GITHUB_STEP_SUMMARY
   257	          echo "- numeric reject: NaN + Inf + -Inf (rfc8785 + jcs)" >> $GITHUB_STEP_SUMMARY
   258	          echo "- PASS scope: G4 *부분 충족 시제* 한정 (G4 전체 PASS 권한 0건, 사용자 명시 답습)" >> $GITHUB_STEP_SUMMARY

exec
/bin/bash -lc 'find tests/fixtures/jsonl_ledger -maxdepth 3 -type f | sort && find tests/fixtures/history_anchor_verifier tests/fixtures/rewrite_defense -maxdepth 3 -type f | sort && find tests/canonical -type f | sort | wc -l' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
tests/fixtures/jsonl_ledger/fail/genesis_mismatch.jsonl
tests/fixtures/jsonl_ledger/fail/hash_recalculation.jsonl
tests/fixtures/jsonl_ledger/fail/missing_event_field.jsonl
tests/fixtures/jsonl_ledger/fail/prev_hash_mismatch.jsonl
tests/fixtures/jsonl_ledger/fail/timestamp_monotonicity.jsonl
tests/fixtures/jsonl_ledger/pass/minimal_chain.jsonl
tests/fixtures/jsonl_ledger/pass/roundtrip_t2_strict.jsonl
tests/fixtures/history_anchor_verifier/chain_only_demo/full_rewrite_ledger.jsonl
tests/fixtures/history_anchor_verifier/fail/anchor_full_rewrite.json
tests/fixtures/history_anchor_verifier/fail/anchor_middle_deletion.json
tests/fixtures/history_anchor_verifier/fail/anchor_substitution.json
tests/fixtures/history_anchor_verifier/fail/anchor_tail_truncation.json
tests/fixtures/history_anchor_verifier/fail/anchor_tampered.json
tests/fixtures/history_anchor_verifier/fail/full_rewrite_ledger.jsonl
tests/fixtures/history_anchor_verifier/fail/middle_deletion_ledger.jsonl
tests/fixtures/history_anchor_verifier/fail/substitution_ledger.jsonl
tests/fixtures/history_anchor_verifier/fail/tail_truncation_ledger.jsonl
tests/fixtures/history_anchor_verifier/pass/extended_anchor.json
tests/fixtures/history_anchor_verifier/pass/extended_ledger.jsonl
tests/fixtures/history_anchor_verifier/pass/original_anchor.json
tests/fixtures/history_anchor_verifier/pass/original_ledger.jsonl
tests/fixtures/rewrite_defense/append_only/pass/commit_history_after.txt
tests/fixtures/rewrite_defense/append_only/pass/commit_history_before.txt
tests/fixtures/rewrite_defense/line_regression/pass/base.jsonl
tests/fixtures/rewrite_defense/line_regression/pass/head.jsonl
tests/fixtures/rewrite_defense/rewrite_command/fail/git_command_log_filter_branch.txt
tests/fixtures/rewrite_defense/rewrite_command/fail/git_command_log_push_force.txt
tests/fixtures/rewrite_defense/rewrite_command/fail/git_command_log_rebase.txt
tests/fixtures/rewrite_defense/rewrite_command/fail/git_command_log_reset_hard.txt
tests/fixtures/rewrite_defense/rewrite_command/pass/git_command_log_safe.txt
72

exec
/bin/bash -lc 'git config --show-origin --get receive.denyNonFastForwards; git config --global --show-origin --get receive.denyNonFastForwards; git config --system --show-origin --get receive.denyNonFastForwards' in /home/delangi/문서/project/category/AI_development_tool
 exited 1 in 0ms:
exec
/bin/bash -lc "nl -ba .github/workflows/rewrite-defense.yml | sed -n '1,320p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# G4 Rewrite Defense — Layer 2/3/4 PoC — Group C 후속 후속
     2	#
     3	# 답습 출처:
     4	#   - docs/phase0/g4-rewrite-defense-layer234-poc.md (본 PoC 사양 §13 — 14 step CI 설계)
     5	#   - docs/decisions/ADR-012-evidence-ledger-protection.md §2.8 (Full Rewrite 5 Layer)
     6	#   - .github/workflows/history-anchor-verifier.yml (Group C 후속 형식 직접 답습 — rfc8785+jcs install 포함)
     7	#   - .github/workflows/boundary-guard.yml (Group G 답습)
     8	#
     9	# 본 workflow 의 10 검증 (사용자 명시 §10 답습):
    10	#   - --list-defenses self-check (5 layers + 4 commands + 3 regression types)
    11	#   - L2 PASS + L2 FAIL × 2 (force-push + reorder)
    12	#   - L3 PASS + L3 FAIL (4 dangerous patterns cover)
    13	#   - L4 PASS + L4 FAIL × 2 (line deletion + in-place rewrite)
    14	#   - F-금지 grep (실 git command 호출 / 실 GitHub API / production data 0건)
    15	#
    16	# 본 PoC 는 G4 *Layer 2/3/4 정적 검출 시제* 한정 — G4 / G2 / G3 / G4 전체 PASS 권한 0건.
    17	# 풀 3+1 승격 trigger 5 = 0/5 발화 → Reviewer-only 단축 합의 적격.
    18	#
    19	# Artifact path = group-cff-logs/ (Group F 후속 답습 — leading dot 미사용).
    20	# 본 PoC 종료 후 = ADR-012 §2.8 5 Layer 답습 5/5 완결.
    21	name: G4 Rewrite Defense (Layer 2/3/4)
    22	
    23	on:
    24	  push:
    25	    branches:
    26	      - main
    27	      - develop
    28	      - "feature/**"
    29	    paths:
    30	      - "tools/rewrite_defense_check.py"
    31	      - "tools/jsonl_hash_chain.py"
    32	      - "tests/fixtures/rewrite_defense/**"
    33	      - ".github/workflows/rewrite-defense.yml"
    34	  pull_request:
    35	    branches:
    36	      - main
    37	      - develop
    38	
    39	permissions:
    40	  contents: read
    41	
    42	jobs:
    43	  defense:
    44	    runs-on: ubuntu-latest
    45	    timeout-minutes: 10
    46	    env:
    47	      PYTHONPATH: tools
    48	    steps:
    49	      - name: Checkout
    50	        uses: actions/checkout@v6
    51	
    52	      - name: Set up Python
    53	        uses: actions/setup-python@v6
    54	        with:
    55	          python-version: "3.12"
    56	
    57	      - name: Install Group C deps (rfc8785 + jcs — Group C `parse_jsonl` 의존)
    58	        run: |
    59	          python -m pip install --upgrade pip
    60	          # parse_jsonl → canonical_json → rfc8785 의존성 답습
    61	          pip install rfc8785==0.1.4 jcs==0.2.1
    62	          python -c "import rfc8785, jcs; print('rfc8785 + jcs OK')"
    63	
    64	      - name: Prepare log directory (artifact 답습)
    65	        run: mkdir -p group-cff-logs
    66	
    67	      - name: --list-defenses self-check
    68	        id: list_defenses
    69	        run: |
    70	          set +e
    71	          python tools/rewrite_defense_check.py --list-defenses \
    72	            > group-cff-logs/list-defenses.stdout 2> group-cff-logs/list-defenses.stderr
    73	          rc=$?
    74	          set -e
    75	          cat group-cff-logs/list-defenses.stderr
    76	          if [ "$rc" -ne 0 ]; then
    77	            echo "::error::--list-defenses expected rc=0, got rc=$rc"
    78	            exit 1
    79	          fi
    80	          if ! grep -q "adr_012_section_2_8_layers=5" group-cff-logs/list-defenses.stderr; then
    81	            echo "::error::adr_012_section_2_8_layers != 5"
    82	            exit 1
    83	          fi
    84	          if ! grep -q "dangerous_git_commands=4" group-cff-logs/list-defenses.stderr; then
    85	            echo "::error::dangerous_git_commands != 4"
    86	            exit 1
    87	          fi
    88	          if ! grep -q "line_regression_types=3" group-cff-logs/list-defenses.stderr; then
    89	            echo "::error::line_regression_types != 3"
    90	            exit 1
    91	          fi
    92	          if ! grep -q "five_layer_compliant=True" group-cff-logs/list-defenses.stderr; then
    93	            echo "::error::five_layer_compliant != True"
    94	            exit 1
    95	          fi
    96	          if ! grep -q "dangerous_command_count_compliant=True" group-cff-logs/list-defenses.stderr; then
    97	            echo "::error::dangerous_command_count_compliant != True"
    98	            exit 1
    99	          fi
   100	          if ! grep -q "line_regression_type_count_compliant=True" group-cff-logs/list-defenses.stderr; then
   101	            echo "::error::line_regression_type_count_compliant != True"
   102	            exit 1
   103	          fi
   104	          echo "list_defenses=PASS" >> $GITHUB_OUTPUT
   105	          echo "--list-defenses OK (5 layers + 4 commands + 3 regression types)"
   106	
   107	      - name: L2 PASS — append-only commit history (rc=0 + violations=0)
   108	        id: l2_pass
   109	        run: |
   110	          set +e
   111	          python tools/rewrite_defense_check.py --mode append-only \
   112	            tests/fixtures/rewrite_defense/append_only/pass/ \
   113	            > group-cff-logs/l2-pass.stdout 2> group-cff-logs/l2-pass.stderr
   114	          rc=$?
   115	          set -e
   116	          cat group-cff-logs/l2-pass.stderr
   117	          if [ "$rc" -ne 0 ]; then
   118	            echo "::error::L2 PASS expected rc=0, got rc=$rc"
   119	            exit 1
   120	          fi
   121	          if ! grep -q "violations=0" group-cff-logs/l2-pass.stderr; then
   122	            echo "::error::L2 PASS missing 'violations=0'"
   123	            exit 1
   124	          fi
   125	          echo "l2_pass=PASS" >> $GITHUB_OUTPUT
   126	          echo "L2 PASS OK (append-only commit history)"
   127	
   128	      - name: L2 FAIL — force-push + reorder (rc=1 + 2 patterns cover)
   129	        id: l2_fail
   130	        run: |
   131	          set +e
   132	          # force-push fixture
   133	          python tools/rewrite_defense_check.py --mode append-only \
   134	            tests/fixtures/rewrite_defense/append_only/fail/force_push/ \
   135	            > group-cff-logs/l2-fail-force-push.stdout 2> group-cff-logs/l2-fail-force-push.stderr
   136	          fp_rc=$?
   137	          # reorder fixture
   138	          python tools/rewrite_defense_check.py --mode append-only \
   139	            tests/fixtures/rewrite_defense/append_only/fail/reorder/ \
   140	            > group-cff-logs/l2-fail-reorder.stdout 2> group-cff-logs/l2-fail-reorder.stderr
   141	          ro_rc=$?
   142	          set -e
   143	          cat group-cff-logs/l2-fail-force-push.stderr
   144	          cat group-cff-logs/l2-fail-reorder.stderr
   145	          if [ "$fp_rc" -ne 1 ]; then
   146	            echo "::error::L2 FAIL force-push expected rc=1, got rc=$fp_rc"
   147	            exit 1
   148	          fi
   149	          if [ "$ro_rc" -ne 1 ]; then
   150	            echo "::error::L2 FAIL reorder expected rc=1, got rc=$ro_rc"
   151	            exit 1
   152	          fi
   153	          if ! grep -q "non_fast_forward_detected" group-cff-logs/l2-fail-force-push.stderr; then
   154	            echo "::error::L2 FAIL force-push missing 'non_fast_forward_detected'"
   155	            exit 1
   156	          fi
   157	          if ! grep -q "history_reorder_detected" group-cff-logs/l2-fail-reorder.stderr; then
   158	            echo "::error::L2 FAIL reorder missing 'history_reorder_detected'"
   159	            exit 1
   160	          fi
   161	          echo "l2_fail=PASS" >> $GITHUB_OUTPUT
   162	          echo "L2 FAIL OK (rc=1 each, 2 patterns cover: non_fast_forward + history_reorder)"
   163	
   164	      - name: L3 PASS — safe commands (rc=0 + violations=0)
   165	        id: l3_pass
   166	        run: |
   167	          set +e
   168	          python tools/rewrite_defense_check.py --mode rewrite-command \
   169	            tests/fixtures/rewrite_defense/rewrite_command/pass/ \
   170	            > group-cff-logs/l3-pass.stdout 2> group-cff-logs/l3-pass.stderr
   171	          rc=$?
   172	          set -e
   173	          cat group-cff-logs/l3-pass.stderr
   174	          if [ "$rc" -ne 0 ]; then
   175	            echo "::error::L3 PASS expected rc=0, got rc=$rc"
   176	            exit 1
   177	          fi
   178	          if ! grep -q "violations=0" group-cff-logs/l3-pass.stderr; then
   179	            echo "::error::L3 PASS missing 'violations=0'"
   180	            exit 1
   181	          fi
   182	          echo "l3_pass=PASS" >> $GITHUB_OUTPUT
   183	          echo "L3 PASS OK (safe git commands)"
   184	
   185	      - name: L3 FAIL — dangerous commands (rc=1 + 4 patterns cover)
   186	        id: l3_fail
   187	        run: |
   188	          set +e
   189	          python tools/rewrite_defense_check.py --mode rewrite-command \
   190	            tests/fixtures/rewrite_defense/rewrite_command/fail/ \
   191	            > group-cff-logs/l3-fail.stdout 2> group-cff-logs/l3-fail.stderr
   192	          rc=$?
   193	          set -e
   194	          cat group-cff-logs/l3-fail.stderr
   195	          if [ "$rc" -ne 1 ]; then
   196	            echo "::error::L3 FAIL expected rc=1, got rc=$rc"
   197	            exit 1
   198	          fi
   199	          for pid in "rebase" "filter-branch" "reset-hard" "push-force-or-amend"; do
   200	            if ! grep -q "$pid" group-cff-logs/l3-fail.stderr; then
   201	              echo "::error::L3 FAIL missing pattern_id: $pid"
   202	              exit 1
   203	            fi
   204	          done
   205	          echo "l3_fail=PASS" >> $GITHUB_OUTPUT
   206	          echo "L3 FAIL OK (rc=1, 4 patterns cover: rebase + filter-branch + reset-hard + push-force-or-amend)"
   207	
   208	      - name: L4 PASS — head extends base (rc=0 + violations=0)
   209	        id: l4_pass
   210	        run: |
   211	          set +e
   212	          python tools/rewrite_defense_check.py --mode line-regression \
   213	            tests/fixtures/rewrite_defense/line_regression/pass/ \
   214	            > group-cff-logs/l4-pass.stdout 2> group-cff-logs/l4-pass.stderr
   215	          rc=$?
   216	          set -e
   217	          cat group-cff-logs/l4-pass.stderr
   218	          if [ "$rc" -ne 0 ]; then
   219	            echo "::error::L4 PASS expected rc=0, got rc=$rc"
   220	            exit 1
   221	          fi
   222	          if ! grep -q "violations=0" group-cff-logs/l4-pass.stderr; then
   223	            echo "::error::L4 PASS missing 'violations=0'"
   224	            exit 1
   225	          fi
   226	          echo "l4_pass=PASS" >> $GITHUB_OUTPUT
   227	          echo "L4 PASS OK (head extends base)"
   228	
   229	      - name: L4 FAIL — line deletion + in-place rewrite (rc=1 + 2 patterns cover)
   230	        id: l4_fail
   231	        run: |
   232	          set +e
   233	          # line_deletion fixture
   234	          python tools/rewrite_defense_check.py --mode line-regression \
   235	            tests/fixtures/rewrite_defense/line_regression/fail/line_deletion/ \
   236	            > group-cff-logs/l4-fail-deletion.stdout 2> group-cff-logs/l4-fail-deletion.stderr
   237	          ld_rc=$?
   238	          # line_rewrite fixture
   239	          python tools/rewrite_defense_check.py --mode line-regression \
   240	            tests/fixtures/rewrite_defense/line_regression/fail/line_rewrite/ \
   241	            > group-cff-logs/l4-fail-rewrite.stdout 2> group-cff-logs/l4-fail-rewrite.stderr
   242	          lr_rc=$?
   243	          set -e
   244	          cat group-cff-logs/l4-fail-deletion.stderr
   245	          cat group-cff-logs/l4-fail-rewrite.stderr
   246	          if [ "$ld_rc" -ne 1 ]; then
   247	            echo "::error::L4 FAIL line_deletion expected rc=1, got rc=$ld_rc"
   248	            exit 1
   249	          fi
   250	          if [ "$lr_rc" -ne 1 ]; then
   251	            echo "::error::L4 FAIL line_rewrite expected rc=1, got rc=$lr_rc"
   252	            exit 1
   253	          fi
   254	          if ! grep -q "line_deletion_detected" group-cff-logs/l4-fail-deletion.stderr; then
   255	            echo "::error::L4 FAIL line_deletion missing 'line_deletion_detected'"
   256	            exit 1
   257	          fi
   258	          if ! grep -q "line_rewrite_detected" group-cff-logs/l4-fail-rewrite.stderr; then
   259	            echo "::error::L4 FAIL line_rewrite missing 'line_rewrite_detected'"
   260	            exit 1
   261	          fi
   262	          echo "l4_fail=PASS" >> $GITHUB_OUTPUT
   263	          echo "L4 FAIL OK (rc=1 each, 2 patterns cover: line_deletion + line_rewrite)"
   264	
   265	      - name: F-금지 자기 검증 (Layer 1 grep — 실 git command / GitHub API / production data 0건)
   266	        id: forbidden_check
   267	        run: |
   268	          set -e
   269	          violations=0
   270	          # F-금지: 실 git command 호출 (subprocess) 0건
   271	          if grep -E "subprocess\.(run|Popen)|os\.system|os\.popen" tools/rewrite_defense_check.py; then
   272	            echo "::error::F-금지 위반 — subprocess / os.system / os.popen 사용"
   273	            violations=$((violations+1))
   274	          fi
   275	          # F-금지: 실 HTTP 클라이언트 import 0건
   276	          if grep -E "^(import|from)\s+(httpx|requests|aiohttp|urllib3)" tools/rewrite_defense_check.py; then
   277	            echo "::error::F-금지 위반 — HTTP client import"
   278	            violations=$((violations+1))
   279	          fi
   280	          # F-금지: 실 git hook / repo path / git library 사용 0건
   281	          if grep -rE "/\.git/hooks|/\.git/refs|gitpython|pygit2" tools/rewrite_defense_check.py; then
   282	            echo "::error::F-금지 위반 — 실 git hook / repo path / git library"
   283	            violations=$((violations+1))
   284	          fi
   285	          # F-금지: production data path
   286	          if grep -rE "/home/.*\.claude/|/Users/.*\.claude/|production[_-]" \
   287	               tests/fixtures/rewrite_defense/ tools/rewrite_defense_check.py 2>/dev/null; then
   288	            echo "::error::F-금지 위반 — production data path"
   289	            violations=$((violations+1))
   290	          fi
   291	          if [ "$violations" -ne 0 ]; then
   292	            echo "::error::F-금지 자기 검증 FAIL — $violations 위반"
   293	            exit 1
   294	          fi
   295	          echo "forbidden_check=PASS" >> $GITHUB_OUTPUT
   296	          echo "F-금지 자기 검증 OK — 0/9 위반"
   297	
   298	      - name: Build summary.json (Evidence summary 답습)
   299	        if: always()
   300	        run: |
   301	          cat > group-cff-logs/summary.json <<EOF
   302	          {
   303	            "list_defenses": "${{ steps.list_defenses.outputs.list_defenses || 'FAIL' }}",
   304	            "l2_pass": "${{ steps.l2_pass.outputs.l2_pass || 'FAIL' }}",
   305	            "l2_fail": "${{ steps.l2_fail.outputs.l2_fail || 'FAIL' }}",
   306	            "l3_pass": "${{ steps.l3_pass.outputs.l3_pass || 'FAIL' }}",
   307	            "l3_fail": "${{ steps.l3_fail.outputs.l3_fail || 'FAIL' }}",
   308	            "l4_pass": "${{ steps.l4_pass.outputs.l4_pass || 'FAIL' }}",
   309	            "l4_fail": "${{ steps.l4_fail.outputs.l4_fail || 'FAIL' }}",
   310	            "forbidden_check": "${{ steps.forbidden_check.outputs.forbidden_check || 'FAIL' }}",
   311	            "f_forbidden_violations": "0/9",
   312	            "escalation_triggers": "0/5",
   313	            "adr_012_section_2_8_layers": "5",
   314	            "dangerous_git_commands": "4",
   315	            "line_regression_types": "3",
   316	            "poc_layer_coverage": "L2+L3+L4 (L1=Group C, L5=Group C 후속)",
   317	            "five_layer_compliant_after_this_poc": "True",
   318	            "commit": "${{ github.sha }}",
   319	            "ref": "${{ github.ref }}",
   320	            "run_id": "${{ github.run_id }}",

exec
/bin/bash -lc "nl -ba .github/workflows/history-anchor-verifier.yml | sed -n '1,340p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# G4 History Rewrite — Layer 5 External Anchor Verifier — Group C 후속 PoC
     2	#
     3	# 답습 출처:
     4	#   - docs/phase0/g4-history-rewrite-layer5-anchor-poc.md (본 PoC 사양 §10 — 13 step CI 설계)
     5	#   - docs/decisions/ADR-012-evidence-ledger-protection.md §2.8 (Full Rewrite 5 Layer)
     6	#   - .github/workflows/boundary-guard.yml (Group G 형식 직접 답습)
     7	#   - .github/workflows/g4-hash-chain.yml (Group C 답습)
     8	#
     9	# 본 workflow 의 10 검증 (사용자 명시 §7 답습):
    10	#   - --list-attack-models self-check (5 scenarios + 11 fields)
    11	#   - Anchor PASS × 2 (original + extended append)
    12	#   - Anchor FAIL × 5 (full rewrite + tail truncation + middle deletion + substitution + tampered anchor)
    13	#   - Layer 1 inadequacy demo (chain-only mode 의도된 PASS)
    14	#   - F-금지 grep (실 signed commit / external service / GitHub API / production data 0건)
    15	#
    16	# 본 PoC 는 G4 *Layer 5 정적 검출 시제* 한정 — G4 / G2 / G3 / G4 전체 PASS 권한 0건.
    17	# 풀 3+1 승격 trigger 5 = 0/5 발화 → Reviewer-only 단축 합의 적격.
    18	#
    19	# Artifact path = group-c-followup-logs/ (Group F 후속 답습 — leading dot 미사용).
    20	name: G4 History Anchor Verifier (Layer 5)
    21	
    22	on:
    23	  push:
    24	    branches:
    25	      - main
    26	      - develop
    27	      - "feature/**"
    28	    paths:
    29	      - "tools/history_anchor_verifier.py"
    30	      - "tools/jsonl_hash_chain.py"
    31	      - "tests/fixtures/history_anchor_verifier/**"
    32	      - ".github/workflows/history-anchor-verifier.yml"
    33	  pull_request:
    34	    branches:
    35	      - main
    36	      - develop
    37	
    38	permissions:
    39	  contents: read
    40	
    41	jobs:
    42	  verify:
    43	    runs-on: ubuntu-latest
    44	    timeout-minutes: 10
    45	    env:
    46	      PYTHONPATH: tools
    47	    steps:
    48	      - name: Checkout
    49	        uses: actions/checkout@v6
    50	
    51	      - name: Set up Python
    52	        uses: actions/setup-python@v6
    53	        with:
    54	          python-version: "3.12"
    55	
    56	      - name: Install Group C deps (rfc8785 + jcs — Group C `compute_entry_hash` 의존)
    57	        run: |
    58	          python -m pip install --upgrade pip
    59	          # validate_chain → compute_entry_hash → canonical_json → rfc8785 의존성 답습
    60	          pip install rfc8785==0.1.4 jcs==0.2.1
    61	          python -c "import rfc8785, jcs; print('rfc8785 + jcs OK')"
    62	
    63	      - name: Prepare log directory (artifact 답습)
    64	        run: mkdir -p group-c-followup-logs
    65	
    66	      - name: --list-attack-models self-check
    67	        id: list_attack
    68	        run: |
    69	          set +e
    70	          python tools/history_anchor_verifier.py --list-attack-models \
    71	            > group-c-followup-logs/list-attack.stdout 2> group-c-followup-logs/list-attack.stderr
    72	          rc=$?
    73	          set -e
    74	          cat group-c-followup-logs/list-attack.stderr
    75	          if [ "$rc" -ne 0 ]; then
    76	            echo "::error::--list-attack-models expected rc=0, got rc=$rc"
    77	            exit 1
    78	          fi
    79	          if ! grep -q "attack_scenarios=5" group-c-followup-logs/list-attack.stderr; then
    80	            echo "::error::attack_scenarios != 5 (ADR-012 §2.8 답습 위반)"
    81	            exit 1
    82	          fi
    83	          if ! grep -q "total_anchor_fields=11" group-c-followup-logs/list-attack.stderr; then
    84	            echo "::error::total_anchor_fields != 11"
    85	            exit 1
    86	          fi
    87	          if ! grep -q "layer_5_compliant=True" group-c-followup-logs/list-attack.stderr; then
    88	            echo "::error::layer_5_compliant != True"
    89	            exit 1
    90	          fi
    91	          if ! grep -q "anchor_field_count_compliant=True" group-c-followup-logs/list-attack.stderr; then
    92	            echo "::error::anchor_field_count_compliant != True"
    93	            exit 1
    94	          fi
    95	          if ! grep -q "layer_1_inadequacy_demo_supported=True" group-c-followup-logs/list-attack.stderr; then
    96	            echo "::error::layer_1_inadequacy_demo_supported != True"
    97	            exit 1
    98	          fi
    99	          echo "list_attack=PASS" >> $GITHUB_OUTPUT
   100	          echo "--list-attack-models OK (5 attack + 11 fields + Layer 1 inadequacy demo supported)"
   101	
   102	      - name: Anchor PASS — original (rc=0 + violations=0)
   103	        id: anchor_pass_original
   104	        run: |
   105	          set +e
   106	          python tools/history_anchor_verifier.py --mode anchor-verify \
   107	            tests/fixtures/history_anchor_verifier/pass/original_anchor.json \
   108	            > group-c-followup-logs/anchor-pass-original.stdout 2> group-c-followup-logs/anchor-pass-original.stderr
   109	          rc=$?
   110	          set -e
   111	          cat group-c-followup-logs/anchor-pass-original.stderr
   112	          if [ "$rc" -ne 0 ]; then
   113	            echo "::error::Anchor PASS original expected rc=0, got rc=$rc"
   114	            exit 1
   115	          fi
   116	          if ! grep -q "violations=0" group-c-followup-logs/anchor-pass-original.stderr; then
   117	            echo "::error::Anchor PASS original missing 'violations=0'"
   118	            exit 1
   119	          fi
   120	          echo "anchor_pass_original=PASS" >> $GITHUB_OUTPUT
   121	          echo "Anchor PASS original OK (rc=0, anchor matched)"
   122	
   123	      - name: Anchor PASS — extended append (rc=0 + violations=0)
   124	        id: anchor_pass_extended
   125	        run: |
   126	          set +e
   127	          python tools/history_anchor_verifier.py --mode anchor-verify \
   128	            tests/fixtures/history_anchor_verifier/pass/extended_anchor.json \
   129	            > group-c-followup-logs/anchor-pass-extended.stdout 2> group-c-followup-logs/anchor-pass-extended.stderr
   130	          rc=$?
   131	          set -e
   132	          cat group-c-followup-logs/anchor-pass-extended.stderr
   133	          if [ "$rc" -ne 0 ]; then
   134	            echo "::error::Anchor PASS extended expected rc=0, got rc=$rc"
   135	            exit 1
   136	          fi
   137	          if ! grep -q "violations=0" group-c-followup-logs/anchor-pass-extended.stderr; then
   138	            echo "::error::Anchor PASS extended missing 'violations=0'"
   139	            exit 1
   140	          fi
   141	          echo "anchor_pass_extended=PASS" >> $GITHUB_OUTPUT
   142	          echo "Anchor PASS extended OK (rc=0, prefix matched — Layer 5 정상 운영 시제)"
   143	
   144	      - name: Anchor FAIL — full rewrite (rc=1 + tail_hash_mismatch)
   145	        id: anchor_fail_rewrite
   146	        run: |
   147	          set +e
   148	          python tools/history_anchor_verifier.py --mode anchor-verify \
   149	            tests/fixtures/history_anchor_verifier/fail/anchor_full_rewrite.json \
   150	            > group-c-followup-logs/anchor-fail-rewrite.stdout 2> group-c-followup-logs/anchor-fail-rewrite.stderr
   151	          rc=$?
   152	          set -e
   153	          cat group-c-followup-logs/anchor-fail-rewrite.stderr
   154	          if [ "$rc" -ne 1 ]; then
   155	            echo "::error::Anchor FAIL full rewrite expected rc=1, got rc=$rc"
   156	            exit 1
   157	          fi
   158	          if ! grep -q "tail-hash-mismatch" group-c-followup-logs/anchor-fail-rewrite.stderr; then
   159	            echo "::error::Anchor FAIL full rewrite missing 'tail-hash-mismatch'"
   160	            exit 1
   161	          fi
   162	          echo "anchor_fail_rewrite=PASS" >> $GITHUB_OUTPUT
   163	          echo "Anchor FAIL full rewrite OK (rc=1, tail-hash-mismatch detected)"
   164	
   165	      - name: Anchor FAIL — tail truncation (rc=1 + entry_count + tail_hash)
   166	        id: anchor_fail_truncation
   167	        run: |
   168	          set +e
   169	          python tools/history_anchor_verifier.py --mode anchor-verify \
   170	            tests/fixtures/history_anchor_verifier/fail/anchor_tail_truncation.json \
   171	            > group-c-followup-logs/anchor-fail-truncation.stdout 2> group-c-followup-logs/anchor-fail-truncation.stderr
   172	          rc=$?
   173	          set -e
   174	          cat group-c-followup-logs/anchor-fail-truncation.stderr
   175	          if [ "$rc" -ne 1 ]; then
   176	            echo "::error::Anchor FAIL tail truncation expected rc=1, got rc=$rc"
   177	            exit 1
   178	          fi
   179	          for pid in "entry-count-mismatch" "tail-hash-mismatch"; do
   180	            if ! grep -q "$pid" group-c-followup-logs/anchor-fail-truncation.stderr; then
   181	              echo "::error::Anchor FAIL tail truncation missing $pid"
   182	              exit 1
   183	            fi
   184	          done
   185	          echo "anchor_fail_truncation=PASS" >> $GITHUB_OUTPUT
   186	          echo "Anchor FAIL tail truncation OK (rc=1, entry-count + tail-hash mismatch)"
   187	
   188	      - name: Anchor FAIL — middle deletion (rc=1 + entry_count + tail_hash)
   189	        id: anchor_fail_deletion
   190	        run: |
   191	          set +e
   192	          python tools/history_anchor_verifier.py --mode anchor-verify \
   193	            tests/fixtures/history_anchor_verifier/fail/anchor_middle_deletion.json \
   194	            > group-c-followup-logs/anchor-fail-deletion.stdout 2> group-c-followup-logs/anchor-fail-deletion.stderr
   195	          rc=$?
   196	          set -e
   197	          cat group-c-followup-logs/anchor-fail-deletion.stderr
   198	          if [ "$rc" -ne 1 ]; then
   199	            echo "::error::Anchor FAIL middle deletion expected rc=1, got rc=$rc"
   200	            exit 1
   201	          fi
   202	          for pid in "entry-count-mismatch" "tail-hash-mismatch"; do
   203	            if ! grep -q "$pid" group-c-followup-logs/anchor-fail-deletion.stderr; then
   204	              echo "::error::Anchor FAIL middle deletion missing $pid"
   205	              exit 1
   206	            fi
   207	          done
   208	          echo "anchor_fail_deletion=PASS" >> $GITHUB_OUTPUT
   209	          echo "Anchor FAIL middle deletion OK (rc=1, entry-count + tail-hash mismatch)"
   210	
   211	      - name: Anchor FAIL — substitution (rc=1 + tail_hash + genesis_hash)
   212	        id: anchor_fail_substitution
   213	        run: |
   214	          set +e
   215	          python tools/history_anchor_verifier.py --mode anchor-verify \
   216	            tests/fixtures/history_anchor_verifier/fail/anchor_substitution.json \
   217	            > group-c-followup-logs/anchor-fail-substitution.stdout 2> group-c-followup-logs/anchor-fail-substitution.stderr
   218	          rc=$?
   219	          set -e
   220	          cat group-c-followup-logs/anchor-fail-substitution.stderr
   221	          if [ "$rc" -ne 1 ]; then
   222	            echo "::error::Anchor FAIL substitution expected rc=1, got rc=$rc"
   223	            exit 1
   224	          fi
   225	          for pid in "tail-hash-mismatch" "genesis-hash-mismatch"; do
   226	            if ! grep -q "$pid" group-c-followup-logs/anchor-fail-substitution.stderr; then
   227	              echo "::error::Anchor FAIL substitution missing $pid"
   228	              exit 1
   229	            fi
   230	          done
   231	          echo "anchor_fail_substitution=PASS" >> $GITHUB_OUTPUT
   232	          echo "Anchor FAIL substitution OK (rc=1, tail-hash + genesis-hash mismatch)"
   233	
   234	      - name: Anchor FAIL — tampered anchor (rc=1 + anchor_self_inconsistent — known limitation)
   235	        id: anchor_fail_tampered
   236	        run: |
   237	          set +e
   238	          python tools/history_anchor_verifier.py --mode anchor-verify \
   239	            tests/fixtures/history_anchor_verifier/fail/anchor_tampered.json \
   240	            > group-c-followup-logs/anchor-fail-tampered.stdout 2> group-c-followup-logs/anchor-fail-tampered.stderr
   241	          rc=$?
   242	          set -e
   243	          cat group-c-followup-logs/anchor-fail-tampered.stderr
   244	          if [ "$rc" -ne 1 ]; then
   245	            echo "::error::Anchor FAIL tampered expected rc=1, got rc=$rc"
   246	            exit 1
   247	          fi
   248	          if ! grep -q "anchor-self-inconsistent" group-c-followup-logs/anchor-fail-tampered.stderr; then
   249	            echo "::error::Anchor FAIL tampered missing 'anchor-self-inconsistent'"
   250	            exit 1
   251	          fi
   252	          echo "anchor_fail_tampered=PASS" >> $GITHUB_OUTPUT
   253	          echo "Anchor FAIL tampered OK (rc=1, anchor-self-inconsistent — known limitation: anchor signing 부재)"
   254	
   255	      - name: Layer 1 inadequacy demo — chain-only mode (의도된 PASS)
   256	        id: layer1_inadequacy
   257	        run: |
   258	          set +e
   259	          python tools/history_anchor_verifier.py --mode chain-only \
   260	            tests/fixtures/history_anchor_verifier/chain_only_demo/full_rewrite_ledger.jsonl \
   261	            > group-c-followup-logs/layer1-demo.stdout 2> group-c-followup-logs/layer1-demo.stderr
   262	          rc=$?
   263	          set -e
   264	          cat group-c-followup-logs/layer1-demo.stderr
   265	          if [ "$rc" -ne 0 ]; then
   266	            echo "::error::Layer 1 inadequacy demo expected rc=0 (의도된 PASS), got rc=$rc"
   267	            echo "::error::만약 rc=1이면 Layer 1 *단독* 으로 full rewrite 검출됨 — 본 PoC evidence 가치 무효화"
   268	            exit 1
   269	          fi
   270	          if ! grep -q "Layer 1 단독으로는 full rewrite" group-c-followup-logs/layer1-demo.stderr; then
   271	            echo "::error::Layer 1 inadequacy NOTE 부재"
   272	            exit 1
   273	          fi
   274	          echo "layer1_inadequacy=PASS" >> $GITHUB_OUTPUT
   275	          echo "Layer 1 inadequacy demo OK (rc=0 의도된 PASS — Layer 5 의무성 evidence)"
   276	
   277	      - name: F-금지 자기 검증 (Layer 1 grep — 실 signed commit / external service / GitHub API 0건)
   278	        id: forbidden_check
   279	        run: |
   280	          set -e
   281	          violations=0
   282	          # F-금지: 실 signed commit / external timestamping 도구 import 0건
   283	          if grep -E "^(import|from)\s+(gnupg|pynacl|sigstore|cosign|tsa|rfc3161)" tools/history_anchor_verifier.py; then
   284	            echo "::error::F-금지 위반 — signed commit / external timestamping 도구 import"
   285	            violations=$((violations+1))
   286	          fi
   287	          # F-금지: 실 HTTP 클라이언트 import 0건
   288	          if grep -E "^(import|from)\s+(requests|httpx|aiohttp|urllib3)" tools/history_anchor_verifier.py; then
   289	            echo "::error::F-금지 위반 — HTTP client import"
   290	            violations=$((violations+1))
   291	          fi
   292	          # F-금지: 실 외부 호출 함수 0건
   293	          if grep -E "requests\.(get|post)|httpx\.(get|post)|urllib\.request\.urlopen|gh\s+api\s+" tools/history_anchor_verifier.py; then
   294	            echo "::error::F-금지 위반 — 실 외부 호출 함수"
   295	            violations=$((violations+1))
   296	          fi
   297	          # F-금지: production data path 0건
   298	          if grep -rE "/home/.*\.claude/|/Users/.*\.claude/|production[_-]" \
   299	               tests/fixtures/history_anchor_verifier/ tools/history_anchor_verifier.py 2>/dev/null; then
   300	            echo "::error::F-금지 위반 — production data path"
   301	            violations=$((violations+1))
   302	          fi
   303	          if [ "$violations" -ne 0 ]; then
   304	            echo "::error::F-금지 자기 검증 FAIL — $violations 위반"
   305	            exit 1
   306	          fi
   307	          echo "forbidden_check=PASS" >> $GITHUB_OUTPUT
   308	          echo "F-금지 자기 검증 OK — 0/7 위반"
   309	
   310	      - name: Build summary.json (Evidence summary 답습)
   311	        if: always()
   312	        run: |
   313	          cat > group-c-followup-logs/summary.json <<EOF
   314	          {
   315	            "list_attack": "${{ steps.list_attack.outputs.list_attack || 'FAIL' }}",
   316	            "anchor_pass_original": "${{ steps.anchor_pass_original.outputs.anchor_pass_original || 'FAIL' }}",
   317	            "anchor_pass_extended": "${{ steps.anchor_pass_extended.outputs.anchor_pass_extended || 'FAIL' }}",
   318	            "anchor_fail_rewrite": "${{ steps.anchor_fail_rewrite.outputs.anchor_fail_rewrite || 'FAIL' }}",
   319	            "anchor_fail_truncation": "${{ steps.anchor_fail_truncation.outputs.anchor_fail_truncation || 'FAIL' }}",
   320	            "anchor_fail_deletion": "${{ steps.anchor_fail_deletion.outputs.anchor_fail_deletion || 'FAIL' }}",
   321	            "anchor_fail_substitution": "${{ steps.anchor_fail_substitution.outputs.anchor_fail_substitution || 'FAIL' }}",
   322	            "anchor_fail_tampered": "${{ steps.anchor_fail_tampered.outputs.anchor_fail_tampered || 'FAIL' }}",
   323	            "layer1_inadequacy_demo": "${{ steps.layer1_inadequacy.outputs.layer1_inadequacy || 'FAIL' }}",
   324	            "forbidden_check": "${{ steps.forbidden_check.outputs.forbidden_check || 'FAIL' }}",
   325	            "f_forbidden_violations": "0/7",
   326	            "escalation_triggers": "0/5",
   327	            "attack_scenarios": "5",
   328	            "total_anchor_fields": "11",
   329	            "anchor_method_supported": "ci_run_id (signed_tag / external_snapshot = 별도 합의)",
   330	            "commit": "${{ github.sha }}",
   331	            "ref": "${{ github.ref }}",
   332	            "run_id": "${{ github.run_id }}",
   333	            "feasibility_scope": "G4 *Layer 5 정적 검출 시제* 한정 — G4 / G2 / G3 / G4 전체 PASS 권한 0건",
   334	            "external_dependencies": "0 (stdlib re + json + dataclasses 단독, signed commit / branch protection / external timestamping 미진입)",
   335	            "evidence_value": "Layer 1 inadequacy demo — chain-only mode 의도된 PASS → Layer 5 의무성 evidence (ADR-012 §2.8 답습)"
   336	          }
   337	          EOF
   338	          cat group-c-followup-logs/summary.json
   339	
   340	      - name: Upload history anchor verifier logs (artifact)

exec
/bin/bash -lc 'gh run view 26557936920 --json databaseId,name,displayTitle,event,status,conclusion,workflowName,headBranch,headSha,createdAt,updatedAt,url,jobs' in /home/delangi/문서/project/category/AI_development_tool
exec
/bin/bash -lc "gh api repos/:owner/:repo/branches/main/protection --jq '{required_contexts: (.required_status_checks.contexts // []), strict: .required_status_checks.strict, allow_force_pushes: .allow_force_pushes.enabled, allow_deletions: .allow_deletions.enabled, required_reviews: .required_pull_request_reviews.required_approving_review_count}'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 345ms:
{"allow_deletions":false,"allow_force_pushes":false,"required_contexts":["guard","verify","feasibility","scan","enforce","defense","validate","bypass-detect"],"required_reviews":0,"strict":true}

 succeeded in 1107ms:
{"conclusion":"success","createdAt":"2026-05-28T06:08:23Z","databaseId":26557936920,"displayTitle":"feat(g4-hash-chain): C-1 timestamp monotonicity FAIL fixture 보강 (E-PA…","event":"push","headBranch":"feature/jarvis-mvp0","headSha":"4c480996cd10313c931bf2906221d5af41f5cdcd","jobs":[{"completedAt":"2026-05-28T06:08:49Z","conclusion":"success","databaseId":78233756904,"name":"enforce","startedAt":"2026-05-28T06:08:27Z","status":"completed","steps":[{"conclusion":"success","name":"Set up job","number":1,"status":"completed"},{"conclusion":"success","name":"Checkout","number":2,"status":"completed"},{"conclusion":"success","name":"Set up Python","number":3,"status":"completed"},{"conclusion":"success","name":"Install jq (POSIX fallback)","number":4,"status":"completed"},{"conclusion":"success","name":"Install Primary 1 + Primary 2 (Q1 합의 R-A2 답습)","number":5,"status":"completed"},{"conclusion":"success","name":"Corpus regression — Primary 1 (rfc8785) byte + sha256","number":6,"status":"completed"},{"conclusion":"success","name":"Corpus regression — Primary 2 (jcs) cross-check (TR-C-2 답습)","number":7,"status":"completed"},{"conclusion":"success","name":"Corpus regression — cross_check mode (Primary 1 ↔ Primary 2 byte equivalence)","number":8,"status":"completed"},{"conclusion":"success","name":"Fallback equivalence — jq -S -c vs Primary 1","number":9,"status":"completed"},{"conclusion":"success","name":"NaN/Inf reject (Q1 합의 C-B8 + 본 합의 C-Q2 답습)","number":10,"status":"completed"},{"conclusion":"success","name":"PASS fixture — jsonl_hash_chain rc=0 (× 2)","number":11,"status":"completed"},{"conclusion":"success","name":"FAIL fixture — jsonl_hash_chain rc=1 + 5 violation_type cover","number":12,"status":"completed"},{"conclusion":"success","name":"Round-trip — T2 strict on PASS fixtures","number":13,"status":"completed"},{"conclusion":"success","name":"Evidence summary","number":14,"status":"completed"},{"conclusion":"success","name":"Post Set up Python","number":27,"status":"completed"},{"conclusion":"success","name":"Post Checkout","number":28,"status":"completed"},{"conclusion":"success","name":"Complete job","number":29,"status":"completed"}],"url":"https://github.com/jokwangwon/AI_development_tool/actions/runs/26557936920/job/78233756904"}],"name":"G4 Hash Chain + JCS","status":"completed","updatedAt":"2026-05-28T06:08:50Z","url":"https://github.com/jokwangwon/AI_development_tool/actions/runs/26557936920","workflowName":"G4 Hash Chain + JCS"}

codex
branch protection은 main 기준 8 contexts와 force push/delete 차단이 실제 API로 확인됐습니다. 반면 local/system `receive.denyNonFastForwards`는 출력 0건, 즉 brief의 2a DEFER 주장은 사실관계상 맞습니다. CI run 상세는 `gh run view`가 아직 반환 중이라 이어서 확인합니다.
exec
/bin/bash -lc 'gh run view 26557460199 --json databaseId,workflowName,status,conclusion,headSha,headBranch,event,createdAt,url,jobs' in /home/delangi/문서/project/category/AI_development_tool
exec
/bin/bash -lc 'gh run view 26557460227 --json databaseId,workflowName,status,conclusion,headSha,headBranch,event,createdAt,url,jobs' in /home/delangi/문서/project/category/AI_development_tool
exec
/bin/bash -lc 'git status --short --branch' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
## feature/jarvis-mvp0...origin/feature/jarvis-mvp0
?? docs/external-review/2026-05-28-mvp2-layer-124-pass-activation-codex-response.md
?? docs/phase0/mvp2-layer-124-pass-activation-brief.md

exec
/bin/bash -lc 'gh run view 26557460197 --json databaseId,workflowName,status,conclusion,headSha,headBranch,event,createdAt,url,jobs' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 1313ms:
{"conclusion":"success","createdAt":"2026-05-28T05:54:19Z","databaseId":26557460199,"event":"push","headBranch":"feature/jarvis-mvp0","headSha":"052e5833abd96ccd7f5d764a7dd66e271ffc122c","jobs":[{"completedAt":"2026-05-28T05:54:46Z","conclusion":"success","databaseId":78232229256,"name":"enforce","startedAt":"2026-05-28T05:54:21Z","status":"completed","steps":[{"conclusion":"success","name":"Set up job","number":1,"status":"completed"},{"conclusion":"success","name":"Checkout","number":2,"status":"completed"},{"conclusion":"success","name":"Set up Python","number":3,"status":"completed"},{"conclusion":"success","name":"Install jq (POSIX fallback)","number":4,"status":"completed"},{"conclusion":"success","name":"Install Primary 1 + Primary 2 (Q1 합의 R-A2 답습)","number":5,"status":"completed"},{"conclusion":"success","name":"Corpus regression — Primary 1 (rfc8785) byte + sha256","number":6,"status":"completed"},{"conclusion":"success","name":"Corpus regression — Primary 2 (jcs) cross-check (TR-C-2 답습)","number":7,"status":"completed"},{"conclusion":"success","name":"Corpus regression — cross_check mode (Primary 1 ↔ Primary 2 byte equivalence)","number":8,"status":"completed"},{"conclusion":"success","name":"Fallback equivalence — jq -S -c vs Primary 1","number":9,"status":"completed"},{"conclusion":"success","name":"NaN/Inf reject (Q1 합의 C-B8 + 본 합의 C-Q2 답습)","number":10,"status":"completed"},{"conclusion":"success","name":"PASS fixture — jsonl_hash_chain rc=0 (× 2)","number":11,"status":"completed"},{"conclusion":"success","name":"FAIL fixture — jsonl_hash_chain rc=1 + 4 violation_type cover","number":12,"status":"completed"},{"conclusion":"success","name":"Round-trip — T2 strict on PASS fixtures","number":13,"status":"completed"},{"conclusion":"success","name":"Evidence summary","number":14,"status":"completed"},{"conclusion":"success","name":"Post Set up Python","number":27,"status":"completed"},{"conclusion":"success","name":"Post Checkout","number":28,"status":"completed"},{"conclusion":"success","name":"Complete job","number":29,"status":"completed"}],"url":"https://github.com/jokwangwon/AI_development_tool/actions/runs/26557460199/job/78232229256"}],"status":"completed","url":"https://github.com/jokwangwon/AI_development_tool/actions/runs/26557460199","workflowName":"G4 Hash Chain + JCS"}

 succeeded in 1346ms:
{"conclusion":"success","createdAt":"2026-05-28T05:54:19Z","databaseId":26557460227,"event":"push","headBranch":"feature/jarvis-mvp0","headSha":"052e5833abd96ccd7f5d764a7dd66e271ffc122c","jobs":[{"completedAt":"2026-05-28T05:54:29Z","conclusion":"success","databaseId":78232229270,"name":"defense","startedAt":"2026-05-28T05:54:21Z","status":"completed","steps":[{"conclusion":"success","name":"Set up job","number":1,"status":"completed"},{"conclusion":"success","name":"Checkout","number":2,"status":"completed"},{"conclusion":"success","name":"Set up Python","number":3,"status":"completed"},{"conclusion":"success","name":"Install Group C deps (rfc8785 + jcs — Group C `parse_jsonl` 의존)","number":4,"status":"completed"},{"conclusion":"success","name":"Prepare log directory (artifact 답습)","number":5,"status":"completed"},{"conclusion":"success","name":"--list-defenses self-check","number":6,"status":"completed"},{"conclusion":"success","name":"L2 PASS — append-only commit history (rc=0 + violations=0)","number":7,"status":"completed"},{"conclusion":"success","name":"L2 FAIL — force-push + reorder (rc=1 + 2 patterns cover)","number":8,"status":"completed"},{"conclusion":"success","name":"L3 PASS — safe commands (rc=0 + violations=0)","number":9,"status":"completed"},{"conclusion":"success","name":"L3 FAIL — dangerous commands (rc=1 + 4 patterns cover)","number":10,"status":"completed"},{"conclusion":"success","name":"L4 PASS — head extends base (rc=0 + violations=0)","number":11,"status":"completed"},{"conclusion":"success","name":"L4 FAIL — line deletion + in-place rewrite (rc=1 + 2 patterns cover)","number":12,"status":"completed"},{"conclusion":"success","name":"F-금지 자기 검증 (Layer 1 grep — 실 git command / GitHub API / production data 0건)","number":13,"status":"completed"},{"conclusion":"success","name":"Build summary.json (Evidence summary 답습)","number":14,"status":"completed"},{"conclusion":"success","name":"Upload rewrite defense logs (artifact)","number":15,"status":"completed"},{"conclusion":"success","name":"Evidence summary","number":16,"status":"completed"},{"conclusion":"success","name":"Post Set up Python","number":31,"status":"completed"},{"conclusion":"success","name":"Post Checkout","number":32,"status":"completed"},{"conclusion":"success","name":"Complete job","number":33,"status":"completed"}],"url":"https://github.com/jokwangwon/AI_development_tool/actions/runs/26557460227/job/78232229270"}],"status":"completed","url":"https://github.com/jokwangwon/AI_development_tool/actions/runs/26557460227","workflowName":"G4 Rewrite Defense (Layer 2/3/4)"}

 succeeded in 1563ms:
{"conclusion":"success","createdAt":"2026-05-28T05:54:19Z","databaseId":26557460197,"event":"push","headBranch":"feature/jarvis-mvp0","headSha":"052e5833abd96ccd7f5d764a7dd66e271ffc122c","jobs":[{"completedAt":"2026-05-28T05:54:29Z","conclusion":"success","databaseId":78232229287,"name":"verify","startedAt":"2026-05-28T05:54:21Z","status":"completed","steps":[{"conclusion":"success","name":"Set up job","number":1,"status":"completed"},{"conclusion":"success","name":"Checkout","number":2,"status":"completed"},{"conclusion":"success","name":"Set up Python","number":3,"status":"completed"},{"conclusion":"success","name":"Install Group C deps (rfc8785 + jcs — Group C `compute_entry_hash` 의존)","number":4,"status":"completed"},{"conclusion":"success","name":"Prepare log directory (artifact 답습)","number":5,"status":"completed"},{"conclusion":"success","name":"--list-attack-models self-check","number":6,"status":"completed"},{"conclusion":"success","name":"Anchor PASS — original (rc=0 + violations=0)","number":7,"status":"completed"},{"conclusion":"success","name":"Anchor PASS — extended append (rc=0 + violations=0)","number":8,"status":"completed"},{"conclusion":"success","name":"Anchor FAIL — full rewrite (rc=1 + tail_hash_mismatch)","number":9,"status":"completed"},{"conclusion":"success","name":"Anchor FAIL — tail truncation (rc=1 + entry_count + tail_hash)","number":10,"status":"completed"},{"conclusion":"success","name":"Anchor FAIL — middle deletion (rc=1 + entry_count + tail_hash)","number":11,"status":"completed"},{"conclusion":"success","name":"Anchor FAIL — substitution (rc=1 + tail_hash + genesis_hash)","number":12,"status":"completed"},{"conclusion":"success","name":"Anchor FAIL — tampered anchor (rc=1 + anchor_self_inconsistent — known limitation)","number":13,"status":"completed"},{"conclusion":"success","name":"Layer 1 inadequacy demo — chain-only mode (의도된 PASS)","number":14,"status":"completed"},{"conclusion":"success","name":"F-금지 자기 검증 (Layer 1 grep — 실 signed commit / external service / GitHub API 0건)","number":15,"status":"completed"},{"conclusion":"success","name":"Build summary.json (Evidence summary 답습)","number":16,"status":"completed"},{"conclusion":"success","name":"Upload history anchor verifier logs (artifact)","number":17,"status":"completed"},{"conclusion":"success","name":"Evidence summary","number":18,"status":"completed"},{"conclusion":"success","name":"Post Set up Python","number":35,"status":"completed"},{"conclusion":"success","name":"Post Checkout","number":36,"status":"completed"},{"conclusion":"success","name":"Complete job","number":37,"status":"completed"}],"url":"https://github.com/jokwangwon/AI_development_tool/actions/runs/26557460197/job/78232229287"}],"status":"completed","url":"https://github.com/jokwangwon/AI_development_tool/actions/runs/26557460197","workflowName":"G4 History Anchor Verifier (Layer 5)"}

exec
/bin/bash -lc 'rg -n "58번째|59번째|26557936920|26557460199|4c48099|6ebc634|violation_type|timestamp_monotonicity" docs/sessions/SESSION_2026-05-28.md' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
93:- N-A-1: `tools/jsonl_hash_chain.py` (genesis hash + 4 violation_type) + `tools/canonical_json.py` + `tests/canonical/` 24 fixtures + `g4-hash-chain.yml` **PoC 시제 이미 운영 중** → brief §2.2.2 "❌ gap" 4 row → "⚠️ PoC 시제 충족 / PASS 시제 미충족" 격상
351:⭐⭐ **조건부 승인 조건 6** (실 구현 sub-cycle 우선 처리): denyNonFastForwards 활성화 + R-6 actual run + 4 G4 workflow actual run + R-S1 정정 평가 + violation_type 정밀화 + Layer subsection 분리.
390:| 5 ⭐ | **실 구현 sub-cycle** — 조건부 승인 조건 6 우선 처리 (denyNonFastForwards (c)+(d) 활성화 + R-6 actual run + 4 G4 workflow actual run + violation_type 정밀화 + history_rewrite fixture 추가 + Layer subsection 분리) | **큰 cycle (다단계)** | 수단별 차등 |
467:| 2 | ⭐ **실 구현 sub-cycle** — 조건부 승인 조건 6 우선: denyNonFastForwards (c)+(d) 활성화 + R-6 actual run + 4 G4 workflow actual run + violation_type 정밀화 + history_rewrite fixture 추가 + Layer subsection 분리 | 실 코드/CI 진전 | 수단별 차등 | **2순위 ((β) 후)** |
557:| 1 | ⭐ **실 구현 sub-cycle** (조건부 승인 조건 6+1: denyNonFastForwards 활성화 + R-6 actual run + 4 G4 workflow run + **R-3 secret-hygiene actual run** + violation_type(HISTORY_REWRITE emission) 정밀화 + history_rewrite fixture + Layer subsection) | 실 코드/CI 진전 | 수단별 차등 |
583:## 58번째 entry — ⭐ 실 구현 sub-cycle (1) violation_type 정밀화: HISTORY_REWRITE Layer 1 제거 (TDD, MVP-2 첫 실제 코드 변경)
587:### 결과 요약 (58번째 entry)
589:⭐ **MVP-2 영역 첫 실제 코드 변경 발효** (51~57 entry = 모두 합의/결정 문서, 본 entry = 첫 src/tools 본문 변경). 57 (β) 결정 발효 답습 — 조건부 승인 조건 6+1 中 조건 4 (violation_type 정밀화) 실 구현.
594:- **W-F 보존 답습**: `.github/workflows/*.yml` 본문 변경 0 (g4-hash-chain.yml "4 violation_type cover" = 4 FAIL fixture [prev_hash + hash_recalc + schema_missing_field + genesis], history_rewrite 미참조 → 변경 불필요)
596:**조건부 승인 조건 6+1 진행 상태**: 조건 4 (violation_type 정밀화) ✅ 본 entry / 조건 1 (denyNonFastForwards) = DEFER (비례 보안) / 조건 5 (history_rewrite fixture) = Layer 2 이미 포괄 (full_rewrite + middle_deletion + substitution + tail_truncation 8 fixtures, 신규 불필요) / 조건 2 (R-6 r2-canary actual run) + 3b (R-3 secret-hygiene actual run) = path 불일치 미트리거 (별도 path 변경/schedule 시) / 조건 3 (4 G4 workflow actual run) = 본 push 로 **3/4 트리거** (g4-hash-chain + history-anchor-verifier + rewrite-defense, jsonl_hash_chain.py path 의존) / 조건 6 (Layer subsection) = Layer 통합 PASS 발효 cycle 영역.
598:**원칙 준수**: `src/` 0 / `tools/` 1 (jsonl_hash_chain.py violation_type 정밀화 한정) / `.github/workflows/` 0 (W-F 보존) / `tests/` 1 신규 (tools pytest 커버리지 0→신규) / denyNonFastForwards 활성화 0 (DEFER) / ADR·헌법·roadmap·governance·G4·ADR-012 본문 0 / 신규 외부 library 도입 0 (rfc8785/jcs venv 설치 = 로컬 test 실행 한정, requirements-dev 기존 답습) / Layer 통합 PASS 발효 0 / MVP-2 PASS 발효 0 / Hermes import 0 / facade real 0 / 자동 후속 진입 0.
600:### 흐름 (58번째 entry)
611:| ⭐ CI actual run capture (조건 3) | **3 G4 workflow 전원 success** — g4-hash-chain `26557460199` + rewrite-defense `26557460227` + history-anchor-verifier `26557460197` (+ boundary-guard + schema-validation + memory-skill-feasibility + pc-1-t3 모두 success = 7/7). violation_type 정밀화가 hash chain 검증 무파괴 입증 (E-PASS-8 증거, 42 entry actual run id 답습) | — |
613:### carry-over (58번째 entry)
615:**해소**: ✅ 57 entry 다음 단계 #1 실 구현 sub-cycle 조건 4 (violation_type 정밀화)
623:### 변경 매트릭스 (58번째 entry)
629:| `docs/sessions/SESSION_2026-05-28.md` | 58번째 entry 추가 |
630:| `docs/INDEX.md` | 58번째 entry 등록 |

exec
/bin/bash -lc "rg -n \"Layer 4|§4\\.4|Layer 1|Layer 2|Layer 3|Layer 5\" docs/architecture/provider-agnostic-memory-skill-design.md | head -80" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
9:> **PR-2 보강 흡수 (2026-05-09 풀 3+1 합의 + 외부 LLM 2건)**: **§4.2 schema 11 필드 (10 → 10 + `event` 신규) + §4.4 hash chain 사양 보강 (Layer 1~5 다층 강제 + RFC 8785 JCS Primary + fallback + Genesis Hash + prev_hash 검증 실패 BLOCK + manual + Full Rewrite 5 Layer 방어) + §4.6 round-trip 검증 절차 보강 (Tier-based + 3 ledger entry 형식 + Migration 검증 실패 rollback 조건) — `docs/decisions/ADR-012-evidence-ledger-protection.md` 와 동일 PR commit. 합의 권위: `docs/review/3plus1-consensus-2026-05-09-pr2-evidence-ledger.md` (5/5 입력 APPROVE WITH CONDITIONS). G4 §11.4 P-1 (RFC 8785 JCS) + P-2 (schema 진화 정책) + P-3 (import schema_version) 처리 완료** — P-4 / P-5 는 PR-1 또는 후속 합의 영역 (PR-1 §11.4 답습).
11:> **ADR-012 (Evidence Ledger Protection) Mandatory Reference (2026-05-09 후속 3 PR-2 신규 발행)**: 본 G4 §4.2 11 필드 schema (`event` 신규) + §4.4 hash chain 사양 (Layer 1~5 + RFC 8785 JCS Primary + Genesis Hash + prev_hash 검증 실패 BLOCK + Full Rewrite 5 Layer) + §4.6 round-trip 검증 절차 (Tier-based + 3 ledger entry 형식 + Migration rollback) 의 *권위 출처*. **G4 §4 = ADR-012 §2.1 ~ §3.5 답습 권위**.
13:> **Gate Enforcement Layer 보호 cross-reference (2026-05-12)**: 본 G4 §3.7.3 #18 (`GATE_ENFORCEMENT_LAYER_MODIFY` T3) + §3.8.2 #10 (`gate_enforcement_bypass_detected` rollback_trigger) + §6.1 매트릭스 row + 인터페이스 Layer 4 신설 = **G3 §2.6 권위 정의 답습 cross-reference 한정**. *권위 정의 = G3 §2.6* (Gate 자체 5 기준 + Layer 0~6 5 기준 + 위협 모델 TM-1~TM-8 + 10 보호 항목 매트릭스 + Rollback Trigger 발화 매트릭스). 본 G4 = Skill permission schema 차원 연결 한정 — **Skill permission 이 `WRITE_CODE` / `RUN_LOCAL_TOOLS` (T2) 를 갖더라도 Gate definition / Gate verdict / Evidence ledger / CI policy 변경 권한은 자동 포함되지 *않는다*** (§3.7.3 #18 = T3 `forbidden_actions` 자동 포함 강제). 본 cross-reference 흡수 = G4 Design/Governance Gate PASS 권위 변경 0건. 본 §11.6 답습.
15:> **P2 v3 (`hermes-adoption-design-v3.md`) = Adopted (Design Adoption only, 2026-05-09 후속 6)** 후속 권위. 본 G4 = P2 v3 §6 (G4 정의 + ADR-012 Mandatory Reference cross-reference) + §10.1 #1 (Provider Liquidity 5-way Multi-layer Defense 5 Layer — 본 G4 §3.5 + §4.3 Layer 3/4 + ADR-012 §원칙 6 Layer 5) + §10.2 Archive Migration Note + §11.1 Hermes PMO 격상 전 인간 전문 리뷰 의무화 답습.
25:**§4 hash chain 보강 합의**: `docs/review/3plus1-consensus-2026-05-09-pr2-evidence-ledger.md` (PR-2 풀 3+1 + 외부 LLM 2건 — ADR-012 발행 + G4 §4.2/§4.4/§4.6 보강, 2026-05-09 후속 3 PR-2)
27:**상위 권위**: 헌법 제5조-2 관용 (Provider Liquidity, 비협상), 헌법 제8조 (보안), ADR-008 차단조건 #2 (JSONL export 표준), **ADR-009 C-N §5 (Provider Liquidity 5-way Multi-layer Defense 모법 ADR Layer 1, 2026-05-09 후속 4 갱신)**, **ADR-012 §원칙 5 + §원칙 6 (Provider Liquidity 5-way Layer 5 — Evidence 형식 차원 provider-neutral 강제)**
56:8. ❌ **실 migration script 구현** — `scripts/hermes-migration/hermes_to_claude.py` 등 사양까지만 (§4.4)
68:| 4 | G4 PASS 합의 가동 (단축 또는 풀 3+1 / **G3 §4.4.2 답습** — 외부 LLM 의견 권장) | `docs/review/3plus1-consensus-YYYY-MM-DD-g4.md` | 단계 3 완료 후 |
535:| 8 | `chain_violation_detected` | Evidence Ledger hash chain 위반 (§4.4.4 답습) | 모든 T1+T2 권한 자동 revoke + Skill 완전 비활성화 | 사용자 명시 review + ADR-012 §2.7 답습 |
537:| 10 | `gate_enforcement_bypass_detected` (**G3 §2.6 cross-reference — 2026-05-12**) | Gate enforcement layer 우회 검출 — Gate 정의 변경 / Gate verdict 변조 / Evidence ledger `event: gate_pass` forge / Gate 순서 skip / Layer 1~4 결과 silent override / Hook 비활성화 / Skill 통한 Gate enforcement 우회 / Memory 통한 Gate verdict 대체 (G3 §2.6 위협 모델 TM-1 ~ TM-8 통합 trigger) | 모든 T1+T2 권한 자동 revoke + Skill 완전 비활성화 | 사용자 명시 review + G3 §2.6.5 답습 (Hermes 컨테이너 정지 + audit log + Gate enforcement 분석) + ADR-008 부록 C §C.2 답습 |
605:| `prev_hash` | string (sha256) | ✅ | 직전 entry 의 `hash` (chain 형성) — 첫 entry 는 `genesis_hash` (§4.4) |
617:| 표준 도구로 검증 가능 | `jq` 로 parse + sha256 검증 + canonical JSON 검증 가능 (RFC 8785 reference output 동등성, §4.4.2 답습) | POSIX 표준 + RFC 8785 |
625:> **ADR-012 §2.3~§2.8 갱신**: 본 §4.4 = ADR-012 §2.3 (Append-only + Hash Chain 다층 강제) + §2.5 (RFC 8785 JCS) + §2.6 (Genesis Hash) + §2.7 (prev_hash 검증 실패 처리) + §2.8 (Full Rewrite 방어) 답습. 이전 (보강 전) "둘 중 하나 의무" 약 사양 → 다층 강제 사양 + canonical JSON 표준 인용 + 실패 처리 + full rewrite 방어 명시.
627:> **P-1 흡수 완료** (2026-05-11): G4 DRAFT 검토 §3.1 P-1 (자기 발견 잠재 위험 — "JSON canonicalization 표준은 RFC 8785 (JCS) 등 명시 표준 존재. 본 초안은 JCS 직접 인용 안 함") 흡수 완료. **canonical JSON 표준 = RFC 8785 (JCS) IETF informational track 명시 인용** — §4.4.2 Primary 정의 + ADR-012 §2.5 권위. 본 §4.4 의 모든 hash 계산은 RFC 8785 (https://www.rfc-editor.org/rfc/rfc8785) 기준 canonical 형식에 SHA-256 적용. fallback (RFC 8259 escape + lex sort + `jq -S -c` 등) 은 RFC 8785 reference output 동등성 의무 (§4.4.2 답습).
629:#### 4.4.1 다층 강제 (Layer 1 ~ Layer 5)
631:**Layer 1 — Hash Chain (MANDATORY 모든 환경)**:
634:- 첫 entry 의 `prev_hash` = `genesis_hash` (§4.4.3)
638:**Layer 2 — Git Append-only Branch (MANDATORY)**:
644:**Layer 3 — Signed Commit (RECOMMENDED MVP, MANDATORY multi-host)**:
649:**Layer 4 — CI 회귀 검증 (MANDATORY)**:
650:- Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증
655:**Layer 5 — External Anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)**:
660:**사용자 명시 옵션 답습 (D-1, ADR-012 §2.4)**: "signed commit OR git append commit (둘 중 하나) 의무" — 사용자 결정 영역. 5/5 입력 권고는 *다층 동시 의무* (Layer 1 + 2 MANDATORY, Layer 3 RECOMMENDED). **본 §4.4 = Layer 1 + Layer 2 MANDATORY 답습** (D-1A / D-1B / D-1C 모두 호환).
682:**참고 (이전 정의 — 보강 전)**: lex sort + RFC 8259 escape + IEEE 754 numeric — 본 정의는 fallback 동등 보장의 *최소 기준*. 본 §4.4.2 갱신으로 RFC 8785 JCS 우선 채택.
720:- Layer 1: pre-commit hook (입력 entry 의 `prev_hash` 검증)
721:- Layer 2: pre-push hook (chain 전체 재검증)
722:- Layer 3: CI nightly 회귀 검증 (R-6 답습 확장)
723:- Layer 4: import script (`scripts/hermes-migration/import.py` — 향후 Implementation 시점)
727:**Layer 1**: Hash chain (middle entry tampering 차단)
728:**Layer 2**: Git append-only branch + denyNonFastForwards (history 재작성 차단)
729:**Layer 3**: pre-commit hook — `git rebase` / `git filter-branch` / `git reset --hard` 감지 시 reject
730:**Layer 4**: CI 회귀 검증 — base branch 대비 JSONL line deletion / rewrite 감지
731:**Layer 5 (RECOMMENDED MVP, MANDATORY multi-host)**: External anchor — GitHub Actions run ID + signed tag 또는 월 1회 external snapshot
735:> 동일 호스트 전체 침해 상황은 본 ADR-012 의 완전 방어 범위 밖이다. 본 ADR / 본 §4.4 는 Hermes container compromise, middle-entry tampering, accidental rewrite, migration 손실, evidence forgery 시도에 대한 탐지와 차단을 목표로 한다.
758:- canonical JSON RFC 8785 (JCS) 기준 (§4.4.2 답습)
778:- §4.6.5 #4 + §4.4.2 답습
781:- 검증 실패 → BLOCK + `event: chain_violation_detected` ledger entry (§4.4.4 답습) + 사용자 명시 review
821:       │ ③ canonical JSON sha256 비교 (RFC 8785 JCS — §4.4.2 답습)
859:4. Hash chain 검증 (§4.4.4 답습, §4.5.3 Step 3)
947:- **Layer 1 (schema-level)** — G4 §3.7 13-category enum (12 Permission Granularity + 1 Gate Enforcement #18) + §3.2 #9/#10 schema validation 필드 *정의* + T3 8-category 자동 차단 *형식*
948:- **Layer 2 (self-escalation)** — G4 §3.8.1 6 차단 메커니즘 *규칙* + §3.8.2 10 rollback_trigger × revoke 매트릭스 *연결* (9 Permission Granularity + 1 Gate Enforcement #10)
949:- **Layer 3 (runtime)** — G3 §3.3 wrapper + sandbox + audit log + 자동 revoke *runtime 강제*
950:- **Layer 4 (Gate Enforcement)** — **G3 §2.6** 권위 정의 (Gate 정의 / verdict / evidence / sequence / failure override + Layer 0~6 enforcement mechanism 보호) — G4 §3.7.3 #18 + §3.8.2 #10 cross-reference
979:| Hash chain 변조 방지 | ✅ §4.4 (G4 형식) | ✅ G3 §1.3 (운영 강제) |
1008:| Hash chain 변조 방지 | ✅ §4.4 | ✅ G3 §3.1 |
1042:| Hash chain 변조 방지 | (위임) | ✅ §4.4 |
1085:| (iv) | JSONL export / import 형식 정의 완료 | §4.1 + §4.2 + §4.4 | ✅ |
1163:| §4.4 hash chain 변조 방지 본문 갱신 | **풀 3+1 합의 + ADR Amendment 절차** (T3 변경 — Evidence 무결성 핵심) |
1167:| **DRAFT 상태 해제 → 정식 채택** | **단축 합의 또는 풀 3+1 합의 APPROVE** + 각 § (a)~(e) 충족 검증 + 외부 LLM 의견 권장 (G3 §4.4.2 답습) |
1184:| **`hash_algo` 변경** (예: SHA-256 → SHA-3) | MAJOR (전 chain 영향) | **풀 3+1 합의 + ADR Amendment 절차** | 새 chain 생성 (§4.4.3 Genesis 답습) + 구 chain read-only + 외부 LLM 의견 의무 |
1217:- 본 초안은 *자기 작성 산출* (P2 v3 / G2 / G3 / G4 모두 동일 컨텍스트). **G3 §4.4.2 답습**: 자기 작성 산출 검증은 외부 LLM 의견 *권장* — 본 초안 정식 채택 시점에 외부 LLM 의견 의무화 가능.
1220:- ~~§4.4 canonical JSON 정의 — JSON canonicalization 표준은 RFC 8785 (JCS) 등 명시 표준 존재. 본 초안은 JCS 직접 인용 안 함 (간단 명시 한정). 정식 채택 시 JCS RFC 인용 권고.~~ **✅ 흡수 완료** (2026-05-11 P-1, §4.4 헤더 + §4.4.2 본문 RFC 8785 IETF 직접 인용 — `https://www.rfc-editor.org/rfc/rfc8785` + ADR-012 §2.5 권위. fallback 동등성 의무 + test corpus 의무 + canonical_json_fallback ledger entry 의무).
1260:| **P-1** | §11.1 자기 명시 한계 — RFC 8785 JCS 미인용 (self-disclosed) | PR-2 풀 3+1 (§4.4.2 본문) + **2026-05-11 §4.4 헤더 / §11.1 갱신** | §4.4 헤더 P-1 흡수 완료 명시 + §4.4.2 본문 RFC 8785 IETF 직접 인용 (`https://www.rfc-editor.org/rfc/rfc8785`) + ADR-012 §2.5 권위 + fallback 동등성 의무 + canonical_json_fallback ledger entry 의무 + §11.1 자기 명시 한계 strikethrough + 흡수 완료 표기 | ✅ **RESOLVED** (2026-05-11) |
1293:- Layer 1: G2 GP-5 (depcruise 룰 + P1 facade 단일 진입점) — *모든 작성 주체* 의 코드 lock-in 차단
1294:- Layer 2: G3 §6.4 (Hermes-originated lock-in 변경 시도 차단) — *Hermes 작성 주체* 한정
1295:- Layer 3: G4 §3.5 (`provider_bindings` schema *required*/*exclusive* 금지) — *Skill 메타데이터* 차원
1296:- Layer 4: G4 §4.3 (JSONL Hermes 의존 0 + 최소 2 provider 재해석 가능) — *export format* 차원
1302:**[Cross-reference Block — (g1-N-3-pamsd) HIGH carry-over, R-7 (vi-γ) 답습]**: 본 §11.4.2 "Provider Liquidity 4-way Multi-layer Defense" 명명 = 헌법-동급 권위 (R-S4 (g1-N-3) 답습). (g1-N-1) commit `148fbbe` 후 **헌법 제5조-2 (Provider Liquidity, 비협상) line 75~80** 직접 모법 발효 — Layer 1~4 모두 헌법 제5조-2 line 80 "본 원칙은 비협상 — ADR-011 line 6 상위 권위 매핑 답습" 답습 형식 직접 활용 자격. 본문 verbatim 변경 0건 (R-7 (vi-α) 사전 기각 + (vi-β) DEFER 양립, (vi-γ) cross-reference 추가만 채택).
1312:| G3 P-3 | §4.4.2 외부 LLM 권장/필수 적용 시점 명확화 | 본 PR-1 G3 §4.7 (C-E 흡수와 *동시*) — 메타-순환 청산 §4.7.1 (a) | §4.7.1 (a) |
1319:- ~~❌ §4.4 RFC 8785 JCS 본문 인용 (PR-2 풀 3+1 영역 — C-G 흡수와 *동시*)~~ **✅ 흡수 완료** (2026-05-09 PR-2 §4.4.2 + 2026-05-11 §4.4 헤더 / §11.1 보강)
1393:| 3 | §6.1 매트릭스 row + Layer 4 신설 | §6.1 표 row 추가 + 인터페이스 본문 (3-layer → 4-layer Gate Enforcement Layer 추가) | G3 §2.6 = Layer 4 (Gate Enforcement Layer) 권위 정의 명시 cross-reference | ✅ **RESOLVED** (2026-05-12) |
1409:- ❌ **hook 구현** — pre-commit / pre-push / Husky / Layer 1~4 자동 차단 hook 본문 (Implementation 영역)

exec
/bin/bash -lc "sed -n '620,670p' docs/architecture/provider-agnostic-memory-skill-design.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:

**P-3 흡수 완료** (2026-05-11): G4 DRAFT 검토 §3.1 P-3 (자기 발견 잠재 위험 — "§4.5 외부 형식 → 본 G4 import 시 schema_version 호환성 (§4.3 #3) — 호환 부재 시 처리 절차 부재") 흡수 완료. **schema_version declaration 절차 = T2 사용자 명시 승인 + §10.2 합의 절차 + §4.5.3 정밀 import 검증 단계**. 본 절차 충족 *전* import = BLOCK (§4.6.5 #1~#3 답습).

### 4.4 Hash Chain 변조 방지 (**ADR-012 §2.3 + §2.5 + §2.6 + §2.7 + §2.8 답습 — 2026-05-09 PR-2 풀 3+1 합의 보강 + 2026-05-11 P-1 흡수 완료**)

> **ADR-012 §2.3~§2.8 갱신**: 본 §4.4 = ADR-012 §2.3 (Append-only + Hash Chain 다층 강제) + §2.5 (RFC 8785 JCS) + §2.6 (Genesis Hash) + §2.7 (prev_hash 검증 실패 처리) + §2.8 (Full Rewrite 방어) 답습. 이전 (보강 전) "둘 중 하나 의무" 약 사양 → 다층 강제 사양 + canonical JSON 표준 인용 + 실패 처리 + full rewrite 방어 명시.
>
> **P-1 흡수 완료** (2026-05-11): G4 DRAFT 검토 §3.1 P-1 (자기 발견 잠재 위험 — "JSON canonicalization 표준은 RFC 8785 (JCS) 등 명시 표준 존재. 본 초안은 JCS 직접 인용 안 함") 흡수 완료. **canonical JSON 표준 = RFC 8785 (JCS) IETF informational track 명시 인용** — §4.4.2 Primary 정의 + ADR-012 §2.5 권위. 본 §4.4 의 모든 hash 계산은 RFC 8785 (https://www.rfc-editor.org/rfc/rfc8785) 기준 canonical 형식에 SHA-256 적용. fallback (RFC 8259 escape + lex sort + `jq -S -c` 등) 은 RFC 8785 reference output 동등성 의무 (§4.4.2 답습).

#### 4.4.1 다층 강제 (Layer 1 ~ Layer 5)

**Layer 1 — Hash Chain (MANDATORY 모든 환경)**:
- `prev_hash` = 직전 entry 의 `hash` (chain 형성)
- `hash` = 본 entry 의 canonical JSON sha256
- 첫 entry 의 `prev_hash` = `genesis_hash` (§4.4.3)
- SHA-256 hardcode (schema_version 0.1) — `hash_algo` 필드 후속 격상 영역 (ADR-012 §3.2 답습)
- JSONL append-only — entry 수정 / 삭제 / 재작성 금지 (T3 영역, ADR-011 §2.4)

**Layer 2 — Git Append-only Branch (MANDATORY)**:
- `git config receive.denyNonFastForwards true` (force-push 차단)
- branch protection rule
- pre-commit hook: `git rebase` / `git filter-branch` / `git reset --hard` 감지 시 reject (T3 자동 *방어* 권한, T3 자동 *변경* 금지의 비대칭 활용 — ADR-012 §2.8 답습)
- CI 회귀 검증: base branch 대비 JSONL line deletion / rewrite 감지

**Layer 3 — Signed Commit (RECOMMENDED MVP, MANDATORY multi-host)**:
- GPG / SSH key signed commit
- 1인 동일 호스트 = SHOULD (G3 §5.5 SPOF 면책)
- Multi-host 전환 / 외부 공유 / 팀 사용 / Hermes PMO 격상 시점 = MUST 승격 (G3 §5.5.3 트리거 답습)

**Layer 4 — CI 회귀 검증 (MANDATORY)**:
- Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증
- canonical JSON 위반 검출
- timestamp monotonicity 검증 (ADR-012 §3.4)
- R-6 workflow (`.github/workflows/r2-canary.yml`) 답습 확장 (별도 PR — Implementation 영역)

**Layer 5 — External Anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)**:
- 월 1회 external snapshot (별도 외부 git remote / cloud storage push)
- GitHub Actions run ID + signed tag (ADR-012 §2.8 답습)
- 1인 SPOF 완화 + 침해 후 발견 가능

**사용자 명시 옵션 답습 (D-1, ADR-012 §2.4)**: "signed commit OR git append commit (둘 중 하나) 의무" — 사용자 결정 영역. 5/5 입력 권고는 *다층 동시 의무* (Layer 1 + 2 MANDATORY, Layer 3 RECOMMENDED). **본 §4.4 = Layer 1 + Layer 2 MANDATORY 답습** (D-1A / D-1B / D-1C 모두 호환).

#### 4.4.2 Canonical JSON — RFC 8785 JCS Primary + Fallback

**Primary**: **RFC 8785 JCS** (https://www.rfc-editor.org/rfc/rfc8785) — *informational track*, IETF 권위.

**Fallback**: `jq -S -c` (lex sort + compact + UTF-8 + RFC 8259 escape) 또는 자체 구현 동등성 의무 + test corpus 검증 (ADR-012 §2.5 답습).

**구현 라이브러리 후보**:
- Python: `pyjcs` / `rfc8785` / 또는 stdlib `json.dumps(sort_keys=True, separators=(",",":"))` 동등 보장
- Node: `canonicalize` npm

exec
/bin/bash -lc 'find tests/fixtures/rewrite_defense -type f | sort' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
tests/fixtures/rewrite_defense/append_only/fail/force_push/commit_history_after.txt
tests/fixtures/rewrite_defense/append_only/fail/force_push/commit_history_before.txt
tests/fixtures/rewrite_defense/append_only/fail/reorder/commit_history_after.txt
tests/fixtures/rewrite_defense/append_only/fail/reorder/commit_history_before.txt
tests/fixtures/rewrite_defense/append_only/pass/commit_history_after.txt
tests/fixtures/rewrite_defense/append_only/pass/commit_history_before.txt
tests/fixtures/rewrite_defense/line_regression/fail/line_deletion/base.jsonl
tests/fixtures/rewrite_defense/line_regression/fail/line_deletion/head.jsonl
tests/fixtures/rewrite_defense/line_regression/fail/line_rewrite/base.jsonl
tests/fixtures/rewrite_defense/line_regression/fail/line_rewrite/head.jsonl
tests/fixtures/rewrite_defense/line_regression/pass/base.jsonl
tests/fixtures/rewrite_defense/line_regression/pass/head.jsonl
tests/fixtures/rewrite_defense/rewrite_command/fail/git_command_log_filter_branch.txt
tests/fixtures/rewrite_defense/rewrite_command/fail/git_command_log_push_force.txt
tests/fixtures/rewrite_defense/rewrite_command/fail/git_command_log_rebase.txt
tests/fixtures/rewrite_defense/rewrite_command/fail/git_command_log_reset_hard.txt
tests/fixtures/rewrite_defense/rewrite_command/pass/git_command_log_safe.txt

codex
CI run IDs는 모두 success입니다. 한 가지 평가 포인트는 `history-anchor-verifier.yml`가 실제로 “Layer 5” workflow 이름/성격을 갖고 있어, Layer 2 evidence로만 쓰면 과장될 수 있다는 점입니다. 다만 이번 brief는 이를 “Layer 5 결정 영역 진입”이 아니라 history rewrite 검출 보조 evidence로 제한해 설명하고 있어 blocking까지는 아닙니다.
exec
/bin/bash -lc 'PYTHONPATH=tools python tools/jsonl_hash_chain.py tests/fixtures/jsonl_ledger/fail/timestamp_monotonicity.jsonl' in /home/delangi/문서/project/category/AI_development_tool
 exited 127 in 0ms:
/bin/bash: line 1: python: command not found

exec
/bin/bash -lc 'PYTHONPATH=tools python tools/jsonl_hash_chain.py tests/fixtures/jsonl_ledger/pass/minimal_chain.jsonl' in /home/delangi/문서/project/category/AI_development_tool
 exited 127 in 0ms:
/bin/bash: line 1: python: command not found

exec
/bin/bash -lc 'PYTHONPATH=tools python -m pytest tests/tools/test_jsonl_hash_chain.py -q' in /home/delangi/문서/project/category/AI_development_tool
 exited 127 in 0ms:
/bin/bash: line 1: python: command not found

exec
/bin/bash -lc 'git log --oneline --decorate -8' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
4c48099 (HEAD -> feature/jarvis-mvp0, origin/feature/jarvis-mvp0) feat(g4-hash-chain): C-1 timestamp monotonicity FAIL fixture 보강 (E-PASS-10 CI 입증)
6ebc634 docs(session): 58번째 entry CI actual run 증거 기록 — 3 G4 workflow 전원 success
052e583 feat(jsonl_hash_chain): 58번째 entry — 실 구현 sub-cycle (1) violation_type 정밀화: HISTORY_REWRITE Layer 1 제거 (TDD)
18e8ad1 docs(mvp2-beta,external-review,review,session,index): 57번째 entry — (β) sub-수단 결정 entry brief 풀 3+1 + 외부 LLM 1+ (cross-vendor codex gpt-5.5) REVISE → v1.1 1pass 흡수 (BLOCKING 6 + 권고 7)
05c2751 docs(context): CONTEXT.md 현재 상태(56 entry) 동기화
de4e2c8 chore(session-end,session,index): 56번째 entry — 🎉 본 자비스 세션 종료 (51 → 56 entry chain, 6 entry 발효 — MVP-2 영역 진입 합의 chain) + 다음 세션 진입 가이드 (1순위 = 실 구현)
311ca3b chore(mvp2-layer-124-pass,external-review,review,session,index): 55번째 entry — Layer 1+2+4 통합 PASS 격상 entry brief 풀 3+1 + 외부 LLM 1+ (cross-vendor codex gpt-5.5) APPROVE WITH CONDITIONS → v1.1 1pass 흡수 (BLOCKING 9 + 권고 18, 4 source 전원 APPROVE WITH CONDITIONS)
895a77b chore(mvp2-gamma-decision,review,session,index): 54번째 entry — (γ-c) Layer 1+2+4 동시 채택 결정 발효 (1-agent 직접 합의, 53 entry Reviewer 통합 권고 답습 한정, 4 source consensus 1순위)

codex
로컬 Python 명령은 이 환경에서 `python` 바이너리가 없어 실패했습니다. 같은 확인을 `python3`로 재시도하고, 의존성 문제가 있으면 CI evidence를 기준으로 분리해서 적겠습니다.
exec
/bin/bash -lc 'PYTHONPATH=tools python3 tools/jsonl_hash_chain.py tests/fixtures/jsonl_ledger/fail/timestamp_monotonicity.jsonl' in /home/delangi/문서/project/category/AI_development_tool
 exited 1 in 0ms:
FAIL: timestamp_monotonicity.jsonl — 2 violation(s):
  [0] id=11111111-1111-4111-8111-111111111111 type=schema_canonical_error
      detail: canonical_json failed: rfc8785 라이브러리 미설치 — `pip install rfc8785==0.1.4`
  [1] id=22222222-2222-4222-8222-222222222222 type=schema_canonical_error
      detail: canonical_json failed: rfc8785 라이브러리 미설치 — `pip install rfc8785==0.1.4`

exec
/bin/bash -lc 'PYTHONPATH=tools python3 -m pytest tests/tools/test_jsonl_hash_chain.py -q' in /home/delangi/문서/project/category/AI_development_tool
 exited 1 in 0ms:
/usr/bin/python3: No module named pytest

exec
/bin/bash -lc 'PYTHONPATH=tools python3 tools/jsonl_hash_chain.py tests/fixtures/jsonl_ledger/pass/minimal_chain.jsonl' in /home/delangi/문서/project/category/AI_development_tool
 exited 1 in 0ms:
FAIL: minimal_chain.jsonl — 2 violation(s):
  [0] id=11111111-1111-4111-8111-111111111111 type=schema_canonical_error
      detail: canonical_json failed: rfc8785 라이브러리 미설치 — `pip install rfc8785==0.1.4`
  [1] id=22222222-2222-4222-8222-222222222222 type=schema_canonical_error
      detail: canonical_json failed: rfc8785 라이브러리 미설치 — `pip install rfc8785==0.1.4`

exec
/bin/bash -lc "python3 --version && python3 -c 'import rfc8785, jcs; print(rfc8785.__version__ if hasattr(rfc8785,\"__version__\") else \"rfc8785\", jcs.__version__ if hasattr(jcs,\"__version__\") else \"jcs\")'" in /home/delangi/문서/project/category/AI_development_tool
 exited 1 in 0ms:
Python 3.12.3
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'rfc8785'

exec
/bin/bash -lc 'ls -la .venv venv 2>/dev/null' in /home/delangi/문서/project/category/AI_development_tool
 exited 2 in 0ms:
.venv:
total 76
drwxrwxr-x  7 delangi delangi  4096 May 26 21:55 .
drwxrwxr-x 22 delangi delangi  4096 May 27 23:28 ..
-rw-rw-r--  1 delangi delangi     1 May 22 18:16 .gitignore
-rw-rw-rw-  1 delangi delangi     0 May 22 18:16 .lock
-rw-rw-r--  1 delangi delangi    43 May 22 18:16 CACHEDIR.TAG
-rw-rw-r--  1 delangi delangi 35148 May 26 21:55 COPYING
drwxrwxr-x  3 delangi delangi  4096 May 26 22:38 bin
drwxrwxr-x  3 delangi delangi  4096 May 26 17:41 etc
drwxrwxr-x  3 delangi delangi  4096 May 26 20:46 include
drwxrwxr-x  3 delangi delangi  4096 May 22 18:16 lib
lrwxrwxrwx  1 delangi delangi     3 May 22 18:16 lib64 -> lib
-rw-rw-r--  1 delangi delangi   113 May 22 18:16 pyvenv.cfg
drwxrwxr-x  8 delangi delangi  4096 May 26 22:38 share

exec
/bin/bash -lc 'rg -n "rfc8785|jcs|pytest" requirements*.txt pyproject.toml setup.cfg tox.ini 2>/dev/null' in /home/delangi/문서/project/category/AI_development_tool
 exited 2 in 0ms:
requirements-dev.txt:17:#   - docs/review/3plus1-consensus-2026-05-10-g4-jcs-library-selection.md (Q1 풀 3+1 합의 17 조건)
requirements-dev.txt:18:#   - docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md §3 (사용자 명시 결정 갱신 — pyjcs PyPI 미존재 → jcs 대체)
requirements-dev.txt:20:rfc8785==0.1.4
requirements-dev.txt:21:jcs==0.2.1
requirements-dev.txt:28:pytest==9.0.3
requirements-dev.txt:29:pytest-cov==7.1.0

exec
/bin/bash -lc "nl -ba tests/tools/test_jsonl_hash_chain.py | sed -n '1,260p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	"""jsonl_hash_chain Layer 1 violation_type 정밀화 테스트 (57 entry 실 구현 sub-cycle).
     2	
     3	(β) sub-수단 결정 발효 답습 — HISTORY_REWRITE 는 Layer 1 (hash chain) 에서
     4	외부 anchor 없이 검출 불가 (history rewrite = Layer 2 history_anchor_verifier
     5	+ rewrite_defense 영역, 55 entry consensus B-1/B-2 답습). 따라서 Layer 1
     6	ViolationType enum 은 Layer-1-검출가능 3종만 보유한다.
     7	"""
     8	from __future__ import annotations
     9	
    10	import sys
    11	from pathlib import Path
    12	
    13	import pytest
    14	
    15	_ROOT = Path(__file__).resolve().parents[2]
    16	sys.path.insert(0, str(_ROOT / "tools"))
    17	
    18	import jsonl_hash_chain as jhc  # noqa: E402
    19	
    20	_LEDGER = _ROOT / "tests" / "fixtures" / "jsonl_ledger"
    21	
    22	# Layer 1 (hash chain) 가 외부 anchor 없이 검출 가능한 violation_type 전체.
    23	_LAYER1_TYPES = {"prev_hash_mismatch", "hash_recalculation", "genesis_mismatch"}
    24	
    25	
    26	def test_violation_type_enum_is_layer1_only() -> None:
    27	    """ViolationType = Layer-1-검출가능 3종 (history_rewrite 부재 — Layer 2 영역)."""
    28	    actual = {v.value for v in jhc.ViolationType}
    29	    assert actual == _LAYER1_TYPES
    30	    assert "history_rewrite" not in actual
    31	
    32	
    33	@pytest.mark.parametrize(
    34	    "fixture, expected",
    35	    [
    36	        ("pass/minimal_chain", []),
    37	        ("fail/prev_hash_mismatch", ["prev_hash_mismatch"]),
    38	        ("fail/hash_recalculation", ["hash_recalculation"]),
    39	        ("fail/genesis_mismatch", ["genesis_mismatch"]),
    40	    ],
    41	)
    42	def test_validate_chain_fixture_regression(fixture: str, expected: list[str]) -> None:
    43	    """fixture 별 validate_chain violation_type 회귀 (g4-hash-chain.yml 답습)."""
    44	    entries, parse_vios = jhc.parse_jsonl(_LEDGER / f"{fixture}.jsonl")
    45	    assert parse_vios == []
    46	    chain_vios = [v.violation_type for v in jhc.validate_chain(entries)]
    47	    assert chain_vios == expected
    48	
    49	
    50	def test_history_rewrite_never_emitted_by_layer1() -> None:
    51	    """invariant: Layer 1 validate_chain 은 history_rewrite 를 절대 emit 하지 않는다.
    52	
    53	    history rewrite 검출 = Layer 2 (history_anchor_verifier.py + rewrite_defense_check.py)
    54	    영역 — 외부 anchor / base branch 비교 의무 (55 entry B-1 답습).
    55	    """
    56	    for path in sorted(_LEDGER.rglob("*.jsonl")):
    57	        entries, _ = jhc.parse_jsonl(path)
    58	        vios = [v.violation_type for v in jhc.validate_chain(entries)]
    59	        assert "history_rewrite" not in vios, f"{path.name}: unexpected history_rewrite"
    60	
    61	
    62	def test_validate_chain_monotonicity_violation() -> None:
    63	    """timestamp monotonicity 위반 fixture = monotonicity_violation emit (ADR-012 §3.4).
    64	
    65	    chain (genesis + prev_hash + entry hash) 은 valid, ts 만 역행 → Layer 1
    66	    monotonicity_violation 단독 emit (E-PASS-10 CI 입증, 59 entry C-1 보강).
    67	    """
    68	    entries, parse_vios = jhc.parse_jsonl(_LEDGER / "fail/timestamp_monotonicity.jsonl")
    69	    assert parse_vios == []
    70	    chain_vios = [v.violation_type for v in jhc.validate_chain(entries)]
    71	    assert "monotonicity_violation" in chain_vios
    72	    # chain (hash/prev_hash/genesis) 은 valid — monotonicity 외 위반 0
    73	    assert set(chain_vios) == {"monotonicity_violation"}
    74	
    75	
    76	def test_build_violation_entry_uses_layer1_types_only() -> None:
    77	    """build_violation_entry chain violation 필터 = Layer-1 enum 한정 (dead enum 0)."""
    78	    entries, _ = jhc.parse_jsonl(_LEDGER / "fail/prev_hash_mismatch.jsonl")
    79	    vios = jhc.validate_chain(entries)
    80	    entry = jhc.build_violation_entry(entries, vios)
    81	    assert entry is not None
    82	    assert entry["content"]["violation_type"] in _LAYER1_TYPES

exec
/bin/bash -lc 'PYTHONPATH=tools .venv/bin/python tools/jsonl_hash_chain.py tests/fixtures/jsonl_ledger/pass/minimal_chain.jsonl' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
PASS: minimal_chain.jsonl — 2 entries, all checks passed (schema + chain + monotonicity)

exec
/bin/bash -lc 'PYTHONPATH=tools .venv/bin/python tools/jsonl_hash_chain.py tests/fixtures/jsonl_ledger/fail/timestamp_monotonicity.jsonl' in /home/delangi/문서/project/category/AI_development_tool
 exited 1 in 0ms:
FAIL: timestamp_monotonicity.jsonl — 1 violation(s):
  [1] id=22222222-2222-4222-8222-222222222222 type=monotonicity_violation
      detail: ts='2026-05-10T10:00:00Z' < prior ts (ADR-012 §3.4 monotonicity)

exec
/bin/bash -lc ".venv/bin/python -c 'import rfc8785, jcs, pytest; print(\"deps ok\")'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
deps ok

exec
/bin/bash -lc 'PYTHONPATH=tools .venv/bin/python -m pytest tests/tools/test_jsonl_hash_chain.py -q' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 171ms:
........                                                                 [100%]
8 passed in 0.01s

codex
**verdict: APPROVE WITH CONDITIONS**

BLOCKING findings: **없음**. 직접 확인한 repo/CI 상태는 activation brief의 핵심 evidence 주장과 대체로 일치합니다.

조건은 다음 3개입니다.

1. **Layer 2a는 “충족”이 아니라 계속 DEFER로 남겨야 함**  
   `git config receive.denyNonFastForwards`는 local/global/system 모두 미설정입니다. 다만 GitHub main branch protection은 실제로 `guard`, `verify`, `feasibility`, `scan`, `enforce`, `defense`, `validate`, `bypass-detect` 8 contexts + `strict=true` + force push/delete false로 확인됐습니다.  
   따라서 2b는 canonical remote main에 대해 operative append-only 보호를 제공합니다. ADR-011 §2.1(a)의 “동등 이상 보안 결과” 관점에서 **개인/미배포 컨테이너 상태의 2a DEFER는 blocking 아님**. 단, future wording에서 “2a까지 충족”처럼 읽히면 안 됩니다.

2. **E-PASS-8 문구는 “4 G4 workflow PASS”가 아니라 “3 ledger workflow PASS + r2-canary out of scope”로 고정해야 함**  
   확인 결과:
   - `26557460199` G4 Hash Chain + JCS: success
   - `26557460227` G4 Rewrite Defense: success
   - `26557460197` G4 History Anchor Verifier: success
   - `r2-canary`는 path 미트리거이며 GP-2/R-2 영역으로 분리됨  
   brief는 이미 “✅ 3/4” 및 r2-canary 비차단을 적고 있으므로 blocking은 아니지만, 표 제목의 “4 G4 workflow actual run PASS”는 과장으로 재사용하지 않는 조건이 필요합니다.

3. **Layer 5 workflow를 Layer 2 evidence로 흡수했다는 오해를 피해야 함**  
   [history-anchor-verifier.yml](/home/delangi/문서/project/category/AI_development_tool/.github/workflows/history-anchor-verifier.yml:1)는 명시적으로 “Layer 5 External Anchor Verifier”입니다. 이번 cycle이 Layer 5 PASS 진입을 발효하지 않는다는 “부분 답습” framing이 유지되어야 합니다. 현재 brief는 이 구분을 대체로 지키고 있어 blocking은 아닙니다.

**직접 verify 결과**

- [jsonl_hash_chain.py](/home/delangi/문서/project/category/AI_development_tool/tools/jsonl_hash_chain.py:67): `ViolationType`은 `prev_hash_mismatch`, `hash_recalculation`, `genesis_mismatch` 3종만 존재. `history_rewrite` Layer 1 제거 주장 일치.
- [jsonl_hash_chain.py](/home/delangi/문서/project/category/AI_development_tool/tools/jsonl_hash_chain.py:224): timestamp monotonicity 검출 코드 존재.
- [g4-hash-chain.yml](/home/delangi/문서/project/category/AI_development_tool/.github/workflows/g4-hash-chain.yml:197): FAIL fixture 5종 cover 존재.
- `tests/fixtures/jsonl_ledger/fail/`: 5 fixture 확인.
- `.venv` 기준 로컬 실행:
  - `timestamp_monotonicity.jsonl`은 `monotonicity_violation` 단독 검출.
  - `minimal_chain.jsonl` PASS.
  - `tests/tools/test_jsonl_hash_chain.py`: `8 passed`.
- `gh run view 26557936920`: success, step “FAIL fixture — jsonl_hash_chain rc=1 + 5 violation_type cover” success.
- `tests/canonical/`: 72 files 확인.
- branch protection API: 8 contexts, force push/delete false, strict true 확인.

**Non-blocking 권고**

- E-PASS-8 표 제목을 “3 ledger workflows actual run PASS”로 바꾸는 것이 좋습니다.
- branch protection의 `required_approving_review_count`는 현재 `0`입니다. 이번 brief가 review count를 핵심 evidence로 주장하지는 않으므로 비차단이지만, 향후 “branch protection 강도” 주장에는 포함하지 않는 편이 안전합니다.
- `r2-canary`와 `secret-hygiene` actual run은 GP-2/MVP-2 PASS 전 별도 evidence로 남겨야 합니다.

**NOTE / 누락**

PASS 발효와 진입 권한 혼동, MVP-2 PASS/GP-2 PASS 합산, denyNonFastForwards 자동 활성화, Layer 3+5 진입, R-S1 자동 정정은 현재 brief에서 모두 scope 밖으로 분리되어 있습니다. 이 범위 통제는 정합합니다.
tokens used
116,277
**verdict: APPROVE WITH CONDITIONS**

BLOCKING findings: **없음**. 직접 확인한 repo/CI 상태는 activation brief의 핵심 evidence 주장과 대체로 일치합니다.

조건은 다음 3개입니다.

1. **Layer 2a는 “충족”이 아니라 계속 DEFER로 남겨야 함**  
   `git config receive.denyNonFastForwards`는 local/global/system 모두 미설정입니다. 다만 GitHub main branch protection은 실제로 `guard`, `verify`, `feasibility`, `scan`, `enforce`, `defense`, `validate`, `bypass-detect` 8 contexts + `strict=true` + force push/delete false로 확인됐습니다.  
   따라서 2b는 canonical remote main에 대해 operative append-only 보호를 제공합니다. ADR-011 §2.1(a)의 “동등 이상 보안 결과” 관점에서 **개인/미배포 컨테이너 상태의 2a DEFER는 blocking 아님**. 단, future wording에서 “2a까지 충족”처럼 읽히면 안 됩니다.

2. **E-PASS-8 문구는 “4 G4 workflow PASS”가 아니라 “3 ledger workflow PASS + r2-canary out of scope”로 고정해야 함**  
   확인 결과:
   - `26557460199` G4 Hash Chain + JCS: success
   - `26557460227` G4 Rewrite Defense: success
   - `26557460197` G4 History Anchor Verifier: success
   - `r2-canary`는 path 미트리거이며 GP-2/R-2 영역으로 분리됨  
   brief는 이미 “✅ 3/4” 및 r2-canary 비차단을 적고 있으므로 blocking은 아니지만, 표 제목의 “4 G4 workflow actual run PASS”는 과장으로 재사용하지 않는 조건이 필요합니다.

3. **Layer 5 workflow를 Layer 2 evidence로 흡수했다는 오해를 피해야 함**  
   [history-anchor-verifier.yml](/home/delangi/문서/project/category/AI_development_tool/.github/workflows/history-anchor-verifier.yml:1)는 명시적으로 “Layer 5 External Anchor Verifier”입니다. 이번 cycle이 Layer 5 PASS 진입을 발효하지 않는다는 “부분 답습” framing이 유지되어야 합니다. 현재 brief는 이 구분을 대체로 지키고 있어 blocking은 아닙니다.

**직접 verify 결과**

- [jsonl_hash_chain.py](/home/delangi/문서/project/category/AI_development_tool/tools/jsonl_hash_chain.py:67): `ViolationType`은 `prev_hash_mismatch`, `hash_recalculation`, `genesis_mismatch` 3종만 존재. `history_rewrite` Layer 1 제거 주장 일치.
- [jsonl_hash_chain.py](/home/delangi/문서/project/category/AI_development_tool/tools/jsonl_hash_chain.py:224): timestamp monotonicity 검출 코드 존재.
- [g4-hash-chain.yml](/home/delangi/문서/project/category/AI_development_tool/.github/workflows/g4-hash-chain.yml:197): FAIL fixture 5종 cover 존재.
- `tests/fixtures/jsonl_ledger/fail/`: 5 fixture 확인.
- `.venv` 기준 로컬 실행:
  - `timestamp_monotonicity.jsonl`은 `monotonicity_violation` 단독 검출.
  - `minimal_chain.jsonl` PASS.
  - `tests/tools/test_jsonl_hash_chain.py`: `8 passed`.
- `gh run view 26557936920`: success, step “FAIL fixture — jsonl_hash_chain rc=1 + 5 violation_type cover” success.
- `tests/canonical/`: 72 files 확인.
- branch protection API: 8 contexts, force push/delete false, strict true 확인.

**Non-blocking 권고**

- E-PASS-8 표 제목을 “3 ledger workflows actual run PASS”로 바꾸는 것이 좋습니다.
- branch protection의 `required_approving_review_count`는 현재 `0`입니다. 이번 brief가 review count를 핵심 evidence로 주장하지는 않으므로 비차단이지만, 향후 “branch protection 강도” 주장에는 포함하지 않는 편이 안전합니다.
- `r2-canary`와 `secret-hygiene` actual run은 GP-2/MVP-2 PASS 전 별도 evidence로 남겨야 합니다.

**NOTE / 누락**

PASS 발효와 진입 권한 혼동, MVP-2 PASS/GP-2 PASS 합산, denyNonFastForwards 자동 활성화, Layer 3+5 진입, R-S1 자동 정정은 현재 brief에서 모두 scope 밖으로 분리되어 있습니다. 이 범위 통제는 정합합니다.
