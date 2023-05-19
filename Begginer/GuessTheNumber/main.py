import random as rnd
from art import logo

LOWER_BOUND = 1
UPPER_BOUND = 100
DIFFICULTIES_OPTION = {'easy': 10, 'hard': 5}

def generate(lower:int, upper:int)->int:
    return rnd.randint(lower, upper)

def playing_game(target:int ,tries_left:int) -> int:
    guess = None
    while (tries_left > 0) and (target != guess): 
        guess = ""
        print(f"You have {tries_left} attempts remaining to guess the number.")
        while not str(guess).isdecimal():
            guess = input ('Make a guess: ')
        tries_left -= 1
        guess = int(guess)
        if guess > target:
            print("Too high")
        elif guess < target:
            print("Too low")
    return guess





def game_loop():
    print(logo)
    print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
    """)
    number_to_guess = generate(LOWER_BOUND, UPPER_BOUND)
    difficulty = ""
    while (not difficulty in list(DIFFICULTIES_OPTION)):
        difficulty=input ("Choose a difficulty. Type 'easy' or 'hard': ") 
    tries_left = DIFFICULTIES_OPTION[difficulty]
    final_guess = playing_game(number_to_guess, tries_left)
    if final_guess == number_to_guess:
        print(f"You got it! The number was {number_to_guess}")
    else:
        print(f'You lost. The correct number was {number_to_guess}')
    

game_loop()