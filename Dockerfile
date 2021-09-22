FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY requirements.txt /code/
COPY . /code/ 
RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev \
    && pip install -r requirements.txt
