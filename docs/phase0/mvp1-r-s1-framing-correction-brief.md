# MVP-1 R-S1 cross-reference 정정 + framing 정정 sub-cycle brief ((b2) + (b3) 병렬)

> **scope**: 24번째 entry brief v1.1 carry-over (b2) R-S1 권위 chain 정정 + (b3) roadmap-mvp1 §3.6.3 line 290 framing 정정 (병렬 sub-cycle). 33번째 entry R-S1 raw verify (Agent B + codex 일치) + Reviewer 통합 R-3 답습 (multi-source 재기술).
>
> **합의 형태 권고 = 단축 합의 + 사용자 명시** (cross-reference 정정 영역, R-MVP1-PASS-2 ADR-008 본문 변경 0건 영구 금지 답습, 메인 권위 변경 0건, 메모리 [Ceremony 인플레이션 차단] 답습).
>
> **본 brief 자체에서 cross-reference 정정 적용 0건 의무** — brief 합의 발효 *후* in-place 정정 단계 답습.

---

## §0 답습 출처

| Source | 위치 | 답습 내용 |
|---|---|---|
| 24번째 entry brief v1.1 carry-over (b2) | `docs/phase0/mvp1-1.5th-reinforcement-entry-brief.md` line 159~163 | "governance-preconditions.md 5 위치 + backlog1 합의 본문 §A.2 R1-2 + §2.6.2 R2-1 인용 정정 + 정확한 R1-2 source 위치 확인 + 일관 정정. ADR-008 본문 변경 0건 의무 답습" |
| 24번째 entry brief v1.1 carry-over (b3) | `docs/phase0/mvp1-1.5th-reinforcement-entry-brief.md` line 165 + line 111 | "roadmap-mvp1 §3.6.3 line 290 framing 정정 sub-cycle (N-8 권고)" — ST-2 = "Hermes upstream 변경" 그룹 framing vs 실 ST-2 = sidecar 분리 (Hermes upstream 0건) mismatch |
| 33번째 entry 합의 보고서 R-3 (multi-source 재기술) | `docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md` §2.1 R-3 | "ADR-008 §A.2 R1-2 직접 인용 = source attribution 손상. 권고 정정: ADR-008 차단조건 #1 (SQLCipher) + #4 (어댑터 추상화) + #6 (Docker 격리 + egress 화이트리스트) + 부록 B + ADR-010 + ADR-009 + ADR-011 + roadmap-mvp1 §3 다층 답습으로 재기술" |
| 33번째 entry 합의 보고서 R-MVP1-PASS-2 | brief v1.1 §6 | "R-S1 정정 = cross-reference 정정 한정, ADR-008 본문 변경 영구 금지. 본문 변경 시 풀 3+1 합의 + ADR 권위 영역" |
| 33번째 entry Reviewer R-S1 raw verify | Agent B + codex 일치 | ADR-008 본문 line 136 = §A.2 = "Hermes JSONL Export 검증" + "R1-2" + "§2.6.4" + "§2.6.2" 식별자 ADR-008 본문 0건 |
| 메모리 답습 | `feedback_ceremony_inflation.md` | "lint·framing·citation 정정 = 1-agent 직접, CLAUDE.md §3 매트릭스 실효 답습 의무" → 단축 합의 자격 |
| 34번째 entry paths-aware audit 완료 | `docs/phase0/mvp1-paths-aware-workflow-audit-evidence.md` | 33번째 D-5 (vi) carry-over 해소 + 다음 우선순위 진입 자격 |

---

## §1 scope (본 sub-cycle 한정)

### 1.1 본 sub-cycle 의 본질

