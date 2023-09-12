import requests


def pull_data():
    endpont = "https://opentdb.com/api.php"
    response = requests.get(endpont,
                            params={'amount': 10, 'category': 9, 'type': "boolean", 'difficulty': "medium"})
    if response.status_code != 200:
        response.raise_for_status()
        return
    else:
        question_data = response.json()
        return question_data["results"]


question_data = pull_data()
