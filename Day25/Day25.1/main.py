import csv
import pandas

# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#
# with open("weather_data.csv") as csv_data_file:
#     data = csv.reader(csv_data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


data = pandas.read_csv("weather_data.csv")
#print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
avg_temp = data["temp"].mean()
print(avg_temp)
max_temp = data["temp"].max()
print(max_temp)

#Get data in columns
print(data["condition"])
print(data.condition)

#Get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9 / 5 + 32
print(monday_temp_F)

#Create a dataframe from scratch
data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}

df = pandas.DataFrame(data_dict)
print(df)

df.to_csv("new_data.csv")