# ADR-008: Hermes Agent 도입 결정 (Option B)

**상태**: 승인 (3+1 합의 완료, 사용자 Option B 선택)
**날짜**: 2026-05-04
**의사결정자**: 사용자 + 3+1 에이전트 합의

---

## 맥락 (Context)

사용자가 "Hermes Agent를 메인 오케스트레이터로 도입, Claude Opus 4.7과 GPT-5.5를 서브 LLM으로 활용"하는 시스템 진화를 제안. 현재 시스템은 Claude Code 단일 의존이며, 사용자는 모델/구독 교체의 자유를 강하게 요구함 (Provider Liquidity 하드 제약: "Claude Max 사용중이지만 모델 성능에 따라 구독 취소나 모델 변경이 용이해야함").

## 결정 (Decision)

**Option B 채택**: Hermes를 메인 오케스트레이터로 단계 도입하되, **6개 차단조건이 모두 충족된 후에만 다음 Phase로 진입**한다.

### 6개 차단조건 (비협상)
1. **SQLCipher**로 Hermes SQLite 암호화 + redaction 필터 (헌법 제8조 준수)
2. **JSONL export 표준** + 메모리/스킬 마이그레이션 경로 정의 (Hermes lock-in 회피)
3. v0.x API **버전 핀** + 회귀 테스트 + 카나리 환경
4. **provider 어댑터 1개 추상화** + 분기 코드 금지 (depcruise로 강제)
5. **최소 2 provider always-on** (단일 구독 의존 금지)
6. Docker **격리 + egress 화이트리스트**

### 단계 마이그레이션
- **Phase 1** (1~2주): Hermes worktree 설치, **API 키만 사용**(OAuth 직결 금지), 비핵심 작업 검증
- **Phase 2** (2~4주): Layer 5(3+1 합의)만 Hermes 서브에이전트로 이전 (A=Claude / B=GPT / C=로컬)
- **Phase 3** (조건부): Hook 계층 watchexec 재구축 + provider 어댑터 본격 적용. **선결조건**: Phase 2 메트릭 ≥ 현 시스템

## 선택지 (Options Considered)

### Option A: LiteLLM 우선 + Hermes 좁은 PoC (3+1 권장 ★★★★★)
- 장점: Provider Liquidity 본업 충족, 기존 SDD/TDD 자산 100% 보존, 즉시 시작
- 단점: Hermes 셀프-임프루빙 가치 일부 늦게 확인

### Option B: Hermes 메인 + 6개 차단조건 단계 도입 ⭐ **채택**
- 장점: 사용자 원안 직접 실현, 셀프-임프루빙 빠른 체험
- 단점: 차단조건 6개 미충족 위험, v0.x 불안정, Hook 재구축 공수 미지수

### Option C: 6개월 보류
- 장점: 신생 프레임워크 리스크 회피
- 단점: 다중 LLM 활용·Liquidity 개선 지연

## 근거 (Rationale)

3+1 합의는 Option A를 1순위로 권장했으나, 사용자가 의식적으로 Option B를 선택. 사용자 의지·선호 존중. 단, 6개 차단조건은 **비협상** — 미충족 시 자동 NO-GO하며, Hermes 도입을 중단하고 Option A로 자동 폴백한다.

## 3+1 에이전트 합의 결과

| 에이전트 | 의견 | 핵심 근거 |
|---------|------|----------|
| Agent A (구현) | 조건부 GO | 8-Layer 통합 MEDIUM, Phase 1·2 즉시 가능, Phase 3는 Hook 재구축 PoC 성공 시 |
| Agent B (품질) | GO with strict conditions | R1 학습루프 평문(CRITICAL), R2 Hermes lock-in(CRITICAL), 6개 차단조건 미충족 시 HOLD |
| Agent C (대안) | LiteLLM 우선 권장 (Option A) | Liquidity는 도구 추상화 문제, Hermes만의 솔루션 아님 |
| **Reviewer** | **Option A 1순위, B는 차단조건 충족 시 가능** | 메타 한계 보정으로 C에 가중치, 사용자 선호 시 B 진행 가능 |

## CRITICAL 위험 (운영 중 상시 감시)

