
import joblib
import pytest
from fastapi.testclient import TestClient

from src.app.main import app, MODEL_PATH

client = TestClient(app)

VALID_CUSTOMER = {
    "tenure_months": 35,
    "monthly_charges": 85.0,
    "support_calls": 2,
    "contract": "month-to-month",
    "internet_service": "fiber",
}


def test_api_contract():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_model_loads():
    model = joblib.load(MODEL_PATH)
    assert hasattr(model, "predict_proba")


def test_input_schema():
    customer = VALID_CUSTOMER.copy()
    customer["tenure_months"] = -1

    response = client.post("/predict", json=customer)
    assert response.status_code == 422


def test_edge_case():
    customer = VALID_CUSTOMER.copy()
    customer["tenure_months"] = 0
    customer["support_calls"] = 0

    response = client.post("/predict", json=customer)
    assert response.status_code == 200
    assert 0 <= response.json()["churn_probability"] <= 1


def test_deterministic_prediction():
    response1 = client.post("/predict", json=VALID_CUSTOMER)
    response2 = client.post("/predict", json=VALID_CUSTOMER)

    assert response1.status_code == 200
    assert response2.status_code == 200
    assert response1.json() == response2.json()
