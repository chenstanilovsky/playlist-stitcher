FROM ubuntu:22.04

WORKDIR /playlist-stitcher

COPY requirements-dev.txt /tmp/requirements-dev.txt
COPY requirements.txt /tmp/requirements.txt
COPY .pypirc /root/.pypirc

RUN apt-get update && \
    apt-get install -y \
        python3.11 \
        python3-pip && \
    pip install -r /tmp/requirements-dev.txt && \ 
    pip install -r /tmp/requirements.txt \