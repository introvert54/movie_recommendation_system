from flask import Flask, request, jsonify
from flask_cors import CORS
from movie_recommendation_system import recommend

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])

@app.route('/')
def home():
    return "Flask server is running!"

@app.route('/recommend/<movie_name>', methods=['GET'])
def recommend_movies(movie_name):
    recommended_movies = recommend(movie_name)
    return jsonify(recommended_movies)

# @app.route('/hybrid/<int:user_id>/<movie_name>', methods=['GET'])
# def hybrid_recommendation(user_id, movie_name):
#     hybrid_list = hybrid(user_id, movie_name)
#     return jsonify({'hybrid recommendation': hybrid_list})    

if __name__ == '__main__':
    app.run(debug=True)