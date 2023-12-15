# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Saket Mugunda
# Section: 217
# Assignment: 4.19
# Date: 09/12/2023


from math import *
#Getting input for coefficients
a = float(input("Please enter the coefficient A: "))
b = float(input("Please enter the coefficient B: "))
c = float(input("Please enter the coefficient C: "))

#First checks if there are roots then solves for roots
if a == 0 and b ==0:
    print("You entered an invalid combination of coefficients!")
if a== 0 and (b != 0):
    root = (-c)/(b)
    print("The root is x =", root)
if b**2 - (4*a*c) == 0:
    root = -b/(2*a)
    print("The root is x =", root)
elif b**2 - (4*a*c) < 0:
    root = sqrt(abs((b**2)-(4*a*c)))
    root1 = (-b)/(2*a)
    print("The roots are x =",root1,"+",str((root)/(2*a))+'i',"and x =",root1,str((-1*root)/(2*a))+'i' )    
else:
    root1 = (-b + (sqrt((b**2) - (4*a*c)))) / (2*a)
    root2 = (-b - (sqrt((b**2) - (4*a*c)))) / (2*a)
    print("The roots are x =", root1,"and x =", root2)
    
