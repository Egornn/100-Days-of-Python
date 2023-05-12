import random as rnd

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")


def round_result(option1, option2):
    if option1==option2: return "That's a tie!"
    if option1-1==option2 or (option1==0 and option2==2):
        return "You\'ve won! Congratulation!"
    else: return 'You\'ve lost!'


print('Welcome to the Rock-Paper-Scissors!')
option=[rock,paper, scissors]
is_continue=True
while is_continue:
    choice = -1 + int(input("Type 1 to choose ROCK, 2 to choose PAPER, 3 to choose SCISSORS or 9 to exit: ")) 
    if choice==8:
        print('Thank you for the play!')
        is_continue=False
    elif choice >= 0 and choice < len(option) :
        print(f'You have chosen \n{option[choice]}')
        computer_choice= rnd.randint(0, len(option)-1)
        print(f'Your oponent have chosen \n{option[computer_choice]}')
        print(round_result(choice,computer_choice))
    else:
        print("Incorrect input. Try again.")

