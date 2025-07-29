import pandas as pd
from unittest.mock import patch, MagicMock
from src.pipelines.training.train_sp500_model import train_sp500_model


@patch("src.pipelines.training.train_sp500_model.os.makedirs")
@patch("src.pipelines.training.train_sp500_model.pd.read_csv")
@patch("src.pipelines.training.train_sp500_model.mlflow")
def test_train_model_outputs(mock_mlflow, mock_read_csv, mock_makedirs):
    # Mock CSV input data
    df = pd.DataFrame(
        {
            "Date": pd.date_range(start="2020-01-01", periods=5),
            "Close": [100, 102, 101, 103, 104],
        }
    )
    mock_read_csv.return_value = df

    # Mock MLflow components
    mock_run = MagicMock()
    mock_run.info.run_id = "test_run_id"
    mock_mlflow.start_run.return_value.__enter__.return_value = mock_run

    # Call function
    run_id, mse = train_sp500_model()

    # Assertions
    assert run_id == "test_run_id"
    assert isinstance(mse, float)
    assert 0 <= mse < 1.0

    # Validate mocks used
    mock_read_csv.assert_called_once()
    mock_mlflow.log_param.assert_called_with("model_type", "LinearRegression")
    mock_mlflow.log_metric.assert_called()
    mock_mlflow.sklearn.log_model.assert_called()
