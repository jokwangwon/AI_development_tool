# 3+1 합의 — Agent B (품질/안전성 검증가) — (β) sub-수단 결정 entry brief (57 entry)

> **작성**: 2026-05-28 (신규 세션)
> **관점**: "안전하고 견고한가?" — 보안, 엣지케이스, 문서 정합성, 권위 chain 정확성
> **검토 대상**: `docs/phase0/mvp2-beta-submeans-decision-brief.md` (v1, §0~§12)
> **편향 회피**: Agent A/C + 외부 LLM 응답 미참조 (독립 분석)
> **cross-check source**: ADR-011 §2.1/§2.3, ADR-012 §2.1/§2.5/§3.2, governance-preconditions.md §2.1/§4 (GP-2), gamma-decision-brief §1.3, layer-124-pass-brief §1.2/§11.1, 실 repo PoC 시제 (filesystem direct verify)

---

## verdict

## **REVISE**

핵심 사유: 본 brief 의 *가장 빈번하고 load-bearing 한 권위 인용* ("R-1 MANDATORY (ADR-011 §2.3 #2)")가 **모법 권위를 정반대로 전도(invert)** 하고 있다. ADR-011 §2.3 #2 + GP-2 §4.1 은 Hermes native redaction(R-1)을 **보조(auxiliary) 역할**로 명시하는데, 본 brief 는 이를 "MANDATORY"의 근거로 인용한다. 이는 §6.2 trigger 4(권위 chain 손상) 발화 + 의사결정 기반 자체를 왜곡하는 BLOCKING. 추가로 ADR-012 §2.1 misattribution(2건), L-1 "stdlib 단독" 실 PoC 시제 불일치(외부 library 강제 의존 0 주장의 사실 오류)가 BLOCKING. 단 — scope 침입 0, (γ-c) 특화 의무 4 정합, base64/외부 library/Hermes import 영구 분리 framing 은 견고. 정정은 in-place v1.1 1pass 흡수 가능 (별도 v2 cycle 불필요, ceremony-inflation 차단). 따라서 REJECT 아님.

---

## BLOCKING findings

### R-B-1 (권위 인용 전도 — BLOCKING, 최우선) — "R-1 MANDATORY (ADR-011 §2.3 #2)" 는 모법을 정반대로 인용

**위치**: 본 brief §2.1 line 117 (`R-1 ... MANDATORY (ADR-011 §2.3 #2) — *결과* 의무`), §2.3 line 138 (`ADR-011 §2.3 #2 R-1 MANDATORY 미충족 risk`).

**모법 verbatim cross-check**:
- **ADR-011 §2.3 운영 함의 #2 (line 113)**: "**Hermes 자체 redaction은 로그/LLM 송신 방어로만 신뢰**: 저장 경로(DB/파일) 차단 책임 없음."
  → 이는 R-1을 *MANDATORY*로 선언하는 조항이 **아니다**. 오히려 Hermes redaction 의 신뢰 *범위를 한정*(scoping) 하는 조항 — "로그/LLM 송신 방어로만" 신뢰. "mandatory"라는 단어도, "필수 수단"이라는 의미도 §2.3 #2 에 없다.
- **governance-preconditions.md §2.1 line 342 (GP-2 row)**: 강제 메커니즘 = "Hermes native redaction (**보조** — ADR-011 §2.3 #2) + LLM facade redaction filter (P1)".
  → 모법은 R-1을 명시적으로 **보조(auxiliary)** 로 분류. "MANDATORY" 의 정반대.
- **governance-preconditions.md §4.1 line 424**: "GP-2 는 ADR-011 §2.3 운영 함의 #2 의 ***보조* 역할**. DB INSERT 차단은 GP-1 의 책임이며, GP-2 는 송신/로그 경로만 다룸. GP-2 단독으로 헌법 8조 본질 충족 시도 금지."

**판정**: 본 brief 가 §2.3 #2 를 "R-1 MANDATORY"의 근거로 인용한 것은 **권위 전도(authority inversion)** — 모법이 *보조*로 못박은 수단을 *필수*로 격상 인용. 이는 단순 오타가 아니라 R-4 채택 권고(§2.2)의 핵심 정당화 논리("R-1 = *결과* 의무, R-3 단독은 §2.3 #2 미충족 risk")를 모법에 반하는 방향으로 구축한 것. CLAUDE.md §7 의존 관계 "ADR-011 line 6/245 상위 권위 매핑 답습" 위반.

