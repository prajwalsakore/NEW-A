import streamlit as st

st.title("Subscription Plans")

plans = {
    "Free": "Basic access to content generation. Limited to 5 uses per day.",
    "Pro": "Unlimited content generation. Priority support.",
    "Premium": "Pro features + Early access to new tools."
}

choice = st.selectbox("Select a plan to see details", list(plans.keys()))
st.info(plans[choice])
