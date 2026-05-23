# 자비스 MVP-1 V-1 PoC Phase 2 cycle entry brief (v2 EXECUTED)

> **본 brief = M3·M4 합의 §5.2 Phase 2 cycle (C-a 활성 파라미터 정량 HF egress) 실행 절차 + 실행 결과.** §1~§8 = v1 시점 계획 (불변 보존), §9 = v2 시점 실행 결과 (cycle 후 추가). brief 자체로 commit·push 0건 (사용자 명시 별도).

---

**작성일**: 2026-05-23 (v1 plan) → 2026-05-23 23:46 KST (v2 cycle 실행 완료)
**Status**: **v2 EXECUTED** (사용자 검토 대기, commit 0건). §1~§8 = v1 계획 (불변), §9 = Phase 2 cycle 실행 결과 raw. M3·M4 합의 §5.2 + R-5 BLOCKING + R-6·R-10·R-11·R-15·R-17 답습. HF egress §9.2 실행 윈도 ~10분 10초 (2026-05-23T23:36:42 ~ 23:46:52 KST). LLM 호출 0.
**진입 단위**: V-1 PoC Phase 1 cycle 완료 (`9c6b578`) 후 → **Phase 2 cycle 운영 entry**
**cycle 자격 근거**: `3plus1-consensus-2026-05-23-jarvis-mvp1-m3-m4-decision.md` §5.2 (Phase 2 = C-a 활성 파라미터 정량 HF egress, ~30분, 별도 명시 승인) + §4.3 (Phase 1 우선 → Phase 2 → Phase 3) + R-5 BLOCKING (F1/F2 검증 cycle 우선순위 명문)
**선행 답습**: V-1 entry brief v1.1 §8 (텔레메트리·egress 위생, R-3·R-11) / Phase 1 결과 `2026-05-24-phase1-summary.json` / Stage 1 결과 `qwen3-coder-next` manifest (`expert_count: 512`, `expert_used_count: 10`, `general.parameter_count: 79.7B`, family `qwen3next`, hybrid SSM `full_attention_interval: 4`)
**답습 권위 한계**: 본 brief = *Phase 2 cycle 운영화 entry* DRAFT — M3·M4 결정 *고정* / OllamaBoss 코드 / setup 변경 / 합의 보고서 작성 / gap-pull 실행 = 별도 단계 (사용자 명시).

---

## 0. 범위

### 0.1 사용자 진입 명령 답습 (2026-05-23)

> "c 로 진행해주세요" — 직전 세션 정리의 후보 (c) Phase 2 cycle = **C-a 활성 파라미터 정량 HF egress** (~30분, R-11 답습 + §8 baseline 시점 포함 의무) 선택. F1 가설 (i) 활성 ~3B vs ~62B 분리 = 직접 답 목표.

### 0.2 본 brief 가 *하는* 것 / *하지 않는* 것

- **하는 것**:
  1. Phase 2 cycle 의 *실행 절차* 운영화 (§2)
  2. HF egress 시점·범위·종료 보장 정의 (§3)
  3. §8 baseline 점검 절차 (egress 직전·직후, §4)
  4. 보고 항목 정의 — raw 한정, PASS/FAIL framing 금지 (§5)
  5. 정직성 한계 식별 (§6)

- **하지 않는 것 (M3·M4 합의 §5.4 + 본 brief 영구 답습)**:
  - ❌ HF 페이지 *실 fetch* (본 brief = 절차 식별만)
  - ❌ Ollama 데몬 재시작·kill·signal (R-1 답습)
  - ❌ 신규 모델 *pull* (HF read-only 페이지 조회만, ollama pull egress 별개)
  - ❌ Ollama config 변경 (`OLLAMA_*` env 영구 설정 X)
  - ❌ M3·M4 결정 *고정* (Phase 2 raw 보고만, 결정은 Phase 1+2 종합 후 별도 합의)
  - ❌ `OllamaBoss` 코드 작성 (트랙 B = Phase 3 이후 별도)
  - ❌ gap-pull *실행* (Phase 2 결과 입력 후 별도 명시 승인 — R-15)
  - ❌ 합의 보고서·commit·push (Phase 2 raw → findings → 별도 합의)
  - ❌ 보안 거버넌스 (credential·4축·BI-*) 자동 재개

### 0.3 비례성 답습

본 cycle = 본인용 개인 개발 툴의 read-only HF 페이지 조회 한정 (~30분). `feedback_proportionate_security_personal_tool` 답습 — HF egress 자체는 일상적 모델 카드 열람 수준의 정상 행위. egress *발생 자체* 의 위생 점검 (R-11 답습) 은 *측정 정직성* 입력 목적 (예: baseline 시점 trace 분리), 보안 거버넌스 자동 재개 trigger 아님.

