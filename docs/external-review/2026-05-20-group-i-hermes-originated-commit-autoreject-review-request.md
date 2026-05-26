# Cross-vendor Blind 검토 의뢰 — Group I (Hermes-originated commit auto-reject) 풀 3+1 진입 전 검토

> **이 문서를 통째로 ChatGPT (GPT-5.x), Gemini, 또는 다른 *비-Claude* vendor 강력한 LLM 에 붙여넣고 평가를 요청하십시오.** 첨부 자료 없이 본 문서만으로 평가 가능하도록 작성되었습니다.
>
> **본 의뢰의 *blind 강도* 는 가장 높습니다. 본 자료에는 다음이 *의도적으로 포함되지 않습니다*:**
> - ❌ 본 프로젝트의 내부 Agent A / B / C 분석 결과 (아직 풀 3+1 진입 전)
> - ❌ 본 프로젝트의 Reviewer 종합 결론
> - ❌ 의뢰자 (사용자) 가 원하는 결론 / 방향 / 선호
> - ❌ APPROVE 유도 표현 / 답안 제시 / 결론 시사
>
> 본 의뢰는 vendor 다양성 (cross-vendor) 을 통해 진정한 *제3자* 의 독립 판단을 확보하기 위함입니다. 본 프로젝트의 메인 작업 컨텍스트는 Claude (Anthropic) 이므로, 본 cross-vendor 의뢰의 핵심 목적은 *비-Claude vendor* 의 독립 의견 확보입니다. 응답은 `docs/external-review/2026-05-20-group-i-hermes-originated-commit-autoreject-review-response{,-gemini,-<vendor>}.md` 에 저장될 예정입니다.

**작성일**: 2026-05-20
**대상 의뢰자**: ChatGPT (GPT-5.x) / Gemini / 다른 *비-Claude* vendor 1+ — cross-vendor blind
**의뢰 대상 brief**: `docs/phase0/group-i-hermes-originated-commit-autoreject-full-3plus1-brief.md` (commit `bc9cb07`, DRAFT)

---

## 0. 검토 의뢰자의 입장 + 본 검토의 형식

### 0.1 검토 의뢰자

저는 1인 개발자로 "**아이디어를 던지면 AI 에이전트 (주로 Claude Code) 가 SDD + TDD 로 자동 개발하도록 설계된 메타-템플릿**" 을 만들고 있습니다. 본 프로젝트 자체는 그 템플릿이며, 새 아이디어가 생길 때마다 본 템플릿을 복사해 시작합니다.

본 프로젝트의 메인 작업 컨텍스트는 Claude (Anthropic) 입니다. 따라서 본 cross-vendor 의뢰는 *비-Claude vendor* 의 의견을 확보하는 것이 핵심 목적입니다.

### 0.2 본 검토의 형식

본 검토는 **10 질문** 입니다. 각 질문에 독립적으로 *근거 기반* 판정을 요청합니다.

본 질문은 다음을 *묻지 않습니다*:
- ❌ 의뢰자가 무슨 답을 원하는지 (의뢰자는 답을 미리 제시하지 않음)
- ❌ 다른 LLM 이 어떤 답을 했는지 (본 자료는 다른 LLM 응답을 *포함하지 않음*)
- ❌ 내부 Agent 가 어떤 결론에 도달했는지 (아직 내부 풀 3+1 진입 전)

**본 의뢰자는 어느 판정도 사전에 선호하지 않습니다.** *근거에 의해 도출된 판정* 이 안전한 답입니다.

### 0.3 본 검토의 *메타* 목적

본 의뢰는 **풀 3+1 합의 *진입 전*** 의뢰입니다. 내부 Agent A / B / C 가 아직 분석하지 않은 시점입니다. 본 의뢰의 응답은 풀 3+1 합의의 *입력* 으로만 사용됩니다 — 자동 운영 적용 / 실 hook 구현 / Hermes PMO 격상 / ADR 본문 자동 갱신 모두 *불가* (§6 답습).

⚠️ **본 의뢰 영역은 특히 cross-vendor blind 가 중요합니다.** 본 의뢰의 주제(Group I) 는 *"AI agent(Claude 포함) 가 자기 자신의 변경을 self-approve 하지 못하게 차단하는 메커니즘"* 입니다. 즉 **본 프로젝트의 메인 AI(Claude) 자신이 평가 주체가 되면 자기참조 편향** 이 발생할 수 있는 영역입니다 — 비-Claude vendor 의 독립 판단이 구조적으로 필수입니다.

---

