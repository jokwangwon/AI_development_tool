# Jarvis MVP-1 format 가족별 분류 합의 cycle entry brief (v1)

> **본 brief = Provider Liquidity deep-dive 합의 cycle (`a9e1e88`, BLOCKING 13 + 권고 17 + NOTE 12) 의 권고 R-26 (C-R2) 답습 후속 cycle entry brief.** v1 = 합의 진입 *전* 사용자 alignment 산출. 본 brief 의 어떤 §도 그 자체로 **코드 작성·런타임 변경·모델 다운로드·측정 실행·config 변경·M3/M4 결정 *고정*·MVP-1 합의 본문 자동 정정·헌법 본문 자동 정정·ADR-011 amendment 자동 발의·메모리 자동 갱신·Provider Liquidity 본질 약화** 를 발생시키지 않는다. 실 변경 0건. staged: **brief v1 (본 문서)** → 사용자 검토 → 풀 3+1 합의 진입 명시 → 합의 → brief v1.1 보강 → 세션 정리·commit·push. 자동 다음 단계 진입 0건.

**작성일**: 2026-05-24 (Provider Liquidity deep-dive cycle `8ae1ab6` 후속)
**카테고리**: 합의 cycle entry brief v1 (Provider Liquidity 합의 R-26 답습 후속, format 가족 분류 자격 평가)
**범위 (사용자 명시 — "(f-K) format 가족별 분류" 선택)**: **4 format 가족 분류 자체의 자격 평가 + 가족 내부/가족 간 Provider Liquidity 충족 자격 분리 가능성 평가** / **진단 + 권고 옵션 매트릭스** (결정 *고정* 0건, 사용자 명시 의무 유지)
**합의 답습** (R-22 의무):
- Provider Liquidity 합의 BLOCKING 13 의 **R-3 (4 수준 framing self-citation + 시간축 missing dimension + 비교 자격 1/4) + R-7 (model loading 5 sub-차원 분해) + R-11 (evidence GGUF 가족 한정 명문) + R-12 (cycle-specific framing 영구화 risk) + R-13 (ADR-011 line 6/245 관용 매핑 권위) + R-21 (Reviewer 권한 한계) + R-26 (format 가족별 분류) + R-29 (de facto 압력 차단) + R-30 (기각 자격 명시)** 답습 의무
- Phase 3 합의 BLOCKING 7 의 **R-3 (window bias) + R-4 (분기점 라벨 anchor effect) + R-6 (PASS/FAIL framing 금지)** 답습 패턴 유지

**선행 답습**:
- `docs/phase0/jarvis-mvp1-provider-liquidity-deepdive-consensus-entry-brief.md` (Provider Liquidity brief v1.1, `8ae1ab6`, 518줄) — 본 cycle 의 *직접* 진입 근거
- `docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-provider-liquidity-deepdive.md` (Provider Liquidity 합의, `a9e1e88`, BLOCKING 13 + 권고 17 + NOTE 12)
- `docs/phase0/jarvis-mvp1-local-boss-design-brief.md` (MVP-1 design v2, `15beb33`, C-2 + R4 + M3)
- `docs/review/3plus1-consensus-2026-05-22-jarvis-mvp1-local-boss.md` (MVP-1 합의, R4 llama.cpp ↔ Ollama 동급)
- `docs/phase0/jarvis-mvp1-v1-poc-phase3-entry-brief.md` (Phase 3 entry v1.1, `25eb008`)
- `docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-v1-poc-phase3-entry.md` (Phase 3 합의 BLOCKING 7)
- `docs/phase0/v1-poc-raw/phase3/2026-05-24T04-36-phase3-summary.json` (Phase 3 실 빌드 cycle summary)
- `docs/phase0/v1-poc-raw/phase3/2026-05-24T04-32-phase3-measure-attempt-blocked.log` (GGUF format 호환성 차단 raw)
- `docs/decisions/ADR-011-means-vs-ends-redaction.md` (§2.1 means/ends 일반 원칙 + **line 6 + line 245 verbatim "헌법 제5조 (Provider Liquidity)" / "제5조 관용 (Provider Liquidity, 비협상)" 권위 매핑** — R-13 답습 본질)
- `docs/constitution/PROJECT_CONSTITUTION.md` (제5조 코드 품질 본문 + 제8-2조 환경 관리 / 하드코딩 제로 모델명)
- 메모리: `feedback_provider_liquidity` (하드 요구, 19일+ stale system reminder verify) / `project_jarvis_local_boss_direction` / `feedback_staged_consensus_workflow` / `feedback_proportionate_security_personal_tool` / `project_minimize_user_intervention`

---

## 0. 본 brief 가 *하는* 것 / *하지 않는* 것

### 하는 것

1. Provider Liquidity 합의 R-26 답습 — 4 format 가족 분류 자체의 자격 평가 (§2)
2. **각 가족 내부 호환성 자격 (runtime 간 format 호환성)** vs **가족 간 호환성 자격 (format 변환 의무 강도)** 분리 가능성 평가 (§4)
3. **Provider Liquidity 충족 자격이 가족 내부 vs 가족 간 분리 가능한가** 의 자격 평가 (R-11 답습 응용)
4. MVP-1 R4 "동급" 진술의 가족 한정 자격 (R-3 + R-11 + R-7 답습)
5. SDD 정합성 매트릭스 — 헌법 5조 + ADR-011 line 6/245 관용 매핑 권위 답습 (R-13) + MVP-1 합의 R4 + 메모리 (§3)
6. 핵심 긴장 **5축** 분석 (§4) — (1) 가족 내부 호환성 / (2) 가족 간 호환성 / (3) Provider Liquidity 분리 자격 / (4) 시간축 (Provider Liquidity 합의 R-3 답습) / (5) **본 framing 임시성 명문** (R-3 + R-12 답습)
7. 3+1 합의 분담안 — Agent A/B/C 관점·핵심 질문·출력 형식 (§5)
8. 합의 출력 형식 명문 + raw json/log line-level cross-check 의무 (§6)
9. 후속 결정 권고 옵션 매트릭스 (§7) — **권고 자격 only, 결정 *고정* 0**. 4 가족 분류 자체의 영구 framing 자격 0 (R-12 답습 — (D3)(D4) 분기 패턴 답습)
10. 정직성 한계 (§8) — 15+ 항목
11. 차단 조건 (§9)
12. NOTE carry-over (§10) — Provider Liquidity 합의 NOTE 12 + 본 cycle 신규
13. **변경 일람 표** (§11) v1 → v1.1 (합의 후 보강 시 사용)

