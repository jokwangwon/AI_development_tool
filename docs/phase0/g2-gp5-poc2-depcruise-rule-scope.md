# G2 GP-5 2차 PoC — depcruise rule 범위 정리 (풀 3+1 합의 입력)

> **상태**: SCOPE DRAFT (2026-05-10, Group A 2차 — 풀 3+1 합의 *직전* 입력 문서)
> **목적**: 사용자 명시 답습 — "실제 코드 작성 전 먼저 7항목 정리 → 풀 3+1 합의 → 구현"
> **답습 출처**: `llm-providers-design.md` §9.3, `hermes-adoption-design-v3.md` §10.1·§11.1, `implementation-runtime-roadmap.md` Group A, `external-review/2026-05-09-g2g3g4-promotion-response-claude.md` L39 (depcruise 본질적 한계 답습)
> **상위 권위**: ADR-008 부록 C, ADR-009 C-N §2.3+§5, ADR-011 §2.1 (a)~(e)
> **선행 작업**: 1차 PoC (commit a3693a0 + 0f503a4 — AST scanner + fixture + CI)

---

## 0. 핵심 쟁점 — 풀 3+1 합의가 필요한 이유

### 0.1 도구 정합성 모순

| 사양 명세 (§9.3) | 본 repo 현실 |
|----------------|------------|
| `.depcruise.cjs` (JS 도구체인) | Python 메타-템플릿 (코드 0줄, `docker/r2-poc/r2_poc.py` + `docker/r4-1-poc/r4_1_poc.py` 만 Python real code) |
| `forbidden.from.pathNot: "^src/adapters/llm/facade\\.py$"` (.py 경로) | depcruise 는 *JS/TS dependency graph* 분석 도구 — Python 호환 비공식 |
| `to: { path: "^(litellm\|anthropic\|openai\|...)" }` | Python 의 `import` 문은 depcruise 가 *직접 파싱 못 함* (TypeScript-Estree 기반) |

**의문**: §9.3 의 `.depcruise.cjs` 명세는 *Bβ-2 의 추상적 룰 시제* (개략, P5 문서로 상세화) 이고, **실제 Python 환경 도입 가능성/대안**은 미합의 상태.

### 0.2 외부 LLM 답습 — depcruise 본질적 한계

`external-review/2026-05-09-g2g3g4-promotion-response-claude.md` L39 답습:

> P10 후보 — Provider-specific endpoint hardcoding: skill 본문이 `https://api.anthropic.com/v1/messages` 같은 URL을 직접 박는 경우. **depcruise는 import만 검사, URL 문자열은 검사 못 함**. P6 facade 우회의 변종.

L51 답습:

> enforcement는 PR review + depcruise에 의존 — depcruise는 코드 수준은 잡되 **의미적 lock-in (특정 모델의 특정 출력 포맷에 대한 가정)은 못 잡습니다**.

**즉 depcruise 의 본질적 한계 3종**:
1. URL/endpoint 하드코딩 검사 불가 (import 만 검사)
2. 의미적 lock-in 검사 불가 (코드 수준 의존만)
3. 동적 import 검사 불가 (`importlib.import_module`, `__import__`)

→ 1차 PoC AST scanner 가 #3 (동적 import) + 모델명 분기를 보완. 2차 depcruise rule 은 *static dependency graph 차단* 만.

### 0.3 풀 3+1 합의 적용 조건 발화

CLAUDE.md §3 "적용 기준":
- "보안 관련 변경 → 3+1 (필수)" — depcruise rule 도입 = Provider Liquidity Layer 1 모법 강화
- "아키텍처 의사결정 → 3+1 (필수)" — JS 도구체인 도입 vs Python equivalent vs 1차 AST scanner 확장 = 도구 선택 결정

→ **풀 3+1 합의 필수**.

---

## 1. depcruise 적용 대상 경로 (Scope of Application)

### 1.1 본 repo 현실 진단

