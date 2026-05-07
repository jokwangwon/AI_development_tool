# Hermes Agent 도입 설계 v3 (Hermes Adoption Design v3) — DRAFT

> **상태: DRAFT (초안)**. P2 v2 §2.1.3 가정 붕괴 사실 + R-2 ~ R-7 evidence + R-6 GitHub Actions actual run PASS + G1b PASS 승격(2026-05-07) 권위를 흡수하고, Hermes PMO 구조와 G2/G3/G4 잔여 게이트의 entry/exit 기준을 명세하는 초안. **Hermes PMO 격상 선언은 본 초안 범위 외** — 4 게이트 모두 통과 + 사용자 명시 결정 후 별도 발행.

**상태**: DRAFT (초안, 2026-05-07 작성). 단축 합의 통과 후 v2 대체.
**작성일**: 2026-05-07
**상위 결정**: ADR-008 (Option B), ADR-011 (수단/목적 분리 — R-3 모법)
**상위 권위**: 헌법 제5조 (Provider Liquidity), 헌법 제8조 (보안), `docs/architecture/system-identity-prequel.md` (R-7 후 본 v3로 흡수, archived 예정)
**관련 ADR**: ADR-009 (자체 Adapter v2.0 진입조건), ADR-010 (SQLCipher Vault HSM 키 관리), ADR-011 (수단/목적 분리)
**대체 대상**: `docs/architecture/hermes-adoption-design.md` (P2 v2, 본 v3 정식화 시 archived)
**관련 설계**: `llm-providers-design.md` (P1 v2), `multi-agent-system-design.md`, `harness-engineering-design.md`, `redaction-pattern-equivalence.md` (R-4), `canary-recheck-design.md` (R-5)
**근거 합의**: `docs/review/3plus1-consensus-2026-05-05-system-identity-redefinition.md` (풀 합의 — 정체성/권위 위계), `docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md` (R-3), `docs/review/3plus1-consensus-2026-05-07-g1b-phase1-acceptance.md` (G1b PASS 단축 합의)
**관련 evidence**: R-1 (`docs/phase0/day2-r1-redaction-location-verification.md`), R-2 (`docs/phase0/day3-r2-sqlite-trigger-poc.md`), R-4 (`docs/architecture/redaction-pattern-equivalence.md`), R-4.1 (`docs/phase0/r4-1-trigger-extension-evidence.md`), R-7 (`docs/phase0/redaction-verification-sop.md`), R-6 actual run (`25482284523`)

---

## 0. 본 초안의 운명과 범위

### 0.1 본 초안이 *하는* 것

1. P2 v2 §2.1.3 (`add_pre_record_hook`) 가정 코드 미존재 사실 명시 흡수 (Day 1 evidence)
2. R-2 ~ R-7 6단계 + R-6 actual run PASS evidence 흡수
3. G1b PASS (2026-05-07) 권위를 P2 본문 권위로 반영
4. Hermes PMO 구조 명세 (현 시점에서는 **활성화 후보 대상의 사전 정의**, 활성화 조건은 별도)
5. G2 / G3 / G4 잔여 게이트 정의 + entry/exit 기준 + 산출 후보 명세
6. 동시 갱신 ADR 매트릭스 (ADR-008 본문 / ADR-009 / ADR-010 / ADR-011 cross-reference 후보)
7. `system-identity-prequel.md` 흡수 후 archived 처리 경로 명시

### 0.2 본 초안이 *하지 않는* 것 (사용자 명시 답습)

1. ❌ **Hermes PMO 격상 선언** — 4 게이트(G1b ✅ + G2 ⏳ + G3 🟡 + G4 ⏳) 모두 통과 + 사용자 명시 결정 후 별도 발행
2. ❌ G2 / G3 / G4 PASS 선언 (본 초안은 *정의*까지만)
3. ❌ ADR-008 본문 / ADR-009 / ADR-010 / ADR-011 본문 자동 갱신 (별도 PR 묶음으로 처리)
4. ❌ `system-identity-prequel.md` 자동 폐기 (본 v3 정식 채택 시점에 archived)
5. ❌ P2 v2 자동 폐기 (본 v3 정식 채택 시점에 archived)
6. ❌ 자동 정책 변경 (ADR-011 §2.4 T3 — 절대 금지)
7. ❌ Tier-2 / Tier-3 catalog 확장 (별도 합의)
8. ❌ Phase 진입 결정 (본 초안은 설계 문서이며, Phase 진입은 별도 합의)

### 0.3 본 초안의 정식화 절차 (예정)

| # | 단계 | 산출 | 시점 |
|---|------|------|------|
| 1 | 본 초안 작성 (현 단계) | 본 문서 (DRAFT) | 2026-05-07 |
| 2 | 사용자 검토 + 수정 | 본 문서 갱신 | 사용자 명시 결정 후 |
| 3 | 합의 가동 (단축 또는 풀) | `docs/review/3plus1-consensus-YYYY-MM-DD-p2-v3.md` | 사용자 명시 결정 후 |
| 4 | v3 정식 채택 + v2 archived + prequel archived | 본 헤더 "DRAFT" 제거 + v2 헤더 갱신 + prequel 헤더 갱신 | 합의 APPROVE 후 |
| 5 | ADR 동시 갱신 PR 묶음 | ADR-008/009/010/011 갱신 (cross-reference 추가) | 단계 4와 동일 PR 또는 후속 PR |
| 6 | INDEX / CONTEXT 갱신 | `docs/INDEX.md`, `docs/CONTEXT.md` | 단계 4와 동일 |

본 초안 자체는 단계 1까지만 처리. 단계 2~6은 본 초안 범위 외.

---

## 1. v2 → v3 차이 (Delta)

### 1.1 §2.1.3 가정 갱신 (P2-N1 결과 반영)

