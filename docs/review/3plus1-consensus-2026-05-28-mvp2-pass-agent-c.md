# Agent C (대안 탐색가) 독립 분석 — Layer 1+2+4 통합 PASS 발효 (59 entry, e2)

> **관점**: "더 나은 발효 형태/판단이 있는가? PASS 발효 형태가 최선인가?"
>
> **검토 대상**: `docs/phase0/mvp2-layer-124-pass-activation-brief.md` (v1, §0~§11)
> **입력**: 55 entry brief (e1 진입 권한) + 32 entry MVP-1 PASS 발효 합의 (답습 패턴)
> **독립성**: Agent A/B 및 외부 LLM 응답 미참조. 본 분석 = filesystem + gh api + CI run direct verify 기반.
> **작성**: 2026-05-28 (Agent C 단독)

---

## §0 verdict

**APPROVE WITH CONDITIONS**

brief 의 PASS 발효 형태("APPROVE WITH CONDITIONS — C-1 완료 + C-2 2a DEFER 명문 + C-3 r2-canary 영역 명시")는 32 entry MVP-1 PASS 발효 형태와 **일관**하며, 더 나은 발효 형태는 발견되지 않았다. C-1 evidence 보강은 filesystem + actual run (`26557936920` green) 으로 실증 확인. 단 **2a DEFER 의 근거 진술 1건이 기술적으로 부정확**(per-repo config = "영향 최소"가 아니라 *no-op*)하여, 이를 BLOCKING 1건으로 정정 요구한다. 정정은 **DEFER 결론을 약화하지 않고 오히려 강화**한다 (조건 처리 흡수 가능, 별도 v2 cycle 불요).

- **BLOCKING: 1건** (R-C-1)
- **권고: 3건** (N-C-1 ~ N-C-3)
- **NOTE: 3건** (NT-C-1 ~ NT-C-3)

---

## §1 evidence direct verify (본 분석 기반)

대안 판단 전, brief 가 주장하는 evidence 를 read-only direct 검증했다 (Agent C 독립):

| brief 주장 | verify 방법 | 결과 |
|----------|----------|------|
| C-1 fixture `timestamp_monotonicity.jsonl` 추가 | `ls tests/fixtures/jsonl_ledger/fail/` | ✅ 존재 (867B, commit `4c48099`) |
| g4-hash-chain.yml 5 violation_type cover | grep workflow line 197~227 | ✅ prev_hash + hash_recalc + schema + genesis + **monotonicity** 5종 |
| C-1 actual run `26557936920` green | `gh run view` | ✅ success, headSha `4c480996...` = commit `4c48099` 일치 |
| 58 entry 3 G4 run green | `gh run view` × 3 | ✅ `26557460199`(hash-chain) + `26557460227`(rewrite-defense) + `26557460197`(history-anchor) 전원 success |
| branch protection 8 contexts + force/delete false | `gh api .../protection` | ✅ `["guard","verify","feasibility","scan","enforce","defense","validate","bypass-detect"]` + force_push false + deletions false |
| denyNonFastForwards 미설정 | `git config --get` | ✅ rc=1 (미설정 확인) |
| history-anchor-verifier = Layer 5 운영 | workflow line 1/20 | ✅ "G4 History Anchor Verifier (Layer 5)", 58 run green |

→ **brief evidence 매트릭스 = 실증 정합** (over-claim 0, 57 (β) B-1 cascade 교훈 답습). 대안 판단의 사실 기반 확보.

---

## §2 BLOCKING

### R-C-1 ⭐⭐ — 2a DEFER 근거의 기술적 부정확: per-repo `receive.denyNonFastForwards` = "영향 최소"가 아니라 *no-op* (효과 0)

**근거 (direct verify)**:

- 본 repo 상태: `git rev-parse --is-bare-repository` = **false** (비-bare 작업 트리 clone), `git remote -v` push target = `git@github.com:jokwangwon/AI_development_tool.git` (GitHub).
- `receive.denyNonFastForwards` 는 git 의미론상 **push 를 *받는* repo (bare/server)** 의 `git-receive-pack` 경로에서만 작동한다. 본 repo 는 push 를 *보내는* clone 이며 push 를 받지 않는다.
- 따라서 본 clone 에서 `git config receive.denyNonFastForwards true` 를 켜도 **어떤 force-push 도 막지 못한다** (no-op). 막을 수 있는 force-push 자체가 이 repo 에 도달하지 않기 때문.
- 55 entry brief §4.4.2 대안 매트릭스: 대안 (c) "per-repo (`git config receive.denyNonFastForwards true`)" = "✅ 영향 최소", 권고 = "(c)+(d) 조합". 본 activation brief §2.2 / §4.1 = 이를 그대로 답습하여 "per-repo local config = 컨테이너 미배포 상태 ceremony" 로 framing.