---

## 1. Phase 2 cycle 목적

### 1.1 F1 가설 (i) 직접 답

**F1 가설** (M3·M4 합의 §2 의외 발견 + brief §2): qwen3-coder-next decode 7.83 tok/s = roofline 90~120 tok/s 대비 7~9% (외부 실측 ~31 tok/s 대비 25%). 가설 5종:
- (i) **활성 파라미터가 가정 ~3B 초과 — 실제 ~10B+ 가능성**
- (ii) SSM state 메모리 압박 (KV cache 와 별도)
- (iii) Ollama 0.20.4 hybrid 구현 효율성 (vs llama.cpp)
- (iv) Qwen3-Next router/gating overhead
- (v) **GB10/Ollama effective BW 자체가 spec 273GB/s 의 1/3 (~85GB/s) — Phase 1 A-진단 + dense qwen2.5 측정 역산 강한 evidence**

본 Phase 2 = **가설 (i) 직접 답** — Qwen3-Next-80B-A3B-Instruct (또는 본 환경 `qwen3-coder-next:latest` 의 원본 HF 모델) 의 모델 카드에서 활성 파라미터 정량.

### 1.2 부차 목적 (R-10 + R-15 답습)

- **R-10 답습**: Agent A 의 manifest 산정 ~4.3B (lower-bound) 와 HF 모델 카드의 공식 표기 일치 여부 검증
- **R-15 답습**: gap-pull 후보 8종 (V-1 entry brief §3.2 Step 2a) 의 활성 파라미터 정량 → 디스크 가드 ≤ 50GB + 활성 ~3B + Q4 ≤ 20GB 우선 의 *옵션 평가 입력*. 본 Phase 2 = 정량만, gap-pull 실 trigger 0
- **R-17 답습**: `attention.head_count_kv: null` 의미 — GQA 적용 여부를 HF config 의 `num_key_value_heads` 또는 모델 카드 architecture 설명에서 확인

### 1.3 Phase 2 단독 자격 한계

- 본 cycle 결과만으로 M3·M4 결정 *고정* 자격 X (M3·M4 합의 §4.4 답습)
- 가설 (i) 답 후에도 가설 (iii) (Ollama vs llama.cpp 효율) = Phase 3 C-e 필요
- F2 (cache 역전) 영향 = Phase 1 결과로 충분, Phase 2 추가 입력 0건

---

## 2. C-a 실행 절차

### 2.1 사전 점검 (HF egress *전*, read-only, ~5분)

| Step | 명령 / 행위 | 산출물 | 성공기준 |
|----|----|----|----|
| 1 | R-1 anchor 6회차 — `sudo sha256sum /proc/3375/exe` (사용자 명시 prompt 1회) | hash | Phase 1 hash `ce95c475...878b10` 와 일치 (silent 교체 미발생 재확인) |
| 2 | §8 baseline — `ss -tnp \| grep -E 'ESTAB' \| grep -v -E '127\.0\.0\.1\|::1'` | 외부 ESTABLISHED 목록 | 사전 baseline 으로 보존 (cycle 후 비교용). huggingface.co 도메인 0건 확인 |
| 3 | `/api/show` modelfile 조회 — `curl -s http://127.0.0.1:11434/api/show -d '{"name":"qwen3-coder-next:latest"}' \| jq '.modelfile, .details, .model_info \| keys'` (egress 0, localhost) | modelfile + 메타 키 | 모델 source URL / Modelfile FROM 행 / HF source 식별 정보 추출 (egress 0 read-only) |
| 4 | R-23 환경 동결 점검 — `ps -ef \| grep -E 'claude\|ollama' \| grep -v grep` + `top -bn1 \| head -10` | 프로세스·CPU 상태 | 본 Claude 세션 only + 다른 GPU heavy 작업 0 (Phase 1 동결 답습) |

### 2.2 C-a HF 페이지 조회 (egress 발생, ~20분)

