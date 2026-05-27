# Jarvis 자가진화 Layer 2 brief — 제안 생성 (read-only Layer 1)

> **scope**: Layer 1 `PatternReport` 를 입력으로 받아 actionable 제안(`Proposal`) 산출 → 사람 가독 출력.
> **safety class**: Layer 1/0 수정 0, 자비스 동작 변경 0, 출력 = `ProposalSet` (frozen) + 텍스트 한정. **단** Layer 2 = "제안" 신설 = 사람 승인 게이트 도입 = 큰 결정 → **풀 3+1 합의 필수** ([[jarvis-layer1-pattern-mining-brief]] 답습 명시).
> **DONE 기준 (설계 단계)**: brief + 3+1 합의 보고서 보존. **코드 구현 0** (발효 DEFER, [[mvp-staged-roadmap]] + [[proportionate-security-personal-tool]] 답습).
> **답습**: [[jarvis-layer0-active]] / [[jarvis-layer1-active]] / [[ceremony-inflation]] / [[mvp-staged-roadmap]].

---

## 1. Layer 2 안전 등급 정당화

| 속성 | 보장 (제안 단계 한정) |
|------|----------------------|
| Layer 1 수정 | **0** — `propose()` 는 `PatternReport` 만 수신 (불변 frozen 입력) |
| Layer 0 수정 | **0** — Layer 1 통해 간접도 0 (PatternReport = 텍스트/숫자 snapshot) |
| 자비스 동작 변경 경로 | **0** — 적용 API 없음, 제안 = "사람이 읽고 결정" 산출물 한정 |
| 외부 호출 | **0** — stdlib + Layer 1 frozen dataclass 만 의존 |
| 출력 형태 | `ProposalSet` (frozen) + `format_proposals()` 텍스트만 |
| 자동 적용 | **0** — Layer 3 (영구 DEFER) 책무. Layer 2 는 *제안* 까지만 |
| 사람 승인 게이트 | 본 brief 단계 = 게이트 **설계** 만. 게이트 *구현 / 발효* 는 추후 cycle (MVP-1 이후) |
| 적용 책임 | **호출자(사용자)** — Layer 2 산출물은 권장 텍스트, 의사결정 / 적용 / 결과 책임 0 |

→ Layer 1 의 "보고만 = 안전 행위 = 게이트 불요" 답습은 Layer 2 에 **확장 안 됨**. Layer 2 산출물 = "사람이 행동하도록 유도하는 제안" → 자동 적용은 안 되더라도 *제안 자체의 품질·편향* 이 사람 의사결정에 영향 = 풀 3+1 검증 필수.

---

## 2. 제안 종류 (v0.0 한정, 설계만)

| 제안 종류 | trigger 조건 (Layer 1 신호) | 출력 형태 |
|---------|------------------------------|----------|
| `WORKER_RELIABILITY_LOW` | 특정 alias `success_rate < 0.5` 이고 `total >= N` (N 후보) | "worker X 의 적용율이 낮음 (a/b). 원인 분석 권장" |
| `FLAG_FREQUENCY_RISING` | `flag_frequency` 중 위험 flag 가 임계 빈도 초과 | "flag F 의 빈도가 높음. boss advisory 분류 점검 권장" |
| `ADVICE_ENDPOINT_DEGRADED` | `advice_failed / advice_total > θ` (θ 후보) | "Boss advisory 실패율 상승. endpoint 건강 점검 권장" |
| `RECENT_FAILURE_CLUSTER` | `recent_failures` 중 동일 worker / flag 가 K건 이상 (K 후보) | "최근 실패가 X에 군집. 회귀 가능성" |
| `ADVICE_AXIS_DEGRADED` | Layer 1 `advice_axis_stats` 4축 중 1축 이상 fail/warn 비율이 임계 이탈 | "advice 축 X 저하. 분류 분포 점검 권장" |
| `INPUT_DROUGHT` | `total_entries == 0` 또는 last_ts 가 오래됨 | "관찰 데이터 부족. Layer 0 가동 점검 권장" |

**수단 후보 (값 결정 = 사용자 영역, 본 brief = 후보만 나열):**
- N (최소 표본): {5, 10, 20, 50}
- θ (실패율 임계): {0.1, 0.2, 0.3}
- K (클러스터 임계): {2, 3, 5}
- `오래됨` 정의: {1h, 24h, 7d}
- α (advice 축 fail 비율 임계): {0.1, 0.2, 0.3}