### 하지 않는 것 (영구 답습, R-29 + R-30 명문 답습)

- ❌ **4 가족 분류 자체의 결정 *고정*** — 본 cycle = 분류 자격 *평가* only, 분류 채택·기각·확장 = 합의 *후* 사용자 명시 의무
- ❌ **MVP-1 합의 본문 (`3plus1-consensus-2026-05-22-jarvis-mvp1-local-boss.md`) 자동 정정** — R4·C-2 진술의 검증 자격 평가 *입력* 자격만, 본문 수정은 합의 *후* 별도 cycle (R-21 답습)
- ❌ **헌법 본문 자동 정정** — 5조·8-2조·ADR-011 line 6/245 권위 답습 명문만, 헌법 amendment 는 별도 단계
- ❌ **ADR-011 amendment 자동 발의** — §2.1 적용 자격 평가만, amendment 발의 = 본 cycle 명시 권고 *후* 사용자 명시 승인 *후* 별도 합의 cycle (R-9 헌법급 변경 답습)
- ❌ **M3 (추론 런타임) / M4 (tok/s threshold) 결정 *고정*** — Phase 1+2+3 evidence 정직성 한계 답습
- ❌ **OllamaBoss·LlamaCppBoss·vLLMBoss·TensorRTLLMBoss·기타 runtime backend 코드 작성** — 본 cycle = framing 합의 입력 deep-dive
- ❌ **새 측정 실행 / 새 빌드 / 새 모델 다운로드 / 새 runtime 설치** — 본 cycle 시작 evidence = Phase 3 cycle + Provider Liquidity 합의 + 외부 식별 (추정 한정)
- ❌ **메모리 `feedback_provider_liquidity` 본문 자동 정정** — 본 cycle 합의 결과가 메모리 갱신 자격을 가질 수 있으나, 자동 갱신 0건
- ❌ **Provider Liquidity 자체 약화** — 5 영구 핵심 제약 답습. binary 본질 (락인 0) 유지, spectrum 화는 framing 도구 한정 (Provider Liquidity 합의 R-10 답습)
- ❌ **본 4 가족 분류의 영구 framing 정착** (R-12 답습) — cycle-specific framing 영구화 risk 차단. 4 가족 분류 = brief v1 의 *임시 framing* 명문 (R-3 답습)
- ❌ **본 brief 의 진단표 (§3·§4) 가 후속 cycle 의 정정 *진입 근거* 가 되는 *de facto* 압력 발생** (R-29 답습)
- ❌ **본 cycle 합의 결과의 *기각* 자격도 자동 발효 0건** (R-30 답습)

---

## 1. 동기 (Why this cycle, Why now)

### 1.1 trigger — Provider Liquidity deep-dive 합의 R-26 (C-R2)

Provider Liquidity 합의 보고서 (`a9e1e88`) line 207 verbatim:

> **R-26 (C-R2)** brief v1.1 §7.3 옵션 (K) 에 **format 가족별 분류** 추가 — (a) GGUF 가족 (Ollama / llama.cpp / llamafile / ktransformers 부분) / (b) HF/safetensors 가족 (vLLM / SGLang / Aphrodite) / (c) compiled-engine 가족 (TensorRT-LLM / MLC-LLM) / (d) 자체 format 가족 (exllamav2 EXL2 / mlc-llm TVM)

본 cycle = R-26 의 **별도 brief 자격** (Provider Liquidity brief v1.1 §7.3 표 자체가 "별도 brief" 컬럼 명시) 답습.

### 1.2 trigger — Provider Liquidity 합의 R-11 (C-B4 + C-S2)

Provider Liquidity 합의 보고서 (`a9e1e88`) line 159~163 verbatim:

> **R-11** — brief evidence 가 *모두 GGUF 가족 내부* 한정 명문 (C-B4 + C-S2 통합)
> **근거**: brief §2.1~§2.4 evidence 가 *모두 GGUF 가족 내부* (Ollama 0.20.4·llama.cpp `c0c7e147`) 한정. 다른 format 가족 (HF/safetensors·TensorRT-engine·EXL2·MLC-TVM) 의 동급 평가에 *입력 자격 X*. 가족 간 비교 자격 본 cycle 미평가.
> **처리**: brief v1.1 §2.5 또는 §10 NOTE 표에 "본 cycle evidence = GGUF 가족 내부 한정 (Ollama·llama.cpp). 다른 format 가족 (HF/safetensors / compiled-engine / 자체 format) 의 동급 평가 입력 자격 0, 별도 cycle 의무" 명문 추가.

본 cycle = R-11 의 "별도 cycle" 답습 (Provider Liquidity brief v1.1 §10 NOTE 9 본문 carry-over).

### 1.3 본 cycle 의 핵심 질문

**Q1**: 4 가족 분류 (GGUF / HF-safetensors / compiled-engine / 자체) 가 **정확한가 + 완정한가**?
- 누락 후보 (Apple MLX / NVIDIA NIM / Cloud-only API like OpenAI-compatible / RWKV·MAMBA 자체 format 등) 자격
- 중첩 후보 (llamafile = GGUF + 실행 바이너리 = 가족 내부 vs 새 차원) 자격
- 분류 기준 (format file extension / loader 구현 path / serialization 방식 / 양자화 호환성) 의 정합성

**Q2**: 가족 내부 호환성과 가족 간 호환성이 **분리 가능한 자격** 인가?
- 가족 내부 = runtime 간 format 호환성 후보 ↑ (예: Ollama·llama.cpp 동일 GGUF 사용)
- 가족 간 = format 변환 의무 ↑ (예: GGUF ↔ HF-safetensors = `convert_hf_to_gguf.py` 의무)
- Phase 3 P3-F1 finding (Ollama `30e51a7c` ≠ llama.cpp `c0c7e147`) 는 **가족 내부에서도 시점 의존 호환성 부재** 발견 — 분리의 *순수 binary* 자격에 균열

**Q3**: Provider Liquidity 충족 자격이 *가족 내부* vs *가족 간* **분리 가능한가**?
- 가족 내부 충족 = "GGUF 가족 안에서 모델/runtime 교체가 코드 변경 없이 가능"
- 가족 간 충족 = "다른 format 가족으로 교체 시에도 코드 변경 없이 가능 (= conversion script 가 *수단*, ends 는 동일)"
- ADR-011 §2.1 means/ends 적용: 변환 script = means, 호환성 보장 = ends. case A (means 보전) / case B (ends 보전) / **case C (means+ends 양면, Provider Liquidity 합의 R-4 신규)** 적용 자격

