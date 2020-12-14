from pathlib import Path
import requests
from bs4 import BeautifulSoup


def create_cache_html():
    movie_file = Path("./empire_top100_movies.html")

    if not movie_file.exists():
        response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
        response.raise_for_status()

        with open("empire_top100_movies.html", mode="w", encoding="utf-8") as file:
            file.write(response.text)


def read_cache_html() -> str:
    with open("empire_top100_movies.html", encoding="utf-8") as file:
        return file.read()


def parse_html(contents: str) -> list:
    soup = BeautifulSoup(markup=contents, features="html.parser")
    movie_titles = soup.find_all(name="h3", class_="title")

    return [title.getText() for title in movie_titles]


def create_movie_list(movie_titles: list):
    with open("my_top100_movies.txt", mode="w", encoding="utf-8") as file:
        file.write("\n".join(movie_titles))


def main():
    create_cache_html()
    contents = read_cache_html()
    titles = parse_html(contents)
    titles.reverse()
    create_movie_list(titles)


main()
