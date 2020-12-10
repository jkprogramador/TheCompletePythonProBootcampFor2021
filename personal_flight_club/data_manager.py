import requests
from flight_search import FlightSearch

API_URL = "https://api.sheety.co/236ed8d960b740b1902dedb235c100ea/flightDeals/prices"
API_BASIC_AUTH = "Basic amtwcm9ncmFtYWRvcjo2ZWUxeS42YTc1ZWU="


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        # self.__flight_search = flight_search
        self.__data = self.__load_data()
        # self.__populate_iata_codes()

    # def __populate_iata_codes(self):
    #     for data in self.__data["prices"]:
    #         iata = self.__flight_search.get_iata(data["city"])
    #         self.__update_iata(iata=iata, data=data)

    @property
    def data(self) -> list:
        return self.__data["prices"]

    @staticmethod
    def __load_data() -> dict:
        headers = {
            "Authorization": API_BASIC_AUTH
        }
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()

        return response.json()

    @staticmethod
    def __update_iata(iata: str, data: dict):
        headers = {
            "Authorization": API_BASIC_AUTH,
            "Content-Type": "application/json"
        }
        body = {
            "price": {
                "iataCode": iata
            }
        }
        response = requests.put(f"{API_URL}/{data['id']}", headers=headers, json=body)
        response.raise_for_status()
