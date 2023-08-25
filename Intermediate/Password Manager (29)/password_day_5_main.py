# Password Generator Project
import random
import string as st
import random as rnd


def generate_pass():
    letters = list(st.ascii_letters.strip())
    numbers = [str(a) for a in range(0, 10)]
    symbols = list('!@#$%^&*()_-+='.strip())
    password_list = [random.choice(letters) for ch in range(random.randint(8, 10))] + \
                    [random.choice(numbers) for nu in range(random.randint(2, 4))] + \
                    [random.choice(symbols) for sy in range(random.randint(2, 4))]
    random.shuffle(password_list)
    password = "".join(password_list)
    print(f"Your password is: {password}")
    return password


if __name__ == '__main__':
    generate_pass()
