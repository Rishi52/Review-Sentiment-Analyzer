from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load model and vectorizer
model = pickle.load(open("./Models/sentiment_model.pkl", "rb"))
vectorizer = pickle.load(open("./Models/tfidf_vectorizer_lem.pkl", "rb"))

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        input_text = data.get("text", "")
        
        if not input_text.strip():
            return jsonify({"error": "Empty input"}), 400

        # Vectorize the lemmatized input
        vectorized_input = vectorizer.transform([input_text])
        
        # Predict sentiment
        prediction = model.predict(vectorized_input)[0]
        
        return jsonify({"prediction": int(prediction)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