## 1. 시스템 목적 (요약)

### 1.1 프로젝트 정체성

- **이름**: AI Development Tool Template
- **사용자**: 1인 개발자 (동일 호스트, SPOF(Single Point of Failure) 의도적 수용)
- **저장소**: 코드 0줄 (PoC 도구 ~17개 = 산출물 시제 한정), 약 80+ 마크다운 (헌법 + 12 ADR + 11 설계 문서 + 60+ 합의/외부검토 보고서 + 가이드 + 사양 + 세션 로그)
- **메타-슬로건**: "에이전트에게 하라고 말하지 말고, 잘못하는 것이 *불가능*하게 만들어라."

### 1.2 핵심 방법론

- **SDD** (Specification-Driven Development): 코드보다 문서 우선
- **TDD** (Test-Driven Development): RED → GREEN → REFACTOR
- **하네스 엔지니어링**: `Agent = Model + Harness` — 가이드(feedforward) + 센서(feedback) 6 layer (Layer 0 CLAUDE.md ~ Layer 6 Human Review)
- **3+1 멀티 에이전트 합의**: Agent A(구현) + Agent B(품질/안전) + Agent C(대안) 병렬 독립 분석 → Reviewer 교차 비교 + 합의

### 1.3 권위 위계 (영구)

```
헌법 (Constitution) > ADR > 설계 문서 > 합의 보고서 > 코드
사용자 명시 결정 = 모든 T2 / T3 의 최종 권위
```

### 1.4 영구 핵심 제약 5건 (본 의뢰의 핵심 배경)

1. **Hermes ≠ root of trust** — Hermes(에이전트 오케스트레이션 runtime) 는 신뢰의 뿌리가 *아니다*. 정책·합의·gate 를 *제안*만 할 수 있고 *승인*할 수 없다.
2. **단일 source-of-truth** — 정책/합의의 권위 source 는 git commit (사용자 명시) 한정.
3. **수단/목적 분리** — 안전 *결과* 가 본질, 특정 수단은 교체 가능.
4. **T1/T2/T3 분리** (아래 §1.5).
5. **SPOF 의도적 수용** — 1인 동일 호스트 모델의 SPOF 를 의도적으로 수용. multi-host/다인 전환 시 추가 layer 의무 발동 트리거 명시.

### 1.5 T1 / T2 / T3 영역 분리

| 분류 | 의미 | 예 |
|----|----|----|
| **T1** | 자동 허용 | Worker 작업 분배 / Tools 검증 / Skill 후보 *제안* / 자체 학습(학습만) |
| **T2** | 사용자 명시 승인 필수 | Skill *등록* / Memory promotion / 합의 결과 채택 / 의존성 업그레이드 merge |
| **T3** | 절대 금지 (자동 시도 시 auto-reject + audit + alert) | 정책/ADR/Constitution 자동 변경 / Gate 실패 무시 / PASS 자동 선언 / PMO 자기 격상 / **합의 결과 silent override** |

---

## 2. Group I 범위 + 배경

### 2.1 Group I 정의

**Group I = Hermes-originated commit auto-reject** — 에이전트 runtime(이하 "Hermes") 이 *단독으로* 생성한 git commit (특히 정책성·합의·gate 정의·`.git/` 영역) 을 자동 식별·차단하고 audit log + 사용자 alert 를 발생시키는 enforcement 설계 단위.

권위 근거(1차): 내부 설계 문서 G3 §2.2 #20 — *"합의 결과 silent override 또는 수정"* 은 **T3 절대 금지** 이고, 강제 메커니즘 = *"합의 보고서 git commit 보존 + Hermes-originated 수정 자동 reject"*.

### 2.2 본 의뢰가 왜 발생했는가 (Group α C-2 답습)

직전 합의(Group α — branch protection / `--no-verify` 우회 차단 / pre-commit 의무화) 의 condition C-2 가 다음을 명시했습니다:

> **"AI agent self-approval 차단 = Group I (Hermes-originated commit auto-reject) 별도 합의 결합 필수"**

즉, branch protection(GitHub repo 영역) 단독으로는 *AI agent 가 자기 변경을 self-approve* 하는 경로를 완전히 차단하지 못하며, Hermes runtime 영역의 commit 식별·차단(Group I) 이 결합되어야 차단책이 완성됩니다.

### 2.3 Defense in depth 3-layer 구도 (검토 대상)