| 디렉터리 | Python 코드 | 검사 필요? |
|---------|-----------|----------|
| `src/` | **0건 (미존재)** — 메타-템플릿 답습 | 미래 대상 (현재 검사 무의미) |
| `tools/` | `provider_import_scanner.py` (1차 PoC) | 검사 제외 (도구 — runtime 아님) |
| `tests/fixtures/` | PASS 1 + FAIL 5 (의도적 위반) | 검사 제외 (white-list) |
| `docker/r2-poc/`, `docker/r4-1-poc/` | `r2_poc.py`, `r4_1_poc.py` (Docker 격리 PoC) | 검사 제외 (LLM 호출 0건) |

**현 시점 검사 대상 = 0건** (실제 application runtime 코드 미존재).

### 1.2 옵션 — 적용 대상 결정 후보

| 옵션 | 적용 대상 | 함의 |
|------|---------|------|
| **A** | `src/` 만 (미래 대상) — 현재 비어 있음 | depcruise rule 은 **빈 적용 대상 + future-proof 룰 정의**. 즉 형식적 시제. |
| **B** | `src/` + `docker/*-poc/` | docker PoC 도 검사 — 단 LLM 호출 0건 fixture 라 의미 약함 |
| **C** | repo 전체 (`tests/fixtures` + `tools/` + `docker/*-poc/` 명시 제외) | enforcement 광범위 — 단 false positive 위험 |

**제안**: **옵션 A** (가장 좁은 범위, future-proof)

---

## 2. 허용 import 경로 (Allow-list)

### 2.1 §4.1 답습

`src/adapters/llm/facade.py` — *정확히* 이 파일만 LiteLLM 직접 import 허용.

### 2.2 추가 후보 (검토 필요)

| 경로 | 허용 사유 | 결정 |
|------|---------|------|
| `src/adapters/llm/facade.py` | §4.1 단일 facade | ✅ 허용 |
| `src/adapters/llm/router.py` | LiteLLM Router 위임 — facade 가 위임할 때 router 가 분리될 가능성 | ⚠️ 보류 (1차는 미정의 — facade 단일 답습) |
| `src/adapters/llm/error_classifier.py` | LiteLLM 표준 예외 catch (§4.3) | ⚠️ 보류 (facade 본문 답습 — 분리 시점에 룰 갱신) |

**제안**: **`src/adapters/llm/facade.py` 단일** (1차 PoC 답습 — 보수적)

---

## 3. 금지 import 경로 (Forbidden)

### 3.1 §9.3 답습 (5종)

```
litellm
anthropic
openai
google.generativeai (보수적: google 단독 — 1차 AST scanner 답습)
ollama
```

### 3.2 추가 후보 (검토 필요)

| 패턴 | 차단 사유 | 결정 |
|------|---------|------|
| `@anthropic-ai/sdk` (JS) | §9.3 명시 — JS SDK | ⚠️ Python repo 무관 (1차 PoC 미적용) |
| `@openai/openai-node` | 동상 | ⚠️ Python repo 무관 |
| `httpx`/`requests` 직접 사용으로 `api.anthropic.com` 호출 | §9.3 #2 — endpoint 하드코딩 | ❌ depcruise 검사 불가 (외부 LLM 답습) — *grep 보조* 또는 *runtime egress 검사* (3차 R-2/R-4.1) |

**제안**: §9.3 의 5종 (`litellm`, `anthropic`, `openai`, `google.generativeai`, `ollama`) — 1차 PoC 답습

---

## 4. 예외 경로 (Exempt)

| 경로 | 예외 사유 |
|------|---------|
| `src/adapters/llm/facade.py` | §3.1 허용 경로 |
| `tests/fixtures/provider_adapter_enforcement/` | 검증 fixture (의도적 위반 — 검사 대상이지만 룰 적용 제외) |
| `tools/` | 도구 — runtime 아님 |
| `docker/r2-poc/`, `docker/r4-1-poc/` | Docker 격리 PoC — LLM 호출 0건 |
| `tests/` 일반 | mock 사용 가능 (단, 본 1차/2차 PoC 에서는 fixture 만 검증) |

