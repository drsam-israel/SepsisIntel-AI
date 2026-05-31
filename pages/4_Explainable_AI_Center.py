# ============================================================
# SepsisIntel AI
# Explainable AI Center
# ============================================================

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Explainable AI Center",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Explainable AI Center")
st.subheader("Model Transparency, SHAP Intelligence & Clinical Feature Drivers")

st.markdown("---")

st.info("""
This center translates model behavior into clinically interpretable intelligence.
It summarizes the major feature drivers identified during SHAP analysis of the
Hourly XGBoost Clinical Sepsis Engine.
""")

# ============================================================
# SHAP FEATURE DRIVER SUMMARY
# ============================================================

st.markdown("## Top Model Drivers")

feature_drivers = pd.DataFrame({
    "Feature": [
        "ICULOS",
        "Age",
        "Heart Rate",
        "Respiratory Rate",
        "Mean Arterial Pressure",
        "Gender",
        "Oxygen Saturation",
        "Temperature",
        "Systolic Blood Pressure",
        "Temperature Missing"
    ],
    "Clinical Interpretation": [
        "Current ICU length-of-stay context strongly influenced risk scoring",
        "Older age increased predicted sepsis risk",
        "Higher heart rate increased predicted sepsis risk",
        "Higher respiratory rate increased predicted sepsis risk",
        "Lower MAP reflected hemodynamic instability",
        "Gender contributed modest predictive signal",
        "Lower oxygen saturation increased predicted risk",
        "Higher temperature increased predicted risk",
        "Blood pressure instability contributed to prediction",
        "Missingness pattern carried clinical workflow signal"
    ],
    "Relative Importance": [
        100,
        75,
        65,
        60,
        55,
        40,
        38,
        35,
        30,
        25
    ]
})

st.dataframe(feature_drivers, use_container_width=True)

fig = px.bar(
    feature_drivers.sort_values("Relative Importance"),
    x="Relative Importance",
    y="Feature",
    orientation="h",
    title="Explainable AI Feature Driver Ranking",
    text="Relative Importance"
)

fig.update_traces(textposition="outside")

fig.update_layout(
    height=600,
    xaxis_title="Relative Importance Score",
    yaxis_title="Clinical Feature"
)

st.plotly_chart(fig, use_container_width=True)

# ============================================================
# CLINICAL INTERPRETATION
# ============================================================

st.markdown("## Clinical Interpretation of Model Behavior")

col1, col2 = st.columns(2)

with col1:
    st.success("""
    ### Physiological Risk Drivers

    The model identified classic sepsis-related physiological patterns:

    - Tachycardia
    - Tachypnea
    - Hypoxemia
    - Fever
    - Hemodynamic instability

    These patterns align with clinical sepsis surveillance principles.
    """)

with col2:
    st.warning("""
    ### Governance Signal

    ICULOS was the strongest model driver.

    This is clinically useful for operational surveillance, but it requires governance review because ICU time context may influence model behavior.

    A second governance model was developed excluding ICULOS.
    """)

# ============================================================
# MISSINGNESS INTELLIGENCE
# ============================================================

st.markdown("## Missingness Intelligence")

st.info("""
Healthcare AI models often learn not only from measured values, but also from
whether specific values were missing. Missingness can reflect clinical workflows,
test-ordering behavior, and severity suspicion.

In this project, missingness indicators such as Temp_Missing, SBP_Missing,
MAP_Missing, and Lactate_Missing contributed to model explainability.
""")

# ============================================================
# EXECUTIVE EXPLAINABILITY SUMMARY
# ============================================================

st.markdown("## Executive Explainability Summary")

st.success("""
The Explainable AI analysis demonstrated that the SepsisIntel AI model is not
a black-box predictor. Its outputs are driven by clinically plausible factors
including age, heart rate, respiratory rate, oxygen saturation, blood pressure,
temperature, and laboratory/workflow patterns.

This supports responsible clinical AI adoption by making model behavior more
transparent, auditable, and interpretable.
""")

st.markdown("---")
st.caption("SepsisIntel AI | Explainable AI Center")