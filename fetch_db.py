import requests
import pandas as pd

# Replace 'YOUR_API_KEY' with your actual TMDB API key
API_KEY = 'YOUR_API_KEY'
BASE_URL = 'https://api.themoviedb.org/3'

# Function to fetch movie details
def fetch_movie_details(movie_id):
    url = f'{BASE_URL}/movie/{movie_id}?api_key={API_KEY}'
    response = requests.get(url)
    return response.json()

# Function to fetch movie list
def fetch_movies(page):
    url = f'{BASE_URL}/movie/popular?api_key={API_KEY}&page={page}'
    response = requests.get(url)
    return response.json()

# List to store movie details
movies_list = []

# Fetch movie details for the first 500 pages (you can increase the number of pages as needed)
for page in range(1, 500):
    movies = fetch_movies(page)
    for movie in movies['results']:
        movie_details = fetch_movie_details(movie['id'])
        movies_list.append({
            'genres': movie_details.get('genres', []),
            'id': movie_details.get('id'),
            'imdb_id': movie_details.get('imdb_id'),
            'original_title': movie_details.get('original_title'),
            'overview': movie_details.get('overview'),
            'release_date': movie_details.get('release_date'),
            'spoken_languages': movie_details.get('spoken_languages', []),
            'title': movie_details.get('title'),
            'vote_average': movie_details.get('vote_average'),
            'vote_count': movie_details.get('vote_count')
        })

# Convert the list to a DataFrame
movies_df = pd.DataFrame(movies_list)

# Save the DataFrame to a CSV file
movies_df.to_csv('movies_metadata.csv', index=False)