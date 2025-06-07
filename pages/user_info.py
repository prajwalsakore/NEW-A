import streamlit as st
from pages import utils

st.title("Your Info")

email = st.session_state.get("user_email", None)
name = st.session_state.get("user_name", None)

if not email:
    st.error("Please enter your name and email on the Home page first.")
else:
    st.markdown(f"**Name:** {name}")
    st.markdown(f"**Email:** {email}")
    st.markdown("**Status:** Active")
