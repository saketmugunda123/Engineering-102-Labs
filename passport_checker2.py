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
# Date:         11/13/23

inputFile = input("Enter the name of the file: ")
mainFile = open(inputFile,"r")
validPassports = open("valid_passports2.txt", "w")
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
            if int(i[4:]) >1919 and int(i[4:]) < 2008:
                cbyr = True
        if("iyr:" in i):
            if int(i[4:]) >2012 and int(i[4:]) < 2024:
                ciyr = True
        if("eyr:" in i):
            if int(i[4:]) >2022 and int(i[4:]) < 2034:
                ceyr = True
        if("hgt:" in i):
            if i[-2:] == "cm":
                if int(i[4:-2]) >149 and int(i[4:-2]) < 194:
                    chgt = True
            if i[-2:] == "in":
                if int(i[4:-2]) >58 and int(i[4:-2]) < 77:
                    chgt = True
        if("hcl:" in i):
            if len(i) == 11:
                chcl = True
            for o in range(5,len(i)):
                if i[o] not in ("abcdef0123456789"):
                    chcl = False
                if i[4] != "#":
                    chcl = False
        if("pid:" in i):
            if len(i) == 13:
                cpid = True
            g = int(i[4:])
        if("cid:" in i):
            ccid = True
            if len(i) < 7:
                ccid = False
            for j in i[4:-3]:
                if j != 0:
                    ccid = False
            if i[-3] == "0" and i[-4] == ":":
                ccid = False
    if(cbyr and ciyr and ceyr and chgt and chcl and cpid and ccid and (len(data)>6)):
        validPassports.write(bigstring+"\n")
        ct+=1
    data = []
print("There are", ct, "valid passports")
mainFile.close()
validPassports.close()        


