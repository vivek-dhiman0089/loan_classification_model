#!/usr/bin/env python3
"""
Streamlit Frontend for Simple Loan Default Predictor
Designed by Vishal Dhiman
"""

import streamlit as st
import pandas as pd
import math
import random
import plotly.express as px

# -----------------------------
# Model parameters (same as backend)
# -----------------------------
COEFFICIENTS = {
    'age': 0.0393,
    'campaign': -0.2032,
    'pdays': -0.2790,
    'previous': 0.1427,
    'contact_cellular': 0.4383,
    'month_mar': 0.1977,
    'month_oct': 0.1847,
    'default_no': 0.1843,
    'job_management': -0.0175,
    'job_technician': -0.0091,
    'marital_married': -0.0181,
    'education_university.degree': 0.0540,
    'housing_no': 0.0093,
    'loan_no': 0.0198
}

INTERCEPT = -0.3273
OPTIMAL_THRESHOLD = 0.6

# -----------------------------
# Prediction Function
# -----------------------------
def predict_loan_default(features):
    score = INTERCEPT
    for f, coef in COEFFICIENTS.items():
        score += coef * features.get(f, 0)
    probability = 1 / (1 + math.exp(-score))
    prediction = 1 if probability > OPTIMAL_THRESHOLD else 0

    if probability < 0.2:
        risk_level = "Low Risk"
        color = "green"
    elif probability < 0.5:
        risk_level = "Medium Risk"
        color = "gold"
    elif probability < 0.8:
        risk_level = "High Risk"
        color = "orange"
    else:
        risk_level = "Very High Risk"
        color = "red"

    recommendation = "REVIEW / REJECT" if prediction == 1 else "APPROVE"
    return probability, risk_level, recommendation, color

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Loan Default Risk Predictor", page_icon="💰", layout="centered")

st.title("💼 Loan Default Risk Predictor")
st.caption("A lightweight rule-based model designed by Vishal Dhiman")

st.markdown("---")

# Sidebar info
st.sidebar.header("📊 Model Parameters")
st.sidebar.write(f"**Intercept:** {INTERCEPT}")
st.sidebar.write(f"**Optimal Threshold:** {OPTIMAL_THRESHOLD}")
st.sidebar.write("**Top Influencing Features:**")
for k, v in list(COEFFICIENTS.items())[:5]:
    st.sidebar.write(f"- {k}: {v:+.3f}")

# User input form
st.subheader("🧍‍♂️ Applicant Information")
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 18, 100, 35)
    campaign = st.number_input("Number of Contacts (Campaign)", 0, 50, 2)
    pdays = st.number_input("Days Since Last Contact", -1, 999, 999)
    previous = st.number_input("Previous Contacts", 0, 20, 0)

with col2:
    contact_cellular = st.checkbox("Contacted by Cellular", value=True)
    job_management = st.checkbox("Job: Management")
    job_technician = st.checkbox("Job: Technician")
    marital_married = st.checkbox("Marital Status: Married")
    education_university = st.checkbox("Education: University Degree")

st.subheader("🏠 Financial Factors")
col3, col4 = st.columns(2)

with col3:
    housing_no = st.checkbox("No Housing Loan", value=True)
    loan_no = st.checkbox("No Personal Loan", value=True)
with col4:
    default_no = st.checkbox("No Previous Default", value=True)
    month_mar = st.checkbox("Application Month: March")
    month_oct = st.checkbox("Application Month: October")

# Prepare features
features = {
    'age': age,
    'campaign': campaign,
    'pdays': pdays,
    'previous': previous,
    'contact_cellular': 1 if contact_cellular else 0,
    'month_mar': 1 if month_mar else 0,
    'month_oct': 1 if month_oct else 0,
    'default_no': 1 if default_no else 0,
    'job_management': 1 if job_management else 0,
    'job_technician': 1 if job_technician else 0,
    'marital_married': 1 if marital_married else 0,
    'education_university.degree': 1 if education_university else 0,
    'housing_no': 1 if housing_no else 0,
    'loan_no': 1 if loan_no else 0
}

# Prediction button
if st.button("🔮 Predict Risk"):
    prob, risk, rec, color = predict_loan_default(features)

    st.markdown("---")
    st.markdown(f"### 🧠 Prediction Result")
    st.markdown(f"**Probability of Default:** {prob:.1%}")
    st.markdown(f"**Risk Level:** :{color}[{risk}]")
    st.markdown(f"**Recommendation:** :blue-background[{rec}]")

    # Visual gauge
    fig = px.bar(
        x=[prob],
        y=["Default Probability"],
        orientation='h',
        range_x=[0, 1],
        color_discrete_sequence=[color],
        text=[f"{prob:.1%}"]
    )
    fig.update_layout(
        height=200,
        xaxis_title="Probability",
        yaxis_title=None,
        showlegend=False,
        plot_bgcolor="rgba(0,0,0,0)"
    )
    st.plotly_chart(fig, use_container_width=True)

    # Business advice
    st.markdown("### 💬 Business Advice")
    if prob < 0.3:
        st.info("Low risk — approve with standard terms ✅")
    elif prob < 0.6:
        st.warning("Moderate risk — consider approval with monitoring ⚠️")
    else:
        st.error("High risk — request collateral or reject ❌")

# Footer
st.markdown("---")
st.caption("© 2025 Vishal Dhiman | Simple Loan Risk Predictor")