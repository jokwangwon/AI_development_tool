# 3+1 합의 보고서 — Jarvis MVP-1 V-1 PoC 운영 entry brief v1

**작성일**: 2026-05-23
**대상**: `docs/phase0/jarvis-mvp1-v1-poc-entry-brief.md` (DRAFT v1)
**프로토콜**: **풀 3+1** (CLAUDE.md §3 — 측정 절차 운영화 + 출처 미상 데몬 발견 = 보안 차원 동시)
**구성**: Agent A(구현 분석가) · Agent B(품질/안전성 검증가) · Agent C(대안 탐색가) 병렬 독립 → Reviewer 교차 비교
**최종 판정**: **APPROVE w/ COND (HIGH) — brief v1.1 보강 후 V1-1 read-only 실 측정 진입 가능. BLOCKING 6건 미반영 시 진입 차단.**

---

## 0. 3개 판정 요약

| Agent | 판정 | 한 줄 |
|-------|------|------|
| **A (구현)** | APPROVE w/ COND | GB10/Ollama 0.20.4 환경 정합. BLOCKING 2건 (prefill 입력 토큰 생성 절차 누락 + 모델 태그 Ollama Hub 실재 미확인) — 측정 신뢰성 직접 영향 |
| **B (안전)** | APPROVE w/ COND | 골격 견고. 정직성/엣지케이스 3 영역 보강 필수 (출처 미상 Ollama silent 교체 위험 / 실패 분기 4 누락 / egress 점검 시간 한정) — A·C 결락된 critical 발견 |
| **C (대안)** | APPROVE w/ COND | BLOCKING 0. 측정 도구 단일·런타임 후보 2개·MoE 후보 3종 한정 = 대안 깊이 부족. 4건 권고 반영 시 재현성·정직성·옵셔널리티 향상 |

**3개 모두 APPROVE w/ COND, agent-level BLOCKING 합 5건.** Reviewer 권위로 6건으로 통합·격상 (R-1 ~ R-6). 방향(read-only 식별 + 절차 운영화 + 권고 매트릭스) 자체에 합의. 조건 = 아래 brief v1.1 보강.

---

## 1. 교차 비교 (4 분류)

### ① 일치 (Consensus, 3/3)

- **C-1**: **종합 판정 = APPROVE w/ COND** — brief v1 방향에 합의. agent-level BLOCKING 은 v1.1 보강 항목.
- **C-2**: **측정 정직성 보강 필요** (A-F4·A-F11·A-F12 / B-F8·B-F13 / C-F4·C-F8) — std/mean·outlier·percentile·anchor effect 모두 "raw 보고 + PASS/FAIL 판정 0건" 정직성 강화로 수렴.
- **C-3**: **R5 (tok/s roofline + 실측) · R11 (egress 추론시점 한정) 답습 충실** — §4 + §8 절차 자체에 이견 0. brief v2 합의 정합.
- **C-4**: **결정 고정 압력 회피** (B-F7·B-F8 / C-F5 / A 암묵) — §9.1 M3 "Ollama 우선" framing + §4.4 "≥15 = PASS 후보" framing 둘 다 anchor effect 위험으로 정정 필요.
- **C-5**: **CLAUDE.md §1 (TDD/SDD) + §3 (3+1) + ADR-011 §2.1 (수단/목적 분리) 정합** — 3개 agent 출력 어느 것도 답습 권위와 모순 없음.
- **C-6**: **롤백 정책 (§10) + 부록 A 매핑 명료** — A·B·C 어느 누구도 이의 제기 없음 (B-F12 가 라벨 강도만 지적).

### ② 부분 일치 (Partial, 2/3)

