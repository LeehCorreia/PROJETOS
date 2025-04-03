import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        print(guess)
        if guess > random_number:
            print(f'{guess} is too high!')
        elif guess < random_number:
            print(f'{guess} is too low!')
        
    print(f'{random_number} is de correct number! Congratulations!! ')
    print('End of game!')
        
guess(10)

