FROM python:3.8-slim-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements/prod.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py makemigrations --noinput
RUN python manage.py collectstatic --noinput


