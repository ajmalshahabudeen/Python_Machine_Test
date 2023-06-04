FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /app1

ADD . /app1

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app1
