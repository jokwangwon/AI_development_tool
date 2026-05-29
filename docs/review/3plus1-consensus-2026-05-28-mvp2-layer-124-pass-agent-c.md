# Agent C (대안 탐색가) 응답 — Layer 1+2+4 통합 PASS 격상 entry brief (55 entry)

> **본 응답** = 3+1 합의 中 Agent C 단독 응답 (대안 탐색가 관점). 다른 Agent (A / B / codex / Reviewer) 응답 미참조 (병렬 독립). CLAUDE.md §3 Phase 2 답습.
>
> **본 응답 자체로 발생시키는 것 0건** — 본 응답 = 추론적 검증 권고 한정. 실 코드 0 / brief 본문 변경 0 / PASS 발효 0 / 사용자 결정 0. Reviewer 통합 + brief v1.x 흡수 후 cycle 발효.

---

## 검토자 / 직접 read 자료

- **검토자**: Agent C (대안 탐색가, Anthropic Claude Opus 4.7 (1M context))
- **검토 시점**: 2026-05-28
- **검토 대상 PRIMARY**: `docs/phase0/mvp2-layer-124-pass-entry-brief.md` (v1, 443줄)
- **직접 read 자료**:
  - `docs/phase0/mvp2-layer-124-pass-entry-brief.md` v1 (line 1~443 full)
  - `docs/phase0/mvp2-gamma-decision-brief.md` (54 entry) line 1~100
  - `docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md` (54 entry) line 1~80
  - `docs/phase0/mvp2-gamma-layer-separation-brief.md` (53 entry v1.1) line 1~120 + line 240~370
  - `docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md` (53 entry Reviewer) line 1~200
  - `docs/architecture/provider-agnostic-memory-skill-design.md` §4.4.1 (line 625~704)
  - `docs/decisions/ADR-012-evidence-ledger-protection.md` §2.3 + §2.5 + §2.7 + §2.8 (line 160~280)
  - `docs/architecture/implementation-runtime-roadmap.md` (W-A/B/C/D/E + R-6 grep)
  - `docs/phase0/mvp2-entry-brief.md` (52 entry, W-A~E 정의 라인 226~232)

---

## §0 총평

**판정**: ⚠️ **APPROVE WITH CONDITIONS** (BLOCKING **3** + 권고 **5** + NOTE **4**)

**핵심 발견**:
1. 본 brief v1 의 **합의 형태 (풀 3+1 + 외부 LLM 1+) 채택** = 53 entry / 54 entry SESSION carry-over #5 직접 답습 + 24/32/52 entry 동형 패턴. **대안 (b)/(c)/(d) 대비 우위 정합**. 단, **대안 (b) audit-only Reviewer-only 단축** = 53 entry §2.5 보강 답습 가능성이 §4.1 정당화 본문에서 *명시 비교* 부재 → R-C-1 흡수.
2. **denyNonFastForwards 활성화 대안 5개 中 (a) system-wide 선호** = 본 brief §1.3 audit 발견 (local + global 0건) 對 5 option 中 (a)~(e) trade-off 평가 *미명시* → R-C-2 흡수.
3. **PASS evidence template Layer subsection 강제** = (γ-c) 특화 의무 1 답습 충실. 대안 (단일 통합 evidence + Layer tag / Layer 별 evidence file 분리) 對 비교 부재 → R-C-3 흡수.
4. PASS 발효 *시점* 대안 (Layer 통합 PASS = MVP-2 PASS 동시/선행/분리) 평가 = §8 다음 단계 답습 한정, brief §0 framing 內 *명시 비교* 부재 → N-C-1 흡수.
5. **(γ-c) 특화 의무 4 영구 답습** = 54 entry §1.3 답습 충실. 단, RT-PASS-1/2/3 신규 trigger 검출 메커니즘 (lint vs review vs runtime hook) 비교 부재 → N-C-2 흡수.
6. (E-α/β/γ) 외부 LLM 자격 옵션 3 분류 = 53 entry N-15 답습 정합. 단, (E-β) 사용자 직접 호출 추가 (codex + Gemini cross-vendor 2+ 강화) 동형 대안 시점 평가 부재 → N-C-3 흡수.
7. **24/52 entry entry brief 동형 패턴 답습** 정합. 단, brief v1 = **PASS 격상 *진입 합의 한정*** (실 구현 + PASS 발효 = 별도 cycle) framing 은 24 entry MVP-1 entry brief 와 32 entry MVP-1 PASS 발효 합의 *중간 단계* 신규 framing → cycle 수 자체 (54 → 55 → (β) → 실 구현 → Layer 통합 PASS 발효 → MVP-2 PASS 발효 = 5 cycle 등가) 명시 부재 → N-C-4 흡수.