**문제점**: "ceremony (= 켜는 게 과잉 의식)" 라는 framing 은 *per-repo config 가 일정한 보호를 제공하나 현 시점 과잉* 이라는 의미를 함축한다. 그러나 본 clone 의 per-repo `receive.deny*` 는 **과잉이 아니라 무효과(no-op)** 다. 정확한 명제는 "ceremony" 가 아니라 "**현 clone 구조에서는 작동 불가 — operative 보호는 (i) GitHub branch protection [Layer 2b, 작동 중] 또는 (ii) 컨테이너 내 *bare/server* repo + pre-receive hook 뿐**" 이다.

**이 정정이 DEFER 를 약화하지 않고 *강화*하는 이유** (Agent C 핵심 판단):
- 부정확한 framing("ceremony") → "그래도 trivial 하니 그냥 켜자" 는 반론을 부른다 (Agent C 임무 2 의 trade-off 질문 자체).
- 정확한 framing("no-op on this clone") → **켤 이유 자체가 소멸**한다. 켜도 보호 0, 안 켜도 보호 0, operative 보호는 Layer 2b 가 이미 제공. DEFER 가 비례 보안 판단이 아니라 **기술적 정합 판단**으로 격상되어 더 견고해진다.

**정정 (조건 처리 흡수, 별도 v2 cycle 불요)**:
- §2.2 / §4.1 / §7 C-2 의 "per-repo local config = ceremony" → "**per-repo `receive.deny*` = 비-bare push-clone 에서 no-op (작동 불가). operative append-only 보호 = Layer 2b (GitHub branch protection, force_push/deletions false 작동 중). 2a 활성화 = 실 *bare/server* repo 또는 컨테이너 내 pre-receive hook 배포 trigger 시점 — 컨테이너 미배포 상태 미충족**" 으로 본문 정정.
- §4.4.2 대안 (c) "✅ 영향 최소" cell → "⚠️ 비-bare clone no-op" 으로 정정 답습 (단 55 brief 본문은 별도 commit 영역, 본 cycle = activation brief 정정 한정).

→ **2a DEFER 결론 자체 = 유지·강화** (PASS 발효 비차단). 정정 = 근거 문장 1건. APPROVE WITH CONDITIONS 의 C-2 조건 본문에 흡수.

---

## §3 권고 (N-C-N)

### N-C-1 — 발효 형태 4 대안 중 brief 채택안이 32 entry 와 일관 (대안 (a)~(d) 기각 근거 명문)

임무 1 (PASS 발효 형태 대안) 검토 결과:

| 대안 | 평가 | 기각/채택 근거 |
|------|------|------------|
| (a) 무조건 APPROVE (조건 0) | ❌ 기각 | 32 entry 도 "APPROVE WITH CONDITIONS"(BLOCKING 6 + 권고 5) 였다. 조건 0 = 32 답습 비일관 + C-2 framing 정정(R-C-1) 미반영 risk |
| (b) 2a DEFER → 영구 결정 | ⚠️ 부분 타당하나 시기상조 | 2a 가 *no-op* 임이 확정(R-C-1)되면 영구 DEFER 가 오히려 정직하나, **컨테이너 배포 trigger 시 bare repo/pre-receive 형태로 재등장** 여지가 있어 "영구 결정"보다 "trigger 시점 활성화 (조건부 DEFER)" 가 정확. [[feedback_proportionate_security_personal_tool]] DESIGN 보존·발효 DEFER 패턴과 동형 |
| (c) Layer 4 r2-canary 포함 full APPROVE | ❌ 기각 | r2-canary = R-6/R-2 redaction canary (GP-2 영역), Layer *ledger* 검증 핵심 아님. 3 ledger workflow 가 Layer 4 충족. 포함 시 GP-2 scope 침입 |
| (d) Layer 1+2+4 부분 발효 (2a 분리) | ❌ 기각 | (γ-c) 특화 의무 3 "통합 동시 발효" 위반 (55 §1.2 #3). Layer subsection 분리 ≠ 발효 분리. 32 entry 도 GP-3+GP-5 통합 발효 |

→ **brief 채택안(APPROVE WITH CONDITIONS, 조건 C-1 완료 + C-2 DEFER 명문 + C-3 영역 명시) = 32 entry 와 형태 일관**. R-C-1 정정 1건 추가 외 발효 형태 변경 불요. 권고: brief §7 또는 §4 에 위 4 대안 기각 근거 1 매트릭스 명문 (55 §4.4.1 합의 형태 대안과 별도로 *발효 형태* 대안 — 누락 영역, NT-C-1 참조).

### N-C-2 — PASS 범위: Layer 5 미포함은 일관적이나 "scope 외" 와 "evidence 사용" 의 긴장 명문 권고

임무 3 (PASS 범위 대안) 검토:

- 55 B-2 (본 brief §1.1/§2.4 답습): `history-anchor-verifier.yml` = workflow name 명시적으로 **"(Layer 5)"** (direct verify: line 20 `name: G4 History Anchor Verifier (Layer 5)`, 58 run `26557460197` green). Layer 5 External anchor PoC 시제 *이미 운영 중*.
- 본 activation brief §2.4 E-PASS-6: 이 동일 workflow 를 **Layer 2 (history rewrite/deletion 검출) evidence** 로 사용 (rewrite-defense + history-anchor-verifier 조합).
- **긴장**: 동일 workflow 가 (i) 자기 이름은 "Layer 5", (ii) brief 에서는 "Layer 2 evidence", (iii) PASS 범위는 "Layer 5 = scope 외". 3중 라벨. 55 B-2 가 "PoC 시제 존재 ≠ Layer 5 PASS 진입" 으로 정리했으나, *동일 workflow 를 Layer 2 evidence 로 끌어쓰는* 행위가 Layer 5 evidence 를 Layer 2 PASS 에 합산하는 것으로 오독될 여지.

→ **PASS 범위(Layer 5 미포함)는 일관적**(External anchor = 독립 보안 결과, Layer 1+2+4 결정 영역과 별개, "부분 답습" framing 정합). 단 권고: §2.4 E-PASS-6 에 "history-anchor-verifier 의 *history rewrite/deletion 검출 step* 만 Layer 2 evidence 로 인용 — 동 workflow 의 *external anchor 검증 step* 은 Layer 5 PoC 로 본 PASS 범위 외" 분담 1줄 명문 (55 §2.4.1 B-1/B-5 workflow↔Layer 분담 매트릭스 동형). RT-PASS-2 (Layer 합산 금지 sensor) 의 cross-workflow 변형 risk.

### N-C-3 — 더 가벼운 발효 경로 검토: 본 PASS 발효 cycle 의 풀 3+1 = 과잉 아님 (비례성 PASS)

임무 4 (ceremony-inflation / 비례성) 검토:

- [[feedback_ceremony_inflation]] / [[feedback_meta_cycle_warning]] 기준 self-check: 본 cycle = "정정의 정정" 이 아니라 **실 milestone (PASS 발효 e2)**. 55 e1 → 본 e2 = 선형 진행 (meta-cycle 차수 0).
- 풀 3+1 + 외부 LLM 1+ 정당화: §6.2 trigger 1(큰 결정 = PASS 발효 milestone) + trigger 5(cross-vendor) 발화. 32 entry 도 동형(풀 3+1 + codex). 헌법 5조-2 cross-vendor. → **과잉 ceremony 아님**.
- 단 **더 가벼운 경로 존재 여부**: C-1 이 *합의 전 미리* 보강 완료(`4c48099`, actual run green)된 점에서, 본 cycle 의 실질 신규 판단 = "(a)~(d) evidence 충족 확인 + (e2) 발효 합의" 뿐. 32 entry 가 최초 PASS 발효였던 것과 달리 본 cycle 은 *2번째 동형 PASS 발효* → 32 의 선례가 형태를 이미 고정. 그럼에도 풀 3+1 유지는 (i) PASS 발효 = 최고 milestone, (ii) cross-vendor 의무, (iii) Claude 단독 cascade risk(P-4) 회피로 정당. → **경로 단축 불요, 현 형태 채택**.
- C-3 (r2-canary) = 조건이라기보다 **scope 명시(영역 분리)** 성격. "조건"으로 framing 하면 충족해야 할 gate 로 오독 → r2-canary 미트리거가 PASS 차단으로 오인될 risk. 권고: C-3 = "조건" 아닌 "**scope-out 명시(R-6/R-2 GP-2 영역, Layer 통합 PASS 비차단)**" 로 격하 표기 (불필요 ceremony 차단).

---

## §4 NOTE (NT-C-N, 참고 한정)

### NT-C-1 — *발효 형태* 대안 매트릭스가 brief 에 부재 (누락)

55 brief §4.4 = "합의 형태 4 대안 / denyNonFastForwards 5 대안 / evidence template 3 대안" 매트릭스 보유. 그러나 본 activation brief 는 **PASS *발효 형태* 자체의 대안 매트릭스가 없다** (무조건 APPROVE / 부분 발효 / full APPROVE 등). N-C-1 의 4 대안 기각 근거가 그 누락을 메운다. 후속 동형 PASS 발효 (MVP-2 PASS) 시 §7 에 발효 형태 대안 매트릭스 표준 포함 권고. 본 cycle = N-C-1 로 충분 (별도 cycle 불요).

### NT-C-2 — C-1 "합의 전 미리 보강" 의 process 정합성 (32 entry 와 차이)

본 brief C-1 = 합의 *전* `4c48099` 로 보강 완료 (사용자 명시). 32 entry 는 BLOCKING 을 합의 *후* v1.1 1pass 흡수. 차이: 본 cycle 은 evidence gap(timestamp fixture)을 *코드/CI 보강*으로 선제 해소 → 합의 시점 (a)~(d) 완전 충족 상태. 이는 over-claim 회피(P-2) + ceremony-inflation 차단 측면에서 **오히려 우월** (gap 을 조건으로 남기지 않고 실 evidence 로 닫음). 비일관 아님, NOTE 한정.

### NT-C-3 — r2-canary workflow_dispatch 보유 확인 (별도 actual run 경로 존재)

direct verify: `r2-canary.yml` = `workflow_dispatch` + `schedule(cron)` + `paths` 트리거 보유. [[feedback_actual_run_trigger_paths_filter]] 기준, r2-canary 는 path 미트리거여도 **workflow_dispatch 로 즉시 actual run 가능**. 따라서 C-3 의 "별도 actual run" 은 실현 가능 경로 확보 상태 (GP-2 cycle 에서). 본 Layer 통합 PASS 비차단 정합.

---

## §5 자기진단 (메타 편향 회피)

| # | 위험 | 처리 |
|---|------|----|
| C-P-1 | Agent C 가 발효 형태 변경을 *과도 제안* (대안 탐색가 편향) | N-C-1 = 4 대안 *기각* 결론 (brief 채택안 일관 확인). 변경 제안 = R-C-1 근거 문장 1건 한정 |
| C-P-2 | R-C-1 (no-op) 발견이 DEFER 를 *뒤집는* 것으로 오해 | §2 명시 = DEFER *강화* (no-op → 켤 이유 소멸). PASS 발효 비차단 |
| C-P-3 | denyNonFastForwards 의미론 주장이 추론적 (verify 부재) | direct verify: `is-bare-repository`=false + remote=GitHub + git 의미론 (receive.* = 수신 repo 한정). 계산적 근거 |
| C-P-4 | Agent C = 55/57/58 작성자(Claude) cascade | filesystem + gh api + CI run direct (브리프 주장 재현 검증), cross-vendor codex (E-α) 병렬 |
| C-P-5 | ceremony-inflation self (본 합의 자체가 과잉?) | N-C-3 = 비례성 PASS 판정 (PASS 발효 milestone + cross-vendor, meta-cycle 차수 0) |

→ **자기진단 5/5 통과**.

---

## §6 결론 요약

- **verdict: APPROVE WITH CONDITIONS**
- **BLOCKING 1**: R-C-1 (2a DEFER 근거 정정 — per-repo `receive.deny*` = no-op, ceremony 아님. DEFER *강화*, 조건 본문 흡수)
- **권고 3**: N-C-1 (발효 형태 4 대안 기각 근거 = 32 일관) + N-C-2 (Layer 5 evidence 분담 1줄 명문) + N-C-3 (C-3 = 조건 아닌 scope-out 격하, 비례성 PASS)
- **NOTE 3**: NT-C-1 (발효 형태 대안 매트릭스 누락) + NT-C-2 (C-1 선제 보강 process 우월) + NT-C-3 (r2-canary workflow_dispatch 경로 존재)
- **발효 형태 판단**: brief 채택안 = 32 entry MVP-1 PASS 발효와 **일관, 최선**. 더 나은 발효 형태 미발견. R-C-1 정정 1건 (별도 v2 cycle 불요, 1pass 흡수 가능).

**본 Agent C 분석 끝.**
