# AI 백엔드 스택 가이드라인 (AI Backend Stack Guideline)

> **로컬 추론/학습이 필요한 프로젝트에서 AI 백엔드를 Python으로 분리하는 가이드라인 — 라이브러리 생태계 + 확장성 확보**

**최종 수정**: 2026-04-06
**상태**: 설계 확정 (3+1 합의 검증 완료)
**상위 문서**: `idea-driven-stack-decision-design.md` (ADR-002)
**관련 ADR**: ADR-005 (AI 백엔드 스택 가이드라인)

---

## 1. 핵심 원칙 (3+1 합의 결과)

| 원칙 | 설명 | 근거 |
|------|------|------|
| **로컬 추론이 분리 트리거** | "AI 기능이 있으면" 아닌, "로컬 추론/학습이 필요하면" Python 분리 | Agent C + Reviewer — 정확한 분기 기준 |
| **API 호출만이면 분리 불필요** | LLM API만 쓰면 메인 백엔드에서 직접. 언어 무관 | 최소 범위 원칙 |
| **가이드라인 (기본값)** | 절대 규칙이 아닌 강한 기본값. 예외 허용 | Agent C — Guide-First 톤 |
| **보안 최소 세트 필수** | 키 관리 + 출력 검증 + 프롬프트 인젝션 방어 | Agent B — 헌법 제8조 |

---

## 2. 분리 판단: 2단계 분기

### 2.1 결정 흐름

```
아이디어에 AI 기능이 있는가?
    │
    ├── 없음 → AI 백엔드 불필요. 끝.
    │
    └── 있음
        │
        ▼
    로컬 추론/학습이 필요한가?
    (= Python 전용 라이브러리가 필요한가?)
        │
        ├── 아니오 (API 호출만)
        │   → 메인 백엔드에서 SDK 직접 호출
        │   → 별도 AI 백엔드 불필요
        │   → 언어: 메인 백엔드와 동일
        │
        └── 예 (로컬 모델, GPU, 학습)
            → Python AI 백엔드 분리
            → FastAPI + PyTorch/HuggingFace
```

### 2.2 "API 호출만" vs "로컬 추론" 판단 체크리스트

| 질문 | 예 → 분리 | 아니오 → 직접 |
|------|----------|-------------|
| 모델을 로컬에 다운로드/실행하는가? | Python 분리 | — |
| GPU가 필요한가? | Python 분리 | — |
| PyTorch/TensorFlow 등 Python 전용 라이브러리를 쓰는가? | Python 분리 | — |
| 모델 파인튜닝/학습이 필요한가? | Python 분리 | — |
| 위 4개 모두 "아니오" | — | 메인 백엔드에서 직접 |

> **1개라도 "예"면 Python 분리를 권장한다.**

---

## 3. Python AI 백엔드 기본 스택

### 3.1 기본 추천

```yaml
language: python >= 3.11
framework: fastapi
package_manager: uv
linter: ruff
type_check: mypy
test: pytest + httpx
```

### 3.2 디렉토리 구조 + 컨테이너

```
ai-backend/
├── app/
│   ├── main.py              # FastAPI 진입점
│   ├── api/                 # 라우터
│   ├── services/            # 비즈니스 로직
│   ├── models/              # Pydantic 스키마
│   └── core/
│       ├── config.py        # 설정 로드
│       └── security.py      # 입력 검증, 키 관리
├── tests/
├── pyproject.toml
├── Dockerfile               # GPU 지원 기본 이미지 사용
├── docker-compose.yml       # 메인 백엔드 + AI 백엔드 + (선택) 벡터 DB
└── .env.example             # API 키 템플릿
```

```dockerfile
# Dockerfile 기본 참조
FROM python:3.11-slim          # CPU 전용
# FROM nvidia/cuda:12.x-python3.11  # GPU 필요 시

WORKDIR /app
COPY pyproject.toml .
RUN pip install uv && uv sync
COPY app/ app/
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]
```

> GPU 폴백: GPU 미사용 환경에서는 ONNX Runtime(CPU)으로 경량 추론 가능. Dockerfile에서 기본 이미지만 교체.

### 3.3 메인 백엔드와의 통신

