# Jarvis 디딤돌1d 설계 brief — frontier CLI planner (plan 공급원 유연) (v1.1)

> **본 brief = 설계 정리 한정.** staged: brief v1 → **3+1 합의(4 source, REVISE)** → **brief v1.1(본 문서, BLOCKING 5 + §7 Q 결정)** → 디딤돌1d TDD 구현. 코드 전 문서 먼저(SDD).

---

**작성일**: 2026-05-30
**Status**: **v1.1 — 3+1 합의(REVISE→AWC) 흡수(BLOCKING 5) + §7 Q1~Q5 결정(2026-05-30, Q2 CLI native RO sandbox). 디딤돌1d TDD 구현 진입 승인됨**
**진입 단위**: `BossPlanner` Protocol(IN-2)의 **두 번째 구현** — frontier CLI(codex/claude)를 planner 로. 약한 로컬 boss 외 더 똑똑한 공급원.
**상위 문서**: `jarvis-stone1b-...`(IN-2) · `jarvis-stone1c-...`(하네스 흡수) · 94 entry(dogfooding) · `ADR-013`
**합의 보고서**: `docs/review/3plus1-consensus-2026-05-30-jarvis-stone1d-frontier-planner.md`
**근거**: dogfooding(94) · `feedback_boss_role_not_smartest`(IN-2 실현) · `feedback_provider_liquidity`(argv 교체=planner 교체) · `feedback_pass_scope_overclaim` · `ADR-011` §2.1 · `reference_codex_verify_tooling`(codex 호출 규약)

---

## v1.1 변경 이력 (3+1 합의 흡수)

| # | v1 → v1.1 | 출처 |
|---|---|---|
| 🔴 BL-1 | **"새 전파면 0" over-claim 정정** — plan *소비* 경로 전파면 0(controller 검증 재사용)은 맞으나 **plan *생성* 단계 frontier CLI subprocess = 신규 실행면**(fs 쓰기·명령 실행 능력, worker.py:268-269). 1b §0 정직성 답습 | B·codex |
| 🔴 BL-2 | **plan 생성 RO 격리 = 필수**(Passthrough = explicit opt-in). 방식 = **CLI native read-only sandbox**(codex `--sandbox read-only`) 우선 + net egress 미차단 잔여 명문화 | B·codex·C |
| 🔴 BL-3 ⭐ | **"grammar 부재" 사실 오류 정정** — codex `--output-schema`/claude `--json-schema` 가 ollama `format` 와 동등 schema 강제. **`_PLAN_JSON_SCHEMA`(boss.py) 재사용** (schema flag 우선 + `_parse_bossplan` 방어 2층) | C |
| 🔴 BL-4 | **Q3 per-CLI envelope adapter → `_parse_bossplan` 단일 수렴** — codex `--json`=JSONL 스트림이라 `from_cli`(단일 JSON) 부적합. CLI 별 추출(codex=`--output-last-message` 파일, claude=`from_cli.result`) | A·B·C·codex |
| 🔴 BL-5 | **CLI subprocess timeout 필수**(hang → PLAN_UNAVAILABLE) | B·codex |
| R1~R3 | planner.py 분리 / ADR-013 보강 / `_parse_bossplan` depends_on bool 제외 + stdout 상한 + empty reject | A·C·codex |

---

## §0 배경 — IN-2 의 실현

- **IN-2**(1b): `BossPlanner` 를 `advise` 와 분리 → "plan 공급원은 boss 로 고정 안 됨". 현 구현 = `OllamaBoss.plan`(약한) + `StubBoss.plan`(트랙 A).
- **dogfooding(94)**: 약한 boss plan 품질 한계. 1c 가 하네스로 흡수, 1d = **더 똑똑한 공급원**(직교 보완, C: "1c+1d 조합이 최강").
- **1d = `BossPlanner` frontier 구현** — codex/claude CLI. dogfooding 으로 약한 boss vs frontier 품질(특히 contract 생성) 비교.

