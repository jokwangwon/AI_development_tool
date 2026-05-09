# ADR-009: P1 Facade MVP 진입조건 + 자체 LLM Adapter v2.0 진입 트리거

**상태**: 승인 (3+1 합의 결과 반영, Bβ-4) + **C-N 갱신 (단축 합의, 2026-05-09 후속 4)**
**날짜**: 2026-05-04 (초기 승인) / **2026-05-09 (C-N 갱신 — P1 facade MVP 진입조건 명시 + Hermes PMO ↔ provider 분리 + Provider Liquidity 5-way 답습 + P2 v3 cross-reference)**
**의사결정자**: 사용자 + 3+1 에이전트 합의 (초기) + **사용자 + Reviewer 단축 합의 (C-N 갱신, 2026-05-09)**
**상위 권위**: 헌법 제5조 관용 (Provider Liquidity), ADR-004 (외부 SDK 우선), ADR-008 (Hermes 도입 Option B), **ADR-011 §2.3 (Hermes ≠ root of trust)**, **ADR-012 §원칙 5 (Provider Liquidity 5-way Multi-layer Defense)**
**관련 합의**: `docs/review/3plus1-consensus-2026-05-04-p1-llm-providers.md` (Bβ-4 출처), **`docs/review/3plus1-consensus-2026-05-09-c-n-adr-009-update.md` (C-N 갱신 단축 합의)**

---

## C-N 갱신 요약 (2026-05-09 후속 4)

본 갱신은 다음 5 영역 흡수:

1. **P1 facade MVP 진입조건 명시** (§2 신설) — 기존 ADR-009 는 *v2.0 진입 트리거* 만 명시. MVP 조건이 *부재* 하여 P2 v3 정식 채택 합의 참조 시 모호. 본 갱신으로 명료화.
2. **Hermes PMO ≠ provider 직접 소유** (§2.3 신설) — Hermes PMO (활성화 후 후보 시점) 가 provider SDK 직접 import / 모델명 분기 코드 *금지*. P1 facade 단일 진입점 강제 (ADR-011 §2.3 + Provider Liquidity 5-way Layer 1 답습).
3. **Provider Liquidity 5-way Multi-layer Defense 답습** (§5 갱신) — 본 ADR-009 가 5-way Layer 1 (코드 lock-in 차단) 의 *모법 ADR* 임을 명시 (ADR-012 §원칙 5 발행으로 확정).
4. **자체 Adapter v2.0 진입 트리거 (T1~T4) vs P1 facade MVP 조건 명확 구분** (§3.0 신설) — 두 개념을 표 형식으로 분리. v2.0 트리거 4종 본문 변경 0건.
5. **P2 v3 정식 채택 합의 cross-reference** (§8 갱신) — 본 ADR 이 P2 v3 §1.6 (P1 과의 관계) + §6 G4 + §10 영구 핵심 제약에서 참조 가능하도록 cross-reference 명시.

**핵심 결정 변경 0건** + **자체 Adapter v2.0 트리거 (T1~T4) 본문 변경 0건** → 단축 합의 적격 (사용자 명시 답습).

---

## 1. 맥락 (Context)

### 1.1 P1 v2 설계 채택 (2026-05-04)

P1 설계(`llm-providers-design.md`)에서 LLM Provider 추상화 방안으로 **Option β (LiteLLM facade 승격)** 가 채택되었다. P1 facade 는 다음 핵심 보장:

- **모든 Worker / Hermes Agent 의 LLM 호출 = P1 facade 단일 진입점 경유**
- **LiteLLM 직접 import = `adapters/llm/facade.py` 한 파일 한정** (`llm-providers-design.md` §4 답습)
- **provider SDK (anthropic / openai / gemini 등) 직접 import = 어떤 작성 주체도 금지** (`llm-providers-design.md` §9 답습 — depcruise 룰 + AST 스캐너)
- **모델명 분기 코드 (`if model == "claude": ...`) = 어떤 작성 주체도 금지** (`llm-providers-design.md` §9)

자체 Adapter 작성은 v2.0 백업 옵션으로 보존되며, 본 ADR 은 (a) **P1 facade MVP 진입조건** + (b) **v2.0 으로 전환할 때의 정량 트리거** 를 명세한다.

