# # Method 2 remember readline =! readlines
# # this method separated with comma is not ideal, takes lot of time
# with open("weather_data.csv", "r") as weather:
#     weather_data = list(weather.readlines())
#     print(weather_data)

import csv
import pandas

# Method 1
with open("weather_data.csv", "r") as weather:
    reader = csv.reader(weather)
    data = list(reader)
    print(data)

# Same thing
with open("weather_data.csv", "r") as weather:
    reader = csv.reader(weather)
    for row in reader:
        print(row)

print("\nChallenge 1")
# Challenge 1 - Separate the temperature in a list
with open("weather_data.csv", "r") as weather:
    reader = csv.reader(weather)
    next(reader)  # This line skip the header row if you only want the data
    temperatures = []
    for row in reader:
        temp_data = int(row[1])  # Only extract from index 1
        temperatures.append(temp_data)
    print(temperatures)

print("\nChallenge 1 another method")
# Challenge 1 again _ let's say that index 1 may have temp not on the header
with open("weather_data.csv", "r") as weather:
    reader = csv.reader(weather)
    temperatures = []
    for row in reader:
        if row[1] != "temp":
            temperatures.append(int(row[1]))  # Only extract from index 1
    print(temperatures)
# -----------------------------------------------------------------------------------------------
print("\n\nHere are the Pandas method")
"""
The top method are very lengthy and hard to work with, so we use Pandas library on tabular CSV data

https://pandas.pydata.org/docs/
"""

pandas_data = pandas.read_csv("weather_data.csv")
print(pandas_data)  # This look so much better that everything formatted in tabular format
print(pandas_data["temp"])  # name of that temp column, but it shows in series
print(type(pandas_data))  # Dataframe - 2 dimensional
print(type(pandas_data["temp"]))  # Series, 1-dimensional, basically equivalent to a column like a list

# Convert it to a dictionary
data_dict = pandas_data.to_dict()
print(data_dict)

# Turn python series to data list
temp_list = pandas_data["temp"].to_list()
print(temp_list)

# Let's find the avg temperature
temp_list = pandas_data["temp"].to_list()
average = sum(temp_list) / len(temp_list)
print(average)

# or the Pandas mean method to get the avg
print(pandas_data["temp"].mean())  # same result as above showing the average
print(pandas_data["temp"].max())  # The max value

# Get Data in Columns
print(pandas_data["condition"])  # header is case-sensitive
print(pandas_data.condition)  # same result, using those heading into attributes

# Get Data in Row
print(pandas_data[pandas_data.day == "Monday"])

# Challenge 2, which row has the highest temp of the week?
print(pandas_data[pandas_data.temp == pandas_data.temp.max()])

# Challenge 3, get Monday's temperature, and convert to Fahrenheit
monday = pandas_data[pandas_data.day == "Monday"]
monday_temp = (monday.temp[0] * (9/5)) + 32
print(monday_temp)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
create_dataframe = pandas.DataFrame(data_dict)  # convert Dict to DataFrame
print(create_dataframe)
create_dataframe.to_csv("new_data.csv")  # Save and create a CSV