---

## §1 핵심 결정 — CliPlanner (신규 planner.py, R1)

```python
# src/jarvis/planner.py (신규 — boss.py "순수 추론" 서술 보존, subprocess+isolation 의존 분리)
class CliPlanner:                               # BossPlanner 구현
    def __init__(self, argv, *, extract, runner=None, timeout_s=..., schema=_PLAN_JSON_SCHEMA): ...
    def plan(self, prompt: str) -> BossPlan:
        # 1) schema flag 로 _PLAN_JSON_SCHEMA 전달(BL-3) + plan_prompt+prompt
        # 2) subprocess(native RO sandbox argv, timeout BL-5) 실행
        # 3) per-CLI extract(BL-4): codex=--output-last-message 파일, claude=from_cli.result
        # 4) _parse_bossplan(추출 텍스트) → BossPlan. 실패=RuntimeError → PLAN_UNAVAILABLE
```

- **CliWorker 패턴 답습**(argv+runner+timeout) 단 **출력=BossPlan**(WorkerResult 아님) → 별도 adapter(planner.py).
- **schema flag(BL-3)**: codex `--output-schema <tmpfile>` / claude `--json-schema` 로 `_PLAN_JSON_SCHEMA` 강제(ollama `format` 동등). prompt 유도 = 보조, `_parse_bossplan` = 방어 2층(provider liquidity — schema 미지원 흡수).
- **per-CLI extract(BL-4)**: 단일 `from_cli` 강제 금지. codex `exec --json`=JSONL → `--output-last-message <file>` 로 최종 메시지 파일 추출. claude `-p --output-format json` → `from_cli().output`. 둘 다 최종 → `_parse_bossplan` 1곳 수렴. extract 전략 주입.
- **timeout(BL-5)**: runner 에 timeout 강제. hang = PLAN_UNAVAILABLE(자원 폭주 방어 — non-adaptive 1회 호출이 비용은 막아도 hang 은 못 막음).
- **provider liquidity**: argv+extract 교체 = planner 교체(codex↔claude). `run_from_planner(CliPlanner(...), prompt, task_id)`.

## §2 plan prompt + 파싱

- `boss_plan_prompt`(boss.py) 재사용(worker_kind·depends_on·contracts 안내·means 금지). schema flag 가 1차 구조 강제이므로 prompt 는 *내용* 안내 위주.
- `_parse_bossplan` 재사용(boss.py) — means 필드 부재 재검증. **R3 보강**: `depends_on` bool 제외(현재 int 통과, boss.py:469) + stdout/메시지 크기 상한 + empty result reject(거짓 진행 금지).

## §3 안전 — frontier 도 untrusted + 신규 실행면 (BL-1·BL-2)

- **plan *데이터* 신뢰 경로 = 기존 재사용(전파면 0)**: CliPlanner 가 낸 BossPlan 도 controller 검증(schema/DAG/table/budget/능력 경계)+사람 승인 그대로(PLAN-SOURCE, `run_from_planner`→`run`). frontier 가 똑똑해도 plan=untrusted, 검증·승인 면제 0.
- ⚠️ **plan *생성* = 신규 실행면(BL-1)**: claude/codex CLI 는 LLM-only 아님(fs 쓰기·명령 실행 능력, worker.py:268-269). `CliPlanner.plan()` subprocess 는 plan 을 만드는 동안 부작용 가능 → **RO 격리로 닫음(BL-2)**.
- **RO 격리(BL-2, Q2 결정)**: **CLI native read-only sandbox**(`codex exec --sandbox read-only`) 우선 — CLI 가 자기 실행 모델을 알아 정확(Landlock 은 RW workdir 전제라 plan 부적합). Landlock = 보조 외부강제(opt-in). **Passthrough = explicit opt-in 만**(plan=읽기 신뢰는 frontier untrusted 와 모순).
- ⚠️ **net egress 미차단 잔여(정직)**: plan 생성은 frontier API 호출에 네트워크 필수 → RO sandbox 도 net 은 못 막음. plan 중 CLI 가 네트워크로 exfil/명령 수신 가능성은 잔여(detection≠prevention, MVP-1+ 후속).
- **injection**: plan prompt=사람 작성. CLI 응답=schema flag + `_parse_bossplan` 구조 강제. 악성 plan 은 controller 검증+능력 경계 흡수(1a~1c 답습).

