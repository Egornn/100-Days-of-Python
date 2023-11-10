import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

website = requests.get(URL).text
soup = BeautifulSoup(website, 'html.parser')
film_list = [x.text for x in soup.find_all('h3',class_='title')]
with open('Web\Movies Beautiful Soup (45)\ 100 Best Movies of All Time.txt', 'w', encoding='UTF-8') as file:
    film_list.reverse()
    file.writelines(title+"\n" for title in film_list)