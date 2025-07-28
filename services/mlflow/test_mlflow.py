import mlflow

mlflow.set_tracking_uri("http://localhost:5001")

experiment_name = "test-experiment"
mlflow.set_experiment(experiment_name)

with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_metric("accuracy", 0.95)

print("✅ Run logged successfully!")
