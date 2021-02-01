FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install g++ -y

WORKDIR /usr/src/project
COPY /project .
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
