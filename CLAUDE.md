# CLAUDE.md — AI 자동화 개발 도구 프로젝트 지시사항

> Claude Code가 매 세션마다 자동으로 읽는 프로젝트 규칙 문서

---

## 1. 핵심 개발 방법론: SDD + TDD

### SDD (Specification-Driven Development)

- **코드보다 문서가 우선**. 코드 변경 전 관련 SDD 문서 확인 필수
- SDD 문서 경로: `docs/architecture/` 하위 명세서 참조
- 문서와 코드 간 불일치 발견 시 → 문서를 기준으로 코드 수정
- **작업 전 필수 워크플로우**:
  1. 관련 설계/명세 문서가 있는지 확인
  2. **문서가 없으면** → 설계 문서를 먼저 작성하고 사용자 검토를 받음
  3. **문서 검토 완료 후** → 별도 브랜치에서 코드 구현 (TDD 적용)
  4. 구현 완료 후 → 문서에 변경사항 반영

### TDD (Test-Driven Development)

- **모든 코드 작성 시 TDD 사이클 적용 필수**
  1. RED: 실패하는 테스트 먼저 작성
  2. GREEN: 테스트를 통과하는 최소한의 코드 구현
  3. REFACTOR: 코드 정리 (테스트는 계속 통과해야 함)
- 테스트 커버리지 목표: **70% 이상**

---

## 2. 하네스 엔지니어링 규칙

> "에이전트에게 하라고 말하지 말고, 잘못하는 것이 불가능하게 만들어라"

### 핵심 공식

```
Agent = Model + Harness
```

모델은 추론을 제공하고, 하네스는 나머지 전부를 제공한다:
도구, 메모리, 권한, 오케스트레이션, 안전 경계, 검증 루프, 라이프사이클 관리.

### 가이드(Feedforward) vs 센서(Feedback)

| 구분 | 가이드 (사전 조향) | 센서 (사후 검증) |
|------|-------------------|-----------------|
| 역할 | 에이전트 행동을 미리 방향 설정 | 에이전트 출력을 사후 검증 |
| 유형 | CLAUDE.md, 설계 문서, 스킬 정의, 프롬프트 | 린터, 타입 체커, 테스트, 코드 리뷰 에이전트 |
| 특성 | 결정적(deterministic) 우선 | 계산적(computational) 우선, 추론적(inferential) 보조 |

### 피드백 루프 계층

| Layer | 수단 | 속도 | 수준 |
|-------|------|------|------|
| 0 | 이 CLAUDE.md | ~0ms | 권고 (가이드) |
| 0.5 | 자동화 검토 질문지 | ~30s | 아이디어 구조화 (가이드) |
| 1 | PostToolUse Hook (자동 lint) | ~500ms | 강제 피드백 (센서) |
| 2 | PreCommit Hook (테스트) | ~10s | 강제 차단 (센서) |
| 3 | git pre-commit hook | ~30s | 강제 차단 (센서) |
| 4 | CI Pipeline | ~3min | 강제 차단 (센서) |
| 5 | 3+1 에이전트 합의 | ~2min | 다관점 검증 (센서) |
| 6 | Human Review | ~hours | 수동 (센서) |

### 에이전트 행동 규칙

1. **코드 편집 후**: Hook이 자동으로 lint를 실행함. lint 오류가 보이면 즉시 수정
2. **커밋 전**: Hook이 테스트를 실행함. 실패 시 커밋이 차단되므로 테스트를 먼저 수정
3. **문서 수정 시**: 해당 문서를 참조하는 다른 문서도 확인 (아래 의존 관계 참조)
4. **중요 결정 시**: 반드시 3+1 에이전트 합의 프로토콜 가동

### 계산적 vs 추론적 검증

| 검증 유형 | 예시 | 특성 | 우선순위 |
|-----------|------|------|---------|
| **계산적 (Computational)** | 린터, 타입 체커, 테스트 | 빠르고 결정적 | 우선 사용 |
| **추론적 (Inferential)** | LLM 코드 리뷰, 의미 분석 | 느리지만 판단력 | 보조 사용 |

