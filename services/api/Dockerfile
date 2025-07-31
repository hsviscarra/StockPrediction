FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# ✅ Set PYTHONPATH so 'api' is importable
ENV PYTHONPATH=/app

# ✅ Launch FastAPI app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9000"]