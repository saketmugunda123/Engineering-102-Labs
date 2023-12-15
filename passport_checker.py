# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Aarjav Vani
# Name:         Saket Mugunda
# name:         Prayag Peram
# Name:         Sankarshan Singh
# Section:      217
# Assignment:   Module 11
# Date:         11/12/23

inputFile = input("Enter the name of the file: ")
mainFile = open(inputFile,"r")
validPassports = open("valid_passports.txt", "w")
ct = 0
data = []
bigstring = ""
o = 0
for line in mainFile:
    cbyr = False
    ciyr = False
    ceyr = False
    chgt = False
    chcl = False
    cpid = False
    ccid = False
    if line[0] not in ("abcdefghijklmonopqrstuvwxyz"):
        bigstring = ""
    else:
        bigstring += (line)
    data = bigstring
    data = data.split()
    
    for i in data:
        #print(i)
        if("byr:" in i):
            cbyr = True
        if("iyr:" in i):
            ciyr = True
        if("eyr:" in i):
            ceyr = True
        if("hgt:" in i):
            chgt = True
        if("hcl:" in i):
            chcl = True
        if("pid:" in i):
            cpid = True
        if("cid:" in i):
            ccid = True
    if(cbyr and ciyr and ceyr and chgt and chcl and cpid and ccid and (len(data)>6)):
        validPassports.write(bigstring+"\n")
        ct+=1
    data = []
print("There are", ct, "valid passports")
mainFile.close()
validPassports.close()      