- **P-1 (A-F1 + C-F4 + B-F5)** — §4 측정 *입력/출력 분포* 신뢰성: A=prefill 입력 생성 절차 누락(BLOCKING) / C=percentile p50/p95(권고) / B=timeout/OOM(권고). 세 방향 모두 §4 신뢰성 = 같은 표면 다른 층 → **통합 채택**.
- **P-2 (A-F2 + C-F3)** — §3.2 MoE 모델 후보: A=후보 3종 실재 미확인(BLOCKING) / C=5~7종 식별 권고(확장). 직교 관점 → **둘 다 채택, A 절차가 C 확장 후보 검증에 재사용**.
- **P-3 (A-F3 + B-F11 + C-F6)** — §6 V1-5 GB10 unified memory 측정: A=pmon fallback / B=한계 노트 명문화 / C=정밀 도구 후보 식별. **A+B 권고 채택, C=NOTE**.
- **P-4 (A-F4 + B-F8)** — §4 framing: A=측정 mechanics(EOS 일찍 종료) / B=결정 압력(anchor effect). 다른 층 → **둘 다 채택, B-F8 = 🔴 BLOCKING(자기모순), A-F4 = 권고**.

### ③ 불일치 (Divergence, 3개 다른 방향)

- **D-1 (M3 §9.1 framing)**: A 미언급 / B-F7 "Ollama 우선 framing 정정" / C-F2 "3rd 후보 식별 추가".
  - **Reviewer 선택**: **B + C 통합 채택** = R-7. 충돌 아님(B=framing / C=fallback 추가). A 침묵 = framing 자체에 이견 없음.
- **D-2 (§4.4 threshold framing)**: A 미언급 / B-F8 "framing 정정 (raw 보고만)" / C-F5 "spectrum 후보".
  - **Reviewer 선택**: **B-F8 = 🔴 BLOCKING (R-6), C-F5 = NOTE (R-26 평행)**. 이유: C-F5 는 결정 단계 carryover trap 위험, 본 brief = 측정 entry 한정.
- **D-3 (§3.2 후보 모델 깊이)**: A-F2(좁고 깊게) / C-F3(넓게) / B 미언급.
  - **Reviewer 선택**: **둘 다 채택, 통합** (앞 P-2 와 동일).

### ④ 누락 (Gap, 1 agent 만)

- **G-1 (B 만, 가장 critical)**: B-F1 출처 미상 Ollama silent 교체 위험 — **🔴 BLOCKING (R-1)**, A·C 미발견. 풀 3+1 의 핵심 가치 (관점 누락 발견).
- **G-2 (B 만)**: B-F2 실패 분기 4 누락 — **🔴 BLOCKING (R-2)**, 모법 R3 fail-closed 답습 직접.
- **G-3 (B 만)**: B-F3 egress 점검 시간 한정 — **🔴 BLOCKING (R-3) + 권고 (R-11b)**, 명문 1줄 = 거짓 안전감 차단.
- **G-4 (A 만)**: A-F1 prefill 입력 토큰 생성 절차 — **🔴 BLOCKING (R-4)**, 측정값 수치 의미 결정.
- **G-5 (A 만)**: A-F2 후보 모델 Ollama Hub 실재 — **🔴 BLOCKING (R-5)**, 헛 결정 차단.
- **G-6 (A 만)**: A-F5 `/v1/` `usage` 필드 불확정 — **권고 (R-12, R-2 흡수)**.
- **G-7 ~ G-17**: 권고/NOTE 12건 (A·B·C 각자 한정 발견) → 합의 결정 사항에 분산 반영.

---

## 2. 합의 결정 사항 (R-# = brief v1.1 반영 의무)

### 🔴 BLOCKING (brief v1.1 보강 필수, 미반영 시 V1-1 진입 차단)

