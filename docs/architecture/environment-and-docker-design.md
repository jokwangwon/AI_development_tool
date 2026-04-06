# 환경 변수 중앙 관리 + Docker-First 설계

> **하드코딩 제로. 모든 설정은 환경 변수로, 한 곳에서 관리. Docker를 기본 실행 환경으로.**

**최종 수정**: 2026-04-06
**상태**: 설계 확정 (3+1 합의 검증 완료)
**상위 문서**: `PROJECT_CONSTITUTION.md` 제8조(보안)
**관련 ADR**: ADR-006 (환경 변수 + Docker-First)

---

## 1. 핵심 원칙 (3+1 합의 결과)

| 원칙 | 설명 | 근거 |
|------|------|------|
| **하드코딩 제로** | 코드에 어떤 설정값도 직접 작성 금지 | 3자 합의 |
| **2-파일 전략** | `.env` + `.env.example`만 유지 | 3자 합의 — 5파일은 과잉 |
| **Docker-First** | `docker compose up`이 기본 실행 | 사용자 요구 |
| **Fail-Fast** | 필수값 누락 시 앱 시작 즉시 중단 | Agent A |
| **MVP 최소 변수** | 8개 변수로 시작, 필요 시 추가 | Agent C + 최소 범위 원칙 |

---

## 2. MVP 필수 — 환경 변수 중앙 관리

### 2.1 2-파일 전략

```
.env              ← 실제 값 (Git 미추적)
.env.example      ← 변수 목록 + 설명 (Git 추적)
```

> `.env.local`, `.env.test`, `.env.production`은 해당 Phase에서 필요 시 추가.
> 프로덕션은 CI/CD 시크릿 매니저에서 직접 주입 (파일 없음).

### 2.2 MVP 환경 변수 (8개)

```bash
# .env.example — MVP 최소 변수

# ── APP ──
APP_NAME=my-project
APP_ENV=development        # development | production
APP_PORT=8000

# ── AI ──
AI_PROVIDER=anthropic      # anthropic | openai | local
AI_MODEL=claude-sonnet-4-6
AI_API_KEY=                # ⚠️ 필수 비밀값
AI_MAX_TOKENS=4096

# ── SECURITY ──
SECRET_KEY=                # ⚠️ 필수 비밀값
```

> 서비스가 추가되면 해당 카테고리(DB, REDIS, ASSET 등)를 그때 추가한다.

### 2.3 하드코딩 금지 규칙

```
금지:
  api_key = "sk-abc123..."        # 비밀값 하드코딩
  port = 8000                     # 설정값 하드코딩
  model = "gpt-4"                 # 모델명 하드코딩

허용:
  api_key = os.environ["AI_API_KEY"]    # 환경 변수
  port = settings.APP_PORT               # 중앙 설정 객체
  model = config.AI_MODEL                # 중앙 설정 객체
```

### 2.4 중앙 설정 객체 + Fail-Fast

모든 환경 변수를 **1개 설정 객체**에서 로드. 코드 전체에서 이 객체만 참조.

```python
# Python: core/config.py
from pydantic_settings import BaseSettings
from pydantic import field_validator

class Settings(BaseSettings):
    # APP
    app_name: str = "my-project"
    app_env: str = "development"
    app_port: int = 8000

    # AI
    ai_provider: str = "anthropic"
    ai_model: str = "claude-sonnet-4-6"
    ai_api_key: str
    ai_max_tokens: int = 4096

    # SECURITY
    secret_key: str

    @field_validator("ai_api_key", "secret_key")
    @classmethod
    def must_not_be_empty(cls, v, info):
        if not v or not v.strip():
            raise ValueError(f"{info.field_name} is required. Set it in .env")
        return v

    class Config:
        env_file = ".env"
```

```typescript
// TypeScript: core/config.ts
import { z } from "zod";
import "dotenv/config";

const envSchema = z.object({
  APP_NAME: z.string().default("my-project"),
  APP_ENV: z.enum(["development", "production"]).default("development"),
  APP_PORT: z.coerce.number().default(8000),
  AI_PROVIDER: z.string().default("anthropic"),
  AI_MODEL: z.string().default("claude-sonnet-4-6"),
  AI_API_KEY: z.string().min(1, "AI_API_KEY is required"),
  AI_MAX_TOKENS: z.coerce.number().default(4096),
  SECRET_KEY: z.string().min(1, "SECRET_KEY is required"),
});

export const config = envSchema.parse(process.env);
```

---

## 3. MVP 필수 — Docker-First 환경

### 3.1 MVP docker-compose.yml

```yaml
# docker-compose.yml — MVP (필요한 서비스만)

services:
  backend:
    build: ./backend
    ports:
      - "${APP_PORT:-8000}:8000"
    env_file: .env
    depends_on:
      postgres:
        condition: service_healthy
    restart: unless-stopped

  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: ${DB_NAME:-app_db}
      POSTGRES_USER: ${DB_USER:-app_user}
      POSTGRES_PASSWORD: ${DB_PASSWORD:?DB_PASSWORD required}
    ports:
      - "${DB_PORT:-5432}:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER:-app_user}"]
      interval: 5s
      timeout: 3s
      retries: 5

volumes:
  postgres_data:
```

```yaml
# docker-compose.override.yml — 로컬 개발 (자동 로드)
services:
  backend:
    volumes:
      - ./backend:/app
    command: uvicorn app.main:app --reload --host 0.0.0.0
```

### 3.2 실행

```bash
# 기본 실행
docker compose up

# 재빌드
docker compose up --build

# 특정 서비스만
docker compose up backend postgres
```

