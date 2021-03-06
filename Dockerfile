FROM python:3.8-slim-buster

WORKDIR /opt/banners_api

# Dependencies for Couchbase
RUN apt update && apt install -y wget gnupg2
RUN wget -O - http://packages.couchbase.com/ubuntu/couchbase.key | apt-key add - && \
    OS_CODENAME=`cat /etc/os-release | grep VERSION_CODENAME | cut -f2 -d=` && \
    echo "deb http://packages.couchbase.com/ubuntu ${OS_CODENAME} ${OS_CODENAME}/main" > /etc/apt/sources.list.d/couchbase.list && \
    apt-get update && apt-get install -y libcouchbase-dev libcouchbase2-bin build-essential

ARG env=prod

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY .env .env
COPY tasks.py tasks.py
COPY ./app ./app