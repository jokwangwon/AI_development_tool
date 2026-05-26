# G2 GP-5 3차 — URL Endpoint + Model Name Scanner — Group A 3차 PoC 사양

> **상태**: DRAFT (2026-05-10, Group A 3차 진입 — URL endpoint hardcoding (E-1) + model name hardcoding (E-2) 통합 PoC, Layer 1c 모법 답습)
> **답습 출처**:
> - `docs/architecture/implementation-runtime-roadmap.md` §2.1 Order 1 (G2 GP-5 Provider Adapter Enforcement) / §3.1 매트릭스 / §5.4 (단축 합의 + PoC evidence)
> - `docs/architecture/llm-providers-design.md` §9.3 (depcruise rule 3 — `no-direct-llm-sdk` / `no-llm-via-httpx` / `no-model-name-in-code`)
> - `docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md` §C-N §5 (Layer 1 모법 ADR — Provider Liquidity 5-way Multi-layer Defense)
> - `docs/decisions/ADR-008-hermes-adoption-decision.md` 차단조건 #4 (provider 직접 호출 차단)
> - `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.1 (a)~(e)
> - **Group A 1차/2차 산출물**: `tools/provider_import_scanner.py` (1차 — AST 5종 패턴) + `.importlinter` (2차 — T-2 import-linter)
> - **Group A 2차 합의 §5.5 #C-8**: "URL 하드코딩 차단 = 본 PoC 외 3차 grep 분리 합의 필수 — 본 2차 PoC 도입으로 그 책무 *해소되지 않음* 명시" — 본 3차 = C-8 직접 답습 영역
> **PASS 조건 답습**: ADR-011 §2.1 (a)~(e) 5/5 + 사용자 명시 6 풀 3+1 승격 trigger / 6 검증 / 8 금지 / 외부 의존 0건
> **상위 권위**: ADR-008 부록 C §C.5 (Design/Governance ↔ Implementation/Runtime 분리), P2 v3 §3.1.4 (Implementation Pending), Provider Liquidity 5-way Multi-layer Defense (ADR-009 C-N §5)
> **답습 시제**: Group A 1차 (`g2-gp5-provider-adapter-enforcement-poc.md`) + Group A 2차 (`g2-gp5-poc2-import-linter-implementation.md`) + Group D + Group E + Group G PoC 사양 형식 직접 답습

---

## 0. 목적

본 PoC 는 G2 GP-5 *Provider Adapter Enforcement* 의 **Layer 1c — URL endpoint + model name 직접 사용 차단** 시제 — Group A 1차 (Layer 1a AST 5종 패턴) + 2차 (Layer 1b transitive import) 답습 후 *3차 분리 영역* (Group A 2차 합의 §5.5 #C-8 답습 의무).

**Layer 분리 책무 매핑** (Group A 1차/2차 + 본 3차 = G2 GP-5 Layer 1 모법 ADR-009 C-N §5 답습 완결):

| Layer | Group A # | 검증 영역 | 도구 | 답습 |
|---|---|---|---|---|
| **Layer 1a** | 1차 (commits `a3693a0` + `0f503a4`) | AST 5종 패턴 (direct-import / from-import / dynamic-importlib / `__import__` / model-name-branch) | `tools/provider_import_scanner.py` (~165줄) | ADR-009 C-N §5 + ADR-008 차단조건 #4 |
| **Layer 1b** | 2차 (commits `cfa0db0` + `d7c4b05` + `9764fd8`) | Transitive import (A→B→openai) | `.importlinter` (T-2 import-linter 2.11) | llm-providers-design.md §9.3 `no-direct-llm-sdk` |
| **Layer 1c** | **3차 (본 PoC)** | **URL endpoint 직접 사용 + model name 하드코딩** | **`tools/provider_url_scanner.py`** | **llm-providers-design.md §9.3 `no-llm-via-httpx` + `no-model-name-in-code`** |

**범위 한정 핵심 결정** (사용자 명시 "최소 PoC" 답습):

- **E-1 (URL endpoint hardcoding)** = Tier-1 provider API endpoint URL 10개 정적 grep — `src/` 코드에서 `api.anthropic.com` / `api.openai.com` 등 직접 사용 시 차단 (yaml/json/md 등 config/docs 는 allowlist).
- **E-2 (model name hardcoding)** = Tier-1 provider 모델 ID 19+ 정적 grep — `src/` 코드에서 `claude-opus-*` / `gpt-4*` / `gemini-pro*` 등 직접 사용 시 차단 (yaml만 허용 답습).

본 PoC 는 **Layer 1c 정적 검출 한정** — 의미적 분석 / runtime hook / depcruise 통합 / pre-commit 활성화 = 본 PoC 방어 범위 외 (사용자 명시 답습).

신규 정책 발명 0건 — `llm-providers-design.md` §9.3 + ADR-009 C-N §5 + Group A 2차 합의 #C-8 명세 그대로 답습.

---

## 1. PoC 범위 (사용자 확인 — 2026-05-10)

### 1.1 포함 산출물 8건

| 산출물 | 경로 | 책무 |
|--------|------|------|
| 본 사양 문서 | `docs/phase0/g2-gp5-poc3-url-endpoint-model-name-scanner.md` | PoC 사양 + 답습 매핑 + 사용자 명시 6 검증 / 6 trigger / 8 금지 / 9 fixture 매트릭스 |
| Validator | `tools/provider_url_scanner.py` | 단일 도구 + 2 mode (url-endpoint / model-name) + Tier-1 catalog (URL 10 + model 19+) + extension allowlist (`.yaml`/`.yml`/`.json`/`.jsonl`/`.toml`/`.cfg`/`.ini`/`.md`) + comment 부분 회피 (`#` / `//`) + `--list-catalogs` self-check + violation reporter (Group D/E/G 답습) |
| E-1 PASS fixture × 1 | `tests/fixtures/provider_url_scanner/url_endpoint/pass/safe_config.yaml` | yaml 안 endpoint URL = allowlist 통과 (FP 검증) |
| E-1 FAIL fixture × 3 | `tests/fixtures/provider_url_scanner/url_endpoint/fail/{hardcoded_url_anthropic, hardcoded_url_openai, hardcoded_url_google}.py` | 3 패턴 cover (Anthropic + OpenAI + Google AI) |
| E-2 PASS fixture × 1 | `tests/fixtures/provider_url_scanner/model_name/pass/safe_model_config.yaml` | yaml 안 model name = allowlist 통과 (FP 검증, §9.3 "yaml만 허용" 답습) |
| E-2 FAIL fixture × 4 | `tests/fixtures/provider_url_scanner/model_name/fail/{hardcoded_model_anthropic, hardcoded_model_openai, hardcoded_model_gemini, hardcoded_model_llama}.py` | 4 패턴 cover (Anthropic + OpenAI + Google + Meta) |
| CI workflow | `.github/workflows/provider-url-scanner.yml` | PASS/FAIL 양방향 + `--list-catalogs` 자기 검증 + F-금지 grep + summary.json + artifact (`group-a3-logs/` Group F 후속 답습) + Evidence summary |
| Reviewer-only 단축 합의 | `docs/review/3plus1-consensus-2026-05-10-g2-gp5-poc3-reviewer-only.md` | PoC 검토 + 6 trigger 0/6 자기 검증 + evidence 매트릭스 통합 (Group D/E/G 답습) |

