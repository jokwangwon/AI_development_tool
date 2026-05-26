# Cross-vendor Blind 검토 의뢰 — Backlog #3 T3 영역 6 sub-영역 통합 진입 결정 사전 검토

> **이 문서를 통째로 ChatGPT (GPT-5.x), Gemini, 또는 다른 *비-Claude* vendor 강력한 LLM 에 붙여넣고 평가를 요청하십시오.** 첨부 자료 없이 본 문서만으로 평가 가능하도록 작성되었습니다.
>
> **본 의뢰의 *blind 강도* 는 가장 높습니다. 본 자료에는 다음이 *의도적으로 포함되지 않습니다*:**
> - ❌ 본 프로젝트의 내부 Agent A / B / C 분석 결과 (아직 풀 3+1 진입 전)
> - ❌ 본 프로젝트의 Reviewer 종합 결론
> - ❌ 의뢰자 (사용자) 가 원하는 결론 / 방향 / 선호
> - ❌ APPROVE 유도 표현 / 답안 제시 / 결론 시사
>
> 본 의뢰는 vendor 다양성 (cross-vendor) 을 통해 진정한 *제3자* 의 독립 판단을 확보하기 위함입니다. 응답은 `docs/external-review/2026-05-13-backlog3-t3-zone-review-response{,-gemini,-claude,-<vendor>}.md` 에 저장될 예정입니다.

**작성일**: 2026-05-13 (실제 작성 = 2026-05-14)
**대상 의뢰자**: ChatGPT (GPT-5.x) / Gemini / 다른 *비-Claude* vendor 1+ — cross-vendor blind
**의뢰 대상 brief**: `docs/phase0/backlog3-t3-zone-full-3plus1-brief.md` (commit `ad9a02d`, 828줄, DRAFT)

---

## 0. 검토 의뢰자의 입장 + 본 검토의 형식

### 0.1 검토 의뢰자

저는 1인 개발자로 "**아이디어를 던지면 AI 에이전트 (주로 Claude Code) 가 SDD + TDD 로 자동 개발하도록 설계된 메타-템플릿**" 을 만들고 있습니다. 본 프로젝트 자체는 그 템플릿이며, 새 아이디어가 생길 때마다 본 템플릿을 복사해 시작합니다.

본 프로젝트의 메인 작업 컨텍스트는 Claude (Anthropic) 입니다. 따라서 본 cross-vendor 의뢰는 *비-Claude vendor* 의 의견을 확보하는 것이 핵심 목적입니다.

### 0.2 본 검토의 형식

본 검토는 **3 Group × 6 질문 = 18 질문 묶음** 입니다. 그리고 마지막에 **종합 판정 1 질문** 이 추가되어 합산 **19 질문** 입니다. 각 질문에 독립적으로 근거 기반 판정을 요청합니다.

**3 Group 분할 답습** (본 prep brief 권고 — `ad9a02d` §4.1 (II) 답습):

- **Group α** — AR-3 + PC-4 T3 sub (enforcement / dev 환경 차단 layer)
- **Group β** — T-5 (β) + Tier-2/3 catalog 일반 (catalog source 정책)
- **Group γ** — C-5b ST-1 + Vault HSM ST-4 (secret source / Hermes upstream)

본 질문은 다음을 *묻지 않습니다*:
- ❌ 의뢰자가 무슨 답을 원하는지 (의뢰자는 답을 미리 제시하지 않음)
- ❌ 다른 LLM 이 어떤 답을 했는지 (본 자료는 다른 LLM 응답을 *포함하지 않음*)
- ❌ 내부 Agent 가 어떤 결론에 도달했는지 (아직 내부 풀 3+1 진입 전)

**본 의뢰자는 어느 판정도 사전에 선호하지 않습니다.** APPROVE 가 안전한 답이 아닙니다. BLOCK 도 안전한 답이 아닙니다. *근거에 의해 도출된 판정* 이 안전한 답입니다.

### 0.3 본 검토의 *메타* 목적

본 의뢰는 **풀 3+1 합의 *진입 전*** 의뢰입니다. 내부 Agent A / B / C 가 아직 분석하지 않은 시점입니다. 본 의뢰의 응답은 풀 3+1 합의의 *입력* 으로만 사용됩니다 — 자동 운영 적용 / Hermes PMO 격상 / ADR 본문 자동 갱신 모두 *불가* (§부록 B 답습).

본 의뢰는 Claude 패밀리 컨텍스트 자기참조 편향 통제를 위한 *blind* 의뢰입니다.

---

## 1. 시스템 목적 (요약)

### 1.1 프로젝트 정체성

- **이름**: AI Development Tool Template
- **사용자**: 1인 개발자 (동일 호스트, SPOF 의도적 수용 — ADR-012 §2.8 명시)
- **저장소**: 코드 0줄 (PoC 도구 ~17개 = 산출물 시제 한정), 약 75+ 마크다운 (헌법 + 12 ADR + 11 설계 문서 + 60+ 합의/외부검토 보고서 + 가이드 + Phase0 사양 + 세션 로그)
- **사용 방식**: 새 프로젝트 → 템플릿 복사 → Phase 0 (질문지) → Phase 1 (스택/에셋 합의) → Phase 2-3 (SDD → TDD)
- **메타-슬로건**: "에이전트에게 하라고 말하지 말고, 잘못하는 것이 *불가능*하게 만들어라."

### 1.2 핵심 방법론 (4축)

- **SDD** (Specification-Driven Development): 코드 변경 전 설계 문서 우선
- **TDD** (RED → GREEN → REFACTOR, 70% 커버리지 목표)
- **하네스 엔지니어링**: 7-Layer 피드백 루프 (CLAUDE.md / 검토 질문지 / PostToolUse / PreCommit / git pre-commit / CI / 3+1 합의 / Human review)
- **3+1 멀티에이전트 합의**: Agent A (구현) + Agent B (안전성) + Agent C (대안) → Reviewer 종합

### 1.3 권위 위계 (영구)

```
Constitution > ADR > SDD > Harness Gates > Hermes > Worker Agents
```

본 위계는 **ADR-011 §2.3** 에 영구 권위로 명시. **Hermes 는 시스템의 root of trust 가 아니라 검증 대상**.

### 1.4 영구 핵심 제약 5건 (5 영구 핵심 제약 답습)