**Q4**: MVP-1 R4 "동급" 진술의 가족 한정 자격은?
- R4 line 63 = "llama.cpp ↔ Ollama 동급" = **GGUF 가족 내부 한정** (양쪽 GGUF runtime) — R-11 답습
- 가족 간 "동급" (예: Ollama ↔ vLLM) = R4 진술 자격 0 (별도 합의 의무)
- 본 자격이 MVP-1 합의 *수정 진입 근거* 인가, 단순 *해석 명확화* 인가 (R-29 답습 — de facto 압력 차단)

### 1.4 헌법 본문 매핑 — Provider Liquidity 합의 R-13 답습

Provider Liquidity 합의 R-13 (Reviewer 단독 BLOCKING) 답습:

**ADR-011 line 6 verbatim** (상위 권위 명시):
> **상위 권위**: 헌법 제8조 (보안), 헌법 제5조 (Provider Liquidity), `docs/architecture/system-identity-prequel.md` §3

**ADR-011 line 245 verbatim** (관련 문서 §8.1 상위 권위):
> `docs/constitution/PROJECT_CONSTITUTION.md` 제8조 (보안), 제5조 **관용** (Provider Liquidity, 비협상)

본 cycle 매핑:
- 헌법 제5조 (관용 매핑, Provider Liquidity 비협상) — 본 cycle 의 *상위 권위* 답습
- 헌법 제8-2조 (하드코딩 제로) — 모델명·runtime 명·format 명·conversion script path 모두 환경 변수·config 의무
- ADR-011 §2.1 (a)~(e) — 변환 script (means) 와 호환성 보장 (ends) 양면 case C 적용
- **본 cycle 의 권위 한계**: 4 가족 분류 자체의 채택·기각·확장 자격 0 (R-12 답습)

### 1.5 ADR-011 §2.1 적용 자격 — 5 조건 (a)~(e) 통합

ADR-011 §2.1 (R-14 답습 — (a)~(e) 정합화):

- **(a) 비교표 명문**: 본 cycle = 4 가족 × Provider Liquidity 자격 4 항목 비교표 *시도*. 단 Phase 3 evidence GGUF 가족 한정 (R-11) → 비교 자격 = 4 × 4 = 16 cell 중 GGUF 한정 충족 cell ≤ 4 개 (sub-차원 (1) tensor naming 한정)
- **(b) 적대적 시연**: 가족 간 conversion 미수행 시 "동급" 진술의 침투 시연 추상 패턴 동형 자격 평가
- **(c) BI 위반 자격**: 4 가족 중 일부의 runtime/format/loader 가 BI-3 (agent ≠ root) 격리 자격 부재 가능성 — 별도 cycle
- **(d) 비례 평가**: 4 가족 모두 동등 평가 비용 vs 비례 우선순위 (GGUF 가족 = 본 환경 우선)
- **(e) 후속 패턴**: Provider Liquidity 합의 BLOCKING 본문 반영 의무 (R-21 답습) — 본 brief v1.1 보강 시점 자동 반영 자격, 본문 수정 자격 0

---

## 2. evidence 통합 (Phase 3 raw + Provider Liquidity 합의 + 외부 식별)

### 2.1 Phase 3 cycle evidence (GGUF 가족 내부 한정, R-11 답습)

**P3-F1 — GGUF format 호환성 부재 (Ollama `30e51a7c` ≠ llama.cpp `c0c7e147`)**

raw: `docs/phase0/v1-poc-raw/phase3/2026-05-24T04-32-phase3-measure-attempt-blocked.log`

- Ollama 보유 GGUF (`sha256-30e51a7c`, 오래된 conversion): `blk.X.ssm_dt` only
- llama.cpp `c0c7e147` master 요구: `blk.X.ssm_dt.bias` (flag=0 required)
- llama.cpp `convert_hf_to_gguf.py:299` 새 형식 `.dt_proj.bias` rename
- llama.cpp `qwen3next.cpp:87` `.bias` flag=0 required 강제

**범위 한정** (R-7 + R-11 답습):
- model loading sub-차원 5 중 (1) tensor naming convention 한정 evidence
- GGUF 가족 내부 한정 (다른 format 가족 입력 자격 0)
- 1 모델 (qwen3-coder-next, Gated DeltaNet hybrid) + 1 시점 (2026-05-24) — 일반화 자격 ↓ (R-3 시간축 답습)