원칙: 계산적 검증이 가능한 곳에서는 항상 계산적 검증을 우선 사용. 추론적 검증은 진정으로 모호한 상황에서만 사용.

---

## 3. 3+1 멀티 에이전트 합의 프로토콜

### 적용 조건

아키텍처/SDD/보안 관련 **큰 결정** 또는 **아이디어 검증**이 필요할 때 가동

### 구성

```
사용자 아이디어/요청
    │
    ▼
┌──────────────────────────────┐
│    메인 컨텍스트 (Orchestrator)  │
│    → 요청 분석 및 작업 분배      │
└───┬──────────┬──────────┬────┘
    │          │          │
    ▼          ▼          ▼         ← Phase 2: 병렬 독립 분석
┌────────┐ ┌────────┐ ┌────────┐
│ Agent A│ │ Agent B│ │ Agent C│
│ 구현   │ │ 품질   │ │ 대안   │
│ 분석가 │ │ 검증가 │ │ 탐색가 │
└───┬────┘ └───┬────┘ └───┬────┘
    │          │          │
    └──────────┼──────────┘
               ▼                    ← Phase 3-4: 교차 비교 + 합의
┌──────────────────────────────┐
│    검토 에이전트 (Reviewer)     │
│    → 3개 출력 교차 비교          │
│    → 일치/불일치/누락 분류       │
│    → 최종 판단 + 합의 보고서     │
└──────────────────────────────┘
    │
    ▼
사용자에게 합의 보고서 전달
```

### 에이전트 역할

| 에이전트 | 관점 | 핵심 질문 |
|---------|------|----------|
| **Agent A** (구현 분석가) | "실제로 동작하는가?" | 기술적 구현 가능성, 의존성, 성능 |
| **Agent B** (품질/안전성 검증가) | "안전하고 견고한가?" | 보안, 엣지케이스, 문서 정합성 |
| **Agent C** (대안 탐색가) | "더 나은 방법이 있는가?" | 대안 기술, 트레이드오프 |
| **Reviewer** (검토 에이전트) | "최선의 합의는?" | 교차 비교, 최종 판단 |

### 적용 기준

| 요청 유형 | 에이전트 수 | 이유 |
|-----------|------------|------|
| 단순 코드 수정/버그 fix | 1 (직접 처리) | 오버헤드 불필요 |
| 아이디어 검증/분석 | 3+1 (필수) | 다관점 검증 필수 |
| 아키텍처 의사결정 | 3+1 (필수) | 다관점 필수 |
| SDD 명세 검토 | 3+1 (필수) | 교차 검증 필수 |
| 보안 관련 변경 | 3+1 (필수) | 보안은 다중 검증 필수 |
| 중간 규모 기능 구현 | 1~2 (복잡도에 따라) | 유연하게 판단 |

### 프로세스 상세

```
Phase 1: 분배 (Distribution)
  → 메인 컨텍스트가 요청을 분석하고 3개 Agent에게 관점별 지시

Phase 2: 독립 분석 (Independent Analysis)
  → Agent A, B, C가 동시(병렬)로 독립 분석
  → 서로의 출력을 참조하지 않음 (편향 방지)

Phase 3: 교차 비교 (Cross-Comparison)
  → 검토 에이전트가 3개 출력 수집:
    ① 일치 (Consensus) — 3개 모두 동의
    ② 부분 일치 (Partial) — 2개 동의, 1개 이견
    ③ 불일치 (Divergence) — 3개 모두 다른 의견
    ④ 누락 (Gap) — 특정 에이전트만 언급한 사항

Phase 4: 합의 도출 (Consensus Resolution)
  → 일치: 그대로 채택
  → 부분 일치: 소수 의견 근거 평가 후 결정
  → 불일치: 각 근거 비교하여 최선 선택 + 이유 명시
  → 누락: 중요도 평가 후 포함/제외 결정

Phase 5: 보고 (Report)
  → 사용자에게 합의 보고서 전달
```

---

## 4. 세션 프로토콜

### 세션 시작 시

1. `docs/CONTEXT.md` 읽기 (현재 상태 파악)
2. 최신 `docs/sessions/SESSION_*.md` 읽기 (마지막 작업 확인)
3. 이 `CLAUDE.md` 규칙 숙지

### 세션 종료 시

1. `docs/sessions/SESSION_{날짜}.md` 세션 로그 작성/업데이트
2. `docs/CONTEXT.md` 최신 상태 반영
3. `docs/INDEX.md` 새 문서가 있으면 등록

---

## 5. Git 워크플로우

### 브랜치 전략 (Simplified Git Flow)

- `main`: 안정 버전 (PR만 허용)
- `develop`: 일상 개발 통합 브랜치
- `feature/*`: 기능 개발 브랜치

**흐름 (비협상)**:
```
feature/* ──PR(잦음)──▶ develop ──[특정 큰 분기에만]──▶ main
```
- feature 작업의 **PR 베이스 = `develop`** (main 아님). 잦은 주기.
- **`main` 으로의 push/PR 은 "특정한 큰 분기"(마일스톤) 시점에만**, 그리고 **사용자가 명시할 때만**. feature마다 main 가지 않음.
- ⛔ **main 으로의 push/PR 을 자동·관성으로 하지 말 것.** develop 검증·정리 완료 + 사용자 명시가 동시 충족돼야 함.

### 커밋 메시지 (Conventional Commits)

```
feat: 새 기능
fix: 버그 수정
docs: 문서 변경
test: 테스트 추가/수정
refactor: 리팩토링
chore: 빌드/설정 변경
```

---

## 6. 소통 규칙

- **한국어**로 소통 (코드/커밋 메시지는 영어)
- 기술 용어는 영어 원문 유지 (Harness, Agent, SDD, TDD 등)

---

## 7. 문서 의존 관계 (수정 시 연쇄 확인 필수)

```
CLAUDE.md 수정 시 → 영향 없음 (최상위)
docs/constitution/* 수정 시 → CLAUDE.md 참조 테이블 확인
docs/architecture/* 수정 시 → 관련 설계 문서 교차 확인
docs/architecture/harness-engineering-design.md 수정 시 → CLAUDE.md Layer 테이블 확인
docs/architecture/multi-agent-system-design.md 수정 시 → CLAUDE.md 섹션 3 확인
docs/architecture/idea-driven-stack-decision-design.md 수정 시 → multi-agent-system-design.md, automated-review-questionnaire-design.md 교차 확인
docs/decisions/ADR-011-means-vs-ends-redaction.md 수정 시 → ADR-008 부록 B Amendment, system-identity-prequel §3 (R-7 후 P2 v3 흡수 시) 교차 확인
docs/decisions/ADR-008-hermes-adoption-decision.md 부록 B 수정 시 → ADR-011 §2.1~§2.3 교차 확인 (일반 원칙 본문은 ADR-011 우선)
docs/architecture/implementation-runtime-roadmap.md 수정 시 → 17 항목 우선순위 변경은 implementation-runtime-roadmap-mvp1.md (MVP-1 deepening) + governance-preconditions.md §3~§8 (각 GP Entry/Exit) + ADR-011 §2.1 (a)~(e) 5조건 패턴 교차 확인
docs/architecture/implementation-runtime-roadmap-mvp1.md 수정 시 → implementation-runtime-roadmap.md (source roadmap, Order 1 + Order 4) + governance-preconditions.md §5 (GP-3) + §7 (GP-5) + Group D PoC + Group A 1차/2차/3차 PoC + 외부 LLM 응답 line 242 + 합의 §C-7 line 378 교차 확인
```

---

## 8. 참조 문서

