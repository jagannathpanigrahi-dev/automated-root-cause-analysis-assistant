from pydantic import BaseModel


class LogRequest(BaseModel):
    message: str


class PredictionResponse(BaseModel):
    root_cause: str
    confidence: float