**정정 (3 중 택1, 사용자/Reviewer 결정 영역)**:
1. **(권고)** "R-1 = MANDATORY (ADR-011 §2.3 #2)" → "R-1 = **보조(auxiliary) 수단** (ADR-011 §2.3 #2 + GP-2 §4.1 line 424 verbatim) — Hermes native redaction 은 로그/LLM 송신 방어로만 신뢰되는 *보조* 역할". R-3 단독이 §2.3 #2 미충족이라는 §2.3 line 138 주장도 삭제 또는 정정 (R-3 = GP-2 §4.5 (d) 자동 회귀 경로의 *주(primary)* 충족 수단으로 모법 정합).
2. R-1 의 진짜 MANDATORY 근거를 찾는다면 그것은 §2.3 #2 가 아니라 GP-2 §4.5 (a) Exit ("Hermes native redaction Tier-1 42 catalog 적용 검증 + P1 facade redaction filter 검증") — 단 여기서도 "MANDATORY"가 아니라 *동등 이상 보안 결과를 위한 구성요소*. 정확 인용으로 교체.
3. R-4 defense-in-depth 채택을 유지하되, 정당화 논리를 "모법은 R-1을 보조로 한정하나, GP-2 ends(egress secret leak 0) 충족을 위해 R-1(보조) + R-2(facade) + R-3(CI canary) 다층을 *채택* — R-3 가 (d) 자동 회귀의 주 수단"으로 재구성 (모법 정합).

---

### R-B-2 (권위 인용 misattribution — BLOCKING) — "ADR-012 §2.1 R-2 / R-4.1 PoC 자동 재실행 trigger"는 §2.1에 부재

**위치**: 본 brief §0.2 #8 line 40, §3.1 L-2 row line 152, §3.2 #3 line 163, §3.3 L-5 row line 172, §11 line 359, §8 line 311. 본 brief 의 L-2/L-5 (외부 library) 영구 분리 정당화의 핵심 인용.

**모법 verbatim cross-check (ADR-012 full read)**:
- **ADR-012 §2.1 = "Evidence Ledger 보호 원칙 (12)"** (line 83~107). "의존성 추가 PoC 자동 재실행 trigger"는 §2.1 에 **존재하지 않는다**.
- 외부 library / 의존성 변경 시 PoC 재실행 trigger 의 실제 모법 위치:
  - **ADR-012 §3.2 (line 404)**: "Hash 알고리즘 변경 ... + 마이그레이션 trigger 정의" (의존성/알고리즘 변경 거버넌스).
  - **ADR-011 §2.3 운영 함의 #4 (line 115)** + **GP-2 §4.3 line 438**: "Hermes 의존성 업그레이드 시 R-2 / R-4.1 PoC 자동 재실행 (ADR-011 §2.3 운영 함의 #4)" — *"R-2 / R-4.1 PoC 자동 재실행"* 이라는 정확한 wording 은 **GP-2 §4.3 + ADR-011 §2.3 #4** 에서 온다. ADR-012 §2.1 이 아니다.
  - 외부 library supply-chain trigger 는 **governance-preconditions P11 (line 249, (e) tooling supply chain — `rfc8785` / `jcs` 명시) + (v) Vendor Change Auto-recheck** 가 더 정확한 권위.

**판정**: "ADR-012 §2.1" 은 misattribution. 모법에 없는 §번호 + 그 §번호에 부재하는 trigger 를 인용 → 권위 chain 부정확. BLOCKING (권고 8건 인용이 모두 동일 오류 답습 — single source of error cascade).

**정정**: "ADR-012 §2.1 R-2 / R-4.1 PoC 자동 재실행 trigger" → "**GP-2 §4.3 (line 438) + ADR-011 §2.3 운영 함의 #4 (line 115)** R-2 / R-4.1 PoC 자동 재실행 trigger (Hermes 의존성 업그레이드 시), 외부 library supply-chain 측면은 **governance P11 (e)+(v)** (`rfc8785`/`jcs` 명시 + Vendor Change Auto-recheck)". §11 cross-reference 표(line 359 "ADR-012 §2.1 (의존성 추가 PoC 재실행)")도 동일 정정.

