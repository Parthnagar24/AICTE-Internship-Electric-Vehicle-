
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from chatbot_service import get_chatbot_response

st.set_page_config(page_title="EV-Insight", layout="centered")

BASE = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE, "model", "ev_range_model.pkl")
DATA_PATH = os.path.join(BASE, "data", "ev_dataset.csv")

st.title("EV-Insight — EV Range Predictor + Chatbot")

tabs = st.tabs(["Range Predictor", "Chatbot", "Dataset & Model"])

with tabs[0]:
    st.header("Predict EV Range")
    battery = st.slider("Battery percentage (%)", 0, 100, 80)
    speed = st.number_input("Speed (km/h)", min_value=0.0, max_value=200.0, value=60.0)
    temp = st.number_input("Ambient temperature (°C)", min_value=-30.0, max_value=60.0, value=25.0)
    if st.button("Predict Range"):
        if os.path.exists(MODEL_PATH):
            model = joblib.load(MODEL_PATH)
            X = pd.DataFrame([[battery, speed, temp]], columns=["battery_percent","speed_kmh","temperature_c"])
            pred = model.predict(X)[0]
            st.success(f"Predicted range: {pred:.1f} km")
        else:
            st.error("Model not found. Please run `python model_train.py` to train and save the model.")

with tabs[1]:
    st.header("EV Chatbot (powered by OpenAI or fallback)")
    user_input = st.text_input("Ask a question about EVs", "")
    if st.button("Send"):
        if user_input.strip():
            with st.spinner("Getting answer..."):
                ans = get_chatbot_response(user_input)
            st.markdown("**Assistant:**")
            st.write(ans)
        else:
            st.warning("Please type a question first.")

with tabs[2]:
    st.header("Dataset & Model")
    st.subheader("Sample Dataset (first rows)")
    df = pd.read_csv(DATA_PATH)
    st.dataframe(df)
    st.write("Model file location:", MODEL_PATH)
    if st.button("Retrain model now"):
        st.info("Training model — this may take a few seconds.")
        import subprocess, sys
        subprocess.run([sys.executable, os.path.join(BASE, "model_train.py")])
        st.success("Training complete. Reload the page if needed.")
