# 3+1 합의 보고서 — 디딤돌1d frontier CLI planner 설계 brief (4 source)

> CLAUDE.md §3 3+1 합의. 검토 대상: `docs/phase0/jarvis-stone1d-frontier-planner-design-brief.md` (DRAFT v1).
> 4 source: Agent A(구현) · Agent B(품질/안전) · Agent C(대안) · codex(cross-vendor). Phase 2 병렬 독립.

**작성일**: 2026-05-30
**종합 판정**: **REVISE → v1.1 정정(BLOCKING 5) 흡수 시 APPROVE WITH CONDITIONS**
**source별**: A=FEASIBLE(BLOCKING 0) · B=REVISE · C=APPROVE(조건부) · codex=REVISE. 방향(BossPlanner frontier 구현)은 전원 타당 판정 + `run_from_planner` 무변경 확인. 그러나 brief 가 **사실 오류 1 + over-claim 1 + 안전 방치 1**.

---

## Phase 3 — 교차 비교

### ① 일치 (Consensus)

| # | 합의 | 출처 |
|---|---|---|
| **CN-1** ⭐ | **"새 전파면 0" over-claim 정정** — plan *소비* 경로 전파면 0(controller 검증 재사용)은 맞으나, **plan *생성* 단계 frontier CLI subprocess 는 신규 실행면**(claude/codex 는 fs 쓰기·명령 실행 능력 보유, worker.py:268-269). "plan 데이터 downstream 실행권은 안 열되, planner 프로세스 실행면은 새로 생김". 1b §0("전파면 새로 연다") 정직성 답습 | B(BL1)·codex(BL1) |
| **CN-2** ⭐ | **plan 생성 RO 격리 = 필수**(Q2 열린질문 → 격상). Passthrough 동등 후보 반대(frontier untrusted 와 모순). plan=제안이지 실행 아님 → 쓰기 차단 기본값 | B(BL2)·codex(BL2)·C(대안3) |
| **CN-3** | **Q3 파싱 = per-CLI envelope adapter → `_parse_bossplan` 단일 수렴**(단일 `from_cli` 강제 반대). codex `--json`=JSONL 스트림이라 from_cli(단일 JSON 가정) 거짓 실패. claude=단일 JSON `{result}`. CLI 별 추출 전략 후 `_parse_bossplan` 1곳 | A·B·C·codex |
| **CN-4** | **신규 `planner.py`**(boss.py 분리) — subprocess+isolation 의존을 boss.py "순수 추론(부작용 0)" 서술과 분리. `_parse_bossplan`·`boss_plan_prompt` 는 import | A·C·codex |
| **CN-5** | **CLI subprocess timeout 필수** — `_subprocess_runner`(worker.py:90-95)에 timeout 부재 → hang 무한 대기. timeout → PLAN_UNAVAILABLE | B(R2)·codex |
| **CN-6** | **ADR-013 보강**(plan 생성 subprocess 실행면 도입이 사유 — plan 공급원 교체 자체 아님) | B(R3)·codex(Q5) (C는 cross-ref면 족) |
| **CN-7** | **Q1 첫 구현 = codex**(설치 확인 + structured output). 둘 다 argv 주입 구조, 첫 TDD 범위는 codex 단일 | A·B·C·codex |

### ② 불일치 (Divergence)

| # | 쟁점 | 입장 |
|---|---|---|
| **DV-1** ⭐ | **§1/§3 "grammar 부재" 사실 오류** | C 발견(단독, 중요): brief 가 "frontier CLI 는 ollama `format` grammar 없음 → prompt 유도 + `_parse_bossplan` 만 구조 강제"라 전제 → **틀림**. `codex exec --output-schema <FILE>` / `claude -p --json-schema` 가 ollama `format` 와 동등 schema 강제. **기존 `_PLAN_JSON_SCHEMA`(boss.py) 재사용 가능** → schema flag 우선 + `_parse_bossplan` 방어 2층. dogfooding 공정성↑(둘 다 schema-constrained 비교). A/B/codex 는 grammar 부재 전제를 그대로 수용(놓침) |
| **DV-2** | **isolation 방식** | B/codex: Landlock RO(단 codex 도 "Landlock API 는 RW workdir 전제 → plan용 profile 별도 필요" 인정) / C: **CLI native read-only sandbox**(`codex exec --sandbox read-only`)가 Landlock 보다 정확(CLI 가 자기 실행 모델 앎, Landlock 은 RW workdir 전제라 plan 부적합). net egress 는 plan 에 필수라 어느 쪽도 미차단(잔여 명문화). → **CLI native 우선(C) + Landlock 보조**가 합리적 |

