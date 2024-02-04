from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data = DataManager()
fs =  FlightSearch()
# pprint(data.sdata)

data.get_rows()

for i in data.sdata:
    if len(i["iataCode"]) == 0:
        iata = fs.find_iatacode(i["city"])
        i["iataCode"] = iata

data.update_rows(data.sdata)
pprint(data.sdata)