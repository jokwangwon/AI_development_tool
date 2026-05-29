# ADR-013: Artifact Contract + Capability Boundary (디딤돌1b 워커 간 산출물 전달)

**상태**: 승인 (3+1 합의 4 source 만장일치 AWC — 2026-05-30)
**날짜**: 2026-05-30
**의사결정자**: 사용자 + 3+1 합의 — `docs/review/3plus1-consensus-2026-05-30-jarvis-stone1b-artifact-contract.md`
**상위 권위**: `ADR-011` §2.1 (수단/목적 분리, (a)~(d) 4조건) · CLAUDE.md §2 (Agent=Model+Harness, 계산적 우선) · 헌법 제5조-2 (Provider Liquidity)
**설계 문서**: `docs/phase0/jarvis-stone1b-artifact-contract-design-brief.md` (v1.1)

---

## 1. 맥락 (Context)

디딤돌1a(`PlanController`)는 다중 subtask 를 결정적 배치 실행하되 **산출물 워커 간 전달이 0**(각 subtask 독립 workdir)이었다. 디딤돌1b 는 상위 협업 오케스트레이션 brief §6 ② 의 "산출물 전달"을 도입한다 — **이는 jarvis 에 처음으로 워커 간 데이터 흐름(injection 전파 채널)을 여는 보안 변경**이다.

핵심 위험: produced_by subtask 출력이 consume subtask 입력으로 흐르면, consume 워커(LLM)가 주입된 데이터를 instruction 으로 해석하는 **2차 injection** 이 가능하다. 약한 로컬 boss + Anthropic 서버사이드 안전망 부재 환경에서, 이 전파면을 *추론적 방어*(redaction·길이 제한)만으로 막는 것은 over-claim 이다(`feedback_pass_scope_overclaim`).

## 2. 결정 (Decision)

### 2.1 typed value 주입 (파일 중계 아님)
controller 가 produced 출력에서 평문 bounded text 를 추출(redact secret → truncate)해 consume subtask 의 desc 말미에 결정적 주입. workdir 독립 유지(파일 공유 0), 워커 간 직접 통신 0. raw NL 전체 전달 0.

### 2.2 ⭐ 능력 경계 (Capability Boundary) — 결정적 완화
**artifact 를 consume 하는 subtask 의 worker_kind 는 기본 `file`(OllamaWorker)만 허용.** `code`/`shell`(CliWorker/TmuxWorker = 실 실행) consume 은 `allow_code_consume=True` opt-in + 계획 게이트 경고로만. → **오염된 artifact 가 주입돼도 LLM-only consume 워커는 임의 명령/경로 실행·workdir escape 0**. 이는 추론적 다층 방어보다 강한 *결정적 능력 제거*(CLAUDE.md §2 "잘못하는 것이 불가능하게").

> **정밀화(2026-05-30, 디딤돌1c BL-1)**: OllamaWorker 는 `output_filename` 설정 시 **workdir 단일 파일 write 경로**가 있다(worker.py:358-393, realpath traversal 차단). 따라서 "fs 실행 능력 0"은 부정확 — 정확히는 **"임의 명령/경로 실행 0 + workdir escape 0, 단 output_filename 설정 시 workdir 단일 파일 산출 잔여"**. consume-safe 불변식 = file alias 가 *writer 없는*(`output_filename=None`) OllamaWorker 임을 harness 구성이 보장.

### 2.3 Contract 모델 — consumed_by 유추
`Contract{name, produced_by}` 만. consume subtask = produced_by 를 transitive depends_on 하는 subtask 로 controller 가 결정적 유추. boss 출력 표면↓ + depends_on/contract 정합 불일치 구조적 제거. means 틀 필드(argv·alias·추출 방법) 부재 — boss 는 "산출 선언"(ends)만, 추출·주입·검사·능력 경계(means)는 controller.

## 3. ADR-011 §2.1 (a)~(d) 적용

| # | 조건 | 본 ADR 이행 |
|---|---|---|
| (a) 동등 이상 보안 결과(비교표) | 능력 경계 + typed value 주입이 "raw 직접 전달 + 무제한 consume" 대비 **실 부작용을 결정적 차단**(§4 비교표) | §4 |
| (b) 격리 PoC 실증 | TDD: code consume 기본 reject / file consume 통과 / redact→truncate / raw value 레저 미영속 / 빈 artifact 중단 / 짧은 injection 통과(한계 실증, 공허참 아님) | `tests/jarvis/test_artifact_contract.py` (13) |
| (c) ADR 권위 명시 | 본 ADR-013 | — |
| (d) 자동 회귀 검증 | 389 passed + grimp 단방향(BL-8) + secret_scanner | CI |

