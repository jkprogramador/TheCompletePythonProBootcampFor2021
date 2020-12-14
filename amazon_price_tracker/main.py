from bs4 import BeautifulSoup
import requests
import smtplib
import lxml

URL = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
TARGET_PRICE = 100
EMAIL_USER = ""
EMAIL_PASSWORD = ""
EMAIL = ""
EMAIL_RECIPIENT = ""


def get_html() -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    }
    response = requests.get(URL, headers=headers)
    response.raise_for_status()

    return response.text


def get_price(contents: str) -> float:
    soup = BeautifulSoup(contents, features="lxml")
    price_tag = soup.find(name="span", id="priceblock_ourprice")

    return float(price_tag.getText()[1:])


def send_email(price: float):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL_USER, password=EMAIL_PASSWORD)
        msg = f"Subject:Amazon Price Alert!\n\nName of the product.\nCurrent price: ${price}.\nLink here: {URL}"
        connection.send_message(msg=msg, from_addr=EMAIL, to_addrs=EMAIL_RECIPIENT)


def main():
    contents = get_html()
    price = get_price(contents)

    if price < TARGET_PRICE:
        send_email(price)


main()
