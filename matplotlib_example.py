# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sangkarshan Singh, Prayag Peram, Saket Mugunda, Aarjav Vani
# Section:      217
# Assignment:   Lab 12.13
# Date:         11 18 2023
#As a team, we have gone through all required sections of the 
#tutorial, and each team member understands the material
import numpy as np
import matplotlib.pyplot as plt
import math

# PLOT 1
rangeX = np.linspace(-2.0, 2.0, 50)
f1 = 2.0 #width 1
f2 = 6.0 #width 2

eq1 = (1/(4*f1))*(rangeX**2)
eq2 = (1/(4*f2))*(rangeX**2)
plt.plot(rangeX, eq1,'r', linewidth=2.0, label='f=2')
plt.plot(rangeX, eq2,'b', linewidth=6.0, label='f=6')
plt.ylabel('y')
plt.xlabel('x')
plt.title("Parabola plots with varying focal lengths")
plt.legend(loc='lower left')
plt.show()

# PLOT 2 
rangeX2 = np.linspace(-4.0, 4.0, 25)

eq1 = (2*rangeX2**3)+(3*rangeX2**2)-(11*rangeX2)-6

plt.plot(rangeX2, eq1,'y*', linewidth=2.0, markeredgecolor='black')
plt.ylabel('y values')
plt.xlabel('x values')
plt.title("Plot of cubic polynomial")
plt.show()

# PLOT 3 
t1 = np.arange(-(2*math.pi), 2*math.pi, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, np.cos(t1), 'r', label = 'cos(x)')
plt.yticks(np.arange(-1, 2))
plt.grid(True)
plt.ylabel('y=cos(x)')
plt.title("Plot of cos(x) and sin(x)")
plt.legend(loc='lower right')


plt.subplot(212)
plt.plot(t1, np.sin(t1), 'gray',  label = 'sin(x)')
plt.yticks(np.arange(-1, 2))
plt.legend(loc='upper right')
plt.grid(True)
plt.ylabel('y=sin(x)')
plt.xlabel('x')
plt.show()