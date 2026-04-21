# 🎬 Movie Recommender System

A content-based movie recommendation system built using machine learning techniques. It suggests similar movies based on genres, keywords, cast, and overview.

---

## 🚀 Features

* Recommend movies based on similarity
* Uses cosine similarity for accurate results
* Text preprocessing with stemming
* Clean and simple pipeline

---

## 🧠 How It Works

1. Combine movie features (overview, genre, cast, etc.)
2. Convert text data into vectors using CountVectorizer
3. Compute similarity using cosine similarity
4. Recommend top 5 similar movies

---

## 🛠 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* NLTK

---

## 📊 Example

Input:
Avatar

Output:

* Aliens vs Predator: Requiem
* Aliens
* Falcon Rising
* Independence Day
* Titan A.E.

---

## 📁 Project Structure

```
movie-recommender/
│
├── app.py
├── movies.pkl
├── similarity.pkl
├── notebook.ipynb
├── requirements.txt
└── README.md
```

---

## 📌 Future Improvements

* Add movie posters using TMDB API
* Build UI with Streamlit
* Deploy as a web app

---

## 👨‍💻 Author

Ayush Verma
