# Implementation/Runtime PASS Roadmap MVP-1 Deepening 단축 합의 보고서 (Reviewer-only)

**합의 형태**: **단축 합의 (Reviewer-only)** — 사용자 명시 결정 답습 (2026-05-12 진입 명령 + 명확화 Q3 응답 = "본 작성 후 Reviewer-only 단축 합의 (권장)")
**합의 일자**: 2026-05-12 후속 (MVP-1 roadmap deepening 작성 commit/push 완료 후속)
**검토 대상**: `docs/architecture/implementation-runtime-roadmap-mvp1.md` (DRAFT, 630줄, 9 섹션, commit `cddd22f`)
**보조 참조**: `docs/architecture/implementation-runtime-roadmap.md` (전체 17 항목 source roadmap), `CLAUDE.md` §7+§8, `docs/CONTEXT.md`, `docs/INDEX.md` (commit `6c91980`)
**검토 목적**: MVP-1 roadmap 이 *DRAFT* 로 적격한지 + GP-3 / GP-5 MVP-1 진입 합의로 넘어갈 수 있는지 판단 한정
**판정**: ✅ **APPROVE AS DRAFT (단축 합의 — Reviewer-only) — MVP-1 roadmap DRAFT 권위 권고 발행 적격 + GP-3 / GP-5 MVP-1 진입 합의 진입 적격, 5/5 풀 3+1 승격 트리거 0건 발화, minor observations 2건 (DRAFT 적격성 영향 0건, GP-3/GP-5 진입 합의 시점 보강 권고)**

---

## 0. 사전 점검

### 0.1 가동 사유

사용자 명시 진입 명령 답습 (2026-05-12 두 번째 명령):

> "MVP-1 roadmap Reviewer-only 단축 합의를 진행해주세요. ... 이번 단계는 MVP-1 roadmap 자체가 다음 단계인 GP-3 / GP-5 MVP-1 진입 합의로 넘어갈 수 있을 만큼 적절한지 검토하는 것입니다."

**사용자 명시 결정 답습**:
- 검토 형태 = **Reviewer-only 단축 합의** (사용자 명시 Q3 응답 답습 + 본 진입 명령 답습)
- 검토 대상 = `docs/architecture/implementation-runtime-roadmap-mvp1.md` 한정
- 검토 목적 = **DRAFT 적격성 + GP-3/GP-5 MVP-1 진입 합의 진입 가능 여부** 한정
- 검토 기준 = 사용자 명시 12 항목 + 5 풀 3+1 승격 트리거 + 0/N 금지 사항
- 결론 형식 = APPROVE AS DRAFT / APPROVE WITH REVISIONS / BLOCK 中 1
- 본 합의 = **GP-3/GP-5 진입 승인 / 수단 확정 / Implementation Evidence PASS 선언 / Operational Readiness PASS 선언 / Hermes PMO 격상 선언 모두 *불가***

### 0.2 단축 채택 사유

| 조건 | 충족 |
|-----|------|
| 새 *권위 결정* 0건 (본 검토 = MVP-1 roadmap DRAFT 적격성 한정, GP-3/GP-5 진입 승인 / 수단 확정 / PASS 선언 0건) | ✅ |
| 직전 합의 (`3plus1-consensus-2026-05-09-implementation-runtime-roadmap.md` Reviewer-only) 패턴 답습 | ✅ |
| ADR-011 §2.4 T2 분류 (사용자 승인 기반 — DRAFT 발효 + 다음 단계 진입 적격성) | ✅ |
| 사용자 명시 결정으로 단축 합의 형태 채택 | ✅ §0.1 답습 |
| **5 풀 3+1 승격 트리거 발화 0건** | ✅ §2 답습 |

### 0.3 메타 편향 인지

본 Reviewer = Claude Opus 4.7 메인 컨텍스트 = `implementation-runtime-roadmap-mvp1.md` 작성자. 자기 작성 산출 자기 검토 한계 인지.

**청산 매커니즘**:

1. **사후 외부 LLM 충족** — 본 roadmap = 외부 LLM 응답 line 242 (MVP-1 정의) + 합의 보고서 §C-7 line 378 (4 입력 만장일치 합의 답습) 직접 답습. cross-vendor 외부 LLM 합산 4건 권위 *내부* 작업 (P2 v3 정식 채택 + ADR-012 발행 답습)
2. **격상 전 면제** — Hermes PMO 격상 *전*. 본 roadmap = MVP-1 = Implementation Evidence PASS Layer 2 1차 진입 *직전 의사결정 사전 정비* 한정
3. **합의 권위 내부 변경** — 본 검토 = `3plus1-consensus-2026-05-09-implementation-runtime-roadmap.md` (전체 17 항목 roadmap, Reviewer-only 단축 합의) 답습 = *권위 내부* 작업 (deepening)
4. **자기 작성 한계 명시** — 본 §0.3 + §3 명시

### 0.4 비검토 대상 (사용자 명시 답습)

