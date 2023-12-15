num = int(input("Enter a value for n: "))
#Set leftnum equal to the summation of n from 1 to (n-1)
leftnum = int((num * (num + 1)) / 2)
rightnum = num
r = 1
#The while condition is the summation formula for 1 to n-1
while leftnum > rightnum:
    rightnum += (num + r)
    #increment r every iteration of the while loop
    r += 1
if leftnum == rightnum:
    print(f'{num} is a balancing number with r={r}')
else:
    print(f'{num} is not a balancing number')