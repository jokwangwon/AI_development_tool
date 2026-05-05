# AI 자동화 개발 도구 — 외부 검토용 시스템 요약 (2026-05-05)

> GPT 등 외부 LLM에 붙여넣어 시스템 전체 구조와 현 의사결정을 검토받기 위한 자기충족적 요약입니다. 첨부 자료 없이 본 문서만으로 평가 가능하도록 작성되었습니다.

---

## 0. 검토를 의뢰하는 사람의 입장

저는 1인 개발자로 "**아이디어를 던지면 AI 에이전트(주로 Claude Code)가 SDD+TDD로 자동 개발하도록 설계된 메타-템플릿**"을 만들고 있습니다. 이 프로젝트 자체는 그 템플릿이며, 새 아이디어가 생길 때마다 본 템플릿을 복사해 시작합니다. 본 검토에서는 다음을 받고 싶습니다:

1. **설계 체계의 일관성** — 헌법, ADR, 설계 문서가 서로 모순되지 않는가
2. **하네스(Harness) 엔지니어링의 합리성** — 에이전트 행동을 잘못하기 어렵게 만드는 메커니즘이 충분한가
3. **현재 진행 중인 Hermes 도입 결정의 위험** — 무엇을 놓치고 있는가
4. **AI 에이전트가 자기 자신을 검증하는 한계** (메타 한계) — 본 시스템이 이걸 어떻게 다루는지에 대한 외부 시각

---

## 1. 프로젝트 정체성

**이름**: AI 자동화 개발 도구 (AI Development Tool Template)
**성격**: 코드 베이스가 아닌 **메타-템플릿** — 새 프로젝트마다 복사해서 시작하는 SDD+TDD+하네스 설계 체계
**저장소 구성**: 코드 0줄, 문서 12개 ADR + 11개 설계 문서 + 3개 합의 보고서 + 헌법 + 가이드. 약 50개 마크다운 파일.
**주 사용자**: 1인 개발자 (저). 실 프로젝트 시작 시 본 템플릿 적용 → Phase 0 자동화 검토 질문지 → Phase 1 3+1 합의 → SDD+TDD 코드 작성.

**왜 코드보다 문서인가**:
> "에이전트에게 하라고 말하지 말고, 잘못하는 것이 불가능하게 만들어라"
>
> Agent = Model + Harness. 모델은 추론을 제공하고, 하네스(문서/규칙/훅/검증)는 나머지 전부.

---

## 2. 핵심 방법론 (4축)

### 2.1 SDD (Specification-Driven Development)
- 코드보다 **문서가 우선**. 코드 변경 전 관련 SDD 문서 확인 필수
- 문서가 없으면 → 설계 문서를 먼저 작성하고 사용자 검토 → 검토 후 코드 구현 → 변경사항 문서 반영

### 2.2 TDD (Test-Driven Development)
- RED → GREEN → REFACTOR 사이클 강제
- 테스트 커버리지 목표 70% 이상

### 2.3 하네스 엔지니어링 (Harness Engineering)
| Layer | 수단 | 속도 | 수준 |
|-------|------|------|------|
| 0 | CLAUDE.md (프로젝트 규칙) | ~0ms | 권고 (가이드) |
| 0.5 | 자동화 검토 질문지 | ~30s | 아이디어 구조화 (가이드) |
| 1 | PostToolUse Hook (자동 lint) | ~500ms | 강제 피드백 (센서) |
| 2 | PreCommit Hook (테스트) | ~10s | 강제 차단 (센서) |
| 3 | git pre-commit hook | ~30s | 강제 차단 (센서) |
| 4 | CI Pipeline | ~3min | 강제 차단 (센서) |
| 5 | 3+1 에이전트 합의 | ~2min | 다관점 검증 (센서) |
| 6 | Human Review | ~hours | 수동 (센서) |

