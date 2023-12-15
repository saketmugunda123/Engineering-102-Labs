# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Saket Mugunda
# Section: 217
# Assignment: 3.15
# Date: 09/06/2023

#converts pounds to force
def pounds_to_force(p):
    force = 4.44822*p
    return force

#converts m to ft
def meters_to_feet(m):
    feet = 3.28084*m
    return feet

#converts atmospheres to kilopascals
def atmospheres_to_kilopascals(a):
    kilopascals  =101.325*a
    return kilopascals

#converts watts to BTU per hour
def watts_to_BTU(w):
    BTU = w*3.412141633
    return BTU

#converts liters per second to gallons per minute
def literSecond_gallonMinute(l):
    liter = 15.850323141489*l
    return liter

#converts from Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    fahrenheit = (c*1.8) + 32
    return fahrenheit

#calling functions
value = float(input("Please enter the quantity to be converted: "))
print(f'{value:.2f} pounds force is equivalent to {pounds_to_force(value):.2f} Newtons')
print(f'{value:.2f} meters is equivalent to {meters_to_feet(value):.2f} feet')
print(f'{value:.2f} atmospheres is equivalent to {atmospheres_to_kilopascals(value):.2f} kilopascals')
print(f'{value:.2f} watts is equivalent to {watts_to_BTU(value):.2f} BTU per hour')
print(f'{value:.2f} liters per second is equivalent to {literSecond_gallonMinute(value):.2f} US gallons per minute')    
print(f'{value:.2f} degrees Celsius is equivalent to {celsius_to_fahrenheit(value):.2f} degrees Fahrenheit')


