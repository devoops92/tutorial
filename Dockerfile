FROM python:3.9.2-slim

ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . .
RUN yum -y install python-dev libpq-dev
RUN pip install -r requirements.txt


