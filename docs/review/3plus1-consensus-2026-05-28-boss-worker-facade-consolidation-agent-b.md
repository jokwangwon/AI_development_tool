# 3+1 합의 — boss/worker facade 통합 (트랙 B → facade.complete()) — Agent B (품질/안전성 검증가)

> **cycle**: 70번째 entry — boss/worker LLM 직호출 → `facade.complete()` 통합
> **검토 대상**: `docs/phase0/boss-worker-facade-consolidation-brief.md` (v1)
> **Agent B lens**: 안전한가 / 견고한가 / 문서 정합성 / over-claim 정직성
> **작성**: 2026-05-28 (세션 #4) — Phase 2 독립 분석 (Agent A/C/codex 미참조)
> **방법**: 직접 read only — boss.py / worker.py / facade.py / redaction.py / redaction_patterns.py / orchestrator.py / memory.py / llm-providers.yaml / .importlinter / governance §4 / ADR-009 §2.2~§2.3 / ADR-008 #4

---

## 0. 판정

**APPROVE WITH CONDITIONS** (BLOCKING 4 + 권고 5).

설계 방향(트랙 B 번복 + facade 단일 진입점 통합 + sync 유지 + DI)은 견고하고 권위 정합한다. RT-1 보안 개선 *방향*도 정확하다. 그러나 brief §3 의 **RT-1 보안 개선 framing 이 over-claim 경계에 있다** — 핵심은 ① boss 의 RT-1 효과는 *송신(request body)* 한정인데 boss 의 실 secret 누출 표면(advice_summary → memory JSONL 평문 영속 + ApprovalGate 표시)은 *응답* 경로이고 이는 deferred 라 **boss 경로의 GP-2 prevention 은 부분적**이라는 점, ② facade `endpoint` 가 registry config 로 이전되면서 SSRF posture 가 "코드 하드코딩 불변식" → "config 신뢰" 로 *약화*된다는 점이 brief 에 누락/과소평가됐다. 4 BLOCKING 흡수 후 APPROVE.

---

## 1. BLOCKING (번호 + file:line + 근거)

### B-1. RT-1 보안 효과 over-claim — boss 실 누출 표면은 *응답* 경로(deferred)이지 *송신* 경로가 아님

**file**: brief §3 line 84~86 + line 14 ("GP-2 prevention 이 boss/worker 경로까지 확장") / `src/jarvis/memory.py:53` (`advice_summary` 평문 영속) / `src/jarvis/orchestrator.py:148` (advice → ApprovalGate 표시)

**근거 (실측 추적)**:
- facade RT-1 redaction = `_redact_request` (facade.py:156~162) = **messages + system 만** (CB-5 범위). 즉 boss 가 *Ollama 로 송신* 하는 user_blob(worker output 포함) 은 redaction 대상이 맞다 — 이 부분은 brief 정확.
- 그러나 boss 의 *실제 secret 누출 표면* 은 송신이 아니라 **응답**: `OllamaBoss.advise` 반환 `BossAdvice(summary=content)` (boss.py:246) → orchestrator `advice` (orchestrator.py:138) → ① `ApprovalRequest(advice=advice)` 로 사람 게이트 화면 표시 (orchestrator.py:148), ② `memory.py:53` `"advice_summary": _truncate(advice.summary)` 로 **JSONL 평문 영속**.
- boss summary = LLM *응답 content* = facade CB-6 답습 **응답 redaction deferred** (facade.py:139 `set_verbose=False` 는 litellm 내장 stdout 로깅만 차단 — 반환 content 자체는 unredacted). 즉 worker output 에 secret 이 있고 boss LLM 이 (mirror-block prompt 가 *advisory 어휘 권고* 일 뿐 구조적 강제 아님 — boss.py:156~163) summary 에 그 secret 을 echo 하면 → **memory JSONL 평문 영속 (P1/P2 누출)**.
- 결론: brief line 14/84 "GP-2 prevention 이 boss/worker 경로까지 확장" 은 **송신 경로 한정** 으로 정확하나, brief 가 강조하는 "boss = untrusted worker output 누출 차단" 의 *실 누출 표면*(memory 영속 + 게이트 표시)은 **응답 경로라 본 cycle 로 차단되지 않는다**. brief §3 line 86 이 "worker 는 코드를 파일 작성(응답 redaction deferred 일관)" 까지만 언급하고 **boss summary → memory 평문 영속 경로를 누락**.

**요구**: brief §3 에 (i) RT-1 효과 = boss/worker *송신(request body)* 한정 명문, (ii) boss `advice_summary` → memory JSONL 평문 영속 + 게이트 표시 = **응답 경로, 본 cycle 미차단(deferred)** 을 known limitation 으로 명문, (iii) "boss 가 untrusted worker output 누출 차단" 표현 → "boss 가 worker output 을 *Ollama 로 송신* 시 redaction" 으로 정밀화. (memory redaction 은 별도 cycle — 본 cycle scope 확장 금지, 단 정직한 명문 의무.)

---

### B-2. SSRF posture *약화* — 하드코딩 불변식 → registry config 신뢰로 이전, brief 가 "여전히 localhost 고정" 으로 과소평가

**file**: brief §6 D6 line 78~79 + RT row 없음 / `facade.py:101~102` (`api_base = p["endpoint"]`) / `llm-providers.yaml:32` (`endpoint: http://localhost:11434`) / 현 `boss.py:98` `_OLLAMA_CHAT_URL` 상수 + `test_ollama_boss.py:111~119` (생성자 url/host/endpoint 인자 부재 = 구조적 차단)

**근거 (실측)**:
- 현 boss/worker: endpoint = **코드 상수 하드코딩** (`boss.py:98`, `worker.py:231`). 생성자에 url/host/endpoint 인자 **부재** → 외부 host 주입 경로가 *구조적으로* 0 (test_ollama_boss.py:114~119 가 inspect.signature 로 강제). 이것이 현 SSRF posture 의 *불변식*.
- 통합 후: facade 가 `to_router_config` 에서 `api_base = p["endpoint"]` (facade.py:101~102) 로 라우팅 → endpoint 가 **`llm-providers.yaml` config 값**(yaml:32). 즉 SSRF 방어가 "코드 상수(편집 = git diff + 코드 리뷰)" → "yaml config 1 줄 편집" 으로 **신뢰 경계 이전 + 약화**. yaml 에 `endpoint: http://evil.internal:11434` 를 쓰면 boss/worker 가 외부 host 로 송신 — 현재는 구조적으로 불가능한 경로가 *열린다*.
- brief D6 line 79 "여전히 localhost 고정, 외부 host 주입 경로 0" 은 **부정확**: localhost 고정은 *현 yaml 값* 일 뿐 *불변식이 아님*. RT-1 redaction 으로 얻는 보안 이득과 SSRF 불변식 약화는 **trade-off** 인데 brief 가 이득만 명시.

**요구**: brief 에 (i) SSRF posture = "코드 하드코딩 불변식" → "registry config 신뢰" 이전 = **trade-off** 명문, (ii) 완화책 명시 — `validate_config` 또는 별도 검증에 **ollama type provider 의 endpoint 가 localhost/127.0.0.1 인지 검증**(또는 허용 host allowlist) 추가 *또는* 본 cycle 미포함 시 명시적 deferred + Rollback Trigger 등록. (현 facade.py validate_config(facade.py:75~85) 에 endpoint 검증 0건 실측.)

---

### B-3. registry alias 구체 미정 — Min 2 + 동일 type 금지 충족이 "무영향" 가정이나 ollama type 추가는 동일 type 충돌 위험

**file**: brief §2 D5 line 76 + §4 line 92 ("alias 추가는 routing 만, providers active 集合 불변이면 validate_config 무영향") / `facade.py:79~85` (validate_config) / `llm-providers.yaml:28~33` (ollama-llama-local 이미 active)

**근거**:
- 현 active 2종 = `anthropic-claude-api`(type anthropic) + `ollama-llama-local`(type ollama) (yaml:21~33). validate_config (facade.py:81~85) = active **type set 중복 금지** ("동일 type 2개 active 금지", facade.py:85).
- brief D5 line 76 은 "기존 `ollama-llama-local`(active) 재사용 **또는** 워커 전용 모델 추가" 양자 모두 잠정 허용. **재사용** 은 안전(active 集合 불변). 그러나 **워커 전용 ollama 모델을 새로 active 등록** 하면 → ollama type 이 2개 active = **facade.py:85 ConfigError(동일 type 금지) → 시작 fail-fast**. brief 가 "active 集合 불변이면 무영향" 이라는 *조건문* 은 맞으나, D5 가 "추가" 옵션을 잠정 열어둬 위반 경로가 존재.
- boss(qwen)/worker(glm) 가 *다른 모델* 을 쓰는 게 현 테스트 의도(test_ollama_boss model=qwen / test_ollama_worker model=glm)인데, 둘 다 ollama type → **둘을 동시 active provider 로 등록 불가**(동일 type 금지). 즉 routing alias 는 추가하되 **둘 다 같은 단일 ollama provider(=ollama-llama-local) 로 라우팅하거나, model_alias→model_list 매핑을 routing dict 로만** 처리해야 함. brief 가 이 제약을 D5 에서 미해소.

**요구**: brief D5 에 (i) boss/worker ollama alias = **routing dict 항목으로만 추가**(providers active 集合 불변 = ollama type 1개 유지), (ii) 워커 전용 모델이 필요하면 *동일 ollama provider 의 litellm_model 교체* 또는 *standby status* 로 등록(active 아님) — **새 active ollama provider 추가 금지**(facade.py:85 fail-fast), 를 명문. RT-3(routing KeyError) 외에 **RT: ollama type 2개 active → ConfigError fail-fast** Rollback row 추가.

---

### B-4. `_redact_request` 가 `model_alias` 미해결 시 부작용 — boss/worker 의 model_alias 가 routing/providers 어디에도 없으면 default fallback 이 anthropic 으로 라우팅(provider 오송신)

**file**: `facade.py:148~154` (`_resolve` default fallback) + brief §9 RT-3 line 136 ("default fallback") / `llm-providers.yaml:16~18` (routing.default = anthropic-claude-api)

**근거 (실측)**:
- `_resolve` (facade.py:148~154): model_alias 가 routing 에도 providers 에도 없으면 → `self._routing.get("default")` = **`anthropic-claude-api`** (yaml:17) 로 fallback.
- 즉 boss/worker 의 model_alias 가 registry 에 **미등록**(B-3 의 alias 등록 누락 또는 오타) 시 → KeyError 가 아니라 **silent 하게 anthropic 으로 라우팅**. boss 가 untrusted worker output(prompt injection 표적)을 **로컬 ollama 가 아니라 외부 anthropic API 로 송신** = (i) Provider Liquidity 의도 위반(로컬 boss 가 외부 provider 소비), (ii) 비용 발생, (iii) worker output 의 외부 송신(redaction 은 적용되나 송신 자체가 의도 외).
- brief RT-3 line 136 은 "facade `_resolve` default fallback + registry alias 등록" 을 *완화책* 으로 들지만, default fallback 이 **anthropic** 인 현 yaml 에서 이는 *완화가 아니라 위험* — silent 외부 송신. KeyError(명시 실패)가 silent anthropic fallback 보다 안전.

**요구**: brief 에 (i) boss/worker model_alias 는 **registry 등록 의무** + 테스트(T-RT3: 미등록 alias → 명시 실패 또는 background_jobs(=ollama-llama-local, yaml:18) 로 fallback 검증), (ii) RT-3 완화책을 "default fallback" → "**ollama 전용 fallback alias(background_jobs) 명시 지정**" 으로 정정. (default(anthropic) 로 새는 경로 차단.)

---

## 2. 권고 (BLOCKING 아님)

### R-1. redaction false-positive — worker 생성 코드의 secret-유사 패턴 손상, brief §3 명문은 적절하나 테스트 의무화 권고
- brief §3 line 87 + §9 RT-1 + §10 P-4 = false-positive known limitation 명문 **충족**(정직). 단 실측: `redaction_patterns.py:110` T1-032(ENV assignment `KEY=value`), T1-033(JSON `"api_key": "..."`), T1-037(JWT `eyJ...`) 는 worker 가 *정상 생성한 코드/config* 에 흔히 등장 → redaction 으로 코드 손상 가능. 특히 worker output 이 파일 작성 경로(worker.py:310~313)일 때 손상된 코드가 디스크에 기록. brief 의 false-positive test 는 boss 송신 경로만 언급(T-RT1) — **worker 파일 작성 경로의 false-positive 영향(송신 redaction 은 facade 에서, 파일 작성은 redaction 전 원본 code)** 을 구분 명문 권고. (실측: worker.py:308 `code = _strip_code_fences(content)` → 파일 작성은 *응답 content* 기반이라 송신 redaction 무관 = 파일은 원본 보존 = 손상 0. 이 점이 오히려 안전 — brief 가 명문하면 false-positive 우려 해소.)

### R-2. asyncio.run 중첩 루프 — RT-2 완화책 "new_event_loop fallback" 은 표준 안티패턴
- brief RT-2 line 135 "충돌 시 asyncio.new_event_loop fallback". `asyncio.run` 은 실행 중 루프가 있으면 `RuntimeError` raise — boss/worker 가 *동기 top-level* 진입(orchestrator.dispatch 가 sync, orchestrator.py:120)이라 중첩은 실제로 없음(brief 분석 정확). 단 fallback 으로 `new_event_loop` 수동 생성은 리소스 누수/경고 유발 안티패턴. 권고: fallback 불요(top-level sync 보장) 명문 + 만약을 위한 방어는 `asyncio.get_event_loop().is_running()` 체크 후 명시 raise(silent 우회 금지).

### R-3. provider-neutral 명칭(D4) — rename 권고는 적절하나 docstring obsolete 동반 정정 의무
- D4 line 73 rename(`LLMBoss`/`LLMWorker`) 권고 = GP-5 위반패턴 #1(코드 식별자 provider 인코딩) 회피로 정합(ADR-009 §2.2 #3). 단 rename 시 boss.py:1~19 + worker.py:1~11 docstring 의 "트랙 B = stdlib urllib 단독" / "OllamaWorker model 인자 교체 = provider 교체" 서술이 **obsolete** 됨 — rename 과 동시 docstring 정정 의무 명문. (rename 미채택 시에도 docstring 의 "urllib 단독" 서술은 facade 경유 후 거짓 → 정정 필수.)

### R-4. import-linter 계약 검증 claim 정합 — boss/worker 가 facade import 시 `litellm` transitive 검출 회피 확인
- brief §5.3 line 110 + §7 line 121 "boss/worker 가 facade 만 import". 실측 `.importlinter`: forbidden = {openai, anthropic, litellm, ollama}, ignore = `src.adapters.llm.facade -> *` (importlinter:34~35). boss/worker 가 facade 를 import 하면 facade→litellm 은 ignore 되나, **boss/worker→facade→litellm transitive** 가 `include_external_packages=True`(importlinter:22) 에서 검출되는지 확인 의무. (ignore 가 facade 의 outbound 만 면제 — boss→litellm transitive 가 별도 위반으로 잡히면 계약 FAIL.) brief 가 "negative control" 언급하나 transitive 경로 명시 권고 + verify 시 실측 의무.

### R-5. R3(boss raise)/fail-soft(worker is_error) 계약 보존 매핑 정밀 — facade 예외 종류 누락 위험
- D3 line 70: boss = facade 예외 catch → RuntimeError, worker = catch → WorkerResult(is_error). facade 가 raise 하는 예외 = `AuthenticationError`/`DegradedError`/`ConfigError`/`RuntimeError` + litellm 원본 예외(facade.py:204~209 에서 재-raise). brief 가 "catch-all"(RT-4 line 137) 이라 하나 D3 line 70 은 열거형 — **`except Exception` catch-all 명문**(특정 예외 열거 시 누락 위험). 단 catch-all 이 R3 의도(advise 가 *던지고* orchestrator 가 누락→경고, boss.py:13)와 정합한지 확인: 현 orchestrator._advise(orchestrator.py:111~118) 가 이미 `except Exception` 으로 흡수 → boss 가 RuntimeError 던지면 정상 흡수. **계약 보존 확인(권고)**: boss 가 DegradedError 를 RuntimeError 로 래핑 시 강등 신호가 advisory_failed 로만 표면화 — 강등 silent 위험은 advisory 비차단 성격상 수용 가능(명문 권고).

---

## 3. NOTE (참고)

- **N-1**: 트랙 B 번복 안전성 — BossLLM Protocol(boss.py:58~69) + StubBoss(boss.py:72~94) **보존** 명문(brief §6 line 116 + §0.2 #2) = 보안 invariant(R2 텍스트 전용 BossAdvice / boss 출력 실행 권한 0) 훼손 0. 실측: BossAdvice frozen(boss.py:43~55) = 제어 흐름 필드 부재 = facade 경유 후에도 불변(summary 텍스트만 반환, boss.py:246). **invariant 보존 확인**.
- **N-2**: SDD 정합 — 트랙 B 번복이 prior 합의(`jarvis-mvp1-local-boss-design-brief` §3 "OpenAI-호환 endpoint 통일(트랙 B)", boss.py:6 답습) reverse. brief §6 line 116 의 "facade real *후* = 트랙 B 전제(facade 부재) 해소" 논리 정합 — 헌법 1조(SDD) 위반 아님(prior 합의의 *전제 조건 변화* 에 의한 정당 번복, 자체 합의 가동). **정합**.
- **N-3**: worker fail-soft 본질 보존 — OllamaWorker 의 "fs 행동 능력 경로 부재 = prompt injection 안전 본질"(worker.py:253~254) 은 facade 경유와 무관(LLM 응답 텍스트만 수신 → 파일 작성은 worker 내부 realpath traversal 차단, worker.py:327~345 보존). **invariant 보존**.
- **N-4**: ApprovalGate output_preview(orchestrator.py:147 `result.output[:200]`) = worker output 200자 = 사람 게이트 표시 경로. 이 또한 unredacted(응답 경로) — B-1 의 worker 버전. 단 사람 게이트는 *사용자 본인* 표시(외부 송신 아님)라 P2 위험도 낮음(개인 툴 비례성, MEMORY proportionate_security). **NOTE 한정**.

---

## 4. over-claim 독립 판단

| # | brief 표현 | Agent B 판정 | 근거 |
|---|----------|-----------|------|
| OC-1 | §0.2 #7 "'Provider Liquidity 완전 발효' 0" + §8 금지 | ✅ **정직** | boss/worker 2 경로 한정 명문 + CliWorker/TmuxWorker 제외(§0.2 #1) |
| OC-2 | §0.2 #5 "실 Ollama end-to-end 0(mock)" + P-2 | ✅ **정직** | facade fake 주입 명문, 실 호출 deferred |
| OC-3 | line 14/84 "GP-2 prevention 이 boss/worker 경로까지 확장" | ⚠️ **부분 over-claim (B-1)** | 송신 경로 한정 — boss summary→memory 평문 영속(응답 경로) 미차단. "확장" 이 *경로 전체* 처럼 읽힘 |
| OC-4 | D6 line 79 "여전히 localhost 고정, 외부 host 주입 경로 0" | ⚠️ **over-claim (B-2)** | localhost 는 yaml 값일 뿐 불변식 아님 — SSRF posture *약화* 를 "유지" 로 framing |
| OC-5 | §4 line 92 "validate_config 무영향" | ⚠️ **조건부 over-claim (B-3)** | "active 集合 불변이면" 조건 충족 시만 — D5 가 active 추가 옵션 열어둠 |
| OC-6 | RT-3 line 136 "default fallback" = 완화책 | ❌ **위험을 완화로 framing (B-4)** | default fallback = anthropic silent 외부 송신 |

**누적 over-claim cascade 경고 답습**: 본 cycle 도 PASS/효과 framing 에서 over-claim 4건(OC-3~OC-6) 포착 — [[feedback_pass_scope_overclaim]] "detection≠prevention / in-repo≠upstream / 명칭 자격 부착" 패턴 답습. **detection(현 urllib 송신 redaction 부재) → prevention(facade 송신 redaction) 은 *송신 경로 한정* 이고, *응답/영속 경로* 는 여전히 미차단** — "boss/worker 경로 확장" 은 송신 한정 명문 의무(B-1).

---

## 5. 권위 cross-verify 매트릭스

| brief 인용 | 실 권위 | 정합 | 비고 |
|----------|--------|-----|------|
| §0.3 "facade `_redact_request` messages+system, CB-5 범위" | facade.py:156~162 (messages + system 만) | ✅ | 정확 — tools 도 _build_opts:167 redact 되나 boss/worker tools 미사용 |
| line 85 "응답 redaction = 69 CB-6 deferred" | facade.py:139 `set_verbose=False`(stdout 로깅만) + 반환 content unredacted | ✅ (단 B-1) | content 자체 unredacted = boss summary 영속 위험(B-1) |
| §2 D6 "endpoint registry 책임 이전" | facade.py:101~102 `api_base=p["endpoint"]` + yaml:32 | ✅ (단 B-2) | 이전은 정확 — 단 posture *약화* 미명문 |
| §4 "Min 2 active + 동일 type 금지" | facade.py:79~85 validate_config | ✅ (단 B-3) | ollama type 2개 active 금지 = D5 alias 추가 제약(B-3) |
| §7 "litellm import = facade 한정" | .importlinter:24~35 (forbidden litellm, ignore facade->*) | ✅ (단 R-4) | transitive 검출 확인 의무(R-4) |
| §3 "GP-2 송신 redaction" = governance §4.1 | governance §4.1 line 422 "LLM API request body redaction" | ✅ | 단 §4.4 line 424 "GP-2 = 송신/로그 경로만, GP-2 단독 헌법 8조 본질 충족 금지" → B-1 정합(boss 응답 영속은 GP-2 범위 밖 누출) |
| §0.2 "ADR-009 §2.2 단일 진입점 의무" | ADR-009 §2.2 line 75 #6 "provider 추가 = facade 변경만" + §2.3 line 89 "Hermes ≠ provider 소유" | ✅ | boss/worker facade 경유 = 단일 진입점 의무 실효 정합 |
| §6 "BossLLM Protocol = provider 추상 보존" | boss.py:58~69 Protocol + ADR-009 §2.3 (provider 분리) | ✅ | N-1 보존 확인 |
| §3 "Tier-1 catalog secret 패턴 한정" | redaction_patterns.py:133~136 (45 patterns) + REDACTION_MARK:170 | ✅ | false-positive = secret-유사 패턴 한정(R-1) |

**cross-verify 결과**: 9/9 인용이 실 권위와 정합(인용 위조 0건). 단 4건(B-1/B-2/B-3 + R-4)이 권위는 정확하나 **brief 의 *해석/framing* 이 보안 함의를 과소평가** — 권위 인용 정직, framing 보수성 미흡.

---

## 6. 요구 사항 종합 (흡수 시 APPROVE)

1. **B-1**: RT-1 효과 = 송신 한정 명문 + boss `advice_summary`→memory JSONL 평문 영속(응답 경로, deferred) known limitation 명문 + "untrusted worker output 누출 차단" → "송신 시 redaction" 정밀화.
2. **B-2**: SSRF posture = 하드코딩 불변식 → registry config 신뢰 이전 = trade-off 명문 + endpoint localhost 검증(validate_config 확장) 또는 명시 deferred + Rollback row.
3. **B-3**: boss/worker ollama alias = routing dict 항목으로만(active ollama 1개 유지) + 새 active ollama provider 추가 금지 명문 + RT(동일 type 2개 active fail-fast) row.
4. **B-4**: model_alias registry 등록 의무 + 미등록 fallback = background_jobs(ollama) 명시(default=anthropic silent 외부 송신 차단) + T-RT3 테스트.
5. 권고 R-1~R-5 검토 반영.

---

**Agent B 검토 끝. Phase 2 독립 분석 — Reviewer 교차 비교 대기.**
