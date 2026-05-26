# 3+1 합의 보고서: P1 (LLM Provider 추상화 설계) 검증

**날짜**: 2026-05-04
**검증 대상**: `docs/architecture/llm-providers-design.md` (P1, 665줄)
**상위 결정**: ADR-008 (Hermes 도입, Option B). 본 P1은 차단조건 #4·#5 충족 메커니즘
**관련 합의**: `3plus1-consensus-2026-05-04-hermes.md` (Reviewer가 Agent C에 메타 가중치 부여한 선례)

---

## 사전 점검 — Provider Liquidity 위반 여부

본 안건은 다중 provider 추상화 설계 자체이며, Liquidity 원칙(2개 이상 active provider 의무)을 약화시키지 않는다. Agent B의 "최소 2 active 회피 가능" 지적은 Liquidity **강화** 방향, Agent C의 LiteLLM 승격안 또한 multi-provider liquidity를 보존(Router의 fallback/cooldown으로 강화). **반려 사유 없음 — 합의 진행.**

---

## Phase 2 — 3 에이전트 독립 분석 요약

### Agent A (구현 분석가) — APPROVE with revisions
- Adapter 인터페이스: 4 provider 조건부 수용 (system/tool_use 왕복/multimodal/streaming chunk 타입 정규화 누락)
- 폴백 race 5종: 헬스체크 전이, active=2 검증, rate-limit thundering herd, OAuth refresh, streaming 이중 출력
- depcruise 회피 6종: importlib 동적, 전이 의존, 테스트 예외, monkey-patch, 모델명 분할/base64/alias, alias에 의미 부여
- 추가 발견: §4.1 health(provider_key) 외부 노출 모순, MVP에 헬스체크 빠진 §6.3 시나리오 모순, Phase 1 시나리오 ollama 미포함(§6.2 위반)

### Agent B (품질·안전성) — APPROVE with revisions
- 위반 패턴 6종 평가: #2/#6만 정규화로 강제, 나머지 4종(#1/#3/#4/#5) 가이드/체크리스트(추론적). 차단조건 #4 미충족
- OAuth 누출 위험: yaml 평문, 메트릭 redaction 미명시, health_check 인증 echo, mount 권한 강제 없음
- "최소 2 active" 회피 경로: 시작 시 1회만 검증, 자동 강등 후 재검증 없음, standby가 폴백 체인엔 들어가나 active 카운트 빠짐, 동일 type 2개 등록 시 권장만
- 추가 위험 7종 (R1~R7): 메트릭 PII, metadata raw dict 누출, yaml 비밀, stateless 위반, alias 무결성, health_check 인증 노출, OpenRouter 분기 폭증

### Agent C (대안 탐색가) — APPROVE with revisions (LiteLLM 승격 권장)
- 자체 Adapter 비용: ~600 LOC + 신규 type ~80~150 LOC + SDK 추적 ~16~32h/년 + 테스트 ~600 LOC, 연간 ~40~80h
- LiteLLM 통합 비용: facade ~100 LOC + 학습 ~4~8h, 연간 ~5~10h
- LiteLLM이 §3·§4·§5·§6·§9의 80% 자체 제공 — 위반 패턴 #1·#2·#5·#6 자연 차단
- ADR-004 본질 위반: P1은 외형(config-driven)만 차용, 본질("외부 SDK 우선") 정면 모순

---

## Phase 3 — 교차 비교

### 일치 (3자 동의)
1. 결론 등급: 전원 APPROVE with revisions (근본 폐기 없음, revision 폭에 합의 없음)
2. **Adapter 스키마 결손 만장일치** — A(system/tool_use/multimodal/streaming), B(metadata raw dict), C(정규화 부족)
3. **차단조건 #4 자기충족 미흡 만장일치** — A(depcruise 회피 6종), B(P5 위임+추론적), C(LiteLLM facade 1줄로 단순화)
4. **차단조건 #5 충족 미흡 만장일치** — 시작 시 1회 검증만으로 부족
5. 자동 강등/폴백 시 운영 안정성 공백 만장일치 (degraded 모드 명세 필요)

### 부분 일치
- **자체 Adapter 채택 정당성**: A·B 채택 자체엔 이견 없음 vs C 반대 (ADR-004 본질 위반) → **메타 한계 가중치로 사용자 결정 옵션 격상** (Option α/β)
- **메트릭/메타 PII·토큰 누출**: A·B 합의 (필수 보강), C 미언급 → 양 옵션 모두 redaction 의무화
- **헬스체크 인증 노출**: A·B 합의, C 미언급 → 헬스체크 명세 본 문서 자기충족화 필수

