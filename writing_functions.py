# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Saket Mugunda
# Section: 217
# Assignment: 3.18
# Date: 08/22/2023

from math import *

side_length = float(input("Please enter the side length: "))

#function for area of triangle
def triangle(s):
    length = s
    height = sqrt(3)*(s/2)
    area = 0.5*length*height
    return area

#function for area of square
def square (s):
    area = s**2
    return area

#function for area of pentagon
def regular_pentagon(s):
    area = (0.25)*(sqrt(5*(5+(2*sqrt(5)))))*(s**2)
    return area

#function for area of dodecagon
def regular_dodecagon(s):
    area = 3*(2+(sqrt(3)))*(s**2)
    return area

print(f'A triangle with side {side_length:.2f} has area {triangle(side_length):.3f}')
print(f'A square with side {side_length:.2f} has area {square(side_length):.3f}')
print(f'A pentagon with side {side_length:.2f} has area {regular_pentagon(side_length):.3f}')
print(f'A dodecagon with side {side_length:.2f} has area {regular_dodecagon(side_length):.3f}')