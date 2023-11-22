from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

EXAMPLE_URL = "https://www.amazon.co.uk/Capstone-Games-Terra-Mystica-Expansion/dp/B09TWMLR4B/ref=sr_1_4?crid=1KXEQN6NSZW29&keywords=terra+mystica&qid=1700143591"

EXAMPLE_URL_2 ='https://www.python.org/'

def get_amazon_price(URL=EXAMPLE_URL):
    driver= webdriver.Chrome()
    driver.get(URL)

    # Timeout to type the CAPTCHA
    time.sleep(15)

    price_whole = driver.find_element(By.CLASS_NAME, value='a-price-whole')
    price_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction')
    print(f"{price_whole.text}.{price_cents.text}")

def search_by(URL=EXAMPLE_URL_2):

    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_experimental_option('detach', True)
    driver= webdriver.Chrome()
    driver.get(URL)
    # Searh by NAME
    search_bar  = driver.find_element(By.NAME, value='q')
    print (search_bar.get_attribute('placeholder'))
    
    # Searh by ID
    button =driver.find_element(By.ID,value='submit')
    print(button.size   )

    # Searh by CSS
    link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
    print(link.text)

    # Search by XPath
    
    title = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
    print(title.text)

    driver.close()

def get_python_events(URL=EXAMPLE_URL_2):
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=chrome_option)
    driver.get(URL)
    dates = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
    events = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
    event_dict = {x:{"time":dates[x].get_attribute('datetime')[0:9], "event": events[x].text} for x in range(len(dates))}
    print(event_dict)
    driver.quit()

# get_amazon_price()
# search_by()
# get_python_events()


# Close is for closing of a Tab
# driver.close()

# Quit is for a coplete exit
# driver.quit()
