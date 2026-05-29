# GP-2 prevention PASS (R-2 in-repo operative + R-1 조건부 위임; 실 canary/R-6 Hermes trigger deferred) 발효 합의 entry brief (v1.1)

> **작성**: 2026-05-28 (67번째 entry 진입 cycle — 세션 #3, SC-3)
>
> **v1 → v1.1 갱신 (reframe)**: 풀 3+1 + 외부 LLM 1+ (codex gpt-5.5 cross-vendor) 통합 합의 (`docs/review/3plus1-consensus-2026-05-28-mvp2-sc3.md`) **REVISE ("full" 명칭 over-claim) → BLOCKING 3 + 권고 4 reframe 흡수** (60 detection reframe 동형, 본 세션 #3 두 번째 cascade). **핵심 정정 (B-1, 4 source 수렴)**: **"GP-2 full PASS" → "GP-2 prevention PASS"** ("full" 완전 제거 — 60 "GP-2 (full) PASS → detection-layer 강등" 선례 직접 충돌, R-1 조건부인데 "full" 부정직, Agent C REVISE + B BLOCKING + codex 조건1) + **축약 금지 규칙** (발효/commit/ledger/INDEX 모든 표기 parenthetical 탈락 금지). **B-2** 커버리지 92% (redaction.py 90% + facade.py 96%) 정확 표기. **B-3** Exit (a) "충족" → "조건부 충족". evidence/발효 자격 정당 (4 source 실증), 명칭만 정정. §11 흡수 매트릭스 추가.
>
> ⚠️ **파일명 주석**: 파일명 `mvp2-sc3-full-gp2-pass-*` 의 "full" = cycle 식별자 (작성 시점), **발효 명칭 = "GP-2 prevention PASS"** (B-1 reframe).
>
> **scope**: **GP-2 송신 redaction PASS 발효 — detection-tier → prevention-tier 격상** (60 GP-2 detection-layer PASS 의 deferred prevention trajectory 완성). **복합 자격 (62 명칭 패턴 답습, over-claim 차단)**: detection operative (R-3) + prevention **R-2 in-repo operative** (65 SC-1) + prevention **R-1 조건부/문서 기반 위임 검증** (66 SC-2, 활성화 전제 + R-6 Tier-1 한정 + 실 격리 canary deferred).
>
> ⚠️ **명칭 정직성 (본 세션 #3 2회 + 세션 #2 4회 = 6회 over-claim cascade 교훈)**: "GP-2 prevention PASS" = GP-2 = detection-layer(60) + prevention(본 cycle) 누적. prevention = **R-2 in-repo operative + R-1 조건부**. ⚠️ **"GP-2 full / 완전 PASS" 영구 금지** (R-1 조건부 + R-5 base64 evasion deferred — "full" 부정직). 무수식 "prevention 완전 보증" 금지. **축약 금지**: 모든 후속 표기 = "GP-2 prevention PASS (R-2 operative + R-1 조건부; canary/R-6 deferred)" parenthetical 유지.
>
> **본 cycle = 큰 cycle / PASS 발효 milestone** (60 GP-2 detection-layer PASS + 62 MVP-2 PASS + 32 MVP-1 PASS 답습 동형, 풀 3+1 + 외부 LLM 1+ + 사용자 명시 의무).
>
> **본 cycle 발효 자격** = detection (60 ✅) + R-2 in-repo (65 ✅) + R-1 조건부 위임 (66 ✅) + (e) 풀 3+1 + 외부 LLM 1+ APPROVE + 사용자 명시.
>
> **본 cycle 발효 효과** = **GP-2 prevention PASS 발효** (Exit (a) prevention R-1 ∧ R-2 검증 *조건부 충족* — R-2 operative + R-1 conditional/document-based) — 60 detection-layer PASS 의 prevention trajectory 발효 (R-2 operative + R-1 조건부). **잔여 deferred (자동 진입 0)**: R-1 실 격리 canary 실행 + R-6 Hermes dependency lock trigger 확장 + R-5 base64 evasion (영구 분리).
>
> **선행 답습**: 60 GP-2 detection-layer PASS (`92e9078`) + 65 SC-1 (R-2 facade RedactionFilter in-repo operative) + 66 SC-2 (R-1 위임 검증 조건부/문서 기반) + 62 MVP-2 PASS (명칭 복합 자격 패턴) + governance §4.5 Exit (a)~(e)

---

## §0 본 brief 의 범위

### §0.1 본 brief 가 *하는* 것

1. **GP-2 Exit 5조건 통합 evidence 매트릭스** (detection + prevention R-2 + R-1) (§2)
2. **detection-tier → prevention-tier 격상 정당성** (60 deferred 완성) (§3)
3. **명칭 복합 자격 + prevention 조건부 scope 정직 명문** (62 답습, over-claim 차단) (§4)
4. **GP-2 prevention PASS 발효 권고 + 조건** (§5)
5. **합의 형태 + 잔여 deferred + 금지 + Rollback + 자기진단** (§6~§10)

### §0.2 본 brief 가 *하지 않는* 것

| # | 영역 | 위반 |
|---|------|----|
| 1 | **"GP-2 완전 PASS / prevention 완전 보증" over-claim** (R-1 조건부 명문 — 실 canary/R-6 Hermes trigger deferred) | 0 |
| 2 | **Hermes 안전성 선언** (ADR-011 §7.3) / runtime egress 완전 PASS | 0 |
| 3 | **MVP-2 PASS (62) 재선언** (답습 유지 — 본 cycle = GP-2 prevention-tier 격상 한정) | 0 |
| 4 | R-1 실 격리 canary 실행 (artifact 재확보 deferred) / R-6 Hermes lock trigger 확장 | 0 |
| 5 | R-5 base64/URL evasion (영구 분리, G3-4) | 0 |
| 6 | detection-layer PASS (60) / SC-1 (65) / SC-2 (66) 재선언 | 0 |
| 7 | Layer 3·5 / 2a / SC-Provider Liquidity (Router 위임) 진입 | 0 |
| 8 | ADR / 헌법 / governance / roadmap 본문 갱신 (발효 후 별도) | 0 |
| 9 | 실 코드 / CI / config 본문 변경 | 0 |
| 10 | 자동 후속 (MVP-3 / R-6 확장 / 실 canary) 진입 | 0 (사용자 명시 의무) |

### §0.3 권위 답습 source

- **governance §4.5 Exit (a)~(e)** — (a) "Hermes native redaction Tier-1 42 catalog 적용 검증 + facade redaction filter 검증" (R-1 ∧ R-2)
- **60 GP-2 detection-layer PASS brief** (`mvp2-gp2-pass-activation-brief.md`) — §2 3축 (detection ✅ / 설계 동등성 / prevention deferred), §6 발효 권고
- **65 SC-1 brief + 합의** (`mvp2-sc1-facade-redaction-implementation-brief.md`) — R-2 facade RedactionFilter in-repo operative (group-aware 치환, 15 test, 커버리지 92% (redaction.py 90% + facade.py 96%))
- **66 SC-2 brief + 합의** (`mvp2-sc2-r1-hermes-delegation-verification-brief.md`) — R-1 조건부/문서 기반 위임 검증 (4축, 활성화 전제 + R-6 Tier-1 한정)
- **62 MVP-2 PASS brief** (`mvp2-implementation-evidence-pass-activation-brief.md`) — 명칭 복합 자격 패턴 (over-claim 차단) + GP-2 detection-tier deferred trajectory
- **ADR-011 §2.1 (a)~(d) + §2.3 #2 (위임) + §7.3 (안전성 선언 금지)** + **ADR-012 §4 (e2 확장)**

---

## §1 진입 컨텍스트

- 60 GP-2 detection-layer PASS 발효 (R-3 detection operative + prevention R-1/R-2 deferred).
- 62 MVP-2 PASS = G4 ledger 완전 + GP-2 **detection-tier** (GP-2 prevention (R-1/R-2) = 후속 trajectory).
- 65 SC-1 → R-2 (facade RedactionFilter) **in-repo operative** (placeholder → real, deferred 해소).
- 66 SC-2 → R-1 (Hermes 위임) **조건부/문서 기반 검증** (위치 ✅ + 동등성 ✅ + 자동회귀 Tier-1 한정 + 활성화 전제).
- → 본 SC-3 = GP-2 prevention (R-1 ∧ R-2) trajectory 완성 → **GP-2 detection-tier → full PASS 격상**.

---

## §2 GP-2 Exit 5조건 통합 evidence 매트릭스 (detection + prevention)

| # | 조건 | detection (60) | prevention R-2 (65 SC-1) | prevention R-1 (66 SC-2) | 통합 판정 |
|---|------|------|------|------|------|
| (a) | 동등 이상 보안 결과 | R-4 설계 동등성 (Tier-1 42) | ✅ **facade RedactionFilter in-repo** (group-aware, Tier-1 45 catalog 공유) | ⚠️ **조건부** (Hermes 47 ⊇ Tier-1, 활성화 전제) | ✅ **R-1 ∧ R-2 prevention 검증 충족** (R-2 강 + R-1 조건부) |
| (b) | 격리 PoC 실증 | ✅ secret-hygiene D-2 | ✅ **redaction 15 test (커버리지 92% (redaction.py 90% + facade.py 96%))** | ⚠️ 실 격리 canary deferred (day2-r1 코드 분석) | ✅ in-repo PoC 충족 / R-1 실 canary deferred |
| (c) | ADR/SDD 권위 | ✅ ADR-011 §2.3 #2 + governance §4 | ✅ ADR-009 §2.2 (facade 단일 진입점) | ✅ ADR-011 §2.3 #2 (위임) | ✅ |
| (d) | 자동 회귀 검증 | ✅ secret-hygiene D-2 CI | ✅ **redaction test (pytest 167)** | ⚠️ R-6 Tier-1 canary (Hermes lock trigger 미구현) | ✅ in-repo 회귀 / R-1 Hermes trigger deferred |
| (e) | 합의 APPROVE | ✅ 60 | ✅ 65 | ✅ 66 | ⏳ **본 SC-3** |

→ **(a)~(d) prevention 검증 *조건부 충족*** (R-2 in-repo operative + R-1 conditional basis). (e) = 본 cycle. **GP-2 prevention PASS = detection + prevention (R-2 operative + R-1 조건부)** (R-1 조건부 명문).

---

## §3 detection-tier → prevention-tier 격상 정당성 (60 deferred 완성)

- 60 GP-2 detection-layer PASS = R-3 detection operative + **prevention (R-1/R-2) deferred trajectory** (in-repo 입증 0).
- 본 SC-3 = 그 deferred trajectory 완성:
  - **R-2 deferred 해소**: 65 SC-1 → facade RedactionFilter in-repo operative (placeholder → real, group-aware 치환 + 15 test). **in-repo 능동 redaction 보증 1 확보** (60 §3.2 B-2 "in-repo 능동 redaction 보증 0" 해소).
  - **R-1 조건부 충족**: 66 SC-2 → Hermes 위임 검증 (위치 + 동등성 + 권위, 조건부).
- → GP-2 = detection (R-3) + prevention (R-2 in-repo + R-1 위임) = **full PASS scope** (Exit (a) R-1 ∧ R-2).

⚠️ **cover 구조 (60 B-2 답습 — 비대칭 해소)**: 60 = prevention in-repo cover 0 (Hermes 단독 위임). 65 SC-1 → **in-repo prevention cover 1 (R-2 facade)** + Hermes 위임 (R-1) = 이중 cover (비대칭 부분 해소).

---

## §4 명칭 복합 자격 + prevention 조건부 scope 정직 명문 (62 답습, over-claim 차단)

⭐ **명칭 = "GP-2 prevention PASS (detection operative + prevention: R-2 in-repo operative + R-1 조건부/문서 기반 위임; 실 격리 canary + R-6 Hermes lock trigger deferred)"** — 62 복합 자격 패턴 답습.

**발효 범위 (operative)**:
- ✅ detection (R-3 secret-hygiene D-2 CI green)
- ✅ prevention R-2 (facade RedactionFilter in-repo, group-aware 치환, 15 test, pytest 167)

**조건부 (정직 명문)**:
- ⚠️ prevention R-1 (Hermes 위임) = **조건부/문서 기반** — 위치 (day2-r1 2026-05-05 코드 분석) + 동등성 (R-4 §5 Hermes ⊇ Tier-1) + 권위 (ADR-011 §2.3 #2). **활성화 전제 (HERMES_REDACT_SECRETS=true)** + **R-6 Tier-1 canary 한정 (Hermes dependency lock trigger 미구현)** + **실 격리 canary deferred** (artifact 재확보).

**deferred (자동 진입 0)**:
- ⚠️ R-1 실 격리 canary 실행 (Hermes re-clone, URL 확보 선결)
- ⚠️ R-6 Hermes dependency lock trigger 확장 (hermes-version.yaml 파일 + lock diff)
- ⚠️ R-5 base64/URL/압축 evasion (영구 분리, G3-4 — Tier-1 42 평문 한정)

→ **GP-2 prevention PASS = detection + prevention 조건부 충족 (Exit (a) R-1 ∧ R-2 — R-2 operative + R-1 conditional). prevention R-1 조건부 + R-5 evasion + 실 canary deferred = 정직 scope (over-claim 0, "full" 영구 회피)**.

---

## §5 GP-2 prevention PASS 발효 권고 + 조건

⭐ **권고 = GP-2 prevention PASS 발효 APPROVE WITH CONDITIONS** (복합 자격, prevention R-1 조건부 명문):

1. **detection (60 ✅) + prevention R-2 in-repo (65 ✅) + R-1 조건부 위임 (66 ✅) + (e) 본 cycle** → Exit (a)~(e) 충족 (R-1 조건부).
2. **조건**:
   - (C-1) **명칭 복합 자격 부착** — 무수식 "GP-2 완전 PASS" 금지, prevention R-1 조건부 + deferred 명문 (62 B-1 답습)
   - (C-2) **R-1 = 조건부/문서 기반** (활성화 전제 + R-6 Tier-1 한정 + 실 canary deferred, 66 답습)
   - (C-3) **R-5 base64 evasion = known limitation** (Tier-1 42 평문 한정)
   - (C-4) **MVP-2 PASS (62) 재선언 0** — 본 cycle = GP-2 detection-tier → prevention-tier 격상 한정 (MVP-2 PASS 명칭 갱신 = 발효 후 별도 chore)
3. **잔여 deferred 명문** (§4) — 자동 진입 0.

→ **GP-2 prevention PASS 발효 자격 = detection + prevention (R-2 in-repo + R-1 조건부) + (e) 합의 APPROVE + 사용자 명시 + (C-1) 복합 자격**.

---

## §6 합의 형태 + 승격 트리거

### §6.1 합의 형태 = 풀 3+1 + 외부 LLM 1+ (의무)

**정당화**: PASS 발효 milestone (60/62/32 답습) + 큰 결정 (ADR-011 §2.4 T3) + 보안 (GP-2 prevention) + 5조-2 cross-vendor + 사용자 명시.

### §6.2 승격 트리거

| # | trigger | 발화 |
|---|---------|----|
| 1 | 큰 결정 (GP-2 prevention PASS milestone) | ✅ |
| 2 | 보안 (GP-2 prevention 발효) | ✅ |
| 3 | 외부 LLM cross-vendor (5조-2) | ✅ |
| 4 | 명칭 over-claim risk (60/62 cascade 답습) | ✅ |

→ **4/4 발화 → 풀 3+1 + 외부 LLM 1+**.

---

## §7 잔여 deferred (자동 진입 0)

1. **R-1 실 격리 canary 실행** — Hermes re-clone (URL 확보) + HERMES_REDACT_SECRETS=true + canary 주입 (SC-2 C-3 SOP). GP-2 prevention PASS 강한 보강.
2. **R-6 Hermes dependency lock trigger 확장** — hermes-version.yaml 파일 + lock diff trigger (SC-2 B-1 잔여).
3. **R-5 base64 evasion** — 영구 분리 (G3-4).
4. **MVP-2 PASS 명칭 갱신** — GP-2 detection-tier → full PASS (roadmap/62 cross-reference, 발효 후 chore).

---

## §8 금지 사항

§0.2 답습 (10). 추가: "GP-2 완전 PASS" 무수식 0 / Hermes 안전성 선언 0 / R-1 "실 canary 완료" 주장 0 / MVP-2 PASS 재선언 0 / 자동 후속 0.

---

## §9 Rollback Trigger

| # | trigger | 대응 |
|---|---------|----|
| RT-1 | "GP-2 완전 PASS" over-claim 발생 | §4 복합 자격 명문 (prevention R-1 조건부 + deferred) |
| RT-2 | R-2 facade redaction 회귀 (15 test FAIL) | pytest CI + RedactionFilter 불변성 (65 답습) |
| RT-3 | R-1 실 격리 canary 실행 시 day2-r1 결론 불일치 | C-3 SOP 결과 우선 → R-1 위임 검증 재평가 |
| RT-4 | Hermes upstream redaction silent 깨짐 | R-6 Tier-1 canary + R-5 재검증 (단 Hermes trigger deferred) |
| RT-5 | base64 evasion 발견 | known limitation (R-5 영구 분리) |

---

## §10 Evidence

- E-1: detection (60, secret-hygiene D-2 CI green)
- E-2: prevention R-2 (65 SC-1, facade RedactionFilter 15 test + 커버리지 92% (redaction.py 90% + facade.py 96%) + pytest 167)
- E-3: prevention R-1 (66 SC-2, 위치 + 동등성 + 권위 조건부)
- E-4: Exit (a)~(e) 통합 매트릭스 (§2)
- E-5: 복합 자격 명칭 (over-claim 0)

---

## §11 자기진단 (메타 편향 회피)

| # | 위험 | 처리 |
|---|------|----|
| P-1 | "GP-2 완전 PASS" over-claim (60/62 cascade 재발) | §4 복합 자격 (prevention R-1 조건부 + deferred), [[feedback_pass_scope_overclaim]] |
| P-2 | prevention "충족"이 R-1 실 canary 미실행 은폐 | §2/§4 — R-1 조건부/문서 기반 명문 (66 답습), 실 canary deferred |
| P-3 | Hermes 안전성 선언 격상 | §0.2 #2 — 위임 검증 ≠ 안전 선언 (ADR-011 §7.3) |
| P-4 | MVP-2 PASS (62) 재선언 | §0.2 #3 + (C-4) — GP-2 prevention-tier 격상 한정 |
| P-5 | R-2 in-repo = full runtime 보증 오인 | §4 — R-2 = facade redaction layer (Router deferred, 65 답습) |
| P-6 | 작성자 = 60/62/65/66 작성자 (Claude) cascade | cross-vendor codex + 풀 3+1 독립 검증 (본 세션 over-claim 5회 포착 입증) |
| P-7 | R-1 조건부를 "충족"으로 단순화 | §4 — R-1 활성화 전제 + R-6 Tier-1 한정 + 실 canary deferred 3중 명문 |

---

## §12 v1.1 흡수 매트릭스 (BLOCKING 3 + 권고 4 reframe)

본 v1.1 = `docs/review/3plus1-consensus-2026-05-28-mvp2-sc3.md` 답습 1pass reframe 흡수 (60 detection reframe 동형). **4 source: Agent C REVISE + codex/Agent A/Agent B APPROVE WITH CONDITIONS → REVISE ("full" over-claim)**. evidence/발효 자격 정당 (실증), 명칭만 정정. **본 세션 #3 두 번째 over-claim cascade** (SC-2 R-6 + SC-3 "full"), 전체 누적 6회 포착.

| # | 흡수 | source | 정정 위치 |
|---|------|--------|------|
| B-1 ⭐ | **"GP-2 full PASS" → "GP-2 prevention PASS"** ("full" 완전 제거 — 60 강등 선례 충돌, R-1 조건부) + 축약 금지 규칙 | Agent C REVISE + B + codex (4 source) | title + 전체 + header |
| B-2 | 커버리지 92% → 92% (redaction.py 90% + facade.py 96%) 정확 표기 | Agent A | §0.3 + §2 + §10 |
| B-3 | Exit (a) "충족" → "조건부 충족" (R-2 operative + R-1 conditional) | Agent B + codex | §2 + §4 + 발효 효과 |
| R-1 | "(a)~(d) prevention 검증 충족" → "조건부 충족" 완화 | codex 3 | §2 |
| R-2 | deferred (실 canary/R-6/활성화) "완료" 표기 금지 — 지속 명문 | codex 조건3 | §4/§7 |
| R-3 | 후속 MVP-2 = cross-reference 갱신/chore (재선언 0) | codex 4 | §7 (4) |
| R-4 | 파일명 "full" = cycle 식별자 (발효 명칭 = "GP-2 prevention PASS") 주석 | Reviewer | header 주석 |

**4 source 정합 (positive)**: evidence 전원 실재 (Agent A filesystem + pytest 167 + secret_scanner 45 equivalence) / 권위 인용 일치 (codex 6/6 + Agent B 10/10) / Hermes 안전성 선언 0 + MVP-2 재선언 0 + prevention 조건부 scope 정직 (1차 견고). "full" 명칭만 over-claim.

---

**본 brief v1.1 끝.**

**다음 단계**: SESSION + INDEX commit + push → **GP-2 prevention PASS 발효 (R-2 in-repo operative + R-1 조건부 위임; 실 canary/R-6 Hermes trigger deferred — "full" 영구 회피)**. 후속: R-1 실 격리 canary 실행 / R-6 Hermes lock trigger 확장 / MVP-2 PASS cross-reference 갱신 (chore) / MVP-3 영역 진입 = 사용자 명시 별도 cycle.
