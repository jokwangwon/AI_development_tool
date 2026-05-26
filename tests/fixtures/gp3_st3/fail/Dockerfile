# GP-3 Stage 2 sub-step 2.2 — FAIL fixture (image layer leak 시연).
# 본 Dockerfile 은 secret 을 COPY 통해 image layer 에 baking — leak 검출용.
# canary = FAKE_TEST_SECRET_DO_NOT_USE_gp3_stage2_layer_leak_canary_2026

FROM python:3.11-slim
WORKDIR /app
COPY baked_secret.txt /app/baked_secret.txt
CMD ["cat", "/app/baked_secret.txt"]