| Step | 행위 | 명령 / 도구 | egress |
|----|----|----|----|
| **1** | **1차 후보 HF 모델 카드 조회** — Qwen3-Next 계열 (본 환경 `qwen3-coder-next:latest` 원본 후보) | `WebFetch` 도구 → `https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct` (M3·M4 §5.2 추정 URL) + `https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Thinking` (대안) + `config.json` 직접 조회 | huggingface.co 도메인만 |
| **2** | **부차 후보 모델 카드 조회 (R-15 답습)** — Step 2a 후보 8종 中 활성 파라미터 정량 가능 후보 | `WebFetch` → `Qwen3.5-A3B-Instruct` / `Qwen3.5-Coder-A10B` / `DeepSeek-V3.1-Lite` / `GLM-4-MoE` / `Granite-3.5-MoE` / `OLMoE` (각각 HF 검색 페이지·모델 카드 조회) | huggingface.co 도메인만 |
| 3 | 각 모델의 **config.json 활성 파라미터 산정 입력 필드** 추출 | `num_experts` / `num_experts_per_tok` / `hidden_size` / `intermediate_size` / `num_hidden_layers` / `num_key_value_heads` / `attention.full_attention_interval` (Qwen3-Next) | (Step 1·2 응답 본문 한정, 추가 egress 0) |
| 4 | (선택) **Qwen3-Next 공식 블로그 / paper 활성 파라미터 표기** 조회 | `WebSearch` "Qwen3-Next 80B activated parameters" 또는 `WebFetch` qwenlm.github.io / arxiv | huggingface.co 외 도메인 발생 시 → §3.2 격리 분리 보고 |

### 2.3 종료 보장 + §8 cycle-후 baseline (~5분)

| Step | 명령 | 성공기준 |
|----|----|----|
| 1 | `ss -tnp \| grep -E 'ESTAB' \| grep -E 'huggingface\|cloudfront'` | huggingface.co / CloudFront ESTABLISHED 0건 (모든 connection close) |
| 2 | R-1 anchor 7회차 (Phase 2 직후) | Phase 1 hash 와 일치 |
| 3 | R-23 환경 동결 사후 — 본 Claude 세션 only 유지 + CPU/GPU baseline | 측정 직전과 동일 |
| 4 | Ollama egress 0 재확인 — `ss -tnp \| grep ollama` | localhost only (Ollama 자체는 외부 egress 0 유지, 텔레메트리 별개 시점은 R-3 답습 한계 명시) |

### 2.4 실패 분기 (fail-closed, advisory 진행 금지)

| 분기 | 조건 | 대응 |
|----|----|----|
| **HF 502/503/timeout** | WebFetch 응답 5xx 또는 30초 timeout | 1회 재시도 → 재실패 시 cycle 중단 + 사용자 보고. 부분 raw 보고 금지 |
| **huggingface.co 외 도메인 egress** | §2.3 Step 1 점검에 다른 도메인 ESTABLISHED | cycle raw 의 §3.2 격리 trace 에 기록 + 사용자 보고. M3·M4 결정 입력 자격 평가 별도 |
| **R-1 hash 불일치** | §2.1 Step 1 또는 §2.3 Step 2 의 sha256sum 변동 | cycle 전체 폐기 + V-1 entry brief §12 옵션 E trigger 강도 ↑ 보고 |
| **HF 모델 카드 활성 파라미터 미표기** | 1차 후보 모델 카드 본문에 activated_params 또는 동등 정량 표기 0 | NOTE 처리 + config.json 직접 산정 + 산정 한계 명시 (가설 (i) "직접 답" 강도 ↓) |

---

## 3. §8 baseline + egress 시점 격리 (R-11 답습)

### 3.1 시점 범위 명문 (V-1 entry brief §8.1 R-3 답습)

- **본 cycle 의 HF egress = §2.2 Step 1~4 실행 윈도 한정**
- baseline 시점 = (a) §2.1 Step 2 (cycle 직전 snapshot) + (b) §2.3 Step 1 (cycle 직후 snapshot)
- **Ollama 자체 egress = 본 cycle 한정 0 검증** (텔레메트리·lazy upload 등 데몬 lifetime 전체 egress = R-11b 별도 cycle 답습)

### 3.2 격리 분리 보고 (egress 발생 *기록* 의무)

cycle 종료 후 raw 에 다음 분리 보고:

| 카테고리 | 보고 항목 |
|----|----|
| **본 cycle 의도 egress** | huggingface.co + CloudFront (HF CDN, 모델 카드 응답) ESTABLISHED 횟수·peak 동시 연결 수 |
| **본 cycle 의도 외 egress** | 예: Qwen 공식 블로그 (qwenlm.github.io) / arxiv 등 §2.2 Step 4 의 의도된 검색 응답이라도 별도 도메인 |
| **Ollama egress** | localhost only 유지 검증 (외부 도메인 0) |
| **다른 프로세스 egress** | claude (본 세션 Anthropic API + GCP) / sshd / tailscaled — 본 cycle 무관 baseline (Phase 1 §8.1 답습) |

본 분리 = "egress 0 검증" 의 *cycle 의도* vs *외부 의도* 격리. 거짓 안전감 차단 (B-F3 답습).

---

## 4. 보고 항목 (raw 한정, R-6 답습)

🔴 **R-6 답습**: PASS/FAIL framing 금지. raw 보고만.

### 4.1 1차 후보 (Qwen3-Next 계열) — F1 가설 (i) 직접 답 입력

