from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)


def test_predict_status_code():
    response = client.get("/predict")
    assert response.status_code == 200


def test_predict_endpoint_data():
    response = client.get("/predict")
    data = response.json()

    assert "symbol" in data
    assert "prediction" in data
    assert data["symbol"] == "SP500"
    assert isinstance(data["prediction"], float)