**합산 = 8 파일** (Group D/E/G 답습 평균).

### 1.2 제외 (별도 합의 영역 — 사용자 명시 8 금지 답습)

| 항목 | 분리 이유 |
|------|----------|
| G2 GP-5 최종 PASS 선언 | **사용자 명시** — 본 PoC = *Layer 1c 정적 검출 시제* 한정 |
| G2 전체 Implementation/Runtime PASS 선언 | **사용자 명시** |
| Hermes PMO 격상 선언 | **사용자 명시** |
| 실 provider API 호출 | **사용자 명시** — fixture 한정, regex 정적 검출 |
| 실 API key 사용 | **사용자 명시** — fixture 의 endpoint URL = path-only canary |
| Provider 구현 자체 변경 | **사용자 명시** — `src/adapters/llm/facade.py` placeholder 변경 0건 (Group A 2차 답습 — `src/__init__.py` placeholder 만 존재) |
| ADR 본문 자동 갱신 | **사용자 명시** — cross-reference 답습 한정 |
| Tier-2 / Tier-3 catalog 자동 확장 | **사용자 명시** — Tier-1 catalog (URL 10 + model 19+) 한정, 확장은 풀 3+1 별도 합의 |
| depcruise rule 통합 (`.dependency-cruiser.cjs` 추가) | Layer 1b 영역 (Group A 2차 import-linter 답습 분리) — 별도 합의 |
| pre-commit hook 활성화 | T2 정책 영역 (ADR-011 §2.4) — 별도 합의 |
| PR auto-reject GitHub branch protection | T3 정책 영역 — 별도 합의 |
| 의미적 분석 (URL 패턴이 *실제* provider API 호출인지 추론) | Layer 5 추론 영역 — 별도 합의 |
| Comment 라인 *완전* 회피 (multi-line block comment) | 본 PoC 부분 cover (`#` / `//` 한정), 완전 회피는 AST 분석 = 별도 합의 |
| Tier-2 vendor (Slack / GCP / Azure 외 100+ vendor) URL endpoint 검출 | Tier-2 catalog 확장 영역 — 사용자 명시 금지 |
| Provider 모델 ID major version 외 *전체* version 매트릭스 (예: `gpt-4-0125-preview-1234`) | Tier-1 base pattern 한정, 세부 version 변형 = 풀 3+1 별도 합의 |

