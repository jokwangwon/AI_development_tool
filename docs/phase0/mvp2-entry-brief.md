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

#### §2.3.2 W 5 대안 매트릭스 (B-7 흡수 — Agent C R-C-1 답습)

| 대안 | 영역 | 장점 | 단점 | (β)/(γ) cycle 시점 평가 영역 |
|------|----|----|----|---------------------|
| **W-A** | 단일 R-6 확장 (GP-2 + G4 §4.4 Layer 4 통합) | ceremony-inflation 차단 / CI 자원 효율 / evidence 통합 | step 수 증가 / 실패 영역 식별 복잡도 ↑ / **실 repo 기존 G4 workflow 분리 운영과 충돌** | (β) cycle 시점 평가 (3 옵션 답습: (i) 일괄 통합 / (ii) 보존 + 중복 step 추가 / (iii) 분산 추가) |
| **W-B** | 별도 workflow 2개 분리 (`secret-egress-redaction.yml` + `ledger-chain-verify.yml`) | 영역 분리 명확 / 실패 영역 식별 즉시 | ceremony-inflation 위험 / branch protection contexts 추가 부담 (43 entry 8 contexts 답습) | (β) cycle 시점 평가 |
| **W-C** ⭐ | 단계 분리 (GP-2 우선 진입 + G4 §4.4 Layer 4 후속 진입) | 시간 분리 / 의존 영역 risk 회피 | 합의 cycle 2회 부담 | (β) cycle 시점 평가 |
| **W-D** ⭐ | roadmap.md §5.3 답습 별도 progression (그룹 D + 그룹 C 별도) | roadmap 권위 답습 충실 | 합의 cycle 2회 부담 + 통합 효율 손실 | (β) cycle 시점 평가 |
| **W-E** ⭐ | pre-commit hook 활용 (CI workflow 외 영역) | dev 환경 즉시 검증 | CI 회귀 검증 ≠ pre-commit (CI 영역 필요) | (β) cycle 시점 평가 — pre-commit + CI workflow 동시 가능 |

→ **본 cycle = W 결정 0** (W-A/B/C/D/E 中 어느 것 채택 결정 = (β) sub-수단 결정 cycle 영역). 51 brief §4.2 W-A 권고는 *후보 권고* 한정 (본 cycle 합의 영역 외).

#### §2.3.3 본 cycle 합의 발효 시 채택 결정 영역

✅ **W 결정 자격 (β) sub-수단 결정 cycle 영역 발효** — W-A/B/C/D/E 中 결정 cycle 진입 자격
✅ **branch protection contexts 추가 영역 결정 사용자 영역 carry-over** (8 contexts 답습 유지, 신규 contexts 추가 사용자 영역, 43 entry 답습)
✅ **실 repo 기존 G4 workflow (`g4-hash-chain.yml` 등) 답습 의무 명시** (W-A 채택 시 통합 framing, W-B/C/D 채택 시 보존 framing)

---

## §3 ADR-011 §2.1 (a)~(d) 4조건 모법 + (e) 합의 APPROVE 후속 운영조건 — 5조건 매트릭스 (두 영역별, B-2 흡수)

본 §3 = 51 entry audit brief §2.2 + §3.3 매트릭스 답습 (재정리 + 본 (α) 합의 발효 시점 격상 명시 + ADR-011 §2.1 framing 정정).

| # | 조건 | 권위 source | GP-2 (§2.1) | G4 §4.4 Layer 4 (§2.2) |
|---|------|----------|-------------|----------------------|
| (a) | 동등 이상 보안 결과 | ADR-011 §2.1 (a)~(d) 4조건 모법 | ✅ R-4 답습 (`redaction-pattern-equivalence.md`) — 충족 | ⚠️ PoC 시제 충족 / PASS 시제 = 실 구현 sub-cycle 영역 (B-6 흡수) |
| (b) | 격리 환경 PoC 실증 | ADR-011 §2.1 (a)~(d) 4조건 모법 | ⚠️ 부분 (Group D PoC 형식적 검출 layer 한정, 송신 redaction PoC = 실 구현 sub-cycle 영역) | ⚠️ PoC 시제 충족 (`g4-hash-chain.yml`) / PASS 시제 = 실 구현 sub-cycle 영역 (B-6 흡수) |
| (c) | ADR / SDD 권위 명시 | ADR-011 §2.1 (a)~(d) 4조건 모법 | ✅ ADR-011 §2.3 + governance-preconditions §4 — 충족 | ✅ ADR-012 §2.8 (5-layer) + G4 §4.4.1 — 충족 (B-1 권위 인용 정정 답습) |
| (d) | 자동 회귀 검증 경로 확보 | ADR-011 §2.1 (a)~(d) 4조건 모법 | ⚠️ PoC 시제 부분 / PASS 시제 = R-6 workflow 답습 확장 (§2.3 W 5 대안 中 결정 = (β) 영역) | ⚠️ PoC 시제 부분 / PASS 시제 = R-6 workflow 답습 확장 (§2.3 W 5 대안 中 결정 = (β) 영역) |
| (e) | 합의 APPROVE | **ADR-011 §3 후속 권위 + governance-preconditions §4.5 Exit (line 455)** — 운영조건 (별도 layer) | ❌ gap — 본 (α) 합의 APPROVE → 진입 *권한* 발효 / Implementation Evidence PASS 발효 = 별도 합의 (실 구현 + (a)~(d) evidence 완료 후) | ❌ gap — 동일 |

