from ignore import password as PASSWORD
from ignore import login as LOGIN
from ignore import user as USER
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.common.keys import Keys
from random import randint

LOGIN_URL = "https://www.instagram.com/accounts/login"
URL = "https://www.instagram.com/chefsteps/"

class InstaFollower:
    def __init__(self, url_to_follow) -> None:
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_experimental_option('detach', True)
        self.driver  = webdriver.Chrome(chrome_option)
        self.driver.maximize_window()
        self.url = url_to_follow
        self.username = LOGIN
        self.password = PASSWORD

    def login(self):
        self.driver.get(LOGIN_URL)
        time.sleep(5)
        dismiss  = self.driver.find_element(By.XPATH,"//*[normalize-space(text()) = 'Разрешить все cookie']")
        dismiss.click()
        time.sleep(1)

        login_filed = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
        pass_field = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
        login_filed.send_keys(self.username)
        pass_field.send_keys(self.password)
        pass_field.send_keys(Keys.ENTER)
        time.sleep(1)

    def find_followers(self):
        self.driver.get(self.url)
        time.sleep(5)
        followers = self.driver.find_element(By.XPATH, "//*[contains(text(), 'подписчиков')]")
        followers.click()
        time.sleep(2)

    def follow_all(self):
        follow_array=self.driver.find_elements(By.XPATH,"//*[normalize-space(text()) = 'Подписаться']")
        try:
            for button in follow_array:
                button.click()
                time.sleep(randint(1,4))
        except:
            print("Sorry, this bot got detected")


insta = InstaFollower(URL)
insta.login()
time.sleep(3)
insta.find_followers()
time.sleep(3)
insta.follow_all()

