# 3+1 합의 — Agent C (대안 탐색가) 독립 분석

> **cycle**: (β) sub-수단 결정 entry brief (57 entry)
> **검토 대상**: `docs/phase0/mvp2-beta-submeans-decision-brief.md` (v1)
> **관점**: "더 나은 방법이 있는가?" — 대안 기술, 트레이드오프, brief 가 놓친 대안
> **작성**: 2026-05-28 (Agent C, 독립 분석 — A/B/외부 LLM 미참조)
> **방법**: brief 4종(57/51/52/55) read + 실 repo PoC 시제 직접 verify (filesystem + 실행)

---

## verdict

**REVISE**

근거 요약: 본 brief 는 R/L/W 결정 framing 의 *방향*(R-4 / L-4 / W 보존우선)은 means-vs-ends + 비례성 측면에서 합리적이다. 그러나 **L sub-수단 분류가 실 repo 시제와 정면 충돌**한다. brief 는 "L-1 (stdlib 단독) 시제 충족 / 외부 library 강제 의존 0" 을 L 결정의 핵심 근거로 삼으나, 실 PoC 시제(`jsonl_hash_chain.py` + `g4-hash-chain.yml`)는 **stdlib 단독이 아니라 rfc8785+jcs 외부 library 를 Primary 로 *강제 의존*** 한다. 이는 brief 가 채택을 권고하는 후보(L-4=stdlib)와 실제로 PASS 격상되는 시제(L-2/L-5=외부 library Primary)의 *동일성 주장* 이 거짓이라는 의미다 — 즉 brief 가 "더 정확한 대안 분류"(L-1 ≠ 현 시제, 현 시제 = L-2 계열)를 놓쳤다. 이 오분류는 "외부 library 도입 = 별도 cycle" 라는 §0.2 #8 금지선을 *이미 위반한 시제* 를 L-1 으로 세탁(launder)하는 효과가 있어 BLOCKING 이다. R/W 영역은 권고 수준 수정으로 충분.

---

## BLOCKING findings

### R-C-1 (BLOCKING) — L-1 "stdlib 단독 / 외부 의존 0" 분류가 실 시제와 거짓 (대안 분류 누락)

**근거 (filesystem + 실행 직접 verify)**:

1. `tools/jsonl_hash_chain.py` line 99 — `compute_entry_hash()` 가 canonical 생성 시 **`mode=CrossCheckMode.PRIMARY_1_ONLY` 를 하드코딩**:
   ```python
   result = to_canonical(payload, mode=CrossCheckMode.PRIMARY_1_ONLY)
   ```
   `PRIMARY_1_ONLY` = `_to_canonical_rfc8785()` (canonical_json.py line 78~83) = **rfc8785 외부 library 호출**. `json.dumps(sort_keys, separators)` 는 *전혀 호출되지 않는다*.

2. `canonical_json.py` line 80~81 — rfc8785 미설치 시 **즉시 `CanonicalizationError` 를 raise** (자동 jq fallback 으로 떨어지지 *않음*). FALLBACK_JQ 는 caller 가 *명시적으로* mode 를 선택해야만 동작하는 별도 경로이며, hash chain 은 이를 선택하지 않는다.

3. **실행 verify** (rfc8785/jcs 미설치 현 환경):
   ```
   $ python3 jsonl_hash_chain.py /tmp/test_ledger.jsonl
   FAIL: ... type=schema_canonical_error
   detail: canonical_json failed: rfc8785 라이브러리 미설치
   ```
   → 외부 library 미설치 시 hash chain 검증이 **100% 실패**. stdlib 로 *전혀 degrade 되지 않는다*.

4. `.github/workflows/g4-hash-chain.yml` line 68 — CI 가 **`pip install rfc8785==0.1.4 jcs==0.2.1` 를 명시적으로 실행**하고 line 69 에서 import 강제 검증. 즉 PASS 격상 시제는 외부 library 2개를 *전제* 한다.

**brief 의 충돌 주장**:
- §1.2 line 93: "L-1 (stdlib) 시제 충족" + "canonical_json.py fallback"
- §3.2 #1: "L-1 (stdlib hash chain) = 외부 의존성 0"
- §3.3: "L-4(권고) ... 외부 의존 0"
- §3.2 #3 + §5.2: "외부 library *강제 의존* 0"
- §5.1 매트릭스: "L → L-4 ... cross-trajectory 의존 *없음*"

