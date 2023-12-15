# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Saket Mugunda
# NAME OF TEAM MEMBER 2 Aarjav Vani
# NAME OF TEAM MEMBER 3 Prayag Peram
# NAME OF TEAM MEMBER 4 Sankarshan Singh
# Section: 217
# Assignment: 6.12
# Date: 10/2/2023
import math
from math import *

#Getting input values and setting surface area to 0
s_length = float(input("Enter the side length in meters: "))
layers = float(input("Enter the number of layers: "))
s_area = 0.0


constant = sqrt(3)/4
l2 = s_length**2

#using summation formula (n)(n+1)/2 with layers
sides = ((((layers)*(layers+1))/2)*3)*l2

#Getting sum of top and bottom
topSum = ((1/6)*layers*(layers+1)*(2*layers+1))*constant*l2
tempLayer = layers-1
bottomSum = ((1/6)*tempLayer*(tempLayer+1)*(2*(tempLayer)+1))*constant*l2

#accounting for layers =1
if layers ==1:
    s_area += (3*l2) + (constant*l2)
else:
    s_area = sides + topSum - bottomSum

#output statement
print(f'You need {s_area:0.2f} m^2 of gold foil to cover the pyramid')