---

## 5. 테스트 fixture

### 5.1 1차 PoC fixture 재사용

| fixture | 1차 검증 | 2차 depcruise 검증 |
|---------|---------|-----------------|
| `pass/facade_only.py` | AST scanner 위반 0건 | depcruise 의존 그래프 위반 0건 |
| `fail/direct_import.py` | direct-import:openai | depcruise: from `fail/direct_import.py` to `openai` 위반 |
| `fail/from_import.py` | from-import:anthropic | depcruise: from `fail/from_import.py` to `anthropic` 위반 |
| `fail/dynamic_importlib.py` | dynamic-importlib:litellm | depcruise: **검출 불가** (동적 import — 본질적 한계) |
| `fail/double_underscore_import.py` | double-underscore-import:openai | depcruise: **검출 불가** (동적 import) |
| `fail/model_name_branch.py` | model-name-branch:claude-opus-4-7 | depcruise: **검출 불가** (문자열) |

### 5.2 추가 fixture 후보

| 신규 fixture | 검증 대상 |
|------------|---------|
| `fail/transitive_import.py` (가) | A → B → openai 의 transitive 의존 차단 (depcruise 의 본래 강점) |

**제안**: **1차 fixture 재사용** + (선택) **transitive_import.py** 1건 추가

---

## 6. CI 연결 방식

### 6.1 옵션

| 옵션 | 방식 | 장단 |
|------|------|------|
| **CI-A** | 1차 `provider-adapter-enforcement.yml` workflow 안에 step 추가 | 단일 workflow — 통합 evidence |
| **CI-B** | 별도 `provider-adapter-depcruise.yml` workflow 생성 | 분리 — 각 도구 독립 PASS/FAIL |
| **CI-C** | 1차 AST scanner + 2차 depcruise 를 *AND 조건* 결합 (양쪽 통과해야 PASS) | 가장 강한 enforcement — 단 depcruise FP 위험 시 false block |

**제안**: **CI-A** (단일 workflow, step 추가) — 1차 PoC 와 evidence 연속성

### 6.2 setup-node action

```yaml
- uses: actions/setup-node@v4
  with:
    node-version: "20"
- run: npm install -g dependency-cruiser
- run: depcruise --config .dependency-cruiser.cjs src/
```

**Python repo 에 Node 도구 도입 = dev-dependency 확장** — 풀 3+1 합의 핵심 쟁점.

---

## 7. FP / FN 방지 기준

### 7.1 False Positive 방지

| FP 위험 | 방지 방법 |
|---------|---------|
| Python 표준 라이브러리 import → 위반 오인 | depcruise rule 의 `from.path` 를 `src/` 로만 한정 |
| 검증 fixture 의 의도적 위반 → CI 실패 | `tests/fixtures/` 명시 제외 |
| 도구/PoC 코드 (LLM 호출 0건) → 위반 오인 | `tools/`, `docker/*-poc/` 명시 제외 |
| `google` 모듈 (`google.protobuf` 등 비-LLM) 차단 | 보수적 — `google.generativeai` 만 차단 (`google` 단독 매치 시 후속 검토) |

### 7.2 False Negative 방지 (외부 LLM 답습)

| FN 위험 | 방지 방법 |
|---------|---------|
| 동적 import (`importlib.import_module`, `__import__`) | **depcruise 영역 외** — 1차 AST scanner 가 보완 (역할 분담 명시) |
| URL/endpoint 하드코딩 (`https://api.anthropic.com/...`) | **depcruise 영역 외** — *3차 grep 룰* 또는 *runtime egress 검사* (R-2/R-4.1) 분리 |
| 의미적 lock-in (특정 모델 출력 가정) | **depcruise 영역 외** — 코드 리뷰 + 라운드트립 검증 (P2-5) |
| Transitive 의존 (A → B → openai) | **depcruise 의 본래 강점** — 본 PoC 핵심 추가 가치 |

