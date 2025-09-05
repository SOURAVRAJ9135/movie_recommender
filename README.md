# Movie_Recommender
🎬 Movie Recommender System

A content-based Movie Recommendation System built with Python and Streamlit, enhanced with TMDb API to fetch posters and movie details. This app suggests the top 5 movies similar to the one you select, making it easy to discover what to watch next.

✨ Features

🎥 Top 5 Recommendations – Select a movie and instantly get 5 similar movies.

🖼️ Posters & Details – Movie posters and metadata fetched dynamically from TMDb API.

⚡ Interactive Web App – Built with Streamlit for a smooth UI.

📊 Content-based Filtering – Uses cosine similarity on movie features (genres, keywords, cast, crew).

🧠 How I Built It

Dataset Preparation

Used a movie dataset (CSV) containing movie details such as title, genres, keywords, cast, and crew.

Cleaned the dataset and selected key features to define similarity between movies.

Feature Engineering

Combined relevant features (overview, genres, keywords, cast, crew) into a single text column.

Applied text vectorization (CountVectorizer / TF-IDF) to convert text into numerical vectors.

Similarity Computation

Used Cosine Similarity to measure closeness between movies based on vectorized features.

Created a similarity matrix for quick lookup of top related movies.

Integration with TMDb API

For each recommended movie, fetched:

Poster image

Title

Additional metadata (release year, etc.)

Streamlit Web App

Built an interactive UI where:

User selects a movie from a dropdown.

Backend fetches top 5 similar movies using the similarity matrix.

Posters & titles are displayed in a clean, responsive layout.

🛠️ Tech Stack

Python

Streamlit – frontend web framework

Pandas / NumPy – data manipulation

Scikit-learn – vectorization + cosine similarity

Requests – API calls

TMDb API – fetch posters & details

🔮 Future Enhancements

Add collaborative filtering for user-based recommendations.

Show ratings, trailers, and reviews from TMDb.

Implement a search bar to find movies directly.

Deploy on HuggingFace/Render in addition to Streamlit Cloud.


Here's link to my app https://movierecommender-han96864mqhrja5v2kgdsb.streamlit.app/
