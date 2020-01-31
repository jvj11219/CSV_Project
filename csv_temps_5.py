import matplotlib.pyplot as plt
import csv
from datetime import datetime

open_file_2 = open("death_valley_2018_simple.csv", "r")
open_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")
csv_file_2 = csv.reader(open_file_2, delimiter=",")

header_row = next(csv_file)
header_row_2 = next(csv_file_2)

#Shows that the header row is a list
print(type(header_row))
print(type(header_row_2))

#Loop through columns and print name and index
for index,column_header in enumerate(header_row):
    print(index,column_header)

for index,column_header in enumerate(header_row_2):
    print(index,column_header)

#Create list and append high termperatures and dates
highs_1 = []
dates_1 = []
lows_1 = []
for row in csv_file:
    try:
        high_1 = int(row[5])
        low_1 = int(row[6])
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
    except ValueError:
        print(f'Missing data for {current_date}')
    else:
        highs_1.append(high_1)
        lows_1.append(low_1)
        dates_1.append(current_date)

#Create list and append high termperatures and dates
highs_2 = []
dates_2 = []
lows_2  = []
for row in csv_file_2:
    try:
        high_2 = int(row[4])
        low_2 = int(row[5])
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
    except ValueError:
        print(f'Missing data for {current_date}')
    else:
        highs_2.append(high_2)
        lows_2.append(low_2)
        dates_2.append(current_date)

#Print 0-9 (top 10) from highs
print(highs_1[:10])
print(dates_1[:10])
print(highs_2[:10])
print(dates_2[:10])

#fig = plt.figure()
fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle("Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, VA US",fontsize=10)
ax1.plot(dates_1, highs_1, color="red", alpha=0.5)
ax1.plot(dates_1, lows_1, color="blue", alpha=0.5)
ax2.plot(dates_2, highs_2, color="red", alpha=0.5)
ax2.plot(dates_2, lows_2, color="blue", alpha=0.5)
ax1.fill_between(dates_1, highs_1, lows_1, facecolor='blue',alpha=0.1)
ax2.fill_between(dates_2, highs_2, lows_2, facecolor='blue',alpha=0.1)
ax1.set_title('SITKA AIRPORT, AK US',fontsize=8)
ax2.set_title('DEATH VALLEY, CA US',fontsize=8)
#ax2.xlabel("",fontsize=10)

ax1.tick_params(axis="both",which="major",labelsize=8)
ax2.tick_params(axis="both",which="major",labelsize=8)

#Formating
#plt.plot(dates, highs, color="red", alpha=0.5)
#plt.plot(dates, lows, color="blue", alpha=0.5)
#plt.fill_between(dates, highs, lows, facecolor='blue',alpha=0.1)
#plt.xlabel("",fontsize=10)
#plt.ylabel("Temperature (F)", fontsize=12)
#plt.tick_params(axis="both",which="major",labelsize=12)

fig.autofmt_xdate()

plt.show()