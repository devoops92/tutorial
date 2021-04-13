FROM python:3.9.2-slim

ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . .
ENV DJANGO_SETTINGS_MODULE "tutorial.settings.docker"
RUN sed -i 's/deb.debian.org/mirror.kakao.com/g' /etc/apt/sources.list
RUN apt-get update
RUN apt-get -y install python-dev libpq-dev gcc
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
CMD python manage.py migrate ; gunicorn --workers 4 tutorial.wsgi:application --bind 0.0.0.0:8888
