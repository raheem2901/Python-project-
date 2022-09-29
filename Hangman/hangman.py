import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #this fuction basically chooses something from the list
    while '-' in words or ' ' in words:
        word = random.choice(words)
        
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # variable that saves letters in the word
    alphabet = set(string.ascii_uppercase) # just upper case char in english
    used_letters = set() # what the user has guessed

    lives = 6

    #getting user input
    while len(word_letters) > 0 and lives > 0 :
             #letters used
        print(f'You have,{lives} lives left and You have used these letters ', ' '.join(used_letters) )

        #What current word is (ie. W _ R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', " ".join(word_list))


        user_letter = input('Guess a letter:').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print("Letter is not in the word")
    
        elif user_letter in used_letters:
            print("You have already used this letter,Please try again")
    
        else:
            print("Invalid input, Please try again")

    #gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(f'You died,Sorry. The word was {word}')
    else:
        print(f'Yayy!, You have guessed the word, {word} ,correctly!!')




hangman()