| 문서 | 경로 | 용도 |
|------|------|------|
| 프로젝트 헌법 | `docs/constitution/PROJECT_CONSTITUTION.md` | 최상위 원칙 |
| 아키텍처 원칙 | `docs/constitution/ARCHITECTURE_PRINCIPLES.md` | 아키텍처 설계 원칙 |
| 코드 품질 원칙 | `docs/constitution/CODE_QUALITY_PRINCIPLES.md` | 코드 품질 규칙 |
| 하네스 설계 | `docs/architecture/harness-engineering-design.md` | 하네스 엔지니어링 상세 |
| 검토 질문지 설계 | `docs/architecture/automated-review-questionnaire-design.md` | 자동화 검토 질문지 |
| 스택 결정 설계 | `docs/architecture/idea-driven-stack-decision-design.md` | 아이디어 기반 스택 결정 |
| 에셋 파이프라인 | `docs/architecture/generative-ai-asset-pipeline-design.md` | 생성 AI 에셋 (Guide-First) |
| 에셋 확장성 | `docs/architecture/generative-ai-extensibility-design.md` | 학습/모델교체/확장 |
| AI 백엔드 스택 | `docs/architecture/ai-backend-stack-convention.md` | Python 분리 기준 |
| 환경+Docker | `docs/architecture/environment-and-docker-design.md` | 하드코딩 금지, Docker-First |
| 변경 영향 분석 | `docs/architecture/change-impact-analysis-design.md` | 의존성/장애 사전 검증 |
| **수단/목적 분리 원칙** | `docs/decisions/ADR-011-means-vs-ends-redaction.md` | **헌법 8조 (보안) + 5조-2 (Provider Liquidity, 비협상) 본질 = 안전 결과 + Provider Liquidity. R-4~R-7 모법, Hermes ≠ root of trust, 자동 학습 vs 자동 정책 변경 분리(T1/T2/T3). 상위 권위 매핑 답습 (ADR-011 line 6/245 + 헌법 line 75~80)** |
| NAI5 LoRA UI 통합 | `docs/architecture/nai5-lora-ui-integration-design.md` | @NAI5 그림체 LoRA를 gen_gate/prompt_lab UI에 통합 (lab 상주 추론 서버 브리지 백엔드, 3+1 합의). gen_gate `lab-inference` 백엔드 + `anima-nai5` 모델 엔트리 |
| gen_gate 인페인트 노출 | `docs/architecture/gen-gate-inpaint-exposure-design.md` | 미노출 SDXL inpaint 백엔드를 gate/HTTP/CLI 3계층 노출(손·비대칭 다리 국소 수정). ⭐ 백엔드 inpaint LoRA 핵심 갭 수정(cak 미전달) + path traversal allowlist(OUT 포함). 1-agent 구현(보안 §3 의도적 하향, 비례 보안). **IMPLEMENTED** gen_gate `9ae2825`(309 passed) |
| 아벨린 베이스 A/B 준비 | `docs/architecture/aveline-base-ab-comparison-design.md` | 아벨린 멀티미디어화(만화·영상·버튜버) + "animagine vs 새 베이스" 두 축 비교 하네스. 3+1 합의(`3plus1-consensus-2026-06-24-aveline-multimedia-base-ab.md`) → 축1(raw 화풍, LoRA 없이)+축2(아벨린 체인 generate_chain). 재학습=범위 밖, Z-Image·Anima 제외(R1 anima 게이트 false-positive 회피). **IMPLEMENTED** gen_gate `compare_aveline_basemodel.py`(317 passed)·comic_lab `make_comic.py --lora`(63 passed). 1순위 e2e 3트랙 PASS(일러·말하는 mp4·만화 패널) |
| 멀티에이전트 설계 | `docs/architecture/multi-agent-system-design.md` | 3+1 에이전트 상세 |
| 개발 가이드 | `docs/guides/DEVELOPMENT_GUIDE.md` | 개발 프로세스 |
| 테스트 전략 | `docs/guides/TEST_STRATEGY.md` | 테스트 방법론 |
| 구현 로드맵 (전체) | `docs/architecture/implementation-runtime-roadmap.md` | 17 항목 우선순위 매트릭스 + 9 그룹 동시 진행 + ADR-011 §2.1 5조건 답습 |
| **MVP-1 로드맵 (deepening)** | `docs/architecture/implementation-runtime-roadmap-mvp1.md` | **GP-3 + GP-5 MVP-1 진입 *직전* 의사결정 사전 정비 — 수단 후보 비교 + threshold 후보 + Rollback Trigger + Evidence + 합의 형태 권고. 수단 *결정* / threshold *고정* 0건** |
| 컨텍스트 | `docs/CONTEXT.md` | 현재 프로젝트 상태 |
