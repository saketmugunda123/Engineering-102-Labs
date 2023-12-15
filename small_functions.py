# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Saket Mugunda
# Section: 217
# Assignment: 9.16
# Date: 10/30/2023

#gathering inputs
from math import *

#Part A
def parta (rSphere,rHole):
    hCylinder = sqrt(rSphere**2 - rHole**2)*2
    volumeSphere = (4/3)*pi*(rSphere**3)
    volumeHole = pi*(rHole**2)*hCylinder
    heightcap = ((2*rSphere) - hCylinder)/2
    volcap = (pi/6)*heightcap*((3*rHole**2) + (heightcap**2))
    #equation
    volumeBead = volumeSphere - volumeHole - (volcap*2)
    return volumeBead



#Part B
def partb(number):
    list = []
    for i in range(1, number, 2):
        list.append(i)
        if sum(list) > number:
            while sum(list) > number:
                list.pop(0)
        
        if sum(list) == number:
            return list
    return False

#Part C
def partc(character, name, company, email):
    info = [character, name, company, email]
    longestString = info[0]
    for char in info:
        if len(char) >= len(longestString):
            longestString = char       
    card = character*(len(longestString) + 6)           
    for char in info[1:]:
        spaces = len(longestString) - len(char) + 2
        List = []      
        if spaces % 2 == 1:
            List.append(ceil(spaces/2))
            List.append(ceil(spaces/2 + 1))
        else:
            List.extend([spaces/2 + 1, spaces/2 + 1])      
        card += '\n' + (character + ' '*(int(List[0])) + char + ' '*(int(List[1])) + character)       
    card += '\n' + character*(len(longestString) + 6)    
    return card

#Part D
def partd(numbers):
    length = len(numbers)
    numbers = sorted(numbers)
    if len(numbers) % 2 == 1:
        median = numbers[ceil(len(numbers)/2) - 1]
    else:
        median = (numbers[ceil(len(numbers)/2) - 1] + numbers[ceil(len(numbers)/2)])/2
    return min(numbers),int(median),max(numbers)

#Part E
def parte(time,distance):
    i = 0 
    velocity = []
    while i < len(time)-1:
        temp = (distance[i+1]-distance[i])/(time[i+1]-time[i])
        velocity.append(temp)
        i+=1
    return velocity

#Part F
def partf(numbers):
    i=0
    complement = {}
    target = 2027
    for num in numbers:
        if target - num in complement:
            return (target-num)*num
        else:
            complement[num] = i
            i+=1
    return False

#Part G
def partg(x, tolerance):
    tot, eval, n = 0, 0, 1  
    while True:
        eval = (2/(2*n-1))*(x**(2*n-1))
        
        if abs(eval) < tolerance:
            break
        else:
            tot += eval
            n += 1
    return tot