**threshold 후보값 = 잠정** — 저자 직관 기반. MVP-1 진입 후 실 evidence 누적 → 재조정 (B§2-4 답습).

→ 임계값 *고정 0* (수단/목적 분리 답습, [[ADR-011-means-vs-ends-redaction]]).

비-scope (DEFER 영구): 시계열 anomaly detection, ML 기반 패턴, 정책 *자동 적용*(Layer 3), 외부 LLM 호출(추론적 제안), 동일 alias 중복 제안 dedup, 제안 expire/만료 정책.

---

## 3. API 설계 (DEFER, 본 brief = 시그니처 합의용)

```python
from enum import Enum
from typing import Mapping

class ProposalKind(Enum):
    WORKER_RELIABILITY_LOW = "worker_reliability_low"
    FLAG_FREQUENCY_RISING = "flag_frequency_rising"
    ADVICE_ENDPOINT_DEGRADED = "advice_endpoint_degraded"
    RECENT_FAILURE_CLUSTER = "recent_failure_cluster"
    ADVICE_AXIS_DEGRADED = "advice_axis_degraded"
    INPUT_DROUGHT = "input_drought"

@dataclass(frozen=True)
class Proposal:
    kind: ProposalKind
    severity: str             # "info" | "warn" | "high" (계산적 결정 룰, §3.1 매트릭스)
    subject: str              # alias / flag / endpoint / axis 등 식별자
    evidence: tuple[str, ...] # 근거 — 포맷: "key=value" (공백 0, 회귀 테스트 가능)
    suggestion: str           # 사람 가독 권장 문장 (코드 변경 명령 아님)

@dataclass(frozen=True)
class ProposalSet:
    generated_ts: str             # ISO 8601 UTC, 호출자 주입 (테스트 결정성)
    source_report_signature: str  # PatternReport 의 sha256 (canonical JSON, sort_keys=True, ensure_ascii=False)
    proposals: tuple[Proposal, ...]  # 정렬: severity desc → kind asc → subject asc (결정성 보장)

def propose(
    report: PatternReport,
    *,
    min_sample: int,                            # Layer 2 threshold (호출자 결정)
    advice_fail_threshold: float,
    cluster_threshold: int,
    staleness_seconds: int,                     # last_ts ISO 8601 UTC 가정 (naive → UTC 추정)
    risk_flags: frozenset[str],                 # FLAG_FREQUENCY_RISING 대상 화이트리스트
    advice_axis_threshold: float,               # ADVICE_AXIS_DEGRADED 축별 fail 비율 임계
    severity_thresholds: Mapping[str, float],   # severity 결정 임계 (호출자 결정, §3.1 매트릭스)
) -> ProposalSet: ...

def format_proposals(proposals: ProposalSet) -> str: ...
```

- **frozen + tuple**: 결과 불변 ([[jarvis-layer1-pattern-mining-brief]] §3 답습).
- **threshold 인자 명시**: 함수 안 magic number 0. 호출자(사용자) 가 정책 결정.
- **`source_report_signature`**: PatternReport 의 sha256 over canonical JSON (sort_keys=True, ensure_ascii=False) — 동일 입력 → 동일 signature 보장 (재현성).
- **`severity` 결정 = 계산적 룰**: 아래 §3.1 매트릭스. 추론적 평가 0.
- **정렬 결정성**: `proposals` 튜플 순서 = severity(high/warn/info) desc → kind(enum value) asc → subject asc. dict 순회 등 비결정 요소 차단.

### §3.1 severity 결정 매트릭스 (5종 × 3단)

`severity_thresholds` 인자의 키는 아래 prefix 와 일치 (예: `"worker_high"`, `"worker_warn"`). 호출자 미지정 시 ValueError.

