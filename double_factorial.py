#By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Saket Mugunda
# Section: 217
# Assignment: 6.14
# Date: 09/26/2023

#double factorial function
def doublefactorial(num):
    #sets newNum equal to num to store intial value
    if num ==0:
        return 1
    newNum = num   
    while num-2 > 0:
        newNum*=(num-2)
        #increments num by -2
        num-=2
    return newNum