| 항목 | 본 검토 범위 |
|-----|----------|
| GP-3 MVP-1 진입 승인 | ❌ (별도 합의 영역) |
| GP-5 MVP-1 진입 승인 | ❌ (별도 합의 영역) |
| 수단 S-1 / ST-3 / PC-3 / AR-1 확정 | ❌ (본 roadmap §3.2.2 / §3.3.2 / §4.3.2 / §4.4.2 *권고 한정* 답습) |
| 수단 T-6 / PC-3 / AR-1 확정 | ❌ (본 roadmap §4.2.3 *권고 한정* 답습) |
| Implementation Evidence PASS 선언 | ❌ |
| Operational Readiness PASS 선언 | ❌ |
| Hermes PMO 격상 선언 | ❌ |
| 실 runtime code / CI workflow 수정 / hook 구현 | ❌ |
| ADR 본문 자동 갱신 | ❌ (cross-reference 답습 한정) |
| Tier-2 / Tier-3 catalog 자동 확장 | ❌ |
| threshold *고정* | ❌ (FP/FN/latency 모두 *후보 한정* 답습) |

---

## 1. 12 검토 기준 평가 매트릭스 (사용자 명시 답습)

### 1.1 검토 기준 #1 — MVP-1 정의 정확성

| 검증 항목 | 본 roadmap 답습 | 충족 |
|----------|---------------|------|
| MVP-1 = G2 GP-3 (Credential / Secret Hygiene) | §1.1 표 1행 통합 정의 | ✅ |
| MVP-1 = G2 GP-5 (Provider Adapter Enforcement) | §1.1 표 1행 통합 정의 | ✅ |
| GP-2 = MVP-2 분리 | §1.3 분리 사유 명시 — 외부 LLM line 242 vs C-7 line 378 충돌 → C-7 답습 (3 사유: R-4/R-4.1 책임 분담 + 1인 부담 경감 + 시점 분리이지 영구 제외 아님) | ✅ |
| 답습 출처 명확 | §1.1 표 3 출처 (외부 LLM line 242 + C-7 line 378 + 본 §1.1 통합) | ✅ |

→ **4/4 충족** — MVP-1 정의 정확.

### 1.2 검토 기준 #2 — 3-layer PASS 분리 유지

| Layer | 본 roadmap 답습 | 충족 |
|-------|---------------|------|
| Layer 1: Design/Governance Gate PASS | §1.2 ASCII art Layer 1 명시 — 4 게이트 모두 PASS Bundled (2026-05-07 + 2026-05-09 후속) | ✅ |
| Layer 2: Implementation Evidence PASS | §1.2 ASCII art Layer 2 명시 — **MVP-1 = 본 layer 1차** 표기 | ✅ |
| Layer 3: Operational Readiness PASS | §1.2 ASCII art Layer 3 명시 — 본 문서 범위 외 (MVP-6 = PMO 격상 검토) | ✅ |

→ **3/3 충족** — 3-layer 분리 유지 + 외부 LLM 응답 §7.1 답습 충실.

### 1.3 검토 기준 #3 — MVP-1 = Implementation Evidence PASS Layer 2 첫 진입 표현

| 검증 항목 | 본 roadmap 답습 | 충족 |
|----------|---------------|------|
| ASCII art "Layer 2 ← MVP-1 = 본 layer 1차" 명시 | §1.2 (line 76 부근) | ✅ |
| §2.2 Exit 기준 = "Implementation Evidence PASS 진입 조건" 명시 | §2.2 본문 | ✅ |
| MVP-2 ~ MVP-5 = "본 PASS 단계" 표현 | §1.2 ASCII art 答습 | ✅ |

→ **3/3 충족** — Layer 2 첫 진입 표현 정확.

### 1.4 검토 기준 #4 — PoC vs MVP-1 차이 명확

| 영역 | PoC 영역 (본 roadmap §3.1.1 / §4.1.1) | MVP-1 영역 (본 roadmap §3.1.2 / §4.1.2) | 충족 |
|------|----------------------------------|-----------------------------------|------|
| GP-3 PoC 완료 | Group D 통합 PoC (2026-05-10, "형식적 검출 layer 시제") | gap 6건 (G3-1 저장 / G3-2 코드 / G3-3 PR auto-reject + G3-4/5/6 분리 영역) | ✅ |
| GP-5 PoC 완료 | Group A 1차/2차/3차 (Layer 1a/1b/1c 시제) | gap 7건 (G5-1 Layer 1 / G5-2 pre-commit / G5-3 branch protection + G5-4/5/6/7 분리 영역) | ✅ |
| PoC = "형식적 검출 layer 시제 한정" 명시 | CONTEXT.md 답습 + 본 roadmap §3.1.1 / §4.1.1 | 본 roadmap §3.1.2 / §4.1.2 = "PoC → Implementation Evidence PASS 사이의 *추가* 작업" | ✅ |

→ **3/3 충족** — PoC vs MVP-1 차이 명확.

### 1.5 검토 기준 #5 — GP-3 로드맵 구체성

