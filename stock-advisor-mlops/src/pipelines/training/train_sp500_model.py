import pandas as pd
import mlflow
import os
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from dotenv import load_dotenv

load_dotenv()


def train_sp500_model(
    experiment_name="SP500 Prediction Experiment",
    model_name="SP500_Model",
    artifact_location="/opt/airflow/data/mlflow_artifacts",
):

    mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))

    os.makedirs(artifact_location, exist_ok=True)

    try:
        mlflow.create_experiment(
            name=experiment_name, artifact_location=artifact_location
        )
    except mlflow.exceptions.MlflowException:
        # Experiment already exists; no problem
        pass

    mlflow.set_experiment(experiment_name)

    # Load data
    df = pd.read_csv("/opt/airflow/data/sp500.csv", parse_dates=["Date"])

    df = df.sort_values("Date").reset_index(drop=True)

    # Create lag features (simple example)
    df["Close_Lag1"] = df["Close"].shift(1)
    df["Close_Lag2"] = df["Close"].shift(2)
    df["Close_Lag3"] = df["Close"].shift(3)
    df.dropna(inplace=True)

    X = df[["Close_Lag1", "Close_Lag2", "Close_Lag3"]]
    y = df["Close"]

    model = LinearRegression()

    with mlflow.start_run() as run:
        model.fit(X, y)
        preds = model.predict(X)
        mse = mean_squared_error(y, preds)

        # Log to MLflow
        mlflow.log_param("model_type", "LinearRegression")
        mlflow.log_metric("mse", mse)

        # Register the model in MLflow Model Registry
        mlflow.sklearn.log_model(
            sk_model=model,
            artifact_path="sp500_model",
            registered_model_name="SP500_Model",
        )

        run_id = run.info.run_id

        print(f"✅ Model trained with MSE={mse:.4f}, run_id={run_id}")

    return run_id, mse

    # Save model
    # model_path = "/opt/airflow/data/models/sp500_model.joblib"
    # os.makedirs(os.path.dirname(model_path), exist_ok=True)
    # dump(model, model_path)
    # mlflow.log_artifact(model_path)

    # print(f"✅ Model trained. MSE: {mse:.4f}. Saved to: {model_path}")
