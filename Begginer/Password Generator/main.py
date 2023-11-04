import string as st
import random as rnd

special_symbols = '!@#$%^&*()_-+='
print('Welcome to the PyPasword Generator!')
number_of_letters = int(input('How many letters would you like in your password?\n'))
number_of_symbols = int(input('How many symbols would you like in your password?\n'))
number_of_numbers = int(input('How many numbers would you like in your password?\n'))
password = ''
for letter in range(number_of_letters):
    password += rnd.choice(st.ascii_letters)
for number in range(number_of_numbers):
    password += str(rnd.randint(1, 9))
for letter in range(number_of_symbols):
    password += rnd.choice(special_symbols)
passwor_list = list(password)
rnd.shuffle(passwor_list)
password = "".join(str(x) for x in passwor_list)
print(f'Your password is {password}')
