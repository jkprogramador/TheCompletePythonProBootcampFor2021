import requests
from flight_data import FlightData

API_LOCATIONS_URL = "https://tequila-api.kiwi.com/locations/query"
API_SEARCH_URL = "https://tequila-api.kiwi.com/v2/search"
API_KEY = ""


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass

    @staticmethod
    def get_iata(city: str) -> str:
        headers = {
            "apikey": API_KEY
        }
        params = {
            "term": city,
            "locale": "en-US",
            "location_types": "city"
        }
        response = requests.get(API_LOCATIONS_URL, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()

        return data["locations"][0]["code"]

    @staticmethod
    def get_flights(date_from: str, date_to: str, departure_iata: str, destination_iata: str) -> list:
        headers = {
            "apikey": API_KEY
        }
        params = {
            "fly_from": departure_iata,
            "fly_to": destination_iata,
            "date_from": date_from,
            "date_to": date_to,
            "one_for_city": 1,
            "flight_type": "round",
            "max_stopovers": 0,
            "nights_in_dst_from": 7,  # Round trips that return between 7 and 28 days in length
            "nights_in_dst_to": 28,
            "adults": 1,
            "curr": "BRL"
        }
        response = requests.get(API_SEARCH_URL, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()["data"]

        return [FlightData(
            departure_iata=flight["route"][0]["cityCodeFrom"],
            destination_iata=flight["route"][0]["cityCodeTo"],
            departure_city=flight["route"][0]["cityFrom"],
            destination_city=flight["route"][0]["cityTo"],
            departure_airport=flight["route"][0]["flyFrom"],
            destination_airport=flight["route"][0]["flyTo"],
            out_date=flight["route"][0]["local_departure"].split("T")[0],
            return_date=flight["route"][1]["local_departure"].split("T")[0],
            price=flight["price"]
        ) for flight in data]
