import random

def guess(x):
    low = 1
    high = x
    number = int(input(f"Enter one number between 1 and {x}: "))
    random_number = random.randint(low, high)
    
    while random_number != number:
        print(f"Computer guessed {random_number}.")
        if random_number < number:
            low = random_number + 1
        elif random_number > number: 
            high = random_number -1
        random_number = random.randint(low, high)
        
    print(f'{random_number} is de correct number! Congratulations!! ')
    print('End of game!')
        
guess(5000)