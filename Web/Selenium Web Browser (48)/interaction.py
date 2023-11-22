from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

URL = "https://en.wikipedia.org/wiki/Main_Page"
FORM_URL = 'https://secure-retreat-92358.herokuapp.com/'

def counter_wekipedia_articles(URL=URL):
    driver = webdriver.Chrome()
    driver.get(url=URL)
    counter = driver.find_element(By.ID, value='articlecount')
    number = ''.join(counter.text.split(' ')[0].split(','))
    print(f'{counter.text} or a number by itself {number}')

def counter_wiki_articles_alt (URL=URL):
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=chrome_option)
    driver.get(url=URL)
    counter = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
    print(counter.text)
    counter.click()
    time.sleep(5)
    driver.quit()

def click_on_links (URL=URL):
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=chrome_option)
    driver.get(url=URL)
    meta_wiki_link = driver.find_element(By.LINK_TEXT, value= "Meta-Wiki")
    meta_wiki_link.click()
    time.sleep(5)
    driver.quit()

def search_wiki(prompt):
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=chrome_option)
    driver.get(url=URL)
    button = driver.find_element(By.CLASS_NAME, value="search-toggle")
    button.click()
    input_field = driver.find_element(By.CLASS_NAME, value="cdx-text-input__input")
    input_field.send_keys(prompt)
    input_field.send_keys(Keys.ENTER)

def fill_form(URL = FORM_URL):
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=chrome_option)
    driver.get(URL)
    name_field = driver.find_element(By.NAME, value='fName')
    sur_field = driver.find_element(By.NAME, value='lName')
    email_field = driver.find_element(By.NAME, value='email')
    button = driver.find_element(By.CLASS_NAME, value='btn-primary')
    name_field.send_keys('Egor')
    sur_field.send_keys("Nazdriukhin")
    email_field.send_keys('egornnn@gmail.com')
    button.click()
    time.sleep(3)   
    driver.quit()


# counter_wekipedia_articles()
# counter_wiki_articles_alt()
# click_on_links()
# search_wiki('anime')
fill_form()