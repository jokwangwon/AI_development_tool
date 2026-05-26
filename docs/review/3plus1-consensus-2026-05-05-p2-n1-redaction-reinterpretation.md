# 단축 3+1 합의 보고서 (Reviewer-only): P2-N1 비협상 조건 해석 갱신

**날짜**: 2026-05-05
**검증 대상**: P2 v2 §2.1.3 정정안 — "외부 pre-record hook" → "Hermes 자체 redaction 강제 활성화 + 보조 안전망"
**상위 결정**: ADR-008 Option B (Hermes 도입), 6 차단조건 비협상
**관련 사실 데이터**: `docs/phase0/day1-environment-and-fact-check.md` §13 (Hermes v0.12.0 코드 grep + 공식 docs 정밀 검증)
**합의 형태**: 단축 (Reviewer-only) — 직전 P1 v2 단축 합의 패턴 답습

---

## 사전 점검 — 합의 가동 정당성

**가동 사유**: ADR-008 부록 A 비협상 조건 R1의 *형태*("외부 pre-record hook 공식 지원")가 Phase 0 Day 1 코드 grep 결과 Hermes v0.12.0에 미존재 확정 (15종 VALID_HOOKS 중 DB 기록 직전 가로채기 hook 0개). 본 형태 요건을 *목적*("DB 평문 저장 차단")으로 재해석할지 여부는 단독 결정 부적절 → 합의 검증.

**단축 합의 채택 사유**: 직전 P1 v2 단축 합의에서 검증된 패턴 (Reviewer 1인 + 메타 편향 자기진단). 본 안건은 **사실 검증된 데이터 기반의 해석 갱신**이지 새 설계 안건이 아니므로 풀 3+1 (병렬 3 에이전트)이 과잉. Reviewer-only로 충분.

**Liquidity 영향**: 본 안건은 Hermes 자체 redaction 활용 권고이며 Provider Liquidity (모델/구독 교체 자유) 와 무관. 반려 사유 없음.

---

## Reviewer 평가 — 결론 및 차원별

### 결론
**APPROVE with revisions** — 정정안 방향성(헌법 8조 본질 = "DB 평문 저장 차단")은 정당. 그러나 **Hermes 자체 redaction의 적용 위치(LLM 송신 전용 vs DB INSERT 경로)가 코드로 미확인**된 채 Primary로 승격하는 것은 부적절. Phase 0에서 적용 위치 직접 검증 + 보조 안전망 (ii) SQLite trigger 의무화 후 안전 채택 가능.

### 차원별 평가

| # | 차원 | 판정 | 핵심 근거 |
|---|------|------|---------|
| 1 | 헌법 제8조 본질 충족 | **PARTIAL** | SQLCipher (a) + redaction (b) 다층 구조는 본질 충족 가능. 그러나 Hermes redaction 적용 위치 미검증 — LLM 송신 전용이면 DB는 평문 |
| 2 | ADR-008 부록 A 해석 갱신 정당성 | **PASS** | "외부 hook"은 R1의 수단, "DB 평문 저장 차단"이 목적. 동일·강한 보장 시 수단 대체 정당. 단 ADR-011/Amendment 명문화 필요 |
| 3 | Hermes 자체 redaction 신뢰도 | **LOW** | v0.12.0 default ON → OFF 전환은 upstream의 redaction 격하 신호. opt-in 핵심 외 기능에 헌법 8조 의존 위험 |
| 4 | 보조 안전망 정합성 | **PARTIAL** | (i) monkey-patch는 silent 깨짐 위험으로 헌법 8조 차단 메커니즘 부적절. (ii) SQLite trigger는 DB 레벨 강제로 정합 |
| 5 | 누락 위험 | 6건 식별 (N1~N6) | 본 §3.5 |

### 누락 위험 (Reviewer 단독 발견 → 합의안 포함)

