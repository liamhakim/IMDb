import requests

TMDB_API_KEY = "af64e76d663517cdc595fc3a08de6d41"

def get_movie_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        poster_path = data.get("poster_path")
        if poster_path:
            return f"https://image.tmdb.org/t/p/original/{poster_path}"
    return None

def get_movie_trailer(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={TMDB_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        videos = data.get("results")
        if videos:
            for video in videos:
                if video.get("type") == "Trailer":
                    key = video.get("key")
                    if key:
                        return f"https://www.youtube.com/watch?v={key}"
    return None
