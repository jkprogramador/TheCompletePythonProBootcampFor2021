import pandas
import random
import smtplib
import datetime as dt

LETTERS = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
MY_EMAIL = ""
MY_EMAIL_USER = ""
MY_EMAIL_PASSWORD = ""

now = dt.datetime.now()
current_month = now.month
current_day = now.day

df = pandas.read_csv("birthdays.csv")

for index, row in df.iterrows():
    if row["month"] == current_month and row["day"] == current_day:
        letter = random.choice(LETTERS)

        with open(f"letter_templates/{letter}") as file:
            message = file.read()

        message = message.replace("[NAME]", row["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL_USER, password=MY_EMAIL_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL_USER, to_addrs=row["email"],
                                msg=f"Subject:Happy Birthday\n\n{message}")