### 1.2 본 ADR 부재 시 위험

이 ADR 이 없으면 다음 위험 발생 가능:

- 매몰비용·관성으로 LiteLLM 에 영구 종속 (P1 facade lock-in)
- 일시적 불편을 이유로 v2.0 자체 작성 시작 → ADR-004 본질 ("외부 SDK 우선") 재위반
- **P1 facade MVP 진입조건 부재 → P2 v3 정식 채택 합의 시 P1 ↔ Hermes ↔ provider 계층 모호** (C-N 갱신 사유)
- **Hermes PMO 가 자체 provider 소유 시도 → Provider Liquidity (헌법 5조 관용) 위반** (Provider Liquidity 5-way Layer 1 차단 부재 시)

---

## 2. P1 Facade MVP 진입조건 (C-N 신설, 2026-05-09)

### 2.1 MVP 진입 시점

**P1 facade MVP 는 다음 *모든* 조건 충족 시점에 *즉시* 진입 가능**:

| # | 조건 | 충족 시점 |
|---|------|---------|
| (a) | ADR-008 (Hermes 도입) Option B 합의 APPROVE | 2026-05-04 ✅ 충족 |
| (b) | P1 v2 (`llm-providers-design.md`) Option β 합의 APPROVE | 2026-05-04 ✅ 충족 |
| (c) | LiteLLM 라이센스 = Apache 2.0 (또는 동등 호환) 확인 | 2026-05-04 시점 ✅ |
| (d) | LiteLLM `Min 2 Active` provider 충족 가능성 (`llm-providers-design.md` §6) | 2026-05-04 시점 ✅ |

본 4 조건 모두 *2026-05-04 시점 이미 충족* — **별도 트리거 없음**. ADR-008 + P1 v2 합의 APPROVE = MVP 진입 의무 도화선 (자체 Adapter v2.0 진입 트리거와 *별도 개념*).

### 2.2 MVP 진입 의미

P1 facade MVP 진입 = 다음 의무 *즉시* 활성화:

| # | 의무 | 강제 매커니즘 |
|---|------|----------|
| 1 | LiteLLM 직접 import = `adapters/llm/facade.py` 한 파일 한정 | depcruise 룰 + AST 스캐너 (`llm-providers-design.md` §9) |
| 2 | provider SDK 직접 import (anthropic / openai / gemini 등) = 모든 작성 주체 금지 | depcruise 룰 + pre-commit hook |
| 3 | 모델명 분기 코드 (`if model == "claude": ...`) = 모든 작성 주체 금지 | depcruise 룰 + AST 스캐너 |
| 4 | `Min 2 Active` provider 의무 (런타임 재검증) | `llm-providers-design.md` §6 |
| 5 | OAuth 직결 금지 (P1 facade 경유 의무) | `llm-providers-design.md` §7 |
| 6 | provider 추가 시 P1 facade `adapters/llm/facade.py` 변경만으로 가능 (단일 진입점) | `llm-providers-design.md` §4 + §10 |

### 2.3 Hermes PMO ↔ Provider 분리 (C-N 핵심)

**Hermes PMO (활성화 후 후보 시점) 가 provider 를 직접 소유하지 않는다** — 본 ADR-009 §2.3 영구 권위.

| 영역 | Hermes PMO 권한 | P1 Facade 권한 |
|----|-------------|-------------|
| LLM 호출 진입점 소유 | ❌ (provider SDK 직접 import 금지) | ✅ (`adapters/llm/facade.py` 한 파일 한정) |
| Provider 라우팅 결정 | ❌ (LiteLLM Router 위임) | ✅ (`llm-providers-design.md` §5) |
| 모델명 분기 | ❌ (`if model == "claude":` 등 금지) | ✅ (config 기반, `llm-providers-design.md` §3 `llm-providers.yaml`) |
| 요청 / 응답 표준화 | ❌ | ✅ (Request/Response 표준 스키마, `llm-providers-design.md` §4) |
| 비용 / 관측성 / Redaction | ❌ (Tier-1 42 catalog 강제) | ✅ (`llm-providers-design.md` §8) |
| OAuth refresh single-flight | ❌ | ✅ (`llm-providers-design.md` §7) |
| Provider 추가 / 제거 / 교체 | ❌ (자기 격상 금지 — ADR-011 §2.4 T3) | ✅ (config 변경 + 사용자 명시 승인 — T2) |

