# GP-3 Stage 2 sub-step 2.2 — PASS fixture (image layer clean).
# 본 Dockerfile 은 secret 을 image 에 굽지 않음 — runtime /run/secrets/ 마운트 한정.
# 검증 canary = FAKE_TEST_SECRET_DO_NOT_USE_gp3_stage2_layer_clean_canary_2026
# (canary 는 image 외부 의 secret material 식별용 — image 안에 *나타나면 안 됨*)

FROM python:3.11-slim
WORKDIR /app
RUN echo 'PoC: runtime secret reader (no baked secret)' > /app/README.txt
CMD ["cat", "/app/README.txt"]
