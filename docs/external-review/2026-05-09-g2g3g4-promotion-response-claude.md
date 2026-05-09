외부 LLM 검토 응답 — G2/G3/G4 동시 PASS 승격 평가
검토자: Claude (Anthropic)
검토일: 2026-05-09
판정: APPROVE WITH CONDITIONS (조건부 승인)

0. 메타 면책 (먼저 읽어주세요)
본 검토자는 Claude이며, DRAFT 작성 컨텍스트와 다른 세션이라 해도 동일 모델 패밀리입니다. §8 제1 한계가 지적한 자기참조 위험을 완전히 해소하지 못합니다. 따라서 본 응답은 외부 의견 1건으로 카운트하되, GPT-5.x 또는 Gemini 추가 의견 1건 이상을 P2 v3 정식 채택 전 필수로 권고합니다 (§10.4 차원 4 응답에 상세).
이 점을 명시한 위에서, 4 차원 평가를 진행합니다.

1. 차원 1 — 운영 가능성 (Operability)
판정: 부분 우려 (concerns)
1.1 명료성
G2 6 GP, G3 22 권한, G4 17 schema 필드는 enumeration 자체는 충분히 명료합니다. 구현자 인계 가능 수준의 디테일이 있고, (a)~(e) 5조건 패턴이 일관되게 적용되어 검증 가능성(verifiability)도 확보되어 있습니다.
1.2 결정적 결함: PoC 미실증
§3.3에서 명시적으로 인정한 부분이 가장 큰 문제입니다:

"GP-1: (a)~(e) 모두 G1b PASS evidence 로 흡수
GP-2 ~ GP-6: (a)~(e) 미충족 — PoC + 합의 필요"

여기서 (b) 조건은 "격리 환경 PoC 실증 (Docker)"입니다. 5개 GP가 (b)를 충족하지 못한 상태에서 G2 PASS는 게이트 자체 정의에 반합니다. G3, G4도 사양 단계이며 §5.4가 인정하듯 "Migration script 사양 (구현 본 초안 외)" — 즉 라운드트립 PoC가 아직 없습니다.
이는 단순한 보강 사항이 아니라 게이트 자체 정의에 따른 필수 조건 미달입니다.
1.3 1인 개발자 스케일 부담
코드 0줄 + 마크다운 약 50개 + 거버넌스 합의 보고서 다수 = process-to-output 비율이 비대칭. 6 GP + 22 권한 + 17 schema 필드는 엔터프라이즈 멀티팀 플랫폼에 적정한 규모이며, 1인 메타-템플릿에는 2~5배 과잉으로 보입니다. 추후 실제 프로젝트 인스턴스에서 거버넌스 부담이 작업 흐름을 침해할 가능성이 큽니다.
1.4 검증 가능성
(a)~(e) 5조건 중 (a)(b)(d)는 검증 가능, (c)(e)는 행정적입니다. 그러나 GP-1의 "G1b 흡수" 주장은 부분적으로 의심스럽습니다 — G1b는 SQLCipher trigger + Tier-1 42 catalog로 검증되었으나 GP-1의 범위는 SessionDB/Memory DB/Skill DB 전체이고, Tier-2/Tier-3 catalog 검증 상태가 명시되지 않았습니다. 흡수의 완전성 입증이 부족합니다.

2. 차원 2 — 보안 / 거버넌스 견고성
판정: 골격은 견고, 일부 누락
2.1 자기참조 차단의 실효성
G3 §4 (Hermes 단독 합의 금지 / Reviewer-only / 외부 LLM / 사용자 최종 권위)는 원칙적으로 자기참조를 차단합니다. 그러나:

메타-순환 관찰: G3 §4가 "Hermes 관련 결정에 외부 LLM 필수/권장"을 명시하지만, G3 DRAFT 자체의 검토는 Reviewer-only였습니다. 즉, 외부 LLM을 의무화하는 규칙이 외부 LLM 없이 작성·검토되었습니다. 본 검토가 그 공백을 메우는 첫 시도라는 점은 인정하지만, 이 메타-순환 자체는 명시 기록 + ADR Amendment로 청산되어야 합니다.
잠재적 우회 경로: Hermes가 합의 결과를 "기록 only" 한다 해도, 기록 시점의 요약 편집권(어떤 evidence를 ledger에 어떤 순서/표현으로 적재할지)은 silent influence 채널이 됩니다. G3 §4가 "Hermes는 기록 만 가능"이라고 명시하지만 기록 형식에 대한 제약(canonical JSON / 사용자 사전 정의 템플릿)은 명시되지 않았습니다.

2.2 P1~P8 위반 경로 enumeration의 완전성
빠진 후보 경로:

P9 후보 — Memory poisoning side-channel: Memory 내용 자체가 미래 Worker/Reviewer 결정에 lock-in 방향으로 영향. G4 §5 boundary 1이 "Memory ≠ policy"를 차단하지만, 판단 형성에 대한 영향은 차단되지 않음. (예: Project memory에 "Claude가 가장 신뢰할 만한 모델"이라는 진술이 누적되면 향후 결정에 편향.)
P10 후보 — Provider-specific endpoint hardcoding: skill 본문이 https://api.anthropic.com/v1/messages 같은 URL을 직접 박는 경우. depcruise는 import만 검사, URL 문자열은 검사 못 함. P6 facade 우회의 변종.
P11 후보 — CLAUDE.md / 프롬프트 파일 lock-in: harness 파일 자체가 Claude 특화 표현/포맷에 의존하면 다른 모델로 교체 시 동작 저하. Provider Liquidity의 prompt-level 차원.

이 셋은 현 P1~P8을 무효화하진 않지만, deferred candidates로 명시 기록 권고.
2.3 단일 실패점 (SPOF)
G2 §9 + G3 §4 + G3 §5.5 의 상호 의존이 의심대로 SPOF입니다. 핵심 메커니즘은:
governance-preconditions.md filesystem read-only
+ Hermes-originated commit auto-reject
+ T3 변경 감지 hook
세 메커니즘이 모두 동일 호스트 OS 권한 모델에 의존합니다. 컨테이너 escape, host 측 git hook 비활성화, IDE GUI를 통한 직접 편집 등은 차단되지 않습니다. "1인 개발자가 동일 호스트에서 모든 도구를 운영"하는 환경의 본질적 한계 — 이를 해소하려면 별도 머신/별도 사용자/외부 git remote의 audit log 비교 등 추가 layer가 필요한데, 1인 메타-템플릿 스케일에서는 ROI가 낮습니다.
→ SPOF는 현실적으로 수용 가능하지만, "known accepted risk"로 명시 기록되어야 합니다 ("우리는 이 SPOF를 알고 있고, 1인 스케일에서는 추가 layer가 비효율적이므로 의도적으로 수용한다").
2.4 Provider Liquidity 보장의 견고성
G4 #15 provider_bindings의 "optional optimization 한정 / required·exclusive 금지 / 최소 2 provider 재해석 가능" 제약은 강력합니다. 그러나 enforcement는 PR review + depcruise에 의존 — depcruise는 코드 수준은 잡되 의미적 lock-in (특정 모델의 특정 출력 포맷에 대한 가정)은 못 잡습니다. P2-5 라운드트립 검증이 진짜 enforcement 입니다 — 그것이 PoC 미실증이라는 것이 다시 차원 1 결함과 연결됩니다.

3. 차원 3 — 단순화 / 대안
판정: 강한 단순화 권고
3.1 동시 PASS vs 단계별 PASS
§7 (3-way 의존성) 논거 — "G2 §9 메타 안전장치는 G3 운영 구현이 없으면 interface만으로 무력화" — 는 타당합니다. 인터페이스 정합성 측면에서 묶음 검토가 합리적입니다. 그러나 "묶음 검토" ≠ "묶음 PASS" 입니다. 묶음 검토 후 단계별 PASS 도 가능합니다:

옵션 4 (제안): 묶음 검토 + 단계별 PASS — 본 합의에서 3 게이트를 동시에 검토하되, PASS는 PoC 실증 순서대로 (예: G4 형식 → G2 GP-2~6 → G3 운영) 부여.

3.2 단순화 후보
G2: 6 GP → 3 카테고리 (Secrets, Provider, Validation) MVP. P3+P4 통합, P6+P7 통합, P5 단독, P1+P2 통합, P8 단독 — 4 카테고리도 가능. 6개의 분리는 운영 시점에 다시 합쳐질 가능성이 높음.
G3: 22 권한 → 12 권한. 다음과 같은 derivation rule로 압축 가능:

"Hermes는 X를 할 수 있다 ⟺ X가 Constitution/ADR/Gate 정의를 수정하지 않고, X가 Evidence Ledger에 기록되며, X가 T2/T3 분류상 사용자 승인을 요구하지 않는 경우."

