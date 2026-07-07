# 3+1 합의 — 프라이데이 진입 (2026-07-07) — Agent A (구현 분석가)

> 독립 분석 (Phase 2). 검증 대상: `docs/phase0/friday-separate-evolution-tool-entry-brief.md`
> + §14 D-2 (R) 하이브리드 결정. 다른 에이전트 출력 참조 0.

## Agent A 구현 분석 보고서

### 1. 종합 판정: **CONDITIONAL-PASS**

(R) 하이브리드는 기술적으로 실현 가능하며, 핵심 격리 부품은 자비스에서 이미 실증된 코드를 거의 그대로 재사용 가능하다. 다만 brief 에 구현상 stale 항목 3건(테스트 수·endpoint 하드코딩·audit log 미구현)과, D-2=(R) 결정이 D-3/D-4 권고를 실질적으로 뒤집는 결합 효과 1건이 있어 조건부 통과로 판정한다.

### 2. 핵심 발견

1. **LandlockIsolation 은 자비스-특정적이지 않다 — 그대로 재사용 가능.** `src/jarvis/isolation.py:74-135` 의 `LandlockIsolation` 은 `sandbox_bin / ro_paths / rw_root / rw_files` 전부 생성자 주입이며 자비스 고유 로직 0건. fail-closed(sandboxer 부재 시 비격리 fallback 금지, `isolation.py:120-126`) + 디바이스 검증(`_safe_rw_device`, `isolation.py:20-41`)까지 포함. 프라이데이 5-layer 격리의 filesystem/workdir 층은 **신규 설계가 아니라 부품 재사용 문제**다.
2. **가짜 홈(레벨 2) 패턴이 (R) 엔진 자체에 적용 가능** — `src/jarvis/worker_setup.py` 의 `CLAUDE_RO_PATHS`(좁은 RO) + `CLAUDE_RW_DEVICES`(/dev/null 단일) + `CLAUDE_ARGV`(headless json) 는 *claude 를 Landlock 안에서 돌리는* 검증된 레시피다. 즉 프라이데이 진화 엔진(Claude `/loop` 인스턴스)을 프라이데이 workdir 를 RW root 로 하는 가짜 홈 샌드박스 안에서 돌리면, **R-Friday-1(자비스 소스 침범 0)이 규약이 아니라 커널 강제**가 된다. brief §4.5 의 fail-closed 요구를 곧바로 충족하는 경로.
3. **E-Friday-3 "144/144" 는 stale.** 현재 테스트 수집 = **791 tests** (`pytest tests/ --collect-only`). brief §7 의 숫자 고정 표현은 "전체 green" 으로 갱신 필요 — 사소하지만 Evidence 정의가 낡은 채 발효되면 센서가 잘못 통과한다.
4. **endpoint 격리 §4.4(a)와 자비스 코드 재사용이 충돌한다.** `boss.py:257` `_OLLAMA_CHAT_URL = "http://localhost:11434/api/chat"` 모듈 상수 + `boss.py:441` "생성자에 url 인자 0건 — SSRF 회피" 의도적 설계. 프라이데이가 `OllamaBoss` 를 재사용해 11435 를 쓰려면 코드 변경이 필요하다. 권고: 프라이데이 쪽에서 **localhost 한정 + 포트만 파라미터화**한 자체 클래스(SSRF 회피 본질 보존, 수단만 조정 — ADR-011 정합).
5. **audit log(§4.5)는 현재 미구현이며 공짜가 아니다.** `ll_sandbox.c` 에 audit/log 코드 0건(grep 0 hits). Landlock 은 deny-by-default 라 거부가 *조용히* 일어난다(가짜 홈 saga 에서 이미 실증된 gotcha — "조용히 실패", `worker_setup.py` 주석). 커널 6.17 은 Landlock audit(6.15+)를 지원하므로 구현 가능하지만 **신규 작업**이다. brief 는 이를 기존 답습처럼 기술하고 있어 정정 필요.
6. **GPU 직렬화 규약은 준비돼 있으나 Ollama 는 미동참 잔여다.** `~/.gb10/gpu_lock.py`(중립 단일 소스) 존재 확인. 프라이데이 별도 Ollama 인스턴스는 **gpu_lock 동참을 진입 조건으로 명문화**해야 한다(기존 메모리상 ollama 배치 = 미동참 잔여 → 프라이데이가 이 갭을 넓히면 안 됨).
7. **D-2=(R) 결정이 D-3/D-4 권고를 뒤집는다** (§4 참조) — brief 의 (a) 별도 브랜치 권고는 (P) 자체코드 전제 시절의 것. (R)에서 진화 엔진=Claude Code 세션이므로 **repo 위치가 곧 Claude 프로젝트 메모리 스코프**가 된다.

### 3. (R) 하이브리드 실현성 평가

**실현 가능 — 두 레이어 분리는 구현상으로도 자연스럽다.**

