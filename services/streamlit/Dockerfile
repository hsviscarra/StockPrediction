FROM python:3.9-slim

# Environment settings
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Set working directory
WORKDIR /app

# Install system dependencies (needed for scikit-learn, etc.)
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Optional: Create a non-root user (good practice)
RUN useradd -m -s /bin/bash streamlit

# Copy your Streamlit app
COPY . /app
RUN chown -R streamlit:streamlit /app

# Switch to the non-root user
USER streamlit

# Expose Streamlit's default port
EXPOSE 8501

# Healthcheck (Streamlit’s internal endpoint)
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1

# Start Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]