---

## 2. Group A 1차 / 2차 / 3차 답습 매트릭스

### 2.1 Layer 1 모법 ADR (ADR-009 C-N §5) 답습 완결

| Layer | 검증 패턴 | Group A 답습 | 본 PoC 영역 |
|---|---|---|---|
| Layer 1a #1 | direct-import (`import openai`) | 1차 ✅ | — |
| Layer 1a #2 | from-import (`from openai import ...`) | 1차 ✅ | — |
| Layer 1a #3 | dynamic-importlib (`importlib.import_module("openai")`) | 1차 ✅ | — |
| Layer 1a #4 | `__import__("openai")` | 1차 ✅ | — |
| Layer 1a #5 | model-name-branch (`if model == "gpt-4": ...`) | 1차 ✅ (AST scanner) | — |
| Layer 1b | Transitive import (A → B → openai) | 2차 ✅ (T-2 import-linter `forbidden_modules`) | — |
| **Layer 1c #1** | **URL endpoint hardcoding (`api.anthropic.com` 등)** | ❌ — 2차 합의 #C-8 답습 *3차 분리* | **본 PoC ✅ (E-1)** |
| **Layer 1c #2** | **model name hardcoding (`claude-opus-4-1` literal in src/)** | ❌ — Layer 1a #5 와 중복이지만 별도 — 1차 = AST `if/elif` *분기 패턴*, 본 PoC = *literal string* 패턴 | **본 PoC ✅ (E-2)** |

**Layer 1c 의 본 PoC 책무** = `llm-providers-design.md` §9.3 `no-llm-via-httpx` + `no-model-name-in-code` *grep 보조* 영역 답습.

### 2.2 Group A 1차/2차 답습 형식

| 형식 영역 | Group A 1차 | Group A 2차 | 본 3차 |
|---|---|---|---|
| Validator 구조 (argparse + dataclass + iter) | ✅ AST scanner | ✅ T-2 config | ✅ regex scanner |
| Fixture 디렉토리 (PASS / FAIL 분리) | ✅ | ✅ | ✅ |
| CI workflow (PASS / FAIL 양방향 + 패턴 cover step) | ✅ | ✅ | ✅ |
| Reviewer-only 단축 합의 형식 | ✅ | (풀 3+1 — depcruise rule 복잡도 ↑) | ✅ Reviewer-only (regex grep 단순) |
| ADR-011 §2.1 (a)~(e) 5/5 충족 매트릭스 | ✅ | ✅ | ✅ |

본 3차 = Group A 1차 답습에 가까움 (단순 정적 검출, regex grep, Reviewer-only 단축).

---

## 3. 도구 선택 근거

### 3.1 stdlib 단독 채택 (Group D/E/G 답습)

| 옵션 | 채택 | 사유 |
|---|---|---|
| **(A) Custom validator (stdlib `re` + `dataclasses` 단독)** | **✅ 채택** | Group D/E/G 답습 (외부 의존 0건) + Tier-2/3 확장 위험 0건 + 신규 tool 1 파일 한정 + Reviewer-only 단축 합의 적격 |
| (B) gitleaks / detect-secrets | ❌ 제외 | Group D 답습 — gitleaks/detect-secrets 도구 도입 = Tier-2/3 catalog 확장 위험 |
| (C) AST extension (Group A 1차 scanner 확장) | ❌ 제외 | 본 PoC = literal string grep, AST 불필요 (Group A 1차 = AST 분기 패턴 한정) |
| (D) depcruise rule 통합 | ❌ 제외 | Layer 1b 영역 (Group A 2차) — Layer 1c 분리 답습 |

