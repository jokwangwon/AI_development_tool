# Jarvis MVP-1 Provider Liquidity deep-dive 합의 cycle entry brief (v1, DRAFT)

> **본 brief = Provider Liquidity finding (V-1 PoC Phase 3) deep-dive 합의 cycle 진입 brief.** 본 brief 의 어떤 §도 그 자체로 **코드 작성·런타임 변경·모델 다운로드·측정 실행·config 변경·M3/M4 결정 *고정*·MVP-1 합의 본문 자동 정정·헌법 본문 자동 정정·ADR-011 amendment 자동 발의** 를 발생시키지 않는다. 실 변경 0건. staged: brief v1(본 문서) → **사용자 검토·승인** → **풀 3+1 합의(별도 명시)** → brief v1.1 보강 → 세션 정리·commit·push. 자동 다음 단계 진입 0건.

**작성일**: 2026-05-24 (carry-over 후 본 세션 산출)
**카테고리**: 합의 cycle entry brief (Phase 3 cycle 산출 finding deep-dive)
**범위 (사용자 명시)**: **Phase 1+2+3 통합 evidence** 분석 / **진단 + 권고 옵션 매트릭스** (결정 *고정* 0건, 사용자 명시 의무 유지)
**선행 답습**:
- `docs/phase0/jarvis-mvp1-local-boss-design-brief.md` (MVP-1 design v2, `15beb33`, C-2 + R4 + M3)
- `docs/review/3plus1-consensus-2026-05-22-jarvis-mvp1-local-boss.md` (MVP-1 합의, R4 llama.cpp ↔ Ollama 동급)
- `docs/phase0/jarvis-mvp1-v1-poc-findings.md` (Phase 1+Stage 5 통합 findings DRAFT, 488줄)
- `docs/phase0/jarvis-mvp1-v1-poc-phase2-entry-brief.md` (Phase 2 entry → EXECUTED `c66756b`)
- `docs/phase0/jarvis-mvp1-v1-poc-phase3-entry-brief.md` (Phase 3 entry v1.1, `25eb008`)
- `docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-v1-poc-phase3-entry.md` (Phase 3 합의 BLOCKING 7)
- `docs/phase0/v1-poc-raw/phase3/2026-05-24T04-36-phase3-summary.json` (Phase 3 실 빌드 cycle summary)
- `docs/phase0/v1-poc-raw/phase3/2026-05-24T04-32-phase3-measure-attempt-blocked.log` (GGUF format 호환성 차단 raw)
- `docs/decisions/ADR-011-means-vs-ends-redaction.md` (§2.1 means/ends 일반 원칙 — 본 cycle 적용 자격 평가 대상)
- `docs/constitution/PROJECT_CONSTITUTION.md` (제5조 코드 품질 + 제8-2조 환경 관리 / 하드코딩 제로 모델명)
- 메모리: `feedback_provider_liquidity` (하드 요구 / Hermes 도입 검토 시 등록) / `project_jarvis_local_boss_direction` / `feedback_staged_consensus_workflow` / `feedback_proportionate_security_personal_tool` / `project_minimize_user_intervention`

---

## 0. 본 brief 가 *하는* 것 / *하지 않는* 것

### 하는 것

1. Phase 1+1.5(Stage 5)+2+3 evidence 통합 정리 (§2)
2. SDD 정합성 매트릭스 — 헌법 본문 정확 매핑 + MVP-1 합의 R4 + C-2 + ADR-011 §2.1 means/ends 일반 원칙 적용 자격 평가 (§3)
3. 핵심 긴장 4축 분석 (§4)
4. 3+1 합의 분담안 — Agent A/B/C 관점·핵심 질문·출력 형식 (§5)
5. 합의 출력 형식 명문 — BLOCKING/권고/NOTE/기각 분류 (§6)
6. 후속 결정 권고 옵션 매트릭스 (§7) — **권고 자격 only, 결정 *고정* 0**
7. 정직성 한계 (§8)
8. 차단 조건 (§9)

### 하지 않는 것 (영구 답습)

- ❌ **MVP-1 합의 본문 (`3plus1-consensus-2026-05-22-jarvis-mvp1-local-boss.md`) 자동 정정** — R4·C-2 진술의 검증 자격 평가 *입력* 자격만, 본문 수정은 합의 *후* 별도 cycle
- ❌ **헌법 본문 자동 정정** — 5조 동형 매핑·8-2조 명시 적용 *해석* 입력만, 헌법 amendment 는 별도 단계
- ❌ **ADR-011 amendment 자동 발의** — §2.1 적용 자격 평가만, amendment 발의 = 본 cycle 명시 권고 *후* 사용자 명시 승인 *후* 별도 합의 cycle
- ❌ **M3 (추론 런타임) / M4 (tok/s threshold) 결정 *고정*** — Phase 1+2+3 evidence 정직성 한계 답습 (`jarvis-mvp1-v1-poc-findings.md` §3e.8)
- ❌ **trigger 발효** — 본 brief 의 어떤 옵션도 자동 실행되지 않는다 (옵션 매트릭스 = 사용자 명시 선택 의무)
- ❌ **메모리 `feedback_provider_liquidity` 본문 자동 정정** — 본 cycle 의 합의 결과가 메모리 갱신 자격을 가질 수 있으나, 자동 갱신 0건. 합의 *후* 별도 사용자 명시
- ❌ **Provider Liquidity 자체 약화** — 5 영구 핵심 제약 답습. 본 cycle = "범위 정의" / "충족 자격 평가" 이고 약화·폐기 0건
- ❌ **새 측정 실행 / 새 빌드 / 새 모델 다운로드** — 본 cycle = 합의 입력 deep-dive, 측정 = 별도 cycle
- ❌ **Phase 3 cycle 자체 진단 자격 재평가** — Phase 3 합의 (`e76acc8`) BLOCKING 7 은 *그 합의 산출*, 본 cycle 은 Phase 3 *후* finding deep-dive

