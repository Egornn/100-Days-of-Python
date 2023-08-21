import csv
import pandas

weather = []
with open("weather_data.csv", mode='r', encoding='utf-8') as fdata:
    weather_data = csv.reader(fdata)
    temperature = [int(x[1]) for x in weather_data if x[1].isdigit()]
# print(temperature)

data = pandas.read_csv("weather_data.csv")
# print(data)
print(data["temp"])
print(type(data))

data_dict = data.to_dict()
print(data_dict)
temperature_list = data["temp"].to_list()
print(f'Average Temperature is {"%.2f" % data["temp"].mean()}')
print(f'Max Temperature is {data["temp"].max()}')
print(data.condition)

# Get a row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(f'Temperature on Monday in F is {monday.temp * 9 / 5 + 32}')

# Create some data
data_dict = {
    'students': ['Amy', "Bob", "Charlie"],
    "score": [100, 99, 98]
}
data_students = pandas.DataFrame(data_dict)
print(data_students)
data_students.to_csv("students.csv")

# Squirrel data
# How many squirrels of different colors
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
colors = squirrel_data["Primary Fur Color"].value_counts()
print(colors)
colors_bad_way = (squirrel_data['Primary Fur Color'].unique())
color_dict = {
    'Fur color': list(colors_bad_way),
    "Count": [len(squirrel_data[squirrel_data['Primary Fur Color'] == x]) for x in colors_bad_way]
}
print(color_dict)
pandas.DataFrame(color_dict).to_csv("squirrel count bad.csv")
colors.to_csv("squirrel count.csv")
