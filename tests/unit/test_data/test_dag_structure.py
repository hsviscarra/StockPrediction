import pytest
from airflow.models import DagBag


@pytest.fixture(scope="module")
def dagbag():
    return DagBag(dag_folder="services/airflow/dags", include_examples=False)


def test_dag_import(dagbag):
    assert dagbag.dags is not None
    assert len(dagbag.import_errors) == 0, f"DAG import errors: {dagbag.import_errors}"


def test_training_dag_loaded(dagbag):
    dag_id = "train_and_promote_sp500_dag"
    assert dag_id in dagbag.dags
    dag = dagbag.get_dag(dag_id)
    assert dag is not None
    assert len(dag.tasks) > 0
