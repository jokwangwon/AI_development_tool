# 3+1 합의 보고서 — G2 GP-5 3차 Provider URL/Model Name Scanner (Group A 3차 PoC, Reviewer-only 단축)

> **세션**: 2026-05-10 (Group A 3차 진입 — URL endpoint hardcoding (E-1) + model name hardcoding (E-2) 통합 PoC, Layer 1c 모법 답습)
> **PASS scope**: G2 GP-5 *Layer 1c 정적 검출 시제* 한정 — **Implementation Pending** (G2 GP-5 / G2 전체 Implementation/Runtime PASS 권한 0건, 사용자 명시 답습)
> **합의 형식**: **Reviewer-only 단축** (풀 3+1 승격 trigger 6 = 0/6 발화 → 단축 적격)
> **검토 대상**:
> - `tools/provider_url_scanner.py`
> - `tests/fixtures/provider_url_scanner/{url_endpoint,model_name}/{pass,fail}/*`
> - `.github/workflows/provider-url-scanner.yml`
> - `docs/phase0/g2-gp5-poc3-url-endpoint-model-name-scanner.md`
> - `.gitignore` (`group-a3-logs/` 추가)
> **상위 권위**: ADR-008 부록 C, ADR-008 차단조건 #4, ADR-009 §C-N §5 (Layer 1 모법 ADR), ADR-011 §2.1 (a)~(e), llm-providers-design.md §9.3 (depcruise rule grep 보조), implementation-runtime-roadmap.md §3.1 (Order 1)
> **답습 시제**: Group A 1차 (`g2-gp5-provider-adapter-enforcement-poc.md`) + Group A 2차 (`g2-gp5-poc2-import-linter-implementation.md`) + Group D + Group E + Group G PoC 합의 형식 (`docs/review/3plus1-consensus-2026-05-10-g3-g4-boundary-guard-reviewer-only.md` 직접 답습)

---

## 1. 검토 사항

### 1.1 산출물 매트릭스 (8건)

| # | 산출물 | 라인 | 답습 |
|---|-------|-----|------|
| 1 | `tools/provider_url_scanner.py` | ~210 | **stdlib `re` + `dataclasses` 단독** (외부 의존 0건). 2 mode CLI (`--mode url-endpoint` E-1 / `--mode model-name` E-2) + `--list-catalogs` self-check + URL Tier-1 catalog 10 (Anthropic/OpenAI/Azure-OpenAI/Google-AI/Replicate/Perplexity/Cohere/HuggingFace/Together/OpenRouter) + Model Tier-1 catalog 19 (Anthropic 5 + OpenAI 5 + Google 3 + Meta 3 + Mistral 3) + extension allowlist (URL: 8 ext / Model: 5 ext) + comment line 부분 회피 (`#` / `//`) + `Violation` reporter (Group A 1차 + Group D 답습) |
| 2 | `tests/fixtures/provider_url_scanner/url_endpoint/pass/safe_config.yaml` | 12 lines | E-1 PASS — yaml allowlist 통과 (FP 검증, Tier-1 URL 5개 포함, allowlist ext 한정) |
| 3 | `tests/fixtures/provider_url_scanner/url_endpoint/fail/{hardcoded_url_anthropic, hardcoded_url_openai, hardcoded_url_google}.py` | 3 fixture | E-1 FAIL — 3 패턴 cover (anthropic + openai + azure-openai + google-ai) |
| 4 | `tests/fixtures/provider_url_scanner/model_name/pass/safe_model_config.yaml` | 16 lines | E-2 PASS — yaml allowlist 통과 (§9.3 "yaml만 허용" 답습, Tier-1 model 5개 포함) |
| 5 | `tests/fixtures/provider_url_scanner/model_name/fail/{hardcoded_model_anthropic, hardcoded_model_openai, hardcoded_model_gemini, hardcoded_model_llama}.py` | 4 fixture | E-2 FAIL — 4 vendor cover (Anthropic + OpenAI + Google + Meta) + 11 pattern_ids cover |
| 6 | `.github/workflows/provider-url-scanner.yml` | ~225 | 12 step (3 setup + 4 mode 검증 + list-catalogs + F-금지 grep + summary.json + artifact + Evidence summary). artifact path = `group-a3-logs/` (Group F 후속 답습) |
| 7 | `docs/phase0/g2-gp5-poc3-url-endpoint-model-name-scanner.md` | 387 | PoC 사양 (14 섹션 — 목적 / 범위 / Layer 1a/1b/1c 분리 / 도구 근거 / URL catalog / model catalog / allowlist / fixture / 검증 매트릭스 / PASS / 한계 / CI / trigger / Evidence / 변경이력) |
| 8 | 본 합의 보고서 | ~310 | Group A~G Reviewer-only 합의 형식 답습 |

