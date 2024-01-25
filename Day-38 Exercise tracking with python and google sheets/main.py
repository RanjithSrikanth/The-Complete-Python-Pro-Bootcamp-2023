import requests
from datetime import datetime

APP_ID = "bed64a31"
N_API_KEY = "d4da258d0918d7415f8e527502672ab6"
N_END_POINT = "https://trackapi.nutritionix.com//v2/natural/exercise"

sheety_endpoint = "https://api.sheety.co/3b5f3c7dbe031b0bf29940054e9de40b/workoutTracking/workouts"

header = {
    "x-app-id" : APP_ID,
    "x-app-key" : N_API_KEY,
}

parameter = {
    "query" : input("Enter activity : "),
    "gender" : "male",
    "weight_kg" : 45,
    "height_cm" : 45,
    "age" : 19,
}

response = requests.post(url=N_END_POINT, json=parameter, headers=header)
data = response.json()
print(data)

today_date = datetime.now().strftime("%d/%m/%y")
now_time = datetime.now().strftime("%X")

for i in data["exercises"]:
    # print(i["name"])
    parameter_add = {
        "workout" : {
            "date" : today_date,
            "time" : now_time,
            "exercise" : i["name"].title(),
            "duration" : i["duration_min"],
            "calories" : i["nf_calories"],
        }
    }
    add_response = requests.post(url=sheety_endpoint, json=parameter_add, auth=("Ranjithhh", "Ranjithhh28*"))
    print(add_response.json())
# print(data["exercises"][0]["name"])

