import requests
from datetime import datetime

PIXELA_ENPOINT = "https://pixe.la/v1/users"
USERNAME = 'tuntis'
TOKEN = "Tuntis_53_19&Egornn+95"
ID = 'kcalcounter'


def set_account():
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": 'yes',
    }
    response = requests.post(url=PIXELA_ENPOINT, json=user_params)
    print(response.text)


def set_graph():
    graph_endpoint = f"{PIXELA_ENPOINT}/{USERNAME}/graphs"
    graph_config = {
        'id': ID,
        'name': "Kcal",
        'unit': 'Calories',
        "type": "int",
        'color': "ajisai",
    }
    headers = {
        "X-USER-TOKEN": TOKEN
    }
    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response.text)


def add_pixel(point_value, date):
    pixel_endpoint = f"{PIXELA_ENPOINT}/{USERNAME}/graphs/{ID}"
    pixel_data = {
        "date": date,
        "quantity": str(point_value),
    }
    headers = {
        "X-USER-TOKEN": TOKEN
    }
    response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
    print(response.text)


def update_pixel(point_value, date):
    pixel_endpoint = f"{PIXELA_ENPOINT}/{USERNAME}/graphs/{ID}/{date}"
    pixel_data = {
        "quantity": str(point_value),
    }
    headers = {
        "X-USER-TOKEN": TOKEN
    }
    response = requests.put(url=pixel_endpoint, json=pixel_data, headers=headers)


def del_pixel(date):
    pixel_endpoint = f"{PIXELA_ENPOINT}/{USERNAME}/graphs/{ID}/{date}"
    headers = {
        "X-USER-TOKEN": TOKEN
    }
    response = requests.delete(url=pixel_endpoint, headers=headers)


if __name__ == "__main__":
    add_pixel(1900, datetime.now().strftime("%Y%m%d"))
    update_pixel(2000, datetime.now().strftime("%Y%m%d"))
    del_pixel(datetime.now().strftime("%Y%m%d"))
