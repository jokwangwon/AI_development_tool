# 문서 인덱스 (Documentation Index)

> **프로젝트 문서 전체 구조 및 읽는 순서**

**최종 업데이트**: 2026-05-06

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
│   └── change-impact-analysis-design.md         # 변경 영향 분석
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
