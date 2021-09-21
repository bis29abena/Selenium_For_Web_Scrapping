# Signing up to a web page using selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Searching for the chrome driver path
chrome_driver_path = "/home/bismark/Documents/Development/chromedriver"
# Using selenium to get the chrome driver path
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# Opening up the web page
driver.get("http://secure-retreat-92358.herokuapp.com")

# Getting the firstname input from the web page using the name atrribute
fname = driver.find_element_by_name("fName")
fname.send_keys("Bismark")
# Getting the lastname input from the web page using the name atrribute
lname = driver.find_element_by_name("lName")
lname.send_keys("Osei")
# Getting the emil input field
email_ = driver.find_element_by_name("email")
email_.send_keys("bismark@gmail.com")
# Using the enter button to signup after typing the email
email_.send_keys(Keys.ENTER)