# Jarvis MVP-1 Boss 추상화 Design Doc

**일자**: 2026-05-26
**유형**: Architecture Design Doc (Phase 0, (4-way) cycle 단계 (4))
**선행**: (4-way) brief v1.1 (`35e0e8c`, 588줄) + 풀 3+1 합의 (`5dcbbdb`, 267줄, APPROVE w/ COND BLOCKING 15 + R-S1~R-S4) + 기존 `src/jarvis/boss.py` 99줄 (commit `83aebad`, 2026-05-22, "feat(jarvis): MVP-1 트랙 A — Boss LLM advisory 판단 지점 (TDD)")
**scope**: 기존 `src/jarvis/boss.py` 99줄 design doc *추출* + Backend 후보 매트릭스 *신규* — **신규 코드 0건, 기존 변경 0건** (R-S1 발효 BLOCKING-1 답습 영구)

---

## 1. 본 design doc 의 자격 (R-9 + R-15 + R-S1 답습)

### 1.1 본 doc 의 목적

- (4-way) cycle 단계 (4) 결과물 = 4 차원 통합 *분석* + Boss 추상화 design doc 추출
- 기존 `src/jarvis/boss.py` 99줄 (commit `83aebad`) 의 design 의도 명문 추출
- Backend 후보 매트릭스 신규 (OllamaBoss / LlamaCppBoss / vLLMBoss + OpenAI-compatible endpoint 통일)
- Boss 신뢰 경계 명문 (R-S2 발효 답습 영구)
- (j) advisory wall-clock 측정 cycle 진입 자격 평가 input
- (k) M3·M4 결정 *고정* + (l) MVP-1 트랙 B 구현 = **별도 cycle 의무** (본 doc scope 외)

### 1.2 본 doc 의 *하지 않는 것*

1. ❌ **신규 코드 작성** (`src/jarvis/boss/` 디렉토리 0건 + 신규 Backend class 0건)
2. ❌ **기존 `src/jarvis/boss.py` 99줄 변경** (commit `83aebad` 답습 영구)
3. ❌ **테스트 작성** (`tests/jarvis/test_boss_advisory.py` 변경 0건)
4. ❌ **M3·M4 결정 *고정*** ((k) 별도 cycle)
5. ❌ **advisory wall-clock 측정** ((j) 별도 cycle)
6. ❌ **MVP-1 트랙 B 실제 구현** ((l) 별도 cycle)
7. ❌ **vLLM 부분 정정** (line 126 verbatim 보존 영구)
8. ❌ **헌법 / ADR-011 / 다른 ADR / 다른 문서 본문 변경** (R-9 답습 영구)

---

## 2. BossLLM Protocol — 기존 `src/jarvis/boss.py:24~98` verbatim 인용

### 2.1 AdviceRequest (boss.py:24~35 verbatim)

```python
@dataclass(frozen=True)
class AdviceRequest:
    """Boss 가 검토할 입력 — 모두 untrusted(워커 출력 포함, prompt injection 표적).

    Boss 는 이 입력으로 *텍스트만* 생성한다. 실행·게이트 통과·workdir·argv 에
    대한 어떤 제어 정보도 여기서 도출되지 않는다(§5 신뢰 경계).
    """

    prompt: str
    worker_alias: str
    output: str
    deterministic_flags: list[str] = field(default_factory=list)
```

**필드 4개**: prompt / worker_alias / output / deterministic_flags
**신뢰 경계**: 모든 필드 = **untrusted** (워커 출력 포함, prompt injection 표적)
**Boss 권한**: 텍스트 생성 only, 실행·게이트 통과·workdir·argv 도출 0건

### 2.2 BossAdvice (boss.py:38~50 verbatim)

