import requests

API_URL = "https://api.sheety.co/236ed8d960b740b1902dedb235c100ea/flightDeals/prices"
USERS_API_URL = "https://api.sheety.co/236ed8d960b740b1902dedb235c100ea/flightDeals/users"
API_BASIC_AUTH = ""


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
    def save_user_data(first_name: str, last_name: str, email: str):
        headers = {
            "Authorization": API_BASIC_AUTH,
            "Content-Type": "application/json"
        }
        post_data = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }
        response = requests.post(USERS_API_URL, json=post_data, headers=headers)
        response.raise_for_status()

    @staticmethod
    def get_user_emails() -> list:
        headers = {
            "Authorization": API_BASIC_AUTH,
            "Content-Type": "application/json"
        }
        response = requests.get(USERS_API_URL, headers=headers)
        response.raise_for_status()
        data = response.json()

        return [user["email"] for user in data["users"]]

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
