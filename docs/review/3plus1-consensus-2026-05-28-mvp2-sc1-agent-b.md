# 3+1 합의 — Agent B (품질/안전성 검증가) — MVP-2 SC-1 facade RedactionFilter 실 구현 brief

> **작성**: 2026-05-28 (65번째 entry cycle — 세션 #3)
> **관점**: "안전하고 견고한가?" (보안, 엣지케이스, 문서 정합성)
> **검토 대상**: `docs/phase0/mvp2-sc1-facade-redaction-implementation-brief.md` (v1)
> **독립 분석**: Agent A/C 및 외부 LLM 응답 미참조. 권위 문서 + 실 코드 직접 read.

---

## 1. 판정

### **APPROVE WITH CONDITIONS**

brief 의 *명칭 정직성* (over-claim 차단), *scope 경계*, *RT-1 window 안전성*, *secret_scanner 변경 0 보존 의도*, *false positive 인식* 은 모두 견고하다. **다만 BLOCKING 3건** — (B-1) catalog 재사용 옵션 (i) 의 실현 가능성을 brief 가 *과소평가* (tools/ 비-package + sys.path hack 이 src 런타임에 침투), (B-2) `[REDACTED]` 치환 권위의 *오귀속* (`is_redaction_marker_match` 는 치환 함수가 아님 — secret_scanner 에 치환 로직 자체가 0), (B-3) 송신 redaction (`redact_messages`) 의 권위 출처를 brief 가 §8.2 로 인용하나 §8.2 에는 송신/request body redaction 이 *부재* (실 권위는 64 trajectory brief §4.4 (R-2-a)). 이 3건은 구현 *전* 정정 가능하며 결정 자체를 뒤집지 않으므로 REVISE 가 아닌 APPROVE WITH CONDITIONS.

---

## 2. BLOCKING (구현 전 정정 필수)

### B-1. catalog 재사용 옵션 (i) 실현 가능성 과소평가 — `tools/` 는 import 가능 package 가 *아님*

**brief 인용** (§2.1 표 옵션 (i), line 71): "RedactionFilter가 `tools.secret_scanner.COMPILED_PATTERNS` import … **src(런타임) → tools(개발도구) 역방향 의존** (아키텍처 부적절, .importlinter root=src 밖이라 **미차단이나 nonidiomatic**)".

**실 코드 검증 (모순)**:
- `tools/__init__.py` **부재** → `tools` 는 Python package 가 아니다. `import tools.secret_scanner` 는 *추가 조치 없이 실패*.
- 프로젝트에 `pyproject.toml` / `setup.py` / `setup.cfg` / `pytest.ini` / 루트 `conftest.py` **모두 부재** → `tools/` 를 src 에서 import 가능하게 만드는 packaging layer 가 *전무*.
- 기존 패턴 증거: `tests/tools/test_jsonl_hash_chain.py` line 16 = `sys.path.insert(0, str(_ROOT / "tools"))` 후 `import jsonl_hash_chain` (line 18). 즉 본 프로젝트는 `tools/` 모듈 접근 시 **sys.path 조작** 을 *test 코드에서* 사용 — clean package import 가 *아님*.
- secret_scanner 는 CI/hook 에서 **standalone script** (`python tools/secret_scanner.py …`, `.pre-commit-config.yaml:45`, `secret-hygiene-egress-redaction.yml:113`) 로만 호출. import 사례 0건.

**위험**: 옵션 (i) 를 채택하면 **런타임 src/ 코드** (RedactionFilter) 가 `sys.path` hack 또는 packaging 신설을 강제당한다. 이는 brief 가 표현한 "nonidiomatic" 수준이 아니라 (a) 런타임 import 신뢰성 risk (작업 디렉토리 의존), (b) Provider Liquidity facade 의 부작용 없는 import 원칙과 충돌, (c) `.importlinter` 가 `root_packages = src` 라 *src→tools 를 아예 인지조차 못 함* (검출 불가 = silent 의존). **brief §2.1 의 옵션 (i) "변경 최소" 라는 평가는 packaging 현실을 반영하지 않음**.

**정정 요구**:
1. §2.1 옵션 (i) 단점에 "tools/ 비-package (`__init__.py` 0) + pyproject 부재 → src 런타임 import 시 sys.path 조작 강제" 를 명문화.
2. **권고 재평가**: 옵션 (i) 우선 권고를 *유지하려면* tools/ packaging 신설 (또는 src 내부로 catalog 이전)을 동반해야 한다 — 이는 사실상 옵션 (ii) (공유 모듈 추출) 와 수렴. 따라서 본 Agent B 는 **옵션 (ii) (공유 모듈 추출, secret_scanner + RedactionFilter 공유) 를 권고 후보로 승격** 하되, secret_scanner 변경 = R-7(b) 차등 자격 평가를 §2.1 fallback 이 아닌 *주 경로* 로 명문화할 것을 요구. (단 catalog *패턴 내용* 변경 0 은 유지 — import 구조만 변경, B-1 정정과 §0.2 #5 양립 가능: 공유 모듈로 *옮기되* 패턴 문자열은 byte-identical.)
3. 최소안 (변경 충돌 최소화): 옵션 (iv) (§8.2 자체 패턴) 을 RT-2 fallback 으로 격상 — Tier-1 45 catalog 미사용 시 커버리지는 ↓ 하나 src→tools 의존 0 + secret_scanner 변경 0 동시 충족. 풀 3+1 에서 (ii) vs (iv) trade-off 결정 필요.

---

### B-2. `[REDACTED]` 치환 권위 오귀속 — `is_redaction_marker_match` 는 *치환* 함수가 아니다

**brief 인용** (§2.2, line 89): "`[REDACTED]` 치환 (secret_scanner `is_redaction_marker_match` 답습 — redaction marker 정합)."

**실 코드 검증 (모순)**:
- `tools/secret_scanner.py` 에는 **치환(substitution) 함수가 0건**. `re.sub` / `.sub(` / `str.replace` 사용 0건. scanner 는 *검출 전용* (`scan_text` → `Violation` 리스트 반환).
- `is_redaction_marker_match` (line 222~228) 는 **detection-side false-positive 회피용** — scan-log mode 에서 *이미 redact 된* 출력 (`OPENAI_API_KEY=[REDACTED]`) 을 위반 미카운트하기 위한 marker *인식* 함수. **secret 을 `[REDACTED]` 로 *바꾸는* 함수가 아니다**.
- `[REDACTED]` literal 은 `REDACTION_MARKER_RE` (line 183~185) 의 *탐지 대상 marker 집합* 일 뿐, scanner 가 *생성* 하는 출력이 아니다.

**위험**: brief 가 "답습" 으로 인용한 함수가 brief 가 의도한 동작 (secret → `[REDACTED]` 치환) 을 *수행하지 않음*. 이는 (a) 권위 인용 정합성 위반 (메모리 `feedback_pass_scope_overclaim` 의 "evidence 실증 vs framing 분리" 답습 대상), (b) 구현자가 "기존 함수 재사용" 으로 오인할 risk. **secret_scanner 는 검출만 제공 — RedactionFilter 의 *치환 로직* 은 신규 작성** 이라는 사실이 brief 에 명시되어야 한다 (catalog *패턴* 만 재사용, 치환은 신규).

**정정 요구**:
1. §2.2 line 89 의 "(secret_scanner `is_redaction_marker_match` 답습)" 삭제 또는 "marker literal `[REDACTED]` *정합* (단 secret_scanner 는 치환 미제공 — 치환 로직 신규)" 로 정정.
2. §0.3 / §2.1 에 "secret_scanner = 검출(detection) 전용, 재사용 대상 = *패턴 catalog* (COMPILED_PATTERNS) 한정. *치환(redaction substitution) 로직은 RedactionFilter 신규*" 명문화.
3. T-5 `scrub` redaction marker 정합 검증 시 `is_redaction_marker_match` 와의 round-trip (RedactionFilter 출력 `[REDACTED]` 가 scan-log mode 에서 미카운트) 을 *명시적 contract test* 로 추가 — detection↔prevention marker 정합 (silent drift 차단). 이는 GP-2 D-2 회귀 (secret-hygiene CI) 와 prevention 의 *단일 marker source* 보장.

---

### B-3. 송신 redaction (`redact_messages`) 권위 출처 = §8.2 *아님* — 실 권위는 64 trajectory brief §4.4

**brief 인용** (§0.3 line 45, §3 line 96): "llm-providers-design.md **§8.2** (RedactionFilter 설계)" + §3 "governance §4.1 line 422 verbatim 'LLM API request body 에 secret 노출 차단'".

**권위 cross-verify (모순)**:
- `llm-providers-design.md` §8.2 (line 518~538) = `RedactionFilter.scrub` — docstring "모든 **응답·예외·메트릭** 에서 비밀값 자동 strip". **`redact_messages` / 송신 / request body 에 대한 언급 0건** (전 파일 grep 확인). §8.1 callback 도 응답/메트릭 (`record = self._redactor.scrub(record)`).
- §4.4 호출 흐름 step 5 = "메트릭 기록 (redaction 적용)" — *메트릭* redaction. *송신* redaction step 부재 (step 3 = "LiteLLM Router 에 위임" 으로 *송신은 redaction 없이* 진행).
- 즉 **§8.2 의 RedactionFilter 는 *egress (응답/로그/메트릭)* redaction 설계** — brief 의 핵심 (송신 request body redaction = `redact_messages`) 은 **§8.2 를 *확장* 한 신규 역할**.
- 실 권위: 64 trajectory brief §4.4 (R-2-a, line 157) = "RedactionFilter (**request body Tier-1 42 redaction**)" + (R-5 line 161) "facade 진입점이 LLM API request body 통과 지점 … redaction은 facade real에 부착 필수". → 송신 redaction 의 직접 권위는 **64 trajectory 합의** (풀 3+1 + codex APPROVE WITH CONDITIONS) 이지 §8.2 *설계 명세* 가 아니다.
- governance §4.1 line 422 = "stdout / stderr / log file / **LLM API request body** 에 secret 을 노출하지 않도록 … 사전 차단한다" — request body 송신 차단 *목적* 은 명시. 단 brief 가 "**verbatim** 'LLM API request body 에 secret 노출 차단'" 이라 인용한 문자열은 line 422 와 *축자 일치하지 않음* (line 422 는 "노출하지 않도록 … 사전 차단한다"). **paraphrase 를 verbatim 으로 표기** = 인용 정합성 위반.

**위험**: (a) "§8.2 설계 명세 직접 답습" 이라는 framing 은 **송신 redaction 이 *기존 설계에 이미 명세됨* 으로 오인** 시킨다 (실제는 설계 *확장*). 이는 over-claim cascade risk (메모리 답습). (b) 설계 확장 = SDD §1 "문서가 코드 우선 / 불일치 시 문서 기준 수정" 과 충돌 가능 — *확장* 이면 llm-providers-design §8.2 본문에 `redact_messages` 역할을 *후속 반영* 의무가 발생 (§0.2 #8 "llm-providers-design 본문 변경 0" 과 긴장). 본 cycle 에서 본문 변경은 하지 않더라도 "설계 확장이며 §8.2 본문 반영은 후속" 임을 *명문화* 해야 SDD 정합.

**정정 요구**:
1. §0.3 / §3 의 "§8.2 (RedactionFilter 설계 — … 블랙리스트 채택)" 인용을 "§8.2 = *egress (응답/예외/메트릭) redaction* 설계. 본 cycle 의 *송신 (request body) redaction* = §8.2 *확장* (직접 권위 = 64 trajectory brief §4.4 (R-2-a) + governance §4.1 request body *목적*)" 로 정정.
2. §3 line 96 의 "(governance §4.1 line 422 **verbatim** …)" 에서 "verbatim" 삭제 (paraphrase 임을 인정) 또는 line 422 축자 문자열로 교체.
3. §0.2 / §8 에 "송신 redaction = §8.2 설계 *확장* — llm-providers-design §8.2 본문 `redact_messages` 역할 반영은 *후속* (본 cycle 본문 변경 0, SDD 후속 반영 의무 명시)" 추가.

---

## 3. 권고 (BLOCKING 아님)

### 권고-1. `system` 필드 redaction 누락 risk (§4.1 vs §4.3 불일치)

§3 line 96 = "`req.messages` (+ `system`) 을 `redact_messages()` 통과". 그러나 §4.1 step 1 = `redact_messages(req.messages)` (system 인자 부재) + §4.3 = "현 placeholder 시그니처 (`alias, messages, metadata`) 기반 … `system` 필드 없음 (설계 §4.1 의 `system` 은 deferred)". → **현 placeholder 에 `system` 필드가 없으므로 송신 secret leak 경로 중 하나 (Anthropic system prompt) 가 본 cycle redaction *밖***. brief 는 이를 §4.3 "최소 변경" 으로 정당화하나, **GP-2 prevention 의 *완전성* 관점에서 system prompt 도 request body 의 일부** (secret 평문 노출 가능). 권고: §3 의 "(+ system)" 표현을 삭제 (현 placeholder 미지원) 하거나, system 필드 추가 + redaction 을 본 cycle 범위에 포함. 최소한 §9 Rollback / known limitation 에 "현 cycle redaction = messages 한정, system 필드 redaction = facade 시그니처 개편 sub-cycle (deferred)" 명문화 (silent gap 차단).

### 권고-2. `metadata` 필드 redaction 미언급

현 placeholder `LLMRequest(alias, messages, metadata)` 의 `metadata: dict[str, Any]` 도 송신 시 직렬화되면 secret leak 경로. brief 의 `redact_messages` 는 messages 만 처리. metadata redaction 여부를 §3 / §4.1 에 명시 (포함 또는 deferred + 근거).

### 권고-3. T-3 catalog 대표 패턴 검증의 "변경 0건" 회귀 lock 보강

T-3 (§5.1) = "Tier-1 45 catalog 대표 패턴 각 1+". 권고: RedactionFilter 가 사용하는 패턴 source 가 secret_scanner `ALL_PATTERNS` 와 *동일 객체/카운트* 임을 검증하는 test 추가 (예: `len(RedactionFilter patterns) == len(secret_scanner.ALL_PATTERNS) == 45` + id 집합 동일). 이는 detection↔prevention single-source 보장 (drift = silent 보안 구멍) + R-4.1 "변경 0건" 의 *계산적 강제* (CLAUDE.md §2 "계산적 검증 우선"). 현 T-3 ("대표 패턴 각 1+") 은 single-source *전수* 보장에 불충분.

### 권고-4. base64 evasion known limitation 의 *능동* 명문 (T-4 와 분리)

RT-4 (§9) + §0.2 #6 = base64 evasion = R-5 영구 분리. 권고: T-4 (false positive) 와 *별도* 로 "T-(known-limit): base64-encoded secret → 미검출 (의도된 한계, R-5)" 를 *assert 가 아닌 문서화 test* (xfail 또는 docstring) 로 명시 — 후속 구현자가 "redaction 통과 = secret 없음" 으로 오신뢰하는 것 차단. secret_scanner docstring (line 31~32) 이 이미 base64 미커버를 명시하므로 RedactionFilter 도 *동일 한계* 임을 상속 명문.

### 권고-5. RT-1 선부착 보장의 *강제 메커니즘* 명문 (현재 절차적 권고에 그침)

§4.2 = "SC-Provider Liquidity (Router) 가 본 SC-1 *후* 진입 → 선부착". 그러나 이는 *순서 권고* 일 뿐 *강제* 가 아니다. Router sub-cycle 작성자가 redaction 부착을 누락하면 window 재발. 권고: facade `complete()` 의 NotImplementedError 본문 (§4.1 step 2) 에 "Router 위임 추가 시 redaction *후* 송신 의무 — redaction 미통과 송신 = RT-1 위반" 주석 + 향후 Router sub-cycle 의 Entry 조건에 "redaction layer 부착 contract test green 선행" 을 *계산적 게이트* 로 등록. brief §9 RT-1 대응을 "선부착 (§4.2)" 절차 참조에서 *test gate* 로 승격.

### 권고-6. 외부 의존성 0 (stdlib) 보존 명문 — RedactionFilter 도 동일

secret_scanner docstring (line 17) = "외부 의존성 0건 (custom scanner 단독)". catalog 재사용 시 RedactionFilter 도 `re` (stdlib) 한정 의존이어야 함 (Provider Liquidity facade 의 부작용/의존 최소 원칙). §verify (§5.4) 에 명문화 권고.

---

## 4. NOTE (관찰)

- **N-1 (명칭 정직성 견고)**: §0.1 line 7 (facade *redaction layer* real ≠ full facade real) + §0.2 #2 (full facade real 0) + §11 P-1/P-2 자기진단 = over-claim cascade (세션 #2 4회) 답습이 *명시적이고 일관됨*. R-2 prong 한정 / R-1 = SC-2 별도 / full GP-2 PASS = SC-3 후 (§0.2 #3, §1, line 235) 구분이 정확. 메모리 `feedback_pass_scope_overclaim` 충실 답습 — **본 항목은 BLOCKING/권고 사유 0**.
- **N-2 (scope 경계 견고)**: §0.2 "하지 않는 것" 10개 (LiteLLM 설치 0 / Router 0 / full facade real 0 / full GP-2 PASS 0 / R-1 0 / Tier-2·3 0 / detection·MVP-2 PASS 재선언 0 / ADR·헌법 본문 0 / yaml 0 / 자동 SC-2·SC-3 0) 가 본문 §3~§7 에서 일관 유지. §4.1 step 2 = redaction *후* 명시적 `NotImplementedError` (Router deferred) = scope 경계의 *코드 레벨 강제*. 침입 0 확인.
- **N-3 (catalog count 정합)**: brief "45 = baseline 5 + prefix 31 + regex 7 + alternation 2" = secret_scanner `ALL_PATTERNS` docstring (line 169) 및 실 리스트 (BASELINE_PREFIX 5 + PREFIX_PATTERNS 31 + REGEX_PATTERNS 7 + ALTERNATION_PATTERNS 2) 와 *정확 일치*. R-2-c 인용 정합.
- **N-4 (R-4 §7.3 인용 정합)**: brief §0.3 "redaction-pattern-equivalence.md (R-4 — … Hermes 안전성 선언 금지 §7.3)" — 단 §7.3 본문은 "trigger 마스킹 vs 차단 정책" (line 362). "Hermes 안전성 선언 금지" 는 **§7.3 가 아니라 ADR-011 §7.3** (R-4 line 39 = "ADR-011 §7.3 '본 ADR은 Hermes 안전성을 선언하지 않는다'"). brief 의 "§7.3" 귀속이 R-4 자체 §7.3 인지 ADR-011 §7.3 인지 모호 — 경미하나 정정 권장 (BLOCKING 아님, §7 매트릭스 참조).
- **N-5 (false positive 인식 견고)**: §3 line 101 + RT-3 + P-5 + T-4 = "Tier-1 catalog 는 secret 패턴 한정 매칭, 정상 대화 손상 아님" 인식이 명확. 단 ALTERNATION_PATTERNS (T1-041/042) 의 word-boundary FP 정정 이력 (secret_scanner line 156~159, b1-PC1-D6 합의) 이 *URL/body key=value* 매칭이라 정상 산문 텍스트에 `token=...` / `key=...` 가 포함되면 FP 가능 — T-4 가 이 edge (산문 내 `key=value`) 를 포함해야 충분. 권고-3/T-4 보강으로 흡수.
- **N-6 (TDD/커버리지 정합)**: §5 RED→GREEN→REFACTOR + 70%+ (CLAUDE.md §1) + verify 4종 (pytest / import-linter / scan-source / jarvis 회귀) 정합. import-linter 보존 (litellm import 0) = `.importlinter` forbidden (openai/anthropic/litellm/ollama) 와 일관. 단 본 cycle 이 catalog 옵션 (i) 채택 시 src→tools 의존은 `.importlinter` 가 *검출 못 함* (root=src 밖) → verify §5.4 가 이 의존을 잡지 못함 (B-1 silent risk 의 verify 사각). 옵션 (ii)/(iv) 채택 시 해소.
- **N-7 (작성자 메타 편향 자각)**: §11 P-7 = "작성자 = 64 작성자 (Claude) cascade → cross-vendor codex + 풀 3+1 독립 검증" 자각 명시. 적절.

---

## 5. 권위 인용 cross-verify 매트릭스

| # | brief 인용 (위치) | 실제 문서 | 판정 |
|---|------------------|----------|------|
| 1 | §8.2 RedactionFilter = PATTERNS 4 + KEY_BLACKLIST 6, 블랙리스트 채택 (§0.3, line 45) | llm-providers-design §8.2 line 524~538: PATTERNS 4개 + KEY_BLACKLIST 6키 + "블랙리스트 채택" (line 538) | ✅ **일치** |
| 2 | §8.2 RedactionFilter = 송신 redaction 설계 (§0.3, §3 함의) | §8.2 docstring = "**응답·예외·메트릭**" (line 522). 송신/request body/`redact_messages` 언급 **0건** | ❌ **모순 (B-3)** — §8.2 = egress 설계, 송신은 *확장* |
| 3 | §4.1 facade complete() 흐름 (§0.3) | llm-providers-design §4.1 line 264~275 = `complete()` 존재. 단 §4.1 흐름엔 redaction step 부재 (정규화·메트릭만) | ⚠️ **부분** — complete() 존재 ✅, 흐름 내 *송신* redaction step 부재 |
| 4 | §4.4 호출 흐름 step 5 = redaction 적용 지점 (§0.3, §3 line 98) | §4.4 line 327 step 5 = "메트릭 기록 (redaction 적용)" = *메트릭* redaction (송신 아님) | ⚠️ **부분** — step 5 = 메트릭 redaction (brief 도 §3 line 98 에서 이를 "보조" 로 정정 — 정직) |
| 5 | governance §4.1 line 422 verbatim "LLM API request body 에 secret 노출 차단" (§3 line 96) | line 422 실문 = "… LLM API request body 에 secret 을 노출하지 않도록 native redaction … + LLM facade redaction filter (P1 v2 §8.2) 가 사전 차단한다" | ⚠️ **paraphrase (verbatim 아님)** — 목적 정합 ✅, "verbatim" 표기 부정확 (B-3) |
| 6 | governance §4.5 (a) facade redaction filter 검증 (§0.3, §1 line 59) | §4.5 (a) line 451 = "Hermes native redaction Tier-1 42 catalog 적용 검증 **+** P1 facade redaction filter 검증" | ✅ **일치** — brief 가 R-2 prong (facade filter) = (a) 의 *부분* (R-1 = SC-2) 으로 정확히 분리 |
| 7 | governance §4.1 "GP-2 = ADR-011 §2.3 #2 보조 / DB 차단 = GP-1" (brief 미인용이나 정합 확인) | §4.1 line 424 = "GP-2 는 ADR-011 §2.3 운영 함의 #2 의 *보조* … DB INSERT 차단은 GP-1 … GP-2 단독으로 헌법 8조 본질 충족 시도 금지" | ✅ brief §1 "R-2 prevention prong" framing = GP-2 *보조* 위계와 정합 (over-claim 0) |
| 8 | ADR-009 §2.2 facade 단일 진입점 의무 (§0.3, §7) | ADR-009 §2.2 line 66~75 = MVP 6 의무 (LiteLLM import = facade.py 한정 #1, provider SDK 직접 import 금지 #2 …) | ✅ **일치** — brief §7 (facade 단일 진입점 보존) 정합. 단 brief 가 "§2.2 = 단일 진입점 *의무*" 라 인용하나 §2.2 제목은 "MVP 진입 *의미*" (의무 표는 §2.2 내부) — 경미, 실질 일치 |
| 9 | secret_scanner Tier-1 45 catalog (baseline 5 + prefix 31 + regex 7 + alternation 2), ALL_PATTERNS/COMPILED_PATTERNS/scan_text, stdlib 의존 0 (§0.3) | secret_scanner line 56~169 (5+31+7+2=45) + line 166 ALL_PATTERNS + line 172 COMPILED_PATTERNS + line 231 scan_text + line 17 "외부 의존성 0건" | ✅ **일치** |
| 10 | `[REDACTED]` 치환 = secret_scanner `is_redaction_marker_match` 답습 (§2.2 line 89) | secret_scanner line 222~228 = marker *인식* (detection FP 회피). 치환 함수 **0건** (re.sub/replace 0) | ❌ **모순 (B-2)** — 인식 ≠ 치환, secret_scanner 는 검출 전용 |
| 11 | R-4.1 "Tier-1 45 patterns 변경 0건" / R-7(b) 차등 (§0.2 #5, §2.1) | r4-1 evidence + secret_scanner docstring line 13 "변경 0건" + scope-policy (line 189~193) "catalog 본문 변경 = R-7(b) 차등" | ✅ **일치** — 단 B-1 (옵션 (ii) 공유 모듈 추출 = secret_scanner *파일* 변경) 이 "변경 0건" 과 긴장 → §2.1 fallback 처리는 정합 (패턴 *내용* 0 vs *파일 구조* 변경 구분) |
| 12 | RedactionFilter = facade 내부 협력자 + RT-1 atomic (64 brief §4.4) (§0.3, §4.2) | 64 trajectory brief line 161 (R-5) "facade 내부 협력자 … 분리 시 redaction 미부착 window (RT-1)" + line 157 (R-2-a) "request body Tier-1 42 redaction" | ✅ **일치** — 송신 redaction 의 *실 권위* (B-3 정정 후 인용 source) |
| 13 | redaction-pattern-equivalence "Hermes 안전성 선언 금지 §7.3" (§0.3) | R-4 §7.3 = "trigger 마스킹 vs 차단" (line 362). "Hermes 안전성 선언 금지" = **ADR-011 §7.3** (R-4 line 39 인용) | ⚠️ **§ 귀속 모호** (N-4) — 본질(안전성 선언 금지) ✅, § 번호 출처 정정 권장 |

---

## 6. 종합

**APPROVE WITH CONDITIONS**. brief 의 *governance 위계 정합* (GP-2 = 보조, R-2 prong 한정), *over-claim 차단* (facade redaction layer ≠ full facade real), *scope 경계 코드 강제* (redaction 후 NotImplementedError), *false positive 인식*, *변경 0건 의도* 는 견고하며 세션 #2 교훈을 충실히 답습한다. **BLOCKING 3건** (B-1 catalog 옵션 (i) packaging 현실 과소평가 / B-2 `[REDACTED]` 치환 권위 오귀속 / B-3 송신 redaction 권위 = §8.2 아님, 64 trajectory) 은 *권위 인용 정합성* + *구현 안전성* 의 정정이며 결정 자체를 뒤집지 않는다. 구현 *전* 정정 후 TDD 진입 가능.

**핵심 안전 메시지**: secret_scanner 는 *검출만* 제공한다. RedactionFilter 의 (a) catalog import 경로 (B-1), (b) 치환 로직 (B-2), (c) 송신 적용 (B-3) 은 모두 *신규* 이며 §8.2/secret_scanner 의 "답습" 으로 과대 포장되어선 안 된다 — 이는 R-2 prevention 의 *실 구현 분량* 을 정직하게 드러내고 over-claim cascade 를 차단한다.

---

**Agent B 검토 끝.**
