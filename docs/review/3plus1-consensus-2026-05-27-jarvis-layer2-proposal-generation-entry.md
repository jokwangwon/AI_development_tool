# 3+1 합의 보고서 — Jarvis 자가진화 Layer 2 (제안 생성) brief v1

> **본 합의는 추론적 검증(권고) 한정이며 — 본 합의의 어떤 §도 그 자체로 (i) Layer 2 코드/테스트 구현, (ii) Layer 0/1 발효 모듈 수정, (iii) 자비스 동작 변경 (prompt/policy/code 갱신 API 도입), (iv) threshold 값 *고정*, (v) 사람 승인 게이트 *구현/발효*, (vi) Layer 3 (자동 적용) 신설, (vii) MVP-1 진입 / GP-3·GP-5 의사결정, (viii) commit / push 강제 — 어떤 행위도 자동 발생시키지 않는다. 본 합의 = brief 설계 일관성 검증 한정. 발효 = MVP-1 이후 실 제안 trigger 가 1건 이상 발생한 시점 재진입 cycle.**

---

**작성일**: 2026-05-27
**합의 형태**: 풀 3+1 (Agent A 구현 · Agent B 안전 · Agent C 대안 + Reviewer)
**합의 입력**: `docs/phase0/jarvis-layer2-proposal-generation-brief.md` (v1)
**1차 권위 답습**: [[jarvis-layer1-pattern-mining-brief]] §1 안전 등급 / [[ADR-011-means-vs-ends-redaction]] §2.1 수단/목적 / [[mvp-staged-roadmap]] 발효 DEFER / [[proportionate-security-personal-tool]] 비례 / [[ceremony-inflation]] 1pass 흡수
**판정**: **APPROVE w/ COND** (13 보강 항목 본 brief 내 1pass 흡수 → v1.1, 별도 cycle 0)

---

## 0. 합의 대상

Layer 0 (관찰 누적, JSONL) + Layer 1 (패턴 마이닝, 보고만) 다음 단계 = Layer 2 = "제안 생성". `PatternReport` → actionable `Proposal` / `ProposalSet`. **본 cycle = 설계 일관성 검증 한정, 코드 0 / 테스트 0 / 발효 DEFER.**

Layer 1 brief §1 "보고 = 안전 행위 = 게이트 불요" 답습은 Layer 2 에 *확장 안 됨* — 제안 = 사람 의사결정 영향 = 큰 결정 = 풀 3+1 필수.

---

## 1. 교차 비교

### 1.1 일치 (Consensus — 3/3)

| # | 항목 |
|---|------|
| K1 | frozen + tuple 출력 + `source_report_signature` (Layer 1 §3 답습) |
| K2 | stdlib + Layer 1 의존만, 외부 호출 0 |
| K3 | threshold 인자 외부화 = ADR-011 §2.1 (a)~(d) 수단/목적 분리 |
| K4 | 자동 적용 0 / Layer 3 (영구 DEFER) / 발효 DEFER |
| K5 | `INPUT_DROUGHT` 거짓 안전감 차단 정합 |

### 1.2 부분 일치 (Partial — 2/3)

| # | 항목 | 동의 | 이견 |
|---|------|------|------|
| P1 | `FLAG_FREQUENCY_RISING` 위험 flag 식별자 부재 — `risk_flags: frozenset[str]` 인자 추가 | A§2-1 / B 암묵 | C 미언급 |
| P2 | severity 명세 — A: 5×3 매트릭스 표 / B: severity 임계도 threshold 인자 | A§2-5 / B§2-1 | C "유지 우월" (단순성 옹호, 명세 결함 미언급) |
| P3 | `source_report_signature` 알고리즘 = sha256 over canonical JSON (sort_keys=True) | A§2-4 / B§2-5 | C 미언급 |

→ P1/P2/P3 모두 brief 본문 결함, 채택. P2 는 A·B 해법 *통합* (매트릭스 + `severity_thresholds` 인자 둘 다).

### 1.3 불일치 (Divergence — 평가 강도)

| Agent | 판정 | 근거 |
|-------|------|------|
| A | REVISE | 시그니처 ↔ trigger 표 *내부 일관성* 결함 (risk_flags 누락, FLAG_FREQUENCY threshold 시그니처 누락 등) |
| B | APPROVE w/ COND | 본문 흡수 가능 |
| C | APPROVE w/ COND | 본 brief 내 ~5 line = 추가 cycle 불요 |

**Reviewer 판단**: A 의 지적 정확. 단 보강 분량 = **본 brief 내 1pass 흡수 가능** (~25 line). 별도 cycle 권고 = ceremony-inflation 위반. → **APPROVE w/ COND** 채택.

### 1.4 누락 (Gap — 단독 언급)

