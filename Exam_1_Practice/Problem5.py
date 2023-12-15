condition = True
count = 0
ageList = []
while condition: 
    if count == 0:
        age = int(input('Enter an age: '))
    else:
        age = int(input('Enter another age: '))
    if age < 0:
        condition = False
    ageList.append(age)
    count +=1 

comparemax = max(ageList)
comparemin = min(ageList)

strings= 'Number of people  Minimum age  Maximum age'
string2 = f'{count} {comparemin} {comparemax}'
print(strings)
print(string2)
