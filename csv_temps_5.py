# Josh Jacobsen - MW 2:30pm
# CSV_Project

import matplotlib.pyplot as plt
import csv
from datetime import datetime

#Load in File
death_valley_file = open("death_valley_2018_simple.csv", "r")
sitka_weather_file = open("sitka_weather_2018_simple.csv", "r")

#Read Files
sitka_weather_csv = csv.reader(sitka_weather_file, delimiter=",")
death_valley_csv = csv.reader(death_valley_file, delimiter=",")

#Get Headers
sitka_header_row = next(sitka_weather_csv)
death_valley_header_row = next(death_valley_csv)

#Display Data Type of the Header Row
#print(type(sitka_header_row))
#print(type(death_valley_header_row))

#Create Variables for Index Locations, Loop Through Headers, and Store Index Value Locations
sitka_low_loc = 0
sitka_high_loc = 0
sitka_date_loc = 0
sitka_station_loc = 0
death_valley_low_loc = 0
death_valley_high_loc = 0
death_valley_date_loc = 0
death_valley_station_loc = 0
for index,column_header in enumerate(sitka_header_row):
    if column_header == "NAME":
        sitka_station_loc = index
    if column_header == "DATE":
        sitka_date_loc = index
    if column_header == "TMAX":
        sitka_high_loc = index
    if column_header == "TMIN":
        sitka_low_loc = index
    #print(index,column_header)
for index,column_header in enumerate(death_valley_header_row):
    if column_header == "NAME":
        death_valley_station_loc = index
    if column_header == "DATE":
        death_valley_date_loc = index
    if column_header == "TMAX":
        death_valley_high_loc = index
    if column_header == "TMIN":
        death_valley_low_loc = index
    #print(index,column_header)

#Create list and Append High/Low Temps for Sitka
sitka_highs = []
sitka_dates = []
sitka_lows = []
sitka_station_name = ''
for row in sitka_weather_csv:
    try:
        sitka_high = int(row[sitka_high_loc])
        sitka_low = int(row[sitka_low_loc])
        current_date = datetime.strptime(row[sitka_date_loc], '%Y-%m-%d')
        sitka_station_name = row[sitka_station_loc]
    except ValueError:
        print(f'Missing data for {current_date}')
    else:
        sitka_highs.append(sitka_high)
        sitka_lows.append(sitka_low)
        sitka_dates.append(current_date)

#Create list and Append High/Low Temps for Death Valley
death_valley_highs = []
death_valley_dates = []
death_valley_lows  = []
death_valley_station_name = ''
for row in death_valley_csv:
    try:
        death_valley_high = int(row[death_valley_high_loc])
        death_valley_low = int(row[death_valley_low_loc])
        current_date = datetime.strptime(row[death_valley_date_loc], '%Y-%m-%d')
        death_valley_station_name = row[death_valley_station_loc]
    except ValueError:
        print(f'Missing data for {current_date}')
    else:
        death_valley_highs.append(death_valley_high)
        death_valley_lows.append(death_valley_low)
        death_valley_dates.append(current_date)

#Print 0-9 (Top 10) Values from Highs
#print(sitka_highs[:10])
#print(sitka_dates[:10])
#print(death_valley_highs[:10])
#print(death_valley_dates[:10])

#Create Subplots and Set Title
fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle("Temperature comparison between " + sitka_station_name + " and " + death_valley_station_name,fontsize=10)

#Format Sitka Subplot
ax1.plot(sitka_dates, sitka_highs, color="red", alpha=0.5)
ax1.plot(sitka_dates, sitka_lows, color="blue", alpha=0.5)
ax1.fill_between(sitka_dates, sitka_highs, sitka_lows, facecolor='blue',alpha=0.1)
ax1.set_title(sitka_station_name,fontsize=8)
ax1.tick_params(axis="both",which="major",labelsize=8)

#Format Death Valley Subplot
ax2.plot(death_valley_dates, death_valley_highs, color="red", alpha=0.5)
ax2.plot(death_valley_dates, death_valley_lows, color="blue", alpha=0.5)
ax2.fill_between(death_valley_dates, death_valley_highs, death_valley_lows, facecolor='blue',alpha=0.1)
ax2.set_title(death_valley_station_name,fontsize=8)
ax2.tick_params(axis="both",which="major",labelsize=8)

#Format Dates
fig.autofmt_xdate()

#Display Plots
plt.show()