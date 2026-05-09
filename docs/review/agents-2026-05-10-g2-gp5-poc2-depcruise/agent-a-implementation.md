# Agent A — 구현 분석가 — G2 GP-5 2차 PoC depcruise rule

> **Phase**: 풀 3+1 합의 Phase 2 (독립 분석)
> **관점**: "실제로 동작하는가? 기술적 구현 가능성은?"
> **분석 일자**: 2026-05-10
> **참조 입력**: g2-gp5-poc2-depcruise-rule-scope.md (7항목 + T-1~T-4), llm-providers-design.md §9.3/§9.4, ADR-009 §5, external-review L39/L51, 1차 PoC 산출물 (provider_import_scanner.py, fixture, CI workflow)
> **답습 강제**: 다른 Agent 출력 미참조 / Reviewer 사전 권고 (T-2) 미답습 / 정책 결정 미제안 / 순수 기술 분석

---

## 0. 본 repo 환경 진단 (분석 토대)

| 항목 | 사실 |
|------|------|
| `src/` | **존재하지 않음** (`ls: src/: 그런 파일이나 디렉터리가 없습니다`) |
| `package.json` | **없음** (Node 프로젝트 manifest 부재) |
| `pyproject.toml` | **없음** (Python 패키징 manifest 부재) |
| `tools/provider_import_scanner.py` | 존재 — Python 3.11+ stdlib `ast` 기반 1차 PoC scanner |
| `tests/fixtures/provider_adapter_enforcement/{pass,fail}/` | 존재 — fixture 6건 (PASS 1 + FAIL 5) |
| `.github/workflows/provider-adapter-enforcement.yml` | 존재 — `setup-python@v5` (Python 3.11) 단일 step |
| 로컬 환경 | Node v20.20.2, Python 3.12.3 모두 사용 가능 |
| 실 LLM 호출 코드 | **0건** (`docker/r2-poc/`, `docker/r4-1-poc/` 만 — 본 PoC 와 무관) |

→ **모든 기술적 평가의 출발점**: 검사 대상 = 실질적으로 0줄. 본 PoC 는 *future-proof 룰 시제*.

---

## 1. 7항목 기술적 구현 평가

### 1-1. 적용 대상 경로 — 옵션 A (`src/` 만)

**기술적 동작 검증**:

| 도구 | `src/` 가 *부재* 일 때 동작 | 빈 `src/` 일 때 동작 |
|------|--------------------------|---------------------|
| dependency-cruiser | `depcruise --config <cfg> src/` → **error: ENOENT** (path not found, exit ≠ 0) | 빈 그래프 → exit 0 (`forbidden` 룰 위반 0건) |
| import-linter | `lint-imports` → contracts 의 `packages: [src.adapters.llm.facade]` 가 import 불가 → **모듈 미발견 에러** | `__init__.py` 만 존재 시 → contract 통과 (위반 0건, exit 0) |
| ruff | `ruff check src/` → 빈 디렉터리 → exit 0 | 정상 |
| 1차 AST scanner | `python tools/provider_import_scanner.py src/` → `[ERROR] target not found` (exit 2) | `[PASS] No violations found` (exit 0) |

**결론**: 옵션 A 는 **빈 `src/` 디렉터리 + `__init__.py` 1개를 placeholder 로 두면** 4종 모두 정상 동작. 단 *부재* 상태는 모든 도구가 ENOENT 를 던짐 → CI 가 `if [ -d src/ ]; then ... fi` 가드 또는 `mkdir -p src/` 선행 필요.

**기술 위험**: depcruise 의 빈 그래프 통과는 *vacuously true* (검사 대상이 없어 위반도 없음). enforcement 가치 = 0, 다만 *룰 시제 등록* 가치는 유지.

### 1-2. 허용 import 경로 — `src/adapters/llm/facade.py` 단일

**정규식 정확성 검증**:

```javascript
// dependency-cruiser
from: { pathNot: "^src/adapters/llm/facade\\.py$" }
```