---

## 1. 동기 (Why this cycle, Why now)

### 1.1 trigger — Phase 3 실 빌드 cycle (2026-05-24) finding

Phase 3 실 빌드 cycle (`7209743`) §2.5 분기 발동 = `missing tensor 'blk.0.ssm_dt.bias'` 즉시 실패. 원인 = **Ollama 보유 GGUF (`sha256-30e51a7c`, 오래된 conversion, `blk.X.ssm_dt` only) ≠ llama.cpp `c0c7e147` master 요구 format (`blk.X.ssm_dt.bias`, flag=0 required)**.

이는 단순한 빌드 실패가 아니다. **두 runtime 의 model loading 호환성이 GGUF format 변환 시점·버전에 의존한다** 는 사실의 강한 evidence — 즉 **"같은 모델을 다른 runtime 에 그대로 옮길 수 없다"**.

### 1.2 MVP-1 합의 R4 진술과의 긴장

MVP-1 합의 (2026-05-22) R4 본문:
> §6·M3 **llama.cpp ↔ Ollama 동급**, **vLLM "제외" → "MVP-2 재검토" 강등**(C-2 충돌)

근거 (design brief v2 §3 line 82·V1-4):
> OpenAI-호환 endpoint 로 통일: Ollama 는 `/v1/chat/completions` 제공 → 클라우드/타 로컬과 *동일 인터페이스*. provider 교체 = endpoint+model 문자열 교체(C-2 충족).

즉 MVP-1 합의는 **인터페이스 수준** 의 동급을 주장한다 — `/v1/chat/completions` API 가 동일하면 OllamaBoss ↔ LlamaCppBoss 가 코드 변경 없이 교체된다는 논리.

**Phase 3 finding 의 함의**: 인터페이스 동일 ≠ model loading 호환. 동일한 *모델 파일* 을 두 runtime 에서 동일하게 실행할 수 없으면, "교체"는 **인터페이스 자체만** 의 교체이고 **모델 파일은 각 runtime 별 별도 변환** 가 의무로 따라온다.

### 1.3 C-2 "Provider Liquidity 비협상" 진술 범위 평가 의무

MVP-1 design brief v2 §1 line 64 C-2:
> **Provider Liquidity (헌법 5조 비협상)**: Boss LLM = 교체 가능. 모델/런타임 = config, 하드코딩 금지

`feedback_provider_liquidity` 메모리 본문:
> 어떤 모델, 구독, 오케스트레이터에도 락인되지 않아야 하며, 교체가 **코드 변경 없이** 가능해야 한다.

**평가 의무**: "코드 변경 없이" 의 범위 = (a) Python 코드만 vs (b) Python + config 파일만 vs (c) Python + config + 모델 파일 동일 vs (d) Python + config + 모델 파일 + 호환성 보장 conversion script 자체 동일. Phase 3 finding 은 (c)~(d) 가 *부분 거짓* 임을 드러낸다.

### 1.4 헌법 본문 정확 매핑 — 5조 동형 vs 8-2조 직접 적용

헌법 본문 grep 결과 (`docs/constitution/PROJECT_CONSTITUTION.md`):
- **제5조 코드 품질 원칙** (line 40~46): SRP·중복 제거·외부 입력 검증·린터 — **Provider Liquidity 와 직접 무관**
- **제8-2조 환경 관리 원칙** (line 67~73): **"하드코딩 제로: 포트, URL, 모델명 등 모든 설정값은 환경 변수로 관리"** — **Provider Liquidity 의 직접 모법**

`feedback_provider_liquidity` 메모리 + MVP-1 design brief v2 line 41 line 64 의 "헌법 5조" 표현 = **동형 해석**. 헌법 본문 자체는 8-2조에 더 정확히 매핑된다. 본 cycle 의 진단 의무 1.

### 1.5 ADR-011 §2.1 means/ends 일반 원칙 적용 자격 평가

ADR-011 §6 line 212 명시:
> Provider Liquidity 영향 = 무관: 본 ADR은 redaction 수단 해석이며 모델/구독 교체 자유와 무관

ADR-011 *자체* 는 Provider Liquidity 의 직접 모법 아님. 그러나 §2.1 의 means/ends 일반 원칙 ((a)~(d) 4조건 + (e) 모법 인용) 은 본 cycle 의 추상 패턴으로 적용 가능 자격을 가진다.

- **means** (수단): GGUF format 변환, Ollama runner, llama.cpp 빌드, `/v1/chat/completions` endpoint
- **ends** (목적): Provider Liquidity = 모델·구독·오케스트레이터 교체 자유

Phase 3 finding 은 *means 의 호환성 부재* 가 *ends 달성 자격* 을 약화시킨다는 강한 evidence. ADR-011 §2.1 추상 패턴 답습 자격 평가 의무.

---

## 2. 분석 대상 evidence (Phase 1+1.5+2+3 통합)

