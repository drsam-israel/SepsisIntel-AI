# ============================================================
# SepsisIntel AI
# Executive Command Center
# ============================================================

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="Executive Command Center | SepsisIntel AI",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Executive Command Center")
st.subheader("Enterprise ICU Sepsis Surveillance & Clinical AI Performance Overview")

st.markdown("---")

# ============================================================
# Executive KPIs
# ============================================================

total_icu_hours = 194_835
septic_hours = 4_267
non_septic_hours = 190_568
sepsis_rate = 2.19
operational_recall = 69.1
governance_recall = 60.0

kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

kpi1.metric("ICU Hourly Records", f"{total_icu_hours:,}")
kpi2.metric("Septic Hours", f"{septic_hours:,}")
kpi3.metric("Sepsis Rate", f"{sepsis_rate}%")
kpi4.metric("Operational Recall", f"{operational_recall}%")
kpi5.metric("Governance Recall", f"{governance_recall}%")

st.markdown("---")

# ============================================================
# Executive Summary
# ============================================================

st.markdown("""
### Executive Intelligence Summary

SepsisIntel AI analyzed **194,835 ICU hourly observations** derived from the PhysioNet Sepsis Challenge dataset.

The production candidate **Hourly XGBoost Operational Model** achieved **69.1% recall**, while the governance-compliant model excluding ICU length-of-stay achieved **60.0% recall**.

This establishes a clinically meaningful early-warning foundation while preserving transparency around model governance, feature dependency, and deployment limitations.
""")

# ============================================================
# Model Comparison
# ============================================================

st.markdown("## Model Performance Comparison")

model_data = pd.DataFrame({
    "Model": [
        "Patient RF with Leakage Risk",
        "Hourly Random Forest",
        "Hourly XGBoost Operational",
        "Hourly XGBoost Governance"
    ],
    "Accuracy": [96.0, 93.2, 90.2, 82.8],
    "Precision": [95.7, 13.7, 14.2, 7.5],
    "Recall": [59.5, 39.3, 69.1, 60.0],
    "F1 Score": [73.3, 20.3, 23.5, 13.3]
})

st.dataframe(model_data, use_container_width=True)

fig = go.Figure()

fig.add_trace(go.Bar(
    x=model_data["Model"],
    y=model_data["Recall"],
    name="Recall"
))

fig.add_trace(go.Bar(
    x=model_data["Model"],
    y=model_data["F1 Score"],
    name="F1 Score"
))

fig.update_layout(
    title="Model Recall and F1 Score Comparison",
    xaxis_title="Model",
    yaxis_title="Performance (%)",
    barmode="group",
    height=500
)

st.plotly_chart(fig, use_container_width=True)

# ============================================================
# Operational Intelligence
# ============================================================

st.markdown("## Operational Intelligence")

col1, col2 = st.columns(2)

with col1:
    st.info("""
    ### Operational Model

    The operational model includes ICU length-of-stay context and achieved the strongest recall.

    **Best use case:**
    - ICU surveillance
    - Early warning monitoring
    - Hospital operations intelligence
    """)

with col2:
    st.warning("""
    ### Governance Model

    The governance model excludes ICU length-of-stay and relies only on clinical and laboratory variables.

    **Best use case:**
    - Responsible AI review
    - Clinical transparency
    - Model governance validation
    """)

# ============================================================
# Executive Recommendations
# ============================================================

st.markdown("## Executive Recommendations")

st.success("""
1. Use the Operational XGBoost model for ICU-level surveillance and early-warning workflows.
2. Use the Governance XGBoost model for model transparency, responsible AI validation, and clinical review.
3. Continue external validation before real-world deployment.
4. Monitor recall, false positives, alert burden, and model drift over time.
""")

st.markdown("---")
st.caption("SepsisIntel AI | Executive Clinical AI Command Center")