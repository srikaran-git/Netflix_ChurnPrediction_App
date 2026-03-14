import streamlit as st
import requests

st.title("Netflix Churn Prediction App")

age = st.number_input("Age")
salary_k = st.number_input("Salary (k)")
tenure_years = st.number_input("Tenure (years)")
number_of_logins = st.number_input("Number of logins")
complaints = st.number_input("Complaints")
engagement_score = st.number_input("Engagement Score")
Years_from_signup = st.number_input("Years from signup")
days_from_last_active_day = st.number_input("Days from last active day")
region = st.selectbox("Region", ['Canada', 'Germany', 'India', 'UK', 'USA'])
device_type = st.selectbox("Device Type", ['Mobile', 'Smart TV', 'Web'])

if st.button("Predict"):

    data = {
        "age": age,
        "salary_k": salary_k,
        "tenure_years": tenure_years,
        "number_of_logins": number_of_logins,
        "complaints": complaints,
        "engagement_score": engagement_score,
        "Years_from_signup": Years_from_signup,
        "days_from_last_active_day": days_from_last_active_day,
        "region": region,
        "device_type": device_type
    }

    response = requests.post("http://127.0.0.1:8000/predict", json=data)

    result = response.json()

    st.success(f"Prediction: {'Churn' if result['churn_prediction'] == 1 else 'Not Churn'}")