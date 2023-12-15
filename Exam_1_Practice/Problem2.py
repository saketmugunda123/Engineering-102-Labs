secret = input("User 1 enter a word minimum of 6 letters: ")
condition = True
count = 0
while condition:
    if count == 0:
        letter = input('Guess a letter: ')
    else:
        letter = input('Guess another letter: ')

    if letter in secret:
        count += 1
    else:
        condition = False    
   
print(f'The secret word is: "{secret}". You took {count} guesses!')