**대안 탐색가 입장**: brief v1 = **(γ-c) 채택 발효 답습 + (γ-c) 특화 의무 4 영구 답습 한정**의 framing 정합성 충실. 단, 합의 형태 / 활성화 / evidence template / PASS 시점 4 영역 대안 비교 부재 = 추가 framing 보강 의무 (BLOCKING 3 + 권고 5). 본 brief v1.1 흡수 후 합의 발효 가능.

**대안 (γ-e/f/g) 자동 재평가 의무 0** — 53 entry B-8 + 54 entry §0.3 #22 영구 답습 보존.

---

## §1 BLOCKING 3건 (R-C-1 ~ R-C-3)

### R-C-1: 합의 형태 대안 명시 비교 부재 — (a)/(b)/(c)/(d) 4 대안 비교 매트릭스 추가 의무

**영역**: brief §4.1 (line 244~252).

**현 framing**: "풀 3+1 + 외부 LLM 1+" 채택 정당화 6 source (53/54 entry carry-over + (γ-c) 채택 발효 답습 + 32 entry MVP-1 PASS 발효 패턴 + 24/52 동형 + 헌법 5조-2 + ADR-011 §2.1 (e)) 답습 한정. **4 대안 (a) 풀 3+1 + 외부 LLM 1+ (현 권고) / (b) audit-only Reviewer-only 단축 / (c) PASS 격상 통합 / (d) 단계별 합의 (Layer 1 + Layer 2 + Layer 4 분리) 비교 매트릭스 부재**.

**대안 (b) audit-only 단축 가능성**:
- 53 entry §2.5 + 본 cycle §1.3 audit 결과 = PoC 시제 전 영역 충족 (denyNonFastForwards 1 영역 미설정 = 실 구현 sub-cycle 활성화 의무, *진입 자격 합의*에서는 evidence 평가 한정)
- audit-only 단축 시 Reviewer-only 1-agent 합의 = ceremony-inflation 차단 메모리 답습 (`feedback_ceremony_inflation`)
- 54 entry (γ-c) 채택 발효 답습 = 1-agent 직접 합의로 발효 (5/7 trigger 0/7 미발화)

**그러나 본 cycle (55 entry) trigger 발화 자체 검증** (§4.3 답습):
- trigger 1 (큰 결정) = ✅ 발화 (Layer 1+2+4 통합 PASS 격상 *진입 권한 발효* = MVP-2 PASS 발효 *직전 단계*)
- trigger 5 (외부 LLM 응답 통합 필요성) = ✅ 발화 (큰 결정 + cross-vendor 의무)

→ 풀 3+1 + 외부 LLM 1+ 적격 정합. 단, **대안 (b)/(c)/(d) 명시 비교 매트릭스가 brief 內 부재** = 사용자 영역 결정 자료 부족 risk.

**흡수 방향**: brief v1.1 §4.1 다음 매트릭스 추가:

| 대안 | 합의 형태 | trade-off | 본 cycle 적격 |
|------|---------|----------|------------|
| (a) 풀 3+1 + 외부 LLM 1+ (현 권고) | 다관점 + cross-vendor | 2 trigger 발화 / 24/32/52 entry 답습 | ✅ 적격 |
| (b) audit-only Reviewer-only 단축 | ceremony-inflation 차단 | trigger 1 (큰 결정) 발화 시 부적격 / PoC 시제 audit 한정 | ❌ trigger 1 발화 → 부적격 |
| (c) PASS 격상 통합 (실 구현 + 합의 통합) | 1 cycle 효율 | 본 brief §0.3 #14 명시 금지 (진입 합의 ≠ 실 구현) | ❌ 영역 침입 risk |
| (d) 단계별 합의 (Layer 1 + 2 + 4 분리) | 영역 분리 명확 | (γ-c) 특화 의무 3 위반 (통합 동시 발효 영구 답습) | ❌ (γ-c) 의무 위반 |

→ (a) 현 권고 정합. 단 명시 비교 표 추가 의무.

### R-C-2: denyNonFastForwards 활성화 5 대안 (a)~(e) 비교 매트릭스 부재

**영역**: brief §2.3.1 line 167 (Layer 2a PASS 격상 영역 설명) + §5.1 RT-PASS-1 + §5.2 E-PASS-5.

**현 framing**: "`git config --system receive.denyNonFastForwards true` 활성화 + entrypoint 또는 pre-receive hook 강제" (line 167) 한정. **5 활성화 대안 명시 비교 부재**.

**5 대안 trade-off** (Agent C 신규 식별):

| 대안 | 명령 | 적용 범위 | trade-off | 본 cycle 평가 |
|------|------|---------|----------|------------|
| (a) system-wide | `git config --system receive.denyNonFastForwards true` | 호스트 전체 모든 repo | 강제 충실 / root 권한 필요 / 다른 repo 영향 | local dev = 강함, **CI 환경 misfit** (Docker 격리 환경에서는 system 영역이 컨테이너 한정) |
| (b) user-global | `git config --global receive.denyNonFastForwards true` | 사용자 모든 repo | 사용자 보호 / 다른 repo 영향 / 협업 시 다른 사용자 영향 0 | 본 cycle PoC 시제 audit 답습 (local + global 0건) → user-global 추가 0건 |
| (c) per-repo | `git config receive.denyNonFastForwards true` | 본 repo 한정 | 영향 영역 최소 / 다른 repo 영향 0 / 각 repo 반복 의무 | **본 cycle 진입 자격 평가 영역 = per-repo 권고** (반복 의무는 entrypoint script 답습) |
| (d) entrypoint script + Dockerfile | Docker 격리 환경 內 자동 활성화 | Docker container 한정 | reproducible / 환경 의존 명문 / Docker dependency | **본 cycle Docker 격리 PoC 답습 정합** (53 entry §2.5 + 본 brief §2.6 답습) |
| (e) GitHub Actions pre-receive (remote 보조) | GitHub server side | remote push 한정 | local force-push 0 차단 / GitHub 의존 / branch protection 이미 발효 | **branch protection 8 contexts 답습 = (e) 보조 가능** (43 entry 답습) |

→ 본 cycle 권고 = **(c) per-repo + (d) entrypoint script + Dockerfile 조합** (PoC 시제 답습 + reproducible + 영향 최소). (a) system-wide 는 root 권한 + 다른 repo 영향 risk. (b) user-global 은 사용자 다른 repo 영향. (e) 는 (a~d) 1 활성화 후 보조.

**흡수 방향**: brief v1.1 §2.3.1 line 167 다음 5 대안 매트릭스 추가 + 권고 명시 ((c) + (d) 조합).

### R-C-3: PASS evidence template — Layer subsection 강제 vs 통합 evidence + Layer tag vs 별도 layer evidence file 분리 3 대안 비교 부재

**영역**: brief §2.5 (line 191~202) + §5.2 (line 295~313).