---

## 8. 도구 선택 결정 (풀 3+1 합의 핵심 쟁점)

### 8.1 옵션 비교

| 옵션 | 도구 | Python 호환 | §9.3 답습 | 학습 비용 | 도입 비용 |
|------|------|----------|----------|---------|---------|
| **T-1** | dependency-cruiser (JS native) | **비공식 — Python 정식 미지원** | ✅ §9.3 직접 답습 | 中 (npm 도구) | 高 (Node 환경 + npm 의존) |
| **T-2** | import-linter (Python native) | ✅ 공식 | ⚠️ §9.3 시제 의도 답습 (도구만 변경) | 低 (Python ecosystem) | 低 (pip 의존만) |
| **T-3** | ruff custom rule | ✅ 공식 | ⚠️ §9.3 의 *AST 해석* 답습 (depcruise 와 다른 도구) | 中 (ruff plugin 작성) | 中 |
| **T-4** | 1차 AST scanner 확장 (transitive 의존 분석) | ✅ stdlib 만 | ❌ §9.3 의 depcruise 명시 미답습 | 高 (자체 구현) | 中 |

### 8.2 결정 권고 (Reviewer 사전 의견 — 풀 3+1 입력)

**옵션 T-2 (`import-linter`)** 권고 사유:
1. Python repo 정합성 — Node 환경 도입 회피
2. §9.3 의 *룰 시제* (allow path / forbidden path) 답습 가능 — 도구만 다름
3. dev-dep 1개 (`pip install import-linter`) 만 추가 — 도구체인 확장 최소
4. CI 통합 단순 (Python 환경 그대로 사용)

**단**, §9.3 가 명시적으로 `.depcruise.cjs` 를 적시하므로 *답습 충실성* 측면에서 옵션 T-1 도 정당화 가능. → 풀 3+1 합의가 도구 선택을 정한다.

---

## 9. 풀 3+1 합의 의제 (Agent A/B/C + Reviewer)

| Agent | 관점 | 핵심 질문 |
|-------|------|---------|
| **Agent A** (구현 분석가) | "실제로 동작하는가?" | T-1~T-4 옵션의 기술적 구현 가능성, 의존성, FP/FN 위험 |
| **Agent B** (품질/안전성 검증가) | "안전하고 견고한가?" | §9.3 답습 충실성, FP 발생 시 false block 위험, 도입 비용 vs 보안 이득 |
| **Agent C** (대안 탐색가) | "더 나은 방법이 있는가?" | T-2/T-3/T-4 의 §9.3 답습 충실성 재검토, 1차 AST scanner + 2차 depcruise 의 중첩 vs 분리 |
| **Reviewer** (검토 에이전트) | "최선의 합의는?" | 도구 선택 + 적용 범위 + CI 통합 + FP/FN 기준 최종 결정 |

---

## 10. 사용자 명시 금지사항 답습

본 단계에서도 다음은 금지:

1. ❌ G2 GP-5 최종 PASS 선언
2. ❌ G2 전체 Implementation/Runtime PASS 선언
3. ❌ Hermes PMO 격상 선언
4. ❌ 실제 provider API key 사용
5. ❌ 실제 외부 API 호출
6. ❌ Provider 구현 자체 변경

본 PoC 는 *Layer 1 형식 차단 강화* 만, runtime / API key / Provider 구현 무관.

---

## 11. 변경 이력

| 일자 | 변경 | 비고 |
|------|------|------|
| 2026-05-10 (Group A 2차) | 신규 작성 | 풀 3+1 합의 *직전* 입력 문서, 7항목 정리 + 도구 선택 옵션 (T-1~T-4) |
