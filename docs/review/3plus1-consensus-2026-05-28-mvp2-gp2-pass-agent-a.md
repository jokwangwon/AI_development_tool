# 3+1 합의 — Agent A (구현 분석가) 검토: MVP-2 GP-2 송신 redaction PASS 발효 (e2)

> **검토 대상**: `docs/phase0/mvp2-gp2-pass-activation-brief.md` (v1)
> **관점**: "evidence가 실제인가?" — filesystem + CI 직접 inspection (다른 Agent/외부 LLM 미참조)
> **검토일**: 2026-05-28
> **검토자**: Agent A (구현 분석가)

---

## VERDICT: **APPROVE**

brief v1 의 (a)~(d) evidence 주장은 **전부 실측으로 사실 확인됨**. (β) cycle 의 "L-1 stdlib 시제 충족" over-claim 전례를 의식하여 핵심 (d) 격상 주장, run ID, 코드 불변, fixture 동작을 직접 verify 한 결과 **over-claim 0건**. BLOCKING 없음.

- **BLOCKING: 0건**
- **권고: 2건** (N-A-1, N-A-2)
- **NOTE: 3건** (NT-A-1, NT-A-2, NT-A-3)

---

## 1. 직접 verify 한 evidence (실측 raw 출력)

### 1.1 ⭐ (d) 핵심 격상 검증 — over-claim 아님

brief §2 (d): 51 audit `(d) ❌ gap` → `(d) ✅`. 근거 = secret-hygiene D-2 scan-log redaction step + run `26517803107` green + 코드 불변. **세 갈래 전부 검증.**

**(1) workflow 에 D-2 scan-log redaction step 실재 — ✅ 사실**

`grep` 결과 (`.github/workflows/secret-hygiene-egress-redaction.yml`):
```
165: - name: D-2 PASS redaction residual — scan-log redaction_pass/ (rc=0 + 0 잔존)
169:     python tools/secret_scanner.py --mode scan-log tests/fixtures/secret_hygiene/redaction_pass/
186: - name: D-2 FAIL redaction leak — scan-log redaction_fail/ (rc=1 + partial leak 검출)
190:     python tools/secret_scanner.py --mode scan-log tests/fixtures/secret_hygiene/redaction_fail/
```
D-2 PASS + D-2 FAIL 2개 step 실재. `--mode scan-log` 호출 실재.

**(2) run `26517803107` = success / 4fec6485 — ✅ 사실**

`gh run view 26517803107 --json conclusion,headSha,status,event`:
```json
{"conclusion":"success","headSha":"4fec64859831fb9bfade31819055070abd079244","status":"completed","event":"push"}
```
- conclusion = `success` (brief 주장 일치)
- headSha = `4fec6485...` (brief `4fec6485` 일치)
- event = `push` (empty/dispatch 가짜 run 아님 — 실 path 변경 push 발화)

**run 이 D-2 step 을 실제 실행했는가 (hollow run 아님)** — `gh run view --json jobs`:
```
scan -> success
    D-2 PASS redaction residual — scan-log redaction_pass/ (rc=0 + 0 잔존)  success
    D-2 FAIL redaction leak — scan-log redaction_fail/ (rc=1 + partial leak 검출)  success
```
→ D-2 step 2개가 실제로 실행되어 success. **빈 run / skip 아님 — 유효 evidence.**

**(3) 코드 불변 (49 entry `4fec6485` 이후) — ✅ 사실**

`git log 4fec6485..HEAD -- tools/secret_scanner.py .github/workflows/secret-hygiene-egress-redaction.yml tests/fixtures/secret_hygiene/`:
```
(empty — 0 commits)
```
→ scanner + workflow + fixtures 전부 `4fec6485` (현 HEAD `0f49eb9`) 까지 **변경 0건**. 최근 green run = 현 코드 유효 evidence 주장 성립.

**핵심 — "51 audit gap 표기 부정확" framing 검증 (P-3 self-flag 영역):**

