import requests

TMDB_API_KEY = "af64e76d663517cdc595fc3a08de6d41"

#  def get_movie_poster(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         poster_path = data.get("poster_path")
        
        
#         if poster_path:
#             return f"https://image.tmdb.org/t/p/original/{poster_path}"
#     return None

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
         #poster_url= 'https://image.tmdb.org/t/p/original/'+ data['results'][0]['poster_path']
      else:
         poster={
             'image_url':'',
             'trailer_id': 0
             }
           # poster_url = ''

    return poster


def get_movie_trailer(id):
    key = 0
    url = f'https://api.themoviedb.org/3/movie/597/videos?api_key=af64e76d663517cdc595fc3a08de6d41&language=en-US'
    response = requests.get(url)
    if response.status_code == 200:
      data = response.json()
      if data['results']:
         key = data['results'][0]['key']
         #poster_url= 'https://image.tmdb.org/t/p/original/'+ data['results'][0]['poster_path']
      else:
         key =0

    return key


# def get_movie_trailer(id):
#     trailer_url= ''
#     url = f"https://api.themoviedb.org/3/search/movie?query={title}&api_key=af64e76d663517cdc595fc3a08de6d41&include_adult=false&language=en-US&page=1"
#     response = requests.get(url)
#     if response.status_code == 200:
#       data = response.json()
#       if data['results']:
#          trailer_url= 'https://image.tmdb.org/t/p/original/'+ data['results'][0]['poster_path']
#       else:
#             trailer_url = ''

#     return trailer_url

# def get_movie_trailer(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={TMDB_API_KEY}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         videos = data.get("results")
#         if videos:
#             for video in videos:
#                 if video.get("type") == "Trailer":
#                     key = video.get("key")
#                     if key:
#                         return f"https://www.youtube.com/watch?v={key}"
#     return None