**P3-F2~F7 carry-over** (Provider Liquidity brief v1.1 §2.1~§2.4 답습):
- F2: sm_120a+sm_121a SASS 모두 포함 (가설 #6 약화)
- F3: R-1 anchor 8회 일치 (silent 교체 미발생)
- F4: Phase 1 prompt 정확 detokenize
- F5: Ollama API FROM 경로 부정확
- F6: docker-proxy 11434 listening (Ollama Docker wrapper 가능성)
- F7: OLLAMA_KEEP_ALIVE=-1

### 2.2 Provider Liquidity 합의 본문 (`a9e1e88`) carry-over 핵심

**합의 BLOCKING 13 + 권고 17 + NOTE 12** (기각 0):

| 항목 | 본 cycle 답습 의무 |
|---|---|
| R-3 (4 수준 framing self-citation + 시간축 + 비교 자격 1/4) | 본 brief framing 임시성 명문 §4.5 + 시간축 5번째 축 |
| R-7 (model loading 5 sub-차원 분해) | §2.1 P3-F1 = sub-차원 (1) 한정 명문 |
| R-11 (evidence GGUF 가족 한정) | **본 cycle 의 직접 진입 근거** — §1.2 |
| R-12 (cycle-specific framing 영구화 risk) | §0 + §7 (D3)(D4) 분기 답습 |
| R-13 (ADR-011 line 6/245 관용 매핑) | §1.4 + §3 권위 매핑 |
| R-21 (Reviewer 권한 한계) | §6 Reviewer 권한 boundary 명문 |
| R-26 (format 가족별 분류) | **본 cycle 의 직접 진입 근거** — §1.1 |
| R-29 (de facto 압력 차단) | §0 + §9 차단 |
| R-30 (기각 자격 명시) | §0 + §7.4 |

### 2.3 4 가족 외부 식별 (추정 한정, 라이브 검증 0건)

**자격 한계 명문**: 본 §2.3 은 *외부 식별 추정* 만, 각 runtime/format 의 라이브 verify (download/install/test) = 본 cycle 자체 진행 0 (§0 답습). 외부 정보 출처 = LLM 사전 지식 + 공식 repo 추정. **각 runtime 의 실제 버전·실제 format spec·실제 호환성 = 별도 cycle 의 라이브 verify 의무**.

#### (a) GGUF 가족

| runtime | format | 비고 |
|---|---|---|
| **Ollama** (v0.20.4 확인, Phase 1 R-1) | GGUF (자체 conversion) | Phase 3 evidence — 오래된 conversion 답습 |
| **llama.cpp** (`c0c7e147` 확인, Phase 3 R-2) | GGUF | Phase 3 evidence — 최신 conversion 요구 |
| **llamafile** | GGUF + 실행 바이너리 | Mozilla Builders, single-file deploy 모델 |
| **ktransformers** (부분) | GGUF + 자체 quant | MoE 최적화 specialized, GGUF 부분 호환 |

**가족 내부 호환성 추정**: 동일 GGUF spec 버전 한정, conversion script 동일 시점 한정 호환. Phase 3 evidence = **시점 의존 호환성 부재** 입증 (R-3 시간축 답습).

#### (b) HF-safetensors 가족

| runtime | format | 비고 |
|---|---|---|
| **vLLM** | HF-safetensors + paged attention | MVP-1 합의 R4 "MVP-1 비채택, MVP-2 재검토" (sm_120/121 binary-compat issue #36821) |
| **SGLang** | HF-safetensors + RadixAttention | 별도 runtime |
| **Aphrodite Engine** | HF-safetensors (vLLM fork) | community fork |

**가족 내부 호환성 추정**: HuggingFace safetensors spec 동일 시 호환. config.json + tokenizer.json 동반 의무.

#### (c) compiled-engine 가족

| runtime | format | 비고 |
|---|---|---|
| **TensorRT-LLM** | `.engine` (TensorRT 컴파일 결과) | NVIDIA, GPU 특정 SM 의존 컴파일 |
| **MLC-LLM** | `.so` / TVM compiled | Apache TVM 기반, GPU/CPU/모바일 다양 target |

**가족 내부 호환성 추정**: **컴파일 시점·target HW 의존성 극강** — 가족 내부에서도 동일 GPU·동일 compiler 버전 한정. Provider Liquidity 충족 자격 *최약*.

#### (d) 자체 format 가족

| runtime | format | 비고 |
|---|---|---|
| **exllamav2** | EXL2 (자체 quant format) | GPTQ 후속, group-wise quant |
| **MLC-LLM TVM** (c 와 일부 중첩) | TVM IR compiled | runtime 통합되어 있음 |

**가족 내부 호환성 추정**: 각 runtime 의 자체 format 한정, 가족 *내부* 자체가 단일 runtime 일 가능성 (Q-C1 ⭐ — 가족 정의 자격).

#### 누락 후보 (사전 식별, Q-C1 답습)

- **Apple MLX** — Apple Silicon 한정, 자체 format
- **NVIDIA NIM** — 컨테이너 단위 배포, format 추상화
- **OpenAI-compatible Cloud API** — format 자체 추상화 (HTTP), Provider Liquidity 의 *반대편 극*
- **RWKV / MAMBA 자체 format** — 아키텍처별 specialized
- **AWQ / GPTQ / SmoothQuant** — 양자화 format (cross-runtime 부분 호환)

#### 중첩 후보 (사전 식별, Q-C2 답습)

- **llamafile** — (a) GGUF 가족 + 실행 바이너리 차원 = (a) 의 sub-차원 vs 새 차원 분류 자격
- **MLC-LLM** — (c) 와 (d) 중첩 (TVM compiled + 자체 runtime)
- **OpenAI-compatible API** — endpoint 추상화 차원 = 4 가족 분류와 *교차 축*

---

## 3. SDD 정합성 매트릭스

### 3.1 헌법·ADR-011 권위 매핑 정합성

| 권위 | 본 cycle 자격 |
|---|---|
| **헌법 제5조 (관용 매핑, Provider Liquidity, 비협상)** (ADR-011 line 245 verbatim) | 본 cycle 상위 권위, 본질 약화 자격 0 (R-10 답습) |
| **헌법 제5조 코드 품질 본문** (line 40~46: SRP·중복 제거·**내부 코드 신뢰**·린터) | 4 가족 분류의 코드 영향 = 별도 cycle (R-15 답습) |
| **헌법 제8-2조 하드코딩 제로** (line 67~73) | 모델명·runtime 명·format 명·conversion script path 모두 환경 변수 의무 |
| **ADR-011 §2.1 (a)~(e)** | 5 조건 적용 자격 평가 (§1.5) — 본 cycle = 자격 평가 only |
| **ADR-011 §6 본문** | 자동 정정 자격 0 (R-21 답습) |

### 3.2 MVP-1 R4 진술 검증 자격 (R-3 + R-7 + R-11 답습)

MVP-1 합의 R4 verbatim (R-17 답습 — 축약 차단):
> **R4**: M3 런타임 재조정 — **llama.cpp ↔ Ollama 동급**(MoE 실측 llama.cpp ~31 tok/s, Ollama MoE 미공개), V-1에서 둘 다 MoE 측정. vLLM "제외(#36821)" → "MVP-1 비채택, MVP-2 재검토"(sm_120/121 binary-compat·0.17 해소 흐름; 영구배제는 C-2 충돌)

**4 수준 + 시간축 비교 자격 (가족 한정 분리)** — Provider Liquidity 합의 R-3 + R-11 답습:

| 수준 | GGUF 가족 내부 (llama.cpp ↔ Ollama) | 가족 간 (Ollama ↔ vLLM 등) |
|---|---|---|
| 인터페이스 (`/v1/chat/completions`) | P1-F2/F4: 양쪽 endpoint 보유 (강한 후보) | 가족 간 endpoint 호환 자격 — vLLM·SGLang 도 OpenAI-compatible 추정 (라이브 verify 0) |
| model loading sub-차원 (1) tensor naming | P3-F1: **부정 강한** (시점 의존) | 가족 간 = format 자체 다름 (HF ↔ GGUF), conversion script 의무 (means 차원) |
| 성능 (tok/s) | Phase 1 Ollama 측정 7.83, llama.cpp 측정 0 (차단) | 가족 간 = 가족 내부 측정 부재 시 자격 0 |
| 운영성 | Ollama 측정 (Stage 1+2+3+4 + Phase 1+1.5), llama.cpp 측정 0 | 가족 간 = 양쪽 측정 부재 |
| **시간축** (R-3 답습) | 변환·빌드 시점 의존 (Ollama `30e51a7c` vs llama.cpp `c0c7e147`) | 가족 간 = 시점 의존 + 가족별 발전 cadence 의존 |

**Q4 자격**: R4 "동급" 진술의 가족 한정 자격 = **GGUF 가족 내부 한정**. 가족 간 동급 진술 자격 0 (별도 합의 의무 — R-21 답습).

### 3.3 ADR-011 §2.1 답습 자격 (a)~(e)

| 조건 | GGUF 가족 내부 | 가족 간 |
|---|---|---|
| **(a) 비교표** | sub-차원 (1) tensor naming 강한 부정, sub-차원 (2)~(5) 미측정 | 가족 간 비교 cell ≥ 4 × 4 = 16, 충족 cell **0건** (외부 식별 추정만, 라이브 verify 0) |
| **(b) 적대적 시연** | P3-F1 = 침투 시연 (시점 차이만으로 차단) | 가족 간 conversion 부재 시 100% 차단 침투 시연 추상 패턴 동형 자격 |
| **(c) BI 위반** | runtime 격리 자격 별도 cycle | 가족별 runtime 격리 자격 별도 cycle |
| **(d) 비례 평가** | 본 환경 (GB10) = GGUF 가족 우선 (vLLM #36821 binary-compat issue 답습) | 다른 환경 (x86_64 datacenter) = HF-safetensors·compiled-engine 비례 우선 가능 |
| **(e) 후속 패턴** | Phase 3 합의 BLOCKING 7 + Provider Liquidity 합의 BLOCKING 13 본문 반영 의무 (R-21 답습) | 본 cycle 합의 결과 BLOCKING 본문 반영 의무 (자동) |

### 3.4 메모리 본문 정확성

`feedback_provider_liquidity` 메모리 본문 (system reminder verify):
> 어떤 모델, 구독, 오케스트레이터에도 락인되지 않아야 하며, 교체가 **코드 변경 없이** 가능해야 한다.

🔴 **메모리 19일+ stale 명문** (Provider Liquidity 합의 R-20 답습) — 본 cycle 본문 인용 자격은 (1) 본 cycle 답습 의무 / (2) 신규 cycle 진입 시 메모리 재verify 의무.

본 cycle 평가: "교체가 코드 변경 없이 가능" 진술의 *범위 한정* 자격 = (a) 가족 내부 한정 / (b) 가족 간 포괄 — 본질은 *전자 가족 한정도 충족 가능* 한가, *후자 포괄까지 의무* 인가의 자격 평가 (단 본 평가는 메모리 본문 정정 자격 0, 합의 후 별도 cycle).

`project_jarvis_local_boss_direction` 메모리:
> provider-agnostic 개인 자비스: 로컬 LLM=사장(직접 지휘)·claude/gpt/GLM CLI=tmux 워커(교체)

본 cycle = "로컬 LLM=사장" 의 runtime 선택 자격에 직접 적용. 4 가족 분류의 사장 측 (로컬 LLM runtime) 적용 자격 평가 의무.

---

## 4. 핵심 긴장 5축 분석

> **🔴 R-3 답습 + R-12 답습 — 본 framing (4 가족 + 5축) 은 brief v1 의 *임시 framing*. ADR-011·헌법·MVP-1 합의·메모리 본문 정의 부재. cycle-specific framing 영구화 risk 차단 의무. 본 framing 채택 자격 = 본 cycle 합의 결과의 별도 명시 — 자동 영구화 0건.**

### 4.1 축 1 — 가족 내부 호환성 자격

**핵심 질문**: 각 가족 내부에서 runtime 간 동일 format 으로 *코드 변경 없이* 교체 가능한가?

- **GGUF 가족**: Phase 3 P3-F1 = **시점 의존 호환성 부재** (시점 정합 시 호환 후보). conversion script 의 *시점 lock* 필요
- **HF-safetensors 가족**: vLLM/SGLang/Aphrodite 간 호환성 추정 (라이브 verify 0)
- **compiled-engine 가족**: GPU SM 의존 컴파일, runtime 간 호환 자격 *최약*
- **자체 format 가족**: 단일 runtime 가족이면 "내부 호환성" 개념 자체 무의미

**평가 자격**: 가족 내부 호환성 = **format spec 동일성 + conversion script 시점 정합성 + runtime 버전 정합성** 의 3 조건 교집합. 단일 binary 호환 자격 X.

### 4.2 축 2 — 가족 간 호환성 자격

**핵심 질문**: 다른 가족으로 교체 시에도 *코드 변경 없이* 가능한가?

- **GGUF ↔ HF-safetensors**: `convert_hf_to_gguf.py` 의무 — *수단* 차원 (means)
- **GGUF ↔ compiled-engine**: GGUF → HF → TensorRT-LLM build 2단계 의무
- **HF-safetensors ↔ compiled-engine**: vLLM ↔ TensorRT-LLM = compilation step 의무
- **자체 format ↔ 다른 가족**: format 변환 의무 + 양자화 재수행 의무

**평가 자격**: 가족 간 호환성 = **conversion 의무 100%** (binary 답습). Provider Liquidity 충족 자격 = conversion script 가 *Python 코드 변경*인가 *config 변경*인가의 자격 평가 (means/ends 적용).

### 4.3 축 3 — Provider Liquidity 충족 자격의 분리 가능성

**핵심 질문**: Provider Liquidity (헌법 5조 비협상) 의 *교체 가능* 진술이 *가족 내부 한정* vs *가족 간 포괄* 분리 가능한가?

| 분리 후보 | 진술 |
|---|---|
| **(α) 가족 내부 한정** | "Provider Liquidity = 본 환경 선택 가족 내부의 runtime 교체 자격" (Liquidity 강도 ↓) |
| **(β) 가족 간 포괄** | "Provider Liquidity = 모든 가족 간 교체 자격 (conversion script 포함)" (Liquidity 강도 본질 유지) |
| **(γ) layered** | "내부 layer 강한 / 외부 layer 약한" (Provider Liquidity 합의 §7 (D) 옵션) |
| **(δ) abstracted via API** | "OpenAI-compatible API 추상화 layer = format 가족 abstraction" (Provider Liquidity 합의 §7 (D2) 답습) |

**자격 평가**:
- (α) = Provider Liquidity 본질 약화 risk (R-10 답습 차단)
- (β) = 본질 유지, conversion script 의무 명문 의무
- (γ) = R-12 답습 — framing 영구화 risk, (D3)(D4) 분기 답습
- (δ) = endpoint 추상화 차원, 4 가족 분류와 교차 축

본 cycle = (α)~(δ) 자격 평가 only, 채택·기각 자격 0 (합의 *후* 사용자 명시 의무).

### 4.4 축 4 — 시간축 (Provider Liquidity 합의 R-3 답습)

**핵심 질문**: format 가족별 호환성이 *시점* 에 따라 어떻게 진화하는가?

- **GGUF spec 진화**: v1 → v2 → v3 (Provider Liquidity 합의 N-12 답습) — spec 자체 변화
- **conversion script 시점**: Ollama `30e51a7c` (≥ N개월 전) vs llama.cpp `c0c7e147` (최신) — 시점 lag
- **runtime 버전 정합성**: Ollama 0.20.4 (Phase 1) ↔ llama.cpp 최신 — 동시 업데이트 부재 시 호환성 disconnect
- **가족별 발전 cadence**: GGUF 가족 (활발 변경) vs compiled-engine (느린 cadence, HW dependent)

**평가 자격**: 시간축 = **본 cycle 평가의 missing dimension** (Provider Liquidity 합의 R-3 답습). 4 가족 분류 = 특정 시점 (2026-05-24) 스냅샷, 시점 변경 시 분류 자체 변동 자격.

### 4.5 축 5 — 본 framing 임시성 명문 (R-3 + R-12 답습)

🔴 **본 §4 의 5축 자체가 brief v1 의 *임시 framing*** — ADR-011·헌법·MVP-1 합의·메모리 본문 정의 부재. 다른 framing 가능:

- **framing α' (4 가족 + 시간축 = 본 brief 채택 framing)**: 5축 분석
- **framing β'**: 양자화 차원 우선 (Q4_K_M / Q8_0 / FP16 / FP8 / INT4-AWQ / EXL2 등) — 양자화별 가족 분류
- **framing γ'**: deployment 차원 우선 (single-binary / docker / kubernetes / cloud-native) — 배포 형태 분류
- **framing δ'**: aggregator abstraction 우선 (LiteLLM / Ollama-compatible / OpenAI-compatible) — endpoint 추상화 분류
- **framing ε'**: hardware target 우선 (NVIDIA / AMD / Apple Silicon / mobile / CPU-only) — HW 분류

**채택 자격**: 본 framing α' 의 본 cycle 채택 = **임시 framing** (R-12 답습 cycle-specific framing 영구화 차단). 합의 채택 자격은 사용자 명시 + 별도 cycle 후속.

---

## 5. 3+1 합의 분담안

### 5.1 Agent 분담 + 핵심 질문 (R-22 답습 — 병렬 독립)

| 에이전트 | 관점 | 핵심 질문 |
|---|---|---|
| **Agent A** (구현 분석가) | "기술적으로 검증 가능한가? 4 가족 분류가 실 호환성 evidence 와 일치하는가?" | (Q-A1) 4 가족 분류의 기술적 정합성 (format spec / loader 구현 path / serialization 방식) / (Q-A2) Phase 3 P3-F1 evidence 의 가족 내부 일반화 자격 / (Q-A3) 가족 내부 호환성과 가족 간 호환성의 분리 가능성 (구현 수준) / (Q-A4) 누락 가족 (MLX·NIM·OpenAI-compat·RWKV·AWQ/GPTQ) 자격 |
| **Agent B** (품질·안전성) | "안전한가? 본 framing 이 헌법·ADR-011·MVP-1 합의·메모리 권위에 정합하는가?" | (Q-B1) Provider Liquidity 본질 약화 risk (α 분리 = 본질 약화 자격?) / (Q-B2) MVP-1 R4 진술의 가족 한정 자격 (자동 정정 자격 차단) / (Q-B3) ADR-011 §2.1 (a)~(e) 5 조건 적용 자격 (가족 간 비교 cell 충족 자격) / (Q-B4) 메모리 본문 "코드 변경 없이" 범위 자격 / (Q-B5) 본 brief 의 self-citation anchor risk (R-3 답습) |
| **Agent C** (대안 탐색가) | "더 나은 framing 이 있는가? 4 가족 분류 자체에 누락·중첩이 있는가?" | (Q-C1) 4 가족 분류 외 framing (양자화/배포/aggregator/HW target) 비교 자격 / (Q-C2) 중첩 후보 (llamafile·MLC-LLM) 분류 자격 / (Q-C3) 시간축 + spec 진화 (GGUF v3·HF safetensors v2·AWQ progression) 자격 / (Q-C4) "format 가족 분리" 가 cycle-specific framing 영구화 risk (R-12 답습) — 영구화 차단 패턴 / (Q-C5) layered 모델 / abstracted API 의 4 가족 분류와의 교차 축 자격 |

### 5.2 분담 의무 (R-22 답습)

- 3 에이전트 **병렬 독립** — 서로의 출력 참조 0건 (편향 방지, CLAUDE.md §3 Phase 2 답습)
- 본 brief 본문 + Provider Liquidity 합의 본문 + Phase 3 raw 17 파일 + 헌법 본문 + ADR-011 본문 + MVP-1 합의 본문 cross-check 한정
- **각 에이전트 자체의 4 가족 분류 *채택*·*기각* 권한 0** — 진단 + 권고 옵션 매트릭스만
- 각 에이전트 자체의 라이브 verify (download/install/test) 권한 0 — 본 cycle 자체 진행 0 답습

### 5.3 Reviewer 권한 + 한계 (R-21 답습 강화)

**Reviewer 권한**:
- 3 에이전트 출력 교차 비교 (일치 / 부분 / 불일치 / 누락)
- 합의 BLOCKING / 권고 / NOTE 분류 + 최종 판단
- **합의 결과 BLOCKING 본문이 brief v1.1 보강의 정정 자격** (R-21 답습)

**Reviewer 한계 (영구 답습)**:
1. ADR-011 §6 본문 정정 자격 0 (헌법급)
2. **Provider Liquidity 본질 약화 자격 0** (binary 본질 유지)
3. MVP-1 합의 본문 정정 자격 0 (별도 cycle)
4. 헌법 본문 정정 자격 0
5. 메모리 본문 정정 자격 0 (본 cycle 합의 결과의 메모리 갱신 자격은 별도 사용자 명시)
6. **4 가족 분류 자체의 영구 framing 정착 자격 0** (R-12 답습)
7. **자동 다음 단계 진입 자격 0** (R-29 + R-30 답습)

---

## 6. 합의 출력 형식

### 6.1 출력 형식 명문

각 Agent 보고서:
- **판정**: APPROVE / REVISE / REJECT
- **BLOCKING** (필수 정정): 본문 verbatim 인용 + 처리 권고
- **권고** (보강): 본문 직접 반영 또는 §10 NOTE carry-over
- **NOTE** (carry-over): 본 cycle 후속 의무

Reviewer 통합 보고서:
- **3 에이전트 정합성 매트릭스**: 일치 / 부분 / 불일치 / 누락
- **단독 발견 표시**: A-S* / B-S* / C-S* / R-S* (Reviewer 단독)
- **BLOCKING 통합 + verbatim 본문 + 처리 권고**
- **권고 통합 + NOTE 통합**
- **기각**: 명시 + 사용자 명시 의무 (R-30 답습)

### 6.2 raw line-level cross-check 의무 (Provider Liquidity 합의 R-23 답습)

- Phase 3 raw 17 파일의 line-level 인용 (offset 명시)
- Provider Liquidity 합의 보고서 line-level 인용 (line 6/245/207/159~163 등)
- 헌법 본문 line 인용 (40~46, 67~73)
- ADR-011 본문 line 인용 (6, 245, §2.1, §6)
- MVP-1 합의 본문 line 인용 (R4 = line 63)

---

## 7. 후속 결정 권고 옵션 매트릭스

### 7.1 옵션 (A)~(E) — 본 cycle 직접 결과 답습

| 옵션 | 내용 | 진입 자격 |
|---|---|---|
| **(A)** | 4 가족 분류 **현 상태 유지** + 본 brief framing 임시성 명문만 (Provider Liquidity 합의 R-12 답습 강한 변형) | 합의 후 사용자 명시. MVP-1 합의·메모리 본문 변경 0건 |
| **(B)** | 4 가족 분류 + 누락 가족 추가 (MLX·NIM·OpenAI-compat·RWKV·AWQ/GPTQ 등) | 합의 후 사용자 명시. C-Q4 답습 |
| **(C)** | 4 가족 분류 폐기 + 다른 framing 채택 (양자화/배포/aggregator/HW target) | 합의 후 사용자 명시 + 별도 framing 합의 cycle |
| **(D)** | layered Provider Liquidity 모델 신규 ADR 발의 (Provider Liquidity 합의 §7 (D) 답습) | 헌법급 변경 trigger — 사용자 명시 + 풀 3+1 + Reviewer 권한 한계 답습 별도 cycle |
| **(E)** | abstracted API layer (LiteLLM / OpenAI-compatible) 채택 ADR 발의 | 별도 합의 cycle |

### 7.2 옵션 (F)~(J) — 가족별 deep-dive cycle

| 옵션 | 내용 | 진입 자격 |
|---|---|---|
| **(F)** | GGUF 가족 deep-dive — sub-차원 (2)~(5) 측정 (MoE routing / tokenizer / chat template / quantization) | 별도 brief + 사용자 명시. 측정 cycle |
| **(G)** | HF-safetensors 가족 라이브 verify — vLLM/SGLang Qwen3-Next 호환성 측정 (sm_120/121 binary-compat 해소 흐름 추적) | 별도 brief + 사용자 명시. 다운로드/설치 cycle |
| **(H)** | compiled-engine 가족 라이브 verify — TensorRT-LLM Blackwell support 추적 | 별도 brief + 사용자 명시. NVIDIA toolchain cycle |
| **(I)** | 자체 format 가족 라이브 verify — exllamav2 / MLC-LLM 평가 | 별도 brief + 사용자 명시 |
| **(J)** | 4 가족 cross-conversion 매트릭스 — GGUF ↔ HF ↔ TensorRT ↔ EXL2 conversion script 평가 | 별도 brief + 사용자 명시 |

### 7.3 옵션 (K)~(M) — 후속 framing cycle

| 옵션 | 내용 | 진입 자격 |
|---|---|---|
| **(K)** | aggregator (LiteLLM / vllm-openai / Ollama-compat / OpenAI-compat) 추상화 layer 비교 cycle | 별도 brief |
| **(L)** | 양자화별 cross-runtime 호환성 cycle (AWQ/GPTQ/EXL2/GGUF Q4_K_M 등) | 별도 brief |
| **(M)** | HW target 별 가족 비례성 (NVIDIA / AMD / Apple Silicon / mobile) | 별도 brief |

### 7.4 DEFER / 기각 옵션 (R-30 답습 — 기각 자격도 사용자 명시)

| 옵션 | 내용 | 발생 |
|---|---|---|
| **(D1)** | 본 4 가족 분류 자체 기각 — framing 채택 자격 0 명문 | 사용자 명시 + 별도 합의 |
| **(D2)** | 본 cycle 결과의 메모리 갱신 자격 0 — `feedback_provider_liquidity` 본문 유지 | 자동 (기본값) |
| **(D3)** | MVP-1 R4 진술 정정 자격 0 — 가족 한정 자격은 *해석 명확화* only, 본문 정정 0건 | 사용자 명시 차단 (R-29 답습) |
| **(D4)** | 4 가족 분류의 영구 framing 정착 0 — 다른 cycle 의 진입 근거화 차단 | 자동 (R-12 + R-29 답습) |

---

## 8. 정직성 한계

1. **본 brief v1 = 외부 식별 추정 only** — 4 가족 8+ runtime 의 라이브 verify (download/install/test) 0건. 각 runtime 의 실제 버전·실제 format spec·실제 호환성 = 별도 cycle 의 라이브 verify 의무
2. **Phase 3 evidence GGUF 가족 한정** (R-11 답습) — 다른 3 가족 (HF/compiled-engine/자체) 의 본 cycle 평가 = *입력 자격 0* 시작점
3. **P3-F1 evidence sub-차원 (1) 한정** (R-7 답습) — model loading 의 sub-차원 (2)~(5) (MoE routing / tokenizer / chat template / quantization) 미측정
4. **4 가족 분류 자체의 영구 framing 자격 0** (R-12 답습) — cycle-specific framing, 채택·기각·확장 자격 = 본 cycle 합의 + 사용자 명시 *후*
5. **시간축 missing dimension 가능성** (R-3 답습) — 본 brief 평가 = 특정 시점 (2026-05-24) 스냅샷, 시점 변경 시 분류 자체 변동 자격
6. **MVP-1 R4 진술의 가족 한정 자격 = 해석 명확화 자격**, 본문 정정 자격 0 (R-21 답습)
7. **헌법 5조 본문 ↔ ADR-011 line 6/245 관용 매핑 권위** = 본 cycle 답습 의무, 권위 자체 변경 자격 0 (R-13 + R-9 답습)
8. **메모리 `feedback_provider_liquidity` 19일+ stale** (R-20 답습) — 본 cycle 인용 자격 답습 후 신규 cycle 진입 시 재verify 의무
9. **Phase 3 P3-F1 일반화 자격 한정** — 1 모델 (qwen3-coder-next) + 2 runtime (Ollama·llama.cpp) + 1 시점 (2026-05-24) 측정. 다른 모델·다른 runtime·다른 시점 일반화 = 별도 cycle
10. **본 brief 의 5축 framing 자체가 anchor effect risk** — 다른 framing 가능 (β'/γ'/δ'/ε' Q-C1 답습), framing 채택 자격 = 본 cycle 합의 + 사용자 명시 *후*
11. **본 brief 의 SDD 정합성 평가 = 본 cycle 시점 한정** — 메모리·MVP-1 합의·헌법·ADR-011 본문이 본 cycle 후 변경되면 본 brief 진술 자격 재평가 의무
12. **Reviewer 권한 한계 답습** — ADR-011 §6 본문 정정 자격 0 + Provider Liquidity 본질 약화 자격 0 + MVP-1 합의 본문 정정 자격 0 + 헌법 본문 정정 자격 0 + 메모리 본문 정정 자격 0 + **4 가족 분류 자체의 영구 framing 정착 자격 0** (R-12 + R-21 답습)
13. **본 brief 가 후속 cycle 의 *de facto* 정정 진입 근거화 0건** (R-29 답습) — 후속 cycle 의 정정 자격은 사용자 명시 + 별도 합의 의무
14. **본 cycle 합의 결과의 *기각* 자격도 자동 발효 0건** (R-30 답습)
15. **본 brief 의 누락 가족 식별 (MLX·NIM·OpenAI-compat·RWKV·AWQ/GPTQ) = 추정** — 라이브 verify 0, 누락 자격 자체 = Agent C 의무
16. **중첩 후보 (llamafile·MLC-LLM) 분류 자격** = 추정, Agent C 의무

---

## 9. 차단 조건

### 9.1 본 brief 가 자동 발효시키지 않는 것

- ❌ 4 가족 분류 자체의 결정 *고정* (모든 옵션 = 사용자 명시 의무)
- ❌ MVP-1 합의·메모리·헌법·ADR-011 본문 자동 정정
- ❌ M3·M4 결정 *고정*
- ❌ runtime backend 코드 작성 (OllamaBoss·LlamaCppBoss·vLLMBoss·TensorRTLLMBoss·기타)
- ❌ 새 측정·새 빌드·새 다운로드·새 설치
- ❌ Provider Liquidity 본질 약화 (binary 본질 유지)

### 9.2 합의 BLOCKING 처리 의무 (R-21 답습)

본 cycle 합의 *후* brief v1 → v1.1 보강:
- BLOCKING verbatim 본문 직접 반영 100% 의무
- 권고 본문 직접 반영 또는 §10 NOTE carry-over
- §11 변경 일람 표 신규 (Provider Liquidity brief v1.1 §11 패턴 답습)

### 9.3 본 brief 진단표 (§3·§4) → 후속 cycle 정정 진입 근거화 차단 (R-29 답습)

본 §3 · §4 의 표 자체가 후속 cycle 의 MVP-1 합의·헌법·ADR-011 본문 정정 *de facto* 진입 근거가 되는 흐름 차단. 후속 cycle 의 정정 자격은 (1) 사용자 명시 + (2) 별도 합의 cycle 의무.

### 9.4 본 cycle 합의 결과의 자동 기각 자격 차단 (R-30 답습)

본 cycle 합의 결과 (BLOCKING / 권고 / NOTE) 의 *기각* 자격도 자동 발효 0건. 기각 자격 = 사용자 명시.

---

## 10. NOTE carry-over

Provider Liquidity 합의 NOTE 12 (`a9e1e88`) carry-over 답습:

| NOTE | 본 cycle 답습 |
|---|---|
| N-1 (SSM 명명법 정정 부분 적용) | Phase 1·2·3 evidence 답습 시 명명법 정합성 유지 |
| N-2 (runtime 별 implementation 차이 어법 약점) | 본 brief §2.1~§2.3 답습 |
| N-3 (P3-F1 일반화 자격 3 차원 한정) | §8 정직성 9 답습 |
| N-4 (ADR-011 §2.1 (e) 모법 인용 자격) | §1.5 (e) 답습 |
| N-5 (메모리 19일+ stale) | §3.4 + §8 정직성 8 답습 |
| N-6 (옵션 (K) R4 범위 확장 자격) | 본 §7 (D)/(D3) 답습 |
| N-7 (LiteLLM 인터페이스 한정) | §7 (K) (E) 답습 |
| N-8 (ADR-008 부록 B Amendment 패턴) | (D) 옵션 자격 답습 |
| N-9 (라이센스 차원) | §7 (M) 후보 답습 |
| N-10 (비용 차원) | §7 (M) 후보 답습 |
| N-11 (한국어 모델 호환성) | 별도 cycle |
| N-12 (외부 표준화 동향 + supply chain opacity) | §4.4 시간축 답습 |

본 cycle 신규 NOTE 후보 (Agent C 의무):
- N-13 후보: 4 가족 분류의 spec 표준화 부재 자격
- N-14 후보: aggregator (LiteLLM 등) 의 4 가족 abstraction 자격 변동
- N-15 후보: HW vendor 의 가족 lock-in 압력 (NIM·MLX) 자격

---

## 11. 다음 단계 (자동 진입 0건)

본 brief v1 → 사용자 검토 → 풀 3+1 합의 진입 사용자 명시 → 풀 3+1 합의 (Agent A/B/C 병렬 독립 → Reviewer 통합) → brief v1.1 보강 (BLOCKING verbatim 반영) → 세션 정리 → commit·push.

**각 단계 = 사용자 명시 의무** (`feedback_staged_consensus_workflow` 답습). 자동 다음 단계 진입 0건.

**합의 *후* 결정 자격**: §7 옵션 (A)~(M) + DEFER (D1)~(D4) 중 사용자 명시.

**본 cycle 의 *영구 핵심 한계* 재확인**:
- 본 cycle = framing 합의 입력 deep-dive
- 측정·빌드·다운로드·설치 0건
- sudo 0회
- M3·M4 결정 *고정* 0건
- runtime backend 코드 0건
- 메모리·헌법·MVP-1 합의·ADR-011 본문 자동 정정 0건
- Provider Liquidity 본질 약화 0건 (binary 본질 유지, spectrum 화는 framing 도구 한정)
- 4 가족 분류 자체의 영구 framing 정착 0건 (R-12 답습)

---

**End of brief v1** (작성일 2026-05-24, 사용자 명시 후 v1.1 보강 staged)
