names = ['Saket Mugunda F      25 rushing touchdowns','Karthik Gilari F     30 rushing touchdowns',]
print(names[0][0:21])
megaList = []
temp = ''
for person in names:
    tempList = []
    count = 0
    tempList.append(person[0:21].strip())
    tempList.append(person[21:].strip())
    megaList.append(tempList)
print(megaList)

user = input('Last Name: ')
print(user)
condition = True
i=0
while condition:
    if user in megaList[i][0]:
        stat = megaList[i][1]
        condition = False
    i+=1

for i in range(len(megaList)):
    if stat in megaList[i][1]:



    