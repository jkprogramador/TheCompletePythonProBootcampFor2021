from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

CHROME_DRIVER_PATH = r"C:\Users\Jack Lee\Documents\chromedriver.exe"
WIKI_URL = "https://en.wikipedia.org/wiki/Main_Page"
APP_BREWERY_URL = "http://secure-retreat-92358.herokuapp.com/"

driver = webdriver.Chrome(CHROME_DRIVER_PATH)
driver.get(APP_BREWERY_URL)

try:
    # Since we are using find_element (singular), it will only return the first link
    # article_count = driver.find_element_by_css_selector(css_selector="#articlecount a")
    #
    # print(article_count.text)
    #
    # article_count.click()
    #
    # all_portals = driver.find_element_by_link_text("All portals")
    # all_portals.click()
    #
    # search_bar = driver.find_element_by_name(name="search")
    # search_bar.send_keys("Python")
    # search_bar.send_keys(Keys.ENTER)
    fname = driver.find_element_by_name("fName")
    fname.send_keys("Jack")
    lname = driver.find_element_by_name("lName")
    lname.send_keys("Lee")
    email = driver.find_element_by_name("email")
    email.send_keys("me.jacklee.jl@gmail.com")
    button = driver.find_element_by_css_selector("form button")
    button.click()
except NoSuchElementException as ex:
    print(ex)
finally:
    driver.quit()
