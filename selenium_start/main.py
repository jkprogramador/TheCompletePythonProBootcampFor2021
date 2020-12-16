from selenium import webdriver

CHROME_DRIVER_PATH = r"C:\Users\Jack Lee\Documents\chromedriver.exe"
WEBSITE_URL = ""

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
# driver.get(WEBSITE_URL)

# price = driver.find_element_by_id(id_="my_id")
# print(price.text)

# search_bar = driver.find_element_by_name(name="q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute(name="placeholder"))

# logo = driver.find_element_by_class_name(name="python-logo")
# print(logo.size)

# documentation_link = driver.find_element_by_css_selector(css_selector=".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element_by_xpath(xpath='//*[@id="tabs--3-tab-5"]/span')
# print(bug_link.text)

# prices = driver.find_elements_by_class_name(name="price")

# driver.close()
driver.quit()