→ **본 (α) cycle 합의 발효 시점 — 두 영역 모두 (e) 진입 *권한* 충족 (Implementation Evidence PASS 발효 ≠ 본 (α), 별도 합의 영역)**.

본 (α) 합의 발효 후 후속 cycle:
- (β) sub-수단 결정 cycle → R-1~R-5 + L-1~L-5 결정 발효
- (γ) 분리 영역 결정 cycle → Layer 1+2 의존 영역 vs Layer 4 동시 결정 (4 대안 답습)
- 실 구현 sub-cycle → (a)~(d) evidence 생성 + R-6 workflow 확장 step 통합
- MVP-2 Implementation Evidence PASS 발효 합의 → (a)~(d) 4조건 evidence + (e) 후속 운영조건 + 사용자 명시 + 별도 합의

---

## §4 합의 형태 + 풀 3+1 승격 트리거 검증

### §4.1 본 cycle 합의 형태 = 풀 3+1 + 외부 LLM 1+ (carry-over 답습 정당화 + N-10 Provider Liquidity 답습)

**합의 형태**: **풀 3+1 + 외부 LLM 1+ (cross-vendor 의무)**

**정당화 출처**:
1. 51 entry audit brief §7.2 — "후속 MVP-2 진입 합의 = 풀 3+1 + 외부 LLM 1+" 권고 직접 답습
2. roadmap-mvp1.md §1.3 — "GP-2 = MVP-2 의 Implementation Evidence PASS 영역 *우선순위 1*" (큰 영역 = 풀 3+1 + 외부 LLM 1+ 의무)
3. 32 entry MVP-1 Implementation Evidence PASS 발효 합의 = 풀 3+1 + 외부 LLM 1+ 답습 패턴
4. 24 entry MVP-1 1.5차 보강 entry brief 합의 = 풀 3+1 + 외부 LLM 1+ 답습 (entry brief 동형 패턴)
5. ADR-011 §2.1 (a)~(d) 4조건 모법 + (e) 후속 운영조건 + §2.4 T3 영역 답습 = "큰 결정 (MVP-2 진입) = 풀 3+1 + 외부 LLM 1+ + 사용자 명시"
6. **헌법 5조-2 Provider Liquidity 비협상** — cross-vendor 검증 의무 (OpenAI ≠ Anthropic) (N-10 흡수)
7. **roadmap.md §5.4 그룹 C+D = "단축 합의 + PoC evidence" 권고 vs 본 cycle = 풀 3+1 + 외부 LLM 1+ 격상** (§1.3 항목 5 답습)

### §4.2 두 영역 *발효 시점* 합의 형태 권고 (선행 권위 답습)

| 영역 | 본 (α) 합의 (진입 권한) | 실 구현 sub-cycle (수단 결정 + 구현) | Implementation Evidence PASS 발효 |
|------|----------------------|--------------------------------|----------------------------|
| **GP-2** | **풀 3+1 + 외부 LLM 1+** (본 (α)) | **(β) sub-수단 결정 cycle = 풀 3+1** (R-1~R-5 中 R-4 권고, 51 brief §2.3 답습) + 실 구현 별도 sub-cycle (수단별 합의 형태 차등) | **풀 3+1 + 외부 LLM 1+ + 사용자 명시** (32 entry 답습) |
| **G4 §4.4 Layer 4** | **풀 3+1 + 외부 LLM 1+** (본 (α)) | **(γ) 분리 영역 결정 = 풀 3+1** (4 대안 (γ-a/b/c/d), §2.2.4 답습) + **(β) sub-수단 결정 = 풀 3+1** (L-1~L-5 中 L-4 MVP 권고) + 실 구현 별도 sub-cycle | **풀 3+1 + 외부 LLM 1+ + 사용자 명시** (32 entry 답습) |

### §4.3 7 풀 3+1 승격 트리거 검증 (본 cycle 자체 ↔ 두 영역별, B-1 + N-7 흡수)

본 cycle 자체:

| # | trigger | 본 (α) 발화 | 근거 |
|---|---------|---------|------|
| 1 | 큰 결정 (영역 진입 발효 / 수단 결정 / threshold 고정) | ✅ **발화** | MVP-2 영역 진입 발효 = 큰 결정 (Layer 2 Implementation Evidence PASS 영역 *2차* 진입) |
| 2 | 아키텍처 / SDD / 보안 본문 변경 | ❌ 미발화 | brief = phase0 신규 1 파일, 본문 변경 0 |
| 3 | ADR 본문 변경 | ❌ 미발화 | brief = ADR 본문 0 (cross-reference 답습 한정) |
| 4 | 권위 chain 다중 source 손상 위험 | ✅ **발화 (R-S1 CONFIRMED 격상)** ⭐ (B-1 + N-7 흡수) | §1.3 항목 2 + §2.2.1 + §4.4 = ADR-012 §2.3 (4-layer) vs §2.8/G4 §4.4.1 (5-layer) **CONFIRMED divergence** (5 source verify: codex + Agent A + Agent B + Agent C + Reviewer). 본 brief v1.1 = 권위 인용 chain 정정 답습 (G4 §4.4.1 + ADR-012 §2.8 PRIMARY, §2.3 = numbering 근거 아님). 다중 source 정정 = §4.4 + §9.5 별도 cycle 영역 |
| 5 | 외부 LLM 응답 통합 필요성 | ✅ **발화** | MVP-2 진입 = 큰 영역, cross-vendor 외부 LLM 1+ 의무 |
| 6 | Tier-2/3 catalog 자동 확장 | ❌ 미발화 | §0.3 #8 명시 금지 |
| 7 | Hermes PMO 격상 | ❌ 미발화 | §0.3 #16 명시 금지 |

