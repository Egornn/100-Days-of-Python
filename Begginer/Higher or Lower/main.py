import random as rnd
from data import data
from art import logo, vs
from os import system

def game_loop():
    used_data = []


    def process_results(choice, option_1, option_2):
        is_correct = False
        if choice == 'a' and option_1['follower_count'] >= option_2['follower_count']:
            is_correct = True
        if choice == 'b' and option_1['follower_count'] <= option_2['follower_count']:
            is_correct = True
            option_1, option_2 = option_2, option_1
        return [is_correct, option_1, option_2]
        
    def get_input():
        is_input_correct = False
        while not is_input_correct:
            choice = input().lower()
            is_input_correct = choice in options
            if is_input_correct: continue
            else: print("Type the correct option")
        return choice
        
    def generate_option():
        option = None
        while not option in used_data:
            option = rnd.choice(data)
            if not option in used_data:
                used_data.append(option)
        return option

    def generate_pair(option_1: dict) -> list:    
        if option_1 == "":
            option_1 = generate_option()
        option_2 = generate_option()
        return  [option_1, option_2]

    def print_pair(option_1: dict, option_2: dict) -> None:
        # Option structure 
        # {
        #'name': 'Instagram',
        #'follower_count': 346,
        #'description': 'Social media platform',
        #'country': 'United States'
        #}
        
        system('cls')
        print(logo)
        if number_of_successes > 0:
            print(f"You're right! Current score: {number_of_successes}.")
        print(f"Compare A: {option_1['name']}, a {option_1['description']}, from {option_2['country']}.")
        print(vs)
        print(f"Compare B: {option_2['name']}, a {option_2 ['description']}, from {option_2['country']}.")
        print("Who has more followers? Type 'A' or 'B': ")
    
    is_correct = True
    number_of_successes = 0
    options = ["a", 'b']
    choice = ""
    option_1 = ""
    option_2 = ""
    
    while is_correct:
        new_pair = generate_pair(option_1)
        option_1, option_2 = new_pair[0], new_pair[1]
        used_data.append(option_1)
        used_data.append(option_2)
        print_pair(option_1, option_2)
        choice = get_input()
        results = process_results(choice, option_1, option_2)
        number_of_successes += 1
        is_correct, option_1, option_2 = results[0], results[1], results[2]
    system('cls')
    print(f"You have lost! Final score is {number_of_successes}")

    

game_loop()