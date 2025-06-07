import streamlit as st
from pages import utils

st.set_page_config(page_title="Content Generator", layout="centered")

st.title("AI Content Generator & Subscription Portal")

# User input form
with st.form("user_info_form"):
    name = st.text_input("Enter your name")
    email = st.text_input("Enter your email")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.success(f"Welcome, {name}!")
        utils.store_user_info(name, email)
        st.session_state["user_email"] = email
        st.session_state["user_name"] = name

st.markdown("---")
st.subheader("Select a feature from the left sidebar to continue")
