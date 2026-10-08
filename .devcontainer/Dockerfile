FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

ENV DEBIAN_FRONTEND=noninteractive

# JDK 21
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        wget \
        procps \
        netcat-openbsd \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Python dependencies
COPY requirements-codespaces.txt /tmp/requirements-codespaces.txt

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /tmp/requirements-codespaces.txt

WORKDIR /workspaces