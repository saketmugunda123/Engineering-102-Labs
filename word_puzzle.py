# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Saket Mugunda
# NAME OF TEAM MEMBER 2 Aarjav Vani
# NAME OF TEAM MEMBER 3 Prayag Peram
# NAME OF TEAM MEMBER 4 Sankarshan Singh
# Section: 217
# Assignment: 9.15
# Date: 10/23/2023
#ASCII ART NUMBERS
def get_valid_letters(string):
  outcome = []
  for i in range(len(string)):
    if (string[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
      if (not (string[i] in outcome)):
        outcome.append(string[i])
  outcomeString = ''.join(outcome)

  return outcomeString


def is_valid_guess(uniqueString, guess):
  if((len(guess) != 10) or (len(uniqueString) != 10)):
    return False
  if get_valid_letters(guess) != guess:
    return False

  #represents the list of unique letters
  uniList = []
  for i in guess:
    if ((i in uniqueString) and (i not in uniList)):
      uniList.append(i)
    else:
      return False
  return True


def check_user_guess(dividend, quotient, divisor, remainder):
  return dividend == quotient * divisor + remainder


def make_number(change, guess):
  number = ""
  for j in range(len(change)):
    for i in range(len(guess)):
      if (guess[i] == change[j]):
        number += (str(i))
  #first check if empty string before converting
  if (number != ""):
    number = int(number)
    return number
  else:
    return 0


def make_numbers(word, guess):
  puzzleList = word.split(",")
  puzzleList[1:2] = puzzleList[1].split("|")
  number1 = make_number(puzzleList[2], guess)  #dividend
  number2 = make_number(puzzleList[0], guess)  #quotient
  number3 = make_number(puzzleList[1], guess)  #divisor
  number4 = make_number(puzzleList[(len(puzzleList)) - 1], guess)  #remainder
  return number1, number2, number3, number4


def print_puzzle(puzzle):
  ''' Print puzzle as a long division problem. '''
  puzzle = puzzle.split(',')
  for i in range(len(puzzle)):
    if i == 1:
      print(f'{len(puzzle[i].split("|")[1]) * "_": >16}')
    print(f'{puzzle[i]: >16}')
    if i > 1 and i % 2 == 0:
      print(f"{'-'*len(puzzle[i]): >16}")


def main():
  puzzle = input("Enter a word arithmetic puzzle: ")
  print()
  print_puzzle(puzzle)
  print()
  guess = input("Enter your guess, for example ABCDEFGHIJ: ")

  valid = get_valid_letters(puzzle)
  temp = (is_valid_guess(valid, guess))
  
  if(temp):
    tuple = make_numbers(puzzle, guess)
    check = check_user_guess(tuple[0], tuple[1], tuple[2], tuple[3])
    if(check):
      print("Good job!")
    else:
      print("Try again!")
  else:
    print("Your guess should contain exactly 10 unique letters used in the puzzle.")
    
  

if __name__ == '__main__':
  main()