from twitterBot import InternetSpeedTwitterBot

# setting the promised up and down
# variables
PROMISED_UP = 150
PROMISED_DOWN = 10

# setting constant variables for both email and pass word
TWITTER_EMAIL = "Your Email"
TWITTER_PASSWORD = "Password"

speed = InternetSpeedTwitterBot(up=PROMISED_UP, down=PROMISED_DOWN)
speed.load_internet_speed_page()

answer = input("Do you want retrieve the internet speed type yes or no: ").lower()

(up, down) = speed.get_internet_speed(answer)

print(f"Download Speed: {up} Upload Speed: {down}")

if PROMISED_UP > float(up) and PROMISED_DOWN > float(down):
    speed.tweet_at_provider(email=TWITTER_EMAIL, password=TWITTER_PASSWORD)
else:
    print("Internet Speed is ok")
