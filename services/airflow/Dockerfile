FROM apache/airflow:2.10.4-python3.11

# Switch to root to install any additional packages if needed
USER root

# Install any additional system packages here if needed
# RUN apt-get update && apt-get install -y <package-name>


# Set environment variables
ENV PYTHONPATH="/app"


USER airflow
# Install any additional Python packages if needed
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy your DAGs (optional)
COPY dags/ /opt/airflow/dags/

# Copy your source code (for PythonOperator imports)
# COPY src/ /app/src/

# Copy entrypoint script and make it executable
USER root
COPY --chown=airflow:airflow entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8080

# Switch back to airflow user
USER airflow

ENTRYPOINT ["/entrypoint.sh"]


#docker run -d   --name airflow   -p 8080:8080   -v $(pwd)/dags:/opt/airflow/dags   -v $(pwd)/data:/opt/airflow/data   airflow
