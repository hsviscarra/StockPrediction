#!/bin/bash

# Wait for database to be ready
# echo "Waiting for database to be ready..."
# while ! nc -z ${DB_HOST:-localhost} ${DB_PORT:-5432}; do
#     sleep 1
# done

# echo "Database is ready!"

set -e
# Initialize MLflow database

# Start MLflow server
exec mlflow server \
    --host 0.0.0.0 \
    --port 5000 \
    --backend-store-uri ${MLFLOW_BACKEND_STORE_URI} \
    --default-artifact-root ${MLFLOW_DEFAULT_ARTIFACT_ROOT} \
    --workers 4