import React, { useState } from "react";
import axios from "axios";

const Recommendation = () => {
  const [movie, setMovie] = useState("");
  const [recommendations, setRecommendations] = useState([]);

  const fetchRecommendations = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:5000/recommend/${movie}`);
      setRecommendations(response.data);
    } catch (error) {
      console.error("Error fetching recommendations:", error);
    }
  };

  return (
    <div>
      <h2>Movie Recommendation System</h2>
      <input
        type="text"
        placeholder="Enter movie title"
        value={movie}
        onChange={(e) => setMovie(e.target.value)}
      />
      <button onClick={fetchRecommendations}>Get Recommendations</button>
      <ul>
        {recommendations.map((title, index) => (
          <li key={index}>{title}</li>
        ))}
      </ul>
    </div>
  );
};

export default Recommendation;
