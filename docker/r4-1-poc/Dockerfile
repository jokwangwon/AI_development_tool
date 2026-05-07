FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
        libsqlcipher-dev \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir "pysqlcipher3==1.2.0"

WORKDIR /poc
COPY r4_1_poc.py /poc/

CMD ["python", "-u", "/poc/r4_1_poc.py"]