**채택 = (A) 단독**. gitleaks / detect-secrets / depcruise 통합 = *별도 합의* 영역.

### 3.2 본 PoC 의 stdlib 답습 영역

| stdlib 모듈 | 책무 |
|------|------|
| `re` | URL endpoint Tier-1 catalog grep + model name catalog grep + comment line 부분 회피 |
| `dataclasses` | `Violation` reporter (Group D/E/G 답습) |
| `argparse` | 2 mode CLI + `--list-catalogs` self-check |
| `pathlib` | 재귀 file iterator |

**외부 의존 0건** (`requirements-dev.txt` 변경 0건).

---

## 4. URL Endpoint Catalog (Tier-1, 10개)

### 4.1 catalog 정의

| # | Provider | Endpoint pattern (regex) | 비고 |
|---|---|---|---|
| 1 | Anthropic | `api\.anthropic\.com` | Direct API |
| 2 | OpenAI | `api\.openai\.com` | Direct API |
| 3 | Azure OpenAI | `[\w-]+\.openai\.azure\.com` | Azure tenant prefix |
| 4 | Google AI / Gemini | `generativelanguage\.googleapis\.com` | Google AI Studio API |
| 5 | Replicate | `api\.replicate\.com` | — |
| 6 | Perplexity | `api\.perplexity\.ai` | — |
| 7 | Cohere | `api\.cohere\.(ai\|com)` | 구/신 도메인 |
| 8 | HuggingFace Inference | `(api-inference\|huggingface)\.co/api` | Inference API |
| 9 | Together AI | `api\.together\.xyz` | — |
| 10 | OpenRouter | `openrouter\.ai/api` | 통합 routing API |

### 4.2 본 catalog *제외* 영역 (의도된 분리)

- `localhost:11434` (Ollama 로컬) — provider-neutral, 허용 (사용자 명시 답습)
- `https://anthropic.com` 등 *general 도메인* (API endpoint 아닌 회사 사이트 URL) — 분리
- Tier-2 vendor (100+ Slack / GCP / Azure 외) — 사용자 명시 금지

---

## 5. Model Name Catalog (Tier-1, 19+)

### 5.1 catalog 정의

| Provider | Pattern (regex) |
|---|---|
| **Anthropic (5)** | `claude-opus-[\w.-]+`, `claude-sonnet-[\w.-]+`, `claude-haiku-[\w.-]+`, `claude-3-[\w.-]+`, `claude-2[\w.-]*` |
| **OpenAI (5)** | `gpt-4[\w.-]*`, `gpt-3\.5[\w.-]*`, `gpt-4o[\w.-]*`, `o1-[\w.-]+`, `o3-[\w.-]+` |
| **Google (3)** | `gemini-1\.5-[\w.-]+`, `gemini-2\.[\w.-]+`, `gemini-pro[\w.-]*` |
| **Meta (3)** | `llama-[\w.-]+`, `llama2-[\w.-]+`, `llama3-[\w.-]+` |
| **Mistral (3)** | `mistral-[\w.-]+`, `mixtral-[\w.-]+`, `codestral-[\w.-]+` |

**합산 = 19 patterns** (Anthropic 5 + OpenAI 5 + Google 3 + Meta 3 + Mistral 3 = 19).

### 5.2 본 catalog *제외* 영역

- 모델 ID *세부 version* 변형 (예: `gpt-4-0125-preview-1234567890`) — base pattern 매칭으로 cover (`gpt-4*`)
- Tier-2 모델 (Cohere / HuggingFace / Replicate 모델 ID) — Tier-2 확장 = 별도 합의

---

## 6. Allowlist 정책 (사용자 명시 답습)

### 6.1 Extension Allowlist

