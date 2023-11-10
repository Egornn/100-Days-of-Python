from bs4 import BeautifulSoup
# import lxml #alternative parser
import requests


URL = 'https://news.ycombinator.com/'

site = requests.get(URL).text
soup =BeautifulSoup (site, 'html.parser')
# link_list = soup.find_all(class_='titleline')
# for link in link_list: print (link)
points_list = soup.find_all(class_='score')
max_points = 0
for score in points_list:
    current_score = int(score.text.replace(" points",""))
    if current_score>max_points:
        max_points= current_score
        id = score.get('id')
        print(id)
post_id = id.replace('score_','')

print(f'The post "{soup.find(id=str(post_id)).find(class_="titleline").text}" has the highest score of {max_points} points. Here is the link {soup.find(id=str(post_id)).find(class_="titleline").find("a").get("href")}')

# with open('c:/Users/Егор/100 Days of Python/Web/Movies Beautiful Soup (45)/website.html', mode='r') as f:
#     contents = f.read()

# soup = BeautifulSoup(contents, "html.parser")

# print(soup.title.string)

# print(soup.prettify()) 

# print(soup.li)

# list_li=[ x.getText() for x in soup.find_all(name='li')]
# print(list_li)

# list_anchors=[ x.get('href') for x in soup.find_all(name='a')]
# print(list_anchors)

# list_by_id = soup.find_all(id='name')
# print (list_by_id)

# list_by_class = soup.find_all(class_='heading')
# print(list_by_class)

# company_url =soup.select_one(selector='p a')
# print(company_url.get('href'))

# name = soup.select_one('#name')
# print(name)

# headings=soup.select('.heading')
# print(headings)