| 항목 | P2 v2 §2.1.3 가정 | Phase 0 Day 1 사실 (2026-05-05) | v3 처리 |
|------|------------------|------------------------------|---------|
| Hermes API | `add_pre_record_hook(pre_record_hook)` 공식 지원 가정 | grep 0건 — `pre_record` / `add_pre_record_hook` / `before_record` 없음. 15종 `VALID_HOOKS` 중 DB 기록 직전 가로채기 hook 0개 | **가정 폐기**. 본 v3 §3.2 (G1a FAIL) + §3.3 (G1b PASS by R-2 trigger) 로 대체 |
| 가정 출처 | ADR-008 부록 A R1 텍스트 + P2 v2 본문 | — | ADR-008 부록 B Amendment (2026-05-06)로 갱신됨. 본 v3는 Amendment 결과 반영 |
| 위험 등급 | R1 = CRITICAL → 비협상 차단조건 #1 | R-1 FAIL 확정 → R-2 PASS by SQLCipher trigger | **G1a 폐기 + G1b 채택**. 차단조건 #1 충족 *수단*은 §1.3 갱신 |

### 1.2 G1 단일 게이트 → G1a / G1b 분리 (ADR-011 §2.2 인용)

```
[v2]
G1: Phase 0 R-1 (canary 검증) — Hermes 자체 redaction이 DB INSERT 경로에 적용되는지 격리 환경 검증

[v3 — ADR-011 §2.2 권위]
G1a: Hermes native redaction applies before DB INSERT
   Result: FAIL (R-1 확정, 2026-05-05)
   Status: 폐기 (이 경로로 헌법 8조 충족 시도 금지)

G1b: DB-level fallback prevents plaintext secret persistence
   Result: PASS (2026-05-07 단축 합의 승격)
   Evidence: R-2 PoC + R-4 pattern equivalence + R-4.1 Tier-1 42 trigger UDF + R-5 canary recheck design
             + R-6 CI workflow + R-6 actual run 25482284523 (PASS, 24초, verdict PASS, 42/42 BLOCK, leak 0)
             + R-7 Phase 1 acceptance SOP + 단축 합의 APPROVE
```

### 1.3 차단조건 #1 충족 메커니즘 갱신 (ADR-008 부록 B.5 반영)