### §4 비교표 (a)

| 위협 | raw 직접 전달 + 무제한 consume | typed value + 능력 경계 (1b) |
|---|---|---|
| 오염 artifact → consume 워커 **실 부작용** | CliWorker consume = 파일·명령 실행 위험 | **기본 file(LLM-only) = 실 부작용 0**. code = opt-in 명시 |
| raw NL 전체 전파 | 전량 전달 | bounded truncate(부피 제한) |
| 워커 간 직접 통신 | 가능 | controller 경유만(contract-first) |
| secret 전파 | 무검사 | redact(secret strip) 먼저 |

## 4. 정직 단서 (Honesty — over-claim 차단)

- ✅ **결정적 차단**: 능력 경계로 오염 artifact 의 **임의 명령/경로 실행 0 + workdir escape 0**(code opt-in 제외). ⚠️ 단 file consume 워커가 `output_filename` 설정 시 **workdir 단일 파일 산출은 잔여**(임의 실행 아님 — 정밀화 §2.2, 1c BL-1).
- ❌ **완전 차단 아님**: consume 워커(LLM)가 주입 텍스트를 instruction 으로 해석해 *오염 텍스트를 산출*하는 것은 막지 못한다(단 능력 경계로 실 부작용 미발생). **"능력 경계로 실 부작용 차단, 오염 텍스트 산출만 잔여"**(under-claim 개선).
- **bounded(truncate)는 injection 차단 아님** — 길이 제한은 부피만 축소, 짧은 injection 문장은 통과(길이≠의미 검사).
- **redaction 은 secret-only** — NL injection payload 미차단(ADR-011 R-4 / 상위 brief §3 B1).
- **exfil catalog = secret-only 시작** — 내부 경로/URL/사용자명은 미적용(후속). detection≠prevention.

## 5. 결과 (Consequences)

- 협업 핵심 유스케이스(API 산출 → 프론트 **code** 워커 소비)는 1b 기본에서 opt-in 으로 밀린다 — 안전(실 부작용 결정적 차단)과 협업 편의의 trade. 사용자 결정(Q7).
- 한 produced 가 여러 의존 subtask 중 일부에만 흐르는 세밀 제어 불가(consumed_by 유추, Q8) — 과주입은 능력 경계 + bounded + 게이트로 흡수(YAGNI).
- 구조화 JSON schema artifact·exfil 경로 catalog 는 후속(평문·secret-only 시작).
- 답습 교차: `ADR-011` §2.1 / CLAUDE.md §2·§3 / `feedback_pass_scope_overclaim` / `feedback_boss_role_not_smartest` / 합의 보고서.

---

## 6. 디딤돌1c·1d 보강 (2026-05-30)

### 6.1 디딤돌1c — depends_on 암묵 contract (능력 경계 정밀화 소급)
controller 가 `depends_on` 에서 데이터 전달을 추론(암묵 contract) — 약한 boss 가 Contract 미생성(94 dogfooding)이어도 전달 발동(하네스 흡수). 능력 경계 동일 적용(file consume 기본). **§2.2 능력 경계 정밀화**(위 정밀화 블록): OllamaWorker 는 `output_filename` 설정 시 workdir 단일 파일 write 잔여 → "임의 명령/경로 실행 0 + workdir escape 0" 으로 정정. consume-safe = writer 없는 OllamaWorker harness 불변식.

### 6.2 디딤돌1d — frontier CLI planner (plan 생성 실행면)
`BossPlanner` 의 frontier 구현(CliPlanner) — plan 공급원 유연(IN-2). **plan *데이터* 신뢰 경로는 기존 controller 검증+승인 재사용(전파면 0)** — frontier 도 untrusted(똑똑함≠신뢰). **단 plan *생성* 단계 frontier CLI subprocess = 신규 실행면**(claude/codex 는 fs 쓰기·명령 실행 능력) → **RO 격리 필수**(CLI native read-only sandbox, codex `--sandbox read-only`). net egress 는 plan API 호출에 필수라 미차단 잔여(detection≠prevention, MVP-1+ 후속). dogfooding: codex(frontier)가 contract 생성(약한 boss 대조 — IN-2 실증), 단 codex CLI 자동 통합은 per-CLI 출력 변동 gotcha(claude=from_cli envelope 결정적, codex 후속).
- 답습: `jarvis-stone1c-...` · `jarvis-stone1d-...` 합의 보고서 / `feedback_boss_role_not_smartest`(IN-2).
