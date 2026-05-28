# 3+1 합의 (Reviewer 통합) — SC-Provider Liquidity (facade Router 위임 real, core `complete()` 경로)

> **날짜**: 2026-05-28 (세션 #4, 69번째 entry 진입 cycle)
> **검토 대상**: `docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md` (v1, §0~§14)
> **합의 형태**: 풀 3+1 + 외부 LLM 1+ (cross-vendor codex gpt-5.5) — TR(아키텍처 + SDD + 보안 + 실코드 + 첫 runtime dep + 5조-2 직결, 5/5 발화)
> **4 source**: Agent A (구현) / Agent B (안전) / Agent C (대안) / codex (OpenAI gpt-5.5, cross-vendor blind)

---

## 0. 최종 판정 — **APPROVE WITH CONDITIONS (4 source 전원)**

| source | 판정 | BLOCKING | 권고 |
|--------|------|----------|------|
| codex (gpt-5.5 cross-vendor) | APPROVE WITH CONDITIONS | 3 | 3 |
| Agent A (구현 분석가) | APPROVE WITH CONDITIONS | 3 | 5 |
| Agent B (품질/안전성) | APPROVE WITH CONDITIONS | 4 | 6 |
| Agent C (대안 탐색가) | APPROVE WITH CONDITIONS | 3 | 7 |

**Reviewer 통합 = APPROVE WITH CONDITIONS, BLOCKING 8 (통합) + 권고 12.** brief v1 방향(LiteLLM Router 위임 real + Core MVP scope + Router mock 검증 + §17 folding + over-claim 차단 framing)은 **4 source 전원 견고 판정**. BLOCKING은 모두 *구현 세부 명세 정밀화 + over-claim 1건 + scope 정직 표기* — **설계 본질 변경 0**. BLOCKING 흡수 후 brief v1.1 → TDD 구현 적격.

⚠️ **codex 절차 재실행 NOTE**: 1차 codex run은 sandbox `workspace-write`의 bubblewrap loopback 초기화 실패(`bwrap: loopback: Failed RTM_NEWADDR`)로 파일 read 불가 → 절차적 REVISE(증거 없는 판정 거부, 정직). 2차 run `--sandbox danger-full-access`로 재실행 → 정상 read + line 인용 기반 APPROVE WITH CONDITIONS. **본 합의 = 2차 run 채택** (1차 = 환경 문제, 검토 내용 0).

---

## 1. Phase 3 — 교차 비교 (일치 / 부분일치 / 불일치 / 누락)

### ① 일치 (Consensus — 다 source 수렴)

- **명칭 over-claim 차단 framing 양호** (4 source 공통): brief §0/§11/§14의 "full facade real / facade 완성 / Provider Liquidity 완전 발효 / 런타임 검증 완료" 4종 금지 + mock-only 명문 = 65/67 cascade 교훈 충실 답습. codex 명칭 판단 = "적절, 더 보수적으로 'facade complete() Router delegation Core MVP (mock-verified)'".
- **async 전환(D1) 타당** (A + C + codex): `grep .complete( src/` = 0 (A/C 독립 실측) → breaking 위험 0. 자비스 fan-out 동시성 적합(C).
- **LiteLLM 유지 정합** (C-7): ADR-009 §3 v2.0 트리거 T1~T4 전원 미충족 → 자체 Adapter 무관, MVP 운영 영역.
- **권위 인용 정확** (codex cross-verify 매트릭스 + B 매트릭스): 12행 중 대부분 일치 (예외 = metadata/metadata_in + model 값 모순 + status flip 주의 = BLOCKING 처리).

### ② 부분 일치 (Partial)

- **응답/예외 redaction "누출 통로 0"**: **Agent B = over-claim BLOCKING** (litellm 내장 로깅 set_verbose + re-raise 예외 본문 미고려) ↔ **Agent C = 논리 타당 NOTE** (유일 sink = deferred callback, caller 로깅 = facade scope 밖). **Reviewer 판정 → B 채택 (부분)**: C는 *프로젝트 callback* 경로만 봤고 B는 *litellm 자체 로깅 + 예외 본문*이라는 추가 sink를 식별 — B의 기술 근거가 더 구체적·타당. "누출 통로 0" = 미입증 단정 → **CB-6으로 강제 정직 축소** (아래 §2).

### ③ 불일치 (Divergence) — 없음

- 4 source가 *근본 방향*(APPROVE)에 전원 동의. 불일치는 ②의 누출 통로 1건(부분일치로 해소).

### ④ 누락 (Gap — 특정 source만 식별, 검증 결과 중요)

- **CB-7 degraded 런타임 강등 감지** — **Agent C 단독** (B-3). 그러나 원본 P1 합의 C-4(`3plus1-consensus-2026-05-04-p1-llm-providers.md:150` 만장일치 CRITICAL "시작 시 1회 검증만으론 차단조건 #5 미충족") + 설계 원칙 line 76 "모든 강등 경로에서 재검증" 직접 인용 → **누락이 아니라 design-authority 근거 강함**. Reviewer verify CONFIRMED. scope(user-set Core MVP defer degraded)와 충돌 → 사용자 결정 필요 (§3).
- **CB-1 model=alias 모순** — Agent A + codex 독립 2 source 수렴 → HIGH.
- **CB-8 lazy import negative control** — Agent C 단독 (A는 positive half 실측). verify-gate 조건.

---

## 2. Phase 4 — 통합 BLOCKING (brief v1.1 흡수 의무)

| ID | finding | source | 흡수 정정 |
|----|---------|--------|----------|
| **CB-1** ⭐⭐ | `complete()`가 Router에 `model=litellm_model` 전달 (brief §6.2 line 186) → 설계 §5.1 `model_name=alias`와 모순. fallback/cooldown/routing 무력화 + 위반패턴 #1 근접 | **Agent A (B-A1) + codex (BLOCKING 2)** — 2 source 수렴 HIGH | §6.2 flow를 `acompletion(model=provider_key)` (provider_key = routing 해소 alias=model_name)으로 정정. `litellm_model`은 `to_router_config` 내부에만 등장(complete() 경로 노출 0). T-G/T-B가 fake Router 받는 `model` 인자 = alias 단언 |
| **CB-2** ⭐⭐⭐ | 설계 §15 "v1.0 = dry probe + 12 보강 모두" (line 773) + §17 체크리스트(streaming/race/OAuth/degraded 포함) ↔ Core MVP 5종 deferred 인데 "확정 v2" flip = SDD 문서↔구현 즉시 불일치 | **Agent B (B-BLOCK-1) + Agent C (C-6) + codex (BLOCKING 3)** — 3 source 수렴 HIGH | status flip을 **"확정 v2 / Core MVP 구현분리 승인 (staged implementation 허용)"**로 제한 + 설계 §15 v1.0 row를 "Core MVP(complete 경로) + 12 보강 단계화(deferred phase 명세 존속)"로 갱신을 본 합의 산출에 포함 (§7) |
| **CB-3** ⭐⭐⭐⭐ | manifest 형식 미결정 + P11 `--require-hashes`(governance:268 강제) "가능 범위"로 연성화 + R-RF2(runtime dep 0 / pyproject 별도 합의) gate lift 암묵 + P11 Implementation Pending 위상 미명시 | **4 source 전원** (A R-A3 + B B-BLOCK-4 + C B-2/C-1 + codex 권고3) — HIGHEST | (a) manifest = **`requirements.txt`(runtime 신규)** 결정 (pyproject 기각 — 기존 핀 컨벤션 + hash native + R-RF2 gate 회피) (b) litellm exact pin + **최소 직접핀 sha256 + lock diff 회귀(P11 i/v) 비협상 의무**, transitive hash = 비례성 평가 후 결정(미결정 금지) (c) "본 cycle = P11 (i)(ii) *일부* 조기 발효, 전체 enforcement(SBOM/Action SHA/Docker digest/auto-recheck) = governance §1.2.7 Implementation Pending 영구 존속" 명문 (d) R-RF2 gate lift = **본 합의 명시 결정 항목** 등록(암묵 금지) |
| **CB-4** ⭐⭐ | 현 `test_redaction_filter.py:92~109` test_t6 = brief가 경고한 "호출됨" trap(`assert "redact_messages" in calls`, line 109) + `pytest.raises(NotImplementedError)`(line 106) + `LLMRequest(alias=)`(line 105) → Router 발효 시 3중 깨짐. brief E-4/T-I "15 test 무회귀"와 모순 | **Agent A (B-A2) + Agent B (B-BLOCK-3)** — 2 source 수렴 HIGH | §8.1에 **test_t6 = RT-1 동치 검증으로 *대체/migration*** 명시 + E-4/T-I "15 test 회귀 0" → **"redaction 순수함수 7건(T-1~T-5,T-7,T-8) 회귀 0 + test_t6 = RT-1 동치 검증 대체"** 정정. **T-A assertion spec 양방향**: captured Router messages에 *원본 secret 문자열 부재* AND *REDACTION_MARK 존재* (한쪽만 = trap 재발) |
| **CB-5** ⭐⭐ | RT-1 redaction 범위가 `messages`만 (brief §3 line 116/T-A line 214). Core MVP가 system/tools passthrough 포함하면 *모든 outbound field*가 Router 전 redaction 대상이어야. + redacted `metadata` 행선지 §6.2 부재 + `metadata` vs 설계 `metadata_in` 필드명 미고정 | **codex (BLOCKING 1) + Agent A (B-A3)** — 2 source 수렴 HIGH | §3/§6.2에 **redaction 범위 = messages + system(+ tools 문자열) — 모든 outbound text field** OR Core MVP에서 해당 passthrough 제외 명시. redacted metadata 행선지: request_id만 LLMMetadata 추출, 나머지 acompletion(metadata=) 미전달(callback deferred). **필드명 = 설계 `metadata_in`으로 통일**(codex 권고1) |
| **CB-6** ⭐⭐ (over-claim) | brief §3 line 118 "응답 redaction 미부착 = 누출 통로 0" = 미입증 단정 (litellm 내장 로깅 set_verbose + re-raise 예외 본문에 endpoint/key fragment 미고려). detection≠prevention가 *응답 경로*에 누락 | **Agent B (B-BLOCK-2)**; C(N-5) 부분 이견 → Reviewer B 채택 | "누출 통로 0" → **"송신 경로(request body) 누출 0; (a) litellm 내장 로깅 비활성(`litellm.set_verbose=False` 등) 의무 + test, (b) 응답/예외 경로 redaction = deferred(metrics callback 동반, 별도 sub-cycle)"**로 정직 축소. **본 세션 #4 첫 over-claim catch** ([[feedback_pass_scope_overclaim]] — detection≠prevention 응답 경로 적용) |
| **CB-7** ⭐⭐ (scope) | degraded 전체 defer = 런타임 강등 무방비. Router 위임 real = 강등이 *비로소 발생 가능*한 시점. P1 합의 C-4(만장일치 CRITICAL) + 설계 line 76/737 "모든 강등 경로 재검증" = 시작-시점만으론 차단조건 #5 미충족 | **Agent C (B-3)** — design-authority 강함, Reviewer CONFIRMED | **(필수)** brief가 차단조건 #5를 "충족"이 아니라 **"시작 fail-fast 부분 충족, 런타임 재검증 deferred = 알려진 공백"**으로 정직 표기. **(사용자 결정)** 최소 런타임 강등 감지+fail-loud (~10 LOC: complete() AuthenticationError/ServiceUnavailableError 경로 active 재계산 <2 → raise+stderr) Core 포함 여부 = §3 사용자 결정 (비례성 ↔ #5 본질) |
| **CB-8** ⭐ (verify) | lazy import 계약 PASS 주장(brief §4.1 line 128)의 negative control 부재 — facade *외부* lazy `import litellm` → 계약 FAIL 실측 없으면 GP-5 Layer 1 약화 가능 | **Agent C (B-1)**; A는 positive half 실측(grimp 귀속) | §8.3 verify E-3에 **(a) lazy import + litellm 미설치 환경 계약 PASS 실측 + (b) facade 외부 의도적 lazy import → 계약 FAIL (negative control)** 양방향 evidence 첨부 의무 |

---

## 3. 사용자 결정 필요 항목 (CB-7 scope)

CB-7은 사용자 명시 scope(Core MVP, degraded defer)와 충돌하므로 사용자 결정 필요:
- **공통(필수, 사용자 선택 무관)**: 차단조건 #5 "시작 fail-fast 부분 충족 / 런타임 재검증 deferred" 정직 표기 (over-claim 차단).
- **선택지 (a)** 최소 런타임 강등 감지+fail-loud ~10 LOC Core 포함 — #5 "always-on" 본질을 시작-한정→런타임-감지로 복원 (degraded *모드*/UI/timer는 여전히 defer). 비례성 부합(C 권고).
- **선택지 (b)** degraded 전체 defer 유지 — brief §11/§12에 "런타임 강등 무방비 = 알려진 공백" 명문 + #5 부분 충족 정직 표기만.

---

## 4. 통합 권고 (비차단 — brief v1.1 흡수 권장)

| # | 권고 | source |
|---|------|--------|
| R-1 | async 전환 채택 + 자비스 fan-out 동시성 근거 1줄 (D1) | A/C/codex |
| R-2 | D8 health() = 축소 fallback("active alias + config validation result") 채택, 반환타입 `dict[str,bool]` 고정 | A/B/C/codex 동의 |
| R-3 | `_normalize` 입력 = **속성 접근**(`raw.choices[0].message.content`)으로 단일화 (brief line 85 dict ↔ line 193 속성 표기 불일치) + mock fake Router도 속성 인터페이스(dict mock 금지) | C-5 + A |
| R-4 | `usage`도 명시 키만 추출(raw usage dict 통과 0 — `prompt_tokens_details` 등 provider 고유 키 차단) | B-REC-4 |
| R-5 | `validate_config` 엣지케이스 test — 필수 필드(type/status) 누락 / malformed yaml → ConfigError | B-REC-1 |
| R-6 | 실 키 부재 시 동작 명시 — validate_config PASS(시작) ≠ 실 호출 가능(첫 acompletion AuthenticationError). "Min2 PASS ≠ 실 호출" | B-REC-2 |
| R-7 | "operative" 단독 인용 금지 — 항상 "코드 경로상 operative (mock 검증; 실 end-to-end 미입증)" 병기 | B-REC-5 |
| R-8 | async test harness = `pytest-asyncio` dev-dep 추가 (complete() async → await test) | B-REC-6 |
| R-9 | ollama smoke 1건 = E-7 *권장* evidence 격상(ollama 가용 시 — credential 불요, mock 자기충족 완화). 미가용 시 "litellm.Router 인터페이스 정합 = 실 호출까지 미입증" 알려진 공백 명문 | C-4 |
| R-10 | "15 test" 수치 명확화 — `def test_` 8개 + parametrize → collected ~15. pytest baseline = **167 passed**(A 실측). B-A2 갱신 후 신규 회귀 기준 재계산 | B NOTE-1 + A N-A3/E-A5 |
| R-11 | registry yaml 위치 = **repo 루트**(`config/` 신설 = ceremony, 단일 yaml 불요) | C N-2 |
| R-12 | `api_key_env` → 실 키 보간 메커니즘 명시 — LiteLLM은 `api_key`(실값) 기대, `api_key_env` 키 자동 해석 안 함 → `to_router_config` 내부 `os.environ.get(...)` 보간 | A R-A1 |

---

## 5. NOTE (positive — 판정 영향 없음)

- **N-1**: Agent A 직접 실행 evidence — pytest **167 passed**(baseline), `grep .complete( src/` 0, grimp lazy import facade 귀속(`/tmp/lazytest`), redaction **0.193ms/call**, litellm 미설치(시스템+venv). 구현 실현가능성 높음.
- **N-2**: import-linter·litellm 미설치 → verify 전 `pip install -r requirements-dev.txt` 선행 의무 (B NOTE-4). import-linter `ignore_imports = facade -> *` + `include_external_packages=True` 정확(B/C/codex 확인).
- **N-3**: D2 alias rename 영향 실측 정확 — src 0 / test 1건(`:105`) / fixture 독립(영향 0) (A/B/C/codex 4 source 확인).
- **N-4**: 응답 redaction defer 자체는 callback sink defer 맥락에서 비례적(C N-5) — 단 "누출 통로 0" 단정만 CB-6으로 정정(litellm 내장 로깅/예외 본문).
- **N-5**: SKIP_DIRECT_REGISTER no-op (COMPILED_PATTERNS에 해당 id 부재 — 45 전부 적용) = SC-1 산출, 본 cycle 손대지 말 것(패턴 내용 0 의무, A N-A1).

---

## 6. 명칭 독립 판단 (4 source 종합)

- 4 source 공통: "SC-Provider Liquidity — facade Router 위임 real (core `complete()` 경로)" = **적절** (over-claim 0).
- codex 더 보수 제안: "facade `complete()` Router delegation Core MVP (mock-verified)".
- **Reviewer 채택 명칭**: **"SC-Provider Liquidity — facade `complete()` Router 위임 real (Core MVP, mock-verified)"** — "Core MVP" + "mock-verified"를 명칭에 내장하여 deferred 5종 + 실 호출 미입증을 명칭 단독 인용 시에도 노출.

---

## 7. 합의 결론

**APPROVE WITH CONDITIONS (4 source 전원)** — brief v1 방향 견고, BLOCKING 8(통합) 흡수 후 brief v1.1 → TDD 구현 적격. **CB-7 = 사용자 scope 결정 선행** (§3). over-claim catch 1건(CB-6 응답 누출 통로 0) = 본 세션 #4 첫 포착 (누적 세션 #2 4 + #3 2 + #4 1 = 7회, 4 source process 가치 누적). 설계 §17 folding = staged 명문 조건부 승격(CB-2).

**다음 단계**: brief v1.1 흡수(BLOCKING 8 + 권고 12, 1pass) → CB-7 사용자 결정 → TDD 구현 승인 → 구현 → verify(negative control 포함) → commit + push.
