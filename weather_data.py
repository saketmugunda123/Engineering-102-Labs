# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Saket Mugunda
# Section: 217
# Assignment: 11.13
# Date: 11/10/2023

#Getting data from file
weather = open("WeatherDataCLL.csv",'r')
weatherData = []
for line in weather:
    weatherData.append(line)
weather.close()

weatherData = [date.strip() for date in weatherData]

weatherDatav2 = []
for date in weatherData:
    weatherDatav2.append(date.split(','))
   
#Getting maximum
maxList = []
i = 1
while i < len(weatherDatav2):
    temp = weatherDatav2[i][5]
    if temp != '':
        maxList.append(int(temp))
    i+=1
maxList = [int(temp) for temp in maxList]
maximum = max(maxList)
print(f'10-year maximum temperature: {maximum} F')


#Getting minimum
minList = []
i = 1
while i < len(weatherDatav2):
    temp = weatherDatav2[i][6]
    if temp != '':
        minList.append(int(temp))
    i+=1
minList = [int(temp) for temp in minList]
minimum = min(minList)
print(f'10-year minimum temperature: {minimum} F')

#Format the dates from numbers to words

Dates = []
j = 1
while j < len(weatherDatav2):
    date = weatherDatav2[j][0]
    if date != '':
        Dates.append(date)
    j+=1

datesFinal = []
for date in Dates:
    temp = date.split('/')
    datesFinal.append(temp)

months = {'1': 'January','2':'February','3':'March','4':'April','5':'May','6':'June',
          '7':'July','8':'August','9':'September','10':'October','11':'November','12':'December',
}

k = 0
datesFinalv2 = []
while k < len(datesFinal):
    if datesFinal[k][0] in months:
        datesFinal[k][0] = months[datesFinal[k][0]]
    k+=1

monthInput = input("Please enter a month: ")
yearInput = input("Please enter a year: ")
print(f'For {monthInput} {yearInput}:')

k = 0 
count = 0
while k < len(datesFinal):
    if monthInput in datesFinal[k] and yearInput in datesFinal[k]:
        startIndex = k + 1
        break
    k+=1

if monthInput == 'January' or monthInput == 'March' or monthInput == 'May' or monthInput == 'July' or monthInput == 'August' or monthInput == 'October' or monthInput == 'December':
    endIndex = startIndex + 31
elif monthInput == 'April' or monthInput == 'June' or monthInput == 'September' or monthInput == 'November':
    endIndex = startIndex + 30
else:
    endIndex = startIndex + 28


#avg temperature of avg temps
avgTemps = []
for i in range(startIndex,endIndex):
    temp = weatherDatav2[i][4]
    if temp != '':
        avgTemps.append(temp)

avgTemps = [int(temp) for temp in avgTemps]
averageTemperature = (sum(avgTemps))/len(avgTemps)
print(f'Mean average daily temperature: {averageTemperature:.1f} F')

#avg relative humidity
avgRhumid = []
for i in range(startIndex,endIndex):
    temp = weatherDatav2[i][3]
    if temp != '':
        avgRhumid.append(temp)

avgRhumid = [int(temp) for temp in avgRhumid]
averageHumidity = (sum(avgRhumid))/len(avgRhumid)
print(f'Mean relative humidity: {averageHumidity:.1f}%')

#Avg daily wind
avgWind = []
for i in range(startIndex,endIndex):
    temp = weatherDatav2[i][1]
    if temp != '':
        avgWind.append(temp)

avgWind = [float(temp) for temp in avgWind]
averageWind = (sum(avgWind))/len(avgWind)
print(f'Mean daily wind speed: {averageWind:.2f} mph')


#avg days of precipitation
avgPrecipation = []
for i in range(startIndex,endIndex):
    temp = weatherDatav2[i][2]
    if temp != '':
        if temp != '0':
            avgPrecipation.append(temp)


averagePrecipation = (len(avgPrecipation)/(endIndex - startIndex))*100
print(f'Percentage of days with precipitation: {averagePrecipation:.1f}%')



