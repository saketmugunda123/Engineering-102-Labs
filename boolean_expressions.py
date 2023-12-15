# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Saket Mugunda
# NAME OF TEAM MEMBER 2 Aarjav Vani
# NAME OF TEAM MEMBER 3 Prayag Peram
# NAME OF TEAM MEMBER 4 Sankarshan Singh
# Section: 217
# Assignment: 4.15
# Date: 09/17/2023

############ Part A ############

#Getting input values
a = input("Enter True or False for a: ")
b = input("Enter True or False for b: ")
c = input("Enter True or False for c: ")
odd = 0

if a== 'True' or a == 't' or a== 'T':
    a = True
    odd+=1
elif a =='False' or a =='f' or a== 'F':
    a = False

if b== 'True' or b == 't' or b== 'T':
    b = True
    odd+=1
elif b =='False' or b =='f' or b== 'F':
    b = False

if c=='True' or c== 't' or  c=='T':
    c = True
    odd+=1
elif c =='False' or c=='f' or c=='F':
    c = False

############ Part B ############

d = a and b and c
y = a or b or c
print("a and b and c:", d)
print("a or b or c:", y)

############ Part C ############
#Using not operater to get Xor
xor = (not(a==b))
print("XOR:",xor)

oddNumber = (odd == 1 or odd ==3)
print("Odd number:",oddNumber)

############ Part D ############
complex1 = (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)

complex2 = (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))

#simplified versions after boolean simplification
simple1 = not a
simple2 = a

print("Complex 1:", complex1)
print("Complex 2:", complex2)
print("Simple 1:", simple1)
print("Simple 2:", simple2)




    