---

### R-B-3 (실 PoC 시제 불일치 + 보안 결과 과장 — BLOCKING) — L-1 "Python stdlib 단독" 은 실 canonical_json.py 와 불일치, "외부 library 강제 의존 0" 은 사실 오류

**위치**: 본 brief §3.1 L-1 row line 151 (`Layer 1 hash chain Python stdlib 단독 (hashlib.sha256 + json.dumps(sort_keys, separators))`), §3.2 #1 line 161 (`L-1 (stdlib hash chain) = MVP 단계 정합 — 외부 의존성 0`), §3.2 #3 line 163 (`외부 library *강제 의존* 0`), §3.3 line 171 (`외부 의존 0`), §3.4 정합 line 165 (`stdlib 단독 (L-1) = "동등 이상 보안 결과"`).

**실 repo filesystem direct verify (`tools/canonical_json.py`)**:
- canonical 경로 = **`rfc8785` (Trail of Bits) Primary 1 + `jcs` (titusz) Primary 2 + `jq -S -c` subprocess fallback** (line 12~14, 34~41, 47~56, 78~90).
- **stdlib `json.dumps(sort_keys=True, separators=(",",":"))` canonicalization 경로는 실 코드에 부재** — Primary 는 외부 library(rfc8785/jcs), Fallback 은 `jq` (외부 *binary* subprocess, stdlib 아님).
- 즉 본 brief 가 L-1을 "stdlib 단독 (hashlib + json.dumps)" 로 기술한 것은 **PoC 시제 misdescription**. 실 시제는 외부 library Primary + 외부 binary fallback.

**보안 risk (canonical 우회 가능성, 사용자 임무 §3 질문 직답)**:
- 본 brief 주장 "RFC 8785 strict 정합 = fallback 동등성으로 확보, 외부 library *강제 의존* 0" (line 163) 은 사실과 반대. 실 시제는 rfc8785/jcs 가 *Primary* 이고 `jq` 가 *fallback*. ADR-012 §11.3 (line 646) + §2.5 (line 207) 가 명시: "fallback `jq -S -c` 가 JCS 와 *모든 케이스 동등* 보장 부재 — test corpus 검증 의무". 즉 **fallback 동등성은 모법 자체가 "모든 케이스 동등 보장 부재"로 한정한 것** — 본 brief 가 이를 "동등성으로 확보"로 표현하면 canonical 우회(jq fallback 이 JCS 와 미세 divergence 시 hash mismatch silent) risk 를 과소평가. 단 corpus 72 files + CROSS_CHECK mode (rfc8785+jcs byte 동등성 강제, canonical_json.py line 49/63) 가 완화 — 이 완화는 본 brief 가 언급한 "corpus 72 files" 보다 강하다 (CROSS_CHECK 가 핵심인데 brief 가 미언급).

**판정**: L-1 의 기술적 정체성(stdlib 단독)이 실 PoC 시제(외부 library Primary)와 불일치 + means-vs-ends "동등 이상 보안 결과 (ADR-011 §2.1 (a))" 논거의 사실 기반 오류. BLOCKING (P-4 자기진단이 "RFC 8785 strict 정합 과소평가" risk 를 인지했으나 정정 방향이 틀림 — fallback 동등성 강조가 아니라 CROSS_CHECK + corpus 가 실제 방어).

