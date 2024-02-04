import requests
from pprint import pprint

API_key = "https://api.sheety.co/66ecabbcbd4d036e4d73470869010339/flightDealsC/prices"


class DataManager:
    def get_rows(self):
        response = requests.get(url=API_key)
        self.sdata = response.json()["prices"]
        # pprint(self.sdata)

    def update_rows(self, iata):
        for i in iata:
            updatable = {
                "price" : {
                "iataCode" : i["iataCode"]
            }
            }
            response = requests.put(url=f"{API_key}/{i['id']}", json=updatable)
            print(response.json())
