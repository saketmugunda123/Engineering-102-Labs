#By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Saket Mugunda
# Section: 217
# Assignment: 7.29
# Date: 10/06/2023
#check to see if string has unique characters
totalCount = 0
for i in range (1,9999):
    string = str(i)
    count = 0
    falseValues = ['1111','2222','3333','4444','5555','6666','7777','8888','9999','0000']


    #adds leading 0s to non 4 digit numbers
    if len(string) < 4:
        lessString = string[:]
        while len(lessString) < 4:
            lessString = '0' + lessString   

    #settings variables
    value = 0
    count = 0

    condition = True
    if string in falseValues:
        condition = False
        count = 1

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
        
        string = str(value)
        count+=1
    totalCount += count
print(f"Kaprekar's routine takes {totalCount} total iterations for all four-digit numbers")
