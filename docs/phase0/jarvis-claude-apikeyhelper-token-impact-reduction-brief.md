# Jarvis claude code 워커 자격 영향 축소 — apiKeyHelper 제한 토큰 (v1.1)

> **본 brief = 설계 정리 한정.** staged: brief v1 → **3+1 합의(4 source, REVISE)** → **brief v1.1(본 문서)**. ⭐ **귀결 = DEFER (BL-1 토큰 scope 실측 기반 *증거*로 확정)**. DESIGN 청사진 보존, 발효는 실 trigger 까지. 코드 전 문서 먼저(SDD). 자동 다음 단계 진입 0([[feedback_staged_consensus_workflow]]).

---

**작성일**: 2026-05-30
**Status**: **v1.1 — 3+1 합의(REVISE×2+AWC×2) 흡수 + BL-1 토큰 scope *실측 완료*. ⭐ 결론 = 구현 DEFER(증거 기반). 영향 축소 이득이 과금 전환·새 노출면 비용에 비례하지 않음(실측이 OAuth blast=bounded 확인). §6 Q1=DEFER, Q8=ADR-014 보강.**

## v1.1 변경 이력 (3+1 합의 + BL-1 실측)

| # | v1 → v1.1 | 출처 |
|---|---|---|
| 🔴 BL-1 ⭐ | **토큰 scope 실측 완료 → DEFER 증거 확정**(§0.4 신설): OAuth 토큰 scope = `user:inference`+`profile`+Claude Code 운영(계정/결제 관리 *없음*), Max 5x **rate-limited**. blast 실제 bounded → apiKeyHelper(종량 $)가 영향 축소 불분명 | C·codex(순서) + 실측 |
| 🔴 BL-2 | **over-claim 잔존 정정**: line 9 "blast bounded" 제거 + §3 "측정 가능한 이득" → "구조적 변화(OAuth 복제본 0)만, 순이득 정도 미검증" | B·codex |
| 🔴 BL-3 | **헬퍼 변조 벡터 + spend cap 한계**: 가짜홈 RW 내 헬퍼/키 = exfil + *임의 코드 실행* 노출면. spend cap=손실 상한(공격자 한도 전액 소진 가능) | B·codex |
| 🔴 BL-4 | **revoke 독립성 하향 + 별도 계정 대안**: "키 단위 독립(계정 단위 미확인)" + §6 Q2 에 별도 Anthropic 계정/구독(과금모델 유지+격리) 추가 | B·codex·C |
| 🔴 BL-5 | **검증 정도 + claude fail-mode**: §5 에 OAuth vs API 키 권한 실측 비교 + 헬퍼 빈출력 시 claude fail-mode(raise/hang/빈출력 = 100 entry) calibration | B·A |

**합의 보고서**: `docs/review/3plus1-consensus-2026-05-30-jarvis-apikeyhelper-impact-reduction.md`
**진입 단위**: 레벨 3 합의(REVISE×4)가 풀 net 격리 대신 검토한 **영향 축소(Q1-b)** — 가짜홈의 OAuth refresh 토큰(2부 복제) 대신 scope/spend 제한 전용 API 키를 apiKeyHelper 로 주입. (BL-1 실측 결과 영향 축소 이득 불분명 → §0.4·§2 DEFER 결론.)
**상위 문서**: `ADR-014`(레벨 2, 잔여=net exfil) · `docs/review/3plus1-consensus-2026-05-30-jarvis-net-egress-isolation.md`(Q1-b 채택) · net 격리 brief v1.1
**근거**: [[feedback_proportionate_security_personal_tool]] · [[feedback_pass_scope_overclaim]](§0.3 "단명" 정정) · [[feedback_boss_role_not_smartest]] · [[project_minimize_user_intervention]] · 헌법 8조·5조(provider liquidity)

---

## §0 배경 — 영향 축소 패러다임 + apiKeyHelper 실측

