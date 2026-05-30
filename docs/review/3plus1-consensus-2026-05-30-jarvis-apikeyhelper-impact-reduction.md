# 3+1 합의 보고서 — Jarvis claude code 워커 자격 영향 축소 (apiKeyHelper 제한 토큰)

**일자**: 2026-05-30
**대상 brief**: `docs/phase0/jarvis-claude-apikeyhelper-token-impact-reduction-brief.md` (v1)
**프로토콜**: CLAUDE.md §3 (보안 변경 = 3+1 필수). 4 source = Agent A(구현)·B(품질/안전)·C(대안) 병렬 독립 + codex cross-vendor blind. Reviewer = 메인 컨텍스트.

---

## Phase 2 — 독립 판정 집계

| Source | 판정 | 핵심 |
|--------|------|------|
| **Agent A** | AWC | provision 교체 = 소규모·타당하나 **apiKeyHelper 인증 경로 미검증**(레벨2 calibration 은 OAuth 만) + **claude fail-mode hang(100 entry) 위험** + Q4 sandbox-밖 헬퍼 = claude 도달 불가 |
| **Agent B** | AWC | brief 정직성 모범적이나 BL-B1 "측정 가능한 이득" over-claim(자격 0 안 됨, type swap) + BL-B2 §5 가 "정도" 미검증 방치 + ⭐ 헬퍼 변조=임의코드실행 + Q1→DEFER |
| **Agent C** | **REVISE** | ⭐ BL-C1 순서 위반(레벨3 BL-1 토큰 scope 실측 선행 필수) + BL-C2 별도 계정 대안 조기 배제 + BL-C3 비례성 자기모순(같은 bounded 위험에 영구 과금) → Q1=DEFER |
| **codex** | **REVISE** | 과금 모델 변경 정당화 실측 0 + "blast bounded" 잔존 over-claim + 헬퍼 변조 벡터 + revoke 독립성 미검증 + 별도 계정 승격 → Q1=DEFER+실측 선행 |

**종합 판정: REVISE — 귀결 = ⭐ DEFER + 레벨3 BL-1(OAuth 토큰 scope 실측) 선행.** apiKeyHelper 구현은 *기술적으로 가능·소규모*(A)이나, 같은 bounded opt-in 위험에 **영구 과금 전환** 비용 + **영향 축소 정도 미검증** → 레벨 3 net 격리와 동일 논리로 보류. 두 번째 연속 DEFER.

---

## Phase 3 — 교차 비교

### ① 일치 (Consensus)
- **C-1 ⭐ Q1 = DEFER + 토큰 scope 실측 선행**(C·codex 명시, A·B 동조): 같은 `--real-workers` opt-in bounded 위험에 구독→종량 과금이라는 *영구 비용*은 비례성 미달. 영향 축소 *정도*와 과금 정당성 둘 다 미검증.
- **C-2 ⭐ 순서 위반**(C BL-C1·codex·B BL-B2): 레벨 3 합의가 **BL-1(OAuth 토큰 scope/과금/데이터접근/revoke 독립성 실측)을 Q1 선행조건**으로 못박음(consensus net §6 Q1). 실측 0 상태 구현 진입 = 합의 결정 위반. 본 brief 가 그 선행조건 흡수해야.
- **C-3 ⭐ over-claim 잔존**(B BL-B1·codex): §0.3 정정은 모범적이나 §0(line 9) "blast bounded"·§3 "2부 복제 제거 = 측정 가능한 이득"이 잔존. **자격은 0 이 안 됨** — 평문 API 키가 가짜홈 RW 에 *새로 상주*(제거 아닌 *자격 종류 교체*). 측정 가능한 건 "OAuth 복제본 0"이라는 구조적 사실뿐, 보안 순이득 정도는 미검증.
- **C-4 ⭐ 새 노출면 = 헬퍼 변조 벡터**(B 놓친위험3·codex): 키/헬퍼가 가짜홈 RW(워커 가독·*가쓰기*) → exfil + **헬퍼 스크립트 변조 = 임의 코드 실행**(키 유출보다 심각). spend cap = *손실 상한*이지 오용 방지 아님(공격자는 한도 전액 자유 소진, B REC-B1·codex).
- **C-5 revoke 독립성 미검증**(B 놓친위험2·codex): "revoke 가 진짜 홈 로그인 무영향"은 *키 단위* 독립일 뿐, 같은 Anthropic 계정/workspace 면 *계정 단위* 독립 미확인(계정 탈취 시 동반).
- **C-6 별도 Anthropic 계정/구독 대안 = 비교표 승격**(C BL-C2·codex): 과금모델 *유지* + 격리 더 깨끗. brief §4 "안 만듦(workspace scope 충분)" 조기 배제 정정.
- **C-7 자격 종류**(전원): capped·revocable 하려면 사실상 API 키 강제(과금). `CLAUDE_CODE_OAUTH_TOKEN` = 영향 축소 거의 0(현 2부복제와 동일 자격). Q7 = apiKeyHelper 경유 > env 예외(ANTHROPIC_* 차단 유지).

