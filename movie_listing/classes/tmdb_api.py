import requests

TMDB_API_KEY = "5fc61c0517c45fa4a16dfc3c7a73f70a"
TMDB_BEARER_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1ZmM2MWMwNTE3YzQ1ZmE0YTE2ZGZjM2M3YTczZjcwYSIsInN1YiI6IjVmZTEyODI0YWI2ODQ5MDAzZTdmYTUwZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mbULf-GA6LCc6pGAccM3rZc2AHNLGcrvvxBy47o15JY"
TMDB_API_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
TMDB_API_MOVIE_URL = "https://api.themoviedb.org/3/movie/"


def get_movies(title: str) -> list:
    headers = {
        "Authorization": TMDB_BEARER_TOKEN,
        "Content-Type": "application/json;charset=utf-8"
    }
    params = {
        "api_key": TMDB_API_KEY,
        "language": "en-US",
        "query": title,
        "include_adult": True
    }
    res = requests.get(TMDB_API_SEARCH_URL, params=params, headers=headers)
    res.raise_for_status()
    data = res.json()["results"]
    movies = []

    for movie in data:
        movies.append({
            "id": movie["id"],
            "title": movie["title"],
            "year": movie["release_date"].split("-")[0],
        })

    return movies


def get_movie(id: int) -> dict:
    params = {
        "api_key": TMDB_API_KEY,
        "language": "en-US"
    }
    res = requests.get(f"{TMDB_API_MOVIE_URL}{id}", params=params)
    res.raise_for_status()
    data = res.json()

    return {
        "title": data["title"],
        "img_url": "https://image.tmdb.org/t/p/w500" + data["poster_path"] if
        data["poster_path"] else "https://via.placeholder.com/500",
        "year": data["release_date"].split("-")[0],
        "description": data["overview"]
    }