| 사용자 명시 영역 | 본 roadmap 답습 | 충족 |
|----------------|---------------|------|
| secret source 관리 — `.env` | §3.2 코드 본문 secret 검출 (S-1 R-4.1 Tier-1 catalog ENV assignment regex H-A 답습 — `env_assignment.py` fixture 답습) | ✅ |
| secret source 관리 — Docker secret | §3.3.1 ST-3 단독 답습 (ADR-008 §2.6.2 R2-1 직접 답습) + §3.3.2 권고 ST-3 1차 채택 | ✅ |
| secret source 관리 — local config | §3.2 (Group D `safe_settings.json` PASS fixture + JSON field regex H-B 답습) | ✅ |
| secret source 관리 — CI secret | ⚠️ **명시적 sub-section 부재** — Group D PoC §1.2 #6 답습 (Hermes upstream + ADR-010 Vault HSM 분리 영역 명시), GP-3 §3.5 R-MVP1-G3-3 (ADR-008/ADR-010 본문 변경 trigger) 답습으로 *부분* 커버. 본 영역 = MVP-1 → MVP-2 (GP-2 송신 redaction) 또는 P11 (Enforcement Tool 자체 secret) 영역으로 분리 가능 | ⚠️ **부분 (Observation O-1)** |
| secret scanner 후보 | §3.2.1 5 수단 매트릭스 (S-1 custom / S-2 gitleaks / S-3 detect-secrets / S-4 trufflehog / S-5 병행) + §3.2.2 권고 (S-1 단독 + 1.5차 S-3 부분 통합 권고) | ✅ |
| rollback trigger | §3.5 Rollback Trigger 8 매트릭스 (R-1 + R-MVP1-G3-1~7) | ✅ |
| evidence 요구사항 | §3.6.1 Evidence Required 5 형식 (Markdown / JSONL ledger / Docker isolation log / GitHub Actions run / 합의 보고서) | ✅ |

→ **6/7 완전 충족 + 1/7 부분 (CI secret) — Observation O-1 (DRAFT 적격성 영향 0건, GP-3 진입 합의 시점 §3.1.2 gap 매트릭스에 G3-7 = CI secret 관리 추가 권고)**.

### 1.6 검토 기준 #6 — GP-5 로드맵 구체성

| 사용자 명시 영역 | 본 roadmap 답습 | 충족 |
|----------------|---------------|------|
| P1 facade 경유 강제 | §4.1.2 G5-4 = P1 v2 facade real 본문 분리 영역 명시 (`g2-gp5-poc2-import-linter-implementation.md` §8 TR-1 답습) | ✅ |
| direct provider SDK import 차단 | §4.2.2 책무 분담 매트릭스 (T-2 import-linter direct + from-import + transitive cover) + §4.2.3 권고 T-6 (T-2 + T-5 병행 PoC 채택 답습) | ✅ |
| dependency / import boundary 검사 | §4.2.1 T-2 (transitive 강점) + T-1 / T-3 / T-4 / T-5 후보 비교 매트릭스 + 책무 분담 §4.2.2 | ✅ |
| pre-commit 후보 | §4.3.1 4 수단 (PC-1 framework / PC-2 git native / PC-3 CI-only / PC-4 병행) + §4.3.2 권고 PC-3 1차 + 1.5차 PC-4 보강 | ✅ |
| PR auto-reject 후보 | §4.4.1 3 수단 (AR-1 CI step / AR-2 branch protection T3 / AR-3 통합) + §4.4.2 권고 AR-1 1차 + 1.5차 AR-3 보강 | ✅ |
| rollback trigger | §4.6 Rollback Trigger 10 매트릭스 (R-5 + R-9 + R-MVP1-G5-1~10) | ✅ |
| evidence 요구사항 | §4.7.1 Evidence Required 5 형식 (`g2-gp5-poc2-import-linter-implementation.md` §4 ledger entry 형식 답습) | ✅ |

→ **7/7 완전 충족** — GP-5 로드맵 구체성 충분.

### 1.7 검토 기준 #7 — GP-3 + GP-5 통합 위험 정리

| 사용자 명시 통합 위험 | 본 roadmap 답습 | 충족 |
|------------------|---------------|------|
| provider key가 adapter를 우회하는 경로 | ⚠️ **명시적 sub-section 부재** — GP-5 §4.1.2 G5-1 Layer 1 (adapter 우회 차단) + GP-3 §3.1.2 G3-2 (코드 본문 secret 검출) 결합으로 *부분* 커버. 단 *통합* 위험 명시 sub-section 부재 | ⚠️ 부분 |
| direct SDK import 와 secret leakage 결합 위험 | ⚠️ **명시적 sub-section 부재** — GP-5 위반 (`import openai`) + GP-3 위반 (`client = OpenAI(api_key="sk-...")`) 두 GP enforcement 결합으로 *부분* 커버. 단 *통합* sub-section 부재 | ⚠️ 부분 |
| local / CI / Docker secret handling 불일치 위험 | ⚠️ **명시적 sub-section 부재** — local (.env) + CI (GitHub secret 별도 영역 분리) + Docker (ST-3 답습) 일관성 명시 sub-section 부재 | ⚠️ 부분 |
| 통합 PASS 기준 + Rollback 통합 매트릭스 | §5.1 통합 PASS 기준 (ADR-011 5/5 양 GP 매트릭스) + §5.3 통합 Rollback Trigger 5 영역 (Tier-1 catalog 변경 / 도구 변경 / Hermes upstream + facade real 본문 / T3 영역 / FP-FN threshold) | ✅ (부분 커버) |
| Evidence Ledger 4 enum 통합 (`mvp1_gate_pass`) | §5.2 4 enum 후보 (마지막 = T3 통합) | ✅ |

