# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Saket Mugunda
# Section: 217
# Assignment: 4.18
# Date: 09/12/2023

#get an input for number of days
days = int(input("Please enter a positive value for day: " ))

#run conditonal to see how many gadgets should be printed based on number of days
if days >=0 and days <= 10:
    gadgets = 10*days
    print("The sum total number of gadgets produced on day", days ,"is", int(gadgets))
elif days>10 and days <=50:
    gadgets = ((days*(days+1)/2)) + 45
    print("The sum total number of gadgets produced on day", days ,"is", int(gadgets))
elif days > 50 and days < 101:
    gadgets = (50*(days-50)) + (1320)
    print("The sum total number of gadgets produced on day", days ,"is", int(gadgets))
elif days >= 101:
    gadgets = 3820
    print("The sum total number of gadgets produced on day", days ,"is", int(gadgets))
else:
    print("You entered an invalid number!")