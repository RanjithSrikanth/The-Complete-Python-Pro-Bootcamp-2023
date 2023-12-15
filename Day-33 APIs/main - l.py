# import requests
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # print(response)
# response.raise_for_status()
#
# data = response.json()
# print(data)
#
# longitude = data["iss_position"]["longitude"]
# # print(longitude)
# latitude = data["iss_position"]["latitude"]
# # print(latitude)
# position = (latitude, longitude)
# print(position)

import requests
from datetime import datetime

MY_LATITUDE = 20.593683
MY_LONGITUDE = 78.962883

parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# print(data)
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
print(sunrise)
print(sunset)

time = datetime.now()
print(time.hour)









