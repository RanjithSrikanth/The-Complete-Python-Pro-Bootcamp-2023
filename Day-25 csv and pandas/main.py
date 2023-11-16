# with open("weather_data.csv", "r") as file:
#     listt = file.readlines()
#     print(listt)

# import csv
#
# with open("weather_data.csv", "r") as file:
#     data = csv.reader(file)
#     temperature = []
#     for i in data:
#         # print(i)
#         if i[1] != "temp":
#             temperature.append(int(i[1]))
#     print(temperature)

import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(data)
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)

# data_l = data["temp"].to_list()
# # print((sum(data_l) / len(data_l)))
# print(data["temp"].max())

# row calling
# print(data[data["day"] == "Monday"])
# print( data[data["temp"] == data["temp"].max()])
#
# monday = data[data["day"] == "Monday"]
# print(monday.temp * 9/5 + 32)


# #creating a dataframe from scratch
# data_dict = {
#     "student": ["Ranjith", "Ramesh", "Suresh"],
#     "marks": [10, 20, 30]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
#
# data.to_csv("data_dict.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# print(len(data[data["Primary Fur Color"] == "Black"]))

black = data[data["Primary Fur Color"] == "Black"]
black_c = len(black)

gray = data[data["Primary Fur Color"] == "Gray"]
gray_c = len(gray)

cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
cinnamon_c = len(cinnamon)

dict_squirrel = {
    "Fur Color" : ["black", "gray", "cinnamon"],
    "count" : [black_c, gray_c, cinnamon_c]
}
# print(dict_squirrel)

csv_data = pandas.DataFrame(dict_squirrel)
csv_data.to_csv("Squirrel.csv")

# data1 = pandas.read_csv("Squirrel.csv")
# print(data1)