**가이드(Feedforward) vs 센서(Feedback)**:
- 가이드: CLAUDE.md, 설계 문서, 스킬 정의 (사전 조향, 결정적)
- 센서: 린터, 타입 체커, 테스트, 코드 리뷰 (사후 검증, 계산적 우선 + 추론적 보조)

**원칙**: 계산적 검증(린터/테스트)이 가능한 곳에서는 항상 우선 사용. 추론적 검증(LLM 코드 리뷰)은 진정으로 모호한 상황에서만.

### 2.4 3+1 멀티 에이전트 합의 프로토콜

큰 결정 또는 아이디어 검증 시 가동:

```
사용자 아이디어 → 메인 컨텍스트(Orchestrator)
                 ↓ 작업 분배
   ┌─────────────┼─────────────┐
   ▼             ▼             ▼
Agent A      Agent B      Agent C       ← 병렬 독립 분석 (편향 방지)
"실 동작?"   "안전?"      "더 나은 방법?"
   │             │             │
   └──────┬──────┴──────┬──────┘
          ▼             ▼
      Reviewer (검토 에이전트)            ← 교차 비교 + 합의
          ↓
   합의 보고서 (일치/부분/불일치/누락 분류)
          ↓
   사용자 결정
```

| 요청 유형 | 에이전트 수 |
|---------|-----------|
| 단순 코드 수정 | 1 (직접) |
| 아이디어 검증 | 3+1 (필수) |
| 아키텍처 결정 | 3+1 (필수) |
| SDD 명세 검토 | 3+1 (필수) |
| 보안 결정 | 3+1 (필수) |
| 단축 합의 (보강 검증) | Reviewer-only |

**메타 한계 (CRITICAL)**: 모든 에이전트가 Claude이므로 "외부 도구 권장 vs 자체 코드 권장" 안건에서 자체 코드 친화 편향이 자동 발생. Reviewer가 의식적으로 외부 SDK 권장 측에 가중치 부여로 보정.

---

## 3. 프로젝트 헌법 (12개 조항, 핵심만)

| 조항 | 핵심 |
|------|------|
| 1조 | SDD+TDD 강제 |
| 2조 | 하네스 엔지니어링 ("잘못하는 것이 불가능하게") |
| 3조 | 계산적 검증 우선, 추론적 보조 |
| 4조 | 3+1 합의 — 에이전트 간 출력 비참조 (편향 방지) |
| 5조 | Provider Liquidity — 모델/구독 교체가 코드 변경 없이 가능해야 함 (영구 기억) |
| 6조 | 의존성 외부 SDK 우선 (자체 구현 최소화) |
| 7조 | 환경 변수 + Docker-First (하드코딩 제로) |
| **8조** | **AI 학습 루프는 비밀값 평문 영구 저장 금지** — 암호화 또는 redaction 처리 |
| 9조 | 변경 영향 분석 — 의존성/장애 사전 검증 |
| 10조 | 미정 (예약) |
| 11조 | 한국어 소통 (코드/커밋은 영어) |
| 12조 | 문서 의존 관계 명시 (수정 시 연쇄 확인) |

---

## 4. 주요 ADR 요약 (10개)

| ADR | 결정 | 핵심 |
|-----|------|------|
| 001 | 자동화 검토 질문지 | Phase 0: 아이디어 → 브리프 (필수3 + 동적2 질문) |
| 002 | 아이디어 기반 스택 결정 | Phase 1: 스택 통합 결정 (3+1 합의) |
| 003 | 생성 AI 에셋 파이프라인 | Guide-First 에셋 생성 |
| 004 | 생성 AI 확장성 | **외부 SDK 우선** + Config 기반 모델 교체 |
| 005 | AI 백엔드 스택 | 로컬 추론 시 Python 분리 |
| 006 | 환경+Docker | 하드코딩 제로 + Docker-First |
| 007 | 변경 영향 분석 | 의존성/장애 사전 검증, 자동 분류 |
| **008** | **Hermes Agent 도입** | **Option B (Hermes 메인 + Claude/GPT 서브)**, 6개 차단조건 비협상 |
| 009 | 자체 Adapter v2.0 진입 조건 | LiteLLM 사용 전제, T1~T4 정량 트리거 |
| 010 | SQLCipher Vault HSM 키관리 | Vault HSM + Shamir 3-of-3 + 90일 회전 |