이 한 규칙으로 22개 중 약 10개가 derivable. 명시적 enumeration은 학습 자료로 유용하지만 운영 시 cognitive overhead.
G4: 17 → 8 MVP 필드 (id, name, version, scope, allowed_actions, forbidden_actions, promotion_status, provider_bindings). 나머지 9개 (description, inputs, outputs, required_evidence, required_tests, rollback_triggers, created_from, last_verified_at, owner)는 사용 시점에 incrementally 추가. 17 필드 모두 작성 의무로 두면 skill 작성 자체가 부담.
3.3 누락 영역
P2 v3 정식 채택 전에 반드시 확인되어야 할 항목:

ADR-009 Adapter v2.0 진입 조건의 명시 상태. G2 GP-5는 "Provider Adapter 강제 (P1 facade 단일 진입점)"인데, P1 facade가 어떤 상태일 때 GP-5가 enforceable인지 명시 부재. P1 facade MVP 정의 → ADR-009 명시 → GP-5 enforce — 이 의존 사슬 확인 필요.
Tier-2/Tier-3 canary catalog 상태. GP-1 G1b 흡수 주장의 완전성 검증.
ADR-011 §2.4 T1/T2/T3 분류와 G3 §2 22 권한 분류의 일관성 cross-check. 본 검토 범위에서 T1/T2/T3 카운트는 자체 일관적이나, ADR-011 본문과의 일대일 mapping 검증은 별도.

3.4 "계산적 비중 vs 추론적 보조"
§8 한계 4가 자체 제기한 질문에 대한 답: 현 비율은 적정하나, "계산적 = 우월" 가정에 일부 허점. 계산적 메커니즘 (regex, depcruise, SQL trigger)은 false negative 시 조용히 실패합니다. 추론적 보조 (Reviewer pattern matching, 합의 검토)는 더 비싸지만 unknown unknowns에 강합니다. GP-4 "외부 입력 검증"과 GP-6 "Memory/Skill Migration"은 추론적 보조를 우위로 설계해야 합니다 (현재 "보조"로 표현됨). pydantic schema는 알려진 형태만 잡고, 라운드트립 검증의 의미 보존성 판단은 본질적으로 추론적입니다.

4. 차원 4 — 메타 편향 / 자기참조 위험
판정: 노출은 충실, 통제는 미흡
4.1 자기참조 노출
§8이 4개 한계를 명시 enumeration한 점은 이 분야 작업물 중 상당히 우수한 transparency입니다. 숨김 없음.
4.2 외부 LLM 1+ 만으로 충분한가?
불충분합니다. 이유:

본 검토자는 Claude이며, DRAFT 작성자도 Claude. 모델 패밀리 동일성은 같은 패턴의 사각지대를 공유합니다 (예: Anthropic의 internal training distribution이 만든 reasoning shortcuts). 본 검토가 "외부"라 표시되어도 vendor-cross 검증이 아닙니다.
G3 §4.4.2가 Hermes PMO 격상에 "외부 LLM 1+ 필수"를 명시한 이유는 cross-vendor 의견을 의미한다고 보는 것이 합리적 해석. 본 합의 (G2/G3/G4 PASS)에서는 "권장"으로 약화되어 있는데, 이는 두 결정의 위험 비대칭이 그만큼 명확하지 않음을 시사.

4.3 권고
P2 v3 정식 채택 전에:

GPT-5.x 또는 Gemini로 동일 문서 재검토 (cross-vendor). 본 응답을 동봉 하면 동일 LLM 검토자가 본 응답에 동조 편향될 수 있으므로, 본 응답을 첨부하지 않은 새 의뢰가 통제 가치 더 큼.
PoC 실증 후 3rd 외부 LLM 검토 (PoC evidence 기반).
G3 §4.4.2 매트릭스 자체를 ADR Amendment로 갱신 — "Hermes 관련 결정"의 정의에 G2/G3/G4 PASS 자체가 포함되도록 명시 강화. 현 "권장"을 일부 항목에서 "필수"로 격상.

4.4 추가 자기참조 관찰
본 검토 작성 중 발견한 메타-편향 1건: §10이 4 차원 + 판정 4옵션을 미리 framework 해서 제공. 이는 평가의 형식을 사전 결정하므로 검토자가 framework 외부의 결함 (예: "왜 GP가 5개나 7개가 아닌 6개인가" 같은 fundamental 질문)을 제기할 인센티브가 약화됩니다. 이는 §8에 명시 추가 권고 사항입니다.

