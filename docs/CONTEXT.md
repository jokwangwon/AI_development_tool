# 프로젝트 컨텍스트 (Project Context)

> **AI 에이전트가 세션 시작 시 반드시 읽어야 하는 현재 상태 문서**

**최종 업데이트**: 2026-05-07 Part 2 (P2 v3 + G2 + G3 + G4 DRAFT 작성 + G2/G3 DRAFT 검토 APPROVE — G4 검토 다음 세션 진입점)

---

## 현재 활성 의사결정 (2026-05-07 Part 2 종료 시점)

**Phase 0 완료 (Part 1) + 4 게이트 DRAFT 진입 (Part 2)** — Part 1 (G1b PASS + Phase 1 acceptance PASS) 후 사용자 명시 결정으로 P2 v3 + G2 + G3 + G4 DRAFT 작성 진입. **G2/G3 DRAFT 검토 APPROVE AS DRAFT** (Reviewer-only). G4 DRAFT 검토는 다음 세션 진입점.

**4 게이트 합산** (2026-05-07 Part 2 종료 시점):
```
G1b = PASS                            ✅ 2026-05-07 Part 1 승격
G2  = DRAFT 검토 APPROVE              ✅ 1b5bde3 / 957cddc
G3  = DRAFT 검토 APPROVE              ✅ 9c488b1 / d42886b
G4  = DRAFT 작성, 검토 다음 세션       ⏳ 079bc6c / 검토 대기
─────────────────────────────────────
4 게이트 PASS 합산 = 1/4
4 게이트 DRAFT 작성 = 4/4
4 게이트 DRAFT 검토 APPROVE = 3/4
Hermes PMO 격상 선언 = 미선언 (4 게이트 통과 + 외부 LLM 1+ + 사용자 명시 결정 후 별도)
```

### 합의·검증 산출 (2026-05-05 ~ 2026-05-07 Part 2 누적)
- `docs/architecture/system-identity-prequel.md` (시스템 정체성 prequel — P2 v3 정식화 전 임시 선언)
- `docs/review/3plus1-consensus-2026-05-05-system-identity-redefinition.md` (풀 3+1 합의)
- `docs/review/3plus1-consensus-2026-05-05-p2-n1-redaction-reinterpretation.md` (단축 합의)
- `docs/external-review/2026-05-05-system-summary-for-gpt.md` (GPT 검토 의뢰 자료)
- `docs/phase0/day1-environment-and-fact-check.md` (Hermes v0.12.0 사실 확인)
- `docs/phase0/day2-r1-redaction-location-verification.md` (R-1 FAIL 확정)
- `docs/phase0/day3-r2-sqlite-trigger-poc.md` (R-2 PASS 확정)
- `docker/r2-poc/` (R-2 PoC Docker 격리 환경 + 6항목 자동 검증 스크립트)
- `docs/sessions/SESSION_2026-05-05.md` (2026-05-05 세션 로그)
- **`docs/decisions/ADR-011-means-vs-ends-redaction.md` (R-3 신규 — 수단/목적 분리 원칙, R-4~R-7 모법)**
- **`docs/decisions/ADR-008-hermes-adoption-decision.md` 부록 B Amendment (R-3 — R1 specific 갱신, B.6 6단계로 갱신)**
- **`docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md` (R-3 단축 합의 APPROVE)**
- **`docs/architecture/redaction-pattern-equivalence.md` (R-4 — 패턴 동등성 비교 + gap 식별 + 보충 권고, ADR-011 §2.1 (a) 충족)**
- **`docs/phase0/r4-1-trigger-extension-evidence.md` (R-4.1 — Tier-1 42종 trigger UDF 확장 PoC PASS evidence, ADR-011 §2.1 (b) 충족)**
- **`docker/r4-1-poc/` (R-4.1 격리 환경 코드 — Dockerfile + compose + r4_1_poc.py)**
- **`docs/architecture/canary-recheck-design.md` (R-5 — canary 재검증 트리거 설계, ADR-011 §2.4 운영 메커니즘)**
- **`.github/workflows/r2-canary.yml` (R-6 — CI/nightly canary regression workflow, ADR-011 §2.1 (d) 자동 회귀 검증 경로)**
- **`docs/phase0/redaction-verification-sop.md` (R-7 — Phase 1 acceptance SOP, ADR-008 부록 B.6 마지막 단계, 2026-05-07 갱신 G1b PASS)**
- **`docs/review/3plus1-consensus-2026-05-07-g1b-phase1-acceptance.md` (R-7 SOP §7.3 단축 합의 APPROVE — G1b PASS 승격 + Phase 1 acceptance PASS 선언 권위)**

