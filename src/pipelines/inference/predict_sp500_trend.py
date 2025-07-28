import pandas as pd
from datetime import timedelta
import numpy as np
import mlflow.sklearn
import logging


def predict_next_5_days():

    logging.basicConfig(level=logging.INFO)

    data_path = "/opt/airflow/data/sp500.csv"
    out_path = "/opt/airflow/data/sp500_predictions.csv"

    model = mlflow.sklearn.load_model("models:/SP500_Model/Production")

    df = pd.read_csv(data_path, parse_dates=["Date"])
    df = df.sort_values("Date").reset_index(drop=True)

    # Create lag features from the latest row
    last = df.iloc[-3:]["Close"].values  # last 3 days
    input_data = last[::-1].reshape(1, -1)  # Flip order to [Lag1, Lag2, Lag3]

    # Predict 5 days forward
    future_dates = []
    future_preds = []

    for i in range(5):
        pred = model.predict(input_data)[0]
        future_preds.append(pred)
        input_data = np.roll(input_data, -1)
        input_data[0, -1] = pred  # append pred as new lag

        next_day = df["Date"].max() + timedelta(days=i + 1)
        future_dates.append(next_day)

    output_df = pd.DataFrame({"Date": future_dates, "Predicted_Close": future_preds})

    output_df.to_csv(out_path, index=False)
    logging.info(f"✅ 5-day forecast saved to {out_path}")