| Mode | Allowlist (검출 *제외*) | Scan target (검출 *적용*) |
|---|---|---|
| **`url-endpoint`** | `.yaml`, `.yml`, `.json`, `.jsonl`, `.toml`, `.cfg`, `.ini`, `.md` (8 ext) | `.py`, `.js`, `.ts`, `.tsx`, `.go`, `.rs`, `.rb`, `.java`, `.kt`, `.cpp`, `.c`, `.swift` 등 source code |
| **`model-name`** | `.yaml`, `.yml`, `.json`, `.jsonl`, `.md` (5 ext, §9.3 "yaml만 허용" 답습) | source code 동일 |

### 6.2 Comment 라인 부분 회피

본 PoC 의 comment 회피 = **부분 cover** (사용자 명시 한계 답습):
- Python `#` line — 회피 ✅
- JavaScript / Go / Rust / C++ `//` line — 회피 ✅
- Multi-line block comment (`/* ... */`) — *부분 회피* (line-by-line 한계, 본 PoC = 시작 라인만 검출)
- Python `"""..."""` docstring — 회피 ❌ (full AST 분석 별도 합의)

→ 본 PoC = `#` / `//` 라인 회피 한정. Multi-line / docstring 회피 = 별도 합의 (Group A 1차 AST scanner 답습 영역).

### 6.3 localhost / general 도메인 제외

- `localhost:11434` (Ollama 로컬) — Tier-1 catalog 미포함 (provider-neutral, 사용자 명시 답습)
- `127.0.0.1` / `0.0.0.0` — 미포함
- General 회사 도메인 (예: `https://anthropic.com` 본 사이트) — Tier-1 catalog 의 *API endpoint* 한정 매칭

---

## 7. fixture 9건 사양

### 7.1 E-1 PASS × 1 (allowlist 통과 검증)

`tests/fixtures/provider_url_scanner/url_endpoint/pass/safe_config.yaml`:

```yaml
# Provider configuration — config-driven URL은 allowlist 통과 (yaml ext)
providers:
  anthropic:
    endpoint: https://api.anthropic.com/v1/messages
  openai:
    endpoint: https://api.openai.com/v1/chat/completions
  ollama_local:
    endpoint: http://localhost:11434
```

**예상**: rc=0 + 위반 0건 (yaml ext = allowlist 통과).

### 7.2 E-1 FAIL × 3 (3 패턴 cover)

| 파일 | 패턴 cover | violation |
|------|----------|-----------|
| `hardcoded_url_anthropic.py` | Anthropic | `URL = "https://api.anthropic.com/v1/messages"` (Python literal) |
| `hardcoded_url_openai.py` | OpenAI | `endpoint = "https://api.openai.com/v1/chat/completions"` |
| `hardcoded_url_google.py` | Google AI | `BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models"` |

**예상**: rc=1 + ≥3 violations + 3 패턴 cover.

### 7.3 E-2 PASS × 1 (allowlist 통과 검증)

`tests/fixtures/provider_url_scanner/model_name/pass/safe_model_config.yaml`:

```yaml
# Model configuration — yaml allowlist 통과 (§9.3 "yaml만 허용" 답습)
models:
  primary:
    name: claude-opus-4-1-20250805
    provider: anthropic
  fallback:
    name: gpt-4o
    provider: openai
  embedding:
    name: gemini-1.5-pro
    provider: google
```

**예상**: rc=0 + 위반 0건 (yaml ext = allowlist 통과).

### 7.4 E-2 FAIL × 4 (4 패턴 cover)

| 파일 | 패턴 cover | violation |
|------|----------|-----------|
| `hardcoded_model_anthropic.py` | Anthropic | `MODEL = "claude-opus-4-1-20250805"` |
| `hardcoded_model_openai.py` | OpenAI | `model_name = "gpt-4o"` |
| `hardcoded_model_gemini.py` | Google | `MODEL = "gemini-1.5-pro"` |
| `hardcoded_model_llama.py` | Meta | `MODEL_ID = "llama3-70b-instruct"` |

**예상**: rc=1 + ≥4 violations + 4 패턴 cover.

### 7.5 fake canary 의무

본 PoC fixture 의 모든 URL / model name 은 **fake** literal (실 API key / 실 endpoint 호출 0건). 사용자 명시 8 금지 #4~#5 답습.

---

## 8. 검증 매트릭스 (사용자 명시 6 검증 답습)

