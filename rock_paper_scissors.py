import random

def play():
    user = input("What's your choice :'r' is for rock 's' for scissors 'p' for paper \n")
    s = computer = random.choice(['r', 's', 'p'])
    print(s)

    if user == computer :
        return 'It\'s a tie'

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'
    
    return 'you lost'

def is_win(player, opponent):
        #return true if player wins
        # r > s, s > p, p > r
        if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or \
        (player == 'p' and opponent == 'r') : return True



print(play())