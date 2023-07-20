import requests

TMDB_API_KEY = "af64e76d663517cdc595fc3a08de6d41"

def get_movie_poster(title):
    poster= {}
    url = f"https://api.themoviedb.org/3/search/movie?query={title}&api_key=af64e76d663517cdc595fc3a08de6d41&include_adult=false&language=en-US&page=1"
    response = requests.get(url)
    if response.status_code == 200:
      data = response.json()
      if data['results']:
         poster={
             'image_url':'https://image.tmdb.org/t/p/original/'+ data['results'][0]['poster_path'],
             'trailer_id': data['results'][0]['id']
             }
         print(poster)
         
      else:
         poster={
             'image_url':'',
             'trailer_id': 0
             }
           

    return poster


def get_movie_trailer(id):
    key = 0
    url = f'https://api.themoviedb.org/3/movie/{id}/videos?api_key=af64e76d663517cdc595fc3a08de6d41&language=en-US'
    response = requests.get(url)
    if response.status_code == 200:
      data = response.json()
      if data['results']:
         key = data['results'][0]['key']
         
      else:
         key =0

    return key

import requests

def get_trending_movies():
    
    url = f"https://api.themoviedb.org/3/trending/movie/week?api_key=af64e76d663517cdc595fc3a08de6d41"
    
    response = requests.get(url)
    data = response.json()
    
    trending_movies = data.get("results", [])
    
    return trending_movies
