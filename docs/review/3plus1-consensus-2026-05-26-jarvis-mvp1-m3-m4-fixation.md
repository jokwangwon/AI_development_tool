# 3+1 합의 보고서 — Jarvis MVP-1 M3·M4 결정 *고정* (s) cycle

**작성일**: 2026-05-26
**대상**: `docs/phase0/jarvis-mvp1-m3-m4-fixation-brief.md` (v1)
**프로토콜**: **풀 3+1** (CLAUDE.md §3 — 아키텍처 큰 결정 + 이전 합의 `9ddec1b` BLOCKING 5 답습)
**구성**: Agent A (구현 분석가) · Agent B (품질/안전성 검증가) · Agent C (대안 탐색가) 병렬 독립 → Reviewer 교차 비교
**최종 판정**: **APPROVE w/ COND (HIGH)** — brief v1.1 보강 의무 7 BLOCKING + 합의 결과로 진입 가능. **M3·M4 결정 *고정* 권고 자격 = 본 cycle 시점 충족 0건**.

---

## 0. 3개 판정 요약

| Agent | 판정 | 한 줄 |
|-------|------|------|
| **A (구현)** | **REVISE** | 4 모델 raw evidence 디스크 부재 (덮어쓰기 + git tracked 0) + 응답 길이 통제 0건 + Q level 비균질 = 3 결함 위에서 *고정 권고 자격* 0. M3-D + M4-A *연기 유지* 외 모든 *고정 권고 자격* 부족. 이전 R-1·R-3·R-5 미해소. |
| **B (안전)** | **REVISE** | framing 의도 정직 (권고 한정·사용자 영역) PASS, **그러나 §2 ranking 표가 raw verifiable + commit log 한정 데이터를 *시각적 동등* 제시 = 거짓 안전감 silent**. 측정 한계 5 종 silent 화 + Provider Liquidity ADR-011 §2.1 (a)~(d) 4조건 답습 0. 거짓 안전감 표지 8 종 발견 (4 CRITICAL/HIGH). |
| **C (대안)** | **REVISE** | **M3-A vs M3-C 이분법 false dichotomy**. `OllamaBoss(model: str)` 답습 시 *현재 코드 자체가 M3-F* (default 인자 + caller 교체 자유 양립). M3-F 신규 후보 brief 본문 silent. (q) 응답 길이 통제 *선행* = 본 cycle 권고 자격 boundary. M3-E 카탈로그 9 후보 식별 확장. |

**3개 모두 본 brief 의 결정 *고정* 0건 답습 정합 + M3-D + M4-A 우선 권고 일치 + 이전 합의 BLOCKING 5 중 R-1·R-3·R-5 미해소 일치.** agent-level BLOCKING 합 11 건 → Reviewer 권위로 7 건 통합·격상 (R-1~R-7). 본 합의 형태 = brief v1.1 보강 의무 7 건 명문 + 권고 자격 게이트 평가 + 사용자 결정 영역 명시.

---

## 1. 교차 비교 (4 분류)

### ① 일치 (Consensus, 3/3)

- **C-1**: **본 합의에서 M3·M4 결정 *고정* 0건** — brief §0 + §6 영구 답습. 본 합의 = 결정 *권고* 한정. (A·B·C 모두)
- **C-2**: **M3-D (트랙 B 진입 연기) + M4-A (threshold 결정 연기) 유지 권고** — 본 cycle 새 evidence 가 *고정* 자격 추가 충족 0건 (3 모두 동의).
- **C-3**: **M4-B (threshold 낮추기) anchor effect 영구 거부** — 이전 합의 R-4 답습 (해소). 본 brief §3.2 명문 PASS (3 모두 확인).
- **C-4**: **응답 길이 통제 0건 = 비교 신호 약화** — glm-4.7-flash latency 101.93s 가 응답 길이 차이 영향 지배적 가능 (3 모두 명시). brief §2.1 부분 답습.
- **C-5**: **이전 합의 R-3 (§12 옵션 E cross-ref) 미해소** — Ollama binary 출처 미상 명문 강도 본 brief 약함 (3 모두).
- **C-6**: **이전 합의 R-5 (F1/F2 Phase 1 cycle) 미해소** — cache miss 분리 / 활성 파라미터 / effective BW 진단 = 본 cycle 측정 0건 (3 모두).
- **C-7**: **M3·M4 *고정* 자체 = 사용자 결정 영역** (Layer 2 사람 게이트 책무, 본 cycle 권고 한정) — 책무 분리 정합 (3 모두).
- **C-8**: **측정 실행 0 / 빌드 0 / 코드 변경 0 / Ollama 변경 0 / 보안 거버넌스 자동 재개 0** — 본 합의 자체 답습.