**정정**:
1. L-1 정체성 = "Python stdlib 단독" → "**rfc8785/jcs Primary + jq -S -c fallback + CROSS_CHECK mode (rfc8785+jcs byte 동등성 강제)** — 외부 library 는 *조건부 import (미설치 시 None + jq fallback)* 구조이므로 *강제 런타임 의존*은 아니나 *Primary 경로는 외부 library*". "stdlib 단독" 표현 삭제.
2. "외부 library 강제 의존 0" → "외부 library = *조건부 Primary* (미설치 시 jq fallback 으로 degrade) — 단 ADR-012 §11.3 'jq fallback 이 JCS 와 모든 케이스 동등 보장 부재' 답습, CROSS_CHECK mode + corpus 72 files 가 동등성 검증 layer".
3. L-2/L-5 "외부 library 도입 = 별도 cycle" framing 은 유지 가능 — 단 근거가 "L-1 은 외부 의존 0 이므로" 가 아니라 "**rfc8785/jcs 는 이미 조건부 import 시제로 존재**(canonical_json.py line 34~41), L-2/L-5 = 이를 *강제 의존 + pin* 으로 격상하는 결정 = governance P11(e) supply-chain trigger" 로 재구성. 실제로 본 brief §3.1 L-2 row(line 152)는 "canonical_json.py 에 rfc8785/jcs import 시도 + jq fallback 이미 존재"라고 옳게 인지 — 이 인지와 §3.2 #1 "stdlib 단독" 주장이 **자가 모순**. 모순 해소 필수.

---

## 권고 (N-B-N)

### N-B-1 — R-3 단독의 GP-2 ends 충족 여부 (사용자 임무 §1 직답, 권고 수준)

사용자 임무 질문: "R-3 단독이 GP-2 ends(secret leak 0)를 충족하는가, 아니면 R-1/R-2 부재가 defense-in-depth 를 위험하게 약화시키는가?"

**Agent B 판정**: 모법 정합 관점에서 **R-3(CI canary)는 GP-2 §4.5 (d) 자동 회귀 검증 경로의 주 충족 수단이지, GP-2 ends 자체의 단독 충족 수단이 아니다**. GP-2 §4.5 (a) Exit = "Hermes native redaction Tier-1 42 catalog 적용 검증 + P1 facade redaction filter 검증" — 즉 (a) 동등 이상 보안 결과는 *송신 시점 redaction*(R-1 보조 + R-2 facade)이 담당하고, R-3 는 *사후 회귀 검증*(이미 leak 된 secret 을 grep 으로 검출). R-3 단독 = "방어(prevention)"가 아니라 "검출(detection)" — secret 이 이미 송신/로그된 *후* grep. 따라서:
- R-3 단독은 GP-2 (d) 충족 ✅, (a) 미충족 (prevention layer 부재).
- R-1/R-2 부재 시 defense-in-depth 가 아니라 *detection-only* — secret 이 실제 leak 된 후에야 알 수 있음 (RT-R-1 이 정확히 이 risk 를 명시 — line 290).
- 그러나 본 brief 의 R-4 채택(R-3 우선 + R-1/R-2 cross-trajectory) 결론은 **타당** — R-1(보조)/R-2(facade)가 prevention, R-3 가 detection/회귀. 단 R-4 의 정당화를 "R-1 MANDATORY"(R-B-1 전도)가 아니라 "GP-2 §4.5 (a) prevention = R-1 보조 + R-2 facade / (d) detection = R-3" 로 재구성하면 모법 정합 + 보안 견고.

**권고**: §2.2 #1 ("GP-2 의 자동 회귀 검증 경로 (ADR-011 §2.1 (d)) = R-3 가 단독 충족")는 정확 — 유지. §2.3 trade-off 표 "R-3 단독 ... ADR-011 §2.3 #2 R-1 MANDATORY 미충족 risk" (line 138)는 R-B-1 전도 정정 후 "R-3 단독 = detection-only, prevention layer (R-1 보조 + R-2) 부재 → GP-2 (a) 미충족" 으로 교체.

### N-B-2 — base64 evasion(R-5) 영구 분리는 known limitation 으로 정당 (사용자 임무 §3 직답)

`tools/secret_scanner.py` line 32 verbatim: "base64 / URL-encoded / 압축 등 advanced evasion 미커버 (Hermes upstream R2-6 영역)". `secret-hygiene-egress-redaction.yml` 도 "base64 known limitation" 명시(본 brief §1.2 line 89). **R-5 영구 분리는 known limitation 으로 정당** — 모법(G3-4 MVP-2/3 분리) + 실 시제 docstring 양쪽이 명시. 단 권고: 본 brief §0.2 #11 + §2.1 R-5 row 에서 "영구 분리"가 *방어 부재의 은폐*가 아님을 명시하기 위해, R-5 = "MVP-2 detection scope 밖 *명시적 known limitation* (secret_scanner.py line 32 docstring + workflow 51791B 명문)" 로 evidence 인용 강화. 현 framing 도 수용 가능 — NOTE 수준.

