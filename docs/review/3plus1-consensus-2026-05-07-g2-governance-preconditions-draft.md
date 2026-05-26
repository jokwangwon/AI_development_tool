# 단축 검토 보고서 (Reviewer-only): G2 거버넌스 사전조건 DRAFT 채택 적격성

**날짜**: 2026-05-07
**검증 대상**: `docs/architecture/governance-preconditions.md` (DRAFT, commit `1b5bde3`)
**합의 형태**: 단축 검토 (Reviewer-only) — DRAFT 적격성 한정
**상위 권위**: ADR-011 §2.4 T2 (사용자 승인) + 본 세션 사용자 명시 옵션 1 결정 (G3/G4 진입 전 G2 DRAFT 적격 검토)
**관련 evidence**:
- P2 v3 DRAFT 단축 검토 결과 (commit `12d7609`, APPROVE AS DRAFT)
- P2 v3 DRAFT (commit `8f8e323`) §4 G2 정의
- 합의 §29~§30 (Agent B 6 거버넌스 사전조건 + 8 위반 경로 P1~P8 식별 — enumeration 없음)
- G1b PASS evidence (R-7 SOP §7.3 단축 합의, 2026-05-07)
**사용자 명시 결정**:
- 옵션 1 채택 — G3 작업 진입 전 G2 DRAFT 적격 검토
- DRAFT 적격이면 별도 commit 후 G3 진입
- G2 PASS / Hermes PMO 격상 / G3·G4 PASS / 정식 채택 자동 트리거 금지

---

## 1. 사전 점검 — 검토 가동 정당성

### 1.1 가동 사유

본 G2 초안은 다음 입력을 흡수한 신규 산출 (commit `1b5bde3`):
- 합의 §29~§30 Agent B 6 거버넌스 사전조건 + 8 위반 경로 P1~P8 식별 (enumeration 없음 → 본 초안에서 **최초 명시**)
- P2 v3 DRAFT §4 G2 정의 (entry/exit 기준 후보)
- ADR-011 §2.1 (a)~(d) 4조건 + ADR-011 §2.3 권위 위계 + ADR-011 §2.4 T1/T2/T3
- ADR-008 6 차단조건
- system-identity-prequel §3.3 / §4.2 G2 명시

본 초안은 *DRAFT 상태로 commit 완료* 상태이며, 본 검토는 *DRAFT 적격성*을 확인하여 G3 작업 진입 가능 여부를 판정. 검토 범위 한정:
- 사용자 명시 10 기준 충족 여부
- 금지 사항 위반 0건 확인
- DRAFT 상태 적격 + G3 진입 적격 여부

### 1.2 단축 검토 채택 사유

- 본 G2 초안 작업은 *evidence 흡수 + 사전조건 정의*이며 새 권위 결정 0건
- G2 PASS 합의는 본 검토 비대상 — 후속 PoC + (a)~(e) 충족 검증 후 별도 합의
- 직전 P2 v3 DRAFT 검토 (Reviewer-only, APPROVE AS DRAFT) 패턴 답습
- ADR-011 §2.4 T2 분류 (사용자 승인 기반 진행)

### 1.3 검토 비대상 (본 검토가 *판정하지 않는* 것)

- ❌ G2 PASS 적격성 — 6 GP 각각 (a)~(e) Exit 기준 충족 검증은 후속 PoC + 합의
- ❌ Hermes PMO 격상 적격성 — 4 게이트 통과 후 별도 결정
- ❌ G3 / G4 PASS 적격성 — 별도 작업 + 별도 합의
- ❌ P2 v3 정식 채택 적격성 — G2/G3/G4 완료 후 별도 합의
- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 갱신 적격성
- ❌ system-identity-prequel.md / P2 v2 archive 처리 적격성

---

## 2. 10 기준 점검 (사용자 명시)

### 2.1 기준 #1 — P2 v3 DRAFT와 충돌 여부

**확인 결과**: ✅ PASS (충돌 0건, *진화* 관계)

| 항목 | P2 v3 §4.2 (6 후보) | G2 초안 (6 GP 정식) | 관계 |
|------|------------------|----------------|------|
| #1 DB 평문 secret 차단 | 식별 | **GP-1** DB-level Secret Persistence | ✅ 진화 (GP-1으로 정식화) |
| #2 단일 Provider 의존 차단 | 식별 | (P1 v2 facade min 2 active 의존) | ⚠️ G2 GP에 직접 매핑 없음 — P1 위임 (ADR-008 차단조건 #5) |
| #3 Constitution/ADR/SDD 자동 변경 차단 | 식별 | **§9 메타 안전장치 + G3 위임** | ✅ 진화 (G3 §5.2 #5 위치 명시) |
| #4 OAuth 직결 사용 차단 (Phase 1) | 식별 | **GP-3** Credential Hygiene 일부 | ✅ 진화 (GP-3 P3 cover) |
| #5 Hermes 자체 SDK 직접 import 차단 | 식별 | **GP-5** Provider Adapter 강제 | ✅ 진화 (GP-5 P6 cover) |
| #6 자동 정책 변경 차단 (T3) | 식별 | **§9 메타 안전장치 + G3 위임** | ✅ 진화 (G3 §5.2 #5 위치 명시) |
| (신규) Egress Redaction (P2) | 미식별 | **GP-2** Egress Redaction | ⚠️ G2 신규 — P2 v3 §4.2 후보 외 |
| (신규) 외부 입력 검증 (P5) | 미식별 | **GP-4** 외부 입력 검증 | ⚠️ G2 신규 — P2 v3 §4.2 후보 외 |
| (신규) Memory/Skill Migration (P8) | 차단조건 #2 cross-ref | **GP-6** Migration | ✅ 진화 (G4와 공동 책임) |