### ② 추가 발견 (단일 source)
- **A**: 구현 PoC 게이트 — apiKeyHelper+OAuth부재+Landlock 인증 *미검증*(API 키 없어 여기서 PoC 불가) / claude fail-mode(헬퍼 빈출력 시 raise vs hang vs 빈출력 — 100 entry 증상) 실 calibration 필요 / Q4 sandbox-밖 헬퍼 = claude 도달 불가(키 sandbox 안 노출 불가피) / settings.json `$HOME/.claude/settings.json` 경로 미실측 / `.claude.json` OAuth 흔적 점검.
- **B**: §5 검증이 "메커니즘 동작"만 보고 "영향 축소 정도" 방치(BL-B2) / 프레이밍 비대칭(이득이 비용보다 먼저·자주) / ADR-014 (a)trigger-gated 와 (b)지금 구현의 논리 충돌.
- **C**: detection(이상 사용 모니터→수동 revoke) = 저비용 보완재 우선 / BL-1 실측을 phase 0 독립 선행 작업으로 분리.

### ③ 불일치 (Divergence)
- 판정 강도만 차이(A·B AWC = "고치면 가능하나 DEFER 권고" / C·codex REVISE = "DEFER + 실측 선행"). **실질 4/4 수렴 = DEFER**. 본질적 불일치 없음.

---

## Phase 4 — 합의 도출 → brief v1.1 (귀결 = DEFER + 실측 선행)

### 🔴 BLOCKING (v1.1 흡수 — 단, 귀결은 "구현 보류")
- **BL-1 ⭐ Q1 = DEFER + 토큰 scope 실측 선행**(C-1·C-2): apiKeyHelper 구현은 레벨 3 BL-1(OAuth 토큰 vs API 키 권한/과금/데이터/revoke 독립성 실측) *선행* 후 재결정. 이 brief = DESIGN 청사진 보존, 발효 trigger = (i) 실측이 OAuth 위험 confirm + (ii) 종량 과금 수용 또는 워커가 bounded opt-in 이탈.
- **BL-2 ⭐ over-claim 잔존 정정**(C-3): §0 line 9 "blast bounded" 제거 + §3 "측정 가능한 이득" → "구조적 변화(OAuth 복제본 0)만 측정 가능, 순이득 정도는 미검증".
- **BL-3 ⭐ 헬퍼 변조 벡터 + spend cap 한계**(C-4): 가짜홈 RW 내 헬퍼/키 = exfil + *임의 코드 실행* 노출면을 §0.3 정직단서로 승격. spend cap = "손실 상한, 오용 방지 아님(공격자 한도 전액 소진 가능)" 명시.
- **BL-4 revoke 독립성 미검증 + 별도 계정 대안**(C-5·C-6): "revoke 독립"을 "키 단위 독립(계정 단위 미확인)"으로 하향 + §4/Q2 표에 별도 Anthropic 계정/구독(과금모델 유지+격리) 추가.
- **BL-5 검증계획 정도 미검증 + claude fail-mode**(B BL-B2·A): §5 에 "OAuth vs API 키 권한 실측 비교(추가 불가면 영구 미검증 가정 명시)" + "헬퍼 빈출력 시 claude fail-mode(raise/hang/빈출력) calibration" 추가.

### 🟡 권고
- R-1 detection(이상 API 사용 모니터→수동 revoke) = 과금/계정 분리 없는 저비용 보완재 — opt-in bounded 단계 최우선.
- R-2 BL-1 토큰 scope 실측을 *독립 선행 작업*으로 분리(apiKeyHelper 구현과 분리).

### 열린 질문 — 합의 권고 + 사용자 결정
| # | 합의 | 비고 |
|---|------|------|
| **Q1 ⭐** | ✅ **DEFER + 토큰 scope 실측 선행** | 4/4 수렴. 실측이 Q1 자동 결정(OAuth broad→구현 정당 / 좁음→DEFER) |
| Q2 | (구현 시) API 키만 유의미 + **별도 계정 대안 추가**. OAuth 토큰=영향축소 0 | C-6·C-7 |
| Q3 | (구현 시) OAuth fallback 미보존(fail-closed) | 전원 |
| Q4 | sandbox 내 키 노출 *불가피*(밖=claude 도달 불가) + 헬퍼 변조 벡터 | A·BL-3 |
| Q5 | 매우 낮은 월 spend 한도부터 | codex |
| Q6 | 로테이션 없으면 단명 아님 — revoke/rotation runbook | 전원 |
| Q7 | ✅ apiKeyHelper 경유(ANTHROPIC_* 차단 유지) > env 예외 | 4/4 |
| Q8 | ✅ ADR-014 보강(신규 ADR 안 만듦) | 4/4, [[feedback_ceremony_inflation]] |

---

## 부록 — source agentId
A=`a9d92d8e41e448cac` · B=`a9eb43f048465f00a` · C=`a584f1cd9fd47b53d` · codex=cross-vendor(blind, `--output-last-message`).
