# ============================================================
# SepsisIntel AI
# Enterprise Clinical Sepsis Early Warning,
# Explainable AI & Governance Intelligence Platform
# ============================================================

import streamlit as st

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="SepsisIntel AI",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.image(
    "https://img.icons8.com/color/96/hospital-3.png",
    width=80
)

st.sidebar.title("SepsisIntel AI")

st.sidebar.markdown("""
Enterprise Clinical Sepsis Early Warning,
Explainable AI & Governance Intelligence Platform
""")

st.sidebar.markdown("---")

st.sidebar.success(
    "Production Models Loaded"
)

# ============================================================
# HEADER
# ============================================================

st.title(
    "🏠 SepsisIntel AI Home"
)

st.subheader(
    "Enterprise Clinical Sepsis Early Warning, Explainable AI & Governance Intelligence Platform"
)

st.markdown("---")

# ============================================================
# EXECUTIVE OVERVIEW
# ============================================================

st.markdown("""
### Executive Overview

SepsisIntel AI is an enterprise healthcare AI platform designed to support:

- Early sepsis detection
- Clinical decision support
- ICU surveillance
- Explainable AI
- Responsible AI governance
- Executive healthcare intelligence

The platform integrates machine learning, clinical analytics,
operational intelligence, and model governance into a unified
healthcare AI ecosystem.
""")

# ============================================================
# PLATFORM CAPABILITIES
# ============================================================

st.markdown("## Platform Capabilities")

col1, col2, col3 = st.columns(3)

with col1:

    st.info("""
    ### Clinical Intelligence

    - Vital Sign Analytics
    - Biomarker Intelligence
    - Risk Stratification
    - Clinical Surveillance
    """)

with col2:

    st.info("""
    ### Predictive AI

    - XGBoost Sepsis Engine
    - Early Warning Detection
    - Risk Probability Scoring
    - Clinical Decision Support
    """)

with col3:

    st.info("""
    ### Responsible AI

    - SHAP Explainability
    - Model Transparency
    - Governance Validation
    - Leakage Assessment
    """)

# ============================================================
# MODEL PERFORMANCE
# ============================================================

st.markdown("## Production Model Performance")

metric1, metric2, metric3 = st.columns(3)

metric1.metric(
    "Operational Recall",
    "69.1%"
)

metric2.metric(
    "Governance Recall",
    "60.0%"
)

metric3.metric(
    "Sepsis Prevalence",
    "2.19%"
)

# ============================================================
# PROJECT SUMMARY
# ============================================================

st.markdown("---")

st.markdown("""
### Project Highlights

- 194,835 ICU Hourly Observations
- 4,267 Septic Hours Identified
- XGBoost Early Warning Engine
- SHAP Explainability Framework
- Responsible AI Governance Validation
- Streamlit Enterprise Deployment

Developed as an advanced healthcare AI solution for clinical intelligence,
operational surveillance, and early sepsis detection.
""")

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "SepsisIntel AI | Enterprise Clinical AI Platform | Samuel Israel"
)