| 조건 | 방식 | 이유 |
|------|------|------|
| 소규모 + 동기 응답 < 1s | **REST** | 가장 단순, FastAPI 자동 문서화 |
| 대용량 페이로드 or 스트리밍 | **gRPC / SSE** | 바이너리 효율, 실시간 토큰 스트리밍 |
| 장시간 작업 (학습, 대량 생성) | **메시지 큐** (Redis Queue) | 비동기, 재시도, 큐잉 |
| 메인도 Python일 때 | **직접 import** | 서비스 분리 오버헤드 불필요 |

---

## 4. AI 보안 최소 세트

> 헌법 제8조 준수. 상세 보안 가이드는 별도 문서로 분리 예정.

### 4.1 API 키/시크릿 관리

```
✓ API 키는 환경변수로만 관리 (.env, 컨테이너 시크릿)
✓ 코드/로그에 키 절대 노출 금지
✓ .env.example에 필요 키 목록만 기록 (값은 비움)
✓ 키 순환 주기 설정 (최소 분기 1회)
```

### 4.2 LLM 출력 검증 (Untrusted Output)

```
✓ LLM 출력은 신뢰할 수 없는 외부 입력으로 취급
✓ 출력을 DB 쿼리, 시스템 명령, HTML에 직접 삽입 금지
✓ 출력 표시 시 이스케이프/새니타이즈 적용
```

### 4.3 프롬프트 인젝션 방어

```
✓ 시스템 프롬프트와 사용자 입력을 명확히 분리
✓ 사용자 입력에서 시스템 지시 패턴 필터링
✓ 민감 정보가 시스템 프롬프트에 포함되지 않도록 주의
```

---

## 5. Python이 아닌 경우 (예외)

| 예외 상황 | 대안 | 판단 기준 |
|-----------|------|----------|
| API 호출만 (추론/학습 없음) | 메인 백엔드 언어 | 체크리스트 4개 모두 "아니오" |
| 극도의 저지연 필요 | Rust/C++ + ONNX | 추론 지연 < 10ms 요구 |
| 엣지/모바일 배포 | Swift(CoreML) / Kotlin | 플랫폼 네이티브 필수 |
| 기존 AI 백엔드가 다른 언어 | 기존 스택 유지 | 전환 비용 > 이점 |

> 예외 적용 시 **ADR에 근거 기록 필수**.

---

## 6. 전체 아키텍처 예시

```
[API 호출만 — 분리 불필요]

  Frontend (React)
      │
      ▼
  Backend (Express/TS)
      │ anthropic.messages.create(...)
      ▼
  Claude API (외부)


[로컬 추론 — Python 분리]

  Frontend (React)
      │
      ▼
  Main Backend (Spring Boot)
      │ REST/gRPC
      ▼
  AI Backend (Python/FastAPI)   ← 이 가이드라인
      │ torch, transformers
      ▼
  Local Model (GPU)


[학습 포함 — Python 분리 + 학습 인프라]

  Main Backend
      │ REST (추론) + MQ (학습 작업)
      ▼
  AI Backend (Python/FastAPI)
      ├── 추론 서비스 (vLLM/TGI)
      └── 학습 작업 (Celery + GPU)
```

---

## 7. 3+1 합의 검증 결과 요약

### 핵심 설계 변경

| 변경 항목 | 초안 | 최종 | 근거 |
|-----------|------|------|------|
| 문서 톤 | "규정" | **"가이드라인"** | Guide-First 정신, 강한 기본값 |
| 분리 트리거 | "AI 기능이 있으면" | **"로컬 추론/학습이 필요하면"** | 더 정확한 분기 기준 |
| 결정 흐름 | 3단계 (단순/중간/복잡) | **2단계** (API호출→직접 / 로컬→분리) | 모호성 제거 |
| 보안 | 없음 | **최소 3항목 추가** | 헌법 제8조 필수 |
| Python 버전 | >=3.11 | **>=3.11 유지** | 3.10은 EOL 임박 |
| 예외 | 주관적 판단 | **판단 기준 + ADR 기록 필수** | 형해화 방지 |
| Docker | Dockerfile만 | **Dockerfile + 기본 참조 + GPU 폴백** | 실용성 |

---

**이 문서는 3+1 에이전트 합의를 거쳐 설계가 확정되었습니다.**