- `^...$` 앵커 → `src/adapters/llm/facade.py` 외 매치 없음. ✅ 정확
- 단 `src/adapters/llm/facade_helper.py` 같은 prefix 매치 위험은 `\\.py$` 로 차단됨. ✅
- depcruise 는 `from.path` 를 모듈 경로 (resolved file path) 로 매칭. POSIX path separator 사용. Windows runner 사용 시 `\` ↔ `/` 변환 이슈 (GitHub Actions ubuntu-latest 기준 무관).

```ini
# import-linter
[importlinter:contract:no-direct-llm-sdk]
type = forbidden
source_modules = src
forbidden_modules = litellm, anthropic, openai, google.generativeai, ollama
ignore_imports = src.adapters.llm.facade -> litellm
                 src.adapters.llm.facade -> anthropic
                 ...
```

- import-linter 는 *모듈 단위* (Python dotted path) 만 인식 — 파일 경로 정규식 미지원. `src.adapters.llm.facade` 로 명시.
- `ignore_imports` 1줄당 1쌍 (importer → imported) → 5종 forbidden × 1 facade = **5줄** 필요. Verbose 하지만 정확.

**결론**: 두 도구 모두 단일 facade 매칭 가능. depcruise 가 정규식으로 더 간결, import-linter 가 모듈 단위로 더 명시적.

### 1-3. 금지 import 경로 — 5종 정규식 + transitive

**정규식 패턴 정확성**:

| 도구 | 패턴 | `google.generativeai` vs `google.protobuf` 분리 |
|------|------|------------------------------------------------|
| depcruise | `to.path: "^(litellm\|anthropic\|openai\|google\\.generativeai\|ollama)"` | ✅ 가능 (정규식 정확 매칭) |
| import-linter | `forbidden_modules = google.generativeai` | ✅ 가능 (서브패키지만 차단) |
| 1차 AST scanner (현재) | `_matches_forbidden` 가 `top == "google"` 시 `google` 단독을 위반으로 보고 | ⚠️ **FP 위험** — `google.protobuf`, `google.cloud.storage` 등 비-LLM 모듈도 차단 |

→ 1차 scanner 의 `if top == "google": return "google"` 는 보수적 차단인데, *실 src/* 가 등장하면 `google.protobuf` 같은 합법 import 를 false positive 로 잡을 위험. 이는 본 2차 PoC 가 아니라 1차 scanner 의 **사전 보강 사항**.

**Transitive 의존 자동 추적**:

| 도구 | Transitive 추적 | 메커니즘 |
|------|---------------|---------|
| dependency-cruiser | ✅ 본래 강점 | TS-AST 그래프 walk → 모든 reachable 모듈을 검사 |
| import-linter | ✅ `forbidden` contract 기본 동작 | Python `importlib` 기반 그래프 (그래프 라이브러리: `grimp`) |
| ruff custom rule | ❌ Per-file 검사만 | AST per file, 그래프 미수집 |
| 1차 AST scanner | ❌ Per-file 검사만 | `ast.walk` per file |

**핵심 갭**: 2차 PoC 의 *추가 가치* = transitive 의존 추적. 1차 scanner 는 `a.py → b.py → openai` 경로를 못 잡음. dependency-cruiser 와 import-linter 는 잡음.

### 1-4. 예외 경로 — `pathNot` vs `excludeOnly`

**dependency-cruiser 옵션 비교**:

| 옵션 | 의미 | 본 case 적용 |
|------|------|------------|
| `forbidden[].from.pathNot` | 룰 단위 — 특정 룰의 source 에서 제외 | 허용 경로 (facade 단독) 표현에 적합 |
| 최상위 `options.exclude` | 전체 그래프 분석에서 제외 (graph 자체에 미포함) | white-list 5종 (tests/fixtures, tools/, docker/*-poc/, tests/) 에 적합 |
| `options.includeOnly` | 그래프 분석에 포함할 패턴만 | `src/` 만 분석 → 사실상 동등 효과 |

**기술적 권고 (config 구조)**:

```javascript
{
  options: {
    includeOnly: "^src/"  // src/ 만 그래프 수집 — tests/fixtures, tools/, docker/ 자동 제외
  },
  forbidden: [{
    name: "no-direct-llm-sdk",
    from: { pathNot: "^src/adapters/llm/facade\\.py$" },
    to: { path: "^(litellm|anthropic|openai|google\\.generativeai|ollama)" }
  }]
}
```

`includeOnly` 가 `excludeOnly` (deprecated alias) 보다 정공법. `pathNot` 은 *허용* 표현. **둘은 직교** — 함께 사용해야 정확.

**import-linter 의 동치**:
- `[importlinter] root_packages = src` 로 `src/` 만 분석.
- white-list 디렉터리는 `root_packages` 외부 → 자동 제외.
- 단 `tests/fixtures/...` 는 Python 모듈로 import 가능한 형태일 때만 영향. `tests/__init__.py` 가 없으면 grimp 가 무시.

### 1-5. 테스트 fixture — 모순 해결

**모순 진단**: §4 가 `tests/fixtures/` 를 white-list 로 두면 fixture 자체가 검사 대상에서 빠짐 → fixture 의 의도적 위반을 *검증* 할 수 없음.

**해결 방법 4가지**:

| 방법 | 메커니즘 | 비고 |
|------|---------|-----|
| **M1: 양방향 검증 (1차 PoC 답습)** | CI step 2개: (a) PASS fixture 를 검사 대상으로 명시 호출 → exit 0 기대 / (b) FAIL fixture 를 검사 대상으로 명시 호출 → exit ≠ 0 기대 | ✅ 1차 `provider-adapter-enforcement.yml` 가 이미 채택. depcruise 도 동일 패턴 적용 가능 |
| M2: fixture 를 src/ 로 이동 | fixture 가 production 룰 적용을 받음 — 단 PASS 만 두고 FAIL 은 이동 불가 | ✗ 부분 해결 |
| M3: 별도 config (test 전용) | `.depcruise.test.cjs` 가 fixture 검사 — 단 production config 가 fixture 무시 | △ config 2 벌 유지비 |
| M4: depcruise `affectedTests` 옵션 | depcruise 내장 — test 파일 별도 처리 | ✗ 본 case 와 의미 다름 (test 의 production 의존 추적용) |

**기술적 권고**: **M1** — 1차 PoC 의 양방향 검증 구조를 그대로 답습. depcruise 호출 명령을 PASS/FAIL 별로 2회 실행 + exit code 검증.

```bash
# PASS fixture
depcruise --config .depcruise.cjs tests/fixtures/provider_adapter_enforcement/pass/
# 기대: exit 0

