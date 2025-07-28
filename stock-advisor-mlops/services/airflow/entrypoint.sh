#!/bin/bash
set -e

if [ "$1" = "webserver" ]; then
    echo "Initializing Airflow DB..."
    airflow db upgrade

    echo "Creating admin user (if not exists)..."
    airflow users create \
        --username admin \
        --password admin \
        --firstname Admin \
        --lastname Admin \
        --role Admin \
        --email admin@example.com || true

    echo "Starting Airflow webserver..."
    exec airflow webserver
elif [ "$1" = "scheduler" ]; then
    echo "Starting Airflow scheduler..."
    exec airflow scheduler
else
    # Default: run whatever command was passed
    exec "$@"
fi