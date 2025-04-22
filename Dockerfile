# Pull base image
FROM python:3.10.12-alpine

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk update && apk add --no-cache nodejs npm postgresql-dev

# Set work directory
WORKDIR /code

# Install dependencies
COPY ./production.txt .
RUN pip install -r production.txt

# Copy project
COPY . .