# FAIL fixture (단, fixture 의 fail/*.py 는 transitive 부재 → depcruise 가 검출 가능한 패턴은 direct/from-import 2종만)
depcruise --config .depcruise.cjs tests/fixtures/provider_adapter_enforcement/fail/
# 기대: exit ≠ 0
```

**중요한 제약**: 1차 fixture 6건 중 depcruise 가 검출 가능한 것은 `direct_import.py` + `from_import.py` *2건만*. 동적 import 3건 + 모델명 분기 1건 = depcruise 영역 외 (scope 문서 §5.1 답습). → **2차 depcruise 는 1차 scanner 의 부분집합 검증** + transitive 추가 검증.

### 1-6. CI 연결 — CI-A (단일 workflow)

**기술적 비용**:

| 항목 | T-1 (depcruise) | T-2 (import-linter) | T-3 (ruff plugin) | T-4 (AST scanner 확장) |
|------|----------------|-------------------|------------------|---------------------|
| Runner setup | `setup-node@v4` 추가 (~10s) | 기존 `setup-python@v5` 재사용 | 기존 재사용 | 기존 재사용 |
| 의존 설치 | `npm install -g dependency-cruiser` (~30s, 첫 install) / `actions/cache` 적용 시 ~5s | `pip install import-linter grimp` (~10s, cache 시 ~2s) | `pip install ruff` (이미 cache 가능) | 0 (stdlib) |
| 추가 step 시간 | ~40~60s (cold) / ~10s (warm) | ~15s (cold) / ~5s (warm) | ~5s | ~2s |
| Job 전체 영향 | 5-min timeout 내 충분 | 거의 무시 가능 | 거의 무시 가능 | 거의 무시 가능 |

**CI-A 통합 명령 (T-1 의 경우)**:

```yaml
- name: Set up Node
  uses: actions/setup-node@v4
  with:
    node-version: "20"
    cache: "npm"

- name: Install dependency-cruiser
  run: npm install -g dependency-cruiser@^16