→ **3/7 발화 → 풀 3+1 + 외부 LLM 1+ 합의 적격 (정당화)**.

### §4.4 ⭐ R-S1 CONFIRMED divergence — Reviewer 단독 verbatim verify 답습 (B-1 흡수)

본 §4.4 = `docs/review/3plus1-consensus-2026-05-28-mvp2-entry.md` §4 답습 (5 source verify: codex + Agent A + Agent B + Agent C + Reviewer = 5/5).

#### §4.4.1 Verbatim 충돌 매트릭스

**ADR-012 §2.3 line 165~185 (4-layer numbering)**:
- Layer 1 — Hash Chain (MANDATORY)
- Layer 2 — Git append-only branch (MANDATORY)
- Layer 3 — Signed commit (RECOMMENDED MVP)
- **Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)**

**ADR-012 §2.8 line 264~272 (5-layer numbering)**:
- Layer 1 — Hash chain
- Layer 2 — Git append-only branch
- Layer 3 — pre-commit hook
- **Layer 4 — CI 회귀 검증**
- **Layer 5 — External anchor**

**G4 §4.4.1 line 629~660 (5-layer numbering, ADR-012 §2.8 동형)**:
- Layer 1 — Hash Chain (MANDATORY)
- Layer 2 — Git append-only branch (MANDATORY)
- Layer 3 — Signed commit (RECOMMENDED MVP)
- **Layer 4 — CI 회귀 검증 (MANDATORY)**
- **Layer 5 — External Anchor (RECOMMENDED MVP)**

→ ⭐⭐⭐⭐ **ADR-012 *자체 내부* §2.3 (4-layer) vs §2.8 (5-layer) divergence** + G4 §4.4.1 = §2.8 답습 동형 → §2.3 만 isolated 4-layer.

#### §4.4.2 본 brief v1.1 권위 인용 chain 정정

본 brief 의 G4 §4.4 Layer 4 인용 = 다음 권위 chain 한정 (§1.2 + §2.2.1 답습):
- **PRIMARY**: `provider-agnostic-memory-skill-design.md §4.4.1 line 629~660` (G4 직접 정의)
- **SUPPORTING**: `ADR-012 §2.8 line 264~272` (5-layer 동형)
- **PRINCIPLE ONLY (not numbering)**: `ADR-012 §2.3 line 165~185` (Append-only + Hash Chain 원칙)
- **MONOTONICITY**: `ADR-012 §3.4`
- **PREV_HASH FAILURE**: `ADR-012 §2.7`
- **CANONICAL**: `ADR-012 §2.5` (RFC 8785 JCS)

#### §4.4.3 다중 source 정정 cycle = 본 cycle scope 외

ADR-012 §2.3 본문 정정 또는 §2.8 동형 답습 cross-reference 강화 = **별도 cross-reference 정정 cycle 사용자 명시 영역** (§9.5 답습). 본 (α) 합의 = 권위 인용 정정 한정 (본문 변경 0).

---

## §5 Rollback Trigger / Evidence *후보* 본문 (본 cycle 합의 발효 시점 후보 채택, 구현 발효 별도 sub-cycle, N-1 흡수)

### §5.1 두 영역별 Rollback Trigger 본문 후보 (51 entry audit brief §5 답습 + N-3 흡수)

| # | Trigger | 영역 | 발화 조건 | 권위 답습 |
|---|---------|----|---------|---------|
| RT-1 | Hermes native redaction 우회 검출 | GP-2 | log file canary inject grep PASS 후 평문 leak 발견 | ADR-011 §2.3 #2 + R-7 SOP §5 ROLLBACK trigger R5 |
| RT-2 | P1 facade RedactionFilter 우회 | GP-2 | LLM API request body 평문 secret 검출 | P1 v2 §8.2 + ADR-008 차단조건 #1 보조 |
| RT-3 | base64 / URL-encoded evasion 신규 발견 | GP-2 (R-5 영역) | Tier-1 42 catalog 미커버 evasion 발견 | G3-4 답습 → MVP-2/3 영역 분리 (본 cycle 범위 외) |
| RT-4 | hash chain middle entry tampering 검출 | G4 §4.4 Layer 4 | Layer 1 검증 실패 | ADR-012 §2.7 (`chain_violation_detected` ledger entry) |
| RT-5 ⭐ (N-3 흡수) | canonical JSON reference mismatch | G4 §4.4 Layer 4 | Layer 4 CI step → **BLOCK** (위반 검출) | ADR-012 §2.5 + §원칙 5/6 + R-6 답습 |
| RT-5.1 ⭐ (N-3 신규 분리) | fallback canonicalizer used | G4 §4.4 Layer 4 | Layer 4 CI step → `canonical_json_fallback` ledger entry + Reviewer/user review | ADR-012 §2.5 (fallback 사용 시 ledger entry 의무) |
| RT-6 | timestamp monotonicity 위반 | G4 §4.4 Layer 4 | Layer 4 CI step FAIL → BLOCK | ADR-012 §3.4 + R-6 답습 |
| RT-7 | R-6 workflow 자체 silent override | 통합 | gate enforcement bypass detected | G3 §2.6 + G4 §3.8.2 #10 + 43 entry 8 contexts (`bypass-detect`) 답습 |

### §5.2 Evidence Required (51 entry audit brief §6 답습 + N-4 + N-6 흡수)

