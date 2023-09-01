from password import GOGGLE_PASS
import smtplib as smtplib
import datetime as dt
import random as rnd
import pandas as pd
import os
import time

MY_EMAIL = "egornnn@gmail.com"
RECEIVER = "egornnnn@gmail.com"
TEMPLATE_PATH = "templates/"


def generate_quote() -> str:
    with open('quotes.txt', "r") as q:
        lines = q.read().splitlines()
        quote = rnd.choice(lines)
    quote = quote.replace('"', "").replace(" - ", "\n")
    return quote


def send_email(message="Empty mail"):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, GOGGLE_PASS)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECEIVER,
                            msg=message)


def motivational_quote(day=0):
    if dt.datetime.now().weekday() == day:
        send_email(f"Subject: Monday Motivational Quote!\n\n {generate_quote()}")
    return


def happy_birthday():
    database = pd.read_csv('birthdays.csv')
    now = dt.datetime.now()
    to_send = database[(database["month"] == now.month) & (database["day"] == now.day)]
    if to_send.empty:
        return
    for line in to_send.iterrows():
        name, email = line[1]['name'], line[1]["email"]
        with open(file=f'{TEMPLATE_PATH}/{rnd.choice(os.listdir(TEMPLATE_PATH))}') as template:
            send_email(template.read().replace("[NAME]", name))


if __name__ == "__main__":
    motivational_quote()
    happy_birthday()
