import csv
import pandas

# avg_tmp = 0
#
# data = pandas.read_csv("002 weather-data.csv")
#
# # data_dic = data.to_dict()
# # print(data_dic)
# #
# # data_list = data["temp"].to_list()
# # print(data_list)
# #
# # a = data.temp.max()
# # # print(f"average Temperature is: {a}")
# #
# #
# # print(data[data.temp == a])
#
# monday = data[data.day == "Monday"]
# temp_monday = int(monday.temp)
# temp_monday_f = (temp_monday * 9 / 5) + 32
# print(f"monday temp = {temp_monday_f}")
from collections import Counter

data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

# color_list = data["Primary Fur Color"].to_list()
# color_counters = Counter(color_list)
# df_counts = pandas.DataFrame(list(color_counters.items()), columns=['Fur Color', 'Count'])
#
# # Save the DataFrame to a CSV file
# df_counts.to_csv('fur_color_counts.csv', index=True)
# for color, count in color_counters.items():
#     print(f"There are {count} {color} fur(s).")


grey_s_count = len(data[data["Primary Fur Color"] == "Gray"])
Cinnamon_c_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_b_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_s_count)
print(Cinnamon_c_count)
print(black_b_count)

squirl_dic = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_s_count, Cinnamon_c_count, black_b_count]
}
#
df = pandas.DataFrame(squirl_dic)
df.to_csv("new data.csv")
