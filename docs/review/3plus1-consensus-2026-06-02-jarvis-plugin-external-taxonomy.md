# 3+1 합의 보고서 — jarvis 플러그인 taxonomy 신설 (탑재형 vs 외부 관제형) brief v2

> **일자**: 2026-06-02 · **대상**: `docs/phase0/jarvis-plugin-taxonomy-external-view-design-brief.md` (v2)
> **프로토콜**: CLAUDE.md §3 (아키텍처 의사결정 + **보안 관련 변경 = 3+1 필수**) — brief §7 자체가 풀 3+1 권고
> **판정**: **REVISE (조건부 — BLOCKING 3건 해소 + 범위 축소 후 진입)**
> **참여**: Agent A(구현) · Agent B(안전/신뢰경계) · Agent C(대안) · Reviewer(교차비교 + 코드 재검증)

---

## 0. 한 줄 요약

세 에이전트 모두 **개념 구분(taxonomy) 자체는 유효**하다는 데 수렴한다. 그러나 **제어 채널 + 자격증명
보유 + 리스크 게이트 집행**은 셋 다 미해결/위험으로 본다. 합의 판정은 **REVISE**: ① 자격증명을
자비스 본체에 두는 §92 결론을 뒤집고(C-β 방향), ② 범위를 **패턴1 링크 허브 읽기측 먼저**로 축소,
③ G6(b) self-선언을 배제한다. **이 세 가지가 BLOCKING이며, 나머지(별도 레지스트리 여부 G1·전권의
강도)는 사용자 가치판단 회부**다.

---

## 1. 교차 검증 — 실측 주장 (Reviewer가 코드 재확인)

| # | 주장 | 출처 | 분류 | Reviewer 확인 |
|---|---|---|---|---|
| 1 | 패턴1 링크허브 = "거의 0 구현". `discover_plugins`/`load_enabled`/`loadPlugins()` 강하게 재사용 가능 → brief §2 "재사용 불가"는 **under-claim** | A | **Consensus(암묵)** | ✅ `plugin_registry.py:122~165` + `index.html:2263 loadPlugins()` 실재. 읽기측 레지스트리는 구조 복제로 충분. brief §2 "거의 재사용 불가"는 *제어채널엔* 맞지만 *링크/표시*엔 과소평가 — A 정확 |
| 2 | `_ENV_ALLOWLIST`(worker_setup:68-71)가 자격증명 차단 → 격리워커로 CLI 제어 불가 | A | Gap(A 단독) | ✅ `worker_setup.py:68` allowlist = PATH/LANG/SSL_CERT 류만. 토큰·SSH·AWS 전부 차단. G5 "CLI 실행" 후보는 격리와 정면충돌 — A 정확 |
| 3 | 현 ApprovalGate는 **워커 반영 게이트일 뿐 외부 송신 게이트 아님** | B | Gap(B 단독) | ✅ `approval.py` ApprovalRequest = `worker_alias`/`output_preview`, "반영 전" 단일 게이트. 외부 시스템 dispatch 게이트 신규. B 정확 |
| 4 | parse_manifest = 단일 스키마(`_REQUIRED=name/title/panel_js`). `kind` 흡수 시 탑재형 검증 오염 | A | **Divergence**(A=별도 레지스트리 / C=단일+source) | ✅ `plugin_registry.py:42 _REQUIRED` 단일. 흡수는 검증 분기 침투 사실. **단** C 반론도 성립 → §2.G1 판정 |
| 5 | 자격증명 = "자비스가 보유"(brief §92)는 invariant **정면 위반** | B | Partial(B강) | ⚠️ **부분 사실 + framing 과장**. 현 코드는 자격증명을 *워커 가짜홈*(`worker_setup:117-145`)에 시드 — 자비스 *본체 프로세스(orchestrator/HUD)* 는 in-memory 보유 0. **B의 "본체가 보유"는 현 상태 오기**. 그러나 brief §92가 *외부 시스템용* 새 자격증명을 자비스가 보유하라는 것은 **신규 표면 도입이 맞음** → B 결론(격리 필요)은 유효, 근거 framing만 정정 |
| 6 | G6(b) "manifest 자기 등급선언" = §90 "결정적 정책"과 **내부모순** | B | Gap(B 단독) | ✅ brief §90(코어 결정적 매핑) vs §147 G6(b)(신뢰경계 밖 주체 자기선언) 양립불가. B 정확 |
| 7 | StaticFiles 마운트 부재(전 합의 C-2) | (배경) | **이미 해소** | ✅ `server.py:692 Mount("/plugins", StaticFiles)` 실재. **세 에이전트 누구도 이걸 already-solved로 명시 안 함** — 패턴1 프론트 마운트 seam은 이미 존재(추가 부담 0). Reviewer 보강 |
| 8 | 패턴2(외부 JSON 렌더) = 저장형 XSS 신규표면 + 외부 URL = SSRF | B | Gap(B 단독) | ✅ 현 `panel.js:86 grid.innerHTML=''` 후 `appendChild(card())` = DOM 조립(textContent 경유)이라 *현재는* 안전. 그러나 패턴2가 외부 임의 JSON을 렌더하면 신규 표면 맞음. B 정확 |
| 9 | 이 환경이 이미 MCP(Notion/Drive) 사용 중 → C-β(외부가 자기 API 노출) 현실적 | C | Gap(C 단독) | ✅ 사실(시스템 MCP 툴 등재). C-β 실현 가능성 보강 |
| 10 | brief는 **코드 변경 0** 개념 정리 | brief §6 | Consensus | ✅ brief §161. 따라서 BLOCKING = "이 방향으로 구현 시 깨질 설계 결정"(TDD 전 해소 가능) |

