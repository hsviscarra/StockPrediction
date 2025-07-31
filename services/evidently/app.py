from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
from monitor import generate_report

app = FastAPI()


@app.on_event("startup")
def on_startup():
    generate_report()


@app.get("/")
def root():
    return {"message": "Evidently Service is running!"}


@app.get("/report.html")
def serve_report():
    report_path = os.path.join(os.getcwd(), "report.html")
    if os.path.exists(report_path):
        return FileResponse(report_path, media_type="text/html")
    return {"detail": "Report not found"}