### 2.1 Phase 1 (V-1 PoC Stage 1~4, 2026-05-23, `6b25453`)

| # | finding | 강도 | 본 cycle 입력 자격 |
|---|---|---|---|
| P1-F1 | `qwen3-coder-next` manifest = `general.architecture: qwen3next` + MoE (`expert_count: 512`, `expert_used_count: 10`) + hybrid SSM (`full_attention_interval: 4` = 48 레이어 중 12 full attn / 36 SSM) | 🟢 강한 | Provider Liquidity 평가 *전제* (model 구조 식별) |
| P1-F2 | `.capabilities: ["completion", "tools"]` 보고 | 🟢 강한 | endpoint 능력 수준 동급 입력 (OllamaBoss 가능성 확인) |
| P1-F3 | dense 4종 모델 `moe_fields = {}` empty 확인 (qwen2.5-coder:32b·llama3.3:70b·exaone3.5:32b·exaone4:32b) | 🟢 강한 | baseline 비교 자격 확정 |
| P1-F4 | `/v1/chat/completions` 추상 가능성 = manifest `tools` 능력 보고로 *인터페이스* 수준 시사 (실 endpoint 거부/수용 binary 미검증) | 🟡 가설 | MVP-1 R4 "동급" 의 인터페이스 수준 진술 근거 |

### 2.2 Phase 1.5 (Stage 5 = Phase 1 cycle, 2026-05-24 새벽, finding 통합)

| # | finding | 강도 | 본 cycle 입력 자격 |
|---|---|---|---|
| P1.5-F1 | SSM state cache reuse 불가 강한 evidence (H-B1) — prefill warm 시점도 27초 prefill 잔존 = SSM state recomputation 본질적 cost | 🟢 강한 | 두 runtime 의 SSM cache 동작 비교 자격 (Ollama vs llama.cpp) |
| P1.5-F2 | dense ≫ MoE+SSM warm cache 90× 역전 (qwen2.5-coder:32b warm = ~8290 / qwen3-coder-next warm = 91.58) | 🟢 강한 | "동급" 진술 적용 시 runtime 별 cache 구현 차이 → Provider Liquidity 평가 입력 |
| P1.5-F3 | MVP-1 advisory 패턴 production 영향 — system_prompt cache hit ratio 손실 → wall-clock 측정 필수 (합의 R-12 답습) | 🟢 강한 | M3 결정 입력 — 본 cycle 직접 모법 아니나 후속 영향 |

### 2.3 Phase 2 (HF egress cycle, 2026-05-24 새벽, `c66756b`)

| # | finding | 강도 | 본 cycle 입력 자격 |
|---|---|---|---|
| P2-F1 | F1 가설 (i) "활성 ~3B 가정" → **부정 강화** (HF 카드 verbatim "3B activated" 4중 cross-check) | 🟢 강한 | model 식별 정확성 (Provider Liquidity 평가 *전제*) |
| P2-F2 | F1 가설 (ii) architecture = **Gated DeltaNet linear attention** (NOT classical SSM/Mamba) — **M3 결정 문구 수정 의무** | 🟢 강한 | model 분류 명명법 정정 — Provider Liquidity "동급" 진술 적용 시 architecture family 정확 식별 자격 |
| P2-F3 | F1 가설 (v) GB10/Ollama effective BW spec 1/3 (~85 GB/s) 강한 evidence | 🟢 강한 | runtime 의 BW 활용도 차이 입력 (Ollama 31% vs llama.cpp 미측정) |

### 2.4 Phase 3 (실 빌드 cycle, 2026-05-24, `7209743`)

| # | finding | 강도 | 본 cycle 입력 자격 |
|---|---|---|---|
| P3-F1 ⭐ | **GGUF format 호환성 부재** — Ollama `sha256-30e51a7c` (`blk.X.ssm_dt` only) ≠ llama.cpp `c0c7e147` master (`.ssm_dt.bias` flag=0 required, conversion/qwen.py:299 새 형식 `.dt_proj.bias` rename) | 🟢 강한 | 🎯 본 cycle 의 trigger finding |
| P3-F2 | sm_120a + sm_121a SASS 모두 포함 verbatim (cuobjdump libggml-cuda.so.0.12.0 102MB) — 가설 #6 sm_120/121 미지원 *후보 약화* | 🟢 강한 | 빌드 자격 확정 (격리 변수 분리) |
| P3-F3 | R-1 anchor 누계 8회 일치 확정 (Phase 1 5회 + Phase 3 시작·mid·end 3회) | 🟢 강한 | binary 식별 안정성 (Provider Liquidity 평가 시 runtime 식별 자격) |
| P3-F4 | Phase 1 prompt 정확 detokenize (GGUFReader + GPT-2 ByteLevel + Qwen3 chat template) — 4종 prompt text 보존 | 🟢 강한 | 후속 cycle 답습 자격 |
| P3-F5 | Ollama API `/api/show` FROM 경로 부정확 (`/root/.ollama/...` stale vs 실제 `/home/delangi/.../bootcamp_game/ollama-data/...`) | 🟡 추가 | runtime opacity 입력 |
| P3-F6 | Port 11434 listening = docker-proxy (pid 4218) — Ollama daemon (pid 3375) 가 Docker container 내 실행 가능성 시사 | 🟡 추가 | Ollama runtime 구조 opacity (Provider Liquidity 평가 시 runtime "교체" 의 의미 범위 입력) |
| P3-F7 | OLLAMA_KEEP_ALIVE=-1 무한 (`/proc env` verify) — 자연 idle 불가 → 측정 진입 시 명시 unload 의무 | 🟡 운영 | runtime 운영 모델 차이 입력 |

