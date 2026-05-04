# 3+1 합의 보고서: Hermes 도입 안건

**날짜**: 2026-05-04
**안건**: Hermes Agent를 메인 오케스트레이터로 도입, Claude Opus 4.7과 GPT-5.5를 서브 LLM으로 활용
**관련 ADR**: [ADR-008](../decisions/ADR-008-hermes-adoption-decision.md)

---

## Phase 0 — 자동화 검토 질문지 결과

### 분류
- 유형: ARCH (primary, 80%) + IMPROVE (secondary, 70%)
- 범위: SYSTEM
- 완성도: 통과
- 에이전트 합의 필요: 예 (필수)

### 핵심 정보
| 차원 | 답변 |
|------|------|
| C1 목적 | 셀프-임프루빙/학습루프 + 모델 자유도 — "시스템 진화·강화" |
| C2 범위 | Hermes 메인 오케스트레이터 + 다중 LLM 서브 (Claude Opus 4.7, GPT-5.5 등). Claude Code 완전 대체 아님 |
| C3 성공 기준 | 4차원 종합: (가) 기능 동등성, (나) 비용·성능, (다) 학습 진화도, (라) 마이그레이션 진척 |
| C4 제약 | **⚠️ Provider Liquidity 필수** — 모델/구독 교체 자유, 코드 변경 0 |
| C5 기존 영향 | 8-Layer 하네스, 3+1 합의, .claude/*, CLAUDE.md, docs/architecture/* 전반 |

### 사용자 환경
- Claude Max 5x 구독 + ChatGPT Pro 구독
- 강한 락인 회피 의지 ("모델 성능에 따라 구독 취소나 모델 변경 용이해야함")

---

## Phase 2 — 3 에이전트 독립 분석 요약

### Agent A (구현 분석가)
**결론**: GO with conditions — Phase 1·2 즉시, Phase 3는 Hook 재구축 PoC 후

**핵심 발견**:
- 기술적 구현 가능성: HIGH (Hermes v0.12 production-ready)
- 8-Layer ↔ Hermes 통합 난이도: MEDIUM (L0/L0.5/L5는 자연 매핑, Hook 계층 L1~3은 부재 → 외부 watcher 필요)
- Provider Liquidity 충족 가능성: MEDIUM-HIGH (모델 교체 config화 가능, OAuth 구독은 약한 고리)

**8-Layer 매핑**:
| Layer | 현재 | Hermes 구현 | 위험 |
|-------|------|------------|------|
| L0 CLAUDE.md | 자동 로드 | `~/.hermes/MEMORY.md` + USER.md | 자동 로드 시점 명세 부족 |
| L0.5 검토 질문지 | 프롬프트 가이드 | Skill로 캡슐화 | 트리거 결정성 검증 필요 |
| L1 PostToolUse Hook | settings.json | **부재** → file watcher 외부 래핑 | 강제력 약화 |
| L2 PreCommit | Claude Code Hook | **부재** → Git pre-commit 이전 | 우회 가능 |
| L3 git pre-commit | .githooks/ | 그대로 유지 | 영향 없음 |
| L4 CI | GitHub Actions | 그대로 유지 | 영향 없음 |
| L5 3+1 합의 | Subagent | hermes 서브에이전트 + 모델별 분배 | 라우팅 로직 신규 |
| L6 Human Review | PR | 그대로 | 영향 없음 |

**주요 위험 (단독 발견)**:
- ChatGPT Pro OAuth Codex CLI **ToS 위반 가능성** — API 키 경로 권장
- Claude Max OAuth 다수 미해결 버그 + Hermes 동시 호출 시 race 악화

### Agent B (품질·안전성 검증가)
**결론**: GO with strict conditions — 6개 차단조건 미충족 시 HOLD

**위험 매트릭스 (10건)**:
| ID | 위험 | 등급 | 완화책 |
|----|------|------|--------|
| **R1** | Hermes 학습루프 평문 저장 (FTS5/SQLite) | **CRITICAL** | SQLCipher, redaction 필터 |
| **R2** | Hermes 자체 lock-in (skill/메모리 포맷) | **CRITICAL** | JSONL export 표준 |
| R3 | v0.x API 변동 (7-10일 릴리스) | HIGH | 버전 핀 + 회귀 테스트 + 카나리 |
| R4 | Claude OAuth 4종 버그 운영 트리거 | HIGH | 헬스체크 + 폴백 |
| R5 | Provider Liquidity 위반 (모델명 하드코딩) | HIGH | 분기 코드 금지(depcruise) |
| R6 | 다중 자격증명 표면 확대 | HIGH | 시크릿 매니저 분리 |
| R7 | 모델 간 응답 일관성 결여 | MEDIUM | JSON Schema 강제 |
| R8 | 구독 취소 = 시스템 정지 | HIGH | 최소 2 provider always-on |
| R9 | Hermes 컨테이너 격리 미적용 | HIGH | Docker-First, egress 화이트리스트 |
| R10 | Self-improvement loop 오염 | MEDIUM | 스킬 채택 PR화 + 인간 게이트 |

**Provider Liquidity 위반 패턴 6종**:
1. 모델명 분기 코드 (`if model == "claude-opus-4-7"`)
2. provider별 응답 후처리 함수 분리
3. 스킬 내 특정 모델 가정 프롬프트
4. 메모리에 provider별 메타 저장
5. Claude 전용 OAuth 갱신 로직
6. 포맷별 다운스트림 파서 의존

**헌법 위반/우려**:
- 제8조(보안): R1 직접 위반
- 제8-2조(하드코딩 제로): 모델/provider 분기 위반 소지
- 제3조(하네스): Hermes self-improvement는 센서 없는 "가이드 자기수정"
- 제4조(3+1 합의): Hermes 자율 스킬 채택은 합의 우회
- 제6조(모듈 독립성): 메인 오케스트레이터화는 모든 모듈을 Hermes에 결합

### Agent C (대안 탐색가)
**결론**: LiteLLM 우선 권장 (Option A 9/10), Hermes 메인 6개월 보류

**대안 비교 매트릭스**:
| # | 대안 | Liquidity | 학습 | 비용 | 위험 | 구현 | 종합 |
|---|------|-----------|------|------|------|------|------|
| 1 | Hermes 메인 (사용자 원안) | HIGH | HIGH | MEDIUM | HIGH | MEDIUM | 6/10 |
| 2 | **LiteLLM + Claude Code + 자체 오케스트레이션** | **HIGH** | MEDIUM | LOW | LOW | MEDIUM | **9/10** ⭐ |
| 3 | Claude Code + 외부 LLM 보조도구만 | MEDIUM | LOW | LOW | LOW | LOW | 7/10 |
| 4 | LangGraph 멀티에이전트 | HIGH | HIGH | MEDIUM | MEDIUM | HIGH | 7/10 |
| 5 | AutoGen | MEDIUM | MEDIUM | MEDIUM | MEDIUM | HIGH | 5/10 |
| 6 | 결정 보류 6개월 | — | — | LOW | LOW | LOW | 7/10 |
| 7 | 부분 도입 (백그라운드만 Hermes) | HIGH | MEDIUM | LOW | LOW | LOW | 8/10 |

**"Hermes만이 솔루션" 가정 도전**:
- 셀프-임프루빙: 추적 메트릭 / ADR 누적 / LangGraph 사이클 / Hooks+메모리 — Hermes 외 다양한 경로 존재
- 다중 LLM: LiteLLM이 사실상 표준 (40k 스타, 1B+ 요청, 200+ models)

---

## Phase 3 — 교차 비교

### 일치 (3자 동의)
- **현 상태 그대로 전면 도입은 부적절** — 셋 다 단계적·조건부 접근 공유
- **Provider Liquidity는 단순 모델 교체로 자동 충족되지 않음** — 새 추상화 레이어 필수
- **OAuth 기반 구독 직결은 위험** — 모두 직결 회피 권고 (API 키 경로 우선)
- **헌법 8조(보안) 및 환경/도커 원칙 준수 필요**
- **모델 선택을 코드가 아닌 설정(YAML)으로 외화** (`llm-providers.yaml` 신설)

### 부분 일치
- **Hermes 셀프-임프루빙 가치**: A·B 인정, C는 다른 경로로도 달성 가능 → **조건부 채택**, 좁은 영역 PoC 한정
- **Hermes 8-Layer 통합 난이도**: A·B 가능, C는 비용 우려 → 재구축 공수 실측 후 결정
- **결정 보류(HOLD) 정당성**: B·C 인정, A는 즉시 진행 → **HOLD를 유효 옵션으로 인정**

### 불일치
- **최적 아키텍처 권장**: A=Hermes 메인 조건부 GO / B=Hermes 메인 strict conditions / C=LiteLLM 우선 → **C 1순위, A·B 2순위 PoC 병행** (메타 한계 보정 후)
- **사용자 의도(Hermes 메인) 자체의 타당성**: A·B 수용 / C 의문 → C의 도전을 사용자에게 명시 전달

### 누락 (단독 발견 → 합의안 포함)
- [A] ChatGPT Pro Codex CLI **ToS 위반 가능성** → CRITICAL (차단조건 포함)
- [A] Claude Max OAuth race 악화 → HIGH (합의안 포함)
- [A] 8-Layer 상세 매핑 → HIGH (Phase 1 PoC 평가지표)
- [B] **R1 학습루프 평문 누적** → **CRITICAL** (최우선 차단조건)
- [B] **R2 Hermes 자체 lock-in** → **CRITICAL** (차단조건 #2)
- [B] R3 v0.x 변동 → HIGH (합의안 포함)
- [B] R8 단일 구독 의존 → HIGH (합의안 포함)
- [C] LiteLLM 사실상 표준 → HIGH (의사결정 핵심 근거)
- [C] Hermes #344 멀티에이전트 설계 중 → MEDIUM (보류 정당성)

---

## Phase 4 — 최종 합의

### 합의된 결론
**현 시점 Hermes 메인 전면 도입은 GO with strict conditions이지만, 본질적 목적(Provider Liquidity + 다중 LLM + 셀프-임프루빙)은 LiteLLM 우선 + Hermes 좁은 PoC 병행이 더 안전하고 SDD/TDD 자산을 보존하므로 권장된다.**

### 사용자 결정 (2026-05-04)
**Option B 채택** — 사용자 원안 (Hermes 메인 + 6개 차단조건 단계 도입)

### 6개 차단조건 (비협상)
1. SQLCipher로 Hermes SQLite 암호화 + redaction 필터 (R1 차단)
2. JSONL export 표준 + 메모리/스킬 마이그레이션 경로 (R2 차단)
3. v0.x API 버전 핀 + 회귀 테스트 + 카나리 (R3 차단)
4. provider 어댑터 1개 추상화 + 분기 금지(depcruise) (R5 차단)
5. 최소 2 provider always-on (R8 차단)
6. Docker 격리 + egress 화이트리스트 (R9 차단)

### 단계 마이그레이션
- Phase 1 (1~2주): Hermes worktree, API 키만, 비핵심 작업 검증
- Phase 2 (2~4주): Layer 5 (3+1 합의)만 Hermes 서브에이전트 (A=Claude/B=GPT/C=로컬)
- Phase 3 (조건부): Hook 재구축 + provider 어댑터 본격, Phase 2 메트릭 ≥ 현 시스템 시

### 옵션 무관 즉시 다음 단계 (5개 공통)
1. `docs/architecture/llm-providers-design.md` 신설 (provider/model_id/auth_method/cost/status)
2. 헌법 제8조 + 환경/도커 설계 재확인 (SQLite/메모리 평문 누적 금지 명문화)
3. OAuth 직결 금지 정책 수립 (Claude Max·ChatGPT Pro 모두 API 키 경로 우선)
4. 최소 2 provider always-on 원칙 헌법화
5. depcruise 룰: provider별 분기 코드 패턴 정적 차단

### 미해결 결정 사항
1. Hermes 학습루프 가치 정량 측정 방법 — Phase 1 PoC에서 측정
2. Hook 계층(L1~3) 재구축 공수 실측치 — Phase 1 측정 항목
3. ChatGPT Pro Codex CLI ToS 정확한 조항 — 진입 전 사실 확인 필수
4. Hermes JSONL export 가능 여부 + 마이그레이션 도구 존재 여부 — 차단조건 #2 기술적 가능성 검증

### 위험 알림 (사용자 상시 인지)
- CRITICAL R1: Hermes SQLite 평문 → SQLCipher + redaction 미구현 시 자동 NO-GO
- CRITICAL R2: Hermes 자체 lock-in → JSONL export 표준 사전 정의 필수
- CRITICAL A-meta: ChatGPT Pro OAuth ToS 위반 가능성 → API 키 경로만
- HIGH R4: Claude Max OAuth race → API 키 경로 우선
- HIGH R3: v0.x API 불안정 → 버전 핀 + 카나리 필수
- HIGH R8: 단일 구독 의존 금지 → 최소 2 provider always-on
- MEDIUM 메타: 본 합의는 Claude 기반 3 에이전트 작성 → 외부(비-Claude) 검증 권장

---

## 메모리 저장
- `~/.claude/projects/-home-delangi----project-category-AI-development-tool/memory/feedback_provider_liquidity.md` — Provider Liquidity 하드 요구를 영구 기억으로 저장
