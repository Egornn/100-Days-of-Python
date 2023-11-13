from bs4 import BeautifulSoup
import requests
from datetime import datetime
import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth

PART1="06b9421748ff4081"
PART2="9f96a8a26961"
YOUR_APP_CLIENT_ID = f"{PART1}ae91d2e3f91b7218"
YOUR_APP_CLIENT_SECRET = f'e59135eed0244ddead4f{PART2}'
YOUR_APP_REDIRECT_URI = "http://example.com "


URL="https://www.billboard.com/charts/hot-100/"

def input_date():
    date =""
    while not check_date(date):
        date = input("What year do you want travel to? Please input the date in a format dd-mm-yyyy: ")
    date = date.split("-")
    date.reverse()
    date_output = "-".join(date)
    return date_output
    
def check_date(date):
    try:
        date_obj = datetime.strptime(date, "%d-%m-%Y")
        current_date= datetime.now()
        if current_date>date_obj:
            return True
        else:
            return False
    except:
        return False

date = input_date()
site_response = requests.get(URL+date)
soup = BeautifulSoup(site_response.text, "html.parser")
required_classes = ["c-title", "a-no-trucate", "a-font-primary-bold-s", "u-letter-spacing-0021"]
pattern = re.compile(r'\b' + r'\b.*\b'.join(required_classes) + r'\b')
song_names=[x.text.strip() for x in soup.find_all('h3', class_=pattern)]


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR_APP_CLIENT_ID",
                                               client_secret="YOUR_APP_CLIENT_SECRET",
                                               redirect_uri="YOUR_APP_REDIRECT_URI",
                                                scope="playlist-modify-private",
))

user = sp.current_user()
playlist_name = f"Best 100 Songs of {date}"
playlist_description = "Best 100 Songs of {date} According to Billboard.com"
playlist = sp.user_playlist_create(user['id'], playlist_name, public=False, description=playlist_description)
for song_name in song_names:
    results = sp.search(q=song_name, type="track", limit=1)
    if results['tracks']['items']:
        track_uri = results['tracks']['items'][0]['uri']
        sp.playlist_add_items(playlist['id'], [track_uri])



