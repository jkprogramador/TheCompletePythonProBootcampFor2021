import datetime as dt
import random
import smtplib

MONDAY = 0
MY_EMAIL = ""
MY_EMAIL_USER = ""
MY_EMAIL_PASSWORD = ""

# now = dt.datetime.now()
# print(f"{now.day:02}/{now.month:02}/{now.year}")

# date_of_birth = dt.datetime(year=1981, month=6, day=1)
# print(f"{date_of_birth.day:02}/{date_of_birth.month:02}/{date_of_birth.year}")

now = dt.datetime.now()

weekday = now.weekday()

if weekday == MONDAY:
    with open("quotes.txt") as file:
        quotes = file.readlines()
        quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL_USER, password=MY_EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Quote of the day\n\n{quote}")
