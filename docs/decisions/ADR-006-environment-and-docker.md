# ADR-006: 환경 변수 중앙 관리 + Docker-First

**상태**: 승인 (3+1 합의 완료)
**날짜**: 2026-04-06
**의사결정자**: 3+1 에이전트 합의

---

## 맥락 (Context)

하드코딩 금지, 설정 중앙 관리, Docker 기본 환경이 프로젝트 전반의 기본 원칙으로 필요하다.

## 결정 (Decision)

**2-파일 전략 + Docker-First + MVP 최소 변수**

- `.env` + `.env.example`만 유지 (5파일→2파일)
- MVP 환경 변수 8개: APP(3) + AI(4) + SECRET_KEY
- MVP docker-compose: backend + postgres 2서비스만
- Fail-Fast: 필수값 누락 시 즉시 중단 (field_validator)
- 프로덕션: CI/CD 시크릿 매니저 사용 (.env 파일 아님)
- 서비스/변수는 실제 필요 시점에 점진적 추가

## 3+1 합의 결과

| 에이전트 | 핵심 |
|---------|------|
| Agent A | .env 3개로 축소, Fail-Fast 검증 누락, GPU 이중화 |
| Agent B | 프로덕션 평문 시크릿 = 제8조 미충족, 정규식 개선 |
| Agent C | **과잉 설계** — 2파일, 8변수, 2서비스로 MVP 축소 |
| **Reviewer** | **C 방향 + A 검증 + B 보안 통합** |

---

**관련 문서**: `docs/architecture/environment-and-docker-design.md`
