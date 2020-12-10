import requests
import datetime as dt

NUTRITIONIX_APP_ID = ""
NUTRITIONIX_APP_KEY = ""
NUTRITIONIX_API_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_API_URL = "https://api.sheety.co/236ed8d960b740b1902dedb235c100ea/jackLeeWorkouts/workouts"
SHEETY_API_AUTH_BASIC = ""
GENDER = "male"


def get_exercise_stats() -> dict:
    query = input("Tell me which exercises you did: ")
    headers = {
        "x-app-id": NUTRITIONIX_APP_ID,
        "x-app-key": NUTRITIONIX_APP_KEY,
        "Content-Type": "application/json"
    }
    post_body = {
        "query": query,
        "gender": GENDER
    }

    response = requests.post(NUTRITIONIX_API_URL, json=post_body, headers=headers)
    response.raise_for_status()

    return response.json()


def save_exercise_stats(exercise_stats: dict):
    headers = {
        "Content-Type": "application/json",
        "Authorization": SHEETY_API_AUTH_BASIC
    }
    now = dt.datetime.now()

    for exercise in exercise_stats["exercises"]:
        post_body = {
            "workout": {
                "date": now.strftime("%d/%m/%Y"),
                "time": now.strftime("%X"),
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }

        response = requests.post(SHEETY_API_URL, json=post_body, headers=headers)
        response.raise_for_status()


def main():
    try:
        exercise_stats = get_exercise_stats()
        save_exercise_stats(exercise_stats)
    except Exception as ex:
        print(ex)


main()
