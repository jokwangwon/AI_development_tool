# Agent B — 보안/거버넌스 분석 (P2 v3 DRAFT → 정식 채택 풀 3+1 합의)

**작성일**: 2026-05-09
**Agent 역할**: 보안/거버넌스 검증가 (3+1 풀 합의 — Phase 2 독립 분석)
**검토 범위**: P2 v3 (`docs/architecture/hermes-adoption-design-v3.md`) DRAFT → *정식 채택* 가능 여부의 *보안/거버넌스 견고성 관점* 입력
**입력 9건**: C-14 응답 2건 (Claude 인접 컨텍스트 + Gemini 사고모델) + C-14 11 핵심 조건 체크리스트 + ADR-012 + G4 §4.2/§4.4/§4.6 + ADR-009 C-N 갱신 + G2 §1.2.6 P10 + G1b PASS + G2/G3/G4 Design/Governance Gate PASS + PR-1/PR-2/C-N/P10 흡수 완료 상태
**검토자 컨텍스트**: 본 분석은 메인 컨텍스트와 동일 Claude 패밀리 인스턴스가 작성 — 자기참조 + 메타 편향 위험 인지하며 §0.3 + §6 + §7 에서 통제. 자기참조 통제는 C-14 응답 2건 (Claude 인접 + Gemini 사고모델 cross-vendor) 으로 *부분* 흡수
**격상 범위 외**: Hermes PMO 격상 선언 / Hermes Runtime Implementation PASS / Implementation 영역 (PoC 실증, runtime hook, migration script) / ADR 본문 자동 갱신 / archive 자동 처리 — 본 합의 영구 답습

---

## 0. 본 입력의 입장 + 메타 한계

### 0.1 핵심 입장 (한 문장)

P2 v3 *Design Adoption only* 한정 정식 채택은 **APPROVE WITH CONDITIONS** — 5 평가 차원 (Hermes PMO 격상 분리 / ADR-012·G4·P10 반영 / Hermes ≠ root of trust / Provider Liquidity 5-way / 자동 정책 변경 부재) 모두 *Design 권위 격상* 차원에서 적격이며 영구 핵심 제약 5건 (Provider Liquidity / Hermes ≠ root of trust / 메타포 강제 금지 / T3 / 수단/목적 분리) 의 보호 layer 도 ADR-009 C-N + ADR-011 §2.3 + ADR-012 §원칙 5/6 + §2.12 매트릭스로 *영구 권위 layer* 가 존재하나, **P2 v3 §0.2 / §2 / §3 / §6 / §7 / §10 본문이 ADR-012 + G4 §4.2/§4.4/§4.6 + G2 §1.2.6 P10 + ADR-009 C-N + Provider Liquidity 5-way 를 *내부 답습* 으로 명시 흡수하지 않으면 archive 후 권위 layer drift (특히 Provider Liquidity 5-way Layer 5 와 Hermes 변조 차단 매트릭스 4항목) 위험이 *정식 채택 시점* 에 1회 동결된다**. C-14 응답 2건의 7+4 핵심 조건 모두 *본문 흡수 권고* 범주이며, P2 v3 본문 *현 상태* 자체가 차단 사유는 아니다 (C-14 1 §7.10 / C-14 2 §7.10 모두 APPROVE WITH CONDITIONS — 진입 승인 + 4~7 조건 흡수 의무).

### 0.2 본 분석의 *판정하지 않는* 것

