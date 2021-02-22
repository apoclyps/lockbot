FROM python:3.9.2-alpine

RUN apk update && \
    apk upgrade && \
    apk add git

    ENV DOCKERIZE_VERSION v0.6.1
    RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
        && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
        && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add requirements
RUN pip install --no-cache-dir pipenv
COPY Pipfile Pipfile.lock /usr/src/app/
RUN pipenv install --deploy --dev --ignore-pipfile --system

COPY . .