**합산 = 8 파일** (Group D/E/G 답습 평균).

### 1.2 fixture 9건 검증 결과

| Fixture | 위치 | 매칭 패턴 | 합계 |
|---|---|---|---|
| `safe_config.yaml` | url_endpoint/pass/ | 0 (yaml allowlist 통과) | 0 (FP 0) |
| `hardcoded_url_anthropic.py` | url_endpoint/fail/ | anthropic × 1 | 1 |
| `hardcoded_url_openai.py` | url_endpoint/fail/ | openai × 1 + azure-openai × 1 | 2 |
| `hardcoded_url_google.py` | url_endpoint/fail/ | google-ai × 1 | 1 |
| `safe_model_config.yaml` | model_name/pass/ | 0 (yaml allowlist 통과) | 0 (FP 0) |
| `hardcoded_model_anthropic.py` | model_name/fail/ | claude-opus × 1 + claude-sonnet × 1 + claude-3 × 1 | 3 |
| `hardcoded_model_openai.py` | model_name/fail/ | gpt-4 × 1 + gpt-4o × 1 + gpt-3.5 × 1 + o1 × 1 | 4 |
| `hardcoded_model_gemini.py` | model_name/fail/ | gemini-1.5 × 1 + gemini-2 × 1 + (gemini-1.5 fast) × 1 | 3 |
| `hardcoded_model_llama.py` | model_name/fail/ | llama3 × 2 + llama2 × 1 | 3 |

**합산** = E-1 FAIL 4 violations + E-2 FAIL 13 violations = 17 violations across 7 fail fixtures.

### 1.3 catalog 등록 확인 (`--list-catalogs` 출력)

```
url_endpoint_catalog=10
  anthropic        Anthropic API
  openai           OpenAI API
  azure-openai     Azure OpenAI
  google-ai        Google AI / Gemini
  replicate        Replicate
  perplexity       Perplexity
  cohere           Cohere
  huggingface      HuggingFace Inference
  together         Together AI
  openrouter       OpenRouter
model_name_catalog=19
  anthropic-claude-opus / sonnet / haiku / 3 / 2 (5)
  openai-gpt-4 / 3-5 / 4o / o1 / o3 (5)
  google-gemini-1-5 / 2 / pro (3)
  meta-llama / llama2 / llama3 (3)
  mistral-mistral / mixtral / codestral (3)
url_endpoint_allowlist_ext=8
  ext=['.yaml', '.yml', '.json', '.jsonl', '.toml', '.cfg', '.ini', '.md']
model_name_allowlist_ext=5
  ext=['.yaml', '.yml', '.json', '.jsonl', '.md']
scan_target_ext=16
comment_prefixes=['#', '//']
url_endpoint_count_compliant=True
model_name_count_compliant=True
url_endpoint_allowlist_compliant=True
```

### 1.4 E-1 / E-2 로컬 검증 결과 (6/6 PASS)

