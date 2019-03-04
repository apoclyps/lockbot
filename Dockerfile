FROM python:3.7-alpine

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add requirements
RUN pip install --no-cache-dir pipenv
COPY Pipfile Pipfile.lock /usr/src/app/
RUN pipenv install --deploy --dev --ignore-pipfile --system

COPY . .
