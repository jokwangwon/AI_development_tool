# 3+1 합의 — Agent B (품질/안전성 검증가) 독립 분석

> **대상**: `docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md` (v1, §0~§10)
>
> **관점**: "안전하고 견고한가?" — over-claim 경계 / 권위 정합 / 보안 경계 / deferred 안전성
>
> **작성**: 2026-05-28 (66번째 entry cycle, 세션 #3) — Agent B 독립 (A/C/외부 LLM 미참조)
>
> **검증 방법**: brief 직접 read + 권위 문서 verbatim cross-verify (ADR-011 / R-4 / day2-r1 / governance) + repo filesystem direct (SC-1 구현 실재 / r2-canary.yml 트리거 / hermes-version.yaml 부재)

---

## 1. 판정

### **APPROVE WITH CONDITIONS** (BLOCKING 2 + 권고 4)

brief 의 **핵심 over-claim 경계는 전반적으로 견고**하다. §0.2 10개 "하지 않는 것" + §5 over-claim 경계 3항 + §10 자기진단 7항이 본 세션 #2 4회 cascade 교훈을 답습하여 "Hermes 안전성 선언 ≠ 위임 검증" / "full GP-2 PASS ≠ 본 cycle" / "코드/문서 분석 기반 (실 격리 canary deferred)" 3축 정직성을 명문화했다. R-2 prong 발효 주장(SC-1 in-repo operative)도 filesystem 실측으로 **사실 확인** (over-claim 아님).

그러나 **2개 BLOCKING**: (B-1) **§2.3 축 3 "자동 회귀 ✅" 의 framing over-claim** — r2-canary.yml paths 필터 + hermes-version.yaml 부재로 *Hermes upstream 변경 자동 검출* 은 현재 미작동 (cron 시점 외 자동 trigger 0). (B-2) **`HERMES_REDACT_SECRETS=false` opt-in 기본값 미언급** — R-1 위임의 *실효 전제* (redaction 활성화 여부)가 brief 4축 어디에도 없음. 이 둘은 "위임 검증 충족" 판정의 *보안 견고성*에 직접 영향하므로 정정 필수.

---

## 2. BLOCKING (정정 필수)

### B-1 ⭐⭐ — §2.3 축 3 "자동 회귀 ✅" framing over-claim (paths 필터 + hermes-version.yaml 부재)

**brief 주장** (line 82~87):
> "축 3 — 자동 회귀 검증 (R-6) ✅ ... ADR-011 §2.3 #4 + governance §1.2.7 Layer 1 = Hermes 의존성 (hermes-version.yaml) 변경 시 R-2/R-4.1 PoC 자동 재실행 ... → **Hermes upstream 변경으로 redaction silent 깨짐 시 자동 검출 경로 ✅** (위임 신뢰의 지속 보증)."

**filesystem 실측 모순** (`.github/workflows/r2-canary.yml` line 20~40 direct):
```yaml
on:
  workflow_dispatch:
  schedule:
    - cron: "0 18 * * *"
  push:
    paths:
      - "docker/r4-1-poc/**"
      - "docker/r2-poc/**"
      - "docs/architecture/canary-recheck-design.md"
      - "docs/phase0/r4-1-trigger-extension-evidence.md"
      - ".github/workflows/r2-canary.yml"
  pull_request:
    paths: (동일 5 경로)
```

- push/PR 트리거의 `paths` 필터는 **PoC 디렉토리 + 설계 문서 5경로에 한정**. `hermes-version.yaml` 은 paths 에 **없음** (애초에 파일 자체 부재 — `find . -name hermes-version.yaml` = 0건, brief §3 C-1 도 "파일 부재" 인정).
- 따라서 **"Hermes 의존성 변경 시 자동 재실행"** 은 *현재 미작동*: hermes-version.yaml 추적 파일이 없으므로 그 drift 를 trigger 할 paths 항목 자체가 없음. 자동 검출은 **nightly cron (`0 18 * * *`) 시점에만** 발화 (시점 외 자동 검출 0).
- 메모리 [[feedback_actual_run_trigger_paths_filter]] 직접 답습: "on.push.paths 필터 확인 의무, empty commit 만으론 trigger 0". 본 건은 *hermes-version.yaml 부재 → paths 미등록 → upstream drift 자동 trigger 0*.

**근거 정합**: governance §1.2.7.3 (line 268~269) P11 감지 기준 (1) 은 "`hermes-version.yaml` git diff 자동 점검 (every commit + nightly)" 를 *목표*로 명시하나, 이는 **P11 enforcement 설계 (미구현)** 이지 현 r2-canary.yml 의 작동 사실이 아니다. brief 가 "governance §1.2.7 Layer 1 = ... 자동 재실행" 을 *현 작동* 으로 인용한 것은 **설계 의무를 작동 사실로 격상** (60 entry B-1 "detection 으로 prevention 대체" 와 동형 framing over-claim).

**정정 요구**:
1. 축 3 → "**R-6 nightly cron 회귀 검증 operative ✅** (Tier-1 42 canary, 60 entry detection-layer PASS 답습) / **단 Hermes upstream 변경 자동 trigger = hermes-version.yaml 파일화 + paths 등록 후 (deferred, §3 C-1)**" 로 강등.
2. "위임 신뢰의 *지속* 보증 ✅" → "**nightly cron 주기 보증 ✅ + upstream-diff-triggered 보증 = deferred**" 로 분리.
3. C-1 contract 의 "version pin v0.12.0 파일 부재" 와 축 3 "자동 재실행 ✅" 의 **내적 모순 해소** (파일 없으면 diff trigger 도 없음).

### B-2 ⭐ — `HERMES_REDACT_SECRETS=false` opt-in 기본값 미언급 (위임 실효 전제 누락)

**R-4 §2.4 line 138 verbatim**:
> "**기본값**: `HERMES_REDACT_SECRETS=false` (line 64) — opt-in. v0.12.0 breaking change 로 default ON → OFF 전환됨 (Day 1 보고서 §2 기록)."

**문제**: brief 4축 (§2.1~§2.4) + evidence contract (§3) + deferred 정당화 (§4) 어디에도 **redaction *활성화 전제*** 가 없다. R-1 위임 = "Hermes 가 GP-2 영역에 redaction 적용" 인데, Hermes v0.12.0 기본값이 **redaction OFF (opt-in)** 이면, *위치/동등성/자동회귀가 모두 ✅ 라도 런타임에서 redaction 이 실제로 켜져 있지 않으면 위임 실효 = 0* 이다.

- canary-recheck-design.md (R-5) line 56 + 348 도 `HERMES_REDACT_SECRETS` 를 trigger 별 startup 체크 대상으로 명시 + line 348 "`=false` 자동 설정 시도 감지 → ADR-011 §2.4 T3 위반 alert" — 즉 **R-5 가 이 config 를 핵심 위임 전제로 다룸**. brief 가 R-5 를 §0.3 source 로 인용(line 50)하면서 이 핵심 전제를 누락한 것은 scope gap.

**정정 요구**: 4축에 **축 0 (또는 §3 C-5) "redaction 활성화 전제 = `HERMES_REDACT_SECRETS=true` 강제 + R-5 config 체크 (`=false` drift = T3 위반 alert)"** 추가. 미설정 시 "redaction 적용 ✅" (축 1) 의 *런타임 실효* 가 보장되지 않음을 명문화. (이는 실 격리 canary deferred 와 별개 — config 전제는 문서 검증만으로 명문 가능.)

---

## 3. 권고 (non-blocking)

### R-1 — §4 deferred 안전성: day2-r1 선례의 "맥락 차이" 명문 (위치 검증 vs 적용 커버리지 검증)

brief §4 (line 122~124) 는 day2-r1 "PoC 미시행 충분" 선례를 SC-2 에 적용한다. **선례 적용 자체는 정당** (코드/문서 분석으로 결정적 결론 가능). 단 *맥락 차이* 명문 권고:
- **day2-r1** = R-1 redaction 의 *위치* 검증 (DB INSERT 경로 미적용 = FAIL). docstring + 25 import grep + 시그니처 = **부재/위치 사실** → 코드 분석으로 결정적 (PoC 가 동일 결론 강화만).
- **SC-2** = R-1 의 *GP-2 영역 적용 커버리지 + Tier-1 동등* 검증 = **존재/동작 사실**. 존재/동작은 부재/위치보다 *실 실행 보강 가치가 상대적으로 높음* (특히 B-2 opt-in 전제 + base64 우회 + group-aware 치환 동작은 정적 분석 한계). brief §4 line 124 "동일 결론 강화 (가치 보강이나 결론 변경 0)" 은 *위치 축* 엔 맞으나 *동작 축* 엔 약함.
- 권고: §4 에 "day2-r1 선례 = *위치/부재* 결정성. SC-2 *동작 커버리지* 는 실 격리 canary 가 보강 가치 위치 축보다 높음 (C-3 SOP 우선순위 trigger)" 1줄 추가. RT-2 (line 176 "코드 분석 < 실 실행") 가 이미 이 위계를 인정하므로 §4 와 정합.

### R-2 — §2.1 day2-r1 "FAIL" 재해석 정합성 (왜곡 0, 단 원 판정 인용 정밀화 권고)

§2.1 (line 71) "day2-r1 'FAIL' = G1a (DB INSERT) 맥락 ... GP-2 위임 근거와 모순 0 (오히려 GP-2 영역 적용 입증)" 의 재해석은 **day2-r1 원문과 정합** (왜곡 0):
- day2-r1 §5.2 (line 131~134): "**G1a (형태 기준)**: 미충족 (DB INSERT 경로 미적용)". day2-r1 §1 (line 14): 적용 위치 = "로그·도구 출력·Gateway 통신 전용". ADR-011 §2.2 (line 68~73) G1a FAIL = "이 경로(DB)로 헌법 8조 충족 시도 금지".
- 즉 day2-r1 "FAIL" 은 *DB INSERT 차단 실패* (= GP-1 책임 영역) 이지 *GP-2 (로그/송신) 영역 redaction 부재* 가 아니다. brief 재해석은 정확.
- 권고: §2.1 에 day2-r1 **§5.2 line 133 verbatim** ("G1a 미충족 = DB INSERT 미적용") 인용 추가 — "FAIL" 단어만 인용 시 독자가 "R-1 전면 실패" 로 오독 위험. 원 판정 §과 line 명시로 추적성 강화.

### R-3 — §2.2 "Tier-1 42" vs R-4 "Tier-1 45" 숫자 불일치 정밀화

brief 가 두 숫자를 혼용:
- §2.2 (line 80) + governance §4.5 (a) 인용 = "Tier-1 **42** catalog". §2.3 (line 84) = "Tier-1 **42** canary". §9 E-2 (line 185) = "Tier-1 **45**".
- R-4 §5.3 (line 272) verbatim = Hermes "47 + 2 frozenset", Tier-1 catalog = "**45**" (baseline 5 + prefix 31 + regex 7 + alternation 2). R-4 §7.2 (line 337) = "Tier-1 보충 패턴 **42**종 (Prefix 31 + 추가 regex 9 + alternation 2)".
- 즉 **45 = secret_scanner 전체 catalog / 42 = trigger UDF 보충 권고 (privacy Tier-3 2 + Tier-2 1 제외)**. 둘 다 실재하나 *다른 집합*. brief 가 §2.2 에서 "governance §4.5 (a) 'Tier-1 42 catalog 적용' 충족" 으로 R-4 §5 (45 비교) 를 인용한 것은 **42(보충 권고) ↔ 45(전체) 혼선**. governance §4.5(a) line 451 원문은 "Tier-1 **42** catalog" 표기.
- 권고: §2.2 에서 "Hermes 47 ⊇ Tier-1 45 (R-4 §5)" 와 "governance §4.5(a) Tier-1 42 적용" 을 **명시 구분** (42 = privacy 제외 secret 한정 보충 집합, 45 = 전체). E-2 (45) → §2.2 (42) 정합 1줄. (숫자 불일치는 판정 변경 아님 — 정밀화.)

### R-4 — §5 governance §4.5 (a) 충족 주장의 "검증" vs "Exit 충족" 분리 (over-claim 인접)

§5 (line 135): "governance §4.5 (a) 'Hermes native redaction Tier-1 42 catalog 적용 검증' = 축 1+2 충족". 
- governance §4.5 (b) (line 452) verbatim = "**격리 환경 PoC 실증** — log file canary inject + grep 검증 PoC (Docker 격리)". 즉 GP-2 Exit 는 (a)~(e) 5조건이며 **(b) 격리 PoC 실증이 별도 의무**. brief §4 가 (b) 를 deferred 처리하는 것은 정직하나, §5 가 "(a) 충족" 을 강조하며 **(b) deferred 가 R-1 prong 의 *부분* 미충족임을 §5 본문에서 약하게 처리** (§0.2 #4 + §4 에만 명시).
- 권고: §5 에 "**R-1 prong = (a) 검증 충족 (코드/문서) + (b) 격리 PoC 실증 = deferred (C-3 SOP)**. full GP-2 Exit (a)~(e) 중 (b) prevention 실증은 SC-3 또는 별도 trigger 보강" 명문. 60 entry M-4 "detection-layer PASS = 빈 껍데기 risk" 답습 — (a) 충족이 (b) 실증을 갈음하지 않음을 §5 본문에 직접 명시 (현재는 §4 분산).

---

## 4. NOTE (관찰)

- **N-1 (over-claim 경계 견고)**: brief 의 over-claim 차단 장치는 본 세션 #2 4회 cascade + 60 entry B-1 reframe 교훈을 충실히 답습. §0.2 #1 (Hermes 안전성 선언 0) / #2 (full GP-2 PASS 발효 0) / #4 (실 격리 canary 0) + §5 over-claim 경계 3항 + §10 P-1~P-7 = ADR-011 §7.3 (line 237 "본 ADR 은 Hermes 안전성을 선언하지 않는다") 와 정합. **scope 명칭 정직성 = 양호** (BLOCKING 아님).

- **N-2 (R-2 prong 발효 주장 = 사실 확인)**: brief line 11 "R-2 prong = SC-1 (facade RedactionFilter) ✅ 이미 발효 → full GP-2 PASS = R-1 ∧ R-2" 의 SC-1 발효 주장은 filesystem 실측으로 **사실** (commit `7051138` "SC-1 facade RedactionFilter ... 첫 실제 코드" + `src/adapters/llm/redaction.py` + `redaction_patterns.py` + `tests/adapters/llm/test_redaction_filter.py` 실재). R-2 prong over-claim 아님.

- **N-3 (Hermes ≠ root of trust 정합 양호)**: §2.4 (line 92) "Hermes ≠ root of trust ... R-6 자동 회귀가 위임 위에 위치" = ADR-011 §2.3 권위 위계 (line 101~108, Constitution > ADR > ... > Hermes) + 운영 함의 #1 (line 112 "Hermes 출력은 Tools 로 검증") 정합. 단 B-1 (R-6 upstream-diff trigger 미작동) 이 정정되지 않으면 "R-6 가 위임 위에 위치" 의 *실효* 가 nightly cron 으로 축소됨 — B-1 과 연동.

- **N-4 (full GP-2 PASS 격상 over-claim 0)**: 본 cycle 이 full GP-2 PASS 발효로 격상하지 않음을 §0.2 #2 + §5 (line 140) + §10 P-4 에서 3중 차단. "full GP-2 PASS = R-1(SC-2) ∧ R-2(SC-1) → SC-3 별도" 구조는 60 entry M-6 (full GP-2 PASS = MVP-2 PASS 잔여 trajectory, 별도 cycle) 와 정합. **격상 over-claim 0**.

- **N-5 (R-1-a 위임 = import 0 정합)**: §0.2 #3 (agent/redact.py import 0) + §1 (R-1 = upstream 위임, 재구현 0) = ADR-011 §2.3 + 64 trajectory (R-1-a) 답습. Provider Liquidity / Hermes 외부 위임 경계 보존 — 보안 경계 침입 0.

- **N-6 (Tier-3 privacy 영역 무관)**: R-4 §6.4 (line 320~327) Tier-3 (Discord/E.164) = "헌법 8조 본질 외, secret 아님". brief 가 Tier-3 를 위임 검증에 포함하지 않은 것은 정합 (privacy ≠ secret). 무관 NOTE.

---

## 5. 권위 인용 cross-verify 매트릭스

| # | brief 인용 | 위치 | 실제 문서 (verbatim) | 판정 |
|---|-----------|------|---------------------|------|
| 1 | "Hermes 자체 redaction 은 로그/LLM 송신 방어로만 신뢰" | §0.3 line 47, §2.4 line 91 | ADR-011 §2.3 #2 line 113 = "Hermes 자체 redaction 은 로그/LLM 송신 방어로만 신뢰: 저장 경로(DB/파일) 차단 책임 없음" | ✅ **일치** |
| 2 | "본 ADR 은 Hermes 안전성을 선언하지 않는다" | line 7, §0.2 #1, §5 line 138, §10 P-1 | ADR-011 §7.3 line 237 = "**본 ADR 은 Hermes 안전성을 선언하지 않는다** — Hermes 는 검증 대상이며 ..." | ✅ **일치** |
| 3 | R-4 §7.3 "Hermes 안전성 선언 금지" | line 7 ("R-4 §7.3 답습") | R-4 §7.3 (line 362~372) = **"trigger 마스킹 vs 차단 정책"** (안전성 선언 금지 아님). R-4 의 안전성 선언 금지는 **§1.3 line 39** ("Hermes 안전성 선언 — ADR-011 §7.3 위반 금지") + **§10.3 line 481** | ⚠️ **§ 오인** — R-4 §7.3 ≠ 안전성 선언. R-4 §1.3/§10.3 또는 ADR-011 §7.3 으로 정정 (line 7 / §0.3 line 45) |
| 4 | "Hermes 47 카테고리 + 2 frozenset ⊇ Tier-1 45" | §0.3 line 45, §2.2 line 76~78 | R-4 §5.3 line 272 = "Hermes **47 + 2 frozenset** / Tier-1 catalog ... **45**" + line 276 "Hermes ⊇ P1_REDACTOR" | ✅ **일치** (Hermes superset 사실) |
| 5 | governance §4.5 (a) "Tier-1 42 catalog 적용 검증 + facade redaction filter 검증" | §0.3 line 48, §2.2 line 80, §5 line 135 | governance §4.5 (a) line 451 = "Hermes native redaction **Tier-1 42 catalog** 적용 검증 + P1 facade redaction filter 검증" | ✅ **일치** (단 42 vs §2.2 의 45 혼선 = R-3 권고) |
| 6 | "R-6 = Tier-1 42 canary regression (nightly cron + PR)" | §0.3 line 46, §2.3 line 84 | r2-canary.yml line 21~40 = workflow_dispatch + cron `0 18 * * *` + push/PR **(paths 필터 5경로, hermes-version.yaml 미포함)** | ⚠️ **부분 모순** — "PR" 트리거는 PoC/설계 파일 paths 한정. Hermes upstream 변경 자동 trigger = 미작동 (B-1) |
| 7 | "governance §1.2.7 Layer 1 = Hermes 의존성 변경 시 R-2/R-4.1 자동 재실행" | §0.3 line 48, §2.3 line 85, §3 C-4 | governance §1.2.7.1 line 249 (d) + §1.2.7.3 line 268~269 = P11 **enforcement *설계*** (미구현 — hermes-version.yaml 부재). "every commit + nightly 자동 점검" = 목표 명시 | ⚠️ **설계 ↔ 작동 격상** — P11 설계 의무를 현 작동으로 인용 (B-1) |
| 8 | "Hermes ≠ root of trust (권위 위계)" | §2.4 line 92, line 13 | ADR-011 §2.3 line 95~108 = "Constitution > ADR > SDD > Harness Gates > Hermes > Worker Agents" + 운영 함의 #1 (line 112) | ✅ **일치** |
| 9 | day2-r1 "FAIL" = G1a (DB) 맥락 | §0.3 line 44, §2.1 line 71, §10 P-2 | day2-r1 §5.2 line 133 = "G1a (형태 기준): 미충족. Hermes 자체 redaction 은 DB INSERT 경로 미적용" + §1 line 14 적용 위치 = "로그·도구 출력·Gateway 전용" | ✅ **일치** (재해석 왜곡 0 — R-2 정밀화 권고) |
| 10 | "day2-r1 §3.2 'PoC 미시행 정당성' = 코드 분석으로 결정적" | §4 line 123 | day2-r1 §3.2 line 48~55 = "PoC 미시행 정당성 ... PoC 는 동일 결과 확인이며 시간·환경 비용 대비 추가 정보 가치 0" | ✅ **일치** (단 위치 vs 동작 맥락 차이 = R-1 권고) |
| 11 | "version pin v0.12.0 (governance §1.2.7 P11/Layer 1, hermes-version.yaml 파일 부재)" | §3 C-1 line 104 | `find . -name hermes-version.yaml` = **0건** (파일 부재 확인) + governance §1.2.7 P11 명문 | ✅ **일치** (파일 부재 정직 인정) |
| 12 | `HERMES_REDACT_SECRETS=false` opt-in 기본값 | **미언급** | R-4 §2.4 line 138 = "기본값 `HERMES_REDACT_SECRETS=false` opt-in" + R-5 line 56/348 (config 체크 + T3 alert) | ❌ **누락** — 위임 실효 전제 (B-2) |

**매트릭스 요약**: 12건 중 ✅ 일치 7 / ⚠️ 부분 모순·격상 3 (#3 § 오인, #6·#7 자동 회귀 framing) / ❌ 누락 1 (#12 opt-in). 권위 *내용* 왜곡은 0 — **§ 번호 오인 (#3) + framing 격상 (#6/#7 = B-1) + 전제 누락 (#12 = B-2)** 이 정정 대상. ADR-011 §7.3 / day2-r1 §5.2 / Hermes ≠ root of trust 핵심 권위는 모두 정합.

---

## 6. 종합 (Agent B)

본 brief 의 **over-claim 1차 경계 (안전성 선언 / full GP-2 PASS 격상 / 실 실행 완료 주장) 는 견고** — 본 프로젝트 세션 #2 4회 cascade + 60 entry detection-layer reframe 교훈을 충실히 답습했다. R-2 prong 발효 + day2-r1 재해석 + Hermes ≠ root of trust 정합도 verbatim 확인 결과 왜곡 0.

그러나 **2개 안전성 구멍**:
1. **B-1**: "자동 회귀 ✅" 가 *Hermes upstream 변경 자동 검출* 을 함의하나, r2-canary.yml paths 필터 + hermes-version.yaml 부재로 현재 **nightly cron 외 자동 trigger = 0**. 60 entry B-1 ("detection 으로 prevention 대체") + 메모리 [[feedback_actual_run_trigger_paths_filter]] 동형 framing over-claim 재발.
2. **B-2**: `HERMES_REDACT_SECRETS=false` opt-in 기본값이 **위임 실효 전제**인데 4축 어디에도 없음. 위치/동등성/회귀 ✅ 라도 런타임 redaction OFF 이면 위임 실효 0.

이 둘은 "R-1 위임 검증 충족" 이 *위임 신뢰의 지속·런타임 실효* 를 보장한다는 **보안 견고성 주장**에 직접 영향하므로 BLOCKING. 정정 시 → "**R-1 위임 검증 = 코드/문서 분석 기반 (위치·동등성·nightly 회귀 ✅) + redaction 활성화 전제 명문 + upstream-diff 자동 trigger / 실 격리 canary = deferred**" 로 강등하면 발효 정당 (REJECT 아님 — evidence 실증 + 발효 형태 정당).

**→ APPROVE WITH CONDITIONS (BLOCKING 2 + 권고 4). v1.1 1pass 흡수 권고 (별도 v2 cycle 불요 — 60/65 동형 ceremony-inflation 차단).**

---

**Agent B 독립 분석 끝.**
