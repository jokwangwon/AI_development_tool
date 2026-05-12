# MVP-1 entry coverage — D-1 FAIL fixture
# 답습 출처: docs/phase0/backlog6-implementation-step-brief.md §2.2.1 sub-step 1.1
#
# 본 fixture 는 기존 fail/ fixture (env_assignment / json_field / prefix_aws / private_key_block)
# 가 cover 하지 않는 regex 카테고리 (H-C / H-F / H-G / H-K) 를 MVP-1 entry 회귀 cover.
# 답습 변경 0건 — tools/secret_scanner.py 본문 / R-4.1 Tier-1 45 patterns 변경 0건.
#
# fake canary 의무 답습 (사용자 명시 — F-금지 #1):
#   모든 fake secret 은 FAKE / NOTAREAL / fakecanary / R41T marker 포함.

# H-C (T1-034) — Authorization Bearer
AUTH_HEADER_EXAMPLE = "Authorization: Bearer FAKEBEARERMVP1ENTRYNOTAREAL123"

# H-F (T1-036) — DB connstr password
DB_DSN = "postgresql://user:FAKEDBMVP1ENTRYNOTAREAL@db.example.com:5432/mydb"
REDIS_DSN = "redis://default:FAKEREDISMVP1ENTRYNOTAREAL@cache.example.com:6379"

# H-G (T1-037) — JWT-style token
FAKE_JWT = "eyJhbGciOiJIUzI1NiFAKEMVP1NOTAREAL.eyJpYXQiOjAxRkFLRQ.SIGFAKENOTAREALMVP1"

# H-K (T1-039) — URL userinfo (non-DB)
FAKE_WEBHOOK = "https://botuser:FAKEURLMVP1ENTRYNOTAREAL@hooks.example.com/path"
