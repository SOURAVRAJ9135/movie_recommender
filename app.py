import streamlit as st
import pickle
import pandas as pd
import requests
from requests.exceptions import ConnectionError
import time

def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=1d3a545d9cd0d8d1ca614c6bf0c3dd32&language=en-US'
    for attempt in range(3):  # retry up to 3 times
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()
            return "https://image.tmdb.org/t/p/w500" + data['poster_path']
        except ConnectionError as e:
            print(f"Connection error on attempt {attempt+1}: {e}")
            time.sleep(2)  # wait before retry
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            break
    return None
#def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=1d3a545d9cd0d8d1ca614c6bf0c3dd32&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]  ## giving index of movie
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id ## going to that particular row


        recommended_movies.append(movies.iloc[i[0]].title)
        ## fetch poster from api
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

movie_dict=pickle.load(open('movie_dict.pkl', 'rb'))
movies= pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommender System")
selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values
)

if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)

    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

