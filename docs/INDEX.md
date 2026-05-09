# 문서 인덱스 (Documentation Index)

> **프로젝트 문서 전체 구조 및 읽는 순서**

**최종 업데이트**: 2026-05-09 (G2 + G3 + G4 통합 풀 3+1 합의 + 외부 LLM 2건 [GPT cross-vendor + Claude 인접 컨텍스트] APPROVE WITH CONDITIONS — **3 게이트 동시 Design/Governance Gate PASS 승격** + P2 v3 정식 채택 합의 단계 진입 적격)

---

## 문서 읽는 순서 (권장)

### 1. 시작하기
1. **[README.md](../README.md)** — 프로젝트 개요, 비전, 개발 방법론
2. **[PROJECT_CONSTITUTION.md](constitution/PROJECT_CONSTITUTION.md)** — 프로젝트 헌법 (최상위 규칙)

### 2. 아키텍처 이해
3. **[harness-engineering-design.md](architecture/harness-engineering-design.md)** — 하네스 엔지니어링 설계
4. **[multi-agent-system-design.md](architecture/multi-agent-system-design.md)** — 3+1 멀티 에이전트 합의 시스템
5. **[automated-review-questionnaire-design.md](architecture/automated-review-questionnaire-design.md)** — 자동화 검토 질문지 (3+1 합의 완료)
6. **[idea-driven-stack-decision-design.md](architecture/idea-driven-stack-decision-design.md)** — 아이디어 기반 스택 결정 (3+1 합의 완료)
7. **[generative-ai-asset-pipeline-design.md](architecture/generative-ai-asset-pipeline-design.md)** — 생성 AI 에셋 파이프라인 (3+1 합의 완료)
8. **[generative-ai-extensibility-design.md](architecture/generative-ai-extensibility-design.md)** — 생성 AI 확장성: 학습/모델교체/확장 (3+1 합의 완료)
9. **[ai-backend-stack-convention.md](architecture/ai-backend-stack-convention.md)** — AI 백엔드 스택 가이드라인: Python 분리 기준 (3+1 합의 완료)
10. **[environment-and-docker-design.md](architecture/environment-and-docker-design.md)** — 환경 변수 중앙 관리 + Docker-First (3+1 합의 완료)
11. **[change-impact-analysis-design.md](architecture/change-impact-analysis-design.md)** — 변경 영향 분석: 의존성/장애 사전 검증 (3+1 합의 완료)

### 3. 원칙 문서
5. **[ARCHITECTURE_PRINCIPLES.md](constitution/ARCHITECTURE_PRINCIPLES.md)** — 아키텍처 10대 원칙
6. **[CODE_QUALITY_PRINCIPLES.md](constitution/CODE_QUALITY_PRINCIPLES.md)** — 코드 품질 원칙

### 4. 개발 가이드
7. **[DEVELOPMENT_GUIDE.md](guides/DEVELOPMENT_GUIDE.md)** — 개발 프로세스, Git 규칙
8. **[TEST_STRATEGY.md](guides/TEST_STRATEGY.md)** — 테스트 전략 (70% 커버리지)

### 5. AI 에이전트 지시사항
9. **[CLAUDE.md](../CLAUDE.md)** — Claude Code 하네스 규칙 (매 세션 자동 로드)

---

## 문서 구조

```
docs/
├── INDEX.md                              # 현재 문서 (문서 인덱스)
├── CONTEXT.md                            # 프로젝트 현재 상태
│
├── constitution/                         # 헌법 및 원칙
│   ├── PROJECT_CONSTITUTION.md           # 프로젝트 헌법 (11개 조항)
│   ├── ARCHITECTURE_PRINCIPLES.md        # 아키텍처 10대 원칙
│   └── CODE_QUALITY_PRINCIPLES.md        # 코드 품질 원칙
│
├── architecture/                         # 설계 문서
│   ├── harness-engineering-design.md     # 하네스 엔지니어링 설계
│   ├── multi-agent-system-design.md      # 3+1 멀티 에이전트 합의 시스템
│   ├── automated-review-questionnaire-design.md  # 자동화 검토 질문지
│   ├── idea-driven-stack-decision-design.md      # 아이디어 기반 스택 결정
│   ├── generative-ai-asset-pipeline-design.md   # 생성 AI 에셋 파이프라인
│   ├── generative-ai-extensibility-design.md    # 생성 AI 확장성
│   ├── ai-backend-stack-convention.md           # AI 백엔드 스택 가이드라인
│   ├── environment-and-docker-design.md         # 환경 변수 + Docker-First
│   ├── change-impact-analysis-design.md         # 변경 영향 분석
│   ├── llm-providers-design.md                  # P1 v2 LiteLLM facade
│   ├── hermes-adoption-design.md                # P2 v2 (정식 채택 시 archived 예정)
│   ├── hermes-adoption-design-v3.md             # P2 v3 DRAFT — Hermes PMO 구조 + G2/G3/G4 잔여 게이트
│   ├── system-identity-prequel.md               # 시스템 정체성 prequel (P2 v3 정식 채택 시 archived 예정)
│   ├── redaction-pattern-equivalence.md         # R-4 pattern equivalence
│   ├── canary-recheck-design.md                 # R-5 canary 재검증 트리거 설계
│   ├── governance-preconditions.md              # G2 Design/Governance Gate PASS (Bundled, 2026-05-09) — 6 거버넌스 사전조건 (P1~P8 / GP-1~GP-6, GP-1 PASS / GP-2~6 IMPLEMENTATION PENDING)
│   ├── hermes-not-root-of-trust-runtime.md      # G3 Design/Governance Gate PASS (Bundled, 2026-05-09) — Hermes ≠ root of trust 운영 구현 (운영 구현 IMPLEMENTATION PENDING)
│   └── provider-agnostic-memory-skill-design.md # G4 Design/Governance Gate PASS (Bundled, 2026-05-09) — Memory scope + Skill schema + JSONL export (라운드트립/migration script IMPLEMENTATION PENDING)
│
├── guides/                               # 개발 가이드
│   ├── DEVELOPMENT_GUIDE.md              # 개발 프로세스, Git 규칙
│   └── TEST_STRATEGY.md                  # 테스트 전략
│
├── decisions/                            # ADR (Architecture Decision Records)
│   ├── ADR-000-template.md               # ADR 템플릿
│   ├── ADR-001-automated-review-questionnaire.md  # 자동화 검토 질문지
│   ├── ADR-002-idea-driven-stack-decision.md      # 아이디어 기반 스택 결정
│   ├── ADR-003-generative-ai-asset-pipeline.md   # 생성 AI 에셋 파이프라인
│   ├── ADR-004-generative-ai-extensibility.md    # 생성 AI 확장성
│   ├── ADR-005-ai-backend-stack-guideline.md     # AI 백엔드 스택
│   ├── ADR-006-environment-and-docker.md         # 환경 변수 + Docker
│   ├── ADR-007-change-impact-analysis.md         # 변경 영향 분석
│   ├── ADR-008-hermes-adoption-decision.md       # Hermes 도입 (Option B) + 부록 B Amendment (R1 수단/목적 분리)
│   ├── ADR-009-self-adapter-v2-entry-conditions.md  # 자체 Adapter v2.0 진입 조건
│   ├── ADR-010-sqlcipher-vault-key-management.md    # SQLCipher Vault HSM 키 관리
│   ├── ADR-011-means-vs-ends-redaction.md        # 수단/목적 분리 원칙 (R-4~R-7 모법)
│   └── ...
│
├── phase0/                              # Phase 0 evidence (사실 확인 / R-1 / R-2 / R-4.1)
│   ├── day1-environment-and-fact-check.md           # Day 1 사실 확인
│   ├── day2-r1-redaction-location-verification.md   # R-1 FAIL evidence
│   ├── day3-r2-sqlite-trigger-poc.md                # R-2 PASS evidence (baseline 5 patterns)
│   └── r4-1-trigger-extension-evidence.md           # R-4.1 PASS evidence (Tier-1 42 + baseline 5)
│
├── sessions/                             # 세션 로그
│   └── ...
│
└── review/                               # 검토 보고서
    └── ...
```

