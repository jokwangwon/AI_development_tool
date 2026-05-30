# Runbook — claude code 워커 자격 오용 탐지 + 대응 (detection 보완재)

> **운영 절차(코드 변경 0).** 예방(prevention)이 DEFER 된 잔여 위험에 대한 *탐지→대응* 보완재. 레벨 3 net 격리·apiKeyHelper 영향 축소가 비례성으로 DEFER 된 후(ADR-014 §3, 106 entry), opt-in 단계에서 **가장 비례적인 보완 수단**(3+1 합의 권고).

**작성일**: 2026-05-30
**상위**: `docs/decisions/ADR-014-fake-home-worker-isolation.md` · `docs/review/3plus1-consensus-2026-05-30-jarvis-apikeyhelper-impact-reduction.md`
**근거**: [[feedback_proportionate_security_personal_tool]] · [[feedback_pass_scope_overclaim]] · [[reference_claude_landlock_isolation]]

---

## 1. 범위 — 무엇에 대한 runbook 인가

- **대상 잔여 위험**: `--real-workers` opt-in 으로 claude code 워커가 실행될 때, 가짜 홈(`~/.jarvis/claude-home`)에 복사된 **claude 자격이 exfil 되어 공격자가 오용**하는 경우.
- **현재 자격 = OAuth 구독 토큰**(실측: `subscriptionType=max`, scope=`user:inference` 외). apiKeyHelper(전용 API 키)는 DEFER. → 본 runbook 은 **OAuth 구독 토큰 기준**. (API 키 채택 시 §5 추가.)
- **이 runbook 이 아닌 것**: prevention 아님(레벨 3 DEFER). exfil 자체를 못 막음 — *오용을 빨리 알아채고 자격을 무효화*하는 reactive 절차.

### ⚠️ 정직 단서 ([[feedback_pass_scope_overclaim]])
- **탐지는 사후(reactive)** — exfil 시점이 아니라 *오용 시점*에 신호. 완전/즉시 탐지 보장 아님.
- **구독 OAuth 는 가시성이 거침** — API Console 의 per-key 사용량/spend 알림 같은 세밀한 대시보드가 *없을 수 있음*(아래 신호는 각자 계정에서 *존재 여부 확인* 필요).
- BL-1 실측상 토큰 blast 는 *bounded*(rate-limited Max 추론 + 경미 프로필, 계정/결제 관리 부재) — 즉 오용의 최악도 "내 구독 추론 한도 소진 + 프로필 노출" 수준. 과민 대응 불요(비례성).

---

## 2. 핵심 사실 — 무엇을 무효화해야 하나

- credential(`~/.claude/.credentials.json`)의 **access 토큰은 단명**(~수시간, 실측 만료 당일). **refresh 토큰이 장기 비밀** — access 를 계속 재발급.
- ⭐ **따라서 "대응 = 로컬 파일 삭제"로 부족**. 가짜 홈 복사본을 지워도 *이미 exfil 된 복사본*은 refresh 토큰으로 계속 유효. → **계정/세션 레벨 무효화**(아래 §4)가 진짜 대응.

---

## 3. 탐지 신호 (Tier 순 — 강→약)

### Tier A ⭐ — jarvis-local 기준선 (가장 신뢰, 비용 0)
- jarvis 는 워커 dispatch 를 **ledger**(`src/jarvis/ledger.py`)에 기록. claude code 워커는 **`--real-workers` 시에만** 실행.
- **신호**: "내가 `--real-workers` 를 돌린 시점/횟수"(ledger) **외**의 claude 활동 = 의심. 즉 ledger 가 *예상 사용 기준선*.
- **점검**: 계정 사용량(Tier B)을 ledger 의 실행 기록과 대조 — 불일치(내가 안 돌렸는데 추론 사용)가 최강 신호.

### Tier B — 계정 사용량 / rate-limit 이상 (확인 필요)
- **rate-limit 조기 도달**: 내 정상 사용보다 일찍 Max 한도에 걸림 = 누군가 토큰을 같이 쓰는 신호.
- **사용량 spike**: claude.ai 사용량 표시(있으면)에서 예상 외 급증.
- ⚠️ 구독 플랜의 사용량 가시성은 계정에서 *직접 확인* — API Console 수준의 세밀도 기대 금지.

### Tier C — 세션/디바이스 목록 (있으면)
- claude.ai 계정 설정에 **활성 세션/로그인 기기** 목록이 있으면 낯선 항목 점검. (기능 존재 여부 계정에서 확인.)

---

## 4. 대응 절차 (오용 의심 시)

1. **즉시 — 계정 세션 무효화(refresh 토큰 회전)**: claude.ai 에서 **전 기기 로그아웃** 또는 재로그인 → refresh 토큰 회전 → **exfil 된 복사본 무효화**. (이것이 핵심 — §2.) 필요 시 비밀번호 변경.
2. **로컬 가짜 홈 정리**: `rm -rf ~/.jarvis/claude-home` → 다음 `--real-workers` 시 재provision(현재 OAuth 재복사). *단 1 후에 해야* 새 토큰이 복사됨.
3. **진짜 홈 재인증**: `claude` 재로그인(또는 `/login`)으로 진짜 홈 자격 갱신.
4. **원인 점검**: ledger + 워커 실행 로그에서 의심 시점 전후 plan/subtask 확인(injection 흔적). jarvis 설계 버그 vs 외부 유출 구분.
5. **기록**: 본 사건을 세션 로그/메모리에 기록 → 실 trigger 면 레벨 3/apiKeyHelper *발효* 재검토(ADR-014 §3 trigger).

---

## 5. (DEFER 해제 시) API 키 채택 후 추가 절차

apiKeyHelper + 전용 API 키를 채택하면(ADR-014 trigger 발효 시) 탐지/대응이 개선됨:
- **Console per-key 사용량 + spend 알림** = Tier B 가 세밀해짐(키 단위).
- **대응 = Console 에서 해당 키 revoke + 신규 발급**(계정 전체 로그아웃 불요 — 키 단위 격리). 단 revoke 독립성은 *키 단위*이며 *계정 단위* 아님(같은 계정 사고 시 동반 위험 — BL-4).
- **spend 한도** = 오용 손실 *상한*(오용 방지 아님 — 공격자는 한도 전액 소진 가능).

---

## 6. 주기 점검 체크리스트 (경량 — 비례성)

- [ ] `--real-workers` 사용 후: 계정 사용량이 내 실행(ledger)과 대략 일치하는가?
- [ ] 월 1회 또는 의심 시: rate-limit 조기 도달·사용량 spike 없었나?
- [ ] (세션 목록 기능 있으면) 낯선 기기/세션 없나?
- [ ] 가짜 홈(`~/.jarvis/claude-home`) 권한 0700·credential 0600 유지되나?

> **과투자 주의**([[feedback_ceremony_inflation]])**: 자동 경보/모니터링 인프라는 현 opt-in bounded 사용엔 과잉. ledger 대조 + 위 수동 체크리스트로 충분. 자동화(ledger 기반 "예상 외 활동" 경보)는 실 사용 빈도가 높아질 때 후속.

---

## 부록 — 답습 교차
ADR-014(레벨 2 + net/apiKeyHelper DEFER resolution) / [[feedback_proportionate_security_personal_tool]](reactive 탐지 = 비례적 보완) / [[feedback_pass_scope_overclaim]](§1 정직 단서) / [[reference_claude_landlock_isolation]] / [[feedback_ceremony_inflation]](§6 과투자 주의).