| 항목 | 출처 |
|----|----|
| 총 파라미터 수 | HF 모델 카드 + config.json `num_parameters` 또는 model card text |
| **활성 파라미터 수 (activated_params)** | HF 모델 카드 표기 — 모델 카드 본문 / Modelcard YAML `tags` 또는 `parameters.activated` |
| expert 수 (total) | config.json `num_experts` (manifest `expert_count: 512` 와 일치 확인) |
| expert 활성 수 (top-k) | config.json `num_experts_per_tok` (manifest `expert_used_count: 10` 와 일치 확인) |
| hidden_size · intermediate_size · num_hidden_layers | config.json (Agent A 산정 보정 재계산 입력) |
| GQA 여부 + KV heads | config.json `num_key_value_heads` (R-17 답습) |
| SSM 구조 (Qwen3-Next 한정) | config.json `full_attention_interval` (manifest `4` 와 일치 확인) + `ssm_*` 필드 |
| Q4_K_M 양자화 후 GGUF 크기 | HF Quantization repo (해당 시) 또는 `ollama show` 의 51.7GB 와 비교 |

### 4.2 부차 후보 (8종) — R-15 gap-pull 옵션 평가 입력

| 항목 | 형식 |
|----|----|
| 후보별 활성 파라미터 | 표 (8 row × {총·활성·expert 수·top-k·SSM/dense·Q4 추정 크기}) |
| 활성 ≤ 10B + Q4 ≤ 20GB 충족 후보 | filtering 결과 (목록만, gap-pull 결정 입력 0) |
| 본 환경 부재 검증 | V-1 entry §3.2 Step 2b 답습 (`/api/show` HTTP 404 재확인 → egress 0) — Phase 2 *부산물*, 단독 trigger 0 |

### 4.3 Agent A 산정 ~4.3B 와 HF 표기 비교 (R-10 답습)

| 항목 | 비교 |
|----|----|
| Agent A manifest 산정 | ~4.3B (lower-bound, 보정 4종 모두 격차 ↑ 방향) |
| HF 공식 표기 | (조회 결과 입력) |
| 정합 / 격차 | 일치 시 가설 (i) 약화 ↑ / 큰 격차 시 가설 (i) 강화. **결정 *고정* 아님, raw 보고만** |

### 4.4 raw 보존 (R-22 답습)

| 항목 | 경로 |
|----|----|
| HF 응답 본문 + 메타 | `docs/phase0/v1-poc-raw/2026-05-2X-phase2-ca-<model-slug>-modelcard.json` (응답 + 조회 timestamp + URL + status) |
| baseline 전/후 snapshot | `docs/phase0/v1-poc-raw/2026-05-2X-phase2-egress-baseline-{pre,post}.json` |
| Phase 2 종합 | `docs/phase0/v1-poc-raw/2026-05-2X-phase2-summary.json` (1차 + 부차 후보 + Agent A 비교 + 정직성 한계) |

---

## 5. 정직성 한계 (R-6·B-F13 답습)

| 한계 | 영향 |
|----|----|
| **HF 모델 카드 = 원저자 표기 신뢰 한정** | 모델 카드 자체의 정확성·일관성 검증 별도 (원저자 fork·재공개 가능). gap-pull 후보 평가 시 모델 카드 변동 가능성 NOTE |
| **"활성 파라미터" 정의 변동** | 모델 카드마다 router/gating params 포함 여부·attention proj 정의 다를 수 있음. Agent A 산정과 다른 산정 방식 비교 시 한계 명시 |
| **본 환경 `qwen3-coder-next:latest` ↔ HF 원본 매핑** | Ollama 의 tag 가 정확히 어느 HF model 의 GGUF 변환인지 직접 매핑 검증 불가 (modelfile FROM 행 또는 source 표기 의존). 매핑 자체가 모호 시 가설 (i) 답 강도 ↓ |
| **HF egress 시점 한정** | 본 cycle 윈도 한정 검증. HF / CloudFront 의 텔레메트리·캐시 정책은 본 cycle 범위 밖 (R-3 답습) |
| **R-23 동결 한계** | 본 cycle 진행 중 다른 Claude 세션 호출 0 가정 (사용자 책임). HF egress 자체는 본 Claude 세션의 WebFetch 사용 → 본 세션 외부 connection 증가 1건 명문 |
| **Phase 2 단독 자격** | 가설 (i) 답 → M3·M4 결정 *입력* 한정. *결정 고정* = Phase 1+2 종합 후 별도 합의 (M3·M4 합의 §4.4) |
| **Ollama prefix cache 영향 0 검증 불가** | Phase 2 = LLM 호출 0, Ollama 데몬 상호작용 0 → cache 영향 없음 명문 |

