#By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Saket Mugunda
# Section: 217
# Assignment: 6.15
# Date: 09/26/2023

num = float(input("Enter a positive integer: "))
if num ==1:
    print("The Juggler sequence starting at 1 is: 1")
    print('It took 0 iterations to reach 1')
#print("The Juggler sequence starting at",int(num),'is:',int(num),',',end='')
string = f'The Juggler sequence starting at {int(num)} is: {int(num)},'
iterations = 0
#When num reaches 1 it exits the loop
if num > 1:
    while num > 1:
        if num%2 ==1:
            num = int(num**1.5)
            #adding to iterations after each activation of the if statement
            iterations +=1
            string+= f' {num},'
        else:
            num = int(num**0.5)
            iterations+=1
            string+= f' {num},'
    #printing output
    string = string[:-1]
    print(string)
    print(f'It took {iterations} iterations to reach 1')