1. **Hermes ≠ root of trust** — Hermes 는 검증 대상, root of trust 아님
2. **수단 ↔ 목적 분리** — 도구는 수단, 안전 결과는 목적 (ADR-011)
3. **메타포 강제 금지** — Hermes 메타포는 *권고* 한정, *강제* 금지
4. **단일 source-of-truth 보존** — catalog / 정책 / ADR 본문 등 1 출처
5. **Provider Liquidity 5-way** — 모델/구독 교체가 코드 변경 없이 가능 (적어도 5 vendor 답습)

### 1.5 T1 / T2 / T3 영역 분리 (ADR-011 §2.4 답습)

| 영역 | 정의 | 합의 형태 |
|----|----|--------|
| T1 | 자동 학습 — 사용자/AI 가 *자유롭게* 변경 가능 | 단축 / 자동 진입 |
| T2 | 정책 / 정적 검출 — 합의 후 변경 (Reviewer-only 단축 또는 풀 3+1) | 단축 또는 풀 3+1 |
| **T3** | **정책 변경 — 5 영구 핵심 제약 영향 / branch protection / Hermes upstream / Vault HSM / Tier-2/3 catalog 확장 / dev 환경 강제** | **풀 3+1 + 외부 LLM 1+ cross-vendor blind + 사용자 명시 *의무*** |

---

## 2. Backlog #3 T3 영역 범위

### 2.1 현 시점 정의

본 의뢰의 대상 = **Backlog #3 T3 영역** = T1 / T2 / T3 中 *T3 영역* 의 6 sub-영역 통합 정비 — Backlog #1 / #2 / #4 / #6 / #7 와 분리된 별도 영역.

### 2.2 7 Backlog 中 본 의뢰의 위치

| Backlog # | 영역 | 현 상태 | 본 의뢰와의 관계 |
|---------|------|------|--------------|
| #1 | GP-3 1.5차 보강 (Secret Hygiene) — S-3 detect-secrets 부분 / ST-2 inotify sidecar | Deferred | 별도 영역 (ST-2 답습 의존) |
| #2 | GP-5 1.5차 보강 (Provider Adapter Enforcement) — T-1/T-3/T-4 단독 + T-5 강화 + AR-3 + PC-4 T2 sub | PC-4 T2 sub Partially Satisfied (`78483c5`) / 잔여 5 Deferred (`8ba5182`) — AR-3 + T-5 (β) Backlog #3 이관 명시 | AR-3 + T-5 (β) **본 의뢰 이관 대상** |
| **#3** | **T3 영역 — AR-2 / Vault HSM / Tier-2/3 / PC-4 T3 sub / C-5b ST-1** | DRAFT brief 작성 완료 (`ad9a02d`) | ✅ **본 의뢰 영역** |
| #4 | P1 v2 facade MVP (G5-4 — facade 실 본문) | Deferred | 별도 영역 |
| #5 | ADR-012 §2.2 `event` enum 정식 등록 | Deferred | 별도 합의 영역 |
| #6 | Runtime enforcement / CI-hook implementation | Implementation Entry 우선순위 1 (`1eab814`) | 별도 영역 |
| #7 | Operational Readiness parity check | MVP-6 영역 | 본 의뢰 Group γ ST-4 cross-reference |

### 2.3 이미 완료된 PoC 시제 답습 (본 의뢰 전제 — 변경 0건)

| PoC 그룹 | 영역 | 시제 |
|--------|-----|-----|
| Group A 1차 | GP-5 Layer 1a — direct provider SDK import 정적 검출 (AST 5 패턴) | `tools/provider_import_scanner.py` |
| Group A 2차 | GP-5 Layer 1b — transitive import 정적 그래프 | `.importlinter` + `import-linter` (PoC 채택) |
| Group A 3차 | GP-5 Layer 1c — URL endpoint + model name (Tier-1 URL 10 + Model 19 답습) | `tools/provider_url_scanner.py` |
| Group D | GP-3 — secret 검출 (R-4.1 Tier-1 42 catalog 답습) | `tools/secret_scanner.py` |
| Group F | G2 GP-6 Memory/Skill migration feasibility | `tools/memory_skill_roundtrip.py` |
| Group C / 후속 / 후속 후속 | G4 Evidence Ledger 보호 5 Layer (정적 검출 시제 한정) | `canonical_json.py` / `jsonl_hash_chain.py` / `history_anchor_verifier.py` / `rewrite_defense_check.py` |
| Group E | G2 GP-4 External Input Validation + G4 Memory/Skill schema validation | `tools/schema_validator.py` |
| Group G | G3 Skill escalation + G4 Memory/Skill boundary | `tools/boundary_guard.py` |

**본 의뢰 전제 답습**: 위 8 PoC 그룹 모두 `tools/*.py` 본문 변경 0건 + CI workflow 본문 변경 0건 + 도구 신설 0건 — *시제 검토* 한정.

### 2.4 현 MVP 단계

| 단계 | 상태 | 비고 |
|----|----|----|
| MVP-0 (PoC 시제) | ✅ 완료 (Phase 0 답습) | Group A/B/C/D/E/F/G + Group C 후속/후속 후속 |
| MVP-1 Design Gate PASS | ✅ 발효 | GP-3 + GP-5 진입 합의 완료 |
| **MVP-1 Implementation Entry** | ✅ READY (`1eab814`) | Backlog #6 우선순위 1 — Runtime + CI-hook |
| MVP-1 Implementation Evidence PASS | ⏳ 미발효 | Backlog #6 진입 + 실 evidence 후 별도 합의 |
| MVP-2 | ⏳ Implementation Evidence PASS 후 | — |
| MVP-3 | ⏳ Layer 2 runtime block / 의미적 lock-in (G4 §4.6) | — |
| MVP-6 | ⏳ Operational Readiness (Layer E) — Backlog #7 | Vault HSM ST-4 진입 시점 |
| Hermes PMO 격상 (Layer F) | ⏳ 미선언 | MVP-6 + 외부 LLM 2 또는 1+사람 리뷰 의무 |

---

## 3. Backlog #3 6 sub-영역 설명

### 3.1 (1) AR-3 (AR-1 + AR-2 통합 — branch protection rule)

