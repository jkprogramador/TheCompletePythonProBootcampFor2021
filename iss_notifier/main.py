import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -23.550520  # Your latitude
MY_LONG = -46.633308  # Your longitude
MY_EMAIL_USER = ""
MY_EMAIL_PASSWORD = ""
MY_EMAIL = ""


def is_iss_overhead() -> bool:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    is_close_lat = MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
    is_close_long = MY_LONG - 5 <= iss_longitude <= MY_LONG + 5

    return is_close_lat and is_close_long


def is_night() -> bool:
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()

    return time_now.hour in range(sunset, sunrise)


def run_iss_notifier():
    # If the ISS is close to my current position
    # and it is currently dark
    # Then send me an email to tell me to look up.
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL_USER, password=MY_EMAIL_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:ISS Nearby\n\n \
             Look up!")


# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    run_iss_notifier()
