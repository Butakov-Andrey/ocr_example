FROM python:3.11-slim

# Копируем uv из отдельного образа
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию
WORKDIR /code

# Устанавливаем системные пакеты и обновляем pip
RUN apt-get update && apt-get install -y --no-install-recommends \
    tesseract-ocr \
    tesseract-ocr-rus \
    tesseract-ocr-eng \
    libsm6 \
    libxext6 \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Копируем только файл pyproject.toml для установки зависимостей
COPY pyproject.toml /code/pyproject.toml

# Устанавливаем зависимости проекта
RUN uv pip install --system --no-cache-dir -r /code/pyproject.toml

# Копируем оставшийся код проекта
COPY . /code/