**현 framing**: "Layer 1/Layer 2/Layer 4 subsection 강제" ((γ-c) 특화 의무 1 영구 답습, 54 entry §1.3 답습) 한정.

**3 대안 trade-off** (Agent C 신규 식별):

| 대안 | 형식 | 검증 | 회귀 | 사용성 |
|------|----|----|----|------|
| (i) Layer subsection 강제 (현 답습, (γ-c) 특화 의무 1) | 단일 evidence 파일 內 Layer 1 / Layer 2 / Layer 4 분리 section | grep `^## Layer N evidence` lint 가능 | Layer evidence 합산 차단 (RT-PASS-2) | 단일 파일 = 답습 용이 |
| (ii) 통합 evidence + Layer tag | 단일 evidence 파일 + 각 evidence 항목 `[Layer N]` tag | tag grep lint 가능 / subsection 부재 | tag 0 시 Layer 합산 검출 어려움 | tag 형식 자유도 ↑ |
| (iii) 별도 layer evidence file 분리 | `evidence-layer1.md` + `evidence-layer2.md` + `evidence-layer4.md` + `evidence-integration.md` | 파일 부재 검출 가능 | 통합 evidence 분리 강제 | 파일 수 ↑ / 통합 답습 어려움 |

→ **(i) 현 답습 권고** 정합:
- 검증: grep `^## Layer N evidence` lint 가능 (RT-PASS-3 grep / lint 권고)
- 회귀: Layer evidence 합산 차단 명확 (RT-PASS-2 발화 영역 정확)
- 사용성: 단일 파일 답습 용이 (32 entry MVP-1 PASS evidence 답습 패턴)
- (γ-c) 특화 의무 1 영구 답습 = 54 entry §1.3 결정 영역 (재평가 0)

(ii) tag 방식 = subsection 부재 시 Layer 합산 검출 어려움 → RT-PASS-2 검출 능력 ↓ (부적격).
(iii) file 분리 = 통합 evidence 분리 강제 → (γ-c) 특화 의무 3 (통합 동시 발효) 위반 risk.

**흡수 방향**: brief v1.1 §5.2 evidence template 다음 매트릭스 추가 + (i) 답습 정합 명시 + (ii)/(iii) 부적격 근거 명시.

---

## §2 권고 5건 (N-C-1 ~ N-C-5)

### N-C-1: PASS 발효 시점 3 대안 명시 비교 (동시 / 선행 / 분리)

**영역**: brief §8 다음 단계 (line 374~384).

**대안**:
- (시점-α) Layer 통합 PASS 발효 = MVP-2 PASS 발효 *동시* (별도 합의 통합)
- (시점-β) Layer 통합 PASS 발효 = MVP-2 PASS 발효 *선행* (단계적)
- (시점-γ) Layer 통합 PASS 발효 ≠ MVP-2 PASS 발효 (분리)

