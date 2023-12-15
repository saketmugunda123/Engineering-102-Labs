# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Saket Mugunda
# Section: 217
# Assignment: 2.10
# Date: 08/22/2023

#Assigning Variables
x1,y1,z1 = 8,6,7
x2,y2,z2 = -5,30,9
t1=12
t2 =85
t = 30.0
x_slope = (x2 - x1)/(t2-t1)
y_slope = (y2-y1)/(t2-t1)
z_slope = (z2-z1)/(t2-t1)
i =1
j = 0
#Running through each value of t
t = 30.0
x = x_slope*(t-t1)+x1
y = y_slope*(t-t1)+y1
z = z_slope*(t-t1)+z1
print("At time",t, "seconds:")
print("x"+str(1),"=", x,"m")
print("y"+str(1),"=", y,"m")
print("z"+str(1),"=", z, "m")
print("-----------------------")

t = 37.5
x = x_slope*(t-t1)+x1
y = y_slope*(t-t1)+y1
z = z_slope*(t-t1)+z1
print("At time",t, "seconds:")
print("x"+str(2),"=", x,"m")
print("y"+str(2),"=", y,"m")
print("z"+str(2),"=", z, "m")
print("-----------------------")

t = 45.0
x = x_slope*(t-t1)+x1
y = y_slope*(t-t1)+y1
z = z_slope*(t-t1)+z1
print("At time",t, "seconds:")
print("x"+str(3),"=", x,"m")
print("y"+str(3),"=", y,"m")
print("z"+str(3),"=", z, "m")
print("-----------------------")


t = 52.5
x = x_slope*(t-t1)+x1
y = y_slope*(t-t1)+y1
z = z_slope*(t-t1)+z1
print("At time",t, "seconds:")
print("x"+str(4),"=", x,"m")
print("y"+str(4),"=", y,"m")
print("z"+str(4),"=", z, "m")
print("-----------------------")

t = 60.0
x = x_slope*(t-t1)+x1
y = y_slope*(t-t1)+y1
z = z_slope*(t-t1)+z1
print("At time",t, "seconds:")
print("x"+str(5),"=", x,"m")
print("y"+str(5),"=", y,"m")
print("z"+str(5),"=", z, "m")







