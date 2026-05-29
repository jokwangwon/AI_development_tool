# Agent C (대안 탐색가) 독립 분석 — MVP-2 GP-2 송신 redaction PASS 발효 (60 entry)

> **관점**: "더 나은 판단/형태가 있는가?" — 다른 Agent(A/B) / 외부 LLM(codex) 응답 미참조 독립 분석.
>
> **검토 대상**: `docs/phase0/mvp2-gp2-pass-activation-brief.md` (v1, §0~§10)
>
> **입력 답습**: 51 audit (GP-2 Exit 5조건) + 59 Layer 1+2+4 통합 PASS brief v1.1 (PASS 발효 형태) + 32 MVP-1 PASS 합의 (PASS 발효 형태 + Agent C (β) 기각 선례)
>
> **작성**: 2026-05-28

---

## verdict

**APPROVE WITH CONDITIONS**

brief 권고 (APPROVE WITH CONDITIONS, C-1~C-3) 의 *발효 형태* 는 59 Layer PASS + 32 MVP-1 PASS 와 일관적이며, "detection-only PASS" 자체는 부당하지 않다 (means-vs-ends 정합). 단 **BLOCKING 1건** — brief 의 (a) evidence 매핑이 ADR-011 §2.1 모법 (a) 의 *대체 수단 동등성* 의미를 prevention deferred 상태에서 over-claim 하는 framing 결함 (권위 전도 risk, 59 B-2 동형 재발) — 정정 후 APPROVE 자격. 4 대안 ((a)~(d)) 中 brief 권고 ((c) detection PASS + prevention deferred) 가 dominant, 나머지 3 기각.

---

## §1 핵심 대안 판단 — 4 발효 형태 비교 (임무 1)

brief §6 권고 = APPROVE WITH CONDITIONS (C-1 prevention deferred 명문 + C-2 R-5 known limitation + C-3 secret-hygiene actual run). 대안 4개를 평가:

| 대안 | 내용 | 평가 | 기각/채택 사유 |
|------|------|------|--------------|
| **(a)** 무조건 APPROVE | C-1~C-3 조건 없이 PASS | ❌ 기각 | prevention(R-1/R-2) 본 repo 동작 0 + R-5 base64 미커버 = honest matrix 의무 위반 (P-2 risk 직접 발화). 조건 명문 없이는 "빈 껍데기 PASS" risk 현실화 |
| **(b)** REVISE — prevention 선행 | R-1/R-2 미충족이므로 PASS 보류, prevention 구현 선행 | ❌ 기각 | **57 (β) 결정 (`18e8ad1`) 직접 위반** — R-3 detection 우선 + R-1/R-2 prevention deferred 는 *이미 합의 발효된 trajectory*. 본 cycle 에서 재논의 = 24 entry 답습 cascade + ceremony-inflation. 또한 본 repo = DESIGN repo 이므로 Hermes import(R-1) 선행 강제는 Provider Liquidity 와 충돌 ([[feedback_provider_liquidity]]) |
| **(c)** detection PASS + prevention deferred (brief 권고) | R-3 operative + R-1/R-2 deferred trajectory 명문 | ✅ **채택 (dominant)** | 59 Layer 2a DEFER 패턴 + 57 (β) 결정 + 32 MVP-1 carry-over 답습 동형. means-vs-ends 정합 (§2). 단 framing 정정 필요 (R-C-1) |
| **(d)** R-3 detection 별도 sub-PASS | detection 만 독립 PASS, GP-2 PASS 미선언 | ❌ 기각 | 32 entry Agent C "(β) 부분 PASS = 의미 0, (α) dominant" 선례 직접 답습. GP-2 = governance §4 단일 GP 단위 — sub-PASS 분할은 권위 chain 파편화 + ceremony-inflation. (c) 가 동일 효과를 단일 PASS + 조건 명문으로 달성 |

→ **(c) brief 권고 = dominant strategy**. 59 Layer PASS (Layer 2a DEFER + 2b operative 충족) 형태와 정확히 동형 — "operative 수단 1개 + DEFER 수단 1개, ends 충족 + DEFER 명문". 32 MVP-1 PASS 형태 (carry-over 명시 + PASS 효과 영향 0건) 와도 일관.