- **R1 학습루프 평문 누적**: Hermes SQLite FTS5에 사용자 컨텍스트·LLM 응답·환경변수 echo가 평문 영구 저장. **헌법 제8조 직접 위반**. 차단조건 #1 미구현 시 자동 NO-GO.
- **R2 Hermes 자체 lock-in**: 누적 학습 결과(스킬/메모리/프로필)는 Hermes 떠나면 손실. Provider Liquidity 정신 위반. 차단조건 #2 미정의 시 자동 NO-GO.
- **A-meta ChatGPT Pro Codex CLI OAuth ToS 위반 가능성**: 위반 시 구독 강제 해지 → 시스템 정지. **API 키 경로만 사용**.
- **R4 Claude Max OAuth race**: 다수 미해결 버그(#15080, #6475, #12905, #10575) — Hermes 동시 호출 시 무한 인증루프 가능. API 키 경로 우선.
- **R8 단일 구독 의존**: 어떤 단계에서도 single point of failure 금지. 차단조건 #5로 강제.

## 메타 한계 (사용자 인지 필요)

본 합의는 3 Claude 에이전트가 작성. Hermes(외부 도구)에 대한 평가에 친화 편향 가능. Reviewer가 Agent C 회의적 입장에 의식적 가중치 부여로 보정함. Option B 진행 중에도 외부(비-Claude) 검증 권장.

## 결과 (Consequences)

- **긍정적**: 다중 LLM 환경 구축, 셀프-임프루빙 학습루프 도입 시도, Provider Liquidity 강제 메커니즘 정착
- **부정적**: 신생 프레임워크 리스크 감수, Hook 재구축 공수 발생, v0.x API 변동 대응 부담, R1/R2 차단조건 미충족 시 전면 폴백 위험
- **주의사항**:
  - 6개 차단조건 중 1개라도 미충족 시 도입 중단 → Option A 자동 폴백
  - 진행 중에도 정기적 재평가 (Phase 종료마다)
  - 차단조건 충족 검증은 별도 SDD 문서로 명세 예정
  - Provider Liquidity 위반 패턴 6종(모델명 분기/provider별 후처리/스킬 내 모델 가정 등)은 depcruise 룰로 정적 차단

---

**관련 문서**:
- `docs/review/3plus1-consensus-2026-05-04-hermes.md` (3+1 합의 보고서 전문)
- `docs/architecture/hermes-adoption-design.md` (도입 설계 — 작성 예정)
- `docs/architecture/llm-providers-design.md` (provider 추상화 — 작성 예정)
- `docs/constitution/PROJECT_CONSTITUTION.md` 제8조 (보안)
- `~/.claude/projects/-home-delangi----project-category-AI-development-tool/memory/feedback_provider_liquidity.md` (Provider Liquidity 영구 기억)

---

## 부록 A — 검증 결과 (2026-05-04)

Phase 1 진입 전 사실 확인 작업 2건 완료. 결과 CRITICAL 위험 2건이 다운그레이드되었으나, 차단조건 6개는 그대로 유지(방어 자세).

### A.1 ChatGPT Pro Codex CLI ToS 검증
- **공식 지원**: Hermes는 OpenAI Codex `device code` OAuth flow를 정식 지원. credentials는 `~/.hermes/auth.json`에 저장, `~/.codex/auth.json`에서 import 가능
- **개인 단일 사용자 시나리오**: ToS 위반 위험 **LOW** — Codex CLI 자체와 동등 사용
- **금지 사례**: "Reselling access" 또는 "third-party services에 ChatGPT 전력 공급". 본 프로젝트는 개인 사용이므로 해당 없음
- **정책 변동성**: OpenAI/Anthropic가 third-party 도구의 구독 집계를 최근 제한한 사례 존재 → API 키 경로 우선 정책은 그대로 유지
- **A-meta 위험 등급**: CRITICAL → **MEDIUM** (정책 변동 모니터링 필요)

### A.2 Hermes JSONL Export 검증
- **공식 명령어**: `hermes sessions export backup.jsonl` 존재. 전체/플랫폼별/단일 세션 export 지원, full message history 포함
- **데이터 저장소 정정**: ChromaDB는 사용하지 않음. **SQLite + FTS5 단일** — 암호화는 SQLCipher 단일 적용으로 충분 (차단조건 #1 단순화)
- **마이그레이션 도구**: `hermes claw migrate` (OpenClaw → Hermes) 존재. 역방향 export는 sessions 단위로 가능
- **스키마 버전 관리**: `schema_version` 테이블 존재
- **R2 위험 등급**: CRITICAL → **HIGH** (skills/memory 범위는 P1 설계 단계에서 추가 검증)
- **추가 검증 항목**: `hermes sessions export`가 sessions만 다루는지, agent-curated memory와 skills도 포함하는지 P1에서 확인 필요

### A.3 차단조건 영향
6개 차단조건은 **그대로 유지**. 검증 결과는 충족 가능성을 높였을 뿐 의무를 약화하지 않음.
- #1 SQLCipher: 적용 대상이 SQLite 단일 → 구현 단순화
- #2 JSONL export: 공식 명령어 활용. skills/memory 범위 보강 필요
- #3 버전 핀: 그대로
- #4 어댑터 추상화: 그대로 (P1 설계의 핵심)
- #5 2 provider always-on: 그대로
- #6 Docker 격리: 그대로
