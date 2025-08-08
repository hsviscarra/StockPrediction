from fastapi import FastAPI
from api.routers import predictions, health

app = FastAPI()
app.include_router(predictions.router)
app.include_router(health.router)
