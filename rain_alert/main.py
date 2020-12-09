import requests
from twilio.rest import Client

WEATHER_API_KEY = "1ee5f778663206baf69d9b2e8481d874"
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/onecall"
TWILIO_ACCOUNT_SID = "AC6fe6a2fef4522ad500511b29106cbd11"
TWILIO_AUTH_TOKEN = "bd1a326d047de5d99ed82f2a4ac5e99a"
TWILIO_PHONE_NUMBER = "+16266584276"

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
                to="+55 11 96465-4105")

    print(message.status)