#### Part 2 (2026-05-07 후속 — P2 v3 + G2 + G3 + G4 DRAFT)
- **`docs/architecture/hermes-adoption-design-v3.md` (P2 v3 DRAFT — 12 섹션, P2 v2 §2.1.3 가정 폐기 + R-2~R-7 흡수 + Hermes PMO 구조 사전 정의 + G2/G3/G4 entry/exit, commit `8f8e323`)**
- **`docs/review/3plus1-consensus-2026-05-07-p2-v3-draft.md` (P2 v3 DRAFT 단축 검토 APPROVE AS DRAFT, 7 기준 7/7 PASS, commit `12d7609`)**
- **`docs/architecture/governance-preconditions.md` (G2 DRAFT — 13 섹션, P1~P8 8 위반 경로 + GP-1~GP-6 6 사전조건 매핑 + 강제 메커니즘 분류 매트릭스 + §9 메타 안전장치 G3 인터페이스, commit `1b5bde3`)**
- **`docs/review/3plus1-consensus-2026-05-07-g2-governance-preconditions-draft.md` (G2 DRAFT 단축 검토 APPROVE AS DRAFT, 10 기준 10/10 PASS, commit `957cddc`)**
- **`docs/architecture/hermes-not-root-of-trust-runtime.md` (G3 DRAFT — 11 섹션, 권위 위계 운영 + Hermes 권한 22 항목 (T1 8 / T2 2 / T3 12) + 3 위험 5 측면 + 합의 자기참조 차단 + Evidence 결정 5 운영 규칙 + G2·G4 인터페이스, commit `9c488b1`)**
- **`docs/review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md` (G3 DRAFT 단축 검토 APPROVE AS DRAFT, 10 기준 10/10 PASS — G3 §4 자기참조 차단의 적용 대상으로 한계 명시, commit `d42886b`)**
- **`docs/architecture/provider-agnostic-memory-skill-design.md` (G4 DRAFT — 11 섹션, 옵션 B 통합. Memory scope 4 단계 (MVP Global+Project) + Skill schema 17 필드 + JSONL export hash chain + Memory/Skill boundary 4 금지 + G3·G2 GP-6 인터페이스 + 3-way, commit `079bc6c`)**
- **G4 DRAFT 단축 검토 — 다음 세션 진입점 (미수행)**

### 핵심 채택 사항 (R-3에서 ADR 권위로 승격)
- **정체성**: "AI Development Company OS" 메타포 (선언적, 즉시)
- **권위 위계**: `Constitution > ADR > SDD > Harness Gates > Hermes > Worker Agents` — **ADR-011 §2.3 영구 권위화**
- **Hermes ≠ root of trust** — **ADR-011 §2.3 영구 권위화** (prequel §3 → ADR 승격, prequel 폐기 후에도 보존)
- **자동 학습 ≠ 자동 정책 변경** (T1 자동 / T2 사용자 승인 / T3 절대 금지) — **ADR-011 §2.4 영구 권위화**
- **수단/목적 분리 원칙** — **ADR-011 §2.1 신설** (헌법 8조 본질 = "DB 평문 저장 차단 결과", 수단 대체에 (a)~(d) 4조건 강제)
- **Evidence 검증**: "Agent proposes / Hermes orchestrates / Tools verify / Evidence decides / Human overrides"
- **메타포 강제 금지** 조항

### MVP 범위 (Phase 1 시작 기준, 변경 없음)
- **Worker Agent 4**: PM/Orchestrator + Architect + Implementation + Reviewer
- **Memory 2단계**: Global + Project (manual promotion만)
- **Evidence**: Markdown + JSONL append-only (hash chain or git append commit으로 변조 방지)

### G1a/G1b 분리 (CRITICAL — 다음 세션 핵심 컨텍스트)

```
G1a: Hermes native redaction applies before DB INSERT
   Result: FAIL (R-1 확정)
   근거: agent/redact.py docstring "for logs and tool output", redact import 25개 모두 비-DB,
         hermes_state.py redact import 0건

G1b: DB-level fallback prevents plaintext secret persistence
   Result: PASS by R-2 PoC
   근거: SQLCipher BEFORE INSERT trigger + REGEXP UDF로 6항목 검증 PASS
         (Docker 격리 환경, canary 5종 차단, DB 평문 부재, 에러 평문 미노출)
```

**G1b의 의미 (사용자 명시)**:
> Hermes native redaction은 로그/LLM 송신 방어로만 취급, DB INSERT 경로는 SQLCipher BEFORE INSERT trigger로 별도 차단. **Hermes를 신뢰하는 구조가 아니라 DB 레벨에서 Hermes를 보완하는 구조.**