**일관성 검증 결론**: 발효 형태 자체는 59 + 32 와 일관. brief 가 4 대안 中 dominant 를 선택했다는 점에서 형태 판단은 정확.

---

## §2 detection-only PASS 의 타당성 — "빈 껍데기 PASS" risk 평가 (임무 2)

### §2.1 means-vs-ends 정합 평가 (brief §3.2)

brief 의 핵심 논리 = "ends = secret 송신/로그 leak 0. detection ends (R-3) ✅ operative. prevention ends (R-1 Hermes upstream + R-2 facade) = 별도 trajectory deferred". 이는 59 Layer 2a 패턴 ("operative 보호 = 다른 layer, 본 layer DEFER") 의 답습.

**타당성 = 조건부 인정**:
- ✅ detection (R-3 secret-hygiene D-2) 은 *실제 in-repo operative green* — actual run `26517803107` success (head_sha `4fec64859831...` = `4fec6485`, gh api 직접 검증), 코드 불변 (`4fec648..HEAD` 변경 0, git log 직접 검증). 이 점에서 59 Layer PASS (3 ledger workflow actual run green) 와 동등한 evidence 강도.
- ⚠️ 단 GP-2 의 *ends* = "secret 송신/로그 leak 0" 인데, **본 repo 에서 leak 을 능동적으로 막는(prevention) 수단은 동작 0**. R-3 는 leak 이 *이미 발생한 후 회귀 검출*(detection) 만 한다. 즉 "leak 0" ends 의 능동 보장은 Hermes upstream (R-1) 에 100% 의존.

### §2.2 59 Layer PASS 와의 비대칭 (핵심 발견)

59 Layer PASS 와 GP-2 PASS 사이에 **operative 강도 비대칭** 이 존재:

| 차원 | 59 Layer 1+2+4 PASS | 본 GP-2 PASS |
|------|---------------------|-------------|
| in-repo operative 보호 수단 | Layer 1 hash chain + Layer 2b branch protection + Layer 4 CI = **본 repo 에서 실제 보호 동작** | R-3 detection 만 (회귀 검출). **능동 보호(prevention) in-repo 동작 0** |
| DEFER 항목 | Layer 2a denyNonFastForwards (no-op, 막으려는 시나리오를 2b+rewrite-defense 가 cover) | R-1 prevention (Hermes upstream operative) + R-2 facade (placeholder) |
| ends 능동 보장 위치 | **본 repo** (Layer 1/2b/4 가 ends 직접 달성) | **Hermes upstream** (본 repo 외부) |

→ 59 에서는 DEFER 항목(2a)이 *no-op 이고 다른 in-repo layer 가 ends 를 cover* 했다. GP-2 에서는 DEFER 항목(R-1 prevention)이 *ends 의 능동 보장 본체* 이고, in-repo 는 detection 만 남는다. **이 비대칭이 "빈 껍데기 PASS" risk 의 본질** — brief P-2 가 식별한 risk 가 59 보다 GP-2 에서 더 현실적이다.

### §2.3 그럼에도 PASS 발효가 정당한 이유 (NT-C-1)

- governance §4.1 정의 자체가 GP-2 prevention 수단을 "Hermes container" + "P1 facade layer" 에 위치시킴 (line 434~435). 즉 GP-2 prevention 의 *제자리* 가 본 repo 외부라는 것은 governance 설계의 명시 전제. 본 repo (DESIGN/governance) 가 책임지는 GP-2 = 패턴 정의(R-4) + 회귀 검출(R-3) + 권위(ADR) 이고, 능동 redaction 의 *실행* 은 upstream — 이는 설계 의도이지 누락이 아니다.
- 따라서 "빈 껍데기" 가 아니라 **"detection-layer PASS (능동 redaction 실행 = upstream 위임 명문)"** 으로 framing 하면 정당. 단 brief 의 현 framing 은 이 비대칭을 §2 evidence 매트릭스에서 충분히 노출하지 않아 over-claim risk (R-C-1 참조).

**결론**: detection-only PASS 자체는 부당하지 않으나, brief 가 (a) evidence 를 *prevention 동등성* 으로 주장하면서 prevention 이 deferred 인 모순을 명확히 분리하지 않은 것이 BLOCKING (R-C-1). framing 정정 후 정당.

---

## §3 DESIGN repo vs runtime 구분 평가 (임무 3)

### §3.1 구분의 일관성 — 조건부 인정

brief §1.2/§3.2 = "본 repo = DESIGN/governance repo, 실 runtime redaction = Hermes upstream (R-1)". 이 구분은:
- ✅ governance §4.5 (a) "Hermes native redaction Tier-1 42 catalog 적용 검증" + §4.3 강제 메커니즘 위치 = "Hermes container" / "P1 facade layer" 와 정합. GP-2 의 prevention 은 설계상 upstream 위치.
- ✅ ADR-011 §2.3 #2 (line 113, 직접 검증) "Hermes 자체 redaction은 로그/LLM 송신 방어로만 신뢰" 와 정합.

### §3.2 단 Layer PASS 와의 비대칭이 framing 으로 은폐되어선 안 됨 (R-C-1 의 근거 2)

임무 3 의 핵심 질문 = "Layer PASS 는 CI/tools 가 실제 동작했음 — GP-2 의 R-1 prevention 은 본 repo 에서 동작 0". 이 지적은 정확하다 (§2.2 비대칭 표).

- 59 Layer PASS: (a) "middle tampering 차단" 은 본 repo Layer 1 코드가 *실제로 차단* 한다 (in-repo operative ends).
- GP-2 PASS: (a) "R-4 패턴 동등성" 은 *문서가 패턴이 동등하다고 명시* 할 뿐, 본 repo 가 secret 을 *실제로 redact* 하지 않는다. 실 redaction 동작은 upstream.

→ 따라서 GP-2 PASS 의 (a) 는 59 의 (a) 와 **evidence 종류가 다르다** (설계 동등성 vs in-repo operative). brief 는 §2 매트릭스에서 (a) = "✅ R-4 패턴 동등성" 으로 59 와 동일한 ✅ 를 부여하나, 이는 *동등성 설계* 이지 *operative redaction* 이 아니다. 이 차이를 §2/§3 에서 명문화하지 않으면 GP-2 PASS 가 Layer PASS 와 동일한 in-repo operative 강도를 가진 것처럼 over-claim 된다.

### §3.3 대안 — GP-2 PASS 가 runtime 까지 포함해야 하는가? (NT-C-2)

- ❌ 본 repo 에서 runtime redaction 을 강제하면 = Hermes import(R-1) 선행 강제 = Provider Liquidity 비협상 ([[feedback_provider_liquidity]]) + DESIGN repo 경계 침범. 따라서 runtime 포함은 비권고.
- ✅ 올바른 형태 = "GP-2 DESIGN/detection-layer PASS (runtime redaction = upstream 위임, R-1 import 시점 별도)". 이는 brief 의 현 구분과 동일하나, **명칭/framing 에 detection-layer 한정성을 명시** 하는 것이 (a) over-claim 을 막는다 (N-C-1 권고).

---

## §4 비례성 / ceremony 평가 (임무 4)

### §4.1 GP-2 PASS cycle 자체 = 비례적 (과잉 아님)

- ✅ GP-2 PASS = MVP-2 Implementation Evidence PASS 의 절반 (Layer PASS 59 ✅ + GP-2 본 + R-S1). MVP-2 milestone 의 필수 구성요소이므로 풀 3+1 + 외부 LLM 1+ 는 ADR-011 §2.4 T3 + 헌법 5조-2 cross-vendor 의무에 정합. 32 MVP-1 PASS / 59 Layer PASS 답습 동형 — ceremony-inflation 아님.
- ✅ §5.2 승격 trigger 2/7 발화 + 1 부분 = 풀 3+1 적격 판정 타당.

### §4.2 R-5 base64 known limitation = 비례적 (NT-C-3)

