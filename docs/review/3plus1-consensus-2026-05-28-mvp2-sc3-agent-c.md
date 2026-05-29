# 3+1 합의 — Agent C (대안 탐색가) 독립 분석: SC-3 GP-2 full PASS 발효 brief

> **작성**: 2026-05-28 (67번째 entry cycle — 세션 #3, SC-3)
> **관점**: "더 나은 방법 / 명칭 / scope 가 있는가?"
> **독립성**: Agent A/B, 외부 LLM 응답 미참조 (직접 read 기반)
> **검토 대상**: `docs/phase0/mvp2-sc3-full-gp2-pass-activation-brief.md` (v1, §0~§11)
> **답습 source 직접 read**: 60 GP-2 detection-layer PASS brief / 62 MVP-2 PASS brief / 65 SC-1 brief / 66 SC-2 brief / governance §4.5 (a)~(e) verbatim / feedback_pass_scope_overclaim

---

## 1. 판정

### **REVISE** (명칭 "full" 자격 — BLOCKING 1건)

evidence 실증은 견고하다 (R-2 in-repo operative `7051138` filesystem 확인, R-1 조건부/문서 기반 66 답습, detection 60 답습). 발효 *자격* 자체도 governance §4.5 (a) 구조상 정당하다. **단 핵심 명칭 "GP-2 full PASS" 의 "full" 수식어가 over-claim 재발**이다 — 본 프로젝트는 cycle 60 에서 정확히 동일한 "GP-2 (full) PASS" 를 REVISE 로 강등시킨 선례가 있고 (feedback_pass_scope_overclaim #3), 본 brief 의 "full" 은 그 강등을 사실상 재도입한다. brief 가 §4 에서 "무수식 GP-2 완전 PASS 금지" 를 명문화한 것은 정직하나, **"full" 자체가 이미 수식어이며 (a) 조건의 절반(R-1 실 canary/(b)(d) Hermes trigger)이 deferred 인 상태에서 "full" = scope over-claim**. 명칭만 정정하면 1pass 흡수 가능 → REVISE (차단급 아닌 framing, 60 동형).

---

## 2. BLOCKING (정정 필수)

### B-C-1 ⭐ — 명칭 "GP-2 **full** PASS" = "full" 수식어 over-claim (60 cascade 5번째 재발)

**근거 (3중)**:

1. **60 선례 직접 충돌**: cycle 60 (`92e9078`) 은 "GP-2 (full) 송신 redaction PASS" 를 4 source REVISE → **"GP-2 detection-layer PASS"** 강등했다 (60 brief §11 B-1: "'GP-2 (full) PASS' + '(a) ✅' = over-claim"). 본 SC-3 의 "GP-2 full PASS" 는 그 강등시킨 "full" 을 prevention 추가를 근거로 *재도입*한다. feedback_pass_scope_overclaim #3 이 명시적으로 경고한 패턴.

2. **(a) 조건의 절반이 deferred 인데 "full"**: governance §4.5 (a) = "Hermes native redaction Tier-1 42 catalog 적용 검증 **+** P1 facade redaction filter 검증" — R-1 sub-evidence 와 R-2 sub-evidence 의 AND. 본 brief 자기 인정 (§2/§4): R-1 = **조건부** (실 격리 canary deferred + 활성화 전제 + R-6 Hermes lock trigger 미구현). 즉 (a) 의 R-1 sub-evidence 가 "조건부/문서 기반" 인데 전체를 "full" 로 명명 = scope 과장. **"full" 은 (a)~(d) 모두 무조건 충족을 함의**하나, 실제로는 (b) R-1 격리 PoC deferred + (d) R-1 Hermes trigger 미구현 (§2 매트릭스 ⚠️ 2칸).

3. **62 MVP-2 PASS 와 명칭 패턴 비대칭**: 62 는 무수식 "MVP-2 PASS" 를 거부하고 **"MVP-2 Implementation Evidence PASS (G4 ledger 완전 + GP-2 detection-tier, prevention/... deferred)"** 복합 자격으로 강등됐다. 62 의 "Implementation Evidence" 는 *축소* 수식어 (runtime 보증 아님 명시). 반면 SC-3 의 "full" 은 *확대* 수식어 — **62 가 깐 보수적 명칭 기조와 정반대 방향**. brief §4 가 62 "복합 자격 패턴 답습" 을 주장하나, "full" 추가는 답습이 아니라 역행.

**정정 권고**: §5 대안 매트릭스 참조 — **"GP-2 prevention PASS (R-2 in-repo operative + R-1 조건부 위임; 실 canary/Hermes trigger deferred)"** (대안 b) 또는 **"GP-2 prevention-tier PASS"** (대안 c, detection-tier 대칭). "full" 제거가 핵심. brief 의 deferred 명문(§4)·복합 자격(C-1)은 모두 유지 — *명칭의 머리글자* 만 정정.

---

## 3. 권고 (BLOCKING 아님, 채택 권장)

### R-C-1 — Exit (a) 판정 = "조건부 충족" 으로 명문 (현 "충족 (R-1 조건부)" 혼재)

§2 매트릭스 통합 판정 칸이 "✅ R-1 ∧ R-2 prevention 검증 충족 (R-2 강 + R-1 조건부)" 로 ✅ + "조건부" 혼재. (a) 전체 판정 = **"조건부 충족 (R-2 강 / R-1 조건부)"** 또는 **"R-2 충족 + R-1 조건부"** 로 ✅ 단독 부착을 피하라 (60 "(a) ✅" over-claim 직접 교훈). §5 Exit (a) 대안 매트릭스 참조.

### R-C-2 — 62 MVP-2 PASS 명칭 갱신 = 별도 chore (현 §7 #4 답습) 유지, 단 *동시 의무화* 명문

GP-2 가 detection-tier → prevention-tier 격상되면 62 MVP-2 PASS 의 "GP-2 detection-tier" 자격이 **stale** 된다. 현 brief 는 (C-4) "MVP-2 PASS 재선언 0" + §7 #4 "발효 후 chore" 로 처리 — 타당하다 (재선언 = scope 침입). 단 chore 를 *선택* 이 아닌 **갱신 의무** 로 명문하라 (방치 시 62/roadmap 에 "GP-2 detection-tier" 잔존 = 권위 chain 내부 불일치). §5 MVP-2 관계 매트릭스 참조.

### R-C-3 — 잔여 deferred 에 진입 trigger 명시 (62 N-2 답습)

§7 잔여 4건 (R-1 실 canary / R-6 Hermes lock trigger / R-5 / MVP-2 명칭)이 deferred 명문은 되나, *언제* 진입하는지 trigger 부재. 62 N-2 (deferred 진입 trigger 매트릭스) 답습 — 최소 "R-1 실 canary = Hermes clone URL 확보 시 / R-6 trigger = hermes-version.yaml 파일화 결정 시" 명시. 자동 진입 0 유지하되 trigger 가시화.

### R-C-4 — scope 대안 "operative 선언 vs PASS 발효" 명시적 비교 부재

brief 는 곧장 "full PASS 발효" 로 직행한다. 그러나 R-1 실 canary 미실행 상태에서 **"GP-2 prevention operative 선언" (PASS 미발효)** 이라는 더 보수적 대안이 존재한다 (§5 scope 매트릭스). brief §5 에 이 대안을 1줄이라도 비교하여 "PASS 발효 선택" 의 정당성을 명문하면 over-claim 방어가 강화된다 (현재는 PASS 발효를 자명한 것으로 전제).

---

## 4. NOTE (관찰)

- **N-C-1**: R-2 in-repo 실증 확인 — `src/adapters/llm/redaction.py` + `redaction_patterns.py` + `tests/adapters/llm/test_redaction_filter.py` filesystem 존재 (`7051138`). "R-2 in-repo operative" = 실증 (over-claim 0). brief §2/§10 E-2 정합.
- **N-C-2**: R-1 (66, `6fbee68`) = doc-only (코드 0). "조건부/문서 기반" framing 정직. brief 가 §4 에서 활성화 전제(HERMES_REDACT_SECRETS=true) + R-6 Tier-1 한정 + 실 canary deferred 3중 명문한 것 = 66 reframe 충실 답습. **이 부분은 모범적**.
- **N-C-3**: brief 의 P-1~P-7 자기진단 (§11) 이 over-claim 위험을 7개 선제 식별 — 특히 P-7 ("R-1 조건부를 '충족'으로 단순화") 은 본 B-C-1 과 동일 위험을 작성자도 인지. **그럼에도 *명칭* 의 "full" 은 자기진단 그물을 빠져나감** (자기진단이 본문 framing 에 집중, 제목 머리글자 누락). 60/62 가 *제목* 에서 강등됐던 것과 동형 — 제목 단어 1개가 cascade source.
- **N-C-4**: §6.2 승격 트리거 4/4 발화 + 풀 3+1 + 외부 LLM 1+ 의무 = PASS 발효 milestone 정합 (60/62/32 답습). 합의 형태 자체는 적정.
- **N-C-5**: cover 구조 비대칭이 60 대비 *부분 해소* (§3: 60 = in-repo prevention cover 0 → SC-3 = R-2 facade in-repo cover 1). 이는 실질 진보 — "full" 명칭만 아니라면 발효 자격은 실제로 강해졌다. **본 cycle 의 evidence 진보 자체는 인정**.

---

## 5. 대안 매트릭스 (Agent C 핵심 산출)

### 5.1 명칭 대안

| # | 명칭 | over-claim risk | 정보 전달 | Agent C 권고 |
|---|------|----------------|----------|------|
| (a) | **"GP-2 full PASS"** (현) | **높음** — "full" = (a)~(d) 무조건 충족 함의, 실제 R-1 (b)/(d) deferred. 60 강등 "full" 재도입 | 높음 (격상 신호) | ❌ **비채택** (B-C-1) |
| (b) | **"GP-2 prevention PASS (R-2 operative + R-1 조건부; 실 canary/trigger deferred)"** | **낮음** — "full" 회피, prevention prong 진입 명시 + 조건부 명문 | 높음 (detection→prevention 격상 + 한계 동시) | ✅ **채택 권고 (1순위)** |
| (c) | **"GP-2 prevention-tier PASS"** | **낮음** — 60 "detection-tier" 와 *대칭* (tier 진행 명확), "full" 회피 | 중 (조건부 명문은 부제로) | ✅ 채택 가능 (2순위, 60 대칭 일관성↑) |
| (d) | **"GP-2 PASS (in-repo prevention operative + upstream 위임 조건부)"** | **낮음** | 높음 (구조 정확) but 장황 | △ 조건부 채택 (정확하나 제목 과길이) |

**Agent C 권고 = (b) 1순위 / (c) 2순위**. 핵심 = **"full" 단어 제거**. (b) 는 prevention 진입(격상)을 정직하게 전달하면서 R-1 조건부+deferred 를 머리글자에 내포. (c) 는 60 "detection-tier" 와 tier 어휘 대칭이라 권위 chain 가독성 최상 — 단 "조건부" 가 제목에서 빠지므로 부제 의무. brief 본문(§4 deferred 명문 + C-1 복합 자격)은 어느 명칭이든 유지.

### 5.2 scope 대안

| # | scope | 트레이드오프 | Agent C 권고 |
|---|-------|-----------|------|
| (a) | **full PASS 발효** (현, "full" 제외 시 prevention PASS 발효) | R-2 in-repo + R-1 조건부 = governance §4.5 (a) AND 구조 충족. 단 (b) R-1 격리 PoC / (d) Hermes trigger deferred | ✅ **채택 (단 명칭 (b)/(c))** — (a) 충족 구조 + (e) 합의 + 사용자 명시면 발효 자격 정당. deferred 명문 전제 |
| (b) | R-1 실 canary 실행까지 발효 보류 | 가장 보수적, over-claim 0. but day2-r1 "코드 분석 충분" 선례 + artifact 부재(URL 불명) = 무기한 보류 risk. 비례성 위반 (개인 툴) | ❌ 비채택 (66 deferred 정당화 답습, 보류 = 진보 동결) |
| (c) | "GP-2 prevention operative" 선언 (PASS 미발효) | PASS milestone 회피, operative 사실만. but detection 60 은 PASS 발효했는데 prevention 만 operative 강등 = 비대칭 + milestone 신호 상실 | △ R-C-4 비교 대상 (명시 권장), 최종 비채택 |
| (d) | detection-tier 유지 + prevention 별도 milestone | tier 분리 명확. but R-2 in-repo + R-1 조건부 = 이미 prevention 검증 충족 → 별도 milestone 분리는 불필요 ceremony | ❌ 비채택 (ceremony inflation) |

**Agent C 권고 = (a) 발효** (명칭 (b)/(c) 전제). R-1 실 canary 보류(scope b)는 artifact/URL 부재로 무기한 동결 risk + day2-r1 선례 위반 → 비례성 부적합. 단 R-C-4 대로 (c) operative 대안을 §5 에 1줄 비교 명문하여 발효 선택 정당화 강화.

### 5.3 Exit (a) 판정 대안

| # | 판정 | 정직성 | Agent C 권고 |
|---|------|-------|------|
| (a) | "충족" (✅ 단독) | **낮음** — 60 "(a) ✅" 강등 직접 교훈 위반 | ❌ 비채택 |
| (b) | "조건부 충족" | 중상 — 조건부 명시하나 R-2 강함 가려짐 | △ 가능 |
| (c) | **"R-2 충족 / R-1 조건부"** (prong 분리) | **높음** — R-2 in-repo 강 + R-1 조건부 분리 = 60 3축 분리 답습, 가장 정확 | ✅ **채택 권고** |

**Agent C 권고 = (c)**. governance §4.5 (a) = R-1 + R-2 AND 구조이므로 prong 별 판정 분리가 가장 정직 (R-2 ✅ in-repo / R-1 조건부). ✅ 단독(a) = 60 over-claim 재발.

### 5.4 MVP-2 PASS 관계 대안

| # | 처리 | 트레이드오프 | Agent C 권고 |
|---|------|-----------|------|
| (a) | 즉시 갱신 (본 cycle 내) | 정합 즉시. but 62 재선언 = scope 침입 (C-4 위반) + 본 cycle = GP-2 격상 한정 | ❌ 비채택 (scope 침입) |
| (b) | **별도 chore (발효 후)** (현 §7 #4) | scope 격리 + 갱신 보장. 단 "선택" 이면 방치 risk | ✅ **채택 (단 R-C-2: 의무화 명문)** |
| (c) | 갱신 0 유지 | 본 cycle 최소. but 62/roadmap "GP-2 detection-tier" 영구 stale = 권위 chain 내부 불일치 | ❌ 비채택 (stale 방치) |

**Agent C 권고 = (b) 별도 chore + 갱신 의무화** (R-C-2). 현 brief (b) 답습은 정합하나 "선택" → "의무" 로 강화하여 stale 방지.

---

## 6. Agent C 종합

- **판정 = REVISE** (명칭 "full" over-claim 1건, 차단급 아닌 framing — 60 동형 1pass 흡수 가능).
- **핵심 = B-C-1**: "GP-2 **full** PASS" → "GP-2 **prevention** PASS (R-2 operative + R-1 조건부; deferred)" 또는 "GP-2 **prevention-tier** PASS". "full" 단어 제거가 전부. brief 의 deferred 명문·복합 자격·자기진단은 모두 우수 — *제목 머리글자 1단어* 가 60/62 cascade 와 동일 source.
- **evidence/발효 자격 자체는 정당** (R-2 in-repo `7051138` 실증 + R-1 조건부 66 답습 + (a) AND 구조 충족 + cover 비대칭 부분 해소). 명칭만 정정하면 발효 가능.
- 권고 R-C-1 (Exit (a) prong 분리 판정) ~ R-C-4 (operative 대안 비교) = 채택 시 over-claim 방어 강화.

**Agent C 독립 분석 끝.**
