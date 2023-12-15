# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Saket Mugunda
# NAME OF TEAM MEMBER 2 Aarjav Vani
# NAME OF TEAM MEMBER 3 Prayag Peram
# NAME OF TEAM MEMBER 4 Sankarshan Singh
# Section: 217
# Assignment: 6.11
# Date: 09/27/2023

#obtaining inputs
length = float(input("Enter the side length in meters: "))
layers = int(input('Enter the number of layers: '))
from math import *

#Finding area of each triangle 
for i in range (1, layers +1):
    #inital triangle surface area includes of squares and triangle
    if i ==1:
        surfaceArea = 3*(i)*((length)**2) + (sqrt(3)/4)*(length)**2
    else:
        #Find the area of the squares of current layer
        squares= 3*(i)*(length**2)
        #subtract the area of the previous triangle from the current triangle to see the extra space
        triangle = (sqrt(3)/4)*(length*(i))**2 - (sqrt(3)/4)*(length*(i-1))**2
        #Add to surface area
        surfaceArea += squares
        surfaceArea += triangle
    
#Output statement
print(f'You need {surfaceArea:.2f} m^2 of gold foil to cover the pyramid')
