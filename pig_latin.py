#By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Saket Mugunda
# Section: 217
# Assignment: 6.15
# Date: 09/26/2023

#Getting input from user
text = input("Enter word(s) to convert to Pig Latin:")
print(f'In Pig Latin, "{text}" is:',end=' ')

#Turning the sentence into a list of words
words = text.split()

#assigns what letters to look out for (vowels)
vowels = 'aeiouy'

#What to add whether the word starts with a vowel or constanant
vowelAdd = 'yay'
constanantAdd ='ay'

#iterating through each word in the list of words
for word in words: 
    temp =''
    count = 0

    #iterating through each letter in the word
    for letter in word:
        if letter not in vowels:
            temp+=letter
            count +=1
        else:
            break

    if count > 0: 
        #starts the new word at the index value count
        word = word[count:]
        #adding the changes to text
        word = word + temp + constanantAdd 
        print(word,end=' ')
    else:
        word += vowelAdd
        print(word,end=' ')

