from selenium import webdriver

chrome_driver_path = "/home/bismark/Documents/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org")
date = [driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/time').text
               for i in range(1, 6)]
events = [driver.find_element_by_xpath(f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/a').text for i in
          range(1, 6)]
date_events = {}

for i in range(0, 5):
    date_events[i] = {"time": date[i], "name": events[i]}
print(date_events)
driver.quit()
