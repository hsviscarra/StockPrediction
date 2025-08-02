from src.data.ingestion.fetch_dgppot import fetch_gdppot_data
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from airflow import DAG
import sys

sys.path.append("/app/src")


print("PYTHONPATH:", sys.path)

# Optional (unused here, can remove unless needed)
# import yfinance as yf
# import time

# DAG default arguments
default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
}

# Define the DAG
with DAG(
    dag_id="fetch_gdppot_data",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["fred", "economic-data"],
) as dag:

    fetch_gdppot_task = PythonOperator(
        task_id="fetch_gdppot_data", python_callable=fetch_gdppot_data
    )
