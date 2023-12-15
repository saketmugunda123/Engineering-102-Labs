# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Saket Mugunda
# NAME OF TEAM MEMBER 2 Aarjav Vani
# NAME OF TEAM MEMBER 3 Prayag Peram
# NAME OF TEAM MEMBER 4 Sankarshan Singh
# Section: 217
# Assignment: 4.13
# Date: 09/17/2023

#Gathering inputs for both cost and pay to obtain change
pay = float(input("How much did you pay? "))
cost = float(input("How much did it cost? "))
change = (pay - cost)*100
print(f'You received ${change/100:.2f} in change. That is...')

#Running through each scneario of change to output least number of coins
# Check if the change is divisible by 25
if change >= 25:
    quarters = change // 25
    if quarters ==1:
        print(int(quarters),'quarter')
    else:
        print(int(quarters),'quarters')
    change %= 25

  # Check if the remaining change is divisible by 10
if change >= 10:
    dimes = change // 10
    if dimes == 1:
        print(int(dimes),'dime')
    else:
        print(int(dimes),'dimes')
    change %= 10

  # Check if the remaining change is divisible by 5
if change >= 5:
    nickels = change // 5
    if nickels == 1:
        print(int(nickels),'nickel')
    else:
        print(int(nickels),'nickels')
    change %= 5

  # The remaining change is pennies
if change > 0.1:   #0.1 accounts for the rounding issue   
    pennies = round(change,0)
    if pennies ==1:
        print(int(pennies),'penny')
    else:
        print(int(pennies),'pennies')