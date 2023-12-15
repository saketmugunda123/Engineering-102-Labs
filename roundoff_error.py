# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Saket Mugunda
# Section: 217
# Assignment: 4.17
# Date: 09/12/2023

############ Part A ############
#comparing a, b, c, d, and f
a = 1/7
print(f'a = {a}')
b = a*7
print(f'b = a * 7 = {b}')
#No, instead b is rounded to 1.0 rather than 1


c = 2*a
d = 5*a
f = c+d
print(f'f = 2 * a + 5 * a = {f}')
# f takes on the value of 0.999 repeating rather than 1

############ Part B ############
from math import sqrt
#comparing values x, y, and z
x = sqrt(1/3)
print(f'x = {x}')
y = x*x*3
print(f'y = x * x * 3 = {y}')
z = x*3*x
print(f'z = x * 3 * x = {z}')
#No y is equal to 1.0 and z is equal to 0.9 repeating
TOL = 1e-10
#check if b and f are equal within specified tolerance 
if abs(b-f) < TOL:
    print(f'b and f are equal within tolerance of {TOL}')
else:
    print (f'b and f are NOT equal within tolerance of {TOL}')

if abs(y-z) < TOL:
    print(f'y and z are equal within tolerance of {TOL}')
else:
    print (f'y and z are NOT equal within tolerance of {TOL}')

############ Part C ############
#Comparing values m, n, p, and q
m = 0.1
print (f'm = {m}')
n = 3*m
print (f'n = 3 * m = 0.3 {n==0.3}')
p = 7*m
print (f'p = 7 * m = 0.7 {p==0.7}')
q = n+p
print(f'q = n + p = 1 {q==1}')
