FROM python:3.9-slim

RUN pip install psycopg2-binary
RUN apt-get update && apt-get install -y libpq-dev

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt







