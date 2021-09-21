from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/home/bismark/Documents/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element_by_css_selector("#articlecount a")
# Clicking on the hyperlink on the webpage
# article_count.click()

# typing in a text box on a webpage
# And using selenium to press the enter key on the keyboard
search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)