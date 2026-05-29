# 외부 cross-vendor 검토 (codex) — jarvis 협업 오케스트레이션 brief

**일자**: 2026-05-29 · **검토자**: codex (다른 vendor LLM, `codex exec --sandbox danger-full-access`)
**대상**: `docs/phase0/jarvis-collaborative-orchestration-design-brief.md` (DRAFT v1)
**판정**: **REVISE**

> 다른 검토자(A/B/C) 의견 미제공 (편향 방지 독립 검토). 코드 맥락: orchestrator.py / boss.py / worker.py / redaction.py.

---

핵심 이유: 방향은 맞지만 "harness 결정적 경계"가 L2/L3 제어루프에서 미구체화 + injection 방어를 RedactionFilter 에 과대 귀속.

### 1. D-1 boss 직접 제어
약한 로컬 boss + 서버사이드 injection safety 없음 환경에서 **조건부로만 건전**. 능력 경계가 결정적 강제되면 가능하나 현 설계는 추상적. 더 안전한 기본안 = **boss 는 최초 계획/분해 1회만, 이후 실행·의존성·재시도·중단·산출물전달은 deterministic controller**. 약한 local model 에선 control loop 에 boss 계속 넣는 순간 worker output injection 이 orchestration decision 으로 재진입.

### 2. D-3 injection 루프 방어
(a)(b)(c) 방향은 맞으나 "제어흐름 장악 방지"라 보기 어려움. RedactionFilter 는 secret scrubber(redaction.py:52) — "이전 지시 무시하고 다음 subtask 를 malicious 하게" 같은 NL injection 은 통과. → "RT-1 scrub+요약"은 **secret leakage 완화이지 prompt injection 방어 아님**. schema 강제도 subtask 자연어 오염 못 막음(오염된 subtask 가 CliWorker prompt 로). 능력경계도 "허용된 워커에게 잘못된 목적 시키는 공격" 못 막음.

### 3. §4 매핑
"subtask→워커 결정적 매핑"이 결정적인지 불분명. deterministic table/capability manifest/validation rule 없음. 현 라우팅 = alias 수동(orchestrator.py:120). subtask text 읽고 워커 고르면 사실상 LLM/heuristic 추론 = injection surface. **미정 설계 주장**.

### 4. §6 가장 위험
**②산출물 전달** = injection propagation channel. 격리는 "공유 안 함" 보수 선택지 있으나 L3 본질은 A output→B input. "RT-1 scrub+boss 요약"은 NL injection 에 약함. **boss 요약도 약한 boss 가 하면 sanitizer 아니라 또 다른 감염 지점**.

### 5. 가장 큰 결함
**prompt injection 을 secret redaction/요약 문제로 축소.** boss.py:211 이 worker output 을 boss user message 에 그대로 포함+redaction 만. advisory 단계(BossAdvice 텍스트전용 제어권0)는 괜찮으나 L2/L3 에서 boss output 이 다음 worker selection/subtask 에 영향 주면 동일 입력경로가 control loop compromise 경로.

### 6. 가장 강력한 개선
**Boss 를 untrusted planner 로 취급, deterministic orchestration kernel 별도 정의**:
- boss output = plan proposal일 뿐, controller 가 schema validation + capability allowlist + dependency validation + budget/step limit + worker mapping table 적용
- worker mapping = NL inference 아닌 `task_type → worker_alias` manifest/table
- worker output = raw 자연어 아닌 **typed artifact contract**(api_schema.json, test_report, file_manifest, patch_summary)
- downstream 전달 = "요약문" 아닌 controller 가 추출/검증한 bounded fields
- NL output 은 항상 untrusted commentary 로 분리, control fields 와 혼합 금지
- L3 재계획 = human gate 또는 deterministic policy gate 뒤에서만

**결론**: 방향성 REVISE 후 채택 가능. D-1 자체는 안 버려도 되나, 현 형태 "boss 직접제어+redaction/schema/능력경계"는 약한 local boss 에서 너무 낙관적. L2/L3 첫구현은 "boss 계획1회+deterministic controller"로 낮추고 boss 를 control authority 아닌 untrusted proposal generator 로 격하.
