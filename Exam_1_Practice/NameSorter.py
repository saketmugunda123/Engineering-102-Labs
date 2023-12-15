User1 = input('Name: ')
User2 = input('Name: ')
User3 = input('Name: ')
User4 = input('Name: ')
User5 = input('Name: ')

NameList = []
NameList.append(User1.split())
NameList.append(User2.split())
NameList.append(User3.split())
NameList.append(User4.split())
NameList.append(User5.split())
print(NameList)
i = 1
newName = []
for list in NameList:
    newName.append(list[i])
print(newName)



Sorted = sorted(newName)
print(Sorted)