### §0.1 왜 (레벨 3 합의의 귀결)
레벨 3 net 격리는 prevention 부적합(정당 채널 exfil 불가차단)으로 DESIGN-DEFER. 합의 결론 = **prevention → 영향 축소**: net 으로 자격이 새는 것을 막는 대신, **새더라도 피해를 줄인다**. 현 가짜홈은 진짜 홈의 **OAuth refresh 토큰**을 복사(ADR-014 Q3, 2부 복제)하므로 exfil 시 *사용자 구독 세션 전체* 오용 + revoke 가 진짜 홈 로그인까지 영향.

### §0.2 apiKeyHelper 실측 (claude-code-guide 확인)
- **동작**: `settings.json` 의 `apiKeyHelper` = 스크립트 경로. claude 가 `/bin/sh` 로 실행 → stdout 의 키를 모든 요청 인증 헤더(X-Api-Key / Bearer)로 사용. 인증 우선순위에서 OAuth(`/login`)보다 위 → **OAuth 자격 없이 headless `claude -p` 인증 가능**(credentials.json 불요).
- **재호출 TTL**: `CLAUDE_CODE_API_KEY_HELPER_TTL_MS`(기본 5분) = 헬퍼 *재호출* 주기 + 401 시 즉시 재호출. **키 *만료* 아님**.
- **API 키 제어**: Anthropic Console — **spend(지출) 한도 ✓ · project/workspace scope ✓**. **자동 만료(단명) = 네이티브 미지원**(확인).
- **실행 컨텍스트**: 헬퍼는 claude 본체 프로세스(/bin/sh)에서 실행 → claude 가 sandbox 안이면 헬퍼도 sandbox 안 → **출력 키가 워커 프로세스에 노출**(메모리/헤더).

### §0.3 ⚠️ 정직 단서 (over-claim 방지)
- 🔴 **"단명 토큰" = over-claim**(레벨 3 합의 용어 정정): Anthropic API 키는 *자동 만료 안 함*. apiKeyHelper TTL 은 재호출 주기일 뿐. 실제 속성 = **"전용 workspace 키 + spend 한도 + 독립 revoke + (수동/주기) 로테이션"**. "단명"은 로테이션을 우리가 구현할 때만([[feedback_pass_scope_overclaim]]).
- 🔴 **prevention 아님 = 영향 축소**: 헬퍼 키도 sandbox 안 워커에 노출(§0.2) → exfil *여전히 가능*. 이득 = exfil 된 자격이 *capped·revocable 키*(OAuth 세션 아님). "exfil 차단"으로 표기 금지.
- 🟡 **blast radius 미검증 전제(레벨 3 BL-1)** → **§0.4 에서 실측 해소**(아래).

### §0.4 ⭐ BL-1 토큰 scope 실측 (2026-05-30, 코드 변경 0, 토큰 값 미노출)
`~/.claude/.credentials.json` 의 OAuth 토큰 *선언* scope 를 직접 읽음(라이브 API probe 는 자격 오용 위험 → 미실행):
- **scopes**: `user:inference` · `user:profile` · `user:file_upload` · `user:mcp_servers` · `user:sessions:claude_code`. **subscriptionType=`max`**, **rateLimitTier=`default_claude_max_5x`**.
- **함의 (blast radius)**: 토큰이 할 수 있는 것 = **Max 구독으로 추론(flat-rate + rate-limited)** + 프로필(경미 PII) + Claude Code 운영. **계정/결제 *관리* scope·org admin·명시적 대화 export scope 부재** → **계정 탈취급 아님, 실제로 bounded**.
- **⭐ apiKeyHelper 결정 반전**: "OAuth > API 키" 전제가 약함. exfil 시 — OAuth = *rate-limited 구독 남용($ 추가 0)* vs API 키 = *종량 $ 남용(spend cap 까지 전액)*. **apiKeyHelper 가 영향을 줄이는지 불분명**(오히려 $ 측면 악화 가능) + 과금 전환·헬퍼 변조 노출면 추가 → **영향 축소 이득 < 비용 → DEFER(증거 기반)**.
- **잔여 미확인(정직)**: `user:sessions:claude_code` 가 *과거 세션/대화 내용 읽기*까지 허용하는지는 scope 이름만으론 불확정(서버 enforcement 미검증, 안전상 probe 안 함) — BL-1 유일 잔여.

