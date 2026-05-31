# ============================================================
# SepsisIntel AI
# Responsible AI Governance Center
# ============================================================

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Responsible AI Governance Center",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Responsible AI Governance Center")
st.subheader("Model Transparency, Leakage Review, Clinical Safety & Governance Validation")

st.markdown("---")

# ============================================================
# GOVERNANCE OVERVIEW
# ============================================================

st.info("""
This center documents the responsible AI governance process applied during
development of the SepsisIntel AI Clinical Sepsis Early Warning Platform.
It highlights model limitations, leakage investigation, governance validation,
and deployment-readiness considerations.
""")

# ============================================================
# MODEL GOVERNANCE COMPARISON
# ============================================================

st.markdown("## Model Governance Comparison")

governance_df = pd.DataFrame({
    "Model": [
        "Patient-Level Random Forest",
        "Hourly Random Forest",
        "Hourly XGBoost Operational",
        "Hourly XGBoost Governance"
    ],
    "ICULOS Included": [
        "Yes - Max_ICULOS",
        "Yes - Current ICULOS",
        "Yes - Current ICULOS",
        "No"
    ],
    "Accuracy (%)": [
        96.0,
        93.2,
        90.2,
        82.8
    ],
    "Precision (%)": [
        95.7,
        13.7,
        14.2,
        7.5
    ],
    "Recall (%)": [
        59.5,
        39.3,
        69.1,
        60.0
    ],
    "Governance Interpretation": [
        "High performance but potential future-information leakage",
        "Hourly model with real-time ICU context",
        "Operational production candidate",
        "Governance-compliant clinical model"
    ]
})

st.dataframe(governance_df, use_container_width=True)

fig = px.bar(
    governance_df,
    x="Model",
    y="Recall (%)",
    color="ICULOS Included",
    title="Recall Performance Across Governance Scenarios"
)

fig.update_layout(
    xaxis_title="Model",
    yaxis_title="Recall (%)",
    height=500
)

st.plotly_chart(fig, use_container_width=True)

# ============================================================
# LEAKAGE ASSESSMENT
# ============================================================

st.markdown("## Data Leakage Assessment")

col1, col2 = st.columns(2)

with col1:
    st.error("""
    ### Leakage Risk Identified

    The initial patient-level Random Forest model used **Max_ICULOS**.

    This variable may represent future information because maximum ICU length
    of stay is only fully known after the ICU encounter ends.

    This created a potential data leakage risk.
    """)

with col2:
    st.success("""
    ### Governance Mitigation

    A second governance-compliant model was developed excluding ICULOS.

    The model retained **60.0% recall**, demonstrating that physiological
    and laboratory features still carried meaningful predictive signal.
    """)

# ============================================================
# RESPONSIBLE AI PRINCIPLES
# ============================================================

st.markdown("## Responsible AI Principles Applied")

principles = pd.DataFrame({
    "Principle": [
        "Clinical Validity",
        "Explainability",
        "Leakage Review",
        "Class Imbalance Awareness",
        "Human Oversight",
        "Deployment Limitation",
        "Monitoring Requirement"
    ],
    "Implementation": [
        "Features aligned with sepsis physiology and ICU monitoring",
        "SHAP analysis used to identify clinical drivers",
        "ICULOS dependency investigated and governance model created",
        "Recall prioritized over accuracy due to rare-event sepsis detection",
        "Tool positioned as clinical decision support, not autonomous diagnosis",
        "External validation required before real-world use",
        "Future monitoring needed for drift, alert burden, and safety"
    ]
})

st.dataframe(principles, use_container_width=True)

# ============================================================
# MODEL RISK REGISTER
# ============================================================

st.markdown("## Model Risk Register")

risk_register = pd.DataFrame({
    "Risk": [
        "False Positives",
        "False Negatives",
        "Dataset Shift",
        "Feature Leakage",
        "Alert Fatigue",
        "Limited External Validation"
    ],
    "Potential Impact": [
        "Increased clinician workload",
        "Missed septic deterioration",
        "Reduced performance in new hospitals",
        "Overestimated model performance",
        "Reduced trust and workflow burden",
        "Limited generalizability"
    ],
    "Mitigation Strategy": [
        "Tune alert threshold and monitor precision",
        "Prioritize recall and clinical escalation review",
        "Monitor drift and retrain periodically",
        "Maintain governance review and feature audit",
        "Integrate human review and alert prioritization",
        "Validate on external ICU datasets before deployment"
    ]
})

st.dataframe(risk_register, use_container_width=True)

# ============================================================
# GOVERNANCE CONCLUSION
# ============================================================

st.markdown("## Governance Conclusion")

st.success("""
The governance review demonstrated that SepsisIntel AI is not presented as a
black-box clinical prediction tool. The project includes model comparison,
feature dependency assessment, leakage investigation, explainability analysis,
and deployment limitation documentation.

The Operational XGBoost model is recommended for ICU surveillance workflows,
while the Governance XGBoost model provides a more conservative clinical AI
baseline excluding ICU length-of-stay context.
""")

st.markdown("---")
st.caption("SepsisIntel AI | Responsible AI Governance Center")