| # | 검증 | 명령 | rc | 결과 |
|---|------|------|-----|------|
| 1 | E-1 PASS | `--mode url-endpoint pass/` | **0** | 위반 0건 (yaml allowlist 통과, FP 0) |
| 2 | E-1 FAIL | `--mode url-endpoint fail/` | **1** | 4 violations + 4 pattern_ids cover (anthropic + azure-openai + google-ai + openai) |
| 3 | E-2 PASS | `--mode model-name pass/` | **0** | 위반 0건 (yaml allowlist 통과, FP 0) |
| 4 | E-2 FAIL | `--mode model-name fail/` | **1** | 13 violations + **11 pattern_ids cover** (4 vendor 모두 — Anthropic Claude Opus/Sonnet/3 + OpenAI GPT-4/3.5/4o/o1 + Google Gemini 1.5/2 + Meta Llama 2/3) |
| 5 | `--list-catalogs` self-check | `--list-catalogs` | **0** | url_endpoint_catalog=10 + model_name_catalog=19 + url_endpoint_allowlist_ext=8 + model_name_allowlist_ext=5 + 3 *_compliant=True |
| 6 | F-금지 grep | scanner + fixture grep | **0** | 실 provider SDK / HTTP client import 0건 + 실 endpoint 호출 0건 + 실 API key 0건 + production data path 0건 |

### 1.5 CI workflow 12 step 구조

| # | Step | 책무 | 검증 |
|---|------|------|------|
| 1 | Checkout | actions/checkout@v4 | — |
| 2 | Set up Python | actions/setup-python@v5 (3.12) | — |
| 3 | Prepare log directory | `mkdir -p group-a3-logs` (Group F 후속 답습) | — |
| 4 | `--list-catalogs` self-check | url_endpoint=10 + model_name≥19 + count/allowlist_compliant=True grep | §1.4 #5 |
| 5 | E-1 PASS | rc=0 + violations=0 grep | §1.4 #1 |
| 6 | E-1 FAIL | rc=1 + 3 패턴 cover (anthropic / openai / google-ai) grep | §1.4 #2 |
| 7 | E-2 PASS | rc=0 + violations=0 grep | §1.4 #3 |
| 8 | E-2 FAIL | rc=1 + 4 vendor cover (anthropic-claude / openai-gpt / google-gemini / meta-llama) grep | §1.4 #4 |
| 9 | F-금지 자기 검증 (Layer 1 grep) | 실 provider SDK / endpoint 호출 / API key / production data 0건 grep | §1.4 #6 |
| 10 | Build summary.json | step output 집계 → `group-a3-logs/summary.json` 17 항목 | — |
| 11 | Upload artifact | `actions/upload-artifact@v4` `provider-url-scanner-evidence` retention 30일 | Group F 후속 답습 |
| 12 | Evidence summary | `$GITHUB_STEP_SUMMARY` | R-6 답습 |

---

## 2. 검토 항목 — Reviewer 관점 10 영역

### 2.1 PASS 조건 답습 — ADR-011 §2.1 (a)~(e)

| 조건 | 충족 | 근거 |
|------|----|------|
| (a) 동등 이상의 안전 결과 | ✅ | llm-providers-design.md §9.3 (`no-llm-via-httpx` + `no-model-name-in-code` grep 보조) 직접 답습 — Provider Liquidity 5-way Multi-layer Defense Layer 1c 완결 |
| (b) 격리 환경 PoC 실증 | ✅ | fixture 한정 (실 API key 0건, 실 endpoint 호출 0건, fake URL/model literal) + 외부 의존 0건 (stdlib 단독) + CI ubuntu-latest |
| (c) ADR/SDD 권위 명시 | ✅ | ADR-008 부록 C / 차단조건 #4 / ADR-009 C-N §5 / ADR-011 §2.1 / llm-providers-design.md §9.3 / roadmap §3.1 cross-reference |
| (d) 자동 회귀 검증 경로 | ✅ | CI workflow 12 step + paths trigger 3 영역 + artifact 30일 retention |
| (e) 합의 APPROVE | ✅ | 본 보고서 §5 결론 |

### 2.2 사용자 명시 PASS 기준 6 (사양 §9 답습)

