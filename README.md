🎬 AI Movie Recommendation System

A beginner-friendly AI-powered Movie Recommendation Web App built using Python and Streamlit that suggests similar movies and displays their posters.

🔗 Live App: https://movie-recommendation-system-pbkepcnxye4v8out2z3js.streamlit.app

🚀 Features

🎥 Select a movie from the list

🤖 Get AI-based movie recommendations

🖼️ View movie posters

🌐 Fully deployed on Streamlit Cloud

⚡ Fast and interactive UI

🧠 How It Works

This project uses content-based filtering.
It recommends movies based on genre similarity and fetches posters using the TMDB API.

🛠️ Tech Stack
Technology	Purpose
Python	Core programming
Pandas	Data handling
Streamlit	Web app framework
TMDB API	Fetch movie posters
📂 Project Structure
movie-recommendation-system/
│
├── app.py               # Main Streamlit app
├── movies.csv           # Movie dataset
├── requirements.txt     # Required libraries
└── posters/             # Stored movie posters

▶️ Run Locally
1️⃣ Clone the repository
git clone https://github.com/rahulbansal024/movie-recommendation-system.git
cd movie-recommendation-system

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the app
streamlit run app.py

🌍 Deployment

This project is deployed using Streamlit Community Cloud.

To deploy your own:

Push code to GitHub

Go to https://share.streamlit.io

Connect your repository

Select app.py

Click Deploy 🚀

📌 Future Improvements

🎯 Add advanced AI similarity (cosine similarity)

🔍 Search movies instead of dropdown

❤️ Add favorites/watchlist

🎨 Improve UI with movie cards

🙌 Author

Rahul Bansal
AI & Data Science Student