### ② 부분 일치 (Partial, 2/3)

- **P-1 (A·B)**: **raw 4 모델 손실 = CRITICAL** — A 의 F-A1 ("4 모델 raw evidence 의 현 디스크 부재") + B 의 F-B-1 ("raw 손실로 4 모델 evidence verifiable 0 — silent 화"). C 는 raw 손실 명시 X, 단 (p)+(r) commit log 답습 한정 인용 = 간접 답습. **Reviewer 격상 → R-1 (BLOCKING)**.
- **P-2 (B·C)**: **옵션 매트릭스 형식 자체 = anchor / Provider Liquidity framing 약화** — B 의 R-B-B3 (M3-A 단점 "Provider Liquidity 약함" 한 줄 → ADR-011 §2.1 (a)~(d) 4조건 답습 의무) + C 의 R-C-1 (M3-A vs M3-C 이분법 false → M3-F 신규). 둘 다 brief §3.1 M3-A 행이 *불완전* 진단. **Reviewer 통합 → R-2 (BLOCKING)**.
- **P-3 (A·C)**: **응답 길이 통제 부재 → ranking 의미 약화** — A 의 R-A-B2 (응답 길이 통제 명시 도입 cycle 권고) + C 의 R-C-2 + R-C-3 ((q) 선행 의무 + schema 권고). B 는 동일 신호 (F-B-2 "decode tok/s 만이 보스 자격" silent 가정) 다른 각도. **Reviewer 통합 → R-3 (BLOCKING)**.
- **P-4 (A·B)**: **이전 R-3 (Ollama 출처 미상) + R-5 (Phase 1 cycle) 미해소 명문 의무** — A 의 §7 매트릭스 + B 의 §7 매트릭스 동등 발견. C 의 §7 매트릭스도 R-3 + R-5 미해소 명시. **Reviewer 통합 → R-4 (BLOCKING)**.
- **P-5 (A·B)**: **운영 안정성 / 한국어·코드 quality 미측정 = 보스 자격 본질 미평가** — A 의 R-A-B3 (운영 안정성 evidence 0) + B 의 R-B-3 + R-B-4 (한국어 + 코드 정확도 미측정). **Reviewer 격상 → R-5 (BLOCKING)**.
- **P-6 (B·C)**: **본 cycle anchor risk + 권고 자격 게이트 명문** — B 의 R-B-B4 (권고 *온전* 자격 옵션 명문) + R-B-B5 (본 cycle = 권고 자격 평가 *gate*) + R-B-7 (anchor risk self-진단) / C 의 권고 자격 boundary 명문 ((q) 선행 의무). **Reviewer 통합 → R-6 (BLOCKING)**.

### ③ 불일치 (Divergence, 3개 다른 방향)

- **D-1 (M3 권고 형태)**:
  - **A**: M3-D + M4-A *연기 유지* 외 모든 권고 자격 0 (이전 합의 BLOCKING 5 중 4 미해소 명시).
  - **B**: 권고 *온전* 자격 옵션 = M3-D + M4-A 한정 (A 동의). M3-A/M3-C/M3-E 모두 결함 (raw 손실 + latency 미통제 + 출처 미상 + 한국어/quality 미측정) 미해소 시 권고 자격 0.
  - **C**: M3-A vs M3-C 이분법 false → **M3-F (default + 교체 자유 양립) 신규 후보**. M3-F = 코드 변경 0 (인자만), Provider Liquidity 본질 보존, 사용자 의무 최소 ([[project_minimize_user_intervention]] 답습). M3-F 권고 = 약한 형태 ("default *후보* 권고 한정") 단 (q) 선행 의무.
  - **Reviewer 분석**: 충돌이 아닌 **시점 차이**. A·B = "현 시점 *고정 권고* 자격 0 = M3-D + M4-A 연기 유지 한정" / C = "M3-F *식별*  + (q) 선행 후 약한 권고 가능". 세 시각 통합 = **본 합의 권고 = M3-D + M4-A 연기 유지 + M3-F 신규 후보 *식별만* (사용자 후속 cycle 결정 입력) + (q) cycle 별도 brief 신규**.
  - **Reviewer 선택**: 통합 권고 = A·B·C 모두 답습.
