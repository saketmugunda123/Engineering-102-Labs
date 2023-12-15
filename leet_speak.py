# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Saket Mugunda
# Section: 217
# Assignment: 7.26
# Date: 10/4/2023

#Creating a dictionary for the letter changes
leetSpeak = {'a':'4',
             'e':'3', 
             'o':'0',
             's':'5',
             't':'7'}

statement = input("Enter some text: ")
i=0
#Creating a variable that stores changes
newStatement = ''
#iterate through each character of statement
for letter in statement:
    #check to see if letter is in dictionary
    if letter in leetSpeak:
        newStatement += leetSpeak[letter]
    else:
        newStatement+=letter

#print outputs
print(f'In leet speak,"{statement}" is:')
print(newStatement)