### 4 게이트 진행 상태

| 게이트 | 정의 | 현 상태 |
|-------|------|--------|
| ~~G1a~~ | Hermes native redaction → DB | ❌ FAIL 확정 (폐기) — **ADR-011 §2.2 / ADR-008 부록 B 권위 명시** |
| **G1b** | **DB-level fallback (SQLCipher trigger)** | ✅ **PASS** (2026-05-07 Part 1 단축 합의 승격) — R-3 ~ R-7 6단계 ✅ + R-4.1 격리 PoC PASS + R-6 GitHub Actions actual run `25482284523` PASS (24초, verdict PASS, 42/42, leak 0) + Reviewer-only 단축 합의 APPROVE (`docs/review/3plus1-consensus-2026-05-07-g1b-phase1-acceptance.md`) |
| **G2** | **6 거버넌스 사전조건** | 🟡 **DRAFT 검토 APPROVE AS DRAFT** (2026-05-07 Part 2) — `governance-preconditions.md` (`1b5bde3`) + 검토 보고서 (`957cddc`). PASS 미선언 |
| **G3** | **"Hermes ≠ root of trust" 운영 구현** | 🟡 **DRAFT 검토 APPROVE AS DRAFT** (2026-05-07 Part 2) — `hermes-not-root-of-trust-runtime.md` (`9c488b1`) + 검토 보고서 (`d42886b`). ADR-011 §2.3 권위 확정 + 본 G3 운영 구현 정의. PASS 미선언, **PASS 합의 시 외부 LLM 의견 권장** (G3 §4.4.2) |
| **G4** | **Provider-agnostic Memory/Skill 형식** | 🟡 **DRAFT 작성** (2026-05-07 Part 2) — `provider-agnostic-memory-skill-design.md` (`079bc6c`, 옵션 B 통합 문서). DRAFT 검토 다음 세션 진입점. PASS 미선언 |

### Phase 0 진행 상태
- ✅ Day 1 (사실 확인)
- ✅ Day 2 (R-1 FAIL)
- ✅ Day 3 (R-2 PASS, baseline 5 patterns)
- ✅ **R-3 (2026-05-06): ADR-011 발행 + ADR-008 부록 B Amendment, 단축 합의 APPROVE**
- ✅ **R-4 (2026-05-06): 패턴 동등성 비교 + gap 식별 + 보충 권고 (ADR-011 §2.1 (a) 충족)**
- ✅ **R-4.1 (2026-05-06): Tier-1 42종 trigger UDF 확장 + 격리 환경 PoC PASS (ADR-011 §2.1 (b) 충족, 1차 PARTIAL → 2차 PASS 진화)**
- ✅ **R-5 (2026-05-06): canary 재검증 트리거 설계 (T13 강화 + 6 trigger 시점 + 4 verdict + 4 안전장치 + Markdown+JSONL evidence + T1/T2/T3 정책 매트릭스)**
- ✅ **R-6 (2026-05-06): CI/nightly canary regression workflow (workflow_dispatch + nightly cron + push/PR + R-4.1 PoC 실행 + JSON evidence 추출 + verdict PASS 검증 + artifact 업로드, permissions: contents: read)**
- ✅ **R-7 (2026-05-06): Phase 1 acceptance SOP — 13 checklist + 4 verdict + 9 ROLLBACK + 7 Evidence + push 전/후 작업 분리**
- ✅ **R-6 actual run (2026-05-07): 1차 FAIL infra bug → fix `939125b` → 2차 run `25482284523` PASS (24초)**
- ✅ **R-7 SOP §7.3 단축 합의 (2026-05-07): Reviewer 13 항목 + 8 PASS 조건 + 5 메타 편향 통제 → APPROVE → G1b PASS 승격 + Phase 1 acceptance PASS 선언**

### 다음 세션 TODO (우선순위 순)

1. ~~**R-3 / R-4 / R-4.1 / R-5 / R-6 / R-7 + G1b PASS 승격 + Phase 1 acceptance PASS 선언**~~ ✅ 완료 (2026-05-06 ~ 2026-05-07 Part 1)
2. ~~**P2 v3 + G2 + G3 + G4 DRAFT 작성 + G2·G3 DRAFT 검토 APPROVE**~~ ✅ 완료 (2026-05-07 Part 2)
3. **G4 Reviewer-only 단축 검토** (다음 진입점): `docs/review/3plus1-consensus-2026-05-XX-g4-provider-agnostic-memory-skill-draft.md` — G2/G3 검토 패턴 답습. APPROVE 시 G4 진입 적격 + 정식 채택 합의 준비.
4. **G2 / G3 / G4 정식 채택 합의 준비** (G4 DRAFT 검토 APPROVE 후):
   - 옵션 1: G4 단독 단축 합의 (Reviewer-only)
   - 옵션 2: G4 + G2 GP-6 통합 합의
   - **옵션 3 (권고 후보)**: G2 + G3 + G4 통합 풀 3+1 합의 + **외부 LLM 1+ 필수** (PR 묶음, 격상 통합 합의 답습)