```python
@dataclass(frozen=True)
class BossAdvice:
    """Boss advisory 결과 — *텍스트 전용*(R2). 제어 흐름 필드 금지.

    - summary: 사람에게 보여줄 자연어 검토 요약(표시용 — 게이트 결정에 자동 반영 0).
    - extra_flags: 결정적 flag 에 *추가*할 위험 태그(union, 감산 불가 = R1 fail-safe).
    - advisory_failed: advisory 가 실패(누락)했는지 표지(R3 명시 경고용 *상태* — 게이트
      통과를 좌우하지 않는 표시 메타데이터). confidence 없음(R6).
    """

    summary: str
    extra_flags: list[str] = field(default_factory=list)
    advisory_failed: bool = False
```

**필드 3개**: summary / extra_flags / advisory_failed (frozen dataclass)
**금지 필드** (R2 답습):
- 콜백 (callbacks/hooks)
- 경로 (paths/file references)
- 명령 (commands/argv)
**금지 필드** (R6 답습):
- **confidence** (LLM 자기보고 = 거짓 안전감 차단)

### 2.3 BossLLM Protocol (boss.py:53~64 verbatim)

```python
@runtime_checkable
class BossLLM(Protocol):
    """로컬 사장 추상 — provider 교체 단위(헌법 5조). 순수 추론(부작용 0).

    name = 교체 키. advise() = MVP-1 유일 판단 지점(결과 검토). 실패 시 예외를
    던질 수 있다(R3: 호출측이 누락→경고로 처리).
    """

    name: str

    def advise(self, req: AdviceRequest) -> BossAdvice:
        ...
```

**추상화 형태**: `@runtime_checkable Protocol` (ABC 아님 — duck typing, 외부 class 정의 자유)
**method**: `advise(req: AdviceRequest) -> BossAdvice` (단일 판단 지점)
**health_check**: 현재 미존재 → (k) 별도 cycle 결정 후보

### 2.4 merge_flags (boss.py:92~98 verbatim)

```python
def merge_flags(deterministic: list[str], extra: list[str]) -> list[str]:
    """결정적 flag ∪ advisory flag — *추가만*, 감산 불가(R1 fail-safe 불변식).

    결정적 flag 는 전부 보존되고, extra 중 새것만 뒤에 덧붙는다(중복 없음).
    advisory 가 결정적 flag 를 줄이는 경로는 구조적으로 존재하지 않는다.
    """
    return [*deterministic, *(f for f in extra if f not in deterministic)]
```

**R1 fail-safe 불변식**: 결정적 flag 합집합 강제, 감산 구조적 불가
**의미적 green washing 차단 한계**: 기계적 flag 감산만 차단, 의미적 우회 (summary 오도) 못 막음 → 3중 방어 (결정적 flag 분리 표시 + raw diff 직접 확인 + ReviewGuard 권위, R1 답습)

### 2.5 StubBoss (boss.py:67~89 verbatim)

```python
class StubBoss:
    """결정적 테스트용 Boss — scripted advice 반환(트랙 A, 실 호출 0).

    fail=True 면 advise 가 예외(endpoint timeout/다운 모사) → R3 경로 검증.
    calls 로 호출 여부 관찰(R8: 워커 실패 시 미호출 확인).
    """
    # ... (생략, boss.py:74~89)
```

**용도**: TDD 트랙 A (실 호출 0, V-1 무관)
**R3 검증**: `fail=True` 시 `RuntimeError("boss endpoint 실패(모사)")` — 호출측 누락→경고 변환 검증
**R8 검증**: `calls` 리스트 — 워커 실패 시 advise 미호출 여부 관찰

---

## 3. Boss 신뢰 경계 (R-S2 발효 + BLOCKING-5 흡수, 4-way 합의)

### 3.1 Boss 입력 신뢰 경계 (R10 + R8 답습)

**AdviceRequest 모든 필드 = untrusted**:
- `prompt`: 사용자 프롬프트 — prompt injection 표적
- `worker_alias`: 워커 식별자 — 가짜 워커 사칭 risk
- `output`: 워커 stdout — **prompt injection 직접 표면** (워커 자체 침해 시 Boss advisory 침해 자격 = injection 표면 확장)
- `deterministic_flags`: 결정적 flag 리스트 — Boss 가 *읽기* 만 (Boss 가 줄이는 경로 0건, R1 fail-safe)