→ **(시점-β) 권고**:
- 32 entry MVP-1 PASS 발효 답습 패턴 = 각 영역 PASS evidence 수집 → 통합 PASS 발효
- Layer 통합 PASS + GP-2 PASS = MVP-2 PASS 사전조건 (brief §0.3 #15 답습)
- RT-γ-6 R-S1 정정 시점 평가 의무 ((γ-c) 특화 의무 4) = MVP-2 PASS 시점 *직전* 평가 가능
- 단계적 = 영역 격리 명확 (Layer evidence 합산 차단 RT-PASS-2 답습)

(시점-α) 동시 = 합의 cycle 1회 효율 / Layer evidence 합산 risk ↑ (RT-PASS-2 발화 위험).
(시점-γ) 분리 = MVP-2 PASS 자격 검증 어려움.

**흡수 방향**: brief v1.1 §8 다음 단계 시점 매트릭스 추가 + (시점-β) 권고 명시.

### N-C-2: RT-PASS-1/2/3 검출 메커니즘 비교 (lint / review / runtime hook)

**영역**: brief §5.1 line 291~293.

**RT-PASS-1 (denyNonFastForwards 활성화 실패) 검출**:
- (i) lint script (per-repo + per-Docker) — entrypoint script + Dockerfile 內 `git config receive.denyNonFastForwards true` 강제 grep
- (ii) runtime hook (force-push 시도 시 reject log) — 자동 발화 / runtime evidence
- (iii) Reviewer 직접 verify (gh api / git config show) — manual

→ (i) + (ii) 조합 권고 (lint = pre-check / runtime = 실제 차단 verify).

**RT-PASS-2 (Layer evidence 합산) 검출**:
- (i) lint (`grep -c '^## Layer [124] evidence'` ≥ 3 + Layer 합산 표현 regex)
- (ii) Reviewer 직접 verify
- (iii) PR review CI check

→ (i) lint 권고 (계산적 검증 우선, CLAUDE.md §2 답습).

**RT-PASS-3 ("defense-in-depth 충실 답습" 표현 사용) 검출**:
- (i) grep lint (`grep -E '(충실 답습|완전 답습)'` zero-match 의무)
- (ii) Reviewer 직접 verify

→ (i) grep lint 권고 (계산적, CLAUDE.md §2 답습).

**흡수 방향**: brief v1.1 §5.1 RT-PASS-1/2/3 각 trigger row 다음 컬럼 "검출 메커니즘" 추가 + 위 권고 명시.

### N-C-3: 외부 LLM 자격 옵션 (E-α/β/γ) — (E-β) 적용 시점 평가 추가

**영역**: brief §7.2 line 351~357.

**현 framing**: 3 옵션 명시 한정. **본 cycle 권고 = (E-α) Claude tmux+codex** (53 entry 답습) 명시 부재.

**(E-β) 사용자 직접 호출 추가 시점 평가**:
- (E-α) Claude tmux+codex = cross-vendor 1+ 충족 (Anthropic 4 + OpenAI 1)
- (E-β) 사용자 직접 호출 추가 = cross-vendor 2+ 강화 (Anthropic 4 + OpenAI 1 + Gemini 1 등) — Provider Liquidity 비협상 답습 강화
- (E-γ) 외부 LLM 0 = 작은 영역 한정 (본 cycle = 큰 결정 → 부적격)

→ 본 cycle 권고 = **(E-α) 기본 / (E-β) 사용자 결정 시 추가 가능** (cross-vendor 강화 영역).

**흡수 방향**: brief v1.1 §7.2 (E-α) 본 cycle 권고 명시 + (E-β) 사용자 영역 결정 옵션 명시.

### N-C-4: 본 brief 后 cycle 수 정량 매트릭스 추가

**영역**: brief §8 다음 단계 (line 372~384).

**현 framing**: 7 항목 다음 단계 한정. **cycle 수 정량 부재**.

**cycle 수 정량 매트릭스** (Agent C 신규 식별, 시점-β 권고 답습):

| # | cycle | 합의 형태 | 영역 |
|---|------|---------|----|
| 1 | 55 entry (본 cycle) | 풀 3+1 + 외부 LLM 1+ | Layer 통합 PASS 격상 *진입 합의* |
| 2 | (β) sub-수단 결정 cycle | 풀 3+1 (수단별 차등) | R-1~R-5 + L-1~L-5 + W-A~E 결정 |
| 3 | 실 구현 sub-cycle | 1-agent 직접 (계산적 검증, Hook 강제) | denyNonFastForwards + R-6 확장 + evidence 수집 |
| 4 | Layer 통합 PASS 발효 합의 | 풀 3+1 + 외부 LLM 1+ (32 entry 답습) | (a)~(d) evidence + (e) 합의 APPROVE |
| 5 | MVP-2 PASS 발효 합의 | 풀 3+1 + 외부 LLM 1+ (32 entry 답습) | Layer 통합 PASS + GP-2 PASS + 통합 + R-S1 정정 평가 |

→ **5 cycle 등가** (54 → 55 → (β) → 실 구현 → Layer PASS → MVP-2 PASS, 본 cycle 포함).

24/32 entry MVP-1 cycle 수 답습 패턴 vs 본 (γ-c) cycle 수 = 답습 정합 (단계 분리).

**흡수 방향**: brief v1.1 §8 다음 단계 위 매트릭스 추가.

### N-C-5: W 워크플로우 확장 5 대안 (W-A~E) 본 cycle scope 외 명시 강화

**영역**: brief §0.3 #10 + §2.4 line 187 + §8 #1.

**현 framing**: "(β) sub-수단 결정" 영역 (line 47 + line 218) 한정. **W-A~E 5 대안 정의 본 brief 內 부재** (52 entry brief §2.3 + 53 entry 답습).

**Agent C 검토 결과**: 본 cycle = framing 한정 (β 영역 ≠ 본 cycle). W 5 대안 정의 본 brief 內 재현 의무 0 (52 entry §2.3 line 226~232 답습 충실). 단 cross-reference 명시 권고:

| W 대안 | 정의 (52 entry 답습) | 본 cycle 평가 |
|--------|--------------------|------------|
| W-A | 단일 R-6 확장 통합 | (β) 시점 평가, ceremony-inflation 차단 / 충돌 risk |
| W-B | 별도 workflow 2개 분리 | (β) 시점 평가 |
| W-C | 단계 분리 (GP-2 우선 + Layer 4 후속) | (β) 시점 평가 |
| W-D | roadmap §5.3 답습 별도 progression | (β) 시점 평가 |
| W-E | pre-commit hook 활용 | (β) 시점 평가 |

→ 추가 W 대안 식별 0 (52 entry 5 대안 답습 충실).

**흡수 방향**: brief v1.1 §0.3 #10 + §2.4 line 187 W-A~E 정의 cross-reference 명시 (52 entry §2.3 답습).

---

## §3 NOTE 4건 (NOTE-C-1 ~ NOTE-C-4)

### NOTE-C-1: brief v1 framing 답습 정합성 — 24/52 entry 동형 패턴 vs 55 entry 신규 framing 비교

24 entry MVP-1 entry brief + 52 entry MVP-2 entry brief = "MVP entry 합의 + 후속 PASS 발효 합의 분리" framing.

본 brief v1 = "Layer 통합 PASS 격상 *진입 합의* + 후속 실 구현 sub-cycle + Layer 통합 PASS 발효 합의 + MVP-2 PASS 발효 합의 분리" framing — 24/52 entry 答습 + 1 추가 단계 (Layer 통합 PASS).

→ framing 답습 정합 + 1 추가 단계 정당화 ((γ-c) 특화 의무 3 영구 답습 — 통합 동시 발효 의무 = 별도 합의 의무).

### NOTE-C-2: (γ-c) 특화 의무 4 영구 답습 = 결정 영역 보존 충실

본 brief §1.2 + §4.2 + §6.2 #4/5 = 54 entry §1.3 의무 4 답습 충실. 의무 1 (Layer subsection 강제) + 의무 2 ("부분 답습" framing) + 의무 3 (통합 동시 발효) + 의무 4 (RT-γ-6 평가) 영구 답습.

→ Agent C 본 응답 = 의무 4 보존 보강 한정 (재평가 0).

### NOTE-C-3: §10 P-7 cascade risk + P-8 24 fixture 정량 verify 답습 정합

본 brief §10 P-7 = "본 brief 작성자 = 52/53/54 entry brief 작성자 (Claude Opus 4.7) → cascade risk" → 53 entry 답습 cascade 정합성 검증 + cross-vendor 후속 합의 시 codex (E-α) 호출 답습 명시.

P-8 = tests/canonical 24 fixture 정량 verify (72 files / 8 × 3 × 3) = 52 entry Agent A R-A-2 carry-over 해소 evidence. 본 cycle audit filesystem direct 답습.

→ 자기진단 정합. Agent C 추가 권고 0.

### NOTE-C-4: cross-vendor 형식 충족 답습 검증

본 brief §4.1 정당화 출처 #5 (헌법 5조-2 Provider Liquidity) + §7.1 #2 + §10 P-7. 본 cycle 합의 발효 시 외부 LLM 1+ (codex 답습) = cross-vendor 형식 충족.

→ Provider Liquidity 비협상 답습 충실. Agent C 추가 권고 0.

---

## §4 합의 형태 대안 평가 (질문 1)

### §4.1 4 대안 trade-off (R-C-1 답습)

| 대안 | trade-off | 본 cycle 적격 |
|------|----------|------------|
| **(a) 풀 3+1 + 외부 LLM 1+ (현 권고)** | 다관점 + cross-vendor 의무 충족 / 24/32/52 entry 동형 답습 | ✅ **적격** (trigger 1 + 5 발화) |
| (b) audit brief 한정 Reviewer-only 단축 | ceremony-inflation 차단 / 53 entry §2.5 보강 답습 가능 | ❌ trigger 1 (큰 결정) 발화 → 부적격 |
| (c) PASS 격상 통합 (실 구현 + 합의 통합) | 1 cycle 효율 | ❌ §0.3 #14 명시 금지 (진입 합의 ≠ 실 구현) |
| (d) 단계별 합의 (Layer 1 + 2 + 4 분리) | 영역 분리 명확 | ❌ (γ-c) 특화 의무 3 위반 (통합 동시 발효 영구 답습) |

→ **(a) 권고**. R-C-1 흡수 후 brief v1.1 §4.1 매트릭스 추가.

### §4.2 Reviewer-only 단축 가능성 (대안 (b)) 한계

54 entry (γ-c) 채택 발효 cycle = 1-agent 직접 합의로 발효 (5/7 trigger 0/7 미발화 자체 검증). 본 (55 entry) cycle 차이:
- 54 entry = **결정 발효 답습 한정** (53 entry Reviewer 통합 권고 답습 → 채택 결정)
- 55 entry = **PASS 격상 *진입 권한 발효*** (MVP-2 PASS 발효 *직전 단계*, 큰 결정)

→ trigger 1 (큰 결정) 발화 차이 = 합의 형태 차이. (b) 부적격.

---

## §5 denyNonFastForwards 활성화 대안 + Layer evidence template 대안 (질문 3 + 2)

### §5.1 denyNonFastForwards 5 활성화 대안 (R-C-2 답습)

R-C-2 매트릭스 답습. 권고 = **(c) per-repo + (d) entrypoint script + Dockerfile 조합**.

### §5.2 PASS evidence template 3 대안 (R-C-3 답습)

R-C-3 매트릭스 답습. 권고 = **(i) Layer subsection 강제** (현 답습, (γ-c) 특화 의무 1 영구).

### §5.3 RT-PASS-1/2/3 검출 메커니즘 (N-C-2 답습)

N-C-2 답습. 권고:
- RT-PASS-1 = lint + runtime hook 조합
- RT-PASS-2 = lint (`grep -c '^## Layer [124] evidence'` ≥ 3)
- RT-PASS-3 = grep lint (`grep -E '(충실 답습|완전 답습)'` zero-match)

계산적 검증 우선 (CLAUDE.md §2 답습).

---

## §6 PASS 발효 시점 대안 평가 (질문 7)

### §6.1 3 시점 대안 (N-C-1 답습)

| 시점 | 의미 | trade-off |
|------|------|----------|
| (시점-α) 동시 | Layer 통합 PASS = MVP-2 PASS 발효 동시 | 1 cycle 효율 / Layer evidence 합산 risk ↑ |
| **(시점-β) 선행** | Layer 통합 PASS = MVP-2 PASS 선행 의무 | 단계적 / 32 entry 답습 패턴 / RT-γ-6 사전 평가 가능 |
| (시점-γ) 분리 | Layer 통합 PASS ≠ MVP-2 PASS | MVP-2 PASS 자격 검증 어려움 |

→ **(시점-β) 권고**. 32 entry MVP-1 PASS 답습 패턴 정합.

### §6.2 (시점-β) 발효 cycle 수 정량 (N-C-4 답습)

5 cycle 등가 (55 entry 포함):
1. 55 entry (본 cycle) = 진입 합의
2. (β) sub-수단 결정
3. 실 구현 sub-cycle
4. Layer 통합 PASS 발효 합의
5. MVP-2 PASS 발효 합의

24/32 entry MVP-1 cycle 수 답습 정합.

---

## §7 자기진단 (메타 편향 회피)

| # | 위험 | 본 응답 의 처리 |
|---|------|--------------|
| P-C-1 | Agent C 가 대안 탐색 강조 → 본 brief v1 채택 부정 방향 편향 | §0 = APPROVE WITH CONDITIONS (REVISE/REJECT 0) + §1 BLOCKING 3 = framing 보강 한정 (본 brief 채택 정합) |
| P-C-2 | 합의 형태 대안 평가 (b) audit-only 단축 = 53/54 entry 답습 일관성 ↑ → 본 brief (a) 권고 부정 편향 | §4.2 = trigger 1 (큰 결정) 발화 차이 명시 → (b) 부적격 정당화 |
| P-C-3 | PASS 시점 대안 평가 (시점-α/β/γ) = 본 brief §8 본문 영역 침입 risk | §6 = §8 답습 한정 (cycle 수 정량 매트릭스 추가만, 결정 ≠ 본 응답) + N-C-1/N-C-4 흡수 권고 한정 |
| P-C-4 | (γ-e/f/g) hybrid 대안 평가 자동 진입 = 영역 침입 | 본 응답 §0 + §3 NOTE-C-2 = 54 entry §0.3 #22 + 53 entry B-8 영구 답습 명시 (재평가 0) |
| P-C-5 | Agent C (Anthropic Claude Opus 4.7) = 53 entry Agent C 동일 model → cascade risk | brief §10 P-7 답습. 본 응답 = 54 entry §1.3 (γ-c) 특화 의무 4 + 53 entry 답습 cascade 정합성 검증 + cross-vendor 후속 (codex) 응답 통합 Reviewer 단계 의무 명시 |
| P-C-6 | denyNonFastForwards 5 대안 (a)~(e) 신규 식별 = brief §6.2 #1 자동 후속 실 구현 sub-cycle 진입 risk | §5.1 = 활성화 자체 ≠ 본 cycle (R-C-2 framing 보강 한정, 실 구현 = 별도 sub-cycle 답습) |
| P-C-7 | evidence template 3 대안 (i)/(ii)/(iii) = (γ-c) 특화 의무 1 재평가 risk | §5.2 = (i) 현 답습 권고 (재평가 0, (γ-c) 특화 의무 1 영구 답습 답습 충실) + (ii)/(iii) 부적격 근거 명시 |
| P-C-8 | 본 응답 작성자 = Agent C 단독 → 다른 Agent (A/B/codex) 응답 참조 위험 | 본 응답 §0 + 검토자 항목 명시: 병렬 독립 (다른 응답 미참조). Reviewer 단계 통합 의무 답습 |

---

**Agent C 응답 끝.**

**다음 단계 (Agent C 영역 외)**: Reviewer (검토 에이전트) 가 Agent A + Agent B + Agent C + 외부 LLM (codex) 4 응답 cross-comparison + 통합 합의 보고서 작성 → brief v1.1 1pass 흡수 → SESSION + INDEX commit + push (55 entry).
