# Dockerfile for the web app AND task worker

FROM python:alpine

# set work dir
RUN mkdir /app
WORKDIR /app

# copy reqs
ADD ./requirements.txt /app/requirements.txt

# install reqs in first layer (for efficiency)
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# copy project files
COPY . /app

