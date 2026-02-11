import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

def page_predict_electricity_cost_body():
    
    st.write("### 🔌 Electricity Cost Prediction")

    st.info(
        "This page allows the user to estimate the expected monthly electricity" \
        "cost for a site based on its operational and environmental characteristics."
    )

    st.write("---")

    version = "v1"
    model_path=f"outputs/ml_pipeline/electricity_cost/{version}"

    model = joblib.load(f"{model_path}/random_forest_model.pkl")
    model_features = joblib.load(f"{model_path}/model_features.pkl")

    st.success("Model and feature list loaded successfully.")

    if st.checkbox("Show model features (debug)"):
        st.write(model_features)
