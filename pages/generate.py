import streamlit as st
from openai import OpenAI

# Set page config
st.set_page_config(page_title="AI Content Generator", page_icon="🧠")

# Title
st.title("🧠 AI Content Generator")
st.markdown("Generate blog ideas, full blogs, emails, and social media captions with AI!")

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Content type selector
content_type = st.selectbox("What would you like to generate?", ["Blog Ideas", "Full Blog", "Marketing Email", "Social Media Caption", "Video Scripts"])

# Topic input
topic = st.text_input("Enter your topic:", placeholder="e.g., Digital Marketing Tips")

# Submit button
if st.button("Generate"):
    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Generating content..."):
            if content_type == "Blog Ideas":
                prompt = f"Give me 5 creative blog post ideas on the topic: {topic}."
            elif content_type == "Full Blog":
                prompt = f"Write a detailed blog post on the topic: {topic}. Include headings and make it informative."
            elif content_type == "Marketing Email":
                prompt = f"Write a marketing email promoting a service or product related to: {topic}. Make it professional and engaging."
            elif content_type == "Social Media Caption":
                prompt = f"Write a catchy social media caption for a post about: {topic}. Include emojis and hashtags."

            # OpenAI API call
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that creates content."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=800
            )

            output = response.choices[0].message.content
            st.subheader("✨ Generated Content")
            st.write(output)

