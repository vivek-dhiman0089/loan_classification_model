# loan_classification_model
A machine learning model that classifies applicants based on whether thay will pay back loan or not
# 💼 Simple Loan Default Risk Predictor

A lightweight **rule-based loan default prediction web app** built using **Streamlit** and **Plotly**.  
This app estimates the probability that a loan applicant will default, based on key demographic and financial features.

Developed by **Vishal Dhiman** as part of an AI & Machine Learning internship project.

---

## 🚀 Features

- 🧠 **Rule-Based Logistic Model:** No external ML libraries — uses manually defined coefficients.
- 🎨 **Interactive Streamlit UI:** Intuitive input forms and color-coded risk levels.
- 📊 **Visual Risk Gauge:** Displays default probability using a dynamic bar chart.
- 💬 **Actionable Recommendations:** Suggests whether to approve, monitor, or reject an applicant.
- 🪶 **Lightweight & Offline:** Runs entirely locally — no database or API needed.

---

## 🧩 Tech Stack

| Component | Technology |
|------------|-------------|
| Frontend UI | [Streamlit](https://streamlit.io) |
| Visualization | [Plotly](https://plotly.com/python/) |
| Language | Python 3.9+ |
| Model Type | Custom Logistic Scoring Function (Rule-based) |

---

## 📂 Project Structure

loan-default-predictor/
│
├── simple_loan_frontend.py # Streamlit frontend app
├── loan_detection.csv # Optional dataset (for demo/testing)
├── requirements.txt # Python dependencies
└── README.md # Project documentation