### 2.5 evidence 통합 요약

- **인터페이스 수준 (`/v1/chat/completions`)**: P1-F2 + P1-F4 → 두 runtime "동급" 가능성 시사 (실 검증 0). MVP-1 R4 진술 근거 약함 (manifest 보고 only, endpoint 실제 거부/수용 미검증).
- **model loading 수준**: P3-F1 → **부정** (GGUF format 호환성 부재 강한 evidence).
- **성능 수준 (BW·cache)**: P1.5-F1/F2/F3 + P2-F3 → runtime 별 implementation 차이 강한 시사. llama.cpp 동일 model 측정 0 (P3-F1 차단).
- **운영성 수준**: P3-F5/F6/F7 → runtime opacity 차이 ↑.

**핵심 함의**: MVP-1 R4 "동급" 진술은 **인터페이스 수준의 *후보* 동급** 까지만 정직하게 보장 가능. 그 이상 (model loading·성능·운영성) 의 동급 = Phase 1+1.5+2+3 evidence 로 *부정 강한* (model loading) ~ *미검증* (성능·운영성).

---

## 3. SDD 정합성 매트릭스

### 3.1 헌법 본문 정확 매핑

| 출처 표현 | 실제 헌법 매핑 | 정합성 |
|---|---|---|
| `feedback_provider_liquidity` 메모리: "코드 변경 없이 교체" | **8-2조** "하드코딩 제로: 포트, URL, 모델명 등 모든 설정값은 환경 변수로 관리" | 🟢 직접 일치 |
| MVP-1 design brief v2 line 41 "헌법 5조 동형" | 5조 = 코드 품질 (SRP·중복 제거·외부 입력 검증·린터) — **Provider Liquidity 와 직접 무관** | 🟡 동형 해석, 본문 직접 아님 |
| MVP-1 design brief v2 line 64 C-2 "Provider Liquidity (헌법 5조 비협상)" | 동상 | 🟡 동상 |

**진단**: 헌법 5조 매핑은 *동형 해석* (관행적 표현). 직접 매핑은 **8-2조** 가 더 정확. **본 cycle 진단 의무 1** — 메모리·MVP-1 합의 본문의 "헌법 5조" 표현이 정확한 매핑인지 평가, 정정 필요 시 권고 자격으로 명시 (자동 정정 0건).

### 3.2 MVP-1 합의 (2026-05-22) R4·C-2 진술 검증 자격

| 진술 | 검증 자격 | Phase 1+2+3 evidence |
|---|---|---|
| R4: llama.cpp ↔ Ollama **동급** | 인터페이스 수준 = 후보 (실 검증 0) / model loading = 부정 강한 / 성능 = 미검증 / 운영성 = 차이 강한 | P1-F2/F4 (인터페이스 가설) / P3-F1 (model loading 부정) / P1.5-F1/F2 (Ollama 측정만, llama.cpp 미측정) / P3-F5/F6/F7 (운영성) |
| C-2: 모델/런타임 = config, 하드코딩 금지 | Boss LLM 코드 추상 (Python) 수준 = MVP-0 트랙 A 구현으로 충족 / 모델 *파일* 수준 = 부정 강한 (GGUF format runtime 의존) | MVP-0 트랙 A `boss.py` (StubBoss·BossLLM Protocol 추상화) ✅ / P3-F1 ❌ |
| V1-4: `/v1/chat/completions` OpenAI-호환 확인 (Ollama·llama.cpp 둘 다) | Ollama 부분 확인 (manifest `tools` 능력) / llama.cpp 미확인 (V-1 PoC 미진입) | P1-F2 부분 / llama.cpp 측정 자격 = Phase 3 차단으로 부재 |

**진단**: MVP-1 R4 "동급" 진술은 **수준 분리 필요**. 본 cycle 의 후속 권고 옵션 매트릭스 (§7) 에서 진술 보강 후보 제시 의무.

### 3.3 ADR-011 §2.1 means/ends 일반 원칙 적용 자격

ADR-011 §6 = "Provider Liquidity 무관" 명시 → ADR-011 *자체* 는 모법 아님. **단 §2.1 (a)~(e) 5조건 추상 패턴** 은 본 cycle 답습 자격을 가진다 (다른 영역 적용 시 패턴 동형).

| (a)~(e) | ADR-011 본문 | 본 cycle 답습 시 의미 |
|---|---|---|
| (a) 대체 수단 동등 이상 비교표 | Hermes redaction ↔ R-2 trigger | OllamaBoss ↔ LlamaCppBoss 의 model loading·성능·운영성 비교표 (현재 부재) |
| (b) 외부 검증 (적대적 침투 시연 binary 등) | R-3 침투 시연 | "동급" 진술의 적대적 시연 (= 동일 모델 두 runtime 실행 — Phase 3 에서 차단됨) |
| (c) 회귀 보호 | R-5 canary 재검증 | runtime/모델 변경 시 회귀 검증 자격 (현재 부재) |
| (d) 자동 회귀 | R-6 CI 회귀 | CI 회귀 자격 (V-1 PoC 미진입) |
| (e) 모법 인용 | ADR-011 §2.1 자체 | 본 cycle 합의 결과의 모법화 자격 평가 |