| 항목 | 내용 |
|---|---|
| **scope** | (b2) R-S1 cross-reference 정정 + (b3) roadmap-mvp1 §3.6.3 line 290 framing 정정 (병렬 단일 sub-cycle, cross-reference 정정 영역 유사 = Agent C C-N-6 답습) |
| **영역** | governance-preconditions.md 6 위치 + backlog1 합의 본문 3 위치 + roadmap-mvp1 §3.6.3 line 290 framing |
| **합의 형태 권고** | **단축 합의 + 사용자 명시** (Reviewer-only, cross-reference 정정 영역 + 메인 권위 변경 0건) |
| **변경 0건 의무** | ADR-008 본문 변경 0건 (R-MVP1-PASS-2 영구 금지 답습) / ADR-011 본문 0 / ADR-010 본문 0 / ADR-009 본문 0 / ADR-012 본문 0 / 헌법 본문 0 / 11 workflow 본문 0 / src 0 / tools 0 / docker 0 / (b1) 4 sub-cycle 본문 0 |
| **변경 허용 영역** | `docs/architecture/governance-preconditions.md` 6 위치 (line 106 / 343 / 488 / 498 / 508 / 523) cross-reference 정정 + `docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md` 3 위치 (line 12 / 84 / 390) cross-reference 정정 + `docs/architecture/implementation-runtime-roadmap-mvp1.md` §3.6.3 line 290 framing 정정 |

### 1.2 본 sub-cycle 이 *하지 않는* 것 (변경 0건 의무)

| # | 항목 | 변경 자격 |
|---|---|---|
| 1 | ADR-008 본문 변경 (`§A.2` / `§2.6.4` / `§2.6.2` / "R1-2" / "R2-1" 라벨 본문 추가/변경) | **0건 영구 금지** (R-MVP1-PASS-2 답습, R-MVP1-PASS-10 답습) |
| 2 | ADR-011 / ADR-010 / ADR-009 / ADR-012 본문 변경 | 0건 |
| 3 | 헌법 본문 변경 | 0건 (5조-2 Provider Liquidity 비협상 답습) |
| 4 | 11 workflow 본문 변경 | 0건 (34번째 entry audit 답습) |
| 5 | branch protection rule 변경 | 0건 (31번째 entry 7 contexts 답습) |
| 6 | (b1) 4 sub-cycle brief + 합의 본문 변경 | 0건 |
| 7 | 33번째 entry PASS 발효 evidence 변경 | 0건 |
| 8 | roadmap-mvp1 §2.2 / §3.5 / §4.5 / §4.7.3 / §5.1 / §9 본문 변경 | 0건 (§3.6.3 line 290 framing 정정 한정) |
| 9 | src / tools / docker / `.pre-commit-config.yaml` / `.githooks/` 본문 변경 | 0건 |
| 10 | governance-preconditions 의 §5 (또는 다른 §) 본문 변경 | 0건 (6 위치 cross-reference 정정 한정) |
| 11 | backlog1 합의 본문 §1~§5 (또는 다른 §) 본문 변경 | 0건 (3 위치 cross-reference 정정 한정) |
| 12 | MVP-2 진입 자격 발효 | 0건 (별도 합의) |
| 13 | adapters/llm/facade.py placeholder → real | 0건 ((d) carry-over) |
| 14 | 32번째 entry 프라이데이 brief / 합의 본문 변경 | 0건 (별도 cycle) |

---

## §2 R-S1 cross-reference 정정 매트릭스 (R-3 multi-source 재기술 답습)

### 2.1 ADR-008 본문 실 권위 (raw verify 답습, 33번째 Reviewer + Agent B + codex 일치)

| ADR-008 영역 | 본문 line | 실 내용 | 인용 권위 |
|---|---|---|---|
| §A.2 | line 136 | "Hermes JSONL Export 검증" | Hermes 영역 (secret storage 영역 *아님*) |
| 차단조건 #1 | line 17 영역 | SQLCipher (저장 경로 secret 보호 핵심) | GP-3 (c) ADR 권위 |
| 차단조건 #4 | line 97 / 149 | 어댑터 추상화 (Provider Liquidity 경계) | GP-5 (c) ADR 권위 |
| 차단조건 #6 | line 17~23 영역 | Docker 격리 + egress 화이트리스트 | GP-3 (c) ADR 권위 |
| 부록 B | line 240~ | Hermes PMO 격상 절차 + 12 조건 + cross-reference Amendment | 권위 chain 통합 |
| "R1-2" 식별자 | **본문 0건** | (식별자 부재) | source 손상 |
| "§2.6.4" 식별자 | **본문 0건** | (식별자 부재) | source 손상 |
| "§2.6.2" 식별자 | **본문 0건** | (식별자 부재) | source 손상 |

### 2.2 정정 본문 (R-3 multi-source 재기술 답습)

**정정 전 (source 손상 인용)**:
- `ADR-008 §A.2 R1-2` (저장 경로 secret 보호 권위로 인용)
- `ADR-008 §2.6.4 R1-2` (OAuth credentials 처리 강화로 인용)
- `ADR-008 §2.6.2 R2-1` (docker secret 정의로 인용)

**정정 후 (multi-source 재기술, R-3 답습)**:

| GP-3 영역 (저장 경로 secret 보호) | GP-5 영역 (어댑터 추상화) |
|---|---|
| `ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리 + egress 화이트리스트) + 부록 B + ADR-010 (SQLCipher Vault) + ADR-011 (수단/목적 분리 §2.1 (a)~(d)) + 헌법 8조 #1` | `ADR-008 차단조건 #4 (어댑터 추상화) + 부록 B + ADR-009 (자체 Adapter v2.0) + ADR-011` |

### 2.3 정정 적용 위치 매트릭스

#### (b2-A) governance-preconditions.md (6 위치)

| # | line | 정정 전 | 정정 후 |
|---|---|---|---|
| 1 | 106 (P3 row) | `ADR-008 §2.6.4 R1-2 + entrypoint stat 검증` | `ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + ADR-010 + ADR-011 + entrypoint stat 검증` |
| 2 | 343 (GP-3 row) | `ADR-008 §2.6.4 R1-2 + R2-1 + 헌법 8조 #1` | `ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 + 헌법 8조 #1` |
| 3 | 488 | `docker secret 정의 (R2-1) \| docker-compose.yml (ADR-008 §2.6.2)` | `docker secret 정의 \| docker-compose.yml (ADR-008 차단조건 #6 답습)` |
| 4 | 498 | `ADR-008 §2.6.4 R1-2 (OAuth credentials 처리 강화) 명시 (충족됨)` | `ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 (OAuth credentials 처리 강화) 명시 (충족됨)` |
| 5 | 508 ((c) cell) | `ADR-008 §2.6.4 R1-2 + 헌법 8조 #1 + 본 §5` | `ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + 헌법 8조 #1 + 본 §5` |
| 6 | 523 | `ADR-008 §2.6.4 R1-2: 본문 변경 없음, GP-3 cross-reference 추가` | `ADR-008 cross-reference (차단조건 #1 + #6 + 부록 B): 본문 변경 없음, GP-3 cross-reference 추가 (33번째 entry R-S1 정정 답습)` |

#### (b2-B) backlog1 합의 본문 (3 위치)

| # | line | 정정 전 | 정정 후 |
|---|---|---|---|
| 1 | 12 | `ADR-008 §A.2 R1-2 + §2.6.2 R2-1 (저장 경로 secret 보호 권위)` | `ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 (저장 경로 secret 보호 권위, 35번째 entry R-S1 정정 답습)` |
| 2 | 84 | `Hermes upstream 변경 / 외부 LLM 자동 호출 \| ❌ (ADR-008 §2.6.2 R2-1 답습)` | `Hermes upstream 변경 / 외부 LLM 자동 호출 \| ❌ (ADR-008 차단조건 #6 답습 + ADR-011 답습)` |
| 3 | 390 | `ADR-008 §A.2 R1-2 + §2.6.2 R2-1 답습 \| ✅ (cross-reference 답습 한정 — 본문 변경 0건)` | `ADR-008 차단조건 #1 + #6 + 부록 B 답습 \| ✅ (cross-reference 답습 한정 — 본문 변경 0건, 35번째 entry R-S1 정정 답습)` |

