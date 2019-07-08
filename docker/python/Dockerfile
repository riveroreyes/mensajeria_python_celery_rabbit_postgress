FROM python:3.6
MAINTAINER carlos@localhost

COPY ./app /app

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY ./docker/python/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

