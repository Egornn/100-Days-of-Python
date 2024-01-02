import requests
ENDPOINT = 'https://api.npoint.io/a42d996ee29a3a980836'


class Post:
    def __init__(self) -> None:
        blog_url = ENDPOINT
        self.blog_json= requests.get(url=blog_url).json()
        