### N-B-3 — W "보존 우선"이 누락(HISTORY_REWRITE enum fixture 등)을 은폐하지 않음 (사용자 임무 §3 직답)

사용자 질문: "W '보존 우선'이 기존 workflow 의 누락(HISTORY_REWRITE enum fixture 미커버 등)을 은폐하는가?"

**Agent B 판정: 은폐하지 않음**. 본 brief §4.2 #2 (line 195)가 "누락 영역 (예: timestamp monotonicity step / HISTORY_REWRITE enum fixture) = 기존 workflow 內 step 추가 (실 구현 sub-cycle)" 로 누락을 *명시적으로 식별 + 실 구현 sub-cycle 로 이관*. 이는 55 entry §2.4.1 B-1 (HISTORY_REWRITE Layer 분담) + §11.1 B-1 답습과 정합 — 55 entry 가 이미 "history_rewrite enum jsonl_ledger/fail fixture 추가 = 실 구현 sub-cycle 영역"(line 204)으로 명문. **은폐 0, 정합**. 단 권고: §7.1 조건부 승인 조건 6 표(line 281) "history_rewrite enum fixture 추가 = Layer 2 (L-3) 실 구현 sub-cycle" 와 §4.2 #2 cross-reference 를 명시적으로 연결 (현재 분산 — 두 곳을 한 줄 cross-ref 로 묶으면 추적성 강화).

### N-B-4 — W 결정 "명칭상 W-A(ii), 실질 보존 우선"의 투명성은 견고하나 51 audit W-A 와의 거리 명시 권장

본 brief §4.2 + §4.1 tension 명시(line 180) + P-2 자기진단(line 377)이 "51 audit W-A 권고 vs 실 repo 현 상태 tension 을 *임의 재해석*" risk 를 투명하게 처리 — 견고. 단 51 audit §4.2 의 "W-A 단일 R-6 통합" 원 권고와 본 brief 의 "보존 우선 minimal"은 *실질적으로 다른 결정*(통합 vs 비통합). 본 brief 는 "51 audit W-A 의 *정신*(ceremony-inflation 차단)을 실 repo 현 상태에 맞춰 정밀화"로 정당화 — 타당하나, 이는 사실상 **W-A 기각 + 신규 옵션 채택**에 가깝다. 권고: "W-A(ii) 변형"이라는 명칭 유지가 51 audit 와의 연속성을 *과장*할 수 있으므로, "51 audit W-A(단일 통합) = 실 repo 분산 운영과 비정합으로 **사실상 비채택**, 본 cycle = 신규 '보존 우선 minimal' 채택 (W-A 의 ceremony-inflation 차단 정신만 답습)" 로 정직하게 framing 강화. 이는 P-2 자기진단 정신과 정합.

### N-B-5 — 합의 형태 trigger 검증(§6.2)은 정합, 단 trigger 4 "부분 발화"가 R-B-1/R-B-2 BLOCKING 으로 격상 가능

