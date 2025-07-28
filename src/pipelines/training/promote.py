from mlflow import MlflowClient


def promote_model(model_name="SP500_Model", stage="Production"):
    client = MlflowClient()
    latest_version = client.get_latest_versions(model_name, stages=["None"])[0]

    client.transition_model_version_stage(
        name=model_name,
        version=latest_version.version,
        stage=stage,
        archive_existing_versions=True,
    )

    print(f"✅ Model version {latest_version.version} promoted to {stage}")
