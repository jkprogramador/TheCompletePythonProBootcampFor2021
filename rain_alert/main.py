import requests
from twilio.rest import Client

WEATHER_API_KEY = ""
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/onecall"
TWILIO_ACCOUNT_SID = ""
TWILIO_AUTH_TOKEN = ""
TWILIO_PHONE_NUMBER = ""
RECIPIENT_PHONE_NUMBER = ""

weather_params = {
    "lat": -23.550520,
    "lon": -46.633308,
    "exclude": "minutely,daily",
    "appid": WEATHER_API_KEY
}

response = requests.get(WEATHER_API_URL, params=weather_params)
response.raise_for_status()
weather_data = response.json()
will_rain = False

for hour_data in weather_data["hourly"][0:12]:
    weather_id = hour_data["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True

if will_rain:
    # Your Account Sid and Auth Token from twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages \
        .create(body="It's going to rain today. Remember to bring ☂️", from_=TWILIO_PHONE_NUMBER,
                to=RECIPIENT_PHONE_NUMBER)

    print(message.status)
