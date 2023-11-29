from ignore import login as LOGIN
from ignore import password as PASSWORD
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import time


URL =  "https://www.linkedin.com/jobs/search/?currentJobId=3689212656&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom"

def main_loop(url=URL):
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=chrome_option)
    driver.get(url)
    time.sleep(2)
    login_button = driver.find_element(By.CLASS_NAME, 'btn-secondary-emphasis')
    login_button.click()
    time.sleep(2)
    login_field = driver.find_element(By.ID, 'username')
    password_field = driver.find_element(By.ID, 'password')
    login_field.send_keys(LOGIN)
    password_field.send_keys(PASSWORD)
    password_field.send_keys(Keys.ENTER)
    time.sleep(5)
    job_array = driver.find_elements(By.CLASS_NAME,value="job-card-list__title")
    for job in job_array:
        try:
            job.click()
            time.sleep(1)
            easy_apply = driver.find_element(By.XPATH,value="//*[contains(text(), 'Easy Apply')]")
            easy_apply.click()  
            done = False 
            while not done:          
                try:
                    svg_element = driver.find_element(By.XPATH, "//svg[path/@d='M10.8 1H5.2L1 5.2v5.6L5.2 15h5.6l4.2-4.2V5.2zM12 9H4V7h8']")
                    svg_element.send_keys(Keys.ESCAPE)
                    discard_button = driver.find_element(By.XPATH,value="//*[contains(text(), 'Discard')]")
                    svg_element.click()
                    done=True
                except NoSuchElementException:
                    try:
                        button = driver.find_element(By.XPATH, "//*[contains(text(), 'Next')]")
                    except NoSuchElementException:
                        try:
                            button = driver.find_element(By.XPATH, "//*[contains(text(), 'Review')]")
                        except NoSuchElementException:
                            try:
                                button = driver.find_element(By.XPATH, "//*[contains(text(), 'Submit application')]")
                            finally:
                                done = True
                    button.click()
        except:
            pass

main_loop(URL)