### ③ 누락 (Gap)

| # | 사항 | 출처 |
|---|---|---|
| **GP-1** | `_parse_bossplan` 의 `depends_on` 에서 `bool` 이 `int` 로 통과(boss.py:469) — `produced_by` 는 bool 제외 있으나 depends_on 누락. bool 제외 회귀 테스트 | codex |
| **GP-2** | stdout 크기 상한 + empty result reject + stderr 포함 오류 메시지 | codex |
| **GP-3** | 2단 파싱 명시(from_cli envelope → result → `_parse_bossplan`) + fence 제거(`_strip_code_fences` worker.py:284) | A |

---

## Phase 4 — 합의 도출 (Reviewer 최종 판단)

### BLOCKING (v1.1 정정 의무)
| # | 정정 | 근거 |
|---|---|---|
| **BL-1** | CN-1 — "새 전파면 0" → "plan 데이터 신뢰 경로는 기존 검증+승인 재사용. **단 frontier CLI subprocess = 신규 실행면**(RO 격리·timeout·fail-closed 필요)" | B·codex |
| **BL-2** | CN-2 — plan 생성 **RO 격리 필수**(Passthrough = explicit opt-in). 방식 = CLI native read-only sandbox 우선(DV-2) + net egress 미차단 잔여 명문화 | B·codex·C |
| **BL-3** ⭐ | DV-1 — §1/§3 **"grammar 부재" 사실 오류 정정** — codex `--output-schema`/claude `--json-schema` 동등, `_PLAN_JSON_SCHEMA` 재사용(schema flag 우선 + `_parse_bossplan` 방어 2층) | C |
| **BL-4** | CN-3 — Q3 per-CLI envelope adapter → `_parse_bossplan` 단일 수렴(단일 from_cli 강제 반대, codex JSONL) | A·B·C·codex |
| **BL-5** | CN-5 — CLI subprocess timeout 필수(hang → PLAN_UNAVAILABLE) | B·codex |

### 채택 (일치 → v1.1)
CN-4(planner.py 분리) · CN-6(ADR-013 보강) · CN-7(codex 첫 구현) + GP-1(bool 제외) + GP-2(stdout 상한·empty reject) + GP-3(2단 파싱·fence).

### 갈림 해소
- **DV-1 (grammar 사실 오류)**: C 단독 발견이나 **명백한 사실** — schema flag 채택(BL-3). dogfooding 공정성·견고성 직결.
- **DV-2 (isolation 방식)**: Reviewer 권고 = **CLI native read-only sandbox 우선**(codex `--sandbox read-only`) — Landlock 은 RW workdir 전제라 plan 부적합(codex 도 인정). Landlock 은 보조 외부강제. **단 사용자 결정(Q2)**.

### 메타 편향 자기진단
brief 가 frontier CLI 능력을 *과소*평가(grammar 부재 = 사실 오류) + *과대*평가("새 전파면 0" = subprocess 실행면 누락) 양방향 결함. C 가 사실 오류를, B/codex 가 실행면을 잡음 — 단일 source 였으면 놓쳤을 것(다관점 가치). frontier 를 "더 똑똑한 공급원"으로 띄우려다 그 능력(=실행 부작용)을 안전 측면에서 경시한 메인 컨텍스트 편향을 4 source 가 교정.

---

## §7 Q 합의 권고 (고정은 사용자)

| Q | 합의 권고 | 분포 |
|---|---|---|
| Q1 첫 frontier | **codex** | 4/4 |
| Q2 isolation | **RO 필수** — CLI native sandbox 우선(C) vs Landlock RO(B/codex). Passthrough=opt-in | 갈림 — 사용자 결정 |
| Q3 파싱 | **per-CLI adapter → `_parse_bossplan`** | 4/4 |
| Q4 위치 | **신규 planner.py** | 3/4 |
| Q5 ADR | **ADR-013 보강**(실행면) | 3/4 |
| (신설) schema flag | **codex --output-schema/claude --json-schema 사용**(`_PLAN_JSON_SCHEMA` 재사용) | C(사실), 채택 권고 |
