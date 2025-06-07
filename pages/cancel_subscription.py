import streamlit as st

st.title("Cancel Subscription")

email = st.session_state.get("user_email", "")

if email:
    st.warning(f"Your subscription for {email} will be marked as canceled.")
    st.success("Subscription canceled (simulated for demo).")
else:
    st.error("Please enter your email on the Home page first.")
