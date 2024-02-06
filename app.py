# app.py
import streamlit as st
from transformers import pipeline

summarizer = pipeline("summarization", model="hussainBurhan/my_article_model2")

def main():
    st.title("Text Summarization App")

    # Input textarea
    user_input = st.text_area("Enter your text here:", "")

    # Summarization button
    if st.button("Generate Summary"):
        if user_input:
            summary = summarizer(user_input, max_length=150, min_length=50, length_penalty=2.0, num_beams=4)
            st.subheader("Generated Summary:")
            st.write(summary[0]['summary_text'])
        else:
            st.warning("Please enter text for summarization.")

if __name__ == "__main__":
    main()