| # | 항목 | 출처 | 처리 |
|---|------|------|------|
| G1 | `staleness_seconds` ↔ `last_ts` ISO 8601 UTC 가정 | A§2-2 | 채택 (§3 staleness_seconds 주석) |
| G2 | `total >= min_sample` **및** `total > 0` 동시 충족 (zero-state) | A§2-3 | 채택 (§4 fail-soft) |
| G3 | `generated_ts` = 호출자 주입 (테스트 결정성) | A§3-1 | 채택 (§3 주석) |
| G4 | `evidence` 포맷 = "key=value" | A§3-2 | 채택 (§3 주석) |
| G5 | `proposals` 정렬 결정성 = severity desc → kind asc → subject asc | A§3-4 / B§3-3 / C§3-1 (사실상 2/3+) | 채택 (§3 주석) |
| G6 | 중복 제안 dedup | A§3-3 / C§3-2 | 비-scope 명시 |
| G7 | threshold 후보값 = 잠정, MVP-1 evidence 후 재조정 | B§2-4 | 채택 (§2) |
| G8 | 적용 책임 = 호출자(사용자) | B§3-2 | 채택 (§1 표 행) |
| G9 | 제안 audit log / severity 인플레이션 unit test | B§3-1·3-4 | **후속 cycle carry-over** (§7) |
| G10 | `ADVICE_AXIS_DEGRADED` 추가 (Layer 1 `advice_axis_stats` 4축 미활용) | C§2-1 | 채택 (§2 표 + ProposalKind) |
| G11 | N 후보에 {5} 추가 (v0.0 144 entry 기준) | C§2-3 | 채택 (§2) |
| G12 | 제안 만료/expire | C§3-3 | 비-scope 명시 |
| G13 | `format_proposals` 출력에 사용 threshold 동봉 (거짓 안전감 추가 차단) | B§2-3 | 채택 (§4) |

---

## 2. 1pass 보강 (brief v1 → v1.1, 본 cycle 내 흡수)

| # | 위치 | 내용 |
|---|------|------|
| 1 | §1 표 | "적용 책임 = 호출자(사용자)" 행 추가 (G8) |
| 2 | §2 표 | `ADVICE_AXIS_DEGRADED` 1행 추가 (G10) |
| 3 | §2 수단 후보 | N = {5, 10, 20, 50}, α 추가 (G11, G10) |
| 4 | §2 | "threshold 후보값 = 잠정, MVP-1 evidence 후 재조정" 1줄 (G7) |
| 5 | §2 비-scope | dedup, expire 2개 추가 (G6, G12) |
| 6 | §3 `ProposalKind` | `ADVICE_AXIS_DEGRADED` enum 1행 (G10) |
| 7 | §3 `evidence` 주석 | "key=value 포맷, 공백 0" (G4) |
| 8 | §3 `generated_ts` 주석 | "ISO 8601 UTC, 호출자 주입" (G3) |
| 9 | §3 `source_report_signature` | "sha256 over canonical JSON, sort_keys=True, ensure_ascii=False" (P3) |
| 10 | §3 `propose()` 시그니처 | `risk_flags`, `advice_axis_threshold`, `severity_thresholds` 3 인자 + `staleness_seconds` 주석 "ISO 8601 UTC 가정" (P1, P2, G1) |
| 11 | §3 신규 §3.1 | severity 결정 매트릭스 5종 × 3단 표 (P2) + 정렬 결정성 (G5) |
| 12 | §4 fail-soft | `total >= min_sample` 및 `total > 0` 동시 충족, severity_thresholds 미지정 ValueError, 출력 헤더 threshold 동봉 (G2, G13) |
| 13 | §7 carry-over | 제안 audit log / severity 인플레이션 unit test (G9) |

**보강 후 brief v1.1 = 본 합의 보고서의 직접 산출물**. 별도 v2 cycle 0.

---

## 3. 원칙 준수 확인

| 원칙 | 보강 후 상태 |
|------|-------------|
| 코드 0 | ✅ (설계만) |
| 테스트 0 | ✅ (설계만) |
| 발효 DEFER | ✅ (§5 명시, MVP-1 이후 재진입) |
| threshold 고정 0 | ✅ (수단 후보만 나열, severity 임계도 호출자 결정) |
| 자동 적용 0 | ✅ (Layer 3 영구 DEFER 답습) |
| Layer 0/1 수정 0 | ✅ (PatternReport frozen 입력) |
| 외부 호출 0 | ✅ (stdlib 만) |
| ceremony-inflation 회피 | ✅ (1pass 흡수, 별도 cycle 0) |

---

## 4. carry-over (발효 단계 진입 시 후속 cycle)

1. 제안 audit log 경로 설계 (수용/기각 이력 append-only JSONL, 편향 회고 가능성, B§3-1).
2. severity 인플레이션 unit test (모든 출력이 `high` 가 되는 임계 시나리오 검출, B§3-4).
3. threshold 후보값 evidence-driven 재조정 (Layer 0/1 누적 데이터 분석, B§2-4).

---

## 5. 결론

**판정: APPROVE w/ COND** — brief v1 → v1.1 보강 후 발효. 발효 자체는 별도 cycle. 본 cycle 산출물 = brief v1.1 + 본 합의 보고서.
