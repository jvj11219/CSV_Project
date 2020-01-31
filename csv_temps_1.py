# Josh Jacobsen - MW 2:30pm
# CSV_Project

import matplotlib.pyplot as plt
import csv

open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

#Shows that the header row is a list
print(type(header_row))

#Loop through columns and print name and index
for index,column_header in enumerate(header_row):
    print(index,column_header)

#Create list and append high termperatures
highs = []
for row in csv_file:
    highs.append(int(row[5]))

#Print 0-9 (top 10) from highs
print(highs[:10])

#Formating
plt.plot(highs,color='red')
plt.title("Daily High Temps, July 2018",fontsize=16)
plt.xlabel("",fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both',which="major",labelsize=16)

#plt.plot([1,2,3,4,5],color='red')
plt.show()