### ADR-008 (가장 큰 결정) 상세
- **결정**: Hermes Agent v0.12.0을 메인 오케스트레이터로 도입 (Option B)
- **6개 차단조건 (비협상)**:
  1. SQLCipher 암호화 (학습 루프 평문 차단)
  2. JSONL export (lock-in 방지)
  3. v0.x 버전 핀 (회귀 테스트 + 카나리)
  4. provider 어댑터 1개 (P1 facade 위임)
  5. Min 2 active provider (Liquidity)
  6. Docker 격리 + egress 화이트리스트
- **사용자 의지로 채택**: Reviewer는 Option A (LiteLLM 우선) 권장이었으나 사용자 결정 존중
- **Phase 0 게이트 신설**: P2-N1·N2 + sqlite 호환성 검증 (3~5일) — 미통과 시 §3.4 폴백 (Option A 회귀)

---

## 5. 개발 파이프라인 (확정)

```
Phase 0: 자동화 검토 질문지 (필수3 + 동적2)
   ↓
Phase 1: 3+1 합의 (아이디어 + 스택 + 에셋 식별)
   ├── Phase 2-3: SDD → TDD (코드)
   └── 에셋 파이프라인 (비코드, Guide-First, 병렬)
   ↓
Phase 4: 통합 테스트 + 배포
```

위 파이프라인은 **새 프로젝트에 본 템플릿 적용 시** 따르는 흐름. 본 템플릿 자체의 개발도 동일한 SDD+TDD+합의 프로세스로 진행.

---

## 6. 현재 진행 중 — Hermes 도입 (P2 v2)

### 6.1 Hermes Agent란
NousResearch가 만든 자율 셀프-임프루빙 AI 에이전트 프레임워크 (v0.12.0 = 2026-04-30 "Curator release"). 다음 특징:
- 자체 학습 루프 (SQLite + FTS5) — 스킬을 경험에서 자동 생성, 사용 중 개선, 과거 대화 검색
- 다중 LLM 백엔드 지원 (Anthropic, OpenAI, Ollama 등)
- 1,096 commits / 550 PRs (v0.11→v0.12 한 사이클)
- ~15k 테스트, ~1390 Python 파일
- Docker / 로컬 / SSH / Termux 지원

### 6.2 도입 단계 (P2 v2)
- **Phase 0** (3~5일, 현재): 사실 확인 게이트 — P2-N1/N2 + sqlite 호환성
- **Phase 1** (3~4주): 6 차단조건 충족 검증 + API 키만 사용
- **Phase 2** (2~4주): Layer 5 (3+1 합의)을 Hermes 서브에이전트로 이전, 다중 LLM 합의
- **Phase 3** (조건부): Hook 계층 Hermes 재구축
- **Phase 4+** (미정의): 전면 이전

### 6.3 자동 롤백 트리거 11종
메트릭 임계 초과 / Hermes deadlock / SQLCipher 키 회전 실패 / 자동 업데이트 시도 / Egress 화이트리스트 위반 / 사용자 무응답 / 차단조건 위반 등.

---

## 7. **현재 의사결정 — Phase 0 Day 1~2 (오늘 진행)**

### 7.1 발견 1: P2 v2 §2.1.3 가정 코드 미존재

**P2 v2가 가정한 코드**:
```python
hermes.session_storage.add_pre_record_hook(redaction_hook)
```
이 hook이 DB INSERT 직전에 redaction을 적용한다는 가정.

