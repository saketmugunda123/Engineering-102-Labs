# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Saket Mugunda
# NAME OF TEAM MEMBER 2 Aarjav Vani
# NAME OF TEAM MEMBER 3 Prayag Peram
# NAME OF TEAM MEMBER 4 Sankarshan Singh
# Section: 217
# Assignment: 8.10
# Date: 10/23/2023
#ASCII ART NUMBERS
ascii0 = [["0","0","0"], ["0"," ","0"],["0"," ","0"],["0"," ","0"],["0","0","0"]]
ascii1 = [[" ","1"," "], ["1","1"," "],[" ","1"," "],[" ","1"," "],["1","1","1"]]
ascii2 = [["2","2","2"], [" "," ","2"],["2","2","2"],["2"," "," "],["2","2","2"]]
ascii3 = [["3","3","3"], [" "," ","3"],["3","3","3"],[" "," ","3"],["3","3","3"]]
ascii4 = [["4"," ","4"], ["4"," ","4"],["4","4","4"],[" "," ","4"],[" "," ","4"]]
ascii5 = [["5","5","5"], ["5"," "," "],["5","5","5"],[" "," ","5"],["5","5","5"]]
ascii6 = [["6","6","6"], ["6"," "," "],["6","6","6"],["6"," ","6"],["6","6","6"]]
ascii7 = [["7","7","7 "], [" "," ","7 "],[" "," ","7 "],[" "," ","7 "],[" "," ","7 "]]
ascii8 = [["8","8","8"], ["8"," ","8"],["8","8","8"],["8"," ","8"],["8","8","8"]]
ascii9 = [["9","9","9"], ["9"," ","9"],["9","9","9"],[" "," ","9"],["9","9","9"]]
#letters
asciiA = [[" ","A"," "], ["A"," ","A"],["A","A","A"],["A"," ","A"],["A"," ","A"]]
asciiP = [["P","P","P"], ["P"," ","P"],["P","P","P"],["P"," "," "],["P"," "," "]]
asciiM = [["M"," "," "," ","M"], ["M","M"," ","M","M"],["M"," ","M"," ","M"],["M"," "," "," ","M"],["M"," "," "," ","M"]]

allowedChar = "abcdeghkmnopqrsuvwxyz@$&*=" #allowed char list
def printLetter(list):
    #prints every element in the list row by row
    for row in list:
        for col in row:
            print(col, end = "")
        print("")
       
def listAppendDoubleHours(list1,list2,list3,list4):
    returnList = list1
    returnList[0].append(" ")
    returnList[1].append(" ")
    returnList[2].append(" ")
    returnList[3].append(" ")
    returnList[4].append(" ")
    for i in range(len(list1)): #appends list2 (hd2) to returnList
        returnList[i].extend(list2[i])
    #append colons
    returnList[0].append("   ")
    returnList[1].append(" : ")
    returnList[2].append("   ")
    returnList[3].append(" : ")
    returnList[4].append("   ")
    for i in range(len(list1)): #append minutes (md1)
        returnList[i].extend(list3[i])
    returnList[0].append(" ")
    returnList[1].append(" ")
    returnList[2].append(" ")
    returnList[3].append(" ")
    returnList[4].append(" ")
    for i in range(len(list1)): #append minutes (md2)
        returnList[i].extend(list4[i])
    return returnList

def listAppendSingleHours(list1,list2,list3):
    returnList = list1
    returnList[0].append("   ")
    returnList[1].append(" : ")
    returnList[2].append("   ")
    returnList[3].append(" : ")
    returnList[4].append("   ")
    for i in range(len(list1)):
        returnList[i].extend(list2[i])
    returnList[0].append(" ")
    returnList[1].append(" ")
    returnList[2].append(" ")
    returnList[3].append(" ")
    returnList[4].append(" ")
    for i in range(len(list1)):
        returnList[i].extend(list3[i])
    returnList[0].append(" ")
    returnList[1].append(" ")
    returnList[2].append(" ") # spaces for am/pm
    returnList[3].append(" ")
    returnList[4].append(" ")  
    return returnList

