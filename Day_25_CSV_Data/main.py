
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(temperatures)


# from numpy.lib.function_base import average
# import pandas as pd

# data = pd.read_csv("weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# average = sum(temp_list) / len(temp_list)
# print(average)

#Get Data in Column
# print(data["temp"].mean())
# print(data["temp"].max())

import pandas as pd

# data = pd.read_csv("weather_data.csv")

#Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday.temp = int(monday.temp)
# fahrenheit = (monday.temp * 9/5) + 32
# print(fahrenheit)

#Create DataFrame from Scratch
# data_dict = {
#     "students": ["Amy","James","Angela"],
#     "scores": [76, 56, 65]
# }

# data = pd.DataFrame(data_dict)
# data.to_csv("new_data.csv")


import pandas as pd

"""

Fur Color,Count
0,grey,2473
1,red,392
2,black,103

"""

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = len(data[data["Primary Fur Color"] == "Gray"]) 
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

# gray_count = len(gray)
# red_count = len(red)
# black_count = len(black)

data_dict = {
    "Fur Color" : ["gray", "red", "black"],
    "Count" : [gray, red, black]
}

new_data = pd.DataFrame(data_dict)
new_data.to_csv("squirrel_count.csv")


























