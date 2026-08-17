FROM python:3.12-alpine

RUN apk add --no-cache curl

COPY --from=ghcr.io/astral-sh/uv:0.11.30 /uv /bin/

# Создаём пользователя ДО копирования файлов
RUN adduser -D -g '' -u 1001 app

WORKDIR /app

# Копируем файлы зависимостей
COPY pyproject.toml uv.lock ./

# Устанавливаем зависимости
RUN uv sync --frozen --compile-bytecode --no-dev

# Копируем исходники
COPY app/ ./

# Меняем владельца на app
RUN chown -R app:app /app

EXPOSE 8000

COPY .env.example .env

# Переключаемся на пользователя app
USER app


CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]