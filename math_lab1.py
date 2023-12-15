import math
from math import *
from sympy import *
from sympy.plotting import (plot,plot_parametric)
from sympy.vector import CoordSys3D
C = CoordSys3D('C', vector_names=('i','j','k'))
import scipy.optimize as optimize

#Question 1a
x = (4*(log(1.29) + ln(11.1)))/(2027-(12**3))
print(x)

#Question 1b
answer1b= (sin((11*pi)/(12))*cos((5*pi)/(12)))+(cos((11*pi)/(12))*sin((5*pi)/(12)))
print(answer1b)
print(answer1b.evalf())

#Question 2a
x= pi/3
sinanswer = (sin(x))**2
cosanswer = 0.5*(1-(cos(2*(x))))
print(sinanswer)
print(cosanswer)

#Question 2b
x=2.13
sinanswer = (sin(x))**2
cosanswer = 0.5*(1-(cos(2*(x))))
print(sinanswer)
print(cosanswer)


#Question 3a
vectorA = [2,3]
vectorB = [-1,5]
answer3a = [vectorA[0]+vectorB[0], vectorA[1]+vectorB[1]]
print(answer3a)
answer3b = [vectorA[0]-vectorB[0], vectorA[1]-vectorB[1]]
print(answer3b)
answer3c = [3*vectorA[0]- 5*vectorB[0], 3*vectorA[1]- 5*vectorB[1]]
print(answer3c)

#Question 3b
angleA = math.atan(3/2)
print(angleA)

#Question 3c
vectorC = answer3c
magnitude = sqrt((11**2)+(16**2))
vectorC = [vectorC[0]/magnitude,vectorC[1]/magnitude]
print(vectorC)

#Question 4a
vector_force = [5,9]
magnitude_force = sqrt((vector_force[0])**2 +(vector_force[1])**2)
print(magnitude_force)

#Question 4b
point1 = [3,4]
point2 = [5,10]
vector_displacement = [point2[0]-point1[0], point2[1]-point1[1]]
print(vector_displacement)

#Question 4c
magnitude_displacement = sqrt((vector_displacement[0])**2 + (vector_displacement[1])**2)
print(magnitude_displacement)

#Question 4d work = dot product
work = (vector_displacement[0]*vector_force[0])+(vector_displacement[1]*vector_force[1])
print(work)
                                                 
#Question 4e 
cosine_theta = (work)/(magnitude_force*magnitude_displacement)
print(cosine_theta)

#Question 4f
theta = math.acos(cosine_theta)
print(theta)






