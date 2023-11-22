from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import datetime

URL = "https://orteil.dashnet.org/cookieclicker/"

def main_loop(seconds, url= URL):
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=chrome_option)
    driver.get(URL)
    consent = driver.find_element(By.CLASS_NAME, value='fc-cta-consent')
    consent.click()
    time.sleep(1)
    language = driver.find_element(By.ID, value='langSelect-EN')
    language.click()
    time.sleep(5)
    endtime = datetime.datetime.now()+datetime.timedelta(seconds=seconds)
    button = driver.find_element(By.ID, value='bigCookie')
    while datetime.datetime.now()<endtime:
        button.click()
        per_second = driver.find_element(By.ID, value="cookiesPerSecond").text
        if datetime.datetime.now().second%5==0:
            try:
                product_array = driver.find_elements(By.CSS_SELECTOR, value='.storeSection .enabled')
                product_array.reverse()
                for upgrade in product_array:
                    upgrade.click()
                    print(product_array)
            except:
                pass
            
    print(f'Final Score per second {per_second}')

main_loop(300)