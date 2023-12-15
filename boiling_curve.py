# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Saket Mugunda
# Section: 217
# Assignment: 5.4
# Date: 09/25/2023

from math import *

#First put the points in terms of variables
temp = float(input("Enter the excess temperature: "))
Ax = 1.3
Ay = 1000
Bx = 5
By = 7000
Cx = 30
Cy = 1.5*(10**6)
Dx = 120
Dy = 2.5 *(10**4)
Ex = 1200
Ey = 1.5 *(10**6)

#Depending on the range in which the temperature is in, it'll be calculated with a different slope and different inital point
#Print statement in each conditional with varying heatFlux value rounded to nearest integer
#Different slope from temp 1 to 5
#Different slope from temp 5 to 30
#Different slope from temp 30 to 120
#Different slope from temp 120 to 1200
#Same format for each value of heatflux when printed
if temp >=1 and temp <5:
    m = (log(By/Ay))/(log(Bx/Ax))
    heatFlux = Ay*((temp/Ax)**m)
    print(f'The surface heat flux is approximately {heatFlux:.0f} W/m^2')
elif temp>=5 and temp<30:
    m = (log(Cy/By))/(log(Cx/Bx))
    heatFlux = By*((temp/Bx)**m)
    print(f'The surface heat flux is approximately {heatFlux:.0f} W/m^2')
elif temp >=30 and temp<120:  
    m = (log(Dy/Cy))/(log(Dx/Cx))
    heatFlux = Cy*((temp/Cx)**m)
    print(f'The surface heat flux is approximately {heatFlux:.0f} W/m^2') 
    
elif temp>=120 and temp<1200:
    m = (log(Ey/Dy))/(log(Ex/Dx))
    heatFlux = Dy*((temp/Dx)**m)
    print(f'The surface heat flux is approximately {heatFlux:.0f} W/m^2')
else:
    #Represents the values of temperature that are outside the allowed interval
    print("Surface heat flux is not available")


