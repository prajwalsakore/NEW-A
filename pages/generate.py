import streamlit as st
import openai
import os

st.title("Generate Content Ideas")

topic = st.text_input("Enter a topic or niche")

if st.button("Generate Ideas"):
    if not topic:
        st.warning("Please enter a topic.")
    else:
        openai.api_key = st.secrets["OPENAI_API_KEY"]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a creative assistant that gives 5 unique content ideas."},
                {"role": "user", "content": f"Give me 5 content creation ideas for {topic}"}
            ]
        )
        ideas = response.choices[0].message.content
        st.markdown("### Here are some ideas:")
        st.markdown(ideas)
