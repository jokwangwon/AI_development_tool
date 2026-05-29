# 3+1 합의 — Agent A (구현 분석가) 독립 분석: MVP-2 SC-3 GP-2 full PASS 발효 brief

> **검토 대상**: `docs/phase0/mvp2-sc3-full-gp2-pass-activation-brief.md` (v1, §0~§11)
> **관점**: "실제로 동작하는가? evidence 가 실재하는가?" (filesystem direct inspection 기반)
> **작성**: 2026-05-28 (67번째 entry cycle, 세션 #3 SC-3) — Agent A 독립 (B/C/외부 LLM 미참조)
> **방법**: 모든 evidence 파일 직접 read + venv pytest 실행 + secret_scanner equivalence self-check 실행

---

## 1. 판정

**APPROVE WITH CONDITIONS**

evidence (Exit (a)~(e)) 는 **실재하며 PASS 발효 근거로 충분**하다. detection(60) + R-2 in-repo(65) + R-1 조건부(66) 의 3 source 가 모두 filesystem 상 실재하고, 167 pytest 전원 green, secret_scanner ↔ redaction_patterns single source equivalence 가 실측 확인됨. §2 매트릭스의 R-1 ⚠️ 조건부 표기, §3 격상 정당성, §4 복합 자격 명문이 실제 코드/source brief 와 일관됨.

단 **BLOCKING 1건 (커버리지 수치 over-claim)** 정정 필수 — 발효 자체는 정정 후 진행 가능.

---

## 2. BLOCKING (정정 필수)

### B-A1. 커버리지 "92%" = 실측 불일치 + source brief 와도 불일치 (over-claim)

brief 가 **3곳**에서 R-2 evidence 를 "커버리지 92%" 로 기술:
- line 48: "65 SC-1 ... group-aware 치환, 15 test, **커버리지 92%**"
- line 70: "(b) ... ✅ **redaction 15 test (커버리지 92%)**"
- line 176: "E-2: prevention R-2 (65 SC-1, facade RedactionFilter 15 test + **커버리지 92%** + pytest 167)"

**filesystem 실측 (`pytest --cov=src.adapters.llm.redaction`)**:
```
src/adapters/llm/redaction.py   50   5   90%   Missing: 46, 57, 70-72, 88
```
→ **실측 = 90%** (full-suite 측정에서도 동일 90%). **92% 아님**.

**source brief (65 SC-1) 과도 불일치**: SC-1 brief 본문은 커버리지 수치를 명시하지 않고 line 159 "커버리지 목표 70%+ (CLAUDE.md §1)", line 222 "E-1: ... 커버리지 70%+" 만 기술. **"92%" 는 어느 source 에도 존재하지 않는 수치**.

**근거**: feedback_pass_scope_overclaim — evidence 실증 vs framing 분리 의무. "92%" 는 실측(90%)도 source(70%+)도 아닌 제3의 수치로, 정직 명문(§4)을 표방하는 PASS brief 에서 수치 over-claim 에 해당.

**정정**: 3곳 모두 "커버리지 90% (실측, 70%+ 목표 충족)" 으로 교체. (수치를 굳이 명시할 필요가 없다면 "커버리지 목표 70%+ 충족" 으로 통일 가능.)

---

## 3. 권고 (BLOCKING 아님)

### R-A1. R-2 "in-repo operative" 의 실 egress 미발생 caveat 명시 강화

`src/adapters/llm/facade.py` `complete()` 실코드 검증 결과:
```python
def complete(self, request: LLMRequest) -> LLMResponse:
    redacted = self._redact_request(request)        # redaction 선행 (operative)
    raise NotImplementedError(                        # Router 위임 deferred
        "LiteLLM Router 위임 = Provider Liquidity sub-cycle deferred ..."
    )
```
→ R-2 redaction layer 는 **실제 호출됨 (operative)** 이나, **실 LLM 송신은 0** (Router 위임 deferred, NotImplementedError). brief §11 P-5 가 "R-2 = facade redaction layer (Router deferred)" 로 일부 명문하나, §2/§4 의 "in-repo operative" 단어가 "실 송신 경로 검증 완료" 로 오인될 여지. **"redaction layer operative (실 Router 송신 = Provider Liquidity sub-cycle deferred)"** 한 줄 caveat 를 §4 발효 범위에 명시 권고. (facade docstring 자체가 이미 "full facade real 아님" 으로 정직 기술 — 답습 가능.)

### R-A2. §3 line 83 "60 §3.2 B-2" cross-reference label 정밀화

§3 line 83 이 "60 §3.2 B-2 'in-repo 능동 redaction 보증 0'" 로 인용하나, 60 brief 의 해당 substantive claim 은 §2 축 3 (line 98 "prevention 능동 redaction, in-repo 입증 0") + §3 (line 105) 위치. **substantive 내용은 정확** (60 이 명백히 "in-repo 입증 0" 선언)하나 "§3.2 B-2" 라는 정확한 anchor 가 60 brief 에 존재하는지 label 정밀 확인 권고 (R-S1 류 cross-reference 정정 cascade 예방). 본질 격상 논리는 영향 없음.

### R-A3. "15 test" 표기 = 함수 8개 / 수집 15개 — 일관성 OK (정보 NOTE)

`test_redaction_filter.py` 는 `def test_` 함수 **8개**이나 parametrize (T-3 4 param + T-4 5 param) 확장으로 **수집 15개**. pytest 실측 "15 passed" 확인. brief 의 "15 test" 표기는 **정확** (수집 기준). 향후 혼동 방지 위해 "15 test case (8 함수 + parametrize)" 정도로 부기하면 명료하나 필수 아님.

---

## 4. NOTE (filesystem direct inspection 발견)

| # | 관찰 | 상태 |
|---|------|------|
| N-1 | `secret-hygiene-egress-redaction.yml` (51KB) + `tools/secret_scanner.py` 실재, D-2 scan-log mode CI step 실재 (line 165~) | ✅ detection 실재 |
| N-2 | `secret_scanner.py` line 51 `from src.adapters.llm.redaction_patterns import ALL_PATTERNS ...` — **detection ↔ prevention single source 공유** (drift 0). `--list-patterns` 실행 → `registered_patterns_count=45`, `tier1_42_catalog_compliant=True`, rc=0 | ✅ equivalence 실측 |
| N-3 | `src/adapters/llm/redaction.py` RedactionFilter — `_redact_match` group-aware 치환 (value_group 0/-1/>0 분기), `redact_messages` shallow copy 원본 불변, `scrub` KEY_BLACKLIST 재귀 = **실 구현** (placeholder 아님) | ✅ R-2 실재 |
| N-4 | `tests/adapters/llm/test_redaction_filter.py` — 8 함수/15 수집, **15 passed in 0.02s** | ✅ |
| N-5 | **full suite `pytest -q` → 167 passed in 0.14s** (brief "pytest 167" 정확) | ✅ |
| N-6 | R-1 supporting: `day2-r1-redaction-location-verification.md`, `r2-canary.yml`, `redaction-pattern-equivalence.md` 모두 실재 | ✅ |
| N-7 | `r2-canary.yml` trigger paths = `docker/r4-1-poc/**` + `docker/r2-poc/**` (cron `0 18 * * *` + PR). **`hermes-version.yaml` trigger 부재** → brief §2 (d)/§4 "R-6 Tier-1 한정, Hermes dependency lock trigger 미구현" 표기 **정확** | ✅ 조건부 표기 검증 |
| N-8 | SC-2 brief(66) line 75/91/118 = HERMES_REDACT_SECRETS opt-in 활성화 전제 + R-6 Hermes lock 미구현 + 실 canary URL 출처 미확보 deferred = brief §2 R-1 ⚠️ 와 **완전 일관** | ✅ R-1 조건부 정직 |
| N-9 | redaction.py 커버리지 실측 90% (Missing 46,57,70-72,88) — **brief 92% 와 불일치** (B-A1) | ⚠️ BLOCKING |
| N-10 | coverage missing line 70-72 = `redact_messages` 의 multimodal/dict content 분기 (`scrub` 위임) + line 57 SKIP_DIRECT_REGISTER skip + line 88 scrub list 분기. 핵심 송신 redaction 경로(redact_text/redact_messages str)는 cover됨 | NOTE (보안 핵심 경로 cover) |

---

## 5. evidence 실재성 평가 (Exit (a)~(e))

> 핵심 질문: 각 evidence 가 실재하는가, PASS 발효 근거로 충분한가?

| Exit | evidence | 실재성 (filesystem) | 발효 근거 충분성 |
|------|----------|-------------------|----------------|
| **(a)** 동등 이상 보안 결과 | detection R-4 설계동등성 + R-2 facade RedactionFilter (Tier-1 45 공유) + R-1 Hermes ⊇ Tier-1 조건부 | ✅ 실재 — redaction_patterns 45 catalog single source, `tier1_42_catalog_compliant=True` 실측 | **충분 (R-2 강, R-1 조건부 명문)**. R-1 ⚠️ = HERMES_REDACT_SECRETS 활성화 전제 정직 기술 |
| **(b)** 격리 PoC 실증 | secret-hygiene D-2 + redaction 15 test | ✅ 실재 — D-2 CI step + 15 passed 실측 | **충분 (in-repo PoC)**. R-1 실 격리 canary = deferred 정직 명문 |
| **(c)** ADR/SDD 권위 | ADR-011 §2.3 #2 + governance §4 + ADR-009 §2.2 | ✅ 답습 source 실재 (facade docstring 인용 일치) | **충분** |
| **(d)** 자동 회귀 검증 | secret-hygiene D-2 CI + redaction pytest 167 + R-6 Tier-1 canary | ✅ 실재 — 167 passed 실측, r2-canary.yml 실재 | **충분 (in-repo 회귀)**. R-6 Hermes lock trigger 미구현 = deferred 정직 (N-7) |
| **(e)** 합의 APPROVE | 60/65/66 합의 + 본 SC-3 | ✅ 60(`92e9078`)/65(`7051138`)/66(`6fbee68`) commit 실재 | 본 cycle 진행 중 |

**종합 평가**:
- **evidence 실재성 = 전원 PASS**. detection(60)/R-2(65)/R-1(66) 의 코드·CI·문서 artifact 가 모두 filesystem 상 실재하며, 추측/placeholder 아님 (RedactionFilter 는 실 group-aware 구현, secret_scanner 는 실 single-source import).
- **격상 정당성 (§3) = 코드상 사실**. 60 "in-repo 능동 redaction 보증 0" → 65 RedactionFilter+facade `_redact_request` 실코드로 "in-repo prevention cover 1 확보" 주장이 정확 (facade.py `complete()` 가 Router 위임 *전* redaction 선행 호출 — T-6 spy test 로 강제 검증).
- **명칭 복합 자격 (§4) = 65/66 실제 상태와 일치**. "R-2 in-repo operative + R-1 조건부" 구분이 정확 (단 R-2 = redaction layer operative, 실 egress 송신은 Router deferred — R-A1 caveat 권고).
- **PASS 발효 근거로 충분**. detection + prevention 양 prong 충족 (R-1 조건부 명문), over-claim 차단 명문(§4/§11) 견고.

**유일한 흠**: 커버리지 "92%" 수치 over-claim (B-A1) — 실측 90%, source 70%+ 와 불일치. 발효 전 정정 필수이나 발효 자격 자체는 불변 (수치 정정 = framing 정정, evidence 실증 영향 0).

---

## 6. Agent A 결론

**APPROVE WITH CONDITIONS** — Exit (a)~(e) evidence 전원 실재, 167 pytest green, single-source equivalence 실측 확인, R-1 조건부 표기 source 일관. GP-2 detection-tier → full PASS 격상은 코드상 사실로 정당하다.

**조건 (발효 전)**:
1. **(B-A1, BLOCKING)** "커버리지 92%" → 실측 "90%" (또는 "70%+ 목표 충족") 3곳 정정.
2. (R-A1, 권고) R-2 "in-repo operative" 에 "실 Router 송신 = deferred" caveat 명시.
3. (R-A2, 권고) §3 line 83 "60 §3.2 B-2" cross-reference label 정밀 확인.

B-A1 정정 후 GP-2 full PASS 발효 evidence 충분.

---

**Agent A 독립 분석 끝.**