---

## §3 (b3) roadmap-mvp1 §3.6.3 line 290 framing 정정

### 3.1 정정 전 (mismatch)

```
| ST-1 / ST-2 / ST-5 진입 (Hermes upstream 변경) | 풀 3+1 합의 + Hermes upstream PR 검토 | Hermes upstream 영역 진입 = 책무 경계 변경 |
```

**mismatch 식별** (24번째 entry brief line 111 답습):
- roadmap framing: ST-1 + ST-2 + ST-5 = "Hermes upstream 변경" 그룹
- 실 ST-2: sidecar 분리 가능 (backlog1 §2.2.2 답습) → Hermes upstream Dockerfile 변경 0건 (R-MVP1-1.5-ST2-2 영구 금지 답습)
- (b1) 4 sub-cycle ST-2 실 구현 (28번째 entry) = sidecar 인프라 (docker/gp3-st2-poc/) 발효 + Hermes upstream 변경 0건 답습

### 3.2 정정 후 (framing 분리)

```
| ST-1 / ST-5 진입 (Hermes upstream 변경) | 풀 3+1 합의 + Hermes upstream PR 검토 | Hermes upstream 영역 진입 = 책무 경계 변경 |
| ST-2 진입 (sidecar 분리, Hermes upstream 변경 ❌ 불필요) | 풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시 | (b1) 4 sub-cycle 발효 답습 (28번째 entry sidecar 인프라 + R-MVP1-1.5-ST2-2 Hermes upstream 변경 영구 금지) |
```

→ ST-2 = 별도 row 분리 + framing 정확화 (sidecar 분리 + Hermes upstream 변경 ❌).

---

## §4 사용자 결정 항목 (brief 합의 진입 전)

