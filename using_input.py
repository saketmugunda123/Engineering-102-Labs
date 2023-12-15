# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Saket Mugunda
# Section: 217
# Assignment: 3.17
# Date: 08/22/2023

from math import *

#Calculating Force
print("This program calculates the applied force given mass and acceleration")
mass = float(input("Please enter the mass (kg): "))
acceleration = float(input("Please enter the acceleration (m/s^2): "))
force = mass*acceleration
print(f'Force is {force:.1f} N')
print()

#Calculating Wavelength
print("This program calculates the wavelength given distance and angle")
distance = float(input("Please enter the distance (nm): "))
angle = float(input("Please enter the angle (degrees): "))
wavelength = (2*distance*sin(angle*pi/180))
print(f'Wavelength is {wavelength:.4f} nm')
print()

#Calculating Remaining Grams
print("This program calculates how much Radon-222 is left given time and initial amount")
time = float(input("Please enter the time (days): "))
initial_amount = float(input("Please enter the initial amount (g): "))
grams =initial_amount*(2**(-time/3.8))
print(f'Radon-222 left is {grams:.2f} g')
print()

#Calculating Pressure
print("This program calculates the pressure given moles, volume, and temperature")
moles = float(input("Please enter the number of moles: "))
volume = float(input("Please enter the volume (m^3): "))
temperature = float(input("Please enter the temperature (K): "))
pressure = (moles*8.314*temperature)/(volume*1000)-(10**-14)
print(f'Pressure is {pressure:.0f} kPa')
