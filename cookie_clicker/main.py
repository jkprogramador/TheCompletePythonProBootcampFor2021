from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

CHROME_DRIVER_PATH = r"C:\Users\Jack Lee\Documents\chromedriver.exe"
COOKIE_CLICKER_URL = "https://orteil.dashnet.org/experiments/cookie/"


def get_cookies_money() -> int:
    return int(driver.find_element_by_id(id_="money").text)


def buy_upgrade():
    upgrades = {}
    for el in driver.find_elements_by_css_selector("#store div"):
        try:
            b_tag = el.find_element_by_tag_name("b")
            text = b_tag.text
            if text:
                upgrades[int(text.split(" ")[-1].strip().replace(",", ""))] = el
        except NoSuchElementException:
            pass

    money = get_cookies_money()
    affordable_price = 0

    for price, text in upgrades.items():
        if money < price:
            break
        affordable_price = price

    if affordable_price > 0:
        upgrades[affordable_price].click()


driver = webdriver.Chrome(CHROME_DRIVER_PATH)
driver.get(COOKIE_CLICKER_URL)

try:
    cookie = driver.find_element_by_id(id_="cookie")
    game_timeout = time.time() + 60 * 5
    check_upgrades_timeout = time.time() + 5

    while time.time() < game_timeout:
        if time.time() > check_upgrades_timeout:
            buy_upgrade()
            check_upgrades_timeout = time.time() + 5
        cookie.click()
        # time.sleep(1)

    cookies_per_second = driver.find_element_by_id(id_="cps")
    print(cookies_per_second.text)
    driver.quit()
except NoSuchElementException as ex:
    print(ex)