**충돌 분석**:
- P2 v3 §4.2 자체에 "본 §4.2는 G2 *작성 트리거 후 정식 매핑* 대상이다. 본 초안에서는 식별 후보까지만 나열하며, 정식 매핑은 별도 산출 `docs/architecture/governance-preconditions.md`로 처리." 명시 → **G2 가 P2 v3 §4.2를 정식 매핑으로 대체**하는 것이 의도된 흐름
- P2 v3 #2 (단일 Provider 의존)는 G2 GP에 직접 매핑 없음. 그러나 P2 v3 §4.2 자체에 "P1 facade min 2 active 검증 (P1 §X)" 명시 — **P1 위임** 의도 명확. G2 신규 누락 아닌 *위임*.
- G2 신규 GP-2 / GP-4 는 P2 v3 §4.2 식별 후보 외 — **G2 정식화 시 추가**. 이는 진화이며 충돌 아님.

**잠재 cross-reference 갱신 필요**: P2 v3 §4.2가 G2 정식 채택 시점에 cross-reference 추가 권고 — 본 검토 **후속 권고 #1** 등록.

→ Criterion 1 PASS, 충돌 0건. 진화 관계.

### 2.2 기준 #2 — G1b PASS evidence 과장 흡수 여부

**확인 결과**: ✅ PASS (과장 0건)

본 초안 GP-1 (§3) 내 G1b 흡수 명시 위치:

| 위치 | 내용 | 과장 여부 |
|------|------|--------|
| §3.5 헤더 | "본 GP-1 은 **G1b PASS 의 직접 흡수** — Exit (a)~(e) 5조건이 G1b 승격 시점에 모두 충족된 상태. 본 §3.5 는 그 *증거 cross-reference* 만 명시." | ❌ 과장 없음 (직접 흡수 명시) |
| §3.5 (a)~(e) 표 | 각 조건의 G1b 승격 evidence cross-reference (R-4 / R-2 / R-4.1 / ADR-011 / R-6 / 합의 보고서) | ❌ 과장 없음 (사실 cross-reference) |
| §3.6 산출 후보 | "본 GP-1 은 G1b 흡수이므로 *추가 산출 0건*" | ❌ 과장 없음 (정직) |
| §10.2 G2 통합 Exit 표 | "GP-1 (a)~(e) 모두 G1b PASS evidence 로 충족 (§3.5) ✅ 본 초안 정식 채택 시 흡수 가능" | ❌ 과장 없음 ("정식 채택 시" → 본 초안 범위 외 명시) |
| §13.2 | "본 초안은 G2 PASS 판정을 *준비* 만 하며 *발생시키지 않는다*" | ❌ 과장 없음 |

**핵심**: GP-1 (a)~(e) 5조건이 *G1b 승격 시점에 충족된 상태*이지만, GP-1 *자체의 PASS 선언*은 본 초안 정식 채택 합의 시점으로 미뤄져 있음. *흡수 가능* ≠ *흡수 발생*. 정직.

→ Criterion 2 PASS, 과장 0건.

### 2.3 기준 #3 — GP-2~GP-6 PASS 아닌 entry/exit 기준 처리

**확인 결과**: ✅ PASS (PASS 자동 0건, entry/exit 기준만)

| GP | Entry 기준 처리 | Exit 기준 처리 | PASS 선언 여부 |
|----|------------|------------|----------|
| GP-2 | §4.4 ⏳ "사용자 명시 GP-2 작업 진입 결정" | §4.5 (a)~(e) 5조건 + 검증 방식 명시 | ❌ 미선언 |
| GP-3 | §5.4 ⏳ "사용자 명시 GP-3 작업 진입 결정" | §5.5 (a)~(e) 5조건 + 검증 방식 명시 | ❌ 미선언 |
| GP-4 | §6.4 ⏳ "사용자 명시 GP-4 작업 진입 결정" | §6.5 (a)~(e) 5조건 + 검증 방식 명시 | ❌ 미선언 |
| GP-5 | §7.4 ⏳ "사용자 명시 GP-5 작업 진입 결정" | §7.5 (a)~(e) 5조건 + 검증 방식 명시 | ❌ 미선언 |
| GP-6 | §8.4 ⏳ "사용자 명시 GP-6 작업 진입 결정 + G4 작업 병행" | §8.5 (a)~(e) 5조건 + 검증 방식 명시 | ❌ 미선언 |

§10.2 G2 통합 Exit 표:
- GP-2 ~ GP-6 모두 "(a)~(e) 미충족 — PoC + 합의 필요" + ⏳ 표기

→ Criterion 3 PASS, GP-2~GP-6 모두 entry/exit 기준만 처리, PASS 자동 0건.

### 2.4 기준 #4 — P1~P8 enumeration 적절성

**확인 결과**: ✅ PASS (적절, 단 §1.2.4 추가 후보 명시 권고)

§1.2 P1~P8 enumeration:

| # | 경로 | 헌법 8조 / Provider Liquidity 매핑 | 적절성 |
|---|------|------------------------------|------|
| P1 | DB INSERT 평문 secret | 8조 #1 #2 | ✅ R-1 FAIL evidence 직접 대응 |
| P2 | 로그/송신 평문 노출 | 8조 #2 | ✅ Hermes redaction docstring "for logs and tool output" 직접 대응 |
| P3 | Credential 파일 권한 노출 | 8조 #2 | ✅ ADR-008 §2.6.4 R1-2 직접 대응 |
| P4 | 비밀값 하드코딩 | 8조 #1 (직접) | ✅ 헌법 8조 #1 직접 대응 |
| P5 | 외부 입력 미검증 | 8조 #3 (직접) | ✅ 헌법 8조 #3 직접 대응 |
| P6 | Hermes SDK 직접 import | Provider Liquidity | ✅ ADR-008 차단조건 #4 직접 대응 |
| P7 | 모델명 / Provider 분기 | Provider Liquidity | ✅ ADR-008 §결과 §주의사항 6종 직접 대응 |
| P8 | Memory/Skill Hermes 종속 | Provider Liquidity | ✅ ADR-008 차단조건 #2 + G4 직접 대응 |

**합산**: 5+3=8 ✅ 합의 §29~§30 일치.