- ❌ Hermes PMO 격상 자동 권유 (4 게이트 통과 + 사용자 명시 결정 + 인간 리뷰 — Gemini §7.10 #3 답습 — 후 별도)
- ❌ Hermes Runtime Implementation PASS 자동 발화
- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012 본문 자동 갱신 권유 (cross-reference 권고 한정)
- ❌ G2 / G3 / G4 본문 자동 갱신 (Design/Governance PASS 후 Implementation 영역 별도)
- ❌ P2 v2 / system-identity-prequel archive 자동 처리 발화 (정식 채택 시점에 별도 commit)
- ❌ P2 v3 본문 자동 갱신 (본 분석은 *Reviewer 종합 판정 입력* 한정)
- ❌ 실 runtime / migration / hook / canary catalog 코드 작성
- ❌ Tier-1/2/3 catalog 자동 확장
- ❌ 다른 Agent (A, C) 출력 참조 (Phase 2 독립 분석 답습)
- ❌ Reviewer 종합 합의 결과 발화

### 0.3 본 분석의 메타 한계 (강조)

본 입력은 메인 컨텍스트와 **동일 Claude 패밀리 인스턴스**. 자기참조 + 메타 편향 위험 인지. C-14 cross-vendor blind 의뢰 응답 2건 (Claude 인접 + Gemini 사고모델 — 비-Claude vendor) 으로 *부분 통제* 하나 1인 개발 환경 구조적 한계 (Gemini §7.6 + §7.11) 잔존.

본 분석에서 자체 식별한 메타 한계 7건:

1. **자기 작성 산출 자기 검토 한계** — Claude 패밀리 (Agent A/B/C + Claude 인접 외부 LLM 1건) 4/5 입력 + Gemini 1/5 입력. ADR-012 §11.1 메타-순환 청산 4 매커니즘 (사후 외부 LLM 충족 / 격상 전 면제 / 합의 권위 내부 변경 / 자기 작성 한계 명시) 답습.
2. **DRAFT 시점 (2026-05-07) 의 §3 4 게이트 진행 상태 표 vs 정식 채택 시점 (2026-05-09 이후) 의 *현재 상태* 정합성** — C-14 1 §7.2 + Gemini §7.2 가 동시에 지적한 *MUST UPDATE* 영역. 본 분석은 *상태표 동기화 권고* 까지, 본문 작성 권한 영역 *아님*.
3. **본 분석이 평가하는 P2 v3 본문은 2026-05-07 DRAFT** — ADR-012 (2026-05-09 발행) / G4 §4.2/§4.4/§4.6 보강 (2026-05-09 PR-2) / ADR-009 C-N (2026-05-09 후속 4) / G2 §1.2.6 P10 (2026-05-09 후속 5) / G2/G3/G4 Design Gate PASS (2026-05-09) 모두 *DRAFT 작성 후* 발생 — *현 본문* 이 아니라 *현재 권위 layer* 가 존재함을 평가 영역으로 분리.
4. **C-14 응답 2건 동시 일치 영역** (풀 3+1 권고 / Design Adoption only 제한 / 격상 전 인간 리뷰 / 5 영구 핵심 제약 archive 후 보존 강화) 은 *cross-vendor 일치* 강도 가산 — 본 분석은 *cross-vendor 일치 영역 = 강한 권고* 로 처리.
5. **Provider Liquidity 5-way Multi-layer Defense 의 archive 후 layer 약화 위험 평가** — ADR-009 C-N §5 가 5-way Layer 1 모법 ADR 영구 권위로 명시 (2026-05-09 후속 4) 하나, P2 v3 §10 본문이 *5-way 자체* 를 명시 답습하지 않음 → §6 흡수 권고. 본 분석은 *권고 의무* 까지, 본문 작성 권한 영역 *아님*.
6. **Hermes 변조 차단 매트릭스 4항목 (ADR-012 §2.12)** = PR-2 Agent B Gap-17 HIGH 의 ADR-012 본문 흡수 결과. P2 v3 §2.5 / §5 (G3) 가 본 매트릭스를 *직접 답습* 하지 않으면 격상 시 차단 layer 약화. 본 분석은 *cross-reference 권고* 까지.
7. **C-14 1 (Claude 인접) §7.7 + Gemini §7.7 동시 강조** — system-identity-prequel archive 시 메타포 금지 + 수단/목적 분리 등 영구 제약이 *단순 참조가 아니라 강제 규정으로 재선언* 되어야 함. 현 P2 v3 §10 표 형식은 *cross-vendor 일치 권고* 기준에서 *약화* — 본 분석은 *Normative Constraints 명시 격상 권고* 까지.

---

## 1. P2 v3 12 섹션 본문 보안/거버넌스 평가

### 1.1 §0 (본 초안의 운명과 범위) — APPROVE

§0.1 (하는 것 7항목) + §0.2 (하지 않는 것 8항목) + §0.3 (정식화 절차 6단계) 모두 *경계 획정* 명료. **§0.2 #1 (Hermes PMO 격상 선언 미발생) + §0.2 #6 (자동 정책 변경 절대 금지) 가 본 합의 단일 질문 #1 + #5 의 본문 답습 layer**. Gemini §7.3 *조건부 적정* 판정 + C-14 1 §7.7 *Hermes PMO non-activation clause 추가 권고* 모두 §0.2 가 *부분 흡수* 한다. 단 §0.3 단계 4 ("v3 정식 채택 + v2 archived + prequel archived") 가 본 합의 진입 후 발생할 작업의 정합성 = §10 영구 핵심 제약 보존 layer 와 결합 검증 의무 (§2 차원 4 + §5 영구 제약 enumeration).

**판정**: **APPROVE** — 단, §0.3 단계 4 archive 시점의 영구 제약 보존 검증은 §10 본문 강화 또는 archive commit 시점 *Normative Constraints* 명시로 흡수 의무 (Gap-1, §3).

### 1.2 §1 (v2 → v3 차이 Delta) — APPROVE

§1.1 ~ §1.5 5 hub 모두 *evidence chain* (R-2 ~ R-7 + R-6 actual run `25482284523`) 답습 정합. ADR-011 §2.1 (a)~(d) 4조건 패턴 답습 (§1.4 R-4 / R-4.1 / R-5 / R-6 cross-reference). **§1.3 차단조건 #1 충족 메커니즘 갱신** = G1b PASS evidence 흡수의 *수단/목적 분리* 본문 정합 (보안 결과 = DB 평문 secret 차단, 수단 = SQLCipher trigger + REGEXP UDF + Tier-1 42 catalog).

**판정**: **APPROVE** — 변경 없음. 본 합의 진입 차단 사유 0건.

### 1.3 §2 (Hermes PMO 구조 — 활성화 후보 대상의 사전 정의) — APPROVE WITH CONDITIONS

**핵심 평가 영역** (본 합의 단일 질문 #1 + #3 직접 영역):

| 항목 | 본 v3 답습 | 평가 |
|---|---|---|
| §2.1.1 격상 후 책임 10항목 | T1/T2/T3 권위 등급 명시 | **PASS** — ADR-011 §2.4 답습 정합 |
| §2.1.2 Hermes 가 *하지 않는* 것 (영구 6항목) | T3 + Hermes-originated commit auto-reject | **PASS** — ADR-011 §2.3 + §2.4 답습 정합 |
| §2.2 권위 위계 (Constitution > ADR > SDD > Harness Gates > Hermes > Worker Agents) | ADR-011 §2.3 영구 권위 인용 | **PASS** — system-identity-prequel §3 ADR 승격 답습 |
| §2.3 5 운영 함의 | ADR-011 §2.3 답습 | **PASS** |
| §2.4 비활성 상태 책임 | ADR-008 합의 자동화 + R-6 CI 회귀 검증만 | **PASS** — 현 시점 (2026-05-09 후속 5) Hermes 책임 한정 정합 |
| §2.5 활성화 후 책임 (4 게이트 통과 시) | "본 v3 범위 외" 명시 | **PASS** |
| §2.6 격상 절차 7 단계 | G1b PASS ✅ + G2/G3/G4 ⏳ + 통합 검증 합의 + 사용자 명시 + 격상 commit | **PASS** — Gemini §7.3 "구조 정의와 활성화 선언 명확 분리" 답습 |

**Gemini §7.3 + C-14 1 §7.3 cross-vendor 일치 권고** (C-14 1 §7.3 + Gemini §7.10 #3 답습):
> P2 v3 §2 상단에 "본 §2 는 Hermes PMO 의 활성화 선언이 아니라, 향후 활성화 검토 시 사용할 구조 사양이다. 본 §2 의 정식 채택은 Hermes 에 추가 권한을 부여하지 않는다. Hermes PMO 격상은 4 게이트 Implementation/Runtime PASS 및 별도 사용자 승인 전까지 금지된다." 강하게 명시 권고.

현 §2 상단 (3 줄) 이 *부분 흡수* 하나 cross-vendor *일치 강도* 권고는 *non-activation clause* 형태로 강화. **Gemini §7.10 #3** = "Hermes PMO 실제 활성화 전, 최소 1회 이상의 *전문적인 인간 리뷰 (Human-in-the-loop)* 를 통한 거버넌스 최종 확인 명문화" 추가 — §2.6 단계 5~7 또는 §11 변경 절차에 인간 리뷰 명시 의무.

**ADR-009 C-N §2.3 (Hermes PMO ↔ provider 분리)** 답습 cross-reference 부재 — §2.5 활성화 후 책임에 "**Hermes PMO 격상 후에도 provider SDK 직접 import / 모델명 분기 코드 / Provider 라우팅 결정 권한 부여 금지** (ADR-009 C-N §2.3 영구 권위 답습)" 명시 권고.

**판정**: **APPROVE WITH CONDITIONS** — Conditions:
- C-1 (Gemini §7.3 + §7.10 #3 + C-14 1 §7.3 + §7.7 + §7.10 #3 cross-vendor 일치): §2 상단에 PMO non-activation clause 강화 + §2.6 또는 §11 에 격상 전 인간 리뷰 의무 명문화 (Gap-2)
- C-2 (ADR-009 C-N §2.3 cross-reference): §2.5 에 Hermes PMO ↔ provider 분리 영구 권위 cross-reference 흡수 (Gap-3)

### 1.4 §3 (4 게이트 정의 + 진행 상태) — BLOCK / MUST UPDATE

**Gemini §7.2 + C-14 1 §7.2 cross-vendor 일치 강력 권고** (MUST UPDATE):

§3.1 4 게이트 개요 표가 2026-05-07 DRAFT 시점:
- G1b ✅ PASS (2026-05-07)
- G2 ⏳ **미작성**
- G3 🟡 **ADR 권위 확정 / 운영 구현 미작성**
- G4 ⏳ **미작성**

**현 (2026-05-09 후속 5) 시점 실제 상태**:
- G1b ✅ Implementation/Runtime PASS (2026-05-07, R-7 SOP §7.3 단축 합의)
- G2 ✅ **Design/Governance Gate PASS (Bundled, 2026-05-09)** + Implementation/Runtime PENDING
- G3 ✅ **Design/Governance Gate PASS (Bundled, 2026-05-09)** + Implementation/Runtime PENDING
- G4 ✅ **Design/Governance Gate PASS (Bundled, 2026-05-09)** + Implementation/Runtime PENDING

§3.5 합산 (1/4) 도 현 상태 (Design 4/4 + Implementation/Runtime 1/4) 와 *직접 모순*. 정식 채택 시 *영구 권위 문서* 가 되므로 후속 참조자 (에이전트 / 개발자) 가 "G2/G3/G4 미작성" 으로 오해 가능 (Gemini §7.2 명시).

**C-14 1 §7.2 권고** (cross-vendor 일치):
- §3.1 → §3.1 (Original Draft Snapshot — 2026-05-07 기준 상태)
- §3.2 → §3.2 (Adoption-time Status — 2026-05-09 이후 현재 상태)
- §3.3 → §3.3 (Delta — DRAFT 이후 G2/G3/G4 Design/Governance PASS + PR-1 + PR-2 + C-N + P10 정식 등록 반영)

**C-14 1 §7.5 + Gemini §7.5 cross-vendor 일치** (Implementation Pending 명시 표 추가):

| 영역 | 상태 |
|---|---|
| G1b DB-level fallback | Implementation/Runtime PASS (2026-05-07) |
| G2 GP-1 | Implementation/Runtime PASS (G1b evidence 흡수, Tier-1 한정) |
| G2 GP-2 ~ GP-6 | Design/Governance PASS / Implementation Pending |
| G3 runtime enforcement | Design/Governance PASS / Implementation Pending |
| G4 migration / round-trip | Design/Governance PASS / Implementation Pending |
| ADR-012 evidence protection CI | Design PASS / Implementation Pending |
| Hermes PMO activation | **Not authorized** |

**P10 정식 등록** (2026-05-09 후속 5, G2 §1.2.6) cross-reference 부재 — §3 또는 §7 ADR 매트릭스에 P10 정식 등록 시점 명시 권고.

**판정**: **BLOCK / MUST UPDATE** (정식 채택 *전* 본문 갱신 의무) — Conditions:
- C-3 (Gemini §7.2 + C-14 1 §7.2 cross-vendor 일치 + §7.5 동시 일치): §3 이중 구조 (DRAFT Snapshot + Adoption-time Status + Delta) + Implementation Pending 표 추가 (Gap-4 HIGH)

**보안/거버넌스 차원**: §3 본문 *현재성 확보 의무* 는 정식 채택 *문서 무결성* 의 핵심 — 본 합의 *진입 자체* 차단 사유 *아님* (C-14 1 §7.10 + Gemini §7.10 모두 APPROVE WITH CONDITIONS), *정식 채택 commit 전 본문 갱신 의무* 영역.

### 1.5 §4 (G2 — 6 거버넌스 사전조건) — APPROVE WITH CONDITIONS

**현 (2026-05-09 후속 5) 시점 실제 상태**:
- G2 §1.2.6 P10 정식 등록 완료 (위반 경로 P1~P8 → **P1~P8 + P10 = 9건**)
- GP-1 ~ GP-6 Design/Governance Gate PASS (Bundled, 2026-05-09)

**§4 본문 평가**:

| 항목 | 본 v3 답습 | 평가 |
|---|---|---|
| §4.1 정의 | 헌법 8조/5조 위반 경로 P1~P8 + 강제 메커니즘 | **PARTIAL** — P10 (Evidence Forgery) 정식 등록 (2026-05-09 후속 5) 후 **P1~P8 + P10 = 9건** 으로 갱신 의무 |
| §4.2 6 사전조건 식별 후보 | GP-1 (DB 평문 차단) ~ GP-6 (자동 정책 변경 차단) | **PARTIAL** — GP-1 = G1b PASS / GP-2~GP-6 = Design PASS / Implementation Pending 갱신 의무 |
| §4.3 Entry / Exit 기준 | (a)~(e) ADR-011 §2.1 패턴 답습 | **PASS** |
| §4.4 산출 후보 | governance-preconditions.md (정식 매핑) | **PARTIAL** — 본 산출 = 2026-05-09 작성 완료 + Design/Governance PASS, *현 본문 위치* 갱신 |
| §4.5 의존 ADR / 갱신 후보 | ADR-008 / ADR-011 + 신규 ADR-012 후보 | **PARTIAL** — ADR-012 = 2026-05-09 정식 발행, *후보* → *발행됨* 갱신 의무 |

**ADR-012 §1.3 trigger** (G2 §1.2.5 P10 정식 등록 *트리거*) cross-reference 부재 — §4.2 또는 §4.5 에 P10 정식 등록 흡수 권고.

**판정**: **APPROVE WITH CONDITIONS** — Conditions:
- C-4 (G2 §1.2.6 답습): §4 본문에 P10 정식 등록 (2026-05-09 후속 5) + GP-1 Implementation/Runtime PASS / GP-2~GP-6 Design/Governance PASS + ADR-012 발행 완료 cross-reference 의무 (Gap-5)

### 1.6 §5 (G3 — Hermes ≠ Root of Trust 운영 구현) — APPROVE WITH CONDITIONS

**현 (2026-05-09 후속 5) 시점 실제 상태**:
- G3 Design/Governance Gate PASS (Bundled, 2026-05-09)
- G3 §5 (Evidence decision principle: PASS 성립 4 요건) + ADR-012 §2.12 (Hermes 변조 차단 매트릭스 4항목) 영구 권위 추가

**§5 본문 평가**:

| 항목 | 본 v3 답습 | 평가 |
|---|---|---|
| §5.1 정의 | ADR-011 §2.3 권위 위계 + 5 운영 함의 운영 가능 메커니즘 | **PASS** |
| §5.2 5 운영 메커니즘 후보 | Layer 1~2 hook / R-6 workflow / SQLCipher trigger / R-2 재실행 / T3 변경 감지 hook | **PASS** |
| §5.3 prequel §3.3 4 강제 메커니즘 | filesystem read-only / 합의 결과 git commit 우회 / audit log / 자동 reject | **PASS** |
| §5.4 Entry / Exit 기준 | (a)~(e) | **PARTIAL** — Design/Governance PASS 완료 사실 흡수 의무 |
| §5.5 합의 인프라 순환 권위 문제 | 별도 호스트 + git commit 우회 + 사용자 명시 commit 만 권위 | **PASS** |
| §5.6 산출 후보 | hermes-not-root-of-trust-runtime.md (가칭) | **PARTIAL** — 본 산출 = 2026-05-09 작성 완료 + Design/Governance PASS |
| §5.7 의존 ADR / 갱신 후보 | ADR-011 §8.5 + ADR-008 부록 + 신규 ADR-013 후보 | **PASS** |

**ADR-012 §2.12 Hermes 변조 차단 매트릭스 4항목** (Hermes-originated ledger entry / 파일 변조 / git commit / 외부 LLM 응답 위조) cross-reference 부재 — §5.2 또는 §5.3 에 *G3 ↔ ADR-012 §2.12 통합 매트릭스* 명시 권고. 본 매트릭스가 P2 v3 §5 본문에 직접 답습되지 않으면 archive (P2 v2 + system-identity-prequel) 후 *Hermes 변조 차단 layer* 의 *영구 권위 layer drift* 위험.

**G3 §5 PASS 성립 4 요건** ((i) Tools 검증 / (ii) Evidence Ledger entry / (iii) 사용자 명시 승인 / (iv) 합의 보고서 commit) cross-reference 부재 — §5.1 또는 §5.2 에 명시 권고.

**판정**: **APPROVE WITH CONDITIONS** — Conditions:
- C-5 (ADR-012 §2.12 + G3 §5 답습): §5.2 / §5.3 에 Hermes 변조 차단 매트릭스 4항목 + PASS 성립 4 요건 cross-reference 흡수 의무 (Gap-6 HIGH)
- C-6: §5.4 / §5.6 에 Design/Governance PASS 완료 흡수 + Implementation Pending 명시 (Gap-7)

### 1.7 §6 (G4 — Provider-agnostic Memory/Skill 형식) — APPROVE WITH CONDITIONS

**현 (2026-05-09 후속 5) 시점 실제 상태**:
- G4 Design/Governance Gate PASS (Bundled, 2026-05-09)
- G4 §4.2 schema **11 필드** (10 → 10 + `event` 신규, ADR-012 §2.2 답습)
- G4 §4.4 hash chain 사양 보강 (Layer 1~5 + RFC 8785 JCS + Genesis Hash + prev_hash 검증 실패 BLOCK + Full Rewrite 5 Layer 방어)
- G4 §4.6 round-trip 검증 절차 보강 (Tier-based + 3 ledger entry 형식 + Migration 검증 실패 rollback 조건)

**§6 본문 평가**:

| 항목 | 본 v3 답습 | 평가 |
|---|---|---|
| §6.1 정의 | Hermes 의존 없이 import 가능 표준 형식 | **PASS** |
| §6.2 Memory 형식 (2단계 Scope) | Global / Project / 형식 후보 (Markdown/JSONL/YAML) / Provider-agnostic 강제 | **PARTIAL** — JSONL §6.2.3 *권고* 수준, ADR-012 §2.3 답습 강화 의무 |
| §6.3 Skill 형식 | YAML/Markdown/Python / Provider-agnostic / T1/T2/T3 분류 | **PARTIAL** — `provider_bindings` 명시 부재 (G4 §3.5) |
| §6.4 Entry / Exit 기준 | (a)~(e) | **PARTIAL** — Design/Governance PASS 완료 흡수 의무 |
| §6.5 메타-템플릿 복사 시 오염 방지 | `.gitignore` + init script | **PASS** |
| §6.6 산출 후보 | memory-scope-design.md / skill-format-design.md / migration scripts | **PARTIAL** — 본 산출 = 2026-05-09 작성 완료 (`provider-agnostic-memory-skill-design.md` 단일 통합) + Design/Governance PASS |
| §6.7 의존 ADR / 갱신 후보 | ADR-008 차단조건 #2 + ADR-009 + 신규 ADR-014 후보 | **PARTIAL** — ADR-009 C-N 갱신 (2026-05-09 후속 4) + ADR-012 §2.1 ~ §2.12 + §3.1 ~ §3.5 cross-reference 의무 |

**ADR-012 §2.2 11 필드 schema** (`type/scope/id/schema_version/ts/agent/event/content/evidence_refs/prev_hash/hash`) + §2.3 (Layer 1~5 다층 강제) + §2.5 (RFC 8785 JCS) + §2.6 (Genesis Hash) + §2.7 (prev_hash 검증 실패 BLOCK + manual review) + §2.8 (Full Rewrite 5 Layer 방어) + §2.9 (Round-trip Tier-based) + §2.10 (Migration 검증 실패 rollback) cross-reference 부재 — §6.2.2 / §6.2.3 / §6.3.2 본문 갱신 의무.

**G2 §1.2.6 P10 정식 등록** + **ADR-009 C-N §5 Provider Liquidity 5-way Multi-layer Defense** cross-reference 부재 — §6.1 또는 §6.7 에 흡수 권고.

**판정**: **APPROVE WITH CONDITIONS** — Conditions:
- C-7 (Gemini §7.4 #2 + C-14 1 §7.4 cross-vendor 일치): §6 본문에 ADR-012 §2.2~§2.12 + §3.1~§3.5 + G4 §4.2/§4.4/§4.6 보강 cross-reference 흡수 의무 (Gap-8 HIGH)
- C-8 (ADR-009 C-N §5 + ADR-012 §원칙 5 답습): §6 또는 §10 에 Provider Liquidity 5-way Multi-layer Defense (Layer 1~5) cross-reference 흡수 의무 (Gap-9 HIGH)

### 1.8 §7 (동시 갱신 ADR 매트릭스) — APPROVE WITH CONDITIONS

**§7 본문 평가**:

§7 표 (ADR-008 / ADR-009 / ADR-010 / ADR-011 갱신 항목) 가 ADR-012 (2026-05-09 발행) + ADR-009 C-N (2026-05-09 후속 4) cross-reference 0건. 본 합의 진입 후 ADR 본문 자동 갱신 *금지* 답습이지만 **cross-reference 매트릭스 갱신** 은 P2 v3 정식 채택 합의 *내부* 작업으로 가능 (C-14 1 §7.4 + Gemini §7.4 cross-vendor 일치).

**Gemini §7.4 권고**: "P2 v3 §7 ADR 매트릭스에 ADR-012 정식 편입 + G4 §6 Hash Chain 메커니즘을 *필수 참조 (Mandatory Reference)* 로 명시"

**ADR-009 C-N §9.4 cross-reference 의무 답습**:
- §1.6 (P1 과의 관계) → ADR-009 §2 (P1 facade MVP 진입조건) + §3.0 (MVP vs v2.0 분리)
- §2.3 (Hermes 권위 위계) → ADR-009 §2.3 (Hermes PMO ↔ provider 분리)
- §6 (G4 — Provider-agnostic Memory/Skill) → ADR-009 §5 (Provider Liquidity 5-way Layer 1 모법)
- §10 (영구 핵심 제약 — Provider Liquidity) → ADR-009 §5 + §8.3 영구 유지

**판정**: **APPROVE WITH CONDITIONS** — Conditions:
- C-9 (Gemini §7.4 + C-14 1 §7.4 cross-vendor 일치): §7 ADR 매트릭스에 ADR-012 정식 편입 + ADR-009 C-N 갱신 항목 4건 cross-reference 흡수 의무 (Gap-10 HIGH)

### 1.9 §8 (v2 carry-over 매핑) — APPROVE

§8 carry-over 본문 v2 archived 후 git history 추적 가능 명시. *변경 없음* 영역. **§2.2 차단조건 #2 (JSONL Export + 마이그레이션)** ↔ G4 cross-reference + **§2.4 차단조건 #4 (P1 Facade 위임)** ↔ ADR-009 C-N §2.2 / §2.3 cross-reference 추가 가능.

**판정**: **APPROVE** — 변경 없음. 보강 권고 (LOW priority).

### 1.10 §9 (본 초안 범위 외 + 다음 단계) — APPROVE WITH CONDITIONS

§9.1 *트리거하지 않는* 7항목 (Hermes PMO 격상 / G2/G3/G4 작업 자동 시작 / ADR 자동 갱신 / archive 자동 / INDEX/CONTEXT 자동 / Phase 진입) 모두 *영구 명시*. C-14 1 §7.7 + Gemini §7.7 cross-vendor 일치 *Hermes PMO non-activation clause* 권고와 정합.

§9.2 다음 단계 진입 옵션 (A/B/C) — **C-14 1 §7.9 + Gemini §7.9 cross-vendor 일치 = 풀 3+1 권고** (단축 합의 비권고). 본 합의가 *풀 3+1 + 외부 LLM 2건 + 사용자 명시 승인 + Evidence Ledger entry + adoption decision commit* 형태로 진행 시 정합.

**판정**: **APPROVE WITH CONDITIONS** — Conditions:
- C-10 (C-14 1 §7.9 + Gemini §7.9 cross-vendor 일치): 본 합의 형태 = *풀 3+1 + C-14 응답 2건 반영 + 외부 LLM 영역 cross-vendor 1+ + 사용자 명시 승인 + Evidence Ledger entry + adoption decision commit* (Gap-11 — 합의 형태 자체)

### 1.11 §10 (영구 핵심 제약) — APPROVE WITH CONDITIONS

§10 표 5 제약:
- Provider Liquidity (헌법 5조)
- Hermes ≠ root of trust (ADR-011 §2.3)
- 메타포 강제 금지 (system-identity-prequel §7)
- 자동 정책 변경 금지 (T3, ADR-011 §2.4)
- 수단/목적 분리 (ADR-011 §2.1 (a)~(d) 4조건)

**Gemini §7.7 + C-14 1 §7.7 cross-vendor 일치 강력 권고** (보완 필요 / ENHANCEMENT REQUIRED):

> P2 v2 와 system-identity-prequel archive 시 5 제약이 새 권위 문서 안에 *완전히 살아 있어야 함*. *단순 요약 / 단순 참조* 가 아니라 *Normative Constraints* 또는 *강제 규정으로 재선언*.

권장 문구 (C-14 1 §7.7 답습):
> Archiving P2 v2 or system-identity-prequel does not weaken, supersede, or delete the five permanent constraints. If any archived document contains stronger wording, the stronger constraint remains preserved through ADR-011 / ADR-012 and this section.

**ADR-009 C-N §5 Provider Liquidity 5-way Multi-layer Defense** (Layer 1 = 본 ADR 모법, Layer 2 = G3 §6.4, Layer 3 = G4 §3.5, Layer 4 = G4 §4.3, Layer 5 = ADR-012 §2.1 원칙 6 + G4 §4.2) cross-reference 부재 — §10 표에 *5-way 명시 답습* 권고.

**ADR-012 §9 5 영구 핵심 제약 = 5/5 HIGH 보호** 매트릭스 답습 cross-reference 권고.

**판정**: **APPROVE WITH CONDITIONS** — Conditions:
- C-11 (Gemini §7.7 + C-14 1 §7.7 cross-vendor 일치 + ADR-009 C-N §5 + ADR-012 §9 답습): §10 본문에 (i) Normative Constraints 명시 격상 + (ii) Provider Liquidity 5-way 답습 + (iii) archive 후 보존 강화 문구 흡수 의무 (Gap-12 HIGH)

### 1.12 §11 (본 초안의 변경 절차) — APPROVE WITH CONDITIONS

§11 표 5 행 (단순 오타 / §1~§3 / §4~§6 / DRAFT 해제 → 정식 채택 / §10 영구 제약 변경) 모두 *적정 분류*. **DRAFT 해제 → 정식 채택** = 단축 합의 또는 풀 3+1 합의 — Gemini §7.9 + C-14 1 §7.9 cross-vendor 일치 풀 3+1 권고.

**Gemini §7.10 #3 권고** (격상 전 인간 리뷰 의무화): §11 또는 §2.6 격상 절차에 "**Hermes PMO 실제 활성화 전, 최소 1회 이상의 *전문적인 인간 리뷰 (Human-in-the-loop)* 를 통한 거버넌스 최종 확인**" 명문화 의무.

**판정**: **APPROVE WITH CONDITIONS** — Conditions:
- C-12 (Gemini §7.10 #3 답습): §11 또는 §2.6 에 격상 전 인간 리뷰 의무 명문화 (Gap-2 답습 — C-1 통합)

### 1.13 §12 (메타 편향 자기진단) — APPROVE

§12 5 통제 수단 (사용자 명시 절차 답습 / R-7 SOP 답습 / ADR-011 §2.4 답습 / 수단/목적 분리 답습 / *하지 않는* 것 명시) 모두 *영구 답습*. 본 합의 진입 시 동일 메타 편향 통제 layer 유지.

**판정**: **APPROVE** — 변경 없음. C-14 응답 2건 (Gemini cross-vendor + Claude 인접) 영역에 §12 추가 답습 권고 (LOW priority, 본 합의 시점 흡수 가능).

---

## 2. 5 차원 평가 (사용자 명시)

### 2.1 차원 1 — Hermes PMO 격상과 P2 v3 정식 채택 분리

**평가**: **명료** (Gemini §7.8 *CLEAR* + C-14 1 §7.8 *조건부 명료* cross-vendor 일치)

**근거**:

P2 v3 본문 5 layer 분리 매커니즘:

| Layer | 분리 매커니즘 | 위치 |
|---|---|---|
| 1 | "Hermes PMO 격상 선언은 본 초안 범위 외" 명시 | §0.2 #1 (영구 답습) |
| 2 | 활성화 후보 사전 정의 = *구조 사양*, 활성화 *결정* 아님 | §2 (개요 강조) + §2.5 |
| 3 | 격상 절차 7 단계 (G1b PASS ✅ + G2/G3/G4 ⏳ + 통합 검증 + 사용자 명시 + 격상 commit) | §2.6 |
| 4 | 비활성 상태 책임 한정 (ADR-008 합의 자동화 + R-6 CI 회귀 검증만) | §2.4 |
| 5 | "본 초안이 트리거하지 *않는* 것" 7항목 (Hermes PMO 격상 활성화 commit 영구 명시) | §9.1 |

**C-14 응답 2건 답습** (cross-vendor 일치):
- C-14 1 §7.3: "본 §2 는 Hermes PMO 의 활성화 선언이 아니라, 향후 활성화 검토 시 사용할 구조 사양이다... Hermes PMO 격상은 4 게이트 Implementation/Runtime PASS 및 별도 사용자 승인 전까지 금지된다."
- Gemini §7.3: "구조 정의와 활성화 선언은 논리적으로 명확히 분리. §2.6 격상 절차는 '설계가 승인되었다고 해서 자동으로 가동되는 것이 아님' 보장."
- C-14 1 §7.5: "P2 v3 Design Adoption = 가능 / Hermes Runtime Adoption = 불가 / Hermes PMO Activation = 불가 / G2/G3/G4 Implementation PASS = 불가"
- Gemini §7.10 #3: "Hermes PMO 실제 활성화 전, 최소 1회 이상의 *전문적인 인간 리뷰 (Human-in-the-loop)* 를 통한 거버넌스 최종 확인 명문화"

**잔여 위험**:
- Gemini §7.3: "사전 정의는 실제 운영에서 쉽게 '이제 활성화해도 된다'는 심리적 신호로 작동 가능"
- C-14 1 §7.7: "정식 채택 이후 운영자가 'P2 v3 가 채택되었으니 Hermes PMO 도 켜도 된다' 오해 가능"

**판정**: **명료** (cross-vendor 일치) — 단 §2 상단 PMO non-activation clause 강화 + §2.6 또는 §11 격상 전 인간 리뷰 명문화 (C-1 + C-12) 흡수 시 *명료성 강화*.

### 2.2 차원 2 — ADR-012 / G4 hash chain / G2 P10 반영 충실성

**평가**: **부분 충실 / 갱신 의무**

**근거**:

P2 v3 본문 (2026-05-07 DRAFT) 작성 시점 vs 현 (2026-05-09 후속 5) 영구 권위 layer 차이:

| 영역 | DRAFT 시점 | 현 시점 | P2 v3 본문 답습 |
|---|---|---|---|
| ADR-012 (Evidence Ledger Protection) | (미발행) | 2026-05-09 정식 발행 | **0건** (cross-reference 부재) |
| G4 §4.2 schema 11 필드 | (10 필드, MVP) | 11 필드 (10 → 10 + `event` 신규) | **0건** (§6.2 본문 갱신 의무) |
| G4 §4.4 hash chain 다층 강제 | "둘 중 하나" 약 사양 | Layer 1~5 + RFC 8785 JCS + Genesis Hash + prev_hash 검증 실패 BLOCK + Full Rewrite 5 Layer | **0건** (§6.2.3 본문 갱신 의무) |
| G4 §4.6 round-trip Tier-based | "hash 일치 OR 의미 보존" 단순 OR | Tier-based + 3 ledger entry 형식 + Migration rollback | **0건** (§6.6 본문 갱신 의무) |
| G2 §1.2.6 P10 (Evidence Forgery) 정식 등록 | (deferred candidate) | 2026-05-09 후속 5 정식 등록 | **0건** (§4.1 / §4.5 본문 갱신 의무) |
| ADR-009 C-N (P1 facade MVP + Hermes ↔ provider 분리 + 5-way 모법 ADR) | (초기 결정만) | 2026-05-09 후속 4 갱신 | **0건** (§1.6 / §6.7 / §10 본문 갱신 의무) |

**ADR-012 §2.12 Hermes 변조 차단 매트릭스 4항목** + **ADR-009 C-N §2.3 Hermes PMO ↔ provider 분리** 모두 P2 v3 본문 흡수 의무 (C-2, C-5, C-7, C-8, C-9, C-10).

**C-14 응답 2건 cross-vendor 일치**:
- C-14 1 §7.4: "ADR-012 와 G4 §4.2 / §4.4 / §4.6 보강은 P2 v3 에 흡수되어야 함. 특히 P2 v3 가 Hermes Adoption Design 의 상위 통합 문서라면, Evidence Ledger 보호와 JSONL hash chain 강화는 핵심 전제. cross-reference 갱신은 P2 v3 합의 내부 작업으로 충분"
- Gemini §7.4: "P2 v3 는 시스템의 중장기적 채택 설계 문서이므로, 최신 안전 표준인 ADR-012 (Evidence Ledger Protection) 흡수는 본문의 무결성을 높이는 작업. 별도 PR 분리보다는 P2 v3 정식 채택 PR 내에서 cross-reference 완성 권장"
- Gemini §7.10 #2: "ADR-012 완전 통합 — §7 ADR 매트릭스에 ADR-012 정식 편입 + G4 §6 Hash Chain 메커니즘 *필수 참조 (Mandatory Reference)* 명시"

**판정**: **부분 충실** — 영구 권위 layer 는 *외부 ADR/G2/G3/G4 본문* 에 영구 존재 (ADR-012 / G4 / ADR-009 C-N / G2 §1.2.6 모두 정식 발행 / PASS 완료) 하나 *P2 v3 본문 답습* 0건 → archive 후 *권위 layer drift* 위험. C-14 응답 2건 cross-vendor 일치 권고 = *P2 v3 정식 채택 합의 내부* 흡수 작업으로 cross-reference 갱신 의무 (Gap-13 HIGH).

### 2.3 차원 3 — Hermes ≠ Root of Trust 원칙 유지

**평가**: **APPROVE WITH CONDITIONS** (영구 권위 layer 존재, P2 v3 본문 답습 의무 잔존)

**근거**:

영구 권위 layer (정식 발행 + 영구 권위):

| Layer | 권위 근거 | 본문 |
|---|---|---|
| Layer 1 | ADR-011 §2.3 영구 권위 | 권위 위계 + 5 운영 함의 |
| Layer 2 | ADR-012 §2.12 (Hermes 변조 차단 매트릭스 4항목) | (i) Hermes-originated ledger entry write 권한 0 / (ii) 파일 변조 read-only ACL / (iii) Hermes-originated commit auto-reject / (iv) 외부 LLM 응답 위조 차단 (`agent="user"` 강제) |
| Layer 3 | ADR-009 C-N §2.3 (Hermes PMO ↔ provider 분리) | Hermes PMO 격상 후에도 provider SDK 직접 import / 모델명 분기 / Provider 라우팅 결정 권한 부여 *영구 금지* |
| Layer 4 | G3 §1.3 + §5 (Evidence decision principle: PASS 성립 4 요건) | (i) Tools 검증 / (ii) Evidence Ledger entry / (iii) 사용자 명시 승인 / (iv) 합의 보고서 commit |
| Layer 5 | G3 §2.5 #11 / §4.5 / §2.2 #20 | filesystem read-only / audit log / Hermes-originated commit auto-reject |

P2 v3 §2.5 (활성화 후 책임) + §10 (영구 핵심 제약 #2 Hermes ≠ root of trust) + §2.1.2 (Hermes 가 *하지 않는* 것 6항목) 가 *부분 답습*. 단:

- §2.5 활성화 후 책임 본문에 ADR-009 C-N §2.3 (Hermes PMO 격상 후 provider 소유 차단) cross-reference 부재
- §5 운영 메커니즘 본문에 ADR-012 §2.12 매트릭스 4항목 cross-reference 부재
- §10 영구 핵심 제약 표에 5 layer 매트릭스 답습 부재

**P2 v3 정식 채택 후 *Hermes 가 자기 격상* 가능성 차단 매커니즘**:

| 차단 매커니즘 | 위치 | 강도 |
|---|---|---|
| Hermes-originated commit auto-reject | G3 §2.2 #20 + ADR-012 §2.12 #3 | **HIGH** (계산적 검증) |
| filesystem read-only on Constitution/ADR/SDD | G3 §2.5 #1 + ADR-012 §2.12 #2 | **HIGH** (계산적 검증) |
| 격상 절차 사용자 명시 commit 만 권위 | P2 v3 §2.6 단계 6 + system-identity-prequel §3.3 #2 | **HIGH** (절차적 강제) |
| 격상 전 인간 리뷰 의무 (Gemini §7.10 #3) | (현 부재 — 흡수 권고) | (강화 필요) |
| ADR-011 §2.4 T3 자동 정책 변경 절대 금지 | ADR-011 §2.4 + ADR-012 §2.7 (BLOCK + manual + chain_violation_detected) | **HIGH** (T3 영역) |

**판정**: 영구 권위 layer **HIGH** (5 layer 모두 정식 발행 + 영구 권위) — 단 P2 v3 본문 답습 cross-reference 흡수 시 *원칙 유지 강화*. C-1, C-2, C-5, C-12 흡수 후 **HIGH 5/5** (조건부 — 흡수 시).

### 2.4 차원 4 — Provider Liquidity 5-way Multi-layer Defense 보존

**평가**: **APPROVE WITH CONDITIONS** (영구 권위 layer 5/5, P2 v3 본문 답습 의무 잔존)

**근거**:

영구 권위 layer = 5-way Multi-layer Defense (ADR-009 C-N §5 + ADR-012 §원칙 5 + 6 정식 발행):

| Layer | 책임 영역 | 모법 / 답습 | 본 영역 정식 발행 |
|---|---|---|---|
| **Layer 1** | 코드 lock-in 차단 (모든 작성 주체 provider SDK 직접 import / 모델명 분기 차단) | ADR-009 C-N §2.2 (모법) + G2 GP-5 (depcruise 룰) + `llm-providers-design.md` §9 | ✅ ADR-009 C-N (2026-05-09 후속 4) + G2 PASS (2026-05-09) |
| **Layer 2** | Hermes-originated lock-in 변경 차단 | G3 §6.4 + ADR-009 C-N §2.3 | ✅ G3 PASS (2026-05-09) + ADR-009 C-N (2026-05-09 후속 4) |
| **Layer 3** | Skill 메타데이터 차원 (`provider_bindings` schema *required*/*exclusive* 금지) | G4 §3.5 | ✅ G4 PASS (2026-05-09) |
| **Layer 4** | Export format 차원 (JSONL Hermes 의존 0 + 최소 2 provider 재해석 가능) | G4 §4.3 + ADR-008 차단조건 #2 | ✅ G4 PASS (2026-05-09) |
| **Layer 5** | Evidence 형식 차원 (11 필드 모두 provider-neutral 강제) | ADR-012 §2.1 원칙 6 + G4 §4.2 | ✅ ADR-012 (2026-05-09) + G4 PASS (2026-05-09) |

**5 Layer 모두 정식 발행 + 영구 권위**. 본 합의 *Design Adoption only* 진입 시점 = **HIGH 5/5**.

**P2 v3 본문 답습 vs 영구 권위 layer 차이**:

- §1.6 (P1 과의 관계) — ADR-009 C-N §2 (P1 facade MVP 진입조건) cross-reference 부재
- §2.5 (활성화 후 책임) — ADR-009 C-N §2.3 (Hermes PMO ↔ provider 분리) cross-reference 부재
- §6 (G4 — Provider-agnostic Memory/Skill) — ADR-009 C-N §5 (Provider Liquidity 5-way Layer 1 모법) + ADR-012 §원칙 5 + 6 (Layer 5 추가) cross-reference 부재
- §10 (영구 핵심 제약 — Provider Liquidity) — 5-way Multi-layer Defense 명시 답습 부재

**archive 시 (P2 v2 / system-identity-prequel) 5-way Layer 약화 위험 평가**:

- P2 v2 archive → ADR-008 차단조건 #4 (P1 Facade 위임) 가 *원본 carry-over* 영역. 본 P2 v3 §8 carry-over 매핑이 *변경 없음* 으로 명시 → archive 시 권위 layer 보존 정합. ADR-009 C-N §9.4 cross-reference (P2 v3 §1.6 + §2.3 + §6 + §10) 흡수 시 *Layer 1 모법 ADR* 영구 권위 보존.
- system-identity-prequel archive → §4.2 G4 (Memory / Skill provider-agnostic) 본문 = G4 (`provider-agnostic-memory-skill-design.md`) 답습 흡수 완료. **5-way 권위는 ADR-009 C-N §5 + ADR-012 §원칙 5/6 영구 권위로 *system-identity-prequel 외부* 에 존재** → archive 후 *layer 약화 0*.

**잔여 위험**:
- P2 v3 §10 표에 *5-way 명시 답습 부재* → archive 후 후속 참조자 (에이전트 / 개발자) 가 *5-way* 명명을 ADR-012 §원칙 5 / ADR-009 C-N §5 까지 추적해야 인지 가능 → drift 위험 (LOW-MEDIUM, P2 v3 §10 본문 흡수 시 0).

**판정**: **APPROVE WITH CONDITIONS** — 영구 권위 layer = HIGH 5/5 (5 Layer 모두 정식 발행 + 영구 권위). C-7, C-8, C-9, C-11 흡수 시 P2 v3 본문 답습 강화 (Gap-9, Gap-10, Gap-12 통합).

### 2.5 차원 5 — 자동 정책 변경 (T3) 유발 위험

**평가**: **APPROVE** (T3 위반 위험 0, 영구 핵심 제약 보존 매커니즘 충실)

**근거**:

ADR-011 §2.4 T3 정의:
> Constitution / ADR / Harness Gates 정의 자체의 변경 = 자동 금지 (절대) + 사용자 명시 결정 + 단축 또는 풀 3+1 합의

본 합의 (P2 v3 정식 채택) = **T3 변경** (Hermes Adoption Design v3 = SDD/Harness Gates 정의 자체) → 자동 금지 + 사용자 명시 + 풀 3+1 합의 + 합의 보고서 commit 필수.

**P2 v3 §0.2 #6 (자동 정책 변경 절대 금지) + §11 변경 절차 + §12 메타 편향 자기진단** 모두 T3 답습.

**ADR-012 §2.7 (prev_hash 검증 실패 = BLOCK + manual + chain_violation_detected)** 답습 = T3 자동 변경 차단 매커니즘 정합. P2 v3 정식 채택 후 *후속 갱신* 시 동일 절차 답습.

**합의 형태 cross-vendor 일치** (Gemini §7.9 + C-14 1 §7.9):
- 풀 3+1 합의 권고 (단축 합의 비권고)
- C-14 응답 2건 반영
- 사용자 명시 승인
- Evidence Ledger entry (ADR-012 §3.1 답습 — `event: external_llm_received` + `agent="user"` 강제)
- adoption decision commit

**P2 v3 정식 채택 후 *후속 갱신* 시 T3 변경 절차 보존**:

| 후속 갱신 유형 | 절차 | T3 분류 |
|---|---|---|
| 단순 오타 / 문구 정리 | 사용자 단독 결정 가능 | T1 자동 / T2 (정정 후 검증) |
| §1 ~ §3 본문 갱신 | 사용자 명시 결정 | T2 |
| §4 / §5 / §6 본문 갱신 | 단축 합의 (Reviewer-only) | T2 |
| **DRAFT 상태 해제 → 정식 채택** | **단축 또는 풀 3+1 합의 APPROVE** (현 본 합의) | **T3** |
| §10 영구 핵심 제약 변경 | **풀 3+1 합의 + ADR Amendment 절차** | **T3** |

§11 표 명시 답습 정합. **자동 정책 변경 위험 0**.

**판정**: **APPROVE** — T3 위반 위험 0. 영구 핵심 제약 보존 매커니즘 충실. C-10 (합의 형태) + C-11 (§10 본문 강화) 흡수 시 *영구 핵심 제약 보존 강화*.

---

### 추가 차원 — 보안 Gap 식별 (사용자 명시 추가)

#### 차원 6.1 — C-14 11 핵심 조건 흡수 시 cross-reference drift / 권위 약화 위험

**C-14 응답 2건 11 핵심 조건 cross-vendor 일치/불일치 분석**:

| # | C-14 1 (Claude 인접) 조건 | Gemini 조건 | cross-vendor 일치 | 본 합의 흡수 권고 |
|---|---|---|---|---|
| 1 | §3 DRAFT Snapshot + Adoption-time Status 이중 구조 갱신 | #1 상태표 동기화 (2026-05-09 시점) | **일치** | C-3 (Gap-4 HIGH) |
| 2 | Design Adoption only 제한 + 4 의미 명시 | (§7.5 답습) | **일치 (간접)** | C-10 + C-11 |
| 3 | Hermes PMO non-activation clause 추가 | (§7.3 답습) | **일치 (간접)** | C-1 (Gap-2) |
| 4 | ADR-012 + G4 §4 보강 cross-reference 반영 | #2 ADR-012 완전 통합 + Mandatory Reference | **일치** | C-7, C-8, C-9 (Gap-8/9/10 HIGH) |
| 5 | 영구 핵심 제약 5건 보존 문구 강화 | #4 Archived 영구 제약 계승 검증 | **일치** | C-11 (Gap-12 HIGH) |
| 6 | Implementation Pending 표 명시 | (§7.5 답습) | **일치** | C-3 (Gap-4 통합) |
| 7 | 풀 3+1 합의 진행 (단축 합의 아님) | (§7.9 풀 3+1 권고) | **일치** | C-10 (Gap-11) |
| - | (없음) | #3 격상 전 인간 리뷰 의무화 | **Gemini 단독 강조** | C-12 (Gap-2 통합) |

**11 조건 cross-vendor 일치 7건 + Gemini 단독 1건** = 흡수 권고 8 항목 (C-1, C-3, C-7, C-8, C-9, C-10, C-11, C-12).

**cross-reference drift 위험**:
- 11 조건 모두 *P2 v3 본문 흡수* 권고 → P2 v3 본문 갱신 의무 8 항목 발생 → 본문 분량 증가 ~30% 예상 (현 652 줄 → ~850 줄)
- 본문 갱신 시 cross-reference 정합성 검증 의무 (P2 v3 §11 변경 절차 답습)
- archive 시점 (P2 v2 / system-identity-prequel) cross-reference 갱신 동시 의무

**권위 약화 위험**:
- P2 v3 정식 채택 = T3 변경 (영구 권위 발행) → 후속 갱신 시 풀 3+1 합의 + ADR Amendment 절차 의무 (§11 답습)
- 11 조건 *단일 PR 흡수* 가능 (C-14 1 §7.4 + Gemini §7.4 cross-vendor 일치) → 권위 약화 위험 0.

**판정**: **APPROVE WITH CONDITIONS** — 8 흡수 권고 의무. 단일 PR 흡수 시 권위 약화 0.

#### 차원 6.2 — 5 영구 핵심 제약 보존 매커니즘 (각 제약별 보호 layer 평가)

**1. Provider Liquidity (헌법 5조 관용)** — **HIGH 5/5**

| Layer | 보호 매커니즘 | 정식 발행 |
|---|---|---|
| Layer 1 | ADR-009 C-N §2.2 모법 + G2 GP-5 + `llm-providers-design.md` §9 (depcruise + AST 스캐너 + pre-commit hook) | ✅ |
| Layer 2 | G3 §6.4 + ADR-009 C-N §2.3 (Hermes-originated lock-in 변경 차단) | ✅ |
| Layer 3 | G4 §3.5 (`provider_bindings` schema *required*/*exclusive* 금지) | ✅ |
| Layer 4 | G4 §4.3 (JSONL Hermes 의존 0 + 최소 2 provider 재해석) | ✅ |
| Layer 5 | ADR-012 §원칙 6 + G4 §4.2 (11 필드 provider-neutral 강제) | ✅ |

**보존 평가**: **HIGH** — 5 Layer 모두 정식 발행 + ADR-009 C-N + ADR-012 영구 권위. archive 후 layer 약화 0.

**2. Hermes ≠ root of trust (ADR-011 §2.3 영구 권위)** — **HIGH (조건부 — 흡수 시)**

| Layer | 보호 매커니즘 | 정식 발행 |
|---|---|---|
| Layer 1 | ADR-011 §2.3 (영구 권위) | ✅ |
| Layer 2 | ADR-012 §2.12 (Hermes 변조 차단 매트릭스 4항목) | ✅ |
| Layer 3 | ADR-009 C-N §2.3 (Hermes PMO ↔ provider 분리) | ✅ |
| Layer 4 | G3 §1.3 + §5 (PASS 성립 4 요건) | ✅ |
| Layer 5 | G3 §2.5 #11 / §4.5 / §2.2 #20 (filesystem read-only / audit log / Hermes-originated commit auto-reject) | ✅ |

**보존 평가**: **HIGH (조건부)** — 5 layer 모두 정식 발행. P2 v3 §2.5 / §5 / §10 본문 답습 흡수 (C-2, C-5, C-12) 시 강화.

**3. 메타포 강제 금지 (system-identity-prequel §7)** — **HIGH (조건부 — archive 시 강화 필요)**

| Layer | 보호 매커니즘 | 정식 발행 |
|---|---|---|
| Layer 1 | system-identity-prequel §7 (현 권위) | ⏳ archive 예정 |
| Layer 2 | P2 v3 §10 영구 핵심 제약 (현 표 형식) | (현 P2 v3 본문) |
| Layer 3 | ADR-012 §1.5 메타포 회피 명시 | ✅ |
| Layer 4 | (Gemini §7.7 + C-14 1 §7.7 cross-vendor 일치) Normative Constraints 강제 규정 재선언 권고 | (흡수 권고) |

**보존 평가**: **HIGH (조건부)** — system-identity-prequel archive 시 §7 권위가 P2 v3 §10 + ADR-012 §1.5 로 영구 이전. 단 *Normative Constraints* 명시 격상 (C-11) 흡수 시 강화. 현 §10 표 형식이 *cross-vendor 일치 권고* 기준에서 *약화* 위험.

**4. 자동 정책 변경 금지 (T3, ADR-011 §2.4)** — **HIGH 5/5**

| Layer | 보호 매커니즘 | 정식 발행 |
|---|---|---|
| Layer 1 | ADR-011 §2.4 영구 권위 | ✅ |
| Layer 2 | ADR-012 §2.7 (prev_hash 검증 실패 = BLOCK + manual + chain_violation_detected) | ✅ |
| Layer 3 | G2 GP-6 + Layer 1~2 hook (설정 파일 변경 감지) + CI/nightly 강제 | ✅ |
| Layer 4 | G3 §2.2 #11 / #20 (T3 자동 reject) | ✅ |
| Layer 5 | P2 v3 §0.2 #6 + §11 변경 절차 + §12 자기진단 | (현 P2 v3) |

**보존 평가**: **HIGH** — 5 Layer 모두 정식 발행 + 영구 권위. archive 후 layer 약화 0. 본 합의 자체 = T3 변경 절차 (풀 3+1 + 사용자 명시 + 합의 보고서 commit) 정합.

**5. 수단/목적 분리 (ADR-011 §2.1 (a)~(d) + (e) 5조건)** — **HIGH**

| Layer | 보호 매커니즘 | 정식 발행 |
|---|---|---|
| Layer 1 | ADR-011 §2.1 영구 권위 | ✅ |
| Layer 2 | ADR-012 §4 ((a)~(e) 5조건 답습 + 비교표) | ✅ |
| Layer 3 | P2 v3 §3.3 / §4.3 / §5.4 / §6.4 (각 게이트 Exit 기준 (a)~(e) 패턴 답습) | ✅ |
| Layer 4 | R-2 ~ R-7 evidence chain | ✅ |
| Layer 5 | R-6 workflow 답습 확장 (자동 회귀 검증 경로) | ✅ |

**보존 평가**: **HIGH** — 5 Layer 모두 정식 발행 + 영구 권위. archive 후 layer 약화 0.

**5 영구 핵심 제약 종합 매트릭스**:

| 제약 | 영구 권위 layer | 보존 강도 | 흡수 권고 |
|---|---|---|---|
| Provider Liquidity | 5/5 정식 발행 | **HIGH** | C-7, C-8, C-9, C-11 |
| Hermes ≠ root of trust | 5/5 정식 발행 | **HIGH (조건부)** | C-1, C-2, C-5, C-12 |
| 메타포 강제 금지 | 4/4 + 흡수 권고 | **HIGH (조건부)** | C-11 (Normative Constraints 명시) |
| T3 자동 정책 변경 금지 | 5/5 정식 발행 | **HIGH** | (현 P2 v3 답습 충실) |
| 수단/목적 분리 | 5/5 정식 발행 | **HIGH** | (현 P2 v3 답습 충실) |

**종합**: **5 제약 = HIGH 5/5** (조건부 — 8 권고 흡수 시) — 본 합의 진입 차단 사유 *아님*.

#### 차원 6.3 — archive 결정 시 system-identity-prequel §3 / §6 / §7 의 P2 v3 흡수 정합성

**system-identity-prequel §3 (권위 위계)** → ADR-011 §2.3 영구 승격 완료 (2026-05-06). **archive 후에도 ADR-011 권위 영구 보존**.

**system-identity-prequel §6 (Evidence 기반 검증 원칙)** → P2 v3 §3.3 (G1b PASS) + §5 (G3) + ADR-012 (Evidence Ledger Protection) + G4 §4 영구 흡수. **archive 후에도 영구 권위 보존**.

**system-identity-prequel §6.3 (Evidence Ledger 최소 구현 MVP)** → ADR-012 §2.2 (11 필드 schema) + G4 §4.2 영구 권위화. **archive 후에도 영구 권위 보존**.

**system-identity-prequel §6.4 (Schema 고정 시점)** → ADR-012 §1.1 (Phase 1 종료 → 4 게이트 Design/Governance PASS + PR-1/PR-2 안정화 시점 재해석) 답습. **archive 후에도 영구 권위 보존**.

**system-identity-prequel §7 (메타포 강제 금지)** → P2 v3 §10 영구 핵심 제약 #3 + ADR-012 §1.5 메타포 회피 명시 답습. **archive 후 권위 layer = §10 + ADR-012 §1.5 = HIGH (조건부 — Normative Constraints 명시 격상 시 강화)**.

**판정**: archive 정합성 **HIGH** — §3 / §6 / §7 모두 영구 권위 layer 로 이전 완료. 단 §7 (메타포 금지) 의 P2 v3 §10 흡수가 *cross-vendor 일치 권고* 기준에서 *Normative Constraints 강제 규정 재선언* 으로 강화 권고 (C-11).

#### 차원 6.4 — ADR-008 부록 B Amendment 의 P2 v3 정식 채택 후 갱신 영역

ADR-008 부록 B Amendment (2026-05-06 발행, ADR-011 동시 발행) — Hermes 도입 결정 본문 + R-1 FAIL 후 갱신 사항 cross-reference. **본 합의 후 ADR-008 본문 자동 갱신 *금지* 답습** (C-14 1 §7.4 + Gemini §7.4 cross-vendor 일치 — 별도 PR).

**P2 v3 정식 채택 후 ADR-008 본문 갱신 후보** (별도 PR):
- 부록 B.5 차단조건 #1 충족 메커니즘 → P2 v3 §1.3 cross-reference (G1b PASS by SQLCipher trigger)
- §단계 마이그레이션 → P2 v3 §3.6 (현 활성화 상태) cross-reference
- (신규) §부록 C 후보 → P2 v3 §10 (영구 핵심 제약) + ADR-012 / ADR-009 C-N cross-reference

**ADR-011 §2.1 (a)~(d) + ADR-012 §4 답습 — Amendment 절차 영구 보존**:

| 절차 | 영구 권위 |
|---|---|
| 일반 원칙 (수단/목적 분리) | ADR-011 §2.1 본문 |
| Amendment specific 갱신 | ADR-008 부록 B (R1 specific) + ADR-009 C-N (P1 facade MVP specific) + ADR-011 §8 후속 작업 등록 |
| 자동 갱신 금지 | ADR-011 §2.4 T3 + 본 합의 §0.2 #3 답습 |

**판정**: ADR-008 부록 B Amendment 갱신 영역 = *P2 v3 정식 채택 후 별도 PR* — 본 합의 진입 차단 사유 *아님*.

#### 차원 6.5 — Hermes PMO 격상 *전* 인간 리뷰 의무화 (Gemini §7.10 #3 권고)

**Gemini §7.10 #3 cross-vendor 단독 강조**:
> Hermes PMO 실제 활성화 전, 최소 1회 이상의 *전문적인 인간 리뷰 (Human-in-the-loop)* 를 통한 거버넌스 최종 확인 명문화

**현 P2 v3 §2.6 격상 절차 7 단계**:
1. G1b PASS ✅ 2026-05-07
2. G2 PASS ⏳
3. G3 PASS ⏳
4. G4 PASS ⏳
5. 4 게이트 통합 검증 합의 (풀 3+1)
6. 사용자 명시 격상 결정
7. 격상 활성화 commit + ADR-008 본문 추가 갱신

**Gemini §7.10 #3 흡수 권고**:
- 단계 5.5 (신규 추가): 전문적인 인간 리뷰 (Human-in-the-loop) — 보안 / 거버넌스 specialist 1+ 최소 1회 거버넌스 최종 확인
- 단계 5 통합 검증 합의 + cross-vendor 외부 LLM 1+ 의견 + 인간 리뷰 = 3 layer 동시 충족 의무

**보안/거버넌스 정합성**:
- 1인 개발 + 단일 호스트 SPOF (G3 §5.5) 환경에서 자기참조 + 메타 편향 위험 *최종 통제 layer*
- ADR-012 §11.1 메타-순환 청산 4 매커니즘 (사후 외부 LLM 충족 / 격상 전 면제 / 합의 권위 내부 변경 / 자기 작성 한계 명시) 답습 강화
- C-14 응답 2건 cross-vendor 일치 풀 3+1 합의 + 외부 LLM 의견 + 사용자 명시 승인 + Evidence Ledger entry + adoption decision commit 답습 정합

**판정**: **HIGH 권고** — §11 변경 절차 또는 §2.6 격상 절차에 명문화 의무 (C-12, Gap-2 통합).

---

## 3. 식별된 Gap (Gap-N enumeration)

### 3.1 종합 Gap 매트릭스

| # | Gap | 영역 | 심각도 | 권고 처리 |
|---|---|---|---|---|
| **Gap-1** | §0.3 단계 4 archive 시점 영구 제약 보존 검증 매커니즘 명시 부재 | P2 v3 §0.3 + §10 | **LOW-MEDIUM** | §10 본문 강화 또는 archive commit 시점 *Normative Constraints* 명시 |
| **Gap-2** | §2 상단 Hermes PMO non-activation clause 강화 + §2.6 또는 §11 격상 전 인간 리뷰 의무 명문화 부재 | P2 v3 §2 + §2.6 + §11 | **HIGH** | C-1 + C-12 (cross-vendor 일치 + Gemini §7.10 #3 단독 강조) |
| **Gap-3** | §2.5 활성화 후 책임에 ADR-009 C-N §2.3 (Hermes PMO ↔ provider 분리) cross-reference 부재 | P2 v3 §2.5 | **MEDIUM** | C-2 (ADR-009 C-N §2.3 영구 권위 답습) |
| **Gap-4** | §3 4 게이트 진행 상태 표 = DRAFT 시점 (2026-05-07) — 현 시점 (2026-05-09 후속 5) 정합성 부재 + Implementation Pending 표 부재 | P2 v3 §3 | **HIGH** | C-3 (cross-vendor 일치 MUST UPDATE — DRAFT Snapshot + Adoption-time Status + Delta + Implementation Pending 표) |
| **Gap-5** | §4 본문에 P10 정식 등록 (2026-05-09 후속 5) + GP-1 Implementation/Runtime PASS / GP-2~GP-6 Design/Governance PASS + ADR-012 발행 cross-reference 부재 | P2 v3 §4 | **MEDIUM** | C-4 |
| **Gap-6** | §5.2 / §5.3 에 Hermes 변조 차단 매트릭스 4항목 (ADR-012 §2.12) + PASS 성립 4 요건 (G3 §5) cross-reference 부재 | P2 v3 §5 | **HIGH** | C-5 |
| **Gap-7** | §5.4 / §5.6 에 Design/Governance PASS 완료 흡수 + Implementation Pending 명시 부재 | P2 v3 §5 | **MEDIUM** | C-6 |
| **Gap-8** | §6 본문에 ADR-012 §2.2~§2.12 + §3.1~§3.5 + G4 §4.2/§4.4/§4.6 보강 cross-reference 부재 | P2 v3 §6 | **HIGH** | C-7 (cross-vendor 일치 ADR-012 완전 통합) |
| **Gap-9** | §6 또는 §10 에 Provider Liquidity 5-way Multi-layer Defense (Layer 1~5) 명시 답습 부재 | P2 v3 §6 + §10 | **HIGH** | C-8 (ADR-009 C-N §5 + ADR-012 §원칙 5/6 답습) |
| **Gap-10** | §7 ADR 매트릭스에 ADR-012 정식 편입 + ADR-009 C-N 갱신 4 항목 cross-reference 부재 | P2 v3 §7 | **HIGH** | C-9 (cross-vendor 일치 — Gemini §7.10 #2 Mandatory Reference) |
| **Gap-11** | 본 합의 형태 = 풀 3+1 + C-14 응답 2건 반영 + 외부 LLM cross-vendor 1+ + 사용자 명시 승인 + Evidence Ledger entry + adoption decision commit | 합의 형태 자체 | **HIGH** | C-10 (cross-vendor 일치 풀 3+1) |
| **Gap-12** | §10 영구 핵심 제약 표 → Normative Constraints 명시 격상 + Provider Liquidity 5-way 답습 + archive 후 보존 강화 문구 부재 | P2 v3 §10 | **HIGH** | C-11 (cross-vendor 일치 ENHANCEMENT REQUIRED) |
| **Gap-13** | DRAFT 시점 (2026-05-07) 본문 vs 현 시점 (2026-05-09 후속 5) 권위 layer 차이 — 6 영역 cross-reference 0건 (ADR-012 / G4 11 필드 / G4 hash chain / G4 round-trip / G2 P10 / ADR-009 C-N) | P2 v3 본문 종합 | **HIGH** | Gap-4/5/6/8/9/10 통합 — 단일 PR 흡수 가능 |
| **Gap-14** | §8 carry-over 매핑에 §2.2 (JSONL Export) ↔ G4 + §2.4 (P1 Facade 위임) ↔ ADR-009 C-N cross-reference 추가 권고 | P2 v3 §8 | **LOW** | (옵션) |
| **Gap-15** | 본 합의 자체가 *동일 Claude 패밀리 자기 작성 산출* — 외부 LLM 영역 cross-vendor 1+ 의견 의무 (C-14 cross-vendor 의뢰 1+ 답습) | 본 합의 형태 + ADR-012 §11.1 메타-순환 청산 답습 | **MEDIUM** | C-10 통합 — C-14 응답 2건 (Claude 인접 + Gemini cross-vendor) 으로 *부분* 충족 |

### 3.2 Gap 통합 정리 (중복 제거 후)

원 15건 → Gap-13 가 Gap-4/5/6/8/9/10 과 통합 → **유효 Gap 9건**.

심각도 분포:
- **HIGH 7건** (Gap-2, 4, 6, 8, 9, 10, 11, 12 — 8 별도 카운트, Gap-13 통합 후)
- **MEDIUM 3건** (Gap-3, 5, 7, 15 — 4 별도 카운트)
- **LOW-MEDIUM 1건** (Gap-1)
- **LOW 1건** (Gap-14)

### 3.3 본 합의 차단 사유 여부 종합

- **HIGH 7건** = P2 v3 본문 흡수 의무 *정식 채택 commit 전* (단일 PR 흡수 가능 — C-14 1 §7.4 + Gemini §7.4 cross-vendor 일치)
- **MEDIUM 3건** = P2 v3 본문 강화 권고 (정식 채택 시점 또는 후속)
- **LOW-MEDIUM / LOW 2건** = 후속 갱신 권고

**종합 판정**: 본 합의 진입 자체 차단 사유 *아님* — C-14 응답 2건 cross-vendor 일치 APPROVE WITH CONDITIONS 답습. 단 **Gap-4 (HIGH MUST UPDATE) + Gap-2 + Gap-6 + Gap-8 + Gap-9 + Gap-10 + Gap-11 + Gap-12 = 8 HIGH 항목** 의 *P2 v3 정식 채택 commit 전* 흡수 의무.

---

## 4. 권고 조건 (격상 통합 합의 또는 P2 v3 본문 갱신 시점 흡수)

### 4.1 본 합의 PASS 진입 권고 조건 (HIGH 8건 강조)

| # | 권고 | 근거 Gap | cross-vendor 일치 | 심각도 |
|---|---|---|---|---|
| **C-1** | §2 상단 PMO non-activation clause 강화 (구체 문구: "본 §2 의 정식 채택은 Hermes 에 추가 권한을 부여하지 않는다... Hermes PMO 격상은 4 게이트 Implementation/Runtime PASS 및 별도 사용자 승인 전까지 금지된다") | Gap-2 | **일치** (C-14 1 §7.3 + Gemini §7.10 #3) | **HIGH** |
| **C-3** | §3 이중 구조 갱신 — DRAFT Snapshot (2026-05-07) + Adoption-time Status (2026-05-09 이후) + Delta + Implementation Pending 표 (Hermes PMO activation = Not authorized 명시) | Gap-4 | **일치** (C-14 1 §7.2 + §7.5 + Gemini §7.2 + §7.5) | **HIGH** |
| **C-5** | §5.2 / §5.3 에 ADR-012 §2.12 Hermes 변조 차단 매트릭스 4항목 + G3 §5 PASS 성립 4 요건 cross-reference 흡수 | Gap-6 | (간접 — Gemini §7.10 #2 Mandatory Reference 답습) | **HIGH** |
| **C-7** | §6 본문에 ADR-012 §2.2~§2.12 + §3.1~§3.5 + G4 §4.2 11 필드 + §4.4 hash chain (Layer 1~5 + RFC 8785 JCS + Genesis Hash + prev_hash 검증 실패 BLOCK + Full Rewrite 5 Layer) + §4.6 round-trip Tier-based cross-reference 흡수 | Gap-8 | **일치** (C-14 1 §7.4 + Gemini §7.4 + §7.10 #2) | **HIGH** |
| **C-8** | §6 또는 §10 에 Provider Liquidity 5-way Multi-layer Defense (Layer 1 ADR-009 C-N §2.2 + Layer 2 G3 §6.4 + Layer 3 G4 §3.5 + Layer 4 G4 §4.3 + Layer 5 ADR-012 §원칙 6 + G4 §4.2) 명시 답습 흡수 | Gap-9 | (간접 — ADR-009 C-N §5 + ADR-012 §원칙 5 영구 권위 답습) | **HIGH** |
| **C-9** | §7 ADR 매트릭스에 ADR-012 정식 편입 (G4 hash chain Mandatory Reference 명시) + ADR-009 C-N 갱신 4 항목 (P2 v3 §1.6 + §2.3 + §6 + §10 cross-reference) | Gap-10 | **일치** (C-14 1 §7.4 + Gemini §7.4 + §7.10 #2) | **HIGH** |
| **C-10** | 본 합의 형태 = **풀 3+1 + C-14 응답 2건 반영 + 외부 LLM cross-vendor 1+ (이미 Gemini 사고모델 회수 완료) + Claude 인접 1건 + 사용자 명시 승인 + Evidence Ledger entry (`event: external_llm_received` + `agent="user"` 강제) + adoption decision commit** | Gap-11 + Gap-15 | **일치** (C-14 1 §7.9 + Gemini §7.9 cross-vendor 일치 풀 3+1 권고) | **HIGH** |
| **C-11** | §10 영구 핵심 제약 표 → (i) Normative Constraints 명시 격상 + (ii) Provider Liquidity 5-way 답습 + (iii) archive 후 보존 강화 문구 ("Archiving P2 v2 or system-identity-prequel does not weaken, supersede, or delete the five permanent constraints. If any archived document contains stronger wording, the stronger constraint remains preserved through ADR-011 / ADR-012 and this section.") + (iv) ADR-012 §9 5/5 HIGH 보호 매트릭스 cross-reference | Gap-12 | **일치** (C-14 1 §7.7 + Gemini §7.7 cross-vendor 일치 ENHANCEMENT REQUIRED) | **HIGH** |
| **C-12** | §11 변경 절차 또는 §2.6 격상 절차에 **격상 전 인간 리뷰 (Human-in-the-loop) 의무 명문화** ("Hermes PMO 실제 활성화 전, 최소 1회 이상의 전문적인 인간 리뷰를 통한 거버넌스 최종 확인") | Gap-2 통합 | **Gemini 단독 강조** (§7.10 #3) | **HIGH** |

### 4.2 보강 권고 (MEDIUM / LOW-MEDIUM / LOW Gap, 후속 흡수)

13. **C-2** (Gap-3 MEDIUM): §2.5 활성화 후 책임에 ADR-009 C-N §2.3 (Hermes PMO ↔ provider 분리 영구 권위) cross-reference 흡수
14. **C-4** (Gap-5 MEDIUM): §4 본문에 P10 정식 등록 (2026-05-09 후속 5) + GP-1 Implementation/Runtime PASS / GP-2~GP-6 Design/Governance PASS + ADR-012 발행 cross-reference 흡수
15. **C-6** (Gap-7 MEDIUM): §5.4 / §5.6 에 Design/Governance PASS 완료 흡수 + Implementation Pending 명시
16. **C-13** (Gap-1 LOW-MEDIUM): §0.3 단계 4 archive 시점 영구 제약 보존 검증 매커니즘 명시
17. **C-14** (Gap-14 LOW): §8 carry-over 매핑에 §2.2 ↔ G4 + §2.4 ↔ ADR-009 C-N cross-reference 추가

---

## 5. 영구 핵심 제약 5건 보호 점검

> 본 §5 는 사용자 명시 답습 5 제약을 본 합의 *진입 시점* + *정식 채택 시점* 에서 *영구 권위 layer 평가* + *archive 후 layer 약화 위험 평가* + *흡수 권고* 로 enumeration. 본 §5 자체는 *합의 보고서 입력* 까지 — P2 v3 본문 작성 권한 영역 *아님*.

### 5.1 Provider Liquidity (헌법 5조 관용)

**영구 권위 layer 5/5** (ADR-009 C-N §5 + ADR-012 §원칙 5/6 영구 권위 — 5 Layer 모두 정식 발행):

- Layer 1: ADR-009 C-N §2.2 (모법) + G2 GP-5 (depcruise) + `llm-providers-design.md` §9 (AST 스캐너 + pre-commit hook)
- Layer 2: G3 §6.4 + ADR-009 C-N §2.3 (Hermes-originated lock-in 변경 차단)
- Layer 3: G4 §3.5 (`provider_bindings` schema *required*/*exclusive* 금지)
- Layer 4: G4 §4.3 (JSONL Hermes 의존 0 + 최소 2 provider 재해석 가능)
- Layer 5: ADR-012 §원칙 6 + G4 §4.2 (11 필드 모두 provider-neutral 강제)

**P2 v3 본문 답습**: §1.6 / §2.5 / §6 / §10 cross-reference 흡수 권고 (C-7, C-8, C-9, C-11).

**archive 후 layer 약화 위험**: **0** — 5 Layer 모두 ADR-009 C-N + ADR-012 영구 권위 (system-identity-prequel + P2 v2 외부) 에 존재.

**보호 강도**: **HIGH**

### 5.2 Hermes ≠ root of trust (ADR-011 §2.3 영구 권위)

**영구 권위 layer 5/5** (ADR-011 §2.3 + ADR-012 §2.12 + ADR-009 C-N §2.3 + G3 §1.3/§5 + G3 §2.5 #11 / §4.5 / §2.2 #20 모두 정식 발행):

- Layer 1: ADR-011 §2.3 영구 권위 (system-identity-prequel §3 ADR 승격 답습)
- Layer 2: ADR-012 §2.12 Hermes 변조 차단 매트릭스 4항목 (Hermes-originated ledger entry / 파일 변조 / git commit / 외부 LLM 응답 위조)
- Layer 3: ADR-009 C-N §2.3 (Hermes PMO ↔ provider 분리 영구 권위)
- Layer 4: G3 §1.3 + §5 (Evidence decision principle: PASS 성립 4 요건)
- Layer 5: G3 §2.5 #11 / §4.5 / §2.2 #20 (filesystem read-only / audit log / Hermes-originated commit auto-reject)

**P2 v3 본문 답습**: §2.1.2 + §2.3 + §2.5 + §5.2 + §5.3 + §10 cross-reference 흡수 권고 (C-1, C-2, C-5, C-12).

**archive 후 layer 약화 위험**: **0** — 5 Layer 모두 ADR-011 + ADR-012 + ADR-009 C-N + G3 영구 권위 (system-identity-prequel + P2 v2 외부) 에 존재.

**보호 강도**: **HIGH (조건부 — C-1, C-2, C-5, C-12 흡수 시)**

### 5.3 메타포 강제 금지 (system-identity-prequel §7)

**영구 권위 layer 4/4** (system-identity-prequel archive 시 P2 v3 §10 + ADR-012 §1.5 로 영구 이전):

- Layer 1: system-identity-prequel §7 (현 권위 — archive 예정)
- Layer 2: P2 v3 §10 영구 핵심 제약 #3 (현 표 형식 — Normative Constraints 격상 권고)
- Layer 3: ADR-012 §1.5 메타포 회피 명시 + §3.3 (형식적 무결성 한계)
- Layer 4: (Gemini §7.7 + C-14 1 §7.7 cross-vendor 일치) Normative Constraints 강제 규정 재선언 권고

**P2 v3 본문 답습**: §10 본문 강화 권고 (C-11 — Normative Constraints 명시 + archive 후 보존 강화 문구).

**archive 후 layer 약화 위험**: **LOW (조건부)** — system-identity-prequel archive 시 §7 권위가 P2 v3 §10 + ADR-012 §1.5 로 영구 이전. 단 *Normative Constraints* 명시 격상 (C-11) 흡수 시 강화. 현 §10 표 형식이 *cross-vendor 일치 권고* 기준에서 *약화* 위험 — 흡수 시 0.

**보호 강도**: **HIGH (조건부 — C-11 흡수 시)**

### 5.4 자동 정책 변경 금지 (T3, ADR-011 §2.4)

**영구 권위 layer 5/5** (ADR-011 §2.4 + ADR-012 §2.7 + G2 GP-6 + G3 §2.2 #11/#20 + P2 v3 §0.2 #6 / §11 / §12 모두 정식 발행):

- Layer 1: ADR-011 §2.4 영구 권위 (T1/T2/T3 분류)
- Layer 2: ADR-012 §2.7 (prev_hash 검증 실패 = BLOCK + manual review + chain_violation_detected ledger entry)
- Layer 3: G2 GP-6 (자동 정책 변경 차단) + Layer 1~2 hook (설정 파일 변경 감지) + CI/nightly 강제
- Layer 4: G3 §2.2 #11 / #20 (T3 자동 reject)
- Layer 5: P2 v3 §0.2 #6 + §11 변경 절차 + §12 메타 편향 자기진단

**P2 v3 본문 답습**: §0.2 #6 + §11 + §12 = HIGH (현 본문 충실).

**archive 후 layer 약화 위험**: **0** — 5 Layer 모두 ADR-011 + ADR-012 + G2 + G3 + P2 v3 영구 권위 (system-identity-prequel + P2 v2 외부) 에 존재.

**본 합의 자체 = T3 변경 절차 정합**: 풀 3+1 + 사용자 명시 + 합의 보고서 commit + Evidence Ledger entry — Gap-11 (C-10) 흡수 시 정합.

**보호 강도**: **HIGH**

### 5.5 수단/목적 분리 (ADR-011 §2.1 (a)~(d) + (e) 5조건)

**영구 권위 layer 5/5** (ADR-011 §2.1 + ADR-012 §4 + P2 v3 §3.3 / §4.3 / §5.4 / §6.4 + R-2 ~ R-7 + R-6 workflow 모두 정식 발행):

- Layer 1: ADR-011 §2.1 영구 권위 ((a)~(d) 4조건)
- Layer 2: ADR-012 §4 ((a)~(e) 5조건 답습 + 비교표)
- Layer 3: P2 v3 §3.3 / §4.3 / §5.4 / §6.4 (각 게이트 Exit 기준 (a)~(e) 패턴 답습)
- Layer 4: R-2 ~ R-7 evidence chain
- Layer 5: R-6 workflow 답습 확장 (자동 회귀 검증 경로)

**P2 v3 본문 답습**: §3.3 + §4.3 + §5.4 + §6.4 = HIGH (현 본문 충실).

**archive 후 layer 약화 위험**: **0** — 5 Layer 모두 ADR-011 + ADR-012 + P2 v3 + Phase 0 evidence 영구 권위 (system-identity-prequel + P2 v2 외부) 에 존재.

**보호 강도**: **HIGH**

### 5.6 5 제약 종합 매트릭스

| 제약 | 영구 권위 layer | 본 합의 진입 시점 보호 강도 | 흡수 권고 흡수 후 |
|---|---|---|---|
| Provider Liquidity | 5/5 정식 발행 | **HIGH** | **HIGH** (C-7, C-8, C-9, C-11) |
| Hermes ≠ root of trust | 5/5 정식 발행 | **HIGH (조건부)** | **HIGH** (C-1, C-2, C-5, C-12) |
| 메타포 강제 금지 | 4/4 + 흡수 권고 | **HIGH (조건부)** | **HIGH** (C-11) |
| T3 자동 정책 변경 금지 | 5/5 정식 발행 | **HIGH** | **HIGH** (현 충실) |
| 수단/목적 분리 | 5/5 정식 발행 | **HIGH** | **HIGH** (현 충실) |

**종합**: **5 제약 = HIGH 5/5** (조건부 — 8 권고 흡수 시 *영구 핵심 제약 보호 강화 완결*) — 본 합의 진입 차단 사유 *아님*.

---

## 6. 본 입력이 *하지 않는* 것

- ❌ Hermes PMO 격상 자동 권유 (4 게이트 Implementation/Runtime PASS + 사용자 명시 결정 + 인간 리뷰 후 별도)
- ❌ Hermes Runtime Implementation PASS 자동 발화
- ❌ P2 v3 정식 채택 자동 발화 (Reviewer 종합 합의 + 사용자 명시 결정 영역)
- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012 본문 자동 갱신 권유 (cross-reference 권고 한정)
- ❌ G2 / G3 / G4 본문 자동 갱신 (Implementation/Runtime PASS 별도)
- ❌ P2 v2 / system-identity-prequel archive 자동 처리 발화 (정식 채택 시점에 별도 commit)
- ❌ P2 v3 본문 자동 갱신 (본 분석은 *Reviewer 종합 판정 입력* 한정)
- ❌ G2 §1.2 P10 추가 갱신 (이미 정식 등록 완료 — 2026-05-09 후속 5)
- ❌ Tier-1/2/3 catalog 자동 확장
- ❌ 다른 Agent (A, C) 출력 참조 (Phase 2 독립 분석 답습)
- ❌ Reviewer 종합 합의 결과 발화 (본 분석은 *Phase 2 독립 분석* 한정)
- ❌ 외부 LLM 의견 위조 또는 모방 (C-14 응답 2건 원문 답습)
- ❌ 본 분석 자체의 자기 검증 (자기참조 위험 통제는 C-14 응답 2건 + Reviewer 종합 영역, Gap-15)

---

## 7. 최종 판정

### 7.1 종합 판정

**APPROVE WITH CONDITIONS**

### 7.2 판정 근거

#### APPROVE 영역 (조건 없이 적격)

1. **Hermes PMO 격상과 P2 v3 정식 채택 분리 = 명료** — §0.2 #1 + §2 + §2.5 + §2.6 + §9.1 5 layer 분리 매커니즘 (cross-vendor 일치 — Gemini §7.8 + C-14 1 §7.8)
2. **Hermes ≠ root of trust 원칙 영구 권위 = 5/5 정식 발행** — ADR-011 §2.3 + ADR-012 §2.12 + ADR-009 C-N §2.3 + G3 §1.3/§5 + G3 §2.5/§4.5/§2.2
3. **Provider Liquidity 5-way Multi-layer Defense = 5/5 정식 발행** — ADR-009 C-N §5 + ADR-012 §원칙 5/6 + G2 GP-5 + G3 §6.4 + G4 §3.5/§4.2/§4.3
4. **자동 정책 변경 금지 (T3) = HIGH 5/5** — ADR-011 §2.4 + ADR-012 §2.7 + G2 GP-6 + G3 §2.2 + P2 v3 §0.2 #6 / §11 / §12
5. **수단/목적 분리 = HIGH** — ADR-011 §2.1 + ADR-012 §4 + P2 v3 §3.3/§4.3/§5.4/§6.4 (a)~(e) 패턴 + R-2 ~ R-7 + R-6
6. **메타포 강제 금지 = HIGH (조건부)** — system-identity-prequel §7 + P2 v3 §10 + ADR-012 §1.5 영구 이전 정합
7. **본 합의 형태 = T3 변경 절차 정합** — 풀 3+1 + 사용자 명시 + 합의 보고서 commit + Evidence Ledger entry (Gap-11 흡수 시)

#### CONDITIONS (정식 채택 commit 전 P2 v3 본문 갱신 또는 Reviewer 종합 합의 시점 흡수 권고)

**HIGH 8건** (C-14 응답 2건 cross-vendor 일치 흡수 권고):

1. **C-1 (Gap-2)**: §2 상단 PMO non-activation clause 강화
2. **C-3 (Gap-4)**: §3 이중 구조 갱신 (DRAFT Snapshot + Adoption-time Status + Delta + Implementation Pending 표)
3. **C-5 (Gap-6)**: §5 에 ADR-012 §2.12 Hermes 변조 차단 매트릭스 4항목 + G3 §5 PASS 성립 4 요건 cross-reference
4. **C-7 (Gap-8)**: §6 에 ADR-012 §2.2~§2.12 + §3.1~§3.5 + G4 §4.2/§4.4/§4.6 보강 cross-reference
5. **C-8 (Gap-9)**: §6 또는 §10 에 Provider Liquidity 5-way Multi-layer Defense 명시 답습
6. **C-9 (Gap-10)**: §7 ADR 매트릭스에 ADR-012 정식 편입 + ADR-009 C-N 갱신 4 항목 cross-reference
7. **C-10 (Gap-11)**: 본 합의 형태 = 풀 3+1 + C-14 응답 2건 반영 + 외부 LLM cross-vendor 1+ + Claude 인접 1건 + 사용자 명시 승인 + Evidence Ledger entry + adoption decision commit
8. **C-11 (Gap-12)**: §10 영구 핵심 제약 표 → Normative Constraints 명시 격상 + Provider Liquidity 5-way 답습 + archive 후 보존 강화 문구
9. **C-12 (Gap-2 통합)**: §11 또는 §2.6 격상 전 인간 리뷰 (Human-in-the-loop) 의무 명문화

**MEDIUM 3건**:

10. **C-2 (Gap-3)**: §2.5 활성화 후 책임에 ADR-009 C-N §2.3 cross-reference
11. **C-4 (Gap-5)**: §4 본문에 P10 정식 등록 + GP-1 Implementation PASS / GP-2~GP-6 Design PASS + ADR-012 발행 cross-reference
12. **C-6 (Gap-7)**: §5 본문에 Design/Governance PASS 완료 흡수 + Implementation Pending 명시

**LOW-MEDIUM / LOW 2건**:

13. **C-13 (Gap-1)**: §0.3 단계 4 archive 시점 영구 제약 보존 검증 매커니즘 명시
14. **C-14 (Gap-14)**: §8 carry-over 매핑에 §2.2 ↔ G4 + §2.4 ↔ ADR-009 C-N cross-reference 추가

### 7.3 본 판정의 *발화하지 않는* 것

- ❌ P2 v3 정식 채택 자동 발화 (Reviewer 종합 합의 + 사용자 명시 결정 영역)
- ❌ Hermes PMO 격상 자동 발화
- ❌ Hermes Runtime Implementation PASS 자동 발화
- ❌ P2 v3 본문 자동 갱신 (본 분석은 *Reviewer 종합 판정 입력* 한정)
- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012 본문 자동 갱신
- ❌ G2 / G3 / G4 본문 자동 갱신
- ❌ P2 v2 / system-identity-prequel archive 자동 처리
- ❌ G2 §1.2 P10 추가 갱신
- ❌ 실 hook / migration / runtime code 작성

본 판정은 **Reviewer 의 종합 합의 보고서 입력** 한정. 최종 합의 형태 + 외부 LLM 의견 형식 + P2 v3 본문 갱신 + archive commit 시점 결정은 **사용자 명시 결정 + Reviewer 종합 + 본문 작성 합의** 영역.

### 7.4 핵심 Gap 1줄 요약

**Gap-13 (HIGH 종합)**: P2 v3 본문 (2026-05-07 DRAFT) 6 영역 cross-reference 0건 (ADR-012 / G4 11 필드 / G4 hash chain Layer 1~5 / G4 round-trip Tier-based / G2 §1.2.6 P10 / ADR-009 C-N §5 Provider Liquidity 5-way) — 정식 채택 commit *전* 단일 PR 흡수 의무 (C-14 응답 2건 cross-vendor 일치 권고 답습) + §3 MUST UPDATE (DRAFT Snapshot + Adoption-time Status + Delta + Implementation Pending 표) + §10 Normative Constraints 격상 + §11 또는 §2.6 격상 전 인간 리뷰 의무 명문화.

---

**작성일**: 2026-05-09
**Agent B 판정**: **APPROVE WITH CONDITIONS** (12 CONDITIONS — C-1/C-3/C-5/C-7/C-8/C-9/C-10/C-11/C-12 HIGH 9건 + C-2/C-4/C-6 MEDIUM 3건 + C-13/C-14 LOW 2건 — 14 통합)
**다음 단계 (Agent B 권고)**: Reviewer 가 Agent A / C 출력 종합 + 본 판정 + 9 Gap (Gap-13 통합 후) + C-14 응답 2건 (Claude 인접 + Gemini cross-vendor) + Claude 인접 컨텍스트 + 사용자 명시 결정 — 본 합의 형태 = 풀 3+1 + 외부 LLM 2건 + 사용자 명시 승인 + Evidence Ledger entry + adoption decision commit (C-10 답습)
**금지 (본 분석 영구 답습)**:
- ❌ Hermes PMO 격상 자동 권유
- ❌ Hermes Runtime Implementation PASS 자동 발화
- ❌ P2 v3 정식 채택 자동 발화
- ❌ ADR / G2 / G3 / G4 / P2 v3 본문 자동 갱신
- ❌ P2 v2 / system-identity-prequel archive 자동 처리
- ❌ G2 §1.2 P10 추가 갱신
- ❌ Tier-1/2/3 catalog 자동 확장
- ❌ 실 runtime code / migration script 작성
- ❌ 다른 Agent (A, C) 출력 참조
