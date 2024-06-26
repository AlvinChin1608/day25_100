import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240530.csv")
grey_squirrels =  len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels =  len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels =  len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrels)
print(red_squirrels)
print(black_squirrels)

# Let's create our DataFrame using a dictionary
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels, red_squirrels, black_squirrels]
}

df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("squirrel_count.csv")  # Save in a new file