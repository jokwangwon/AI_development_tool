OpenAI Codex v0.128.0 (research preview)
--------
workdir: /home/delangi/문서/project/category/AI_development_tool
model: gpt-5.5
provider: openai
approval: never
sandbox: danger-full-access
reasoning effort: none
reasoning summaries: none
session id: 019e6d4a-9ab6-7e03-a508-011a183a29e1
--------
user
당신은 외부 LLM 검토자 (cross-vendor blind review)입니다. 응답 vendor = OpenAI (codex CLI), 풀 3+1 Agent vendor = Anthropic Claude. cross-vendor 충족 (헌법 5조-2).

## 본 cycle 개요

AI_development_tool 프로젝트. 본 cycle = **G2 GP-2 (송신/Egress redaction) Implementation Evidence PASS 발효 (e2)** (60 entry). MVP-2 = Layer 1+2+4 통합 PASS (59 발효 완료) + **GP-2 PASS (본 cycle)** + R-S1 hard gate. 본 cycle = GP-2 절반. 32 MVP-1 PASS / 59 Layer PASS 발효 답습 동형.

본 cycle 발효 효과: GP-2 송신 redaction PASS 발효.
본 cycle 발효 *하지 않는 것*: MVP-2 PASS 발효 0 / R-1 Hermes import 0 / R-2 facade real(TR-1) 0 / R-5 base64 evasion 진입 0 / R-S1 정정 0 / secret_scanner·workflow 본문 변경 0 / 자동 후속 0.

## 검토 대상 (working directory 자료, codex 직접 read 의무)

PRIMARY:
- `docs/phase0/mvp2-gp2-pass-activation-brief.md` (v1, 본 brief, §0~§10)

직접 입력 자료:
- `docs/phase0/mvp2-entry-eligibility-audit-brief.md` (51 audit §2 GP-2 Exit 5조건)
- `docs/phase0/mvp2-beta-submeans-decision-brief.md` (57 (β) R-4 = R-3 detection + R-1/R-2 prevention deferred)
- `docs/phase0/mvp2-layer-124-pass-activation-brief.md` (59 Layer PASS — means-vs-ends + DEFER + B-2 (a)~(d)/(e2) framing 답습)
- `docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass-activation.md` (59 Reviewer 통합)

