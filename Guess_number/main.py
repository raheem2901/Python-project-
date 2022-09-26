import random

def computer_guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number  between 1 and {x}: '))
        if guess < random_number:
            print('Sorry guess again, too low')
        elif guess > random_number:
            print('Sorry guess again too high')
    print(f"congrats!! you got the random number {random_number} correctly")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = high#could also be low b/c low is then =  high
        guess = random.randint(low, high)#random.randint would throw an error is low and high equal the same thing

        feedback = input(f'Is {guess} too high (H), too low(L) or correct(c)').lower()
        if feedback == 'h':
            high =  guess - 1
        elif feedback == 'l':
            low = guess + 1
        
    print(f'Yayy the computer guess the number {guess} correctly')


         
 
computer_guess(10)#couldbe changed to a larger set