| # | 검증 | 입력 | 명령 | 예상 rc | 결과 |
|---|------|------|------|---------|------|
| 1 | E-1 PASS | `url_endpoint/pass/` | `--mode url-endpoint` | 0 | violations=0 |
| 2 | E-1 FAIL | `url_endpoint/fail/` | `--mode url-endpoint` | 1 | ≥3 + 3 패턴 cover (anthropic / openai / google) |
| 3 | E-2 PASS | `model_name/pass/` | `--mode model-name` | 0 | violations=0 |
| 4 | E-2 FAIL | `model_name/fail/` | `--mode model-name` | 1 | ≥4 + 4 패턴 cover (claude / gpt / gemini / llama) |
| 5 | `--list-catalogs` self-check | `--list-catalogs` | 0 | url_endpoint=10 + model_name=19+ + extension_allowlist=8+ |
| 6 | F-금지 grep | scanner + fixture grep | 0 | 실 API key / 실 endpoint 호출 / production data 0건 |

**합산 6 검증** (E-1 PASS+FAIL + E-2 PASS+FAIL + list-catalogs + F-금지 grep).

---

## 9. PASS 기준 자기 검증 매트릭스

| # | PASS 기준 | 본 PoC 충족 |
|---|----------|------------|
| 1 | E-1 PASS scan | rc=0 + 위반 0건 (allowlist 통과) |
| 2 | E-1 FAIL scan | rc=1 + ≥3 + 3 패턴 cover |
| 3 | E-2 PASS scan | rc=0 + 위반 0건 (yaml allowlist 통과) |
| 4 | E-2 FAIL scan | rc=1 + ≥4 + 4 패턴 cover |
| 5 | `--list-catalogs` self-check | url_endpoint=10 + model_name=19+ + extension_allowlist=8+ |
| 6 | F-금지 grep | 0건 (실 API key / 실 endpoint 호출 / production data 부재) |

**합산 6/6 충족 적격**.

---

## 10. 알려진 한계 (의도된 분리)

| # | 한계 | 분리 이유 | 미래 영역 |
|---|------|----------|----------|
| 1 | depcruise rule 통합 (`.dependency-cruiser.cjs`) 미진입 | Layer 1b 영역 (Group A 2차 import-linter 답습 분리) | 별도 합의 |
| 2 | pre-commit hook 활성화 미진입 | T2 정책 영역 (ADR-011 §2.4) | 별도 합의 |
| 3 | PR auto-reject GitHub branch protection | T3 정책 영역 | 별도 합의 |
| 4 | 의미적 분석 (URL 패턴이 실 provider API 호출인지 추론) | Layer 5 추론 영역 | 별도 합의 |
| 5 | Multi-line block comment 완전 회피 | line-by-line regex 한계, AST 분석 영역 | 별도 합의 (Group A 1차 답습 영역) |
| 6 | Python docstring (`"""..."""`) 완전 회피 | full AST 분석 별도 합의 | 별도 합의 |
| 7 | Tier-2 vendor URL endpoint (Slack / GCP / Azure 외 100+) | Tier-2 catalog 확장 = 사용자 명시 금지 | 풀 3+1 + 외부 LLM 1+ |
| 8 | 모델 ID 세부 version 변형 catalog | Tier-1 base pattern 한정 | 별도 합의 |
| 9 | URL fragment / query string 분석 (예: `?api_key=...`) | Group D `secret_scanner.py` 영역 — 별도 책무 분리 | Group D 답습 분리 |
| 10 | 실 src/ 코드에 적용 시 false positive 위험 | fixture 한정으로 회피, 실 적용 = 별도 합의 | 별도 합의 |
| 11 | Markdown 본문 자기 검출 (Group D/E/G 답습 패턴) | CI 는 `tests/fixtures/provider_url_scanner/` 한정 scan 으로 회피 | Group B PoC 사양 §2.8 #1 답습 |

---

## 11. CI workflow 설계

### 11.1 12 step 구조 (Group D/E/G 답습)

