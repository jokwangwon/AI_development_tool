# 3+1 합의 — Agent A (구현 분석가) 출력

> **cycle**: (β) sub-수단 결정 entry brief (57 entry)
> **검토 대상**: `docs/phase0/mvp2-beta-submeans-decision-brief.md` (v1)
> **관점**: "실제로 동작하는가?" — 기술적 구현 가능성, 의존성, 성능, **filesystem 직접 inspection**
> **작성**: 2026-05-28 / Agent A (Claude Opus 4.7)
> **방법**: 실 repo filesystem 직접 read + tool 실행 + grep cross-check (편향 방지 — 타 Agent/외부 LLM 미참조)

---

## verdict: **APPROVE WITH CONDITIONS**

본 brief 의 핵심 시제 충족 주장은 **filesystem 직접 verify 결과 대부분 정확**하다. 파일 크기/line 수/count/mode/violation_type/fixture 가 brief 기술과 일치한다. 단, **3건의 과장/부정확** (BLOCKING) 이 발견되었으며, 이는 brief 본문에서 시제 충족 framing 이 *실제 동작 범위* 보다 넓게 서술된 지점이다. 정정 흡수 후 R-4 / L-4 / W 보존우선 수단 결정 권고는 기술적으로 타당하다.

---

## filesystem 직접 verify 결과 (evidence)

### ✅ 정확하게 검증된 주장 (brief 기술 = 실 repo 일치)

| brief 주장 | brief 기술값 | filesystem 실측 | 판정 |
|----------|-----------|---------------|----|
| `secret_scanner.py` 크기 | 16802B | **16802B** (379 line) | ✅ 정확 |
| `secret_scanner.py --mode scan-log` 존재 | 존재 | **line 327 `choices=("scan-source", "scan-log")`** + line 169/186 scan-log 분기 실재 | ✅ 정확 |
| `secret_scanner.py` Tier-1 42 + baseline 5 = 45 patterns | 45 | **`ALL_PATTERNS` = 5 baseline + 31 prefix + 7 regex + 2 alternation = 45** (line 169 docstring), `--list-patterns` 실행 시 T1-042 까지 출력 확인 | ✅ 정확 |
| `jsonl_hash_chain.py` 크기 | 14038B | **14038B** (397 line) | ✅ 정확 |
| `jsonl_hash_chain.py` genesis | 존재 | **`compute_genesis_hash()` line 85, `sha256("genesis:<scope>:<schema_version>")`** | ✅ 정확 |
| `jsonl_hash_chain.py` violation_type 4종 | prev_hash_mismatch / hash_recalculation / history_rewrite / genesis_mismatch | **enum `ViolationType` line 66~72 = 정확히 4개 정의** | ✅ enum 정의 정확 (단 emission 은 R-A-1 참조) |
| `canonical_json.py` 크기 | 10055B | **10055B** (282 line) | ✅ 정확 |
| `canonical_json.py` rfc8785 + jcs + jq fallback + cross-check | 4 경로 | **rfc8785 (line 34) + jcs (line 39) + jq -S -c subprocess fallback (line 94~100) + CROSS_CHECK mode (line 55)** 모두 실재 | ✅ 정확 |
| `tests/canonical/` 72 files / 8 카테고리 | 72 / 8 | **`find tests/canonical -type f \| wc -l` = 72** / 8 dir (array, escape, hash_stability, key_ordering, lossy, nested, number, unicode), 각 3 case × (input.json + expected.canonical + expected.sha256) = 8×3×3 = 72 | ✅ **정확** |
| `secret-hygiene-egress-redaction.yml` 크기 | 51791B | **51791B** | ✅ 정확 |
| `g4-hash-chain.yml` 크기 | 10652B | **10652B** | ✅ 정확 |
| `history-anchor-verifier.yml` 크기 | 19094B | **19094B** | ✅ 정확 |
| `rewrite-defense.yml` 크기 | 16454B | **16454B** | ✅ 정확 |
| `r2-canary.yml` 존재 | 존재 | **5476B 실재** | ✅ 정확 |
| `src/adapters/llm/facade.py` = placeholder | placeholder | **line 4 "현 시점은 placeholder", line 38 `raise NotImplementedError("Placeholder — TR-1 풀 3+1 합의 후 real 본문 작성")`** (1390B) | ✅ 정확 |
| `agent/redact.py` 본 repo 부재 (R-1) | 부재 | **`agent/` 디렉터리 자체 부재** (ls 실패 확인) | ✅ 정확 |
| denyNonFastForwards 미설정 | local + global 0건 | **`git config receive.denyNonFastForwards` local exit=1 + global exit=1 (양쪽 unset)** | ✅ 정확 |
| W "보존 우선" — 실 repo workflow 분리 운영 | 5+ 분리 운영 | **`.github/workflows/` 실측 12개 workflow** (5 G4/GP-2 관련 + 7 추가) — 분리 운영 사실 정확 | ✅ 정확 (오히려 brief 의 "5+" 보다 더 많음) |