- **N1**: Hermes 자체 redaction 적용 위치 미검증 — LLM 송신 단계만 적용 시 DB 평문 우회
- **N2**: redaction 패턴 커버리지 격차 — Hermes 패턴 ↔ P1_REDACTOR 패턴 비동일 가능성
- **N3**: SQLite trigger ↔ SQLCipher 호환성 미검증 — REGEXP 미포함, user-defined function 등록 필요
- **N4**: T13 false negative — config가 true여도 Hermes 내부 버그로 redaction 미동작 가능성
- **N5**: Phase 1 합격 #2 검증 SOP 부재 — canary 주입/검증 절차 미명세
- **N6**: CI nightly 회귀 부재 — Hermes 버전 업그레이드 시 redaction 깨짐 자동 검증 누락

---

## 필수 보강 7건 (Phase 0 Day 2~3 + Phase 1 반영)

### R-1 (Phase 0 의무 — CRITICAL, 차원 1·N1 대응)

Hermes v0.12.0에서 `security.redact_secrets: true` 활성화 후, **DB INSERT 경로에 redaction이 실제 적용되는지 직접 검증**.

- 작업: 격리 환경에서 canary 비밀 주입 (예: `sk-ant-CANARY-XXXXX`) → LLM 호출 → `sqlcipher state.db "SELECT content FROM messages WHERE content LIKE '%sk-ant%'"` 실행
- PASS 기준: 0건 반환 (DB에 평문 부재)
- FAIL 기준: 1건 이상 반환 → **정정안 즉시 폐기 → 옵션 A로 회귀 → §3.4 폴백 트리거 (ADR-011)**

본 검증은 Phase 0 Day 2의 **새 1순위 작업**으로 격상.

### R-2 (보조 안전망 의무화 — 차원 4 대응)

원안 "(i) 택일 또는 병행" → 정정:
- **(ii) SQLite trigger 의무 채택** (DB 레벨 강제, BEFORE INSERT on messages, REGEXP user-defined function 등록)
- **(i) monkey-patch는 비차단 모니터링용으로만 강등** — 헌법 8조 차단 경로 의존 금지. 침해 발생 시 알림 트리거로만 사용

### R-3 (ADR-011 또는 ADR-008 Amendment 발행 — 차원 2 대응)

ADR-008 부록 A의 R1 텍스트 갱신:

> "R1의 비협상 핵심은 *DB 평문 저장 차단이라는 결과*이며, *외부 hook이라는 수단*은 동등 이상의 보장 시 대체 가능하다."

발행 시점: 본 합의 결과 확정 시 즉시 (Phase 0 Day 5 이전).

### R-4 (패턴 동등성 검증 — N2 대응)

Phase 0에서 Hermes 자체 redaction 패턴 집합 ↔ P1_REDACTOR (P1 v2 §8.2) 패턴 집합 비교. gap 발견 시 SQLite trigger에서 보충 패턴 적용.

### R-5 (T13 강화 — N4 대응)

P2 v2 §7.1 자동 롤백 트리거 신규 T13:
- (a) config `redact_secrets: true` 비활성화 감지 (entry point + 1시간 헬스체크)
- (b) **주기적 canary inject DB 검증** (1시간 간격 healthcheck job, R-1과 동일 방식)
- 둘 다 포함 — config만으로는 false negative 회피 불가

### R-6 (CI nightly 회귀 — N6 대응)

CI에 Hermes 의존성 업그레이드 PR 자동 R-1 canary 실행. redaction 깨짐 발견 시 머지 차단.

### R-7 (Phase 1 합격 #2 SOP 명세화 — N5 대응)

별도 문서 `docs/phase0/redaction-verification-sop.md` 작성:
- canary 비밀 패턴 목록
- 주입 절차
- sqlcipher 검증 쿼리
- PASS/FAIL 판정 기준

---

## Phase 1 차단조건 #1 검증 항목 갱신 (R-1~R-7 반영)

본 합의 채택 시 P2 v2 §2.1.5는 다음으로 갱신:

```
✅ Phase 1 차단조건 #1 exit (7항목):
  1. 강제 sqlite3 열기 거부 (SQLCipher 동작) — 기존
  2. 환경변수 echo LLM 호출 → DB 평문 확인 안 됨 (Hermes 자체 redaction + SQLite trigger 보조) — R-1
  3. Base64 인코딩 비밀 LLM 호출 → 동일 (R2-6 유지)
  4. 디스크 탈취 시뮬레이션 → 키 없이 열기 불가 — 기존
  5. Vault 헬스체크 + Shamir 분할 키 보존 — 기존
  6. Sample restore 1회 성공 (분기 의무) — 기존
  7. 신규: redact_secrets config 검증 + 주기적 canary 검증 (R-5) + 패턴 동등성 (R-4)
```

---

## 메타 편향 자기진단 (Reviewer 보고서 인용)

> 본 평가에서 자체 코드 친화 편향을 통제하기 위해 두 가지를 적용했다.
>
> 첫째, "외부 hook 형태가 비협상이라는 엄격 해석"이 합리적인지 진지하게 재고했다. *수단*과 *목적* 분리 결론에 도달했으나, 이는 자체 코드 우호 결론이므로 한 단계 더 회의적으로 점검 — *대체 수단의 신뢰도*가 원래 수단보다 낮다면 엄격 해석을 유지하는 것이 안전. 이로 인해 "Primary 단독 의존 금지", "보조 안전망 의무화", "redaction 적용 위치 직접 검증을 Phase 0 차단조건으로 격상" 도출.
>
> 둘째, F2 "redaction 적용 위치 미확인"을 가볍게 처리하지 않았다. 자체 코드 우호 해석은 "redaction 기능이 있으니 Primary로 충분"으로 흐를 수 있는데, 본 평가는 차원 1 PARTIAL 판정과 R-1 Phase 0 의무 검증으로 명시 차단. v0.12.0 default OFF 전환을 LOW 신뢰도 신호로 평가한 것도 같은 맥락 — upstream 의도를 우호적으로 해석하지 않고 부정 신호로 독해.

---

## 최종 합의 — 사용자 결정 입력

### Reviewer 권고

**정정안 채택 (단, R-1~R-7 보강 후) + R-1 검증 결과에 조건부**

- Phase 0 Day 2 새 1순위: **R-1 (Hermes 자체 redaction 적용 위치 직접 검증)**
- R-1 PASS (DB INSERT 경로 적용됨) → R-2~R-7 적용 후 정정안 확정 → Phase 0 계속
- R-1 FAIL (LLM 송신 전용) → 즉시 §3.4 폴백 → ADR-011 작성 → 옵션 A 회귀

### 메인 컨텍스트 권고 (단축 합의 메타 평가)

- Reviewer 평가 정합성: **HIGH** (메타 편향 통제 명시 + 차원별 PARTIAL/LOW 판정의 보수성 + 누락 위험 6건 식별)
- 사용자 결정 옵션:

| 옵션 | 의미 | 다음 |
|------|------|------|
| **(1) Reviewer 권고 채택** | 정정안 + R-1 검증 우선 + R-2~R-7 보강 | Phase 0 Day 2 진입, R-1 검증 결과에 따라 분기 |
| (2) 옵션 A로 즉시 회귀 | Reviewer의 "정정안 채택" 결론도 보수적으로 거부 | §3.4 폴백 ADR-011 작성, P2 폐기 |
| (3) 추가 합의 (풀 3+1) | 본 단축 합의로 부족하다고 판단 | Agent A/B/C 병렬 분석 추가 (~30분) |

**메인 컨텍스트 추천: 옵션 (1)** — Reviewer 평가가 보수적·균형적이며 R-1을 차단조건으로 설계해두어 안전. 옵션 (2)는 정보 손실, 옵션 (3)은 사실 데이터 기반 안건에 과잉.

---

**합의 보고서 작성 시각**: 2026-05-05
**다음 진입점**: 사용자 결정 (위 (1)/(2)/(3)) → R-1 검증 또는 §3.4 폴백