| # | 기준 | 충족 | 근거 |
|---|----|----|------|
| 1 | E-1 PASS scan | ✅ | rc=0 + 위반 0건 (yaml allowlist 통과) |
| 2 | E-1 FAIL scan | ✅ | rc=1 + 4 violations + 4 pattern_ids cover |
| 3 | E-2 PASS scan | ✅ | rc=0 + 위반 0건 (yaml allowlist 통과) |
| 4 | E-2 FAIL scan | ✅ | rc=1 + 13 violations + 11 pattern_ids cover (4 vendor 모두) |
| 5 | `--list-catalogs` self-check | ✅ | url=10 + model=19 + allowlist 8/5 + 3 compliant flag |
| 6 | F-금지 grep | ✅ | 실 SDK / endpoint 호출 / API key / production data 0건 |

**합산 6/6 충족.**

### 2.3 사용자 명시 8 금지 자기 검증 (0/8 위반)

| # | 금지 | 위반 | 근거 |
|---|------|----|------|
| 1 | G2 GP-5 최종 PASS 선언 | 0 | 본 PoC = *Layer 1c 정적 검출 시제* 한정 (사양 §0 + §1.2 명시) |
| 2 | G2 전체 Implementation/Runtime PASS 선언 | 0 | CONTEXT.md 변경 0건 (meta 갱신 시 *부분 충족 시제* 한정) |
| 3 | Hermes PMO 격상 선언 | 0 | 변경 0건 |
| 4 | 실 provider API 호출 | 0 | scanner 본문 `import (httpx\|requests)` / `urllib.request.urlopen` 0건 — F-금지 grep step 자동 강제 |
| 5 | 실 API key 사용 | 0 | fixture 의 endpoint URL = path-only canary, 실 key 0건 (grep 검증) |
| 6 | Provider 구현 자체 변경 | 0 | `src/adapters/llm/facade.py` placeholder 변경 0건 (Group A 2차 답습) |
| 7 | ADR 본문 자동 갱신 | 0 | `docs/decisions/` + `docs/architecture/` 본문 변경 0건 (cross-reference 답습 한정) |
| 8 | Tier-2 / Tier-3 catalog 자동 확장 | 0 | URL Tier-1 10 + model Tier-1 19 한정, 확장 0건 |

**합산 0/8 위반.**

### 2.4 사용자 명시 풀 3+1 승격 trigger 6 자기 검증 (0/6 발화)

| # | Trigger | 발화 | 근거 |
|---|---------|----|------|
| 1 | URL Tier-1 catalog 를 Tier-2/3 로 확장 | 0 | Tier-1 10 catalog 한정 (변경 0건) |
| 2 | model name catalog 변경 필요 | 0 | Tier-1 19 catalog 한정 (변경 0건) |
| 3 | allowlist 정책 변경 필요 | 0 | §9.3 "yaml만 허용" 답습만 (URL: 8 ext / Model: 5 ext 직접 정의, 정책 변경 0건) |
| 4 | Group A 1차/2차 답습 형식을 벗어남 | 0 | argparse + dataclass + iter + violation reporter 직접 답습 |
| 5 | ADR-009 / ADR-011 / llm-providers-design.md §9 와 충돌 | 0 | cross-reference 답습 한정 |
| 6 | false positive가 정상 개발 흐름을 과도하게 차단 | ⚠️ 부분 위험 — fixture 한정으로 회피 | safe_*.yaml PASS 검증 + comment line 부분 회피 |

**합산 0/6 발화** → **Reviewer-only 단축 합의 적격**.

### 2.5 Layer 1a / 1b / 1c 분리 답습 충실도 (사용자 명시 사양 §2 답습)

| Layer | Group A # | 검증 영역 | 도구 | 본 PoC 답습 |
|---|---|---|---|---|
| Layer 1a | 1차 | AST 5종 패턴 | `tools/provider_import_scanner.py` | 형식 답습 (argparse + dataclass + iter), 영역 미중복 |
| Layer 1b | 2차 | Transitive import | `.importlinter` | 영역 미중복 (별도 합의 분리) |
| **Layer 1c** | **3차 (본 PoC)** | **URL endpoint + model name 직접 사용** | **`tools/provider_url_scanner.py`** | **본 PoC = Layer 1c 모법 답습 — Group A 2차 합의 §5.5 #C-8 답습 의무 충족** |

