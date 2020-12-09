import requests
from twilio.rest import Client
import os
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_VANTAGE_API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")
ALPHA_VANTAGE_API_URL = "https://www.alphavantage.co/query"
NEWS_API_URL = "http://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
TWILIO_ACCOUNT_SID = "AC6fe6a2fef4522ad500511b29106cbd11"
TWILIO_AUTH_TOKEN = "bd1a326d047de5d99ed82f2a4ac5e99a"
TWILIO_PHONE_NUMBER = "+16266584276"
RECIPIENT_PHONE_NUMBER = ""


def get_stock_value_change() -> float:
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": ALPHA_VANTAGE_API_KEY
    }
    response = requests.get(ALPHA_VANTAGE_API_URL, params=params)
    response.raise_for_status()
    data = response.json()
    stocks = data["Time Series (Daily)"]
    now = dt.datetime.now()
    yesterday = (now - dt.timedelta(days=1)).date().isoformat()
    day_before_yesterday = (now - dt.timedelta(days=2)).date().isoformat()
    stock_value_y = float(stocks[yesterday]["close"])
    stock_value_dfy = float(stocks[day_before_yesterday]["close"])
    value_change = (stock_value_y - stock_value_dfy) / stock_value_y * 100

    return value_change


def get_news() -> list:
    params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }
    response = requests.get(NEWS_API_URL, params=params)
    response.raise_for_status()
    data = response.json()

    return data["articles"][:3]


def send_alerts(news: list, stock_value_change: float):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    if stock_value_change < 0:
        msg_body = f"{STOCK}: 🔻{round(abs(stock_value_change))}%\n"
    else:
        msg_body = f"{STOCK}: 🔺{round(abs(stock_value_change))}%\n"

    for news_item in news:
        msg_body += f"Headline: {news_item['title']}\nBrief: {news_item['description']}"
        message = client.messages.create(body=msg_body, from_=TWILIO_PHONE_NUMBER, to=RECIPIENT_PHONE_NUMBER)
        print(message.status)


def main():
    stock_value_change = get_stock_value_change()

    if abs(stock_value_change) > 5:
        news = get_news()
        send_alerts(news, stock_value_change)


main()