```
잔존 우회 경로                       차단 layer                      책무 영역
──────────────────────────────────────────────────────────────────────────
인간/AI 의 --no-verify 우회      →  branch protection + required CI   GitHub repo (Group α, 발효)
Hermes-originated commit          →  식별 + auto-reject                Hermes runtime (Group I, 본 의뢰)
정책성 파일 직접 변조             →  filesystem read-only mount + ACL  Hermes container (G3 §2.5)
```

세 layer 의 *결합* 이 Defense in depth 이며, 각 layer 의 enforcement 주체가 다른 것이 "단일 source-of-truth 보존(핵심 제약 #4)" 의 핵심입니다.

### 2.4 self-reference (합의 인프라 순환 권위) 배경

Hermes 가 3+1 합의의 *실행 인프라* 이기도 하다면, *Hermes 자기 격상 / 정책 변경 / gate PASS* 같은 Hermes 관련 결정을 Hermes 가 실행한 합의로 결정 → **자기참조 역설**. 내부 설계는 이를 다음으로 차단합니다: *"Hermes 는 합의 결과를 기록만 가능, 승인 주체가 될 수 없다 — 합의 결과 commit author ≠ Hermes(Hermes-originated commit auto-reject)."* **Group I = 이 원칙의 runtime enforcement 단위입니다.**

### 2.5 현 구현 상태 (전제 — 변경 0건)

- 내부 설계 문서 G3 = **DESIGN PASS / IMPLEMENTATION PENDING** (격리 환경 PoC + 자동 회귀 검증 경로 미충족)
- 본 의뢰는 **설계 결정 합의 진입 전** 단계 — 실 hook / filesystem ACL / CI step / GitHub ruleset 구현은 *별도 합의(Implementation/Runtime PASS) 영역* 으로 본 의뢰 범위 밖
- "Hermes" 는 본 의뢰에서 *에이전트 오케스트레이션 runtime* 의 일반 명칭으로 이해하시면 됩니다 (특정 제품에 대한 사전 지식 불필요 — commit 출처가 "사람 사용자" 가 아니라 "자동 에이전트" 라는 점이 핵심).

---

## 3. 풀 3+1 + 외부 LLM 1+ 필요성 (본 의뢰의 근거)

본 프로젝트는 Group I 를 **T3 보안 enforcement 영역** 으로 잠정 분류했습니다. 그 근거:

- Group I = T3 절대 금지(합의 결과 silent override 차단) 의 *enforcement*
- 5 영구 핵심 제약 中 #1(Hermes ≠ root of trust) + #4(단일 source-of-truth) 에 직결
- 합의 인프라 self-reference(순환 권위) 자체를 대상으로 함 → Reviewer-only 단축 합의(메인 AI 가 orchestrate 하는 단축) 는 메타-편향 통제 부족 → **풀 3+1 + 외부 LLM 1+ 가 구조적으로 정합**

또한 직전의 cross-vendor 외부 응답(GPT/Gemini, 2026-05-13) 은 branch protection(Group α) enforcement 중심이었고 **Group I 의 식별·차단 메커니즘 자체에 대한 직접 입력이 부족** 했습니다. 본 의뢰는 그 공백을 메우기 위한 Group I 전용 cross-vendor blind 검토입니다.

---

## 4. 본 의뢰의 *10 질문* (검토 의뢰)

**Q1**. Hermes(자동 에이전트) 가 생성한 commit 을 *어떻게 식별* 해야 하는가? 어떤 식별 신호가 (i) 신뢰성 (ii) 위장 저항성 (iii) 1인 개발자 운영 부담 측면에서 적절한가? 근거는?

**Q2**. commit author / committer / signature(GPG/SSH) / 기타 metadata(예: commit trailer, committer email domain, 별도 committer identity) 中 *무엇을 신뢰* 할 수 있는가? 각 신호의 위장(spoofing) 가능성과 한계는? 자동 에이전트가 사람 사용자의 identity 를 사칭하는 경우를 어떻게 다룰 것인가?

**Q3**. 자동 에이전트(Hermes) 가 *우회할 수 없는* 외부 enforcement layer 는 무엇인가? 에이전트가 코드 실행 권한을 가진 환경에서 "에이전트 스스로는 끌 수 없는" 차단 지점을 어떻게 설계하는가? (예: 격리 컨테이너 read-only mount / 별도 권한 경계 / server-side 강제)

**Q4**. pre-commit / pre-push / server-side(pre-receive) / GitHub ruleset(branch protection) 中 *어느 계층* 이 Hermes-originated commit 차단에 적절한가? 각 계층의 장단점과 우회 가능성은? 단일 계층 vs 다계층(Defense in depth) 中 권고는?

