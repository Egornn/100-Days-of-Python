print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print ('You\'re at a cross road. Where do you want to go? Type "left" or "right"')
is_continue = False
choice = input().lower()

while (is_continue==False): 
    if choice == 'left':
        is_continue = True
    elif choice =='right':
        print('You\'ve faced the hungry lion. You are dead')
        exit()
    else:
        choice= input('Incorrect choice. Type "left" or "right".\n').lower()
        

is_continue=False

print('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.')
choice = input().lower()

while (is_continue==False): 
    if choice == 'wait':
        is_continue=True
    elif choice =='swim':
        print('A shark ate you. You are dead')
        exit()
    else:
        choice= input('Incorrect choice. Type "wait" or "swim".\n').lower()
is_continue=False


print('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?')
choice = input().lower()
while (is_continue==False): 
    if choice == 'yellow':
        is_continue=True
    elif choice =='red':
        print('It\'s a room full of fire. You are dead')
        exit()
    elif choice == 'blue':
        print("You enter a room of beasts. You are dead")
        exit()
    else:
        choice= input('Incorrect choice. Type "red" or "yellow" or "blue".\n').lower()
is_continue=False

print('You found the treasure! You Win!')
