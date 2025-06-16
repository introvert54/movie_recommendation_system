import requests
import pandas as pd

# Replace 'YOUR_API_KEY' with your actual TMDB API key
API_KEY = 'YOUR_API_KEY'
BASE_URL = 'https://api.themoviedb.org/3'

def fetch_movies(page):
    url = f'{BASE_URL}/movie/popular?api_key={API_KEY}&page={page}'
    response = requests.get(url)
    return response.json()

# Function to fetch movie credits
def fetch_movie_credits(movie_id):
    url = f'{BASE_URL}/movie/{movie_id}/credits?api_key={API_KEY}'
    response = requests.get(url)
    return response.json()

# Function to fetch movie keywords
def fetch_movie_keywords(movie_id):
    url = f'{BASE_URL}/movie/{movie_id}/keywords?api_key={API_KEY}'
    response = requests.get(url)
    return response.json()

# List to store credits and keywords details
credits_list = []
keywords_list = []

# Fetch credits and keywords details for the first 500 pages (you can increase the number of pages as needed)
for page in range(1, 500):
    movies = fetch_movies(page)
    for movie in movies['results']:
        movie_id = movie['id']
        
        # Fetch credits
        credits = fetch_movie_credits(movie_id)
        credits_list.append({
            'id': movie_id,
            'cast': credits.get('cast', []),
            'crew': credits.get('crew', [])
        })
        
        # Fetch keywords
        keywords = fetch_movie_keywords(movie_id)
        keywords_list.append({
            'id': movie_id,
            'keywords': keywords.get('keywords', [])
        })

# Convert the lists to DataFrames
credits_df = pd.DataFrame(credits_list)
keywords_df = pd.DataFrame(keywords_list)

# Save the DataFrames to CSV files
credits_df.to_csv('credits.csv', index=False)
keywords_df.to_csv('keywords.csv', index=False)