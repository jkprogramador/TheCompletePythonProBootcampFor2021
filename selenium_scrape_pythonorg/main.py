from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

CHROME_DRIVER_PATH = r"C:\Users\Jack Lee\Documents\chromedriver.exe"
URL = "https://www.python.org/"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
# driver.set_window_size(width=100, height=200)
driver.maximize_window()
driver.get(URL)

try:
    # event_times = driver.find_elements_by_css_selector(".event-widget time")
    # print(event_times[0].text)
    # for time in event_times:

    events = driver.find_elements_by_css_selector(css_selector=".event-widget .shrubbery .menu li")
    events_dict = {}

    for index, event in enumerate(events):
        time_tag = event.find_element_by_tag_name(name="time")
        anchor_tag = event.find_element_by_tag_name(name="a")
        events_dict[index] = {
            "time": time_tag.text,
            "name": anchor_tag.text
        }

    print(events_dict)
except NoSuchElementException as ex:
    print(ex)
finally:
    driver.quit()