---

## 6. 다음 단계 (사용자 결정 — 자동 진입 0건)

| 옵션 | 내용 | 자격 |
|----|----|----|
| (A) | 본 brief 사용자 검토 → Phase 2 cycle 실행 명시 승인 → §2.1~§2.3 진행 | brief v1 commit 별도 / 또는 brief 검토 후 곧장 실행 |
| (B) | brief 보강 (누락 항목·절차 정밀화) | brief v2 → 재검토 |
| (C) | Phase 2 cycle 실행 후 → Phase 2 findings (`docs/phase0/jarvis-mvp1-v1-poc-phase2-findings.md` 또는 v1-poc-findings.md 부록) | findings 작성 별도 명시 |
| (D) | Phase 2 결과 후 → Phase 3 진입 (C-e llama.cpp 빌드·측정) | 별도 brief + 사용자 명시 (M3·M4 §5.3) |
| (E) | Phase 2 결과 후 → M3·M4 *결정 고정* 합의 cycle (Phase 1+2 결과 종합) | 별도 합의 brief + 사용자 명시 (M3·M4 §4.4) |
| (F) | Phase 2 결과 후 → gap-pull 별도 명시 승인 (R-15 답습) | 별도 brief — 디스크 가드 + egress 명시 + raw 보존 |

**보안 거버넌스 자동 재개 금지** (비례성, `feedback_proportionate_security_personal_tool` 답습).

**단계별 명시 승인 답습** (`feedback_staged_consensus_workflow`): brief → 사용자 승인 → 실행 → findings → commit → push, 자동 다음 단계 진입 0건.

---

## 7. 산출물 (계획)

본 brief commit 시:
- `docs/phase0/jarvis-mvp1-v1-poc-phase2-entry-brief.md` (본 문서)

Phase 2 cycle 실행 *후* 작성 예정 (별도 명시 승인 후):
- `docs/phase0/v1-poc-raw/2026-05-2X-phase2-summary.json` (Phase 2 raw 종합)
- `docs/phase0/v1-poc-raw/2026-05-2X-phase2-ca-*-modelcard.json` (HF 응답 raw)
- `docs/phase0/v1-poc-raw/2026-05-2X-phase2-egress-baseline-{pre,post}.json`
- (findings 별도 명시 시) `docs/phase0/jarvis-mvp1-v1-poc-phase2-findings.md` 또는 `jarvis-mvp1-v1-poc-findings.md` 부록

본 brief 작성만으로는 위 raw / findings / commit / push 0건.

---

## 8. 답습 요약 (영구)

- **하는 것** (v1 계획): Phase 2 cycle (C-a) 운영 절차 식별 + HF egress 시점/범위 격리 + 보고 항목 raw 한정
- **하지 않는 것** (v1 계획): HF 실 fetch / Ollama 데몬 변경 / 모델 pull / config 변경 / M3·M4 결정 *고정* / OllamaBoss 코드 / 합의 보고서·commit·push / 보안 거버넌스 자동 재개
- **v2 갱신**: §9 추가 — Phase 2 cycle 실행 완료 raw (HF read-only fetch 10회 발생, F1 (i) 답 확보, LLM 호출 0). 합의 보고서·commit·push 는 여전히 0건 (별도 명시 승인 대기)
- **출처**: `3plus1-consensus-2026-05-23-jarvis-mvp1-m3-m4-decision.md` §5.2 + R-5/R-10/R-11/R-15/R-17 / V-1 entry brief v1.1 §8 (R-3·R-11) / Phase 1 결과 (`2026-05-24-phase1-summary.json`) / Stage 1 manifest (`2026-05-23T11-53-qwen3-coder-next-manifest.json`) / `feedback_proportionate_security_personal_tool` / `feedback_staged_consensus_workflow` / `project_jarvis_local_boss_direction`.

---

## 9. Phase 2 cycle 실행 결과 (v2 EXECUTED, raw 한정, R-6 답습)

🔴 **본 §9 = Phase 2 cycle 실 실행 후 raw 결과 답습.** §1~§8 = 계획 (v1 시점, 불변). §9 추가 = 계획 vs 실행 격리 보존.

**실행 일시**: 2026-05-23 23:36:42 ~ 23:46:52 KST (~10분 10초)
**실행자**: 본 Claude 세션 (PID 1225200, delangi/pts/0)
**LLM 호출**: 0건 (read-only HF + 부차 페이지 조회 한정)
**WebFetch 횟수**: 10회 (1차+부차 + alternate)
**R-1 hash 일관**: 6회차 + 7회차 = `ce95c47...8877b10` 완전 동일 (Phase 1 답습 7회 연속)

