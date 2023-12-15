#By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Saket Mugunda
# Section: 217
# Assignment: 12.14
# Date: 11/20/2023

#importing the necessary modules
import numpy as np
import matplotlib.pyplot as plt

#setting the values of the original matrix and vector
original_matrix = np.array([[1.02,0.095], 
                            [-0.095,1.02]])

original_point = np.array([[0],
                           [1]])
print(original_point.shape)

points_list = []

#iterating through to get a list of points
for i in range (0,250):
    newPoint = np.dot(original_matrix,original_point)
    points_list.append(newPoint)
    original_point = newPoint

points_array = np.array(points_list)
print(points_list)

#Plotting those points on a scatter plot
plt.scatter(points_array[:, 0], points_array[:, 1], marker='o', label='Transformed Points')

plt.title('A Swirl of Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

plt.show()






