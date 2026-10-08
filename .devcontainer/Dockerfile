FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

# Python dependencies
COPY requirements-codespaces.txt /tmp/requirements-codespaces.txt

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /tmp/requirements-codespaces.txt

WORKDIR /workspaces