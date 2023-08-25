import tkinter as tk
from tkinter import messagebox
from pyperclip import copy
from password_day_5_main import generate_pass as gen

FONT = ('Courier', 10)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, tk.END)
    random_password = gen()
    copy(random_password)
    password_entry.insert(0, random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    login = email_entry.get()
    password = password_entry.get()
    data = [website, login, password]
    if website == "" or login == "" or password == '':
        top = tk.Toplevel(window)
        top.geometry("265x100")
        top.title("Error")
        top.config(padx=20, pady=20)
        tk.Label(top, text="Please fill all the entries!", font=FONT).place(x=0, y=0)
        tk.Button(top, text="OK", command=top.destroy).place(x=100, y=35)
        return
    is_ok = messagebox.askokcancel(title=website,
                                   message=f'This are details entered: \n Login: {login} \n Password: {password}')
    if is_ok:
        with open('data.txt', encoding='utf-8', mode="a") as d:
            d.writelines(" | ".join(data) + "\n")
        top = tk.Toplevel(window)
        top.geometry("220x100")
        top.title("Saved")
        top.config(padx=20, pady=20)
        tk.Label(top, text="Your password is saved!", font=FONT).place(x=0, y=0)
        tk.Button(top, text="OK", command=top.destroy).place(x=75, y=35)
        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        return


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

website_entry = tk.Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
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
