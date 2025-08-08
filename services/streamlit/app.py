import streamlit as st
import requests
import os
import time

st.set_page_config(page_title="Stock Prediction", layout="centered")

st.title("📈 S&P 500 Prediction")

API_URL = os.getenv("API_URL", "http://localhost:9000")


def fetch_prediction_with_retry(max_retries=3):
    for attempt in range(max_retries):
        try:
            # First try health check
            health_response = requests.get(f"{API_URL}/health", timeout=10)
            if health_response.status_code == 200:
                st.success("✅ API is healthy")

            # Then fetch prediction
            response = requests.get(f"{API_URL}/predict", timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if attempt == max_retries - 1:
                st.error(f"❌ Failed to connect to API after {max_retries} attempts")
                st.error(f"Error: {e}")
                st.info(f"Trying to connect to: {API_URL}")
                return None
            else:
                st.warning(f"⚠️ Attempt {attempt + 1} failed, retrying...")
                time.sleep(2)
    return None


data = fetch_prediction_with_retry()
if data:
    st.metric(label=f"Prediction for {data['symbol']}", value=f"${data['prediction']}")