| 메커니즘 | 위치 | 신뢰도 (v2) | 신뢰도 (v3) |
|---------|------|------------|------------|
| SQLCipher 암호화 (디스크) | DB 파일 | Primary | 기존대로 유지 |
| Hermes native redaction | 로그 / LLM 송신 / 도구 출력 | Primary (DB INSERT 경로 가정) | **보조** (DB 차단 책임 없음, ADR-011 §2.3 운영 함의 #2) |
| **SQLCipher BEFORE INSERT trigger + REGEXP UDF (Tier-1 42 catalog)** | **DB INSERT 경로** | (가정 외) | **Primary (G1b)** |
| canary 재검증 트리거 (R-5 설계, T13 강화) | CI / nightly / Hermes 업그레이드 / catalog 갱신 / dev local | (가정 외) | **운영 메커니즘** (ADR-011 §2.4 T1 자동) |
| CI/nightly 자동 회귀 (R-6 workflow) | GitHub Actions | (가정 외) | **자동 회귀 검증 경로** (ADR-011 §2.1 (d) 충족) |

차단조건 #2 ~ #6은 본 v3에서 **변경 없음** — §8 (carry-over) 참조.

### 1.4 R-2 ~ R-7 6단계 evidence 흡수표

| # | 산출 | 본 v3 인용 위치 | ADR-011 충족 |
|---|------|---------------|-------------|
| R-2 | `docs/phase0/day3-r2-sqlite-trigger-poc.md` + `docker/r2-poc/` | §3.3 G1b — baseline 5 patterns PoC | §2.2 G1b PASS by R-2 |
| R-3 | `docs/decisions/ADR-011-means-vs-ends-redaction.md` + ADR-008 부록 B Amendment | §2 (Hermes PMO 구조 권위) + §3 (게이트 정의 권위) | (R-3 = ADR-011 자체) |
| R-4 | `docs/architecture/redaction-pattern-equivalence.md` | §3.3 G1b — pattern equivalence | §2.1 (a) 동등 이상 보안 결과 |
| R-4.1 | `docs/phase0/r4-1-trigger-extension-evidence.md` + `docker/r4-1-poc/` | §3.3 G1b — Tier-1 42 trigger UDF 격리 PoC | §2.1 (b) 격리 환경 PoC 실증 |
| R-5 | `docs/architecture/canary-recheck-design.md` | §3.3 G1b — 운영 메커니즘 + ADR-011 §2.4 T1/T2/T3 정책 매트릭스 | §2.4 자동 학습 vs 정책 변경 분리 |
| R-6 | `.github/workflows/r2-canary.yml` + actual run `25482284523` | §3.3 G1b — 자동 회귀 검증 경로 | §2.1 (d) 자동 회귀 검증 경로 |
| R-7 | `docs/phase0/redaction-verification-sop.md` (G1b PASS 갱신) | §3.3 G1b — 정식 충족 SOP | §2.2 G1b 정식 충족 절차 |

### 1.5 carry-over (v2 본문 변경 없음)

다음 v2 섹션은 본 v3에서 **본문 변경 없이 유지**한다 (§8 carry-over 매핑 참조):

- §1.4 전제 조건
- §1.5 ADR-008과의 관계
- §1.6 P1과의 관계
- §1.7 하네스 위치
- §2.0 차단조건 분류 (R3-1)
- §2.2 차단조건 #2 (JSONL Export + 마이그레이션)
- §2.3 차단조건 #3 (버전 핀 + 회귀 + 카나리)
- §2.4 차단조건 #4 (P1 Facade 위임)
- §2.5 차단조건 #5 (Min 2 Active)
- §2.6 차단조건 #6 (Docker 격리 강화)
- §3 Phase 0 ~ §6 Phase 3 단계 정의 (단, §3 Phase 0의 **R-1 결과**는 본 v3 §3.2 G1a FAIL로 갱신)
- §7 롤백 (단, R-7 SOP §5 9 ROLLBACK trigger와 cross-reference 추가)
- §8 검증 메트릭
- §9 헌법 정합성

---

## 2. Hermes PMO 구조 (활성화 후보 대상의 사전 정의)

> **본 §2는 Hermes PMO *격상 선언이 아니다*.** 본 §2는 4 게이트(G1b/G2/G3/G4) 모두 통과 후 사용자 명시 결정으로 활성화될 수 있는 PMO의 *구조 사전 정의*이다. 현 시점 상태는 §3.6 (현 활성화 상태)을 따른다.

### 2.1 Hermes 역할 정의 (system-identity-prequel §4 흡수)

```
Hermes = AI 조직의 운영 본부 + 기억 관리자 + Skill 관리자 + 합의 프로토콜 실행기
```

#### 2.1.1 격상 후 담당 후보 (10항목)

| # | 책임 | 권위 |
|---|------|-----|
| 1 | 사용자 아이디어를 작업 가능한 단위로 구조화 | T2 (사용자 승인 결과 실행) |
| 2 | Phase 0 질문지 또는 브리프 생성 | T1 자동 |
| 3 | 작업 위험도 분류 | T1 자동 (T3 후보 식별 시 즉시 사용자에게 escalation) |
| 4 | 필요한 ADR/SDD 문서 판단 (제안만, 작성 권한 없음) | T1 자동 (제안), T2 (작성은 사용자 승인 후) |
| 5 | 3+1 멀티 에이전트 합의 프로토콜 실행 (orchestrate) | T1 자동 |
| 6 | Worker Agent (Claude Code, GPT 등) 호출 및 조율 | T1 자동 |
| 7 | 반복되는 작업을 Skill 후보로 추출 | T1 자동 (등록은 사용자 승인) |
| 8 | 프로젝트별 Memory 관리 (read/append) | T1 자동 |
| 9 | 작업 결과를 Evidence Report로 남김 | T1 자동 |
| 10 | 성공/실패 패턴을 다음 프로젝트에 재사용 | T1 자동 (Global 승격은 manual only) |

본 10항목은 **활성화 후 책임 후보**이며, 본 v3는 *책임의 권위 등급(T1/T2/T3)* 만 명시한다. 구체 구현은 G2 (6 거버넌스 사전조건) / G3 (Hermes ≠ root of trust 운영 구현) 통과 후 별도 SDD에서 정의.

#### 2.1.2 Hermes가 *하지 않는* 것 (영구)

| # | 금지 행위 | 권위 근거 |
|---|----------|---------|
| 1 | Constitution / ADR / SDD 본문 자동 작성 또는 수정 | ADR-011 §2.4 T3 + system-identity-prequel §3.3 #1 |
| 2 | Harness Gate 정의 자체의 변경 | ADR-011 §2.4 T3 |
| 3 | Tools 검증 결과를 우회하여 PASS 처리 | ADR-011 §2.3 권위 위계 (Tools > Hermes 출력) |
| 4 | DB INSERT 경로 차단의 *유일한* 메커니즘으로 작동 | ADR-011 §2.3 운영 함의 #2 (Hermes native redaction은 보조) |
| 5 | 합의 결과(Reviewer 출력) 수정 | system-identity-prequel §3.3 #2 |
| 6 | 자체 권위 상승을 트리거하는 결정 | ADR-011 §2.4 T3 + system-identity-prequel §3 권위 위계 |

### 2.2 권위 위계 (ADR-011 §2.3 영구 권위 인용)

```
Constitution
  > ADR
  > SDD
  > Harness Gates (Layer 0~6)
  > Hermes
  > Worker Agents
```

본 위계는 **ADR-011 §2.3** 영구 권위로 승격되어 있으며, system-identity-prequel.md archived 후에도 보존된다. 본 v3는 위 위계를 *전제*로 한다.

### 2.3 운영 함의 (ADR-011 §2.3 5항목 인용)

본 v3는 ADR-011 §2.3 5항목을 P2 본문 운영 권위로 흡수한다:

1. **Hermes 출력은 Tools로 검증된다**: 린터/타입체커/테스트/trigger/canary가 Hermes 출력 위에 위치 → §3.4 G3 운영 메커니즘 5항목 #1
2. **Hermes 자체 redaction은 로그/LLM 송신 방어로만 신뢰**: 저장 경로(DB/파일) 차단 책임 없음 → §1.3 차단조건 #1 갱신
3. **DB INSERT 경로는 Hermes 외부에서 별도 보호**: SQLCipher trigger 기반 fallback (G1b) → §1.3 + §3.3
4. **Hermes 의존성 업그레이드는 자동 R-2 재실행으로 회귀 검증**: 신뢰 경계 외부 변경의 자동 검출 → §3.3 G1b 운영 메커니즘 + R-6 workflow
5. **Hermes 학습 결과의 자동 정책 반영 금지**: §2.1.2 #1~#6 + ADR-011 §2.4 결합 → §3.4 G3

### 2.4 Hermes 비활성 상태에서의 책임 (현 시점)

현 시점(2026-05-07, G1b PASS 직후) Hermes 책임은 다음으로 한정한다:

- ✅ ADR-008 합의 자동화 책임 (Option B 6 차단조건 검증 자동화)
- ✅ R-6 CI workflow 자동 회귀 검증 (`r2-canary.yml` push/PR/nightly trigger)
- ❌ §2.1.1 10항목 책임 모두 **미활성**
- ❌ Memory 격상 권한 없음 (Project → Global manual only)
- ❌ Skill 등록 권한 없음 (사용자 승인 강제)
- ❌ 합의 결과 수정 권한 없음

### 2.5 활성화 후 책임 (4 게이트 통과 시)

§2.1.1 10항목 + §2.3 5 운영 함의 + §3.4 G3 5 운영 메커니즘 모두 활성. **단, 활성화는 본 v3 범위 외이며, 4 게이트 통과 후 별도 합의로 결정**.

### 2.6 격상 절차 (별도 합의)

| 단계 | 조건 | 산출 |
|------|------|------|
| 1 | G1b PASS | ✅ 2026-05-07 (R-7 SOP §7.3 단축 합의) |
| 2 | G2 PASS | ⏳ §4 entry/exit 기준 충족 후 |
| 3 | G3 PASS | ⏳ §5 entry/exit 기준 충족 후 |
| 4 | G4 PASS | ⏳ §6 entry/exit 기준 충족 후 |
| 5 | 4 게이트 통합 검증 합의 (풀 3+1) | 별도 합의 보고서 |
| 6 | 사용자 명시 격상 결정 | 명시 명령 |
| 7 | 격상 활성화 commit + ADR-008 본문 추가 갱신 | 별도 PR |

본 v3는 **단계 1~4의 정의까지만 다룬다**. 단계 5~7은 본 v3 범위 외.

---

## 3. 4 게이트 정의 + 진행 상태

### 3.1 4 게이트 개요

| 게이트 | 정의 | 현 상태 (2026-05-07) | 본 v3 상세 |
|-------|------|--------------------|----------|
| **G1a** | Hermes native redaction → DB | ❌ **FAIL 확정 (폐기)** | §3.2 |
| **G1b** | DB-level fallback (SQLCipher trigger) | ✅ **PASS** (2026-05-07 승격) | §3.3 |
| **G2** | 6 거버넌스 사전조건 | ⏳ **미작성** | §4 |
| **G3** | "Hermes ≠ root of trust" 운영 구현 | 🟡 **ADR-011 §2.3 권위 확정 / 운영 구현 미작성** | §5 |
| **G4** | Provider-agnostic Memory/Skill 형식 | ⏳ **미작성** | §6 |

### 3.2 G1a (폐기)

**정의**: Hermes native redaction이 DB INSERT 경로에 적용되는지 격리 환경 검증.

**결과**: FAIL (R-1 확정, 2026-05-05).

**evidence**: `docs/phase0/day2-r1-redaction-location-verification.md`
- `agent/redact.py:1-8` docstring "Regex-based secret redaction for logs and tool output"
- redact 모듈 import 25개 모두 비-DB 경로
- `hermes_state.py` (SessionDB) redact import 0건

**상태**: ADR-011 §2.2 권위로 **영구 폐기**. 이 경로로 헌법 8조 충족 시도 금지.

### 3.3 G1b (PASS, 2026-05-07)

**정의**: DB-level fallback (SQLCipher BEFORE INSERT trigger + REGEXP UDF)이 plaintext secret persistence를 차단.

**결과**: PASS (2026-05-07 R-7 SOP §7.3 단축 합의 APPROVE — Reviewer-only).

**evidence chain (R-2 ~ R-7 + actual run)**:

| # | 산출 | 결과 |
|---|------|------|
| R-2 | `docker/r2-poc/` + `docs/phase0/day3-r2-sqlite-trigger-poc.md` | baseline 5 patterns C1~C6 PASS |
| R-3 | `ADR-011` + ADR-008 부록 B Amendment | 권위 확정 (수단/목적 분리) |
| R-4 | `docs/architecture/redaction-pattern-equivalence.md` | pattern equivalence + gap 식별 + 보충 권고 (ADR-011 §2.1 (a) 충족) |
| R-4.1 | `docker/r4-1-poc/` + `docs/phase0/r4-1-trigger-extension-evidence.md` | Tier-1 42 trigger UDF 격리 PoC PASS (ADR-011 §2.1 (b) 충족) |
| R-5 | `docs/architecture/canary-recheck-design.md` | T13 강화 + 6 trigger 시점 + 4 verdict + 4 안전장치 + Markdown+JSONL evidence + T1/T2/T3 정책 매트릭스 |
| R-6 | `.github/workflows/r2-canary.yml` + actual run `25482284523` | 24초 PASS, verdict=PASS, 42/42 BLOCK, leak 0, ROLLBACK 미발화 (ADR-011 §2.1 (d) 충족) |
| R-7 | `docs/phase0/redaction-verification-sop.md` | 13 checklist + 4 verdict + 9 ROLLBACK + 7 Evidence + push 전/후 작업 분리 + §7.3 단축 합의 절차 |

**Phase 1 acceptance**: PASS 선언 (PARTIAL → PASS, 2026-05-07).

**상태 영구화**: 본 v3가 정식 채택될 때, G1b PASS는 본 v3 §3.3 본문 권위로 영구 등재된다.

### 3.4 G2 / G3 / G4 잔여 게이트 — §4 / §5 / §6 상세

§4 (G2 — 6 거버넌스 사전조건), §5 (G3 — Hermes ≠ root of trust 운영 구현), §6 (G4 — Provider-agnostic Memory/Skill 형식) 참조.

### 3.5 4 게이트 합산 진행 상태 (2026-05-07 시점)

```
G1a = FAIL (폐기)                  ✅ 영구 결정
G1b = PASS                         ✅ 2026-05-07 승격
G2  = 미작성                       ⏳ §4
G3  = ADR 권위 확정 / 운영 구현 미작성  🟡 §5
G4  = 미작성                       ⏳ §6
───────────────────────────────────
4 게이트 PASS 합산 = 1/4
Hermes PMO 격상 선언 = 미선언 (본 v3 범위 외)
```

### 3.6 현 활성화 상태 (Hermes 책임 한정)

§2.4 참조. 현 시점 Hermes는 **ADR-008 합의 자동화 책임 + R-6 CI 자동 회귀 검증**만 활성. PMO/Memory/Skill 격상 책임 모두 비활성.

---

## 4. G2 — 6 거버넌스 사전조건

### 4.1 정의

**G2**: 헌법 제8조(보안) / 제5조(Provider Liquidity) 위반 경로 P1~P8 각각에 대한 강제 메커니즘이 매핑되어, 위반 발생 시 자동 차단되는 상태.

**근거**: system-identity-prequel §4.2 G2 + GPT 외부 검토 결과(2026-05-05 풀 합의).

### 4.2 6 사전조건 식별 후보

> **본 §4.2는 G2 *작성 트리거 후 정식 매핑* 대상이다.** 본 초안에서는 식별 후보까지만 나열하며, 정식 매핑은 별도 산출 `docs/architecture/governance-preconditions.md`로 처리.

| # | 사전조건 후보 | 위반 시 위험 | 강제 메커니즘 후보 | 근거 |
|---|------------|-----------|----------------|------|
| 1 | DB 평문 secret 저장 차단 | 헌법 8조 위반 | SQLCipher trigger (G1b) | ADR-011 §2.1 |
| 2 | 단일 Provider 의존 차단 | 헌법 5조 위반 | P1 facade min 2 active 검증 (P1 §X) | ADR-008 차단조건 #5 |
| 3 | Constitution / ADR / SDD 본문 자동 변경 차단 | T3 위반 | filesystem read-only + audit log + Hermes write 차단 | ADR-011 §2.4 + system-identity-prequel §3.3 |
| 4 | OAuth 직결 사용 차단 (Phase 1) | A-meta 위험 (구독 강제 해지) | API 키 경로 강제 + entrypoint stat + inotify 감시 | ADR-008 차단조건 #4 + R1-2 |
| 5 | Hermes 자체 SDK 직접 import 차단 | Provider lock-in | depcruise 룰 정적 차단 | ADR-008 차단조건 #4 + P1 v2 |
| 6 | 자동 정책 변경 차단 (T3) | T3 위반 | Layer 1~2 hook (설정 파일 변경 감지) + CI/nightly 강제 | ADR-011 §2.4 + R-6 |

**주의**: 위 6항목은 *후보*이며, G2 정식 작성 시 다음을 포함해 재평가한다:
- 헌법 제5조 / 제8조 외 다른 조항(예: 자기개선 한계, 환경 관리)의 위반 경로
- P1~P8 분류는 system-identity-prequel §4.2 G2의 P1~P8 명시 후 정식 매핑

### 4.3 Entry / Exit 기준 (제안)

#### 4.3.1 Entry (G2 작업 시작 조건)

- ✅ G1b PASS (2026-05-07, 충족됨)
- ⏳ 사용자 명시 G2 작업 시작 결정

#### 4.3.2 Exit (G2 PASS 조건)

| # | 조건 | 검증 방식 |
|---|------|---------|
| (a) | 6 사전조건 정식 매핑 작성 완료 | `docs/architecture/governance-preconditions.md` |
| (b) | 각 사전조건의 강제 메커니즘이 *계산적*으로 검증 가능 | 자동 테스트 또는 hook |
| (c) | 위반 시 자동 차단 1회 이상 시연 | 격리 환경 PoC |
| (d) | 자동 회귀 검증 경로 확보 | CI/nightly workflow 추가 |
| (e) | 단축 합의 또는 풀 3+1 합의 APPROVE | `docs/review/3plus1-consensus-YYYY-MM-DD-g2.md` |

(a)~(d)는 ADR-011 §2.1 (a)~(d) 4조건 패턴을 G2에 적용한 것. (e)는 G1b 승격 절차 답습.

### 4.4 산출 후보

- `docs/architecture/governance-preconditions.md` (정식 매핑)
- 각 사전조건별 hook / depcruise 룰 / CI step 추가
- G2 격리 PoC (Docker 환경, R-2 패턴 답습)
- 합의 보고서

### 4.5 의존 ADR / 갱신 후보

- ADR-008 본문: 6 차단조건 → 6 거버넌스 사전조건 cross-reference 추가 (격상 후)
- ADR-011: §2 본문은 변경 없음, §8 후속 작업에 G2 산출 등록
- 신규 ADR 후보: ADR-012 (거버넌스 사전조건 매트릭스) — Phase 1 종료 후 검토

---

## 5. G3 — "Hermes ≠ Root of Trust" 운영 구현

### 5.1 정의

**G3**: ADR-011 §2.3 권위 위계 + 5 운영 함의가 *운영 가능한 메커니즘*으로 구현된 상태. ADR 권위는 이미 확정(2026-05-06), 운영 구현은 미작성.

**근거**: ADR-011 §2.3 (영구 권위) + system-identity-prequel §3.3 (4 강제 메커니즘 후보).

### 5.2 5 운영 함의 → 5 운영 메커니즘 후보

| # | ADR-011 §2.3 운영 함의 | 운영 메커니즘 후보 | 검증 방식 |
|---|----------------------|----------------|---------|
| 1 | Hermes 출력은 Tools로 검증된다 | 린터/타입체커/테스트/trigger/canary 출력이 Hermes 출력보다 *상위* 권위 — Hermes 출력 우회 시 자동 차단 | Layer 1~2 hook + CI step |
| 2 | Hermes 자체 redaction은 로그/LLM 송신 방어로만 신뢰 | DB INSERT 경로에서 Hermes redaction 의존 0건 검증 | R-6 workflow + grep 자동 검증 |
| 3 | DB INSERT 경로는 Hermes 외부에서 별도 보호 | SQLCipher trigger (G1b PASS) + Tier-1 42 catalog | R-6 actual run 회귀 |
| 4 | Hermes 의존성 업그레이드는 자동 R-2 재실행 | `hermes-version.yaml` 변경 → R-2 / R-4.1 PoC 자동 재실행 | R-6 workflow trigger 확장 |
| 5 | Hermes 학습 결과의 자동 정책 반영 금지 | T3 변경 감지 hook + audit log + 자동 reject | Layer 1~2 hook + filesystem read-only |

### 5.3 system-identity-prequel §3.3 4 강제 메커니즘 흡수

| # | prequel §3.3 메커니즘 | 본 v3 §5 매핑 | 운영 메커니즘 후보 |
|---|--------------------|------------|---------------|
| 1 | 파일시스템 read-only on Constitution/ADR/SDD | §5.2 #5 | filesystem ACL + Hermes container read-only mount |
| 2 | 합의 결과는 Hermes 우회 (git commit 직접 보존 + UI 직접 전달) | §5.2 #1 + 신규 #6 | git pre-commit hook + UI router separation |
| 3 | 모든 Hermes-originated 변경은 audit log | §5.2 #5 | structured audit log (JSONL append-only, hash chain) |
| 4 | 권위 등급 위반 시 자동 reject | §5.2 #5 | Layer 1~2 hook + CI step |

§5.2의 5 메커니즘 + 본 §5.3의 4 메커니즘은 G3 작성 시 통합 매트릭스로 정리. 본 초안은 *후보 식별*까지만.

### 5.4 Entry / Exit 기준 (제안)

#### 5.4.1 Entry

- ✅ ADR-011 §2.3 권위 확정 (2026-05-06, 충족됨)
- ✅ G1b PASS (2026-05-07, 충족됨)
- ⏳ 사용자 명시 G3 작업 시작 결정

#### 5.4.2 Exit

| # | 조건 | 검증 방식 |
|---|------|---------|
| (a) | 5 운영 메커니즘 + 4 강제 메커니즘 통합 매트릭스 완성 | `docs/architecture/hermes-not-root-of-trust-runtime.md` (가칭) |
| (b) | 각 메커니즘의 격리 환경 시연 | Docker isolation + 자동 검증 항목 |
| (c) | T3 위반 자동 reject 1회 이상 시연 | hook 격리 PoC |
| (d) | 합의 인프라 순환 권위 해결 (prequel §4.2 G3 명시) | 합의 보고서 |
| (e) | 단축 합의 또는 풀 3+1 합의 APPROVE | `docs/review/3plus1-consensus-YYYY-MM-DD-g3.md` |

### 5.5 합의 인프라 순환 권위 문제 (특기)

**문제**: 합의 자체가 Hermes 위에서 실행될 경우, "합의 결과로 Hermes 권위 변경"의 자기참조 위험.

**해결 방향 후보** (G3 작성 시 정식화):
- 합의 실행 인프라(3+1 multi-agent)는 Hermes와 *별도 프로세스* 또는 *별도 호스트*에서 실행
- Reviewer 출력은 git commit 으로 Hermes 우회 보존 (system-identity-prequel §3.3 #2)
- 격상/강등 결정은 사용자 명시 commit 만 권위 인정 (Hermes-originated commit 자동 거부)

본 §5.5는 G3 정식 작성 시 결정. 본 초안은 *문제 명시*까지만.

### 5.6 산출 후보

- `docs/architecture/hermes-not-root-of-trust-runtime.md` (가칭, 통합 매트릭스)
- 5 운영 메커니즘 각각의 hook / CI step / audit log schema
- 격리 환경 PoC (G2와 통합 가능)
- 합의 보고서

### 5.7 의존 ADR / 갱신 후보

- ADR-011: §2.3 본문 변경 없음, §8.5 후속 작업에 G3 산출 등록
- ADR-008: 본문 부록 추가 (G3 운영 구현 cross-reference) — 격상 후
- 신규 ADR 후보: ADR-013 (Hermes Runtime Boundary) — 합의 시점 결정

---

## 6. G4 — Provider-agnostic Memory/Skill 형식

### 6.1 정의

**G4**: Memory / Skill 의 저장 형식이 Hermes 의존 없이 다른 오케스트레이터(Claude Code, GPT, Gemini, Local LLM)로 import 가능한 표준 형식으로 정의된 상태. 헌법 5조 (Provider Liquidity) 의 Memory/Skill 경로 강제.

**근거**: 헌법 5조 + system-identity-prequel §4.2 G4 + ADR-008 차단조건 #2 (JSONL export) 의 Memory/Skill 확장.

### 6.2 Memory 형식 (system-identity-prequel §8.4 흡수)

#### 6.2.1 2단계 Scope (확정)

| Scope | 위치 | 내용 |
|-------|------|------|
| Global | `~/.claude/global/` | 헌법, SDD/TDD 원칙, ADR 작성 방식, 역할 정의, 검증 원칙, 금지 사항 |
| Project | `<project>/.claude/project/` | 프로젝트 목표, 기술 스택, 도메인 용어, 주요 결정, 반복 버그, 테스트 전략 |

#### 6.2.2 형식 후보

- **Markdown** (사람 검토 대상): 헌법, ADR, 결정 기록
- **JSONL append-only** (자동화 분석 대상): 학습 패턴, 실패 회피 휴리스틱
- **YAML** (구조화 메타): 역할 정의, scope 경계

#### 6.2.3 Provider-agnostic 강제 메커니즘 후보

- Hermes plugin 의존 import 0건 검증 (depcruise)
- JSONL append-only + hash chain (변조 방지, prequel §6.3 흡수)
- 다른 오케스트레이터 sample import 1회 시연 (`hermes_to_claude.py`, `hermes_to_gpt.py` 등 변환 스크립트)

#### 6.2.4 Boundary 강제

- 파일시스템 분리 (1차)
- 환경변수 `CLAUDE_MEMORY_SCOPE=global|project` (2차)
- Hermes memory plugin 사용 시 plugin scope 검증 항목 (G4 의존)

#### 6.2.5 Project → Global 승격

**manual only** (자동화 금지). 패턴이 일반화될 만한지 사용자가 판단.

### 6.3 Skill 형식

#### 6.3.1 형식 후보

- **YAML 메타** (`skill.yaml`): 이름 / 설명 / trigger / 입력 / 출력 / 권한 등급
- **Markdown 본문** (`skill.md`): 사용자 검토 대상 사용 방법 / 예시
- **실행 코드** (`skill.py` 또는 `skill.sh`): 옵션, 격리 환경에서 실행

#### 6.3.2 Provider-agnostic 강제 메커니즘 후보

- Hermes 자체 skill DSL 의존 0건 (표준 YAML/Markdown/Python)
- 다른 오케스트레이터에서 import 가능 (변환 스크립트 시연)
- T2 등록 (사용자 승인 강제, ADR-011 §2.4)

#### 6.3.3 Skill 추출 자동화

- T1 자동: 반복 작업 패턴 → Skill 후보 추출 + 알림
- T2 사용자 승인: 후보를 정식 Skill로 등록
- T3 절대 금지: Constitution/ADR/SDD 변경하는 Skill

### 6.4 Entry / Exit 기준 (제안)

#### 6.4.1 Entry

- ✅ ADR-008 차단조건 #2 (JSONL export 표준) 검증 완료
- ⏳ 사용자 명시 G4 작업 시작 결정

#### 6.4.2 Exit

| # | 조건 | 검증 방식 |
|---|------|---------|
| (a) | Memory 형식 + Skill 형식 ADR / SDD 명세 완성 | `docs/architecture/memory-scope-design.md` + `docs/architecture/skill-format-design.md` |
| (b) | Hermes 의존 import 0건 검증 (계산적) | depcruise 룰 + 자동 테스트 |
| (c) | 다른 오케스트레이터 sample import 1회 시연 | `scripts/hermes-migration/` 1회 시연 (ADR-008 §2.2 R2-5와 통합) |
| (d) | T1/T2/T3 분류가 형식별로 명시 | 매트릭스 표 |
| (e) | 단축 합의 또는 풀 3+1 합의 APPROVE | `docs/review/3plus1-consensus-YYYY-MM-DD-g4.md` |

### 6.5 메타-템플릿 복사 시 오염 방지 (system-identity-prequel §8.4 흡수)

- 본 템플릿 `.gitignore` 에 `.claude/project/memory.jsonl` 추가
- 복사 후 init script (`init-project.sh`) 로 Project Memory 초기화

### 6.6 산출 후보

- `docs/architecture/memory-scope-design.md`
- `docs/architecture/skill-format-design.md`
- `scripts/hermes-migration/hermes_to_claude.py` (sample 변환)
- `scripts/hermes-migration/hermes_to_gpt.py` (sample 변환)
- 합의 보고서

### 6.7 의존 ADR / 갱신 후보

- ADR-008 차단조건 #2: Memory/Skill 형식 cross-reference 추가
- ADR-009 (자체 Adapter v2.0 진입조건): G4 충족과 자체 Adapter 진입의 관계 갱신
- 신규 ADR 후보: ADR-014 (Provider-agnostic Memory/Skill Format) — 합의 시점 결정

---

## 7. 동시 갱신 ADR 매트릭스

> **본 §7은 ADR 본문 자동 갱신을 트리거하지 않는다.** 본 §7은 v3 정식 채택 시점에 동시 갱신될 ADR 후보 항목 목록이다. 갱신은 별도 PR 묶음.

| ADR | 갱신 항목 | 본 v3 인용 |
|-----|---------|---------|
| **ADR-008** | 본문 §6 차단조건 #1 충족 메커니즘 → 본 v3 §1.3 cross-reference 추가. 부록 B 그대로 유지. | §1.3 |
| **ADR-008** | 본문 §단계 마이그레이션 → 본 v3 §3.6 (현 활성화 상태) cross-reference 추가 | §2.4, §3.6 |
| **ADR-009** | 자체 Adapter v2.0 진입조건 → G4 PASS 후 재평가 cross-reference 추가 | §6.7 |
| **ADR-010** | SQLCipher Vault HSM 키 관리 → G1b PASS evidence cross-reference 추가 | §3.3 |
| **ADR-011** | §2.2 G1b 정식 충족 조건 표 → R-7 SOP §4.2 PASS 갱신 결과 cross-reference 추가 | §3.3 |
| **ADR-011** | §8.5 후속 작업 → G2 / G3 / G4 산출 등록 (작성 시) | §4.4, §5.6, §6.6 |

**갱신 절차**: 본 v3 정식 채택 합의 → ADR PR 묶음 1건 → INDEX/CONTEXT 갱신.

---

## 8. v2 carry-over 매핑

> **본 §8은 P2 v2 본문이 변경 없이 v3로 이월되는 섹션을 명시한다.** 본 v3는 carry-over 본문을 *재서술하지 않는다* — v3 정식 채택 시 v2 archived + 본 §8 매핑이 권위 인용 경로.

| v2 섹션 | 본문 위치 (v2) | v3 위치 |
|--------|------------|--------|
| §1.4 전제 조건 | `hermes-adoption-design.md` §1.4 | 변경 없음 (carry-over) |
| §1.5 ADR-008과의 관계 | §1.5 | 변경 없음 |
| §1.6 P1과의 관계 | §1.6 | 변경 없음 |
| §1.7 하네스 위치 | §1.7 | 변경 없음 |
| §2.0 차단조건 분류 | §2.0 | 변경 없음 |
| §2.1.1 SQLite → SQLCipher 전환 | §2.1.1 | 변경 없음 |
| §2.1.2 Vault HSM + Shamir SSS | §2.1.2 | 변경 없음 (ADR-010 위임) |
| **§2.1.3 Pre-Record Redaction Hook** | §2.1.3 | **갱신** (본 v3 §1.3 + §3.3 G1b 메커니즘으로 대체) |
| §2.1.4 Base64 우회 테스트 | §2.1.4 | 변경 없음 (R-4.1 Tier-1 42 catalog 흡수 후 cross-reference) |
| §2.1.5 검증 방법 | §2.1.5 | 변경 없음 (R-7 SOP 8 PASS 조건과 cross-reference) |
| §2.1.6 미충족 시 | §2.1.6 | 변경 없음 (R-7 SOP §5 9 ROLLBACK trigger와 cross-reference) |
| §2.2 차단조건 #2 (JSONL Export + 마이그레이션) | §2.2 | 변경 없음 (G4와 cross-reference 추가 가능) |
| §2.3 차단조건 #3 (버전 핀 + 회귀 + 카나리) | §2.3 | 변경 없음 (R-6 workflow와 cross-reference) |
| §2.4 차단조건 #4 (P1 Facade 위임) | §2.4 | 변경 없음 |
| §2.5 차단조건 #5 (Min 2 Active) | §2.5 | 변경 없음 |
| §2.6 차단조건 #6 (Docker 격리) | §2.6 | 변경 없음 |
| §3 Phase 0 | §3 | 변경 없음 (단, **R-1 결과**는 본 v3 §3.2 G1a FAIL로 갱신) |
| §4 Phase 1 | §4 | 변경 없음 (단, **차단조건 #1 exit**는 본 v3 §3.3 G1b PASS로 갱신) |
| §5 Phase 2 | §5 | 변경 없음 |
| §6 Phase 3 | §6 | 변경 없음 |
| §7 롤백 | §7 | 변경 없음 (R-7 SOP §5 9 ROLLBACK trigger와 cross-reference) |
| §8 검증 메트릭 | §8 | 변경 없음 |
| §9 헌법 정합성 | §9 | 변경 없음 |

**carry-over 본문은 v2 archived 후에도 git history 로 추적 가능**. v3 정식 채택 시점부터 새 작업은 본 v3 본문을 권위 우선 인용.

---

## 9. 본 초안 범위 외 + 다음 단계

### 9.1 본 초안이 트리거하지 *않는* 것

- ❌ Hermes PMO 격상 활성화 commit
- ❌ G2 / G3 / G4 작업 자동 시작 (사용자 명시 결정 필요)
- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 자동 갱신 (별도 PR)
- ❌ `system-identity-prequel.md` 자동 archived 처리 (v3 정식 채택 시점에)
- ❌ P2 v2 (`hermes-adoption-design.md`) 자동 archived 처리 (v3 정식 채택 시점에)
- ❌ INDEX / CONTEXT 자동 갱신 (v3 정식 채택 시점에)
- ❌ Phase 1 / Phase 2 / Phase 3 진입 결정

### 9.2 다음 단계 진입 옵션

| 옵션 | 다음 단계 | 합의 형태 | 비고 |
|-----|---------|---------|-----|
| **A** | 본 초안 단축 합의 → v3 정식 채택 → ADR PR 묶음 → INDEX/CONTEXT 갱신 | 단축 합의 (Reviewer-only) | 본 초안 자체에 새 설계 안건 없음 (R-3 ~ R-7 + G1b PASS 권위 흡수 + G2/G3/G4 정의) — 단축 합의 적격 |
| **B** | G2 / G3 / G4 병행 작성 시작 → 작성 완료 후 v3 정식 채택과 함께 묶음 | 풀 3+1 (G2/G3/G4 통합 검증) | v3 정식 채택을 G2/G3/G4 작성 완료까지 보류 |
| **C** | 본 초안 보류 + 추가 evidence 대기 | 합의 미가동 | Phase 1 운영 evidence 누적 후 검토 |

**권고 옵션** (사용자 결정 후보, 본 초안은 *권고 단정 금지*): 옵션 A. 사유: G1b PASS evidence는 이미 권위 확정 (R-7 SOP §7.3 단축 합의), 본 v3는 그 결과를 P2 본문으로 흡수하는 작업. 새 설계 안건 없음. 단, 옵션 B / C 도 사용자 결정 시 정당.

### 9.3 다음 세션 진입점 후보

- "P2 v3 단축 합의 진행해주세요" → 옵션 A
- "G2 작업 시작해주세요" → 옵션 B 분기
- "G3 작업 시작해주세요" → 옵션 B 분기
- "G4 작업 시작해주세요" → 옵션 B 분기
- "P2 v3 초안 검토 보류" → 옵션 C

---

## 10. 영구 핵심 제약 (변동 없음)

본 v3 작성 + 정식 채택 + Hermes PMO 격상(미래) 전 과정에서 다음은 **무조건 영구 유지**:

| 제약 | 권위 근거 |
|------|---------|
| **Provider Liquidity** | 헌법 제5조 (비협상), `feedback_provider_liquidity.md` |
| **Hermes ≠ root of trust** | ADR-011 §2.3 (영구 권위), system-identity-prequel §3 → ADR 승격 |
| **메타포 강제 금지** | system-identity-prequel §7 (본 v3 §2.5로 흡수 — 격상 후도 메타포 정합성 위해 구조 늘림 금지) |
| **자동 정책 변경 금지 (T3)** | ADR-011 §2.4 |
| **수단/목적 분리 원칙** | ADR-011 §2.1 (a)~(d) 4조건, 본 v3 §3.3 / §4.3 / §5.4 / §6.4 의 exit 기준 패턴) |

---

## 11. 본 초안의 변경 절차

본 v3는 DRAFT 상태에서 다음 절차를 따른다:

| 변경 유형 | 절차 |
|---------|------|
| 단순 오타 / 문구 정리 | 사용자 단독 결정 가능 |
| §1 ~ §3 (Delta + 4 게이트 정의) 본문 갱신 | 사용자 명시 결정 |
| §4 / §5 / §6 (G2 / G3 / G4 정의) 본문 갱신 | 단축 합의 (Reviewer-only) |
| **DRAFT 상태 해제 → 정식 채택** | **단축 합의 또는 풀 3+1 합의 APPROVE** (옵션 A 또는 B) |
| §10 영구 핵심 제약 변경 | **풀 3+1 합의 + ADR Amendment 절차** (T3 변경 — 매우 신중) |

---

## 12. 부록 — 본 초안의 메타 편향 자기진단

본 초안은 다음 5 통제 수단을 명시 답습한다:

1. **사용자 명시 절차 답습**: Hermes PMO 격상 선언 금지, G2/G3/G4 PASS 선언 금지, 본 초안 작성까지만.
2. **R-7 SOP §0 핵심 선언 답습**: G1b PASS는 R-7 SOP §7.3 단축 합의 결과 인용, 본 v3가 새 PASS 선언 트리거하지 않음.
3. **ADR-011 §2.4 T1/T2/T3 답습**: 본 v3 §4 / §5 / §6 의 산출 후보는 모두 사용자 명시 결정(T2) 후 진입.
4. **수단/목적 분리 원칙 답습**: §4.3 / §5.4 / §6.4 의 Exit 기준 (a)~(e) 는 ADR-011 §2.1 (a)~(d) 4조건 패턴 답습.
5. **본 초안이 *하지 않는* 것 명시 (§0.2 + §9.1)**: Hermes PMO 격상 / P2 v3 정식 채택 / ADR 본문 자동 갱신 / system-identity-prequel 자동 폐기 / v2 자동 폐기 / Phase 진입 결정 모두 명시 부정.

본 5 통제는 G1b PASS 단축 합의(2026-05-07)의 5 통제 수단 답습이며, P2 v3 → Hermes PMO 격상까지 동일 패턴 유지.

---

**작성일**: 2026-05-07
**상태**: DRAFT (초안)
**다음 진입점**: 사용자 결정 — 옵션 A (단축 합의 → 정식 채택) / 옵션 B (G2 / G3 / G4 병행) / 옵션 C (보류)
**금지 (사용자 명시 답습, 변동 없음)**:
- ❌ Hermes PMO 격상 선언 자동
- ❌ P2 v3 본문 자동 갱신 (단순 오타 외)
- ❌ G2 / G3 / G4 자동 통과 선언
- ❌ 추가 정책 변경 자동 (ADR-011 §2.4 T3)
- ❌ Tier-2 / Tier-3 catalog 확장 자동 (별도 합의)