| R-# | 출처 | 요지 | 반영 § |
|----|----|----|----|
| **R-1** | B-F1 (Reviewer 격상) | §1.2 출처 미상 Ollama silent 교체 위험 명문화 + `sha256sum /proc/<pid>/exe` 식별값 기록 의무 (측정 단계 entry) + §0.2 금지에 "Ollama 데몬 재시작/kill/signal" 추가 | §0.2, §1.2 |
| **R-2** | B-F2 + A-F5 (통합) | §2.3 실패 분기 4 추가 — (1) 측정 중 데몬 죽음 (2) 11434 다른 프로세스 점유 (3) GPU OOM CPU fallback 감지 (4) `/api/version` 비정상 응답. §5.2 `eval_count` 우회 명시 | §2.3, §5.2 |
| **R-3** | B-F3 (b) | §8.1 끝 1줄 — 본 §8 = 측정 세션 한정. 외부 시점 (자체 업데이트·텔레메트리·lazy upload) egress 범위 밖 | §8.1 |
| **R-4** | A-F1 | §4.2 Step 2·4 사전/사후 토큰 검증 — `/api/tokenize` 로 사전 측정 → 목표 ±10% 도달 + 응답 `prompt_eval_count` 사후 확인 | §4.2 Step 2·4 |
| **R-5** | A-F2 + C-F3 (통합) | §3.2 Step 2 절차 분리 — **2a**: 후보 5~7종 식별 (DeepSeek-V3.1-Lite·GLM-4-MoE·Granite-3.5-MoE·OLMoE·Qwen3-Next family 추가). **2b**: 각 후보 `/api/library` 또는 `ollama search` read-only 조회 → 실 tag 확정 | §3.2 Step 2 (2a / 2b 분리) |
| **R-6** | B-F8 | §4.4 전면 재작성 — "성공기준" → "보고 항목". PASS/FAIL 0건. raw 보고 (decode·prefill mean·std·p50·p95 / wall-clock @ 8192). "≥15 PASS 후보" 라인 삭제 (M4 결정 라인은 §9.2 그대로 유지) | §4.4 (전면 재작성) |

### 🟡 권고 (brief v1.1 반영 권고, 미반영도 V1-1 진입 비차단)

| R-# | 출처 | 요지 | 반영 § |
|----|----|----|----|
| **R-7** | B-F7 + C-F2 (통합) | §9.1 표 "권고(고정 아님)" → "V-1 findings 후 별도 합의에서 결정 — 본 brief 0건 고정". 끝에 1행 추가: "둘 다 FAIL → 3rd 후보 식별 (MLC-LLM / llamafile / ktransformers / vLLM MVP-2 재검토)" | §9.1 |
| **R-8** | A-F4 | §4.2 Step 1 명령에 `"temperature": 0.0`·`"stop": []` 추가 + 한국어 프롬프트 "긴 출력 유도" (단락 5개 이상) 강화 | §4.2 Step 1 |
| **R-9** | A-F6 + A-F12 | §4.2 Step 3 — 첫 호출 outlier (2σ 초과) 시 재warm-up 또는 warm-up 2회 + 5회 중 1개 trim 정책 명시 | §4.2 Step 3 |
| **R-10** | A-F3 + B-F11 | §6.2 Step 2 `pmon` 보고 불완전 시 fallback (`/api/show` + `/api/ps`) + §6.3 한계 노트 강화 (`/proc/meminfo` = 시스템 전체) | §6.2 Step 2, §6.3 |
| **R-11b** | B-F3 (a) | §8 끝 옵션 메모 — 더 강한 점검 = baseline + 5분 polling = 별도 cycle | §8 |
| **R-14** | A-F7 | §3.2 (또는 §4.3) 1줄 — `mixtral:8x7b` 활성 ~13B = A3B 4배, 'MoE 동작 검증' 한정 | §3.2 또는 §4.3 |
| **R-15** | A 추가권고 1 | §2.2 또는 §4 — `OLLAMA_NUM_PARALLEL`·`OLLAMA_MAX_LOADED_MODELS` 조회 + 측정 중 동시 호출 차단 (R-23 합류) | §2.2 또는 §4 |
| **R-16** | C-F1 | §4.2 끝 옵션 — `ollama run <model> --verbose` 보조 측정 → curl/jq 값과 ±5% 일치 확인 | §4.2 |
| **R-17** | B-F6 | §7.2 Phase 7-B — 빌드 *전* `~/build/llama.cpp` 비어있음 확인 + 실패 시 정리 + `make install` 금지 명시 | §7.2 |
| **R-18** | B-F9 | §6.2 Step 4 — "MoE ≥ 2x → 병목 가설 PASS" → "병목 가설과 *모순 안 함*" 한정 | §6.2 Step 4, §6.3 |
| **R-19** | B-F10 | §12 옵션 (E) 추가 — V-1 findings 후 출처 미상 Ollama 위생 정정 trigger 검토. §10 cross-ref | §10, §12 |
| **R-22** | C 추가권고 1 | §4.5 신규 — raw JSON 보존 (`docs/phase0/v1-poc-raw/<timestamp>-<model>-<scenario>.json`) | §4.5 신규 |
| **R-23** | C 추가권고 2 | §4.6 신규 — 측정 환경 동결 (다른 GPU/CPU heavy 0, 백그라운드 Claude Code 포함 → R-15 합류) | §4.6 신규 (또는 R-15 통합) |
| **R-11a / R-12 / R-13** | (BLOCKING 으로 흡수) | R-3·R-2·R-9 의 일부로 흡수됨 | — |