→ **2/5 완전 충족 + 3/5 부분 (통합 위험 sub-section 부재) — Observation O-2 (DRAFT 적격성 영향 0건, GP-3/GP-5 진입 합의 시점 §5.4 통합 위험 sub-section 추가 권고. 본 영역 = §5 통합 PASS 기준 + 양 GP Rollback 답습으로 부분 커버 가능, 본 부재 = *치명적 결함 아님*)**.

### 1.8 검토 기준 #8 — 수단 후보 = 후보/권고 한정 유지

| 영역 | 본 roadmap 답습 | 충족 |
|------|---------------|------|
| GP-3 코드 본문 5 수단 | §3.2.2 "본 권고는 *수단 결정 아님*" 명시 | ✅ |
| GP-3 저장 5 수단 | §3.3.2 "본 권고는 *수단 결정 아님*" 명시 | ✅ |
| GP-5 Layer 1 6 수단 | §4.2.3 "본 권고는 *수단 결정 아님*" 명시 (T-6 = 현 PoC 답습 형태 권고) | ✅ |
| GP-5 pre-commit 4 수단 | §4.3.2 "본 권고는 *수단 결정 아님*" 명시 | ✅ |
| GP-5 PR auto-reject 3 수단 | §4.4.2 "본 권고는 *수단 결정 아님*" 명시 | ✅ |
| §0.2 미발생 #8 (수단 결정 0건) | §0.2 명시 | ✅ |
| §7.2 미발생 #8 (수단 결정 0건) | §7.2 명시 | ✅ |

→ **7/7 완전 충족** — 수단 후보/권고 한정 유지 + 5 sub-section + §0.2 + §7.2 三重 명시.

### 1.9 검토 기준 #9 — ADR-011 §2.1 (a)~(e) 매핑 충분성