### 9.1 §2.1 사전 점검 raw

| Step | 결과 | 답습 |
|----|----|----|
| 1 (R-1 hash 6회차) | `ce95c475432376728311695163fae21c7406998e4c05450e48b7908b78877b10` | Phase 1 답습 일관 ✅ |
| 2 (§8 baseline pre, 23:36:42) | 외부 8 IP — HF/CF/Fastly 0건. iptables OUTPUT 0 pkts/0 bytes | clean baseline ✅ + iptables 측정 한계 확인 |
| 3 (`/api/show`) | qwen3-coder-next 메타. modelfile FROM = blob hash only (HF source URL 명시 0). model_info_keys 37개 — `qwen3next.expert_count: 512`, `expert_used_count: 10`, `full_attention_interval: 4`, `ssm.*` 필드 다수 | R-17 입력 ✅ |
| 4 (R-23 동결) | 🟡 1차 점검: 다른 Claude 세션 PID 1200229 발견 → 사용자 (a) 종료 승인 → kill 확인. 재점검: 본 세션 only. Ollama runner 2 (LLM 호출 0 → 영향 0) | 정직성 답습 |

### 9.2 §2.2 HF + 부차 페이지 조회 raw (egress 발생 윈도)

**총 WebFetch 10회** raw 답습:

| # | URL | HTTP | 핵심 raw 답 |
|----|----|----|----|
| 1 | `huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct` | 200 | **"Number of Parameters: 80B in total and 3B activated"** (verbatim) ✅ F1 직접 답 |
| 2 | `huggingface.co/.../blob/main/config.json` | 200 | num_experts=512, num_experts_per_tok=10, hidden=2048, 48 layers, Q heads=16/KV heads=2 (GQA 8:1), full_attention_interval=4 |
| 3 | `qwenlm.github.io/blog/qwen3_next/` | **404** | — |
| 4 | `qwenlm.github.io/blog/qwen3-next/` | **404** | — |
| 5 | `qwenlm.github.io/blog/` (index) | 200 | "not found in index" verbatim |
| 6 | `qwen.ai/blog` (index) | 200 | "not found" verbatim |
| 7 | `arxiv.org/abs/2505.09388` | 200 | Qwen3 일반 paper (Qwen3-Next/A3B/Gated DeltaNet 미언급). Qwen3-Next 전용 paper 미존재 |
| 8 | `huggingface.co/.../Instruct` (URL 추출 재조회) | 200 (캐시 적중 가능) | 진짜 블로그 URL 발견: `qwen.ai/blog?id=4074cca8...` + 외부 URL 16종 |
| 9 | `qwen.ai/blog?id=4074cca8...` | 200 | "only contains Qwen" (SPA, JS-rendered, fetch 추출 0) |
| 10 | `docs.vllm.ai/projects/recipes/en/latest/Qwen/Qwen3-Next.html` | 200 | 80B + "hybrid attention" + "highly sparse MoE" + "MTP" verbatim. 활성 파라미터 "Not stated". 권장 `--tensor-parallel-size 4` |

**F1 직접 답 (R-6 raw 한정, framing 0건)**:

| 출처 | 활성 파라미터 raw | 자격 |
|----|----|----|
| HF 모델 카드 | **3B activated** (verbatim) | ✅ 직접 명시 |
| HF config.json | 512 expert × top-10 + shared 1 + FFN 512 dim (구조 정합) | ✅ 구조 cross-check |
| Ollama `/api/show` | expert_count=512, expert_used_count=10 (config.json 일치) | ✅ 메타 일관 |
| vLLM 레시피 | 80B + hybrid + MoE + MTP (활성 미명시) | 🟡 부분 확인 |
| 공식 블로그 (qwen.ai SPA) | verbatim 추출 0 | ❌ 수단 한계 |
| 공식 블로그 (qwenlm) | 미게시 (404) | ❌ |
| Qwen3-Next 전용 arXiv | **미존재** | ❌ 정직성 보고 |

**F1 가설 (i) 답** (raw, framing 0건): 활성 파라미터 = **3B activated** (HF 모델 카드 verbatim 1회 + 3중 cross-check). 가설 "~3B 가정 초과 — 실제 ~10B+" → **부정** (가정 = 실측 일치).