| 영역 | 설명 |
|----|----|
| 정의 | AR-1 (CI step fail-closed — 현 PoC + Layer B 본문 채택, T2 영역) + AR-2 (GitHub branch protection rule 강제 — CODEOWNERS / required check / commit signing / merge restriction, T3 영역) 통합 |
| 현 상태 | AR-1 = Layer B `f40423f` 본문 채택 / AR-2 = Deferred / AR-3 = `8ba5182` Backlog #3 이관 명시 |
| 책무 영역 | enforcement layer (GitHub repo 정책 / CI step) |
| T3 진입 속성 | GitHub repo 정책 변경 (branch protection / CODEOWNERS / required check) ✅ HIGH / Hermes upstream 변경 0건 |

### 3.2 (2) T-5 (β) — provider URL/model name Tier-2/3 catalog 확장 (GP-5)

| 영역 | 설명 |
|----|----|
| 정의 | Group A 3차 `tools/provider_url_scanner.py` Tier-1 URL catalog 10 (Anthropic/OpenAI/Azure-OpenAI/Google-AI/Replicate/Perplexity/Cohere/HuggingFace/Together/OpenRouter) + Tier-1 Model catalog 19 (Anthropic 5 + OpenAI 5 + Google 3 + Meta 3 + Mistral 3) 를 Tier-2 (베타/소규모) + Tier-3 (legacy/비주류) 까지 확장 |
| 현 상태 | Tier-1 답습 완결 / Tier-2/3 = 자동 확장 0건 (사용자 명시 답습) |
| 책무 영역 | catalog source 정책 (GP-5 specific subset) |
| T3 진입 속성 | catalog 본문 변경 (T3 정책) ✅ HIGH / Provider Liquidity 영향 ⚠️ MEDIUM / FP 폭증 위험 ⚠️ HIGH |

### 3.3 (3) PC-4 T3 sub — `pre-commit install` 의무화 + dev 환경 강제

