from src.pipelines.training.evaluate import evaluate_model


def test_evaluation_pass():
    assert evaluate_model(10, threshold=50)


def test_evaluation_fail():
    assert not evaluate_model(100, threshold=50)