## §4 dogfooding 계획 (약한 boss vs frontier)

- 데모 `--planner ollama|codex` 옵션 → 같은 작업 (a) OllamaBoss.plan vs (b) CliPlanner(codex) 비교. **contract 생성 여부**(94 약한 boss 미생성 → frontier schema flag 로 개선?) + subtask 분해 품질. 1c(하네스 흡수)+1d(공급원 품질) 2축 가치(C).

## §5 비례성 — 무엇을 *안* 하는가

- **boss→frontier 자동 fallback 안 함**(추론적 판정·과설계). **사람 planner 별도 후속**. **Landlock plan profile 신규 설계 안 함**(CLI native sandbox 로 시작, 범위 축소 C). **plan 캐싱·재계획 안 함**(L4).

## §6 변경 영향 + 다음 단계

### 변경 영향
- 신규 `src/jarvis/planner.py`: `CliPlanner`(BossPlanner) + per-CLI extract 전략. `_parse_bossplan`·`boss_plan_prompt`·`_PLAN_JSON_SCHEMA`(boss.py) + `_strip_code_fences`·runner(worker.py) import. grimp 단방향(planner→boss/worker/isolation).
- boss.py: `_parse_bossplan` depends_on bool 제외(R3, 소). 데모 `--planner` 옵션.
- 재사용: `run_from_planner`(controller, 변경 0). 회귀 0 목표(396 passed).

### 다음 단계
1. brief v1 → 3+1 합의(REVISE) → **brief v1.1** + §7 Q 결정 ← 완료
2. **TDD 구현**(planner.py + CliPlanner + schema flag + native RO sandbox + per-CLI extract + timeout) + dogfooding 비교
3. 구현 후 → **ADR-013 보강**(plan 생성 subprocess 실행면 + RO 격리) + 문서 반영

## §7 열린 질문 — ✅ 사용자 결정 (2026-05-30)

| # | 질문 | ✅ 결정 | 근거 |
|---|---|---|---|
| Q1 | 첫 frontier | ✅ **codex**(설치·규약 확인 `reference_codex_verify_tooling`). claude 는 argv+extract 주입 추가 | 4/4 |
| Q2 | plan isolation | ✅ **CLI native RO sandbox**(codex `--sandbox read-only`) 우선 + Landlock 보조 + net egress 잔여 명문화. Passthrough=opt-in | 갈림 → 사용자 |
| Q3 | 파싱 | ✅ **per-CLI extract → `_parse_bossplan` 단일 수렴**(codex `--output-last-message`, claude `from_cli.result`) | 4/4 |
| Q4 | 위치 | ✅ **신규 `planner.py`**(boss.py 순수 추론 서술 보존) | 3/4 |
| Q5 | ADR | ✅ **ADR-013 보강**(plan 생성 실행면 + RO 격리). plan 데이터 경로 재사용 vs frontier subprocess 실행면 분리 서술 | 3/4 |
| (신설) | schema flag | ✅ **codex `--output-schema`/claude `--json-schema` 사용**(`_PLAN_JSON_SCHEMA` 재사용 + `_parse_bossplan` 방어 2층) | C(사실 정정) |

---

## 부록 — 답습 교차
1b IN-2 / 1c 하네스 흡수 / 94 dogfooding / ADR-013(보강 대상) / 헌법 5조 / [[feedback_boss_role_not_smartest]] · [[feedback_provider_liquidity]] · [[feedback_pass_scope_overclaim]] · [[reference_codex_verify_tooling]] · [[project_jarvis_collaborative_orchestration]].