이 5개 진술은 모두 **거짓**이다. 현 시제는 외부 library 를 *강제 의존* 하며, 그 의존이 없으면 검증이 실패한다.

**대안 탐색가 관점 — brief 가 놓친 정확한 분류**:
- 실 시제 = **L-2/L-5 계열** (RFC 8785 JCS Primary via 외부 library), L-1 (stdlib) 이 *아니다*.
- brief 가 권고하는 L-4(L-1+L-3, stdlib) 를 진짜로 채택하려면 `jsonl_hash_chain.py` line 99 를 `PRIMARY_1_ONLY` → stdlib canonicalizer 로 *변경* 해야 한다 — 이는 실 구현 sub-cycle 의 비자명한 작업이며 "시제 충족" 이 아니다.
- 또는 현 시제를 그대로 PASS 격상하려면 이것이 **L-2/L-5 (외부 library Primary) 결정** 임을 정직하게 인정해야 하고, 그러면 §0.2 #8 "외부 library 도입 = 별도 cycle" 와 §8 금지선이 *이미 발효된 시제* 에 의해 충돌한다.

**정정 (REVISE 요구)**:
1. §1.2 / §3.1 / §3.2 / §3.3 / §5.1 의 "L-1 stdlib 시제 충족 / 외부 의존 0" 표현을 전면 정정. 실 시제 = **rfc8785+jcs Primary (L-2 계열)** 임을 명시.
2. 다음 중 하나를 *명시적 결정 경로* 로 분기:
   - **(경로 A) 현 시제 그대로 PASS 격상** → 본 cycle 이 사실상 **L-5 (또는 L-2) 결정** 임을 인정 + 외부 library 2개(rfc8785, jcs)가 `g4-hash-chain.yml` 에서 *이미 의존성으로 발효 중* 임을 ADR-012 §2.1(의존성 추가 PoC 재실행 trigger) 관점에서 사후 정합 처리.
   - **(경로 B) 진짜 L-1(stdlib) 채택** → `jsonl_hash_chain.py` line 99 의 `PRIMARY_1_ONLY` 하드코딩을 stdlib canonicalizer 로 교체하는 것이 실 구현 sub-cycle 작업임을 명시 (= "시제 충족" 주장 철회).
3. RT-L-2 ("fallback 동등성 실패") 정정: 현 시제는 fallback 으로 degrade 하지 않고 *즉시 fail* 하므로, 실제 trigger 는 "외부 library 미설치 시 검증 불능" 이다. corpus 72 files 동등성은 fallback 을 보호하지 못한다 (fallback 이 런타임 경로가 아니므로).

---

### R-C-2 (BLOCKING) — W "보존 우선 = W-A(ii) 변형" 명칭 분류가 부정확 (W-F 신규 정의 또는 W-B 재분류 필요)

**근거**:

1. **실 repo workflow 실측 = 12개** (`ls .github/workflows/`):
   boundary-guard / evidence-pass-gate / **g4-hash-chain** / **history-anchor-verifier** / memory-skill-migration-feasibility / pre-commit-bypass-detection / provider-adapter-enforcement / provider-url-scanner / **r2-canary** / **rewrite-defense** / schema-validation / **secret-hygiene-egress-redaction**. brief §1.2/§4.1 이 "5+ workflow" 로 셈하나 G4+GP-2 관련만 추려도 5개이고 전체는 12개 — "5+" 표현은 맞으나 통합 가능성 판단의 기준 모집단을 흐린다.

2. **W-A(ii) 정의 (52 entry §2.3.2 + 51 §4.2)** = "단일 R-6 확장 (GP-2 + G4 §4.4 Layer 4 *통합*)" 의 sub-옵션 = "보존 + *중복 step 추가*". 즉 W-A 의 본질은 **단일 workflow 로 통합** 이다. 그러나 본 brief §4.2 권고의 실질은:
   - 신규 통합 workflow 생성 **0**
   - 기존 분산 workflow **보존**
   - 누락 step 만 *기존 분산 workflow 內* 보강

   이것은 W-A(통합)의 정신과 *정반대* — **분산 구조를 유지** 하는 것이며, 분류상 **W-B(분리/별도 운영)에 더 가깝거나**, 정확히는 어느 기존 후보에도 없는 **신규 대안(= W-F: 기존 분산 구조 minimal 보존, 신규 workflow 0)** 이다.