- **D-2 (M3-E 카탈로그 강도)**:
  - **A**: 이전 합의 R-7 (MLC-LLM·llamafile 식별) 답습, 추가 측정 권고 0 (운영 검증 우선).
  - **B**: 직접 권고 X (안전성 관점).
  - **C**: 카탈로그 9 후보 (MLC-LLM·llamafile·TGI·SGLang·vLLM 재확인·ktransformers·TensorRT-LLM·ExecuTorch·Hermes/LiteLLM). 측정·채택 0, 식별만.
  - **Reviewer 선택**: **C-R-C-4 단독 채택, NOTE 격** — 본 합의 시점 측정 cost 비례성 약함. 식별 정도 확장 권고만. **R-7 (권고)**.
- **D-3 (M3-G task-domain routing)**:
  - **A**: 미언급.
  - **B**: 미언급.
  - **C**: R-C-7 (M3-G 신규 후보, MVP-2 단계 식별만).
  - **Reviewer 선택**: **C-R-C-7 단독, NOTE 격** — MVP-2 별도 brief 적격. 본 합의 시점 범위 초과.

### ④ 누락 (Gap, 특정 Agent 만)

- **G-A1**: A 의 §3.1 M3-A 단점 칼럼에 "운영 안정성 evidence 0 / 한국어 능력 미측정 / Ollama 출처 미상 답습" 명문 의무 — R-5 에 통합.
- **G-A2**: A 의 R-A-3 (Boss prompt 4 도메인 × 7 모델 동작 검증 0건, 별도 cycle) — 누락. **Reviewer 추가 → R-8 (권고)**.
- **G-A3**: A 의 R-A-5 ("bartowski" 제3자 quant 출처 명시 cycle) — 누락. **Reviewer 추가 → R-9 (권고)**.
- **G-B1**: B 의 거짓 안전감 표지 8 종 — 강력. CRITICAL/HIGH 4 종 (T-B-1~T-B-4) 은 R-1~R-3 답습. MEDIUM 4 종 (T-B-5~T-B-8) 은 brief v1.1 §6 거짓 안전감 표지 명문 의무 — **Reviewer 통합 → R-1 + R-6 답습**.
- **G-B2**: B 의 R-B-11 (본 합의 자체 ceremony 인플레이션 risk self-진단) — 누락. **Reviewer 추가 → R-10 (NOTE)**.
- **G-C1**: C 의 (q) cycle schema (R-C-3 BLOCKING) — `num_predict` 인자 + prompt 길이 동일 + N=3 + 3 metric 별도 기록. **R-3 답습 (Reviewer 통합)**.
- **G-C2**: C 의 R-C-9 (동급 cluster qwen2.5-coder ≈ exaone3.5 명문) — 누락. **Reviewer 추가 → R-11 (권고)**.

---

## 2. Reviewer 통합 — BLOCKING 7 + 권고 5 + NOTE 1

### BLOCKING (brief v1.1 보강 의무 — 합의 결과 진입 자격 조건)