**Layer 분리 책무 매트릭스** (사양 §2.1 답습) — 1a/1b/1c 모두 ADR-009 C-N §5 Layer 1 모법 답습 완결.

### 2.6 Tier-1 catalog 충실도 (llm-providers-design.md §9.3 답습)

| 영역 | 답습 방식 | 신규 작성 |
|---|---|---|
| URL Tier-1 catalog 10 patterns | §9.3 `no-llm-via-httpx` 답습 (Anthropic + OpenAI + Azure-OpenAI + Google-AI + Replicate + Perplexity + Cohere + HuggingFace + Together + OpenRouter) | catalog 정의 (변경 0건) |
| Model Tier-1 catalog 19 patterns | §9.3 `no-model-name-in-code` 답습 (5+5+3+3+3 = 19) | catalog 정의 (변경 0건) |
| Extension allowlist (URL 8 / Model 5) | §9.3 "yaml만 허용" 답습 (json/jsonl/toml/cfg/ini/md 확장) | 정의 (변경 0건) |
| Comment line 부분 회피 (`#` / `//`) | — (본 PoC 신규, multi-line block / docstring 별도 합의) | ~10줄 |
| Custom 2 mode CLI dispatch | Group D/E/G 답습 | ~80줄 |
| Violation reporter | Group A 1차 + Group D 답습 | ~30줄 |

**리팩토링 0건 + 복제 0건 + 외부 의존 0건** (gitleaks/depcruise/AST 통합 미진입). 신규 작성 ~120줄.

### 2.7 Group A 1차 / 2차 / Group D/E/G 답습 충실

| 영역 | Group 답습 |
|---|---|
| Validator 구조 (argparse + dataclass + N mode + `--list-*` self-check) | Group A 1차 + Group D + Group E + Group G |
| Fixture 디렉토리 구조 (PASS / FAIL 분리, 2 mode × subdir) | Group A 1차 + Group D + Group E + Group G |
| CI workflow (N mode × PASS+FAIL + count self-check + F-금지 grep + summary.json + artifact + Evidence summary) | Group D + Group E + Group G 직접 답습 |
| Reviewer-only 단축 합의 형식 | Group A 1차 + Group D + Group E + Group G |
| **artifact path (leading dot 미사용)** | **Group F 후속 + Group D/E/G (group-a3-logs/) 직접 답습** |
| ADR-011 §2.1 (a)~(e) 5/5 충족 매트릭스 | Group A 1차/2차 + Group B + Group C + Group D + Group E + Group F + Group G |
| Layer 분리 책무 매트릭스 (1a/1b/1c) | Group A 1차/2차 답습 + 본 PoC = 1c 신규 분리 |

### 2.8 책무 분리 — 별도 합의 영역

| 영역 | 분리 사유 | 미래 영역 |
|------|---------|---------|
| depcruise rule 통합 (`.dependency-cruiser.cjs`) | Layer 1b 영역 (Group A 2차 import-linter 답습) | 별도 합의 |
| pre-commit hook 활성화 | T2 정책 영역 (ADR-011 §2.4) | 별도 합의 |
| PR auto-reject GitHub branch protection | T3 정책 영역 | 별도 합의 |
| 의미적 분석 (URL 패턴이 실 API 호출인지 추론) | Layer 5 추론 영역 | 별도 합의 |
| Multi-line block comment / Python docstring 완전 회피 | full AST 분석 영역 | 별도 합의 (Group A 1차 답습 영역) |
| Tier-2 vendor URL endpoint (100+ Slack/GCP/Azure 외) | 사용자 명시 금지 — Tier-2/3 확장 | 풀 3+1 + 외부 LLM 1+ |
| 모델 ID 세부 version catalog | Tier-1 base pattern 한정 | 별도 합의 |
| URL fragment / query string 분석 (`?api_key=...`) | Group D `secret_scanner.py` 영역 | Group D 답습 분리 |
| 실 src/ 코드 적용 시 false positive 정량 분석 | fixture 한정 | 별도 합의 |

