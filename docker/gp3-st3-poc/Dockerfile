# GP-3 Stage 2 ST-3 PoC — Dockerfile
# 본 image 는 docker secret 을 *image layer 에 포함하지 않음* 검증용.
# ENV / COPY / ARG 통한 secret 주입 0건 — 런타임 /run/secrets/ 마운트 한정.

FROM python:3.11-slim

WORKDIR /poc
COPY app.py /poc/app.py

USER 1000:1000

CMD ["python", "-u", "/poc/app.py"]