**진단**: ADR-011 §2.1 적용 자격 = **본 cycle 의 합의 결과가 패턴 답습 가치를 가지는가** 의 평가. 합의 결과에 따라 (i) ADR-011 자체 amendment 발의 / (ii) 별도 ADR 신규 / (iii) MVP-1 합의 본문 보강 / (iv) DEFER 4 분기.

### 3.4 feedback_provider_liquidity 메모리 본문 정확성

| 메모리 진술 | 평가 |
|---|---|
| "어떤 모델, 구독, 오케스트레이터에도 락인되지 않아야 하며, 교체가 **코드 변경 없이** 가능해야 한다" | 🟢 원칙 정합 (헌법 8-2조 직접 매핑) — 단 "코드 변경 없이"의 *범위* 명시 부재 (모델 *파일* 변경 자격이 포함되는지 미정의) |
| "LLM provider 선택은 코드가 아닌 설정 파일(YAML 등)에서만" | 🟢 일치 — MVP-0 트랙 A 구현으로 충족 |
| "최소 2 provider always-on 원칙" | 🟡 부분 — MVP-0 = StubBoss 한정, 2 provider 실 always-on 미구현 (트랙 B 진입 후 평가) |
| "depcruise 또는 동등한 정적 검사로 분기 코드 패턴 강제 차단" | 🟡 부분 — `if model == ...` 패턴 정적 검사 미구현 |

**진단**: 메모리 본문은 원칙 수준 정합. 단 "범위 정의" 가 부재 = 본 cycle 의 합의 결과로 명문화 자격 (자동 갱신 0건).

---

## 4. 핵심 긴장 4축

### 4.1 축 1 — "동급" 진술의 수준 분리

**긴장**: MVP-1 R4 = "동급" 단일 진술. Phase 1+2+3 evidence = 4 수준 (인터페이스 / model loading / 성능 / 운영성) 각각 다른 자격. 단일 진술이 *어느 수준* 의 동급을 의미하는지 명시 부재 = 자의적 해석 risk.

**분석 자격**: 진술 수준 분리 의무 평가. (a) 진술 폐기 / (b) 진술 보강 (수준별 분리) / (c) 진술 유지 + 한계 명시 / (d) DEFER (V-1 PoC 완료까지) 4 분기.

### 4.2 축 2 — GGUF format = means or ends

**긴장**: GGUF format conversion script (`convert_hf_to_gguf.py`) = 수단 (means) 인가, Provider Liquidity 의 일부 (ends 자체 의무) 인가?

**case A (means)**: GGUF = runtime 별 means 의 하나. runtime 교체 시 conversion script 도 함께 교체 = 정상. ends (provider 교체 자유) 는 유지.
**case B (ends 일부)**: GGUF = "모델 파일 호환성" = Provider Liquidity 의 일부. 호환성 부재 = Provider Liquidity *부분 위배*.

**분석 자격**: ADR-011 §2.1 추상 패턴 답습 (a) 대체 수단 동등 이상 비교 → GGUF Ollama format vs llama.cpp format 동등성 평가. case A/B 선택은 합의 결과 입력 자격.

### 4.3 축 3 — "코드 변경 없이"의 범위 정의

**긴장**: `feedback_provider_liquidity` 메모리 "코드 변경 없이" 의 범위 = (a) Python 코드만 / (b) Python + config 파일만 / (c) Python + config + 모델 파일 동일 / (d) 추가로 conversion script 동일.

| 범위 | Phase 3 finding 적용 | 평가 |
|---|---|---|
| (a) Python 코드만 | MVP-0 트랙 A = ✅ 충족 (StubBoss·BossLLM Protocol) | 🟢 |
| (b) + config 파일만 | endpoint URL · model 문자열 = config 교체로 가능 | 🟢 (인터페이스 수준) |
| (c) + 모델 파일 동일 | 동일 GGUF 파일 두 runtime 동일 실행 = 부정 강한 (P3-F1) | ❌ |
| (d) + conversion script 동일 | 별도 평가 — runtime 별 conversion 자체가 호환성 의무 | 미평가 |

**분석 자격**: 범위 정의 = 본 cycle 의 권고 자격으로 합의 결과에 따라 명문화 (자동 0).

### 4.4 축 4 — runtime "교체"의 의미 범위

**긴장**: P3-F6 (docker-proxy 11434 listening, Ollama daemon Docker container 내 가능성) + P3-F5 (FROM 경로 stale) + P3-F7 (KEEP_ALIVE=-1 무한) = runtime opacity 차이 ↑. "runtime 교체" 가 (a) endpoint URL 교체만 / (b) daemon 재시작 / (c) docker container 교체 / (d) 다른 OS·하드웨어 stack 어디까지 의무 인가?

**분석 자격**: 운영성 수준 동급 평가. MVP-1 advisory 패턴 (boss 동일 system prompt) 에서 runtime 의 KV cache 동작·KEEP_ALIVE 차이 = production wall-clock 영향. 합의 R-12 (advisory wall-clock 측정 필수) 와 결합.

---

## 5. 3+1 합의 분담안

### 5.1 분담 구조 (CLAUDE.md §3 답습)