### 불일치 — 본 합의 최대 분기점
**§14 "v2.0 LiteLLM 검토" 일정 적정성**:
- A·B: 침묵 (암묵적 수용, 적극적 동의 아님)
- C: v1.0(MVP)로 승격 — 매몰비용 누적 회피
- **결정**: 정량 근거(LOC, 유지부담) 제시한 C 의견에 가중치. **사용자 결정 옵션으로 분기**

### 누락 (단독 발견 → 합의안 포함)
- [A CRITICAL] 폴백 race 5종 (특히 OAuth refresh = ADR-008 R1 재현 통로)
- [A HIGH] §4.1 health(provider_key) 인자 모순
- [A MEDIUM] stream 합 타입화 (AsyncIterator[StreamEvent])
- [B HIGH] OAuth credentials 처리 명세 부재 (mount/env/echo)
- [B HIGH] 동일 type 2개 active 금지를 권장→강제 격상
- [B HIGH] LLMResponse.metadata raw dict 화이트리스트화
- [B HIGH] §6.1 fail-fast vs 자동 강등 결합 시 정전 → degraded 모드
- [C CRITICAL] ADR-004 본질 위반 (외형만 차용)
- [C HIGH] 이전 Hermes 합의 Reviewer 보정 정신과 P1 모순

---

## Phase 4 — 최종 합의

### 합의된 결론 (한 문장)
**P1은 현재 상태로 승인 불가이며, ADR-008 차단조건 #4·#5 충족을 위해 상위 2개 옵션 중 사용자 결정 후 필수 12개 보강을 적용해야 한다.**

### 사용자 결정 옵션

#### Option α — 자체 Adapter 유지 + 강화 보강 (P1 현행 노선)
- **의미**: 자체 Adapter 4개 v1.0에 그대로 작성. 차단조건 #4·#5는 정적 룰 + runtime sentinel + active 재검증으로 자력 충족
- **비용**: ~600 LOC + 차단 테스트 ~600 LOC + 연간 ~40~80h 유지
- **장점**: 외부 SDK 종속성 회피, 모든 동작 자가 통제
- **단점**: ADR-004 본질 위반 가능성, 위반 패턴 차단을 100% 자력 구현
- **추가 의무**: ADR-004 정합성 별도 ADR 작성

#### Option β — LiteLLM facade 1차 채택 (Agent C 승격안) ⭐ Reviewer 권고
- **의미**: §14 v2.0 LiteLLM을 v1.0(MVP)로 승격. §4 Adapter는 LiteLLM facade ~100 LOC. ADR-008 차단조건 #4 "어댑터 1개"는 LiteLLM facade가 충족. 자체 Adapter는 v2.0 백업
- **비용**: facade ~100 LOC + facade 보강 ~150 LOC + 테스트 ~200 LOC, 연간 ~5~10h
- **장점**: 위반 패턴 #1·#2·#5·#6이 LiteLLM 정규화로 자연 차단, ADR-004 정신 보존, 연간 유지부담 1/3~1/5, P1 LOC 62% 감축
- **단점**: latency +20~80ms (proxy 모드만), LiteLLM 신규 provider 지원 종속성
- **추가 의무**: v2.0 자체 Adapter 진입조건 ADR 작성

#### Reviewer 권고
**메타 한계 보정 + Hermes 합의 일관성 + ADR-004 정합성 3중 가중치 적용 시 Option β 권장.** 단, Option α도 "ADR-004 정합성 ADR + 12개 보강 완전 이행" 조건부 유효.

---

### Revision 항목 통합

#### 옵션 무관 — 양쪽 모두 필수 (12개)

