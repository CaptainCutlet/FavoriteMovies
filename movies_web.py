import requests
import urllib.parse

API_KEY = "8116cbc6e190e454f52dbd721cd725ad"
MOVIE_SEARCH_ENDPOINT = "https://api.themoviedb.org/3/search/movie?"
MOVIE_DETAIL_SEARCH_ENDPOINT = "https://api.themoviedb.org/3/movie/"


class MoviesWeb:

    def __init__(self):
        pass

    def search_by_title(self, movie_title):
        response = requests.get(MOVIE_SEARCH_ENDPOINT, params={"api_key": API_KEY, "query": movie_title})
        return response.json()['results']

    def get_movie_details(self, movie_id):
        response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}",
                                params={"api_key": API_KEY, "language": "en-US"})
        return response.json()


