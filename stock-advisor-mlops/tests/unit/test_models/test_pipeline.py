from src.pipelines.training.train_sp500_model import train_sp500_model
from src.pipelines.training.evaluate import evaluate_model
from src.pipelines.training.register import register_model


def test_pipeline_flow():
    run_id, mse = train_sp500_model()

    if evaluate_model(mse, threshold=50):
        register_model(run_id)
    else:
        assert mse > 50