- ✅ `base64_evasion.txt` fixture (직접 read 검증) 는 미검출을 *의도적으로 문서화* 하며 workflow line 205~210 이 검출 시 오히려 `::warning` 발화. R-5 = G3-4 MVP-2/3 분리 영역. solo 개인 툴 비례성 ([[feedback_proportionate_security_personal_tool]]) 상 base64 evasion 능동 디코딩 = 과잉이며 known limitation 명문이 정직한 처리. 비례적.
- 단 NT-C-4: GP-2 ends = "송신/로그 leak 0" 인데 base64 인코딩된 secret 송신은 leak 0 을 위반한다. R-5 deferred 는 "Tier-1 42 평문 한정" 으로 GP-2 PASS scope 를 *축소* 한다는 점이 §4.1 에 명문화되어야 한다 (brief §4.1 이 이미 "Tier-1 42 catalog 평문 redaction 한정" 명시 — 충족). NOTE 한정.

### §4.3 secret-hygiene workflow_dispatch 미지원 = 비차단 (NT-C-5)

- ✅ workflow 직접 검증: trigger = push(paths) + pull_request + schedule(cron `0 3 * * *`). **workflow_dispatch 없음** (brief C-3 주장 정확). 코드 불변(git 검증) + 최근 green run 으로 evidence 유효성 충족. [[feedback_actual_run_trigger_paths_filter]] 답습 — empty commit 만으로 trigger 0 이므로 fresh run 강제는 비례적이지 않음. brief 의 "코드 불변 → 최근 green = 유효 evidence" 처리 타당.

---

## §5 누락 대안 / 리스크 (임무 5)

- **NT-C-6 (51 audit (b) "부분" → brief (b) "✅" 격상)**: 51 audit §2.2 (b) = "⚠️ Group D PoC 부분 (형식적 검출 layer 한정, 송신 redaction 영역 미커버)". brief §2 (b) = "✅". 이 격상의 근거 = D-2 scan-log redaction residual PoC. 단 D-2 는 *이미 redact 된 로그(`[REDACTED]` 마커)의 잔존 검사* 이지 *redaction 자체의 실증* 이 아니다 (`env_redacted.txt` 직접 read 검증 — 이미 마스킹된 상태). 즉 51 audit 이 지적한 "송신 redaction 영역 미커버" 는 본질적으로 여전히 유효 (prevention 은 upstream). (b) ✅ 는 *detection PoC* 한정으로는 정확하나, 51 audit 의 "송신 redaction 미커버" 우려를 (b) 가 해소한 것은 아니다. → R-C-1 framing 정정에 포함 권고 (P-3 over-claim risk 와 동일 축).
- **NT-C-7 (r2-canary = R-6 = ADR-011 모법 (d) 와의 관계)**: ADR-011 §2.1 (d) 모법 (line 59 + line 147) = "자동 회귀 = R-6 (`r2-canary.yml`)". brief 의 (d) 충족 수단 = secret-hygiene D-2 (R-3) 이지 R-6 아님. 59 Layer brief 는 r2-canary 를 "R-6/R-2 영역, 미트리거" 로 분리했다. GP-2 의 (d) 를 R-3 secret-hygiene 로 충족하는 것은 governance §4.5 (d) ("R-6 workflow 에 log file canary inject step 추가") 와 *다른 workflow*. → 비차단 (R-3 가 동등 회귀 검증 제공) 이나, brief 가 (d) 충족 수단이 모법/governance 가 상정한 R-6 가 아닌 R-3 secret-hygiene 임을 §2 (d) cell 에 명시하면 일관성 ↑. N-C-2 권고.
- **NT-C-8 (R-1 prevention 이 실제 operative 인지 본 repo 에서 입증 불가)**: brief §3.1 = "R-1 Hermes native redaction = runtime prevention = Hermes upstream operative". 단 본 repo 는 Hermes import 미결정이므로 R-1 이 실제로 operative 인지 *본 cycle 에서 증명 0*. brief 가 "Hermes runtime 자체는 redaction 수행" 으로 단정 (§3.2 line 107) — 이는 upstream 가정에 의존한 미검증 주장. PASS 비차단 (detection PASS 는 R-1 operative 여부와 독립) 이나, "R-1 operative" 단정은 약화 권고 (N-C-3).