- name: depcruise — PASS path
  run: |
    set +e
    depcruise --config .depcruise.cjs --output-type err tests/fixtures/provider_adapter_enforcement/pass/
    rc=$?
    [ "$rc" -eq 0 ] || { echo "::error::PASS fixture rule violation"; exit 1; }

- name: depcruise — FAIL path (양방향)
  run: |
    set +e
    depcruise --config .depcruise.cjs --output-type err tests/fixtures/provider_adapter_enforcement/fail/
    rc=$?
    [ "$rc" -ne 0 ] || { echo "::error::FAIL fixture not blocked"; exit 1; }
```

**기술 위험**:
- `package.json` 부재 → `npm install -g` 는 작동하나 lock file 부재로 *재현 불가능한* 버전 (의존 cruiser 버전이 시간에 따라 변동). `package.json` + `package-lock.json` 추가가 사실상 강제 — **Python repo 에 Node manifest 도입 = dev-deps 영구 확장**.
- `actions/setup-node@v4` 는 stable, 비용 무시. 단 *최초 도입의 경계 비용* (manifest 파일 신설, dependabot 대상 확장, supply chain 위험 1축 추가) 이 본 PoC 의 *주된 합의 쟁점*.

### 1-7. FP/FN 방지 — Python 직접 파싱 가능?

**dependency-cruiser 의 Python 지원 사실 검증**:

- 공식 README (`github.com/sverweij/dependency-cruiser`): "**JavaScript, TypeScript, CoffeeScript, LiveScript** ... CommonJS, AMD, ES6 모듈". **Python 미명시**.
- TypeScript-Estree (Babel 호환 parser) 기반. Python `import` 구문은 ESTree AST 가 아니므로 **공식 지원 없음**.
- 비공식 plugin: `dependency-cruiser` 의 `extensions` 옵션이 `.py` 를 허용하지 않음 (`.js`, `.ts`, `.jsx`, `.tsx`, `.cjs`, `.mjs`, `.coffee`, `.litcoffee`, `.ls`, `.svelte`, `.vue` 만). `.py` 추가 시 *parser 미발견* 에러.
- 우회 방법: 전무. dependency-cruiser 를 Python 에 적용하는 *공식적/비공식 문서화된* 방법 없음.

**결론**: **T-1 은 본 repo (Python only) 에 사실상 적용 불가**. §9.3 의 `.depcruise.cjs` 명세는 *추상적 시제* (scope 문서 §0.1 자인) 였고, *Python 호환 비공식* 으로 표기된 것이 실제로는 *Python 미지원*.

이것이 본 분석의 가장 중요한 발견.

---

## 2. 도구 4 옵션 기술적 검증

### T-1: dependency-cruiser

| 항목 | 평가 |
|------|------|
| Python 지원 | **공식 미지원, 비공식 plugin 부재** (extensions whitelist 에 `.py` 없음) |
| §9.3 답습 충실성 | 명세 문법 그대로 — 단 *실 적용 불가능* |
| 도입 비용 | Node 도구체인 + `package.json` 영구 도입 + supply chain 1축 확장 |
| Transitive 추적 | ✅ (단 Python 미지원으로 무용) |
| FP/FN | Python source 미분석 → **모든 검사 결과 vacuously true** |

→ **T-1: 기술적으로 동작 불가**. §9.3 명세 답습은 *문서적 정합성* 에 불과.

### T-2: import-linter

| 항목 | 평가 |
|------|------|
| Python 호환 | ✅ 공식 (Python 3.9+, `pip install import-linter`) |
| Config 형식 | INI (`.importlinter`) 또는 TOML (`pyproject.toml`) |
| Contracts 종류 | `forbidden`, `independence`, `layers`, `forbidden_modules` (3.x+) |
| Transitive 추적 | ✅ `grimp` 그래프 라이브러리 (Python AST 기반) |
| 본 case 적합성 | `forbidden` contract 가 정확히 §9.3 의 forbidden rule 등가 |
| `ignore_imports` | facade → forbidden 5종 예외 표현 가능 |
| 빈 `src/` 동작 | `__init__.py` 1개 두면 정상. 부재 시 `ImportError` |
| 1차 PoC fixture 통합 | fixture 가 패키지 형태 (`__init__.py`) 이면 검사 가능 — 단 fixture 가 src/ 외부에 있으면 `root_packages` 미포함 → 자동 제외 → **양방향 검증 위해 별도 config 또는 검사 디렉터리 인자 명시 필요** |
| dev-dep | `pip install import-linter` (의존: grimp, click) |

**최소 config 예시**:

```ini
[importlinter]
root_package = src