- **① 엔진(Claude `/loop`+Workflow)**: `/loop` 스킬은 본 환경에 실존하며 self-paced 반복을 지원. 주기 내 fan-out 은 Agent tool 병렬 dispatch 로 이미 이 프로젝트에서 상시 사용 중(3+1 합의 자체가 그 패턴). 신규 기술 리스크 낮음.
- **② 두뇌(로컬 Ollama)**: 자비스 `OllamaBoss`(stdlib urllib 단독, SDK 의존 0)가 존재 실증 — 프라이데이 자식도 동일 패턴으로 즉시 구동 가능. Provider Liquidity 논리도 구현상 정합: **제품(프라이데이 런타임)은 로컬로 돌고, 공장(진화 루프)만 Claude** — 공장 lock-in 은 제품 lock-in 이 아니다.

**병목/실패 모드 3가지 (모두 대응 가능):**

| 실패 모드 | 내용 | 대응 |
|---|---|---|
| **컨텍스트 소진** | 장기 `/loop` 는 대화 컨텍스트가 자라다 compaction 으로 루프 상태를 잃음 | **루프 상태를 컨텍스트가 아닌 파일(JSONL/registry)로 외부화** 의무 — 자비스 Layer 0 JSONL 패턴 답습. brief 미명시 → 조건 |
| **무인 실행 권한** | 루프가 사람 개입 없이 돌려면 permission 우회 필요 | 자비스 워커 레시피(`--dangerously-skip-permissions` + Landlock 가짜 홈) 그대로 — 권한 우회를 커널 격리가 상쇄하는 검증된 조합 |
| **비용/rate limit** | Workflow fan-out × self-paced 주기 = 구독 quota 소진 | R-Friday-5 와 직결. 주기 하한 + fan-out 폭 상한을 MVP-0 에서 수치 고정 필요 |

또 하나: "자동 진입 0건" 원칙과 self-paced 루프의 긴장은 **T1/T2/T3 분리로 해소 가능** — 격리 안 관찰·제안·검증(T1) 자동은 허용, 프라이데이 자기 코드 commit(적용)의 자동 여부는 D-8 에서 cadence 를 정해야 한다. 구현상 막히는 지점은 아니다.

### 4. 격리 메커니즘 구현 평가

5-layer 중 **4개는 실증 부품 재사용, 1개(audit log)만 신규**:

| Layer | 재사용 원천 | 판정 |
|---|---|---|
| filesystem ACL/Landlock | `isolation.py` LandlockIsolation + `ll_sandbox.c`(ABI 7 실증) | ✅ 그대로. 단 audit log 는 신규(발견 5) |
| workdir | `/tmp/friday-*` prefix + rw_root 가짜 홈 | ✅ 생성자 인자만 교체 |
| endpoint | 별도 Ollama 포트 | ⚠️ `OllamaBoss` url 하드코딩 → 프라이데이 자체 클래스 필요(발견 4) |
| 메모리 | Claude 프로젝트 메모리 스코프 | ⚠️ D-3 과 결합 — 아래 |
| commit | 브랜치/repo 분리 + branch protection | ✅ 기존 규약 |

**핵심 지적 — D-3/D-4 결합**: (R)에서 진화 엔진은 Claude Code 세션이므로, **별도 repo(별도 cwd)를 쓰면 Claude 프로젝트 메모리 스코프 분리(사실상 (iii) 최강 격리)가 공짜로 따라온다.** 반면 brief 권고 (a) 같은 repo 별도 브랜치는 (i) 같은 CLAUDE.md·같은 메모리 스코프를 엔진이 공유(격리 약화), (ii) 공유 워킹트리에서 프라이데이 루프와 자비스 세션의 checkout 충돌(기존 `feedback_parallel_session_isolation` 메모리의 실사고 패턴 재현). ll_sandbox 재사용은 별도 repo 에서도 바이너리 복사/서브모듈로 해결 가능. **구현 관점에서 D-3 = (b) 별도 repo 로 권고 변경** — 사용자의 기존 lab 패턴(~/gen_gate, ~/motion_lab, ~/style_forge 전부 별도 repo)과도 일치.

### 5. HW 평가

**별도 Ollama 인스턴스 병행은 기술적으로 사소하다** — `OLLAMA_HOST=127.0.0.1:11435 ollama serve` + `OLLAMA_MODELS` 를 기존 스토어로 공유하면 모델 blob 디스크 중복 0. 현재 메모리 121GB 중 112GB 가용 실측. Qwen3-30B-A3B q4 급 2개 동시 상주(~40-50GB)는 수치상 여유.

