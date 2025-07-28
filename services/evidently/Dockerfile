FROM python:3.10-slim

WORKDIR /app

# System dependencies for building Python packages
RUN apt-get update && \
    apt-get install -y gcc python3-dev libffi-dev build-essential curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*


# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --prefer-binary -r requirements.txt

# Copy app files
COPY . .

EXPOSE 8000

CMD ["uvicorn", "evidently.ui.app:app", "--host", "0.0.0.0", "--port", "8000"]