---

## 우선순위별 문서

### CRITICAL (반드시 읽어야 함)
- `PROJECT_CONSTITUTION.md` — 프로젝트 헌법 (모든 개발의 기준)
- `harness-engineering-design.md` — 하네스 엔지니어링 (핵심 설계 철학)
- `multi-agent-system-design.md` — 3+1 에이전트 합의 (검증 시스템)

### HIGH (개발 시작 전)
- `ARCHITECTURE_PRINCIPLES.md` — 아키텍처 원칙
- `CODE_QUALITY_PRINCIPLES.md` — 코드 품질 원칙
- `DEVELOPMENT_GUIDE.md` — 개발 프로세스
- `TEST_STRATEGY.md` — 테스트 전략

---

## 문서 간 관계

```
PROJECT_CONSTITUTION.md (헌법)
    ↓
    ├─→ ARCHITECTURE_PRINCIPLES.md (제3조, 제6조 상세화)
    ├─→ CODE_QUALITY_PRINCIPLES.md (제5조 상세화)
    ├─→ harness-engineering-design.md (제3조 상세화)
    └─→ multi-agent-system-design.md (제4조 상세화)

CLAUDE.md (에이전트 지시사항)
    ↓
    ├─→ 헌법 참조
    ├─→ 하네스 설계 참조
    └─→ 멀티에이전트 설계 참조
```

---

## 문서 업데이트 이력

