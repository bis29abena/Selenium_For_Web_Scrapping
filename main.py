from selenium import webdriver

# -----------------------INSTRUCTIONS-----------------------------------
# DOWNLOAD THE CHROME DRIVER FROM https://chromedriver.chromium.org/
# CHECK YOU GOOGLE CHROME VERSION AND MAKE SURE YOU DOWNLOAD THE RIGHT CHROME DRIVER VERSION
# BOTH VERSIONS SHOULD BE EQUAL
# MAKE SURE THE CHROME_DRIVER_PATH IS IN THE EXACT LOCATION AS THE PATH SPECIFIED
# ------------------------------------------------------------------------

chrome_driver_path = "/home/bismark/Documents/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org")
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# search_bar = driver.find_element_by_name("q")
# print(search_bar)
#
# python_logo = driver.find_element_by_class_name("python-logo")
# print(python_logo.size)

# documentation = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation.get_attribute("href"))

# bug = driver.find_elements_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug[0].text)

driver.quit()