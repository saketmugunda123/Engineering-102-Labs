#By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Saket Mugunda
# Section: 217
# Assignment: 6.15
# Date: 09/26/2023
#Gets input from user
num = int(input("Enter a value for n: "))\
#Set leftnum equal to the summation of n from 1 to (n-1)
leftnum = int((((num**2)-num)/2))
rightnum = num+1
r=0
n=1
total=0
#The while condition is the summation formula for 1 to n-1
while leftnum > total:
    rightnum =num+n
    total+=rightnum
    #increment r every iteration of the while loop
    r+=1
    n+=1
if leftnum == total:
    print(f'{num} is a balancing number with r={r}')
else:
    print(f'{num} is not a balancing number')

