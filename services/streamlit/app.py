import streamlit as st
import requests
import os

st.set_page_config(page_title="Stock Prediction", layout="centered")

st.title("📈 S&P 500 Prediction")

API_URL = os.getenv("API_URL", "http://localhost:9000")

try:
    response = requests.get(f"{API_URL}/predict")
    data = response.json()
    st.metric(label=f"Prediction for {data['symbol']}", value=f"${data['prediction']}")
except Exception as e:
    st.error(f"Failed to fetch prediction: {e}")