---

## BLOCKING

### R-C-1 ⭐ — (a) evidence 매핑이 ADR-011 모법 (a) 의 *대체 수단 동등성* 을 prevention deferred 상태에서 over-claim (권위 전도, 59 B-2 동형 재발)

**근거** (직접 검증):
- ADR-011 §2.1 (a) 모법 (line 56) = "동등 이상의 보안 결과 → **명시적 비교표 (수단 A 보장 ↔ 수단 B 보장)**". R-4 (`redaction-pattern-equivalence.md`) 는 ADR-011 line 145 에서 "**대체 수단(R-2 trigger)이 기존 수단(Hermes redaction) 대비 패턴 커버리지 동등 이상**" 으로 정의 — 즉 (a) 는 *prevention 수단(R-2 trigger vs Hermes redaction) 의 동등성*.
- brief §2/§4 (a) = "✅ R-4 패턴 동등성" 으로 충족 주장하면서, 동시에 §3 에서 R-1/R-2 prevention 을 deferred 로 둔다. **(a) 가 입증하는 대상(prevention 수단 동등성) 이 deferred 인데 (a) 를 ✅ 로 격상** = 논리 모순. R-4 동등성은 "prevention 수단이 *채택되면* 동등하다" 는 설계 명시이지, "현재 prevention 이 operative 하다" 는 증거가 아니다.
- 이는 59 B-2 (ADR-011 §2.1 권위 전도 — Reviewer 가 BLOCKING 으로 흡수한 동형 결함) 의 재발 축. brief P-7 이 "권위 인용 전도 (59 B-2 재발)" 를 self-flag 했으나, framing(§4 header) 만 답습하고 *(a) evidence 의 의미* 는 여전히 over-claim.

**정정**:
- §2/§4 (a) cell 을 "R-4 = prevention 수단(R-1/R-2) 채택 시 패턴 동등성 *설계* (ADR-011 line 145) — prevention 실행은 deferred trajectory, 본 PASS 는 detection-layer + 설계 동등성 한정" 으로 명문화.
- §2 evidence 매트릭스에 "(a) = 설계 동등성 / (b)(d) = detection(R-3) operative / prevention operative = upstream 위임 (본 repo 입증 0)" 의 3-축 분리 명시 (§2.2 비대칭 표 답습). 59 Layer (a) "in-repo operative 차단" 과 GP-2 (a) "설계 동등성" 의 evidence 종류 차이를 honest 하게 노출.
- 이 정정으로 detection-only PASS 가 "빈 껍데기" 가 아닌 "detection-layer + 설계 동등성 PASS, 능동 redaction = upstream 위임 명문" 으로 정당화됨 (§2.3 + §3.3).

---

## 권고 (N-C-N)

- **N-C-1**: GP-2 PASS 명칭을 "**GP-2 detection-layer PASS**" 또는 "GP-2 송신 redaction PASS (detection operative + prevention deferred)" 로 명시적 부분 발효 framing 채택 (임무 2 의 "더 나은 framing" 답). 59 "Layer 1+2+4 *통합* PASS (부분 답습, Layer 3+5 scope 외)" framing 동형 — scope 한정을 명칭에 노출하면 over-claim 차단 + MVP-2 PASS 합의 시점 R-1/R-2 prevention trajectory 잔여 명확.
- **N-C-2**: §2 (d) cell 에 "(d) 충족 수단 = R-3 secret-hygiene D-2 (≠ ADR-011 모법/governance §4.5 가 상정한 R-6 r2-canary). R-3 가 동등 회귀 검증 제공" 명시 (NT-C-7 답습). governance §4.5 (d) ("R-6 에 log canary step 추가") 와의 수단 차이를 명문화.
- **N-C-3**: §3.1 line 107 "Hermes runtime 자체는 redaction 수행" 단정 → "Hermes upstream redaction = R-1 import 시점 검증 (본 cycle 입증 0, 설계 신뢰 한정)" 으로 약화 (NT-C-8 답습, P-2 over-claim 방지 일관).
- **N-C-4**: (선택) 51 audit (b) "송신 redaction 미커버" → brief (b) "✅" 격상 시, "(b) ✅ = detection PoC 한정. 송신 redaction *실증* 은 upstream (51 audit 우려 유지)" cross-reference 추가 (NT-C-6 답습). R-C-1 정정에 흡수 가능.

