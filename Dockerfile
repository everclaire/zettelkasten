FROM ubuntu:20.04

RUN apt-get update \
    && apt-get -y install python3 python3-pip \
    && pip3 install httpx kazoo

COPY zetl /usr/local/bin/

COPY cli.py /usr/local/bin/