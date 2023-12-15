# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Saket Mugunda
# Section: 217
# Assignment: 10.15
# Date: 11/05/2023
#function for getting input
def get_input():
    print("What is your guess?",end=' ')
    while True:
        try:
            guess = int(input(""))
            return guess
        except:
            print("Bad input! Try again:")

def game():
    print("Guess the secret number! Hint: it's an integer between 1 and 100...")
    count = 0
    condition = True
    #runs through the game
    while condition:
        #gets the input from the get_input function
        guess = get_input()
        count +=1
        if guess > 27:
            print('Too high!')
        elif guess < 27:
            print('Too low!')
        else:
            condition = False
    #output answer
    print(f'You guessed it! It took you {count} guesses.')

if __name__ == "__main__":
    game()