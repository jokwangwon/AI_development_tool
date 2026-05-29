# 3+1 합의 (Reviewer 통합) — SC-2 R-1 Hermes 위임 검증 brief

> **cycle**: 66번째 entry — SC-2 R-1 Hermes 위임 검증 brief (세션 #3)
> **대상**: `docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md` (v1)
> **합의 형태**: 풀 3+1 + 외부 LLM 1+ (cross-vendor codex gpt-5.5)
> **4 source**: codex (OpenAI) + Agent A (구현) + Agent B (안전) + Agent C (대안)
> **작성**: 2026-05-28

---

## §0 통합 판정

⭐ **APPROVE WITH CONDITIONS (4 source 전원)** — **BLOCKING 4 + 권고 4 → brief v1.1 reframe 흡수** ("충족" → **조건부/문서 기반 충족**, 60 entry detection reframe 동형). evidence 실증 (day2-r1 위치 + R-4 동등성), **framing over-claim 정정** (R-6 자동 회귀 + activation 전제 + "충족" 강도).

| source | 판정 | BLOCKING | 핵심 |
|--------|------|----------|------|
| codex (OpenAI gpt-5.5) | APPROVE WITH CONDITIONS | 0 (조건 3) | R-6 표현 축소 + HERMES_REDACT_SECRETS + "R-1 prong 충족" → Exit (a) sub-evidence. 권위 6/8 일치 (R-6 부분/dependency trigger 미구현) |
| Agent A (구현) | APPROVE WITH CONDITIONS | 2 | R-6 영역 오귀속 (Tier-1 canary ≠ Hermes egress) + 위치 evidence 시점성. R-2 prong 167 green 실측 |
| Agent B (안전) | APPROVE WITH CONDITIONS | 2 | R-6 자동 회귀 over-claim (60 B-1 재발) + HERMES_REDACT_SECRETS opt-in 전제 누락 |
| Agent C (대안) | APPROVE WITH CONDITIONS | 3 | R-6 = R-2 trigger 회귀 (R-1 착시) + URL 출처 정정 + docker 골격 존재 |

→ **60 entry over-claim cascade 재발** (4 source 또 framing over-claim 포착 — process 가치 재입증). 본 세션 #3 첫 over-claim 포착.

---

## §1 BLOCKING (Reviewer 독립 verify 후 흡수 의무)

### B-1 ⭐ (4 source 수렴, Reviewer verify CONFIRMED) — R-6 자동 회귀 over-claim (축 3)

| source | 입장 |
|--------|------|
| codex | R-6 trigger path = docker/r4-1-poc, docker/r2-poc, docs, workflow뿐. hermes-version.yaml/lock diff trigger 없음 → "Tier-1 42 canary까지만 operative" |
| Agent A | R-6 = GP-1 DB trigger UDF/Tier-1 canary, Hermes GP-2 egress 자동 회귀 아님 (영역 오귀속) |
| Agent B | "자동 회귀 ✅" = Hermes upstream 자동 검출 함의 over-claim (60 B-1 framing 재발) |
| Agent C | R-6 = R-2 trigger 회귀 검증 (R-1 자동 보증 착시 제거) |

**Reviewer verify** (직접 read `.github/workflows/r2-canary.yml`):
- workflow name = **"R-4.1 Tier-1 42 canary regression"** + step "Run R-4.1 PoC (Docker isolation, Tier-1 42 canary)".
- paths trigger = `docker/r4-1-poc/**` + `docker/r2-poc/**` + `canary-recheck-design.md` + `r2-canary.yml`. **hermes-version.yaml / Hermes dependency lock diff trigger 0**.
→ ✅ **CONFIRMED**: R-6 = **R-4.1 Tier-1 42 catalog (secret_scanner 패턴) canary regression**, Hermes native redaction egress 자동 회귀 *아님*.

→ **흡수 (B-1)**: 축 3 "자동 회귀 ✅" → "ADR-011 §2.3 #4 / governance Layer 1 = 자동 재실행 ***의무 요구***, **현 R-6 = Tier-1 42 catalog canary regression operative (Hermes dependency lock diff trigger 미구현)**". Hermes native redaction 자동 회귀 ≠ 현 R-6 (착시 제거).

### B-2 ⭐ (codex + Agent A + Agent B, Reviewer verify CONFIRMED) — HERMES_REDACT_SECRETS opt-in 활성화 전제

- **Reviewer verify** (R-4 line 138): `HERMES_REDACT_SECRETS=false` (opt-in) — **v0.12.0 breaking change로 default ON→OFF**. day2-r1 §2 "security.redact_secrets: true 활성화 후" 전제.
→ ✅ **CONFIRMED**: Hermes redaction = **명시적 활성화 필요** (기본 off).
→ **흡수 (B-2)**: 축 1 "Hermes redaction = GP-2 영역 적용 ✅" → "***활성화된 (HERMES_REDACT_SECRETS=true)*** Hermes redaction 코드 경로 = GP-2 영역". **활성화 전제 (5번째 축 또는 전제 조건) 신설** — 위임 실효 = 활성화 전제 (미활성화 시 redaction 미작동).

### B-3 (Agent C, Reviewer verify 부분 정정) — 사실 정정 2건

- **(a) docker/r2-poc 격리 골격 존재** ✅ CONFIRMED (Dockerfile + docker-compose.r2-poc.yml + r2_poc.py 10788B) → "artifact 완전 부재" 단정 완화. ⚠️ 단 docker/r2-poc = **우리 R-2 PoC (SQLite trigger, GP-1)** 골격, **Hermes `agent/redact.py` 아님** (Hermes artifact는 여전히 부재).
- **(b) Hermes upstream URL 출처** — Reviewer verify: day2-r1 §3.1 = grep 명령어 (URL 아님), ADR-008 = 미확인. **URL 출처 불명** (Agent C "day1 §3.1 명시"도 부분 부정확).
→ **흡수 (B-3)**: §4 "artifact 부재" → "Hermes `agent/redact.py` artifact 부재 (단 R-2 PoC 격리 골격 docker/r2-poc 존재)". §3 C-3 SOP "URL = ADR-008 출처" → "Hermes upstream clone URL 출처 확보 선결 (문서 미명시)".

### B-4 (Agent A) — 위치 evidence 시점성

- day2-r1 (2026-05-05) 위치 검증 = Hermes v0.12.0 코드 분석. artifact 부재로 *현 시점 재확인 불가* (시점성).
→ **흡수 (B-4)**: §2.1 "위치 검증 (2026-05-05 day2-r1 코드 분석 시점, artifact 부재로 현 재확인 = C-3 SOP artifact 재확보 시)" 시점성 명시.

---

## §2 권고 (흡수 — 채택)

| # | 권고 | source | 흡수 |
|---|------|--------|------|
| R-1 | "R-1 prong 충족" → "Exit (a) Hermes-native sub-evidence 조건부/문서 기반 충족" 좁히기 | codex 3 | §5 + title framing |
| R-2 | 동등성 출처 = R-4 §5 **+ R-4.1/R-6 catalog 체계** (R-4 §5 단독 아님) | codex 4 | §2.2 |
| R-3 | GP-2 Exit (b)/(d) 격리 PoC + R-6 log canary = SC-3 또는 별도 (R-1 prong과 경계) | codex 3 | §5 |
| R-4 | version pin contract = 문서 명문 수준 vs 파일 enforcement 구분 | codex NOTE | §3 C-1 |

---

## §3 Reviewer 독립 verify (5 source 격상)

| 항목 | verify 결과 |
|------|------|
| R-6 = Tier-1 canary (≠ Hermes egress) | ✅ CONFIRMED (r2-canary.yml name "R-4.1 Tier-1 42 canary", hermes lock trigger 0) |
| HERMES_REDACT_SECRETS opt-in | ✅ CONFIRMED (R-4 line 138, default false, v0.12.0 ON→OFF) |
| docker/r2-poc 골격 존재 | ✅ CONFIRMED (Dockerfile + compose + r2_poc.py) — 단 R-2 PoC (Hermes 아님) |
| Hermes URL 출처 | ⚠️ 불명 (day2-r1 §3.1 = grep ≠ URL, ADR-008 미확인) |
| day2-r1 위치 검증 정합 | ✅ (docstring + 25 import 비-DB, FAIL = G1a DB 맥락 — GP-2 위임 재해석 타당, codex/Agent 공통) |
| R-4 §5 Hermes ⊇ Tier-1 | ✅ (47 + 2 frozenset ⊇ Tier-1, 단 R-4.1/R-6 catalog 체계 결합) |

---

## §4 합의 결론

✅ **SC-2 R-1 위임 검증 APPROVE WITH CONDITIONS (4 source 전원)** — **brief v1.1 reframe 흡수 후 발효** (60 detection reframe 동형):

1. **방향 견고** (4 source): R-1 위임 검증 4축 종합 + day2-r1 FAIL 재해석 타당 + over-claim 1차 경계 (Hermes 안전성 선언/full GP-2 PASS 격상) 견고.
2. **BLOCKING 4 흡수 (framing reframe)**:
   - (B-1) 축 3 R-6 자동 회귀 → "ADR 의무 요구 / 현 R-6 Tier-1 catalog까지만 operative (Hermes lock trigger 미구현)"
   - (B-2) 축 1 → "활성화된 (HERMES_REDACT_SECRETS=true) Hermes redaction" + 활성화 전제 신설
   - (B-3) artifact 부재 완화 (docker/r2-poc 골격) + URL 출처 불명 정직
   - (B-4) 위치 evidence 시점성 (2026-05-05, 재확인 = C-3)
3. **"충족" → "조건부/문서 기반 충족"** (R-1 + codex): R-1 prong = Exit (a) Hermes-native sub-evidence 조건부 충족 (활성화 전제 + R-6 Tier-1 한정 + 위치 시점성 + URL 불명).
4. **full GP-2 PASS = R-1 (조건부) ∧ R-2 (SC-1 ✅) → SC-3** (실 격리 canary 강한 보강 = SC-3 또는 별도 trigger).
5. **process 가치 재입증**: 60 over-claim cascade 재발 (4 source가 R-6/activation framing over-claim 포착) — 본 세션 #3 첫 cascade.

→ **brief v1.1 1pass reframe 흡수 → commit + push**.

---

## §5 메타 편향 자기진단 (Reviewer)

| # | 위험 | 처리 |
|---|------|----|
| M-1 | Reviewer = brief 작성자 (Claude) cascade | cross-vendor codex + 3 Agent BLOCKING (R-6/activation framing 작성자 미포착 포착) |
| M-2 | R-6 over-claim = 사소 무시 risk | Reviewer 직접 verify (r2-canary name = Tier-1 canary) — 60 B-1 동형 재발 = 핵심 |
| M-3 | "충족" reframe = brief 가치 하락 우려 | reframe = 정직 scope (조건부/문서 기반), evidence 실증 유지 (60 detection reframe 동형 — 가치 보존) |
| M-4 | B-2 activation 전제 = 위임 검증 무효화? | 무효화 0 — 활성화 전제 *명시*로 정직성 강화 (HERMES_REDACT_SECRETS=true 전제 위임) |
| M-5 | 4 source 전원 APPROVE = rubber-stamp | BLOCKING 4 실질 흡수 (framing reframe + 사실 정정 2 + 시점성) |

---

**본 합의 보고서 끝.**

**다음 단계**: brief v1.1 reframe 흡수 (BLOCKING 4 + 권고 4) → commit + push → **R-1 위임 검증 조건부/문서 기반 충족 (활성화 전제 + R-6 Tier-1 한정)**. 후속: SC-3 (full GP-2 PASS 발효 합의) — R-1 (SC-2 조건부) ∧ R-2 (SC-1) + 실 격리 canary 보강 = 사용자 명시 별도 cycle.