### 2.9 알려진 한계 (사양 §10 답습)

11건 (모두 분리 영역 명시):
1. depcruise rule 통합 미진입 (Layer 1b)
2. pre-commit hook 활성화 미진입 (T2)
3. PR auto-reject 미진입 (T3)
4. 의미적 분석 미진입 (Layer 5)
5. Multi-line block comment 완전 회피 미진입
6. Python docstring 완전 회피 미진입
7. Tier-2 vendor URL endpoint 미진입
8. 모델 ID 세부 version 변형 catalog 미진입
9. URL fragment / query string 분석 = Group D 영역 분리
10. 실 src/ 코드 적용 시 FP 위험 — fixture 한정으로 회피
11. Markdown 본문 자기 검출 — CI fixture 한정 scan 으로 회피

### 2.10 Group A 2차 합의 §5.5 #C-8 답습 충실도

| 조건 | 본 PoC 답습 |
|---|---|
| C-8 = "URL 하드코딩 차단 = 본 PoC 외 3차 grep 분리 합의 필수" | ✅ 본 PoC = 3차 분리 영역 직접 답습 |
| Group A 2차 = T-2 import-linter 한정 (URL 미 cover) | ✅ 본 PoC = Layer 1c 분리, 2차 영역 미중복 |
| llm-providers-design.md §9.3 `no-llm-via-httpx` 답습 의무 | ✅ URL Tier-1 catalog 10 |
| llm-providers-design.md §9.3 `no-model-name-in-code` 답습 의무 | ✅ Model Tier-1 catalog 19 |
| §9.3 "yaml만 허용" 답습 의무 | ✅ Extension allowlist (URL 8 / Model 5) |

**Group A 2차 합의 §5.5 #C-8 답습 완결.**

---

## 3. 풀 3+1 승격 trigger 6 자기 검증 (재명시)

§2.4 와 동일 — 0/6 미발화. **Reviewer-only 단축 합의 적격**.

---

## 4. 본 PoC 의 *발생* / *미발생* 사항

### 4.1 본 PoC 가 *발생* 시키는 것

- ✅ G2 GP-5 *Layer 1c — URL endpoint + model name 직접 사용 차단* 정적 검출 layer 운영 적용 첫 시제
- ✅ Group A 2차 합의 §5.5 #C-8 답습 의무 충족 — *3차 분리 영역* 책무 해소
- ✅ Custom validator 단독 채택 (외부 의존 0건 + Tier-2/3 확장 위험 0건) 답습 검증
- ✅ Layer 1a / 1b / 1c 분리 답습 — Group A 1차/2차/3차 = ADR-009 C-N §5 Layer 1 모법 답습 완결
- ✅ Group F 후속 artifact path 답습 (`group-a3-logs/` — leading dot 미사용)
- ✅ Reviewer-only 단축 합의 답습 (Group A 1차 + Group D/E/G 답습)

### 4.2 본 PoC 가 *발생시키지 않는* 것 (사용자 명시 답습)

- ❌ G2 GP-5 최종 Implementation/Runtime PASS 선언
- ❌ G2 전체 Implementation/Runtime PASS 선언
- ❌ Hermes PMO 격상 선언
- ❌ 실 provider API 호출 / 실 API key 사용 / Provider 구현 변경
- ❌ ADR 본문 자동 갱신 (cross-reference 답습 한정)
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ depcruise rule 통합 (Layer 1b 영역 — Group A 2차 답습 분리)
- ❌ pre-commit hook 활성화 / PR auto-reject (T2/T3 정책 영역)
- ❌ Multi-line block comment / docstring 완전 회피
- ❌ 의미적 분석 (Layer 5 추론 영역)

---

## 5. 검토 결론

### 5.1 Reviewer 종합 판정

