# ============================================================
# SepsisIntel AI
# Executive Insights & Recommendations Center
# ============================================================

import streamlit as st

st.set_page_config(
    page_title="Executive Insights & Recommendations",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Executive Insights & Recommendations")

st.subheader(
    "Strategic Clinical AI Findings and Actionable Recommendations"
)

st.markdown("---")

# ============================================================
# EXECUTIVE INSIGHTS
# ============================================================

st.markdown("## Executive Insights")

st.info("""
• Sepsis prevalence was **2.19%**, representing **4,267 septic hours**
across **194,835 ICU hourly observations**, confirming sepsis as a
low-frequency but high-impact clinical event.

• The Operational XGBoost model achieved **69.1% recall** and
**90.2% accuracy**, successfully identifying approximately
**7 in 10 septic events**.

• ICU Length of Stay (**ICULOS**) emerged as the strongest predictor
of sepsis risk, highlighting the importance of prolonged ICU exposure.

• Age was the second most influential predictor, indicating elevated
vulnerability among older ICU patients.

• Key physiological drivers included Heart Rate(65), Respiratory Rate(60),
Mean Arterial Pressure(55), emphasizing the role of cardiopulmonary instability
in sepsis development.

• Oxygen Saturation (38) and Temperature (35 remained important contributors,
reinforcing the significance of hypoxemia and fever in sepsis surveillance.

        
• Governance validation demonstrated that removing ICULOS reduced
recall from **69.1% to 60.0%** while retaining **86.8%**
of predictive capability,demonstrating meaningful clinical signal beyond operational variables.

• Explainable AI analysis confirmed that model predictions were
driven by clinically plausible variables, supporting transparency
and responsible AI adoption.
""")

# ============================================================
# STRATEGIC RECOMMENDATIONS
# ============================================================

st.markdown("## Strategic Recommendations")

st.success("""
### Recommended Actions

• Prioritize recall (sensitivity) over accuracy to minimize
missed septic deterioration.

• Deploy the Operational XGBoost model as a clinical decision
support and ICU surveillance tool.

• Implement risk escalation protocols at ICU exposure thresholds
such as 24, 48, and 72 hours.

• Establish enhanced surveillance pathways for patients aged
65 years and older.

• Integrate automated alerts for:

    - HR > 100 bpm
    - Respiratory Rate > 22/min
    - MAP < 65 mmHg
    - Oxygen Saturation < 92%
    - Temperature > 38°C

• Use the Governance XGBoost model as a Responsible AI benchmark
for transparency and validation.

• Incorporate SHAP explainability outputs into clinical workflows
to improve clinician trust.

• Conduct external validation and monitor model drift,
alert burden, predictive performance, and patient safety outcomes.

• Position SepsisIntel AI as an enterprise platform for:

    - Early Sepsis Detection
    - ICU Surveillance
    - Clinical Decision Support
    - Healthcare Intelligence
    - Responsible AI Governance
""")

# ============================================================
# EXECUTIVE CONCLUSION
# ============================================================

st.markdown("## Executive Conclusion")

st.warning("""
SepsisIntel AI successfully transformed 194,835 ICU observations
into an explainable, governance-aware Clinical AI platform.

The Operational XGBoost model achieved 69.1% recall, while the
Governance Model retained 60.0% recall without ICU length-of-stay
dependency.

These findings support the platform's use as an ICU surveillance
and clinical decision-support system while maintaining transparency,
accountability, and responsible AI principles.
""")

st.markdown("---")

st.caption(
    "SepsisIntel AI | Executive Insights & Recommendations Center"
)