| # | Evidence | 출처 |
|---|---------|------|
| E-1 | Hermes native redaction Tier-1 42 catalog 적용 검증 | `agent/redact.py` 실행 evidence (R-4 답습, Hermes upstream 영역) |
| E-2 | P1 facade RedactionFilter 적용 검증 | facade 진입점 evidence (TR-1 (d) carry-over 의존) |
| E-3 | log file canary inject + grep PASS evidence | Docker 격리 PoC (R-1 / R-4.1 답습) |
| E-4 | hash chain 검증 PoC PASS evidence | middle tampering 차단 PoC (Docker 격리) |
| E-5 | canonical JSON test corpus PASS (≥ 20 RFC 8785 reference) | `tests/canonical/` 24 fixtures (G4 §4.4.2 답습, PoC 시제 충족) |
| E-6 | timestamp monotonicity 위반 차단 PoC | Docker 격리 (ADR-012 §3.4 답습) |
| E-7 ⭐ (N-6 흡수) | R-6 workflow 확장 step actual run PASS | GitHub Actions run ID + verdict PASS (**42 entry actual run id `25623028888` 답습 framing**) |
| E-8 | 합의 보고서 commit | 본 (α) 합의 + (β) + (γ) + 실 구현 sub-cycle 별 |
| E-9 ⭐ (N-4 흡수) | 외부 LLM 응답 1+ (cross-vendor) | `docs/external-review/2026-05-28-mvp2-entry-codex-response.md` 등. **`external_llm_received` ledger entry 사용 시 `agent="user"` 강제 + vendor/model identifier 명시 + 입력 prompt hash 포함 + 검토 대상 commit/hash 포함** (ADR-012 §2.2 line 140 답습) |

### §5.3 JSONL Ledger event enum 후보 (본 cycle 합의 발효 시점 *reserved candidate* 한정, N-5 흡수)

본 cycle 합의 발효 시 **reserved candidate** 한정 (ADR-012 §2.2 amendment 또는 schema_version 갱신 전까지 non-authoritative, 실제 ledger write 금지):

| # | event enum 후보 (reserved) | 영역 | 답습 |
|---|--------------|----|----|
| 1 | `gp2_redaction_layer1_implementation` | GP-2 | ADR-012 §2.2 line 150~152 답습 패턴 |
| 2 | `g4_ledger_chain_verify_layer4_implementation` | G4 §4.4 Layer 4 | 동일 답습 |
| 3 | `r6_workflow_extension_mvp2` | 통합 | R-6 답습 확장 시점 |

→ 본 enum 후보 = **ADR-012 §2.2 *본문 변경* trigger** (cross-reference 갱신 ≠ 본문 변경, N-A-3 답습). 본 (α) 합의 후 ADR-012 §2.2 amendment 별도 cycle (사용자 명시 영역).

---

## §6 금지 사항

### §6.1 본 brief 자체 금지 사항

§0.3 답습 (29 항목 재명시 생략).

### §6.2 본 brief 발효 *후* 후속 cycle 진입 시점 금지 사항 (의무 답습)

본 (α) 합의 APPROVE 후 (β) / (γ) / 실 구현 sub-cycle 진입 시:

| # | 금지 영역 | 의무 답습 |
|---|---------|---------|
| 1 | 자동 (β) sub-수단 결정 cycle 진입 | 사용자 명시 의무 |
| 2 | 자동 (γ) 분리 영역 결정 cycle 진입 | 사용자 명시 의무 |
| 3 | 자동 실 구현 sub-cycle 진입 | 사용자 명시 의무 |
| 4 | MVP-2 Implementation Evidence PASS *자동* 선언 | 실 구현 + (a)~(d) evidence + (e) 합의 APPROVE + 사용자 명시 (별도 합의) |
| 5 | 외부 library (`pyjcs` / `rfc8785`) 자동 도입 | ADR-012 §2.1 R-2 / R-4.1 PoC 자동 재실행 trigger 발화 + 별도 cycle |
| 6 | G4 §4.4 Layer 1/2/3/5 영역 자동 진입 | 별도 cycle 또는 의존 영역 자동 (사용자 명시) |
| 7 | GP-1 / GP-4 / GP-6 / G3 / G4 (Layer 4 외) 자동 진입 | MVP-3~MVP-5 영역 (별도 합의) |
| 8 | branch protection contexts 자동 추가 | 사용자 admin scope 영역 (43 entry 답습) |
| 9 | ADR 본문 갱신 자동 cross-reference 변경 | 별도 commit 영역 (R-S1 정정 영역 포함) |
| 10 | Tier-2/3 catalog 자동 확장 | 별도 풀 3+1 + 외부 LLM 1+ |
| 11 ⭐ (B-4 답습) | Hermes upstream `agent/redact.py` 본 repo 內 import 결정 | 별도 합의 (Hermes upstream PR vs 본 repo 영역 분리 답습 유지) |
| 12 ⭐ (B-1 답습) | ADR-012 §2.3 본문 정정 자동 진입 (R-S1 다중 source 정정) | 별도 cross-reference 정정 cycle 사용자 명시 영역 (§9.5 답습) |
| 13 ⭐ (B-7 답습) | roadmap.md §5.4 격상 차이 정정 자동 진입 | 별도 cross-reference 정정 cycle (선택 영역, 본 cycle 합의 자체로 격상 답습) |

---

## §7 외부 LLM 응답 요구 영역 (사용자 준비 자료)

### §7.1 외부 LLM 응답 1+ 의무 답습 출처