| # | 항목 | 우선순위 | 출처 |
|---|------|---------|------|
| R1 | LLMRequest 스키마 보강 (system/response_format/tool_choice/stop_sequences/stream) | CRITICAL | A |
| R2 | LLMResponse.metadata raw dict 금지 → 화이트리스트 구조화 | CRITICAL | B |
| R3 | 메트릭/예외/응답 redaction 필터 의무화 (PII·토큰) | CRITICAL | A,B |
| R4 | 런타임 active≥2 재검증 (모든 강등 경로 + degraded 모드) | CRITICAL | A,B |
| R5 | 동일 type 2개 active 금지를 권장→강제 | HIGH | B |
| R6 | OAuth refresh single-flight 잠금 (R1 재현 차단) | CRITICAL | A |
| R7 | OAuth credentials 처리 명세 (env/mount :ro+0600/echo 금지) | HIGH | B |
| R8 | 폴백 race 5종 완화 (immutable snapshot/semaphore+지터/first-token 후 폴백 금지) | HIGH | A |
| R9 | health_check dry probe + MVP 포함 일치화 | HIGH | A,B |
| R10 | §4.1 health(provider_key) 모순 해소 | HIGH | A |
| R11 | stream 반환 타입 AsyncIterator[StreamEvent] | MEDIUM | A |
| R12 | tool_use·tool_result 정규화 명세 또는 명시 비지원 | HIGH | A |

#### Option α 추가 (5개)
| # | 항목 | 우선순위 |
|---|------|---------|
| Aα-1 | depcruise allowlist + httpx 직접 호출 차단 | CRITICAL |
| Aα-2 | AST 동적 import 차단 룰 | CRITICAL |
| Aα-3 | runtime sentinel (provider 모듈 wrapping 검증) | HIGH |
| Aα-4 | routing alias 네이밍 컨벤션 + 의미 부여 금지 | HIGH |
| Aα-5 | ADR-004 정합성 ADR 작성 | CRITICAL |

#### Option β 추가 (4개)
| # | 항목 | 우선순위 |
|---|------|---------|
| Bβ-1 | §4 Adapter를 LiteLLM facade로 재정의, §14 LiteLLM v1.0 승격 | CRITICAL |
| Bβ-2 | depcruise 룰 단순화 (litellm 외 LLM SDK 직접 import 금지) | HIGH |
| Bβ-3 | LiteLLM 자체 redaction 검증 + 부족분 facade 보강 | HIGH |
| Bβ-4 | v2.0 자체 Adapter 진입조건 ADR 작성 | HIGH |

---

### 미해결 결정 (사용자 입력 필요)
1. Option α vs β 선택 (본 합의 핵심)
2. Option β 채택 시 LiteLLM SDK 모드 vs Proxy 모드 (SDK 권장)
3. Option α 채택 시 ADR-004 정합성 ADR 작성 시점 (선결 vs 동시)
4. R3 redaction의 화이트리스트/블랙리스트 방식 (화이트리스트 권장)
5. R4 degraded 모드 사용자 노출 방식 (UI/로그/메트릭 — P3와 연계)

---

### 위험 알림

#### CRITICAL
- C-1: P1 채택은 ADR-004 사실상 무력화 (헌법 위계). ADR-004 정합성 ADR 없이 Option α 진행 위험
- C-2: OAuth refresh race는 ADR-008 R1 재현 통로. R6 누락 시 재발 가능
- C-3: 메트릭 PII + metadata 누출은 헌법 제8조 위반 직접 통로 (R2·R3 누락 시)
- C-4: 시작 시 1회 검증만으로는 차단조건 #5 충족 불가 (자동 강등 후 1 active 전락 가능)

#### HIGH
- H-1: Option α 시 위반 패턴 #1·#3·#4가 추론적 검증 의존 — 헌법 제3조 위반 (Aα-1~3로 격상 필수)
- H-2: 메타 한계 — 3 Claude 에이전트 → 자체 Adapter 친화 편향 가능. Reviewer는 C에 가중치 부여
- H-3: Phase 1 시나리오 ollama 미포함으로 §6.2 type 다양성 위반 — P1 본문 정정 필수

---

## LiteLLM 승격(Option β) 채택 시 P1 재작성 가이드

11개 섹션별 변경 사항:
1. §3 Provider 정의: 유지 + LiteLLM model prefix 매핑
2. §4 Adapter: 전면 재작성 (LiteLLMAdapter ~100 LOC)
3. §5 Fallback: LiteLLM Router 위임
4. §6 Liquidity: 유지 + R5+R4 추가
5. §7 Health: dry probe + Router cooldown 통합
6. §8 메트릭: LiteLLM callback + R3 redaction
7. §9 OAuth: facade 격리 + R6+R7
8. §13 ADR-004 정합성: 재작성 ("본질 따름")
9. §14 v2.0 로드맵: "자체 Adapter 진입조건"으로 변경
10. §16 차단 검증: LiteLLM 자연 차단 활용
11. §4.1 health 모순: Router health 활용

**LOC 영향**: 자체 Adapter ~1200 → LiteLLM facade ~450 (62% 감축)
