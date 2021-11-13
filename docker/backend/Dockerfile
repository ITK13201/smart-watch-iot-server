FROM python:3.9-buster AS development

ENV PYTHONDONTWRITEBITECOTE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /backend \
    && mkdir -p /var/log/backend

WORKDIR /backend

RUN apt-get update \
    && pip install --upgrade pip \
    && pip install pipenv

COPY ./backend/Pipfile /backend/Pipfile
COPY ./backend/Pipfile.lock /backend/Pipfile.lock

RUN pipenv install --ignore-pipfile --deploy --system --dev

COPY ./backend /backend
RUN cd /var/log/backend && \
    touch app.log sql.log


FROM python:3.9-buster AS production

ENV PYTHONDONTWRITEBITECOTE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /backend \
    && mkdir -p /var/log/backend

WORKDIR /backend

RUN apt-get update \
    && pip install --upgrade pip \
    && pip install pipenv

COPY ./backend/Pipfile /backend/Pipfile
COPY ./backend/Pipfile.lock /backend/Pipfile.lock

RUN pipenv install --ignore-pipfile --deploy --system

COPY ./backend /backend
RUN cd /var/log/backend && \
    touch app.log
