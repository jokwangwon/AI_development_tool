# AI Development Tool — AI 자동화 개발 방법론 템플릿

> **하네스 엔지니어링 + SDD + TDD + 3+1 멀티에이전트 합의 기반 AI 자동화 개발 프레임워크**
>
> **v1.0.0** | 새 프로젝트에 복사하여 즉시 사용

---

## 이 프로젝트는 무엇인가

**개발 방법론 템플릿**이다. 새 아이디어로 프로젝트를 시작할 때, 이 파일들을 가져와 적용하면 체계적인 자동화 개발을 진행할 수 있다.

```
사용법:
  1. 새 프로젝트 디렉토리 생성
  2. 이 템플릿의 파일을 복사
  3. Claude에게 아이디어를 제시
  4. Phase 0 → 1 → 2 → 3 → 4 자동화 개발 진행
```

---

## 핵심 가치

| 가치 | 설명 |
|------|------|
| **Specification First** | 코드보다 명세가 먼저 (SDD) |
| **Test First** | 구현보다 테스트가 먼저 (TDD) |
| **Harness First** | 잘못하는 것이 불가능하게 만들어라 |
| **Multi-Agent Consensus** | 중요 결정은 3+1 에이전트 합의로 검증 |
| **Zero Hardcoding** | 모든 설정은 환경 변수, Docker-First |

---

## 개발 파이프라인

```
사용자 아이디어
    │
    ▼
Phase 0: 자동화 검토 질문지          [ADR-001]
    → 아이디어 자동 구조화 + 최소 질문 (필수3 + 동적2)
    → 구조화된 아이디어 브리프 출력
    │
    ▼
Phase 1: 3+1 에이전트 합의 (통합)    [ADR-002]
    → 아이디어 검증 + 기술 스택 결정 + 에셋 식별
    → Agent A(구현) / B(품질) / C(대안) → Reviewer(합의)
    │
    ├─── Phase 2: SDD 설계 문서 작성
    │    → 확정된 스택 기반 명세 작성
    │
    ├─── Phase 3: TDD 구현
    │    → RED → GREEN → REFACTOR
    │
    └─── 에셋 파이프라인 (병렬)       [ADR-003]
         → Guide-First: 최적 AI 모델 탐색 + 안내
    │
    ▼
Phase 4: 통합 테스트 + 배포
```

---

## 포함된 설계 체계 (v1.0.0)

### 헌법 + 원칙
| 문서 | 설명 |
|------|------|
| `docs/constitution/PROJECT_CONSTITUTION.md` | 12개 조항 프로젝트 헌법 |
| `docs/constitution/ARCHITECTURE_PRINCIPLES.md` | 아키텍처 10대 원칙 |
| `docs/constitution/CODE_QUALITY_PRINCIPLES.md` | 코드 품질 원칙 |

### 아키텍처 설계 (6개 ADR)
| 문서 | ADR | 핵심 |
|------|-----|------|
| `automated-review-questionnaire-design.md` | ADR-001 | Phase 0: 아이디어 → 브리프 |
| `idea-driven-stack-decision-design.md` | ADR-002 | Phase 1: 아이디어가 스택을 결정 |
| `generative-ai-asset-pipeline-design.md` | ADR-003 | 비코드 에셋 Guide-First 생성 |
| `generative-ai-extensibility-design.md` | ADR-004 | 모델 교체/학습 Config 기반 |
| `ai-backend-stack-convention.md` | ADR-005 | 로컬 추론 시 Python 분리 |
| `environment-and-docker-design.md` | ADR-006 | 하드코딩 제로 + Docker-First |

### 가이드
| 문서 | 설명 |
|------|------|
| `CLAUDE.md` | AI 에이전트 개발 지시사항 (매 세션 자동 로드) |
| `docs/guides/DEVELOPMENT_GUIDE.md` | 개발 프로세스, Git 규칙 |
| `docs/guides/TEST_STRATEGY.md` | 테스트 전략 (70% 커버리지) |

### 하네스 인프라
| 파일 | 설명 |
|------|------|
| `.claude/settings.json` | Claude Code Hook 설정 |
| `.githooks/pre-commit` | 시크릿/디버그 코드 감지 |
| `.githooks/setup.sh` | Git hooks 초기 설정 |
| `.gitignore` | 표준 무시 규칙 |

---

## 새 프로젝트에서 사용하기

### 1. 복사

```bash
# 새 프로젝트에 템플릿 파일 복사
cp -r AI_development_tool/* /path/to/new-project/
cp -r AI_development_tool/.claude /path/to/new-project/
cp -r AI_development_tool/.githooks /path/to/new-project/
cp AI_development_tool/.gitignore /path/to/new-project/
```

### 2. 초기 설정

```bash
cd /path/to/new-project
git init
bash .githooks/setup.sh     # Git hooks 활성화
cp .env.example .env         # 환경 변수 생성 (API 키 설정)
```

### 3. 아이디어 제시

Claude에게 아이디어를 제시하면 Phase 0부터 자동 시작:

```
사용자: "실시간 채팅 앱을 만들자. WebSocket 기반, 읽지 않은 메시지 알림 포함"

→ Phase 0: 검토 질문지 자동 실행
→ Phase 1: 3+1 합의 (아이디어 + 스택 + 에셋)
→ Phase 2: SDD 작성
→ Phase 3: TDD 구현
→ Phase 4: 통합 + 배포
```

### 4. Docker 실행

```bash
docker compose up            # 기본 실행
docker compose --profile gpu up  # GPU 포함 (AI 백엔드)
```

---

## v1.0.0 알려진 제한사항

Phase 0~1(아이디어 구조화 + 합의)은 상세 설계 완료. 아래 항목은 프로젝트별로 구현:

- Phase 2~3 자동 변환 (합의→SDD→테스트→코드)
- 복합 기능 분해 메커니즘
- 런타임 AI 코드 패턴
- 프로젝트 스캐폴딩 자동화
- 실동작 CI Pipeline

---

## 참고 자료

| 주제 | 링크 |
|------|------|
| 하네스 엔지니어링 | [Martin Fowler](https://martinfowler.com/articles/harness-engineering.html) |
| 하네스 설계 | [Anthropic](https://www.anthropic.com/engineering/harness-design-long-running-apps) |
| Claude Code | [Docs](https://code.claude.com/docs/en/how-claude-code-works) |
| SDD | [Agent Factory](https://agentfactory.panaversity.org/docs/General-Agents-Foundations/spec-driven-development) |

---

**버전**: v1.0.0
**작성일**: 2026-04-06
**라이선스**: MIT
