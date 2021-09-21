from selenium import webdriver

chrome_drive_path = "/home/bismark/Documents/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_drive_path)
driver.get("https://orteil.dashnet.org/cookieclicker")
cookies = driver.find_element_by_id("bigCookie")
click = True
while click:
    cookies.click()