| R-# | 강도 | 요지 | 반영 위치 (brief v1.1) |
|----|------|----|----|
| **R-1** | CRITICAL | **raw 4 모델 evidence 손실 명문 + ranking 표 재현 가능성 비대칭성 명시** — §2 ranking 표에 raw verifiable 3 모델 (llama3.3 / qwen3-coder-next / exaone4) 와 commit log 한정 4 모델 (qwen3-30b-a3b / glm-4.7-flash / qwen2.5-coder / exaone3.5) 분리 또는 마커 (예: `†` = commit log 한정). §2.1 측정 신뢰도에 "raw 손실 4 모델 = git tracked 0 + 덮어쓰기 = verifiable 0" 답습. P-1 답습. | §2 + §2.1 |
| **R-2** | CRITICAL | **M3 후보 표 재정비** — M3-A vs M3-C 이분법 → M3-F (default + 교체 자유 양립) 신규 행 추가 + ADR-011 §2.1 (a)~(d) 4조건 답습 명문. 현 `OllamaBoss(model: str)` 답습 = default 0건 + caller 명시 의무 = Provider Liquidity 헌법 5조-2 line 77~80 정합. M3-A *단독* 권고 자격 0건 명문. P-2 답습. | §3.1 |
| **R-3** | CRITICAL | **(q) 응답 길이 통제 cycle *선행* 의무 명문 + schema 권고** — `num_predict=128` (또는 32/64) 고정 + prompt 길이 동일 + N=3 + warmup 1 + decode/prefill/wall-clock 3 metric 별도 기록 + within-CoV 우선 검증. (q) 미실행 시 본 cycle ranking 의미 약함, "default *후보* 권고 한정" 약한 형태 명문. P-3 답습. | §3.3 (Q3) + §5 + §6 |
| **R-4** | HIGH | **이전 합의 R-3 (§12 옵션 E Ollama binary 출처) + R-5 (F1/F2 Phase 1 cycle) 미해소 본 brief 본문 명문** — Phase 1 cycle = C-c (cache miss 분리) + C-a (활성 파라미터 HF egress) + A-진단 (nvidia-smi dmon / NVBandwidth) 진행 0건 답습. P-4 답습. | §2.1 + §6 |
| **R-5** | HIGH | **§3.1 M3-A/M3-F 행 단점 칼럼에 "운영 안정성 evidence 0 / 한국어 능력 미측정 / 코드 정확도 미측정 / Ollama bartowski quant 출처 답습" 4 항목 명문** — 보스 자격 본질 미평가. 속도만으로 의사결정 부적합 명문. P-5 답습. | §3.1 |
| **R-6** | HIGH | **§3.3 위에 "권고 *온전* 자격 옵션" 부속절 추가** — M3-D + M4-A *연기 유지* 한정. M3-A/M3-C/M3-E/M3-F 모두 R-1~R-5 미해소 시 권고 자격 0. **본 cycle anchor risk self-진단 명문** — brief→합의→commit→push→사용자 결정 chain 의 자동 진입 차단. P-6 답습. | §3.3 + §0 |
| **R-7** | MEDIUM | **§6 비-scope 에 "본 cycle 후속 'M3·M4 *고정* cycle' 의 *필요 evidence 6 종 카탈로그*" 명문** — (i) raw 재측정 + git tracking + freeze (ii) 응답 길이 통제 (iii) 한국어 능력 평가 (iv) 코드 정확도 평가 (v) Ollama binary 출처 정정 (§12 옵션 E) (vi) ADR-011 §2.1 4조건 충족 검증. 본 cycle = 6 종 *식별* 한정, 충족 0건. B 의 R-B-B5/R-B-9 답습. | §6 |

### 권고 (R-8 ~ R-12)

| R-# | 요지 |
|----|----|
| **R-8** | Boss prompt 4 도메인 (code/shell/file/general) × 7 모델 동작 검증 cycle 별도 brief — A 의 R-A-3 답습. mode collapse 회피 (commit `35d64f3` 답습) 검증 의무. |
| **R-9** | "bartowski" 제3자 quant 출처 정정 cycle 별도 brief — A 의 R-A-5 답습. 공식 Qwen3 release vs bartowski quant 차이 검증 0. M3-F default 변경 시 모델 출처도 means 의 일부 (ADR-011 §2.1 답습). |
| **R-10** | 본 합의 자체 ceremony 인플레이션 risk self-진단 — B 의 R-B-11 답습. 본 cycle 4 단계 (brief → 합의 → commit → push) = 단순 평가 자격 충족. REVISE 가 단순 보강 패턴 ([[ceremony-inflation]] 답습). |
| **R-11** | §2 ranking 표에 "동급 cluster" 칼럼 — C 의 R-C-9 답습. qwen2.5-coder ≈ exaone3.5 (dense 32B Q4 동급 ~4.85 tok/s) cluster 식별. *다른* 신호 (정확도·한국어·코드·라이센스·context window) 미측정 명문. |
| **R-12** | M3-E 카탈로그 9 후보 식별 확장 — C 의 R-C-4 답습. MLC-LLM / llamafile / TGI / SGLang / vLLM 재확인 / ktransformers / TensorRT-LLM (비권고) / ExecuTorch (비권고) / Hermes-LiteLLM. 측정·채택 0, 식별만. MVP-2 brief 신규. |

