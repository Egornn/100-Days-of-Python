import requests
from datetime import date, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

API_STOCK_KEY = "UMSW58VVAMXI6R7H"
API_NEWS_KEY = "39a1d03b2b1947a4b9ad396024bebea2"
MIN_CHANGE_STOCK = 0.05


def news_report(stock=STOCK):
    change_in_stock = fetch_stock_change(stock)
    if change_in_stock > MIN_CHANGE_STOCK or True:
        news = get_news(COMPANY_NAME)
        news_dictionary = {k.get("title"): k.get("url") for k in news[:3]}

        send_news(news_dictionary, change_in_stock)


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
# HINT 2: Work out the value of 5% of yesterday's closing stock price.


def fetch_stock_change(stock):
    dictionary = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": stock,
        "apikey": API_STOCK_KEY,
        "interval": "60min",
    }
    response = requests.get(STOCK_ENDPOINT, params=dictionary)
    today = date.today()
    yesterday = today - timedelta(days=1)
    time_series = response.json()["Time Series (60min)"]
    is_data_available = False
    while is_data_available == False:
        if time_series.get(f"{yesterday} 19:00:00") == None:
            yesterday = yesterday - timedelta(days=1)
        else:
            last_day_data = time_series.get(f"{yesterday} 19:00:00")
            is_data_available = True
    yesterday_close_price = (last_day_data.get('4. close'))
    is_data_available = False
    before_yesterday = yesterday - timedelta(days=1)
    while is_data_available == False:
        if time_series.get(f"{before_yesterday} 19:00:00") == None:
            before_yesterday = before_yesterday - timedelta(days=1)
        else:
            before_last_day_data = time_series.get(f"{before_yesterday} 19:00:00")
            is_data_available = True
    before_yesterday_close_price = (before_last_day_data.get('4. close'))
    return abs(float(yesterday_close_price) / float(before_yesterday_close_price) - 1)


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
# HINT 1: Think about using the Python Slice Operator
def get_news(company_name):
    params = {
        "q": company_name,
        "apiKey": API_NEWS_KEY,
    }
    response = requests.get(NEWS_ENDPOINT, params=params)
    return response.json().get('articles')


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
# HINT 1: Consider using a List Comprehension.
def send_news(news: {str: str}, change: float, stock=STOCK):
    account_sid = 'ACd2eb03ed855f2a4c9c279a786bfe234f'
    auth_token = 'ebd2b0f61a71489bc94a994a48f74d95'
    client = Client(account_sid, auth_token)
    if change > 0:
        change = f"🔺{change * 100}%"
    else:
        change = f"🔻{change * -100}%"
    for title in news.keys():
        message = client.messages.create(
            from_='+447361593525',
            to='+447469637234',
            body=f'Stock:{stock}\n{change}\ntitle:{title}\nURL:{news.get(title)}'
        )

    return


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

if __name__ == "__main__":
    news_report(STOCK)
