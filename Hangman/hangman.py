import random
from word_list import words
import string

def get_valid_word(words):
    word = random.choice(words)
    print(word)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)


