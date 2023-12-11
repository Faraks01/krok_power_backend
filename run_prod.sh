#!/bin/bash

if [[ -z "${EMAIL_HOST_USER}" ]]; then
  echo "Enter an email host user"
  read EMAIL_HOST_USER
fi

if [[ -z "${EMAIL_HOST_PASSWORD}" ]]; then
  echo "Enter an email host password"
  read EMAIL_HOST_PASSWORD
fi

# Stopping running server instance if exists
PID=$(lsof -t -i:8000)

if [ -n "${PID}" ]; then
    echo "Stopping instance at pid: $PID"
    sudo kill -9 $PID
fi

# Run server at background
echo "Starting server on 0.0.0.0:8000"
DEBUG=False EMAIL_HOST_USER=$EMAIL_HOST_USER EMAIL_HOST_PASSWORD=$EMAIL_HOST_PASSWORD nohup python3 manage.py runserver 0.0.0.0:8000 > /dev/null 2>&1&