# 💬 SentimentSnap

**SentimentSnap** is an end-to-end NLP project that analyzes user reviews and predicts their sentiment (**Positive**, **Neutral**, or **Negative**). It combines a Flask API backend with a Streamlit frontend for a seamless, interactive user experience.

---

## 🔍 Features

- ✅ Real-time sentiment prediction
- 🧹 Text preprocessing with Lemmatization
- 🤖 Trained ML models (Logistic Regression, SVM, Naive Bayes and Random Forest.)
- ✨ TF-IDF vectorization using bi-grams (3000 features)
- 🔌 Flask backend serving predictions via API
- 🌐 Streamlit frontend with a user-friendly interface

---

## 🧰 Tech Stack

| Layer       | Technology              |
|-------------|--------------------------|
| Frontend    | Streamlit                |
| Backend     | Flask (API-only)         |
| ML Models   | Scikit-learn             |
| Text Prep   | NLTK, TfidfVectorizer    |
| Serialization | Pickle                |

---

## 📁 Project Structure

```
SentimentSnap/
├── sentiment_api.py          # Flask API backend
├── sentiment_ui.py           # Streamlit frontend
├── models/
│   ├── sentiment_model.pkl       # Trained ML model
│   └── tfidf_vectorizer.pkl      # TF-IDF vectorizer
├── text_preprocess.py        # Text cleaning and lemmatization
├── README.md
└── requirements.txt          # Project dependencies
```

---

## 🚀 Getting Started

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/Rishi52/SentimentSnap
cd SentimentSnap
```

### 📦 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🖥️ 3. Start the Flask API Server

```bash
python sentiment_api.py
```

> The API will be available at: `http://localhost:5000/predict`

### 🌐 4. Launch the Streamlit Frontend

In a new terminal:

```bash
streamlit run sentiment_ui.py
```

---

## 🧪 Example

> **Input:**
> ```
> The food was absolutely amazing and the service was top-notch!
> ```
>
> **Output:**
> ```
> Sentiment: Positive ✅
> ```

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgments

- 🛠️ [NLTK](https://www.nltk.org/) – For text preprocessing
- 📚 [Scikit-learn](https://scikit-learn.org/) – For building ML models
- 🎨 [Streamlit](https://streamlit.io/) – For crafting an intuitive UI
- ⚙️ [Flask](https://flask.palletsprojects.com/) – For building a lightweight API layer

---

> 🔗 Ready to bring insights out of text — one sentiment at a time!

