from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import requests
from time import sleep
from pathlib import Path

CHROME_DRIVER_PATH = r"C:\Users\Jack Lee\Documents\chromedriver.exe"
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSeFHjG9lCyf7G8hRoaAf6Iuo6z4mtVOo8J1U-3VlrloYuegLQ/viewform?usp=sf_link"
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"


def create_cache():
    path = Path("./cache.html")

    if not path.exists():
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9"
        }
        response = requests.get(ZILLOW_URL, headers=headers)
        response.raise_for_status()

        with open("cache.html", mode="w", encoding="utf-8") as file:
            file.write(response.text)


def read_cache() -> str:
    with open("cache.html", encoding="utf-8") as file:
        return file.read()


create_cache()
contents = read_cache()
soup = BeautifulSoup(contents, features="html.parser")
articles = soup.find_all(name="article", class_="list-card")
listing_links = []
listing_prices = []
listing_addresses = []

for article in articles:
    anchor_tag = article.find(name="a", class_="list-card-link")
    url = anchor_tag.get("href")
    url = "https://www.zillow.com" + url if not url.startswith("https") else url
    listing_links.append(url)
    price_tag = article.find(name="div", class_="list-card-price")

    if price_tag:
        price = price_tag.getText()
        listing_prices.append(price.split("/")[0])
    else:
        price_tag = article.find(name="ul", class_="list-card-details")
        price = price_tag.find_next(name="li").getText()
        listing_prices.append(price.split("+")[0])

    address_tag = article.find(name="address", class_="list-card-addr")
    address = address_tag.getText()
    listing_addresses.append(address)

driver = webdriver.Chrome(CHROME_DRIVER_PATH)

try:
    for i in range(len(listing_addresses)):
        driver.get(FORM_URL)
        sleep(1)
        address_field = driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_field.send_keys(listing_addresses[i])
        price_field = driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_field.send_keys(listing_prices[i])
        link_field = driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_field.send_keys(listing_links[i])
        submit_btn = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
        submit_btn.click()
        sleep(2)

except NoSuchElementException as ex:
    print(ex)
finally:
    driver.quit()
