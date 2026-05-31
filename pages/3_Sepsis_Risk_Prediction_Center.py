# ============================================================
# SepsisIntel AI
# Sepsis Risk Prediction Center
# ============================================================

import os
import joblib
import numpy as np
import pandas as pd
import streamlit as st

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Sepsis Risk Prediction Center",
    page_icon="🚨",
    layout="wide"
)

# ============================================================
# LOAD PRODUCTION MODEL
# ============================================================

MODEL_PATH = "models/xgb_operational.pkl"

@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        st.error("Production model not found. Please confirm models/xgb_operational.pkl exists.")
        st.stop()

    return joblib.load(MODEL_PATH)

model = load_model()

# ============================================================
# PAGE HEADER
# ============================================================

st.title("🚨 Sepsis Risk Prediction Center")

st.subheader(
    "Real-Time Clinical Sepsis Risk Scoring Using the Operational XGBoost Engine"
)

st.markdown("---")

st.info("""
This module uses the production Operational XGBoost model to estimate sepsis risk
from hourly ICU clinical observations. The output is intended for portfolio,
analytics, and clinical AI demonstration purposes only.
""")

# ============================================================
# INPUT FORM
# ============================================================

st.markdown("## Patient Clinical Inputs")

with st.form("sepsis_prediction_form"):

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age", min_value=18.0, max_value=100.0, value=65.0)
        gender = st.selectbox("Gender", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
        hr = st.number_input("Heart Rate (HR)", min_value=30.0, max_value=220.0, value=105.0)
        resp = st.number_input("Respiratory Rate", min_value=5.0, max_value=70.0, value=24.0)
        map_value = st.number_input("Mean Arterial Pressure (MAP)", min_value=20.0, max_value=180.0, value=75.0)

    with col2:
        sbp = st.number_input("Systolic Blood Pressure (SBP)", min_value=40.0, max_value=250.0, value=120.0)
        o2sat = st.number_input("Oxygen Saturation (O2Sat)", min_value=40.0, max_value=100.0, value=95.0)
        temp = st.number_input("Temperature (°C)", min_value=30.0, max_value=43.0, value=37.5)
        bun = st.number_input("BUN", min_value=1.0, max_value=200.0, value=20.0)
        creatinine = st.number_input("Creatinine", min_value=0.1, max_value=20.0, value=1.0)

    with col3:
        wbc = st.number_input("WBC", min_value=0.1, max_value=100.0, value=12.0)
        lactate = st.number_input("Lactate", min_value=0.1, max_value=30.0, value=1.9)
        platelets = st.number_input("Platelets", min_value=1.0, max_value=1000.0, value=250.0)
        iculos = st.number_input("ICU Length of Stay Hour (ICULOS)", min_value=1.0, max_value=500.0, value=24.0)

        lactate_missing = st.selectbox(
            "Was Lactate Missing?",
            options=[0, 1],
            format_func=lambda x: "No" if x == 0 else "Yes"
        )

    submit = st.form_submit_button("Generate Sepsis Risk Prediction")

# ============================================================
# FEATURE ENGINEERING
# ============================================================

if submit:

    input_df = pd.DataFrame([{
        "HR": hr,
        "O2Sat": o2sat,
        "Temp": temp,
        "SBP": sbp,
        "MAP": map_value,
        "Resp": resp,
        "WBC": wbc,
        "Lactate": lactate,
        "Creatinine": creatinine,
        "BUN": bun,
        "Platelets": platelets,
        "Age": age,
        "Gender": gender,
        "ICULOS": iculos,
        "HR_Missing": 0,
        "O2Sat_Missing": 0,
        "Temp_Missing": 0,
        "SBP_Missing": 0,
        "MAP_Missing": 0,
        "Resp_Missing": 0,
        "WBC_Missing": 0,
        "Lactate_Missing": lactate_missing,
        "Creatinine_Missing": 0,
        "BUN_Missing": 0,
        "Platelets_Missing": 0
    }])

    expected_features = list(model.get_booster().feature_names)

    input_df = input_df[expected_features]

    probability = model.predict_proba(input_df)[0][1]
    prediction = model.predict(input_df)[0]

    # ========================================================
    # RISK STRATIFICATION
    # ========================================================

    if probability < 0.20:
        risk_level = "Low Risk"
        alert_type = "success"
    elif probability < 0.50:
        risk_level = "Moderate Risk"
        alert_type = "warning"
    else:
        risk_level = "High Risk"
        alert_type = "error"

    st.markdown("---")
    st.markdown("## Prediction Result")

    colA, colB, colC = st.columns(3)

    colA.metric("Sepsis Probability", f"{probability * 100:.2f}%")
    colB.metric("Risk Level", risk_level)
    colC.metric("Model Output", "Sepsis" if prediction == 1 else "Non-Sepsis")

    if alert_type == "success":
        st.success("Low predicted sepsis risk based on current clinical inputs.")
    elif alert_type == "warning":
        st.warning("Moderate sepsis risk detected. Clinical review may be appropriate.")
    else:
        st.error("High sepsis risk detected. Urgent clinical review recommended.")

    st.markdown("## Input Summary")
    st.dataframe(input_df, use_container_width=True)

# ============================================================
# DISCLAIMER
# ============================================================

st.markdown("---")

st.warning("""
Clinical Disclaimer: This application is a portfolio-grade Clinical AI demonstration.
It is not intended for real-world clinical diagnosis, treatment, or patient management.
Any clinical deployment would require external validation, regulatory review,
clinical governance, monitoring, and prospective evaluation.
""")

st.caption("SepsisIntel AI | Sepsis Risk Prediction Center")