| 조건 | 본 roadmap 답습 | 충족 |
|------|---------------|------|
| (a) 동등 이상의 보안 결과 | §5.1 표 양 GP 충족 방식 명시 (R-4.1 Tier-1 42 답습 + §9.3 답습) | ✅ |
| (b) 격리 환경 PoC 실증 | §5.1 표 양 GP (docker secret + chmod 644 시뮬레이션 + PR auto-reject 시뮬레이션 + facade single entry) | ✅ |
| (c) ADR / SDD 권위 명시 | §5.1 표 양 GP (ADR-008 §A.2 + ADR-010 + R-4 + GP-3 §5 + 본 §3 + ADR-008 #4 + ADR-009 C-N §5 + P1 v2 + GP-5 §7 + 본 §4) | ✅ |
| (d) 자동 회귀 검증 경로 확보 | §5.1 표 양 GP (secret-scan.yml + provider-adapter-enforcement.yml + provider-url-scanner + 매 PR + nightly) | ✅ |
| (e) 합의 APPROVE | §5.1 표 양 GP (단축 / 풀 3+1 분기 권고) | ✅ |
| §2.2 MVP-1 Exit = ADR-011 답습 명시 | §2.2 본문 표 | ✅ |
| §3.6.3 / §4.7.3 합의 형태 권고 답습 | 본 roadmap 양 GP 명시 | ✅ |

→ **7/7 완전 충족** — ADR-011 §2.1 (a)~(e) 매핑 충분.

### 1.10 검토 기준 #10 — Evidence Ledger enum 후보 적절성

| 후보 enum | 영역 | T1/T2/T3 | 본 roadmap 답습 | 충족 |
|----------|------|---------|---------------|------|
| `secret_scan_layer1_implementation` | GP-3 코드 본문 | T2 (CI step) | §5.2 #1 — Group D PoC §11 evidence summary 답습 | ✅ |
| `secret_storage_isolation_implementation` | GP-3 저장 경로 | T2 (Hermes upstream sidecar) | §5.2 #2 — ADR-008 §A.2 R1-2 답습 | ✅ |
| `provider_adapter_enforcement_layer1_static` | GP-5 Layer 1a/1b/1c 통합 | T2 (CI step) | §5.2 #3 — `g2-gp5-poc2-import-linter-implementation.md` §4 ledger entry 직접 답습 | ✅ |
| `mvp1_gate_pass` | MVP-1 = GP-3 + GP-5 양쪽 PASS | T3 (사용자 명시 + ADR-011 §2.1 5/5 evidence) | §5.2 #4 — 통합 enum | ✅ |
| 본 4 enum = *후보 한정* 명시 (정식 등록 = 별도 합의) | §5.2 본문 + ADR-012 §2.2 답습 + G4 §10.2 schema 진화 정책 답습 | ✅ |
| §0.2 + §7.2 미발생 #14 (`event` enum 정식 등록 0건) | 양쪽 명시 | ✅ |

→ **6/6 완전 충족** — Evidence Ledger 4 enum 후보 적절 + 후보 한정 명시.

### 1.11 검토 기준 #11 — MVP-1 → MVP-2 진입 조건 명확성

| 검증 항목 | 본 roadmap 답습 | 충족 |
|----------|---------------|------|
| §6.1 5 조건 매트릭스 | (1) GP-3 Implementation Evidence PASS / (2) GP-5 Implementation Evidence PASS / (3) Evidence Ledger 4 enum 등록 / (4) MVP-2 영역 진입 권고 합의 / (5) 사용자 명시 결정 | ✅ |
| §6.2 MVP-2 영역 미리 보기 | GP-2 + G4 §4.4 Layer 4 (C-7 line 379 답습) | ✅ |
| §6.2 MVP-2 본문 deepening = 본 문서 범위 외 명시 | §6.2 마지막 줄 + §0.2 미발생 #11 + §7.2 미발생 #11 | ✅ |

→ **3/3 완전 충족** — MVP-1 → MVP-2 진입 조건 명확.

### 1.12 검토 기준 #12 — 0/N 금지 사항 준수

| # | 금지 영역 | 본 roadmap 위반 | 본 검토 위반 |
|---|---------|-------------|-----------|
| 1 | 실 runtime code 구현 | 0건 (§0.2 + §7.2 명시) | 0건 |
| 2 | CI workflow 수정 / hook 구현 | 0건 (§0.2 + §7.2 명시) | 0건 |
| 3 | Hermes PMO 격상 선언 | 0건 (§0.2 + §7.2 명시) | 0건 |
| 4 | Operational Readiness PASS 선언 | 0건 (§0.2 + §7.2 명시) | 0건 |
| 5 | Implementation/Runtime PASS 자동 선언 | 0건 (§0.2 + §7.2 명시) | 0건 |
| 6 | G2 / G3 / G4 일괄 PASS 선언 | 0건 (§0.2 + §7.2 명시) | 0건 |
| 7 | ADR 본문 자동 갱신 | 0건 (§0.2 + §7.2 명시 — cross-reference 답습 한정) | 0건 |
| 8 | 수단 *결정* | 0건 (5 sub-section "수단 결정 아님" + §0.2 + §7.2 명시) | 0건 |
| 9 | Tier-2 / Tier-3 catalog 자동 확장 | 0건 (§0.2 + §7.2 명시) | 0건 |
| 10 | threshold *고정* | 0건 (§3.4 + §4.5 모두 "후보 한정" + §0.2 + §7.2 명시) | 0건 |
| 11 | MVP-2 ~ MVP-6 본문 deepening | 0건 (§6.2 권고 한정 + §0.2 + §7.2 명시) | 0건 |
| 12 | 17 항목 우선순위 자동 *재고정* | 0건 (`implementation-runtime-roadmap.md` §5.1 답습 + §0.2 + §7.2 명시) | 0건 |
| 13 | 신규 ADR / 신규 P / 신규 GP 발행 | 0건 (§7.2 명시) | 0건 |
| 14 | ADR-012 §2.2 `event` enum 정식 등록 | 0건 (4 enum 후보 = 후보 한정 §5.2 + §7.2 명시) | 0건 |
| 15 | 외부 LLM 자동 호출 | 0건 (§7.2 명시) | 0건 |
| 16 | 실 API key / provider SDK / 외부 API 호출 | 0건 (§7.2 명시) | 0건 |

→ **16/16 완전 준수** — 본 roadmap + 본 검토 모두 0/N 위반.

### 1.13 12 검토 기준 종합

| # | 기준 | 평가 | Observation |
|---|------|------|----------|
| 1 | MVP-1 정의 정확성 | ✅ 완전 충족 (4/4) | — |
| 2 | 3-layer PASS 분리 유지 | ✅ 완전 충족 (3/3) | — |
| 3 | MVP-1 = Implementation Evidence PASS Layer 2 1차 | ✅ 완전 충족 (3/3) | — |
| 4 | PoC vs MVP-1 차이 명확 | ✅ 완전 충족 (3/3) | — |
| 5 | GP-3 로드맵 구체성 | ⚠️ 6/7 충족 + 1 부분 | **O-1**: CI secret 관리 sub-section 부재, GP-3 진입 합의 시점 G3-7 추가 권고 |
| 6 | GP-5 로드맵 구체성 | ✅ 완전 충족 (7/7) | — |
| 7 | GP-3 + GP-5 통합 위험 | ⚠️ 2/5 충족 + 3 부분 | **O-2**: 통합 위험 sub-section 부재, GP-3/GP-5 진입 합의 시점 §5.4 추가 권고 |
| 8 | 수단 후보 = 후보/권고 한정 | ✅ 완전 충족 (7/7) | — |
| 9 | ADR-011 §2.1 (a)~(e) 매핑 | ✅ 완전 충족 (7/7) | — |
| 10 | Evidence Ledger enum 후보 적절성 | ✅ 완전 충족 (6/6) | — |
| 11 | MVP-1 → MVP-2 진입 조건 명확성 | ✅ 완전 충족 (3/3) | — |
| 12 | 0/N 금지 사항 준수 | ✅ 완전 준수 (16/16) | — |

**합산: 10/12 완전 충족 + 2/12 부분 충족 (Observation O-1, O-2). DRAFT 적격성 영향 0건 — 모두 GP-3/GP-5 진입 합의 시점 보강 적격 (별도 영역 분리로 부분 커버 가능, 치명적 결함 아님).**

---

## 2. 5 풀 3+1 승격 트리거 검증 (사용자 명시 답습)

| # | 트리거 | 본 검토 | 발화 |
|---|----|----|----|
| 1 | **MVP-1 정의 자체 변경** (GP-3 + GP-5 외 항목 추가/제거) | 본 roadmap §1.1 = 외부 LLM line 242 + C-7 line 378 직접 답습, 변경 0건 | ❌ 0 |
| 2 | **3-layer PASS 분리 의미 변경** (Design Gate / Implementation Evidence / Operational Readiness) | 본 roadmap §1.2 = 외부 LLM 응답 §7.1 직접 답습, 변경 0건 | ❌ 0 |
| 3 | **수단 *결정* 발생** (S-1 / T-6 / PC-3 / AR-1 등 채택 결정) | 본 roadmap = *권고 한정* 5 sub-section 三重 명시 (§3.2.2 / §3.3.2 / §4.2.3 / §4.3.2 / §4.4.2) + §0.2 + §7.2 명시. 결정 0건 | ❌ 0 |
| 4 | **5 영구 핵심 제약 약화 가능성** | 본 roadmap = 5 제약 직접 답습 (Provider Liquidity 5-way / Hermes ≠ root of trust 5 layer / 메타포 강제 금지 / T3 / 수단/목적 분리). §3 + §4 도구 후보 비교 = 5 제약 직접 답습 (예: T-6 = facade single entry 강화 / S-1 = R-4.1 catalog 답습). 약화 0건 | ❌ 0 |
| 5 | **ADR-011 §2.1 (a)~(e) 조건 충돌** | 본 roadmap §5.1 = ADR-011 §2.1 (a)~(e) 5조건 양 GP 매트릭스 직접 답습, 충돌 0건 | ❌ 0 |

→ **5/5 트리거 0건 발화** → **단축 합의 (Reviewer-only) 적격** 확정.

**Observation O-1, O-2 가 트리거 발화 영역인가 검토**:
- O-1 (CI secret 관리 부재) = MVP-1 정의 변경 아님 (GP-3 §3.1.2 gap 매트릭스 보강 영역, 5 제약 약화 0건)
- O-2 (통합 위험 sub-section 부재) = MVP-1 정의 변경 아님 (§5 통합 PASS 기준 + 양 GP Rollback 답습으로 부분 커버, 5 제약 약화 0건)
- 두 Observation = *DRAFT 발효 후 보강 권고* 한정 — **트리거 발화 영역 아님**.

---

## 3. 메타 편향 자기진단

### 3.1 본 검토자의 컨텍스트 한계

본 Reviewer = Claude Opus 4.7 메인 컨텍스트 = `implementation-runtime-roadmap-mvp1.md` 작성자와 동일 컨텍스트. 자기 작성 산출 자기 검토 한계 인지.

### 3.2 본 한계의 청산

| # | 청산 원칙 | 본 검토 적용 |
|---|-------|--------|
| 1 | 사후 외부 LLM 충족 | 본 roadmap = 외부 LLM line 242 + C-7 line 378 (4 입력 만장일치 합의 답습) 직접 답습 = cross-vendor 외부 LLM 합산 4건 권위 *내부* 작업 |
| 2 | 격상 전 면제 | Hermes PMO 격상 *전* — 본 roadmap = MVP-1 = Implementation Evidence PASS Layer 2 1차 진입 *직전* 의사결정 사전 정비 한정 |
| 3 | 합의 권위 내부 변경 | 본 검토 = `3plus1-consensus-2026-05-09-implementation-runtime-roadmap.md` (전체 17 항목 roadmap, Reviewer-only 단축 합의) 답습 = *권위 내부* 작업 (deepening) |
| 4 | 자기 작성 한계 명시 | 본 §0.3 + §3 명시 |

### 3.3 5 통제 답습

| # | 통제 | 본 검토 |
|---|-----|--------|
| 1 | 사용자 명시 절차 답습 | ✅ 사용자 명시 작업명 + 검토 형태 + 검토 대상 + 검토 목적 + 12 검토 기준 + 결론 형식 + 금지 사항 모두 §0 + §1 + §2 + §4 답습 |
| 2 | R-7 SOP §0 핵심 선언 답습 | ✅ §0.4 비검토 대상 + §1 12 평가 + §2 5 트리거 |
| 3 | ADR-011 §2.4 T1/T2/T3 답습 | ✅ §1.7 (`mvp1_gate_pass` enum = T3) + §1.8 (수단 결정 = T2/T3 영역, 본 roadmap = 권고 한정 답습) |
| 4 | 수단/목적 분리 원칙 답습 | ✅ §1.9 (ADR-011 §2.1 (a)~(e) 5조건 직접 답습) + §1.5 ~ §1.7 (수단 후보 = *목적* (Provider Liquidity / Credential Hygiene) 보호 위한 *수단 후보 비교* 답습) |
| 5 | 본 검토가 *하지 않는* 것 명시 (§0.4 + §4.2) | ✅ 명시 |

### 3.4 본 단축 합의가 *하지 않는* 것

§4.2 답습.

---

## 4. 결론

```
✅ APPROVE AS DRAFT (단축 합의, Reviewer-only)
   — MVP-1 roadmap DRAFT 권위 권고 발행 적격
   — GP-3 / GP-5 MVP-1 진입 합의 진입 적격 (별도 합의 영역 답습)
   — Observation O-1, O-2 = DRAFT 발효 후 GP-3/GP-5 진입 합의 시점 보강 권고 (DRAFT 적격성 영향 0건)
```

본 결론은 **MVP-1 roadmap DRAFT 적격성 + GP-3/GP-5 진입 합의 진입 가능 여부** 한정. **본 합의는 GP-3 / GP-5 진입 승인 / 수단 확정 / Implementation Evidence PASS / Operational Readiness PASS / Hermes PMO 격상 모두 *불가***.

### 4.1 본 합의가 *발생시키는* 것

- ✅ `docs/architecture/implementation-runtime-roadmap-mvp1.md` (DRAFT) 권위 권고 발행
- ✅ MVP-1 정의 단일 source-of-truth 확정 (GP-3 + GP-5, GP-2 = MVP-2 분리 + 3 사유 답습)
- ✅ 3-layer PASS 분리 유지 + MVP-1 = Implementation Evidence PASS Layer 2 1차 진입 표현 권위 권고
- ✅ GP-3 PoC → MVP-1 gap 6건 + GP-5 PoC → MVP-1 gap 7건 = 합산 13 gap 분석 권위 권고
- ✅ GP-3 코드 본문 5 수단 + 저장 5 수단 + GP-5 Layer 1 6 수단 + pre-commit 4 + PR auto-reject 3 = 합산 23 수단 후보 비교 권위 권고
- ✅ GP-3 Rollback Trigger 8 + GP-5 Rollback Trigger 10 = 합산 18 Rollback Trigger 권위 권고
- ✅ Evidence Ledger 4 enum 후보 (`secret_scan_layer1_implementation` / `secret_storage_isolation_implementation` / `provider_adapter_enforcement_layer1_static` / `mvp1_gate_pass`) 권위 권고
- ✅ 합의 형태 권고 매트릭스 (단축 / 풀 3+1 / T2/T3 영역 분류) 권위 권고
- ✅ MVP-1 → MVP-2 진입 5 조건 + MVP-2 영역 미리 보기 권위 권고
- ✅ GP-3 / GP-5 MVP-1 진입 합의 진입 적격 (별도 합의 영역)
- ✅ **Observation O-1** (CI secret 관리 sub-section 부재) GP-3 진입 합의 시점 보강 권고 = DRAFT 적격성 영향 0건
- ✅ **Observation O-2** (통합 위험 sub-section 부재) GP-3/GP-5 진입 합의 시점 §5.4 추가 권고 = DRAFT 적격성 영향 0건

### 4.2 본 합의가 *발생시키지 않는* 것 (사용자 명시 답습 — 2026-05-12 진입 명령)

- ❌ GP-3 MVP-1 진입 승인
- ❌ GP-5 MVP-1 진입 승인
- ❌ 수단 S-1 / ST-3 / PC-3 / AR-1 / T-6 확정 (모두 *권고 한정*)
- ❌ Implementation Evidence PASS 선언
- ❌ Operational Readiness PASS 선언
- ❌ Hermes PMO 격상 선언
- ❌ 실 runtime code / CI workflow 수정 / hook 구현
- ❌ ADR 본문 자동 갱신 (cross-reference 답습 한정)
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ threshold *고정* (FP / FN / latency 모두 *후보 한정*)
- ❌ MVP-2 ~ MVP-6 본문 deepening
- ❌ 17 항목 우선순위 자동 *재고정*
- ❌ 신규 ADR / 신규 P / 신규 GP 발행
- ❌ ADR-012 §2.2 `event` enum 정식 등록 (4 enum 후보 = 후보 한정)
- ❌ MVP-1 roadmap 본문 자동 보강 (Observation O-1, O-2 자동 흡수 = GP-3/GP-5 진입 합의 시점 별도 작업 영역)

### 4.3 다음 진입점 (사용자 결정 영역)

본 검토 APPROVE AS DRAFT → MVP-1 roadmap DRAFT 권위 권고 발효 → 다음 작업 (사용자 결정 영역):

| 후보 | 영역 | 합의 형태 | Observation 흡수 |
|------|------|---------|----------------|
| (b) | **GP-3 MVP-1 진입 합의** (S-1 + ST-3 + PC-3 + AR-1 권고 채택) | 단축 합의 + PoC evidence (Group D 답습) | **O-1 흡수** = §3.1.2 gap 매트릭스에 G3-7 (CI secret 관리) 추가 |
| (c) | **GP-5 MVP-1 진입 합의** (T-6 + PC-3 + AR-1 권고 채택) | 단축 합의 + PoC evidence (Group A 1차/2차/3차 답습) | — |
| (d) | **MVP-1 1.5차 보강 합의** (S-3 / ST-2 / PC-1 / AR-3) | 풀 3+1 합의 (수단별 §3.6.3 / §4.7.3 답습) | — |
| (e) | **MVP-1 PASS 발효** | 별도 합의 + 사용자 명시 결정 + ADR-011 §2.1 (a)~(e) 5/5 충족 evidence | — |
| (b+c 통합 시점) | **GP-3 + GP-5 통합 위험 sub-section 추가** (§5.4 신설) | 본 roadmap 보강 영역 (단축 합의 적격) | **O-2 흡수** = §5.4 통합 위험 3 영역 (provider key adapter 우회 / direct SDK + secret leakage 결합 / local-CI-Docker 일관성) sub-section 추가 |

**권고 시작 명령** (사용자 권한 영역):

- **"GP-3 MVP-1 진입 합의 시작 (S-1 + ST-3 + PC-3 + AR-1)"** — GP-3 1차 합의 진입 + Observation O-1 흡수 (G3-7 CI secret 관리 추가)
- **"GP-5 MVP-1 진입 합의 시작 (T-6 + PC-3 + AR-1)"** — GP-5 1차 합의 진입
- **"GP-3/GP-5 통합 위험 sub-section §5.4 신설"** — Observation O-2 흡수 (단독 또는 b/c 합의 시 통합 적격)

본 합의 자체 = **GP-3 / GP-5 진입 합의 *진입 가능* 만 권위 권고 발행**. 진입 결정 = 사용자 명시 결정 영역.

---

## 5. Observation 매트릭스 (보강 권고 — DRAFT 적격성 영향 0건)

### 5.1 Observation O-1 — CI secret 관리 sub-section 부재 (검토 기준 #5 부분 충족)

| 항목 | 내용 |
|------|------|
| 발견 | 본 roadmap §3.1.2 gap 매트릭스 G3-1 ~ G3-6 中, CI secret (GitHub Actions secret) 관리 영역 명시적 row 없음 |
| 본 roadmap 부분 커버 | Group D PoC §1.2 #6 답습 (Hermes upstream + ADR-010 Vault HSM 분리 영역) + GP-3 §3.5 R-MVP1-G3-3 (ADR-008 / ADR-010 본문 변경 trigger) + 본 roadmap §3.6.2 의존성 (ADR-008 §A.2 R1-2 cross-reference 갱신) |
| 영향 | DRAFT 적격성 영향 0건 — 본 영역 = MVP-1 → MVP-2 (GP-2 송신 redaction) 또는 P11 (Enforcement Tool 자체 secret) 영역으로 분리 가능 |
| 권고 처리 | GP-3 MVP-1 진입 합의 시점에 §3.1.2 gap 매트릭스에 **G3-7 (CI secret — GitHub Actions secret 관리)** row 추가 권고. 본 row 의 책무 분리 = (i) GitHub secret 정의 / (ii) workflow 노출 정책 / (iii) Hermes upstream R2-6 Hermes upstream 영역 분리 / (iv) Vault HSM 통합 = ADR-010 영역 분리 |

### 5.2 Observation O-2 — GP-3 + GP-5 통합 위험 sub-section 부재 (검토 기준 #7 부분 충족)

| 항목 | 내용 |
|------|------|
| 발견 | 본 roadmap §5 통합 PASS 기준 中 통합 위험 명시 sub-section 부재. 사용자 명시 3 통합 위험 (provider key adapter 우회 / direct SDK + secret leakage 결합 / local-CI-Docker 불일치) 모두 명시적 row 없음 |
| 본 roadmap 부분 커버 | §5.1 ADR-011 5/5 양 GP 매트릭스 + §5.3 통합 Rollback Trigger 5 영역 + 양 GP §3.5 / §4.6 Rollback (R-MVP1-G3-1~7 + R-MVP1-G5-1~10) 답습으로 부분 커버 가능 |
| 영향 | DRAFT 적격성 영향 0건 — 본 영역 = §5 통합 PASS 기준 + 양 GP Rollback 답습으로 부분 커버, 치명적 결함 아님 |
| 권고 처리 | GP-3 + GP-5 진입 합의 시점에 본 roadmap §5.4 (통합 위험 매트릭스) sub-section 추가 권고. 3 통합 위험 row 본문화 + 각 위험 별 enforcement 매트릭스 (GP-3 + GP-5 어느 layer 가 차단 책무) + Rollback Trigger cross-reference 매트릭스 |

### 5.3 두 Observation 의 합의 형태 권고

| 처리 시점 | 합의 형태 | 사유 |
|---------|---------|------|
| GP-3 진입 합의 시점 (O-1 흡수) | 단축 합의 + PoC evidence (Group D 답습) | gap 매트릭스에 1 row 추가 = 영역 분리 명시 영역 |
| GP-3 + GP-5 진입 합의 시점 (O-2 흡수) | 단축 합의 + 본 roadmap §5.4 sub-section 추가 | 양 GP 통합 위험 = ADR-011 §2.1 5/5 답습 영역, 새 권위 결정 0건 |
| 본 합의 자체 (DRAFT 적격성 한정) | Reviewer-only 단축 합의 (본 보고서) | 사용자 명시 진입 명령 답습 + 5 트리거 0/5 발화 |

---

**합의 commit 권위**: 본 commit (`docs(review): record MVP-1 roadmap short review`)
**본 commit + 직전 commits (`cddd22f` MVP-1 roadmap 본문 + `6c91980` references) = MVP-1 roadmap deepening 작성 + 단축 합의 완료**
**다음 세션 진입점**: 사용자 결정 영역 — (b) GP-3 MVP-1 진입 합의 + O-1 흡수 / (c) GP-5 MVP-1 진입 합의 / (d) MVP-1 1.5차 보강 합의 / (e) MVP-1 PASS 발효 / (b+c 통합 시점) GP-3 + GP-5 통합 위험 sub-section §5.4 신설 + O-2 흡수