### 3.2 Boss 출력 신뢰 경계 (R2 답습)

**BossAdvice = 텍스트 전용 frozen dataclass**:
- 콜백·경로·명령 필드 **금지** (R2 답습 — 산문이 아니라 데이터 모델 제약으로 강제)
- 실행·게이트 통과·workdir·argv 도출 **0건** (boss.py:28~29 docstring verbatim)
- `summary` = 표시용 only, 게이트 결정에 자동 반영 **0건** (boss.py:42 verbatim)
- `extra_flags` = 결정적 flag 에 *추가*만 (union, 감산 불가, R1 fail-safe)
- `confidence` 필드 **0건** (R6 답습 — LLM 자기보고 = 거짓 안전감 차단)

### 3.3 Boss = root of trust 아님 (ADR-011 §2.1 + MVP-1 brief v2 §5 답습)

**게이트 결정 권위**:
- 결정적 flag (정적 분석, lint, type check, test)
- raw diff (사람 직접 확인 의무)
- ReviewGuard 권위 (보안 검토)

**BossAdvice.summary 종속 금지** (R10 답습):
- 사람 게이트 = 결정적 flag + raw diff 직접 확인 의무
- Boss summary 만 보고 결정 0건
- `output_preview[:200]` Boss summary 종속 위험 회피

**의미적 green washing 방어 (R1 답습)** — 3중 방어:
1. 결정적 flag 분리 표시 (Boss 가 줄이는 경로 0건, merge_flags fail-safe)
2. raw diff 직접 확인 (사람 의무, Boss summary 우회)
3. ReviewGuard 권위 (보안 검토 별개 layer)

**한계 정직성**: 기계적 flag 감산만 차단, 의미적 우회 (summary 오도) 못 막음 (boss.py:9~11 docstring verbatim)

### 3.4 워커 실패 시 advise 미호출 (R8 답습, BLOCKING-6 흡수)

**원칙**: `result.is_error` 면 BossLLM.advise 호출 **0건**
**근거**: 실패 출력 = 침해된 워커 advisory injection 표면 확장 risk + LLM 비용/지연 낭비
**검증**: `StubBoss.calls` 답습 verify (boss.py:71/83 — 호출 여부 관찰)
**위치**: `orchestrator.py` early-return (advise 호출 *전* `result.is_error` 검사)

### 3.5 advisory failure ≠ health_check failure 분리 (BLOCKING-8 흡수)

| 실패 유형 | 거동 | 답습 |
|---|---|---|
| **advise 실패** (timeout/다운/비정상) | **fail-open** — 게이트 진행 (비차단) + 사람에게 "Boss advisory 실패" 명시 경고 | R3 답습 (boss.py:12~13 verbatim) |
| **merge_flags** (결정적 flag 합집합) | **fail-safe** — 감산 구조적 불가 (R1 답습) | merge_flags 답습 |
| **health_check 실패** (현재 boss.py 미존재) | (k) 별도 cycle 결정 후보 | 본 doc scope 외 |

⚠️ "**fail-closed 정신**" 표현 부정확 (BLOCKING-8) — R3 = fail-open + R1 = fail-safe 분리 명문, "fail-closed" 단어 삭제

---

## 4. Backend 후보 매트릭스 (4-way 측정 evidence + OpenAI-compatible endpoint 통일)

### 4.1 후보 매트릭스 (BLOCKING-7 + BLOCKING-11 흡수)

