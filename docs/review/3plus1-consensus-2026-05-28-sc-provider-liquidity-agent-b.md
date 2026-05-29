# 3+1 합의 — SC-Provider Liquidity (facade Router 위임 real) — Agent B (품질/안전성 검증가)

> **작성**: 2026-05-28 (세션 #4, 69번째 entry 진입 cycle)
> **Agent**: B (Quality & Safety Reviewer) — 렌즈: "안전하고 견고한가?" (보안 / 엣지케이스 / 문서 정합성 / over-claim 정직성)
> **검토 대상**: `docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md` (v1)
> **독립성 (Phase 2)**: 본 검토는 Agent A / Agent C / 외부 codex 의 결론을 *보지 않고* 직접 filesystem read 만으로 작성. 인용은 file:line 명시.

---

## 0. 판정

### **APPROVE WITH CONDITIONS**

설계 의도(RT-1 선부착 / Min2+동일type / LLMMetadata 화이트리스트 / lazy import hermetic / over-claim 차단 framing)는 안전/품질 관점에서 견고하다. brief §0/§11/§14 의 over-claim 차단 framing 은 65 cascade 교훈을 충실히 답습한다(독립 판단 §5 참조). **단, 구현 진입 전 해소해야 할 BLOCKING 4건** — 그중 2건은 *권위 정합성*(P11 Implementation 위상 + 설계 §15 ↔ Core MVP 분할 모순), 2건은 *보안 실증 정밀성*(RT-1 동치 검증의 spec 강제 + 응답 redaction 누출 통로 0 주장의 미입증)이다. BLOCKING 해소 후 brief v1.1 흡수 + 구현 진입 적격.

---

## 1. BLOCKING 항목 (구현 진입 전 해소 의무)

### **B-BLOCK-1 — 설계 §15 "12 보강 모두" ↔ Core MVP 분할 모순 미해소 (SDD 정합성)**

- **근거**: `llm-providers-design.md:773` — MVP(v1.0) 정의 = "LiteLLM facade + ... + **12 보강 모두**", 진입조건 = "본 설계 재합의 통과". 그리고 `llm-providers-design.md:6` 상태 = "초안 v2 ... 재합의 대기" + `:827` "이 문서는 3+1 에이전트 재합의를 통과해야 확정됩니다."
- **문제**: brief §7(line 199~206)은 본 풀 3+1 합의로 설계 status 를 `재합의 대기` → `확정 v2` 로 flip 하면서, *동시에* 구현은 Core MVP(streaming/OAuth/degraded/metrics/race 5종 deferred)만 한다. 즉 **설계가 자기 §15 에서 "v1.0 = 12 보강 모두"라고 선언한 상태로 "확정" 승격하면, 5종 deferred 구현은 "확정된 v1.0 명세 미달"이 된다.** brief 는 이 모순을 §7(line 206)에서 "Reviewer 판단 대상"으로 *지목만* 하고 *해소안을 제시하지 않는다*.
- **SDD 위반 위험**: CLAUDE.md §1 SDD = "문서 우선 / 미확정 설계 구현 금지". 설계 §15 가 v1.0 범위를 "12 보강 모두"로 못 박은 채 status 만 "확정"되면, *문서(§15)와 구현(Core MVP)이 즉시 불일치* → 다음 세션이 "확정된 v1.0 인데 왜 streaming 없나"를 다시 재합의해야 하는 cascade 유발.
- **해소 요구**: brief v1.1 이 둘 중 하나를 *명시*해야 함 — (옵션 1) 설계 §15 의 v1.0 row 를 "Core MVP(complete 경로) + 12 보강 *deferred phase 명세 존속*"으로 *갱신*하는 것을 본 합의 산출에 포함, 또는 (옵션 2) status flip 을 `확정 v2 (Core MVP 한정, §15 deferred phase 별도)` 로 *조건부 승격*. 둘 다 아닌 "단순 확정 flip + §15 미수정"은 SDD 불일치를 코드 진입과 동시에 발생시킴.

---

### **B-BLOCK-2 — RT-1 응답 redaction deferred 의 "누출 통로 0" 주장 미입증 (보안 핵심)**

- **근거**: brief §3(line 118) — "응답 redaction(`scrub`)은 metrics callback(deferred)과 함께. Core MVP는 응답 본문을 사용자에게 그대로 반환 ... 응답이 로그/메트릭에 기록되는 경로 0(callback deferred)이므로 응답 redaction 미부착 = 누출 통로 0 (검증)."
- **문제**: 이 주장은 **3개 미입증 전제**에 의존하며, brief §8.1 의 TDD 계획에 *이를 강제하는 test 가 없다*:
  1. **LiteLLM Router 자체가 응답/예외를 로깅하지 않는다는 보장이 없다.** `litellm.Router` 는 내부적으로 success/failure 시 자체 로깅·verbose 출력·`litellm.set_verbose`/내장 callback 등을 가질 수 있다 — 본 cycle 이 `DomainMetricsCallback` 을 deferred 해도 *litellm 라이브러리 기본 로깅이 응답을 stdout/파일로 흘릴 가능성*은 차단되지 않았다. "callback deferred = 누출 0"은 *본 프로젝트 callback* 만 고려하고 *litellm 내장 로깅*을 누락.
  2. **응답 본문이 secret 을 포함할 수 있다** (예: LLM 이 echo 한 입력, tool output 반환). 그 응답이 `_normalize` 후 caller 에게 그대로 반환되고, caller(자비스 PMO/tmux 워커)가 이를 로그/DB 에 기록하면 P2(송신/로그 평문 노출) 재발 — facade 책임 경계 밖이라도 *brief 가 "누출 통로 0"이라고 단정*한 것은 over-claim 소지.
  3. **예외 경로**(brief §6.2 line 188 `except litellm.AuthenticationError: raise`): re-raise 되는 litellm 예외 메시지에 redacted 되지 않은 url/api_key/토큰이 포함될 수 있다(litellm 예외는 종종 endpoint·헤더 fragment 포함). 이 예외가 상위로 전파되어 로깅되면 누출. brief §8.1 T-E 는 "AuthenticationError re-raise"만 검증하고 *예외 본문 redaction*은 검증 안 함.
- **해소 요구**: brief v1.1 이 (a) litellm 내장 로깅 비활성화(`litellm.set_verbose=False` 또는 동등) 의무를 §6.2 흐름에 명문 + test 강제, (b) "누출 통로 0" 단정을 "**송신 경로(request body) 누출 0; 응답/예외 redaction = deferred(metrics callback 동반) — 응답/예외 경로 누출 위험은 별도 sub-cycle 에서 차단**"으로 *정직하게 축소* 재서술(P2 over-claim 차단), (c) T-E 에 예외 메시지가 raw secret/endpoint 를 노출하지 않는지(또는 caller 가 redaction 책임을 진다는 경계) 명시. detection≠prevention, "그대로 반환 + callback 없음 = 누출 0" 은 과도한 단정.

---

### **B-BLOCK-3 — §8.1 T-A 동치 검증의 "spec 강제" 부재 + 현존 test_t6 trap 그대로 잔존 위험**

- **근거**: 현 코드 `tests/adapters/llm/test_redaction_filter.py:92~109` `test_t6_facade_redaction_before_router_deferred` 는 정확히 **brief 가 함정이라 경고한 "redaction 호출됨" 확인** 패턴이다 — line 109 `assert "redact_messages" in calls`. brief §3(line 117) + §8.1 T-A(line 214)는 "단순 '호출됨' 확인이 아니라 **Router 입력 = redacted output 동치 검증**"을 의무화한다.
- **문제**: brief 가 T-A 를 *서술*은 했으나, (a) **현존 test_t6 가 Router 위임 발효 후 어떻게 되는지 미명시** — Router 가 더 이상 `NotImplementedError` 를 던지지 않으므로 `pytest.raises(NotImplementedError)`(line 106) 가 *실패*한다. test_t6 는 *반드시 갱신/대체*되어야 하나 brief §0.2/§8.1 어디에도 "test_t6 갱신/migration" 이 명시되지 않음. T-I(line 222) "기존 RedactionFilter 15 test 무회귀"는 test_t6 의 `NotImplementedError` 전제와 정면 충돌(Router 발효 = test_t6 RED). → **"무회귀" 주장과 test_t6 폐기 필요성이 모순.**
- **추가**: T-A 의 동치 검증이 "secret 이 Router 인자에 *도달 0*"을 어떤 assertion 형태로 강제하는지 brief 가 구체화하지 않음 — fake Router 가 받은 `messages` 인자를 캡처하여 `REDACTION_MARK` 포함 + 원본 secret 부재를 *둘 다* assert 해야 trap 회피. 한쪽만(예: REDACTION_MARK 존재)이면 trap 재발.
- **해소 요구**: brief v1.1 §8.1 에 (i) test_t6 가 Router 발효 후 **폐기 또는 동치 검증으로 대체**됨을 명시 + T-I "무회귀" 문구를 "test_t6 는 RT-1 동치 검증으로 *대체*, 나머지 redaction 7 test 무회귀"로 정정, (ii) T-A assertion spec = "captured Router messages 에 원본 secret 문자열 부재 AND REDACTION_MARK 존재" 양방향 명문.

---

### **B-BLOCK-4 — P11 supply-chain "Implementation Pending" 위상 ↔ brief §4.2 hash 도입의 권위 정합성**

- **근거**: `governance-preconditions.md:280` — P11 Implementation status = "**Pending** — 별도 Implementation/Runtime PASS 합의 (실 ... pip --require-hashes 강제 ... 모두 미구현)". `:306` 본 §1.2.7 이 *하지 않는 것* = "pip --require-hashes 강제 / SBOM diff 회귀 검증 step ... 등 runtime code 구현". P11 은 **Hermes PMO 격상 전 precondition 권장 (blocking 아님)** (`:282`).
- **문제**: brief §4.2(line 139) 가 본 cycle 에 `--require-hashes`/hash 매니페스트를 P11 (ii) 답습으로 *도입*한다. 이는 *나쁘지 않으나*, P11 enforcement 가 governance 상 명시적으로 "Implementation Pending / 별도 합의 영역"인 상태에서 본 brief 가 그 일부를 *조기 발효*하는 것이므로 **권위 위상 정정이 필요**하다. brief §4.2 는 "P11 (ii)" 만 인용하고 *P11 이 현재 Pending/별도합의 영역임*을 명시하지 않아 — 독자가 "본 cycle 이 P11 enforcement 를 충족했다"로 오독할 over-claim 소지(P11 은 SBOM/Action SHA pin/Docker digest/auto-recheck 5측면 중 본 cycle 은 (i)(ii) 일부만). 또한 `requirements-dev.txt:8~9` 는 "runtime application 의존성 0건 / pyproject 신설 = 별도 합의(R-RF2)"를 명문 — 본 cycle 이 첫 runtime dep 을 도입하므로 **이 gate lift 자체가 별도 합의 결정 사항**임은 brief §4.2 가 인지하나, 이 결정이 *본 합의 권한 내*인지(아니면 R-RF2 별도 합의 필요인지) 위상이 모호.
- **해소 요구**: brief v1.1 이 (a) "본 cycle 은 P11 (i)(ii) 의 *일부*(litellm 단일 dep 핀 + hash)만 조기 발효 — P11 전체 enforcement(SBOM/Action SHA/Docker digest/auto-recheck)는 governance §1.2.7 답습 Implementation Pending 영구 존속"을 명문(over-claim 차단), (b) `requirements-dev.txt` R-RF2 "runtime 의존성 0건 / pyproject 별도 합의" gate lift 가 *본 합의 산출에 포함*됨을 명시적 결정 항목으로 등록(암묵 lift 금지 — 자동 정책 변경 회피).

---

## 2. 권고 (BLOCKING 아님, v1.1 흡수 권장)

### B-REC-1 — `validate_config` Min2 우회 엣지케이스 명시 부족
brief §5.2(line 164~168) `validate_config` 은 `status=="active"` provider 만 카운트. **엣지케이스 미처리**: (i) `providers` 키 자체가 비거나 yaml 파싱 실패 시 동작(KeyError vs ConfigError), (ii) `status` 필드 누락 provider 의 default 처리(active 간주? 무시?), (iii) `type` 필드 누락 시 `set(types)` 동작. brief §8.1 T-C/T-D 는 "active 1개" / "동일 type 2개"만 검증 — *malformed yaml* / *필드 누락* 케이스 test 부재. 권고: T-C 에 "필수 필드(type/status) 누락 → ConfigError" 케이스 추가.

### B-REC-2 — 실 키 부재 시 `validate_config` ↔ Router 구성 동작 미검증
brief §5.1 기본 active 2종 = `ANTHROPIC_API_KEY`(api_key) + ollama(none). `validate_config` 은 *status/type* 만 검증하고 **api_key env 존재 여부는 검증 안 함**(설계 §6.1 도 동일). 실 키 부재 시 (a) validate_config PASS(시작 fail-fast 통과) 후 (b) 첫 `acompletion` 에서 litellm AuthenticationError — 이 분리가 의도된 동작인지 brief 가 명시 권장(특히 mock 검증만 하므로 실 키 부재 = 정상 CI 경로). over-claim 회피: "Min2 검증 PASS ≠ 실 호출 가능".

### B-REC-3 — D8 health() dry probe 의 `health()` 시그니처 ↔ 설계 §9.2 alias loop 불일치
현 코드 `facade.py:62` `async def health(self) -> dict[str, bool]: return {}`. 설계 §9.2(line 576) 는 active provider loop. brief §2 D8(line 108)은 "active 목록 + 설정검증 반환으로 축소 가능"을 fallback 으로 둠 — 권고: Core MVP 의 health() 반환 *형태*(dict[str,bool] 유지 여부)를 v1.1 에 1줄 고정(반환 타입 변경은 caller 계약 영향, 현 caller 0 이지만 명시 권장).

### B-REC-4 — LLMMetadata 화이트리스트의 `raw` 누출 경로 추가 점검
brief D3 + §6.3(line 193) "raw dict 통과 0 (화이트리스트 외 키 버림)" 은 위반패턴 #2/#4 차단으로 적절. 단 `usage` 필드(line 187 `{input_tokens, output_tokens, cost_estimate?}`)는 *dict* 로 남으므로 — litellm usage 객체에 provider 고유 키(예: `prompt_tokens_details`)가 섞여 들어올 경우 화이트리스트 우회. 권고: usage 도 명시 키만 추출(frozen dataclass 또는 명시 dict comprehension) — raw usage dict 통과 0 보장.

### B-REC-5 — over-claim 명칭 1건 잔존 점검 ("operative")
brief §1(line 64) + line 14 "facade `complete()` core 경로 **operative**". "operative" 는 "실동작"을 함의하나 본 cycle 검증 = mock 한정(실 호출 0). brief 가 line 14 에서 "단 실 호출 검증 = mock 한정"을 *즉시 병기*하여 완화하나, 독립 NOTE: "operative"가 단독 인용될 때 "런타임 실동작 입증"으로 오독 위험 → 권고: "**코드 경로상** operative (mock 검증; 실 end-to-end 미입증)"로 항상 묶어 인용.

### B-REC-6 — `complete()` 동기→async 전환의 단일 test 환경 검증
brief D1(line 70~74) async 전환은 설계 §4.1 충실 + caller 0(실측 확인) 으로 breaking 위험 낮음(독립 확인: `grep .complete( src/` = 0건). 단 현 test_t6(line 106) 는 sync `facade.complete(req)` 호출 — async 전환 시 `await` 필요 + `@pytest.mark.asyncio` 또는 동등. brief §8.1 이 async test harness(pytest-asyncio 등) 도입을 명시 권장(requirements-dev.txt 에 pytest-asyncio 부재 — 추가 dep 결정).

---

## 3. NOTE (정보 — 판정 영향 없음)

- **NOTE-1 (factual imprecision)**: brief §8.1 T-I(line 222) + §13 E-4(line 287) "RedactionFilter **15 test**". 실측: `test_redaction_filter.py` 의 `def test_` = **8개**(t1~t8). 단 T3/T4 가 `@pytest.mark.parametrize`(line 41, 60) → *collected* count 는 8 초과 가능(parametrize 케이스 합산 시 ~15 도달 가능). pytest 미설치 환경(`python3 -m pytest` 불가)으로 정확 collected 수 미확인. → "15 test" 가 *함수 수*인지 *collected 수*인지 brief 명확화 권장(과장 아닐 수 있으나 모호). BLOCKING 아님.
- **NOTE-2 (인용 정확)**: brief §0.3 + §3 의 governance §4.5(a) 인용 정확 — `governance-preconditions.md:451` (a) = "Hermes native redaction Tier-1 42 catalog ... + **P1 facade redaction filter 검증**". RT-1 협력 대상 명시 일치. ✅
- **NOTE-3 (인용 정확)**: brief D6 §5.1(line 99) credential env 보간 "§7.3" = `llm-providers-design.md:470~478` §7.3 Credentials 처리(yaml 평문 금지 + env 보간) 정확 인용. ✅ (※ 본 reviewer 과제 헤더의 "ADR-011 §7.3" 은 ADR-011 §7.3 = "주의사항"이며 credential 무관 — brief 는 ADR-011 §7.3 을 credential 권위로 인용하지 *않았으므로* brief 오류 아님.)
- **NOTE-4 (인용 정확)**: import-linter 계약 `ignore_imports = src.adapters.llm.facade -> *`(`.importlinter`) 는 facade *발신* import 를 면제 → lazy `import litellm`(함수 내부)도 AST 그래프상 facade 발신으로 동일 면제. `include_external_packages = True` → litellm 미설치 환경(실측: litellm import 실패 확인)에서도 검출 정상. brief §4.1(line 128) 주장 일치. ✅ 단 import-linter 도 현재 *미설치*(실측: `import importlinter` 실패) — verify 단계에서 `pip install -r requirements-dev.txt` 선행 의무(brief §8.3 verify 가 import-linter green 요구하나 설치 전제 미명시).

---

## 4. 권위 cross-verify 매트릭스

| # | brief 인용 | 권위 원문 (file:line) | 정합 | 비고 |
|---|----------|---------------------|------|------|
| 1 | RT-1 = facade real 후 redaction 미부착 window 0 | (64 trajectory / 65 SC-1 — `facade.py:5~8` SC-1 명문) | ✅ | redaction = Router 위임 전 위치(`facade.py:53~56`) 확인 |
| 2 | GP-2 §4.5(a) facade redaction filter 검증 = RT-1 협력 | `governance-preconditions.md:451` | ✅ | 정확 |
| 3 | GP-2 = 송신/로그 경로만, DB INSERT = GP-1 책임 | `governance-preconditions.md:424` | ✅ | brief §3 응답 redaction deferred 가 이 경계와 정합(단 B-BLOCK-2 누출 통로 단정 별개) |
| 4 | ADR-008 #3 버전 핀 | `ADR-008:20` "v0.x API 버전 핀 + 회귀 테스트 + 카나리" | ✅ | #3 은 "버전 핀"만 — *hash* 는 #3 아닌 P11 (ii) 소관(brief §4.2 가 #3+P11 분리 인용, 정확) |
| 5 | ADR-008 #4 단일 facade + 분기 금지 | `ADR-008:21` | ✅ | brief §0.2 #4 deferred 무관, §10 facade 한정 import 일치 |
| 6 | ADR-008 #5 Min 2 always-on | `ADR-008:22` | ✅ | brief §5.2 validate_config 일치 |
| 7 | ADR-009 §2.2 litellm import = facade 한정 | `ADR-009:70~75` (의무 1~6) | ✅ | lazy import 도 facade 내부 = 의무 1 충족(위치만 함수 내부) |
| 8 | ADR-009 §2.3 Hermes PMO ↔ provider 분리 | `ADR-009:77~99` | ✅ | brief §10 단일 진입점 일치 |
| 9 | ADR-011 §2.3 Hermes ≠ root of trust | `ADR-011:110~120` 운영 함의 #2 (Hermes redaction = 로그/송신 방어만) | ✅ | brief §3 응답 redaction deferred framing 정합 |
| 10 | (과제 헤더) ADR-011 §7.3 | `ADR-011:233~238` = "주의사항"(credential 무관) | ⚠️ | **과제 헤더 인용 오류** — credential 권위는 design §7.3. brief 본문은 design §7.3 인용(정확), brief 오류 아님 |
| 11 | P11 (ii) hash 검증 | `governance:259` Layer3 + `:268`(4) — 단 `:280/:306` **Implementation Pending** | ⚠️ | brief §4.2 가 P11 Pending 위상 미명시 → **B-BLOCK-4** |
| 12 | 설계 §17 재합의 folding → status flip | `llm-providers-design.md:6/827` 재합의 대기 ↔ `:773` §15 "12 보강 모두" | ⚠️ | §15 ↔ Core MVP 모순 → **B-BLOCK-1** |
| 13 | requirements-dev.txt runtime dep 0 gate | `requirements-dev.txt:8~9` "runtime 0건 / pyproject 별도 합의(R-RF2)" | ⚠️ | gate lift = 명시 결정 필요 → **B-BLOCK-4 (b)** |
| 14 | D2 alias rename caller 영향 | 실측: `src/` 0건, `test_redaction_filter.py:105` 1건, fixture `facade_only.py` 독립 | ✅ | brief D2(line 80) 정확 |

---

## 5. over-claim 명칭 — 독립 판단

> **본 reviewer 가 brief framing 을 보기 전, 직접 read 한 facade.py/redaction.py/brief §0/§11/§14 기준 독립 평가.**

| 위험 표현 | brief 처리 | 독립 판정 |
|----------|----------|---------|
| "full facade real" | §0 헤더(line 10) + §11 영구 금지 명문 | ✅ 충실 — 67 "GP-2 full→prevention" 강등 동형 답습 적절 |
| "facade 완성" | §11(line 265) 금지 | ✅ |
| "Provider Liquidity 완전 발효" | §0 헤더 + §10 "코드 경로 operative ≠ 5-way 완결"(§14 P-3) | ✅ — ADR-009 §5 5 Layer 별개 명시 적절 |
| "런타임 검증 완료" | §0(line 10) "실 LLM 호출 = mock 검증, 런타임 검증 완료 표현 금지" | ✅ 명문 |
| "operative" (잔존) | §1 line 64/14 — "단 실 호출 = mock 한정" 병기 | ⚠️ **B-REC-5** — 단독 인용 시 오독 위험, 항상 mock 한정 병기 의무 |
| **응답 redaction "누출 통로 0"** | §3 line 118 단정 | ❌ **B-BLOCK-2** — litellm 내장 로깅 + 예외 본문 미고려, 미입증 단정 = *새로운 over-claim 유형* (detection scope 과장) |

**독립 결론**: brief 의 명시적 over-claim 차단 framing(§0/§11/§14)은 65 cascade 교훈을 *충실히* 답습하여 "full/완성/완전/런타임 완료" 4종을 명문 금지한다 — 이 점은 합격. **그러나 brief 자신이 §3 "누출 통로 0" 에서 *새로운 미입증 단정*을 도입했다** — 이는 "명칭 over-claim"은 차단했으나 "*보안 scope over-claim*"(detection≠prevention, callback 없음=누출 0 과장)이 *프레이밍 사각지대*로 재발한 사례. [[feedback_pass_scope_overclaim]] 의 "in-repo≠upstream / detection≠prevention" 원칙이 *응답 경로*에도 적용되어야 함. B-BLOCK-2 로 강제 정정.

---

## 6. 요약

- **판정**: APPROVE WITH CONDITIONS
- **BLOCKING 4건**: (B-BLOCK-1) 설계 §15 "12보강 모두" ↔ Core MVP 분할 모순 미해소(SDD 불일치) / (B-BLOCK-2) 응답·예외 redaction "누출 통로 0" 미입증 단정(litellm 내장 로깅+예외 본문 누락, 보안 scope over-claim) / (B-BLOCK-3) T-A 동치 검증 spec 미강제 + 현존 test_t6 "호출됨" trap 잔존·"무회귀" 모순 / (B-BLOCK-4) P11 Implementation Pending 위상 미명시 + requirements-dev R-RF2 gate lift 암묵 처리
- **권고 6건**: validate_config 엣지케이스 / 실키부재 동작 / health 시그니처 / usage 화이트리스트 / "operative" 병기 / async test harness dep
- **NOTE 4건**: "15 test" 수치 모호 / §4.5(a)·design §7.3·import-linter 인용 정확 / import-linter·litellm 미설치(verify 전 설치 의무)

---

**Agent B 검토 끝.**
