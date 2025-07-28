from src.pipelines.inference.predict_sp500_trend import predict_next_5_days
from datetime import datetime, timedelta
from airflow.sensors.external_task import ExternalTaskSensor
from airflow.operators.python import PythonOperator
from airflow import DAG
import sys

sys.path.append("/app")

default_args = {"owner": "airflow", "retries": 1, "retry_delay": timedelta(minutes=2)}

with DAG(
    dag_id="predict_sp500_dag",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["prediction", "sp500"],
) as dag:

    wait_for_training = ExternalTaskSensor(
        task_id="wait_for_training",
        external_dag_id="train_sp500_dag",
        external_task_id="promote_model",
        allowed_states=["success", "skipped"],
        mode="poke",
        poke_interval=30,
        timeout=600,
    )

    predict_task = PythonOperator(
        task_id="predict_next_5_days",
        python_callable=predict_next_5_days,
        execution_timeout=timedelta(minutes=5),
        retries=1,
        retry_delay=timedelta(minutes=2),
    )

    # wait_for_training >> predict_task
    predict_task