**Coverage 평가**:
- 헌법 8조 본문 4개 항 (#1 #2 #3 #4) 중 #4 ("보안 변경 3+1 합의")는 *절차* 영역으로 P-class enumeration 외 — 합리적
- Provider Liquidity 3개 측면 (코드 import / 분기 / Memory·Skill 형식) 적절히 분리

**잠재 누락 (자기 발견)**:
- *Hermes 학습 silent drift* — Hermes 자체 학습 결과가 redaction 정책을 silent 변경 → ADR-011 §2.4 T3 영역 → §1.2.4 "다루지 않음" 명시 + G3 위임
- *Hermes upstream silent breakage* — 의존성 업그레이드로 redaction 동작 silent 깨짐 → ADR-011 §2.3 운영 함의 #4 영역 → R-6 workflow가 다룸 → §1.2.4 명시 안됨 (잠재 보완)
- *Skill 권한 escalation* — Skill이 정의된 권한을 넘어 작동 → T1/T2/T3 분류 영역 → G3 위임 → §1.2.4 명시 안됨 (잠재 보완)

§1.2.4 현 명시:
- 헌법 1조 (SDD) / 2조 (TDD) / 4조 (3+1 합의) / 7조 (투명성) / 10조 (문서)
- ADR-011 §2.4 T3 자체 → G3 위임

§1.2.4 미명시 잠재 후보 (위 3건) — **본 검토 후속 권고 #2** 등록.

→ Criterion 4 PASS, P1~P8 적절. §1.2.4 추가 후보 (학습 silent drift / upstream breakage / Skill escalation) 명시 권고 (LOW, 정식 채택 시점에).

### 2.5 기준 #5 — 6 GP가 Hermes PMO 격상 전 거버넌스 사전조건으로 충분한가

**확인 결과**: ✅ PASS (제한적 충분 — 헌법 8조·5조 한정 + G3·G4 의존 명시)

**Coverage 검증** (P1~P8 → GP-1~GP-6):
- P1 → GP-1 ✅
- P2 → GP-2 ✅
- P3 → GP-3 ✅
- P4 → GP-3 ✅
- P5 → GP-4 ✅
- P6 → GP-5 ✅
- P7 → GP-5 ✅
- P8 → GP-6 ✅

→ 8/8 위반 경로가 6 GP에 매핑됨, coverage 완전.

**충분성 평가**:

| 측면 | G2 처리 | 충분성 |
|------|--------|------|
| 헌법 8조 (보안) | GP-1 ~ GP-4 | ✅ 충분 (5 P 모두 매핑) |
| Provider Liquidity (관용 5조) | GP-5 ~ GP-6 | ✅ 충분 (3 P 모두 매핑) |
| T3 변경 차단 자체 | §9 + G3 위임 | 🟡 *interface*까지 충분, 본격 운영은 G3 |
| 합의 결과 무결성 | §9 + G3 위임 | 🟡 G3 §5.5 (합의 인프라 순환 권위) |
| Memory boundary 강제 | GP-6 + G4 위임 | 🟡 G4 (Memory 형식 표준화) 의존 |
| Evidence Ledger 변조 방지 | (헌법 7조 영역, §1.2.4 명시 안됨) | ⚠️ G2 외, 헌법 7조 / 신규 ADR 영역 |

**충분성 결론**: 6 GP는 *헌법 8조·5조 위반 경로* coverage로 충분. 단, T3 자체 + 합의 무결성 + Memory boundary는 G3 / G4 위임으로 명시. Evidence Ledger 변조 방지는 헌법 7조 / 신규 ADR 영역으로 G2 범위 외 — *G2 PASS만으로는 Hermes PMO 격상 충분 조건 아님* 명시 (헤더 + §10.3).

**격상 충분 조건**: G1b ✅ + **G2 PASS** + **G3 PASS** + **G4 PASS** + 통합 합의 + 사용자 명시 결정. 본 G2 초안 자체는 G2 한정 충분, *4 게이트 통합 충분*은 G3/G4 통과 의존.

→ Criterion 5 PASS (헌법 8조·5조 한정 충분, G3·G4 의존 명시).

### 2.6 기준 #6 — 강제 메커니즘 분류 (계산적 / 추론적 보조 / 자동 롤백) 적절성

**확인 결과**: ✅ PASS (분류 적절)

§2.2 매트릭스 검증:

| GP | 계산적 | 추론적 보조 | 자동 롤백 | Reviewer 평가 |
|----|------|---------|--------|----------|
| GP-1 | ✅ Tier-1 42 trigger UDF + R-6 regex test | ⚠️ LLM sensitive content 감지 (G2 범위 외) | ✅ ROLLBACK trigger R1~R3 | ✅ 적절 (R-2 / R-4.1 / R-6 / R-7 evidence 실증) |
| GP-2 | ✅ test_redaction.py + base64 evasion (R2-6) | ⚠️ 보조 | ✅ ROLLBACK R5 | ✅ 적절 (Hermes native + P1 facade 이중 redaction) |
| GP-3 | ✅ gitleaks / detect-secrets / chmod check / entrypoint stat | ❌ 추론 불필요 | ✅ inotify 즉시 정지 + pre-commit reject | ✅ 적절 (정적 분석 + 권한 체크 충분) |
| GP-4 | ✅ schema validation + regex sanitizer + escape | ✅ Reviewer prompt injection 감지 | ✅ 검증 실패 BLOCK | ✅ 적절 (계산적 우선 + Reviewer 보조) |
| GP-5 | ✅ depcruise 정적 분석 + PR auto-reject | ❌ 추론 불필요 | ✅ depcruise FAIL CI 강제 | ✅ 적절 (정적 분석 단독 충분) |
| GP-6 | ✅ JSONL schema 검증 + 변환 스크립트 자동 테스트 | ⚠️ 다른 오케스트레이터 import 의미 보존 (부분 추론) | ✅ schema_version 호환 실패 export 차단 | ✅ 적절 (JSONL 표준 + 라운드트립 검증) |

**합산**: 6/6 계산적, 4/6 추론적 보조, 6/6 자동 롤백.

**원칙 답습**:
- CLAUDE.md "계산적 검증 우선" 답습 ✅
- ADR-011 §2.3 운영 함의 #1 ("Hermes 출력은 Tools로 검증") 답습 ✅
- 합의 §31 ("8 중 7 계산적 가능") 보다 본 6 GP는 **6/6 계산적 가능** — 사유: Path-level (P1~P8) → Enforcement-level (GP-1~GP-6) 추상화로 계산적 메커니즘 집계

**적절성 검증**:
- GP-3 추론적 ❌ 정확 (정적 분석 + 권한 체크는 결정적)
- GP-5 추론적 ❌ 정확 (depcruise는 정적)
- GP-4 추론적 ✅ 정당 (prompt injection 감지는 LLM 보조)
- GP-1 / GP-2 / GP-6 추론적 ⚠️ 정당 (보조 영역, G2 범위 외 명시)

→ Criterion 6 PASS, 분류 적절.

### 2.7 기준 #7 — G3 / G4 위임 범위 명확성

**확인 결과**: ✅ PASS (위임 명확)

**G3 위임 명시 위치**:

| 위치 | G3 위임 내용 | 명확성 |
|------|---------|------|
| §1.2.4 | "ADR-011 §2.4 T3 (자동 정책 변경) 위반 자체 — **G3** 범위" | ✅ 명시 |
| §9.2 메커니즘 #1 | "filesystem read-only on `governance-preconditions.md`" → G3 §5.2 #5 위치 | ✅ G3 §X 위치 명시 |
| §9.2 메커니즘 #2 | "본 문서 변경은 git commit으로만 권위 인정 (Hermes-originated commit auto-reject)" → G3 §5.5 (합의 인프라 순환 권위) | ✅ G3 §X 위치 명시 |
| §9.2 메커니즘 #3 | "Hermes-originated 변경 audit log" → G3 §5.2 #5 | ✅ G3 §X 위치 명시 |
| §9.2 메커니즘 #4 | "T3 변경 감지 hook + 자동 reject + 사용자 alert" → G3 §5.2 #5 | ✅ G3 §X 위치 명시 |
| §9.3 | "본 §9가 *하지 않는* 것 — G3 운영 구현 / 합의 인프라 순환 권위 해결 본문 / Hermes-originated commit 자동 reject 구현" | ✅ 명시 |
| §10.2 §9 표시 | "🟡 (interface 한정)" + "본격 운영 구현은 G3 범위" | ✅ 명시 |

**G4 위임 명시 위치**:

| 위치 | G4 위임 내용 | 명확성 |
|------|---------|------|
| §8.1 GP-6 정의 | "**G4** (Provider-agnostic Memory/Skill 형식) 와 *공동 책임*" | ✅ 명시 |
| §8.4 Entry | "G4 작업 진입 또는 병행 (본 §8 은 *마이그레이션 가능성* 측면, G4 는 *형식 표준화* 측면)" | ✅ 측면 분리 명시 |
| §8.7 신규 ADR | "ADR-014 (Provider-agnostic Memory/Skill Format) — G4 통합 시점" | ✅ 시점 명시 |

→ Criterion 7 PASS, G3 / G4 위임 모두 위치 + 측면 분리 명시.

### 2.8 기준 #8 — 영구 핵심 제약 5건 유지

**확인 결과**: ✅ PASS (5건 모두 명시)

§11 영구 핵심 제약 표:

| 제약 | 본 초안 §11 명시 | 권위 근거 인용 |
|------|--------------|---------|
| Provider Liquidity | ✅ | 헌법 5조 (관용) + `feedback_provider_liquidity.md` + ADR-008 본문 |
| Hermes ≠ root of trust | ✅ | ADR-011 §2.3 (영구 권위) |
| 메타포 강제 금지 | ✅ | system-identity-prequel §7 (P2 v3 §10 흡수) |
| 자동 정책 변경 금지 (T3) | ✅ | ADR-011 §2.4 |
| 수단/목적 분리 원칙 | ✅ | ADR-011 §2.1 (a)~(d) → 본 §3~§8 (a)~(e) 패턴 답습 |

**§9 메타 안전장치 — 추가 보호**:
- 본 5건 제약은 §9 메타 안전장치로 *추가* 보호 (Hermes 자기참조 차단)
- §9.4 #4: "본 §9 자체의 변경은 풀 3+1 합의 + ADR Amendment 절차 (T3 변경)"
- §12: §11 영구 핵심 제약 변경은 풀 3+1 합의 + ADR Amendment 절차 (T3 변경 — 매우 신중)

**삼중 보호**:
1. §11 본문 명시
2. §9 메타 안전장치 (자기참조 차단)
3. §12 변경 절차 (T3 영역 명시)

→ Criterion 8 PASS, 5건 모두 명시 + 삼중 보호.

### 2.9 기준 #9 — G2 PASS / Hermes PMO 격상 / P2 v3 정식 채택 암시 문구 부재

**확인 결과**: ✅ PASS (암시 문구 0건, 명시 부정 다수)

**명시 부정 위치 (헤더 + 본문 + 종료 부분)**:

| 위치 | 부정 문구 |
|------|---------|
| 헤더 첫 줄 | "**G2 PASS 선언은 본 초안 범위 외**" |
| §0.2 #1 | "❌ G2 PASS 선언" |
| §0.2 #2 | "❌ G3 / G4 PASS 선언" |
| §0.2 #3 | "❌ Hermes PMO 격상 선언" |
| §0.2 #4 | "❌ P2 v3 정식 채택 선언" |
| §0.3 단계 4 | "G2 PASS 합의 가동 (단축 또는 풀 3+1)" → 본 초안 범위 외 명시 |
| §3.5 헤더 | "본 §3.5 는 그 *증거 cross-reference* 만 명시" — *PASS 발생*이 아닌 *evidence 존재* 명시 |
| §10.2 표 GP-1 | "✅ 본 초안 정식 채택 시 흡수 가능" — *흡수 가능* ≠ *흡수 발생* |
| §10.2 G2 PASS 조건 | "GP-1 ~ GP-6 모든 (a)~(e) 충족 + §9 메타 안전장치 interface 명시 + G3 작업 동시 진입 (또는 G3 PASS 후) + 합의 보고서 APPROVE" — 미충족 조건 명시 |
| §10.3 | "본 G2 PASS 합의 APPROVE 시점에 발생: G2 status 갱신 / 본 문서 헤더 'DRAFT' 제거" — *합의 시점* = 본 초안 범위 외 |
| §10.3 | "발생하지 않는 것: G3/G4 자동 PASS / Hermes PMO 격상 자동 활성화 / P2 v3 정식 채택 자동 / archive 자동" |
| §13.2 | "본 초안은 G2 PASS 판정을 *준비* 만 하며 *발생시키지 않는다*" |
| 종료 줄 | "❌ G2 PASS 선언 자동 / G3 / G4 PASS 선언 자동 / Hermes PMO 격상 선언 자동 / P2 v3 정식 채택 자동 / ADR 본문 자동 갱신 / archive 자동 처리" |

**잠재 암시 검색** (Reviewer 자기 검토):
- "충족" 단어: §3.5 표 헤더 "충족 evidence" — 단어 "충족"은 *G1b 승격 시점에 (a)~(e) evidence가 존재함*의 의미, *GP-1 PASS 발생*이 아님. §10.2 G2 통합 Exit 표가 "✅ 본 초안 정식 채택 시 흡수 가능"으로 *발생 시점*을 본 초안 범위 외로 미룸. 정직.
- "PASS" 단어: G1b PASS / R-6 PASS 등 *기존 권위 결정* 인용에만 사용. *G2 PASS / GP-X PASS / Hermes PMO PASS* 인용 0건.

→ Criterion 9 PASS, 암시 0건, 명시 부정 13회.

### 2.10 기준 #10 — 후속 합의 검증 위험/누락 명시

**확인 결과**: ✅ PASS (메타 한계 명시 + 후속 검증 대상 식별)

**§13.1 메타 한계 명시**:

| 항목 | 명시 내용 |
|------|--------|
| 자기 작성 한계 | "본 초안은 *자기 작성 산출* (P2 v3 와 동일 컨텍스트). 외부 Reviewer 검토는 본 초안 대체 불가." |
| P1~P8 enumeration 권위 | "§1.2 P1~P8 enumeration 은 *최초 명시* — 합의 §29~§30 의 Agent B 원안은 enumeration 없음. 본 §1.2 가 P1~P8 의 *원안* 으로 권위화되려면 후속 합의 검증 필요." |
| 6 GP 매핑 권위 | "§2.1 6 GP 매핑은 본 초안 *원안* — 합의 §164 ('B의 6 거버넌스 사전조건 전건 채택')의 6 항목 enumeration 도 합의 보고서에 명시되지 않아, 본 §2.1 이 *6 항목의 원안*. 후속 합의에서 GP 분류 / 매핑 적정성 검증 대상." |

**§1.1 명명 정정 명시**:
- "후속 작업: 헌법 본문 갱신 또는 ADR Amendment 결정은 풀 3+1 합의 영역 (T3 변경 — ADR-011 §2.4)"

**§13.2 PASS 트리거 부재 명시**:
- 8건 명시 부정 (G2 PASS / Hermes PMO 격상 / G3·G4 PASS / ADR 갱신 / archive / INDEX·CONTEXT 갱신 / Phase 진입 / Tier-2·3 catalog)

→ Criterion 10 PASS, 메타 한계 + 후속 검증 대상 명시.

---

## 3. 추가 점검 항목 (Reviewer 자기 발견)

본 §3은 사용자 명시 10 기준 외 Reviewer가 자기 발견한 잠재 위험 항목.

### 3.1 P-1 — §1.2.4 추가 위반 경로 후보 명시 권고 (소프트 관찰)

**위치**: 본 초안 §1.2.4 ("본 §1.2가 다루지 않는 위반 경로")

**현 명시 비대상**:
- 헌법 1조 (SDD) / 2조 (TDD) / 4조 (3+1 합의) / 7조 (투명성) / 10조 (문서)
- ADR-011 §2.4 T3 자체 → G3 위임

**현 미명시 잠재 후보**:
- *Hermes 학습 silent drift* — Hermes 자체 학습 결과가 redaction 정책을 silent 변경 (ADR-011 §2.4 T3 영역, R-5 canary recheck design에서 다룸)
- *Hermes upstream silent breakage* — 의존성 업그레이드로 redaction 동작 silent 깨짐 (ADR-011 §2.3 운영 함의 #4 영역, R-6 workflow가 다룸)
- *Skill 권한 escalation* — Skill이 정의된 권한을 넘어 작동 (T1/T2/T3 분류 영역 → G3 위임)

**위험 등급**: 낮음 (LOW)
- 위 3건은 R-5 / R-6 / G3 가 다루므로 G2 GP에 enumerate되지 않아도 *cover됨*
- §1.2.4가 *명시적으로 다루지 않음* 형식이라 추가 후보 명시는 *완결성* 측면

**권고 처리**: BLOCK 사유 아님 / APPROVE WITH REVISIONS 의무 아님. **본 검토 후속 권고 #2** 등록 — 정식 채택 시점 또는 G3 작업 도중 §1.2.4에 위 3건 추가 명시.

### 3.2 P-2 — P2 v3 §4.2와의 cross-reference 갱신 권고 (소프트 관찰)

**위치**: P2 v3 DRAFT (`hermes-adoption-design-v3.md`) §4.2

**현 상태**:
- P2 v3 §4.2: "본 §4.2는 G2 *작성 트리거 후 정식 매핑* 대상이다. 본 초안에서는 식별 후보까지만 나열하며, 정식 매핑은 별도 산출 `docs/architecture/governance-preconditions.md`로 처리."
- G2 초안: P2 v3 §4.2 cross-reference 명시 (헤더 "**관련 설계**: `hermes-adoption-design-v3.md` §4")

**현 갭**:
- P2 v3 §4.2 6 후보 ↔ G2 6 GP 정식 매핑의 *항목별 매핑 표* 가 G2 초안 §2.1에 명시 안됨
- §1 본 검토 §2.1 에서 정리 — G2 초안 본문에 직접 흡수되지 않음

**위험 등급**: 낮음 (LOW)
- DRAFT 상태이며 *진화 관계*가 양 문서에 명시되어 있음
- 후속 검토자가 두 문서 비교 시 §2.1 표를 참조하면 reconciliation 가능

**권고 처리**: BLOCK 사유 아님 / **본 검토 후속 권고 #3** 등록 — G2 정식 채택 시점에 §2.1 또는 §1.5 carry-over에 P2 v3 §4.2 6 후보 매핑 표 추가.

### 3.3 P-3 — §1.1 명명 정정의 처리 권한 명시 (확인 사항)

**위치**: §1.1 "헌법 5조 (Provider Liquidity)" 명명 정정

**현 명시**:
- 프로젝트 관용 답습 + 1회 명시
- "후속 작업: 헌법 본문 갱신 또는 ADR Amendment 결정은 풀 3+1 합의 영역 (T3 변경 — ADR-011 §2.4)"

**관찰**:
- §1.1 이 *프로젝트 관용 답습*으로 결정 — 정당
- *근본 정정* (헌법 본문 갱신 또는 신규 ADR-012)은 T3 영역 명시 — 정당
- 그러나 *DRAFT 상태에서 명명 불일치 인지*가 *G2 PASS 합의 통과*를 차단하는지 여부는 명시되지 않음

**위험 등급**: 매우 낮음 (VERY LOW)
- §1.1은 *알림*이며 *차단*이 아님
- G2 PASS 합의는 *6 GP (a)~(e) 충족*에 의존, *명명 정정*에 의존 안 함

**권고 처리**: BLOCK 사유 아님 / 보존 권고. *명명 정정의 G2 PASS 차단 여부*는 G2 PASS 합의 보고서에서 결정 — 본 초안 범위 외.

### 3.4 P-4 — §10.2 옵션 3 ("G2/G3/G4 통합 풀 3+1") 권고 표현 (확인 사항)

**위치**: §10.2 G2 PASS 합의 형태:
> "**권고 형태** (사용자 결정 후보, 본 초안은 *권고 단정 금지*): 옵션 3 — G2/G3/G4 통합 풀 3+1 합의가 PR 묶음 + 메타 안전장치 (§9) 의 G3 의존성 감안 시 비용 효율적. 단, 옵션 1 / 2 도 사용자 결정 시 정당."

**관찰**:
- "권고 단정 금지" hedge 명시 ✅
- "옵션 1 / 2 도 정당" 명시 ✅
- P2 v3 DRAFT §9.2 "권고 옵션 A" 표현 패턴 답습 (P2 v3 검토 §3.1 P-1에서 후속 권고로 등록됨)

**위험 등급**: 낮음 (LOW), P2 v3 검토 §3.1 P-1과 동일 패턴

**권고 처리**: BLOCK 사유 아님 / 보존. P2 v3 검토 §3.1 P-1과 동일 사유로 *정식 채택 시점에 권고 표현 정밀화 검토*.

---

## 4. 금지 사항 위반 점검 (사용자 명시 답습)

| # | 금지 항목 | 본 초안 위반 여부 |
|---|---------|---------------|
| 1 | G2 PASS 선언 | ❌ 위반 0건 (§2.3 + §2.9 기준 점검 결과) |
| 2 | G3 / G4 PASS 자동 선언 | ❌ 위반 0건 (§2.7 G3/G4 위임 + §0.2 #2) |
| 3 | Hermes PMO 격상 선언 | ❌ 위반 0건 (헤더 + §0.2 #3 + §10.3 + 종료 줄 4회 명시 부정) |
| 4 | P2 v3 정식 채택 선언 | ❌ 위반 0건 (§0.2 #4 + §10.3 + 종료 줄 명시 부정) |
| 5 | ADR-008/009/010/011 본문 자동 갱신 | ❌ 위반 0건 (§0.2 #5 + §3.7 / §4.7 / §5.7 / §6.7 / §7.7 / §8.7 모두 "갱신 후보"로 명시) |
| 6 | P2 v2 archive 처리 | ❌ 위반 0건 (§0.2 #6) |
| 7 | system-identity-prequel archive 처리 | ❌ 위반 0건 (§0.2 #7) |
| 8 | 자동 정책 변경 (ADR-011 §2.4 T3) | ❌ 위반 0건 (§9 메타 안전장치 + §11 #4 + §12 T3 영역 명시) |
| 9 | 사전조건별 PoC 자동 실행 | ❌ 위반 0건 (§0.2 #9 + 각 GP §X.5 검증 방식 *기준*까지) |
| 10 | Tier-2 / Tier-3 catalog 확장 | ❌ 위반 0건 (§0.2 #10) |

→ 10/10 금지 항목 위반 0건.

---

## 5. 메타 편향 자기진단

**본 검토는 메타 편향 위험을 명시 인지한다**: Reviewer가 *본 초안을 작성한 동일 컨텍스트* — 자기 작성 산출 자기 검토. P2 v3 DRAFT 검토 + ADR-011 단축 합의 + G1b PASS 단축 합의에서 동일 위험 명시했으며 동일 5 통제 답습.

### 5.1 5 통제 답습

| # | 통제 수단 | 본 검토 적용 |
|---|---------|---------|
| 1 | 사용자 명시 절차 답습 | ✅ 사용자 명시 10 기준 §2 + 10 금지 항목 §4 + DRAFT 적격 검토 한정 |
| 2 | 직전 단축 합의 패턴 답습 | ✅ P2 v3 DRAFT 검토 §2/§3/§4/§5 구조 답습 |
| 3 | 10 항목 답습 + 10 금지 점검 | ✅ §2 10/10 + §4 10/10 점검 |
| 4 | 자기 발견 잠재 위험 명시 (§3 P-1 ~ P-4) | ✅ 4건 자기 발견, 모두 BLOCK 사유 아님으로 정직 분류 |
| 5 | 본 검토가 *하지 않는* 것 명시 (§1.3) | ✅ 6건 명시 비대상 |

### 5.2 본 검토의 한계

- 본 검토는 *자기 작성 산출 자기 검토* (P2 v3 / G2 모두 동일 컨텍스트). 외부 Reviewer 검토는 본 검토 대체 불가.
- 본 검토는 *DRAFT 적격성*만 판정. G2 PASS 적격성은 6 GP (a)~(e) 충족 검증 + 별도 합의.
- §3 자기 발견 잠재 위험 4건은 본 Reviewer 의 시야 한정 — 다른 Reviewer 시야에서 추가 발견 가능.
- 특히 *6 GP 분류 적정성* (P1~P8 → 6 GP 매핑)은 합의 §164 enumeration 부재로 본 초안이 *원안* — 후속 합의 검증 의무.

### 5.3 본 검토의 *PASS 판정이 트리거하지 않는 것*

본 §6 결론 PASS 판정은 다음을 *트리거하지 않는다*:

- ❌ G2 PASS
- ❌ Hermes PMO 격상
- ❌ G3 / G4 PASS 선언
- ❌ ADR-008/009/010/011 갱신
- ❌ P2 v2 / system-identity-prequel archive
- ❌ INDEX / CONTEXT 갱신
- ❌ Phase 진입 결정
- ❌ Tier-2 / Tier-3 catalog 확장
- ❌ G3 / G4 작업 자동 시작 (사용자 명시 결정 대기)

본 검토 PASS 판정은 *오직* "G2 거버넌스 사전조건 DRAFT 적격 + G3 작업 진입 적격" 의미.

---

## 6. 결론

### 6.1 판정

```
✅ APPROVE AS DRAFT
```

### 6.2 사유

- **10 기준 10/10 PASS** (§2.1 ~ §2.10) — P2 v3 충돌 0건 + G1b 과장 0건 + GP-2~GP-6 entry/exit 기준만 + P1~P8 적절 + 6 GP 충분 + 분류 적절 + G3/G4 위임 명확 + 영구 제약 5건 유지 + 암시 0건 + 메타 한계 명시
- **10 금지 항목 10/10 위반 0건** (§4)
- **자기 발견 잠재 위험 4건** (§3 P-1 ~ P-4) 모두 LOW/VERY LOW 등급 + BLOCK 사유 아님 + 정식 채택 또는 G3 작업 도중 흡수 가능
- **메타 편향 5 통제 답습** (§5.1)

### 6.3 후속 권고 (DRAFT 적격성과 *분리*)

본 결론은 DRAFT 적격성 판정 한정. 후속 작업 시 다음 표현 정밀화 권고 (선택):

| # | 권고 (선택) | 위치 | 처리 시점 |
|---|---------|-----|---------|
| 1 | P2 v3 §4.2 cross-reference 갱신 — G2 6 GP 정식 매핑 표 추가 | P2 v3 §4.2 또는 G2 §1.5 / §2.1 | G2 정식 채택 시점 |
| 2 | §1.2.4 추가 위반 경로 후보 명시 (학습 silent drift / upstream silent breakage / Skill 권한 escalation) | G2 §1.2.4 | G3 작업 도중 또는 G2 정식 채택 시점 |
| 3 | §10.2 옵션 3 권고 표현 정밀화 (P2 v3 §9.2 권고 옵션 A 후속 처리와 통합) | G2 §10.2 | G2 정식 채택 시점 |

본 권고 3건은 *G2 정식 채택 합의에 진입할 때* 또는 *G3 작업 도중* 함께 검토. 본 DRAFT 적격성 판정 단계에서는 처리 불필요.

### 6.4 G3 진입 적격성

본 G2 DRAFT 적격성 판정 결과 + 사용자 명시 옵션 1 ("G2 DRAFT 검토 APPROVE 시 G3 작업 진입") 답습 → **G3 작업 진입 적격**.

G3 작업 진입 시점에 본 G2 §9 메타 안전장치 + §10.2 메타 안전장치 *interface* → G3 §5.2 / §5.5 *본격 운영 구현* 의 위임 관계 답습.

### 6.5 본 검토 보고서 commit 절차

본 결론 APPROVE AS DRAFT에 따라 다음 단일 파일을 별도 commit으로 처리 가능:

```
docs/review/3plus1-consensus-2026-05-07-g2-governance-preconditions-draft.md
```

commit 메시지 (사용자 예시 답습):
```
docs(review): record G2 governance draft short review
```

본 commit에 포함하지 *않는* 항목 (사용자 명시 답습):
- G2 본문 갱신
- ADR-008/009/010/011 본문 갱신
- P2 v2 / system-identity-prequel archive 처리
- INDEX / CONTEXT 갱신
- Hermes PMO 격상 선언
- G2 / G3 / G4 PASS 선언

---

## 7. 다음 진입점 (본 검토 *이후*)

본 검토 PASS 후 사용자 명시 5단계 순서 답습:

| # | 단계 | 산출 | 시점 |
|---|------|------|------|
| 1 | G2 초안 Reviewer-only 단축 검토 | 본 보고서 | 본 단계 (완료) |
| 2 | 검토 보고서 별도 commit | `docs(review): record G2 governance draft short review` | 본 단계 직후 |
| 3 | G3 작업 시작 | `docs/architecture/hermes-not-root-of-trust-runtime.md` (DRAFT) | 사용자 명시 결정 후 |
| 4 | G4 작업 시작 | `docs/architecture/memory-scope-design.md` + `skill-format-design.md` (DRAFT) | G3 후 또는 병행 |
| 5 | G2/G3/G4 완료 후 P2 v3 정식 채택 합의 | 합의 보고서 + ADR PR 묶음 | G2/G3/G4 완료 후 |

본 검토 *이후* 금지 사항은 변동 없음 — §4 10 금지 항목 + 사용자 명시 답습.

---

**검토일**: 2026-05-07
**검토자**: Reviewer-only (메타 편향 자기진단 §5 명시)
**판정**: ✅ APPROVE AS DRAFT
**다음 단계**: 본 검토 보고서 별도 commit → G3 작업 시작 (사용자 명시 결정 후)
