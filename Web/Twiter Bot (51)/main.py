from ignore import password as PASSWORD
from ignore import login as LOGIN
from ignore import user as USER
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.common.keys import Keys

DOWN_EXPECTED = 50
UP_EXPECTED = 10
TWITTER_EMAIL = LOGIN
TWITTER_PASSWORD = PASSWORD
SPEEDTEST = 'https://www.speedtest.net/'
TWITTER ='https://twitter.com/i/flow/signup'


class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_experimental_option('detach', True)
        self.driver  = webdriver.Chrome(chrome_option)
        self.driver.maximize_window()
        self.up_exp = UP_EXPECTED
        self.down_exp = DOWN_EXPECTED
        self.up = None
        self.down = None

    def get_internet_speed(self):
        self.driver.get(SPEEDTEST)
        start_test = self.driver.find_element(By.CLASS_NAME,'js-start-test')
        start_test.click()
        time.sleep(10)
        while self.driver.current_url == SPEEDTEST:
            time.sleep(1)
        speed_array = self.driver.find_elements(By.CLASS_NAME, 'result-data-large')
        self.down = speed_array[0].text
        self.up = speed_array[1].text
        

    
    def tweet_at_provider(self):
        MESSAGE = f"Hey, Internet Provider. Why is my internet speed is {self.down}down&{self.up}up when I pay for {self.down_exp}down&{self.up_exp}up?"
        
        self.driver.get(TWITTER)
        time.sleep(6)

        link_entry = self.driver.find_element(By.XPATH, "//*[normalize-space(text()) = 'Войти']")
        link_entry.click()
        time.sleep(4)
        
        login_field = self.driver.find_element(By.TAG_NAME,'input')
        login_field.send_keys(TWITTER_EMAIL)
        login_field.send_keys(Keys.ENTER)
        time.sleep(10)

        login_field = self.driver.find_element(By.TAG_NAME,'input')
        login_field.send_keys(USER)
        login_field.send_keys(Keys.ENTER)
        time.sleep(3)        

        pasword_field = self.driver.find_elements(By.TAG_NAME,'input')[1]
        pasword_field.send_keys(TWITTER_PASSWORD)
        pasword_field.send_keys(Keys.ENTER)
        time.sleep(7)
        
        button_tweet = self.driver.find_element(By.XPATH, "//*[normalize-space(text())='Опубликовать пост']")
        button_tweet.click()
        time.sleep(3)

        tweet_field= self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
        tweet_field.send_keys(MESSAGE)
        time.sleep(2)

        send_button = self.driver.find_element(By.XPATH, "//*[normalize-space(text())='Опубликовать пост']")
        send_button.click()
        time.sleep(4)
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()