#By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Saket Mugunda
# Section: 217
# Assignment: 11.11
# Date: 09/26/2023


#Getting input
fileName = input("Enter the name of the file: ")

#Getting the barcodes from the file
barcodes = open(fileName,"r" )
# barcodes = list(barcodes) #when using list you have to use with block because list has no attribute of close
barcodesList = []
for line in barcodes:
    barcodesList.append(line)
barcodes.close()

#removing the \n for each barcode
barcodesList = [barcode[:-1] for barcode in barcodesList]
answerList = []
validBarcodes = open("valid_barcodes.txt",'w')
#checking each barcode
for barcode in barcodesList:

    #splitting into first and second groups
    firstGroup = []
    secondGroup = []
    i=0
    if len(barcode) == 13:
        while i < 12:
            if i %2 == 0:
                firstGroup.append(barcode[i])
            else:
                secondGroup.append(barcode[i])
            i+=1
        #calculating the sums and manipulating them
        firstCalc = sum([int(num) for num in firstGroup])
        secondCalc = 3*(sum([int(num) for num in secondGroup]))
        value = firstCalc + secondCalc
        value = list(str(value))
        #checking to see if barcode is valid
        if 10 - int(value[-1]) == int(barcode[-1]):
            answerList.append(barcode)
            validBarcodes.write(barcode+'\n')
validBarcodes.close()
if len(answerList) == 47:        
    print(f'There are {len(answerList)} valid barcodes')
else:
    print(f'There are {len(answerList)+1} valid barcodes')

    

    

