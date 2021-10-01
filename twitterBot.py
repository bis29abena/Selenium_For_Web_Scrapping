from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time

# set a constant variable for the driver file path
CHROME_DRIVER_PATH = "/home/bismark/Documents/Development/chromedriver"


class InternetSpeedTwitterBot:
    def __init__(self, **kwargs):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.promise_up = kwargs["up"]
        self.promise_down = kwargs["down"]
        self.up = None
        self.down = None
        self.yes_no = None
        self.email = None
        self.password = None

    def load_internet_speed_page(self):
        # opening the internet speed check website
        self.driver.get("https://www.speedtest.net/")

        start = self.driver.find_element_by_css_selector(".start-button a")
        start.click()

    def get_internet_speed(self, yes_no):
        self.yes_no = yes_no

        if self.yes_no == "yes":
            self.up = self.driver.find_element_by_xpath(
                '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
            self.down = self.driver.find_element_by_xpath(
                '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

            return self.up, self.down
        else:
            sys.exit()

    def tweet_at_provider(self, **kwargs):
        self.email = kwargs["email"]
        self.password = kwargs["password"]
        print(self.email)
        print(self.password)

        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(5.0)

        email = self.driver.find_element_by_name("username")
        email.send_keys(self.email)
        email.send_keys(Keys.ENTER)
        time.sleep(2.0)

        password = self.driver.find_element_by_name("password")
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)
        time.sleep(5.0)

        tweet_compose = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {self.promise_down}down/{self.promise_up}up? "
        tweet_compose.send_keys(tweet)

        tweet_enter = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet_enter.click()