1. **51 entry audit brief §7.2** — "후속 MVP-2 진입 합의 = 풀 3+1 + **외부 LLM 1+** 권고 (cross-vendor 의무)" 직접 답습
2. **24 entry MVP-1 1.5차 보강 entry brief** — entry brief 동형 패턴 외부 LLM 1+ 답습
3. **32 entry MVP-1 Implementation Evidence PASS 발효 합의** — 외부 LLM 1+ (codex via tmux cross-vendor) 답습
4. **헌법 5조-2 Provider Liquidity (비협상)** — cross-vendor 검증 의무 (OpenAI ≠ Anthropic)
5. **ADR-011 §2.1 (a)~(d) 4조건 모법 + (e) 후속 운영조건 + §2.4 T3 영역** — 큰 결정 = 외부 LLM 1+ + 사용자 명시

### §7.2 외부 LLM 응답 *입력 자료* 정의 + 호출 자격 답습

본 (α) cycle 외부 LLM 응답 *입력 자료* (실 호출 시점 답습 — 본 brief v1 codex 호출 답습):

| 필수 입력 | 자료 위치 |
|---------|---------|
| 본 brief v1 (mvp2-entry-brief.md) | `docs/phase0/mvp2-entry-brief.md` |
| 51 entry audit brief | `docs/phase0/mvp2-entry-eligibility-audit-brief.md` |
| 51 entry 합의 보고서 | `docs/review/3plus1-consensus-2026-05-28-mvp2-entry-eligibility-audit.md` |
| 32 entry MVP-1 PASS 발효 합의 | `docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md` |
| roadmap-mvp1.md §1.3 | `docs/architecture/implementation-runtime-roadmap-mvp1.md` |
| governance-preconditions.md §4 | `docs/architecture/governance-preconditions.md` |
| provider-agnostic-memory-skill-design.md §4.4 | `docs/architecture/provider-agnostic-memory-skill-design.md` |
| ADR-012 §2.3 + §2.5 + §2.7 + §2.8 + §3.4 | `docs/decisions/ADR-012-evidence-ledger-protection.md` |
| ADR-011 §2.1 (a)~(d) + §3 후속 권위 | `docs/decisions/ADR-011-means-vs-ends-redaction.md` |

**외부 LLM 호출 자격 답습 (본 cycle 실 호출)**: **(α) Claude tmux + codex bypass sandbox 직접 호출** — 사용자 명시 (2026-05-28) + 24 entry (α) 답습 + cross-vendor (OpenAI ≠ Anthropic) 충족.

### §7.3 외부 LLM 응답 *자격 검증* 기준 (Reviewer 검토 영역, 24 entry §7.3 답습)

외부 LLM 응답 입력 시 Reviewer 직접 검증 7 기준:

| # | 기준 | 검증 영역 |
|---|------|---------|
| 1 | cross-vendor 충족 (OpenAI ≠ Anthropic) | vendor identifier 명시 검증 |
| 2 | 본 brief v1 입력 자료 직접 읽기 evidence | 응답 본문 내 brief §X verbatim 인용 또는 영역 식별 |
| 3 | **ADR-011 §2.1 (a)~(d) 4조건 모법 + (e) 후속 운영조건 답습 정확성** (B-2 답습) | (a)~(d) + (e) 분리 framing 검증 |
| 4 | 두 영역 (GP-2 + G4 §4.4 Layer 4) 진입 자격 평가 | 두 영역별 평가 본문 |
| 5 | (β) sub-수단 결정 분리 답습 정확성 | 본 cycle = 영역 진입 한정, sub-수단 결정 = (β) 분리 인식 |
| 6 | Rollback Trigger / Evidence 요건 평가 (후보 vs 구현 발효 분리) | RT-1~RT-7 / E-1~E-9 평가 (N-1 답습 — 후보 vs 발효 분리) |
| 7 | ⭐ **R-S1 CONFIRMED divergence 검증** (B-1 답습) | 본 brief §4.4 권위 인용 chain 정정 답습 + ADR-012 §2.3 vs §2.8 verbatim 직접 read |

---

## §8 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

### §8.1 본 brief 발효 *후* (= 본 cycle 합의 APPROVE 시점) 다음 단계 (사용자 결정 영역)

본 (α) 합의 APPROVE 발효 후:

1. **(β) sub-수단 결정 cycle** — R-1/2/3/4/5 (GP-2) + L-1/2/3/4/5 (G4 §4.4 Layer 4) — 풀 3+1 합의
   - 본 (α) 권고: GP-2 = R-4 (R-1+R-2+R-3 병행) / G4 §4.4 Layer 4 = L-4 (L-1+L-3 병행 MVP)
   - W 5 대안 (W-A/B/C/D/E, §2.3.2 답습) 채택 결정 영역
