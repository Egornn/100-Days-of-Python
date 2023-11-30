from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time

chrome_driver_path = r"C:\Users\Egor\Desktop\Develoment chrome driver\chromedriver.exe"
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
ser = Service(chrome_driver_path)
opt = webdriver.ChromeOptions()
opt.binary_location = brave_path
driver = webdriver.Chrome(service=ser, options=opt)
driver.maximize_window()
driver.get("https://tinder.com/")


login_in = driver.find_element(By.XPATH, "//*[@id='o41285377']/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a")
login_in.click()
time.sleep(1)

login_with_facebook = driver.find_element(By.XPATH, "//*[@id='o-1687095699']/div/div/div[1]/div/div[3]/span/div[2]/button")
login_with_facebook.click()
time.sleep(4)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(By.NAME, "email")
email.send_keys('Your email')
password = driver.find_element(By.NAME, "pass")
password.send_keys('Password')
password.send_keys(Keys.ENTER)
time.sleep(2)



driver.switch_to.window(base_window)
print(driver.title)
time.sleep(5)

allow_button = driver.find_element(By.XPATH, "//*[@id='o-1687095699']/div/div/div/div/div[3]/button[1]")
allow_button.click()
time.sleep(2)
not_interested_button = driver.find_element(By.XPATH, "//*[@id='o-1687095699']/div/div/div/div/div[3]/button[2]")
not_interested_button.click()
time.sleep(2)
accept_button = driver.find_element(By.XPATH, "//*[@id='o41285377']/div/div[2]/div/div/div[1]/button")
accept_button.click()
time.sleep(7)


for i in range(20):
    print(i)
    try:
        dislike_button = driver.find_element(By.XPATH, "//*[@id='o41285377']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button")
        dislike_button.click()

    except ElementNotInteractableException:
        try:
            dislike_button_2 = driver.find_element(By.XPATH,
                                                   "//*[@id='o41285377']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[2]/button")
            dislike_button_2.click()
            time.sleep(3)
        except:
            not_interested = driver.find_element(By.XPATH, "//*[@id='o-1687095699']/div/div/div[2]/button[2]")
            not_interested.click()
            time.sleep(3)


    except:
        # time.sleep(3)
        dislike_button_2 = driver.find_element(By.XPATH, "//*[@id='o41285377']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[2]/button")
        dislike_button_2.click()
        time.sleep(3)


    else:
        time.sleep(3)