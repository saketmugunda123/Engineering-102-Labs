# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Saket Mugunda
# Section: 217
# Assignment: 10.14
# Date: 11/06/2023

def from_roman(roman_numeral):
    symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    total = 0
    previous_value = 0

    for numeral in roman_numeral[::-1]:
        current_value = symbols[numeral]

        if current_value >= previous_value:
            total += current_value
        else:
            total -= current_value

        previous_value = current_value

    return total

def compare_roman_numerals(roman_numeral_1, roman_numeral_2):
    a = from_roman(roman_numeral_1)
    b = from_roman(roman_numeral_2)
    
    if a < b:
        return -1
    elif a == b:
        return 0
    else:
        return 1

def main():
    num1 = input("Enter the first Roman numeral: ")
    num2 = input("Enter the second Roman numeral: ")
    result = compare_roman_numerals(num1, num2)

    if result == -1:
        compare = 'smaller than'
    elif result == 0:
        compare = 'equal to'
    else:
        compare = 'larger than'
        
    print(f'{num1} is {compare} {num2}')

if __name__ == '__main__':
    main()