### NOTE (참고 — 본 cycle 범위 외)

| N-# | 요지 |
|----|----|
| **N-1** | M3-G (task-domain 별 default routing) — C 의 R-C-7 답습. MVP-2 별도 brief 적격 (사람 게이트 적격 평가 영역). 본 합의 시점 식별만. |
| **N-2** | M4-D (UX wall-clock metric) — 이전 합의 NOTE 답습 + C 의 R-C-6 답습. glm-4.7-flash latency 101.93s = tok/s rate 단독 → UX 매핑 부적합 evidence 강화. 별도 brief. |
| **N-3** | 한국어 능력 측정 (exaone family) cycle — C 의 R-C-8 답습. boss role 본질 평가 입력. MVP-2 brief 신규. |

---

## 3. 이전 합의 BLOCKING 5 (R-1~R-5) 본 cycle 답습 매트릭스

3 Agent 매트릭스 통합:

| 이전 R-# | 요지 | A | B | C | Reviewer 합 |
|---------|------|---|---|---|----|
| **R-1** | dense effective BW 31% (F4 추가) | ❌ 미해소 | ❌ 미해소 | ⚠️ 부분 (dense 4.82-4.89 일관 답습, 진단 0) | **❌ 미해소** — Phase 1 cycle 별도 진입 |
| **R-2** | 옵션 매트릭스 위 권고 자격 검증 명문 | ❌ 미해소 (부분) | ⚠️ 부분 (§3.1 표 + §3.3 형식 유사) | ⚠️ 부분 (M3-A vs M3-C false dichotomy = anchor 동형) | **⚠️ 부분 해소** — 본 cycle R-6 명문 의무 |
| **R-3** | §12 옵션 E cross-ref 강화 | ❌ 미해소 | ❌ 미해소 | ❌ 미해소 | **❌ 미해소** — R-4 + R-9 답습 |
| **R-4** | M4-B framing 영구 거부 | ✅ 해소 | ✅ 해소 | ✅ 해소 | **✅ 해소** — brief §3.2 명문 PASS |
| **R-5** | F1/F2 Phase 1 cycle | ❌ 미해소 | ❌ 미해소 (delegated) | ❌ 미해소 | **❌ 미해소** — R-4 답습, 별도 cycle |

**해소율**: 1/5 PASS (R-4) + 1/5 부분 (R-2) + 3/5 미해소 (R-1·R-3·R-5).

**의미**: 이전 합의 BLOCKING 5 중 4/5 가 본 cycle 시점에도 해소 0 또는 부분. M3·M4 *고정* 권고 자격 0건 = 3 Agent 모두 동의. 본 cycle 합의 = **brief v1.1 보강 의무 + M3-D + M4-A 연기 유지 + Phase 1 cycle 별도 진입** 한정.

---

## 4. 최종 합의 권고

### 4.1 본 cycle 권고 (사용자 결정 입력)

| 항목 | 권고 |
|------|------|
| **M3 (런타임/모델 결정)** | **M3-D 연기 유지** — *추가 측정* cycle 권고. M3-F (default + 교체 자유 양립) **신규 후보 식별만** (코드 변경 0 답습, ADR-011 §2.1 4조건 평가는 별도 cycle). M3-A 단독 채택 권고 자격 0건. |
| **M4 (threshold 결정)** | **M4-A 연기 유지** — threshold *고정* 부적합 (raw 손실 + 응답 길이 미통제 + quality 미측정 = threshold 기준 부재). M4-D (UX wall-clock metric) framing 별도 cycle (NOTE). M4-B 영구 거부 명문 보존. |
| **본 cycle scope** | **권고 한정** — M3·M4 *고정* 자체 = 사용자 명시 의무, 본 cycle 범위 외. 본 합의 = brief v1.1 보강 의무 7 + 권고 5 + NOTE 3 명문. |

### 4.2 brief v1.1 보강 후 합의 결과 채택 — 진입 자격 조건

본 cycle 의 합의 결과 (M3-D + M4-A 연기 유지 권고) 가 *발효* 되려면:

1. **R-1 ~ R-7 BLOCKING 7 건 brief v1.1 본문 반영** (생략 0건)
2. **사용자 명시 검토 + 합의 결과 채택** (자동 진입 0건)
3. **brief v1.1 + 본 합의 보고서 git commit 1 회** + push

본 cycle 의 *후속* 작업 (자동 진입 0건, 사용자 결정 영역):

- **(q) cycle**: 응답 길이 통제 측정 — R-3 + R-C-3 schema 답습
- **Phase 1 cycle**: F1/F2 검증 (C-c cache miss + C-a HF egress + A-진단 nvidia-smi) — 이전 R-5 답습
- **§12 옵션 E 정정 cycle**: Ollama binary 출처 미상 trigger 평가 — 이전 R-3 답습
- **R-8 ~ R-12 권고 cycle**: 모두 별도 brief 신규
- **M3·M4 결정 *고정* cycle 진입**: R-7 의 6 종 evidence 충족 *후*, 사용자 명시 + 별도 풀 3+1 합의 적격

### 4.3 사용자 결정 영역

본 합의는 *권고* 한정. 사용자가 결정할 영역:

| 영역 | 권한 |
|------|------|
| brief v1.1 보강 진행 여부 | ✅ 사용자 명시 |
| 합의 결과 (M3-D + M4-A 연기 유지) 채택 | ✅ 사용자 명시 |
| 후속 (q) / Phase 1 / §12 옵션 E / R-8~R-12 cycle 진입 | ✅ 사용자 명시 + 별도 brief |
| `OllamaBoss(model="...")` default 신설 (M3-F 채택) | ✅ 사용자 명시 + 별도 cycle (코드 변경 = 헌법 5조-2 정합 검증 의무) |
| M3·M4 *고정* cycle 진입 | ✅ 사용자 명시 + 별도 풀 3+1 |
| 본 합의 폐기 / 정정 | ✅ 사용자 결정 |

---

## 5. 본 합의 자격 한계 (정직성 노트)

- 3 Agent 모두 다른 Agent 출력 미참조 (편향 방지 답습) — Reviewer 만 통합
- 본 합의 = 권고 한정. M3·M4 *고정* 자동 진입 0건
- 측정 실행 0 / 빌드 0 / 코드 변경 0 / Ollama 변경 0 / pull 0
- 본 합의 자체 = **ceremony 인플레이션 risk** (R-10 답습) — brief → 합의 → commit → push 4 단계, 단순 평가 자격 충족. 자비스 self-improvement cycle 의 정직성 명문
- **본 합의가 *발효*하는 것 = 권고 보고서 commit/push** 한정. brief v1.1 보강 / 후속 cycle 진입 / 코드 변경 / 사용자 결정 = 본 합의 *외* 영역
- 본 합의 보고서 = `docs/review/3plus1-consensus-2026-05-26-jarvis-mvp1-m3-m4-fixation.md` 1 파일. brief v1.1 미반영 시 권고 결과 채택 자격 0 (R-1~R-7 BLOCKING 답습)

---

## 6. 답습 출처

- 이전 합의: `docs/review/3plus1-consensus-2026-05-23-jarvis-mvp1-m3-m4-decision.md` (`9ddec1b`)
- 이전 brief: `docs/phase0/jarvis-mvp1-m3-m4-decision-consensus-entry-brief.md`
- 본 cycle brief: `docs/phase0/jarvis-mvp1-m3-m4-fixation-brief.md` (v1)
- 본 cycle 측정: (p) `beac955` (4 모델) + (r) `a20d3ca` (3 모델)
- ADR-011 §2.1 (a)~(d) 4조건
- 헌법 5조-2 line 77~80 Provider Liquidity
- CLAUDE.md §3 풀 3+1 매트릭스
- [[v00-sprint-pending]] (s) 답습
- [[ceremony-inflation]] / [[meta-cycle-warning]] / [[provider-liquidity]] / [[proportionate-security-personal-tool]] / [[project_minimize_user_intervention]]

---

**최종 판정 = APPROVE w/ COND (HIGH)** — brief v1.1 보강 의무 R-1 ~ R-7 + 합의 결과 (M3-D + M4-A 연기 유지) 로 진입 가능. **M3·M4 결정 *고정* 권고 자격 = 본 cycle 시점 충족 0건**.