**부차 발견 (raw verbatim)**:
- **Architecture**: Hybrid Gated DeltaNet (linear attention) + Gated Attention (GQA Q=16/KV=2) + MoE (512 expert top-10 + shared 1) + MTP. layout verbatim: `12 * (3 * (Gated DeltaNet → MoE) → 1 * (Gated Attention → MoE))`
- **명명 격차**: HF 모델 카드 verbatim "**No SSM/Mamba components**" vs Ollama 메타 `qwen3next.ssm.*` 키 → Ollama 가 Gated DeltaNet 내부 conv·state 필드를 ssm 으로 라벨링. 두 시스템 라벨 정의 격차 정직성 보고
- **"A3B" 명시 정의 0건** — HF 모델 카드·config·vLLM·블로그 모두에서 verbatim 정의 0. 문맥상 "Active 3B" 추정만
- **Qwen3-Next 전용 arXiv paper 미존재** — 모델 카드의 `2505.09388` 인용 = Qwen3 일반 paper (정직성 보고)
- **vLLM 권장 `--tensor-parallel-size 4`** — GB10 1대 (single device) 로는 vLLM 권장 미충족. Phase 3 이후 inference stack 의사결정 입력

### 9.3 R-10 답습 — Agent A 산정 비교

| 출처 | 활성 파라미터 |
|----|----|
| Agent A manifest 산정 (lower-bound, 4 보정 모두 ↑) | ~4.3B |
| HF 공식 표기 (verbatim) | **3B** |
| 격차 | Agent A 추정 = **+43% 과대 추정** |

**평가**: Agent A 산정 방식 (Ollama manifest 추정) 의 over-estimate 경향 1건 확인. 격차 원인 가설 = expert_intermediate_size 512 (작은 FFN) + shared expert 1개 효과 미반영 가능성. **R-10 누락 raw 답습 완료**. M3·M4 결정 *고정* 자격 X — Agent A 산정 방식의 일반화 가능성 = Phase 1+2 종합 후 별도 합의 입력.

### 9.4 R-15 답습 — gap-pull 8종 후보 평가 입력

본 cycle = Qwen3-Next 1차 후보만 정량. 부차 8종 (V-1 entry brief §3.2 Step 2a) = §2.2 Step 2 에서 skip (사용자 명시 승인 없음, cycle 범위 한정). **R-15 부차 입력 = config.json 산정 framework 확보** (num_experts × top-k × expert_FFN × shared FFN + linear attn family 식별) — 8종 후보 별도 cycle 입력 가능.

### 9.5 §2.3 cycle-後 baseline + §3 egress 시점 격리

**R-1 hash 7회차** (23:46:52): `ce95c475432376728311695163fae21c7406998e4c05450e48b7908b78877b10` — 6회차 완전 동일 ✅

**ss established cycle-前 vs cycle-後 변동**:

| 신규 출현 IP | 추정 | 격리 |
|----|----|----|
| `172.67.154.127:443` | **Cloudflare** (172.64.0.0/13) | 본 cycle 의도 (HF + qwen.ai = CF 호스팅) |
| `151.101.3.42:443` | **Fastly CDN** (151.101.0.0/16) | 본 cycle 의도 (docs.vllm.ai 추정) |
| `35.168.55.154:443` | AWS us-east-1 | 본 cycle 무관 (백그라운드) |
| `192.168.45.100:50970 → 160.79.104.10:443` | Anthropic | 본 Claude 세션 신규 (cycle 무관) |

**§3 격리 평가** (R-3, 시간 범위 23:36:42~23:46:52):
- **본 cycle 의도 egress**: HF (CF) + qwen.ai (CF) + qwenlm.github.io (GitHub Pages) + arxiv.org + docs.vllm.ai (Fastly) — TCP established 흔적 CF + Fastly 격리 ✅
- **본 cycle 무관 egress**: Anthropic API (본 Claude 세션) + AWS/Google 백그라운드 — 분리 가능
- **Ollama egress**: localhost only (외부 0) ✅
- **비-의도 egress (의외 도메인) 0건** — 모든 신규 외부 IP 가 본 cycle 의도 fetch 대상으로 설명 가능

**iptables OUTPUT 측정 수단 한계** (정직성 raw 보고):
- cycle-前/後 모두 `policy ACCEPT 0 packets, 0 bytes`
- 시스템이 **nftables** 사용 추정 → iptables 로는 egress delta 측정 불가
- → **iptables 는 cycle 비교 anchor 로 무효** 명문. nft 직접 조회 또는 ss 변동 + 도메인 IP range 식별이 유효 수단

### 9.6 정직성 한계 답습 (실행 후 갱신)

