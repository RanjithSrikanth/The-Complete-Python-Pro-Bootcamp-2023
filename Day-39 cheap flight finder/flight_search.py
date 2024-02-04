import requests

api_key = "0LV9FZHzDjs6o5ttpfAO0ySC2cSiCC6h"
endpoint = "https://tequila-api.kiwi.com"

class FlightSearch:
    def find_iatacode(self, city):
        urll = f"{endpoint}/locations/query"
        headers = {
            "apikey" : api_key
        }
        query = {
            "term" : city,
            "location_types" : "city"
        }
        response = requests.get(url=urll, headers=headers, params=query)
        result = response.json()["locations"]
        code = result[0]["code"]
        # code = result["code"]
        # print(code)
        return code

