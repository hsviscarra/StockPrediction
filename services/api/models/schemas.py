from pydantic import BaseModel


class PredictionResult(BaseModel):
    symbol: str
    prediction: float
