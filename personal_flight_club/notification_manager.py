from twilio.rest import Client
import smtplib

TWILIO_ACCOUNT_SID = ""
TWILIO_AUTH_TOKEN = ""
TWILIO_PHONE_NUMBER = ""
RECIPIENT_PHONE_NUMBER = ""
MY_EMAIL_USER = ""
MY_EMAIL_PASSWORD = ""
MY_EMAIL = ""


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.__client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_message(self, msg: str):
        self.__client.messages.create(body=msg, from_=TWILIO_PHONE_NUMBER, to=RECIPIENT_PHONE_NUMBER)

    def send_emails(self, msg: str, recipients: str):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL_USER, password=MY_EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=recipients,
                msg=f"Subject:Great flight deals\n\n{msg.encode('utf-8')}"
            )