| 영역 | 설명 |
|----|----|
| 정의 | PC-4 (PC-1 + PC-3 병행 — Defense in depth) 中 T3 sub = `pre-commit install` 의무화 / `default_install_hook_types` / `fail_fast` / dev 환경 강제 / `commit-msg` / `pre-push` stage 도입 |
| 현 상태 | PC-4 T2 sub (`.pre-commit-config.yaml` + 6 hook + opt-in) = Partially Satisfied (`78483c5`) / PC-4 T3 sub = Deferred (Backlog #3 T3 영역) |
| 책무 영역 | dev 환경 정책 (ADR-011 §2.4 답습) |
| T3 진입 속성 | dev 환경 *정책* 변경 ✅ HIGH / hook stage 변경 ⚠️ HIGH / 개발자 우회 (`--no-verify`) ⚠️ HIGH |

### 3.4 (4) C-5b ST-1 — Hermes upstream Dockerfile entrypoint stat chmod 600 강제

| 영역 | 설명 |
|----|----|
| 정의 | Hermes upstream Dockerfile entrypoint 시점에 `~/.hermes/auth.json` (또는 동등) 의 `stat` 검증 (chmod 600 강제) — 644 등 위반 시 컨테이너 정지 |
| 현 상태 | C-5b (ST-1) = Deferred (`78483c5` 답습) — Backlog #3 T3 영역 / ST-3 (docker secret) = Layer B 본문 채택 / ST-2 (inotify sidecar) = Backlog #1 영역 / ST-5 (Defense in depth 통합) = MVP-2 이후 영역 |
| 책무 영역 | secret source / Hermes upstream (file system perm 영역) |
| T3 진입 속성 | Hermes upstream Dockerfile *본문* 변경 ✅ HIGH / Hermes ≠ root of trust 검토 의무 ✅ HIGH / Hermes upstream PR 의무 ⚠️ HIGH / sidecar (ST-2) 와 책무 분담 결정 의무 ⚠️ MEDIUM |

### 3.5 (5) Vault HSM ST-4 — ADR-010 통합

| 영역 | 설명 |
|----|----|
| 정의 | HashiCorp Vault + HSM (Hardware Security Module) 통합 — Hermes 가 Vault 클라이언트 호출, secret 저장 = 외부 HSM (Multi-host 환경 권고) |
| 현 상태 | ST-4 = Deferred (`78483c5` 답습) — Operational Readiness 영역 (MVP-6) cross-reference |
| 책무 영역 | secret source (외부 HSM) / Multi-host 인프라 |
| T3 진입 속성 | ADR-010 §X 진입 합의 의무 ✅ HIGH / Multi-host 인프라 의무 ✅ HIGH / 운영 비용 高 ⚠️ HIGH / 단일 source-of-truth 영향 ⚠️ MEDIUM (HSM 단일화 시 ↑) |

### 3.6 (6) Tier-2/3 catalog 자동 확장 *가능성 일반* (GP-3 + GP-5 통합 정책)

| 영역 | 설명 |
|----|----|
| 정의 | GP-3 R-4.1 Tier-1 42 catalog (45 patterns 답습) + GP-5 URL Tier-1 10 + Model Tier-1 19 → Tier-2 + Tier-3 자동 확장 가능성 *일반 정책* 결정 |
| 현 상태 | Tier-2/3 자동 확장 0건 (`78483c5` + `8ba5182` 답습) |
| 책무 영역 | catalog source 정책 일반 (GP-3 + GP-5 + 미래 catalog) |
| T3 진입 속성 | catalog *정책* 변경 ✅ HIGH / FP/FN 폭증 위험 ⚠️ HIGH / Implementation Evidence PASS 의존 ⚠️ HIGH (실 src/ 도입 후 measurement baseline 의무) |

### 3.7 (2) T-5 (β) 와 (6) Tier-2/3 일반 의 책무 분리

본 의뢰는 (2) T-5 (β) 와 (6) Tier-2/3 일반 을 **별도** sub-영역으로 다룹니다 — 책무 분리:

- (2) T-5 (β) = **GP-5 specific subset** (provider URL/model name Tier-2/3 vendor 추가 결정)
- (6) Tier-2/3 일반 = **GP-3 + GP-5 + 미래 catalog 일반 정책** (catalog *정책* / *형식* / *프로세스* 결정)

본 의뢰는 (2) 와 (6) 을 **Group β** 로 통합 검토 — subset / superset 관계 + 동시 결정 권고.

---

## 4. 3 그룹 분리 권고

### 4.1 그룹 분리 권고 (본 prep brief `ad9a02d` §4.1 (II) 답습)

본 의뢰자는 6 sub-영역 중 결합 위험 / 책무 중첩 / 분리 가능성 매트릭스 (15 페어 中 11 ✅ 분리 + 3 ⚠️ 부분 분리 + 0 분리 어려움) 답습 후 다음 3 그룹 분리를 권고합니다:

```
Group α  =  (1) AR-3 + (3) PC-4 T3 sub
            영역 : enforcement / dev 환경 차단
            결합 : Defense in depth ('--no-verify' 우회 차단 결합)

Group β  =  (2) T-5 (β) + (6) Tier-2/3 일반
            영역 : catalog source 정책
            결합 : subset (T-5 β) / superset (Tier-2/3 일반) 관계

Group γ  =  (4) C-5b ST-1 + (5) Vault HSM ST-4
            영역 : secret source / Hermes upstream
            결합 : ST-1 (file system perm) + ST-4 (HSM secret source)
                  책무 분담 결정 의무 (Defense in depth vs
                  단일 source-of-truth)
```

본 권고 = **본 의뢰자가 사전 분석한 책무 영역 분배**. 외부 LLM 의뢰자에게는 본 권고가 *적절한지* 판단을 요청합니다 (§5 그룹별 위험 + §6 핵심 질문 답습).

### 4.2 그룹 분리 대안 옵션 (참고)

| 옵션 | 단위 | 합의 부담 |
|-----|----|--------|
| (I) 6 sub-영역 *단일 통합* (1 합의) | 1 합의 | 매우 高 |
| **(II) 3 그룹 분리 (Group α / β / γ, 3 합의)** | 3 합의 | **中 — 본 권고** |
| (III) 6 sub-영역 *각각* 분리 (6 합의) | 6 합의 | 低-中 (각 단독) — 결합 위험 분석 분리 부담 |
| (IV) Group α 통합 + 나머지 4 분리 (5 합의) | 5 합의 | 中 |
| (V) Group α + β 통합 + Group γ 분리 (다른 그룹화) | 3 합의 | 中 |
| (VI) 책무 영역 별 분리 (enforcement / catalog / dev 환경 / Hermes upstream / HSM) | 5 합의 | 中 |

본 의뢰의 핵심 질문 #19 (§6.4) 에서 본 그룹 분리의 적절성 판단을 요청합니다.

---

## 5. 각 그룹별 위험

### 5.1 Group α (AR-3 + PC-4 T3 sub) 위험

#### 5.1.1 위험 매트릭스

| # | 위험 | 발화 |
|---|----|------|
| 1 | branch protection rule 변경 = GitHub repo 정책 변경 = 사용자 명시 결정 의무 (T3 영역) | ✅ HIGH |
| 2 | dev 환경 강제 = 개발자 friction 폭증 / 1인 개발자 환경 부적합 위험 | ⚠️ HIGH |
| 3 | `--no-verify` 우회 = PC-4 T3 sub 단독 무력화 → AR-3 branch protection 필수 | ✅ HIGH |
| 4 | fork PR / external contributor 정책 = `pull_request_target` 위험 / fork PR secret 접근 위험 | ⚠️ MEDIUM |
| 5 | commit signing key 관리 = GPG / SSH signing 운영 비용 / key revocation 정책 | ⚠️ MEDIUM |
| 6 | CODEOWNERS 매트릭스 충돌 = 1인 개발자 환경에서 CODEOWNERS 의미 약화 | ⚠️ MEDIUM |
| 7 | hook stage 충돌 (`pre-commit` + `commit-msg` + `pre-push`) = hook 실행 시간 폭증 | ⚠️ LOW |
| 8 | Hermes-originated commit auto-reject (G3 §2.2 #20 답습) 통합 시 책무 영역 확장 | ⚠️ MEDIUM |

#### 5.1.2 5 영구 핵심 제약 영향

| 제약 | 영향 |
|----|----|
| Hermes ≠ root of trust | ❌ 영향 없음 (GitHub repo / dev 환경 영역) |
| 수단-목적 분리 | ⚠️ MEDIUM — enforcement layer 가 *목적* (안전 결과) 인지 *수단* (특정 도구) 인지 검토 의무 |
| 메타포 강제 금지 | ❌ 영향 없음 |
| 단일 source-of-truth | ⚠️ LOW — AR-3 + PC-4 T3 sub 통합 시 enforcement 정책 source 가 분산 위험 |
| Provider Liquidity 5-way | ❌ 영향 없음 (vendor 의존 0건) |

### 5.2 Group β (T-5 (β) + Tier-2/3 일반) 위험

#### 5.2.1 위험 매트릭스

| # | 위험 | 발화 |
|---|----|------|
| 1 | Tier-2/3 catalog 확장 = Tier-1 보존 정책 변경 = T3 영역 정책 결정 | ✅ HIGH |
| 2 | **Provider Liquidity 5-way 영향** — Tier-2/3 vendor 추가/제거 시 5-way 책무 영향 | ⚠️ HIGH |
| 3 | FP 폭증 위험 — catalog 확장 = pattern 충돌 + 정상 코드 false positive ↑ | ⚠️ HIGH |
| 4 | FN cover — Tier-2/3 vendor 미커버 시 lock-in 위험 잔존 | ⚠️ MEDIUM |
| 5 | 외부 catalog source 의존 (LiteLLM vendor list 자동 동기화 등) = supply chain 위험 | ⚠️ HIGH |
| 6 | vendor 이름 변경 / deprecated vendor / vendor merge / vendor split 대응 정책 | ⚠️ MEDIUM |
| 7 | catalog 본문 *형식* 분리 (yaml/json/도구 내장) = 단일 source-of-truth 영향 | ⚠️ MEDIUM |
| 8 | **provider lock-in 강화 위험 *역효과*** — Tier-2/3 catalog 차단 강화 시 신규 vendor 채택 부담 ↑ → *Provider Liquidity 5-way 약화 가능성* | ⚠️ **HIGH** (사용자 명시 위험 영역) |
| 9 | Implementation Evidence PASS 의존 — 실 src/ 도입 후 measurement baseline 의무 | ⚠️ HIGH |
| 10 | Group D §2.1 (D) 답습 — gitleaks default ruleset Tier-2/3 자동 확장 위험 회피 | ✅ 답습 |

#### 5.2.2 5 영구 핵심 제약 영향

| 제약 | 영향 |
|----|----|
| Hermes ≠ root of trust | ❌ 영향 없음 |
| 수단-목적 분리 | ⚠️ MEDIUM — catalog 차단 = 수단, 안전 결과 = 목적 (수단 변경 시 목적 보존 검증 의무) |
| 메타포 강제 금지 | ❌ 영향 없음 |
| 단일 source-of-truth | ⚠️ HIGH — catalog 본문 형식 분리 / 자동 동기화 도입 시 source 분산 위험 |
| Provider Liquidity 5-way | ⚠️ **HIGH** — Tier-2/3 catalog 차단 강화 = 신규 vendor 채택 부담 ↑ = 5-way 약화 위험 |

### 5.3 Group γ (C-5b ST-1 + Vault HSM ST-4) 위험

#### 5.3.1 위험 매트릭스

| # | 위험 | 발화 |
|---|----|------|
| 1 | **Hermes upstream Dockerfile 변경** = 책무 경계 변경 = Hermes ≠ root of trust 검토 의무 | ✅ **HIGH** |
| 2 | Hermes upstream PR 절차 = Hermes maintainer 협의 / fork+downstream patch 대안 | ⚠️ HIGH |
| 3 | ST-1 (file system perm) + ST-4 (HSM secret source) **책무 중첩** | ⚠️ HIGH |
| 4 | Vault HSM 인프라 운영 비용 高 = 1인 개발자 환경 부적합 | ⚠️ **HIGH** |
| 5 | ADR-010 §X 진입 합의 = ADR 본문 변경 = 별도 영역 (별도 합의 의무) | ✅ HIGH |
| 6 | Multi-host 인프라 = single-host 환경에서 의미 약화 | ⚠️ HIGH |
| 7 | Operational Readiness PASS (Backlog #7 / MVP-6) **경계** — Vault HSM ST-4 진입 시점이 MVP-6 영역 cross-reference | ⚠️ **HIGH** (사용자 명시 위험 영역) |
| 8 | **Hermes PMO 격상 경계** — Hermes upstream 변경 = Hermes PMO 격상 시 의무 영역 cross-reference | ⚠️ **HIGH** (사용자 명시 위험 영역) |
| 9 | ST-2 inotify sidecar (Backlog #1) 와 책무 분담 결정 의무 | ⚠️ MEDIUM |
| 10 | ST-3 docker secret (Layer B 본문 채택) 와 책무 분담 결정 의무 | ⚠️ MEDIUM |
| 11 | HSM SPOF / Vault inaccessible 시 fallback 정책 | ⚠️ MEDIUM |
| 12 | HSM key 관리 / Vault audit log 통합 | ⚠️ MEDIUM |

#### 5.3.2 5 영구 핵심 제약 영향

| 제약 | 영향 |
|----|----|
| Hermes ≠ root of trust | ✅ **HIGH** — Hermes upstream 변경 = root of trust 영역 침범 위험 검토 의무 |
| 수단-목적 분리 | ⚠️ HIGH — ST-1/ST-4 = 수단, 안전 결과 = 목적 (수단 변경 시 목적 보존 검증) |
| 메타포 강제 금지 | ❌ 영향 없음 |
| 단일 source-of-truth | ⚠️ MEDIUM — ST-4 도입 시 secret source 가 Vault HSM 단일화 → 정합성 ↑ |
| Provider Liquidity 5-way | ❌ 영향 없음 (secret source 영역) |

---

## 6. 풀 3+1 + 외부 LLM 1+ 필요성

### 6.1 풀 3+1 의무 발화 트리거 (7/7 매트릭스)

| # | 트리거 | 본 6 sub-영역 발화 |
|---|----|--------------|
| 1 | 9 sub-수단 외 수단 *재결정* | ⚠️ 부분 — (2) T-5 (β) + (4) ST-1 + (5) ST-4 = 추가 수단 결정 |
| 2 | **T3 영역 자동 진입** | ✅ **HIGH (BLOCKING)** — 본 6 sub-영역 *모두* T3 영역 |
| 3 | 사용자 명시 3 결정 (α/ii/(가)) *재변경* | ❌ 0건 (PC-4 T2 sub Cycle 4 답습 한정) |
| 4 | Provider Liquidity 5-way 약화 | ⚠️ HIGH — (2) Tier-2/3 vendor 추가 시 / (5) Vault HSM 도입 시 |
| 5 | 5 영구 핵심 제약 약화 | ⚠️ **HIGH** — (4) C-5b ST-1 = Hermes ≠ root of trust / (5) Vault HSM = 단일 source-of-truth |
| 6 | **MVP-1 PASS 재선언 / Layer E (Operational Readiness PASS) / Layer F (Hermes PMO 격상)** | ❌ 0건 (사용자 명시 7 금지 답습) |
| 7 | **외부 LLM cross-vendor blind 없는 T3 결정** | ✅ **HIGH** — 본 의뢰의 *발생 사유 자체* |

**합산**: 7/7 中 트리거 #2 + #5 + #7 = HIGH (BLOCKING) + 부분 #1 + #4 → **풀 3+1 + 외부 LLM 1+ cross-vendor blind + 사용자 명시 의무 확정**.

### 6.2 외부 LLM 1+ cross-vendor blind 의무성

본 의뢰는 다음 조건이 모두 충족되어 *발생*:

- T3 영역 진입 (Tier-2/3 catalog / Hermes upstream / branch protection / Vault HSM / dev 환경 강제) — `ADR-011 §2.4` 답습
- Provider Liquidity 5-way 보존 책무 (vendor 다양성 = cross-vendor 평가 의무)
- 5 영구 핵심 제약 보존 책무 (Hermes ≠ root of trust 등)
- Claude 패밀리 컨텍스트 자기참조 편향 통제 (cross-vendor 응답이 *제3자* 의 독립 판단)

본 의뢰자는 **비-Claude vendor 1+** 의 응답을 의무화합니다. 권고 = GPT (OpenAI) + Gemini (Google) 2 vendor — C-14 cross-vendor 답습.

### 6.3 응답 회수 후 처리

| 응답 시나리오 | 처리 |
|----------|----|
| 응답 1건 + 단순 검토 → 별 issue 없음 | Reviewer-only 단축 합의 *부적격* (T3 영역 의무) — 풀 3+1 의무 |
| 응답 1건 이상 BLOCK 또는 PARTIAL | 풀 3+1 + 외부 LLM 의무 — 그룹별 결함 수정 후 재의뢰 또는 재합의 |
| 응답 1건 이상 APPROVE WITH CONDITIONS | 조건 흡수 + 풀 3+1 합의 진입 |

---

## 7. 본 의뢰의 *19 질문* (검토 의뢰)

### 7.1 Group α 질문 (AR-3 + PC-4 T3 sub) — 6 질문

본 그룹 = enforcement / dev 환경 차단 layer. branch protection rule 변경 / `pre-commit install` 의무화 / `--no-verify` 우회 차단 등 결정.

**Q1**. AR-3 (CI step fail-closed + GitHub branch protection rule 통합) 의 7 결정 영역 — (a) CODEOWNERS only / (b) required status check only / (c) commit signing only / (d) merge restriction only / (e) (a)+(b) 통합 / (f) (a)+(b)+(c) 통합 / (g) (a)+(b)+(c)+(d) 통합 — 中 어느 옵션이 (i) Provider Liquidity 5-way 보존 (ii) Hermes ≠ root of trust 보존 (iii) 우회 차단 효과 (iv) 1인 개발자 운영 부담 측면에서 최선인가? 근거는?

**Q2**. PC-4 T3 sub (`pre-commit install` 의무화 + dev 환경 강제) 의 6 결정 영역 — `pre-commit install` 시점 / `default_install_hook_types` / `fail_fast` / README 강제 install / `--no-verify` 차단 / `minimum_pre_commit_version` — 中 (i) 개발자 friction 최소화 (ii) 우회 가능성 최소화 측면에서 최선 옵션 조합은? 근거는?

**Q3**. AR-3 × PC-4 T3 sub 결합 (Defense in depth) 시 `--no-verify` 우회 차단 효과 평가 — 결합 효과 / 한계 / 우회 잔존 가능성? branch protection 단독 / pre-commit 단독 / 결합 中 우회 차단 가장 강한 형태는?

**Q4**. 외부 contributor / fork PR 정책 — `pull_request_target` 도입 (workflow) vs fork PR 자동 차단 (T3) vs default 정책 유지 (`secrets` = fork PR 자동 차단 답습) 中 1인 개발자 환경에 최선인 옵션은? 근거는?

**Q5**. commit signing 의무화 시점 — MVP-1 1.5차 (현 시점 진입) / Operational Readiness 발효 시 (MVP-6) / Hermes PMO 격상 시 (MVP-6 + 외부 LLM 의무) 中 권고는? 1인 개발자 환경에서 GPG/SSH signing 운영 비용 / key revocation 정책 영향은?

**Q6**. 본 Group α 합의가 *진입 부적합* 인 시점 또는 *차단 의무* 인 영역이 있는가? 예: Backlog #6 (Runtime + CI-hook implementation) 미진입 시 진입 부적합 / Implementation Evidence PASS 발효 후 권고 / 1인 개발자 환경에서 PC-4 T3 sub 부적합 등.

### 7.2 Group β 질문 (T-5 (β) + Tier-2/3 일반) — 6 질문

본 그룹 = catalog source 정책. provider URL/model name Tier-2/3 catalog 확장 / GP-3 R-4.1 Tier-1 42 catalog 확장 / catalog 본문 형식 / 자동 동기화 정책 결정.

**Q7**. Tier-2/3 catalog 자동 확장 *정책 일반* 의 6 결정 영역 — Tier 정의 기준 / 확장 프로세스 / 본문 형식 (yaml/json/도구 내장) / 자동 동기화 / FP/FN mitigation / Implementation Evidence PASS 의존 — 中 (i) FP/FN 균형 (ii) catalog 유지 부담 (iii) Provider Liquidity 보존 측면에서 최선 옵션 조합은? 근거는?

**Q8**. T-5 (β) (provider URL Tier-1 10 / Model Tier-1 19 → Tier-2/3 확장) 의 6 결정 영역 — Tier 분류 기준 / Tier-2 URL 확장 범위 (5/10/0 vendor) / Tier-3 URL / Model Tier-2 catalog / catalog 본문 형식 / FP 폭증 mitigation — 中 권고 vendor catalog 확장 범위는? Tier-2 에 추가하기 적합한 vendor 후보 (예: Mistral / AI21 / Inflection / Aleph Alpha / Stability)? Tier-3 도입 보류가 권고되는가?

**Q9**. LiteLLM vendor list 자동 동기화 vs 자체 catalog 유지 中 권고는? LiteLLM 의존 시 supply chain 위험 / vendor revocation 정책 / vendor 이름 변경 대응? Provider Liquidity 5-way 답습 (모델/구독 교체 = 코드 변경 없이 가능) 영향은?

**Q10**. **provider lock-in 강화 위험 *역효과*** — Tier-2/3 catalog 차단 강화 시 신규 vendor 채택 부담 ↑ → Provider Liquidity 5-way *약화* 가능성. 본 위험은 실재하는가? 어느 강도? 어떤 완화 방법이 있는가? 차단 강도 vs Provider Liquidity 보존 트레이드오프는?

**Q11**. Tier-2/3 도입 시 GP-3 R-4.1 42 catalog 확장 정책 / GP-5 URL/Model 확장 정책 *분리* vs *통합* 中 권고는? 양쪽이 같은 정책 frame 으로 다뤄야 하는가? 별도 frame 이 필요한가? Implementation Evidence PASS 의존 시점 — MVP-1 1.5차 진입 (Evidence baseline 없이) vs MVP-2 이후 中 권고는?

**Q12**. 본 Group β 합의가 *진입 부적합* 인 시점 또는 *차단 의무* 인 영역이 있는가? 예: Implementation Evidence PASS 미발효 시 진입 부적합 / 1인 개발자 환경에서 Tier-2/3 도입 미권고 / Tier-1 보존 권고 등.

### 7.3 Group γ 질문 (C-5b ST-1 + Vault HSM ST-4) — 6 질문

본 그룹 = secret source / Hermes upstream. Hermes upstream Dockerfile 변경 / Vault HSM 통합 / Multi-host 인프라 결정.

**Q13**. C-5b ST-1 (Hermes upstream Dockerfile entrypoint stat chmod 600 강제) 의 6 결정 영역 — ST-1 진입 시점 / Hermes upstream PR 절차 / chmod 강제 형태 / 위반 시 동작 / ST-2/ST-3 와 통합 / ST-4 와 책무 분담 — 中 (i) Hermes ≠ root of trust 보존 (ii) Hermes upstream 변경 최소화 (iii) 1인 개발자 운영 부담 측면에서 최선 옵션 조합은?

**Q14**. Vault HSM ST-4 (ADR-010 통합) 의 6 결정 영역 — ST-4 진입 시점 / Vault 인프라 형태 / Vault client 통합 방식 / ADR-010 §X 본문 형태 / 다른 ST 와 통합 정책 / Multi-host 전환 시점 — 中 (i) Multi-host 인프라 부담 (ii) 운영 비용 (iii) 단일 source-of-truth 보존 측면에서 최선 옵션 조합은? 1인 개발자 single-host 환경에서 Vault HSM 의 의미는?

**Q15**. ST-1 (file system perm) + ST-2 (inotify sidecar) + ST-3 (docker secret) + ST-4 (Vault HSM) 통합 정책 — Defense in depth (전체 통합) vs 단일 source-of-truth (ST-4 단독) 트레이드오프 中 권고는? 책무 중첩 vs 책무 분담 결정?

**Q16**. ST-4 진입 시점 — MVP-2 (조기 진입) / MVP-6 Operational Readiness 발효 시 (현 권고) / Hermes PMO 격상 후 中 권고는? 운영 비용 高 / Multi-host 인프라 부담 / single-host SPOF 의도적 수용 (ADR-012 §2.8 답습) 트레이드오프는?

**Q17**. **Hermes upstream 변경 *경계* vs Hermes PMO 격상 *경계*** — C-5b ST-1 진입 (Hermes upstream Dockerfile 변경) 이 Hermes PMO 격상 *전* / *후* / *동시* 中 어느 시점이 적합한가? Hermes ≠ root of trust 보존 영향? **Hermes upstream 변경이 root of trust 영역 침범 위험을 발생시키는가?** 어떤 안전장치가 의무인가?

**Q18**. **Operational Readiness PASS 경계** — Vault HSM ST-4 진입은 Operational Readiness PASS (Backlog #7 / MVP-6) *전* / *후* / *동시* 中 어느 시점이 적합한가? Multi-host 전환 시점은? 1인 개발자 환경에서 Operational Readiness PASS 의 의미는 (현재 single-host SPOF 의도적 수용)?

### 7.4 종합 판정 질문 — 1 질문 (#19)

**Q19**. 위 18 질문 종합 시, 본 시점 Backlog #3 T3 영역 *진입 결정* 에 대한 최종 판정은?

- (A) **APPROVE — 3 그룹 동시 진입 권고** (Group α + β + γ 모두 풀 3+1 진입 가능)
- (B) **APPROVE WITH CONDITIONS** — 특정 조건 (예: Backlog #6 우선 진입 / Implementation Evidence PASS 발효 후 / 외부 LLM 응답 추가 회수 등) 충족 시 진입 가능
- (C) **PARTIAL** — 일부 그룹 (Group α 또는 β) 만 진입 가능, 나머지 (Group γ — 특히 Vault HSM ST-4) 는 별도 시점 권고
- (D) **BLOCK** — 본 시점 진입 부적합 (예: 결함 수정 / 추가 답습 / Operational Readiness PASS 발효 의무 등 시점 결함)

**판정 근거 + 우선순위 권고**:
- Group α / β / γ 中 어느 그룹 *우선* 진입?
- 본 prep brief `ad9a02d` 가 권고한 우선순위 (α → β → γ) 가 적절한가? 다른 우선순위 권고?
- 3 그룹 분리 vs 다른 그룹화 (옵션 I / III / IV / V / VI — §4.2 답습) 中 적절한가?
- 본 prep brief 의 결함 / 누락 / 추가 검토 필요 영역?

---

## 8. 금지 사항 (사용자 명시 답습)

본 외부 LLM 검토 의뢰의 응답 / 결론은 **풀 3+1 합의의 *입력* 으로만 사용** 됩니다. 다음은 자동으로 발생하지 않습니다 (사용자 명시 결정 의무 영역):

### 8.1 본 의뢰 응답의 *영원 격리* (§부록 B 답습)

| 영역 | 자동 발생 여부 |
|----|----|
| 풀 3+1 합의 보고서 *작성* | ❌ 자동 0건 (응답 회수 후 별도 단계, 사용자 명시 결정) |
| **T3 영역 실제 진입** | ❌ 자동 0건 (응답 자체 = 입력 한정) |
| **branch protection rule 변경** | ❌ 자동 0건 (실 GitHub repo 정책 변경 0건) |
| **dev 환경 강제** (`pre-commit install` 의무화 / `.git/hooks` 자동 install) | ❌ 자동 0건 |
| **Hermes upstream Dockerfile 변경** (entrypoint stat / chmod / image 빌드) | ❌ 자동 0건 |
| **Vault HSM 구현** (실 Vault 클라이언트 / 실 HSM 환경 / ADR-010 §X 본문 변경) | ❌ 자동 0건 |
| **Tier-2/3 catalog 본문 확장** (URL 10 / Model 19 / R-4.1 42 보존) | ❌ 자동 0건 |
| **Operational Readiness PASS (Layer E) 선언** | ❌ 자동 0건 (MVP-6 + Backlog #7 영역) |
| **Hermes PMO 격상 (Layer F) 선언** | ❌ 자동 0건 (MVP-6 + 외부 LLM 2 또는 1+사람 리뷰 영역) |
| **외부 LLM 응답 없는 상태에서 PASS 선언** | ❌ 자동 0건 |
| ADR 본문 자동 갱신 (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012) | ❌ 자동 0건 |
| Implementation Evidence PASS 자동 발효 | ❌ 자동 0건 |
| MVP-1 PASS *재선언* | ❌ 자동 0건 (Layer D `210c98f` APPROVE WITH CONDITIONS 그대로 유지) |
| MVP-2 자동 진입 | ❌ 자동 0건 |

### 8.2 본 의뢰 응답이 *해서는 안 되는* 것 (외부 LLM 의뢰자 명시 답습)

응답에서 다음은 *발생하지 않아야* 합니다:

- ❌ 의뢰자가 원할 것 같은 답 추측 (`APPROVE 가 사용자 의도일 가능성이 높습니다` 등 추측 표현)
- ❌ 다른 LLM 의 답을 시사하는 표현 (`다른 vendor 와 일치할 것입니다` 등)
- ❌ 내부 Agent 결론을 시사하는 표현 (`Agent A 가 동의할 것입니다` 등)
- ❌ APPROVE 유도 / BLOCK 유도 / 결론 시사
- ❌ 의뢰 자료에 포함되지 않은 *증거를 만들어내는* 행위

응답에서 *발생해야* 합니다:

- ✅ 19 질문 각각에 대한 *근거 기반* 판정
- ✅ 본 의뢰 자료의 결함 / 누락 / 모순 지적 (의뢰자도 알지 못한 결함)
- ✅ 본 prep brief 의 *외부 LLM 관점* 평가 (Claude 패밀리 자기참조 편향 통제 효과)
- ✅ 1인 개발자 환경의 *실제 운영* 관점 평가 (가상의 enterprise 환경 가정 금지)

### 8.3 응답 형식 권고

```
응답 헤더:
- 응답자 vendor (예: GPT-5 / Gemini Pro / 다른 vendor)
- 응답 일자
- 응답자 자기 명시 (선택, blind 의뢰 답습 시 생략 가능)

19 질문 각각:
Q<N>. <질문 답습>
판정: <APPROVE / APPROVE WITH CONDITIONS / PARTIAL / BLOCK / 권고 옵션>
근거:
  - <근거 1>
  - <근거 2>
  - ...
조건 (APPROVE WITH CONDITIONS 시):
  - <조건 1>
  - ...
한계 / 가정:
  - <한계 / 가정 1>
  - ...

종합 (Q19 답습):
- 최종 판정: <APPROVE / APPROVE WITH CONDITIONS / PARTIAL / BLOCK>
- 우선순위: <Group α / β / γ 中 어느 그룹 우선>
- 본 prep brief 의 결함 / 누락:
  - ...
```

응답 저장 경로: `docs/external-review/2026-05-13-backlog3-t3-zone-review-response{,-gemini,-claude,-<vendor>}.md` (응답자 vendor별 분리)

---

## 9. 부록 — 본 의뢰의 검증 / 참조

### 9.1 본 의뢰 자료의 *self-contained* 검증

| 검증 영역 | 본 의뢰 자료 포함 여부 |
|--------|------------|
| Backlog #3 정의 + 6 sub-영역 설명 | ✅ §2 + §3 |
| 그룹 분리 권고 + 대안 옵션 | ✅ §4 |
| 그룹별 위험 매트릭스 + 5 영구 핵심 제약 영향 | ✅ §5 |
| 풀 3+1 + 외부 LLM 1+ 의무성 + 응답 회수 후 처리 | ✅ §6 |
| 19 질문 (3 Group × 6 + 종합 1) | ✅ §7 |
| 금지 사항 + 응답 형식 권고 | ✅ §8 |
| 본 의뢰자 입장 + 검토 메타 목적 | ✅ §0 |
| 시스템 목적 + 권위 위계 + 5 영구 핵심 제약 + T1/T2/T3 정의 | ✅ §1 |
| MVP 단계 / Backlog 현 상태 / PoC 시제 완료 영역 | ✅ §2 |

### 9.2 본 의뢰 응답이 *흡수* 될 후속 단계

```
본 의뢰 응답 회수 (vendor 1+, 권고 GPT + Gemini)
  ↓
사용자 명시 응답 회수 + 응답 저장
  ↓
풀 3+1 합의 *진입* 결정 (사용자 명시) — 응답 회수 후 별도 단계
  ↓
내부 Agent A / B / C 독립 분석 (본 의뢰 응답 + 본 prep brief 답습)
  ↓
Reviewer 종합 (Agent A/B/C 결과 + 외부 LLM 응답 + 본 prep brief)
  ↓
사용자 명시 결정 영역 (Group α / β / γ 진입 우선순위 결정 / 진입 부적합 시 결함 수정 / 재의뢰)
```

### 9.3 본 의뢰의 답습 출처

| 출처 | 답습 영역 |
|------|--------|
| `docs/phase0/backlog3-t3-zone-full-3plus1-brief.md` (commit `ad9a02d`, 828줄) | 본 의뢰의 주요 대상 — prep brief |
| `docs/external-review/2026-05-10-cross-vendor-evidence-ledger-protection-request.md` | 의뢰 형식 답습 |
| `docs/external-review/2026-05-09-c14-cross-vendor-p2v3-pre-adoption-request.md` | 의뢰 형식 답습 + cross-vendor blind 답습 |
| `docs/architecture/implementation-runtime-roadmap-mvp1.md` | §3.3 + §3.5 + §4.3 + §4.4 + §4.6 + §4.7 + §5.5 답습 |
| `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.4 | T3 영역 분리 답습 |
| `docs/decisions/ADR-010-vault-hsm.md` | Vault HSM 권위 본문 답습 (§X 진입 의무 명시) |
| `docs/decisions/ADR-008-hermes-adoption-decision.md` §A.2 R1-2 + §2.6.2 R2-1 | entrypoint stat / docker secret 답습 |
| `docs/review/3plus1-consensus-2026-05-13-backlog2-gp5-1.5-remaining-items.md` (commit `8ba5182`) | Backlog #2 잔여 5 항목 Deferred 유지 합의 답습 |
| `docs/review/3plus1-consensus-2026-05-13-pc4-t2-c5c-c6-satisfaction.md` (commit `78483c5`) | PC-4 T2 sub Partially Satisfied 합의 답습 |
| `docs/review/3plus1-consensus-2026-05-12-backlog6-implementation-entry.md` (commit `f40423f`) | Layer B 9 sub-수단 본문 채택 답습 |

---

**의뢰 마무리**:

본 의뢰는 19 질문의 *근거 기반 독립 판정* 을 요청합니다. 의뢰자는 어떤 판정도 사전에 선호하지 않습니다. 응답은 풀 3+1 합의의 *입력* 으로만 사용되며, 자동 운영 적용 / Hermes PMO 격상 / ADR 본문 자동 갱신 등 자동 발효는 0건입니다.

**감사합니다.**