[importlinter:contract:no-direct-llm-sdk]
name = Provider SDK direct import forbidden outside facade
type = forbidden
source_modules =
    src
forbidden_modules =
    litellm
    anthropic
    openai
    google.generativeai
    ollama
ignore_imports =
    src.adapters.llm.facade -> litellm
    src.adapters.llm.facade -> anthropic
    src.adapters.llm.facade -> openai
    src.adapters.llm.facade -> google.generativeai
    src.adapters.llm.facade -> ollama
```

**제약**: import-linter 는 *Python 동적 import* 미검출 (`importlib.import_module`, `__import__`). 1차 AST scanner 영역 보존.

### T-3: ruff custom rule

| 항목 | 평가 |
|------|------|
| Python 호환 | ✅ ruff 자체는 Python 코드 분석 (Rust 구현) |
| Custom rule 작성 | **현재 미지원** — ruff (≤ 0.7) 는 *내장 rule 만* 추가 가능. plugin/extension 시스템 없음 (issue #283 — 2026 기준 미해결) |
| 기존 rule 활용 | `flake8-import-restrictions` 호환 rule (TID253, TID252) — *모듈 단위 ban* 가능 단 transitive 추적 X |
| Maintenance | 내장 rule 미해당 → fork ruff (현실 불가) |

→ **T-3: custom rule 작성 = 사실상 불가능 (2026-05 기준)**. 내장 `tidy-imports` (TID) 룰로 *direct import 차단만* 가능 (1차 AST scanner 의 부분집합).

### T-4: 1차 AST scanner 확장 (transitive)

| 항목 | 평가 |
|------|------|
| 구현 가능성 | ✅ stdlib `ast` + 재귀 수집 로 가능 |
| 구현 복잡도 | 中 — 1단계 scan → 모듈 import 그래프 구축 → DFS/BFS 로 transitive reachability |
| 의존 라이브러리 | stdlib only (또는 `networkx` 옵션) |
| 동적 import 추적 | 정적 분석 한계 — 1차 와 동일하게 패턴 매칭만 |
| 유지비 | 자체 구현 코드 ~150줄 추정 (모듈 경로 resolver + 그래프 + reachability) |
| §9.3 답습 | **명시 미답습** (depcruise 어휘 사용 X — *동등 기능* 만 답습) |

**구현 스케치**:
```python
# tools/provider_import_graph.py (가)
import ast, pathlib, collections
def build_import_graph(src_root: pathlib.Path) -> dict[str, set[str]]:
    g = collections.defaultdict(set)
    for py in src_root.rglob("*.py"):
        mod = ".".join(py.relative_to(src_root.parent).with_suffix("").parts)
        tree = ast.parse(py.read_text())
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for a in node.names: g[mod].add(a.name)
            elif isinstance(node, ast.ImportFrom) and node.module:
                g[mod].add(node.module)
    return g
def reachable(g, start, target_set):
    seen, stack = set(), [start]
    while stack:
        n = stack.pop()
        if n in seen: continue
        seen.add(n)
        for d in g.get(n, ()):
            if any(d == t or d.startswith(t+".") for t in target_set): return d
            stack.append(d)
    return None
