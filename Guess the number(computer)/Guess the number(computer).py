# import random
# random.randint(a,b)
# def  function

import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0 
    while guess != random_number:
        guess = input(f'Guess a number between 1 and {x}: ')
        if guess < random.number:
            print('Sorry, guess again, Too Low. ')
        elif guess > random_number:
            print('Sorry, guess again. Too High. ')
guess(10)