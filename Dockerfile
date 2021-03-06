FROM python:3.9-alpine3.13

# enables proper stdout flushing
ENV PYTHONUNBUFFERED yes
# no .pyc files
ENV PYTHONDONTWRITEBYTECODE yes

# pip optimizations
ENV PIP_NO_CACHE_DIR yes
ENV PIP_DISABLE_PIP_VERSION_CHECK yes

WORKDIR /src

COPY poetry.lock pyproject.toml ./

RUN apk add --no-cache libpq \
    && apk add --no-cache --virtual .build-deps \
    # https://cryptography.io/en/latest/installation/#alpine
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev \
    openssl-dev \
    cargo \
    postgresql-dev \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev \
    && apk del --purge .build-deps

COPY src .

RUN addgroup -S pinwin \
    && adduser -S grape_kun -G pinwin \
    && chown -R grape_kun:pinwin /src

USER grape_kun

EXPOSE 80
EXPOSE 8000

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0:8000"]