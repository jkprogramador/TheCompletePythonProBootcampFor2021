from twilio.rest import Client

TWILIO_ACCOUNT_SID = ""
TWILIO_AUTH_TOKEN = ""
TWILIO_PHONE_NUMBER = ""
RECIPIENT_PHONE_NUMBER = ""


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.__client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_message(self, msg: str):
        self.__client.messages.create(body=msg, from_=TWILIO_PHONE_NUMBER, to=RECIPIENT_PHONE_NUMBER)