5. 최종 판정
APPROVE WITH CONDITIONS
본 framework은 specification-level에서 PASS 자격이 있습니다. 그러나 게이트 자체 정의의 (b) 조건이 GP-2~GP-6, G3 운영, G4 라운드트립에서 미충족이므로, 무조건 PASS는 게이트 정의에 반합니다. 다음 조건 충족 시 PASS 승격 가능:
조건 (필수)
C-1 (Specification PASS vs Operational PASS 분리): 본 합의 결과는 "specification PASS"로 한정. "operational PASS"는 PoC 실증 후 별도 보고. 두 단계의 명시적 구분을 합의 보고서에 기록.
C-2 (PoC 의무): P2 v3 정식 채택 합의 진입 전에 다음 PoC 완료 + Evidence Ledger 등재:

GP-2 (egress redaction filter), GP-3 (gitleaks/inotify), GP-4 (pydantic+sanitizer), GP-5 (depcruise rule + facade), GP-6 (JSONL 변환 라운드트립) — 각각 Docker 격리 환경
G3 핵심 T2/T3 권한 (#9, #10, #13, #14, #15, #16, #17 최소) enforcement 검증
G4 hash chain 적재/검증 + migration script 라운드트립

C-3 (Cross-vendor 외부 LLM): GPT-5.x 또는 Gemini 1+ 추가 검토 후 P2 v3 진입. 본 응답은 동봉하지 말 것 (동조 편향 통제).
C-4 (P 경로 enumeration 보강): P9 (Memory poisoning side-channel), P10 (provider-specific URL hardcoding), P11 (CLAUDE.md prompt-level lock-in)을 deferred candidates로 명시 기록. 즉시 GP 추가 의무는 아니나, 추후 합의 시 우선 검토.
C-5 (메타-순환 청산): G3 §4의 "외부 LLM 권장/필수" 자체가 외부 LLM 없이 작성된 메타-순환을 ADR-011 Amendment 또는 별도 합의 보고서에 명시 기록. 본 응답 + 후속 cross-vendor 응답이 그 청산의 evidence가 됨을 합의 보고서에 적시.
C-6 (SPOF accepted risk): G2 §9 + G3 §4 + G3 §5.5의 단일 실패점이 "1인 동일 호스트 운영 환경에서 의도적 수용된 risk"임을 명시 기록. 추후 multi-host 운영으로 전환 시 추가 layer 의무 발동 트리거 정의.
C-7 (Tier-2/Tier-3 catalog 검증): GP-1의 G1b 흡수 주장의 완전성을 위해 Tier-2/Tier-3 canary catalog 검증 상태 명시. 미검증 시 GP-1 흡수 주장을 "Tier-1 한정 흡수"로 표현 정정.
조건 (강력 권고, 의무 아님)
C-8 (단순화 검토): G2 6 GP → 3~4 카테고리, G3 22 → 12 권한, G4 17 → 8 MVP 필드 단순화 가능성 별도 합의에서 검토. 현 enumeration 유지 시 유지 근거 명시.
C-9 (ADR-009 Adapter v2.0 진입 조건): GP-5 enforceability의 전제가 되는 ADR-009 / P1 facade 상태를 P2 v3 정식 채택 전에 명시.
진행 가능 범위

✅ specification PASS 승격: 가능 (조건 C-1 충족 시)
⏳ operational PASS: PoC 후 별도 합의 (C-2)
⏳ P2 v3 정식 채택 합의 진입: C-1 ~ C-7 모두 충족 후


6. 메타 코멘트 — 검토자 자기 노출
본 검토는 약 1시간 분량의 추론입니다. 다음 사각지대가 있을 수 있습니다:

본 검토자는 Claude이므로 Claude-favoring lock-in을 덜 검출했을 수 있음
1인 개발자 환경에 대한 가정이 본 검토자의 prior에 의존
본 framework의 역사적 맥락 (R-1~R-7 합의의 세부 evidence)을 직접 확인하지 못함 — §1.2의 "코드 0줄 + 마크다운 약 50개"라는 자기 보고만으로 판단

따라서 본 응답은 단일 evidence 가 아닌, multi-LLM 평가의 한 입력으로만 다루기를 권합니다.