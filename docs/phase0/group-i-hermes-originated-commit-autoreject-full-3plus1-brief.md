# Backlog #3 Group I (Hermes-originated commit auto-reject) 단독 풀 3+1 합의 *진입 전 정비* Brief (DRAFT v2)

> **본 brief = Group I (Hermes-originated commit auto-reject) 단독 합의 *진입 전 정비* DRAFT 한정** — 합의 보고서 작성 / commit / push / Hermes runtime 실 구현 / 실 차단 hook 구현 = 별도 단계 (staged cycle: brief → 승인 → 합의 → commit → push). 본 brief = **brief 단계 한정**.
>
> **v2 변경 (2026-05-20)**: 외부 cross-vendor blind 응답 1건 (GPT-5.5 Thinking, `docs/external-review/2026-05-20-group-i-hermes-originated-commit-autoreject-review-response-gpt.md`) 회수 → §7 trigger #7 충족. 응답의 5개 보강점을 I-1 / I-2 / I-5 / I-7 + §3.3 + §7.2 에 *입력 한정* 반영 (강제 채택 0건 — §0.4 + ADR-011 외부 LLM 입력 원칙). 응답의 framing 권고(설계명 재정의)는 §7.3 에 *외부 입력 flag* 로만 기록 — 채택/발효는 풀 3+1 + 사용자 결정 권한.

---

**작성일**: 2026-05-20
**Status**: **DRAFT v2** (진입 전 정비 — 합의 미발효, 외부 응답 1건 회수 반영)
**진입 단위**: Backlog #3 — Group I (Group α §8 옵션 (E) 분리 권고 영역)
**선행 발효 답습**: Group α `2026-05-14` (`3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md`, AR-3 + PC-4 T3 sub 3/3 APPROVE WITH CONDITIONS) + Group β `aa8a29a` + Group γ-1 `9b1f8cd` + Group γ-2 `2e9d46b` + GP-3 C-3 / GP-5 C-2 resolution `0749970`
**답습 입력 (1차 권위)**: **G3 §2.2 #20** (Hermes-originated 식별·차단 — `hermes-not-root-of-trust-runtime.md`) + Group α §6.1 (Group I cross-reference) + Group α C-2 (AI agent self-approval 차단 = Group I 결합 필수) + AR-3 × Group I Defense in depth (Group α §5.2 / §6.1)
**합의 권위 한계**: 본 brief = 진입 정비 DRAFT — 합의 *발효* 아님. T3 vs T2 *판정* (§5) 도 본 brief 는 *권고*만 발행, *발효* 는 풀 3+1 합의 (또는 합의 형태 결정) 의 권한.

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습 (2026-05-20)

> "다음 세션 1순위로 확정된 Group I (Hermes-originated commit auto-reject) 별도 합의 진입 brief를 작성해주세요. 배경: Group α 합의 condition C-2 가 'AI agent self-approval 차단 = Group I (Hermes-originated commit auto-reject) 별도 합의 결합 필수'로 명시했고, Group α §8 옵션 (E)로 분리 권고된 영역입니다. G3 §2.2 #20(Hermes-originated commit 식별·차단)을 답습 입력으로 삼고, Group α(`3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md`) §6.1 Group I cross-reference + AR-3 × Group I Defense in depth 결합을 반영해주세요. 먼저 brief 만 작성하고, 합의·commit·push 는 진행하지 마세요. Group I 가 보안 enforcement T3 영역인지(풀 3+1 의무) 또는 T2 영역인지(Reviewer-only 단축 가능) 를 brief 에서 판정 영역으로 정비해주세요."

본 brief = 위 명령 답습 — Group I 단독 합의 **진입 전 정비** + **T3/T2 판정 영역 정비** (§5) + 실 변경 0건.

### 0.2 본 brief 가 *하는* 것