본 brief §6.2 trigger 4 (권위 chain 다중 source 손상 위험) = "부분 발화 (R-S1 후행 영향, 평가 한정)". 그러나 R-B-1(§2.3 #2 전도) + R-B-2(§2.1 misattribution)는 *본 brief 자체가 권위 chain 을 손상*시키는 신규 발화 — R-S1(기존 ADR-012 §2.3 vs §2.8 numbering tension) 과 별개. 권고: trigger 4 발화 근거에 "본 brief 의 §2.3 #2 / ADR-012 §2.1 인용 정확성 = 풀 3+1 검증 핵심 영역" 추가 (BLOCKING 정정이 합의 입력의 주 대상임을 명시). 단 풀 3+1 적격성 결론(2/7 발화 + 1 부분)은 변동 없음.

### N-B-6 — RT-R-2 (defense-in-depth 약화 trigger)는 견고, RT 표에 R-3 detection-only 명시 권장

§7.2 RT-R-2 (line 291) "R-1/R-2 cross-trajectory 미충족 시 GP-2 defense-in-depth 약화" + RT-R-1 (line 290) "R-3 grep PASS 후 평문 leak" = 정확한 보안 risk 식별. R-B-1 정정 후 이 두 RT 가 핵심 안전장치 — 유지. 권고: RT-R-1 발화 조건에 "R-3 = detection-only, prevention(R-1 보조+R-2) 부재 시 leak 후 검출 한정" 명시.

---

## NOTE (NT-B-N)

### NT-B-1 — scope 침입 0건 (사용자 임무 §4 직답)

본 brief 의 실 구현 / 외부 library 도입 / Hermes import / facade real 침입 검증:
- §0.2 금지 24항목 (line 31~56) + §8 추가 금지 (line 308~315) = 실 코드 0 / tools 본문 0 / workflow 본문 0 / denyNonFastForwards 활성화 0 / 외부 library 도입 0 / Hermes import 0 / facade real 0 / base64 evasion 0 모두 명문 금지.
- §5.2 발효 영역 (line 219~225) = "*결정 발효*" 한정, 실 구현 = §5.3 deferred (line 227~233).
- **scope 침입 0건 확인**. 반대로 수단 *결정*을 회피하고 모호하게 남기는가? → **아니오**. §2.2 (R-4 채택) + §3.2 (L-4 채택) + §4.2 (W 보존 우선 채택)이 명확한 결정 권고 — "수단 결정 cycle"의 본업(51 후보 → 결정)을 회피 0. 단 R-B-1 전도가 R-4 의 *근거*를 왜곡할 뿐, R-4 *결정 자체*는 명확. NT 수준 (긍정).

### NT-B-2 — (γ-c) 특화 의무 4 정합 (사용자 임무 §5 직답)

gamma-decision-brief §1.3 (line 102~114) 의 특화 의무 4 cross-check:
1. **Layer subsection 강제** — 본 brief §5 통합 매트릭스 Layer 별 분리(line 213~217) + §7.1 조건부 승인 조건 6 #6 (Layer subsection 분리, line 282) 정합 ✅.
2. **"부분 답습" framing 영구 (Layer 3+5 scope 외)** — 본 brief §0.2 #19 (line 51) + §4.3 (line 204) 정합. **사용자 임무 §5 핵심 질문 (history-anchor-verifier.yml = Layer 5 PoC 시제 존재가 "보존"으로 Layer 5 진입을 유발하는가?)**: 본 brief §4.3 line 204 verbatim = "history-anchor-verifier.yml = Layer 5 External anchor PoC 시제 *이미 운영* — 55 B-2 답습. '보존' = PoC 시제 보존이지 Layer 5 *결정 영역 진입* 0". → **55 entry §2.4.1 B-2 (line 201/206) + §11.1 B-2 (line 510) 답습과 정확 정합** — "PoC 시제 존재 ≠ Layer 5 PASS 진입". **Layer 5 진입 유발 0건 확인** ✅.
3. **통합 동시 발효** — 본 brief §5.1 통합 의존(line 213) + §4.3 line 205 (W 보존이 통합 동시 발효 저해 0) 정합 ✅.
4. **RT-γ-6** — 본 brief §7.2 RT-γ-6 (line 295) + §10 #5 (line 349, "평가 한정, 정정 = 별도 cycle") = 55 entry B-8 ("의무" → "*평가* 의무" framing, line 516) 답습 정합 ✅.

→ **(γ-c) 특화 의무 4 전원 정합. RT-γ-6 의 "평가 한정 / 정정 별도 cycle" framing 도 55 B-8 verbatim 답습** (MVP-2 PASS 가 R-S1 정정에 종속 회피).

### NT-B-3 — denyNonFastForwards 미설정 = 실 repo verify 정합

filesystem direct verify: `git config receive.denyNonFastForwards` (local) + `--global` 모두 출력 0 = 미설정 확인. 본 brief §1.2 line 96 + layer-124-pass-brief §1.3 line 137 답습 정합 ✅. 활성화 = 실 구현 sub-cycle 영역(§0.2 #5, §7.1 조건 1) 으로 정확 이관.

### NT-B-4 — 실 repo workflow 12개 (brief 의 "5+" 표현 정합)

filesystem: .github/workflows/ 에 12 파일 (boundary-guard, evidence-pass-gate, g4-hash-chain, history-anchor-verifier, memory-skill-migration-feasibility, pre-commit-bypass-detection, provider-adapter-enforcement, provider-url-scanner, r2-canary, rewrite-defense, schema-validation, secret-hygiene-egress-redaction). 본 brief 가 GP-2/G4 관련 5개(line 180/194)를 "5+" 로 표기 — **"5+" 표현이 12개 중 GP-2/G4 scope 5개를 정확히 한정**. 과장 0. 단 권고(경량): "기존 5+ workflow" → "GP-2/G4 관련 5 workflow (전체 12 中)" 로 명시하면 보존 scope 의 정밀성 강화 (W "보존 우선"이 *전체* 12 보존인지 *관련* 5 보존인지 모호 회피).

### NT-B-5 — secret_scanner.py 의 ADR-011 §2.1 (a)~(e) 인용은 정확

`tools/secret_scanner.py` line 10 = "ADR-011-means-vs-ends-redaction.md §2.1 (a)~(e)". ADR-011 §2.1 실제 = (a)~(d) 4조건 (line 54~60) + (e) 후속 운영조건(§3 모법 역할 + 합의 APPROVE). 실 코드 인용 "(a)~(e)" 는 ADR-011 §2.1 + §3/§6 (e) 통합 표현으로 정합. 본 brief 도 ADR-011 §2.1 (a)~(e) 표현 일관 사용 — **ADR-011 §2.1 인용은 정확** (R-B-1/R-B-2 와 달리 §2.1 자체 인용은 견고). BLOCKING 은 §2.3 #2 (R-B-1) + ADR-012 §2.1 (R-B-2) 두 곳 한정.

### NT-B-6 — P10/Evidence Forgery / append-only 등 ADR-012 핵심 보호 원칙은 본 brief scope 외 (정합)

ADR-012 §2.1 (12 보호 원칙) / §2.7 (prev_hash BLOCK) / §2.8 (Full Rewrite 5 Layer) / §3.4 (timestamp monotonicity)는 Layer 1/2/4 hash chain + CI 회귀와 연결되나, 본 brief 의 L-4 결정이 이를 변경/약화 0. §7 evidence 요건(line 299~302)이 §2.7/§3.4 답습(timestamp monotonicity 위반 BLOCK, prev_hash 검출)을 실 구현 sub-cycle 로 정확 이관. 정합.

---

## 종합 (Agent B 관점)

- **결정의 방향(R-4 / L-4 / W 보존 우선)은 보안상 타당** — defense-in-depth(R-4) + stdlib/조건부 외부 library MVP 단계 정합(L-4) + 기존 분산 구조 보존(W). scope 침입 0, (γ-c) 특화 의무 4 전원 정합, Layer 5 진입 유발 0, base64 known limitation 정당.
- **그러나 결정의 *근거(권위 인용)* 가 BLOCKING 3건으로 손상**:
  - R-B-1: "R-1 MANDATORY (ADR-011 §2.3 #2)" = 모법(보조 역할)을 **정반대로 전도** — 최우선 정정.
  - R-B-2: "ADR-012 §2.1 PoC 재실행 trigger" = 모법에 부재하는 §번호 misattribution (정확 = GP-2 §4.3 + ADR-011 §2.3 #4 + governance P11).
  - R-B-3: L-1 "stdlib 단독" = 실 canonical_json.py(rfc8785/jcs Primary + jq fallback) 와 불일치 + "외부 library 강제 의존 0"의 사실 오류 + §3.1 L-2 row 와 자가 모순.
- **3건 모두 in-place v1.1 1pass 흡수 가능** (별도 v2 불필요, ceremony-inflation 차단 메모리 답습). 정정 후 R-4/L-4/W 결정 자체는 발효 적격.
- **REVISE** — 권위 인용 정확성은 means-vs-ends 거버넌스의 근간(ADR-011 line 61 "텍스트 해석으로 본질 회귀 차단" 모법)이므로, 전도/misattribution 은 APPROVE WITH CONDITIONS 가 아닌 REVISE 수준. 단 REJECT 아님 (결정 방향 타당 + 정정 경로 명확).

---

**Agent B 끝.**
