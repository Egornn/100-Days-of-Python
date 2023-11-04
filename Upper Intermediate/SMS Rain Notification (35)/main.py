import requests
from twilio.rest import Client
import os

API_KEY = "55f5be3c9c05d1932de255c8fed7ca0c"
MY_LAT = 51.491640
MY_LONG = -0.287096
ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
MESSAGE = {'True': 'Today is gonna be raining. Bring an umbrella!', "False": "It's sunny"}


def is_raining(weather_response, next_hours: int = 13) -> bool:
    for i in range(min(next_hours, len(weather_response.get("list")))):
        if len(weather_response.get("list")[i].get("weather")) > 0:
            if weather_response.get("list")[i].get("weather")[0].get("id") < 700:
                return True
    return False


params = {
    'lat': MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "units": 'metric',
}

response = requests.get(ENDPOINT, params=params)
response.raise_for_status()
weather_data = response.json()

account_sid = 'ACd2eb03ed855f2a4c9c279a786bfe234f'
auth_token = 'ebd2b0f61a71489bc94a994a48f74d95'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+447361593525',
    to='+447469637234',
    body=MESSAGE[str(is_raining(weather_data))]
)

print(message.sid)
