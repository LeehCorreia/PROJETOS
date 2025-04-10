import random
from word_list import words
import string

def get_valid_word(words):
    word = random.choice(words)
    # print(word)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0:
        print('You have used these letters: ',' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]

        print('Current word: ', ' '.join(word_list))
        print()
        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print('You hava already used that character. Please guess again.')
        
        else:
            print('Invalid character. Please try a valid character.')
        if len(word_letters) == 0:
            print(word)

    
hangman()
