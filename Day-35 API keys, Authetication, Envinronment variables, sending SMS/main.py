import requests
from twilio.rest import Client


api_key = "182ffa80f024baf208f09b444b658bc5"
account_sid = "ACcb6d810a204002f2ac0d033e07a684f2"
auth_token = "dd233d277b432303489b5102e988ebd4"
endpoint = "https://api.openweathermap.org/data/2.5/weather"

parameters = {
    "lat" : 30.50,
    "lon" : 70.52,
    "appid" : api_key,
    # "exclude" : "main, wind, clouds, sys, coord"
}

response = requests.get(endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()["weather"][0]["id"]
# print(weather_data)

# will_rain

if weather_data > 700:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="its gonna rain today, bring umbrella ☂ !!!",
        from_='+14753488807',
        to='+919585148852'
    )

print(message.status)