→ **secret_scanner.py / jsonl_hash_chain.py / canonical_json.py 모두 실제 실행 가능 확인** (`--list-patterns`, `--help` 정상 출력, syntax/import 오류 0). 시제 = "동작하는 코드" 임이 입증됨.

---

## BLOCKING findings

### R-A-1 (BLOCKING): violation_type 4종 中 `history_rewrite` 는 **정의만 존재, 실제 emission 0** — brief §1.2/§2.1 "4 violation_type 시제 충족" framing 이 *동작 범위* 를 과장

**근거 (filesystem 직접)**:
- `ViolationType` enum (line 66~72) 은 4개 값을 *정의* 한다: `PREV_HASH_MISMATCH` / `HASH_RECALCULATION` / `HISTORY_REWRITE` / `GENESIS_MISMATCH`.
- 그러나 `validate_chain()` (line 165~239) 이 실제 *생성(emit)* 하는 `Violation` 은 **3종뿐**: `GENESIS_MISMATCH` (line 204), `PREV_HASH_MISMATCH` (line 214), `HASH_RECALCULATION` (line 191). **`HISTORY_REWRITE.value` 를 Violation 으로 할당하는 코드 경로가 단 1곳도 없다** (grep 결과 line 18 docstring / line 71 enum 정의 / line 254 *주석* 만 — 실 할당 0).
- `g4-hash-chain.yml` 의 "FAIL fixture — 4 violation_type cover" step (line 197~226) 이 실제 검증하는 4개는 `prev_hash_mismatch` / `hash_recalculation` / **`schema_missing_field`** / `genesis_mismatch` (line 201~206 `EXPECTED` 배열). **즉 "4 violation_type cover" 의 4번째는 `history_rewrite` 가 아니라 `schema_missing_field`** 다.
- `tests/fixtures/jsonl_ledger/fail/` 실측 = `genesis_mismatch.jsonl` / `hash_recalculation.jsonl` / `missing_event_field.jsonl` / `prev_hash_mismatch.jsonl` — **`history_rewrite` fixture 부재 확인**.

**문제**: brief §1.2 표 ("genesis + 4 violation_type") + §2.1 표 R-3/L-1 행 ("genesis + 4 violation_type ... 시제 충족") 은 독자에게 "history_rewrite 검출이 동작한다"고 읽히게 한다. 실제로는 `HISTORY_REWRITE` 는 **dead enum** (정의되었으나 도달 불가). 이는 brief §7.1 조건 5 ("history_rewrite enum fixture 추가" = 실 구현 sub-cycle) 와 **자기모순**: 한편으로 "시제 충족" 이라 하고, 다른 편으로 "fixture 추가 필요" 라 한다.