**근거** (영구 권위):
- ADR-011 §2.3 (Hermes ≠ root of trust) — Hermes 권한 위계 답습
- ADR-008 차단조건 #4 (P1 Facade 위임 — `hermes-adoption-design.md` §2.4 답습)
- ADR-012 §원칙 6 (provider-neutral 강제) — Hermes 가 evidence ledger entry 작성 시에도 `agent` 필드 = provider-neutral identifier
- 헌법 5조 관용 (Provider Liquidity 비협상)

**Hermes PMO 격상 (활성화) 시점** (P2 v3 §2.6 7 단계 답습):
- 본 ADR-009 §2.3 분리는 *Hermes PMO 격상 후에도 영구 유지* — 격상 = 책임 활성화 *까지*, provider 소유 *아님*
- 격상 후 Hermes 가 provider SDK 직접 import 시도 = T3 위반 + Hermes-originated commit auto-reject (G3 §2.2 #20 답습)

---

## 3. 자체 LLM Adapter v2.0 진입 트리거 (초기 결정 — 변경 0건)

### 3.0 P1 Facade MVP vs v2.0 트리거 분리 (C-N 신설)

본 ADR 은 두 *별도* 개념을 다룬다:

| 개념 | 위치 | 진입 시점 | 트리거 |
|----|----|---------|------|
| **P1 facade MVP** | §2 | 2026-05-04 (ADR-008 + P1 v2 합의 APPROVE 시점) | 별도 트리거 없음 (4 충족 조건 § 2.1) |
| **자체 LLM Adapter v2.0** | §3.1 ~ §3.5 | 미정 (트리거 1개 이상 충족 시) | T1 ~ T4 정량 트리거 (§3.1~§3.4) |

**핵심**: P1 facade MVP 는 *현재 운영 중* (LiteLLM Option β). 자체 Adapter v2.0 은 *백업 옵션* — 트리거 충족 시점에만 진입.

### 3.1 결정 (Decision) — 자체 LLM Adapter v2.0 진입 결정 (변경 0건)

자체 LLM Adapter v2.0 작성은 다음 **트리거 중 1개 이상** 이 충족될 때에만 시작한다. 추측·선호·"느낌"으로는 진입할 수 없다.

#### T1. LiteLLM 신규 provider 미지원 (강한 트리거)
- 본 프로젝트가 도입하려는 신규 provider/모델을 **LiteLLM이 2분기(약 6개월) 내 지원하지 않음**
- AND 본 프로젝트가 제출한 PR이 거부 또는 무대응 1분기 이상 지속
- AND 해당 provider/모델이 본 프로젝트 핵심 워크플로의 필수 요소

#### T2. LiteLLM 라이센스 변경 (즉시 트리거)
- LiteLLM이 Apache 2.0에서 비호환 라이센스로 전환
- AND 새 라이센스가 본 프로젝트 운영 모델과 충돌 (예: 상업적 사용 제한)

#### T3. LiteLLM 정상화 불가 결함 (강한 트리거)
- LiteLLM에서 다음 결함 중 하나가 **2분기 이상 미해결**:
  - 보안 결함 (CVE 등급 HIGH 이상)
  - 본 프로젝트 핵심 워크플로 차단 버그 (회피 불가능)
  - 응답 정규화 결함으로 Provider Liquidity 위반 (역설적 lock-in)

#### T4. LiteLLM 운영 부담 정량 역전 (정량 트리거)
- 자체 Adapter 추정 유지 부담(40~80h/년)보다 **LiteLLM 통합/우회 부담이 더 커짐**
- 측정 기간: 4분기 연속
- 측정 방법: facade 보강 시간 + LiteLLM 버그 우회 시간 + 버전 추적 시간을 분기별 기록

### 3.2 트리거 미충족 시 — 자동 NO-GO (변경 0건)

위 4개 트리거 중 어느 것도 충족되지 않으면, 자체 Adapter 작성 제안은 **자동 반려** 한다. 다음 같은 사유는 트리거가 아니다:
- "외부 종속성 줄이고 싶다" (선호)
- "LiteLLM 업데이트가 잦다" (불편)
- "모든 코드를 자가 통제하고 싶다" (취향)
- "특정 provider만 사용하면 되니 LiteLLM 과잉" (단기적 판단)

---

## 4. 선택지 (Options Considered) — 변경 0건

### 옵션 A: 트리거 없이 v2.0 시점만 명시 (예: "1년 후 재검토")
- 장점: 단순
- 단점: 시점 도달 시 정당성 없이 자동 진입 가능 → ADR-004 본질 재위반

### 옵션 B: 정량 트리거 4종 명세 (T1~T4) ⭐ 채택
- 장점: 객관적 의사결정, ADR-004 본질 보호, 매몰비용 회피
- 단점: 트리거 측정 부담 (특히 T4의 시간 기록)

### 옵션 C: "필요 시 결정"으로 미명세
- 장점: 유연성
- 단점: 본 ADR 작성 목적 자체가 무력화

---

## 5. Provider Liquidity 5-way Multi-layer Defense (C-N 갱신, 2026-05-09)

본 ADR-009 는 **Provider Liquidity 5-way Multi-layer Defense 의 Layer 1 모법 ADR** 이다 (ADR-012 §원칙 5 발행으로 확정).

| Layer | 책임 영역 | 모법 / 답습 |
|------|--------|---------|
| **Layer 1** (코드 lock-in 차단) | 모든 작성 주체의 provider SDK 직접 import / 모델명 분기 코드 차단 | **본 ADR-009 §2.2** + G2 GP-5 (depcruise 룰) + `llm-providers-design.md` §9 |
| Layer 2 (Hermes-originated lock-in 변경 차단) | Hermes 작성 주체 한정 차단 | G3 §6.4 + 본 ADR-009 §2.3 |
| Layer 3 (Skill 메타데이터 차원) | `provider_bindings` schema *required*/*exclusive* 금지 | G4 §3.5 |
| Layer 4 (export format 차원) | JSONL Hermes 의존 0 + 최소 2 provider 재해석 가능 | G4 §4.3 |
| Layer 5 (Evidence 형식 차원) | 11 필드 모두 provider-neutral 강제 | ADR-012 §2.1 원칙 6 + G4 §4.2 |

**5 Layer 모두 충족** 시 Provider Liquidity 의 *완결성* 확보. 1 Layer 만 깨져도 lock-in 위험 잔존.

### 5.1 자체 Adapter v2.0 진입 시 Provider Liquidity 보장

자체 Adapter v2.0 진입 시점 (트리거 1+ 충족) 에도 **Provider Liquidity 5-way Layer 1~5 모두 보존 의무**:

- Layer 1: v2.0 자체 Adapter 도 단일 진입점 강제 (provider SDK 직접 import 금지)
- Layer 2 ~ Layer 5: 변경 없음 (Hermes / Skill / JSONL / Evidence 차원은 v2.0 무관)
- v2.0 진입 = *수단 변경* (LiteLLM → 자체 Adapter), *목적 보존* (Provider Liquidity 비협상) — ADR-011 §2.1 (a)~(e) 5조건 답습 의무

---

## 6. 근거 (Rationale)

### 6.1 초기 근거 (변경 0건)

P1 v2 설계가 LiteLLM 의존을 채택하는 만큼, 그 의존을 끊는 의사결정도 동일한 엄격함으로 게이트되어야 한다. ADR-004는 "외부 SDK 부족 입증 후에만 v2.0"이라 명시했고, 본 ADR은 그 "입증"을 정량 트리거로 구체화한 것이다.

### 6.2 C-N 갱신 근거 (2026-05-09)

P2 v3 정식 채택 합의 진입 *전*, 다음 모호 영역 해소 의무:

1. **P1 facade MVP 진입조건 부재** — P2 v3 §1.6 (P1 과의 관계) 참조 시 "MVP 가 언제 시작됐고 어떤 의무가 활성화되어 있는가" 모호 → 본 갱신 §2.1 + §2.2 명시
2. **Hermes PMO ↔ provider 계층 분리 부재** — Hermes PMO 격상 후 provider 소유 가능성 시사 → 본 갱신 §2.3 영구 권위로 차단
3. **Provider Liquidity 5-way Multi-layer Defense 모법 ADR 부재** — ADR-012 §원칙 5 가 "5-way" 명명을 발행했으나 Layer 1 의 *모법 ADR* 부재 → 본 갱신 §5 명시
4. **v2.0 트리거 vs MVP 조건 분리 부재** — 두 개념 혼동 가능 → 본 갱신 §3.0 매트릭스 명시
5. **P2 v3 cross-reference 부재** — 본 ADR 이 P2 v3 정식 채택 합의에서 인용 가능하도록 §8 강화

본 갱신 = *MVP 조건 명시* + *cross-reference 강화* + *모법 ADR 권위 확정* 한정. **자체 Adapter v2.0 트리거 (T1~T4) 본문 변경 0건** + **핵심 결정 (옵션 B 채택) 변경 0건** → 단축 합의 적격 (사용자 명시 답습).

---

## 7. 합의 결과

### 7.1 초기 3+1 합의 (2026-05-04, 변경 0건)

P1 (Option β) 합의의 일부로 다뤄짐. 별도 ADR 작성 의무는 Bβ-4 항목.

| 출처 | 핵심 |
|------|------|
| Agent C | "v2.0 진입조건을 정량 트리거로 명시 — 매몰비용 누적 회피" |
| Reviewer | "Option β 채택 시 진입조건 ADR 작성 의무 (Bβ-4)" |

### 7.2 C-N 갱신 단축 합의 (2026-05-09)

세부: `docs/review/3plus1-consensus-2026-05-09-c-n-adr-009-update.md`

| 차원 | 판정 | 핵심 근거 |
|------|----|---------|
| P1 facade MVP 진입조건 명시 (§2 신설) | **PASS** | 4 충족 조건 (a)~(d) 명시 + 6 의무 매커니즘 명시 + 진입 시점 = 2026-05-04 답습 |
| Hermes PMO ↔ provider 분리 (§2.3) | **PASS** | ADR-011 §2.3 + ADR-008 차단조건 #4 + ADR-012 §원칙 6 + 헌법 5조 답습 |
| Provider Liquidity 5-way 모법 ADR 권위 (§5) | **PASS** | ADR-012 §원칙 5 발행으로 5-way 명명 확정 + 본 ADR 이 Layer 1 모법 명시 |
| v2.0 트리거 vs MVP 조건 분리 (§3.0) | **PASS** | 분리 매트릭스 명시 + 두 개념 *별도 진입 시점* 명료 |
| P2 v3 cross-reference 강화 (§8) | **PASS** | P2 v3 §1.6 + §6 + §10 인용 가능 |
| **자체 Adapter v2.0 트리거 (T1~T4) 변경** | **변경 0건** | 단축 합의 적격 (사용자 명시 답습) |
| **핵심 결정 (옵션 B 채택) 변경** | **변경 0건** | 단축 합의 적격 |
| **Provider Liquidity 영향** | **5-way 답습 강화** | 본 ADR 이 Layer 1 모법으로 영구 명시됨 (보호 강도 ↑) |
| **메타 편향 통제** | **명시** | 본 갱신은 자체 코드 우호 결론 부재 — Hermes 권한 *축소* 답습 (Hermes ↔ provider 분리) |

---

## 8. 결과 (Consequences)

### 8.1 긍정적 (C-N 갱신 후)

- ADR-004 본질을 v2.0까지 보호 (변경 0건)
- 자체 Adapter 작성을 객관적 트리거로만 게이트 (변경 0건)
- 매몰비용 의사결정 회피 (변경 0건)
- **P1 facade MVP 진입조건 명료화** — P2 v3 정식 채택 합의 참조 시 모호성 해소 (C-N 신설)
- **Hermes PMO ↔ provider 계층 분리 영구 권위** — Hermes PMO 격상 후에도 provider 소유 시도 차단 (C-N 신설)
- **Provider Liquidity 5-way Multi-layer Defense 모법 ADR 확정** — Layer 1 권위 강화 (C-N 신설)

### 8.2 부정적

- T4 측정 부담 (분기별 시간 기록) — 변경 0건
- 트리거 모니터링 task 신설 — 변경 0건
- C-N 갱신 = 본 ADR 분량 약 2.5배 증가 (91 → 약 240 줄) — 가독성 ↓ (수용)

### 8.3 주의사항

- 트리거는 **OR** 관계 (1개라도 충족 시 진입 가능) — 단 충족 증거를 별도 검토 보고서로 기록 필수.
- v2.0 진입 시 본 ADR 갱신 + 새로운 ADR (예: ADR-XXX-self-adapter-v2-implementation) 로 실제 작성 결정 분리.
- LiteLLM 사용 중 발견되는 작은 불편은 facade 보강 (LOC 추가) 으로 처리 — 트리거가 아님.
- **본 ADR §2.3 Hermes PMO ↔ provider 분리는 영구 유지** — Hermes PMO 격상 시점에도 provider 소유 권한 부여 *금지* (T3 영역, ADR-011 §2.4 답습).
- **본 ADR §5 Provider Liquidity 5-way 모법 ADR 권위는 영구 유지** — 자체 Adapter v2.0 진입 시에도 5 Layer 모두 보존 의무 (ADR-011 §2.1 (a)~(e) 5조건 답습).

---

## 9. 관련 문서

### 9.1 상위 권위

- `docs/constitution/PROJECT_CONSTITUTION.md` 제5조 관용 (Provider Liquidity)
- `docs/decisions/ADR-004-generative-ai-extensibility.md` (외부 SDK 우선 원칙)
- `docs/decisions/ADR-008-hermes-adoption-decision.md` (Hermes 도입 Option B + 차단조건 #4 P1 Facade 위임)
- `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.3 (Hermes ≠ root of trust 영구 권위)
- `docs/decisions/ADR-012-evidence-ledger-protection.md` §원칙 5 + 원칙 6 (Provider Liquidity 4-way → 5-way Multi-layer Defense)

### 9.2 관련 설계

- `docs/architecture/llm-providers-design.md` (P1 v2, §15 Phase 로드맵 v2.0 항목, §4 LLM Facade 인터페이스, §6 Min 2 Always-On, §9 Liquidity 위반 패턴 차단)
- `docs/architecture/hermes-adoption-design-v3.md` §1.6 (P1 과의 관계), §6 (G4 — Provider-agnostic Memory/Skill), §10 (영구 핵심 제약)
- `docs/architecture/governance-preconditions.md` GP-5 (Provider Adapter 강제)
- `docs/architecture/hermes-not-root-of-trust-runtime.md` §6.4 (Hermes-originated lock-in 변경 차단)
- `docs/architecture/provider-agnostic-memory-skill-design.md` §3.5 + §4.3 (Provider Liquidity 4-way / 5-way)

### 9.3 합의 보고서

- `docs/review/3plus1-consensus-2026-05-04-p1-llm-providers.md` (Bβ-4 출처, 초기 ADR 발행)
- `docs/review/3plus1-consensus-2026-05-09-c-n-adr-009-update.md` (C-N 갱신 단축 합의, 2026-05-09)
- `docs/review/3plus1-consensus-2026-05-09-pr2-evidence-ledger.md` (ADR-012 §원칙 5 발행 — 5-way 명명 출처)

### 9.4 P2 v3 cross-reference (C-N 신설)

본 ADR 은 P2 v3 정식 채택 합의에서 다음 위치에 cross-reference 가능:

| P2 v3 § | 본 ADR cross-reference |
|--------|------------------|
| §1.6 (P1 과의 관계) | 본 ADR §2 (P1 facade MVP 진입조건) + §3.0 (MVP vs v2.0 분리) |
| §2.3 (Hermes 권위 위계) | 본 ADR §2.3 (Hermes PMO ↔ provider 분리) |
| §6 (G4 — Provider-agnostic Memory/Skill) | 본 ADR §5 (Provider Liquidity 5-way Layer 1 모법) |
| §10 (영구 핵심 제약 — Provider Liquidity) | 본 ADR §5 + §8.3 영구 유지 |