**실제 (코드 grep 결과)**:
- `pre_record`, `add_pre_record_hook`, `before_record` 검색 → **0건**
- `VALID_HOOKS` 권위 정의 (`hermes_cli/plugins.py:78`) — 15종 hook 모두 확인
- DB 기록 직전 가로채기 hook **0개**
- `SessionDB.append_message`(`hermes_state.py:1222`) — 콜백 등록 인자 없음, 직접 SQL INSERT

→ **P2 v2 §2.1.3 코드 그대로 동작 불가 확정**

### 7.2 발견 2: Hermes 자체 redaction 시스템 존재

**위치**: `agent/redact.py`, `cli.py:585`, `hermes_cli/main.py:186` 등
**활성화**: `~/.hermes/config.yaml`에 `security.redact_secrets: true` 또는 환경변수 `HERMES_REDACT_SECRETS=true`
**v0.12.0 breaking change**: default ON → OFF로 뒤집힘 (opt-in 전환)

→ "외부 hook 형태"가 아닌 "Hermes 자체 redaction 활용"이라는 대안 경로 등장

### 7.3 단축 합의 (Reviewer-only) 가동

**안건**: P2-N1 비협상 조건 해석 갱신 — "외부 hook 형태가 비협상"이 아닌 "DB 평문 저장 차단 결과가 비협상"으로 재해석할 수 있는가

**Reviewer 결론**: APPROVE with revisions, 단 **R-1 결과에 조건부**

**필수 보강 7건 (R-1~R-7)**:
- R-1 (CRITICAL): Phase 0에서 Hermes 자체 redaction이 **DB INSERT 경로**에 실제 적용되는지 직접 검증 (canary 비밀 주입 → sqlcipher SELECT)
  - PASS → R-2~R-7 보강 후 정정안 채택
  - FAIL (LLM 송신만 적용 시) → 즉시 옵션 A 회귀
- R-2: SQLite trigger 의무화, monkey-patch는 비차단 모니터링용으로만 강등
- R-3: ADR-011 또는 ADR-008 Amendment 발행 (수단/목적 분리 명문화)
- R-4: redaction 패턴 동등성 검증 (Hermes redact_secrets ↔ P1_REDACTOR)
- R-5: 자동 롤백 T13 강화 (config 체크 + 주기적 canary 검증)
- R-6: CI nightly 회귀 (Hermes 업그레이드 자동 검증)
- R-7: Phase 1 합격 SOP 명세화 (canary 주입 절차)

### 7.4 Reviewer 신뢰도 평가

- **차원 1 (헌법 8조 본질 충족)**: PARTIAL — redaction 적용 위치 미검증
- **차원 2 (해석 갱신 정당성)**: PASS — 수단/목적 분리 정당
- **차원 3 (Hermes 자체 redaction 신뢰도)**: **LOW** — v0.12.0 default OFF는 upstream 격하 신호
- **차원 4 (보조 안전망 정합성)**: PARTIAL — monkey-patch 부적절, trigger 정합
- **차원 5 (누락 위험)**: 6건 식별 (N1~N6)

### 7.5 메타 편향 통제 명시
Reviewer가 "외부 hook 형태가 비협상이라는 엄격 해석을 진지하게 재고했고, 수단/목적 분리는 자체 코드 우호적 결론이므로 한 단계 더 회의적으로 점검했다"고 명시. 결과: Primary 단독 의존 금지 + 보조 안전망 의무화 + R-1 Phase 0 차단조건 격상.

---

## 8. 핵심 미해결 위험

### 8.1 메타 한계
- 모든 합의 에이전트가 Claude → 외부 도구(LiteLLM, Hermes) 평가 시 자체 코드 친화 편향
- Reviewer가 의식적으로 보정하나 완전 해소 불가
- → 본 GPT 검토가 메타 한계를 외부 시각으로 보완하는 역할

### 8.2 Hermes Upstream 의존
- v0.12.0 default OFF (redaction 격하)는 upstream의 redaction 우선순위가 낮다는 신호
- 향후 redaction 기능 제거/시그니처 변경 가능성 배제 불가
- → SQLite trigger (DB 레벨 강제) + Vault HSM (키 관리)로 우회 의도