| # | 항목 | 후보 | 권고 |
|---|---|---|---|
| **D-1** | 합의 형태 | (i) 단축 합의 (Reviewer-only) / (ii) 풀 3+1 | **(i) 단축 합의 (Reviewer-only)** — cross-reference 정정 영역 + R-MVP1-PASS-2 영구 금지 답습 + 메인 권위 변경 0건 + 메모리 [Ceremony 인플레이션 차단] 답습 |
| **D-2** | 정정 형태 | (A) multi-source 재기술 (R-3 답습) / (B) 단순 인용 정정 (governance-preconditions 자체 R1-2 정의로 변환) | **(A) multi-source 재기술** — 33번째 entry R-3 BLOCKING 답습. ADR-008 본문 실 권위 (차단조건 #1/#4/#6 + 부록 B) + ADR-010/ADR-011/ADR-009 multi-source 정확 attribution |
| **D-3** | framing 정정 형태 | (X) ST-2 별도 row 분리 (§3.1 답습) / (Y) 단일 row 안 footnote 추가 | **(X) ST-2 별도 row 분리** — framing 정확성 + ST-2 합의 형태 변경 (풀 3+1 + Hermes upstream PR 검토 → 풀 3+1 + 외부 LLM 1+ + 사용자 명시) 정확 표시 |
| **D-4** | 적용 단계 | (i) 단일 commit 모두 적용 / (ii) governance + backlog1 별도 commit + roadmap 별도 commit | **(i) 단일 commit** — cross-reference 정정 영역 유사 (병렬 sub-cycle 답습) |

---

## §5 합의 형태 권고 + 다음 단계

### 5.1 합의 형태 권고

**단축 합의 + 사용자 명시 (Reviewer-only)** 권고 — 근거:

| 근거 | 내용 |
|---|---|
| **24번째 entry brief carry-over (b2)** | "ADR-008 본문 변경 0건 의무" + cross-reference 정정 영역 명시 |
| **33번째 entry R-MVP1-PASS-2** | ADR-008 본문 변경 영구 금지 답습. cross-reference 정정 = 단축 합의 자격 |
| **메모리 [Ceremony 인플레이션 차단]** | "lint·framing·citation 정정 = 1-agent 직접, CLAUDE.md §3 매트릭스 실효 답습 의무" |
| **메인 권위 변경 0건** | ADR / 헌법 / roadmap §2.2 / (b1) 4 sub-cycle / PASS 발효 evidence 모두 0건 |
| **풀 3+1 승격 trigger** | 5/5 발화 0건 (① 새 권위 결정 0 / ② Tier-2/3 자동 확장 0 / ③ PASS 자동 선언 0 / ④ 후속 합의 본문 변경 0 — cross-reference 정정 한정 / ⑤ ADR-011 5조건 자동 충족 선언 0) |
| **34번째 entry 답습** | 1-agent 직접 cycle 발효 답습 (`5f876ea`) |

### 5.2 다음 단계 (단축 cycle 6단계 답습)

1. ✅ **brief 작성** (본 단계)
2. ⏳ **사용자 승인** — D-1~D-4 결정 의무
3. ⏳ **단축 합의 (Reviewer-only)** — 5/5 풀 3+1 승격 trigger 발화 0건 검증 + cross-reference verbatim cross-check
4. ⏳ **in-place 정정 적용** — governance-preconditions 6 위치 + backlog1 합의 3 위치 + roadmap §3.6.3 line 290 framing
5. ⏳ **SESSION + INDEX + commit + push** (SSH 답습)
6. ⏳ **다음 cycle**: (iii) Markdown evidence 통합 → (b1-PC1-D6) → PR #2 merge → (d) facade → MVP-2 → 32번째 프라이데이

---

## §6 본 brief 자기진단 (8/8 통과 의무)

| # | 항목 | 통과 |
|---|---|---|
| 1 | 본 brief 자체 cross-reference 정정 적용 0건 / ADR 본문 변경 0건 (R-MVP1-PASS-2 영구 금지 답습) | ✅ |
| 2 | R-S1 raw verify 답습 명문 (33번째 Reviewer + Agent B + codex 일치) + ADR-008 본문 §A.2 = "Hermes JSONL Export 검증" + R1-2 식별자 부재 cross-check | ✅ §2.1 |
| 3 | governance-preconditions 6 위치 + backlog1 3 위치 정정 매트릭스 명문 (R-3 multi-source 재기술 답습) | ✅ §2.3 |
| 4 | roadmap-mvp1 §3.6.3 line 290 framing 정정 mismatch 식별 + 정정 후 본문 명문 | ✅ §3 |
| 5 | 변경 0건 의무 14항 (ADR-008 본문 + 다른 ADR + 헌법 + 11 workflow + (b1) 4 sub-cycle + PASS evidence + 32번째 프라이데이 모두 0건) | ✅ §1.2 |
| 6 | 사용자 결정 D-1~D-4 + 합의 형태 권고 (단축 합의 + 사용자 명시) | ✅ §4 + §5.1 |
| 7 | 풀 3+1 승격 trigger 5/5 발화 0건 검증 + 34번째 entry 1-agent 직접 cycle 답습 | ✅ §5.1 |
| 8 | 다음 단계 6단계 + 다음 cycle 우선순위 답습 (33번째 D-5 + 34번째 paths-aware 완료 후) | ✅ §5.2 |

---

> **본 brief 발효 시점** = 사용자 승인 (§4 D-1~D-4 결정) + Reviewer-only 단축 합의 APPROVE + 본 brief commit. 본 brief 자체 = **cross-reference 정정 + framing 정정 권한 발효 자격 한정**. 실 정정 적용 = brief 합의 발효 *후* in-place 정정 단계 답습 (ADR-008 본문 변경 0건 영구 의무 답습).
