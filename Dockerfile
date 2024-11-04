FROM python:3.12.7-bullseye

ENV POETRY_VERSION=1.8.3

RUN apt-get update && apt-get install -y curl make \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry \
    && rm -rf /var/lib/apt/lists/*

ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

COPY ./pyproject.toml ./poetry.lock ./

RUN poetry install --no-root

COPY . .