### 8.3 Phase 0 검증 미완료
- P2-N1: pre-record hook 부재 확정 → 단축 합의로 정정안 도출 → R-1 검증 대기
- P2-N2: skills/memory export 미포함 확정 → 우회 방안 (profile export, state.db raw 백업)
- sqlite 호환: 18개 `import sqlite3` 위치 확인, 잠정 PASS 가능 (Day 4 실측)

### 8.4 Provider Liquidity 강제
- 영구 기억으로 저장 (`feedback_provider_liquidity.md`)
- 6 차단조건 #5 (Min 2 active) 로 코드화
- Hermes 도입 시 Hermes 자체가 단일 제공자에 lock되지 않도록 P1 facade 위임

---

## 9. 검토 요청 사항 (GPT가 답해주기를 원하는 질문)

### Q1. 시스템 설계의 일관성
12개 헌법 조항 + 10개 ADR + Phase 0~4 파이프라인이 서로 모순되거나 누락된 영역이 있는가? 특히 헌법 8조(평문 저장 금지)와 ADR-004(외부 SDK 우선)의 조합이 Hermes 도입 결정과 정합한가?

### Q2. 하네스 엔지니어링의 충분성
Layer 0~6 피드백 루프가 1인 개발자 + AI 에이전트 협업에 충분한가? 누락된 강제 메커니즘이 있는가? (예: 내부 코드 리뷰 단계, 정적 분석 단계, secret scanning 등)

### Q3. Hermes 도입 결정의 위험
ADR-008 Option B (Hermes 메인) 선택이 Reviewer가 권장한 Option A (LiteLLM 우선)보다 합리적이라고 판단할 정량적/정성적 근거가 충분한가? Phase 0 진입 결정 자체가 sunk cost를 키우는 함정인가?

### Q4. R-1 검증 결과 해석
Hermes 자체 redaction이 LLM 송신 단계에만 적용되고 DB INSERT 경로에는 미적용이라면, "정정안 즉시 폐기 → 옵션 A 회귀"가 올바른 결정인가? 아니면 SQLite trigger만으로도 헌법 8조 본질 충족 가능하다고 볼 수 있는가?

### Q5. 메타 한계
모든 합의 에이전트가 Claude인 시스템에서 외부 도구 평가 시 발생하는 자체 코드 친화 편향을 어떻게 더 잘 통제할 수 있는가? Reviewer의 의식적 보정 외 다른 메커니즘이 있는가?

### Q6. 1인 개발자 + AI 에이전트 협업의 함정
본 시스템이 1인 개발자가 다루기에 과도한 거버넌스/문서 부담을 만드는가? 어느 단계에서 단순화가 필요한가?

---

## 10. 자료 위치 (참고용, 외부 검토에는 불필요)

```
docs/
├── CONTEXT.md                              # 현재 상태
├── INDEX.md                                # 전체 문서 색인
├── constitution/                           # 헌법 + 원칙
├── decisions/                              # ADR-001~010
├── architecture/                           # 11개 설계 문서
│   ├── harness-engineering-design.md
│   ├── multi-agent-system-design.md
│   ├── llm-providers-design.md            # P1 v2
│   ├── hermes-adoption-design.md          # P2 v2
│   └── ...
├── review/                                 # 3+1 합의 보고서 (4건)
├── phase0/                                 # 현재 진행 (1건)
└── sessions/                               # 세션 로그
```

---

**작성일**: 2026-05-05
**작성 목적**: GPT 외부 검토용 자기충족 요약
**현재 진행 단계**: Phase 0 Day 2 R-1 검증 (Hermes 자체 redaction이 DB INSERT 경로에 실제 적용되는지 격리 환경에서 canary 검증)
**다음 결정**: R-1 결과에 따라 정정안 채택 (R-2~R-7 보강) 또는 옵션 A 회귀 (§3.4 폴백 → ADR-011)