5. **정식 채택 후 ADR PR 묶음**: ADR-008 / ADR-009 / ADR-010 / ADR-011 cross-reference 갱신 + 신규 ADR-014 (Provider-agnostic Memory/Skill Format) 후보 검토
6. **P2 v2 / system-identity-prequel.md archive 처리** (정식 채택 시점에)
7. **INDEX / CONTEXT 갱신** (정식 채택 시점에 — 본 Part 2 종료 housekeeping 외 추가 갱신)
8. **Hermes PMO 격상 후보** (4 게이트 모두 PASS + 외부 LLM 1+ 합의 + 사용자 명시 결정 후 별도)

**권고 시작점**: "G4 Reviewer-only 단축 검토를 진행해주세요"

### 잔여 (Task #16, 본 세션 미처리)
- P1 v2 minor revisions 6건 — P2 v3 작성과 병합 검토
- `.claude/settings.local.json` gitignore 처리
- 잘못된 origin/main 커밋 2개 정리

### 영구 핵심 제약
- **Provider Liquidity** (헌법 5조 비협상, `feedback_provider_liquidity.md`)
- **Hermes ≠ root of trust** (system-identity-prequel §3)
- **메타포 강제 금지** (system-identity-prequel §7)

상세: `docs/sessions/SESSION_2026-05-05.md`, `docs/architecture/system-identity-prequel.md`

---

## 프로젝트 성격

**이 프로젝트는 "AI Development Company OS 메타-템플릿"이다.**

새 아이디어로 개발을 시작할 때, 이 프로젝트의 문서/설정 파일을 가져와 적용한다.

```
사용법:
  1. 새 프로젝트 생성
  2. 이 템플릿의 파일을 복사
  3. 아이디어를 제시하면 Phase 0부터 자동화 개발 시작
```

---

## 릴리스: v1.0.0

### 포함된 설계 체계

| 문서 | ADR | 설명 |
|------|-----|------|
| 프로젝트 헌법 | — | 12개 조항 (제8-2조 환경 관리 포함) |
| 하네스 엔지니어링 설계 | — | 8-Layer 피드백 루프 |
| 3+1 멀티에이전트 설계 | — | 합의 기반 의사결정 시스템 |
| 아키텍처/코드 품질 원칙 | — | 10대 원칙 + 코드 품질 기준 |
| 자동화 검토 질문지 | ADR-001 | Phase 0: 아이디어 → 브리프 |
| 아이디어 기반 스택 결정 | ADR-002 | Phase 1: 스택 통합 결정 |
| 생성 AI 에셋 파이프라인 | ADR-003 | Guide-First 에셋 생성 |
| 생성 AI 확장성 | ADR-004 | Config 기반 모델 교체 + 학습 안내 |
| AI 백엔드 스택 가이드라인 | ADR-005 | 로컬 추론 시 Python 분리 |
| 환경 변수 + Docker-First | ADR-006 | 하드코딩 제로 + 중앙 관리 |
| 변경 영향 분석 | ADR-007 | 의존성/장애 사전 검증, 자동 분류 |
| **시스템 정체성 prequel** | — (P2 v3로 정식화 예정) | **AI Development Company OS, Hermes PMO 4 게이트, MVP 4 Agent + 2 Memory** |
| 개발 가이드 | — | SDD+TDD 워크플로우 |
| 테스트 전략 | — | 70% 커버리지 목표 |

### 개발 파이프라인 (확정)

```
Phase 0: 자동화 검토 질문지 (필수3 + 동적2)
Phase 1: 3+1 합의 (아이디어 + 스택 + 에셋 식별)
    ├── Phase 2-3: SDD → TDD (코드)
    └── 에셋 파이프라인 (비코드, Guide-First, 병렬)
Phase 4: 통합 테스트 + 배포
```

---

**이 문서는 매 세션 시작 시 반드시 읽어야 합니다.**
**상세**: `docs/sessions/SESSION_2026-05-05.md`, `docs/architecture/system-identity-prequel.md`, `docs/review/3plus1-consensus-2026-05-05-system-identity-redefinition.md`