| ProposalKind | high (severity_thresholds key) | warn | info |
|--------------|--------------------------------|------|------|
| `WORKER_RELIABILITY_LOW` | `success_rate < worker_high` (e.g., 0.3) | `< worker_warn` (e.g., 0.5) | 그 외 |
| `FLAG_FREQUENCY_RISING` | `count / total > flag_high` (e.g., 0.5) | `> flag_warn` (e.g., 0.3) | 그 외 |
| `ADVICE_ENDPOINT_DEGRADED` | `failed/total > advice_high` (e.g., 0.5) | `> advice_warn` (e.g., 0.3) | 그 외 |
| `RECENT_FAILURE_CLUSTER` | `cluster_size >= cluster_high` (e.g., 5) | `>= cluster_warn` (e.g., 3) | 그 외 |
| `ADVICE_AXIS_DEGRADED` | `axis_fail_ratio > axis_high` (e.g., 0.5) | `> axis_warn` (e.g., 0.3) | 그 외 |
| `INPUT_DROUGHT` | (항상 info — 신호 부족 상황) | — | 단일 |

(예시값은 *권고 default 후보*, 본 brief = 값 고정 0. 사용자가 `severity_thresholds` 로 주입.)

---

## 4. fail-soft + 거짓 안전감 차단

- 빈 `PatternReport` (total_entries=0) → `INPUT_DROUGHT` 1건만 제안 + 다른 제안 skip.
- threshold 인자 negative / 0 → ValueError (호출자 실수 명시).
- `severity_thresholds` 미지정 키 / `risk_flags` 빈 frozenset → ValueError.
- `success_rate` 평가는 `total >= min_sample` **및** `total > 0` 동시 충족 시만 (zero-state 거짓 양성 차단).
- `format_proposals` = 빈 ProposalSet 일 때 "현재 제안 없음 — 관찰 데이터 정상" 명시 출력 (거짓 안전감 방지: "제안 없음 = 시스템 OK" 가 아니라 "현재 임계 도달 신호 없음" 명시).
- `format_proposals` 출력 헤더에 사용 threshold 값 동봉 ("min_sample=N, advice_fail_threshold=θ 기준 — 임계 조정 시 결과 변동").

---

## 5. 발효 정책 (본 cycle 한정)

- **DEFER**: SDD 문서 + 3+1 합의 보존만. **코드 0 / 테스트 0**.
- **재진입 조건**: MVP-1 진입 후 Layer 0/1 evidence 가 누적되어 *실제 제안 trigger 가 발생할 사례* 가 1건 이상 생긴 시점.
- **답습**: [[mvp-staged-roadmap]] + [[proportionate-security-personal-tool]] = "DESIGN 보존, 발효는 실 trigger 까지".

---

## 6. pass / fail 기준 (3+1 합의)

| 기준 | 답습 |
|------|------|
| Agent A (구현) | API 시그니처 / threshold 인자 분리 / fail-soft 룰 *실제로 동작 가능* 한가? |
| Agent B (안전) | 제안 = 사람 의사결정 영향 = 편향 위험 점검 (e.g., severity 룰의 임의성, "추론적 제안 0" 진짜 성립?) |
| Agent C (대안) | 제안 종류 5개 외 누락된 신호? threshold 후보값의 근거? API 더 단순 가능? |
| Reviewer | 일치 / 부분일치 / 불일치 / 누락 분류 → 최종 보고서 |

**APPROVE 조건**: 3개 출력 모두 "Layer 2 = 제안까지, 적용 0, 발효 DEFER" 원칙 위반 없음 확인. 시그니처는 추후 cycle 에서 재조정 허용.

---

## 7. carry-over

- 본 brief 자체 = scope (h+1) carry-over 0. 단독 cycle.
- 합의 결과 = `docs/decisions/` 신규 ADR 또는 `docs/architecture/self-evolution-layer2-design.md` 흡수 (사용자 결정).
- **후속 cycle carry-over** (발효 단계 진입 시):
  - 제안 audit log 경로 설계 (수용/기각 이력 append-only JSONL, 편향 회고 가능성, B§3-1).
  - severity 인플레이션 unit test (모든 출력이 `high` 가 되는 임계 시나리오 검출, B§3-4).

---

## 8. 의존 / 참조

- [[jarvis-layer0-memory-accumulation-brief]] — Layer 0 기반
- [[jarvis-layer1-pattern-mining-brief]] — 직속 입력
- [[ADR-011-means-vs-ends-redaction]] — 수단/목적 분리 (threshold 후보만, 고정 0)
- [[mvp-staged-roadmap]] — 발효 DEFER 정당화
- [[proportionate-security-personal-tool]] — 비례 보안 답습
- [[ceremony-inflation]] — brief 단계 1-agent 직접 작성, 풀 3+1 = 본 cycle 결정 단계만