2. **(γ) 분리 영역 결정 cycle** — G4 §4.4 Layer 4 분리 영역 4 대안 ((γ-a/b/c/d), §2.2.4 답습) — 풀 3+1 합의
3. **실 구현 sub-cycle** ((β) + (γ) 후) — **planning/decision track → implementation track 진입** (N-2 답습). Hermes upstream `agent/redact.py` 영역 + 본 repo P1 facade RedactionFilter (TR-1 (d) carry-over 의존) + Layer 1 (hash chain) PoC 시제 → PASS 시제 격상 + canonical JSON test corpus PoC → PASS + R-6 workflow 확장 step + 합의 형태 별
4. **MVP-2 Implementation Evidence PASS 발효 합의** — 실 구현 + (a)~(d) evidence + (e) 합의 APPROVE + 사용자 명시 (32 entry 답습 패턴)
5. **R-S1 cross-reference 정정 cycle** — ADR-012 §2.3 본문 정정 또는 §2.8 동형 답습 cross-reference 강화 — 별도 풀 3+1 + 사용자 명시 (§9.5 답습)
6. **ADR 본문 cross-reference 갱신 별도 commit** — ADR-008 차단조건 #1 보조 + ADR-012 §2.2 event enum amendment (B-1 + N-A-3 답습) + ADR-011 §8.5 후속 작업에 GP-2 + G4 §4.4 Layer 4 등록
7. **51 audit brief carry-over 결함 정정 cycle** (선택) — `agent/redact.py` 본 repo 內 표기 framing 정정 (B-4 답습)

본 brief 합의는 다음 단계 진입을 *발생시키지 않음* — 사용자 명시 의무.

---

## §9 답습 참조

### §9.1 상위 권위 (N-9 + N-10 흡수)

- **헌법 제8조 (보안)** — `docs/constitution/PROJECT_CONSTITUTION.md` — **본 cycle = 헌법 8조 본질 충족 *보조* 영역 진입** (DB INSERT 차단 = GP-1 본질 책임, GP-2 + G4 §4.4 Layer 4 = 보조 layer)
- **헌법 제5조-2 (Provider Liquidity, 비협상)** — **본 cycle = sub-수단 자격 평가 영역** ((β) cycle 시점, R-1~R-5 + L-1~L-5 中 Provider Liquidity 충족 영역 평가)
- **ADR-011 §2.1 (a)~(d) 4조건 모법 + §3 후속 권위 (e) 합의 APPROVE 운영조건** (B-2 답습) — `docs/decisions/ADR-011-means-vs-ends-redaction.md`
- **ADR-011 §2.3** (Hermes ≠ root of trust) — 동상
- **ADR-011 §2.4** (T1/T2/T3) — 동상

### §9.2 직접 선행 자료

- **51 entry audit brief** (본 brief 의 직접 입력 자료, ⚠️ carry-over 결함 framing 정정 영역 — B-4 답습) — `docs/phase0/mvp2-entry-eligibility-audit-brief.md`
- **51 entry 합의 보고서** — `docs/review/3plus1-consensus-2026-05-28-mvp2-entry-eligibility-audit.md`
- **본 cycle Reviewer 통합 합의 보고서** — `docs/review/3plus1-consensus-2026-05-28-mvp2-entry.md` (BLOCKING 7 + 권고 13 매트릭스)
- **외부 LLM codex 응답** — `docs/external-review/2026-05-28-mvp2-entry-codex-response.md` (3597줄, REVISE AS ENTRY BRIEF INPUT, BLOCKING 3 + 권고 5 + NOTE 3)
- **32 entry MVP-1 PASS 발효 합의** — `docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md`
- **24 entry MVP-1 1.5차 보강 entry brief** (본 brief 구조 답습 source) — `docs/phase0/mvp1-1.5th-reinforcement-entry-brief.md`
- **24 entry 합의 보고서** — `docs/review/3plus1-consensus-2026-05-27-mvp1-1.5th-reinforcement-entry.md`
- **`implementation-runtime-roadmap-mvp1.md`** — `docs/architecture/implementation-runtime-roadmap-mvp1.md`
- **`implementation-runtime-roadmap.md` §3 + §4 + §5.4 (그룹 C+D 합의 형태 격상 답습) + §6**
- **`governance-preconditions.md §4`** (GP-2)
- **`provider-agnostic-memory-skill-design.md §4.4`** (Layer 1~5)
- **`ADR-012-evidence-ledger-protection.md §2.3 + §2.5 + §2.7 + §2.8 + §3.4`**

### §9.3 메타 영역

- `redaction-pattern-equivalence.md` (R-4 답습, ADR-011 §2.1 (a) 충족)
- `r4-1-trigger-extension-evidence.md` (R-4.1 PoC PASS, ADR-011 §2.1 (b) 충족)
- `g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md` (Group D PoC, 형식적 검출 layer 한정)
- ADR-008 차단조건 #1 보조 (`docs/decisions/ADR-008-hermes-adoption-decision.md`)
- **Hermes upstream HEAD v0.12.0** (B-4 답습) — `/tmp/hermes-phase0/hermes-agent/agent/redact.py` 401 LOC

### §9.4 관련 도구 / workflow (51 entry audit brief §10 답습 + B-5 + B-6 답습)

- `agent/redact.py` (Hermes native redaction) — R-1 영역 (**Hermes upstream**, B-4 답습)
- P1 facade RedactionFilter — R-2 영역 (TR-1 (d) carry-over 의존)
- `.github/workflows/r2-canary.yml` (R-6 workflow) — R-3 + L-3 영역
- `.github/workflows/g4-hash-chain.yml` (10652B) — G4 §4.4 영역 (실 repo 기존 분리 운영, B-5 답습)
- `.github/workflows/history-anchor-verifier.yml` (19094B) — G4 §4.4 영역 (실 repo 기존)
- `.github/workflows/rewrite-defense.yml` (16454B) — G4 §4.4 영역 (실 repo 기존)
- `tools/jsonl_hash_chain.py` (genesis hash + 4 violation_type) — Layer 1 PoC 시제 (B-6 답습)
- `tools/canonical_json.py` — canonical PoC 시제 (B-6 답습)
- `tests/canonical/` 24 fixtures (8 카테고리 × 3) — test corpus PoC 시제 (B-6 답습)
- `tools/secret_scanner.py` (Group D Tier-1 42 catalog 답습) — 본 cycle 외 (MVP-1 답습)

