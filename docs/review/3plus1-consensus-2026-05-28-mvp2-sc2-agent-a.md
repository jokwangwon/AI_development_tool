# 3+1 합의 — Agent A (구현 분석가) 독립 분석: MVP-2 SC-2 R-1 Hermes 위임 검증 brief (v1)

> **작성**: 2026-05-28 (66번째 entry cycle — 세션 #3)
> **관점**: "실제로 동작하는가?" — 기술적 검증 가능성 + evidence 실재성
> **검토 대상**: `docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md` (v1, §0~§10)
> **독립성**: Agent B/C/외부 LLM 응답 미참조. filesystem direct inspection 기반.

---

## §0 판정

⭐ **APPROVE WITH CONDITIONS**

brief 의 *방향* (R-1 = upstream 위임 → 재구현 0, 위임 *검증* ≠ Hermes 안전성 선언, 실 격리 canary deferred = day2-r1 선례 동형) 은 기술적으로 견고하다. R-2 prong (SC-1) 의 in-repo operative 상태는 실측으로 확인된다 (pytest green). 그러나 **§2.3 (축 3 자동 회귀)** 가 r2-canary.yml 을 "Hermes native redaction silent 깨짐 자동 검출 경로" 로 귀속하는 것은 **filesystem direct inspection 결과 부정확** — r2-canary.yml/R-4.1 PoC 는 *우리* SQLCipher BEFORE INSERT trigger UDF (GP-1 DB persistence 영역) canary 이지, Hermes native redaction (GP-2 egress 영역) canary 가 아니다. 이 귀속 오류는 BLOCKING 정정 대상이다.

| 항목 | 결과 |
|------|------|
| BLOCKING | 2건 (B-1 r2-canary 영역 오귀속, B-2 §4.4 Entry "존재 확인" evidence 와 artifact 부재 모순) |
| 권고 | 3건 |
| NOTE | 4건 |

---

## §1 BLOCKING (정정 필수)

### B-1 — §2.3 "축 3 자동 회귀 (R-6)" 의 r2-canary.yml 영역 오귀속 (GP-1 ≠ GP-2)

**brief 인용** (§2.3 line 84): "r2-canary.yml (R-6) = Tier-1 42 canary regression (nightly cron `0 18 * * *` + PR). silent 깨짐 자동 검출." → §2.3 결론 (line 87): "Hermes upstream 변경으로 redaction silent 깨짐 시 자동 검출 경로 ✅ (위임 신뢰의 지속 보증)".

**filesystem direct inspection 결과** (`.github/workflows/r2-canary.yml` + `docker/r4-1-poc/r4_1_poc.py` 직접 read):

- r2-canary.yml line 47~48: job name = "R-4.1 Tier-1 42 canary regression", step (line 61~75) = `docker compose -f docker/r4-1-poc/docker-compose.r4-1-poc.yml up ... --exit-code-from r4-1-poc`.
- `docker/r4-1-poc/r4_1_poc.py` line 1: docstring = "R-4.1 PoC: Tier-1 42종 **trigger UDF** 확장 + R-2 격리 환경 재실행".
- 동 line 15~17 검증 항목: "C1. **BEFORE INSERT trigger** 등록 성공 / C2. **REGEXP UDF** 등록·동작 / C3. Tier-1 42종 canary **INSERT** 모두 차단".
- verdict 판정 (line 526~533): `tier1_pass_rate = "42/42"` 기준 = trigger UDF 가 42 catalog 를 INSERT 차단하는지.

→ **r2-canary.yml 이 검증하는 것 = 우리 SQLCipher BEFORE INSERT trigger UDF (GP-1 DB persistence 영역, day3-r2 + R-4.1)**. 이것은 governance §3 (GP-1) 의 강제 메커니즘 (line 384 "SQLCipher BEFORE INSERT trigger + REGEXP UDF + Tier-1 42 catalog") 이지, **§4 (GP-2 egress, Hermes native redaction `agent/redact.py`) 의 자동 회귀 경로가 아니다**.

**기술적 판단**: §2.3 은 "Hermes upstream redaction silent 깨짐 자동 검출" 을 r2-canary.yml 로 증명하려 하나, 동 workflow 는 Hermes container 의 `agent/redact.py` 를 *전혀 실행하지 않는다* (Docker image 는 우리 `docker/r4-1-poc/`, SQLite trigger 만). Hermes upstream 의 redaction 이 깨져도 r2-canary.yml 의 verdict 는 PASS 로 남는다 (서로 다른 코드 경로). 이는 day2-r1 §4.2 가 명시한 GP-1(DB) vs GP-2(송신) 책임 분리를 §2.3 에서 다시 혼합하는 것이다.

**정정 방향**:
1. §2.3 을 "R-6 = GP-1 (DB trigger UDF) 영역 Tier-1 42 catalog 자동 회귀 — *우리 측* secret_scanner/trigger catalog 의 silent drift 검출" 로 정정.
2. **Hermes native redaction (GP-2 egress) 의 자동 회귀 경로는 현재 미구현임을 명시**. governance §4.5 Exit (d) (line 454) = "R-6 workflow 에 **log file canary inject step 추가**" → 이 step 은 r2-canary.yml 에 *부재* (workflow 는 docker trigger PoC 만, log file grep canary step 0). 즉 GP-2 Exit (d) 미충족.
3. "Hermes 의존성 변경 → R-2/R-4.1 자동 재실행" (§2.3 line 85, governance §4.3 line 438) 은 *설계 명문이자 trigger 매핑* 이며, r2-canary.yml `on.push.paths` (line 27~32: `docker/r4-1-poc/**`, `docker/r2-poc/**`, ...) 에 **`hermes-version.yaml` 경로가 부재** (애초에 파일 부재, §3 C-1 답습). 따라서 "Hermes 의존성 변경 시 자동 재실행" 도 현 시점 *trigger 경로 미연결*. 이를 NOTE 가 아닌 §2.3 본문에 명시.

⚠️ 이 정정 없이는 §2.4 "축 4 권위" 의 "Hermes 출력은 Tools(canary/R-6)로 검증 → 위임 ≠ 맹신" (line 92) 도 over-claim 이 된다 — 현 R-6 는 Hermes 출력을 검증하지 않으므로.

### B-2 — §4.4 Entry "Hermes native redaction `agent/redact.py` 존재 확인" 과 현 artifact 부재의 정합 미명시

**filesystem direct inspection 결과**:
- 본 repo `agent/redact.py` = **부재** (`find ... -name redact.py` → repo 내 0건; in-repo redaction 은 `src/adapters/llm/redaction.py` = R-2 facade, 별개).
- `/tmp/hermes-phase0` = **부재** (`ls` → "그런 파일이나 디렉터리가 없습니다").
- `hermes-version.yaml` = **부재** (repo 전역 + /tmp 0건).

brief §4 (line 120) 는 "artifact 부재 (/tmp/hermes-phase0 휘발 + 본 repo 부재)" 를 **정확히** 명시한다 (실재 확인). 그러나 governance §4.4 Entry (line 444) = "✅ Hermes native redaction `agent/redact.py` **존재 확인** (R-1 Day 2 evidence)" 이며, brief §0.3/§2.1 은 이 day2-r1 evidence 를 위치 검증 근거로 인용한다.

**기술적 판단**: 이것은 *모순이 아니라 시점 차이* 다 — day2-r1 (2026-05-05) 시점에 `/tmp/hermes-phase0/hermes-agent/agent/redact.py` 가 존재했고 (R-4 §2 line 46 + day2-r1 §4 docstring 인용이 그 evidence), 현재는 휘발. 즉 **위치 검증 (축 1) 의 evidence 는 *과거 1회 직접 관찰* 의 문서 기록이며, 현 시점 재확인 불가**. brief §2.1 은 이 사실 (evidence = 2026-05-05 코드 분석 기록) 을 인용하나, **"현 시점 artifact 부재로 재검증 불가, 검증 = 과거 기록 신뢰" 라는 evidence 시점성** 을 §2.1 에 명시하지 않는다. §4 (deferred) 에만 부재가 언급되고, §2.1 (위치 검증 ✅) 에는 "결정적 사실 3건" 이 *현재형* 으로 서술된다.

**정정 방향**: §2.1 에 "위치 검증 evidence = day2-r1 (2026-05-05) 1회 직접 관찰 문서 기록. 현 시점 artifact 부재 (§4) → *재확인 불가, 기록 신뢰 기반*" 1줄 추가. 이것은 over-claim 차단 ([[feedback_pass_scope_overclaim]] 답습) 의 일관 적용이다 — "코드/문서 분석 기반" (§5) 을 §2.1 위치 축에도 명시해야 4축 모두 evidence 등급이 명확해진다.

---

## §2 권고

### R-1 — §2.2 동등성 수치 표기 통일 (47 vs 45, frozenset 별산)

brief §2.2 (line 76~78): "Hermes 35 prefix + 12 regex + 2 frozenset = **47 카테고리 + 2 frozenset**", "Tier-1 catalog = ... = **45**", "Hermes ⊇ Tier-1".

**filesystem direct inspection** (`redaction-pattern-equivalence.md` §5.3 line 266~272 직접 read):
- §5.3 합계: Hermes = "47 + 2 frozenset" (prefix 35 + regex 12 = 47, frozenset 2 별산). ✅ brief 와 일치.
- 그러나 brief 가 비교 대상으로 든 "Tier-1 catalog (secret_scanner, R-4.1) = baseline 5 + prefix 31 + regex 7 + alternation 2 = 45" 는 R-4 §5.3 표의 "R-2 trigger (현 baseline)" 컬럼 (5종) *도 아니고* §7.2 "Tier-1 보충 42종 (prefix 31 + regex 9 + alternation 2)" *도 아니다*. brief 의 "45" 는 secret_scanner 의 catalog 수치 (SC-1 brief §0.3 line 51 "baseline 5 + prefix 31 + regex 7 + alternation 2 = 45") 를 가져온 것으로, **R-4 §5 의 3-way 매트릭스 (Hermes/P1_REDACTOR/R-2 trigger) 에는 secret_scanner 컬럼이 없다**.

→ brief §2.2 가 "R-4 §5 3-way 비교" 라 하면서 실제로는 secret_scanner(45) vs Hermes(47) 를 비교한다. R-4 §5 의 3-way 는 secret_scanner 를 포함하지 않는다. **"Hermes ⊇ Tier-1" 라는 *결론*은 유효** (R-4 §5.3 핵심 관찰 #1 "Hermes ⊇ P1_REDACTOR" + R-4 §7.2 Tier-1 42종 = Hermes 부분집합이므로 Hermes ⊇ Tier-1 catalog 성립). 다만 **출처 표기를 "R-4 §5 + §7.2 (Tier-1 42 = Hermes 부분집합) + SC-1 secret_scanner 45 catalog" 로 정밀화** 권고. 현 "R-4 §5 3-way" 단독 인용은 비교 구성이 부정확.

### R-2 — §3 C-2 "R-6 자동 재실행 답습 유지" 를 B-1 정정에 종속

C-2 (line 105) "R-6 자동 재실행 — r2-canary.yml operative (nightly + PR) — 답습 유지 (변경 0)" 는 B-1 정정 후 "R-6 = GP-1 DB trigger 영역 operative. GP-2 Hermes egress 자동 회귀 = 미구현 (governance §4.5 Exit (d) 미충족)" 으로 동기화 필요. evidence contract C-2 가 GP-2 위임 검증의 "지속 보증" 으로 인용되면 B-1 과 동일 over-claim.

### R-3 — §5 판정 문장에 "GP-2 Exit (d) 자동 회귀 미충족" 명시

§5 (line 142): "full GP-2 PASS Exit (a) = R-1 prong (SC-2 ✅) + R-2 prong (SC-1 ✅) → SC-3 발효 자격". 이 문장은 Exit **(a)** 만 다룬다. governance §4.5 Exit 은 (a)~(e) 5조건이며, **(b) 격리 환경 PoC 실증 (log canary inject) + (d) 자동 회귀 (log file canary inject step) 은 현 미충족** (B-1). full GP-2 PASS 발효 (SC-3) 시 (a) 충족만으로 PASS 불가함을 §5 또는 §0.2 에 명시 권고 — SC-3 으로 over-claim 이 cascade 되지 않도록.

---

## §3 NOTE (filesystem direct inspection 발견)

- **N-1 (R-2 prong 실측 green)**: `src/adapters/llm/redaction.py` + `facade.py` + `redaction_patterns.py` + `tests/adapters/llm/test_redaction_filter.py` 실재. `.venv/bin/python -m pytest tests/adapters/llm/ -q` → **15 passed**. 전체 suite → **167 passed in 0.14s**. brief §1/§5 의 "R-2 prong (SC-1) operative" 는 실측 충족. SC-1 consensus (`3plus1-consensus-2026-05-28-mvp2-sc1.md` §0) = APPROVE WITH CONDITIONS (4 source) → in-repo operative. ✅

- **N-2 (ADR-011 §2.3 #2 인용 정확)**: `ADR-011-means-vs-ends-redaction.md` 운영 함의 #2 = "Hermes 자체 redaction은 **로그/LLM 송신 방어로만 신뢰**: 저장 경로(DB/파일) 차단 책임 없음" — brief §2.4 (line 91) 인용과 정확 일치. #4 (자동 R-2 재실행) + §7.3 (line 237 "본 ADR은 Hermes 안전성을 선언하지 않는다") 도 일치. brief 의 over-claim 경계 (§0/§5/§10) 권위 인용 견고. ✅

- **N-3 (day2-r1 "FAIL" 맥락 인용 정확)**: `day2-r1-redaction-location-verification.md` §5.2 (line 133) = "G1a (현 정의 — 형태 기준): 미충족. Hermes 자체 redaction은 DB INSERT 경로 미적용". brief §2.1 (line 71) 의 "day2-r1 'FAIL' = G1a (DB INSERT) 맥락 (DB = GP-1 책임)" 정확. day2-r1 §4.1 docstring "for logs and tool output ... before they reach log files, verbose output, or gateway logs" 도 brief §2.1 사실 1 (line 67) 과 일치. brief 의 "FAIL = DB 맥락, GP-2 송신 영역은 적용 ✅" 재해석은 day2-r1 §5.2 / §8.2 (line 192 "풀 합의 옵션 (1) 채택의 안전성") 과 정합. ✅

- **N-4 (artifact/파일 부재 실재 — brief §3/§4 정확)**: `agent/redact.py` (repo) 부재, `/tmp/hermes-phase0` 부재, `hermes-version.yaml` (전역) 부재 모두 실측 확인. brief §3 C-1 (line 104 "governance §1.2.7 P11/Layer 1 명문, hermes-version.yaml 파일 부재"), §4 (line 120 artifact 부재), §0.2 #6 (파일 생성 0) 의 부재 서술은 모두 정확. governance §1.2.7 P11 (line 249/257) = "`hermes-version.yaml` v0.12.0 명시" 는 *enforcement 요구 명문* 이지 파일 실재가 아님 — brief §3 C-1 "governance 명문 (파일 부재)" 정확. ✅

---

## §4 deferred vs 실 실행 — 기술적 판단

> **질문**: 코드/문서 분석으로 R-1 위임 검증 충족 가능한가? 실 격리 canary 실 실행이 기술적으로 필수인가?

### §4.1 코드/문서 분석으로 충족 가능한 부분 (deferred 정당)

R-1 위임 검증의 **핵심 명제 = "Hermes redaction 이 GP-2 영역(로그/송신)에 적용되며, Tier-1 패턴을 동등 이상 포함한다"**. 이 명제는:
- 축 1 (위치): docstring + import grep + SessionDB import 0 = **정적 코드 분석으로 결정적** (day2-r1 §3.2 "PoC 가 동일 결론 강화만, 변경 0" 정당화 유효). 단, B-2 — 현 artifact 부재로 *재확인* 불가, 과거 기록 신뢰.
- 축 2 (동등성): 패턴 카탈로그 *enumerate 비교* = **정적 분석으로 충족** (R-4 §5 매트릭스). "Hermes 카탈로그가 Tier-1 패턴 문자열을 포함하는가" 는 정규식 비교이지 실행 비교가 아니므로 코드 분석 충분.
- 축 4 (권위): ADR-011 §2.3 #2 = **문서 권위 명시**, 검증 불요.

→ **이 3축은 코드/문서 분석으로 충족 가능** (day2-r1 선례 동형). brief 의 deferred 정당화 (§4) 는 이 범위에서 기술적으로 타당하다.

### §4.2 코드/문서 분석으로 충족 *불가* 한 부분 (실 실행이 기술적 가치)

- **축 3 (자동 회귀)**: B-1 — Hermes native redaction 의 자동 회귀 검출은 *현재 어떤 artifact 로도 검증되지 않는다* (r2-canary.yml 은 GP-1 DB trigger 영역). 이것은 deferred 가 아니라 **미구현** 이다. governance §4.5 Exit (d) "R-6 에 log file canary inject step 추가" 가 충족되어야 비로소 "Hermes redaction 깨짐 자동 검출" 이 성립한다. **이 부분은 실 격리 canary (혹은 최소한 CI log-grep canary step) 가 기술적으로 필수** — 정적 분석으로 "redaction 이 *런타임에 실제 마스킹하는지*" 를 증명할 수 없기 때문.

- **실 격리 canary 의 고유 가치**: 정적 분석은 "패턴 *문자열* 이 카탈로그에 존재" 를 보이나, "그 패턴이 런타임에 `re.sub`/마스킹 경로를 *실제 통과* 하여 `[REDACTED]` 출력" 은 보이지 못한다. `HERMES_REDACT_SECRETS` 가 기본 `false` (R-4 §2.4 line 138 "opt-in, default ON → OFF") 라는 사실은 **정적 분석으로 "redaction 코드 존재" 와 "redaction 활성" 이 다름** 을 보여준다 — 즉 실 실행 canary 만이 "활성 상태에서 실제 마스킹" 을 입증한다.

### §4.3 종합 판단

- **R-1 위임 검증 = 코드/문서 분석으로 *부분 충족*** (축 1 위치 + 축 2 동등성 + 축 4 권위). 이 부분은 deferred 정당.
- **축 3 (자동 회귀) 은 deferred 가 아니라 미구현** — brief 가 r2-canary.yml 을 Hermes egress 회귀로 오귀속한 결과 충족으로 보이나, 실제로는 GP-2 egress 자동 회귀 경로 부재 (B-1). 이 축은 **실 격리 canary 또는 CI log-canary step 이 기술적으로 필수**.
- 따라서 brief 의 "R-1 위임 검증 충족 (코드/문서 분석 기반)" 판정은 **축 1/2/4 한정으로는 타당, 축 3 을 충족으로 포함하면 over-claim**. 4축 중 3축 충족 + 축 3 (자동 회귀) 은 GP-2 Exit (d) 와 함께 미구현 명시 — 이것이 정확한 기술적 상태.

⚠️ 단, "축 3 미구현" 이 R-1 위임 검증 *전체* 를 FAIL 로 만들지는 않는다. R-1 의 본질 = "Hermes 가 GP-2 영역에 redaction 을 적용 + Tier-1 동등 이상 포함" (위치+동등성+권위) 이며, 자동 회귀 (축 3) 는 *지속 보증* 메커니즘이지 위임 *성립* 의 전제가 아니다. 따라서 **B-1 정정 (축 3 = GP-1 영역 + GP-2 egress 회귀 미구현 명시) 후 APPROVE 가능**. SC-3 (full GP-2 PASS 발효) 시점에 Exit (d) (log canary step) 가 별도 충족되어야 한다는 조건만 §5 에 명시되면 된다.

---

## §5 Agent A 최종

- **판정**: **APPROVE WITH CONDITIONS** (BLOCKING 2 + 권고 3).
- **방향 견고**: R-1 = upstream 위임 (재구현 0), 위임 검증 ≠ 안전 선언 (ADR-011 §7.3 정합), R-2 prong (SC-1) in-repo operative 실측 (167 green), day2-r1 / ADR-011 / artifact 부재 인용 정확.
- **BLOCKING 핵심**: (B-1) §2.3 r2-canary.yml = GP-1 DB trigger 영역 ≠ Hermes GP-2 egress 자동 회귀 — 영역 오귀속 정정 + GP-2 Exit (d) 미구현 명시. (B-2) §2.1 위치 검증 evidence 시점성 (과거 기록, 현 artifact 부재 재확인 불가) 명시.
- **deferred 기술 판단**: 축 1/2/4 = 코드/문서 분석 충족 (deferred 정당). 축 3 (자동 회귀) = deferred 아닌 *미구현*, 실 격리 canary / CI log-canary step 이 기술적 필수. R-1 위임 *성립* 은 축 3 없이도 가능 (자동 회귀는 지속 보증), 단 SC-3 full GP-2 PASS 시 Exit (d) 별도 충족 조건.

---

**Agent A 독립 분석 끝.**