선행 권위:
- `docs/decisions/ADR-011-means-vs-ends-redaction.md` (§2.1 (a)~(d) 모법 + §2.3 #2 Hermes redaction 송신 방어 신뢰)
- `docs/decisions/ADR-012-evidence-ledger-protection.md` (§4 (a)~(d)+(e) 확장)
- `docs/architecture/governance-preconditions.md` (§4 GP-2)
- `docs/architecture/redaction-pattern-equivalence.md` (R-4, (a)) + `docs/phase0/r4-1-trigger-extension-evidence.md` (R-4.1, (b))

실 evidence (filesystem + CI 직접 verify 의무 — brief evidence 매트릭스 검증):
- `.github/workflows/secret-hygiene-egress-redaction.yml` (D-2 scan-log redaction step, R-3)
- `tools/secret_scanner.py` (--mode scan-log)
- `tests/fixtures/secret_hygiene/redaction_pass/` + `redaction_fail/` (env_redacted + partial_redact + base64_evasion)
- `agent/redact.py` (R-1 본 repo 부재 확인) / `src/adapters/llm/facade.py` (R-2 placeholder)
- secret-hygiene 최근 actual run: `gh run view 26517803107 --json conclusion,headSha` (success / 4fec6485)

## 본 brief 핵심 주장 (검증 대상)

1. **GP-2 PASS 발효 권고 = APPROVE WITH CONDITIONS** (Exit (a)~(d) 4/4 충족: R-4 패턴 동등성 + secret-hygiene D-2 PoC + ADR 권위 + R-3 CI 회귀 green; (e2) = 본 cycle)
2. **51 audit "(d) gap" 부정확 정정** — secret-hygiene D-2 (scan-log redaction CI) 이미 운영 green → (d) ✅ (52 entry PoC 시제 발견 동형). **이 격상이 over-claim 아닌지 critical verify**
3. **R-3 detection (operative green) + R-1/R-2 prevention (deferred trajectory) 분리** (means-vs-ends, 59 Layer 2a DEFER 답습). 본 repo = DESIGN/governance, 실 runtime redaction = Hermes upstream (R-1)
4. **R-5 base64 evasion = known limitation** (Tier-1 42 평문 한정)
5. **(a)~(d) ADR-011 모법 + (e2) ADR-012 §4 확장** framing (59 B-2 정정 답습)

## 요청 사항

1. **verdict**: APPROVE / APPROVE WITH CONDITIONS / REVISE / REJECT 중 1
2. **BLOCKING findings** (근거 + 정정): evidence 매트릭스가 실제 repo/CI 상태와 일치? 특히 **(d) "secret-hygiene D-2 CI green" 격상이 정당한지** (run 26517803107 실재 + 코드 49 entry 이후 불변 verify) — 51 "(d) gap"→"✅" 격상이 over-claim 인가? R-3 detection 만으로 GP-2 PASS 가 means-vs-ends (ADR-011 §2.1 (a) 동등 이상 보안 결과)를 충족하는가, 아니면 R-1/R-2 prevention 부재가 보안 hole 인가? DESIGN repo GP-2 PASS vs runtime redaction 구분이 타당한가? 권위 인용 정확 (ADR-011 §2.1 = (a)~(d), §2.3 #2 송신 방어)? scope 침입 (MVP-2 PASS / R-1 import / R-2 facade / R-5 evasion) 0?
3. **권고 (non-blocking)** / 4. **NOTE / 누락**

filesystem + CI direct verify 로 부정확/과장 발견 시 BLOCKING. 특히 "(d) ✅ 격상"과 "R-3 detection PASS (prevention deferred)" 의 보안 타당성을 비판적으로 평가. 한국어 응답.

codex
요청 범위에 맞춰 로컬 brief와 권위 문서, 실제 CI/workflow/scanner/fixture 상태를 직접 대조하겠습니다. 핵심은 `(d) CI green` 격상이 증거상 정당한지와, R-3 detection만으로 GP-2 PASS를 발효해도 되는지입니다.
exec
/bin/bash -lc "sed -n '1,240p' docs/phase0/mvp2-gp2-pass-activation-brief.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
# GP-2 송신 redaction Implementation Evidence PASS 발효 합의 entry brief (v1)

> **작성**: 2026-05-28 (60번째 entry 진입 cycle — 신규 세션 #2)
>
> **scope**: G2 GP-2 (Egress/송신 redaction) Implementation Evidence PASS **발효 (e2)** — MVP-2 의 GP-2 절반
>
> **본 cycle = 큰 cycle** (PASS *발효* milestone, 풀 3+1 + 외부 LLM 1+ 의무, 59 Layer 통합 PASS 발효 + 32 MVP-1 PASS 발효 답습 동형)
>
> **본 cycle 발효 자격** = (a)~(d) evidence + (e2) 풀 3+1 + 외부 LLM 1+ 합의 APPROVE + 사용자 명시
>
> **본 cycle 발효 효과** = **GP-2 송신 redaction PASS 발효**. MVP-2 Implementation Evidence PASS = Layer 통합 PASS (59 ✅) + GP-2 PASS (본 cycle) + R-S1 hard gate 후 별도 cycle
>
> **선행 답습**: 51 audit (GP-2 Exit 5조건, R-1~R-5 후보) + 57 ((β) R-4 = R-3 detection 우선 + R-1/R-2 prevention deferred) + 59 (Layer 통합 PASS 발효, means-vs-ends + DEFER 패턴 답습)

---

## §0 본 brief 의 범위

### §0.1 본 brief 가 *하는* 것

1. **GP-2 Exit 5조건 evidence 매트릭스** ((a)~(d) + (e2)) — 51 audit §2.2 현행화 (§2)
2. **R-3 detection (operative) + R-1/R-2 prevention (deferred trajectory) 분리** (57 (β) + 59 Layer 2a DEFER 패턴 답습) (§3)
3. **ADR-011 §2.1 (a)~(d) 모법 + (e2) ADR-012 §4 확장 매핑** (59 B-2 정정 framing 답습) (§4)
4. **R-5 base64 evasion = known limitation 명문** (R-5 영구 분리) (§4)
5. **합의 형태 = 풀 3+1 + 외부 LLM 1+ + 승격 트리거** (§5)
6. **GP-2 PASS 발효 권고 + 조건** (§6)
7. 금지 / 다음 단계 / cross-ref / 자기진단 (§7~§10)

### §0.2 본 brief 가 *하지 않는* 것

| # | 영역 | 위반 |
|---|------|----|
| 1 | GP-2 PASS *발효* 자체 (본 brief = 합의 입력, 발효 = 합의 APPROVE + 사용자 명시 후) | 0 |
| 2 | **MVP-2 Implementation Evidence PASS 발효** (Layer 통합 PASS + GP-2 PASS + R-S1 후 별도) | 0 |
| 3 | **R-1 Hermes import 결정** (prevention 구현 경로, 별도 cycle) | 0 |
| 4 | **R-2 facade real (TR-1)** (prevention 구현 경로, 별도 trajectory) | 0 |
| 5 | R-5 base64/URL-encoded/압축 evasion 영역 진입 (MVP-2/3 분리, G3-4) | 0 |
| 6 | 신규 외부 library 도입 / secret_scanner Tier-2/3 catalog 확장 | 0 |
| 7 | R-S1 cross-reference 정정 (MVP-2 PASS 전 hard gate, 별도 cycle) | 0 |
| 8 | Layer 통합 PASS 재선언 (59 답습 유지) / MVP-1 PASS 재선언 (32 답습) | 0 |
| 9 | ADR / 헌법 / roadmap / governance / ADR-008/011/012 본문 갱신 | 0 |
| 10 | secret_scanner.py / secret-hygiene-egress-redaction.yml 본문 변경 | 0 (PoC 시제 보존) |
| 11 | 자동 후속 cycle 진입 (MVP-2 PASS / R-S1) | 0 (사용자 명시 의무) |
| 12 | 본 brief 자체 영구화 / 권위 chain 등재 | 0 |

### §0.3 권위 답습 source

- **ADR-011 §2.1 (a)~(d) 4조건 모법** (line 52~61) — `docs/decisions/ADR-011-means-vs-ends-redaction.md`
- **ADR-011 §2.3 운영 함의 #2** (Hermes redaction = 로그/LLM 송신 방어 신뢰, 저장 경로 책임 0) — 동상 line 112
- **ADR-012 §4 (a)~(d) + (e) 5조건 답습 확장** (PASS 발효 (e2) 권위) — `docs/decisions/ADR-012-evidence-ledger-protection.md`
- **governance-preconditions.md §4** (GP-2 Egress Redaction Entry/Exit) — `docs/architecture/governance-preconditions.md`
- **redaction-pattern-equivalence.md** (R-4, (a) 충족) + **r4-1-trigger-extension-evidence.md** (R-4.1, (b) 충족)
- **51 audit §2** (GP-2 Exit 5조건) — `docs/phase0/mvp2-entry-eligibility-audit-brief.md`
- **57 (β) brief v1.1** (R-4 = R-3 detection + R-1/R-2 prevention deferred) — `docs/phase0/mvp2-beta-submeans-decision-brief.md`
- **59 Layer 통합 PASS 발효 brief v1.1 + 합의** (means-vs-ends + DEFER + B-2 framing 답습) — `docs/phase0/mvp2-layer-124-pass-activation-brief.md`
- **본 cycle audit (read-only, 2026-05-28)** — secret-hygiene CI + fixtures + secret_scanner filesystem direct

---

## §1 진입 컨텍스트

### §1.1 선행 chain

| 합의/구현 | 본 cycle 답습 |
|----------|-----------|
| 59 Layer 1+2+4 통합 PASS 발효 (`0f49eb9`, 4 source APPROVE WITH CONDITIONS) | MVP-2 = Layer 통합 PASS ✅ + **GP-2 PASS (본 cycle)** + R-S1. means-vs-ends + DEFER 패턴 + B-2 (a)~(d)/(e2) framing 답습 |
| 57 (β) R-4 결정 (`18e8ad1`) | GP-2 수단 = R-4 (R-3 detection 우선 + R-1/R-2 prevention deferred trajectory). R-5 영구 분리 |
| 51 audit §2 (`f7ac61d`) | GP-2 Exit 5조건 — 본 cycle 현행화 (51 audit "(d) gap" = 부정확, secret-hygiene D-2 이미 운영) |

### §1.2 GP-2 = 송신 redaction 영역 정의 (governance §4)

- Hermes / Worker Agent 가 stdout/stderr/log file/LLM API request body 에 secret 노출 차단 (송신/로그 경로 한정).
- ADR-011 §2.3 #2: "Hermes 자체 redaction은 로그/LLM 송신 방어로만 신뢰, 저장 경로 차단 책임 0" (DB INSERT = GP-1 책임).
- 본 repo = DESIGN/governance repo (docs + tools + CI). 실 runtime redaction = Hermes upstream (R-1). 본 repo GP-2 PASS = redaction 패턴 정의 (R-4) + CI 회귀 검출 (R-3) + 설계 권위 (ADR-011 §2.3).

---

## §2 Evidence 매트릭스 (GP-2 Exit 5조건, 51 audit §2.2 현행화)

| # | 조건 | 상태 | evidence |
|---|------|------|---------|
| (a) | 동등 이상 보안 결과 | ✅ | `redaction-pattern-equivalence.md` (R-4 — Hermes Tier-1 42 catalog 패턴 동등성) — ADR-011 §2.1 (a) 충족 |
| (b) | 격리 환경 PoC 실증 | ✅ | secret-hygiene D-2 scan-log redaction PoC (`tests/fixtures/secret_hygiene/redaction_pass/env_redacted.txt` rc=0 잔존 0 + `redaction_fail/partial_redact.txt` rc=1 leak 검출) + `r4-1-trigger-extension-evidence.md` (R-4.1 Tier-1 42 + baseline 5 PoC) |
| (c) | ADR/SDD 권위 명시 | ✅ | ADR-011 §2.3 #2 (송신 방어 신뢰) + governance §4 (GP-2 정의) |
| (d) | 자동 회귀 검증 경로 | ✅ ⭐ | **`secret-hygiene-egress-redaction.yml` D-2 step (scan-log redaction residual, `secret_scanner.py --mode scan-log`) — 51 audit "❌ gap" 부정확 정정 (52 entry PoC 시제 발견 동형). actual run `26517803107` success (headSha `4fec6485`). ⚠️ secret-hygiene = `workflow_dispatch` 미지원 (schedule cron `0 3 * * *` 만) — 단 secret_scanner.py + workflow + redaction fixtures = 49 entry (`4fec6485`) 이후 **변경 0 (불변)** → 최근 green run = 현 코드 유효 evidence** |
| **(e2)** | **PASS 발효 합의 APPROVE** | ⏳ | 본 cycle 풀 3+1 + 외부 LLM 1+ + 사용자 명시 |

→ **(a)~(d) 4/4 충족** (51 audit 2.5/5 → 본 cycle 4/4, R-3 secret-hygiene D-2 CI operative green). (e2) = 본 cycle.

---

## §3 R-3 detection (operative) + R-1/R-2 prevention (deferred) 분리 (57 (β) + 59 Layer 2a 답습)

### §3.1 수단별 상태 (R-4 defense-in-depth)

| 수단 | 역할 | 본 repo 상태 | PASS 영향 |
|------|----|-----------|---------|
| **R-3** log canary CI (`secret-hygiene-egress-redaction.yml` + `secret_scanner.py --mode scan-log`) | **detection (회귀 검증)** | ✅ operative green | GP-2 (d) 자동 회귀 충족 — in-repo operative means |
| **R-1** Hermes native redaction (`agent/redact.py`) | **prevention (능동 redaction)** | ❌ 본 repo 부재 (Hermes upstream v0.12.0) | runtime prevention = Hermes upstream operative (import 결정 별도 cycle). ADR-011 §2.3 #2 송신 방어 신뢰 |
| **R-2** facade RedactionFilter | prevention (LLM API 진입점) | ⚠️ facade placeholder | facade real (TR-1) 시점 추가 layer (deferred trajectory) |
| **R-5** base64/URL/압축 evasion | (out of scope) | ❌ known limitation (`base64_evasion.txt` fixture) | 영구 분리 (MVP-2/3, G3-4) |

### §3.2 means-vs-ends 정합 (59 Layer 2a DEFER 답습)

- **ends** = secret 송신/로그 leak 0.
- **detection ends** = R-3 (secret-hygiene D-2 CI) ✅ operative green — 송신/로그에 secret 잔존 시 BLOCK (회귀 검증).
- **prevention ends** = R-1 (Hermes upstream native redaction, 실 runtime operative — 본 repo 는 DESIGN repo 이므로 import 미결정이나 Hermes runtime 자체는 redaction 수행) + R-2 (facade real deferred).
- **본 repo (DESIGN/governance) GP-2 PASS** = R-4 패턴 정의 (a) + R-3 CI 회귀 검출 (b)(d) + ADR 권위 (c). prevention 능동 redaction 의 실 구현 = Hermes upstream (R-1) + facade real (R-2) = 별도 trajectory (59 Layer 2a "operative 보호 = 다른 layer, 본 layer DEFER" 패턴 동형).

→ **GP-2 PASS = detection (R-3 operative) + 설계 권위 + 패턴 동등성. prevention 능동 redaction 구현 경로 (R-1 Hermes import / R-2 facade real) = cross-trajectory deferred** (57 (β) 결정 답습, 59 DEFER 패턴).

---

## §4 ADR-011 §2.1 (a)~(d) 모법 + (e2) ADR-012 §4 확장 (59 B-2 framing 답습)

> ⚠️ 59 B-2 답습: ADR-011 §2.1 = (a)~(d) 4조건 모법, "(e) 합의 APPROVE" = ADR-012 §4 "(a)~(d)+(e) 5조건 답습" 확장.

| 조건 | 출처 | GP-2 충족 |
|------|------|---------|
| (a) 동등 이상 보안 결과 | ADR-011 §2.1 | ✅ R-4 패턴 동등성 |
| (b) 격리 PoC | ADR-011 §2.1 | ✅ secret-hygiene D-2 + r4-1 PoC |
| (c) ADR/SDD 권위 | ADR-011 §2.1 | ✅ ADR-011 §2.3 #2 + governance §4 |
| (d) 자동 회귀 검증 | ADR-011 §2.1 | ✅ secret-hygiene D-2 CI green |
| (e2) 합의 APPROVE | ADR-012 §4 확장 | ⏳ 본 cycle |

### §4.1 R-5 base64 evasion = known limitation (영구 분리)

`tests/fixtures/secret_hygiene/redaction_fail/base64_evasion.txt` 존재 — secret-hygiene D-2 가 base64 evasion 미검출 (known limitation 명문, workflow line 13). R-5 = MVP-2/3 분리 (G3-4), GP-2 PASS scope 외. GP-2 PASS = Tier-1 42 catalog 평문 redaction 한정 (base64 evasion 제외 명문).

---

## §5 합의 형태 + 풀 3+1 승격 트리거

### §5.1 합의 형태 = 풀 3+1 + 외부 LLM 1+ (의무)

**정당화**: PASS *발효* milestone (59 Layer PASS + 32 MVP-1 PASS 답습) + 큰 결정 (ADR-011 §2.4 T3) + 헌법 5조-2 cross-vendor + MVP-2 PASS 직전 단계.

### §5.2 7 승격 트리거

| # | trigger | 발화 | 근거 |
|---|---------|----|------|
| 1 | 큰 결정 (PASS 발효 milestone) | ✅ | GP-2 PASS 발효 = MVP-2 PASS 절반 |
| 2 | 아키텍처/SDD/보안 본문 변경 | ❌ | brief = phase0 신규 1 |
| 3 | ADR 본문 변경 | ❌ | 0 |
| 4 | 권위 chain 다중 source 손상 | ⚠️ 부분 | R-S1 (MVP-2 PASS 전 hard gate, 본 cycle 비차단) |
| 5 | 외부 LLM 통합 필요 | ✅ | cross-vendor 의무 |
| 6 | Tier-2/3 catalog 확장 | ❌ | 0 |
| 7 | Hermes PMO 격상 | ❌ | 0 |

→ **2/7 발화 + 1 부분 → 풀 3+1 + 외부 LLM 1+ 적격**.

---

## §6 GP-2 PASS 발효 권고 + 조건

⭐ **권고 = GP-2 송신 redaction PASS 발효 APPROVE WITH CONDITIONS**:

1. **(a)~(d) 4/4 충족** — R-4 패턴 동등성 + secret-hygiene D-2 PoC + ADR 권위 + R-3 CI 회귀 green. (e2) = 본 cycle.
2. **조건**:
   - (C-1) **R-1 (Hermes import) / R-2 (facade real) = prevention deferred trajectory 명문** (GP-2 PASS = detection operative + 설계 권위 기반, 능동 redaction 구현 = 별도 cycle, 59 Layer 2a DEFER 답습)
   - (C-2) **R-5 base64 evasion = known limitation 명문** (Tier-1 42 평문 한정)
   - (C-3) secret-hygiene D-2 actual run = `26517803107` green (`4fec6485`) + 코드 불변 (49 entry 이후 변경 0) = 유효 evidence. workflow_dispatch 미지원이므로 fresh run 은 schedule (cron) 또는 path 변경 시 (GP-2 PASS 비차단)
3. **R-S1 = GP-2 PASS 비차단** (MVP-2 PASS 전 hard gate, 별도 cycle).

→ **GP-2 PASS 발효 자격 = (a)~(d) 충족 + (e2) 합의 APPROVE + 사용자 명시 + (C-1) prevention deferred 명문**.

---

## §7 금지 사항

§0.2 답습 (12). 추가: MVP-2 PASS 자동 선언 0 / R-1 Hermes import 결정 0 / R-2 facade real 0 / R-5 evasion 진입 0 / R-S1 자동 정정 0 / 자동 후속 0.

---

## §8 다음 단계 (사용자 명시 의무 — 자동 진입 0)

1. 본 brief 승인 → 풀 3+1 + 외부 LLM 1+ (codex (E-α)) → Reviewer 통합 → v1.1 흡수 → commit + push → **GP-2 PASS 발효**
2. **MVP-2 Implementation Evidence PASS 발효 합의** (Layer 통합 PASS ✅ + GP-2 PASS ✅ + R-S1 hard gate 후, 32 답습) — MVP-2 최종 milestone
3. R-S1 cross-reference 정정 cycle (MVP-2 PASS 전 hard gate 3 옵션)
4. (선택) R-1 Hermes import / R-2 facade real (TR-1) prevention trajectory

---

## §9 cross-reference 답습

- ADR-011 §2.1 (a)~(d) 모법 + §2.3 #2 (송신 방어 신뢰) — `docs/decisions/ADR-011-means-vs-ends-redaction.md`
- ADR-012 §4 (e 확장) — `docs/decisions/ADR-012-evidence-ledger-protection.md`
- governance-preconditions.md §4 (GP-2)
- redaction-pattern-equivalence.md (R-4) + r4-1-trigger-extension-evidence.md (R-4.1) + g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md (Group D PoC)
- 51 audit §2 + 57 (β) brief v1.1 + 59 Layer PASS brief v1.1 + 합의
- 실 evidence: `secret-hygiene-egress-redaction.yml` (D-2) + `tools/secret_scanner.py` (--mode scan-log) + `tests/fixtures/secret_hygiene/{redaction_pass,redaction_fail}/`

---

## §10 자기진단 (메타 편향 회피)

| # | 위험 | 처리 |
|---|------|----|
| P-1 | GP-2 PASS *기정사실화* | 발효 = 합의 APPROVE + 사용자 명시 후 (§0.2 #1 + §8) |
| P-2 | R-3 detection 만으로 GP-2 PASS *단순화* (prevention R-1/R-2 부재 은폐) | §3 detection/prevention 분리 명시 + (C-1) deferred 명문 (59 Layer 2a DEFER 답습, β B-1 cascade 교훈) |
| P-3 | 51 audit "(d) gap" → 본 brief "(d) ✅" 격상 over-claim risk | §2 (d) = secret-hygiene D-2 CI green actual run 근거 (filesystem + run direct verify), 52 entry PoC 시제 발견 동형 (gap 표기 부정확 정정) |
| P-4 | DESIGN repo GP-2 PASS vs runtime redaction 혼동 | §1.2 + §3.2 = 본 repo = 설계/CI, 실 runtime redaction = Hermes upstream (R-1) 명시 |
| P-5 | R-5 base64 known limitation 과소 | §4.1 명문 (base64_evasion.txt fixture + workflow line 13) |
| P-6 | 본 brief 작성자 = 57/59 작성자 (Claude) cascade | cross-vendor codex + 풀 3+1 독립 검증 (59 동형 — over-claim 0 입증) |
| P-7 | 권위 인용 (ADR-011 §2.1 (a)~(e)) 전도 (59 B-2 재발) | §4 = "(a)~(d) ADR-011 모법 + (e2) ADR-012 §4 확장" framing 답습 |

---

**본 brief v1 끝.**

**다음 단계**: 사용자 승인 → 풀 3+1 + 외부 LLM 1+ ((E-α) 권고) → Reviewer 통합 → v1.1 흡수 → commit + push → GP-2 송신 redaction PASS 발효.

exec
/bin/bash -lc "sed -n '1,220p' docs/phase0/mvp2-entry-eligibility-audit-brief.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
# MVP-2 진입 자격 audit brief (v1)

> **작성**: 2026-05-28 (51번째 entry 진입 cycle)
>
> **scope**: G2 GP-2 송신 redaction + G4 §4.4 Layer 4 (CI 회귀 검증) 진입 자격 audit
>
> **본 brief = audit 한정** (23 entry `mvp1-gp3-gp5-current-state-audit-brief.md` 답습 — 작은 cycle)
>
> **본 cycle 발효 = brief commit + 합의 commit + SESSION/INDEX commit 한정** (수단 결정 0, MVP-2 진입 발효 0, ADR/헌법/roadmap 본문 변경 0)

---

## §0 본 brief 의 scope

### §0.1 본 brief 가 *하는* 것

1. MVP-1 PASS 답습 상태 + MVP-2 영역 정의 확정 (50 entry carry-over §4 답습)
2. G2 GP-2 (송신 redaction) 진입 자격 audit (Entry 충족 자격 + Exit 5조건 매핑 권고)
3. G4 §4.4 Layer 4 (CI 회귀 검증) 진입 자격 audit (Entry 충족 자격 + Exit 5조건 매핑 권고)
4. 두 영역 통합 R-6 workflow 확장 권고 (단일 workflow 통합 vs 분리 대안)
5. sub-수단 후보 식별 (수단 *결정* 아님 — 별도 합의 영역)
6. Rollback Trigger 후보 + Evidence 요건 + 합의 형태 권고
7. 금지 사항 명시 + 다음 단계 (단계별 cycle 답습)

### §0.2 본 brief 가 *하지 않는* 것 (사용자 명시 답습)

- ❌ 수단 결정 (R-1~R-5 / L-1~L-5 中 채택 결정 = 별도 cycle)
- ❌ threshold 고정 (catalog 규모 / monotonicity tolerance 등)
- ❌ MVP-2 진입 발효 (본 brief = audit, MVP-2 진입 = 별도 cycle)
- ❌ ADR 본문 갱신 (ADR-011 / 012 / 008 / 009 / 010 본문 변경 0)
- ❌ 헌법 본문 갱신 (T3 영역, ADR Amendment 절차 별도)
- ❌ roadmap-mvp1 본문 갱신 (MVP-1 영역 답습 유지)
- ❌ governance-preconditions.md §4 본문 갱신 (GP-2 정의 답습)
- ❌ provider-agnostic-memory-skill-design.md §4.4 본문 갱신 (Layer 정의 답습)
- ❌ ADR-012 본문 갱신 (Layer 1~5 권위 답습)
- ❌ 실 코드 변경 (`tools/` / `src/` / `.github/workflows/` / `.pre-commit-config.yaml` / `agent/redact.py` / `adapters/llm/facade.py`)
- ❌ MVP-1 Implementation Evidence PASS 재선언 (32 entry 답습 유지)
- ❌ Operational Readiness PASS 발효
- ❌ Hermes PMO 격상
- ❌ adapters/llm/facade.py placeholder → real (별도 (d) carry-over)
- ❌ Tier-2/3 catalog 확장 (별도 합의 영역)

### §0.3 권위 답습 source

- **ADR-011 §2.1 (a)~(e) 5조건** (수단/목적 분리, 모법) — `docs/decisions/ADR-011-means-vs-ends-redaction.md`
- **governance-preconditions.md §4** (GP-2 Egress Redaction) — `docs/architecture/governance-preconditions.md`
- **provider-agnostic-memory-skill-design.md §4.4** (Layer 1~5 다층 강제) — `docs/architecture/provider-agnostic-memory-skill-design.md`
- **ADR-012 §2.3 + §2.5 + §2.7** (Append-only + Hash Chain + RFC 8785 JCS + prev_hash 실패 처리) — `docs/decisions/ADR-012-evidence-ledger-protection.md`
- **implementation-runtime-roadmap-mvp1.md §1.2 + §1.3** (3-layer PASS + GP-2 = MVP-2 분리 사유) — `docs/architecture/implementation-runtime-roadmap-mvp1.md`
- **implementation-runtime-roadmap.md §3 + §4 + §6** (G2 + G4 영역 + 9 그룹) — `docs/architecture/implementation-runtime-roadmap.md`
- **32 entry MVP-1 Implementation Evidence PASS 발효 합의** — `docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md`
- **50 entry carry-over §4** (다음 세션 진입 후보) — `docs/sessions/SESSION_2026-05-27.md`

---

## §1 MVP-1 PASS 답습 + MVP-2 영역 정의

### §1.1 MVP-1 답습 상태 (2026-05-27 32 entry 답습)

⭐⭐⭐ **MVP-1 Implementation Evidence PASS *완전 발효 (α)*** — GP-3 5/5 + GP-5 5/5 양쪽 충족 + 사용자 명시 결정 + 풀 3+1 + 외부 LLM 1+ APPROVE WITH CONDITIONS.

- 4 sub-cycle 완료: PC-1-T3 (`3a63a5b`) + S-3 (`4451716`) + ST-2 (`1edc5bb`) + AR-3 (`7f57323`/`7c294bb`/`73ed20d`/`9837298`)
- 31 entry 첫 PR (head SHA `9837298befdeda6c7e170879cc9f15e331c52bce`) 11/11 SUCCESS + mergeable CLEAN
- 32 entry 합의: `docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md` (BLOCKING 6 + 권고 5 1pass 흡수)
- PR #2 MERGED → main `eb51284` 영구 통합 (31 commits / 21,095 줄, 44 entry)
- 후속 정리 entry chain (40~50): D-6 workflow 4 entry full cycle + Actions Node.js 24 마이그레이션 + secret-scanner 정밀화

### §1.2 본 brief 시점 상태

- **HEAD**: `3517453` (50 entry 정리 commit, branch `feature/jarvis-mvp0`)
- **branch**: feature/jarvis-mvp0 (clean), main `eb51284` 답습
- **세션**: 2026-05-28 (51 entry 진입 cycle, 본 brief = 51 entry 첫 산출)

### §1.3 MVP-2 영역 정의 (50 entry carry-over §4 답습)

50 entry carry-over §4: "MVP-2 진입 자격 검토 (G2 GP-2 송신 redaction + G4 §4.4 Layer 4)".

**G2 GP-2 송신 redaction** (governance-preconditions §4):
- Hermes / Worker Agent 가 stdout / stderr / log file / LLM API request body 에 secret 노출 차단
- ADR-011 §2.3 운영 함의 #2 의 *보조* 역할 (DB INSERT 차단 = GP-1 책임, GP-2 = 송신/로그 경로 한정)

**G4 §4.4 Layer 4 — CI 회귀 검증** (provider-agnostic-memory-skill-design §4.4.1):
- Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증
- canonical JSON 위반 검출
- timestamp monotonicity 검증 (ADR-012 §3.4)
- R-6 workflow (`.github/workflows/r2-canary.yml`) 답습 확장 (별도 PR — Implementation 영역)
- MANDATORY 등급 (Layer 5 中 4번째, Layer 1 + 2 + 4 MANDATORY, Layer 3 + 5 RECOMMENDED MVP)

### §1.4 두 영역 공통 통합 영역 (핵심 발견)

⭐ **두 영역 모두 R-6 workflow (`.github/workflows/r2-canary.yml`) 답습 확장 영역**:

- **GP-2 §4.6 산출 후보**: R-6 workflow 확장 — log file canary inject step
- **G4 §4.4 Layer 4**: R-6 workflow 답습 확장 (Layer 1+2 자동 회귀 + canonical JSON 위반 + timestamp monotonicity)

→ **단일 R-6 workflow 확장으로 두 영역 동시 진행 가능** (§4 권고 답습).

### §1.5 MVP-2 영역 분리 사유 답습 (roadmap-mvp1.md §1.3)

GP-2 = MVP-2 로 분리한 사유 (32 entry 답습 전 결정):

1. **R-4 / R-4.1 답습 책임 분담** — GP-2 의 송신 redaction = R-4.1 Tier-1 42 catalog 의 *런타임 적용* 영역. Group D PoC = *형식적 검출 layer 한정*. 실 송신 redaction = Hermes upstream 영역 (Group D PoC §1.2 #6 답습) + P1 facade RedactionFilter 본문 (Group D PoC §1.2 마지막 항목 답습).
2. **MVP-1 부담 경감** — GP-3 + GP-5 만으로도 의사결정 부담 충분. GP-2 추가 시 4 영역 동시 진입 — 1인 개발자 환경에서 운영 부담 ↑.
3. **외부 LLM line 242 vs C-7 line 378 충돌 해소 = C-7 답습** — GP-2 = **MVP-2** 의 Implementation Evidence PASS 영역 *우선순위 1* (C-7 line 379 답습) — 본 분리 = *시점* 분리이지 *영구 제외* 아님.

---

## §2 G2 GP-2 진입 자격 audit

### §2.1 Entry 기준 충족 자격 (governance-preconditions.md §4.4)

| # | 조건 | 현 상태 (2026-05-28) | 충족 자격 |
|---|------|---------------------|---------|
| 1 | R-4 pattern equivalence 작성 완료 | ✅ `docs/architecture/redaction-pattern-equivalence.md` (ADR-011 §2.1 (a) 충족, 2026-05-06) | 충족 |
| 2 | Hermes native redaction `agent/redact.py` 존재 확인 | ✅ R-1 Day 2 evidence | 충족 |
| 3 | 사용자 명시 GP-2 작업 진입 결정 | ⏳ 본 brief = 진입 *자격* 평가, 진입 *결정* = 별도 cycle | 사용자 영역 |

→ **현 시점 Entry 충족 = 2/3 충족 + 1 사용자 영역** (Entry 자체는 기술적 gap 0).

### §2.2 Exit 기준 5조건 매핑 권고 (ADR-011 §2.1 (a)~(e) + governance-preconditions §4.5 답습)

| # | 조건 | GP-2 영역 현 상태 | 충족 경로 권고 (수단 결정 0) |
|---|------|----------------|----------------------|
| (a) | 동등 이상 보안 결과 | ✅ R-4 답습 (충족) — `redaction-pattern-equivalence.md` | Hermes native redaction Tier-1 42 catalog 적용 검증 evidence + P1 facade RedactionFilter 검증 evidence (둘 다 *실행* 시점 evidence 추가 수집) |
| (b) | 격리 환경 PoC 실증 | ⚠️ Group D PoC 부분 (`g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md` — 형식적 검출 layer 한정, 송신 redaction 영역 미커버) | log file canary inject + grep 검증 PoC (Docker 격리) 추가 — *송신 redaction* 영역 확장 |
| (c) | ADR / SDD 권위 명시 | ✅ ADR-011 §2.3 + 본 §4 권위 (충족) | ADR-008 차단조건 #1 보조 메커니즘 cross-reference 추가 (본문 변경 0, cross-reference 한정) |
| (d) | 자동 회귀 검증 경로 확보 | ❌ gap | **R-6 workflow 에 log file canary inject step 추가 — §4 통합 권고 (G4 §4.4 Layer 4 와 단일 workflow 확장)** |
| (e) | 합의 APPROVE | ❌ gap | 단축 또는 풀 3+1 합의 (G2 GP-2 한정 또는 G2 통합) — §7 합의 형태 권고 답습 |

→ **현 시점 5조건 충족 자격 = 2.5/5** ((a) + (c) 충족 / (b) 부분 / (d) + (e) gap).

### §2.3 sub-수단 후보 식별 (수단 결정 0, 후보 비교만)

| # | 수단 | 영역 | base64 evasion 처리 | 호환성 | 비고 |
|---|------|----|------------------|------|----|
| **R-1** | Hermes native redaction (`agent/redact.py`) | 송신 직전 redaction | known limitation (G3-4 영역, MVP-2/3 분리 답습) | Tier-1 42 catalog 답습 | MANDATORY (ADR-011 §2.3 #2) |
| **R-2** | P1 facade RedactionFilter | LLM API 진입점 redaction | 별도 layer | P1 v2 §8.2 답습 | MANDATORY (facade single entry point) |
| **R-3** | log file canary inject + grep CI step | CI 회귀 검증 | 별도 layer | R-6 workflow 답습 확장 | MANDATORY ((d) 충족 경로) |
| **R-4** | R-1 + R-2 + R-3 병행 (defense-in-depth) | 다층 redaction | 보조 | 양쪽 활용 | **본 brief 권고 — 5/5 입력 패턴 답습** |
| **R-5** | base64 / URL-encoded / 압축 evasion 별도 영역 | Hermes upstream R2-6 또는 P1 facade RedactionFilter 확장 | MVP-2/3 분리 영역 (G3-4 답습) | 본 cycle 범위 외 | 분리 영역 명시 |

→ **수단 *결정* = 별도 합의 영역** (MVP-2 entry 합의 시점). 본 brief 권고: **R-4 (R-1 + R-2 + R-3 병행)** = MVP-2 진입 시점 채택.

---

## §3 G4 §4.4 Layer 4 진입 자격 audit

### §3.1 영역 정의 답습 (G4 §4.4.1 + ADR-012 §2.3)

**Layer 4 — CI 회귀 검증 (MANDATORY)**:
- Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증
- canonical JSON 위반 검출 (RFC 8785 JCS Primary + fallback 동등성)
- timestamp monotonicity 검증 (ADR-012 §3.4 답습)
- R-6 workflow (`.github/workflows/r2-canary.yml`) 답습 확장 (별도 PR — Implementation 영역)

**참고**: 본 audit = Layer 4 영역 한정. Layer 1 / Layer 2 / Layer 3 / Layer 5 = 본 brief 직접 scope 외 (단, Layer 4 검증 대상 = Layer 1 + Layer 2 이므로 *의존 영역* 으로 명시).

### §3.2 Entry 자격 (현 상태)

| # | 조건 | 현 상태 (2026-05-28) | 충족 자격 |
|---|------|---------------------|---------|
| 1 | Design/Governance Gate PASS 답습 | ✅ G4 = PASS Bundled (2026-05-07 + 2026-05-09 후속) | 충족 |
| 2 | ADR-012 §2.3 Layer 1~5 권위 정의 발효 | ✅ 2026-05-09 PR-2 풀 3+1 + 외부 LLM 2건 APPROVE WITH CONDITIONS | 충족 |
| 3 | G4 §4.4 본문 P-1 (RFC 8785 JCS) 흡수 완료 | ✅ 2026-05-11 흡수 완료 | 충족 |
| 4 | Layer 1 (hash chain) 실 구현 (`tools/jsonl_chain_verify.py` 또는 동등) | ❌ gap (의존 영역) | 미충족 |
| 5 | canonical JSON test corpus (≥ 20개 RFC 8785 reference) | ❌ gap (`tests/canonical/` 미존재) | 미충족 |
| 6 | Layer 4 CI step 실 구현 (R-6 workflow 확장) | ❌ gap | 미충족 |
| 7 | ledger 첫 entry (genesis hash) 작성 | ❌ gap (의존 영역) | 미충족 |
| 8 | 사용자 명시 작업 진입 결정 | ⏳ 본 brief = 진입 *자격* 평가, 진입 *결정* = 별도 cycle | 사용자 영역 |

→ **현 시점 Entry 충족 자격 = 3/8 충족 + 1 사용자 영역** (Design Gate + Layer 정의 + JCS 채택만 충족, 4 의존 영역 + Layer 4 자체 구현 gap).

### §3.3 Exit 기준 5조건 매핑 권고 (ADR-011 §2.1 (a)~(e))

| # | 조건 | G4 §4.4 Layer 4 현 상태 | 충족 경로 권고 (수단 결정 0) |
|---|------|--------------------|----------------------|
| (a) | 동등 이상 보안 결과 | ❌ gap (실 구현 부재) | Layer 1+2+4 결합 보안 결과 vs 기존 (없음) 비교표 — middle entry tampering / canonical 위반 / timestamp 위반 차단 |
| (b) | 격리 환경 PoC 실증 | ❌ gap | Docker 격리 PoC 3종 — middle entry tampering 차단 + canonical JSON 위반 차단 + timestamp monotonicity 위반 차단 |
| (c) | ADR / SDD 권위 명시 | ✅ ADR-012 §2.3 + G4 §4.4 (충족) | (충족 — 추가 작업 0, cross-reference 만 보강) |
| (d) | 자동 회귀 검증 경로 확보 | ❌ gap | **R-6 workflow 답습 확장 step 추가 — §4 통합 권고 (GP-2 와 단일 workflow)** |
| (e) | 합의 APPROVE | ❌ gap | **풀 3+1 합의 권고** (G4 §4.4 Layer 1+2+4 통합 + Layer 5 권고 영역 추가 의사결정) |

→ **현 시점 5조건 충족 자격 = 1/5** ((c) 만 충족, (a)/(b)/(d)/(e) 모두 gap).

### §3.4 sub-수단 후보 식별 (수단 결정 0, 후보 비교만)

| # | 수단 | 영역 | Library | 비고 |
|---|------|----|---------|----|
| **L-1** | Layer 1 (hash chain) Python stdlib 단독 (`hashlib.sha256` + `json.dumps(sort_keys=True, separators=(",",":"))`) | hash chain 검증 | stdlib | fallback canonical JSON, RFC 8785 동등성 test corpus 의무 |
| **L-2** | Layer 1 + RFC 8785 JCS Primary (`pyjcs` / `rfc8785` library) | hash chain + canonical | 외부 library 1+ (의존성 추가 trigger — R-2 / R-4.1 PoC 자동 재실행 의무 ADR-012 §2.1 답습) | Primary 채택, fallback 보조 |
| **L-3** | Layer 4 R-6 workflow step (canonical JSON 위반 + prev_hash mismatch + timestamp monotonicity) | CI 회귀 | shell + Python (stdlib) | R-6 답습 확장 |
| **L-4** | L-1 + L-3 병행 (MVP 권고) | Layer 1+4 동시 | stdlib 단독 | **본 brief 권고 — MVP 단계 답습 (5/5 입력 권고 답습)** |
| **L-5** | L-2 + L-3 병행 (정식 권고) | Layer 1+4 + JCS Primary | 외부 library 1+ | 정식 채택 시점 (Operational Readiness 영역 또는 별도 cycle) |

→ **수단 *결정* = 별도 합의 영역** (MVP-2 entry 합의 시점). 본 brief 권고: **L-4 (L-1 + L-3 병행)** = MVP-2 진입 시점 채택, L-5 = 별도 cycle (외부 library 의존성 추가 = ADR-012 §2.1 답습 R-2 / R-4.1 PoC 자동 재실행 trigger).

---

## §4 두 영역 통합 R-6 workflow 확장 권고

### §4.1 통합 가능성 분석

| 영역 | 산출 후보 | R-6 workflow 답습 확장 |
|----|----------|-----------------------|
| GP-2 §4.6 | log file canary inject + grep CI step | ✅ R-6 답습 확장 (governance-preconditions §4.6 line 460 답습) |
| G4 §4.4 Layer 4 | Layer 1 + Layer 2 자동 회귀 + canonical 위반 + timestamp monotonicity CI step | ✅ R-6 답습 확장 (provider-agnostic-memory-skill-design §4.4.1 line 653 답습) |

→ **두 영역 모두 동일 R-6 workflow (`.github/workflows/r2-canary.yml`) 확장 대상**.

### §4.2 통합 vs 분리 대안 비교

| 대안 | 장점 | 단점 | 권고 |
|----|----|----|----|
| **W-A: 단일 R-6 확장 (GP-2 + G4 §4.4 Layer 4 통합)** | ceremony-inflation 차단 / CI 자원 효율 / evidence 통합 / R-6 답습 한 PR | step 수 증가 / 실패 영역 식별 복잡도 ↑ (step name 분리로 완화 가능) | **✅ 본 brief 권고** |
| W-B: 별도 workflow 2개 분리 (`secret-egress-redaction.yml` 신설 + `ledger-chain-verify.yml` 신설) | 영역 분리 명확 / 실패 영역 식별 즉시 | ceremony-inflation 위험 / R-6 답습 미답습 / branch protection contexts 추가 부담 (43 entry 8 contexts 답습) | ❌ 비권고 |

### §4.3 통합 시 R-6 workflow 확장 step 후보 (예시, 결정 0)

```yaml
# .github/workflows/r2-canary.yml (R-6 답습 확장, 본 brief = 예시 수준 결정 0)

exec
/bin/bash -lc "sed -n '1,220p' docs/phase0/mvp2-beta-submeans-decision-brief.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
# (β) sub-수단 결정 entry brief (v1.1)

> **작성**: 2026-05-28 (57번째 entry 진입 cycle — 신규 세션)
>
> **v1 → v1.1 갱신**: 풀 3+1 + 외부 LLM 1+ (codex gpt-5.5 cross-vendor) 통합 합의 (`docs/review/3plus1-consensus-2026-05-28-mvp2-beta.md`) **REVISE → BLOCKING 6 + 권고 7 1pass 흡수** (별도 v2 cycle 0, ceremony-inflation 차단). 핵심 정정: **B-1 L-1 stdlib 시제 충족 주장 = 거짓** (실 시제 rfc8785/jcs Primary, Q1 합의 2026-05-10 이미 채택) → L 결정 "기존 rfc8785/jcs PoC 보존, 신규 도입 0" / B-3 R-1 권위 전도 / B-5 W-F 라벨. §13 v1.1 흡수 매트릭스 추가.
>
> **scope**: MVP-2 영역 sub-수단 *결정* — R-1~R-5 (GP-2 송신 redaction) + L-1~L-5 (G4 §4.4 Layer 4 CI 회귀 검증) + W-A~E (workflow 통합 방식)
>
> **본 cycle = 큰 cycle** (실 구현 *직전* 마지막 합의, 풀 3+1 + 외부 LLM 1+ 권고, 수단별 차등)
>
> **본 cycle 발효 자격** = **풀 3+1 합의 + 외부 LLM 1+ 응답 입력 (cross-vendor) + 사용자 명시 결정**
>
> **본 cycle 발효 효과** = R / L / W sub-수단 *결정 발효* + 후속 실 구현 sub-cycle 진입 자격 (조건부 승인 조건 6 입력). 실 구현 (denyNonFastForwards 활성화 + R-6 actual run + evidence 수집) = 별도 sub-cycle (본 cycle = 수단 결정 한정)
>
> **선행 답습**: 51 audit brief (R/L 후보 식별) + 52 (α) entry brief v1.1 (W-A~E 5 대안 확장) + 53 (γ) Layer 분리 + 54 (γ-c) 채택 발효 + 55 Layer 1+2+4 통합 PASS 격상 진입 합의 (조건부 승인 조건 6)

---

## §0 본 brief 의 범위

### §0.1 본 brief 가 *하는* 것 (51 audit brief = "수단 결정 0" 과 *대비* — 본 cycle = 수단 *결정* cycle)

1. **R sub-수단 결정** (GP-2 송신 redaction) — R-1~R-5 中 채택 결정 권고 + 실 구현 매핑 (§2)
2. **L sub-수단 결정** (G4 §4.4 Layer 4 CI 회귀 검증) — L-1~L-5 中 채택 결정 권고 (§3)
3. **W 통합 방식 결정** (workflow 통합) — W-A~E 中 채택 결정 권고 (실 repo 현 상태 핵심 반영) (§4)
4. **통합 수단 결정 매트릭스 + 의존 관계** (R ↔ L ↔ W cross-dependency) (§5)
5. **합의 형태 = 풀 3+1 + 외부 LLM 1+ 정당화 + 승격 트리거 검증** (§6)
6. **수단 결정 발효 후 실 구현 sub-cycle 입력 (조건부 승인 조건 6 매핑 + Rollback Trigger / Evidence)** (§7)
7. 금지 사항 + 외부 LLM 응답 영역 + 다음 단계 + cross-reference + 자기진단 (§8~§12)

### §0.2 본 brief 가 *하지 않는* 것 (55 entry §0.3 답습 + 본 cycle 한계)

| # | 영역 | 위반 시점 |
|---|------|----------|
| 1 | 실 코드 / runtime code 구현 | 0건 (수단 *결정* ≠ 구현) |
| 2 | `tools/*.py` 본문 변경 (jsonl_hash_chain / canonical_json / secret_scanner 등) | 0건 (PoC 시제 답습 보존) |
| 3 | `.github/workflows/*.yml` 본문 변경 | 0건 (기존 workflow 보존) |
| 4 | `tests/canonical/` + `tests/fixtures/` 본문 변경 | 0건 (72 files 답습 보존) |
| 5 | **`git config receive.denyNonFastForwards true` 활성화 실행** | 0건 (실 구현 sub-cycle 영역) |
| 6 | R-6 workflow actual run 트리거 | 0건 (실 구현 sub-cycle) |
| 7 | ledger 첫 entry (genesis hash) 작성 | 0건 (실 구현 sub-cycle) |
| 8 | **신규 외부 library 도입 결정** (B-4 정정: rfc8785/jcs = Q1 합의 2026-05-10 *이미 채택*, 신규 도입 아님) | 0건 (신규 외부 JCS library 도입/운영 승격 = 별도 cycle. 의존성 변경 trigger 권위 = **ADR-011 §2.3 운영 함의 #4** "Hermes 의존성 업그레이드 → R-2/R-6 자동 재실행" — *ADR-012 §2.1 아님*, B-4 흡수) |
| 9 | **Hermes upstream `agent/redact.py` 본 repo 內 import 결정** (R-1 구현 경로) | 0건 (별도 cycle, 52 entry R-A-1 답습) |
| 10 | **`adapters/llm/facade.py` placeholder → real** (R-2 구현 경로, TR-1) | 0건 (별도 trajectory, (d) carry-over) |
| 11 | base64 / URL-encoded / 압축 evasion 영역 진입 (R-5) | 0건 (MVP-2/3 분리, G3-4 답습) |
| 12 | threshold 고정 (catalog 규모 / monotonicity tolerance 등) | 0건 |
| 13 | Tier-2 / Tier-3 vendor catalog 본문 확장 | 0건 |
| 14 | Layer 1+2+4 통합 PASS *발효* | 0건 (55 entry = 진입 권한, 발효 = 실 구현 + evidence + 합의 후 별도) |
| 15 | MVP-2 Implementation Evidence PASS 발효 | 0건 |
| 16 | MVP-1 PASS 재선언 | 0건 (32 entry 답습 유지) |
| 17 | Operational Readiness PASS / Hermes PMO 격상 | 0건 |
| 18 | ADR / 헌법 / roadmap / governance / G4 / ADR-012 본문 갱신 | 0건 |
| 19 | Layer 3 (Signed commit) + Layer 5 (External anchor) 영역 진입 결정 | 0건 ((γ-c) "부분 답습" framing 영구 답습) |
| 20 | (γ-a/b/d) + (γ-e/f/g) 대안 재평가 | 0건 (54 entry (γ-c) 채택 영구 발효) |
| 21 | R-S1 cross-reference 정정 (ADR-012 §2.3 vs §2.8) | 0건 (별도 cycle, RT-γ-6 평가 한정) |
| 22 | branch protection contexts 자동 추가 | 0건 (사용자 admin scope 영역) |
| 23 | 자동 후속 실 구현 sub-cycle 진입 | 0건 (사용자 명시 의무) |
| 24 | 본 brief 자체 영구화 / 권위 chain 등재 | 0건 |

### §0.3 권위 답습 source

- **ADR-011 §2.1 (a)~(d) 4조건 모법 + (e) 후속 운영조건** (수단/목적 분리) — `docs/decisions/ADR-011-means-vs-ends-redaction.md`
- **51 audit brief §2.3 (R-1~R-5) + §3.4 (L-1~L-5) + §4.2 (W-A/B)** — `docs/phase0/mvp2-entry-eligibility-audit-brief.md`
- **52 (α) entry brief v1.1 §2.3.2 (W-A~E 5 대안)** — `docs/phase0/mvp2-entry-brief.md`
- **55 Layer 1+2+4 통합 PASS 격상 brief v1.1 §2.4 + §4.4 + §11.1 B-4 (조건부 승인 조건 6)** — `docs/phase0/mvp2-layer-124-pass-entry-brief.md`
- **54 (γ-c) 채택 decision brief §1.3 (특화 의무 4)** — `docs/phase0/mvp2-gamma-decision-brief.md`
- **governance-preconditions.md §4** (GP-2) + **provider-agnostic-memory-skill-design.md §4.4** (Layer 1~5)
- **ADR-012 §2.3 + §2.5 + §2.7 + §2.8 + §3.4** — `docs/decisions/ADR-012-evidence-ledger-protection.md`
- **본 cycle audit (read-only, 2026-05-28 신규 세션)** — 실 repo PoC 시제 현 상태 직접 verify

---

## §1 진입 컨텍스트 + 실 repo PoC 시제 현 상태 (본 cycle audit)

### §1.1 선행 권위 chain 답습 (55 → 54 → 53 → 52 → 51)

| 합의 / 권위 | 본 cycle 답습 영역 |
|----------|-----------------|
| 55 Layer 1+2+4 통합 PASS 격상 진입 합의 (`311ca3b`, 4 source APPROVE WITH CONDITIONS) | Layer 1+2+4 PASS 격상 *진입 권한* 발효 답습 + 조건부 승인 조건 6 (실 구현 sub-cycle 입력) |
| 54 (γ-c) 채택 결정 발효 (`895a77b`) | (γ-c) 특화 의무 4 영구 답습 (Layer subsection 강제 + "부분 답습" framing + 통합 동시 + RT-γ-6) |
| 53 (γ) Layer 분리 4 대안 평가 (`f5cf584`) | (γ-c) 1순위 + (γ-d) 모순 CONFIRMED + R-S1 5 source verify |
| 52 (α) MVP-2 진입 합의 entry brief (`c739c53`) | MVP-2 영역 진입 권한 발효 + **W-A~E 5 대안 확장 (B-5/B-7 흡수)** + Agent A filesystem 발견 (agent/ 부재 + G4 workflow 분리 운영) |
| 51 진입 자격 audit brief (`f7ac61d`) | **R-1~R-5 + L-1~L-5 후보 식별** (수단 결정 0) — 본 cycle = 51 후보 → 결정 |

### §1.2 실 repo PoC 시제 현 상태 (2026-05-28 본 cycle audit, filesystem direct)

⭐ **본 cycle 핵심 발견 = GP-2 + G4 양 영역 PoC 시제 광범위 존재 (55 entry audit 답습 + GP-2 측 신규 확인)**:

| 영역 | PoC 시제 현 상태 | 수단 매핑 |
|------|----------------|---------|
| **GP-2 CI 회귀 검증** | ✅ `secret-hygiene-egress-redaction.yml` (51791B, D-2 scan-log redaction_pass/fail + base64 known limitation) + `tools/secret_scanner.py` (16802B, `--mode scan-log` redaction 잔존 검출, **registered 45 (Tier-1 42 catalog compliant + baseline 포함)**, N-1 정정) | **R-3 (log canary CI) 시제 충족** |
| GP-2 Hermes native | ❌ `agent/redact.py` 본 repo 부재 (Hermes upstream HEAD v0.12.0, 52 R-A-1 답습) | R-1 = upstream 영역 |
| GP-2 facade redaction | ⚠️ `src/adapters/llm/facade.py` = placeholder (TR-1 발화 시 real, (d) carry-over) | R-2 = 별도 trajectory |
| Layer 1 hash chain | ✅ `tools/jsonl_hash_chain.py` (14038B, genesis + **3 violation_type actual emission** PREV_HASH_MISMATCH + HASH_RECALCULATION + GENESIS_MISMATCH + **HISTORY_REWRITE = enum 정의만, emission 0**, B-2 정정) + `g4-hash-chain.yml` (10652B) | **rfc8785/jcs Primary 시제 충족** (B-1 정정 — stdlib 아님) |
| canonical JSON | ✅ `tools/canonical_json.py` (10055B, **rfc8785 + jcs = Primary, jq -S -c = corpus cross-check fallback**, runtime `jsonl_hash_chain.py:99` = `PRIMARY_1_ONLY` rfc8785 단독) + `requirements-dev.txt:20-21` rfc8785==0.1.4 + jcs==0.2.1 고정 + `tests/canonical/` 72 files / 8 카테고리 (24 input) | **외부 library Primary 시제 충족 (Q1 합의 2026-05-10 채택)** — B-1 정정 |
| Layer 2 history | ✅ `history-anchor-verifier.yml` (19094B) + `rewrite-defense.yml` (16454B) + tools | L-3 영역 시제 충족 |
| Layer 4 CI step | ✅ 4 G4 workflow 분리 운영 (g4-hash-chain + history-anchor-verifier + rewrite-defense + r2-canary), 실 repo 총 12 workflow | **L-3 (R-6 step) 시제 충족** |
| Layer 2a denyNonFastForwards | ⚠️ **미설정** (local + global 0건, 55 §1.3 답습) | 실 구현 sub-cycle 활성화 |

→ ⭐ **핵심 함의 (B-1 정정)**: R-3 (log canary CI) + Layer 1/4 (rfc8785/jcs Primary hash chain + R-6 step) = **모두 PoC 시제 *이미 충족***. 본 (β) cycle 의 수단 결정 = "신규 구현 수단 선택" 보다 **"기존 PoC 시제 → MANDATORY 채택 + PASS 격상 경로 확정"** 성격. ⚠️ **실 시제 = stdlib 단독 아님** — runtime 은 rfc8785 (`PRIMARY_1_ONLY`), 외부 library 는 Q1 합의 2026-05-10 (`3plus1-consensus-2026-05-10-g4-jcs-library-selection.md`) 로 *이미 채택*. 본 cycle = **신규 외부 library 도입 0 (기존 보존)**. R-1 (Hermes upstream) + R-2 (facade real) = 별도 trajectory 의존 (본 cycle = 결정 영역 명시, 구현 경로 결정 0).

### §1.3 (γ-c) 특화 의무 4 영구 답습 (54 entry §1.3, 본 cycle 적용)

| # | 의무 | 본 brief 답습 |
|---|------|-----------|
| 1 | PASS evidence template Layer 1/2/4 subsection 강제 | §5 통합 매트릭스 Layer 별 분리 + §7 evidence Layer subsection |
| 2 | "defense-in-depth 부분 답습" framing 영구 (Layer 3+5 = scope 외) | §0.2 #19 + §4 W 결정 시 Layer 3+5 진입 0 |
| 3 | Layer 1+2+4 통합 PASS evidence 동시 발효 | §5 통합 의존 + W 결정이 통합 동시 발효 저해 0 |
| 4 | RT-γ-6 R-S1 PASS 시점 선행/동시 정정 *평가* 의무 | §7 + §10 #5 답습 (정정 = 별도 cycle) |

---

## §2 R sub-수단 결정 (GP-2 송신 redaction)

### §2.1 후보 비교 (51 audit §2.3 답습 + 본 cycle audit 갱신)

| # | 수단 | 영역 | 본 repo 구현 상태 | 의존 | 등급 |
|---|------|----|----------------|----|----|
| **R-1** | Hermes native redaction (`agent/redact.py`) | 송신 직전 redaction | ❌ 본 repo 부재 (Hermes upstream v0.12.0) | Hermes import 결정 (별도 cycle) | GP-2 송신/로그 방어 **신뢰 수단** (ADR-011 §2.3 운영 함의 #2 — "로그/LLM 송신 방어로만 신뢰, 저장 경로 책임 0", B-3 정정 — "MANDATORY" 아님) — *결과* 보조 means, 구현 경로 = upstream |
| **R-2** | P1 facade RedactionFilter | LLM API 진입점 redaction | ⚠️ facade placeholder | facade real (TR-1, (d) carry-over) | facade single entry point redaction means — 구현 경로 = TR-1 trajectory |
| **R-3** | log canary inject + grep CI step | CI 회귀 검증 | ✅ **시제 충족** (`secret-hygiene-egress-redaction.yml` + `secret_scanner.py --mode scan-log`) | 없음 (즉시 PASS 격상 가능) | MANDATORY ((d) 자동 회귀 경로) |
| **R-4** | R-1 + R-2 + R-3 병행 (defense-in-depth) | 다층 redaction | 부분 (R-3 충족, R-1/R-2 trajectory) | R-1 + R-2 의존 | **51 audit 권고** |
| **R-5** | base64 / URL-encoded / 압축 evasion | Hermes upstream R2-6 또는 facade 확장 | ❌ known limitation | MVP-2/3 분리 (G3-4) | **본 cycle 범위 외 (영구 분리)** |

### §2.2 R 결정 권고

⭐ **권고 R 결정 = R-4 (defense-in-depth 목적) 채택 + 구현 경로 차등 명시**:

1. **R-3 = MVP-2 PASS gating 수단** (CI 회귀 검증, 시제 충족 — 즉시 PASS 격상 경로). ⚠️ **R-3 = GP-2 (d) *detection* (자동 회귀 검증) 충족** (N-5 정정). *prevention* (능동 송신 redaction) = R-1/R-2 의존 — facade placeholder 현 시점 능동 redaction 0.
2. **R-1 (Hermes upstream) + R-2 (facade real) = ends (prevention) 보조 means, 구현 경로 = 별도 trajectory**. 본 cycle = R-1/R-2 를 R-4 defense-in-depth 구성요소로 채택하되, **구현 경로 결정 (Hermes import / facade real) = 별도 cycle** 명시 (§0.2 #9 #10).
3. **R-5 = 영구 분리** (base64 evasion = MVP-2/3, G3-4 답습).

→ ⭐ **R-4 ≡ "R-3 (즉시 발효) + R-1/R-2 (deferred trajectory)" framing 선택지** (N-4): "R-4 채택" 과 "R-3 단독 채택 + R-1/R-2 deferred 명시" = 실질 동형 (현 시점 능동 means = R-3 한정). 본 brief = R-4 라벨 채택 (defense-in-depth ends 지향) + R-3 우선 발효 명시.

→ **means-vs-ends 정합 (ADR-011)**: GP-2 의 *ends* (secret 송신/로그 leak 0) = R-4 다층 지향. 본 repo 內 *즉시 발효 가능 means* = R-3 (CI detection). R-1/R-2 = prevention 보조 means, 구현 = cross-trajectory 의존. **MVP-2 PASS 시점 GP-2 (a)~(e) 충족 = R-3 actual run PASS (detection) + R-1/R-2 evidence 가용 시점 (prevention) 합산** (실 구현 sub-cycle 영역).

### §2.3 R 결정 시 trade-off

| 결정 | 장점 | 단점 / risk |
|------|----|----------|
| R-4 (권고) | defense-in-depth ends 충족 / R-3 즉시 발효 / 기존 시제 답습 | R-1/R-2 cross-trajectory 의존 → MVP-2 PASS 시점 GP-2 완전 충족이 Hermes import + facade real 에 부분 종속 (단, R-3 단독으로 (d) 자동 회귀 충족) |
| R-3 단독 | 즉시 발효 / 의존 0 | prevention 부재 (detection-only) — R-1/R-2 deferred 시 능동 송신 redaction 0 (단, R-4 와 실질 동형 — R-1/R-2 deferred 명시 시) |
| R-1 우선 | Hermes native 정공 | Hermes import 결정 선행 의무 (본 cycle 범위 외) → MVP-2 진입 지연 |

→ **R-4 채택 + R-3 우선 발효 + R-1/R-2 cross-trajectory 의존 명시** 가 ceremony-inflation 차단 + 즉시 진전 + ends 충족 정합.

---

## §3 L sub-수단 결정 (G4 §4.4 Layer 4 CI 회귀 검증)

### §3.1 후보 비교 (51 audit §3.4 답습 + 본 cycle audit 갱신)

⚠️ **B-1 핵심 정정**: v1 은 L-4 (L-1 stdlib) 를 시제 충족으로 권고했으나, 실 시제는 **rfc8785/jcs Primary** (runtime `PRIMARY_1_ONLY`). stdlib 단독 경로는 runtime 미사용 (auto-degrade 0). rfc8785/jcs = **Q1 합의 2026-05-10 이미 채택**. 후보 분류 재정렬:

| # | 수단 | 영역 | Library | 본 repo 구현 상태 | 등급 |
|---|------|----|---------|----------------|----|
| **L-1** | Layer 1 hash chain Python stdlib 단독 (`hashlib.sha256` + `json.dumps`) | hash chain 검증 | stdlib | ❌ **시제 미충족** (runtime = PRIMARY_1_ONLY rfc8785, stdlib 경로 미사용) | 가설적 (auto-degrade 부재) |
| **L-1.5** ⭐ (N-2 신규) | Layer 1 + stdlib auto-degrade fallback (rfc8785 부재 시 json.dumps degrade) | hash chain | stdlib fallback | ❌ 미구현 (현 PRIMARY_1_ONLY = degrade 없음) | 별도 실 구현 sub-cycle 선택 (Provider Liquidity 강화 옵션) |
| **L-2** | Layer 1 + RFC 8785 JCS Primary (`rfc8785` / `jcs`) | hash chain + canonical | 외부 library | ✅ **시제 충족** (`requirements-dev.txt:20-21` 고정 + `canonical_json.py` Primary + Q1 합의 채택) | 기존 PoC 운영 중 |
| **L-3** | Layer 4 R-6 workflow step (canonical 위반 + prev_hash mismatch + timestamp monotonicity) | CI 회귀 | shell + Python | ✅ **시제 충족** (4 G4 workflow 분리 운영) | R-6 답습 확장 |
| **L-4** | L-1 + L-3 병행 (stdlib MVP) | Layer 1+4 | stdlib | ❌ 시제 미충족 (L-1 미충족) | ~~51 audit 권고~~ → 재분류 |
| **L-5** | L-2 + L-3 병행 (외부 JCS Primary) | Layer 1+4 + JCS | 외부 library | ✅ **양쪽 시제 충족 (기존 PoC = 실질 L-5)** | **본 cycle 실 상태 = L-5** |

### §3.2 L 결정 권고 (B-1 정정)

⭐ **권고 L 결정 = "기존 rfc8785/jcs Primary PoC 보존 (Q1 합의 2026-05-10 답습) + L-3 CI step" — 실질 L-5, 본 cycle 신규 외부 library 도입 0**:

1. **기존 rfc8785/jcs Primary 보존** — Q1 합의 (`3plus1-consensus-2026-05-10-g4-jcs-library-selection.md`, 17 조건) 로 *이미 채택*. `requirements-dev.txt:20-21` 고정 + `canonical_json.py` Primary + `jsonl_hash_chain.py:99` runtime PRIMARY_1_ONLY + `g4-hash-chain.yml:64` CI 설치. 본 cycle = **보존, 신규 도입 0**.
2. **L-3 (R-6 step) = CI 회귀 검증** — 4 G4 workflow 분리 운영 시제 충족.
3. **신규 외부 JCS library 도입/운영 승격 = 별도 cycle** (N-7 정정 — "L-2/L-5 영구 분리" 아님). 의존성 *변경* trigger = ADR-011 §2.3 #4 (Hermes 의존성 → R-2/R-6 재실행). rfc8785/jcs 는 Q1 합의 채택이므로 본 cycle trigger 발화 0.
4. **L-1.5 (stdlib auto-degrade) = 별도 실 구현 sub-cycle 선택** (N-2) — Provider Liquidity 강화 옵션 (rfc8785 부재 시 degrade), 현 시제 미구현. 본 cycle 결정 0.

→ ⭐ **"본 cycle 신규 외부 library 도입 0" (true) ≠ "현 PoC 외부 library 미사용" (false)** 분리 (B-1/codex BL-2). 현 PoC = rfc8785/jcs Primary 사용 중.

→ **means-vs-ends 정합 (N-3)**: Layer 4 의 *ends* = ledger 무결성 (middle tampering / canonical 위반 / timestamp 위반 차단). **RFC 8785 JCS = canonical *interop* 수단 (means), 무결성 ends 자체 아님**. 기존 rfc8785/jcs Primary + cross-check corpus (72 files) = ends 충족 입증. L-1.5 (stdlib degrade) = 동일 ends 의 Provider-liquidity 강화 *대안 means* (별도 선택).

### §3.3 L 결정 시 trade-off

| 결정 | 장점 | 단점 / risk |
|------|----|----------|
| 기존 rfc8785/jcs 보존 (권고, 실질 L-5) | 시제 충족 (Q1 합의 채택) / 즉시 PASS 격상 / 신규 도입 0 (trigger 발화 0) | 외부 library 의존 (단 Q1 합의 발효 답습, 신규 결정 아님) / rfc8785 부재 시 degrade 0 (L-1.5 별도 보강 영역) |
| L-1.5 stdlib auto-degrade 추가 | Provider Liquidity 강화 (외부 library 부재 내성) | 실 구현 부담 (별도 sub-cycle) + degrade 경로 canonical 동등성 재검증 의무 |
| L-1 stdlib 단독 전환 | 외부 의존 0 | 기존 PoC + Q1 합의 파괴 + runtime canonical 재작성 (과잉, 비권고) |

---

## §4 W 통합 방식 결정 (workflow 통합) — 실 repo 현 상태 핵심

### §4.1 후보 비교 (52 entry §2.3.2 답습 + 본 cycle audit 현 상태)

⭐ **본 cycle 핵심 tension (52 entry B-5 답습)**: 51 audit §4.2 = "W-A 단일 R-6 통합" 권고. 그러나 **실 repo 는 이미 workflow 분리 운영** (g4-hash-chain.yml + history-anchor-verifier.yml + rewrite-defense.yml + r2-canary.yml + secret-hygiene-egress-redaction.yml). W-A "일괄 통합" = **기존 5+ workflow 병합 = 대규모 파괴적 변경**.

⚠️ **B-5 정정**: v1 은 권고를 "보존 우선 = W-A(ii) 변형" 으로 명명했으나, W-A 본질 = *단일 통합* 이고 권고 실질 = *분산 보존 (신규 0)* = 정반대. 명칭 혼선 차단 위해 **2축 분류 (통합/분리)×(신설/보존)** + **W-F (분산 보존, 신규 통합/신설 0) 신규 라벨** 도입:

| # | 수단 | 축 (통합·분리 / 신설·보존) | 실 repo 현 상태 정합 | 비고 |
|---|------|------------------|------------------|----|
| **W-A** | 단일 R-6 확장 (GP-2 + G4 통합) | 통합 / 신설·병합 | ⚠️ (i) 일괄 통합 = 파괴적 / (ii) 보존 + 중복 step | 비권고 (기존 분리 운영 파괴) |
| **W-B** | 별도 workflow 2개 신설 | 분리 / 신설 | ⚠️ 기존 workflow 와 중복 신설 (ceremony-inflation) | 비권고 (기존 secret-hygiene + g4-hash-chain 중복) |
| **W-C** | 단계 분리 (GP-2 우선 + G4 후속) | 시간 분리 | 합의 cycle 2회 부담 | (γ-c) 통합 동시 의무와 trade-off |
| **W-D** | roadmap.md §5.3 별도 progression | progression | roadmap 답습 / 통합 효율 손실 | 검토 |
| **W-E** | pre-commit hook (CI 외 보조) | 보조 layer | CI 회귀 검증 ≠ pre-commit | **보조 동시 가능** (CI 와 병행) |
| **W-F** ⭐ (B-5 신규) | **기존 분산 workflow 보존 (신규 통합/신설 0), 누락 step 만 기존 workflow 內 보강** | 분리 / 보존 | ✅ **실 repo 12 workflow 분산 운영 정합** | **본 brief 권고** |

### §4.2 W 결정 권고

⭐ **권고 W 결정 = W-F (기존 분산 workflow 보존, 신규 통합/신설 0) + W-E 보조 병행** (B-5 정정 — "W-A(ii) 변형" 명칭 폐기):

1. **기존 5+ workflow 보존** (g4-hash-chain.yml + history-anchor-verifier.yml + rewrite-defense.yml + r2-canary.yml + secret-hygiene-egress-redaction.yml) — 신규 통합 workflow 생성 0, 기존 파괴 0. 이는 W-A(ii) "보존 + 중복 step 추가" 의 *최소 변형* = "보존 + (필요 시) 누락 step 추가".
2. **Layer 4 CI 회귀 검증 (L-3) = 기존 G4 workflow 답습 확장** — g4-hash-chain.yml (Layer 1) + history-anchor-verifier.yml + rewrite-defense.yml (Layer 2) 이 이미 Layer 4 회귀 검증 역할 수행. 누락 영역 (예: timestamp monotonicity step / HISTORY_REWRITE enum fixture) = 기존 workflow 內 step 추가 (실 구현 sub-cycle).
3. **GP-2 (R-3) = 기존 secret-hygiene-egress-redaction.yml 답습** — D-2 scan-log redaction 검증 이미 운영. 신규 step 불필요 (또는 canary inject 보강 = 실 구현 sub-cycle).
4. **W-E (pre-commit) = 보조 병행** — dev 환경 즉시 검증 (CI 회귀와 병행, 대체 아님).
5. **W-A(i) 일괄 통합 + W-B 신설 = 비권고** (파괴적 / ceremony-inflation). **W-C 단계 분리 = 비권고** ((γ-c) 통합 동시 의무 3 와 trade-off — Layer 1+2+4 통합 동시 발효 의무가 GP-2 와 G4 의 *동시* 진행을 요구하지는 않으나, 55 entry 진입 권한이 통합 영역으로 발효되어 분리 cycle 2회 부담은 ceremony-inflation).

→ ⭐ **W 결정 핵심 = W-F "기존 분산 구조 보존, 신규 통합/신설 0, 누락 step 만 기존 workflow 內 보강"**. 이는 51 audit W-A 권고의 *정신* (ceremony-inflation 차단)을 *실 repo 현 상태* (이미 12 workflow 분산 운영)에 맞춰 정밀화한 신규 라벨. codex = "W-A 권고를 repo 현실에 맞춘 정밀화로 정합" 판정 + Agent C = "명칭 W-A(ii) 부정확" 지적 → **실질 권고 정합 + 라벨 W-F 정정** 동시 충족 (B-5).

### §4.3 W 결정 시 (γ-c) 특화 의무 정합 확인

- 의무 2 ("부분 답습" framing): W 결정이 Layer 3 (Signed commit) + Layer 5 (External anchor) 진입 유발 0. (단, history-anchor-verifier.yml = Layer 5 External anchor PoC 시제 *이미 운영* — 55 B-2 답습. "보존" = PoC 시제 보존이지 Layer 5 *결정 영역 진입* 0).
- 의무 3 (통합 동시 발효): W "보존 우선" 이 Layer 1+2+4 통합 PASS evidence 동시 발효 저해 0 (기존 workflow 가 Layer 1+2 분담, Layer 4 = 회귀 검증 통합).


codex
초기 문서 대조상 60 brief는 51 audit의 `(d) gap`을 “나중에 구현된/발견된 D-2 workflow가 이미 운영 중이었다”는 식으로 정정하고 있습니다. 이제 실제 workflow, scanner, fixtures, ADR 문구, `gh run`과 git history를 확인해 그 정정이 과장인지 보겠습니다.
exec
/bin/bash -lc "nl -ba .github/workflows/secret-hygiene-egress-redaction.yml | sed -n '1,220p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# G2 GP-3 + GP-2 Credential/Secret Hygiene + Egress Redaction — Group D PoC
     2	#
     3	# 답습 출처:
     4	#   - docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md (본 PoC 사양 §9 — 12 step CI 설계)
     5	#   - docs/architecture/redaction-pattern-equivalence.md (R-4 — 패턴 동등성 카탈로그)
     6	#   - docs/phase0/r4-1-trigger-extension-evidence.md §4.1 (R-4.1 — 45 patterns trigger 등록)
     7	#   - .github/workflows/memory-skill-migration-feasibility.yml (Group F 형식 + 후속 보조 작업 답습)
     8	#
     9	# 본 workflow 의 6 검증 (사용자 명시 5.1 답습):
    10	#   - D-1 PASS scan (scan-source pass/) rc=0 + violations=0
    11	#   - D-1 FAIL scan (scan-source fail/) rc=1 + ≥4 + 4 패턴 cover (prefix / regex / alternation / private-key)
    12	#   - D-2 PASS redaction residual (scan-log redaction_pass/) rc=0 + 0 잔존
    13	#   - D-2 FAIL redaction leak (scan-log redaction_fail/) rc=1 + partial leak 검출 (base64 = known limitation)
    14	#   - Tier-1 pattern count self-check (--list-patterns) registered_patterns_count=45 + tier1_42_catalog_compliant=True
    15	#   - F-금지 자기 검증 (실 API key / provider SDK import 0건 grep)
    16	#
    17	# 본 PoC 는 G2 GP-2 / GP-3 *형식적 검출 layer 시제* 한정 — G2 GP-2 / GP-3 / G2 전체 Implementation/Runtime PASS 권한 0건.
    18	# 풀 3+1 승격 trigger 7 = 0/7 발화 → Reviewer-only 단축 합의 적격.
    19	#
    20	# Artifact path = group-d-logs/ (Group F 후속 답습 — leading dot 미사용, hidden dir 정책 미의존).
    21	name: G2 GP-3 + GP-2 Secret Hygiene & Egress Redaction
    22	
    23	on:
    24	  push:
    25	    branches:
    26	      - main
    27	      - develop
    28	      - "feature/**"
    29	    paths:
    30	      - "tools/secret_scanner.py"
    31	      - "tools/docker_secret_image_layer_check.sh"
    32	      - "tools/docker_secret_restart_recovery.sh"
    33	      - "tools/mvp1_pc3_ar1_integration_check.py"
    34	      - "tools/workflow_secrets_usage_check.py"
    35	      - "tools/workflow_secrets_reference_check.py"
    36	      - "tools/workflow_fork_pr_secret_policy_check.py"
    37	      - "tools/workflow_permissions_check.py"
    38	      - "tools/docker_secret_inotify_sidecar_check.sh"
    39	      - "tests/fixtures/secret_hygiene/**"
    40	      - "tests/fixtures/gp3_st3/**"
    41	      - "tests/fixtures/gp3_st2/**"
    42	      - "tests/fixtures/mvp1_pc3_ar1_integration/**"
    43	      - "tests/fixtures/stage5_g3_7/**"
    44	      - "docker/gp3-st3-poc/**"
    45	      - "docker/gp3-st2-poc/**"
    46	      - "tests/fixtures/secret_hygiene/mvp1_s3/**"
    47	      - "requirements-dev.txt"
    48	      - ".github/workflows/secret-hygiene-egress-redaction.yml"
    49	      # Stage 4 (PC-3 + AR-1 통합 검증) 답습 — 양 GP workflow 변경 시 cross-workflow re-verify
    50	      - ".github/workflows/provider-adapter-enforcement.yml"
    51	      - ".github/workflows/provider-url-scanner.yml"
    52	  pull_request:
    53	    branches:
    54	      - main
    55	      - develop
    56	  schedule:
    57	    # ST-2 inotify sidecar PoC + S-3 detect-secrets 일관 nightly 발화 의무
    58	    # 답습 출처:
    59	    #   - docs/phase0/mvp1-st2-inotify-sidecar-brief.md §4 (D-2 = UTC 03:00 = KST 12:00)
    60	    #   - docs/review/3plus1-consensus-2026-05-27-mvp1-st2-inotify-sidecar.md (Reviewer-only APPROVE)
    61	    #   - 24번째 entry brief v1.1 §3 line 261 ST-2 cell ("docker-compose sidecar nightly run +
    62	    #     tools/docker_secret_inotify_sidecar_check.sh nightly workflow 통합")
    63	    # nightly UTC 03:00 = KST 12:00 (한국 업무 시간 중 발화 = 사용자 인지 + 신속 대응 자격)
    64	    - cron: "0 3 * * *"
    65	
    66	permissions:
    67	  contents: read
    68	
    69	jobs:
    70	  scan:
    71	    runs-on: ubuntu-latest
    72	    timeout-minutes: 10
    73	    steps:
    74	      - name: Checkout
    75	        uses: actions/checkout@v6
    76	
    77	      - name: Set up Python
    78	        uses: actions/setup-python@v6
    79	        with:
    80	          python-version: "3.12"
    81	
    82	      - name: Prepare log directory (artifact 답습)
    83	        run: mkdir -p group-d-logs
    84	
    85	      - name: Tier-1 pattern count self-check (--list-patterns)
    86	        id: pattern_count
    87	        run: |
    88	          set +e
    89	          python tools/secret_scanner.py --list-patterns \
    90	            > group-d-logs/list-patterns.stdout 2> group-d-logs/list-patterns.stderr
    91	          rc=$?
    92	          set -e
    93	          cat group-d-logs/list-patterns.stderr
    94	          if [ "$rc" -ne 0 ]; then
    95	            echo "::error::--list-patterns expected rc=0, got rc=$rc"
    96	            exit 1
    97	          fi
    98	          if ! grep -q "registered_patterns_count=45" group-d-logs/list-patterns.stderr; then
    99	            echo "::error::registered_patterns_count != 45 (expected R-4.1 답습)"
   100	            exit 1
   101	          fi
   102	          if ! grep -q "tier1_42_catalog_compliant=True" group-d-logs/list-patterns.stderr; then
   103	            echo "::error::tier1_42_catalog_compliant != True (R-4.1 답습 위반)"
   104	            exit 1
   105	          fi
   106	          echo "pattern_count=PASS" >> $GITHUB_OUTPUT
   107	          echo "Tier-1 pattern count self-check OK (registered=45, compliant=True)"
   108	
   109	      - name: D-1 PASS scan — scan-source pass/ (rc=0 + violations=0)
   110	        id: d1_pass
   111	        run: |
   112	          set +e
   113	          python tools/secret_scanner.py --mode scan-source \
   114	            tests/fixtures/secret_hygiene/pass/ \
   115	            > group-d-logs/d1-pass.stdout 2> group-d-logs/d1-pass.stderr
   116	          rc=$?
   117	          set -e
   118	          cat group-d-logs/d1-pass.stderr
   119	          if [ "$rc" -ne 0 ]; then
   120	            echo "::error::D-1 PASS expected rc=0, got rc=$rc (FP detected)"
   121	            exit 1
   122	          fi
   123	          if ! grep -q "violations=0" group-d-logs/d1-pass.stderr; then
   124	            echo "::error::D-1 PASS missing 'violations=0'"
   125	            exit 1
   126	          fi
   127	          echo "d1_pass=PASS" >> $GITHUB_OUTPUT
   128	          echo "D-1 PASS scan OK (rc=0, violations=0, FP=0)"
   129	
   130	      - name: D-1 FAIL scan — scan-source fail/ (rc=1 + ≥4 + 4 패턴 cover)
   131	        id: d1_fail
   132	        run: |
   133	          set +e
   134	          python tools/secret_scanner.py --mode scan-source \
   135	            tests/fixtures/secret_hygiene/fail/ \
   136	            > group-d-logs/d1-fail.stdout 2> group-d-logs/d1-fail.stderr
   137	          rc=$?
   138	          set -e
   139	          cat group-d-logs/d1-fail.stderr
   140	          if [ "$rc" -ne 1 ]; then
   141	            echo "::error::D-1 FAIL expected rc=1, got rc=$rc"
   142	            exit 1
   143	          fi
   144	          # ≥4 violations 강제
   145	          violations=$(grep -oE "violations=[0-9]+" group-d-logs/d1-fail.stderr | head -1 | grep -oE "[0-9]+")
   146	          if [ -z "$violations" ] || [ "$violations" -lt 4 ]; then
   147	            echo "::error::D-1 FAIL expected violations>=4, got '$violations'"
   148	            exit 1
   149	          fi
   150	          # 3 카테고리 cover (prefix-baseline + regex + alternation; private-key 는 regex sub-type T1-035)
   151	          for cat in "prefix-baseline" "regex" "alternation"; do
   152	            if ! grep -q "$cat" group-d-logs/d1-fail.stderr; then
   153	              echo "::error::D-1 FAIL missing pattern category: $cat"
   154	              exit 1
   155	            fi
   156	          done
   157	          # private-key sub-type 검증 (T1-035 ID grep)
   158	          if ! grep -q "T1-035" group-d-logs/d1-fail.stderr; then
   159	            echo "::error::D-1 FAIL missing private-key sub-type (T1-035)"
   160	            exit 1
   161	          fi
   162	          echo "d1_fail=PASS" >> $GITHUB_OUTPUT
   163	          echo "D-1 FAIL scan OK (rc=1, violations=$violations, 4 패턴 cover incl. private-key T1-035)"
   164	
   165	      - name: D-2 PASS redaction residual — scan-log redaction_pass/ (rc=0 + 0 잔존)
   166	        id: d2_pass
   167	        run: |
   168	          set +e
   169	          python tools/secret_scanner.py --mode scan-log \
   170	            tests/fixtures/secret_hygiene/redaction_pass/ \
   171	            > group-d-logs/d2-pass.stdout 2> group-d-logs/d2-pass.stderr
   172	          rc=$?
   173	          set -e
   174	          cat group-d-logs/d2-pass.stderr
   175	          if [ "$rc" -ne 0 ]; then
   176	            echo "::error::D-2 PASS expected rc=0 (redaction marker 인식 OK), got rc=$rc"
   177	            exit 1
   178	          fi
   179	          if ! grep -q "violations=0" group-d-logs/d2-pass.stderr; then
   180	            echo "::error::D-2 PASS missing 'violations=0'"
   181	            exit 1
   182	          fi
   183	          echo "d2_pass=PASS" >> $GITHUB_OUTPUT
   184	          echo "D-2 PASS redaction residual OK (rc=0, 잔존=0, [REDACTED] 마커 인식)"
   185	
   186	      - name: D-2 FAIL redaction leak — scan-log redaction_fail/ (rc=1 + partial leak 검출)
   187	        id: d2_fail
   188	        run: |
   189	          set +e
   190	          python tools/secret_scanner.py --mode scan-log \
   191	            tests/fixtures/secret_hygiene/redaction_fail/ \
   192	            > group-d-logs/d2-fail.stdout 2> group-d-logs/d2-fail.stderr
   193	          rc=$?
   194	          set -e
   195	          cat group-d-logs/d2-fail.stderr
   196	          if [ "$rc" -ne 1 ]; then
   197	            echo "::error::D-2 FAIL expected rc=1 (partial leak 검출), got rc=$rc"
   198	            exit 1
   199	          fi
   200	          # partial_redact.txt leak 검출 강제
   201	          if ! grep -q "partial_redact.txt" group-d-logs/d2-fail.stderr; then
   202	            echo "::error::D-2 FAIL missing partial_redact.txt leak detection"
   203	            exit 1
   204	          fi
   205	          # base64_evasion.txt 미검출 = 의도된 known limitation (PoC 사양 §8 #1 답습)
   206	          if grep -q "base64_evasion.txt" group-d-logs/d2-fail.stderr; then
   207	            echo "::warning::base64_evasion.txt 가 검출됨 — known limitation 영역 변경 가능성 (사양 §8 #1 검토 필요)"
   208	          else
   209	            echo "base64 evasion = known limitation 답습 (Hermes upstream R2-6 영역, 본 PoC 미검출 의도)"
   210	          fi
   211	          echo "d2_fail=PASS" >> $GITHUB_OUTPUT
   212	          echo "D-2 FAIL redaction leak OK (rc=1, partial_redact 검출, base64 미검출 = known limitation)"
   213	
   214	      - name: F-금지 자기 검증 (Layer 1 grep — 실 API key / provider SDK 0건)
   215	        id: forbidden_check
   216	        run: |
   217	          set -e
   218	          # F-금지 #1: 실 API key 0건 (fake canary 의무 — 모든 secret 은 FAKE / NOTAREAL / fakecanary marker 포함)
   219	          # 검사 대상 = fixture + scanner. scanner regex catalog 자체는 정의이므로 *fake marker 없는 raw secret*
   220	          # 형식이 fixture / scanner 외 위치에 존재 시 위반.

exec
/bin/bash -lc "nl -ba tools/secret_scanner.py | sed -n '1,260p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	#!/usr/bin/env python3
     2	"""Secret scanner — Group D PoC (G2 GP-3 Credential/Secret Hygiene + GP-2 Egress Redaction).
     3	
     4	답습 출처:
     5	  - docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md (본 PoC 사양)
     6	  - docs/architecture/redaction-pattern-equivalence.md (R-4 — 패턴 동등성 카탈로그)
     7	  - docs/phase0/r4-1-trigger-extension-evidence.md §4.1 (R-4.1 — Tier-1 42 catalog + baseline 5)
     8	  - docker/r4-1-poc/r4_1_poc.py line 51~213 (Tier-1 42 patterns + baseline 5 직접 답습)
     9	  - docs/architecture/governance-preconditions.md §4 (GP-2) + §5 (GP-3)
    10	  - docs/decisions/ADR-011-means-vs-ends-redaction.md §2.1 (a)~(e)
    11	
    12	핵심 강제 조건 (사용자 명시 답습):
    13	  - R-4.1 Tier-1 42 catalog + baseline 5 = 45 patterns 직접 답습 (변경 0건)
    14	  - Prefix 36 (baseline 5 + Tier-1 prefix 31) + 추가 regex 7 (H-A/B/C/E/F/G/K) + alternation 2 (H-J/H-L key 기반)
    15	  - H-J / H-L 직접 등록 제외 (alternation 채택, R-4.1 §4.2 답습)
    16	  - Tier-2 / Tier-3 catalog 확장 0건
    17	  - 외부 의존성 0건 (custom scanner 단독, gitleaks/detect-secrets 미도입)
    18	
    19	Mode (사용자 명시):
    20	  --mode scan-source : code-side secret 검출 (D-1 GP-3 Credential/Secret Hygiene)
    21	  --mode scan-log    : redaction 후 잔존 secret 검출 (D-2 GP-2 Egress Redaction)
    22	
    23	  본 PoC = 형식적 검출 layer 한정. Hermes 컨테이너 chmod / inotify (R1-2) =
    24	  Hermes upstream 영역, 본 PoC 미진입 (사용자 명시 #6).
    25	
    26	종료 코드:
    27	  0 = 위반 0건 (PASS)
    28	  1 = ≥1 위반 검출 (FAIL — D-1 secret 검출 / D-2 잔존 leak 검출)
    29	  2 = 입력 오류 (path 부재 등)
    30	
    31	알려진 한계 (사용자 명시 — 사양 §8):
    32	  - base64 / URL-encoded / 압축 등 advanced evasion 미커버 (Hermes upstream R2-6 영역)
    33	"""
    34	from __future__ import annotations
    35	
    36	import argparse
    37	import dataclasses
    38	import re
    39	import sys
    40	from dataclasses import dataclass
    41	from pathlib import Path
    42	from typing import Callable
    43	
    44	# ============================================================================
    45	# Tier-1 패턴 카탈로그 (45종) — R-4.1 §4.1 직접 답습
    46	#
    47	# 형식: (id, source, category, vendor, regex)
    48	#   - id: BL-N (baseline) 또는 T1-NNN (Tier-1)
    49	#   - source: Hermes 측 출처 식별자
    50	#   - category: prefix-baseline / prefix / regex / alternation
    51	#   - vendor: 사람이 읽을 수 있는 vendor/유형 라벨
    52	#   - regex: scanner 등록용 정규식 문자열
    53	# ============================================================================
    54	
    55	# Baseline 5 prefix (R-2 PoC 보존 — R-4.1 §4.1)
    56	BASELINE_PREFIX: list[tuple[str, str, str, str, str]] = [
    57	    ("BL-1", "Hermes #1 (sk-ant-)", "prefix-baseline", "Anthropic",
    58	     r"sk-ant-[A-Za-z0-9_-]{10,}"),
    59	    ("BL-2", "Hermes #1 (sk-)", "prefix-baseline", "OpenAI/Anthropic/etc",
    60	     r"sk-[A-Za-z0-9_-]{10,}"),
    61	    ("BL-3", "Hermes #2", "prefix-baseline", "GitHub PAT classic",
    62	     r"ghp_[A-Za-z0-9]{10,}"),
    63	    ("BL-4", "Hermes #15", "prefix-baseline", "AWS Access Key ID",
    64	     r"AKIA[A-Z0-9]{16}"),
    65	    ("BL-5", "Hermes #8", "prefix-baseline", "Slack tokens",
    66	     r"xox[baprs]-[A-Za-z0-9-]{10,}"),
    67	]
    68	
    69	# Tier-1 prefix 31 (Hermes #3..#7, #9..#14, #16..#35) — R-4.1 §4.1 직접 답습
    70	PREFIX_PATTERNS: list[tuple[str, str, str, str, str]] = [
    71	    ("T1-001", "Hermes #3", "prefix", "GitHub PAT (fine-grained)",
    72	     r"github_pat_[A-Za-z0-9_]{10,}"),
    73	    ("T1-002", "Hermes #4", "prefix", "GitHub OAuth access token",
    74	     r"gho_[A-Za-z0-9]{10,}"),
    75	    ("T1-003", "Hermes #5", "prefix", "GitHub user-to-server",
    76	     r"ghu_[A-Za-z0-9]{10,}"),
    77	    ("T1-004", "Hermes #6", "prefix", "GitHub server-to-server",
    78	     r"ghs_[A-Za-z0-9]{10,}"),
    79	    ("T1-005", "Hermes #7", "prefix", "GitHub refresh token",
    80	     r"ghr_[A-Za-z0-9]{10,}"),
    81	    ("T1-006", "Hermes #9", "prefix", "Google API keys",
    82	     r"AIza[A-Za-z0-9_-]{30,}"),
    83	    ("T1-007", "Hermes #10", "prefix", "Perplexity",
    84	     r"pplx-[A-Za-z0-9]{10,}"),
    85	    ("T1-008", "Hermes #11", "prefix", "Fal.ai",
    86	     r"fal_[A-Za-z0-9_-]{10,}"),
    87	    ("T1-009", "Hermes #12", "prefix", "Firecrawl",
    88	     r"fc-[A-Za-z0-9]{10,}"),
    89	    ("T1-010", "Hermes #13", "prefix", "BrowserBase",
    90	     r"bb_live_[A-Za-z0-9_-]{10,}"),
    91	    ("T1-011", "Hermes #14", "prefix", "Codex encrypted tokens",
    92	     r"gAAAA[A-Za-z0-9_=-]{20,}"),
    93	    ("T1-012", "Hermes #16", "prefix", "Stripe secret key (live)",
    94	     r"sk_live_[A-Za-z0-9]{10,}"),
    95	    ("T1-013", "Hermes #17", "prefix", "Stripe secret key (test)",
    96	     r"sk_test_[A-Za-z0-9]{10,}"),
    97	    ("T1-014", "Hermes #18", "prefix", "Stripe restricted key",
    98	     r"rk_live_[A-Za-z0-9]{10,}"),
    99	    ("T1-015", "Hermes #19", "prefix", "SendGrid API key",
   100	     r"SG\.[A-Za-z0-9_-]{10,}"),
   101	    ("T1-016", "Hermes #20", "prefix", "HuggingFace token",
   102	     r"hf_[A-Za-z0-9]{10,}"),
   103	    ("T1-017", "Hermes #21", "prefix", "Replicate API token",
   104	     r"r8_[A-Za-z0-9]{10,}"),
   105	    ("T1-018", "Hermes #22", "prefix", "npm access token",
   106	     r"npm_[A-Za-z0-9]{10,}"),
   107	    ("T1-019", "Hermes #23", "prefix", "PyPI API token",
   108	     r"pypi-[A-Za-z0-9_-]{10,}"),
   109	    ("T1-020", "Hermes #24", "prefix", "DigitalOcean PAT",
   110	     r"dop_v1_[A-Za-z0-9]{10,}"),
   111	    ("T1-021", "Hermes #25", "prefix", "DigitalOcean OAuth",
   112	     r"doo_v1_[A-Za-z0-9]{10,}"),
   113	    ("T1-022", "Hermes #26", "prefix", "AgentMail API key",
   114	     r"am_[A-Za-z0-9_-]{10,}"),
   115	    ("T1-023", "Hermes #27", "prefix", "ElevenLabs TTS key",
   116	     r"sk_[A-Za-z0-9_]{10,}"),
   117	    ("T1-024", "Hermes #28", "prefix", "Tavily search API",
   118	     r"tvly-[A-Za-z0-9]{10,}"),
   119	    ("T1-025", "Hermes #29", "prefix", "Exa search API",
   120	     r"exa_[A-Za-z0-9]{10,}"),
   121	    ("T1-026", "Hermes #30", "prefix", "Groq Cloud API key",
   122	     r"gsk_[A-Za-z0-9]{10,}"),
   123	    ("T1-027", "Hermes #31", "prefix", "Matrix access token",
   124	     r"syt_[A-Za-z0-9]{10,}"),
   125	    ("T1-028", "Hermes #32", "prefix", "RetainDB API key",
   126	     r"retaindb_[A-Za-z0-9]{10,}"),
   127	    ("T1-029", "Hermes #33", "prefix", "Hindsight API key",
   128	     r"hsk-[A-Za-z0-9]{10,}"),
   129	    ("T1-030", "Hermes #34", "prefix", "Mem0 Platform API key",
   130	     r"mem0_[A-Za-z0-9]{10,}"),
   131	    ("T1-031", "Hermes #35", "prefix", "ByteRover API key",
   132	     r"brv_[A-Za-z0-9]{10,}"),
   133	]
   134	
   135	# Tier-1 추가 regex 7 (H-A, H-B, H-C, H-E, H-F, H-G, H-K — H-J/H-L 제외, R-4.1 §4.2 답습)
   136	REGEX_PATTERNS: list[tuple[str, str, str, str, str]] = [
   137	    ("T1-032", "Hermes H-A", "regex", "ENV assignment",
   138	     r"([A-Z0-9_]{0,50}(?:API_?KEY|TOKEN|SECRET|PASSWORD|PASSWD|CREDENTIAL|AUTH)[A-Z0-9_]{0,50})\s*=\s*(['\"]?)(\S+)\2"),
   139	    ("T1-033", "Hermes H-B", "regex", "JSON field with secret keys",
   140	     r'(?i)("(?:api_?[Kk]ey|token|secret|password|access_token|refresh_token|auth_token|bearer|secret_value|raw_secret|secret_input|key_material)")\s*:\s*"([^"]+)"'),
   141	    ("T1-034", "Hermes H-C", "regex", "Authorization header (Bearer)",
   142	     r"(?i)(Authorization:\s*Bearer\s+)(\S+)"),
   143	    ("T1-035", "Hermes H-E", "regex", "Private key block",
   144	     r"-----BEGIN[A-Z ]*PRIVATE KEY-----[\s\S]*?-----END[A-Z ]*PRIVATE KEY-----"),
   145	    ("T1-036", "Hermes H-F", "regex", "DB connstr password",
   146	     r"(?i)((?:postgres(?:ql)?|mysql|mongodb(?:\+srv)?|redis|amqp)://[^:]+:)([^@]+)(@)"),
   147	    ("T1-037", "Hermes H-G", "regex", "JWT token",
   148	     r"eyJ[A-Za-z0-9_-]{10,}(?:\.[A-Za-z0-9_=-]{4,}){0,2}"),
   149	    ("T1-039", "Hermes H-K", "regex", "URL userinfo (non-DB)",
   150	     r"(https?|wss?|ftp)://([^/\s:@]+):([^/\s@]+)@"),
   151	]
   152	
   153	# Tier-1 alternation 2 (H-J / H-L sensitive key 기반 변환, R-4.1 §4.1 답습)
   154	ALTERNATION_PATTERNS: list[tuple[str, str, str, str, str]] = [
   155	    # (b1-PC1-D6-false-positives) 합의 2026-05-27 APPROVE WITH CONDITIONS (R-1 BLOCKING 흡수)
   156	    # (b1-PC1-D6-fp-edge-extensions) 합의 2026-05-27 APPROVE (단축 + codex cross-vendor, semicolon + fragment 확장)
   157	    # word boundary `(?:^|[?&\s'\";#])` prefix — Python keyword arg FP 해소 + quoted body literal cover + Cookie semicolon + OAuth fragment cover
   158	    # `(` paren delimiter 추가 0 = `sort(key=...)` / `WorkerResult(exit_code=...)` FP 재발 회피 (codex N-4 답습)
   159	    # carry-over: (b1-PC1-D6-ast-context) AST SAFE_CONTEXT
   160	    ("T1-041", "Hermes _SENSITIVE_QUERY_PARAMS", "alternation", "URL query sensitive keys (16)",
   161	     r"(?i)(?:^|[?&\s'\";#])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|session|secret|key|code|signature|x-amz-signature)=[^&\s]+"),
   162	    ("T1-042", "Hermes _SENSITIVE_BODY_KEYS", "alternation", "Body/form sensitive keys (14)",
   163	     r"(?i)(?:^|[?&\s'\";#])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|secret|private_key|authorization|key)=[^&\s]+"),
   164	]
   165	
   166	ALL_PATTERNS: list[tuple[str, str, str, str, str]] = (
   167	    BASELINE_PREFIX + PREFIX_PATTERNS + REGEX_PATTERNS + ALTERNATION_PATTERNS
   168	)
   169	"""All registered patterns — 5 baseline + 31 prefix + 7 regex + 2 alternation = 45 patterns."""
   170	
   171	# Compiled regex objects (모듈 import 시 1회 컴파일)
   172	COMPILED_PATTERNS: list[tuple[str, str, str, str, re.Pattern[str]]] = [
   173	    (pid, src, cat, vendor, re.compile(rgx))
   174	    for (pid, src, cat, vendor, rgx) in ALL_PATTERNS
   175	]
   176	
   177	# 본 PoC 직접 등록 제외 (R-4.1 §4.2 답습 — alternation 채택, H-J/H-L 직접 등록 false-positive 회피)
   178	SKIP_DIRECT_REGISTER: frozenset[str] = frozenset({"T1-038", "T1-040"})
   179	
   180	# Redaction marker exclusion (scan-log mode 전용 — GP-2 D-2 contract 답습).
   181	# 사양 §0 — D-2 = "redaction 후 잔존 secret 검증". 본 marker 가 매칭 substring 전체를
   182	# 차지하면 *정상 redacted output* 로 분류, 위반 미카운트 (FP 회피).
   183	REDACTION_MARKER_RE: re.Pattern[str] = re.compile(
   184	    r"(?i)(\[REDACTED\]|\[FILTERED\]|\[MASKED\]|<REDACTED>|<MASKED>|<<masked>>|\*{5,})"
   185	)
   186	
   187	# Scan 대상 file extension (사양 §4.1~§4.2 답습)
   188	#
   189	# scope 정책 (49 entry 발효): docs/architecture/secret-scanner-scope-policy.md
   190	#   - hook entry scope: src + .github 한정 (.pre-commit-config.yaml 답습)
   191	#   - docs/ 영역 영구 금지 (~800+ 잠재 false positive 답습 — fake canary / redaction 예시 / codex 응답 sample)
   192	#   - scope 확장 의무 절차: 정책 §2 답습 (별도 sub-cycle + 풀 3+1 + R-7(b) 차등)
   193	#   - 본 SCAN_SOURCE_EXTENSIONS 변경 = catalog 본문 변경 = R-7(b) 차등 자격
   194	SCAN_SOURCE_EXTENSIONS: tuple[str, ...] = (
   195	    ".py", ".json", ".yaml", ".yml", ".toml", ".sh", ".bash",
   196	    ".env", ".ini", ".cfg", ".pem", ".key", ".txt", ".md",
   197	)
   198	SCAN_LOG_EXTENSIONS: tuple[str, ...] = (".txt", ".log", ".json", ".jsonl", ".md", ".pem")
   199	
   200	
   201	@dataclass(frozen=True)
   202	class Violation:
   203	    """Single secret detection."""
   204	
   205	    file: Path
   206	    line: int
   207	    pattern_id: str
   208	    pattern_source: str
   209	    pattern_category: str
   210	    pattern_vendor: str
   211	    matched_text: str
   212	
   213	    def format_short(self) -> str:
   214	        # Truncate matched_text to avoid leaking full canary in CI log (defensive)
   215	        sample = self.matched_text[:30] + ("..." if len(self.matched_text) > 30 else "")
   216	        return (
   217	            f"{self.file}:{self.line}:{self.pattern_id}:"
   218	            f"{self.pattern_category}:{self.pattern_vendor}: {sample!r}"
   219	        )
   220	
   221	
   222	def is_redaction_marker_match(matched_text: str) -> bool:
   223	    """Scan-log mode 한정 — 매칭 텍스트가 redaction marker 만 포함하면 정상 redacted (FP 회피).
   224	
   225	    GP-2 D-2 contract — 'redaction 후 잔존 secret 검증' (사양 §0).
   226	    예: `OPENAI_API_KEY=[REDACTED]` 의 H-A regex 매칭은 [REDACTED] marker → 위반 미카운트.
   227	    """
   228	    return REDACTION_MARKER_RE.search(matched_text) is not None
   229	
   230	
   231	def scan_text(text: str, file_path: Path, mode: str | None = None) -> list[Violation]:
   232	    """Apply all 45 patterns to text and return violations.
   233	
   234	    Line number = 1-indexed (file::line 표기 답습).
   235	    mode='scan-log' 시 redaction marker 매칭은 위반 미카운트 (FP 회피, 사양 §0).
   236	    """
   237	    vios: list[Violation] = []
   238	    for pid, src, cat, vendor, pattern in COMPILED_PATTERNS:
   239	        if pid in SKIP_DIRECT_REGISTER:
   240	            continue
   241	        for m in pattern.finditer(text):
   242	            matched = m.group(0)
   243	            if mode == "scan-log" and is_redaction_marker_match(matched):
   244	                continue
   245	            line_no = text[: m.start()].count("\n") + 1
   246	            vios.append(
   247	                Violation(
   248	                    file=file_path,
   249	                    line=line_no,
   250	                    pattern_id=pid,
   251	                    pattern_source=src,
   252	                    pattern_category=cat,
   253	                    pattern_vendor=vendor,
   254	                    matched_text=matched,
   255	                )
   256	            )
   257	    return vios
   258	
   259	
   260	def iter_files(root: Path, allowed_exts: tuple[str, ...]) -> list[Path]:

exec
/bin/bash -lc "find tests/fixtures/secret_hygiene -maxdepth 3 -type f -print -exec sed -n '1,80p' {} \\;" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
tests/fixtures/secret_hygiene/redaction_fail/partial_redact.txt
[INFO] config loaded with broken redaction
OPENAI_API_KEY=sk-FAKE-GROUP-D-NOT-A-REAL-SECRET
[WARN] partial redaction: prefix retained -> sk-FAK[REDACTED]
GITHUB_TOKEN=ghp_FAKE_GROUP_D_NOT_REAL_TOKEN
[INFO] residual scan expected: >=1 violation (leak detected)
tests/fixtures/secret_hygiene/redaction_fail/base64_evasion.txt
[INFO] config loaded with base64-encoded canary (advanced evasion test)
[NOTE] base64 evasion is a known limitation in Group D PoC scope.
[NOTE] base64 advanced evasion = Hermes upstream R2-6 area, separate consensus.
[NOTE] direct prefix/regex/alternation matching does NOT decode base64.
encoded_canary=c2stRkFLRS1HUk9VUC1ELU5PVC1BLVJFQUwtU0VDUkVU
[NOTE] this fixture documents the limitation; PoC is not blocked by missed detection.
[NOTE] decoding the value above yields a fake canary used elsewhere in tests.
tests/fixtures/secret_hygiene/pass/safe_config.py
# Group D PoC — D-1 PASS fixture (safe ENV assignment, no secrets)
# 답습: docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md §4.1
# 본 fixture 는 Tier-1 prefix / regex / alternation 패턴 0건 의무 (FP 검증).

BASE_URL = "https://example.com"
MAX_RETRIES = 3
TIMEOUT_SECONDS = 30
USER_AGENT = "group-d-poc/0.1"
tests/fixtures/secret_hygiene/pass/safe_settings.json
{
  "name": "alice",
  "email": "public@example.com",
  "page": 2,
  "lang": "en",
  "theme": "dark",
  "max_results": 100
}
tests/fixtures/secret_hygiene/mvp1_entry/pass/safe_lookalikes.py
# MVP-1 entry coverage — D-1 PASS fixture (FP-resistance 회귀 보강)
# 답습 출처: docs/phase0/backlog6-implementation-step-brief.md §2.2.1 sub-step 1.1
#
# 본 fixture 는 Tier-1 패턴 lookalike (정상 식별자 / 변수명 / docstring) 가
# FP 를 일으키지 않음을 MVP-1 entry 시점 회귀 보강. 답습 변경 0건.
#
# 본 fixture 위반 = 0건 의무 (D-1 PASS scan rc=0 + violations=0 답습).

# 정상 docstring (자주 sk / api / token 단어 사용)
"""Example module docstring.

This file demonstrates safe identifiers using sk and api token concepts
without any fake secret prefix patterns that should trigger detection.
"""

# 변수명 only (값 없음) — sk_ / ghp_ 등 prefix 어떤 변수명도 사용하지 않음
mock_placeholder = None
empty_value = ""
identifier_documentation = "see docs/architecture/* for identifier model definitions"

# 짧은 식별자 (prefix 패턴 길이 미만 → 미발화)
short_id = "sk-x"
short_aws = "AKIA0001"  # only 4 digits, 16자 미만 → AKIA[A-Z0-9]{16} 미발화

# 정상 URL (userinfo 없음)
DOC_URL = "https://docs.example.com/path?ref=normal"
API_BASE = "https://api.example.com/v1"

# 정상 JSON-like (sensitive key 없음)
NORMAL_CONFIG = {"name": "example", "version": "0.1", "max_retries": 3}
tests/fixtures/secret_hygiene/mvp1_entry/fail/regex_categories_extra.py
# MVP-1 entry coverage — D-1 FAIL fixture
# 답습 출처: docs/phase0/backlog6-implementation-step-brief.md §2.2.1 sub-step 1.1
#
# 본 fixture 는 기존 fail/ fixture (env_assignment / json_field / prefix_aws / private_key_block)
# 가 cover 하지 않는 regex 카테고리 (H-C / H-F / H-G / H-K) 를 MVP-1 entry 회귀 cover.
# 답습 변경 0건 — tools/secret_scanner.py 본문 / R-4.1 Tier-1 45 patterns 변경 0건.
#
# fake canary 의무 답습 (사용자 명시 — F-금지 #1):
#   모든 fake secret 은 FAKE / NOTAREAL / fakecanary / R41T marker 포함.

# H-C (T1-034) — Authorization Bearer
AUTH_HEADER_EXAMPLE = "Authorization: Bearer FAKEBEARERMVP1ENTRYNOTAREAL123"

# H-F (T1-036) — DB connstr password
DB_DSN = "postgresql://user:FAKEDBMVP1ENTRYNOTAREAL@db.example.com:5432/mydb"
REDIS_DSN = "redis://default:FAKEREDISMVP1ENTRYNOTAREAL@cache.example.com:6379"

# H-G (T1-037) — JWT-style token
FAKE_JWT = "eyJhbGciOiJIUzI1NiFAKEMVP1NOTAREAL.eyJpYXQiOjAxRkFLRQ.SIGFAKENOTAREALMVP1"

# H-K (T1-039) — URL userinfo (non-DB)
FAKE_WEBHOOK = "https://botuser:FAKEURLMVP1ENTRYNOTAREAL@hooks.example.com/path"
tests/fixtures/secret_hygiene/mvp1_entry/fail/tier1_prefix_variety.py
# MVP-1 entry coverage — D-1 FAIL fixture
# 답습 출처: docs/phase0/backlog6-implementation-step-brief.md §2.2.1 sub-step 1.1
#
# 본 fixture 는 기존 fail/ fixture 가 baseline 5 prefix (sk- / sk-ant- / ghp_ / AKIA / xoxb-) 만
# cover 하는 한계를 MVP-1 entry 시점 회귀 보강. Tier-1 prefix 31 中 6 vendor sample cover.
# 답습 변경 0건 — Tier-1 catalog 자동 확장 0건 (R-4.1 §4.1 답습 한정).
#
# fake canary 의무 답습 (사용자 명시 — F-금지 #1):
#   모든 fake secret 은 FAKE / NOTAREAL / fakecanary / R41T marker 포함.

# T1-002 (gho_ — GitHub OAuth access token)
GITHUB_OAUTH = "gho_FAKEMVP1ENTRYNOTAREALOAUTHXX"

# T1-006 (AIza — Google API key)
GOOGLE_API = "AIzaFAKEMVP1ENTRYNOTAREALGOOGLEKEY1234"

# T1-016 (hf_ — HuggingFace token)
HF_TOKEN = "hf_FAKEMVP1ENTRYNOTAREALHUGGINGFACE"

# T1-019 (pypi- — PyPI API token)
PYPI_TOKEN = "pypi-FAKEMVP1ENTRYNOTAREALPYPIAPI"

# T1-024 (tvly- — Tavily search API)
TAVILY = "tvly-FAKEMVP1ENTRYNOTAREALTAVILY"

# T1-026 (gsk_ — Groq Cloud API key)
GROQ = "gsk_FAKEMVP1ENTRYNOTAREALGROQCLOUD"
tests/fixtures/secret_hygiene/mvp1_s3/pass/clean.py
# S-3 detect-secrets PASS fixture — secret 0건 (false positive 0 evidence)
# 답습: docs/phase0/mvp1-s3-detect-secrets-partial-integration-brief.md §4.4

import os


def get_config():
    return {
        "timeout": 30,
        "retries": 3,
        "endpoint": os.environ.get("API_ENDPOINT", "http://localhost:8080"),
    }


def main():
    config = get_config()
    print(f"config loaded: {config}")


if __name__ == "__main__":
    main()
tests/fixtures/secret_hygiene/mvp1_s3/fail/base64_entropy.py
# S-3 detect-secrets FAIL fixture — Base64HighEntropyString plugin 검출 evidence
# 답습: docs/phase0/mvp1-s3-detect-secrets-partial-integration-brief.md §4.4
# fake canary 의무 — high entropy Base64 string (decoded = random bytes, not real secret)

# High entropy Base64 string (>4.5 bits/char) — Base64HighEntropyString 검출 대상
# 본 string = "0123456789abcdef..." 의 random base64 encoded, 실 secret 0
HIGH_ENTROPY_BASE64 = "Zk5xN3JZb1ZwUjVYbU5oQjJBdEdpc09qVEFmS3o0R3Q3Sg=="

# 추가 high entropy fixture
ANOTHER_BASE64 = "VGhpc0lzRkFLRVMzTm90QVJlYWxTZWNyZXRCYXNlNjRYWA=="
tests/fixtures/secret_hygiene/mvp1_s3/fail/private_key.py
# S-3 detect-secrets FAIL fixture — PrivateKeyDetector plugin 검출 evidence
# 답습: docs/phase0/mvp1-s3-detect-secrets-partial-integration-brief.md §4.4
# fake canary 의무 — fake private key marker (실 key material 0)

# RSA private key marker — PrivateKeyDetector 검출 대상 (-----BEGIN... marker)
FAKE_RSA_KEY = """-----BEGIN RSA PRIVATE KEY-----
FAKES3NOTREALPRIVATEKEYBASE64ENCODEDCONTENTHEREXXXXXXXXXXXXXXXX
FAKES3NOTREALPRIVATEKEYBASE64ENCODEDCONTENTHEREXXXXXXXXXXXXXXXX
-----END RSA PRIVATE KEY-----"""

# OpenSSH private key marker
FAKE_SSH_KEY = """-----BEGIN OPENSSH PRIVATE KEY-----
FAKES3NOTREALOPENSSHPRIVATEKEYCONTENTXXXXXXXXXXXXXXXXXXXXXXXXXX
-----END OPENSSH PRIVATE KEY-----"""
tests/fixtures/secret_hygiene/mvp1_s3/fail/hex_entropy.py
# S-3 detect-secrets FAIL fixture — HexHighEntropyString plugin 검출 evidence
# 답습: docs/phase0/mvp1-s3-detect-secrets-partial-integration-brief.md §4.4
# fake canary 의무 — high entropy Hex string (실 secret 0)

# High entropy Hex string (>3 bits/char) — HexHighEntropyString 검출 대상
# 본 string = random hex, 실 secret 0
HIGH_ENTROPY_HEX = "a3f5d8c2b9e7f1a4d6c8b5e2f9a1d4c7b3e6f8a2d5c9b4e1f7a8d3c6b9e2f5a1"

# 추가 high entropy hex fixture
ANOTHER_HEX = "fakes3notrealf1e2d3c4b5a69788776655443322110099887766554433221100"
tests/fixtures/secret_hygiene/mvp1_s3/fail/aws_key.py
# S-3 detect-secrets FAIL fixture — AWSKeyDetector plugin 검출 evidence
# 답습: docs/phase0/mvp1-s3-detect-secrets-partial-integration-brief.md §4.4
# fake canary 의무 — AKIA + 16자 (총 20자) marker (사용자 명시 답습)
#
# 수정 이력 (31번째 entry, 첫 PR evidence 수집 시점):
#   - v1 (4451716): "AKIAFAKES3NOTREAL01" (19자) + "ASIAFAKES3NOTREAL02" (19자, ASIA) → AWSKeyDetector regex 미충족 = check FAIL
#   - v2 (본 commit): "AKIA + 16자 정확 format" (총 20자) + ASIA 제거 (detect-secrets AWSKeyDetector regex `AKIA[0-9A-Z]{16}` 답습)

# AKIA prefix + 16자 [0-9A-Z] (총 20자) — AWSKeyDetector regex `AKIA[0-9A-Z]{16}` 정확 매치
AWS_ACCESS_KEY_ID = "AKIAFAKES3NOTREAL01X"  # 20자 (AKIA=4 + FAKES3NOTREAL01X=16)
AWS_ACCESS_KEY_ID_ALT = "AKIATESTNOTREAL02XYZ"  # 20자 (다른 fake canary, 동일 format)
tests/fixtures/secret_hygiene/mvp1_s3/fail/keyword.py
# S-3 detect-secrets FAIL fixture — KeywordDetector plugin 검출 evidence
# 답습: docs/phase0/mvp1-s3-detect-secrets-partial-integration-brief.md §4.4
# fake canary 의무 — FAKES3NOTAREAL marker

# api_key / password / token keyword assignment — KeywordDetector 검출 대상
api_key = "sk-FAKES3NOTAREALSECRETXX"
password = "FAKES3NOTAREALPASSWORDXX"
token = "FAKES3NOTAREALTOKENXX"
tests/fixtures/secret_hygiene/redaction_pass/env_redacted.txt
[INFO] config loaded
OPENAI_API_KEY=[REDACTED]
ANTHROPIC_API_KEY=[REDACTED]
GITHUB_TOKEN=[REDACTED]
AWS_ACCESS_KEY=[REDACTED]
Authorization: [REDACTED]
[INFO] all secrets masked, residual scan expected: 0 violations
tests/fixtures/secret_hygiene/fail/private_key_block.pem
-----BEGIN RSA PRIVATE KEY-----
fakekeydataR41T-fakecanary-D-not-real-not-a-real-private-key
this-block-is-a-poc-fixture-only-do-not-use-as-real-credential
-----END RSA PRIVATE KEY-----
tests/fixtures/secret_hygiene/fail/json_field.json
{
  "name": "fake-config",
  "api_key": "ghp_FAKE_GROUP_D_NOT_REAL_TOKEN",
  "redirect_url": "https://example.com/oauth/cb?access_token=fakecanaryR41T-NOTAREAL&state=x",
  "version": "0.1"
}
tests/fixtures/secret_hygiene/fail/env_assignment.py
# Group D PoC — D-1 FAIL fixture (prefix + regex H-A cover)
# 답습: 사양 §4.2
# fake canary 의무 — sk-FAKE-GROUP-D-NOT-A-REAL-SECRET (사용자 명시 답습)

OPENAI_API_KEY = "sk-FAKE-GROUP-D-NOT-A-REAL-SECRET"
ANTHROPIC_API_KEY = "sk-ant-FAKEGROUPDNOTAREALSECRETXX"
tests/fixtures/secret_hygiene/fail/prefix_aws.py
# Group D PoC — D-1 FAIL fixture (baseline prefix AKIA cover)
# 답습: 사양 §4.2 — fake canary AKIAFAKEGROUPDNOTREAL01 (16자, AKIA prefix 4 + canary marker 12)

AWS_ACCESS_KEY = "AKIAFAKEGROUPDNOTREAL01"
SLACK_BOT_TOKEN = "xoxb-FAKEGROUPDNOTREAL-not-a-real-token"

exec
/bin/bash -lc "nl -ba tools/secret_scanner.py | sed -n '260,460p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
   260	def iter_files(root: Path, allowed_exts: tuple[str, ...]) -> list[Path]:
   261	    """Recursively iter target files under root, filtered by extension."""
   262	    if root.is_file():
   263	        return [root] if root.suffix in allowed_exts else []
   264	    out: list[Path] = []
   265	    for p in sorted(root.rglob("*")):
   266	        if p.is_file() and p.suffix in allowed_exts:
   267	            out.append(p)
   268	    return out
   269	
   270	
   271	def scan_path(root: Path, mode: str) -> list[Violation]:
   272	    """Scan all matching files under root and return aggregated violations."""
   273	    if mode == "scan-source":
   274	        exts = SCAN_SOURCE_EXTENSIONS
   275	    elif mode == "scan-log":
   276	        exts = SCAN_LOG_EXTENSIONS
   277	    else:
   278	        raise ValueError(f"unknown mode: {mode!r}")
   279	
   280	    vios: list[Violation] = []
   281	    for file_path in iter_files(root, exts):
   282	        try:
   283	            text = file_path.read_text(encoding="utf-8", errors="replace")
   284	        except OSError as e:
   285	            print(f"READ_ERROR: {file_path}: {e}", file=sys.stderr)
   286	            continue
   287	        vios.extend(scan_text(text, file_path, mode=mode))
   288	    return vios
   289	
   290	
   291	def list_patterns() -> int:
   292	    """Print Tier-1 catalog summary (사용자 명시 검증 5 — Tier-1 pattern count 자기 검증)."""
   293	    n_baseline = len(BASELINE_PREFIX)
   294	    n_prefix = len(PREFIX_PATTERNS)
   295	    n_regex = len(REGEX_PATTERNS)
   296	    n_alt = len(ALTERNATION_PATTERNS)
   297	    total_registered = n_baseline + n_prefix + n_regex + n_alt
   298	    n_active = total_registered - len(SKIP_DIRECT_REGISTER & {p[0] for p in ALL_PATTERNS})
   299	
   300	    print(f"registered_patterns_count={total_registered}", file=sys.stderr)
   301	    print(f"  baseline_prefix={n_baseline}", file=sys.stderr)
   302	    print(f"  tier1_prefix={n_prefix}", file=sys.stderr)
   303	    print(f"  tier1_regex={n_regex}", file=sys.stderr)
   304	    print(f"  tier1_alternation={n_alt}", file=sys.stderr)
   305	    print(f"  skip_direct_register={sorted(SKIP_DIRECT_REGISTER)}", file=sys.stderr)
   306	    print(f"  active_patterns={n_active}", file=sys.stderr)
   307	    print(
   308	        f"  tier1_42_catalog_compliant={total_registered >= 42}", file=sys.stderr
   309	    )
   310	
   311	    for pid, src, cat, vendor, rgx in ALL_PATTERNS:
   312	        flag = " (skipped)" if pid in SKIP_DIRECT_REGISTER else ""
   313	        print(f"  {pid}\t{cat}\t{vendor}\t{src}{flag}", file=sys.stderr)
   314	
   315	    return 0
   316	
   317	
   318	def _cli() -> int:
   319	    p = argparse.ArgumentParser(
   320	        description="Secret scanner — Group D PoC (G2 GP-3 + GP-2, R-4.1 Tier-1 42 catalog 답습)"
   321	    )
   322	    p.add_argument(
   323	        "path", type=str, nargs="?", default=None,
   324	        help="대상 파일/디렉토리 경로 (재귀). --list-patterns 시 생략 가능."
   325	    )
   326	    p.add_argument(
   327	        "--mode", choices=("scan-source", "scan-log"), default=None,
   328	        help=(
   329	            "scan-source = code-side secret 검출 (D-1). "
   330	            "scan-log = redaction 후 잔존 secret 검출 (D-2)."
   331	        ),
   332	    )
   333	    p.add_argument(
   334	        "--list-patterns", action="store_true",
   335	        help="등록된 45 patterns enumerate + Tier-1 42 catalog count 자기 검증",
   336	    )
   337	    p.add_argument(
   338	        "--max-lines", type=int, default=20,
   339	        help="violation 출력 최대 라인 수 (default 20, CI log 폭주 방지)",
   340	    )
   341	    args = p.parse_args()
   342	
   343	    if args.list_patterns:
   344	        return list_patterns()
   345	
   346	    if not args.path or not args.mode:
   347	        print("ERROR: path 와 --mode 필수 (--list-patterns 단독 모드 외)", file=sys.stderr)
   348	        return 2
   349	
   350	    root = Path(args.path)
   351	    if not root.exists():
   352	        print(f"PATH_NOT_FOUND: {root}", file=sys.stderr)
   353	        return 2
   354	
   355	    vios = scan_path(root, args.mode)
   356	
   357	    if not vios:
   358	        print(f"[PASS] mode={args.mode} target={root} violations=0", file=sys.stderr)
   359	        return 0
   360	
   361	    print(
   362	        f"[FAIL] mode={args.mode} target={root} violations={len(vios)}",
   363	        file=sys.stderr,
   364	    )
   365	    seen_categories: set[str] = set()
   366	    for v in vios[: args.max_lines]:
   367	        seen_categories.add(v.pattern_category)
   368	        print(v.format_short(), file=sys.stderr)
   369	    if len(vios) > args.max_lines:
   370	        print(f"  ... and {len(vios) - args.max_lines} more", file=sys.stderr)
   371	    print(
   372	        f"  pattern_categories_cover={sorted(seen_categories)}", file=sys.stderr
   373	    )
   374	
   375	    return 1
   376	
   377	
   378	if __name__ == "__main__":
   379	    sys.exit(_cli())

exec
/bin/bash -lc "python tools/secret_scanner.py --list-patterns >/tmp/list.out 2>/tmp/list.err; printf 'rc=%s\\n' \""'$?"; sed -n '"'1,80p' /tmp/list.err" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
rc=127
/bin/bash: line 1: python: command not found

exec
/bin/bash -lc "python tools/secret_scanner.py --mode scan-log tests/fixtures/secret_hygiene/redaction_pass/ >/tmp/pass.out 2>/tmp/pass.err; printf 'pass_rc=%s\\n' \""'$?"; sed -n '"'1,80p' /tmp/pass.err; python tools/secret_scanner.py --mode scan-log tests/fixtures/secret_hygiene/redaction_fail/ >/tmp/fail.out 2>/tmp/fail.err; printf 'fail_rc=%s\\n' \""'$?"; sed -n '"'1,120p' /tmp/fail.err" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
pass_rc=127
/bin/bash: line 1: python: command not found
fail_rc=127
/bin/bash: line 1: python: command not found

codex
로컬 셸에는 `python` 명령이 없고 `python3`만 있을 가능성이 큽니다. GitHub Actions는 `setup-python` 후 `python` 별칭이 제공되는 환경이라 workflow 자체 결함으로 보지는 않고, 로컬 재현은 `python3`로 다시 돌립니다.
exec
/bin/bash -lc "python3 tools/secret_scanner.py --list-patterns >/tmp/list.out 2>/tmp/list.err; printf 'rc=%s\\n' \""'$?"; sed -n '"'1,80p' /tmp/list.err" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
rc=0
registered_patterns_count=45
  baseline_prefix=5
  tier1_prefix=31
  tier1_regex=7
  tier1_alternation=2
  skip_direct_register=['T1-038', 'T1-040']
  active_patterns=45
  tier1_42_catalog_compliant=True
  BL-1	prefix-baseline	Anthropic	Hermes #1 (sk-ant-)
  BL-2	prefix-baseline	OpenAI/Anthropic/etc	Hermes #1 (sk-)
  BL-3	prefix-baseline	GitHub PAT classic	Hermes #2
  BL-4	prefix-baseline	AWS Access Key ID	Hermes #15
  BL-5	prefix-baseline	Slack tokens	Hermes #8
  T1-001	prefix	GitHub PAT (fine-grained)	Hermes #3
  T1-002	prefix	GitHub OAuth access token	Hermes #4
  T1-003	prefix	GitHub user-to-server	Hermes #5
  T1-004	prefix	GitHub server-to-server	Hermes #6
  T1-005	prefix	GitHub refresh token	Hermes #7
  T1-006	prefix	Google API keys	Hermes #9
  T1-007	prefix	Perplexity	Hermes #10
  T1-008	prefix	Fal.ai	Hermes #11
  T1-009	prefix	Firecrawl	Hermes #12
  T1-010	prefix	BrowserBase	Hermes #13
  T1-011	prefix	Codex encrypted tokens	Hermes #14
  T1-012	prefix	Stripe secret key (live)	Hermes #16
  T1-013	prefix	Stripe secret key (test)	Hermes #17
  T1-014	prefix	Stripe restricted key	Hermes #18
  T1-015	prefix	SendGrid API key	Hermes #19
  T1-016	prefix	HuggingFace token	Hermes #20
  T1-017	prefix	Replicate API token	Hermes #21
  T1-018	prefix	npm access token	Hermes #22
  T1-019	prefix	PyPI API token	Hermes #23
  T1-020	prefix	DigitalOcean PAT	Hermes #24
  T1-021	prefix	DigitalOcean OAuth	Hermes #25
  T1-022	prefix	AgentMail API key	Hermes #26
  T1-023	prefix	ElevenLabs TTS key	Hermes #27
  T1-024	prefix	Tavily search API	Hermes #28
  T1-025	prefix	Exa search API	Hermes #29
  T1-026	prefix	Groq Cloud API key	Hermes #30
  T1-027	prefix	Matrix access token	Hermes #31
  T1-028	prefix	RetainDB API key	Hermes #32
  T1-029	prefix	Hindsight API key	Hermes #33
  T1-030	prefix	Mem0 Platform API key	Hermes #34
  T1-031	prefix	ByteRover API key	Hermes #35
  T1-032	regex	ENV assignment	Hermes H-A
  T1-033	regex	JSON field with secret keys	Hermes H-B
  T1-034	regex	Authorization header (Bearer)	Hermes H-C
  T1-035	regex	Private key block	Hermes H-E
  T1-036	regex	DB connstr password	Hermes H-F
  T1-037	regex	JWT token	Hermes H-G
  T1-039	regex	URL userinfo (non-DB)	Hermes H-K
  T1-041	alternation	URL query sensitive keys (16)	Hermes _SENSITIVE_QUERY_PARAMS
  T1-042	alternation	Body/form sensitive keys (14)	Hermes _SENSITIVE_BODY_KEYS

exec
/bin/bash -lc "python3 tools/secret_scanner.py --mode scan-log tests/fixtures/secret_hygiene/redaction_pass/ >/tmp/pass.out 2>/tmp/pass.err; printf 'pass_rc=%s\\n' \""'$?"; sed -n '"'1,80p' /tmp/pass.err; python3 tools/secret_scanner.py --mode scan-log tests/fixtures/secret_hygiene/redaction_fail/ >/tmp/fail.out 2>/tmp/fail.err; printf 'fail_rc=%s\\n' \""'$?"; sed -n '"'1,120p' /tmp/fail.err" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
pass_rc=0
[PASS] mode=scan-log target=tests/fixtures/secret_hygiene/redaction_pass violations=0
fail_rc=1
[FAIL] mode=scan-log target=tests/fixtures/secret_hygiene/redaction_fail violations=3
tests/fixtures/secret_hygiene/redaction_fail/partial_redact.txt:2:BL-2:prefix-baseline:OpenAI/Anthropic/etc: 'sk-FAKE-GROUP-D-NOT-A-REAL-SEC...'
tests/fixtures/secret_hygiene/redaction_fail/partial_redact.txt:2:T1-032:regex:ENV assignment: 'OPENAI_API_KEY=sk-FAKE-GROUP-D...'
tests/fixtures/secret_hygiene/redaction_fail/partial_redact.txt:4:T1-032:regex:ENV assignment: 'GITHUB_TOKEN=ghp_FAKE_GROUP_D_...'
  pattern_categories_cover=['prefix-baseline', 'regex']

exec
/bin/bash -lc 'gh run view 26517803107 --json conclusion,headSha,event,workflowName,createdAt,updatedAt,status,url' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 613ms:
{"conclusion":"success","createdAt":"2026-05-27T14:32:31Z","event":"push","headSha":"4fec64859831fb9bfade31819055070abd079244","status":"completed","updatedAt":"2026-05-27T14:38:11Z","url":"https://github.com/jokwangwon/AI_development_tool/actions/runs/26517803107","workflowName":"G2 GP-3 + GP-2 Secret Hygiene & Egress Redaction"}

exec
/bin/bash -lc 'git diff --name-status 4fec64859831fb9bfade31819055070abd079244 -- .github/workflows/secret-hygiene-egress-redaction.yml tools/secret_scanner.py tests/fixtures/secret_hygiene/redaction_pass tests/fixtures/secret_hygiene/redaction_fail' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
exec
/bin/bash -lc 'git status --short && git rev-parse --short HEAD && git log --oneline --decorate -8 -- .github/workflows/secret-hygiene-egress-redaction.yml tools/secret_scanner.py tests/fixtures/secret_hygiene/redaction_pass tests/fixtures/secret_hygiene/redaction_fail' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
?? docs/external-review/2026-05-28-mvp2-gp2-pass-codex-response.md
?? docs/phase0/mvp2-gp2-pass-activation-brief.md
0f49eb9
4fec648 chore(secret-scanner-scope-policy,architecture,pre-commit-config,session,index): 49번째 entry — (secret-scanner docs scope 정책 분리) sub-cycle (Reviewer-only 단축 APPROVE + 정책 문서 발효 + .pre-commit-config.yaml + secret_scanner.py 주석 cross-reference, 46/47 entry codex N-3 carry-over 해소)
ad5b875 chore(actions-nodejs-24,workflows,external-review,session,index): 47번째 entry — GitHub Actions Node.js 24 마이그레이션 sub-cycle (단축 + 외부 LLM 1+ cross-vendor REVISE-then-APPROVE + 12 workflow 31 위치 action version upgrade — checkout@v6 × 12 + setup-python@v6 × 11 + upload-artifact@v7 × 8)
d71f8a8 chore(b1-pc1-d6-fp-edge-extensions,secret-scanner,external-review,session,index): 46번째 entry — (b1-PC1-D6-fp-edge-extensions) semicolon + fragment delimiter 확장 sub-cycle (단축 + 외부 LLM 1+ cross-vendor APPROVE + Cookie semicolon + OAuth fragment cover + canary 4/4 PASS)
eb51284 (origin/main) MVP-1 1.5차 보강 (b1) 4 sub-cycle + AR-3 branch protection evidence (draft) (#2)
ffa0cbf feat(g2-gp3): add ST-2 evidence summary fields
ea22358 feat(g2-gp3): add ST-2 inotify sidecar CI entry step
155f1a9 feat(g2): adapt Stage 5 permissions assertion after K-2 fix
de727de feat(g2): add Stage 5 cycle 4 workflow permissions CI step

exec
/bin/bash -lc "test -e agent/redact.py; printf 'agent_redact_exists=%s\\n' \""'$?"; ls -la agent 2>/dev/null || true; nl -ba src/adapters/llm/facade.py | sed -n '"'1,220p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
agent_redact_exists=1
     1	"""LLMFacade — Provider-agnostic facade (G2 GP-5 placeholder).
     2	
     3	본 파일은 *유일하게* LiteLLM 직접 import 가 *허용되는 경로* 입니다 (§4.1 답습).
     4	현 시점은 **placeholder** — real 본문 작성 시 자동 풀 3+1 합의 trigger TR-1 발화.
     5	
     6	답습 출처:
     7	  - docs/architecture/llm-providers-design.md §4.1 (정확히 이 파일만 LiteLLM 직접 import)
     8	  - docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md §2.3 (Hermes PMO ↔ provider 영구 권위)
     9	  - docs/review/3plus1-consensus-2026-05-10-g2-gp5-poc2-depcruise-full.md §5.4 TR-1
    10	  - docs/phase0/g2-gp5-poc2-depcruise-rule-scope.md §2.1
    11	"""
    12	from __future__ import annotations
    13	
    14	from dataclasses import dataclass
    15	from typing import Any
    16	
    17	
    18	@dataclass(frozen=True)
    19	class LLMRequest:
    20	    alias: str
    21	    messages: list[dict[str, str]]
    22	    metadata: dict[str, Any] | None = None
    23	
    24	
    25	@dataclass(frozen=True)
    26	class LLMResponse:
    27	    content: str
    28	    metadata: dict[str, Any]
    29	
    30	
    31	class LLMFacade:
    32	    """Placeholder — real LiteLLM import + Router 위임은 TR-1 발화 시 작성."""
    33	
    34	    def __init__(self, registry_path: str) -> None:
    35	        self._registry_path = registry_path
    36	
    37	    def complete(self, request: LLMRequest) -> LLMResponse:
    38	        raise NotImplementedError("Placeholder — TR-1 풀 3+1 합의 후 real 본문 작성")
    39	
    40	    async def health(self) -> dict[str, bool]:
    41	        return {}

codex
`gh run`은 실제로 success, headSha `4fec6485`입니다. 또한 현재 HEAD `0f49eb9`와 해당 run SHA 사이에 D-2 workflow/scanner/redaction fixture diff가 없어 “최근 green run이 현 코드에 적용된다”는 주장은 증거상 성립합니다.
exec
/bin/bash -lc "nl -ba docs/decisions/ADR-011-means-vs-ends-redaction.md | sed -n '45,125p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
    45	
    46	### 2.1 수단/목적 분리 원칙 (Means-vs-Ends Separation)
    47	
    48	**비협상 조건의 본질은 특정 구현 수단이 아니라, 달성해야 하는 안전 결과(safety outcome)이다.**
    49	
    50	- 헌법 제8조 (보안)의 본질은 **DB 평문 저장 차단이라는 결과**이다.
    51	- 외부 hook, redaction 호출, trigger, 암호화 등은 **수단**이다.
    52	- 대체 수단은 다음 4조건을 **모두** 충족할 때 기존 수단을 대체할 수 있다:
    53	
    54	  | # | 조건 | 검증 방식 |
    55	  |---|------|---------|
    56	  | (a) | 동등 이상의 보안 결과 | 명시적 비교표 (수단 A 보장 ↔ 수단 B 보장) |
    57	  | (b) | 격리 환경 PoC로 실증 | Docker isolation + 자동 검증 항목 |
    58	  | (c) | ADR 권위로 명시 | 본 ADR 또는 후속 ADR |
    59	  | (d) | 자동 회귀 검증 경로 확보 | CI/nightly 재실행 (R-6) |
    60	
    61	**원칙 위반**: "수단이 비협상이다"는 텍스트 해석으로 본질 회귀를 차단하는 것은 본 ADR로 무효화된다. 동시에 (a)~(d) 4조건 미충족 시 수단 대체도 금지된다 — 본 ADR은 *수단 자유*가 아니라 *목적 달성 검증 의무*를 강제한다.
    62	
    63	### 2.2 G1a / G1b 게이트 분리 공식화
    64	
    65	P2 v2의 단일 G1 게이트는 본 ADR로 다음 두 게이트로 분해된다.
    66	
    67	```
    68	G1a: Hermes native redaction applies before DB INSERT
    69	   Result: FAIL (R-1 확정)
    70	   Evidence: agent/redact.py docstring "for logs and tool output",
    71	             redact import 25개 모두 비-DB,
    72	             hermes_state.py redact import 0건
    73	   Status: 폐기 (이 경로로 헌법 8조 충족 시도 금지)
    74	
    75	G1b: DB-level fallback prevents plaintext secret persistence
    76	   Result: PASS by R-2 PoC
    77	   Evidence: Docker 격리 환경 (network_mode: none + read_only + cap_drop ALL)
    78	             + SQLCipher BEFORE INSERT trigger + REGEXP UDF
    79	             + 6항목 자동 검증 (C1~C6 모두 PASS)
    80	   Status: PoC PASS, 정식 충족은 R-3~R-5 완료 후
    81	```
    82	
    83	#### G1b 정식 충족 조건 (Phase 1 차단조건 #1 exit 기준)
    84	
    85	| # | 조건 | 산출 |
    86	|---|------|------|
    87	| R-3 | 본 ADR-011 발행 + ADR-008 Amendment | `ADR-011`, `ADR-008` 부록 B |
    88	| R-4 | Hermes redact pattern ↔ P1_REDACTOR 패턴 동등성 검증, gap 발견 시 trigger UDF 보충 | `docs/architecture/redaction-pattern-equivalence.md` |
    89	| R-5 | canary 재검증 트리거 설계 (T13 강화 — config + 주기적 inject) | `docs/architecture/canary-recheck-design.md` |
    90	| R-6 | CI/nightly 회귀 검증 (Hermes 업그레이드 자동 R-2 재실행) | `.github/workflows/r2-canary.yml` |
    91	| R-7 | Phase 1 합격 SOP (canary 패턴/주입/검증/PASS·FAIL 기준) | `docs/phase0/redaction-verification-sop.md` |
    92	
    93	R-3~R-7 모두 완료 시 G1b는 PoC 단계를 벗어나 Phase 1 차단조건 #1 정식 exit 기준이 된다.
    94	
    95	### 2.3 Hermes ≠ Root of Trust
    96	
    97	**Hermes는 시스템의 최종 신뢰 근거가 아니라 검증 대상이다.**
    98	
    99	#### 권위 위계 (Authority Hierarchy)
   100	
   101	```
   102	Constitution
   103	  > ADR
   104	  > SDD
   105	  > Harness Gates
   106	  > Hermes
   107	  > Worker Agents
   108	```
   109	
   110	#### 운영 함의 (Operational Implications)
   111	
   112	1. **Hermes 출력은 Tools로 검증된다**: 린터/타입체커/테스트/trigger/canary가 Hermes 출력 위에 위치한다.
   113	2. **Hermes 자체 redaction은 로그/LLM 송신 방어로만 신뢰**: 저장 경로(DB/파일) 차단 책임 없음.
   114	3. **DB INSERT 경로는 Hermes 외부에서 별도 보호**: SQLCipher trigger 기반 fallback (G1b).
   115	4. **Hermes 의존성 업그레이드는 자동 R-2 재실행으로 회귀 검증**: 신뢰 경계 외부 변경의 자동 검출 (R-6).
   116	5. **Hermes 학습 결과의 자동 정책 반영 금지**: §2.4와 결합.
   117	
   118	#### prequel과의 관계
   119	
   120	본 §2.3은 `docs/architecture/system-identity-prequel.md` §3 ("Hermes ≠ root of trust") 의 prequel(임시) 선언을 ADR 영구 권위로 승격한다. prequel은 R-7 완료 후 P2 v3로 흡수되며 폐기되지만, 본 ADR-011 §2.3은 영구 유지된다.
   121	
   122	### 2.4 자동 학습과 자동 정책 변경 분리
   123	
   124	- **자동 학습은 허용**: Worker Agent가 도구 사용/패턴/실패 사례를 누적 학습하는 것은 시스템 가치의 핵심.
   125	- **자동 정책 변경은 금지**: Constitution / ADR / Harness Gates / Hermes 설정의 변경은 사용자 승인 경로(3+1 합의 또는 단축 합의)를 거쳐야 한다.

exec
/bin/bash -lc "nl -ba docs/decisions/ADR-012-evidence-ledger-protection.md | sed -n '1,170p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# ADR-012: Evidence Ledger Protection (Evidence Ledger 보호 강화)
     2	
     3	**상태**: 승인 (풀 3+1 + 외부 LLM 2건 — 2026-05-09)
     4	**날짜**: 2026-05-09
     5	**의사결정자**: 사용자 + Reviewer 종합 합의 — `docs/review/3plus1-consensus-2026-05-09-pr2-evidence-ledger.md`
     6	**상위 권위**: 헌법 제8조 (보안), 헌법 제5조 (Provider Liquidity, 관용), ADR-011 §2.1 (수단/목적 분리), §2.3 (Hermes ≠ root of trust), §2.4 (T1/T2/T3)
     7	**모법 ADR**: ADR-011 (Means-vs-Ends Redaction Principle)
     8	**갱신 대상**: G4 §4.2 schema (10 → 11 필드), G4 §4.4 hash chain 사양 보강, G4 §4.6 round-trip 검증 절차 보강 (동일 PR — `provider-agnostic-memory-skill-design.md`)
     9	**P10 트리거**: 본 ADR-012 발행 시점 = G2 §1.2.5 P10 (Evidence Forgery) 정식 등록 *트리거* (정식 row 추가는 별도 G2 update PR — 본 ADR 범위 외)
    10	**합의 권위**: `docs/review/3plus1-consensus-2026-05-09-pr2-evidence-ledger.md` (5/5 입력 APPROVE WITH CONDITIONS — Agent A/B/C + cross-vendor 외부 LLM + Claude 인접 컨텍스트)
    11	
    12	**[Cross-reference Block — (g1-N-3-adr-008+sip+adr-012') R-7 (f) cross-ref block 만 채택 + R-S4 답습 + R-1 (P4) 신설 *기각* 답습]**: 본 ADR-012 line 6 (상위 권위) + line 61 (§1.4 cross-ref 표 cell) + line 579 (영구 핵심 제약 표) + line 665 (관련 문서) 표기 "헌법 제5조 (Provider Liquidity, 관용)" / "헌법 제5조 관용" / "헌법 5조 (관용)" = (g1-N-1) commit `148fbbe` 후 **헌법 제5조-2: Provider Liquidity 원칙 (비협상) (line 75~80)** 직접 모법 발효 — (g1-N-1) 이전 관용 표현 답습. **line 61 = (P2) cross-ref 표 cell 처리** ((P4) 신규 verbatim 유형 신설 *기각* — R-1 + 기각-2 답습, Reviewer 권한 한계 (11) sub-boundary 신설 *기각*). 본 cycle = gov §1.1 line 78 verbatim 명문 4 source *외* 추가 동형 source 자격 식별 (R-S4 HIGH, ADR-012 = 명문 4 source 외 추가 동형 매핑 자격 강함). (g1-N-3-pamsd) `ab96e30` 동형 패턴 답습, **본문 verbatim 변경 0건** ((f) cross-ref block 만 채택). 정정 후 형식 = ADR-011 line 245 모법 "제5조-2 관용 (Provider Liquidity, 비협상)" (R-rec-3 답습 + 사용자 명시 직접 확인). 추가 위치 line 62/455/513/552/555/561/583/597 (P2 ADR-011 cross-ref + P3 "Provider Liquidity 4-way → 5-way" 본문 다수) = (P3) 본문 답습 본질 동형, 정정 자격 약함 ((P3) 약식 통일 cycle DEFER carry-over). 본 cycle 합의 = `209f04d`.
    13	
    14	---
    15	
    16	## 1. 맥락 (Context)
    17	
    18	### 1.1 본 ADR 발행 트리거 (prequel §6.4 재해석)
    19	
    20	`docs/architecture/system-identity-prequel.md` §6.4 는 "Phase 1 종료 시점에 Evidence Ledger schema 의 ADR 권위화" 를 명시했다. **본 ADR-012 는 그 트리거를 *4 게이트 Design/Governance PASS + PR-1/PR-2 묶음 안정화 시점* 으로 재해석하여 발행** (합의 보고서 §5.2 Agent C C-1 답습).
    21	
    22	재해석 사유:
    23	- Phase 1 acceptance PASS = 2026-05-07 (G1b PASS, R-7 SOP §7.3 단축 합의)
    24	- G2 / G3 / G4 Design/Governance Gate PASS (Bundled) = 2026-05-09
    25	- PR-1 6건 본문 흡수 완료 = 2026-05-09 후속 2 (`commit 750faaf`)
    26	- 본 PR-2 = G2/G3/G4 정식 PASS 합의 §11.2 P1 조건 흡수 (C-C + C-G) — **권위 내부 작업**
    27	
    28	### 1.2 G3 "Evidence decides" 운영 규칙의 근거 강화 필요성
    29	
    30	`docs/architecture/hermes-not-root-of-trust-runtime.md` §5 Evidence 결정 5 운영 규칙:
    31	
    32	```
    33	Agent proposes.       (제안)
    34	Hermes orchestrates.  (조율 — 격상 후)
    35	Tools verify.         (검증 — 계산적 우선)
    36	Evidence decides.     (결정 — 기록 없으면 PASS 미성립)
    37	Human overrides.      (사람이 최종 방향)
    38	```
    39	
    40	**PASS 성립 4 요건** (G3 §5.3):
    41	- (i) Tools 검증
    42	- (ii) **Evidence Ledger entry** ← 본 ADR-012 보호 강화 대상
    43	- (iii) (T2/T3) 사용자 명시 승인
    44	- (iv) (해당 시) 합의 보고서 commit
    45	
    46	Evidence Ledger 변조 가능성 = G3 root-of-trust 직접 훼손 → 본 ADR 권위로 보호.
    47	
    48	### 1.3 G2 §1.2.5 P10 (Evidence Forgery) 정식 등록 트리거 명시
    49	
    50	PR-1 §1.4 (C-I 흡수, `commit 750faaf`) 에서 G2 §1.2.5 P9~P12 deferred candidates 4건 등록:
    51	- P9 (Prompt Injection)
    52	- **P10 (Evidence Forgery)** ← **본 ADR-012 발행 시점 = 정식 등록 트리거** (G2 §1.2.5.2 명시)
    53	- P11 (Supply-chain)
    54	- P12 (Memory Poisoning Side-channel)
    55	
    56	본 ADR-012 발행은 P10 의 *정식 위반 경로 등록 트리거*. 단 **G2 §1.2 본문 P10 row 추가는 별도 G2 update PR** (본 ADR 범위 외, 합의 §4.2 답습).
    57	
    58	### 1.4 Cross-reference (헌법 + ADR + G + 5 영구 핵심 제약)
    59	
    60	| 연결 대상 | 연결 사유 |
    61	|--------|--------|
    62	| **헌법 제8조 (보안)** | Evidence Ledger entry 자체에 평문 secret 포함 가능 (P1 변종) — GP-1 SQLCipher trigger 보호 범위에 ledger DB 명시 포함 의무 (외부 LLM 2 C-1) |
    63	| **헌법 제5조 관용 (Provider Liquidity)** | Ledger 형식 = Hermes 의존 0 (ADR-008 차단조건 #2 답습) + provider-neutral 강제 (Provider Liquidity 4-way Multi-layer Defense → **5-way** Evidence 형식 layer 추가) |
    64	| **ADR-011 §2.1 (수단/목적 분리)** | 본 ADR 자체가 Evidence 무결성 = 목적, hash chain + signed/append commit + JCS = 수단. (a)~(d) + (e) 5조건 답습 (§4) |
    65	| **ADR-011 §2.3 (Hermes ≠ root of trust)** | Hermes 는 ledger entry 생성 가능 (T1 자동 학습), 단 promotion / approval 은 사용자 명시 (T2). Hash chain + signed/append commit = Hermes 변조 차단 운영 매커니즘. **본 ADR-012 는 Hermes 안전성을 선언하지 않는다** (ADR-011 §7.3 직접 답습 — 외부 LLM 2 C-15 / Agent B Gap-18) |
    66	| **ADR-011 §2.4 (T1/T2/T3)** | prev_hash 검증 실패 자동 revert = T3 위반 위험 → BLOCK + manual review 채택 (외부 LLM 2 C-3 / Agent B C-3) |
    67	| **ADR-008 차단조건 #2** | JSONL export 표준 — 본 ADR §2.10 흡수 |
    68	| **ADR-010 (SQLCipher Vault)** | secret 처리 cross-reference — Evidence Ledger DB 가 secret 포함 가능 시 GP-1 보호 범위 명시 의무 |
    69	| **G3 §1.3 + §5.3** | Evidence 결정 5 운영 규칙 + PASS 성립 4 요건 |
    70	| **G4 §4.4 + §4.6** | Hash chain + canonical JSON + round-trip 검증 (본 ADR §2.3 + §2.5 + §2.7 + §2.8 + §2.9 와 동시 보강) |
    71	| **system-identity-prequel §6.3** | Evidence Ledger schema 후보 권위 근거 — 본 ADR §2.2 답습 |
    72	
    73	### 1.5 메타포 회피 명시 (외부 LLM 2 §1)
    74	
    75	본 ADR-012 는 *형식적 무결성* (hash chain / canonical / append-only / signed) 까지만 보호. *의미적 정확성* (예: 사용자가 위조된 사실을 본인이 작성한 것처럼 ledger 에 기록) 은 본 ADR 방어 범위 외 (§11 한계 명시 답습). "Ledger 를 *불변의 진리* 로 비유" 같은 메타포 회피 — `system-identity-prequel §7` 답습.
    76	
    77	---
    78	
    79	## 2. 결정 (Decision)
    80	
    81	본 ADR-012 는 다음 12 보호 원칙 + 4 매트릭스 항목 + 5 추가 의무 을 권위로 선언한다.
    82	
    83	### 2.1 Evidence Ledger 보호 원칙 (12)
    84	
    85	**원칙 1**: Evidence Ledger 는 PASS 의 *보조 기록* 이 아니라 **PASS 성립 조건** 이다.
    86	
    87	**원칙 2**: Evidence 가 없으면 PASS 는 *존재하지 않는다*.
    88	
    89	**원칙 3**: Evidence Ledger 는 Hermes 가 *승인하거나 수정* 할 수 없다 (T3 영역).
    90	
    91	**원칙 4**: Evidence Ledger 의 변조 가능성은 G3 root-of-trust 구조를 직접 훼손한다.
    92	
    93	**원칙 5**: Evidence Ledger 는 *Hermes 의존 0* — 모든 entry 가 표준 도구 (`jq` + `sha256sum` + 표준 라이브러리) 만으로 검증 가능 (ADR-008 차단조건 #2 답습).
    94	
    95	**원칙 6**: Evidence Ledger entry 작성 주체는 `agent` 필드로 *provider-neutral* 식별 — `user` / `<worker_name>` / `hermes` 등.
    96	
    97	**원칙 7**: External LLM response 적재 시 entry `agent = "user"` (수동 paste 주체) 강제 (외부 LLM 2 C-9). Hermes 가 외부 LLM response 를 자기 제안으로 위조 차단 (Gap-17 #4).
    98	
    99	**원칙 8**: Evidence Ledger 는 *append-only* — entry 수정 / 삭제 / 재작성 금지 (T3 영역, ADR-011 §2.4).
   100	
   101	**원칙 9**: Hash chain 검증 실패 = 즉시 BLOCK. 자동 복구 / 자동 revert 금지 (T3 위반 위험 답습).
   102	
   103	**원칙 10**: Round-trip 검증은 tier-based — T2 (로컬 promotion) strict / T3 (cross-vendor migration) 의미 보존 + 사용자 명시 review (§2.9 답습).
   104	
   105	**원칙 11**: Evidence Ledger 보호 범위 = *형식적 무결성* — *의미적 정확성* (content-level forgery) 은 본 ADR 방어 범위 외 (§11 답습).
   106	
   107	**원칙 12**: 1인 동일 호스트 SPOF 한계 인지 (G3 §5.5 답습) — 동일 호스트 전체 침해는 본 ADR 의 완전 방어 범위 밖. multi-host 전환 시 Layer 3 / Layer 5 의무 발동 트리거.
   108	
   109	### 2.2 11 필드 구조 (G4 §4.2 schema 갱신, 10 → 11 필드)
   110	
   111	```jsonl
   112	{
   113	  "type": "memory|skill|meta",
   114	  "scope": "global|project|session|team",
   115	  "id": "<uuid-v4-or-slug>",
   116	  "schema_version": "0.2",
   117	  "ts": "2026-05-09T10:00:00Z",
   118	  "agent": "user|<worker_name>|hermes",
   119	  "event": "<event-enum>",
   120	  "content": {...},
   121	  "evidence_refs": ["docs/evidence/<path>.md"],
   122	  "prev_hash": "<sha256>",
   123	  "hash": "<sha256>"
   124	}
   125	```
   126	
   127	**11번째 필드 = `event`** (4/5 합의, Agent A enumeration 결과적 일치 — 합의 §3.1).
   128	
   129	**`event` enum 후보 (25건, MVP 의무 12건 + 후속 확장 5건 + MVP-1 신규 8건 — schema_version 0.2)**:
   130	
   131	| # | enum | 정체성 | T 분류 |
   132	|---|------|------|------|
   133	| 1 | `memory_write` | Memory entry 작성 | T1 (Hermes) / T2 (사용자 promotion) |
   134	| 2 | `skill_proposed` | Skill 후보 추출 | T1 (Hermes 자동) |
   135	| 3 | `skill_approved` | Skill `proposed` → `approved` | T2 (사용자 명시) |
   136	| 4 | `skill_promoted` | Skill `approved` → `promoted` | T2 + Evidence |
   137	| 5 | `skill_revoked` | Skill `promoted` → `revoked` | T3 자동 안전 (rollback_trigger) |
   138	| 6 | `gate_pass` | Gate (G1b/G2/G3/G4 등) PASS 선언 | T2 사용자 명시 |
   139	| 7 | `gate_fail` | Gate FAIL 선언 | T2 사용자 명시 |
   140	| 8 | `external_llm_received` | External LLM response 적재 | **T2 + agent="user" 강제** (원칙 7) |
   141	| 9 | `evidence_forgery_detected` | P10 위반 검출 | T3 BLOCK |
   142	| 10 | `roundtrip_pass` | Round-trip hash 일치 | T1 자동 |
   143	| 11 | `roundtrip_lossy` | Round-trip 의미 보존 (lossy) | T3 사용자 review |
   144	| 12 | `roundtrip_fail` | Round-trip 정책/권한/증거 손실 | T3 BLOCK |
   145	| 13 | `migration_failed` | Migration 검증 실패 (Agent A 권고) | T3 BLOCK + manual |
   146	| 14 | `chain_violation_detected` | prev_hash mismatch 또는 hash 재계산 검출 (외부 LLM 2 C-3) | T3 BLOCK + manual |
   147	| 15 | `hash_chain_broken` | Hash chain 자체 단절 (외부 LLM 1) | T3 BLOCK |
   148	| 16 | `policy_change_attempted` | Hermes 가 정책 변경 시도 (T3 위반) | T3 BLOCK + audit |
   149	| 17 | `canonical_json_fallback` | Canonical JSON `jq -S -c` fallback 사용 | T1 audit |
   150	| 18 | `secret_scan_layer1_implementation` | Secret scan Layer 1 구현 ledger (MVP-1 Stage 1, GP-3 S-1) | T1 audit |
   151	| 19 | `docker_secret_isolation_layer1_implementation` | Docker secret 격리 Layer 1 구현 ledger (MVP-1 Stage 2, GP-3 ST-3) | T1 audit |
   152	| 20 | `provider_adapter_enforcement_layer1_static` | Provider adapter Layer 1 static 검출 ledger (MVP-1 Stage 3, GP-5 T-6) | T1 audit |
   153	| 21 | `pc3_ar1_integration_implementation` | pre-commit + auto-revert 통합 구현 ledger (MVP-1 Stage 4) | T1 audit |
   154	| 22 | `g3_7_workflow_hygiene_implementation` | Workflow hygiene 4 항목 구현 ledger (MVP-1 Stage 5, G3-7) | T1 audit |
   155	| 23 | `provider_key_adapter_bypass_risk_detected` | Provider lock-in 위반 detect (MVP-1 IR-1) | T2 사용자 review |
   156	| 24 | `direct_sdk_with_secret_leakage_detected` | Direct SDK + secret 검출 (MVP-1 IR-2) | T3 BLOCK + manual |
   157	| 25 | `secret_handling_environment_mismatch_detected` | 환경 secret mismatch detect (MVP-1 IR-3) | T2 사용자 review |
   158	
   159	**MVP 의무 12 enum** (1~12, schema_version 0.1 도입). **후속 확장 5 enum** (13~17, schema_version 0.2 진입). **MVP-1 신규 8 enum** (18~25, schema_version 0.2 정식 등록 — Backlog #5 합의 `docs/review/3plus1-consensus-2026-05-13-adr-012-event-enum-registration.md` 권위, MVP-1 PASS §C-2 충족).
   160	
   161	**Provider-neutral 강제** (Agent B C-16): 11 필드 모두 provider-specific 식별자 미허용.
   162	
   163	### 2.3 Append-only 원칙 + Hash Chain (다층 강제)
   164	
   165	**Layer 1 — Hash Chain (MANDATORY 모든 환경)**:
   166	- `prev_hash` = 직전 entry 의 `hash` (chain 형성)
   167	- `hash` = 본 entry 의 canonical JSON sha256
   168	- 첫 entry 의 `prev_hash` = `genesis_hash` (§2.6)
   169	- SHA-256 hardcode (schema_version 0.1) — `hash_algo` 필드 후속 격상 영역 (§3.2 답습)
   170	

exec
/bin/bash -lc "nl -ba docs/architecture/governance-preconditions.md | sed -n '410,485p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
   410	
   411	### 3.7 의존 ADR / 갱신 후보
   412	
   413	- ADR-011 §2.1: 본문 변경 없음, §8.5 후속 작업에 G2 GP-1 흡수 등록 (G2 PASS 시점)
   414	- ADR-008 부록 B: 본문 변경 없음, B.6 결과를 G2 GP-1 cross-reference 추가 (G2 PASS 시점)
   415	
   416	---
   417	
   418	## 4. GP-2 — Egress Redaction (로그/LLM 송신)
   419	
   420	### 4.1 정의
   421	
   422	Hermes / Worker Agent 가 stdout / stderr / log file / LLM API request body 에 secret 을 노출하지 않도록 native redaction (`agent/redact.py`) + LLM facade redaction filter (P1 v2 §8.2) 가 사전 차단한다.
   423	
   424	**중요**: GP-2 는 ADR-011 §2.3 운영 함의 #2 의 *보조* 역할. **DB INSERT 차단은 GP-1 의 책임이며, GP-2 는 송신/로그 경로만 다룸**. GP-2 단독으로 헌법 8조 본질 충족 시도 금지.
   425	
   426	### 4.2 위반 경로
   427	
   428	- **P2** — 로그/LLM 송신 경로 평문 노출
   429	
   430	### 4.3 강제 메커니즘
   431	
   432	| 분류 | 메커니즘 | 위치 |
   433	|-----|---------|-----|
   434	| 계산적 | Hermes native redaction `agent/redact.py` (Tier-1 catalog 적용) | Hermes container |
   435	| 계산적 | P1 v2 LLM facade RedactionFilter | P1 facade layer |
   436	| 계산적 | base64 evasion test (R2-6) | `tests/hermes/redaction/test_base64_evasion.py` |
   437	| 계산적 | log file grep canary 자동 검증 | CI step (R-6 확장) |
   438	| 자동 회귀 | Hermes 의존성 업그레이드 시 R-2 / R-4.1 PoC 자동 재실행 (ADR-011 §2.3 운영 함의 #4) | R-6 workflow trigger 확장 |
   439	| 자동 롤백 | R-7 SOP §5 ROLLBACK trigger R5 (Hermes 학습 평문 검출) | R-7 SOP |
   440	
   441	### 4.4 Entry 기준
   442	
   443	- ✅ R-4 pattern equivalence 작성 완료 (충족됨)
   444	- ✅ Hermes native redaction `agent/redact.py` 존재 확인 (R-1 Day 2 evidence)
   445	- ⏳ 사용자 명시 GP-2 작업 진입 결정
   446	
   447	### 4.5 Exit 기준
   448	
   449	| # | 조건 | 검증 방식 |
   450	|---|------|---------|
   451	| (a) | 동등 이상의 보안 결과 | Hermes native redaction Tier-1 42 catalog 적용 검증 + P1 facade redaction filter 검증 |
   452	| (b) | 격리 환경 PoC 실증 | log file canary inject + grep 검증 PoC (Docker 격리) |
   453	| (c) | ADR / SDD 권위 명시 | ADR-011 §2.3 운영 함의 #2 cross-reference + 본 §4 권위 |
   454	| (d) | 자동 회귀 검증 경로 확보 | R-6 workflow 에 log file canary inject step 추가 |
   455	| (e) | 합의 APPROVE | 단축 또는 풀 3+1 합의 (G2 GP-2 한정 또는 G2 통합) |
   456	
   457	### 4.6 산출 후보
   458	
   459	- `tests/hermes/redaction/test_log_canary.py` (log file inject + grep)
   460	- R-6 workflow 확장 — log file canary inject step
   461	- 합의 보고서
   462	
   463	### 4.7 의존 ADR / 갱신 후보
   464	
   465	- ADR-011 §2.3: 본문 변경 없음, §8.5 후속 작업에 GP-2 산출 등록 (G2 PASS 시점)
   466	- ADR-008 차단조건 #1 보조 메커니즘 cross-reference
   467	
   468	---
   469	
   470	## 5. GP-3 — Credential / Secret Hygiene (저장 + 코드)
   471	
   472	### 5.1 정의
   473	
   474	API 키 / OAuth credentials 의 *저장 경로* (런타임) 와 *코드 본문* (개발/배포 시점) 양쪽에서 secret 노출이 차단된다.
   475	
   476	- **저장 경로** (P3): docker secret + chmod 600 + entrypoint stat 검증 + inotify 런타임 감시
   477	- **코드 본문** (P4): pre-commit hook (gitleaks / detect-secrets) + CI step + PR auto-reject
   478	
   479	### 5.2 위반 경로
   480	
   481	- **P3** — Credential / OAuth 파일 권한 노출
   482	- **P4** — 비밀값 하드코딩
   483	
   484	### 5.3 강제 메커니즘
   485	

exec
/bin/bash -lc "nl -ba docs/architecture/redaction-pattern-equivalence.md | sed -n '1,180p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# Redaction Pattern Equivalence (R-4)
     2	
     3	> **ADR-011 §2.1 (a) "동등 이상 보장" 검증 의무의 직접 충족 작업 — 코드 변경 없는 패턴 비교 + gap 식별 + 보충 권고 문서화**
     4	
     5	**상태**: 작성 (R-4 단축 검증 — 코드 수정 미포함)
     6	**날짜**: 2026-05-06
     7	**상위 권위**: ADR-011 §2.1 (a) (대체 수단 동등 이상 보장 검증 의무), §3 R-4 매핑
     8	**모법 ADR**: `docs/decisions/ADR-011-means-vs-ends-redaction.md`
     9	**갱신 대상**: ADR-008 부록 B B.6 R-4 항목 ⏳ → 본 문서 발행 시 ✅
    10	**산출 의도**: trigger UDF 보충 권고 카탈로그 — 실제 보충 코드 작성은 별도 작업 (보충 자체도 ADR-011 §2.1 (a)~(d) 4조건 적용 대상)
    11	
    12	---
    13	
    14	## 1. 작업 정의
    15	
    16	### 1.1 본 R-4의 본질 (사용자 명시)
    17	
    18	> **이번 단계의 핵심은 "코드 수정"이 아니라 "패턴 추출 → 비교 → gap 식별 → 보충 권고 문서화"이다.**
    19	
    20	본 문서는 다음 4단계를 산출한다:
    21	
    22	| # | 단계 | 산출 §  |
    23	|---|------|--------|
    24	| 1 | **추출** — Hermes / P1_REDACTOR / R-2 trigger UDF 패턴 카탈로그 | §2 / §3 / §4 |
    25	| 2 | **비교** — 3-way 동등성 매트릭스 | §5 |
    26	| 3 | **gap 식별** — Tier 1/2/3 분류 | §6 |
    27	| 4 | **보충 권고** — trigger UDF 확장 카탈로그 (코드 미작성) | §7 |
    28	
    29	### 1.2 ADR-011 §2.1 (a) 충족 의무
    30	
    31	> **(a) 동등 이상의 보안 결과 — 명시적 비교표 (수단 A 보장 ↔ 수단 B 보장)**
    32	
    33	본 문서 §5의 3-way 비교표가 (a) 직접 충족 산출이다. 본 문서는 보안 결과를 *선언*하지 않으며, 비교 사실과 gap을 *기록*한다 — gap이 미보충 상태에서 G1b 정식 충족 (ADR-008 부록 B.6) 진입 불가.
    34	
    35	### 1.3 본 문서가 *하지 않는* 것
    36	
    37	- ❌ trigger UDF 패턴 코드 수정 — 본 문서는 *권고 카탈로그*이며 보충 작업은 별도 작업으로 분리 (ADR-011 §2.1 (b) "격리 환경 PoC 실증" 의무 별도 적용)
    38	- ❌ Hermes redaction 우회 가능성 평가 — base64 우회 등은 R-2 PoC §6 향후 검증 항목 + R-7 SOP 영역
    39	- ❌ Hermes 안전성 선언 — ADR-011 §7.3 "본 ADR은 Hermes 안전성을 선언하지 않는다" 위반 금지
    40	- ❌ P1_REDACTOR ↔ R-2 trigger UDF 직접 비교의 우선시 — P1_REDACTOR는 P1 facade 호출 경로 한정 (LiteLLM callback). DB INSERT 차단의 기준선은 Hermes 패턴 카탈로그 (광역 수단)
    41	
    42	---
    43	
    44	## 2. Hermes 패턴 카탈로그 추출
    45	
    46	**출처**: `/tmp/hermes-phase0/hermes-agent/agent/redact.py` (v0.12.0 main HEAD, 401 LOC)
    47	**docstring 명시 (line 1-2)**: "Regex-based secret redaction for logs and tool output"
    48	**적용 범위**: 로그/도구 출력/LLM 송신 — DB INSERT 미적용 (R-1 FAIL 확정, ADR-011 §2.2 G1a)
    49	
    50	### 2.1 `_PREFIX_PATTERNS` (35종, line 67-103)
    51	
    52	| # | Vendor / Type | Regex | 출처 라인 |
    53	|---|------|------|------|
    54	| 1 | OpenAI / OpenRouter / Anthropic (`sk-ant-*`) | `sk-[A-Za-z0-9_-]{10,}` | 68 |
    55	| 2 | GitHub PAT (classic) | `ghp_[A-Za-z0-9]{10,}` | 69 |
    56	| 3 | GitHub PAT (fine-grained) | `github_pat_[A-Za-z0-9_]{10,}` | 70 |
    57	| 4 | GitHub OAuth access token | `gho_[A-Za-z0-9]{10,}` | 71 |
    58	| 5 | GitHub user-to-server | `ghu_[A-Za-z0-9]{10,}` | 72 |
    59	| 6 | GitHub server-to-server | `ghs_[A-Za-z0-9]{10,}` | 73 |
    60	| 7 | GitHub refresh token | `ghr_[A-Za-z0-9]{10,}` | 74 |
    61	| 8 | Slack tokens | `xox[baprs]-[A-Za-z0-9-]{10,}` | 75 |
    62	| 9 | Google API keys | `AIza[A-Za-z0-9_-]{30,}` | 76 |
    63	| 10 | Perplexity | `pplx-[A-Za-z0-9]{10,}` | 77 |
    64	| 11 | Fal.ai | `fal_[A-Za-z0-9_-]{10,}` | 78 |
    65	| 12 | Firecrawl | `fc-[A-Za-z0-9]{10,}` | 79 |
    66	| 13 | BrowserBase | `bb_live_[A-Za-z0-9_-]{10,}` | 80 |
    67	| 14 | Codex encrypted tokens | `gAAAA[A-Za-z0-9_=-]{20,}` | 81 |
    68	| 15 | AWS Access Key ID | `AKIA[A-Z0-9]{16}` | 82 |
    69	| 16 | Stripe secret key (live) | `sk_live_[A-Za-z0-9]{10,}` | 83 |
    70	| 17 | Stripe secret key (test) | `sk_test_[A-Za-z0-9]{10,}` | 84 |
    71	| 18 | Stripe restricted key | `rk_live_[A-Za-z0-9]{10,}` | 85 |
    72	| 19 | SendGrid API key | `SG\.[A-Za-z0-9_-]{10,}` | 86 |
    73	| 20 | HuggingFace token | `hf_[A-Za-z0-9]{10,}` | 87 |
    74	| 21 | Replicate API token | `r8_[A-Za-z0-9]{10,}` | 88 |
    75	| 22 | npm access token | `npm_[A-Za-z0-9]{10,}` | 89 |
    76	| 23 | PyPI API token | `pypi-[A-Za-z0-9_-]{10,}` | 90 |
    77	| 24 | DigitalOcean PAT | `dop_v1_[A-Za-z0-9]{10,}` | 91 |
    78	| 25 | DigitalOcean OAuth | `doo_v1_[A-Za-z0-9]{10,}` | 92 |
    79	| 26 | AgentMail API key | `am_[A-Za-z0-9_-]{10,}` | 93 |
    80	| 27 | ElevenLabs TTS key | `sk_[A-Za-z0-9_]{10,}` | 94 |
    81	| 28 | Tavily search API | `tvly-[A-Za-z0-9]{10,}` | 95 |
    82	| 29 | Exa search API | `exa_[A-Za-z0-9]{10,}` | 96 |
    83	| 30 | Groq Cloud API key | `gsk_[A-Za-z0-9]{10,}` | 97 |
    84	| 31 | Matrix access token | `syt_[A-Za-z0-9]{10,}` | 98 |
    85	| 32 | RetainDB API key | `retaindb_[A-Za-z0-9]{10,}` | 99 |
    86	| 33 | Hindsight API key | `hsk-[A-Za-z0-9]{10,}` | 100 |
    87	| 34 | Mem0 Platform API key | `mem0_[A-Za-z0-9]{10,}` | 101 |
    88	| 35 | ByteRover API key | `brv_[A-Za-z0-9]{10,}` | 102 |
    89	
    90	**경계 강제 (line 182-184)**: `(?<![A-Za-z0-9_-])(...)(?![A-Za-z0-9_-])` — 앞뒤 단어 경계 부정 lookahead로 부분 매칭 회피.
    91	
    92	### 2.2 추가 Regex 패턴 (12종)
    93	
    94	| # | 이름 | 용도 | 출처 라인 |
    95	|---|------|------|------|
    96	| H-A | `_ENV_ASSIGN_RE` | `OPENAI_API_KEY=value` 형태 ENV 대입 | 107-109 |
    97	| H-B | `_JSON_FIELD_RE` | `"apiKey": "..."` JSON 필드 (12 키) | 113-116 |
    98	| H-C | `_AUTH_HEADER_RE` | `Authorization: Bearer <token>` | 119-122 |
    99	| H-D | `_TELEGRAM_RE` | `bot<digits>:<token>` Telegram bot | 126-128 |
   100	| H-E | `_PRIVATE_KEY_RE` | `-----BEGIN ... PRIVATE KEY-----` 블록 | 131-133 |
   101	| H-F | `_DB_CONNSTR_RE` | `postgres/mysql/mongodb/redis/amqp://user:pass@host` | 137-140 |
   102	| H-G | `_JWT_RE` | `eyJ...` JWT (1/2/3-part) | 144-147 |
   103	| H-H | `_DISCORD_MENTION_RE` | `<@<snowflake>>` (privacy) | 151 |
   104	| H-I | `_SIGNAL_PHONE_RE` | E.164 `+<country><number>` (privacy) | 155 |
   105	| H-J | `_URL_WITH_QUERY_RE` | URL 쿼리 스트링 — `_SENSITIVE_QUERY_PARAMS` 16종 redact | 160-166 |
   106	| H-K | `_URL_USERINFO_RE` | `https://user:pass@host` (DB 외 스킴) | 171-173 |
   107	| H-L | `_FORM_BODY_RE` | `k=v&k=v` 폼 바디 — `_SENSITIVE_BODY_KEYS` 14종 redact | 177-179 |
   108	
   109	### 2.3 Sensitive Key Frozenset (2종)
   110	
   111	#### `_SENSITIVE_QUERY_PARAMS` (16개, line 19-36)
   112	```
   113	access_token, refresh_token, id_token, token, api_key, apikey, client_secret,
   114	password, auth, jwt, session, secret, key, code, signature, x-amz-signature
   115	```
   116	
   117	#### `_SENSITIVE_BODY_KEYS` (14개, line 41-56)
   118	```
   119	access_token, refresh_token, id_token, token, api_key, apikey, client_secret,
   120	password, auth, jwt, secret, private_key, authorization, key
   121	```
   122	
   123	#### `_JSON_KEY_NAMES` (line 112)
   124	```
   125	api_?[Kk]ey, token, secret, password, access_token, refresh_token,
   126	auth_token, bearer, secret_value, raw_secret, secret_input, key_material
   127	```
   128	(`re.IGNORECASE` 적용)
   129	
   130	### 2.4 Hermes 측 총 카탈로그 요약
   131	
   132	| 카테고리 | 수 | 적용 게이트 |
   133	|---------|---|----------|
   134	| Prefix patterns | **35** | 단어 경계 강제 |
   135	| 추가 regex | **12** | 카테고리별 별도 정규식 |
   136	| Sensitive frozenset | **2** (16+14 키) | URL/form 키 매칭 |
   137	
   138	**기본값**: `HERMES_REDACT_SECRETS=false` (line 64) — opt-in. v0.12.0 breaking change로 default ON → OFF 전환됨 (Day 1 보고서 §2 기록).
   139	
   140	---
   141	
   142	## 3. P1_REDACTOR 패턴 카탈로그 추출
   143	
   144	**출처**: `docs/architecture/llm-providers-design.md` §8.2 (line 521-536)
   145	**적용 범위**: P1 facade의 LiteLLM `success_callback` / `failure_callback` (메트릭/메시지 — DB INSERT 미적용 + Day 1 §218 명시 "P1 facade 레벨 → 영향 없음")
   146	**상태**: P1 v2 *설계 명세* 단계 — 구현 코드 미존재
   147	
   148	### 3.1 `RedactionFilter.PATTERNS` (4종)
   149	
   150	| # | Vendor / Type | Regex |
   151	|---|------|------|
   152	| P-1 | OpenAI API key | `sk-[a-zA-Z0-9]{20,}` |
   153	| P-2 | Anthropic API key | `sk-ant-[a-zA-Z0-9]{20,}` |
   154	| P-3 | Bearer token | `Bearer [a-zA-Z0-9._-]+` |
   155	| P-4 | JSON field with secret keys | `"(api_key\|token\|auth\|secret\|password\|credential)"\s*:\s*"[^"]+"` |
   156	
   157	### 3.2 `KEY_BLACKLIST` (6개)
   158	```
   159	api_key, token, secret, auth, credential, authorization
   160	```
   161	
   162	### 3.3 P1_REDACTOR 측 총 카탈로그 요약
   163	
   164	| 카테고리 | 수 |
   165	|---------|---|
   166	| Patterns | **4** |
   167	| KEY_BLACKLIST | **6** 키 |
   168	
   169	P-1과 Hermes #1 모두 `sk-` prefix를 다루나 **문자 클래스 차이 존재** — Hermes는 `[A-Za-z0-9_-]` (`_`/`-` 허용), P1은 `[a-zA-Z0-9]` (`_`/`-` 미허용). Hermes가 **더 광범위**.
   170	
   171	---
   172	
   173	## 4. R-2 PoC trigger UDF 패턴 카탈로그 (현 baseline)
   174	
   175	**출처**: `docs/phase0/day3-r2-sqlite-trigger-poc.md` line 110-122 + `docker/r2-poc/r2_poc.py`
   176	**적용 범위**: SQLCipher BEFORE INSERT trigger (DB INSERT 직전, REGEXP UDF로 Python `re.search`)
   177	**작동 방식**: 매칭 시 `RAISE(ABORT, 'secret-pattern-detected: ...')` — 마스킹 미시도, INSERT 자체 거부 (사용자 선호 명시)
   178	**에러 메시지 고정 문자열**: `NEW.content` echo 안 함 → C6 만족 (에러 평문 미노출)
   179	
   180	### 4.1 현 trigger UDF 패턴 (5종)

exec
/bin/bash -lc "nl -ba docs/phase0/r4-1-trigger-extension-evidence.md | sed -n '1,180p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# R-4.1 Trigger UDF Extension Evidence
     2	
     3	> **ADR-011 §2.1 (b) 격리 환경 PoC 실증 직접 충족 산출 — R-4 §6/§7 권고 카탈로그를 R-2 PoC 격리 환경에 적용하여 trigger UDF 가 Tier-1 42종 canary 를 차단하면서 정상 메시지 처리에 영향이 없음을 실증**
     4	
     5	**상태**: PASS (2026-05-06)
     6	**산출 형태**: 옵션 B — 신규 evidence 문서 (사용자 결정 2026-05-06)
     7	**상위 권위**: ADR-011 §2.1 (b) 격리 환경 PoC 실증 의무, ADR-008 부록 B.6 정식 충족 5단계 중 R-4
     8	**입력 권위**: `docs/architecture/redaction-pattern-equivalence.md` (R-4, commit `3b005f0`) §6/§7 권고 카탈로그
     9	**평가 기준**: 사용자 명시 R-4.1 PASS 기준 7항목 (2026-05-06)
    10	
    11	---
    12	
    13	## 1. 작업 정의
    14	
    15	### 1.1 본 R-4.1 의 본질 (사용자 명시)
    16	
    17	R-4.1 은 R-2 PoC 의 단순 부록이 아니라, ADR-011 §2.1 (b) "computationally verifiable" 조건을 직접 충족하기 위한 별도 evidence 문서이다. R-7 SOP 와 이후 P2 v3 에서 인용하기 쉽도록 **독립 evidence 문서**로 작성.
    18	
    19	### 1.2 사용자 명시 R-4.1 필수 범위
    20	
    21	| # | 범위 | 본 evidence § |
    22	|---|------|------|
    23	| 1 | Tier-1 42종 trigger UDF 확장 | §4 |
    24	| 2 | R-2 PoC 격리 환경 재실행 | §3 |
    25	| 3 | 각 Tier-1 패턴별 C1 canary inject | §5 |
    26	| 4 | 정상 safe message insert 유지 확인 | §6 |
    27	| 5 | DB 평문 부재 확인 | §7 (C5) |
    28	| 6 | 에러 메시지에 canary 평문 미노출 확인 | §7 (C6) |
    29	| 7 | 결과를 신규 evidence 문서에 기록 | 본 문서 |
    30	
    31	### 1.3 사용자 명시 R-4.1 PASS 기준 (7항목)
    32	
    33	| # | 기준 | 본 R-4.1 결과 |
    34	|---|------|------|
    35	| 1 | Tier-1 42종 패턴이 trigger UDF 에 반영됨 | ✅ §4.1 |
    36	| 2 | C1 canary 42종 insert 가 모두 차단됨 | ✅ §5 (42/42 BLOCK) |
    37	| 3 | 정상 safe message insert 는 계속 성공함 | ✅ §6 (9/9 PASS) |
    38	| 4 | DB 내부에 C1 canary 평문이 남지 않음 | ✅ §7 C5 |
    39	| 5 | 에러 메시지에 C1 canary 평문이 노출되지 않음 | ✅ §7 C6 |
    40	| 6 | Docker 격리 환경에서 재현 가능함 | ✅ §3 |
    41	| 7 | 실행 명령어와 결과가 evidence 문서에 기록됨 | ✅ §3.2 / §7 / §8 |
    42	
    43	**최종 verdict**: **PASS** (7/7 충족, 2차 실행)
    44	
    45	### 1.4 범위 외 (사용자 명시)
    46	
    47	| 항목 | 처리 |
    48	|------|------|
    49	| Tier-2 Telegram bot | 본 R-4.1 미포함 — R-7 SOP 작성 시점에 Tier-1 승격 검토 |
    50	| Tier-3 Discord, E.164 (privacy) | 본 R-4.1 미포함 — 별도 합의, 헌법 8조 외 영역 |
    51	| C2 base64/URL encode/Unicode 우회 | 본 R-4.1 PASS/FAIL 차단조건 외 — §11 Deferred Hardening Candidates 에 후속 과제 기록 |
    52	
    53	---
    54	
    55	## 2. 패턴 카탈로그 정정 (R-4 §7.2 enumerate)
    56	
    57	R-4 §7.2 헤딩 "41종 (Prefix 30 + 추가 regex 9 + frozenset 2)" 표현은 prefix 카운트 산술 오류로 추정된다. R-4 §6.2.1 본문 카탈로그를 직접 enumerate 하면 다음과 같다:
    58	
    59	| 카테고리 | 본 R-4.1 enumerate | R-4 §7.2 헤딩 표현 | 차이 사유 |
    60	|---------|------|------|------|
    61	| Prefix patterns (Hermes 35 - baseline 4) | **31** | 30 | `sk_` ElevenLabs 별도 enumerate (Hermes line 94 disambiguation 코멘트 채택) |
    62	| 추가 regex (Hermes 12 - Tier-2 1 - Tier-3 2) | **9** | 9 | 일치 |
    63	| Frozenset → alternation regex 변환 | **2** | 2 | 일치 (의미: H-J/H-L 의 sensitive key 기반 변형) |
    64	| **합계** | **42** | 41 | +1 (sk_ ElevenLabs) |
    65	
    66	본 R-4.1 은 **42종 enumerate** 로 진행하며, 이는 사용자 결정 "Tier-1 41종" 의 본질 (Hermes 측 Tier-1 카탈로그 전수 반영) 을 충족한다. R-4 (commit `3b005f0`) 의 §7.2 헤딩 산술 표기는 후속 ADR Amendment 또는 R-4 후속 commit 에서 41 → 42 정정 권고.
    67	
    68	---
    69	
    70	## 3. 격리 환경 (Docker)
    71	
    72	### 3.1 환경 구성
    73	
    74	R-2 PoC 와 동일 격리 강도 적용:
    75	
    76	| 항목 | 설정 | 출처 |
    77	|------|------|------|
    78	| base image | `python:3.11-slim` | `docker/r4-1-poc/Dockerfile` |
    79	| SQLCipher | `libsqlcipher-dev` apt + `pysqlcipher3==1.2.0` pip | 동상 |
    80	| 네트워크 | `network_mode: none` | `docker-compose.r4-1-poc.yml` |
    81	| 파일시스템 | `read_only: true` + `tmpfs: /tmp:noexec,nosuid,size=64m` | 동상 |
    82	| Linux capabilities | `cap_drop: ALL` | 동상 |
    83	| 권한 escalation | `security_opt: no-new-privileges:true` | 동상 |
    84	| user | `1000:1000` (non-root) | 동상 |
    85	
    86	### 3.2 실행 명령어
    87	
    88	```bash
    89	cd docker/r4-1-poc
    90	docker compose -f docker-compose.r4-1-poc.yml up --build --abort-on-container-exit
    91	```
    92	
    93	### 3.3 SQLCipher 설정
    94	
    95	| PRAGMA | 값 |
    96	|--------|-----|
    97	| `PRAGMA key` | `'test-key-r4-1-poc-not-for-prod'` (테스트 전용) |
    98	| `PRAGMA cipher_page_size` | `4096` |
    99	
   100	---
   101	
   102	## 4. trigger UDF 구현 요약
   103	
   104	### 4.1 등록 패턴 (45종)
   105	
   106	```
   107	Baseline 5 prefix (R-2 PoC 보존):
   108	  sk-ant-, sk-, ghp_, AKIA, xox[baprs]-
   109	
   110	Tier-1 prefix 31 (Hermes #3..#7, #9..#14, #16..#35):
   111	  github_pat_, gho_, ghu_, ghs_, ghr_, AIza, pplx-, fal_, fc-, bb_live_,
   112	  gAAAA, sk_live_, sk_test_, rk_live_, SG\., hf_, r8_, npm_, pypi-, dop_v1_,
   113	  doo_v1_, am_, sk_ (ElevenLabs), tvly-, exa_, gsk_, syt_, retaindb_, hsk-,
   114	  mem0_, brv_
   115	
   116	Tier-1 추가 regex 7 (H-A, H-B, H-C, H-E, H-F, H-G, H-K — H-J/H-L 제외):
   117	  ENV assignment, JSON field (12 keys, IGNORECASE),
   118	  Authorization header (Bearer, IGNORECASE), Private key block,
   119	  DB connstr password (postgres/mysql/mongodb/redis/amqp, IGNORECASE),
   120	  JWT (eyJ...), URL userinfo (non-DB schemes)
   121	
   122	Tier-1 alternation 2 (H-J/H-L 의 sensitive key 기반 변환):
   123	  URL query sensitive keys alternation (16, IGNORECASE),
   124	  Body/form sensitive keys alternation (14, IGNORECASE)
   125	```
   126	
   127	총 **5 + 31 + 7 + 2 = 45 patterns** trigger 등록.
   128	
   129	### 4.2 H-J / H-L 직접 등록 제외 결정
   130	
   131	R-4 §7.2.2 권고 9종 중 H-J `_URL_WITH_QUERY_RE` 와 H-L `_FORM_BODY_RE` 는 **직접 등록 제외**. 사유:
   132	
   133	1. **1차 실행 false-positive** (§8.1): 모든 URL+query / form-shaped body 메시지 차단 — 정상 사용 케이스 (`https://example.com/?q=hello&page=2`) 도 차단.
   134	2. **R-4 §7.2.3 alternation 변환이 본질적 해결**: `_SENSITIVE_QUERY_PARAMS` 16 키 / `_SENSITIVE_BODY_KEYS` 14 키 의 alternation regex 가 *sensitive key 기반 정확한 매칭* 담당.
   135	3. **canary 차단 보장**: H-J/H-L canary (T1-038, T1-040) 가 alternation T1-041/T1-042 에 의해 매칭 차단됨 (canary input 에 `access_token=` 포함, alternation 매칭 ✓).
   136	4. **R-4 §7.2 권고의 *세부화***: trigger 적용 형태로는 alternation 만 채택 — 본 R-4.1 evidence 는 R-4 §7.2.3 alternation 의 트리거 적용을 정식화.
   137	
   138	### 4.3 trigger SQL 구조
   139	
   140	```sql
   141	CREATE TRIGGER block_secrets_messages
   142	BEFORE INSERT ON messages
   143	FOR EACH ROW
   144	WHEN NEW.content IS NOT NULL AND (
   145	       NEW.content REGEXP 'sk-ant-[A-Za-z0-9_-]{10,}'
   146	    OR NEW.content REGEXP 'sk-[A-Za-z0-9_-]{10,}'
   147	    OR ... (43 추가 OR 절) ...
   148	    OR NEW.content REGEXP '(?i)(?:access_token|refresh_token|...|x-amz-signature)=[^&\s]+'
   149	    OR NEW.content REGEXP '(?i)(?:access_token|refresh_token|...|key)=[^&\s]+'
   150	)
   151	BEGIN
   152	    SELECT RAISE(ABORT, 'secret-pattern-detected: INSERT blocked by R-4.1 trigger');
   153	END;
   154	```
   155	
   156	- ABORT 메시지는 **고정 문자열** — `NEW.content` echo 안 함 (C6 만족 설계).
   157	- REGEXP UDF 는 Python `re.search` 기반 — 인라인 flag `(?i)` 인식.
   158	- 멀티라인 매칭 (H-E `[\s\S]*?`) 은 `[\s\S]` 자체로 DOTALL 회피 — REGEXP UDF 정상 작동.
   159	
   160	전체 코드: `docker/r4-1-poc/r4_1_poc.py`.
   161	
   162	---
   163	
   164	## 5. C1 canary 결과 — Tier-1 42종 (모두 BLOCK PASS)
   165	
   166	각 canary input 은 명백히 가짜임을 표시 (공통 marker `R41T` + `NOTAREAL` / `fakecanary` prefix).
   167	
   168	### 5.1 Prefix patterns (T1-001 ~ T1-031, 31종)
   169	
   170	| ID | Source | Vendor | Canary Input | Expected | Actual | Result |
   171	|---|---|---|---|---|---|---|
   172	| T1-001 | Hermes #3 | GitHub PAT (fine-grained) | `config token=github_pat_CANARYR41T001NOTAREAL` | BLOCK | BLOCK | PASS |
   173	| T1-002 | Hermes #4 | GitHub OAuth access token | `user gho_CANARYR41T002NOTAREAL value` | BLOCK | BLOCK | PASS |
   174	| T1-003 | Hermes #5 | GitHub user-to-server | `ghu_CANARYR41T003NOTAREAL hint` | BLOCK | BLOCK | PASS |
   175	| T1-004 | Hermes #6 | GitHub server-to-server | `tok ghs_CANARYR41T004NOTAREAL string` | BLOCK | BLOCK | PASS |
   176	| T1-005 | Hermes #7 | GitHub refresh token | `refresh ghr_CANARYR41T005NOTAREAL boom` | BLOCK | BLOCK | PASS |
   177	| T1-006 | Hermes #9 | Google API keys | `key AIzaCANARYR41T006NOTAREALSECRETTOKEN001 ok` | BLOCK | BLOCK | PASS |
   178	| T1-007 | Hermes #10 | Perplexity | `pplx-CANARYR41T007NOTAREAL test` | BLOCK | BLOCK | PASS |
   179	| T1-008 | Hermes #11 | Fal.ai | `fal_CANARYR41T008NOTAREAL key` | BLOCK | BLOCK | PASS |
   180	| T1-009 | Hermes #12 | Firecrawl | `fc-CANARYR41T009NOTAREAL crawl` | BLOCK | BLOCK | PASS |

exec
/bin/bash -lc 'rg -n "MVP-2 Implementation Evidence PASS|R-1|R-2|R-5|base64|R-S1|secret_scanner.py|secret-hygiene" docs/phase0/mvp2-gp2-pass-activation-brief.md' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
11:> **본 cycle 발효 효과** = **GP-2 송신 redaction PASS 발효**. MVP-2 Implementation Evidence PASS = Layer 통합 PASS (59 ✅) + GP-2 PASS (본 cycle) + R-S1 hard gate 후 별도 cycle
13:> **선행 답습**: 51 audit (GP-2 Exit 5조건, R-1~R-5 후보) + 57 ((β) R-4 = R-3 detection 우선 + R-1/R-2 prevention deferred) + 59 (Layer 통합 PASS 발효, means-vs-ends + DEFER 패턴 답습)
22:2. **R-3 detection (operative) + R-1/R-2 prevention (deferred trajectory) 분리** (57 (β) + 59 Layer 2a DEFER 패턴 답습) (§3)
24:4. **R-5 base64 evasion = known limitation 명문** (R-5 영구 분리) (§4)
34:| 2 | **MVP-2 Implementation Evidence PASS 발효** (Layer 통합 PASS + GP-2 PASS + R-S1 후 별도) | 0 |
35:| 3 | **R-1 Hermes import 결정** (prevention 구현 경로, 별도 cycle) | 0 |
36:| 4 | **R-2 facade real (TR-1)** (prevention 구현 경로, 별도 trajectory) | 0 |
37:| 5 | R-5 base64/URL-encoded/압축 evasion 영역 진입 (MVP-2/3 분리, G3-4) | 0 |
39:| 7 | R-S1 cross-reference 정정 (MVP-2 PASS 전 hard gate, 별도 cycle) | 0 |
42:| 10 | secret_scanner.py / secret-hygiene-egress-redaction.yml 본문 변경 | 0 (PoC 시제 보존) |
43:| 11 | 자동 후속 cycle 진입 (MVP-2 PASS / R-S1) | 0 (사용자 명시 의무) |
54:- **57 (β) brief v1.1** (R-4 = R-3 detection + R-1/R-2 prevention deferred) — `docs/phase0/mvp2-beta-submeans-decision-brief.md`
56:- **본 cycle audit (read-only, 2026-05-28)** — secret-hygiene CI + fixtures + secret_scanner filesystem direct
66:| 59 Layer 1+2+4 통합 PASS 발효 (`0f49eb9`, 4 source APPROVE WITH CONDITIONS) | MVP-2 = Layer 통합 PASS ✅ + **GP-2 PASS (본 cycle)** + R-S1. means-vs-ends + DEFER 패턴 + B-2 (a)~(d)/(e2) framing 답습 |
67:| 57 (β) R-4 결정 (`18e8ad1`) | GP-2 수단 = R-4 (R-3 detection 우선 + R-1/R-2 prevention deferred trajectory). R-5 영구 분리 |
68:| 51 audit §2 (`f7ac61d`) | GP-2 Exit 5조건 — 본 cycle 현행화 (51 audit "(d) gap" = 부정확, secret-hygiene D-2 이미 운영) |
74:- 본 repo = DESIGN/governance repo (docs + tools + CI). 실 runtime redaction = Hermes upstream (R-1). 본 repo GP-2 PASS = redaction 패턴 정의 (R-4) + CI 회귀 검출 (R-3) + 설계 권위 (ADR-011 §2.3).
83:| (b) | 격리 환경 PoC 실증 | ✅ | secret-hygiene D-2 scan-log redaction PoC (`tests/fixtures/secret_hygiene/redaction_pass/env_redacted.txt` rc=0 잔존 0 + `redaction_fail/partial_redact.txt` rc=1 leak 검출) + `r4-1-trigger-extension-evidence.md` (R-4.1 Tier-1 42 + baseline 5 PoC) |
85:| (d) | 자동 회귀 검증 경로 | ✅ ⭐ | **`secret-hygiene-egress-redaction.yml` D-2 step (scan-log redaction residual, `secret_scanner.py --mode scan-log`) — 51 audit "❌ gap" 부정확 정정 (52 entry PoC 시제 발견 동형). actual run `26517803107` success (headSha `4fec6485`). ⚠️ secret-hygiene = `workflow_dispatch` 미지원 (schedule cron `0 3 * * *` 만) — 단 secret_scanner.py + workflow + redaction fixtures = 49 entry (`4fec6485`) 이후 **변경 0 (불변)** → 최근 green run = 현 코드 유효 evidence** |
88:→ **(a)~(d) 4/4 충족** (51 audit 2.5/5 → 본 cycle 4/4, R-3 secret-hygiene D-2 CI operative green). (e2) = 본 cycle.
92:## §3 R-3 detection (operative) + R-1/R-2 prevention (deferred) 분리 (57 (β) + 59 Layer 2a 답습)
98:| **R-3** log canary CI (`secret-hygiene-egress-redaction.yml` + `secret_scanner.py --mode scan-log`) | **detection (회귀 검증)** | ✅ operative green | GP-2 (d) 자동 회귀 충족 — in-repo operative means |
99:| **R-1** Hermes native redaction (`agent/redact.py`) | **prevention (능동 redaction)** | ❌ 본 repo 부재 (Hermes upstream v0.12.0) | runtime prevention = Hermes upstream operative (import 결정 별도 cycle). ADR-011 §2.3 #2 송신 방어 신뢰 |
100:| **R-2** facade RedactionFilter | prevention (LLM API 진입점) | ⚠️ facade placeholder | facade real (TR-1) 시점 추가 layer (deferred trajectory) |
101:| **R-5** base64/URL/압축 evasion | (out of scope) | ❌ known limitation (`base64_evasion.txt` fixture) | 영구 분리 (MVP-2/3, G3-4) |
106:- **detection ends** = R-3 (secret-hygiene D-2 CI) ✅ operative green — 송신/로그에 secret 잔존 시 BLOCK (회귀 검증).
107:- **prevention ends** = R-1 (Hermes upstream native redaction, 실 runtime operative — 본 repo 는 DESIGN repo 이므로 import 미결정이나 Hermes runtime 자체는 redaction 수행) + R-2 (facade real deferred).
108:- **본 repo (DESIGN/governance) GP-2 PASS** = R-4 패턴 정의 (a) + R-3 CI 회귀 검출 (b)(d) + ADR 권위 (c). prevention 능동 redaction 의 실 구현 = Hermes upstream (R-1) + facade real (R-2) = 별도 trajectory (59 Layer 2a "operative 보호 = 다른 layer, 본 layer DEFER" 패턴 동형).
110:→ **GP-2 PASS = detection (R-3 operative) + 설계 권위 + 패턴 동등성. prevention 능동 redaction 구현 경로 (R-1 Hermes import / R-2 facade real) = cross-trajectory deferred** (57 (β) 결정 답습, 59 DEFER 패턴).
121:| (b) 격리 PoC | ADR-011 §2.1 | ✅ secret-hygiene D-2 + r4-1 PoC |
123:| (d) 자동 회귀 검증 | ADR-011 §2.1 | ✅ secret-hygiene D-2 CI green |
126:### §4.1 R-5 base64 evasion = known limitation (영구 분리)
128:`tests/fixtures/secret_hygiene/redaction_fail/base64_evasion.txt` 존재 — secret-hygiene D-2 가 base64 evasion 미검출 (known limitation 명문, workflow line 13). R-5 = MVP-2/3 분리 (G3-4), GP-2 PASS scope 외. GP-2 PASS = Tier-1 42 catalog 평문 redaction 한정 (base64 evasion 제외 명문).
145:| 4 | 권위 chain 다중 source 손상 | ⚠️ 부분 | R-S1 (MVP-2 PASS 전 hard gate, 본 cycle 비차단) |
158:1. **(a)~(d) 4/4 충족** — R-4 패턴 동등성 + secret-hygiene D-2 PoC + ADR 권위 + R-3 CI 회귀 green. (e2) = 본 cycle.
160:   - (C-1) **R-1 (Hermes import) / R-2 (facade real) = prevention deferred trajectory 명문** (GP-2 PASS = detection operative + 설계 권위 기반, 능동 redaction 구현 = 별도 cycle, 59 Layer 2a DEFER 답습)
161:   - (C-2) **R-5 base64 evasion = known limitation 명문** (Tier-1 42 평문 한정)
162:   - (C-3) secret-hygiene D-2 actual run = `26517803107` green (`4fec6485`) + 코드 불변 (49 entry 이후 변경 0) = 유효 evidence. workflow_dispatch 미지원이므로 fresh run 은 schedule (cron) 또는 path 변경 시 (GP-2 PASS 비차단)
163:3. **R-S1 = GP-2 PASS 비차단** (MVP-2 PASS 전 hard gate, 별도 cycle).
171:§0.2 답습 (12). 추가: MVP-2 PASS 자동 선언 0 / R-1 Hermes import 결정 0 / R-2 facade real 0 / R-5 evasion 진입 0 / R-S1 자동 정정 0 / 자동 후속 0.
178:2. **MVP-2 Implementation Evidence PASS 발효 합의** (Layer 통합 PASS ✅ + GP-2 PASS ✅ + R-S1 hard gate 후, 32 답습) — MVP-2 최종 milestone
179:3. R-S1 cross-reference 정정 cycle (MVP-2 PASS 전 hard gate 3 옵션)
180:4. (선택) R-1 Hermes import / R-2 facade real (TR-1) prevention trajectory
189:- redaction-pattern-equivalence.md (R-4) + r4-1-trigger-extension-evidence.md (R-4.1) + g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md (Group D PoC)
191:- 실 evidence: `secret-hygiene-egress-redaction.yml` (D-2) + `tools/secret_scanner.py` (--mode scan-log) + `tests/fixtures/secret_hygiene/{redaction_pass,redaction_fail}/`
200:| P-2 | R-3 detection 만으로 GP-2 PASS *단순화* (prevention R-1/R-2 부재 은폐) | §3 detection/prevention 분리 명시 + (C-1) deferred 명문 (59 Layer 2a DEFER 답습, β B-1 cascade 교훈) |
201:| P-3 | 51 audit "(d) gap" → 본 brief "(d) ✅" 격상 over-claim risk | §2 (d) = secret-hygiene D-2 CI green actual run 근거 (filesystem + run direct verify), 52 entry PoC 시제 발견 동형 (gap 표기 부정확 정정) |
202:| P-4 | DESIGN repo GP-2 PASS vs runtime redaction 혼동 | §1.2 + §3.2 = 본 repo = 설계/CI, 실 runtime redaction = Hermes upstream (R-1) 명시 |
203:| P-5 | R-5 base64 known limitation 과소 | §4.1 명문 (base64_evasion.txt fixture + workflow line 13) |

codex
검토의 핵심 판정은 갈립니다. `(d) 자동 회귀 경로` 자체는 over-claim로 보이지 않지만, 이를 근거로 `(a) 동등 이상 보안 결과`와 “GP-2 송신 redaction PASS”까지 4/4로 닫는 부분은 governance §4.5의 prevention 요구와 충돌할 소지가 큽니다.
exec
/bin/bash -lc 'rg -n "DEFER|means-vs-ends|Layer 2a|B-2|APPROVE|조건|R-S1|deferred" docs/phase0/mvp2-layer-124-pass-activation-brief.md docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass-activation.md' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
docs/phase0/mvp2-layer-124-pass-activation-brief.md:5:> **v1 → v1.1 갱신**: 풀 3+1 + 외부 LLM 1+ (codex gpt-5.5 cross-vendor) 통합 합의 (`docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass-activation.md`) **APPROVE WITH CONDITIONS (4 source 전원) → BLOCKING 3 + 권고 4 1pass 흡수**. 정정: B-1 citation (`6ebc634`→`052e583`) / B-2 ADR-011 §2.1 (a)~(d) 모법 + (e2) ADR-012 §4 확장 / B-3 2a denyNonFastForwards = non-bare clone no-op (DEFER 강화) + N-1 2a DEFER 이중 cover (2b + rewrite-defense CI). evidence 4 source 전원 실증 (over-claim 0). §12 흡수 매트릭스 추가.
docs/phase0/mvp2-layer-124-pass-activation-brief.md:11:> **본 cycle 발효 자격** = (a)~(d) evidence + (e2) 풀 3+1 + 외부 LLM 1+ 합의 APPROVE + 사용자 명시
docs/phase0/mvp2-layer-124-pass-activation-brief.md:13:> **본 cycle 발효 효과** = **Layer 1+2+4 통합 PASS 발효** (G4 §4.4 Layer 1+2+4 부분 답습 — Layer 3+5 scope 외). MVP-2 Implementation Evidence PASS = Layer 통합 PASS + GP-2 PASS + R-S1 hard gate 후 별도 cycle
docs/phase0/mvp2-layer-124-pass-activation-brief.md:25:3. **gap / DEFER 처리** — Layer 2a denyNonFastForwards DEFER (57/58 비례 보안 결정) + E-PASS-10 timestamp fixture + r2-canary (§4)
docs/phase0/mvp2-layer-124-pass-activation-brief.md:26:4. **R-S1 hard gate (RT-γ-6) PASS 시점 선행/동시 정정 *자격* 평가** ((γ-c) 특화 의무 4) (§5)
docs/phase0/mvp2-layer-124-pass-activation-brief.md:28:6. **PASS 발효 권고 + 조건** (§7)
docs/phase0/mvp2-layer-124-pass-activation-brief.md:35:| 1 | Layer 통합 PASS *발효* 자체 (본 brief = 합의 입력, 발효 = 합의 APPROVE + 사용자 명시 후) | 0건 |
docs/phase0/mvp2-layer-124-pass-activation-brief.md:36:| 2 | **MVP-2 Implementation Evidence PASS 발효** (Layer 통합 PASS + GP-2 PASS + R-S1 후 별도) | 0건 |
docs/phase0/mvp2-layer-124-pass-activation-brief.md:38:| 4 | denyNonFastForwards 활성화 실행 (57/58 DEFER 답습, 비례 보안) | 0건 |
docs/phase0/mvp2-layer-124-pass-activation-brief.md:40:| 6 | R-S1 cross-reference 정정 자체 (RT-γ-6 = 평가 한정, 정정 = 별도 cycle) | 0건 |
docs/phase0/mvp2-layer-124-pass-activation-brief.md:47:| 13 | 자동 후속 cycle 진입 (MVP-2 PASS / R-S1 정정) | 0건 (사용자 명시 의무) |
docs/phase0/mvp2-layer-124-pass-activation-brief.md:52:- **ADR-011 §2.1 (a)~(d) 4조건 모법** (line 52~61) — `docs/decisions/ADR-011-means-vs-ends-redaction.md` (B-2: §2.1 = (a)~(d), (e) 아님)
docs/phase0/mvp2-layer-124-pass-activation-brief.md:53:- **ADR-012 §4 (a)~(d) + (e) 5조건 답습 확장** (PASS 발효 (e2) 권위 출처) — `docs/decisions/ADR-012-evidence-ledger-protection.md`
docs/phase0/mvp2-layer-124-pass-activation-brief.md:69:| 55 통합 PASS 격상 **진입 권한 (e1)** (`311ca3b`, 4 source APPROVE WITH CONDITIONS, BLOCKING 9 + 권고 18) | (e1) 진입 권한 발효 답습 → 본 cycle = (e2) PASS 발효 |
docs/phase0/mvp2-layer-124-pass-activation-brief.md:80:| 4 | RT-γ-6 R-S1 PASS 시점 선행/동시 정정 *평가* 의무 | §5 평가 (정정 = 별도 cycle) |
docs/phase0/mvp2-layer-124-pass-activation-brief.md:99:### §2.2 Layer 2a — local denyNonFastForwards ⚠️ DEFER
docs/phase0/mvp2-layer-124-pass-activation-brief.md:103:| E-PASS-5: denyNonFastForwards 활성화 + force-push reject PoC | ⚠️ **DEFER** | 57/58 사용자 비례 보안 결정. ⭐ **B-3 정정**: `receive.denyNonFastForwards` = push *받는* repo (bare/server) 에서만 작동 — 본 repo = 비-bare 작업 clone (push 대상 = GitHub) → 본 clone 활성화 = **no-op (효과 0, "영향 최소" 아님)**. operative append-only 보호 = Layer 2b (§2.3) + rewrite-defense.yml CI (§2.4) |
docs/phase0/mvp2-layer-124-pass-activation-brief.md:105:→ **Layer 2a = DEFER** (B-3: 본 clone no-op, 켤 이유 소멸). ⭐ **N-1 — Layer 2 append-only ends 이중 cover** (ADR-012 §2.3 Layer 2 = denyNonFastForwards/branch protection/pre-commit/CI **4 means 동시 열거**, 단일 수단 종속 0): (1) Layer 2b branch protection (allow_force_pushes/deletions false + enforce_admins true) + (2) rewrite-defense.yml Layer 4 CI (`non_fast_forward_detected` / `history_reorder_detected` 검출, actual run green). 2a 가 막으려는 시나리오를 2 layer 가 이미 cover. 2a = 실 bare/server 배포 trigger 시점 (별도, [[feedback_proportionate_security_personal_tool]]).
docs/phase0/mvp2-layer-124-pass-activation-brief.md:119:⚠️ **N-3 (Layer 5 framing)**: `history-anchor-verifier.yml` 은 이름이 "Layer 5 External Anchor Verifier" 이나, 본 cycle 은 이를 **Layer 2 history rewrite 검출 보조 evidence 로만 인용** (Layer 5 External anchor *PASS 진입 발효 0*). "부분 답습" framing 유지 (Layer 3+5 scope 외, 55 entry B-2 답습).
docs/phase0/mvp2-layer-124-pass-activation-brief.md:121:→ **Layer 2 = 충족** (2b operative + rewrite-defense CI 이중 cover + history 검출 actual run green, 2a DEFER no-op 문서화).
docs/phase0/mvp2-layer-124-pass-activation-brief.md:141:| E-PASS-15: R-S1 정정 자격 평가 (RT-γ-6) | §5 |
docs/phase0/mvp2-layer-124-pass-activation-brief.md:145:## §3 PASS 발효 자격 매핑 — ADR-011 §2.1 (a)~(d) 모법 + (e2) ADR-012 §4 확장 (B-2 정정)
docs/phase0/mvp2-layer-124-pass-activation-brief.md:147:> ⚠️ **B-2**: ADR-011 §2.1 = **(a)~(d) 4조건만** (line 52~61). "(e) 합의 APPROVE" = ADR-012 §4 "(a)~(d) + (e) 5조건 답습" 확장 패턴 (§0.3 framing). 본 §3 = (a)~(d) ADR-011 모법 + (e2) ADR-012 §4 확장 매핑.
docs/phase0/mvp2-layer-124-pass-activation-brief.md:149:| # | 조건 | Layer 1 | Layer 2 (2a+2b) | Layer 4 | 통합 |
docs/phase0/mvp2-layer-124-pass-activation-brief.md:151:| (a) | 동등 이상 보안 결과 | ✅ middle tampering 차단 (3 violation type) | ✅ 2b force push/delete 차단 + history 재작성 차단 (2a DEFER, 2b operative) | ✅ CI 회귀 (canonical BLOCK + timestamp monotonicity, C-1 보강) | Layer 1+2+4 통합 (subsection 분리) |
docs/phase0/mvp2-layer-124-pass-activation-brief.md:155:| **(e2)** | **PASS 발효 합의 APPROVE** | ⏳ 본 cycle | ⏳ 본 cycle | ⏳ 본 cycle | ⏳ **본 cycle 풀 3+1 + 외부 LLM + 사용자 명시** |
docs/phase0/mvp2-layer-124-pass-activation-brief.md:157:→ **(a)~(d) 충족 = Layer 1 완전 / Layer 2 충족 (2a DEFER 문서화, 2b operative) / Layer 4 충족 (C-1 timestamp 보강 완료, r2-canary = R-6/R-2 영역)**. (e2) = 본 cycle 합의.
docs/phase0/mvp2-layer-124-pass-activation-brief.md:161:## §4 gap / DEFER 처리
docs/phase0/mvp2-layer-124-pass-activation-brief.md:163:### §4.1 Layer 2a denyNonFastForwards = DEFER (B-3 + N-1 정정)
docs/phase0/mvp2-layer-124-pass-activation-brief.md:165:- ⭐ **B-3**: `receive.denyNonFastForwards` = push *받는* repo (bare/server) 에서만 작동. 본 repo = 비-bare 작업 clone, push 대상 = GitHub → 본 clone 활성화 = **no-op (효과 0)**. "per-repo = 영향 최소/ceremony" framing (55 §4.4.2) 부정확 → 정정 = **켤 이유 소멸** (no-op), DEFER 강화.
docs/phase0/mvp2-layer-124-pass-activation-brief.md:167:- **PASS 발효 영향**: Layer 2 append-only *결과(ends)* = 2b + rewrite-defense CI 이중 충족. 2a = 실 bare/server 배포 시점 (별도 trigger, no-op 이므로 본 clone 무관). PASS 발효 = ends 충족 + 2a DEFER no-op 명문.
docs/phase0/mvp2-layer-124-pass-activation-brief.md:181:## §5 R-S1 hard gate (RT-γ-6) PASS 시점 선행/동시 정정 *자격* 평가
docs/phase0/mvp2-layer-124-pass-activation-brief.md:183:- R-S1 = ADR-012 *자체 내부* §2.3 (4-layer numbering) vs §2.8 / G4 §4.4.1 (5-layer numbering) divergence (52/53 entry 5 source verify CONFIRMED).
docs/phase0/mvp2-layer-124-pass-activation-brief.md:184:- **RT-γ-6 평가** (54 §1.3 의무 4): MVP-2 Implementation Evidence PASS 발효 시점 R-S1 정정 선행/동시 *자격* 평가 의무. **단 본 cycle = Layer 통합 PASS 발효 (MVP-2 PASS 아님)**. R-S1 정정 = MVP-2 PASS 전 hard gate (3 옵션: ADR-012 §2.3 정정 / §2.8 강화 / 권위 선언) — **별도 cycle**.
docs/phase0/mvp2-layer-124-pass-activation-brief.md:185:- **본 cycle 영향**: Layer 통합 PASS 는 G4 §4.4.1 numbering (PRIMARY, 5-layer) 답습 — R-S1 정정 *전*에도 G4 §4.4.1 권위로 Layer 1+2+4 정의 명확 (52 brief v1.1 답습). **Layer 통합 PASS 발효 = R-S1 정정 미종속** (MVP-2 PASS 가 종속, B-8 답습 "평가 의무" framing).
docs/phase0/mvp2-layer-124-pass-activation-brief.md:187:→ **R-S1 = Layer 통합 PASS 발효 비차단** (MVP-2 PASS 전 hard gate, 별도 cycle). 본 cycle = 평가 한정 (N-4: ADR-011 §2.3 #4 line 113 "의존성 변경 → R-2/R-6 재실행" cross-ref — rfc8785/jcs = Q1 합의 채택이므로 본 cycle trigger 발화 0).
docs/phase0/mvp2-layer-124-pass-activation-brief.md:204:| 4 | 권위 chain 다중 source 손상 | ⚠️ 부분 | R-S1 (RT-γ-6 평가 한정) |
docs/phase0/mvp2-layer-124-pass-activation-brief.md:213:## §7 PASS 발효 권고 + 조건
docs/phase0/mvp2-layer-124-pass-activation-brief.md:215:⭐ **권고 = Layer 1+2+4 통합 PASS 발효 APPROVE WITH CONDITIONS**:
docs/phase0/mvp2-layer-124-pass-activation-brief.md:218:2. **조건 처리 상태**:
docs/phase0/mvp2-layer-124-pass-activation-brief.md:220:   - (C-2) Layer 2a denyNonFastForwards DEFER 명문 (2b operative 충족 근거) — 비례 보안 답습 (잔여 문서화 조건)
docs/phase0/mvp2-layer-124-pass-activation-brief.md:222:3. **R-S1 = Layer 통합 PASS 비차단** (MVP-2 PASS 전 hard gate, 별도 cycle, §5).
docs/phase0/mvp2-layer-124-pass-activation-brief.md:225:→ **PASS 발효 자격 = (a)~(d) 충족 (C-1 완료) + (e2) 합의 APPROVE + 사용자 명시 + (C-2) 2a DEFER 명문**.
docs/phase0/mvp2-layer-124-pass-activation-brief.md:231:§0.2 답습 (14). 추가: MVP-2 PASS 자동 선언 0 / GP-2 PASS 합산 0 / denyNonFastForwards 자동 활성화 0 / R-S1 자동 정정 0 / Layer 3+5 진입 0 / 자동 후속 cycle 0.
docs/phase0/mvp2-layer-124-pass-activation-brief.md:238:2. (C-1) timestamp fixture 보강 (PASS 발효 조건 또는 후속 자율)
docs/phase0/mvp2-layer-124-pass-activation-brief.md:239:3. **MVP-2 Implementation Evidence PASS 발효 합의** (Layer 통합 PASS + GP-2 PASS + R-S1 hard gate 후 별도, 32 entry 답습)
docs/phase0/mvp2-layer-124-pass-activation-brief.md:240:4. R-S1 cross-reference 정정 cycle (MVP-2 PASS 전 hard gate 3 옵션)
docs/phase0/mvp2-layer-124-pass-activation-brief.md:247:- ADR-011 §2.1 (a)~(e) — `docs/decisions/ADR-011-means-vs-ends-redaction.md`
docs/phase0/mvp2-layer-124-pass-activation-brief.md:262:| P-1 | 본 brief 가 PASS 발효를 *기정사실화* | 발효 = 합의 APPROVE + 사용자 명시 후 (§0.2 #1 + §9) |
docs/phase0/mvp2-layer-124-pass-activation-brief.md:263:| P-2 | evidence gap (timestamp fixture / 2a DEFER) 은폐 | §2.5 + §4 명시 (honest matrix, 57 (β) B-1 cascade 교훈 — 시제 주장 over-claim 방지) |
docs/phase0/mvp2-layer-124-pass-activation-brief.md:264:| P-3 | 2a DEFER 가 Layer 2 충족 *과대* | §2.2 + §4.1 = 2b operative 충족 근거 명시, 2a = 컨테이너 배포 trigger 시점 |
docs/phase0/mvp2-layer-124-pass-activation-brief.md:266:| P-5 | timestamp fixture gap 을 BLOCKING vs 자율 보강 판단 | §7 (C-1) 조건 명시, 풀 3+1 판정 위임 |
docs/phase0/mvp2-layer-124-pass-activation-brief.md:267:| P-6 | R-S1 RT-γ-6 = Layer 통합 PASS 차단 오해 | §5 = MVP-2 PASS 전 hard gate (Layer 통합 PASS 비차단), B-8 "평가 의무" 답습 |
docs/phase0/mvp2-layer-124-pass-activation-brief.md:275:본 v1.1 = `docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass-activation.md` 답습 1pass 흡수 (별도 v2 cycle 0, ceremony-inflation 차단, 52/55/57 동형). **4 source 전원 APPROVE WITH CONDITIONS — evidence 실증 (over-claim 0)**.
docs/phase0/mvp2-layer-124-pass-activation-brief.md:280:| B-2 | ADR-011 §2.1 = (a)~(d), (e2) = ADR-012 §4 확장 (권위 전도) | Agent B R-B-1 | §3 header + §10 |
docs/phase0/mvp2-layer-124-pass-activation-brief.md:281:| B-3 | 2a denyNonFastForwards = non-bare clone no-op (DEFER 강화) | Agent C R-C-1 | §2.2 + §4.1 |
docs/phase0/mvp2-layer-124-pass-activation-brief.md:282:| N-1 | 2a DEFER append-only ends 이중 cover (2b + rewrite-defense CI) | Agent B + C + codex | §2.2 + §4.1 |
docs/phase0/mvp2-layer-124-pass-activation-brief.md:293:**다음 단계**: SESSION + INDEX commit + push → 본 cycle 합의 발효 (APPROVE WITH CONDITIONS 4 source) → **Layer 1+2+4 통합 PASS 발효 (e2)**. 후속: MVP-2 Implementation Evidence PASS 발효 합의 (Layer 통합 PASS + GP-2 PASS + R-S1 hard gate) = 사용자 명시 별도 cycle.
docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass-activation.md:9:> **입력**: Agent A (구현 분석가, filesystem+CI direct) + Agent B (품질/안전성, 권위+means-vs-ends) + Agent C (대안 탐색) + codex (OpenAI gpt-5.5, cross-vendor blind) — 3 Agent 병렬 독립 + codex 독립
docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass-activation.md:17:| Agent A (구현 분석가) | **APPROVE WITH CONDITIONS** | 1 (R-A-1) | evidence 전원 실증 (over-claim 0, β cycle 재발 0), pytest 152 pass, 4 actual run success direct verify. citation `6ebc634` 부정확 |
docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass-activation.md:18:| Agent B (품질/안전성) | **APPROVE WITH CONDITIONS** | 1 (R-B-1) | 2a DEFER = hole 아님 (Layer 2 = 4 means 동시, ends 2b+rewrite-defense CI 이중 cover). ADR-011 §2.1 (a)~(e) 권위 전도 |
docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass-activation.md:19:| Agent C (대안 탐색) | **APPROVE WITH CONDITIONS** | 1 (R-C-1) | 2a denyNonFastForwards = non-bare clone no-op. 발효 형태 APPROVE WITH CONDITIONS = 32 entry 일관 최선 (4 대안 기각) |
docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass-activation.md:20:| codex (cross-vendor) | **APPROVE WITH CONDITIONS** | 0 | repo/CI direct verify 정합. 2a DEFER 비차단 + "4 G4" wording + Layer 5 framing 권고 |
docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass-activation.md:22:→ **Reviewer 통합 verdict = APPROVE WITH CONDITIONS** (4 source 전원 동일 — PASS 발효 최강 consensus). BLOCKING = 3 단독 발견 (각기 다름, 문서 정밀화 한정 — evidence/CI 실증 무결) → **brief v1.1 1pass 흡수 후 Layer 1+2+4 통합 PASS 발효**.
docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass-activation.md:33:| **B-2** | **ADR-011 §2.1 (a)~(e2) 권위 전도** | Agent B R-B-1 | ADR-011 §2.1 = (a)~(d) 4조건만 (line 52~61 verbatim). "(e) 합의 APPROVE" = ADR-012 §4 "(a)~(d)+(e) 5조건 답습" 확장 패턴. brief §0.3 정확 ("(a)~(d) 모법 + (e) 후속") but §3 header + §10 cross-ref 모법 과장 (β B-3/B-4 동형) | §3 header + §10 → §0.3 framing 통일 ("(a)~(d) 모법 + (e2) ADR-012 §4 확장") |
docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass-activation.md:34:| **B-3** | **2a denyNonFastForwards = non-bare clone no-op** | Agent C R-C-1 | 본 repo = 비-bare 작업 clone (`is-bare`=false), push 대상 = GitHub. `receive.denyNonFastForwards` = push *받는* repo (bare/server) 에서만 작동 → 본 clone 활성화 = **no-op (효과 0, "영향 최소" 아님)**. operative 보호 = Layer 2b. **정정 = DEFER 강화** (no-op 이면 켤 이유 소멸) | §2.2 + §4.1 "per-repo = 영향 최소/ceremony" → "non-bare clone no-op, operative = 2b" 정정 |
docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass-activation.md:36:### §2.2 Consensus 권고 (multi-source — 2a DEFER 정당성 + wording)
docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass-activation.md:40:| N-1 ⭐ (2a DEFER 정당성 3-source 강화) | 2a DEFER = means-vs-ends 정합. **(B)** ADR-012 §2.3 Layer 2 = denyNonFastForwards/branch protection/pre-commit/CI **4 means 동시 열거** (단일 수단 종속 0), ends (append-only) = (1) branch protection allow_force_pushes/deletions false + enforce_admins true + (2) rewrite-defense.yml CI `non_fast_forward_detected`/`history_reorder_detected` 검출 **이중 cover**. **(C)** denyNonFastForwards no-op. **(codex)** 2b operative, "2a까지 충족" wording 회피 | §2.2 + §4.1 강화 (2b + rewrite-defense CI 이중 cover 명시, brief 가 2b 만 인용해 *과소* 주장 정정) |
docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass-activation.md:42:| N-3 (Layer 5 framing) | history-anchor-verifier.yml = 이름 "Layer 5 External Anchor" — Layer 2 history evidence 인용 시 "부분 답습" framing 유지 (Layer 5 PASS 진입 0) 1줄 명문 | codex + Agent C | §2.4 1줄 cross-ref (55 B-2 답습) |
docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass-activation.md:43:| N-4 | §5 R-S1 RT-γ-6 에 ADR-011 §2.3 #4 (line 113) cross-ref / enforce_admins evidence 추가 | Agent B | §5 + §2.3 보강 |
docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass-activation.md:52:- ✅ denyNonFastForwards 전 scope 미설정 (DEFER 정확)
docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass-activation.md:56:- ✅ scope 침입 0 (MVP-2 PASS / GP-2 PASS 합산 / denyNonFastForwards 활성화 / R-S1 정정 0)
docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass-activation.md:66:| B-2 | §3 header + §10 → "(a)~(d) 모법 + (e2) ADR-012 §4 확장" (§0.3 framing 통일) |
docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass-activation.md:67:| B-3 | §2.2 + §4.1 "per-repo = 영향 최소/ceremony" → "non-bare clone no-op, operative = 2b" (DEFER 강화) |
docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass-activation.md:68:| N-1 | §2.2 + §4.1 2a DEFER 정당성 강화 (2b branch protection + rewrite-defense CI 이중 cover) |
docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass-activation.md:70:| N-3 | §2.4 history-anchor-verifier "Layer 5" 이름 — "부분 답습" framing 1줄 (55 B-2) |
docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass-activation.md:82:| M-4 | 2a DEFER 보안 hole | 3 source (B 이중 cover + C no-op + codex 2b operative) = DEFER 정당 강화 (hole 아님) |
docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass-activation.md:84:| M-6 | 본 합의 = PASS 발효 자체 진입 (실 구현/MVP-2 PASS 확대) | 본 합의 = Layer 1+2+4 통합 PASS 발효 한정. MVP-2 PASS / GP-2 PASS / denyNonFastForwards 활성화 / R-S1 정정 0 |
docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass-activation.md:88:**본 합의 verdict = APPROVE WITH CONDITIONS (4 source 전원) → brief v1.1 1pass 흡수 (BLOCKING 3 + 권고 4) → Layer 1+2+4 통합 PASS 발효 (e2)**.
docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass-activation.md:90:**PASS 발효 효과**: G4 §4.4 Layer 1+2+4 통합 Implementation Evidence PASS 발효 (부분 답습 — Layer 3+5 scope 외). Layer 1 완전 + Layer 2 (2b operative + rewrite-defense CI, 2a DEFER 비례 보안) + Layer 4 (3 ledger workflow green + canonical/timestamp BLOCK). **MVP-2 Implementation Evidence PASS = Layer 통합 PASS + GP-2 PASS + R-S1 hard gate 후 별도 cycle**.

exec
/bin/bash -lc "nl -ba docs/phase0/mvp2-layer-124-pass-activation-brief.md | sed -n '90,180p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
    90	| Evidence | 상태 | 출처 |
    91	|---------|------|------|
    92	| E-PASS-1: hash chain PASS fixture rc=0 (× 2) | ✅ | `g4-hash-chain.yml:182` PASS fixture step (minimal_chain + roundtrip_t2_strict), 58 actual run `26557460199` green |
    93	| E-PASS-2: violation_type 검출 actual run | ✅ | `g4-hash-chain.yml:197` FAIL fixture (prev_hash_mismatch + hash_recalculation + genesis_mismatch + schema_missing_field), 58 entry violation_type 정밀화 (HISTORY_REWRITE Layer 1 제거 → 3 Layer-1 type + schema) |
    94	| E-PASS-3: canonical JSON sha256 동등성 | ✅ | corpus 회귀 Primary 1 (rfc8785) + Primary 2 (jcs) byte+sha256 + jq fallback equivalence (`tests/canonical/` 72 files / 8 카테고리) + NaN/Inf reject |
    95	| E-PASS-4: genesis hash 첫 entry | ✅ | `compute_genesis_hash` + genesis_mismatch fixture |
    96	
    97	→ **Layer 1 = 완전 충족** (PoC 시제 + actual run green + 58 violation_type 정밀화).
    98	
    99	### §2.2 Layer 2a — local denyNonFastForwards ⚠️ DEFER
   100	
   101	| Evidence | 상태 | 출처 |
   102	|---------|------|------|
   103	| E-PASS-5: denyNonFastForwards 활성화 + force-push reject PoC | ⚠️ **DEFER** | 57/58 사용자 비례 보안 결정. ⭐ **B-3 정정**: `receive.denyNonFastForwards` = push *받는* repo (bare/server) 에서만 작동 — 본 repo = 비-bare 작업 clone (push 대상 = GitHub) → 본 clone 활성화 = **no-op (효과 0, "영향 최소" 아님)**. operative append-only 보호 = Layer 2b (§2.3) + rewrite-defense.yml CI (§2.4) |
   104	
   105	→ **Layer 2a = DEFER** (B-3: 본 clone no-op, 켤 이유 소멸). ⭐ **N-1 — Layer 2 append-only ends 이중 cover** (ADR-012 §2.3 Layer 2 = denyNonFastForwards/branch protection/pre-commit/CI **4 means 동시 열거**, 단일 수단 종속 0): (1) Layer 2b branch protection (allow_force_pushes/deletions false + enforce_admins true) + (2) rewrite-defense.yml Layer 4 CI (`non_fast_forward_detected` / `history_reorder_detected` 검출, actual run green). 2a 가 막으려는 시나리오를 2 layer 가 이미 cover. 2a = 실 bare/server 배포 trigger 시점 (별도, [[feedback_proportionate_security_personal_tool]]).
   106	
   107	### §2.3 Layer 2b — remote branch protection ✅
   108	
   109	| Evidence | 상태 | 출처 |
   110	|---------|------|------|
   111	| E-PASS-7: branch protection rule actual state | ✅ | gh api main protection 8 contexts = `["guard","verify","feasibility","scan","enforce","defense","validate","bypass-detect"]` + allow_force_pushes false + allow_deletions false + **enforce_admins true** (N-4, 43 entry 답습) |
   112	
   113	### §2.4 Layer 2 — history (rewrite/deletion 검출) ✅
   114	
   115	| Evidence | 상태 | 출처 |
   116	|---------|------|------|
   117	| E-PASS-6: base branch JSONL line deletion/rewrite 감지 actual run | ✅ | `rewrite-defense.yml` (58 actual run `26557460227` green) + `history-anchor-verifier.yml` (58 actual run `26557460197` green) + FAIL fixtures 8 (append_only force_push/reorder + line_regression deletion/rewrite + anchor full_rewrite/middle_deletion/substitution/tail_truncation) |
   118	
   119	⚠️ **N-3 (Layer 5 framing)**: `history-anchor-verifier.yml` 은 이름이 "Layer 5 External Anchor Verifier" 이나, 본 cycle 은 이를 **Layer 2 history rewrite 검출 보조 evidence 로만 인용** (Layer 5 External anchor *PASS 진입 발효 0*). "부분 답습" framing 유지 (Layer 3+5 scope 외, 55 entry B-2 답습).
   120	
   121	→ **Layer 2 = 충족** (2b operative + rewrite-defense CI 이중 cover + history 검출 actual run green, 2a DEFER no-op 문서화).
   122	
   123	### §2.5 Layer 4 — CI 회귀 검증 (MANDATORY) ✅ 부분
   124	
   125	| Evidence | 상태 | 출처 |
   126	|---------|------|------|
   127	| E-PASS-8: 4 G4 workflow actual run PASS | ✅ 3/4 | 58 entry: g4-hash-chain `26557460199` + rewrite-defense `26557460227` + history-anchor-verifier `26557460197` 전원 green. r2-canary (R-6/R-2 canary) = path 미트리거 (별도 §4.3) |
   128	| E-PASS-9: canonical 위반 BLOCK | ✅ | corpus 회귀 Primary 1/2 byte+sha256 mismatch BLOCK + NaN/Inf reject (RFC 8785 §3.2.2.2) |
   129	| E-PASS-10: timestamp monotonicity 위반 BLOCK | ✅ | 코드 검출 (`jsonl_hash_chain.py:224` monotonicity_violation) + **C-1 보강 (59 entry): `timestamp_monotonicity.jsonl` fixture 추가 (valid chain + ts 역행) → g4-hash-chain.yml 5 violation_type cover, actual run `26557936920` green** |
   130	| E-PASS-11: R-6 workflow 확장 step actual run | ⚠️ W-F | W-F (기존 보존, 신규 step 0) 답습 — 별도 R-6 step 미추가. Layer 4 회귀 = 3 ledger workflow 가 충족 |
   131	
   132	→ **Layer 4 = 충족** (3 ledger workflow green + canonical BLOCK ✅ + timestamp monotonicity ✅ C-1 보강, r2-canary 미트리거는 R-6/R-2 영역).
   133	
   134	### §2.6 통합 evidence ((γ-c) 의무 3 — 동시 발효, Layer subsection 분리 유지)
   135	
   136	| Evidence | 상태 |
   137	|---------|------|
   138	| E-PASS-12: 통합 evidence (Layer subsection 분리 명시) | ✅ 본 §2 (Layer 1/2a/2b/2/4 subsection 분리, 합산 0) |
   139	| E-PASS-13: 합의 보고서 commit | ⏳ 본 cycle 합의 |
   140	| E-PASS-14: 외부 LLM 1+ (cross-vendor) | ⏳ 본 cycle codex |
   141	| E-PASS-15: R-S1 정정 자격 평가 (RT-γ-6) | §5 |
   142	
   143	---
   144	
   145	## §3 PASS 발효 자격 매핑 — ADR-011 §2.1 (a)~(d) 모법 + (e2) ADR-012 §4 확장 (B-2 정정)
   146	
   147	> ⚠️ **B-2**: ADR-011 §2.1 = **(a)~(d) 4조건만** (line 52~61). "(e) 합의 APPROVE" = ADR-012 §4 "(a)~(d) + (e) 5조건 답습" 확장 패턴 (§0.3 framing). 본 §3 = (a)~(d) ADR-011 모법 + (e2) ADR-012 §4 확장 매핑.
   148	
   149	| # | 조건 | Layer 1 | Layer 2 (2a+2b) | Layer 4 | 통합 |
   150	|---|------|------|------|------|----|
   151	| (a) | 동등 이상 보안 결과 | ✅ middle tampering 차단 (3 violation type) | ✅ 2b force push/delete 차단 + history 재작성 차단 (2a DEFER, 2b operative) | ✅ CI 회귀 (canonical BLOCK + timestamp monotonicity, C-1 보강) | Layer 1+2+4 통합 (subsection 분리) |
   152	| (b) | 격리 환경 PoC 실증 | ✅ jsonl_hash_chain + fixtures | ✅ 2b actual state + history fixtures 8 | ✅ 3 G4 actual run green | 통합 (합산 0) |
   153	| (c) | ADR/SDD 권위 명시 | ✅ G4 §4.4.1 + ADR-012 §2.3/§2.8 | ✅ 동상 | ✅ 동상 | ✅ |
   154	| (d) | 자동 회귀 검증 경로 | ✅ g4-hash-chain CI | ✅ rewrite-defense + history-anchor CI | ✅ 3 ledger workflow CI green | ✅ |
   155	| **(e2)** | **PASS 발효 합의 APPROVE** | ⏳ 본 cycle | ⏳ 본 cycle | ⏳ 본 cycle | ⏳ **본 cycle 풀 3+1 + 외부 LLM + 사용자 명시** |
   156	
   157	→ **(a)~(d) 충족 = Layer 1 완전 / Layer 2 충족 (2a DEFER 문서화, 2b operative) / Layer 4 충족 (C-1 timestamp 보강 완료, r2-canary = R-6/R-2 영역)**. (e2) = 본 cycle 합의.
   158	
   159	---
   160	
   161	## §4 gap / DEFER 처리
   162	
   163	### §4.1 Layer 2a denyNonFastForwards = DEFER (B-3 + N-1 정정)
   164	
   165	- ⭐ **B-3**: `receive.denyNonFastForwards` = push *받는* repo (bare/server) 에서만 작동. 본 repo = 비-bare 작업 clone, push 대상 = GitHub → 본 clone 활성화 = **no-op (효과 0)**. "per-repo = 영향 최소/ceremony" framing (55 §4.4.2) 부정확 → 정정 = **켤 이유 소멸** (no-op), DEFER 강화.
   166	- ⭐ **N-1 — append-only ends 이중 cover** (단일 수단 종속 0, ADR-012 §2.3 Layer 2 = 4 means 동시): (1) Layer 2b branch protection (allow_force_pushes/deletions false + enforce_admins true, gh api verify) + (2) rewrite-defense.yml Layer 4 CI (`non_fast_forward_detected`/`history_reorder_detected` 검출, actual run green). 2a 시나리오를 2 layer 가 cover.
   167	- **PASS 발효 영향**: Layer 2 append-only *결과(ends)* = 2b + rewrite-defense CI 이중 충족. 2a = 실 bare/server 배포 시점 (별도 trigger, no-op 이므로 본 clone 무관). PASS 발효 = ends 충족 + 2a DEFER no-op 명문.
   168	
   169	### §4.2 E-PASS-10 timestamp monotonicity fixture (C-1) — ✅ 보강 완료 (합의 전 미리 보강, 사용자 명시)
   170	
   171	- 코드 검출 확인 (`validate_chain:224` — `cur_ts < prev_ts` → monotonicity_violation).
   172	- **C-1 보강 완료 (59 entry, commit `4c48099`)**: `tests/fixtures/jsonl_ledger/fail/timestamp_monotonicity.jsonl` 추가 (valid chain genesis/prev_hash/entry hash + ts 역행 → monotonicity_violation 단독) + g4-hash-chain.yml FAIL fixture step 4→5 violation_type cover (W-F 기존 workflow 內 보강) + TDD test (test_validate_chain_monotonicity_violation). **actual run `26557936920` green** → E-PASS-10 CI 입증.
   173	
   174	### §4.3 r2-canary (E-PASS-11) 미트리거
   175	
   176	- r2-canary = R-6/R-2 redaction canary (paths = docker/r4-1-poc, docker/r2-poc, canary docs). Layer 1+2+4 *ledger* 검증 핵심 아님 (3 ledger workflow 가 Layer 4 충족).
   177	- **권고**: r2-canary 는 GP-2 영역 (R-3) 또는 workflow_dispatch 로 별도 actual run. 본 Layer 통합 PASS 영향 = 3 ledger workflow 로 충족.
   178	
   179	---
   180	

exec
/bin/bash -lc "nl -ba docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass-activation.md | sed -n '1,180p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
     1	# 3+1 합의 통합 보고서 — Layer 1+2+4 통합 PASS 발효 (e2) (59 entry)
     2	
     3	> **작성**: 2026-05-28 (Reviewer 통합)
     4	>
     5	> **대상**: `docs/phase0/mvp2-layer-124-pass-activation-brief.md` (v1)
     6	>
     7	> **합의 형태**: 풀 3+1 + 외부 LLM 1+ (cross-vendor codex gpt-5.5) — 4 source
     8	>
     9	> **입력**: Agent A (구현 분석가, filesystem+CI direct) + Agent B (품질/안전성, 권위+means-vs-ends) + Agent C (대안 탐색) + codex (OpenAI gpt-5.5, cross-vendor blind) — 3 Agent 병렬 독립 + codex 독립
    10	
    11	---
    12	
    13	## §1 4 source verdict 요약
    14	
    15	| source | verdict | BLOCKING | 핵심 |
    16	|--------|---------|---------|------|
    17	| Agent A (구현 분석가) | **APPROVE WITH CONDITIONS** | 1 (R-A-1) | evidence 전원 실증 (over-claim 0, β cycle 재발 0), pytest 152 pass, 4 actual run success direct verify. citation `6ebc634` 부정확 |
    18	| Agent B (품질/안전성) | **APPROVE WITH CONDITIONS** | 1 (R-B-1) | 2a DEFER = hole 아님 (Layer 2 = 4 means 동시, ends 2b+rewrite-defense CI 이중 cover). ADR-011 §2.1 (a)~(e) 권위 전도 |
    19	| Agent C (대안 탐색) | **APPROVE WITH CONDITIONS** | 1 (R-C-1) | 2a denyNonFastForwards = non-bare clone no-op. 발효 형태 APPROVE WITH CONDITIONS = 32 entry 일관 최선 (4 대안 기각) |
    20	| codex (cross-vendor) | **APPROVE WITH CONDITIONS** | 0 | repo/CI direct verify 정합. 2a DEFER 비차단 + "4 G4" wording + Layer 5 framing 권고 |
    21	
    22	→ **Reviewer 통합 verdict = APPROVE WITH CONDITIONS** (4 source 전원 동일 — PASS 발효 최강 consensus). BLOCKING = 3 단독 발견 (각기 다름, 문서 정밀화 한정 — evidence/CI 실증 무결) → **brief v1.1 1pass 흡수 후 Layer 1+2+4 통합 PASS 발효**.
    23	
    24	---
    25	
    26	## §2 cross-validation 매트릭스
    27	
    28	### §2.1 단독 BLOCKING (Reviewer raw verify 격상 — 모두 문서 정밀화, 발효 비차단)
    29	
    30	| # | BLOCKING | source | 근거 (Reviewer verify) | 정정 |
    31	|---|----------|--------|---------------------|------|
    32	| **B-1** | citation "58 실 구현 = `6ebc634`" 부정확 | Agent A R-A-1 | `6ebc634` = docs(session) CI 증거 기록 commit. 실 구현 commit = `052e583` (3 actual run headSha = `052e583`). C-1 = `4c48099` | §0.3 + §1.1 citation `052e583` 정정 |
    33	| **B-2** | **ADR-011 §2.1 (a)~(e2) 권위 전도** | Agent B R-B-1 | ADR-011 §2.1 = (a)~(d) 4조건만 (line 52~61 verbatim). "(e) 합의 APPROVE" = ADR-012 §4 "(a)~(d)+(e) 5조건 답습" 확장 패턴. brief §0.3 정확 ("(a)~(d) 모법 + (e) 후속") but §3 header + §10 cross-ref 모법 과장 (β B-3/B-4 동형) | §3 header + §10 → §0.3 framing 통일 ("(a)~(d) 모법 + (e2) ADR-012 §4 확장") |
    34	| **B-3** | **2a denyNonFastForwards = non-bare clone no-op** | Agent C R-C-1 | 본 repo = 비-bare 작업 clone (`is-bare`=false), push 대상 = GitHub. `receive.denyNonFastForwards` = push *받는* repo (bare/server) 에서만 작동 → 본 clone 활성화 = **no-op (효과 0, "영향 최소" 아님)**. operative 보호 = Layer 2b. **정정 = DEFER 강화** (no-op 이면 켤 이유 소멸) | §2.2 + §4.1 "per-repo = 영향 최소/ceremony" → "non-bare clone no-op, operative = 2b" 정정 |
    35	
    36	### §2.2 Consensus 권고 (multi-source — 2a DEFER 정당성 + wording)
    37	
    38	| # | 권고 | source | v1.1 흡수 |
    39	|---|------|--------|---------|
    40	| N-1 ⭐ (2a DEFER 정당성 3-source 강화) | 2a DEFER = means-vs-ends 정합. **(B)** ADR-012 §2.3 Layer 2 = denyNonFastForwards/branch protection/pre-commit/CI **4 means 동시 열거** (단일 수단 종속 0), ends (append-only) = (1) branch protection allow_force_pushes/deletions false + enforce_admins true + (2) rewrite-defense.yml CI `non_fast_forward_detected`/`history_reorder_detected` 검출 **이중 cover**. **(C)** denyNonFastForwards no-op. **(codex)** 2b operative, "2a까지 충족" wording 회피 | §2.2 + §4.1 강화 (2b + rewrite-defense CI 이중 cover 명시, brief 가 2b 만 인용해 *과소* 주장 정정) |
    41	| N-2 (Layer 4 "4 G4" wording) | "4 G4 workflow actual run PASS" 표 제목 = 과장 (실 3/4, r2-canary = R-6/R-2 영역). wording 재사용 금지 | codex + Agent A | §2.5 "3 ledger workflow (r2-canary = R-6/R-2 별도)" 명확화 |
    42	| N-3 (Layer 5 framing) | history-anchor-verifier.yml = 이름 "Layer 5 External Anchor" — Layer 2 history evidence 인용 시 "부분 답습" framing 유지 (Layer 5 PASS 진입 0) 1줄 명문 | codex + Agent C | §2.4 1줄 cross-ref (55 B-2 답습) |
    43	| N-4 | §5 R-S1 RT-γ-6 에 ADR-011 §2.3 #4 (line 113) cross-ref / enforce_admins evidence 추가 | Agent B | §5 + §2.3 보강 |
    44	
    45	### §2.3 4 source 정합 확인 (BLOCKING 아님 — evidence 실증)
    46	
    47	- ✅ **evidence 전원 실증, over-claim 0** (Agent A/B/C/codex direct verify — β cycle "L-1 stdlib" 거짓 재발 0)
    48	- ✅ actual run 4개 direct: C-1 `26557936920` (headSha `4c48099`, 5 violation_type cover step success) + 58 `26557460199`/`26557460227`/`26557460197` (headSha `052e583`) 전원 success
    49	- ✅ `timestamp_monotonicity.jsonl` 실재 (valid chain + ts 역행 → monotonicity_violation 단독)
    50	- ✅ ViolationType 3종 (HISTORY_REWRITE 부재 — 58 제거 확인, β dead enum 우려 해소)
    51	- ✅ branch protection 8 contexts + force push/delete false + enforce_admins true
    52	- ✅ denyNonFastForwards 전 scope 미설정 (DEFER 정확)
    53	- ✅ Layer 2 history fixtures 8 + canonical 72 files + pytest 152 pass
    54	- ✅ (γ-c) 특화 의무 4 전원 정합 (Layer subsection evidence 합산 0 + "부분 답습" framing + 통합 동시 + RT-γ-6 §5 수행)
    55	- ✅ PASS 발효 (e2) vs 진입 권한 (e1) 명확 구분
    56	- ✅ scope 침입 0 (MVP-2 PASS / GP-2 PASS 합산 / denyNonFastForwards 활성화 / R-S1 정정 0)
    57	- ✅ 발효 형태 = 32 entry MVP-1 PASS 발효 일관 (Agent C 4 대안 기각)
    58	
    59	---
    60	
    61	## §3 v1.1 흡수 매트릭스 (BLOCKING 3 + 권고 4 1pass)
    62	
    63	| 흡수 | brief v1.1 정정 |
    64	|------|---------------|
    65	| B-1 | §0.3 + §1.1 citation `6ebc634` → `052e583` (실 구현) + `4c48099` (C-1) |
    66	| B-2 | §3 header + §10 → "(a)~(d) 모법 + (e2) ADR-012 §4 확장" (§0.3 framing 통일) |
    67	| B-3 | §2.2 + §4.1 "per-repo = 영향 최소/ceremony" → "non-bare clone no-op, operative = 2b" (DEFER 강화) |
    68	| N-1 | §2.2 + §4.1 2a DEFER 정당성 강화 (2b branch protection + rewrite-defense CI 이중 cover) |
    69	| N-2 | §2.5 "3 ledger workflow (r2-canary = R-6/R-2 영역)" |
    70	| N-3 | §2.4 history-anchor-verifier "Layer 5" 이름 — "부분 답습" framing 1줄 (55 B-2) |
    71	| N-4 | §5 ADR-011 §2.3 #4 cross-ref + enforce_admins evidence |
    72	
    73	---
    74	
    75	## §4 메타 자기진단 (Reviewer)
    76	
    77	| # | 위험 | 처리 |
    78	|---|------|----|
    79	| M-1 | 3 Agent 병렬 독립 미보장 | A/B/C 상호 미참조 + codex cross-vendor blind |
    80	| M-2 | cross-vendor 미충족 | codex = OpenAI gpt-5.5, Agent = Claude (헌법 5조-2) |
    81	| M-3 | PASS 발효 강행 (evidence 불충분) | **4 source 전원 evidence 실증 + over-claim 0** — actual run/fixture/contexts direct verify. BLOCKING = 문서 정밀화 한정 (발효 비차단) |
    82	| M-4 | 2a DEFER 보안 hole | 3 source (B 이중 cover + C no-op + codex 2b operative) = DEFER 정당 강화 (hole 아님) |
    83	| M-5 | ceremony-inflation (v2 cycle) | 1pass 흡수 (52/55/57 동형), v2 cycle 0 |
    84	| M-6 | 본 합의 = PASS 발효 자체 진입 (실 구현/MVP-2 PASS 확대) | 본 합의 = Layer 1+2+4 통합 PASS 발효 한정. MVP-2 PASS / GP-2 PASS / denyNonFastForwards 활성화 / R-S1 정정 0 |
    85	
    86	---
    87	
    88	**본 합의 verdict = APPROVE WITH CONDITIONS (4 source 전원) → brief v1.1 1pass 흡수 (BLOCKING 3 + 권고 4) → Layer 1+2+4 통합 PASS 발효 (e2)**.
    89	
    90	**PASS 발효 효과**: G4 §4.4 Layer 1+2+4 통합 Implementation Evidence PASS 발효 (부분 답습 — Layer 3+5 scope 외). Layer 1 완전 + Layer 2 (2b operative + rewrite-defense CI, 2a DEFER 비례 보안) + Layer 4 (3 ledger workflow green + canonical/timestamp BLOCK). **MVP-2 Implementation Evidence PASS = Layer 통합 PASS + GP-2 PASS + R-S1 hard gate 후 별도 cycle**.
    91	
    92	**본 합의 발효 = brief v1.1 commit + SESSION + INDEX commit + push 후** (단계별 합의 cycle 답습).

exec
/bin/bash -lc 'rg -n "''^## 4|'"\\(a\\)|\\(e\\)|5조건|ADR-011 §2.1\" docs/decisions/ADR-012-evidence-ledger-protection.md | head -80" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
6:**상위 권위**: 헌법 제8조 (보안), 헌법 제5조 (Provider Liquidity, 관용), ADR-011 §2.1 (수단/목적 분리), §2.3 (Hermes ≠ root of trust), §2.4 (T1/T2/T3)
64:| **ADR-011 §2.1 (수단/목적 분리)** | 본 ADR 자체가 Evidence 무결성 = 목적, hash chain + signed/append commit + JCS = 수단. (a)~(d) + (e) 5조건 답습 (§4) |
337:| (a) | 1인 호스트 침해 | **약** — host 전체 침해 시 모든 layer 우회 | Layer 5 external snapshot (월 1회) |
339:| (c) | Git history rewrite | **중** — Layer 2~4 차단, 그러나 host 권한 상승 시 force push 가능 | (a) 동일 + Layer 5 |
341:| (e) | External LLM response 위조 | **약** — vendor API key / signed response 부재 시 검증 부족 | 원칙 7 (`agent="user"` 강제) + Layer 3 권장 |
436:## 4. ADR-011 §2.1 (a)~(d) + (e) 5조건 답습 (Means-vs-Ends Pattern)
438:본 ADR-012 는 ADR-011 §2.1 5조건 패턴 답습 (수단/목적 분리):
440:### (a) 동등 이상의 보안 결과 (Agent B Gap-21)
478:### (e) 합의 APPROVE
557:- ADR-011 §2.1 (a)~(d) + (e) 5조건 패턴 답습 — 미래 다른 비협상 조항 해석에도 적용 가능
563:- 본 ADR-012 의 (a)~(e) 5조건 검증 부담 — 의도된 안전 비용
585:| 수단/목적 분리 | ADR-011 §2.1 (a)~(d) + (e) | §4 (a)~(e) 5조건 답습 — (a) 비교표 / (b) Implementation 영역 / (c) ADR-012 자체 / (d) R-6 답습 확장 / (e) 본 합의 APPROVE | **HIGH** ((b) 별도) |
655:4. ADR-011 §2.1 + §2.3 + §2.4 cross-reference 답습

codex
**Verdict: REVISE**

**BLOCKING finding**

1. **`(a) 동등 이상 보안 결과 ✅` 및 “GP-2 송신 redaction PASS”는 현재 evidence로는 over-claim입니다.**

`(d)` 격상은 정당합니다. `.github/workflows/secret-hygiene-egress-redaction.yml`의 D-2 step은 실제로 `scan-log` redaction pass/fail을 실행하고, `gh run view 26517803107`도 `success`, `headSha=4fec6485`로 확인됩니다. 현재 HEAD `0f49eb9` 기준으로 workflow/scanner/redaction fixture diff도 없습니다.

하지만 `(a)`는 별개입니다. [governance-preconditions.md](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/governance-preconditions.md:451)는 GP-2 Exit `(a)`를 “Hermes native redaction Tier-1 catalog 적용 검증 + P1 facade redaction filter 검증”으로 둡니다. 현재 repo 상태는 `agent/redact.py` 부재, [facade.py](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:31)는 placeholder입니다. [redaction-pattern-equivalence.md](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/redaction-pattern-equivalence.md:33)도 비교/문서화 산출이지 Hermes 안전성 선언이 아니며, 같은 문서가 Hermes safety 선언 금지를 명시합니다.

따라서 R-3 detection green만으로 “GP-2 egress redaction PASS 4/4”를 닫으면 prevention 부재를 detection으로 대체하는 꼴입니다. 정정은 다음 중 하나여야 합니다.

- “GP-2 R-3/D-2 자동 회귀 검증 PASS”로 scope를 낮춘다.
- 또는 `(a)`를 `⚠️ partial / condition`으로 낮추고, R-1 Hermes runtime redaction 적용 검증 및 R-2 facade real 검증을 full GP-2 PASS의 선행 조건으로 둔다.

**Non-blocking**

- 51 audit의 `(d) gap` → `✅` 정정 자체는 over-claim이 아닙니다. workflow D-2, scanner `--mode scan-log`, fixtures, actual run이 일치합니다.
- R-5 base64 evasion은 known limitation으로 잘 분리되어 있습니다.
- ADR-011 §2.1이 `(a)~(d)` 4조건이고, `(e2)`를 ADR-012 §4 확장으로 두는 framing은 59 cycle 정정과 정합합니다.
- MVP-2 PASS, R-1 import, R-2 facade real, R-S1 정정, secret_scanner/workflow 본문 변경은 brief 상 자동 발효하지 않도록 잘 금지되어 있습니다.

**NOTE**

`APPROVE WITH CONDITIONS`까지 가려면 조건 문구만으로는 부족합니다. 현재 제목과 evidence matrix가 “GP-2 PASS”를 이미 성립한 것처럼 읽히므로, full GP-2 PASS가 아니라 “R-3 detection evidence PASS”임을 명시적으로 낮춰야 합니다.
tokens used
91,747
**Verdict: REVISE**

**BLOCKING finding**

1. **`(a) 동등 이상 보안 결과 ✅` 및 “GP-2 송신 redaction PASS”는 현재 evidence로는 over-claim입니다.**

`(d)` 격상은 정당합니다. `.github/workflows/secret-hygiene-egress-redaction.yml`의 D-2 step은 실제로 `scan-log` redaction pass/fail을 실행하고, `gh run view 26517803107`도 `success`, `headSha=4fec6485`로 확인됩니다. 현재 HEAD `0f49eb9` 기준으로 workflow/scanner/redaction fixture diff도 없습니다.

하지만 `(a)`는 별개입니다. [governance-preconditions.md](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/governance-preconditions.md:451)는 GP-2 Exit `(a)`를 “Hermes native redaction Tier-1 catalog 적용 검증 + P1 facade redaction filter 검증”으로 둡니다. 현재 repo 상태는 `agent/redact.py` 부재, [facade.py](/home/delangi/문서/project/category/AI_development_tool/src/adapters/llm/facade.py:31)는 placeholder입니다. [redaction-pattern-equivalence.md](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/redaction-pattern-equivalence.md:33)도 비교/문서화 산출이지 Hermes 안전성 선언이 아니며, 같은 문서가 Hermes safety 선언 금지를 명시합니다.

따라서 R-3 detection green만으로 “GP-2 egress redaction PASS 4/4”를 닫으면 prevention 부재를 detection으로 대체하는 꼴입니다. 정정은 다음 중 하나여야 합니다.

- “GP-2 R-3/D-2 자동 회귀 검증 PASS”로 scope를 낮춘다.
- 또는 `(a)`를 `⚠️ partial / condition`으로 낮추고, R-1 Hermes runtime redaction 적용 검증 및 R-2 facade real 검증을 full GP-2 PASS의 선행 조건으로 둔다.

**Non-blocking**

- 51 audit의 `(d) gap` → `✅` 정정 자체는 over-claim이 아닙니다. workflow D-2, scanner `--mode scan-log`, fixtures, actual run이 일치합니다.
- R-5 base64 evasion은 known limitation으로 잘 분리되어 있습니다.
- ADR-011 §2.1이 `(a)~(d)` 4조건이고, `(e2)`를 ADR-012 §4 확장으로 두는 framing은 59 cycle 정정과 정합합니다.
- MVP-2 PASS, R-1 import, R-2 facade real, R-S1 정정, secret_scanner/workflow 본문 변경은 brief 상 자동 발효하지 않도록 잘 금지되어 있습니다.

**NOTE**

`APPROVE WITH CONDITIONS`까지 가려면 조건 문구만으로는 부족합니다. 현재 제목과 evidence matrix가 “GP-2 PASS”를 이미 성립한 것처럼 읽히므로, full GP-2 PASS가 아니라 “R-3 detection evidence PASS”임을 명시적으로 낮춰야 합니다.
