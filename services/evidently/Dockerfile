FROM python:3.10-slim

WORKDIR /app

# 🔧 Add build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    build-essential \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files (if using scripts or monitoring setup)
COPY . .

# ✅ Set PYTHONPATH
ENV PYTHONPATH=/app

# Expose default port
EXPOSE 8008

# 📡 Start the service (adjust for Streamlit or FastAPI)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