| # | Step | 책무 |
|---|------|------|
| 1 | Checkout | actions/checkout@v4 |
| 2 | Set up Python | actions/setup-python@v5 (3.12) |
| 3 | Prepare log directory | `mkdir -p group-a3-logs` (Group F 후속 답습 — leading dot 미사용) |
| 4 | `--list-catalogs` self-check | rc=0 + url_endpoint=10 + model_name=19+ + extension_allowlist=8+ grep |
| 5 | E-1 PASS — url-endpoint pass/ | rc=0 + violations=0 grep |
| 6 | E-1 FAIL — url-endpoint fail/ | rc=1 + ≥3 + 3 패턴 cover (anthropic / openai / google) grep |
| 7 | E-2 PASS — model-name pass/ | rc=0 + violations=0 grep |
| 8 | E-2 FAIL — model-name fail/ | rc=1 + ≥4 + 4 패턴 cover (claude / gpt / gemini / llama) grep |
| 9 | F-금지 자기 검증 (Layer 1 grep) | 실 API key / 실 endpoint 호출 / production data 0건 grep |
| 10 | Build summary.json | step output 집계 → `group-a3-logs/summary.json` |
| 11 | Upload artifact | `actions/upload-artifact@v4` `provider-url-scanner-evidence` retention 30일 |
| 12 | Evidence summary | `$GITHUB_STEP_SUMMARY` |

**artifact path = `group-a3-logs/`** (Group F 후속 답습 — leading dot 미사용).

### 11.2 paths trigger

```yaml
paths:
  - tools/provider_url_scanner.py
  - tests/fixtures/provider_url_scanner/**
  - .github/workflows/provider-url-scanner.yml
```

---

## 12. 풀 3+1 승격 trigger 자기 검증 (사용자 명시 6 trigger)

| # | Trigger | 본 PoC 발화 | 자기 검증 |
|---|---------|-----------|----------|
| 1 | URL Tier-1 catalog 를 Tier-2/3 로 확장 | ❌ 미발화 | Tier-1 10 catalog 한정 (변경 0건) |
| 2 | model name catalog 변경 필요 | ❌ 미발화 | Tier-1 19+ catalog 한정 |
| 3 | allowlist 정책 변경 필요 | ❌ 미발화 | §9.3 "yaml만 허용" 답습만 |
| 4 | Group A 1차/2차 답습 형식을 벗어남 | ❌ 미발화 | 직접 답습 |
| 5 | ADR-009 / ADR-011 / llm-providers-design.md §9 와 충돌 | ❌ 미발화 | cross-reference 답습 |
| 6 | false positive가 정상 개발 흐름을 과도하게 차단 | ⚠️ 부분 위험 — fixture 한정으로 회피 | 본 PoC = fixture 한정, 실 src/ 적용 = 별도 합의 |

**합산 0/6 발화 (#6 부분은 fixture 한정으로 통제)** → **Reviewer-only 단축 합의 적격**.

---

## 13. Evidence 형식 (5종 — Group A/B/C/D/E/F/G 답습)

| Evidence | 형식 | 본 PoC 산출 |
|---|---|---|
| Markdown report | 본 사양 (`docs/phase0/g2-gp5-poc3-...`) | 본 문서 |
| JSONL ledger entry | summary.json (단순화 — Group D/E/G 답습) | summary.json 16 항목 |
| 격리 검증 | fixture 한정 + 실 API key 0건 + 실 endpoint 호출 0건 + 외부 의존 0건 | F-금지 grep step 자동 강제 |
| GitHub Actions run | actual run id / duration / step PASS 매트릭스 | `provider-url-scanner.yml` 실행 결과 |
| 합의 보고서 | Reviewer-only 단축 (`docs/review/3plus1-consensus-2026-05-10-g2-gp5-poc3-...`) | 본 PoC 산출물 #8 |

---

## 14. 변경 이력

| 일자 | 변경 | 비고 |
|------|------|------|
| 2026-05-10 | 신규 작성 (DRAFT) | Group A 3차 진입 사양 — Layer 1c 모법 답습 (Group A 2차 합의 §5.5 #C-8 답습 의무). 사용자 명시 6 검증 / 6 trigger / 8 금지 / 9 fixture / 2 mode (url-endpoint + model-name) / Tier-1 catalog (URL 10 + model 19+) / extension allowlist (8 / 5) / stdlib 단독 채택. Group A 1차/2차 + Group B + Group C + Group D + Group E + Group F + Group G 사양 형식 직접 답습. ADR-009 C-N §5 + llm-providers-design.md §9.3 + ADR-011 §2.1 답습 (변경 0건). Reviewer-only 단축 합의 적격 (풀 3+1 trigger 0/6 발화). artifact path `group-a3-logs/` (Group F 후속 답습, leading dot 미사용). |
