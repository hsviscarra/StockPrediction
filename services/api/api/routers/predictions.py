from fastapi import APIRouter
from ..models.schemas import PredictionResult
import random

router = APIRouter()


@router.get("/predict", response_model=PredictionResult)
def get_prediction():
    return {"symbol": "SP500", "prediction": round(random.uniform(4300, 4600), 2)}
