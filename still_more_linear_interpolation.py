# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Saket Mugunda
# Section: 217
# Assignment: 3.16
# Date: 09/06/2023

#gathering inputs
t1= float(input("Enter time 1: "))
x1 = float(input("Enter the x position of the object at time 1: "))
y1 = float(input("Enter the y position of the object at time 1: "))
z1 = float(input("Enter the z position of the object at time 1: "))
t2 = float(input("Enter time 2: "))
x2 = float(input("Enter the x position of the object at time 2: "))
y2 = float(input("Enter the y position of the object at time 2: "))
z2 = float(input("Enter the z position of the object at time 2: "))

#assigning different time variables
time1 = t1
time2 = t1 +((t2-t1)/4)
time3 = t1 +((t2-t1)/2)
time4 = t1 +((t2-t1)*3/4)
time5= t2

#function for x value
def linear_interpolation_x(time):
    x_answer = ((x2-x1)/(t2-t1))*(time-t1)+x1
    return x_answer

#function for y value
def linear_interpolation_y(time):
    y_answer = ((y2-y1)/(t2-t1))*(time-t1)+y1
    return y_answer

#function for z value
def linear_interpolation_z(time):
    z_answer = ((z2-z1)/(t2-t1))*(time-t1)+z1
    return z_answer

#calling all the functions and printing in a specific format
print(f'At time {time1:.2f} seconds the object is at ({linear_interpolation_x(time1):.3f}, {linear_interpolation_y(time1):.3f}, {linear_interpolation_z(time1):.3f})')
print(f'At time {time2:.2f} seconds the object is at ({linear_interpolation_x(time2):.3f}, {linear_interpolation_y(time2):.3f}, {linear_interpolation_z(time2):.3f})')
print(f'At time {time3:.2f} seconds the object is at ({linear_interpolation_x(time3):.3f}, {linear_interpolation_y(time3):.3f}, {linear_interpolation_z(time3):.3f})')
print(f'At time {time4:.2f} seconds the object is at ({linear_interpolation_x(time4):.3f}, {linear_interpolation_y(time4):.3f}, {linear_interpolation_z(time4):.3f})')
print(f'At time {time5:.2f} seconds the object is at ({linear_interpolation_x(time5):.3f}, {linear_interpolation_y(time5):.3f}, {linear_interpolation_z(time5):.3f})')