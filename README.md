
# AI381 Lab 2 — Containerized Churn Prediction API

[![CI](https://github.com/ismaeel-20/AI381-MLOPS-Lab2/actions/workflows/ci.yml/badge.svg)](https://github.com/ismaeel-20/AI381-MLOPS-Lab2/actions/workflows/ci.yml)

## Overview

A customer churn prediction service built using Logistic Regression, FastAPI, Docker, and GitHub Actions.

The model is trained using `churn_v2.csv`.

## Run with one command

Requires Docker.

```bash
docker run --rm -p 8000:8000 ghcr.io/ismaeel-20/ai381-mlops-lab2:70315126febd3439b2043ffe83c91653949c0e74
```

## API Endpoints

- `GET /health` — Returns the health status.
- `POST /predict` — Returns the customer's churn probability.

Example prediction request:

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"tenure_months":35,"monthly_charges":85,"support_calls":2,"contract":"month-to-month","internet_service":"fiber"}'
```

## Local Testing

```bash
python -m pip install -r requirements.txt -r requirements-dev.txt
python -m pytest -v tests/
python -m ruff check src/ tests/
```

## CI/CD Pipeline

GitHub Actions automatically:

1. Runs Ruff and five pytest tests on pull requests.
2. Builds the Docker image on `main`.
3. Scans the image using Trivy.
4. Publishes it to GitHub Container Registry with a commit SHA tag.

## Published Docker Image

Registry: GitHub Container Registry (GHCR)

Image digest:

`sha256:0d39f39bef95f745068a85f57e0d740a4c2a713d3e53d2da39fbfa0b725f4489`

## Model Performance

- F1 Score: 0.587
- AUC: 0.792

## Author

Ismail Alzyout — AI381 Machine Learning Operations