1. Group I (Hermes-originated commit auto-reject) 범위 + 책무 정의 (G3 §2.2 #20 + §2.5 보호 대상 enumeration + §4 self-reference 답습) (§1)
2. Group I 결정 영역 통합 검토 (식별 방법 / 차단 지점 / 보호 범위 / Defense in depth 결합 / self-reference 연결 / Rollback / SPOF / 구현 시점 의존) (§2)
3. AR-3 (Group α) × Group I **Defense in depth 결합** 정비 (Group α §5.2 + §6.1 + C-2 답습) (§3)
4. §4 합의 인프라 순환 권위(self-reference) 연결 + §5.5 SPOF Accepted Risk 정비 (§4)
5. **⭐ 합의 형태 판정 영역 정비 — Group I = T3 (풀 3+1 의무) vs T2 (Reviewer-only 단축 가능)** (§5)
6. 풀 3+1 Agent A/B/C 관점 분배 + Reviewer 검토 의무 영역 (§6)
7. 외부 LLM 입력 영역 + *입력 한계* 명시 (§7)
8. Rollback Trigger 통합 매트릭스 (Group I 한정) (§8)
9. 다음 단계 (사용자 결정 영역 — 자동 진입 0건) (§9)

**v2 추가**:
10. 외부 응답(GPT-5.5) 회수 → §7 trigger #7 충족 + 5개 보강점 *입력* 반영 (§7.1~§7.2) — I-1 (positive allow-list / metadata = 참고 신호 한정) / I-2 (runtime = sensor, 최종 reject = Hermes 밖 + GHES pre-receive ≠ GitHub.com 기본) / I-5 (root of trust = Hermes 밖) / I-7 (T3 path 한정 + observe mode + quarantine) + §3.3 (`.git/` 직접 변조 gap) + negative-control-only 조항
11. 외부 응답 framing 권고 *flag* (§7.3) — 설계명 "Hermes-originated commit auto-reject → Human-authorized T3 change enforcement with Hermes credential isolation" = 외부 입력 한정 (채택은 풀 3+1 + 사용자 결정)

### 0.3 본 brief 가 *하지 않는* 것 (사용자 명시 영구 답습)

본 brief 의 어떤 §도 그 자체로 다음을 발생시키지 않는다:

- ❌ Hermes runtime 실 구현 (orchestrator / container / agent runtime 본문)
- ❌ Hermes-originated commit 실 차단 hook 구현 (git pre-commit / pre-receive / filesystem ACL / read_only mount / CI step 본문)
- ❌ Hermes upstream 변경 (Dockerfile / `hermes-version.yaml` / upstream PR)
- ❌ 수단 결정 (식별 방법·차단 지점·보호 범위 최종 고정)
- ❌ threshold 고정
- ❌ CI workflow 변경 / actual run 재실행 / workflow_dispatch 추가 / paths 필터 변경
- ❌ Operational Readiness PASS (Layer E) 선언 / Hermes PMO 격상 (Layer F) 선언
- ❌ MVP-1 exit 발효 (GP-3 5/5 + GP-5 5/5 별도)
- ❌ Phase α defer-lockdown 변경
- ❌ G3 §2.2 #20 / §2.5 / §2.6 / §4 본문 변경 / ADR 본문 자동 갱신
- ❌ 합의 보고서 작성 / commit / push (별도 단계)
- ❌ Backlog #4 · Backlog #6 자동 진입 / 외부 LLM 추가 자동 호출 / 외부 LLM 응답 결론 강제 채택
- ❌ 5 영구 핵심 제약 · Provider Liquidity 5-way 약화

### 0.4 본 brief 의 권위 한계

본 brief 는 결론을 *선취하지 않는다*. T3/T2 판정(§5) 은 trigger 매트릭스 기반 *권고*만 발행하며, *발효* 는 합의(또는 사용자 명시 합의 형태 결정) 의 권한이다. Group I 의 식별 방법 / 차단 지점 / 보호 범위 *결정* 은 모두 풀 3+1 Agent A/B/C 독립 평가 + Reviewer 종합에서 도출 (수단 결정·구현 = Implementation/Runtime PASS 영역 + Backlog #6 연결 별도).

---

## 1. Group I 범위 + 책무 정의

### 1.1 정의 (G3 §2.2 #20 답습)

| 항목 | 내용 |
|----|----|
| Group I 정의 | **Hermes-originated commit auto-reject** — Hermes runtime 이 *단독으로* 생성한 commit (특히 정책성·합의·gate 정의·`.git/` 영역) 을 자동 식별·차단 + audit log + 사용자 alert |
| 권위 근거 (1차) | **G3 §2.2 #20** ("합의 결과 silent override 또는 수정", T3 절대 금지 — 강제 메커니즘 = "합의 보고서 git commit 보존 + Hermes-originated 수정 자동 reject") |
| 권위 근거 (보강) | G3 §2.5 보호 대상 enumeration (16건) + §2.6 Gate Enforcement 보호 (TM-1~TM-8) + §4.5 ("합의 결과 commit author = Hermes-originated commit auto-reject") + system-identity-prequel §3.3 #2 |
| 책무 영역 | **Hermes runtime 영역 한정** (Group α = GitHub repo / branch protection 영역 — 책무 분리) |
| ADR-011 분류 | **T3 절대 금지의 *enforcement*** (§2.2 #20 = T3 12건 중 1건) |
| 현 상태 | G3 = **DESIGN PASS / IMPLEMENTATION PENDING** (§1~§7 (b) 격리 PoC + (d) 자동 회귀 미충족) — Group I 실 강제 = Implementation/Runtime PASS 영역 |

### 1.2 G3 §2.2 #20 ↔ Group I 정밀 (Hermes 변조 차단 매트릭스 4항목)

G3 §2.2 #20 + ADR-012 §2.12 "Hermes 변조 차단 매트릭스 4항목" = (1) Hermes-originated ledger entry / (2) 파일 변조 / (3) **git commit** / (4) 외부 LLM 응답 위조. **Group I = 이 중 (3) git commit 차단의 설계 단위** (나머지 3항목은 G4 hash chain / §2.5 ACL / ADR-012 §2.12 #4 각각 다른 단위).

### 1.3 §2.5 보호 대상 enumeration 中 Hermes-originated commit auto-reject 가 강제 메커니즘인 항목

| §2.5 # | 보호 대상 | Group I 강제 관여 |
|----|----|----|
| 1 | `.git/` (HEAD, config, hooks, refs) | ✅ container `read_only` + §2.2 #20 |
| 2 | `.github/workflows/*.yml` | ✅ git pre-commit hook + auto-reject |
| 9 | `docs/external-review/*.md` | ✅ append-only + Hermes-originated 변경 auto-reject |
| 10 | `docs/review/3plus1-consensus-*.md` (합의 보고서) | ✅ git append-only + Hermes-originated 수정 auto-reject (system-identity-prequel §3.3 #2) |
| 4 | `.github/CODEOWNERS` / branch protection 정의 | ✅ (Group α ↔ Group I 경계) |
| 5~8 | ADR 본문 / G2·G3·G4 정의 / SDD / 헌법 | ✅ filesystem read-only + git pre-commit hook |

> Group I = 위 §2.5 항목들의 *commit-차원* 강제 (filesystem read-only 는 §2.5 별도 layer / Group I = "Hermes-originated commit 자체의 식별·차단" layer). **Defense in depth = filesystem ACL (§2.5) + Group I commit auto-reject + Group α branch protection 3-layer.**

---

## 2. Group I 결정 영역 통합 검토 (8 영역)

> ⚠️ 본 §2 = *결정 영역 enumeration* (검토 대상 정비) — *결정/수단 고정 아님* (§0.4). 각 영역의 *결정* = 풀 3+1 Agent A/B/C 독립 평가 + Reviewer 종합.

| # | 결정 영역 | 핵심 의제 (검토 대상) | 권위 근거 |
|----|----|----|----|
| **I-1** | **Hermes-originated commit *식별* 방법** | commit author/committer 메타 (`agent=hermes`) / GPG 서명 부재 / commit trailer / container origin / process 출처 — *신뢰성 있게* Hermes-originated vs user-originated 구분하는 방법 (위장 가능성 평가 포함). **⚠️ v2 외부 입력(§7.2 #1): negative detection(metadata 판별) 보다 positive allow-list(사람 전용 signed commit 만 T3 허용) 권고. author/committer/trailer = 신뢰 신호 아님 → 참고 신호 한정 (신뢰 등급 분리 §7.2 표).** 식별 신뢰 등급 *결정* = Agent A/B 평가 | §4.5 + §3.1 Hermes-originated detection |
| **I-2** | **차단 *지점* (blocking point) + layer** | git pre-commit hook (local) / pre-receive hook (server) / filesystem `read_only` mount on Hermes container (`:ro` bind + `cap_drop=ALL`) / CI step / branch protection 결합 — single layer vs Defense in depth. **⚠️ v2 외부 입력(§7.2 #2/#3): (a) GHES `pre-receive` hook ≠ GitHub.com 기본 수단 (Enterprise Server appliance 한정) → GitHub.com 에서 현실적 server-side = ruleset + CI provenance check. (b) Hermes runtime 내부 reject = sensor/audit producer 한정, 최종 reject 권한 = Hermes 밖 (ruleset / container ACL / hardware key).** | §2.5 #1 + §2.2 #20 강제 메커니즘 |
| **I-3** | **보호 대상 *범위*** | §2.5 16건 全 적용 vs 핵심 경로 한정 (`.git/` + workflows + 합의 보고서 + ADR + Constitution + gate 정의 + external-review + redaction-policy + catalog) — silent expansion 차단 | §2.5 enumeration + §2.2 #9~#22 |
| **I-4** | **AR-3 (Group α) × Group I 결합 형태** | `--no-verify` 우회 차단 (Group α branch protection + required CI) + Hermes-originated commit 식별 차단 (Group I) 의 *결합* — 책무 분리 유지 + Defense in depth (§3) | Group α §5.2 + §6.1 + C-2 |
| **I-5** | **§4 self-reference 순환 권위 연결** | Group I = "Hermes 가 합의 결과 commit author 가 될 수 없음" enforcement (§4.5) → **AI agent self-approval 차단** (Group α C-2) 의 runtime 차원 구현 | §4.2 원칙 4 + §4.5 + Group α C-2 |
| **I-6** | **Rollback Trigger / audit / Evidence ledger** | 검출 시 `consensus_self_reference_detected` (G4 §3.8.2 #7) / `policy_drift_detected` (#9) / `gate_enforcement_bypass_detected` (#10 후보) 발화 + audit JSONL + 컨테이너 정지 + 사용자 alert | §2.6.5 + G4 §3.8.2 |
| **I-7** | **SPOF Accepted Risk (1인 single-host)** | 1인 동일 호스트에서 *사용자 자신* 의 commit 은 허용 + Hermes-originated 만 차단 → single-host 에서 식별 신뢰성·우회 한계 (사용자 = Hermes container 양쪽 제어) + multi-host 전환 시 추가 layer 트리거. **⚠️ v2 외부 입력(§7.2 #4): false positive 통제 = "탐지 정확도 향상"보다 (a) 보호 범위 T3 protected path 한정 (일반 코드/문서 = audit-only/warn 시작) (b) 초기 1~2주 observe mode 로 FP/FN 측정 (c) reject 대신 quarantine branch / patch artifact 저장 (작업 손실 방지) (d) 사람 commit 허용 기준 = 사람 서명 + 사람 token + ruleset 통과. credential/process boundary 실분리가 Q6 가능성의 *전제* — 동일 credential 공유 시 FP 보다 FN(Hermes 가 사람으로 보이는 commit) 이 더 큰 위험.** | §5.5 SPOF Accepted Risk + ADR-012 §원칙 12 |
| **I-8** | **구현 시점 의존성** | 실 강제 = Implementation/Runtime PASS 영역 (G3 DESIGN PASS / IMPLEMENTATION PENDING) + Backlog #6 Runtime + CI-hook 연결 (Group α C-1 답습) | Group α §6.2 + G3 §1 (b)/(d) |

---

## 3. AR-3 (Group α) × Group I — Defense in depth 결합 (1차 답습 영역)

### 3.1 Group α C-2 답습 (결합 필수 근거)

Group α 합의 condition **C-2** (B + C 일치, A 부분): *"AI agent self-approval 차단 = Group I (Hermes-originated commit auto-reject) 별도 합의 결합 필수"* — Group α §8 옵션 (E) 로 분리 권고. **즉 Group α (branch protection / `--no-verify` 차단) 단독으로는 AI agent self-approval 을 완전 차단 못 함 → Group I 결합이 비로소 차단책 완성.**

### 3.2 Group α §6.1 답습 (cross-reference 영역)

| 항목 | Group α §6.1 명시 |
|----|----|
| Group I 정의 | Hermes-originated commit auto-reject (G3 §2.2 #20 답습) — Hermes runtime 영역 한정 |
| Group α × Group I 결합 효과 | **Defense in depth 高** — `--no-verify` 우회 차단 + Hermes-originated commit 식별 차단 |
| 분리 사유 | 책무 영역 다름 (Group α = GitHub repo / Group I = Hermes runtime) + 5 영구 핵심 제약 #4 (단일 source-of-truth) 보존 + **Hermes ≠ root of trust 보존 (5 영구 핵심 제약 #1)** |
| 미진입 시 영향 | Group α 단독 = "유일하게 유효한 차단책" *불완전* (잔존 Hermes 경로) — Backlog #6 의존성과 함께 후속 영역 |
| Group α 권고 | Group α 발효 후 **Group I 별도 합의 진입 권고** (Defense in depth 결합) |

### 3.3 Defense in depth 3-layer 정비 (검토 대상)

```
잔존 우회 경로                   차단 layer
────────────────────────────────────────────────────────
인간/AI 의 --no-verify 우회   →  Group α: branch protection + required CI (GitHub repo)
Hermes-originated commit       →  Group I: 식별 + auto-reject (Hermes runtime)   ← 본 brief
정책성 파일 직접 변조          →  G3 §2.5: filesystem read_only mount + ACL
```

> Defense in depth = 세 layer 의 *결합* (single layer 만으로는 불완전). Group I = 가운데 layer. **책무 분리 유지** (Group α/Group I/§2.5 ACL = 각 다른 enforcement 주체) = 5 영구 핵심 제약 #4 (단일 source-of-truth) 보존.

#### 3.3.1 ⚠️ v2 외부 입력 — `.git/` 직접 변조 gap + 최종 reject 위치 (Q8 / Q3 / Q7)

외부 응답(§7.2 #5)이 지적한 Defense in depth 보강 공백:

1. **`.git/` 직접 변조는 commit 검사로 잡히지 않는다** — `.git/config`, hooks, refs, index, credential helper 변경은 commit-based 식별(I-1) 의 사각지대. → **반드시 filesystem read_only ACL layer(§2.5 #1)에서 차단** (Group I commit layer 가 아닌 *맨 아래 layer* 책무). brief §1.3 의 §2.5 #1 (`.git/` `read_only`) 가 이 gap 의 1차 대응 — v2 에서 명시 강조.
2. **최종 reject 권한 = Hermes 밖** (Q3/Q7) — Group I runtime reject 가 *유일 enforcement* 이면 self-reference 잔존. → Group I runtime = **provenance sensor / audit producer**, 최종 reject = GitHub ruleset / container ACL / hardware-backed human key / 별도 사용자 관리 credential 中 1+ (Hermes 밖). 이는 핵심 제약 #1 (Hermes ≠ root of trust) *강화* 방향 — §5.1 trigger #5 + §4 self-reference 와 정합.
3. **Group I enforcement *설정 변경 자체* = T3 분류** — Hermes 가 ruleset/CI workflow/audit log 를 수정할 token 을 가지면 안 됨 (§7.2 표). → R-I-CONFIG-CHANGE (신규 후보, §8) 와 연결.

> 위 3건 = 외부 *입력 한정* (강제 채택 0건). Defense in depth 책무 재배치 *결정* = 풀 3+1 Agent B/C + Reviewer 종합.

#### 3.3.2 ⚠️ v2 외부 입력 — negative control only 조항 (Q8 결함 #7)

외부 응답이 권고한 신규 조항: **Group I = negative control only.** Group I 의 식별·차단 동작 또는 PASS 가 **PMO / Operational Readiness 의 *positive evidence* 로 오용되어서는 안 됨** (Group I 는 "무엇이 *안 됨*"을 강제하는 negative control 이지, "무엇이 *됨*"을 증명하는 positive evidence 아님). → §5.1 trigger #6 (Operational Readiness 경계) + brief §0.3 금지 사항과 정합. 조항 *채택* = 풀 3+1 / 사용자 결정.

---

## 4. §4 합의 인프라 순환 권위(self-reference) 연결 + §5.5 SPOF

### 4.1 self-reference 역설 ↔ Group I

G3 §4.1 "합의 인프라 순환 권위 역설": Hermes 가 3+1 합의 *실행 인프라* 라면 Hermes 관련 결정(자기 격상 / 정책 변경 / G2~G4 PASS) 을 Hermes 가 실행한 합의로 결정 → 자기참조. **§4.5 = "합의 결과 commit author ≠ Hermes (Hermes-originated commit auto-reject)" + "합의 결과 적용 = 사용자 명시 commit 만 권위 인정".** → **Group I = §4.5 의 runtime enforcement 단위.**

| §4.5 처리 권한 | Hermes 단독 | Group I 관여 |
|----|----|----|
| 합의 진행 orchestrate | ✅ | — |
| 합의 결과 본문 보존 | ❌ (수정 가능 형태 금지) | git commit immutable 보존 |
| **합의 결과 commit author** | ❌ **Hermes-originated commit auto-reject** | ✅ **Group I 핵심** |
| 합의 결과 적용 (status 갱신) | ❌ 사용자 명시 commit 만 | filesystem read-only + 사용자 명시 |

### 4.2 §5.5 SPOF Accepted Risk (1인 single-host) — Group I 한계 명시

1인 동일 호스트에서 *사용자 자신* 의 commit 은 정당 권위 → Group I 은 **Hermes-originated 만** 차단해야 함. 그러나 1인 환경에서 사용자가 Hermes container 와 host 양쪽을 제어 → 식별 신뢰성·우회 한계가 SPOF (의도적 수용, §5.5). **multi-host / 다인 운영 전환 시 추가 layer 의무 발동 트리거** (ADR-012 §원칙 12 Layer 3/5) 명시 기록 대상. → 이 한계 평가 = Agent B (안전성) 의무 영역 (§6).

---

## 5. ⭐ 합의 형태 판정 영역 — Group I = T3 (풀 3+1 의무) vs T2 (Reviewer-only 단축 가능)

> **사용자 명시 요청 핵심 정비 영역.** 본 §5 = 판정 *근거 정비 + 권고* — *발효* 는 합의(또는 사용자 명시 합의 형태 결정) 의 권한 (§0.4).

### 5.1 판정 기준 (γ-2 §5.2 trigger 매트릭스 답습)

| 트리거 | Group I 발화 | 근거 |
|----|----|----|
| #2 T3 영역 자동 진입 | ✅ **HIGH (BLOCKING)** | Group I = **G3 §2.2 #20 (T3 절대 금지) 의 enforcement** — 합의 결과 / `.git/` / 정책성 파일 / gate 정의 차단 영역 |
| #4 Provider Liquidity 5-way 약화 | ❌ 영향 없음 | enforcement layer = catalog/provider 영역과 직교 |
| #5 5 영구 핵심 제약 약화 | ✅ **HIGH** | Group α §6.1 명시 — Group I = **핵심 제약 #1 (Hermes ≠ root of trust) + #4 (단일 source-of-truth) 직결**. §4 self-reference 순환 권위 자체가 대상 |
| #6 Operational Readiness / Hermes PMO 격상 경계 | ⚠️ **MEDIUM** | §4 self-reference = Hermes PMO 격상 (Layer F) 을 gate 하는 메타-순환 차단 — 실 구현은 Backlog #6 / Implementation PASS 영역 |
| #7 외부 LLM cross-vendor blind 없는 T3 결정 | ✅ **HIGH → v2 충족 (1건 회수)** | 기존 외부 LLM 응답 2건 (`2026-05-13`) = AR-3 중심, Group I thin. **v2: GPT-5.5 Thinking 신규 응답 1건 회수** (`2026-05-20-...-response-gpt.md`) — Group I 식별·차단(I-1/I-2) 직접 평가 + 5 보강점 (§7.2). → trigger #7 *충족*. (Gemini 등 2차 vendor 추가 입력 = 사용자 결정 영역, 의무 아님) |

### 5.2 형태 후보 비교

| 형태 | 적격 조건 (§4.4.1 답습) | Group I 충족? |
|----|----|----|
| **풀 3+1 (Agent A/B/C + Reviewer)** | T3 영역 + 새 권위 결정 발생 + 5 핵심 제약 직결 + self-reference 영역 | ✅ **적격 (해당)** |
| Reviewer-only 단축 | 새 권위 결정 0건 + 직전 합의 패턴 답습 + T2 + evidence 흡수 한정 | ❌ **부적격** — Group I = 새 *식별·차단 메커니즘 결정* 발생 (단순 evidence 흡수 아님) |

### 5.3 ⚠️ self-reference 구조적 논점 (Reviewer-only 부적격 보강 근거)

Group I 는 **합의 인프라의 순환 권위(self-reference) 자체를 대상으로 하는 결정** (§4). G3 §4.2 원칙 2: *"Reviewer-only 또는 외부 LLM 의견이 Hermes 관련 결정의 합의에 *필수*"*. → Group I 처럼 *Hermes 자신의 commit 권한* 을 다루는 결정에서 Reviewer-only(Hermes orchestrated 단축) 단독 = 메타-편향 통제 부족. **풀 3+1 + 외부 LLM 1+ 가 구조적으로 정합** (§4.4.2 답습).

### 5.4 권고 (발효 아님)

**Group I = T3 보안 enforcement 영역 → 풀 3+1 (Agent A/B/C + Reviewer) *의무*, Reviewer-only 단축 *부적격*** (트리거 #2 BLOCKING + #5 HIGH (핵심 제약 #1 직결) + #7 외부 LLM 미충족 + §5.3 self-reference 구조). **외부 LLM 1+ 신규 입력 권장/의무** (§7 — 기존 응답 Group I thin). 사용자 명시 결정 = 최종 권위 (§4.4.3). 본 권고 = §0.4 권위 한계 — *발효* 는 합의/사용자 결정.

---

## 6. 풀 3+1 Agent A / B / C 관점 분배 + Reviewer 검토 의무 영역

| Agent | 관점 | 분석 영역 (Group I) |
|----|----|----|
| **Agent A** (구현 분석가) | "실제로 동작하는가?" | Hermes-originated commit *식별* 기술 신뢰성 (author 메타 / GPG 부재 / trailer / container origin — 위장 가능성) + 차단 지점 기술 (pre-commit / pre-receive / `read_only` mount + `cap_drop=ALL` / CI) + Backlog #6 Runtime + CI-hook 연결 의존 + 성능/false-positive. **v2 외부 입력 평가: positive allow-list(signed commit) 기술 실현성 + GitHub.com ruleset/CI provenance check vs GHES pre-receive 운영 차이(§7.2 #2) + runtime=sensor 구조(§7.2 #3) 기술 타당성** |
| **Agent B** (품질/안전성 검증가) | "안전하고 견고한가?" | **식별 우회·위장 시나리오** (Hermes 가 author 위장 / `--no-verify` / hook 비활성화 — TM-6) + §5.5 SPOF (1인 single-host 식별 신뢰성 한계) + false-negative (Hermes-originated 누락) vs false-positive (사용자 commit 오차단) + **Hermes ≠ root of trust (핵심 제약 #1) 보존** + 단일 source-of-truth (#4) + §4 self-reference 차단 견고성. **v2 외부 입력 평가: credential boundary 실패 = metadata 위조가 아닌 사건 분류(§7.2 표) + `.git/` 직접 변조 gap(§3.3.1) + 동일 credential 공유 시 FN > FP 위험(§7.2 #4) + negative-control-only(§3.3.2) 견고성** |
| **Agent C** (대안 탐색가) | "더 나은 방법이 있는가?" | 식별 방법 대안 (signed commit 의무화 / 별도 committer identity / 격리 working tree) + 차단 지점 대안 (server-side vs local) + Group α/§2.5 ACL 과의 *최소 중복* 결합 + multi-host 전환 시 식별 강화 대안 + 신규 영역 발굴 (예: Hermes-originated PR auto-reject / commit trailer 표준) |
| Reviewer | "최선의 합의는?" | 3 출력 교차 비교 (일치/부분/불일치/누락) + 8 결정 영역 (I-1~I-8) 최종 합의 권고 + **AR-3 × Group I Defense in depth 결합 적격성 판정** + Group α C-2 결합 완성 여부 + 실 구현 = Backlog #6 / Implementation PASS 분리 명시 + **⭐ v2: 외부 framing 권고 판정** (§7.3 — "명칭 유지 + 중심 명제 명시" vs "Human-authorized T3 change enforcement with Hermes credential isolation 재정의") + **외부 5 보강점(§7.2) 채택/기각/조건부 판정** + negative-control-only 조항(§3.3.2) 채택 여부 |

---

## 7. 외부 LLM 입력 영역 + *입력 한계* 명시

### 7.1 입력 회수 현황 (v2)

| 영역 | 외부 LLM 응답 | Group I 적용 |
|----|----|----|
| AR-3 enforcement (branch protection / `--no-verify` / admin bypass) | Gemini + GPT 상세 응답 有 (`2026-05-13`) | ✅ Group α 영역 (입력 답습 완료) |
| **Hermes-originated commit *식별·차단* 메커니즘 자체 (I-1/I-2)** | **v2: GPT-5.5 Thinking 신규 응답 회수** (`2026-05-20-group-i-...-response-gpt.md`, Q1~Q8 직접 평가) | ✅ **trigger #7 충족** — §7.2 5 보강점 반영 |

> ⚠️ **입력 한계 (불변)**: 외부 LLM 응답 = *입력 한정* (강제 채택 0건 — §0.4 + ADR-011). 본 brief v2 는 응답의 5 보강점을 해당 §에 *입력*으로 반영했을 뿐, 식별 방법 / 차단 지점 / framing *결정* 은 풀 3+1 Agent A/B/C 독립 평가 + Reviewer 종합 + 사용자 명시 권한. 2차 vendor (Gemini 등) 추가 입력 = 사용자 결정 영역 (의무 아님 — 1건 회수로 trigger #7 충족).

### 7.2 ⭐ GPT-5.5 응답 5 보강점 (입력 — 반영 위치)

| # | 보강점 | 외부 Q | 반영 위치 | 핵심 |
|----|----|----|----|----|
| 1 | **positive allow-list > negative detection** | Q1/Q2 | I-1 | 사람 전용 signed commit 만 T3 허용. author/committer/trailer = 신뢰 신호 아님 → 참고 신호 (신뢰 등급 표 ↓) |
| 2 | **GHES pre-receive ≠ GitHub.com 기본** | Q4 | I-2 (a) | GitHub.com 현실적 server-side = ruleset + CI provenance check. pre-receive = Enterprise Server appliance 한정 |
| 3 | **runtime = sensor, 최종 reject = Hermes 밖** | Q3/Q7 | I-2 (b) / I-5 / §3.3.1 | Group I runtime = provenance sensor/audit producer. 최종 reject 권한 = ruleset/container ACL/hardware key (Hermes ≠ root of trust *강화*) |
| 4 | **false positive 통제 = 범위 한정 + observe mode + quarantine** | Q5/Q6 | I-7 | T3 path 한정 + 1~2주 observe mode + reject 대신 quarantine branch/patch artifact + 사람 commit 기준 명시 |
| 5 | **`.git/` 직접 변조 gap + negative control only** | Q8 | §3.3.1 / §3.3.2 | `.git/` 변조는 commit 검사 사각 → filesystem ACL 책무. Group I = negative control only (PMO positive evidence 오용 금지) |

#### 외부 응답 신뢰 등급 표 (Q2 — I-1 식별 신뢰성 평가 입력)

| 신호 | 신뢰도 | 판단 |
|----|----|----|
| author / committer name·email | 낮음 | spoof 가능, 인증 신호 아님 |
| commit trailer | 낮음 | convention 한정, Hermes 작성 가능 |
| committer email domain | 낮음~중간 | 계정 관리 엄격 시만 보조 |
| verified signature | 중간~높음 | 키 격리 시 강함 / 키 공유 시 무력화 |
| server-observed pusher identity | 중간~높음 | token 격리 시 강함 / token 공유 시 무력화 |
| **human-only hardware-backed key** | **높음** | 1인 운영 최실용 강신호 |

> ⚠️ 위 신뢰 등급 = 외부 *입력* — I-1 식별 신뢰성 *결정* 은 Agent A(기술 신뢰) + Agent B(우회·위장 시나리오) 독립 평가가 발효. brief 기존 I-1 의 "author/committer 메타" 를 *root signal* 로 쓰지 말 것이라는 외부 경고를 합의 입력으로 명시.

### 7.3 ⚠️ 외부 framing 권고 *flag* (채택 아님 — 풀 3+1 + 사용자 결정 영역)

외부 응답 최종 권고는 Group I 설계명을 다음으로 바꾸라는 것:

> **"Hermes-originated commit auto-reject"** → **"Human-authorized T3 change enforcement with Hermes credential isolation"**

근거: "metadata 기반 Hermes 식별"을 중심에 두면 구현 단계에서 *잘못된 안전감(false sense of security)* 을 만들 수 있고, 중심은 **credential isolation + protected branch enforcement + CI provenance + filesystem ACL 의 결합**이어야 한다는 것.

**본 brief v2 의 처리**: 이 framing 권고를 **flag 로만 기록** — *채택/발효 0건*. 근거:
- 외부 응답 = 입력 한정 (§7.1) — framing 변경은 G3 §2.2 #20 / §2.5 / §4.5 본문 + Group α §6.1 cross-reference 명칭과 연동되는 *결정* → 풀 3+1 + 사용자 명시 권한 (brief §0.3 금지: "G3 §2.2 #20 본문 변경 0건").
- ⚠️ **정합성 평가 (입력)**: 외부 framing 은 brief 와 *충돌하지 않고 강화* 방향 — brief §3.3 Defense in depth 3-layer + §4.5 self-reference + §5.1 trigger #5 (Hermes ≠ root of trust) 가 이미 "credential/enforcement boundary 중심" 골격을 가짐. 외부 권고는 *명칭*을 그 골격에 맞추라는 것 (실 설계 방향 전환 아님). → Reviewer 가 §6 에서 "명칭 유지 + 중심 명제 명시" vs "명칭 재정의" 를 판정 영역으로 다룰 것 권고.
- framing *결정* = 풀 3+1 Reviewer 종합 + 사용자 명시 (자동 채택 0건).

---

## 8. Rollback Trigger 통합 매트릭스 (Group I 한정)

| Trigger | 발화 조건 | 발화 시 행동 |
|----|----|----|
| **ADR-011 §2.4** | T3 영역 (§2.2 #20 enforcement) 결정 | 풀 3+1 + 외부 LLM 1+ + 사용자 명시 |
| **`consensus_self_reference_detected`** (G4 §3.8.2 #7) | Hermes-originated commit 이 합의 보고서 / verdict 변조 시도 (TM-2) | 시도 주체 Skill T1+T2 권한 revoke + 합의 자기참조 분석 + audit |
| **`policy_drift_detected`** (G4 §3.8.2 #9) | Hermes-originated commit 이 gate 정의 / 정책성 파일 변경 시도 (TM-1) | 동상 + 컨테이너 정지 |
| **`gate_enforcement_bypass_detected`** (G4 §3.8.2 #10 후보) | §2.6 (a)~(e) 위반 공통 trigger | 동상 + Evidence 보완 의무 |
| **R-I-MULTIHOST** (신규 후보) | multi-host / 다인 전환 결정 | §5.5 추가 layer 의무 발동 (ADR-012 §원칙 12 Layer 3/5) + Group I 식별 강화 재평가 |
| **R-I-IMPL-BOUNDARY** (신규 후보) | Group I 실 강제 hook 구현 진입 | Implementation/Runtime PASS + Backlog #6 연결 + 별도 풀 3+1 |
| **R-I-CONFIG-CHANGE** (v2 신규 후보 — 외부 §7.2 #5/Q7) | Group I enforcement *설정 자체* (ruleset / CI provenance workflow / audit log 보존 정책) 변경 시도 | T3 분류 → Hermes 는 해당 token 미보유 + 변경 = 풀 3+1 + 사용자 명시. self-reference 차단 (Hermes 가 자기 차단책을 끄지 못함) |

### 8.1 후속 단계 Rollback Trigger (본 brief 영역 외)

| 영역 | 후속 Rollback Trigger | 분리 사유 |
|----|----|----|
| Group I 실 hook 구현 | Implementation/Runtime PASS + Backlog #6 + 별도 풀 3+1 + 사용자 명시 | Implementation 영역 |
| AR-3 실 branch protection 활성화 | Backlog #6 + 사용자 명시 (Group α C-1) | Group α 영역 |
| Hermes PMO 격상 (Layer F) | 4 게이트 PASS + 외부 LLM 2 또는 1+사람 + 사용자 명시 | Layer F 영역 |

---

## 9. 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

| 옵션 | 영역 | 후속 단계 |
|----|----|----|
| **(A)** | 본 brief v2 그대로 승인 → **Group I 풀 3+1 합의 진입** (Agent A/B/C + Reviewer, §5 판정 발효 + 외부 입력 = GPT-5.5 응답 §7.2/§7.3 회수 완료 — trigger #7 충족, 추가 vendor 의무 아님) | 합의 보고서 작성 |
| (B) | 본 brief 일부 수정 요청 → 수정 후 승인 | v2 작성 |
| (C) | 본 brief 승인 → commit (`docs/phase0/group-i-hermes-originated-commit-autoreject-full-3plus1-brief.md`) *까지만* (합의 보류) | 1 commit (사용자 명시 시) |
| (D) | 본 brief 보류 → GP-5 C-2 완전 해소 trigger = facade real 본문 P1 v2 (Backlog #4 / GP-5 C-3) 별도 풀 3+1 | Backlog #4 |
| (E) | 본 brief 보류 → MVP-2 deepening roadmap / `roadmap-mvp1.md` Reviewer-only 단축 합의 (MVP-1 entry #5) | 별도 |
| (F) | 본 brief 보류 → 세션 종료 | — |

> 본 brief = **brief 단계 한정** (staged cycle: brief → 승인 → 합의 → commit → push). 합의 / commit / push = 사용자 명시 승인 후 별도 단계. Group I 합의 = **풀 3+1 의무** (§5 권고 — 발효는 합의/사용자 결정). 본 brief 완료 시 Group α §8 옵션 (E) 분리 권고 영역 진입 정비 완료.

---

## 10. 한 단락 요약

Backlog #3 中 **Group I (Hermes-originated commit auto-reject)** 단독 풀 3+1 합의 *진입 전 정비* DRAFT — Group α `2026-05-14` 합의 condition **C-2** ("AI agent self-approval 차단 = Group I 결합 필수") + §8 옵션 (E) 분리 권고 영역. Group I = **G3 §2.2 #20** ("합의 결과 silent override 또는 수정", T3 절대 금지) 의 *git commit 차원 enforcement* — Hermes runtime 이 단독 생성한 commit (특히 `.git/` / 합의 보고서 / ADR / Constitution / gate 정의 / external-review / 정책성 파일) 을 자동 식별·차단 + audit + 사용자 alert. **AR-3 (Group α) × Group I = Defense in depth** — Group α (branch protection + `--no-verify` 차단, GitHub repo) + Group I (Hermes-originated commit 식별 차단, Hermes runtime) + G3 §2.5 (filesystem read_only ACL) 3-layer 결합 (책무 분리 유지 = 단일 source-of-truth 핵심 제약 #4 보존). 8 결정 영역 = 식별 방법(I-1) / 차단 지점(I-2) / 보호 범위(I-3) / Defense in depth 결합(I-4) / §4 self-reference 연결(I-5) / Rollback·audit(I-6) / SPOF(I-7) / 구현 시점 의존(I-8). **합의 형태 판정 (사용자 명시 요청 핵심): Group I = T3 보안 enforcement 영역 → 풀 3+1 (Agent A/B/C + Reviewer) *의무*, Reviewer-only 단축 *부적격*** — 트리거 #2 (T3 BLOCKING) + #5 (5 핵심 제약 #1 Hermes ≠ root of trust 직결, Group α §6.1 명시) + #7 (외부 LLM cross-vendor blind 미충족 — 기존 응답 AR-3 중심, Group I 식별·차단 thin) + §4 self-reference 순환 권위 구조 (§4.2 원칙 2 "Reviewer-only 또는 외부 LLM 필수"). 1인 single-host SPOF (§5.5) = 사용자 자신 commit 허용 + Hermes-originated 만 차단 → 식별 신뢰성 한계 의도적 수용 + multi-host 전환 시 추가 layer 트리거. **v2 (2026-05-20): 외부 cross-vendor blind 응답 1건 (GPT-5.5 Thinking) 회수 → trigger #7 충족.** 응답의 5 보강점 = (1) positive allow-list > negative detection (metadata = 참고 신호 한정, I-1) / (2) GHES pre-receive ≠ GitHub.com 기본 — ruleset+CI provenance check 중심 (I-2) / (3) runtime = sensor·audit producer, 최종 reject = Hermes 밖 (I-2/I-5/§3.3.1, Hermes ≠ root of trust 강화) / (4) false positive 통제 = T3 path 한정 + observe mode + quarantine (I-7) / (5) `.git/` 직접 변조 gap = filesystem ACL 책무 + negative-control-only 조항 (§3.3) — 모두 *입력 한정* 반영 (강제 채택 0건). 외부 framing 권고 ("Hermes-originated commit auto-reject → Human-authorized T3 change enforcement with Hermes credential isolation", §7.3) = *flag 한정* (채택/발효 0건 — 풀 3+1 Reviewer + 사용자 결정). 외부 권고는 brief 기존 골격(§3.3 Defense in depth + §4.5 + §5.1 trigger #5)과 *충돌 없이 강화* 방향. 본 brief 는 결론을 *선취하지 않으며* (판정·식별 방법·차단 지점·framing *결정* = 풀 3+1 독립 평가 + Reviewer 종합), 실 강제 = Implementation/Runtime PASS + Backlog #6 연결 영역 별도. 본 brief = 진입 정비 DRAFT v2 한정 — 합의 보고서 작성 / commit / push / Hermes runtime 실 구현 / 실 차단 hook 구현 / Hermes upstream 변경 / 수단 결정 / threshold 고정 / CI workflow 변경 / actual run / Operational Readiness PASS / Hermes PMO 격상 / MVP-1 exit / Phase α defer-lockdown 변경 모두 0건이며, 모든 *결정* 은 별도 풀 3+1 합의 (사용자 명시 승인 후).

---

## 부록 A — 본 brief 답습 출처

| 출처 | 답습 영역 |
|----|----|
| `hermes-not-root-of-trust-runtime.md` §2.2 #20 | 1차 권위 — Hermes-originated commit auto-reject 정의 + 강제 메커니즘 |
| 동 §2.5 (보호 대상 16건) + §2.6 (Gate Enforcement TM-1~TM-8) | 보호 범위(I-3) + Rollback(I-6) |
| 동 §4 (합의 인프라 순환 권위) + §4.5 (합의 결과 처리 권한) | self-reference 연결(I-5) + §4.2 원칙 2 (Reviewer-only/외부 LLM 필수) |
| 동 §5.5 (SPOF Accepted Risk) | 1인 single-host 한계(I-7) |
| `3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md` §5.2 + §6.1 + C-2 + §8 (E) | AR-3 × Group I Defense in depth + 결합 필수 + 분리 권고 |
| `governance-preconditions.md` §1.2.6 (P10) + §9.2 | Hermes 변조 차단 매트릭스 4항목 + 자기참조 차단 |
| ADR-012 §2.12 #3 (git commit 차단) + §원칙 12 (single-host SPOF) | 변조 차단 4항목 中 git commit + multi-host 전환 |
| `2026-05-13-backlog3-t3-zone-review-request.md` §264 row 8 + response 2건 | 외부 LLM 입력 한계 명시(§7) |
| **`2026-05-20-group-i-hermes-originated-commit-autoreject-review-response-gpt.md` (GPT-5.5 Thinking)** | **v2 신규 외부 입력 — Q1~Q8 + 5 보강점(§7.2) + framing 권고(§7.3). trigger #7 충족.** |
| `backlog3-groupgamma2-st4-vault-hsm-full-3plus1-brief.md` §5.2 | 풀 3+1 vs Reviewer-only trigger 매트릭스 형식 답습 |

## 부록 B — 금지 사항 (사용자 명시 영구 답습)

본 brief 의 어떤 §도 그 자체로 다음을 발생시키지 않는다:
풀 3+1 합의 보고서 작성 / commit / push / **Hermes runtime 실 구현** / **Hermes-originated commit 실 차단 hook 구현** (git pre-commit / pre-receive / filesystem ACL / `read_only` mount / `cap_drop` / CI step 본문) / **Hermes upstream 변경** (Dockerfile / `hermes-version.yaml` / upstream PR) / **수단 결정** (식별 방법·차단 지점·보호 범위 고정) / **threshold 고정** / CI workflow 변경 / actual run 재실행 / workflow_dispatch 추가 / paths 필터 변경 / **Operational Readiness PASS** (Layer E) / **Hermes PMO 격상** (Layer F) / **MVP-1 exit 발효** / **Phase α defer-lockdown 변경** / G3 §2.2 #20·§2.5·§2.6·§4·§5.5 본문 변경 / ADR 본문 자동 갱신 (ADR-008/011/012) / Group α·β·γ-1·γ-2 합의 본문 변경 / GP entry 합의 본문 변경 / Backlog #4·Backlog #6 자동 진입 / §5 T3/T2 판정 *발효* (권고 한정 — 발효는 합의/사용자 결정) / 외부 LLM 응답 결론 강제 채택 / 외부 LLM 추가 자동 호출 / 5 영구 핵심 제약·Provider Liquidity 5-way 약화.
