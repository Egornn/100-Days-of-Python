import random as rnd
from  drawing import *
from lwords import *
 

print("Welcome to the Hangman!")

soluton=list(rnd.choice(word_list))
current_word=["_" for x in range(len(soluton))]
is_solved=False
progress_of_drawing=0
print(hangman_list[0])
already_tried=[]






while (not is_solved) and (progress_of_drawing<(len(hangman_list)-1)): 
    print(" ".join(current_word))
    letter = input('Guess a letter\n').lower()
    if letter in already_tried:
        print("You have already tried that letter!")
        continue
    already_tried.append(letter)
    is_hit=False
    for i in range(len(soluton)):
        if soluton[i]==letter:
            is_hit=True
            current_word[i]=letter
    if is_hit==False:
        progress_of_drawing+=1
        print('You have missed!')
        print(hangman_list[progress_of_drawing])
    is_hit=False
    if current_word==soluton:
        is_solved=True
if progress_of_drawing==7:
    print('You have lost!')
else:
    print("You have won!")
print(f'The word is {"".join(soluton)}')