**Q5**. **1인 single-host 환경** 에서 false positive(사용자 본인의 정당한 commit 을 Hermes-originated 로 오차단) 를 어떻게 통제할 것인가? 사용자와 에이전트가 같은 호스트·같은 자격증명을 공유할 가능성이 높은 환경에서 식별 신뢰성의 한계는?

**Q6**. 사용자 직접 commit 은 *허용* 하고 Hermes-originated commit 만 *차단* 하는 것이 기술적으로 가능한가? 가능하다면 어떤 메커니즘으로? 불가능하거나 신뢰성이 낮다면, 그 한계를 어떻게 보완(예: 사용자 명시 승인 절차 / 사후 audit) 할 것인가?

**Q7**. **Hermes ≠ root of trust** 원칙(자동 에이전트는 신뢰의 뿌리가 아니며 정책/합의를 승인할 수 없다) 을 commit 차단 설계에서 *어떻게 보존* 할 것인가? 차단 메커니즘 자체가 에이전트에 의해 변조될 수 있다면 원칙이 무너지는데, 이를 어떻게 막는가?

**Q8**. 3-layer 책무 분리 — (a) branch protection(GitHub repo) + (b) filesystem read-only ACL(컨테이너) + (c) Hermes-originated commit reject(runtime) — 가 *적절* 한가? 책무 중첩/공백은 없는가? 단일 source-of-truth 보존 관점에서 이 분리가 옳은가, 아니면 통합이 나은가?

**Q9**. Group I 이 **Hermes PMO 격상**(에이전트 runtime 의 권한 승격) 이나 **Operational Readiness PASS**(운영 준비 완료 선언) 와 *연결될 때의 위험* 은 무엇인가? commit 차단 메커니즘이 거꾸로 "에이전트가 충분히 신뢰할 만하다" 는 근거로 오용될 위험은? 어떤 경계가 의무인가?

**Q10**. 본 Group I 설계를 *풀 3+1 합의에 진입하기 전 반드시 보강* 해야 할 blocker(결함 / 누락 / 모순) 가 있는가? 의뢰자도 알지 못한 결함을 지적해 주십시오. (예: 식별 신호의 근본적 우회 가능성 / single-host 에서 차단이 사실상 무의미한 시나리오 / 다른 layer 와의 충돌 등)

---

## 5. 본 의뢰 자료의 결함을 지적해 주십시오

본 의뢰자는 본 자료의 결함을 *모를 수 있습니다*. 응답에서 다음을 환영합니다:
- 본 의뢰 자료의 누락 / 모순 / 가정 오류
- 1인 single-host 환경에서 Group I 가 *실효성이 없거나 과잉* 인 시나리오
- 본 프로젝트가 잘못 분류했을 수 있는 영역 (예: T3 가 아니라 다른 분류가 적절 / 별도 layer 가 더 적합)

---

## 6. 금지 사항 (사용자 명시 답습) — 본 의뢰 응답의 *영원 격리*

본 외부 LLM 검토 의뢰의 응답 / 결론은 **풀 3+1 합의의 *입력* 으로만 사용** 됩니다. 다음은 자동으로 발생하지 않습니다 (사용자 명시 결정 의무 영역):

| 영역 | 자동 발생 여부 |
|----|----|
| 풀 3+1 합의 보고서 *작성* | ❌ 자동 0건 (응답 회수 후 별도 단계) |
| Hermes-originated commit 차단 *실 구현* | ❌ 자동 0건 |
| git hook(pre-commit / pre-push / pre-receive) 구현 | ❌ 자동 0건 |
| CI workflow 변경 / GitHub ruleset(branch protection) 변경 | ❌ 자동 0건 |
| server-side enforcement 구현 / filesystem ACL 구현 | ❌ 자동 0건 |
| Hermes upstream(runtime 본문 / Dockerfile) 변경 | ❌ 자동 0건 |
| **Operational Readiness PASS 선언** | ❌ 자동 0건 |
| **Hermes PMO 격상 선언** | ❌ 자동 0건 |
| 식별 방법 / 차단 지점 / 보호 범위 *수단 최종 결정* | ❌ 자동 0건 (풀 3+1 + 사용자 명시) |
| 외부 LLM 응답 없는 상태에서 PASS 선언 | ❌ 자동 0건 |
| ADR 본문 자동 갱신 | ❌ 자동 0건 |

### 6.1 응답이 *해서는 안 되는* 것 (외부 LLM 의뢰자 명시)