---

## 2. 핵심 갈림길 3건 — 3자 입장 + 합의

### G1: 외부형 = 별도 레지스트리(a) vs 단일 manifest `kind/source` 필드(b)

| | A | B | C | 판정 |
|---|---|---|---|---|
| 입장 | **(a) 별도** — kind 흡수는 parse_manifest 단일 스키마 오염 | (직접 입장 약함, 보안 무관) | **(b) 단일+source** — 별도 ~250줄 vs 속성 ~40줄, 유지보수/dogfood 2배 | **Partial → (b) 우세, 단 조건부** |

**Reviewer 판정**: **(b) 단일 모델 + `source` 속성**을 권고하되 A의 우려를 흡수한다. 근거:
- A의 "검증 오염"은 **실재 리스크**(parse_manifest는 단일 `_REQUIRED`). 그러나 이는 (b)를 기각할
  근거가 아니라 **(b)를 깨끗하게 구현할 제약**이다 — `source: external`이면 `panel_js` 등 탑재형
  필수 필드를 **요구하지 않는 분기**를 명시적으로 두면 오염이 아니라 정상 분기다.
- C의 정량(250 vs 40줄)과 "두 메커니즘 = dogfood 2배"는 **비례성상 강한 근거**. 솔로 툴에서 병렬
  레지스트리 유지보수는 과설계 쪽.
- **단**: 읽기측 MVP(아래 범위 축소) 단계에서는 *어느 쪽이든 코드가 거의 안 나옴* — 링크 카드는
  `name+url`만 필요. G1 최종 확정은 **패턴2(제어) 승격 시점으로 DEFER 가능**. 지금 강제 결정 불요.

### 풀 3+1 합의 필요성: B(보안표면 ↑ = 필수) vs C(지금 링크만이면 미룸)

| | B | C | 판정 |
|---|---|---|---|
| 입장 | **필수** — 자격증명+write/control = 보안 다중검증 | 지금 **링크 카드만**이면 고위험 없음 = YAGNI, 2~3 사례 후 비례 추가 | **둘 다 옳음 — 단계 분리로 양립** |

**Reviewer 판정**: 모순이 아니라 **범위에 대한 조건부**다.
- **읽기측(패턴1 링크 + 패턴2 read-only 렌더)**: 고위험 자격증명/제어 0 → C 옳음. 풀 3+1 **불요**,
  1-agent TDD로 충분. (**이 보고서가 이미 그 read-only 범위에 대한 합의를 종결**한다.)
- **제어측(§3.5 게이트 + 자격증명 보유 + write)**: B 옳음. 이 범위는 **별도 풀 3+1 필수**이며,
  본 합의가 승인하지 않는다. brief §7-2의 풀 3+1 권고는 **제어측에 한해 유효**.

### 범위: brief 원안(taxonomy + 제어 게이트 동시) vs C-γ(링크 카드 1개만)

**Reviewer 판정**: **C-γ(점진) 채택**. brief §3은 스스로 "TTS 1사례로 탑재형 추상을 정당화한
실수"를 인정했는데, **외부형도 TTS 1사례로 제어 인프라 전체를 정당화하면 같은 실수**다(C 항목6,
정확한 지적). rule-of-three 살아있음. 따라서:
- **1단계(지금)**: 패턴1 링크 허브 읽기측. 제어·자격증명·게이트 전부 제외.
- **2단계(2~3 외부 사례 관찰 후)**: 패턴2 read-only 렌더(저위험 리터치는 제외).
- **3단계(명시 trigger + 별도 풀 3+1)**: §3.5 제어 게이트 + 자격증명. 본 합의 범위 밖.

---

## 3. 통합 BLOCKING 3건 (A 3 + B 3 + C-β 수렴, 중복제거)

