import csv
import pandas 

#with open("weather_data.csv") as file:
#    data = csv.reader(file)
#    tempereatures = []
#    for row in data:
#        if row[1] != "temp":
#            tempereatures.append(int(row[1]))

data = pandas.read_csv("weather_data.csv")

# print(data['temp'])

data_dict = data.to_dict()

temp_list = data["temp"].to_list()

avg_temp = sum(temp_list) / len(temp_list)
print(avg_temp)

print(data["temp"].mean())