### 🟢 NOTE (선택, 향후 답습 — 17건)

R-20 `pmon -c 5` 간격 명시 · R-21 streaming/TTFT 별도 측정 · R-24 llama.cpp prebuilt release 식별 · R-25 GB10 정밀 도구 후보 · R-26 출처 미상 Ollama 4 대안 매트릭스 부록 · R-27 디스크 가드 MoE quant 용량 표 · R-28 findings 정직성 SOP 1줄 · R-29 부록 A "부분 완료" 라벨 강도 보강 · R-30 isovolumetric 별도 단계 · R-31 `qwen3-coder-next` MoE 판별 필드 예시 · R-32 빌드 시스템 README 확인 · R-33 `-d @file.json` 일관성 · R-34 fresh subshell 환경변수 격리 · R-35 데몬 uptime/PID 변동 확인 · R-36 측정 대상 무결성 검증 (R-1 확장) · R-37 모델 전환 cache 처리 · R-38 §5 `tools` 거부 검증 · R-39 prebuilt SHA 확인.

---

## 3. 합의 결과 통계

| 분류 | 건수 |
|----|----|
| 🔴 BLOCKING (R-1 ~ R-6) | **6** |
| 🟡 권고 (R-7 ~ R-19, R-22, R-23) | **14** (흡수 3건: R-11a·R-12·R-13) |
| 🟢 NOTE (R-20 ~ R-39) | **17** |
| 기각 | **0** |
| **합계** | **37** (흡수 제외) |

**3개 agent 출력 모두 답습 권위 (brief v2 + 합의 R1~R13 + CLAUDE.md + ADR-011) 와 모순 없음.** C-F5 (threshold spectrum) 만 결정 단계 carryover 로 *격하* (NOTE R-26 평행) 이되 기각 아님.

---

## 4. 본 brief v1 / v1.1 권위 한계 (변동 0)

- **측정 실행 0건** (모법 §0.2 영구 답습) — brief v1.1 보강 자체도 측정 실행 0건.
- **M2 (모델) · M3 (런타임) · M4 (threshold) 결정 *고정* 0건** — R-7 (M3 framing 정정) 도 결정 고정 강화가 아니라 *해제*.
- **보안 거버넌스 자동 재개 0건** (`feedback_proportionate_security_personal_tool`) — R-1 (위생 정정 trigger 명문화) 도 정정 *실행* 0, trigger *식별* 만.
- **단계별 합의 cycle 답습** (`feedback_staged_consensus_workflow`) — brief v1.1 작성 → 사용자 검토 → V1-1 측정 = **각각 별도 명시 승인**.

---

## 5. 다음 단계 권고 (사용자 결정 — 자동 진입 0건)

