
import json
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, Field

ROOT = Path(__file__).resolve().parents[2]
MODEL_PATH = ROOT / "artifacts" / "model.joblib"

app = FastAPI(title="AI381 Lab 3 Churn API")

model = joblib.load(MODEL_PATH)
METADATA_PATH = ROOT / "artifacts" / "metadata.json"
with open(METADATA_PATH, encoding="utf-8") as f:
    metadata = json.load(f)


class Customer(BaseModel):
    model_config = ConfigDict(extra="forbid")

    tenure_months: int = Field(ge=0)
    monthly_charges: float = Field(ge=0)
    support_calls: int = Field(ge=0)
    contract: str
    internet_service: str


@app.get("/health")
def health():
    return {
        "status": "ok",
        "model_version": metadata["model_version"],
        "mlflow_run_id": metadata["mlflow_run_id"],
    }


@app.post("/predict")
def predict(customer: Customer):
    data = customer.model_dump()

    X = pd.DataFrame([data])

    probability = float(model.predict_proba(X)[0, 1])

    return {"churn_probability": round(probability, 3)}
