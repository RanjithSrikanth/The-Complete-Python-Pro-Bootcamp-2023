import requests
from datetime import datetime

pixel_uname = "ranjith2828"
token = "28fdrewe20sdsf"

pixel_endpoint = "https://pixe.la/v1/users"
graph = f"{pixel_endpoint}/{pixel_uname}/graphs"

pixel_params = {
    "token" : token,
    "username" : pixel_uname,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

# response = requests.post(pixel_endpoint, json= pixel_params)
# print(response.text)
graph_params = {
    "id" : "graph1",
    "name" : "walking graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "shibafu"
}

headers = {
    "X-USER-TOKEN" : token,
}

# response = requests.post(graph, json=graph_params, headers=headers)
# print(response.text)

post_endpoint = f"{pixel_endpoint}/{pixel_uname}/graphs/graph1"


today = datetime.now()
# today = datetime(year=2023, month=3, day=27)
# date = today.date()
# print(today.strftime("%Y%m%d"))


# parameter = {
#     "date" : today.strftime("%Y%m%d"),
#     "quantity" : "7.0",
# }

parameter = {
    "quantity" : "3.0"
}
put_update_ep =  f"{pixel_endpoint}/{pixel_uname}/graphs/graph1/20230327"
response = requests.put(url = put_update_ep, json=parameter, headers=headers)
# response = requests.post(url=post_endpoint, json=parameter, headers=headers)

##use json() not text
print(response.json())


##delete without parameters, only header token

#take input from user to ask how many kms u walked today in quantity parameter and post

