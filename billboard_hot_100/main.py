from bs4 import BeautifulSoup
import requests
from pathlib import Path
import spotipy
from spotipy.oauth2 import SpotifyOAuth

BILLBOARD_CACHE = "billboard_cache.html"
SPOTIFY_CLIENT_ID = ""
SPOTIFY_CLIENT_SECRET = ""

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri="http://example.com",
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="token.txt"
))


def create_billboard_cache(year: str):
    file_path = Path(BILLBOARD_CACHE)

    if not file_path.exists():
        response = requests.get(f"https://www.billboard.com/charts/hot-100/{year}")
        response.raise_for_status()

        with open(BILLBOARD_CACHE, mode="w", encoding="utf-8") as file:
            file.write(response.text)


def read_billboard_cache() -> str:
    with open(BILLBOARD_CACHE, encoding="utf-8") as file:
        return file.read()


def parse_billboard_results(contents: str) -> list:
    soup = BeautifulSoup(contents, features="html.parser")
    song_titles = soup.find_all(name="span", class_="chart-element__information__song")

    return [title.getText() for title in song_titles]


def get_spotify_user_id() -> str:
    return sp.current_user()["id"]


def get_spotify_uris(song_titles: list, year: str) -> list:
    uris = []

    for song_title in song_titles:
        song_info = sp.search(q=f"track:{song_title} year:{year}")
        try:
            uris.append(song_info["tracks"]["items"][0]["uri"])
        except IndexError:
            print(f"{song_title} does not exist in Spotify. Skipped.")

    return uris


def create_spotify_playlist(user_id: str, name: str) -> str:
    playlist = sp.user_playlist_create(user=user_id, name=name, public=False)

    return playlist["id"]


def add_tracks_to_spotify(user_id: str, playlist_id: str, tracks: list):
    sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=tracks)


def main():
    travel_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    create_billboard_cache(travel_date)
    billboard_contents = read_billboard_cache()
    song_titles = parse_billboard_results(billboard_contents)
    user_id = get_spotify_user_id()
    year = travel_date.split('-')[0]
    spotify_uris = get_spotify_uris(song_titles=song_titles, year=year)
    playlist_id = create_spotify_playlist(user_id=user_id, name=f"{travel_date} Billboard 100")
    add_tracks_to_spotify(user_id=user_id, playlist_id=playlist_id, tracks=spotify_uris)


main()
