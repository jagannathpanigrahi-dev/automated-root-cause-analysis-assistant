from fastapi import FastAPI

from app.schemas import LogRequest, PredictionResponse
from app.predictor import predict_root_cause

app = FastAPI(
    title="Automated Root Cause Analysis API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Automated Root Cause Analysis API"
    }


@app.post("/predict", response_model=PredictionResponse)
def predict(request: LogRequest):

    result = predict_root_cause(request.message)

    return PredictionResponse(
        root_cause=result["root_cause"],
        confidence=result["confidence"]
    )