def isCharAllowed(char):
    if char in allowedChar: #checking if char is valid
        return True
    else:
        return False
def appendAMPM(list1,list2,list3):
    list1[0].append("")
    list1[1].append("")
    list1[2].append("") # spaces for am/pm
    list1[3].append("")
    list1[4].append("")#append am/pm
    for i in range(len(list1)):
        list1[i].extend(list2[i])
    list1[0].append(" ")
    list1[1].append(" ")
    list1[2].append(" ")
    list1[3].append(" ")
    list1[4].append(" ")
    for i in range(len(list1)):
        list1[i].extend(list3[i])
    return list1
           
def replaceElement(char,list1): #replace element with prefered character
    if isCharAllowed(char) == True and char != "":  
        for i in range (len(list1)):
            for j in range(len(list1[i])):
                if list1[i][j] != " ":
                    list1[i][j] = char
    elif char == "":
        list1 = list1
    return list1
   
 #MAIN CODE
time = input("Enter the time: ")
clockType = input("Choose the clock type (12 or 24): ")
prefChar = input("Enter your preferred character: ")

while isCharAllowed(prefChar) == False:
    prefChar = input("Character not permitted! Try again: ")
print()

asciiDict = {"0":ascii0, "1":ascii1, "2":ascii2, "3":ascii3, "4":ascii4, "5":ascii5, "6":ascii6, "7":ascii7, "8":ascii8, "9":ascii9, 'A':asciiA, 'P':asciiP, 'M':asciiM}
hours,minutes = time.split(":")
listA = []
if int(hours) == 0:
    hours = int(hours)
    hours = 12
    hours = str(hours)
md1 = minutes[0]
md2 = minutes[1]
if clockType == "12":
    if int(hours) > 12:
        hours = int(hours)- 12
        hours = str(hours)
        if len(hours) == 1:
            hd = hours[0]
            listA = listAppendSingleHours(replaceElement(prefChar,asciiDict[hd]),replaceElement(prefChar,asciiDict[md1]),replaceElement(prefChar,asciiDict[md2]))
            listA = appendAMPM(listA,asciiP,asciiM)
            printLetter(listA)

        else:
            hd1 = hours[0]
            hd2 = hours[1]
            listA = listAppendDoubleHours(replaceElement(prefChar,asciiDict[hd1]),replaceElement(prefChar,asciiDict[hd2]),replaceElement(prefChar,asciiDict[md1]),replaceElement(prefChar,asciiDict[md2]))
            listA = appendAMPM(listA,asciiP,asciiM)
            printLetter(listA)

    elif int(hours) <= 12.:
        if len(hours) == 1:
            hd = hours[0]
            listA = listAppendSingleHours(replaceElement(prefChar,asciiDict[hd]),replaceElement(prefChar,asciiDict[md1]),replaceElement(prefChar,asciiDict[md2]))
            listA = appendAMPM(listA,asciiA,asciiM)
            printLetter(listA)

        else:
            hd1 = hours[0]
            hd2 = hours[1]
            listA = listAppendDoubleHours(replaceElement(prefChar,asciiDict[hd1]),replaceElement(prefChar,asciiDict[hd2]),replaceElement(prefChar,asciiDict[md1]),replaceElement(prefChar,asciiDict[md2]))
            listA = appendAMPM(listA,asciiA,asciiM)
            printLetter(listA)

elif clockType == "24":
    if len(hours) == 1:
        hd = hours[0]
        listA = listAppendSingleHours(replaceElement(prefChar,asciiDict[hd]),replaceElement(prefChar,asciiDict[md1]),replaceElement(prefChar,asciiDict[md2]))
        printLetter(listA)

    else:
        hd1 = hours[0]
        hd2 = hours[1]
        listA = listAppendDoubleHours(replaceElement(prefChar,asciiDict[hd1]),replaceElement(prefChar,asciiDict[hd2]),replaceElement(prefChar,asciiDict[md1]),replaceElement(prefChar,asciiDict[md2]))
        printLetter(listA)