### 3.3 서비스 간 통신

```bash
# Docker 내부: 서비스명으로 통신
DB_HOST=postgres          # docker-compose 서비스명

# 로컬 직접 실행 시: .env를 수정
# DB_HOST=localhost
```

---

## 4. 하드코딩 감지 (하네스 센서)

### 4.1 Pre-commit Hook

```bash
# .githooks/pre-commit에 추가

# 시크릿 패턴 감지 (테스트/문서 파일 제외)
EXCLUDE_PATHS="tests/|docs/|\.env\.example|\.md$"
if git diff --cached --name-only | grep -vE "$EXCLUDE_PATHS" | \
   xargs -r git diff --cached -- | \
   grep -iE '(api_key|secret|password|token)\s*=\s*["\x27][A-Za-z0-9_\-\.\/\+]{10,}["\x27]' \
   > /dev/null 2>&1; then
    echo "[ERROR] 하드코딩된 시크릿이 감지되었습니다!"
    echo "  → 환경 변수(.env)를 사용하세요."
    exit 1
fi
```

> 테스트 더미값 허용: `# nosec` 주석이 있는 줄은 무시

### 4.2 보안 참고

```
⚠️ 프로덕션 시크릿 관리:
  개발: .env 파일 (평문, 로컬 전용)
  프로덕션: CI/CD 시크릿 매니저 또는 Docker Secrets 사용 필수
  → .env 파일을 프로덕션에 배포하지 않는다
```

---

## 5. 초기 셋업

```bash
#!/bin/bash
# scripts/setup.sh

set -e
echo "=== 프로젝트 초기 셋업 ==="

# .env 생성
if [ ! -f .env ]; then
    cp .env.example .env
    echo "[OK] .env 생성됨 — 필수 값을 설정하세요:"
    echo "  AI_API_KEY, SECRET_KEY"
else
    echo "[SKIP] .env 이미 존재"
fi

# Git hooks
if [ -d .githooks ]; then
    git config core.hooksPath .githooks
    echo "[OK] Git hooks 설정됨"
fi

echo ""
echo "실행: docker compose up"
```

---

## 6. 확장 가이드 (MVP 이후)

아래 항목은 **해당 서비스/기능이 실제로 추가될 때** 적용한다.

### 6.1 서비스 추가 시

| 서비스 | 추가 시점 | 추가할 환경 변수 | docker-compose 추가 |
|--------|----------|----------------|-------------------|
| AI 백엔드 | 로컬 추론 필요 시 | `AI_BACKEND_URL`, `AI_PORT` | `ai-backend` 서비스 + `profiles: [gpu]` |
| 프론트엔드 | UI 구현 시 | `FRONTEND_PORT` | `frontend` 서비스 |
| Redis | 캐시/큐 필요 시 | `REDIS_HOST`, `REDIS_PORT` | `redis` 서비스 |
| 에셋 생성 | 에셋 파이프라인 시 | `ASSET_*` 카테고리 | — |
| 모니터링 | 프로덕션 시 | `SENTRY_DSN`, `LOG_FORMAT` | — |

### 6.2 환경 분리 (Phase 2+)

```
필요 시 추가:
  .env.test           ← 테스트 전용 (⚠️ 실제 시크릿 포함 금지)
  .env.production     ← 프로덕션 (CI/CD 시크릿에서 자동 생성)
```

### 6.3 Docker GPU 지원 (AI 백엔드 추가 시)

```yaml
# docker-compose.yml에 추가 (profiles 방식)
  ai-backend:
    build: ./ai-backend
    env_file: .env
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: all
              capabilities: [gpu]
    profiles:
      - gpu

# 실행: docker compose --profile gpu up
```

> GPU 폴백: CPU 환경에서는 ONNX Runtime 경량 추론으로 대체 가능.

### 6.4 프로덕션 시크릿 관리 (배포 시)

| 환경 | 방식 |
|------|------|
| GitHub Actions | `secrets.AI_API_KEY` → 환경 변수 주입 |
| Docker Swarm | `docker secret create` |
| Kubernetes | `kubectl create secret` |
| 클라우드 | AWS Secrets Manager / GCP Secret Manager |

---

## 7. 3+1 합의 검증 결과 요약

### 핵심 설계 변경

| 변경 항목 | 초안 | 최종 | 근거 |
|-----------|------|------|------|
| .env 파일 수 | 5개 | **2개** (.env + .env.example) | 3자 합의 — 과잉 |
| 환경 변수 수 | 30+ (8카테고리) | **MVP 8개** (APP+AI+SECRET_KEY) | Agent C + 최소 범위 |
| docker-compose 서비스 | 5개 | **MVP 2개** (backend + postgres) | Agent C + 최소 범위 |
| DOCKER_GPU_ENABLED | 존재 | **제거** | 3자 합의 — 죽은 변수 |
| GPU 설정 | profiles + gpu.yml 이중 | **profiles만** | Agent A — 이중화 제거 |
| Python Fail-Fast | 빈문자열 통과 | **field_validator 추가** | Agent A — 검증 누락 |
| Pre-commit Hook | 경로 제외 없음 | **tests/docs 제외 + 특수문자 대응** | Agent A/B |
| 프로덕션 시크릿 | .env만 | **.env=개발, 프로덕션=시크릿 매니저** | Agent B — 제8조 |
| 문서 구조 | 단일 | **"MVP 필수" + "확장 가이드"** | Agent C |

---

**이 문서는 3+1 에이전트 합의를 거쳐 설계가 확정되었습니다.**
