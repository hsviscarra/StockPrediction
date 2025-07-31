import streamlit as st
import requests

st.set_page_config(page_title="Stock Prediction", layout="centered")

st.title("📈 S&P 500 Prediction")

try:
    response = requests.get("http://api:8000/predict")
    data = response.json()
    st.metric(label=f"Prediction for {data['symbol']}", value=f"${data['prediction']}")
except Exception as e:
    st.error(f"Failed to fetch prediction: {e}")
