import random as rnd
from  drawing import *
from lwords import *
import os


print("Welcome to the Hangman!")

soluton=list(rnd.choice(word_list))
current_word=["_" for x in range(len(soluton))]
is_solved=False
progress_of_drawing=0
already_tried=[]
clear = lambda: os.system('cls')
message=["","You have already tried that letter!", "You have missed!"]
message_index=0



while (not is_solved) and (progress_of_drawing<(len(hangman_list)-1)): 
    print(hangman_list[progress_of_drawing]+"\n")
    print(" ".join(current_word)+"\n")
    
    letter = input(message[message_index]+' Guess a letter\n').lower()
    message_index=0
    if letter in already_tried:
        message_index=1
        
    else:
        already_tried.append(letter)
        is_hit=False
        for i in range(len(soluton)):
            if soluton[i]==letter:
                is_hit=True
                current_word[i]=letter
        if is_hit==False:
            progress_of_drawing+=1
            message_index=2
        is_hit=False
        if current_word==soluton:
            is_solved=True
    clear()
print(hangman_list[progress_of_drawing])
if progress_of_drawing==7:
    print('You have lost!')
else:
    print("You have won!")
print(f'The word is {"".join(soluton)}')