brief 가 51 audit 의 `(d) ❌ gap` 을 "부정확 정정" 이라 주장 (§1.1 + §2 (d) + §10 P-3). 이게 사후 합리화인지 검증:
- workflow + D-2 step 생성 commit = `43c51ef` (**2026-05-10** 16:34, "ci(g2-gp3-gp2): add secret hygiene egress redaction workflow") — D-2 PASS redaction residual step 이 *최초 생성 commit* 부터 존재 (`git log -S "D-2 PASS redaction residual"` = `43c51ef` 단일).
- run `26517803107` headSha `4fec6485` = **2026-05-27** (D-2 green).
- 51 audit commit `f7ac61d` = **2026-05-28 09:49** (D-2 보다 **나중**).
- `git merge-base --is-ancestor 43c51ef f7ac61d` = YES, `--is-ancestor 4fec6485 f7ac61d` = YES.

→ **D-2 CI 가 51 audit 시점에 이미 17일 전 (5/10) 부터 operative + green 이었다.** 51 audit 가 "(d) gap, R-6 workflow 에 canary inject step *추가* 필요" (51 audit line 127) 라 적은 것이 부정확했던 것이 사실. brief 의 "52 entry PoC 시제 발견 동형" framing = **사후 합리화 아님, 실측 정당.** over-claim 아님.

### 1.2 (a) R-4 — ✅ 사실

`docs/architecture/redaction-pattern-equivalence.md` 실재 (29018 bytes). 내용 = 패턴 동등성:
- 제목 "Redaction Pattern Equivalence (R-4)", 상위 권위 "ADR-011 §2.1 (a) (대체 수단 동등 이상 보장 검증 의무)"
- 3-way 동등성 매트릭스 (Hermes / P1_REDACTOR / R-2 trigger UDF), Tier 1/2/3 gap 분류, Hermes `_PREFIX_PATTERNS` 35종 추출
- ADR-011 §7.3 "Hermes 안전성 선언 금지" 명문 준수
→ brief §2/§4 (a) "패턴 동등성" 주장 정확.

### 1.3 (b) PoC fixtures + 실행 — ✅ 사실 (직접 실행)

fixtures 실재: `redaction_pass/env_redacted.txt` (216B), `redaction_fail/partial_redact.txt` (260B) + `base64_evasion.txt` (514B).

**`.venv/bin/python tools/secret_scanner.py --mode scan-log redaction_pass/`:**
```
[PASS] mode=scan-log target=.../redaction_pass violations=0
rc=0
```
→ brief 주장 "rc=0 잔존 0" **일치.**

**`--mode scan-log redaction_fail/`:**
```
[FAIL] mode=scan-log target=.../redaction_fail violations=3
  partial_redact.txt:2: BL-2:prefix-baseline / T1-032:regex (sk-FAKE..., OPENAI_API_KEY=...)
  partial_redact.txt:4: T1-032:regex (GITHUB_TOKEN=ghp_FAKE...)
rc=1
```
→ brief 주장 "rc=1 leak 검출" **일치.** leak = `partial_redact.txt` 한정 (prefix-baseline + regex 카테고리).

### 1.4 R-1 / R-2 상태 — ✅ 사실

- **R-1** `agent/redact.py`: 본 repo **부재** (`find` 결과 0건). brief §3.1 "❌ 본 repo 부재 (Hermes upstream)" 정확. (단 R-4 doc 은 `/tmp/hermes-phase0/.../agent/redact.py` 401 LOC 참조 — upstream 위치.)
- **R-2** `src/adapters/llm/facade.py`: **실재 + placeholder 확인** (1390B). `complete()` = `raise NotImplementedError("Placeholder — TR-1 풀 3+1 합의 후 real 본문 작성")`. docstring "현 시점은 placeholder — real 본문 작성 시 자동 풀 3+1 합의 trigger TR-1 발화". brief §3.1 "⚠️ facade placeholder" 정확.

### 1.5 R-5 base64 evasion = known limitation — ✅ 사실 (직접 실행)

**`--mode scan-log redaction_fail/base64_evasion.txt` 단독:**
```
[PASS] mode=scan-log target=.../base64_evasion.txt violations=0
rc=0
```
→ base64_evasion.txt **미검출 (rc=0)** — secret-hygiene D-2 가 base64 evasion 못 잡음 = brief §4.1 / R-5 "known limitation" 주장 **실측 확인.** workflow line 13/205~212 = "base64 = known limitation" 명문 일치. §1.3 의 redaction_fail/ 전체 scan 에서도 violation 3건이 전부 partial_redact.txt 였고 base64_evasion.txt 는 0건 → 일관.

