import requests

api_key = "0LV9FZHzDjs6o5ttpfAO0ySC2cSiCC6h"
endpoint = "https://api.tequila.kiwi.com/v2"

class FlightData():
    def find_cheap(self, city):
        #This class is responsible for structuring the flight data.
        endpoint1 = f"{endpoint}/search"
        headers = {
            "apikey": api_key
        }
        parameters = {
            "fly_from" : "LON",
            "fly_to" : city,
            "date_from" : "31/03/2023",
            "date_to" : "30/09/2023",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(url=endpoint1, headers=headers, params=parameters)
        print(response.json()["data"][0])

fd = FlightData()
fd.find_cheap("BER")