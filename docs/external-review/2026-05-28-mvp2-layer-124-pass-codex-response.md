OpenAI Codex v0.128.0 (research preview)
--------
workdir: /home/delangi/문서/project/category/AI_development_tool
model: gpt-5.5
provider: openai
approval: never
sandbox: danger-full-access
reasoning effort: none
reasoning summaries: none
session id: 019e6c7f-dc0f-7581-81db-6b6244abb743
--------
user
당신은 외부 LLM 검토자 (cross-vendor blind review)입니다. 응답 vendor = OpenAI (codex CLI), 본 cycle 풀 3+1 Agent vendor = Anthropic Claude. cross-vendor 충족 (헌법 5조-2).

## 본 cycle 개요

AI_development_tool 프로젝트. 본 cycle = **Layer 1+2+4 통합 PASS 격상 entry brief** (55 entry, 24/52 entry entry brief 답습 동형 큰 cycle). 54 entry (γ-c) Layer 1+2+4 동시 채택 결정 발효 후 carry-over 5번.

본 cycle 발효 효과:
- Layer 1+2+4 통합 PASS 격상 *진입 권한* 발효
- 후속 실 구현 sub-cycle 진입 자격 발효
- (γ-c) 특화 의무 4 영구 답습 (Layer subsection 강제 + "부분 답습" framing 영구 + 통합 동시 + RT-γ-6)
- PASS evidence template *후보 채택* + Rollback Trigger 후보 채택

본 cycle 발효 *하지 않는 것*: Layer 1+2+4 통합 PASS *발효* 0 / 실 구현 0 / denyNonFastForwards 활성화 0 / R-6 actual run 0 / MVP-2 Implementation Evidence PASS 발효 0 / sub-수단 결정 0 / Layer 3+5 진입 결정 0 / R-S1 정정 0 / 자동 후속 진입 0 (총 30 금지).

## 검토 대상 (working directory 자료, codex 직접 read 의무)

PRIMARY:
- `docs/phase0/mvp2-layer-124-pass-entry-brief.md` (v1, 443줄, §0~§10)

직접 입력 자료:
- `docs/phase0/mvp2-gamma-decision-brief.md` (54 entry, 241줄, (γ-c) 채택 발효 답습 source)
- `docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md` (54 entry, 181줄, APPROVE)
- `docs/phase0/mvp2-gamma-layer-separation-brief.md` (53 entry v1.1, 522줄, (γ) 4 대안 답습)
- `docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md` (53 entry Reviewer 통합, 264줄)
- `docs/external-review/2026-05-28-mvp2-gamma-codex-response.md` (53 entry codex 응답)

선행 권위:
- `docs/architecture/provider-agnostic-memory-skill-design.md` (§4.4.1 line 629~660, Layer 1~5 PRIMARY)
- `docs/decisions/ADR-012-evidence-ledger-protection.md` (§2.3 + §2.5 + §2.7 + §2.8 + §3.4)
- `docs/decisions/ADR-011-means-vs-ends-redaction.md` (§2.1 (a)~(d) 4조건 모법 + §3 후속 (e))

실 repo PoC 시제 (filesystem direct 의무):
- `tools/jsonl_hash_chain.py` (14038B, genesis + 4 violation_type)
- `tools/canonical_json.py` (10055B)
- `tests/canonical/` (72 files / 8 카테고리)
- 4 G4 workflows (g4-hash-chain.yml 10652B + history-anchor-verifier.yml 19094B + rewrite-defense.yml 16454B + r2-canary.yml 5476B)
- `tests/fixtures/jsonl_ledger/{pass,fail}/` + `tests/fixtures/history_anchor_verifier/`
- ⚠️ `git config receive.denyNonFastForwards` 미설정 (Layer 2a evidence 별도 verify 의무)

## 검토 의무 (7 기준)

본 brief 의 PASS 격상 *진입 합의 input* 자격 평가:

1. **cross-vendor 충족 명시** (OpenAI codex / Anthropic Claude)

2. **본 brief v1 직접 읽기 evidence** (§X verbatim 인용)

3. **(γ-c) 특화 의무 4 답습 정확성** (54 entry §1.3 답습):
   - Layer subsection 강제 (§2 + §3 매트릭스 + §5.2 evidence template)
   - "부분 답습" framing 영구 (§2.1 + §6 + §0.3 #20)
   - 통합 동시 (§2.5 통합)
   - RT-γ-6 평가 (§5.1 + §8 #5)

4. **Layer 1+2+4 각 영역 PoC 시제 충족 자격 평가** (Layer 1 hash chain + Layer 2a denyNonFastForwards 미설정 + Layer 2b branch protection + Layer 4 4 G4 workflows + canonical test corpus 72 files)

5. **ADR-011 §2.1 (a)~(d) + (e) 매트릭스 (Layer 별 + 통합)** 평가

6. **Rollback Trigger / Evidence 후보 평가** (RT-γ-1/4/5/6 + RT-PASS-1/2/3 신규 + E-PASS-1~15 Layer subsection 강제)

7. ⚠️ **R-S1 후행 영향 RT-γ-6 평가 + MVP-2 PASS 시점 선행/동시 정정 사전조건 평가 의무** (53 entry N-5 + 54 entry §1.3 의무 4 답습)

## 판정 형식

- 총평: APPROVE / APPROVE WITH CONDITIONS / REVISE / REJECT
- BLOCKING N건 (R-1, R-2, ...)
- 권고 N건 (N-1, N-2, ...)
- NOTE N건 (필요 시)

## 응답 형식

응답 길이: ~250~400 줄. 한국어 + 영문 기술 용어 혼용. Markdown.

응답 구조:
- 검토자 / Vendor (cross-vendor 명시)
- 직접 검토한 working directory 자료 path
- §0 총평
- §1 BLOCKING N건
- §2 권고 N건
- §3 NOTE N건 (필요 시)
- §4 7 기준별 평가
- §5 (γ-c) 특화 의무 4 답습 정확성 평가
- §6 R-S1 RT-γ-6 평가 결과
- §7 PoC 시제 5 영역 cross-check

codex
요청하신 형식이 문서 기반 review라서 먼저 지정된 파일과 repo 상태를 직접 확인하겠습니다. 특히 primary brief의 실제 문구, ADR 조건, PoC 파일/테스트 corpus 수량, git config 상태를 함께 대조하겠습니다.
exec
/bin/bash -lc 'wc -l docs/phase0/mvp2-layer-124-pass-entry-brief.md docs/phase0/mvp2-gamma-decision-brief.md docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md docs/phase0/mvp2-gamma-layer-separation-brief.md docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md docs/external-review/2026-05-28-mvp2-gamma-codex-response.md docs/architecture/provider-agnostic-memory-skill-design.md docs/decisions/ADR-012-evidence-ledger-protection.md docs/decisions/ADR-011-means-vs-ends-redaction.md tools/jsonl_hash_chain.py tools/canonical_json.py' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
   443 docs/phase0/mvp2-layer-124-pass-entry-brief.md
   241 docs/phase0/mvp2-gamma-decision-brief.md
   181 docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md
   522 docs/phase0/mvp2-gamma-layer-separation-brief.md
   264 docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md
  3284 docs/external-review/2026-05-28-mvp2-gamma-codex-response.md
  1443 docs/architecture/provider-agnostic-memory-skill-design.md
   698 docs/decisions/ADR-012-evidence-ledger-protection.md
   290 docs/decisions/ADR-011-means-vs-ends-redaction.md
   397 tools/jsonl_hash_chain.py
   282 tools/canonical_json.py
  8045 total

exec
/bin/bash -lc 'rg -n "Layer 1|Layer 2|Layer 4|부분 답습|RT-γ-6|RT-PASS|E-PASS|denyNonFastForwards|Rollback|ADR-011|PASS|발효|진입|subsection|통합" docs/phase0/mvp2-layer-124-pass-entry-brief.md' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
1:# Layer 1+2+4 통합 PASS 격상 entry brief (v1)
3:> **작성**: 2026-05-28 (55번째 entry 진입 cycle)
5:> **scope**: G4 §4.4 Layer 1+2+4 통합 PASS 격상 진입 합의 ((γ-c) 채택 발효 답습)
7:> **본 cycle = 큰 cycle** (54 entry (γ-c) 채택 발효 후 carry-over 5번, 풀 3+1 + 외부 LLM 1+, 24/52 entry entry brief 답습 동형)
9:> **본 cycle 발효 자격** = **풀 3+1 합의 + 외부 LLM 1+ 응답 입력 (cross-vendor) + 사용자 명시 결정**
11:> **본 cycle 발효 효과** = Layer 1+2+4 통합 PASS 격상 진입 권한 발효 + 후속 실 구현 sub-cycle 진입 자격 발효 (evidence 평가 + (γ-c) 특화 의무 4 답습 + RT-γ-6 평가). 실 구현 + R-6 actual run + PASS 발효 = 별도 sub-cycle (본 cycle = 진입 합의 한정)
17:### §0.1 사용자 진입 명령 답습 (carry-over from 54 entry, commit `895a77b`)
20:- (α) ✅ **54 entry 발효** ((γ-c) Layer 1+2+4 동시 채택 결정 발효)
22:- **5번: Layer 1+2+4 통합 PASS 격상 cycle ((γ-c) 채택 발효 답습) — 풀 3+1 + 외부 LLM 1+, Layer subsection 강제 + "부분 답습" framing 영구 + RT-γ-6 답습**
24:본 cycle 진입 사용자 명시 (2026-05-28, 54 entry commit `895a77b` push 후) — "5번 Layer 1+2+4 통합 PASS 격상 진입". 본 brief = (γ-c) 채택 발효 답습 한정. (β) sub-수단 결정 + 실 구현 sub-cycle + MVP-2 PASS 발효 합의 = 별도 cycle.
28:1. **54 entry (γ-c) 채택 발효 답습** ((γ-c) 특화 의무 4 답습 cross-check) (§1)
29:2. **PoC 시제 충족 자격 평가** (Layer 1+2+4 각 영역별, 53 entry §2.5 + 본 cycle audit 답습) (§2)
30:3. **Layer 별 PASS 격상 영역 분석** — Layer 1 (hash chain) + Layer 2 (Git append-only, 2a local + 2b remote 분리) + Layer 4 (CI 회귀 검증) (§2)
31:4. **ADR-011 §2.1 (a)~(d) 4조건 모법 + (e) 후속 운영조건 매트릭스 (Layer 별 + 통합)** (§3, 52 entry B-2 framing 답습)
33:6. **(γ-c) 특화 의무 4 영구 답습** — Layer subsection 강제 + "부분 답습" framing + 통합 동시 + RT-γ-6 (§4.2)
35:8. **Rollback Trigger / Evidence *후보 채택*** (구현 발효 ≠ 본 합의, 52/53 entry N-1 답습) (§5)
36:9. **RT-γ-6 R-S1 PASS 시점 선행/동시 정정 평가** ((γ-c) 특화 의무 4 답습, §5.2 영구 의무) (§5)
38:11. **후속 실 구현 sub-cycle 진입 자격 명문** (§8)
48:| 5 | **`git config receive.denyNonFastForwards true` 활성화 실행** ⭐ (53 entry B-3 답습) | 0건 (활성화 = 별도 실 구현 sub-cycle 영역, 본 brief = evidence 평가 + 활성화 계획 권고 한정) |
52:| 9 | **G4 §4.4 Layer 4 sub-수단 결정** (L-1~L-5) | 0건 ((β) 별도 cycle) |
53:| 10 | **W 통합 결정** (W-A~E) | 0건 ((β) 별도 cycle) |
57:| 14 | **Layer 1+2+4 통합 PASS 발효** ⭐ | 0건 (본 cycle = 진입 합의, PASS 발효 = 실 구현 + (a)~(d) evidence + (e) 합의 APPROVE + 사용자 명시 후 별도 합의) |
58:| 15 | **MVP-2 Implementation Evidence PASS 발효** | 0건 (Layer 통합 PASS + GP-2 PASS + 통합 합의 후 별도) |
59:| 16 | **MVP-1 PASS 재선언** | 0건 (32 entry 답습 유지) |
60:| 17 | Operational Readiness PASS / Hermes PMO 격상 | 0건 |
63:| 20 | G4 §4.4 Layer 3 (Signed commit) + Layer 5 (External anchor) 영역 진입 결정 | 0건 ((γ-c) "부분 답습" framing 영구 답습, 54 entry §1.3 의무 2) |
64:| 21 | (γ-a/b/d) 대안 재평가 | 0건 (54 entry (γ-c) 채택 결정 영구 발효 답습) |
66:| 23 | R-S1 cross-reference 정정 자동 진입 (ADR-012 §2.3 vs §2.8) | 0건 (별도 cycle, RT-γ-6 답습 — 단, 본 cycle = PASS 시점 선행/동시 정정 *평가* 의무) |
69:| 26 | 자동 후속 실 구현 sub-cycle 진입 | 0건 (사용자 명시 의무) |
70:| 27 | Layer 4 PASS 선발효 (Layer 1+2 PASS 부재 시, (γ-d) 모순 답습) | 0건 (영구 금지, 54 entry §5 #3 답습) |
71:| 28 | Layer 4 evidence 內 Layer 1+2 evidence 합산 (Layer subsection 미준수) | 0건 ((γ-c) 특화 의무 1 영구 답습, 54 entry §5 #9) |
77:- ✅ 본 brief 발효 자격 = **풀 3+1 합의 + 외부 LLM 1+ 응답 입력 (cross-vendor) + 사용자 명시 결정**
78:- ✅ 본 brief 발효 결과:
79:  1. Layer 1+2+4 통합 PASS 격상 *진입 권한 발효*
80:  2. 후속 실 구현 sub-cycle 진입 자격 발효
81:  3. (γ-c) 특화 의무 4 답습 영구 보존 (Layer subsection 강제 + "부분 답습" framing + 통합 동시 + RT-γ-6)
82:  4. PASS evidence template *후보 채택* (Layer 1/2/4 subsection 분리 강제)
83:  5. Rollback Trigger / Evidence 후보 채택
84:- ❌ 본 brief 자체에서 Layer 1+2+4 통합 PASS *발효* 0건 (실 구현 + (a)~(d) evidence + (e) 합의 APPROVE 후 별도)
86:- ❌ 본 brief 자체에서 실 구현 0건 (denyNonFastForwards 활성화 0 / R-6 actual run 0)
87:- ❌ 본 brief 자체에서 MVP-2 Implementation Evidence PASS 발효 0건
88:- ❌ 본 brief 자체에서 R-S1 cross-reference 정정 0건 (RT-γ-6 평가 한정, 정정 = 별도 cycle)
89:- ❌ 본 brief 자체에서 ADR-011 §2.1 (a)~(d) 4조건 자동 충족 선언 0건
90:- ⚠️ 본 brief 합의 후 *자동 실 구현 sub-cycle 진입 금지* — 사용자 명시 결정 의무
94:## §1 진입 컨텍스트 답습
100:| 54 entry decision brief + 1-agent 직접 합의 (`895a77b` 발효) — (γ-c) Layer 1+2+4 동시 채택 결정 발효 | 본 brief 의 **직접 입력 자료** (54 entry §1.3 (γ-c) 특화 의무 4 답습 source) |
101:| 53 entry (γ) brief v1.1 + Reviewer 통합 합의 — 4 source consensus + R-S1 5 source verify CONFIRMED | 4 source consensus 권고 답습 (Reviewer 통합 (γ-c) 1순위) + R-S1 후행 영향 RT-γ-6 답습 source |
102:| 52 entry (α) entry brief v1.1 + Reviewer 통합 합의 — MVP-2 진입 권한 발효 | MVP-2 영역 (GP-2 + G4 §4.4 Layer 4) 진입 권한 발효 답습 |
103:| 32 entry MVP-1 Implementation Evidence PASS *완전 발효 (α)* | MVP-1 PASS 답습 그대로 유지 (재선언 0). MVP-2 PASS = Layer 통합 PASS + GP-2 PASS + 통합 합의 후 별도 |
104:| `provider-agnostic-memory-skill-design.md §4.4.1 line 629~660` (PRIMARY, 5-layer) | Layer 1~5 정의 |
108:| `ADR-012 §3.4` (timestamp monotonicity) | RT-γ-6 답습 |
110:| `ADR-011 §2.1 (a)~(d) 4조건 모법 + (e) 후속 운영조건` (52 entry B-2 답습) | 5조건 매트릭스 §3 |
117:| 1 | PASS evidence template Layer 1/Layer 2/Layer 4 subsection 강제 | §2 Layer 별 분리 분석 + §3 매트릭스 Layer 별 컬럼 + §5.2 evidence template 후보 (Layer subsection 강제) |
118:| 2 | "defense-in-depth 부분 답습" framing 영구 유지 (Layer 3+5 = scope 외) | §0.3 #20 명시 + §2.1 영역 정의 "부분 답습" 표현 사용 + §6 #6 영구 답습 |
119:| 3 | Layer 1+2+4 통합 PASS evidence 동시 발효 | §2.4 통합 영역 + §3 통합 매트릭스 + §4.2 통합 발효 |
120:| 4 | RT-γ-6 R-S1 PASS 시점 선행/동시 정정 평가 의무 | §5.2 RT-γ-6 평가 + §8 다음 단계 #5 명문 |
135:| **`git config receive.denyNonFastForwards`** ⭐ | ⚠️ **미설정** (local + global 모두 출력 0건) — 53 entry B-3 답습 (Layer 2a local workflow evidence 별도 verify 의무) | 53 entry B-3 답습 — 본 cycle = 활성화 evidence 별도 verify 의무 명문 + 실 구현 sub-cycle 활성화 의무 |
139:→ **PoC 시제 전 영역 충족 (Layer 2a denyNonFastForwards 1 영역 미설정 = 실 구현 sub-cycle 활성화 의무)**. tests/canonical 24 fixture 정량 = 본 cycle audit 직접 verify 완료 (72 files / 8 × 3 × 3, 52 entry Agent A R-A-2 carry-over 해소).
143:## §2 Layer 별 PASS 격상 영역 분석
145:### §2.1 영역 정의 ((γ-c) 특화 의무 2 답습 — "부분 답습" framing)
147:본 brief = **G4 §4.4 Layer 1+2+4 통합 *부분 답습*** (Layer 3 Signed commit + Layer 5 External anchor = 본 cycle scope 외, 별도 cycle 영역, 54 entry §1.3 의무 2 영구 답습).
149:### §2.2 Layer 1 — Hash Chain (MANDATORY)
155:| **PASS 격상 영역** | (a) hash chain 검증 PoC PASS (middle tampering 차단 PoC, Docker 격리) + (b) canonical JSON sha256 동등성 검증 + (c) genesis hash 첫 entry 작성 evidence + (d) Layer 4 CI step 內 hash chain 검증 actual run PASS |
157:| **violation_type Layer 매핑** (53 entry N-6 답습) | PREV_HASH_MISMATCH + HASH_RECALCULATION + GENESIS_MISMATCH = Layer 1 |
159:### §2.3 Layer 2 — Git Append-only Branch (MANDATORY, 2a + 2b 분리, 53 entry B-3 답습)
161:#### §2.3.1 Layer 2a — local workflow
165:| **PoC 시제** | ⚠️ **`git config receive.denyNonFastForwards` 미설정** (local + global 모두 0건 verify, 본 cycle §1.3 답습) — Layer 2a evidence 별도 verify 의무 |
167:| **PASS 격상 영역** | (a) `git config --system receive.denyNonFastForwards true` 활성화 + entrypoint 또는 pre-receive hook 강제 + (b) Docker 격리 PoC (force-push 시도 → reject) + (c) Layer 4 CI step base branch 대비 JSONL line deletion / rewrite 감지 actual run PASS |
169:| **실 구현 sub-cycle 의무** | denyNonFastForwards 활성화 = 본 cycle scope 외, 실 구현 sub-cycle 영역 (별도 사용자 명시) |
170:| **violation_type Layer 매핑** (53 entry N-6 답습) | HISTORY_REWRITE = Layer 2 |
172:#### §2.3.2 Layer 2b — remote / admin
178:| **PASS 격상 영역** | (a) main branch protection 8 contexts + force push/delete false + required_approving_review_count + (b) admin scope 신규 contexts 추가 (사용자 영역) |
181:### §2.4 Layer 4 — CI 회귀 검증 (MANDATORY)
187:| **PASS 격상 영역** | (a) Layer 1 (hash chain) 자동 회귀 검증 + Layer 2 (history) 자동 회귀 검증 + (b) canonical JSON 위반 검출 (RFC 8785 reference 동등성) + (c) timestamp monotonicity 검증 (ADR-012 §3.4) + (d) R-6 workflow 답습 확장 step (사용자 결정 영역, W-A/B/C/D/E 中 결정 = (β) 별도 cycle, 53 entry §2.3.2 답습) |
191:### §2.5 통합 PASS 격상 ((γ-c) 특화 의무 3 답습 — 통합 동시 발효)
193:본 (γ-c) 채택 발효 답습 — Layer 1+2+4 **통합** PASS evidence 동시 발효 의무 (54 entry §1.3 의무 3 영구 답습):
195:| 통합 영역 | evidence template ((γ-c) 특화 의무 1 답습 — Layer subsection 강제) |
197:| Layer 1 evidence subsection | hash chain 검증 PoC PASS + 4 violation_type 검출 actual run + canonical JSON sha256 동등성 |
198:| Layer 2a evidence subsection | denyNonFastForwards 활성화 evidence + Docker 격리 PoC (force-push reject) + JSONL line deletion / rewrite 감지 actual run |
199:| Layer 2b evidence subsection | branch protection rule actual state (43 entry 8 contexts + force push/delete false) |
200:| Layer 4 evidence subsection | 4 G4 workflow actual run PASS + canonical 위반 BLOCK + timestamp monotonicity 위반 BLOCK + R-6 workflow 통합 step (W 결정 답습) |
201:| 통합 evidence subsection | Layer 1+2+4 동시 actual run PASS evidence (Layer evidence 합산 금지, 54 entry §1.3 의무 1 영구 답습) |
203:⚠️ **Layer 4 evidence 內 Layer 1+2 evidence 합산 영구 금지** (54 entry §5 #9 답습).
205:### §2.6 본 cycle 합의 발효 시 채택 결정 영역
207:✅ **Layer 1+2+4 통합 PASS 격상 진입 발효 자격** — 본 cycle 합의 APPROVE 시점 발효
208:✅ **후속 실 구현 sub-cycle 진입 자격 발효** — denyNonFastForwards 활성화 + R-6 workflow 확장 step + actual run PASS evidence 수집 sub-cycle (별도 사용자 명시)
209:✅ **PASS evidence template *후보 채택*** (Layer subsection 강제, 구현 발효 ≠ 본 합의)
210:✅ **Rollback Trigger 본문 *후보 채택*** (§5.1 답습, RT-γ-1~6 + RT-PASS-1~3 신규)
211:✅ **(γ-c) 특화 의무 4 영구 답습 보존** (Layer subsection 강제 + "부분 답습" framing + 통합 동시 + RT-γ-6)
212:✅ **RT-γ-6 R-S1 PASS 시점 선행/동시 정정 *평가*** (정정 자체 = 별도 cycle)
214:### §2.7 미발효 영역 (deferred)
216:❌ Layer 1+2+4 통합 PASS 발효 자체 = 실 구현 + (a)~(d) evidence + (e) 합의 APPROVE + 사용자 명시 후 별도
217:❌ MVP-2 Implementation Evidence PASS 발효 = Layer 통합 PASS + GP-2 PASS + 통합 합의 후 별도
219:❌ Layer 3 + Layer 5 영역 진입 = "부분 답습" framing 영구 답습 (54 entry §1.3 의무 2)
220:❌ R-S1 cross-reference 정정 자체 = 별도 cycle (RT-γ-6 평가 한정)
224:## §3 ADR-011 §2.1 (a)~(d) 4조건 모법 + (e) 후속 운영조건 — 5조건 매트릭스 (Layer 별 + 통합, 52 entry B-2 framing 답습)
226:| # | 조건 | Layer 1 | Layer 2 (2a+2b) | Layer 4 | 통합 |
228:| (a) | 동등 이상 보안 결과 | hash chain middle tampering 차단 (PoC 시제 충족) | 2a force-push 차단 + 2b branch protection / history 재작성 차단 (2a 미설정 verify 의무) | CI 회귀 검증 (Layer 1+2 통합 회귀, PoC 시제 충족) | Layer 1+2+4 통합 (각 subsection 분리) |
229:| (b) | 격리 환경 PoC 실증 | ✅ tools/jsonl_hash_chain.py + fixtures (PoC 시제 충족) | 2a ⚠️ denyNonFastForwards 활성화 + Docker 격리 PoC (실 구현 sub-cycle 의무) / 2b ✅ branch protection 답습 | ✅ 4 G4 workflow PoC 시제 충족 + R-6 actual run (실 구현 sub-cycle 의무) | 통합 evidence (Layer subsection 분리 강제) |
231:| (d) | 자동 회귀 검증 경로 확보 | Layer 4 CI step 內 hash chain 검증 (R-6 workflow 답습) | Layer 4 CI step 內 base branch JSONL line deletion / rewrite 감지 | R-6 workflow 답습 확장 step (W 결정 = (β) 영역) | 통합 R-6 확장 step |
232:| (e) | 합의 APPROVE | ❌ gap — 본 cycle (α) 진입 합의 → 발효 ≠ 본 cycle (Layer 통합 PASS 발효 = 별도) | ❌ 동상 | ❌ 동상 | ❌ 동상 |
234:→ **본 cycle (e) = 진입 *권한* 충족 (Layer 통합 PASS 발효 ≠ 본 합의, 별도 합의)**.
236:→ **PoC 시제 충족 영역 = (a)+(b)+(c)+(d) 부분 충족**. PASS 시제 = 실 구현 sub-cycle (denyNonFastForwards 활성화 + R-6 actual run + evidence 수집) 후 (e) 통합 PASS 발효 합의.
247:1. 53 entry brief §8.1 항목 3 + 54 entry SESSION carry-over #5 — "Layer 1+2+4 통합 PASS 격상 cycle = 풀 3+1 + 외부 LLM 1+" 직접 답습
248:2. (γ-c) 채택 발효 답습 (54 entry) — 큰 결정 (PASS 격상 진입 발효 = MVP-2 Implementation Evidence PASS 발효 *직전 단계*)
249:3. 32 entry MVP-1 PASS 발효 합의 답습 패턴 (풀 3+1 + 외부 LLM 1+)
252:6. ADR-011 §2.1 (e) + §2.4 T3 영역
256:본 cycle = (γ-c) 채택 발효 답습 한정. 특화 의무 4 영구 보존:
260:| 1 | PASS evidence template Layer 1/Layer 2/Layer 4 subsection 강제 | §2 Layer 별 분리 + §3 매트릭스 Layer 별 컬럼 + §5.2 evidence template 후보 (Layer subsection 강제) |
261:| 2 | "defense-in-depth 부분 답습" framing 영구 유지 (Layer 3+5 = scope 외) | §2.1 + §6 영구 답습 + §0.3 #20 명시 금지 |
262:| 3 | Layer 1+2+4 통합 PASS evidence 동시 발효 | §2.5 통합 영역 + §3 통합 매트릭스 |
263:| 4 | RT-γ-6 R-S1 PASS 시점 선행/동시 정정 평가 의무 | §5.2 평가 + §8 #5 명문 |
269:| 1 | 큰 결정 (PASS 격상 진입 발효 / sub-수단 결정 / threshold 고정) | ✅ **발화** | Layer 1+2+4 통합 PASS 격상 *진입* 합의 = MVP-2 PASS 발효 *직전 단계* (큰 영역) |
272:| 4 | 권위 chain 다중 source 손상 위험 | ⚠️ **부분 발화** (R-S1 후행 영향 RT-γ-6, 52/53 entry 발견 cascade) | 본 cycle = 후행 영향 평가 한정, 정정 = 별도 cycle |
273:| 5 | 외부 LLM 응답 통합 필요성 | ✅ **발화** | 큰 결정 + cross-vendor 의무 (53/54 entry 답습) |
281:## §5 Rollback Trigger / Evidence *후보 채택* (구현 발효 ≠ 본 합의, 52/53 entry N-1 답습)
283:### §5.1 Rollback Trigger 본문 후보 (53 entry §5.1 답습 + 본 cycle 신규)
287:| RT-γ-1 | Layer 1+2 PoC 시제 회귀 | 모든 | tools/* 본문 변경 시 PoC 시제 미작동 | 후속 sub-cycle | 53 entry §5.1 답습 |
288:| RT-γ-4 | Layer 1 violation_type 검출 실패 | Layer 1 | PREV_HASH_MISMATCH + HASH_RECALCULATION + GENESIS_MISMATCH 미작동 | 실 구현 sub-cycle | 53 entry N-6 답습 |
289:| RT-γ-5 | (γ-d) Layer 4 PASS 선발효 시도 (영구 금지 위반) | (γ-d) 비채택 답습 | Layer 4 PASS 발효 + Layer 1+2 미발효 | 영구 금지 (54 entry §5 #3 답습) | 53 entry §2.4.5 + B-1 답습 |
290:| RT-γ-6 | R-S1 cross-reference 정정 후행 영향 + **MVP-2 PASS 시점 선행/동시 정정 평가** | 모든 (γ-c 특화 의무 4 답습) | ADR-012 §2.3 본문 정정 + MVP-2 Implementation Evidence PASS 발효 시점 R-S1 정정 사전조건 평가 | 본 cycle + Layer 통합 PASS 발효 + MVP-2 PASS 발효 | 52 entry §9.5 + 53 entry §5.1 + 54 entry §1.3 의무 4 답습 |
291:| **RT-PASS-1** ⭐ (신규) | denyNonFastForwards 활성화 실패 | Layer 2a | 실 구현 sub-cycle 활성화 후 force-push 시도 reject 실패 | 실 구현 sub-cycle | 53 entry B-3 + 본 brief §1.3 audit 답습 |
292:| **RT-PASS-2** ⭐ (신규) | Layer 4 evidence 內 Layer 1+2 evidence 합산 (subsection 미준수) | (γ-c) 특화 의무 1 위반 | PASS evidence template Layer subsection 분리 미준수 | Layer 통합 PASS 발효 시점 | 54 entry §1.3 의무 1 + §5 #9 답습 |
293:| **RT-PASS-3** ⭐ (신규) | "defense-in-depth 충실 답습" 또는 "완전 답습" 표현 사용 | (γ-c) 특화 의무 2 위반 | Layer 3+5 scope 외 framing 영구 위반 | 본 cycle 후 모든 시점 | 54 entry §1.3 의무 2 + §5 #8 답습 |
295:### §5.2 Evidence Required (Layer subsection 강제, (γ-c) 특화 의무 1 답습)
297:| # | Evidence | Layer subsection | 출처 |
299:| E-PASS-1 | hash chain 검증 PoC PASS evidence | Layer 1 | Docker 격리 PoC (middle tampering 차단) |
300:| E-PASS-2 | 4 violation_type 검출 actual run evidence | Layer 1 | tools/jsonl_hash_chain.py + fixtures |
301:| E-PASS-3 | canonical JSON sha256 동등성 evidence | Layer 1 | canonical_json.py + tests/canonical/ 72 files |
302:| E-PASS-4 | genesis hash 첫 entry actual evidence | Layer 1 | jsonl_hash_chain.py + audit log |
303:| E-PASS-5 | denyNonFastForwards 활성화 evidence | Layer 2a | git config + Docker 격리 PoC (force-push reject) |
304:| E-PASS-6 | base branch JSONL line deletion / rewrite 감지 evidence | Layer 2 | Layer 4 CI step actual run |
305:| E-PASS-7 | branch protection rule actual state | Layer 2b | gh api (43 entry 8 contexts 답습) |
306:| E-PASS-8 | 4 G4 workflow actual run PASS evidence | Layer 4 | GitHub Actions run ID + verdict PASS (42 entry actual run id `25623028888` 답습, 52 entry N-6 답습) |
307:| E-PASS-9 | canonical 위반 BLOCK PoC | Layer 4 | Docker 격리 + RFC 8785 reference mismatch |
308:| E-PASS-10 | timestamp monotonicity 위반 BLOCK PoC | Layer 4 | Docker 격리 + ADR-012 §3.4 답습 |
309:| E-PASS-11 | R-6 workflow 확장 step actual run PASS (W 결정 답습) | Layer 4 | (β) sub-수단 결정 cycle 후 |
310:| E-PASS-12 | 통합 evidence (Layer subsection 분리 명시) | 통합 | 본 cycle PASS evidence template (Layer subsection 강제, (γ-c) 특화 의무 1) |
311:| E-PASS-13 | 합의 보고서 commit | 통합 | 본 cycle Reviewer 통합 + 후속 PASS 발효 합의 |
312:| E-PASS-14 | 외부 LLM 1+ 응답 (cross-vendor) | 통합 | `docs/external-review/2026-05-28-mvp2-layer-124-pass-*.md` |
313:| E-PASS-15 ⭐ (RT-γ-6 답습) | R-S1 cross-reference 정정 사전조건 평가 evidence | 통합 | ADR-012 §2.3 vs §2.8 정정 cycle 진행 상태 + MVP-2 PASS 시점 선행/동시 의무 평가 |
323:### §6.2 본 brief 발효 후 후속 cycle 진입 시점 금지 사항
327:| 1 | 자동 후속 실 구현 sub-cycle 진입 | 사용자 명시 의무 |
328:| 2 | 자동 (β) sub-수단 결정 cycle 진입 | 사용자 명시 의무 |
329:| 3 | Layer 4 PASS 선발효 ((γ-d) 모순, RT-γ-5) | 영구 금지 (54 entry §5 #3 답습) |
330:| 4 | Layer 4 evidence 內 Layer 1+2 evidence 합산 (Layer subsection 미준수, RT-PASS-2) | 영구 금지 ((γ-c) 특화 의무 1, 54 entry §5 #9 답습) |
331:| 5 | "defense-in-depth 충실 답습" / "완전 답습" 표현 (RT-PASS-3) | 영구 금지 ((γ-c) 특화 의무 2, 54 entry §5 #8 답습) |
332:| 6 | Layer 3 (Signed commit) + Layer 5 (External anchor) 자동 진입 | "부분 답습" framing 영구 답습, 별도 cycle |
333:| 7 | (γ-a/b/d) 대안 재평가 자동 진입 | 54 entry (γ-c) 채택 결정 영구 발효 답습 |
334:| 8 | MVP-2 Implementation Evidence PASS 자동 선언 | 실 구현 + (a)~(d) evidence + (e) 합의 APPROVE + 사용자 명시 + R-S1 RT-γ-6 평가 후 별도 |
335:| 9 | R-S1 cross-reference 정정 자동 진입 | 별도 cycle (RT-γ-6 평가 한정) |
347:3. ADR-011 §2.1 (a)~(d) + (e) + §2.4 T3 영역
364:| 53 entry (γ) brief v1.1 + Reviewer 통합 합의 + codex 응답 | `docs/phase0/mvp2-gamma-layer-separation-brief.md` + `docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md` + `docs/external-review/2026-05-28-mvp2-gamma-codex-response.md` |
365:| 52 entry (α) entry brief v1.1 + Reviewer 통합 합의 | `docs/phase0/mvp2-entry-brief.md` + `docs/review/3plus1-consensus-2026-05-28-mvp2-entry.md` |
368:| **`ADR-011 §2.1` + `PROJECT_CONSTITUTION` (헌법 8조 + 5조-2)** (52 entry N-11 답습) | 답습 source |
372:## §8 다음 단계 (사용자 결정 영역 — 자동 진입 0건)
374:본 cycle 합의 APPROVE 발효 후 (사용자 명시 의무):
377:2. **실 구현 sub-cycle** — denyNonFastForwards 활성화 + R-6 workflow 확장 step 통합 + evidence 수집 (E-PASS-1~14) — 수단별 차등
378:3. **Layer 1+2+4 통합 PASS 발효 합의** — (a)~(d) evidence + (e) 합의 APPROVE + 사용자 명시 (32 entry 답습)
379:4. **MVP-2 Implementation Evidence PASS 발효 합의** — Layer 통합 PASS + GP-2 PASS + 통합 합의 (32 entry 답습)
380:5. ⭐ **R-S1 cross-reference 정정 cycle** — ADR-012 §2.3 본문 정정 또는 §2.8 동형 답습 강화 (RT-γ-6 답습 + MVP-2 PASS 시점 선행/동시 의무 평가 후)
384:본 brief 합의는 다음 단계 진입을 *발생시키지 않음* — 사용자 명시 의무.
394:- ADR-011 §2.1 (a)~(d) 4조건 모법 + §3 후속 권위 (e) — `docs/decisions/ADR-011-means-vs-ends-redaction.md`
398:- 54 entry decision brief + 1-agent 직접 합의 ((γ-c) 채택 발효 답습 source)
399:- 53 entry (γ) brief v1.1 + Reviewer 통합 합의 + codex 응답
400:- 52 entry (α) entry brief v1.1 + Reviewer 통합 합의
401:- 32 entry MVP-1 PASS 발효 합의
414:- ⚠️ `git config receive.denyNonFastForwards` 미설정 (실 구현 sub-cycle 활성화 의무, B-3 답습)
418:- Layer 1+2+4 통합 PASS evidence template (Layer subsection 강제, (γ-c) 특화 의무 1 답습)
419:- R-S1 cross-reference 정정 (52/53 entry §9.5 + RT-γ-6 + MVP-2 PASS 시점 선행/동시 평가)
422:- ADR-011 §8.5 후속 작업에 Layer 통합 PASS 등록
430:| P-1 | 본 brief 가 PASS 격상 진입을 *권유* 방향으로 편향 | §0.3 + §6.2 30+11 금지 + §0.4 권위 한계 = "본 brief 자체에서 PASS 발효 0" 영구 분리 |
431:| P-2 | (γ-c) 특화 의무 4 영구 답습 강조가 결정 영역 침입 risk | §1.2 + §4.2 = 54 entry §1.3 답습 한정 (Reviewer 통합 권고 답습 + 1-agent 직접 합의 발효 답습) |
432:| P-3 | PoC 시제 충족 발견 (§1.3 + §2.5) 이 PASS 발효 단순화 risk | §2.7 + §3 (e) gap 명시 + §6.2 #8 "MVP-2 PASS 자동 선언 금지" 영구 답습 |
433:| P-4 | denyNonFastForwards 미설정 발견 (§1.3) 이 실 구현 자동 진입 risk | §6.2 #1 명시 + §0.3 #5 명시 (활성화 = 실 구현 sub-cycle 영역, 본 cycle scope 외) |
434:| P-5 | RT-γ-6 R-S1 후행 영향 평가가 본 cycle 결정 영향 | §5.1 RT-γ-6 명시 + §9.4 = 별도 cycle 영역 답습 + 본 cycle = *평가* 한정 (정정 ≠ 본 cycle) |
436:| P-7 | 본 brief 작성자 = 52/53/54 entry brief 작성자 (Claude Opus 4.7) → cascade risk | §1.1 선행 권위 답습 + §1.2 (γ-c) 특화 의무 4 답습 = 54 entry 답습 한정 (Reviewer 통합 권고 + 1-agent 직접 합의 발효 답습 보존). 본 brief = 답습 cascade 정합성 검증 + cross-vendor 후속 합의 시 codex (E-α) 호출 답습 (53 entry 답습, cross-vendor 형식 충족) |
443:**다음 단계**: 사용자 승인 + 외부 LLM 자격 옵션 결정 (§7.2) → 외부 LLM 호출 + Agent A/B/C 3 병렬 launch → Reviewer 통합 합의 → brief v1.1 1pass 흡수 → SESSION + INDEX commit + push (55 entry).

exec
/bin/bash -lc 'find tests/canonical -type f | wc -l && find tests/canonical -maxdepth 2 -type f | sort && find tests/fixtures/jsonl_ledger -type f | sort && find tests/fixtures/history_anchor_verifier -type f | sort' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
72
tests/canonical/array/01.expected.canonical
tests/canonical/array/01.expected.sha256
tests/canonical/array/01.input.json
tests/canonical/array/02.expected.canonical
tests/canonical/array/02.expected.sha256
tests/canonical/array/02.input.json
tests/canonical/array/03.expected.canonical
tests/canonical/array/03.expected.sha256
tests/canonical/array/03.input.json
tests/canonical/escape/01.expected.canonical
tests/canonical/escape/01.expected.sha256
tests/canonical/escape/01.input.json
tests/canonical/escape/02.expected.canonical
tests/canonical/escape/02.expected.sha256
tests/canonical/escape/02.input.json
tests/canonical/escape/03.expected.canonical
tests/canonical/escape/03.expected.sha256
tests/canonical/escape/03.input.json
tests/canonical/hash_stability/01.expected.canonical
tests/canonical/hash_stability/01.expected.sha256
tests/canonical/hash_stability/01.input.json
tests/canonical/hash_stability/02.expected.canonical
tests/canonical/hash_stability/02.expected.sha256
tests/canonical/hash_stability/02.input.json
tests/canonical/hash_stability/03.expected.canonical
tests/canonical/hash_stability/03.expected.sha256
tests/canonical/hash_stability/03.input.json
tests/canonical/key_ordering/01.expected.canonical
tests/canonical/key_ordering/01.expected.sha256
tests/canonical/key_ordering/01.input.json
tests/canonical/key_ordering/02.expected.canonical
tests/canonical/key_ordering/02.expected.sha256
tests/canonical/key_ordering/02.input.json
tests/canonical/key_ordering/03.expected.canonical
tests/canonical/key_ordering/03.expected.sha256
tests/canonical/key_ordering/03.input.json
tests/canonical/lossy/01.expected.canonical
tests/canonical/lossy/01.expected.sha256
tests/canonical/lossy/01.input.json
tests/canonical/lossy/02.expected.canonical
tests/canonical/lossy/02.expected.sha256
tests/canonical/lossy/02.input.json
tests/canonical/lossy/03.expected.canonical
tests/canonical/lossy/03.expected.sha256
tests/canonical/lossy/03.input.json
tests/canonical/nested/01.expected.canonical
tests/canonical/nested/01.expected.sha256
tests/canonical/nested/01.input.json
tests/canonical/nested/02.expected.canonical
tests/canonical/nested/02.expected.sha256
tests/canonical/nested/02.input.json
tests/canonical/nested/03.expected.canonical
tests/canonical/nested/03.expected.sha256
tests/canonical/nested/03.input.json
tests/canonical/number/01.expected.canonical
tests/canonical/number/01.expected.sha256
tests/canonical/number/01.input.json
tests/canonical/number/02.expected.canonical
tests/canonical/number/02.expected.sha256
tests/canonical/number/02.input.json
tests/canonical/number/03.expected.canonical
tests/canonical/number/03.expected.sha256
tests/canonical/number/03.input.json
tests/canonical/unicode/01.expected.canonical
tests/canonical/unicode/01.expected.sha256
tests/canonical/unicode/01.input.json
tests/canonical/unicode/02.expected.canonical
tests/canonical/unicode/02.expected.sha256
tests/canonical/unicode/02.input.json
tests/canonical/unicode/03.expected.canonical
tests/canonical/unicode/03.expected.sha256
tests/canonical/unicode/03.input.json
tests/fixtures/jsonl_ledger/fail/genesis_mismatch.jsonl
tests/fixtures/jsonl_ledger/fail/hash_recalculation.jsonl
tests/fixtures/jsonl_ledger/fail/missing_event_field.jsonl
tests/fixtures/jsonl_ledger/fail/prev_hash_mismatch.jsonl
tests/fixtures/jsonl_ledger/pass/minimal_chain.jsonl
tests/fixtures/jsonl_ledger/pass/roundtrip_t2_strict.jsonl
tests/fixtures/history_anchor_verifier/chain_only_demo/full_rewrite_ledger.jsonl
tests/fixtures/history_anchor_verifier/fail/anchor_full_rewrite.json
tests/fixtures/history_anchor_verifier/fail/anchor_middle_deletion.json
tests/fixtures/history_anchor_verifier/fail/anchor_substitution.json
tests/fixtures/history_anchor_verifier/fail/anchor_tail_truncation.json
tests/fixtures/history_anchor_verifier/fail/anchor_tampered.json
tests/fixtures/history_anchor_verifier/fail/full_rewrite_ledger.jsonl
tests/fixtures/history_anchor_verifier/fail/middle_deletion_ledger.jsonl
tests/fixtures/history_anchor_verifier/fail/substitution_ledger.jsonl
tests/fixtures/history_anchor_verifier/fail/tail_truncation_ledger.jsonl
tests/fixtures/history_anchor_verifier/pass/extended_anchor.json
tests/fixtures/history_anchor_verifier/pass/extended_ledger.jsonl
tests/fixtures/history_anchor_verifier/pass/original_anchor.json
tests/fixtures/history_anchor_verifier/pass/original_ledger.jsonl

exec
/bin/bash -lc "git config --get receive.denyNonFastForwards; printf 'exit=%s\\n' "'$?' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
exit=1

codex
Primary brief의 핵심 문구와 repo 수량은 확인됐습니다. 이제 선행 권위 문서에서 Layer 정의, ADR-011 조건, ADR-012 R-S1 관련 조항이 brief의 해석과 맞는지 직접 대조하겠습니다.
exec
/bin/bash -lc "sed -n '620,665p' docs/architecture/provider-agnostic-memory-skill-design.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:

**P-3 흡수 완료** (2026-05-11): G4 DRAFT 검토 §3.1 P-3 (자기 발견 잠재 위험 — "§4.5 외부 형식 → 본 G4 import 시 schema_version 호환성 (§4.3 #3) — 호환 부재 시 처리 절차 부재") 흡수 완료. **schema_version declaration 절차 = T2 사용자 명시 승인 + §10.2 합의 절차 + §4.5.3 정밀 import 검증 단계**. 본 절차 충족 *전* import = BLOCK (§4.6.5 #1~#3 답습).

### 4.4 Hash Chain 변조 방지 (**ADR-012 §2.3 + §2.5 + §2.6 + §2.7 + §2.8 답습 — 2026-05-09 PR-2 풀 3+1 합의 보강 + 2026-05-11 P-1 흡수 완료**)

> **ADR-012 §2.3~§2.8 갱신**: 본 §4.4 = ADR-012 §2.3 (Append-only + Hash Chain 다층 강제) + §2.5 (RFC 8785 JCS) + §2.6 (Genesis Hash) + §2.7 (prev_hash 검증 실패 처리) + §2.8 (Full Rewrite 방어) 답습. 이전 (보강 전) "둘 중 하나 의무" 약 사양 → 다층 강제 사양 + canonical JSON 표준 인용 + 실패 처리 + full rewrite 방어 명시.
>
> **P-1 흡수 완료** (2026-05-11): G4 DRAFT 검토 §3.1 P-1 (자기 발견 잠재 위험 — "JSON canonicalization 표준은 RFC 8785 (JCS) 등 명시 표준 존재. 본 초안은 JCS 직접 인용 안 함") 흡수 완료. **canonical JSON 표준 = RFC 8785 (JCS) IETF informational track 명시 인용** — §4.4.2 Primary 정의 + ADR-012 §2.5 권위. 본 §4.4 의 모든 hash 계산은 RFC 8785 (https://www.rfc-editor.org/rfc/rfc8785) 기준 canonical 형식에 SHA-256 적용. fallback (RFC 8259 escape + lex sort + `jq -S -c` 등) 은 RFC 8785 reference output 동등성 의무 (§4.4.2 답습).

#### 4.4.1 다층 강제 (Layer 1 ~ Layer 5)

**Layer 1 — Hash Chain (MANDATORY 모든 환경)**:
- `prev_hash` = 직전 entry 의 `hash` (chain 형성)
- `hash` = 본 entry 의 canonical JSON sha256
- 첫 entry 의 `prev_hash` = `genesis_hash` (§4.4.3)
- SHA-256 hardcode (schema_version 0.1) — `hash_algo` 필드 후속 격상 영역 (ADR-012 §3.2 답습)
- JSONL append-only — entry 수정 / 삭제 / 재작성 금지 (T3 영역, ADR-011 §2.4)

**Layer 2 — Git Append-only Branch (MANDATORY)**:
- `git config receive.denyNonFastForwards true` (force-push 차단)
- branch protection rule
- pre-commit hook: `git rebase` / `git filter-branch` / `git reset --hard` 감지 시 reject (T3 자동 *방어* 권한, T3 자동 *변경* 금지의 비대칭 활용 — ADR-012 §2.8 답습)
- CI 회귀 검증: base branch 대비 JSONL line deletion / rewrite 감지

**Layer 3 — Signed Commit (RECOMMENDED MVP, MANDATORY multi-host)**:
- GPG / SSH key signed commit
- 1인 동일 호스트 = SHOULD (G3 §5.5 SPOF 면책)
- Multi-host 전환 / 외부 공유 / 팀 사용 / Hermes PMO 격상 시점 = MUST 승격 (G3 §5.5.3 트리거 답습)

**Layer 4 — CI 회귀 검증 (MANDATORY)**:
- Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증
- canonical JSON 위반 검출
- timestamp monotonicity 검증 (ADR-012 §3.4)
- R-6 workflow (`.github/workflows/r2-canary.yml`) 답습 확장 (별도 PR — Implementation 영역)

**Layer 5 — External Anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)**:
- 월 1회 external snapshot (별도 외부 git remote / cloud storage push)
- GitHub Actions run ID + signed tag (ADR-012 §2.8 답습)
- 1인 SPOF 완화 + 침해 후 발견 가능

**사용자 명시 옵션 답습 (D-1, ADR-012 §2.4)**: "signed commit OR git append commit (둘 중 하나) 의무" — 사용자 결정 영역. 5/5 입력 권고는 *다층 동시 의무* (Layer 1 + 2 MANDATORY, Layer 3 RECOMMENDED). **본 §4.4 = Layer 1 + Layer 2 MANDATORY 답습** (D-1A / D-1B / D-1C 모두 호환).

#### 4.4.2 Canonical JSON — RFC 8785 JCS Primary + Fallback

**Primary**: **RFC 8785 JCS** (https://www.rfc-editor.org/rfc/rfc8785) — *informational track*, IETF 권위.


exec
/bin/bash -lc "sed -n '1,130p' docs/decisions/ADR-011-means-vs-ends-redaction.md && sed -n '130,230p' docs/decisions/ADR-011-means-vs-ends-redaction.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
# ADR-011: Means-vs-Ends Redaction Principle (수단/목적 분리 원칙)

**상태**: 승인 (단축 합의 — Reviewer-only, 2026-05-06)
**날짜**: 2026-05-06
**의사결정자**: 사용자 + Reviewer 합의 — `docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md`
**상위 권위**: 헌법 제8조 (보안), 헌법 제5조-2 (Provider Liquidity, 비협상), `docs/architecture/system-identity-prequel.md` §3
**갱신 대상**: ADR-008 부록 B Amendment (동시 발행)
**모법 역할**: R-4 / R-5 / R-6 / R-7 작업의 권위 근거

---

## 1. 맥락 (Context)

### 1.1 P2 v2 가정의 붕괴

ADR-008 부록 A는 R1 (학습루프 평문 누적)을 비협상 CRITICAL 위험으로 명시했다. P2 v2 §2.1.3은 R1 차단 메커니즘으로 "외부 pre-record hook" 형태를 가정 채택했다.

Phase 0 Day 1 사실 확인(`docs/phase0/day1-environment-and-fact-check.md`)에서 Hermes v0.12.0 main HEAD에 `pre_record` / `add_pre_record_hook` / `before_record` API가 존재하지 않음이 grep 0건으로 확정되었다 (15종 `VALID_HOOKS` 중 DB 기록 직전 가로채기 hook 0개).

### 1.2 Phase 0 R-1 / R-2 evidence

- **R-1 검증**(`docs/phase0/day2-r1-redaction-location-verification.md`): Hermes 자체 redaction(`agent/redact.py`)이 LLM 송신/도구 출력/로깅 전용이고 DB INSERT 경로 미적용 확정 → **G1a FAIL**.
  - `agent/redact.py:1-8` docstring 명시: "Regex-based secret redaction for logs and tool output"
  - redact 모듈 import 25개 모두 비-DB 경로
  - `hermes_state.py` (SessionDB) redact import 0건

- **R-2 PoC**(`docs/phase0/day3-r2-sqlite-trigger-poc.md`): SQLCipher BEFORE INSERT trigger + REGEXP UDF 조합이 Docker 격리 환경(network_mode: none + read_only + cap_drop ALL)에서 6항목 모두 PASS → **G1b PASS by R-2 PoC**.

### 1.3 ADR 권위 해석 요청 사항

위 결과는 다음 질문에 대한 ADR 권위 해석을 요구한다:

> **R1의 "비협상" 본질은 무엇인가 — 특정 구현 수단인가, 보안 결과인가?**

본 ADR은 이 질문에 답하고, 동시에 다음 3개 인접 안건을 ADR 권위로 정착한다:
- G1a/G1b 게이트 분리 공식화
- "Hermes ≠ root of trust" 권위 위계 영구화 (prequel §3 → ADR 승격)
- 자동 학습 vs 자동 정책 변경 분리

---

## 2. 결정 (Decision)

본 ADR은 다음 4가지를 권위로 선언한다.

### 2.1 수단/목적 분리 원칙 (Means-vs-Ends Separation)

**비협상 조건의 본질은 특정 구현 수단이 아니라, 달성해야 하는 안전 결과(safety outcome)이다.**

- 헌법 제8조 (보안)의 본질은 **DB 평문 저장 차단이라는 결과**이다.
- 외부 hook, redaction 호출, trigger, 암호화 등은 **수단**이다.
- 대체 수단은 다음 4조건을 **모두** 충족할 때 기존 수단을 대체할 수 있다:

  | # | 조건 | 검증 방식 |
  |---|------|---------|
  | (a) | 동등 이상의 보안 결과 | 명시적 비교표 (수단 A 보장 ↔ 수단 B 보장) |
  | (b) | 격리 환경 PoC로 실증 | Docker isolation + 자동 검증 항목 |
  | (c) | ADR 권위로 명시 | 본 ADR 또는 후속 ADR |
  | (d) | 자동 회귀 검증 경로 확보 | CI/nightly 재실행 (R-6) |

**원칙 위반**: "수단이 비협상이다"는 텍스트 해석으로 본질 회귀를 차단하는 것은 본 ADR로 무효화된다. 동시에 (a)~(d) 4조건 미충족 시 수단 대체도 금지된다 — 본 ADR은 *수단 자유*가 아니라 *목적 달성 검증 의무*를 강제한다.

### 2.2 G1a / G1b 게이트 분리 공식화

P2 v2의 단일 G1 게이트는 본 ADR로 다음 두 게이트로 분해된다.

```
G1a: Hermes native redaction applies before DB INSERT
   Result: FAIL (R-1 확정)
   Evidence: agent/redact.py docstring "for logs and tool output",
             redact import 25개 모두 비-DB,
             hermes_state.py redact import 0건
   Status: 폐기 (이 경로로 헌법 8조 충족 시도 금지)

G1b: DB-level fallback prevents plaintext secret persistence
   Result: PASS by R-2 PoC
   Evidence: Docker 격리 환경 (network_mode: none + read_only + cap_drop ALL)
             + SQLCipher BEFORE INSERT trigger + REGEXP UDF
             + 6항목 자동 검증 (C1~C6 모두 PASS)
   Status: PoC PASS, 정식 충족은 R-3~R-5 완료 후
```

#### G1b 정식 충족 조건 (Phase 1 차단조건 #1 exit 기준)

| # | 조건 | 산출 |
|---|------|------|
| R-3 | 본 ADR-011 발행 + ADR-008 Amendment | `ADR-011`, `ADR-008` 부록 B |
| R-4 | Hermes redact pattern ↔ P1_REDACTOR 패턴 동등성 검증, gap 발견 시 trigger UDF 보충 | `docs/architecture/redaction-pattern-equivalence.md` |
| R-5 | canary 재검증 트리거 설계 (T13 강화 — config + 주기적 inject) | `docs/architecture/canary-recheck-design.md` |
| R-6 | CI/nightly 회귀 검증 (Hermes 업그레이드 자동 R-2 재실행) | `.github/workflows/r2-canary.yml` |
| R-7 | Phase 1 합격 SOP (canary 패턴/주입/검증/PASS·FAIL 기준) | `docs/phase0/redaction-verification-sop.md` |

R-3~R-7 모두 완료 시 G1b는 PoC 단계를 벗어나 Phase 1 차단조건 #1 정식 exit 기준이 된다.

### 2.3 Hermes ≠ Root of Trust

**Hermes는 시스템의 최종 신뢰 근거가 아니라 검증 대상이다.**

#### 권위 위계 (Authority Hierarchy)

```
Constitution
  > ADR
  > SDD
  > Harness Gates
  > Hermes
  > Worker Agents
```

#### 운영 함의 (Operational Implications)

1. **Hermes 출력은 Tools로 검증된다**: 린터/타입체커/테스트/trigger/canary가 Hermes 출력 위에 위치한다.
2. **Hermes 자체 redaction은 로그/LLM 송신 방어로만 신뢰**: 저장 경로(DB/파일) 차단 책임 없음.
3. **DB INSERT 경로는 Hermes 외부에서 별도 보호**: SQLCipher trigger 기반 fallback (G1b).
4. **Hermes 의존성 업그레이드는 자동 R-2 재실행으로 회귀 검증**: 신뢰 경계 외부 변경의 자동 검출 (R-6).
5. **Hermes 학습 결과의 자동 정책 반영 금지**: §2.4와 결합.

#### prequel과의 관계

본 §2.3은 `docs/architecture/system-identity-prequel.md` §3 ("Hermes ≠ root of trust") 의 prequel(임시) 선언을 ADR 영구 권위로 승격한다. prequel은 R-7 완료 후 P2 v3로 흡수되며 폐기되지만, 본 ADR-011 §2.3은 영구 유지된다.

### 2.4 자동 학습과 자동 정책 변경 분리

- **자동 학습은 허용**: Worker Agent가 도구 사용/패턴/실패 사례를 누적 학습하는 것은 시스템 가치의 핵심.
- **자동 정책 변경은 금지**: Constitution / ADR / Harness Gates / Hermes 설정의 변경은 사용자 승인 경로(3+1 합의 또는 단축 합의)를 거쳐야 한다.

#### 3-tier 분류 (T1 / T2 / T3)

| Tier | 정의 | 예시 | 승인 경로 |
|------|------|------|---------|
|------|------|------|---------|
| **T1** | 자동 허용 | Worker Agent 패턴 학습, 도구 사용 빈도 누적, 실패 회피 휴리스틱 | 자동 |
| **T2** | 사용자 승인 필수 | Skill/Memory promotion, 새 도구 등록, 합의 형태 결정 | 사용자 명시 결정 |
| **T3** | 자동 금지 (절대) | Constitution / ADR / Harness Gates 정의 자체의 변경 | 단축 또는 풀 3+1 합의 |

본 분리는 prequel §6의 3-tier 선언을 ADR 권위로 승격한 것이며, R-5 (canary 재검증) / R-6 (CI 회귀)의 권위 근거이기도 하다 — Hermes 내부 학습 또는 upstream 변경으로 redaction 동작이 silent 깨짐 발생 가능성을 자동 검증으로 차단.

---

## 3. R-4 ~ R-7 모법 역할 (Governing Precedent)

본 ADR은 다음 후속 작업의 권위 근거로 기능한다.

| 작업 | 산출 | 본 ADR §과의 관계 |
|------|------|----------------|
| **R-4** | `docs/architecture/redaction-pattern-equivalence.md` | §2.1 (a) — 대체 수단(R-2 trigger)이 기존 수단(Hermes redaction) 대비 패턴 커버리지 동등 이상임을 명시적 비교표로 실증 |
| **R-5** | `docs/architecture/canary-recheck-design.md` | §2.4 — Hermes 학습 또는 upstream 변경으로 redaction silent 깨짐 발생 가능성 자동 검증 + §2.3 운영 함의 #4 구현 |
| **R-6** | `.github/workflows/r2-canary.yml` | §2.1 (d) + §2.3 — Hermes 의존성 업그레이드의 자동 회귀 검증 |
| **R-7** | `docs/phase0/redaction-verification-sop.md` | §2.2 G1b 정식 충족 절차의 SOP화 |

후속 작업은 본 ADR §2를 명시 인용하고, 본 ADR 위반(예: "수단이 비협상이다" 텍스트 회귀, T3 자동 변경 시도) 시 단축 합의 + ADR Amendment 절차로만 갱신 가능하다.

---

## 4. 선택지 (Options Considered)

### 옵션 A: ADR-011 단독 (Amendment 없음)

- 장점: 일반 원칙 ADR 단일 산출 — 작성 부담 최소
- 단점: ADR-008 부록 A R1 표면 텍스트("외부 pre-record hook 공식 지원")가 갱신되지 않아 ADR-008 본문과 ADR-011 사이 표면 모순. 이력 추적 시 혼란.

### 옵션 B: ADR-008 Amendment 단독 (ADR-011 없음)

- 장점: ADR-008 한 문서로 일관
- 단점:
  - "수단/목적 분리"는 R1을 넘어선 일반 원칙 — Amendment에 일반 원칙을 담는 것은 Amendment 형식 위반
  - "Hermes ≠ root of trust" 운영 ADR화는 ADR-008 (Hermes 도입 결정) 범위 초과
  - R-4~R-7이 Amendment를 권위 근거로 인용하는 것은 비표준 (Amendment는 specific 갱신 한정)

### 옵션 C: ADR-011 신규 + ADR-008 Amendment ⭐ **채택**

- 장점:
  - 일반 원칙(수단/목적 분리, G1a/G1b 분리, Hermes ≠ root of trust, 학습/정책 분리)은 ADR-011로 권위화
  - ADR-008 부록 A R1 specific 갱신은 Amendment로 짧게 처리 + ADR-011 cross-reference
  - R-4~R-7이 ADR-011을 명확한 모법으로 인용
  - ADR-008 본문 read 시 즉시 R-1 FAIL 후 갱신 사항 파악 가능
- 단점: 작성 분량 2배 (수용)

---

## 5. 근거 (Rationale)

### 5.1 헌법 제8조 본질 재해석의 정당성

헌법 제8조의 비협상 본질은 "특정 hook이 존재해야 함"이 아니라 "비밀이 평문 영구 저장되지 않음"이다. R-2 PoC는 SQLCipher trigger 기반 fallback이 이 본질을 충족함을 실증했다.

수단을 비협상으로 굳히면, 수단이 부재한 시점(현 Hermes v0.12.0)에 헌법 제8조 자체를 충족할 수 없는 모순이 발생한다. 본 ADR은 이 모순을 수단/목적 분리로 해소하되, 동시에 (a)~(d) 4조건으로 자의적 수단 대체를 차단한다.

### 5.2 "Hermes ≠ root of trust" ADR 권위화 필요성

system-identity-prequel은 임시 선언(Pre-Declaration)으로, R-7 완료 후 P2 v3 흡수와 함께 폐기된다. 그러나 "Hermes ≠ root of trust"는 폐기되어서는 안 되는 영구 권위 원칙이다. 본 ADR-011 §2.3으로 권위 승격하여 prequel 폐기 후에도 보존한다.

### 5.3 G1a/G1b 분리의 영구화 필요성

R-1 FAIL과 R-2 PASS는 Phase 0 evidence 보고서에 기록되어 있으나, 이는 보고서이지 ADR 권위가 아니다. G1a/G1b 분리를 ADR로 권위화하지 않으면 미래 합의에서 "G1 단일 게이트로 회귀 가능" 해석 위험이 발생한다. 본 ADR §2.2가 이를 차단한다.

### 5.4 단축 합의(Reviewer-only)의 정당성

본 R-3은 새 설계 안건이 아니라 R-1 FAIL + R-2 PASS + 단축 합의 §R-3 (`docs/review/3plus1-consensus-2026-05-05-p2-n1-redaction-reinterpretation.md`) + 풀 합의 §3 권위 위계 (`docs/review/3plus1-consensus-2026-05-05-system-identity-redefinition.md`) 의 ADR 형식화 작업이다. 새 합의 검증이 아니므로 풀 3+1은 과잉. 직전 R-1 단축 합의 패턴 답습.

---

## 6. 합의 결과 (단축 합의 — Reviewer-only)

세부: `docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md`

| 차원 | 판정 | 핵심 근거 |
|------|------|---------|
| 헌법 제8조 본질 충족 권위화 | **PASS** | §2.1 수단/목적 분리 + (a)~(d) 4조건 명시로 자의적 회귀·자의적 수단 대체 양방향 차단 |
| G1a/G1b 분리 공식화 | **PASS** | R-1 FAIL evidence + R-2 PASS evidence 모두 인용, 정식 충족 조건 명시 |
| Hermes ≠ root of trust 권위 승격 | **PASS** | prequel §3 → ADR §2.3 영구화, 운영 함의 5항목 명문화 |
| 자동 학습 vs 정책 변경 분리 | **PASS** | T1/T2/T3 3-tier 분류 본문 흡수, R-5/R-6 권위 근거화 |
| Provider Liquidity 영향 | **무관** | 본 ADR은 redaction 수단 해석이며 모델/구독 교체 자유와 무관 |
| 메타 편향 통제 | **명시** | 본 ADR은 자체 코드 우호 결론(R-2 PASS)을 반영하나, (a)~(d) 4조건과 R-4~R-7 모법으로 회귀 견제 — 합의 보고서 §메타 편향 자기진단 참조 |

---

## 7. 결과 (Consequences)

### 7.1 긍정적

- 헌법 제8조 본질 충족이 specific 수단에 종속되지 않음 → 미래 Hermes API 변경 / upstream 변경 시에도 본질 보존 경로 확보
- G1a/G1b 분리로 R-2 PASS evidence가 P2 v3에 직접 흡수 가능
- "Hermes ≠ root of trust" ADR 권위화 → prequel 폐기 후에도 운영 원칙 영구 보존
- R-4~R-7이 권위 근거 명확화 → 후속 작업 의사결정 비용 감소
- 자동 학습/자동 정책 분리(T1/T2/T3)의 ADR 권위화 → silent 깨짐 자동 차단의 권위 근거

### 7.2 부정적

- ADR-008 부록 A R1의 표면 텍스트와 본 ADR §2.1 사이 텍스트 차이 존재 (Amendment로 동시 갱신하여 완화)
- "수단/목적 분리"가 일반화되어 미래 다른 비협상 조항 해석에도 적용 시 합의 비용 발생 가능 (대체 수단 검증 부담 — 의도된 비용)

exec
/bin/bash -lc "sed -n '40,120p' docs/decisions/ADR-012-evidence-ledger-protection.md && sed -n '120,230p' docs/decisions/ADR-012-evidence-ledger-protection.md && sed -n '330,390p' docs/decisions/ADR-012-evidence-ledger-protection.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
**PASS 성립 4 요건** (G3 §5.3):
- (i) Tools 검증
- (ii) **Evidence Ledger entry** ← 본 ADR-012 보호 강화 대상
- (iii) (T2/T3) 사용자 명시 승인
- (iv) (해당 시) 합의 보고서 commit

Evidence Ledger 변조 가능성 = G3 root-of-trust 직접 훼손 → 본 ADR 권위로 보호.

### 1.3 G2 §1.2.5 P10 (Evidence Forgery) 정식 등록 트리거 명시

PR-1 §1.4 (C-I 흡수, `commit 750faaf`) 에서 G2 §1.2.5 P9~P12 deferred candidates 4건 등록:
- P9 (Prompt Injection)
- **P10 (Evidence Forgery)** ← **본 ADR-012 발행 시점 = 정식 등록 트리거** (G2 §1.2.5.2 명시)
- P11 (Supply-chain)
- P12 (Memory Poisoning Side-channel)

본 ADR-012 발행은 P10 의 *정식 위반 경로 등록 트리거*. 단 **G2 §1.2 본문 P10 row 추가는 별도 G2 update PR** (본 ADR 범위 외, 합의 §4.2 답습).

### 1.4 Cross-reference (헌법 + ADR + G + 5 영구 핵심 제약)

| 연결 대상 | 연결 사유 |
|--------|--------|
| **헌법 제8조 (보안)** | Evidence Ledger entry 자체에 평문 secret 포함 가능 (P1 변종) — GP-1 SQLCipher trigger 보호 범위에 ledger DB 명시 포함 의무 (외부 LLM 2 C-1) |
| **헌법 제5조 관용 (Provider Liquidity)** | Ledger 형식 = Hermes 의존 0 (ADR-008 차단조건 #2 답습) + provider-neutral 강제 (Provider Liquidity 4-way Multi-layer Defense → **5-way** Evidence 형식 layer 추가) |
| **ADR-011 §2.1 (수단/목적 분리)** | 본 ADR 자체가 Evidence 무결성 = 목적, hash chain + signed/append commit + JCS = 수단. (a)~(d) + (e) 5조건 답습 (§4) |
| **ADR-011 §2.3 (Hermes ≠ root of trust)** | Hermes 는 ledger entry 생성 가능 (T1 자동 학습), 단 promotion / approval 은 사용자 명시 (T2). Hash chain + signed/append commit = Hermes 변조 차단 운영 매커니즘. **본 ADR-012 는 Hermes 안전성을 선언하지 않는다** (ADR-011 §7.3 직접 답습 — 외부 LLM 2 C-15 / Agent B Gap-18) |
| **ADR-011 §2.4 (T1/T2/T3)** | prev_hash 검증 실패 자동 revert = T3 위반 위험 → BLOCK + manual review 채택 (외부 LLM 2 C-3 / Agent B C-3) |
| **ADR-008 차단조건 #2** | JSONL export 표준 — 본 ADR §2.10 흡수 |
| **ADR-010 (SQLCipher Vault)** | secret 처리 cross-reference — Evidence Ledger DB 가 secret 포함 가능 시 GP-1 보호 범위 명시 의무 |
| **G3 §1.3 + §5.3** | Evidence 결정 5 운영 규칙 + PASS 성립 4 요건 |
| **G4 §4.4 + §4.6** | Hash chain + canonical JSON + round-trip 검증 (본 ADR §2.3 + §2.5 + §2.7 + §2.8 + §2.9 와 동시 보강) |
| **system-identity-prequel §6.3** | Evidence Ledger schema 후보 권위 근거 — 본 ADR §2.2 답습 |

### 1.5 메타포 회피 명시 (외부 LLM 2 §1)

본 ADR-012 는 *형식적 무결성* (hash chain / canonical / append-only / signed) 까지만 보호. *의미적 정확성* (예: 사용자가 위조된 사실을 본인이 작성한 것처럼 ledger 에 기록) 은 본 ADR 방어 범위 외 (§11 한계 명시 답습). "Ledger 를 *불변의 진리* 로 비유" 같은 메타포 회피 — `system-identity-prequel §7` 답습.

---

## 2. 결정 (Decision)

본 ADR-012 는 다음 12 보호 원칙 + 4 매트릭스 항목 + 5 추가 의무 을 권위로 선언한다.

### 2.1 Evidence Ledger 보호 원칙 (12)

**원칙 1**: Evidence Ledger 는 PASS 의 *보조 기록* 이 아니라 **PASS 성립 조건** 이다.

**원칙 2**: Evidence 가 없으면 PASS 는 *존재하지 않는다*.

**원칙 3**: Evidence Ledger 는 Hermes 가 *승인하거나 수정* 할 수 없다 (T3 영역).

**원칙 4**: Evidence Ledger 의 변조 가능성은 G3 root-of-trust 구조를 직접 훼손한다.

**원칙 5**: Evidence Ledger 는 *Hermes 의존 0* — 모든 entry 가 표준 도구 (`jq` + `sha256sum` + 표준 라이브러리) 만으로 검증 가능 (ADR-008 차단조건 #2 답습).

**원칙 6**: Evidence Ledger entry 작성 주체는 `agent` 필드로 *provider-neutral* 식별 — `user` / `<worker_name>` / `hermes` 등.

**원칙 7**: External LLM response 적재 시 entry `agent = "user"` (수동 paste 주체) 강제 (외부 LLM 2 C-9). Hermes 가 외부 LLM response 를 자기 제안으로 위조 차단 (Gap-17 #4).

**원칙 8**: Evidence Ledger 는 *append-only* — entry 수정 / 삭제 / 재작성 금지 (T3 영역, ADR-011 §2.4).

**원칙 9**: Hash chain 검증 실패 = 즉시 BLOCK. 자동 복구 / 자동 revert 금지 (T3 위반 위험 답습).

**원칙 10**: Round-trip 검증은 tier-based — T2 (로컬 promotion) strict / T3 (cross-vendor migration) 의미 보존 + 사용자 명시 review (§2.9 답습).

**원칙 11**: Evidence Ledger 보호 범위 = *형식적 무결성* — *의미적 정확성* (content-level forgery) 은 본 ADR 방어 범위 외 (§11 답습).

**원칙 12**: 1인 동일 호스트 SPOF 한계 인지 (G3 §5.5 답습) — 동일 호스트 전체 침해는 본 ADR 의 완전 방어 범위 밖. multi-host 전환 시 Layer 3 / Layer 5 의무 발동 트리거.

### 2.2 11 필드 구조 (G4 §4.2 schema 갱신, 10 → 11 필드)

```jsonl
{
  "type": "memory|skill|meta",
  "scope": "global|project|session|team",
  "id": "<uuid-v4-or-slug>",
  "schema_version": "0.2",
  "ts": "2026-05-09T10:00:00Z",
  "agent": "user|<worker_name>|hermes",
  "event": "<event-enum>",
  "content": {...},
  "content": {...},
  "evidence_refs": ["docs/evidence/<path>.md"],
  "prev_hash": "<sha256>",
  "hash": "<sha256>"
}
```

**11번째 필드 = `event`** (4/5 합의, Agent A enumeration 결과적 일치 — 합의 §3.1).

**`event` enum 후보 (25건, MVP 의무 12건 + 후속 확장 5건 + MVP-1 신규 8건 — schema_version 0.2)**:

| # | enum | 정체성 | T 분류 |
|---|------|------|------|
| 1 | `memory_write` | Memory entry 작성 | T1 (Hermes) / T2 (사용자 promotion) |
| 2 | `skill_proposed` | Skill 후보 추출 | T1 (Hermes 자동) |
| 3 | `skill_approved` | Skill `proposed` → `approved` | T2 (사용자 명시) |
| 4 | `skill_promoted` | Skill `approved` → `promoted` | T2 + Evidence |
| 5 | `skill_revoked` | Skill `promoted` → `revoked` | T3 자동 안전 (rollback_trigger) |
| 6 | `gate_pass` | Gate (G1b/G2/G3/G4 등) PASS 선언 | T2 사용자 명시 |
| 7 | `gate_fail` | Gate FAIL 선언 | T2 사용자 명시 |
| 8 | `external_llm_received` | External LLM response 적재 | **T2 + agent="user" 강제** (원칙 7) |
| 9 | `evidence_forgery_detected` | P10 위반 검출 | T3 BLOCK |
| 10 | `roundtrip_pass` | Round-trip hash 일치 | T1 자동 |
| 11 | `roundtrip_lossy` | Round-trip 의미 보존 (lossy) | T3 사용자 review |
| 12 | `roundtrip_fail` | Round-trip 정책/권한/증거 손실 | T3 BLOCK |
| 13 | `migration_failed` | Migration 검증 실패 (Agent A 권고) | T3 BLOCK + manual |
| 14 | `chain_violation_detected` | prev_hash mismatch 또는 hash 재계산 검출 (외부 LLM 2 C-3) | T3 BLOCK + manual |
| 15 | `hash_chain_broken` | Hash chain 자체 단절 (외부 LLM 1) | T3 BLOCK |
| 16 | `policy_change_attempted` | Hermes 가 정책 변경 시도 (T3 위반) | T3 BLOCK + audit |
| 17 | `canonical_json_fallback` | Canonical JSON `jq -S -c` fallback 사용 | T1 audit |
| 18 | `secret_scan_layer1_implementation` | Secret scan Layer 1 구현 ledger (MVP-1 Stage 1, GP-3 S-1) | T1 audit |
| 19 | `docker_secret_isolation_layer1_implementation` | Docker secret 격리 Layer 1 구현 ledger (MVP-1 Stage 2, GP-3 ST-3) | T1 audit |
| 20 | `provider_adapter_enforcement_layer1_static` | Provider adapter Layer 1 static 검출 ledger (MVP-1 Stage 3, GP-5 T-6) | T1 audit |
| 21 | `pc3_ar1_integration_implementation` | pre-commit + auto-revert 통합 구현 ledger (MVP-1 Stage 4) | T1 audit |
| 22 | `g3_7_workflow_hygiene_implementation` | Workflow hygiene 4 항목 구현 ledger (MVP-1 Stage 5, G3-7) | T1 audit |
| 23 | `provider_key_adapter_bypass_risk_detected` | Provider lock-in 위반 detect (MVP-1 IR-1) | T2 사용자 review |
| 24 | `direct_sdk_with_secret_leakage_detected` | Direct SDK + secret 검출 (MVP-1 IR-2) | T3 BLOCK + manual |
| 25 | `secret_handling_environment_mismatch_detected` | 환경 secret mismatch detect (MVP-1 IR-3) | T2 사용자 review |

**MVP 의무 12 enum** (1~12, schema_version 0.1 도입). **후속 확장 5 enum** (13~17, schema_version 0.2 진입). **MVP-1 신규 8 enum** (18~25, schema_version 0.2 정식 등록 — Backlog #5 합의 `docs/review/3plus1-consensus-2026-05-13-adr-012-event-enum-registration.md` 권위, MVP-1 PASS §C-2 충족).

**Provider-neutral 강제** (Agent B C-16): 11 필드 모두 provider-specific 식별자 미허용.

### 2.3 Append-only 원칙 + Hash Chain (다층 강제)

**Layer 1 — Hash Chain (MANDATORY 모든 환경)**:
- `prev_hash` = 직전 entry 의 `hash` (chain 형성)
- `hash` = 본 entry 의 canonical JSON sha256
- 첫 entry 의 `prev_hash` = `genesis_hash` (§2.6)
- SHA-256 hardcode (schema_version 0.1) — `hash_algo` 필드 후속 격상 영역 (§3.2 답습)

**Layer 2 — Git append-only branch (MANDATORY)**:
- `git config receive.denyNonFastForwards true` (force-push 차단)
- branch protection rule
- pre-commit hook: `git rebase` / `git filter-branch` / `git reset --hard` 감지 시 reject
- CI 회귀 검증: base branch 대비 JSONL line deletion / rewrite 감지

**Layer 3 — Signed commit (RECOMMENDED MVP, MANDATORY multi-host)**:
- GPG / SSH key signed commit
- 1인 동일 호스트 = SHOULD (SPOF 면책)
- Multi-host 전환 / 외부 공유 / 팀 사용 / Hermes PMO 격상 시점 = MUST 승격 (G3 §5.5.3 트리거 답습)

**Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)**:
- 월 1회 external snapshot (별도 외부 git remote / cloud storage push)
- GitHub Actions run ID + signed tag (Agent B C-4 권고)
- 1인 SPOF 완화 + 침해 후 발견 가능

### 2.4 Signed commit OR Git append commit (사용자 명시 답습)

**사용자 명시 결정 답습**: "signed commit 또는 git append commit (둘 중 하나) 의무".

**5/5 입력 권고**: Layer 1 + Layer 2 동시 의무 (Hash chain + Git append-only) + Layer 3 RECOMMENDED.

**옵션** (사용자 결정 영역 — D-1):

| 옵션 | 정체성 | 적용 |
|-----|------|---|
| **D-1A** (사용자 명시 답습) | "둘 중 하나 의무" 그대로 — 최소 = git append-only, signed = 권장 | 사용자 결정 |
| **D-1B** (5 입력 권고) | "Hash chain + Git append-only MANDATORY + Signed RECOMMENDED" 다층 | 사용자 결정 |
| **D-1C** (절충, Reviewer 권고) | MVP = "둘 중 하나 의무" + Implementation 시점 다층 격상 | 사용자 결정 |

**본 ADR 의 권위 결정**: D-1A / D-1B / D-1C 모두 본 ADR §2.3 Layer 1 + Layer 2 동시 의무 *호환*. 단 사용자 명시 결정 영역 — 본 ADR 갱신은 단축 합의 가능.

### 2.5 RFC 8785 JCS Canonicalization (채택 + Fallback)

**Primary**: RFC 8785 JCS (https://www.rfc-editor.org/rfc/rfc8785) — *informational track*, IETF 권위.

**Fallback**: `jq -S -c` (lex sort + compact + UTF-8 + RFC 8259 escape) 또는 자체 구현 동등성 의무 + test corpus 검증.

**구현 라이브러리 후보** (Agent C C-3 권고):
- Python: `pyjcs` / `rfc8785` / 또는 stdlib `json.dumps(sort_keys=True, separators=(",",":"))` 동등 보장
- Node: `canonicalize` npm
- Go: `cyberphone/json-canonicalization` / `gowebpki/jcs`

**Test corpus 의무** (외부 LLM 2 C-6):
- `tests/canonical/` 디렉토리에 RFC 8785 reference 출력 ≥ 20개 포함
- CI 회귀 검증: 입력 → 자체 canonical → JCS reference output 비교
- 불일치 시 BLOCK

**Fallback 사용 시 의무**:
- `event: canonical_json_fallback` ledger entry 작성 의무
- Reviewer 알림 + 사용자 review 권장

### 2.6 Genesis Hash 정의

**MVP (schema_version 0.1) — 현 G4 §4.4 정의 유지**:

```
genesis_hash = sha256("genesis:<scope>:<schema_version>")
```

- G2 본문 변경 = T3 변경 + 별도 합의 (단축 가능)
- 본 ADR §1.3 cross-reference 명시는 의무

**Evidence Forgery 공격 모델 5종** (외부 LLM 2 §6 답습):

| # | 공격 | 본 ADR 방어 유효성 | 보강 |
|---|------|--------------|----|
| (a) | 1인 호스트 침해 | **약** — host 전체 침해 시 모든 layer 우회 | Layer 5 external snapshot (월 1회) |
| (b) | Hermes container compromise | **강** — Hermes 는 ledger write 권한 0 (G3 §2 T3) | (그대로) |
| (c) | Git history rewrite | **중** — Layer 2~4 차단, 그러나 host 권한 상승 시 force push 가능 | (a) 동일 + Layer 5 |
| (d) | JSONL middle tampering | **강** — Layer 1 (hash chain) 정확히 이 케이스 차단 | (그대로) |
| (e) | External LLM response 위조 | **약** — vendor API key / signed response 부재 시 검증 부족 | 원칙 7 (`agent="user"` 강제) + Layer 3 권장 |

### 2.12 Hermes 변조 차단 매트릭스 4항목 (Agent B Gap-17 HIGH)

본 §2.12 = Agent B Gap-17 HIGH 흡수 — Hermes ≠ root of trust 운영 매커니즘:

| # | 변조 영역 | 차단 매커니즘 | G3 cross-reference |
|---|--------|---------|----|
| 1 | **Hermes-originated ledger entry** (Hermes 자기 entry 작성 시도 — T1 자동 학습 vs T2 사용자 승인 분기) | Hermes container `~/.claude/global/` write 권한 0 + Hermes-originated commit auto-reject | G3 §2.5 #11 + G3 §2.2 #20 |
| 2 | **파일 변조 (filesystem 직접 변경)** | `evidence/<scope>.jsonl` filesystem read-only + audit log + 컨테이너 정지 | G3 §4.5 |
| 3 | **Git commit (Hermes 가 ledger commit 시도)** | Hermes-originated commit auto-reject (commit author = Hermes 검출 시 차단) | G3 §2.2 #20 |
| 4 | **외부 LLM 응답 위조 (Hermes 가 외부 LLM response 를 자기 제안으로 위조)** | External LLM response ledger entry `agent = "user"` 강제 (수동 paste 시) + signed commit 권장 (multi-host 시 의무) | G3 §2.5 #9 + 본 §2.1 원칙 7 |

**4 항목 모두 본 ADR 권위로 차단**. ADR-011 §2.3 (Hermes ≠ root of trust) 운영 매커니즘 흡수.

---

## 3. 추가 의무 (5)

### 3.1 External LLM Response Ledger Entry (N-1)

External LLM response 적재 시 의무 entry 형식:

```jsonl
{
  "type":"meta",
  "scope":"<scope>",
  "id":"<uuid>",
  "schema_version":"0.1",
  "ts":"<ISO 8601>",
  "agent":"user",
  "event":"external_llm_received",
  "content":{
    "source_vendor":"gpt-5.x|gemini|claude-adjacent|other",
    "request_file":"docs/external-review/<request-file>.md",
    "response_file":"docs/external-review/<response-file>.md",
    "canonical_hash":"<sha256(canonical(response_body))>",
    "verdict":"APPROVE|APPROVE_WITH_CONDITIONS|PARTIAL|BLOCK"
  },
  "evidence_refs":["docs/external-review/<response-file>.md"],
  "prev_hash":"<sha256>",
  "hash":"<sha256>"
}
```

**의무**:
- `agent = "user"` 강제 (수동 paste 주체, 본 §2.12 #4 답습)
- `canonical_hash` = response 본문의 canonical JSON sha256
- Multi-host 전환 시 signed commit MUST (Layer 3)


exec
/bin/bash -lc 'ls -l .github/workflows/g4-hash-chain.yml .github/workflows/history-anchor-verifier.yml .github/workflows/rewrite-defense.yml .github/workflows/r2-canary.yml && rg -n "jsonl_hash_chain|canonical|history|anchor|rewrite|monotonic|R-6|denyNonFastForwards|force" .github/workflows/g4-hash-chain.yml .github/workflows/history-anchor-verifier.yml .github/workflows/rewrite-defense.yml .github/workflows/r2-canary.yml' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
-rw-rw-r-- 1 delangi delangi 10652 May 27 22:37 .github/workflows/g4-hash-chain.yml
-rw-rw-r-- 1 delangi delangi 19094 May 27 22:37 .github/workflows/history-anchor-verifier.yml
-rw-rw-r-- 1 delangi delangi  5476 May 27 22:37 .github/workflows/r2-canary.yml
-rw-rw-r-- 1 delangi delangi 16454 May 27 22:37 .github/workflows/rewrite-defense.yml
.github/workflows/r2-canary.yml:3:# R-6: CI/nightly canary regression workflow.
.github/workflows/r2-canary.yml:7:#   - ADR-011 §3 R-6 매핑
.github/workflows/r2-canary.yml:69:        # 정상 동작 (R-6 first run 인프라 fix, 사용자 단축 합의 2026-05-07).
.github/workflows/r2-canary.yml:103:            echo "R-6 FAIL: JSON evidence missing — PoC output 형식 변경 가능성"
.github/workflows/r2-canary.yml:115:              print(f"R-6 FAIL: canary verdict={verdict} (PASS 외 — R-5 §5 판정 위반)")
.github/workflows/r2-canary.yml:118:              print(f"R-6 FAIL: tier1_pass_rate={tier1_rate} (42/42 외 — R-4.1 catalog drift)")
.github/workflows/r2-canary.yml:120:          print("R-6 PASS: canary regression OK (Tier-1 42/42 BLOCK, verdict PASS)")
.github/workflows/rewrite-defense.yml:4:#   - docs/phase0/g4-rewrite-defense-layer234-poc.md (본 PoC 사양 §13 — 14 step CI 설계)
.github/workflows/rewrite-defense.yml:6:#   - .github/workflows/history-anchor-verifier.yml (Group C 후속 형식 직접 답습 — rfc8785+jcs install 포함)
.github/workflows/rewrite-defense.yml:11:#   - L2 PASS + L2 FAIL × 2 (force-push + reorder)
.github/workflows/rewrite-defense.yml:13:#   - L4 PASS + L4 FAIL × 2 (line deletion + in-place rewrite)
.github/workflows/rewrite-defense.yml:30:      - "tools/rewrite_defense_check.py"
.github/workflows/rewrite-defense.yml:31:      - "tools/jsonl_hash_chain.py"
.github/workflows/rewrite-defense.yml:32:      - "tests/fixtures/rewrite_defense/**"
.github/workflows/rewrite-defense.yml:33:      - ".github/workflows/rewrite-defense.yml"
.github/workflows/rewrite-defense.yml:60:          # parse_jsonl → canonical_json → rfc8785 의존성 답습
.github/workflows/rewrite-defense.yml:71:          python tools/rewrite_defense_check.py --list-defenses \
.github/workflows/rewrite-defense.yml:107:      - name: L2 PASS — append-only commit history (rc=0 + violations=0)
.github/workflows/rewrite-defense.yml:111:          python tools/rewrite_defense_check.py --mode append-only \
.github/workflows/rewrite-defense.yml:112:            tests/fixtures/rewrite_defense/append_only/pass/ \
.github/workflows/rewrite-defense.yml:126:          echo "L2 PASS OK (append-only commit history)"
.github/workflows/rewrite-defense.yml:128:      - name: L2 FAIL — force-push + reorder (rc=1 + 2 patterns cover)
.github/workflows/rewrite-defense.yml:132:          # force-push fixture
.github/workflows/rewrite-defense.yml:133:          python tools/rewrite_defense_check.py --mode append-only \
.github/workflows/rewrite-defense.yml:134:            tests/fixtures/rewrite_defense/append_only/fail/force_push/ \
.github/workflows/rewrite-defense.yml:135:            > group-cff-logs/l2-fail-force-push.stdout 2> group-cff-logs/l2-fail-force-push.stderr
.github/workflows/rewrite-defense.yml:138:          python tools/rewrite_defense_check.py --mode append-only \
.github/workflows/rewrite-defense.yml:139:            tests/fixtures/rewrite_defense/append_only/fail/reorder/ \
.github/workflows/rewrite-defense.yml:143:          cat group-cff-logs/l2-fail-force-push.stderr
.github/workflows/rewrite-defense.yml:146:            echo "::error::L2 FAIL force-push expected rc=1, got rc=$fp_rc"
.github/workflows/rewrite-defense.yml:153:          if ! grep -q "non_fast_forward_detected" group-cff-logs/l2-fail-force-push.stderr; then
.github/workflows/rewrite-defense.yml:154:            echo "::error::L2 FAIL force-push missing 'non_fast_forward_detected'"
.github/workflows/rewrite-defense.yml:157:          if ! grep -q "history_reorder_detected" group-cff-logs/l2-fail-reorder.stderr; then
.github/workflows/rewrite-defense.yml:158:            echo "::error::L2 FAIL reorder missing 'history_reorder_detected'"
.github/workflows/rewrite-defense.yml:162:          echo "L2 FAIL OK (rc=1 each, 2 patterns cover: non_fast_forward + history_reorder)"
.github/workflows/rewrite-defense.yml:168:          python tools/rewrite_defense_check.py --mode rewrite-command \
.github/workflows/rewrite-defense.yml:169:            tests/fixtures/rewrite_defense/rewrite_command/pass/ \
.github/workflows/rewrite-defense.yml:189:          python tools/rewrite_defense_check.py --mode rewrite-command \
.github/workflows/rewrite-defense.yml:190:            tests/fixtures/rewrite_defense/rewrite_command/fail/ \
.github/workflows/rewrite-defense.yml:199:          for pid in "rebase" "filter-branch" "reset-hard" "push-force-or-amend"; do
.github/workflows/rewrite-defense.yml:206:          echo "L3 FAIL OK (rc=1, 4 patterns cover: rebase + filter-branch + reset-hard + push-force-or-amend)"
.github/workflows/rewrite-defense.yml:212:          python tools/rewrite_defense_check.py --mode line-regression \
.github/workflows/rewrite-defense.yml:213:            tests/fixtures/rewrite_defense/line_regression/pass/ \
.github/workflows/rewrite-defense.yml:229:      - name: L4 FAIL — line deletion + in-place rewrite (rc=1 + 2 patterns cover)
.github/workflows/rewrite-defense.yml:234:          python tools/rewrite_defense_check.py --mode line-regression \
.github/workflows/rewrite-defense.yml:235:            tests/fixtures/rewrite_defense/line_regression/fail/line_deletion/ \
.github/workflows/rewrite-defense.yml:238:          # line_rewrite fixture
.github/workflows/rewrite-defense.yml:239:          python tools/rewrite_defense_check.py --mode line-regression \
.github/workflows/rewrite-defense.yml:240:            tests/fixtures/rewrite_defense/line_regression/fail/line_rewrite/ \
.github/workflows/rewrite-defense.yml:241:            > group-cff-logs/l4-fail-rewrite.stdout 2> group-cff-logs/l4-fail-rewrite.stderr
.github/workflows/rewrite-defense.yml:245:          cat group-cff-logs/l4-fail-rewrite.stderr
.github/workflows/rewrite-defense.yml:251:            echo "::error::L4 FAIL line_rewrite expected rc=1, got rc=$lr_rc"
.github/workflows/rewrite-defense.yml:258:          if ! grep -q "line_rewrite_detected" group-cff-logs/l4-fail-rewrite.stderr; then
.github/workflows/rewrite-defense.yml:259:            echo "::error::L4 FAIL line_rewrite missing 'line_rewrite_detected'"
.github/workflows/rewrite-defense.yml:263:          echo "L4 FAIL OK (rc=1 each, 2 patterns cover: line_deletion + line_rewrite)"
.github/workflows/rewrite-defense.yml:271:          if grep -E "subprocess\.(run|Popen)|os\.system|os\.popen" tools/rewrite_defense_check.py; then
.github/workflows/rewrite-defense.yml:276:          if grep -E "^(import|from)\s+(httpx|requests|aiohttp|urllib3)" tools/rewrite_defense_check.py; then
.github/workflows/rewrite-defense.yml:281:          if grep -rE "/\.git/hooks|/\.git/refs|gitpython|pygit2" tools/rewrite_defense_check.py; then
.github/workflows/rewrite-defense.yml:287:               tests/fixtures/rewrite_defense/ tools/rewrite_defense_check.py 2>/dev/null; then
.github/workflows/rewrite-defense.yml:328:      - name: Upload rewrite defense logs (artifact)
.github/workflows/rewrite-defense.yml:332:          name: rewrite-defense-evidence
.github/workflows/rewrite-defense.yml:344:            echo "- event: g4_rewrite_defense_layer234"
.github/workflows/rewrite-defense.yml:349:            echo "- l2_fail: ${{ steps.l2_fail.outputs.l2_fail || 'FAIL' }} (force-push + reorder)"
.github/workflows/rewrite-defense.yml:351:            echo "- l3_fail: ${{ steps.l3_fail.outputs.l3_fail || 'FAIL' }} (4 patterns: rebase + filter-branch + reset-hard + push-force/amend)"
.github/workflows/rewrite-defense.yml:353:            echo "- l4_fail: ${{ steps.l4_fail.outputs.l4_fail || 'FAIL' }} (line deletion + in-place rewrite)"
.github/workflows/g4-hash-chain.yml:14:#   - PASS fixture × 2: jsonl_hash_chain.py rc=0
.github/workflows/g4-hash-chain.yml:15:#   - FAIL fixture × 4: jsonl_hash_chain.py rc=1 + 4 violation_type cover
.github/workflows/g4-hash-chain.yml:28:      - "tools/canonical_json.py"
.github/workflows/g4-hash-chain.yml:29:      - "tools/jsonl_hash_chain.py"
.github/workflows/g4-hash-chain.yml:31:      - "tests/canonical/**"
.github/workflows/g4-hash-chain.yml:44:  enforce:
.github/workflows/g4-hash-chain.yml:76:          for inp in tests/canonical/*/*.input.json; do
.github/workflows/g4-hash-chain.yml:78:            exp_canonical="${base}.expected.canonical"
.github/workflows/g4-hash-chain.yml:81:            if ! python tools/canonical_json.py --mode primary_1_only --input "$inp" \
.github/workflows/g4-hash-chain.yml:82:                  --expected-canonical "$exp_canonical" \
.github/workflows/g4-hash-chain.yml:101:          for inp in tests/canonical/*/*.input.json; do
.github/workflows/g4-hash-chain.yml:103:            exp_canonical="${base}.expected.canonical"
.github/workflows/g4-hash-chain.yml:106:            if ! python tools/canonical_json.py --mode primary_2_only --input "$inp" \
.github/workflows/g4-hash-chain.yml:107:                  --expected-canonical "$exp_canonical" >/dev/null 2>err.log; then
.github/workflows/g4-hash-chain.yml:125:          for inp in tests/canonical/*/*.input.json; do
.github/workflows/g4-hash-chain.yml:127:            exp_canonical="${base}.expected.canonical"
.github/workflows/g4-hash-chain.yml:129:            if ! python tools/canonical_json.py --mode cross_check --input "$inp" \
.github/workflows/g4-hash-chain.yml:130:                  --expected-canonical "$exp_canonical" >/dev/null 2>err.log; then
.github/workflows/g4-hash-chain.yml:148:          for inp in tests/canonical/*/*.input.json; do
.github/workflows/g4-hash-chain.yml:150:            exp_canonical="${base}.expected.canonical"
.github/workflows/g4-hash-chain.yml:152:            if ! python tools/canonical_json.py --mode primary_1_only --input "$inp" \
.github/workflows/g4-hash-chain.yml:153:                  --expected-canonical "$exp_canonical" \
.github/workflows/g4-hash-chain.yml:172:                                  ("jcs", lambda v: jcs.canonicalize({"n": v}))]:
.github/workflows/g4-hash-chain.yml:182:      - name: PASS fixture — jsonl_hash_chain rc=0 (× 2)
.github/workflows/g4-hash-chain.yml:187:            python tools/jsonl_hash_chain.py "$f"
.github/workflows/g4-hash-chain.yml:197:      - name: FAIL fixture — jsonl_hash_chain rc=1 + 4 violation_type cover
.github/workflows/g4-hash-chain.yml:211:            python tools/jsonl_hash_chain.py "$f" 2> chain_out.txt
.github/workflows/history-anchor-verifier.yml:4:#   - docs/phase0/g4-history-rewrite-layer5-anchor-poc.md (본 PoC 사양 §10 — 13 step CI 설계)
.github/workflows/history-anchor-verifier.yml:12:#   - Anchor FAIL × 5 (full rewrite + tail truncation + middle deletion + substitution + tampered anchor)
.github/workflows/history-anchor-verifier.yml:29:      - "tools/history_anchor_verifier.py"
.github/workflows/history-anchor-verifier.yml:30:      - "tools/jsonl_hash_chain.py"
.github/workflows/history-anchor-verifier.yml:31:      - "tests/fixtures/history_anchor_verifier/**"
.github/workflows/history-anchor-verifier.yml:32:      - ".github/workflows/history-anchor-verifier.yml"
.github/workflows/history-anchor-verifier.yml:59:          # validate_chain → compute_entry_hash → canonical_json → rfc8785 의존성 답습
.github/workflows/history-anchor-verifier.yml:70:          python tools/history_anchor_verifier.py --list-attack-models \
.github/workflows/history-anchor-verifier.yml:83:          if ! grep -q "total_anchor_fields=11" group-c-followup-logs/list-attack.stderr; then
.github/workflows/history-anchor-verifier.yml:84:            echo "::error::total_anchor_fields != 11"
.github/workflows/history-anchor-verifier.yml:91:          if ! grep -q "anchor_field_count_compliant=True" group-c-followup-logs/list-attack.stderr; then
.github/workflows/history-anchor-verifier.yml:92:            echo "::error::anchor_field_count_compliant != True"
.github/workflows/history-anchor-verifier.yml:103:        id: anchor_pass_original
.github/workflows/history-anchor-verifier.yml:106:          python tools/history_anchor_verifier.py --mode anchor-verify \
.github/workflows/history-anchor-verifier.yml:107:            tests/fixtures/history_anchor_verifier/pass/original_anchor.json \
.github/workflows/history-anchor-verifier.yml:108:            > group-c-followup-logs/anchor-pass-original.stdout 2> group-c-followup-logs/anchor-pass-original.stderr
.github/workflows/history-anchor-verifier.yml:111:          cat group-c-followup-logs/anchor-pass-original.stderr
.github/workflows/history-anchor-verifier.yml:116:          if ! grep -q "violations=0" group-c-followup-logs/anchor-pass-original.stderr; then
.github/workflows/history-anchor-verifier.yml:120:          echo "anchor_pass_original=PASS" >> $GITHUB_OUTPUT
.github/workflows/history-anchor-verifier.yml:121:          echo "Anchor PASS original OK (rc=0, anchor matched)"
.github/workflows/history-anchor-verifier.yml:124:        id: anchor_pass_extended
.github/workflows/history-anchor-verifier.yml:127:          python tools/history_anchor_verifier.py --mode anchor-verify \
.github/workflows/history-anchor-verifier.yml:128:            tests/fixtures/history_anchor_verifier/pass/extended_anchor.json \
.github/workflows/history-anchor-verifier.yml:129:            > group-c-followup-logs/anchor-pass-extended.stdout 2> group-c-followup-logs/anchor-pass-extended.stderr
.github/workflows/history-anchor-verifier.yml:132:          cat group-c-followup-logs/anchor-pass-extended.stderr
.github/workflows/history-anchor-verifier.yml:137:          if ! grep -q "violations=0" group-c-followup-logs/anchor-pass-extended.stderr; then
.github/workflows/history-anchor-verifier.yml:141:          echo "anchor_pass_extended=PASS" >> $GITHUB_OUTPUT
.github/workflows/history-anchor-verifier.yml:144:      - name: Anchor FAIL — full rewrite (rc=1 + tail_hash_mismatch)
.github/workflows/history-anchor-verifier.yml:145:        id: anchor_fail_rewrite
.github/workflows/history-anchor-verifier.yml:148:          python tools/history_anchor_verifier.py --mode anchor-verify \
.github/workflows/history-anchor-verifier.yml:149:            tests/fixtures/history_anchor_verifier/fail/anchor_full_rewrite.json \
.github/workflows/history-anchor-verifier.yml:150:            > group-c-followup-logs/anchor-fail-rewrite.stdout 2> group-c-followup-logs/anchor-fail-rewrite.stderr
.github/workflows/history-anchor-verifier.yml:153:          cat group-c-followup-logs/anchor-fail-rewrite.stderr
.github/workflows/history-anchor-verifier.yml:155:            echo "::error::Anchor FAIL full rewrite expected rc=1, got rc=$rc"
.github/workflows/history-anchor-verifier.yml:158:          if ! grep -q "tail-hash-mismatch" group-c-followup-logs/anchor-fail-rewrite.stderr; then
.github/workflows/history-anchor-verifier.yml:159:            echo "::error::Anchor FAIL full rewrite missing 'tail-hash-mismatch'"
.github/workflows/history-anchor-verifier.yml:162:          echo "anchor_fail_rewrite=PASS" >> $GITHUB_OUTPUT
.github/workflows/history-anchor-verifier.yml:163:          echo "Anchor FAIL full rewrite OK (rc=1, tail-hash-mismatch detected)"
.github/workflows/history-anchor-verifier.yml:166:        id: anchor_fail_truncation
.github/workflows/history-anchor-verifier.yml:169:          python tools/history_anchor_verifier.py --mode anchor-verify \
.github/workflows/history-anchor-verifier.yml:170:            tests/fixtures/history_anchor_verifier/fail/anchor_tail_truncation.json \
.github/workflows/history-anchor-verifier.yml:171:            > group-c-followup-logs/anchor-fail-truncation.stdout 2> group-c-followup-logs/anchor-fail-truncation.stderr
.github/workflows/history-anchor-verifier.yml:174:          cat group-c-followup-logs/anchor-fail-truncation.stderr
.github/workflows/history-anchor-verifier.yml:180:            if ! grep -q "$pid" group-c-followup-logs/anchor-fail-truncation.stderr; then
.github/workflows/history-anchor-verifier.yml:185:          echo "anchor_fail_truncation=PASS" >> $GITHUB_OUTPUT
.github/workflows/history-anchor-verifier.yml:189:        id: anchor_fail_deletion
.github/workflows/history-anchor-verifier.yml:192:          python tools/history_anchor_verifier.py --mode anchor-verify \
.github/workflows/history-anchor-verifier.yml:193:            tests/fixtures/history_anchor_verifier/fail/anchor_middle_deletion.json \
.github/workflows/history-anchor-verifier.yml:194:            > group-c-followup-logs/anchor-fail-deletion.stdout 2> group-c-followup-logs/anchor-fail-deletion.stderr
.github/workflows/history-anchor-verifier.yml:197:          cat group-c-followup-logs/anchor-fail-deletion.stderr
.github/workflows/history-anchor-verifier.yml:203:            if ! grep -q "$pid" group-c-followup-logs/anchor-fail-deletion.stderr; then
.github/workflows/history-anchor-verifier.yml:208:          echo "anchor_fail_deletion=PASS" >> $GITHUB_OUTPUT
.github/workflows/history-anchor-verifier.yml:212:        id: anchor_fail_substitution
.github/workflows/history-anchor-verifier.yml:215:          python tools/history_anchor_verifier.py --mode anchor-verify \
.github/workflows/history-anchor-verifier.yml:216:            tests/fixtures/history_anchor_verifier/fail/anchor_substitution.json \
.github/workflows/history-anchor-verifier.yml:217:            > group-c-followup-logs/anchor-fail-substitution.stdout 2> group-c-followup-logs/anchor-fail-substitution.stderr
.github/workflows/history-anchor-verifier.yml:220:          cat group-c-followup-logs/anchor-fail-substitution.stderr
.github/workflows/history-anchor-verifier.yml:226:            if ! grep -q "$pid" group-c-followup-logs/anchor-fail-substitution.stderr; then
.github/workflows/history-anchor-verifier.yml:231:          echo "anchor_fail_substitution=PASS" >> $GITHUB_OUTPUT
.github/workflows/history-anchor-verifier.yml:234:      - name: Anchor FAIL — tampered anchor (rc=1 + anchor_self_inconsistent — known limitation)
.github/workflows/history-anchor-verifier.yml:235:        id: anchor_fail_tampered
.github/workflows/history-anchor-verifier.yml:238:          python tools/history_anchor_verifier.py --mode anchor-verify \
.github/workflows/history-anchor-verifier.yml:239:            tests/fixtures/history_anchor_verifier/fail/anchor_tampered.json \
.github/workflows/history-anchor-verifier.yml:240:            > group-c-followup-logs/anchor-fail-tampered.stdout 2> group-c-followup-logs/anchor-fail-tampered.stderr
.github/workflows/history-anchor-verifier.yml:243:          cat group-c-followup-logs/anchor-fail-tampered.stderr
.github/workflows/history-anchor-verifier.yml:248:          if ! grep -q "anchor-self-inconsistent" group-c-followup-logs/anchor-fail-tampered.stderr; then
.github/workflows/history-anchor-verifier.yml:249:            echo "::error::Anchor FAIL tampered missing 'anchor-self-inconsistent'"
.github/workflows/history-anchor-verifier.yml:252:          echo "anchor_fail_tampered=PASS" >> $GITHUB_OUTPUT
.github/workflows/history-anchor-verifier.yml:253:          echo "Anchor FAIL tampered OK (rc=1, anchor-self-inconsistent — known limitation: anchor signing 부재)"
.github/workflows/history-anchor-verifier.yml:259:          python tools/history_anchor_verifier.py --mode chain-only \
.github/workflows/history-anchor-verifier.yml:260:            tests/fixtures/history_anchor_verifier/chain_only_demo/full_rewrite_ledger.jsonl \
.github/workflows/history-anchor-verifier.yml:267:            echo "::error::만약 rc=1이면 Layer 1 *단독* 으로 full rewrite 검출됨 — 본 PoC evidence 가치 무효화"
.github/workflows/history-anchor-verifier.yml:270:          if ! grep -q "Layer 1 단독으로는 full rewrite" group-c-followup-logs/layer1-demo.stderr; then
.github/workflows/history-anchor-verifier.yml:283:          if grep -E "^(import|from)\s+(gnupg|pynacl|sigstore|cosign|tsa|rfc3161)" tools/history_anchor_verifier.py; then
.github/workflows/history-anchor-verifier.yml:288:          if grep -E "^(import|from)\s+(requests|httpx|aiohttp|urllib3)" tools/history_anchor_verifier.py; then
.github/workflows/history-anchor-verifier.yml:293:          if grep -E "requests\.(get|post)|httpx\.(get|post)|urllib\.request\.urlopen|gh\s+api\s+" tools/history_anchor_verifier.py; then
.github/workflows/history-anchor-verifier.yml:299:               tests/fixtures/history_anchor_verifier/ tools/history_anchor_verifier.py 2>/dev/null; then
.github/workflows/history-anchor-verifier.yml:316:            "anchor_pass_original": "${{ steps.anchor_pass_original.outputs.anchor_pass_original || 'FAIL' }}",
.github/workflows/history-anchor-verifier.yml:317:            "anchor_pass_extended": "${{ steps.anchor_pass_extended.outputs.anchor_pass_extended || 'FAIL' }}",
.github/workflows/history-anchor-verifier.yml:318:            "anchor_fail_rewrite": "${{ steps.anchor_fail_rewrite.outputs.anchor_fail_rewrite || 'FAIL' }}",
.github/workflows/history-anchor-verifier.yml:319:            "anchor_fail_truncation": "${{ steps.anchor_fail_truncation.outputs.anchor_fail_truncation || 'FAIL' }}",
.github/workflows/history-anchor-verifier.yml:320:            "anchor_fail_deletion": "${{ steps.anchor_fail_deletion.outputs.anchor_fail_deletion || 'FAIL' }}",
.github/workflows/history-anchor-verifier.yml:321:            "anchor_fail_substitution": "${{ steps.anchor_fail_substitution.outputs.anchor_fail_substitution || 'FAIL' }}",
.github/workflows/history-anchor-verifier.yml:322:            "anchor_fail_tampered": "${{ steps.anchor_fail_tampered.outputs.anchor_fail_tampered || 'FAIL' }}",
.github/workflows/history-anchor-verifier.yml:328:            "total_anchor_fields": "11",
.github/workflows/history-anchor-verifier.yml:329:            "anchor_method_supported": "ci_run_id (signed_tag / external_snapshot = 별도 합의)",
.github/workflows/history-anchor-verifier.yml:340:      - name: Upload history anchor verifier logs (artifact)
.github/workflows/history-anchor-verifier.yml:344:          name: history-anchor-verifier-evidence
.github/workflows/history-anchor-verifier.yml:356:            echo "- event: g4_history_rewrite_layer5_anchor"
.github/workflows/history-anchor-verifier.yml:358:            echo "- ledger_layer: Layer 5 — External anchor metadata (ADR-012 §2.8 답습)"
.github/workflows/history-anchor-verifier.yml:360:            echo "- anchor_pass_original: ${{ steps.anchor_pass_original.outputs.anchor_pass_original || 'FAIL' }}"
.github/workflows/history-anchor-verifier.yml:361:            echo "- anchor_pass_extended: ${{ steps.anchor_pass_extended.outputs.anchor_pass_extended || 'FAIL' }} (Layer 5 정상 운영 시제)"
.github/workflows/history-anchor-verifier.yml:362:            echo "- anchor_fail_rewrite: ${{ steps.anchor_fail_rewrite.outputs.anchor_fail_rewrite || 'FAIL' }}"
.github/workflows/history-anchor-verifier.yml:363:            echo "- anchor_fail_truncation: ${{ steps.anchor_fail_truncation.outputs.anchor_fail_truncation || 'FAIL' }}"
.github/workflows/history-anchor-verifier.yml:364:            echo "- anchor_fail_deletion: ${{ steps.anchor_fail_deletion.outputs.anchor_fail_deletion || 'FAIL' }}"
.github/workflows/history-anchor-verifier.yml:365:            echo "- anchor_fail_substitution: ${{ steps.anchor_fail_substitution.outputs.anchor_fail_substitution || 'FAIL' }}"
.github/workflows/history-anchor-verifier.yml:366:            echo "- anchor_fail_tampered: ${{ steps.anchor_fail_tampered.outputs.anchor_fail_tampered || 'FAIL' }} (known limitation: anchor signing 부재)"
.github/workflows/history-anchor-verifier.yml:373:            echo "- evidence_value: Layer 1 (Group C) 단독으로는 full rewrite/truncation/deletion/substitution 검출 불가 → Layer 5 anchor 의무성 (ADR-012 §2.8 답습)"

codex
선행 문서 대조 결과, G4 §4.4.1은 Layer 1/2/4를 mandatory로 정의하고 Layer 3/5는 현재 scope 밖으로 남깁니다. 다음은 실제 PoC가 “시제 충족” 수준인지, 아니면 PASS evidence로 오인될 위험이 있는지를 로컬 실행으로 확인하겠습니다.
exec
/bin/bash -lc 'python tools/jsonl_hash_chain.py tests/fixtures/jsonl_ledger/pass/minimal_chain.jsonl && python tools/jsonl_hash_chain.py tests/fixtures/jsonl_ledger/pass/roundtrip_t2_strict.jsonl' in /home/delangi/문서/project/category/AI_development_tool
 exited 127 in 0ms:
/bin/bash: line 1: python: command not found

exec
/bin/bash -lc 'for f in tests/fixtures/jsonl_ledger/fail/*.jsonl; do python tools/jsonl_hash_chain.py "$f" >/tmp/hash.out 2>/tmp/hash.err; rc=$?; printf '"'%s rc=%s\\n' \""'$f" "$rc"; sed -n '"'1,6p' /tmp/hash.err; done" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
tests/fixtures/jsonl_ledger/fail/genesis_mismatch.jsonl rc=127
/bin/bash: line 1: python: command not found
tests/fixtures/jsonl_ledger/fail/hash_recalculation.jsonl rc=127
/bin/bash: line 1: python: command not found
tests/fixtures/jsonl_ledger/fail/missing_event_field.jsonl rc=127
/bin/bash: line 1: python: command not found
tests/fixtures/jsonl_ledger/fail/prev_hash_mismatch.jsonl rc=127
/bin/bash: line 1: python: command not found

exec
/bin/bash -lc 'for inp in tests/canonical/*/*.input.json; do base=${inp%.input.json}; python tools/canonical_json.py --mode cross_check --input "$inp" --expected-canonical "${base}.expected.canonical" --expected-sha256 "${base}.expected.sha256" >/dev/null || exit 1; done; echo canonical_cross_check_all_pass' in /home/delangi/문서/project/category/AI_development_tool
 exited 1 in 0ms:
/bin/bash: line 1: python: command not found

exec
/bin/bash -lc 'git remote -v && git branch --show-current && gh repo view --json nameWithOwner,defaultBranchRef 2>/tmp/gh.err || { rc=$?; printf '"'gh_failed rc=%s\\n' \""'$rc"; sed -n '"'1,20p' /tmp/gh.err; }" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 784ms:
{"defaultBranchRef":{"name":"main"},"nameWithOwner":"jokwangwon/AI_development_tool"}

codex
로컬에서는 `python` 명령이 없고 `python3`만 있는 환경입니다. 그래서 PoC 실행 판정은 `python3`로 재시도하고, GitHub remote의 default branch protection 상태도 `gh`로 가능한 범위에서 직접 조회하겠습니다.
exec
/bin/bash -lc 'python3 tools/jsonl_hash_chain.py tests/fixtures/jsonl_ledger/pass/minimal_chain.jsonl && python3 tools/jsonl_hash_chain.py tests/fixtures/jsonl_ledger/pass/roundtrip_t2_strict.jsonl' in /home/delangi/문서/project/category/AI_development_tool
 exited 1 in 0ms:
FAIL: minimal_chain.jsonl — 2 violation(s):
  [0] id=11111111-1111-4111-8111-111111111111 type=schema_canonical_error
      detail: canonical_json failed: rfc8785 라이브러리 미설치 — `pip install rfc8785==0.1.4`
  [1] id=22222222-2222-4222-8222-222222222222 type=schema_canonical_error
      detail: canonical_json failed: rfc8785 라이브러리 미설치 — `pip install rfc8785==0.1.4`

exec
/bin/bash -lc 'for f in tests/fixtures/jsonl_ledger/fail/*.jsonl; do python3 tools/jsonl_hash_chain.py "$f" >/tmp/hash.out 2>/tmp/hash.err; rc=$?; printf '"'%s rc=%s\\n' \""'$f" "$rc"; sed -n '"'1,12p' /tmp/hash.err; done" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
tests/fixtures/jsonl_ledger/fail/genesis_mismatch.jsonl rc=1
FAIL: genesis_mismatch.jsonl — 1 violation(s):
  [0] id=ffffffff-ffff-4fff-8fff-ffffffffffff type=schema_canonical_error
      detail: canonical_json failed: rfc8785 라이브러리 미설치 — `pip install rfc8785==0.1.4`
tests/fixtures/jsonl_ledger/fail/hash_recalculation.jsonl rc=1
FAIL: hash_recalculation.jsonl — 2 violation(s):
  [0] id=cccccccc-cccc-4ccc-8ccc-cccccccccccc type=schema_canonical_error
      detail: canonical_json failed: rfc8785 라이브러리 미설치 — `pip install rfc8785==0.1.4`
  [1] id=dddddddd-dddd-4ddd-8ddd-dddddddddddd type=schema_canonical_error
      detail: canonical_json failed: rfc8785 라이브러리 미설치 — `pip install rfc8785==0.1.4`
tests/fixtures/jsonl_ledger/fail/missing_event_field.jsonl rc=1
FAIL: missing_event_field.jsonl — 1 violation(s):
  [0] id=eeeeeeee-eeee-4eee-8eee-eeeeeeeeeeee type=schema_missing_field
      detail: missing required fields: ['event']
tests/fixtures/jsonl_ledger/fail/prev_hash_mismatch.jsonl rc=1
FAIL: prev_hash_mismatch.jsonl — 2 violation(s):
  [0] id=aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa type=schema_canonical_error
      detail: canonical_json failed: rfc8785 라이브러리 미설치 — `pip install rfc8785==0.1.4`
  [1] id=bbbbbbbb-bbbb-4bbb-8bbb-bbbbbbbbbbbb type=schema_canonical_error
      detail: canonical_json failed: rfc8785 라이브러리 미설치 — `pip install rfc8785==0.1.4`

exec
/bin/bash -lc 'for inp in tests/canonical/*/*.input.json; do base=${inp%.input.json}; python3 tools/canonical_json.py --mode cross_check --input "$inp" --expected-canonical "${base}.expected.canonical" --expected-sha256 "${base}.expected.sha256" >/dev/null || exit 1; done; echo canonical_cross_check_all_pass' in /home/delangi/문서/project/category/AI_development_tool
 exited 1 in 0ms:
CANONICAL_ERROR: rfc8785 라이브러리 미설치 — `pip install rfc8785==0.1.4`

exec
/bin/bash -lc 'gh api repos/jokwangwon/AI_development_tool/branches/main/protection 2>/tmp/protect.err || { rc=$?; printf '"'protection_query_failed rc=%s\\n' \""'$rc"; sed -n '"'1,40p' /tmp/protect.err; }" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 362ms:
{"url":"https://api.github.com/repos/jokwangwon/AI_development_tool/branches/main/protection","required_status_checks":{"url":"https://api.github.com/repos/jokwangwon/AI_development_tool/branches/main/protection/required_status_checks","strict":true,"contexts":["guard","verify","feasibility","scan","enforce","defense","validate","bypass-detect"],"contexts_url":"https://api.github.com/repos/jokwangwon/AI_development_tool/branches/main/protection/required_status_checks/contexts","checks":[{"context":"guard","app_id":15368},{"context":"verify","app_id":15368},{"context":"feasibility","app_id":15368},{"context":"scan","app_id":15368},{"context":"enforce","app_id":15368},{"context":"defense","app_id":15368},{"context":"validate","app_id":15368},{"context":"bypass-detect","app_id":15368}]},"required_pull_request_reviews":{"url":"https://api.github.com/repos/jokwangwon/AI_development_tool/branches/main/protection/required_pull_request_reviews","dismiss_stale_reviews":false,"require_code_owner_reviews":false,"require_last_push_approval":false,"required_approving_review_count":0},"required_signatures":{"url":"https://api.github.com/repos/jokwangwon/AI_development_tool/branches/main/protection/required_signatures","enabled":false},"enforce_admins":{"url":"https://api.github.com/repos/jokwangwon/AI_development_tool/branches/main/protection/enforce_admins","enabled":true},"required_linear_history":{"enabled":false},"allow_force_pushes":{"enabled":false},"allow_deletions":{"enabled":false},"block_creations":{"enabled":false},"required_conversation_resolution":{"enabled":false},"lock_branch":{"enabled":false},"allow_fork_syncing":{"enabled":false}}
exec
/bin/bash -lc 'rg -n "rfc8785|jcs|requirements|pyproject|pip install" -S .github/workflows tools tests pyproject.toml requirements*.txt setup.cfg setup.py 2>/dev/null' in /home/delangi/문서/project/category/AI_development_tool
 exited 2 in 0ms:
requirements-dev.txt:9:# pyproject.toml (PEP 621) 신설은 *별도 합의* 답습 (R-RF2 답습).
requirements-dev.txt:15:# Group C PoC — RFC 8785 JCS Primary 1 + Primary 2 cross-check
requirements-dev.txt:17:#   - docs/review/3plus1-consensus-2026-05-10-g4-jcs-library-selection.md (Q1 풀 3+1 합의 17 조건)
requirements-dev.txt:18:#   - docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md §3 (사용자 명시 결정 갱신 — pyjcs PyPI 미존재 → jcs 대체)
requirements-dev.txt:20:rfc8785==0.1.4
requirements-dev.txt:21:jcs==0.2.1
.github/workflows/g4-hash-chain.yml:1:# G4 JSONL Hash Chain + RFC 8785 JCS + Round-trip — Group C PoC
.github/workflows/g4-hash-chain.yml:4:#   - docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md (본 PoC 사양 §6)
.github/workflows/g4-hash-chain.yml:5:#   - docs/review/3plus1-consensus-2026-05-10-g4-jcs-library-selection.md (Q1 풀 3+1 합의 17 조건)
.github/workflows/g4-hash-chain.yml:7:#   - docs/decisions/ADR-012-evidence-ledger-protection.md §2.5 (RFC 8785 JCS Primary + jq fallback + corpus 검증)
.github/workflows/g4-hash-chain.yml:12:#   - corpus 24 회귀 (Primary 1 rfc8785 + Primary 2 jcs cross-check + sha256 일관성)
.github/workflows/g4-hash-chain.yml:19:name: G4 Hash Chain + JCS
.github/workflows/g4-hash-chain.yml:34:      - "requirements-dev.txt"
.github/workflows/g4-hash-chain.yml:66:          python -m pip install --upgrade pip
.github/workflows/g4-hash-chain.yml:68:          pip install rfc8785==0.1.4 jcs==0.2.1
.github/workflows/g4-hash-chain.yml:69:          python -c "import rfc8785, jcs; print('rfc8785:', rfc8785.__file__); print('jcs:', jcs.__file__)"
.github/workflows/g4-hash-chain.yml:71:      - name: Corpus regression — Primary 1 (rfc8785) byte + sha256
.github/workflows/g4-hash-chain.yml:92:            echo "::error::Primary 1 (rfc8785) corpus regression: $fail / $total cases failed"
.github/workflows/g4-hash-chain.yml:96:      - name: Corpus regression — Primary 2 (jcs) cross-check (TR-C-2 답습)
.github/workflows/g4-hash-chain.yml:116:            echo "::error::Primary 2 (jcs) corpus regression: $fail / $total cases failed (TR-C-2 escalation)"
.github/workflows/g4-hash-chain.yml:168:          import rfc8785, jcs
.github/workflows/g4-hash-chain.yml:171:              for libname, fn in [("rfc8785", lambda v: rfc8785.dumps({"n": v})),
.github/workflows/g4-hash-chain.yml:172:                                  ("jcs", lambda v: jcs.canonicalize({"n": v}))]:
.github/workflows/g4-hash-chain.yml:246:          echo "## G4 Hash Chain + JCS — Evidence" >> $GITHUB_STEP_SUMMARY
.github/workflows/g4-hash-chain.yml:250:          echo "- event: g4_hash_chain_jcs_layer1" >> $GITHUB_STEP_SUMMARY
.github/workflows/g4-hash-chain.yml:256:          echo "- numeric reject: NaN + Inf + -Inf (rfc8785 + jcs)" >> $GITHUB_STEP_SUMMARY
.github/workflows/secret-hygiene-egress-redaction.yml:47:      - "requirements-dev.txt"
.github/workflows/secret-hygiene-egress-redaction.yml:310:          pip install detect-secrets==1.5.0
tools/canonical_json.py:2:"""Canonical JSON (RFC 8785 JCS) — Group C PoC (G4 통합).
tools/canonical_json.py:5:  - docs/decisions/ADR-012-evidence-ledger-protection.md §2.5 (RFC 8785 JCS Primary + jq fallback + corpus 검증 ≥20개)
tools/canonical_json.py:7:  - docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md §3 (사용자 명시 결정 갱신 — rfc8785 + jcs 병렬 cross-check)
tools/canonical_json.py:8:  - docs/review/3plus1-consensus-2026-05-10-g4-jcs-library-selection.md (Q1 풀 3+1 합의 17 조건)
tools/canonical_json.py:12:  - Primary 1: rfc8785 (Trail of Bits, Apache-2.0, RA-9 §B.2 11/11 sanity PASS)
tools/canonical_json.py:13:  - Primary 2: jcs (titusz, Apache-2.0, RA-9 §B.2 11/11 sanity PASS)
tools/canonical_json.py:34:    import rfc8785  # Primary 1 (Trail of Bits)
tools/canonical_json.py:36:    rfc8785 = None  # type: ignore[assignment]
tools/canonical_json.py:39:    import jcs  # Primary 2 (titusz)
tools/canonical_json.py:41:    jcs = None  # type: ignore[assignment]
tools/canonical_json.py:47:    - PRIMARY_1_ONLY: rfc8785 단독 사용 (runtime 1× 권고)
tools/canonical_json.py:48:    - PRIMARY_2_ONLY: jcs 단독 사용 (테스트/디버깅용)
tools/canonical_json.py:49:    - CROSS_CHECK: rfc8785 + jcs 동시 호출, 출력 byte 동등성 + sha256 동등성 강제 (corpus 시점 권고)
tools/canonical_json.py:64:    """rfc8785 + jcs cross-check 출력 불일치 — TR-C-2 escalation trigger."""
tools/canonical_json.py:78:def _to_canonical_rfc8785(obj: Any) -> bytes:
tools/canonical_json.py:79:    """Primary 1 — rfc8785 (Trail of Bits)."""
tools/canonical_json.py:80:    if rfc8785 is None:
tools/canonical_json.py:81:        raise CanonicalizationError("rfc8785 라이브러리 미설치 — `pip install rfc8785==0.1.4`")
tools/canonical_json.py:82:    out = rfc8785.dumps(obj)
tools/canonical_json.py:86:def _to_canonical_jcs(obj: Any) -> bytes:
tools/canonical_json.py:87:    """Primary 2 — jcs (titusz)."""
tools/canonical_json.py:88:    if jcs is None:
tools/canonical_json.py:89:        raise CanonicalizationError("jcs 라이브러리 미설치 — `pip install jcs==0.2.1`")
tools/canonical_json.py:90:    out = jcs.canonicalize(obj)
tools/canonical_json.py:127:        mode: CrossCheckMode (기본 PRIMARY_1_ONLY — rfc8785 단독, runtime 1× 권고)
tools/canonical_json.py:134:        CrossCheckMismatchError: CROSS_CHECK 모드에서 rfc8785 ↔ jcs 출력 불일치 (TR-C-2 trigger)
tools/canonical_json.py:140:        canonical = _to_canonical_rfc8785(obj)
tools/canonical_json.py:142:        canonical = _to_canonical_jcs(obj)
tools/canonical_json.py:144:        out_p1 = _to_canonical_rfc8785(obj)
tools/canonical_json.py:145:        out_p2 = _to_canonical_jcs(obj)
tools/canonical_json.py:148:                f"rfc8785 ↔ jcs cross-check 불일치 — TR-C-2 escalation. "
tools/canonical_json.py:149:                f"rfc8785={out_p1[:80]!r} jcs={out_p2[:80]!r}"
tools/canonical_json.py:172:        description="Canonical JSON (RFC 8785 JCS) — Group C PoC validator"
.github/workflows/provider-adapter-enforcement.yml:11:#   - .importlinter (config) + requirements-dev.txt (TR-2 답습)
.github/workflows/provider-adapter-enforcement.yml:37:      - "requirements-dev.txt"
.github/workflows/provider-adapter-enforcement.yml:94:          pip install -r requirements-dev.txt
.github/workflows/memory-skill-migration-feasibility.yml:33:      - "requirements-dev.txt"
.github/workflows/memory-skill-migration-feasibility.yml:57:      - name: Install Group C deps (rfc8785 + jcs — 답습 import 직접)
.github/workflows/memory-skill-migration-feasibility.yml:59:          python -m pip install --upgrade pip
.github/workflows/memory-skill-migration-feasibility.yml:61:          pip install rfc8785==0.1.4 jcs==0.2.1
.github/workflows/memory-skill-migration-feasibility.yml:62:          python -c "import rfc8785, jcs; print('rfc8785:', rfc8785.__file__); print('jcs:', jcs.__file__)"
.github/workflows/pre-commit-bypass-detection.yml:71:          python -m pip install --upgrade pip
.github/workflows/pre-commit-bypass-detection.yml:72:          pip install pre-commit==4.0.1
.github/workflows/history-anchor-verifier.yml:56:      - name: Install Group C deps (rfc8785 + jcs — Group C `compute_entry_hash` 의존)
.github/workflows/history-anchor-verifier.yml:58:          python -m pip install --upgrade pip
.github/workflows/history-anchor-verifier.yml:59:          # validate_chain → compute_entry_hash → canonical_json → rfc8785 의존성 답습
.github/workflows/history-anchor-verifier.yml:60:          pip install rfc8785==0.1.4 jcs==0.2.1
.github/workflows/history-anchor-verifier.yml:61:          python -c "import rfc8785, jcs; print('rfc8785 + jcs OK')"
tools/memory_skill_roundtrip.py:6:  - tools/canonical_json.py (RFC 8785 JCS canonical JSON — Group C)
.github/workflows/rewrite-defense.yml:6:#   - .github/workflows/history-anchor-verifier.yml (Group C 후속 형식 직접 답습 — rfc8785+jcs install 포함)
.github/workflows/rewrite-defense.yml:57:      - name: Install Group C deps (rfc8785 + jcs — Group C `parse_jsonl` 의존)
.github/workflows/rewrite-defense.yml:59:          python -m pip install --upgrade pip
.github/workflows/rewrite-defense.yml:60:          # parse_jsonl → canonical_json → rfc8785 의존성 답습
.github/workflows/rewrite-defense.yml:61:          pip install rfc8785==0.1.4 jcs==0.2.1
.github/workflows/rewrite-defense.yml:62:          python -c "import rfc8785, jcs; print('rfc8785 + jcs OK')"
tools/jsonl_roundtrip.py:7:  - docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md §4.3 (JSONL → JSONL 동일 형식 한정)
tools/jsonl_roundtrip.py:67:    각 entry 는 canonical JSON (rfc8785) 으로 직렬화 후 newline join.
tools/jsonl_hash_chain.py:9:  - docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md §2 / §4.2
tools/jsonl_hash_chain.py:10:  - tools/canonical_json.py (Q1 합의 답습 — rfc8785 + jcs 병렬 cross-check)
tools/jsonl_hash_chain.py:96:    Q1 합의 답습 — runtime mode = PRIMARY_1_ONLY (rfc8785 단독), corpus 시점 cross-check 별도.
tools/pre_commit_install_audit.sh:47:    echo "  [FAIL] pre-commit 명령 PATH 부재 → pip install 미실행 의심"

exec
/bin/bash -lc "sed -n '1,220p' tools/jsonl_hash_chain.py" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
#!/usr/bin/env python3
"""JSONL ledger hash chain validator — Group C PoC (G4 통합).

답습 출처:
  - docs/decisions/ADR-012-evidence-ledger-protection.md §2.2 (event 11번째 필드 17 enum) /
    §2.3 (Append-only + Hash Chain Layer 1) / §2.6 (Genesis Hash MVP) /
    §2.7 (prev_hash 검증 실패 BLOCK + manual + violation entry)
  - docs/architecture/provider-agnostic-memory-skill-design.md §4.2 (11 필드) / §4.4 (hash chain)
  - docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md §2 / §4.2
  - tools/canonical_json.py (Q1 합의 답습 — rfc8785 + jcs 병렬 cross-check)

핵심 강제 조건:
  - 11 필드 schema (type / scope / id / schema_version / ts / agent / event / content / evidence_refs / prev_hash / hash)
  - schema_version != "0.1" → BLOCK (ADR-012 §2.10 답습)
  - Genesis hash = sha256("genesis:<scope>:<schema_version>") (ADR-012 §2.6 MVP)
  - hash 계산 = sha256(canonical_json(entry - "hash" field))
  - prev_hash 검증 실패 = BLOCK + chain_violation_detected entry 자동 작성
  - violation_type 4종: prev_hash_mismatch / hash_recalculation / history_rewrite / genesis_mismatch
  - timestamp monotonicity: 본 entry ts >= prev_hash entry ts (ADR-012 §3.4)
  - T3 자동 정책 변경 금지 (ADR-011 §2.4) — 자동 revert 0건, BLOCK + manual

종료 코드:
  0 = 모든 검사 PASS
  1 = 1+ violation 검출
  2 = invalid input (parse 실패 등)
"""
from __future__ import annotations

import argparse
import dataclasses
import datetime as dt
import hashlib
import json
import sys
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any

from canonical_json import (  # type: ignore[import-not-found]
    CanonicalizationError,
    CrossCheckMode,
    to_canonical,
)

REQUIRED_FIELDS: tuple[str, ...] = (
    "type",
    "scope",
    "id",
    "schema_version",
    "ts",
    "agent",
    "event",
    "content",
    "evidence_refs",
    "prev_hash",
    "hash",
)

ALLOWED_TYPES: tuple[str, ...] = ("memory", "skill", "meta")
ALLOWED_SCOPES: tuple[str, ...] = ("global", "project", "session")
ALLOWED_AGENTS: tuple[str, ...] = ("user", "claude-code", "hermes", "external_llm")
SUPPORTED_SCHEMA_VERSION: str = "0.1"


class ViolationType(str, Enum):
    """Chain violation 4종 (ADR-012 §2.7 답습)."""

    PREV_HASH_MISMATCH = "prev_hash_mismatch"
    HASH_RECALCULATION = "hash_recalculation"
    HISTORY_REWRITE = "history_rewrite"
    GENESIS_MISMATCH = "genesis_mismatch"


@dataclass
class Violation:
    """Single violation report."""

    entry_index: int
    entry_id: str
    violation_type: str  # ViolationType.value or "schema_*" / "monotonicity_*"
    detail: str


def compute_genesis_hash(scope: str, schema_version: str) -> str:
    """Genesis hash MVP — sha256("genesis:<scope>:<schema_version>") (ADR-012 §2.6).

    schema_version 0.2 이상 진입 시 별도 chain (별도 chain_id 또는 schema_version) — 별도 합의 영역.
    """
    return hashlib.sha256(f"genesis:{scope}:{schema_version}".encode("utf-8")).hexdigest()


def compute_entry_hash(entry: dict[str, Any]) -> str:
    """Entry hash = sha256(canonical_json(entry - "hash" field)).

    Q1 합의 답습 — runtime mode = PRIMARY_1_ONLY (rfc8785 단독), corpus 시점 cross-check 별도.
    """
    payload = {k: v for k, v in entry.items() if k != "hash"}
    result = to_canonical(payload, mode=CrossCheckMode.PRIMARY_1_ONLY)
    return result.sha256_hex


def parse_iso8601(s: str) -> dt.datetime:
    """ISO 8601 timestamp parse — 'Z' suffix 정규화."""
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    return dt.datetime.fromisoformat(s)


def validate_schema(entry: dict[str, Any], index: int) -> list[Violation]:
    """11 필드 schema validation."""
    vios: list[Violation] = []
    entry_id = str(entry.get("id", f"<index={index}>"))

    missing = [f for f in REQUIRED_FIELDS if f not in entry]
    if missing:
        vios.append(
            Violation(
                entry_index=index,
                entry_id=entry_id,
                violation_type="schema_missing_field",
                detail=f"missing required fields: {missing}",
            )
        )
        return vios

    if entry["type"] not in ALLOWED_TYPES:
        vios.append(
            Violation(index, entry_id, "schema_invalid_type", f"type={entry['type']!r} not in {ALLOWED_TYPES}")
        )
    if entry["scope"] not in ALLOWED_SCOPES:
        vios.append(
            Violation(index, entry_id, "schema_invalid_scope", f"scope={entry['scope']!r} not in {ALLOWED_SCOPES}")
        )
    if entry["agent"] not in ALLOWED_AGENTS:
        vios.append(
            Violation(index, entry_id, "schema_invalid_agent", f"agent={entry['agent']!r} not in {ALLOWED_AGENTS}")
        )
    if entry["schema_version"] != SUPPORTED_SCHEMA_VERSION:
        vios.append(
            Violation(
                index,
                entry_id,
                "schema_version_unsupported",
                f"schema_version={entry['schema_version']!r} != {SUPPORTED_SCHEMA_VERSION!r} (ADR-012 §2.10)",
            )
        )
    if not isinstance(entry["evidence_refs"], list):
        vios.append(
            Violation(index, entry_id, "schema_invalid_evidence_refs", "evidence_refs must be list")
        )
    if not isinstance(entry["content"], (dict, list, str, int, float, bool)) and entry["content"] is not None:
        vios.append(
            Violation(index, entry_id, "schema_invalid_content", "content must be JSON-serializable")
        )

    try:
        parse_iso8601(entry["ts"])
    except (ValueError, TypeError) as e:
        vios.append(Violation(index, entry_id, "schema_invalid_ts", f"ts parse error: {e}"))

    return vios


def validate_chain(entries: list[dict[str, Any]]) -> list[Violation]:
    """Genesis + prev_hash ↔ hash chain + timestamp monotonicity 검증."""
    vios: list[Violation] = []
    if not entries:
        return vios

    prev_ts: dt.datetime | None = None
    prev_hash_actual: str | None = None

    for i, entry in enumerate(entries):
        entry_id = str(entry.get("id", f"<index={i}>"))

        # Hash recalculation 검증
        try:
            recomputed = compute_entry_hash(entry)
        except CanonicalizationError as e:
            vios.append(
                Violation(i, entry_id, "schema_canonical_error", f"canonical_json failed: {e}")
            )
            continue

        if recomputed != entry.get("hash"):
            vios.append(
                Violation(
                    i,
                    entry_id,
                    ViolationType.HASH_RECALCULATION.value,
                    f"hash field={entry.get('hash')!r} != recomputed={recomputed!r}",
                )
            )

        # prev_hash 검증
        if i == 0:
            expected_genesis = compute_genesis_hash(entry["scope"], entry["schema_version"])
            if entry["prev_hash"] != expected_genesis:
                vios.append(
                    Violation(
                        i,
                        entry_id,
                        ViolationType.GENESIS_MISMATCH.value,
                        f"first entry prev_hash={entry['prev_hash']!r} != genesis={expected_genesis!r}",
                    )
                )
        else:
            if entry["prev_hash"] != prev_hash_actual:
                vios.append(
                    Violation(
                        i,
                        entry_id,
                        ViolationType.PREV_HASH_MISMATCH.value,
                        f"prev_hash={entry['prev_hash']!r} != prior entry hash={prev_hash_actual!r}",
                    )
                )

        # Timestamp monotonicity (ADR-012 §3.4)
        try:

exec
/bin/bash -lc "sed -n '1,220p' tools/canonical_json.py" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
#!/usr/bin/env python3
"""Canonical JSON (RFC 8785 JCS) — Group C PoC (G4 통합).

답습 출처:
  - docs/decisions/ADR-012-evidence-ledger-protection.md §2.5 (RFC 8785 JCS Primary + jq fallback + corpus 검증 ≥20개)
  - docs/architecture/provider-agnostic-memory-skill-design.md §4.4.2 (Canonical JSON 보강)
  - docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md §3 (사용자 명시 결정 갱신 — rfc8785 + jcs 병렬 cross-check)
  - docs/review/3plus1-consensus-2026-05-10-g4-jcs-library-selection.md (Q1 풀 3+1 합의 17 조건)
  - docs/review/3plus1-consensus-2026-05-10-g4-corpus-poc-scope-short.md (Q2/Q3 단축 합의 6 조건)

핵심 강제 조건:
  - Primary 1: rfc8785 (Trail of Bits, Apache-2.0, RA-9 §B.2 11/11 sanity PASS)
  - Primary 2: jcs (titusz, Apache-2.0, RA-9 §B.2 11/11 sanity PASS)
  - Fallback: jq -S -c (POSIX 표준, ADR-012 §2.5 명시 답습)
  - cross-check 시점 = corpus 시점 강제 (TR-C-2 trigger 답습 — Q1 합의 D-1)
  - cross-check 시점 runtime = 본 PoC 호출자 결정 (Mode 옵션 제공, 기본 = Mode 1 단독 + corpus 시점 cross-check)
  - Fallback 사용 시 = `event: canonical_json_fallback` ledger entry 작성 의무 (caller 책임)

본 모듈 = Hermes 의존 0 (ADR-008 차단조건 #2 답습) — POSIX + Python stdlib + provider-neutral PyPI 한정.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from enum import Enum
from typing import Any

try:
    import rfc8785  # Primary 1 (Trail of Bits)
except ImportError:
    rfc8785 = None  # type: ignore[assignment]

try:
    import jcs  # Primary 2 (titusz)
except ImportError:
    jcs = None  # type: ignore[assignment]


class CrossCheckMode(str, Enum):
    """Cross-check mode — Q1 합의 D-1 답습 (corpus 시점 강제 + runtime 호출자 결정).

    - PRIMARY_1_ONLY: rfc8785 단독 사용 (runtime 1× 권고)
    - PRIMARY_2_ONLY: jcs 단독 사용 (테스트/디버깅용)
    - CROSS_CHECK: rfc8785 + jcs 동시 호출, 출력 byte 동등성 + sha256 동등성 강제 (corpus 시점 권고)
    - FALLBACK_JQ: jq -S -c subprocess (Primary install 실패 시, canonical_json_fallback entry 의무)
    """

    PRIMARY_1_ONLY = "primary_1_only"
    PRIMARY_2_ONLY = "primary_2_only"
    CROSS_CHECK = "cross_check"
    FALLBACK_JQ = "fallback_jq"


class CanonicalizationError(Exception):
    """Canonical JSON 생성 실패 (NaN/Inf/cross-check mismatch 등)."""


class CrossCheckMismatchError(CanonicalizationError):
    """rfc8785 + jcs cross-check 출력 불일치 — TR-C-2 escalation trigger."""


@dataclass
class CanonicalResult:
    """Canonicalization 결과 + audit trail."""

    canonical: bytes
    sha256_hex: str
    mode_used: CrossCheckMode
    fallback_used: bool = False
    cross_check_passed: bool | None = None  # None = N/A, True/False = cross-check 결과


def _to_canonical_rfc8785(obj: Any) -> bytes:
    """Primary 1 — rfc8785 (Trail of Bits)."""
    if rfc8785 is None:
        raise CanonicalizationError("rfc8785 라이브러리 미설치 — `pip install rfc8785==0.1.4`")
    out = rfc8785.dumps(obj)
    return out if isinstance(out, bytes) else out.encode("utf-8")


def _to_canonical_jcs(obj: Any) -> bytes:
    """Primary 2 — jcs (titusz)."""
    if jcs is None:
        raise CanonicalizationError("jcs 라이브러리 미설치 — `pip install jcs==0.2.1`")
    out = jcs.canonicalize(obj)
    return out if isinstance(out, bytes) else out.encode("utf-8")


def _to_canonical_jq_fallback(obj: Any) -> bytes:
    """Fallback — jq -S -c subprocess.

    POSIX 표준 도구, ADR-012 §2.5 명시. 본 함수 호출 후 caller 는
    `event: canonical_json_fallback` ledger entry 작성 의무.
    """
    jq_path = shutil.which("jq")
    if jq_path is None:
        raise CanonicalizationError(
            "jq fallback 불가 — `jq` POSIX 도구 미설치 (apt install jq / brew install jq)"
        )
    input_json = json.dumps(obj, allow_nan=False).encode("utf-8")
    try:
        result = subprocess.run(
            [jq_path, "-S", "-c", "."],
            input=input_json,
            capture_output=True,
            check=True,
            timeout=30,
        )
    except subprocess.CalledProcessError as e:
        raise CanonicalizationError(
            f"jq fallback subprocess 실패 — rc={e.returncode} stderr={e.stderr.decode('utf-8', 'replace')[:200]}"
        ) from e
    out = result.stdout.rstrip(b"\n")
    return out


def to_canonical(obj: Any, mode: CrossCheckMode = CrossCheckMode.PRIMARY_1_ONLY) -> CanonicalResult:
    """Canonical JSON 생성 + audit trail.

    Args:
        obj: 입력 Python object (dict / list / str / int / float / bool / None)
        mode: CrossCheckMode (기본 PRIMARY_1_ONLY — rfc8785 단독, runtime 1× 권고)

    Returns:
        CanonicalResult (canonical bytes + sha256 hex + mode used + fallback/cross-check flag)

    Raises:
        CanonicalizationError: NaN/Inf reject 또는 라이브러리 미설치 또는 jq 실패
        CrossCheckMismatchError: CROSS_CHECK 모드에서 rfc8785 ↔ jcs 출력 불일치 (TR-C-2 trigger)
    """
    fallback_used = False
    cross_check_passed: bool | None = None

    if mode == CrossCheckMode.PRIMARY_1_ONLY:
        canonical = _to_canonical_rfc8785(obj)
    elif mode == CrossCheckMode.PRIMARY_2_ONLY:
        canonical = _to_canonical_jcs(obj)
    elif mode == CrossCheckMode.CROSS_CHECK:
        out_p1 = _to_canonical_rfc8785(obj)
        out_p2 = _to_canonical_jcs(obj)
        if out_p1 != out_p2:
            raise CrossCheckMismatchError(
                f"rfc8785 ↔ jcs cross-check 불일치 — TR-C-2 escalation. "
                f"rfc8785={out_p1[:80]!r} jcs={out_p2[:80]!r}"
            )
        canonical = out_p1
        cross_check_passed = True
    elif mode == CrossCheckMode.FALLBACK_JQ:
        canonical = _to_canonical_jq_fallback(obj)
        fallback_used = True
    else:
        raise CanonicalizationError(f"알 수 없는 mode: {mode}")

    sha256_hex = hashlib.sha256(canonical).hexdigest()
    return CanonicalResult(
        canonical=canonical,
        sha256_hex=sha256_hex,
        mode_used=mode,
        fallback_used=fallback_used,
        cross_check_passed=cross_check_passed,
    )


def _cli() -> int:
    """CLI — corpus 회귀 + cross-check + fallback 동등성 검증."""
    p = argparse.ArgumentParser(
        description="Canonical JSON (RFC 8785 JCS) — Group C PoC validator"
    )
    p.add_argument(
        "--mode",
        choices=[m.value for m in CrossCheckMode],
        default=CrossCheckMode.CROSS_CHECK.value,
        help="Cross-check mode (default: cross_check)",
    )
    p.add_argument(
        "--input",
        type=str,
        default="-",
        help="입력 JSON 파일 경로 (- = stdin)",
    )
    p.add_argument(
        "--expected-canonical",
        type=str,
        default=None,
        help="기대 canonical 출력 파일 (있으면 byte 비교)",
    )
    p.add_argument(
        "--expected-sha256",
        type=str,
        default=None,
        help="기대 sha256 hex 파일 (있으면 비교)",
    )
    p.add_argument(
        "--verify-fallback-equiv",
        action="store_true",
        help="jq fallback 출력과 byte 동등성 검증",
    )
    args = p.parse_args()

    try:
        if args.input == "-":
            input_text = sys.stdin.read()
        else:
            with open(args.input, "r", encoding="utf-8") as f:
                input_text = f.read()
        obj = json.loads(input_text)
    except (OSError, json.JSONDecodeError) as e:
        print(f"INPUT_ERROR: {e}", file=sys.stderr)
        return 2

    try:
        result = to_canonical(obj, mode=CrossCheckMode(args.mode))
    except CrossCheckMismatchError as e:
        print(f"CROSS_CHECK_MISMATCH: {e}", file=sys.stderr)
        return 3

exec
/bin/bash -lc "rg -n \"RT-γ-6|R-S1|부분 답습|Layer 1\\+2\\+4|subsection|통합\" docs/phase0/mvp2-gamma-decision-brief.md docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md docs/phase0/mvp2-gamma-layer-separation-brief.md docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md docs/external-review/2026-05-28-mvp2-gamma-codex-response.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:3:> **본 합의** = Reviewer 통합 합의 보고서. Agent A (구현 분석가) + Agent B (품질/안전성 검증가) + Agent C (대안 탐색가) 3 병렬 독립 분석 + 외부 LLM 1+ (codex, OpenAI gpt-5.5) cross-vendor 응답 통합. CLAUDE.md §3 3+1 멀티 에이전트 합의 프로토콜 답습.
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:13:**Reviewer 통합 판정**: ⚠️ **APPROVE WITH CONDITIONS (BLOCKING 8 + 권고 16)** — brief v1.1 보강 후 본 cycle 합의 발효 자격 충실. 4 source consensus 강력 ((γ-c) 1순위 + (γ-a) 2순위 + (γ-d) 비권고).
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:23:| **Reviewer 통합** | Anthropic Claude (Opus 4.7) | **APPROVE WITH CONDITIONS** | **8** (Consensus 1 + Unique 7) | **16** (중복 제거) |
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:25:**원칙 준수**: 실 코드 0 / CI 0 / hook 0 / branch protection 0 / config 본문 0 / ADR 본문 0 / 헌법 0 / roadmap 본문 0 / governance 본문 0 / G4 본문 0 / ADR-012 본문 0 / MVP-1 PASS 재선언 0 / MVP-2 Implementation Evidence PASS 발효 0 / Operational Readiness PASS 0 / Hermes PMO 격상 0 / GP-2 sub-수단 결정 0 (R-1~R-5 후보 식별만) / G4 §4.4 Layer 4 sub-수단 결정 0 (L-1~L-5 후보 식별만) / W 통합 결정 0 / threshold 고정 0 / Tier-2/3 catalog 확장 0 / 외부 library 도입 결정 0 / Layer 3+5 영역 진입 결정 0 / 다른 GP 진입 결정 0 / facade.py placeholder 0 변경 / Hermes upstream import 결정 0 / ADR-012 §2.3 본문 정정 자동 진입 0 / 자동 후속 sub-cycle 진입 0 — **27/27 유지**.
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:42:### §1.2 Unique BLOCKING 영역 (단일 source 발견, Reviewer 통합 격상 자격)
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:49:- **U-3 (Agent A R-A-1)**: brief §2.1.3 (γ-a) "N회" 정량 부재 — (γ-a) = 4 cycle (Layer 1 + Layer 2 + canonical corpus + Layer 4) vs (γ-c) = 3 cycle (Layer 1+2 + canonical + Layer 4 통합) **대비표 추가 의무**
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:53:- **U-5 (Agent B R-B-1)**: (γ-c) "defense-in-depth 답습 충실" framing 부정확 — G4 §4.4.1 = 5-layer (Layer 1~5)이나 본 (γ) = Layer 1+2+4 한정 (Layer 3 Signed commit + Layer 5 External anchor 누락) → **"부분 답습" 표현으로 정정 의무**
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:67:| 대안 | codex 권고 | Agent A 권고 | Agent B 명시 | Agent C 명시 | Reviewer 통합 |
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:69:| (γ-c) Layer 1+2+4 동시 | **1순위** | **1순위** | (부분 답습 정정 후 권고) | (R-C-3 framing fragile 경고) | **1순위 (3/4 source consensus, 단 U-5 framing 정정 답습)** |
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:76:## §2 BLOCKING 8건 통합 매트릭스
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:81:| **B-2** | U-1 (codex 조건부 승인 조건 R-1) | brief §2.6 표 권고 순위 통일 의무 | codex Unique | brief §2.6 표 "본 brief 권고 (1)" vs 비고 "(γ-c) 1순위" 내부 충돌 정정 → "본 brief 권고 (Reviewer 통합)" 분리 | v1.1 §2.6 표 정정 |
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:85:| **B-6** | U-5 (Agent B 안전성) | (γ-c) "defense-in-depth 답습 충실" → "부분 답습" (Layer 3+5 누락) 정정 | Agent B Unique | brief §2.3.2 + §2.6 권고 매트릭스 framing 정정 | v1.1 §2.3.2 + §2.6 |
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:91:## §3 권고 16건 통합 매트릭스 (중복 제거)
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:95:| N-1 | (γ-c) layer별 evidence subsection 강제 (PASS evidence template) | codex N-3 + Agent A N-A-1 | §2.3 + §5 |
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:97:| N-3 | RT-γ-6 R-S1 정정 PASS 시점 선행/동시 정정 의무 평가 추가 | codex N-5 + Agent B R-B-2 + Agent C N-C-4 | §5.1 RT-γ-6 |
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:106:| N-12 | §1.3 R-S1 후행 영향 row 추가 | Agent B N-B-5 | §1.3 |
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:108:| N-14 | (γ-c) 1순위 권고 자격 검증 보강 (U-5 부분 답습 답습 정합 후) | Agent C N-C-1 | §2.6 |
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:142:3. Layer 1+2+4를 동시 PASS evidence로 묶음 → 사실상 **(γ-c)**
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:168:| B-2 (§2.6 표 순위 통일) | §2.6 | "본 brief 권고 (1)" → "Reviewer 통합 권고 (1순위)" 표기 통일 + (γ-c) 1순위 + (γ-a) 2순위 + (γ-b) 3순위 + (γ-d) 비권고 |
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:170:| B-4 ((γ-a) "N회" 정량) | §2.1.3 + §2.3.1 + §2.4.1 | (γ-a) = 4 cycle (Layer 1 + Layer 2 + canonical corpus + Layer 4) / (γ-b) = 1 cycle (통합) / (γ-c) = 3 cycle (Layer 1+2 + canonical + Layer 4 통합 evidence 분리) / (γ-d) = 2 cycle (Layer 4 + Layer 1+2 별도, 비권고) |
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:172:| B-6 ((γ-c) "부분 답습" 정정) | §2.3.2 + §2.6 | "defense-in-depth 답습 충실" → "defense-in-depth 부분 답습 (Layer 1+2+4 한정, Layer 3 Signed commit + Layer 5 External anchor = 본 cycle scope 외)" |
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:180:| N-1 ((γ-c) layer subsection 강제) | §2.3.3 + §5.2 신규 | (γ-c) 채택 시 PASS evidence template = Layer 1/Layer 2/Layer 4 subsection 강제 명문 |
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:182:| N-3 (RT-γ-6 R-S1 PASS 시점 선행/동시 정정) | §5.1 RT-γ-6 | "본 (γ) cycle 자동 진입 대상 아님 / MVP-2 Implementation Evidence PASS 발효 시점 선행/동시 정정 필요성 재평가" |
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:189:| N-10 ("수단 결정 0" 강화) | §2.6 | "권고 매트릭스 = Reviewer 통합 후보 비교 한정, 수단 *결정* = 풀 3+1 + 사용자 명시 영역" 강조 |
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:191:| N-12 (R-S1 후행 영향 row) | §1.3 항목 4 | R-S1 후행 영향 row 추가 (RT-γ-6 답습) |
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:193:| N-14 ((γ-c) 1순위 검증 보강) | §2.6 | (B-6 부분 답습 답습 정합 후) (γ-c) 1순위 권고 자격 |
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:211:1. **(γ) 4 대안 평가 권고 발효** (Reviewer 통합 권고: (γ-c) 1순위 + (γ-a) 2순위)
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:213:3. **후속 sub-cycle 진입 자격 발효** ((γ-c) 채택 시 = Layer 1+2+4 통합 PASS 격상 cycle 진입 자격 / (γ-a) 채택 시 = Layer 1+2 우선 + Layer 4 후속 cycle 진입 자격)
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:221:- ❌ (γ) 4 대안 中 채택 *결정* (Reviewer 통합 권고 ≠ 결정, 결정 = 풀 3+1 합의 발효 + 사용자 명시 영역)
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:224:- ❌ R-S1 cross-reference 정정 자동 진입
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:237:   - **(γ) 4 대안 中 채택 결정** — Reviewer 통합 권고 ((γ-c) 1순위 + (γ-a) 2순위) 답습 + 사용자 명시 결정 (별도 cycle)
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:239:   - **Layer 1+2 PASS 격상 cycle** ((γ-a) 채택 시) 또는 **Layer 1+2+4 통합 PASS 격상 cycle** ((γ-c) 채택 시)
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:242:   - **R-S1 cross-reference 정정 cycle**
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:248:## §8 메타 편향 자기진단 (Reviewer 통합)
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:252:| M-1 | Reviewer + 3 Agent = 모두 Anthropic Claude vendor → cross-vendor blind 의문 | codex (OpenAI gpt-5.5) 1+ 응답 통합 + cross-vendor 형식 충족 (N-4 + N-13 흡수) |
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:255:| M-4 | (γ-d) 모순 5 source verify = 52 entry R-S1 답습 동형 → "절차적 답습" 위험 | §4 verbatim 직접 read evidence (5 source 모두 verbatim + filesystem evidence + ADR-012 / G4 / 자체 함수 분석 다층 답습) |
docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md:257:| M-6 | (γ-c) 1순위 권고 자격 = Reviewer 통합 권고 → 결정 영역 침입 risk | §0 + §6.2 = "권고 ≠ 결정" 영구 분리. 결정 = 풀 3+1 합의 발효 + 사용자 명시 영역 답습 |
docs/phase0/mvp2-gamma-layer-separation-brief.md:5:> **v1 → v1.1 갱신**: 풀 3+1 + 외부 LLM 1+ (codex gpt-5.5 cross-vendor) 통합 합의 (`docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md`) BLOCKING 8 + 권고 16 1pass 흡수 (별도 v2 cycle 0, ceremony-inflation 차단). §11 v1.1 보강 매트릭스 추가.
docs/phase0/mvp2-gamma-layer-separation-brief.md:47:| 8 | W 통합 결정 (W-A~E) | 0건 ((β) 별도) |
docs/phase0/mvp2-gamma-layer-separation-brief.md:57:| 18 | G4 §4.4 Layer 3 (Signed commit) / Layer 5 (External anchor) 영역 진입 결정 | 0건 (본 cycle = Layer 1+2+4 한정) |
docs/phase0/mvp2-gamma-layer-separation-brief.md:59:| 20 | R-S1 cross-reference 정정 자동 진입 (ADR-012 §2.3 vs §2.8) | 0건 (별도 cycle) |
docs/phase0/mvp2-gamma-layer-separation-brief.md:64:| 25 | 자동 후속 sub-cycle 진입 ((β) / Layer 1+2 PASS 격상 / 통합 / 실 구현) | 0건 |
docs/phase0/mvp2-gamma-layer-separation-brief.md:72:- ❌ 본 brief 자체에서 (γ) 4 대안 中 *채택 결정* 0건 (Reviewer 통합 권고 ≠ 결정)
docs/phase0/mvp2-gamma-layer-separation-brief.md:92:| ADR-012 §2.3 line 165~185 (PRINCIPLE ONLY, 4-layer) | Append-only + Hash Chain 원칙 (numbering 근거 아님, R-S1 답습) |
docs/phase0/mvp2-gamma-layer-separation-brief.md:94:| ⭐ 본 cycle Reviewer 통합 합의 (`3plus1-consensus-2026-05-28-mvp2-gamma.md`, 264줄, BLOCKING 8 + 권고 16) | 본 v1.1 = 1pass 흡수 답습 |
docs/phase0/mvp2-gamma-layer-separation-brief.md:102:| **(γ-c)** | Layer 1+2+4 동시 진입 (defense-in-depth) |
docs/phase0/mvp2-gamma-layer-separation-brief.md:109:| 1 | Layer 1+2 의존 영역 framing | "(γ-d) 현 framing" | **4 대안 평가 + Reviewer 통합 권고 ((γ-c) 1순위 + (γ-a) 2순위 + (γ-d) 비권고)** | ✅ 정당 (52 entry §8.1 답습 + 4 source consensus) |
docs/phase0/mvp2-gamma-layer-separation-brief.md:112:| 4 ⭐ (N-12 흡수) | R-S1 후행 영향 (RT-γ-6) | 별도 cycle 영역 | **본 (γ) cycle = RT-γ-6 평가 + MVP-2 PASS 발효 시점 선행/동시 정정 의무 평가 (N-3 답습)** | ✅ 정당 (52 entry §9.5 답습) |
docs/phase0/mvp2-gamma-layer-separation-brief.md:129:- ✅ R-S1 후행 영향 흡수 용이
docs/phase0/mvp2-gamma-layer-separation-brief.md:155:### §2.3 (γ-c) Layer 1+2+4 동시 진입
docs/phase0/mvp2-gamma-layer-separation-brief.md:159:Layer 1+2+4 동시 합의 cycle 진입. **합의 cycle 수 = 3 cycle 등가** (Layer 1+2 통합 + canonical corpus + Layer 4 통합 evidence 분리). 실 구현 = `g4-hash-chain.yml` 7 step 답습 시 step prefix `[Layer N]` 권고 (N-5 흡수).
docs/phase0/mvp2-gamma-layer-separation-brief.md:163:- ✅ **defense-in-depth *부분 답습*** (Layer 1+2+4 한정, Layer 3 Signed commit + Layer 5 External anchor = 본 cycle scope 외) — (γ-c) "충실 답습" framing 정정 답습 (B-6)
docs/phase0/mvp2-gamma-layer-separation-brief.md:170:- ⚠️ 합의 부담 ↑ (Layer 1+2+4 통합 + 각 layer evidence 분리)
docs/phase0/mvp2-gamma-layer-separation-brief.md:172:- 📌 N-1 답습: (γ-c) 채택 시 PASS evidence template = Layer 1/Layer 2/Layer 4 subsection 강제 명문 의무
docs/phase0/mvp2-gamma-layer-separation-brief.md:205:3. Layer 1+2+4 동시 PASS evidence → 사실상 (γ-c)
docs/phase0/mvp2-gamma-layer-separation-brief.md:213:| Layer 1 (hash chain) | ✅ `tools/jsonl_hash_chain.py` (14038B, genesis hash + 4 violation_type) | PASS 격상 = R-6 workflow 답습 통합 + actual run PASS | **PREV_HASH_MISMATCH + HASH_RECALCULATION + GENESIS_MISMATCH** |
docs/phase0/mvp2-gamma-layer-separation-brief.md:218:| Layer 4 (CI 회귀 검증) | ✅ `.github/workflows/g4-hash-chain.yml` (10652B) PoC 시제 운영, 7 step 분리 (N-A-3 답습) | PASS 격상 = R-6 답습 통합 또는 단독 PASS 격상 + actual run PASS | (회귀 검증 영역) |
docs/phase0/mvp2-gamma-layer-separation-brief.md:222:### §2.6 (γ) 4 대안 권고 매트릭스 (Reviewer 통합, B-2 + B-6 + N-10 + N-14 흡수)
docs/phase0/mvp2-gamma-layer-separation-brief.md:224:**핵심 답습**: 본 §2.6 = **Reviewer 통합 권고 (수단 *결정* = 풀 3+1 합의 발효 + 사용자 명시 영역, N-10 답습)**.
docs/phase0/mvp2-gamma-layer-separation-brief.md:226:| 대안 | 의존 chain | 합의 cycle 수 | ceremony-inflation 억제 | defense-in-depth | PoC 시제 | PASS 발효 정합성 | **Reviewer 통합 순위** |
docs/phase0/mvp2-gamma-layer-separation-brief.md:228:| (γ-c) Layer 1+2+4 동시 | 높음 | 3 (등가) | 높음 | **부분 답습** (Layer 1+2+4) | 높음 | 높음 | **1순위** (4 source consensus, B-6 framing 정정 답습) |
docs/phase0/mvp2-gamma-layer-separation-brief.md:241:| **(γ-g)** | 시점 vs evidence 분리 — 본 (γ) cycle = 시점 분리 결정 + MVP-2 PASS = evidence 통합 | (γ-a)+(γ-c) hybrid, MVP-2 PASS 발효 시점 evidence 통합 정합 |
docs/phase0/mvp2-gamma-layer-separation-brief.md:251:| (a) | 동등 이상 보안 결과 | Layer 1+2+4 동시 PASS evidence (분리 명시) | Layer 1+2 PASS + Layer 4 PASS (단계적) | Layer 4 PASS (Layer 1+2 자동 통합) | Layer 4 PASS (Layer 1+2 미발효 시 모순) |
docs/phase0/mvp2-gamma-layer-separation-brief.md:254:| (d) | 자동 회귀 검증 경로 확보 | R-6 답습 (각 layer step 분리) | R-6 답습 (단계적) | R-6 답습 (1 cycle 통합) | R-6 답습 (Layer 4 한정, 회귀 대상 부재 모순) |
docs/phase0/mvp2-gamma-layer-separation-brief.md:274:1. **(γ) 4 대안 평가 권고 발효** (Reviewer 통합 권고: (γ-c) 1순위 + (γ-a) 2순위)
docs/phase0/mvp2-gamma-layer-separation-brief.md:287:| 4 | 권위 chain 다중 source 손상 위험 | ⚠️ **부분 발화** (R-S1 후행 영향 RT-γ-6, 52 entry 발견 cascade) | 본 cycle = 후행 영향 평가 한정 |
docs/phase0/mvp2-gamma-layer-separation-brief.md:288:| 5 ⭐ (N-8 framing 정밀화) | 외부 LLM 응답 통합 필요성 | ✅ **사용자 영역 결정 발화** (52 entry §8.1 답습 + cross-vendor 권고) | 본 cycle = 사용자 명시 (α) Claude tmux+codex 직접 호출 답습 발효 |
docs/phase0/mvp2-gamma-layer-separation-brief.md:311:3. Layer 1+2+4 동시 PASS evidence → 사실상 **(γ-c)**
docs/phase0/mvp2-gamma-layer-separation-brief.md:332:| RT-γ-6 ⭐ (N-3 흡수) | R-S1 cross-reference 정정 후행 영향 + **MVP-2 PASS 시점 선행/동시 정정 필요성 재평가** | 모든 (γ) | ADR-012 §2.3 본문 정정 시 (γ) 결정 영향 + MVP-2 Implementation Evidence PASS 발효 시점 R-S1 정정 사전조건 평가 | 본 cycle 후 + MVP-2 PASS 발효 cycle 시점 | 52 entry §9.5 + codex N-5 답습 |
docs/phase0/mvp2-gamma-layer-separation-brief.md:336:(γ-c) 채택 시 PASS evidence template = **Layer 1/Layer 2/Layer 4 subsection 강제** (N-1 흡수).
docs/phase0/mvp2-gamma-layer-separation-brief.md:340:| E-γ-1 | (γ) 4 대안 평가 권고 합의 보고서 | 본 cycle Reviewer 통합 합의 |
docs/phase0/mvp2-gamma-layer-separation-brief.md:365:| 9 | R-S1 cross-reference 정정 자동 진입 | 별도 cycle (RT-γ-6 답습) |
docs/phase0/mvp2-gamma-layer-separation-brief.md:395:| 52 entry Reviewer 통합 합의 | `docs/review/3plus1-consensus-2026-05-28-mvp2-entry.md` |
docs/phase0/mvp2-gamma-layer-separation-brief.md:398:| `ADR-012 §2.3 + §2.8` (R-S1) | 답습 source |
docs/phase0/mvp2-gamma-layer-separation-brief.md:407:1. **(γ) 4 대안 中 채택 결정** — Reviewer 통합 권고 ((γ-c) 1순위 + (γ-a) 2순위) 답습 + 사용자 명시 결정 (별도 cycle)
docs/phase0/mvp2-gamma-layer-separation-brief.md:409:3. **Layer 1+2 PASS 격상 sub-cycle** ((γ-a) 채택 시) 또는 **Layer 1+2+4 통합 PASS 격상 cycle** ((γ-c) 채택 시)
docs/phase0/mvp2-gamma-layer-separation-brief.md:410:4. **실 구현 sub-cycle** — Hermes upstream + 본 repo P1 facade + Layer 1+2+4 PoC → PASS + R-6 workflow 확장
docs/phase0/mvp2-gamma-layer-separation-brief.md:411:5. **MVP-2 Implementation Evidence PASS 발효 합의** — (a)~(d) 4조건 evidence + (e) 후속 운영조건 + 사용자 명시 (32 entry 답습 + RT-γ-6 R-S1 정정 사전조건 평가)
docs/phase0/mvp2-gamma-layer-separation-brief.md:412:6. **R-S1 cross-reference 정정 cycle** — ADR-012 §2.3 본문 정정 또는 §2.8 동형 답습 cross-reference 강화
docs/phase0/mvp2-gamma-layer-separation-brief.md:429:- 본 cycle Reviewer 통합 합의 — `docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md` (264줄, BLOCKING 8 + 권고 16)
docs/phase0/mvp2-gamma-layer-separation-brief.md:432:- 52 entry Reviewer 통합 합의 — `docs/review/3plus1-consensus-2026-05-28-mvp2-entry.md`
docs/phase0/mvp2-gamma-layer-separation-brief.md:452:- (γ-c) 채택 시 = Layer 1+2+4 통합 evidence cross-reference (Layer 4 evidence 內 분리 명시, N-1 답습)
docs/phase0/mvp2-gamma-layer-separation-brief.md:455:- R-S1 cross-reference 정정 (52 entry §9.5 답습)
docs/phase0/mvp2-gamma-layer-separation-brief.md:456:- ⭐ **roadmap.md §5.3 그룹 C+D 분리 progression 답습 명문 보강** (N-16 흡수) — 본 (γ) cycle = 그룹 C 內 Layer 분리 영역 결정 한정, 그룹 D (GP-2) 와의 통합 가능성 = W-D 답습
docs/phase0/mvp2-gamma-layer-separation-brief.md:464:| P-1 | 본 brief 가 (γ) 특정 대안 (γ-c) 권고 방향으로 편향 | §0.3 + §6.2 27+10 금지 + §2.6 권고 매트릭스 = Reviewer 통합 권고 한정 (수단 결정 ≠ 본 cycle, §0.4 답습) |
docs/phase0/mvp2-gamma-layer-separation-brief.md:467:| P-4 | R-S1 cross-reference 정정 후행 영향 (RT-γ-6) 본 cycle 결정 영향 | §5.1 RT-γ-6 명시 + §9.4 = 별도 cycle 영역 답습 |
docs/phase0/mvp2-gamma-layer-separation-brief.md:470:| P-7 ⭐ (N-4 + N-13 흡수) | **본 brief 작성자 = 52 entry brief 작성자 (Claude Opus 4.7) → 답습 cascade risk + cross-vendor blind 의문** | §1.3 선차 변경 매트릭스 명시 + §4.4 모순 risk 발견 (52 entry framing 답습 한정) + Reviewer 통합 합의 시 cross-check 영역 (Agent A/B/C 3 병렬 독립 + **외부 LLM codex (OpenAI gpt-5.5) cross-vendor 검증** = 4 source vendor 분포: Claude 3 + OpenAI 1 = cross-vendor 형식 충족, 헌법 5조-2 답습) |
docs/phase0/mvp2-gamma-layer-separation-brief.md:483:| B-2 (§2.6 표 순위 통일) | §2.6 | "본 brief 권고" → "Reviewer 통합 순위" 표기 통일 + (γ-c) 1순위 + (γ-a) 2순위 + (γ-b) 3순위 + (γ-d) 비권고 |
docs/phase0/mvp2-gamma-layer-separation-brief.md:487:| B-6 ((γ-c) "부분 답습" 정정) | §2.3.2 + §2.6 | "defense-in-depth 답습 충실" → "defense-in-depth *부분 답습* (Layer 1+2+4 한정, Layer 3+5 = 본 cycle scope 외)" |
docs/phase0/mvp2-gamma-layer-separation-brief.md:495:| N-1 ((γ-c) layer subsection 강제) | §2.3.3 + §5.2 | (γ-c) PASS evidence template Layer 1/2/4 subsection 강제 |
docs/phase0/mvp2-gamma-layer-separation-brief.md:497:| N-3 (RT-γ-6 R-S1 PASS 시점 선행/동시 정정) | §5.1 RT-γ-6 | "본 (γ) cycle 자동 진입 대상 아님 / MVP-2 PASS 발효 시점 선행/동시 정정 필요성 재평가" |
docs/phase0/mvp2-gamma-layer-separation-brief.md:504:| N-10 ("수단 결정 0" 강화) | §2.6 | "Reviewer 통합 권고 한정, 수단 *결정* = 풀 3+1 + 사용자 명시 영역" 강조 |
docs/phase0/mvp2-gamma-layer-separation-brief.md:506:| N-12 (R-S1 후행 영향 row) | §1.3 항목 4 | R-S1 후행 영향 row 추가 |
docs/phase0/mvp2-gamma-layer-separation-brief.md:508:| N-14 ((γ-c) 1순위 검증 보강) | §2.6 | B-6 부분 답습 정합 후 (γ-c) 1순위 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:23:본 cycle 발효 *하지 않는 것*: 실 코드 0 / G4 §4.4 Layer sub-수단 결정 (L-1~L-5) 0 / GP-2 sub-수단 결정 (R-1~R-5) 0 / W 통합 결정 (W-A~E) 0 / MVP-2 Implementation Evidence PASS 발효 0 (총 27 금지 사항).
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:29:- **(γ-c)** Layer 1+2+4 동시 진입 (defense-in-depth)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:46:- `docs/decisions/ADR-012-evidence-ledger-protection.md` (§2.3 + §2.8 — Layer numbering R-S1 답습)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:77:7. ⚠️ **R-S1 (ADR-012 §2.3 vs §2.8) 후행 영향 (RT-γ-6) 평가** — 52 entry §9.5 답습 (별도 cycle 영역, 본 cycle 후행 영향 답습)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:121:| Layer 1 (hash chain) | ✅ `tools/jsonl_hash_chain.py` (genesis hash 함수 + 4 violation_type) | PASS 격상 = R-6 workflow 답습 통합 + actual run PASS evidence |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:125:| Layer 4 (CI 회귀 검증) | ✅ `.github/workflows/g4-hash-chain.yml` (10652B) PoC 시제 운영 | PASS 격상 = R-6 답습 통합 또는 단독 PASS 격상 + actual run PASS |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:134:| (γ-b) Layer 4 단독 (Layer 1+2 자동) | ✅ 답습 (자동) | 1 cycle | ✅ 차단 | 동시 | ⚠️ 통합 risk | 권고 (3) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:135:| (γ-c) Layer 1+2+4 동시 (defense-in-depth) | ✅ 답습 충실 | 1 cycle (큰 영역) | ✅ 차단 | 동시 | ✅ 명시 분리 | ✅ **권고 (2)** — defense-in-depth + 효율 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:138:→ **본 brief 권고 (수단 *결정* 0, 후보 비교만)**: **(γ-c) Layer 1+2+4 동시 (defense-in-depth)** 1순위 + **(γ-a) Layer 1+2 우선 → Layer 4 후속** 2순위. 본 결정 = 풀 3+1 합의 + 사용자 명시 영역.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:148:| (a) | 동등 이상 보안 결과 | Layer 1+2 PASS 발효 + Layer 4 PASS 발효 (단계적 evidence) | Layer 4 PASS 발효 (Layer 1+2 자동 의존 통합 evidence) | Layer 1+2+4 동시 PASS evidence (분리 명시) | Layer 4 PASS 발효 (Layer 1+2 미발효 시 모순) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:151:| (d) | 자동 회귀 검증 경로 확보 | R-6 workflow 답습 확장 (단계적) | R-6 답습 (1 cycle 통합) | R-6 답습 (각 layer step 분리) | R-6 답습 (Layer 4 한정, Layer 1+2 부재 시 회귀 *대상* 부재 모순) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:183:   - (γ-b) 채택 시 = Layer 1+2+4 통합 PASS 격상 cycle (1 cycle, Layer 4 evidence 內 합산)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:184:   - (γ-c) 채택 시 = Layer 1+2+4 통합 PASS 격상 cycle (1 cycle, 각 layer evidence 분리)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:195:| 4 | 권위 chain 다중 source 손상 위험 | ❌ 미발화 | R-S1 (ADR-012 §2.3 vs §2.8) = 52 entry 발견 + 별도 cross-reference 정정 cycle 답습 (본 cycle scope 외) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:196:| 5 | 외부 LLM 응답 통합 필요성 | ⚠️ **부분 발화 (사용자 영역 결정)** | (γ) 결정 = 큰 영역, cross-vendor 외부 LLM 권고. 단, 작은 영역 결정 시 외부 LLM 0 가능 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:213:| RT-γ-4 | (γ-c) 채택 시 합의 부담 ↑ → 합의 cycle 지연 | (γ-c) | 큰 합의 영역 (Layer 1+2+4 통합 + 각 layer evidence 분리) | (γ-c) 단점 답습 (§2.3.3) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:215:| RT-γ-6 | R-S1 cross-reference 정정 후행 영향 | 모든 (γ) | ADR-012 §2.3 본문 정정 시 (γ) 결정 영향 (예: Layer 4 numbering 변경 시 본 cycle 결정 영역 변경) | 52 entry §9.5 답습 (R-S1 정정 cycle 별도, 본 cycle 후행 영향 답습) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:223:| E-γ-1 | (γ) 4 대안 中 채택 결정 합의 보고서 | 본 cycle Reviewer 통합 합의 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:247:| 1 | 자동 후속 sub-cycle 진입 (Layer 1+2 PASS 격상 / Layer 4 PASS 격상 / 통합) | 사용자 명시 의무 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:256:| 10 | R-S1 cross-reference 정정 자동 진입 | 별도 cycle 사용자 명시 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:282:| 52 entry Reviewer 통합 합의 | `docs/review/3plus1-consensus-2026-05-28-mvp2-entry.md` |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:285:| `ADR-012 §2.3 + §2.8` (Layer numbering R-S1) | 답습 source |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:298:3. **Layer 1+2+4 통합 PASS 격상 cycle** ((γ-b) 또는 (γ-c) 채택 시) — 큰 합의
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:299:4. **실 구현 sub-cycle** — Hermes upstream + 본 repo P1 facade + Layer 1+2+4 PoC → PASS + R-6 workflow 확장
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:301:6. **R-S1 cross-reference 정정 cycle** — ADR-012 §2.3 본문 정정 또는 §2.8 동형 답습 cross-reference 강화 — 풀 3+1 + 사용자 명시
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:321:- **52 entry Reviewer 통합 합의 보고서** — `docs/review/3plus1-consensus-2026-05-28-mvp2-entry.md`
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:344:- (γ-b) 채택 시 = Layer 1+2+4 통합 evidence cross-reference (Layer 4 evidence 內 분리 명시)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:346:- R-S1 cross-reference 정정 영역 (52 entry §9.5 답습, 본 cycle scope 외)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:359:| P-4 | R-S1 cross-reference 정정 후행 영향 (RT-γ-6) 가 본 cycle 결정 영향 | §5.1 RT-γ-6 명시 + §9.4 = 별도 cycle 영역 답습, 본 cycle = 4 대안 결정 한정 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:362:| P-7 | 본 brief 작성자 = 52 entry brief 작성자 (Claude Opus 4.7) → 답습 cascade risk | §1.3 선차 변경 매트릭스 명시 + §2.4 (γ-d) 모순 risk 발견 (52 entry framing 답습 한정) + Reviewer 통합 합의 시 cross-check 영역 (Agent A/B/C 3 병렬 독립 + 외부 LLM 검증) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:415:| 1 | 실 코드 / runtime code 구현 | 0건 (Layer 1+2+4 PASS 격상 본문 모두 0건) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:423:| 9 | **W 통합 결정** (W-A / W-B / W-C / W-D / W-E 中 채택) | 0건 ((β) 별도 cycle) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:437:| 23 | G4 §4.4 Layer 3 (Signed commit) / Layer 5 (External anchor) 영역 진입 결정 | 0건 (본 cycle = Layer 1+2+4 한정, Layer 3+5 = 별도 cycle 영역) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:439:| 25 | R-S1 cross-reference 정정 자동 진입 (ADR-012 §2.3 vs §2.8) | 0건 (별도 cross-reference 정정 cycle 사용자 명시 영역, 52 entry B-1 답습) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:461:| `mvp2-entry-brief.md` v1.1 (52 entry, `c739c53` 발효) + Reviewer 통합 합의 (BLOCKING 7 + 권고 13 흡수) | 본 (γ) brief 의 **직접 입력 자료**. 본 cycle = 52 entry §2.2.4 + §8.1 항목 2 답습 (γ) 결정 cycle |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:462:| 52 entry brief §2.2.4 — (γ) 4 대안 매트릭스 (N-12 흡수) | (γ-a) Layer 1+2 의존 영역 우선 → Layer 4 후속 / (γ-b) Layer 4 단독 (Layer 1+2 자동 동시) / (γ-c) Layer 1+2+4 동시 (defense-in-depth) / (γ-d) Layer 4 단독 + Layer 1+2 별도 cycle 분리 (현 framing) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:464:| `provider-agnostic-memory-skill-design.md §4.4.1 line 629~660` (G4 직접 정의 5-layer) — 52 entry §4.4.2 R-S1 답습 PRIMARY 권위 | Layer 1 (Hash Chain MANDATORY) + Layer 2 (Git append-only MANDATORY) + Layer 3 (Signed commit RECOMMENDED MVP) + Layer 4 (CI 회귀 검증 MANDATORY) + Layer 5 (External Anchor RECOMMENDED MVP) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:476:| **(γ-c)** | **Layer 1+2+4 동시 진입** | "defense-in-depth 답습" |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:526:| **PASS 발효 시점** | Layer 1+2+4 동시 발효 (단일 합의) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:537:- ⚠️ 합의 부담 ↑ (Layer 1+2+4 통합 합의 = 큰 영역, 풀 3+1 + 외부 LLM 1+ + 사용자 명시)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:542:PoC 시제 답습 자동 (Layer 1+2 PoC 시제 + Layer 4 PoC 시제 = 모두 충족). PASS 격상 영역 = Layer 1+2+4 통합.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:544:### §2.3 (γ-c) Layer 1+2+4 동시 진입 (defense-in-depth)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:550:| **순서** | Layer 1+2+4 동시 합의 cycle 진입 — defense-in-depth 답습 (각 layer 명시 진입 자격) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:551:| **합의 cycle 수** | 1 cycle (Layer 1+2+4 통합) — (γ-b) 와 형식 유사하지만 각 layer evidence 분리 명시 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:552:| **PASS 발효 시점** | Layer 1+2+4 동시 발효 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:558:- ✅ 통합 합의 효율 + Layer evidence 분리 동시 충족
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:563:- ⚠️ 합의 부담 ↑ (Layer 1+2+4 통합 + 각 layer evidence 분리 = 큰 영역)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:568:(γ-b) 동형 — PoC 시제 충족 자동, PASS 격상 = Layer 1+2+4 통합 동시.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:916:/bin/bash -lc "rg -n \"2\\.2\\.4|γ-a|γ-b|γ-c|γ-d|N-A-1|B-6|§8\\.1|R-S1|9\\.5\" docs/phase0/mvp2-entry-brief.md" in /home/delangi/문서/project/category/AI_development_tool
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:919:72:| 27 | **R-S1 cross-reference 정정 cycle 자동 진입** | 0건 (별도 사용자 명시 영역, §4.4 답습) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:920:109:| **G4 §4.4 Layer 4 — CI 회귀 검증** | G4 | Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증 + canonical JSON 위반 검출 + timestamp monotonicity 검증 + R-6 workflow 답습 확장. **MANDATORY 등급 5-layer 체계 內 Layer 4** (G4 §4.4.1 + ADR-012 §2.8 동형, B-1 답습 §4.4 권위 인용 정정 답습) | **PRIMARY**: `provider-agnostic-memory-skill-design.md §4.4.1 line 629~660` (G4 직접 정의) + **SUPPORTING**: `ADR-012 §2.8 line 264~272` (5-layer 동형) + **PRINCIPLE ONLY**: `ADR-012 §2.3 line 165~185` (Append-only + Hash Chain 원칙, **numbering 근거 아님** — §4.4 R-S1 답습) + `ADR-012 §3.4` (timestamp monotonicity) + `ADR-012 §2.7` (prev_hash 실패) + `ADR-012 §2.5` (RFC 8785 JCS) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:921:118:| 2 | **G4 §4.4 Layer 4 진입 자격** | provider-agnostic-memory-skill-design §4.4 (5-layer) + ADR-012 §2.3 (4-layer) + §2.8 (5-layer) | **Layer 4 = CI 회귀 검증 (MANDATORY), MVP-2 진입 영역 채택** | **R-S1 CONFIRMED divergence — 권위 인용 chain 정정 답습 (§4.4)** (B-1 흡수) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:922:123:→ **요약**: 본 (α) cycle = "MVP-2 영역 *진입* 합의" 한정 (수단 결정 = (β) 분리). 두 영역 모두 풀 3+1 + 외부 LLM 1+ + 사용자 명시 일관. R-S1 = **CONFIRMED divergence** (§4.4 답습 5 source verify).
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:923:175:| **권위 출처** ⭐ (B-1 R-S1 정정 답습) | **PRIMARY**: `provider-agnostic-memory-skill-design.md §4.4.1 line 629~660` (G4 직접 정의 5-layer) + **SUPPORTING**: `ADR-012 §2.8 line 264~272` (5-layer 동형) + **PRINCIPLE ONLY (numbering 근거 아님)**: `ADR-012 §2.3 line 165~185` (Append-only + Hash Chain 원칙) + `ADR-012 §3.4` (timestamp monotonicity) + `ADR-012 §2.7` (prev_hash 실패) + `ADR-012 §2.5` (RFC 8785 JCS) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:925:182:| ADR-012 §2.3 + §2.8 Layer 1~5 권위 정의 발효 (R-S1 정정 답습) | ✅ 충족 | (그대로) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:933:207:- **(γ-c) Layer 1+2+4 동시 진입** (defense-in-depth 답습)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:938:295:| 4 | 권위 chain 다중 source 손상 위험 | ✅ **발화 (R-S1 CONFIRMED 격상)** ⭐ (B-1 + N-7 흡수) | §1.3 항목 2 + §2.2.1 + §4.4 = ADR-012 §2.3 (4-layer) vs §2.8/G4 §4.4.1 (5-layer) **CONFIRMED divergence** (5 source verify: codex + Agent A + Agent B + Agent C + Reviewer). 본 brief v1.1 = 권위 인용 chain 정정 답습 (G4 §4.4.1 + ADR-012 §2.8 PRIMARY, §2.3 = numbering 근거 아님). 다중 source 정정 = §4.4 + §9.5 별도 cycle 영역 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:939:302:### §4.4 ⭐ R-S1 CONFIRMED divergence — Reviewer 단독 verbatim verify 답습 (B-1 흡수)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:941:409:| 9 | ADR 본문 갱신 자동 cross-reference 변경 | 별도 commit 영역 (R-S1 정정 영역 포함) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:942:412:| 12 ⭐ (B-1 답습) | ADR-012 §2.3 본문 정정 자동 진입 (R-S1 다중 source 정정) | 별도 cross-reference 정정 cycle 사용자 명시 영역 (§9.5 답습) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:943:457:| 7 | ⭐ **R-S1 CONFIRMED divergence 검증** (B-1 답습) | 본 brief §4.4 권위 인용 chain 정정 답습 + ADR-012 §2.3 vs §2.8 verbatim 직접 read |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:946:473:5. **R-S1 cross-reference 정정 cycle** — ADR-012 §2.3 본문 정정 또는 §2.8 동형 답습 cross-reference 강화 — 별도 풀 3+1 + 사용자 명시 (§9.5 답습)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:952:529:- **R-S1 정정 영역 (별도 cross-reference 정정 cycle 사용자 명시 영역)** ⭐ (B-1 흡수):
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:953:535:- **Implementation Evidence PASS 발효 시점 R-S1 정정 사전조건 명문** ⭐ (N-13 흡수): MVP-2 Implementation Evidence PASS 합의 시 R-S1 정정 *선행 의무* 또는 *동시 의무* 영역 결정 (별도 합의)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:954:550:| **P-4** ⭐⭐⭐ (CONFIRMED divergence 격상) | **R-S1 CONFIRMED divergence** — ADR-012 §2.3 (4-layer) vs §2.8/G4 §4.4.1 (5-layer) | §4.4 답습 (5 source verify: codex + Agent A + Agent B + Agent C + Reviewer). 본 brief v1.1 = 권위 인용 chain 정정 한정 (§1.2 + §2.2.1 + §4.4.2). 다중 source 정정 = §9.5 별도 cycle 영역 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:956:566:| B-1 (R-S1 CONFIRMED 격상) | §0.4 + §1.2 + §1.3 항목 2 + §2.2.1 + §3 (c) + §4.3 (4) + §4.4 신규 + §6.2 #12 + §9.5 + §10 P-4 | "잠재 risk" → "CONFIRMED divergence" 격상 + 5 source cross-confirm + 권위 인용 chain 정정 (G4 §4.4.1 + ADR-012 §2.8 PRIMARY, §2.3 = principle only) + 별도 cross-reference 정정 cycle 사용자 명시 영역 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:960:584:| N-7 (trigger 4 격상) | §4.3 (4) | "부분 발화" → "발화" 격상 (B-1 R-S1 CONFIRMED 답습) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:962:590:| N-13 (PASS 발효 사전조건) | §9.5 | Implementation Evidence PASS 발효 시점 R-S1 정정 사전조건 명문 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:965:/bin/bash -lc "rg -n \"γ|Layer 1\\+2|Layer 4|N-A-1|B-6|R-S1|Rollback|APPROVE|REVISE\" docs/review/3plus1-consensus-2026-05-28-mvp2-entry.md" in /home/delangi/문서/project/category/AI_development_tool
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:968:13:**Reviewer 통합 판정**: ⚠️ **REVISE AS ENTRY BRIEF INPUT (BLOCKING 7 + 권고 13)** — brief v1.1 보강 후 본 cycle 합의 발효 자격 충실. 24 entry codex 답습 동형 판정 (codex `REVISE AS ENTRY BRIEF INPUT` 직접 답습).
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:973:23:| **Reviewer 통합** | Anthropic Claude (Opus 4.7) | **REVISE AS ENTRY BRIEF INPUT** | **7** (Consensus 2 + Unique 5) | **13** (중복 제거) | 통합 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:975:37:| 1 | **R-S1 잠재 → CONFIRMED 격상** | ✅ R-2 BLOCKING | ✅ N-A-4 권고 + verbatim verify | ✅ R-B-1 BLOCKING | ✅ verbatim verify (NOTE) | **Consensus 4/4 ⭐⭐⭐⭐ + Reviewer verify 5/5** |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:977:48:- **C-1 (4/4 source + Reviewer = 5/5)**: **R-S1 = CONFIRMED divergence** (ADR-012 §2.3 4-layer numbering vs §2.8/G4 §4.4.1 5-layer numbering)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:978:73:| **B-1** | C-1 (Consensus 4/4 + Reviewer = 5/5) | **R-S1 CONFIRMED 격상** | codex R-2 + Agent A N-A-4 + Agent B R-B-1 + Agent C verify + Reviewer 단독 verify | brief §10 P-4 "잠재 risk" → "CONFIRMED divergence" 격상 + §1.3 G4 §4.4 Layer 4 항목 답습 보강 + §4.3 trigger (4) "부분 발화" → "발화" 격상 + §9.5 cross-reference 정정 cycle 사용자 명시 영역 추가 | v1.1 §10 P-4 본문 정정 + §1.3 + §4.3 + §9.5 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:983:93:| N-7 | trigger (4) "부분 발화" → "발화" 격상 (B-1 R-S1 CONFIRMED 답습) | Agent B N-B-1 | §4.3 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:984:98:| N-12 | (γ) 4 대안 매트릭스 ((γ-a) Layer 1+2 우선 → Layer 4 후속 / (γ-b) Layer 4 단독 / (γ-c) Layer 1+2+4 동시 / (γ-d) Layer 4 + Layer 1+2 별도) + L 외부 library trade-off + L-1.5 alternative | Agent C N-C-2 + N-C-3 | §2.2.4 + §8.1 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:985:99:| N-13 | Implementation Evidence PASS 발효 시점 R-S1 정정 사전조건 명문 | Agent C N-C-5 + N-C-6 | §9.5 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:986:103:## §4 R-S1 CONFIRMED divergence — Reviewer 단독 verbatim verify 결과
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:987:105:### §4.1 Verbatim 직접 read 결과 (Reviewer 단독, 24 entry R-S1 답습 패턴)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:993:136:### §4.3 R-S1 판정
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:994:138:**R-S1 = CONFIRMED** (5 source verify: codex + Agent A + Agent B + Agent C + Reviewer = 5/5).
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:995:141:- 권위 chain 다중 source divergence (ADR-008 §A.2 R1-2 유형 답습 — 24 entry R-S1 답습 패턴)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:997:145:**본 cycle 처리** (24 entry R-S1 답습):
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1004:185:| N-7 | §4.3 | trigger (4) "부분 발화" → "발화" 격상 (B-1 R-S1 CONFIRMED 답습) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1006:191:| N-13 | §9.5 | Implementation Evidence PASS 발효 시점 R-S1 정정 사전조건 명문 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1013:218:- ❌ R-S1 cross-reference 정정 cycle 자동 진입 (별도 사용자 명시 영역, §4.3 답습)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1017:234:   - **R-S1 cross-reference 정정 cycle** (ADR-012 §2.3 본문 정정 또는 §2.8 동형 답습 cross-reference 강화 — 별도 풀 3+1 + 사용자 명시)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1019:249:| M-5 | R-S1 = 24 entry R-S1 답습 동형 패턴 → "절차적 답습" 위험 | §4 verbatim 직접 read evidence (Reviewer 단독 verify + 4 source verbatim cross-confirm = 5 source) + ADR-012 *자체 내부* divergence 명문 (24 entry 답습 외 발견 영역) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1023:/bin/bash -lc 'rg -n "N-A-1|B-6|R-S1|Layer 1|Layer 4|jsonl_hash_chain|canonical_json|g4-hash-chain|history-anchor|rewrite-defense" docs/external-review/2026-05-28-mvp2-entry-codex-response.md' in /home/delangi/문서/project/category/AI_development_tool
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1029:64:7. ⚠️ **R-S1 잠재 risk 검증** — 본 brief §10 P-4 자기진단 영역 (ADR-012 §2.3 line 182 verbatim = "Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)" 인지 / 또는 G4 §4.4.1 line 649~653 verbatim = "Layer 4 — CI 회귀 검증 (MANDATORY)" 인지). 두 source 의 "Layer 4" 정의 *충돌* 검증 — 권위 chain 다중 source 손상 위험 (24 entry R-S1 답습 패턴, ADR-008 §A.2 R1-2 권위 chain 다중 source 손상 확정 유형). codex 가 ADR-012 §2.3 line 182 verbatim 직접 read + G4 §4.4.1 line 649~653 verbatim 직접 read 후 비교 평가 의무
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1030:85:- §5 R-S1 잠재 risk 검증 결과 (verbatim 인용 + 충돌 분석)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1040:218:| (d) | 자동 회귀 검증 경로 확보 | ❌ gap | **R-6 workflow 에 log file canary inject step 추가 — §4 통합 권고 (G4 §4.4 Layer 4 와 단일 workflow 확장)** |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1050:268:| (a) | 동등 이상 보안 결과 | ❌ gap (실 구현 부재) | Layer 1+2+4 결합 보안 결과 vs 기존 (없음) 비교표 — middle entry tampering / canonical 위반 / timestamp 위반 차단 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1051:272:| (e) | 합의 APPROVE | ❌ gap | **풀 3+1 합의 권고** (G4 §4.4 Layer 1+2+4 통합 + Layer 5 권고 영역 추가 의사결정) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1058:305:| **W-A: 단일 R-6 확장 (GP-2 + G4 §4.4 Layer 4 통합)** | ceremony-inflation 차단 / CI 자원 효율 / evidence 통합 / R-6 답습 한 PR | step 수 증가 / 실패 영역 식별 복잡도 ↑ (step name 분리로 완화 가능) | **✅ 본 brief 권고** |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1063:381:  - GP-2 + G4 §4.4 Layer 4 = 두 영역 통합 합의 (단일 R-6 workflow 확장)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1079:560:| `implementation-runtime-roadmap.md §6` | 2026-05-09 (APPROVED) | 그룹 D (Order 4+5): G2 GP-3 + G2 GP-2. GP-3 = MVP-1 완료, **GP-2 잔존**. 그룹 C (Order 3 tie): G4 JSONL hash chain + JCS + Round-trip PoC (G4 §4.4 영역) | 본 cycle = 그룹 D 잔존 GP-2 진입 + 그룹 C G4 §4.4 Layer 4 진입 통합. |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1080:568:| **G4 §4.4 Layer 4 — CI 회귀 검증** | G4 | Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증 + canonical JSON 위반 검출 + timestamp monotonicity 검증 + R-6 workflow 답습 확장. MANDATORY 등급 (Layer 5 中 4번째, Layer 1+2+4 MANDATORY, Layer 3+5 RECOMMENDED MVP) | `provider-agnostic-memory-skill-design.md §4.4.1 line 649~653` (Layer 4 정의) + `ADR-012 §2.3` (다층 강제) + `ADR-012 §3.4` (timestamp monotonicity) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1081:577:| **G4 §4.4 Layer 4 진입 자격** | provider-agnostic-memory-skill-design §4.4 line 624 (Layer 1~5 MANDATORY/RECOMMENDED 매트릭스) + ADR-012 §2.3 line 165 "Layer 1 MANDATORY 모든 환경" + line 182 "Layer 4 RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점" | **Layer 4 = MANDATORY 등급, MVP-2 진입 영역 채택** | **⚠️ 권위 미세 충돌 흡수 — ADR-012 §2.3 line 182 = "Layer 4 RECOMMENDED MVP" vs G4 §4.4.1 line 649 = "Layer 4 MANDATORY"**. 본 cycle = G4 §4.4.1 line 649 답습 (Layer 4 = MANDATORY). ADR-012 §2.3 line 182 = Layer 4 *External anchor* (Layer 5 영역) 와 혼동 위험 (line 182 verbatim 재확인 의무, R-S1 유형 잠재 risk → 본 brief §10 P-? 자기진단 영역). 본 (α) 합의 발효 시 cross-reference 정정 cycle 후속 영역. |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1082:581:→ **요약**: 본 (α) cycle = "MVP-2 영역 *진입* 합의" 한정 (수단 결정 = (β) 분리). 두 영역 모두 풀 3+1 + 외부 LLM 1+ + 사용자 명시 일관. R-S1 유형 잠재 risk (ADR-012 §2.3 line 182 verbatim 재확인) = §10 자기진단 명시 영역.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1094:669:| **목적** | GP-2 §4.6 산출 후보 (log file canary inject step) + G4 §4.4 Layer 4 (Layer 1+2 자동 회귀 + canonical 위반 + timestamp monotonicity step) **단일 R-6 workflow (`r2-canary.yml`) 확장 통합** |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1098:737:| 4 | 권위 chain 다중 source 손상 위험 | ⚠️ **부분 발화 (R-S1 유형 잠재)** | §1.3 G4 §4.4 Layer 4 항목 = ADR-012 §2.3 line 182 verbatim 재확인 의무 (Layer 4 vs Layer 5 혼동 risk). 본 brief §10 P-? 자기진단 영역 명시. Reviewer 단독 verify 자격 (24 entry R-S1 답습 패턴) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1099:749:| G4 §4.4 Layer 4 | (1) 큰 결정 + (4) 잠재 R-S1 (Layer 4 vs Layer 5 혼동) + (5) 외부 LLM | 풀 3+1 + 외부 LLM 1+ |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1106:815:| 9 | ADR 본문 갱신 자동 cross-reference 변경 | 별도 commit 영역 (R-S1 잠재 정정 영역 포함) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1109:862:| 7 | R-S1 잠재 risk 인식 (ADR-012 §2.3 line 182 Layer 4 vs Layer 5 혼동) | §1.3 자기진단 영역 cross-reference 답습 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1114:877:5. **ADR 본문 cross-reference 갱신 별도 commit** — ADR-008 차단조건 #1 보조 cross-reference 추가 + ADR-012 §2.2 event enum 신규 등록 + ADR-011 §8.5 후속 작업에 GP-2 등록 (R-S1 정정 영역 포함)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1117:925:- **R-S1 정정 영역** (§1.3 ADR-012 §2.3 line 182 Layer 4 vs Layer 5 혼동 verbatim 재확인 + cross-reference 정정) — 본 (α) 합의 발효 후 사용자 명시 시 별도 cycle
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1118:938:| **P-4** | **⚠️ R-S1 유형 잠재 risk 1 — ADR-012 §2.3 line 182 verbatim 재확인 부족 — Layer 4 vs Layer 5 혼동 위험** | §1.3 G4 §4.4 Layer 4 항목 명시 + §4.3 trigger (4) 부분 발화 명시. 본 brief 발효 후 Reviewer 단독 verify 자격 (24 entry R-S1 답습 패턴, 권위 chain 다중 source 손상 확정 시 §9.5 별도 cycle 영역). 본 brief 의 Layer 4 정의 = G4 §4.4.1 line 649~653 답습 (Reviewer Read 확인 evidence 본 brief 작성 시점 read 완료) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1119:941:| **P-7** | 두 영역 통합 진행이 GP-2 / G4 §4.4 Layer 4 *각각* 의 영역 특성 무시 위험 | §2.1 + §2.2 각각 별도 분석 + §3 매트릭스 별도 컬럼 + §4.2 발효 시점 합의 형태 권고 각각 명시 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1120:947:**다음 단계**: 사용자 승인 → 외부 LLM 자격 옵션 결정 ((α) Claude tmux+codex 직접 호출 또는 (β) 사용자 직접 호출) → 외부 LLM 응답 capture → 풀 3+1 합의 (Agent A/B/C 3 병렬 독립 → Reviewer 통합 + R-S1 verify) → brief v1.1 1pass 흡수 보강 → SESSION + INDEX commit + push.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1124:1004:| 4 | 권위 chain 다중 source 손상 위험 | ❌ 미발화 | brief = cross-reference 답습 한정 (§10 17 source 명시), 24 entry R-S1 유형 손상 0건 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1134:1061:| §11 (lines 350~358) | "P-1~P-5 자기진단 (편향 / 통합 복잡도 / 권고 무단 침입 / Layer 4 해석 / 의존 영역)" | ✅ 메타 편향 회피 답습 정확 (특히 P-4 Layer 4 해석 사용자 검토 정정 가능 영역 명시) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1142:1138:PRIMARY와 51 entry 입력 자료는 확인했습니다. 이제 사용자가 지정한 권위 조항의 실제 문구를 직접 대조해서, 특히 ADR-011의 “(a)~(e)” 표현과 R-S1 Layer 4 충돌 가능성을 판정하겠습니다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1143:1454:   488	| 계산적 | docker secret 정의 | `docker-compose.yml` (ADR-008 차단조건 #6 답습, 35번째 entry R-S1 정정 답습) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1168:1932:   137	| (c) | ADR / SDD 권위 명시 | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 + R-4 + 본 §3 (36번째 entry R-S1 정정 답습) | ADR-008 차단조건 #4 + 부록 B + ADR-009 C-N §5 + ADR-011 + P1 v2 + 본 §4 (36번째 entry R-S1 정정 답습) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1169:2082:R-S1의 핵심 대조점이 확인됐습니다. ADR-012 §2.3의 Layer 4는 External anchor이고, G4 §4.4.1의 Layer 4는 CI 회귀 검증입니다. 같은 “Layer 4” 라벨이 서로 다른 의미로 쓰여 있어, brief가 이를 “미세 충돌”로만 처리해도 되는지 별도 blocking으로 판단하겠습니다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1170:2084:/bin/bash -lc 'rg -n "R1-2|권위 chain|다중 source|source 손상|R-S1" docs/decisions docs/review docs/phase0 docs/architecture | head -80' in /home/delangi/문서/project/category/AI_development_tool
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1171:2092:docs/architecture/governance-preconditions.md:106:| **P3** | **Credential / OAuth 파일 권한 노출** | API 키 파일 / OAuth credentials 파일이 world-readable / docker socket mount / inotify 미감시 | 8조 #2 | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 + entrypoint stat 검증 (35번째 entry R-S1 정정 답습) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1172:2093:docs/architecture/governance-preconditions.md:343:| **GP-3** | Credential / Secret Hygiene (저장 + 코드) | P3, P4 | (저장) docker secret + chmod 600 + entrypoint stat + inotify, (코드) gitleaks / detect-secrets pre-commit hook + CI step | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 + 헌법 8조 #1 (35번째 entry R-S1 정정 답습) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1173:2095:docs/architecture/governance-preconditions.md:488:| 계산적 | docker secret 정의 | `docker-compose.yml` (ADR-008 차단조건 #6 답습, 35번째 entry R-S1 정정 답습) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1174:2098:docs/architecture/governance-preconditions.md:498:- ✅ ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 (OAuth credentials 처리 강화) 명시 (충족됨, 35번째 entry R-S1 정정 답습)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1175:2099:docs/architecture/governance-preconditions.md:508:| (c) | ADR / SDD 권위 명시 | ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + 헌법 8조 #1 + 본 §5 (35번째 entry R-S1 정정 답습) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1176:2100:docs/architecture/governance-preconditions.md:523:- ADR-008 cross-reference (차단조건 #1 + #6 + 부록 B): 본문 변경 없음, GP-3 cross-reference 추가 (35번째 entry R-S1 정정 답습)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1177:2102:docs/architecture/jarvis-mvp1-boss-abstraction-design.md:5:**선행**: (4-way) brief v1.1 (`35e0e8c`, 588줄) + 풀 3+1 합의 (`5dcbbdb`, 267줄, APPROVE w/ COND BLOCKING 15 + R-S1~R-S4) + 기존 `src/jarvis/boss.py` 99줄 (commit `83aebad`, 2026-05-22, "feat(jarvis): MVP-1 트랙 A — Boss LLM advisory 판단 지점 (TDD)")
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1178:2103:docs/architecture/jarvis-mvp1-boss-abstraction-design.md:6:**scope**: 기존 `src/jarvis/boss.py` 99줄 design doc *추출* + Backend 후보 매트릭스 *신규* — **신규 코드 0건, 기존 변경 0건** (R-S1 발효 BLOCKING-1 답습 영구)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1179:2104:docs/architecture/jarvis-mvp1-boss-abstraction-design.md:10:## 1. 본 design doc 의 자격 (R-9 + R-15 + R-S1 답습)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1180:2105:docs/architecture/jarvis-mvp1-boss-abstraction-design.md:398:- ⭐⭐⭐ **본 design doc = 기존 `src/jarvis/boss.py` 99줄 (commit `83aebad`) design doc *추출* + Backend 후보 매트릭스 *신규* only** (신규 코드 0건, 기존 변경 0건, R-S1 발효 답습 영구)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1181:2106:docs/architecture/jarvis-mvp1-boss-abstraction-design.md:417:| R-S1 발효 (boss.py:24~98 verbatim 인용) | ✓ §2.1~§2.5 verbatim 인용 완료 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1182:2107:docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification.md:3:> **합의 cycle (f-K)**: Provider Liquidity deep-dive 합의 (`a9e1e88`, BLOCKING 13) 의 **R-26 (C-R2) + R-11** 답습 후속 cycle. brief v1 (`f305174`, 556줄) → 풀 3+1 합의 (Agent A/B/C 병렬 독립 → Reviewer 통합) 산출. **APPROVE w/ COND**, BLOCKING 16 + 권고 21 + NOTE 24, **기각 0**, **Reviewer 단독 격상 BLOCKING 3** (R-S1 / R-S2 / R-S3). 본 합의는 brief v1 의 진술을 BLOCKING 으로 정정하는 *권한* 을 가지나, **(1) ADR-011 §6 본문 정정 자격 0 + (2) Provider Liquidity 본질 약화 자격 0 + (3) MVP-1 합의 본문 정정 자격 0 + (4) 헌법 본문 정정 자격 0 + (5) 메모리 본문 정정 자격 0 + (6) 4 가족 분류 자체의 영구 framing 정착 자격 0 (R-12 답습) + (7) 자동 다음 단계 진입 자격 0 (R-29 + R-30 답습)** 의 **7 권한 한계 영구 답습**.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1183:2108:docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification.md:35:| evidence "GGUF 한정" 더 좁은 한정 (시점 부정합 vs 분류 축) | A-B2 + A-S1 ⭐ / C-B1 + C-S1 ⭐ | A 시점 부정합 + C 분류 축 = 본질 부정 *분리* 동형 → R-S1 통합 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1184:2109:docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification.md:75:- **R-S1 (A-S1 격상)** ⭐: Phase 3 raw line 25~32 결론 verbatim 직접 확인 — "Ollama 다운로드 GGUF = 더 오래된 conversion (`.ssm_dt.bias` 미저장) + llama.cpp `c0c7e147` master = `.dt_bias` → `.dt_proj.bias` rename + `.bias` flag=0 required 강제". 본 evidence 의 본질 = **시점 부정합** (Ollama blob 동기화 미수행 + llama.cpp conversion lineage backward-incompatible 변경) ≠ "GGUF 가족 본질 부정". A-S1 = Reviewer 단독 직접 raw 확인으로 격상 BLOCKING.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1185:2110:docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification.md:163:P3-F1 evidence 의 일반화 자격 = "GGUF 가족 한정" + "sub-차원 (1) tensor naming 한정" + **"1 conversion script lineage × 1 시점" 한정** 3 layer 답습 의무. **R-S1 통합 답습**.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1186:2111:docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification.md:397:**End of consensus report** — 작성 2026-05-24, 3 Agent 병렬 독립 PASS + Reviewer 단독 격상 3건 (R-S1·R-S2·R-S3) + 정합성 매트릭스 + BLOCKING 16 + 권고 21 + NOTE 24 + 기각 0
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1187:2112:docs/architecture/mvp-1-to-6-entry-conditions-brief.md:93:| (c) | ADR / SDD 권위 명시 | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 + R-4 + `roadmap-mvp1.md` §3 (36번째 entry R-S1 정정 답습) | ADR-008 차단조건 #4 + 부록 B + ADR-009 C-N §5 + ADR-011 + P1 v2 + `roadmap-mvp1.md` §4 (36번째 entry R-S1 정정 답습) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1188:2113:docs/architecture/hermes-not-root-of-trust-runtime.md:25:> **[Cross-reference Block — (g1-N-3-adr-008+sip+adr-012') R-7 (f) cross-ref block 만 채택 + R-S1 (CRITICAL) 답습]**: 본 line 23 (상위 권위) + line 176 (cross-ref 표) + line 1040 (영구 핵심 제약 표) 표기 "헌법 제5조 관용 (Provider Liquidity)" / "헌법 5조 (관용 — Provider Liquidity)" / "헌법 5조 (관용)" = (g1-N-1) commit `148fbbe` 후 **헌법 제5조-2: Provider Liquidity 원칙 (비협상) (line 75~80)** 직접 모법 발효 — (g1-N-1) 이전 관용 표현 답습. 본 cycle = gov §1.1 line 78 verbatim 명문 4 source ("ADR-008 / ADR-011 / system-identity-prequel / 본 v3") *외* **유일 추가 동형 source** 신규 식별 (R-S1 CRITICAL, Reviewer raw cross-check 강화 — bash grep `"헌법 제5조 (Provider Liquidity\|헌법 제5조 관용 (Provider Liquidity"` = ADR-012 + 본 source 단 2 파일 verify). Agent C 단독 발견 + Reviewer raw cross-check 직접 verify (line 176/1040 단독 추가 식별). (g1-N-3-pamsd) `ab96e30` 동형 패턴 답습, **본문 verbatim 변경 0건** ((f) cross-ref block 만 채택). 정정 후 형식 = ADR-011 line 245 모법 "제5조-2 관용 (Provider Liquidity, 비협상)" (R-rec-3 답습 + 사용자 명시 직접 확인). 추가 위치 line 7/897/1073 (P3 본문) = 본질 답습, 정정 자격 약함 ((P3) 약식 통일 cycle DEFER carry-over). 본 cycle 합의 = `209f04d`.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1189:2114:docs/phase0/mvp1-r-s1-framing-correction-brief.md:1:# MVP-1 R-S1 cross-reference 정정 + framing 정정 sub-cycle brief ((b2) + (b3) 병렬)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1190:2115:docs/phase0/mvp1-r-s1-framing-correction-brief.md:3:> **scope**: 24번째 entry brief v1.1 carry-over (b2) R-S1 권위 chain 정정 + (b3) roadmap-mvp1 §3.6.3 line 290 framing 정정 (병렬 sub-cycle). 33번째 entry R-S1 raw verify (Agent B + codex 일치) + Reviewer 통합 R-3 답습 (multi-source 재기술).
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1191:2118:docs/phase0/mvp1-r-s1-framing-correction-brief.md:18:| 33번째 entry 합의 보고서 R-MVP1-PASS-2 | brief v1.1 §6 | "R-S1 정정 = cross-reference 정정 한정, ADR-008 본문 변경 영구 금지. 본문 변경 시 풀 3+1 합의 + ADR 권위 영역" |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1192:2119:docs/phase0/mvp1-r-s1-framing-correction-brief.md:19:| 33번째 entry Reviewer R-S1 raw verify | Agent B + codex 일치 | ADR-008 본문 line 136 = §A.2 = "Hermes JSONL Export 검증" + "R1-2" + "§2.6.4" + "§2.6.2" 식별자 ADR-008 본문 0건 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1193:2120:docs/phase0/mvp1-r-s1-framing-correction-brief.md:31:| **scope** | (b2) R-S1 cross-reference 정정 + (b3) roadmap-mvp1 §3.6.3 line 290 framing 정정 (병렬 단일 sub-cycle, cross-reference 정정 영역 유사 = Agent C C-N-6 답습) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1194:2122:docs/phase0/mvp1-r-s1-framing-correction-brief.md:58:## §2 R-S1 cross-reference 정정 매트릭스 (R-3 multi-source 재기술 답습)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1195:2134:docs/phase0/mvp1-r-s1-framing-correction-brief.md:97:| 6 | 523 | `ADR-008 §2.6.4 R1-2: 본문 변경 없음, GP-3 cross-reference 추가` | `ADR-008 cross-reference (차단조건 #1 + #6 + 부록 B): 본문 변경 없음, GP-3 cross-reference 추가 (33번째 entry R-S1 정정 답습)` |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1196:2135:docs/phase0/mvp1-r-s1-framing-correction-brief.md:103:| 1 | 12 | `ADR-008 §A.2 R1-2 + §2.6.2 R2-1 (저장 경로 secret 보호 권위)` | `ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 (저장 경로 secret 보호 권위, 35번째 entry R-S1 정정 답습)` |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1197:2136:docs/phase0/mvp1-r-s1-framing-correction-brief.md:105:| 3 | 390 | `ADR-008 §A.2 R1-2 + §2.6.2 R2-1 답습 \| ✅ (cross-reference 답습 한정 — 본문 변경 0건)` | `ADR-008 차단조건 #1 + #6 + 부록 B 답습 \| ✅ (cross-reference 답습 한정 — 본문 변경 0건, 35번째 entry R-S1 정정 답습)` |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1198:2138:docs/phase0/mvp1-r-s1-framing-correction-brief.md:175:| 2 | R-S1 raw verify 답습 명문 (33번째 Reviewer + Agent B + codex 일치) + ADR-008 본문 §A.2 = "Hermes JSONL Export 검증" + R1-2 식별자 부재 cross-check | ✅ §2.1 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1199:2139:docs/architecture/implementation-runtime-roadmap-mvp1.md:137:| (c) | ADR / SDD 권위 명시 | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 + R-4 + 본 §3 (36번째 entry R-S1 정정 답습) | ADR-008 차단조건 #4 + 부록 B + ADR-009 C-N §5 + ADR-011 + P1 v2 + 본 §4 (36번째 entry R-S1 정정 답습) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1200:2140:docs/architecture/implementation-runtime-roadmap-mvp1.md:143:> ⭐⭐⭐ **2026-05-27 발효 (32번째 entry)**: **GP-3 5/5 + GP-5 5/5 모두 충족 자격 자격 인정 + 사용자 명시 결정 = MVP-1 Implementation Evidence PASS *완전 발효* (α)**. 본 발효 = (b1) 4 sub-cycle 완료 (PC-1-T3 `3a63a5b` + S-3 `4451716` + ST-2 `1edc5bb` + AR-3 `7f57323`/`7c294bb`/`73ed20d`/`9837298`) + 31번째 entry 첫 PR (head SHA `9837298befdeda6c7e170879cc9f15e331c52bce`) 11/11 SUCCESS + mergeable CLEAN + main branch protection 7 contexts 발효 evidence + 본 cycle 풀 3+1 + 외부 LLM 1+ APPROVE WITH CONDITIONS 답습 (`docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md`). carry-over (PASS 효과 영향 0건): (b2) R-S1 cross-reference 정정 + PC-1-T3 PoC evidence 자율 수집 + ST-2 nightly actual run id 자율 수집 + paths-aware workflow audit (R-6 답습).
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1201:2141:docs/architecture/implementation-runtime-roadmap-mvp1.md:205:| **ST-1** | **Hermes Dockerfile entrypoint stat 검증** (chmod 600 강제) | 컨테이너 시작 시 | ✅ 필요 (Hermes upstream Dockerfile 수정) | ❌ | 低 | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + GP-3 §5.3 답습 (36번째 entry R-S1 정정 답습) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1202:2142:docs/architecture/implementation-runtime-roadmap-mvp1.md:206:| **ST-2** | **inotify sidecar** (mtime/perm 변경 → 컨테이너 정지) | 런타임 지속 | ❌ (sidecar 분리 가능) | ✅ | 中 (sidecar process 운영) | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + GP-3 §5.3 답습 (36번째 entry R-S1 정정 답습) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1203:2143:docs/architecture/implementation-runtime-roadmap-mvp1.md:207:| **ST-3** | **docker secret 직접 사용** | 런타임 (file system 통한 노출 회피) | 부분 (docker-compose.yml 갱신) | ❌ | 低 | ADR-008 차단조건 #6 (Docker 격리) + GP-3 §5.3 답습 (36번째 entry R-S1 정정 답습) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1204:2144:docs/architecture/implementation-runtime-roadmap-mvp1.md:209:| **ST-5** | **ST-1 + ST-2 + ST-3 통합** (Defense in depth) | 시작 + 런타임 + file system | ✅ 필요 | ✅ | 中-高 | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + GP-3 §5.3 통합 답습 (36번째 entry R-S1 정정 답습) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1205:2145:docs/architecture/implementation-runtime-roadmap-mvp1.md:283:| ADR-008 cross-reference 갱신 (차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011) | ADR-008 본문 답습 (cross-reference 한정, R-MVP1-PASS-2 영구 금지 답습) | ✅ 35번째 entry (b2) gov + backlog1 + 36번째 entry (b2-roadmap) roadmap-mvp1 본문 R-S1 정정 완료 답습 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1206:2146:docs/architecture/implementation-runtime-roadmap-mvp1.md:506:> ⭐⭐⭐ **2026-05-27 발효 완료 (32번째 entry, commit `(본 commit)`)**: 본 5/5 매트릭스 양 GP 모두 충족 자격 자격 인정 + 사용자 명시 결정 + 본 cycle 풀 3+1 + 외부 LLM 1+ APPROVE WITH CONDITIONS 답습 = **MVP-1 Implementation Evidence PASS *완전 발효 (α)***. 답습 source: (b1) 4 sub-cycle (PC-1-T3 + S-3 + ST-2 + AR-3) + 31번째 entry 첫 PR (head SHA `9837298befdeda6c7e170879cc9f15e331c52bce`) 11/11 SUCCESS + mergeable CLEAN + 본 cycle 합의 (`docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md`, BLOCKING 6 + 권고 5 1pass 흡수). carry-over (PASS 효과 영향 0건): (b2) R-S1 cross-reference 정정 (별도 sub-cycle, ADR-008 본문 변경 0건 영구 의무 R-MVP1-PASS-2 답습) + PC-1-T3 PoC evidence 자율 수집 + ST-2 nightly actual run id 자율 수집 + paths-aware workflow audit (R-MVP1-PASS-8 답습 + R-6 BLOCKING 답습 = 다음 cycle 우선순위).
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1207:2147:docs/architecture/implementation-runtime-roadmap-mvp1.md:660:| **ST-3** | docker secret (저장 경로 isolation) | GP-3 저장 경로 secret 검출 (G3-1) | ADR-008 차단조건 #6 (Docker 격리) 답습 + Layer A §1.2 + Layer B §1.1 답습 (36번째 entry R-S1 정정 답습) | Vault HSM ST-4 미진입 (Backlog #7 분리) / entrypoint stat ST-1 / inotify ST-2 미진입 (Backlog #1 1.5차 보강 분리) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1208:2148:docs/architecture/implementation-runtime-roadmap-mvp1.md:827:| 2026-05-27 (32번째 entry) | ⭐⭐⭐ **MVP-1 Implementation Evidence PASS 완전 발효 (α)** — §2.2 (line 141 영역) + §3.6.3 (GP-3 합의 형태 권고 표) + §4.7.3 (GP-5 합의 형태 권고 표) + §5.1 (통합 PASS 권고) 각 영역에 "2026-05-27 발효 완료" 행 추가 | (b1) 4 sub-cycle 완료 (PC-1-T3 `3a63a5b` + S-3 `4451716` + ST-2 `1edc5bb` + AR-3 chain `7f57323`/`7c294bb`/`73ed20d`/`9837298`) + 31번째 entry 첫 PR (head SHA `9837298befdeda6c7e170879cc9f15e331c52bce`) 11/11 SUCCESS + mergeable CLEAN + main branch protection 7 contexts 발효 evidence + 본 cycle 풀 3+1 + 외부 LLM 1+ APPROVE WITH CONDITIONS (`docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md`, BLOCKING 6 + 권고 5 1pass 흡수). 본 흡수 = §2.2 + §3.6.3 + §4.7.3 + §5.1 + §9 갱신 한정 — §3 GP-3 / §4 GP-5 / §5.2~§5.5 / §6 / §7 본문 변경 0건. carry-over (PASS 효과 영향 0건): (b2) R-S1 + PC-1-T3 PoC 자율 + ST-2 nightly 자율 + paths-aware audit (R-6 BLOCKING 답습) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1209:2149:docs/architecture/implementation-runtime-roadmap-mvp1.md:837:**다음 단계** (2026-05-27 32번째 entry 후): ✅ (b) MVP-1 1.5차 보강 합의 완료 (24번째 entry) → ✅ (b1) 4 sub-cycle 완료 (PC-1-T3 + S-3 + ST-2 + AR-3) → ✅ (c) **Implementation Evidence PASS 완전 발효 완료** (32번째 entry, 본 commit) → ⏳ (D-5 재조정 R-6 BLOCKING 답습): paths-aware workflow audit (R-MVP1-PASS-8 답습) → (b2) R-S1 cross-reference 정정 + (b3) framing 정정 (병렬) → Markdown evidence 통합 (D-3 carry-over) → (b1-PC1-D6) bypass detection CI 통합 → PR #2 merge 결정 (사용자 자율) → (d) facade real → MVP-2 진입 자격 검토 (별도 합의 영역)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1210:2150:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:3:> **본 brief v1.1 = (R4-evidence) brief v1 (`12a3191`, 381줄) 의 풀 3+1 합의 (`f7ed37d`, 346줄, APPROVE w/ COND + BLOCKING 9 + R-S1~R-S5 + 권고 16 + NOTE 15 + 기각 5) verbatim 본문 직접 반영.** v1.1 진입 자격 = (1) BLOCKING 9 verbatim 100% 반영 (R-21 답습 영구) / (2) R-S1~R-S5 정정 흡수 11+곳 / (3) 명명 일관성 통일 = "(R4-evidence)" 단일 + 후속 본문 정정 cycle = "**(R4-body)**" 변경 (R-S2 발효, (g1-N) chain 영구 종결 의무 답습 영구 framing 정합) / (4) §2.2 line 33 → **line 63** verbatim 정정 (R-S1 발효) / (5) §3.5 Phase 1 행 추가 (5-way framing, R-S5 발효) / (6) §11 v→v1.1 변경 일람 신규 / (7) 본 cycle = read-only analysis only (단 brief commit + raw report 단계 R-1 anchor 24회 sudo 1회 의무 자격 별도 분리 명문, R-S4 발효). 자동 다음 단계 진입 0건 (chain 영구 종결 의무 답습 영구).
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1211:2151:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:10:- **(R4-evidence) 풀 3+1 합의** (`docs/review/3plus1-consensus-2026-05-25-jarvis-mvp1-r4-framing-evidence-entry.md`, commit `f7ed37d`, 346줄, BLOCKING 9 + R-S1~R-S5 + 권고 16 + NOTE 15 + 기각 5) — **본 brief v1.1 의 직접 input 자격 영구**
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1212:2152:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:15:- **MVP-1 합의 보고서** (`docs/review/3plus1-consensus-2026-05-22-jarvis-mvp1-local-boss.md`, R4 verbatim **line 63**, R-S1 발효 정정)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1213:2153:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:25:1. MVP-1 합의 R4 본문 verbatim read (MVP-1 brief line 20/124~125/141 + MVP-1 합의 보고서 **line 63**, R-S1 발효 정정) + 현재 framing 명문
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1214:2154:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:62:  - F-2 ⭐⭐⭐: R-S1 완벽 raw evidence (Ollama 자체 standard copy + 별도 inode + content-addressable sha256)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1215:2155:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:65:  - **R4 본문 verbatim (MVP-1 합의 보고서 line 63, R-S1 발효 정정 확정)**: "**R4** | M3 런타임 재조정 — **llama.cpp ↔ Ollama 동급**(MoE 실측 llama.cpp ~31 tok/s, Ollama MoE 미공개), V-1에서 둘 다 MoE 측정. **vLLM \"제외(#36821)\" → \"MVP-1 비채택, MVP-2 재검토\"**(sm_120/121 binary-compat·0.17 해소 흐름; 영구배제는 C-2 충돌) | C | 🔴 정합"
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1216:2156:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:95:## 2. MVP-1 합의 R4 본문 verbatim (read-only, R-S1 발효 line 63 + R-S3 발효 nested quote 정직성)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1217:2157:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:108:### 2.2 MVP-1 합의 보고서 R4 verbatim (R-S1 발효 line 63 정정)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1218:2158:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:110:> **R4 행 verbatim (line 63, R-S1 발효 line 33 → line 63 정정 확정)**: "**R4** | M3 런타임 재조정 — **llama.cpp ↔ Ollama 동급**(MoE 실측 llama.cpp ~31 tok/s, Ollama MoE 미공개), V-1에서 둘 다 MoE 측정. **vLLM \"제외(#36821)\" → \"MVP-1 비채택, MVP-2 재검토\"**(sm_120/121 binary-compat·0.17 해소 흐름; 영구배제는 C-2 충돌) | C | 🔴 정합"
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1219:2159:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:159:- **R-S1 발효 완벽 evidence**: **Ollama 자체 standard copy** ((h-OM) raw line 44 답습 영구, Ollama issue #1450 closed-as-not-planned + docs.ollama.com/import "regular copy" 답습)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1220:2160:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:169:| Source | Ollama library (다른 conversion) | bartowski Q4_K_M | bartowski Q4_K_M | Ollama library blob | **(h) bartowski blob (R-S1 발효 Ollama 자체 standard copy)** |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1221:2161:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:203:- **"동급" 단언 부적정성 자격 강함** (S1 confirmed + R-S1 완벽 raw evidence 답습 영구)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1222:2162:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:213:  - Ollama **(h-OM) Qwen3-30B-A3B bartowski Modelfile** decode generation = **14.69 t/s** (R-S1 발효 standard copy 답습)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1223:2163:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:238:| evidence 강도 (3 차원 a/b/c + 4 차원 격차 + model variant) | ⭐⭐⭐ HIGH (4-way + Phase 1 5-way confirmed, S1 + R-S1 답습 영구) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1224:2164:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:251:  - MVP-1 합의 보고서 R4 행 **line 63** 답습 (R-S1 발효 정정)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1225:2165:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:279:   - (h-O) ↔ (h-OM): source conversion lineage 변수 (R-S1 발효 Ollama 자체 standard copy)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1228:2352:/bin/bash -lc "rg -n \"RT-|E-[1-9]|Rollback|Evidence|R-S1|P-4|ADR-011 §2.1|\\(a\\)~\\(e\\)|Layer 4\" docs/phase0/mvp2-entry-brief.md" in /home/delangi/문서/project/category/AI_development_tool
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1238:2371:93:| `implementation-runtime-roadmap.md §6` | 2026-05-09 (APPROVED) | 그룹 D (Order 4+5): G2 GP-3 + G2 GP-2. GP-3 = MVP-1 완료, **GP-2 잔존**. 그룹 C (Order 3 tie): G4 JSONL hash chain + JCS + Round-trip PoC (G4 §4.4 영역) | 본 cycle = 그룹 D 잔존 GP-2 진입 + 그룹 C G4 §4.4 Layer 4 진입 통합. |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1239:2373:101:| **G4 §4.4 Layer 4 — CI 회귀 검증** | G4 | Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증 + canonical JSON 위반 검출 + timestamp monotonicity 검증 + R-6 workflow 답습 확장. MANDATORY 등급 (Layer 5 中 4번째, Layer 1+2+4 MANDATORY, Layer 3+5 RECOMMENDED MVP) | `provider-agnostic-memory-skill-design.md §4.4.1 line 649~653` (Layer 4 정의) + `ADR-012 §2.3` (다층 강제) + `ADR-012 §3.4` (timestamp monotonicity) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1240:2375:110:| **G4 §4.4 Layer 4 진입 자격** | provider-agnostic-memory-skill-design §4.4 line 624 (Layer 1~5 MANDATORY/RECOMMENDED 매트릭스) + ADR-012 §2.3 line 165 "Layer 1 MANDATORY 모든 환경" + line 182 "Layer 4 RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점" | **Layer 4 = MANDATORY 등급, MVP-2 진입 영역 채택** | **⚠️ 권위 미세 충돌 흡수 — ADR-012 §2.3 line 182 = "Layer 4 RECOMMENDED MVP" vs G4 §4.4.1 line 649 = "Layer 4 MANDATORY"**. 본 cycle = G4 §4.4.1 line 649 답습 (Layer 4 = MANDATORY). ADR-012 §2.3 line 182 = Layer 4 *External anchor* (Layer 5 영역) 와 혼동 위험 (line 182 verbatim 재확인 의무, R-S1 유형 잠재 risk → 본 brief §10 P-? 자기진단 영역). 본 (α) 합의 발효 시 cross-reference 정정 cycle 후속 영역. |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1241:2376:114:→ **요약**: 본 (α) cycle = "MVP-2 영역 *진입* 합의" 한정 (수단 결정 = (β) 분리). 두 영역 모두 풀 3+1 + 외부 LLM 1+ + 사용자 명시 일관. R-S1 유형 잠재 risk (ADR-012 §2.3 line 182 verbatim 재확인) = §10 자기진단 명시 영역.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1250:2391:202:| **목적** | GP-2 §4.6 산출 후보 (log file canary inject step) + G4 §4.4 Layer 4 (Layer 1+2 자동 회귀 + canonical 위반 + timestamp monotonicity step) **단일 R-6 workflow (`r2-canary.yml`) 확장 통합** |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1254:2404:270:| 4 | 권위 chain 다중 source 손상 위험 | ⚠️ **부분 발화 (R-S1 유형 잠재)** | §1.3 G4 §4.4 Layer 4 항목 = ADR-012 §2.3 line 182 verbatim 재확인 의무 (Layer 4 vs Layer 5 혼동 risk). 본 brief §10 P-? 자기진단 영역 명시. Reviewer 단독 verify 자격 (24 entry R-S1 답습 패턴) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1255:2405:282:| G4 §4.4 Layer 4 | (1) 큰 결정 + (4) 잠재 R-S1 (Layer 4 vs Layer 5 혼동) + (5) 외부 LLM | 풀 3+1 + 외부 LLM 1+ |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1261:2429:348:| 9 | ADR 본문 갱신 자동 cross-reference 변경 | 별도 commit 영역 (R-S1 잠재 정정 영역 포함) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1263:2436:395:| 7 | R-S1 잠재 risk 인식 (ADR-012 §2.3 line 182 Layer 4 vs Layer 5 혼동) | §1.3 자기진단 영역 cross-reference 답습 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1267:2441:410:5. **ADR 본문 cross-reference 갱신 별도 commit** — ADR-008 차단조건 #1 보조 cross-reference 추가 + ADR-012 §2.2 event enum 신규 등록 + ADR-011 §8.5 후속 작업에 GP-2 등록 (R-S1 정정 영역 포함)
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1269:2446:458:- **R-S1 정정 영역** (§1.3 ADR-012 §2.3 line 182 Layer 4 vs Layer 5 혼동 verbatim 재확인 + cross-reference 정정) — 본 (α) 합의 발효 후 사용자 명시 시 별도 cycle
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1270:2447:471:| **P-4** | **⚠️ R-S1 유형 잠재 risk 1 — ADR-012 §2.3 line 182 verbatim 재확인 부족 — Layer 4 vs Layer 5 혼동 위험** | §1.3 G4 §4.4 Layer 4 항목 명시 + §4.3 trigger (4) 부분 발화 명시. 본 brief 발효 후 Reviewer 단독 verify 자격 (24 entry R-S1 답습 패턴, 권위 chain 다중 source 손상 확정 시 §9.5 별도 cycle 영역). 본 brief 의 Layer 4 정의 = G4 §4.4.1 line 649~653 답습 (Reviewer Read 확인 evidence 본 brief 작성 시점 read 완료) |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1271:2448:474:| **P-7** | 두 영역 통합 진행이 GP-2 / G4 §4.4 Layer 4 *각각* 의 영역 특성 무시 위험 | §2.1 + §2.2 각각 별도 분석 + §3 매트릭스 별도 컬럼 + §4.2 발효 시점 합의 형태 권고 각각 명시 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1272:2449:480:**다음 단계**: 사용자 승인 → 외부 LLM 자격 옵션 결정 ((α) Claude tmux+codex 직접 호출 또는 (β) 사용자 직접 호출) → 외부 LLM 응답 capture → 풀 3+1 합의 (Agent A/B/C 3 병렬 독립 → Reviewer 통합 + R-S1 verify) → brief v1.1 1pass 흡수 보강 → SESSION + INDEX commit + push.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1273:2485:2. **R-S1 Layer 4 충돌**은 잠재 risk가 아니라 실제 source divergence로 판정해야 합니다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1274:2546:### R-2. R-S1 Layer 4 충돌은 “잠재 risk”가 아니라 실제 source divergence로 격상 필요
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1287:2602:- “R-S1 잠재 risk” → “R-S1 confirmed source divergence”
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1299:2791:- §10 P-4: R-S1 잠재 risk 자기진단
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1302:2833:**평가: GP-2 PASS / G4 PARTIAL WITH R-S1 BLOCKING**
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1310:2920:### 7. R-S1 잠재 risk 검증
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1314:2949:entry brief input 전에는 confirmed R-S1로 격상하고, 본 cycle이 사용하는 Layer numbering 권위를 명시해야 합니다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1315:2951:## §5 R-S1 잠재 risk 검증 결과
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1325:2996:### §5.3 최종 R-S1 판정
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1326:2998:**R-S1 = CONFIRMED**
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1328:3008:1. brief v1.1에서 R-S1을 confirmed로 격상
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1330:3020:- R-2: R-S1은 잠재 risk가 아니라 confirmed source divergence로 격상
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1331:3059:2. **R-S1 Layer 4 충돌**은 잠재 risk가 아니라 실제 source divergence로 판정해야 합니다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1332:3120:### R-2. R-S1 Layer 4 충돌은 “잠재 risk”가 아니라 실제 source divergence로 격상 필요
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1345:3176:- “R-S1 잠재 risk” → “R-S1 confirmed source divergence”
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1357:3365:- §10 P-4: R-S1 잠재 risk 자기진단
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1360:3407:**평가: GP-2 PASS / G4 PARTIAL WITH R-S1 BLOCKING**
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1368:3494:### 7. R-S1 잠재 risk 검증
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1372:3523:entry brief input 전에는 confirmed R-S1로 격상하고, 본 cycle이 사용하는 Layer numbering 권위를 명시해야 합니다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1373:3525:## §5 R-S1 잠재 risk 검증 결과
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1383:3570:### §5.3 최종 R-S1 판정
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1384:3572:**R-S1 = CONFIRMED**
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1386:3582:1. brief v1.1에서 R-S1을 confirmed로 격상
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1388:3594:- R-2: R-S1은 잠재 risk가 아니라 confirmed source divergence로 격상
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1406:| 21 | `pc3_ar1_integration_implementation` | pre-commit + auto-revert 통합 구현 ledger (MVP-1 Stage 4) | T1 audit |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1556:R-S1은 실제로 §2.3과 §2.8의 Layer numbering divergence가 확인됩니다. 마지막으로 PoC 시제의 “5 영역 모두 충족” 주장 자체를 파일 시스템과 테스트 fixture 수 기준으로 검증합니다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1561:"""JSONL ledger hash chain validator — Group C PoC (G4 통합).
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:1825:"""Canonical JSON (RFC 8785 JCS) — Group C PoC (G4 통합).
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:2408:- brief §5.1 RT-γ-6 및 §9.4가 R-S1 후행 영향을 별도 cycle로 보존합니다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:2437:- `본 brief 권고 ... (γ-c) Layer 1+2+4 동시 ... 1순위 + (γ-a) ... 2순위`
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:2529:다만 위험은 단순히 “evidence 분리 미명확”이 아니라, 합의 문서상으로는 Layer 4 단독처럼 보이지만 실제로는 Layer 1+2+4가 묶이는 **implicit bundled scope**입니다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:2533:- `(γ-b)`는 의존 chain은 만족하지만, Layer 1+2의 evidence namespace가 Layer 4 evidence에 흡수될 위험이 있으므로 후속 PASS evidence template에서 layer별 subsection을 강제해야 한다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:2551:### N-5. RT-γ-6은 “후행 영향”뿐 아니라 “PASS 전 선행/동시 정정 후보”로도 남겨야 함
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:2553:brief §5.1 RT-γ-6은 R-S1 cross-reference 정정 후행 영향을 잘 보존합니다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:2555:52 entry §9.5에는 MVP-2 Implementation Evidence PASS 발효 시점에 R-S1 정정이 선행 또는 동시 의무 영역으로 다뤄질 수 있다는 취지가 있습니다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:2559:- R-S1 정정은 본 `(γ)` cycle의 자동 진입 대상은 아니나, MVP-2 Implementation Evidence PASS 발효 시점에는 선행 또는 동시 정정 필요성이 재평가되어야 한다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:2583:- §5.1: RT-γ-1~RT-γ-6
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:2629:### NOTE-4. ADR-012 R-S1 확인 결과
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:2635:따라서 R-S1은 실제 divergence입니다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:2675:- R-S1 정정 후행 영향도 단계별로 흡수하기 쉽습니다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:2696:따라서 `(γ-b)`는 표면상 단일 Layer 4 cycle이지만, 실질적으로는 Layer 1+2+4 통합 cycle입니다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:2713:- 채택 시 layer별 evidence subsection 강제가 필요합니다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:2715:### §4.3 `(γ-c)` Layer 1+2+4 동시 진입
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:2721:`(γ-c)`는 `(γ-b)`와 동일하게 1 cycle 효율을 얻으면서도, Layer 1+2+4를 명시적으로 동시에 다룹니다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:2728:- Layer 1+2+4 evidence를 한 cycle에서 분리 명시할 수 있습니다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:2737:- PASS evidence template이 부실하면 통합 cycle의 장점이 사라집니다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:2787:- Layer 1+2+4를 동시 PASS evidence로 묶음
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:2811:| R-S1 후행 영향 흡수 | 높음 | 중간 | 중간~높음 | 낮음 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:2816:1. `(γ-c)` Layer 1+2+4 동시 진입: **1순위**
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:2866:- brief §5.1 RT-γ-6 및 §9.4가 R-S1 후행 영향을 별도 cycle로 보존합니다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:2895:- `본 brief 권고 ... (γ-c) Layer 1+2+4 동시 ... 1순위 + (γ-a) ... 2순위`
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:2987:다만 위험은 단순히 “evidence 분리 미명확”이 아니라, 합의 문서상으로는 Layer 4 단독처럼 보이지만 실제로는 Layer 1+2+4가 묶이는 **implicit bundled scope**입니다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:2991:- `(γ-b)`는 의존 chain은 만족하지만, Layer 1+2의 evidence namespace가 Layer 4 evidence에 흡수될 위험이 있으므로 후속 PASS evidence template에서 layer별 subsection을 강제해야 한다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:3009:### N-5. RT-γ-6은 “후행 영향”뿐 아니라 “PASS 전 선행/동시 정정 후보”로도 남겨야 함
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:3011:brief §5.1 RT-γ-6은 R-S1 cross-reference 정정 후행 영향을 잘 보존합니다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:3013:52 entry §9.5에는 MVP-2 Implementation Evidence PASS 발효 시점에 R-S1 정정이 선행 또는 동시 의무 영역으로 다뤄질 수 있다는 취지가 있습니다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:3017:- R-S1 정정은 본 `(γ)` cycle의 자동 진입 대상은 아니나, MVP-2 Implementation Evidence PASS 발효 시점에는 선행 또는 동시 정정 필요성이 재평가되어야 한다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:3041:- §5.1: RT-γ-1~RT-γ-6
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:3087:### NOTE-4. ADR-012 R-S1 확인 결과
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:3093:따라서 R-S1은 실제 divergence입니다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:3133:- R-S1 정정 후행 영향도 단계별로 흡수하기 쉽습니다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:3154:따라서 `(γ-b)`는 표면상 단일 Layer 4 cycle이지만, 실질적으로는 Layer 1+2+4 통합 cycle입니다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:3171:- 채택 시 layer별 evidence subsection 강제가 필요합니다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:3173:### §4.3 `(γ-c)` Layer 1+2+4 동시 진입
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:3179:`(γ-c)`는 `(γ-b)`와 동일하게 1 cycle 효율을 얻으면서도, Layer 1+2+4를 명시적으로 동시에 다룹니다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:3186:- Layer 1+2+4 evidence를 한 cycle에서 분리 명시할 수 있습니다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:3195:- PASS evidence template이 부실하면 통합 cycle의 장점이 사라집니다.
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:3245:- Layer 1+2+4를 동시 PASS evidence로 묶음
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:3269:| R-S1 후행 영향 흡수 | 높음 | 중간 | 중간~높음 | 낮음 |
docs/external-review/2026-05-28-mvp2-gamma-codex-response.md:3274:1. `(γ-c)` Layer 1+2+4 동시 진입: **1순위**
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:3:> **본 합의는 추론적 검증(권고) 한정이며 — 본 합의의 어떤 §도 그 자체로 (i) 실 runtime code / CI workflow / hook 구현 / 변경, (ii) Layer 1+2+4 통합 PASS 격상 sub-cycle 자동 진입, (iii) (β) sub-수단 결정 cycle 자동 진입 (R-1~R-5 + L-1~L-5 + W-A~E), (iv) MVP-2 Implementation Evidence PASS 발효, (v) Operational Readiness PASS / Hermes PMO 격상, (vi) ADR / 헌법 / roadmap / governance / G4 / ADR-012 본문 갱신, (vii) Layer 3 (Signed commit) + Layer 5 (External anchor) 영역 자동 진입, (viii) (γ-a/b/d) 대안 재평가 자동 진입, (ix) (γ-e/f/g) hybrid 대안 결정 자동 진입, (x) R-S1 cross-reference 정정 자동 진입, (xi) Tier-2/3 catalog 자동 확장, (xii) 외부 library 도입 결정, (xiii) `adapters/llm/facade.py` placeholder → real 본문 (TR-1), (xiv) Hermes upstream `agent/redact.py` 본 repo 內 import 결정, (xv) branch protection contexts 자동 추가, (xvi) Layer 4 PASS 선발효 ((γ-d) 모순 답습) — 어떤 행위도 자동 발생시키지 않는다. 본 합의 = `mvp2-gamma-decision-brief.md` (241줄) (γ-c) 채택 결정 발효 한정.**
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:8:**합의 형태**: **1-agent 직접 합의** (Claude Opus 4.7 자체 검증, 53 entry Reviewer 통합 권고 답습 한정 + 5/5 풀 3+1 승격 trigger 0/7 발화 자체 검증 후 확정)
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:10:**1차 권위 답습**: 53 entry Reviewer 통합 합의 (`3plus1-consensus-2026-05-28-mvp2-gamma.md`, 264줄, APPROVE WITH CONDITIONS, BLOCKING 8 + 권고 16, (γ-c) 1순위 4 source consensus)
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:11:**판정**: ✅ **APPROVE (1-agent 직접 합의) — (γ-c) Layer 1+2+4 동시 채택 결정 발효 가능, 5/5 풀 3+1 승격 trigger 0/7 발화**
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:20:- (γ-c) Layer 1+2+4 동시 채택 결정 발효 ((γ-a/b/d) = 비채택)
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:21:- Layer 1+2+4 통합 PASS 격상 cycle 진입 자격 발효
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:23:  1. PASS evidence template Layer 1/Layer 2/Layer 4 subsection 강제
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:24:  2. "defense-in-depth 부분 답습" framing 영구 유지 (Layer 3+5 = scope 외)
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:25:  3. Layer 1+2+4 통합 PASS evidence 동시 발효
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:26:  4. RT-γ-6 R-S1 PASS 시점 선행/동시 정정 평가 의무 답습
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:33:- ❌ Layer 1+2+4 통합 PASS 격상 sub-cycle 자동 진입
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:41:- ❌ R-S1 cross-reference 정정 자동 진입 (RT-γ-6 답습)
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:57:| 1 | 큰 결정 (신규 영역 결정 / 수단 결정 / threshold 고정) | ❌ 미발화 | (γ-c) 채택 결정 = 53 entry Reviewer 통합 권고 답습 한정 (4 source consensus 발효 답습). 신규 영역 결정 0 / 수단 결정 0 / threshold 고정 0 |
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:60:| 4 | 권위 chain 다중 source 손상 위험 | ❌ 미발화 | R-S1 = 52/53 entry 발견 + RT-γ-6 답습 (별도 cycle, 본 cycle scope 외) |
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:61:| 5 | 외부 LLM 응답 통합 필요성 | ❌ 미발화 | 본 cycle = Reviewer 통합 권고 답습 한정, 외부 LLM 응답 = 53 entry codex 이미 발효 (재호출 불필요) |
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:65:→ **0/7 미발화 = 1-agent 직접 합의 적격** (Reviewer 통합 권고 답습 한정, ceremony-inflation 차단 메모리 답습).
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:69:## §2 53 entry Reviewer 통합 권고 답습 cross-check
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:72:- (γ-c) Layer 1+2+4 동시 = 1순위 (codex + Agent A 직접 명시 1순위 / Agent B 부분 답습 정정 후 권고 / Agent C 정합)
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:78:- PASS evidence template Layer subsection 강제 = 53 entry N-1 흡수 답습
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:79:- "defense-in-depth 부분 답습" framing 영구 = 53 entry B-6 흡수 답습
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:80:- Layer 1+2+4 통합 PASS 동시 = 53 entry §2.3 답습
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:81:- RT-γ-6 답습 = 53 entry §5.1 답습
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:95:| §0.1 사용자 진입 명령 | "**대안 선택**: **(γ-c) Layer 1+2+4 동시**" + "**합의 형태**: **1-agent 직접**" | ✅ 사용자 명시 (2026-05-28 AskUserQuestion) 정확 |
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:96:| §0.2 #1 | "(γ-c) 채택 결정 발효 정당성 (53 entry Reviewer 통합 권고 + 4 source consensus 답습 cross-check)" | ✅ scope 정확 |
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:98:| §0.4 발효 결과 | "(γ-c) Layer 1+2+4 동시 채택 결정 발효 + 후속 Layer 1+2+4 통합 PASS 격상 cycle 진입 자격 발효 + (γ-c) 특화 의무 명문" | ✅ 발효 효과 정확 |
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:99:| §1.1 4 source consensus | "(γ-c) 1순위 = 4 source consensus (3/4 직접 명시 + Agent B 부분 답습 정정 후 권고)" | ✅ 53 entry §1.4 verbatim 답습 |
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:101:| §1.3 (γ-c) 특화 의무 4 | Layer subsection 강제 + "부분 답습" framing 영구 + Layer 1+2+4 통합 PASS 동시 + RT-γ-6 답습 | ✅ 53 entry N-1 + B-6 + §2.3 + §5.1 답습 정확 |
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:114:- ❌ **Layer 1+2+4 통합 PASS 격상 cycle** — Layer 1+2+4 동시 PASS evidence (각 layer subsection 분리 강제) — 풀 3+1 + 외부 LLM 1+
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:115:- ❌ **실 구현 sub-cycle** — Hermes upstream + 본 repo facade + Layer 1+2+4 PoC → PASS + R-6 확장 (Layer 2a `denyNonFastForwards` 활성화 evidence 별도 verify 의무)
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:116:- ❌ **MVP-2 Implementation Evidence PASS 발효 합의** — (a)~(d) 4조건 evidence + (e) 후속 운영조건 + 사용자 명시 + RT-γ-6 R-S1 PASS 시점 선행/동시 정정 평가
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:118:- ❌ **R-S1 cross-reference 정정 cycle** (RT-γ-6 답습)
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:120:- ❌ Layer 3 (Signed commit) + Layer 5 (External anchor) 영역 진입 — 별도 cycle ("부분 답습" framing 영구 유지)
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:131:- §2: 53 entry Reviewer 통합 권고 답습 5/5 cross-check 정확 (4 source consensus + (γ-c) 특화 의무 + ADR-011 §2.1 매트릭스 + PoC 시제 + (γ-d) 비권고 보존)
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:137:- **(γ-c) Layer 1+2+4 동시 채택 결정 발효** ((γ-a/b/d) = 비채택)
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:138:- **Layer 1+2+4 통합 PASS 격상 cycle 진입 자격 발효**
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:144:**발효되지 않는 영역**: §0 권위 한계 답습 (16+ 금지 사항). Layer 1+2+4 통합 PASS 격상 sub-cycle / (β) 결정 / 실 구현 / MVP-2 Implementation Evidence PASS / Operational Readiness PASS / Hermes PMO 격상 / ADR 본문 갱신 / Layer 3+5 진입 / (γ-a/b/d) 재평가 / (γ-e/f/g) 결정 / R-S1 정정 / Tier-2/3 확장 / 외부 library 도입 / facade.py / Hermes upstream import / branch protection 추가 / Layer 4 PASS 선발효 — 모두 별도 합의 + 사용자 명시 결정 의무 영역.
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:152:1. (1) ✅ **본 합의로 발효** — (γ-c) Layer 1+2+4 동시 채택 결정 발효 + 후속 cycle 진입 자격
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:154:3. **Layer 1+2+4 통합 PASS 격상 cycle** — 풀 3+1 + 외부 LLM 1+ (각 layer subsection 강제)
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:155:4. **실 구현 sub-cycle** ((β) + Layer 통합 PASS 격상 후) — 수단별 차등
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:158:7. **R-S1 cross-reference 정정 cycle** (RT-γ-6 답습)
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:169:| M-1 | 1-agent 직접 합의 = Claude 단독 검증 → cross-vendor blind 의문 | 본 cycle = Reviewer 통합 권고 답습 한정 (53 entry 4 source = Claude 3 + OpenAI 1 cross-vendor 발효 답습). 본 1-agent 직접 = 권고 답습 적격 검증 (신규 결정 0) — cross-vendor 답습 53 entry 답습 보존 |
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:170:| M-2 | 1-agent 직접 합의 = ceremony-inflation 회피 자격 위협 | §1 0/7 풀 3+1 승격 trigger 발화 명시 + 53 entry Reviewer 통합 권고 4 source consensus 답습 한정 + ceremony-inflation 차단 메모리 답습 충실 |
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:172:| M-4 | (γ-c) 특화 의무 (brief §1.3) 가 후속 sub-cycle 결정 영역 침입 | brief §1.3 = 53 entry N-1 + B-6 흡수 답습 (Reviewer 통합 권고 답습 한정) + 후속 sub-cycle 진입 = 사용자 명시 의무 |
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:173:| M-5 | 9/9 verbatim cross-check = 절차적 답습 위험 | §3 cross-check = brief 본문 verbatim 인용 + 53 entry Reviewer 통합 권고 답습 정합성 검증 (단방향 답습 아님, 정합성 검증) |
docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md:174:| M-6 | Reviewer = brief 작성자와 동일 LLM (Opus 4.7) → 편향 위험 | 본 cycle = Reviewer 통합 권고 답습 한정 (53 entry 4 source cross-vendor 발효 답습 보존) + 본 §7 자기진단 다층 답습 |
docs/phase0/mvp2-gamma-decision-brief.md:5:> **scope**: (γ) 4 대안 中 **(γ-c) Layer 1+2+4 동시 채택 결정 발효** 한정 (53 entry Reviewer 통합 권고 답습)
docs/phase0/mvp2-gamma-decision-brief.md:7:> **본 cycle = 작은 영역** (1-agent 직접, Reviewer 통합 권고 답습 한정, ceremony-inflation 차단)
docs/phase0/mvp2-gamma-decision-brief.md:11:> **본 cycle 발효 효과** = (γ-c) Layer 1+2+4 동시 채택 결정 발효 + 후속 Layer 1+2+4 통합 PASS 격상 cycle 진입 자격 발효 (구현 발효 ≠ 본 합의)
docs/phase0/mvp2-gamma-decision-brief.md:20:- **(γ) 4 대안 中 채택 결정** — Reviewer 통합 권고 ((γ-c) 1순위 + (γ-a) 2순위) 답습 + 사용자 명시 결정 (별도 cycle)
docs/phase0/mvp2-gamma-decision-brief.md:23:- **대안 선택**: **(γ-c) Layer 1+2+4 동시** (Reviewer 통합 권고 1순위 답습, 4 source consensus)
docs/phase0/mvp2-gamma-decision-brief.md:26:본 brief = (γ-c) 채택 결정 영역 한정. (β) sub-수단 결정 + Layer 1+2+4 통합 PASS 격상 + 실 구현 = 후속 별도 cycle.
docs/phase0/mvp2-gamma-decision-brief.md:30:1. (γ-c) 채택 결정 발효 정당성 (53 entry Reviewer 통합 권고 + 4 source consensus 답습 cross-check) (§1)
docs/phase0/mvp2-gamma-decision-brief.md:31:2. (γ-c) 채택 결정 발효 효과 명문 (Layer 1+2+4 통합 PASS 격상 cycle 진입 자격 발효) (§2)
docs/phase0/mvp2-gamma-decision-brief.md:43:| 4 | Layer 1+2+4 통합 PASS 격상 sub-cycle 자동 진입 | 0건 (사용자 명시 의무) |
docs/phase0/mvp2-gamma-decision-brief.md:51:| 12 | G4 §4.4 Layer 3 (Signed commit) + Layer 5 (External anchor) 영역 진입 결정 | 0건 (본 (γ-c) = Layer 1+2+4 한정) |
docs/phase0/mvp2-gamma-decision-brief.md:52:| 13 | (γ-a/b/d) 대안 재평가 | 0건 (Reviewer 통합 권고 답습 한정) |
docs/phase0/mvp2-gamma-decision-brief.md:54:| 15 | R-S1 cross-reference 정정 자동 진입 (ADR-012 §2.3 vs §2.8) | 0건 (별도 cycle, RT-γ-6 답습) |
docs/phase0/mvp2-gamma-decision-brief.md:65:- ✅ 본 brief 발효 결과 = **(γ-c) Layer 1+2+4 동시 채택 결정 발효** + 후속 Layer 1+2+4 통합 PASS 격상 cycle 진입 자격 발효 + (γ-c) 특화 의무 명문 ((γ-c) PASS evidence template Layer 1/2/4 subsection 강제 + "부분 답습" framing 영구 유지)
docs/phase0/mvp2-gamma-decision-brief.md:67:- ❌ 본 brief 자체에서 Layer 1+2+4 통합 PASS 격상 sub-cycle 자동 진입 0건
docs/phase0/mvp2-gamma-decision-brief.md:76:### §1.1 Reviewer 통합 권고 답습 (53 entry §1 답습)
docs/phase0/mvp2-gamma-decision-brief.md:80:| 대안 | codex 권고 | Agent A 권고 | Agent B | Agent C | Reviewer 통합 |
docs/phase0/mvp2-gamma-decision-brief.md:82:| **(γ-c) Layer 1+2+4 동시** | **1순위** | **1순위** | (부분 답습 정정 후 권고) | (R-C-3 framing fragile 경고) | **1순위 (3/4 source consensus + Agent B 부분)** |
docs/phase0/mvp2-gamma-decision-brief.md:87:→ **(γ-c) 1순위 = 4 source consensus (3/4 직접 명시 + Agent B 부분 답습 정정 후 권고)**.
docs/phase0/mvp2-gamma-decision-brief.md:93:| 4 source consensus 1순위 | codex §6 + Agent A §6 + Agent B (부분 답습 정정 후 권고) + Reviewer 통합 §1.4 |
docs/phase0/mvp2-gamma-decision-brief.md:96:| defense-in-depth 부분 답습 정합 | 53 entry §2.3.2 + B-6 흡수 — Layer 1+2+4 한정 (Layer 3+5 = scope 외) |
docs/phase0/mvp2-gamma-decision-brief.md:97:| 합의 cycle 효율 | 1 cycle 등가 (Layer 1+2+4 동시 PASS evidence 분리) vs (γ-a) 4 cycle |
docs/phase0/mvp2-gamma-decision-brief.md:106:1. **PASS evidence template Layer 1/Layer 2/Layer 4 subsection 강제** (53 entry N-1 흡수 답습)
docs/phase0/mvp2-gamma-decision-brief.md:109:2. **"defense-in-depth 부분 답습" framing 영구 유지** (53 entry B-6 흡수 답습)
docs/phase0/mvp2-gamma-decision-brief.md:110:   - "부분 답습" 표현 = Layer 1+2+4 한정, Layer 3 (Signed commit) + Layer 5 (External anchor) = 본 cycle scope 외
docs/phase0/mvp2-gamma-decision-brief.md:112:3. **Layer 1+2+4 통합 PASS evidence 동시 발효** ((γ-a) 단계적 vs (γ-c) 통합 차이)
docs/phase0/mvp2-gamma-decision-brief.md:113:4. **R-S1 후행 영향 RT-γ-6 답습** (53 entry §5.1 답습) — Layer 1+2+4 통합 PASS 발효 시 R-S1 정정 영향 평가 의무
docs/phase0/mvp2-gamma-decision-brief.md:123:1. **(γ-c) Layer 1+2+4 동시 채택 결정 발효** — (γ-a/b/d) 대안 = 비채택 (Reviewer 통합 권고 답습 한정)
docs/phase0/mvp2-gamma-decision-brief.md:124:2. **Layer 1+2+4 통합 PASS 격상 cycle 진입 자격 발효** — 후속 sub-cycle 진입 권한 (사용자 명시 의무)
docs/phase0/mvp2-gamma-decision-brief.md:131:- ❌ Layer 1+2+4 통합 PASS 격상 sub-cycle 자동 진입 (사용자 명시 의무)
docs/phase0/mvp2-gamma-decision-brief.md:140:본 §3 = 본 cycle 1-agent 직접 합의 적격성 자체 검증 (Reviewer 통합 권고 답습 한정 = ceremony-inflation 차단).
docs/phase0/mvp2-gamma-decision-brief.md:144:| 1 | 큰 결정 (신규 영역 결정 / 수단 결정 / threshold 고정) | ❌ 미발화 | (γ-c) 채택 결정 = Reviewer 통합 권고 답습 한정 (53 entry 4 source consensus 발효 답습). 신규 영역 결정 0 / 수단 결정 0 |
docs/phase0/mvp2-gamma-decision-brief.md:147:| 4 | 권위 chain 다중 source 손상 위험 | ❌ 미발화 | R-S1 = 52/53 entry 발견 + RT-γ-6 답습 (별도 cycle, 본 cycle scope 외) |
docs/phase0/mvp2-gamma-decision-brief.md:148:| 5 | 외부 LLM 응답 통합 필요성 | ❌ 미발화 | 본 cycle = Reviewer 통합 권고 답습 한정, 외부 LLM 응답 = 53 entry codex 이미 발효 (재호출 불필요) |
docs/phase0/mvp2-gamma-decision-brief.md:152:→ **0/7 발화 → 1-agent 직접 합의 적격 (Reviewer 통합 권고 답습 한정, ceremony-inflation 차단 메모리 답습)**.
docs/phase0/mvp2-gamma-decision-brief.md:161:2. **Layer 1+2+4 통합 PASS 격상 cycle** — Layer 1 hash chain + Layer 2 Git append-only + Layer 4 CI 회귀 검증 동시 PASS evidence (각 layer subsection 분리 강제, §1.3 답습) — 풀 3+1 + 외부 LLM 1+
docs/phase0/mvp2-gamma-decision-brief.md:162:3. **실 구현 sub-cycle** ((β) + (γ-c) 채택 후) — Hermes upstream `agent/redact.py` 영역 + 본 repo P1 facade RedactionFilter (TR-1 (d) carry-over 의존) + Layer 1+2+4 PoC → PASS + R-6 workflow 확장 step (Layer 2a `denyNonFastForwards` 활성화 evidence 별도 verify 의무, 53 entry B-3 답습)
docs/phase0/mvp2-gamma-decision-brief.md:163:4. **MVP-2 Implementation Evidence PASS 발효 합의** — (a)~(d) 4조건 evidence + (e) 후속 운영조건 + 사용자 명시 + RT-γ-6 R-S1 PASS 시점 선행/동시 정정 평가 (32 entry 답습 패턴)
docs/phase0/mvp2-gamma-decision-brief.md:165:6. **R-S1 cross-reference 정정 cycle** — ADR-012 §2.3 본문 정정 또는 §2.8 동형 답습 강화 (RT-γ-6 답습)
docs/phase0/mvp2-gamma-decision-brief.md:178:| 1 | 자동 Layer 1+2+4 통합 PASS 격상 sub-cycle 진입 | 사용자 명시 의무 |
docs/phase0/mvp2-gamma-decision-brief.md:183:| 6 | R-S1 cross-reference 정정 자동 진입 | 별도 cycle (RT-γ-6 답습) |
docs/phase0/mvp2-gamma-decision-brief.md:184:| 7 | Layer 3 (Signed commit) + Layer 5 (External anchor) 자동 진입 | 별도 cycle ("부분 답습" framing 영구 유지) |
docs/phase0/mvp2-gamma-decision-brief.md:186:| 9 | Layer 4 evidence 內 Layer 1+2 evidence 합산 | 영구 금지 (PASS evidence template Layer subsection 강제 §1.3 답습) |
docs/phase0/mvp2-gamma-decision-brief.md:201:- 53 entry Reviewer 통합 합의 — `docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md` (264줄, APPROVE WITH CONDITIONS, BLOCKING 8 + 권고 16, (γ-c) 1순위 + (γ-a) 2순위 + (γ-b) 3순위 + (γ-d) 비권고 4 source consensus)
docs/phase0/mvp2-gamma-decision-brief.md:205:- 52 entry Reviewer 통합 합의 — `docs/review/3plus1-consensus-2026-05-28-mvp2-entry.md`
docs/phase0/mvp2-gamma-decision-brief.md:222:- (γ-c) Layer 1+2+4 통합 PASS evidence template 작성 (Layer subsection 강제, §1.3 답습)
docs/phase0/mvp2-gamma-decision-brief.md:223:- R-S1 cross-reference 정정 (52/53 entry §9.5 + RT-γ-6 답습)
docs/phase0/mvp2-gamma-decision-brief.md:231:| P-1 | 본 brief 가 (γ-c) 채택을 *권유* 방향으로 편향 | §0.3 21 금지 + §0.4 권위 한계 + §3 5/5 trigger 0건 자체 검증 = Reviewer 통합 권고 답습 한정 (4 source consensus 답습) |
docs/phase0/mvp2-gamma-decision-brief.md:232:| P-2 | 1-agent 직접 합의가 ceremony-inflation 회피 자격 위협 | §3 0/7 trigger 발화 자체 검증 + 53 entry Reviewer 통합 권고 4 source consensus 답습 = ceremony-inflation 차단 정합 (메모리 답습) |
docs/phase0/mvp2-gamma-decision-brief.md:233:| P-3 | (γ-c) 채택 결정 = (γ-a/b/d) 대안 영구 비채택 → 결정 영역 침입 risk | §5 #4 "재평가 = 별도 cycle 사용자 명시" 영구 보존 + Reviewer 통합 권고 답습 한정 (본 cycle = 권고 답습, 신규 결정 0) |
docs/phase0/mvp2-gamma-decision-brief.md:234:| P-4 | (γ-c) 특화 의무 (§1.3) 가 후속 sub-cycle 결정 영역 침입 | §1.3 의무 = 53 entry N-1 + B-6 흡수 답습 (Reviewer 통합 권고 답습 한정) + 후속 sub-cycle = 사용자 명시 의무 (§5 #1 답습) |
docs/phase0/mvp2-gamma-decision-brief.md:235:| P-5 | R-S1 후행 영향 (RT-γ-6) 가 본 cycle 결정 영향 | §1.3 의무 #4 + §5 #6 = 별도 cycle 답습 + Layer 1+2+4 통합 PASS 발효 시 평가 의무 명문 |

codex
PoC scripts themselves는 requirements-dev에 의존성이 명시돼 있고 workflows도 설치 step을 포함합니다. 현재 shell에는 해당 패키지가 없어 로컬 “actual run”은 실패했으므로, repo를 건드리지 않는 임시 venv로 의존성을 넣어 실행 가능성만 검증하겠습니다.
exec
/bin/bash -lc 'python3 -m venv /tmp/aidt-review-venv && /tmp/aidt-review-venv/bin/python -m pip install --upgrade pip >/tmp/aidt-pip.log && /tmp/aidt-review-venv/bin/pip install rfc8785==0.1.4 jcs==0.2.1 >>/tmp/aidt-pip.log 2>&1 && echo venv_ready' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 2301ms:
venv_ready

exec
/bin/bash -lc '/tmp/aidt-review-venv/bin/python tools/jsonl_hash_chain.py tests/fixtures/jsonl_ledger/pass/minimal_chain.jsonl && /tmp/aidt-review-venv/bin/python tools/jsonl_hash_chain.py tests/fixtures/jsonl_ledger/pass/roundtrip_t2_strict.jsonl' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
PASS: minimal_chain.jsonl — 2 entries, all checks passed (schema + chain + monotonicity)
PASS: roundtrip_t2_strict.jsonl — 2 entries, all checks passed (schema + chain + monotonicity)

exec
/bin/bash -lc 'for f in tests/fixtures/jsonl_ledger/fail/*.jsonl; do /tmp/aidt-review-venv/bin/python tools/jsonl_hash_chain.py "$f" >/tmp/hash.out 2>/tmp/hash.err; rc=$?; printf '"'%s rc=%s\\n' \""'$f" "$rc"; sed -n '"'1,12p' /tmp/hash.err; done" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
tests/fixtures/jsonl_ledger/fail/genesis_mismatch.jsonl rc=1
FAIL: genesis_mismatch.jsonl — 1 violation(s):
  [0] id=ffffffff-ffff-4fff-8fff-ffffffffffff type=genesis_mismatch
      detail: first entry prev_hash='ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff' != genesis='41773a975288c776944ef8fa8d4b5c6bc79504d2197874aec2bfe27b820db5b5'
tests/fixtures/jsonl_ledger/fail/hash_recalculation.jsonl rc=1
FAIL: hash_recalculation.jsonl — 1 violation(s):
  [1] id=dddddddd-dddd-4ddd-8ddd-dddddddddddd type=hash_recalculation
      detail: hash field='deadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeefdeadbeef' != recomputed='349e86f04c95d8a5b3fd2b81dff6e8ef7711154616140cbe3649b592b68069f2'
tests/fixtures/jsonl_ledger/fail/missing_event_field.jsonl rc=1
FAIL: missing_event_field.jsonl — 1 violation(s):
  [0] id=eeeeeeee-eeee-4eee-8eee-eeeeeeeeeeee type=schema_missing_field
      detail: missing required fields: ['event']
tests/fixtures/jsonl_ledger/fail/prev_hash_mismatch.jsonl rc=1
FAIL: prev_hash_mismatch.jsonl — 1 violation(s):
  [1] id=bbbbbbbb-bbbb-4bbb-8bbb-bbbbbbbbbbbb type=prev_hash_mismatch
      detail: prev_hash='0000000000000000000000000000000000000000000000000000000000000000' != prior entry hash='ff0fb84f7a3786f718afb6d9bd56e2dae0232361b8fc881c9ee1e99df4bdeab4'

exec
/bin/bash -lc 'for inp in tests/canonical/*/*.input.json; do base=${inp%.input.json}; /tmp/aidt-review-venv/bin/python tools/canonical_json.py --mode cross_check --input "$inp" --expected-canonical "${base}.expected.canonical" --expected-sha256 "${base}.expected.sha256" >/dev/null || exit 1; done; echo canonical_cross_check_all_pass' in /home/delangi/문서/project/category/AI_development_tool
exec
/bin/bash -lc "/tmp/aidt-review-venv/bin/python tools/jsonl_hash_chain.py --help | sed -n '1,80p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
usage: jsonl_hash_chain.py [-h] [--emit-violation-entry] path

JSONL ledger hash chain validator — Group C PoC (G4 통합)

positional arguments:
  path                  JSONL ledger 파일 경로

options:
  -h, --help            show this help message and exit
  --emit-violation-entry
                        chain violation 검출 시 chain_violation_detected entry 를
                        stdout 에 출력

 succeeded in 585ms:
# mode=cross_check sha256=c41176394d3b2dfdac3e8edff2d8e9e4ae62a218f674f6929d3d12ce5aca369b fallback_used=False cross_check_passed=True
# mode=cross_check sha256=d554384db4d03f45143bbb1b6e534c0faa839eab6e418cad97e46becd728fe42 fallback_used=False cross_check_passed=True
# mode=cross_check sha256=e6a3385fb77c287a712e7f406a451727f0625041823ecf23bea7ef39b2e39805 fallback_used=False cross_check_passed=True
# mode=cross_check sha256=a0a095eaef4ef6f5971cea52026bb5c5b50844a55c96d4cf9f0bf9292363d777 fallback_used=False cross_check_passed=True
# mode=cross_check sha256=0888e6b69fec49c8af5806a8f8c244026f1fb0da3bb73553189248b2ee58d7c8 fallback_used=False cross_check_passed=True
# mode=cross_check sha256=0a80298409fda443db411d68bc6792586238af52f752955aaa10d397b40d5503 fallback_used=False cross_check_passed=True
# mode=cross_check sha256=5e4291a72609c36fbe21976831a8fbd154d33f0dca203f915b6fa21e965acdc9 fallback_used=False cross_check_passed=True
# mode=cross_check sha256=59e0492137bd5891160f9f69bb080ca4eb7d63f34cf4cc1d22661c11911eec8a fallback_used=False cross_check_passed=True
# mode=cross_check sha256=e29e1c543a1326961abf9a7e87f6551eb260a5b734e3d065ad619fc0a76fe1a8 fallback_used=False cross_check_passed=True
# mode=cross_check sha256=65b2bf481f2377af7fe4efeedbbc8e32b32677a6bbae02dd3f2c138a65a4e9b4 fallback_used=False cross_check_passed=True
# mode=cross_check sha256=23b7fe02eabd305fc16aa735008b290c197a7e0514c2a4a31f2fe2d68825394e fallback_used=False cross_check_passed=True
# mode=cross_check sha256=20d9223d96ee25b968bf08a080abc1028dcc5a84d56bf5770dfde3885b5de3cf fallback_used=False cross_check_passed=True
# mode=cross_check sha256=d065701b86083f489cc8669338c6fc18d144256ea58416c010e7c4927dcd7b0a fallback_used=False cross_check_passed=True
# mode=cross_check sha256=4dad51ac41eb73862fce375fae85ba13711fd19f1b26d8e4b1f9fa405c3d5adf fallback_used=False cross_check_passed=True
# mode=cross_check sha256=b84c301717ca815f8ad20b0cfd2c918f7e1d85b0af2e2980e7d814ef5e7cd437 fallback_used=False cross_check_passed=True
# mode=cross_check sha256=f3013f933b9fb80ab6d995e7ad9da36f683837ba1d81e950c943d40111eac2f0 fallback_used=False cross_check_passed=True
# mode=cross_check sha256=9aa3f9b311e3f026d97defa4d776d1145b534e38d0ca856a7b215fd80091ea3d fallback_used=False cross_check_passed=True
# mode=cross_check sha256=344183faebdcdc99617d29bf5f6787f7e7bbfd9bc15987b32dca64599ad86820 fallback_used=False cross_check_passed=True
# mode=cross_check sha256=47a47202d021be06dcb0cf0f7f943a022eb9bb434ef039969ffaa344b9280dca fallback_used=False cross_check_passed=True
canonical_cross_check_all_pass

exec
/bin/bash -lc "sed -n '190,240p' .github/workflows/g4-hash-chain.yml && rg -n \"history_rewrite|ViolationType|emit-violation|violation_type\" tools/jsonl_hash_chain.py tests/fixtures/jsonl_ledger .github/workflows/g4-hash-chain.yml" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
            if [ "$rc" -ne 0 ]; then
              echo "::error::PASS fixture $f returned rc=$rc (expected 0)"
              exit 1
            fi
          done
          echo "PASS fixtures verified (rc=0 for all)"

      - name: FAIL fixture — jsonl_hash_chain rc=1 + 4 violation_type cover
        run: |
          set -e
          # Expected violation_type per fixture (4 패턴 cover 강제)
          declare -A EXPECTED=(
            [prev_hash_mismatch.jsonl]=prev_hash_mismatch
            [hash_recalculation.jsonl]=hash_recalculation
            [missing_event_field.jsonl]=schema_missing_field
            [genesis_mismatch.jsonl]=genesis_mismatch
          )
          for f in tests/fixtures/jsonl_ledger/fail/*.jsonl; do
            name=$(basename "$f")
            expected="${EXPECTED[$name]:-}"
            set +e
            python tools/jsonl_hash_chain.py "$f" 2> chain_out.txt
            rc=$?
            set -e
            cat chain_out.txt
            if [ "$rc" -ne 1 ]; then
              echo "::error::FAIL fixture $name returned rc=$rc (expected 1)"
              exit 1
            fi
            if [ -n "$expected" ] && ! grep -q "type=$expected" chain_out.txt; then
              echo "::error::FAIL fixture $name missing violation_type=$expected"
              exit 1
            fi
            echo "  $name OK (rc=1, violation_type=$expected)"
          done
          rm -f chain_out.txt
          echo "FAIL fixtures verified — 4 violation_type cover (chain violation 4 패턴 답습)"

      - name: Round-trip — T2 strict on PASS fixtures
        run: |
          set -e
          for f in tests/fixtures/jsonl_ledger/pass/*.jsonl; do
            set +e
            python tools/jsonl_roundtrip.py --require-strict "$f"
            rc=$?
            set -e
            if [ "$rc" -ne 0 ]; then
              echo "::error::Round-trip T2 strict FAIL on $f (rc=$rc, TR-C-4 trigger)"
              exit 1
            fi
            echo "  $(basename $f) — T2 strict PASS"
.github/workflows/g4-hash-chain.yml:15:#   - FAIL fixture × 4: jsonl_hash_chain.py rc=1 + 4 violation_type cover
.github/workflows/g4-hash-chain.yml:197:      - name: FAIL fixture — jsonl_hash_chain rc=1 + 4 violation_type cover
.github/workflows/g4-hash-chain.yml:200:          # Expected violation_type per fixture (4 패턴 cover 강제)
.github/workflows/g4-hash-chain.yml:220:              echo "::error::FAIL fixture $name missing violation_type=$expected"
.github/workflows/g4-hash-chain.yml:223:            echo "  $name OK (rc=1, violation_type=$expected)"
.github/workflows/g4-hash-chain.yml:226:          echo "FAIL fixtures verified — 4 violation_type cover (chain violation 4 패턴 답습)"
tools/jsonl_hash_chain.py:18:  - violation_type 4종: prev_hash_mismatch / hash_recalculation / history_rewrite / genesis_mismatch
tools/jsonl_hash_chain.py:66:class ViolationType(str, Enum):
tools/jsonl_hash_chain.py:71:    HISTORY_REWRITE = "history_rewrite"
tools/jsonl_hash_chain.py:81:    violation_type: str  # ViolationType.value or "schema_*" / "monotonicity_*"
tools/jsonl_hash_chain.py:121:                violation_type="schema_missing_field",
tools/jsonl_hash_chain.py:191:                    ViolationType.HASH_RECALCULATION.value,
tools/jsonl_hash_chain.py:204:                        ViolationType.GENESIS_MISMATCH.value,
tools/jsonl_hash_chain.py:214:                        ViolationType.PREV_HASH_MISMATCH.value,
tools/jsonl_hash_chain.py:254:    # 첫 violation 이 history_rewrite 가능성 ↔ 그 외 분류
tools/jsonl_hash_chain.py:258:        if v.violation_type in {vt.value for vt in ViolationType}
tools/jsonl_hash_chain.py:285:            "violation_type": chain_violations[0].violation_type,
tools/jsonl_hash_chain.py:314:                        violation_type="parse_error",
tools/jsonl_hash_chain.py:324:                        violation_type="parse_error",
tools/jsonl_hash_chain.py:339:        "--emit-violation-entry",
tools/jsonl_hash_chain.py:383:            f"  [{v.entry_index}] id={v.entry_id} type={v.violation_type}",

exec
/bin/bash -lc "sed -n '240,310p' tools/jsonl_hash_chain.py && sed -n '310,390p' tools/jsonl_hash_chain.py" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:


def build_violation_entry(
    entries: list[dict[str, Any]],
    violations: list[Violation],
) -> dict[str, Any] | None:
    """chain_violation_detected ledger entry 자동 작성 (ADR-012 §2.7).

    Returns:
        새 ledger entry dict (caller 가 ledger 에 append 가능 형식) 또는 None (위반 0건)
    """
    if not violations:
        return None

    # 첫 violation 이 history_rewrite 가능성 ↔ 그 외 분류
    first_vio = violations[0]
    chain_violations = [
        v for v in violations
        if v.violation_type in {vt.value for vt in ViolationType}
    ]
    if not chain_violations:
        # schema/monotonicity 위반만 — chain_violation_detected 자동 작성 영역 외
        return None

    # 마지막 entry 의 hash 를 prev_hash 로 사용 (chain 연속성 — append-only 답습)
    if entries:
        last_entry = entries[-1]
        prev_hash = last_entry.get("hash", compute_genesis_hash(
            last_entry.get("scope", "global"), last_entry.get("schema_version", SUPPORTED_SCHEMA_VERSION)
        ))
        scope = last_entry.get("scope", "global")
    else:
        prev_hash = compute_genesis_hash("global", SUPPORTED_SCHEMA_VERSION)
        scope = "global"

    now_iso = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    entry: dict[str, Any] = {
        "type": "meta",
        "scope": scope,
        "id": f"chain-violation-{now_iso}",
        "schema_version": SUPPORTED_SCHEMA_VERSION,
        "ts": now_iso,
        "agent": "user",  # ADR-012 §2.12 — Hermes 자기 작성 금지, 외부 트리거 한정
        "event": "chain_violation_detected",
        "content": {
            "violation_type": chain_violations[0].violation_type,
            "detected_at": now_iso,
            "affected_entry": chain_violations[0].entry_id,
            "violations_count": len(chain_violations),
            "first_detail": chain_violations[0].detail[:200],
        },
        "evidence_refs": [],
        "prev_hash": prev_hash,
    }
    entry["hash"] = compute_entry_hash(entry)
    return entry


def parse_jsonl(path: Path) -> tuple[list[dict[str, Any]], list[Violation]]:
    """JSONL 파일 파싱 — line-by-line (Group A 답습)."""
    entries: list[dict[str, Any]] = []
    parse_vios: list[Violation] = []
    with open(path, "r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            stripped = line.strip()
            if not stripped:
                continue
            try:
                entry = json.loads(stripped)
            except json.JSONDecodeError as e:
                parse_vios.append(
                parse_vios.append(
                    Violation(
                        entry_index=lineno - 1,
                        entry_id=f"<line={lineno}>",
                        violation_type="parse_error",
                        detail=f"JSON parse failed: {e}",
                    )
                )
                continue
            if not isinstance(entry, dict):
                parse_vios.append(
                    Violation(
                        entry_index=lineno - 1,
                        entry_id=f"<line={lineno}>",
                        violation_type="parse_error",
                        detail=f"entry not dict: type={type(entry).__name__}",
                    )
                )
                continue
            entries.append(entry)
    return entries, parse_vios


def _cli() -> int:
    p = argparse.ArgumentParser(
        description="JSONL ledger hash chain validator — Group C PoC (G4 통합)"
    )
    p.add_argument("path", type=str, help="JSONL ledger 파일 경로")
    p.add_argument(
        "--emit-violation-entry",
        action="store_true",
        help="chain violation 검출 시 chain_violation_detected entry 를 stdout 에 출력",
    )
    args = p.parse_args()

    try:
        path = Path(args.path)
    except OSError as e:
        print(f"PATH_ERROR: {e}", file=sys.stderr)
        return 2

    if not path.exists():
        print(f"FILE_NOT_FOUND: {path}", file=sys.stderr)
        return 2

    try:
        entries, parse_vios = parse_jsonl(path)
    except OSError as e:
        print(f"READ_ERROR: {e}", file=sys.stderr)
        return 2

    all_vios: list[Violation] = list(parse_vios)
    schema_vios: list[Violation] = []
    for i, entry in enumerate(entries):
        schema_vios.extend(validate_schema(entry, i))
    all_vios.extend(schema_vios)

    # schema 위반된 entry 는 chain 검증 skip (cascading 회피)
    valid_indices = set(range(len(entries))) - {v.entry_index for v in schema_vios}
    valid_entries = [entries[i] for i in sorted(valid_indices)]
    chain_vios = validate_chain(valid_entries)
    all_vios.extend(chain_vios)

    if not all_vios:
        print(
            f"PASS: {path.name} — {len(entries)} entries, all checks passed (schema + chain + monotonicity)",
            file=sys.stderr,
        )
        return 0

    print(f"FAIL: {path.name} — {len(all_vios)} violation(s):", file=sys.stderr)
    for v in all_vios:
        print(
            f"  [{v.entry_index}] id={v.entry_id} type={v.violation_type}",
            file=sys.stderr,
        )
        print(f"      detail: {v.detail}", file=sys.stderr)

    if args.emit_violation_entry:
        violation_entry = build_violation_entry(entries, all_vios)
        if violation_entry is not None:

exec
/bin/bash -lc "nl -ba tools/jsonl_hash_chain.py | sed -n '305,330p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
   305	            if not stripped:
   306	                continue
   307	            try:
   308	                entry = json.loads(stripped)
   309	            except json.JSONDecodeError as e:
   310	                parse_vios.append(
   311	                    Violation(
   312	                        entry_index=lineno - 1,
   313	                        entry_id=f"<line={lineno}>",
   314	                        violation_type="parse_error",
   315	                        detail=f"JSON parse failed: {e}",
   316	                    )
   317	                )
   318	                continue
   319	            if not isinstance(entry, dict):
   320	                parse_vios.append(
   321	                    Violation(
   322	                        entry_index=lineno - 1,
   323	                        entry_id=f"<line={lineno}>",
   324	                        violation_type="parse_error",
   325	                        detail=f"entry not dict: type={type(entry).__name__}",
   326	                    )
   327	                )
   328	                continue
   329	            entries.append(entry)
   330	    return entries, parse_vios

exec
/bin/bash -lc "printf 'local='; git config --local --get receive.denyNonFastForwards || true; printf 'global='; git config --global --get receive.denyNonFastForwards || true; printf 'system='; git config --system --get receive.denyNonFastForwards || true" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
local=global=system=
exec
/bin/bash -lc 'gh api repos/jokwangwon/AI_development_tool/branches/main/protection/required_status_checks/contexts && gh api repos/jokwangwon/AI_development_tool/branches/main/protection/required_pull_request_reviews && gh api repos/jokwangwon/AI_development_tool/branches/main/protection/enforce_admins' in /home/delangi/문서/project/category/AI_development_tool
exec
/bin/bash -lc "find tests/canonical -mindepth 1 -maxdepth 1 -type d -printf '%f\\n' | sort | wc -l && find tests/canonical -mindepth 1 -maxdepth 1 -type d -printf '%f\\n' | sort" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
8
array
escape
hash_stability
key_ordering
lossy
nested
number
unicode

exec
/bin/bash -lc 'find tests/fixtures/jsonl_ledger/pass -type f | wc -l; find tests/fixtures/jsonl_ledger/fail -type f | wc -l; find tests/fixtures/history_anchor_verifier/pass -type f | wc -l; find tests/fixtures/history_anchor_verifier/fail -type f | wc -l' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
2
4
4
9

 succeeded in 1262ms:
["guard","verify","feasibility","scan","enforce","defense","validate","bypass-detect"]{"url":"https://api.github.com/repos/jokwangwon/AI_development_tool/branches/main/protection/required_pull_request_reviews","dismiss_stale_reviews":false,"require_code_owner_reviews":false,"require_last_push_approval":false,"required_approving_review_count":0}{"url":"https://api.github.com/repos/jokwangwon/AI_development_tool/branches/main/protection/enforce_admins","enabled":true}
codex
**검토자 / Vendor**

- 검토자: OpenAI Codex CLI
- 응답 vendor: OpenAI
- 본 cycle 3+1 Agent vendor: Anthropic Claude
- Cross-vendor blind review 조건: 충족
- 판정: **APPROVE WITH CONDITIONS**
- BLOCKING: **0건**
- 권고: **8건**
- NOTE: **5건**

**직접 검토한 Working Directory 자료**

- [mvp2-layer-124-pass-entry-brief.md](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-layer-124-pass-entry-brief.md)
- [mvp2-gamma-decision-brief.md](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-gamma-decision-brief.md)
- [1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md](/home/delangi/문서/project/category/AI_development_tool/docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md)
- [mvp2-gamma-layer-separation-brief.md](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-gamma-layer-separation-brief.md)
- [3plus1-consensus-2026-05-28-mvp2-gamma.md](/home/delangi/문서/project/category/AI_development_tool/docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md)
- [2026-05-28-mvp2-gamma-codex-response.md](/home/delangi/문서/project/category/AI_development_tool/docs/external-review/2026-05-28-mvp2-gamma-codex-response.md)
- [provider-agnostic-memory-skill-design.md](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/provider-agnostic-memory-skill-design.md)
- [ADR-012-evidence-ledger-protection.md](/home/delangi/문서/project/category/AI_development_tool/docs/decisions/ADR-012-evidence-ledger-protection.md)
- [ADR-011-means-vs-ends-redaction.md](/home/delangi/문서/project/category/AI_development_tool/docs/decisions/ADR-011-means-vs-ends-redaction.md)
- [jsonl_hash_chain.py](/home/delangi/문서/project/category/AI_development_tool/tools/jsonl_hash_chain.py)
- [canonical_json.py](/home/delangi/문서/project/category/AI_development_tool/tools/canonical_json.py)
- `.github/workflows/g4-hash-chain.yml`
- `.github/workflows/history-anchor-verifier.yml`
- `.github/workflows/rewrite-defense.yml`
- `.github/workflows/r2-canary.yml`
- `tests/canonical/`
- `tests/fixtures/jsonl_ledger/`
- `tests/fixtures/history_anchor_verifier/`

**§0 총평**

판정은 **APPROVE WITH CONDITIONS**입니다.

본 brief v1은 “Layer 1+2+4 통합 PASS 발효”가 아니라 “통합 PASS 격상 진입 합의 input”으로는 충분합니다.

Primary brief의 권위 한계가 반복적으로 명시되어 있고, 특히 다음 직접 문구가 핵심입니다.

> “본 cycle 발효 효과 = Layer 1+2+4 통합 PASS 격상 진입 권한 발효”

> “실 구현 + R-6 actual run + PASS 발효 = 별도 sub-cycle”

> “본 brief 자체에서 Layer 1+2+4 통합 PASS 발효 0건”

따라서 entry brief로는 APPROVE 가능합니다.

다만 PASS 발효 시점으로 넘어가기 전에는 조건이 남습니다.

핵심 조건은 Layer 2a `denyNonFastForwards` 활성화, R-6 actual run, R-S1 선행/동시 정정 평가, 그리고 `4 violation_type` 표현의 정밀화입니다.

**§1 BLOCKING 0건**

BLOCKING은 없습니다.

R-1: 없음.

R-2: 없음.

R-3: 없음.

검토 이유는 다음과 같습니다.

본 brief는 아직 실 구현 또는 PASS 발효를 선언하지 않습니다.

Layer 2a 미설정도 brief 내부에서 gap으로 정확히 표시합니다.

R-S1 정정도 “본 cycle 정정 0 / 평가 의무”로 제한합니다.

ADR-011 (a)~(d)+(e)도 “자동 충족”이 아니라 gap 포함 매트릭스로 다룹니다.

따라서 현재 단계의 산출물 성격을 기준으로 blocking 결함은 아닙니다.

**§2 권고 8건**

N-1. `4 violation_type` 표현 정밀화가 필요합니다.

`tools/jsonl_hash_chain.py` enum은 `prev_hash_mismatch`, `hash_recalculation`, `history_rewrite`, `genesis_mismatch` 4종을 선언합니다.

하지만 `tests/fixtures/jsonl_ledger/fail/`와 `g4-hash-chain.yml`의 실제 4 fail fixture는 다음 4개입니다.

- `prev_hash_mismatch`
- `hash_recalculation`
- `schema_missing_field`
- `genesis_mismatch`

즉 workflow의 “4 violation_type cover”는 enum 4종이 아니라 “4 fail pattern cover”에 가깝습니다.

`history_rewrite`는 Layer 2 rewrite-defense 영역으로 분리되어 보입니다.

PASS 발효 전에는 E-PASS-2 문구를 “Layer 1 chain violation 3종 + schema_missing_field + Layer 2 history rewrite 별도”로 정정하는 편이 안전합니다.

N-2. Layer 2b branch protection evidence에 `required_approving_review_count=0`을 명시해야 합니다.

`gh api` 직접 조회 결과 required contexts 8개, force push false, deletion false, admins enforced는 확인됐습니다.

다만 `required_approving_review_count`는 `0`입니다.

brief가 “required_approving_review_count”를 포함 evidence로 요구한다면, PASS evidence에서는 0이 허용 상태인지 별도 해석이 필요합니다.

N-3. 로컬 PoC 실행 전제 의존성 명시가 필요합니다.

현재 기본 shell에서 `python`은 없고 `python3`만 있습니다.

또한 기본 환경에는 `rfc8785`, `jcs`가 없어 scripts는 실패했습니다.

임시 venv에 `rfc8785==0.1.4`, `jcs==0.2.1` 설치 후 실행은 PASS했습니다.

PASS evidence에는 “workflow installs deps”와 “local actual run deps”를 분리해 적는 것이 좋습니다.

N-4. R-S1은 entry brief 단계에서는 평가 의무로 충분하지만, MVP-2 PASS 직전에는 hard gate로 격상해야 합니다.

현재 brief의 RT-γ-6 위치는 적절합니다.

다만 MVP-2 Implementation Evidence PASS 발효 합의에서는 “선행/동시 정정 여부”가 권고가 아니라 사전조건이어야 합니다.

N-5. E-PASS-8의 “42 entry actual run id” 답습은 최신 actual run으로 갱신해야 합니다.

현재 evidence template 후보로는 허용됩니다.

하지만 PASS 발효 evidence에서는 과거 run id 답습만으로 부족합니다.

Layer 1+2+4 통합 PASS 발효 시점의 GitHub Actions run id가 필요합니다.

N-6. Layer 4 evidence에 Layer 1/2 evidence를 포함하지 않는다는 금지는 잘 되어 있으나, 실행 로그명도 layer prefix를 강제하는 편이 좋습니다.

예: `[Layer 1] hash chain`, `[Layer 2a] denyNonFastForwards`, `[Layer 2b] branch protection`, `[Layer 4] CI regression`.

이렇게 해야 RT-PASS-2를 운영에서 판별하기 쉽습니다.

N-7. `denyNonFastForwards` 활성화는 local/global/system 출력 0건으로 직접 확인됐으므로, 실 구현 sub-cycle 첫 step으로 고정하는 것이 적절합니다.

현재 brief가 이를 “별도 verify 의무”로 둔 것은 맞습니다.

다만 sub-cycle 진입 시 가장 먼저 처리해야 합니다.

N-8. `history-anchor-verifier.yml`은 Layer 5 성격 evidence를 포함합니다.

본 cycle scope는 Layer 1+2+4 부분 답습이므로, 이 workflow를 “4 G4 workflows 시제”로 언급할 때 Layer 5 PASS 진입으로 오해되지 않게 제한 문구를 유지해야 합니다.

**§3 NOTE 5건**

NOTE-1. 파일 line count 직접 확인 결과 primary brief는 443줄입니다.

사용자 제공 정보와 일치합니다.

NOTE-2. `tests/canonical/`은 72 files, 8 categories, 각 3 case × 3 files 구조입니다.

직접 확인한 category는 `array`, `escape`, `hash_stability`, `key_ordering`, `lossy`, `nested`, `number`, `unicode`입니다.

NOTE-3. 4 G4 workflows는 모두 존재하고 size도 사용자 제공값과 일치합니다.

`g4-hash-chain.yml` 10652B, `history-anchor-verifier.yml` 19094B, `rewrite-defense.yml` 16454B, `r2-canary.yml` 5476B입니다.

NOTE-4. GitHub branch protection 조회는 성공했습니다.

Required contexts는 `guard`, `verify`, `feasibility`, `scan`, `enforce`, `defense`, `validate`, `bypass-detect` 8개입니다.

NOTE-5. 본 검토는 repo 파일 읽기와 로컬/remote 상태 확인을 직접 수행했습니다.

웹 검색은 필요하지 않았습니다.

**§4 7 기준별 평가**

1. Cross-vendor 충족 명시: PASS.

본 응답 vendor는 OpenAI Codex CLI입니다.

본 cycle 풀 3+1 Agent vendor는 Anthropic Claude입니다.

헌법 5조-2의 cross-vendor blind review 형식은 충족됩니다.

2. 본 brief v1 직접 읽기 evidence: PASS.

Primary brief에서 직접 확인한 핵심 문구는 다음입니다.

> “본 cycle = 큰 cycle”

> “풀 3+1 합의 + 외부 LLM 1+ 응답 입력 (cross-vendor) + 사용자 명시 결정”

> “PASS evidence template 후보 채택”

> “Layer 1+2+4 통합 PASS 발효 0건”

> “R-S1 cross-reference 정정 0건”

이 문구들은 brief가 entry 합의와 PASS 발효를 분리하고 있음을 보여줍니다.

3. (γ-c) 특화 의무 4 답습 정확성: PASS with minor precision condition.

Layer subsection 강제, 부분 답습 framing, 통합 동시, RT-γ-6 모두 primary brief에 반영되어 있습니다.

단 `4 violation_type`의 세부 표현은 PASS 전 정밀화 권고가 있습니다.

4. Layer 1+2+4 각 영역 PoC 시제 충족 자격 평가: PASS WITH CONDITIONS.

Layer 1 hash chain은 임시 venv에서 actual run PASS 확인했습니다.

Layer 2a `denyNonFastForwards`는 local/global/system 모두 미설정입니다.

Layer 2b branch protection은 remote state 확인했습니다.

Layer 4 workflows는 존재 및 내용 확인했습니다.

Canonical corpus 72 files는 cross-check PASS했습니다.

5. ADR-011 §2.1 (a)~(d)+(e) matrix 평가: PASS for entry, not PASS activation.

(a) safety outcome 비교는 충분합니다.

(b) isolated PoC는 Layer 2a에서 아직 gap입니다.

(c) ADR/G4 권위 연결은 충분합니다.

(d) CI regression path는 후보/시제로 충분합니다.

(e) 합의 APPROVE는 본 cycle entry에 한정되며 PASS 발효 합의가 아닙니다.

6. Rollback Trigger / Evidence 후보 평가: PASS WITH CONDITIONS.

RT-γ-1/4/5/6와 RT-PASS-1/2/3 후보는 적절합니다.

E-PASS-1~15도 Layer subsection을 강제합니다.

단 E-PASS-2와 E-PASS-8은 PASS 발효 전에 최신 actual run 및 violation taxonomy 정밀화가 필요합니다.

7. R-S1 후행 영향 RT-γ-6 평가 + MVP-2 PASS 선행/동시 정정 사전조건 평가: PASS.

Brief는 R-S1 정정을 자동 진입시키지 않습니다.

동시에 MVP-2 PASS 시점에는 선행/동시 정정 필요성 평가를 의무화합니다.

이 균형은 53 entry N-5 및 54 entry §1.3 의무 4 답습과 정합합니다.

**§5 (γ-c) 특화 의무 4 답습 정확성 평가**

의무 1. Layer subsection 강제: PASS.

Primary brief §2.5와 §5.2가 Layer 1, Layer 2a, Layer 2b, Layer 4, 통합 evidence subsection을 분리합니다.

특히 “Layer 4 evidence 內 Layer 1+2 evidence 합산 영구 금지” 문구가 명확합니다.

RT-PASS-2도 이 위반을 rollback trigger로 둡니다.

의무 2. “부분 답습” framing 영구: PASS.

Primary brief §2.1은 “G4 §4.4 Layer 1+2+4 통합 부분 답습”이라고 명시합니다.

Layer 3 Signed commit과 Layer 5 External anchor를 scope 외로 둔 점이 정확합니다.

RT-PASS-3도 “완전 답습” 또는 “충실 답습” 표현을 rollback trigger로 둡니다.

의무 3. 통합 동시: PASS.

Primary brief §2.5는 Layer 1+2+4 통합 PASS evidence 동시 발효 의무를 명시합니다.

이는 (γ-a) 단계적 발효와 구분됩니다.

다만 본 cycle은 “통합 PASS 발효”가 아니라 “통합 PASS 격상 진입”입니다.

의무 4. RT-γ-6 평가: PASS.

Primary brief §5.1은 RT-γ-6을 별도 row로 둡니다.

§8 다음 단계에도 R-S1 정정 cycle을 별도로 둡니다.

정정 자체를 자동 발효하지 않는 점이 적절합니다.

**§6 R-S1 RT-γ-6 평가 결과**

R-S1 관련 현재 상태 판정: **entry 단계 PASS, MVP-2 PASS 전 hard gate 필요**.

ADR-012 §2.3은 Layer 4를 External anchor로 서술하는 구 numbering 흔적이 있습니다.

G4 §4.4.1은 Layer 4를 CI 회귀 검증으로 정의합니다.

본 brief는 G4 §4.4.1을 Layer numbering PRIMARY로 두고, ADR-012 §2.3 vs §2.8 정정은 별도 cycle로 미룹니다.

이 판단은 entry brief 단계에서는 적절합니다.

그러나 MVP-2 Implementation Evidence PASS 발효 시점에는 다음 중 하나가 선행 또는 동시로 필요합니다.

- ADR-012 §2.3 본문 정정
- 또는 ADR-012 §2.8 동형 답습 강화 및 cross-reference 명확화
- 또는 “G4 §4.4.1 numbering PRIMARY / ADR-012 §2.3 principle-only” 권위 선언

현재 brief는 이 필요성을 RT-γ-6과 E-PASS-15로 반영합니다.

따라서 R-S1은 blocking이 아니라 후속 PASS 사전조건입니다.

**§7 PoC 시제 5 영역 Cross-check**

1. Layer 1 Hash Chain: PASS as PoC 시제.

직접 실행 결과, 임시 venv 의존성 설치 후 pass fixtures 2개가 PASS했습니다.

`minimal_chain.jsonl`: schema + chain + monotonicity PASS.

`roundtrip_t2_strict.jsonl`: schema + chain + monotonicity PASS.

Fail fixtures도 기대 rc=1로 검출됐습니다.

`genesis_mismatch.jsonl`: `genesis_mismatch`.

`hash_recalculation.jsonl`: `hash_recalculation`.

`missing_event_field.jsonl`: `schema_missing_field`.

`prev_hash_mismatch.jsonl`: `prev_hash_mismatch`.

단 `history_rewrite` enum은 `jsonl_ledger/fail` fixture에서 직접 cover되지 않았습니다.

이 점은 권고 N-1입니다.

2. Layer 2a denyNonFastForwards: GAP correctly disclosed.

직접 확인 결과:

`git config --local --get receive.denyNonFastForwards`: 출력 없음.

`git config --global --get receive.denyNonFastForwards`: 출력 없음.

`git config --system --get receive.denyNonFastForwards`: 출력 없음.

따라서 Layer 2a는 PASS evidence가 아니라 실 구현 sub-cycle 의무입니다.

Brief는 이를 정확히 “미설정”으로 표시합니다.

3. Layer 2b Branch Protection: PASS with precision note.

`gh api repos/jokwangwon/AI_development_tool/branches/main/protection` 직접 조회 결과:

Required contexts 8개 확인.

`allow_force_pushes.enabled=false`.

`allow_deletions.enabled=false`.

`enforce_admins.enabled=true`.

`required_approving_review_count=0`.

따라서 branch protection 시제는 존재합니다.

다만 review count 0의 의미는 PASS evidence에서 명시해야 합니다.

4. Layer 4 4 G4 workflows: PASS as filesystem 시제.

확인한 workflow 4개:

- `.github/workflows/g4-hash-chain.yml`
- `.github/workflows/history-anchor-verifier.yml`
- `.github/workflows/rewrite-defense.yml`
- `.github/workflows/r2-canary.yml`

각 workflow는 hash chain, canonical regression, history anchor, rewrite defense, R-6 canary 경로를 포함합니다.

단 PASS 발효에는 최신 actual GitHub Actions run id가 별도로 필요합니다.

5. Canonical test corpus 72 files: PASS.

직접 count: 72 files.

구조: 8 categories × 3 cases × 3 files.

임시 venv에서 `tools/canonical_json.py --mode cross_check` 전체 실행 PASS.

`rfc8785`와 `jcs` cross-check가 전 case에서 통과했습니다.

**최종 판정**

본 brief v1은 **Layer 1+2+4 통합 PASS 격상 진입 합의 input**으로 승인 가능합니다.

다만 본 승인은 PASS 발효 승인이 아닙니다.

후속 실 구현 sub-cycle과 MVP-2 PASS 발효 전에는 다음 조건이 선행되어야 합니다.

- `denyNonFastForwards` 활성화 및 force-push reject evidence
- R-6 actual run evidence
- 최신 4 G4 workflow actual run PASS evidence
- R-S1 선행/동시 정정 평가
- E-PASS-2 `4 violation_type` 문구 정밀화
- Layer subsection evidence 분리 유지
tokens used
85,389
**검토자 / Vendor**

- 검토자: OpenAI Codex CLI
- 응답 vendor: OpenAI
- 본 cycle 3+1 Agent vendor: Anthropic Claude
- Cross-vendor blind review 조건: 충족
- 판정: **APPROVE WITH CONDITIONS**
- BLOCKING: **0건**
- 권고: **8건**
- NOTE: **5건**

**직접 검토한 Working Directory 자료**

- [mvp2-layer-124-pass-entry-brief.md](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-layer-124-pass-entry-brief.md)
- [mvp2-gamma-decision-brief.md](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-gamma-decision-brief.md)
- [1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md](/home/delangi/문서/project/category/AI_development_tool/docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md)
- [mvp2-gamma-layer-separation-brief.md](/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-gamma-layer-separation-brief.md)
- [3plus1-consensus-2026-05-28-mvp2-gamma.md](/home/delangi/문서/project/category/AI_development_tool/docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md)
- [2026-05-28-mvp2-gamma-codex-response.md](/home/delangi/문서/project/category/AI_development_tool/docs/external-review/2026-05-28-mvp2-gamma-codex-response.md)
- [provider-agnostic-memory-skill-design.md](/home/delangi/문서/project/category/AI_development_tool/docs/architecture/provider-agnostic-memory-skill-design.md)
- [ADR-012-evidence-ledger-protection.md](/home/delangi/문서/project/category/AI_development_tool/docs/decisions/ADR-012-evidence-ledger-protection.md)
- [ADR-011-means-vs-ends-redaction.md](/home/delangi/문서/project/category/AI_development_tool/docs/decisions/ADR-011-means-vs-ends-redaction.md)
- [jsonl_hash_chain.py](/home/delangi/문서/project/category/AI_development_tool/tools/jsonl_hash_chain.py)
- [canonical_json.py](/home/delangi/문서/project/category/AI_development_tool/tools/canonical_json.py)
- `.github/workflows/g4-hash-chain.yml`
- `.github/workflows/history-anchor-verifier.yml`
- `.github/workflows/rewrite-defense.yml`
- `.github/workflows/r2-canary.yml`
- `tests/canonical/`
- `tests/fixtures/jsonl_ledger/`
- `tests/fixtures/history_anchor_verifier/`

**§0 총평**

판정은 **APPROVE WITH CONDITIONS**입니다.

본 brief v1은 “Layer 1+2+4 통합 PASS 발효”가 아니라 “통합 PASS 격상 진입 합의 input”으로는 충분합니다.

Primary brief의 권위 한계가 반복적으로 명시되어 있고, 특히 다음 직접 문구가 핵심입니다.

> “본 cycle 발효 효과 = Layer 1+2+4 통합 PASS 격상 진입 권한 발효”

> “실 구현 + R-6 actual run + PASS 발효 = 별도 sub-cycle”

> “본 brief 자체에서 Layer 1+2+4 통합 PASS 발효 0건”

따라서 entry brief로는 APPROVE 가능합니다.

다만 PASS 발효 시점으로 넘어가기 전에는 조건이 남습니다.

핵심 조건은 Layer 2a `denyNonFastForwards` 활성화, R-6 actual run, R-S1 선행/동시 정정 평가, 그리고 `4 violation_type` 표현의 정밀화입니다.

**§1 BLOCKING 0건**

BLOCKING은 없습니다.

R-1: 없음.

R-2: 없음.

R-3: 없음.

검토 이유는 다음과 같습니다.

본 brief는 아직 실 구현 또는 PASS 발효를 선언하지 않습니다.

Layer 2a 미설정도 brief 내부에서 gap으로 정확히 표시합니다.

R-S1 정정도 “본 cycle 정정 0 / 평가 의무”로 제한합니다.

ADR-011 (a)~(d)+(e)도 “자동 충족”이 아니라 gap 포함 매트릭스로 다룹니다.

따라서 현재 단계의 산출물 성격을 기준으로 blocking 결함은 아닙니다.

**§2 권고 8건**

N-1. `4 violation_type` 표현 정밀화가 필요합니다.

`tools/jsonl_hash_chain.py` enum은 `prev_hash_mismatch`, `hash_recalculation`, `history_rewrite`, `genesis_mismatch` 4종을 선언합니다.

하지만 `tests/fixtures/jsonl_ledger/fail/`와 `g4-hash-chain.yml`의 실제 4 fail fixture는 다음 4개입니다.

- `prev_hash_mismatch`
- `hash_recalculation`
- `schema_missing_field`
- `genesis_mismatch`

즉 workflow의 “4 violation_type cover”는 enum 4종이 아니라 “4 fail pattern cover”에 가깝습니다.

`history_rewrite`는 Layer 2 rewrite-defense 영역으로 분리되어 보입니다.

PASS 발효 전에는 E-PASS-2 문구를 “Layer 1 chain violation 3종 + schema_missing_field + Layer 2 history rewrite 별도”로 정정하는 편이 안전합니다.

N-2. Layer 2b branch protection evidence에 `required_approving_review_count=0`을 명시해야 합니다.

`gh api` 직접 조회 결과 required contexts 8개, force push false, deletion false, admins enforced는 확인됐습니다.

다만 `required_approving_review_count`는 `0`입니다.

brief가 “required_approving_review_count”를 포함 evidence로 요구한다면, PASS evidence에서는 0이 허용 상태인지 별도 해석이 필요합니다.

N-3. 로컬 PoC 실행 전제 의존성 명시가 필요합니다.

현재 기본 shell에서 `python`은 없고 `python3`만 있습니다.

또한 기본 환경에는 `rfc8785`, `jcs`가 없어 scripts는 실패했습니다.

임시 venv에 `rfc8785==0.1.4`, `jcs==0.2.1` 설치 후 실행은 PASS했습니다.

PASS evidence에는 “workflow installs deps”와 “local actual run deps”를 분리해 적는 것이 좋습니다.

N-4. R-S1은 entry brief 단계에서는 평가 의무로 충분하지만, MVP-2 PASS 직전에는 hard gate로 격상해야 합니다.

현재 brief의 RT-γ-6 위치는 적절합니다.

다만 MVP-2 Implementation Evidence PASS 발효 합의에서는 “선행/동시 정정 여부”가 권고가 아니라 사전조건이어야 합니다.

N-5. E-PASS-8의 “42 entry actual run id” 답습은 최신 actual run으로 갱신해야 합니다.

현재 evidence template 후보로는 허용됩니다.

하지만 PASS 발효 evidence에서는 과거 run id 답습만으로 부족합니다.

Layer 1+2+4 통합 PASS 발효 시점의 GitHub Actions run id가 필요합니다.

N-6. Layer 4 evidence에 Layer 1/2 evidence를 포함하지 않는다는 금지는 잘 되어 있으나, 실행 로그명도 layer prefix를 강제하는 편이 좋습니다.

예: `[Layer 1] hash chain`, `[Layer 2a] denyNonFastForwards`, `[Layer 2b] branch protection`, `[Layer 4] CI regression`.

이렇게 해야 RT-PASS-2를 운영에서 판별하기 쉽습니다.

N-7. `denyNonFastForwards` 활성화는 local/global/system 출력 0건으로 직접 확인됐으므로, 실 구현 sub-cycle 첫 step으로 고정하는 것이 적절합니다.

현재 brief가 이를 “별도 verify 의무”로 둔 것은 맞습니다.

다만 sub-cycle 진입 시 가장 먼저 처리해야 합니다.

N-8. `history-anchor-verifier.yml`은 Layer 5 성격 evidence를 포함합니다.

본 cycle scope는 Layer 1+2+4 부분 답습이므로, 이 workflow를 “4 G4 workflows 시제”로 언급할 때 Layer 5 PASS 진입으로 오해되지 않게 제한 문구를 유지해야 합니다.

**§3 NOTE 5건**

NOTE-1. 파일 line count 직접 확인 결과 primary brief는 443줄입니다.

사용자 제공 정보와 일치합니다.

NOTE-2. `tests/canonical/`은 72 files, 8 categories, 각 3 case × 3 files 구조입니다.

직접 확인한 category는 `array`, `escape`, `hash_stability`, `key_ordering`, `lossy`, `nested`, `number`, `unicode`입니다.

NOTE-3. 4 G4 workflows는 모두 존재하고 size도 사용자 제공값과 일치합니다.

`g4-hash-chain.yml` 10652B, `history-anchor-verifier.yml` 19094B, `rewrite-defense.yml` 16454B, `r2-canary.yml` 5476B입니다.

NOTE-4. GitHub branch protection 조회는 성공했습니다.

Required contexts는 `guard`, `verify`, `feasibility`, `scan`, `enforce`, `defense`, `validate`, `bypass-detect` 8개입니다.

NOTE-5. 본 검토는 repo 파일 읽기와 로컬/remote 상태 확인을 직접 수행했습니다.

웹 검색은 필요하지 않았습니다.

**§4 7 기준별 평가**

1. Cross-vendor 충족 명시: PASS.

본 응답 vendor는 OpenAI Codex CLI입니다.

본 cycle 풀 3+1 Agent vendor는 Anthropic Claude입니다.

헌법 5조-2의 cross-vendor blind review 형식은 충족됩니다.

2. 본 brief v1 직접 읽기 evidence: PASS.

Primary brief에서 직접 확인한 핵심 문구는 다음입니다.

> “본 cycle = 큰 cycle”

> “풀 3+1 합의 + 외부 LLM 1+ 응답 입력 (cross-vendor) + 사용자 명시 결정”

> “PASS evidence template 후보 채택”

> “Layer 1+2+4 통합 PASS 발효 0건”

> “R-S1 cross-reference 정정 0건”

이 문구들은 brief가 entry 합의와 PASS 발효를 분리하고 있음을 보여줍니다.

3. (γ-c) 특화 의무 4 답습 정확성: PASS with minor precision condition.

Layer subsection 강제, 부분 답습 framing, 통합 동시, RT-γ-6 모두 primary brief에 반영되어 있습니다.

단 `4 violation_type`의 세부 표현은 PASS 전 정밀화 권고가 있습니다.

4. Layer 1+2+4 각 영역 PoC 시제 충족 자격 평가: PASS WITH CONDITIONS.

Layer 1 hash chain은 임시 venv에서 actual run PASS 확인했습니다.

Layer 2a `denyNonFastForwards`는 local/global/system 모두 미설정입니다.

Layer 2b branch protection은 remote state 확인했습니다.

Layer 4 workflows는 존재 및 내용 확인했습니다.

Canonical corpus 72 files는 cross-check PASS했습니다.

5. ADR-011 §2.1 (a)~(d)+(e) matrix 평가: PASS for entry, not PASS activation.

(a) safety outcome 비교는 충분합니다.

(b) isolated PoC는 Layer 2a에서 아직 gap입니다.

(c) ADR/G4 권위 연결은 충분합니다.

(d) CI regression path는 후보/시제로 충분합니다.

(e) 합의 APPROVE는 본 cycle entry에 한정되며 PASS 발효 합의가 아닙니다.

6. Rollback Trigger / Evidence 후보 평가: PASS WITH CONDITIONS.

RT-γ-1/4/5/6와 RT-PASS-1/2/3 후보는 적절합니다.

E-PASS-1~15도 Layer subsection을 강제합니다.

단 E-PASS-2와 E-PASS-8은 PASS 발효 전에 최신 actual run 및 violation taxonomy 정밀화가 필요합니다.

7. R-S1 후행 영향 RT-γ-6 평가 + MVP-2 PASS 선행/동시 정정 사전조건 평가: PASS.

Brief는 R-S1 정정을 자동 진입시키지 않습니다.

동시에 MVP-2 PASS 시점에는 선행/동시 정정 필요성 평가를 의무화합니다.

이 균형은 53 entry N-5 및 54 entry §1.3 의무 4 답습과 정합합니다.

**§5 (γ-c) 특화 의무 4 답습 정확성 평가**

의무 1. Layer subsection 강제: PASS.

Primary brief §2.5와 §5.2가 Layer 1, Layer 2a, Layer 2b, Layer 4, 통합 evidence subsection을 분리합니다.

특히 “Layer 4 evidence 內 Layer 1+2 evidence 합산 영구 금지” 문구가 명확합니다.

RT-PASS-2도 이 위반을 rollback trigger로 둡니다.

의무 2. “부분 답습” framing 영구: PASS.

Primary brief §2.1은 “G4 §4.4 Layer 1+2+4 통합 부분 답습”이라고 명시합니다.

Layer 3 Signed commit과 Layer 5 External anchor를 scope 외로 둔 점이 정확합니다.

RT-PASS-3도 “완전 답습” 또는 “충실 답습” 표현을 rollback trigger로 둡니다.

의무 3. 통합 동시: PASS.

Primary brief §2.5는 Layer 1+2+4 통합 PASS evidence 동시 발효 의무를 명시합니다.

이는 (γ-a) 단계적 발효와 구분됩니다.

다만 본 cycle은 “통합 PASS 발효”가 아니라 “통합 PASS 격상 진입”입니다.

의무 4. RT-γ-6 평가: PASS.

Primary brief §5.1은 RT-γ-6을 별도 row로 둡니다.

§8 다음 단계에도 R-S1 정정 cycle을 별도로 둡니다.

정정 자체를 자동 발효하지 않는 점이 적절합니다.

**§6 R-S1 RT-γ-6 평가 결과**

R-S1 관련 현재 상태 판정: **entry 단계 PASS, MVP-2 PASS 전 hard gate 필요**.

ADR-012 §2.3은 Layer 4를 External anchor로 서술하는 구 numbering 흔적이 있습니다.

G4 §4.4.1은 Layer 4를 CI 회귀 검증으로 정의합니다.

본 brief는 G4 §4.4.1을 Layer numbering PRIMARY로 두고, ADR-012 §2.3 vs §2.8 정정은 별도 cycle로 미룹니다.

이 판단은 entry brief 단계에서는 적절합니다.

그러나 MVP-2 Implementation Evidence PASS 발효 시점에는 다음 중 하나가 선행 또는 동시로 필요합니다.

- ADR-012 §2.3 본문 정정
- 또는 ADR-012 §2.8 동형 답습 강화 및 cross-reference 명확화
- 또는 “G4 §4.4.1 numbering PRIMARY / ADR-012 §2.3 principle-only” 권위 선언

현재 brief는 이 필요성을 RT-γ-6과 E-PASS-15로 반영합니다.

따라서 R-S1은 blocking이 아니라 후속 PASS 사전조건입니다.

**§7 PoC 시제 5 영역 Cross-check**

1. Layer 1 Hash Chain: PASS as PoC 시제.

직접 실행 결과, 임시 venv 의존성 설치 후 pass fixtures 2개가 PASS했습니다.

`minimal_chain.jsonl`: schema + chain + monotonicity PASS.

`roundtrip_t2_strict.jsonl`: schema + chain + monotonicity PASS.

Fail fixtures도 기대 rc=1로 검출됐습니다.

`genesis_mismatch.jsonl`: `genesis_mismatch`.

`hash_recalculation.jsonl`: `hash_recalculation`.

`missing_event_field.jsonl`: `schema_missing_field`.

`prev_hash_mismatch.jsonl`: `prev_hash_mismatch`.

단 `history_rewrite` enum은 `jsonl_ledger/fail` fixture에서 직접 cover되지 않았습니다.

이 점은 권고 N-1입니다.

2. Layer 2a denyNonFastForwards: GAP correctly disclosed.

직접 확인 결과:

`git config --local --get receive.denyNonFastForwards`: 출력 없음.

`git config --global --get receive.denyNonFastForwards`: 출력 없음.

`git config --system --get receive.denyNonFastForwards`: 출력 없음.

따라서 Layer 2a는 PASS evidence가 아니라 실 구현 sub-cycle 의무입니다.

Brief는 이를 정확히 “미설정”으로 표시합니다.

3. Layer 2b Branch Protection: PASS with precision note.

`gh api repos/jokwangwon/AI_development_tool/branches/main/protection` 직접 조회 결과:

Required contexts 8개 확인.

`allow_force_pushes.enabled=false`.

`allow_deletions.enabled=false`.

`enforce_admins.enabled=true`.

`required_approving_review_count=0`.

따라서 branch protection 시제는 존재합니다.

다만 review count 0의 의미는 PASS evidence에서 명시해야 합니다.

4. Layer 4 4 G4 workflows: PASS as filesystem 시제.

확인한 workflow 4개:

- `.github/workflows/g4-hash-chain.yml`
- `.github/workflows/history-anchor-verifier.yml`
- `.github/workflows/rewrite-defense.yml`
- `.github/workflows/r2-canary.yml`

각 workflow는 hash chain, canonical regression, history anchor, rewrite defense, R-6 canary 경로를 포함합니다.

단 PASS 발효에는 최신 actual GitHub Actions run id가 별도로 필요합니다.

5. Canonical test corpus 72 files: PASS.

직접 count: 72 files.

구조: 8 categories × 3 cases × 3 files.

임시 venv에서 `tools/canonical_json.py --mode cross_check` 전체 실행 PASS.

`rfc8785`와 `jcs` cross-check가 전 case에서 통과했습니다.

**최종 판정**

본 brief v1은 **Layer 1+2+4 통합 PASS 격상 진입 합의 input**으로 승인 가능합니다.

다만 본 승인은 PASS 발효 승인이 아닙니다.

후속 실 구현 sub-cycle과 MVP-2 PASS 발효 전에는 다음 조건이 선행되어야 합니다.

- `denyNonFastForwards` 활성화 및 force-push reject evidence
- R-6 actual run evidence
- 최신 4 G4 workflow actual run PASS evidence
- R-S1 선행/동시 정정 평가
- E-PASS-2 `4 violation_type` 문구 정밀화
- Layer subsection evidence 분리 유지
