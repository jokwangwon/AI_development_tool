# 프로젝트 컨텍스트 (Project Context)

> **AI 에이전트가 세션 시작 시 반드시 읽어야 하는 현재 상태 문서**

**최종 업데이트**: 2026-05-06 (R-3 완료 — ADR-011 발행 + ADR-008 Amendment 추가, R-4 진입 대기)

---

## 현재 활성 의사결정 (2026-05-06 R-3 완료 시점)

**Phase 0 Day 1~3 + R-3 완료, ADR-011 발행 + ADR-008 부록 B Amendment 추가, 단축 합의 APPROVE** — R-4~R-7 진입 대기.

### 합의·검증 산출 (2026-05-05 ~ 2026-05-06 누적)
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
- **`docs/decisions/ADR-008-hermes-adoption-decision.md` 부록 B Amendment (R-3 — R1 specific 갱신)**
- **`docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md` (R-3 단축 합의 APPROVE)**

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
| **G1b** | **DB-level fallback (SQLCipher trigger)** | ✅ PoC PASS 실증 + **R-3 완료**, 정식 충족은 R-4~R-7 후 (ADR-011 §2.2 5단계) |
| G2 | 6 거버넌스 사전조건 | ⏳ 미작성 |
| G3 | "Hermes ≠ root of trust" 운영 구현 | 🟡 ADR 권위 확정 (ADR-011 §2.3), 운영 구현 미작성 |
| G4 | Provider-agnostic Memory/Skill 형식 | ⏳ 미작성 |

### Phase 0 진행 상태
- ✅ Day 1 (사실 확인)
- ✅ Day 2 (R-1 FAIL)
- ✅ Day 3 (R-2 PASS, timebox 1~2일 내 조기 완료)
- ✅ **R-3 (2026-05-06): ADR-011 발행 + ADR-008 부록 B Amendment 추가, 단축 합의 APPROVE**
- ⏳ R-4~R-7: 다음 진입 대기

### 다음 세션 TODO (우선순위 순)

1. ~~**R-3**~~ ✅ 완료 (2026-05-06)
2. **R-4** (다음 진입점): Hermes redact pattern (`_PREFIX_PATTERNS` 35종) ↔ P1_REDACTOR 패턴 동등성 비교 — `docs/architecture/redaction-pattern-equivalence.md`
3. **R-5**: canary 재검증 트리거 설계 (T13 강화 — config 체크 + 주기적 inject) — `docs/architecture/canary-recheck-design.md`
4. **R-6**: CI/nightly 회귀 검증 (Hermes 업그레이드 자동 R-2 재실행) — `.github/workflows/r2-canary.yml`
5. **R-7**: Phase 1 합격 SOP 작성 — `docs/phase0/redaction-verification-sop.md`
6. **P2 v3 신규 작성** (R-7 완료 후) + ADR-008/009/010/**011** 갱신 PR 묶음
7. **G2/G3/G4** 작성 (병행 가능, G3는 ADR-011 §2.3 운영 구현)

**권고 시작점**: "R-4 진행해주세요" 명령으로 Hermes `_PREFIX_PATTERNS` 추출 + P1_REDACTOR 비교 시작. ADR-011 §2.1 (a) 동등 이상 보장 검증 의무의 직접 충족 작업.

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
