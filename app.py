import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Movie Recommendation System", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
body {
    background-color: #0E1117;
}

.title {
    text-align: center;
    font-size: 55px;
    font-weight: bold;
    color: white;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #AAAAAA;
    margin-bottom: 35px;
    font-size: 18px;
}

.movie-card {
    background-color: #161B22;
    padding: 12px;
    border-radius: 14px;
    text-align: center;
    transition: transform 0.3s ease;
}

.movie-card:hover {
    transform: scale(1.08);
}

.movie-title {
    color: white;
    margin-top: 8px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)


# ---------- HEADER ----------
st.markdown('<div class="title">🎬 Movie Recommendation System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Select a movie and get recommendations with posters</div>', unsafe_allow_html=True)

# ---------- LOAD DATA ----------
df = pd.read_csv("movies.csv")

movie_name = st.selectbox("Choose a movie:", df["Movie"])

def get_poster(movie):
    filename = movie.lower().replace(" ", "") + ".jpg"
    path = os.path.join("posters", filename)
    if os.path.exists(path):
        return path
    else:
        return "https://via.placeholder.com/300x450?text=No+Image"

# ---------- RECOMMEND BUTTON ----------
if st.button("🎯 Recommend Movies"):
    genre = df[df["Movie"] == movie_name]["Genre"].values[0]
    recommendations = df[(df["Genre"] == genre) & (df["Movie"] != movie_name)]

    st.markdown("### ⭐ You may also like")

    cols = st.columns(len(recommendations), gap="large")

    for col, movie in zip(cols, recommendations["Movie"]):
        with col:
            st.markdown('<div class="movie-card">', unsafe_allow_html=True)
            st.image(get_poster(movie), width=260)
            st.markdown(f"**{movie}**")
            st.markdown('</div>', unsafe_allow_html=True)