### 1.6 로컬 pytest — ✅ 통과

`.venv/bin/python -m pytest tests/tools tests/jarvis -q`:
```
152 passed in 0.07s
```
→ scanner 회귀 0. brief 의 "PoC 시제 보존 (본문 변경 0)" 주장과 정합.

---

## 2. 기술적 타당성 판단 (추가 질문)

### 2.1 R-3 detection (CI) 만으로 (d) 자동 회귀 충족이 기술적으로 타당한가? — ✅ 타당

GP-2 Exit (d) = "**자동 회귀 검증 경로**". (d) 의 본질은 "secret 송신/로그 leak 이 회귀하면 자동으로 BLOCK 되는가" 이다. secret-hygiene D-2 가:
- redaction marker `[REDACTED]` 가 깨지거나 평문 secret 이 로그에 잔존하면 → `scan-log` rc=1 → CI fail → BLOCK.
- D-2 PASS (rc=0 회귀 방지) + D-2 FAIL (rc=1 leak 검출) 양방향 검증 fixture 존재.

→ **detection 수단 (R-3) 으로 (d) "자동 회귀 검증" 을 충족하는 것은 정의상 정합.** (d) 는 prevention(능동 redaction) 을 요구하지 않고 "회귀를 검출하는 자동 경로" 를 요구하므로, CI canary 가 정확히 그 역할. brief §3.2 의 detection ends / prevention ends 분리는 means-vs-ends 관점에서 타당.

### 2.2 prevention (R-1/R-2) deferred 가 GP-2 PASS 를 실제 차단하는가? — ❌ 차단 안 함

- 본 repo = DESIGN/governance repo (docs + tools + CI). 실 runtime 능동 redaction = Hermes upstream (R-1) 책임 — ADR-011 §2.3 #2 "Hermes redaction = 송신 방어 신뢰" 권위로 위임됨.
- GP-2 PASS scope (brief §1.2 + §3.2) = 패턴 정의 (R-4) + CI 회귀 검출 (R-3) + 설계 권위 (ADR). prevention 실 구현은 본 repo scope 외.
- 59 Layer 2a "operative 보호 = 다른 layer, 본 layer DEFER" 패턴 답습이 일관 적용됨.

→ **prevention deferred 는 GP-2 PASS 를 차단하지 않음** (단 (C-1) deferred 명문 조건은 정직성 유지에 필수 — 아래 N-A-1).

---

## 3. BLOCKING (R-A-N)

**없음 (0건).** evidence 주장 부정확/과장 0건. (d) 격상 / run ID / 코드 불변 / fixture 동작 전부 실측 일치.

---

## 4. 권고 (N-A-N)

### N-A-1 (권고): (C-1) prevention deferred 명문 = 발효 *필수 조건* 으로 격상 유지

brief §6 (C-1) 이 R-1/R-2 prevention deferred 를 조건으로 명문화한 것은 적절. 단 §10 P-2 의 우려("R-3 만으로 GP-2 PASS 단순화 → prevention 부재 은폐")가 실재 risk 이므로, 발효 시 PASS 선언문에 **"GP-2 PASS = detection (R-3 operative) + 설계 권위 기반. 능동 redaction prevention (R-1 Hermes import / R-2 facade real) 은 본 repo scope 외 deferred trajectory"** 를 반드시 동반할 것. (현 brief 가 이미 이를 명문화 — 발효 문구에서 누락되지 않도록 유지 권고.)

### N-A-2 (권고): run evidence 는 5/27 snapshot — fresh run trigger 불가 한계 명시 유지

