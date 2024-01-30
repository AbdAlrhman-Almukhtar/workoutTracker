import requests
from datetime import datetime

APP_ID = "bf5370f6"
API_KEY = "4707121178158b341c79c41a659c54a3"
USER = "abdalrhman"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": USER,
}

query = input("Write your workout: ")
par = {
    "query": query,
    "gender": "male",
    "weight_kg": 68.4,
    "height_cm": 175.0,
    "age": 20
}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",
                         json=par,
                         headers=headers)
response.raise_for_status()
response = response.json()
print(response)
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for i in response["exercises"]:
    exercisePar = {
        "sheet1": {
         "date": today_date,
         "time": now_time,
         "exercise": i["name"].title(),
         "duration": i["duration_min"],
         "calories": i["nf_calories"]}
    }
    exerciseHeader = {
        "Authorization": "Basic YWJkYWxyaG1hbjphem1uMTIzNA=="
    }
    exerciseResponse = requests.post(url="https://api.sheety.co/34f8e3f3e171ad0f57b1bf74903acce5/workingOut/sheet1",
                                     json={"sheet1": exercisePar},
                                     auth=(
                                         "abdalrhman",
                                         "azmn1234"
                                     )
                                     )

    print(exerciseResponse.text)
