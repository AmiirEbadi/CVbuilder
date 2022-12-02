FROM python:alpine

WORKDIR /app/core

RUN mkdir /app/media

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

CMD sh ./entrypoint.sh