- ❌ 의뢰자가 원할 것 같은 답 추측
- ❌ 다른 LLM 의 답을 시사하는 표현
- ❌ 내부 Agent 결론을 시사하는 표현
- ❌ APPROVE 유도 / BLOCK 유도 / 결론 시사
- ❌ 의뢰 자료에 포함되지 않은 *증거를 만들어내는* 행위

### 6.2 응답이 *발생해야* 하는 것

- ✅ 10 질문 각각에 대한 *근거 기반* 판정
- ✅ 본 의뢰 자료의 결함 / 누락 / 모순 지적
- ✅ Claude 패밀리 자기참조 편향 통제 관점 평가 (본 의뢰 영역이 특히 중요)
- ✅ 1인 개발자 *실제 운영* 관점 평가 (가상의 enterprise 환경 가정 금지)

---

## 7. 응답 형식 권고

```
응답 헤더:
- 응답자 vendor (예: GPT-5 / Gemini Pro / 다른 vendor)
- 응답 일자
- 응답자 자기 명시 (선택, blind 의뢰 답습 시 생략 가능)

10 질문 각각:
Q<N>. <질문 답습>
판정 / 권고: <근거 기반 결론 또는 권고 옵션>
근거:
  - <근거 1>
  - <근거 2>
한계 / 가정:
  - <한계 / 가정 1>

종합:
- 본 Group I 설계의 풀 3+1 진입 적합성 (진입 가능 / 조건부 / 보강 후 / 부적합)
- 진입 전 반드시 보강해야 할 blocker:
  - ...
- 본 의뢰 자료의 결함 / 누락:
  - ...
```

응답 저장 경로: `docs/external-review/2026-05-20-group-i-hermes-originated-commit-autoreject-review-response{,-gemini,-<vendor>}.md` (응답자 vendor별 분리)

---

## 8. 부록 — 본 의뢰의 검증 / 참조

### 8.1 본 의뢰 자료의 *self-contained* 검증

본 문서는 첨부 없이 단독으로 평가 가능하도록 작성되었습니다. Group I 정의(§2.1) / 배경(§2.2~§2.5) / 5 영구 핵심 제약(§1.4) / T1/T2/T3 분리(§1.5) 모두 본문에 포함되어 있어, 본 프로젝트 내부 문서에 대한 사전 지식 없이 10 질문에 답할 수 있습니다.

### 8.2 본 의뢰 응답이 *흡수* 될 후속 단계

```
본 의뢰 응답 회수 (vendor 1+, 권고 GPT + Gemini)
  ↓
사용자 명시 응답 회수 + 응답 저장
  ↓
풀 3+1 합의 *진입* 결정 (사용자 명시) — 응답 회수 후 별도 단계
  ↓
내부 Agent A / B / C 독립 분석 (본 의뢰 응답 + Group I brief 답습)
  ↓
Reviewer 종합 (Agent A/B/C 결과 + 외부 LLM 응답 + Group I brief)
  ↓
사용자 명시 결정 영역 (Group I 진입 여부 / 결함 수정 / 재의뢰)
```

### 8.3 본 의뢰의 답습 출처

| 출처 | 답습 영역 |
|------|--------|
| `docs/phase0/group-i-hermes-originated-commit-autoreject-full-3plus1-brief.md` (commit `bc9cb07`) | 본 의뢰의 주요 대상 — Group I brief |
| `docs/review/3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md` | Group α C-2 (결합 필수) + §6.1 (Defense in depth) |
| 내부 설계 G3 §2.2 #20 / §2.5 / §4 (Hermes-originated commit auto-reject / self-reference 차단) | Group I 권위 근거 |
| `docs/external-review/2026-05-13-backlog3-t3-zone-review-request.md` | 의뢰 형식 답습 (cross-vendor blind) |

---

**의뢰 마무리**:

본 의뢰는 10 질문의 *근거 기반 독립 판정* 을 요청합니다. 의뢰자는 어떤 판정도 사전에 선호하지 않습니다. 응답은 풀 3+1 합의의 *입력* 으로만 사용되며, 자동 운영 적용 / 실 hook 구현 / GitHub ruleset 변경 / server-side enforcement 구현 / Hermes PMO 격상 / Operational Readiness PASS / ADR 본문 자동 갱신 등 자동 발효는 0건입니다.

본 의뢰 영역은 *AI 자신이 자기 변경을 self-approve 하지 못하게 하는 메커니즘* 이므로, 비-Claude vendor 의 독립 판단이 구조적으로 가장 중요합니다.

**감사합니다.**
