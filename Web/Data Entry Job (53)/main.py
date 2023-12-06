import requests
from ignore import FORM_LINK
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.common.keys import Keys
from random import randint
from bs4 import BeautifulSoup

RENT_LINK = "https://appbrewery.github.io/Zillow-Clone/"

def pull_data(URL) -> list:
    site_response = requests.get(RENT_LINK)
    soup = BeautifulSoup(site_response.text, "html.parser")

    links_to_rent = [x.get('href') for x in soup.findAll('a', class_ ='property-card-link')]
    price_of_rent = [price_cleaner(x.get_text()) for x in soup.findAll('span', class_ = 'PropertyCardWrapper__StyledPriceLine')]
    address_of_rent = [(x.get_text()).replace('\n','').strip() for x in soup.findAll('address')]
    return [{"address":address, "price": price, 'link':link} for address,price,link in zip(address_of_rent, price_of_rent, links_to_rent)]
    
    
def price_cleaner(price_string):
    return ''.join(filter(lambda x: x.isdigit() or x == ',' or x == '$', price_string ))

def send_data(dataset:[dict], url:str):
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=chrome_option)
    for element in dataset:
        driver.get(url)
        time.sleep(2)
        address_input = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_input = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_input = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

        address_input.send_keys(element.get('address'))
        price_input.send_keys(element.get('price'))
        link_input.send_keys(element.get('link'))
        
        button = driver.find_element(By.XPATH, "//*[contains(text(), 'Отправить')]")
        button.click()
        time.sleep(1)
    
    driver.close()


data = pull_data(RENT_LINK)
# data = [{'address': '747 Geary Street, 747 Geary St, Oakland, CA 94609', 'price': '$2,895', 'link': 'https://www.zillow.com/b/747-geary-street-oakland-ca-CYzGVt/'},{'address': 'Parkmerced | 3711 19th Ave, San Francisco, CA', 'price': '$2,810', 'link': 'https://www.zillow.com/apartments/san-francisco-ca/parkmerced/5XjKHx/'}]
send_data(data, FORM_LINK)