| 에이전트 | 관점 | 핵심 질문 | 출력 형식 |
|---|---|---|---|
| **Agent A** (구현 분석가) | "실제로 동작하는가? Phase 1+2+3 evidence 가 MVP-1 R4·C-2 진술과 정합한가?" | (Q-A1) §2 evidence 표의 각 finding 의 강도·해석 정확성 / (Q-A2) MVP-1 R4 "동급" 진술의 수준 분리 자격 / (Q-A3) GGUF format = means/ends 분류 자격 / (Q-A4) ADR-011 §2.1 (a)~(e) 답습 자격 평가 | BLOCKING/권고/NOTE 분류 + 본문 verbatim 인용 + 정직성 한계 |
| **Agent B** (품질·안전성 검증가) | "안전하고 견고한가? 거짓 안전감·anchor effect·자동 정정 risk 가 있는가?" | (Q-B1) 본 brief 의 진술 중 "헌법 5조"·"동급"·"코드 변경 없이" 등 anchor 표현이 거짓 안전감을 유발하는가 / (Q-B2) 메모리·MVP-1 합의·헌법 본문 자동 정정 risk 평가 / (Q-B3) 합의 결과의 결정 *고정* 자격 자제 검증 / (Q-B4) Provider Liquidity 자체 약화 risk 평가 | BLOCKING/권고/NOTE 분류 + 거짓 안전감 패턴 명시 |
| **Agent C** (대안 탐색가) | "더 나은 방법이 있는가? 본 cycle 의 분석 frame 자체에 누락이 있는가?" | (Q-C1) Phase 1+2+3 외 evidence 누락 자격 (Stage 2 후보 11종 404·HF community GGUF 등) / (Q-C2) "동급" 진술 외 대안 framing (예: "후보 동급 + 변환 의무 명문") / (Q-C3) LiteLLM 게이트웨이·다른 runtime (MLC-LLM·llamafile·ktransformers·exllamav2·vLLM·TensorRT-LLM) 입력 자격 / (Q-C4) "Provider Liquidity 의 layered 모델" framing (인터페이스/모델/성능/운영성 4-layer 명문화) | BLOCKING/권고/NOTE 분류 + 대안 옵션 별도 단독 발견 표시 |

### 5.2 분담 의무

- 3 에이전트 **병렬 독립** — 서로의 출력 참조 0건 (편향 방지, CLAUDE.md §3 Phase 2 답습)
- 본 brief 본문 + §1.4 선행 답습 8 문서 cross-check + Phase 3 raw 17 파일 + Phase 3 합의 보고서 본문 한정
- 새 측정·새 빌드·새 다운로드 = 0건 (본 brief §0.2 답습)
- M3·M4 결정 *고정* 0건 답습
- 메모리·헌법·MVP-1 합의 본문 자동 정정 0건 답습

### 5.3 Reviewer (검토 에이전트) 역할

- Agent A/B/C 3 출력 수집 → 교차 비교 → 일치(Consensus)/부분 일치(Partial)/불일치(Divergence)/누락(Gap) 분류
- Reviewer 가 **자체 발견** 추가 가능 (3 에이전트 누락 + Reviewer 의 직접 cross-check)
- 합의 결과 = BLOCKING (해소 필수) / 권고 (반영 권고, 사용자 명시) / NOTE (carry-over) / 기각 (근거 명시)
- Reviewer 정직성 명문 — 권한 한계 (본 cycle = 합의 입력, 결정 *고정* 자격 0, MVP-1 합의 본문 자동 정정 0)

---

## 6. 합의 출력 형식

### 6.1 분류

| 분류 | 의미 | 처리 |
|---|---|---|
| **BLOCKING** | 본 brief 진술의 사실 오류·거짓 안전감·anchor effect·논리 불일치 등 | brief v1.1 보강 시 verbatim 반영 의무 |
| **권고** | 본문 직접 반영 또는 NOTE carry-over 자격 | brief v1.1 또는 후속 cycle 입력 |
| **NOTE** | carry-over only, 본 cycle 후 별도 cycle 자격 | brief v1.1 §10 NOTE 표 carry-over |
| **기각** | 근거 명시 필수 (자동 기각 0건) | 합의 보고서에 verbatim 근거 |

### 6.2 합의 보고서 의무 사항

- 본 brief 본문 직접 grep cross-check (line 번호 인용 의무)
- Phase 1+1.5+2+3 evidence verbatim 인용 의무
- MVP-1 합의 R4·C-2 본문 verbatim 인용 의무
- 헌법 본문 5조·8-2조 verbatim 인용 의무
- ADR-011 §2.1 본문 verbatim 인용 의무
- citation stale 0 점검 (BI-3·BI-4·BI-5·BI-1 답습 — 3+1 후속 cycle 패턴)
- 3 에이전트 단독 발견 명시 (A-S·B-S·C-S 라벨 답습)
- Reviewer 직접 cross-check 시 line 번호 verbatim

---

## 7. 후속 결정 권고 옵션 매트릭스 (**권고 자격 only, 결정 *고정* 0**)

> 본 §7 = 합의 결과에 따라 사용자 명시 후 별도 cycle 진입 자격을 가지는 후보. 본 cycle 의 어떤 옵션도 자동 발효 0건.

### 7.1 진술·문서 보강 옵션 (낮은 위험, 권고 자격 강)

