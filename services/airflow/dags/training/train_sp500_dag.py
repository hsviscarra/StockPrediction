from datetime import datetime, timedelta
from airflow.sensors.external_task import ExternalTaskSensor
from airflow.operators.python import PythonOperator
from airflow import DAG
import sys

sys.path.append("/app")


default_args = {"owner": "airflow", "retries": 1, "retry_delay": timedelta(minutes=1)}


def train_task(experiment_name, **context):
    from src.pipelines.training.train_sp500_model import train_sp500_model

    run_id, mse = train_sp500_model(experiment_name=experiment_name)

    # Pass values to next task using XCom
    context["ti"].xcom_push(key="run_id", value=run_id)
    context["ti"].xcom_push(key="mse", value=mse)


def evaluate_task(threshold, **context):
    from src.pipelines.training.evaluate import evaluate_model

    mse = context["ti"].xcom_pull(key="mse", task_ids="train_model")

    if evaluate_model(mse, threshold):
        return "promote_model"
    else:
        print("❌ Model not promoted: Evaluation failed.")
        return "end_pipeline"


def promote_task(**context):
    from src.pipelines.training.promote import promote_model

    promote_model(model_name="SP500_Model", stage="Production")


with DAG(
    dag_id="train_and_promote_sp500_dag",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["training", "sp500"],
) as dag:

    wait_for_ingestion = ExternalTaskSensor(
        task_id="wait_for_ingestion",
        external_dag_id="sp500_data_ingestion_dag",
        external_task_id="fetch_sp500_data",
        mode="poke",
        poke_interval=30,
        timeout=600,
    )

    train_model = PythonOperator(
        task_id="train_model",
        python_callable=train_task,
        op_kwargs={"experiment_name": "SP500 Prediction Experiment_v1.0"},
    )

    evaluate = PythonOperator(
        task_id="evaluate_model",
        python_callable=evaluate_task,
        op_kwargs={"threshold": 50},
    )

    promote = PythonOperator(task_id="promote_model", python_callable=promote_task)

    end_pipeline = PythonOperator(
        task_id="end_pipeline",
        python_callable=lambda: print("Pipeline finished without promotion."),
    )

    # Define flow with branching behavior
    wait_for_ingestion >> train_model >> evaluate
    evaluate >> promote
    evaluate >> end_pipeline
