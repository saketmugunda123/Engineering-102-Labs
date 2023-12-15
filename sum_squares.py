# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Aarjav Vani, Sankarshan Singh, Prayag Peram, Saket Mugunda
# Section:      217
# Assignment:   10.13 Sum squares
# Date:         5 November 2023

from time import time

def list_nums(n):

    max_num = int(n**0.5) + 1
    answerList = set()
    for a in range(0, max_num):
        for b in range(a, max_num):
            for c in range(max_num)[::-1]:
                for d in range(1,max_num):
                    if n - a**2 - b**2 - c**2 == d**2:
                        return [a,b,c,d]
    return [a,b,c,d]
def count_sets(n):
    '''Return the number of unique sets of values whose squares add up to n'''
    def find_squares(n):
        squares = []
        
        for i in range(0, int(n**0.5) + 1):
            square = i**2
            squares.append(square)
            
        return squares
    
    def generate_coms(squares, target, com, count):
        if len(com) == 4:
            if sum(com) == target:
                return 1
            else:
                return 0
        if len(com) > 4 or sum(com) > target:
            return 0
        
        total_count = 0
        
        for i, square in enumerate(squares):
            total_count += generate_coms(squares[i:], target, com + [square], count)
            
        return total_count
    
    squares = find_squares(n)
    return generate_coms(squares, n, [], 0)

# how to measure how long your function takes to run:
t3 = time()
print(list_nums(844474))
t4 = time()
print(count_sets(25))
print(f"This took {(t4-t3):.5f} seconds") # print result



