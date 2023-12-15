#By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Saket Mugunda
# Section: 217
# Assignment: 7.27
# Date: 10/05/2023

#Getting number inputs
textNumbers = input('Enter numbers: ')
textNumbers = textNumbers.split()


#Turning the str of numbers into a list of integers
numbers = []
for number in textNumbers:
    numbers.append(int(number))

#These are the indexes that are being sliced
a = 0 
b = 1
indexLength = len(numbers)-1

#Slicing the list to see if each side is equal to one another
while b <= len(numbers)-1:
    leftSum = 0 
    rightSum = 0
    leftList = numbers[a:b]
    for num in leftList:
        leftSum += num
    rightList = numbers[b:]
    for num in rightList:
        rightSum += num
    if leftSum == rightSum:
        break
    b+=1

#Checks to see if there is a solution
if leftSum == rightSum:
    print(f'Left: {leftList}')
    print(f'Right: {rightList}')
    print(f'Both sum to {leftSum}')
else:
    print("Cannot split evenly")