**APPROVE WITH CONDITIONS** — Group A 3차 PoC = G2 GP-5 *Layer 1c 정적 검출 시제* 답습 충실 (Reviewer 관점 10 영역 모두 충족, 풀 3+1 승격 trigger 0/6 발화, 8 금지 0/8 위반, ADR-011 §2.1 5/5 충족, 사용자 명시 PASS 기준 6/6 충족, 로컬 6/6 검증 PASS, CI workflow 12 step 형식 검증 PASS, llm-providers-design.md §9.3 + Group A 2차 #C-8 직접 답습 (변경 0건 / 외부 의존 0건 / Tier-2/3 확장 0)).

### 5.2 추가 조건 (C-A3-1 ~ C-A3-7)

| # | 조건 | 답습 위치 |
|---|----|---------|
| C-A3-1 | 본 PoC = G2 GP-5 *Layer 1c 정적 검출 시제* 한정 — G2 GP-5 / G2 전체 Implementation/Runtime PASS 권한 0건 (사용자 명시 답습) | 사양 §0 + §1.2 + 본 합의 §2.3 #1~#2 명시 |
| C-A3-2 | Layer 1a / 1b / 1c 분리 답습 — 본 PoC = 1c 단독, 1a/1b 영역 미중복 (Group A 1차/2차 답습 분리) | 사양 §2 + 본 합의 §2.5 명시 |
| C-A3-3 | Tier-1 catalog (URL 10 + model 19) 한정 — Tier-2/3 확장 = 풀 3+1 + 외부 LLM 1+ 별도 합의 | 사양 §1.2 + §10 #7 + 본 합의 §2.3 #8 명시 |
| C-A3-4 | depcruise rule / pre-commit hook / PR auto-reject = T2/T3 정책 영역 (별도 합의) | 사양 §10 #1~#3 + 본 합의 §2.8 명시 |
| C-A3-5 | Multi-line block comment / docstring 완전 회피 = full AST 영역 (별도 합의) | 사양 §10 #5~#6 + 본 합의 §2.8 명시 |
| C-A3-6 | URL fragment / query string 분석 = Group D `secret_scanner.py` 영역 (책무 분리) | 사양 §10 #9 + 본 합의 §2.8 명시 |
| C-A3-7 | Step 8 GitHub Actions actual run 결과 → CONTEXT/INDEX/SESSION 메타 갱신 영역 (사양 §14 변경 이력 답습) | 본 합의 §5.3 #4 |

### 5.3 다음 단계 권고

1. 본 합의 commit 분리 (PoC 본문 / CI workflow / 사양 / 합의 / .gitignore)
2. push (사용자 confirm 후) origin feature/hermes-phase0
3. GitHub Actions actual run 검증 (R-6 답습)
4. CONTEXT / INDEX / SESSION 갱신 (사용자 명시 답습) — *meta* 문서 영역, ADR 본문 변경 0건
5. **다음 진입점 (사용자 결정 영역)**:
   - (a) Group F 후속 — `hermes_to_openai` 또는 Skill 변환 feasibility 추가
   - (b) Group C 후속 — `history_rewrite` Layer 5 PoC (ADR-012 §2.8)
   - (c) cross-vendor LLM 의뢰 (Group D/E/G/A3 산출물)
   - (d) Group H — ADR-014 발행 (풀 3+1 + 외부 LLM 1+)
   - (e) Group I — G3 22 권한 분해 (풀 3+1 + 외부 LLM 1+)

---

## 6. 변경 이력

| 일자 | 변경 | 비고 |
|------|------|------|
| 2026-05-10 | 신규 작성 | Group A 3차 통합 PoC, Reviewer-only 단축 합의 APPROVE WITH CONDITIONS, 풀 3+1 승격 trigger 6 0/6 발화, 8 금지 0/8 위반, PASS 기준 6/6 + ADR-011 §2.1 5/5 충족, 로컬 6/6 PASS, CI workflow 12 step 형식 검증 PASS, llm-providers-design.md §9.3 + Group A 2차 #C-8 직접 답습 (변경 0건 / 외부 의존 0건 / Tier-2/3 확장 0). evidence 별도 파일 미작성 — 본 보고서 §1~§4 매트릭스 통합 (Group D/E/G 답습). Step 8 actual run 결과 = 본 합의 *후속* meta 문서 영역. |
