import streamlit as st
import pickle

movies = pickle.load(open('movies.pkl','rb'))
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()
similarity = cosine_similarity(vectors)
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [movies.iloc[i[0]].title for i in movies_list]

st.title("🎬 Movie Recommender")

selected_movie = st.selectbox("Select a movie", movies['title'].values)

if st.button("Recommend"):
    results = recommend(selected_movie)
    for movie in results:
        st.write(movie)