| # | BLOCKING | 수렴 출처 | 왜 막아야 하나 | 해결 방향 |
|---|---|---|---|---|
| **X-1** ⭐비협상 | **자비스 본체 자격증명 보유 금지** | A-BLOCK-1 + B-BLOCK-2 + C-β | brief §92 "자격증명은 자비스가 보유"는 현 격리(본체 in-memory 자격 0)를 역행. 본체엔 untrusted boss LLM + 워커 산출물 흐름 → 본체 침해 = 외부 자격 전파. "게이트가 막는다"는 detection, 보유 자체가 prevention 실패 표면 | **C-β 우선**: 외부 시스템이 자기 prod 자격증명 보유, 자비스↔외부는 로컬 토큰 1개(또는 기존 MCP). 자비스가 부득이 보유 시 본체 메모리 밖(broker/키체인/송신시점 fetch) + `_SENSITIVE_NAMES`(plugin_install.py:36) 등재. "보유+게이트"만으론 불충분 |
| **X-2** ⭐비협상 | **제어 채널 ↔ 격리 충돌 미해결 + 게이트 집행 seam 부재** | A-BLOCK-2 + A-BLOCK-3 + B-BLOCK-1 | G5 "CLI 실행" 후보는 `_ENV_ALLOWLIST`가 자격 차단해 격리워커로 불가, 비격리 실행은 invariant 위반(A). §3.5 게이트는 *집행 seam이 없으면 문서상 정책에 그침*(A). 현 ApprovalGate는 워커 반영 전용이라 외부 송신 미커버(B). **누적/빈도/외부효과 비가역**(저위험 100회 재실행 → ban/과금)은 개별 동작 테이블이 못 막음(B) | 제어측은 **HTTP API로 좁힘**(격리 정합 — A). 단일 결정적 controller가 외부 dispatch 게이트 신설(boss 직접 호출 차단). 빈도/누적 게이트 코어 고정. **이 전체가 3단계(별도 풀 3+1)로 DEFER** |
| **X-3** ⭐비협상 | **리스크 등급 매핑 = 코어 고정만, G6(b) self-선언 배제** | B-BLOCK-3 + B(§90↔§147 모순) | brief §147 G6(b)(manifest 자기 등급선언)는 신뢰경계 밖 주체가 자기 게이트를 정함 = §90 "결정적 정책"과 양립불가(B, 사실). 미등재 동작이 self-선언으로 저위험 위장 가능 | **G6(a)만 채택**: 등급 = 코어 고정 allowlist(`select_ports` 패턴 답습 — 미등재=미자율/고위험 fail-closed). G6(b) **기각**. capability 기반(C 항목3: 외부형이 capability 선언 → 고위험 capability는 코어가 자동 사람승인 회부)은 *코어가 등급 소유* 한에서 G6(a)와 정합 — 후속 채택 후보 |

**DEFER (합의 등록만, 발효는 명시 trigger까지)**: §3.5 제어 게이트 전체 / 자격증명 broker 구현 /
패턴2 reader / 빈도·누적 게이트 / iframe 임베드. **솔로 툴 비례성 + rule-of-three.**

---

## 4. brief over-claim / 오류 정정 권고 (R-prefix, [[feedback_pass_scope_overclaim]])

1. **§2 "재사용 불가"** → **under-claim 정정**(A). 읽기측(레지스트리/HUD 카드/loadPlugins)은 강하게
   재사용 가능. "재사용 불가"는 *제어 채널*에만 한정. **추가**: StaticFiles 마운트(server.py:692)는
   이미 존재 — 패턴1 프론트 마운트 부담 0.
2. **§92 "자격증명은 자비스가 보유하되 게이트가 막는다"** → **정정**. ① detection≠prevention(보유
   자체가 표면) ② 현 격리는 자격을 *워커 가짜홈*에 두고 본체는 in-memory 0 — 본체 보유는 **신규
   역행**. C-β(외부 보유 + 로컬 토큰) 우선 명시.
3. **§90 "결정적 정책" vs §147 G6(b)** → **내부모순 해소**. G6(b) 기각, G6(a) 코어 고정만 채택을
   본문에 못박음.
4. **§135 "능력은 전권으로 깔고 게이트로 조절"** → **framing 완화**(B). "게이트 1버그 = 전권 노출"은
   비례 보안 역행. "능력 범위는 *코어 allowlist가 정의*하고 미등재=미자율" 로 재서술. 단 Reviewer
   보강: brief §80 구조(전권=넓은 범위, 게이트=리스크 비례) 자체는 정합 가능 — **언어 차원 위험**
   이지 구조 결함 아님(B도 정직 단서에서 동의).
