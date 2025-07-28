FROM python:3.10-slim

# Install MLflow
RUN pip install --no-cache-dir mlflow

# Create folders for artifacts
RUN mkdir -p /mlflow/artifacts


# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Expose MLflow's default port
EXPOSE 5000



# # Run MLflow with local SQLite and artifact store
# CMD ["mlflow", "server", \
#      "--backend-store-uri=sqlite:////mlflow_data/mlflow.db", \
#      "--default-artifact-root=/mlflow/artifacts", \
#      "--host=0.0.0.0", \
#      "--port=5000"]