| backend | 측정 t/s (decode gen) | OpenAI-compatible endpoint | 우선순위 | MVP-2 재검토 trigger | 비고 |
|---|---|---|---|---|---|
| **LlamaCppBoss** | 49.6 (Qwen3-30B-A3B classical, bartowski direct, **N=1 정직성**) | `http://localhost:8080/v1/chat/completions` (llama-server) ✓ | ⭐⭐⭐ MVP-1 우선 | N/A (MVP-1 채택) | 빠름 / N=3 분산 검증 carry-over MEDIUM ((h)' REC-3 신규) |
| **OllamaBoss** | 14.69~15.29 (qwen3:30b-a3b-instruct-2507-q4_K_M) | `http://localhost:11434/v1/chat/completions` (Ollama OpenAI mode) ✓ | ⭐⭐ MVP-1 보조 | N/A (MVP-1 채택) | Provider Liquidity 보조 + Modelfile 호환 + Phase 1 N=3 carry-over MEDIUM |
| **vLLMBoss** | (MVP-1 비채택) | `/v1/chat/completions` (vLLM OpenAI mode) ✓ | MVP-2 재검토 | **vLLM 공식 sm_121 native support release + DGX Spark binary wheel 제공 + sm_121f SCALED_MM_ARCHS 포함 시** | **영구 배제 금지 (line 126 답습 영구, C-2 충돌 회피)** |

### 4.2 OpenAI-compatible 통일 자격 (BLOCKING-7, Provider Liquidity 직접 실현)

**3 backend 모두 OpenAI-compatible `/v1/chat/completions` 지원 confirmed**:
- llama-server 2026 release: `/v1/chat/completions` ✓ + Prefix caching + Tensor parallelism + SvelteKit web UI
- Ollama 공식 docs: `http://localhost:11434/v1/chat/completions` ✓ (OpenAI SDK 호환)
- vLLM OpenAI mode: `/v1/chat/completions` ✓

→ **BossLLM Protocol 내부 = HTTPClient + base_url 만 차이, Provider Liquidity 직접 입증** ⭐⭐⭐

**httpx 표준 클라이언트** (boss.py:15 verbatim "트랙 B 에서 httpx/OpenAI-호환"):
- 외부 LLM SDK 0건 (외부 의존 최소화)
- worker.py 원칙 동형 답습 (REC-2 cousin)

**추상화 layer 매우 얇음 자격** = 헌법 5조-2 비협상 직접 실현

### 4.3 vLLMBoss MVP-2 재검토 trigger 명문 (BLOCKING-11, 외부 evidence 답습)

**현재 (2026-05-26) 외부 상황**:
- vllm Issue #36821: "No sm_121 (Blackwell) support on aarch64"
- vllm Issue #31128: "vLLM 0.17 sm_121 일부 fix BUT SCALED_MM_ARCHS 미포함"
- PyTorch binary sm_120 까지만 compile
- Workaround: sm_120 forward compat (실동작 보고 only, 본 cycle 실측 0건)

**MVP-2 재검토 trigger (vLLMBoss 채택 자격 발효 조건)**:
1. vLLM 공식 sm_121 native support release
2. DGX Spark binary wheel 제공
3. sm_121f SCALED_MM_ARCHS 포함

**영구 배제 금지** (MVP-1 brief line 126 verbatim 답습 영구):
- "vLLM = "제외" → "MVP-1 비채택, MVP-2 재검토"로 강등. 근거: 2026 기준 sm_120/121 binary-compat 으로 실동작 보고 + vLLM 0.17 해소 흐름(MXFP4 gpt-oss-120B ~56 tok/s 최고속). **영구 배제는 C-2(런타임도 교체 가능)와 충돌** → 문서에서 영구 못 박지 않음."

---

## 5. LiteLLM 4 후보 대안 architecture 매트릭스 (REC-5 footnote, MVP-1 결정 *후보* only)

본 §5 = 외부 evidence 답습 footnote. 본 doc 결정 0건 = **(k) M3·M4 결정 *고정* cycle carry-over input only**.

### 5.1 4 후보 매트릭스

| # | 후보 architecture | 의존성 | Provider Liquidity | DGX Spark 적합도 | MVP-1 결정 자격 |
|---|---|---|---|---|---|
| A | **BossLLM Protocol 직접** (현재 boss.py:54) | 0건 | 코드 의존 (실현) | ⭐⭐ | ⭐⭐⭐ (기존 구현 + 외부 의존 0) |
| B | **LiteLLM 게이트웨이** | LiteLLM | config 의존 (자격 매우 강) | ⭐⭐⭐ | (k) carry-over, **LiteLLM lock-in 우려 정직성** (NOTE-7) |
| C | **Hybrid** (BossLLM 얇은 wrapper + LiteLLM 내부 client) | LiteLLM | 양쪽 자격 | ⭐⭐⭐ | (k) carry-over |
| D | **BossLLM + llama-swap** (NVIDIA DGX Spark GB10 stack 답습, 2026-05) | llama-swap (Go) | config + 자동 model swap | ⭐⭐⭐ (GB10 production stack 표준) | (k) carry-over |

### 5.2 외부 evidence 답습 (NOTE-6/NOTE-7 정직성)

**NVIDIA Developer Forum 2026-05** (DGX Spark GB10 production stack):
- `Client → LiteLLM (OpenAI-compatible gateway) → llama-swap (model swap) → vLLM/llama.cpp/Ollama`
- 본 project HW (GB10/121GB) 와 동일 — architecture 후보 답습 자격 매우 높음

**LiteLLM lock-in 우려 정직성** (NOTE-7):
- LiteLLM 자체 의존 (라이센스 / 유지보수 / API 안정성)
- 본 cycle = design doc *추출* + Backend 후보 매트릭스 only
- (k) 결정 *고정* 자격 0건 (R-9 답습 영구)

### 5.3 추가 backend 후보 (LOW carry-over, NOTE-6)

- **exllamav2** (~70 t/s+ Ampere/Ada 대형 모델 typical)
- **TabbyAPI** (exllamav2 OpenAI-compatible front)
- **KoboldCpp** (llama.cpp 기반, OpenAI-compatible)
- **MLX** (Apple Silicon, GB10 무관 but 향후 ARM Mac 대비)
- **Triton / TensorRT-LLM** (sm_121 추가 검증 의무, MVP-2 carry-over)

---

## 6. 보안 의무 (M6 + R11 답습 영구, BLOCKING-4 흡수)

### 6.1 localhost 127.0.0.1 바인딩 의무

- OllamaBoss / LlamaCppBoss endpoint = **127.0.0.1 localhost 한정** (외부 노출 금지)
- vLLMBoss (MVP-2) = 동일 의무 (영구 답습)
- 헌법 8조 (보안) + M6 답습

### 6.2 egress 0 의무

- **추론 시점 egress 0** (R11 답습)
- 단 설치 / 모델 pull / 텔레메트리는 별개 (egress 자연 변동)
- (j) 측정 cycle 에서 실측 확인 의무

### 6.3 외부 LLM SDK 미import

- boss.py:15 verbatim: "본 모듈은 외부 LLM SDK 를 직접 import 하지 않는다(트랙 B 에서 httpx/OpenAI-호환)"
- httpx 표준 클라이언트 only (외부 의존 최소화)

---

## 7. (j) advisory wall-clock 측정 cycle 진입 자격 (BLOCKING-9 + BLOCKING-10 + BLOCKING-15 + R-S4 흡수)

### 7.1 wall-clock = decode + prefill 합산 의무 (BLOCKING-9)

- decode generation 만 = 정의 부정확
- prefill processing 격차 (Ollama (h-O)/(h-OM) ~3.65~3.77× outlier) 답습 의무
- (R4-body) M3 매트릭스 4 차원 격차 답습

### 7.2 threshold 후보 매트릭스 (BLOCKING-10, T1~T6 다중 후보, 본 cycle 결정 0건)

| # | threshold | 보수성 | Ollama 통과 | llama.cpp 통과 | false positive risk | false negative risk |
|---|---|---|---|---|---|---|
| T1 | ~10 t/s | 매우 보수 | ✓ | ✓ (5×) | 高 | 매우 낮음 |
| T2 | ~15 t/s (R5 권고) | 표준 | 경계 (-2% ~ +2% 진동) | ✓ (3.3×) | 中 | 低 |
| T3 | ~20 t/s | 적정 | ✗ | ✓ (2.5×) | 低 | 中 |
| T4 | ~30 t/s | 공격 | ✗ | ✓ (1.65×) | 매우 낮음 | 高 |
| T5 | 동적 (latency budget × context length) | N/A | 조건부 | 조건부 | 低 | 低 |
| T6 | 다중 tier (short ~30 / mid ~20 / long ~15) | 절충 | short context ✗ | ✓ | 低 | 低 |

→ **(j) 별도 cycle 측정 후 결정 *후보* only (본 doc 결정 0건)**

### 7.3 prefill 입력 상한 + 요약 후보 (REC-4 흡수, 외부 evidence 2026)

| 입력 상한 | 요약 방법 | 트레이드오프 |
|---|---|---|
| ~512 tokens | TextRank | 빠름 + 의미 손실 가능 |
| ~1024 tokens | LLM summary | 정확 + latency 비용 |
| ~2048 tokens | Sliding window | 균형 + cache 효과 |
| ~4096 tokens | Hybrid (TextRank → LLM 요약) | 최선 BUT 복잡도 (외부 evidence "Hybrid 접근 production 표준") |

### 7.4 (j) 진입 선결 cycle carry-over 4 의무 (BLOCKING-15 + R-S4)

- Phase 1 N=3 repetitions Ollama 답습 MEDIUM (Ollama 분산 검증 필수)
- **(h)' LlamaCppBoss bartowski direct N=3 별도 측정 cycle MEDIUM (REC-3 신규)** — (h) 단일 측정 49.6 t/s 분산 미확인
- Ollama embedded llama.cpp version verify MEDIUM (변수 분리)
- (h-OL) llama.cpp Ollama library blob 직접 측정 MEDIUM (5-way confirm)
- Ollama prefill processing framework overhead 검증 MEDIUM (F-4 (h-OM) 답습)

### 7.5 (j)→(k)→(l) cycle chain 명시 (REC-2 흡수)

```
(j) advisory wall-clock 측정 (별도 cycle)
  └→ (k) M3·M4 결정 *고정* (별도 cycle)
       └→ (l) MVP-1 트랙 B 구현 (OllamaBoss/LlamaCppBoss 실제 Backend class 코드)
```

→ **현재 본 doc = (j) 진입 자격 *평가* only, 측정/결정/구현 모두 별도 cycle**

---

## 8. 4 차원 통합 분석 결과 종합 (R4 + F2 + Provider Liquidity + (j))

### 8.1 R4 차원 결론

- (R4-body) Edit 4건 결과 = "llama.cpp > Ollama 확정" framing 확립 + line 126 vLLM verbatim 보존
- R4 referent 보존 = **4 위치** (BLOCKING-14 + R-S3 산술 정합)
- 본 cycle 분석 = R4 정정 *후속* 일관성 확정 ✓
- 추가 cascade 검토 = LOW carry-over (별도 cycle)

### 8.2 F2 차원 결론

- (g) Qwen3-Next-80B SSM 32.3 vs (h) Qwen3-30B-A3B classical 49.6 = ~1.54× (N=1 정직성)
- classical MoE > SSM hybrid 모든 차원 빠름 (S2 강화 시나리오 일부)
- 미해소 변수 3개 (model size + expert routing + 도구 version) — *간접* input only (N-7 답습)
- **(m) F2 model size 단독 분리 cycle MEDIUM (REC-1 신규)** carry-over

### 8.3 Provider Liquidity 차원 결론

- BossLLM Protocol (boss.py:54, commit `83aebad`) = 기존 구현 design doc 추출 완료
- Backend 후보 매트릭스 (LlamaCppBoss ⭐⭐⭐ MVP-1 우선 / OllamaBoss ⭐⭐ MVP-1 보조 / vLLMBoss MVP-2 재검토)
- OpenAI-compatible `/v1/chat/completions` 통일 → Provider Liquidity 직접 입증
- Boss 신뢰 경계 명문 (R-S2 발효): Boss 입력 untrusted + Boss = root of trust 아님 + 3중 방어
- 헌법 5조-2 비협상 답습 영구

### 8.4 (j) 차원 결론

- LlamaCppBoss 우선 + Phase 1 N=3 + (h)' N=3 verify 후 → (j) 진입 자격 충족 가능
- wall-clock = decode + prefill 합산 의무 (BLOCKING-9)
- threshold 후보 T1~T6 다중 매트릭스, 본 cycle 결정 0건 (BLOCKING-10)
- 선결 cycle carry-over MEDIUM 4건 모두 (j) 진입 *전* 충족 의무

---

## 9. carry-over 매트릭스 (자동 진입 0건, 사용자 명시 의무 답습 영구)

| 후보 cycle | 우선순위 | 비고 |
|---|---|---|
| **(R4-body) 완료 후 cascade 검토 cycle** | LOW ⭐ | R-10 발효 정직성 #19 + R-S3 발효 본 cycle 답습 cascade (R4 referent "5 위치" 산술 자기모순 정정) |
| **vLLM verify cycle** | LOW ⭐ | R-9 답습 영구 R4 본문 vLLM 부분 evidence |
| **(h)' LlamaCppBoss bartowski direct N=3 별도 측정** | MEDIUM ⭐⭐ | REC-3 신규, (h) 단일 측정 분산 미확인 |
| **(h-OL) llama.cpp Ollama library blob 직접 측정** | MEDIUM ⭐⭐ | (h-O)/(h-OM) R-15 답습, 5-way confirm |
| **Phase 1 N=3 repetitions Ollama 답습** | MEDIUM ⭐⭐ | C-S2 답습 + (j) 선결 의무 |
| **Ollama embedded llama.cpp version verify** | MEDIUM ⭐⭐ | (h-O) R-S4 답습 + 변수 분리 |
| **Ollama prefill processing framework overhead 검증** | MEDIUM ⭐⭐ | F-4 (h-OM) 답습 |
| **(m) F2 model size 단독 분리 cycle** | MEDIUM ⭐⭐ | REC-1 신규, F2 미해소 변수 분리 |
| **(j) advisory wall-clock 측정** | MEDIUM ⭐⭐ | 본 cycle = 진입 자격 평가 only, 측정 별도 |
| **(k) M3·M4 결정 *고정*** | DEFER | 변수 분리 input 강화 후 |
| **(l) MVP-1 트랙 B 구현** | DEFER | (k) 통과 후, OllamaBoss/LlamaCppBoss 실제 Backend class 코드 |
| **`llama-bench` carry-over** | MEDIUM ⭐⭐ | (g)/(h)/(h-O)/(h-OM) 답습 |
| 추가 quant / 외부 benchmark / 통합 본문 정정 / (n) 등 | LOW/DEFER | by-reference |
| **(g1-N-3-adr-008+sip+adr-012'') + (h-X) + (h-O-X) + (h-OM-X) + (R4-evidence-X) + (R4-body-X) + (4-way-X) prime/super-prime** | ❌ **자동 진입 명백 부정** | chain 영구 종결 의무 답습 영구 |

---

## 10. 답습 영구 권위

- ⭐⭐⭐ **본 design doc = 기존 `src/jarvis/boss.py` 99줄 (commit `83aebad`) design doc *추출* + Backend 후보 매트릭스 *신규* only** (신규 코드 0건, 기존 변경 0건, R-S1 발효 답습 영구)
- ⭐⭐⭐ **Boss 신뢰 경계 명문 (R-S2 발효)** = Boss 입력 untrusted + Boss = root of trust 아님 + R8 워커 실패 advise 미호출 + 3중 방어
- ⭐⭐ **OpenAI-compatible `/v1/chat/completions` endpoint 통일** = Provider Liquidity 직접 입증 (헌법 5조-2 비협상 답습 영구)
- ⭐⭐ **BossAdvice frozen + confidence 0건 (R6) + 콜백·경로·명령 필드 금지 (R2)** 답습 영구
- ⭐⭐ **R3 fail-open + R1 fail-safe + health_check (k) 별도 분리** (BLOCKING-8 답습)
- ⭐ **threshold T1~T6 다중 후보 매트릭스** (본 doc 결정 0건, (j) 별도 cycle 의존)
- ⭐ **(j)→(k)→(l) cycle chain 명시** (REC-2 답습)
- ⭐ **LiteLLM 4 후보 architecture footnote** (REC-5 답습, MVP-1 결정 *후보* only, lock-in 우려 정직성 NOTE-7)
- ⭐ **본 doc 자체 머신 변경 0건** (측정/Modelfile/ollama/sudo/실제 코드 0)
- ⭐ **(4-way-X) prime/super-prime 자동 진입 명백 부정 답습 영구**

---

## 11. 답습 정합성 verify

| 답습 패턴 | verify 결과 |
|---|---|
| R-9 답습 영구 (헌법/ADR/다른 문서 본문 변경 0건) | ✓ 본 doc 자체 = 신규 architecture doc, 헌법 5조-2 + ADR-011 §2.1 (a)~(e) 본문 변경 0건 |
| R-15 self-consistency 영구 (§1.2 ↔ 본 doc scope 1:1 매핑) | ✓ §1.2 *하지 않는 것* 8 항목 ↔ 본 doc scope 외 8 카테고리 정합 |
| R-S1 발효 (boss.py:24~98 verbatim 인용) | ✓ §2.1~§2.5 verbatim 인용 완료 |
| R-S2 발효 (Boss 신뢰 경계 명문) | ✓ §3 신규 신뢰 경계 절 완비 |
| R-S3 발효 (R4 referent 4 위치 산술 정합) | ✓ §8.1 결론 답습 |
| R-S4 발효 ((j) 진입 선결 의무 강화) | ✓ §7.4 carry-over 4 의무 명문 |
| chain 영구 종결 의무 답습 영구 ((4-way-X) prime/super-prime 자동 진입 명백 부정) | ✓ §9 carry-over 매트릭스 + §10 권위 |
| 헌법 5조-2 (Provider Liquidity 비협상) 답습 정합 | ✓ §4.2 OpenAI-compatible 통일 자격 직접 입증 |
| 헌법 8조 (보안) 답습 정합 | ✓ §6 보안 의무 + §3 Boss 신뢰 경계 |
| ADR-011 §2.1 5조건 (a)~(e) 답습 정합 | ✓ §3.3 Boss = root of trust 아님 + §1.2 본 doc scope 외 명문 |
| line 126 vLLM verbatim 보존 답습 영구 | ✓ §4.3 vLLMBoss MVP-2 재검토 trigger + 영구 배제 금지 (line 126 verbatim 답습) |
| password literal redact (R-S2 발효 영구) | ✓ 본 doc literal pattern 직접 사용 0건 (grep verify 통과) |

---

**본 design doc 종결** ((4-way) cycle 단계 (4) 결과물 = 기존 `src/jarvis/boss.py` 99줄 design doc 추출 + Backend 후보 매트릭스 신규 + Boss 신뢰 경계 명문 + (j) 진입 자격 평가 + carry-over 매트릭스. 신규 코드 0건, 기존 변경 0건. 다음 cycle 진입 = 사용자 명시 의무 답습 영구.)
