# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Saket Mugunda
# Section: 217
# Assignment: 6.13
# Date: 09/26/2023

#Getting inputs for integers
int1 = int(input("Enter an integer: "))
int2 = int(input("Enter another integer: "))

#For loop for each integer within the range 
for i in range (1,101):
    #Executes this set of if statements for each number in range
    if  i % int1 ==0 and i % int2 ==0:
        print("Howdy Whoop")
    elif i % int2 ==0:
        print("Whoop")
    elif i % int1 == 0:
        print("Howdy")
    else:
        print(i)