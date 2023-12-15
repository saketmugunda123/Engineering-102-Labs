# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Prayag Peram
#               Saket Mugunda
#               Aarjav Vani 
#               Sangkarshan Singh
# Section:      217
# Assignment:   4.14
# Date:         09/12/2023
#

#



def equation(A, B, C):
    equation = ""
    if A==0:
        equation+=""
    if A==1:
        equation += "x^2"
    elif A< -1:
        equation += "- "
    if A != 1 and A!=0 and A!=-1:
        equation += str(abs(A))
        equation += "x^2"
    elif A == -1:
        equation += "- "
        equation += "x^2"
    
    
    if B==0:
        equation+=""
    if B > 0 and A!=0:
        equation += " + "
    elif B < 0:
        equation += " - "
    
    if abs(B) != 1 and B != 0:
        equation += str(abs(B))
    
    if B != 0:
        equation += "x"
    
    
    if C > 0:
        equation += " + "
    elif C < 0:
        equation += " - "
    
    if C != 0:
        equation += str(abs(C))

    return equation

# user input
A = int(input("Please enter the coefficient A: "))
B = int(input("Please enter the coefficient B: "))
C = int(input("Please enter the coefficient C: "))

# equation
ans = equation(A, B, C)

# Printing the result
print(f"The quadratic equation is {ans} = 0")