run `26517803107` 은 2026-05-27 push 발화. secret-hygiene 는 `workflow_dispatch` 미지원 (확인: `on:` = push/pull_request/schedule cron `0 3 * * *` 만, line 23~64). 따라서 발효 시점 fresh run 재발화는 (a) cron nightly (다음 UTC 03:00) 또는 (b) 감시 path (line 30~51) 변경 push 로만 가능. brief §2 (d)/§6 (C-3) 가 이를 명시했고 "코드 불변 → 최근 green = 유효 evidence" 논리도 §1.1(3) 에서 실측 입증됨 → 현 상태 수용 가능. 단 fresh run 의무화는 불필요(코드 불변 확인됨)하다는 점을 발효 문구에 유지 권고.

---

## 5. NOTE (NT-A-N)

### NT-A-1: R-4.1 evidence doc 경로 = `docs/phase0/` (architecture 아님)
brief §0.3 line 52 / §9 line 189 가 `r4-1-trigger-extension-evidence.md` 를 경로 없이 참조. 실제 위치 = `docs/phase0/r4-1-trigger-extension-evidence.md` (27236B, 실재). `docs/architecture/` 에는 부재. brief 가 경로를 명시하지 않아 오류는 아니나, cross-ref 정확성 위해 `docs/phase0/` 명기 권장. (비차단 — doc 실재 확인됨.)

### NT-A-2: 51 audit (b) 는 "부분 충족" 표기였음 (brief 가 ✅ 로 격상)
51 audit line 130 = "5조건 충족 자격 = 2.5/5 ((a)+(c) 충족 / **(b) 부분** / (d)+(e) gap)". brief §2 는 (b) 를 ✅ 로 표기. §1.3 실측상 D-2 PoC fixture 가 실제 동작(rc=0/rc=1 양방향)하므로 (b) ✅ 격상은 정당하다고 판단. 단 51 audit 의 "(b) 부분" → brief "(b) ✅" 격상도 (d) 와 함께 일어난 격상이므로, 발효 문구에 (b) 격상 근거(D-2 PoC + r4-1 PoC 실증)를 (d) 와 동등하게 명시 권장.

### NT-A-3: brief §0.3 "본 cycle audit (read-only)" 주장 = 본 Agent A 검토로 독립 재현됨
brief 가 "secret-hygiene CI + fixtures + secret_scanner filesystem direct" audit 을 근거로 삼음. 본 Agent A 가 동일 대상을 독립 inspection 하여 brief 주장과 100% 일치 확인 → audit 자체의 신뢰성 입증. P-6 ("작성자 = 57/59 Claude cascade") 우려에 대해, 본 Agent A (구현 분석가) 의 독립 실측이 over-claim 0 을 입증함.

---

## 6. 종합

(β) cycle 의 "L-1 stdlib 시제 충족" 실측 거짓 전례를 의식한 비판적 검증에도 불구하고, 본 brief 의 evidence 는 **모든 갈래에서 실측 사실**:

| 검증 항목 | 결과 |
|----------|------|
| (d) workflow D-2 step 실재 | ✅ line 165/186 |
| (d) run 26517803107 = success/4fec6485/push | ✅ |
| (d) run 이 D-2 step 실제 실행 (hollow 아님) | ✅ scan job D-2 2 step success |
| (d) 코드 불변 (4fec6485..HEAD) | ✅ 0 commits |
| (d) 51 audit "gap" 부정확 framing 정당성 | ✅ D-2 가 5/10 부터 audit(5/28) 전 operative |
| (a) R-4 equivalence doc 실재 + 내용 | ✅ 29KB 동등성 매트릭스 |
| (b) PoC redaction_pass rc=0 violations=0 | ✅ 직접 실행 |
| (b) PoC redaction_fail rc=1 leak 검출 | ✅ violations=3 직접 실행 |
| R-1 agent/redact.py 부재 | ✅ |
| R-2 facade placeholder (NotImplementedError) | ✅ |
| R-5 base64_evasion 미검출 (known limitation) | ✅ rc=0 직접 실행 |
| pytest tests/tools tests/jarvis | ✅ 152 passed |
| R-3 detection 으로 (d) 충족 타당성 | ✅ 정의 정합 |
| prevention deferred 가 PASS 차단? | ❌ 차단 안 함 (DESIGN repo scope) |

**VERDICT = APPROVE** (BLOCKING 0 / 권고 2 / NOTE 3).

---

**Agent A 검토 끝.**
