import streamlit as st
import requests
from text_preprocessing import preprocess_text

# Set the Flask API endpoint
API_URL = "http://127.0.0.1:5000/predict"

# Streamlit app
st.set_page_config(page_title="Sentiment Predictor", layout="centered")
st.title("📊 Sentiment Analysis App")
st.markdown("Enter a review to predict its sentiment (Positive, Neutral, Negative).")

# Input text box
user_input = st.text_area("✍️ Enter your review here:", height=150)

# Predict button
if st.button("🔍 Predict Sentiment"):
    if not user_input.strip():
        st.warning("Please enter some text to analyze.")
    else:
        with st.spinner("Processing..."):
            # Preprocess the text (lemmatize)
            preprocessed_text = preprocess_text(user_input)

            # Send to Flask API
            response = requests.post(API_URL, json={"text": preprocessed_text})

            if response.status_code == 200:
                prediction = response.json()["prediction"]
                label_map = {0: "❌ Negative", 1: "😐 Neutral", 2: "✅ Positive"}
                st.success(f"**Predicted Sentiment:** {label_map.get(prediction, 'Unknown')}")

            else:
                st.error("Something went wrong with the prediction request.")