**그러나 문제는 Ollama 2개가 아니라 3자 경합이다**: 이 머신은 diffusion/영상 lab 들이 GPU 를 크게 쓰는 공유 풀이고(OOM 사고 이력), 프라이데이 진화 루프의 "검증" 단계가 로컬 추론을 반복 호출하면 상시 부하가 된다. 따라서:
- **D-5 = "자비스 idle 시점만" 권고 지지** (R-Friday-2 회피).
- 프라이데이 Ollama 는 **gpu_lock flock 동참 + `keep_alive` 짧게(사용 후 언로드)** 를 진입 조건으로.
- R-Friday-2 의 "응답 지연 ≥2배" trigger 는 **baseline 이 있어야 센서가 된다** — 자비스 `model_benchmark.py`/`model_measurement_repo.py` 가 이미 측정 인프라이므로 재사용해 baseline 을 사전 기록할 것(현재 brief 는 측정 수단 미지정).

### 6. D 항목 권고 (D-1, D-3~D-8)

| # | 구현 관점 권고 | 근거 |
|---|---|---|
| D-1 | MVP-1 완료 후 유지. 구현상 블로커 없음 — 제어측 반영 루프(PR #55)까지 실증돼 gate 근접 | stage gate 자체는 구현 중립 |
| D-3 | **(b) 별도 repo 로 권고 변경** (brief 의 (a) 아님) | §4 결합 효과: 메모리 스코프 공짜 분리 + 워킹트리 충돌 회피 + lab 패턴 일치 |
| D-4 | 별도 repo 채택 시 (iii) 상당이 자동 충족 — 별도 결정 소멸. 같은 repo 고수 시에만 (ii), 단 이는 **규약 격리일 뿐 강제 아님** 명시 | Claude 프로젝트 메모리 = cwd 기반 스코프 |
| D-5 | idle 시점만 + 포트 11435 + `OLLAMA_MODELS` 공유(RO) + **gpu_lock 동참 의무** + keep_alive 단축 | 발견 6, 실측 112GB 가용 |
| D-6 | 권고안 그대로(문서 작업, 구현 리스크 0) | — |
| D-7 | 풀 3+1 + 외부 LLM 1+ 지지 — codex 경로(`codex exec --sandbox danger-full-access`) 이미 실증돼 실행 비용 낮음 | 기존 reference 답습 |
| D-8 | commit cadence 를 **T1(관찰/제안 산출물)=루프 자동, T2(프라이데이 자기 코드 변경 commit)=주기당 사람 승인 배치, T3=해당 없음(자비스 영역 영구 0)** 으로 분리 정의 후 결정 | §3 "자동 진입 0건" 긴장 해소 |

### 7. 갭/리스크 목록

1. **[정정 필요] E-Friday-3 수치 stale** — 144 → 현재 791 collected. "전체 green" 표현으로 교체.
2. **[신규 작업] audit log 미구현** — `ll_sandbox.c` 에 로깅 0건, Landlock 거부는 조용함. 커널 6.17 = Landlock audit 지원이므로 구현 가능하나 brief 가 기존 답습처럼 기술한 것은 부정확. 격리 PoC(E-Friday-2) 범위에 명시 포함할 것.
3. **[코드 갭] OllamaBoss endpoint 하드코딩** (`boss.py:257`, 의도적 SSRF 회피) — 프라이데이 재사용 시 localhost 한정+포트 파라미터화 자체 클래스 필요.
4. **[미명시] 루프 상태 외부화** — `/loop` 장기 구동 시 컨텍스트 compaction 으로 진화 상태 소실. 파일 기반 상태(JSONL) 의무를 MVP-0 에 명문화해야 함.
5. **[미정의] 진화 루프의 fitness/검증 대상** — "관찰→제안→검증" 에서 *무엇을* 계산적으로 검증하는지(테스트? 벤치마크 점수? 로컬 모델 응답 품질?) 미정. MVP-0 scope 이나, (R) 채택으로 이 정의가 D-2 의 실질이 됐음 — 계산적 센서 우선 원칙(CLAUDE.md §2) 적용 필수.
6. **[센서 부재] R-Friday-2 baseline** — "지연 ≥2배" 는 사전 측정 없이는 발화 불가. `model_benchmark.py` 재사용으로 해소 가능.
7. **[비용] Workflow fan-out × self-paced 루프의 quota 소진** — R-Friday-5 와 연동해 주기 하한/fan-out 상한 수치를 MVP-0 에서 고정.
8. **[구조 리스크] 같은 repo 브랜치 격리 채택 시** 공유 워킹트리 충돌 + 메모리 스코프 공유 — D-3 (b) 전환으로 소거 가능 (본 보고서 최대 권고).

**결론**: (R) 하이브리드는 자비스 실증 부품(Landlock/가짜 홈/OllamaBoss 패턴/gpu_lock/측정 인프라) 위에 얇게 얹을 수 있어 1인 개발 부담 추정(brief 의 (P) ~10-15 cycle)보다 낮아질 여지가 크다. 위 조건 8건 중 1·2·3 정정 + 4·5 의 MVP-0 명문화를 전제로 진입 자격 충족.