| 옵션 | 내용 | 발생 |
|---|---|---|
| **(A)** | MVP-1 합의 본문 R4 진술 수준 분리 보강 — "인터페이스 후보 동급 / 모델 loading 호환성 별도 / 성능 미검증 / 운영성 차이 ↑" 명문 | 합의 본문 보강 cycle (별도 brief + 단축 합의) |
| **(B)** | 메모리 `feedback_provider_liquidity` 본문 "범위 정의" 명문 — (a)~(d) 4 범위 + 본 프로젝트 채택 범위 명시 | 메모리 update (사용자 명시 후) |
| **(C)** | 헌법 5조 동형 매핑 → 8-2조 직접 매핑 정정 — MVP-1 design brief v2 + 메모리 표현 정정 | 문서 update (사용자 명시 후) |
| **(D)** | `Provider Liquidity 의 layered 모델` 신규 ADR — 인터페이스/모델/성능/운영성 4-layer 명문 + 각 layer 충족 자격 | 신규 ADR 발의 cycle (별도 brief + 풀 3+1) |

### 7.2 ADR-011 amendment 옵션 (중간 위험)

| 옵션 | 내용 | 발생 |
|---|---|---|
| **(E)** | ADR-011 §6 "Provider Liquidity 무관" 진술 정정 — §2.1 (a)~(e) 추상 패턴이 다른 영역 답습 자격 명문 | ADR amendment cycle (별도 brief + 풀 3+1, **헌법급 변경**) |
| **(F)** | ADR-011 amendment + §2.1 (a)~(e) 본 cycle 합의 결과 답습 시연 — OllamaBoss ↔ LlamaCppBoss 비교표 (a) / Phase 3 finding = (b) 적대적 시연 | ADR amendment cycle 본문 시연 자격 |

### 7.3 측정·실험 옵션 (높은 위험, V-1 PoC 답습)

| 옵션 | 내용 | 발생 |
|---|---|---|
| **(G)** | Phase 3.5 brief — HF community GGUF (`unsloth/bartowski Qwen3-Next-80B-A3B-Q4_K_M`) 다운로드 → llama.cpp 재시도 | egress ~50GB, 디스크 +50GB, 별도 brief + 풀 3+1 |
| **(H)** | Phase 3.5 brief — Qwen3-30B-A3B 대조군 (classical MoE + dense, SSM 미포함, `LLM_ARCH_QWEN3MOE` = GGUF format 호환성 격차 X) | 측정 자격, 변수 분리 강화 |
| **(I)** | llama.cpp 이전 commit checkout (`.ssm_dt.bias` optional 였던 시점) + 재빌드 | 측정 *후* MVP-1 R4 진술 보강 입력 자격 |
| **(J)** | LiteLLM 게이트웨이 PoC — 다중 provider 라우팅·fallback 의 진화 경로 (MVP-2) | 별도 cycle, MVP-2 진입 자격 |
| **(K)** | 다른 inference engine 외부 식별 cycle — MLC-LLM·llamafile·ktransformers·exllamav2·vLLM·TensorRT-LLM. Provider Liquidity 답습 강화 | 별도 brief |

### 7.4 DEFER 옵션

| 옵션 | 내용 | 발생 |
|---|---|---|
| **(L)** | 본 cycle = 합의·보고서 작성 + brief v1.1 보강 + commit + push → 후속 모두 DEFER | 별도 cycle 자격, MVP-1 트랙 B 진입 *전* 본 합의 결과 반드시 답습 |
| **(M)** | 본 cycle = 진단까지만, 권고 옵션 매트릭스 전체 DEFER (사용자 권고 자격 약화 시) | 합의 본문 단순화 |

### 7.5 옵션 매트릭스 적용 의무

- 합의 결과에 따라 옵션 (A)~(M) 중 일부가 권고 자격, 일부가 NOTE carry-over, 일부가 기각
- **결정 *고정* 0건** — 본 cycle 의 어떤 옵션도 자동 발효 0건
- 사용자 명시 승인 후 별도 cycle 자격

---

## 8. 정직성 한계

1. **본 brief 의 어떤 §도 결정 *고정* 자격 X** — Phase 1+2+3 evidence 정직성 한계 답습 (`jarvis-mvp1-v1-poc-findings.md` §3e.8 + §4 17 한계 답습).
2. **새 측정·새 빌드·새 다운로드 = 0건** — 본 cycle = 합의 입력 deep-dive.
3. **MVP-1 합의 본문 자동 정정 = 0건** — R4·C-2 본문은 합의 *결과* 에 따라 별도 cycle 에서 정정 자격.
4. **헌법 본문 자동 정정 = 0건** — 5조 동형 매핑 정정도 사용자 명시 후 별도 cycle.
5. **ADR-011 amendment 자동 발의 = 0건** — §2.1 적용 자격 평가 → 합의 결과에 따라 별도 cycle.
6. **메모리 자동 갱신 = 0건** — `feedback_provider_liquidity` 본문 범위 명문도 사용자 명시 후.
7. **`/v1/chat/completions` 인터페이스 동급 = 실 검증 0** (P1-F2 = manifest 능력 보고만, endpoint 실제 거부/수용 binary 미검증).
8. **llama.cpp 측정 자격 = 부재** (Phase 3 GGUF 차단으로 0건).
9. **Phase 3 finding 의 일반화 자격 한정** — 1 모델 (qwen3-coder-next) + 2 runtime (Ollama·llama.cpp) + 1 시점 (2026-05-24, llama.cpp `c0c7e147`) 측정. 다른 모델·다른 runtime·다른 시점 일반화 = 별도 cycle.
10. **"동급" 진술의 수준 분리 자체가 anchor effect risk** — 4 수준 (인터페이스/모델/성능/운영성) 분류 자체가 본 brief 의 framing 이고 다른 framing 가능 (Agent C 의무).
11. **본 brief 의 SDD 정합성 평가 = 본 cycle 시점 한정** — 메모리·MVP-1 합의·헌법·ADR-011 본문이 본 cycle 후 변경되면 본 brief 진술 자격 재평가 의무.
12. **Reviewer 권한 한계** — 본 brief = 합의 cycle entry brief 자격, 합의 *결과* 가 본 brief 의 진술을 BLOCKING 으로 정정할 가능성. 자동 정정 0건.

