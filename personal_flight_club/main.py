from data_manager import DataManager
from flight_search import FlightSearch
# from notification_manager import NotificationManager
import datetime as dt

DEPARTURE_CITY_IATA = "SAO"


def main():
    data_manager = DataManager()
    # notification_manager = NotificationManager()
    now = dt.datetime.now()
    date_from = now + dt.timedelta(days=1)
    date_to = now + dt.timedelta(days=6 * 30)
    cities_to = [data["iataCode"] for data in data_manager.data]
    prices = {data["iataCode"]: data["lowestPrice"] for data in data_manager.data}

    print("Welcome to Flight Club.")
    print("We find the best flight deals and email you.")
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    email = input("What is your email? ")
    email_confirmation = input("Type your email again. ")

    while email != email_confirmation:
        email_confirmation = input("Type your email again. ")

    data_manager.save_user_data(first_name, last_name, email)
    user_emails = data_manager.get_user_emails()

    results = FlightSearch.get_flights(
        date_from=date_from.strftime("%d/%m/%Y"),
        date_to=date_to.strftime("%d/%m/%Y"),
        departure_iata=DEPARTURE_CITY_IATA,
        destination_iata=",".join(cities_to)
    )

    for flight in results:
        my_lowest_price = prices[flight.destination_iata]

        if flight.price < my_lowest_price:
            msg = f"Low price alert! Only R${flight.price} to fly from \
{flight.departure_city}-{flight.departure_airport} to \
{flight.destination_city}-{flight.destination_airport}, \
from {flight.out_date} to {flight.return_date}"
            # notification_manager.send_message(msg)
            # notification_manager.send_emails(msg, user_emails)


main()