| 옵션 | 내용 | Reviewer 평가 |
|----|----|----|
| **(a)** | brief v1.1 작성 (R-1~R-6 BLOCKING + R-7~R-19/R-22/R-23 권고 14건 반영, NOTE 17건은 부록 또는 별도 cycle carryover) → 사용자 검토 → V1-1 §2 read-only 실 측정 승인 단계 | **★ 권고** |
| (b) | brief v1.1 작성 후 추가 3+1 합의 (단축 Reviewer-only 옵션) | 비용 대비 이득 낮음 (v1.1 = R-# 반영 + 1차 셀프 점검 충분) |
| (c) | brief v1 그대로 V1-1 §2 read-only 즉시 실행 | **비권고** — 6 BLOCKING 미반영 시 측정값 해석 불가 또는 자기모순 → cycle 반복 비용 > v1.1 보강 비용 |
| (d) | commit / push (v1 그대로) | **비권고** — 답습 정합 침식 |

---

## 6. Reviewer 정직성 노트

### Reviewer 가 *직접 검증하지 못한* 것

1. **환경 사실 재검증 0건** — brief v1 §1 (Ollama PID 3375 / version 0.20.4 / 5 모델 인벤토리) 인용은 *재검증 0*. 본 합의 = 3개 agent 출력 교차 비교 한정 (사용자 진입 명령 답습: "사실 식별 + 절차 운영화 + 권고 매트릭스", 사실 재검증은 측정 cycle 단계).
2. **A-F2 후보 모델 실재 미확인** — Reviewer 도 `ollama search` 실행 0건. R-5 = 절차 추가 의무화 = Reviewer 자체 검증과 동치.
3. **B-F1 출처 미상 Ollama *실 위험 수준*** (silent 자동 업데이트 빈도·origin 확정) 도 Reviewer 직접 평가 불가. R-1 = "위험 명문화 + sha256sum 기록 의무화" 까지만 = Reviewer 권한 한계.
4. **C-F3 후보 5~7종 실재** — C 자체 "식별만" 표기, R-5 절차 (`/api/library`) 가 검증 위임.
5. **agent 출력의 사실 인용** (예: A-F4 의 `temperature: 0.0`·`stop: []` 가 Ollama 0.20.4 정확한 옵션명인지) 재검증 0 — R-8 절차 반영 시 측정 단계에서 자동 검증.

### 본 합의의 권위 한계

본 합의 = brief v1 → v1.1 *진입 게이트* 한정. 결정 *고정* 0건 (M2·M3·M4·런타임·boss 코드 = 별도 단계). brief v1.1 작성 → 사용자 검토 → V1-1 실 측정 → findings → M3·M4 결정 = 각각 별도 명시 승인.

### 본 합의가 생성한 것 / 생성하지 않은 것

- **생성한 것**: R-# 39 결정 (BLOCKING 6 + 권고 14 + NOTE 17 + 흡수 2: R-11a·R-12·R-13), brief v1.1 보강 의무 목록, 다음 단계 권고 4 옵션.
- **생성하지 않은 것**: brief 직접 수정 0 / commit·push 0 / 실 명령 실행 0 / M2·M3·M4 결정 0 / 보안 거버넌스 재개 0.

---

**출처**: brief v1 (`jarvis-mvp1-v1-poc-entry-brief.md`) / brief v2 모법 (`jarvis-mvp1-local-boss-design-brief.md` §6) / 합의 (`3plus1-consensus-2026-05-22-jarvis-mvp1-local-boss.md` R1~R13, 특히 R4·R5·R11) / CLAUDE.md §1·§3 / ADR-011 §2.1 (a)~(d)·§2.4 T1/T2/T3 / Agent A·B·C 독립 출력 3개 (병렬, 상호 미참조).

**답습**: `project_jarvis_local_boss_direction` / `feedback_provider_liquidity` / `feedback_proportionate_security_personal_tool` / `project_minimize_user_intervention` / `feedback_staged_consensus_workflow`.

**금지 (영구 답습, 본 합의 0건)**: brief 직접 수정 / commit·push / 합의 보고서 외 파일 작성 / 실 명령 실행 / 측정 실행 / 설치 / sudo / 모델 pull / M2·M3·M4 결정 고정 / 보안 거버넌스 자동 재개.
