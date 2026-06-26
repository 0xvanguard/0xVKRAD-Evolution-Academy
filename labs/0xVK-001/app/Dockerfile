# ============================================================
#  0xVKRAD Lab 0xVK-001 — Aplicación Flask vulnerable
#  Imagen ligera Python 3.11 slim
# ============================================================

FROM python:3.11-slim

LABEL maintainer="0xVKRAD Evolution Academy"
LABEL description="Vulnerable web app for SQLi practice — educational use only"

WORKDIR /app

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN adduser --disabled-password --gecos '' labuser
RUN chown -R labuser:labuser /app
USER labuser

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:5000/health || exit 1

CMD ["python", "-m", "gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]