---

## NOTE (NT-C-N)

- **NT-C-1**: GP-2 prevention 의 제자리 = 본 repo 외부 (governance §4.1/§4.3 설계 전제) → "빈 껍데기" 아닌 "upstream 위임 설계". (§2.3)
- **NT-C-2**: GP-2 PASS 에 runtime 포함 강제 = Provider Liquidity + DESIGN repo 경계 침범 → 비권고. detection-layer PASS 가 올바른 형태. (§3.3)
- **NT-C-3**: R-5 base64 known limitation = 비례적 (solo 개인 툴, fixture + workflow warning 명문 직접 검증). (§4.2)
- **NT-C-4**: R-5 deferred = GP-2 PASS scope 를 "Tier-1 42 평문 한정" 으로 축소 (brief §4.1 이미 명문 — 충족). (§4.2)
- **NT-C-5**: secret-hygiene workflow_dispatch 미지원 + cron-only = 비차단. actual run `26517803107` success + head_sha `4fec6485` + 코드 불변 (`4fec648..HEAD` 변경 0) 모두 직접 검증 — brief C-3 evidence 처리 정확. (§4.3)
- **NT-C-6**: 51 audit (b) "송신 redaction 미커버" 우려는 (b) ✅ 격상으로 해소되지 않음 (D-2 = 마스킹 결과 잔존 검사이지 redaction 실증 아님, `env_redacted.txt` 직접 검증). R-C-1 축. (§5)
- **NT-C-7**: (d) 충족 수단 = R-3 (≠ 모법 R-6 r2-canary). 59 가 r2-canary 를 R-6/R-2 영역으로 분리한 것과 일관. (§5)
- **NT-C-8**: "R-1 operative" 단정 = upstream 가정 의존 (본 cycle 입증 0). detection PASS 와 독립이므로 비차단. (§5)
- **NT-C-9**: 발효 형태 (APPROVE WITH CONDITIONS, detection PASS + prevention deferred) = 59 Layer PASS + 32 MVP-1 PASS 와 일관. 4 대안 中 dominant. (§1)

---

## 자기진단 (메타 편향 회피)

| # | 위험 | 처리 |
|---|------|----|
| 1 | Agent C 가 대안 제시 압박으로 무리한 BLOCKING 생성 | R-C-1 = ADR-011 line 56/145 + governance §4.5 직접 검증 근거 (추론 아닌 문서 대조). 4 대안 中 3 기각 = 변경 최소화 |
| 2 | A/B/codex 미참조 의무 | 본 분석 = brief + 4 입력 문서 + 실 evidence(workflow/fixture/gh api/git) 직접 검증만. 타 source 0 |
| 3 | detection-only PASS 를 과도히 부정 (REVISE 편향) | (b) REVISE 기각 (57 (β) 결정 위반) + (d) sub-PASS 기각 (32 Agent C 선례). verdict = APPROVE WITH CONDITIONS (brief 권고 형태 인정) |
| 4 | over-claim 지적이 ceremony-inflation | R-C-1 = framing 정정 1건 (59 B-2 흡수 동형, 1pass 흡수 가능). 신규 cycle 0 |
| 5 | 비례성 과소/과대 | §4 = GP-2 cycle + R-5 + workflow_dispatch 모두 비례 인정 ([[feedback_proportionate_security_personal_tool]] + [[feedback_actual_run_trigger_paths_filter]] 답습) |

---

**Agent C 분석 끝.** verdict = **APPROVE WITH CONDITIONS** / BLOCKING **1** (R-C-1) / 권고 4 (N-C-1~4) / NOTE 9 (NT-C-1~9).