```

**제약**: 표준 라이브러리/3rd-party 모듈은 별도 install 없이 import 가 안 되므로 *grimp* (import-linter 의존) 가 동등 기능을 더 견고하게 제공. T-4 는 T-2 대비 *재발명* 위험.

---

## 3. PoC 명령 (실행 가능)

### T-1 (dependency-cruiser) — 기술적으로 *작동 불가* 예시 (참고용)

```bash
# 본 명령은 Python source 에 대해 vacuously true 결과만 반환 (확장자 매칭 실패)
mkdir -p src/adapters/llm && touch src/adapters/llm/__init__.py src/adapters/llm/facade.py
cat > package.json <<'EOF'
{ "name": "provider-adapter-enforcement", "private": true, "devDependencies": { "dependency-cruiser": "^16.0.0" } }
EOF
npm install
cat > .depcruise.cjs <<'EOF'
module.exports = {
  options: { includeOnly: "^src/", tsPreCompilationDeps: false },
  forbidden: [{
    name: "no-direct-llm-sdk",
    from: { pathNot: "^src/adapters/llm/facade\\.py$" },
    to:   { path: "^(litellm|anthropic|openai|google\\.generativeai|ollama)" }
  }]
};
EOF
npx depcruise --config .depcruise.cjs --output-type err src/
# 기대: exit 0 (vacuously, .py 미파싱)
echo "RC=$?  ← 의미 없는 PASS"
```

→ 실행해도 *안전한 PASS* 만 나오며, 실제 violation 검출 능력 없음. 본 기술 검증 목적으로만 명시.

### T-2 (import-linter) — 실제 동작 가능

```bash
cd /home/delangi/문서/project/category/AI_development_tool
mkdir -p src/adapters/llm
touch src/__init__.py src/adapters/__init__.py src/adapters/llm/__init__.py
cat > src/adapters/llm/facade.py <<'EOF'
"""Stub facade — single allow-listed entry point for LiteLLM."""
EOF

# 의존
python3 -m venv .venv-poc2 && source .venv-poc2/bin/activate
pip install --quiet import-linter grimp

# config
cat > .importlinter <<'EOF'
[importlinter]
root_package = src

[importlinter:contract:no-direct-llm-sdk]
name = Provider SDK direct import forbidden outside facade
type = forbidden
source_modules =
    src
forbidden_modules =
    litellm
    anthropic
    openai
    google.generativeai
    ollama
ignore_imports =
    src.adapters.llm.facade -> litellm
    src.adapters.llm.facade -> anthropic
    src.adapters.llm.facade -> openai
    src.adapters.llm.facade -> google.generativeai
    src.adapters.llm.facade -> ollama
EOF

# 양방향 PASS path
lint-imports --config .importlinter
# 기대: Contracts: 1 kept, 0 broken. (exit 0)

# 양방향 FAIL path — 검증을 위해 src/ 내에 의도적 위반 도입
cat > src/__forbidden_probe.py <<'EOF'
import openai  # 의도적 위반 — fixture 답습
EOF
lint-imports --config .importlinter
# 기대: 1 broken (exit 1)
rm src/__forbidden_probe.py
```

### T-3 (ruff TID — 부분 동치)

```bash
cat > pyproject.toml <<'EOF'
[tool.ruff.lint]
select = ["TID"]

[tool.ruff.lint.flake8-tidy-imports.banned-api]
"openai".msg = "Use src.adapters.llm.facade only (Provider Liquidity Layer 1)"
"anthropic".msg = "Use src.adapters.llm.facade only"
"litellm".msg = "Use src.adapters.llm.facade only"
"google.generativeai".msg = "Use src.adapters.llm.facade only"
"ollama".msg = "Use src.adapters.llm.facade only"

