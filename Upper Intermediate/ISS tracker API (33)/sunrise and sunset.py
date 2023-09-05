import requests
from datetime import datetime

LAT = 51.491640
LNG = -0.287096
my_position = {'lat': LAT, 'lng': LNG, "formatted": 0}
endpoint = "https://api.sunrise-sunset.org/json"

response = requests.get(endpoint, params=my_position)
if response.status_code != 200:
    raise response.raise_for_status()
sunrise = response.json()['results']['sunrise']
sunset = response.json()['results']['sunset']
sunset_hour = int(sunset.split('T')[1][0:2])
sunrise_hour = int(sunrise.split('T')[1][0:2])

now = datetime.now()
print(sunrise, now, sunset)

print(now.hour > sunset_hour or now.hour < sunrise_hour)