### §9.5 본 brief 발효 후 cross-reference 갱신 영역 (별도 commit, B-1 + N-13 흡수)

- **R-S1 정정 영역 (별도 cross-reference 정정 cycle 사용자 명시 영역)** ⭐ (B-1 흡수):
  - ADR-012 §2.3 본문 정정 (4-layer → 5-layer 동형, §2.8 답습) — 별도 풀 3+1 + 사용자 명시
  - 또는 §2.8 동형 답습 cross-reference 강화 (§2.3 = 원칙 영역, §2.8 = numbering 권위 layer 명시)
- ADR-008 차단조건 #1 보조 cross-reference 추가 (governance-preconditions §4.7 line 466 답습)
- ADR-012 §2.2 event enum amendment (`gp2_redaction_layer1_implementation` / `g4_ledger_chain_verify_layer4_implementation` / `r6_workflow_extension_mvp2` 등록 — N-A-3 답습)
- ADR-011 §8.5 후속 작업에 GP-2 + G4 §4.4 Layer 4 등록
- **Implementation Evidence PASS 발효 시점 R-S1 정정 사전조건 명문** ⭐ (N-13 흡수): MVP-2 Implementation Evidence PASS 합의 시 R-S1 정정 *선행 의무* 또는 *동시 의무* 영역 결정 (별도 합의)
- roadmap.md §5.4 격상 차이 명시 (선택, §1.3 항목 5 답습)
- 51 audit brief carry-over 결함 정정 (B-4 답습, 선택)

---

## §10 본 brief v1 작성 자격 자기진단 (메타 편향 회피)

본 brief 작성자 (Claude Opus 4.7) 의 자기 발견 잠재 위험:

| # | 위험 | 본 brief 의 처리 |
|---|------|--------------|
| **P-1** | 본 brief 가 MVP-2 진입을 *권유* 하는 방향으로 편향 | §0.3 + §6.2 29+13 금지 사항 다층 명시, §0.4 발효 자격 3 조건 |
| **P-2** | (α) cycle 자체에서 sub-수단 결정 (β) 무단 침입 | §0.3 #10 #11 + §1.3 항목 4 + §2.1.3 + §2.2.3 다층 답습 |
| **P-3** | 51 entry audit brief 답습이 단방향 (audit → entry) — 51 brief 결함 잔존 시 본 brief 에 cascade | ⭐ **확정 cascade 발견 — B-4 (`agent/redact.py` 본 repo 內 부재 표기)** = 51 brief carry-over 결함. 본 brief v1.1 = framing 정정 한정 (§2.1.1 + §2.1.2 + §6.2 #11). 51 brief 자체 정정 = 별도 cycle |
| **P-4** ⭐⭐⭐ (CONFIRMED divergence 격상) | **R-S1 CONFIRMED divergence** — ADR-012 §2.3 (4-layer) vs §2.8/G4 §4.4.1 (5-layer) | §4.4 답습 (5 source verify: codex + Agent A + Agent B + Agent C + Reviewer). 본 brief v1.1 = 권위 인용 chain 정정 한정 (§1.2 + §2.2.1 + §4.4.2). 다중 source 정정 = §9.5 별도 cycle 영역 |
| **P-5** | 24 entry 답습 동형 패턴 적용이 본 (α) cycle 특수성 무시 위험 | §1.3 항목 4 + N-8 + N-11 답습 (sub-수단 결정 분리 정당화 보강, 25 조합 복잡도) |
| **P-6** | "W-A 통합" 권고 (§2.3) 가 사용자 영역 침입 위험 | §2.3.2 W 5 대안 매트릭스 (W-A/B/C/D/E) + §6.2 #1 자동 진입 0건 |
| **P-7** | 두 영역 통합 진행이 GP-2 / G4 §4.4 Layer 4 *각각* 의 영역 특성 무시 위험 | §2.1 + §2.2 각각 별도 분석 + §3 매트릭스 별도 컬럼 + §4.2 발효 시점 합의 형태 권고 각각 명시 |
| **P-8** ⭐ (Agent B 권고 답습) | filesystem 직접 inspection evidence (B-4 + B-5 + B-6) 가 본 cycle 발효 시점 (2026-05-28) state 한정 → 본 cycle 後 변경 시 evidence 변질 | §0.3 #2 + #5 명시 (본 cycle 內 변경 0) + filesystem state 답습 시점 명시. 본 cycle 후 변경 영역 = 별도 cycle |

---

## §11 v1.1 보강 매트릭스 (BLOCKING 7 + 권고 13 1pass 흡수 답습)

본 v1.1 보강 = `docs/review/3plus1-consensus-2026-05-28-mvp2-entry.md` §5 답습 1pass 흡수 (별도 v2 cycle 0, ceremony-inflation 차단).

### §11.1 BLOCKING 7 흡수 매트릭스

| # | 흡수 영역 | 답습 |
|---|---------|-----|
| B-1 (R-S1 CONFIRMED 격상) | §0.4 + §1.2 + §1.3 항목 2 + §2.2.1 + §3 (c) + §4.3 (4) + §4.4 신규 + §6.2 #12 + §9.5 + §10 P-4 | "잠재 risk" → "CONFIRMED divergence" 격상 + 5 source cross-confirm + 권위 인용 chain 정정 (G4 §4.4.1 + ADR-012 §2.8 PRIMARY, §2.3 = principle only) + 별도 cross-reference 정정 cycle 사용자 명시 영역 |
| B-2 (ADR-011 §2.1 framing 정정) | §0.2 #3 + #5, §0.4, §1.1, §3, §4.1, §7.1, §7.3, §9.1 다수 | "(a)~(e) 5조건" → "(a)~(d) 4조건 모법 + (e) 합의 APPROVE 후속 운영조건" 정정 |
| B-3 (§0.1 잔여 문구) | §0.1 | "(β) — 별도 합의 또는 (α) 內 흡수" → "(β) — 별도 합의 (본 cycle 內 흡수 0)" 정정 |
| B-4 (`agent/redact.py` framing) | §0.3 #2 + §1.1 51 entry row + §1.2 GP-2 row + §2.1.1 + §2.1.2 + §6.2 #11 + §9.3 + §9.4 + §10 P-3 | Hermes upstream 영역 vs 본 repo 영역 분리 framing + 51 audit brief carry-over 결함 명문 + Hermes upstream HEAD v0.12.0 401 LOC 답습 |
| B-5 (W-A framing 정밀화) | §1.3 항목 3 + §2.3.1 + §2.3.2 + §9.4 | 실 repo 기존 G4 workflow 답습 (`g4-hash-chain.yml` + `history-anchor-verifier.yml` + `rewrite-defense.yml`) + W-A 3 옵션 명시 |
| B-6 (PoC 시제 격상) | §0.3 #5 + #6 + §2.2.2 4 row + §3 (a)+(b)+(d) + §2.2.4 + §9.4 + §10 P-8 | "❌ gap" → "⚠️ PoC 시제 충족 / PASS 시제 미충족" 격상 + 실 PoC evidence 답습 (tools/jsonl_hash_chain.py + canonical_json.py + tests/canonical/ + g4-hash-chain.yml) |
| B-7 (§1.3 항목 5 + W 대안 매트릭스 확장) | §1.3 항목 5 신규 + §2.3.2 W 5 대안 + §4.1 (7) + §6.2 #13 + §9.2 | roadmap.md §5.4 "단축 합의" vs 본 cycle "풀 3+1 + 외부 LLM 1+" 격상 차이 명시 + W-A/B/C/D/E 5 대안 |

### §11.2 권고 13 흡수 매트릭스

| # | 흡수 영역 | 답습 |
|---|---------|-----|
| N-1 (후보 vs 발효 분리) | §0.2 #9 + §0.3 #26 + §0.4 + §2.1.3 + §2.2.3 + §5 (전체) + §7.3 (6) | "후보 채택" vs "구현 발효" 표현 분리 |
| N-2 (planning vs implementation track) | §2.2.3 + §8.1 항목 3 | G4 Layer 4 "planning/decision track" vs "implementation track" 분리 |
| N-3 (RT-5 분리) | §5.1 RT-5 + RT-5.1 신규 | "canonical JSON reference mismatch → BLOCK" vs "fallback canonicalizer used → ledger entry + review" 분리 |
| N-4 (E-9 attribution) | §5.2 E-9 | `external_llm_received` ledger entry + `agent="user"` 강제 + vendor/model/prompt hash/commit hash 명시 |
| N-5 (event enum reserved) | §5.3 + §9.5 | "reserved candidate" 격하 + ADR-012 §2.2 amendment 별도 cycle |
| N-6 (E-7 actual run id) | §5.2 E-7 | 42 entry actual run id `25623028888` 답습 framing 추가 |
| N-7 (trigger 4 격상) | §4.3 (4) | "부분 발화" → "발화" 격상 (B-1 R-S1 CONFIRMED 답습) |
| N-8 (24 entry 답습 변경 자격 명시) | §1.3 항목 4 | sub-수단 결정 분리 = 24 entry 답습 형태 변경 자격 명문 (25 조합 복잡도) |
| N-9 (헌법 8조 보조) | §1.1 헌법 row + §9.1 | 헌법 8조 본질 보조 영역 본문 답습 보강 |
| N-10 (Provider Liquidity) | §1.1 헌법 5조-2 row + §4.1 (6) + §9.1 | Provider Liquidity sub-수단 자격 평가 본문 명시 ((β) cycle 시점) |
| N-11 ((β) 분리 정당화) | §1.3 항목 4 | 25 조합 (R-1~R-5 × L-1~L-5) 복잡도 답습 정당화 |
| N-12 ((γ) 4 대안 + L-1.5) | §2.2.4 + §8.1 항목 2 | (γ-a/b/c/d) 4 대안 매트릭스 + L-1.5 alternative (stdlib + 자체 RFC 8785 test corpus 충분성) |
| N-13 (PASS 발효 사전조건) | §9.5 | Implementation Evidence PASS 발효 시점 R-S1 정정 사전조건 명문 |

### §11.3 v1.1 1pass 흡수 정직성

- 본 cycle = 1pass 흡수 (ceremony-inflation 차단 메모리 답습, 24 entry 동형 패턴)
- 별도 v2 cycle 진입 0건
- 본 v1.1 보강 시 추가 신규 자기 발견 잠재 risk 발생 = §10 P-8 추가 (Agent B 답습), §11 신설 한정 (별도 cycle 0)

---

**본 brief v1.1 끝.**

**다음 단계**: SESSION + INDEX commit + push (52 entry) → 본 cycle 합의 발효 (REVISE → v1.1 commit 후 자동 격상) → (β)/(γ)/실 구현 = 사용자 명시 별도 cycle.