---

## 9. 차단 조건

### 9.1 본 cycle 진입 *전* 차단 조건 (사용자 명시 의무)

- [x] 분석 대상 범위 = Phase 1+1.5+2+3 통합 (사용자 명시 ✅)
- [x] 권고 자격 = 진단 + 권고 옵션 매트릭스 (사용자 명시 ✅, 결정 *고정* 0 답습)
- [x] 단계별 명시 승인 패턴 답습 (`feedback_staged_consensus_workflow`)

### 9.2 본 cycle 진행 중 차단 조건

- 본 brief v1 작성 *후* 사용자 검토·승인 → commit·push (별도 명시) → 풀 3+1 합의 (별도 명시) → brief v1.1 보강 → 세션 정리. 자동 다음 단계 진입 0건.
- 합의 진입 *전* 사용자 명시 의무 — 3 에이전트 병렬 독립 시작 = 사용자 명시 받은 후만.
- 합의 결과에 따라 후속 옵션 (A)~(M) 자동 발효 0건 — 사용자 명시 받은 후만 별도 cycle.

### 9.3 본 cycle 종료 후 차단 조건

- 합의 BLOCKING 이 brief v1.1 반영 *전* 본 cycle 종료 = 차단.
- M3·M4 결정 *고정* 자동 진입 = 차단 (별도 합의 cycle 의무).
- 메모리·헌법·MVP-1 합의·ADR-011 본문 자동 정정 = 차단 (사용자 명시 후 별도 cycle).

---

## 10. NOTE carry-over (본 cycle 미해소, 후속 cycle 자격)

| # | NOTE | carry-over 자격 |
|---|---|---|
| N-1 | Phase 1+1.5+2+3 외 evidence 누락 자격 (Stage 2 후보 11종 404 → Ollama Hub `ollama search` egress 별도 cycle 필요) | Phase 3.5+ |
| N-2 | LiteLLM 게이트웨이 PoC 자격 (MVP-2 진입 시) | MVP-2 cycle |
| N-3 | 다른 inference engine (MLC-LLM 등) 외부 식별 cycle | 별도 brief |
| N-4 | OllamaBoss·LlamaCppBoss 코드 0건 답습 (MVP-1 트랙 B 진입 전) | 트랙 B cycle |
| N-5 | Provider Liquidity layered 모델 (4-layer 명문 ADR) 발의 자격 | Agent C 권고 시 별도 cycle |
| N-6 | ADR-011 §6 "Provider Liquidity 무관" 진술 정정 자격 | 헌법급 변경, 별도 합의 cycle |
| N-7 | 메모리 `feedback_provider_liquidity` 본문 범위 명문 자격 | 합의 결과에 따라 사용자 명시 후 |
| N-8 | 헌법 5조 동형 매핑 → 8-2조 직접 매핑 정정 자격 | 합의 결과에 따라 |
| N-9 | MVP-1 합의 R4 진술 수준 분리 보강 자격 | 합의 결과에 따라 |
| N-10 | depcruise 정적 검사 자격 (`if model == ...` 패턴 차단) | MVP-1 트랙 B 진입 후 |
| N-11 | 2 provider always-on 원칙 실 구현 자격 | 트랙 B cycle |

---

## 11. 다음 단계 (자동 진입 0건, 사용자 명시 의무)

- (1) **사용자 brief 검토** — 본 brief v1 본문 검토 후 commit·push 명시 또는 보강 요청
- (2) **brief v1 commit + push** (사용자 명시 후) — `feature/jarvis-mvp0` 브랜치, conventional commit (`docs(phase0): Provider Liquidity deep-dive 합의 entry brief v1`)
- (3) **풀 3+1 합의 진입** (사용자 별도 명시 후) — Agent A/B/C 병렬 독립 → Reviewer 통합
- (4) **brief v1.1 보강** — 합의 BLOCKING verbatim + 권고 본문 직접 반영 (NOTE carry-over only)
- (5) **세션 정리** — SESSION_2026-05-24.md update + CONTEXT.md + INDEX.md
- (6) **commit + push** (사용자 별도 명시)

---

**출처**: 위 §1.4 답습 8 문서 + Phase 3 raw 17 파일 + 헌법·ADR-011·메모리 4건.

**답습**: `project_jarvis_local_boss_direction` / `feedback_provider_liquidity` / `feedback_proportionate_security_personal_tool` / `feedback_staged_consensus_workflow` / `project_minimize_user_intervention`.

**금지 (영구 답습, 본 brief 0건)**: MVP-1 합의 본문 자동 정정 / 헌법 본문 자동 정정 / ADR-011 amendment 자동 발의 / 메모리 자동 갱신 / M3·M4 결정 *고정* / 측정·빌드·다운로드 / Provider Liquidity 자체 약화 / commit·push (별도 단계) / 보안 거버넌스 자동 재개.