**정정 방향**: §1.2 + §2.1 의 "4 violation_type 시제 충족" 을 **"3 violation_type 실 emission 충족 (genesis_mismatch / prev_hash_mismatch / hash_recalculation) + schema/monotonicity 위반 검출 + `history_rewrite` enum 정의만 존재 (emission 경로 + fixture = 조건 5 실 구현 sub-cycle 영역)"** 로 정정. §7.1 조건 5 와 정합. (이는 "수단 결정" 자체를 바꾸지 않음 — L-4 채택은 유효하되, 시제 *완성도* 를 정직하게 서술하는 정정.)

---

### R-A-2 (BLOCKING): L-4 "stdlib 단독 / 외부 의존 0 / 즉시 PASS 격상" 주장과 **g4-hash-chain.yml CI 가 rfc8785+jcs 를 *강제 설치/실행* 하는 현 운영** 사이 tension — "즉시 PASS 격상 가능" 의 의존성 0 주장이 부정확

**근거 (filesystem 직접)**:
- brief §3.2 #1 + §3.3 + §5.1 L 행: "**외부 의존 0** / stdlib 단독 / **즉시 PASS 격상**". §1.2 핵심 함의: "L-1 (stdlib hash chain) ... 이미 충족".
- 그러나 `g4-hash-chain.yml` 실측 (line 64~69): **`pip install rfc8785==0.1.4 jcs==0.2.1`** 를 *무조건* 설치하고, line 69 에서 import 검증 (`python -c "import rfc8785, jcs"`)을 한다. 후속 corpus regression step (line 71~164) 은 `--mode primary_1_only` (rfc8785), `--mode primary_2_only` (jcs), `--mode cross_check` (rfc8785+jcs 동시) 를 실행한다. **현 CI workflow 는 순수 stdlib `FALLBACK_JQ` 경로를 *전혀 실행하지 않는다***.
- 즉, **현재 운영 중인 Layer 1 CI (g4-hash-chain.yml) 는 사실상 L-2/L-5 (외부 library JCS Primary) 형태로 동작 중**이다. brief 가 권고하는 L-4 (stdlib 단독) 형태가 *즉시 PASS 격상* 되려면, g4-hash-chain.yml 이 (a) 외부 library 설치를 유지하면서 그것을 PASS gating 으로 쓰거나, (b) FALLBACK_JQ stdlib 경로를 PASS gating 으로 전환해야 한다 — **둘 중 어느 것도 "현 시제 그대로 즉시 격상" 이 아니다**.

**문제**: brief 는 L-4 (stdlib, 외부 의존 0) 를 "이미 시제 충족 → 즉시 격상" 으로 서술하지만, *실 CI 운영* 은 외부 의존 (rfc8785+jcs) 에 기반한다. canonical_json.py *코드* 가 fallback 경로를 가진 것은 사실이나 (R-A-2 와 무관하게 ✅ 정확), **CI workflow 가 그 fallback 경로를 gating 으로 사용하지 않으므로** "외부 의존 0 으로 즉시 PASS 격상" 은 현 시제와 불일치다.

**정정 방향**: §3.2/§3.3/§5.1 에 다음 중 1 명시 — (1) "L-4 = canonical_json.py *코드* 는 stdlib fallback 보유, 단 g4-hash-chain.yml CI 는 현재 rfc8785+jcs 설치/실행 (사실상 L-5 형태 운영). L-4 즉시 격상 = CI 의 외부 library 설치 유지 하에 stdlib 동등성을 corpus 로 입증하는 형태이며, 외부 library *강제 의존 제거* 는 실 구현 sub-cycle 영역" 으로 의존성 현실 정직 서술. 또는 (2) L-4 의 "외부 의존 0" 을 "외부 library *강제 의존* 0 (fallback 경로 보장)" 로 한정하되 "현 CI 운영은 Primary library 사용" 임을 병기. — **수단 결정 (L-4 채택) 은 유효** 하나 의존성 0 framing 의 정밀화 필수.

---

