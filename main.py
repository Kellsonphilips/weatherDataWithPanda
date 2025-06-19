
# How we could get our data in a list format

# weather_data = []
# with open("weather_data.csv") as weather_file:
#     all_data = weather_file.readlines()
#     for data in all_data:
#         new_data = data.strip("\n")
#         weather_data.append(new_data)
# print(weather_data)

# import csv
# using csv to manipulate data from our csv file

# with open("weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temp = int(row[1])
#             temperature.append(temp)
#     print(temperature)

import pandas
# using pandas to manipulate data from our csv file

# data = pandas.read_csv("weather_data.csv")
# temperature = data["temp"]
# # print(temperature)
#
# temp_list = data["temp"].to_list()
# # print(temp_list)
# average_temp = round(sum(temp_list) / len(temp_list), 2)
# print(average_temp)

# # Pandas methods for getting the max, min mean mode and median of a specific data series
# print(data["temp"].max())
# print(data["temp"].min())
# print(round(data["temp"].mean(), 2))
# print(data["temp"].median())
# print(data["temp"].mode())
#
# # we can also do it this way
# # removing the square brackets and pandas makes working with data easier
# print(data.temp.max())
# print(data.temp.min())
# print(round(data.temp.mean(), 2))
# print(data.temp.median())
# print(data.temp.mode())

# # getting a specific row of data from our data with a certain condition
# print(data[data.day == "Tuesday"])
# print(data[data.temp == data.temp.max()])
#
# # getting hold of monday temperature and converting it from celsius to fahrenheit
# monday = data[data.temp == data.temp.min()]
# monday_tempe = int(monday.temp)
# monday_tempe_F = ((9/5) * monday_tempe + 32)
# print(monday_tempe_F)

# Creating a Dataframe from scratch
# data_dic = {
#     "students": ["Philip", "John", "Micheal", "Grace"],
#     "scores": [86, 70, 88, 54]
# }
#
# student_data = pandas.DataFrame(data_dic)
# print(student_data)
# # converting our dataframe to a csv file
# student_data.to_csv("student_data.csv")

# # create the dataframe
# df = pandas.DataFrame(data)

# print(df.head())
# print(df.tail())

# getting a specific row of data from Central_Park_Squirrel_Census and manipulating the data to create a new csv file

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_color = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
black_color = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]
cinnamon_color = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]

gray = len(gray_color)
black = len(black_color)
cinnamon = len(cinnamon_color)

squirrel_dic = {
    "colors": ["Gray", "Cinnamon", "Black"],
    "squirrel count": [gray, cinnamon, black]
}

squirrel_color_data = pandas.DataFrame(squirrel_dic)
print(squirrel_color_data)

# converting squirrel color datat to a csv file
squirrel_color_data.to_csv("squirrel_color_data.csv")