3. brief 스스로 §4.2 line 200 에서 "명칭상 W-A(ii) 채택이나 실질 = 보존 우선 minimal" 이라고 자인한다 — 이는 *명칭과 실질의 불일치를 인정하면서 명칭을 유지* 하는 것으로, 후속 cycle / 외부 LLM / 사용자에게 명칭 혼선 risk 를 전가한다. ceremony-inflation 차단 원칙과는 별개로, **결정의 추적가능성(traceability)** 을 훼손한다.

**대안 탐색가 관점**:
- W-A 는 "통합", W-B 는 "분리 신설", 현 권고는 "분리 *보존* (신설 0)". 이 셋은 서로 다른 축이다 — brief 가 W-B 를 "기존과 중복 *신설*" 로만 좁게 해석해 비권고 처리했으나, "신설 없이 기존 분산 보존" 은 W-B 의 단점(중복 신설)을 *회피* 하면서 분리의 장점(실패 영역 식별 즉시)을 취하는 *제3의 위치* 다.

**정정 (REVISE 요구)**:
- 권고를 **W-F (신규): "기존 분산 workflow 보존 + 신규 통합/신설 0 + 누락 step 만 기존 workflow 內 보강"** 로 명시적으로 *재명명* 하거나, 최소한 §4.1 후보표에 이 위치를 신규 행으로 추가. "W-A(ii) 변형" 표기를 철회.
- W 5 대안(W-A~E) 의 분류 축이 (통합 vs 분리) 단일 축이 아니라 (통합/분리) × (신설/보존) 2축임을 §4.1 에 명시 → 향후 명칭 혼선 차단.

---

## 권고 (N-C-N)

### N-C-1 — R-3 단독 + R-1/R-2 deferred 대안의 비례성 재평가 (R-4 defense-in-depth 과잉 검토)

brief §2.3 은 "R-3 단독 = defense-in-depth 약화 (ADR-011 §2.3 #2 R-1 MANDATORY 미충족 risk)" 로 R-3 단독을 격하한다. 그러나 대안 탐색가 관점에서:
- R-1(Hermes upstream) + R-2(facade real) 는 **본 repo 외 trajectory 의존** (R-1=upstream PR, R-2=TR-1 carry-over). 이 둘은 본 cycle 에서 *결정도 구현도 불가* 하다.
- 따라서 "R-4 채택" 의 실질 = "R-3 즉시 발효 + R-1/R-2 는 언젠가" 이며, 이는 **R-3 단독 + R-1/R-2 deferred 명시** 와 *실질적으로 동일* 하다. 차이는 framing 뿐.
- 1인 개발자 비례 보안 관점에서, R-1 을 "MANDATORY 결과 의무" 로 *결정* 하면서 구현은 무기한 deferred 하는 것보다, **R-3 = MVP-2 PASS 단일 gating + R-1/R-2 = 후보(deferred, MANDATORY 재평가는 Hermes import cycle 시점)** 로 두는 것이 means-vs-ends(ends=secret leak 0)에 더 정직하다. R-3(CI log canary)는 송신·로그 경로 leak 을 *결과적으로* 차단하는 ends 충족 수단이며, R-1 의 "송신 직전 redaction" 은 동일 ends 의 *다른 means* 일 뿐이다 (ADR-011 §2.1 (a) 동등 결과).

→ R-4 와 "R-3 단독 + R-1/R-2 deferred" 가 실질 동형임을 §2.3 에 명시하고, 사용자가 framing 을 선택하게 할 것. 어느 쪽이든 즉시 발효 가능 means = R-3 단독으로 동일.

### N-C-2 — L-1.5 중간 대안 정식 식별 (canonical_json.py 조건부 구조 활용)

R-C-1 의 경로 분기와 별개로, `canonical_json.py` 가 이미 `try: import rfc8785 ... except ImportError: rfc8785 = None` 조건부 구조 + 4개 mode(PRIMARY_1/2, CROSS_CHECK, FALLBACK_JQ)를 갖추고 있으므로, **L-1.5 = "stdlib canonicalizer 를 4번째 Primary 옵션으로 추가 + 미설치 시 자동 stdlib degrade"** 가 자연스러운 중간 대안이다 (52 brief §2.2.4 가 "L-1.5 alternative" 를 이미 언급했으나 본 brief 가 누락). 이는:
- 외부 library 미설치 환경(현 상태)에서도 검증이 동작 (현 시제의 hard fail 회피)
- corpus 72 files 로 stdlib ↔ rfc8785 동등성 검증
- Provider Liquidity / 의존성 거버넌스 마찰 0

