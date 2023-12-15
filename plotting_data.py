# # By submitting this assignment, I agree to the following:
# # "Aggies do not lie, cheat, or steal, or tolerate those who do."
# # "I have not given or received any unauthorized aid on this assignment."
# #
# # Name: Saket Mugunda
# # Section: 217
# # Assignment: 12.15
# # Date: 11/20/2023

#Getting data from file

import matplotlib.pyplot as plt
import numpy as np

weather = open("WeatherDataCLL.csv",'r')
weatherData = []
for line in weather:
    weatherData.append(line)
weather.close()

weatherData = [date.strip() for date in weatherData]

weatherDatav2 = []
for date in weatherData:
    weatherDatav2.append(date.split(','))



#For first graph of max temp and avg wind
dates = []
for i in range(len(weatherDatav2)-1):
    dates.append(i+1)

maxTemps = []
i = 1
while i < len(weatherDatav2):
    temp = weatherDatav2[i][5]
    if temp != '':
        maxTemps.append(int(temp))
    else:
        maxTemps.append(0)
    i+=1

windSpeed = []
i = 1
while i < len(weatherDatav2):
    temp = weatherDatav2[i][1]
    if temp != '':
        windSpeed.append(float(temp))
    else:
        windSpeed.append(0)
    i+=1


axis1 = plt.subplots()

# Plot the maximum temperature on the first y-axis
axis1.plot(dates, maxTemps, color='b', label='Max Temperature')
axis1.set_xlabel('Date')
axis1.set_ylabel('Max Temperature (°C)', color='b')

# Create a secondary y-axis for the average wind speed
axis2 = axis1.twinx()

# Plot the average wind speed on the second y-axis
axis2.plot(dates, windSpeed, color='r', label='Avg Wind Speed')
axis2.set_ylabel('Avg Wind Speed (m/s)', color='r')

# Title and legend
plt.title('Max Temperature and Avg Wind Speed Over Time')
plt.tight_layout()
plt.legend()

# Show the plot
plt.show()

#Plotting the histogram
ranges = np.arange(0, 24, 3)  
plt.hist(windSpeed, bins=ranges, edgecolor='black', alpha=0.7)
plt.xlabel('Average Wind Speed (m/s)')
plt.ylabel('Number of Days')
plt.title('Histogram of Average Wind Speed')
plt.show()

#creating the scatterplot
precipitation = []
i = 1
while i < len(weatherDatav2):
    temp = weatherDatav2[i][2]
    if temp != '':
        precipitation.append(float(temp))
    else:
        precipitation.append(0)
    i+=1

humidity = []
i = 1
while i < len(weatherDatav2):
    temp = weatherDatav2[i][2]
    if temp != '':
        humidity.append(float(temp))
    else:
        humidity.append(0)
    i+=1

plt.scatter(humidity, precipitation, marker='o', color='black')

plt.xlabel('Average Relative Humidity (%)')
plt.ylabel('Precipitation (mm)')
plt.title('Scatter Plot of Precipitation vs. Average Relative Humidity')

plt.show()





#Plotting the bar chart
def Month_datas():
    MD = {m: {'maximum_temperature': float('-inf'), 'minimum_temperature': float('inf'), 'mean_temp': 0, 'count': 0} for m in range(1, 13)}

    Weather = open('WeatherDataCLL.csv')
    for existing in Weather:
        existing = existing.strip()
        try:
            LD = existing.split(',')
            m = int(LD[0].split('/')[0])
            MT = float(LD[-2])
            minimum_temperature = float(LD[-1])

            MD[m]['maximum_temperature'] = max(MD[m]['maximum_temperature'], MT)
            MD[m]['minimum_temperature'] = min(MD[m]['minimum_temperature'], minimum_temperature)
            MD[m]['mean_temp'] += (MT + minimum_temperature) / 2
            MD[m]['count'] += 1
        except ValueError:
            continue
    Weather.close()


    for m in MD:
        if MD[m]['count'] > 0:
            MD[m]['mean_temp'] /= MD[m]['count']


    return MD



def Montlyh_tchart(MD):
    months = list(MD.keys())
    mean_temps = [MD[m]['mean_temp'] for m in months]
    MaximumTemps = [MD[m]['maximum_temperature'] for m in months]
    minimum_temperatures = [MD[m]['minimum_temperature'] for m in months]

    plt.plot(months, MaximumTemps, label='Highest T', marker='o', linestyle='--', color='red')
    plt.plot(months, minimum_temperatures, label='Lowest T', marker='o', linestyle='--', color='blue')
    plt.bar(months, mean_temps, label='Average Temperature', color='lightblue')

    plt.title('Temperature by Month')
    plt.xlabel('Month')
    plt.ylabel('Average Temperature (F)')
    plt.legend()
    plt.show()

MD = Month_datas()
Montlyh_tchart(MD)


