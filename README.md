# 🏥 SepsisIntel AI

### Enterprise Clinical Sepsis Early Warning, Explainable AI & Responsible Governance Platform

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?style=for-the-badge&logo=streamlit)
![XGBoost](https://img.shields.io/badge/XGBoost-Production_Model-green?style=for-the-badge)
![Healthcare AI](https://img.shields.io/badge/Healthcare-AI-blueviolet?style=for-the-badge)
![Explainable AI](https://img.shields.io/badge/Explainable-AI-orange?style=for-the-badge)
![Responsible AI](https://img.shields.io/badge/Responsible-AI-success?style=for-the-badge)
![Clinical Intelligence](https://img.shields.io/badge/Clinical-Intelligence-darkgreen?style=for-the-badge)
![Digital Health](https://img.shields.io/badge/Digital-Health_Transformation-teal?style=for-the-badge)

---

## 🚀 Live Application

[🔗 Launch SepsisIntel AI](https://sepsisintel-ai-ccjyevamxsnsy9slhtmdh6.streamlit.app/)

---

## Executive Overview

SepsisIntel AI is an enterprise-grade Clinical AI platform designed to support early sepsis detection, ICU surveillance, clinical decision support, Explainable AI, and Responsible AI Governance.

Built using over **194,000 ICU hourly observations**, the platform transforms complex clinical and operational data into actionable intelligence for clinicians, healthcare leaders, and digital health stakeholders.

The solution integrates:

- Clinical Intelligence
- Predictive AI
- Early Warning Analytics
- Explainable AI (SHAP)
- Responsible AI Governance
- Executive Reporting
- Strategic Decision Support

into a unified healthcare intelligence ecosystem.

---

## Business Challenge

Sepsis remains one of the most significant causes of morbidity, mortality, and healthcare expenditure worldwide.

Healthcare organizations continue to face challenges related to:

- Delayed sepsis recognition
- Clinical deterioration
- ICU resource utilization
- Alert fatigue
- Model transparency
- Responsible AI deployment

Traditional rule-based approaches often lack predictive capability and may fail to identify high-risk patients early enough for timely intervention.

SepsisIntel AI addresses these challenges through explainable machine learning and governance-aware clinical intelligence.

---

## Platform Capabilities

### 🏠 Home Center

Executive platform overview and enterprise healthcare AI positioning.

### 📊 Executive Command Center

- ICU surveillance intelligence
- Sepsis burden analytics
- Model performance monitoring
- Operational KPI tracking

### 🩺 Clinical Intelligence Center

- Clinical driver analysis
- Biomarker intelligence
- Sepsis risk factor exploration
- Population health insights

### 🚨 Clinical Sepsis Prediction Engine

- Real-time sepsis prediction
- XGBoost risk scoring
- Clinical decision support
- Risk stratification

### 🧠 Explainable AI Intelligence Center

- SHAP-based explainability
- Clinical feature attribution
- Model transparency
- Prediction interpretability

### 🛡️ Responsible AI Governance Center

- Leakage assessment
- Governance validation
- Model risk register
- Responsible AI monitoring

### 📑 Executive Reporting Center

- Strategic reporting
- Model findings
- Executive summaries
- Deployment recommendations

### 📈 Executive Insights & Recommendations Center

- Executive-level findings
- Strategic healthcare recommendations
- Operational improvement opportunities
- Responsible AI guidance

---

## Dataset Overview

| Metric | Value |
|----------|----------:|
| ICU Hourly Observations | 194,835 |
| Septic Hours | 4,267 |
| Sepsis Prevalence | 2.19% |
| Patient Encounters | 40,336+ |
| Prediction Target | Sepsis Early Warning |

Dataset Source:

PhysioNet 2019 Sepsis Challenge Dataset

---

## Model Performance

### Operational XGBoost Model

| Metric | Value |
|----------|----------:|
| Accuracy | 90.2% |
| Precision | 14.2% |
| Recall | 69.1% |
| F1 Score | 23.5% |

### Governance XGBoost Model

| Metric | Value |
|----------|----------:|
| Recall | 60.0% |
| Governance Retention | 86.8% |

The operational model successfully identified approximately **7 out of every 10 septic events**, demonstrating meaningful clinical utility as an ICU surveillance tool.

---

## Explainable AI

SHAP analysis identified the most influential drivers of sepsis risk:

1. ICU Length of Stay (ICULOS)
2. Age
3. Heart Rate
4. Respiratory Rate
5. Mean Arterial Pressure
6. Oxygen Saturation
7. Temperature

Explainability analysis confirmed that model behavior aligns with established clinical understanding of sepsis physiology and deterioration patterns.

---

## Responsible AI Governance

The platform incorporates Responsible AI principles through:

- Explainability validation
- Leakage assessment
- Governance model comparison
- Clinical interpretability review
- Risk register documentation
- Deployment limitation disclosure

A secondary Governance XGBoost model was developed excluding ICU Length of Stay to assess feature dependency and model robustness.

---

# Platform Screenshots

## Executive Sepsis Surveillance Dashboard

![Executive Sepsis Surveillance Dashboard](Screenshots/executive_sepsis_surveillance_dashboard.png)

---

## Clinical Sepsis Prediction Engine

![Clinical Sepsis Prediction Engine](Screenshots/clinical_sepsis_prediction_engine.png)

---

## Explainable AI Intelligence Center

![Explainable AI Intelligence Center](Screenshots/explainable_ai_intelligence_center.png)

---

## Executive Insights

- Sepsis prevalence was **2.19%**, representing **4,267 septic hours across 194,835 ICU hourly observations**, confirming sepsis as a low-frequency but high-impact clinical event.

- The Operational XGBoost model achieved **69.1% recall and 90.2% accuracy**, successfully identifying approximately **7 in 10 septic events** and demonstrating strong early-warning capability.

- ICU Length of Stay (**ICULOS**) was the strongest predictor of sepsis risk, highlighting the importance of prolonged ICU exposure as a clinical risk factor.

- Age emerged as the second most influential predictor, indicating elevated vulnerability among older ICU patients.

- Key physiological drivers included **Heart Rate (65)**, **Respiratory Rate (60)**, and **Mean Arterial Pressure (55)**, emphasizing the role of cardiopulmonary instability in sepsis development.

- Oxygen Saturation (**38**) and Temperature (**35**) remained important contributors, reinforcing the significance of hypoxemia and fever in sepsis surveillance.

- Governance validation showed that removing ICULOS reduced recall from **69.1% to 60.0%**, while retaining **86.8% of predictive performance**.

- Explainable AI analysis confirmed that model predictions were driven by clinically plausible factors, supporting transparency, interpretability, and responsible AI adoption.

---

## Strategic Recommendations

- Prioritize recall (sensitivity) over accuracy when evaluating sepsis detection systems.

- Deploy the Operational XGBoost model as a clinical decision support and ICU surveillance tool.

- Implement risk escalation protocols at ICU exposure thresholds of 24, 48, and 72 hours.

- Establish enhanced surveillance pathways for patients aged 65 years and older.

- Integrate automated alerts for:
  - HR > 100 bpm
  - Respiratory Rate > 22/min
  - MAP < 65 mmHg
  - Oxygen Saturation < 92%
  - Temperature > 38°C

- Use the Governance XGBoost model as a Responsible AI benchmark for transparency reviews and validation exercises.

- Incorporate SHAP explainability outputs into clinical workflows.

- Conduct external validation and ongoing monitoring for model drift, alert burden, predictive performance, and patient safety outcomes.

---

## Technology Stack

- Python
- Pandas
- NumPy
- XGBoost
- Scikit-Learn
- SHAP
- Plotly
- Streamlit
- Joblib

---

## Project Structure

```text
Clinical_Sepsis_Intelligence_System/

│
├── app.py
│
├── assets/
│   ├── executive_sepsis_surveillance_dashboard.png
│   ├── clinical_sepsis_prediction_engine.png
│   └── explainable_ai_intelligence_center.png
│
├── models/
│   ├── xgb_operational.pkl
│   └── xgb_governance.pkl
│
├── pages/
│   ├── 1_Executive_Command_Center.py
│   ├── 2_Clinical_Intelligence_Center.py
│   ├── 3_Sepsis_Risk_Prediction_Center.py
│   ├── 4_Explainable_AI_Center.py
│   ├── 5_Responsible_AI_Governance_Center.py
│   ├── 6_Executive_Reporting_Center.py
│   └── 7_Executive_Insights_Recommendations.py
│
├── notebooks/
│   └── 01_data_exploration.ipynb
│
├── requirements.txt
│
└── README.md
```

### Architecture Overview

* **app.py** – Main Streamlit application entry point.
* **assets/** – Platform screenshots and README visual assets.
* **models/** – Serialized production XGBoost models used for inference.
* **pages/** – Multi-page Streamlit application modules supporting executive intelligence, prediction, explainability, governance, and reporting.
* **notebooks/** – Data exploration, feature engineering, model development, and experimentation workflows.
* **requirements.txt** – Project dependencies for deployment and reproducibility.
* **README.md** – Project documentation, executive overview, deployment instructions, and portfolio showcase.

```

## Future Enhancements

- External validation on independent ICU datasets
- Real-time EHR integration
- FHIR interoperability
- Clinical workflow integration
- Drift monitoring dashboards
- Prospective clinical evaluation

---

## Author

### Samuel Israel, MD

Healthcare AI Engineer | Clinical AI Specialist | Digital Health Transformation Strategist | Explainable AI & Responsible AI Advocate

**LinkedIn:** www.linkedin.com/in/dr-samuel-israel-90893b228

---

## Disclaimer

This platform was developed for educational, research, and portfolio demonstration purposes.

It is not intended for real-world clinical diagnosis, treatment, or patient management. Any clinical deployment would require extensive external validation, regulatory review, governance oversight, and prospective evaluation.

---

### ⭐ If you found this project valuable, please consider starring the repository.