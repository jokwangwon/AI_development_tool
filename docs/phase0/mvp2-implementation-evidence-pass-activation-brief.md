# MVP-2 Implementation Evidence PASS (G4 ledger 완전 + GP-2 detection-tier, prevention/Layer 3·5/2a deferred) 발효 합의 entry brief (v1.1)

> **작성**: 2026-05-28 (62번째 entry 진입 cycle — 신규 세션 #2)
>
> **v1 → v1.1 갱신**: 풀 3+1 + 외부 LLM 1+ (codex gpt-5.5 cross-vendor) 통합 합의 (`docs/review/3plus1-consensus-2026-05-28-mvp2-final-pass.md`) **APPROVE WITH CONDITIONS (4 source 전원) → BLOCKING 3 + 권고 3 1pass 흡수**. ⭐ **핵심 정정 (B-1)**: 무수식 "MVP-2 PASS" 명칭 → **복합 자격 부착** (G4 ledger 완전 + GP-2 detection-tier, prevention R-1/R-2 + Layer 3·5 + 2a deferred) — 60 GP-2 detection-layer 강등 cascade 상위 재발 방지 (β B-1 / 59 B-2 / 60 B-1 4번째). B-2 "trajectory" 진행성 완화 + B-3 citation 정정. evidence 차단급 over-claim 0. §10 흡수 매트릭스 추가.
>
> **scope**: MVP-2 Implementation Evidence PASS **발효** (G4 ledger 무결성 *완전* + GP-2 송신 redaction *detection-tier*, prevention/Layer 3·5/2a *deferred*) — MVP-2 영역 (G2 GP-2 + G4 §4.4 Layer 1+2+4) 최종 milestone. ⚠️ **full GP-2 PASS (prevention) 아님**
>
> **본 cycle = 큰 cycle / 최종 milestone** (32 MVP-1 Implementation Evidence PASS 발효 답습 동형, 풀 3+1 + 외부 LLM 1+ + 사용자 명시 의무)
>
> **본 cycle 발효 자격** = 3 의존성 충족 (Layer 통합 PASS + GP-2 detection-layer PASS + R-S1) + 풀 3+1 + 외부 LLM 1+ APPROVE + 사용자 명시
>
> **본 cycle 발효 효과** = **MVP-2 Implementation Evidence PASS 발효** (in-repo governance/CI 구현 evidence). **full GP-2 prevention (R-1 Hermes runtime redaction / R-2 facade real) + Layer 3+5 = MVP-2 PASS 후속 trajectory (deferred, 자동 진입 0)**
>
> **선행 답습 (3 의존성 모두 발효)**: 59 Layer 1+2+4 통합 PASS (`0f49eb9`) + 60 GP-2 detection-layer PASS (`92e9078`) + 61 R-S1 정정 (`bb59342`)

---

## §0 본 brief 의 범위

### §0.1 본 brief 가 *하는* 것

1. **3 의존성 충족 audit** (Layer 통합 PASS + GP-2 detection-layer PASS + R-S1) (§1)
2. **MVP-2 영역 ADR-011 §2.1 (a)~(d) 모법 + (e2) ADR-012 §4 확장 통합 매핑** (59 B-2 framing 답습) (§2)
3. **MVP-2 PASS scope 정직 명문** — Implementation Evidence PASS (in-repo evidence) + full GP-2 prevention + Layer 3+5 = deferred trajectory (60 over-claim 교훈 답습) (§3)
4. **합의 형태 + 승격 트리거** (§4)
5. **PASS 발효 권고 + 조건 + 발효 시 효과 (roadmap/governance 등록 — 사용자 명시 후)** (§5)
6. 금지 / 다음 단계 / cross-ref / 자기진단 (§6~§9)

### §0.2 본 brief 가 *하지 않는* 것

| # | 영역 | 위반 |
|---|------|----|
| 1 | MVP-2 PASS *발효* 자체 (본 brief = 합의 입력, 발효 = 합의 APPROVE + 사용자 명시 후) | 0 |
| 2 | **full GP-2 PASS 발효** (prevention R-1/R-2 = deferred trajectory) | 0 |
| 3 | Layer 3 (Signed commit) + Layer 5 (External anchor) PASS 발효 | 0 ("부분 답습" 영구) |
| 4 | R-1 Hermes import / R-2 facade real (TR-1) | 0 |
| 5 | Layer 통합 PASS / GP-2 detection-layer PASS / R-S1 재선언 | 0 (59/60/61 답습) |
| 6 | MVP-1 PASS 재선언 (32 답습) | 0 |
| 7 | MVP-3~6 영역 진입 | 0 |
| 8 | Operational Readiness PASS / Hermes PMO 격상 | 0 |
| 9 | ADR / 헌법 / ADR-012 본문 갱신 (roadmap MVP-2 PASS 등록 = 발효 후 §5) | 0 |
| 10 | 신규 외부 library / Tier-2/3 catalog 확장 | 0 |
| 11 | 자동 후속 cycle 진입 | 0 (사용자 명시) |
| 12 | 본 brief 자체 영구화 / 권위 chain 등재 | 0 |

### §0.3 권위 답습 source

- **ADR-011 §2.1 (a)~(d) 4조건 모법** + **ADR-012 §4 (a)~(d)+(e) 확장** (PASS 발효 권위) — `docs/decisions/`
- **59 Layer 1+2+4 통합 PASS 발효 brief v1.1 + 합의** (`0f49eb9`) — `docs/phase0/mvp2-layer-124-pass-activation-brief.md`
- **60 GP-2 detection-layer PASS 발효 brief v1.1 + 합의** (`92e9078`) — `docs/phase0/mvp2-gp2-pass-activation-brief.md`
- **61 R-S1 cross-reference 정정** (`bb59342`) — `docs/decisions/ADR-012-evidence-ledger-protection.md` §2.3 + §2.8 note
- **32 MVP-1 Implementation Evidence PASS 발효 합의** (최종 milestone 패턴 답습) — `docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md`
- **implementation-runtime-roadmap-mvp1.md §1.3** (GP-2 = MVP-2 분리) + **`3plus1-consensus-2026-05-07-g2-g3-g4-gate-adoption.md §C-7`** (line 378~379, GP-2 = MVP-2 우선순위 1 — B-3 정정: roadmap.md 아님)

---

## §1 3 의존성 충족 audit

| 의존성 | 발효 | commit | scope |
|--------|------|--------|------|
| **G4 §4.4 Layer 1+2+4 통합 PASS** | ✅ 59 entry (APPROVE WITH CONDITIONS, 4 source) | `0f49eb9` | Layer 1 완전 + Layer 2 (2b operative + rewrite-defense CI 이중 cover, 2a DEFER no-op) + Layer 4 (3 ledger workflow green + canonical/timestamp BLOCK). "부분 답습" (Layer 3+5 scope 외) |
| **GP-2 detection-layer PASS** | ✅ 60 entry (REVISE → v1.1 detection-layer reframe, 4 source) | `92e9078` | R-3 detection operative (secret-hygiene D-2 CI green) + R-4 설계 동등성 + ADR 권위. **prevention (R-1 Hermes / R-2 facade) = deferred trajectory (in-repo 입증 0, Hermes upstream 위임)** |
| **R-S1 cross-reference 정정** | ✅ 61 entry (Reviewer-only 단축 APPROVE) | `bb59342` | ADR-012 §2.3/§2.8 canonical numbering 선언 (§2.8/G4 §4.4.1 5-layer = canonical). MVP-2 "Layer 1+2+4" = 5-layer 기준 확정 |

→ **3 의존성 모두 발효** — MVP-2 Implementation Evidence PASS 발효 자격 충족 ((e2) = 본 cycle).

---

## §2 MVP-2 영역 ADR-011 §2.1 (a)~(d) + (e2) 통합 매핑 (59 B-2 framing 답습)

> ⚠️ 59 B-2 답습: ADR-011 §2.1 = (a)~(d) 모법, "(e2) 합의 APPROVE" = ADR-012 §4 확장 + 프로젝트 내부 label.

| 조건 | G4 §4.4 Layer 1+2+4 | G2 GP-2 (detection-layer) | MVP-2 통합 |
|------|------|------|----|
| (a) 동등 이상 보안 결과 | ✅ ledger 무결성 (hash chain + append-only + CI 회귀) | ⚠️ detection ✅ / prevention (R-1/R-2) deferred (60 답습) | ✅ ledger 완전 + GP-2 detection (prevention deferred 명문) |
| (b) 격리 PoC | ✅ 59 (jsonl_hash_chain + fixtures + 3 G4 actual run) | ✅ 60 (secret-hygiene D-2 PoC) | ✅ |
| (c) ADR/SDD 권위 | ✅ G4 §4.4.1 + ADR-012 §2.3/§2.8 (R-S1 정정 후 canonical 명확) | ✅ ADR-011 §2.3 #2 + governance §4 | ✅ |
| (d) 자동 회귀 검증 | ✅ 3 ledger workflow CI green | ✅ secret-hygiene D-2 CI green | ✅ |
| **(e2) 합의 APPROVE** | ✅ 59 | ✅ 60 (detection-layer) | ⏳ **본 cycle (MVP-2 통합 PASS)** |

→ **(a)~(d) = Implementation Evidence scope 충족** (B-1 정정): G4 축 (a) = 무결성 *완전* / **GP-2 축 (a) = detection + 설계 동등성, prevention (R-1/R-2) deferred** (60 답습 — full prevention 충족 아님). (e2) = 본 cycle MVP-2 통합 PASS 합의.

---

## §3 MVP-2 PASS scope 정직 명문 (60 over-claim 교훈 답습)

⭐ **MVP-2 Implementation Evidence PASS = in-repo governance/CI 구현 evidence PASS** (MVP-1 PASS 32 동형 — "Implementation Evidence" = 구현 evidence, runtime 보증 아님).

**발효 범위 (operative in-repo)**:
- ✅ G4 ledger 무결성: Layer 1 (hash chain) + Layer 2 (2b branch protection + rewrite-defense CI) + Layer 4 (CI 회귀 검증) operative green
- ✅ GP-2 송신 redaction **detection**: secret-hygiene D-2 CI (redaction residual 검출) operative green

**deferred (명문, 자동 진입 0)** — ⚠️ B-2: "trajectory" 진행성 함의 회피 (R-1 = import 결정조차 미진입, R-2 = placeholder):
- ⚠️ **GP-2 prevention (능동 redaction)**: R-1 Hermes runtime redaction (upstream 위임, ADR-011 §2.3 #2) + R-2 facade real (TR-1) — **in-repo 입증 0 + Hermes safety 미선언** (ADR-011 §7.3 / ADR-012 §3.3 답습 — redaction-pattern-equivalence = 설계 동등성, 안전 선언 아님). R-1 import 미결정 / R-2 placeholder. **full GP-2 PASS = MVP-2 PASS 후속 (deferred)**
- ⚠️ **Layer 2a denyNonFastForwards**: non-bare clone no-op (2b + rewrite-defense CI 이중 cover), 실 bare/server 배포 시점
- ⚠️ **Layer 3 (Signed commit) + Layer 5 (External anchor)**: "부분 답습" scope 외 (RECOMMENDED MVP, MANDATORY multi-host)
- ⚠️ **R-5 base64 evasion**: known limitation (G3-4 MVP-2/3 분리)

→ **MVP-2 PASS = ledger 무결성 완전 + GP-2 detection operative + 설계/CI 권위. prevention runtime + Layer 3/5 + denyNonFastForwards = solo 1-host 비례 보안 + upstream 위임 deferred (over-claim 0, 정직 scope)**.

---

## §4 합의 형태 + 승격 트리거

### §4.1 합의 형태 = 풀 3+1 + 외부 LLM 1+ (의무)

**정당화**: MVP-2 최종 milestone (32 MVP-1 PASS 발효 답습) + 큰 결정 (ADR-011 §2.4 T3) + 헌법 5조-2 cross-vendor + 사용자 명시 (32 답습).

### §4.2 7 승격 트리거

| # | trigger | 발화 |
|---|---------|----|
| 1 | 큰 결정 (MVP-2 최종 PASS milestone) | ✅ |
| 2 | 아키텍처/SDD 본문 변경 | ❌ (brief = phase0 신규 1, roadmap 등록 = 발효 후) |
| 3 | ADR 본문 변경 | ❌ (R-S1 = 61 완료) |
| 4 | 권위 chain 다중 source 손상 | ❌ (R-S1 해소) |
| 5 | 외부 LLM 통합 필요 | ✅ cross-vendor 의무 |
| 6 | Tier-2/3 확장 | ❌ |
| 7 | Hermes PMO 격상 | ❌ |

→ **2/7 발화 → 풀 3+1 + 외부 LLM 1+ 적격**.

---

## §5 PASS 발효 권고 + 발효 시 효과

⭐ **권고 = MVP-2 Implementation Evidence PASS (G4 ledger 완전 + GP-2 detection-tier, prevention/Layer 3·5/2a deferred) 발효 APPROVE WITH CONDITIONS** (B-1: 복합 자격 부착, 무수식 "MVP-2 PASS" 회피):

1. **3 의존성 충족** (Layer 통합 PASS 59 + GP-2 detection-layer PASS 60 + R-S1 61) + (a)~(d) 충족.
2. **조건**:
   - (C-1) **MVP-2 PASS scope = Implementation Evidence (in-repo). full GP-2 prevention (R-1/R-2) + Layer 3/5 + 2a = deferred trajectory 명문** (§3, over-claim 0)
   - (C-2) **roadmap/governance MVP-2 PASS 등록 = 발효 후 별도 commit** (사용자 명시, 32 동형 — roadmap-mvp1 §2.2 갱신 패턴)
3. **MVP-3~6 영역 진입 = 본 PASS 무관** (별도).

### §5.1 발효 시 효과 (사용자 명시 발효 후)

- `implementation-runtime-roadmap.md` / `-mvp1.md`: MVP-2 Implementation Evidence PASS 발효 등록 (별도 commit, 발효 후)
- governance-preconditions §4 (GP-2): detection-layer PASS + prevention deferred cross-reference (선택)
- MVP-2 PASS = MVP-3 (다른 GP/G 영역) 진입 자격 (별도 cycle)

→ **MVP-2 PASS 발효 자격 = 3 의존성 + (a)~(d) + (e2) 합의 APPROVE + 사용자 명시 + (C-1) deferred trajectory 명문**.

---

## §6 금지 사항

§0.2 답습 (12). 추가: full GP-2 PASS 자동 발효 0 / Layer 3/5 진입 0 / R-1 import 0 / R-2 facade 0 / MVP-3~6 자동 진입 0 / roadmap 본문 자동 갱신 0 (발효 후 별도) / 자동 후속 0.

---

## §7 다음 단계 (사용자 명시 의무 — 자동 진입 0)

1. 본 brief 승인 → 풀 3+1 + 외부 LLM 1+ (codex (E-α)) → Reviewer 통합 → v1.1 흡수 → commit + push → 🎉 **MVP-2 Implementation Evidence PASS 발효 (G4 ledger 완전 + GP-2 detection-tier, prevention/Layer 3·5/2a deferred — ⚠️ full GP-2 PASS 아님)**
2. roadmap/governance MVP-2 PASS 등록 (발효 후 별도 commit, 사용자 명시)
3. **full GP-2 PASS trajectory** (R-1 Hermes runtime redaction import / R-2 facade real TR-1 prevention)
4. (선택) Layer 3 (Signed commit) / Layer 5 (External anchor) / MVP-3 영역 진입

---

## §8 cross-reference 답습

- ADR-011 §2.1 (a)~(d) + ADR-012 §4 (e 확장) + §2.3/§2.8 (R-S1 정정 후)
- 59 Layer 통합 PASS (`0f49eb9`) + 60 GP-2 detection-layer PASS (`92e9078`) + 61 R-S1 (`bb59342`)
- 32 MVP-1 PASS 발효 합의 (패턴 답습)
- implementation-runtime-roadmap-mvp1.md §1.3 + `3plus1-consensus-2026-05-07-g2-g3-g4-gate-adoption.md §C-7` (GP-2 = MVP-2, B-3 정정)

---

## §9 자기진단 (메타 편향 회피)

| # | 위험 | 처리 |
|---|------|----|
| P-1 | MVP-2 PASS *기정사실화* | 발효 = 합의 APPROVE + 사용자 명시 후 (§0.2 #1 + §7) |
| P-2 | **MVP-2 "full PASS" over-claim (60 GP-2 over-claim 재발)** | §3 정직 scope 명문 — Implementation Evidence PASS (in-repo), full GP-2 prevention + Layer 3/5 + 2a = deferred trajectory. "runtime 완전 보증" 표현 0 |
| P-3 | GP-2 detection-layer 를 MVP-2 통합 시 "full GP-2" 로 격상 | §1 + §2 (a) + §3 = GP-2 detection-layer + prevention deferred 일관 명문 |
| P-4 | 본 brief 작성자 = 59/60/61 작성자 (Claude) cascade | cross-vendor codex + 풀 3+1 독립 검증 (59/60 over-claim 포착 process 가치) |
| P-5 | citation 부정확 (59 B-1 재발) | §1 commit hash 직접 verify (`0f49eb9`/`92e9078`/`bb59342`) |
| P-6 | (e2) 권위 전도 (59 B-2 재발) | §2 "(a)~(d) ADR-011 모법 + (e2) ADR-012 §4 확장" framing 답습 |

---

---

## §10 v1.1 흡수 매트릭스 (BLOCKING 3 + 권고 3 1pass — 명칭 복합 자격 부착)

본 v1.1 = `docs/review/3plus1-consensus-2026-05-28-mvp2-final-pass.md` 답습 1pass 흡수 (52/57/59/60 동형). **4 source 전원 APPROVE WITH CONDITIONS** (evidence 실증, 차단급 over-claim 0).

| # | 흡수 | source | 정정 |
|---|------|--------|------|
| B-1 ⭐ (4 source 수렴) | 무수식 "MVP-2 PASS" → 복합 자격 "(G4 ledger 완전 + GP-2 detection-tier, prevention/Layer 3·5/2a deferred)" 부착 (title + §2 결론 + §5 + §7) + "GP-2 detection-layer PASS" 고정 — 60 cascade 상위 재발 방지 | Agent C R-C-1 + Agent B R-B-1 + codex 권고 1/2/3 | title/§2/§3/§5/§7 |
| B-2 | "deferred trajectory" → "deferred (R-1 import 미결정 / R-2 placeholder, in-repo 입증 0 + Hermes safety 미선언)" | Agent B R-B-2 | §3 |
| B-3 | citation "roadmap.md §C-7" → `3plus1-consensus-2026-05-07-g2-g3-g4-gate-adoption.md §C-7` + roadmap-mvp1 §1.3 | Agent A R-A-1 | §0.3 + §8 |
| N-1 | actual run id anchor | Agent A | §1 (선택) |
| N-2 | deferred 진입 trigger 매트릭스 | Agent C | §3 (선택) |
| N-3 | MVP-1 Implementation Evidence framing 일관 | Agent B | §3 |

**4 source 정합**: 3 의존성 commit 실재 + hash 정확 (`0f49eb9`/`92e9078`/`bb59342`) + pytest 152 + scope 차단급 over-claim 0 + (e2) 권위 전도 0 + scope 침입 0 + 발효 형태 32 일관.

---

**본 brief v1.1 끝.**

**다음 단계**: SESSION + INDEX commit + push → 🎉 **MVP-2 Implementation Evidence PASS 발효 (G4 ledger 완전 + GP-2 detection-tier, prevention/Layer 3·5/2a deferred)**. 후속: roadmap/governance MVP-2 PASS 등록 (발효 후 별도 commit) + full GP-2 PASS trajectory (R-1/R-2) = 사용자 명시 별도 cycle.
