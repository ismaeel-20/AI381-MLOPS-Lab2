
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field, ConfigDict


ROOT = Path(__file__).resolve().parents[2]
MODEL_PATH = ROOT / "model.joblib"

app = FastAPI(title="AI381 Lab 2 Churn API")

model = joblib.load(MODEL_PATH)


class Customer(BaseModel):
    model_config = ConfigDict(extra="forbid")

    tenure_months: int = Field(ge=0)
    monthly_charges: float = Field(ge=0)
    support_calls: int = Field(ge=0)
    contract: str
    internet_service: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(customer: Customer):
    data = customer.model_dump()

    # Map the request field to the v2 training feature
    data["monthly_fee"] = data.pop("monthly_charges")

    X = pd.DataFrame([data])

    probability = float(model.predict_proba(X)[0, 1])

    return {"churn_probability": round(probability, 3)}
