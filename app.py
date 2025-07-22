import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("C:\\Users\\91810\\linear_model.pkl")  # Adjust path as needed

# Page config
st.set_page_config(
    page_title="E-Commerce Spending Predictor",
    layout="centered",
    page_icon="🛍️"
)

# CSS with white text
st.markdown("""
    <style>
        html, body, .main {
            background-color: #ffffff;
            color: white;
        }
        .main-card {
            background-color: #292966;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 6px 20px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
            color: white;
            font-weight: bold;
            font-size: 36px;
            margin-bottom: 0.2em;
        }
        h3 {
            text-align: center;
            color: white;
            font-weight: 500;
            font-size: 20px;
            margin-bottom: 1.5em;
        }
        label, .stNumberInput label {
            font-weight: 600;
            color: white !important;
        }
        .stNumberInput > div {
            background-color: #444476;
            border: 2px solid #A3A3CC;
            border-radius: 10px;
            color: white;
        }
        .stButton button {
            background-color: #5C5C99;
            color: white;
            font-weight: bold;
            font-size: 16px;
            border: none;
            border-radius: 8px;
            padding: 0.6rem 1.2rem;
        }
        .stButton button:hover {
            background-color: #292966;
            color: white;
        }
        .result {
            text-align: center;
            font-size: 22px;
            font-weight: bold;
            color: white;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# ---- UI Starts ----
st.markdown("<h1>Yearly Revenue Estimator for Online Customers</h1>", unsafe_allow_html=True)
st.markdown("<h3>Enter customer usage details to predict yearly spending</h3>", unsafe_allow_html=True)

st.markdown('<div class="main-card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    membership_length = st.number_input("📆 Length of Membership (Years)", min_value=0.0, max_value=6.0, value=3.0, step=0.1)
    session_length = st.number_input("🕒 Avg. Session Length (Minutes)", min_value=20.0, max_value=40.0, value=30.0, step=0.5)

with col2:
    app_time = st.number_input("📱 Time on App (Minutes)", min_value=0.0, max_value=20.0, value=10.0, step=0.5)
    website_time = st.number_input("💻 Time on Website (Minutes)", min_value=0.0, max_value=20.0, value=10.0, step=0.5)

# Predict Button
if st.button("🔍 Predict Spending"):
    input_data = np.array([[1, website_time, app_time, membership_length, session_length]])
    prediction = model.predict(input_data)[0]
    st.markdown(f"<div class='result'> Estimated Yearly Spending: <strong>${prediction:,.2f}</strong></div>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
