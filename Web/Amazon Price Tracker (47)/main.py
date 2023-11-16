from bs4 import BeautifulSoup
import requests
from datetime import datetime
import smtplib as smtplib
import datetime as dt
import random as rnd
import pandas as pd
import os
import time

GOGGLE_PASS = "gmlkjzkmwugomoxs"
MY_EMAIL = "egornnn@gmail.com"
RECEIVER = "egornnn@gmail.com"
URL = "https://www.amazon.co.uk/Capstone-Games-Terra-Mystica-Expansion/dp/B09TWMLR4B/ref=sr_1_4?crid=1KXEQN6NSZW29&keywords=terra+mystica&qid=1700143591&s=kids&sprefix=terra+mystic%2Ctoys%2C745&sr=1-4&ufe=app_do%3Aamzn1.fos.23648568-4ba5-49f2-9aa6-31ae75f1e9cd"
COOKIES={
    "session-token": "CsMWdZMEqPdr12I3KVHKcVh6jsNZEgFeJbI3WBI4Dkd+1/IUXuDwtOrFVoPdcKr50FXJI4vWr77MRZ9witDHc54h1844YdZ1BnndnGPCt9a6MCMKky0S51VsbrxGJkIEB9d7fuD90dXlAll3Yi6ht9ovvtf4Hj0SSigC7xTjEt8BX3ltPmuDnZi6+ZPGUuvBJxnA+Ur1Pd1T1O28sKZfJP2Z7sdcZfuvsu1hEB6ODU81yE8lwhnNVU3mIi7rUdrjaZR4/b+V8wS5ajh8TB0eua3PvURc15CeGgqFWKDZEDrhFUvWqh4LkA5i0TDMTbCnzFNKzx6rpUWK+3pyo9JKWJPNjz9oWWk8SIzIwMZ3R/U=",
    "session-id-time": '2082787201l',  
    "ubid-acbuk": '262-0061339-8019157',
    "session-id": '258-6022080-4969660',
    "x-acbuk": "jPi9m0CEzl1LGtXoYGYp8cgI2o5dolwigxky@k3LGq5HmdfqHSBGbAaKWuX89?bt",
}



def get_price(URL):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'referer': 'https://www.amazon.com/',
    # 'Connection': 'keep-alive',
    # "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    # "sec-ch-ua":'"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    # "X-Forwarded-For": '152.37.103.25',                       

}
    website=requests.get(URL, headers=headers, cookies=COOKIES)
    soup = BeautifulSoup(website.text, 'html.parser')
    price = soup.find('div', 'a-text-center a-size-mini a-color-secondary').text.strip()
    price = price.split(' ')
    return (int(price[1][:4]))


def send_email(message="Empty mail"):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, GOGGLE_PASS)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECEIVER,
                            msg=message)


price =  get_price(URL=URL)
if price < 2000:
    send_email(f"The price is low enough {URL}. Go buy it!")
    

