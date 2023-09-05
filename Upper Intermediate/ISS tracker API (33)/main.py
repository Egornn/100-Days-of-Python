import time

import requests
from datetime import datetime
import smtplib
from password import GOGGLE_PASS

MY_LAT = 51.491640
MY_LONG = -0.287096
MY_EMAIL = "egornnn@gmail.com"
RECEIVER = "egornnn@gmail.com"


def send_email(message="Empty mail"):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, GOGGLE_PASS)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECEIVER,
                            msg=message)


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


def isabove(lat, long):
    global MY_LAT, MY_LONG
    return (MY_LAT - 5 <= lat <= MY_LAT + 5) and (MY_LONG - 5 <= long <= MY_LONG + 5)


def isnight(sunrise, sunset, now):
    return now > sunset or now < sunrise


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.now()

while True:
    if isabove(iss_latitude, iss_longitude) and isnight(sunrise, sunset, time_now.hour):
        msg = f"Subject: ISS is above & visible!!\n\n " \
              f"Hey, ISS is now at {iss_latitude} and {iss_longitude}." \
              f"\n Your house is at {MY_LAT}, {MY_LONG}"
        send_email(msg)
    print(iss_latitude, iss_longitude)
    time.sleep(120)
