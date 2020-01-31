# Josh Jacobsen - MW 2:30pm
# CSV_Project

import matplotlib.pyplot as plt
import csv
from datetime import datetime

open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

#Shows that the header row is a list
print(type(header_row))

#Loop through columns and print name and index
for index,column_header in enumerate(header_row):
    print(index,column_header)

#Create list and append high termperatures and dates
highs = []
dates = []
lows = []
for row in csv_file:
    try:
        high = int(row[4])
        low = int(row[5])
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
    except ValueError:
        print(f'Missing data for {current_date}')
    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)

#Print 0-9 (top 10) from highs
print(highs[:10])
print(dates[:10])

fig = plt.figure()

#Formating
plt.plot(dates, highs, color="red", alpha=0.5)
plt.plot(dates, lows, color="blue", alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue',alpha=0.1)
plt.title("Daily High Temps, July 2018",fontsize=16)
plt.xlabel("",fontsize=10)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both",which="major",labelsize=12)

fig.autofmt_xdate()

#plt.plot([1,2,3,4,5],color='red')
plt.show()