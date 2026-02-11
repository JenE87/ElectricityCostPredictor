import streamlit as st
import pandas as pd

def page_predict_electricity_cost_body():
    
    st.write("### 🔌 Electricity Cost Predictor")

    st.info(
        "This page allows the user to estimate the expected monthly electricity" \
        "cost for a site based on its operational and environmental characteristics."
    )

    st.write("---")