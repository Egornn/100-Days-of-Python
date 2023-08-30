import tkinter as tk
from tkinter import messagebox
import pandas
import pandas as p
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
RANDOM_WORDS = []


def get_words_bank(path: str):
    try:
        data = p.read_csv('data/save.csv')
        if len(data) == 0:
            data = p.read_csv(path)
    except (FileNotFoundError, pandas.errors.EmptyDataError):
        data = p.read_csv(path)
    dictionary_list = data.to_dict(orient='records')
    return dictionary_list


def get_a_word():
    global words, flip_id, RANDOM_WORDS
    window.after_cancel(flip_id)
    if len(words) == 0:
        return
    keys = list(words[0].keys())
    language_to_learn = keys[0]
    language_to_translate = keys[1]
    RANDOM_WORDS = choice(words)
    canvas.itemconfig(canvas_word, text=RANDOM_WORDS[language_to_learn], fill='black')
    canvas.itemconfig(canvas_label, text=language_to_translate, fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_id = window.after(3000, show_translation, RANDOM_WORDS, language_to_translate)


def show_translation(random_words, language_to_translate):
    canvas.itemconfig(canvas_word, text=random_words[language_to_translate], fill="white")
    canvas.itemconfig(canvas_label, text=language_to_translate, fill="white")
    canvas.itemconfig(canvas_image, image=card_back)


def remove_word():
    global words, RANDOM_WORDS
    words.remove(RANDOM_WORDS)
    if len(words) == 0:
        messagebox.showinfo(title='All completed!', message='You have successfully learnt all the words!')
        window.destroy()
    get_a_word()


def save_data():
    global words
    pandas.DataFrame(words).to_csv("data/save.csv", index=False)
    return


words = get_words_bank('data/french_words.csv')
window = tk.Tk()
window.title('Flash Cards')
window.minsize(width=880, height=726)
window.config(background=BACKGROUND_COLOR, pady=50, padx=50)

card_back = tk.PhotoImage(file='images/card_back.png')
card_front = tk.PhotoImage(file='images/card_front.png')
right = tk.PhotoImage(file='images/right.png')
wrong = tk.PhotoImage(file='images/wrong.png')

canvas = tk.Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 268, image=card_front)
canvas_label = canvas.create_text(400, 180, text="French", font=("Ariel", 40, 'italic'))
canvas_word = canvas.create_text(400, 293, text="Trouve", font=("Ariel", 60, 'bold'))
canvas.grid(columnspan=2, row=0, column=0)

yes_button = tk.Button(image=right, highlightthickness=0, background=BACKGROUND_COLOR, command=remove_word)
no_button = tk.Button(image=wrong, highlightthickness=0, background=BACKGROUND_COLOR, command=get_a_word)
yes_button.grid(row=1, column=0)
no_button.grid(row=1, column=1)

flip_id = window.after(3000, show_translation)
get_a_word()
window.mainloop()
save_data()
