import pandas

# data = pandas.read_csv("weather_data.csv")
# data_to_dict = data.to_dict()
# print(data_to_dict)
# print(type(data))
# print(data["temp"].to_list())
# temperatures = data["temp"].to_list()
# print(sum(temperatures) / len(temperatures))
# print(data["temp"].mean())
# print(data.temp.max())
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(int(monday.temp) * (9 / 5) + 32)
# data_dict = {
#     "students": ["Joe", "Jane", "Jack"],
#     "scores": [8, 7, 1]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("student_scores.csv")

# TODO: Create CSV squirrel_count.csv containing the number of gray, cinnamon and black squirrels based on fur color.
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
black_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
gray_count = len(data[data["Primary Fur Color"] == "Gray"])

color_data = {
    "Fur Color": ["gray", "cinnamon", "black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

color_dataframe = pandas.DataFrame(color_data)
color_dataframe.to_csv("squirrel_count.csv")