### R-A-3 (BLOCKING): 조건부 승인 조건 6 §7.1 수단 매핑 中 **조건 3 "4 G4 workflow actual run PASS" 의 workflow 집합이 부정확** + 조건 2 (R-6 actual run) 의 수단 (r2-canary.yml) 매핑 불충분

**근거 (filesystem 직접)**:
- brief §1.2 + task 지시문 + §7.1 = "4 G4 workflow" = g4-hash-chain + history-anchor-verifier + rewrite-defense + r2-canary. 그러나 실측 `.github/workflows/` 에는 GP-2/G4 관련만 **5개** (위 4 + `secret-hygiene-egress-redaction.yml`). brief §1.2 표 "Layer 4 CI step" 행은 "4 G4 workflow 분리 운영" 이라 하면서 secret-hygiene 을 별도 (R-3) 로 분류 — 일관성은 있으나, §7.1 조건 3 ("4 G4 workflow actual run PASS") 과 조건 2 ("R-6 actual run = r2-canary.yml") 가 **secret-hygiene-egress-redaction.yml (R-3 = R 영역 핵심 gating) 의 actual run 을 조건 목록에서 누락**한다.
- R-3 (secret-hygiene) 가 GP-2 PASS 의 (d) 자동 회귀 핵심 수단인데 (brief §2.2 #1), §7.1 조건 표에 **R-3 actual run 이 명시적 조건으로 부재** (§7.3 Evidence 에는 "R-3 actual run PASS" 가 있으나 §7.1 조건 6 표에는 누락). 조건 2 의 "R-6 actual run" 이 r2-canary.yml 을 가리키는데, r2-canary 는 R-2 facade canary 영역이지 R-3 (secret 잔존 검출) 영역이 아님 — 수단 매핑 모호.

**문제**: 실 구현 sub-cycle 의 입력 (조건부 승인 조건 6) 이 R-3 (가장 핵심적인 즉시 격상 수단) 의 actual run gating 을 조건 표에서 빠뜨려, 실 구현 sub-cycle 이 R-3 PASS 없이 진행될 빈틈을 남긴다.

**정정 방향**: §7.1 조건 표에 "R-3 (secret-hygiene-egress-redaction.yml) scan-log redaction_pass/fail actual run PASS" 를 명시 조건으로 추가 (또는 조건 2 를 "R-6 (r2-canary) + R-3 (secret-hygiene) actual run PASS" 로 확장). 5개 GP-2/G4 workflow (R-3 + 4 G4) 전부를 조건에 매핑.

---

## 권고 (non-blocking)

### N-A-1: brief §1.2 표 "Layer 2 history" 행 — history-anchor-verifier.yml = Layer 5 (External anchor) PoC 시제임을 명확히
§4.3 에서 "history-anchor-verifier.yml = Layer 5 External anchor PoC 시제 *이미 운영*" 이라 정확히 인정하나, §1.2 표는 이를 "Layer 2 history" 로만 분류한다. (γ-c) 의무 2 ("부분 답습 framing", Layer 3+5 = scope 외) 와의 정합을 위해, §1.2 표에 "history-anchor-verifier 는 Layer 2 + Layer 5 PoC 시제 겸함 (보존 = PoC 시제 보존, Layer 5 결정 영역 진입 0)" 병기 권고. (BLOCKING 아님 — §4.3 에 이미 면책 서술 존재.)

### N-A-2: §2.2 "R-3 단독으로 (d) 자동 회귀 충족이 충분" 주장 — base64 known limitation 의 (d) 충족 범위 한정 명시
secret-hygiene-egress-redaction.yml 실측 (line 205~212) 은 `base64_evasion.txt` 를 **의도적 미검출 (known limitation)** 로 처리한다 (`::warning::` 만, rc 영향 0). 따라서 R-3 의 "(d) 자동 회귀 충족" 은 **평문 + prefix/regex/alternation 패턴 한정** 이며 base64/URL-encoded/압축 evasion 은 미포함 (R-5 = 영구 분리). brief 가 이미 R-5 분리를 명시하므로 모순은 아니나, §2.2 #1 "R-3 가 단독 충족" 에 "(평문/패턴 layer 한정, base64 evasion = R-5 영구 분리)" 를 병기하면 (d) 충족 범위 오해 방지. (RT-R-1/RT-R-2 trigger 와 정합.)

### N-A-3: W 결정 "5+ workflow" → 실측 12개 명시
brief §4.1/§4.2 는 "5+ workflow" 라 하나 실측 `.github/workflows/` = **12개** (boundary-guard, evidence-pass-gate, g4-hash-chain, history-anchor-verifier, memory-skill-migration-feasibility, pre-commit-bypass-detection, provider-adapter-enforcement, provider-url-scanner, r2-canary, rewrite-defense, schema-validation, secret-hygiene-egress-redaction). W "보존 우선 / 신규 통합 0" 권고는 12개 분산 운영 현실에서 *더욱* 타당 (W-A(i) 일괄 통합의 파괴 규모가 brief 가정보다 큼). 정확한 숫자 (12) 로 갱신 권고 — W 결정 강화.

### N-A-4: §7.1 조건 4 "violation_type 정밀화" 와 조건 5 "history_rewrite enum fixture 추가" 통합 정리
R-A-1 정정과 연동 — 조건 4 (violation_type 정밀화) 의 실체가 곧 조건 5 (history_rewrite emission 경로 + fixture) 임을 명시하여 두 조건의 중복/관계를 정리. `HISTORY_REWRITE` 를 어느 검출 경로 (예: history-anchor-verifier 의 anchor mismatch ↔ jsonl_hash_chain 의 prev_hash chain 단절 구분) 에서 emit 할지 = 실 구현 sub-cycle 의 구체 task 로 명문화.

---

## NOTE / 누락 영역 (NT-A-N)

### NT-A-1: 성능/scale 영역 미평가 (brief scope 외이나 실 구현 sub-cycle 입력 권고)
구현 분석가 관점에서 — jsonl_hash_chain.py 의 `validate_chain` 은 ledger 전체를 메모리 list 로 로드 (`entries: list[dict]`) 후 O(n) 순회한다. MVP 단계 ledger 규모에서는 무관하나, ledger 가 수만 entry 로 성장 시 CI step 의 메모리/시간 특성 = 실 구현 sub-cycle 에서 evidence 수집 권고. brief 는 성능 영역을 전혀 다루지 않음 (수단 결정 cycle 특성상 정당하나, NOTE 로 기록).

### NT-A-2: canonical_json.py cross_check mismatch 시 거동 = TR-C-2 escalation — CI gating 영향 미서술
canonical_json.py 는 `CrossCheckMismatchError` (line 64) 를 정의하고 cross_check mode 에서 rfc8785 ↔ jcs 출력 불일치 시 raise 한다. g4-hash-chain.yml 이 `--mode cross_check` 를 corpus 에 실행 (line 129) 하므로, 외부 library 2개 (rfc8785 0.1.4 / jcs 0.2.1) 버전 drift 가 발생하면 CI 가 fail 한다. 이는 **Provider Liquidity 와 무관한 외부 library 의존성 risk** 로, brief §3.2 #3 "외부 library 강제 의존 0" 주장 (R-A-2) 과 직결되는 운영 risk. RT-L-2 (RFC 8785 reference corpus mismatch) 와 별개로 *library 버전 drift* trigger 를 Rollback Trigger 에 추가 검토 권고.

### NT-A-3: R-1/R-2 cross-trajectory 의존이 GP-2 MVP-2 PASS 를 차단하는가? — **차단하지 않음 (R-3 단독으로 (d) 충족 충분, 단 ADR-011 §2.3 #2 MANDATORY 정합은 부분)**
task 추가 분석 질문에 대한 구현 분석가 판정:
- **(d) 자동 회귀 검증 경로**: R-3 (secret-hygiene scan-log) 가 *단독으로* 자동 회귀 검증을 충족한다 (workflow actual run 시). 이 경로는 R-1 (Hermes upstream) / R-2 (facade real) 에 의존하지 않는다 — **GP-2 의 (d) 조건은 R-3 단독으로 차단 없이 충족 가능**.
- **단, ADR-011 §2.3 #2 의 R-1 MANDATORY (Hermes native redaction = 송신 직전 결과 의무)** 는 R-3 (CI 회귀) 만으로 충족되지 않는다. R-3 는 "redaction 후 잔존 검출" (사후 센서) 이지 "송신 직전 redaction 수행" (능동 means) 이 아니다. facade 가 placeholder (NotImplementedError) 인 현 시점, **실제 송신 경로의 능동 redaction 은 0** 이다. 따라서 GP-2 의 *ends* (secret 송신 0) 의 *능동 보장* 은 R-1/R-2 trajectory 발효 전까지 미충족 — R-3 는 "leak 발생 시 검출" 만 보장.
- **결론**: R-3 는 GP-2 MVP-2 PASS 의 (d) 회귀 검증을 차단 없이 충족하나, GP-2 의 *완전한* defense-in-depth ends (능동 송신 redaction) 는 R-1/R-2 에 부분 종속. brief §2.3 trade-off 표 + RT-R-2 가 이를 정직하게 인정함 (✅). **MVP-2 PASS 를 R-3 단독 (d) 충족으로 선언하되, "능동 redaction means (R-1/R-2) = carry-over" 를 PASS evidence 에 명시** 하는 것이 정합 — 이는 brief 권고와 일치. **R-A-1/R-A-2/R-A-3 정정 후 R-4 채택 = 기술적 타당**.

### NT-A-4: 본 검토는 시제 *존재/동작* 검증 한정 — 시제 *정확성* (예: 45 patterns 의 FP/FN율, canonical 72 corpus 의 RFC 8785 strict 동등성 실측) 은 미검증
파일 실행 (`--list-patterns`, `--help`) 으로 syntax/import 정상은 확인했으나, 실제 secret 검출 정확도 / canonical 출력의 RFC 8785 byte-level 정합성 actual run 은 본 검토 범위 밖 (실 구현 sub-cycle 의 actual run evidence 영역). brief §3.2 "corpus 72 files 로 동등성 검증" 주장의 *동등성 결과* 는 미verify (corpus 파일 존재 = ✅, 동등성 PASS = 실 구현 sub-cycle).

---

## 종합

| 영역 | Agent A 판정 |
|------|-----------|
| 시제 존재/동작 주장 (파일 크기/line/count/mode/enum 정의/fixture) | **대부분 정확** (✅ 17건 검증) |
| `history_rewrite` 4번째 violation_type 시제 충족 | ⚠️ **과장** (R-A-1, enum 정의만 / emission+fixture 0) |
| L-4 "외부 의존 0 / 즉시 PASS 격상" | ⚠️ **부정확** (R-A-2, 현 CI 는 rfc8785+jcs 강제 설치/실행) |
| 조건부 승인 조건 6 수단 매핑 | ⚠️ **R-3 actual run 누락** (R-A-3) |
| R-4 / L-4 / W 보존우선 수단 결정 권고 자체 | **정정 후 타당** (NT-A-3 분석 지지) |

R-4 / L-4 / W 보존우선 = 채택 권고에 동의하나, **3건 BLOCKING (시제 framing 정직성 정정) 흡수 조건부**. 정정은 모두 "수단 결정 변경" 이 아니라 "시제 완성도/의존성 현실의 정직한 서술" 이므로, v1.1 1pass 흡수 가능.

---

**verdict: APPROVE WITH CONDITIONS / BLOCKING 3건 (R-A-1 history_rewrite dead enum, R-A-2 L-4 외부 의존 0 부정확, R-A-3 R-3 actual run 조건 누락) / 권고 4 (N-A-1~4) / NOTE 4 (NT-A-1~4)**
