# Agent B (품질/안전성 검증가) — MVP-2 Implementation Evidence PASS 발효 brief 검토

> **관점**: "MVP-2 PASS가 정당한가? scope가 정직한가?" — 보안, 권위 정합, means-vs-ends
>
> **검토 대상**: `docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md` (v1, §0~§9)
>
> **권위 cross-check (직접 read)**: ADR-011 §2.1 (a)~(d) (line 52~61) + ADR-012 §4 (line 440~484) + §2.8 R-S1 (line 276) / 32 MVP-1 PASS 합의 / 60 GP-2 detection-layer PASS brief v1.1 / 59 Layer 통합 PASS brief v1.1
>
> **다른 Agent(A/C) / 외부 LLM 미참조** (편향 방지)
>
> **작성**: 2026-05-28 (62번째 entry cycle — 신규 세션 #2)

---

## verdict: **APPROVE WITH CONDITIONS**

**BLOCKING 2 (R-B-1 ~ R-B-2) + 권고 4 (N-B-1 ~ N-B-4) + NOTE 5 (NT-B-1 ~ NT-B-5)**

본 brief 는 이번 세션 consensus 가 잡은 3 over-claim (β L-1 stdlib / 59 권위 전도 / 60 GP-2 full→detection-layer) 의 교훈을 **대체로 정직하게 답습**했다. §3 가 prevention deferred / Layer 3/5 / 2a no-op 을 명문하고, §2 (a) cell 을 "⚠️" 로 정직 표기하며, "Implementation Evidence PASS" 명칭이 32 MVP-1 PASS 동형이다. **4번째 over-claim 은 아니다** — 단 §1/§2 결론의 "(a)~(d) 충족" 단언 표현 + §0.2 #2 의 "full GP-2 PASS = deferred trajectory" 라벨에 잔여 over-claim 소지가 있어 BLOCKING 2 로 정정 요구한다.

---

## §1 권위 정합 검증 (직접 line 인용)

### §1.1 ADR-011 §2.1 = (a)~(d) 4조건만 (e 없음) — brief framing **정확**

ADR-011 §2.1 line 52~61 직접 인용:

```
대체 수단은 다음 4조건을 모두 충족할 때 기존 수단을 대체할 수 있다:
| (a) | 동등 이상의 보안 결과 |
| (b) | 격리 환경 PoC로 실증 |
| (c) | ADR 권위로 명시 |
| (d) | 자동 회귀 검증 경로 확보 |
```

→ ADR-011 §2.1 = **(a)~(d) 4조건. (e) 부재 확인**. brief §0.3 / §2 header / §9 P-6 의 "ADR-011 §2.1 = (a)~(d) 모법" framing 은 **정확**. 59 B-2 (line 280) / 60 N-1 (line 133, 238) 에서 이미 권위 전도가 정정·답습된 형태. **59/60 권위 전도 재발 0**.

### §1.2 ADR-012 §4 = "(a)~(d) + (e) 5조건 답습", (e) = 합의 APPROVE — brief framing **정확**

ADR-012 §4 line 440~442 직접 인용:

```
## 4. ADR-011 §2.1 (a)~(d) + (e) 5조건 답습 (Means-vs-Ends Pattern)
본 ADR-012 는 ADR-011 §2.1 5조건 패턴 답습 (수단/목적 분리):
```

ADR-012 §4 (e) line 482~484:

```
### (e) 합의 APPROVE
본 PR-2 풀 3+1 + 외부 LLM 2건 합의 (5/5 입력 APPROVE WITH CONDITIONS)
```

→ (e) 는 ADR-012 가 *신설한 5번째 보안 조건* 이 아니라, ADR-011 (a)~(d) 에 **"합의 APPROVE" 라는 절차 조건을 더해 5조건 패턴화한 것**. brief 의 "(e2)" = 프로젝트 내부 label (60 N-1 line 133 명시: "(e2) PASS 발효 / (e1) 진입 권한 분리, ADR 본문 문자열 아님"). brief §2 header line 70 가 이 단서를 답습 ("(e2) = ADR-012 §4 확장 + 프로젝트 내부 label") → **정확**. **단 §0.3 #1 (line 47) 의 "ADR-012 §4 (a)~(d)+(e) 확장" 표현은 brief 본문 §2 의 "(e2)" 와 라벨 일관성이 약함 → N-B-1**.

### §1.3 R-S1 / Layer numbering 정합 — brief §3 **정확**

ADR-012 §2.8 line 276 (R-S1 canonical) 직접 인용:

```
canonical numbering (R-S1 cross-reference, 2026-05-28): 본 §2.8 5-layer =
provider-agnostic-memory-skill-design.md §4.4.1 (PRIMARY) 동형 — cross-document
"Layer N" 참조 canonical (Layer 4 = CI 회귀 검증, Layer 5 = External anchor).
MVP-2 "Layer 1+2+4" = 본 §2.8 5-layer 기준 (hash + git append-only + CI 회귀 검증).
```

→ canonical = Layer 4 = CI 회귀 검증, Layer 5 = External anchor. brief §3 line 95 "Layer 3 (Signed commit) + Layer 5 (External anchor) = scope 외" + line 89 "Layer 4 (CI 회귀 검증) operative green" = **정확**. "Layer 1+2+4" = hash + git append-only + CI 회귀 검증 = 5-layer 기준 정합. **Layer numbering over-claim 0**.

---

## §2 BLOCKING

### R-B-1 ⭐ (scope over-claim, 60 GP-2 강등 부분 복원 risk) — §0.2 #2 + §1 결론 + §2 결론의 "(a)~(d) 충족" 단언이 GP-2 (a) partial 을 은폐

**문제**: 60 (line 5, 96, 137) 에서 GP-2 의 **(a) 동등 이상 보안 결과 = "⚠️ partial (설계 동등성 한정)"** 로 강등됐다 — governance §4 (a) = R-1/R-2 prevention 검증인데 in-repo 입증 0 (Hermes upstream 위임). 본 brief §2 매트릭스 (a) cell (line 74) 은 이를 **정직하게 "⚠️"** 로 표기했다 (over-claim 0, 양호).

그러나 다음 3 위치는 GP-2 (a) partial 을 **"충족" 으로 단언**하여 60 강등을 부분 복원할 risk:

1. **§1 audit 결론 (line 64)**: "→ 3 의존성 모두 발효 — MVP-2 Implementation Evidence PASS 발효 자격 충족 ((e2) = 본 cycle)." — GP-2 의존성을 "발효" 로 표기하나 그것이 *detection-layer PASS* 임을 이 줄에서 누락 (§1 표 cell 에는 있으나 결론 줄에서 소실).
2. **§2 결론 (line 80)**: "→ **(a)~(d) 충족** (GP-2 (a) = detection + prevention deferred 명문)." — "(a)~(d) 충족" 단언 + 괄호로 GP-2 (a) 한정. 그러나 GP-2 의 (a) 는 60 에서 **partial (full 미충족)** 로 강등됐으므로, MVP-2 통합 (a) 를 "충족" 으로 단언하면 60 강등이 통합 layer 에서 흐려진다.
3. **§5 line 128 + line 140**: "(a)~(d) 충족" 반복.

**59 Layer PASS 와 비대칭**: 59 의 (a) (line 151) 는 Layer 1/2/4 모두 **operative ✅** (2a DEFER 도 2b+CI 이중 cover 로 ends 충족) — (a) full 충족. **GP-2 의 (a) 는 prevention 능동 redaction 이 in-repo 0 (60 §2 축3 line 98~104) 이므로 ends(secret 송신 leak 0) 의 prevention 측면이 in-repo cover 0** (60 B-2 line 125: "in-repo layer 0, Hermes upstream 단독 위임, cover 구조 비대칭"). 즉 **MVP-2 통합 (a) 는 "ledger 무결성 (a) full + GP-2 송신 redaction (a) partial" 의 혼합인데, "(a)~(d) 충족" 단언은 이 비대칭을 평탄화**한다.

**정정**:
- §1 결론 (line 64): "3 의존성 모두 발효 (GP-2 = **detection-layer** PASS, full GP-2 prevention 미발효)" 로 detection-layer 한정 명문.
- §2 결론 (line 80) + §5 (line 128/140): "(a)~(d) 충족" → **"(a) = ledger 무결성 full + GP-2 detection (prevention deferred → (a) GP-2 측 partial), (b)~(d) 충족"** 로 (a) 의 혼합/partial 성격을 결론 줄에서 명문. 60 B-1 강등 (line 5) 을 통합 layer 결론에서 평탄화 0.
- 근거: 60 line 96 "(a) full 충족 = R-1/R-2 prevention 선행 (deferred)" + 60 line 137 "(a) ⚠️ partial".

### R-B-2 (scope over-claim, "full GP-2 PASS = deferred trajectory" 라벨이 means-ends hole 은폐) — prevention runtime in-repo 0 인데 "trajectory" 표현이 "곧 발효될 경로" 로 오독

**문제**: brief §0.2 #2 (line 33) "full GP-2 PASS (prevention R-1/R-2 = deferred trajectory)" + §3 line 93 "full GP-2 PASS = MVP-2 PASS 후속 trajectory" + §7 #3 line 154 "full GP-2 PASS trajectory". "trajectory" 라는 단어는 **"이미 궤도에 올라 진행 중인 경로"** 를 함의 — 그러나 실상은:
- R-1 = Hermes upstream runtime redaction = **본 repo import 결정조차 0** (60 line 102 "import 결정 별도 cycle", Hermes v0.12.0 에 DB INSERT redaction 부재 = ADR-011 §1.2 G1a FAIL 의 redaction 모듈은 송신용, line 22~26).
- R-2 = facade real (TR-1) = **placeholder** (60 line 103).

즉 prevention 능동 redaction 은 in-repo 0 이고 Hermes upstream 위임이며, R-1 import 결정 cycle 도 아직 미진입. "trajectory" 는 진행성을 과대 함의하여, **"MVP-2 PASS = 송신 redaction prevention 이 곧 보증됨" 으로 오독될 means-ends hole**. ADR-011 §2.3 #2 (line 113) 은 "Hermes 자체 redaction 은 로그/LLM 송신 방어로만 신뢰" 라고 하나, brief 가 강조해야 할 것은 **"본 repo 의 GP-2 PASS 는 detection (CI 검출) 만 in-repo operative, prevention 능동 차단은 in-repo 보증 0 (Hermes 안전성 미선언, ADR-011 §7.3 / ADR-012 §3.3 답습)"**.

**정정**:
- "deferred trajectory" → **"deferred — in-repo 입증 0 + R-1 import 결정 미진입 (Hermes upstream 위임, 진행 보증 아님)"** 명문. ADR-011 §7.3 line 237 "본 ADR 은 Hermes 안전성을 선언하지 않는다" + ADR-012 §3.3 line 416 답습.
- §3 결론 (line 98): "prevention runtime ... deferred (over-claim 0, 정직 scope)" 에 **"in-repo 능동 redaction 보증 0 (Hermes safety 미선언)"** 추가. 60 B-2 line 124~125 (in-repo 능동 redaction 보증 0) 직접 답습.
- 근거: ADR-011 line 237 + ADR-012 line 414~416 (content-level / 안전성 미선언 한계) + 60 line 124.

---

## §3 권고 (N-B-N)

### N-B-1 — §0.3 #1 (line 47) "(a)~(d)+(e) 확장" vs 본문 "(e2)" 라벨 일관성

§0.3 line 47 은 "ADR-012 §4 (a)~(d)+(e) 확장" 인데 본문 §2 (line 78) 는 "(e2)". 60 N-1 (line 133, 238) 이 "(e2) = 내부 label, ADR 본문 문자열 아님" 을 명문화했으므로, §0.3 에도 "(e) = ADR-012 §4 합의 APPROVE 조건, (e2) = 본 프로젝트 PASS 발효 내부 label" 단서 1줄 추가 권고. (BLOCKING 아님 — §2 header line 70 에 단서 존재, 라벨 cascade 일관성 한정.)

### N-B-2 — §1 표 GP-2 cell (line 61) "detection operative" 와 §2 (a) cell (line 74) "⚠️" 의 충족 라벨 cascade

§1 표 line 61 GP-2 cell = "R-3 detection operative + R-4 설계 동등성 + ADR 권위. prevention = deferred trajectory" (정직). §2 (a) cell line 74 = "⚠️ detection ✅ / prevention deferred" (정직). 두 cell 자체는 양호하나, R-B-1 의 결론 줄 평탄화와 결합 시 cell↔결론 비대칭. R-B-1 정정 시 자동 해소되나, §1 표 GP-2 cell 의 "발효 ✅ 60 entry" 표기 옆에 "(detection-layer)" 명문 권고 (line 61 첫 cell).

### N-B-3 — MVP-1 PASS 일관성 명문 강화 (32 답습)

brief §3 line 86 "MVP-1 PASS 32 동형 — Implementation Evidence = 구현 evidence, runtime 보증 아님" 은 정확하다. 32 합의 (line 91) "PASS 효과 영향 0건 (보안 효과 한정)" + (line 5) "Implementation Evidence PASS" framing 과 본 MVP-2 PASS 가 **일관적**이다 (둘 다 in-repo evidence, runtime 보증 아님). 단 32 는 GP-3/GP-5 (a) 가 full 충족이었던 반면 (32 §3.2), **본 MVP-2 는 GP-2 (a) 가 partial** 이라는 차이를 §3 에 1줄 명문 권고 — "32 MVP-1 PASS = 5/5 조건 full, 본 MVP-2 = GP-2 (a) partial (prevention deferred) 차이 = solo 1-host 비례 + upstream 위임 구조 차이". (일관성 자체는 유지되나 (a) 강도 차이 명문이 정직.)

### N-B-4 — §5.1 발효 효과 line 137 "governance §4 (GP-2) cross-reference (선택)" 의 R-S1 numbering 정합

§5.1 line 137 "governance §4 (GP-2): detection-layer PASS + prevention deferred cross-reference (선택)" — governance-preconditions §4 본문 갱신은 §0.2 #9 (line 40) 에서 금지됐으므로 "(선택)" 이 맞으나, 갱신 시 R-S1 canonical numbering (ADR-012 §2.8 line 276) 준수 의무를 1줄 명문 권고 (60 PASS 가 governance §4 (a) line 451 = prevention 검증임을 명시했으므로, cross-ref 시 (a) partial attribution 정합 필요).

---

## §4 NOTE (NT-B-N)

### NT-B-1 — 자기진단 §9 P-2/P-3 가 R-B-1/R-B-2 를 *부분* 선제 처리

brief §9 P-2 (line 173) "MVP-2 full PASS over-claim (60 재발)" + P-3 (line 174) "GP-2 detection-layer 를 full GP-2 로 격상" 은 R-B-1/R-B-2 와 동일 risk 를 자기진단에 등록했다 (메타 편향 회피 양호). 그러나 자기진단 등록 ≠ 본문 결론 줄 정정 — R-B-1/R-B-2 는 본문 §1/§2/§3 결론 줄의 단언 표현 자체를 정정 요구. P-2/P-3 의 "처리" 가 §3 (정직 scope) 까지만이고 §1/§2 결론 줄까지 미도달.

### NT-B-2 — scope 침입 0 확인 (full GP-2 PASS / Layer 3/5 / R-1 import / R-2 facade / MVP-3~6 / roadmap 본문 자동 갱신)

§0.2 표 (line 30~43, 12 항목) + §6 금지 (line 146) cross-check 결과 **scope 침입 0**:
- full GP-2 PASS 발효 = §0.2 #2 (0) + §6 명문.
- Layer 3/5 발효 = §0.2 #3 (0, "부분 답습" 영구).
- R-1 import / R-2 facade = §0.2 #4 (0).
- MVP-3~6 = §0.2 #7 (0) + §5 #3 (line 132 "본 PASS 무관").
- roadmap/governance 본문 자동 갱신 = §0.2 #9 (line 40 "발효 후 §5") + §5.1 (line 136 "별도 commit, 발효 후") + §6 (line 146).
→ **scope 침입 BLOCKING 0**. 발효 ≠ 합의 입력 분리 (§0.2 #1) 도 명확.

### NT-B-3 — means-vs-ends 핵심: MVP-2 PASS 정당성

MVP-2 PASS = (operative) ledger 무결성 (Layer 1+2+4) + GP-2 detection CI + 설계/ADR 권위. **prevention runtime 이 in-repo 0 인데 "MVP-2 PASS" 가 정당한가?** → **정당하다 (단 명칭 한정 하에)**:
- 32 MVP-1 PASS 도 "Implementation Evidence PASS" = in-repo 구현 evidence (runtime 보증 아님, 32 line 91 "PASS 효과 영향 0건 보안 효과 한정"). 본 MVP-2 도 동형.
- ledger 무결성 = in-repo full operative (59 검증). GP-2 detection = in-repo CI operative (60 검증). prevention 능동 redaction 만 upstream 위임 (ADR-011 §2.3 #2 권위).
- 즉 "MVP-2 **Implementation Evidence** PASS" 라는 정확한 명칭 하에서는 means-ends hole 없음. **단 "MVP-2 PASS" 로 축약되어 runtime 완전 보증으로 오독될 때 hole 발생** → R-B-1/R-B-2 가 이를 차단. brief 가 일관되게 "Implementation Evidence PASS" full 명칭을 쓰면 정당.

### NT-B-4 — 메타-cycle / 작성자 cascade 인지 (§9 P-4)

brief §9 P-4 (line 175) = 작성자 = 59/60/61 작성자 (Claude) cascade → cross-vendor codex + 풀 3+1 독립 검증으로 청산. 본 검토 (Agent B) 도 Claude 패밀리 — 동일 한계 인지. ADR-012 §11.1 (line 632~640) 메타-순환 청산 4 매커니즘 답습 필요 (사후 외부 LLM 충족 = (E-α) codex 의무).

### NT-B-5 — "MVP-2 Implementation Evidence PASS" 명칭의 runtime 오독 risk

질문 1 (명칭 오독): "MVP-2 Implementation Evidence PASS" 명칭 자체는 32 동형으로 **runtime 완전 보증으로 오독될 risk 낮음** ("Implementation Evidence" = 구현 evidence 명시). 단 brief 가 §1/§5/§7 에서 "MVP-2 PASS" 로 축약하는 위치 (line 64, 132, 138, 154) 가 다수 — 축약 시 runtime 보증 오독 risk. R-B-1/R-B-2 정정 + 축약 위치에 "Implementation Evidence" 보존 권고 (NT 한정, BLOCKING 아님).

---

## §5 verdict 종합

| 임무 항목 | 판정 | 근거 |
|---|---|---|
| 1. scope 정직성 (4번째 over-claim?) | ⚠️ **부분 (R-B-1/R-B-2)** | §2 (a) cell "⚠️" + §3 deferred 명문 = 정직 (over-claim 아님). 단 §1/§2/§5 결론 "(a)~(d) 충족" 단언 + "trajectory" 라벨 = 잔여 over-claim 소지 |
| 2. means-vs-ends | ✅ (R-B-2 조건) | "Implementation Evidence PASS" 정확 명칭 하 정당 (32 동형). prevention in-repo 0 = upstream 위임 (ADR-011 §2.3 #2). R-B-2 = "trajectory" 진행성 과대 정정 |
| 3. 권위 인용 정확성 | ✅ | ADR-011 §2.1 = (a)~(d) (e 없음) 정확 / ADR-012 §4 (e)=합의 APPROVE 정확 / (e2)=내부 label 단서 답습 / R-S1 numbering 정확. 59/60 권위 전도 재발 0 |
| 4. MVP-1 PASS 일관성 | ✅ (N-B-3 강화) | 32 Implementation Evidence framing 동형. GP-2 (a) partial 차이만 명문 권고 |
| 5. scope 침입 | ✅ **0** | full GP-2 / Layer 3/5 / R-1 import / R-2 facade / MVP-3~6 / roadmap 본문 자동 갱신 모두 0 (NT-B-2) |

**verdict: APPROVE WITH CONDITIONS** — BLOCKING 2 (R-B-1 결론 줄 (a) partial 평탄화 정정 + R-B-2 "trajectory" 진행성 과대 정정) 1pass 흡수 후 MVP-2 Implementation Evidence PASS 발효 자격 인정. 권위 정합 정확 (59/60 전도 재발 0), scope 침입 0, 32 일관. 본 brief 는 **4번째 over-claim 이 아니다** — §2/§3 의 정직 scope 명문이 60 교훈을 답습했고, 잔여 2건은 결론 줄 표현 정정 한정이다.

---

**본 Agent B 검토 끝.**