[tool.ruff.lint.per-file-ignores]
"src/adapters/llm/facade.py" = ["TID251"]
EOF
pip install ruff
ruff check src/
# direct import 만 검출 — transitive X, 동적 import X
```

### T-4 (AST scanner 확장)

§2 T-4 의 `build_import_graph` + `reachable` 함수 (~150 LOC) 를 `tools/provider_import_graph.py` 로 신설. 명령은 `python3 tools/provider_import_graph.py src/` — 미구현 상태로 본 분석에서는 *구현 가능성* 만 검증. 메리트: stdlib only. 단점: T-2 의 grimp 재발명.

---

## 4. 기술적 권고

### 4.1 우선순위

| 순위 | 옵션 | 이유 |
|------|------|------|
| **1순위** | **T-2 (import-linter)** | Python 호환 ✅, transitive ✅, dev-dep 1개, CI 통합 단순, 1차 AST scanner 와 *역할 분담* 명확 (T-2 = transitive 정적 / 1차 = 동적 import + 모델명 분기) |
| 2순위 | T-2 + T-4 합성 | T-2 가 grimp 로 transitive 처리, T-4 는 추가 가치 없음 → 2순위 자체가 *불필요한 중첩* |
| 3순위 | T-3 (ruff TID) | direct import 만 — 1차 scanner 의 *부분집합*. 추가 가치 0 |
| 권고 외 | **T-1 (dependency-cruiser)** | **Python 미지원 — 기술적 동작 불가** |

### 4.2 권고 근거 (기술 한정)

1. **Python 호환성** = T-1 0점 / T-2 만점 / T-3 부분 / T-4 만점.
2. **Transitive 추적** = T-2 만점 / T-4 만점 / T-1 (이론) 만점 / T-3 0점.
3. **유지비** = T-2 (1 dev-dep) < T-4 (자체 코드 +150 LOC) < T-1 (Node manifest 영구 도입) < T-3 (custom rule 미지원).
4. **§9.3 답습 충실성** = T-1 명시 답습 (단 동작 불가) > T-2/T-4 *기능 등가* 답습 > T-3 부분 답습.

기술 분석 결론: **T-2 가 유일하게 동작 + 추가 가치 (transitive) 가 명확**. §9.3 의 어휘 답습 (`depcruise`) 은 *동작하지 않는* 도구를 강제할 수 없음 → 기능 등가 도구로 대체가 필연.

### 4.3 1차 scanner 와의 역할 분담

| 검증 항목 | 1차 AST scanner | 2차 (T-2 import-linter) | 외부 (R-2/R-4.1 runtime) |
|----------|---------------|------------------------|----------------------|
| Direct import (5종) | ✅ | ✅ (중첩 — 강화) | — |
| From-import | ✅ | ✅ (중첩 — 강화) | — |
| Transitive (A→B→openai) | ❌ | **✅ (2차 신규 가치)** | — |
| 동적 import (`importlib`) | ✅ | ❌ | — |
| `__import__` | ✅ | ❌ | — |
| 모델명 분기 (문자열) | ✅ | ❌ | — |
| URL/endpoint 하드코딩 | ❌ | ❌ | grep + egress (영역 외) |
| 의미적 lock-in | ❌ | ❌ | 코드리뷰 + 라운드트립 |

→ 2차 PoC 의 *유일한 추가 가치* = **transitive 의존 차단**. 그 외는 1차 scanner 가 이미 처리.

### 4.4 대안 (만약 §9.3 어휘 답습이 절대 명령이라면)

§9.3 의 *문자 그대로* 답습 (즉 `.depcruise.cjs`) 가 정책적으로 절대 요구되면, 두 가지 보조 경로:

1. **T-1 + future migration**: src/ 가 향후 TypeScript 컴포넌트를 포함할 가능성 시점에 도입 — 그 전까지는 *미동작 시제만 등록*. (2차 PoC 가치 0)
2. **§9.3 명세 amendment**: "depcruise *또는 동등 기능 도구*" 로 어휘 갱신 + T-2 채택. → 정책 결정이므로 본 분석 영역 외.

---

## 5. 위험 (RED FLAG)

| ID | 위험 | 심각도 | 비고 |
|----|------|--------|-----|
| **RA-1** | **dependency-cruiser 가 Python 을 공식/비공식 미지원** — §9.3 명세가 *동작 불가* 도구를 명시 | **CRITICAL** | T-1 채택 시 enforcement = 0. 풀 3+1 합의의 *근본 입력* 으로 명시 필요 |
| RA-2 | `src/` 부재 상태에서 모든 도구 ENOENT — placeholder `__init__.py` 만 두는 공허 시제 | 中 | 본 PoC 자체가 future-proof 시제임을 자인하면 수용 가능 |
| RA-3 | 1차 AST scanner 의 `google` 단독 차단이 `google.protobuf` 등 합법 import 를 FP 위험 | 中 | 본 2차 PoC 외 사항 — 1차 scanner 의 사전 보강 권고 |
| RA-4 | T-2 채택 시 `pyproject.toml` 신설 필요 (현재 manifest 부재) — Python 패키징 표준 도입 = 별도 영향 | 低~中 | 단 Node manifest 도입 (T-1) 보다 본 repo 정합성 측면 비용이 적음 |
| RA-5 | T-1 의 `package.json` 도입 = supply chain 1축 영구 확장 + dependabot 대상 + npm registry 의존 | 高 | Python only repo 에 미스매치 |
| RA-6 | depcruise CI step 의 cold install ~30~60s — 5-min timeout 위협은 없으나 build 시간 증가 누적 | 低 | actions/cache 적용으로 완화 |
| RA-7 | import-linter 의 `forbidden` contract 가 `ignore_imports` 5줄을 verbose 하게 요구 — 새 forbidden 추가 시 `ignore_imports` 도 함께 갱신 누락 위험 | 低 | 검사 fixture 추가로 자동 검증 가능 |
| RA-8 | 1차 fixture 6건 중 depcruise/import-linter 검출 가능 = 2건 (direct/from-import). 양방향 검증 fail-closed 임계값 (현재 ≥5) 을 2차 도구에 그대로 적용하면 *FAIL fixture 가 통과되어 false PASS* | 中 | 2차 CI 의 임계값을 도구별 별도 산출 필요 |
| RA-9 | T-2 의 `grimp` 가 import 시 모듈 실행 (`importlib.util.find_spec`) — fixture 의 `from anthropic import Anthropic` 이 *anthropic* 미설치 환경에서 `ModuleNotFoundError` → import-linter 가 violation 으로 보고 못 할 가능성. 검증 명령 내 `pip install anthropic openai litellm google-generativeai ollama` 가 필요할 수 있음 | **CRITICAL** | 실제 PoC 명령 작성 시 사전 확인 필수. 또는 fixture 를 stub 모듈로 위장 |
| RA-10 | scope §3.2 의 `google` 단독 매치 보수성 — import-linter 의 `forbidden_modules = google.generativeai` 는 `google.protobuf` 분리 가능, 단 1차 scanner 와 *기준 불일치* 위험 | 中 | 두 도구의 forbidden 정의 동기화 필요 |

**RED FLAG 종합**: RA-1 + RA-9 가 본 분석의 핵심 발견.

- RA-1 은 §9.3 의 어휘 답습이 *기술적으로 무의미* 함을 드러냄 → 정책 합의가 어휘를 갱신하거나 도구를 바꾸어야 함.
- RA-9 는 import-linter 가 forbidden 모듈의 실 install 을 요구하는지 여부에 따라 PoC CI 비용이 달라짐 — 사전 검증 필요. 미설치 시 grimp 의 import graph 가 *external import* 를 식별하는 모드 (`include_external_packages = True`) 사용 가능 — 본 옵션이 본 PoC 의 *실작동 핵심*.

---

## 6. 본 분석의 한계

1. 본 분석은 *기술 동작 가능성* 에 한정. 정책/거버넌스 결정 (§9.3 어휘 amendment 여부, Hermes PMO 격상 함의, ADR 갱신 범위) 은 Reviewer 영역.
2. depcruise Python 비공식 plugin 부재 검증은 2026-05 기준 공식 README + extensions 목록 기반.
3. import-linter 의 grimp `include_external_packages` 옵션 실 동작은 본 PoC 명령을 CI 에서 1회 실행하여 RA-9 확정 권고.
4. 1차 AST scanner 의 `google` 단독 차단 보강 (RA-3) 은 본 2차 PoC 영역 외.

---

## 7. 결론 요약

| 결론 | 출처 |
|------|------|
| T-1 (dependency-cruiser) 는 Python 미지원으로 *기술적 동작 불가* | RA-1, §1-7 |
| T-2 (import-linter) 가 유일하게 Python 호환 + transitive 추적 + 단순 통합 | §2 T-2, §4.1 |
| T-3 (ruff) 는 custom rule 미지원 — 내장 TID 만 부분 동치 | §2 T-3 |
| T-4 (AST scanner 확장) 는 grimp 의 재발명 — T-2 대비 추가 가치 없음 | §2 T-4 |
| 2차 PoC 의 *유일한 신규 가치* = transitive 의존 차단 | §4.3 |
| §9.3 의 `.depcruise.cjs` 어휘는 *동작 불가* — 정책 합의에서 어휘 갱신 또는 도구 대체가 필연 | RA-1, §4.4 |
| 본 분석은 정책/거버넌스 결정을 *제안하지 않음* — 풀 3+1 Reviewer 영역으로 보존 | §6 |

— Agent A (구현 분석가) 분석 종료.
