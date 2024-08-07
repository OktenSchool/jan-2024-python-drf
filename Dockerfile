FROM python:3.11-alpine

MAINTAINER Some Dev

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.8.2 \
    POETRY_NO_INTERACTION=1 \
    DEBIAN_FRONTEND=noninteractive \
    COLUMNS=80

RUN apk update
RUN apk add --no-cache gcc musl-dev mariadb-dev
RUN apk add --no-cache curl
# for pillow
RUN apk add --no-cache jpeg-dev zlib-dev libjpeg

RUN mkdir /app
WORKDIR /app

#RUN pip install --upgrade pip
#
#COPY requirements.txt /tmp
#
#RUN cd /tmp && pip install -r requirements.txt
ENV POETRY_HOME=/usr/local/poetry
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH=$POETRY_HOME/bin:$PATH

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-ansi