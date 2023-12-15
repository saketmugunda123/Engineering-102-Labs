# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sangkarshan Singh, Prayag Peram, Saket Mugunda, Aarjav Vani
# Section:      217
# Assignment:   Lab 12.12
# Date:         18 11 2023
#As a team, we have gone through all required sections of the 
#tutorial, and each team member understands the material

#code
import numpy as np

A = np.arange(12).reshape(3,4)
B = np.arange(8).reshape(4,2)
C = np.arange(6).reshape(2,3)

print(f'A = {A}\n')
print(f'B = {B}\n')
print(f'C = {C}\n')

E = np.dot(A,B)
D = np.dot(E,C)
print(f'D = {D}\n')

X = np.transpose(D)
print(f'D^T = {X}\n')

Y = ((D)**(1/2))/2
print(f'E = {Y}')