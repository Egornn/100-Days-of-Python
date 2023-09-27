import requests
from datetime import datetime
import os

APP_ID_38 = os.environ["APP_ID_38"]
API_KEY_38 = os.environ["API_KEY_38"]
ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/5ca3135dd8eec0f8c2feea42d263d450/myWorkouts/workouts"
SHEETY_API_38 = os.environ["SHEETY_API_38"]
HEIGHT = 183.0
WEIGHT = 74.3
AGE = 28
SEX = "male"


def get_nutrients(exercise):
    products_params = {
        "query": exercise,
        "gender": SEX,
        "weight_kg": WEIGHT,
        "height_cm": HEIGHT,
        "age": AGE

    }
    header = {
        "x-app-id": APP_ID_38,
        "x-app-key": API_KEY_38,
        "Content-Type": "application/json",
    }
    response = requests.post(url=ENDPOINT, json=products_params, headers=header)
    return response.json()


def post_exercises(exercises):
    header = {"Authorization": f"Bearer {SHEETY_API_38}"}
    for exc in exercises['exercises']:
        exercises_params = {
            "workout": {
                "date": datetime.now().strftime("%d/%m/%Y"),
                "time": datetime.now().strftime("%H:%M:%S"),
                "exercise": exc["name"].title(),
                "duration": exc['duration_min'],
                "calories": exc['nf_calories'],
            }
        }
        sheet_response = requests.post(SHEETY_ENDPOINT, json=exercises_params, headers=header)
        print(sheet_response)
    return


if __name__ == "__main__":
    input_text = input("Tell me which exercises you did: ")
    post_exercises(get_nutrients(input_text))
