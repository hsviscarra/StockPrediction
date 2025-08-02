from fastapi import FastAPI
from api.routers import predictions

app = FastAPI()
app.include_router(predictions.router)
