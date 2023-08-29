import tkinter as tk
from tkinter import messagebox
from pyperclip import copy
import random as random
import string as st
import json as json

FONT = ('Courier', 10)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, tk.END)
    random_password = gen()
    copy(random_password)
    password_entry.insert(0, random_password)


def gen():
    letters = list(st.ascii_letters.strip())
    numbers = [str(a) for a in range(0, 10)]
    symbols = list('!@#$%^&*()_-+='.strip())
    password_list = [random.choice(letters) for ch in range(random.randint(8, 10))] + \
                    [random.choice(numbers) for nu in range(random.randint(2, 4))] + \
                    [random.choice(symbols) for sy in range(random.randint(2, 4))]
    random.shuffle(password_list)
    password = "".join(password_list)
    return password


# ---------------------------- SAVE PASSWORD ------------------------------- #
def error_pop():
    top = tk.Toplevel(window)
    top.geometry("265x100")
    top.title("Error")
    top.config(padx=20, pady=20)
    tk.Label(top, text="Please fill all the entries!", font=FONT).place(x=0, y=0)
    tk.Button(top, text="OK", command=top.destroy).place(x=100, y=35)
    return


def saved_pop():
    top = tk.Toplevel(window)
    top.geometry("220x100")
    top.title("Saved")
    top.config(padx=20, pady=20)
    tk.Label(top, text="Your password is saved!", font=FONT).place(x=0, y=0)
    tk.Button(top, text="OK", command=top.destroy).place(x=75, y=35)
    website_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    return


def save_data():
    website = website_entry.get().lower()
    login = email_entry.get()
    password = password_entry.get()
    data = {
        website:
            {
                "email": login,
                "password": password
            }
    }

    if len(website) == 0 or len(password) == 0:
        error_pop()
    else:
        try:
            with open('data.json', encoding='utf-8', mode="r") as d:
                stored_data = json.load(d)
                stored_data.update(data)
        except FileNotFoundError:
            with open('data.json', encoding='utf-8', mode="w") as d:
                json.dump(data, d, indent=4)
        else:
            with open('data.json', encoding='utf-8', mode="w") as d:
                json.dump(stored_data, d, indent=4)
        finally:
            saved_pop()


def find_password():
    try:
        with open('data.json', encoding='utf-8', mode="r") as d:
            stored_data = json.load(d)
            if website_entry.get().lower() in stored_data:
                login = stored_data[website_entry.get().lower()]['email']
                password = stored_data[website_entry.get().lower()]['password']

    except FileNotFoundError:
        messagebox.showerror(title="Data is missing", message=f'No Data File Found')
    except KeyError:
        messagebox.showerror(title="Data is missing", message=f'No details for the website')
    else:
        messagebox.showinfo(title=website_entry.get(),
                            message=f'Login: {login} \nPassword: {password}')


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Password Manager')
canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
logo = tk.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
window.config(pady=20, padx=20)
canvas.grid(row=0, column=1)
website_label = tk.Label(text='Website:', font=FONT)
website_label.grid(row=1, column=0)
email_label = tk.Label(text='Email/Login:', font=FONT)
email_label.grid(row=2, column=0)
password_label = tk.Label(text='Password:', font=FONT)
password_label.grid(row=3, column=0)

website_entry = tk.Entry(width=33)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()
search_button = tk.Button(width=15, text="Search", command=find_password)
search_button.grid(row=1, column=2)
email_entry = tk.Entry(width=52)
email_entry.insert(tk.END, string="egornnn@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = tk.Entry(width=33)
password_entry.grid(row=3, column=1)

generate_button = tk.Button(width=15, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)
add_button = tk.Button(width=44, text='Add', highlightthickness=0, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