| 날짜 | 변경 내용 | 관련 문서 |
|------|-----------|-----------|
| 2026-04-06 | 프로젝트 초기 문서 체계 수립 | 전체 문서 |
| 2026-04-06 | 자동화 검토 질문지 설계 (3+1 합의 완료) | `automated-review-questionnaire-design.md`, `ADR-001` |
| 2026-04-06 | 아이디어 기반 스택 결정 (3+1 합의 완료) | `idea-driven-stack-decision-design.md`, `ADR-002` |
| 2026-04-06 | 생성 AI 에셋 파이프라인 (3+1 합의 완료) | `generative-ai-asset-pipeline-design.md`, `ADR-003` |
| 2026-04-06 | 생성 AI 확장성 — 학습/모델교체/확장 (3+1 합의 완료) | `generative-ai-extensibility-design.md`, `ADR-004` |
| 2026-04-06 | AI 백엔드 스택 가이드라인 (3+1 합의 완료) | `ai-backend-stack-convention.md`, `ADR-005` |
| 2026-04-06 | 환경 변수 중앙 관리 + Docker-First (3+1 합의 완료) | `environment-and-docker-design.md`, `ADR-006` |
| 2026-04-06 | 변경 영향 분석 (3+1 합의 완료) | `change-impact-analysis-design.md`, `ADR-007` |
| 2026-05-04 | Hermes Agent 도입 결정 — Option B 채택 (3+1 합의 완료) | `ADR-008-hermes-adoption-decision.md`, `review/3plus1-consensus-2026-05-04-hermes.md` |
| 2026-05-04 | LLM Provider 추상화 설계 — Option β 채택 (LiteLLM facade 승격, 3+1 합의 완료, v2 보강 적용) | `llm-providers-design.md`, `ADR-009-self-adapter-v2-entry-conditions.md`, `review/3plus1-consensus-2026-05-04-p1-llm-providers.md` |
| 2026-05-04 | Hermes Agent 도입 설계 (P2) — 6개 차단조건 충족 메커니즘 + Phase 1/2/3 + 롤백 + 검증 메트릭 (3+1 합의 완료) | `hermes-adoption-design.md`, `review/3plus1-consensus-2026-05-04-p2-hermes-adoption.md` |
| 2026-05-04 | P2 v2 적용 (TIER 0+1+2+3 보강 19건) — Phase 0 신설, SQLCipher Vault HSM + Shamir, 격리 강화 6항목, 자동 롤백 11트리거, Phase 2 메트릭 분리 등 | `hermes-adoption-design.md` (v2), `ADR-010-sqlcipher-vault-key-management.md` |
| 2026-05-05 | Phase 0 Day 1 사실 확인 + P2-N1 단축 합의 — Hermes v0.12.0 코드 grep 결과 `add_pre_record_hook` API 미존재 확정, Hermes 자체 redaction 발견. R-1~R-7 보강 (R-1 결과 조건부) | `phase0/day1-environment-and-fact-check.md`, `review/3plus1-consensus-2026-05-05-p2-n1-redaction-reinterpretation.md` |
| 2026-05-05 | 시스템 정체성 재정의 풀 3+1 합의 (GPT 외부 4번째 의견 포함) — "AI Development Company OS" 비전 채택, Hermes PMO 4 게이트 후 격상, P2 v3 R-7 후 신규 작성, MVP 부분 채택 (4 Agent + 2 Memory + Markdown/JSONL Evidence) | `architecture/system-identity-prequel.md`, `review/3plus1-consensus-2026-05-05-system-identity-redefinition.md` |
| 2026-05-05 | Phase 0 R-1 검증 결과 — FAIL 확정 (Hermes native redaction은 로그/도구 출력/통신 전용, DB INSERT 경로 미적용) | `phase0/day2-r1-redaction-location-verification.md` |
| 2026-05-05 | Phase 0 R-2 SQLite trigger PoC — PASS (Docker 격리 환경에서 SQLCipher BEFORE INSERT trigger + REGEXP UDF로 canary 5종 차단, DB 평문 부재, 에러 평문 미노출). G1b 재판정 진입 조건 충족 | `phase0/day3-r2-sqlite-trigger-poc.md`, `docker/r2-poc/` |
| 2026-05-05 | 세션 로그 — 시스템 정체성 재정의 + R-1 FAIL + R-2 PASS + G1a/G1b 분리. 다음 세션 R-3~R-7 진입 대기 | `sessions/SESSION_2026-05-05.md` |
| 2026-05-06 | Phase 0 R-3 — ADR-011 (수단/목적 분리 원칙) 신규 + ADR-008 부록 B Amendment 추가. 단축 합의(Reviewer-only) APPROVE. G1a/G1b 분리 / Hermes ≠ root of trust / 자동 학습 vs 자동 정책 변경 분리(T1/T2/T3) ADR 권위화. R-4~R-7 모법 역할 명시 | `decisions/ADR-011-means-vs-ends-redaction.md`, `decisions/ADR-008-hermes-adoption-decision.md` (부록 B), `review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md` |
| 2026-05-06 | 세션 로그 — R-3 ADR 형식화 + 세션 단절 후 복구 + INDEX/CLAUDE/CONTEXT 갱신. 다음 세션 R-4 진입 대기 | `sessions/SESSION_2026-05-06.md` |
| 2026-05-06 | Phase 0 R-4 — Hermes redact pattern ↔ P1_REDACTOR 패턴 동등성 비교 + gap 식별 + 보충 권고. ADR-011 §2.1 (a) 충족 의무의 직접 산출 | `architecture/redaction-pattern-equivalence.md` |
| 2026-05-06 | Phase 0 R-4.1 — Tier-1 42종 trigger UDF 확장 + Docker 격리 환경 PoC PASS. ADR-011 §2.1 (b) 직접 충족 evidence 생성. 1차 PARTIAL → 2차 PASS 진화 (H-J/H-L 직접 등록 제외 + alternation 채택) | `phase0/r4-1-trigger-extension-evidence.md`, `docker/r4-1-poc/` |
| 2026-05-06 | R-4 §7.2 산술 정정 (Prefix 30 → 31, Tier-1 41 → 42, frozenset → alternation) + ADR-008 부록 B.6 R-4 ✅ / R-4.1 ✅ 갱신 | `architecture/redaction-pattern-equivalence.md`, `decisions/ADR-008-hermes-adoption-decision.md` |
| 2026-05-06 | `.claude/settings.local.json` untrack + `.gitignore` 갱신 — 로컬 사용자 설정 commit 분리, 권한 승인 누적 디스크 보존 | `.gitignore` |
| 2026-05-06 | Phase 0 R-5 — canary 재검증 트리거 설계. T13 강화 / R-4.1 catalog 재사용 / 6 trigger 시점 / PASS-PARTIAL-FAIL-ROLLBACK 판정 / 4 안전장치 / Markdown+JSONL 이중 evidence / T1/T2/T3 정책 매트릭스. 실제 자동화 구현은 R-6 위임 | `architecture/canary-recheck-design.md` |
| 2026-05-06 | Phase 0 R-6 — CI/nightly canary regression workflow 구현. workflow_dispatch + nightly cron + push/PR triggers (5 paths) + Docker R-4.1 PoC 실행 + JSON evidence 추출 + verdict PASS 검증 + artifact 업로드. permissions: contents: read (CI verifies, does not mutate). ADR-011 §2.1 (d) 자동 회귀 검증 경로 직접 충족 | `.github/workflows/r2-canary.yml` |
| 2026-05-06 | Phase 0 R-7 — Phase 1 acceptance SOP 작성. 13 항목 checklist + PASS/PARTIAL/FAIL/ROLLBACK 판정 + G1a FAIL/G1b CONDITIONALLY PASS 명시 + 9 ROLLBACK trigger + 7 Evidence 요구 + push 전/후 작업 분리. ADR-008 부록 B.6 6단계 모두 작성 ✅. **G1b PASS 선언은 R-6 GitHub Actions actual run PASS 후 단축 합의 거쳐 승격 (자동 승격 금지)** | `phase0/redaction-verification-sop.md` |
| 2026-05-06 | ADR-008 부록 B.6 R-5/R-6/R-7 ✅ 갱신 + G1b CONDITIONALLY PASS 명시 (R-6 actual run 후 PASS 승격 절차 본문 추가) | `decisions/ADR-008-hermes-adoption-decision.md` |
| 2026-05-07 | R-6 GitHub Actions actual run — 1차 FAIL (docker compose stdout prefix JSON parse infra bug, 보안/catalog/secret 위반 아님 사용자 분류) → fix `939125b` (`--no-log-prefix` flag 추가, workflow YAML 1 file 한정) → 2차 run `25482284523` PASS (24초, verdict PASS, 42/42, leak 0, ROLLBACK 9 조건 0 발화) | `.github/workflows/r2-canary.yml` |
| 2026-05-07 | R-7 SOP §7.3 Reviewer-only 단축 합의 APPROVE — Reviewer 13 항목 + 8 PASS 조건 + 5 메타 편향 통제 수단. **G1b CONDITIONALLY PASS → PASS 승격, Phase 1 acceptance PARTIAL → PASS 선언**. 자동 승격 아님 (사용자 명시 + ADR-011 §2.4 T2 절차 답습). Hermes PMO 격상은 4 게이트 통과 후 별도 결정 (본 합의 범위 외) | `review/3plus1-consensus-2026-05-07-g1b-phase1-acceptance.md`, `decisions/ADR-008-hermes-adoption-decision.md` (부록 B.6), `phase0/redaction-verification-sop.md` (§3.4 / §4.2 / §4.3 / §6.1 / §7.1.1 / §7.3 갱신) |
| 2026-05-07 | 세션 로그 — push 진행 + 1차 FAIL infra fix + 2차 PASS + 단축 합의 APPROVE + G1b PASS 승격 + Phase 1 acceptance PASS 선언. 다음 진입점 P2 v3 또는 G2/G3/G4 병행 | `sessions/SESSION_2026-05-07.md` |
| 2026-05-07 (Part 2) | P2 v3 신규 작성 (DRAFT) — P2 v2 §2.1.3 가정 폐기 + R-2~R-7 흡수 + Hermes PMO 구조 사전 정의 (격상 미선언) + G2/G3/G4 잔여 게이트 entry/exit | `architecture/hermes-adoption-design-v3.md` |
| 2026-05-07 (Part 2) | P2 v3 DRAFT Reviewer-only 단축 검토 APPROVE AS DRAFT — 7 기준 7/7 PASS + 8 금지 위반 0건 + 4 자기 발견 잠재 위험 (LOW) | `review/3plus1-consensus-2026-05-07-p2-v3-draft.md` |
| 2026-05-07 (Part 2) | G2 거버넌스 사전조건 신규 작성 (DRAFT) — 헌법 8조·5조(Provider Liquidity) 위반 경로 P1~P8 정의 + 6 거버넌스 사전조건 GP-1~GP-6 매핑 + 강제 메커니즘 분류 (계산적 6/6, 추론적 보조 4/6, 자동 롤백 6/6) + §9 메타 안전장치 G3 인터페이스 | `architecture/governance-preconditions.md` |
| 2026-05-07 (Part 2) | G2 DRAFT Reviewer-only 단축 검토 APPROVE AS DRAFT — 10 기준 10/10 PASS + 10 금지 위반 0건 + 4 자기 발견 잠재 위험 (LOW) | `review/3plus1-consensus-2026-05-07-g2-governance-preconditions-draft.md` |
| 2026-05-07 (Part 2) | G3 Hermes ≠ root of trust runtime 신규 작성 (DRAFT) — 권위 위계 운영 구현 + Hermes 권한 22 항목 (T1 8 / T2 2 / T3 12) + 3 위험 5 측면 분해 + 합의 인프라 자기참조 차단 + Evidence 결정 5 운영 규칙 + G2/G4 인터페이스 | `architecture/hermes-not-root-of-trust-runtime.md` |
| 2026-05-07 (Part 2) | G3 DRAFT Reviewer-only 단축 검토 APPROVE AS DRAFT — 10 기준 10/10 PASS + 8 금지 위반 0건 + 4 자기 발견 잠재 위험 (LOW). G3 §4 자기참조 차단의 적용 대상으로 한계 명시 — G3 PASS 합의 시 외부 LLM 의견 권장 | `review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md` |
| 2026-05-07 (Part 2) | G4 Provider-agnostic Memory/Skill 신규 작성 (DRAFT, 옵션 B 통합 문서) — Memory scope 4단계 (MVP Global+Project + 후속 Session/Team-Agent) + Skill schema 17 필드 + JSONL export hash chain 변조 방지 + Memory/Skill boundary 4 금지 + G3·G2 GP-6 인터페이스 + 3-way (GP-6/G3/G4). 검토 다음 세션 진입점 | `architecture/provider-agnostic-memory-skill-design.md` |
| 2026-05-07 (Part 2) | 세션 로그 Part 2 + CONTEXT/INDEX 갱신 — 4 게이트 진행 상태 표 갱신 (G1b PASS / G2·G3 DRAFT 검토 APPROVE / G4 DRAFT 검토 다음 세션) + 다음 세션 TODO 갱신 (G4 단축 검토 → 옵션 1/2/3 정식 채택 합의 / 옵션 3 외부 LLM 1+ 필수) | `sessions/SESSION_2026-05-07.md` (Part 2), `CONTEXT.md`, `INDEX.md` |
| 2026-05-09 | G4 DRAFT Reviewer-only 단축 검토 APPROVE AS DRAFT — 10 기준 10/10 PASS + 8 금지 위반 0건 + 5 자기 발견 잠재 위험 (LOW/VERY LOW: P-1 RFC 8785 JCS / P-2 schema 진화 / P-3 schema_version declaration / P-4 §6.4 명명 / P-5 `~/.claude/global` path). G3 §4 자기참조 차단의 적용 대상으로 한계 명시 — G4 PASS 합의 시 외부 LLM 의견 권장. G2/G3/G4 정식 채택 합의 진입 적격 | `review/3plus1-consensus-2026-05-09-g4-provider-agnostic-memory-skill-draft.md` |
| 2026-05-09 (후속) | **G2 + G3 + G4 통합 풀 3+1 합의 + 외부 LLM 2건 (옵션 3)** — 외부 LLM 검토 의뢰 자료 작성 + Agent A (구현/운영, Opus) + Agent B (보안/거버넌스, Opus) + Agent C (대안/단순화, Opus) 3 내부 독립 분석 + GPT (cross-vendor) + Claude (인접 컨텍스트, 메타 면책 명시) 외부 LLM 2건 + Reviewer 종합 합의. **5/5 입력 APPROVE WITH CONDITIONS — Design/Governance Gate PASS (Bundled)**. P0 3건 (PASS 범위 한정 / GP-2~GP-6 IMPLEMENTATION PENDING / 외부 LLM 1+ 충족) + P1 10건 + P2 일부. Implementation/Runtime PASS / Hermes PMO 격상 / P2 v3 정식 채택 / ADR 자동 갱신 모두 본 합의 범위 외 (사용자 명시 답습) | `external-review/2026-05-09-g2g3g4-promotion-request.md`, `external-review/2026-05-09-g2g3g4-promotion-response.md` (GPT), `external-review/2026-05-09-g2g3g4-promotion-response-claude.md` (Claude), `review/agents-2026-05-09-g2g3g4/agent-a-implementation.md`, `agent-b-security.md`, `agent-c-alternatives.md`, `review/3plus1-consensus-2026-05-09-g2g3g4-formal-promotion.md` |
| 2026-05-09 (후속) | **G2/G3/G4 정식 PASS 헤더 갱신 + CONTEXT/INDEX 갱신 (P0 조건 C-A + C-B 흡수)** — 3 게이트 헤더 DRAFT → "Design/Governance Gate PASS (Bundled, 2026-05-09)" + Implementation/Runtime PASS 미포함 명시 + GP-2~GP-6 / G3 운영 / G4 라운드트립 = "DESIGN PASS / IMPLEMENTATION PENDING" 표기. CONTEXT.md 4 게이트 표 갱신 + 다음 세션 TODO 갱신 (P1 흡수 PR 묶음 결정 → P2 v3 정식 채택 합의 형태 결정) | `architecture/governance-preconditions.md`, `architecture/hermes-not-root-of-trust-runtime.md`, `architecture/provider-agnostic-memory-skill-design.md`, `CONTEXT.md`, `INDEX.md` |
| 2026-05-09 (후속 2) | **P1 분류 + PR 묶음 형태 결정 (옵션 β 채택)** — 사용자 명시 결정 3건: PR 묶음 = 옵션 β (PR-1 단축 합의 본문 6건 + PR-2 풀 3+1 ADR-012/G4 hash chain) / 검토 형태 = 본문 단축 / 신규 ADR 풀 3+1 + 외부 LLM 1+ / 외부 LLM 추가 시점 = P1 흡수 후 + P2 v3 진입 전 (Claude C-3). P1 10건 분류 매트릭스 + 별도 후속 (C-H Implementation / C-N ADR-009) | `sessions/SESSION_2026-05-09.md` (§11), `CONTEXT.md` |
| 2026-05-09 (후속 2) | **PR-1 본문 흡수 6건 (C-D / C-E / C-F / C-I / C-K / C-L)** — C-D: G3 §2.5 보호 대상 enumeration (Git/CI/external-review/Evidence/ADR/SDD/gate 정의 등 15건). C-E: G3 §4.7 메타-순환 청산 (4 사례 + 4 청산 원칙). C-F: G3 §5.5 + G2 §9.5 SPOF accepted risk (1인 동일 호스트 의도적 수용 + 5 multi-host 트리거). C-I: G2 §1.2.5 P9~P12 deferred candidates (prompt injection / evidence forgery / supply-chain / memory poisoning + P13/P14). C-K: G4 §3.1 + §3.6 MVP 필수/권장/후속 분리 + #15 provider_bindings 권장→필수 격상 + #11 required_evidence MVP-필수. C-L: G4 §11.4 P-1~P-5 + §11.4.3 G3 4건 잔여 처리 (G3 4건 모두 흡수, G4 4건 PR-2 또는 별도) | `architecture/governance-preconditions.md`, `architecture/hermes-not-root-of-trust-runtime.md`, `architecture/provider-agnostic-memory-skill-design.md` |
| 2026-05-09 (후속 2) | **PR-1 단축 합의 보고서 APPROVE (Reviewer-only)** — 8 기준 8/8 PASS (각 흡수 항목 충실성 6 + 8 금지 위반 0건 + 메타 편향 5 통제) + G3 4건 후속 권고 본 PR-1 모두 흡수 + G4 P-4 본 PR-1 흡수 + G4 P-1/P-2/P-3 PR-2 영역 + G4 P-5 Implementation/Runtime 별도. 본 합의 = G2/G3/G4 정식 PASS 합의 §11.2 P1 조건 권위 *내부* 작업 → 외부 LLM 별도 회수 불필요 (사후 충족 G3 §4.7.1 (a) 답습). 다음 진입점: PR-2 풀 3+1 (ADR-012 + G4 hash chain) | `review/3plus1-consensus-2026-05-09-p1-doc-absorption.md` |
| 2026-05-09 (후속 3) | **PR-2 풀 3+1 합의 + 외부 LLM 2건 (cross-vendor + Claude 인접 컨텍스트) APPROVE WITH CONDITIONS — Design/Governance Gate 권위 격상 적격** (5/5 입력 일치). 외부 LLM 의뢰 자료에 *내부 Agent A/B/C 분석 미포함* (편향 통제 강화) + Agent A (구현/운영, 8 조건, R-6/R-7/R-11 HIGH binary) + Agent B (보안/거버넌스, 4 + 14 NOTES, **Gap-17 HIGH** Hermes 변조 차단 매트릭스 4항목) + Agent C (대안/단순화, 4 핵심 + 6 보조) + cross-vendor 외부 LLM (5 권고 + 16 차원, 11번째 = `event` + JCS primary + jq fallback) + Claude 인접 컨텍스트 (17 조건 C-1~C-17, 다층 동시 의무 + C-14 cross-vendor P2 v3 진입 전 의무) + Reviewer 종합. 5/5 영구 핵심 제약 보호 HIGH | `external-review/2026-05-XX-pr2-evidence-ledger-request.md`, `external-review/2026-05-09-pr2-evidence-ledger-response.md` (cross-vendor), `external-review/2026-05-09-pr2-evidence-ledger-response-claude.md` (Claude 인접), `review/agents-2026-05-09-pr2-evidence-ledger/agent-a-implementation.md` (481 줄), `agent-b-security.md` (597 줄), `agent-c-alternatives.md` (424 줄), `review/3plus1-consensus-2026-05-09-pr2-evidence-ledger.md` |
| 2026-05-09 (후속 3) | **ADR-012 신규 발행 — Evidence Ledger Protection** (Evidence Ledger 보호 강화). 12 보호 원칙 + 4 매트릭스 + 5 추가 의무. 11 필드 (10 → 10 + `event`) + 17 enum 후보 (MVP 12 의무) + Layer 1~5 다층 강제 (Hash chain MANDATORY + Git append-only MANDATORY + Signed RECOMMENDED + CI 회귀 + External anchor RECOMMENDED) + RFC 8785 JCS Primary + `jq -S -c` Fallback + Genesis hash MVP+0.2 전이 + prev_hash 검증 실패 BLOCK + manual + chain_violation_detected + Full Rewrite 5 Layer 방어 + Round-trip Tier-based (T2 strict / T3 의미 보존) + 3 ledger entry 형식 + Migration BLOCK + manual + migration_failed entry + Hermes 변조 차단 매트릭스 4항목 (Gap-17) + External LLM response `agent="user"` 강제 + Schema 진화 정책 (semver MAJOR/MINOR) + Content-level forgery 한계 명시 + Timestamp monotonicity + 운영 부담 monitoring trigger + Provider Liquidity 4-way → **5-way** Multi-layer Defense. ADR-011 §2.1 (a)~(d) + (e) 5조건 답습. P10 (Evidence Forgery) 정식 등록 *트리거* (G2 §1.2 본문 row 추가는 별도 G2 update PR) | `decisions/ADR-012-evidence-ledger-protection.md` |
| 2026-05-09 (후속 3) | **G4 §4.2 schema 11 필드 갱신 + §4.4 hash chain 사양 보강 + §4.6 round-trip 검증 절차 보강** (ADR-012 동일 PR commit). §4.2 = 10 → 11 필드 (`event` 신규, 17 enum 후보) + provider-neutral 강제 + timestamp monotonicity. §4.4 = Layer 1~5 다층 강제 본문 + Canonical JSON RFC 8785 JCS Primary + jq fallback + 구현 라이브러리 후보 (Python/Node/Go) + Test corpus 의무 + Genesis Hash MVP+0.2 전이 + prev_hash 검증 실패 BLOCK + chain_violation_detected entry + Full Rewrite 5 Layer 방어. §4.6 = Tier-based 검증 + 3 ledger entry 형식 (`roundtrip_pass`/`lossy`/`fail`) + 자동화 vs 사용자 review 분리 + JSONL Export/Import 무결성 + Migration 검증 실패 rollback (BLOCK + manual + `event: migration_failed`). G4 §11.4 P-1 (RFC 8785 JCS) + P-2 (schema 진화) + P-3 (import schema_version) 처리 완료 | `architecture/provider-agnostic-memory-skill-design.md` (§4.2 / §4.4 / §4.6) |
| 2026-05-09 (후속 4) | **C-14 cross-vendor blind 의뢰 + 응답 2건 (cross-vendor + Gemini 사고모델) APPROVE WITH CONDITIONS** — P2 v3 정식 채택 합의 진입 *전* 사전 검토. 의뢰 자료 *blind 강도 가장 높음* (내부 Agent / Reviewer / 사용자 선호 / APPROVE 유도 / 다른 외부 LLM 응답 모두 의도적 미포함). 응답 1 (vendor 자기 명시 부재) = 7 핵심 조건 (§3 dual-structure / Design Adoption only / Hermes PMO non-activation clause / ADR-012+G4 cross-ref / 5 영구 제약 보존 / Implementation Pending 표 / 풀 3+1). 응답 2 (Gemini 사고모델) = 4 핵심 조건 (상태표 동기화 / ADR-012 완전 통합 / **격상 전 인간 리뷰 의무화** / Archived 영구 제약 계승). 양 응답 일치: APPROVE WITH CONDITIONS / 풀 3+1 합의 형태 권고 / DESIGN PASS / IMPLEMENTATION PENDING 명시 의무. C-14 의뢰 의무 충족 → P2 v3 정식 채택 합의 진입 적격. **11 핵심 조건 = P2 v3 정식 채택 풀 3+1 합의 전 체크리스트 (CONTEXT.md 추적)** | `external-review/2026-05-09-c14-cross-vendor-p2v3-pre-adoption-request.md`, `external-review/2026-05-09-c14-cross-vendor-p2v3-pre-adoption-response.md` (vendor 미명시), `external-review/2026-05-09-c14-cross-vendor-p2v3-pre-adoption-response-gemini.md` (Gemini 사고모델) |
| 2026-05-09 (후속 4) | **C-N ADR-009 갱신 단축 합의 APPROVE (Reviewer-only)** — 5 영역 흡수: (1) **P1 facade MVP 진입조건 명시** (§2 신설 — 4 충족 조건 (a)~(d) 모두 2026-05-04 시점 충족, 별도 트리거 없음, 6 의무 매커니즘 명시) + (2) **Hermes PMO ↔ provider 분리** (§2.3 신설 — 7 영역 권한 매트릭스, ADR-011 §2.3 + ADR-008 차단조건 #4 + ADR-012 §원칙 6 + 헌법 5조 답습, Hermes PMO 격상 후에도 영구 유지) + (3) **Provider Liquidity 5-way Multi-layer Defense 모법 ADR 권위 확정** (§5 신설 — Layer 1 = 본 ADR-009, ADR-012 §원칙 5 발행 권위 답습) + (4) **v2.0 트리거 vs MVP 조건 분리** (§3.0 신설, **자체 Adapter v2.0 트리거 T1~T4 본문 변경 0건**, **핵심 결정 옵션 B 채택 변경 0건** — 단축 합의 적격) + (5) **P2 v3 cross-reference** (§9.4 신설 — P2 v3 §1.6 / §2.3 / §6 / §10 인용 가능). 5/5 PASS + 5 통제 답습 | `decisions/ADR-009-self-adapter-v2-entry-conditions.md`, `review/3plus1-consensus-2026-05-09-c-n-adr-009-update.md` |
| 2026-05-09 (후속 5) | **G2 §1.2 P10 (Evidence Forgery) 정식 row 등록 단축 합의 APPROVE (Reviewer-only)** — 3 영역 갱신: (1) §1.2.3 정식 위반 경로 합산 갱신 (8 → 9건, P1~P8 + **P10**, 분류 카테고리 추가 — 헌법 8조 / Provider Liquidity / **Evidence Integrity**). (2) §1.2.5 P10 deferred row 갱신 (deferred → 정식 등록 완료 §1.2.6 답습, 2026-05-09 후속 5). (3) **§1.2.6 신설** (Evidence Integrity 위반 경로 1건 P10 정식 등록) — P10 시나리오 (5 위장 형태 + 5 측면) + ADR-012 §2.1~§3.5 + G3 §5 + G4 §4.2/§4.4/§4.6 cross-reference + P10 enforcement layer 매핑 (Layer 1~5 + Hermes 변조 차단 매트릭스 4항목 + External LLM `agent="user"` 강제) + 처리 범위 (Status / Implementation Pending / GP 매핑 별도 합의) + 합의 권위 (단축 합의 적격 + **4 풀 3+1 승격 트리거 0건 발화**) + 11 *하지 않는* 것. ADR-012 발행 권위 *내부* 작업, P2 v3 정식 채택 합의 진입 마지막 사전 작업 완료 | `architecture/governance-preconditions.md` (§1.2.3 / §1.2.5 / §1.2.6), `review/3plus1-consensus-2026-05-09-g2-p10-evidence-forgery.md` |
| 2026-05-09 (후속 6) | **P2 v3 (Hermes Adoption Design v3) 정식 채택 풀 3+1 + 외부 LLM 2건 (cross-vendor — Gemini 사고모델 + vendor 미명시) APPROVE WITH CONDITIONS — Design Adoption only** (5/5 입력 일치). 9 입력 모두 반영 (C-14 응답 2건 + C-14 11 조건 + ADR-012 + G4 §4 보강 + ADR-009 C-N + G2 §1.2.6 P10 + G1b PASS + G2/G3/G4 Design/Governance Gate PASS + PR-1/PR-2/C-N/P10 흡수). Agent A 15 조건 (P0 4 HIGH binary) + Agent B 12 CONDITIONS + 14 Gap (HIGH 8건, Gap-13 종합) + Agent C 8 조건 (Alt-1 즉시 채택 + 본문 최소 갱신 + 후속 PR 분리) + cross-vendor 외부 LLM 7 조건 (vendor 미명시) + Gemini 사고모델 4 조건. 5/5 영구 핵심 제약 보호 HIGH | `external-review/2026-05-09-c14-cross-vendor-p2v3-pre-adoption-{request,response,response-gemini}.md`, `review/agents-2026-05-09-p2v3-formal-adoption/{agent-a-implementation,agent-b-security,agent-c-alternatives}.md`, `review/3plus1-consensus-2026-05-09-p2v3-formal-adoption.md` |
| 2026-05-09 (후속 6) | **P2 v3 본문 갱신 (DRAFT → Adopted, Design Adoption only) — 8 본문 영역** — (1) §0 헤더 갱신 (DRAFT → Adopted, Design Adoption only 의미 제한, 정식 채택 합의 권위 명시) + (2) §2 Hermes PMO Non-Activation Clause 강화 (한국어 + cross-vendor 영문 권고 답습) + (3) **§3 dual-structure** (§3.1.1 DRAFT Snapshot 2026-05-07 사실 보존 + §3.1.2 Adoption-time Status 2026-05-09 후속 6 + §3.1.3 Delta 7 evidence Δ-1~Δ-7 + §3.1.4 Implementation Pending 표) + (4) §6 G4 **ADR-012 Mandatory Reference** + ADR-009 C-N + Provider Liquidity 5-way Layer 5 cross-reference + (5) §7 ADR 매트릭스 갱신 (ADR-012 + ADR-009 C-N row 추가, 본 합의 후 별도 PR 영역 명시) + (6) **§10 Normative Constraints 격상** (5/5 영구 제약 표 + Multi-layer 보호 5/5 매트릭스) + **§10.2 Archive Migration Note** (영문 + 한국어, archive 후 권위 보존) + (7) §11 변경 절차 갱신 (Hermes PMO 격상 = 풀 3+1 + 외부 LLM 2개 또는 외부 LLM 1개 + 인간 전문 리뷰 + 사용자 명시 + Adoption decision commit + Evidence Ledger entry 의무) + **§11.1 Hermes PMO 격상 전 인간 전문 리뷰 (Human-in-the-loop) 의무 명문화** (Gemini 사고모델 §7.10 #3 직접 인용) + (8) §2.6 격상 절차 단계 5.5 인간 리뷰 신설 + §2.6.1 PMO 격상 체크리스트 신설 (12 조건 enumeration) + §9.1 미발생 사항 + §9.2 별도 PR 우선순위 8건 + §9.3 다음 세션 진입점 후보 갱신 + §0.3 정식화 절차 시점 갱신 (단계 4 = ✅ 본 commit) | `architecture/hermes-adoption-design-v3.md` (DRAFT → **Adopted (Design Adoption only)**, 8 본문 영역 갱신) |
| 2026-05-09 (후속 7) | **P2 v2 (`hermes-adoption-design.md`) Archive 적격성 검토 + Archive 전환 단축 합의 APPROVE (Reviewer-only)** — 7/7 검토 기준 PASS (P2 v3 정식 채택 / carry-over 23 영역 = 22 + 1 갱신 / 폐기 가정 5 권위 위치 명시 / ADR 5건 cross-reference 깨짐 0 / PMO 격상 오해 0 / Implementation PASS 오해 0 / 5 영구 제약 보호 HIGH 5/5) + 5/5 풀 3+1 승격 트리거 0건 발화 (carry-over 누락 / ADR 참조 깨짐 / PMO 격상 오해 / 5 제약 약화 / Implementation Pending 흐려짐) + **옵션 A (최소 침습 — 헤더 갱신 + 본문 보존, path 변경 0건) 채택**. ADR-008 / 009 / 010 / 011 / 012 cross-reference 영향 0건. P2 v3 §10.2 Archive Migration Note + ADR-012 §605 답습. system-identity-prequel.md archive 는 별도 작업 분리 (사용자 명시 답습) | `architecture/hermes-adoption-design.md` (헤더 갱신 — 확정 → **Archived**), `review/3plus1-consensus-2026-05-09-p2-v2-archive-decision.md` |
| 2026-05-09 (후속 8) | **system-identity-prequel.md Archive 적격성 검토 + Archive 전환 단축 합의 APPROVE (Reviewer-only)** — 8/8 검토 기준 PASS (P2 v3 정식 채택 / 핵심 내용 이관 16 영역 = 12 완전 흡수 + 4 부분/분산 / 5 영구 제약 보존 HIGH 5/5 / PMO 격상 오해 0 / Implementation PASS 오해 0 / Archive Migration Note 4 조건 모두 충족 / ADR-008/009/010/011/012 + INDEX/CONTEXT cross-reference 깨짐 0 / **AI Dev Company OS 정체성 보존 HIGH**) + 6/6 풀 3+1 승격 트리거 0건 발화 (이관 불완전성 / 5 제약 약화 / 정체성 재정의 근거 사라짐 / PMO 격상 오해 / Design Adoption ↔ Implementation PASS 혼동 / ADR INDEX CONTEXT 참조 깨짐) + **옵션 A (최소 침습 — 헤더 갱신 + 본문 보존, path 변경 0건) 채택**. **prequel §1.2 자체 archive 예고 정합** ("P2 v3 작성 완료 시 → 본 문서 archived 처리"). ADR-011 §2.3 / §2.4 영구 권위 승격 답습 + ADR-012 §6.4 트리거 실현 답습 + P2 v3 §10.2 Archive Migration Note 직접 답습. **§2 정체성 선언 / §2.2 메타포 매핑 / §2.3 핵심 명제 = prequel 본문 보존으로 직접 권위 출처 영구 보존** (옵션 A 핵심 가치) | `architecture/system-identity-prequel.md` (헤더 갱신 — 임시 선언 → **Archived**), `review/3plus1-consensus-2026-05-09-system-identity-prequel-archive-decision.md` |
| 2026-05-09 (후속 9) | **ADR-008 / 010 / 011 본문 갱신 PR 묶음 *범위 결정* 단축 합의 APPROVE (Reviewer-only)** — 사용자 명시 6 항목 분류 (반영 내용 / 단순 cross-ref vs 결정 변경 / 단축 vs 풀 / ADR-012/P2 v3/G2/G3/G4 참조 관계) + 6/6 풀 3+1 승격 트리거 0건 발화 (3 ADR 결정 변경 / 5 제약 약화 / PMO 격상 오해 / Implementation PASS 오해) + **옵션 1 (3 ADR 단일 PR 묶음) 권고**. 25 cross-reference 갱신 항목 enumeration (ADR-008 A1~A9 9건 + ADR-010 A10~A13 4건 + ADR-011 A14~A25 12건). **3 ADR 모두 결정 내용 변경 0건** (Option B / Vault HSM / 수단/목적 분리 / G1a-G1b / Hermes ≠ root of trust / T1-T2-T3 모두 영구 권위 답습). **본 검토 = 범위 결정만, 본문 수정 X — 별도 PR/commit (사용자 명시 답습)** | `review/3plus1-consensus-2026-05-09-adr-008-010-011-update-scope-decision.md` |
| 2026-05-09 (후속 10) | **ADR-008 / 010 / 011 본문 갱신 단일 PR 묶음 commit (옵션 1 답습)** — 25 cross-reference 갱신 항목 (A1~A25) 모두 반영. **ADR-008** = §관련 문서 9 항목 (P2 v2 Archived 표기 / P2 v3 Adopted 신규 row / ADR-009 C-N + ADR-011 + ADR-012 cross-reference / G2/G3/G4 정식 산출 cross-reference / 차단조건 #2 (JSONL export) Mandatory Reference / 차단조건 #4 (P1 Facade) Hermes PMO ↔ provider 분리 / 부록 B §B.6 G1b PASS + G2 GP-1 흡수 표기). **ADR-010** = §맥락 §11 + §관련 문서 4 항목 (P2 v2 Archived / P2 v3 Adopted / ADR-012 / **Evidence Ledger DB Secret 처리 주의 사항** — Hermes SQLite + Memory DB + Skill DB + Evidence Ledger DB 모두 SQLCipher Vault 보호 범위 명시 포함, ADR-012 §원칙 5 + 외부 LLM 2 C-1 답습). **ADR-011** = §8.1 (prequel Archived) + §8.2 (P2 v2 Archived + P2 v3 Adopted 신규) + §8.5 12 항목 (R-4~R-7 ✅ 완료 + G1b PASS + G2/G3/G4 PASS + ADR-012 발행 + ADR-009 C-N + G2 §1.2.6 P10 + P2 v3 + P2 v2/prequel Archived + 본 후속 9 모두 등록). **결정 내용 변경 0건** + 6 풀 3+1 승격 트리거 0건 발화 (재확인) + 6 금지 사항 위반 0건 (Hermes PMO 격상 / Runtime PASS / G2/G3/G4 Implementation PASS / ADR 결정 변경 / P2 v3 정식 채택 재해석 / runtime code 모두 0건) | `decisions/ADR-008-hermes-adoption-decision.md` (§관련 문서 갱신), `decisions/ADR-010-sqlcipher-vault-key-management.md` (§맥락 + §관련 문서 갱신), `decisions/ADR-011-means-vs-ends-redaction.md` (§8 갱신) |
| 2026-05-09 (후속 11) | **G2 / G3 / G4 헤더 P2 v3 cross-reference 갱신 단축 PR** — 3 게이트 헤더 영역 cross-reference 보강. **G2** = §1.2.6 P10 정식 등록 명시 + P2 v3 §4 답습 권위 + P2 v3 §3.1.4 Implementation Pending 표 + P2 v3 §10.1 Normative Constraints + §10.2 Archive Migration Note + §11.1 인간 전문 리뷰 의무화 + ADR-009 C-N + ADR-012 cross-reference + 후속 권위 표기 (P2 v2 Archived / prequel Archived). **G3** = **Hermes 변조 차단 매트릭스 4항목** (ADR-012 §2.12 답습 — Hermes-originated ledger entry / 파일 변조 / git commit / 외부 LLM 응답 위조) + P2 v3 §5 답습 권위 + §2.1.2 + §2.2 + §10.1 #2 (Hermes ≠ root of trust 5 layer 보호) + §11.1 + ADR-009 C-N §2.3 + ADR-012 §2.12 + ADR-011 §2.3/§2.4 영구 권위 직접 명시 + prequel §3 → ADR-011 §2.3 영구 승격 답습 (archive 후 권위 보존). **G4** = **ADR-012 Mandatory Reference** (§4.2 11 필드 + §4.4 Layer 1~5 + §4.6 Tier-based round-trip 권위 출처 = ADR-012 §2.1~§3.5) + Provider Liquidity 5-way Layer 매트릭스 (ADR-009 C-N §5 Layer 1 모법 + ADR-012 §원칙 6 Layer 5) + P2 v3 §6 답습 권위 + §10.1 #1 + §10.2 + §11.1. **5 풀 3+1 승격 트리거 0건 발화** (Design vs Implementation 분리 / PMO 격상 오해 / P2 v3 의미 변경 / ADR 충돌 / 5 제약 약화). 본 갱신 = cross-reference 보강만, 게이트 PASS 상태 / Design ↔ Implementation 분리 변경 0건 | `architecture/governance-preconditions.md` (헤더 갱신), `architecture/hermes-not-root-of-trust-runtime.md` (헤더 갱신), `architecture/provider-agnostic-memory-skill-design.md` (헤더 갱신) |
| 2026-05-09 (후속 12) | **ADR-013 / 014 후보 발행 결정 검토 단축 합의 APPROVE (Reviewer-only)** — 두 후보 *현 시점 발행 보류* 권고. 7 항목 분류 (필요 이유 / 기존 ADR 커버 / Implementation 처리 / 격상 전후 / 합의 형태) + 4+4 새 ADR 기준 (필요 4 + 불필요 4) 평가 + 5 풀 3+1 승격 트리거 0건 발화 (격상 절차 변경 / Human review 의무 변경 / Provider Liquidity·Evidence Integrity 변경 / 새 영구 제약 / ADR-008~012 충돌). **ADR-013 후보** (Hermes PMO Activation / Human Review / Runtime Governance) = P2 v3 §2.6 + §11.1 + §2.6.1 + ADR-008 부록 B + ADR-011 §2.3/§2.4 + ADR-009 C-N §2.3 + ADR-012 §2.12 = **7 권위 layer 중첩 답습 충족** → **ADR-008 본문 갱신 PR (부록 추가) 으로 대체 가능**. **ADR-014 후보** (Memory/Skill Runtime / Migration / Round-trip) = G4 §4.5 + §4.6 + ADR-012 §2.10 답습 충족 + **Implementation/Runtime PASS PoC 완료 *후* 발행 검토** (PoC 전 발행 = ADR-011 §2.1 (b) 패턴 위반). **본 검토 = 후보 결정만, 본문 작성 X**. 현 시점 발행 불필요 영역 9건 + Implementation 작업 영역 8건 + 격상 후 영역 6건 enumerate. 발행 시점 후보 ADR-013 a/b/c (격상 시점 / Implementation PASS 후 / 외부 LLM 권고) + ADR-014 a/b/c (Implementation PASS 후 / Schema MAJOR 변경 / Tier-2/3 확장). 발행 시 풀 3+1 + 외부 LLM 1+ 의무 명시 | `review/3plus1-consensus-2026-05-09-adr-013-014-candidate-decision.md` |
| 2026-05-09 (후속 13) | **ADR-008 본문 갱신 PR — 부록 C 신설 (Hermes PMO Activation Cross-Reference) 단축 합의 APPROVE (Reviewer-only)** — 사용자 명시 7 항목 답습 + 6 풀 3+1 승격 트리거 0건 발화. **ADR-013 신규 발행 *대체* 권위 정착** — 8 권위 layer 중첩 답습 (P2 v3 §2.6 + §11.1 + §2.6.1 + 본 부록 C + ADR-008 부록 B + ADR-011 §2.3/§2.4 + ADR-009 C-N §2.3 + ADR-012 §2.12). 부록 C 구조: §C.1 의미 (오해 방지 — Hermes PMO 격상 선언 *아님*) + §C.2 P2 v3 §2.6.1 12 조건 체크리스트 직접 답습 (현 상태 2/12 충족) + §C.3 외부 LLM 2 + 인간 전문 리뷰 조건 (P2 v3 §11 + Gemini §7.10 #3 답습) + §C.4 자동 격상 절대 금지 (5 layer 다중 차단 매트릭스 — ADR-011 §2.4 T3 + ADR-012 §원칙 9 + ADR-009 C-N §2.3 + ADR-012 §2.12 + G3 §2.5 #11/§4.5/§2.2 #20) + §C.5 Implementation/Runtime PASS ↔ Design/Governance PASS 분리 매트릭스 (Design 4/4 + Implementation 2/4 G1b+GP-1) + §C.6 ADR-013 보류 사유 (8 권위 layer 답습) + §C.7 cross-reference 매트릭스 (12 권위) + §C.8 발생/미발생 enumerate. **ADR-008 §결정 본문 변경 0건** (Option B / 6 차단조건 / 단계 마이그레이션 / 부록 B Amendment 모두 변경 없음) | `decisions/ADR-008-hermes-adoption-decision.md` (부록 C 신설), `review/3plus1-consensus-2026-05-09-adr-008-update-pmo-activation-cross-ref.md` |

---

## AI 에이전트를 위한 안내

이 프로젝트에서 개발을 도울 때:

1. **반드시 준수**: `PROJECT_CONSTITUTION.md` (헌법)
2. **설계 참고**: `docs/architecture/` 폴더의 설계 문서들
3. **코딩 스타일**: `DEVELOPMENT_GUIDE.md` 참고
4. **아이디어 검증**: 반드시 3+1 에이전트 합의 프로토콜 적용

**변경 사항 발생 시**:
- 관련 문서 업데이트 필수
- 이 INDEX.md의 업데이트 이력에 기록

---

**이 문서는 프로젝트의 모든 문서를 안내하는 인덱스입니다.**
**새로운 문서 추가 시 반드시 이 파일도 업데이트하세요.**