→ L 결정 후보표에 L-1.5 를 명시적으로 추가하고, 경로 B(진짜 stdlib 채택) 채택 시 구현 수단으로 권고.

### N-C-3 — means-vs-ends ends 달성 다른 수단 조합 (누락 hybrid)

ends = (secret leak 0 / ledger 무결성) 를 달성하는 brief 미언급 조합:
- **ledger 무결성 ends**: 현 stdlib(`hashlib.sha256`)는 brief 가 채택. 그러나 canonical *직렬화* 의 결정성(determinism)만 보장되면 RFC 8785 strict 가 *아니어도* ends(동일 입력 → 동일 hash → tampering 검출)는 충족된다. 즉 RFC 8785 정합은 *상호운용성(interop)* 요구이지 *무결성* ends 요구가 아니다. 본 repo ledger 가 외부 시스템과 hash 를 교환하지 않는 1인 도구 단계라면 stdlib canonical(L-1.5)로 ends 완전 충족 — RFC 8785 strict(L-5)는 interop 가 실제 trigger 될 때까지 deferred 가 비례적. (메모리 `feedback_proportionate_security_personal_tool` 답습)
- **secret leak 0 ends**: R-3(CI 사후 canary) + W-E(pre-commit 사전) 조합 외에, **GP-1 DB INSERT 차단(brief 가 §0 에서 GP-1 책임으로 분리)** 과의 경계가 §2 에서 흐릿하다. 송신 redaction(GP-2)의 ends 중 일부는 애초에 secret 을 ledger/log 에 *쓰지 않는* GP-1 설계로 달성될 수 있음 — R 수단 깊이 결정 전 GP-1/GP-2 ends 경계를 §2.1 에 1줄 명시 권고.

### N-C-4 — 수단별 차등 합의 깊이(§6.3) 는 적절하나 L 영역 깊이 상향

§6.3 의 차등(R-4/L-4 풀 검토, W 풀 검토, R-5/L-2/L-5 얕은 검토)은 방향이 옳다. 단 R-C-1 발견(L 오분류)에 비추어, **L 영역은 "얕은 검토(L-2/L-5 분리 확정)" 가 아니라 "현 시제가 이미 L-2 계열" 이라는 사실 자체가 풀 검토 대상** 이다. §6.3 에서 L-2/L-5 를 "분리 확정 = 얕은 검토" 로 둔 것이 R-C-1 오분류를 은폐한 구조적 원인 — 차등표에서 L-2/L-5 의 "이미 발효된 시제" 여부를 별도 행으로 분리 권고.

### N-C-5 — W-E(pre-commit) 보조 병행의 실효성 confirm

`.pre-commit-config.yaml` 이 실재(5644B)하므로 W-E 병행은 즉시 가능. 다만 brief §4.2 #4 가 "W-E = 대체 아님" 이라고만 적었는데, **무엇을 pre-commit 에 넣을지** (secret_scanner --mode scan-source? canonical 검증?) 의 후보가 없다. W-E 를 보조로 *결정* 하려면 최소 hook 후보 1~2개를 §4.2 에 명시 권고 (없으면 W-E 결정은 공허).

---

## NOTE (NT-C-N)

### NT-C-1 — R 영역(R-3 시제) 분류는 정확

`secret-hygiene-egress-redaction.yml` (51791B) line 165~191 의 `--mode scan-log` redaction_pass/fail 검증 + `secret_scanner.py` 시제는 brief §1.2/§2.1 묘사대로 실재한다. R-3 "시제 충족 = 즉시 PASS 격상 경로" 주장은 *정확*하다 (R-C-1 의 L 오분류와 대조). R 영역은 권고 수준 수정으로 충분.

### NT-C-2 — r2-canary trigger paths 정합 (메모리 답습)

`r2-canary.yml` push.paths = `docker/r4-1-poc/**`, `docker/r2-poc/**` 등으로 한정 → `tools/jsonl_hash_chain.py` 변경은 r2-canary 가 *아니라* g4-hash-chain 을 trigger 한다. brief §7.1 조건 2(R-6 actual run = r2-canary)와 조건 3(4 G4 workflow run = g4-hash-chain 등)의 분리 매핑은 정합. (메모리 `feedback_actual_run_trigger_paths_filter` 답습 — empty commit 만으로 trigger 0 유의)

### NT-C-3 — "4 G4 workflow" 셈 일관성

