class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, departure_iata: str, destination_iata: str, departure_city: str, destination_city: str,
                 price: float, destination_airport: str, departure_airport: str, out_date: str, return_date: str):
        self.__departure_iata = departure_iata
        self.__destination_iata = destination_iata
        self.__departure_city = departure_city
        self.__destination_city = destination_city
        self.__departure_airport = departure_airport
        self.__destination_airport = destination_airport
        self.__out_date = out_date
        self.__return_date = return_date
        self.__price = price

    @property
    def departure_iata(self) -> str:
        return self.__departure_iata

    @property
    def destination_iata(self) -> str:
        return self.__destination_iata

    @property
    def departure_airport(self) -> str:
        return self.__departure_airport

    @property
    def destination_airport(self) -> str:
        return self.__destination_airport

    @property
    def out_date(self) -> str:
        return self.__out_date

    @property
    def return_date(self) -> str:
        return self.__return_date

    @property
    def return_airport(self) -> str:
        return self.__return_date

    @property
    def departure_city(self) -> str:
        return self.__departure_city

    @property
    def destination_city(self) -> str:
        return self.__destination_city

    @property
    def price(self) -> float:
        return self.__price