| 한계 | 영향 |
|----|----|
| **공식 블로그 verbatim 추출 0** | qwen.ai SPA + qwenlm 미게시. F1 답 = HF 모델 카드 verbatim 1회 + 3중 cross-check 한정. 공식 블로그 검증 차수 0 |
| **Qwen3-Next 전용 arXiv paper 미존재** | 학술 검증 차수 0 (정직성 보고) |
| **"SSM" vs "Gated DeltaNet" 명명 불일치** | Ollama 메타 `qwen3next.ssm.*` 키와 HF verbatim "No SSM/Mamba" 격차. 두 시스템 라벨 정의 격차 명문 |
| **iptables 측정 수단 무효** | nftables 사용 추정 → ss 변동 + IP range 식별이 유효. iptables 0 카운터 = anchor 아님 |
| **R-23 1차 위반 후 정정** | 본 cycle 시작 전 다른 Claude 세션 1건 존재 → 종료 후 진행. LLM 호출 0 cycle 이므로 영향 0 명문 |
| **WebFetch 캐시 영향** | 15분 자동 캐시 — 본 cycle 내 동일 URL 재조회 시 캐시 적중 가능 (fetch #8 의심). egress 실 횟수 < 10 가능성 명문 |

### 9.7 Phase 2 cycle 결과 종합

| 지표 | 값 |
|----|----|
| F1 직접 답 확보 | ✅ 활성 파라미터 = **3B activated** (HF verbatim + 3중 cross-check) |
| F1 가설 (i) 평가 | "~3B 가정 초과" **부정** — 가정 = 실측 일치 |
| 부차 — Architecture | Hybrid Gated DeltaNet + Gated Attention + MoE (512 top-10) + MTP, 48 layers, 256K ctx |
| 부차 — A3B 명시 정의 | **0건** (verbatim 미발견) |
| 부차 — Qwen3-Next 전용 paper | **미존재** |
| R-10 답습 (Agent A 비교) | Agent A 산정 +43% 과대 추정 1건 확인 |
| R-15 입력 (gap-pull 8종) | framework 확보, 8종 정량 별도 cycle |
| R-23 동결 | 1차 위반 → 정정 → cycle 진행 (LLM 호출 0 → 영향 0) |
| R-1 hash 일관 | 7회 답습 ✅ |
| 비-의도 egress | 0건 |
| 의도 egress 격리 | CF + Fastly + GitHub Pages + arxiv + qwen.ai 분리 보고 |
| iptables 한계 | 측정 수단 무효 정직성 보고 |
| LLM 호출 | 0건 |
| commit·push | 0건 |

### 9.8 F1·F2 가설 5종 갱신

| 가설 | Phase 1 | Phase 2 | 결합 평가 |
|----|----|----|----|
| (i) 활성 파라미터 ~3B 가정 초과 | — | ✅ **부정** | **가설 (i) 사실상 종결** |
| (ii) SSM state 메모리 압박 | A-진단 → roofline 90~120 tok/s | Architecture = Gated DeltaNet (NOT classical SSM) → 명칭 정정. linear attn family state 압박 가능성 = Phase 3 별개 | 명명 정정 + Phase 3 입력 |
| (iii) Ollama 0.20.4 hybrid 효율성 (vs llama.cpp) | — | — | **Phase 3 C-e 측정 필요** |
| (iv) Qwen3-Next router/gating overhead | A-진단 입력 | 512 expert × top-10 + shared 1 = router 부담 가능성 ↑ | 가설 (iv) 입력 강화, Phase 3 별도 측정 |
| (v) GB10/Ollama effective BW spec 1/3 (~85GB/s) | 강한 evidence (qwen2.5 dense 측정 역산) | — | **여전히 가장 강한 evidence** |

→ **갱신 결론**: F1 본질은 (i) 부정 + (v) 강화 + (iii)(iv) 미해소. M3·M4 결정 *고정* = Phase 3 입력 후 종합 합의 필요. **Phase 2 단독 자격 = F1 (i) 종결 + (v) 강화 입력만, 결정 고정 자격 X** (M3·M4 §4.4 답습).

### 9.9 다음 단계 옵션 (사용자 결정 — 자동 진입 0건)

| 옵션 | 내용 | 자격 |
|----|----|----|
| (G) | brief v2 검토 후 → commit (`docs: V-1 PoC Phase 2 cycle — F1 (i) 부정 + 활성 3B 4중 확인`) | 사용자 명시 |
| (H) | brief v2 + raw artifact 별도 작성 (`v1-poc-raw/2026-05-23-phase2-summary.json` + modelcard JSON) → commit | R-22 답습 강화 |
| (I) | brief v2 commit 후 → **풀 3+1 합의 가동** — Phase 2 결과 + R-10/R-15 입력 + (i) 부정 + (v) 강화 종합 → M3·M4 결정 *고정* 자격 평가 | M3·M4 §4.4 답습 |
| (J) | brief v2 commit 후 → **Phase 3 entry brief** (C-e llama.cpp 빌드·측정) — (iii)(iv) 미해소 입력 | M3·M4 §5.3 답습 |
| (K) | brief v2 commit 후 일시 정지 — 다음 세션 진입 시 (I)(J) 결정 | 휴식 |

---
