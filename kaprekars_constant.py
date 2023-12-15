#By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Saket Mugunda
# Section: 217
# Assignment: 7.28
# Date: 10/06/2023


#check to see if string has unique characters
falseValues = ['1111','2222','3333','4444','5555','6666','7777','8888','9999','0000']
string = input("Enter a four-digit integer: ")
condition = True
if string in falseValues:
    print(f'{string} > 0') 
    print(f"{string} reaches 0 via Kaprekar's routine in 1 iterations")
    condition = False

#adds leading 0s to non 4 digit numbers
if len(string) < 4:
    lessString = string[:]
    while len(lessString) < 4:
        lessString = '0' + lessString
    newString = lessString

#Sets stores string in newString for final print statement
newString = string[:]

#settings variables
value = 0
answer = (f'{string} > ')
count = 0

#iterates until the value is reached (6174)
while value != 6174 and condition:
    if len(string) < 4:
        while len(string) < 4:
            string = '0' + string


    #changes string to list and then to a list of integers
    list(string)
    digits = [int(character) for character in string]

    #creates two sorted numbers
    digits_reverse = digits[:]

    digits.sort()
    sort = digits

    digits_reverse.sort(reverse=True)
    rsort = digits_reverse

    #Turns into string for concatination and then back into integer
    stringSort = ''
    for num in sort:
        stringSort+=str(num)

    stringRsort = ''
    for num in rsort:
        stringRsort+=str(num)

    sortNumber = int(stringSort)
    rsortNumber = int(stringRsort)


    if rsortNumber > sortNumber:
        value = rsortNumber - sortNumber
    else:
        value = sortNumber - rsortNumber
    
    answer += (f'{value} > ')
    string = str(value)
    count+=1

#print outputs
if condition:
    print(answer[:-2])
    print(f"{newString} reaches 6174 via Kaprekar's routine in {count} iterations")