5. **§3 vs 외부형 첫 사례** → **추가**(C 항목6). 외부형도 TTS 1사례로 제어 인프라 정당화 = §3가
   인정한 실수 반복. "1~2개 ad-hoc 링크 카드 먼저 관찰" 명시.

**정직하게 유지할 brief 강점(공정)**: §3.5 결정적 테이블 + 모호 시 고위험 fail-closed(C의 가역성
자동판정보다 안전 — C도 동의), §6 TTS 재분류 그대로 두기(되돌림 비용 0), §6 풀 3+1 권고(제어측),
개념 구분 자체. brief는 over-claim 회피를 *대체로* 잘했고(§3·§6 자기비판 정직), 정정은 §92·G6
2개 지점에 집중된다.

---

## 5. 최종 판정: REVISE → brief v3 (또는 읽기측 직접 TDD 진입)

- **R1 (BLOCKING)**: X-1·X-2·X-3 해소. **셋 다 제어측이므로 1단계(읽기측)는 BLOCKING 회피**.
- **R2 (범위)**: C-γ 점진 채택 — **1단계 = 패턴1 링크 허브 읽기측만**. 제어·자격증명·게이트 DEFER.
- **R3 (over-claim)**: §4의 1~5 정정.
- **R4 (갈림길)**: G1 = **(b) 단일 + source 속성 우세**(단 읽기측 단계엔 결정 불요, DEFER 가능) /
  G3 = TTS 그대로 + 새 외부형은 새 사례(안전 기본값) / G5 = **HTTP만**(제어 도입 시) / G6 = **(a)
  코어 고정만, (b) 기각**.
- **R5 (프로세스)**: **읽기측 1단계는 풀 3+1 불요**(본 합의가 종결, 1-agent TDD). **제어측 3단계는
  별도 풀 3+1 필수**(brief §7-2 유효).

---

## 6. 사용자 회부 사항 (가치판단 — 합의가 못 정함)

| # | 회부 사항 | 왜 사용자 영역인가 | 합의의 권고(참고) |
|---|---|---|---|
| **U-1** | **"전권 통제"의 강도/긴급성** | C 정직 단서: 즉시 제어를 원하면 C-γ(링크만)로 부족 → C-β 절충 필요. "쉽게 보고 싶을 뿐"(발화1) vs "전면 제어권"(발화2)의 무게는 사용자만 안다 | 발화1(보기) = 1단계 링크로 100% 충족. 발화2(제어) = *능력 희망*이지 즉시 필수 아님 → 점진 권고 |
| **U-2** | **외부 시스템이 본인 작품인가, 제3자인가** | C-β(외부가 자기 API/자격 노출)는 **외부가 본인 통제 하**일 때만 성립. 제3자 SaaS면 C-β 불가 → X-1 해법 재설계 | 본인 작품 가정 시 C-β 최적. 제3자면 broker 필수(무게 ↑) |
| **U-3** | **G1 최종(별도 레지스트리 vs 단일+source)** | 읽기측엔 코드 거의 안 나와 DEFER 가능하나, 사용자가 미리 정하고 싶으면 결정 | (b) 단일+source 권고(비례성). 단 강제 아님 |
| **U-4** | **제어측(3단계) 진입 trigger 시점** | "명시 trigger 전 DEFER"가 합의 기본값. 사용자가 지금 trigger를 당기면 별도 풀 3+1 즉시 가동 | 2~3 외부 사례 관찰 후 비례 진입 권고 |

---

## 7. 다음 단계 권고 (자동 진입 0)

1. **사용자 검토**: U-1~U-4 회부 사항 + §5 REVISE 항목이 멘탈 모델과 맞는지.
2. **brief v3 정정**(§4 over-claim) 또는 — 사용자가 1단계 읽기측을 승인하면 — **v3 생략하고 패턴1
   링크 허브 직접 TDD 진입**(BLOCKING 전부 회피, 풀 3+1 불요). A의 점진 MVP 권고와 일치:
   `external_registry`(구조 복제) + `/api/jarvis/external` GET + HUD `loadExternal` 링크 카드.
3. **제어측(§3.5)은 본 합의가 승인하지 않음** — U-4 trigger + 별도 풀 3+1 + 보안 다중검증 후에만.

---

**관련**: `[[3plus1-consensus-2026-06-01-jarvis-plugin-architecture]]`(직전 합의 형식 답습) ·
`[[project_jarvis_plugin_architecture]]` · `[[project_jarvis_controlled_child_then_friday]]` ·
`[[project_minimize_user_intervention]]` · `[[feedback_proportionate_security_personal_tool]]` ·
`[[feedback_pass_scope_overclaim]]` · `[[feedback_ceremony_inflation]]` ·
`[[reference_claude_landlock_isolation]]` · 대상 brief `jarvis-plugin-taxonomy-external-view-design-brief.md` v2
