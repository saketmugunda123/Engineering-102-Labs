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