brief §1.2 가 "4 G4 workflow (g4-hash-chain + history-anchor-verifier + rewrite-defense + r2-canary)" 로 셈하나, r2-canary 는 GP-2/R-4.1 canary 영역(Layer 4 ledger 검증 아님)이고 secret-hygiene 은 GP-2 영역이다. Layer 1/2/4 ledger 무결성 직접 담당 = g4-hash-chain(Layer1) + history-anchor-verifier(Layer2) + rewrite-defense(Layer2) 3개. "4 G4 workflow" 표현이 r2-canary 를 Layer 4 로 오귀속할 소지 — §1.2 표기 정밀화 권고 (BLOCKING 아님, R-C-2 W 재분류와 함께 처리 가능).

### NT-C-4 — 자기진단 P-4 가 R-C-1 을 부분 인지했으나 오결론

brief §12 P-4 = "L-1 stdlib 권고가 RFC 8785 strict 정합 과소평가 → fallback 동등성 + corpus 72 로 처리" 라고 적었다. 이는 R-C-1 의 *반대 방향* 결론이다 — 실제 문제는 "stdlib 가 strict 를 과소평가" 가 아니라 "**시제가 stdlib 가 아니라 외부 library Primary 인데 brief 가 stdlib 로 오분류**" 다. P-4 의 자기진단이 정확한 방향이었다면 R-C-1 이 brief 단계에서 잡혔을 것 — 자기진단이 fallback 동등성을 *방어선* 으로 신뢰한 것 자체가 fallback 이 런타임 경로가 아님(R-C-1 #2)을 놓친 결과.

### NT-C-5 — 작성자 cascade risk (P-5) 실재 확인

본 brief 작성자 = 51/52/55 작성자(Claude Opus 4.7). L-1 오분류(R-C-1)는 51 audit §3.4 의 "L-1 stdlib 단독" 후보 정의를 *실 시제 검증 없이* 답습한 데서 비롯 — 51 audit 가 "수단 결정 0" 이어서 시제 검증이 면제됐으나, 본 (β) cycle 은 "결정 cycle" 이므로 시제 ↔ 후보 동일성 검증이 *필수* 였다. cross-vendor (E-α) 외부 LLM 에 본 R-C-1(filesystem evidence 포함)을 *명시 입력* 하여 독립 재검증 권고.

---

## 요약 매트릭스

| ID | 등급 | 영역 | 핵심 |
|----|------|------|------|
| R-C-1 | BLOCKING | L | "L-1 stdlib 시제 충족 / 외부 의존 0" 거짓 — 실 시제 = rfc8785+jcs 강제 의존(g4-hash-chain.yml line 68 pip install + jsonl_hash_chain.py line 99 PRIMARY_1_ONLY). 미설치 시 검증 100% 실패(실행 verify). 현 시제 = L-2/L-5 계열 |
| R-C-2 | BLOCKING | W | "보존우선 = W-A(ii) 변형" 부정확 — 실질은 분산 보존(신설 0) = W-A(통합) 반대. W-F 신규 정의 또는 W-B 재분류 + 2축 분류 명시 필요 |
| N-C-1 | 권고 | R | R-4 ≡ "R-3 단독 + R-1/R-2 deferred" 실질 동형 — framing 선택지로 명시 |
| N-C-2 | 권고 | L | L-1.5(stdlib 4번째 Primary + 자동 degrade) 정식 후보 추가 (52 §2.2.4 답습) |
| N-C-3 | 권고 | 통합 | ends 달성 다른 조합 — RFC8785 strict=interop≠무결성, GP-1/GP-2 ends 경계 명시 |
| N-C-4 | 권고 | §6.3 | L 영역 합의 깊이 상향 (시제=L-2 사실이 풀 검토 대상) |
| N-C-5 | 권고 | W | W-E pre-commit hook 후보 1~2개 명시 (없으면 결정 공허) |
| NT-C-1~5 | NOTE | - | R 분류 정확 / trigger 정합 / 4-workflow 셈 / 자기진단 오결론 / cascade 재검증 |

---

**verdict: REVISE** (BLOCKING 2 + 권고 5 + NOTE 5)

핵심: 본 brief 의 *방향*(R defense-in-depth + L MVP stdlib 정신 + W 보존)은 비례성·means-vs-ends 정합하나, **L sub-수단의 후보(L-1)와 실 시제(L-2 계열)의 동일성 주장이 실측으로 거짓**(R-C-1)이고 **W 명칭 분류가 실질과 불일치**(R-C-2)하여, "수단 *결정* cycle" 의 결정 기반이 부정확하다. 두 BLOCKING 정정 후 재합의 권고.