---

## §1 ⚠️ 핵심 트레이드오프 — API 과금 (구독 아님)

**가장 중요한 결정 인자**(Q1): 현 워커는 OAuth = **구독 크레딧**으로 동작(실측: `claudeAiOauth`, Pro/Max). apiKeyHelper + API 키 = **API 과금**(per-token, Console 청구). 즉 영향 축소의 *대가* = **워커의 claude 호출이 구독에서 종량 API 과금으로 전환**.
- spend 한도로 상한은 두나, 비용 *모델*이 바뀜(구독 정액 → 종량).
- 대안: `CLAUDE_CODE_OAUTH_TOKEN`(Bearer, 구독) — apiKeyHelper 가 OAuth 토큰을 출력할 수도. 단 **구독 OAuth 토큰은 scope/spend 제한·독립 revoke 가 없음**(=현 2부 복제와 동일 자격). → **capped·revocable 자격을 얻으려면 사실상 별도 API 키(과금) 또는 별도 계정 필요**. 영향 축소 ⟺ 과금 전환이 묶여 있음.

## §2 ⭐ 결론 — DEFER (BL-1 실측 기반). DESIGN 청사진은 보존

§0.4 실측이 Q1 을 *증거로* 결정: **OAuth 토큰 blast 가 이미 bounded**(rate-limited Max 추론 + 경미 프로필, 계정/결제 관리 부재)이고, apiKeyHelper(종량 $)가 영향을 줄이는지 불분명(오히려 $ 악화 가능) + 과금 전환·헬퍼 변조 노출면 비용 추가 → **지금 구현하지 않음**(레벨 3 net 격리 DEFER 와 동일 논리, [[feedback_proportionate_security_personal_tool]]).

**발효 trigger(이때 아래 설계 발효)**: (i) `user:sessions:claude_code` 가 대화 데이터 읽기까지 허용으로 판명 (ii) 종량 과금 수용 의사 (iii) 워커가 `--real-workers` opt-in bounded 사용 이탈(상시/광범위). 아래는 trigger 시 즉시 구현 가능한 *보존 청사진*.

### 보존 설계 (발효 시)
```
provision_claude_home (변경 — 발효 시):
  - 진짜 홈 .credentials.json(OAuth) 복사 *중단*  ← OAuth 복제본 0 (구조적 변화)
  - 가짜홈 settings.json 에 apiKeyHelper = <키 출력 스크립트> 설정
  - OAuth fallback 미보존  ← 보존하면 복제 부활, fail-closed 선택
키 출처: Console 전용 workspace 키(spend 한도) 1회 생성 → 헬퍼 출력
```
- **fail-closed**: 헬퍼 실패 시 OAuth fallback 미보존 → 워커 인증 실패. 단 claude fail-mode(빈출력 hang=100 entry) calibration 필요(§5).
- **키 저장**(BL-3): 헬퍼/키는 sandbox 안(claude 가 sandbox 안이라 밖 도달 불가) → 워커가 *읽기·쓰기* 가능 = exfil + **헬퍼 변조=임의 코드 실행** 노출면. "capped 노출 수용"으로만 기술.

## §3 안전 논증 / 정직 (§0.3·§0.4 답습)

