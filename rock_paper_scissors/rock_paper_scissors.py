import random

def game():
    player = input("'r' for rock, 'p' for paper, 's' for scissors: ").lower()
    computer = random.choice(['r', 'p', 's'])
    print(computer)

    if player == computer:
        return 'It\'s a tie!'
    
    if is_win(player, computer):
        return 'Player win!'
    
    return 'Computer win!'

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(game())