# 프로젝트 컨텍스트 (Project Context)

> **AI 에이전트가 세션 시작 시 반드시 읽어야 하는 현재 상태 문서**

**최종 업데이트**: 2026-05-05 (시스템 정체성 재정의 + Phase 0 Day 1~2 진행 중)

---

## 현재 활성 의사결정 (2026-05-05)

**시스템 정체성 재정의 합의 완료** — 풀 3+1 합의 + GPT 외부 4번째 의견 종합 결과 "AI Development Company OS" 방향성 채택, MVP 부분 채택, Hermes PMO 격상은 4 게이트 충족 후.

### 합의 산출
- `docs/architecture/system-identity-prequel.md` (시스템 정체성 prequel — P2 v3 정식화 전 임시 선언)
- `docs/review/3plus1-consensus-2026-05-05-system-identity-redefinition.md` (풀 3+1 합의 보고서)

### 핵심 채택 사항
- **정체성**: "AI Development Company OS" 메타포 (선언적, 즉시)
- **권위 위계**: `Constitution > ADR > SDD > Harness Gates > Hermes > Worker Agents`
- **Hermes ≠ root of trust** (운영적 강제 4가지)
- **자동 학습 ≠ 자동 정책 변경** (T1 자동 / T2 사용자 승인 / T3 절대 금지)
- **Evidence 검증**: "Agent proposes / Hermes orchestrates / Tools verify / Evidence decides / Human overrides"
- **메타포 강제 금지** 조항 (메타포 인플레이션 회피)

### MVP 범위 (Phase 1 시작 기준)
- **Worker Agent 4**: PM/Orchestrator + Architect + Implementation + Reviewer (QA/Security/Doc은 hook/CI/secret scanner/체크리스트로 대체)
- **Memory 2단계**: Global + Project (manual promotion만, Team/Session은 미래 ADR)
- **Evidence**: Markdown + JSONL append-only (hash chain or git append commit으로 변조 방지)

### Hermes PMO 격상 4 게이트 (G1~G4)
- **G1**: Phase 0 R-1 (canary 검증) 완료 — Hermes 자체 redaction이 DB INSERT 경로 적용 확인
- **G2**: 6 거버넌스 사전조건 충족 (8 위반 경로 P1~P8 강제 메커니즘 매핑)
- **G3**: "Hermes ≠ root of trust" 운영적 구현 (read-only on Constitution/ADR/SDD, 합의 결과 git commit + UI 직접 전달)
- **G4**: Provider-agnostic Memory/Skill 저장 형식 확정

### Phase 0 진행 상태 (Day 1~2)
- **Day 1 완료**: Hermes v0.12.0 사실 확인. P2 v2 §2.1.3 가정 코드 (`add_pre_record_hook`) 공식 API 미존재 확정. Hermes 자체 redaction 시스템 발견 (`security.redact_secrets`, v0.12.0 default OFF).
- **단축 합의 완료**: APPROVE with revisions. R-1~R-7 보강 (R-1 결과 조건부).
- **R-1 검증 재개**: Hermes 자체 redaction이 DB INSERT 경로에 실제 적용되는지 격리 환경 canary 검증.
  - PASS → R-2~R-7 보강 후 P2 v3 작성
  - FAIL → 합의 옵션 (2) C-③안 변형 자동 전환 (Hermes PMO 격상 6~12개월 완전 보류)

### 작업 우선순위 (사용자 확정)
1. ✅ 정체성 prequel 선언 작성 (현 단계 완료)
2. ⏳ Phase 0 R-1 검증 재개
3. ⏳ 6 거버넌스 사전조건 매트릭스 작성
4. ⏳ Role Contract 25건 작성 (`docs/roles/AGENT_<NAME>.md` × 4)
5. ⏳ Memory boundary 최소 메커니즘 작성
6. ⏳ Evidence 최소 schema 작성
7. ⏳ R-7 완료 후 P2 v3 신규 작성
8. ⏳ ADR-008/009/010 갱신 PR 묶음
9. ⏳ 4 게이트 충족 검증 후 Hermes PMO 격상 활성화 (예상 2~4주 후)

### 영구 핵심 제약
- **Provider Liquidity** (`feedback_provider_liquidity.md`): 모델/구독 교체가 코드 변경 없이 가능해야 함
- **Hermes ≠ root of trust** (system-identity-prequel §3): 모든 PASS 결정의 최종 근거는 계산적 검증 + Evidence
- **메타포 강제 금지** (system-identity-prequel §7): 메타포 정합성 위해 실 구조 늘리지 말 것

### 현 잔여 작업 (Task #16, 보류 중)
1. P1 v2 minor revisions 6건 적용 — P2 v3 작성과 병합 검토
2. `.claude/settings.local.json` 처리 (gitignore 권장)
3. 잘못된 origin/main 커밋 2개 정리

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
**상세**: `docs/architecture/system-identity-prequel.md`, `docs/review/3plus1-consensus-2026-05-05-system-identity-redefinition.md`