- **영향 축소 = exfil 된 자격의 *가치* 하향**(차단 아님). exfil 채널(정당 API·DNS·SNI)은 레벨 3 DEFER 로 그대로.
- **"측정 가능한 이득" 정정(BL-2)**: 측정 가능한 건 *구조적 변화*(OAuth 복제본 0)뿐 — **자격은 0 이 안 됨**(평문 API 키가 가짜홈 RW 에 새로 상주, 제거 아닌 교체). 보안 *순이득 정도*는 §0.4 실측상 *불분명~음(-)*.
- **spend cap = 손실 상한, 오용 방지 아님(BL-3)**: 공격자는 exfil 한 키로 한도 *전액* 자유 소진.
- **revoke 독립성 하향(BL-4)**: "키 단위 독립"일 뿐, 같은 Anthropic 계정/workspace 면 *계정 단위* 독립 미확인.
- **env allowlist 정합**: apiKeyHelper 경유면 `ANTHROPIC_*` env 차단 유지 가능(전용 키만 헬퍼 stdout). 단 헬퍼/키 평문이 가짜홈에 = 노출면(위).
- **로테이션 미구현 시 "단명" 아님**: 키는 revoke 까지 유효.

## §4 비례성 — 핵심 판단 (DEFER)

- ⚠️ **핵심(Q1, 실측 해소)**: 영향 축소 이득(구조적 OAuth 복제본 0 + capped)이 **API 과금 전환(영구) + 헬퍼 변조 노출면**에 *비례하지 않음* — §0.4 실측이 OAuth blast=bounded 확인 → 줄일 게 별로 없음. 워커가 `--real-workers` opt-in bounded 사용이므로 OAuth exfil 잔여 *수용*이 비례적. **레벨 3 DEFER 와 일관.**
- **자동 만료 키·풀 로테이션 안 함**(Anthropic 미지원·과잉).
- **저비용 보완재(R)**: 과금/계정 분리 없이 Console 사용량 알림 + 수동 revoke runbook = detection(이상 사용 시 trigger). opt-in 단계 최우선.

## §5 검증 계획 (구현 채택 시)

1. PoC(토큰/과금 소량): 전용 키 + apiKeyHelper 로 가짜홈(OAuth 부재) + Landlock 에서 `claude -p` 인증·동작 ✅(레벨 2 calibration 패턴). credentials.json 부재 확인.
2. 음성: 가짜홈에 OAuth refresh 토큰 부재 + 헬퍼 키가 capped(spend 한도 동작) 실증.
3. 트랙 A: provision 이 OAuth 미복사 + settings.json apiKeyHelper 설정 + 헬퍼 실패 시 fail-closed 단위 테스트.

## §6 열린 질문 — ✅ 사용자 결정 (2026-05-30)

| # | 질문 | ✅ 결정 | 근거 |
|---|------|--------|------|
| **Q1 ⭐** | 지을 가치 | ✅ **토큰 scope 실측 선행 → DEFER**(§0.4) | 실측: OAuth blast=bounded(rate-limited 추론, 계정관리 X) → apiKeyHelper 영향축소 불분명 + 과금/노출면 비용. 4/4 합의 |
| Q2 | 자격 종류 | (발효 시) API 키만 유의미 + 별도 계정 대안 비교. OAuth 토큰=영향축소 0 | C·codex |
| Q3 | OAuth fallback | (발효 시) 미보존(fail-closed) | 전원 |
| Q4 | 키/헬퍼 위치 | sandbox 내 노출 *불가피*(밖=claude 도달 불가) + 헬퍼 변조 벡터 | A·BL-3 |
| Q5 | spend 한도 | (발효 시) 매우 낮은 월 한도부터 | codex |
| Q6 | 로테이션 | 미구현=단명 아님, revoke runbook | 전원 |
| Q7 | env allowlist | ✅ apiKeyHelper 경유(ANTHROPIC_* 차단 유지) | 4/4 |
| Q8 | ADR | ✅ **ADR-014 보강**(신규 안 만듦) | 4/4, [[feedback_ceremony_inflation]] |

---

## 부록 — 답습 교차
ADR-014(레벨 2·net resolution — 본 brief DEFER 보강 대상) / 레벨 3 합의(Q1-b) / 헌법 8조·5조 / [[feedback_proportionate_security_personal_tool]](Q1 DEFER) · [[feedback_pass_scope_overclaim]](§0.3·§0.4·BL-2) · [[feedback_boss_role_not_smartest]] · [[project_minimize_user_intervention]] · [[feedback_ceremony_inflation]] · [[feedback_staged_consensus_workflow]].
